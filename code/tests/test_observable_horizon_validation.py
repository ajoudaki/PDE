"""Deterministic worker/supervisor checks; no research trajectory is executed.

Predeclared local cap before tests: 120 CPU seconds and 180 wall seconds, one
numerical thread; generated scratch only in H4_VALIDATION_TEST_SCRATCH. This is
part of the 600-CPU-second observable-test allowance. The only solver steps
use a small manufactured state
and four steps of length 1/100. No Gaussian initialization is run.

Run code/tests/test_observable_horizon_validation.py from the edition root with
PYTHONPATH=code, PYTHONDONTWRITEBYTECODE=1 and the three BLAS/OMP thread variables
set to one. Execute under timeout 180s; keep command/environment/source hashes,
exit status and output log in a fresh directory under data/established.
Set H4_VALIDATION_TEST_SCRATCH and TMPDIR to that directory; the complete
setup for the full suite is in code/README.md.
"""
from decimal import Decimal
from fractions import Fraction
import json
import os
from pathlib import Path
import resource
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

import numpy as np

from pde.observable_arithmetic import Arithmetic
from pde.observable_fixed import Fixed
from pde.observable_solver import State, DataLaw
from pde import observable_solver as solver
from scripts import validate_observable_horizon as worker
from scripts import run_observable_validation as supervisor


def fixture(ar=None):
    ar = ar or Arithmetic()
    A = ar.array
    F = Fraction
    state = State(A([[1, F(1, 5)], [1, F(-1, 3)]]), A([[F(1, 5), F(-2, 3)], [F(3, 5), F(1, 2)]]),
                  A([[F(1, 4), F(-3, 5)], [F(2, 3), F(1, 3)]]), A([F(1, 3), F(2, 3)]),
                  A([[1, F(1, 3)], [1, F(-1, 4)]]), A([F(1, 10), F(-1, 12)]), A([F(1, 2), F(1, 2)]),
                  A([[F(1, 3), F(1, 5)], [F(-1, 7), F(1, 4)]]),
                  A([[F(1, 4), F(1, 5)], [F(-1, 8), F(1, 4)]]), ar,
                  {"fixture": "manufactured deterministic state"}).validate()
    data = DataLaw(A([[1, 0], [0, 1]]), A([1, -1]), A([F(1, 2), F(1, 2)]), {"fixture": True}).validate(ar)
    return state, data


def decode_array(record, ar):
    if ar.digits is None:
        values = [float.fromhex(value) for value in record["values"]]
    elif ar.backend == "rational":
        values = [Fixed.from_units(int(value, 16), ar.digits) for value in record["values"]]
    else:
        values = [Decimal(value) for value in record["values"]]
    return np.asarray(values, dtype=ar.dtype).reshape(record["shape"])


class ScratchTest(unittest.TestCase):
    def setUp(self):
        scratch = os.environ.get("H4_VALIDATION_TEST_SCRATCH")
        if not scratch:
            self.fail("H4_VALIDATION_TEST_SCRATCH must name fresh test scratch; see code/README.md")
        Path(scratch).mkdir(parents=True, exist_ok=True)
        self.temporary = tempfile.TemporaryDirectory(prefix="deterministic_", dir=scratch)
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)


