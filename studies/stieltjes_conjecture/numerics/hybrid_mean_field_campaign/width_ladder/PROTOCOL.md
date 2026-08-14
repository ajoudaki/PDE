# Coupled finite-width ladder: frozen scientific protocol

Status: **protocol specification; no new scientific trajectory is authorized by
this file**.

Parent campaign lock: this child protocol is subordinate to
`studies/stieltjes_conjecture/numerics/hybrid_mean_field_campaign/PROTOCOL.md`
at SHA-256
`d1e75ad896a3572f77b9bc6ec68a7047219a075645b87d44c520d677fc3b153a`.
Any mismatch with that parent protocol invalidates this child campaign.

The purpose of this campaign is to estimate the ordinary-Gaussian,
infinite-width output-coordinate kernel of the canonical one-sample quadratic
network while separating finite-width bias, Monte Carlo variation, numerical
time error, and initialization imbalance.  The campaign is an empirical test of
finite-width convergence.  It is not by itself an identification theorem for
the literal mean-field limit or an all-time theorem.

## 1. Canonical system and limit order

For every width \(n\), initialize \(a_i,W_{ij},u_j\) independently from
\(N(0,1)\), and define

\[
z_i=n^{-1/2}\sum_jW_{ij}u_j^2,
\qquad
f_n=n^{-1}\sum_i a_i z_i^2.
\]

Physical squared-loss gradient flow is

\[
\dot\theta=2(1-f_n)n\nabla f_n,
\qquad
\dot f_n=2(1-f_n)K_n,
\qquad
K_n=n\lVert\nabla f_n\rVert^2.
\]

The finite systems are simulated first at fixed \(n\), then the ordinary
ensemble expectation is estimated, and only then is \(n\to\infty\)
extrapolated.  No microcanonical conditioning, clipping, trajectory deletion,
isotonic repair, or replacement of physical flow by output-clock flow is
permitted.

The checked finite-width equations are imported read-only from
`global_proxy_campaign/reference/canonical_model.py`; its digest is part of the
campaign lock.

## 2. Competing hypotheses and logical scope

- **Regular-limit hypothesis:** on the declared output interval the ordinary
  physical ensemble concentrates around a deterministic kernel, with a
  finite-width expansion compatible with at least one preregistered model.
- **Unresolved/preasymptotic alternative:** widths through 8192 do not identify
  a stable intercept because bias models disagree, paired corrections fail to
  contract, or uncertainty remains wider than the decision target.
- **Numerical/statistical invalidity:** a validity gate fails.  Such an outcome
  is inconclusive and cannot count against the Stieltjes conjecture.

Agreement of a valid extrapolation with a Stieltjes proxy is evidence only for
tested-curve compatibility.  It does not prove series convergence, the
Stieltjes property, interchange of width and time limits, or global training
identification.

## 3. Primary and secondary estimands

Let

\[
m_n(t)=\mathbb E f_n(t),
\qquad m_n(t_n(y))=y.
\]

The primary estimand is the kernel that exactly drives the mean output:

\[
K_{\mathrm{eff},n}(y)
=
\frac{
\mathbb E[(1-f_n(t_n(y)))K_n(t_n(y))]
}{1-y}.
\]

Every bootstrap resample must recompute its own mean curve, its own hitting
time \(t_n^{(b)}(y)\), and its own weighted numerator.  Reusing the full-sample
hitting time inside bootstrap resamples is forbidden.

The secondary estimand aligns each trajectory by normalized training progress.
For each realization \(r\), define

\[
f_{n,r}(\tau_{n,r}(y))
=f_{n,r}(0)+(1-f_{n,r}(0))y,
\qquad 0\le y<1,
\]

and

\[
K_{\mathrm{prog},n}(y)
=\mathbb E K_{n,r}(\tau_{n,r}(y)).
\]

