# Design-Erbe für die Website der Goldschmiedin Michaela Kusche

Stand 02.10.2026. Dieses Dokument bringt alles mit, was aus den bisherigen
Projekten (zwei Friseursalons, ein Restaurant) für eine neue Website von
**michaela-kusche.de** brauchbar ist: Grundsätze, Bauteile mit Code,
Prüfwege, Fallen — dazu die Recherche der bestehenden Seite.

**Es ist keine Vorlage zum Umfärben.** Übertragen wird die Arbeitsweise und
das Handwerk. Palette, Schrift, Bildsprache und die eigene Idee entstehen neu
aus ihrer Werkstatt, ihrem Schmuck und ihr selbst. Wo unten ein Bauteil mit
Code steht, ist der Code das *Muster* (Technik, Zugänglichkeit, Bewegung),
nicht das Aussehen.

In die Wurzel des Goldschmiedin-Repos legen. Wer den ganzen Werkzeugkasten
will (Skills, Prüfskripte, Workflow), kopiert zusätzlich `.claude/`,
`.github/workflows/deploy-pages.yml` und `CLAUDE.md` aus dem Repo
*Die-Friseure-* — siehe dort `NEUER-SALON.md`.

---

## 1. Was die bestehende Seite hergibt (Recherche)

Alle Angaben von michaela-kusche.de, gelesen am 02.10.2026. Vor dem Bauen
bestätigen lassen (Abschnitt 8).

### Fakten

| | |
|---|---|
| Name | Goldschmiedin Michaela Kusche |
| Anschrift | Bachbauernstraße 5, 81241 München (Pasing), drei Gehminuten vom Pasinger Bahnhof |
| Telefon | 089 / 41 85 88 65 |
| E-Mail | hallo@michaela-kusche.de |
| Öffnungszeiten | Mi–Fr 11:30–18:30, Sa 10:30–14:00, „und gerne nach Vereinbarung“ |
| Seit | 2008 Geschäft „im Herzen von Pasing“ |
| Werkstatt | direkt im Laden — „So haben Sie Gelegenheit, mitzuerleben, wie Ihr Schmuckstück entsteht.“ |
| Material | Unikatschmuck in Silber, **mattiertem Gelbgold**, Weißgold, Rotgold, Palladium, Platin; Perlen, Brillanten, Perlrochenleder, Ebenholz, Keramik, Kautschuk, Glas |
| Leistungen | Unikate, Eheringe, Männerschmuck, Restaurierungen, Ohrschmuck individuell angepasst |
| Edelsteine | „Meine Leidenschaft sind Edelsteine in außergewöhnlichen Farben und Fantasieschliffen.“ Große Sammlung zur Auswahl in Ruhe; Schleifer aus Brasilien, Australien, Idar-Oberstein |
| Nachhaltigkeit | Recyclinggold in der Werkstatt; Ringe auch aus Fairtrade-Gold; Sponsorin von mercuryfreemining.org (Toby Pomeroy) |
| Webdesign bisher | chekka.de, Vorlage „miku_2014“ |

### Gliederung der alten Seite

Home · Ringe · Ohrschmuck · Halsschmuck (Ketten, Anhänger, Perlen) ·
Broschen · Edelsteine · Inspiration · Werkstatt · Faires Gold · Anfahrt ·
Impressum / Datenschutz / Haftungsausschluss.

### Ihre Stimme (wörtlich, zum Weitertragen)

- „Schmuck für ganz besondere Menschen!“
- „Schmuck ist Ausdruck unserer Persönlichkeit und Zeichen unserer Kultur.“
- „Ich freue mich darauf, Sie kennen zu lernen!“
- Der Dreischritt der Startseite: **Auswählen · Kombinieren · Bearbeiten**
  von edlen Metallen, edlen Steinen, Naturstoffen, experimentellen Stoffen —
  mit Erfahrung, einfühlsamer Beratung, Liebe zur Arbeit und zum Detail,
  handwerklicher Perfektion, künstlerischem Geschick — „wird in meiner
  Werkstatt Ihr Schmucktraum Wirklichkeit!“
- Inspiration von Reisen: „besondere Details und alte, traditionelle Formen“
  — FEDE-Ring, Krokodilring (aus Thailand, beweglich), Samenkapseln
  (Karibikküste Guatemalas), Mayakönige und Frösche in schwarzer Jade.
- Spricht per **Sie**, in der Ich-Form. Die Person ist die Marke.

### Bildbestand (gemessen)

