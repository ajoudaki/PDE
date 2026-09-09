# Preregistered Machinery Probes

## General evidentiary rule

These computations are witness tests for proposed norms and recursions.  They cannot prove compact-time convergence.  A clean failure can falsify a particular certificate; a clean success only justifies investing in its proof.  Scripts, environment metadata, raw outputs, and plots must remain under this experiment directory.

## Probe H1: Hermite tail of the arctangent differential chain

### Question

Does `arctan(Z)` or `d(Z)=(1+Z^2)^{-1}`, for `Z~N(0,1)`, have an exponentially weighted Wiener-chaos tail, or only a root-exponential/Gevrey tail?

### Method fixed in advance

1. Compute normalized probabilists-Hermite coefficients
   \[
   c_k(h)=\mathbb E[h(Z)\,\mathrm{He}_k(Z)]/\sqrt{k!}
   \]
   for `h=arctan,d`, using high-order Gauss--Hermite quadrature and a stable normalized three-term recurrence.
2. Use parity as an internal check: even coefficients of arctangent and odd coefficients of `d` must be zero to numerical accuracy.
3. Repeat with at least two quadrature orders.  Retain a coefficient only while the two estimates agree to relative error below `10^-6` or absolute error below `10^-13`.
4. On the reliable tail, compare least-squares fits of
   \[
   \log|c_k|=a-b\sqrt{k}+c\log k,
   \qquad
   \log|c_k|=a-bk+c\log k,
   \]
   on an early fit interval and a disjoint late validation interval.

### Predicted outcomes and decisions

- A stable linear-in-`k` decay supports an exponential chaos weight.
- A stable linear-in-`sqrt(k)` decay with materially smaller validation residual rejects every fixed positive exponential chaos weight `sum exp(rho k)|c_k|^2`, while remaining compatible with factorial Malliavin-response norms and root-exponential truncation.
- Failure of quadrature agreement leaves the test undecided.

The response calculus will not conflate a positive derivative-generating radius with exponential chaos decay.

## Probe Q1: scaling of the first adaptive transpose query

### Question

Are the proposed normalized Malliavin response energies dimension-uniform even for a transpose query that reuses the forward matrix?

### Cell

At initialization of the two-hidden-layer arctangent model,

\[
x=\arctan u,
\quad z=\Gamma x,
\quad b=A(1+z^2)^{-1},
\quad q=\Gamma^*b,
\]

with iid standard Gaussian `u,A` and `Gamma_ij=n^{-1/2}g_ij`.

### Method fixed in advance

For widths in a geometric grid and independent replicates:

1. record normalized coordinate moments of `q` through at least order eight;
2. compute the exact first derivative
   \[
   D_{ab}q_k
   =\frac{\mathbf1_{b=k}}{\sqrt n}A_a d(z_a)
   +\frac1n g_{ak}A_a d'(z_a)x_b;
   \]
3. record
   \[
   E_{2,1}(q)^2
   =\frac1n\sum_k\sum_{a,b}|D_{ab}q_k|^2;
   \]
4. independently estimate the same Hilbert--Schmidt norm with randomized Jacobian-vector products as an implementation check.

### Predicted outcomes and decisions

- Tight width trajectories for the coordinate moments and `E_{2,1}` validate the proposed normalization and the exact response-query atom at first order.
- Polynomial growth in `n` after analytic and randomized implementations agree falsifies that response normalization before any flow experiment.
- Tightness here does not establish preservation under training or at higher response order.

## Probe K1: Koopman/Taylor coefficient growth on the full arctangent `L=2` flow

### Question

Is a simple width-uniform time-analytic Koopman bound already implausible on the mandatory nonlinear ladder rung?

### Method fixed in advance

1. Implement truncated-power-series arithmetic for the exact finite-width ODE, including convolutional matrix products, normalized rank-one updates, arctangent composition via its rational derivative, and reciprocal series.
2. Compute Taylor coefficients at `t=0` through the highest order that passes residual and precision checks for `f` and `Theta`.
3. Use several widths and independent seeds.  Record the median and upper quantiles of
   \[
   |[t^k]Q_n(t)|^{1/k}
   =\left|\mathscr L^kQ_n(Y_n(0))/k!\right|^{1/k}.
   \]
