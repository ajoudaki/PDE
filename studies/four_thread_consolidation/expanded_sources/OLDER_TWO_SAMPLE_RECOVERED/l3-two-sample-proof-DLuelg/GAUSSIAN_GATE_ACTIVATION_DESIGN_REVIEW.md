# Independent adversarial review of the Gaussian-gate activation design

Reviewed 2026-09-06.

Sole mathematical input: `/tmp/l3-two-sample-proof-DLuelg/GAUSSIAN_GATE_ACTIVATION_DESIGN.md`, read in full (228 lines, 9,992 bytes).

Source SHA-256:

```text
fe7ac18d21022823911c32d3a61447a65f376cf08160f42e76a27ee70ba7b716
```

I independently read and followed `/etc/codex/skills/solve-math-rigorously/SKILL.md` as a procedural instruction. I consulted no prior notes, reviews, project history, or additional mathematical sources, and used no agents or experiments. The calculations below are deductions from the supplied candidate. The candidate was not edited. Source line references below refer to the version with the hash above.

## Verdict and precise scope

**Pass for the stated deterministic fixed-sign, frozen-control tangent lemma and the stated independent-initialization properties. No required mathematical repair was found.**

In particular, the claimed estimate

\[
\|D_{z_0}z(T;z_0,u)\|_{\mathrm{op}}
\le \sqrt{\frac{1+|\rho|}{1-|\rho|}}\,e^6
       (e+U)^{64/(1-|\rho|)},\qquad
U=\frac1{10}\int_0^T\|u(t)\|_1\,dt,
\]

is supported by the proof for every finite initial state, every fixed \(|\rho|<1\), and every prescribed integrable control admitting constant signs \(s_i\in\{-1,1\}\) with \(s_i u_i\ge0\) almost everywhere. The signs may be chosen separately for each control. There is no restriction on changing ratios, number of switches between active coordinates, temporal boundedness, or intervals on which one or both components vanish. The constants contain no initial-state dependence.

The initialization argument also survives the singular first covariance at \(\rho=-1\). Its essential object is the **uncentered feature second-moment matrix**, which becomes positive definite even there. This does not extend the tangent theorem to \(|\rho|=1\).

The verdict concerns the mathematical statements supplied in this file. The comparison with an “existing short-time bootstrap” and with a previous sensitivity obstruction cannot be independently checked under the stipulated isolation: those other arguments were not supplied or consulted. The numerical activation inequalities and the asserted initial nonlinearity properties themselves are verified below. No global mean-field result, trained sign condition, trained control moment estimate, or derivative of a coupled training system is required for this verdict; the candidate explicitly excludes them.

The proof architecture is sound: the reflected covariance supplies a tangent energy; a bounded potential pays for growth in the truncated region; monotonicity of the sum bounds the weighted central occupation; Gaussian decay makes the remaining terms small at logarithmic cutoff scale. I checked the identities and constants independently, including the regularity needed to use them.

## 1. Activation and initialization audit

**Activation bounds (lines 39–55).** For \(v\ge1\), the comparison with \(v e^{-v^2}\) gives

\[
\int_0^\infty e^{-v^2}\,dv
\le 1+\tfrac12e^{-1}<\tfrac32.
\]

Consequently \(|\phi(z)-1|<3/20\), so both the stated interval \((17/20,23/20)\) and the weaker interval \((5/6,7/6)\) are valid. Also

\[
\phi'(z)=\tfrac1{10}e^{-z^2}>0,
\qquad
|\phi''(z)|=\tfrac15|z|e^{-z^2}\le\tfrac1{10},
\]

because \(e^{z^2}\ge1+z^2\ge2|z|\). Repeated differentiation produces polynomial multiples of \(e^{-z^2}\); these are continuous and vanish at both tails, so every fixed positive-order derivative is bounded. The activation itself is bounded as well. These checks require no special convention for the error function.

