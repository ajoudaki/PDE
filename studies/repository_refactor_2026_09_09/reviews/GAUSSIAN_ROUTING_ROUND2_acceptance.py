"""Bounded actual-interface probes. Never call scientific producer bodies."""
import ast
from contextlib import ExitStack, redirect_stdout, redirect_stderr
from fractions import Fraction
import hashlib
import importlib
import io
import json
from pathlib import Path
import runpy
import sys
import tempfile
from types import ModuleType
from unittest import mock

from bounded import BASE, OUT
from studies._output_paths import StudyPaths

rows = []
class StopWork(RuntimeError):
    pass

def note(name, **details):
    row = {'check': name, **details}
    rows.append(row)
    print(json.dumps(row, default=str, sort_keys=True))

def module(relative):
    return importlib.import_module('studies.' + relative.replace('/', '.').removesuffix('.py'))

def path_contracts():
    for name in ('causal_flow_peeling_calculus/experiments/adaptive_query_probe.py',
                 'd3_arctan_closure_program/analyze_gpu_high_moment_tail.py',
                 'mfp_gaussian_calculus/depth_order5/audit/compare_frozen.py',
                 'mfp_identity_compiler/linear_gaussian_program/depth2_all_order_search/audit_hankel40.py',
                 'mfp_linear_growth_uniform_counterexample/full_l2_paired_transition.py'):
        paths = StudyPaths(BASE / 'studies' / name)
        fresh = paths.parse([], inputs=True)
        historical = paths.parse(['--historical-inputs'], inputs=True)
        assert fresh.input_dir == fresh.output_dir
        assert historical.input_dir.is_relative_to(paths.historical)
        assert historical.output_dir == fresh.output_dir
        rejected = []
        for target in (BASE / 'studies' / name, paths.historical / 'no-write',
                       BASE / 'data/generated/another_study/no-write'):
            try:
                paths.require_output(target)
            except ValueError:
                rejected.append(str(target))
        assert len(rejected) == 3
        assert paths.require_output(OUT / 'scratch-unused') == OUT / 'scratch-unused'
        note('StudyPaths', source=name, fresh_input=fresh.input_dir,
             fresh_output=fresh.output_dir, historical_input=historical.input_dir, rejected=rejected)
    with tempfile.TemporaryDirectory() as scratch:
        root = Path(scratch)
        target = BASE / 'data/historical/studies/mfp_gaussian_calculus/depth_order5_scalar/multi_observable/audit/H3_NORMALIZED_SINE_RESULT.json'
        link = root / target.name
        link.symlink_to(target)
        shared = StudyPaths(BASE / 'studies/mfp_gaussian_calculus/study_paths.py')
        try:
            shared.require_output(root)
        except ValueError as exc:
            shared_result = str(exc)
        gaussian = module('mfp_gaussian_calculus/study_paths.py')
        accepted = gaussian.require_output(root)
        assert link.resolve() == target
        note('Gaussian guard retained-child alias', accepted_directory=accepted,
             child=link.name, resolved_write_target=target, shared_guard_refusal=shared_result,
             limit='Only guard and path resolution executed; no target write or postprocessing')

def parser_only():
    for relative, suffix, first_file in (
        ('d3_arctan_closure_program/analyze_gpu_high_moment_tail.py', 'gpu_tail_results', 'tail_main_n256_h0.01.npz'),
        ('d3_arctan_closure_program/analyze_gpu_gauge_block_gradient.py', 'gpu_gauge_gradient_results', 'gauge_main_h001_eps002_fp32_n256.npz'),
        ('d3_arctan_closure_program/analyze_gpu_weighted_offcolumn_response.py', 'gpu_weighted_response_results', 'weighted_main_h001_eps002_fp32_n256.npz'),
    ):
        m = module(relative)
        for flags in ([], ['--historical-inputs'], ['--input-dir', str(OUT / 'selected')]):
            with mock.patch.object(sys, 'argv', [relative] + flags), \
                 mock.patch.object(Path, 'mkdir') as mkdir, \
                 mock.patch.object(m.np.random, 'default_rng', return_value=object()), \
                 mock.patch.object(m, 'load', side_effect=StopWork('before first data read')) as read:
                try:
                    m.main()
                except StopWork:
                    pass
            selected = read.call_args.args[0]
            expected = ((OUT / 'selected') if '--input-dir' in flags else m.PATHS.input_dir(historical=bool(flags), relative=suffix)) / first_file
            assert selected == expected
            note('D3 actual main input selection', source=relative, flags=flags, selected=selected,
                 output_directory=mkdir.call_args, retained_exists=selected.is_file() if flags == ['--historical-inputs'] else 'not inspected',
                 limit='mkdir and RNG stubbed; first load raises before reading data or analysis')
    for relative in ('causal_flow_peeling_calculus/experiments/adaptive_query_probe.py',
                     'causal_flow_peeling_calculus/experiments/hermite_tail_probe.py',
                     'causal_flow_peeling_calculus/experiments/koopman_taylor_probe.py',
                     'causal_flow_peeling_calculus/experiments/l1_koopman_obstruction.py',
                     'mfp_linear_growth_uniform_counterexample/full_l2_paired_transition.py'):
        m = module(relative)
        with mock.patch.object(sys, 'argv', [relative, '--help']), redirect_stdout(io.StringIO()) as capture:
            try:
                m.main()
            except SystemExit as exc:
                assert exc.code == 0
        assert '--output-dir' in capture.getvalue()
        note('Actual help', source=relative, output_option=True, limit='argument parser exits before main work')

