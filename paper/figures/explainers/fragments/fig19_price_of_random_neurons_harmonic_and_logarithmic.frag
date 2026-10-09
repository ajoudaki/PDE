<h2 class="sr-only">Figure 19. Random neurons estimate the Gram with noise, selected weighted neurons reproduce it exactly; the neurons needed to match a second dense run grow like n for random neurons and polylogarithmically for Harmonic and Logarithmic.</h2>
<div style="font-size:15px;font-weight:500;color:var(--text-primary);margin:0 0 8px">Figure 19 · The price of random neurons, both selected models</div>
<div style="display:flex;align-items:center;gap:10px;margin:0 0 6px;font-size:13px;color:var(--text-secondary)">
<button id="rs" style="font-size:13px;padding:4px 10px">Resample</button>
<span>Width n</span><input type="range" id="ns" min="12" max="30" step="1" value="12" style="flex:1">
<span id="nl" style="min-width:90px;text-align:right"></span>
</div>
<svg id="sv" width="100%" viewBox="0 0 680 330" role="img"><title>Figure 19: the price of random neurons, both selected models</title><desc>Left: a neuron cloud with its Gram ellipse, six iid neurons and six selected weighted neurons. Right: neurons needed versus width for smaller dense networks, Harmonic, and Logarithmic.</desc></svg>
<div id="rd" style="font-size:13px;color:var(--text-secondary);margin-top:2px"></div>
<script>
(()=>{
const svg=document.getElementById('sv'),GN='#1baf7a',OR='#eb6834',GR='#888780';
const E=(n,a,t)=>{const e=document.createElementNS('http://www.w3.org/2000/svg',n);for(const k in a)e.setAttribute(k,a[k]);if(t!==undefined)e.textContent=t;return e};
let seed=7;const rnd=()=>{seed=(seed*16807)%2147483647;return seed/2147483647};
const gauss=()=>Math.sqrt(-2*Math.log(rnd()+1e-12))*Math.cos(2*Math.PI*rnd());
const N=600,pts=[];for(let i=0;i<N;i++){const s=0.6+0.8*rnd(),a=gauss()*s,b=gauss()*0.42*s,c=Math.cos(0.5),d=Math.sin(0.5);pts.push([c*a-d*b,d*a+c*b])}
const mom=(P,W)=>{let s=[0,0,0],t=0;P.forEach((p,i)=>{const w=W?W[i]:1;s[0]+=w*p[0]*p[0];s[1]+=w*p[0]*p[1];s[2]+=w*p[1]*p[1];t+=w});return W?s:s.map(v=>v/t)};
const S=mom(pts),fro=A=>Math.sqrt(A[0]**2+2*A[1]**2+A[2]**2),rel=A=>fro([A[0]-S[0],A[1]-S[1],A[2]-S[2]])/fro(S);
function eig(A){const tr=A[0]+A[2],det=A[0]*A[2]-A[1]*A[1],r=Math.sqrt(Math.max(tr*tr/4-det,0));return [tr/2+r,tr/2-r,Math.atan2(tr/2+r-A[0],A[1])]}
const[,,a0]=eig(S),u=[Math.cos(a0),Math.sin(a0)],v=[-Math.sin(a0),Math.cos(a0)];
const dirs=[u,[-u[0],-u[1]],v,[-v[0],-v[1]],[(u[0]+v[0])/1.41,(u[1]+v[1])/1.41],[(u[0]-v[0])/1.41,(u[1]-v[1])/1.41]];
const sel=dirs.map(d=>{let b=0,bv=-1e9;pts.forEach((p,i)=>{const r=Math.hypot(...p),val=(p[0]*d[0]+p[1]*d[1])/(r+1e-9)*Math.min(r,1.6);if(val>bv){bv=val;b=i}});return b});
const SP=sel.map(i=>pts[i]);let w=SP.map(()=>S[0]/2);
for(let it=0;it<20000;it++){const M=mom(SP,w),D=[M[0]-S[0],M[1]-S[1],M[2]-S[2]];w=w.map((wi,k)=>{const p=SP[k];return Math.max(0,wi-0.02*(D[0]*p[0]*p[0]+2*D[1]*p[0]*p[1]+D[2]*p[1]*p[1]))})}
const selErr=rel(mom(SP,w));
function ell(cx,cy,A,sc,st){const[l1,l2,ang]=eig(A);return E('ellipse',Object.assign({cx,cy,rx:2*Math.sqrt(Math.max(l1,1e-9))*sc,ry:2*Math.sqrt(Math.max(l2,1e-9))*sc,transform:`rotate(${ang*180/Math.PI} ${cx} ${cy})`,fill:'none'},st))}
function cloud(g,cx,cy,sc){pts.forEach(p=>g.appendChild(E('circle',{cx:(cx+p[0]*sc).toFixed(1),cy:(cy-p[1]*sc).toFixed(1),r:1.3,fill:GR,opacity:0.4})));g.appendChild(ell(cx,cy,S,sc,{stroke:'var(--s)','stroke-width':1,'stroke-dasharray':'4 3'}))}
const left=E('g',{}),right=E('g',{});svg.appendChild(left);svg.appendChild(right);
function drawLeft(){left.innerHTML='';const q=6,sc=26,idx=[];while(idx.length<q){const k=Math.floor(rnd()*N);if(!idx.includes(k))idx.push(k)}const IP=idx.map(i=>pts[i]),IM=mom(IP);
left.appendChild(E('text',{x:100,y:22,'text-anchor':'middle',class:'th'},'6 random neurons'));cloud(left,100,140,sc);
IP.forEach(p=>left.appendChild(E('circle',{cx:100+p[0]*sc,cy:140-p[1]*sc,r:3.4,fill:'var(--s)'})));left.appendChild(ell(100,140,IM,sc,{stroke:'var(--s)','stroke-width':2}));
left.appendChild(E('text',{x:100,y:250,'text-anchor':'middle',class:'ts'},`Gram error ${(100*rel(IM)).toFixed(0)}%`));
left.appendChild(E('text',{x:290,y:22,'text-anchor':'middle',class:'th'},'6 selected, weighted'));cloud(left,290,140,sc);
const wm=Math.max(...w);SP.forEach((p,j)=>{if(w[j]>1e-6){left.appendChild(E('circle',{cx:290+p[0]*sc,cy:140-p[1]*sc,r:3+6*Math.sqrt(w[j]/wm),fill:GN,opacity:0.75}));left.appendChild(E('circle',{cx:290+p[0]*sc,cy:140-p[1]*sc,r:3+6*Math.sqrt(w[j]/wm),fill:'none',stroke:OR,'stroke-width':1.2,'stroke-dasharray':'2 2'}))}});
left.appendChild(ell(290,140,mom(SP,w),sc,{stroke:GN,'stroke-width':2}));
left.appendChild(E('text',{x:290,y:250,'text-anchor':'middle',class:'ts'},`Gram error ${(100*selErr).toFixed(2)}%`));
left.appendChild(E('text',{x:290,y:268,'text-anchor':'middle',class:'ts'},'same step in Harmonic and Logarithmic'));
left.appendChild(E('text',{x:40,y:300,class:'ts'},'dashed ellipse: Gram of all n neurons on the source space E'))}
const CH=210/Math.pow(Math.log(4096),5.5),CL=158/Math.pow(Math.log(4096),1.5);
const qD=n=>n/2,qH=n=>CH*Math.pow(Math.log(n),5.5),qL=n=>CL*Math.pow(Math.log(n),1.5);
function drawRight(){right.innerHTML='';const p=+document.getElementById('ns').value,n=Math.pow(2,p);
const X0=432,PW=210,Y0=40,PH=210,lx=e=>X0+PW*(e-12)/18,ly=q=>Y0+PH*(1-(Math.log10(q)-1)/8);
right.appendChild(E('text',{x:X0-10,y:22,class:'th'},'Neurons to match a second dense run'));
right.appendChild(E('line',{x1:X0,y1:Y0+PH,x2:X0+PW,y2:Y0+PH,stroke:'var(--b)','stroke-width':0.5}));right.appendChild(E('line',{x1:X0,y1:Y0,x2:X0,y2:Y0+PH,stroke:'var(--b)','stroke-width':0.5}));
[[qD,GR,'smaller dense ∝ n'],[qH,GN,'Harmonic ∝ (log n)^5.5'],[qL,OR,'Logarithmic ∝ (log n)^1.5']].forEach(([f,c,lab],k)=>{let d='';for(let e=12;e<=30.001;e+=0.25)d+=(e===12?'M':'L')+lx(e).toFixed(1)+' '+ly(f(Math.pow(2,e))).toFixed(1);
right.appendChild(E('path',{d,fill:'none',stroke:c,'stroke-width':2}));
const ty=[ly(qD(2**26))-8,ly(qH(2**30))-10,ly(qL(2**30))+26][k];right.appendChild(E('text',{x:k===0?lx(26):X0+PW,y:ty,'text-anchor':'end',class:'ts'},lab))});
[[2048,GR],[210,GN],[158,OR]].forEach(([q,c])=>right.appendChild(E('circle',{cx:lx(12),cy:ly(q),r:4.5,fill:'none',stroke:c,'stroke-width':1.6})));
right.appendChild(E('line',{x1:lx(p),y1:Y0,x2:lx(p),y2:Y0+PH,stroke:GR,'stroke-width':0.8,'stroke-dasharray':'2 3'}));
[[qD,GR],[qH,GN],[qL,OR]].forEach(([f,c])=>right.appendChild(E('circle',{cx:lx(p),cy:ly(f(n)),r:4,fill:c})));
[[12,'4k'],[16,'65k'],[20,'1M'],[25,'34M'],[30,'1B']].forEach(([e,s])=>right.appendChild(E('text',{x:lx(e),y:Y0+PH+16,'text-anchor':'middle',class:'ts'},s)));
[[1e2,'100'],[1e4,'10⁴'],[1e6,'10⁶'],[1e8,'10⁸']].forEach(([q,s])=>right.appendChild(E('text',{x:X0-6,y:ly(q)+4,'text-anchor':'end',class:'ts'},s)));
right.appendChild(E('text',{x:X0+PW/2,y:Y0+PH+34,'text-anchor':'middle',class:'ts'},'width n (log); rings: runs at n = 4,096'));
document.getElementById('nl').textContent='n = '+(n>=1e6?(n/1048576).toFixed(0)+'M':n.toLocaleString());
const f=v=>Math.round(v).toLocaleString(),s2=v=>(v*v).toExponential(1);
document.getElementById('rd').textContent=`Neurons kept (state ≈ q²): smaller dense ${f(qD(n))} (${s2(qD(n))}) · Harmonic ${f(qH(n))} (${s2(qH(n))}) · Logarithmic ${f(qL(n))} (${s2(qL(n))})`}
document.getElementById('rs').onclick=drawLeft;document.getElementById('ns').oninput=drawRight;drawLeft();drawRight();
})();
</script>