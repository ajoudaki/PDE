# Frozen successor 02: auditable canonical pilot

Status: **frozen before any successor-02 trajectory**.  This is a separately
named successor to the closed Stage-2 run in `PROTOCOL.md`.  It neither
amends nor reclassifies that run, and it preserves every predecessor and
successor-01 artifact.

## 1. Ancestry and data-independence

The original Stage-2 run stopped after 7.623125169426203 seconds because its
first physical point had `max_time=0.012`, which did not reach the registered
$y=.99$ node.  It wrote no NPZ and exposed only the censored statement
$T_n(.99)>.012$.  Its classification remains permanently inconclusive.

`SUCCESSOR_01_PROTOCOL.md` and `configs/FROZEN_SUCCESSOR_01.json` were drafted
before another neural trajectory was run.  A hostile pre-execution audit
found four avoidable ambiguities: its enlarged raw-array caps were not needed,
its four-lineage half-step run was called held out rather than explicitly
paired to the coarse run, it had only one output-clock width, and its offline
analysis choices were not all frozen in a machine-readable file.  Successor
01 was therefore not executed.  It remains an immutable historical artifact;
successor 02 is not a retrospective reinterpretation of it.

No kernel, output, loss, projection, or finite-width trajectory value was
available when this protocol, `configs/FROZEN_SUCCESSOR_02.json`, and
`configs/FROZEN_SUCCESSOR_02_ANALYSIS.json` were fixed.  The physical horizon
remains the a-priori value $0.024$, selected from the old NTK and one-moment
proxy hitting times, not from a neural trajectory.

## 2. Scientific question and estimands

The claim tested is exactly the canonical conjunction in `PROTOCOL.md`: the
ordinary finite-width natural squared-loss flow has a deterministic
width-first kernel on $0\leq y\leq.99$, that kernel has the accepted MFP jet,
and it is the Stieltjes resolvent selected by the accepted moments.

The primary estimator is the ordinary antithetic physical-flow kernel formed
after ensemble averaging,

$$
\widehat K_{\mathrm{eff},n}(y)
=\frac{\widehat{\mathbb E}[(1-f_n)K_n]}{1-\widehat{\mathbb E}[f_n]}.
$$

The rank-one-centered output-clock ensemble is still a sensitivity analysis,
not a replacement estimand.  Its two widths test whether the conditioned and
ordinary width limits agree and whether the conditioning projection shrinks.

## 3. Frozen points

Every point uses float64 RK4, target one, seed base `202608140200`, and output
nodes

$$
(0,.1,.25,.5,.75,.9,.95,.99).
$$

| point | mode | $(n,R)$ | step | endpoint | role | raw cap |
|---|---|---:|---:|---:|---|---:|
| `canonical_physical_n256_r32` | physical | $(256,32)$ | $2\cdot10^{-5}$ | $t=.024$ | ordinary width ladder | 32 MiB |
| `canonical_physical_n512_r16` | physical | $(512,16)$ | $2\cdot10^{-5}$ | $t=.024$ | ordinary width ladder | 32 MiB |
| `canonical_output_clock_n256_r32` | output clock | $(256,32)$ | $.002$ | $y=.99$ | centered width sensitivity | 32 MiB |
| `canonical_output_clock_n512_r16` | output clock | $(512,16)$ | $.002$ | $y=.99$ | centered width sensitivity | 32 MiB |
| `canonical_physical_n512_r4_halfstep` | physical | $(512,4)$ | $10^{-5}$ | $t=.024$ | paired step halving | 16 MiB |

The half-step point is **not held out**.  Because initialization is generated
independently from `seed_base + 104729 * pair_index`, its four lineages are
exactly lineages $0,1,2,3$ of `canonical_physical_n512_r16`.  The coarse
comparison is recomputed from that four-lineage subset after recomputing and
inverting its own ensemble mean-output clock.  Comparing the coarse 16-pair
estimate to a fine four-pair estimate is forbidden.

All per-point `analysis` objects contain the consumed
`comparison_group`, `family_key`, and `role` fields.  The half-step object also
names its coarse partner and its paired lineage indices.  These fields, not
filename inference, determine analysis membership.

## 4. Frozen uncertainty and width analysis

The authoritative choices are in
`configs/FROZEN_SUCCESSOR_02_ANALYSIS.json`.  In summary:

- resample whole antithetic pair lineages, separately for every registered
  point, using 2,000 distinct fixed-seed resamples;
- construct 99% studentized maximum-absolute-deviation bands on the
  log-kernel scale and reject a point if fewer than 95% of resamples span the
  common grid;
- for each of the ordinary and output-clock groups, take the nodewise outer
  union of `inv_n_all`, `inv_sqrt_n_all`,
  `inv_n_leave_smallest`, and `top_width_direct`, retaining `inv_n_all` only
  as the central curve;
- use the ordinary sensitivity union for every scientific Stieltjes
  comparison.  The output-clock union is diagnostic only.

