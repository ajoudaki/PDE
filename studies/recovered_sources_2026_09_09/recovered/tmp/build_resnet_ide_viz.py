#!/usr/bin/env python3
import json
from pathlib import Path

data_path = Path("/home/codex-b/.codex/visualizations/2026/08/22/01a029da-1475-7973-9659-be5387acef2f/resnet-ide-single-input.json")
output_path = Path("/home/codex-b/.codex/visualizations/2026/08/22/01a029da-1475-7973-9659-be5387acef2f/resnet-ide-single-input.html")
data = json.loads(data_path.read_text())
packed = json.dumps(data, separators=(",", ":"))

fragment = r'''
<div id="resnet-ide-audit">
  <div class="audit-heading">
    <div class="audit-title">One-input residual IDE: independent numerical audit</div>
    <div class="audit-subtitle">Eulerian density transport versus finite particle ResNets · x = 1, y = 0, η = 1, ρ₀ = N((2,2,0), I₃)</div>
  </div>
  <div class="audit-grid">
    <section class="audit-panel">
      <div class="panel-title">Output trajectory</div>
      <div class="legend" data-legend="output"></div>
      <div class="chart" data-chart="output"></div>
    </section>
    <section class="audit-panel">
      <div class="panel-title">MSE trajectory</div>
      <div class="legend" data-legend="loss"></div>
      <div class="chart" data-chart="loss"></div>
    </section>
    <section class="audit-panel">
      <div class="panel-title">Final output versus particle width</div>
      <div class="chart" data-chart="convergence"></div>
    </section>
    <section class="audit-panel">
      <div class="panel-title">β marginal at depth s = 0.5, time t = 0.5</div>
      <div class="legend" data-legend="beta"></div>
      <div class="chart" data-chart="beta"></div>
    </section>
  </div>
  <div class="audit-foot" aria-label="Numerical audit summary"></div>
  <div class="tooltip" role="tooltip"></div>
</div>
<style>
#resnet-ide-audit { color: var(--foreground); font-family: ui-sans-serif, system-ui, sans-serif; position: relative; width: 100%; }
#resnet-ide-audit .audit-heading { margin: 2px 0 12px; }
#resnet-ide-audit .audit-title { font-size: 17px; font-weight: 650; letter-spacing: -0.01em; }
#resnet-ide-audit .audit-subtitle, #resnet-ide-audit .audit-foot { color: var(--muted-foreground); font-size: 12px; line-height: 1.45; margin-top: 3px; }
#resnet-ide-audit .audit-grid { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 18px 20px; }
#resnet-ide-audit .audit-panel { min-width: 0; }
#resnet-ide-audit .panel-title { font-size: 13px; font-weight: 620; margin-bottom: 3px; }
#resnet-ide-audit .chart { width: 100%; min-height: 250px; }
#resnet-ide-audit svg { display: block; width: 100%; height: auto; overflow: visible; }
#resnet-ide-audit text { fill: var(--foreground); font-size: 12px; }
#resnet-ide-audit .axis path, #resnet-ide-audit .axis line { stroke: var(--border); }
#resnet-ide-audit .axis text { fill: var(--muted-foreground); }
#resnet-ide-audit rect[data-chart-frame] { fill: transparent; stroke: var(--border); }
#resnet-ide-audit .legend { min-height: 23px; display: flex; flex-wrap: wrap; gap: 4px 12px; align-items: center; }
#resnet-ide-audit .legend button { appearance: none; border: 0; background: transparent; color: var(--foreground); padding: 2px 0; font: inherit; font-size: 11px; cursor: pointer; }
#resnet-ide-audit .legend button[aria-pressed="false"] { opacity: 0.42; }
#resnet-ide-audit .swatch { display: inline-block; width: 14px; height: 3px; margin-right: 5px; vertical-align: middle; }
#resnet-ide-audit .tooltip { position: absolute; pointer-events: none; visibility: hidden; z-index: 20; background: var(--popover); color: var(--popover-foreground); border: 1px solid var(--border); padding: 6px 8px; border-radius: 5px; font-size: 11px; line-height: 1.45; white-space: nowrap; }
#resnet-ide-audit .audit-foot { margin-top: 12px; }
@media (max-width: 720px) { #resnet-ide-audit .audit-grid { grid-template-columns: 1fr; } }
</style>
<script src="https://cdn.jsdelivr.net/npm/d3@7.9.0/dist/d3.min.js"></script>
<script>
(() => {
  const root = document.getElementById("resnet-ide-audit");
  const DATA = __DATA__;
  const tooltip = d3.select(root).select(".tooltip");
  const colors = ["var(--viz-series-1)","var(--viz-series-2)","var(--viz-series-3)","var(--viz-series-4)","var(--viz-series-5)"];
  const enabled = new Map();

  function addLegend(name, series, redraw) {
    const legend = d3.select(root).select(`[data-legend="${name}"]`);
    legend.selectAll("button").data(series, d => d.key).join("button")
      .attr("type", "button").attr("aria-pressed", d => enabled.get(d.key) !== false)
      .html(d => `<span class="swatch" style="background:${d.color}"></span>${d.label}`)
      .on("click", function(event, d) {
        enabled.set(d.key, enabled.get(d.key) === false);
        d3.select(this).attr("aria-pressed", enabled.get(d.key));
        redraw();
      });
  }

  function linePanel(name, yLabel, series, bands = []) {
    const holder = root.querySelector(`[data-chart="${name}"]`);
    series.forEach(d => { if (!enabled.has(d.key)) enabled.set(d.key, true); });
    function draw() {
      holder.innerHTML = "";
      const width = Math.max(330, holder.clientWidth || 480), height = 260;
      const margin = {top: 10, right: 18, bottom: 48, left: 66};
      const svg = d3.select(holder).append("svg").attr("viewBox", `0 0 ${width} ${height}`);
      const x = d3.scaleLinear().domain(d3.extent(DATA.time)).range([margin.left, width-margin.right]);
      const visible = series.filter(d => enabled.get(d.key));
      const ys = visible.flatMap(d => d.values);
      bands.filter(b => enabled.get(b.key)).forEach(b => { ys.push(...b.low, ...b.high); });
      const extent = d3.extent(ys.length ? ys : [0,1]);
      const pad = Math.max((extent[1]-extent[0])*0.08, 1e-4);
      const y = d3.scaleLinear().domain([extent[0]-pad, extent[1]+pad]).nice().range([height-margin.bottom, margin.top]);
      svg.append("rect").attr("data-chart-frame", "").attr("x",margin.left).attr("y",margin.top).attr("width",width-margin.left-margin.right).attr("height",height-margin.top-margin.bottom);
      const area = d3.area().x((d,i)=>x(DATA.time[i])).y0((d,i)=>y(d.low)).y1((d,i)=>y(d.high));
      bands.filter(b => enabled.get(b.key)).forEach(b => svg.append("path").datum(b.low.map((v,i)=>({low:v,high:b.high[i]}))).attr("d",area).attr("fill",b.color).attr("opacity",0.14));
      const line = d3.line().x((d,i)=>x(DATA.time[i])).y(d=>y(d));
      visible.forEach(d => svg.append("path").datum(d.values).attr("data-series",d.key).attr("fill","none").attr("stroke",d.color).attr("stroke-width",d.width||2).attr("stroke-dasharray",d.dash||null).attr("d",line));
      svg.append("g").attr("class","axis").attr("transform",`translate(0,${height-margin.bottom})`).call(d3.axisBottom(x).ticks(width<400?4:6));
      svg.append("g").attr("class","axis").attr("transform",`translate(${margin.left},0)`).call(d3.axisLeft(y).ticks(5));
      svg.append("text").attr("class","axis-title").attr("data-axis","x").attr("x",(margin.left+width-margin.right)/2).attr("y",height-8).attr("text-anchor","middle").text("training time t");
      svg.append("text").attr("class","axis-title").attr("data-axis","y").attr("transform",`translate(15,${(margin.top+height-margin.bottom)/2}) rotate(-90)`).attr("text-anchor","middle").text(yLabel);
      const guide = svg.append("line").attr("data-chart-hover-guide","").attr("y1",margin.top).attr("y2",height-margin.bottom).attr("stroke","var(--muted-foreground)").attr("stroke-dasharray","3,3").style("visibility","hidden");
      const markers = new Map(visible.map(d => [d.key, svg.append("circle").attr("r",3.5).attr("fill",d.color).style("visibility","hidden")]));
      svg.append("rect").attr("data-chart-hit","").attr("data-chart-hover-overlay","cross-series").attr("x",margin.left).attr("y",margin.top).attr("width",width-margin.left-margin.right).attr("height",height-margin.top-margin.bottom).attr("fill","transparent")
        .on("mousemove", event => {
          const [mx] = d3.pointer(event); const tx = Math.max(DATA.time[0],Math.min(DATA.time.at(-1),x.invert(mx)));
          guide.attr("x1",x(tx)).attr("x2",x(tx)).style("visibility","visible");
          const rows=[];
          visible.forEach(d => { const i=d3.bisector(v=>v).center(DATA.time,tx); const val=d.values[i]; markers.get(d.key).attr("cx",x(DATA.time[i])).attr("cy",y(val)).style("visibility","visible"); rows.push(`<div><span style="color:${d.color}">●</span> ${d.label}: ${val.toFixed(5)}</div>`); });
          const rect=root.getBoundingClientRect(); tooltip.html(`<b>t = ${tx.toFixed(3)}</b>${rows.join("")}`).style("left",`${event.clientX-rect.left+12}px`).style("top",`${event.clientY-rect.top-8}px`).style("visibility","visible");
        }).on("mouseleave",()=>{guide.style("visibility","hidden");markers.forEach(m=>m.style("visibility","hidden"));tooltip.style("visibility","hidden");});
    }
    addLegend(name, series, draw); draw();
    new ResizeObserver(draw).observe(holder);
  }

  const p4096 = DATA.particles["4096"];
  const outputSeries = [
    {key:"out-fine",label:"Eulerian 23³",values:DATA.eulerian_fine.output,color:colors[0],width:2.4},
    {key:"out-coarse",label:"Eulerian 17³",values:DATA.eulerian_coarse.output,color:colors[1],dash:"5,4"},
    {key:"out-particle",label:"particles n=4096",values:p4096.output_mean,color:colors[2],width:2}
  ];
  const outputBand = [{key:"out-particle",low:p4096.output_mean.map((v,i)=>v-p4096.output_std[i]),high:p4096.output_mean.map((v,i)=>v+p4096.output_std[i]),color:colors[2]}];
  linePanel("output","network output f(t)",outputSeries,outputBand);
  linePanel("loss","MSE ½(f-y)²",[
    {key:"loss-fine",label:"Eulerian 23³",values:DATA.eulerian_fine.loss,color:colors[0],width:2.4},
    {key:"loss-particle",label:"particles n=4096",values:p4096.loss_mean,color:colors[2],width:2}
  ],[{key:"loss-particle",low:p4096.loss_mean.map((v,i)=>v-p4096.loss_std[i]),high:p4096.loss_mean.map((v,i)=>v+p4096.loss_std[i]),color:colors[2]}]);

  function convergencePanel() {
    const holder=root.querySelector('[data-chart="convergence"]'); holder.innerHTML="";
    const width=Math.max(330,holder.clientWidth||480),height=283,margin={top:18,right:18,bottom:50,left:66};
    const rows=Object.entries(DATA.particles).map(([n,d])=>({n:+n,y:d.output_mean.at(-1),sd:d.output_std.at(-1)}));
    const fine=DATA.eulerian_fine.output.at(-1), coarse=DATA.eulerian_coarse.output.at(-1);
    const allY=rows.flatMap(d=>[d.y-d.sd,d.y+d.sd]).concat([fine,coarse]); const ext=d3.extent(allY),pad=Math.max((ext[1]-ext[0])*.18,1e-3);
    const x=d3.scaleLog().domain(d3.extent(rows,d=>d.n)).range([margin.left,width-margin.right]);
    const y=d3.scaleLinear().domain([ext[0]-pad,ext[1]+pad]).nice().range([height-margin.bottom,margin.top]);
    const svg=d3.select(holder).append("svg").attr("viewBox",`0 0 ${width} ${height}`);
    svg.append("rect").attr("data-chart-frame","").attr("x",margin.left).attr("y",margin.top).attr("width",width-margin.left-margin.right).attr("height",height-margin.top-margin.bottom);
    svg.append("rect").attr("x",margin.left).attr("width",width-margin.left-margin.right).attr("y",y(Math.max(fine,coarse))).attr("height",Math.abs(y(fine)-y(coarse))).attr("fill",colors[0]).attr("opacity",.12);
    svg.append("line").attr("x1",margin.left).attr("x2",width-margin.right).attr("y1",y(fine)).attr("y2",y(fine)).attr("stroke",colors[0]).attr("stroke-width",2);
    svg.selectAll("line.whisker").data(rows).join("line").attr("class","whisker").attr("x1",d=>x(d.n)).attr("x2",d=>x(d.n)).attr("y1",d=>y(d.y-d.sd)).attr("y2",d=>y(d.y+d.sd)).attr("stroke",colors[2]).attr("stroke-width",2);
    svg.selectAll("circle.point").data(rows).join("circle").attr("class","point").attr("cx",d=>x(d.n)).attr("cy",d=>y(d.y)).attr("r",5).attr("fill",colors[2]);
    svg.append("g").attr("class","axis").attr("transform",`translate(0,${height-margin.bottom})`).call(d3.axisBottom(x).tickValues(rows.map(d=>d.n)).tickFormat(d3.format("d")));
    svg.append("g").attr("class","axis").attr("transform",`translate(${margin.left},0)`).call(d3.axisLeft(y).ticks(5));
    svg.append("text").attr("class","axis-title").attr("data-axis","x").attr("x",(margin.left+width-margin.right)/2).attr("y",height-8).attr("text-anchor","middle").text("particles per layer n (log scale)");
    svg.append("text").attr("class","axis-title").attr("data-axis","y").attr("transform",`translate(15,${(margin.top+height-margin.bottom)/2}) rotate(-90)`).attr("text-anchor","middle").text("final output f(0.5)");
    svg.append("text").attr("x",width-margin.right-4).attr("y",y(fine)-6).attr("text-anchor","end").attr("fill",colors[0]).text("Eulerian fine");
  }
  convergencePanel(); new ResizeObserver(convergencePanel).observe(root.querySelector('[data-chart="convergence"]'));

  function betaPanel() {
    const holder=root.querySelector('[data-chart="beta"]'); holder.innerHTML="";
    const width=Math.max(330,holder.clientWidth||480),height=260,margin={top:10,right:18,bottom:48,left:66};
    const beta=DATA.beta_marginal, series=[{key:"beta-pde",label:"Eulerian density",values:beta.pde,color:colors[0]},{key:"beta-particle",label:"particle histogram",values:beta.particles,color:colors[2]}];
    series.forEach(d=>{if(!enabled.has(d.key))enabled.set(d.key,true)}); const visible=series.filter(d=>enabled.get(d.key));
    const x=d3.scaleLinear().domain(d3.extent(beta.centers)).range([margin.left,width-margin.right]); const ymax=d3.max(visible.flatMap(d=>d.values))||1; const y=d3.scaleLinear().domain([0,ymax*1.08]).nice().range([height-margin.bottom,margin.top]);
    const svg=d3.select(holder).append("svg").attr("viewBox",`0 0 ${width} ${height}`); svg.append("rect").attr("data-chart-frame","").attr("x",margin.left).attr("y",margin.top).attr("width",width-margin.left-margin.right).attr("height",height-margin.top-margin.bottom);
    const line=d3.line().x((d,i)=>x(beta.centers[i])).y(d=>y(d)); visible.forEach((d,i)=>svg.append("path").datum(d.values).attr("fill","none").attr("stroke",d.color).attr("stroke-width",i?1.8:2.4).attr("stroke-dasharray",i?"4,3":null).attr("d",line));
    svg.append("g").attr("class","axis").attr("transform",`translate(0,${height-margin.bottom})`).call(d3.axisBottom(x).ticks(width<400?4:6)); svg.append("g").attr("class","axis").attr("transform",`translate(${margin.left},0)`).call(d3.axisLeft(y).ticks(5));
    svg.append("text").attr("class","axis-title").attr("data-axis","x").attr("x",(margin.left+width-margin.right)/2).attr("y",height-8).attr("text-anchor","middle").text("raw bias parameter β"); svg.append("text").attr("class","axis-title").attr("data-axis","y").attr("transform",`translate(15,${(margin.top+height-margin.bottom)/2}) rotate(-90)`).attr("text-anchor","middle").text("probability density");
  }
  const betaSeries=[{key:"beta-pde",label:"Eulerian density",color:colors[0]},{key:"beta-particle",label:"particles n=4096",color:colors[2]}]; betaSeries.forEach(d=>enabled.set(d.key,true)); addLegend("beta",betaSeries,betaPanel); betaPanel(); new ResizeObserver(betaPanel).observe(root.querySelector('[data-chart="beta"]'));

  const a=DATA.audits, gap=Math.abs(DATA.eulerian_fine.output.at(-1)-p4096.output_mean.at(-1));
  root.querySelector(".audit-foot").textContent=`Mass error ${DATA.eulerian_fine.mass_error.toExponential(1)} · no positive loss increments · fine/coarse Eulerian final gap ${DATA.eulerian_coarse.final_output_difference_from_fine.toFixed(4)} · Eulerian/4096-particle final gap ${gap.toFixed(4)} · β-marginal W₁ ${DATA.beta_marginal.histogram_w1.toFixed(4)}`;
})();
</script>
'''.replace("__DATA__", packed)

output_path.write_text(fragment)
print(output_path)
