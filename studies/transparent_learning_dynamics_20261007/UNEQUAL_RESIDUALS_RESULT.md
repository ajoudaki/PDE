# Beyond one clock: ordered learning and passive nonlinear geometry

2026-10-07. Continuation of the user's experimental/mechanistic request.
Global accuracy proofs remain paused. This report records a bounded campaign,
not an all-data or full-trajectory approximation theorem. It extends, rather
than silently replaces, [the symmetric experiment](BEYOND_INITIALIZATION_RESULT.md).

## Headline

The full causal feature–response system survives two new tests: unequal labels,
and then unequal labels with correlated training inputs. A small initialized
cubic approximation exposes an additional mechanism—response to the **order**
of sample forces—but its passive prediction remains inaccurate. Adding this
one memory correction does not justify discarding evolving nonlinear features.

The most useful new explanation is an exact decomposition of passive learning.
Its departure from the geometric mixture of training predictions is built by
readout updates, learned middle-layer writes, and moving lower-layer features.
These contributions can be measured additively on one trajectory. An ablation
is different: other layers compensate when a channel is removed. Current
activation sensitivities determine which transported changes reach the passive
input, and their change during training makes a measurable contribution.

## 1. Common setup and evidence boundary

The network has two hidden tanh layers of width n and a zero initial readout:

\[
z_{1,a}=Av_a,\quad h_{1,a}=\tanh z_{1,a},\qquad
z_{2,a}=Wh_{1,a},\quad h_{2,a}=\tanh z_{2,a},\qquad
f_a=\frac1n w^\top h_{2,a}.
\]

Initially the entries of A are independent standard Gaussians, the entries of
W are independent Gaussians of variance 1/n, and A,W are independent. The
normalized inputs v are unit vectors; the book's inputs are x=√2 v. Only
samples 1 and 2 train. With deficits c_a=y_a−f_a, loss is
(c_1²+c_2²)/2 and block mobilities are (n,1,n). These match the existing
candidate and dense reference; no passive label enters a force.

Both new cases use y=(0.6,−0.3) and passive v_3=(2,1)/√5:

| Case | Training inputs | Passive input expressed in training inputs |
|---|---|---|
| A | v_1=(1,0), v_2=(0,1) | v_3=(2v_1+v_2)/√5 |
| B | v_1=(1,0), v_2=(0.6,0.8) | v_3=√5(v_1+v_2)/4 |

The original orthogonal example with labels (0.6,−0.6) supplies a separately
identified diagnostic control. These are exploratory amplitudes, **not**
certified instances of the original theorem's conservative small-label cap.
No accuracy statement for the general activation class follows from tanh tests.

The fixed horizon is [0,24], by which the training residuals are small. Dense
RK4 uses widths 512 and 1024, three seeds each, and step 0.1; seed 101 at width
1024 is refined to step 0.05 in both cases. The full causal population solver
uses 4096 particles and three seeds at Euler step 0.4. Dense Euler on that same
mesh supplies the primary comparison. Separate 1024-particle runs at steps
0.4 and 0.2 measure quadrature/time sensitivity. There are 26 dense and 16
causal runs in total, including controls, about 336.5 seconds summed numerical
wall time and a process high-water mark below 0.65 GiB. All numerical work was
single-threaded. The predeclared campaign is now closed.

Means and standard errors below describe these small ensembles; they are not
confidence intervals, asymptotic-rate estimates, or individual-run bounds.
The full candidate remains a joint-law history-state system with local
sensitivities. Its finite particle implementation is an adaptive empirical
approximation, not a collection of exactly independent Gaussian trajectories.

## 2. What the full causal system predicts beyond initialization

On the common Euler mesh, compare all three output curves by their largest
absolute discrepancy, first averaging over seeds within each model:

| Case | Largest causal-mean versus dense-mean output discrepancy | Mean pairwise dense-run discrepancy in the same norm |
|---|---:|---:|
| A: unequal labels, orthogonal inputs | 0.005174 | 0.013067 |
| B: unequal labels, correlated inputs | 0.005486 | 0.016889 |