Unlike the absolute pathwise condition \(f=y\), normalized progress is defined
for paths beginning on either side of zero and tends to the ordinary output
coordinate as \(f_n(0)\to0\).  Every trajectory must hit every declared node;
non-hitters invalidate the point and are never dropped or conditioned away.

The nodes are

\[
y\in\{0,0.1,0.25,0.5,0.75,0.9,0.95,0.99\}.
\]

The point \(y=0\) is analyzed only by the initialization calibration in
Section 5.  Positive-node curve inference uses both estimands.  The primary
authorization discriminator is \(y=0.9\); \(y=0.95,0.99\) are tail stresses and
are descriptive unless a later, separately frozen decision explicitly uses
them.

## 4. True nested coupling

Each Gaussian is a deterministic function of

\[
(\text{campaign seed},\text{lineage},\text{tensor domain},\text{coordinate}).
\]

For matrices, the coordinate is the ordered pair \((i,j)\), encoded without a
width-dependent row stride.  Consequently, the arrays at width \(n\) are
bitwise the upper-left/vector prefixes of the same lineage at every larger
width.  The model normalization remains the correct \(n^{-1/2}\) or \(n^{-1}\)
normalization at each width.  Readout-sign antithetic partners share \(W,u\)
and use \(a,-a\).

Merely reusing a stateful RNG seed with differently shaped tensors is not
accepted as nested coupling.

## 5. Exact initialization calibration and controls

At finite width,

\[
\mathbb E K_{a,n}(0)=27+\frac{288}{n},
\quad
\mathbb E K_{W,n}(0)=36+\frac{384}{n},
\quad
\mathbb E K_{u,n}(0)=48+\frac{672}{n},
\]

and hence

\[
\mathbb E K_n(0)=111+\frac{1344}{n}.
\]

Initialization is a separate calibration:

1. antithetic initial outputs must cancel to the declared floating-point
   tolerance;
2. component kernels must sum to the total kernel;
3. every raw component sample mean must lie within four raw lineage standard
   errors of its exact finite-\(n\) expectation;
4. nested prefixes must be bitwise identical before normalization-dependent
   forward evaluation.

The primary positive-time control is the scalar

\[
C_{n,r}=K_{n,r}(0)-(111+1344/n).
\]

At each width, node, and estimand, a four-fold deterministic cross-fit estimates
one scalar coefficient on the other three folds and applies it to the held-out
fold.  Original-sample fold assignment is `lineage mod 4`.  The unweighted
regression is on the linear \(K\) scale and includes an intercept while
estimating the slope:

\[
\widehat\beta=
\frac{\sum_{r\in\mathrm{train}}(C_r-\bar C)(Y_r-\bar Y)}
{\sum_{r\in\mathrm{train}}(C_r-\bar C)^2+\lambda}.
\]

Only the slope is used in the held-out adjustment \(Y_r-\widehat\beta C_r\).
The ridge is fixed at \(10^{-12}\) times the centered training-control sum of
squares, with a machine-tiny floor.  For \(K_{\mathrm{eff}}\), \(Y_r\) is the
lineage-pair weighted kernel at the common ensemble hitting time divided by
\(1-y\).  For \(K_{\mathrm{prog}}\), it is the pair average of the two branch
kernels at their separate normalized-progress hitting times.  Raw lineage
standard error is \(\operatorname{sd}(Y_r)/\sqrt{R}\), with `ddof=1`.

The cross-fit algorithm, scale, ridge, and fold structure are frozen—not the
data-estimated slopes.  Every bootstrap resample refits the complete cross-fit
on that resample.  Holding the original-sample slopes fixed in bootstrap is
forbidden because it would omit coefficient-estimation uncertainty.

The three centered component controls are a sensitivity analysis only.  They
use the same folds and a fixed ridge
\(10^{-10}\operatorname{tr}(C^TC)/3\).  They cannot replace the scalar-control
primary result because 16 lineages are too few for a stable unrestricted
three-control fit.

## 6. Widths, replication, integration, and hard caps

