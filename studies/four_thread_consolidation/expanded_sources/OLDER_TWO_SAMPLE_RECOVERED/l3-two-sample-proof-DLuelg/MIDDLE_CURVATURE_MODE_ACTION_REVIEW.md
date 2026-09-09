# Independent adversarial audit

Candidate: `/tmp/l3-two-sample-proof-DLuelg/MIDDLE_CURVATURE_MODE_ACTION.md`

Exact SHA256 of the candidate read:

```text
13eb30bc81437f27d1c341243f69266ccfd95ff35b887789d9f986663625e473
```

The candidate was read fully, through line 178. This review used only that file and direct mathematical reasoning. No other project, history, review, skill, or mathematical source was read; no experiments or agents were used. Line references below refer to that candidate. The candidate was not edited.

## Verdict

**PASS as a conditional, time-integrated second-moment estimate on the stipulated existing path. No required mathematical correction was found.**

The common scalar coefficients work for both signs; the adjoint identities concern the actual queries; the Hilbert--Schmidt and energy normalizations are consistent; the forward contrast inequality has the required direction; both constants in (8) are valid; and the top comparison gives even the joint weighted bound stated below. No division by a gate, a gate difference, a contrast, or an angle is required. No probabilistic independence or factorization of correlated fields is required.

This verdict uses the ordinary finite-norm interpretation of the displayed L2/operator setup and of an existing regular path. In particular, finite numerical constants require finite initial operator norms. Hilbert--Schmidt increments alone would not establish boundedness of an otherwise unbounded initial operator. Making that convention explicit is optional finding O1 below; it is not an existence conclusion supplied by the proof.

The path, equations (1), energy identity (2), and feature second-moment symmetry are accepted as hypotheses. This audit does not demand that the note construct such a path or establish those hypotheses. It also does not certify any application to raw gradient descent, initialization, finite-width limits, cuts, restart, historical response, or a global theorem.

## Detailed verification

### 1. Scalar gate law and exactly the same coefficients for both signs

For the stated activation and fixed positive e,

\[
p(z)=\frac{e\exp z}{1+\exp z},\qquad
\phi''(z)=\frac{e\exp z}{(1+\exp z)^2}
          =p(z)-\frac{p(z)^2}{e}.
\]

Thus 0 < p < e, 0 < phi'' <= p, and phi >= 1. All three facts used later are valid.

Set A = 1 - (p1+p2)/e and B = p1*p2/e. For either sample index a, letting b denote the other sample,

\[
A p_a+B
=p_a-\frac{p_a^2+p_ap_b}{e}+\frac{p_ap_b}{e}
=p_a-\frac{p_a^2}{e}.
\]

Multiplication by the arbitrary real q_a gives m_a = A delta_a + B q_a. Crucially, A and B have identical values for a=1 and a=2 at the point under consideration. Therefore taking either half-sum or half-difference proves both identities (3) with the displayed coefficients. No interchange of signs or additional factor of two is missing.

Since -1 < A < 1 and 0 < B < e, the weaker closed bounds in the note are valid and give (4). This argument also covers p1=p2 and q1=+q2 or q1=-q2. It never divides by any of these quantities. The division by e is harmless because e=1/10 is fixed.

To check the discussion of the mixed term, write p_+=(p1+p2)/2 and p_-=(p1-p2)/2. The direct expansion is

\[
m_-=(1-p_+/e)\delta_--(p_-/e)\delta_+.
\]

The exact relation

\[
p_+\delta_- -p_-\delta_+=p_1p_2q_-
\]

turns this into (3). For the plus sign the corresponding relation is

\[
p_+\delta_+ -p_-\delta_-=p_1p_2q_+.
\]

Consequently the rewrite really does remove the opposite delta mode. It also changes the coefficient of the same delta mode; the mixed term alone is not equal to B q_-. This is a possible prose clarification, not an error in (3); see O4.

### 2. Actual adjoint queries and the squared inequalities (5)

At each fixed time both delta^(3) samples belong to L2(Omega_3), and the same trained adjoint maps them to L2(Omega_2). Its linearity gives, for either sign,

