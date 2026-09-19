# C-X1 validation record

These checks accompany the proof; none replaces its continuation or closure
convergence arguments. Generated evidence is under the study's separate
`data/generated/cx1_many_point_closure_20260919/` namespace.

The corrected implementation adds an iterative dimension-independent exponent
enumerator. All seven semantic tests passed in 14.753 seconds in
`closure/deterministic_v3/`, including a d=600/order=1 regression. A subsequent
test-docstring cleanup changed the test source hash but no executable test;
the final-source run is separately retained as `closure/deterministic_v4/`.
All seven tests passed there in 14.705 seconds with matching final source
hashes, zero errors and zero failures under the 120-second/512-MiB cap.
The first v3 launch failed before importing the test module because its runpy
wrapper omitted the study from PYTHONPATH; the corrected command included it.
This was a launch error, not a scientific or implementation test failure.

The corrected module also repeated exactly the five operational configurations
in `operational_02/`. They passed in 15.477 seconds, with every recorded loss,
paired RMS and passive prediction bitwise equal to the original values below.
Only timings and measured resource peaks differ. These reruns validate the
corrected executable; they do not strengthen the numerical-accuracy claim.

## Deterministic semantics

`test_cx1_closure.py` checks six obligations: genuine dictionary enrichment
and dimensions; agreement with the maintained joint Gaussian compiler in d=2;
both reused-action responses with the seventh Gaussian coordinate; adjunction
and independent finite-difference gradients in all three moving blocks;
same-population observations and exact restart; rational arithmetic and
resource/domain failures. All six passed in 14.87 seconds, recorded in
`closure/deterministic_v2/results.json`. Source hashes are recorded there.

The independent exact rational initialization certificate also passed; see
`reference_constants_01/record.json` and `check_reference_constants.py`.

A separate fresh-working-directory check imported the solver, initialized
d=3/order=1, and evaluated its initial zero prediction. It passed using only
this study's module and maintained `code/`, without a historical array or
trained trajectory. `standalone_01/record.json` preserves the exact command;
its stdout hashes every loaded project module. `DEPENDENCY_HASHES.json`
records the maintained proof and implementation dependencies separately.

## Bounded operational run

The five configurations in `VALIDATION_PLAN.md` were fixed before execution.
All completed in about 16 seconds aggregate with peak resident memory below
42 MiB and bitwise exact midpoint restart. The evolving state retained its
initial dimensions in every run. Full records, checkpoints and observations:
`operational_01/record.json` and the files hashed there. No full neural training
was run. The standard reproduction command is in the plan.

| Configuration | Final closure loss | First-layer paired RMS | Second-layer paired RMS | Retained array bytes |
| --- | ---: | ---: | ---: | ---: |
| Reference, order 1 | 1.95e-6 | 0.302 | 0.365 | 11,904 |
| Reference, order 3 | 1.57e-6 | 0.277 | 0.472 | 87,440 |
| Reference, order 3, twice the time steps | 1.57e-6 | 0.277 | 0.472 | 87,440 |
| Reference, order 3, twice Q and P | 2.42e-8 | 0.317 | 0.501 | 146,320 |
| Nonorthogonal operational example, order 3 | 7.05e-7 | 0.279 | 0.485 | 87,440 |

These are finite closure outputs. The maximum change on the eight recorded
passive probes was about 1.82e-7 upon time refinement but 0.061 upon doubling
integration and population nodes. In particular, small training loss and
small time-discretization change do NOT certify population-prediction accuracy.
Two closure orders and this small refinement check do not estimate an order
rate. The nonorthogonal example is not asserted to lie in the theorem's
unevaluated radius. Its role is only to check operation of the same algorithm
away from exact orthogonality.

No rerun search, parameter fitting, favorable-seed selection or broad sweep
was used. The initializer is deterministic. Mathematical qualitative limits
retain the separate order and numerical resolutions specified in the proof.
