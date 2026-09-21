// Functional and layout checks for the saved radial visualization; no training.
const fs = require('fs');
const path = require('path');
const assert = require('assert');
const crypto = require('crypto');
const { chromium } = require('/tmp/radial-viewer-browser/node_modules/playwright-core');
const [previewPath, payloadPath, outputDirectory] = process.argv.slice(2);
if (!previewPath || !payloadPath || !outputDirectory) throw new Error('Expected preview, payload and output directory');
const payload = JSON.parse(fs.readFileSync(payloadPath, 'utf8'));
const expected = new Map(payload.records.map(record => [record.id, record]));
const keys = ['closure1024', 'width55', 'width105'];
const errors = [], inspected = [];
const digest = file => crypto.createHash('sha256').update(fs.readFileSync(file)).digest('hex');
const unique = values => [...new Set(values)];

async function main() {
  fs.mkdirSync(outputDirectory, { recursive: true });
  const browser = await chromium.launch({
    executablePath: '/tmp/radial-viewer-browser/browsers/chromium_headless_shell-1161/chrome-linux/headless_shell',
    headless: true, args: ['--no-sandbox', '--disable-dev-shm-usage'],
  });
  try {
    const context = await browser.newContext({ viewport: { width: 768, height: 1150 }, reducedMotion: 'reduce' });
    await context.route('https://cdn.jsdelivr.net/npm/d3@7.9.0/dist/d3.min.js', route => route.fulfill({
      status: 200, contentType: 'application/javascript',
      body: fs.readFileSync('/tmp/radial-viewer-browser/d3-7.9.0.min.js'),
    }));
    const page = await context.newPage();
    page.on('pageerror', error => errors.push(error.message));
    await page.goto('file://' + path.resolve(previewPath));
    await page.frameLocator('iframe').locator('#alternating-radial-rounds[data-ready="true"]').waitFor({ timeout: 30000 });
    const frame = page.frames().find(f => f !== page.mainFrame());
    assert(frame, 'Preview iframe missing');
    const state = () => frame.evaluate(() => document.getElementById('alternating-radial-rounds').__viewerCheck());
    const getOptions = role => frame.locator('[data-role="' + role + '"] option').evaluateAll(nodes => nodes.map(n => n.value));
    async function layout(label) {
      const result = await frame.evaluate(() => {
        const root = document.getElementById('alternating-radial-rounds');
        const bounds = root.getBoundingClientRect();
        const chart = root.querySelector('.ar-chart').getBoundingClientRect();
        const outside = [...root.querySelectorAll('.ar-chart text')].map(node => ({ text: node.textContent, box: node.getBoundingClientRect().toJSON() }))
          .filter(item => item.box.left < chart.left - 1 || item.box.right > chart.right + 1 || item.box.top < chart.top - 1 || item.box.bottom > chart.bottom + 1);
        const oversize = [...root.querySelectorAll('select,button')].filter(node => {
          const b = node.getBoundingClientRect();
          return b.width && (b.left < bounds.left - 1 || b.right > bounds.right + 1);
        }).map(node => node.getAttribute('aria-label'));
        const rings = [...root.querySelectorAll('g[data-grid] circle')].map(node => ({
          r: node.getAttribute('r'), stroke: getComputedStyle(node).stroke,
          strokeWidth: getComputedStyle(node).strokeWidth, fill: getComputedStyle(node).fill,
        }));
        return { rootWidth: bounds.width, scrollWidth: root.scrollWidth, outside, oversize, rings };
      });
      assert(result.scrollWidth <= result.rootWidth + 1, label + ': horizontal overflow');
      assert.equal(result.outside.length, 0, label + ': SVG labels outside frame ' + JSON.stringify(result.outside));
      assert.equal(result.oversize.length, 0, label + ': control overflow');
      assert.equal(result.rings.length, 3, label + ': missing output guide rings');
      assert(result.rings.every(r => Number(r.r) > 0 && r.stroke !== 'none' && parseFloat(r.strokeWidth) > 0), label + ': invisible output guide rings ' + JSON.stringify(result.rings));
      return result;
    }
    const initial = await state();
    assert.equal(initial.round, 'gd'); assert.equal(initial.m, 126);
    assert.equal(initial.gain, 'high'); assert.equal(initial.seed, 20260921);
    assert.equal(initial.radialSpread, .35);
    assert.equal(initial.selected.length, 3);
    const originalMetrics = initial.selected.map(r => [r.id, r.mse, r.rmse, r.signErrors, r.samples]);
    const ringRadii = () => frame.locator('g[data-grid] circle').evaluateAll(nodes => nodes.map(n => Number(n.getAttribute('r'))));
    const originalRings = await ringRadii();
    await frame.locator('[data-role="spread"]').press('End');
    const wideRings = await ringRadii();
    assert(Math.abs((originalRings[2] - originalRings[0]) / (wideRings[2] - wideRings[0]) - .35) < 1e-12);
    await frame.locator('[data-role="spread"]').press('Home');
    const narrowRings = await ringRadii();
    assert(Math.abs((narrowRings[2] - narrowRings[0]) / (wideRings[2] - wideRings[0]) - .1) < 1e-12);
    assert.deepEqual((await state()).selected.map(r => [r.id, r.mse, r.rmse, r.signErrors, r.samples]), originalMetrics);
    for (let i = 0; i < 5; i++) await frame.locator('[data-role="spread"]').press('ArrowRight');
    const coverage = new Set(), combinations = [];
    for (const round of await getOptions('round')) {
      await frame.locator('[data-role="round"]').selectOption(round);
      for (const samples of await getOptions('samples')) {
        await frame.locator('[data-role="samples"]').selectOption(samples);
        for (const gain of await getOptions('gain')) {
          await frame.locator('[data-role="gain"]').selectOption(gain);
          for (const eta of await getOptions('eta')) {
            if (await frame.locator('[data-role="eta"]').isVisible()) await frame.locator('[data-role="eta"]').selectOption(eta);
            for (const seed of await getOptions('seed')) {
              await frame.locator('[data-role="seed"]').selectOption(seed);
              const current = await state();
              const records = payload.records.filter(r => r.round === round && r.m === Number(samples) && r.gain === gain &&
                r.seed === Number(seed) && r.etaMax === (round === 'adam' ? null : Number(eta)));
              assert.equal(current.selected.length, records.length, 'Missing or fabricated records');
              for (const record of current.selected) {
                const source = expected.get(record.id); assert(source);
                assert.equal(record.rmse, source.rmse); assert.equal(record.signErrors, source.signErrors);
                assert.equal(record.circleAvailable, source.circleAvailable);
                const buffer = Buffer.from(source.samples64, 'base64');
                const samples64 = Array.from({ length: source.m }, (_, i) => buffer.readDoubleLE(i * 8));
                assert.deepEqual(record.samples, samples64, 'Training predictions altered');
                assert.equal(await frame.locator('[data-sample-method="' + record.model + '"]').count(), source.m);
                assert.equal(await frame.locator('[data-curve="' + record.model + '"]').count(), source.circleAvailable ? 1 : 0);
                if (source.circleAvailable) {
                  assert.equal(record.curve.length, source.circleCount);
                  const v = Buffer.from(source.circle32, 'base64'), k = Buffer.from(source.indices16, 'base64');
                  record.curve.forEach((p, i) => {
                    assert.equal(p.y, v.readFloatLE(i * 4)); assert.equal(p.x, 360 * k.readUInt16LE(i * 2) / payload.circleGrid);
                    assert(Math.abs(p.y) < current.bound, 'Curve clipped by radial domain');
                  });
                }
                coverage.add(record.id);
              }
              for (const model of keys) {
                assert.equal(await frame.locator('[data-method="' + model + '"]').isDisabled(), !records.some(r => r.model === model));
              }
              assert.equal(await frame.locator('[data-target]').count(), Number(samples));
              assert.equal(await frame.locator('[data-role="precision"]').isVisible(), records.some(r => !r.circleAvailable));
              combinations.push({ round, m: Number(samples), gain, eta, seed: Number(seed), records: records.length });
            }
          }
        }
      }
    }
    assert.equal(coverage.size, payload.records.length);
    for (const round of ['gd', 'adam']) {
      await frame.locator('[data-role="round"]').selectOption(round);
      await frame.locator('[data-role="seed"]').selectOption('20260921');
      inspected.push({ label: round + '-desktop', ...await layout(round + '-desktop') });
      await page.screenshot({ path: path.join(outputDirectory, round + '-desktop.png'), fullPage: true });
    }
    await frame.locator('[data-role="round"]').selectOption('gd');
    await frame.locator('[data-method="width55"]').click();
    assert.equal(await frame.locator('[data-curve="width55"]').count(), 0);
    assert.equal(await frame.locator('[data-sample-method="width55"]').count(), 0);
    const box = await frame.locator('.ar-chart').boundingBox();
    await page.mouse.move(box.x + box.width * .73, box.y + box.height * .33);
    await frame.locator('[data-role="tooltip"]').waitFor({ state: 'visible' });
    assert.equal(await frame.locator('[data-chart-hover-marker]').count(), 2);
    assert.equal(await frame.locator('[data-role="tooltip"] [data-method="width55"]').count(), 0);
    await frame.locator('[data-method="width55"]').click();
    await frame.evaluate(() => {
      window.dispatchEvent(new CustomEvent('openai:set_globals', { detail: { globals: { widgetState: {
        modelContent: { round: 'adam', samples: 62, initialization: 'canonical', seed: 20260921, maximumGdStep: null },
        privateContent: { visible: { closure1024: false, width55: true, width105: false } },
      } } } }));
    });
    const restored = await state();
    assert.equal(restored.round, 'adam'); assert.equal(restored.m, 62);
    assert.equal(restored.selected[0].circleAvailable, false);
    assert.equal(await frame.locator('[data-curve]').count(), 0);
    assert.equal(await frame.locator('[data-sample-method="width55"]').count(), 62);
    await page.screenshot({ path: path.join(outputDirectory, 'precision-samples-only.png'), fullPage: true });
    for (const width of [392, 352]) {
      await page.setViewportSize({ width, height: 1200 });
      await frame.locator('[data-role="round"]').selectOption('gd');
      for (const model of keys) {
        const button = frame.locator('button[data-method="' + model + '"]');
        if (await button.getAttribute('aria-pressed') === 'false') await button.click();
      }
      inspected.push({ label: 'viewport-' + width, ...await layout('viewport-' + width) });
      await page.screenshot({ path: path.join(outputDirectory, 'mobile-' + width + '.png'), fullPage: true });
    }
    await page.setViewportSize({ width: 768, height: 1150 });
    await page.emulateMedia({ colorScheme: 'dark', reducedMotion: 'no-preference' });
    await frame.locator('[data-role="round"]').selectOption('adam');
    await page.waitForTimeout(250);
    await frame.locator('[data-role="round"]').selectOption('gd');
    await page.waitForTimeout(250);
    inspected.push({ label: 'dark-animated-desktop', ...await layout('dark-animated-desktop') });
    await page.screenshot({ path: path.join(outputDirectory, 'gd-dark.png'), fullPage: true });
    assert.deepEqual(errors, [], 'Browser errors');
    const report = { passed: true, records: coverage.size, combinations: combinations.length, layout: inspected,
      errors, preview_sha256: digest(previewPath), payload_sha256: digest(payloadPath), checker_sha256: digest(__filename),
      covered: [...coverage], states: combinations };
    fs.writeFileSync(path.join(outputDirectory, 'browser_check.json'), JSON.stringify(report, null, 2) + '\n');
    console.log(JSON.stringify({ passed: true, records: coverage.size, combinations: combinations.length, outputDirectory }));
  } finally { await browser.close(); }
}
main().catch(error => { console.error(error); process.exitCode = 1; });
