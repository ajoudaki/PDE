// Archived from matched_network_preview01/browser_check.cjs. Browser assertions
// are unchanged. Dependency paths are configurable and output must be fresh.
const fs = require('fs');
const path = require('path');
const assert = require('assert');
const cache = process.env.MATCHED_NETWORK_BROWSER_CACHE || '/tmp/radial-viewer-browser';
const { chromium } = require(process.env.MATCHED_NETWORK_PLAYWRIGHT || path.join(cache, 'node_modules/playwright'));
const chromiumPath = process.env.MATCHED_NETWORK_CHROMIUM || path.join(cache, 'browsers/chromium_headless_shell-1161/chrome-linux/headless_shell');
const d3Path = process.env.MATCHED_NETWORK_D3 || path.join(cache, 'd3-7.9.0.min.js');

(async () => {
  const [preview, radialData, output, ...extra] = process.argv.slice(2);
  if (!preview || !radialData || !output || extra.length)
    throw new Error('Usage: node matched_network_browser_check.cjs PREVIEW_HTML VIEWER_DATA_JSON FRESH_OUTPUT_DIRECTORY');
  if (fs.existsSync(output)) throw new Error('Refusing to replace existing browser output: ' + output);
  const data = JSON.parse(fs.readFileSync(radialData, 'utf8'));
  fs.mkdirSync(output, {recursive: true});
  const browser = await chromium.launch({
    executablePath: chromiumPath,
    headless: true, args: ['--no-sandbox']
  });
  const context = await browser.newContext({ viewport: { width: 768, height: 1400 } });
  await context.route('https://cdn.jsdelivr.net/npm/d3@7.9.0/dist/d3.min.js', route =>
    route.fulfill({ path: d3Path, contentType: 'application/javascript' }));
  const page = await context.newPage();
  const errors = [];
  page.on('pageerror', error => errors.push(error.message));
  await page.goto('file://' + path.resolve(preview));
  const rootSelector = '#matched-network-explorer';
  await page.frameLocator('iframe').locator(rootSelector + '[data-ready="true"]').waitFor({timeout: 20000});
  const frame = page.frames().find(f => f !== page.mainFrame());
  const snapshots = [];
  const getState = () => frame.evaluate(() => document.getElementById('matched-network-explorer').__viewerCheck());
  for (const caseData of data.cases) {
    await frame.locator('[data-role="experiment"]').selectOption(caseData.id);
    let scale;
    for (const order of caseData.orders) {
      await frame.locator('[data-role="order"]').selectOption(String(order.p));
      await page.waitForTimeout(300);
      const state = await getState();
      assert.equal(state.caseId, caseData.id);
      assert.equal(state.p, order.p);
      assert.equal(state.columns, order.columns);
      assert.equal(state.states.length, 4);
      if (scale) assert.deepStrictEqual([state.radius, state.bound], scale);
      scale = [state.radius, state.bound];
      for (const model of state.states) {
        const expected = model.key === 'full' ? caseData.reference : order.models[model.key];
        for (const field of ['width', 'trainable', 'total', 'level', 'rms', 'mse', 'time', 'valid'])
          assert.equal(model[field], expected[field], caseData.id + ' p' + order.p + ' ' + model.key + ' ' + field);
        assert.deepStrictEqual(model.curve, expected.curve);
      }
      const hasUnresolved = state.states.some(s => !s.valid);
      assert.equal(await frame.locator('[data-role="qualification"]').isVisible(), hasUnresolved);
      assert.equal(await frame.locator('[data-curve]').count(), 4);
      await page.screenshot({path: path.join(output, caseData.id + '_p' + order.p + '_736.png'), fullPage: true});
      snapshots.push({case: state.caseId, p: state.p, radius: state.radius, bound: state.bound,
        widths: state.states.map(s => s.width), unresolved: state.states.filter(s => !s.valid).map(s => s.key)});
    }
  }
  const hit = frame.locator('[data-chart-hit]');
  const hitBox = await hit.boundingBox();
  await page.mouse.move(hitBox.x + hitBox.width * .78, hitBox.y + hitBox.height * .33);
  assert.equal(await frame.locator('[data-chart-hover-marker]').count(), 4);
  assert.equal(await frame.locator('[data-role="tooltip"] [data-method]').count(), 4);
  await frame.locator('button[data-method="small_total"]').click();
  assert.equal(await frame.locator('[data-curve]').count(), 3);
  assert.equal((await getState()).visible.small_total, false);
  await page.mouse.move(hitBox.x + hitBox.width * .6, hitBox.y + hitBox.height * .2);
  assert.equal(await frame.locator('[data-chart-hover-marker]').count(), 3);
  assert.equal(await frame.locator('[data-role="tooltip"] [data-method]').count(), 3);
  await hit.click({position: {x: hitBox.width * .65, y: hitBox.height * .4}});
  await page.mouse.move(0, 0);
  assert.equal(await frame.locator('[data-role="tooltip"]').isVisible(), true);
  await hit.click({position: {x: hitBox.width * .65, y: hitBox.height * .4}});
  assert.equal(await frame.locator('[data-role="tooltip"]').isVisible(), false);
  await frame.locator('button[data-method="small_total"]').click();
  const layouts = [];
  for (const colorScheme of ['light', 'dark']) {
    await page.emulateMedia({colorScheme});
    for (const width of [736, 360, 320]) {
      await page.setViewportSize({width: width + 32, height: 1500});
      await page.waitForTimeout(150);
      const layout = await frame.evaluate(() => {
        const root = document.getElementById('matched-network-explorer');
        const box = root.getBoundingClientRect();
        const svg = root.querySelector('svg');
        const outliers = [...root.querySelectorAll('select,button,.sc-chart text')].filter(el => {
          const r = el.getBoundingClientRect();
          return r.left < box.left - 1 || r.right > box.right + 1;
        }).map(el => el.textContent);
        const frameRect = svg.querySelector('[data-chart-frame]').getBBox();
        const outsidePaths = [...svg.querySelectorAll('[data-curve]')].filter(el => {
          const r = el.getBBox();
          return r.x < frameRect.x || r.y < frameRect.y || r.x + r.width > frameRect.x + frameRect.width || r.y + r.height > frameRect.y + frameRect.height;
        }).length;
        return {width: box.width, viewport: svg.viewBox.baseVal.width,
          scrollWidth: document.documentElement.scrollWidth, clientWidth: document.documentElement.clientWidth,
          outliers, outsidePaths};
      });
      assert.equal(layout.width, layout.viewport);
      assert(layout.scrollWidth <= layout.clientWidth, JSON.stringify(layout));
      assert.deepStrictEqual(layout.outliers, [], JSON.stringify(layout));
      assert.equal(layout.outsidePaths, 0);
      layouts.push({colorScheme, ...layout});
      await page.screenshot({path: path.join(output, colorScheme + '_' + width + '.png'), fullPage: true});
    }
  }
  assert.deepStrictEqual(errors, []);
  const result = {passed: true, snapshots, layouts, checks: ['all case/order data', 'fixed per-case scale across p',
    'exact saved widths/counts/RMS/curves', 'unresolved flags', 'four curve overlay', 'cross-series hover',
    'legend curve and tooltip toggles', 'click pin/unpin', 'light and dark layouts', 'no horizontal overflow',
    'measured SVG width', 'paths stay within chart', 'no JavaScript errors'], errors};
  fs.writeFileSync(path.join(output, 'browser_checks.json'), JSON.stringify(result, null, 2) + '\n');
  await browser.close();
  console.log(JSON.stringify({passed: true, snapshots: snapshots.length, layouts: layouts.length}));
})().catch(error => { console.error(error); process.exit(1); });
