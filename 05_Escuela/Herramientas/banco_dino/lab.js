// Banco del Dino — laboratorio. Se inyecta junto con vt.js, antes que el juego.
//
// Dos maneras de medir, las dos con el CÓDIGO REAL del juego:
//   1. El Runner entero corriendo (Lab.init / Lab.start / __vt.step), con teclas
//      despachadas como eventos del documento: lo que el jugador vería.
//   2. Clones de las clases reales (Trex, Obstacle) en un mundo de laboratorio que
//      repite el ORDEN de Runner.update: salto -> obstáculos -> colisión con el
//      PRIMER obstáculo -> aceleración -> animación. Sirve para barrer cuándo
//      apretar sin tener que jugar miles de partidas.
// Ningún cálculo de colisión está reescrito: se llama a Runner.prototype.checkForCollision.
window.Lab = (() => {
  const L = {};
  L.key = (type, code) => document.dispatchEvent(new KeyboardEvent(type, { keyCode: code, bubbles: true }));
  L.init = (seed = 1) => { __vt.seed(seed); L.R = DinoLab.Runner.initializeInstance('.interstitial-wrapper'); L.proto = DinoLab.Runner.prototype; return L.R; };

  // Paso de cuadro con jitter gaussiano opcional (ms). El jitter usa su propio
  // generador para no consumir el azar del juego.
  L.dtGen = (hz, jitter = 0) => {
    let js = 12345; const jr = () => { js = (js + 0x6D2B79F5) | 0; let t = Math.imul(js ^ (js >>> 15), 1 | js); t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t; return ((t ^ (t >>> 14)) >>> 0) / 4294967296; };
    const gj = () => { let u, v, s; do { u = jr() * 2 - 1; v = jr() * 2 - 1; s = u * u + v * v; } while (s >= 1 || s === 0); return u * Math.sqrt(-2 * Math.log(s) / s); };
    return () => 1000 / hz + (jitter ? gj() * jitter : 0);
  };

  // Primer salto + intro. La intro del juego termina con un evento de animación CSS
  // de 0.4 s; acá se despacha a los 0.4 s de tiempo virtual, como en el navegador.
  L.start = (hz = 60) => {
    const R = L.R, dt = 1000 / hz;
    L.key('keydown', 32); L.key('keyup', 32);
    let g = 0; while (!R.playingIntro && g++ < 2000) __vt.step(dt);
    const t0 = __vt.now; while (__vt.now - t0 < 400) __vt.step(dt);
    R.containerEl.dispatchEvent(new Event('webkitAnimationEnd'));
  };
  // Choque y reinicio con Enter: deja UN solo bucle de actualización (ver 'velocidad').
  L.restart = (hz = 60) => { L.R.gameOver(); __vt.step(1000 / hz); L.key('keyup', 13); };
  L.god = on => { if (on) L.R.checkForCollision = () => null; else delete L.R.checkForCollision; };
  L.collide = (o, t) => L.proto.checkForCollision.call(L.R, o, t);

  // ---- clones en un lienzo que no dibuja ----
  const dummy = new Proxy({}, { get: (t, k) => (k in t ? t[k] : () => {}), set: (t, k, v) => { t[k] = v; return true; } });
  L.cloneTrex = t => { const c = Object.assign(Object.create(Object.getPrototypeOf(t)), t); c.canvasCtx = dummy; return c; };
  L.cloneObs = o => { const c = Object.assign(Object.create(Object.getPrototypeOf(o)), o); c.canvasCtx = dummy; return c; };
  L.groundTrex = () => { const t = L.cloneTrex(L.R.tRex); t.reset(); return t; };

  // Teclas, con las mismas condiciones que Runner.onKeyDown / onKeyUp.
  L.input = (S, k) => { const t = S.trex;
    if (k === 'jd') { if (!t.jumping && !t.ducking) t.startJump(S.speed); }
    else if (k === 'ju') { t.endJump(); }
    else if (k === 'dd') { if (t.jumping) t.setSpeedDrop(); else if (!t.ducking) t.setDuck(true); }
    else if (k === 'du') { t.speedDrop = false; t.setDuck(false); } };

  // Un cuadro del mundo de laboratorio. Si S.pend existe, inyecta el segundo
  // obstáculo con la regla de Horizon.updateObstacles (hueco libre o lista vacía).
  L.step = (S, dt) => { const t = S.trex;
    if (t.jumping) t.updateJump(dt);
    const keep = S.obs.slice(0);
    for (const o of S.obs) { o.update(dt, S.speed); if (o.remove) keep.shift(); }
    S.obs = keep;
    if (S.pend && (S.obs.length === 0 || (S.src.isVisible() && S.src.xPos + S.src.width + S.src.gap < 600))) { S.obs.push(L.cloneObs(S.pend)); S.pend = null; }
    const f = S.obs[0];
    if (f && !S.ghostAll && !(S.ghost && f === S.src) && L.collide(f, t)) return true;
    if (S.speed < S.max) S.speed += S.acc;
    t.update(dt);
    return false; };

  // Obstáculo de un tipo, tamaño y altura dados, armado con el constructor real.
  L.mkObs = (type, size, y, off, x, speed) => {
    const R = L.R, H = R.horizon;
    const tc = H.obstacleTypes.find(t => t.type === type);
    const o = new DinoLab.Obstacle(R.canvasCtx, tc, H.spritePos[type], R.dimensions, H.gapCoefficient, speed, tc.width, R, false);
    o.size = size; o.cloneCollisionBoxes(); o.width = tc.width * size;
    if (size > 1) { o.collisionBoxes[1].width = o.width - o.collisionBoxes[0].width - o.collisionBoxes[2].width; o.collisionBoxes[2].x = o.width - o.collisionBoxes[2].width; }
    if (y !== null) o.yPos = y;
    o.speedOffset = off || 0; o.xPos = x; o.followingObstacleCreated = true;
    return L.cloneObs(o);
  };
  const evMap = acts => { const ev = new Map(); for (const [k, f] of acts) { if (f === null || f === undefined) continue; if (!ev.has(f)) ev.set(f, []); ev.get(f).push(k); } return ev; };
  const minBx = o => Math.min(...o.collisionBoxes.map(b => b.x));

  // Un obstáculo solo, un guion de teclas. Devuelve el cuadro del choque o -1.
  L.simAct = (trex, obsList, speed, acc, dt, acts, maxF = 400) => {
    const S = { trex: L.cloneTrex(trex), obs: obsList.map(L.cloneObs), speed, acc, max: 13 };
    const ev = evMap(acts); const tx = S.trex.xPos;
    for (let f = 0; f < maxF; f++) {
      const e = ev.get(f); if (e) for (const k of e) L.input(S, k);
      if (L.step(S, dt)) return { crash: f };
      if (!S.obs.length || (S.obs.every(o => o.xPos + o.width < tx) && !S.trex.jumping)) return { crash: -1, end: f };
    }
    return { crash: -1, end: maxF };
  };

  // Par real del generador: O1 desde su nacimiento, O2 inyectado cuando el juego lo haría.
  // stop: 'land1' (O1 pasado y en el piso) | 'both' | 'arr1' / 'arr2' (sin colisiones:
  // cuadro en que la caja delantera del obstáculo llega al frente del T-Rex).
  L.runPair = (P, acts, stop, maxF = 260, ghost = false) => {
    const o1 = L.cloneObs(P.o1);
    const S = { trex: L.cloneTrex(P.trex), obs: [o1], src: o1, pend: P.o2, speed: P.v, acc: P.acc, max: 13, ghost, ghostAll: stop.startsWith('arr') };
    const ev = evMap(acts); const tx = S.trex.xPos;
    for (let f = 0; f < maxF; f++) {
      const e = ev.get(f); if (e) for (const k of e) L.input(S, k);
      if (L.step(S, 1000 / P.hz)) return { crash: f };
      if (stop === 'land1' && o1.xPos + o1.width < tx && !S.trex.jumping) return { crash: -1, land: f };
      if (stop === 'both' && !S.pend && S.obs.every(o => o.xPos + o.width < tx) && !S.trex.jumping) return { crash: -1, land: f };
      if (stop === 'arr1' && o1.xPos + 1 + minBx(o1) <= tx + 40) return { crash: -1, arr: f };
      if (stop === 'arr2' && !S.pend && S.obs.length && S.obs.at(-1).xPos + 1 + minBx(S.obs.at(-1)) <= tx + 40) return { crash: -1, arr: f };
    }
    return { crash: -1, land: maxF, timeout: true };
  };

  // ---- bot ----
  // Respuesta natural: cactus y volador bajo se saltan, el medio se agacha, el alto se deja pasar.
  L.natural = o => o.typeConfig.type !== 'pterodactyl' ? 'jump' : (o.yPos === 100 ? 'jump' : o.yPos === 75 ? 'duck' : 'none');
  L.world = () => { const R = L.R; return { trex: L.cloneTrex(R.tRex), obs: R.horizon.obstacles.map(L.cloneObs), speed: R.currentSpeed, acc: R.config.acceleration * (L.chains || 1), max: R.config.maxSpeed }; };
  L.simW = (W0, ev, untilIdx, dt, maxF = 200) => {
    const S = { trex: L.cloneTrex(W0.trex), obs: W0.obs.map(L.cloneObs), speed: W0.speed, acc: W0.acc, max: W0.max };
    const target = S.obs[untilIdx]; const tx = S.trex.xPos;
    for (let f = 0; f < maxF; f++) { const e = ev[f]; if (e) for (const k of e) L.input(S, k); if (L.step(S, dt)) return { crash: f }; if (target.xPos + target.width < tx && !S.trex.jumping) return { crash: -1, land: f }; }
    return { crash: -1, land: maxF };
  };
  // Una partida del bot en el Runner real. Ve cada obstáculo cuando entra a pantalla,
  // puede actuar recién R_ms después, solo desde el piso, apunta al centro de la
  // ventana que todavía queda (prefiriendo, si ya ve el siguiente, las presiones que
  // lo dejan pasable) y aprieta con error gaussiano sigma_ms. Registra cada plan en L.plans.
  L.botGame = opts => {
    const R = L.R, dt = 1000 / opts.hz; let t = 0, frame = 0; const tx = R.tRex.xPos;
    const vis = new Map(); const handled = new Set(); let plan = null; L.plans = []; L.duckObj = null; const commits = [];
    let bs = opts.botSeed | 0; const br = () => { bs = (bs + 0x6D2B79F5) | 0; let x = Math.imul(bs ^ (bs >>> 15), 1 | bs); x = (x + Math.imul(x ^ (x >>> 7), 61 | x)) ^ x; return ((x ^ (x >>> 14)) >>> 0) / 4294967296; };
    const gauss = () => { let u, v, s; do { u = br() * 2 - 1; v = br() * 2 - 1; s = u * u + v * v; } while (s >= 1 || s === 0); return u * Math.sqrt(-2 * Math.log(s) / s); };
    const fire = k => L.key(k[1] === 'd' ? 'keydown' : 'keyup', k[0] === 'j' ? 32 : 40);
    const PH = Math.round(2000 / dt);
    while (t < opts.maxT && !R.crashed) {
      const obs = R.horizon.obstacles;
      for (const o of obs) if (!vis.has(o) && o.xPos < 600) vis.set(o, frame);
      if (plan) { for (const [k, f] of plan.ev) if (f === frame) fire(k); if (frame >= plan.end) plan = null; }
      if (!plan && !R.tRex.jumping) {
        const idx = obs.findIndex(o => !handled.has(o) && o.xPos + o.width >= tx);
        if (idx >= 0) {
          const o = obs[idx]; const nat = L.natural(o);
          const earliest = vis.has(o) ? vis.get(o) + Math.round(opts.R_ms / dt) : Infinity;
          if (nat === 'none') handled.add(o);
          else if (frame >= earliest && nat === 'duck') { fire('dd'); L.duckObj = o; handled.add(o); }
          else if (frame >= earliest) {
            const W0 = L.world(); const ok = [];
            for (let p = 0; p < PH; p++) { const ev = {}; ev[p] = ['jd']; if (L.simW(W0, ev, idx, dt, PH + Math.round(1500 / dt)).crash < 0) ok.push(p); }
            let cand = ok;
            if (ok.length && idx + 1 < W0.obs.length && L.natural(W0.obs[idx + 1]) === 'jump') {
              const joint = ok.filter(p => { for (let p2 = p + Math.round(300 / dt); p2 < p + Math.round(1500 / dt); p2++) { const ev = {}; ev[p] = ['jd']; ev[p2] = ['jd']; if (L.simW(W0, ev, idx + 1, dt, Math.round(4000 / dt)).crash < 0) return true; } return false; });
              if (joint.length) cand = joint;
            }
            handled.add(o);
            if (cand.length) {
              const c = cand[Math.floor(cand.length / 2)];
              let p = Math.round(c + gauss() * opts.sigma_ms / dt); if (p < 0) p = 0;
              const rel = Math.max(1, Math.round(opts.hold_ms / dt));
              plan = { ev: [['jd', frame + p], ['ju', frame + p + rel]], end: frame + p + rel };
              for (const [k, f] of plan.ev) if (f === frame) fire(k);
              L.plans.push({ v: +R.currentSpeed.toFixed(2), ok: ok.length, cand: cand.length, type: o.typeConfig.type + o.size }); commits.push({ o, press: frame + p });
            }
          }
        }
      }
      if (L.duckObj && (L.duckObj.xPos + L.duckObj.width < tx || !obs.includes(L.duckObj))) { fire('du'); L.duckObj = null; }
      __vt.step(dt); t += dt; frame++;
    }
    const f0 = R.horizon.obstacles[0];
    // Muerte "ciega": el obstáculo que mató se vio recién después de que ya no se podía
    // corregir el salto anterior (visible + reacción > presión del salto anterior).
    const prev = commits.filter(c => c.o !== f0).at(-1);
    const ciega = !!(R.crashed && f0 && prev && vis.has(f0) && vis.get(f0) + Math.round(opts.R_ms / dt) > prev.press);
    return { t: +(t / 1000).toFixed(2), crashed: R.crashed, ciega, score: R.distanceMeter.getActualDistance(Math.ceil(R.distanceRan)), speed: +R.currentSpeed.toFixed(2), killer: f0 ? f0.typeConfig.type + f0.size + '@' + f0.yPos : null };
  };
  return L;
})();
