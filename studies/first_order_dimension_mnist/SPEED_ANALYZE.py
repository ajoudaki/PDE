"""Matched-horizon speed and live-allocation comparison at two widths."""
import argparse
import hashlib
import json
from pathlib import Path
import numpy as np

HERE=Path(__file__).resolve().parent
BASE=HERE.parents[1]/'data/generated/first_order_dimension_mnist'
CORE=('RUN.py','NETWORK_ENGINE.py','P1_ENGINE.py','P1_INITIALIZATION.py','DATA.py')

def analyze(output):
    destination=BASE/output
    destination.mkdir(parents=True,exist_ok=False)
    report={'scope':'Matched T100 integration speed and peak live training allocation; no predictive-accuracy claim',
            'rows':[],'aggregates':{},'repeat_checks':{},'summary_sha256':{}}
    reference_config=None
    reference_hashes=None
    for model in ('network','closure'):
        for width in (2048,4096):
            rows=[];arrays=[]
            for repetition in (1,2):
                path=BASE/f'speed4096/{model}_{width}_r{repetition}'
                summary=json.loads((path/'summary.json').read_text());config=summary['configuration']
                report['summary_sha256'][path.name]=hashlib.sha256((path/'summary.json').read_bytes()).hexdigest()
                signature=(summary['data']['metadata']['dataset_sha256'],config['seed'],config['dtype'],config['block'],config['environment']['tf32'])
                assert signature[1:]==(1729,'float32',2048,False)
                assert config['gpu']==((0 if model=='network' else 1) if repetition==1 else (1 if model=='network' else 0))
                if reference_config is None:reference_config=signature
                assert signature==reference_config
                hashes={name:config['source_sha256'][name] for name in CORE}
                if reference_hashes is None:reference_hashes=hashes
                assert hashes==reference_hashes
                assert config['width']==width and config['model']==model
                assert config['step']==(.25 if model=='network' else .125)
                assert summary['final_time']==100 and summary['stop_reason']=='horizon'
                assert summary['steps']==(400 if model=='network' else 800)
                assert not config['continue_validation'] and not config['precision_probe']
                with np.load(path/'observations.npz',allow_pickle=False) as a:
                    values={k:a[k].copy() for k in ('times','train_predictions','val_predictions','gram1','gram2')}
                assert all(np.isfinite(value).all() for value in values.values())
                arrays.append(values)
                row={'model':model,'width':width,'repetition':repetition,'gpu':config['gpu'],
                     'physical_time':summary['final_time'],'steps':summary['steps'],
                     'integration_seconds':summary['integration_seconds'],
                     'seconds_per_physical_time':summary['integration_seconds']/summary['final_time'],
                     'milliseconds_per_heun_step':summary['integration_seconds']/summary['steps']*1000,
                     'initialization_seconds':summary['initialization_seconds'],
                     'training_wall_seconds':summary['training_wall_seconds'],
                     'peak_allocated_mib':summary['peak_allocated_bytes']/2**20,
                     'moving_state_mib':summary['moving_state_bytes']/2**20,
                     'retained_model_mib':summary['retained_model_bytes']/2**20}
                report['rows'].append(row);rows.append(row)
            errors={key:float(np.max(np.abs(arrays[0][key].astype(np.float64)-arrays[1][key]))) for key in arrays[0]}
            assert rows[0]['moving_state_mib']==rows[1]['moving_state_mib']
            assert rows[0]['retained_model_mib']==rows[1]['retained_model_mib']
            assert max(errors.values())<=1e-5,errors
            report['repeat_checks'][f'{model}_{width}']={'max_absolute_errors':errors,
                       'all_bitwise_identical':all(np.array_equal(arrays[0][key],arrays[1][key]) for key in arrays[0]),'passed':True}
            times=[r['integration_seconds'] for r in rows]
            report['aggregates'][f'{model}_{width}']={
                'mean_integration_seconds':float(np.mean(times)),
                'integration_seconds_range':[min(times),max(times)],
                'timing_relative_range':(max(times)-min(times))/np.mean(times),
                'timing_variability_flag':bool((max(times)-min(times))/np.mean(times)>.15),
                'mean_training_wall_seconds':float(np.mean([r['training_wall_seconds'] for r in rows])),
                'peak_allocated_mib_range':[min(r['peak_allocated_mib'] for r in rows),max(r['peak_allocated_mib'] for r in rows)],
                'moving_state_mib':rows[0]['moving_state_mib'],'retained_model_mib':rows[0]['retained_model_mib']}
    report['ratios']={}
    for width in (2048,4096):
        n=report['aggregates'][f'network_{width}'];c=report['aggregates'][f'closure_{width}']
        report['ratios'][str(width)]={'network_over_closure_integration_time':n['mean_integration_seconds']/c['mean_integration_seconds'],
               'closure_peak_memory_reduction':1-max(c['peak_allocated_mib_range'])/max(n['peak_allocated_mib_range'])}
        report['ratios'][str(width)]['same_gpu_time_ratios']={str(gpu):next(r['integration_seconds'] for r in report['rows'] if r['width']==width and r['gpu']==gpu and r['model']=='network')/next(r['integration_seconds'] for r in report['rows'] if r['width']==width and r['gpu']==gpu and r['model']=='closure') for gpu in (0,1)}
    report['width_doubling']={model:{'time_factor':report['aggregates'][f'{model}_4096']['mean_integration_seconds']/report['aggregates'][f'{model}_2048']['mean_integration_seconds'],
            'peak_memory_factor':max(report['aggregates'][f'{model}_4096']['peak_allocated_mib_range'])/max(report['aggregates'][f'{model}_2048']['peak_allocated_mib_range'])} for model in ('network','closure')}
    report['core_source_hashes']=reference_hashes
    report['analysis_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    (destination/'summary.json').write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    keys=list(report['rows'][0]);csv=np.array([[r[k] for k in keys] for r in report['rows']],dtype=object)
    np.savetxt(destination/'timings.csv',csv,fmt='%s',delimiter=',',header=','.join(keys),comments='')
    print(json.dumps({k:report[k] for k in ('aggregates','ratios','width_doubling','repeat_checks')},indent=2))

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--output',default='speed4096_analysis_001');a=p.parse_args();analyze(a.output)