| Gruppe | Anzahl | Größe | Befund |
|---|---|---|---|
| Ringe, Ohrschmuck, Ketten, Anhänger, Perlen | ~70 | meist 1066 × 800, einige 600 × 800 hoch | echte Stücke, aber **jeder auf anderem Grund** (Blatt, Moos, Holz, Stein, bunter Karton, Rosenblüte) |
| Broschen | 6 | bis 3872 × 2592 | die schärfsten Aufnahmen |
| Inspiration (Zoom) | 5 | 1084–1764 breit | Krokodilring auf Flechte, Samenkapseln — gut |
| Werkstatt, Laden | 3 | **375–400 px** | zu klein für mehr als eine Kachel |
| Porträt | 1 | **243 × 338** | zu klein für den ersten Bildschirm |
| Unterschrift | 1 | 300 × 41, PNG | ihre echte Handschrift — wertvoll |
| Logo „Miku“ | 1 | 148 × 60, PNG | Handschrift-Kürzel |

Folgerungen:

- **Neue Fotos sind der größte Hebel.** Ein Porträt in der Werkstatt (am
  Brett, mit Lupe), drei, vier Werkstattbilder, und die Stücke auf
  *einheitlichem* Grund. Bis dahin: kein Bild über seine Vorlage ziehen,
  das Porträt bleibt klein, und die Startseite trägt ein Schmuckstück statt
  der Person — mit dem fehlenden Porträt als Punkt 1 der Abnahme.
- Die bunten Hintergründe nicht nachträglich „vereinheitlichen“ durch
  Freistellen mit Kreismaske o. Ä. — das wirkt billiger als das Original.
  Lieber auswählen: die Stücke auf Naturgrund (Holz, Stein, Flechte, Muschel)
  passen zusammen und zu ihrer Reise-Inspiration; die auf Karton weglassen.
- Die alte Seite lädt Google Fonts von Google (abmahnfähig, LG München I,
  3 O 17493/20) — die neue Seite hostet Schriften selbst.

---

## 2. Grundsätze, die übertragen werden

Aus den bisherigen Projekten, jedes Mal gemessen oder einmal schiefgegangen.

1. **Die Atmosphäre kommt aus dem Laden, nicht aus einer Vorlage.** Palette,
   Schrift, Bildsprache aus den echten Fotos, dem Material, dem Licht. Erst
   schauen, dann festlegen. *Prüftest für die Leitfarbe:* Gehört sie ihr
   oder einem Lieferanten / einem Klischee?
2. **Gold auf Schwarz ist hier die naheliegende Falle.** Es war die Antwort
   für ein Restaurant und für ein nächtliches Friseurschaufenster — für eine
   Goldschmiedin, deren Hausmaterial *mattiertes* Gelbgold ist, wäre es das
   Branchenklischee. Glanz und Spiegelung sind nicht ihre Handschrift; das
   Matte, Gebürstete, die Farbsteine sind es.
3. **Die Person im ersten Bildschirm**, sobald es ein brauchbares Porträt
   gibt. Bei einem inhabergeführten Handwerk kaufen die Leute die Person.
4. **Eine eigene Idee pro Seite**, die es sonst nirgends gibt, aus ihrem
   Material — und sie muss **klein funktionieren**. Was nur groß wirkt, ist
   ein Schaustück. Kandidaten in Abschnitt 4.
5. **Eine zweite Farbe tritt nur als Ornament auf, nie als Textfarbe.**
6. **Zurückhaltung beim Ornament.** Wenige Einsätze, an Stellen, wo sie
   etwas bedeuten. Zurücknehmen ist schwerer als nachlegen.
7. **Echte Inhalte.** Keine Platzhalter, kein Blindtext, keine Werbeaussage
   ohne Beleg („Premium“, „nachhaltig zertifiziert“ nur, wenn es stimmt).
   Ihre eigenen Sätze tragen weiter als neue Werbezeilen — und sie sind belegt.
8. **Bildauswahl ist Gestaltung.** Lieber acht saubere Bilder als zwölf, von
   denen vier schaden. Kein Bild über seine Vorlage gezogen. Dasselbe Foto
   nie zweimal auf einer Seite. Fotos anklickbar, aber ohne Symbol und ohne
   Text auf der Kachel.
9. **Der Rahmen gibt nicht das Format vor, die Aufnahme tut es.** Ein
   erzwungenes `aspect-ratio` + `object-fit: cover` schneidet einem
   Hochformat genau das Schmuckstück weg. Hoch- und Querformate gemischt
   setzen (Mauerwerk-Raster), nicht beschneiden.
10. **Das Handy ist keine gestapelte Desktop-Seite.** Eigene Komposition:
    erster Bildschirm als Bild, genau ein leuchtender Knopf, das Anschauliche
    vor dem Text, Reihen zum Wischen statt Säulen, Vorschauen statt Listen.
    Desktop und Tablet dabei unverändert — gemessen, nicht angenommen.
11. **Eine Lampe pro Knopfgruppe.** Nur der Hauptknopf hebt sich ab.
12. **Telefonnummer schon auf dem ersten Bildschirm.** Impressum und
    Datenschutz als eigene Seiten, Copyright in den Fuß.