4. Validate low orders against finite differences or automatic Taylor-mode differentiation and validate the ODE-series residual coefficientwise.

### Predicted outcomes and decisions

- Stabilization in width and bounded coefficient roots over a growing reliable order range is weak support for a local analytic hierarchy; it is not a proof.
- Reproducible growth of the coefficient roots with both order and width falsifies the simple uniform analytic Koopman estimate.
- Coefficient cancellation in `f` will be handled by also testing nonnegative `Theta` and selected squared state contractions; no conclusion will be drawn from a single near-zero scalar series.

## Probe K0: unbounded-seed obstruction to a uniform Koopman radius

### Question

Does Gaussian readout initialization already destroy a uniform time-analytic `L^p` radius in the coordinate-only one-hidden-layer arctangent flow?

### Cell and exact leading-degree prediction

Use

\[
\dot A=\arctan u,
\qquad
\dot u=A(1+u^2)^{-1},
\qquad
u(0)=0,quad A(0)\sim N(0,1).
\]

Set `R(u)=u+u^3/3` and let `psi=R^{-1}`.  Under the large-initial-velocity scaling `tau=A(0)t`, the leading weighted-degree part has `u=psi(tau)` and

\[
\Theta/A(0)^2\longrightarrow \psi'(\tau)^2.
\]

The inverse map has branch points at `tau=+/-2i/3`, so the leading coefficient `h_k=[tau^k]psi'(tau)^2` has limsup root `3/2`.  Therefore the coefficient `[t^k]Theta` is a polynomial in `A(0)` of degree `k+2` with leading coefficient `h_k`.

### Method fixed in advance

1. Compute the exact ordinary Taylor recurrence through at least order 120, vectorized over Gauss--Hermite nodes for `A(0)`.
2. Use two quadrature orders and require agreement for signed expectations and coefficient `L^2` norms.
3. Verify `(k+1)[t^(k+1)]f=[t^k]Theta` and compare the numerically extracted top polynomial coefficient against a separate inverse-series computation of `psi'(tau)^2` at low orders.
4. Record roots of both the signed mean coefficient and its Gaussian `L^2` norm.

### Decision

- Divergence of the `L^2` coefficient roots like `sqrt(k)`, as predicted by the nonzero top Hermite component, rigorously kills a width-uniform analytic Koopman estimate in an `L^2` state norm.
- Divergence of the signed-mean roots also kills analyticity of the deterministic limiting observable itself.
- Bounded roots would trigger an audit of the leading-degree derivation or a cancellation theorem; no analytic claim will be inferred merely from orders too low to see the asymptotic.

## Probe G1: truncation and restart defect

This probe is deferred until a precise graded projection is fixed.  Before it is run, the projection, time integrator, norm, cutoff sequence, and pass/fail threshold must be added here.  No post hoc Galerkin experiment will be treated as evidence.

## Probe O1: depth-three reachable-tail and self-clip probe

### Purpose

The analytic frontier after the Yudovich--Orlicz stability lemma is the
projective moment estimate

\[
 \sup_{n,R,t\le T}\|r_2^R(t)\|_{p,*}\le K_Tp^\beta,
 \qquad \beta\le1,
\]

for the depth-three arctangent flow with `r_2` clipped at radius `R` only in
the hidden gate `b_2=d(z_2)kappa_R(r_2)`.  O1 is a route discriminator for
that estimate, not evidence for convergence by itself.

### Frozen implementation

- Gaussian seeds `A_0,u_0` and two persistent matrices with entries
  `N(0,1/n)`.
- Explicit Euler in raw feature time.  Learned matrices are represented by
  their exact Euler rank-one histories, so forward and transpose actions use
  the same source matrix and the same learned history.
- Coupled trajectories use the same initialization and source matrices.
- Configurations: untruncated and hard clips `R in {1,2,3,4,6,8}`.  Hard
  clipping is used only for the empirical discriminator; the proof calculus
  uses smooth clipping.
- Primary horizons `T in {0,0.25,0.5,1}`; primary step `h=0.005`.
- Widths `n in {1024,2048,4096,8192}` as resources permit, at least four
  independent trials per width.  A step-doubling control compares
  `h=0.01,0.005,0.0025` at `n=1024`.
