# Independent complete audit: odd two-input theorem

Date: 2026-09-07. Reviewer: independent `odd_final_core` agent.

**Verdict: PASS.** The complete population/GF/raw-GD theorem for the stated
two-input class is supported by the inspected proof and its mathematical
dependencies. I found no counterexample or remaining mathematical or
quantifier gap in the theorem. The two presentation points identified
during this audit were corrected and the revised files were rechecked.

This is a fresh audit of the four files identified below. I read the
candidate contract and all four mathematical files in full, independently
derived the principal equations and constants, and inspected the source
arguments needed by the response and limit interfaces. I did not read
sibling or historical review reports or status files, use another review
as evidence, delegate, run mathematical experiments, or edit the proofs.
Historical headers within mathematical source files were not premises.
The `solve-math-rigorously` skill was read and followed.

## 1. Inspected candidate and source integrity

I computed SHA-256 directly from the file bytes. All four values match
`CANDIDATE_HASHES.json`:

| Candidate file | Inspected SHA-256 |
| --- | --- |
| `PROOF.md` | `a4d6ed0ee99a1e111b5eba068f2219cf561a2281b1828b26227aca7a0a54a050` |
| `AFFINE_CORE.md` | `634dd3bbc35436e9d1760bee5c11cbf2124b3c42e8920a1bf3a4fcbb15039711` |
| `SOURCE_AND_LIMIT_BRIDGE.md` | `2a140f2a5a39f911b5c2ca51bc79102d20e9209f1450d38005360c88103f6e77` |
| `INITIAL_MOTION_AND_NORMALIZATION.md` | `c96316fdc481ef3f9e6fc402514ca9b45bcff12e199023505fbbb86d4e15bf24` |

I also independently verified every entry of `SOURCE_HASHES.json`:

| Source file | Verified SHA-256 |
| --- | --- |
| `ANGLE_SPECIFIC_THEOREM_ASSEMBLY.md` | `27b2579f27ec14319dd39a93a4942d7b6463860648462d5ccb31b662c7725b75` |
| `CONTRACT.md` | `e32b52edb2c8061a341b1e93ff237f62f59d03f84b16e5b67a941bdd460c21bd` |
| `FIXED_CAP_VELOCITY_BRIDGE.md` | `a2322a8dbacf28244b9fef63e757ba3a915628dbdf31020062f8c5772a1c0aa0` |
| `INITIAL_FEATURE_LEARNING.md` | `bd81de0a7ad0cb9bdd1f27f89961f4a3b7a7da6914456ae08596a882fa2ec351` |
| `L3_LOCAL_COMPLETE_PROOF.md` | `f97148f84979ab5b8489927d477b6abb3d919e27fd457455f2e3b98416725de4` |
| `NONLINEAR_RESPONSE_PERTURBATION.md` | `ef0ea077406a27307bc84e045feebf5099f6f81883bdfed41508035fe4559568` |
| `PREVIOUS_TWO_SAMPLE_PROOF.md` | `2891b892667396d64bd747689bcd59aa7ca3ffd224d3579fc3407bca0b623f9a` |
| `PRIMAL_COMPARISON_AND_CONTINUATION_BRIDGE.md` | `99eb60a64df1bbf4d8b70f351198abced9ef7eaeacf9b39c3997da5700a8f066` |
| `SYMMETRY_RADIAL_CLOCK.md` | `40882fc19e44b4b9245156595bb1071bd4de6007d619fada54c9fce7c37903f4` |
| `THREE_SAMPLE_CONTROLLED_RESPONSE_LEMMA.md` | `49da0f68047b4f516d3ad3c94b7112259838bcebf68e2296a948364232842789` |
| `TWO_SAMPLE_SOURCE_BASELINE.md` | `a84187ecd3639d0c4b7b209255056597326c97f11548faaf9b918659ae07477f` |

Hash verification of this entire source manifest is distinct from the
mathematical reading scope. The latter included the controlled-response
proof, the comparison/continuation proof, the fixed-cap velocity proof,
and the previous two-sample assembly in full; the operative source
representation, primal/probe, and finite-array sections of the affine
baseline; the moment, derivative, same-array, and chronological closure
sections of the nonlinear response proof; and the generic conditioning,
singular-query, common-action/adjunction, and scalar-gradient portions of
`L3_LOCAL_COMPLETE_PROOF.md`. The new affine and initial-motion arguments
were checked directly, without importing their older counterparts.