13. **Verbesserung wird gemessen, alt gegen neu:** Wörter im ersten
    Bildschirm, Höhe je Abschnitt, Abstand bis zum ersten Bild, Anzahl
    Kästen, Verhältnis Überschrift : Text. Wird eine Zahl schlechter, wird
    nachgebessert, bevor es „fertig“ heißt.

### Bewegung

- Nur `ease-out`-Kurven, kein Federn, kein Zurückschwingen.
- Nur `transform` und `opacity` animieren, nie Layout-Eigenschaften.
- Hover hinter `@media (hover: hover) and (pointer: fine)`.
- `prefers-reduced-motion` immer bedienen; was ruhend sinnlos ist, ganz aus.
- Dauern 0,3–0,9 s; Endlosschleifen deutlich langsamer.
- Höchstens drei Bewegungen gleichzeitig; der Rest ~90 ms später.
- Auftritt bremst aus, Abgang beschleunigt.
- Eine Kamerafahrt fährt heran, nicht heraus (am Rand stehen die Dinge, die
  nicht ins Bild sollen).

### Technik

- Statisch: HTML, CSS, Vanilla JS. Kein Build, keine Abhängigkeiten, keine
  CDNs, Schriften (OFL) im Repo, `font-display: swap`, Preload der zwei
  wichtigsten. GitHub Pages deployt bei jedem Push; danach die Live-URL
  abfragen, bis die Änderung wirklich da ist.
- **Jeder Gestaltungswert ist ein Token in `:root`.** Alpha-Stufen aus dem
  Token über `color-mix`, nie als Rohwert.

---

## 3. Bauteile — bewertet für eine Goldschmiede

| Bauteil | Herkunft | Hier brauchbar? | Übertragung |
|---|---|---|---|
| Token-System (oklch + `color-mix`) | alle | **ja** | 3.1 |
| Schild + Handschrift als Überschrift | Irmonhair | **ja, mit ihrer echten Unterschrift** | 3.2 |
| Ornament aus einer Vorlage nachzeichnen, Generator mit Marken | Irmonhair (Schleife) | **ja: Unterschrift und „Miku“ als SVG** | 3.3 |
| Wechsel an derselben Stelle (gestapelte Ebenen, Überblendung) | Irmonhair (Spiegel-Adresse) | **ja: Stück ↔ Detail, Vorder- ↔ Rückseite** | 3.4 |
| Etiketten auf einer Ablage | Die Friseure (Preisetiketten) | **ja: Hängeetikett mit Material/Feingehalt** | 3.5 |
| Galerie mit Ansicht, Blättern, Esc, Fokus zurück | beide | **ja, Kern der Seite** | 3.6 |
| Leiste weicht beim Runterscrollen aus | beide | ja | 3.7 |
| Kapitelname in der Leiste (wo bin ich?) | Irmonhair Fenster | ja, ab Tablet | 3.8 |
| „Heute geöffnet?“ in Münchner Zeit | Die Friseure | **ja — ihre Zeiten sind ungewöhnlich** | 3.9 |
| Nachrichten-Baukasten statt Warenkorb | Irmonhair (Extensions → WhatsApp) | **ja: Anfrage für ein Unikat / Eheringe** | 3.10 |
| Vollflächiges Foto, Schleier nur hinter dem Text | beide | erst mit neuen Werkstattfotos | 3.11 |
| Lichtkante als Hauptknopf, LED-Fuge | Irmonhair Fenster | **nein** — Nacht-/Schaufensterwelt, nicht ihre |
| Drehendes Nasenschild (Salonwahl) | Die Friseure | nein (ein Laden) — aber die Idee „Vorder-/Rückseite“ lebt in 3.4 |
| Preisliste aus Buchungsdienst, Längenwahl | beide Salons | nein — Unikate haben keine Liste. Höchstens Eheringe „ab“ nach Bestätigung |
| Limettengrün, Archivo, Jost/Cormorant, Schleife, Gold auf Schwarz | — | **nein** — gehören anderen Läden |

### 3.1 Token-System

```css
:root {
  /* Farben — aus IHREN Fotos messen (Abschnitt 5), nicht diese Werte nehmen */
  --grund: oklch(97% 0.004 80);
  --tinte: oklch(26% 0.01 60);
  --tinte-leise: oklch(46% 0.01 60);        /* Nebentext, ≥ 4.5:1 messen */
  --metall: oklch(78% 0.06 85);             /* mattes Gelbgold: Ornament, nie Text */
  --linie: color-mix(in oklch, var(--tinte) 14%, transparent);
  --linie-stark: color-mix(in oklch, var(--tinte) 32%, transparent);

  --kurve: cubic-bezier(0.22, 1, 0.36, 1);       /* ease-out */
  --kurve-ab: cubic-bezier(0.55, 0, 1, 0.45);    /* Abgang beschleunigt */
  --dauer: 0.45s;

  --rand: clamp(1rem, 0.5rem + 2.5vw, 2.5rem);
  --breite: 76rem;
}
[hidden] { display: none !important; }
html { -webkit-text-size-adjust: 100%; text-size-adjust: 100%; }
.mitte { width: min(100% - 2 * var(--rand), var(--breite)); margin-inline: auto; }
```

