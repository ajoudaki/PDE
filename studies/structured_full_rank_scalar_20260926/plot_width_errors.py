"""Quick log-log figures from saved fitted-function RMS tables; no training."""
import json,math,csv,hashlib
from pathlib import Path
import numpy as np
from reportlab.graphics.shapes import Drawing,String,Line,Rect
from reportlab.graphics.charts.lineplots import LinePlot
from reportlab.graphics.widgets.markers import makeMarker
from reportlab.graphics import renderPM,renderSVG,renderPDF
from reportlab.lib.colors import HexColor,Color
from circle_tasks import TASKS

ROOT=Path(__file__).resolve().parents[2]
BASE=ROOT/'data/generated/structured_full_rank_scalar_20260926'
OUT=BASE/'width_error_plots_20260926_ready'
COLORS=['#0072B2','#E69F00','#009E73','#D55E00','#CC79A7','#6A3D9A',
        '#8C564B','#666666','#56B4E9','#B79A00','#E7298A','#222222']
LABELS=['Two-point cosine 1','Two-point cosine 3','Nearby opposite labels',
 'Three-point cosine 3','Three-point mixed','Clustered cosine 9',
 'Broad ridge (2048 only)','Sharp ridge (2048 only)',
 'Alternating 3','Alternating 5','Alternating 9','Multiscale (2048 only)']


def load():
 paths=[BASE/'dense_main_function_analysis_20260926/summary.json',BASE/'wide_hd_analysis_20260926/summary.json']
 small,wide=[json.loads(p.read_text()) for p in paths]
 rows=[]
 for i,t in enumerate(TASKS):
  for model,method in [('HD','hd'),('Gaussian control','gaussian_control')]:
   for n in [128,256]:
    c=next(c for c in small['function_cells'] if c['task']==t.name and c['width']==n and c['method']==method and c['stage']=='fit6')
    if c.get('function_rms_distance_mean') is not None:
     rows.append(dict(task=t.name,model=model,width=n,RMS=c['function_rms_distance_mean'],seeds=12,train_MSE=1e-6))
   c=next(c for c in wide['task_summary'] if c['task']==t.name)
   rows.append(dict(task=t.name,model=model,width=2048,RMS=c['HD_G_mean' if model=='HD' else 'G2_G_mean'],seeds=1,train_MSE=1e-4))
 return paths,rows


def panel(rows,model):
 d=Drawing(720,570)
 d.add(String(65,535,'HD versus Gaussian' if model=='HD' else 'Gaussian versus independent Gaussian',fontName='Helvetica-Bold',fontSize=17))
 lp=LinePlot();lp.x=70;lp.y=80;lp.width=615;lp.height=420
 lp.joinedLines=1
 lp.xValueAxis.valueMin=math.log10(105);lp.xValueAxis.valueMax=math.log10(2450)
 lp.xValueAxis.valueSteps=list(np.log10([128,256,512,1024,2048]))
 lp.xValueAxis.labelTextFormat=lambda v:str(round(10**v))
 lp.xValueAxis.labels.fontSize=11
 lp.yValueAxis.valueMin=math.log10(.0004);lp.yValueAxis.valueMax=math.log10(.2)
 ticks=[.0005,.001,.002,.005,.01,.02,.05,.1,.2]
 lp.yValueAxis.valueSteps=list(np.log10(ticks))
 lp.yValueAxis.labelTextFormat=lambda v:f'{10**v:g}'
 lp.yValueAxis.labels.fontSize=10
 for axis in [lp.xValueAxis,lp.yValueAxis]:
  axis.visibleGrid=1;axis.gridStrokeColor=HexColor('#e5e7eb');axis.gridStrokeWidth=.6
  axis.strokeColor=HexColor('#7b8490')
 data=[]
 for t in TASKS:
  rr=sorted([r for r in rows if r['task']==t.name and r['model']==model],key=lambda r:r['width'])
  data.append([(math.log10(r['width']),math.log10(r['RMS'])) for r in rr])
 # Arbitrary vertical position: this is a slope guide, never a fitted curve.
 data.append([(math.log10(n),math.log10(.14*(n/128)**(-.5))) for n in [128,256,2048]])
 lp.data=data
 for i,col in enumerate(COLORS):
  lp.lines[i].strokeColor=Color(*HexColor(col).rgb(),alpha=.6)
  lp.lines[i].strokeWidth=1.05
  marker=makeMarker('FilledCircle');marker.size=7
  marker.fillColor=HexColor(col);marker.strokeColor=HexColor(col)
  lp.lines[i].symbol=marker
 lp.lines[len(COLORS)].strokeColor=HexColor('#333333')
 lp.lines[len(COLORS)].strokeWidth=1.25
 lp.lines[len(COLORS)].strokeDashArray=[5,4]
 d.add(lp)
 d.add(String(280,31,'Width n (log scale)',fontSize=12))
 d.add(String(70,513,'Absolute circle RMS difference (log scale)',fontSize=11))
 # Slope-guide label near n=650.
 xx=70+615*(math.log10(650)-lp.xValueAxis.valueMin)/(lp.xValueAxis.valueMax-lp.xValueAxis.valueMin)
 yy=80+420*(math.log10(.14*(650/128)**(-.5))-lp.yValueAxis.valueMin)/(lp.yValueAxis.valueMax-lp.yValueAxis.valueMin)
 d.add(String(xx,yy+9,'slope -1/2 guide',fontSize=10,fillColor=HexColor('#333333')))
 return d