## 2. Exact claim and model

The verified order is

\[
\forall\delta\in(0,1]\ \exists e_\delta>0\
\forall a\in[1/2,1]\ \forall e\in(0,e_\delta]\
\forall(d,x_1,x_2,y_1,y_2)\text{ satisfying (2)}\
\forall T<\infty.
\]

The same activation is used in all three hidden layers, without offsets
or biases. The input condition excludes both incompatible endpoints for
both label sectors. At \(\delta=1\), the class reduces to orthogonal
inputs and remains covered; dimensions unable to realize the class are
explicitly vacuous. The proof does not select a coefficient using an
actual correlation, label pair, dimension, mesh, cap, width, or horizon.

I independently differentiated the finite predictor and loss in the
displayed metric. The Euclidean first-layer derivative contains \(1/n\),
which the metric factor \(d/n\) converts to \(1/d\). The two matrix
updates retain \(1/n\), and the readout metric cancels its predictor's
\(1/n\). This gives precisely equation (5). The four kernel blocks in
(6), including the first-block factor \(\Gamma_{ij}\), are the resulting
raw gradient inner products. The Hilbert--Schmidt normalization matches
the ordinary Frobenius norm because
\(\|uv^T/n\|_F=\|u\|_n\|v\|_n\).

The finite readout has RMS size \(O_{\mathbb P}(n^{-1})\), is retained in
both algorithms, and vanishes only in the population limit. The proof
does not replace the actual two residuals by a finite-width scalar
residual. Raw GD is simultaneous Euler at exactly \(n^{-2}\), and the
stipulated recomputed fields and one-sided derivative conventions are
used.

## 3. Label symmetry and the affine core

**Label folding: checked.** Odd forward maps and even derivatives give
\(h(-x)=-h(x)\), \(f(-x)=-f(x)\), and \(b(-x)=b(x)\).
Replacing each pair by \((y_ix_i,1)\) preserves the entire raw loss and
each update, including the first-layer input factor. The folded
correlation is \(\tau\rho\), where \(\tau=y_1y_2\).

The reflection exchanging two equal-norm folded inputs is defined
because \(\tau\rho<1\). Gaussian initialization is invariant under
this raw isometry. Fixed-program limiting contractions are deterministic,
so exchange invariance implies equal folded predictions. Passing through
fixed-cap Euler and strong limits avoids assuming uniqueness before the
uncut flow exists. Thus the uncut population relation
\(f_i=y_i g\) is justified for every binary label pair.

**Affine equations and gains: checked.** With
\(u=(x_1+\tau x_2)/2\), \(v=(x_1-\tau x_2)/2\), their normalized
variances are \(v_u=(1+\tau\rho)/2\),
\(v_v=(1-\tau\rho)/2\), both at least \(\delta/2\). Direct
gradient differentiation gives

\[
C'=\sigma aP_3,\quad
B'=\sigma a^2C\otimes P_2,\quad
A'=\sigma a^3B^*C\otimes P_1,\quad
P_1'=\sigma v_u a^3A^*B^*C,\quad Q_1'=0.
\]

The active sector is common for equal labels and contrast for opposite
labels. In either case the dynamics depend only on the active root and
initial matrices when the initial readout is zero.

**Radial and endpoint estimates: checked.** Writing the hidden
linearization of \(H\) as \(J\) gives
\(C''=JJ^*C\). Convexity of the regularized readout norm passes to
convexity of \(\|C\|\), with initial slope \(\|H_0\|\). Therefore
\(g'\ge\|C'\|^2\ge a^6v_u\ge\delta/128\).
The raw energy identity and Cauchy--Schwarz give the strong endpoint
estimate and prevent loss of the affine branch before its target hit.
The numerical bounds are correct:

\[
S\le192/\delta,\qquad
\sup_{s\le S}\|\Theta(s)-\Theta(0)\|_{\rm raw}
\le12\sqrt{2/\delta}.
\]

Each path stops at its own hit of \(3/2\); the proof never runs an affine
reference past that hit merely to reach the uniform duration bound.
Only first-layer projections and displacement enter the selection
constants, so the full initial \(\sqrt d\|w_0\|_2\) causes no hidden
dimension dependence.