Ein Token, dessen Name sich mit „auf X“ ergänzen lässt (`--text-auf-gold`),
trägt zwei Aufgaben — entzweien, bevor eine dunkle Variante kommt.

### 3.2 Schild und Handschrift

Bei Irmonhair sprach der Laden in gesperrten Versalien und Schreibschrift,
also sprachen die Überschriften genauso: ein Wort als Schild, darunter eine
Zeile Handschrift. Bei der Goldschmiedin gibt es die Handschrift **echt** —
ihre Unterschrift und das „Miku“. Keine Schreibschrift-Webfont dafür
nehmen (die alte Seite lädt „Satisfy“), sondern ihre Linie als SVG (3.3).

```html
<h2 class="schild">Ringe</h2>
<p class="handschrift-zeile" aria-hidden="true"><!-- Ausschnitt ihrer Unterschrift als SVG --></p>
```

```css
.schild { letter-spacing: .28em; text-transform: uppercase; font-weight: 500; }
.schild::after { content: ""; display: block; width: 2.5rem; height: 1px;
  margin-top: .8rem; background: var(--metall); }
```

Sparsam: Die Handschrift steht an zwei, drei Stellen (Auftakt, Gruß vor dem
Kontakt, Fuß), nicht unter jeder Überschrift.

### 3.3 Ornament aus einer Vorlage — Unterschrift als Linie

Methode aus der Irmonhair-Schleife, übertragen:

1. Die Vorlage (`michaela-kusche-unterschrift.png`, 300 × 41) **im
   Koordinatenraum der Vorlage** nachzeichnen (`viewBox="0 0 300 41"`).
   Besser: sie um eine größere Aufnahme bitten (Papier, schwarzer Stift,
   Foto von oben) — 300 px sind wenig. Nebeneinander rendern und
   vergleichen, bis die Linie stimmt.
2. Als **ein Strich** anlegen, damit sie sich schreiben lässt:

```html
<svg class="unterschrift" viewBox="0 0 300 41" aria-hidden="true">
  <path d="…" pathLength="1" fill="none" stroke="currentColor" stroke-width="1.6"
        stroke-linecap="round" stroke-linejoin="round"/>
</svg>
```

```css
.unterschrift path { stroke-dasharray: 1; stroke-dashoffset: 1;
  animation: schreiben 1.6s var(--kurve) .3s forwards; }
@keyframes schreiben { to { stroke-dashoffset: 0; } }
@media (prefers-reduced-motion: reduce) {
  .unterschrift path { animation: none; stroke-dashoffset: 0; }
}
```

3. **Ein Generator, mehrere Einsätze** (Python schreibt den Pfad zwischen
   Marken `<!-- unterschrift:gross -->` in alle Seiten): Auftakt, Gruß,
   Fuß, Favicon (dort nur „Miku“). Jede Inline-Kopie bekommt ein eigenes
   ID-Präfix, falls Verläufe oder Masken drin sind.
4. Farbe am SVG-Element (`stroke` als Attribut oder `currentColor`), Breite
   und Animation im CSS — CSS-`stroke` überschreibt das Attribut.
5. Ein Zeichen in 40 px ist ein Ausschnitt, keine Verkleinerung: fürs
   Favicon nur das „M“ oder „Miku“.

### 3.4 Wechsel an derselben Stelle

Aus dem Irmonhair-Spiegel: Zwei Inhalte liegen gestapelt in derselben
Rasterzelle, nur einer ist sichtbar, der Wechsel blendet über — nichts
springt. Für die Goldschmiede: **Stück am Körper ↔ Detail**, **Ring von
vorn ↔ Innenseite**, **Rohstein ↔ gefasst**.

```html
<figure class="wechsel" data-zeigt="a">
  <img data-seite="a" src="…" alt="FEDE-Ring geschlossen: zwei gefasste Hände">
  <img data-seite="b" src="…" alt="FEDE-Ring geöffnet: die Hände geben das Herz frei">
  <button type="button" class="wechsel-knopf" aria-pressed="false">Hände öffnen</button>
</figure>
```

```css
.wechsel { display: grid; }
.wechsel > img { grid-area: 1 / 1; opacity: 0; visibility: hidden;
  transition: opacity .22s ease-in, visibility 0s linear .22s; }       /* Abgang */
.wechsel[data-zeigt="a"] [data-seite="a"],
.wechsel[data-zeigt="b"] [data-seite="b"] { opacity: 1; visibility: visible;
  transition: opacity .4s var(--kurve) .12s, visibility 0s; }           /* Auftritt */
@media (prefers-reduced-motion: reduce) { .wechsel > img { transition: none; } }
```

