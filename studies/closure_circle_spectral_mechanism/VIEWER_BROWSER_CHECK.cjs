/* Presentation and browser checks only; no trajectories are simulated here. */
const fs = require('fs');
const path = require('path');
const assert = require('assert/strict');
const { execFileSync } = require('child_process');
const { gunzipSync } = require('zlib');
process.env.PLAYWRIGHT_BROWSERS_PATH ||= '/tmp/radial-viewer-browser/browsers';
const { chromium } = require(process.env.PLAYWRIGHT_MODULE || '/tmp/radial-viewer-browser/node_modules/playwright');
const source = process.argv[2] || '/home/amir/.codex/visualizations/2026/09/14/01a09f0d-694c-70f3-b27e-4c9b0e1d774a/circle-experiments.html';
const destination = '/home/amir/Codes/PDE/data/generated/closure_circle_spectral_mechanism/radial_viewer_001';
const logName = process.argv.includes('--edges') ? 'browser-check-edges.json' : process.argv.includes('--preview') ? 'browser-check-preview.json' : 'browser-check.json';
const renderer = '/home/amir/.codex/plugins/cache/openai-bundled/visualize/1.0.37/skills/visualize/scripts/render.py';
const rootSelector = '#circle-closure-explorer';
const result = { source, browser: null, scenarios: [], screenshots: [], layout: [], errors: [], consoleErrors: [], requestsFailed: [], warnings: [] };
const document = execFileSync('python3', [renderer, source], { encoding: 'utf8', maxBuffer: 10000000 });
const fragment = fs.readFileSync(source, 'utf8');
const encoded = fragment.match(/<script type="application\/octet-stream" data-role="payload">([\s\S]*?)<\/script>/)[1].trim();
const data = JSON.parse(gunzipSync(Buffer.from(encoded, 'base64')).toString());
const close = (a, b, tolerance = 1e-8) => Math.abs(a - b) <= tolerance * Math.max(1, Math.abs(a), Math.abs(b));
let browser;
(async () => {
  browser = await chromium.launch({ headless: true });
  result.browser = browser.version();
  const context = await browser.newContext({ viewport: { width: 768, height: 1500 }, colorScheme: 'light', offline: true, serviceWorkers: 'block' });
  // The approval review requires no outbound data access during inspection.
  // Offline mode plus catch-all interception keep all research payloads local.
  await context.route('**/*', route => route.request().url() === 'https://cdn.jsdelivr.net/npm/d3@7.9.0/dist/d3.min.js'
    ? route.fulfill({ status: 200, contentType: 'application/javascript', body: fs.readFileSync('/tmp/radial-viewer-browser/d3-7.9.0.min.js') })
    : route.fulfill({ status: 200, contentType: 'application/javascript', body: '' }));
  await context.routeWebSocket('**/*', socket => socket.close());
  const page = await context.newPage();
  page.on('pageerror', e => result.errors.push(String(e)));
  page.on('console', m => { if (m.type() === 'error') result.consoleErrors.push(m.text()); });
  page.on('requestfailed', r => result.requestsFailed.push({ url: r.url(), failure: r.failure() }));
  await page.setContent(document, { waitUntil: 'load', timeout: 60000 });
  const frame = page.frames().find(f => f !== page.mainFrame());
  assert(frame, 'Sandboxed preview iframe is present');
  await frame.waitForSelector(rootSelector + '[data-ready="true"]', { timeout: 30000 });
  const control = role => frame.locator(`[data-role="${role}"]`);
  const state = () => frame.evaluate(() => document.getElementById('circle-closure-explorer').__viewerCheck());
  const change = (role, value, event = 'change') => frame.evaluate(({role, value, event}) => {
    const el = document.querySelector(`#circle-closure-explorer [data-role="${role}"]`);
    el.value = String(value); el.dispatchEvent(new Event(event, { bubbles: true }));
  }, { role, value, event });
  const getOptions = async role => control(role).locator('option').evaluateAll(xs => xs.map(x => ({ value: x.value, label: x.textContent })));
  const cases = await getOptions('experiment');
  assert.equal(cases.length, 15, 'All 15 experiment choices exist');
  assert.equal(new Set(cases.map(c => c.value)).size, 15, 'Experiment IDs are unique');
  assert.equal(data.cases.length, cases.length);

  for (const width of [320, 736]) {
    await page.setViewportSize({ width: width + 32, height: 1600 });
    await page.waitForTimeout(100);
    const screenshot = path.join(destination, `browser-first-${width}.png`);
    await page.screenshot({ path: screenshot, fullPage: true });
    result.screenshots.push(screenshot);
    console.log(JSON.stringify({ firstRender: screenshot, layout: await frame.evaluate(() => ({ viewport: innerWidth, documentWidth: document.documentElement.scrollWidth })) }));
  }
  if (process.argv.includes('--preview')) return;

  async function allModels(enabled) {
    await control('legend').locator('button').evaluateAll((buttons, enabled) => {
      for (const b of buttons) if ((b.getAttribute('aria-pressed') === 'true') !== enabled) b.click();
    }, enabled);
  }
  async function verifyState(expectedMode, progress, expectedRadius) {
    const s = await state();
    assert.equal(s.mode, expectedMode);
    assert(s.states.length > 0);
    assert(s.radius > s.bound && s.bound > 0, `${s.caseId}: radius exceeds fixed curve bound`);
    if (expectedRadius !== undefined) assert.equal(s.radius, expectedRadius, 'Radius fixed while slider changes');
    const target = Math.exp(Math.log(s.lossHigh) + progress / 1000 * Math.log(s.lossLow / s.lossHigh));
    for (const model of s.states) {
      assert(model.curve.length > 30, `${model.key} has a sampled curve`);
      assert(model.curve.every(v => Number.isFinite(v) && s.radius + v > 0), `${s.caseId}/${model.key}: finite values and positive radial coordinates`);
      assert(Number.isFinite(model.loss) && model.loss >= 0, `${model.key}: valid loss`);
      if (expectedMode === 'time') assert(close(model.time, progress / 1000 * s.horizon), `${model.key}: physical time synchronized`);
      if (expectedMode === 'loss') assert(Math.abs(model.loss - target) <= Math.max(1e-10, target * 1e-7), `${s.caseId}/${model.key}: MSE ${model.loss} agrees with requested ${target}`);
    }
    const rendered = await frame.locator('[data-curve]').evaluateAll(xs => xs.map(x => ({ key: x.dataset.curve, d: x.getAttribute('d') })));
    assert.deepEqual(rendered.map(x => x.key), s.states.map(x => x.key));
    assert(rendered.every(x => x.d && !/NaN|Infinity/.test(x.d)), 'Displayed paths have valid coordinates');
    const status = await frame.locator('[data-state]').evaluateAll(xs => xs.map(x => ({ key: x.dataset.state, time: Number(x.dataset.time), loss: Number(x.dataset.loss) })));
    assert.deepEqual(status.map(x => x.key), s.states.map(x => x.key));
    status.forEach((x, i) => { assert(close(x.loss, s.states[i].loss)); assert(x.time === s.states[i].time || close(x.time, s.states[i].time)); });
    assert.equal(await control('error').isVisible(), false, 'No visible error');
    return s;
  }

  for (const experiment of process.argv.includes('--edges') ? [] : cases) {
    await change('experiment', experiment.value);
    await allModels(true);
    for (const mode of ['settled', 'time', 'loss']) {
      await change('alignment', mode);
      const reference = (await state()).radius;
      for (const value of mode === 'settled' ? [1000] : [0, 317, 1000]) {
        await change('progress', value, 'input');
        const s = await verifyState(mode, value, reference);
        result.scenarios.push({ case: experiment.value, mode, progress: value, models: s.states.map(m => m.key), radius: s.radius });
      }
    }
    for (const model of await control('legend').locator('button').evaluateAll(xs => xs.map(x => x.dataset.model))) {
      const button = frame.locator(`[data-model="${model}"]`);
      await button.click();
      assert.equal(await frame.locator(`[data-curve="${model}"]`).count(), 0, `${model} curve hidden by legend`);
      assert.equal(await frame.locator(`[data-state="${model}"]`).count(), 0, `${model} status hidden by legend`);
      await button.click();
      assert.equal(await frame.locator(`[data-curve="${model}"]`).count(), 1, `${model} curve restored`);
    }
    if (await control('network-controls').isVisible()) {
      for (const width of ['1024', '4096']) for (const seed of ['mean', '1729', '2718', '3141']) {
        await change('width', width); await change('seed', seed);
        await change('alignment', 'loss'); await change('progress', 500, 'input');
        const s = await verifyState('loss', 500);
        assert(s.states.some(m => m.key === 'network'), 'Network remains available');
        result.scenarios.push({ case: experiment.value, mode: 'loss', progress: 500, width, seed });
      }
    }
  }

  await change('experiment', 'pair_d15_r45'); await change('width', '4096'); await change('seed', 'mean');
  await change('alignment', 'time'); await change('progress', 100, 'input');
  await control('play').click();
  await page.waitForTimeout(300);
  assert(Number(await control('progress').inputValue()) > 100, 'Playback advances slider');
  assert.equal(await control('play').textContent(), 'Pause');
  await control('play').click();
  const paused = await control('progress').inputValue();
  await page.waitForTimeout(160);
  assert.equal(await control('progress').inputValue(), paused, 'Pause stops advancement');
  await change('progress', 998, 'input'); await control('play').click(); await page.waitForTimeout(250);
  assert.equal(await control('progress').inputValue(), '1000', 'Playback stops at end');
  assert.equal(await control('play').textContent(), 'Play');
  await change('alignment', 'settled');
  assert(await control('play').isDisabled());
  assert.equal(await control('slider-wrap').isVisible(), false);
  result.scenarios.push({ playback: 'advance, pause, stop at end, settled disabled' });

  for (const soleModel of ['network', 'N2']) {
    await change('experiment', 'pair_d15_r45');
    const onlyButton = frame.locator(`[data-model="${soleModel}"]`);
    if (await onlyButton.getAttribute('aria-pressed') !== 'true') await onlyButton.click();
    await control('legend').locator('button').evaluateAll((buttons, soleModel) => {
      for (const b of buttons) if (b.dataset.model !== soleModel && b.getAttribute('aria-pressed') === 'true') b.click();
    }, soleModel);
    assert.deepEqual((await state()).states.map(s => s.key), [soleModel]);
    const nextCase = data.cases.find(c => !c.models.some(m => soleModel === 'network' ? m.kind.startsWith('network') : m.kind === 'closure' && m.order === 2));
    assert(nextCase, `A case without ${soleModel} is available`);
    await change('experiment', nextCase.id);
    assert((await state()).states.length > 0, 'Switching away from sole visible model recovers a visible model');
    await verifyState('settled', 1000);
    result.scenarios.push({ soleModel, caseSwitch: nextCase.id });
  }
  await change('experiment', 'pair_d15_r45');
  await allModels(true);

  for (const colorScheme of ['light', 'dark']) {
    await page.emulateMedia({ colorScheme });
    for (const width of [736, 320]) {
      await page.setViewportSize({ width: width + 32, height: 1800 });
      for (const view of ['radial', 'angle']) {
        await change('view', view);
        await page.waitForTimeout(120);
        const layout = await frame.evaluate(() => {
          const root = document.getElementById('circle-closure-explorer'), box = root.getBoundingClientRect(), svg = root.querySelector('svg'), sb = svg.getBoundingClientRect();
          const textBounds = [...svg.querySelectorAll('text')].map(t => { const b=t.getBoundingClientRect(); return { text:t.textContent, left:b.left-sb.left, right:b.right-sb.left, top:b.top-sb.top, bottom:b.bottom-sb.top, fontSize:parseFloat(getComputedStyle(t).fontSize) }; });
          return { rootWidth:box.width, viewportWidth:innerWidth, documentWidth:document.documentElement.scrollWidth, height:root.scrollHeight, svgWidth:sb.width, svgHeight:sb.height, textBounds, outside:textBounds.filter(t => t.left < -1 || t.top < -1 || t.right > sb.width+1 || t.bottom > sb.height+1), small:textBounds.filter(t=>t.fontSize < 11), colors:{ foreground:getComputedStyle(root).getPropertyValue('--foreground').trim(), background:getComputedStyle(root).getPropertyValue('--background').trim() } };
        });
        result.layout.push({ colorScheme, width, view, ...layout });
        if (layout.documentWidth > layout.viewportWidth + 1) result.warnings.push(`${colorScheme}/${width}/${view}: horizontal overflow ${layout.documentWidth} > ${layout.viewportWidth}`);
        if (layout.outside.length) result.warnings.push(`${colorScheme}/${width}/${view}: labels outside SVG: ${layout.outside.map(x=>x.text).join(', ')}`);
        if (layout.small.length) result.warnings.push(`${colorScheme}/${width}/${view}: labels smaller than 11px`);
        await page.locator('iframe').evaluate((iframe, height) => iframe.style.height = `${height + 12}px`, layout.height);
        const screenshot = path.join(destination, `browser-${colorScheme}-${width}-${view}.png`);
        await page.screenshot({ path: screenshot, fullPage: true });
        result.screenshots.push(screenshot);
        const plot = frame.locator('[data-chart-hit]');
        await plot.hover({ position: { x: Math.min(120, width/2), y: 120 } });
        assert(await control('tooltip').isVisible(), 'Cross-series tooltip appears');
        assert.equal(await frame.locator('[data-chart-hover-marker]').count(), (await state()).states.length, 'Hover marker for every visible model');
        await plot.click({ position: { x: Math.min(120, width/2), y: 120 } });
        await page.mouse.move(0, 0);
        assert(await control('tooltip').isVisible(), 'Tap/click pins tooltip');
        await plot.click({ position: { x: Math.min(120, width/2), y: 120 } });
        assert.equal(await control('tooltip').isVisible(), false, 'Second tap dismisses tooltip');
      }
    }
  }
  assert.equal(result.errors.length, 0, 'No uncaught JavaScript errors');
  assert.equal(result.consoleErrors.length, 0, 'No console errors');
  result.passed = result.warnings.length === 0;
})().catch(error => { result.passed = false; result.failure = error.stack; console.error(error.stack); process.exitCode = 1; }).finally(async () => {
  if (browser) await browser.close();
  fs.mkdirSync(destination, { recursive: true });
  fs.writeFileSync(path.join(destination, logName), JSON.stringify(result, null, 2) + '\n');
  console.log(JSON.stringify({ passed: result.passed, scenarios: result.scenarios.length, warnings: result.warnings, errors: result.errors, consoleErrors: result.consoleErrors, requestsFailed: result.requestsFailed, log: path.join(destination, logName) }, null, 2));
});
