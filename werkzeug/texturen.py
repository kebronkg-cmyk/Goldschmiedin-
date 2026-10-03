"""Texturen aus ihren eigenen Aufnahmen — für Flächen und für Schrift.

Aufruf:  python3 werkzeug/texturen.py <ordner-mit-originalen>
Schmale Streifen (Disthen, gebürstetes Gold) werden gespiegelt gestapelt:
das ergibt nahtlose Kacheln ohne Hochskalieren. Ausgabe: bilder/textur/*.webp
"""
import json, pathlib, sys
import numpy as np
from PIL import Image, ImageOps

Q = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "quelle")
Z = pathlib.Path(__file__).resolve().parent.parent / "bilder" / "textur"

def nahtlos_waagrecht(bild, ueberlapp):
    """Rechte Kante in die linke überblenden: die Kachel schließt nahtlos an sich selbst an."""
    a = np.asarray(bild).astype(float); w = a.shape[1]; o = ueberlapp
    t = np.linspace(0, 1, o)[None, :, None]
    aus = a[:, : w - o].copy()
    aus[:, :o] = a[:, w - o:] * (1 - t) + a[:, :o] * t
    return Image.fromarray(aus.clip(0, 255).astype("uint8"))

def nahtlos_senkrecht(bild, ueberlapp):
    return nahtlos_waagrecht(bild.transpose(Image.Transpose.TRANSPOSE), ueberlapp).transpose(Image.Transpose.TRANSPOSE)

def streifen_stapeln(streifen, hoehe, ueberlapp, saat=7):
    """Ein schmaler Streifen wird zur Fläche: Lagen mit seitlichem Versatz, weich überblendet (kein Spiegeln)."""
    rng = np.random.default_rng(saat)
    s = np.asarray(streifen).astype(float); h, w = s.shape[:2]; schritt = h - ueberlapp
    n = int(np.ceil((hoehe + ueberlapp) / schritt)) + 1
    aus = np.zeros((schritt * n + ueberlapp, w, 3))
    for k in range(n):
        lage = np.roll(s, int(rng.integers(0, w)), axis=1)
        y = k * schritt
        if k == 0:
            aus[y:y + h] = lage
        else:
            t = np.linspace(0, 1, ueberlapp)[:, None, None]
            aus[y:y + ueberlapp] = aus[y:y + ueberlapp] * (1 - t) + lage[:ueberlapp] * t
            aus[y + ueberlapp:y + h] = lage[ueberlapp:]
    bild = Image.fromarray(aus[: hoehe + ueberlapp].clip(0, 255).astype("uint8"))
    return nahtlos_senkrecht(bild, ueberlapp)

