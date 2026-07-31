# Fixed-\(P=5\) operator–Liouville PDE: preregistered generalization study

**Date:** 2026-07-23  
**Status:** final processed-evidence report  
**Primary conclusion:** descriptively broad transfer; formally
**boundary or unresolved**

## 1. Executive conclusion

The fixed \(P=5\) PDE is not behaving like a closure tuned to one particular
label vector or one activation. Without fitting, retuning, changing \(P\), or
reading a dense-network trajectory, it tracked 14 preregistered configurations
covering:

- four label changes, including a new sign pattern, a concentrated target, and
  doubled label amplitude;
- two new input geometries, including pairwise correlation \(0.85\);
- \(m=2,3,4,5\) samples while keeping the ambient dimension and \(P\) fixed;
- tanh, normalized erf, and normalized arctangent activations;
- two crossed stress cases.

Across all 14 cases, the observed full-curve normalized errors were:

| metric | median | maximum | worst case |
|---|---:|---:|---|
| all-depth Gram-increment curve | 1.71% | 4.14% | \(m=4\) |
| output-increment curve | 1.46% | 1.83% | \(m=5\) |
| loss curve | 0.63% | 1.97% | \(m=5\) |

All 14 references exhibited active, nonlazy feature learning. The ratio of PDE
feature motion to dense-network feature motion stayed between \(0.977\) and
\(1.023\). This rules out a trivial match obtained by predicting nearly static
features.

The label tests are the cleanest anti-fine-tuning result. All four passed every
PDE numerical gate and both plateau windows. Their maximum observed errors
were 1.56% for Gram motion, 1.47% for outputs, and 1.41% for loss. Doubling the
original labels was the most accurate case: 0.95%, 0.74%, and 0.70%,
respectively. Both alternative activations were also accurate and numerically
resolved.

The strongest honest verdict is nevertheless not “universal pass.” The
preregistered decision demanded one-sided 95% bounds simultaneous over all 14
cases and all three metrics. The resulting joint bootstrap critical increment
was 5.94%, already larger than the 5% equivalence margin. Consequently, no
individual case could satisfy the frozen strong-transfer rule, even though
every observed error was below 5%. Six harder cases also failed a PDE
quadrature/depth-resolution gate, and four did not pass both strict plateau
windows by \(t=32\).

Therefore:

\[
\boxed{\text{The evidence strongly rejects “tuned only to the original data,”
but does not certify uniform transfer over the whole proposed class.}}
\]

No material counterexample was found. In particular, no simultaneous lower
confidence bound exceeded 10%, every feature-motion ratio remained inside
\([0.5,2]\), and the PDE and dense reference never disagreed about whether a
case had plateaued.

## 2. What was held fixed

The experiment used the smallest previously successful complete linear
Hermite closure in ambient dimension \(d=3\):

\[
P=d+2=5,\qquad
\{\phi_j\}_{j=1}^{5}=\{1,B_1,B_2,B_3,a/A\}.
\]

Every case used the same:

| component | fixed value |
|---|---|
| Galerkin basis | complete degree-one Hermite, \(P=5\) |
| depth discretization | \(N=16\) |
| immutable-label cubature | tensor Gauss–Hermite, order 3, \(M=81\) |
| row-characteristic cubature | scrambled Sobol, \(R=128\) |
| primary cubature seed | 20260723 |
| integrator | RK4 |
| time step / saved step | \(0.02/0.04\) |
| horizon | \(t=32\) |
| physical parameters | \(\sigma_w=0.65,\ A=\gamma=1\) |

Most importantly, \(P\) did not grow with \(m\). The same five-dimensional row
coefficient law was used for \(m=2,3,4,5\). There are no case-specific fitted
coefficients.

The PDE stage, including the independent quadrature scramble and all
resolution diagnostics, was completed and content-hash sealed before the
dense-reference stage was admitted.

## 3. Model and finite PDE