- Float32 GPU arithmetic is admissible after the step-doubling control;
  finite-width identities are checked from the stored fields.

### Recorded statistics

For `p in {2,3,4,6,8,10,12,16}` record

\[
 M_p(t)=\left[n^{-1}\sum_i|r_{2i}(t)|^p\right]^{1/p},
 \quad M_p/\sqrt p,\quad M_p/p.
\]

Also record empirical excess energies

\[
 \tau_S(t)=\left[n^{-1}\sum_i(|r_{2i}(t)|-S)_+^2\right]^{1/2},
 \qquad S\in\{1,1.5,2,2.5,3,4,5,6\},
\]

state energies, predictor, partial raw-kernel terms, maximum coordinate, and
coupled untruncated-versus-clipped `L^2` discrepancies in `A,u,r_2`.

### Preregistered interpretations

- **Compatible with the required envelope:** at fixed horizon the curves
  `M_p/p` do not turn upward with `p`, width, or self-clip radius beyond the
  step/trial uncertainty; `tau_S` decreases with `S`; and increasing the
  self-clip radius does not systematically inflate the bulk scale of
  `r_2^R`.
- **Evidence for the stronger subgaussian candidate:** `M_p/sqrt(p)` is
  approximately bounded over the reliable moment range and empirical
  `log tau_S` is closer to affine in `S^2` than in `S`.
- **Kill signal for the proposed moment route:** `M_p/p` grows reproducibly
  with both `p` and width, or the bulk/tail scale of `r_2^R` grows
  reproducibly with its own clip radius, after step refinement and across
  trials.
- Moments whose effective sample size is visibly dominated by fewer than
  ten coordinates are reported but excluded from model comparison.
- Agreement of raw and clipped trajectories is not a proof of tail closure;
  disagreement at modest `R` is not a kill unless it persists systematically
  as `R` and numerical resolution increase.

## Probe G2: reachable one-step defect of gate-resolved peeling

### Purpose

The deterministic spike construction falsifies uniform gate-block stability
on all normalized-`L^2` energy balls.  It does not decide whether Gaussian
initialization and its finite-time reachable set suppress those spikes.  G2
tests the narrower empirical proposition that the gate-resolved frozen-input
block has a width-stable local defect along actual depth-three trajectories.

### Frozen implementation

- Activations `phi_alpha(z)=alpha*z+atan(z)` with
  `alpha in {0,0.05,0.2}`.
- Gaussian `u_0,A_0` and two persistent iid `N(0,1/n)` matrices.
- First evolve the exact finite-width ODE to base times
  `t_0 in {0,0.25,0.5}` using RK4 with a reference step no larger than
  `2^-11`.
- From each base state compare: (i) a reference RK4 interval of length `h`,
  and (ii) one exact frozen-input peeling block (top coordinate subsystem
  solved by refined RK4, followed by the paired-edge recursion and forward
  reconstraint).
- Widths `n in {128,256,512,1024}`, at least four coupled seeds where
  resources permit.  Step sizes `h in {0.04,0.02,0.01,0.005}`.  Repeat the
  smallest two steps with the reference resolution doubled.

### Recorded statistics

Record normalized `L^2` errors in `A,u`; ordinary Frobenius and sampled
operator-action errors in each learned matrix increment; forward and
backward field errors; predictor and raw-kernel errors.  Report
`err/h`, `err/h^(3/2)`, and `err/h^2`, empirical log--log slopes, maximum
coordinates, and reliable `L^4/L^2` ratios of the backpropagated fields.

### Preregistered decisions

- A width-stable slope strictly above one for the parameter/predictor/kernel
  defects is compatible with a reachable-set consistency modulus and
  motivates a theoretical restricted-tangent program.
- A stable slope near two supports the strongest ordinary local-error
  conjecture, but does not prove it.
- Growth of `err/h` with width, or slopes tending to one as width grows after
  reference refinement, is a kill signal for this gate block as a mesh-
  removal mechanism even on the tested reachable ensemble.
- Pure arctangent versus positive `alpha` is interpreted only as a mechanism
  comparison; no `alpha downarrow 0` theorem is inferred.
- Passing G2 cannot overcome the deterministic no-go.  A proof would still
  need a uniform probabilistic reachable-state certificate and a restart
  theorem.