**Strict Gaussian nonaffinity (lines 57–63).** A scalar Gaussian with positive variance has strictly positive density everywhere. If \(\phi(G)=a+bG\) almost surely, continuity of \(\phi(z)-a-bz\) forces equality for every real \(z\): any nonzero value would persist on an open interval of positive Gaussian probability. This would make \(\phi'\) constant, contrary to its formula. Since \(\phi(G)\in L^2\) and \(\operatorname{span}\{1,G\}\) is finite dimensional and closed in \(L^2\), the best-affine squared error is strictly positive. The proof correctly requires positive scalar variance; it makes no such claim for a constant Gaussian variable.

**Two initial modes (lines 65–85).** Write \(g=\phi-1\). Oddness and symmetry of any centered scalar Gaussian give \(\mathbb E g(G)=0\), including centered Gaussian marginals with variances different from one. Hence

\[
\frac14\mathbb E(\phi(Z_1)+\phi(Z_2))^2
\ge \frac14\bigl(\mathbb E[\phi(Z_1)+\phi(Z_2)]\bigr)^2=1.
\]

For the first pair, \(\operatorname{Var}(Z_1-Z_2)=2(1-\rho)>0\) whenever \(\rho<1\), including \(\rho=-1\). Thus \(Z_1\ne Z_2\) almost surely. Strict monotonicity gives \(\phi(Z_1)\ne\phi(Z_2)\) almost surely, and their bounded squared difference has strictly positive expectation.

At an interior correlation, positive definiteness of the feature second-moment matrix can also be checked directly. If

\[
a\phi(Z_1)+b\phi(Z_2)=0\quad\text{almost surely},
\]

the positive joint density and continuity imply this identity for every \((z_1,z_2)\in\mathbb R^2\). Varying \(z_1\) with \(z_2\) fixed gives \(a=0\); varying \(z_2\) gives \(b=0\). This rules out every nonzero vector in the null space of the second-moment matrix.

**Singular endpoint, explicitly.** At \(\rho=-1\), take \((Z_1,Z_2)=(G,-G)\) and set \(a=\mathbb E[g(G)^2]>0\). The uncentered feature matrix is exactly

\[
M=\mathbb E
\begin{pmatrix}1+g(G)\\1-g(G)\end{pmatrix}
\begin{pmatrix}1+g(G)&1-g(G)\end{pmatrix}
=\begin{pmatrix}1+a&1-a\\1-a&1+a\end{pmatrix}.
\]

Its eigenvalues are \(2\) and \(2a\), both positive. In contrast, the centered feature covariance is

\[
a\begin{pmatrix}1&-1\\-1&1\end{pmatrix},
\]

which is singular. A fresh centered Gaussian weight row has conditional covariance equal to the **uncentered** empirical feature second moment, so the candidate uses the correct matrix. The initial singular Gaussian still has unit marginal variances, and the next Gaussian has positive-definite covariance; there is no use of a positive-density argument on a singular two-dimensional law.

**Finite-width induction and covariance continuity (lines 87–97).** Here is the precise argument behind the candidate's abbreviated induction. Given preceding feature vectors \(V_j\in\mathbb R^2\), let

\[
Q_n=\frac1n\sum_{j=1}^n V_jV_j^\top.
\]

For a fresh matrix with independent \(N(0,1/n)\) entries, a new row field is \(Y_i=\sum_j W_{ij}V_j\). Conditional on all preceding layers, the \(Y_i\) are independent and each has law \(N(0,Q_n)\). The calculation is exact, including when \(Q_n\) is singular.

With \(M_0=23/20\), each product \(\phi(Y_{i,a})\phi(Y_{i,b})\) has absolute value at most \(M_0^2\). Its empirical average has conditional variance at most \(M_0^4/n\). Thus its difference from its conditional mean tends to zero in \(L^2\), and hence in probability. The conditional mean is

\[
\Psi_{ab}(Q_n)
=\mathbb E\bigl[\phi((Q_n^{1/2}\xi)_a)
                  \phi((Q_n^{1/2}\xi)_b)\bigr],
\qquad \xi\sim N(0,I_2).
\]

This function is continuous on the entire positive-semidefinite cone. To check that no hidden nonsingularity condition is being used: if \(Q_m\to Q\), the positive-semidefinite square roots are bounded; every convergent subsequence of them has a positive-semidefinite limit \(B\) with \(B^2=Q\). Uniqueness of the positive-semidefinite square root forces \(B=Q^{1/2}\), so the full sequence of square roots converges. The common \(\xi\) coupling then gives pointwise convergence of the displayed integrand, and its uniform bound gives convergence of expectations. In particular, singular empirical covariances and the singular first population covariance cause no problem.

The same conditional variance argument applies to every bounded continuous test of the new Gaussian pair. Starting with the independent first rows therefore yields the claimed empirical pair laws in probability and the feature-covariance recursion. Positive definiteness persists after the first activation, so all three initial hidden layers have nondegenerate Gaussian marginals and the two strict mode properties. A finite collection of layerwise convergences is joint in probability by the union bound.

Even a reading of “joint” that stacks same-index fields from the finitely many initial layers can be supported by the same argument. For bounded tests \(f\) of earlier fields and \(h\) of the new pair, the conditional mean of

\[
\frac1n\sum_i f(\text{earlier fields at }i)h(Y_i)
\]

is the empirical average of \(f\) multiplied by \(\mathbb E h(N(0,Q_n))\), and the conditional variance is \(O(1/n)\). Induction handles product tests, and tightness and approximation on compact sets handle bounded continuous joint tests. An explicit definition of the intended empirical law would improve presentation, but there is no evident initialization gap under either of these natural forward-field interpretations.

These positivity statements are pointwise in the admissible correlation. They do not assert a lower bound uniform as \(\rho\uparrow1\). Indeed, the Lipschitz bound on \(\phi\) gives

\[
\frac14\mathbb E(\phi(Z_1)-\phi(Z_2))^2
\le\frac{1-\rho}{200},
\]

so such an angle-uniform lower bound would be false. At \(\rho=1\) the antisymmetric mode vanishes; that endpoint is correctly excluded.

## 2. Integrable controls and the initial-state derivative

The existence and differentiability paragraph at lines 101–107 is valid. The following details check that it gives an everywhere-defined initial-state Fréchet derivative with the control fixed, rather than merely formal directional equations.

For fixed \(u\), put

\[
F(t,z)=C\operatorname{diag}(\phi'(z_1),\phi'(z_2))u(t).
\]

Since \(\|C\|_{\mathrm{op}}=1+k\), both a speed bound and a global spatial Lipschitz bound are supplied by the integrable function

\[
L(t)=\frac{1+k}{10}\|u(t)\|_1:
\qquad
\|F(t,z)\|_2\le L(t),\quad
\|D_zF(t,z)\|_{\mathrm{op}}\le L(t).
\]

On a subinterval where \(\int L<1\), the integral-equation map is a contraction on continuous paths with the prescribed starting point. Finitely many such subintervals cover \([0,T]\). Its solution is absolutely continuous because its derivative is bounded in norm by an integrable function. In particular,

\[
\|z(t)-z_0\|_2\le\int_0^T L(s)\,ds=(1+k)U,
\]

so finite-time escape is impossible. Values of the control on null sets have no effect.

For completeness, let \(M_3=\sup_z|\phi'''(z)|<\infty\) and \(M(t)=(1+k)M_3\|u(t)\|_1\). Then

\[
\|D_zF(t,a)-D_zF(t,b)\|_{\mathrm{op}}
\le M(t)\|a-b\|_2.
\]

The integral Lipschitz inequality gives, with \(L_* =\int_0^T L\),

\[
\sup_t\|z(t;z_0+h,u)-z(t;z_0,u)\|_2
\le e^{L_*}\|h\|_2.
\]

This inequality can be obtained by iterating the integral inequality, whose iterated integrals sum to the exponential. Let \(J\) solve

\[
J'=D_zF(t,z(t))J,\qquad J(0)=I_2.
\]

Its integrable coefficient gives a unique absolutely continuous solution by the same integral-equation construction. The Taylor remainder for \(F\) is bounded by \(\tfrac12M(t)\|h\|_2^2\). Applying this along the perturbed trajectory and again iterating the integral inequality yields

\[
\sup_t\|z(t;z_0+h,u)-z(t;z_0,u)-J(t)h\|_2
\le \tfrac12 e^{3L_*}\Bigl(\int_0^T M(t)\,dt\Bigr)\|h\|_2^2.
\]

Thus \(J(t)=D_{z_0}z(t;z_0,u)\) in the Fréchet sense at every \(z_0\). The crude exponential estimate here establishes differentiability only; it is not substituted for the sharper polynomial bound. There is no circular use of the desired estimate.

## 3. Reflection, tangent energy, and signs

For any admissible control choose \(S=\operatorname{diag}(s_1,s_2)\), with each \(s_i\in\{-1,1\}\), and put \(q=(x,y)^\top=Sz\). Since the Gaussian gate is even,

\[
q'=SCS\begin{pmatrix}\alpha e^{-x^2}\\\beta e^{-y^2}\end{pmatrix}
=C_r\begin{pmatrix}A\\B\end{pmatrix},
\qquad r=\rho s_1s_2.
\]

This verifies (3), including opposite signs of the original controls and either sign of \(\rho\). An identically zero component permits either sign choice. The signs depend only on the frozen control, so differentiating the initial state does not differentiate the reflection. Since \(S\) is orthogonal, original and reflected flow derivatives are related by conjugation with \(S\) and have the same Euclidean operator norm.

The reflected variational equation is

\[
\eta'=C_rD\eta,\qquad D=\operatorname{diag}(-2xA,-2yB).
\]

As \(|r|=k<1\), \(C_r\) is positive definite. For \(E=\eta^\top C_r^{-1}\eta\), differentiation almost everywhere gives exactly

\[
E'=2\eta^\top D\eta=-4xA\eta_1^2-4yB\eta_2^2.
\]

There is no omitted cross term. The coordinate estimate used in the candidate follows from the identities

\[
E=\eta_1^2+\frac{(\eta_2-r\eta_1)^2}{1-r^2}
 =\eta_2^2+\frac{(\eta_1-r\eta_2)^2}{1-r^2}.
\]

Therefore \(\eta_i^2\le E\), and

\[
E'\le4(x_-A+y_-B)E=2hE,
\qquad h=2x_-A+2y_-B.
\]

The function \(h\) is integrable: \(|v|e^{-v^2}\) is globally bounded and \(\alpha+\beta\in L^1\). Integrating the scalar energy inequality and using the eigenvalue bounds gives

\[
\|\eta(T)\|_2^2
\le (1+k)E(T)
\le \frac{1+k}{1-k}e^{2I}\|\eta(0)\|_2^2,
\qquad I=\int_0^T h(t)\,dt.
\]

Taking square roots proves the exact prefactor and exponent in (4). All equalities and inequalities here are valid almost everywhere for the absolutely continuous paths; no derivative of the time-dependent controls is used.

## 4. Truncation, occupation, and tail audit

The truncated potential is correctly oriented and bounded. With the source's \(f_Q\), one can write

\[
H_Q(v)=\int_0^{v_-}2a\chi(a/Q)\,da.
\]

Continuity of \(f_Q\) gives \(H_Q\in C^1\), including at zero, with \(H_Q'=-f_Q\). Its bounds follow directly from its support:

\[
0\le H_Q\le\int_0^{2Q}2a\,da=4Q^2,
\qquad 0\le f_Q\le4Q.
\]

Thus \(P=H_Q(x)+H_Q(y)\) lies in \([0,8Q^2]\) for every initial state, including arbitrarily deep negative tails. Because \(H_Q'\) is bounded, composition with an absolutely continuous path obeys the usual chain rule. The candidate never differentiates \(f_Q\), so its piecewise-linear cutoff example introduces no second-derivative difficulty.

The discarded growth is nonnegative and satisfies

\[
0\le 2v_- - f_Q(v)\le2|v|\mathbf1_{\{v\le-Q\}}.
\]

On \([Q,\infty)\), with \(Q\ge1\), the derivative of \(a e^{-a^2}\) is \((1-2a^2)e^{-a^2}<0\). Consequently the discarded part of \(I\) is at most

\[
2Qe^{-Q^2}\int_0^T(\alpha+\beta)\,dt
=2Qe^{-Q^2}U.
\]

This verifies (5), with the normalization of \(U\) intact.

If \(r\ge0\), the full potential derivative is

\[
P'=-[f_Q(x)A+f_Q(y)B]-r[f_Q(x)B+f_Q(y)A].
\]

Both bracketed expressions are nonnegative. Integrating therefore bounds the retained growth by \(P(0)-P(T)\le8Q^2\), exactly as asserted. This case includes \(r=0\).

For \(r=-k<0\), write

\[
R=f_Q(x)A+f_Q(y)B,\qquad
X=f_Q(x)B+f_Q(y)A.
\]

The exact identity is \(P'=-R+kX\), with the signs in (6) correct. Let

\[
\mathcal C_Q=\{t:|x(t)|\le2Q,\ |y(t)|\le2Q\},
\qquad w=x+y.
\]

Then \(w'=\delta(A+B)\ge0\) almost everywhere, and \(\mathcal C_Q\subset\{|w|\le4Q\}\). Set \(p(s)=\max(-4Q,\min(s,4Q))\). The absolutely continuous function \(p\circ w\) has derivative

\[
(p\circ w)'=w'\mathbf1_{\{-4Q<w<4Q\}}
\quad\text{almost everywhere}.
\]

At either boundary level, \(w'=0\) almost everywhere. Indeed, almost every point of a level set is both a density point of that set and a differentiability point of \(w\); difference quotients along other points of that set force the derivative to be zero. At such a point the Lipschitz property of \(p\) also forces \((p\circ w)'=0\). Thus the open strip in the formula may be replaced by the closed strip when integrating \(w'\).

It follows that

\[
\begin{aligned}
\delta\int_{\mathcal C_Q}(A+B)\,dt
&\le\int_0^T\mathbf1_{\{|w|\le4Q\}}w'\,dt\\
&=p(w(T))-p(w(0))\le8Q.
\end{aligned}
\]

This proves (7) for arbitrary absolutely continuous solutions. Neither coordinate has to be monotone. The central square may be entered and left repeatedly; bounding its indicator by that of the sum strip remains valid. Flat portions, infinitely many boundary contacts, and time intervals of zero controls do not introduce an extra term. The estimate controls the weighted occupation \(\int(A+B)\), not the amount of elapsed time, so long pauses do not threaten it.

On \(\mathcal C_Q\), \(X\le4Q(A+B)\), giving

\[
\int_{\mathcal C_Q}X\,dt\le\frac{32Q^2}{\delta}.
\]

Outside \(\mathcal C_Q\), if \(f_Q(x)\ne0\), then \(-2Q<x<0\). It follows that \(|y|>2Q\), and hence

\[
f_Q(x)B\le4Q\beta e^{-4Q^2}.
\]

The symmetric argument gives \(f_Q(y)A\le4Q\alpha e^{-4Q^2}\) outside the central set. Therefore

\[
\int_{[0,T]\setminus\mathcal C_Q}X\,dt
\le4Qe^{-4Q^2}U.
\]

This verifies (8). The decaying factor belongs to the other coordinate's gate in each cross term, exactly as the identity requires. The argument works for a distant positive coordinate as well as a distant negative one. Boundary equality \(|x|=2Q\) or \(|y|=2Q\) is harmless: the central set includes its boundary and \(f_Q(\pm2Q)=0\).

Finally,

\[
\int_0^T R\,dt
=P(0)-P(T)+k\int_0^T X\,dt
\le8Q^2+k\int_0^T X\,dt.
\]

Adding the discarded growth gives precisely

\[
I\le\left(8+\frac{32k}{\delta}\right)Q^2
       +4kQe^{-4Q^2}U+2Qe^{-Q^2}U.
\]

Every dependence on a possibly large initial coordinate has been eliminated: the endpoint potential is uniformly bounded, the central integral is controlled by the range of the clamped sum, and both remaining terms are bounded using the control cost. I found no unbounded initial-potential term concealed in (9).

## 5. Cutoff constants and probability consequence

Let \(E_0=e+U\) and \(Q=\sqrt{2\log E_0}\). Then \(E_0\ge e\) and \(Q\ge\sqrt2\), so all preceding cutoff estimates apply, including when \(U=0\). Also

\[
Qe^{-Q^2}U=\frac{QU}{E_0^2}\le\frac{Q}{E_0}\le1.
\]

The last inequality is justified by \(2\log E_0\le E_0^2\); the function \(t^2-2\log t\) is positive at \(t=1\) and nondecreasing for \(t\ge1\). The faster tail is no larger, so the sum of tail contributions is at most \(4k+2\le6\). The potential contribution is

\[
\left(8+\frac{32k}{\delta}\right)Q^2
=\left(16+\frac{64k}{\delta}\right)\log E_0,
\]

and

\[
16+\frac{64k}{\delta}
=\frac{16+48k}{\delta}\le\frac{64}{\delta}.
\]

Thus \(I\le6+(64/\delta)\log(e+U)\). For \(r\ge0\), the earlier estimate gives the stronger intermediate bound \(I\le16\log(e+U)+2\), which is also covered by the same final expression. Combining with the energy estimate proves (2) with the exact stated constants. No optimization over an initial-state-dependent quantity is being performed.

The result is a finite-power bound in the control cost for each fixed \(\rho\); its exponent need not be an integer. If “polynomial” is interpreted as requiring an integer degree, replacing \(64/\delta\) by its ceiling gives such a polynomial upper bound because \(e+U\ge1\). This is a terminological clarification, not a defect in the estimate.

For a measurable random initial point and a measurable random \(L^1\) control satisfying the sign premise almost surely, the pointwise bound gives, for every \(q>0\),

\[
\mathbb E\|J(T)\|_{\mathrm{op}}^q
\le\kappa^{q/2}e^{6q}
   \mathbb E(e+U)^{64q/\delta}.
\]

Here \(\rho\) is fixed, as in the deterministic statement. The initial point may have arbitrary dependence on the control; it requires no moment assumption of its own. The derivative has been established at every initial point, so there is no exceptional set in the initial state that a dependent random control could select. Ordinary measurability of the flow and its frozen derivative follows from their integral equations, using the integrable coefficient bounds and continuity in the initial state and in the \(L^1\) control. No adaptedness assumption is needed for this pathwise statement.

## 6. Adversarial edge cases and scope checks

I checked the following potential failure mechanisms analytically:

- **Zero cost and zero horizon.** If \(U=0\), then \(u=0\) almost everywhere, the flow is the identity, and its derivative is \(I_2\). The cutoff remains defined and the stated right-hand side is at least one. The same conclusion holds on a zero-length interval.
- **One component vanishes, including on arbitrary measurable sets.** Every identity remains meaningful; there is no division by a control component, by \(A+B\), or by a ratio of controls. An identically zero coordinate can be assigned either fixed sign.
- **All four sign assignments and either sign of \(\rho\).** Reflection uses evenness of \(\phi'\), not evenness of \(\phi\). It yields either \(r\ge0\) or \(r=-k<0\), both treated. The constants depend on \(|\rho|\) only.
- **Unbounded or highly concentrated integrable controls.** The solution and tangent have absolutely continuous paths and integrable coefficients. All estimates are integral estimates. No boundedness, continuity, piecewise constancy, or derivative of \(u\) is needed.
- **Infinitely changing ratios or alternating active coordinates.** The proof counts neither ratio changes nor visits to the central square. It uses only nonnegativity of \(A,B\) and their sum in the monotone coordinate. This is the part that permits arbitrary ratio variation.
- **Initial coordinates arbitrarily far into any tail.** The saturated potential remains in \([0,8Q^2]\); the discarded self-growth and the cross terms outside the square are charged to Gaussian tails times \(U\). Cancellation of large opposite coordinates in \(x+y\) does not cause a gap, since such a point is handled by the outside-square estimate.
- **Correlation endpoints.** The initialization assertion includes \(\rho=-1\) and handles it separately. The tangent energy requires \(|\rho|<1\), exactly as stated. No constant is claimed uniform as \(|\rho|\uparrow1\), and no positivity is claimed at \(\rho=1\).
- **Singular empirical covariance during initialization.** The conditional Gaussian representation and covariance-to-expectation continuity apply to positive-semidefinite matrices without any positive lower eigenvalue. The limiting positive definiteness is established separately.
- **Dependence of the realized control on the initial point.** Evaluation of the frozen derivative at a dependent pair \((z_0,u)\) is covered. Differentiation of the map that also changes \(u\) is a different operation and is explicitly excluded.

For the last distinction, a simultaneous first variation of the state and the control satisfies

\[
\delta z'
=C\operatorname{diag}(u_i\phi''(z_i))\,\delta z
 +C\operatorname{diag}(\phi'(z_i))\,\delta u.
\]

The candidate bounds the homogeneous propagator with the control frozen. It supplies no estimate on the additional forcing or on a feedback law producing \(\delta u\). Likewise, genuinely sign-changing prescribed controls do not admit the single constant reflection used in the proof. The candidate makes both limitations explicit. The root's work on actual trained sign-changing controls therefore remains a separate problem; its completion is not a missing step in this lemma.

## 7. Required repairs versus optional presentation

**Required repairs: none identified for the stated lemma or the stated initialization conclusions.** I found no false inequality, missing factor, invalid endpoint inclusion, hidden initial-state dependence, unjustified demand for temporal smoothness, or change of quantifier needed to obtain (2).

**Optional presentation improvements:**

1. At lines 19–20, state the sign condition explicitly as the existence of a constant \(s\in\{-1,1\}^2\) with \(s_i u_i\ge0\) almost everywhere. At lines 109–113, write \((x,y)^\top=Sz\) and \(C_r=SCS\). This makes the arbitrary-sign and zero-component cases immediately inspectable.
2. Expand lines 101–107 with the integrable bound on \(D_zF\) and one sentence controlling the difference-quotient remainder using bounded \(\phi'''\). The argument is valid as written; the expansion would make its Fréchet and frozen-control meaning explicit.
3. Add the two completing-square identities and the eigenvalue comparison from this review near lines 115–125. These explain why there is no additional factor in \(h\) and why the norm-conversion factor is exactly \(\sqrt\kappa\).
4. Display the endpoint matrix \(\bigl[\begin{smallmatrix}1+a&1-a\\1-a&1+a\end{smallmatrix}\bigr]\) and its eigenvalues near lines 76–83. Explicitly saying “uncentered” would help prevent a reader from replacing it with the singular centered feature covariance.
5. Define the empirical forward law and covariance recursion near lines 87–94, particularly what “joint” indexes. The conditional variance and square-root arguments support the natural forward-field readings, including singular covariances, but a definition would remove avoidable ambiguity.
6. Keep the bootstrap-comparison language at lines 52–55 limited to numerical hypothesis matching, as it currently is. A later integration into a larger manuscript should point to the actual hypothesis list if that external comparison is meant to be independently checkable. This isolated review does not certify an unseen bootstrap theorem or the history of the earlier obstruction.

These suggestions improve inspectability and precision; they are not conditions for accepting the mathematical bound. In particular, adding a proof of global mean-field evolution or of trained control sign behavior is not an appropriate repair request for this document's stated scope.
