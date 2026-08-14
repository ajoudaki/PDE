# Existing-MFP breadth panel — frozen research contract

Status: **prospective; no breadth trajectory has been launched**.

This successor tests whether the large NTK → M1 → M2 improvement and the
associated conditional Stieltjes bounds recur across configurations whose MFP
jets are already exact.  It computes no new derivative and does not attempt to
resolve the much smaller canonical M3–M5 differences.

The predecessor FP32 Stage V remains failed for \(h=5\times10^{-6}\).  This is
a separate, explicitly post-hoc engineering qualification of Euler
\(h=10^{-5}\), justified only for proxy gaps at least 2% and output coordinates
\(0\le y\le0.95\).  Every comparison carries a fixed 0.20% nodewise numerical
kernel envelope.  It estimates a fixed-step FP32 finite-width prelimit, not a
literal continuous-time or width-first theorem.

## 1. Proxy hierarchy and claim

For each accepted family write

\[
K(y)=A+y^2\int_0^\infty\frac{\rho(d\lambda)}{1+\lambda y^2}.
\]

The three primary levels are

\[
K_0(y)=A,
\qquad
K_{\rm M1}(y)=A+\mu_0y^2,
\qquad
K_{\rm M2}(y)
=A+\frac{\mu_0y^2}{1+(\mu_1/\mu_0)y^2}.
\]

Conditional on the Stieltjes conjecture,

\[
K_0\le K_{\rm M2}\le K\le K_{\rm M1}\qquad(y\ge0).
\]

Thus the primary test is contraction of the conditional interval

\[
[K_0,K_{\rm M1}]\longrightarrow[K_{\rm M2},K_{\rm M1}],
\]

not a requirement that alternating approximants have monotonically decreasing
individual errors.  Where \(\mu_2\) or more is already available, later
Gauss/zero-Radau intervals are reported secondarily without increasing the
simulation budget.

For label-one scalar loss,

\[
\dot y=2(1-y)K(y),\qquad L=(1-y)^2.
\]

Kernel bounds are propagated through this ODE to give output and loss bounds.
Those are consequences and consistency checks, not independent evidence.

## 2. Frozen core configurations

All proxy coefficients come from the existing exact inventory.  The primary
physical points are:

| key | configuration | moment depth | symmetric M1–M2 gap at \(y=.9\) |
|---|---|---:|---:|
| C | canonical one input | \(\mu_0,\ldots,\mu_4\) | 2.53% |
| A | first activation \(u^2-1\) (\(c=1\)) | \(\mu_0,\mu_1,\mu_2\) | 9.55% |
| M | relative block metric \(\lambda=2\) | \(\mu_0,\ldots,\mu_3\) | 2.97% |
| V | middle-weight initialization variance \(v=1/2\) | \(\mu_0,\ldots,\mu_4\) | 14.31% |
| T+ | two inputs, \(t=\theta^2=1/2\), labels \(+,+\) | \(\mu_0,\mu_1,\mu_2\) | 2.76% |
| T− | same inputs, labels \(+,-\) | \(\mu_0,\mu_1,\mu_2\) | 8.02% |

The angle is fixed as \(\theta=+1/\sqrt2\); its sign is redundant for the
quadratic activation.  No \(B=3\), \(B=4\), cubic, depth, or new-MFP branch is
authorized.

Every tabulated gap means

\[
\frac{K_{\rm M1}(.9)-K_{\rm M2}(.9)}
{[K_{\rm M1}(.9)+K_{\rm M2}(.9)]/2}.
\]

For V, the stored normalized kernel obeys

\[
K_v(y)=v\,\kappa_v(y/v).
\]

All physical comparisons must apply this coordinate conversion.

## 3. Hidden observables at M

The \(\lambda=2\) trajectory also records

\[
Q_1=n^{-1}\sum_j u_j^2,
\qquad Q_2=n^{-1}\sum_i z_i^2,
\]

and their RMS square roots.

The first norm is inherited from the output kernel:

\[
\frac{dQ_1}{dy}=\frac{8\lambda y}{K_\lambda(y)}.
\]

It is a consistency test, not independent Stieltjes evidence.  The second norm
has its own accepted companion moments.  Writing

\[
N_2(y)=3+y^2T_2(y^2),
\]

its M1/M2 interval is an independent expanded-observable conjecture.  The
primary comparison uses output coordinate \(y\), not physical time.

## 4. Faithful two-input reduction and leakage

The two-input runs use the actual average squared loss, never an imposed scalar
feature-ascent direction.  For labels \(s=(1,\sigma)\), define signed margins

\[
m_1=f_1,\qquad m_2=\sigma f_2,
\qquad g=\frac{m_1+m_2}{2},
\qquad \delta=\frac{m_1-m_2}{2}.
\]