def gebuerstet(farbe, breite, hoehe, saat=11):
    """Mattiertes, gebürstetes Gold: gerichtetes Korn in der gemessenen Farbe des Broschenrahmens."""
    rng = np.random.default_rng(saat)
    rauschen = rng.normal(0, 1, (hoehe, breite // 8))
    zeilen = np.repeat(rauschen, 8, axis=1)                      # lange, gerichtete Züge
    from scipy.ndimage import gaussian_filter
    zeilen = gaussian_filter(zeilen, sigma=(0.6, 40), mode="wrap")
    fein = gaussian_filter(rng.normal(0, 1, (hoehe, breite)), sigma=(0.4, 6), mode="wrap")
    korn = zeilen / zeilen.std() * 0.65 + fein / fein.std() * 0.35
    f = np.array(farbe, float)[None, None, :]
    bild = f * (1 + korn[..., None] * 0.07)
    return Image.fromarray(bild.clip(0, 255).astype("uint8"))

def schiefer(groesse=900, saat=5):
    """Probierstein (Kieselschiefer): erzeugt, nicht fotografiert — nahtloses Korn mit feinen Adern."""
    from scipy.ndimage import gaussian_filter
    rng = np.random.default_rng(saat)
    grob = gaussian_filter(rng.normal(0, 1, (groesse, groesse)), 60, mode="wrap")
    mittel = gaussian_filter(rng.normal(0, 1, (groesse, groesse)), 6, mode="wrap")
    fein = rng.normal(0, 1, (groesse, groesse))
    adern = np.abs(gaussian_filter(rng.normal(0, 1, (groesse, groesse)), (90, 18), mode="wrap"))
    adern = np.exp(-(adern / adern.std() * 9) ** 2)            # schmale, helle Linien
    h = 0.0 + grob / grob.std() * 0.008 + mittel / mittel.std() * 0.008 + fein * 0.016 + adern * 0.008
    basis = np.array([15, 17, 19], float) / 255                 # #0f1113, wie der Stein in der Anfrage
    bild = (basis[None, None, :] + h[..., None] * np.array([1.0, 1.02, 1.06])[None, None, :]) * 255
    return Image.fromarray(bild.clip(0, 255).astype("uint8"))

def farbton_drehen(bild, ziel_h, ziel_c_faktor=1.0, l_versatz=0.0):
    """Gleiche Fasern, anderer Stein: dreht den Farbton in OKLCH (Helligkeit und Korn bleiben)."""
    a = np.asarray(bild).astype(float) / 255
    lin = np.where(a <= 0.04045, a / 12.92, ((a + 0.055) / 1.055) ** 2.4)
    M1 = np.array([[0.4122214708, 0.5363325363, 0.0514459929], [0.2119034982, 0.6806995451, 0.1073969566], [0.0883024619, 0.2817188376, 0.6299787005]])
    M2 = np.array([[0.2104542553, 0.7936177850, -0.0040720468], [1.9779984951, -2.4285922050, 0.4505937099], [0.0259040371, 0.7827717662, -0.8086757660]])
    lab = np.cbrt(lin @ M1.T) @ M2.T
    L, A, B = lab[..., 0], lab[..., 1], lab[..., 2]
    C = np.hypot(A, B); H = np.arctan2(B, A)
    mittel = np.degrees(np.angle(np.mean(np.exp(1j * H) * C)))
    H = H + np.radians(ziel_h - mittel); C = C * ziel_c_faktor; L = L + l_versatz
    lab = np.stack([L, C * np.cos(H), C * np.sin(H)], -1)
    lms = (lab @ np.linalg.inv(M2).T) ** 3
    lin = np.clip(lms @ np.linalg.inv(M1).T, 0, 1)
    srgb = np.where(lin <= 0.0031308, lin * 12.92, 1.055 * lin ** (1 / 2.4) - 0.055)
    return Image.fromarray((srgb * 255).round().astype("uint8"))

def main():
    Z.mkdir(parents=True, exist_ok=True)
    b2 = Image.open(Q / "media__Broschen__b2.jpg").convert("RGB")
    kro = Image.open(Q / "media__topics-pictures__zoom__michaela_kusche_schmuck_krokoring_3.jpg").convert("RGB")
    sam = Image.open(Q / "media__topics-pictures__zoom__ohrringe-samen_mcp0012.jpg").convert("RGB")
    aus = {
        # Disthen: die Fasern des Steins der Brosche
        "disthen": streifen_stapeln(nahtlos_waagrecht(b2.crop((1150, 1080, 2300, 1225)), 140), 900, 50),
        # Gebürstetes, mattiertes Gold: Farbe vom Rahmen der Brosche gemessen, Korn gerichtet
        "gold": gebuerstet(np.median(np.asarray(b2.crop((1700, 830, 2600, 870))).reshape(-1, 3), 0), 1200, 600),
        # Der rostrote Stein unter der Brosche
        "rost": b2.crop((0, 1750, 3872, 2592)).resize((2400, 522), Image.LANCZOS),
        # Birkenrinde unter den Samenkapseln — fast Papier
        "rinde": nahtlos_senkrecht(nahtlos_waagrecht(sam.crop((0, 0, 700, 300)), 90), 60),
        # Flechte vom Ast des Krokodilrings
        "flechte": kro.crop((0, 560, 640, 1100)),
        # Smaragd: dieselben Fasern wie der Disthen, Farbton auf Smaragdgrün gedreht
        "smaragd": None,
        # Probierstein — erzeugt (kein Foto vorhanden), Farbe des Steins aus der Anfrage
        "stein": schiefer(),
    }
    aus["smaragd"] = farbton_drehen(aus["disthen"], 162, 1.05, -0.02)
    farben = {}
    for n, b in aus.items():
        b.save(Z / f"{n}.webp", "WEBP", quality=78, method=6)
        a = np.asarray(b).reshape(-1, 3)
        farben[n] = {"mittel": [int(x) for x in np.median(a, 0)], "hell": [int(x) for x in np.percentile(a, 85, 0)], "dunkel": [int(x) for x in np.percentile(a, 15, 0)], "groesse": b.size}
    (Z / "farben.json").write_text(json.dumps(farben, indent=1))
    for n, f in farben.items():
        print(n, f)

if __name__ == "__main__":
    main()
