<h2 class="sr-only">Figure 17. The weight is a grid of pairings between modes of the backward and forward histories; orthogonality empties every cross block, so truncation loses only the dropped-times-dropped corner.</h2>
<div style="font-size:15px;font-weight:500;color:var(--text-primary);margin:0 0 8px">Figure 17 · Only like pairs with like</div>
<div style="display:flex;align-items:center;gap:10px;margin:0 0 6px;font-size:13px;color:var(--text-secondary)">
<span>Moments q</span><input type="range" id="qs" min="1" max="14" step="1" value="5" style="flex:1">
<span id="ql" style="min-width:260px;text-align:right"></span>
</div>
<svg id="sv" width="100%" viewBox="0 0 680 370" role="img"><title>Figure 17: only like pairs with like</title><desc>A grid of mode pairings with only the diagonal nonzero; kept block, empty cross blocks, dropped corner; error versus q.</desc></svg>
<script>
(()=>{
const svg=document.getElementById('sv'),BL='#2a78d6',PU='#7F77DD',PD='#534AB7',GR='#888780';
const E=(n,a,t)=>{const e=document.createElementNS('http://www.w3.org/2000/svg',n);for(const k in a)e.setAttribute(k,a[k]);if(t!==undefined)e.textContent=t;return e};
const fh=s=>0.55*Math.tanh(4*(s-0.3))+0.45*Math.abs(s-0.65)-0.1,fb=s=>Math.exp(-2.5*s)*(1-1.4*Math.abs(s-0.22));
const gauss=n=>{const X=[],W=[];for(let i=1;i<=n;i++){let x=Math.cos(Math.PI*(i-0.25)/(n+0.5)),dp=1;for(let it=0;it<60;it++){let p0=1,p1=x;for(let k=2;k<=n;k++){const p2=((2*k-1)*x*p1-(k-1)*p0)/k;p0=p1;p1=p2}dp=n*(x*p1-p0)/(x*x-1);const dx=p1/dp;x-=dx;if(Math.abs(dx)<1e-15)break}X.push(x);W.push(2/((1-x*x)*dp*dp))}return [X,W]};
const [gX,gW]=gauss(220),cuts=[-1,-0.56,0.3,1],xs=[],ws=[];
for(let p=0;p<3;p++){const a=cuts[p],b=cuts[p+1];gX.forEach((x,k)=>{xs.push((a+b)/2+(b-a)/2*x);ws.push((b-a)/2*gW[k])})}
const JM=170,Fh=xs.map(x=>fh((x+1)/2)),Fb=xs.map(x=>fb((x+1)/2)),ch=[],cb=[];
let P0=xs.map(()=>1),P1=xs.slice();
const co=(F,P,j)=>{let s=0;for(let k=0;k<xs.length;k++)s+=ws[k]*F[k]*P[k];return (2*j+1)/2*s};
ch.push(co(Fh,P0,0),co(Fh,P1,1));cb.push(co(Fb,P0,0),co(Fb,P1,1));
for(let j=1;j<JM-1;j++){const P2=xs.map((x,k)=>((2*j+1)*x*P1[k]-j*P0[k])/(j+1));P0=P1;P1=P2;ch.push(co(Fh,P1,j+1));cb.push(co(Fb,P1,j+1))}
const cell=j=>cb[j]*ch[j]/(2*j+1);
const tail=(c,q)=>{let s=0;for(let j=q;j<c.length;j++)s+=c[j]*c[j]/(2*j+1);return Math.sqrt(s)};
const pair=q=>{let s=0;for(let j=q;j<JM;j++)s+=cell(j);return Math.abs(s)};
const QS=Array.from({length:40},(_,i)=>i+1),TH=QS.map(q=>tail(ch,q)),TB=QS.map(q=>tail(cb,q)),PA=QS.map(pair),PT=QS.map((q,i)=>TH[i]*TB[i]);
const G=14,cs=18,gx=96,gy=62,cmax=Math.max(...Array.from({length:G},(_,j)=>Math.abs(cell(j))));
function draw(){const q=+document.getElementById('qs').value;svg.innerHTML='';
svg.appendChild(E('text',{x:40,y:22,class:'th'},'∫ b hᵀ as a grid of mode pairings'));
svg.appendChild(E('text',{x:gx,y:gy-24,class:'ts'},'forward history h, mode j →'));
svg.appendChild(E('text',{x:40,y:gy+8,class:'ts'},'b, i ↓'));
const W=G*cs,k=Math.min(q,G)*cs;
svg.appendChild(E('rect',{x:gx,y:gy,width:k,height:k,fill:BL,opacity:0.14}));
if(q<G)svg.appendChild(E('rect',{x:gx+k,y:gy+k,width:W-k,height:W-k,fill:PU,opacity:0.16}));
svg.appendChild(E('rect',{x:gx,y:gy,width:W,height:W,fill:'none',stroke:'var(--b)','stroke-width':0.5}));
if(q<G){svg.appendChild(E('line',{x1:gx+k,y1:gy,x2:gx+k,y2:gy+W,stroke:GR,'stroke-width':0.8,'stroke-dasharray':'3 3'}));svg.appendChild(E('line',{x1:gx,y1:gy+k,x2:gx+W,y2:gy+k,stroke:GR,'stroke-width':0.8,'stroke-dasharray':'3 3'}))}
for(let i=0;i<G;i++){svg.appendChild(E('text',{x:gx-8,y:gy+i*cs+cs/2+4,'text-anchor':'end',class:'ts'},i));svg.appendChild(E('text',{x:gx+i*cs+cs/2,y:gy-6,'text-anchor':'middle',class:'ts'},i));
for(let j=0;j<G;j++){const cx=gx+j*cs+cs/2,cy=gy+i*cs+cs/2;if(i!==j){svg.appendChild(E('circle',{cx,cy,r:0.9,fill:GR,opacity:0.5}));continue}
const v=cell(i),r=Math.max(1.2,(cs/2-1)*Math.sqrt(Math.abs(v)/cmax)),kept=i<q;svg.appendChild(E('circle',{cx,cy,r:r.toFixed(2),fill:kept?BL:PD,opacity:kept?0.95:0.85}))}}
const ly=gy+W+22;
svg.appendChild(E('rect',{x:gx,y:ly-10,width:12,height:12,fill:BL,opacity:0.3}));svg.appendChild(E('text',{x:gx+18,y:ly,class:'ts'},'kept × kept: stored'));
svg.appendChild(E('rect',{x:gx,y:ly+8,width:12,height:12,fill:'none',stroke:'var(--b)'}));svg.appendChild(E('text',{x:gx+18,y:ly+18,class:'ts'},'kept × dropped: exactly 0'));
svg.appendChild(E('rect',{x:gx+180,y:ly-10,width:12,height:12,fill:PU,opacity:0.35}));svg.appendChild(E('text',{x:gx+198,y:ly,class:'ts'},'dropped × dropped:'));svg.appendChild(E('text',{x:gx+198,y:ly+18,class:'ts'},'the whole error'));
const X0=430,PW=210,Y0=62,PH=230,lx=v=>X0+PW*Math.log10(v)/Math.log10(40),lo=-8,ly2=v=>Y0+PH*Math.min(1,Math.log10(Math.max(v,1e-12))/lo);
svg.appendChild(E('text',{x:X0,y:22,class:'th'},'Error versus q'));
svg.appendChild(E('line',{x1:X0,y1:Y0+PH,x2:X0+PW,y2:Y0+PH,stroke:'var(--b)','stroke-width':0.5}));svg.appendChild(E('line',{x1:X0,y1:Y0,x2:X0,y2:Y0+PH,stroke:'var(--b)','stroke-width':0.5}));
[[TH,BL,1.2,'none'],[TB,PU,1.2,'none'],[PT,PD,2.2,'none'],[PA,PD,0.9,'2 3']].forEach(([A,c,w,da])=>{let d='';A.forEach((v,i)=>{d+=(i?'L':'M')+lx(QS[i]).toFixed(1)+' '+ly2(v).toFixed(1)});svg.appendChild(E('path',{d,fill:'none',stroke:c,'stroke-width':w,'stroke-dasharray':da}))});
svg.appendChild(E('line',{x1:lx(q),y1:Y0,x2:lx(q),y2:Y0+PH,stroke:GR,'stroke-width':0.8,'stroke-dasharray':'2 3'}));
svg.appendChild(E('circle',{cx:lx(q),cy:ly2(PT[q-1]),r:4,fill:PD}));
svg.appendChild(E('text',{x:lx(14),y:ly2(TH[13])-12,class:'ts'},'one tail ~ 1/q'));
svg.appendChild(E('text',{x:X0+14,y:ly2(1e-6),class:'ts'},'tail × tail'));svg.appendChild(E('text',{x:X0+14,y:ly2(1e-6)+16,class:'ts'},'~ 1/q²'));
[1,10,40].forEach(v=>svg.appendChild(E('text',{x:lx(v),y:Y0+PH+16,'text-anchor':'middle',class:'ts'},v)));
[0,-2,-4,-6,-8].forEach(e=>svg.appendChild(E('text',{x:X0-6,y:ly2(Math.pow(10,e))+4,'text-anchor':'end',class:'ts'},e===0?'1':'1e'+e)));
svg.appendChild(E('text',{x:X0+PW/2,y:Y0+PH+34,'text-anchor':'middle',class:'ts'},'moments q (log)'));
document.getElementById('ql').textContent=`q = ${q}: tails ${TB[q-1].toExponential(0)} × ${TH[q-1].toExponential(0)}, product ${PT[q-1].toExponential(0)}`}
document.getElementById('qs').oninput=draw;draw();
})();
</script>