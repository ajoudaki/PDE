from pathlib import Path
import subprocess,time,json,urllib.request,websocket,base64
S=Path(__file__).resolve().parent;R=S.parent
chrome=R.parent/'promotion_tooling/share/quarto/chrome-headless-shell/chrome-headless-shell-linux64/chrome-headless-shell'
profile=S/'cdp-profile';profile.mkdir(exist_ok=True)
log=(S/'cdp_browser.log').open('w')
p=subprocess.Popen([str(chrome),'--no-sandbox','--disable-gpu','--allow-file-access-from-files','--remote-debugging-port=0','--remote-allow-origins=*','--user-data-dir='+str(profile),'about:blank'],stdout=log,stderr=log)
results=[]
try:
 for _ in range(100):
  if (profile/'DevToolsActivePort').exists():break
  time.sleep(.1)
 port=(profile/'DevToolsActivePort').read_text().splitlines()[0]
 tabs=json.load(urllib.request.urlopen('http://127.0.0.1:'+port+'/json'))
 ws=websocket.create_connection(tabs[0]['webSocketDebuggerUrl'],timeout=60);count=0
 def call(method,params={}):
  global count
  count+=1;ws.send(json.dumps(dict(id=count,method=method,params=params)))
  while True:
   ans=json.loads(ws.recv())
   if ans.get('id')==count:return ans
 def evaluate(expr):return call('Runtime.evaluate',dict(expression=expr,returnByValue=True))
 call('Page.enable');call('Runtime.enable');call('Emulation.setDeviceMetricsOverride',dict(width=1500,height=1200,deviceScaleFactor=1,mobile=False))
 print(call('Page.navigate',dict(url=(R/'rendered_html/02-gaussian-reuse.html').as_uri())),flush=True)
 for n in range(30):
  status=evaluate('JSON.stringify({ready:document.readyState,body:!!document.body,math:!!window.MathJax,mjx:document.querySelectorAll("mjx-container").length,scroll:scrollY,height:document.body?.scrollHeight})');print(n,status,flush=True)
  results.append(status)
  if n>=4 and '"ready":"complete"' in status.get('result',{}).get('result',{}).get('value',''):break
  time.sleep(1)
 for name,target in [('opening','sec-mfp-finite-derivative-programs'),('adjoints','eq-mfp-coordinate-adjoint'),('interface','sec-mfp-symbolic-interface')]:
  evaluate('document.documentElement.style.scrollBehavior="auto";document.getElementById('+json.dumps(target)+').scrollIntoView({behavior:"instant",block:"start"})');time.sleep(1)
  detail=evaluate('JSON.stringify({bodyStyle:getComputedStyle(document.body).cssText,visibility:getComputedStyle(document.body).visibility,rect:document.getElementById('+json.dumps(target)+').getBoundingClientRect().toJSON(),title:document.title,mjx:document.querySelectorAll("mjx-container").length,errors:[...document.querySelectorAll("mjx-merror")].map(e=>e.textContent)})');print(name,detail,flush=True);results.append(dict(name=name,detail=detail))
  shot=call('Page.captureScreenshot',dict(format='png',captureBeyondViewport=False));(S/f'html_{name}_cdp.png').write_bytes(base64.b64decode(shot['result']['data']))
 (S/'browser_checks.json').write_text(json.dumps(results,indent=2)+'\n')
finally:
 p.terminate()
 try:p.wait(timeout=10)
 except subprocess.TimeoutExpired:p.kill();p.wait()