**Frozen inactive fields: checked independently.** This part correctly
uses finite conditional independence, not an invalid inference from a
bounded learned operator alone. At a fixed affine scalar-Euler mesh,
condition on \(P_{1,0},A_0,B_0\). The inactive root is independently
\(N(0,v_vI_n)\), and the active trajectory and learned increments are
measurable under this conditioning. Bounded RMS update factors imply
bounded ordinary Frobenius increments. Hence

\[
E[\|T_nQ_0\|_n^2\mid\mathscr F_n]
=v_v\|T_n\|_F^2/n\longrightarrow0
\]

for \(T_n=A_s-A_0\) and \(T_n=B_sA_s-B_0A_0\). The latter is
Frobenius bounded by the two product-difference terms displayed in the
proof. Fixed-program joint convergence and then strong affine Euler
convergence yield the exact frozen identities at every reference time.
Conditional scalar variance estimates also give zero inactive mean and
active/inactive cross moment. These arguments hold in both label sectors.

With linear activation, every finite population transcript is linear in
its Gaussian source coordinates; rank-one learned memories involve only
deterministic contractions. Strong limits preserve Gaussianity. Active
root sign symmetry and the preceding inactive calculation make the laws
centered. Consequently

\[
\operatorname{Var}(z_i^\ell)
\ge a^{2(\ell-1)}v_v\ge\delta/32,
\qquad \|z_i^\ell\|_2\le U^3.
\]

The worst gain/layer is \(a=1/2,\ell=3\), giving exactly
\((1/16)(\delta/2)=\delta/32\). There is no missing activation power.

## 4. Uniform nonaffinity and the one coefficient choice

The arctangent affine-regression error is continuous on the stated
Gaussian parameter interval, whose standard deviation is bounded below
by \(m=\sqrt{\delta/32}\). Full Gaussian support excludes zero error.
Thus the compact minimum \(\eta\) is strictly positive and depends only
on \(\delta\).

The transfer estimate uses the optimal slope for the perturbed variable.
Centering is a contraction, so \(\|Z-Z_0\|_2\le m/2\) yields
\(\operatorname{sd}(Z)\ge m/2\), and the slope magnitude is at most
\(\pi/m\). Using that regression as a competitor for \(Z_0\) proves
the stated \(\eta/4\) conclusion. It does not assume Gaussianity of
the nonlinear trained field.

I checked the forward comparison constants \(Q,J,O\), their use of the
raw component sum norm, and all restrictions in (17). The same-state
component error bounds sum to at most \(40eb^3\); the affine
\(9b^2\)-Lipschitz bound is valid in the raw/HS norm. The restrictions
leave strict primal slack and give an endpoint above \(5/4\). Each term
in the minimum is positive at fixed \(\delta\). The resulting margin is

\[
\inf_{i,\ell,s\le S}\inf_{\alpha,\beta}
E[\phi_{a,e}(z_i^\ell)-\alpha-\beta z_i^\ell]^2
\ge e^2\eta/4>0.
\]

This is uniform over the reference interval, samples, layers, gains and
admissible datasets for each fixed positive \(e\). It does not assert a
positive margin uniform as \(e\downarrow0\), which would be false.

## 5. Gaussian actions, response closure, and removal of caps

The generic conditioning proof identifies both orientations of each
initialized Gaussian matrix. It retains the complete derivative response
and the full second moments of query inputs. Its independent-query noise
argument regularizes singular Gram matrices at fixed transcript length;
fixed-program stability and continuity of finite covariance square roots
remove that noise. It does not assume pseudoinverse convergence at rank
drops. Countable compatible programs, finite matrix norm bounds, dense
generated probes, and finite transpose identities construct bounded
canonical actions with their actual adjoints. The use here satisfies the
coordinate/root hypotheses after fixing a cap.

