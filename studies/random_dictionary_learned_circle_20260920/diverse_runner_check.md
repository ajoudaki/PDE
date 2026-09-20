# Internal adaptive-runner check

2026-09-20. Scoped implementation audit, not an independent promotion review.
No other study was an input. No benchmark training was performed.

The corrected runner passes the bounded update and bookkeeping checks below.
This permits the planned experiment to proceed; it does not establish endpoint
accuracy, successful fitting, or a ranking between dictionaries. Those require
the preregistered run and its refinement checks.

## Inputs and scope

Read the complete study `benchmark.py`, `diverse_benchmark.py`,
`diverse_dictionary.py`, and maintained `code/pde/finite_torch.py` and
`code/pde/observable_torch_p1.py`. The earlier case-design task read this study's
README, `docs/NOTATION.md`, and the investigate-conjectures skill and experiment
design reference. The dictionary's word construction is outside this runner
audit's validation claim; its interface was inspected for initialization and
comparison fairness.

## Defects found and corrected by the lead task

1. The original summary constructor contained the invalid keyword expression
   `loss_increases_above_1e-10=...`, which prevented Python from importing the
   runner. It now adds that literal dictionary key after construction. The
   corrected file imported and completed all checks.
2. A state already satisfying the threshold originally retained `time_cap`
   without entering the loop. The runner now initializes its status to
   `fitted` in that case. The zero-step case is explicitly checked.

No unresolved update-formula or saved-state chronology defect was identified
within the checked scope.

## Executed checks

The exact successful command, from `/home/amir/Codes/PDE`, was:

```sh
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 /home/amir/miniconda3/bin/python -B studies/random_dictionary_learned_circle_20260920/validate_diverse_runner.py --device cuda:0 --out data/generated/random_dictionary_learned_circle_20260920/diverse_runner_validation01/checks.json
```

The real neural checks use GPU 0, float64, width 8, a deterministic noninitial
state with all three blocks nontrivial, and step sizes 0.001, 0.05, and 0.2.
They compare `heun_trial` with each maintained engine's own `heun_step` and
check that the input state is unchanged. Maximum state discrepancy is **0**.
A complete orthonormal basis additionally identifies the closure with the
uncompressed network; the maximum discrepancy after one step is
**1.1102230246251565e-16**. Every recorded embedded-error ratio is finite and
nonnegative. These are tiny algebraic update checks, not training trajectories.

A CPU synthetic flow `c'=1` with the monotone event function `exp(-8c)` checks
the trajectory wrapper. It does not simulate a neural network. The six cases
are threshold fitting, physical-time cap, accepted-step cap, expired worker
cap, deliberate RHS failure, and an initially fitted state. All pass. The fit
time is 0.8634694099426268, within 1e-9 of `log(1000)/8`, with final event value
0.000999999999441122. Checks reconstruct every saved synthetic prediction,
state, and event value; confirm strictly increasing timestamps and snapshots;
match accepted step lengths to time differences; verify the final snapshot
equals the reported endpoint; and confirm zero-step failures retain their
initial checkpoint. Temporary probe arrays were created and removed inside
the study-owned `diverse_runner_validation01` directory.

The JSON above contains all values and tested source hashes. The tested runner
SHA256 is
`9556b9baaa89643a6dc474873b6536f6dda7a4e3cad0bd3fbba9fee2a9a3b43e`.
The test script SHA256 is
`4b5c091eb0e5407f423cf69a73376a2cf7c857a221b46f302540b111440b5c20`.

Execution notes: the initial invocation found the syntax defect before any
checks ran. A later default-sandbox GPU invocation found CUDA unavailable and
performed no neural computation. The authorized bounded retry used elevated
execution to access GPU 0. An initial synthetic probe used `(c-1)^2` with
`c'=1`; that unsuitable probe can enter and leave the threshold region within
one accepted step, so it was replaced with the monotone event function above.
The failed probe was not counted as validation evidence. Both small GPU runs
together remained below the assigned 30-second allowance.

## Numerical and scope limits

At each fixed accepted step, the update is the maintained simultaneous Heun
formula. The controller estimates its difference from the Euler stage; this is
an embedded numerical indicator, not an exact-flow error bound. The middle
block's norm is scaled by its trained increment, with a floor of one, rather
than by the initial Gaussian bulk. Its value depends on the representation,
so equal controller tolerances across full and reduced states do not imply
equal function error. Independent tolerance refinement remains necessary.

The final threshold state is found by bisection along the **linear chord**
between an accepted step's endpoints. This is not the quadratic continuous
extension of Heun. The runner detects the first accepted endpoint below the
threshold and refines that bracket; it does not certify the earliest crossing
of the true flow or detect a transient crossing whose two endpoints are both
above threshold. Report that numerical endpoint rule literally.

Time and step caps are checked before integration trials. Setup, already
running operations, circle evaluation, and checkpoint writing can finish
after the deadline. The worker deliberately creates explicit initialized
wall-cap records for remaining cells. Thus these limits stop integration;
they are not hard end-to-end wall-clock limits. Likewise,
`peak_cuda_allocated` is the process peak since the CUDA allocator was last
reset, not isolated per-cell peak memory.

The methods within each case share the actual initialized first weights and
readout. Every trajectory clones its own initial state; all three blocks use
the maintained dynamics. Frozen dictionaries and random draws are independent
of the case labels and trajectories. Gaussian and orthogonal controls share
their underlying sampled spans, while their frame conditioning differs.
These facts support the intended finite-carrier comparison. Worker deadlines
can truncate later cells by execution order, and different devices can differ
in throughput; preserve all capped cells and avoid interpreting these timing
records as a controlled speed comparison. A comparison lacking fitted and
numerically validated endpoints remains inconclusive.
