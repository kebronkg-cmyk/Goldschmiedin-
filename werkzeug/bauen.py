"""Setzt Bilder, Galerien und Zeichen in die Seiten. Beliebig oft ausführbar.

Aufruf:  python3 werkzeug/bauen.py

1. <img data-bild="name" …> bekommt src, srcset, width, height aus bilder/mass.json.
2. Zwischen <!-- galerie:x --> und <!-- /galerie:x --> entsteht die Galerie x.
3. Zwischen <!-- zeichen --> … und <!-- unterschrift:schreibt --> … stehen
   Unterschrift und „Miku“ aus werkzeug/zeichen.json.

Bildangaben stammen wörtlich von der alten Seite (Material, Feingehalt);
{750} wird zur Punze. Nur bestätigte Angaben eintragen.
"""
import html, json, pathlib, re

WURZEL = pathlib.Path(__file__).resolve().parent.parent
MASS = json.loads((WURZEL / "bilder" / "mass.json").read_text())
ZEICHEN = json.loads((WURZEL / "werkzeug" / "zeichen.json").read_text())
SEITEN = ["index.html", "impressum.html", "datenschutz.html"]

# (bild, Stein / Titel, Metall mit {Punze}, Alternativtext)
GALERIEN = {
    "ringe": [
        ("mantelring", "Mantelring", "Feinsilber, Gold {900}, Palladium {500}", "Breiter Mantelring aus Feinsilber mit einem Band aus Gold, auf einem Holzbrett"),
        ("citrin-ring", "Citrin", "Gold {750}", "Goldring mit großem, facettiertem Citrin zwischen Blättern und gelben Blüten"),
        ("opal-ring", "Black Opal, Lightning Ridge", "Gold {900}", "Goldring mit schwarzem Opal, der rot und blau schimmert"),
        ("amethyst-ring", "Amethyst im Onion Cut", "Silber {925}", "Silberring mit einem Amethyst im Zwiebelschliff, in einer Schale gefasst"),
        ("brillant-ring-bicolor", "Brillanten 0,12 ct tw-si", "Weißgold, Gelbgold {750}", "Ring in Weiß- und Gelbgold mit einer Reihe Brillanten, auf Moos"),
        ("lapis-ring", "Lapislazuli", "Gold {750}", "Breiter Goldring mit eingelegten Quadraten aus Lapislazuli"),
        ("brillant-ring-quadrat", "Brillanten, weiß bis light brown", "Gold {750}", "Quadratischer Goldring mit Brillanten in Weiß und hellem Braun"),
        ("brillant-ring-pave", "Brillanten 0,2 ct tw-si", "Gold {750}", "Ring mit zwei rautenförmigen Flächen voller Brillanten, auf einem Blatt"),
    ],
    "ohrschmuck": [
        ("brillant-ohrstecker", "Brillanten 0,26 ct", "Gold {900}", "Runde Ohrstecker aus strukturiertem Gold mit Brillant, auf Sand zwischen Muscheln"),
        ("lapis-malachit-ohrstecker", "Lapislazuli, Malachit", "Gold {900}", "Quadratische Goldohrstecker mit einem Mosaik aus Lapislazuli und Malachit"),
        ("amethyst-ohrhaenger", "Grüner Amethyst", "Gold {750}", "Goldene Ohrhänger mit grünen Amethysten im Navetteschliff"),
        ("samenkapsel-ohrstecker", "Samenkapseln", "Silber, Gold {750}", "Silberne Ohrstecker in Form gedrehter Samenkapseln, auf einem Blatt"),
        ("quarz-ohrhaenger", "Einschlussquarze", "Silber, Gold {750}", "Rechteckige Ohrhänger mit Einschlussquarzen, an einem Zweig hängend"),
        ("bernstein-ohrstecker", "Roter Bernstein, behandelt", "Silber {925}", "Mattsilberne Ohrstecker in Schalenform mit rotem Bernstein, auf Treibholz"),
        ("citrin-ohrhaenger", "Citrin, Keramik", "Gold {900}", "Ohrhänger aus Keramik mit Goldmuster und Citrin, auf einem türkisfarbenen Stein"),
    ],
    "halsschmuck": [
        ("glas-kette", "Spinell, Onyx, Perlen, handgearbeitetes Glas", "", "Kette aus feinen Drähten mit einem roten Glasanhänger, auf Treibholz"),
        ("aquamarin-anhaenger", "Aquamarin an Perlrochenleder", "Rotgold, Weißgold {750}", "Quadratischer Aquamarin-Anhänger an einem Band aus Perlrochenleder"),
        ("keramik-kette", "Keramik", "Gold {900}", "Gliederkette aus Keramikquadraten in Goldfassungen, auf Holz"),
        ("bernstein-kette", "Grüner Bernstein", "Gold {900}", "Fächer aus feinen Drähten mit einem Anhänger aus grünem Bernstein"),
        ("turmalin-anhaenger", "Rote Turmalinscheibe", "Silber {925}", "Anhänger mit einer roten Turmalinscheibe an einer Silberkette, im Gras"),
        ("opal-anhaenger", "Boulderopale", "Gold {900}", "Zwei Boulderopale an einer Goldkette, auf einem türkisfarbenen Stein"),
    ],
    "perlen": [
        ("barockperlen", "Süßwasserperlen, Fancy-Tropfen 19–25 mm, Zirkone", "Gold", "Kette aus großen, unregelmäßig geformten Süßwasserperlen auf dunklem Grund"),
        ("perlen-reihen", "Süßwasserperlen", "", "Mehrreihiger Halsschmuck aus weißen, rosé und grauen Süßwasserperlen"),
        ("keshi-perlen", "Keshi-Perlen 14–16 mm", "goldplattierte Zwischenteile", "Kette aus Keshi-Perlen mit goldenen Zwischenteilen"),
    ],
    "broschen": [
        ("turmalin-brosche", "Turmalin", "Palladium {500}, Feinsilber, Gold", "Runde Brosche aus Palladium mit Feinsilber-Tropfen und einem rosa Turmalin"),
        ("chip-brosche", "Computerelement", "Silber, teilweise Goldauflage", "Brosche aus Silber mit Goldauflage und einem Computerbauteil"),
        ("chrysokoll-brosche", "Chrysokoll, Goldstaub", "Palladium {500}", "Blattförmige Brosche mit Chrysokoll und Goldstaub, auf blauer Seide"),
    ],
}