def legend(d,y):
 for i,label in enumerate(LABELS):
  x=30+(i%4)*357;yy=y-(i//4)*23
  d.add(Line(x,yy+3,x+19,yy+3,strokeColor=HexColor(COLORS[i]),strokeWidth=3))
  d.add(String(x+27,yy,label,fontSize=10,fillColor=HexColor('#25313e')))


def main():
 OUT.mkdir(parents=True,exist_ok=False)
 paths,rows=load()
 d=Drawing(1460,790);d.add(Rect(0,0,1460,790,fillColor=HexColor('#ffffff'),strokeColor=None))
 d.add(String(30,758,'Fitted circle-function discrepancies versus network width',fontSize=21,fontName='Helvetica-Bold'))
 d.add(String(30,735,'Absolute RMS(f_candidate - f_Gaussian); no division by Gaussian signal amplitude. Both axes logarithmic.',fontSize=12))
 for x,model,name in [(0,'HD','hd_width_errors'),(730,'Gaussian control','gaussian_width_errors')]:
  p=panel(rows,model);p.translate(x,180);d.add(p)
 legend(d,188)
 d.add(String(30,96,'Points: means over 12 paired seeds at n=128,256; one paired seed at n=2048. Lines only connect observed points.',fontSize=11))
 d.add(String(30,75,'Stopping MSE: 1e-6 at n=128,256; 1e-4 at n=2048. Gaussian control changes the middle draw, with shared outer initialization.',fontSize=11))
 d.add(String(30,54,'Three tasks have no fitted lower-width comparison. The dashed line is a reference slope, not an extrapolation or convergence claim.',fontSize=11))
 renderPM.drawToFile(d,str(OUT/'width_errors.png'),fmt='PNG',dpi=72)
 renderSVG.drawToFile(d,str(OUT/'width_errors.svg'));renderPDF.drawToFile(d,str(OUT/'width_errors.pdf'))
 for model,name in [('HD','hd_width_errors'),('Gaussian control','gaussian_width_errors')]:
  q=Drawing(1460,790);q.add(Rect(0,0,1460,790,fillColor=HexColor('#ffffff'),strokeColor=None))
  p=panel(rows,model);p.translate(365,180);q.add(p);legend(q,188)
  q.add(String(30,94,'12-seed means at n=128,256; one paired seed at n=2048. Training MSE stops differ: 1e-6 versus 1e-4.',fontSize=11))
  q.add(String(30,72,'Absolute function RMS; dashed line is a slope -1/2 guide only. Three tasks have n=2048 data only.',fontSize=11))
  renderPM.drawToFile(q,str(OUT/(name+'.png')),fmt='PNG',dpi=72)
 with (OUT/'plotted_values.csv').open('w') as f:
  w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
 provenance={'inputs':{str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'new_training':False}
 (OUT/'provenance.json').write_text(json.dumps(provenance,indent=2)+'\n')
 print(OUT/'width_errors.png')

if __name__=='__main__':main()