def identity_and_linear():
    lin = module('mfp_linear_growth_uniform_counterexample/map_inputs.py')
    fresh = lin.parse_map_path([])
    old = lin.parse_map_path(['--historical-inputs'])
    assert old.is_file()
    with mock.patch.object(Path, 'read_text', autospec=True, return_value='{"probe": 1}') as read:
        assert lin.load_map() == {'probe': 1}
        assert read.call_args.args[0] == fresh
        lin.load_map(old)
        assert read.call_args.args[0] == old
    note('Linear map loader', fresh=fresh, historical=old, historical_sha256=hashlib.sha256(old.read_bytes()).hexdigest(), limit='JSON fixture for loader dispatch; actual historical file hashed only')
    # sympy is absent. This blank module is only an import placeholder. Any
    # attribute use will fail; all scientific entry points stop before use.
    with mock.patch.dict(sys.modules, {'sympy': ModuleType('sympy')}):
        for relative, entry in (
            ('mfp_identity_compiler/linear_gaussian_program/depth2_all_order_search/run_search.py', 'depth2_taylor'),
            ('mfp_identity_compiler/linear_gaussian_program/depth2_all_order_search/spectral_closure.py', None),
            ('mfp_identity_compiler/linear_gaussian_program/depth2_all_order_search/audit_hankel40.py', None),
        ):
            m = module(relative)
            for flags in ([], ['--historical-inputs']) if entry is None else ([],):
                with ExitStack() as stack:
                    stack.enter_context(mock.patch.object(sys, 'argv', [relative] + flags))
                    if entry:
                        stop = stack.enter_context(mock.patch.object(m, entry, side_effect=StopWork('before coefficient work')))
                    else:
                        stop = stack.enter_context(mock.patch.object(Path, 'read_text', autospec=True, side_effect=StopWork('before input read')))
                    try:
                        m.main()
                    except StopWork:
                        pass
                note('Identity actual main selection', source=relative, flags=flags,
                     selected=str(stop.call_args.args[0]) if entry is None else 'producer argument parser reached',
                     generated_default=m.PATHS.input_dir(),
                     limit='Blank sympy import placeholder; stopped at first data read or depth2_taylor call')

def frozen_loaders():
    refs = module('mfp_gaussian_calculus/depth_order5_scalar/audit/reference_maps.py')
    audit = module('mfp_gaussian_calculus/depth_order5_scalar/primary/audit_full_scalar_recurrence.py')
    original = dict(refs.REFERENCE)
    for depth in (2, 3, 4):
        retained = refs.historical_reference_path(depth)
        loaded = refs.load_reference(depth)
        selected = audit.load_selected_reference(depth, refs.HISTORICAL_ROOT)
        assert loaded == selected
        note('Actual frozen coefficient readers', depth=depth, historical=retained,
             counts={key: len(value) for key, value in loaded.items()},
             expected_hash=refs.REFERENCE[depth][1], generated_selection=audit.selected_reference(depth, audit.selected_input_root())[0],
             limit='Retained JSON digest/schema/count reading and canonicalization only; no candidate compilation')
    assert original == refs.REFERENCE
    assert audit.selected_input_root(historical_inputs=True) == refs.HISTORICAL_ROOT
    try:
        audit.selected_input_root(OUT, historical_inputs=True)
    except ValueError:
        note('Gaussian conflicting input modes', rejected=True, shared_reference_table_unchanged=True)