## Probe G3: compact-time accumulation of reachable gate blocks

### Trigger and purpose

G2 exhibited a width-stable approximately `O(h^2)` local defect on sampled
reachable states.  G3 asks whether iterating the same autonomous block gives
the corresponding `O(h)` compact-time error, or whether transverse
instability amplifies the local defects as width grows.

### Frozen implementation

- The exact same finite-width model, activation family, tied sources, and
  frozen-input block as G2.
- Compare dense RK4 reference flow with iterated blocks on `[0,0.5]`.
- Primary activations `alpha in {0,0.2}` and mesh sizes
  `h in {0.02,0.01,0.005}`; pure arctangent is the principal target and the
  positive slope is a transport control.
- Widths `n in {128,256,512,1024}`, four seeds as resources permit.
- Reference RK4 step `2^-11`; repeat selected widths with `2^-12` or float64
  if precision affects the learned-matrix statistic.
- Record errors at `t in {0.25,0.5}` using coupled initial data.  No clipping
  or source resampling is allowed.

### Recorded statistics and decisions

Record the G2 state, field, predictor, kernel, maximum-coordinate, and
moment-ratio statistics, now as compact-time errors.  Fit log--log global
error slopes in `h`.

- A width-stable slope near one is compatible with stable accumulation of
  the observed local defect and promotes the reachable-tangent program.
- A slope strictly above zero but below one motivates a weaker Osgood/Hölder
  global certificate if it is stable in width.
- Growth of `error/h^gamma` with width for every positive apparent `gamma`,
  or failure of errors to decrease with `h`, is a kill signal for this block
  as a compact-time approximation.
- A positive result is empirical support only.  It does not supply the
  annealed tangent estimate, source-limit theorem, or restart proof.

## Probe C1: marked-column cavity and tangent scaling

### Decision question

Does replacing one standardized column of the persistent top source in the
pure-arctangent, one-sample, three-hidden-layer flow create an order-one
effect only in the directly marked transpose coordinate, while its effect on
bulk fields is of normalized order `n^{-1/2}` through feature time `0.5`?
This is the first quantitative premise needed by a leave-one-column cavity
expansion.  It does not test forest summability or convergence of the full
network.

### Competing hypotheses

- **Cavity scaling (`H1`).**  For a fixed marked column `j`, replacing
  `g[:,j]=sqrt(n)*Gamma_2[:,j]` by an independent standard Gaussian column
  gives `Delta r_2[j]=O_P(1)`, while normalized bulk differences in
  `x_2,z_3,b_3,u` and the unmarked part of `r_2` are `O_P(n^{-1/2})` on the
  tested compact interval.  The full `G_2` operator difference is allowed to
  remain order one because it contains the deliberately replaced source
  column; the operator difference of the learned displacement
  `G_2(t)-Gamma_2`, and that of `G_1(t)-Gamma_1`, should instead be
  `O_P(n^{-1/2})`.
- **Adaptive amplification (`H0`).**  Feedback through the tied transpose
  turns a single-column perturbation into a bulk effect larger than
  `n^{-1/2}`, or makes the marked response grow with width, by either test
  time.
- **Third outcome.**  Strong cancellations make the marked effect vanish,
  or trial variation/resolution prevents either scaling from being
  distinguished.  This is inconclusive for the cavity mechanism.

### Mechanism-preserving testbed

Use exactly the frozen model `(F)` in `PROGRAM_CONTRACT.md` at hidden depth
three with `phi=arctan`, iid standard Gaussian `A(0),u(0)`, and two persistent
iid `N(0,1/n)` matrices.  Column zero of `Gamma_2` is marked.  A coupled copy
replaces only that column by an independently sampled column; every other
seed is bitwise shared.  Both copies are integrated by the same RK4 mesh,
without clipping, source refreshment, independent transpose copies, or loss
time-change.  Measurements are made at `t in {0,0.25,0.5}`.

### Primary perturbation metrics

Widths are `n in {128,256,512,1024}` with four independent coupled trials.
The primary mesh is at most `2^-10`.  For each time record:

1. `|Delta r_2[j]|` and its normalization by
   `||g'_j-g_j||_2/sqrt(n)`;