Then exactly at finite width

\[
L=(1-g)^2+\delta^2.
\]

With

\[
K_g=n\|\nabla g\|^2,
\quad K_\delta=n\|\nabla\delta\|^2,
\quad C=n\langle\nabla g,\nabla\delta\rangle,
\]

natural loss flow gives

\[
\dot g=2[(1-g)K_g-\delta C],
\qquad
\dot\delta=2[(1-g)C-\delta K_\delta].
\]

The input Gram matrix must enter both the Gaussian initialization and the
first-layer gradient metric.  The effective scalar-channel kernel is

\[
K_{\rm eff}(y)=
\frac{\mathbb E[(1-g)K_g-\delta C]}{1-\mathbb Eg}.
\]

Every run retains \(\mathbb E K_g\), \(\mathbb E\delta^2\),
\(\mathbb E(\delta C)\), \(|C|/\sqrt{K_gK_\delta}\), full physical loss, and
projected loss.  Failure of transverse leakage to contract with width makes
the scalar Stieltjes comparison inconclusive.

## 5. Numerical-method gates

The production candidate is deterministic IEEE FP32 explicit Euler with
\(h=10^{-5}\).  TF32 is disabled.  Each noncanonical configuration first runs
one common \(n=4096\) antithetic lineage at \(h=2\times10^{-5}\) and
\(10^{-5}\), through \(y=.95\).  The validation pair has a 30-second internal
cap per point and 60 GPU-seconds cumulative per configuration.

The fine point is locally valid only if, through \(y=.95\):

- state and positive kernel components are finite;
- mean output is nondecreasing and mean loss nonincreasing within \(10^{-6}\);
- \(a/u\) update cosines are at least 0.999 and sampled-\(W\) cosine at least
  0.995;
- \(a/u\) norm ratios lie in [0.95,1.05] and sampled-\(W\) in [0.80,1.20];
- driver maximum is at most 0.20%, RMS at most 0.05%, and cumulative defect at
  most 0.05%;
- the symmetric coarse/fine difference in the primary kernel is at most
  \(\min(0.20\%,\text{one quarter of the frozen M1--M2 gap})\).

Unchanged-entry fractions are retained as red flags, not used alone as a
failure criterion: aggregate norm, cosine, and driver gates measure lost
update geometry more directly.  Q2 requires the same 0.20% symmetric
coarse/fine tolerance in output coordinates.  Each two-input \(K_g\),
effective numerator, and leakage score defined below requires the same local
validation; canonical validation cannot certify them by analogy.  No
\(h<10^{-5}\) run is permitted.

For T± the discrete driver gate is applied to the exact channel numerator
\((1-g)K_g-\delta C\): the forward difference of the ensemble mean \(g\) is
compared with twice its ensemble mean at the left endpoint, and nodes use the
common ensemble-\(g\) clock.  It is not replaced by \((1-g)K_g\) when leakage
is nonzero.

Every accepted nodewise kernel band is enlarged multiplicatively by 0.20%.
Output/loss propagation additionally includes the measured cumulative driver
allowance.  Nodes above \(y=.95\) are descriptive only.

## 6. Bounded width/replication ladder

After local validation, each configuration starts with eight common nested
antithetic lineages at \(n=2048\) and \(4096\).  This first block is a
resolution screen only and cannot produce a compatible or contrary verdict.
A second block of eight lineages is authorized only when the first-block
simultaneous relative half-width at \(y=.9\), including the 0.20% numerical
allowance and width-model spread, is no more than one half of that
configuration's frozen M1--M2 gap.  This rule is independent of the observed
center.  A broader first-block band stops that configuration as
resolution-inconclusive rather than spending another block.

Per configuration and width:

| stage | lineages | one-input GPU cap | two-input GPU cap |
|---|---:|---:|---:|
| \(n=2048\), first block | 8 | 30 s | 45 s |
| \(n=4096\), first block | 8 | 90 s | 150 s |
| optional second block | 8 | same | same |

The cumulative core-screen cap is 1800 GPU-seconds, including failed points.
Lineages are split across the two GPUs.  The memory-safe batch unit is exactly
one antithetic lineage (two trajectories); a shard is a provenance group, not
a tensor batch.

At most two configurations may be promoted to \(n=8192\), in this fixed
priority order among unresolved valid screens:

1. T− (label-character and multi-input stress);
2. M (independent hidden companion);
3. T+;
4. A;
5. V;
6. C.

Promotion receives at most 16 lineages and 600 GPU-seconds per configuration,
with 1200 GPU-seconds cumulative.  \(n=16384\) has zero budget.  Passing a
screen never authorizes it automatically.

