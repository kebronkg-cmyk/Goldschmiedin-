# Product

<!-- impeccable:product-schema 1 -->

Quelle: die bisherige Seite michaela-kusche.de (gelesen 02.10.2026) und `DESIGN-ERBE.md`,
das der Auftraggeber als verbindliche Grundlage übergeben hat. Unbestätigtes steht in `ABNAHME.md`.

## Platform

web

## Stack

Statisches HTML, CSS, Vanilla JS; kein Build-Schritt, keine Abhängigkeiten, keine CDNs.
Ausgeliefert über GitHub Pages (Workflow `.github/workflows/deploy-pages.yml`).

## Users

Menschen in und um München, die ein besonderes Schmuckstück suchen — ein Unikat, Eheringe,
ein Stück nach Maß, die Restaurierung eines geliebten Stücks — und dafür eine Person suchen,
der sie ihr Vorhaben anvertrauen. Sie kommen meist mit einem Anlass und wollen wissen: Wer
macht das, wie sieht ihre Arbeit aus, wie komme ich mit ihr ins Gespräch.

## Product Purpose

Die Website der Goldschmiedin Michaela Kusche, München-Pasing, Werkstatt im Laden seit 2008.
Sie soll ihre Arbeit zeigen, ihre Person spürbar machen und den Weg ins Gespräch öffnen
(Besuch, Anruf, E-Mail). Erfolg: Besucherinnen melden sich mit einem konkreten Vorhaben.

## Positioning

Unikate aus **mattiertem** Gelbgold, Weißgold, Rotgold, Palladium, Platin und Silber, mit
Edelsteinen in außergewöhnlichen Farben und Fantasieschliffen aus einer eigenen Sammlung.
Die Werkstatt liegt im Laden: man kann zusehen, wie das Stück entsteht. Formen aus Reisen
(FEDE-Ring, Krokodilring aus Thailand, Samenkapseln und Maya-Jade aus Guatemala).
Recyclinggold, Ringe auf Wunsch aus Fairtrade-Gold, Sponsorin von mercuryfreemining.org.

## Operating Context

Beratung im Laden, Auswahl des Steins aus ihrer Sammlung „in Ruhe“, Fertigung am Werkbrett,
Ohrschmuck wird individuell angepasst. Öffnungszeiten Mi–Fr 11:30–18:30, Sa 10:30–14:00,
und gerne nach Vereinbarung. Bachbauernstraße 5, 81241 München, drei Gehminuten vom Pasinger
Bahnhof. Telefon 089 / 41 85 88 65, hallo@michaela-kusche.de.

## Capabilities and Constraints

- Kein Shop, keine Preise; Anfrage als vorbereitete E-Mail, die die Besucherin selbst sendet.
- Fotos stammen von der alten Seite, meist 1066 × 800, unterschiedliche Naturgründe; Porträt
  nur 243 × 338. Kein Bild über seine Vorlage ziehen. Neue Fotos sind angefragt.
- Schriften selbst hosten (OFL), keine Google-Dienste.
- Offene Produktfragen: Erhältlichkeit einzelner Stücke, Eheringpreise, Impressumsangaben.

## Brand Commitments

- Sie spricht in der Ich-Form und siezt. Ihre eigenen Sätze tragen die Seite:
  „Schmuck für ganz besondere Menschen!“, „Schmuck ist Ausdruck unserer Persönlichkeit und
  Zeichen unserer Kultur.“, „Ich freue mich darauf, Sie kennen zu lernen!“,
  Dreischritt „Auswählen · Kombinieren · Bearbeiten“.
- Ihre echte Unterschrift und das Kürzel „Miku“ (Vektor aus der Vorlage in `werkzeug/zeichen.json`).
- Der Auftraggeber wünscht: die sich selbst schreibende Unterschrift groß, auffällig und
  zugleich dezent und elegant; Texturen und Farben aus ihren Fotos als Flächen und mit der
  Schrift verschmolzen; keine erkennbaren KI-Gestaltungsmuster.

## Evidence on Hand

Texte und Bildangaben der alten Seite (Material, Feingehalt) in `werkzeug/bauen.py`;
41 aufbereitete Fotos in `bilder/` (Herkunft: michaela-kusche.de/media). Keine
Kundenstimmen, keine Preise, keine Auszeichnungen — nichts davon erfinden.

## Product Principles

1. Die Person ist die Marke: Hand, Unterschrift, Werkstatt vor jeder Werbezeile.
2. Das Material spricht: mattes Gold, Steinfarben, Naturgründe aus ihren eigenen Aufnahmen.
3. Nur Belegtes: jede Angabe stammt von ihr oder wird erfragt.
4. Der Weg ins Gespräch ist immer nah: Telefon, Adresse, Anfrage.

## Accessibility & Inclusion

Kontrast für Fließtext ≥ 4,5 : 1, Bedienung per Tastatur, `prefers-reduced-motion` bedienen,
lesbar ohne JavaScript.