- \(n=1024\) is diagnostic only and is excluded from every intercept fit.
- \(n=2048,4096,8192\), each with 16 common antithetic-pair lineages, form the
  scientific ladder.
- \(n=16384\) is held out and unauthorized.  Passing Section 10 makes it only
  eligible for a new user authorization.
- Float64 is mandatory.
- The physical solver is fixed-step RK4 with \(\Delta t=2\times10^{-5}\) and
  \(t_{\max}=0.024\).
- A two-lineage \(n=4096\) paired run at \(\Delta t=10^{-5}\) is the
  step-halving control.
- Each declared point has a wall, step, host-memory, GPU-memory, state-amplitude,
  and kernel ceiling.  Reaching a cap stops the point and marks it inconclusive.
- The 8192 point is split into provenance shards 0--7 and 8--15 so the two GPUs
  may run independently, but each GPU batch contains exactly one lineage (two
  antithetic trajectories).  Analysis is forbidden unless both shards are
  complete, disjoint, source-identical, and collectively contain exactly
  lineages 0--15.

The cumulative production budget, including failed attempts, is 3300 GPU
wall-seconds: at most 180 seconds for all 2048 work, 720 seconds for all 4096
work including step halving, and 2400 seconds total across the two 8192 shards.

No adaptive extension of time, replication, width, or memory is authorized by
this protocol.

## 7. Step-halving gate

Using exactly lineages 0--1, recompute both estimands from the coarse and fine
raw trajectories.  Initial states must have identical deterministic SHA-256
digests.  The digest is computed before device transfer or any reduction from
the little-endian float64 bytes of \(a,u,W\), with domain separators and the
seed, lineage, and width under scheme `nested-width-initial-state-v1`.  Initial
outputs and kernels are compared only at an eight-ulp-scale tolerance because
GPU batch shape may change reduction order.  The maximum
relative coarse/fine difference must be at most

- \(2\times10^{-3}\) through \(y=0.95\);
- \(5\times10^{-3}\) at \(y=0.99\).

In addition, at \(y=0.9\) the absolute step error for each estimand must be at
most one quarter of that estimand's realized mandatory width-model union.  The
union is computed first without using the fine-step result.  Both the fixed
relative gate and this realized-resolution gate must pass.  Failure makes all
curve inference inconclusive.

## 8. Paired lineage bootstrap

The resampling unit is a whole antithetic-pair lineage, coupled across all
widths.  The frozen analysis uses 20,000 resamples and seed 202608190731.  It is
a four-stratum bootstrap: within each original `lineage mod 4` fold, four
lineages are drawn with replacement.  The same ordered draws are used at 2048,
4096, and 8192.  This keeps every held-out fold populated while retaining the
complete cross-fit in each replicate.

For \(K_{\mathrm{eff}}\), every resample recomputes its mean-output inversion.
For \(K_{\mathrm{prog}}\), each branch is interpolated at its own normalized
progress before branches are paired.  The scalar and component cross-fits are
then refit inside that replicate using the frozen recipe.  At least 99.5% of
requested replicates must satisfy all positivity,
monotonicity, and hitting gates; otherwise analysis is inconclusive.

Uncertainty bands are 99% simultaneous log-kernel max-deviation bootstrap
bands.  The analysis reports raw and scalar-controlled results; scientific
classification uses the scalar-controlled primary estimand, while any material
raw/control disagreement is flagged.

Because \(K_{\mathrm{eff},n}\) is a nonlinear plug-in functional of an
estimated clock at only 16 lineages, the bootstrap is supplemented by a
delete-one-lineage jackknife.  For raw and scalar-controlled estimates at every
node, report

\[
\widehat{\operatorname{bias}}_{\mathrm{JK}}
=(R-1)\left(R^{-1}\sum_i\widehat K_{(-i)}-\widehat K\right)
\]

