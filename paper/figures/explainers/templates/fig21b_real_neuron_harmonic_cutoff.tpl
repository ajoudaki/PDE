<h2 class="sr-only">Figure 21b. A real neuron and the output of a trained width-1024 network on the input sphere, their truncation to spherical-harmonic degree at most K, the difference, and the degree spectra of all 1024 neurons.</h2>
<div style="font-size:15px;font-weight:500;color:var(--text-primary);margin:0 0 8px">Figure 21b · A real neuron needs few harmonics</div>
<div style="display:flex;align-items:center;gap:10px;margin:0 0 6px;font-size:13px;color:var(--text-secondary)">
<button id="nx" style="font-size:13px;padding:4px 10px">Next neuron</button>
<button id="pp" style="font-size:13px;padding:4px 10px">Pause</button>
<span>Degree cutoff K</span><input type="range" id="Ks" min="1" max="15" step="2" value="5" style="flex:1">
<span id="Kl" style="min-width:60px;text-align:right"></span>
</div>
<div style="position:relative;width:680px;height:440px">
<canvas id="c0" style="position:absolute;left:30px;top:44px;width:170px;height:170px"></canvas>
<canvas id="c1" style="position:absolute;left:255px;top:44px;width:170px;height:170px"></canvas>
<canvas id="c2" style="position:absolute;left:480px;top:44px;width:170px;height:170px"></canvas>
<svg id="ov" width="680" height="440" viewBox="0 0 680 440" style="position:absolute;left:0;top:0" role="img"><title>Figure 21b: a real neuron needs few harmonics</title><desc>Three spheres: the function, its degree-K truncation and the magnified difference; below, energy per degree for this function and for all 1024 neurons.</desc></svg>
</div>
<div id="rd" style="font-size:13px;color:var(--text-secondary)"></div>
<script>
(()=>{
const D=__DATA__;
const DPR=2,GN=[27,175,122],PU=[127,119,221],BASE=[236,234,228],KM=D.KM;
const fac=n=>{let r=1;for(let i=2;i<=n;i++)r*=i;return r};
function plmAll(L,x){const s=Math.sqrt(Math.max(0,1-x*x)),P=[];for(let m=0;m<=L;m++){P[m]=[];let pmm=1,f=1;for(let i=1;i<=m;i++){pmm*=-f*s;f+=2}P[m][m]=pmm;if(m<L){P[m][m+1]=x*(2*m+1)*pmm}for(let l=m+2;l<=L;l++)P[m][l]=((2*l-1)*x*P[m][l-1]-(l+m-1)*P[m][l-2])/(l-m)}return P}
const NL=[];for(let l=0;l<=KM;l++){NL[l]=[];for(let m=0;m<=l;m++)NL[l][m]=Math.sqrt((2*l+1)/(4*Math.PI)*fac(l-m)/fac(l+m))}
const NT=72,NP=144,NC=D.funcs[0].c.length,deg=[];for(let l=1;l<=KM;l+=2)for(let m=-l;m<=l;m++)deg.push(l);
const Yt=new Float32Array(NC*NT*NP);
for(let it=0;it<NT;it++){const th=Math.PI*(it+0.5)/NT,ct=Math.cos(th),P=plmAll(KM,ct);for(let ip=0;ip<NP;ip++){const ph=2*Math.PI*ip/NP;let c=0;for(let l=1;l<=KM;l+=2)for(let m=-l;m<=l;m++){const am=Math.abs(m),b=NL[l][am]*P[am][l];Yt[c*NT*NP+it*NP+ip]=m===0?b:m>0?Math.SQRT2*b*Math.cos(am*ph):Math.SQRT2*b*Math.sin(am*ph);c++}}}
function tex(c,K){const T=new Float32Array(NT*NP);for(let j=0;j<NC;j++){if(deg[j]>K)continue;const cj=c[j];if(cj===0)continue;const o=j*NT*NP;for(let p=0;p<NT*NP;p++)T[p]+=cj*Yt[o+p]}return T}
const SS=170*DPR,pix=[];const e=0.35;
for(let j=0;j<SS;j++)for(let i=0;i<SS;i++){const x=2*(i+0.5)/SS-1,y=1-2*(j+0.5)/SS,q=x*x+y*y;if(q>1){pix.push(null);continue}const z=Math.sqrt(1-q);pix.push([x,-y*Math.sin(e)+z*Math.cos(e),y*Math.cos(e)+z*Math.sin(e),0.62+0.38*Math.max(0,-0.4*x+0.55*y+0.73*z)])}
const cvs=[0,1,2].map(k=>{const c=document.getElementById('c'+k);c.width=c.height=SS;const ctx=c.getContext('2d');return {ctx,img:ctx.createImageData(SS,SS)}});
const mix=(v,sh)=>{const a=Math.max(-1,Math.min(1,v)),m=Math.abs(a),c=a>=0?GN:PU;return BASE.map((b,i)=>Math.round((b+(c[i]-b)*m)*sh))};
let fi=0,K=5,full,cut,diff,scale=1,dmul=1,rot=0,run=true,last=null,stats={};
function rebuild(){const c=D.funcs[fi].c;full=tex(c,KM);cut=tex(c,K);diff=full.map((v,p)=>v-cut[p]);scale=Math.max(...full.map(Math.abs));const dm=Math.max(...diff.map(Math.abs));dmul=1;if(dm>0){const r=0.8*scale/dm;let best=1;for(let e=0;e<8;e++)for(const b of [1,2,5]){const v=b*Math.pow(10,e);if(v<=r)best=v}dmul=best}
let e2=0,t2=0;for(let l=1;l<=KM;l+=2){let s=0;c.forEach((v,j)=>{if(deg[j]===l)s+=v*v});t2+=s;if(l>K)e2+=s}stats={lost:e2/t2,maxerr:dm/scale};drawSVG()}
function render(){[full,cut,diff].forEach((T,k)=>{const {ctx,img}=cvs[k],mul=k===2?dmul:1;for(let p=0;p<pix.length;p++){const o=pix[p];if(!o){img.data[4*p+3]=0;continue}
const cr=Math.cos(rot),sr=Math.sin(rot),wx=cr*o[0]-sr*o[1],wy=sr*o[0]+cr*o[1],wz=o[2];let it=Math.floor(Math.acos(Math.max(-1,Math.min(1,wz)))/Math.PI*NT);it=Math.min(NT-1,it);let ip=Math.floor(((Math.atan2(wy,wx)+2*Math.PI)%(2*Math.PI))/(2*Math.PI)*NP)%NP;
const col=mix(mul*T[it*NP+ip]/scale,o[3]);img.data[4*p]=col[0];img.data[4*p+1]=col[1];img.data[4*p+2]=col[2];img.data[4*p+3]=255}ctx.putImageData(img,0,0)})}
const ov=document.getElementById('ov'),NS='http://www.w3.org/2000/svg';
const E=(n,a,t)=>{const el=document.createElementNS(NS,n);for(const k in a)el.setAttribute(k,a[k]);if(t!==undefined)el.textContent=t;return el};
function drawSVG(){ov.innerHTML='';const c=D.funcs[fi].c,odd=D.odd;
ov.appendChild(E('text',{x:115,y:30,'text-anchor':'middle',class:'th'},fi===0?'Network output f':'One hidden neuron'));
ov.appendChild(E('text',{x:340,y:30,'text-anchor':'middle',class:'th'},`Kept: degree ≤ ${K}`));
ov.appendChild(E('text',{x:565,y:30,'text-anchor':'middle',class:'th'},`Difference × ${dmul.toLocaleString()}`));
ov.appendChild(E('text',{x:115,y:232,'text-anchor':'middle',class:'ts'},D.funcs[fi].name));
ov.appendChild(E('text',{x:340,y:232,'text-anchor':'middle',class:'ts'},`${(K+1)*(K+1)} harmonics (${(K+1)*(K+2)/2} odd ones used)`));
ov.appendChild(E('text',{x:565,y:232,'text-anchor':'middle',class:'ts'},`max error ${(100*stats.maxerr).toFixed(2)}% of max |f|`));
const X0=70,XW=560,Y0=270,YH=120,lx=l=>X0+XW*(l-1)/(KM-1),ly=v=>Y0+YH*Math.min(1,-Math.log10(Math.max(v,1e-12))/10);
ov.appendChild(E('text',{x:40,y:258,class:'th'},`Energy per degree: this function and all ${D.n.toLocaleString()} neurons`));
ov.appendChild(E('rect',{x:lx(K)+XW/(KM-1),y:Y0,width:Math.max(0,X0+XW-lx(K)-XW/(KM-1)),height:YH,fill:'#888780',opacity:0.08}));
let band='M'+odd.map((l,i)=>lx(l).toFixed(1)+' '+ly(D.p95[i]).toFixed(1)).join('L')+'L'+odd.slice().reverse().map((l,i)=>lx(l).toFixed(1)+' '+ly(D.p5[odd.length-1-i]).toFixed(1)).join('L')+'Z';
ov.appendChild(E('path',{d:band,fill:'#888780',opacity:0.2,stroke:'none'}));
ov.appendChild(E('path',{d:'M'+odd.map((l,i)=>lx(l).toFixed(1)+' '+ly(D.p50[i]).toFixed(1)).join('L'),fill:'none',stroke:'#888780','stroke-width':1.2,'stroke-dasharray':'4 3'}));
const tot=c.reduce((s,v)=>s+v*v,0),ef=odd.map(l=>c.reduce((s,v,j)=>s+(deg[j]===l?v*v:0),0)/tot);
ov.appendChild(E('path',{d:'M'+odd.map((l,i)=>lx(l).toFixed(1)+' '+ly(ef[i]).toFixed(1)).join('L'),fill:'none',stroke:'#1baf7a','stroke-width':2.2}));
odd.forEach((l,i)=>ov.appendChild(E('circle',{cx:lx(l),cy:ly(ef[i]),r:3,fill:'#1baf7a',opacity:l<=K?1:0.4})));
ov.appendChild(E('line',{x1:lx(K)+XW/(KM-1),y1:Y0,x2:lx(K)+XW/(KM-1),y2:Y0+YH,stroke:'var(--p)','stroke-width':1.2,'stroke-dasharray':'4 3'}));
ov.appendChild(E('line',{x1:X0,y1:Y0+YH,x2:X0+XW,y2:Y0+YH,stroke:'var(--b)','stroke-width':0.5}));ov.appendChild(E('line',{x1:X0,y1:Y0,x2:X0,y2:Y0+YH,stroke:'var(--b)','stroke-width':0.5}));
odd.filter(l=>l%4===1||l===KM).forEach(l=>ov.appendChild(E('text',{x:lx(l),y:Y0+YH+15,'text-anchor':'middle',class:'ts'},l)));
[[1,'1'],[1e-5,'1e-5'],[1e-10,'1e-10']].forEach(([v,s])=>ov.appendChild(E('text',{x:X0-6,y:ly(v)+4,'text-anchor':'end',class:'ts'},s)));
ov.appendChild(E('text',{x:X0+XW,y:Y0+YH+32,'text-anchor':'end',class:'ts'},'degree k (odd only: tanh is odd and the network has no biases)'));
ov.appendChild(E('text',{x:X0+XW,y:Y0+14,'text-anchor':'end',class:'ts'},'gray: 5–95% of all neurons · dashed: median'));
document.getElementById('Kl').textContent='K = '+K;
document.getElementById('rd').textContent=`Energy beyond degree ${K}: this function ${(100*stats.lost).toFixed(3)}% · median neuron ${(100*D.lost50[(K-1)/2]).toFixed(3)}% · 95% of all ${D.n.toLocaleString()} neurons below ${(100*D.lost95[(K-1)/2]).toFixed(3)}%`}
function frame(ts){if(last===null)last=ts;const dt=Math.min(0.05,(ts-last)/1000);last=ts;if(run)rot+=0.35*dt;render();requestAnimationFrame(frame)}
document.getElementById('nx').onclick=()=>{fi=(fi+1)%D.funcs.length;rebuild()};
document.getElementById('Ks').oninput=e=>{K=+e.target.value;rebuild()};
document.getElementById('pp').onclick=ev=>{run=!run;ev.target.textContent=run?'Pause':'Play'};
rebuild();requestAnimationFrame(frame);
})();
</script>