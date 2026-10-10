from pathlib import Path
import subprocess, json, time, urllib.request, websocket, base64, sys

run = Path(__file__).resolve().parent.parent
scratch = Path(__file__).resolve().parent
chrome = run.parent/'promotion_tooling/share/quarto/chrome-headless-shell/chrome-headless-shell-linux64/chrome-headless-shell'
online = '--online' in sys.argv
suffix = '_online' if online else ''
profile = scratch/('chrome-cdp'+suffix+'-'+str(time.time_ns()))
log = (scratch/('browser_cdp'+suffix+'.log')).open('w')
proc = subprocess.Popen([str(chrome), '--no-sandbox', '--disable-dev-shm-usage',
    '--remote-allow-origins=*', '--remote-debugging-port=0',
    '--allow-file-access-from-files', '--no-proxy-server',
    *([] if online else ['--host-resolver-rules=MAP cdnjs.cloudflare.com ~NOTFOUND, MAP cdn.jsdelivr.net ~NOTFOUND']),
    '--user-data-dir='+str(profile), 'about:blank'], stdout=log, stderr=log)
try:
    portfile=profile/'DevToolsActivePort'
    for _ in range(100):
        if portfile.exists():break
        time.sleep(.1)
    port=portfile.read_text().splitlines()[0]
    targets=json.load(urllib.request.urlopen('http://127.0.0.1:'+port+'/json'))
    ws=websocket.create_connection(targets[0]['webSocketDebuggerUrl'],timeout=30)
    seq=0
    def call(method,params=None):
        global seq
        seq+=1
        ws.send(json.dumps({'id':seq,'method':method,'params':params or {}}))
        while True:
            reply=json.loads(ws.recv())
            if reply.get('id')==seq:
                if 'error' in reply:raise RuntimeError(reply)
                return reply.get('result',{})
    call('Page.enable')
    call('Emulation.setDeviceMetricsOverride',{'width':1500,'height':1100,'deviceScaleFactor':1,'mobile':False})
    url=(run/'rendered_html/02-gaussian-reuse.html').as_uri()
    call('Page.navigate',{'url':url})
    for _ in range(100):
        state=call('Runtime.evaluate',{'expression':'document.readyState','returnByValue':True})
        if state['result'].get('value')=='complete':break
        time.sleep(.1)
    if online:
        for _ in range(200):
            state=call('Runtime.evaluate',{'expression':'!!window.MathJax && !!document.querySelector("mjx-container")','returnByValue':True})
            if state['result'].get('value'):break
            time.sleep(.1)
    records={}
    for name,anchor in [('definition','def-mfp-primitive-program'),('theorem','thm-mfp-finite-derivative-program'),('proof','proof-mfp-raw-entry-moments'),('kernel','eq-mfp-kernel-example-clock')]:
        expression="""(() => {const el=document.getElementById(%s); el.scrollIntoView(); return {ready:document.readyState, title:document.title, text:el.innerText, rect:el.getBoundingClientRect().toJSON(), body:document.body.getBoundingClientRect().toJSON(), mathJax:!!window.MathJax, mainDisplay:getComputedStyle(document.querySelector('main')).display};})()""" % json.dumps(anchor)
        records[name]=call('Runtime.evaluate',{'expression':expression,'returnByValue':True})
        time.sleep(.5)
        shot=call('Page.captureScreenshot',{'format':'png','captureBeyondViewport':False})
        (scratch/('browser_'+name+suffix+'.png')).write_bytes(base64.b64decode(shot['data']))
    records['math_errors']=call('Runtime.evaluate',{'expression':'Array.from(document.querySelectorAll("mjx-merror")).map(e=>e.innerText)','returnByValue':True})
    records['new_math_widths']=call('Runtime.evaluate',{'expression':'''(() => {const main=document.querySelector('main').getBoundingClientRect(); const sec=document.getElementById('sec-mfp-finite-derivative-programs');return Array.from(sec.querySelectorAll('mjx-container[display="true"]')).map(e=>{const math=e.querySelector('mjx-math'); const r=(math||e).getBoundingClientRect();const anchor=e.closest('[id]'); return {anchor:anchor&&anchor.id,text:e.innerText,width:r.width,left:r.left,right:r.right,mainLeft:main.left,mainRight:main.right,overflow:getComputedStyle(e).overflowX};}).filter(e=>e.left<e.mainLeft-3||e.right>e.mainRight+3);})()''','returnByValue':True})
    (scratch/('browser_checks'+suffix+'.json')).write_text(json.dumps(records,indent=2)+'\n')
    print(json.dumps(records,indent=2))
finally:
    proc.terminate()
    proc.wait(timeout=10)
    log.close()
