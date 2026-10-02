# Werkzeug

Die Seite selbst braucht nichts davon. Die Skripte erzeugen nur, was in `bilder/`
und zwischen den Marken in den HTML-Seiten steht.

```sh
pip install pillow numpy scikit-image potracer

# 1. Originale der alten Seite holen (einmalig) — Dateiname: Pfad mit „__“ statt „/“
mkdir -p quelle && cd quelle
curl -s https://www.michaela-kusche.de/media/Broschen/b2.jpg -o media__Broschen__b2.jpg   # usw.
cd ..

# 2. Bilder in mehreren Breiten als WebP (nie größer als die Vorlage)
python3 werkzeug/bilder.py quelle

# 3. Unterschrift und „Miku“ nachzeichnen → werkzeug/zeichen.json
python3 werkzeug/zeichen.py quelle

# 4. Bilder, Galerien und Zeichen in die Seiten setzen (beliebig oft ausführbar)
python3 werkzeug/bauen.py
```

- Neues Bild: in `bilder.py` unter `BILDER` eintragen, in `bauen.py` unter `GALERIEN`
  mit Stein, Metall (`{750}` wird zur Punze) und Alternativtext.
- Ein Bild außerhalb der Galerien: `<img data-bild="name" sizes="…" alt="…">` schreiben,
  `bauen.py` ergänzt `src`, `srcset`, `width`, `height`.
- Die Metallfarben auf dem Probierstein stehen als oklch-Tokens `--m-*` in `stil.css` und
  als sRGB in `seite.js` (`FARBE`). Wer eine ändert, ändert beide.
- Eine größere Vorlage der Unterschrift (Papier, schwarzer Stift, Foto von oben) einfach
  als `media__michaela-kusche-unterschrift.png` in `quelle/` legen und Schritt 3 + 4 wiederholen.
