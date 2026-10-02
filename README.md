# Goldschmiedin Michaela Kusche — Website

Neue Website für michaela-kusche.de. Statisch: HTML, CSS, Vanilla JS. Kein Build-Schritt
im Browser, keine Abhängigkeiten, keine CDNs. Schriften (OFL) und Bilder liegen im Repo.

## Ansehen

```sh
python3 -m http.server 8000   # dann http://localhost:8000
```

Bei jedem Push auf `main` veröffentlicht `.github/workflows/deploy-pages.yml` die Seite
über GitHub Pages (in den Repo-Einstellungen unter *Pages* als Quelle „GitHub Actions“ wählen).

## Aufbau

| Datei | Inhalt |
|---|---|
| `index.html` | die Seite: Auftakt, Dreischritt, Schmuck, Inspiration, Edelsteine, Werkstatt, Faires Gold, Anfrage, Besuch |
| `impressum.html`, `datenschutz.html` | Pflichtseiten |
| `stil.css` | alle Gestaltungswerte als Tokens in `:root` (Farben aus ihren Fotos gemessen) |
| `seite.js` | Verhalten — ohne Skript bleibt alles lesbar |
| `bilder/` | WebP in mehreren Breiten, nie über die Vorlage gezogen |
| `schrift/` | Newsreader, Hanken Grotesk (selbst gehostet, Lizenzen daneben) |
| `werkzeug/` | Skripte, die Bilder, Unterschrift und Galerien erzeugen — siehe `werkzeug/README.md` |
| `ABNAHME.md` | offene Fragen an die Goldschmiedin, vor dem Livegang |
| `DESIGN-ERBE.md` | Grundsätze und Bauteile aus den früheren Projekten |

## Die Besonderheiten

- **Die Unterschrift schreibt sich.** Ihre echte Unterschrift (nachgezeichnet aus der Vorlage),
  Zug für Zug über eine Maske aus der Mittellinie.
- **Die Lupe.** Über der Disthen-Brosche im ersten Bildschirm zeigt eine Goldschmiedelupe
  die mattierte, gebürstete Oberfläche in voller Auflösung (nur mit Maus).
- **Der Probierstein.** In der Anfrage wählt man das Metall wie in der Werkstatt: Probiernadel
  ziehen, auf dem schwarzen Stein erscheint der matte Strich der Legierung mit ihrer Punze.
  Mit der Maus kann man selbst über den Stein streichen.
- **Punzen statt Preise.** Jeder Feingehalt (750 · 900 · 925 · 500) steht als kleiner Stempel.