def bildattrs(name, sizes=None):
    m = MASS[name]
    breiten = [w for w in m["breiten"] if w <= 1800]
    src = f"bilder/{name}-{min(breiten, key=lambda w: abs(w - 800))}.webp"
    srcset = ", ".join(f"bilder/{name}-{w}.webp {w}w" for w in breiten)
    return {"src": src, "srcset": srcset, "width": str(m["b"]), "height": str(m["h"])}, f"bilder/{name}-{max(breiten)}.webp"


def punzen(text):
    return re.sub(r"\{(\w+)\}", r'<b class="punze">\1</b>', html.escape(text))


def galerie(name):
    zeilen = [f'<ul class="galerie" data-galerie="{name}">']
    for bild, stein, metall, alt in GALERIEN[name]:
        a, gross = bildattrs(bild)
        sizes = "(min-width: 60em) 24rem, (min-width: 40em) 31vw, 46vw" if name != "steine" else "(min-width: 60em) 40vw, 92vw"
        metall_html = f'\n      <span class="etikett-metall">{punzen(metall)}</span>' if metall else ""
        zeilen.append(f'''  <li class="stueck">
    <button class="stueck-bild" type="button" data-gross="{gross}"><img src="{a['src']}" srcset="{a['srcset']}" sizes="{sizes}" width="{a['width']}" height="{a['height']}" loading="lazy" alt="{html.escape(alt)}"></button>
    <p class="etikett fundzettel"><span class="etikett-stein">{html.escape(stein)}</span>{metall_html}</p>
  </li>''')
    zeilen.append("</ul>")
    return "\n".join(zeilen)


def sprite():
    u, m = ZEICHEN["unterschrift"], ZEICHEN["miku"]
    return (f'<svg class="sprite" width="0" height="0" aria-hidden="true">'
            f'<symbol id="unterschrift" viewBox="{u["viewBox"]}"><path d="{u["d"]}"/></symbol>'
            f'<symbol id="miku" viewBox="{m["viewBox"]}"><path d="{m["d"]}"/></symbol></svg>')


