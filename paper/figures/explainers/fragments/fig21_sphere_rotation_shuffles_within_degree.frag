<h2 class="sr-only">Figure 21. A neuron's response on the input sphere rotates with its weight; its spherical-harmonic coefficients shuffle within each degree while the energy per degree stays fixed, so one degree cutoff serves every neuron.</h2>
<div style="font-size:15px;font-weight:500;color:var(--text-primary);margin:0 0 8px">Figure 21 · Rotation shuffles within a degree</div>
<div style="display:flex;align-items:center;gap:10px;margin:0 0 6px;font-size:13px;color:var(--text-secondary)">
<button id="pp" style="font-size:13px;padding:4px 10px">Pause</button>
<span>Degree cutoff L</span><input type="range" id="Ls" min="0" max="5" step="1" value="3" style="flex:1">
<span id="Ll" style="min-width:250px;text-align:right"></span>
</div>
<div style="position:relative;width:680px;height:330px">
<canvas id="cs" style="position:absolute;left:4px;top:52px;width:200px;height:200px"></canvas>
<canvas id="cp" style="position:absolute;left:214px;top:34px;width:360px;height:250px"></canvas>
<svg id="ov" width="680" height="330" viewBox="0 0 680 330" style="position:absolute;left:0;top:0" role="img"><title>Figure 21: rotation shuffles within a degree</title><desc>A rotating sphere showing one neuron's response, a pyramid of spherical harmonics whose brightness shows the neuron's coefficients, and constant energy bars per degree.</desc></svg>
</div>
<script>
(()=>{
const DPR=2,GN=[27,175,122],PU=[127,119,221],BASE=[232,230,223];
const e=0.38,LV=(()=>{const v=[-0.45,0.55,0.7],n=Math.hypot(...v);return v.map(x=>x/n)})();
const toWorld=(x,y,z)=>[x,-y*Math.sin(e)+z*Math.cos(e),y*Math.cos(e)+z*Math.sin(e)];
const LM=5;
function plm(l,m,x){let pmm=1;const s=Math.sqrt(Math.max(0,1-x*x));let f=1;for(let i=1;i<=m;i++){pmm*=-f*s;f+=2}if(l===m)return pmm;let pm1=x*(2*m+1)*pmm;if(l===m+1)return pm1;let pl=0;for(let ll=m+2;ll<=l;ll++){pl=((2*ll-1)*x*pm1-(ll+m-1)*pmm)/(ll-m);pmm=pm1;pm1=pl}return pl}
const fac=n=>{let r=1;for(let i=2;i<=n;i++)r*=i;return r};
const NLM=(l,m)=>Math.sqrt((2*l+1)/(4*Math.PI)*fac(l-m)/fac(l+m));
function Y(l,m,p){const ct=Math.max(-1,Math.min(1,p[2])),ph=Math.atan2(p[1],p[0]),am=Math.abs(m);const b=NLM(l,am)*plm(l,am,ct);return m===0?b:m>0?Math.SQRT2*b*Math.cos(am*ph):Math.SQRT2*b*Math.sin(am*ph)}
const gauss=n=>{const X=[],W=[];for(let i=1;i<=n;i++){let x=Math.cos(Math.PI*(i-0.25)/(n+0.5)),dp=1;for(let it=0;it<60;it++){let p0=1,p1=x;for(let k=2;k<=n;k++){const p2=((2*k-1)*x*p1-(k-1)*p0)/k;p0=p1;p1=p2}dp=n*(x*p1-p0)/(x*x-1);const d=p1/dp;x-=d;if(Math.abs(d)<1e-15)break}X.push(x);W.push(2/((1-x*x)*dp*dp))}return [X,W]};
const g=t=>Math.tanh(4*t+0.5),[gx,gw]=gauss(160),LT=40,Gl=[];
for(let l=0;l<=LT;l++){let s=0;gx.forEach((x,k)=>{let p0=1,p1=x,pl=l===0?1:x;for(let j=2;j<=l;j++){pl=((2*j-1)*x*p1-(j-1)*p0)/j;p0=p1;p1=pl}s+=gw[k]*g(x)*pl});Gl.push(2*Math.PI*s)}
const El=Gl.map((G,l)=>G*G*(2*l+1)/(4*Math.PI)),Etot=El.reduce((a,b)=>a+b,0);
const mix=(v,sh)=>{const a=Math.max(-1,Math.min(1,v)),m=Math.abs(a),c=a>=0?GN:PU;return BASE.map((b,i)=>Math.round((b+(c[i]-b)*m)*sh))};
const IS=26*DPR,icons={};
for(let l=0;l<=LM;l++)for(let m=-l;m<=l;m++){let mx=0;const vals=[];for(let j=0;j<IS;j++)for(let i=0;i<IS;i++){const x=2*(i+0.5)/IS-1,y=1-2*(j+0.5)/IS,q=x*x+y*y;if(q>1){vals.push(null);continue}const z=Math.sqrt(1-q),v=Y(l,m,toWorld(x,y,z));mx=Math.max(mx,Math.abs(v));vals.push([v,z,x,y])}
icons[l+','+m]=[1,-1].map(sg=>{const c=document.createElement('canvas');c.width=c.height=IS;const ctx=c.getContext('2d'),im=ctx.createImageData(IS,IS);vals.forEach((o,k)=>{if(!o){im.data[4*k+3]=0;return}const sh=0.62+0.38*Math.max(0,o[2]*LV[0]+o[3]*LV[1]+o[1]*LV[2]),col=mix(sg*o[0]/mx,sh);im.data[4*k]=col[0];im.data[4*k+1]=col[1];im.data[4*k+2]=col[2];im.data[4*k+3]=255});ctx.putImageData(im,0,0);return c})}
const cs=document.getElementById('cs'),SS=200*DPR;cs.width=cs.height=SS;const sctx=cs.getContext('2d'),sim=sctx.createImageData(SS,SS);
const pix=[];for(let j=0;j<SS;j++)for(let i=0;i<SS;i++){const x=2*(i+0.5)/SS-1,y=1-2*(j+0.5)/SS,q=x*x+y*y;if(q>1){pix.push(null);continue}const z=Math.sqrt(1-q);pix.push([toWorld(x,y,z),0.6+0.4*Math.max(0,x*LV[0]+y*LV[1]+z*LV[2])])}
const cp=document.getElementById('cp');cp.width=360*DPR;cp.height=250*DPR;const pctx=cp.getContext('2d');
const ov=document.getElementById('ov'),NS='http://www.w3.org/2000/svg';
const E=(n,a,t)=>{const el=document.createElementNS(NS,n);for(const k in a)el.setAttribute(k,a[k]);if(t!==undefined)el.textContent=t;return el};
const cell=30,rowY=l=>34+l*42,colX=(l,m)=>410+m*cell;
let run=true,T=0,last=null;
function frame(ts){if(last===null)last=ts;const dt=Math.min(0.05,(ts-last)/1000);last=ts;if(run)T+=dt;
const L=+document.getElementById('Ls').value,al=0.55*T,be=1.05+0.65*Math.sin(0.31*T),w=[Math.sin(be)*Math.cos(al),Math.sin(be)*Math.sin(al),Math.cos(be)];
for(let k=0;k<pix.length;k++){const o=pix[k];if(!o){sim.data[4*k+3]=0;continue}const p=o[0],c=mix(g(p[0]*w[0]+p[1]*w[1]+p[2]*w[2]),o[1]);sim.data[4*k]=c[0];sim.data[4*k+1]=c[1];sim.data[4*k+2]=c[2];sim.data[4*k+3]=255}
sctx.putImageData(sim,0,0);
const vx=w[0],vy=-w[1]*Math.sin(e)+w[2]*Math.cos(e),vz=w[1]*Math.cos(e)+w[2]*Math.sin(e),mk=document.getElementById('wm'),mt=document.getElementById('wt');mk.setAttribute('cx',(104+100*vx).toFixed(1));mk.setAttribute('cy',(152-100*vy).toFixed(1));mt.setAttribute('x',(112+100*vx).toFixed(1));mt.setAttribute('y',(148-100*vy).toFixed(1));mk.style.display=mt.style.display=vz>0?'':'none';
pctx.clearRect(0,0,cp.width,cp.height);const C={};for(let l=0;l<=LM;l++)for(let m=-l;m<=l;m++)C[l+','+m]=Gl[l]*Y(l,m,w);
const rowE=[];for(let l=0;l<=LM;l++){let s=0;for(let m=-l;m<=l;m++){const v=C[l+','+m];s+=v*v;const a=Math.abs(v)/Math.sqrt(El[l]);pctx.globalAlpha=(l<=L?1:0.25)*Math.max(0.06,a);
pctx.drawImage(icons[l+','+m][v>=0?0:1],(colX(l,m)-214-13)*DPR,(rowY(l)-34+2)*DPR,IS,IS)}rowE.push(s)}
pctx.globalAlpha=1;
const EM=Math.max(...El.slice(0,LM+1));for(let l=0;l<=LM;l++)document.getElementById('b'+l).setAttribute('width',Math.max(1,86*Math.sqrt(rowE[l]/EM)).toFixed(1));
const tail=El.slice(L+1).reduce((a,b)=>a+b,0)/Etot,cut=document.getElementById('cut');cut.setAttribute('y1',rowY(L)+36);cut.setAttribute('y2',rowY(L)+36);cut.style.display=L<LM?'':'none';
document.getElementById('Ll').textContent=`${(L+1)*(L+1)} shapes · energy beyond L: ${(100*tail).toFixed(2)}%`;
requestAnimationFrame(frame)}
ov.appendChild(E('text',{x:14,y:22,class:'th'},'One neuron on the input sphere'));
ov.appendChild(E('text',{x:104,y:276,'text-anchor':'middle',class:'ts'},'tanh(⟨w, v⟩ + β) as w rotates'));
ov.appendChild(E('text',{x:410,y:22,'text-anchor':'middle',class:'th'},'Its harmonic coefficients, by degree'));
ov.appendChild(E('text',{x:592,y:22,class:'th'},'Energy'));
for(let l=0;l<=LM;l++){ov.appendChild(E('text',{x:210,y:rowY(l)+20,class:'ts'},'ℓ = '+l));ov.appendChild(E('rect',{id:'b'+l,x:584,y:rowY(l)+9,width:1,height:14,rx:3,fill:'#1baf7a'}))}
ov.appendChild(E('line',{id:'cut',x1:206,x2:676,y1:0,y2:0,stroke:'#888780','stroke-width':1,'stroke-dasharray':'4 3'}));
ov.appendChild(E('text',{x:584,y:300,class:'ts'},'per degree:'));ov.appendChild(E('text',{x:584,y:316,class:'ts'},'never changes'));
ov.appendChild(E('text',{x:244,y:308,class:'ts'},'brightness: share of its degree · green +, purple −'));
ov.appendChild(E('circle',{id:'wm',cx:0,cy:0,r:4,fill:'#fff',stroke:'#2C2C2A','stroke-width':1.5}));ov.appendChild(E('text',{id:'wt',x:0,y:0,class:'ts',style:'fill:#2C2C2A'},'w'));
document.getElementById('pp').onclick=ev=>{run=!run;ev.target.textContent=run?'Pause':'Play'};
requestAnimationFrame(frame);
})();
</script>