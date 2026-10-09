<h2 class="sr-only">Figure 1. The learning clock: equal-area bands under the residual map to equal clock ticks.</h2>
<div style="display:flex;align-items:center;gap:12px;margin:0 0 6px;font-size:13px;color:var(--text-secondary)">
<span>Fitting rate ν</span><input type="range" id="nu" min="0.12" max="0.6" step="0.01" value="0.25" style="flex:1"><span id="lab" style="min-width:170px;text-align:right"></span>
</div>
<svg id="cs" width="100%" viewBox="0 0 680 330" role="img"><title>Figure 1: learning clock</title><desc>Equal-area bands under the residual connect to equally spaced clock ticks.</desc></svg>
<script>
const NS='http://www.w3.org/2000/svg',svg=document.getElementById('cs');
const E=(n,a,t)=>{const e=document.createElementNS(NS,n);for(const k in a)e.setAttribute(k,a[k]);if(t!==undefined)e.textContent=t;return e};
function draw(){const nu=+document.getElementById('nu').value,K=16,Tm=24,x0=60,x1=620,yb=300,yt=60,H=110;
const tinf=1/nu;document.getElementById('lab').textContent=`τ∞ = 1/ν = ${tinf.toFixed(2)}`;
svg.innerHTML='';
const xt=t=>x0+(x1-x0)*Math.min(t,Tm)/Tm, rho=t=>Math.exp(-nu*t), yr=t=>yb-H*rho(t);
const tk=k=>k>=K?Infinity:-Math.log(1-k/K)/nu;
for(let k=0;k<K;k++){const a=tk(k),b=Math.min(tk(k+1),Tm);if(a>=Tm)break;let d=`M${xt(a)} ${yb}`;const S=24;for(let s=0;s<=S;s++){const t=a+(b-a)*s/S;d+=`L${xt(t).toFixed(1)} ${yr(t).toFixed(1)}`}d+=`L${xt(b)} ${yb}Z`;
svg.appendChild(E('path',{d,fill:'#7F77DD',opacity:k%2?0.28:0.55,stroke:'none'}))}
let dc='';for(let s=0;s<=240;s++){const t=Tm*s/240;dc+=(s?'L':'M')+xt(t).toFixed(1)+' '+yr(t).toFixed(1)}
svg.appendChild(E('path',{d:dc,fill:'none',stroke:'#D85A30','stroke-width':1.8}));
for(let k=0;k<=K;k++){const xa=x0+(x1-x0)*k/K,t=tk(k);const xbt=t>=Tm?x1:xt(t);
svg.appendChild(E('line',{x1:xa,y1:yt,x2:xbt,y2:yb-H-12,stroke:'#534AB7','stroke-width':0.6,opacity:0.55}));
svg.appendChild(E('line',{x1:xa,y1:yt-5,x2:xa,y2:yt+5,stroke:'#534AB7','stroke-width':1.2}))}
svg.appendChild(E('line',{x1:x0,y1:yt,x2:x1,y2:yt,stroke:'#534AB7','stroke-width':1.2}));
svg.appendChild(E('text',{x:x0,y:yt-14,class:'th'},'learning clock τ: equal ticks'));
svg.appendChild(E('text',{x:x1,y:yt-14,'text-anchor':'end',class:'ts'},'τ∞'));
svg.appendChild(E('line',{x1:x0,y1:yb,x2:x1+30,y2:yb,stroke:'var(--b)','stroke-width':0.8}));
[0,4,8,12,16,20,24].forEach(t=>{svg.appendChild(E('line',{x1:xt(t),y1:yb,x2:xt(t),y2:yb+5,stroke:'var(--b)','stroke-width':0.8}));svg.appendChild(E('text',{x:xt(t),y:yb+19,'text-anchor':'middle',class:'ts'},String(t)))});
svg.appendChild(E('text',{x:x1+34,y:yb+4,class:'ts'},'∞'));
svg.appendChild(E('text',{x:x0+190,y:yb-H+18,class:'ts'},'residual ρ(t); every band has the same area'));
svg.appendChild(E('text',{x:340,y:yb+40,'text-anchor':'middle',class:'ts'},'physical time t ∈ [0, ∞) folds into the finite interval τ ∈ [0, τ∞); Legendre moments live there'));
}
document.getElementById('nu').oninput=draw;draw();
</script>