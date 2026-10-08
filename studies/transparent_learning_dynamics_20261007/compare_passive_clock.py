"""Test frozen initialization-only passive coefficients against existing runs."""
import json
import numpy as np
from scipy.integrate import cumulative_trapezoid
from analyze_learning_experiment import ROOT, constants, cubic_clock, load_group


def main():
    coefficients=json.loads((ROOT/'passive_quadrature'/'coefficients.json').read_text())['frozen_coefficients']
    results={}
    for amplitude,tag,sign,suffix in ((.075,'0075',-1,''),(.15,'015',-1,''),(.6,'06',-1,''),(.6,'06',1,'_same')):
        runs=load_group(f'dense_n512_s{{seed}}_a{tag}{suffix}')
        times=runs[0]['time'];mean=np.mean([r['f'][:,2] for r in runs],0)
        c=coefficients[str(sign)];u=cubic_clock(amplitude,times,constants())
        predicted=c['k_linear']*u+c['kappa_passive']*u**3
        # Diagnostic only: does using actual residual eliminate passive error?
        diagnostic=[]
        for r in runs:
            measured=cumulative_trapezoid(amplitude-(r['f'][:,0]+sign*r['f'][:,1])/2,times,initial=0)
            diagnostic.append(c['k_linear']*measured+c['kappa_passive']*measured**3)
        results[f'Y{amplitude}_sign{sign}']=dict(dense_endpoint=float(mean[-1]),predicted_endpoint=float(predicted[-1]),
                                                max_abs_error=float(max(abs(predicted-mean))),
                                                max_error_over_final_prediction=float(max(abs(predicted-mean))/abs(mean[-1])),
                                                measured_clock_diagnostic_endpoint=float(np.mean(diagnostic,0)[-1]))
    output=ROOT/'passive_comparison';output.mkdir(exist_ok=False)
    (output/'summary.json').write_text(json.dumps(results,indent=2)+'\n')
    print(json.dumps(results,indent=2))


if __name__=='__main__':main()
