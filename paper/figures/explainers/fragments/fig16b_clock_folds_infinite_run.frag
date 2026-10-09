<h2 class="sr-only">Figure 16b. The activity clock is the area under the residual activity; an infinite training run maps to a finite clock interval, where the backward history and its Legendre moments settle and freeze.</h2>
<div style="font-size:15px;font-weight:500;color:var(--text-primary);margin:0 0 8px">Figure 16b · The clock folds an infinite run into a finite interval</div>
<div style="display:flex;align-items:center;gap:10px;margin:0 0 6px;font-size:13px;color:var(--text-secondary)">
<button id="pp" style="font-size:13px;padding:4px 10px">Pause</button>
<button id="rs" style="font-size:13px;padding:4px 10px">Restart</button>
<span>Moments q</span><input type="range" id="qs" min="1" max="8" step="1" value="5" style="flex:1">
<span id="ql" style="min-width:230px;text-align:right"></span>
</div>
<svg id="sv" width="100%" viewBox="0 0 680 420" role="img"><title>Figure 16b: the clock folds an infinite run into a finite interval</title><desc>Top: residual activity over real time with the area so far. Middle: threads mapping real times to clock times, converging at a finite end. Bottom: the backward history on the clock with its moment fit. Right: the moments, which stop changing.</desc></svg>
<script>
(()=>{
const D={"t":[0.0,0.2,0.4,0.6,0.8,1.0,1.2,1.4,1.6,1.8,2.0,2.2,2.4,2.6,2.8,3.0,3.2,3.4,3.6,3.8,4.0,4.2,4.4,4.6,4.8,5.0,5.2,5.4,5.6,5.8,6.0,6.2,6.4,6.6,6.8,7.0,7.2,7.4,7.6,7.8,8.0,8.2,8.4,8.6,8.8,9.0,9.2,9.4,9.6,9.8,10.0,10.2,10.4,10.6,10.8,11.0,11.2,11.4,11.6,11.8,12.0,12.2,12.4,12.6,12.8,13.0,13.2,13.4,13.6,13.8,14.0,14.2,14.4,14.6,14.8,15.0,15.2,15.4,15.6,15.8,16.0,16.2,16.4,16.6,16.8,17.0,17.2,17.4,17.6,17.8,18.0,18.2,18.4,18.6,18.8,19.0,19.2,19.4,19.6,19.8,20.0,20.2,20.4,20.6,20.8,21.0,21.2,21.4,21.6,21.8,22.0,22.2,22.4,22.6,22.8,23.0,23.2,23.4,23.6,23.8,24.0,24.2,24.4,24.6,24.8,25.0,25.2,25.4,25.6,25.8,26.0,26.2,26.4,26.6,26.8,27.0,27.2,27.4,27.6,27.8,28.0,28.2,28.4,28.6,28.8,29.0,29.2,29.4,29.6,29.8,30.0,30.2,30.4,30.6,30.8,31.0,31.2,31.4,31.6,31.8,32.0],"rho":[1.0,0.97102,0.94059,0.90673,0.86826,0.82493,0.77748,0.72736,0.67635,0.62607,0.57774,0.53214,0.48974,0.45095,0.41614,0.38559,0.35941,0.33748,0.31948,0.30496,0.2934,0.28426,0.27705,0.27132,0.26672,0.26295,0.25978,0.25704,0.2546,0.25237,0.25027,0.24826,0.24631,0.2444,0.24251,0.24063,0.23876,0.2369,0.23505,0.2332,0.23136,0.22954,0.22773,0.22593,0.22415,0.22239,0.22064,0.2189,0.21719,0.21549,0.2138,0.21214,0.21049,0.20885,0.20723,0.20562,0.20403,0.20245,0.20088,0.19933,0.19779,0.19626,0.19474,0.19324,0.19174,0.19026,0.18878,0.18732,0.18586,0.18441,0.18297,0.18154,0.18011,0.17869,0.17727,0.17586,0.17445,0.17305,0.17165,0.17025,0.16886,0.16747,0.16608,0.16469,0.1633,0.16192,0.16053,0.15914,0.15776,0.15637,0.15498,0.15359,0.15221,0.15082,0.14942,0.14803,0.14664,0.14524,0.14385,0.14245,0.14105,0.13965,0.13825,0.13685,0.13544,0.13404,0.13263,0.13123,0.12982,0.12842,0.12702,0.12561,0.12421,0.12281,0.12141,0.12002,0.11863,0.11724,0.11585,0.11447,0.11309,0.11172,0.11035,0.10899,0.10764,0.10629,0.10495,0.10361,0.10228,0.10096,0.099646,0.09834,0.097043,0.095753,0.094473,0.093201,0.091938,0.090685,0.089441,0.088207,0.086982,0.085768,0.084564,0.08337,0.082187,0.081014,0.079853,0.078703,0.077563,0.076436,0.075319,0.074214,0.073121,0.07204,0.070971,0.069913,0.068868,0.067835,0.066814,0.065805,0.064809],"tau":[1.0,1.1971,1.3883,1.5731,1.7507,1.9201,2.0804,2.2309,2.3713,2.5015,2.6218,2.7328,2.8349,2.9289,3.0155,3.0956,3.1701,3.2397,3.3053,3.3677,3.4275,3.4852,3.5413,3.5962,3.65,3.7029,3.7552,3.8068,3.858,3.9087,3.959,4.0088,4.0583,4.1073,4.156,4.2043,4.2523,4.2999,4.347,4.3939,4.4403,4.4864,4.5321,4.5775,4.6225,4.6672,4.7115,4.7554,4.799,4.8423,4.8852,4.9278,4.9701,5.012,5.0536,5.0949,5.1359,5.1765,5.2169,5.2569,5.2966,5.336,5.3751,5.4139,5.4524,5.4906,5.5285,5.5661,5.6034,5.6405,5.6772,5.7136,5.7498,5.7857,5.8213,5.8566,5.8916,5.9264,5.9608,5.995,6.029,6.0626,6.0959,6.129,6.1618,6.1943,6.2266,6.2585,6.2902,6.3216,6.3528,6.3836,6.4142,6.4445,6.4745,6.5043,6.5338,6.5629,6.5919,6.6205,6.6488,6.6769,6.7047,6.7322,6.7594,6.7864,6.8131,6.8394,6.8655,6.8914,6.9169,6.9422,6.9672,6.9919,7.0163,7.0404,7.0643,7.0879,7.1112,7.1342,7.157,7.1795,7.2017,7.2236,7.2453,7.2667,7.2878,7.3086,7.3292,7.3495,7.3696,7.3894,7.4089,7.4282,7.4472,7.466,7.4845,7.5028,7.5208,7.5386,7.5561,7.5734,7.5904,7.6072,7.6237,7.6401,7.6561,7.672,7.6876,7.703,7.7182,7.7332,7.7479,7.7624,7.7767,7.7908,7.8047,7.8183,7.8318,7.8451,7.8581],"kap":0.06982273028862791,"bt":[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.032599,0.083599,0.13445,0.18502,0.23516,0.28474,0.33363,0.38171,0.42886,0.47497,0.51996,0.56373,0.60619,0.64728,0.68699,0.7253,0.76217,0.79758,0.8316,0.86424,0.89552,0.92554,0.95429,0.98188,1.0083,1.0337,1.058,1.0812,1.1033,1.1244,1.1443,1.1631,1.1806,1.1968,1.2118,1.2254,1.2378,1.2488,1.2585,1.2668,1.2736,1.2788,1.282,1.2829,1.2811,1.2764,1.2684,1.2573,1.2432,1.2267,1.2086,1.1897,1.1708,1.1528,1.1361,1.1213,1.1086,1.098,1.0897,1.0836,1.0794,1.0771,1.0765,1.0774,1.0796,1.0829,1.0871,1.0922,1.0978,1.104,1.1105,1.1172,1.1242,1.1312,1.1383,1.1454,1.1525,1.1595,1.1663,1.1731,1.1796,1.1859,1.1921,1.1979,1.2035,1.2088,1.2138,1.2184,1.2227,1.2267,1.2302,1.2334,1.2361,1.2385,1.2404,1.2419,1.243,1.2437,1.244,1.2439,1.2434,1.2426,1.2415,1.2402,1.2387,1.237,1.2352,1.2334,1.2317,1.2301,1.2287,1.2276,1.2269,1.2267,1.227,1.228,1.2297,1.2323,1.2357,1.2402,1.2458,1.2525,1.2605,1.2699,1.2806,1.2927,1.3064,1.3216,1.3384,1.3569,1.3771,1.3991,1.4228,1.4484,1.4757,1.5049,1.5359,1.5686,1.6031,1.6393],"tauEnd":7.858128358120142};
const svg=document.getElementById('sv'),BL='#2a78d6',BD='#185FA5',PU='#7F77DD',PD='#534AB7',GR='#888780';
const E=(n,a,t)=>{const e=document.createElementNS('http://www.w3.org/2000/svg',n);for(const k in a)e.setAttribute(k,a[k]);if(t!==undefined)e.textContent=t;return e};
const T32=32,r32=D.rho[D.rho.length-1],t32=D.tauEnd,TI=t32+r32/D.kap;
const lin=(xs,ys,x)=>{const n=xs.length;if(x<=xs[0])return ys[0];if(x>=xs[n-1])return ys[n-1];let i=Math.floor((x-xs[0])/(xs[1]-xs[0]));i=Math.min(n-2,Math.max(0,i));const w=(x-xs[i])/(xs[i+1]-xs[i]);return ys[i]*(1-w)+ys[i+1]*w};
const rho=t=>t<=T32?lin(D.t,D.rho,t):r32*Math.exp(-D.kap*(t-T32));
const tau=t=>t<=T32?lin(D.t,D.tau,t):t32+r32/D.kap*(1-Math.exp(-D.kap*(t-T32)));
const bg=D.bt.map((_,k)=>t32*k/(D.bt.length-1)),bval=s=>s<=t32?lin(bg,D.bt,s):D.bt[D.bt.length-1];
const bmn=Math.min(...D.bt),bmx=Math.max(...D.bt);
const X0=40,XW=440,xt=t=>X0+XW*Math.min(t,64)/64,xs=s=>X0+XW*s/TI;
const leg=(x,q)=>{const P=[1,x];for(let j=1;j<q;j++)P.push(((2*j+1)*x*P[j]-j*P[j-1])/(j+1));return P};
function moments(s,Q){const M=500,c=Array(Q).fill(0);for(let k=0;k<=M;k++){const u=s*k/M,w=(k===0||k===M?0.5:1)*s/M,P=leg(2*u/s-1,Q),v=bval(u);for(let j=0;j<Q;j++)c[j]+=w*P[j]*v}return c.map((v,j)=>(2*j+1)/s*v)}
let t=0,run=true,last=null;const CREF=Math.max(...[2,3,4,5,6,7,8.5].map(u=>Math.max(...moments(u,8).map(Math.abs))));
function draw(){const q=+document.getElementById('qs').value,s=tau(t);svg.innerHTML='';
svg.appendChild(E('text',{x:X0,y:20,class:'th'},'Real time: residual activity ρ(t)'));
const ry=v=>112-70*v,top=[];let ar=`M${xt(0)} ${ry(0)}`;
for(let k=0;k<=256;k++){const u=64*k/256;top.push([xt(u),ry(rho(u))]);if(u<=t)ar+=`L${xt(u).toFixed(1)} ${ry(rho(u)).toFixed(1)}`}
ar+=`L${xt(Math.min(t,64)).toFixed(1)} ${ry(rho(Math.min(t,64))).toFixed(1)}L${xt(Math.min(t,64)).toFixed(1)} ${ry(0)}Z`;
svg.appendChild(E('path',{d:ar,fill:BL,opacity:0.22,stroke:'none'}));
let d1='',d2='';top.forEach((p,k)=>{const u=64*k/256,str=(k?'L':'M')+p[0].toFixed(1)+' '+p[1].toFixed(1);if(u<=T32)d1+=str;if(u>=T32)d2+=(d2?'L':'M')+p[0].toFixed(1)+' '+p[1].toFixed(1)});
svg.appendChild(E('path',{d:d1,fill:'none',stroke:BD,'stroke-width':1.6}));svg.appendChild(E('path',{d:d2,fill:'none',stroke:BD,'stroke-width':1.2,'stroke-dasharray':'3 3'}));
svg.appendChild(E('line',{x1:X0,y1:ry(0),x2:X0+XW+24,y2:ry(0),stroke:'var(--s)','stroke-width':0.8}));
svg.appendChild(E('text',{x:X0+XW+30,y:ry(0)+4,class:'ts'},'∞'));
[0,16,32,48,64].forEach(u=>svg.appendChild(E('text',{x:xt(u),y:ry(0)+14,'text-anchor':'middle',class:'ts'},u)));svg.appendChild(E('text',{x:X0+XW+30,y:ry(0)+14,class:'ts'},'t'));
svg.appendChild(E('text',{x:xt(36),y:ry(rho(36))-10,class:'ts'},'fitted tail'));
const tx=t<=64?xt(t):X0+XW+20;svg.appendChild(E('circle',{cx:tx,cy:ry(0),r:4.5,fill:'var(--p)'}));
const yA=130,yB=232;
for(let u=0;u<=64;u+=2){const s2=tau(u);svg.appendChild(E('line',{x1:xt(u),y1:yA,x2:xs(s2),y2:yB,stroke:GR,'stroke-width':0.6,opacity:u%16===0?0.9:0.35}))}
[80,100,130,170,240].forEach(u=>svg.appendChild(E('line',{x1:X0+XW+8+(u-80)/12,y1:yA,x2:xs(tau(u)),y2:yB,stroke:GR,'stroke-width':0.6,opacity:0.35})));
svg.appendChild(E('line',{x1:tx,y1:yA,x2:xs(s),y2:yB,stroke:'var(--p)','stroke-width':1.4}));
svg.appendChild(E('text',{x:528,y:156,class:'ts'},'every later time'));svg.appendChild(E('text',{x:528,y:172,class:'ts'},'lands before τ∞'));
const by=v=>372-86*(v-bmn)/(bmx-bmn),cy0=yB;
svg.appendChild(E('line',{x1:X0,y1:cy0,x2:xs(TI),y2:cy0,stroke:'var(--s)','stroke-width':0.8}));
svg.appendChild(E('rect',{x:xs(1),y:cy0-3,width:Math.max(0,xs(s)-xs(1)),height:6,fill:BL,opacity:0.35}));
svg.appendChild(E('line',{x1:xs(TI),y1:cy0-8,x2:xs(TI),y2:cy0+8,stroke:'var(--p)','stroke-width':1.5}));
svg.appendChild(E('text',{x:xs(TI)+6,y:cy0+4,class:'ts'},'τ∞ = '+TI.toFixed(2)));
svg.appendChild(E('text',{x:xs(0),y:cy0+18,'text-anchor':'middle',class:'ts'},'0'));svg.appendChild(E('text',{x:xs(1),y:cy0+18,'text-anchor':'middle',class:'ts'},'1'));svg.appendChild(E('text',{x:xs(1)+8,y:cy0+18,class:'ts'},'clock τ: blue length = blue area above'));
let dp='',df='';for(let k=0;k<=300;k++){const u=TI*k/300,v=bval(u),str=(u<=s?(dp?'L':'M'):(df?'L':'M'))+xs(u).toFixed(1)+' '+by(v).toFixed(1);if(u<=s)dp+=str;else df+=str}
svg.appendChild(E('path',{d:dp,fill:'none',stroke:PU,'stroke-width':1.6}));if(df)svg.appendChild(E('path',{d:df,fill:'none',stroke:PU,'stroke-width':1,opacity:0.3}));
const c=moments(Math.max(s,1e-3),8);let dfit='';for(let k=0;k<=200;k++){const u=s*k/200,P=leg(2*u/s-1,q);let v=0;for(let j=0;j<q;j++)v+=c[j]*P[j];dfit+=(k?'L':'M')+xs(u).toFixed(1)+' '+by(v).toFixed(1)}
svg.appendChild(E('path',{d:dfit,fill:'none',stroke:PD,'stroke-width':2,'stroke-dasharray':'5 3'}));
svg.appendChild(E('circle',{cx:xs(s),cy:by(bval(s)),r:4.5,fill:'var(--p)'}));
svg.appendChild(E('text',{x:X0,y:270,class:'th'},'On the clock: backward history bᵢ, q-moment memory'));
const MX=566,MY=282;svg.appendChild(E('text',{x:MX-40,y:MY-12,class:'th'},'Moments now'));
const cm=CREF;c.forEach((v,j)=>{const w=Math.min(84,70*Math.abs(v)/cm),kept=j<q;svg.appendChild(E('rect',{x:v>=0?MX+20:MX+20-w,y:MY+j*16,width:Math.max(w,0.5),height:11,rx:2,fill:PU,opacity:kept?0.9:0.25}));svg.appendChild(E('text',{x:MX-40,y:MY+j*16+10,class:'ts'},'k='+j))});
svg.appendChild(E('line',{x1:MX+20,y1:MY-4,x2:MX+20,y2:MY+8*16,stroke:'var(--b)','stroke-width':0.5}));
document.getElementById('ql').textContent=`t = ${t<1000?t.toFixed(1):'∞'} → τ = ${s.toFixed(2)} of ${TI.toFixed(2)}`}
function frame(ts){if(last===null)last=ts;const dt=Math.min(0.05,(ts-last)/1000);last=ts;if(run){t+=dt*(1.2+t/3);if(t>400){t=400;run=false;document.getElementById('pp').textContent='Play'}}draw();requestAnimationFrame(frame)}
document.getElementById('pp').onclick=e=>{if(!run&&t>=400)t=0;run=!run;e.target.textContent=run?'Pause':'Play'};
document.getElementById('rs').onclick=()=>{t=0;run=true;document.getElementById('pp').textContent='Pause'};
document.getElementById('qs').oninput=draw;requestAnimationFrame(frame);
})();
</script>