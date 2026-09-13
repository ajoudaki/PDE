"""Portable supervisor tests: the temporary workers perform no solver work."""
import json
import os
from pathlib import Path
import shutil
import signal
import subprocess
import sys
import tempfile
import time
import unittest

from scripts import run_observable_validation as supervisor


FAKE_WORKER = r'''
import argparse, hashlib, json, os, sys, time
from pathlib import Path
import portable_marker
p = argparse.ArgumentParser()
p.add_argument('--plan', required=True)
p.add_argument('--id', required=True)
p.add_argument('--output', required=True)
a = p.parse_args()
plan_bytes = Path(a.plan).read_bytes()
plan = json.loads(plan_bytes)
config = next(c for c in plan['configurations'] if c['id'] == a.id)
mode = config.get('mode', 'pass')
if mode == 'missing':
    sys.exit(7)
out = Path(a.output)
out.mkdir(parents=True, exist_ok=False)
record = dict(id=a.id, configuration=config,
              plan_sha256=hashlib.sha256(plan_bytes).hexdigest(),
              status='running', pid=os.getpid(),
              marker=portable_marker.VALUE,
              thread_environment={k: os.environ.get(k) for k in (
                  'OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS',
                  'BLIS_NUM_THREADS', 'VECLIB_MAXIMUM_THREADS', 'NUMEXPR_NUM_THREADS')})
path = out/'record.json'
path.write_text(json.dumps(record))
if mode == 'sleep':
    time.sleep(30)
if mode == 'cpu':
    until = time.process_time()+3
    while time.process_time() < until:
        pass
if mode == 'noisy':
    sys.stdout.write('worker-noise-'*60000)
    sys.stdout.flush()
if mode == 'malformed':
    path.write_text('{bad json')
    sys.exit(0)
if mode == 'oversized':
    path.write_bytes(b'x'*(4*1024*1024+1))
    sys.exit(0)
record.update(status='operational_pass', total_seconds={'cpu': time.process_time()},
              peak_rss_bytes=0)
if mode == 'wrong_id':
    record['id'] = 'some_other_id'
path.write_text(json.dumps(record))
print(json.dumps({'id': a.id, 'status': record['status']}))
'''