class ObservationTests(ScratchTest):
    def test_exact_encoding_retains_signed_zero_and_sub_float_difference(self):
        encoded = worker.encode_array(np.array([0., -0.]), Arithmetic())
        self.assertNotEqual(encoded["values"][0], encoded["values"][1])
        ar = Arithmetic(60)
        values = ar.array(["1", "1.0000000000000000000000000000000000000001"])
        self.assertEqual(float(values[0]), float(values[1]))
        encoded = worker.encode_array(values, ar)
        self.assertNotEqual(encoded["values"][0], encoded["values"][1])
        np.testing.assert_array_equal(decode_array(encoded, ar), values)

    def test_saved_pair_loss_and_prediction_consistency_all_backends(self):
        for index, ar in enumerate((Arithmetic(), Arithmetic(40), Arithmetic(24, "rational"))):
            state, data = fixture(ar)
            signature = worker.frozen_signature(state, data)
            circle = solver.circle_inputs(8, ar)
            row = worker.save_observation(self.root, index, Fraction(1, 200), state, data, circle, block_size=1)
            exact = json.loads((self.root/row["exact_json"]).read_text())
            self.assertEqual(exact["time"], "1/200")
            self.assertEqual(exact["format"], worker.OBSERVATION_FORMAT)
            arrays = {key: decode_array(value, ar) for key, value in exact["arrays"].items()}
            with np.load(self.root/row["npz"], allow_pickle=False) as saved:
                self.assertEqual(set(saved.files), set(arrays))
                for key in arrays:
                    np.testing.assert_array_equal(saved[key], np.asarray(arrays[key], float))
            with ar.context():
                for prefix in ("first", "second"):
                    pair = arrays[prefix+"_pairs"]
                    squared = arrays[prefix+"_weights"] @ ((pair[:, :, 1]-pair[:, :, 0])**2) @ arrays["input_weights"]
                    reported = arrays["rms1" if prefix == "first" else "rms2"].item()
                    self.assertLess(abs(float(reported*reported-squared)), 1e-14)
                expected = arrays["input_weights"] @ ((arrays["training_prediction"]-arrays["labels"])**2)
                self.assertEqual(expected, arrays["loss"].item())
            np.testing.assert_array_equal(arrays["prediction"], solver.predict(state, circle, block_size=1))
            self.assertEqual(signature, worker.frozen_signature(state, data))

    def test_offmesh_observations_do_not_feed_back_into_evolution(self):
        state, data = fixture()
        h = Fraction(1, 100)
        observations, restarts = {}, {}
        timing = dict(wall=0., cpu=0.)
        final = worker.observe_path(state, data, steps=4, step_size=h,
            observation_times=[0, Fraction(1, 1000), Fraction(3, 1000), h, 2*h, 4*h],
            restart_time=2*h, block_size=1,
            observer=lambda t, s: observations.setdefault(t, s.copy()),
            checkpoint=lambda t, s: restarts.setdefault(t, s.copy()), timing=timing)
        direct = solver.evolve(state, data, steps=4, step_size=h, block_size=1)
        self.assertTrue(worker.exact_restart_comparison(final, data, direct, data)["all_exact"])
        right = solver.evolve(state, data, steps=1, step_size=h, block_size=1)
        for instant, fraction in ((Fraction(1, 1000), Fraction(1, 10)), (Fraction(3, 1000), Fraction(3, 10))):
            expected = solver.interpolate_state(state, right, fraction)
            self.assertTrue(worker.exact_restart_comparison(observations[instant], data, expected, data)["all_exact"])
        expected_restart = solver.evolve(state, data, steps=2, step_size=h, block_size=1)
        self.assertTrue(worker.exact_restart_comparison(restarts[2*h], data, expected_restart, data)["all_exact"])
        self.assertEqual(set(observations), {Fraction(0), Fraction(1, 1000), Fraction(3, 1000), h, 2*h, 4*h})

    def test_restart_comparison_covers_all_state_data_and_metadata(self):
        state, data = fixture()
        for key in worker.STATE_KEYS:
            changed = state.copy()
            getattr(changed, key).flat[0] += 1
            self.assertFalse(worker.exact_restart_comparison(state, data, changed, data)["all_exact"], key)
        for key in worker.DATA_KEYS:
            changed = DataLaw(*(getattr(data, k).copy() for k in worker.DATA_KEYS), dict(data.metadata))
            getattr(changed, key).flat[0] += 1
            self.assertFalse(worker.exact_restart_comparison(state, data, state, changed)["all_exact"], key)
        changed = state.copy()
        changed.metadata["different"] = True
        self.assertFalse(worker.exact_restart_comparison(state, data, changed, data)["all_exact"])
        changed_data = DataLaw(*(getattr(data, k).copy() for k in worker.DATA_KEYS), {"different": True})
        self.assertFalse(worker.exact_restart_comparison(state, data, state, changed_data)["all_exact"])

    def test_condition_diagnostic_singularity_is_json_serializable(self):
        state, _ = fixture()
        state.b1[:] = 0
        diagnostics = worker.conditioning_diagnostics(state)
        self.assertIsNone(diagnostics["population_1"]["condition_2"])
        self.assertEqual(diagnostics["population_1"]["condition_status"], "singular_or_unresolved")
        json.dumps(diagnostics, allow_nan=False)

    def test_supported_scope_requires_the_canonical_fixed_radius(self):
        plan = dict(supported_radius=worker.supported_radius().to_record(),
                    common=dict(law_limits={}),
                    law_parameters={"case": dict(radius="supported_radius", a="0", b="0", c="1", d="1",
                                                  scope_tag="H4_explicit_supported_T40")})
        law, _ = worker.build_law(plan, {"law": "case"})
        self.assertEqual(law.exact_description(), worker.supported_law(a=0, b=0, c=1, d=1).exact_description())
        plan["supported_radius"] = {"kind": "dyadic", "exponent": {"op": "integer", "value": "0x8"}}
        with self.assertRaises(ValueError):
            worker.build_law(plan, {"law": "case"})
        plan["law_parameters"]["case"]["radius"] = plan["supported_radius"]
        with self.assertRaises(ValueError):
            worker.build_law(plan, {"law": "case"})

    def test_workspace_scales_with_dimensions_and_not_steps(self):
        state, data = fixture(Arithmetic(24, "rational"))
        result = worker.workspace_accounting(state, data, 1)
        self.assertEqual(result["state_scalars"], sum(getattr(state, key).size for key in worker.STATE_KEYS))
        self.assertEqual(result["data_scalars"], sum(getattr(data, key).size for key in worker.DATA_KEYS))
        self.assertEqual(result["final_pair_scalars"], 2*(len(state.b1)+len(state.b2))*len(data.inputs))
        self.assertTrue(result["independent_of_elapsed_step_count"])
        self.assertGreater(result["maximum_fixed_scale_bits"], 70)
        self.assertGreater(result["evolution_scalar_slot_allowance"], result["state_scalars"])

    def test_complete_worker_record_with_manufactured_four_step_state(self):
        state, _ = fixture()
        plan = dict(version="manufactured-four-step-semantics-only", horizon="1/25", method="H3 explicit Heun",
            supported_radius={"kind": "dyadic", "exponent": {"op": "integer", "value": "0x8"}},
            law_parameters={"fixture": dict(radius={"kind": "dyadic", "exponent": {"op": "integer", "value": "0x8"}},
                                             a="-1", b="1", c="-1", d="1")},
            common=dict(law_limits={}, allow_radius_collapse=True, epsilon_cov="0.001", block_size=1,
                        circle_directions=8, observation_times=["0", "1/1000", "3/1000", "1/100", "1/50", "1/25"],
                        restart_time="1/50"),
            budget=dict(cpu_seconds_per_configuration=120),
            configurations=[dict(id="fixture", law="fixture", order=1, initialization_nodes=1,
                                population_nodes=2, digits=None, backend="decimal", nodes_per_arc=2, steps=4)])
        path, output = self.root/"plan.json", self.root/"record_output"
        path.write_text(json.dumps(plan))
        with patch.object(worker.observable_solver, "initialize", return_value=state), patch.object(worker.resource, "setrlimit"):
            self.assertEqual(worker.run(path, "fixture", output), 0)
        record = json.loads((output/"record.json").read_text())
        self.assertEqual(record["status"], "operational_pass")
        self.assertTrue(record["restart_exact"])
        self.assertTrue(all(record["restart_comparison"].values()))
        self.assertEqual([row["time"] for row in record["observations"]], plan["common"]["observation_times"])
        for filename, expected in record["outputs"].items():
            self.assertEqual(worker.digest(output/filename), expected)
        for row in record["observations"]:
            self.assertTrue((output/row["npz"]).is_file())
            self.assertTrue((output/row["exact_json"]).is_file())
        with self.assertRaises(FileExistsError):
            worker.run(path, "fixture", output)


