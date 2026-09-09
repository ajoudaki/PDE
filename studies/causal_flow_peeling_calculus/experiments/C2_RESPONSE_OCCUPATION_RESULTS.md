# C2 response-weighted occupation audit

## Outcome

The square-exponential premise cannot support the intended uniform or
annealed theorem route: before execution, an analytic correction showed that
already at finite width and `t=0`,

\[
r_{2,i}\mid(u,G_1,G_2)\sim N(0,S_i),\qquad
S_i=\sum_m G_{2,mi}^2\phi'(z_{3,m})^2,
\]

and `S_i` has unbounded support.  Conditional Gaussian integration gives
`E[exp(lambda r2_i^2) | u,G1,G2] = infinity` whenever
`2 lambda S_i >= 1`; that event has positive probability for every positive
`lambda`.  Hence
`E exp(lambda r2_i^2) = infinity` for every `lambda>0`.  In particular, a
finite square-exponential sample cannot establish the uniform integrability
needed by a factorization argument.  This exact analytic obstruction is
logically prior to the numerical result.

The locked numerical grid was nevertheless preserved rather than changed
post hoc.  Its preregistered **finite typical-sample label is inconclusive**.
Every numerical-validity gate passed and no fail condition fired, but the
familywise upper confidence bound for the width exponent exceeded the pass
threshold in all 18 primary cells.  Thus the run neither passes nor fails its
locked finite-grid discriminator.

Descriptively, the tested samples show no increasing sensitivity alignment
with rare large `|r2|`: every alignment slope was negative, true-versus-
shuffled contrasts at width 1024 were between `-0.0325` and `0.00358`, and
the locked median ESS/max-contribution gates passed comfortably.  These are
finite-sample facts only and do not counter the analytic infinite-moment
obstruction.

## Locked design executed

- Exact `D=3`, `phi=atan` flow and exact transpose reuse from the C2
  preregistration.
- Widths `128,256,512,1024`, times `0,0.25,0.5`, and 48 independent
  model/direction replicates at every width.
- Marked column `j=0` with
  `Delta G2[:,0]=h/||h||_2`; all other initial tangent components zero.
- Full tangent-linear primal/JVP RK4 trajectory, not a frozen or endpoint
  derivative.
- Primary bulk fields `V=D r2[Delta]` and `V=D b2[Delta]`, excluding the
  marked coordinate.
- Literal unnormalized
  `M(lambda)=sum_bulk exp(lambda r2^2)|V|^2` at
  `lambda=0,0.05,0.10,0.20`.
- Thirty-two retained weight permutations per instance and a rank-aligned
  positive control.
- Float32 CUDA RK4 at `dt=1/64`; eight-seed `dt=1/128` mesh and float64
  controls at widths 256 and 1024; four-seed full-trajectory central
  differences at width 128.

The post-lock analytic caveat did not alter any grid point, threshold, seed,
or calculation.

## Primary estimates

The following table shows the most stressful locked weight `lambda=0.20`.
`beta` is the point width exponent of the arithmetic mean of `M`, `FW U` is
its familywise 95% upper bound, `a1024` is the pooled log true/shuffled
contrast, and the final two columns are the width-1024 medians.

| field | time | beta | beta FW U | a1024 (familywise interval) | rESS | max share |
|---|---:|---:|---:|---:|---:|---:|
| `D r2` | 0 | 0.197 | 0.416 | 0.00026 `[-0.00615,0.00722]` | 0.311 | 0.0148 |
| `D r2` | 0.25 | 0.0810 | 0.300 | -0.000745 `[-0.00715,0.00622]` | 0.315 | 0.0138 |
| `D r2` | 0.5 | 0.0256 | 0.244 | 0.000605 `[-0.00580,0.00757]` | 0.320 | 0.0130 |
| `D b2` | 0 | 0.192 | 0.411 | 0.00358 `[-0.00283,0.0105]` | 0.255 | 0.0191 |
| `D b2` | 0.25 | 0.0481 | 0.267 | -0.0156 `[-0.0220,-0.00864]` | 0.258 | 0.0168 |
| `D b2` | 0.5 | 0.00124 | 0.220 | -0.0325 `[-0.0389,-0.0255]` | 0.257 | 0.0170 |

Across all 18 primary cells:

- point `beta` ranged from `0.00124` to `0.224`, while the familywise upper
  bound ranged from `0.220` to `0.443`; every cell therefore missed the
  all-cells pass requirement `FW U <= 0.20`;
- every alignment slope `alpha` was negative, ranging from `-0.0199` to
  `-0.000508`, with every familywise upper bound below the locked `0.10`
  threshold;
- `a1024` ranged from `-0.0325` to `0.00358`, with every familywise upper
  bound below `0.15`;
- the largest cellwise 95% lower bound for `beta` was only `0.0415`, far
  below the replicated fail threshold `0.30`; no adjacent-lambda or
  confirmation-half failure occurred.

For scale, the arithmetic mean `M(0.20)` values by width were:

