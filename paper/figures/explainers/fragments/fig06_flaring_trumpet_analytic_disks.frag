<h2 class="sr-only">Figure 6. Analyticity disks widen as the residual decays; Taylor pieces lengthen; piece count versus a uniform covering.</h2>
<div style="display:flex;align-items:center;gap:12px;margin:0 0 6px;font-size:13px;color:var(--text-secondary)">
<span>Fitting rate ν</span><input type="range" id="nu" min="0.2" max="0.8" step="0.02" value="0.5" style="flex:1"><span id="cnt" style="min-width:260px;text-align:right"></span>
</div>
<svg id="fl" width="100%" viewBox="0 0 680 330" role="img"><title>Figure 6: flaring disks</title><desc>Residual on top; widening disks along real time; Taylor pieces below.</desc></svg>
<script>
const NS='http://www.w3.org/2000/svg',svg=document.getElementById('fl');
const E=(n,a,t)=>{const e=document.createElementNS(NS,n);for(const k in a)e.setAttribute(k,a[k]);if(t!==undefined)e.textContent=t;return e};
function draw(){const nu=+document.getElementById('nu').value,K=1,rn=0.15,T=24,dh=nu/(2*K);
const h=t=>Math.log(1+2*K*rn*Math.exp(nu*t))/(2*K),rad=t=>h(t)/(2*(1+dh));
const anchors=[0];while(anchors[anchors.length-1]<T&&anchors.length<5000){const t=anchors[anchors.length-1];anchors.push(Math.min(T,t+rad(t)/2))}
const J=anchors.length-1,Ju=Math.ceil(T/(rad(0)/2));
document.getElementById('cnt').textContent=`pieces: flaring ${J}, uniform ${Ju.toLocaleString()}`;
svg.innerHTML='';const x0=40,x1=640,px=(x1-x0)/T,X=t=>x0+t*px,yax=225;
svg.appendChild(E('text',{x:x0,y:22,class:'th'},'Remaining learning ρ(t) = e^(−νt)'));
let d='';for(let i=0;i<=200;i++){const t=T*i/200;d+=(i?'L':'M')+X(t).toFixed(1)+' '+(95-55*Math.exp(-nu*t)).toFixed(1)}
svg.appendChild(E('path',{d:d+`L${x1} 95L${x0} 95Z`,fill:'#F5C4B3',opacity:0.5,stroke:'none'}));svg.appendChild(E('path',{d,fill:'none',stroke:'#D85A30','stroke-width':1.6}));
anchors.slice(0,-1).forEach((t,i)=>{const R=rad(t)*px,frac=t/T;svg.appendChild(E('circle',{cx:X(t),cy:yax,r:Math.max(R,0.6),fill:'#7F77DD',opacity:0.05+0.1*frac,stroke:'#534AB7','stroke-width':0.5,'stroke-opacity':0.25+0.5*frac}))});
svg.appendChild(E('line',{x1:x0,y1:yax,x2:x1+12,y2:yax,stroke:'var(--b)','stroke-width':0.8}));
anchors.forEach((t,i)=>{if(i<anchors.length-1)svg.appendChild(E('line',{x1:X(t),y1:yax+70,x2:X(anchors[i+1]),y2:yax+70,stroke:i%2?'#534AB7':'#AFA9EC','stroke-width':6}))});
svg.appendChild(E('text',{x:x0,y:yax+92,class:'ts'},'Taylor pieces along real time (alternating shades): short early, long late'));
svg.appendChild(E('text',{x:x1,y:yax-80,'text-anchor':'end',class:'ts'},'disk of analyticity in complex time'));
svg.appendChild(E('text',{x:x1+4,y:yax+16,'text-anchor':'end',class:'ts'},'Re t'));
svg.appendChild(E('text',{x:x0,y:132,class:'ts'},'e^(−κ(t+is)) only rotates in s: less remaining learning, wider disk'));}
document.getElementById('nu').oninput=draw;draw();
</script>