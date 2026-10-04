"""Render saved endpoints only; no fitting or coefficient regeneration."""
import csv
import json
from pathlib import Path
from reportlab.graphics.shapes import Drawing, String, Line
from reportlab.graphics.charts.lineplots import LinePlot
from reportlab.graphics.widgets.markers import makeMarker
from reportlab.graphics import renderPDF, renderPM
from reportlab.lib import colors
import numpy as np

HERE = Path(__file__).resolve().parent
OUT = HERE.parents[1]/'data/generated/structured_full_rank_scalar_20260926/cubic_scalar_20260930'


def main():
    rows = json.loads((OUT/'summary.json').read_text())['results']
    fig = Drawing(1080,880)
    fig.add(String(540,858,'Fitted circle outputs: scalar ODE versus dense Gaussian',textAnchor='middle',fontSize=17))
    fig.add(String(540,837,'Same initialization contractions; n = 1024; each stops at training MSE 0.001',textAnchor='middle',fontSize=11))
    for index,row in enumerate(rows):
        left, bottom = 58+(index%3)*354, 595-(index//3)*260
        chart = LinePlot()
        chart.x,chart.y,chart.width,chart.height = left,bottom,280,180
        with np.load(OUT/f"{row['task']}.npz") as saved:
            angle = np.r_[saved['angles'],2*np.pi]
            chart.data = [list(zip(angle,np.r_[saved[key],saved[key][0]])) for key in ('dense','scalar')]
            chart.data.append(list(zip(np.mod(saved['train_angles'],2*np.pi),saved['labels'])))
        chart.lines[0].strokeColor = colors.HexColor('#171717')
        chart.lines[0].strokeWidth = 1.8
        chart.lines[1].strokeColor = colors.HexColor('#df6525')
        chart.lines[1].strokeWidth = 1.6
        chart.lines[1].strokeDashArray = [5,3]
        chart.lines[2].strokeColor = None
        chart.lines[2].symbol = makeMarker('FilledCircle')
        chart.lines[2].symbol.fillColor = colors.HexColor('#2c6daa')
        chart.lines[2].symbol.strokeColor = colors.HexColor('#2c6daa')
        chart.lines[2].symbol.size = 4
        chart.xValueAxis.valueMin,chart.xValueAxis.valueMax = 0,2*np.pi
        chart.xValueAxis.valueSteps = [0,np.pi,2*np.pi]
        chart.xValueAxis.labelTextFormat = lambda x: '0' if x<1 else ('pi' if x<5 else '2pi')
        chart.xValueAxis.labels.fontSize = 9
        chart.yValueAxis.labels.fontSize = 9
        chart.yValueAxis.visibleGrid = 1
        chart.yValueAxis.gridStrokeColor = colors.HexColor('#e2e2e2')
        chart.yValueAxis.maximumTicks = 5
        fig.add(chart)
        fig.add(String(left+140,bottom+215,row['task'],textAnchor='middle',fontSize=11))
        fig.add(String(left+140,bottom+199,f"Circle RMS difference = {row['scalar_dense_rms']:.4f}",textAnchor='middle',fontSize=10))
        fig.add(String(left+140,bottom-34,'Input angle (radians)',textAnchor='middle',fontSize=9))
    for x,color,label,dash in [(205,'#171717','Dense Gaussian',None),(455,'#df6525','Scalar response ODE',[5,3]),(720,'#2c6daa','Training labels',None)]:
        fig.add(Line(x,20,x+28,20,strokeColor=colors.HexColor(color),strokeWidth=2,strokeDashArray=dash))
        fig.add(String(x+36,16,label,fontSize=11))
    renderPDF.drawToFile(fig,str(OUT/'circle_functions.pdf'))
    renderPM.drawToFile(fig,str(OUT/'circle_functions.png'),fmt='PNG',dpi=72)
    with (OUT/'results.csv').open('w') as stream:
        writer = csv.writer(stream)
        writer.writerow(['task','training_samples','effective_samples','scalar_states',
                         'scalar_dense_circle_RMS','frozen_dense_circle_RMS',
                         'scalar_train_MSE','dense_train_MSE','frozen_train_MSE','frozen_fitted','scalar_flow_time',
                         'dense_flow_time','coefficient_seconds','scalar_ODE_seconds'])
        for row in rows:
            writer.writerow([row['task'],row['original_samples'],row['effective_samples'],
                             row['total_state_count'],row['scalar_dense_rms'],row['frozen_dense_rms'],
                             row['scalar']['train_mse'],row['dense_train_mse'],row['frozen']['train_mse'],row['frozen']['fitted'],
                             row['scalar']['physical_time'],row['dense_physical_time'],
                             row['coefficient_seconds'],row['scalar']['training_seconds']])
    print(OUT/'circle_functions.png')


if __name__ == '__main__':
    main()