2. normalized Euclidean differences `||Delta v||_n` for
   `x_2,z_3,b_3,u,A` and for `r_2` after deleting coordinate `j`;
3. predictor and raw-kernel differences;
4. ordinary operator norms and `||.||_F/sqrt(n)` for the full matrix
   differences, and separately for the learned displacements
   `G_l(t)-Gamma_l` in the two coupled systems.

The primary width summary is the log--log slope of the across-trial RMS for
each metric, using all four widths.  Because four trials do not support a
sharp asymptotic confidence interval, slopes are descriptive and all raw
trial values are retained.

### JVP cross-check

Where memory and runtime permit, compute forward-mode Jacobian--vector
products with respect to the standardized marked column, using independent
Rademacher directions.  Pooling directions and trials, the RMS directional
derivative of scalar `r_2[j]` estimates
`||nabla_{g[:,j]} r_2[j]||_2`; the RMS normalized output tangent estimates
`||J_v||_F/sqrt(n)` for vector fields.  Record the same vector fields and
the learned matrix displacements.  At least one direction in each of four
trials is required for the primary JVP width grid; extra directions are
allowed only up to the frozen budget below.  A small-width direct
`torch.func.jvp` comparison is required if a hand-coded tangent-linear RK4
is used for the production grid.

### Pass, fail, and inconclusive thresholds

At both positive test times:

- **Pass as empirical compatibility:** the marked-response RMS slope lies
  in `[-0.25,0.25]`; the slopes of the primary bulk differences
  `x_2,z_3,b_3,u` are all in `[-0.8,-0.2]`; no one of those RMS values at
  width `1024` exceeds its width-`128` value; and the corresponding JVP
  marked/bulk slopes, if available, have the same signs and differ from the
  replacement slopes by at most `0.35`.  Learned-displacement operator
  slopes are reported as a secondary check, not allowed to rescue a failed
  field metric.
- **Fail for this cavity hypothesis:** after numerical controls pass, the
  marked-response slope exceeds `0.25`, or any primary bulk slope exceeds
  `-0.2` with width-`1024` RMS at least `1.25` times its width-`128` RMS.
- **Inconclusive:** any primary slope falls between the pass and fail rules,
  trial-to-trial sign cancellation dominates an RMS estimate, JVP and
  replacement scaling disagree beyond `0.35`, or a numerical validity gate
  fails.

The exact `t=0` identities are sanity checks, not independent evidence:
`Delta x_2=Delta u=0`, the full `G_2` operator perturbation is order one,
and only the marked coordinate has a direct transpose-query perturbation.

### Numerical validity, replication, and stopping

- Primary runs use float32 CUDA RK4 with step `2^-10` or finer.
- Repeat trials `0,1` at widths `128,512,1024` with step `2^-11`.  For every
  primary metric, the refinement discrepancy must be below `5%` of the
  across-trial RMS or absolute `2e-6`, whichever is larger.
- Repeat trial zero at widths `128,512` in float64 at steps `2^-10` and
  `2^-11`; qualitative width direction and all non-negligible metrics must
  agree to `5%` or absolute `2e-9`.
- Reject any run with a nonfinite state, normalized state norm above `100`,
  or an RK4 common-seed coupling mismatch at `t=0` outside the exact
  identities above.
- Hard cap: four primary trials, two JVP directions per trial, six refined
  float32 pairs, and four float64 pairs.  If GPU access is unavailable, the
  same frozen design may be run on CPU with no enlargement.  Computation
  stops after these controls; no post-hoc width, time, or seed search is
  authorized.

### Claim-level consequence

A pass promotes only the finite-time, tested-ensemble marked-column scaling
from open to empirically supported.  It does not prove an annealed cavity
lemma, a zero-defect forest estimate, uniform integrability, or an
interchange of response depth and width.  A fail rejects the marked-column
cavity premise in this form but does not reject the depth-three limit.

## C2 — Response-weighted bulk JVP occupation

This section was locked on 2026-08-24, before implementation and before
inspection of local helpers or prior experiment outputs.  The verbatim
standalone lock is `C2_PREREGISTRATION_LOCK.md`; this section records the same
normative design.  It is an empirical finite-width audit only, and no outcome
may be stated as proving or disproving an infinite-width theorem.