## 7. Statistical estimands and decisions

At common ensemble-output time \(t_n(y)\), \(\mathbb E f(t_n(y))=y\), retain

\[
K_{\rm eff,n}(y)=\frac{\mathbb E[(1-f)K]}{1-y},
\qquad K_{\rm dir,n}(y)=\mathbb E K.
\]

Their exact finite-width difference is

\[
K_{\rm eff,n}=K_{\rm dir,n}
-\frac{\operatorname{Cov}(f,K)}{1-y}.
\]

Also retain

\[
\mathbb E(1-f)^2-(1-\mathbb Ef)^2=\operatorname{Var}(f).
\]

The primary nodes are \(y\in\{.5,.75,.9,.95\}\).  \(y=0\) is a separate
initialization calibration and is excluded from simultaneous containment,
because all proxy intervals collapse there while a finite-width confidence
band does not.

For V these are **physical** output nodes.  The proxy evaluator must use
\(z=y/v\), \(\kappa(z)=K_v(y)/v\), while the empirical common clock remains
the physical output clock.  A checked end-to-end regression is mandatory.

For T± define the dimensionless leakage score

\[
\Lambda_n=\max_y\left\{
\frac{\sqrt{\mathbb E\delta^2}}{1-y},
\frac{|\mathbb E(\delta C)|}{\mathbb E[(1-g)K_g]},
\frac{\mathbb E|C|}{\sqrt{\mathbb EK_g\,\mathbb EK_\delta}}
\right\}.
\]

The scalar-channel result is eligible only if the point estimates satisfy
\(\Lambda_{4096}\le0.9\Lambda_{2048}\) and
\(\Lambda_{4096}\le0.05\).  Otherwise it is leakage-inconclusive.  These
thresholds are diagnostics of convergence to the symmetry channel, not a
theorem about the finite-width dynamics.  The gate is a conservative point
diagnostic; bootstrap leakage bands are reported but are not required to
satisfy the 0.9 contraction factor.

Bootstrap whole antithetic lineages with the same indices across widths.
Regression/control coefficients and mean-clock inversions are recomputed in
each resample.  Use 20,000 deterministic resamples and require at least 95%
valid replicates.  The reported 99% simultaneous bootstrap band is explicitly
a small-sample sensitivity band, not an exact coverage guarantee.  Eight
lineages are resolution-only; any directional classification requires all 16.
Raw estimates are primary; cross-fitted \(K_n(0)\)-controlled estimates are
precision companions.  The control is enabled only after its exact
family-specific finite-width expectation and transformed-prefix coupling pass
unit tests.  A raw/controlled conflict is inconclusive.

The frozen total-kernel control means in physical coordinates are

| key | exact \(\mathbb E K_n(0)\) |
|---|---:|
| C | \(111+1344/n\) |
| A | \(60+840/n\) |
| M | \(195+2400/n\) |
| V | \(36.75+432/n\) |
| T+ | \(80+970/n\) |
| T− | \(31+374/n\) |

For V the normalized control is twice the physical value.  Componentwise
controls are checked in source and retained as diagnostics, but the scalar
total is the primary variance-reduction covariate.

With only two widths, the width-model band is the outer union of the top-width
band and affine \(1/n\) and \(1/\sqrt n\) extrapolations.  A promoted third
width adds the top-two \(1/n\) model.  No quadratic fit is allowed.

For each proxy \(P\), report

\[
E_P=\sup_{.5\le y\le.95}
\left|\log\frac{P(y)}{K_{\rm ref}(y)}\right|.
\]

Equal-information Taylor truncations are controls only; their global failure
does not count against Stieltjes because the formal Taylor series has zero
radius.

Classification per configuration (only after 16 lineages at both base
widths):

- **compatible:** the numerical+statistical+width band is inside
  \([K_{\rm M2},K_{\rm M1}]\) at every resolvable node and all local/leakage
  gates pass;
- **contrary:** a definite same-signed escape occurs at both valid top widths
  and in the conservative extrapolation, for raw and controlled estimators;
- **inconclusive:** any boundary is touched, a width model is unstable, the
  band is too wide, or a numerical/leakage gate fails.

Compatibility is strong finite-width robustness evidence, not a proof of the
global Stieltjes conjecture or identification of the formal MFP jet with a
literal width-first curve.

## 8. Stop rules

The fixed screen order is T−, M, T+, A, V, C.  Stop the entire panel if the
common Euler implementation fails its local gates in two configurations, if
cumulative caps are reached, or if the first three valid screens all remain
statistically unresolved at M1/M2 scale.  Do not
respond by lowering the FP32 step, adding \(n=16384\), computing new MFP jets,
or expanding to more architectures.  Any such move requires a new research
round and contract.
