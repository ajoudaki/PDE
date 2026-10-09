<h2 class="sr-only">Figure 7. Time-based amplification explodes; activity-based amplification saturates.</h2>
<div style="display:flex;align-items:center;gap:12px;margin:0 0 6px;font-size:13px;color:var(--text-secondary)">
<span>Fitting rate ν</span><input type="range" id="nu" min="0.1" max="0.8" step="0.01" value="0.3" style="flex:1"><span id="lab" style="min-width:210px;text-align:right"></span>
</div>
<svg id="fa" width="100%" viewBox="0 0 680 290" role="img"><title>Figure 7: feedback amplification</title><desc>e to the Lt versus e to the C times integrated residual, log scale against time.</desc></svg>
<script>
const NS='http://www.w3.org/2000/svg',svg=document.getElementById('fa');
const E=(n,a,t)=>{const e=document.createElementNS(NS,n);for(const k in a)e.setAttribute(k,a[k]);if(t!==undefined)e.textContent=t;return e};
function draw(){const nu=+document.getElementById('nu').value,L=0.5,C=1,T=30,x0=60,x1=620,y0=240,H=190;
const X=t=>x0+(x1-x0)*t/T,Y=lg=>y0-H*Math.min(lg,6)/6;
svg.innerHTML='';
for(let k=0;k<=6;k+=2){svg.appendChild(E('line',{x1:x0,y1:Y(k),x2:x1,y2:Y(k),stroke:'var(--b)','stroke-width':0.4,opacity:0.6}));svg.appendChild(E('text',{x:x0-8,y:Y(k)+4,'text-anchor':'end',class:'ts'},k?`10^${k}`:'1'))}
let dr='';for(let i=0;i<=200;i++){const t=T*i/200;dr+=(i?'L':'M')+X(t).toFixed(1)+' '+(y0-60*Math.exp(-nu*t)).toFixed(1)}
svg.appendChild(E('path',{d:dr+`L${x1} ${y0}L${x0} ${y0}Z`,fill:'#F5C4B3',opacity:0.45,stroke:'none'}));
let dn='',da='';for(let i=0;i<=300;i++){const t=T*i/300;const ln=L*t/Math.LN10,la=C*(1-Math.exp(-nu*t))/nu/Math.LN10;if(ln<=6.05)dn+=(dn?'L':'M')+X(t).toFixed(1)+' '+Y(ln).toFixed(1);da+=(i?'L':'M')+X(t).toFixed(1)+' '+Y(la).toFixed(1)}
svg.appendChild(E('path',{d:dn,fill:'none',stroke:'#888780','stroke-width':1.8,'stroke-dasharray':'6 4'}));
svg.appendChild(E('path',{d:da,fill:'none',stroke:'#534AB7','stroke-width':2.4}));
const ceil=C/nu/Math.LN10;svg.appendChild(E('line',{x1:x0,y1:Y(ceil),x2:x1,y2:Y(ceil),stroke:'#534AB7','stroke-width':0.6,'stroke-dasharray':'2 3'}));
svg.appendChild(E('text',{x:X(19),y:Y(5.4),class:'ts'},'per unit time: e^(Lt) → ∞'));
svg.appendChild(E('text',{x:x1,y:Y(ceil)-7,'text-anchor':'end',class:'ts'},'per unit learning: e^(C∫ρ) ≤ e^(C/ν)'));
svg.appendChild(E('text',{x:x0+4,y:y0-66,class:'ts'},'shaded: remaining learning ρ(t)'));
svg.appendChild(E('line',{x1:x0,y1:y0,x2:x1,y2:y0,stroke:'var(--b)','stroke-width':0.8}));
svg.appendChild(E('text',{x:(x0+x1)/2,y:y0+20,'text-anchor':'middle',class:'ts'},'training time t'));
svg.appendChild(E('text',{x:x0,y:22,class:'th'},'How much can feedback amplify a compression error?'));
document.getElementById('lab').textContent=`ceiling e^(1/ν) = ${Math.exp(C/nu).toFixed(1)}`;}
document.getElementById('nu').oninput=draw;draw();
</script>