\[
q^{(2)}_\pm
=\frac{(W^{(3)})^*\delta^{(3)}_1
       \mathbin{\pm}(W^{(3)})^*\delta^{(3)}_2}{2}
=(W^{(3)})^*\delta^{(3)}_\pm.
\]

These are identities for the defined full queries. They do not assume that an operator is independent of the fields to which it is applied. The argument does not commute a gate multiplier with an adjoint.

Equation (4), the triangle inequality, and the adjoint norm bound yield

\[
\|M^{(2)}_\pm\|_2
\le \|\delta^{(2)}_\pm\|_2
   +e\|W^{(3)}\|_{\rm op}\|\delta^{(3)}_\pm\|_2.
\]

Squaring with (x+y)^2 <= 2x^2+2y^2 proves (5). Both factors 2 and the factor e^2 are correct. The coefficients A and B can depend on, and be correlated with, every field here: their pointwise bounds suffice.

### 3. Raw metric and gradient normalization

The differential of the stated objective, evaluated on a variation, has readout term

\[
\langle V^{(3)},\dot W^{(4)}\rangle_3,
\]

matrix terms

\[
\sum_{\ell=2,3}
\left\langle
\frac{\delta^{(\ell)}_1\otimes H^{(\ell-1)}_1
      -\delta^{(\ell)}_2\otimes H^{(\ell-1)}_2}{2},
\dot W^{(\ell)}\right\rangle_{\rm HS},
\]

and first-population term

\[
\frac12\mathbb E_1[
\delta^{(1)}_1\dot Z^{(1)}_1
-\delta^{(1)}_2\dot Z^{(1)}_2].
\]

The adjoint definitions in the note give precisely these matrix and first-population terms. With the specified first-pair metric, its gradient is C(delta^(1)_1,-delta^(1)_2)^T/2, agreeing with (1). There is no extra averaging factor to add to the matrix or readout blocks.

For |rho|<1 the squared first-block gradient norm is

\[
\frac14\mathbb E_1[
(\delta^{(1)}_1)^2+(\delta^{(1)}_2)^2
-2\rho\delta^{(1)}_1\delta^{(1)}_2]
=\frac{1-\rho}{2}\|\delta^{(1)}_+\|_2^2
 +\frac{1+\rho}{2}\|\delta^{(1)}_-\|_2^2.
\]

At rho=-1, differentiating along the single coordinate (Z,-Z) gives gradient delta^(1)_+, with squared norm ||delta^(1)_+||_2^2. Equation (1), using C with rho=-1 without attempting to invert it, gives the same pair of velocities. Thus the separately prescribed degenerate metric is consistent. The endpoint rho=1 is not included by the hypotheses and is not proved by this audit.

The readout contribution is ||(W^(4))'||_2^2 = kappa_3. Hence the raw squared norm contains each matrix Hilbert--Schmidt squared norm with coefficient one, plus nonnegative first and readout contributions. This verifies the normalization needed to discard those other blocks in (7). It checks consistency of the assumed chain rule; it does not derive path existence from a formal gradient computation.

### 4. Hilbert--Schmidt expansion and symmetry in (6)--(7)

Expanding delta_1=delta_++delta_-, delta_2=delta_+-delta_-, H_1=U+V, and H_2=U-V gives

\[
\frac{\delta_1\otimes H_1-\delta_2\otimes H_2}{2}
=\delta_-\otimes U+\delta_+\otimes V.
\]

For the tensor normalization specified in the note,

\[
\langle u\otimes v,\widetilde u\otimes\widetilde v\rangle_{\rm HS}
=\langle u,\widetilde u\rangle\langle v,\widetilde v\rangle.
\]

Consequently the cross term before using symmetry is exactly

\[
2\langle\delta_-,\delta_+\rangle\langle U,V\rangle.
\]

The source-population inner product is

\[
\langle U,V\rangle
=\frac{\mathbb E[H_1^2]-\mathbb E[H_2^2]}4=0.
\]

The hypotheses supply this equality on Omega_1 and Omega_2, exactly the two source populations needed for ell=2 and ell=3. No orthogonality of delta_+ and delta_-, and no symmetry on Omega_3, is used. Equation (6) is therefore exact.

