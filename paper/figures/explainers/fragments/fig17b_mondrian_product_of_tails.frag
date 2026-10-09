<h2 class="sr-only">Figure 17b. The weight written by a link is a Mondrian of rectangles: column widths are forward moment sizes, row heights are backward moment sizes; only diagonal cells are filled, so truncating at q loses only the small corner cells.</h2>
<div style="font-size:15px;font-weight:500;color:var(--text-primary);margin:0 0 8px">Figure 17b · Only like pairs with like (Mondrian)</div>
<div style="display:flex;align-items:center;gap:10px;margin:0 0 6px;font-size:13px;color:var(--text-secondary)">
<span>Moments q</span><input type="range" id="qs" min="1" max="11" step="1" value="3" style="flex:1">
<span id="ql" style="min-width:250px;text-align:right"></span>
</div>
<svg id="sv" width="100%" viewBox="0 0 680 445" role="img"><title>Figure 17b: only like pairs with like</title><desc>A square divided into columns by forward moment sizes and rows by backward moment sizes; diagonal cells filled; truncation lines split kept, cross and dropped blocks; error versus q.</desc></svg>
<script>
(()=>{
const svg=document.getElementById('sv'),BL='#2a78d6',PU='#7F77DD',PD='#534AB7',GR='#888780';
const E=(n,a,t)=>{const e=document.createElementNS('http://www.w3.org/2000/svg',n);for(const k in a)e.setAttribute(k,a[k]);if(t!==undefined)e.textContent=t;return e};
const K=12,sf=[1,-1,1,1,-1,1,-1,-1,1,-1,1,1],sg=[1,1,-1,1,1,-1,-1,1,-1,1,1,-1];
const f=Array.from({length:K},(_,k)=>sf[k]*Math.pow(k+1,-1.5)),g=Array.from({length:K},(_,k)=>sg[k]*0.9*Math.pow(k+1,-1.5)*(1+0.3*Math.sin(k)));
const FT=f.reduce((s,v)=>s+Math.abs(v),0),GT=g.reduce((s,v)=>s+Math.abs(v),0);
const S=330,X0=60,Y0=64,cw=f.map(v=>S*Math.abs(v)/FT),rh=g.map(v=>S*Math.abs(v)/GT);
const cx=[X0],cy=[Y0];cw.forEach((w,k)=>cx.push(cx[k]+w));rh.forEach((h,k)=>cy.push(cy[k]+h));
const N=200,tailf=q=>{let s=0;for(let k=q;k<N;k++)s+=Math.pow(k+1,-3);return Math.sqrt(s)},tailg=q=>0.9*tailf(q);
const total=f.reduce((s,v,k)=>s+v*g[k],0);
function draw(){const q=+document.getElementById('qs').value;svg.innerHTML='';
svg.appendChild(E('text',{x:40,y:22,class:'th'},'Wᵢⱼ as rectangles: width × height = what a pair writes'));
svg.appendChild(E('text',{x:X0,y:Y0-10,class:'ts'},'forward moments h̄ₖ: column width = size →'));
svg.appendChild(E('text',{x:X0,y:Y0+S+34,class:'ts'},'rows: backward moments b̄ₖ, row height = size'));
if(q<K){svg.appendChild(E('rect',{x:cx[q],y:Y0,width:cx[K]-cx[q],height:cy[q]-Y0,fill:GR,opacity:0.07}));svg.appendChild(E('rect',{x:X0,y:cy[q],width:cx[q]-X0,height:cy[K]-cy[q],fill:GR,opacity:0.07}));
svg.appendChild(E('rect',{x:cx[q],y:cy[q],width:cx[K]-cx[q],height:cy[K]-cy[q],fill:PU,opacity:0.14}))}
svg.appendChild(E('rect',{x:X0,y:Y0,width:cx[q]-X0,height:cy[q]-Y0,fill:BL,opacity:0.08}));
for(let j=0;j<K;j++)for(let k=0;k<K;k++){const x=cx[k],y=cy[j],w=cw[k],h=rh[j];
if(j!==k){svg.appendChild(E('rect',{x,y,width:w,height:h,fill:'none',stroke:'var(--b)','stroke-width':0.5}));continue}
const kept=k<q,pos=f[k]*g[k]>0;svg.appendChild(E('rect',{x:x+0.5,y:y+0.5,width:Math.max(w-1,0.6),height:Math.max(h-1,0.6),fill:pos?BL:PD,opacity:kept?0.9:0.45}))}
svg.appendChild(E('rect',{x:X0,y:Y0,width:S,height:S,fill:'none',stroke:'var(--s)','stroke-width':0.8}));
if(q<K){svg.appendChild(E('line',{x1:cx[q],y1:Y0-4,x2:cx[q],y2:Y0+S+4,stroke:'var(--p)','stroke-width':1.4,'stroke-dasharray':'4 3'}));svg.appendChild(E('line',{x1:X0-4,y1:cy[q],x2:X0+S+4,y2:cy[q],stroke:'var(--p)','stroke-width':1.4,'stroke-dasharray':'4 3'}))}
for(let k=0;k<4;k++){svg.appendChild(E('text',{x:(cx[k]+cx[k+1])/2,y:Y0+S+16,'text-anchor':'middle',class:'ts'},k));svg.appendChild(E('text',{x:X0-8,y:(cy[k]+cy[k+1])/2+4,'text-anchor':'end',class:'ts'},k))}
const lx=416;
[[BL,0.9,'filled diagonal: mode k forward × mode k backward'],[GR,0.12,'gray blocks: kept × dropped, empty'],[PU,0.3,'purple corner: dropped × dropped']].forEach(([c,o,t],i)=>{svg.appendChild(E('rect',{x:lx,y:58+i*20,width:12,height:12,rx:2,fill:c,opacity:o,stroke:c==GR?'var(--b)':'none'}));svg.appendChild(E('text',{x:lx+18,y:68+i*20,class:'ts'},t))});
let kept=0,drop=0;f.forEach((v,k)=>{if(k<q)kept+=v*g[k];else drop+=v*g[k]});
const crossArea=q<K?((cx[q]-X0)*(cy[K]-cy[q])+(cx[K]-cx[q])*(cy[q]-Y0))/(S*S):0,cornerCells=f.reduce((s,v,k)=>s+(k>=q?cw[k]*rh[k]:0),0)/(S*S);
svg.appendChild(E('text',{x:lx,y:142,class:'ts'},`gray blocks: ${(100*crossArea).toFixed(0)}% of the square, all empty`));
svg.appendChild(E('text',{x:lx,y:160,class:'ts'},`lost corner cells: ${(100*cornerCells).toFixed(2)}% of it`));
const PX=lx+10,PW=220,PY=200,PH=170,qx=v=>PX+PW*Math.log10(v)/Math.log10(40),qy=v=>PY+PH*Math.min(1,-Math.log10(v)/5);
svg.appendChild(E('text',{x:lx,y:PY-12,class:'th'},'What is lost versus q'));
svg.appendChild(E('line',{x1:PX,y1:PY+PH,x2:PX+PW,y2:PY+PH,stroke:'var(--b)','stroke-width':0.5}));svg.appendChild(E('line',{x1:PX,y1:PY,x2:PX,y2:PY+PH,stroke:'var(--b)','stroke-width':0.5}));
let a1='',a2='';for(let v=1;v<=40;v++){const t1=tailf(v),t2=tailf(v)*tailg(v);a1+=(v>1?'L':'M')+qx(v).toFixed(1)+' '+qy(t1/tailf(0)).toFixed(1);a2+=(v>1?'L':'M')+qx(v).toFixed(1)+' '+qy(t2/(tailf(0)*tailg(0))).toFixed(1)}
svg.appendChild(E('path',{d:a1,fill:'none',stroke:GR,'stroke-width':1.6}));svg.appendChild(E('path',{d:a2,fill:'none',stroke:PD,'stroke-width':2.2}));
svg.appendChild(E('line',{x1:qx(q),y1:PY,x2:qx(q),y2:PY+PH,stroke:GR,'stroke-width':0.8,'stroke-dasharray':'2 3'}));
svg.appendChild(E('text',{x:qx(9),y:qy(tailf(9)/tailf(0))-8,class:'ts'},'one side ~ 1/q'));
svg.appendChild(E('text',{x:PX+8,y:PY+PH-10,class:'ts'},'corner: side × side ~ 1/q²'));
[1,10,40].forEach(v=>svg.appendChild(E('text',{x:qx(v),y:PY+PH+15,'text-anchor':'middle',class:'ts'},v)));
document.getElementById('ql').textContent=`written by q pairs: ${(100*kept/total).toFixed(1)}% · lost: ${(100*Math.abs(drop/total)).toFixed(2)}%`}
document.getElementById('qs').oninput=draw;draw();
})();
</script>