The source extension changes the constant affine gates to \(aI\) and
removes an additive constant whose derivative was zero. The explicit
bounds \(|\phi'|,|D_q|\le2\), \(|D_z|\le2eR\), and linear
forward growth suffice. No response formula needs a positive offset or
an inverse input covariance. The affine probe argument remains valid
with gain \(a\le1\); its state, answer, and output bounds are dominated
by the displayed gain-one bounds. The factor two in the chosen block
and time-row constants is conservative and accounts for the required
sum of maximum block row norms.

The bounded continuous affine path supplies sufficiently fine population
Euler bounds. Exact finite rank-one unrolling supplies the finite-array
premise with \(p=11+2U+4S_\delta(2U)^3\); this does not require trained
operator-norm convergence across widths.

I checked the moment Volterra estimates, the source-step factor in a
single reverse-source derivative, the past-time exponential envelope,
and the necessary current multiplier \(1+eQ_k\) for backward outputs.
The convexity/Hölder argument controls the envelope moments without a
random supremum over all source times. The chronological order
\(\alpha^2_k,\alpha^3_k,\beta^3_k,\beta^2_k\) closes using only
already available rows. The current transpose returns are retained;
there is no simultaneous unknown current-row inverse. Taking every
unindexed gain at its upper bound gives one finite \(K\) before
selecting \(e\). Thus the source threshold is uniform in \(a\),
geometry, controls, cap and mesh under its precise affine premise.

The asymmetric gate identity is exact. Its incoming-field discrepancy
is multiplied by at most two; only forward-state discrepancies receive
the factor \(R\). Backward substitution therefore has a single linear
\(R\) loss. The reference's Gaussian tails defeat the resulting
\(\exp(CR)\) factor. This proves strong cap removal including raw
directions and Hilbert--Schmidt increments. Comparing an arbitrary
bounded-primal competitor to the reference uses no competitor tail
assumption and yields strong uniqueness. Repeating the estimate from a
reached time proves the stated restart property.

## 6. Physical time and every requested limit

The uncut gradient path has positive initial projected kernel by the
odd monotonicity inequalities
\(q_\ell\pm c_\ell\ge a^2(q_{\ell-1}\pm c_{\ell-1})\).
The strong trajectory chain rule justifies the nonlinear radial argument
after existence has been constructed. A first hit of \(g=1\) occurs
strictly before the endpoint. Bounded derivative at that hit makes
\(\int ds/[2(1-g)]\) diverge, producing one global physical path.
The loss rate \(\mathcal L(t)\le\exp(-\delta t/32)\) has the correct
factor four from \(d\mathcal L/dt=-4\kappa\mathcal L\).

For caps the first-hit clock requires continuity and bounded derivative,
not monotonicity or a gradient identity. The source bridge explicitly
proves this correct version. Each resulting physical reference inherits
the feature-interval primal and tail bounds. Physical uniqueness uses
both actual residuals, so nonsymmetric competitors are covered.

The finite bridge first identifies a fixed cap and fixed auxiliary mesh.
Finite rank-one unrolling gives a larger primal ball with slack; the
deterministic Euler defect bound is independent of width on this ball.
This removes the auxiliary mesh without applying a Gaussian theorem to
an increasing transcript. The finite uncut system is compared with its
same-width cap reference using only reference tails, then width precedes
cap removal. For actual raw GD, its derivative is evaluated at the
preceding GD node and the only extra cap-reference defect is
\(C_{R,T}n^{-2}\). The argument gives the full width sequence in
probability, not a selected subsequence.

I checked the velocity source extension by the two additional forward
queries. The products \(\phi'(Z)P\) are first smoothly truncated;
the bounded-derivative conditioning theorem is not applied directly to
these unbounded-derivative products. Their response and memory terms
are retained. The deterministic velocity comparison uses a single
truncation level multiplying the state error and only reference
velocity tails. The compact \(L^2\) image of the uncut velocity supplies
uniformly vanishing tails. Taking cap to infinity at fixed velocity
truncation, then removing the truncation, avoids an unsupported bound
on the growth of cap-dependent fourth moments.

These estimates give uniform-time joint same-layer \(\mathcal W_2\)
laws with velocities, fixed-finite-time joint laws, all second moments,
and integrated squared speeds. Products of convergent \(L^2\) fields
give every kernel entry. The interpolation bound
\(\|x-I_hx\|_\infty^2\le4h\int|x'|^2\) supplies the additional
path-space coupling estimate, so the claimed
\(\mathcal W_2(C([0,T];\mathbb R^4))\) topology is justified.
There is no inference of a continuous-path velocity law, a pairing of
different neuron populations, or cross-width operator-norm convergence.

## 7. Initial motion and normalization

Initial forward Gram positivity follows from full Gaussian support and
strictly positive derivative. For \(e>0\), the beta Gram \(S_3\) is
positive definite: a vanishing quadratic form gives the everywhere
product identity in the companion, and nonconstant \(\phi'\) then
forces both coefficients to vanish. This argument would not give
strict definiteness at \(e=0\); the proof only needs it at positive
\(e\).

The initial transpose law correctly assigns covariance \(S_3\) itself
to the reverse Gaussian source, together with the displayed derivative
return. A residual covariance after forward regression would be wrong.
Conditioning on the middle forward fields gives the lower bound on
\(S_2\), and the second transpose uses its full covariance and the
derivative of the actual middle query. The conditional-variance lower
bounds for the first block and each first-layer sample are correct.
The trace identities make both matrix blocks nonzero. The aggregate
upper-layer adjunction identities, combined with the input exchange and
readout sign symmetry, establish nonzero acceleration for each sample,
not merely for one of them. The positive gate transfers it to features.

The kernel expansion coefficients and time conversions check:
\(\vartheta(s)=\vartheta_0+s^2V/2+o(s^2)\),
\(\kappa(s)=\kappa_0+2s^2\|V\|^2+o(s^2)\), and
\(s'(0)=2\), so physical hidden acceleration is \(4V\) and the
physical kernel coefficient is \(8\|V\|^2\). The readout has
initial velocity \(2H_0\ne0\). Its optional physical acceleration
formula \(-4\kappa_0H_0\) is also consistent.

For normalization, pointwise \(0<|\arctan z|<|z|\) yields
\(0<\nu<\mu<1\), hence
\(1<D_r<1+r\le2\) when \(0<r\le1\). Thus the normalized
coefficients lie in the proven rectangle, with \(e_r\le r\), and
unit Gaussian second moment holds exactly. A positive literal convex
mixture has strictly smaller Gaussian energy than the identity.
Normalized positive coefficients sum to more than one. The distinction
is correctly stated, and initialization variance preservation is not
mistaken for trained variance conservation.

## 8. Revision verification and final assessment

The first inspected versions of `PROOF.md` and `AFFINE_CORE.md` had hashes
`485bf06344107b63b09ae4585408dc733362c97870848b5d4605f6334880b574`
and `57c154d7b4d5d161b8f4c5c78114ff692784897c389e063e3340bdfb815ee9dc`.
I identified a local notation-scope issue: the phrase “including cap
paths” preceded an equation also containing the uncut gradient identity.
The correct cap identity is
\(\dot\Theta_R=2(1-g_R)V_R(\Theta_R)\), and it does not assert a
gradient field. The downstream clock proof already used this correct
distinction, so this did not leave a missing construction or estimate.
Several displays also had literal `quad` separators without their
LaTeX backslashes.

The revised files have the hashes in Section 1, independently recomputed
after the revision. I inspected the revised mathematical text, including
the revised full affine companion and the main proof's unchanged
construction/limit argument. Equation (7) now contains only the scalar
identities. Its following paragraph explicitly distinguishes the uncut
gradient from the capped feature field, and `AFFINE_CORE.md` Section 1
explicitly restricts the gradient and kernel-derivative identities to
the uncut field. The missing separator backslashes are restored. The
other two candidate hashes remain unchanged. These corrections resolve
both presentation points without changing any estimate or quantifier.

I explicitly tested the two label sectors, \(\delta=1\), the smallest
gain, near-endpoint correlations still inside the allowed class,
\(e\downarrow0\) with each coefficient fixed before the width limit,
the finite nonzero readout, inactive-root conditioning, and cap-clock
nonmonotonicity as possible failure points. None yields a counterexample
or a missing mathematical implication. The excluded antipodal/equal-label
and identical/opposite-label obstructions do not apply to the target.

**Final verdict: PASS for the exact theorem and the inspected candidate
hashes.** The theorem has the complete stated global population,
strong uniqueness/restart, finite GF/raw-GD, observable, nonaffinity,
initial-motion, and normalization scope. This verdict supplies no claim
uniform over the physical half-line, no positive coefficient for all
\(\delta>0\), and no three-input odd-activation theorem.
