# Independent round-two review

**Verdict: clean PASS for the stated conditional special-angle implication.**

**Required corrections: none.** Optional expository clarifications are listed at the end.

Sole mathematical input:

- File: SPECIAL_ANGLE_NONTRIVIALITY.md, at /tmp/l2-two-sample-proof-0ywjpp/SPECIAL_ANGLE_NONTRIVIALITY.md.
- SHA256: b14f75e6909b32762aca147f14a6ab7d3bafd6394c2d93e9a4df76ed1b142c3c.
- Read in full: all 346 lines.

This audit used only that candidate as mathematical input. No previous report, project files, other mathematical files, external theorems, experiments, or agents were used. The procedural solve-math-rigorously skill was read. The candidate was not edited.

The verdict does **not** certify the existence of the assumed global representations, a canonical population construction, convergence of a complete finite-width trajectory, intermediate angles, or additional hidden layers. It certifies the deductions from the candidate's stated premises and the finite initialization calculation within its stipulated independent initialization regime.

## 1. Premises and scope: valid conditional setup

The two population spaces remain distinct. Every movement of an operator across an inner product uses the actual adjoint between those spaces. Hilbert--Schmidt increments supply the metric for the hidden matrix even though the initial bounded operator need not itself be Hilbert--Schmidt.

The regularity assumptions in lines 41–47 are sufficient for the curve calculations used subsequently:

- Continuous original velocities give locally integrable \(L^2\) velocities and pointwise absolutely continuous representatives of the field curves.
- Operator-norm continuity gives a bounded operator norm on every fixed compact time interval and permits passage to limits through the operator and its adjoint.
- Bounded \(W^{(3)}\), bounded activations and bounded activation derivatives make the displayed kernel entries finite. Their continuity follows from the stated \(L^2\) continuity and the bounded-gate argument checked below.
- The assumed raw loss identity gives bounded residual controls on each finite interval.
- The exchange symmetry supplies both \(f=(g,-g)\) and equality of the two samples' corresponding velocity norms. For orthogonal inputs these are population-law consequences, not finite-neuron identities.

The global decompositions (2), Gaussian-source properties, independence of the entire \(\zeta\) process from \(G\), deterministic finite-interval bounds on the remainders, and variance identities (3) are substantive assumptions. They are not derived from the operator or primal-field bounds in this note. The informal response-row explanation in lines 72–74 is not needed to establish the conditional implication and is not separately certified here.

For \(C=I\), the first-layer metric is the sum of the two field metrics. For antiparallel inputs it is the metric of one independent field. The candidate consistently retains this distinction.

## 2. Transformed first-field tails and feature Gram: valid

