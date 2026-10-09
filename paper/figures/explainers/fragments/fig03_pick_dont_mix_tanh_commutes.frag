<h2 class="sr-only">Figure 3. Selecting coordinates commutes with tanh; mixing does not.</h2>
<div style="display:flex;align-items:center;gap:12px;margin:0 0 6px;font-size:13px;color:var(--text-secondary)">
<button id="nv" style="font-size:13px;padding:4px 10px">New vector</button><span id="msg"></span>
</div>
<svg id="pm" width="100%" viewBox="0 0 680 330" role="img"><title>Figure 3: pick versus mix</title><desc>Pick-then-tanh equals tanh-then-pick; mix-then-tanh differs.</desc></svg>
<script>
const NS='http://www.w3.org/2000/svg',svg=document.getElementById('pm');
const E=(n,a,t)=>{const e=document.createElementNS(NS,n);for(const k in a)e.setAttribute(k,a[k]);if(t!==undefined)e.textContent=t;return e};
let seed=5;const rnd=()=>{seed=(seed*16807)%2147483647;return seed/2147483647};
const g=()=>Math.sqrt(-2*Math.log(rnd()+1e-12))*Math.cos(2*Math.PI*rnd());
function bars(x0,y0,vals,cols,w,gap,sc){vals.forEach((v,i)=>{const h=Math.abs(v)*sc,x=x0+i*(w+gap);svg.appendChild(E('rect',{x,y:v>=0?y0-h:y0,width:w,height:Math.max(h,0.5),fill:cols[i],rx:1.5}))});svg.appendChild(E('line',{x1:x0-4,y1:y0,x2:x0+vals.length*(w+gap),y2:y0,stroke:'var(--b)','stroke-width':0.5}))}
function draw(){svg.innerHTML='';const n=24,q=5;const z=Array.from({length:n},()=>1.6*g());
const I=[];while(I.length<q){const k=Math.floor(rnd()*n);if(!I.includes(k))I.push(k)}I.sort((a,b)=>a-b);
const P=Array.from({length:q},()=>{const r=Array.from({length:n},()=>rnd());const s=r.reduce((a,b)=>a+b);return r.map(v=>v/s)});
svg.appendChild(E('text',{x:40,y:24,class:'th'},'Preactivations z of n neurons'));
bars(40,90,z,z.map((_,i)=>I.includes(i)?'#1D9E75':'#B4B2A9'),20,4,22);
svg.appendChild(E('text',{x:40,y:150,class:'ts'},'green: the selected neurons I'));
const tz=z.map(Math.tanh);
const pickA=I.map(i=>tz[i]),pickB=I.map(i=>Math.tanh(z[i]));
const mixA=P.map(r=>r.reduce((s,p,i)=>s+p*tz[i],0)),mixB=P.map(r=>Math.tanh(r.reduce((s,p,i)=>s+p*z[i],0)));
svg.appendChild(E('text',{x:40,y:186,class:'th'},'Pick: exact'));
const inter=(A,B)=>{const out=[],c=[];A.forEach((a,i)=>{out.push(a,B[i]);c.push('#5DCAA5','#0F6E56')});return [out,c]};
let [v1,c1]=inter(pickA,pickB);bars(40,262,v1,c1,14,4,48);
svg.appendChild(E('text',{x:40,y:318,class:'ts'},'light: tanh then pick; dark: pick then tanh'));
svg.appendChild(E('text',{x:370,y:186,class:'th'},'Mix: not exact'));
let [v2,c2]=inter(mixA,mixB);c2=c2.map((c,i)=>i%2?'#993C1D':'#F0997B');bars(370,262,v2,c2,14,4,48);
svg.appendChild(E('text',{x:370,y:318,class:'ts'},'light: tanh then mix; dark: mix then tanh'));
const errPick=Math.max(...pickA.map((a,i)=>Math.abs(a-pickB[i]))),errMix=Math.max(...mixA.map((a,i)=>Math.abs(a-mixB[i])));
document.getElementById('msg').textContent=`max mismatch: pick ${errPick.toExponential(0)}, mix ${errMix.toFixed(2)}`;}
document.getElementById('nv').onclick=draw;draw();
</script>