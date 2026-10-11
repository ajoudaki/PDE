# Narrow reconstruction of nonparallel initial variability

2026-10-11. Internal separate mathematical check; not a promotion review.

## Verdict and input boundary

**The candidate's mathematical conclusions pass this reconstruction.** The argument proves initialized rank and a fixed-test initial derivative small-ball bound, followed by a simultaneous near-zero time interval under the existing source assumptions. It does not prove endpoint variability, future-transcript independence, or a polynomial width onset.

I checked Sections 1–5 and 7 of NONPARALLEL_INITIAL_VARIABILITY.md, its opening quantifiers, the scalar smoothing lemma in Section 2 of WIDTH_UPGRADE.md, and the relevant canonical model, finite-query initialization/fitting statements, and analytic-source interface in the compact paper. The current Section 6 contains the finite-query source application rather than a local ODE construction; I checked that displayed radius and interval substitution as needed to verify the requested same-time conclusion. No optional local ODE route or other active route note was used. The paper's source proposition is an imported result here; its complete cavity proof was not reaudited.

One minor wording correction is advisable: Section 4 says “The second derivative value in (1).” It means **the second run's derivative value**, not a second-order time derivative. The formulas and subsequent argument use the correct first derivative. No source file was edited.

## 1. Nonpolynomial activation and tensor separation

Let \(v_1,\ldots,v_N\) be fixed unit directions, with \(v_i\ne\pm v_j\) for distinct indices. The first activation is holomorphic on a connected strip, has bounded real derivative, and is nonaffine. If its Taylor series at zero terminated, analytic uniqueness would make it a polynomial throughout the strip; a polynomial with bounded real derivative has degree at most one. Hence its Taylor series has arbitrarily high nonzero coefficients.

For \(g\sim N(0,I_d)\), suppose

\[
\mathbb E\left|\sum_{i=1}^N b_i\phi_1(g^\top v_i)\right|^2=0.
\]

Gaussian positive density and continuity make the summed function zero everywhere in \(\mathbb R^d\). Choose a degree \(k\ge N-1\) with nonzero activation Taylor coefficient. Its homogeneous term implies

\[
\sum_i b_i v_i^{\otimes k}=0.
\]

The tensor-independence step is valid even when \(N>d\). For \(j\ne i\), the explicit linear form

\[
\ell_{ij}(x)=
\big(v_i-(v_i^\top v_j)v_j\big)^\top x
\]

vanishes at \(v_j\), while its value at \(v_i\) is
\(1-(v_i^\top v_j)^2>0\). Taking \(\ell_i(x)=v_i^\top x\), the homogeneous polynomial

\[
p_i(x)=\left(\prod_{j\ne i}\ell_{ij}(x)\right)
\ell_i(x)^{k-N+1}
\]

vanishes on every listed direction except \(v_i\). Contracting its symmetric coefficient tensor with the preceding tensor relation gives \(b_i p_i(v_i)=0\). Therefore all \(b_i\) vanish and the first uncentered population feature Gram is strictly positive definite.

The nonparallel condition handles both possible parity obstructions: even activations identify antipodes, and odd activations negate them. No input Gram rank assumption has been inserted.

## 2. All subsequent population Grams and finite-width ranks

If \(C\succ0\), a Gaussian \(Z\sim N(0,C)\) has positive density throughout \(\mathbb R^N\). A linear relation
\(\sum_i b_i\phi_j(Z_i)=0\) almost surely extends by continuity to every \(z\). Varying one coordinate with \(b_i\ne0\) contradicts nonconstancy. Thus the uncentered feature Gram remains positive definite at every later layer. Affine but nonconstant later activations are permitted by this argument.

For exact finite-width rank, the first-layer evaluation vectors span \(\mathbb R^N\), by the already proved absence of a nonzero linear relation. Some \(N\) deterministic row locations therefore give a nonzero determinant. That determinant is a nonzero real-analytic function of the row locations, so its zero set has Lebesgue measure zero. The candidate gives the needed local coefficient-expansion/Fubini justification of this fact. Gaussian row laws are absolutely continuous, hence the first \(N\) rows form an invertible minor almost surely.

