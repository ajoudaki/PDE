<h2 class="sr-only">Figure 8. Neurons as rotated petals share one Fourier spectrum and span about log n directions.</h2>
<div style="display:flex;align-items:center;gap:12px;margin:0 0 6px;font-size:13px;color:var(--text-secondary)">
<span>Width n</span>
<input type="range" id="ns" min="6" max="24" step="1" value="12" style="flex:1">
<span id="nl" style="min-width:250px;text-align:right"></span>
</div>
<svg id="hv" width="100%" viewBox="0 0 680 330" role="img"><title>Figure 8: rotated petals</title><desc>Petals, shared spectrum with cutoff J, and directions versus width.</desc></svg>
<script>
const NS='http://www.w3.org/2000/svg',svg=document.getElementById('hv');
const E=(n,a,t)=>{const e=document.createElementNS(NS,n);for(const k in a)e.setAttribute(k,a[k]);if(t!==undefined)e.textContent=t;return e};
const M=1024,cache={};
function spec(r){const key=r.toFixed(3);if(cache[key])return cache[key];const a=[];for(let j=0;j<=80;j++){let s=0;for(let k=0;k<M;k++){const th=2*Math.PI*k/M;s+=Math.tanh(r*Math.cos(th))*Math.cos(j*th)}a.push(Math.abs(2*s/M))}cache[key]=a;return a}
function Jneed(r,eps){const a=spec(r);let tail=0;for(let j=80;j>=0;j--){tail+=a[j];if(tail>eps)return j}return 0}
let seed=11;const rnd=()=>{seed=(seed*16807)%2147483647;return seed/2147483647};
const petals=[];for(let i=0;i<14;i++){const r=Math.sqrt(-2*Math.log(rnd()+1e-12));petals.push([r,2*Math.PI*rnd()])}
const curveNs=[];for(let p=4;p<=24;p++)curveNs.push(2**p);
const curve=curveNs.map(n=>{const rmax=Math.sqrt(2*Math.log(n));return [n,2*Jneed(rmax,1/n)+1]});
function draw(){const p=+document.getElementById('ns').value,n=2**p,eps=1/n,rmax=Math.sqrt(2*Math.log(n));
const J=Jneed(rmax,eps),dirs=2*J+1;
document.getElementById('nl').textContent=`n = ${n.toLocaleString()}  →  ${dirs} harmonic directions`;
svg.innerHTML='';
svg.appendChild(E('text',{x:110,y:24,'text-anchor':'middle',class:'th'},'Neurons: rotated petals'));
const cx=110,cy=150,R0=55,sc=30;
svg.appendChild(E('circle',{cx,cy,r:R0,fill:'none',stroke:'var(--b)','stroke-width':0.5,'stroke-dasharray':'3 3'}));
const all=petals.concat([[rmax,0.6]]);
all.forEach((q,i)=>{let d='';for(let k=0;k<=200;k++){const th=2*Math.PI*k/200,rr=R0+sc*Math.tanh(q[0]*Math.cos(th-q[1]));const x=cx+rr*Math.cos(th),y=cy-rr*Math.sin(th);d+=(k?'L':'M')+x.toFixed(1)+' '+y.toFixed(1)}
const last=i===all.length-1;svg.appendChild(E('path',{d,fill:'none',stroke:last?'#D85A30':'#1D9E75','stroke-width':last?2:0.9,opacity:last?1:0.55}))});
svg.appendChild(E('text',{x:110,y:262,'text-anchor':'middle',class:'ts'},'response tanh(⟨wᵢ, v⟩) around the circle'));
svg.appendChild(E('text',{x:110,y:280,'text-anchor':'middle',class:'ts'},'orange: sharpest of n, |w| ≈ √(2 ln n)'));
const X0=250,Y0=40,PW=190,PH=190,jmax=60,lmin=-10;
svg.appendChild(E('text',{x:X0+PW/2,y:24,'text-anchor':'middle',class:'th'},'One shared spectrum'));
svg.appendChild(E('line',{x1:X0,y1:Y0+PH,x2:X0+PW,y2:Y0+PH,stroke:'var(--b)','stroke-width':0.5}));
svg.appendChild(E('line',{x1:X0,y1:Y0,x2:X0,y2:Y0+PH,stroke:'var(--b)','stroke-width':0.5}));
const yv=v=>Y0+PH*(Math.max(Math.log10(v+1e-300),lmin)/lmin);const xv=j=>X0+PW*j/jmax;
[[1.0,'#1D9E75',0.9],[1.6,'#1D9E75',0.9],[rmax,'#D85A30',1.8]].forEach(([r,c,w])=>{const a=spec(r);let d='',first=true;for(let j=1;j<=jmax;j+=2){if(a[j]<1e-10)continue;d+=(first?'M':'L')+xv(j).toFixed(1)+' '+yv(a[j]).toFixed(1);first=false}svg.appendChild(E('path',{d,fill:'none',stroke:c,'stroke-width':w}))});
svg.appendChild(E('line',{x1:X0,y1:yv(eps),x2:X0+PW,y2:yv(eps),stroke:'#5F5E5A','stroke-width':0.8,'stroke-dasharray':'4 3'}));
svg.appendChild(E('text',{x:X0+PW-2,y:yv(eps)-5,'text-anchor':'end',class:'ts'},'accuracy 1/n'));
svg.appendChild(E('line',{x1:xv(J),y1:Y0,x2:xv(J),y2:Y0+PH,stroke:'#D85A30','stroke-width':0.8,'stroke-dasharray':'2 3'}));
svg.appendChild(E('text',{x:Math.min(xv(J)+4,X0+PW-30),y:Y0+12,class:'ts'},`J = ${J}`));
svg.appendChild(E('text',{x:X0+PW/2,y:Y0+PH+18,'text-anchor':'middle',class:'ts'},'frequency j'));
svg.appendChild(E('text',{x:X0+PW/2,y:262,'text-anchor':'middle',class:'ts'},'rotation shifts phase, never degree:'));
svg.appendChild(E('text',{x:X0+PW/2,y:280,'text-anchor':'middle',class:'ts'},'all petals use modes j ≤ J'));
const A0=480,B0=40,AW=180,AH=190;
svg.appendChild(E('text',{x:A0+AW/2,y:24,'text-anchor':'middle',class:'th'},'Directions vs width'));
svg.appendChild(E('line',{x1:A0,y1:B0+AH,x2:A0+AW,y2:B0+AH,stroke:'var(--b)','stroke-width':0.5}));
svg.appendChild(E('line',{x1:A0,y1:B0,x2:A0,y2:B0+AH,stroke:'var(--b)','stroke-width':0.5}));
const lx=n=>A0+AW*(Math.log10(n)-1)/(Math.log10(2**24)-1),ly=v=>B0+AH*(1-(Math.log10(v))/(Math.log10(2**24)));
let dn='';curveNs.forEach((n,i)=>{dn+=(i?'L':'M')+lx(n).toFixed(1)+' '+ly(n).toFixed(1)});svg.appendChild(E('path',{d:dn,fill:'none',stroke:'#5F5E5A','stroke-width':1,'stroke-dasharray':'4 3'}));
svg.appendChild(E('text',{x:lx(2**18),y:ly(2**18)-8,'text-anchor':'end',class:'ts'},'n neurons'));
let dc='';curve.forEach(([n,v],i)=>{dc+=(i?'L':'M')+lx(n).toFixed(1)+' '+ly(v).toFixed(1)});svg.appendChild(E('path',{d:dc,fill:'none',stroke:'#1D9E75','stroke-width':2}));
svg.appendChild(E('circle',{cx:lx(n),cy:ly(dirs),r:5,fill:'#D85A30'}));
svg.appendChild(E('text',{x:lx(2**20),y:ly(curve[curve.length-1][1])-10,'text-anchor':'end',class:'ts'},'2J+1 ~ polylog n'));
svg.appendChild(E('text',{x:A0+AW/2,y:B0+AH+18,'text-anchor':'middle',class:'ts'},'width n (log scale)'));
svg.appendChild(E('text',{x:A0+AW/2,y:262,'text-anchor':'middle',class:'ts'},'infinitely many inputs × n neurons'));
svg.appendChild(E('text',{x:A0+AW/2,y:280,'text-anchor':'middle',class:'ts'},'live in 2J+1 fixed directions'));
svg.appendChild(E('text',{x:340,y:316,'text-anchor':'middle',class:'ts'},'adding time multiplies modes by a Chebyshev degree; on the sphere, degrees become spherical harmonics'));
}
document.getElementById('ns').oninput=draw;draw();
</script>