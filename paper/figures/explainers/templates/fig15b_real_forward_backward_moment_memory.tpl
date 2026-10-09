<h2 class="sr-only">Figure 15b. Real forward and backward histories of one weight entry of a trained network, their q-moment memory up to now, a short continuation, and the weight written so far.</h2>
<div style="font-size:15px;font-weight:500;color:var(--text-primary);margin:0 0 8px">Figure 15b · The trail fades, the moments remember (real histories)</div>
<div style="display:flex;align-items:center;gap:10px;margin:0 0 6px;font-size:13px;color:var(--text-secondary)">
<button id="pp" style="font-size:13px;padding:4px 10px">Play</button>
<span>Now τ</span><input type="range" id="ts" min="1.3" max="7.85" step="0.01" value="5.5" style="flex:1">
<span>Moments q</span><input type="range" id="qs" min="1" max="10" step="1" value="5" style="flex:1">
<span id="ql" style="min-width:120px;text-align:right"></span>
</div>
<svg id="sv" width="100%" viewBox="0 0 680 470" role="img"><title>Figure 15b: real histories and their moment memory</title><desc>Phase plane of forward and backward histories with fading trail, moment fit, continuation and arms; time series of both histories; the weight entry written so far and its moment reconstruction; stored moment pairs.</desc>
<defs><clipPath id="c15a"><rect x="40" y="40" width="300" height="260"/></clipPath><clipPath id="c15b"><rect x="390" y="36" width="270" height="118"/></clipPath><clipPath id="c15c"><rect x="390" y="190" width="270" height="112"/></clipPath></defs>
<g id="g1" clip-path="url(#c15a)"></g><g id="g2" clip-path="url(#c15b)"></g><g id="g3" clip-path="url(#c15c)"></g><g id="g4"></g></svg>
<script>
(()=>{
const D=__DATA__;
const BL='#2a78d6',BD='#185FA5',PU='#7F77DD',PD='#534AB7',GR='#888780',Q=10,NG=D.tau.length;
const at=(arr,s)=>{const f=s/D.tauEnd*(NG-1),i=Math.max(0,Math.min(NG-2,Math.floor(f))),w=f-i;return arr[i]*(1-w)+arr[i+1]*w};
const leg=(x,q)=>{const P=[1,x];for(let j=1;j<q;j++)P.push(((2*j+1)*x*P[j]-j*P[j-1])/(j+1));return P.slice(0,Math.max(q,1))};
function moments(s){const M=600,cx=Array(Q).fill(0),cy=Array(Q).fill(0);for(let k=0;k<=M;k++){const u=s*k/M,w=(k===0||k===M?0.5:1)*s/M,P=leg(2*u/s-1,Q),xv=at(D.x,u),yv=at(D.y,u);for(let j=0;j<Q;j++){cx[j]+=w*P[j]*xv;cy[j]+=w*P[j]*yv}}
return cx.map((v,j)=>[(2*j+1)/s*v,(2*j+1)/s*cy[j]])}
const ev=(c,q,s,u)=>{const P=leg(2*u/s-1,q);let a=0,b=0;for(let j=0;j<q;j++){a+=c[j][0]*P[j];b+=c[j][1]*P[j]}return [a,b]};
const xmn=Math.min(...D.x),xmx=Math.max(...D.x),ymn=Math.min(...D.y),ymx=Math.max(...D.y);
const px=v=>50+280*(v-xmn)/(xmx-xmn),py=v=>285-230*(v-ymn)/(ymx-ymn);
const tx=s=>395+260*s/D.tauEnd,nx=v=>(v-xmn)/(xmx-xmn),ny=v=>(v-ymn)/(ymx-ymn),hy=v=>140-95*v;
const Wm=Math.max(...D.W.map(Math.abs),...D.Wq.flat().map(Math.abs)),wy=v=>246-50*v/Wm;
let now=+document.getElementById('ts').value,run=false,psi=0,last=null,cache={s:-1};
const seg=(pts,attr)=>{let d='';pts.forEach((p,k)=>{d+=(k?'L':'M')+p[0].toFixed(1)+' '+p[1].toFixed(1)});return `<path d="${d}" fill="none" ${attr}/>`};
function draw(){const q=+document.getElementById('qs').value;if(Math.abs(cache.s-now)>1e-9){cache={s:now,c:moments(now)}}const c=cache.c,s=now,fut=Math.min(D.tauEnd*1.04,s*1.3);
let a='';
const past=[];for(let k=0;k<=160;k++){const u=s*k/160;past.push([px(at(D.x,u)),py(at(D.y,u)),u])}
for(let k=0;k<160;k++){const op=0.12+0.65*Math.exp(-(s-past[k+1][2])/1.8);a+=`<line x1="${past[k][0].toFixed(1)}" y1="${past[k][1].toFixed(1)}" x2="${past[k+1][0].toFixed(1)}" y2="${past[k+1][1].toFixed(1)}" stroke="${GR}" stroke-width="2.4" stroke-linecap="round" opacity="${op.toFixed(3)}"/>`}
const fu=[];for(let k=0;k<=80;k++){const u=s+(D.tauEnd-s)*k/80;fu.push([px(at(D.x,u)),py(at(D.y,u))])}a+=seg(fu,`stroke="${GR}" stroke-width="1" stroke-dasharray="1 3" opacity="0.8"`);
if(q>1){const fit=[];for(let k=0;k<=200;k++){const p=ev(c,q,s,s*k/200);fit.push([px(p[0]),py(p[1])])}a+=seg(fit,`stroke="${BL}" stroke-width="2" stroke-dasharray="6 4"`);
const co=[];for(let k=0;k<=60;k++){const p=ev(c,q,s,s+(fut-s)*k/60);co.push([px(p[0]),py(p[1])])}a+=seg(co,`stroke="${BL}" stroke-width="1.6" stroke-dasharray="2 3" opacity="0.6"`)}
a+=`<circle cx="${px(c[0][0]).toFixed(1)}" cy="${py(c[0][1]).toFixed(1)}" r="4" fill="none" stroke="${BD}" stroke-width="1.6"/>`;
const xp=-Math.cos(psi),P=leg(xp,q);let ox=c[0][0],oy=c[0][1];for(let j=1;j<q;j++){const nx2=ox+c[j][0]*P[j],ny2=oy+c[j][1]*P[j],op=Math.max(0.35,1-0.09*j);
a+=`<line x1="${px(ox).toFixed(1)}" y1="${py(oy).toFixed(1)}" x2="${px(nx2).toFixed(1)}" y2="${py(ny2).toFixed(1)}" stroke="${BD}" stroke-width="${Math.max(1,2.8-0.25*j)}" stroke-linecap="round" opacity="${op}"/><circle cx="${px(nx2).toFixed(1)}" cy="${py(ny2).toFixed(1)}" r="2" fill="${BD}" opacity="${op}"/>`;ox=nx2;oy=ny2}
if(q>1)a+=`<circle cx="${px(ox).toFixed(1)}" cy="${py(oy).toFixed(1)}" r="5" fill="none" stroke="${BD}" stroke-width="1.4"/>`;
a+=`<circle cx="${px(at(D.x,s)).toFixed(1)}" cy="${py(at(D.y,s)).toFixed(1)}" r="4.5" fill="var(--p)"/>`;
document.getElementById('g1').innerHTML=a;
let b=`<line x1="${tx(s)}" y1="36" x2="${tx(s)}" y2="154" stroke="${GR}" stroke-width="0.8" stroke-dasharray="2 3"/>`;
[[D.x,nx,BL,0],[D.y,ny,PU,1]].forEach(([arr,nm,col,ci])=>{const pa=[],pf=[];for(let k=0;k<=240;k++){const u=D.tauEnd*k/240;(u<=s?pa:pf).push([tx(u),hy(nm(at(arr,u)))])}
b+=seg(pa,`stroke="${col}" stroke-width="1.2"`)+seg(pf,`stroke="${col}" stroke-width="1" opacity="0.35"`);
if(q>0){const fi=[],co=[];for(let k=0;k<=120;k++){const u=s*k/120;fi.push([tx(u),hy(nm(ev(c,q,s,u)[ci]))])}for(let k=0;k<=40;k++){const u=s+(fut-s)*k/40;co.push([tx(u),hy(nm(ev(c,q,s,u)[ci]))])}
b+=seg(fi,`stroke="${col}" stroke-width="2" stroke-dasharray="5 3"`)+seg(co,`stroke="${col}" stroke-width="1.6" stroke-dasharray="2 3" opacity="0.6"`)}});
document.getElementById('g2').innerHTML=b;
let w=`<line x1="${tx(s)}" y1="190" x2="${tx(s)}" y2="302" stroke="${GR}" stroke-width="0.8" stroke-dasharray="2 3"/><line x1="395" y1="${wy(0)}" x2="655" y2="${wy(0)}" stroke="var(--b)" stroke-width="0.5"/>`;
const wp=[],wf=[],wr=[];for(let k=0;k<NG;k++){const u=D.tau[k];(u<=s?wp:wf).push([tx(u),wy(D.W[k])]);if(u<=s&&u>=1)wr.push([tx(u),wy(D.Wq[q-1][k])])}
w+=seg(wp,`stroke="var(--p)" stroke-width="1.6"`)+seg(wf,`stroke="var(--p)" stroke-width="1" opacity="0.3"`)+seg(wr,`stroke="${BL}" stroke-width="2" stroke-dasharray="5 3"`);
document.getElementById('g3').innerHTML=w;
let z=`<text x="40" y="22" class="th">One link, one example: forward × backward</text>`;
z+=`<text x="44" y="316" class="ts">forward hⱼ (layer 1) →</text><text x="44" y="34" class="ts">↑ backward bᵢ (layer 2)</text>`;
z+=`<text x="390" y="22" class="th">Both histories on the clock</text>`;
z+=`<text x="395" y="168" class="ts">blue: forward · purple: backward · each scaled</text>`;
z+=`<text x="390" y="184" class="th">Weight Wᵢⱼ written so far</text>`;
z+=`<text x="395" y="318" class="ts">black: true · blue: from q moments</text>`;
const Wnow=at(D.W,s),Wrec=s>=1?at(D.Wq[q-1],s):0;
z+=`<text x="40" y="346" class="th">Stored for this example: q moment pairs</text>`;
const vm=Math.max(...c.map(p=>Math.max(Math.abs(p[0]),Math.abs(p[1])))),bx=48,by=410;
for(let j=0;j<Q;j++){const kept=j<q,hx=40*Math.abs(c[j][0])/vm,hb=40*Math.abs(c[j][1])/vm,x0=bx+j*30;
z+=`<rect x="${x0}" y="${(by-hx).toFixed(1)}" width="11" height="${Math.max(hx,0.5).toFixed(1)}" rx="2" fill="${BL}" opacity="${kept?0.9:0.25}"/><rect x="${x0+12}" y="${(by-hb).toFixed(1)}" width="11" height="${Math.max(hb,0.5).toFixed(1)}" rx="2" fill="${PU}" opacity="${kept?0.9:0.25}"/><text x="${x0+11}" y="${by+15}" text-anchor="middle" class="ts">${j}</text>`}
z+=`<line x1="${bx-4}" y1="${by}" x2="${bx+Q*30-6}" y2="${by}" stroke="var(--b)" stroke-width="0.5"/>`;
z+=`<text x="${bx}" y="${by+34}" class="ts">mode k · faded: dropped</text>`;
z+=`<text x="400" y="358" class="ts">gray trail: past, fading (never stored)</text><text x="400" y="376" class="ts">dotted gray: the future, still to come</text><text x="400" y="394" class="ts">dashed blue: memory from q moments</text><text x="400" y="412" class="ts">dotted blue: memory continued past now</text>`;
z+=`<text x="400" y="440" class="ts">W now: true ${(Wnow/Wm).toFixed(3)} · from moments ${(Wrec/Wm).toFixed(3)}</text>`;
document.getElementById('g4').innerHTML=z;
document.getElementById('ql').textContent=`τ = ${s.toFixed(2)} of ${D.tauEnd.toFixed(2)}`}
function frame(t){if(last===null)last=t;const dt=Math.min(0.05,(t-last)/1000);last=t;psi+=2*dt;
if(run){now=Math.min(D.tauEnd,now+0.7*dt);document.getElementById('ts').value=now;if(now>=D.tauEnd){run=false;document.getElementById('pp').textContent='Play'}}draw();requestAnimationFrame(frame)}
document.getElementById('pp').onclick=e=>{if(!run&&now>=D.tauEnd-1e-3)now=1.3;run=!run;e.target.textContent=run?'Pause':'Play'};
document.getElementById('ts').oninput=e=>{now=+e.target.value};document.getElementById('qs').oninput=draw;
requestAnimationFrame(frame);
})();
</script>