Die Zelle ist so groß wie der größere Inhalt; beide Aufnahmen im selben
Format, sonst springt doch etwas.

### 3.5 Hängeetikett statt Bildunterschrift

Bei den Friseuren standen Preisetiketten auf einer Eichenablage. Beim
Goldschmied hängt am Stück ein kleines Etikett am Faden — die natürliche
Form für ihre Angaben „Pink Turmalin, Weißgold, Gelbgold 750/000“.

```html
<li class="stueck">
  <button class="stueck-bild" data-gross="…"><img src="…" alt="Ring mit pinkem Turmalin in Weiß- und Gelbgold"></button>
  <p class="etikett"><span class="etikett-stein">Pink Turmalin</span>
     <span class="etikett-metall">Weißgold, Gelbgold <b>750</b></span></p>
</li>
```

Der Feingehalt (`750`, `925`, `900`) in Tabellenziffern wie eine Punze —
klein, gerahmt, das einzige „Ornament“ an der Angabe. Kein Text auf der
Bildkachel selbst.

### 3.6 Galerie mit Ansicht

Am Handy zwei nebeneinander (weiter antippbar), ab Tablet drei. **Hier
nicht auf ein einheitliches Format zuschneiden** (Hoch- und Querformate,
siehe Grundsatz 9) — Spalten mit `columns` oder ein Raster mit
`grid-row: span` je Format. Klick öffnet `<dialog>`; Pfeiltasten blättern,
Esc schließt, der Fokus kehrt zur Kachel zurück.

```js
const ansicht = document.querySelector('.ansicht');
const bild = ansicht.querySelector('img');
let reihe = [], stelle = 0, ausloeser = null;
const zeigen = (i) => {
  stelle = (i + reihe.length) % reihe.length;
  const k = reihe[stelle];
  bild.src = k.dataset.gross; bild.alt = k.querySelector('img').alt;
};
document.querySelectorAll('.stueck-bild').forEach((k) => k.addEventListener('click', () => {
  reihe = [...k.closest('.galerie').querySelectorAll('.stueck-bild')];
  ausloeser = k; zeigen(reihe.indexOf(k)); ansicht.showModal();
}));
ansicht.addEventListener('keydown', (e) => {
  if (e.key === 'ArrowLeft') zeigen(stelle - 1);
  if (e.key === 'ArrowRight') zeigen(stelle + 1);
});
ansicht.addEventListener('click', (e) => { if (e.target === ansicht) ansicht.close(); });
ansicht.addEventListener('close', () => ausloeser?.focus({ preventScroll: true }));
```

Das `<img>` im Dialog braucht ein echtes `src` (oder wird per Skript
erzeugt) — ein leeres `src=""` meldet der Detektor als kaputtes Bild.

### 3.7 Leiste, die ausweicht

Eine Leiste, die dauerhaft über dem Bild steht, versperrt die Sicht: beim
Runterscrollen weg, beim Hochscrollen zurück, mit 6 px Hysterese.

```js
const leiste = document.querySelector('.leiste');
let zuletzt = scrollY, weg = false;
addEventListener('scroll', () => {
  const y = scrollY, d = y - zuletzt;
  if (Math.abs(d) < 6) return;
  const soll = d > 0 && y > leiste.offsetHeight * 2;
  if (soll !== weg) { weg = soll; leiste.classList.toggle('weg', weg); }
  zuletzt = y;
}, { passive: true });
leiste.addEventListener('focusin', () => { weg = false; leiste.classList.remove('weg'); });
```

```css
.leiste { position: sticky; top: 0; transition: transform .4s var(--kurve); }
.leiste.weg { transform: translateY(-100%); transition-timing-function: var(--kurve-ab); }
```

### 3.8 Kapitelname in der Leiste

Ab Tablet steht oben links, in welchem Abschnitt man ist (Ringe,
Ohrschmuck, Werkstatt …). Abschnitte tragen `data-kapitel`.

```js
const anzeige = document.querySelector('.leiste-kapitel');
const abschnitte = [...document.querySelectorAll('section[data-kapitel]')];
const sichtbar = new Set();
const beob = new IntersectionObserver((eintraege) => {
  for (const e of eintraege) {
    if (e.isIntersecting) sichtbar.add(e.target); else sichtbar.delete(e.target);
  }
  const oben = abschnitte.find((a) => sichtbar.has(a));
  const text = oben ? oben.dataset.kapitel : '';
  if (anzeige.textContent !== text) {
    anzeige.textContent = text;
    // Neues Kapitel: kurz einblenden
    anzeige.classList.remove('neu'); void anzeige.offsetWidth; anzeige.classList.add('neu');
  }
}, { rootMargin: '-30% 0px -60% 0px' });
abschnitte.forEach((a) => beob.observe(a));
```

`.neu` blendet kurz ein (`opacity`, 0,4 s, nur ab Tablet).

### 3.9 „Heute geöffnet?“ in Münchner Zeit

