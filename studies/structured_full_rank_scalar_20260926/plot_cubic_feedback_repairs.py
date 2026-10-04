"""Plot saved scalar-repair endpoints only; no coefficient fitting or training."""
import csv
import json
from pathlib import Path
import numpy as np
from reportlab.graphics import renderPDF,renderPM
from reportlab.graphics.shapes import Drawing,String,Line
from reportlab.graphics.charts.lineplots import LinePlot
from reportlab.graphics.widgets.markers import makeMarker
from reportlab.lib import colors

HERE = Path(__file__).resolve().parent
DATA = HERE.parents[1]/'data/generated/structured_full_rank_scalar_20260926'
OUT = DATA/'cubic_feedback_repair_20260930'
OLD = DATA/'cubic_scalar_20260930'


def main():
    tasks = ['near_pair_sin9','cluster_triple_cos9','cluster_triple_cos1']
    titles = ['Close opposite-label pair','Oscillating three-point cluster','Smooth labels, same cluster']
    fig = Drawing(1110,435)
    fig.add(String(555,412,'Fitted circle functions: repairing scalar feedback',
                   textAnchor='middle',fontSize=17))
    fig.add(String(555,389,'Dense Gaussian n=1024; all models stop at training MSE 0.001',
                   textAnchor='middle',fontSize=11))
    for index,(task,title) in enumerate(zip(tasks,titles)):
        with np.load(OLD/f'{task}.npz') as saved:
            angle = np.r_[saved['angles'],2*np.pi]
            dense,original = saved['dense'],saved['scalar']
            trainangles,labels = saved['train_angles'],saved['labels']
        with np.load(OUT/'round2'/f'{task}__bounded.npz') as saved:
            repaired = saved['prediction'][:256]
        chart = LinePlot()
        chart.x,chart.y,chart.width,chart.height = 58+index*365,100,292,225
        chart.data = [list(zip(angle,np.r_[values,values[0]]))
                      for values in (dense,original,repaired)]
        chart.data.append(list(zip(np.mod(trainangles,2*np.pi),labels)))
        for k,color in enumerate(['#171717','#d47442','#008775']):
            chart.lines[k].strokeColor = colors.HexColor(color)
            chart.lines[k].strokeWidth = 1.8
        chart.lines[1].strokeDashArray = [4,3]
        chart.lines[3].strokeColor = None
        chart.lines[3].symbol = makeMarker('FilledCircle')
        chart.lines[3].symbol.fillColor = colors.HexColor('#2367ac')
        chart.lines[3].symbol.strokeColor = colors.HexColor('#2367ac')
        chart.lines[3].symbol.size = 4
        chart.xValueAxis.valueMin,chart.xValueAxis.valueMax = 0,2*np.pi
        chart.xValueAxis.valueSteps = [0,np.pi,2*np.pi]
        chart.xValueAxis.labelTextFormat = lambda x:'0' if x<1 else ('pi' if x<5 else '2pi')
        chart.xValueAxis.labels.fontSize = 9
        chart.yValueAxis.labels.fontSize = 9
        chart.yValueAxis.maximumTicks = 6
        chart.yValueAxis.visibleGrid = 1
        chart.yValueAxis.gridStrokeColor = colors.HexColor('#e8e8e8')
        fig.add(chart)
        fig.add(String(chart.x+146,354,title,textAnchor='middle',fontSize=11))
        rmsold = np.sqrt(np.mean((original-dense)**2))
        rmsnew = np.sqrt(np.mean((repaired-dense)**2))
        fig.add(String(chart.x+146,337,f'RMS difference: {rmsold:.4f} -> {rmsnew:.4f}',
                       textAnchor='middle',fontSize=10))
        fig.add(String(chart.x+146,66,'Input angle (radians)',textAnchor='middle',fontSize=9))
    for x,color,label,dash in [(105,'#171717','Dense',None),(300,'#d47442','Original scalar',[4,3]),
                               (530,'#008775','Bounded-Gram repair',None),(845,'#2367ac','Training labels',None)]:
        fig.add(Line(x,26,x+25,26,strokeColor=colors.HexColor(color),strokeWidth=2,strokeDashArray=dash))
        fig.add(String(x+33,22,label,fontSize=11))
    renderPDF.drawToFile(fig,str(OUT/'feedback_repair_functions.pdf'))
    renderPM.drawToFile(fig,str(OUT/'feedback_repair_functions.png'),fmt='PNG',dpi=72)
    rows = []
    for name in ('round2','round2_transfer','round3','round3_mode','round4','bounded_numerical_check'):
        for row in json.loads((OUT/name/'summary.json').read_text())['results']:
            rows.append(dict(round=name,**row))
    keys = ['round','task','method','fitted','train_mse','circle_rms','old_circle_rms',
            'training_states','total_states','training_seconds','nested_rms_change']
    with (OUT/'all_dynamic_repairs.csv').open('w') as stream:
        writer = csv.DictWriter(stream,fieldnames=keys,extrasaction='ignore')
        writer.writeheader()
        writer.writerows(rows)
    print(OUT/'feedback_repair_functions.png')


if __name__ == '__main__':
    main()
