from pathlib import Path
import subprocess,json,time,urllib.request,websocket,base64,sys
R=Path(__file__).resolve().parent.parent; S=R/'integration_reviewer'; chrome=R.parent/'promotion_tooling/share/quarto/chrome-headless-shell/chrome-headless-shell-linux64/chrome-headless-shell'
log=(S/'browser.log').open('w'); port=9347
proc=subprocess.Popen([str(chrome),'--no-sandbox','--disable-gpu','--disable-dev-shm-usage','--allow-file-access-from-files','--remote-allow-origins=*',f'--remote-debugging-port={port}',f'--user-data-dir={S}/chrome_profile','about:blank'],stdout=log,stderr=log)
try:
 for _ in range(100):
  try:
   pages=json.load(urllib.request.urlopen(f'http://127.0.0.1:{port}/json'));break
  except Exception:time.sleep(.1)
 ws=websocket.create_connection(pages[0]['webSocketDebuggerUrl'],timeout=600); seq=0
 def call(method,params={}):
  global seq
  seq+=1; ws.send(json.dumps(dict(id=seq,method=method,params=params)))
  while True:
   msg=json.loads(ws.recv())
   if msg.get('id')==seq:
    if 'error' in msg:raise RuntimeError(msg)
    return msg.get('result',{})
 def js(expression,awaitPromise=False):
  out=call('Runtime.evaluate',dict(expression=expression,returnByValue=True,awaitPromise=awaitPromise))
  if 'exceptionDetails' in out:raise RuntimeError(out)
  return out['result'].get('value')
 call('Page.enable');call('Runtime.enable')
 call('Emulation.setDeviceMetricsOverride',dict(width=1500,height=1100,deviceScaleFactor=1,mobile=False))
 call('Page.navigate',dict(url=(R/'rendered_html/02-gaussian-reuse.html').as_uri()))
 for _ in range(120):
  if js('Boolean(window.MathJax && MathJax.startup && MathJax.startup.promise)'):break
  time.sleep(.5)
 def readiness():
  return js("""(()=>{const d=[...document.querySelectorAll('#sec-mfp-finite-derivative-programs .math.display')];return {count:d.length,typeset:d.filter(e=>e.querySelector('mjx-math')).length,fonts:document.fonts.status,widths:d.map(e=>e.querySelector('mjx-math')?.getBoundingClientRect().width),loadedFonts:[...document.fonts].filter(f=>f.status==='loaded').map(f=>f.family)}})()""")
 samples=[]
 for _ in range(180):
  state=readiness()
  if state['count']==44 and state['typeset']==44 and state['fonts']=='loaded':
   samples.append(state)
   if len(samples)>=3 and samples[-1]['widths']==samples[-2]['widths']==samples[-3]['widths']:break
  else:samples=[]
  time.sleep(1)
 assert len(samples)>=3 and samples[-1]['widths']==samples[-2]['widths']==samples[-3]['widths'],samples
 samples=samples[-3:]
 ready=dict(criterion='Every one of 44 new-section displays contains mjx-math, fonts loaded, three stable width samples separated by one second',samples=samples)
 (S/'mathjax_readiness.json').write_text(json.dumps(ready,indent=2)); print('Scoped MathJax readiness established',flush=True)
 results=[]
 for width in [1500,1280]:
  call('Emulation.setDeviceMetricsOverride',dict(width=width,height=1100,deviceScaleFactor=1,mobile=False))
  time.sleep(.4)
  data=js('''(()=>{const root=document.querySelector('#sec-mfp-finite-derivative-programs'); const main=document.querySelector('main'); const b=main.getBoundingClientRect(); const displays=[...root.querySelectorAll('.math.display')]; const rect=e=>{const r=e.getBoundingClientRect();return {x:r.x,y:r.y,width:r.width,height:r.height,right:r.right,bottom:r.bottom}};return {article:rect(main),heading:root.querySelector('h2').textContent,displayCount:displays.length,errors:root.querySelectorAll('mjx-merror').length,untypeset:displays.filter(e=>!e.querySelector('mjx-container')).map(e=>e.textContent),displays:displays.map((e,i)=>{const m=e.querySelector('mjx-math');const box=m?rect(m):null; const children=m?[...m.querySelectorAll('*')].map(rect).filter(r=>r.width&&r.height):[];const left=Math.min(box?box.x:Infinity,...children.map(r=>r.x));const right=Math.max(box?box.right:-Infinity,...children.map(r=>r.right));return {index:i,id:e.closest('[id]')?.id,box,left,right,outside:left<b.x-.75||right>b.right+.75,tex:e.textContent}}),sidebar:rect(document.querySelector('#quarto-sidebar')),toc:rect(document.querySelector('#quarto-margin-sidebar')),definition:root.querySelector('#def-mfp-primitive-program')?.textContent.slice(0,150)}})()''')
  data['viewport']=width;results.append(data)
  print('Measured',width,'displays',data['displayCount'],'untypeset',len(data['untypeset']),'outside',sum(d['outside'] for d in data['displays']),flush=True)
  ids=['eq-mfp-expectation-graph','eq-mfp-forward-ad','eq-mfp-kernel-example-clock','eq-mfp-jet-algebra','eq-mfp-source-response']
  for ident in ids:
   clip=js(f'''(()=>{{const e=document.getElementById({json.dumps(ident)});e.scrollIntoView({{block:'center',behavior:'instant'}});const r=e.getBoundingClientRect();return {{x:Math.max(0,r.x-12),y:Math.max(0,r.y+scrollY-12),width:Math.min(innerWidth-r.x+12,r.width+24),height:r.height+24,scale:1}}}})()''')
   time.sleep(.5)
   shot=call('Page.captureScreenshot',dict(format='png',captureBeyondViewport=False))
   (S/f'{width}_{ident}.png').write_bytes(base64.b64decode(shot['data']))
  js("document.getElementById('sec-mfp-finite-derivative-programs').scrollIntoView({behavior:'instant'})")
  shot=call('Page.captureScreenshot',dict(format='png',captureBeyondViewport=False));(S/f'{width}_navigation.png').write_bytes(base64.b64decode(shot['data']))
 (S/'mathjax_layout.json').write_text(json.dumps(results,indent=2))
finally:
 proc.terminate();proc.wait(timeout=15);log.close()