### 3.1 Dense reference

For samples \(u_r\in\mathbb R^3\), the canonical fully dense residual network
is

\[
h_r^0=Bu_r,\qquad
z_r^\ell=W_\ell h_r^\ell,\qquad
h_r^{\ell+1}
=h_r^\ell+\frac{\gamma}{L}\sigma(z_r^\ell),
\]

\[
f_r=\frac1n a^\top h_r^L,\qquad
\mathcal L=\frac12\sum_{r=1}^{m}(f_r-y_r)^2.
\]

Initialization and ordinary Euclidean \(\mu\)P multipliers are

\[
(W_\ell)_{ij}\sim N(0,\sigma_w^2/n),\quad
B_{ij}\sim N(0,1),\quad
a_i\sim N(0,A^2),
\]

\[
\eta_{W_\ell}=L,\qquad \eta_B=\eta_a=n.
\]

The intended asymptotic order remains width first and depth second:

\[
n\to\infty\text{ at fixed }L,\qquad L\to\infty\text{ afterward}.
\]

The present references use finite \(n,L\), so they test consistency with this
limit rather than proving it.

### 3.2 Width-independent operator projection

Let the immutable neuron label be

\[
\theta=(B_i(0),a_i(0)/A)\sim N(0,I_4).
\]

After the width limit, a dense Gaussian row operator is projected onto the
five Hermite functions. If \(v(\theta)\) is a slow neuron field,

\[
(W_P^0v)(\theta,\varepsilon)
=\sigma_w\sum_{j=1}^{5}
\varepsilon_j\langle\phi_j,v\rangle,
\qquad \varepsilon\sim N(0,I_5).
\]

The same row coefficients are reused in the adjoint action. Thus forward and
transpose propagation satisfy an exact finite-\(P\) pairing; the solver does
not introduce an independent backward Gaussian and contains no hidden
\(n\times n\) matrix.

### 3.3 Conditional Liouville equation

For depth \(s\), label \(\theta\), and training time \(t\), let
\(\rho_{s,t}^{\theta}\) be the conditional law of the current row coefficient
\(w\in\mathbb R^5\). Define

\[
H_{jr}(s,t)=\int\phi_j(\theta)h_r(s,\theta,t)\,d\mu(\theta),
\]

\[
z_r(s,\theta,w,t)=\sum_{j=1}^{5}w_jH_{jr}(s,t),\qquad
\beta_r=\sigma'(z_r)p_r.
\]

With residual \(e=f-y\), the characteristic velocity is

\[
V_j(s,\theta,w,t)
=-\gamma\sum_{q=1}^{m}e_q(t)\,
\beta_q(s,\theta,w,t)H_{jq}(s,t).
\]

The actual simulated PDE is

\[
\boxed{
\partial_t\rho_{s,t}^{\theta}
+\nabla_w\!\cdot(\rho_{s,t}^{\theta}V)=0.
}
\]

It is coupled to the forward and adjoint depth equations

\[
\partial_sh_r
=\gamma\int\sigma(z_r)\,d\rho_{s,t}^{\theta}(w),
\]

