"""Adaptive N3--N5 aggregation of unchanged frozen endpoint-analysis evidence.

No training, job-data modification, or replacement of the original verdict.
See PAIR_ENDPOINT_SCOPE.md for the post-observation scope declaration.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path


def _sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def _analysis():
    path=Path(__file__).with_name('ANALYZE.py')
    spec=importlib.util.spec_from_file_location('frozen_endpoint_analysis',path)
    module=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def analyze_focused(manifest_path,verification_path):
    """Return a separately named adaptive verdict; retain original raw analysis."""
    manifest_path=Path(manifest_path).resolve()
    verification_path=Path(verification_path).resolve()
    manifest=json.loads(manifest_path.read_text())
    verification=json.loads(verification_path.read_text())
    module=_analysis()
    # This changes only the requested comparison of an in-memory manifest.
    # The complete original job set, trajectories and saved manifest stay intact.
    request=dict(manifest,pair=[3,5],correctness=verification)
    original=module.analyze_confirmation(request)
    pair=original['adjacent_pairs']['3-5']
    required={f'cl_N{n}_{role}' for n in (3,5) for role in ('main','fine','half')}
    required.update(('net_n8192_s11','net_n8192_s29','net_n8192_s47',
                     'net_n4096_s11','net_n8192_s11_half','net_n4096_s11_double'))
    possible=required|{'cl_N3_finest','cl_N5_finest'}
    present=set(manifest['jobs'])
    relevant=sorted(present & possible)
    excluded=sorted(present-possible)
    unknown=sorted(set(excluded)-{f'cl_N1_{role}' for role in ('main','fine','finest','half')})
    missing=sorted(required-present)
    focused_settling={name:original['settling'][name] for name in relevant}
    controls={}
    excluded_controls={}
    for name,value in original['numerical_controls'].items():
        destinations=controls if value.get('a') in relevant and value.get('b') in relevant else excluded_controls
        destinations[name]=value
    uncertainty_sources={name:value for name,value in controls.items()
                         if value['category']!='earlier_quadrature'}
    uncertainty={}
    for metric in ('gap_rms','gap_max'):
        witness=max(uncertainty_sources,key=lambda name:uncertainty_sources[name][metric],default=None)
        uncertainty[metric]=dict(value=uncertainty_sources[witness][metric] if witness else None,witness=witness)
    common_time=original['common_time']
    relevant_times={name:float(verification.get('jobs',{}).get(name,{}).get('last_time',
                         original['settling'][name]['time'])) for name in relevant}
    # The analysis's requested-time field is not a substitute for a job's actual
    # saved final time; read this field directly from each original record.
    for name in relevant:
        path=manifest['jobs'][name]
        directory=Path(path if isinstance(path,str) else path['path'])
        record=json.loads((directory/'record.json').read_text())
        relevant_times[name]=float(record['last_time'])
    common_final=all(abs(t-common_time)<1e-7 for t in relevant_times.values())
    margin=bool(pair.get('refined')) and all(
        uncertainty[metric]['value'] is not None and
        min(pair['main'][metric],pair['refined'][metric])>
        module.THRESHOLDS['uncertainty_factor']*uncertainty[metric]['value']
        for metric in ('gap_rms','gap_max'))
    verification_matches=(verification.get('manifest_sha256')==_sha(manifest_path)
                          and Path(verification.get('manifest','')).resolve()==manifest_path)
    gates=dict(required_jobs_present=not missing,only_declared_jobs=not unknown,
               complete_original_correctness_passed=original['correctness_passed'],
               verification_matches_manifest=verification_matches,
               original_missing_requirements_clear=not original['missing'],
               same_common_final_time=common_final,
               original_horizon_rule_passed=original['horizon_rule_passed'],
               relevant_models_settled=bool(relevant) and all(v['passed'] for v in focused_settling.values()),
               relevant_numerical_controls_passed=bool(controls) and all(v['passed'] for v in controls.values()),
               main_shape_visible=pair.get('main_visible',False),
               main_previous100_visible=pair.get('previous100_visible',False),
               refined_shape_visible=pair.get('refined_visible',False),
               refined_previous100_visible=pair.get('refined_previous100_visible',False),
               focused_uncertainty_margin_passed=margin)
    passed=all(gates.values())
    training=pair.get('matched_training_fit',dict(passed=False))
    u=uncertainty['gap_rms']['value']
    error_excess=pair.get('higher_order_gap_rmse_excess')
    worse=(passed and u is not None and error_excess is not None
           and error_excess>=module.THRESHOLDS['worse_rmse']
           and error_excess>module.THRESHOLDS['uncertainty_factor']*4*u)
    result=dict(kind='adaptive_focused_pair_endpoint_interpretation',pair=[3,5],
                common_time=common_time,focused_validated_separation=passed,
                focused_off_support_selection=passed and training['passed'],
                focused_higher_order_worse=bool(worse),
                interpretation=('Adaptive finite-time N3–N5 separation meets the stated pair settling diagnostics and numerical margins.'
                    if passed else 'The adaptive finite-time N3–N5 separation remains unresolved under its stated gates.'),
                not_claimed=['Original all-model contract success','Infinite-time equilibrium',
                             'Monotone higher-order accuracy','Hierarchy convergence'],
                thresholds=module.THRESHOLDS,gates=gates,
                failed_gates=[name for name,value in gates.items() if not value],
                relevant_jobs=relevant,relevant_final_times=relevant_times,
                missing_jobs=missing,unknown_jobs=unknown,
                excluded_jobs={name:dict(reason='N1 does not enter the N3–N5 or network-reference prediction',
                                         settling=original['settling'].get(name),
                                         validation=original['validation'].get(name)) for name in excluded},
                focused_settling=focused_settling,focused_numerical_controls=controls,
                excluded_aggregate_controls=excluded_controls,focused_uncertainty=uncertainty,
                pair_raw_evidence=pair,matched_training_fit=training,
                higher_order_error_uncertainty_bound=None if u is None else 4*u,
                original_all_model_verdict=dict(validated_separation=original['validated_separation'],
                    all_settled=original['all_settled'],numerical_passed=original['numerical_passed'],
                    correctness_passed=original['correctness_passed'],uncertainty=original['uncertainty']),
                original_frozen_analysis=original,
                provenance=dict(manifest=str(manifest_path),manifest_sha256=_sha(manifest_path),
                    verification=str(verification_path),verification_sha256=_sha(verification_path),
                    focused_source_sha256=_sha(__file__),
                    scope_note=str(Path(__file__).with_name('PAIR_ENDPOINT_SCOPE.md').resolve()),
                    scope_note_sha256=_sha(Path(__file__).with_name('PAIR_ENDPOINT_SCOPE.md')),
                    frozen_analysis_sha256=_sha(Path(__file__).with_name('ANALYZE.py'))))
    result.update(focused_separation=passed,
                  all_compared_settled=gates['same_common_final_time'] and gates['relevant_models_settled'],
                  uncertainty=uncertainty,selected_pair=pair,
                  full_contract_pass=original['validated_separation'])
    return module._jsonable(result)


def evaluate_focus(manifest_or_path,verification_path):
    """AUTO-facing API; a dict must equal the complete saved verified manifest."""
    if isinstance(manifest_or_path,dict):
        verification=json.loads(Path(verification_path).read_text())
        source=Path(verification['manifest'])
        if json.loads(source.read_text())!=manifest_or_path:
            raise ValueError('In-memory manifest differs from the saved verified manifest')
        manifest_or_path=source
    return analyze_focused(manifest_or_path,verification_path)


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--manifest',required=True)
    parser.add_argument('--verification',required=True)
    parser.add_argument('--out',required=True)
    args=parser.parse_args()
    result=analyze_focused(args.manifest,args.verification)
    destination=Path(args.out)
    destination.parent.mkdir(parents=True,exist_ok=True)
    destination.write_text(json.dumps(result,indent=2,allow_nan=False)+'\n')
    print(json.dumps({key:result[key] for key in ('kind','common_time','focused_validated_separation',
          'focused_off_support_selection','failed_gates','focused_uncertainty')},indent=2))


if __name__=='__main__':
    main()
