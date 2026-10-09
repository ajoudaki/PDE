<h2 class="sr-only">Figure 19b. Random neurons estimate the Gram with error falling like q to the minus one half; six selected weighted neurons are exact, a step shared by Harmonic and Logarithmic; below, neurons needed versus width for both selected models and for smaller dense networks.</h2>
<div style="font-size:15px;font-weight:500;color:var(--text-primary);margin:0 0 8px">Figure 19b · The price of random neurons</div>
<div style="display:flex;align-items:center;gap:12px;margin:0 0 6px;font-size:13px;color:var(--text-secondary)">
<span>Random neurons q</span><input type="range" id="qq" min="0" max="11" step="1" value="2" style="flex:1"><span id="ql" style="min-width:230px;text-align:right"></span>
</div>
<svg id="sv" width="100%" viewBox="0 0 680 290" role="img"><title>Figure 19b: random versus selected neurons</title><desc>iid sample, selected neurons, and Gram error versus q.</desc></svg>
<div style="display:flex;align-items:center;gap:12px;margin:10px 0 6px;font-size:13px;color:var(--text-secondary)">
<span>Width n</span><input type="range" id="ns" min="12" max="30" step="1" value="12" style="flex:1"><span id="nl" style="min-width:90px;text-align:right"></span>
</div>
<svg id="sv2" width="100%" viewBox="0 0 680 270" role="img"><title>Neurons needed versus width</title><desc>Smaller dense networks need a number of neurons proportional to n; Harmonic and Logarithmic need polylogarithmically many.</desc></svg>
<div id="rd" style="font-size:13px;color:var(--text-secondary)"></div>
<script>
(()=>{
const svg=document.getElementById('sv'),GN='#1baf7a',OR='#eb6834',GR='#888780';
const E=(n,a,t)=>{const e=document.createElementNS('http://www.w3.org/2000/svg',n);for(const k in a)e.setAttribute(k,a[k]);if(t!==undefined)e.textContent=t;return e};
let seed=7;const rnd=()=>{seed=(seed*16807)%2147483647;return seed/2147483647};
const gauss=()=>Math.sqrt(-2*Math.log(rnd()+1e-12))*Math.cos(2*Math.PI*rnd());
const N=600,pts=[];for(let i=0;i<N;i++){const s=0.6+0.8*rnd();const a=gauss()*s,b=gauss()*0.42*s;const c=Math.cos(0.5),d=Math.sin(0.5);pts.push([c*a-d*b,d*a+c*b])}
const mom=(P,W)=>{let s=[0,0,0],t=0;P.forEach((p,i)=>{const w=W?W[i]:1;s[0]+=w*p[0]*p[0];s[1]+=w*p[0]*p[1];s[2]+=w*p[1]*p[1];t+=w});return W?s:s.map(v=>v/t)};
const S=mom(pts),fro=A=>Math.sqrt(A[0]**2+2*A[1]**2+A[2]**2),rel=A=>fro([A[0]-S[0],A[1]-S[1],A[2]-S[2]])/fro(S);
function eig(A){const tr=A[0]+A[2],det=A[0]*A[2]-A[1]*A[1],r=Math.sqrt(Math.max(tr*tr/4-det,0));return [tr/2+r,tr/2-r,Math.atan2(tr/2+r-A[0],A[1])]}
const[,,a0]=eig(S);const u=[Math.cos(a0),Math.sin(a0)],v=[-Math.sin(a0),Math.cos(a0)];
const dirs=[u,[-u[0],-u[1]],v,[-v[0],-v[1]],[(u[0]+v[0])/1.41,(u[1]+v[1])/1.41],[(u[0]-v[0])/1.41,(u[1]-v[1])/1.41]];
const sel=dirs.map(d=>{let b=0,bv=-1e9;pts.forEach((p,i)=>{const r=Math.hypot(...p),val=(p[0]*d[0]+p[1]*d[1])/(r+1e-9)*Math.min(r,1.6);if(val>bv){bv=val;b=i}});return b});
const SP=sel.map(i=>pts[i]);let w=SP.map(()=>S[0]/2);
for(let it=0;it<20000;it++){const M=mom(SP,w),D=[M[0]-S[0],M[1]-S[1],M[2]-S[2]];w=w.map((wi,k)=>{const p=SP[k];return Math.max(0,wi-0.02*(D[0]*p[0]*p[0]+2*D[1]*p[0]*p[1]+D[2]*p[1]*p[1]))})}
const selErr=Math.max(rel(mom(SP,w)),1e-6);
const Q=[3,4,6,8,12,16,24,32,48,64,96,128],stats=Q.map(q=>{const e=[];for(let r=0;r<300;r++){const idx=[];while(idx.length<q){const k=Math.floor(rnd()*N);if(!idx.includes(k))idx.push(k)}e.push(rel(mom(idx.map(i=>pts[i]))))}e.sort((a,b)=>a-b);return [e[30],e[150],e[270]]});
function ell(cx,cy,A,sc,st){const[l1,l2,ang]=eig(A);return E('ellipse',Object.assign({cx,cy,rx:2*Math.sqrt(Math.max(l1,1e-9))*sc,ry:2*Math.sqrt(Math.max(l2,1e-9))*sc,transform:`rotate(${ang*180/Math.PI} ${cx} ${cy})`,fill:'none'},st))}
function cloud(cx,cy,sc){pts.forEach(p=>svg.appendChild(E('circle',{cx:cx+p[0]*sc,cy:cy-p[1]*sc,r:1.4,fill:'#B4B2A9',opacity:0.45})));svg.appendChild(ell(cx,cy,S,sc,{stroke:'var(--s)','stroke-width':1,'stroke-dasharray':'4 3'}))}
function draw(){const qi=+document.getElementById('qq').value,q=Q[qi];svg.innerHTML='';const sc=27;
const idx=[];while(idx.length<q){const k=Math.floor(rnd()*N);if(!idx.includes(k))idx.push(k)}const IP=idx.map(i=>pts[i]),IM=mom(IP);
svg.appendChild(E('text',{x:105,y:22,'text-anchor':'middle',class:'th'},`${q} random neurons`));cloud(105,135,sc);
IP.forEach(p=>svg.appendChild(E('circle',{cx:105+p[0]*sc,cy:135-p[1]*sc,r:3.2,fill:'#5F5E5A'})));svg.appendChild(ell(105,135,IM,sc,{stroke:'#5F5E5A','stroke-width':2}));
svg.appendChild(E('text',{x:105,y:262,'text-anchor':'middle',class:'ts'},`Gram error ${(100*rel(IM)).toFixed(0)}%`));
svg.appendChild(E('text',{x:315,y:22,'text-anchor':'middle',class:'th'},'6 selected, weighted'));cloud(315,135,sc);
const wm=Math.max(...w);SP.forEach((p,j)=>{if(w[j]>1e-6){const r=3+6*Math.sqrt(w[j]/wm);svg.appendChild(E('circle',{cx:315+p[0]*sc,cy:135-p[1]*sc,r,fill:GN,opacity:0.8}));svg.appendChild(E('circle',{cx:315+p[0]*sc,cy:135-p[1]*sc,r:r+1.5,fill:'none',stroke:OR,'stroke-width':1.2,'stroke-dasharray':'2 2'}))}});svg.appendChild(ell(315,135,mom(SP,w),sc,{stroke:GN,'stroke-width':2}));
svg.appendChild(E('text',{x:315,y:262,'text-anchor':'middle',class:'ts'},'metric weights: exact on E'));
svg.appendChild(E('text',{x:315,y:280,'text-anchor':'middle',class:'ts'},'shared by Harmonic and Logarithmic'));
const X0=450,W=200,Y0=40,H=190,lx=q=>X0+W*(Math.log10(q)-Math.log10(3))/(Math.log10(128)-Math.log10(3)),ly=e=>Y0+H*(-Math.log10(e))/6;
svg.appendChild(E('text',{x:X0+W/2,y:22,'text-anchor':'middle',class:'th'},'Error versus q'));
svg.appendChild(E('line',{x1:X0,y1:Y0+H,x2:X0+W,y2:Y0+H,stroke:'var(--b)','stroke-width':0.5}));svg.appendChild(E('line',{x1:X0,y1:Y0,x2:X0,y2:Y0+H,stroke:'var(--b)','stroke-width':0.5}));
let band='M'+Q.map((q,i)=>lx(q).toFixed(1)+' '+ly(stats[i][2]).toFixed(1)).join('L')+'L'+Q.slice().reverse().map((q,i)=>lx(q).toFixed(1)+' '+ly(stats[Q.length-1-i][0]).toFixed(1)).join('L')+'Z';
svg.appendChild(E('path',{d:band,fill:GR,opacity:0.3,stroke:'none'}));
svg.appendChild(E('path',{d:'M'+Q.map((q,i)=>lx(q).toFixed(1)+' '+ly(stats[i][1]).toFixed(1)).join('L'),fill:'none',stroke:'#5F5E5A','stroke-width':2}));
svg.appendChild(E('line',{x1:lx(3),y1:ly(selErr),x2:lx(128),y2:ly(selErr),stroke:GN,'stroke-width':2}));
svg.appendChild(E('circle',{cx:lx(q),cy:ly(stats[qi][1]),r:4.5,fill:'#5F5E5A'}));
svg.appendChild(E('text',{x:X0+W,y:ly(stats[11][0])+16,'text-anchor':'end',class:'ts'},'random ~ q^(-1/2)'));
svg.appendChild(E('text',{x:X0+W,y:ly(selErr)-8,'text-anchor':'end',class:'ts'},'selected: exact'));
svg.appendChild(E('text',{x:X0+W/2,y:Y0+H+18,'text-anchor':'middle',class:'ts'},'neurons q, 3 to 128 (log)'));
document.getElementById('ql').textContent=`q = ${q}: random median error ${(100*stats[qi][1]).toFixed(0)}%`}
document.getElementById('qq').oninput=draw;draw();
const s2=document.getElementById('sv2');
const CH=210/Math.pow(Math.log(4096),5.5),CL=158/Math.pow(Math.log(4096),1.5);
const qD=n=>n/2,qH=n=>CH*Math.pow(Math.log(n),5.5),qL=n=>CL*Math.pow(Math.log(n),1.5);
function draw2(){s2.innerHTML='';const p=+document.getElementById('ns').value,n=Math.pow(2,p);
const X0=90,PW=410,Y0=30,PH=190,lx=e=>X0+PW*(e-12)/18,ly=q=>Y0+PH*(1-(Math.log10(q)-1)/8);
s2.appendChild(E('text',{x:40,y:16,class:'th'},'Neurons needed to match a second dense run'));
s2.appendChild(E('line',{x1:X0,y1:Y0+PH,x2:X0+PW,y2:Y0+PH,stroke:'var(--b)','stroke-width':0.5}));s2.appendChild(E('line',{x1:X0,y1:Y0,x2:X0,y2:Y0+PH,stroke:'var(--b)','stroke-width':0.5}));
[[qD,GR,'smaller dense ∝ n'],[qH,GN,'Harmonic ∝ (log n)^5.5'],[qL,OR,'Logarithmic ∝ (log n)^1.5']].forEach(([f,c,lab])=>{let d='';for(let e=12;e<=30.001;e+=0.25)d+=(e===12?'M':'L')+lx(e).toFixed(1)+' '+ly(f(Math.pow(2,e))).toFixed(1);
s2.appendChild(E('path',{d,fill:'none',stroke:c,'stroke-width':2}));s2.appendChild(E('text',{x:X0+PW+8,y:ly(f(2**30))+4,class:'ts'},lab))});
[[2048,GR],[210,GN],[158,OR]].forEach(([q,c])=>s2.appendChild(E('circle',{cx:lx(12),cy:ly(q),r:4.5,fill:'none',stroke:c,'stroke-width':1.6})));
s2.appendChild(E('line',{x1:lx(p),y1:Y0,x2:lx(p),y2:Y0+PH,stroke:GR,'stroke-width':0.8,'stroke-dasharray':'2 3'}));
[[qD,GR],[qH,GN],[qL,OR]].forEach(([f,c])=>s2.appendChild(E('circle',{cx:lx(p),cy:ly(f(n)),r:4,fill:c})));
[[12,'4k'],[16,'65k'],[20,'1M'],[25,'34M'],[30,'1B']].forEach(([e,s])=>s2.appendChild(E('text',{x:lx(e),y:Y0+PH+16,'text-anchor':'middle',class:'ts'},s)));
[[1e2,'100'],[1e4,'10⁴'],[1e6,'10⁶'],[1e8,'10⁸']].forEach(([q,s])=>s2.appendChild(E('text',{x:X0-6,y:ly(q)+4,'text-anchor':'end',class:'ts'},s)));
s2.appendChild(E('text',{x:X0+PW/2,y:Y0+PH+34,'text-anchor':'middle',class:'ts'},'width n (log); rings: runs at n = 4,096; lines: theorem growth rates'));
document.getElementById('nl').textContent='n = '+(n>=1e6?(n/1048576).toFixed(0)+'M':n.toLocaleString());
const f=v=>Math.round(v).toLocaleString();
document.getElementById('rd').textContent=`Neurons kept: smaller dense ${f(qD(n))} · Harmonic ${f(qH(n))} · Logarithmic ${f(qL(n))} (state grows like q²)`}
document.getElementById('ns').oninput=draw2;draw2();
})();
</script>