Ihre Zeiten sind ungewöhnlich (Mo/Di zu, Sa nur bis 14 Uhr, „nach
Vereinbarung“) — genau dort hilft eine Zeile „Jetzt geöffnet, heute bis
18:30“ oder „Geschlossen · Mittwoch ab 11:30“. Uhrzeit von München, nicht
vom Gerät; der statische Text bleibt die Rückfallebene.

```html
<p class="heute" data-zeiten="3-5 11:30-18:30;6 10:30-14:00">Mi–Fr 11:30–18:30, Sa 10:30–14 Uhr und nach Vereinbarung</p>
```

```js
const TAGE = ['Sonntag','Montag','Dienstag','Mittwoch','Donnerstag','Freitag','Samstag'];
function jetzt() {
  const t = Object.fromEntries(new Intl.DateTimeFormat('de-DE', { timeZone: 'Europe/Berlin',
    weekday: 'short', hour: '2-digit', minute: '2-digit', hour12: false })
    .formatToParts(new Date()).map((p) => [p.type, p.value]));
  return { tag: ['So','Mo','Di','Mi','Do','Fr','Sa'].indexOf(t.weekday.replace('.', '')),
           min: (+t.hour % 24) * 60 + +t.minute };
}
function plan(s) {
  const p = {};
  for (const b of s.split(';')) {
    const m = b.trim().match(/^(\d)(?:-(\d))?\s+(\d\d):(\d\d)-(\d\d):(\d\d)$/);
    if (m) for (let d = +m[1]; d <= +(m[2] || m[1]); d++) p[d] = [m[3]*60 + +m[4], m[5]*60 + +m[6]];
  }
  return p;
}
const uhr = (m) => `${Math.floor(m / 60)}${m % 60 ? ':' + String(m % 60).padStart(2, '0') : ''} Uhr`;
document.querySelectorAll('[data-zeiten]').forEach((el) => {
  const p = plan(el.dataset.zeiten), j = jetzt(), h = p[j.tag];
  let satz;
  if (h && j.min >= h[0] && j.min < h[1]) satz = `Jetzt geöffnet, heute bis ${uhr(h[1])}`;
  else if (h && j.min < h[0]) satz = `Heute ab ${uhr(h[0])} geöffnet`;
  else for (let i = 1; i <= 7; i++) { const t = (j.tag + i) % 7;
    if (p[t]) { satz = `Geschlossen · ${i === 1 ? 'morgen' : TAGE[t]} ab ${uhr(p[t][0])}`; break; } }
  if (satz) el.textContent = satz + ' · und nach Vereinbarung';
});
```

### 3.10 Anfrage statt Warenkorb

Aus dem Extensions-Regal bei Irmonhair: Auswahl sammeln, daraus einen
fertigen Text bauen, den die Kundin selbst schickt (E-Mail, ggf. WhatsApp)
oder am Telefon durchgibt. Kein Server, keine Zahlung. Für die Goldschmiede
passt das genau zur Auftragsarbeit:

- **Was:** Ring · Eheringe · Ohrschmuck · Kette/Anhänger · Brosche ·
  Umarbeitung/Restaurierung
- **Metall:** Silber · Gelbgold matt · Weißgold · Rotgold · Palladium ·
  Platin · noch offen
- **Stein:** aus der Sammlung aussuchen · eigener Stein · ohne
- **Anlass / Zeitpunkt** (frei)

Daraus: „Guten Tag Frau Kusche, ich interessiere mich für Eheringe in
Gelbgold matt … Wann darf ich vorbeikommen?“ — in einer **bearbeitbaren**
`<textarea>`; Zeilen, die die Auswahl erzeugt, werden ersetzt, von Hand
geänderte bleiben stehen (`vonHand`-Merker). Knopf „Per E-Mail senden“
(`mailto:` mit `subject` und `body`, URL-kodiert) und „Text kopieren“.
Die Adresse steht genau einmal im HTML (`data-mail`), das Skript liest
sie von dort.

### 3.11 Vollflächiges Foto mit Schleier

Erst sinnvoll mit neuen, großen Werkstattfotos (die vorhandenen haben
400 px). Dann: Bild trägt den Abschnitt, **nie breiter als die Aufnahme**
(`width: min(100%, <Bildbreite>px)`), Schleier nur hinter dem Textblock als
senkrechtes Band, nach oben ausgeblendet — vier Fünftel des Bildes bleiben
offen. Am Handy der Text unter das Bild statt darüber.

```css
.buehne { position: relative; isolation: isolate; width: min(100%, 1600px); margin-inline: auto; }
.buehne > img { position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; z-index: -2; }
.buehne::before { content: ""; position: absolute; inset: 0; z-index: -1;
  background: linear-gradient(to right,
    color-mix(in oklch, var(--grund) 94%, transparent) 0,
    color-mix(in oklch, var(--grund) 86%, transparent) 30rem,
    color-mix(in oklch, var(--grund) 0%, transparent) 46rem);
  mask-image: linear-gradient(to top, black 0, black 40%, transparent 72%); }
```

