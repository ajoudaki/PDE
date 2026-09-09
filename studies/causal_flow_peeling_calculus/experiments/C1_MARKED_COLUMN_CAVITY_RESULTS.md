# C1: Marked-Column Cavity and Tangent Scaling

## Claim level

This probe **passes its preregistered empirical-compatibility gate**.  On the
tested pure-arctangent depth-three flows, replacing one standardized column
of the persistent top source leaves an order-one effect in the directly
marked transpose coordinate, while its effects on all preregistered bulk
fields decay at rates compatible with `n^{-1/2}` through feature time `0.5`.
Full-trajectory forward-mode JVPs show the same scaling.

This is empirical evidence for a marked-column/leave-one-column proof
strategy.  It is not a cavity theorem, a width limit, a response-forest tail
bound, or evidence that width and response depth can be interchanged.

## Frozen experiment

- exact one-sample, three-hidden-layer flow `(F)` with `phi=arctan`;
- persistent tied matrices `Gamma_1,Gamma_2` with entries `N(0,1/n)`;
- column zero of `Gamma_2` replaced by an independent column in the coupled
  trajectory, with every other seed shared;
- widths `128,256,512,1024`, four trials per width, and times
  `0,0.25,0.5`;
- primary float32 CUDA RK4 mesh `2^-10`;
- two independent Rademacher JVP directions per trial, differentiated with
  `torch.func.jvp` through the complete RK4 trajectory with respect to the
  standardized column `g[:,0]=sqrt(n) Gamma_2[:,0]`;
- doubled-resolution float32 controls at widths `128,512,1024`, trials
  zero and one;
- float64 meshes `2^-10` and `2^-11` at widths `128,512`, trial zero.

The preregistration was appended before the implementation was executed.
The source script hash recorded by every run is
`7f404eeab9e1065533b908f0d83c491e445e2803c2a911e409b7f8ae778d4a0a`.
The machine-readable summary records analyzer hash
`4a12071a66b30b139d468238717d78806b602036e6c18a58563077c4409dedeb`.

## Primary width scaling

The table reports slopes from a log--log regression of across-trial RMS on
width.  A slope of zero is the marked-coordinate prediction and a slope of
`-1/2` is the bulk prediction.

| metric | `t=0.25` | `t=0.5` |
|---|---:|---:|
| replaced-column `|Delta r_2[0]|` | `-0.073` | `-0.073` |
| `||Delta x_2||_n` | `-0.447` | `-0.444` |
| `||Delta z_3||_n` | `-0.598` | `-0.581` |
| `||Delta b_3||_n` | `-0.567` | `-0.573` |
| `||Delta u||_n` | `-0.464` | `-0.443` |
| learned `G_1` operator estimate | `-0.497` | `-0.478` |
| learned `G_2` operator estimate | `-0.592` | `-0.566` |

The marked-response RMS changes from `1.051` at width `128` to `0.884` at
width `1024` at time `0.25`, and from `0.964` to `0.808` at time `0.5`.
Thus the test sees no width amplification of the coordinate that receives
the direct transpose reuse.

The full `G_2` operator perturbation remains order one, with width slope
`0.007`, exactly as it must: it contains the deliberately replaced source
column.  Its normalized Frobenius norm has slope `-0.493`.  After subtracting
the source separately in each trajectory, the learned-displacement operator
differences have the negative half-power slopes displayed above.  Operator
values are deterministic 30-step power-iteration estimates, not certified
upper bounds; they are secondary metrics and were not used to rescue any
field-level decision.

## Independent tangent check

For a Rademacher direction `v`, the scalar directional derivative
`D_v r_2[0]` has squared expectation equal to
`||nabla_g r_2[0]||_2^2`.  The pooled RMS over eight direction/trial cells at
each width therefore estimates the desired Euclidean gradient norm.  Bulk
JVPs use the normalized output norm.

| JVP metric | `t=0.25` | `t=0.5` |
|---|---:|---:|
| marked `|D_v r_2[0]|` | `-0.135` | `-0.140` |
| `||D_v x_2||_n` | `-0.428` | `-0.438` |
| `||D_v z_3||_n` | `-0.574` | `-0.556` |
| `||D_v b_3||_n` | `-0.567` | `-0.560` |
| `||D_v u||_n` | `-0.479` | `-0.470` |

Every JVP exponent has the predicted sign and differs from its finite
independent-replacement counterpart by less than `0.07`, well inside the
preregistered tolerance `0.35`.  The estimated marked gradient RMS changes
from `0.754` to `0.640` between widths `128` and `1024` at time `0.25`, and
from `0.691` to `0.581` at time `0.5`; it is compatible with an order-one
gradient rather than a growing one.

## Numerical validity

- Every state was finite and the largest recorded normalized state envelope
  was `1.227`, below the preregistered rejection threshold `100`.
- All exact time-zero coupling identities held with recorded error exactly
  zero.
- The largest relative discrepancy among non-negligible float32
  doubled-resolution control metrics was `0.00417`; there were no failures
  of the `5%`/absolute-`2e-6` gate.
- The largest corresponding float64 mesh discrepancy was
  `5.76e-12`; there were no failures of the `5%`/absolute-`2e-9` gate.
- The final decision computed from the frozen rules is
  `pass_empirical_compatibility`.

Scalar predictor and raw-kernel differences were retained but were not
primary scaling gates.  In particular, absolute scalar cancellation makes
the four-trial kernel slope noisy at time `0.5`; it does not alter the field
or JVP result.

## Exact inference and remaining gap

The experiment supports the following narrow statement:

> On ordinary Gaussian-reachable states at the tested widths and times, a
> single top-source column has order-one influence on its marked transpose
> coordinate and diffuse `n^{-1/2}` influence on normalized bulk fields,
> without visible adaptive amplification.

It does **not** show that the leave-one-column field is conditionally
Gaussian, that rare columns obey a uniform tail bound, or that the estimate
holds after iterating a growing number of response insertions.  In
particular, it does not resolve the collided finite-width sector identified
by the chronological-forest audit.  The theoretical next gate is a uniform
annealed Efron--Stein/Malliavin or cavity estimate that propagates this
one-column influence through time and then controls joint marked forests
without taking absolute values term by term.

## Artifacts

- preregistration: `PREREGISTRATION.md`, Probe C1;
- implementation: `marked_column_cavity_probe.py`;
- analyzer: `analyze_marked_column_cavity.py`;
- primary raw data and metadata:
  `outputs/c1_marked_column_primary_a/` and
  `outputs/c1_marked_column_primary_b/`;
- doubled-resolution controls:
  `outputs/c1_marked_column_refined_a/` and
  `outputs/c1_marked_column_refined_b/`;
- float64 controls:
  `outputs/c1_marked_column_float64_coarse/` and
  `outputs/c1_marked_column_float64_fine/`;
- machine-readable decision and all width slopes:
  `outputs/c1_marked_column_summary/`.
