# Addendum: bounded derivatives, linear growth, and an unrounded coefficient exponent

New derivation 2026-09-08. This extends `/tmp/broad_activation_class_findings.md`. It replaces boundedness of psi by bounded first two derivatives plus control at zero, and gives a direct raw-moment proof avoiding normalization by a small inactive variance. It retains the mathematical source dependencies listed in that file; no prior review outcome is a premise.

## 1. Class and exact threshold

Let

\[
\mathcal A=\{\psi\in C^2(\mathbb R):
|\psi(0)|\le1,\quad\|\psi'\|_\infty\le1,
\quad\|\psi''\|_\infty\le1\}.
\]

Then \(|\psi(z)|\le1+|z|\). Assume psi is not globally affine; bounded nonconstancy is replaced by this exact requirement. Set

\[
\eta_\psi=\min_{1/\sqrt{404}\le\nu\le260}
\inf_{\alpha,\beta}E[\psi(\nu G)-\alpha-\beta\nu G]^2>0.
\]

The fixed interval is proved in the preceding note. Positivity follows from full Gaussian support and global nonaffinity. Continuity of the Gaussian regression formula follows by dominated convergence using \(|\psi(\nu G)|\le1+260|G|\), including integrands with G and squared psi. Consequently no boundedness or tail-limit assumption is needed here.

Let C0,Cz,Cg,H be the constants in Section 5 of the preceding note, and put \(\bar H=H^2\). Define

\[
c_{\rm primal,\psi}=\min\left\{\frac14,
\frac1{2C_0(8\sqrt2)^3},
\frac1{4C_g(8\sqrt2)^{11/4}},
\frac{\sqrt{\eta_\psi}}{4C_z(8\sqrt2)^{7/2}}\right\},
\]

\[
c_{\rm source}=\tfrac12\,24^{-31/4}\bar H^{-46},
\qquad c_\psi=\min\{c_{\rm primal,\psi},c_{\rm source}\}.
\]

Subject to the existing power-four affine/source coefficient inequalities cited in the preceding note, the full two-sample L3 theorem, with precisely its original architecture, initialization, metric and raw GD, holds for

\[
\boxed{\phi(z)=az+e\psi(z),\quad a\in[1/2,1],
\quad0<e\le c_\psi\delta^{31/8},\quad|\rho|\le1-\delta.}
\]

The exponent 31/8 simply retains the existing source estimate's power count \(19+12=31\), rather than rounding it to 32 and then delta to the fourth power. It does not constitute a new stronger source estimate. The fourth-power version is included because \(\delta^4\le\delta^{31/8}\) for \(0<\delta\le1\).

There are two separate improvements: the scalar shape class is now all nonaffine C2 functions with bounded first two derivatives, after normalization; and the sufficient exponent is stated without rounding. The universal prefactor remains extremely small, even with the lighter direct source restriction. This is not a practical-mixing result.

## 2. Direct same-state forcing with linear growth

Work on a common raw primal ball of radius \(b\ge1\), with first projections, A,B and C each bounded by b. Take \(e\le1/4\). Write a subscript 0 for the affine field evaluated at this same state. Triangle inequalities give

\[
\|h_e^1\|\le\tfrac32b,\quad
\|h_e^2\|\le\tfrac{17}{8}b^2,\quad
\|h_e^3\|\le\tfrac{93}{32}b^3<4b^3,
\]

where, for example, \(\|h_e^1\|\le(5/4)b+1/4\), and then
\(\|h_e^2\|\le(5/4)(3b^2/2)+1/4\le17b^2/8\).

The same-state forward discrepancies satisfy

\[
\|h_e^1-h_0^1\|\le2eb,
\quad\|h_e^2-h_0^2\|\le\tfrac92 eb^2,
\quad\|h_e^3-h_0^3\|\le\tfrac{61}{8}eb^3.
\]

For the last bound, propagate the preceding discrepancy with norm b and bound the new term by \(e[1+(17/8)b^3]\), giving \((9/2+25/8)eb^3=61eb^3/8\).

The cap gate always obeys \(\|D_R(z,q)\|\le(a+e)\|q\|\le5\|q\|/4\), without using a sign of psi-prime. Thus

\[
\|\delta_e^3\|\le\tfrac54 b,\quad
\|\delta_e^2\|\le\tfrac{25}{16}b^2,
\]
\[
\|\delta_e^3-\delta_0^3\|\le eb,
\quad\|\delta_e^2-\delta_0^2\|\le\tfrac94 eb^2,
\quad\|\delta_e^1-\delta_0^1\|\le\tfrac{61}{16}eb^3.
\]