---

## 4. Kandidaten für die eigene Idee (aus ihrem Material)

Nur Vorschläge — die Entscheidung fällt, wenn ihre Fotos und ihr Laden
angesehen sind. Jede muss klein funktionieren.

1. **Der FEDE-Ring als Geste.** Ihr eigener Text: „Der Ring verbirgt in
   getragenem Zustand das Herz. Erst wenn man den Ring abstreift, kann man
   die Hände öffnen.“ Ein kleines Bild, das sich auf Tippen öffnet (3.4) —
   im Kapitel Inspiration oder Eheringe. Belegt, berührend, klein.
2. **Die Steinsammlung als Schublade.** „Ich halte eine große Sammlung für
   Sie bereit, aus der Sie in Ruhe auswählen.“ Eine flache Reihe Steine im
   Steinbriefchen (gefaltetes Papier, in dem Edelsteine liegen) — antippen
   faltet das Briefchen auf und zeigt Stein, Herkunft, Schliff. Nur echte
   Steine aus ihren Fotos (die Edelstein-Aufnahmen sind freigestellt
   tauglich), beschriftet nur, was sie bestätigt.
3. **Punze statt Preis.** Jede Angabe trägt den Feingehalt als kleinen
   Stempel (750 · 925 · 900 · 500) — ihr Handwerk als Typografie (3.5).
4. **Die Unterschrift schreibt sich** einmal im Auftakt (3.3) — und sonst
   steht sie still.
5. **Werkstatt im Laden:** „mitzuerleben wie Ihr Schmuckstück entsteht“ —
   mit neuen Fotos eine Reihe *Rohling → Fassen → Polieren* zum Wischen.

Ausdrücklich nicht: drehende 3D-Ringe, Glitzerpartikel, Goldverläufe als
Text, Spiegelglanz — das ist Juwelier-Klischee, nicht ihre matte Werkstatt.

---

## 5. Palette und Schrift: wie man sie findet (nicht welche)

- Farben **aus den Fotos messen** (Mittelwert eines Ausschnitts, als oklch):
  die Wand und der Tisch im Laden, das matte Gelbgold eines Stücks, ein
  Stein aus der Sammlung. Die alte Seite nutzt ein Grasgrün (`#58b12c`) als
  Linkfarbe — prüfen, ob das ihres ist (Ladenwand? Logo?) oder ein Rest der
  Vorlage.
- Steinfarben sind **pro Stück**, nicht Seitenfarben: Ein Stein darf in
  seinem Kapitel als Ornament auftauchen (eine Linie, ein Punkt), nicht als
  Grund.
- Schrift: selbst gehostet (OFL). Eine Antiqua oder eine ruhige Grotesk mit
  Charakter — entschieden nach dem, was ihre Unterschrift und ihr Laden
  erzählen. Keine Systemschrift als Auszeichnung. Laden über
  `cdn.jsdelivr.net/npm/@fontsource-variable/<name>/files/<name>-latin-wght-normal.woff2`
  (einmalig herunterladen, ins Repo legen), Lizenz von
  `raw.githubusercontent.com/google/fonts/main/ofl/<name>/OFL.txt`.
- Eine dunkle Variante ist keine Umkehrung: Leitfarbe neu messen,
  Ankerfläche tiefer, feine Muster auf dunklem Grund verschwinden.

---

## 6. Prüfen statt behaupten

Vor jeder Fertigmeldung:

1. Aufnahmen auf **1440 px und 390 px** (dazu 820/1180 fürs iPad),
   angesehen — nicht nur erzeugt. Aufnahmen erst nach abgeschlossenem
   Auftritt (Klasse setzen, 1,2 s warten).
2. Detektor `node .claude/skills/impeccable/scripts/detect.mjs --json`
   → `[]` oder jede Meldung in der Übergabe begründet.
3. Konsolenfehler abfragen (`pageerror`, `console.error`).
4. Überbreite bei 360 und 390 px (`scrollWidth ≤ clientWidth`).
5. Kontrast gegen den **gerenderten** Grund messen, die kleinste Zeile zuerst
   (Nebentext ≥ 4,5 : 1).
6. Verhalten per Kurztest: Ansicht öffnen/blättern/Esc/Fokus, Wechsel 3.4,
   Anfrage-Text, Tastatur, ohne Skript.
7. Kein Bild doppelt (`currentSrc` aller sichtbaren Bilder vergleichen).
8. Behauptungen über Größe, Tempo, Lage **messen**. Gleich hohe Knöpfe
   nebeneinander: Oberkanten messen auf 768/820/1024/1180.

---

## 7. Fallen, die schon zugeschlagen haben (Auswahl, passend hier)