FAKE_WORKER = '''
import argparse, hashlib, json, time
from pathlib import Path
parser=argparse.ArgumentParser()
parser.add_argument('--plan',required=True)
parser.add_argument('--id',required=True)
parser.add_argument('--output',required=True)
args=parser.parse_args()
payload=Path(args.plan).read_bytes()
plan=json.loads(payload)
configuration=next(c for c in plan['configurations'] if c['id']==args.id)
output=Path(args.output)
output.mkdir(parents=True,exist_ok=False)
record=dict(id=args.id,configuration=configuration,plan_sha256=hashlib.sha256(payload).hexdigest(),
status='operational_pass',total_seconds={'cpu':time.process_time()},peak_rss_bytes=0,
selected_worker=Path(__file__).name)
(output/'record.json').write_text(json.dumps(record))
'''


class WorkerSelectionTests(ScratchTest):
    def test_default_and_optional_worker_are_portable_and_prevalidated(self):
        scripts = self.root/"code"/"scripts"
        scripts.mkdir(parents=True)
        runner = scripts/"run_observable_validation.py"
        shutil.copyfile(supervisor.__file__, runner)
        for name in ("validate_observable_solver.py", "validate_observable_horizon.py"):
            (scripts/name).write_text(FAKE_WORKER)
        plan = dict(version="fake-workers-no-dynamics", configurations=[dict(id="fixture")],
            budget=dict(maximum_configurations=1, cpu_seconds_per_configuration=5,
                        wall_seconds_per_configuration=5, total_cpu_seconds=10, rss_bytes_per_process=128*1024*1024,
                        threads_per_process=1, parallel_trajectory_processes=1))
        path = self.root/"plan.json"
        path.write_text(json.dumps(plan))
        for selected in (None, "validate_observable_horizon.py"):
            output = self.root/("default" if selected is None else "selected")
            command = [sys.executable, "-B", str(runner), "--plan", str(path), "--output-dir", str(output)]
            if selected:
                command += ["--worker", selected]
            result = subprocess.run(command, cwd=self.root, capture_output=True, text=True, timeout=10)
            self.assertEqual(result.returncode, 0, result.stderr)
            expected = selected or "validate_observable_solver.py"
            record = json.loads((output/"fixture"/"record.json").read_text())
            self.assertEqual(record["selected_worker"], expected)
            parent = json.loads((output/"supervisor.json").read_text())
            self.assertEqual(Path(parent["worker"]).name, expected)
            self.assertEqual(parent["worker_sha256"], worker.digest(scripts/expected))
        output = self.root/"missing"
        result = subprocess.run([sys.executable, "-B", str(runner), "--plan", str(path),
                                 "--output-dir", str(output), "--worker", "missing.py"],
                                capture_output=True, text=True, timeout=10)
        self.assertNotEqual(result.returncode, 0)
        self.assertFalse(output.exists())


if __name__ == "__main__":
    resource.setrlimit(resource.RLIMIT_CPU, (120, 120))
    unittest.main(verbosity=2)
