<h2 class="sr-only">Figure 5. Neurons as rotated caps on the sphere, degree-L truncation, and harmonic directions by input dimension.</h2>
<div style="display:flex;align-items:center;gap:12px;margin:0 0 6px;font-size:13px;color:var(--text-secondary)">
<span>Max degree L</span><input type="range" id="L" min="0" max="14" step="1" value="3" style="flex:1"><span id="Ll" style="min-width:230px;text-align:right"></span>
</div>
<div style="font-size:13px;color:var(--text-secondary);margin:4px 0 2px">Five neurons: one cap, rotated</div>
<div id="row1" style="display:flex;gap:10px;flex-wrap:wrap"></div>
<div style="font-size:13px;color:var(--text-secondary);margin:10px 0 2px">One neuron: exact, degree ≤ L, and error ×10</div>
<div id="row2" style="display:flex;gap:10px;flex-wrap:wrap"></div>
<svg id="dimbar" width="100%" viewBox="0 0 680 150" role="img" style="margin-top:8px"><title>Figure 5: harmonic directions by dimension</title><desc>Number of spherical harmonics of degree at most L for d equals 2, 3, 5, 10.</desc></svg>
<script>
const r=2.6,S=104;
const legA=(()=>{const M=4001,dt=2/(M-1),ts=Array.from({length:M},(_,k)=>-1+k*dt),f=ts.map(t=>Math.tanh(r*t));let P0=ts.map(()=>1),P1=ts.slice();const a=[];
const c=(P,l)=>{let s=0;for(let k=0;k<M;k++)s+=(k===0||k===M-1?0.5:1)*f[k]*P[k];return (2*l+1)/2*s*dt};a.push(c(P0,0),c(P1,1));
for(let l=1;l<16;l++){const P2=ts.map((t,k)=>((2*l+1)*t*P1[k]-l*P0[k])/(l+1));P0=P1;P1=P2;a.push(c(P1,l+1))}return a})();
const trunc=(t,L)=>{let p0=1,p1=t,s=legA[0];if(L>=1)s+=legA[1]*t;for(let l=1;l<L;l++){const p2=((2*l+1)*t*p1-l*p0)/(l+1);p0=p1;p1=p2;s+=legA[l+1]*p2}return s};
const col=(v,z)=>{const a=Math.max(-1,Math.min(1,v)),m=Math.abs(a),base=[232,230,223],c=a>=0?[216,90,48]:[29,158,117],sh=0.62+0.38*z;return base.map((b,i)=>Math.round((b+(c[i]-b)*m)*sh))};
function sphere(fn,dir){const cv=document.createElement('canvas');cv.width=S;cv.height=S;cv.style.width=S+'px';cv.style.height=S+'px';const ctx=cv.getContext('2d'),img=ctx.createImageData(S,S);
const n=Math.hypot(...dir),d=dir.map(x=>x/n);
for(let j=0;j<S;j++)for(let i=0;i<S;i++){const u=2*(i+0.5)/S-1,v=1-2*(j+0.5)/S,q=u*u+v*v,k=4*(j*S+i);if(q>1){img.data[k+3]=0;continue}const z=Math.sqrt(1-q),t=u*d[0]+v*d[1]+z*d[2];const c=col(fn(t),z);img.data[k]=c[0];img.data[k+1]=c[1];img.data[k+2]=c[2];img.data[k+3]=255}
ctx.putImageData(img,0,0);return cv}
const dirs=[[0.6,0.4,0.7],[-0.7,0.3,0.6],[0.1,-0.8,0.6],[-0.4,-0.5,0.75],[0.8,-0.2,0.55]];
const row1=document.getElementById('row1');dirs.forEach(d=>row1.appendChild(sphere(t=>Math.tanh(r*t),d)));
const NS='http://www.w3.org/2000/svg',bar=document.getElementById('dimbar');const E=(n,a,t)=>{const e=document.createElementNS(NS,n);for(const k in a)e.setAttribute(k,a[k]);if(t!==undefined)e.textContent=t;return e};
const binom=(n,k)=>{if(k<0||k>n)return 0;let s=1;for(let i=1;i<=k;i++)s=s*(n-k+i)/i;return s};
const Nd=(d,L)=>binom(L+d-1,d-1)+binom(L+d-2,d-1);
function draw(){const L=+document.getElementById('L').value;const row2=document.getElementById('row2');row2.innerHTML='';
const D=[0.6,0.4,0.7];row2.appendChild(sphere(t=>Math.tanh(r*t),D));row2.appendChild(sphere(t=>trunc(t,L),D));row2.appendChild(sphere(t=>10*(trunc(t,L)-Math.tanh(r*t)),D));
let mx=0;for(let k=0;k<=400;k++){const t=-1+k/200;mx=Math.max(mx,Math.abs(trunc(t,L)-Math.tanh(r*t)))}
document.getElementById('Ll').textContent=`L = ${L}: max error ${mx.toExponential(1)}`;
bar.innerHTML='';bar.appendChild(E('text',{x:40,y:18,class:'th'},`Harmonic directions with degree ≤ ${L}`));
const ds=[2,3,5,10],lmax=Math.log10(Nd(10,14))+0.2;ds.forEach((d,i)=>{const v=Nd(d,L),w=Math.max(4,500*Math.log10(Math.max(v,1))/lmax),y=34+i*27;
bar.appendChild(E('text',{x:40,y:y+13,class:'ts'},`d = ${d}`));bar.appendChild(E('rect',{x:100,y,width:w,height:18,rx:3,fill:d===3?'#1D9E75':'#9FE1CB'}));bar.appendChild(E('text',{x:108+w,y:y+13,class:'ts'},Math.round(v).toLocaleString()))});}
document.getElementById('L').oninput=draw;draw();
</script>