def schreibt():
    """Unterschrift, die sich schreibt: Maske aus der Mittellinie, Zug für Zug."""
    u = ZEICHEN["unterschrift"]
    gesamt = sum(z["l"] for z in u["zuege"])
    dauer, t, pfade = 2.6, 0.0, []
    for z in u["zuege"]:
        d = max(0.04, dauer * z["l"] / gesamt)
        pfade.append(f'<path pathLength="1" style="--v:{t:.2f}s;--t:{d:.2f}s" d="{z["d"]}"/>')
        t += d
    return (f'<svg class="unterschrift unterschrift-gross auftritt" viewBox="{u["viewBox"]}" role="img" aria-label="Michaela Kusche">'
            f'<defs><mask id="schreibmaske" maskUnits="userSpaceOnUse" x="-4" y="-4" width="308" height="49">'
            f'<g class="schreibzuege" fill="none" stroke="#fff" stroke-width="3.8" stroke-linecap="round" stroke-linejoin="round">'
            + "".join(pfade) +
            f'</g></mask></defs><use href="#unterschrift" mask="url(#schreibmaske)"/></svg>')


def feder(name):
    """Ihr Name in ruhiger Schreibschrift (Corinthia), Zug für Zug geschrieben.

    Sichtbar ist der echte Umriss der Schrift mit Haar- und Schattenstrichen; freigelegt
    wird er durch eine Maske aus der Mittellinie (Klasse .zug, mit --v Beginn und --t Dauer).
    Tempo aus der gemessenen Länge, kleine Pause, wo die Feder absetzt. Wann geschrieben
    wird, entscheidet das CSS (Klasse .schreibt). Der Probierstein liest dieselben Züge.
    """
    z = ZEICHEN["schriftzug"]
    tempo = 330.0  # Einheiten der viewBox pro Sekunde (≈ 4,5 s für den ganzen Namen)
    t, pfade, letzt_x = 0.0, [], None
    for zug in z["feder"]:
        if letzt_x is not None and zug["x"] - letzt_x > 9:
            t += 0.22  # Feder setzt ab
        d = max(0.12, zug["l"] / tempo)
        pfade.append(f'<path class="zug" pathLength="1" style="--v:{t:.2f}s;--t:{d:.2f}s" d="{zug["d"]}"/>')
        t += d * 0.92
        letzt_x = min(zug["x"], 9000) + 4
    mid = f"zugmaske-{name}"
    return (f'<svg class="feder feder-{name}" viewBox="{z["viewBox"]}" role="img" aria-label="Michaela Kusche" data-dauer="{t:.2f}">'
            f'<defs><mask id="{mid}" maskUnits="userSpaceOnUse">'
            f'<g fill="none" stroke="#fff" stroke-width="{z["maskenbreite"]}" stroke-linecap="round" stroke-linejoin="round">'
            + "".join(pfade) +
            f'</g></mask></defs><path class="umriss" d="{z["d"]}" mask="url(#{mid})"/></svg>')

def zwischen(s, marke, inhalt):
    muster = re.compile(rf"(<!-- {re.escape(marke)} -->).*?(<!-- /{re.escape(marke)} -->)", re.S)
    if not muster.search(s):
        return s
    return muster.sub(lambda m: m.group(1) + inhalt + m.group(2), s)


def img_fuellen(s):
    def ersetze(m):
        tag = m.group(0)
        name = re.search(r'data-bild="([^"]+)"', tag).group(1)
        a, _ = bildattrs(name)
        for k, v in a.items():
            if re.search(rf'\s{k}="[^"]*"', tag):
                tag = re.sub(rf'(\s){k}="[^"]*"', rf'\g<1>{k}="{v}"', tag)
            else:
                tag = tag.replace(f'data-bild="{name}"', f'data-bild="{name}" {k}="{v}"', 1)
        return tag
    return re.sub(r"<img\b[^>]*\bdata-bild=\"[^\"]+\"[^>]*>", ersetze, s)


def main():
    for seite in SEITEN:
        pfad = WURZEL / seite
        if not pfad.exists():
            continue
        s = pfad.read_text()
        s = zwischen(s, "zeichen", sprite())
        s = zwischen(s, "unterschrift:schreibt", schreibt())
        for name in ("auftakt", "gruss", "fuss"):
            s = zwischen(s, f"feder:{name}", feder(name))
        for name in GALERIEN:
            s = zwischen(s, f"galerie:{name}", "\n" + galerie(name) + "\n")
        s = img_fuellen(s)
        pfad.write_text(s)
        print("gebaut:", seite)


if __name__ == "__main__":
    main()