Expand each outer product with the nonlinear forward factor and affine backward factor. Since the controls have l1 norm one, the four raw update differences are bounded, respectively, by

\[
\tfrac{61}{16}eb^3,\quad
\left(\tfrac94\tfrac32+2\right)eb^3
=\tfrac{43}{8}eb^3,
\]
\[
\left(\tfrac{17}{8}+\tfrac92\right)eb^3
=\tfrac{53}{8}eb^3,\quad\tfrac{61}{8}eb^3.
\]

Their sum is \(375eb^3/16<24eb^3<40eb^3\). Thus the exact old raw forcing constant 40 survives; no C3 assumption is introduced.

Only the affine field is differentiated in the comparison, so the old integrated affine Hessian estimate yields the unchanged

\[
E_{\rm raw}\le C_0 e\lambda^{-3},\qquad
\lambda=a^3\sqrt v,\quad v=(1+y_1y_2\rho)/2.
\]

This closes the radius-one tube under the first primal restrictions stated above.

## 3. Forward and prediction bounds with the old numerical constants

Across the nonlinear and affine states in the tube, direct action expansions give

\[
\|z_e^1-z_0^1\|\le E,
\quad\|z_e^2-z_0^2\|\le2bE+2eb^2,
\]
\[
\|z_e^3-z_0^3\|\le3b^2E+\tfrac92 eb^3.
\]

The old affine tube bounds are \(b^2\le235M^2\), \(b^3\le3600M^3\), where

\[
M=(3/(\sqrt2\lambda))^{1/4},\quad M^2<1.5\lambda^{-1/2},
\quad M^3<1.84\lambda^{-3/4}.
\]

Therefore the last line is bounded by
\((1057.5C_0+29808)e\lambda^{-7/2}\), which is smaller than
\(C_z e\lambda^{-7/2}\), since \(C_z=1500C_0\) and \(C_0\) exceeds the required numerical constant. The lower layers obey the same upper bound. This verifies the old Cz despite the extra growth term.

At a common state, the projected prediction perturbation is at most
\(8eb^4\). The affine state comparison retains its factor lambda:
\(|g_0(\Theta_e)-g_0(\Theta_0)|\le\lambda b^3E\).
Using \(b^4\le235^2M^4\), \(M^4=3/(\sqrt2\lambda)<2.122\lambda^{-1}\), and \(\lambda\le1\), their sum is below

\[
(10^6+6624C_0)e\lambda^{-11/4}
< C_g e\lambda^{-11/4},\qquad C_g=14400C_0.
\]

Hence the same numerical primal restrictions give \(g_{e,R}(S)\ge5/4\). The two-Lipschitz square-root regression estimate from the preceding note remains valid because psi is one-Lipschitz. It yields activation regression error at least \(e^2\eta_\psi/4\) throughout the feature interval. All these comparisons are cap uniform.

## 4. Raw learned moments avoid the inactive-variance issue

One must not infer \(e/\sqrt\delta\lesssim eM^4\) for the *intrinsic* M above: when \(v\) approaches one, the inactive variance \(1-v\) can be arbitrarily small while M stays bounded. The crude S-inverse norm bound in the old normalized-gates note only proves that statement with its global delta envelope, not with this intrinsic M. No such inverse is needed for the original-time source coefficients.

Use the typed Qf,Qb bases from the preceding note, without normalizing by S. Their norm conversion costs are fixed numerical constants. Across the actual nonlinear and affine states,

\[
\|\Delta h^1\|\le E+2eb,\qquad
\|\Delta\delta^3\|\le E+eb,
\]
\[
\|\Delta h^2\|\le2bE+\tfrac92eb^2,\qquad
\|\Delta\delta^2\|\le2bE+\tfrac94eb^2.
\]

The second backward inequality follows by first expanding B-star times delta3 and then adding its local e-weighted gate term. These bounds require only \(b\le16M\) and \(E\le C_0e\lambda^{-3}\le C_0eM^{12}\).

For each Gram entry, \(|\langle u,u'\rangle-\langle v,v'\rangle|\) is bounded by the sum of two products with one discrepancy factor. The forward h1 and backward delta3 Grams therefore have error
\(C(bE+eb^2)\); the forward h2 and backward delta2 Grams have error
\(C(b^3E+eb^4)\). Explicitly the largest coefficient from the displayed factors is below 15 before the harmless two-slot conversions. A single bound