The right column uses three dependent pairs from three dense draws; it is a
descriptive variability scale, not a lower confidence bound. Comparing a
population mean to dense means is weaker than certifying a predictor against
each dense realization.

The passive endpoints give a complementary, simpler view:

| Case | Dense Euler | Full causal Euler | Dense RK4 |
|---|---:|---:|---:|
| A | 0.482046 | 0.483418 | 0.482637 |
| B | 0.232941 | 0.234899 | 0.235321 |

The last column is the three-run step-0.1 RK4 mean, with its seed-101 refinement
checked separately. It must not be substituted into the matched-Euler error.
The per-run standard errors of the first two columns are, respectively,
(0.005268,0.000920) for A and (0.005427,0.000631) for B.

Across outputs, all current hidden-Gram changes, and signed order memory,
the measured mean discrepancies fall inside the predeclared diagnostic
envelope: three combined run standard errors, plus particle-size change and
dense-width change. The latter is estimated from the RK4 cohorts at the
comparison times, not from an unrun width-512 Euler cohort. This envelope is
not a confidence theorem and does not bound unknown systematic particle bias.

Reciprocal return remains important with correlated data. Removing it in case
B still fits the labels, but changes the learned geometry and passive output:

| Quantity at time 24, case B | Full causal | Reciprocal return removed |
|---|---:|---:|
| Change of lower training cross-Gram | −0.12933 | −0.06154 |
| Change of upper training cross-Gram | −0.20968 | −0.14489 |
| Passive prediction | 0.23490 | 0.20130 |
| Signed order memory | 0.06254 | 0.33585 |

Full uses three seeds; the control uses two. The control's largest final
training deficit is below 6×10⁻⁶. This does not show that reciprocal feedback
is needed for interpolation. It shows that interpolation does not determine
the hidden geometry or passive response, and that the return through the
same initialized map is a mechanism of those differences. The reciprocal-off
system is an intervention, not asserted to be another neural gradient flow.

## 3. A closed small approximation reveals ordered response—but does not solve passive prediction

For the orthogonal panel, let u_a=∫₀ᵗc_a(s)ds be each sample's accumulated
deficit. Keeping quadratic feature motion and cubic output response gives the
following autonomous four-state training approximation, initialized at zero:

\[
\dot u=y-f,\qquad
\dot f=
\begin{pmatrix}
\nu+2\lambda u_1^2+\mu u_2^2&\mu u_1u_2\\
\mu u_1u_2&\nu+\mu u_1^2+2\lambda u_2^2
\end{pmatrix}(y-f),
\]

where ν=0.2364504105, λ=0.0802460709, μ=0.1914828841 are **initial Gaussian
expectations**, not fitted trajectory coefficients. Their explicit integrals,
passive extension, and derivation are in
[ASYMMETRIC_RESPONSE_APPROXIMATION.md](ASYMMETRIC_RESPONSE_APPROXIMATION.md).
This approximation is not asserted for the nonorthogonal panel B.

The diagonal terms increase each sample's responsiveness as features move.
The off-diagonal term carries the signed cross-sample association: with the
opposite signs of u in this test, it is negative. Acting on opposite-signed
residuals, it helps the two predictions separate. Positive definiteness of
this approximate matrix is an algebraic fact, not proof of approximation
accuracy at the moderate tested labels.

The relevant order memory is

\[
\mathcal A(t)=\int_0^t[c_1(s)u_2(s)-c_2(s)u_1(s)]\,ds.
\]

It measures the ordering of hidden writes supplied by earlier readout writes;
it is not a second time variable. The same accumulated deficits can in general
come from different force orders. Importantly, leading same-time training
Grams can cancel this information, while two-time pairings retain it. For
example, writing the upper cross-Gram as
C²₁₂(t,s)=E[h₂,₁(t)h₂,₂(s)], its formal quadratic approximation is

\[
C^2_{12}(t,s)\simeq\frac\mu2\big[
u_1(t)u_2(t)+u_1(s)u_2(s)+\mathcal A(t)-\mathcal A(s)\big].
\]

At equal times its area contribution vanishes. The readout, however, pairs
current features with features written at earlier times, so that cancellation
does not generally remove its ordered response.