Conditioning on a preceding full-column-rank feature matrix gives independent next preactivation rows with positive-definite covariance. The same determinant argument applies to their coordinatewise activation evaluations. Conditional failure has probability zero, and finite-depth induction proves the asserted almost-sure full rank for every individual width \(n\ge N\).

The empirical Gram convergence imported from the fitting proof applies to any fixed augmented finite query list. Its proof uses linear growth and conditional Gaussian moments, not the small-label cap. Thus the candidate correctly separates these initialization assertions from its later small-label/source assertion.

## 3. Centered final-row covariance and uniform fixed-label constants

For the \(m+1\) training-and-test list, let \(C_*=Q^{(L-1)}\succ0\). Given \(Z\sim N(0,C)\), write \(U=\phi_L(Z)\) and

\[
\Sigma(C)=\operatorname{Cov}(U_qU_1,\ldots,U_qU_m).
\]

This centered covariance, not merely the feature Gram, is strictly positive definite for every \(C\succ0\). Indeed, zero variance in a nonzero direction \(e\) would make

\[
\phi_L(z_q)\sum_a e_a\phi_L(z_a)
\]

constant everywhere. By varying a training coordinate with nonzero coefficient, one can choose training-coordinate values at which the sum is nonzero. Varying the independent coordinate \(z_q\) then contradicts nonconstancy. This remains valid for noncentered or unbounded activations.

Gaussian square-root coupling, linear growth and fourth-moment domination imply continuity of \(\Sigma(C)\). Thus a fixed neighborhood \(\mathcal U\) of \(C_*\) can be chosen with
\(\Sigma(C)\succeq\kappa I\), where
\(\kappa=\lambda_{\min}(\Sigma(C_*))/2>0\).

