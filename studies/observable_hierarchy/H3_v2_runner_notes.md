# Portable validation supervisor

The frozen candidate `H3_v2_supervise.py` installs unchanged as
`code/scripts/run_observable_validation.py`. It directly executes its sibling
`validate_observable_solver.py`, prepends their code root to `PYTHONPATH`,
and keeps the worker's existing `--plan`, `--id`, `--output` interface and
`record.json`, restart JSON and observation NPZ protocol. No candidate loader,
study path or repository-specific absolute path appears in the source.

From a checkout containing the assembled canonical files:

```text
python -B code/scripts/run_observable_validation.py --help
python -B code/scripts/run_observable_validation.py --plan code/validation/observable_solver_plan.json --output-dir data/established/observable_solver_check
```

The output directory must be fresh. The runner requires Linux and psutil;
the numerical worker also requires NumPy and the canonical `pde` modules.
It executes only the listed configurations, serially, with one BLAS/OpenMP
thread. It reads every CPU, wall, RSS and total-worker-CPU allowance from
the supplied plan. Thus the revised twelve-configuration plan's 3600-second
total budget needs no source change; the original plan's 7200-second budget
is not embedded in the runner.

Each completed or stopped configuration adds a supervisor record and one
compact parent-output line. Individual failures permit later listed
configurations; an exhausted total CPU budget records the remaining IDs as
`not_run_total_budget`. SIGINT/SIGTERM terminates and reaps the current worker
session, records interruption and lists the unstarted IDs. Existing worker
evidence is preserved. `supervisor.json` is checkpointed by atomic replacement;
its accumulated configuration entries are retained. Exit status is 0 only
when every configuration operationally passes, 1 for failure/skipped budget
work, and 130 for interruption. Invalid setup exits nonzero before launching.

The worker retains its OS CPU limit. The runner checks CPU, wall time and RSS
at most every 0.05 seconds of ordinary monitoring, including interpreter
startup; OS scheduling can delay a check, so these sampled stops can overshoot
their boundaries. Recorded worker peak RSS and CPU are checked after exit as
well. Charged CPU is the maximum of sampled CPU, worker-reported CPU and the
increment of reaped-child OS CPU, which includes short-lived startup/failure
work. Parent CPU is reported separately. The existing numerical worker starts
no subprocesses; this is a single-worker resource contract, not a general
container or an instantaneous RSS bound.

Each combined stdout/stderr log retains at most 256 KiB. Excess worker output
is drained without copying it into parent output, and truncation is recorded.
The monitor performs one bounded pipe read between resource checks. Plan and
worker-record reads are capped at 1 MiB and 4 MiB, respectively. Parent memory
and metadata storage are bounded by those allowances and the declared finite
configuration count; at most two supervisor JSON copies coexist during an
atomic update. Scientific worker artifacts retain their original format and
are outside the parent-log cap. The runner does not claim a filesystem quota.

## Static and fake-worker validation

`H3_v2_supervise_tests.py` installs unchanged as
`code/tests/test_observable_validation.py`. Its canonical import is
`from scripts import run_observable_validation`; `PYTHONPATH=code` makes the
scripts directory available as a namespace package. Tests copy the imported
source into a temporary code/scripts layout with a fake worker, so the tests
perform no solver initialization, evolution or scientific reproduction.

```text
PYTHONPATH=code OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python -B -m unittest discover -s code/tests -p 'test_observable_validation.py' -v
```

The deterministic test allowance remains at most 600 CPU seconds and 4 GiB;
these tests belong within that allowance, not an additional trajectory budget.
The eight tests cover portable direct execution, thread settings, the worker
record protocol, bounded noisy logs, unique safe IDs and plan limits, fresh
output rejection, missing/malformed/oversized/mismatched records, continuation
after individual failure, CPU/wall/RSS/total CPU stops, and SIGTERM cleanup.

Author static validation parsed both complete source files and ran all eight
tests on 2026-09-13. Result: **8 passed**, 3.083 wall seconds; test-parent CPU
0.099674 seconds, reaped-child CPU 2.752475 seconds, parent peak RSS
22,978,560 bytes and maximum child peak RSS 30,261,248 bytes. The test driver
set a 600-second CPU limit. No real trajectory or initialization was run.
The full test source is the accompanying test file; test products used
temporary directories and were cleaned up.

Frozen source SHA-256 values:

```text
3ac1b85367416d0b744daf56233ae8d9f97123971cd5cc0c46ee8b1694fcde73  H3_v2_supervise.py
e1ee08c217ce6f39e64801f1c2b64f71482fe6efe5ee8924fe36c6bacc0201c1  H3_v2_supervise_tests.py
```

This is author operational evidence for the supervisor. It supplies no
numerical accuracy certificate or independent scientific reproduction.
