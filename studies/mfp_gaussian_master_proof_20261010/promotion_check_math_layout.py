"""Typeset the candidate chapter and measure all new display-math bounds."""
from pathlib import Path
import argparse
import base64
import json
import subprocess
import time
import urllib.request
import websocket

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('run')
parser.add_argument('--widths', default='1500,1280')
parser.add_argument('--output-name', default='math_layout_check')
args = parser.parse_args()
study = Path(__file__).resolve().parent
generated = study.parents[1] / 'data/generated' / study.name
run = generated / args.run
assert Path(args.output_name).name == args.output_name
scratch = run / args.output_name
scratch.mkdir(exist_ok=False)
chrome = generated / 'promotion_tooling/share/quarto/chrome-headless-shell/chrome-headless-shell-linux64/chrome-headless-shell'
profile = scratch / 'chrome-profile'
with (scratch / 'browser.log').open('w') as log:
    process = subprocess.Popen([
        str(chrome), '--no-sandbox', '--disable-dev-shm-usage',
        '--remote-allow-origins=*', '--remote-debugging-port=0',
        '--allow-file-access-from-files', '--no-proxy-server',
        '--user-data-dir=' + str(profile), 'about:blank'], stdout=log, stderr=log)
    try:
        portfile = profile / 'DevToolsActivePort'
        for _ in range(150):
            if portfile.exists():
                break
            time.sleep(.1)
        port = portfile.read_text().splitlines()[0]
        targets = json.load(urllib.request.urlopen('http://127.0.0.1:' + port + '/json'))
        connection = websocket.create_connection(targets[0]['webSocketDebuggerUrl'], timeout=60)
        sequence = 0

        def call(method, params=None):
            global sequence
            sequence += 1
            connection.send(json.dumps({'id': sequence, 'method': method, 'params': params or {}}))
            while True:
                reply = json.loads(connection.recv())
                if reply.get('id') == sequence:
                    assert 'error' not in reply, reply
                    return reply.get('result', {})

        def evaluate(expression, await_promise=False):
            result = call('Runtime.evaluate', {'expression': expression,
                'returnByValue': True, 'awaitPromise': await_promise})
            assert 'exceptionDetails' not in result, result
            return result['result'].get('value')

        call('Page.enable')
        call('Page.navigate', {'url': (run / 'rendered_html/02-gaussian-reuse.html').as_uri()})
        for _ in range(400):
            if evaluate('document.readyState === "complete" && !!window.MathJax?.startup?.promise'):
                break
            time.sleep(.1)
        assert evaluate('!!window.MathJax?.startup?.promise'), 'MathJax unavailable'
        previous = None
        stable = 0
        readiness = None
        for _ in range(300):
            readiness = evaluate('''(() => {
                const s=document.getElementById('sec-mfp-finite-derivative-programs');
                const sources=Array.from(s.querySelectorAll('.math.display'));
                const rendered=Array.from(s.querySelectorAll('mjx-container[display="true"] mjx-math'));
                return {fonts:document.fonts.status, expected:sources.length,
                    rendered:rendered.length, widths:rendered.map(e=>e.getBoundingClientRect().width)};
            })()''')
            if (readiness['expected'] > 0 and readiness['expected'] == readiness['rendered']
                    and readiness['fonts'] == 'loaded' and readiness == previous):
                stable += 1
                if stable >= 5:
                    break
            else:
                stable = 0
            previous = readiness
            time.sleep(.2)
        (scratch / 'readiness.json').write_text(json.dumps(readiness, indent=2) + '\n')
        assert stable >= 5, readiness
        records = {'mathjax_version': evaluate('MathJax.version'),
                   'new_section_all_displays_typeset_and_fonts_loaded': True, 'viewports': []}
        for width in map(int, args.widths.split(',')):
            call('Emulation.setDeviceMetricsOverride', {'width': width, 'height': 1100,
                'deviceScaleFactor': 1, 'mobile': False})
            time.sleep(.5)
            measured = evaluate('''(() => {
                const main=document.querySelector('main').getBoundingClientRect();
                const section=document.getElementById('sec-mfp-finite-derivative-programs');
                const displays=Array.from(section.querySelectorAll('mjx-container[display="true"]'));
                return {main_width:main.width, display_count:displays.length,
                    math_errors:Array.from(section.querySelectorAll('mjx-merror')).map(e=>e.innerText),
                    overflows:displays.map(e=>{
                        const r=(e.querySelector('mjx-math')||e).getBoundingClientRect();
                        return {anchor:e.closest('[id]')?.id, width:r.width,
                            left:r.left, right:r.right, main_left:main.left, main_right:main.right};
                    }).filter(e=>e.left<e.main_left-3 || e.right>e.main_right+3)};
            })()''')
            measured['viewport_width'] = width
            records['viewports'].append(measured)
            for anchor in ('eq-mfp-expectation-graph', 'eq-mfp-forward-ad', 'eq-mfp-kernel-example-clock'):
                evaluate('document.getElementById(' + json.dumps(anchor) + ').scrollIntoView()')
                time.sleep(.2)
                shot = call('Page.captureScreenshot', {'format': 'png', 'captureBeyondViewport': False})
                (scratch / f'{width}_{anchor}.png').write_bytes(base64.b64decode(shot['data']))
        (scratch / 'result.json').write_text(json.dumps(records, indent=2) + '\n')
        print(json.dumps(records, indent=2))
        assert all(not row['overflows'] and not row['math_errors'] for row in records['viewports'])
    finally:
        process.terminate()
        process.wait(timeout=10)