For orthogonal inputs,
\[
\frac{d}{dt}F(Z^{(1)}_a)
=(1+(Z^{(1)}_a)^2)\bigl(-2r_a\phi'(Z^{(1)}_a)Q^{(1)}_a\bigr)
=-2r_aQ^{(1)}_a.
\]
For the independent antiparallel field the coefficient is \(-4r_1\), since \(r_2=-r_1\) and the reverse fields coincide.

Applying this scalar identity to the absolutely continuous representatives is legitimate without assuming that composition by the cubic \(F\) is differentiable on all of \(L^2\). Its integrated right side belongs to \(L^2\): \(F(G_a)\) has finite second moment, the controlled Gaussian integral has finite variance by hypothesis, and the remainder integral is bounded by a deterministic constant on each finite interval.

The residuals are scalar population quantities, so their time dependence gives deterministic controls for the Gaussian integrals. Consequently the integrated Gaussian vector \(I(t)\) is independent of \(G\). No independence of the bounded integrated error \(E(t)\) is needed.

For every fixed finite time and threshold, the event that \(I(t)\) lies in a sufficiently large bounded box has positive probability. Intersecting this event with a sufficiently extreme positive or negative Gaussian initial coordinate proves both tails of each first field. A degenerate \(I(t)\), including at time zero, causes no problem.

For \(C=I\), the full support of the initial Gaussian pair permits all four extreme sign patterns simultaneously with that bounded-box event. Hence the closure of the support of the first-feature pair contains all four saturation corners. If \(v^\top H^{(1)}=0\) almost surely, the closed zero set of this linear function must contain \((B,B)\) and \((B,-B)\). These two equations imply \(v=0\), proving that the uncentered Gram \(\Gamma_1(t)\) is positive definite.

For antiparallel inputs, \(H^{(1)}_2=-H^{(1)}_1\), so the Gram has rank one and \(\|H^{(1)}_1\|_2>0\). The proof does not invert this singular Gram.

## 3. Second-field tails and distributional nonaffinity: valid

The positive first-feature norm makes each \(\xi_a(t)\) nondegenerate through (3). The event inclusions
\[
\{\xi_a>R+M_T\}\subseteq\{Z^{(2)}_a>R\},\qquad
\{\xi_a<-R-M_T\}\subseteq\{Z^{(2)}_a<-R\}
\]
prove both second-field tails even when \(S_a\) depends on \(\xi_a\).

Every field involved is an \(L^2\) random variable. For any one of these variables \(Z\), the Gram of \(1,Z\) has determinant \(\operatorname{Var}(Z)>0\). Thus their span is a closed two-dimensional subspace of \(L^2\).

If the squared distance in (5) were zero, closedness would imply an exact equality \(\phi(Z)=aZ+b\) almost surely. A nonzero \(a\) is incompatible with an unbounded tail and bounded \(\phi\). If \(a=0\), strict monotonicity of \(\phi\) forces \(Z\) to be constant. Both cases are excluded. Equation (5) therefore holds for both layers, both samples, and every finite time, including zero.

This establishes a strictly positive distance for each distribution and time. It does not claim a time-uniform positive distance.

## 4. Residual evolution and nonfreezing: valid at every \(t>0\)

The three kernel blocks are Gram matrices in the respective physical parameter metrics. Direct differentiation gives
\[
\dot f=-2Kr,\qquad K=K^{(1)}+K^{(2)}+K^{(3)}.
\]
Since \(r=(g-1)y\) and \(g=y^\top f/2\),
\[
\dot g=(1-g)y^\top Ky=4(1-g)\kappa.
\]
The finite-interval bounds make \(\kappa\) locally bounded. With \(g(0)=0\), integrating this scalar equation proves (6) and \(g(t)<1\) at every finite time.

At zero the hidden blocks vanish and \(\kappa(0)=\|(\phi(X_1)-\phi(X_2))/2\|_2^2>0\). Independence and nonconstancy prove positivity in the orthogonal case; exact opposition proves it in the antiparallel case. Continuity gives positive \(g\) immediately after zero, and \(\kappa\geq0\) then gives \(0<g(t)<1\) for every \(t>0\).

The remaining implications are valid in the following order:

1. \(g>0\) implies \(W^{(3)}\neq0\) in \(L^2\).
2. Since \(\phi'\) is everywhere strictly positive, each \(\delta^{(2)}_a\neq0\).
3. By (3), each corresponding \(\zeta_a\) is nondegenerate. Its bounded remainder cannot remove its tails, so each \(Q^{(1)}_a\neq0\).
4. The nonzero residual coefficient and strictly positive gate make each first preactivation velocity nonzero. Another multiplication by the positive gate makes each first activation velocity nonzero.

For the hidden matrix, the squared-speed expression (7) is the Hilbert--Schmidt norm expansion of its finite sum of rank-one velocities. Applying \(\Gamma_1\geq\lambda_{\min}(\Gamma_1)I\) to the vector \((y_a\delta^{(2)}_a)\) pointwise in population 2 proves the lower bound. Both its coefficient and the resulting sum of squared norms are positive. In the antiparallel case the reduced rank-one expression has two nonzero factors, so its speed is positive.

The energy pairing (8) is also exact. Its matrix term is
\[
\sum_a c_a\langle\delta^{(2)}_a,\dot W^{(2)}H^{(1)}_a\rangle_2
=\left\|\sum_a c_a\delta^{(2)}_a\otimes H^{(1)}_a\right\|_{\rm HS}^2.
\]
Its other term becomes \(\sum_a c_a\langle\delta^{(1)}_a,\dot Z^{(1)}_a\rangle_1\) by the actual adjoint and the activation chain rule. This equals the sum of first-field squared speeds for \(C=I\). For antiparallel inputs it equals
\[
(c_1-c_2)\langle\delta^{(1)}_1,\dot Z^{(1)}_1\rangle_1
=\|\dot Z^{(1)}_1\|_2^2,
\]
because \(\dot Z^{(1)}_1=(c_1-c_2)\delta^{(1)}_1\). There is no missing factor two.

The positive right side of (8) excludes both second preactivation velocities being zero. The stipulated exchange symmetry, or exact opposition in the antiparallel case, then excludes either one being zero. Positive gates give the same conclusion for the second activations.

Finally, a zero readout velocity would make \(H^{(2)}_1-H^{(2)}_2=0\), contradicting
\[
g=\tfrac12\langle W^{(3)},H^{(2)}_1-H^{(2)}_2\rangle_2>0.
\]
The continuity assumptions support these conclusions at every positive time, not just almost every time. Hidden velocities are correctly zero at initialization.

## 5. Actual reused-transpose initialization law: valid

The calculation is in the candidate's independent finite initialization regime: conditional on the first-coordinate array, the initial matrix has independent \(N(0,1/n)\) entries. It would not follow merely from Gaussian marginal entries without that initialization independence.

Let \(P_H=H(H^\top H)^{-1}H^\top\). Conditional on \(H,Z\), the rowwise Gaussian decomposition is
\[
W_0=Z(H^\top H)^{-1}H^\top+\widetilde W(I-P_H).
\]
The remaining Gaussian matrix can be taken independent of \(H,Z\). Since \(D\) is a function of \(Z\), transposition and multiplication give exactly the conditional law (10). In particular, its mean is
\[
H\Gamma_n^{-1}(Z^\top D/n),
\]
and its residual conditional covariance between row \(i\), component \(a\), and row \(j\), component \(b\), is
\[
(\delta_{ij}-(P_H)_{ij})(\Sigma_n)_{ab}.
\]
Thus the reused reverse rows are not conditionally independent before the projection is removed.

Conditional on \(H\), the rows of \(Z\) are independent centered Gaussian pairs with covariance \(\Gamma_n\). The bounded continuous functions defining \(D\) give conditional averaging errors of order \(1/n\) in variance for \(D^\top D/n\). For \(Z^\top D/n\), bounded \(D\) and a bounded Gaussian second moment on bounded-Gram events give the same variance order. The conditional means converge as \(\Gamma_n\to mI\). These facts justify all three empirical coefficient limits in lines 243–247, including the one involving the unbounded factor \(Z\).

The discarded part is \(P_H\mathcal G\Sigma_n^{1/2}\). Its conditional expected squared empirical \(L^2\) norm is
\[
\frac{\operatorname{rank}(P_H)\operatorname{tr}\Sigma_n}{n}.
\]
For every fixed \(p\geq2\), its conditional expected empirical \(p\)th moment is bounded by
\[
\frac{c_p\|\Sigma_n\|^{p/2}}{n}
\sum_i(P_H)_{ii}^{p/2}
\leq\frac{2c_p\|\Sigma_n\|^{p/2}}{n}.
\]
Here \(0\leq(P_H)_{ii}\leq1\) and \(\sum_i(P_H)_{ii}=2\). This is a conditional moment estimate, not a pathwise bound. It proves the stated vanishing errors in probability. The antiparallel version has rank one.

After dropping this error, the added Gaussian rows are conditionally independent. Their common coefficients converge, their shifts are bounded on events of probability tending to one, and their covariance is bounded. Conditional averaging, initial Gaussian moments, and Gaussian added-row moments therefore give convergence of the joint empirical law with the old first coordinates, including each fixed polynomial moment. Mixed polynomial errors from dropping the projection are controlled by its higher empirical moments together with the tight empirical moments of the retained fields.

The limiting mean in row \(i\) is \(\sum_b B_{ab}\phi(G_b)\), with \(B=\mathbb E[DX^\top]/m\), so the index orientation in (9) is correct. The remaining covariance is \(\Sigma=\mathbb E[DD^\top]\). It should not be replaced by a covariance with a regression subtraction: the regression appears in the mean, while the removed noise has fixed rank and vanishing empirical size.

For \(C=I\), continuity and Gaussian full support extend an almost-sure linear relation among \(D_1,D_2\) to all \((x,y)\). Outside \(x=y\), the nonzero contrast then gives
\[
v_1\phi'(x)+v_2\phi'(y)=0.
\]
Varying \(x\) with \(y\) fixed, and then using \(\phi'>0\), forces \(v_1=v_2=0\). Hence \(\Sigma\) is positive definite. In the antiparallel case \(D=\phi(X)\phi'(X)\) is nonzero almost surely, so \(\mathbb E D^2>0\).

Both reverse-law formulas therefore yield strictly positive conditional Gaussian variance and \(\|\phi'(G_a)Q_a\|_2>0\). Their use for the actual initial operator is conditional on the explicitly stipulated joint empirical initialization law; this calculation does not independently construct that operator.

## 6. First nonzero strong limits: valid

The feature clock is locally invertible because \(ds/dt=4(1-g)>0\), and \(ds/dt=4\) at zero. In feature time the readout equation is
\[
(W^{(3)})'=V(s),\qquad V(s)=\tfrac12(H^{(2)}_1-H^{(2)}_2).
\]
Its integral and \(L^2\) continuity give \(W^{(3)}(s)/s\to V(0)\). Multiplication by the bounded gates then gives \(\delta^{(2)}_a(s)/s\to D_a\). Operator-norm continuity and the actual adjoint give \(Q^{(1)}_a(s)/s\to W_0^*D_a=Q_a\).

The gate convergence step is sound. If \(b_s\to b_0\) in probability with uniformly bounded gates and \(U_s\to U\) in \(L^2\), then
\[
\|b_sU_s-b_0U\|_2
\leq \|b_s\|_\infty\|U_s-U\|_2+\|(b_s-b_0)U\|_2\longrightarrow0.
\]
For the last term, first truncate the fixed \(U\); bounded convergence in probability controls the truncated part, and the \(L^2\) tail controls the rest. This argument also justifies the activation chain rule along the differentiable \(L^2\) curves. No global \(L^2\) Frechet differentiability is required.

The feature equations give the first two limits in (12) directly. For the second field, use
\[
\frac{(Z^{(2)}_a)'}s
=\frac{(W^{(2)})'}sH^{(1)}_a+
W^{(2)}\frac{(H^{(1)}_a)'}s.
\]
The initial Gram \(mI\) makes the first term tend to \(y_amD_a/2\). The second tends to \(y_aW_0(\phi'(G_a)^2Q_a)/2\). This proves the displayed \(v^{(2)}_a\), with strong convergence in the correct population. The matrix limit is strong in Hilbert--Schmidt norm.

The antiparallel equations reduce to coefficient one, giving exactly (14).

The squared-norm formula (13) follows because orthogonality of the two initial first features removes the matrix cross terms. The adjoint identity gives
\[
y_a\langle D_a,v^{(2)}_a\rangle_2
=\tfrac12\left(m\|D_a\|_2^2+\|\phi'(G_a)Q_a\|_2^2\right)>0.
\]
In the antiparallel case the corresponding pairing equals \(d>0\). Thus these are nonzero leading velocities, including in the second layer.

## 7. Hidden and full kernel quadratic change: valid

The feature-time gradient identity is consistent with the physical metrics:
\[
\kappa_{\rm hidden}
=\sum_a\|(Z^{(1)}_a)'\|_2^2+\|(W^{(2)})'\|_{\rm HS}^2
\]
for \(C=I\), with only one first-field squared norm in the antiparallel reduction. The strong limits therefore give
\[
\kappa_{\rm hidden}(s)=ds^2+o(s^2),\qquad d>0.
\]

The readout block must also be expanded. Since \(\kappa_{\rm readout}=\|V(s)\|_2^2\), its derivative is exactly
\[
\kappa_{\rm readout}'(s)
=\sum_a y_a\langle V(s)\phi'(Z^{(2)}_a(s)),(Z^{(2)}_a)'(s)\rangle_2.
\]
The strong limits yield
\[
\lim_{s\downarrow0}\frac{\kappa_{\rm readout}'(s)}s
=\sum_a y_a\langle D_a,v^{(2)}_a\rangle_2
=2d.
\]
For antiparallel inputs, the two terms are equal after accounting for the opposite second velocities and opposite labels; their sum is \(2\langle D,v^{(2)}\rangle_2=2d\).

Integrating the derivative limit yields the readout contribution \(ds^2+o(s^2)\). Adding the hidden contribution proves
\[
\kappa(s)=\kappa(0)+2ds^2+o(s^2).
\]
The positive coefficient implies \(\kappa(s)>\kappa(0)\) for every sufficiently small positive \(s\). Since \(\kappa=y^\top Ky/4\), the full raw kernel matrix cannot be constant near initialization. This is stronger than movement of parameters alone, and the readout contribution has not been omitted.

In physical time, \(s(t)=4t+o(t)\), so the same conclusion reads
\[
\kappa(t)=\kappa(0)+32dt^2+o(t^2).
\]
Thus using the local clock does not manufacture the kernel change or conceal the zero initial hidden velocities.

## 8. Factor cross-check

| Quantity | Orthogonal inputs | Antiparallel inputs, one independent field |
|---|---|---|
| First-field physical equation | \(2(1-g)y_a\delta^{(1)}_a\) | \(4(1-g)\delta^{(1)}_1\) |
| First-field feature equation | \(y_a\delta^{(1)}_a/2\) | \(\delta^{(1)}_1\) |
| Matrix feature equation | \(\frac12\sum_a y_a\delta^{(2)}_a\otimes H^{(1)}_a\) | \(\delta^{(2)}_1\otimes H^{(1)}_1\) |
| Readout feature equation | \((H^{(2)}_1-H^{(2)}_2)/2\) | \(H^{(2)}_1\) |
| First-field metric in (8) | Sum of two squared speeds | One squared speed |
| Initial readout kernel, \(q=\mathbb E[\phi(N(0,m))^2]\) | \(q/2\) | \(q\) |
| Hidden quadratic coefficient | \(d\) from (13) | \(d\) from (14) |
| Readout quadratic coefficient | \(d\) | \(d\) |
| Full quadratic coefficient in feature time | \(2d\) | \(2d\) |

All displayed factors agree with the original physical equations and the respective parameter metrics.

## 9. Required versus optional

**Required:** No corrections identified. All steps needed for the conditional conclusions pass.

**Optional exposition only:**

1. Explicitly define the \(P_{ii}\) in lines 252–253 as the diagonal of the removed projection \(P_H\), rather than its complement.
2. Add “independent of the initial first-coordinate array” to the finite initialization sentence to make the row-conditioning interpretation immediately explicit.
3. Display the physical-time expansion \(\kappa(t)=\kappa(0)+32dt^2+o(t^2)\) if a reader might otherwise mistake the local feature clock for a different nonlaziness claim.

These clarifications do not supply missing mathematical steps under the stipulated initialization and representation premises. The unresolved canonical/global representation obligations remain outside this conditional PASS.
