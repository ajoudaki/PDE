<h2 class="sr-only">Figure 19c. Neuron selection, the step used by Harmonic and Logarithmic: random neurons estimate the Gram of the source space with error falling like q to the minus one half and need about half of all neurons to match a second dense network; six selected weighted neurons are exact at every width.</h2>
<div style="font-size:15px;font-weight:500;color:var(--text-primary);margin:0 0 6px">Figure 19c · The price of random neurons</div>
<div style="display:flex;flex-wrap:wrap;gap:6px;margin:0 0 8px;font-size:12px">
<span style="background:var(--bg-success);color:var(--text-success);padding:2px 8px;border-radius:var(--radius)">Harmonic: selects neurons</span>
<span style="background:var(--bg-success);color:var(--text-success);padding:2px 8px;border-radius:var(--radius)">Logarithmic: selects neurons</span>
<span style="background:var(--surface-1);color:var(--text-secondary);padding:2px 8px;border-radius:var(--radius)">Legendre: keeps all n neurons, compresses time</span>
</div>
<div style="display:flex;align-items:center;gap:10px;margin:0 0 6px;font-size:13px;color:var(--text-secondary)">
<span>Width n</span><select id="ns" style="font-size:13px"><option>300</option><option selected>600</option><option>1200</option><option>2400</option></select>
<span>Random neurons q</span><input type="range" id="qq" min="0" max="20" step="1" value="4" style="flex:1"><span id="ql" style="min-width:40px;text-align:right"></span>
<button id="rd" style="font-size:13px;padding:4px 10px">Draw again</button>
</div>
<svg id="sv" width="100%" viewBox="0 0 680 270" role="img"><title>Figure 19c: random versus selected neurons</title><desc>All neurons with the Gram ellipse of the source space, q random neurons, and six selected weighted neurons.</desc></svg>
<svg id="sv2" width="100%" viewBox="0 0 680 250" role="img"><title>Gram error versus q</title><desc>Random-neuron error band versus q, the level of a second dense network, and the exact selected model.</desc></svg>
<div id="rdt" style="font-size:13px;color:var(--text-secondary);margin-top:2px"></div>
<script>
(()=>{
const s1=document.getElementById('sv'),s2=document.getElementById('sv2'),GN='#1baf7a',GR='#888780',DK='#5F5E5A';
const E=(n,a,t)=>{const e=document.createElementNS('http://www.w3.org/2000/svg',n);for(const k in a)e.setAttribute(k,a[k]);if(t!==undefined)e.textContent=t;return e};
let seed=7;const rnd=()=>{seed=(seed*16807)%2147483647;return seed/2147483647};
const gauss=()=>Math.sqrt(-2*Math.log(rnd()+1e-12))*Math.cos(2*Math.PI*rnd());
const neuron=()=>{const s=0.6+0.8*rnd(),a=gauss()*s,b=gauss()*0.42*s,c=Math.cos(0.5),d=Math.sin(0.5);return [c*a-d*b,d*a+c*b]};
const mom=(P,W)=>{let s=[0,0,0],t=0;P.forEach((p,i)=>{const w=W?W[i]:1;s[0]+=w*p[0]*p[0];s[1]+=w*p[0]*p[1];s[2]+=w*p[1]*p[1];t+=w});return W?s:s.map(v=>v/t)};
const fro=A=>Math.sqrt(A[0]**2+2*A[1]**2+A[2]**2);
function eig(A){const tr=A[0]+A[2],det=A[0]*A[2]-A[1]*A[1],r=Math.sqrt(Math.max(tr*tr/4-det,0));return [tr/2+r,tr/2-r,Math.atan2(tr/2+r-A[0],A[1])]}
function ell(g,cx,cy,A,sc,st){const[l1,l2,ang]=eig(A);g.appendChild(E('ellipse',Object.assign({cx,cy,rx:2*Math.sqrt(Math.max(l1,1e-9))*sc,ry:2*Math.sqrt(Math.max(l2,1e-9))*sc,transform:`rotate(${ang*180/Math.PI} ${cx} ${cy})`,fill:'none'},st)))}
let W={};
function setup(n){seed=7+n;const pts=Array.from({length:n},neuron),S=mom(pts),rel=A=>fro([A[0]-S[0],A[1]-S[1],A[2]-S[2]])/fro(S);
const[,,a0]=eig(S),u=[Math.cos(a0),Math.sin(a0)],v=[-Math.sin(a0),Math.cos(a0)],dirs=[u,[-u[0],-u[1]],v,[-v[0],-v[1]],[(u[0]+v[0])/1.41,(u[1]+v[1])/1.41],[(u[0]-v[0])/1.41,(u[1]-v[1])/1.41]];
const sel=dirs.map(d=>{let b=0,bv=-1e9;pts.forEach((p,i)=>{const r=Math.hypot(...p),val=(p[0]*d[0]+p[1]*d[1])/(r+1e-9)*Math.min(r,1.6);if(val>bv){bv=val;b=i}});return b}),SP=sel.map(i=>pts[i]);let w=SP.map(()=>S[0]/2);
for(let it=0;it<20000;it++){const M=mom(SP,w),D=[M[0]-S[0],M[1]-S[1],M[2]-S[2]];w=w.map((wi,k)=>{const p=SP[k];return Math.max(0,wi-0.02*(D[0]*p[0]*p[0]+2*D[1]*p[0]*p[1]+D[2]*p[1]*p[1]))})}
const idx=[...Array(n).keys()],draw=q=>{for(let i=0;i<q;i++){const j=i+Math.floor(rnd()*(n-i));[idx[i],idx[j]]=[idx[j],idx[i]]}return idx.slice(0,q)};
const Q=[];for(let q=3;q<n;q=Math.max(q+1,Math.round(q*1.45)))Q.push(q);Q.push(n);
const stats=Q.map(q=>{const e=[];for(let r=0;r<120;r++)e.push(rel(mom(draw(q).map(i=>pts[i]))));e.sort((a,b)=>a-b);return [e[12],e[60],e[107]]});
const dd=[];for(let r=0;r<40;r++){const P=Array.from({length:n},neuron);dd.push(rel(mom(P)))}dd.sort((a,b)=>a-b);const dense=dd[20];
let qstar=n;for(let i=0;i<Q.length;i++)if(stats[i][1]<=dense){qstar=Q[i];break}
W={n,pts,S,rel,SP,w,selErr:Math.max(rel(mom(SP,w)),1e-6),Q,stats,dense,qstar,draw};document.getElementById('qq').max=Q.length-1}
function render(){const qi=Math.min(+document.getElementById('qq').value,W.Q.length-1),q=W.Q[qi],sc=24;s1.innerHTML='';document.getElementById('ql').textContent=q;
const sample=W.draw(q).map(i=>W.pts[i]),IM=mom(sample),cloud=(cx,cy,op)=>{const g=E('g',{});W.pts.forEach((p,i)=>{if(i%Math.ceil(W.n/600))return;g.appendChild(E('circle',{cx:(cx+p[0]*sc).toFixed(1),cy:(cy-p[1]*sc).toFixed(1),r:1.3,fill:GR,opacity:op}))});s1.appendChild(g);ell(s1,cx,cy,W.S,sc,{stroke:'var(--s)','stroke-width':1.1,'stroke-dasharray':'4 3'})};
[[115,'All n neurons'],[340,`${q} random neurons`],[565,'6 selected, weighted']].forEach(([x,t])=>s1.appendChild(E('text',{x,y:18,'text-anchor':'middle',class:'th'},t)));
cloud(115,125,0.55);cloud(340,125,0.3);cloud(565,125,0.3);
sample.slice(0,400).forEach(p=>s1.appendChild(E('circle',{cx:340+p[0]*sc,cy:125-p[1]*sc,r:q>100?1.8:3,fill:DK})));ell(s1,340,125,IM,sc,{stroke:DK,'stroke-width':2});
const wm=Math.max(...W.w);W.SP.forEach((p,j)=>{if(W.w[j]>1e-6){const r=3+6*Math.sqrt(W.w[j]/wm);s1.appendChild(E('circle',{cx:565+p[0]*sc,cy:125-p[1]*sc,r,fill:GN,opacity:0.85}))}});ell(s1,565,125,mom(W.SP,W.w),sc,{stroke:GN,'stroke-width':2});
s1.appendChild(E('text',{x:115,y:232,'text-anchor':'middle',class:'ts'},'dot: one neuron at (uᵢ, vᵢ), its entries'));s1.appendChild(E('text',{x:115,y:248,'text-anchor':'middle',class:'ts'},'in two source vectors u, v ∈ E'));
s1.appendChild(E('text',{x:115,y:264,'text-anchor':'middle',class:'ts'},'dashed: Gram ⟨u,v⟩ₙ, what must be kept'));
s1.appendChild(E('text',{x:340,y:232,'text-anchor':'middle',class:'ts'},`Gram error ${(100*W.rel(IM)).toFixed(1)}%`));s1.appendChild(E('text',{x:340,y:248,'text-anchor':'middle',class:'ts'},'equal weights 1/q'));
s1.appendChild(E('text',{x:565,y:232,'text-anchor':'middle',class:'ts'},`Gram error ${(100*W.selErr).toFixed(2)}%`));s1.appendChild(E('text',{x:565,y:248,'text-anchor':'middle',class:'ts'},'weights = the metric M'));
s2.innerHTML='';const X0=70,PW=520,Y0=24,PH=170,lx=v=>X0+PW*Math.log(v/3)/Math.log(W.n/3),ly=e=>Y0+PH*Math.min(1,-Math.log10(Math.max(e,1e-4))/4);
s2.appendChild(E('text',{x:40,y:14,class:'th'},'Gram error versus neurons kept'));
s2.appendChild(E('line',{x1:X0,y1:Y0+PH,x2:X0+PW,y2:Y0+PH,stroke:'var(--b)','stroke-width':0.5}));s2.appendChild(E('line',{x1:X0,y1:Y0,x2:X0,y2:Y0+PH,stroke:'var(--b)','stroke-width':0.5}));
const QQ=W.Q.slice(0,-1),ST=W.stats.slice(0,-1);
s2.appendChild(E('path',{d:'M'+QQ.map((q,i)=>lx(q).toFixed(1)+' '+ly(ST[i][2]).toFixed(1)).join('L')+'L'+QQ.slice().reverse().map((q,i)=>lx(q).toFixed(1)+' '+ly(ST[QQ.length-1-i][0]).toFixed(1)).join('L')+'Z',fill:GR,opacity:0.28,stroke:'none'}));
s2.appendChild(E('path',{d:'M'+QQ.map((q,i)=>lx(q).toFixed(1)+' '+ly(ST[i][1]).toFixed(1)).join('L'),fill:'none',stroke:DK,'stroke-width':2}));
s2.appendChild(E('line',{x1:X0,y1:ly(W.dense),x2:X0+PW,y2:ly(W.dense),stroke:'var(--s)','stroke-width':1,'stroke-dasharray':'5 3'}));
s2.appendChild(E('text',{x:X0+6,y:ly(W.dense)+16,class:'ts'},`as close as a second dense network of width ${W.n}`));
s2.appendChild(E('line',{x1:lx(W.qstar),y1:ly(W.dense),x2:lx(W.qstar),y2:Y0+PH,stroke:DK,'stroke-width':1,'stroke-dasharray':'2 2'}));
s2.appendChild(E('text',{x:lx(W.qstar)-6,y:ly(W.dense)+16,'text-anchor':'end',class:'ts'},`q* ≈ ${W.qstar}`));
s2.appendChild(E('line',{x1:lx(6),y1:Y0+PH-2,x2:X0+PW,y2:Y0+PH-2,stroke:GN,'stroke-width':3}));s2.appendChild(E('circle',{cx:lx(6),cy:Y0+PH-2,r:4,fill:GN}));
s2.appendChild(E('text',{x:lx(6)+8,y:Y0+PH-10,class:'ts'},'selected: exact from 6 neurons'));
s2.appendChild(E('circle',{cx:lx(q),cy:ly(W.stats[qi][1]),r:5,fill:DK}));
s2.appendChild(E('text',{x:lx(QQ[Math.floor(QQ.length*0.3)]),y:ly(ST[Math.floor(QQ.length*0.3)][2])-8,class:'ts'},'random neurons: ~ q^(−1/2)'));
[3,10,30,100,300,1000].filter(v=>v<W.n/1.7).concat([W.n]).forEach(v=>s2.appendChild(E('text',{x:lx(v),y:Y0+PH+16,'text-anchor':'middle',class:'ts'},v)));
[[1,'100%'],[0.1,'10%'],[0.01,'1%'],[0.001,'0.1%']].forEach(([v,l])=>s2.appendChild(E('text',{x:X0-6,y:ly(v)+4,'text-anchor':'end',class:'ts'},l)));
s2.appendChild(E('text',{x:X0+PW/2,y:Y0+PH+34,'text-anchor':'middle',class:'ts'},'neurons kept q (log scale)'));
document.getElementById('rdt').textContent=`Width ${W.n}: random neurons need about ${W.qstar} (${Math.round(100*W.qstar/W.n)}% of the layer) to be as close as a second dense network; double n and this doubles. Selected neurons: 6, exact, at every width.`}
document.getElementById('ns').onchange=e=>{setup(+e.target.value);document.getElementById('qq').value=Math.min(+document.getElementById('qq').value,W.Q.length-1);render()};
document.getElementById('qq').oninput=render;document.getElementById('rd').onclick=render;
setup(600);render();
})();
</script>