"""Run only the explicitly inspected migration suites, with private writes."""
import importlib.util
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import unittest

ROOT = Path("/home/amir/Codes/PDE")
PRIVATE = Path(__file__).parent
SUITES = [
  "studies/resnet_generalization/tests/test_migration_paths.py",
  "studies/resnet_generalization/tests/test_output_boundaries.py",
  "studies/resnet_generalization/tests/test_writer_boundaries.py",
  "studies/resnet_proof_audit/tests/test_trapezoid_compat.py",
  "studies/stieltjes_finite_width/test_migration_paths.py",
  "studies/stieltjes_finite_width/test_output_boundaries.py",
  "studies/stieltjes_finite_width/test_shared_output_paths.py",
  "studies/stieltjes_hybrid_campaign/breadth_panel/test_migration_paths.py",
  "studies/stieltjes_hybrid_campaign/breadth_panel/test_output_boundaries.py",
  "studies/stieltjes_hybrid_campaign/width_ladder/euler_fp32/test_output_boundaries.py",
  "studies/stieltjes_proxy_campaign/analysis/tests/test_output_boundaries.py",
  "studies/resnet_generalization/tests/test_raw_output_preflight.py",
  "studies/resnet_activation_controls/tests/test_migration_boundaries.py",
  "studies/resnet_proof_audit/tests/test_migration_boundaries.py",
  "studies/stieltjes_finite_width/test_migration_preflight.py",
  "studies/stieltjes_direct_loewner/test_writer_boundaries.py",
  "studies/stieltjes_hybrid_campaign/breadth_panel/test_acceptance_boundaries.py",
  "studies/stieltjes_hybrid_campaign/width_ladder/test_analysis_boundaries.py",
  "studies/stieltjes_proxy_campaign/analysis/tests/test_reference_migration_boundaries.py"
]
if len(sys.argv) > 1:
    spec = importlib.util.spec_from_file_location("isolated_boundary_suite", ROOT / sys.argv[1])
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    result = unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromModule(module))
    raise SystemExit(not result.wasSuccessful())

environment = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", PYTHONPATH=str(ROOT),
                   TMPDIR=str(PRIVATE), MPLCONFIGDIR=str(PRIVATE / "mpl"), XDG_CACHE_HOME=str(PRIVATE / "cache"),
                   OPENBLAS_NUM_THREADS="1", OMP_NUM_THREADS="1", MKL_NUM_THREADS="1",
                   PYTEST_DISABLE_PLUGIN_AUTOLOAD="1")
records, fixtures = [], []
for index, suite in enumerate(SUITES):
    result = subprocess.run([sys.executable, "-B", str(Path(__file__)), suite], cwd=PRIVATE,
                            env=environment, capture_output=True, text=True, timeout=45)
    output = result.stdout + result.stderr
    log = f"suite-{index:02d}.log"
    (PRIVATE / log).write_text(output)
    count = re.search(r"Ran (\d+) tests?", result.stderr)
    records.append(dict(suite=suite, tests=int(count[1]) if count else 0, exit_code=result.returncode, log=log))
    for line in result.stdout.splitlines():
        if line.startswith("FIXTURE_SHA256 "):
            fixtures.append(dict(suite=suite, **json.loads(line.removeprefix("FIXTURE_SHA256 "))))
    print(suite, "exit=" + str(result.returncode), flush=True)
    print("\n".join(result.stderr.strip().splitlines()[-5:]), flush=True)
(PRIVATE / "test-results.json").write_text(json.dumps(records, indent=2) + "\n")
(PRIVATE / "fixture-hashes.json").write_text(json.dumps(fixtures, indent=2) + "\n")
raise SystemExit(any(item["exit_code"] for item in records))
