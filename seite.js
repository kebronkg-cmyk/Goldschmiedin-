/* Goldschmiedin Michaela Kusche — Verhalten. Ohne Skript bleibt alles lesbar. */
(() => {
  'use strict';
  const $ = (s, el = document) => el.querySelector(s);
  const $$ = (s, el = document) => [...el.querySelectorAll(s)];
  const ruhig = matchMedia('(prefers-reduced-motion: reduce)');
  const feinZeiger = matchMedia('(hover: hover) and (pointer: fine)');

  /* ───── Auftritt: erst wenn die Seite steht ───── */
  // Nach dem letzten Zug fällt die Maske weg — die Unterschrift steht dann vollständig.
  // (animationend feuert in Masken nicht verlässlich, daher die Dauer aus den Zügen.)
  const zuege = $$('.schreibzuege path');
  const maskeWeg = () => $('.unterschrift-gross use')?.removeAttribute('mask');
  let begonnen = false;
  const auftritt = () => {
    if (begonnen) return; begonnen = true;
    requestAnimationFrame(() => requestAnimationFrame(() => {
      document.body.classList.add('geladen');
      const l = zuege[zuege.length - 1];
      if (!l) return;
      if (ruhig.matches) return maskeWeg();
      const s = (v) => parseFloat(l.style.getPropertyValue(v)) || 0;
      setTimeout(maskeWeg, (s('--v') + s('--t') + 0.55 + 0.2) * 1000);
    }));
  };
  (document.fonts ? document.fonts.ready : Promise.resolve()).then(auftritt);
  setTimeout(auftritt, 1200);

  /* ───── Leiste weicht beim Runterscrollen aus ───── */
  const leiste = $('.leiste');
  const nav = $('.haupt-nav');
  const menue = $('.menue-knopf');
  let zuletzt = scrollY, weg = false;
  const navZu = () => { nav.classList.remove('offen'); menue.setAttribute('aria-expanded', 'false'); };
  addEventListener('scroll', () => {
    const y = scrollY, d = y - zuletzt;
    leiste.classList.toggle('gerollt', y > 8);
    if (Math.abs(d) < 6) return;
    const soll = d > 0 && y > leiste.offsetHeight * 2 && !nav.classList.contains('offen');
    if (soll !== weg) { weg = soll; leiste.classList.toggle('weg', weg); }
    zuletzt = y;
  }, { passive: true });
  leiste.addEventListener('focusin', () => { weg = false; leiste.classList.remove('weg'); });

  menue.addEventListener('click', () => {
    const auf = !nav.classList.contains('offen');
    nav.classList.toggle('offen', auf);
    menue.setAttribute('aria-expanded', String(auf));
  });
  nav.addEventListener('click', (e) => { if (e.target.closest('a')) navZu(); });
  document.addEventListener('keydown', (e) => { if (e.key === 'Escape' && nav.classList.contains('offen')) { navZu(); menue.focus(); } });

  /* ───── Kapitelname in der Leiste ───── */
  const anzeige = $('.leiste-kapitel');
  const abschnitte = $$('section[data-kapitel]');
  const sichtbar = new Set();
  const navLinks = $$('.haupt-nav a');
  const kapitelBeob = new IntersectionObserver((eintraege) => {
    for (const e of eintraege) e.isIntersecting ? sichtbar.add(e.target) : sichtbar.delete(e.target);
    const oben = abschnitte.find((a) => sichtbar.has(a));
    const text = oben ? oben.dataset.kapitel : '';
    if (anzeige.textContent !== text) {
      anzeige.textContent = text;
      anzeige.classList.remove('neu'); void anzeige.offsetWidth; anzeige.classList.add('neu');
    }
    navLinks.forEach((a) => {
      if (oben && a.hash === '#' + oben.id) a.setAttribute('aria-current', 'true');
      else a.removeAttribute('aria-current');
    });
  }, { rootMargin: '-30% 0px -60% 0px' });
  abschnitte.forEach((a) => kapitelBeob.observe(a));

  /* ───── Auftreten beim Scrollen, Geschwister leicht versetzt ───── */
  const zeigen = $$('.zeigen');
  if ('IntersectionObserver' in window && !ruhig.matches) {
    const beob = new IntersectionObserver((eintraege) => {
      let n = 0;
      for (const e of eintraege) {
        if (!e.isIntersecting) continue;
        e.target.style.setProperty('--folge', `${Math.min(n++, 4) * 90}ms`);
        e.target.classList.add('da');
        beob.unobserve(e.target);
      }
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });
    zeigen.forEach((el) => beob.observe(el));
  } else zeigen.forEach((el) => el.classList.add('da'));

  /* ───── Reiter ───── */
  const reiter = $('.reiter');
  if (reiter) {
    const tabs = $$('[role="tab"]', reiter);
    const tafeln = tabs.map((t) => document.getElementById(t.getAttribute('aria-controls')));
    reiter.hidden = false;
    const waehle = (i, fokus) => {
      tabs.forEach((t, j) => {
        const an = i === j;
        t.setAttribute('aria-selected', String(an));
        t.tabIndex = an ? 0 : -1;
        tafeln[j].hidden = !an;
      });
      tafeln[i].classList.remove('blendet'); void tafeln[i].offsetWidth; tafeln[i].classList.add('blendet');
      // Bilder in der neuen Tafel sofort zeigen
      $$('.zeigen', tafeln[i]).forEach((el) => el.classList.add('da'));
      if (fokus) { tabs[i].focus(); tabs[i].scrollIntoView({ block: 'nearest', inline: 'nearest' }); }
    };
    tabs.forEach((t, i) => {
      t.addEventListener('click', () => waehle(i));
      t.addEventListener('keydown', (e) => {
        const k = { ArrowRight: 1, ArrowLeft: -1, Home: -i, End: tabs.length - 1 - i }[e.key];
        if (k === undefined) return;
        e.preventDefault(); waehle((i + k + tabs.length) % tabs.length, true);
      });
    });
    tafeln.forEach((t, j) => { t.hidden = j !== 0; });
  }

  /* ───── Ansicht (Bild groß) ───── */
  const ansicht = $('.ansicht');
  const aBild = $('img', ansicht);
  const aEtikett = $('figcaption', ansicht);
  let reihe = [], stelle = 0, ausloeser = null;
  const zeige = (i) => {
    stelle = (i + reihe.length) % reihe.length;
    const k = reihe[stelle];
    const img = $('img', k);
    aBild.classList.remove('wechselt'); void aBild.offsetWidth; aBild.classList.add('wechselt');
    aBild.removeAttribute('srcset');
    aBild.src = k.dataset.gross;
    aBild.alt = img.alt;
    const et = k.closest('li, figure')?.querySelector('.etikett');
    aEtikett.innerHTML = et ? et.innerHTML : '';
    $('.lupe-hinweis', aEtikett)?.remove();
  };
  $$('.stueck-bild').forEach((k) => k.addEventListener('click', () => {
    const galerie = k.closest('.galerie');
    reihe = galerie ? $$('.stueck-bild', galerie) : [k];
    ansicht.classList.toggle('einzeln', reihe.length < 2);
    ausloeser = k; zeige(reihe.indexOf(k));
    ansicht.showModal();
  }));
  $('.ansicht-zu', ansicht).addEventListener('click', () => ansicht.close());
  $('.ansicht-zurueck', ansicht).addEventListener('click', () => zeige(stelle - 1));
  $('.ansicht-weiter', ansicht).addEventListener('click', () => zeige(stelle + 1));
  ansicht.addEventListener('keydown', (e) => {
    if (reihe.length < 2) return;
    if (e.key === 'ArrowLeft') zeige(stelle - 1);
    if (e.key === 'ArrowRight') zeige(stelle + 1);
  });
  ansicht.addEventListener('click', (e) => { if (e.target === ansicht || e.target.classList.contains('ansicht-figur')) ansicht.close(); });
  ansicht.addEventListener('close', () => ausloeser?.focus({ preventScroll: true }));
  // Wischen am Handy
  let wischX = null;
  ansicht.addEventListener('pointerdown', (e) => { if (e.pointerType !== 'mouse') wischX = e.clientX; });
  ansicht.addEventListener('pointerup', (e) => {
    if (wischX === null || reihe.length < 2) return;
    const d = e.clientX - wischX; wischX = null;
    if (Math.abs(d) > 50) zeige(stelle + (d < 0 ? 1 : -1));
  });

  /* ───── Lupe über der Disthen-Brosche ───── */
  const flaeche = $('.lupe-flaeche');
  const lupe = $('.lupe');
  if (flaeche && lupe) {
    const darf = () => feinZeiger.matches && innerWidth >= 960;
    const fein = 'bilder/disthen-brosche-3200.webp';
    const bild = $('img', flaeche);
    const ZOOM = 3;
    let geladen = false, x = 0, y = 0, laeuft = false;
    const zeichne = () => {
      laeuft = false;
      const r = bild.getBoundingClientRect(), f = flaeche.getBoundingClientRect();
      const L = lupe.offsetWidth;
      const fx = (x - r.left) / r.width, fy = (y - r.top) / r.height;
      lupe.style.setProperty('--x', `${x - f.left - L / 2}px`);
      lupe.style.setProperty('--y', `${y - f.top - L / 2}px`);
      lupe.style.backgroundSize = `${r.width * ZOOM}px ${r.height * ZOOM}px`;
      lupe.style.backgroundPosition = `${-(fx * r.width * ZOOM - L / 2 + 7)}px ${-(fy * r.height * ZOOM - L / 2 + 7)}px`;
    };
    flaeche.addEventListener('pointerenter', (e) => {
      if (!darf() || e.pointerType !== 'mouse') return;
      if (!geladen) {
        geladen = true;
        lupe.style.backgroundImage = `url("${bild.currentSrc || bild.src}")`;
        const hoch = new Image(); hoch.src = fein;
        hoch.decode().then(() => { lupe.style.backgroundImage = `url("${fein}")`; }).catch(() => {});
      }
      lupe.hidden = false; flaeche.classList.add('lupe-an');
      x = e.clientX; y = e.clientY; zeichne();
      requestAnimationFrame(() => { lupe.classList.add('da'); setTimeout(() => lupe.classList.add('folgt'), 360); });
    });
    flaeche.addEventListener('pointermove', (e) => {
      if (!flaeche.classList.contains('lupe-an')) return;
      x = e.clientX; y = e.clientY;
      if (!laeuft) { laeuft = true; requestAnimationFrame(zeichne); }
    });
    flaeche.addEventListener('pointerleave', () => {
      flaeche.classList.remove('lupe-an'); lupe.classList.remove('da', 'folgt');
    });
  }

  /* ───── Wechsel an derselben Stelle (Krokodilring) ───── */
  $$('.wechsel-knopf').forEach((k) => {
    const fig = document.getElementById(k.getAttribute('aria-controls'));
    k.addEventListener('click', () => {
      const b = fig.dataset.zeigt !== 'b';
      fig.dataset.zeigt = b ? 'b' : 'a';
      k.setAttribute('aria-pressed', String(b));
      k.textContent = b ? k.dataset.b : k.dataset.a;
    });
  });

  /* ───── „Heute geöffnet?“ in Münchner Zeit ───── */
  const TAGE = ['Sonntag', 'Montag', 'Dienstag', 'Mittwoch', 'Donnerstag', 'Freitag', 'Samstag'];
  const jetzt = () => {
    const t = Object.fromEntries(new Intl.DateTimeFormat('de-DE', {
      timeZone: 'Europe/Berlin', weekday: 'short', hour: '2-digit', minute: '2-digit', hour12: false,
    }).formatToParts(new Date()).map((p) => [p.type, p.value]));
    return { tag: ['So', 'Mo', 'Di', 'Mi', 'Do', 'Fr', 'Sa'].indexOf(t.weekday.replace('.', '')), min: (+t.hour % 24) * 60 + +t.minute };
  };
  const plan = (s) => {
    const p = {};
    for (const b of s.split(';')) {
      const m = b.trim().match(/^(\d)(?:-(\d))?\s+(\d\d):(\d\d)-(\d\d):(\d\d)$/);
      if (m) for (let d = +m[1]; d <= +(m[2] || m[1]); d++) p[d] = [m[3] * 60 + +m[4], m[5] * 60 + +m[6]];
    }
    return p;
  };
  const uhr = (m) => `${Math.floor(m / 60)}${m % 60 ? ':' + String(m % 60).padStart(2, '0') : ''} Uhr`;
  const zeit = jetzt();
  $$('[data-zeiten]').forEach((el) => {
    const p = plan(el.dataset.zeiten), h = p[zeit.tag];
    let satz, offen = false;
    if (h && zeit.min >= h[0] && zeit.min < h[1]) { satz = `Jetzt geöffnet, heute bis ${uhr(h[1])}`; offen = true; }
    else if (h && zeit.min < h[0]) satz = `Heute ab ${uhr(h[0])} geöffnet`;
    else for (let i = 1; i <= 7; i++) {
      const t = (zeit.tag + i) % 7;
      if (p[t]) { satz = `Geschlossen · ${i === 1 ? 'morgen' : TAGE[t]} ab ${uhr(p[t][0])}`; break; }
    }
    if (satz) { el.textContent = satz + ' · und nach Vereinbarung'; el.dataset.offen = offen ? 'ja' : 'nein'; }
  });
  $$('.zeiten [data-tage]').forEach((z) => {
    const [a, b] = z.dataset.tage.split('-').map(Number);
    if (zeit.tag >= a && zeit.tag <= (b || a)) z.classList.add('heute-zeile');
  });

  /* ───── Probierstein ───── */
  const stein = $('.probierstein-flaeche');
  const nadeln = $$('.nadeln input');
  // sRGB der Tokens --m-* aus stil.css (oklch → hex, siehe werkzeug/README.md)
  const FARBE = {
    'Silber 925': '#ced1d5', 'Gelbgold 750, mattiert': '#dab568', 'Gold 900': '#dba341', 'Rotgold 750': '#d09070',
    'Weißgold 750': '#cdcbbf', 'Palladium 500': '#abaeb2', 'Platin': '#bbbec1',
  };
  const NAME = (v) => v.replace(', mattiert', '');
  let streiche = []; // { metall, linie:[{x,y}], fasern, alpha, fortschritt, punze, frei }
  const zufall = (saat) => () => { saat = (saat * 16807) % 2147483647; return (saat - 1) / 2147483646; };
  const saatVon = (s) => [...s].reduce((h, c) => (h * 31 + c.charCodeAt(0)) % 2147483647, 7) || 1;
  const hash = (a, b) => { const x = Math.sin(a * 127.1 + b * 311.7) * 43758.5453; return x - Math.floor(x); };

  // Ein Probierstrich ist matter Abrieb: viele feine, leicht versetzte Fasern,
  // dichter in der Mitte, mit ausgefransten Enden und kleinen Aussetzern — kein Glanz.
  const fasern = (zz, n = 26) => Array.from({ length: n }, (_, i) => {
    const o = (zz() + zz() + zz()) / 1.5 - 1; // zur Mitte gehäuft
    return {
      i, o, w: 0.5 + zz() * 1.1, a: (0.1 + zz() * 0.22) * (1 - Math.abs(o) * 0.55),
      h: zz() * 0.24 - 0.1, s0: zz() * 16, s1: zz() * 18, wackel: zz() * 6.28,
    };
  });

  const neuerStrich = (metall, i) => {
    const zz = zufall(saatVon(metall));
    const bahn = 0.13 + i * (0.74 / 6);
    const x0 = 0.07 + zz() * 0.08, x1 = 0.62 + zz() * 0.16;
    const neig = (zz() - 0.5) * 0.06, phase = zz() * 6;
    const linie = [];
    for (let k = 0; k <= 16; k++) {
      const u = k / 16;
      linie.push({ x: x0 + (x1 - x0) * u, y: bahn + neig * (u - 0.5) + Math.sin(u * 3.1 + phase) * 0.006 });
    }
    return { metall, linie, fasern: fasern(zz), alpha: 1, fortschritt: 0, punze: $(`input[value="${metall}"]`).dataset.punze };
  };

  let ctx, W = 0, H = 0, dpr = 1, grund = null;
  const steinGrund = () => {
    // Kieselschiefer: fast schwarz, feines Korn, ein Hauch matter Glanz
    const c = document.createElement('canvas'); c.width = W; c.height = H;
    const g = c.getContext('2d');
    g.fillStyle = '#0f1113'; g.fillRect(0, 0, W, H);
    const zz = zufall(4711);
    for (let i = 0; i < (W * H) / 90; i++) {
      g.fillStyle = `rgba(${zz() < 0.5 ? '255,255,255' : '120,130,140'},${zz() * 0.035})`;
      g.fillRect(zz() * W, zz() * H, dpr, dpr);
    }
    for (let i = 0; i < 4; i++) { // Adern
      g.strokeStyle = `rgba(160,170,180,${0.025 + zz() * 0.03})`; g.lineWidth = dpr * (0.5 + zz());
      g.beginPath(); let x = zz() * W, y = 0; g.moveTo(x, y);
      while (y < H) { x += (zz() - 0.5) * 40 * dpr; y += 12 * dpr; g.lineTo(x, y); }
      g.stroke();
    }
    const glanz = g.createRadialGradient(W * 0.22, H * 0.1, 0, W * 0.22, H * 0.1, W * 0.7);
    glanz.addColorStop(0, 'rgba(255,255,255,0.06)'); glanz.addColorStop(1, 'rgba(255,255,255,0)');
    g.fillStyle = glanz; g.fillRect(0, 0, W, H);
    return c;
  };
  const hell = (hex, d) => {
    const n = parseInt(hex.slice(1), 16);
    const f = (v) => Math.max(0, Math.min(255, Math.round(v + d * 255)));
    return `rgb(${f(n >> 16)},${f((n >> 8) & 255)},${f(n & 255)})`;
  };
  const zeichneStrich = (st) => {
    const farbe = FARBE[st.metall];
    const P = st.linie.map((p) => ({ x: p.x * W, y: p.y * H }));
    if (P.length < 2) return;
    const lang = [0];
    for (let k = 1; k < P.length; k++) lang.push(lang[k - 1] + Math.hypot(P[k].x - P[k - 1].x, P[k].y - P[k - 1].y));
    const L = lang[lang.length - 1], bis = L * st.fortschritt, dicke = 10 * dpr, schritt = 3 * dpr;
    const an = (d) => { // Punkt und Normale bei Abstand d
      let k = 1; while (k < lang.length - 1 && lang[k] < d) k++;
      const a = P[k - 1], b = P[k], l = lang[k] - lang[k - 1] || 1, u = (d - lang[k - 1]) / l;
      return { x: a.x + (b.x - a.x) * u, y: a.y + (b.y - a.y) * u, nx: -(b.y - a.y) / l, ny: (b.x - a.x) / l };
    };
    ctx.lineCap = 'round';
    for (const f of st.fasern) {
      const von = f.s0 * dpr, nach = Math.min(bis, L - f.s1 * dpr);
      if (nach <= von) continue;
      ctx.globalAlpha = f.a * st.alpha;
      ctx.strokeStyle = hell(farbe, f.h);
      ctx.lineWidth = f.w * dpr;
      ctx.beginPath();
      let offen = false;
      for (let d = von; d <= nach; d += schritt) {
        const fach = Math.floor(d / (7 * dpr));
        if (hash(f.i, fach) < 0.1) { offen = false; continue; } // Aussetzer im Abrieb
        const q = an(d), o = f.o * dicke / 2 + Math.sin(d / (23 * dpr) + f.wackel) * 0.8 * dpr;
        const x = q.x + q.nx * o, y = q.y + q.ny * o;
        if (offen) ctx.lineTo(x, y); else { ctx.moveTo(x, y); offen = true; }
      }
      ctx.stroke();
    }
    if (st.punze && st.fortschritt >= 1) {
      const e = P[P.length - 1];
      ctx.globalAlpha = 0.7 * st.alpha;
      ctx.fillStyle = farbe;
      ctx.font = `600 ${11 * dpr}px "Hanken Grotesk", system-ui, sans-serif`;
      ctx.textBaseline = 'middle';
      ctx.fillText(st.punze, e.x + 14 * dpr, e.y);
    }
  };
  const zeichneStein = () => {
    if (!ctx) return;
    ctx.globalAlpha = 1;
    ctx.clearRect(0, 0, W, H);
    ctx.drawImage(grund, 0, 0);
    streiche.forEach(zeichneStrich);
    stein.parentElement.classList.toggle('beschrieben', streiche.some((x) => !x.weg));
    ctx.globalAlpha = 1;
  };
  let animiert = false;
  const lauf = () => {
    let weiter = false;
    for (const s of streiche) {
      if (s.weg) { s.alpha = Math.max(0, s.alpha - 0.07); weiter ||= s.alpha > 0; }
      else if (s.fortschritt < 1) { s.fortschritt = Math.min(1, s.fortschritt + 0.028); weiter = true; }
    }
    streiche = streiche.filter((s) => !(s.weg && s.alpha <= 0));
    zeichneStein();
    if (weiter) requestAnimationFrame(lauf); else animiert = false;
  };
  const bewege = () => { if (!animiert) { animiert = true; requestAnimationFrame(lauf); } };
  const masse = () => {
    const r = stein.getBoundingClientRect();
    dpr = Math.min(2, devicePixelRatio || 1);
    W = Math.round(r.width * dpr); H = Math.round(r.height * dpr);
    if (!W || !H) return;
    stein.width = W; stein.height = H;
    ctx = stein.getContext('2d');
    grund = steinGrund();
    zeichneStein();
  };
  if (stein) {
    masse();
    new ResizeObserver(masse).observe(stein);
    document.fonts?.ready.then(zeichneStein);
    nadeln.forEach((n, i) => n.addEventListener('change', () => {
      if (n.checked) {
        streiche = streiche.filter((s) => s.metall !== n.value || !s.weg);
        if (!streiche.some((s) => s.metall === n.value && !s.frei)) {
          const s = neuerStrich(n.value, i);
          if (ruhig.matches) s.fortschritt = 1;
          streiche.push(s);
        }
      } else streiche.forEach((s) => { if (s.metall === n.value) s.weg = true; });
      if (ruhig.matches) { streiche = streiche.filter((s) => !s.weg); zeichneStein(); } else bewege();
      steinStand();
    }));
    // Mit der Maus selbst über den Stein streichen (mit der zuletzt gewählten Nadel)
    let zug = null, letzteNadel = null;
    nadeln.forEach((n) => n.addEventListener('change', () => { if (n.checked) letzteNadel = n.value; else if (letzteNadel === n.value) letzteNadel = nadeln.filter((x) => x.checked).pop()?.value ?? null; }));
    const pos = (e) => { const r = stein.getBoundingClientRect(); return { x: (e.clientX - r.left) / r.width, y: (e.clientY - r.top) / r.height }; };
    stein.addEventListener('pointerdown', (e) => {
      if (e.pointerType !== 'mouse' && e.pointerType !== 'pen') return;
      if (!letzteNadel) { $('.probierstein-stand').textContent = 'Wählen Sie zuerst eine Probiernadel.'; return; }
      zug = { metall: letzteNadel, linie: [pos(e)], fasern: fasern(zufall(Date.now() % 100000 + 1)), alpha: 1, fortschritt: 1, frei: true };
      streiche.push(zug);
      stein.setPointerCapture(e.pointerId);
    });
    stein.addEventListener('pointermove', (e) => {
      if (!zug) return;
      const p = pos(e), l = zug.linie[zug.linie.length - 1];
      if (Math.hypot(p.x - l.x, (p.y - l.y) * H / W) < 0.006) return;
      zug.linie.push(p);
      zeichneStein();
    });
    const ende = () => { if (zug && zug.linie.length < 2) streiche = streiche.filter((x) => x !== zug); zug = null; };
    stein.addEventListener('pointerup', ende); stein.addEventListener('pointercancel', ende);
  }
  function steinStand() {
    const gewaehlt = nadeln.filter((n) => n.checked).map((n) => NAME(n.value));
    const el = $('.probierstein-stand');
    el.textContent = gewaehlt.length ? `Auf dem Stein: ${liste(gewaehlt)}.` : '';
  }

  /* ───── Anfrage: Auswahl → Nachricht ───── */
  const form = $('.baukasten');
  const feld = form && $('textarea', form);
  const senden = form && $('.brief-senden', form);
  function liste(a) { return a.length < 2 ? a.join('') : a.slice(0, -1).join(', ') + ' und ' + a[a.length - 1]; }
  // Jede Zeile hat einen festen Platz; null = Zeile entfällt
  const zeilen = () => {
    const f = new FormData(form);
    const was = f.get('was');
    const metalle = f.getAll('metall').map(NAME);
    const stein = f.get('stein');
    const anlass = (f.get('anlass') || '').trim();
    const name = (f.get('name') || '').trim();
    let satz = `ich interessiere mich für ${was || 'ein Unikat aus Ihrer Werkstatt'}`;
    if (metalle.length) satz += ` in ${liste(metalle)}`;
    if (stein === 'sammlung') satz += ', mit einem Stein aus Ihrer Sammlung';
    if (stein === 'ohne') satz += ', ohne Stein';
    satz += '.';
    return [
      'Guten Tag Frau Kusche,', '',
      satz,
      stein === 'eigener' ? 'Einen eigenen Stein bringe ich mit.' : null,
      anlass ? `Anlass / Wunschtermin: ${anlass}` : null,
      was === 'Eheringe' ? 'Wann dürfen wir zu zweit zur Beratung vorbeikommen?' : 'Wann darf ich zur Beratung vorbeikommen?', '',
      'Viele Grüße',
      name || null,
    ];
  };
  const text = (z) => z.filter((l) => l !== null).join('\n');
  let vorher = form ? zeilen() : null;
  const betreff = () => {
    const was = new FormData(form).get('was');
    const kurz = { 'einen Ring': 'Ring', 'eine Kette oder einen Anhänger': 'Kette oder Anhänger', 'eine Brosche': 'Brosche', 'die Restaurierung eines Schmuckstücks': 'Restaurierung' }[was] || was;
    return kurz ? `Anfrage: ${kurz}` : 'Anfrage über die Website';
  };
  const mailto = () => {
    senden.href = `mailto:${form.dataset.mail}?subject=${encodeURIComponent(betreff())}&body=${encodeURIComponent(feld.value)}`;
  };
  const aktualisiere = () => {
    const neu = zeilen();
    if (feld.value === text(vorher)) feld.value = text(neu);
    else {
      // Von Hand geänderte Zeilen bleiben; nur erzeugte Zeilen werden ersetzt
      let l = feld.value.split('\n');
      neu.forEach((z, i) => {
        const alt = vorher[i];
        if (alt === z || (alt === '' && z === '')) return;
        const at = alt ? l.indexOf(alt) : -1;
        if (at >= 0) { if (z === null) l.splice(at, 1); else l[at] = z; return; }
        if (alt === null && z !== null) {
          // Einfügen hinter der nächsten vorhandenen Vorgängerzeile
          for (let j = i - 1; j >= 0; j--) {
            const anker = neu[j] && l.indexOf(neu[j]);
            if (anker >= 0) { l.splice(anker + 1, 0, z); return; }
          }
          l.push(z);
        }
      });
      feld.value = l.join('\n');
    }
    vorher = neu;
    mailto();
  };
  if (form) {
    form.addEventListener('input', (e) => { if (e.target !== feld) aktualisiere(); else mailto(); });
    form.addEventListener('change', (e) => { if (e.target !== feld) aktualisiere(); });
    form.addEventListener('submit', (e) => e.preventDefault());
    feld.value = text(vorher); mailto();
    const stand = $('.brief-stand', form);
    $('.brief-kopieren', form).addEventListener('click', async () => {
      try { await navigator.clipboard.writeText(feld.value); }
      catch { feld.select(); document.execCommand('copy'); }
      stand.textContent = 'Der Text ist kopiert.';
      setTimeout(() => { stand.textContent = ''; }, 3500);
    });
  }
})();
