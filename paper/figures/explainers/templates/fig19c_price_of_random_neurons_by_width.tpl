<h2 class="sr-only">Figure 19c. Each dot is one of the 1,024 layer-2 neurons of a trained network, placed at its forward value and backward response for one training input, and the cloud moves as training time plays. Left: q neurons drawn at random. Right: q neurons selected once by the Logarithmic rule; they stay spread across the cloud, and with their metric they reproduce the pairings on the source space exactly.</h2>
<div style="font-size:15px;font-weight:500;color:var(--text-primary);margin:0 0 8px">Figure 19c · Random versus selected neurons</div>
<div style="display:flex;align-items:center;gap:10px;margin:0 0 6px;font-size:13px;color:var(--text-secondary)">
<button id="pp" style="font-size:13px;padding:4px 10px;min-width:62px">Pause</button>
<span>Training time</span><input type="range" id="ts" min="0" max="1000" step="1" value="0" style="flex:1"><span id="tl" style="min-width:58px;text-align:right"></span>
</div>
<div style="display:flex;align-items:center;gap:10px;margin:0 0 6px;font-size:13px;color:var(--text-secondary)">
<span>Neurons shown q</span><input type="range" id="qs" min="4" max="128" step="1" value="32" style="flex:1"><span id="ql" style="min-width:28px;text-align:right"></span>
<button id="rd" style="font-size:13px;padding:4px 10px">Draw again</button>
</div>
<svg id="sv" width="100%" viewBox="0 0 680 408" role="img"><title>Figure 19c: random versus selected neurons</title><desc>Two copies of the cloud of all layer-2 neurons in the plane of forward value and backward response, moving with training time; one highlights q random neurons, the other q neurons chosen by the Logarithmic selection.</desc></svg>
<script>
(()=>{
const D=__DATA__;
const svg=document.getElementById('sv'),GN='#1baf7a',GR='#888780',NS='http://www.w3.org/2000/svg';
const E=(n,a,t)=>{const e=document.createElementNS(NS,n);for(const k in a)e.setAttribute(k,a[k]);if(t!==undefined)e.textContent=t;return e};
const dec=s=>Uint8Array.from(atob(s),c=>c.charCodeAt(0)),HB=dec(D.h),DB=dec(D.d),n=D.n,F=D.t.length;
let seed=11;const rnd=()=>{seed=(seed*16807)%2147483647;return seed/2147483647};
const perm=()=>{const p=[...Array(n).keys()];for(let i=n-1;i>0;i--){const j=Math.floor(rnd()*(i+1));[p[i],p[j]]=[p[j],p[i]]}return p};
let iid=perm(),s=Math.round(0.55*(F-1)),run=true,last=null,hold=0;
const W=290,Hh=250,Y0=58,PX=[40,370];
const panels=PX.map((x0,k)=>{const g=E('g',{});svg.appendChild(g);
g.appendChild(E('rect',{x:x0,y:Y0,width:W,height:Hh,fill:'none',stroke:'var(--b)','stroke-width':0.5}));
g.appendChild(E('line',{x1:x0,y1:Y0+Hh/2,x2:x0+W,y2:Y0+Hh/2,stroke:'var(--b)','stroke-width':0.6,'stroke-dasharray':'3 3'}));
g.appendChild(E('line',{x1:x0+W/2,y1:Y0,x2:x0+W/2,y2:Y0+Hh,stroke:'var(--b)','stroke-width':0.6,'stroke-dasharray':'3 3'}));
[[-1,x0],[0,x0+W/2],[1,x0+W]].forEach(([v,x])=>g.appendChild(E('text',{x,y:Y0+Hh+14,'text-anchor':'middle',class:'ts'},v)));
g.appendChild(E('text',{x:x0+W/2,y:Y0+Hh+30,'text-anchor':'middle',class:'ts'},'forward hᵢ'));
const yl=E('text',{x:x0-8,y:Y0+Hh/2,'text-anchor':'middle',class:'ts',transform:`rotate(-90 ${x0-8} ${Y0+Hh/2})`},'backward δᵢ');g.appendChild(yl);
const cloud=E('path',{fill:'none',stroke:GR,'stroke-width':3,'stroke-linecap':'round',opacity:0.35});g.appendChild(cloud);
const dots=E('path',{fill:'none',stroke:k?GN:'var(--p)','stroke-width':7.5,'stroke-linecap':'round'});g.appendChild(dots);
const title=E('text',{x:x0,y:Y0-10,class:'th'});g.appendChild(title);
const ymax=E('text',{x:x0+4,y:Y0+12,class:'ts'});g.appendChild(ymax);
const read=E('text',{x:x0,y:Y0+Hh+48,class:'ts'});g.appendChild(read);
return {x0,cloud,dots,title,ymax,read}});
svg.appendChild(E('text',{x:40,y:384,class:'ts'},`Each dot: one of the ${n.toLocaleString()} layer-2 neurons at training input ${D.input+1}; δᵢ = wᵢ tanh′(zᵢ), rescaled each frame.`));
svg.appendChild(E('text',{x:40,y:401,class:'ts'},`Chosen once for the whole run by pivoted QR on E, the span of these fields over time (dim ${D.dimE}).`));
function frame(s){const f0=Math.min(F-2,Math.floor(s)),w=s-f0,o0=f0*n,o1=o0+n,h=new Float64Array(n),dn=new Float64Array(n);
for(let i=0;i<n;i++){h[i]=(HB[o0+i]*(1-w)+HB[o1+i]*w)/127.5-1;dn[i]=(DB[o0+i]*(1-w)+DB[o1+i]*w)/127.5-1}
return {h,dn,dm:D.dmax[f0]*(1-w)+D.dmax[f0+1]*w,t:D.t[f0]*(1-w)+D.t[f0+1]*w}}
function gram(fr,S,wt){let a=0,b=0,c=0;for(const i of S){const x=fr.h[i],y=fr.dn[i]*fr.dm;a+=x*x;b+=x*y;c+=y*y}return [a*wt,b*wt,c*wt]}
function draw(){const q=+document.getElementById('qs').value,fr=frame(s),all=[...Array(n).keys()];
document.getElementById('ql').textContent=q;document.getElementById('tl').textContent='t = '+fr.t.toFixed(1);
document.getElementById('ts').value=Math.round(1000*s/(F-1));
const sets=[iid.slice(0,q),D.order.slice(0,q)],G=gram(fr,all,1/n),gn=Math.hypot(G[0],Math.SQRT2*G[1],G[2]);
panels.forEach((P,k)=>{const X=i=>(P.x0+(fr.h[i]+1)/2*W).toFixed(1),Y=i=>(Y0+Hh/2-fr.dn[i]*Hh/2*0.94).toFixed(1);
let c='';for(let i=0;i<n;i++)c+=`M${X(i)} ${Y(i)}h0`;P.cloud.setAttribute('d',c);
let d='';sets[k].forEach(i=>{d+=`M${X(i)} ${Y(i)}h0`});P.dots.setAttribute('d',d);
P.title.textContent=k?`${q} selected neurons (Logarithmic)`:`${q} random neurons`;P.ymax.textContent='±'+fr.dm.toPrecision(2);
if(k===0){const g=gram(fr,sets[0],1/q),e=Math.hypot(g[0]-G[0],Math.SQRT2*(g[1]-G[1]),g[2]-G[2])/gn;P.read.textContent=`pairing error ${(100*e).toFixed(1)}% now, equal weights 1/q`}
else P.read.textContent=q>=D.dimE?`pairing error ≤ ${(100*D.selErr[q-D.dimE]).toFixed(2)}% at all times, with metric M`:`q below dim E = ${D.dimE}: no exact metric yet`})}
function tick(ts){if(last===null)last=ts;const dt=Math.min(0.05,(ts-last)/1000);last=ts;
if(run){if(s>=F-1){hold+=dt;if(hold>1.5){s=0;hold=0}}else s=Math.min(F-1,s+dt*(F-1)/14);draw()}requestAnimationFrame(tick)}
const pp=document.getElementById('pp');pp.onclick=()=>{run=!run;pp.textContent=run?'Pause':'Play'};
document.getElementById('ts').oninput=e=>{run=false;pp.textContent='Play';s=(F-1)*e.target.value/1000;draw()};
document.getElementById('qs').oninput=draw;document.getElementById('rd').onclick=()=>{iid=perm();draw()};
draw();requestAnimationFrame(tick);
})();
</script>
