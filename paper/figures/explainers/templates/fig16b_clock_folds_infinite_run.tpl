<h2 class="sr-only">Figure 16b. The activity clock is the area under the residual activity; an infinite training run maps to a finite clock interval, where the backward history and its Legendre moments settle and freeze.</h2>
<div style="font-size:15px;font-weight:500;color:var(--text-primary);margin:0 0 8px">Figure 16b · The clock folds an infinite run into a finite interval</div>
<div style="display:flex;align-items:center;gap:10px;margin:0 0 6px;font-size:13px;color:var(--text-secondary)">
<button id="pp" style="font-size:13px;padding:4px 10px">Pause</button>
<button id="rs" style="font-size:13px;padding:4px 10px">Restart</button>
<span>Moments q</span><input type="range" id="qs" min="1" max="8" step="1" value="5" style="flex:1">
<span id="ql" style="min-width:230px;text-align:right"></span>
</div>
<svg id="sv" width="100%" viewBox="0 0 680 420" role="img"><title>Figure 16b: the clock folds an infinite run into a finite interval</title><desc>Top: residual activity over real time with the area so far. Middle: threads mapping real times to clock times, converging at a finite end. Bottom: the backward history on the clock with its moment fit. Right: the moments, which stop changing.</desc></svg>
<script>
(()=>{
const D=__DATA__;
const svg=document.getElementById('sv'),BL='#2a78d6',BD='#185FA5',PU='#7F77DD',PD='#534AB7',GR='#888780';
const E=(n,a,t)=>{const e=document.createElementNS('http://www.w3.org/2000/svg',n);for(const k in a)e.setAttribute(k,a[k]);if(t!==undefined)e.textContent=t;return e};
const T32=32,r32=D.rho[D.rho.length-1],t32=D.tauEnd,TI=t32+r32/D.kap;
const lin=(xs,ys,x)=>{const n=xs.length;if(x<=xs[0])return ys[0];if(x>=xs[n-1])return ys[n-1];let i=Math.floor((x-xs[0])/(xs[1]-xs[0]));i=Math.min(n-2,Math.max(0,i));const w=(x-xs[i])/(xs[i+1]-xs[i]);return ys[i]*(1-w)+ys[i+1]*w};
const rho=t=>t<=T32?lin(D.t,D.rho,t):r32*Math.exp(-D.kap*(t-T32));
const tau=t=>t<=T32?lin(D.t,D.tau,t):t32+r32/D.kap*(1-Math.exp(-D.kap*(t-T32)));
const bg=D.bt.map((_,k)=>t32*k/(D.bt.length-1)),bval=s=>s<=t32?lin(bg,D.bt,s):D.bt[D.bt.length-1];
const bmn=Math.min(...D.bt),bmx=Math.max(...D.bt);
const X0=40,XW=440,xt=t=>X0+XW*Math.min(t,64)/64,xs=s=>X0+XW*s/TI;
const leg=(x,q)=>{const P=[1,x];for(let j=1;j<q;j++)P.push(((2*j+1)*x*P[j]-j*P[j-1])/(j+1));return P};
function moments(s,Q){const M=500,c=Array(Q).fill(0);for(let k=0;k<=M;k++){const u=s*k/M,w=(k===0||k===M?0.5:1)*s/M,P=leg(2*u/s-1,Q),v=bval(u);for(let j=0;j<Q;j++)c[j]+=w*P[j]*v}return c.map((v,j)=>(2*j+1)/s*v)}
let t=0,run=true,last=null;const CREF=Math.max(...[2,3,4,5,6,7,8.5].map(u=>Math.max(...moments(u,8).map(Math.abs))));
function draw(){const q=+document.getElementById('qs').value,s=tau(t);svg.innerHTML='';
svg.appendChild(E('text',{x:X0,y:20,class:'th'},'Real time: residual activity ρ(t)'));
const ry=v=>112-70*v,top=[];let ar=`M${xt(0)} ${ry(0)}`;
for(let k=0;k<=256;k++){const u=64*k/256;top.push([xt(u),ry(rho(u))]);if(u<=t)ar+=`L${xt(u).toFixed(1)} ${ry(rho(u)).toFixed(1)}`}
ar+=`L${xt(Math.min(t,64)).toFixed(1)} ${ry(rho(Math.min(t,64))).toFixed(1)}L${xt(Math.min(t,64)).toFixed(1)} ${ry(0)}Z`;
svg.appendChild(E('path',{d:ar,fill:BL,opacity:0.22,stroke:'none'}));
let d1='',d2='';top.forEach((p,k)=>{const u=64*k/256,str=(k?'L':'M')+p[0].toFixed(1)+' '+p[1].toFixed(1);if(u<=T32)d1+=str;if(u>=T32)d2+=(d2?'L':'M')+p[0].toFixed(1)+' '+p[1].toFixed(1)});
svg.appendChild(E('path',{d:d1,fill:'none',stroke:BD,'stroke-width':1.6}));svg.appendChild(E('path',{d:d2,fill:'none',stroke:BD,'stroke-width':1.2,'stroke-dasharray':'3 3'}));
svg.appendChild(E('line',{x1:X0,y1:ry(0),x2:X0+XW+24,y2:ry(0),stroke:'var(--s)','stroke-width':0.8}));
svg.appendChild(E('text',{x:X0+XW+30,y:ry(0)+4,class:'ts'},'∞'));
[0,16,32,48,64].forEach(u=>svg.appendChild(E('text',{x:xt(u),y:ry(0)+14,'text-anchor':'middle',class:'ts'},u)));svg.appendChild(E('text',{x:X0+XW+30,y:ry(0)+14,class:'ts'},'t'));
svg.appendChild(E('text',{x:xt(36),y:ry(rho(36))-10,class:'ts'},'fitted tail'));
const tx=t<=64?xt(t):X0+XW+20;svg.appendChild(E('circle',{cx:tx,cy:ry(0),r:4.5,fill:'var(--p)'}));
const yA=130,yB=232;
for(let u=0;u<=64;u+=2){const s2=tau(u);svg.appendChild(E('line',{x1:xt(u),y1:yA,x2:xs(s2),y2:yB,stroke:GR,'stroke-width':0.6,opacity:u%16===0?0.9:0.35}))}
[80,100,130,170,240].forEach(u=>svg.appendChild(E('line',{x1:X0+XW+8+(u-80)/12,y1:yA,x2:xs(tau(u)),y2:yB,stroke:GR,'stroke-width':0.6,opacity:0.35})));
svg.appendChild(E('line',{x1:tx,y1:yA,x2:xs(s),y2:yB,stroke:'var(--p)','stroke-width':1.4}));
svg.appendChild(E('text',{x:528,y:156,class:'ts'},'every later time'));svg.appendChild(E('text',{x:528,y:172,class:'ts'},'lands before τ∞'));
const by=v=>372-86*(v-bmn)/(bmx-bmn),cy0=yB;
svg.appendChild(E('line',{x1:X0,y1:cy0,x2:xs(TI),y2:cy0,stroke:'var(--s)','stroke-width':0.8}));
svg.appendChild(E('rect',{x:xs(1),y:cy0-3,width:Math.max(0,xs(s)-xs(1)),height:6,fill:BL,opacity:0.35}));
svg.appendChild(E('line',{x1:xs(TI),y1:cy0-8,x2:xs(TI),y2:cy0+8,stroke:'var(--p)','stroke-width':1.5}));
svg.appendChild(E('text',{x:xs(TI)+6,y:cy0+4,class:'ts'},'τ∞ = '+TI.toFixed(2)));
svg.appendChild(E('text',{x:xs(0),y:cy0+18,'text-anchor':'middle',class:'ts'},'0'));svg.appendChild(E('text',{x:xs(1),y:cy0+18,'text-anchor':'middle',class:'ts'},'1'));svg.appendChild(E('text',{x:xs(1)+8,y:cy0+18,class:'ts'},'clock τ: blue length = blue area above'));
let dp='',df='';for(let k=0;k<=300;k++){const u=TI*k/300,v=bval(u),str=(u<=s?(dp?'L':'M'):(df?'L':'M'))+xs(u).toFixed(1)+' '+by(v).toFixed(1);if(u<=s)dp+=str;else df+=str}
svg.appendChild(E('path',{d:dp,fill:'none',stroke:PU,'stroke-width':1.6}));if(df)svg.appendChild(E('path',{d:df,fill:'none',stroke:PU,'stroke-width':1,opacity:0.3}));
const c=moments(Math.max(s,1e-3),8);let dfit='';for(let k=0;k<=200;k++){const u=s*k/200,P=leg(2*u/s-1,q);let v=0;for(let j=0;j<q;j++)v+=c[j]*P[j];dfit+=(k?'L':'M')+xs(u).toFixed(1)+' '+by(v).toFixed(1)}
svg.appendChild(E('path',{d:dfit,fill:'none',stroke:PD,'stroke-width':2,'stroke-dasharray':'5 3'}));
svg.appendChild(E('circle',{cx:xs(s),cy:by(bval(s)),r:4.5,fill:'var(--p)'}));
svg.appendChild(E('text',{x:X0,y:270,class:'th'},'On the clock: backward history bᵢ, q-moment memory'));
const MX=566,MY=282;svg.appendChild(E('text',{x:MX-40,y:MY-12,class:'th'},'Moments now'));
const cm=CREF;c.forEach((v,j)=>{const w=Math.min(84,70*Math.abs(v)/cm),kept=j<q;svg.appendChild(E('rect',{x:v>=0?MX+20:MX+20-w,y:MY+j*16,width:Math.max(w,0.5),height:11,rx:2,fill:PU,opacity:kept?0.9:0.25}));svg.appendChild(E('text',{x:MX-40,y:MY+j*16+10,class:'ts'},'k='+j))});
svg.appendChild(E('line',{x1:MX+20,y1:MY-4,x2:MX+20,y2:MY+8*16,stroke:'var(--b)','stroke-width':0.5}));
document.getElementById('ql').textContent=`t = ${t<1000?t.toFixed(1):'∞'} → τ = ${s.toFixed(2)} of ${TI.toFixed(2)}`}
function frame(ts){if(last===null)last=ts;const dt=Math.min(0.05,(ts-last)/1000);last=ts;if(run){t+=dt*(1.2+t/3);if(t>400){t=400;run=false;document.getElementById('pp').textContent='Play'}}draw();requestAnimationFrame(frame)}
document.getElementById('pp').onclick=e=>{if(!run&&t>=400)t=0;run=!run;e.target.textContent=run?'Pause':'Play'};
document.getElementById('rs').onclick=()=>{t=0;run=true;document.getElementById('pp').textContent='Pause'};
document.getElementById('qs').oninput=draw;requestAnimationFrame(frame);
})();
</script>