and the bias-corrected value only as a sensitivity; the primary estimate is
never silently shifted.  At \(y=0.9\), the absolute raw and controlled bias at
every width, and the movement of every mandatory model intercept after the
sensitivity correction, must each be no more than one quarter of the realized
primary mandatory union width.  A larger diagnostic bias makes the campaign
inconclusive rather than widening or recentering the result post hoc.

## 9. Preregistered extrapolation union

At each node, the mandatory model set is

\[
\begin{array}{ll}
\text{top width:}&K_\infty=K_{8192},\\
\text{inverse width:}&K_n=K_\infty+b/n,\\
\text{inverse square-root width:}&K_n=K_\infty+c/\sqrt n.
\end{array}
\]

All intercept regressions are unweighted least squares on the linear \(K\)
scale; logarithms are used only to construct positive simultaneous uncertainty
bands.  The scientific uncertainty set is the nodewise outer union of the
simultaneous bands from all three models.  No post-result model selection is
allowed.

For each affine correction law, the two-width line through 4096 and 8192 is a
mandatory leave-2048 sensitivity.  Its intercept and 99% paired-bootstrap band
are reported separately and never used to narrow the three-model union.

The optional model

\[
K_n=K_\infty+b/n+c/n^2
\]

is included only as a labeled sensitivity if, at every node from 0.5 through
0.95, the two paired adjacent-width corrections have the same sign, their
99% paired bootstrap intervals exclude zero with that sign, and

\[
0.25\le
\left|\frac{K_{4096}-K_{8192}}
{K_{2048}-K_{4096}}\right|
\le0.75.
\]

With only three widths the quadratic model interpolates point estimates, so it
never narrows the mandatory union or overrides a classification.

## 10. Eligibility gate for a separately authorized 16384 holdout

At \(y=0.9\), all of the following are required:

1. every numerical and initialization gate passes;
2. the step-halving gate passes;
3. both adjacent paired corrections are resolved at 99% and contract in
   magnitude;
4. primary and secondary mandatory model-union bands overlap;
5. the scalar-controlled primary mandatory union has full absolute width at
   most 0.8209726639786652, the exact three-moment proxy width recorded in
   `EXACT_PROXY_GATE.json` and bound to its source hashes;
6. for both affine correction laws, the leave-2048 intercept lies inside the
   corresponding full-ladder 99% band and differs from the full-ladder
   intercept by at most half the mandatory union width;
7. define

   \[
   D_n(y)=\left|\log K_{\mathrm{eff},n}(y)
   -\log K_{\mathrm{prog},n}(y)\right|.
   \]

   At every inferential node through 0.9, the point estimates satisfy
   \(D_{8192}\le D_{4096}\le D_{2048}\); at \(y=0.9\), the 99% paired-bootstrap
   upper endpoint for \(D_{8192}-D_{4096}\) is strictly below zero;
8. the step-error requirements of Section 7, including the one-quarter actual
   union-width gate, pass.

Passing does not launch \(n=16384\).  It creates only the status
`eligible_for_separate_authorization`.  Failure stops the direct-width branch
at 8192 as inconclusive or preasymptotic.

## 11. Evidence classifications

- **Compatible:** every validity gate passes and the eventual, separately
  frozen Stieltjes comparison contains the complete primary mandatory union at
  all inferential nodes through 0.9.
- **Contrary:** every validity gate passes and a signed escape from the frozen
  Stieltjes band is reproduced by both estimands and all mandatory width models.
- **Inconclusive:** any validity failure, model overlap, unresolved width trend,
  insufficient precision, or conflict between estimands.

This width-ladder campaign cannot on its own declare the strongest global
conjecture proved or falsified.

## 12. Reproducibility and immutability

Every scientific output must record the exact command, environment, config
digest, protocol digest, source digests, canonical-model digest, lineage range,
device, resource telemetry, failure state, and raw arrays needed to recompute
both estimands.  Scientific execution requires a separate unlock record that
matches all frozen digests.  Validation and preflight outputs are permanently
labeled non-scientific.