\[
-\partial_sp_r
=\gamma\sum_{j=1}^{5}\phi_j(\theta)
\int w_j\beta_r(s,\theta',w,t)\,
d\mu(\theta')\,d\rho_{s,t}^{\theta'}(w),
\]

and to the input/readout characteristics

\[
\dot B(\theta,t)
=-\sum_qe_qp_q(0,\theta,t)u_q^\top,\qquad
\dot a(\theta,t)
=-\sum_qe_qh_q(1,\theta,t).
\]

The prediction is

\[
f_r(t)=\int a(\theta,t)h_r(1,\theta,t)\,d\mu(\theta).
\]

The state and velocity are autonomous, restartable, and independent of dense
network width. The finite-\(P\) solver passes the exact gradient-flow identity

\[
\dot f=-\Theta_P(f-y),\qquad \Theta_P\succeq0,
\]

to numerical precision in every case.

## 4. Sparse, high-information experimental matrix

The matrix was chosen to isolate mechanisms before adding crossed stresses.

| ID | change from the anchor |
|---|---|
| B0 | orthogonal inputs, labels \((0.8,-0.55,0.35)\), tanh |
| Y1 | label perturbation of Euclidean norm exactly 0.05 |
| Y2 | equal positive labels at the original label norm |
| Y3 | one-coordinate label at the original label norm |
| Y4 | twice the original labels |
| X1 | generic asymmetric unit-vector geometry |
| X2 | equicorrelated input geometry, pairwise correlation \(0.85\) |
| M2 | two orthogonal samples in the same ambient dimension |
| M4 | four samples, adding the normalized all-ones direction |
| M5 | five samples, adding two nonorthogonal directions |
| A1 | normalized \(\operatorname{erf}(\sqrt\pi z/2)\) |
| A2 | normalized \((2/\pi)\arctan(\pi z/2)\) |
| I1 | correlated inputs crossed with doubled labels |
| I2 | \(m=5\) crossed with normalized erf |

Tanh, normalized erf, and normalized arctangent are smooth, bounded, odd, and
slope-matched at the origin: \(\sigma'(0)=1\). The two alternatives are
extension tests; they do not silently broaden the already stated narrow tanh
theorem claim.

## 5. Reference and statistical protocol

Every case first received a fresh \(n=128,L=32\), 32-member dense ensemble in
two fixed 16-seed blocks. Eight cases declared in advance used a held-out
\(n=256,L=32\), 24-member ensemble in two fixed 12-seed blocks for the final
comparison. \(I1\) and \(I2\) also received diagnostic
\(n=256,L=64\), 16-member ensembles; those were never substituted into the
primary result.

The primary normalized errors are:

\[
E_G=
\frac{\sup_{t,s}\|\Delta G_{\rm PDE}(s,t)
-\Delta G_{\rm dense}(s,t)\|_F}
{\max(\sup\|\Delta G_{\rm PDE}\|_F,
\sup\|\Delta G_{\rm dense}\|_F,0.05)},
\]

\[
E_f=
\frac{\sup_t\|\Delta f_{\rm PDE}(t)
-\Delta f_{\rm dense}(t)\|_2}
{\max(\|y\|_2,\sup\|\Delta f_{\rm PDE}\|_2,
\sup\|\Delta f_{\rm dense}\|_2,0.1)},
\]

\[
E_{\mathcal L}=
\frac{\sup_t|\mathcal L_{\rm PDE}(t)
-\mathcal L_{\rm dense\ mean}(t)|}
{\max(\mathcal L_{\rm PDE}(0),
\mathcal L_{\rm dense\ mean}(0),0.1)}.
\]

The bootstrap resamples whole dense-network trajectories within each
preregistered block. The same resampled indices are shared across cases in a
tier, preserving cross-case dependence. Two thousand replicates with fixed
seed 2026072301 produce one-sided 95% bounds from a maximum over all 14 cases
and all three metrics.

The frozen decisions are:

- **strong transfer:** every judged joint UCB \(\le5\%\), plus numerical and
  plateau gates;
- **near-original Gram accuracy:** Gram-only simultaneous UCB \(\le2.5\%\);
- **material counterexample:** a joint LCB \(>10\%\), active feature-motion
  ratio outside \([0.5,2]\), or PDE/dense plateau-status mismatch;
- otherwise: **boundary or unresolved**.

This deliberately severe rule prevents a favorable average from hiding a
single difficult direction.

## 6. Primary results

All values below are normalized full-curve errors. “Joint UCB max” is the
largest of the three casewise simultaneous 95% UCBs.

| case | final tier | Gram | output | loss | joint UCB max | PDE numerics | two-window plateau |
|---|---|---:|---:|---:|---:|---|---|
| B0 | \(128/32/32\) | 1.81% | 1.34% | 0.39% | 7.75% | pass | pass |
| Y1 | \(256/32/24\) | 1.26% | 1.47% | 1.41% | 7.41% | pass | pass |
| Y2 | \(128/32/32\) | 1.56% | 1.33% | 0.95% | 7.50% | pass | pass |
| Y3 | \(256/32/24\) | 1.24% | 1.47% | 0.95% | 7.41% | pass | pass |
| Y4 | \(256/32/24\) | 0.95% | 0.74% | 0.70% | 6.89% | pass | pass |
| X1 | \(128/32/32\) | 2.46% | 1.53% | 0.56% | 8.40% | unresolved | pass |
| X2 | \(256/32/24\) | 2.55% | 1.59% | 0.46% | 8.49% | unresolved | latest window only |
| M2 | \(128/32/32\) | 1.62% | 1.18% | 0.46% | 7.56% | pass | pass |
| M4 | \(128/32/32\) | 4.14% | 1.51% | 0.55% | 10.08% | unresolved | not flat by \(32\) |
| M5 | \(256/32/24\) | 3.11% | 1.83% | 1.97% | 9.05% | unresolved | not flat by \(32\) |
| A1 | \(256/32/24\) | 1.34% | 1.46% | 1.38% | 7.40% | pass | pass |
| A2 | \(128/32/32\) | 1.52% | 1.31% | 0.31% | 7.46% | pass | pass |
| I1 | \(256/32/24\) | 2.10% | 1.04% | 0.44% | 8.04% | unresolved | pass |
| I2 | \(256/32/24\) | 2.44% | 1.68% | 1.96% | 8.38% | unresolved | not flat by \(32\) |

### 6.1 Label robustness

Changing the labels did not degrade the closure. The four label cases have a
median observed Gram error of 1.25%; the largest is 1.56%. This includes two
changes far outside the original small neighborhood:

- a completely different all-positive direction;
- a doubled-amplitude target with four times the initial squared scale.

The doubled-label case is more accurate than the anchor. Since labels enter
only through \(e=f-y\), while the state representation and quadrature remain
unchanged, this is direct evidence that the solver was not calibrated to the
original target vector.

### 6.2 Activation robustness

Normalized erf and arctangent remain accurate with the same basis and
resolution. Their observed Gram errors are 1.34% and 1.52%. Both pass the
independent cubature-scramble and exact gradient-identity gates, and both
systems plateau in both windows.

This supports an activation-class extension, plausibly to a bounded smooth
odd slope-normalized class. It does not establish that extension uniformly;
only three activations were tested.

### 6.3 Sample count

\(m=2\) transfers cleanly. \(m=4\) and \(m=5\) still give close output and loss
curves, but their Gram errors rise to 4.14% and 3.11%. They also expose
quadrature sensitivity, and neither is flat enough by \(t=32\) under the
strict preregistered criterion. Thus the data support useful fixed-\(P\)
prediction across \(m=2\) through 5, but do not close a uniform \(m=2,\ldots,5\)
claim.

### 6.4 Input geometry and interactions

Both new geometries have observed Gram error around 2.5% and output error
around 1.5%. The correlated geometry settles later and fails the first
plateau window, although both PDE and dense reference pass the final
\(16\)-to-\(32\) window.

The two crossed stresses remain close descriptively. \(I1\) reaches plateau
and has only 1.04% output error. \(I2\), the \(m=5\)-erf cross, remains slowly
evolving at \(t=32\). Both are numerically unresolved under the frozen
quadrature/depth gates.

## 7. Global-time and plateau behavior

Ten cases pass every PDE and dense threshold on both \(8\)-to-\(16\) and
\(16\)-to-\(32\):

\[
\{B0,Y1,Y2,Y3,Y4,X1,M2,A1,A2,I1\}.
\]

\(X2\) fails only the earlier window and both systems pass the final window.
\(M4\), \(M5\), and \(I2\) remain measurably active through \(t=32\).

There are zero PDE/dense plateau-status mismatches. This is useful qualitative
evidence: the PDE does not predict a false early plateau or miss a dense
plateau. A common failure to plateau is nevertheless not positive
plateau evidence, so the four cases remain unresolved under the frozen rule.

The full-curve metrics include every recorded time from initialization to
\(t=32\); they are not terminal-only or local-Taylor comparisons.

## 8. Numerical-resolution audit

Every case passes:

- finite-state checks;
- the exact loss-dissipation identity to at worst
  \(1.33\times10^{-15}\);
- positive-semidefinite tangent-kernel checks.

Eight cases pass all applicable resolution gates:

\[
\{B0,Y1,Y2,Y3,Y4,M2,A1,A2\}.
\]

Six trigger the preregistered unresolved rule:

\[
\{X1,X2,M4,M5,I1,I2\}.
\]

The trigger is primarily a change under the independent Sobol scramble larger
than 1% of feature motion. \(I1\) and \(I2\) also exceed the fixed
Gauss–Hermite/QMC or \(N=16/32\) comparison thresholds, while their
\(dt=0.02/0.01\) comparisons pass.

The mandated \(R=256\) runs are diagnostic only and cannot erase a trigger.
Their differences from \(R=128\) are:

| case | Gram difference | output difference |
|---|---:|---:|
| X1 | 0.44% | 0.05% |
| X2 | 0.50% | 0.08% |
| M4 | 1.28% | 0.25% |
| M5 | 1.23% | 0.19% |
| I1 | 0.31% | 0.08% |
| I2 | 1.19% | 0.19% |

These magnitudes explain why the hardest Gram comparisons cannot yet be
called resolution-converged. They do not reveal a catastrophic discrepancy,
but post-hoc use of \(R=256\) as a “better answer” was prohibited.

## 9. Statistical interpretation

The observed results and the formal decision differ because the uncertainty
correction is global:

\[
c_{0.95}^{\rm upper}=0.0594006,\qquad
c_{0.95}^{\rm lower}=0.0152036.
\]

Adding the upper critical value to even a zero observed error would exceed
the 5% equivalence margin. Thus the study is underpowered for its deliberately
strong all-cases/all-metrics certification rule. The Gram-only critical value
is 2.13%, so no case meets the separate 2.5% “near-original” UCB rule either.

This does **not** turn the observed 1–4% curve gaps into 6–10% estimated
errors. It means the available finite-network ensemble sizes do not exclude
such errors simultaneously at the declared confidence level.

Conversely, the largest UCB, 10.08% for \(M4\) Gram motion, is not a material
counterexample. The counterexample rule uses a lower bound above 10%;
\(M4\)'s lower bound is only 2.62%. No case meets any frozen counterexample
condition.

Additional interpretation guardrails are:

- Gram and output errors compare learned increments, intentionally removing
  initialization offsets. Absolute-state gaps are retained as secondary
  outputs but are not the primary equivalence statistic.
- The loss comparison uses the loss of the ensemble-mean predictor, not the
  mean loss of individual finite networks.
- Bootstrap bounds quantify finite-network seed uncertainty under the two
  fixed blocks. They do not include PDE truncation/cubature bias or finite
  width/depth bias.
- The 14 cases are fixed synthetic stresses, not random draws from a
  population of datasets. Y1 is one direction at radius 0.05, not a uniform
  neighborhood theorem.
- Most numerical comparisons are evaluated on \(t\le8\), while the primary
  curves extend to \(t=32\).
- The plateau rule is a finite-horizon operational test. Matching failures do
  not prove a common infinite-time limit, and the dense memberwise check is a
  95th percentile rather than a guarantee for every seed.

## 10. What this says about the conjecture

The experiment supports a broader empirical conjecture than the single
original dataset:

> For fixed ambient dimension and compact nondegenerate sets of finite
> datasets, labels, and smooth bounded odd slope-normalized activations, a
> width-independent operator–Liouville Galerkin closure can approximate dense
> \(\mu\)P output, loss, and Gram-evolution curves uniformly on finite training
> horizons, with a closure order chosen for the class and target accuracy
> rather than fitted to each dataset.

The fixed \(P=5\) evidence is especially persuasive for labels, standalone
activation changes, and \(m=2\). It is suggestive but unresolved for strongly
correlated inputs, \(m=4,5\), and crossed stresses.

Only B0 and the exact-radius Y1 perturbation directly test the current narrow
tanh conjecture. Every other case is extension evidence. This study does not
establish:

1. the ordered \(n\to\infty\), then \(L\to\infty\) identification;
2. convergence as \(P\to\infty\);
3. arbitrary-accuracy approximation;
4. uniformity over all \(m\), all input degeneracies, or an infinite
   activation class.

It also does not repair the earlier nonmonotone \(P=5,15,35\) result. The
correct interpretation is that one very small PDE is surprisingly portable,
not that the tested Hermite hierarchy has been proved convergent.

## 11. Integrity and anti-oracle audit

The completed release has:

- 32 frozen scientific source/protocol files with aggregate hash
  `421ae71793d558822da3ff8b16a40c4189fb118d30025cc9f08ca7d666a0fcab`;
- 56 sealed PDE-stage entries, including 55 numerical archives, PDE-stage seal
  `8389943369fc137cf5ff618c5a2b48273ac81db30176ba299737f5b6959e316a`;
- 46 sealed dense-reference archives, dense-stage seal
  `e5c5e3fd71f144b4b346a0cd8ea37185c4315bc514358a7fc0908ed367f9c390`;
- 2,000 deterministic bootstrap replicates;
- 50 passing source, algebra, provenance, metric, bootstrap, and structural
  tests;
- a read-only full-evidence verifier that passes.

The PDE source imports no dense-reference trajectory or code path. Dense
archives record the already frozen PDE seal. Case selection is metadata-based,
time grids must match exactly, seed blocks are fixed, and the held-out tier is
chosen before reference generation.

Two post-freeze compatibility amendments are disclosed and checksummed. One
provides a redundant first-block `seed_start` alias to a sealer with an eager
default-expression bug. The other registers the frozen analyzer module for
Python 3.12 and reconstructs redundant `m`, `d`, and `seed_ids` metadata from
the case registry, array shapes, exact stored seed vector, and fixed schedule.
Neither amendment changes a trajectory, observable, bootstrap draw, metric,
threshold, case, or tier. Full evidence verification passes after the
amendments.

## 12. Final assessment

The original ad-hoc concern is substantially weakened:

- the same smallest useful closure works for radically different labels;
- it works for two different smooth bounded activations;
- it remains accurate when sample count and input geometry change;
- it predicts active nonlazy Gram motion, not merely loss fitting;
- it tracks the whole transient and agrees qualitatively on plateau status;
- no case-specific fitting or reference-curve access occurs.

The remaining boundary is equally clear:

- the global simultaneous confidence rule is underpowered at the available
  ensemble sizes;
- six difficult cases are not PDE-resolution-certified;
- four cases fail the fixed two-window plateau requirement;
- higher-\(P\) convergence remains unestablished.

Accordingly, the scientifically defensible claim is:

> The \(P=5\) operator–Liouville PDE exhibits broad, nontrivial portability
> across labels, activations, input geometry, and \(m=2\) through \(5\), with
> observed global curve errors below 5% in every preregistered case. The study
> finds no material counterexample, but its frozen simultaneous-confidence,
> resolution, and plateau rules leave the full category-level claim
> unresolved.

That is considerably stronger evidence than a single-setup match, but it is
not a proof or a blanket certification.