\[
32(b^3E+eb^4)h_j
\le32(4096C_0+65536)eM^{15}h_j
\le\bar H eM^{15}h_j
\]

covers every learned coefficient discrepancy, including the control factor (which has magnitude 1/2). Only strict learned terms carry h_j, exactly as in the source formulas. The total original feature duration satisfies \(S\le M^4\), so the corresponding backward row error is at most \(\bar H eM^{19}\).

This establishes the needed intrinsic learned-moment input directly, with no small inactive denominator, no assumption on random sample-gate diagonality, and no unproved estimate on a normalized nonlinear remainder. It applies to both the bounded and linear-growth shape classes.

## 5. Source values with linear growth: the self terms have the same powers

On the power-four sector box, replace H by the enlarged \(K=\bar H\). The already proved affine/source transfers then obey

\[
|R_i|_r,|L_i|_r\le K^2M^5,\quad
|F|_r,|V|_r,|U_{\rm top}|_r\le K^3M^4,
\]
\[
|B_2|_r\le K^2M^9,\quad|B_3|_r\le K^2M^7,
\quad|EH_c|_r\le KM^4.
\]

Primitive Gaussian standard deviations in their source order are at most
\(K,KM^2,KM,KM,KM^2\). The exact source identities remain

\[
Z_1=R_1Z_{1,0}+(F/a)\zeta_1
+e(F/a^2)[d_1+aB_2\psi(Z_1)],
\]
\[
Z_2=R_2\xi_2+(V/a)\zeta_2
+e(V/a^2)[d_2+aB_3\psi(Z_2)],
\]
\[
Z_3=R_{\rm top}\xi_3+eU_{\rm top}[d_3+aEH_c\psi(Z_3)].
\]

Here \(|d_j|\le|q_j|\), and
\(q_1=\zeta_1+B_2(aZ_1+e\psi(Z_1))\), with the analogous formulas for q2 and C. For \(p\ge2\), write Zjp for the supremum of individual Lp norms, not the norm of a random time supremum.

At the bottom, \(|\psi(Z)|\le1+|Z|\) gives

\[
\|q_1\|_p\le KM^2\sqrt p+2K^2M^9Z_{1p}+eK^2M^9,
\]

so the nonlinear bracket is bounded by
\(KM^2\sqrt p+3K^2M^9Z_{1p}+2K^2M^9\).
Multiplying by the row bound \(4K^3M^4\) for F/a2 shows that its self coefficient is at most \(12eK^5M^{13}\). The remaining forcing terms are at most

\[
K^3M^5\sqrt p+2K^4M^6\sqrt p
+4eK^4M^6\sqrt p+8eK^5M^{13}.
\]

For K at least 100 and \(eK^{22}M^{19}\le1\), this is at most \(K^6M^6\sqrt p\), and the self coefficient is at most \(eK^6M^{13}\). Thus the old bottom inequality remains valid.

At the middle the identical calculation replaces the backward row exponent 9 by 7 and gives self coefficient at most \(12eK^5M^{11}\). Its direct forward source has power \(5+1=6\), hence

\[
Z_{2p}\le K^6M^6\sqrt p+eK^6M^{11}Z_{2p}.
\]

At the top, the bracket is bounded by \(3KM^4Z_{3p}+2KM^4\), so its self coefficient is at most \(3eK^4M^8\); the direct forward source has power \(5+2=7\). Thus

\[
Z_{1p}\le K^6M^6\sqrt p+eK^6M^{13}Z_{1p},
\quad Z_{3p}\le K^6M^7\sqrt p+eK^6M^8Z_{3p}.
\]

Under the stated source smallness all three self coefficients are below 1/2. Absorption yields exactly the old moment exponents:

\[
\|q_1\|_p\le K^{10}M^{15}\sqrt p,\quad
\|q_2\|_p\le K^{10}M^{13}\sqrt p,\quad
\|C\|_p\le K^{10}M^{11}\sqrt p.
\]

The direct raw primal L2 bounds remain \(KM^3,KM^2,KM\), because h and delta obey the same ball envelopes. These are the smaller norms used after bounding the perturbative exponential, as in the existing response proof.

## 6. Response defects, exact numerical closure, and downstream limits

The random gate derivatives depend only on psi-prime and psi-double-prime, whose bounds are unchanged. The old same-array single-insertion identities, the full current returns, the perturbative exponential envelope, and the Cauchy–Schwarz step with actual primal L2 therefore remain unchanged. Section 4 supplies the only learned-moment input that needed extra attention. With K=Hbar the complete defect bound is