The Stage-3 resolution gate is fixed at $y=.9$.  For the bracket using
$\mu_0,\mu_1$,

$$
\log(K^+/K^-)=0.025280526092500397\ldots,
$$

so the complete ordinary 99% sensitivity-union band must have full log width

$$
\log(U_{.99}/L_{.99})
\leq 0.012640263046250199.
$$

This is a pre-run arithmetic constant: exactly one half of the accepted
two-moment bracket width, up to the displayed floating representation.

## 5. Paired step-halving gate

Let $I=\{0,1,2,3\}$ and let $\widehat K_{h,I}$ denote the physical effective
kernel recomputed from precisely those coarse lineages, including a fresh
inversion of their mean-output clock.  Let $\widehat K_{h/2,I}$ be the
corresponding four-lineage fine result.  Initial output and direct-kernel
arrays for the paired lineages must be bitwise equal at time zero.  Define

$$
d_K(y)=
\frac{|\widehat K_{h,I}(y)-\widehat K_{h/2,I}(y)|}
{|\widehat K_{h/2,I}(y)|}.
$$

Positivity of the denominator is already a mandatory numerical gate.  The
step gate is

$$
\max_{y\leq.95}d_K(y)\leq2\cdot10^{-3},
\qquad d_K(.99)\leq5\cdot10^{-3}.
$$

Failure is numerical inconclusiveness, never evidence against the
conjecture.

## 6. Output-clock, projection, and self-averaging gates

At every common node the ordinary and output-clock 99% width-union intervals
must overlap:

$$
\max(L_{\rm physical},L_{\rm clock})
\leq\min(U_{\rm physical},U_{\rm clock}).
$$

The maximum relative rank-one projection must be finite, nonnegative, and
strictly smaller at width 512 than at width 256.  As a rate sanity check,
$\sqrt{512}p_{512}/(\sqrt{256}p_{256})$ may not exceed 2.  These two finite
widths cannot prove that the projection vanishes; failure merely prevents the
conditioned clock from validating the ordinary reference.

For the two ordinary widths, define

$$
J_n=\max_y
\frac{|\widehat{\mathbb E}(1-f)^2-(1-\widehat{\mathbb E}f)^2|}
{\widehat{\mathbb E}(1-f)^2}
$$

and

$$
S_n=\max_y
\frac{\operatorname{sd}(K_{\rm pair,n}(y))}
{|\operatorname{mean}(K_{\rm pair,n}(y))|\sqrt R}.
$$

Independent whole-lineage bootstraps form frozen equal-tail 99% percentile
intervals for $J_{512}-J_{256}$ and $S_{512}-S_{256}$.  A lower endpoint
strictly above zero is a statistically resolved worsening and makes the
pilot inconclusive.  An unresolved trend is not affirmative evidence of
self-averaging.

Every physical point must retain nondecreasing mean output and nonincreasing
mean loss within $10^{-10}$.  Every output-clock point must have maximum
clock defect at most $10^{-7}$.  Every point must satisfy its recorded
float64 antithetic-cancellation bound

$$
64\epsilon_{64}\max(1,\max|f_n(0)|).
$$

All registered pairs must remain present at every node.  Clipping, dropping,
isotonic repair, seed substitution, and post-hoc grid changes are forbidden.

## 7. Classification and stopping

After all validity gates pass:

- **compatible** at a moment prefix means the complete ordinary 99%
  sensitivity-union band lies inside its rational bracket at every node;
- **contrary** requires a definite signed escape of the union and the same
  signed escape at both ordinary finite widths;
- every overlap, failed validity gate, incomplete point, unresolved
  resolution gate, or width/clock discrepancy is **inconclusive**.

The fixed-parity rational subsequences, Taylor controls, hitting times,
outputs, losses, and terminal rate are reported exactly as in `PROTOCOL.md`.
They do not alter the three-way classifier.  Passing this pilot can authorize
only the already-frozen Stage-3 branch of `PROTOCOL.md`; it cannot prove the
global conjecture.

## 8. Hard ceilings and one-attempt rule

Each point has a 600-second, 8-GiB GPU-allocation, and 8-GiB host-RSS cap.
Declared batch-step caps are 4,800 for physical points and 1,980 for
output-clock points.  State and kernel ceilings are unchanged.

The predecessor's 7.623125169426203 seconds remain charged.  Consequently the
successor-02 configuration has a run wall cap of
`2392.376874830574` seconds, so predecessor plus successor cannot exceed
2,400 seconds.  The global cap intersects every point cap and may stop the
last point early.

There is one successor-02 attempt only.  No retry, horizon change, cap
increase, batch-size change, seed change, partial-run salvage, successor 03,
or larger-width rescue is permitted.  Any failure closes this neural pilot.

Because the capped wrapper is part of the source hash, the final CPU, GPU-0,
and GPU-1 `validation_v3` configurations must all pass after this wrapper
change and before an unlock can be written.  A future unlock must bind the
successor-02 protocol, production config, analysis config, and final source
bundle hashes.  This protocol creates no unlock and executes no trajectory.
