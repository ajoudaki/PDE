<h2 class="sr-only">Figure 20. Rotated petals share one spectrum, so all n neurons live in a few Fourier directions; selecting about twice that many neurons with a metric reproduces the kernel of all n neurons, while the same number of random neurons does not.</h2>
<div style="font-size:15px;font-weight:500;color:var(--text-primary);margin:0 0 8px">Figure 20 · Rotated petals, tied back to selection</div>
<div style="display:flex;align-items:center;gap:10px;margin:0 0 6px;font-size:13px;color:var(--text-secondary)">
<span>Width n</span><input type="range" id="ns" min="7" max="13" step="1" value="11" style="flex:1">
<span id="nl" style="min-width:300px;text-align:right"></span>
</div>
<svg id="sv" width="100%" viewBox="0 0 680 580" role="img"><title>Figure 20: rotated petals, tied back to selection</title><desc>Petals of neurons with selected neurons marked; one shared spectrum with cutoff J; the kernel of all n neurons against q random and q selected neurons; directions versus width.</desc></svg>
<script>
(()=>{
const svg=document.getElementById('sv'),GN='#1baf7a',OR='#D85A30',GR='#888780';
const E=(n,a,t)=>{const e=document.createElementNS('http://www.w3.org/2000/svg',n);for(const k in a)e.setAttribute(k,a[k]);if(t!==undefined)e.textContent=t;return e};
const JX=70,RG=Array.from({length:221},(_,i)=>i*0.03);
const specR=r=>{const M=512,a=[];for(let j=0;j<=JX;j++){let s=0;for(let k=0;k<M;k++){const th=2*Math.PI*k/M;s+=Math.tanh(r*Math.cos(th))*Math.cos(j*th)}a.push(2*s/M)}return a};
const TAB=RG.map(specR);
const coefAt=(r,j)=>{const x=Math.min(r/0.03,RG.length-1.001),i=Math.floor(x),f=x-i;return TAB[i][j]*(1-f)+TAB[i+1][j]*f};
const Jneed=(r,eps)=>{let tail=0;for(let j=JX;j>=0;j--){tail+=Math.abs(coefAt(r,j));if(tail>eps)return j}return 0};
const dirsOf=J=>2*Math.ceil((J+1)/2);
const KA=256,TH=Array.from({length:KA},(_,k)=>-Math.PI+2*Math.PI*k/KA);
function build(n){let s=11;const rnd=()=>{s=(s*16807)%2147483647;return s/2147483647};
const r=new Float64Array(n),ph=new Float64Array(n);for(let i=0;i<n;i++){r[i]=Math.sqrt(-2*Math.log(rnd()+1e-12));ph[i]=2*Math.PI*rnd()}
const rmax=Math.max(...r),J=Jneed(rmax,1/n),modes=[];for(let j=1;j<=J;j+=2)modes.push(j);
const k=2*modes.length,U=Array.from({length:k},()=>new Float64Array(n));
modes.forEach((j,m)=>{for(let i=0;i<n;i++){const a=coefAt(r[i],j);U[2*m][i]=a*Math.cos(j*ph[i]);U[2*m+1][i]=a*Math.sin(j*ph[i])}});
const keep=[];for(let c=0;c<k;c++){const v=U[c];for(const p of keep){let d=0;for(let i=0;i<n;i++)d+=v[i]*p[i];d/=n;for(let i=0;i<n;i++)v[i]-=d*p[i]}let nn=0;for(let i=0;i<n;i++)nn+=v[i]*v[i];nn=Math.sqrt(nn/n);if(nn>1e-9){for(let i=0;i<n;i++)v[i]/=nn;keep.push(v)}}
const kk=keep.length,row=i=>keep.map(c=>c[i]);
const sel=[];for(let pass=0;pass<2;pass++){const R=Array.from({length:n},(_,i)=>row(i));for(let t=0;t<kk;t++){let bi=-1,bv=-1;for(let i=0;i<n;i++){if(sel.includes(i))continue;let s2=0;for(const x of R[i])s2+=x*x;if(s2>bv){bv=s2;bi=i}}
sel.push(bi);const nv=Math.sqrt(bv),v=R[bi].map(x=>x/nv);for(let i=0;i<n;i++){let d=0;for(let c=0;c<kk;c++)d+=R[i][c]*v[c];for(let c=0;c<kk;c++)R[i][c]-=d*v[c]}}}
const q=sel.length,UI=sel.map(row),G=Array.from({length:kk},(_,a)=>Array.from({length:kk},(_,b)=>UI.reduce((s,ro)=>s+ro[a]*ro[b],0)));
const L=G.map(r=>r.map(()=>0));for(let a=0;a<kk;a++)for(let b=0;b<=a;b++){let s=G[a][b];for(let c=0;c<b;c++)s-=L[a][c]*L[b][c];L[a][b]=a===b?Math.sqrt(Math.max(s,1e-300)):s/L[b][b]}
const solve=y=>{const z=y.slice();for(let a=0;a<kk;a++){for(let c=0;c<a;c++)z[a]-=L[a][c]*z[c];z[a]/=L[a][a]}for(let a=kk-1;a>=0;a--){for(let c=a+1;c<kk;c++)z[a]-=L[c][a]*z[c];z[a]/=L[a][a]}return z};
const hv=(i,th)=>Math.tanh(r[i]*Math.cos(th-ph[i]));
const h0=sel.map(i=>hv(i,0)),av=Array.from({length:kk},(_,c)=>UI.reduce((s,ro,t)=>s+ro[c]*h0[t],0)),bv=solve(solve(av)),v0=UI.map(ro=>ro.reduce((s,x,c)=>s+x*bv[c],0));
const Kd=TH.map(th=>{let s=0;for(let i=0;i<n;i++)s+=hv(i,th)*hv(i,0);return s/n});
const Ks=TH.map(th=>sel.reduce((s,i,t)=>s+hv(i,th)*v0[t],0));
let sr=7+n;const rr=()=>{sr=(sr*16807)%2147483647;return sr/2147483647};const iid=[];while(iid.length<q){const i=Math.floor(rr()*n);if(!iid.includes(i))iid.push(i)}
const Ki=TH.map(th=>iid.reduce((s,i)=>s+hv(i,th)*hv(i,0),0)/q);
const km=Math.max(...Kd.map(Math.abs)),er=A=>Math.max(...A.map((v,t)=>Math.abs(v-Kd[t])))/km;
return {n,r,ph,rmax,J,k:kk,q,sel,Kd,Ks,Ki,es:er(Ks),ei:er(Ki)}}
const cache={},curve=[];for(let p=7;p<=24;p++){const n=2**p,J=Jneed(Math.sqrt(2*Math.log(n)),1/n);curve.push([n,dirsOf(J)])}
const petals=(()=>{let s=5;const rnd=()=>{s=(s*16807)%2147483647;return s/2147483647};return Array.from({length:12},()=>[Math.sqrt(-2*Math.log(rnd()+1e-12)),2*Math.PI*rnd()])})();
function draw(){const p=+document.getElementById('ns').value,n=2**p,D=cache[p]||(cache[p]=build(n));svg.innerHTML='';
document.getElementById('nl').textContent=`n = ${n.toLocaleString()} → ${D.k} directions, ${D.q} selected neurons`;
svg.appendChild(E('text',{x:40,y:22,class:'th'},'Neurons: rotated petals'));
const cx=170,cy=150,R0=52,sc=30;svg.appendChild(E('circle',{cx,cy,r:R0,fill:'none',stroke:'var(--b)','stroke-width':0.5,'stroke-dasharray':'3 3'}));
const pet=(rr,pp,col,w,op)=>{let d='';for(let k=0;k<=180;k++){const th=2*Math.PI*k/180,R=R0+sc*Math.tanh(rr*Math.cos(th-pp));d+=(k?'L':'M')+(cx+R*Math.cos(th)).toFixed(1)+' '+(cy-R*Math.sin(th)).toFixed(1)}svg.appendChild(E('path',{d,fill:'none',stroke:col,'stroke-width':w,opacity:op}))};
petals.forEach(([rr,pp])=>pet(rr,pp,GR,0.8,0.45));
D.sel.slice(0,8).forEach(i=>pet(D.r[i],D.ph[i],GN,1.1,0.85));
const im=D.r.indexOf(D.rmax);pet(D.rmax,D.ph[im],OR,1.8,1);
D.sel.forEach(i=>{const R=R0+sc+12,a=D.ph[i];svg.appendChild(E('circle',{cx:(cx+R*Math.cos(a)).toFixed(1),cy:(cy-R*Math.sin(a)).toFixed(1),r:2.4,fill:GN}))});
svg.appendChild(E('text',{x:cx,y:268,'text-anchor':'middle',class:'ts'},'gray: random · green: selected · orange: sharpest'));
const X0=390,Y0=40,PW=250,PH=190,jm=50,lmin=-10,yv=v=>Y0+PH*(Math.max(Math.log10(Math.abs(v)+1e-300),lmin)/lmin),xv=j=>X0+PW*j/jm;
svg.appendChild(E('text',{x:X0,y:22,class:'th'},'One shared spectrum'));
svg.appendChild(E('line',{x1:X0,y1:Y0+PH,x2:X0+PW,y2:Y0+PH,stroke:'var(--b)','stroke-width':0.5}));svg.appendChild(E('line',{x1:X0,y1:Y0,x2:X0,y2:Y0+PH,stroke:'var(--b)','stroke-width':0.5}));
[[1.0,GR,0.9],[1.7,GR,0.9],[D.rmax,OR,1.8]].forEach(([r,c,w])=>{let d='',f=true;for(let j=1;j<=jm;j+=2){const v=coefAt(r,j);if(Math.abs(v)<1e-10)continue;d+=(f?'M':'L')+xv(j).toFixed(1)+' '+yv(v).toFixed(1);f=false}svg.appendChild(E('path',{d,fill:'none',stroke:c,'stroke-width':w}))});
svg.appendChild(E('line',{x1:X0,y1:yv(1/n),x2:X0+PW,y2:yv(1/n),stroke:'var(--s)','stroke-width':0.8,'stroke-dasharray':'4 3'}));
svg.appendChild(E('text',{x:X0+PW-2,y:yv(1/n)-5,'text-anchor':'end',class:'ts'},'accuracy 1/n'));
svg.appendChild(E('line',{x1:xv(D.J),y1:Y0,x2:xv(D.J),y2:Y0+PH,stroke:OR,'stroke-width':0.8,'stroke-dasharray':'2 3'}));
svg.appendChild(E('text',{x:xv(D.J)+5,y:Y0+12,class:'ts'},`J = ${D.J}`));
svg.appendChild(E('text',{x:X0+PW/2,y:Y0+PH+18,'text-anchor':'middle',class:'ts'},'frequency j; orange: sharpest neuron'));
const KX=60,KY=316,KW=270,KH=100,kx=t=>KX+KW*(TH[t]+Math.PI)/(2*Math.PI),km=Math.max(...D.Kd.map(Math.abs))*1.25,ky=v=>KY+KH/2-KH/2*v/km;
svg.appendChild(E('text',{x:40,y:300,class:'th'},'Kernel of all n neurons, rebuilt from q'));
svg.appendChild(E('line',{x1:KX,y1:ky(0),x2:KX+KW,y2:ky(0),stroke:'var(--b)','stroke-width':0.5}));
const pl=(A,c,w,da,op)=>{let d='';A.forEach((v,t)=>{d+=(t?'L':'M')+kx(t).toFixed(1)+' '+ky(v).toFixed(1)});svg.appendChild(E('path',{d,fill:'none',stroke:c,'stroke-width':w,'stroke-dasharray':da,opacity:op}))};
pl(D.Kd,'var(--p)',5,'none',0.18);pl(D.Ki,'var(--s)',1.2,'none',1);pl(D.Ks,GN,2,'5 3',1);
const DY=KY+KH+30,DH=40,dm=Math.max(...D.Ki.map((v,t)=>Math.abs(v-D.Kd[t])))*1.1,dy=v=>DY-DH/2*v/dm;
svg.appendChild(E('line',{x1:KX,y1:DY,x2:KX+KW,y2:DY,stroke:'var(--b)','stroke-width':0.5}));
svg.appendChild(E('text',{x:KX,y:KY+KH+6,class:'ts'},'difference from all n'));
const pd=(A,c,w,da)=>{let d='';A.forEach((v,t)=>{d+=(t?'L':'M')+kx(t).toFixed(1)+' '+dy(v-D.Kd[t]).toFixed(1)});svg.appendChild(E('path',{d,fill:'none',stroke:c,'stroke-width':w,'stroke-dasharray':da}))};
pd(D.Ki,'var(--s)',1.2,'none');pd(D.Ks,GN,2,'none');
svg.appendChild(E('text',{x:KX,y:DY+DH/2+16,class:'ts'},'angle between two inputs, −π to π'));
const lg=[['var(--p)',0.25,5,'none','all n neurons'],['var(--s)',1,1.2,'none',`${D.q} random: error ${(100*D.ei).toFixed(0)}%`],[GN,1,2,'5 3',`${D.q} selected + metric: ${(100*D.es).toFixed(2)}%`]];
lg.forEach(([c,op,w,da,t],k)=>{const y=DY+DH/2+36+k*17;svg.appendChild(E('line',{x1:KX,y1:y-4,x2:KX+22,y2:y-4,stroke:c,'stroke-width':w,opacity:op,'stroke-dasharray':da}));svg.appendChild(E('text',{x:KX+30,y,class:'ts'},t))});
const AX=390,AY=318,AW=250,AH=150,lx=v=>AX+AW*(Math.log2(v)-7)/17,ly=v=>AY+AH*(1-Math.log2(v)/24);
svg.appendChild(E('text',{x:AX,y:300,class:'th'},'Directions versus width'));
svg.appendChild(E('line',{x1:AX,y1:AY+AH,x2:AX+AW,y2:AY+AH,stroke:'var(--b)','stroke-width':0.5}));svg.appendChild(E('line',{x1:AX,y1:AY,x2:AX,y2:AY+AH,stroke:'var(--b)','stroke-width':0.5}));
let dn='';curve.forEach(([n2],i)=>{dn+=(i?'L':'M')+lx(n2).toFixed(1)+' '+ly(n2).toFixed(1)});svg.appendChild(E('path',{d:dn,fill:'none',stroke:GR,'stroke-width':1,'stroke-dasharray':'4 3'}));
svg.appendChild(E('text',{x:lx(2**15),y:ly(2**15)-8,'text-anchor':'end',class:'ts'},'n neurons'));
let dc='';curve.forEach(([n2,v],i)=>{dc+=(i?'L':'M')+lx(n2).toFixed(1)+' '+ly(v).toFixed(1)});svg.appendChild(E('path',{d:dc,fill:'none',stroke:GN,'stroke-width':2}));
svg.appendChild(E('circle',{cx:lx(n),cy:ly(D.k),r:4.5,fill:GN}));
svg.appendChild(E('text',{x:AX+AW,y:ly(curve[curve.length-1][1])-10,'text-anchor':'end',class:'ts'},'directions ~ polylog n'));
[[7,'128'],[13,'8k'],[18,'262k'],[24,'16M']].forEach(([e,s])=>svg.appendChild(E('text',{x:lx(2**e),y:AY+AH+18,'text-anchor':'middle',class:'ts'},s)));
svg.appendChild(E('text',{x:AX,y:AY+AH+38,class:'ts'},'width n (log); both axes log'))}
document.getElementById('ns').oninput=draw;draw();
})();
</script>