@unittest.skipUnless(sys.platform == "linux", "Linux resource-monitor tests")
class SupervisorTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        scripts = self.root / "code" / "scripts"
        scripts.mkdir(parents=True)
        self.runner = scripts / "run_observable_validation.py"
        shutil.copyfile(supervisor.__file__, self.runner)
        (scripts / "validate_observable_solver.py").write_text(FAKE_WORKER)
        (scripts.parent / "portable_marker.py").write_text("VALUE = 'from code root'\n")
        self.plan = self.root / "plan.json"
        self.output = self.root / "output"

    def write_plan(self, configurations, **changes):
        budget = dict(maximum_configurations=12, cpu_seconds_per_configuration=4,
                      wall_seconds_per_configuration=5, total_cpu_seconds=20,
                      rss_bytes_per_process=128*1024*1024,
                      threads_per_process=1, parallel_trajectory_processes=1)
        budget.update(changes)
        self.plan.write_text(json.dumps(dict(version="fake-worker-only", budget=budget,
                                            configurations=configurations)))

    def command(self):
        return [sys.executable, "-B", str(self.runner), "--plan", str(self.plan),
                "--output-dir", str(self.output)]

    def execute(self):
        environment = dict(os.environ, OPENBLAS_NUM_THREADS="8", PYTHONPATH="")
        completed = subprocess.run(self.command(), cwd=self.root, env=environment,
                                   capture_output=True, text=True, timeout=10)
        record = json.loads((self.output / "supervisor.json").read_text())
        return completed, record

    def test_help_and_plan_validation_before_output(self):
        helped = subprocess.run([sys.executable, "-B", str(self.runner), "--help"],
                                capture_output=True, text=True, timeout=5)
        self.assertEqual(helped.returncode, 0)
        self.assertIn("--output-dir", helped.stdout)
        for configurations, changes in (
            ([dict(id="../bad")], {}),
            ([dict(id="same"), dict(id="same")], {}),
            ([dict(id="ok")], dict(maximum_configurations=0)),
            ([dict(id="ok")], dict(threads_per_process=2)),
            ([dict(id="ok")], dict(total_cpu_seconds=float("nan"))),
        ):
            with self.subTest(configurations=configurations, changes=changes):
                self.write_plan(configurations, **changes)
                completed = subprocess.run(self.command(), capture_output=True, timeout=5)
                self.assertNotEqual(completed.returncode, 0)
                self.assertFalse(self.output.exists())

    def test_serial_protocol_environment_and_bounded_log(self):
        self.write_plan([dict(id="first", mode="noisy"), dict(id="second")])
        completed, record = self.execute()
        self.assertEqual(completed.returncode, 0, completed.stderr)
        self.assertEqual(record["status"], "operational_pass")
        self.assertEqual([r["id"] for r in record["configurations"]], ["first", "second"])
        self.assertEqual(len(completed.stdout.splitlines()), 2)
        self.assertNotIn("worker-noise", completed.stdout)
        first = record["configurations"][0]
        self.assertTrue(first["log_truncated"])
        self.assertEqual((self.output / "first.log").stat().st_size, supervisor.MAX_LOG_BYTES)
        self.assertGreater(first["reaped_cpu_seconds"], 0)
        self.assertGreaterEqual(first["cpu_seconds"], first["reaped_cpu_seconds"])
        for entry in record["configurations"]:
            worker = json.loads((self.output / entry["id"] / "record.json").read_text())
            self.assertEqual(worker["marker"], "from code root")
            self.assertEqual(set(worker["thread_environment"].values()), {"1"})
            self.assertEqual(Path(entry["command"][2]).name, "validate_observable_solver.py")
            self.assertNotIn("candidate_loader", " ".join(entry["command"]))
        # The runner rejects reuse before modifying earlier evidence.
        original = (self.output / "supervisor.json").read_bytes()
        repeated = subprocess.run(self.command(), capture_output=True, timeout=5)
        self.assertNotEqual(repeated.returncode, 0)
        self.assertEqual((self.output / "supervisor.json").read_bytes(), original)

    def test_missing_malformed_oversized_and_mismatched_records_continue(self):
        self.write_plan([dict(id=mode, mode=mode) for mode in
                         ("missing", "malformed", "oversized", "wrong_id")] + [dict(id="last")])
        completed, record = self.execute()
        self.assertEqual(completed.returncode, 1)
        self.assertEqual([r["status"] for r in record["configurations"]],
                         ["failure"]*4 + ["operational_pass"])
        self.assertTrue(all(r["worker_status"] == "invalid_or_missing_record"
                            for r in record["configurations"][:4]))
        self.assertLess((self.output / "supervisor.json").stat().st_size, 20000)

    def test_wall_cap_stops_only_that_configuration(self):
        self.write_plan([dict(id="sleep", mode="sleep"), dict(id="after")],
                        wall_seconds_per_configuration=0.3)
        completed, record = self.execute()
        self.assertEqual(completed.returncode, 1)
        first, second = record["configurations"]
        self.assertEqual(first["stopped"], "wall_budget")
        self.assertEqual(first["exit_code"], -signal.SIGKILL)
        self.assertEqual(second["status"], "operational_pass")
        self.assertLess(first["wall_seconds"], 2)

    def test_per_configuration_cpu_cap(self):
        self.write_plan([dict(id="busy", mode="cpu")], cpu_seconds_per_configuration=1)
        completed, record = self.execute()
        self.assertEqual(completed.returncode, 1)
        first = record["configurations"][0]
        self.assertEqual(first["stopped"], "cpu_budget")
        self.assertGreaterEqual(first["cpu_seconds"], 1)
        self.assertLess(first["cpu_seconds"], 2)

    def test_total_cpu_cap_records_unstarted_configurations(self):
        self.write_plan([dict(id="busy", mode="cpu"), dict(id="unstarted")],
                        total_cpu_seconds=0.1)
        completed, record = self.execute()
        self.assertEqual(completed.returncode, 1)
        first, second = record["configurations"]
        self.assertEqual(first["stopped"], "total_cpu_budget")
        self.assertEqual(second["status"], "not_run_total_budget")
        self.assertFalse((self.output / "unstarted").exists())
        self.assertFalse((self.output / "unstarted.log").exists())
        self.assertGreaterEqual(record["total_cpu_seconds"], 0.1)

    def test_rss_cap(self):
        self.write_plan([dict(id="resident", mode="sleep")], rss_bytes_per_process=1024)
        completed, record = self.execute()
        self.assertEqual(completed.returncode, 1)
        first = record["configurations"][0]
        self.assertEqual(first["stopped"], "rss_budget")
        self.assertGreater(first["sampled_peak_rss"], 1024)

    def test_sigterm_reaps_worker_and_records_remaining_ids(self):
        self.write_plan([dict(id="sleep", mode="sleep"), dict(id="unstarted")])
        process = subprocess.Popen(self.command(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        try:
            record_path = self.output / "sleep" / "record.json"
            until = time.monotonic() + 5
            while not record_path.exists() and time.monotonic() < until:
                time.sleep(0.02)
            self.assertTrue(record_path.exists())
            # Wait for the fake worker's single small write to finish.
            time.sleep(0.03)
            pid = json.loads(record_path.read_text())["pid"]
            process.send_signal(signal.SIGTERM)
            stdout, stderr = process.communicate(timeout=5)
            self.assertEqual(process.returncode, 130, stderr)
            record = json.loads((self.output / "supervisor.json").read_text())
            self.assertEqual(record["status"], "interrupted")
            self.assertEqual(record["configurations"][0]["stopped"], "supervisor_interrupted")
            self.assertEqual(record["configurations"][1]["status"], "not_run_interrupted")
            with self.assertRaises(ProcessLookupError):
                os.kill(pid, 0)
        finally:
            if process.poll() is None:
                process.kill()
                process.communicate()


if __name__ == "__main__":
    unittest.main()
