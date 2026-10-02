"""Zeichnet ihre Unterschrift und das „Miku“ aus den Vorlagen nach.

Aufruf:  python3 werkzeug/zeichen.py <ordner-mit-originalen>
Schreibt werkzeug/zeichen.json; bauen.py setzt es in die Seiten.

Die sichtbare Form ist die gefüllte Kontur der echten Vorlage (potrace).
Zum „Schreiben“ dient eine Maske aus der Mittellinie (Skelett), Zug für
Zug von links nach rechts — so bleibt die Linie ihre eigene.
"""
import json, pathlib, sys
import numpy as np, potrace
from PIL import Image, ImageFilter
from skimage.morphology import skeletonize

QUELLE = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "quelle")
ZIEL = pathlib.Path(__file__).resolve().parent / "zeichen.json"
F = 8  # Hochrechnung für die Kontur

def tinte(datei, hell_auf_dunkel):
    a = np.array(Image.open(QUELLE / datei).convert("RGBA")).astype(float) / 255
    return a[..., 3] if hell_auf_dunkel else a[..., 3] * (1 - a[..., :3].mean(-1))

def maske(ink, schwelle):
    h, w = ink.shape
    gross = Image.fromarray((ink * 255).astype("uint8")).resize((w * F, h * F), Image.BICUBIC)
    gross = gross.filter(ImageFilter.GaussianBlur(2.2))
    return np.array(gross) / 255 > schwelle

def kontur(b):
    # potracer behandelt True als Papier — daher invertiert übergeben
    pfad = potrace.Bitmap(~b).trace(turdsize=12, alphamax=1.1, opticurve=True, opttolerance=0.6)
    p = lambda pt: f"{pt.x / F:.1f} {pt.y / F:.1f}"
    d = []
    for c in pfad:
        d.append("M" + p(c.start_point))
        for s in c.segments:
            d.append(("L" + p(s.c) + "L" + p(s.end_point)) if s.is_corner
                     else ("C" + p(s.c1) + " " + p(s.c2) + " " + p(s.end_point)))
        d.append("Z")
    return "".join(d)

def rdp(P, eps):
    if len(P) < 3:
        return P
    a, b = np.array(P[0]), np.array(P[-1])
    ab = b - a
    L = np.hypot(*ab) or 1e-9
    d = [abs(ab[0] * (p[1] - a[1]) - ab[1] * (p[0] - a[0])) / L for p in P[1:-1]]
    i = int(np.argmax(d)) + 1
    if d[i - 1] > eps:
        return rdp(P[:i + 1], eps)[:-1] + rdp(P[i:], eps)
    return [P[0], P[-1]]

def zuege(b):
    pts = set(zip(*np.nonzero(skeletonize(b))))
    N = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    nb = lambda p: [(p[0] + a, p[1] + c) for a, c in N if (p[0] + a, p[1] + c) in pts]
    knoten = {p for p in pts if len(nb(p)) != 2}
    benutzt, wege = set(), []
    ek = lambda a, b: (a, b) if a < b else (b, a)
    def gehe(start, erst):
        weg, vor, jetzt = [start, erst], start, erst
        benutzt.add(ek(start, erst))
        while jetzt not in knoten:
            nx = [r for r in nb(jetzt) if r != vor and ek(jetzt, r) not in benutzt]
            if not nx:
                break
            benutzt.add(ek(jetzt, nx[0])); vor, jetzt = jetzt, nx[0]; weg.append(jetzt)
        return weg
    for n in knoten:
        for q in nb(n):
            if ek(n, q) not in benutzt:
                wege.append(gehe(n, q))
    for p in pts:  # geschlossene Schleifen ohne Knoten
        for q in nb(p):
            if ek(p, q) not in benutzt:
                wege.append(gehe(p, q))
    aus = []
    for w in wege:
        if len(w) < 6:
            continue
        q = [(x / F, y / F) for y, x in w]
        if q[0][0] > q[-1][0]:
            q = q[::-1]
        aus.append(rdp(q, 0.25))
    aus.sort(key=lambda q: min(x for x, _ in q))
    return [{"d": "M" + "L".join(f"{x:.1f} {y:.1f}" for x, y in q),
             "l": round(sum(np.hypot(q[i + 1][0] - q[i][0], q[i + 1][1] - q[i][1]) for i in range(len(q) - 1)), 1)}
            for q in aus]

def main():
    sig = maske(tinte("media__michaela-kusche-unterschrift.png", False), 0.42)
    miku = maske(tinte("templates__miku_2014__img__miku-trans-neg.png", True), 0.56)
    daten = {"unterschrift": {"viewBox": "0 0 300 41", "d": kontur(sig), "zuege": zuege(sig)},
             "miku": {"viewBox": "0 0 148 60", "d": kontur(miku)}}
    ZIEL.write_text(json.dumps(daten))
    print("Unterschrift", len(daten["unterschrift"]["d"]), "Zeichen,", len(daten["unterschrift"]["zuege"]), "Züge;",
          "Miku", len(daten["miku"]["d"]), "Zeichen")

if __name__ == "__main__":
    main()