| field | time | n=128 | n=256 | n=512 | n=1024 |
|---|---:|---:|---:|---:|---:|
| `D r2` | 0 | 0.0595 | 0.0501 | 0.0601 | 0.0882 |
| `D r2` | 0.25 | 0.0759 | 0.0633 | 0.0756 | 0.0863 |
| `D r2` | 0.5 | 0.1009 | 0.0895 | 0.0967 | 0.1043 |
| `D b2` | 0 | 0.0385 | 0.0322 | 0.0387 | 0.0565 |
| `D b2` | 0.25 | 0.0488 | 0.0389 | 0.0461 | 0.0515 |
| `D b2` | 0.5 | 0.0567 | 0.0491 | 0.0517 | 0.0559 |

The nonmonotone width pattern and fixed 48-seed uncertainty explain why the
simultaneous pass bound remained too wide.  The result was not enlarged with
additional seeds after inspection.

## Shuffle, factorization, and rare-contribution diagnostics

Fifteen of 18 primary cells met the locked factorization-compatibility band.
The three resolved exceptions all had **negative** alignment:
`D b2` at `(t,lambda)=(0.25,0.20),(0.5,0.10),(0.5,0.20)`.  There was no
resolved positive alignment cell.  Forced rank alignment raised the median
moment relative to shuffling by factors from `1.061` to `1.449`, confirming
that the comparison could detect a constructed alignment.

At width 1024 and `lambda=0.20`, across the six field/time cells:

- median relative ESS ranged from `0.255` to `0.320` (locked minimum `0.05`);
- median maximum contribution share ranged from `0.0130` to `0.0191`
  (locked maximum `0.10`);
- median weight-only relative ESS ranged from `0.924` to `0.945`, and median
  maximum weight share from `0.00360` to `0.00443`;
- median unweighted response energy in the top 1% by `|r2|` ranged from
  `0.00468` to `0.0109`; the corresponding weighted-contribution share
  ranged from `0.0117` to `0.0338`.

One width-1024 instance (`replicate=2`, `D b2`, `t=0.25`, `lambda=0.20`)
had maximum contribution share `0.118` and relative ESS `0.0538`; this is
retained, not excluded.  It did not trigger the preregistered median and
replication failure rule.  The largest `|r2|` observed anywhere in the locked
primary grid was `4.333` (largest sampled weight about `42.7`).  These finite
maxima illustrate why the grid cannot diagnose the analytically known tail
beyond its realized sample.

## Numerical validity

All 48 trajectories at every width were finite and valid.  The largest
absolute primal/tangent/derived entry was `4.976`, and the exact time-zero
`D z2=D x2=0` checks held bit-for-bit.

| control | observed maximum | locked gate |
|---|---:|---:|
| mesh JVP relative L2 | `5.10e-6` | `5e-4` |
| mesh moment relative difference | `2.05e-6` | `5e-3` |
| float32/float64 JVP relative L2 | `1.17e-5` | `1e-3` |
| float32/float64 moment relative difference | `2.35e-5` | `1e-2` |
| fine central-difference JVP relative L2 | `9.61e-7` | `2e-4` |
| fine/coarse central-difference absolute-error ratio | `0.062501` | `1.2` |

The central-difference ratio is approximately `1/16`, consistent with the
fourfold reduction expected when a second-order central difference decreases
its perturbation by a factor of four.

## Claim ledger

1. **Exact analytic result:** the positive square-exponential weight lacks a
   finite annealed moment for every positive lambda.  Any theorem route that
   requires that moment is falsified.
2. **Locked finite-grid classification:** inconclusive; all numerical gates
   passed, but simultaneous width bounds did not meet the stringent pass
   band, and no fail pattern occurred.
3. **Descriptive mechanism evidence:** the sampled response did not align
   increasingly with large `|r2|`; if anything, three `D b2` cells showed
   small negative alignment.  This is not tail-uniform evidence.
4. **Unresolved alternative:** exponential-linear weights would avoid this
   particular Gaussian square-MGF obstruction, but they were not part of C2
   and were not run post hoc.

## Reproducibility and artifacts

Production and every control used
`/home/amir/miniconda3/envs/textgen/bin/python`, PyTorch `2.5.1+cu121`, CUDA
12.1, deterministic algorithms, disabled TF32, and two RTX 3090 GPUs.  All
production/control runs used source SHA-256
`f7ae950a1f2eb4d50e48da1c80acee4a7bde81d161851ebd6ad4d35286bd5ed8`.
The per-run metadata retain exact commands, seeds, environment, source and
preregistration hashes.

- Preregistration: `PREREGISTRATION.md`, `C2_PREREGISTRATION_LOCK.md`
- Production: `c2_response_occupation.py`
- Analysis: `analyze_c2_response_occupation.py`
- Main raw data: `outputs/c2_response_occupation_main_low/`,
  `outputs/c2_response_occupation_main_1024_a/`,
  `outputs/c2_response_occupation_main_1024_b/`
- Controls: `outputs/c2_response_occupation_controls/`,
  `outputs/c2_response_occupation_fd/`
- Derived results: `outputs/c2_response_occupation_summary/summary.json`,
  `cell_summary.csv`, `tail_summary.csv`, `secondary_summary.csv`, and
  `fd_gate_details.csv`

The raw archive contains 9,216 per-instance metric rows, 294,912 individual
shuffle rows, 2,304 retained response-vector records, 768 mesh/precision
rows, and 96 central-difference rows.  No trajectory or adverse diagnostic
was dropped.