def retired_and_dispatch():
    report = module('mfp_gaussian_calculus/depth_order5/primary/build_self_contained_report.py')
    with mock.patch.object(report, 'build_bytes', side_effect=StopWork('report work entered')) as build:
        try:
            report.build()
        except StopWork:
            note('Unguarded report callable', entry='build', scientific_or_report_work_calls=build.call_count,
                 code_file=report.build.__code__.co_filename, first_line=report.build.__code__.co_firstlineno,
                 limit='build_bytes tripwire stops before report source reads or writes')
    try:
        report.main()
    except RuntimeError as exc:
        note('Report CLI main refusal', message=str(exc))
    reducer = module('mfp_gaussian_calculus/depth_order5_observables/independent/reduce_frozen_head.py')
    digest = hashlib.sha256(reducer.SOURCE.read_bytes()).hexdigest()
    assert digest == reducer.SOURCE_SHA256
    def stop_reduce(frame, event, arg):
        if event == 'call' and frame.f_code.co_filename == reducer.__file__ and frame.f_code.co_name == 'reduce':
            raise StopWork('CLI reached reduce() before any refusal')
        return stop_reduce
    try:
        sys.settrace(stop_reduce)
        with mock.patch.object(sys, 'argv', [reducer.__file__]):
            runpy.run_path(reducer.__file__, run_name='__main__')
    except StopWork as exc:
        note('Unguarded frozen-head CLI', message=str(exc), frozen_source_digest_matches=True,
             recurrence_output=reducer.HERE / 'FROZEN_GAMMA04_REDUCED_RECURRENCE.json',
             formula_output=reducer.HERE / 'FROZEN_GAMMA04_REDUCED_TRANSITIONS.md',
             limit='Trace abort at reduce function call, before first body line; no reduction or artifact generation')
    finally:
        sys.settrace(None)
    runner = module('mfp_gaussian_calculus/order5/compiler/run_checks.py')
    test = runner.test_population_jet.test_all_frozen_coefficient_comparisons_report_zero_discrepancies
    calls = []
    def first_gate(frame, event, arg):
        if event == 'call' and frame.f_code == test.__code__:
            calls.append(frame.f_code.co_name)
            raise StopWork('package dispatch reached first frozen-comparison gate')
        return first_gate
    try:
        sys.settrace(first_gate)
        runner.run()
    except StopWork:
        pass
    finally:
        sys.settrace(None)
    try:
        test()  # this inspected test only reads two JSONs and checks flags/counts
    except FileNotFoundError as exc:
        note('Broken compiler package first gate', dispatched=calls, missing=exc.filename,
             retained_counterpart=BASE / 'data/historical/studies/mfp_gaussian_calculus/order5/independent/SYMBOLIC_Q0_PRIMARY_COMPARISON.json',
             limit='Actual selected check only, two JSON reads; package loop stopped before all scientific tests')

def report_build_routing():
    report = module('mfp_program_history/report/build_report.py')
    assert report.OUTPUT_DIR == BASE / 'data/generated/mfp_program_history/report'
    assert report.BUILD_DIR.parent == report.OUTPUT_DIR
    assert report.MARKDOWN_DIR.parent == report.BUILD_DIR
    assert all(path.is_relative_to(BASE / 'studies/mfp_program_history') and path.is_file() for path in report.SOURCES)
    with mock.patch.object(report, 'protect_markdown', side_effect=StopWork('before payload conversion')), \
         mock.patch.object(Path, 'exists', return_value=False), mock.patch.object(Path, 'mkdir', autospec=True) as mkdir:
        try:
            report.main()
        except StopWork:
            pass
    assert mkdir.call_args.args[0] == report.MARKDOWN_DIR
    note('History report build routing', output=report.REPORT_PDF, build=report.BUILD_DIR,
         source_payloads=report.SOURCES, wrapper=report.REPORT_TEX,
         limit='Checked current paths and main dispatch; mkdir mocked and stopped before payload reads, TeX execution or PDF writes')

if __name__ == '__main__':
    for probe in (path_contracts, parser_only, identity_and_linear, frozen_loaders, retired_and_dispatch, report_build_routing):
        try:
            probe()
        except Exception as exc:
            note('DIAGNOSTIC ERROR', probe=probe.__name__, error=repr(exc))
    (OUT / 'acceptance.json').write_text(json.dumps(rows, indent=2, default=str) + '\n')