### Decision question and exact model

For the exact depth-three flow, test whether the response-weighted energy of
an unmarked layer-two full-trajectory JVP remains width-stable through time
`0.5`, rather than aligning increasingly with rare large values of `|r2|`.
All vectors have length `n`, both persistent matrices are `n x n`, and
`<a,b>_n = n^{-1} sum_i a_i b_i`.  Independently at time zero,
`u_i,A_i ~ N(0,1)` and each entry of `G1,G2` is `N(0,1/n)`.  The same
realized matrix is reused under transpose.  With `phi(s)=atan(s)`, the model
is exactly

```
z1=u, x1=phi(u), z2=G1 x1, x2=phi(z2), z3=G2 x2, x3=phi(z3),
b3=A phi'(z3), r2=G2^T b3, b2=phi'(z2) r2,
r1=G1^T b2, b1=phi'(u) r1,
A'=x3, G2'=b3 x2^T/n, G1'=b2 x1^T/n, u'=b1.
```

No sign, scaling, distribution, transpose, architecture, or horizon may be
altered after the lock.

### Marked perturbation and relevant response fields

Fix the marked column `j=0`.  Draw an independent `h ~ N(0,I_n)` and set
only `Delta G2(0)[:,j] = h/||h||_2`; all other initial tangent components
are zero.  The actual marked-column direction has Euclidean norm one, or
equivalently `<|sqrt(n) Delta G2[:,j]|^2>_n=1`.  Evolve the tangent jointly
with all primal variables by differentiating the complete ODE at every RK4
stage.  Frozen-state and endpoint-only derivatives are forbidden.

Delete coordinate `j` to obtain the bulk `B={1,...,n-1}`.  The joint primary
responses are

```
V_r[k] = D r2[k](t)[Delta G2(0)],
V_b[k] = D b2[k](t)[Delta G2(0)],       k in B.
```

`V_r` is the principal field because the weight is a function of the same
causal back-propagated field `r2`.  `V_b` checks the gated layer-two field
that drives `G1'`.  JVPs of `z2` and `x2` are secondary propagation
diagnostics only; their exact time-zero zeros cannot rescue a primary fail.

### Fixed grid, replication, and controls

- Widths are `128,256,512,1024`; checkpoints are `0,0.25,0.5`.
- The main ensemble has 48 independent model/direction seeds per width,
  rooted at seed `20260824`.  Replicates `0:24` and `24:48` are fixed
  confirmation halves.
- Main integration is float32 CUDA classical RK4 with `dt=1/64`.  Metric
  reductions and exponentials are evaluated in float64 without clipping.
- Mesh controls rerun the first eight seeds at widths `256,1024` with
  float32 CUDA RK4 at `dt=1/128`.
- Precision controls rerun those same canonical variates and directions in
  float64 CUDA at `dt=1/64` for widths `256,1024`.
- Tangent validation uses the first four width-128 seeds in float64 and
  central differences of the full integrated trajectory at perturbation
  sizes `2^-7` and `2^-9`.
- There is no post-result seed, width, time, lambda, or solver search.  The
  grid and controls above are the terminal computational stop.

### Locked weights, normalization, and controls

Use `lambda in {0,0.05,0.10,0.20}`.  For either primary field define the
literal, unweighted-normalization observable

```
M_V(lambda;n,t)
  = n < exp(lambda r2[k]^2) |V[k]|^2 1{k in B} >_n
  = sum_{k in B} exp(lambda r2[k]^2) |V[k]|^2.
```

It is never divided by the weight sum, ESS, or `M_V(0)`.  Separately define
`wbar_B=(n-1)^-1 sum_B exp(lambda r2^2)` and the factorization diagnostic
`F_V=M_V(lambda)/(M_V(0) wbar_B)`.  Thirty-two independently seeded bulk
weight permutations per instance give shuffled `M` and `F`; these preserve
both marginals while destroying coordinate alignment.  The pooled log ratio
of true to mean-shuffled `M` is the alignment contrast.  A rank-aligned
weight/response pairing is a diagnostic positive control only.

For `c_k=exp(lambda r2[k]^2)|V[k]|^2`, record the exact sum, maximum
contribution fraction, and

```
rESS = (sum c_k)^2 / ((n-1) sum c_k^2).
```