If \(D\) bounds the covariance diagonals, \(b=|\phi_L(0)|\), and \(s=\sup_{\mathbb R}|\phi_L'|\), then

\[
F_6=b+s\sqrt D\,15^{1/6}
\]

bounds each \(\|U_a\|_6\). For every deterministic unit vector \(e\),

\[
X=U_q\sum_a e_aU_a,\qquad
\|X\|_3\le\sqrt m F_6^2,\qquad
\|X-\mathbb EX\|_3\le2\sqrt m F_6^2.
\]

Hence the candidate's uniform bound
\(M_3=8m^{3/2}F_6^6\) and variance lower bound \(\operatorname{Var}X\ge\kappa\) are correct. No coordinate independence is used. Both constants depend on the fixed augmented geometry and activation, but not on the chosen deterministic unit label direction.

## 4. Smoothing estimate, independent shift and numerical gate

For centered iid \(V_i\) with variance \(\sigma^2>0\) and third absolute moment at most \(M\), an independent copy gives

\[
|\mathbb E e^{itV}|^2
\le1-\sigma^2t^2+\frac43M|t|^3.
\]

For \(|t|\le3\sigma^2/(8M)\), this yields
\(|\mathbb E e^{itV}|\le e^{-\sigma^2t^2/4}\).
The Gaussian majorant of an interval, followed by its Fourier integral, gives an inner contribution at most
\(\sqrt2 e^{1/2}h/\sigma<3h/\sigma\). Discarding the characteristic function on the complementary integral gives at most

\[
4\exp\!\left(-\frac{9h^2\sigma^4n}{128M^2}\right).
\]

Thus the stated finite small-ball inequality, including its constants and uniformity in the interval center, is valid.

The canonical normalization is also correct. Since \(w(0)=0\), hidden-feature time derivatives do not contribute to the initial output derivative, and

\[
\dot f_n(0,\sqrt d\,v_q)
=\frac2{mn}\sum_i U_{i,q}\sum_a y_aU_{i,a}
=\frac{2Y}{\sqrt m\,n}\sum_iX_i,
\qquad e=\frac{y}{\sqrt mY}.
\]

Conditioning on the first run through layer \(L-1\) and the entire independent second initialization leaves the first run's last rows iid. The event \(C_n\in\mathcal U\) is measurable under that conditioning. The second run's initial derivative and the first run's conditional row mean are fixed there and contribute only an arbitrary shift in the smoothing inequality. Matching the two means is unnecessary, and no conditioning on the first run's final rows has occurred.

For

\[
h_\delta=\frac{\delta\sqrt\kappa}{24},\qquad
c_\delta=\frac{2h_\delta}{\sqrt m},
\]

the first smoothing term is at most \(\delta/8\). The exponent in its second term is bounded below by
\(\delta^2\kappa^3 n/(8192M_3^2)\). Consequently

\[
n\ge\frac{8192M_3^2}{\delta^2\kappa^3}
\log\frac{32}{\delta}
\]

makes that term at most \(\delta/8\). Adding a covariance-event failure of at most \(\delta/4\) proves the derivative-gap success probability \(1-\delta/2\). The additional width threshold for covariance convergence remains an eventual fixed-problem threshold.

Uniformity of these constants over label directions does not yield one event for all directions. The derivative difference at one test is a scalar linear functional of \(y\), with a nontrivial nullspace when \(m\ge2\). The candidate states this distinction correctly.

## 5. The same-time early window

For the actual scalar difference \(g(t)\), suppose it is holomorphic near the closed disk of radius \(R\), bounded there by \(M\), and satisfies \(g(0)=0\) and \(|g'(0)|\ge a_n\). Cauchy coefficients give

\[
|g(t)-g'(0)t|\le\frac{2Mt^2}{R^2}
\]

for every \(0<t\le R/2\). On that same event, the reverse triangle inequality therefore gives

\[
|g(t)|\ge\frac{a_nt}{2}
\quad\text{for every}\quad
0<t\le\min\{R/2,a_nR^2/(4M)\}.
\]

This is a simultaneous interval statement, not the existence of one witness time.

The actual finite-query source interface in paper/compact_foundations.tex gives holomorphy near
\([-r,T+r]+i[-r,r]\), with

\[
r=\frac1{\lambda\sqrt{\ell}},\qquad
|f_n|\le16\beta^{6L}\frac Y\lambda,\qquad
\ell=\log(en),\quad \lambda=\gamma/m.
\]

The full closed disk \(|t|\le r\) is contained in that rectangle, so no smaller ellipse-derived disk is needed. For two runs,
\(R=r\), \(M=32\beta^{6L}Y/\lambda\), and
\(a_n=c_\delta Y/\sqrt n\) yield exactly

\[
t_n=\min\left\{
\frac1{2\lambda\sqrt\ell},
\frac{c_\delta}{128\beta^{6L}\lambda\sqrt n\,\ell}
\right\}.
\]

For fixed problem and confidence, the second term is eventually smaller and \(t_n\to0\). The two source-event failure budgets \(\delta/4\) and the derivative failure budget \(\delta/2\) sum to \(\delta\), without an independence requirement. The original label cap is sufficient because it is precisely the imported source assumption.

The conclusion excludes \(t=0\), where both outputs vanish. It does not imply a fixed-positive-time lower bound, an endpoint lower bound, or any model-to-dense ratio without a separately suitable numerator estimate.

## 6. Initialized innovation versus a future transcript

At width \(n\ge m+1\), initialized full rank makes the empirical Schur complement in (16) strictly positive. Empirical Gram convergence and continuity of matrix inversion make it converge in probability to the strictly positive population Schur complement. This is valid linear feature-space innovation relative to the initialized training feature span.

Likewise, condition on the preceding initialized layers and a final row's training preactivations. Gaussian regression gives test preactivation variance

\[
C_{qq}-C_{q,\mathrm{tr}}
C_{\mathrm{tr},\mathrm{tr}}^{-1}C_{\mathrm{tr},q}>0.
\]

The conditional law has full real support, so a nonconstant continuous activation has positive conditional variance at every finite conditioned mean. The candidate correctly refrains from a uniform lower bound over all such means.

Neither claim entails survival after conditioning on a complete future training transcript. The actual small-ball proof uses only the permitted initialization conditioning. Section 7 keeps that boundary explicit.

## Final assessment

No substantive defect was found in the requested statements or their constants. The initialized rank and derivative lower bound hold without a label cap; the simultaneous shrinking-time interval uses the original compact source event and retains its eventual-probability qualification. The only suggested edit is the minor “second run's derivative” wording noted above.

## Coordinator resolution

The source now reads “The independent second run's derivative value in (1),”
so the wording issue is resolved without changing the mathematics. The checked
source SHA-256 is
`017c2dcbd3e3b938099ab7dd748a211f859126bd636767b667ef3432386e33bc`.
This resolution note is by the coordinator, not a new independent review.
