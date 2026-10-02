"""Bereitet die Fotos der alten Seite für die neue auf.

Aufruf:  python3 werkzeug/bilder.py <ordner-mit-originalen>

Der Ordner enthält die Originale von michaela-kusche.de/media/… mit
„__“ statt „/“ im Namen (so lädt sie werkzeug/README.md herunter).
Jedes Bild wird nie über seine Vorlage gezogen: Breiten über der
Originalbreite entfallen.
"""
import json, sys, pathlib
from PIL import Image, ImageOps

QUELLE = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "quelle")
ZIEL = pathlib.Path(__file__).resolve().parent.parent / "bilder"
BREITEN = (480, 800, 1200, 1800)

# name: (datei, beschnitt (l, o, r, u) oder None)
BILDER = {
    # Auftakt
    "disthen-brosche": ("media__Broschen__b2.jpg", None),
    # Ringe
    "mantelring": ("media__Ringe__r13.jpg", None),
    "citrin-ring": ("media__Ringe__goldschmiedin_michaela_kusche_ring1a.jpg", None),
    "opal-ring": ("media__Ringe__goldschmiedin_michaela_kusche_ring4a.jpg", None),
    "amethyst-ring": ("media__Ringe__r14.jpg", None),
    "lapis-ring": ("media__Ringe__r12.jpg", None),
    "brillant-ring-bicolor": ("media__Ringe__r8.jpg", None),
    "brillant-ring-pave": ("media__Ringe__r2.JPG", None),
    "brillant-ring-quadrat": ("media__Ringe__goldschmiedin_michaela_kusche_ring3a.jpg", None),
    # Ohrschmuck
    "brillant-ohrstecker": ("media__Ohrschmuck__goldschmiedin_michaela_kusche_ohrschmuck1a.jpg", None),
    "lapis-malachit-ohrstecker": ("media__Ohrschmuck__goldschmiedin_michaela_kusche_ohrschmuck3a.jpg", None),
    "samenkapsel-ohrstecker": ("media__Ohrschmuck__goldschmiedin_michaela_kusche_ohrschmuck4a.jpg", None),
    "amethyst-ohrhaenger": ("media__Ohrschmuck__goldschmiedin_michaela_kusche_ohrschmuck7a.jpg", None),
    "quarz-ohrhaenger": ("media__Ohrschmuck__goldschmiedin_michaela_kusche_ohrschmuck9a.jpg", None),
    "bernstein-ohrstecker": ("media__Ohrschmuck__goldschmiedin_michaela_kusche11a.jpg", None),
    "citrin-ohrhaenger": ("media__Ohrschmuck__goldschmiedin_michaela_kusche_ohrschmuck12a.jpg", None),
    # Halsschmuck
    "glas-kette": ("media__Ketten__michaela_kusche_k10.jpg", None),
    "keramik-kette": ("media__Ketten__michaela_kusche_k11.jpg", None),
    "aquamarin-anhaenger": ("media__Anhaenger__a5.jpg", None),
    "turmalin-anhaenger": ("media__Anhaenger__goldschmiedin_michaela_kusche_anhanger2a.jpg", None),
    "opal-anhaenger": ("media__Anhaenger__a7.jpg", None),
    "bernstein-kette": ("media__Ketten__Michaela_Kusche__1_gruener_Bernstein.JPG", None),
    # Perlen
    "barockperlen": ("media__Perlen__p5.JPG", None),
    "perlen-reihen": ("media__Perlen__p4.JPG", None),
    "keshi-perlen": ("media__Perlen__p3.JPG", None),
    # Broschen
    "turmalin-brosche": ("media__Broschen__b1.JPG", None),
    "chrysokoll-brosche": ("media__Broschen__b6.jpg", None),
    "chip-brosche": ("media__Broschen__b3.jpg", None),
    # Edelsteine
    "steine-opale": ("media__Edelsteine__goldschmiedin_michaela_kusche_edelsteine3.jpg", None),
    "steine-farben": ("media__Edelsteine__goldschmiedin_michaela_kusche_edelsteine2.jpg", None),
    # Inspiration — Krokodil auf das Format der Hand-Aufnahme (862 × 800) gebracht,
    # nur Flechte und Grund am Rand fallen weg
    "krokodilring-ast": ("media__topics-pictures__zoom__michaela_kusche_schmuck_krokoring_3.jpg", (100, 0, 1630, 1420)),
    "krokodilring-hand": ("media__Krokodilring__Michaela_Kusche_Schmuck_Krokoring.jpg", None),
    "fede-ring": ("media__topics-pictures__zoom__michaela_kusche_schmuck_fede_ring.jpg", None),
    "samenkapseln": ("media__topics-pictures__zoom__ohrringe-samen_mcp0012.jpg", None),
    "mayakoenige": ("media__topics-pictures__zoom__michaela_kusche_ohrschmuck_mayakoenige.jpg", None),
    "froesche": ("media__topics-pictures__zoom__michaela_kusche_schmuck_froschohrringe_1.jpg", None),
    # Werkstatt
    "portraet": ("media__Portrait__goldschmiedin_michaela_kusche.jpg", None),
    "werkbrett": ("media__Geschaeft-Laden__goldschmiedin_michaela_kusche_werkstatt1.jpg", None),
    "werkzeug": ("media__Geschaeft-Laden__goldschmiedin_michaela_kusche_werkstatt2.jpg", None),
    "laden": ("media__Geschaeft-Laden__goldschmiedin_michaela_kusche_laden2.jpg", None),
    "eheringe-ebenholz": ("media__Ringe__e2.jpg", None),
}

def main():
    ZIEL.mkdir(exist_ok=True)
    mass = {}
    for name, (datei, beschnitt) in BILDER.items():
        bild = ImageOps.exif_transpose(Image.open(QUELLE / datei)).convert("RGB")
        if beschnitt:
            bild = bild.crop(beschnitt)
        b, h = bild.size
        breiten = [w for w in BREITEN if w < b] + [min(b, BREITEN[-1])]
        if name == "disthen-brosche":
            breiten.append(min(b, 3200))  # Vorlage für die Lupe
        breiten = sorted(set(breiten))
        for w in breiten:
            klein = bild if w == b else bild.resize((w, round(h * w / b)), Image.LANCZOS)
            klein.save(ZIEL / f"{name}-{w}.webp", "WEBP", quality=80, method=6)
        mass[name] = {"b": b, "h": h, "breiten": breiten}
    (ZIEL / "mass.json").write_text(json.dumps(mass, indent=1))
    print(len(mass), "Bilder")

if __name__ == "__main__":
    main()