The precise obstruction to replacing f by a cubic function of u alone is
also explicit. For the natural radial formula
F_a(u)=νu_a+(2/3)(λu_a³+μu_a u_b²), b≠a, the displayed training approximation
satisfies

\[
\frac d{dt}[f-F(u)]
=\frac\mu3\begin{pmatrix}u_2\\-u_1\end{pmatrix}\dot{\mathcal A}.
\]

This is response transverse to the accumulated-deficit direction. It is not
captured by a single symmetric training clock. A six-state version evolving
(u_1,u_2,𝒜,f_1,f_2,f_3), or an equivalent five-state reconstruction using two
third-order histories, closes the passive cubic response as well. All its
coefficients are computed at initialization. No completed trajectory is used.

There is an important perturbative qualification: for fixed small labels and
orthogonal inputs, both leading residuals initially share the same exponential
clock. Then 𝒜 is fourth order in the common label scale, and its correction to
the cubic radial output starts at fifth order. Unequal labels do not by
themselves make the area a leading quadratic effect on that fixed-label path.
The ordered closure retains only some of those higher-order effects; it is
not a complete fifth-order approximation.

### What the new experiment says about this reduction

The continuous dense mean area in case A develops as follows:

| Time | 0 | 2 | 4 | 8 | 24 |
|---|---:|---:|---:|---:|---:|
| A | 0 | −0.00754 | −0.07753 | −0.22023 | −0.25991 |
| B | 0 | 0.02828 | 0.08293 | 0.04925 | 0.02863 |

Case B even accumulates and then partially cancels order memory. Its endpoint
alone hides that path. This observation does not prove that every observable
needs the area; the same-time Gram cancellation above is a counterexample.

The initialization-only cubic reductions were then tested, without fitting:

| Case A model | Passive endpoint | Largest training-output error versus dense RK4 mean | Largest passive-output error |
|---|---:|---:|---:|
| Dense RK4 reference mean | 0.482637 | — | — |
| Two-state radial cubic | 0.448760 | 0.010855 | 0.033965 |
| Ordered cubic closure | 0.447236 | 0.013111 | 0.035401 |

Thus retaining this order correction **does not improve this moderate-label
example**; its passive error is about 7.3% of the reference endpoint. The full
causal system is much more accurate here. The correction is a valid structural
term, not an empirically validated cure. It should not replace the full system.
The radial model's saved area is deliberately zero in its reconstruction,
not a measurement of the actual area traced by its own turning u path.

## 4. An exact and more revealing passive observable

In either geometry, define the fixed coefficients a,b by v_3=a v_1+b v_2,
and define

\[
q_\ell=h_{\ell,3}-a h_{\ell,1}-b h_{\ell,2},\qquad
e=f_3-a f_1-b f_2=\frac1n w^\top q_2.
\]

The scalar e is the passive prediction's departure from the same geometric
mixture of training predictions. It is not an error against a validation
label—no such label is used or known here. A feature Gram gives the norm of
q_2, but its alignment with the learned readout is additional information.

The first-layer preactivations always obey the linear input relation. Therefore,
with g= tanh′ and componentwise products, their nonlinear defect obeys exactly

\[
\dot q_1=
a[g(z_{1,3})-g(z_{1,1})]\odot\dot z_{1,1}
+b[g(z_{1,3})-g(z_{1,2})]\odot\dot z_{1,2}.
\]

This identifies a concrete mechanism: **the same transported parameter motion
changes a passive representation differently because its activation sensitivity
differs from the training sensitivities**. For correlated inputs the actual
preactivation velocity is

\[
\dot z_{1,a}=\sum_{j=1}^2 c_j(v_a^\top v_j)
g(z_{1,j})\odot W^\top[w\odot g(z_{2,j})].
\]

Keeping only the j=a term for a training input would be incorrect. The
implementation tests this distinction away from initialization.

Differentiating e gives three exact sources:

