// Banco del Dino — tiempo virtual y azar sembrado. Se inyecta ANTES que el juego.
// performance.now y requestAnimationFrame quedan bajo control del banco: cada
// __vt.step(dt) avanza el reloj dt ms y corre los callbacks pendientes, como un
// cuadro real. Math.random queda sembrado (mulberry32) para que cada partida se
// pueda repetir con la misma semilla.
(() => {
  let vt = 1000;
  performance.now = () => vt;
  let rafQ = []; let rafId = 1;
  window.requestAnimationFrame = cb => { const id = rafId++; rafQ.push({ id, cb }); return id; };
  window.cancelAnimationFrame = id => { rafQ = rafQ.filter(r => r.id !== id); };
  let s = 1;
  Math.random = () => { s = (s + 0x6D2B79F5) | 0; let t = Math.imul(s ^ (s >>> 15), 1 | s); t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t; return ((t ^ (t >>> 14)) >>> 0) / 4294967296; };
  window.__vt = {
    get now() { return vt; },
    seed(x) { s = x | 0; },
    step(dt) { vt += dt; const q = rafQ; rafQ = []; for (const r of q) r.cb(vt); },
    advance(dt) { vt += dt; },
    pending() { return rafQ.length; },
  };
})();