Also record unweighted-response and weighted-contribution fractions in the
largest 5% and, at widths at least 256, largest 1% of coordinates ranked by
`|r2|`, as well as weight-only ESS/max share.  Report mean, median, 10/90%
quantiles, and both fixed replication halves.

### Fixed statistical discriminator

For every `(V,t,lambda>0)` primary cell, fit `beta` by OLS of
`log(mean_seed M_V)` on `log(n)` over all four widths.  Let
`a_n=log[(sum_seed M)/(sum_seed mean_shuffle M)]` and fit its width slope
`alpha` on `log(n)`.  Use 5,000 within-width seed bootstraps with root seed
`20260825`; familywise 95% one-sided bounds over all 18 cells use a
maximum-deviation bootstrap statistic.  All raw instance summaries and
permutation seeds are retained.

An **empirical pass** requires all numerical gates and, simultaneously over
both primary fields, all checkpoints, and all three positive lambdas:

- familywise upper `beta <= 0.20`;
- familywise upper `alpha <= 0.10` and familywise upper `a_1024 <= 0.15`;
- at `lambda=0.20,n=1024`, median contribution `rESS >= 0.05` and median
  maximum contribution share `<=0.10`;
- neither fixed half has a point estimate beyond a fail threshold.

An **empirical fail** requires all numerical gates and a replicated adverse
pattern at two adjacent lambdas for the same field/time: either a cellwise
95% lower bound `beta > 0.30`, or both lower `alpha > 0.15` and lower
`a_1024 > 0.30`.  Both fixed halves must have the same sign and relevant
point estimate beyond threshold.  Alternatively, median maximum contribution
share above `0.20` at `lambda=0.20` that grows by at least a factor `1.5`
from width 512 to 1024 in both halves is a replicated rare-dominance fail.

Every other valid result is **inconclusive**, including disagreement between
`r2` and `b2`.  Exact factorization is reported separately as compatible
only when the familywise true-versus-shuffle log-contrast interval contains
zero and lies within `[-0.15,0.15]`; it does not override the occupation
verdict.

### Numerical-validity gates

- CUDA is required for all announced production runs.  Any nonfinite primal,
  tangent, contribution, or unclipped exponential, or any absolute
  state/tangent entry above `1e6`, invalidates interpretation.
- At width 128 and time 0.5, fine central-difference relative l2 error for
  each bulk `r2,b2,z2,x2` JVP is at most `2e-4` and no more than `1.2` times
  its coarse error, with a `1e-12` absolute floor only for that ratio.
- Every paired primary-field/checkpoint mesh JVP differs by at most `5e-4`
  in relative l2, and every locked-lambda `M` differs by at most `0.5%`.
- Every paired primary-field/checkpoint float32/float64 JVP differs by at
  most `1e-3` in relative l2, and every locked-lambda `M` differs by at most
  `1%`.  Initial canonical normal variates are shared before casting.
- At least 46 of 48 main trajectories per width must be valid.  A failed
  validity gate makes the scientific verdict inconclusive, and no
  unregistered repair run is allowed.

### Claim-level consequence

A pass supplies only finite-width empirical support through time `0.5` for
this response-weighted occupation/factorization mechanism in the exact
witness.  A fail disfavors this mechanism/witness on the fixed grid but does
not refute a broader closure or existence claim.  An inconclusive result
leaves the premise open.  The rank control, secondary propagation fields,
and unregistered visual trends are descriptive only.

### C2 post-lock, pre-run analytic caveat (not a gate change)

After C2 was frozen but before any C2 execution, an analytic correction
showed that at finite `n,t=0`, conditional on `u,G1,G2`, `r2_i` is Gaussian
in `A` with variance
`S_i=sum_m G2[m,i]^2 phi'(z3_m)^2`, whose support is unbounded.  Therefore
`E exp(lambda r2_i^2)=infinity` for every `lambda>0`.  This proof-level fact
already falsifies any annealed or uniform square-exponential moment premise.
The square-exponential grid and decision rules stay locked solely to avoid a
post-hoc pivot.  The run can characterize only the deliberately finite,
typical-sample diagnostic and cannot support uniform integrability or a
theorem, even if its preregistered finite-grid label is “pass.”
