"""Standalone scientific PDF/PNG figures using ReportLab's plotting library."""
import argparse,json
from pathlib import Path
import numpy as np
from reportlab.lib.colors import HexColor, Color
from reportlab.pdfgen.canvas import Canvas
from reportlab.graphics.shapes import Drawing, String, Line, Rect
from reportlab.graphics.charts.lineplots import LinePlot
from reportlab.graphics import renderPDF, renderPM, renderSVG
from circle_tasks import TASKS,METHODS

COLORS={"gaussian":"#202832","gaussian_control":"#8d949e","hd":"#2687ca",
        "hdhd":"#8955ad","fastfood":"#18977b","reflection4":"#e48626","diagonal":"#cf4758"}
LABELS={"gaussian":"Gaussian","gaussian_control":"Gaussian replicate","hd":"HD",
        "hdhd":"D1 H D2 H D3","fastfood":"Fastfood","reflection4":"Four reflections",
        "diagonal":"Signed diagonal"}


def collect(paths):
    records={}
    for path in paths:
        root=Path(path)
        for filename in root.glob("*__dt*.json"):
            r=json.loads(filename.read_text())
            if r["status"]=="ok": records[(r["task"],r["width"],r["seed"],r["method"])]=(r,root)
    return records


def legend(drawing,x,y,methods):
    for i,method in enumerate(methods):
        xx=x+(i%4)*172;yy=y-(i//4)*15
        drawing.add(Line(xx,yy,xx+17,yy,strokeColor=HexColor(COLORS[method]),strokeWidth=2))
        drawing.add(String(xx+23,yy-3,LABELS[method],fontSize=9,fillColor=HexColor("#26313b")))


def curve_plot(records, task, width, x,y, size=300):
    drawing=Drawing(size,180)
    data=[];names=[]
    means={}
    for method in METHODS:
        series=[]
        for (tn,n,seed,met),(rec,root) in records.items():
            if tn==task.name and n==width and met==method and seed==0:
                stage="fit6" if "fit6" in rec["records"] else "final"
                with np.load(root/rec["data_file"]) as a:
                    series.append(a[stage+"_circle"][::16])
        if series:
            means[method]=np.mean(series,axis=0)
    if not means:return drawing
    length=len(next(iter(means.values())))
    angles=2*np.pi*np.arange(length)/length
    # Repeat the start at 2pi for a visually closed periodic curve.
    aa=np.r_[angles,2*np.pi]
    for method,values in means.items():
        data.append(list(zip(aa,np.r_[values,values[0]])));names.append(method)
    lp=LinePlot();lp.x=32;lp.y=28;lp.width=size-42;lp.height=126
    lp.data=data;lp.joinedLines=1
    lp.xValueAxis.valueMin=0;lp.xValueAxis.valueMax=2*np.pi
    lp.xValueAxis.valueSteps=[0,np.pi,2*np.pi]
    lp.xValueAxis.labelTextFormat=lambda v: "0" if v==0 else ("pi" if abs(v-np.pi)<1e-6 else "2pi")
    lp.xValueAxis.labels.fontSize=7;lp.yValueAxis.labels.fontSize=7
    lo=min(min(v for _,v in s) for s in data);hi=max(max(v for _,v in s) for s in data)
    pad=.08*max(.2,hi-lo);lp.yValueAxis.valueMin=lo-pad;lp.yValueAxis.valueMax=hi+pad
    for i,name in enumerate(names):
        lp.lines[i].strokeColor=HexColor(COLORS[name])
        lp.lines[i].strokeWidth=2.1 if name=="gaussian" else 1.1
        if name=="gaussian_control":lp.lines[i].strokeDashArray=[1,2]
    drawing.add(lp);drawing.add(String(32,165,task.name,fontName="Helvetica-Bold",fontSize=10))
    return drawing


def function_heatmap(records,width,stage):
    methods=[m for m in METHODS if m!="gaussian"]
    W,H=1050,420;d=Drawing(W,H)
    d.add(Rect(0,0,W,H,fillColor=HexColor("#ffffff"),strokeColor=None))
    d.add(String(20,H-28,f"Whole-circle FUNCTION discrepancy from canonical Gaussian, width {width}",fontName="Helvetica-Bold",fontSize=15))
    d.add(String(20,H-47,"Mean relative RMS over paired seeds: RMS(f - f_Gaussian) / RMS(f_Gaussian). Lower is closer.",fontSize=10))
    cellw=70;cellh=38;left=185;bottom=82
    values=[]
    for row,method in enumerate(methods):
        d.add(String(10,bottom+(len(methods)-1-row)*cellh+14,LABELS[method],fontSize=10))
        for col,task in enumerate(TASKS):
            diffs=[];available=0
            for seed in range(12):
                pair=[records.get((task.name,width,seed,m)) for m in ("gaussian",method)]
                if all(pair):
                    ga,me=pair[0][0],pair[1][0]
                    if stage in ga["records"] and stage in me["records"]:
                        with np.load(pair[0][1]/ga["data_file"]) as gdata, np.load(pair[1][1]/me["data_file"]) as mdata:
                            gf=gdata[stage+"_circle"];mf=mdata[stage+"_circle"]
                            diffs.append(float(np.sqrt(np.mean((mf-gf)**2))/np.sqrt(np.mean(gf**2))))
                    available+=1
            val=float(np.mean(diffs)) if diffs else None
            values.append({"task":task.name,"method":method,"value":val,"pairs":len(diffs)})
            if val is None:color=HexColor("#e2e5e8");label="unfitted"
            else:
                intensity=min(val/.25,1.)
                target=(.87,.27,.24)
                color=Color(*(1+(v-1)*intensity for v in target))
                label=f"{100*val:.1f}%"+("*" if len(diffs)<12 else "")
            xx=left+col*cellw;yy=bottom+(len(methods)-1-row)*cellh
            d.add(Rect(xx,yy,cellw-2,cellh-2,fillColor=color,strokeColor=HexColor("#ffffff")))
            d.add(String(xx+cellw/2-1,yy+14,label,textAnchor="middle",fontSize=9))
    for col,task in enumerate(TASKS):
        d.add(String(left+col*cellw+cellw/2,bottom-17,str(col+1),textAnchor="middle",fontSize=9))
    labels="   ".join(f"{i+1}: {t.name}" for i,t in enumerate(TASKS))
    # Explicitly split the long key into three legible lines.
    for j in range(3):
        line="    ".join(f"{i+1}: {TASKS[i].name}" for i in range(4*j,4*j+4))
        d.add(String(20,51-14*j,line,fontSize=9))
    d.add(String(20,H-63,f"Stage: {stage}; * = fewer than 12 fitted pairs. Grey cells have no matched fitted endpoint.",fontSize=9))
    return d,values


def main():
    p=argparse.ArgumentParser();p.add_argument("--base",required=True)
    p.add_argument("--continuation",nargs="*",default=[]);p.add_argument("--output",required=True)
    args=p.parse_args();out=Path(args.output);out.mkdir(parents=True,exist_ok=False)
    records=collect([args.base]+args.continuation)
    pdf=Canvas(str(out/"dense_circle_comparison.pdf"),pagesize=(1050,820))
    heatmap_values={}
    for width in (128,256):
        for stage in ("fit6","time300"):
            draw,vals=function_heatmap(records,width,stage)
            name=f"function_difference_n{width}_{stage}"
            renderPM.drawToFile(draw,str(out/(name+".png")),fmt="PNG",dpi=130)
            renderSVG.drawToFile(draw,str(out/(name+".svg")))
            renderPDF.draw(draw,pdf,0,350)
            pdf.setFont("Helvetica",11)
            pdf.drawString(20,320,"Empirical comparison on the declared suite; finite widths and finite physical horizons.")
            pdf.drawString(20,300,"The Gaussian replicate is context only; matching its variation is not evidence of matching a fixed reference.")
            pdf.showPage();heatmap_values[name]=vals
        drawing=Drawing(1050,820)
        drawing.add(String(20,795,f"Whole-circle fitted functions: width {width}, matched seed 0",fontName="Helvetica-Bold",fontSize=16))
        drawing.add(String(20,777,"Black: canonical Gaussian reference. First MSE <= 1e-6 endpoint; final state for nonfitting runs.",fontSize=10))
        legend(drawing,22,754,list(METHODS))
        for i,task in enumerate(TASKS):
            panel=curve_plot(records,task,width,0,0,size=333)
            panel.translate(8+(i%3)*347,535-(i//3)*175)
            drawing.add(panel)
        renderPDF.draw(drawing,pdf,0,0);pdf.showPage()
        renderPM.drawToFile(drawing,str(out/f"circle_functions_n{width}.png"),fmt="PNG",dpi=150)
    pdf.save()
    (out/"plot_values.json").write_text(json.dumps(heatmap_values,indent=2)+"\n")
    print(str(out/"dense_circle_comparison.pdf"))


if __name__=="__main__":main()