\[
q_{\rm def}\le K^{30}eM^{19}
\quad\text{provided }eK^{22}M^{19}\le1.
\]

The existing positive sector supersolution requires
\(q_{\rm def}\le K^{-16}M^{-12}\). It is sufficient to impose

\[
eM^{31}\le\tfrac12K^{-46}.
\]

Indeed then the defect is at most \(K^{-16}M^{-12}/2\), while
\(eK^{22}M^{19}\le K^{-24}M^{-12}/2<1\). Also
\(M\le24^{1/4}\delta^{-1/8}\), so exactly the stated
\(e\le\frac12 24^{-31/4}K^{-46}\delta^{31/8}\) implies the intrinsic restriction. The exponent and prefactor follow from these inequalities, with no unstated lower bound on a mesh step.

For strict amplitude homotopy closure, all bounded-primal comparisons hold on the proposed source box and the supersolution returns bounds strictly inside it. At each fixed cap and sufficiently fine fixed mesh the coefficients depend continuously on e, including linearly growing C2 shapes by the displayed growth/derivative bounds and Gaussian moments. A first exit is contradicted. The previous fixed-program construction and then strong cap removal apply.

The generic conditioning maps are globally Lipschitz C1 at fixed cap, because phi has linear growth and bounded first derivative, while DR has bounded first derivatives. The velocity query proof uses bounded phi-prime and phi-double-prime and its original product-query truncation. The asymmetric cap comparison uses bounded psi-double-prime and unchanged incoming-field subGaussian tails. Thus the first-hit clock, all-time physical existence, nonsymmetric uniqueness/restart and every stipulated GF/GD/path/velocity/adjoint observable limit have the same proofs as the bounded-class note.

The initial-motion proof also extends verbatim with the already checked substitutions: global nonaffinity of C2 psi is equivalent to psi-double-prime not being identically zero, while phi-prime is at least 1/4. At initialization all needed expectations are finite under linear growth. The odd/even decomposition argument in the preceding note gives the same lower kernel bound without assuming psi odd.

## 7. Uniform classes and examples

The natural norm on differences is

\[
\|u\|_* = \max\{|u(0)|,\|u'\|_\infty,\|u''\|_\infty\}.
\]

For \(\nu\le260\), Minkowski and \(|u(z)|\le|u(0)|+\|u'\|_\infty|z|\) give
\(\|u(\nu G)\|_2\le261\|u\|_*\).
Distance to the affine regression subspace therefore gives

\[
|\sqrt{\mathcal R_{\psi+u}(\nu G)}-
\sqrt{\mathcal R_\psi(\nu G)}|\le261\|u\|_*.
\]

For a nonaffine center of norm strictly below one, a ball of radius at most
\(\min\{(1-\|\psi\|_*)/2,\sqrt{\eta_\psi}/522\}\)
stays in the normalized class and has a common regression margin at least \(\eta_\psi/4\). The same activation coefficient c(delta) works throughout that full, nonodd, infinite-dimensional ball.

Unbounded examples already normalized into the class include
\(\psi(z)=\log(1+e^z)\) and \(\psi(z)=\sqrt{1+z^2}\). Their derivative bounds follow directly: softplus has derivative sigmoid in (0,1), second derivative at most 1/4 and value log2 at zero; the square-root shape has derivative z/sqrt(1+z2), second derivative (1+z2)^(-3/2), and value one at zero. The bounded oscillatory, saturating and compact-support examples from the preceding note are all included as well.

For arbitrary global C2 psi with finite first/second derivative bounds and finite value at zero, divide by
\(B=\max\{1,|\psi(0)|,\|\psi'\|_\infty,\|\psi''\|_\infty\}\)
and require eB to satisfy the normalized coefficient restriction. Any affine component of psi is allowed; only a wholly affine psi fails the nonaffinity conclusion.

## 8. Scope of confidence

This addendum proves the extra shape-growth estimates and the raw-moment repair explicitly. It does not independently reprove every inherited power-four affine probe or Gaussian action theorem. The typed equivariance and the old power-four source/sector certificate are the highest-priority independent audit points. The numerical source prefactor has been selected directly from the displayed closure inequalities; if an inherited hidden restriction is found, it must be added explicitly. Finite GF well-posedness, an affine reference trajectory, or a raw-state estimate alone are not asserted to imply the full population limit.