The product in the Hilbert--Schmidt inner-product formula is a property of rank-one operators between Hilbert spaces. It is not an assumption that trained random fields factor probabilistically.

Since U>=1 pointwise and each underlying measure is a probability measure, ||U||_2^2>=1. Adding the two block lower bounds and integrating gives all four terms of (7) with coefficient one. Their sum, rather than just each term separately, is controlled by the energy g(S). Also g(S)>=0 follows from the assumed nonnegative energy, so all subsequent uses of it as an upper bound are legitimate.

The finite normalization remark at lines 36--37 is consistent with empirical averaging: on a source population of n equally weighted points, u tensor v has coordinate matrix uv^T/n. If source and target sizes differ, each adjoint uses its own averaging normalization. No claim about convergence or finite residual modes follows from this remark or is used here.

### 5. Trained operator bounds

Under the stated regular-path convention, the operator increment is the time integral of the Hilbert--Schmidt derivative. Therefore

\[
\begin{aligned}
\|W^{(\ell)}(s)-W^{(\ell)}(0)\|_{\rm op}
&\le\int_0^s\|(W^{(\ell)})'(r)\|_{\rm HS}\,dr\\
&\le\sqrt{s}\left(\int_0^s\|(W^{(\ell)})'(r)\|_{\rm HS}^2\,dr\right)^{1/2}\\
&\le\sqrt S\,g(S)^{1/2}\le\sqrt S.
\end{aligned}
\]

Thus the displayed M_ell is valid uniformly in time. The bound uses the energy once, with its square root before the final g(S)<=1 simplification. It does not mistakenly place g(S), rather than sqrt(g(S)), at this step.

The initial operator need not itself be Hilbert--Schmidt. A bounded initial operator plus a Hilbert--Schmidt increment suffices. Conversely, a Hilbert--Schmidt increment does not make an unbounded initial operator bounded. See O1 for explicit wording of the finite-norm and regularity conventions.

### 6. Forward contrast inequality

The two preactivations on Omega_2 satisfy

\[
\frac{Z^{(2)}_1-Z^{(2)}_2}{2}=W^{(2)}V^{(1)}.
\]

Since sup |phi'| <= e, the pointwise Lipschitz inequality on Omega_2 gives

\[
|V^{(2)}|\le e|W^{(2)}V^{(1)}|.
\]

Taking norms in their respective populations yields

\[
\|V^{(2)}\|_{L^2(\Omega_2)}
\le e\|W^{(2)}\|_{\rm op}\|V^{(1)}\|_{L^2(\Omega_1)},
\qquad
\kappa_2\le e^2M_2^2\kappa_1.
\]

The half-difference factors cancel correctly. The comparison goes in precisely the direction required to control the kappa_2-weighted middle-plus term by the kappa_1-weighted energy term. Neither invertibility nor positivity of W^(2), nor a coupling or independence of the two populations, is needed.

### 7. Both squared time-integrated constants in (8)

Define the four nonnegative action terms

\[
\begin{aligned}
a&=\int_0^S\|\delta^{(2)}_-\|_2^2\,ds,&
b&=\int_0^S\|\delta^{(3)}_-\|_2^2\,ds,\\
c&=\int_0^S\kappa_1\|\delta^{(2)}_+\|_2^2\,ds,&
d&=\int_0^S\kappa_2\|\delta^{(3)}_+\|_2^2\,ds.
\end{aligned}
\]

Equation (7) says a+b+c+d <= g(S). Directly from (5),

\[
\int_0^S\|M^{(2)}_-\|_2^2\,ds
\le 2a+2e^2M_3^2b
\le 2(1+e^2M_3^2)g(S).
\]

For the plus mode, multiplication by the nonnegative kappa_2 is legitimate even when it is zero. The forward inequality then gives

\[
\begin{aligned}
\int_0^S\kappa_2\|M^{(2)}_+\|_2^2\,ds
&\le 2\int_0^S\kappa_2\|\delta^{(2)}_+\|_2^2\,ds
 +2e^2M_3^2d\\
&\le 2e^2M_2^2c+2e^2M_3^2d\\
&\le 2e^2(M_2^2+M_3^2)g(S).
\end{aligned}
\]

These are exactly the constants printed in (8). Bounding each nonnegative action term by g(S) makes them conservative but does not invalidate them. There is no missing e^2, square on an operator norm, factor 2, or factor S.

The displayed quantities are integrals of squared spatial norms. They are not squares of time integrals. A subsequent estimate of a time integral by this action would in general introduce a time-length factor through Cauchy--Schwarz; the note does not claim otherwise.

### 8. Top comparison, including the joint bound

For any two scalar preactivations,

\[
\phi''(x)-\phi''(y)
=(p(x)-p(y))\left(1-\frac{p(x)+p(y)}e\right).
\]

The second factor has absolute value at most one. This proves the difference comparison at line 146. Also 0 <= phi'' <= p proves the sum comparison, because both summands on each side are nonnegative before multiplication by the common readout.

Let T_- and T_+ denote the two top curvature fields displayed at lines 149--152. With W^(4) common to both samples, even when it changes sign over Omega_3,

\[
|T_-|\le |\delta^{(3)}_-|,
\qquad |T_+|\le |\delta^{(3)}_+|.
\]

The absolute values correctly account for the readout sign. Every half-sum or half-difference retains the factor 1/2 on both sides. Consequently the stronger, unambiguous joint formulation is valid:

\[
\int_0^S\left(\|T_-\|_2^2+\kappa_2\|T_+\|_2^2\right)ds
\le\int_0^S\left(\|\delta^{(3)}_-\|_2^2
                   +\kappa_2\|\delta^{(3)}_+\|_2^2\right)ds
\le\int_0^S\|(W^{(3)})'\|_{\rm HS}^2ds
\le g(S).
\]

No extra factor 2 is needed here. Top-population second-moment symmetry is not a hidden premise; only the source symmetry on Omega_2 enters the matrix-gradient estimate.

### 9. Zero contrast, inverse constants, and dependence

All appearances of kappa_1 and kappa_2 are as nonnegative multipliers or on the forward side of kappa_2 <= e^2 M_2^2 kappa_1. The proof does not invert that inequality. If kappa_1=0 at a time, it implies kappa_2=0 at that time; if only kappa_2=0, the middle-plus weighted integrand is zero. No division or cancellation by zero is involved. Finiteness of the fields comes from the regular L2 setup, not from a lower bound on either contrast.

The proof also does not divide by p_a, p1-p2, 1-rho, or 1+rho. Although the first-pair metric is stated using C^(-1) in the nondegenerate case, the estimates use only the nonnegative matrix-block portion of the stipulated total energy. No inverse-angle factor is introduced into (8).

With e fixed, the displayed constants depend on S and the two displayed initial operator norms. This is uniform in contrasts with those quantities held bounded. It is not a separate proof that the initial operator norms remain uniformly bounded in some externally specified angle-dependent family, or that the energy hypothesis holds uniformly in such a family.

The weighted plus estimate supplies no unweighted plus estimate at zero or very small contrast. The note does not assert one. At S=0 both integrated conclusions are zero, with no exceptional algebra needed.

### 10. Scope audit

- The opening description correctly states an estimate conditional on an existing regular path, exact equations, energy, and stipulated sample symmetry. Neither the proof nor this review treats these as an existence theorem.
- The title and the references to ACTUAL modes are supported for the explicitly defined local gate-curvature fields phi''(Z)q and the analogous top fields. They do not identify these fields with the complete Hessian or complete historical response.
- The assertion that there is no mode conversion in (4) is correct as a statement about which delta and query signs appear. The common coefficients still depend on both samples; the claim does not establish dynamically independent modes.
- The claim that no factorization of correlated random variables is used is correct. The bounded scalar multipliers, shared linear adjoint, and Hilbert--Schmidt rank-one identity suffice.
- The finite-population normalization remark is only a normalization remark. No finite-width identification, limit, or residual-mode identity is established or needed.
- The no-inverse-contrast statement is correct within the displayed dependence on initial norms and S. It does not remove the need for the assumed energy and symmetry.
- The top statement is valid even when read as a single bound on the sum of the two weighted squared actions.
- The exclusions at lines 167--172 are appropriate. An L2 action bound alone does not bound multiplication by the curvature field on every L2 input: that would require control of the multiplier in L-infinity. Nor does this action bound alone provide the L2 norm of a product with another correlated L2 field, an exponential moment, a signed variational inequality, or a historical response estimate. No Osgood or global-path conclusion has been smuggled in.
- The final paragraph correctly leaves equations (1)--(2) and symmetry as hypotheses. The caution about internal query cuts supplies no extra premise to this proof and no preservation theorem for a cut dynamics. Particular cuts are not defined here, so no result about a specific cut scheme is verified by this review.
- The references to an original raw GD program, Gaussian initialization, autonomous restart, other observables, and nonlazy/nonlinear requirements are statements of matters not discharged. None is used to prove (8). With external material expressly out of scope, this review does not certify correspondence to those programs or any claim of novelty implied by the word "new."

## Required findings

**None for the stated conditional lemma in its ordinary regular L2/bounded-operator interpretation.** No scalar or modal identity needs repair, no energy factor needs repair, and neither constant in (8) is too small. No additional independence, contrast lower bound, top symmetry, or path-existence premise is needed for the proof presented.

## Optional findings

### O1. State finite initial norms and the integration regularity explicitly

For maximum standalone precision, lines 10--12 and 28 can explicitly say that the initial W^(2) and W^(3) are bounded L2 operators, the fields have finite indicated L2 norms, and the operator increments are absolutely continuous in the Hilbert--Schmidt norm with the derivatives in (1). These are the standard conventions under which the displayed norm and path calculations are meaningful.

This suggestion must not be read as a demand to construct a path or prove these hypotheses. The point is only that Hilbert--Schmidt increments, considered in isolation, do not establish bounded initial operators, and an unspecified weak path notion would not automatically justify the integral representation at lines 108--111. If the author intended to admit unbounded initial operators or a path without that integration property, the finite quantitative conclusion would need those assumptions added; this audit does not certify that broader interpretation.

### O2. Make two local scope statements explicit

At line 47, append "for ell=1,2" to the orthogonality assertion. Its context already supplies precisely those populations, and those are the only ones used. This avoids an accidental reading that symmetry on Omega_3 has also been assumed or proved.

At lines 154--155, display the joint top bound from section 8 of this review. The existing wording is supportable, but the explicit sum removes ambiguity about whether the energy bounds each term separately or their sum. Both are true, with the joint version stronger.

### O3. The two constants in (8) can both be halved

This is an improvement, not a correctness repair. Before using the loose square bound in (5), apply Cauchy--Schwarz to

\[
\|M^{(2)}_-\|_2
\le \|\delta^{(2)}_-\|_2+eM_3\|\delta^{(3)}_-\|_2.
\]

It gives

\[
\|M^{(2)}_-\|_2^2
\le(1+e^2M_3^2)
   (\|\delta^{(2)}_-\|_2^2+\|\delta^{(3)}_-\|_2^2).
\]

For the plus mode the forward inequality gives

\[
\sqrt{\kappa_2}\|M^{(2)}_+\|_2
\le eM_2\sqrt{\kappa_1}\|\delta^{(2)}_+\|_2
   +eM_3\sqrt{\kappa_2}\|\delta^{(3)}_+\|_2,
\]

and hence

\[
\kappa_2\|M^{(2)}_+\|_2^2
\le e^2(M_2^2+M_3^2)
 (\kappa_1\|\delta^{(2)}_+\|_2^2
 +\kappa_2\|\delta^{(3)}_+\|_2^2).
\]

Integrating and using (7) yields the optional sharpened bounds

\[
\int_0^S\|M^{(2)}_-\|_2^2ds
\le(1+e^2M_3^2)g(S),
\qquad
\int_0^S\kappa_2\|M^{(2)}_+\|_2^2ds
\le e^2(M_2^2+M_3^2)g(S).
\]

This sharpening also uses no division by contrast and adds no premise. The constants actually printed in the candidate remain valid.

### O4. Describe the entire mixed-expression rewrite

At lines 160--164, "rewrites the expression using only the same delta mode and the same reverse-query mode" would be more literal than saying that the mixed term is replaced by the reverse query. Equation (3) also adjusts the delta coefficient, as shown in section 1 of this review. The displayed proof already handles that adjustment exactly.