\[
\begin{aligned}
\dot e={}&\frac1n\dot w^\top q_2\\
&+\frac1n w^\top\big[g(z_{2,3})\odot\dot W h_{1,3}
 -a g(z_{2,1})\odot\dot W h_{1,1}
 -b g(z_{2,2})\odot\dot W h_{1,2}\big]\\
&+\frac1n w^\top\big[g(z_{2,3})\odot W\dot h_{1,3}
 -a g(z_{2,1})\odot W\dot h_{1,1}
 -b g(z_{2,2})\odot W\dot h_{1,2}\big].
\end{aligned}
\]

The lines are readout learning, learned middle-layer writes, and lower-feature
motion propagated upward. Since w(0)=0, their integrated contributions add
to e(t), even though initialized features may already be nonlinear. They are
not obtained by subtracting endpoints of separately trained models.

The RK4 mean measurements at time 24 are:

| Same-trajectory source | Case A | Case B |
|---|---:|---:|
| Readout updates | 0.024590 | 0.020705 |
| Middle-layer writes | 0.015273 | 0.015313 |
| Propagated lower-feature motion | 0.040291 | 0.031598 |
| Sum: passive nonadditivity e | 0.080154 | 0.067617 |

The readout source can itself read inherited or newly changed nonlinear
geometry. Its portion paired with the **initial** q_2 is −0.007181 in A and
−0.002684 in B; these small means have substantial run variability and are
not claimed to have robust negative sign. Subtracting them from the full
readout source isolates its part paired with changed geometry. All three
primary sources above have the displayed positive sign in every tested seed.

The explicit drift of the *upper* gate inside the two feature sources adds
0.007657+0.009314 in A, and 0.008108+0.009750 in B. These are partitions of
the middle/lower terms, **not** a fourth source. They do not include indirect
gate effects on other state variables and must not be identified with either
the cubic approximation error or a full-versus-affine intervention difference.

The complete derivation, alternative current-state secant-gate decomposition,
and causal-history equivalents are in
[PASSIVE_NONLINEARITY_DIAGNOSTICS.md](PASSIVE_NONLINEARITY_DIAGNOSTICS.md).
In particular the causal passive readout requires current passive features
paired with earlier training features. Its Gaussian source is not frozen:
its covariance changes with the lower feature defect. A constant initialized
kernel or independent fresh return noise would lose different parts of this
mechanism.

## 5. Why small ablation effects need not mean an unimportant mechanism

For the symmetric diagnostic control, the same two initialized dense draws
were trained normally, with W frozen, or with each activation replaced by its
initialized affine tangent in both forward and backward calculations:

| Symmetric control | Passive output | Integrated readout source | Middle source | Lower source |
|---|---:|---:|---:|---:|
| Full tanh | 0.354033 | 0.030746 | 0.014777 | 0.040183 |
| Frozen middle matrix | 0.351793 | 0.031178 | 0 | 0.052304 |
| Initialized-affine activations | 0.315566 | 0.018086 | 0.007392 | 0.021760 |

The source columns sum to passive nonadditivity, not to the passive output;
the latter also has its geometric training-prediction part. Freezing W changes
the final passive prediction by only about 0.00224, although middle learning
contributes about 0.01478 on the full path. Much of that contribution is
reallocated to lower-feature motion in the frozen-W trajectory. This is a
concrete compensation effect, visible in the equations and the measured
sources. It is not legitimate to infer a source contribution from the small
endpoint difference alone.

The affine control retains parameter learning but removes gate evolution
consistently from both forward and backward maps. It has a smaller passive
nonlinear response. It is a changed, input-anchored model, neither a frozen
kernel nor a theorem-backed approximation of the original network.

These two-seed controls confirm the direction of the earlier four-seed
phase-1 comparisons; they are not a new large-sample causal-effect estimate.

## 6. Numerical controls, corrections and remaining uncertainty

- Instantaneous dense identities agree to at most 1.63×10⁻¹⁵ over the saved
  trajectories. Independent tiny finite-difference checks validate outputs,
  Gram velocities and correlated-input gate identities away from t=0.
- RK4 step halving changes output curves by at most 2.29×10⁻⁸ in A and
  1.65×10⁻⁸ in B. Integrated passive-source reconstruction errors over all
  RK4 cohorts stay below 8.83×10⁻⁹. The nonlinear ordered-integral identity
  has integration error up to 1.94×10⁻⁷; it is not an instantaneous identity
  violation. Separate small-step tests show fourth-order RK4 convergence.
