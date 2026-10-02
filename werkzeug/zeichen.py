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



# ───── Federlinie: die Unterschrift als glatter, feiner Strich (für große Größen) ─────

def federlinie(b, glatt=2.2):
    """Mittellinie als zusammenhängende Züge; an Knoten geht es in die geradeste Richtung weiter."""
    from scipy.ndimage import gaussian_filter1d
    pts = set(zip(*np.nonzero(skeletonize(b))))
    N = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    nb = lambda p: [(p[0] + a, p[1] + c) for a, c in N if (p[0] + a, p[1] + c) in pts]
    knoten = {p for p in pts if len(nb(p)) != 2}
    # Kanten zwischen Knoten (oder geschlossene Schleifen)
    benutzt, kanten = set(), []
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
    for n in sorted(knoten):
        for q in nb(n):
            if ek(n, q) not in benutzt:
                kanten.append(gehe(n, q))
    for p in sorted(pts):
        for q in nb(p):
            if ek(p, q) not in benutzt:
                kanten.append(gehe(p, q))
    kanten = [k for k in kanten if len(k) >= 5]
    # Knoten zusammenfassen (Skelett-Knoten liegen oft als kleine Haufen)
    def schluessel(p):
        return (p[0] // 5, p[1] // 5)
    frei = list(range(len(kanten)))
    def richtung(k, am_ende):
        a = np.array(k[-1] if am_ende else k[0], float)
        b_ = np.array(k[-6] if am_ende else k[5], float) if len(k) > 6 else np.array(k[0] if am_ende else k[-1], float)
        v = a - b_
        return v / (np.linalg.norm(v) or 1)
    zuege = []
    while frei:
        # links beginnen: Kante mit dem kleinsten x-Wert
        i = min(frei, key=lambda j: min(p[1] for p in kanten[j]))
        frei.remove(i)
        k = kanten[i]
        if k[0][1] > k[-1][1]:
            k = k[::-1]
        zug = list(k)
        while True:
            ende = zug[-1]; v = richtung(zug, True)
            beste, bwert, bk = None, -0.2, None
            for j in frei:
                kj = kanten[j]
                for umkehr in (False, True):
                    kk = kj[::-1] if umkehr else kj
                    if np.hypot(kk[0][0] - ende[0], kk[0][1] - ende[1]) > 7:
                        continue
                    w = float(np.dot(v, -richtung(kk, False)))
                    if w > bwert:
                        beste, bwert, bk = j, w, kk
            if beste is None:
                break
            frei.remove(beste); zug += bk[1:]
        zuege.append(zug)
    aus = []
    for z in zuege:
        P = np.array([(x / F, y / F) for y, x in z], float)
        if len(P) < 4:
            continue
        # gleichmäßig neu abtasten, dann glätten (Enden bleiben fest)
        d = np.r_[0, np.cumsum(np.hypot(*np.diff(P, axis=0).T))]
        if d[-1] < 1.2:
            continue
        s = np.linspace(0, d[-1], max(6, int(d[-1] / 0.5)))
        Q = np.c_[np.interp(s, d, P[:, 0]), np.interp(s, d, P[:, 1])]
        G = np.c_[gaussian_filter1d(Q[:, 0], glatt, mode="nearest"), gaussian_filter1d(Q[:, 1], glatt, mode="nearest")]
        G[0], G[-1] = Q[0], Q[-1]
        G = np.array(rdp([tuple(p) for p in G], 0.06))
        # Catmull-Rom → kubische Bézier
        teile = [f"M{G[0][0]:.2f} {G[0][1]:.2f}"]
        for k in range(len(G) - 1):
            p0 = G[max(k - 1, 0)]; p1 = G[k]; p2 = G[k + 1]; p3 = G[min(k + 2, len(G) - 1)]
            c1 = p1 + (p2 - p0) / 6; c2 = p2 - (p3 - p1) / 6
            teile.append(f"C{c1[0]:.2f} {c1[1]:.2f} {c2[0]:.2f} {c2[1]:.2f} {p2[0]:.2f} {p2[1]:.2f}")
        aus.append({"d": "".join(teile), "l": round(float(d[-1]), 1), "x": round(float(G[:, 0].min()), 1)})
    aus.sort(key=lambda z: z["x"])
    return aus


def feder_main():
    sig = maske(tinte("media__michaela-kusche-unterschrift.png", False), 0.42)
    daten = json.loads(ZIEL.read_text())
    daten["unterschrift"]["feder"] = federlinie(sig)
    ZIEL.write_text(json.dumps(daten))
    print("Federlinie:", len(daten["unterschrift"]["feder"]), "Züge")


if __name__ == "__main__":
    main()
    feder_main()