| Falle | Auflösung |
|---|---|
| `[hidden]` verliert gegen Klassen, die `display` setzen | `[hidden] { display: none !important; }` |
| Grid mit zwei Kindern erzeugt zwei Zeilen | `grid-area: 1 / 1` zum Stapeln |
| `position: sticky` meldet beim Scrollen die Klebeposition | festen Anker davor setzen und dessen `offsetTop` nehmen |
| Scroll-Umschalter flackert beim Auslaufen | 6 px Hysterese |
| Android-WebViews (WhatsApp) blasen Text auf | `text-size-adjust: 100%` |
| Viele DOM-Zeilen einzeln einfügen ruckelt | `DocumentFragment` + `replaceChildren` |
| `#` in einer SVG-Daten-URI → Bild still leer | `%23` schreiben |
| CSS-`stroke` überschreibt das `stroke`-Attribut | Farbe am Element, Breite/Animation in CSS |
| Mehrere Inline-Kopien desselben SVG teilen IDs | ID-Präfix je Einsatz |
| `pathLength` + `vector-effect: non-scaling-stroke` strichelt in Chrome falsch | nicht kombinieren |
| CSS-Animation mit `forwards` überschreibt Inline-Stile aus dem Skript | nur `backwards` oder andere Eigenschaft |
| Element mit `z-index: -1` verschwindet hinter `body` | Elternteil `isolation: isolate` |
| Wischreihe in Flex-Spalte mit `align-items: start` wird so breit wie ihr Inhalt | `align-items: stretch` |
| Flex-Knopf (`inline-flex`) mit `<span>` im Text verliert Leerzeichen | ganzen Text in eine Spanne fassen |
| Knopfreihen in zwei Karten brechen verschieden um → Knöpfe auf ungleicher Höhe | Container-Query an der Kartenbreite (beide gleich breit), `margin-top: auto` |
| Spezifischere Nachbarregel hebelt Ein-Klassen-Regel aus | mit Elternselektor schreiben, nicht `!important` |
| Zwei Regeln mit demselben Selektor: die zweite gewinnt still | nach dem Einfügen `grep -c` auf den Selektor |
| Neue Klasse mit vergebenem Namen zerlegt eine andere Seite | vor dem Benennen `grep` über alle Seiten |
| Verlauf mit letztem Halt vor 100 % → gerade Kante quer durchs Bild | Ellipse im eigenen Kasten auf null auslaufen lassen; für breite Textblöcke senkrechtes Band |
| Kleinste Zeile über Bild scheitert am Kontrast | Zeile dorthin, wo der Schleier dicht ist |
| Detektor meldet Farbstreifen (auch `::after`) als „side-tab“ | Ablage als Hintergrund der Reihe, nicht als Rand |
| Warmes Off-White meldet der Detektor als „cream-palette“ | Wandfarbe messen statt Cremeton aus Gewohnheit |
| `box-shadow: inset 0 0 0 1px` gilt als Glühen | `border` nehmen |
| Element folgt dem Scrollen und ruckelt am Handy | weich nachführen (rAF, exponentiell), Variable am Element statt an `<html>`, kein `drop-shadow` am bewegten Element |
| Standbild aus einem Video als Foto | Kantenenergie gegen echte Fotos messen; bei einem Drittel nur klein |

---

## 8. Offene Fragen an die Goldschmiedin (Start für `ABNAHME.md`)

1. **Fotos:** Neues Porträt (in der Werkstatt, mind. 1600 px), Laden und
   Werkstatt groß, Stücke auf einheitlichem Grund? Bis dahin bleibt das
   Porträt klein.
2. **Unterschrift / „Miku“:** als größere Vorlage oder Vektor vorhanden?
3. **Öffnungszeiten:** noch Mi–Fr 11:30–18:30, Sa 10:30–14, und nach
   Vereinbarung?
4. **Faires Gold:** Gilt „Ringe aus Fairtrade-Gold“ noch, mit Zertifikat?
   Noch Sponsorin bei mercuryfreemining.org? Recyclinggold weiter Standard?
   Nur Bestätigtes kommt auf die Seite.
5. **Eheringe:** Soll ein Einstiegspreis („ab …“) genannt werden — oder
   bewusst keiner?
6. **Welche Stücke sind noch erhältlich**, welche nur als Beispiel? (Wichtig
   für die Beschriftung — ein falsch beschriftetes Stück ist schlimmer als
   ein unbeschriftetes.)
7. **Impressum:** Angaben nach § 5 DDG (statt TMG), USt-IdNr., zuständige
   Handwerkskammer (Gold- und Silberschmied ist ein Handwerk der Anlage B).
8. **Kontaktweg:** E-Mail, Telefon — auch WhatsApp? Termin zur Beratung
   gewünscht (Formular-Text, Anruf)?
9. **Grün der alten Seite (`#58b12c`):** ihres oder Rest der Vorlage?
10. **Domain:** bleibt michaela-kusche.de; wer stellt die Weiterleitung um?
