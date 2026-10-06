#!/usr/bin/env node
// Banco del Dino — mide el Chrome Dino CORRIENDO, no calculado sobre el código.
//
// Baja el juego de Chromium en un commit fijo (licencia BSD; no se aloja en el vault:
// se descarga a la carpeta de trabajo), lo compila tal cual con dos shims de
// chrome://resources, y lo corre en Chromium sin cabeza con tiempo virtual
// (vt.js) y el laboratorio de lab.js. Cada número de 05_Endless_runner que dice
// "medido (EST-021)" sale de un experimento de acá.
//
// Uso (Node >= 18, red para npm y raw.githubusercontent.com):
//   node medir.mjs [experimento ...] [--trabajo DIR] [--chrome RUTA] [--rapido]
//   experimentos: velocidad salto ventanas pares bot estados real   (sin nombre: todos menos 'real')
//   --trabajo  carpeta FUERA del vault para node_modules, fuentes y build (default: <tmp>/banco_dino)
//   --chrome   ejecutable de Chromium/Chrome (default: el de Playwright; `npx playwright install chromium`)
//   --rapido   menos semillas y partidas (para probar que corre, no para citar)
//
// Semillas fijas: dos corridas con los mismos argumentos dan los mismos números.
import fs from 'fs';
import os from 'os';
import path from 'path';
import { execSync } from 'child_process';
import { createRequire } from 'module';
import { fileURLToPath } from 'url';

const AQUI = path.dirname(fileURLToPath(import.meta.url));
const COMMIT = '9b4a14466a0e';
const RAW = `https://raw.githubusercontent.com/chromium/chromium/${COMMIT}/components/neterror/resources`;
const FUENTES = ['offline.ts', 'horizon.ts', 'obstacle.ts', 'trex.ts', 'distance_meter.ts', 'cloud.ts', 'night_mode.ts', 'horizon_line.ts', 'background_el.ts', 'constants.ts', 'dimensions.ts', 'game_over_panel.ts', 'generated_sound_fx.ts', 'offline_sprite_definitions.ts', 'utils.ts', 'game_state_provider.ts', 'image_sprite_provider.ts', 'sprite_position.ts', 'game_config.ts'];

const args = process.argv.slice(2);
const opt = (k, d) => { const i = args.indexOf(k); return i >= 0 ? args[i + 1] : d; };
const RAPIDO = args.includes('--rapido');
const TRABAJO = path.resolve(opt('--trabajo', path.join(os.tmpdir(), 'banco_dino')));
const CHROME = opt('--chrome', undefined);
const pedidos = args.filter((a, i) => !a.startsWith('--') && !['--trabajo', '--chrome'].includes(args[i - 1]));
const TODOS = ['velocidad', 'salto', 'ventanas', 'pares', 'bot', 'estados'];
const EXP = pedidos.length ? pedidos : TODOS;

