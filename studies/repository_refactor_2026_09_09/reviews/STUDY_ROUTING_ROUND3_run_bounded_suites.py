import importlib.util
import os
from pathlib import Path
import subprocess
import sys
import unittest

ROOT = Path('/home/amir/Codes/PDE')
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
  "studies/stieltjes_proxy_campaign/analysis/tests/test_output_boundaries.py"
]
if len(sys.argv) > 1:
    spec = importlib.util.spec_from_file_location('isolated_boundary_suite', ROOT/sys.argv[1])
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    result = unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromModule(module))
    raise SystemExit(not result.wasSuccessful())
environment = dict(os.environ, PYTHONDONTWRITEBYTECODE='1', PYTHONPATH=str(ROOT),
                   TMPDIR=str(PRIVATE), MPLCONFIGDIR=str(PRIVATE/'mpl'), XDG_CACHE_HOME=str(PRIVATE/'cache'),
                   OPENBLAS_NUM_THREADS='1', OMP_NUM_THREADS='1', MKL_NUM_THREADS='1',
                   PYTEST_DISABLE_PLUGIN_AUTOLOAD='1')
failed = 0
for index, suite in enumerate(SUITES):
    result = subprocess.run([sys.executable, '-B', str(Path(__file__)), suite], cwd=PRIVATE,
                            env=environment, capture_output=True, text=True, timeout=45)
    (PRIVATE/f'suite-{index:02d}.log').write_text(result.stdout+result.stderr)
    print(suite, 'exit='+str(result.returncode), flush=True)
    print('\n'.join(result.stderr.strip().splitlines()[-4:]), flush=True)
    failed += bool(result.returncode)
raise SystemExit(bool(failed))
