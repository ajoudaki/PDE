#!/usr/bin/env node
'use strict';
/* Local, read-only browser verification of this study's standalone viewer.
 * Usage: node comparison_browser_check.cjs --html /absolute/viewer.html
 *          --out /absolute/fresh/generated/check-directory
 * The existing browser installation is reused; nothing is downloaded.
 */
const fs = require('fs');
const path = require('path');
const crypto = require('crypto');
const {pathToFileURL} = require('url');

const generated = path.resolve(__dirname, '../../data/generated/gradient_flow_probe_dictionary_20260921');
const playwrightPath = '/tmp/radial-viewer-browser/node_modules/playwright';
const browserPath = '/tmp/radial-viewer-browser/browsers/chromium_headless_shell-1161/chrome-linux/headless_shell';
const cases = ['quadrant_pairs', 'two_outliers_alternating'];
const sha256 = filename => crypto.createHash('sha256').update(fs.readFileSync(filename)).digest('hex');
const under = (filename, root) => filename.startsWith(root + path.sep);

async function checkViewer(htmlPath, out) {
  const {chromium} = require(playwrightPath);
  fs.mkdirSync(out, {recursive: false});
  const htmlHash = sha256(htmlPath);
  const browser = await chromium.launch({headless: true, executablePath: browserPath, args: ['--no-sandbox']});
  const page = await browser.newPage({viewport: {width: 1280, height: 900}});
  const errors = [], externalRequests = [], records = [], screenshots = [];
  page.on('pageerror', error => errors.push(String(error)));
  page.on('request', request => {if (/^https?:/.test(request.url())) externalRequests.push(request.url());});
  await page.addInitScript(() => {
    window.__geometryErrors = [];
    window.__lines = 0;
    window.__arcs = [];
    for (const name of ['moveTo', 'lineTo', 'arc', 'setTransform', 'fillRect', 'clearRect']) {
      const original = CanvasRenderingContext2D.prototype[name];
      CanvasRenderingContext2D.prototype[name] = function(...args) {
        if (args.some(value => typeof value === 'number' && !Number.isFinite(value))) window.__geometryErrors.push(name + ': nonfinite');
        if (name === 'arc') {
          if (args[2] < 0) window.__geometryErrors.push('negative radius');
          window.__arcs.push(args[2]);
        }
        if (name === 'lineTo') window.__lines++;
        return original.apply(this, args);
      };
    }
  });
  try {
    await page.goto(pathToFileURL(htmlPath).href);
    if (await page.locator('#level').inputValue() !== 'refined') throw Error('Finer accuracy is not the default run');
    const before = await page.evaluate(() => JSON.stringify(data));
    const sharedScale = new Map();
    for (const width of [360, 1280]) {
      await page.setViewportSize({width, height: 900});
      for (const c of cases) for (const p of ['1', '2', '3']) for (const level of ['primary', 'refined']) for (const density of ['1024', '2048']) for (const amplitude of ['50', '150']) {
        const state = {c, p, level, density, amplitude};
        const result = await page.evaluate(state => {
          for (const [id, value] of Object.entries({case: state.c, degree: state.p, level: state.level, density: state.density, amplitude: state.amplitude})) document.getElementById(id).value = value;
          window.__lines = 0;
          window.__arcs = [];
          document.getElementById('case').dispatchEvent(new Event('change'));
          const s = selected();
          const expectedLines = 4 + s.curves.reduce((count, item) => count + Math.min(s.density, item.raw.endpoint_angles.length) - 1, 0);
          let expectedBound = 1;
          for (const [key, levels] of Object.entries(data.curves)) if (key.startsWith(state.c + '_')) for (const raw of Object.values(levels)) for (const value of raw.endpoint_prediction) expectedBound = Math.max(expectedBound, Math.abs(value));
          return {lines: window.__lines, expectedLines, rings: window.__arcs.slice(0, 3), geometryErrors: window.__geometryErrors.slice(), bodyWidth: document.body.scrollWidth, viewWidth: innerWidth, rows: document.querySelectorAll('#summary tr').length, caseBound: caseMagnitude[state.c], expectedBound};
        }, state);
        if (result.geometryErrors.length) throw Error(JSON.stringify(result.geometryErrors));
        if (result.lines !== result.expectedLines) throw Error('Wrong number of raw sample segments');
        if (result.rows !== 3) throw Error('Missing comparison rows');
        if (result.bodyWidth > result.viewWidth + 1) throw Error('Page overflows horizontally');
        if (result.caseBound !== result.expectedBound) throw Error('Case bound omits a saved order or run');
        const key = [width, c, amplitude].join(':');
        if (sharedScale.has(key) && JSON.stringify(sharedScale.get(key)) !== JSON.stringify(result.rings)) throw Error('Radial scale changed across order, run, or display density');
        sharedScale.set(key, result.rings);
        records.push({...state, width, lines: result.lines, rings: result.rings, caseBound: result.caseBound});
      }
    }
    for (const width of [1280, 360]) {
      await page.setViewportSize({width, height: 900});
      for (const c of cases) for (const p of ['1', '2', '3']) {
        await page.evaluate(({c, p}) => {
          for (const [id, value] of Object.entries({case: c, degree: p, level: 'refined', density: '2048', amplitude: '100'})) document.getElementById(id).value = value;
          document.getElementById('case').dispatchEvent(new Event('change'));
        }, {c, p});
        const filename = `${c}_p${p}_${width}.png`;
        await page.screenshot({path: path.join(out, filename), fullPage: true});
        screenshots.push(filename);
      }
    }
    const downloadPromise = page.waitForEvent('download');
    await page.locator('#save').click();
    const download = await downloadPromise;
    await download.saveAs(path.join(out, 'downloaded_radial.png'));
    if (await page.evaluate(() => JSON.stringify(data)) !== before) throw Error('Viewer controls changed saved input data');
    if (errors.length || externalRequests.length) throw Error(JSON.stringify({errors, externalRequests}));
    if (sha256(htmlPath) !== htmlHash) throw Error('Input HTML changed during verification');
    const svgFiles = fs.readdirSync(path.dirname(htmlPath)).filter(name => name.endsWith('.svg'));
    for (const name of svgFiles) {
      const svg = fs.readFileSync(path.join(path.dirname(htmlPath), name), 'utf8');
      for (const match of svg.matchAll(/\b(?:d|points|cx|cy|r|x|y|width|height|transform)="([^"]*)"/g)) if (/(?:NaN|[+-]?Infinity)/i.test(match[1])) throw Error('Nonfinite SVG geometry: ' + name);
    }
    const report = {
      status: 'PASS', checked_utc: new Date().toISOString(),
      source: {path: htmlPath, sha256: htmlHash},
      checker: {path: __filename, sha256: sha256(__filename)},
      browser: browserPath, browser_version: browser.version(),
      checks: ['all case/order/run selections', '1024/2048 raw sample counts', '50/150 percent display amplitude', 'shared case bound across every order/run', 'finite canvas and SVG geometry', '360/1280 pixel layout', 'finer-accuracy default', 'PNG download', 'saved data unchanged', 'no external requests'],
      states: records, screenshots, svg_files: svgFiles, browser_errors: errors, external_requests: externalRequests,
    };
    fs.writeFileSync(path.join(out, 'browser_check.json'), JSON.stringify(report, null, 2) + '\n');
    console.log(JSON.stringify({status: 'PASS', states: records.length, evidence: out, html_sha256: htmlHash}));
    return report;
  } finally {
    await browser.close();
  }
}

if (require.main === module) {
  const args = {};
  for (let i = 2; i < process.argv.length; i += 2) args[process.argv[i]] = process.argv[i + 1];
  if (!args['--html'] || !args['--out']) throw Error('Required: --html <current-study HTML> --out <fresh current-study evidence folder>');
  const htmlPath = fs.realpathSync(args['--html']);
  const out = path.resolve(args['--out']);
  if (!under(htmlPath, generated) || !under(out, generated) || fs.existsSync(out)) throw Error('Inputs and fresh output must be within this study generated directory');
  const outParent = fs.realpathSync(path.dirname(out));
  if (outParent !== generated && !under(outParent, generated)) throw Error('Evidence parent resolves outside this study');
  checkViewer(htmlPath, out).catch(error => {console.error(error); process.exitCode = 1;});
}

module.exports = {checkViewer};
