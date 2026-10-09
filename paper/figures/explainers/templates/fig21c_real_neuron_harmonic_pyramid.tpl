<h2 class="sr-only">Figure 21c. Real functions from a trained network on the input sphere, turning; their spherical-harmonic coefficients light a pyramid of basis shapes and move only within each degree; one degree cutoff K captures them and every neuron of the layer.</h2>
<div style="font-size:15px;font-weight:500;color:var(--text-primary);margin:0 0 8px">Figure 21c · A real neuron, spelled in spherical harmonics</div>
<div id="ctl" style="display:flex;flex-wrap:wrap;align-items:center;gap:6px 8px;margin:0 0 6px;font-size:13px;color:var(--text-secondary)"></div>
<div style="display:flex;align-items:center;gap:10px;margin:0 0 6px;font-size:13px;color:var(--text-secondary)">
<button id="pp" style="font-size:13px;padding:4px 10px">Pause</button>
<span>Degree cutoff K</span><input type="range" id="Ks" min="1" max="13" step="2" value="5" style="flex:1"><span id="Kl" style="min-width:250px;text-align:right"></span>
</div>
<div style="position:relative;width:680px;height:440px">
<canvas id="c0" style="position:absolute;left:14px;top:46px;width:150px;height:150px"></canvas>
<canvas id="c1" style="position:absolute;left:14px;top:262px;width:150px;height:150px"></canvas>
<canvas id="cp" style="position:absolute;left:200px;top:40px;width:470px;height:210px"></canvas>
<svg id="ov" width="680" height="440" viewBox="0 0 680 440" style="position:absolute;left:0;top:0" role="img"><title>Figure 21c: a real neuron, spelled in spherical harmonics</title><desc>Two spheres: the turning function and its truncation to degree K; a pyramid of spherical harmonics lit by the function's coefficients; energy per degree for the function and for all neurons.</desc></svg>
</div>
<script>
(()=>{
const D=__DATA__;
const DPR=2,GN=[27,175,122],PU=[127,119,221],BASE=[236,234,228],KM=D.KM,ODD=D.odd;
const fac=n=>{let r=1;for(let i=2;i<=n;i++)r*=i;return r};
const NL=[];for(let l=0;l<=KM;l++){NL[l]=[];for(let m=0;m<=l;m++)NL[l][m]=Math.sqrt((2*l+1)/(4*Math.PI)*fac(l-m)/fac(l+m))}
function plmAll(x){const s=Math.sqrt(Math.max(0,1-x*x)),P=[];for(let m=0;m<=KM;m++){P[m]=new Float64Array(KM+1);let pmm=1,f=1;for(let i=1;i<=m;i++){pmm*=-f*s;f+=2}P[m][m]=pmm;if(m<KM)P[m][m+1]=x*(2*m+1)*pmm;for(let l=m+2;l<=KM;l++)P[m][l]=((2*l-1)*x*P[m][l-1]-(l+m-1)*P[m][l-2])/(l-m)}return P}
const deg=[],mm=[];ODD.forEach(l=>{for(let m=-l;m<=l;m++){deg.push(l);mm.push(m)}});const NC=deg.length;
function Yvec(p,out){const ct=Math.max(-1,Math.min(1,p[2])),ph=Math.atan2(p[1],p[0]),P=plmAll(ct);for(let c=0;c<NC;c++){const l=deg[c],m=mm[c],am=Math.abs(m),b=NL[l][am]*P[am][l];out[c]=m===0?b:m>0?Math.SQRT2*b*Math.cos(am*ph):Math.SQRT2*b*Math.sin(am*ph)}return out}
const gl=n=>{const X=[],W=[];for(let i=1;i<=n;i++){let x=Math.cos(Math.PI*(i-0.25)/(n+0.5)),dp=1;for(let it=0;it<60;it++){let p0=1,p1=x;for(let k=2;k<=n;k++){const p2=((2*k-1)*x*p1-(k-1)*p0)/k;p0=p1;p1=p2}dp=n*(x*p1-p0)/(x*x-1);const d=p1/dp;x-=d;if(Math.abs(d)<1e-15)break}X.push(x);W.push(2/((1-x*x)*dp*dp))}return [X,W]};
const [gx,gw]=gl(16),NPh=32,QP=[],QW=[];gx.forEach((x,i)=>{const s=Math.sqrt(1-x*x);for(let k=0;k<NPh;k++){const ph=2*Math.PI*k/NPh;QP.push([s*Math.cos(ph),s*Math.sin(ph),x]);QW.push(gw[i]*2*Math.PI/NPh)}});
const YQ=QP.map(p=>Yvec(p,new Float64Array(NC)));
const NT=64,NPt=128,TP=[];for(let i=0;i<NT;i++){const th=Math.PI*(i+0.5)/NT;for(let k=0;k<NPt;k++){const ph=2*Math.PI*(k+0.5)/NPt;TP.push([Math.sin(th)*Math.cos(ph),Math.sin(th)*Math.sin(ph),Math.cos(th)])}}
const YT=TP.map(p=>Yvec(p,new Float32Array(NC)));
const e=0.35,toW=(x,y,z)=>[x,-y*Math.sin(e)+z*Math.cos(e),y*Math.cos(e)+z*Math.sin(e)],LV=[-0.4,0.55,0.73];
const SS=150*DPR,PIX=[];for(let j=0;j<SS;j++)for(let i=0;i<SS;i++){const x=2*(i+0.5)/SS-1,y=1-2*(j+0.5)/SS,q=x*x+y*y;if(q>1){PIX.push(null);continue}const z=Math.sqrt(1-q),w=toW(x,y,z);const u=Math.acos(Math.max(-1,Math.min(1,w[2])))/Math.PI*NT-0.5,v=((Math.atan2(w[1],w[0])+2*Math.PI)%(2*Math.PI))/(2*Math.PI)*NPt-0.5;let i0=Math.floor(u),j0=Math.floor(v);const fu=u-i0,fv=v-j0;const i1=Math.min(NT-1,i0+1);i0=Math.max(0,i0);const j1=(j0+1+NPt)%NPt;j0=(j0+NPt)%NPt;PIX.push([i0*NPt+j0,i0*NPt+j1,i1*NPt+j0,i1*NPt+j1,(1-fu)*(1-fv),(1-fu)*fv,fu*(1-fv),fu*fv,0.6+0.4*Math.max(0,x*LV[0]+y*LV[1]+z*LV[2])])}
const mix=(v,sh)=>{const a=Math.max(-1,Math.min(1,v)),m=Math.abs(a),c=a>=0?GN:PU;return BASE.map((b,i)=>Math.round((b+(c[i]-b)*m)*sh))};
const cvs=['c0','c1'].map(id=>{const c=document.getElementById(id);c.width=c.height=SS;const ctx=c.getContext('2d');return {ctx,img:ctx.createImageData(SS,SS)}});
const IS=24*DPR,icons=[];for(let c=0;c<NC;c++){if(deg[c]>7){icons.push(null);continue}let mx=0;const vals=[];for(let j=0;j<IS;j++)for(let i=0;i<IS;i++){const x=2*(i+0.5)/IS-1,y=1-2*(j+0.5)/IS,q=x*x+y*y;if(q>1){vals.push(null);continue}const z=Math.sqrt(1-q),yv=Yvec(toW(x,y,z),new Float64Array(NC))[c];mx=Math.max(mx,Math.abs(yv));vals.push([yv,0.62+0.38*Math.max(0,x*LV[0]+y*LV[1]+z*LV[2])])}
icons.push([1,-1].map(sg=>{const cv=document.createElement('canvas');cv.width=cv.height=IS;const ctx=cv.getContext('2d'),im=ctx.createImageData(IS,IS);vals.forEach((o,k)=>{if(!o)return;const col=mix(sg*o[0]/mx,o[1]);im.data[4*k]=col[0];im.data[4*k+1]=col[1];im.data[4*k+2]=col[2];im.data[4*k+3]=255});ctx.putImageData(im,0,0);return cv}))}
const cp=document.getElementById('cp');cp.width=470*DPR;cp.height=210*DPR;const pctx=cp.getContext('2d');
const ov=document.getElementById('ov'),NS='http://www.w3.org/2000/svg',E=(n,a,t)=>{const el=document.createElementNS(NS,n);for(const k in a)el.setAttribute(k,a[k]);if(t!==undefined)el.textContent=t;return el};
let fi=1,K=5,T=0,run=true,last=null,c0=null,El=null,scale=1;
const ctl=document.getElementById('ctl');ctl.appendChild(Object.assign(document.createElement('span'),{textContent:'Function'}));
const fb=D.funcs.map((f,k)=>{const b=document.createElement('button');b.textContent=['output f','neuron A','neuron B','neuron C','ridge'][k];b.style.cssText='font-size:13px;padding:3px 9px';b.onclick=()=>{fi=k;setF()};ctl.appendChild(b);return b});
const rowY=r=>22+r*50,colX=(l,m)=>215+m*26;
function setF(){c0=Float64Array.from(D.funcs[fi].c);El=ODD.map(l=>c0.reduce((s,v,c)=>s+(deg[c]===l?v*v:0),0));scale=0;TP.forEach((p,g)=>{let s=0;for(let c=0;c<NC;c++)s+=c0[c]*YT[g][c];scale=Math.max(scale,Math.abs(s))});
fb.forEach((b,k)=>{b.style.borderColor=k===fi?'#2a78d6':'';b.style.color=k===fi?'#2a78d6':''});drawSVG()}
const R=a=>{const ax=[0.35,0.55,0.76],n=Math.hypot(...ax),[x,y,z]=ax.map(v=>v/n),c=Math.cos(a),s=Math.sin(a),C=1-c;return [[c+x*x*C,x*y*C-z*s,x*z*C+y*s],[y*x*C+z*s,c+y*y*C,y*z*C-x*s],[z*x*C-y*s,z*y*C+x*s,c+z*z*C]]};
const tmp=new Float64Array(NC);
function frame(ts){if(last===null)last=ts;const dt=Math.min(0.05,(ts-last)/1000);last=ts;if(run)T+=dt;
const M=R(0.5*T),cr=new Float64Array(NC);
for(let q=0;q<QP.length;q++){const p=QP[q],pr=[M[0][0]*p[0]+M[1][0]*p[1]+M[2][0]*p[2],M[0][1]*p[0]+M[1][1]*p[1]+M[2][1]*p[2],M[0][2]*p[0]+M[1][2]*p[1]+M[2][2]*p[2]];Yvec(pr,tmp);let f=0;for(let c=0;c<NC;c++)f+=c0[c]*tmp[c];const wf=QW[q]*f,yq=YQ[q];for(let c=0;c<NC;c++)cr[c]+=wf*yq[c]}
const Tf=new Float32Array(TP.length),Tc=new Float32Array(TP.length);for(let g=0;g<TP.length;g++){const y=YT[g];let a=0,b=0;for(let c=0;c<NC;c++){const v=cr[c]*y[c];a+=v;if(deg[c]<=K)b+=v}Tf[g]=a;Tc[g]=b}
[Tf,Tc].forEach((T2,k)=>{const {ctx,img}=cvs[k];for(let p=0;p<PIX.length;p++){const o=PIX[p];if(!o){img.data[4*p+3]=0;continue}const val=o[4]*T2[o[0]]+o[5]*T2[o[1]]+o[6]*T2[o[2]]+o[7]*T2[o[3]],col=mix(val/scale,o[8]);img.data[4*p]=col[0];img.data[4*p+1]=col[1];img.data[4*p+2]=col[2];img.data[4*p+3]=255}ctx.putImageData(img,0,0)});
pctx.clearRect(0,0,cp.width,cp.height);for(let c=0;c<NC;c++){const l=deg[c];if(l>7)continue;const r=(l-1)/2,El_=El[r]||1e-30,a=Math.min(1,Math.abs(cr[c])/Math.sqrt(El_));pctx.globalAlpha=(l<=K?1:0.22)*Math.max(0.05,a);pctx.drawImage(icons[c][cr[c]>=0?0:1],(colX(l,mm[c])-12)*DPR,(rowY(r)-12)*DPR,IS,IS)}pctx.globalAlpha=1;
requestAnimationFrame(frame)}
function drawSVG(){ov.innerHTML='';const tot=El.reduce((a,b)=>a+b,0);
ov.appendChild(E('text',{x:89,y:36,'text-anchor':'middle',class:'th'},'Turning function'));ov.appendChild(E('text',{x:89,y:252,'text-anchor':'middle',class:'th'},`Kept: degree ≤ ${K}`));
ov.appendChild(E('text',{x:435,y:24,'text-anchor':'middle',class:'th'},'Its harmonics, lit by its coefficients'));
[1,3,5,7].forEach((l,r)=>{const y=40+rowY(r);ov.appendChild(E('text',{x:200+colX(l,-l)-48,y:y+4,class:'ts'},'ℓ = '+l));const pc=100*El[r]/tot;ov.appendChild(E('text',{x:200+colX(l,l)+18,y:y+4,class:'ts'},(pc<0.1?pc.toFixed(2):pc.toFixed(1))+'%'))});
if(K<7)ov.appendChild(E('line',{x1:186,x2:676,y1:40+rowY((K+1)/2-0.5),y2:40+rowY((K+1)/2-0.5),stroke:'#888780','stroke-width':1,'stroke-dasharray':'4 3'}));
const X0=230,XW=400,Y0=292,YH=110,lx=l=>X0+XW*(l-1)/(KM-1),ly=v=>Y0+YH*Math.min(1,-Math.log10(Math.max(v,1e-8))/7);
ov.appendChild(E('text',{x:200,y:280,class:'th'},`Energy per degree, this function and all ${D.n.toLocaleString()} layer-2 neurons`));
ov.appendChild(E('path',{d:'M'+ODD.map((l,i)=>lx(l).toFixed(1)+' '+ly(D.p95[i]).toFixed(1)).join('L')+'L'+ODD.slice().reverse().map((l,i)=>lx(l).toFixed(1)+' '+ly(D.p5[ODD.length-1-i]).toFixed(1)).join('L')+'Z',fill:'#888780',opacity:0.2,stroke:'none'}));
ov.appendChild(E('path',{d:'M'+ODD.map((l,i)=>lx(l).toFixed(1)+' '+ly(D.p50[i]).toFixed(1)).join('L'),fill:'none',stroke:'#888780','stroke-width':1.2,'stroke-dasharray':'4 3'}));
ov.appendChild(E('path',{d:'M'+ODD.map((l,i)=>lx(l).toFixed(1)+' '+ly(El[i]/tot).toFixed(1)).join('L'),fill:'none',stroke:'#1baf7a','stroke-width':2.2}));
ODD.forEach((l,i)=>ov.appendChild(E('circle',{cx:lx(l),cy:ly(El[i]/tot),r:3,fill:'#1baf7a',opacity:l<=K?1:0.35})));
ov.appendChild(E('line',{x1:lx(K)+XW/(KM-1),y1:Y0,x2:lx(K)+XW/(KM-1),y2:Y0+YH,stroke:'var(--p)','stroke-width':1.2,'stroke-dasharray':'4 3'}));
ov.appendChild(E('line',{x1:X0,y1:Y0+YH,x2:X0+XW,y2:Y0+YH,stroke:'var(--b)','stroke-width':0.5}));ov.appendChild(E('line',{x1:X0,y1:Y0,x2:X0,y2:Y0+YH,stroke:'var(--b)','stroke-width':0.5}));
ODD.forEach(l=>ov.appendChild(E('text',{x:lx(l),y:Y0+YH+15,'text-anchor':'middle',class:'ts'},l)));
[[1,'1'],[1e-4,'1e-4'],[1e-7,'1e-7']].forEach(([v,s])=>ov.appendChild(E('text',{x:X0-6,y:ly(v)+4,'text-anchor':'end',class:'ts'},s)));
ov.appendChild(E('text',{x:X0+XW,y:Y0+10,'text-anchor':'end',class:'ts'},'band: 5–95% of all neurons'));
ov.appendChild(E('text',{x:89,y:430,'text-anchor':'middle',class:'ts'},D.funcs[fi].name.split(' (')[0]));
const lost=El.reduce((s,v,i)=>s+(ODD[i]>K?v:0),0)/tot;
document.getElementById('Kl').textContent=`K = ${K}: ${(K+1)*(K+2)/2} odd harmonics · energy beyond K ${(100*lost).toFixed(2)}%`}
document.getElementById('Ks').oninput=e=>{K=+e.target.value;drawSVG()};
document.getElementById('pp').onclick=ev=>{run=!run;ev.target.textContent=run?'Pause':'Play'};
setF();requestAnimationFrame(frame);
})();
</script>