// ---------- preparar: dependencias, fuentes fijadas, build ----------
async function preparar() {
  fs.mkdirSync(path.join(TRABAJO, 'src'), { recursive: true });
  if (!fs.existsSync(path.join(TRABAJO, 'node_modules', 'playwright')) || !fs.existsSync(path.join(TRABAJO, 'node_modules', 'esbuild'))) {
    if (!fs.existsSync(path.join(TRABAJO, 'package.json'))) fs.writeFileSync(path.join(TRABAJO, 'package.json'), '{"private":true}');
    execSync('npm install --no-audit --no-fund esbuild playwright@1', { cwd: TRABAJO, stdio: 'inherit' });
  }
  const bajar = async (url, dest, bin = false) => { if (fs.existsSync(dest)) return; const r = await fetch(url); if (!r.ok) throw new Error(`${r.status} ${url}`); fs.writeFileSync(dest, bin ? Buffer.from(await r.arrayBuffer()) : await r.text()); };
  for (const f of FUENTES) await bajar(`${RAW}/dino_game/${f}`, path.join(TRABAJO, 'src', f));
  await bajar(`${RAW}/constants.ts`, path.join(TRABAJO, 'constants.ts'));
  await bajar(`${RAW}/images/default_100_percent/offline/100-offline-sprite.png`, path.join(TRABAJO, 'sprite1x.png'), true);
  const shims = path.join(TRABAJO, 'shims'); fs.mkdirSync(shims, { recursive: true });
  fs.writeFileSync(path.join(shims, 'assert.js'), "export function assert(c, m) { if (!c) throw new Error('assert: ' + (m || '')); }\nexport function assertNotReached(m) { throw new Error(m); }\n");
  fs.writeFileSync(path.join(shims, 'load_time_data.js'), "export const loadTimeData = { valueExists: () => false, getString: () => '', getValue: () => '', getBoolean: () => false, getInteger: () => 0 };\n");
  fs.writeFileSync(path.join(TRABAJO, 'entry.ts'), "import {Runner} from './src/offline.js';\nimport {Trex} from './src/trex.js';\nimport {Obstacle} from './src/obstacle.js';\n(window as any).DinoLab = {Runner, Trex, Obstacle};\n");
  const req = createRequire(path.join(TRABAJO, 'package.json'));
  const esbuild = req('esbuild');
  await esbuild.build({ entryPoints: [path.join(TRABAJO, 'entry.ts')], bundle: true, format: 'iife', outfile: path.join(TRABAJO, 'dino.js'), target: 'es2020', logLevel: 'warning',
    plugins: [{ name: 'shims', setup(b) {
      b.onResolve({ filter: /^chrome:\/\/resources\/js\// }, a => ({ path: path.join(shims, a.path.split('/').pop()) }));
      b.onResolve({ filter: /\.js$/ }, a => a.path.startsWith('.') ? { path: path.resolve(path.dirname(a.importer), a.path.replace(/\.js$/, '.ts')) } : undefined);
    } }] });
  // Página mínima con los recursos que el Runner busca (sprite, sonidos mudos, contenedor de 600 px).
  const wav = Buffer.concat([Buffer.from('RIFF'), Buffer.from([44, 0, 0, 0]), Buffer.from('WAVEfmt '), Buffer.from([16, 0, 0, 0, 1, 0, 1, 0, 0x40, 0x1f, 0, 0, 0x40, 0x1f, 0, 0, 1, 0, 8, 0]), Buffer.from('data'), Buffer.from([8, 0, 0, 0]), Buffer.alloc(8, 0x80)]).toString('base64');
  const spr = fs.readFileSync(path.join(TRABAJO, 'sprite1x.png')).toString('base64');
  const au = id => `<audio id="${id}" src="data:audio/wav;base64,${wav}"></audio>`;
  fs.writeFileSync(path.join(TRABAJO, 'index.html'), `<!doctype html><html dir="ltr"><head><meta charset="utf-8"><style>body{margin:0}.interstitial-wrapper{width:600px;padding:0;margin:20px 0}.hidden{display:none}.runner-container{height:150px;width:44px;overflow:hidden}</style></head><body><div class="interstitial-wrapper"><div class="icon icon-offline"></div></div><div id="offline-resources"><img id="offline-resources-1x" src="data:image/png;base64,${spr}"><template id="audio-resources">${au('offline-sound-press')}${au('offline-sound-hit')}${au('offline-sound-reached')}</template></div><script src="dino.js"></script></body></html>`);
  return req('playwright');
}

let PW, BROWSER;
async function pagina() {
  const page = await BROWSER.newPage({ viewport: { width: 800, height: 400 }, deviceScaleFactor: 1 });
  page.on('pageerror', e => console.error('ERROR EN PÁGINA:', e.message));
  await page.addInitScript({ path: path.join(AQUI, 'vt.js') });
  await page.addInitScript({ path: path.join(AQUI, 'lab.js') });
  await page.goto('file://' + path.join(TRABAJO, 'index.html'));
  return page;
}
const conPagina = async fn => { const p = await pagina(); try { return await fn(p); } finally { await p.close(); } };
const f2 = x => (x === null || x === undefined) ? '—' : (+x).toFixed(2);
const med = a => { const s = [...a].sort((x, y) => x - y); return s.length ? s[Math.floor(s.length / 2)] : null; };

// ---------- experimentos ----------
const E = {};

// Curva de velocidad, ventana de anticipación y posición del T-Rex, por frecuencia y por bucle.
//  doble   = primera partida, arrancada mientras el T-Rex parpadea (dos bucles de rAF)
//  reinicio = partida después de un choque (un bucle)
E.velocidad = async () => {
  console.log('\n== VELOCIDAD: tiempo hasta vmax y ventana de anticipación (s) ==');
  console.log('Hz   bucle     jitter  T-Rex x  Δv/cuadro  t(vmax)  ventana inicio   ventana a tope   volador a tope');
  const casos = [[60, 'doble', 0], [60, 'reinicio', 0], [60, 'reinicio', 0.5], [120, 'doble', 0], [120, 'reinicio', 0], [144, 'doble', 0], [144, 'reinicio', 0]];
  for (const [hz, modo, jit] of casos) {
    const r = await conPagina(p => p.evaluate(([hz, modo, jit]) => {
      const R = Lab.init(11); Lab.start(hz); if (modo === 'reinicio') Lab.restart(hz); Lab.god(true);
      const dtg = Lab.dtGen(hz, jit); const front = R.tRex.xPos + 40; const seen = new Map(); const wins = [], pts = [];
      let t = 0, tmax = null; const s0 = R.currentSpeed; __vt.step(dtg()); const dv = R.currentSpeed - s0;
      while (t < 140000) {
        const dt = dtg(); __vt.step(dt); t += dt;
        for (const o of R.horizon.obstacles) {
          let s = seen.get(o); if (!s) { s = {}; seen.set(o, s); }
          const mb = Math.min(...o.collisionBoxes.map(b => b.x));
          if (s.vis === undefined && o.xPos < 600) s.vis = t;
          if (s.vis !== undefined && s.arr === undefined && o.xPos + 1 + mb <= front) { s.arr = t; if (!o.speedOffset) wins.push([t, s.arr - s.vis]); else pts.push([R.currentSpeed, s.arr - s.vis]); }
        }
        if (tmax === null && R.currentSpeed >= R.config.maxSpeed) tmax = t / 1000;
      }
      const a = wins.filter(w => w[0] < 12000).map(w => w[1]), b = wins.filter(w => w[0] > tmax * 1000 + 3000).map(w => w[1]);
      const p2 = pts.filter(w => w[0] >= 13).map(w => w[1]);
      return { x: R.tRex.xPos, dv, tmax, ini: [Math.min(...a), Math.max(...a)], fin: [Math.min(...b), Math.max(...b)], v2: [Math.min(...p2), Math.max(...p2)] };
    }, [hz, modo, jit]));
    console.log(`${String(hz).padEnd(5)}${modo.padEnd(10)}${String(jit).padEnd(8)}${String(r.x).padEnd(9)}${r.dv.toFixed(4).padEnd(11)}${r.tmax.toFixed(1).padEnd(9)}${(f2(r.ini[0] / 1000) + '–' + f2(r.ini[1] / 1000)).padEnd(16)}${(f2(r.fin[0] / 1000) + '–' + f2(r.fin[1] / 1000)).padEnd(17)}${f2(r.v2[0] / 1000)}–${f2(r.v2[1] / 1000)}`);
  }
  // Velocidad del mundo a tope: desplazamiento real por cuadro (Math.floor) contra la nominal.
  console.log('\nvelocidad del mundo a tope (px/s), nominal 780:');
  for (const [hz, jit] of [[60, 0], [60, 0.5], [75, 0], [90, 0], [120, 0], [144, 0], [165, 0]]) {
    const v = await conPagina(p => p.evaluate(([hz, jit]) => {
      const R = Lab.init(11); Lab.start(hz); Lab.restart(hz); Lab.god(true); R.currentSpeed = 13 + R.config.acceleration; // el tope real: el último incremento lo pasa de 13
      const dtg = Lab.dtGen(hz, jit); let px = 0, ms = 0;
      for (let i = 0; i < hz * 20; i++) { const o = R.horizon.obstacles[0]; const x = o && o.xPos; const dt = dtg(); __vt.step(dt); if (o && R.horizon.obstacles[0] === o && !o.speedOffset) { px += x - o.xPos; ms += dt; } }
      return px / ms * 1000;
    }, [hz, jit]));
    console.log(`  ${hz} Hz${jit ? ' ±' + jit + ' ms' : ''}: ${v.toFixed(0)}`);
  }
};

// El salto: altura y tiempo en el aire según cuánto se sostiene la tecla, y la caída rápida.
E.salto = async () => {
  console.log('\n== SALTO: altura H (px) y tiempo en el aire T (s) según el sostén de la tecla ==');
  for (const hz of [60, 120, 144]) for (const v of [6, 8.5, 13]) {
    const r = await conPagina(p => p.evaluate(([hz, v]) => {
      const R = Lab.init(3); Lab.start(60); const g = R.tRex.groundYPos; const dt = 1000 / hz;
      const salto = (hold, ff) => { const S = { trex: Lab.groundTrex(), obs: [], speed: v, acc: 0, max: 99 }; Lab.input(S, 'jd'); let f = 0, minY = g;
        while (f < 500) { if (hold !== null && f === hold) Lab.input(S, 'ju'); if (ff !== null && f === ff) Lab.input(S, 'dd'); Lab.step(S, dt); f++; minY = Math.min(minY, S.trex.yPos); if (!S.trex.jumping) break; }
        return [g - minY, f * dt / 1000]; };
      const tabla = []; for (let h = 0; h <= Math.round(0.2 * hz); h++) tabla.push([Math.round(h * dt), ...salto(h, null)]);
      const full = salto(null, null); const ff83 = salto(null, Math.round(83 / dt));
      let ffMax = 0; for (let k = 1; k < full[1] * 1000 / dt; k++) ffMax = Math.max(ffMax, salto(null, k)[1]);
      return { tabla, full, ff83, ffMax };
    }, [hz, v]));
    const bandas = []; for (const [ms, H, T] of r.tabla) { const b = bandas.at(-1); if (b && b[2] === H) b[1] = ms; else bandas.push([ms, ms, H, T]); }
    console.log(`${hz} Hz v${v}: completo H=${r.full[0]} T=${f2(r.full[1])} | soltar a: ` + bandas.map(([a, b, H, T]) => `${a}${a !== b ? '–' + b : ''} ms→H${H}/T${f2(T)}`).join('  ') + ` | caída rápida a 83 ms: H${r.ff83[0]} T${f2(r.ff83[1])}; vuelo más largo con caída rápida: ${f2(r.ffMax)} s`);
  }
};

// Ventana de presión por obstáculo y respuesta (60 Hz). Un obstáculo solo, entrando a 600 px.
E.ventanas = async () => {
  console.log('\n== VENTANAS: cuadros de presión que sobreviven, en s (60 Hz) ==');
  console.log('v     obstáculo             nada   completo                toque 100 ms            corto 67 ms             agacharse   desde que entra a pantalla');
  const r = await conPagina(p => p.evaluate(() => {
    const R = Lab.init(5); Lab.start(60); const T = Lab.groundTrex(); const dt = 1000 / 60;
    const acts = { full: q => [['jd', q]], tap: q => [['jd', q], ['ju', q + 6]], short: q => [['jd', q], ['ju', q + 4]], duck: q => [['dd', q]] };
    const casos = [];
    for (const v of [6, 8.5, 10, 13]) {
      for (const [ty, sz] of [['cactusSmall', 1], ['cactusSmall', 3], ['cactusLarge', 1], ['cactusLarge', 3]]) if (!(ty === 'cactusLarge' && sz > 1 && v < 7)) casos.push([v, ty, sz, null, 0]);
      if (v >= 8.5) for (const y of [100, 75, 50]) for (const off of [-0.8, 0.8]) casos.push([v, 'pterodactyl', 1, y, off]);
    }
    return casos.map(([v, ty, sz, y, off]) => {
      const o = Lab.mkObs(ty, sz, y, off, 600, v); const out = { v, ty, sz, y, off };
      out.none = Lab.simAct(T, [o], v, 0, dt, []).crash < 0;
      const arr = Lab.runPair({ trex: T, o1: o, o2: null, v, acc: 0, hz: 60 }, [], 'arr1', 400, true).arr;
      const okFull = []; for (let q = 0; q < 120; q++) if (Lab.simAct(T, [o], v, 0, dt, [['jd', q]]).crash < 0) okFull.push(q);
      out.lead = okFull.length ? (arr - okFull[0]) * dt / 1000 : null; out.llega = arr * dt / 1000;
      if (ty === 'pterodactyl' && y === 50) { // el timing del cactus chico a esta velocidad, llevado a este volador
        const c = Lab.mkObs('cactusSmall', 1, null, 0, 600, v); const ac = Lab.runPair({ trex: T, o1: c, o2: null, v, acc: 0, hz: 60 }, [], 'arr1', 400, true).arr;
        const habit = []; for (let q = 0; q < 120; q++) if (Lab.simAct(T, [c], v, 0, dt, [['jd', q]]).crash < 0) habit.push(q - ac);
        const mata = habit.filter(d => Lab.simAct(T, [o], v, 0, dt, [['jd', arr + d]]).crash >= 0).length;
        out.habit = `${mata} de ${habit.length}`;
      }
      for (const [k, fn] of Object.entries(acts)) {
        if (k === 'duck' && ty !== 'pterodactyl') continue;
        const ok = []; for (let q = 0; q < 120; q++) if (Lab.simAct(T, [o], v, 0, dt, fn(q)).crash < 0) ok.push(q);
        const runs = []; for (const q of ok) { if (runs.length && runs.at(-1)[1] === q - 1) runs.at(-1)[1] = q; else runs.push([q, q]); }
        out[k] = runs.map(([a, b]) => ((b - a + 1) * dt / 1000).toFixed(2) + (b === 119 ? '+' : ''));
      }
      return out;
    });
  }));
  for (const c of r) console.log(`${String(c.v).padEnd(6)}${(c.ty + '×' + c.sz + (c.y ? ' y' + c.y + (c.off > 0 ? ' +' : ' −') : '')).padEnd(22)}${(c.none ? 'pasa' : 'muere').padEnd(7)}${c.full.join(' / ').padEnd(24)}${c.tap.join(' / ').padEnd(24)}${c.short.join(' / ').padEnd(24)}${(c.duck ? (c.duck.length ? c.duck.join(' / ') : 'muere') : '').padEnd(12)}${'llega en ' + f2(c.llega) + ' s · '}${c.lead !== null ? 'abre ' + f2(c.lead) + ' s antes' : ''}${c.habit ? ' · con el timing del cactus chico mata en ' + c.habit + ' cuadros' : ''}`);
  console.log('(varias cifras = varias ventanas separadas; "+" = abierta hasta el borde del barrido)');
};

// Pares reales del generador: ¿alguno imposible? ¿cuántos en síncopa? ¿se leen a tiempo?
E.pares = async () => {
  const semillas = RAPIDO ? 3 : 24;
  console.log(`\n== PARES: ${semillas} partidas de 135 s del generador real (60 Hz, un bucle) ==`);
  const listas = [];
  for (let s = 1; s <= semillas; s++) listas.push(await conPagina(p => p.evaluate(seed => {
    const R = Lab.init(seed); Lab.start(60); Lab.restart(60); Lab.god(true); const seen = new Set(), list = []; let t = 0;
    while (t < 135000) { __vt.step(1000 / 60); t += 1000 / 60; for (const o of R.horizon.obstacles) if (!seen.has(o)) { seen.add(o); list.push({ t, v: R.currentSpeed, type: o.typeConfig.type, size: o.size, y: o.yPos, off: o.speedOffset || 0, x: o.xPos, gap: o.gap }); } }
    return list;
  }, s)));
  const pares = []; for (const l of listas) for (let i = 0; i + 1 < l.length; i++) pares.push([l[i], l[i + 1]]);
  const res = [];
  for (let k = 0; k < pares.length; k += 200) res.push(...await conPagina(p => p.evaluate(lote => {
    const R = Lab.init(99); Lab.start(60); const trex = Lab.groundTrex();
    const mk = r => { const o = Lab.mkObs(r.type, r.size, r.y, r.off, r.x, r.v); o.gap = r.gap; return o; };
    const A1 = { full: q => [['jd', q]], tap: q => [['jd', q], ['ju', q + 6]], short: q => [['jd', q], ['ju', q + 4]], ff8: q => [['jd', q], ['dd', q + 8], ['du', q + 11]], ff12: q => [['jd', q], ['dd', q + 12], ['du', q + 15]], ff16: q => [['jd', q], ['dd', q + 16], ['du', q + 19]], ff20: q => [['jd', q], ['dd', q + 20], ['du', q + 23]], duck: q => [['dd', q]], none: () => [] };
    const A2 = { full: q => [['jd', q]], tap: q => [['jd', q], ['ju', q + 6]], short: q => [['jd', q], ['ju', q + 4]], duck: q => [['dd', q]], none: () => [] };
    return lote.map(([r1, r2]) => {
      const P = { trex, o1: mk(r1), o2: mk(r2), v: r1.v, acc: 0.001, hz: 60 };
      const a1 = Lab.runPair(P, [], 'arr1', 400, true).arr, a2 = Lab.runPair(P, [], 'arr2', 600, true).arr;
      const rango = (a, n) => Array.from({ length: n }, (_, k) => a - n + 2 + k).filter(q => q >= 0);
      const ph1 = {}; for (const [a, fn] of Object.entries(A1)) { ph1[a] = []; for (const q of (a === 'none' ? [0] : rango(a1, 48))) { const x = Lab.runPair(P, fn(q), 'land1', 400); if (x.crash < 0) ph1[a].push([q, x.land]); } }
      const solo = []; for (const q of rango(a1, 48)) if (Lab.runPair({ ...P, o2: null }, A1.full(q), 'land1', 400).crash < 0) solo.push(q);
      let maxP2 = -1; for (const [a, fn] of Object.entries(A2)) for (const q of (a === 'none' ? [0] : rango(a2, 50))) if (Lab.runPair(P, fn(q), 'both', 600, true).crash < 0) maxP2 = Math.max(maxP2, a === 'none' ? 1e9 : q);
      const okAfter = land => maxP2 >= land;
      const jointFull = ph1.full.filter(([, l]) => okAfter(l)).map(([q]) => q);
      return { v: r1.v, t1: r1.type, y1: r1.y, B: a2 - a1, solo: solo.length, joint: jointFull.length, latestJoint: jointFull.length ? Math.max(...jointFull) - a1 : null,
        any: Object.values(ph1).some(l => l.some(([, x]) => okAfter(x))), noFF: ['full', 'tap', 'short', 'duck', 'none'].some(a => ph1[a].some(([, x]) => okAfter(x))),
        vis2: Math.round((r2.t - r1.t) / (1000 / 60)) + 2 - a1 };
    });
  }, pares.slice(k, k + 200))));
  const salta = x => x.t1 !== 'pterodactyl' || x.y1 === 100;
  console.log(`pares: ${res.length} · imposibles: ${res.filter(x => !x.any).length} · que exigen caída rápida: ${res.filter(x => x.any && !x.noFF).length}`);
  console.log('v           pares  síncopa        ventana perdida (mediana / máx)   B mín   B mediana');
  for (const [a, b] of [[6, 7], [7, 8.5], [8.5, 10], [10, 11.5], [11.5, 13.1]]) {
    const zs = res.filter(x => salta(x) && x.v >= a && x.v < b); const si = zs.filter(x => x.joint < x.solo);
    const per = si.map(x => 1 - x.joint / x.solo);
    console.log(`[${a},${b})`.padEnd(12) + String(zs.length).padEnd(7) + `${si.length} (${(100 * si.length / zs.length).toFixed(1)}%)`.padEnd(15) + (per.length ? `${(100 * med(per)).toFixed(0)}% / ${(100 * Math.max(...per)).toFixed(0)}%` : '—').padEnd(34) + `${f2(Math.min(...zs.map(x => x.B)) / 60)} s`.padEnd(8) + `${f2(med(zs.map(x => x.B)) / 60)} s`);
  }
  const si = res.filter(x => salta(x) && x.joint < x.solo);
  const legibles = si.filter(x => x.vis2 + 15 <= x.latestJoint);
  console.log(`síncopas legibles (el 2.º visible ≥ 250 ms antes de la última presión segura del 1.º): ${legibles.length} de ${si.length}`);
  console.log(`el 2.º aparece, mediana, ${f2(-med(si.map(x => x.vis2)) / 60)} s antes de que llegue el 1.º; la última presión segura del 1.º, mediana, ${f2(-med(si.map(x => x.latestJoint)) / 60)} s antes`);
  console.log(`margen por par entre ver el 2.º y la última presión segura del 1.º: mediana ${f2(med(si.map(x => x.latestJoint - x.vis2)) / 60)} s (reacción supuesta: 0.25 s)`);
  console.log(`(síncopa medida con salto completo sobre el 1.º; porcentajes sobre los ${res.filter(salta).length} pares cuyo 1.º se salta)`);
};

// Bot con reacción de 250 ms que apunta al centro de la ventana, con error de timing gaussiano.
E.bot = async () => {
  const n = RAPIDO ? 4 : 30;
  console.log(`\n== BOT: ${n} partidas por fila, tope 150 s, reacción 250 ms, salto completo ==`);
  console.log('Ventana efectiva = cuadros de presión que todavía sirven cuando el bot ya vio el obstáculo, reaccionó y está en el piso.');
  console.log('σ (ms)  Hz   bucle     llegan a 150 s   muertes ciegas   muerte mediana (s / v)   ventana efectiva v<8: mediana, p10, mín   v≥12.5: mediana, p10, mín');
  for (const [sigma, hz, modo] of [[0, 60, 'reinicio'], [0, 120, 'reinicio'], [20, 60, 'reinicio'], [40, 60, 'reinicio'], [70, 60, 'reinicio'], [70, 60, 'doble'], [100, 60, 'reinicio']]) {
    const rs = []; const planes = [];
    for (let g = 1; g <= n; g++) {
      const r = await conPagina(p => p.evaluate(([g, sigma, hz, modo]) => {
        const R = Lab.init(1000 + g); Lab.start(hz); if (modo === 'reinicio') { Lab.restart(hz); Lab.chains = 1; } else Lab.chains = 2;
        const x = Lab.botGame({ hz, R_ms: 250, sigma_ms: sigma, hold_ms: 200, maxT: 150000, botSeed: 77 + g });
        return { ...x, planes: Lab.plans };
      }, [g, sigma, hz, modo]));
      rs.push(r); planes.push(...r.planes);
    }
    const muertas = rs.filter(r => r.crashed);
    const ef = (a, b) => { const x = planes.filter(q => q.v >= a && q.v < b).map(q => q.ok / hz).sort((u, w) => u - w); return x.length ? `${f2(med(x))}, ${f2(x[Math.floor(x.length * 0.1)])}, ${f2(x[0])} s` : '—'; };
    console.log(`${String(sigma).padEnd(8)}${String(hz).padEnd(5)}${modo.padEnd(10)}${(rs.length - muertas.length + ' de ' + rs.length).padEnd(17)}${(muertas.filter(r => r.ciega).length + ' de ' + muertas.length).padEnd(17)}${(muertas.length ? f2(med(muertas.map(r => r.t))) + ' s / ' + f2(med(muertas.map(r => r.speed))) : '—').padEnd(25)}${ef(0, 8).padEnd(42)}${ef(12.5, 99)}`);
  }
};

// Estados: bloqueo de reinicio, foco, hitos y modo noche.
E.estados = async () => {
  console.log('\n== ESTADOS ==');
  const r = await conPagina(p => p.evaluate(() => {
    const R = Lab.init(22); const dt = 1000 / 60; Lab.start(60); const out = { lock: [] };
    for (const [key, wait] of [[32, 300], [32, 1150], [32, 1250], [13, 0]]) {
      R.gameOver(); const t0 = __vt.now; while (__vt.now - t0 < wait) __vt.advance(Math.min(dt, wait - (__vt.now - t0)));
      Lab.key('keydown', key); Lab.key('keyup', key); out.lock.push([key === 13 ? 'Enter' : 'espacio', wait, !R.crashed]);
      if (R.crashed) Lab.key('keyup', 13); for (let i = 0; i < 5; i++) __vt.step(dt);
    }
    Lab.god(true); for (let i = 0; i < 400; i++) __vt.step(dt);
    window.dispatchEvent(new Event('blur')); const pausa = !R.playing; const antes = R.horizon.obstacles.map(o => o.xPos);
    for (let i = 0; i < 60; i++) __vt.step(dt);
    window.dispatchEvent(new Event('focus')); out.foco = { pausa, sigue: R.playing, mismos: JSON.stringify(antes) === JSON.stringify(R.horizon.obstacles.map(o => o.xPos)), dist: Math.min(...antes) - R.tRex.xPos - 40 };
    return out;
  }));
  for (const [k, w, ok] of r.lock) console.log(`  reinicio con ${k} a los ${w} ms: ${ok ? 'sí' : 'no'}`);
  console.log(`  pierde el foco → pausa: ${r.foco.pausa}; vuelve el foco → sigue al instante: ${r.foco.sigue}, con los obstáculos donde estaban: ${r.foco.mismos} (el más cercano a ${r.foco.dist} px)`);
  for (const modo of ['reinicio', 'doble']) {
    const x = await conPagina(p => p.evaluate(modo => {
      const R = Lab.init(21); Lab.start(60); if (modo === 'reinicio') Lab.restart(60); Lab.god(true);
      const inv = [], ach = []; let t = 0, ul = false, ua = false;
      while (t < 200000) { __vt.step(1000 / 60); t += 1000 / 60; const n = document.documentElement.classList.contains('inverted'); if (n !== ul) { inv.push([+(t / 1000).toFixed(1), n]); ul = n; } const a = R.distanceMeter.achievement; if (a && !ua) ach.push(t / 1000); ua = a; }
      return { inv, ach };
    }, modo));
    const g = x.ach.slice(1).map((a, i) => a - x.ach[i]);
    console.log(`  ${modo}: modo noche ${x.inv.filter(v => v[1]).map(v => v[0]).join(', ')} s (dura ${f2(x.inv[1][0] - x.inv[0][0])} s); hito cada ${f2(g[0])} s al inicio y ${f2(g.at(-1))} s a tope`);
  }
};

// En un Chromium SIN TOCAR: chrome://dino, cuántos requestAnimationFrame por segundo pide el juego.
E.real = async () => {
  console.log('\n== REAL: chrome://dino en el navegador sin modificar ==');
  const page = await BROWSER.newPage();
  await page.addInitScript(() => { window.__raf = 0; const o = window.requestAnimationFrame.bind(window); window.requestAnimationFrame = cb => { window.__raf++; return o(cb); }; });
  try { await page.goto('chrome://dino/', { timeout: 10000 }); } catch { /* la página de error ES el juego */ }
  await page.waitForTimeout(1000);
  const tasa = async ms => { const a = await page.evaluate(() => window.__raf); await page.waitForTimeout(ms); return Math.round((await page.evaluate(() => window.__raf) - a) * 1000 / ms); };
  console.log(`  ${BROWSER.version()} · esperando: ${await tasa(2000)} rAF/s`);
  await page.keyboard.press('Space'); await page.waitForTimeout(1500);
  console.log(`  primera partida: ${await tasa(3000)} rAF/s`);
  await page.waitForTimeout(8000); await page.keyboard.press('Enter'); await page.waitForTimeout(1000);
  console.log(`  segunda partida (después del choque): ${await tasa(3000)} rAF/s`);
  await page.close();
};

// ---------- main ----------
PW = await preparar();
BROWSER = await PW.chromium.launch({ executablePath: CHROME });
console.log(`Banco del Dino · Chromium ${COMMIT} · navegador ${BROWSER.version()}${RAPIDO ? ' · RÁPIDO (no citar)' : ''}`);
try { for (const e of EXP) { if (!E[e]) { console.error('experimento desconocido:', e); continue; } await E[e](); } }
finally { await BROWSER.close(); }
