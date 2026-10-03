# Arbeitsweise in diesem Repo

Alles auf Deutsch: Oberfläche, Kommentare, Commits, Antworten. Kein Modellname in Commits,
PR-Texten oder Code. Auf der Seite selbst kein Hinweis auf KI oder Werkzeuge.

## Versionen — nie direkt auf `main`

`main` ist die veröffentlichte Seite (GitHub Pages: https://kebronkg-cmyk.github.io/Goldschmiedin-/).
Es wird **nie direkt auf `main` committet oder gepusht.** Jede Arbeit läuft so:

1. Arbeit auf einem Zweig `arbeit/<name>`, Pull Request als Entwurf gegen `main`.
2. Vorschau ohne Veröffentlichung: Jeder Zweig `arbeit/version-<n>-<name>` erscheint nach dem Push
   unter `https://kebronkg-cmyk.github.io/Goldschmiedin-/vorschau/<name>/` (noindex). Diesen Link
   bekommt die Inhaberin. Nach dem Push abfragen, bis die Änderung wirklich da ist.
3. Schreibt der Auftraggeber **„neue Version“** (ggf. mit Namen der Variante):
   - Der aktuelle Stand von `main` ist bereits als Zweig `version-<n>` gesichert (sonst jetzt sichern).
   - Pull Request auf „bereit“ setzen und mergen (Merge-Commit, kein Squash).
   - Danach `main` als `version-<n+1>` sichern: `git branch version-<n+1> origin/main && git push -u origin version-<n+1>`.
   - Live-URL abfragen, bis die Änderung wirklich da ist.
4. Schreibt der Auftraggeber **„back“**: die vorige Version wiederherstellen, ohne Geschichte zu löschen.
   - Zweig `arbeit/back-zu-version-<n>` von `main`, darin den Dateibaum von `version-<n>` herstellen:
     `git rm -rq -- . ':!.github' && git checkout version-<n> -- . ':!.github' && git commit -m "Zurück zu Version <n>"`
     (der Veröffentlichungs-Ablauf in `.github/` bleibt auf dem neuesten Stand)
   - Pull Request, mergen, Live-URL prüfen. Kein Force-Push, kein Löschen von Zweigen.

Tags lassen sich über den Zugang dieser Umgebung nicht pushen; Versionen sind deshalb Zweige.

| Zweig | Stand |
|---|---|
| `version-1` | erste veröffentlichte Fassung (Newsreader, heller Grund) |

## Bauart

Statisch: HTML, CSS, Vanilla JS. Kein Build im Browser, keine CDNs, Schriften (OFL) im Repo.
`werkzeug/` erzeugt Bilder, Texturen, Unterschrift und Galerien (`werkzeug/README.md`).
Gestaltungswerte als Token in `:root`.

## Prüfen vor jeder Vorschau

1. Aufnahmen 1440 und 390 px, angesehen (dazu 820/1180 bei Layout-Änderungen).
2. `node .claude/skills/impeccable/scripts/detect.mjs --json index.html stil.css` — Befunde beheben
   oder einzeln begründen.
3. Konsolenfehler, Überbreite bei 360/390, ohne Skript lesbar, `prefers-reduced-motion`.
4. Kein Bild doppelt, Kontraste gemessen.

## Gestaltung

Grundsätze aus `DESIGN-ERBE.md` und `PRODUCT.md`. Keine KI-Muster: keine Überzeilen in
gesperrten Versalien über Überschriften, keine Abschnittsnummern, keine gleich großen
Kartenraster, keine Einblend-Bewegung auf jedem Abschnitt, keine Schriften von der
impeccable-Liste der Standardschriften.
