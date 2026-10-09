<h2 class="sr-only">Figure 15. A feature history in two neuron coordinates; its trail fades while q Legendre moment vectors, evolving online, reconstruct the whole past.</h2>
<div style="font-size:15px;font-weight:500;color:var(--text-primary);margin:0 0 8px">Figure 15 · The trail fades, the moments remember</div>
<div style="display:flex;align-items:center;gap:10px;margin:0 0 6px;font-size:13px;color:var(--text-secondary)">
<button id="pp" style="font-size:13px;padding:4px 10px">Pause</button>
<button id="rs" style="font-size:13px;padding:4px 10px">Restart</button>
<span>Moments q</span><input type="range" id="qs" min="1" max="10" step="1" value="3" style="flex:1">
<span id="ql" style="min-width:170px;text-align:right"></span>
</div>
<svg id="sv" width="100%" viewBox="0 0 680 350" role="img"><title>Figure 15: the trail fades, the moments remember</title><desc>Left: a history curve whose old trail fades, the reconstruction from q moments, and a chain of moment arms drawing it. Right: the stored moment vectors and their magnitudes.</desc>
<defs><clipPath id="cp15"><rect x="8" y="56" width="430" height="272"/></clipPath></defs>
<g id="gl" clip-path="url(#cp15)"></g><g id="gr"></g></svg>
<script>
(()=>{
const S=8,Q=12,T1=1+S,BL='#2a78d6',BD='#185FA5',GR='#888780';
const path=u=>[-1.0+1.9*u-0.55*Math.sin(2*Math.PI*u),-0.55+1.25*Math.sin(Math.PI*u)+0.3*Math.sin(3*Math.PI*u)];
const h=xi=>path(Math.min(Math.max((xi-1)/S,0),1));
const leg=(x,q)=>{const P=[1,x];for(let j=1;j<q;j++)P.push(((2*j+1)*x*P[j]-j*P[j-1])/(j+1));return P};
const X=x=>230+125*x,Y=y=>200-125*y;
let tau,m,run=true,psi=0,last=null;
function reset(){tau=1;m=Array.from({length:Q},()=>[0,0]);m[0]=h(0).slice();}
function step(dt){const n=Math.max(1,Math.ceil(dt/0.002)),d=dt/n;for(let s=0;s<n;s++){const hv=h(tau);let a0=0,a1=0;const dm=[];
for(let j=0;j<Q;j++){dm.push([hv[0]-(j*m[j][0]+a0)/tau,hv[1]-(j*m[j][1]+a1)/tau]);a0+=(2*j+1)*m[j][0];a1+=(2*j+1)*m[j][1]}
for(let j=0;j<Q;j++){m[j][0]+=d*dm[j][0];m[j][1]+=d*dm[j][1]}tau+=d}}
const coef=()=>m.map((v,j)=>[(2*j+1)/tau*v[0],(2*j+1)/tau*v[1]]);
function draw(){const q=+document.getElementById('qs').value,c=coef();let s='';
s+=`<line x1="${X(-0.06)}" y1="${Y(0)}" x2="${X(0.06)}" y2="${Y(0)}" stroke="${GR}" stroke-width="0.8"/><line x1="${X(0)}" y1="${Y(-0.06)}" x2="${X(0)}" y2="${Y(0.06)}" stroke="${GR}" stroke-width="0.8"/>`;
const K=160;for(let k=0;k<K;k++){const a=1+(tau-1)*k/K,b=1+(tau-1)*(k+1)/K,p=h(a),r=h(b),op=0.06+0.7*Math.exp(-(tau-b)/1.1);
s+=`<line x1="${X(p[0]).toFixed(1)}" y1="${Y(p[1]).toFixed(1)}" x2="${X(r[0]).toFixed(1)}" y2="${Y(r[1]).toFixed(1)}" stroke="${GR}" stroke-width="2.4" stroke-linecap="round" opacity="${op.toFixed(3)}"/>`}
if(q===1){s+=`<circle cx="${X(c[0][0])}" cy="${Y(c[0][1])}" r="5" fill="none" stroke="${BL}" stroke-width="2"/>`}else{let d='';for(let k=0;k<=220;k++){const x=-1+2*k/220,P=leg(x,q);let u=0,v=0;for(let j=0;j<q;j++){u+=c[j][0]*P[j];v+=c[j][1]*P[j]}d+=(k?'L':'M')+X(u).toFixed(1)+' '+Y(v).toFixed(1)}
s+=`<path d="${d}" fill="none" stroke="${BL}" stroke-width="2" stroke-dasharray="6 4"/>`}
const xp=-Math.cos(psi),P=leg(xp,q);let ox=0,oy=0;
for(let j=0;j<q;j++){const nx=ox+c[j][0]*P[j],ny=oy+c[j][1]*P[j],op=Math.max(0.35,1-0.09*j);
s+=`<line x1="${X(ox).toFixed(1)}" y1="${Y(oy).toFixed(1)}" x2="${X(nx).toFixed(1)}" y2="${Y(ny).toFixed(1)}" stroke="${BD}" stroke-width="${Math.max(1,3-0.3*j)}" stroke-linecap="round" opacity="${op}"/><circle cx="${X(nx).toFixed(1)}" cy="${Y(ny).toFixed(1)}" r="2.2" fill="${BD}" opacity="${op}"/>`;ox=nx;oy=ny}
s+=`<circle cx="${X(ox).toFixed(1)}" cy="${Y(oy).toFixed(1)}" r="5.5" fill="none" stroke="${BD}" stroke-width="1.5"/>`;
const hn=h(tau);s+=`<circle cx="${X(hn[0]).toFixed(1)}" cy="${Y(hn[1]).toFixed(1)}" r="4.5" fill="var(--p)"/>`;
s+=`<text x="${X(hn[0])+9}" y="${Y(hn[1])+4}" class="ts">now</text>`;
document.getElementById('gl').innerHTML=s;
let r=`<text x="20" y="22" class="th">Two neuron coordinates of a history</text>`;
r+=`<line x1="22" y1="44" x2="44" y2="44" stroke="${GR}" stroke-width="2.4" opacity="0.6"/><text x="50" y="48" class="ts">trail, not stored</text><line x1="160" y1="44" x2="182" y2="44" stroke="${BL}" stroke-width="2" stroke-dasharray="6 4"/><text x="188" y="48" class="ts">memory from q moments</text><line x1="352" y1="44" x2="374" y2="44" stroke="${BD}" stroke-width="2.4"/><text x="380" y="48" class="ts">arms</text>`;
r+=`<text x="458" y="22" class="th">Stored state</text>`;
const cx=555,cy=118,sc=62;r+=`<circle cx="${cx}" cy="${cy}" r="2" fill="var(--s)"/>`;
for(let j=Q-1;j>=0;j--){const kept=j<q,ex=cx+sc*c[j][0],ey=cy-sc*c[j][1],ang=Math.atan2(ey-cy,ex-cx),L=Math.hypot(ex-cx,ey-cy);
if(L<1)continue;const hx=ex-6*Math.cos(ang-0.4),hy=ey-6*Math.sin(ang-0.4),gx=ex-6*Math.cos(ang+0.4),gy=ey-6*Math.sin(ang+0.4);
const col=kept?BD:GR,op=kept?1:0.35;r+=`<g opacity="${op}"><line x1="${cx}" y1="${cy}" x2="${ex.toFixed(1)}" y2="${ey.toFixed(1)}" stroke="${col}" stroke-width="${kept?1.8:1}" ${kept?'':'stroke-dasharray="3 3"'}/><path d="M${hx.toFixed(1)} ${hy.toFixed(1)}L${ex.toFixed(1)} ${ey.toFixed(1)}L${gx.toFixed(1)} ${gy.toFixed(1)}" fill="none" stroke="${col}" stroke-width="1.4"/></g>`}
r+=`<text x="458" y="198" class="ts">q vectors in neuron space</text>`;
const bx=470,by=290,bw=14;
const vmax=Math.max(...c.map(v=>Math.hypot(...v)));const lg=v=>v/vmax;
for(let j=0;j<Q;j++){const v=Math.hypot(...c[j]),hh=70*lg(v),kept=j<q;
r+=`<rect x="${bx+j*15}" y="${(by-hh).toFixed(1)}" width="${bw-2}" height="${Math.max(hh,0.5).toFixed(1)}" rx="2" fill="${kept?BL:GR}" opacity="${kept?0.9:0.3}"/>`}
r+=`<line x1="${bx-3}" y1="${by}" x2="${bx+Q*15}" y2="${by}" stroke="var(--b)" stroke-width="0.5"/>`;
r+=`<text x="${bx}" y="${by+16}" class="ts">mode j = 0 … 11, size</text>`;
r+=`<text x="20" y="344" class="ts">j = 0: mean position · j = 1: mean velocity · j = 2: mean bend · each arm is a stored vector scaled by Pⱼ</text>`;
document.getElementById('gr').innerHTML=r;
document.getElementById('ql').textContent=`clock τ = ${tau.toFixed(1)} · ${q} stored vector${q>1?'s':''}`}
function frame(t){if(last===null)last=t;const dt=Math.min(0.05,(t-last)/1000);last=t;
if(run){if(tau<T1)step(Math.min(1.4*dt,T1-tau));psi+=2.0*dt}draw();requestAnimationFrame(frame)}
document.getElementById('pp').onclick=e=>{run=!run;e.target.textContent=run?'Pause':'Play'};
document.getElementById('rs').onclick=()=>{reset();psi=0};
document.getElementById('qs').oninput=draw;
reset();step(3.2);requestAnimationFrame(frame);
})();
</script>