- Euler histories require their exact discrete product-rule correction.
  Raw left-point sums satisfy
  I+Iᵀ=uuᵀ−h²Σ_k c_kc_kᵀ, not the continuous identity. The correction is
  symmetric, so signed area is unchanged. Integrating continuous source
  rates by Euler also leaves expected finite-step error; **only RK4 source
  integrals** are used in the additive source tables.
- Causal step halving is not negligible at the displayed precision. Maximum
  output-mean changes are about 0.00580 in A and 0.00504 in B. For B, area
  changes by about 0.01944. Dense B likewise has area 0.06714 with Euler
  step 0.4 versus 0.02863 with accurate RK4. Good output agreement must not
  be mistaken for high-precision continuous-time order-memory agreement.
- The Gaussian factorization's maximum covariance reconstruction discrepancy
  is 6.37×10⁻⁹ and maximum discarded innovation variance 1.16×10⁻¹².
  Those numbers audit factorization, not Monte Carlo error or closure bias.
- Initial coefficient quadrature uses order 96. Refining 64→96 changes
  the lower and upper tensors by at most 3.94×10⁻⁷ and 1.43×10⁻⁷;
  rotating Gaussian coordinates at order 96 changes them by at most
  4.24×10⁻⁹ and 1.57×10⁻⁹. Reduced-ODE solver refinement changes outputs
  by less than 2.3×10⁻¹¹. These numerical errors do not explain the
  observed cubic passive failure. Quadrature convergence is empirical,
  not a rigorous enclosure of every coefficient.

No correction to the full causal equations was indicated by these tests.
What required correction was the proposed simplification and its interpretation:
current training Grams and a cubic residual clock are not adequate substitutes
for passive feature/response history at the tested moderate labels. Likewise,
the integral diagnostics must respect discrete versus continuous identities.

A possible next approximation retains the initialized quadratic preactivation
displacement but evaluates tanh on it without Taylor-truncating the gate. Its
explicit initialization program is recorded in the passive diagnostic note.
It matches known local coefficients, but has **not** been tested in this
campaign. Later displacement-direction changes remain omitted. It is not
reported as an improvement, nor silently used to repair failed predictions.

## 7. Evidence and reproducibility

Sources frozen during this campaign:

- [dense_response_phase2.py](dense_response_phase2.py): dense flow and
  joint-stage companion diagnostics, arbitrary declared panel geometry.
- [causal_response_phase2.py](causal_response_phase2.py): wrappers around the
  unchanged full causal simulator, with configuration and source hashes.
- [ordered_response_approximation.py](ordered_response_approximation.py):
  initialization-only coefficient integration and closed approximations;
  this program never reads a completed dense or causal trajectory.
- [analyze_response_phase2.py](analyze_response_phase2.py): numerical summaries,
  comparison diagnostics, figure and generated-output checksum manifest.

All raw arrays and records are under
`data/generated/transparent_learning_dynamics_20261007/unequal_residuals_v1/`.
`analysis/summary.json` contains all reported values, `analysis/sha256.json`
records generated-file hashes, and `analysis/mechanism_phase2.png` plots
the evolving passive response, area, and source contributions. Its full causal
curves use Euler; its dense mechanism curves use RK4, explicitly labeled.

[The scoped instrumentation check](PHASE2_INSTRUMENTATION_CHECK.md)
independently tests the exact identities and discretization qualifications.
The separate [approximation/evidence check](PHASE2_APPROXIMATION_EVIDENCE_CHECK.md)
examines tensor indices and reconstructs the reported numbers. Its identified
missing plus sign in the displayed lower-defect equation has been corrected;
this was a transcription defect in the report, not in the numerical code.
These are internal checks, not independent promotion reviews or full campaign
replications.

No shared-book edit, external literature search, global-proof expansion or Git
commit was performed. The original full-trajectory dense-variability guarantee
remains open and paused. This phase resolves a narrower scientific question:
it explains a measured passive nonlinear response and demonstrates why a
seemingly successful training-only reduction loses it.
