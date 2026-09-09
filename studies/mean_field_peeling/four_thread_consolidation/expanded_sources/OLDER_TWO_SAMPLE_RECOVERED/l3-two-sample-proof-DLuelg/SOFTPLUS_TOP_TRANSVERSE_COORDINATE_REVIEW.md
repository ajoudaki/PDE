# Candidate-only adversarial review: softplus top transverse coordinate

Date: 2026-09-06.

Audited file: `/tmp/l3-two-sample-proof-DLuelg/SOFTPLUS_TOP_TRANSVERSE_COORDINATE.md`.

Verified SHA256, exactly:

`1623764a294c53a475c004c3d99e2d17b65a3cd70a5a5993bd80599908544c98`

## Verdict and audit boundary

**Conditional pass as the stated structural lemma on existing symmetric reference paths.** I find no incorrect factor, sign, differentiation, inverse estimate, or uniform estimate in equations (1)--(15), when the explicitly imported reference assumptions are granted. No mathematical correction is required for that restricted statement.

This verdict does **not** certify the imported reference construction, propagation of its coercivity, its local assembly, or its common-space realization. It does not establish a full response theorem, a global canonical theorem, canonical global existence or restartability, or joint global GD/MF/GF convergence. In particular, it does not turn a conditional reference lemma into an unconditional theorem about canonical initialization.

The material limitations are real: the forward coordinate need not have uniform L2 control; its direct-readout cancellation leaves forcing that depends on the actual network; the actual transverse tangent equation has additional coupled terms; and (15) provides no positive moment of its scalar multiplier. Moreover, the logarithmic estimate in (15) already follows from a direct bound on the scalar coefficient, without using the special invariant. These limitations do not contradict the note's expressly restricted claims.

Only the candidate named above was read as mathematical project material. The procedural solve-math guidance was also read. No cited source, other project file, earlier review, or history was opened. No experiments, numerical or symbolic-computation tests, agents, or candidate edits were used. The calculations below are independent analytic checks. Candidate line references refer to the hash-verified file.

## 1. Exactly what remains conditional

The following are used as the candidate's explicit imported reference premise, not as independently proved conclusions of this audit:

- Existing classical symmetric bounded-kernel reference paths on their entire intervals `[0,s_N]`, with a common upper bound `S_max`, and the stated separate population probability spaces.
- The feature-gradient/raw-metric convention underlying the displayed updates, including the norm-one first-sample evaluation used at lines 90--93.
- Uniform primal, forward, and operator bounds by a configuration-dependent `M`, and the action bound `integral_0^{s_N} a^2 = 1`.
- The positive readout-speed bound invoked at lines 63--70: `k_* <= ||w'(s)||_2^2` throughout these intervals, for sufficiently large reference indices.

The last item is an **all-time reference bound** as used in the candidate. Its advertised origin in readout convexity and positive initial label-mode Gram is not certified here. Merely stating positivity at time zero would not itself be the all-time inequality used below; if only initial positivity were admitted, its propagation would remain a separate proof obligation. This report accepts the candidate's explicitly invoked imported bound conditionally and does not silently prove or enlarge that import.

Population norms and expectations below are those appropriate to each field. In particular, `A`, `kappa`, and `gamma` are deterministic scalars obtained by population-two averaging, whereas `u`, `v`, `w`, `J`, `E`, and `chi` are fields on population three. That distinction is necessary for the product estimates involving `gamma'`.

## 2. Actual modal equations and every normalization

Write `H_1,H_2` for the two population-two features, and let

\[
U=(H_1+H_2)/2,\qquad V=(H_1-H_2)/2,\qquad
c=\mathbb E_2[UV].
\]

At every instant, linearity of the current third-layer operator gives

\[
u=W^{(3)}U,\qquad v=W^{(3)}V.
\]

The half-sample feature-gradient convention is internally consistent with

\[
G=\tfrac12\mathbb E_3[w(H^{(3)}_1-H^{(3)}_2)]
 =\mathbb E_3[wF].
\]

Its readout gradient is `w'=F`. Its third-matrix gradient is

\[
\begin{aligned}
(W^{(3)})'
&=\tfrac12\left(w\phi'(u+v)\otimes H_1
              -w\phi'(u-v)\otimes H_2\right)\\
&=wD\otimes U+wP\otimes V.
\end{aligned}
\]

Indeed, inserting `H_1=U+V`, `H_2=U-V`, and
`phi'(u+v)=P+D`, `phi'(u-v)=P-D` cancels both extra factors of two. This checks the displayed gradient's normalization relative to the convention already fixed by `w'=F`; it is not an independent verification of an unstated physical-time loss or imported metric.

For population operators, `(p tensor q)h=p E_2[qh]`. At equal finite width `n`, this operator has coordinate matrix `p_i q_j/n`. If the input population has size `n_2`, that denominator is `n_2`. There is no additional sample-averaging factor after the half-sample gradient above has been formed.

Applying the update to the modal features and differentiating those features gives the general equations

\[
\begin{aligned}
u'&=AwD+cwP+b_u,\\
v'&=cwD+\kappa wP+b_v,\\
w'&=F.
\end{aligned}
\tag{R1}
\]

Thus the candidate's equation (2) is exactly (R1) with the symmetric-reference condition `c=0`. Another factor check is the sample Gram matrix

\[
K=\begin{pmatrix}A+\kappa&A-\kappa\\A-\kappa&A+\kappa\end{pmatrix}.
\]

Its ordinary eigenvalues are `2A` and `2kappa`; with the sample averaging factor `1/2`, the modal coefficients are `A` and `kappa`, as in (2).

The forcing has not omitted a derivative of a trained layer. Explicitly,

\[
b_a=W^{(3)}\left[\phi'(Z^{(2)}_a)
\left((W^{(2)})'H^{(1)}_a+
W^{(2)}[\phi'(Z^{(1)}_a)(Z^{(1)}_a)']\right)\right].
\tag{R2}
\]

Products inside the brackets are pointwise products on the appropriate population. The `W^(3)` update is already the other term in the product rule, so it is not also part of `b_a`. Both the second-matrix update and first-layer motion remain in (R2).

**Boundary:** ordinary finite realizations need not have `c=0`. Their extra terms in (R1) cannot be discarded. The candidate explicitly restricts (2) to symmetric population references at lines 59--61, which is the correct restriction. A label reversal is also consistent: reversing the label mode and readout reverses both factors in the hidden-layer gradients, leaving their product unchanged, and reverses the readout update.

## 3. Coercivity, moving Gram, and actual coefficient estimates

Since `F` is the half-difference of top activations and `phi` is `epsilon`-Lipschitz,

\[
|F|\leq\epsilon|v|,\qquad
\|F\|_2\leq\epsilon\|W^{(3)}\|_{\mathrm{op}}\sqrt\kappa.
\]

Together with the admitted readout-speed bound and `||W^(3)||_op<=M`, this yields the explicit valid choice

\[
\kappa\geq k_{\min}:=\frac{k_*}{\epsilon^2M^2}>0.
\]

The factor `epsilon^2` and both modal halves are correct. No inverse input covariance is used in this deduction.

Also,

\[
U^2-V^2=H_1H_2,\qquad
A-\kappa=\mathbb E_2[H_1H_2]\geq1,
\]

because `phi>=1`. The separate forward norm bounds imply `A,kappa<=M^2`, hence

\[
1+M^{-2}\leq\gamma=A/\kappa\leq M^2/k_{\min}.
\]

This verifies (3), including uniform separation from both zero in `kappa` and the singular value `gamma=1`. With `c=0`, the lower sample Gram has positive eigenvalues `2A,2kappa`. The claimed applicability to antiparallel inputs is therefore conditional only on the admitted reference/coercivity premise holding for that configuration. This audit does not prove that premise for any input configuration.

For the motion estimates, the raw norm dominates the operator norm of a kernel variation under the displayed Hilbert-space tensor convention. Consequently,

\[
\begin{aligned}
\|(Z^{(2)}_a)'\|_2
&\leq\|(W^{(2)})'\|_{\mathrm{op}}\|H^{(1)}_a\|_2
 +\|W^{(2)}\|_{\mathrm{op}}\epsilon\|(Z^{(1)}_a)'\|_2\\
&\leq C_Ma,\\
\|(H^{(2)}_a)'\|_2&\leq\epsilon C_Ma.
\end{aligned}
\]

Here the first-layer evaluation bound is precisely the raw-metric premise stated by the candidate. Averaging and differencing yield bounds for `U'` and `V'`. Differentiation then gives

\[
A'=2\langle U,U'\rangle_2,\quad
\kappa'=2\langle V,V'\rangle_2,\quad
\gamma'=\frac{A'}\kappa-\frac{A\kappa'}{\kappa^2}.
\]

The primal bounds and `kappa>=k_min` prove all scalar estimates in (4). Equation (R2) and the operator bound for `W^(3)` prove `||b_u||_2+||b_v||_2<=Ca`. Finally, `u=W^(3)U` and `v=W^(3)V` give the last bound in (4). Thus the moving Gram estimates are derived from actual lower motion and do not require freezing it.

For any subinterval `B`, Cauchy--Schwarz in time gives

\[
\int_B a\leq\sqrt{|B|\int_B a^2}.
\]

The stated time-integrated bounds follow from the action `integral a^2=1`. They require neither uniform pointwise feature bounds over the reference index nor operator bounds on every Lp space.

## 4. Logistic algebra and the exact invariant

Let `y=exp(u)`, `C_v=cosh(v)`, `S_v=sinh(v)`, and
`Delta=1+2y C_v+y^2`. Direct substitution of
`phi'(z)=epsilon exp(z)/(1+exp(z))` gives

\[
P=\epsilon\frac{y(C_v+y)}\Delta,\qquad
D=\epsilon\frac{yS_v}\Delta.
\]

Therefore

\[
\frac DP=\frac{\sinh v}{\cosh v+e^u}.
\]

This verifies (5). In particular, `P>0` for all finite `u,v`, `|D/P|<1`, and the factor `epsilon` cancels. The additive constant in softplus cancels from the activation contrast, for which

\[
F=\frac\epsilon2\log\frac{1+e^{u+v}}{1+e^{u-v}},
\qquad F_u=D,\quad F_v=P.
\]

For fixed `gamma>1`, direct differentiation of (6) gives exactly

\[
I_u=-\frac1\gamma e^{-u/\gamma}(\cosh v+e^u),
\qquad I_v=e^{-u/\gamma}\sinh v.
\]

Multiplying the first expression by `gamma D` and the second by `P` gives zero by (5). Since `A=gamma kappa`, the full chain rule along an actual symmetric reference is

\[
I'=I_u b_u+I_v b_v+I_\gamma\gamma'.
\]

For completeness, the moving-parameter derivative is

\[
I_\gamma=\frac{u}{\gamma^2}I+
\frac{e^{(1-1/\gamma)u}}{(\gamma-1)^2}.
\tag{R3}
\]

Thus (8) retains an actual, generally nonzero moving-Gram term. The cancellation is of the explicit direct `w` contribution only: `b_u`, `b_v`, and the evolving Gram can still depend on the readout through the network dynamics.

No division by `w`, `v`, `F`, or `v'` is needed. At `v=0`, `D=I_v=0` and the identity still holds. At zeros or sign changes of `w`, the same differentiated identity applies. This verifies the asserted sign robustness.

The discovery calculation is also correct on the portions where its divisions are allowed:

\[
\frac{du}{dv}=\gamma\frac{\sinh v}{\cosh v+e^u}
\quad\Longrightarrow\quad
\frac{dC_v}{dy}-\frac{C_v}{\gamma y}=\frac1\gamma.
\]

Its integrating factor `y^(-1/gamma)` recovers (6). The global proof properly uses the differentiated identity, not the division argument.

**Limit:** (R3) and the spatial derivatives have exponential growth. The stated L2/action information does not supply uniform L2 bounds for the right side of (8), or even assert that the forward coordinate lies in a uniform L2 class. Pointwise classical validity at each reference is not such a bound. Lines 260--264 correctly recognize this gap.

## 5. Global inverse bounds and their exact domain

At fixed `v,gamma`, `I_u<0`. As `u` tends to negative infinity, the positive term `exp(-u/gamma) cosh(v)` diverges and the negative term vanishes. As `u` tends to positive infinity, the negative term
`-exp((1-1/gamma)u)/(gamma-1)` diverges and the positive term vanishes. This proves the claimed bijection onto the whole real line.

For `t=cosh(v)>=1` and `y=exp(u)>0`,

\[
|I_u|=\frac1\gamma\bigl(t y^{-1/\gamma}+y^{1-1/\gamma}\bigr).
\]

Differentiating in `y` gives its unique minimum at `y=t/(gamma-1)`, with value

\[
t^{1-1/\gamma}(\gamma-1)^{-(\gamma-1)/\gamma}.
\]

The expression is at least the positive minimum of
`(gamma-1)^(-(gamma-1)/gamma)` over the compact interval (3). Denote that minimum by `c_0>0`. This verifies the normalization and the uniform lower bound at lines 156--166.

If `u=h_gamma(I,v)` is the inverse, differentiating its defining equation gives

\[
|(h_\gamma)_I|\leq c_0^{-1},\qquad
|(h_\gamma)_v|=\left|\frac{I_v}{I_u}\right|
=\left|\gamma\frac DP\right|\leq\gamma.
\]

The nonzero derivative and smooth defining function give a smooth local inverse at every point; the global uniqueness makes those local inverses one global inverse. Integrating the displayed bounds along coordinate segments gives the genuinely global estimate

\[
|h_\gamma(I_1,v_1)-h_\gamma(I_2,v_2)|
\leq c_0^{-1}|I_1-I_2|+\Gamma|v_1-v_2|,
\]

where `Gamma` is the upper endpoint of (3). Equation (9) and the fixed-`gamma` global Lipschitz claim are correct.

This is not a forward Lipschitz estimate and not a joint uniform Lipschitz estimate in `gamma`. For example, at fixed `v` and large positive `u`, implicit differentiation gives

\[
\partial_\gamma h_\gamma(I,v)
=-\frac{u}{\gamma(\gamma-1)}+
\frac{\gamma}{(\gamma-1)^2}+o(1),
\]

evaluated at `I=I_gamma(u,v)`. The derivative is unbounded. The candidate explicitly fixes `gamma` in the inverse assertion, so this is a boundary of the result, not a counterexample to it.

## 6. Logarithmic normal identity and uniform L2 estimates

Writing `Q=cosh(v)+exp(u)`, the normal logarithm is

\[
J=-\log\gamma-u/\gamma+\log Q.
\]

The lower derivative bound gives `J>=log(c_0)`. The upper bound
`log Q<=log 2+|u|+|v|`, together with (3), proves the stated linear-growth bound on `|J|`. Differentiation gives

\[
J_u=-1/\gamma+e^u/Q,\quad
J_v=\sinh v/Q=D/P,\quad
J_\gamma=-1/\gamma+u/\gamma^2.
\]

Both `|J_u|` and `|J_v|` are at most one. These calculations verify (10)--(11), including the parameter derivative.

On the actual symmetric path, the self terms in the chain rule are

\[
\begin{aligned}
J_uAwD+J_v\kappa wP
&=-\frac A\gamma wD+
A\frac{e^u}{Q}wD+\kappa wD\\
&=A\frac{e^u}{Q}wD=\chi.
\end{aligned}
\]

Thus `J'=chi+E` is exact, with the full `E` specified by the candidate. No sign or factor is missing in (12).

For the uniform estimate,

\[
\begin{aligned}
\|E\|_2
&\leq\|b_u\|_2+\|b_v\|_2+
|\gamma'|\left(\gamma^{-1}+\gamma^{-2}\|u\|_2\right)\\
&\leq Ca.
\end{aligned}
\]

Multiplication by `gamma'` is harmless here because it is a deterministic scalar, not an arbitrary L2 field. Applying the time Cauchy--Schwarz inequality proves (13) for every subinterval with exactly its stated square-root factor.

Since `|D|<=epsilon/2` and `0<e^u/Q<1`,

\[
\|\chi\|_2\leq\frac\epsilon2 M^2\|w\|_2
\leq\frac\epsilon2 M^3.
\tag{R4}
\]

There is no readout supremum in this estimate. Consequently `J` has a uniform L2 bound, its derivative is uniformly bounded in time-L2 with values in population-L2, and

\[
\|J(t)-J(s)\|_2
\leq C\left((t-s)+\sqrt{(t-s)\int_s^t a(r)^2\,dr}\right)
\leq C\bigl((t-s)+\sqrt{t-s}\bigr).
\tag{R5}
\]

This supplies the asserted uniform time modulus explicitly. These are estimates on the actual path, with its moving Gram and forcing.

The identities can be read pointwise along the classical references. Their L2 interpretation is also justified: the right side of (12) is integrable in time with values in L2, and `J` has the stated L2 growth bound. An absolutely continuous representative gives the endpoint identity in that space. Time-integrability and the population probability measure also give pointwise time-integrability outside a null set, as needed for the scalar exponential below.

The word “damping” must not be read as a sign assertion. Since `D` has the sign of `v`, `chi` has the sign of `wv`. It can be negative. The transport formula and estimates correctly allow this.

## 7. Transport, (15), and a stronger direct logarithmic bound

Integrating (12) gives

\[
-\int_s^t\chi=J(s)-J(t)+\int_s^tE.
\]

Exponentiation proves (14) with the correct sign on every term. The lower bound for `J(t)` yields pointwise

\[
\log^+T(s,t)
\leq |J(s)|+|\log c_0|+\int_s^t|E(r)|\,dr.
\]

Taking the L2 norm, using Minkowski's inequality and (13), proves (15). Replacing the last integral by `integral_s^{s_N}|E|` proves the claimed version with a supremum over terminal times. For fixed `s`, continuity of the scalar integral and its integrable absolute value ensure that this supremum can be taken outside a single population null set.

Chebyshev's inequality then gives, for `R>1`,

\[
\mathbb P_3\{T(s,t)>R\}
\leq\frac{\|\log^+T(s,t)\|_2^2}{(\log R)^2},
\]

with the same kind of bound for the terminal-time supremum. The candidate absorbs the squared constant into `C`, legitimately.

**Adversarial observation about the strength of this result.** From the definition of `T` and (R4) alone,

\[
\begin{aligned}
\log^+\sup_{s\leq r\leq t}T(s,r)
&\leq\int_s^t|\chi(r)|\,dr,\\
\left\|\log^+\sup_{s\leq r\leq t}T(s,r)\right\|_2
&\leq C(t-s).
\end{aligned}
\tag{R6}
\]

There is even a bound `C S_max` for the L2 norm of the positive logarithm of the supremum over **both** endpoints in a reference interval, since every such integral is bounded by `integral_0^{s_N}|chi|`. These bounds need no invariant or endpoint estimate for `J`. In particular, uniform logarithmic tightness itself is not additional integrability obtained from the special coordinate. The exact endpoint/forcing representation (14) is the structural information supplied by that coordinate.

This observation does not falsify (15). It does mean that (15) should not be presented as resolving a response-integrability obstacle merely because it was derived using (14).

## 8. Homogeneous transverse tangent: correct calculation, restricted meaning

To avoid confusing the activation contrast `F` with the tangent direction, put

\[
R=D/P,\qquad f=\gamma R,\qquad q=\kappa wP.
\]

In the self system with constant `gamma` and zero lower forcing,
`u'=fq`, `v'=q`. For a differentiable variation with fixed `gamma`, set
`x=delta u`, `y=delta v`, and `e=x-fy`. Direct differentiation gives

\[
\begin{aligned}
e'
&=q(f_ux+f_vy)-f'y,\\
f'&=(f_uf+f_v)q,\\
e'&=qf_u(x-fy)=qf_ue.
\end{aligned}
\]

All variations of the common scalar speed `q` cancel in the first line. In particular, the direct variation of `w` cancels, even if it is allowed instead of held fixed. The derivative and coefficient are

\[
f_u=-\gamma\frac{e^u\sinh v}{Q^2},\qquad
qf_u=-\gamma\kappa\frac{e^u}{Q}wD=-\chi.
\]

This verifies the candidate's homogeneous equation, including its negative sign.

An independent sign check uses `I_v=-fI_u`: the variation satisfies
`delta I=I_u e`. In the fixed-`gamma`, zero-forcing self system, `delta I` is constant. Since `I_u=-exp(J)` and `J'=chi`, this gives `e'=-chi e` again.

No assertion that such a homogeneous equation governs the whole actual tangent follows. To make the missing terms concrete, consider any differentiable family of full paths for which variations exist, based at a symmetric reference, and let `delta c` be the variation of the cross-Gram coefficient from (R1). Algebraic differentiation of (R1) yields

\[
\begin{aligned}
e'={}&-\chi e
 +\delta b_u-f\delta b_v
 +qR\,\delta\gamma
 +w(P-fD)\,\delta c\\
&-\bigl(f_ub_u+f_vb_v+R\gamma'\bigr)\delta v,
\qquad
\delta\gamma=\frac{\delta A-\gamma\delta\kappa}{\kappa}.
\end{aligned}
\tag{R7}
\]

This is a conditional first-variation calculation, not a theorem asserting differentiability of the imported construction. For variations that remain symmetric, `delta c=0`. Arbitrary perturbations can have `delta c!=0`, even though the base reference has `c=0`.

Equation (R7) identifies three distinct issues for any attempted response theorem:

- Actual lower and Gram motion produces the last, moving-coordinate term even before considering the variations of those motions.
- Variations of the Gram and forcing, and possibly of symmetry, provide further terms. The forcing variations include variations of trained matrices and lower-layer dynamics.
- These terms are coupled to the unknown variation itself. Their designation as sources in a scalar variation-of-constants formula does not make them externally controlled functions.

In particular, the direct cancellation of `delta w` in the self speed does not cancel the readout dependence hidden inside the full lower dynamics. Also, an L2 bound on the coefficient of `delta v` would not control its product with an arbitrary L2 variation in L2.

Thus `T` is the homogeneous multiplier for the specifically isolated scalar coefficient `-chi`. It is not the propagator of the full tangent system or a bound for a complete projected response operator. Lines 246--248 state the appropriate limitation. Writing (R7) in the candidate would make that limitation harder to overlook, but its omission does not invalidate the stated restricted calculation.

## 9. Why the gaps to full response and canonical conclusions remain open

The failure of a moment conclusion from a logarithmic estimate is substantive. As an elementary analytic example, let a nonnegative scalar `X` have survival probability

\[
\mathbb P\{X>x\}=(1+x)^{-3},\qquad x\geq0,
\]

and set `Y=exp(X)`. Then

\[
\mathbb E[(\log Y)^2]
=2\int_0^\infty\frac{x}{(1+x)^3}\,dx=1,
\]

whereas `E[Y^p]=infinity` for every `p>0`, since the density of `X` is `3(1+x)^(-4)` and exponential growth dominates that polynomial. This is a logical example about the estimate class, not an alleged realization of the network dynamics. It establishes precisely why an estimate such as (15) or (R6), alone, proves no positive multiplier moment.

For the same reason, a logarithmic tail is not an L2 operator bound for multiplication by `T`: that operator's L2-to-L2 norm requires an essential supremum of `T`. Other response norms might use higher moments and additional source integrability, but neither is provided here. Even a hypothetical scalar initial-data estimate would leave the coupled terms in (R7) to control.

The coordinate identity has another independent obstruction: exponential derivatives of `I` multiply actual L2 forcing in (8). A Lipschitz inverse does not reverse this estimate. Nor do primal L2 bounds and finite action furnish exponential moments of `integral |E|`.

The final Gaussian-initialization observation is correct with its stated restriction. For jointly Gaussian scalar initial fields `u(0),v(0)` with finite variances,
`|J(0)|<=C(1+|u(0)|+|v(0)|)` implies finite expectations of `exp(p|J(0)|)` for every fixed finite `p`: each one-dimensional Gaussian density integrates `exp(q|x|)`, and Cauchy--Schwarz handles the joint expression without an independence assumption. This is a statement about that specified initial law. The audit does not certify the canonical law or an approximation theorem connecting it to the reference paths.

Strong L2 approximation alone cannot supply uniform exponential moments. For example, a spike of height `n` on a set of probability `n^(-4)` tends to zero in L2 while its exponential moment contribution is `n^(-4) exp(pn)`, which diverges for every `p>0`. Each spike is bounded individually. This is again an analytic obstruction to inferring exponential bounds from the stated topology, not a construction or experiment on the candidate's dynamics.

Even if initial exponential moments were uniform, (14) still contains `exp(integral E)`, and the full response still has (R7). The candidate does not close these estimates and explicitly says so. No full response or global canonical conclusion is justified by this note.

## 10. Required fixes versus optional improvements

### Required for the statement actually made

None found, under the precise conditional premise in Section 1. Equations (1)--(15), the fixed-parameter inverse claims, the actual L2 estimates, and the restricted homogeneous tangent calculation survive the adversarial check.

The scope restrictions are essential hypotheses and limitations, not dispensable qualifications. If the result is restated, it must retain the imported all-time reference/coercivity premise, the symmetric-reference restriction, fixed `gamma` in the inverse Lipschitz claim, and the scalar/logarithmic scope of (15). This audit does not authorize deleting any of them.

If a subsequent claim admits only time-zero coercivity, asserts the modal equations for nonsymmetric paths, treats `T` as the full response propagator, or concludes a positive multiplier moment or a canonical global theorem, it requires new hypotheses or proofs. Those would be substantive missing steps, not wording fixes. They are not claims presently established by the candidate.

### Optional improvements to this candidate

1. State the half-sample feature-gradient functional and the normalized tensor action explicitly. This makes the factor check self-contained without appealing to the imported convention for its interpretation.
2. Include the general modal equations (R1), or at least their cross-Gram terms, to expose exactly what symmetry removes. For a tangent discussion, display (R7) or its symmetric-variation specialization.
3. Give the explicit time modulus (R5). This distinguishes an actual proved uniform estimate from an unspecified continuity assertion.
4. Add the direct estimate (R6). It shows that the logarithmic bound itself is already available from the primal coefficient bound and locates the contribution of the coordinate in the exact representation (14).
5. State once that “damping” allows negative `chi`, and that inverse Lipschitz continuity is not uniform jointly in the moving parameter. Both restrictions are already consistent with the text; making them explicit would prevent overinterpretation.

These changes would improve exposition and scope enforcement. They are not repairs of a discovered algebraic counterexample.

## Final scoped assessment

The candidate correctly derives a direct-readout cancellation and a logarithmic normal transport identity for the actual symmetric reference equations, while retaining full lower forcing and a moving Gram. Its inverse bounds and uniform L2/logarithmic estimates are valid under its admitted reference premise. The scalar homogeneous transverse calculation is also correct in its expressly restricted sense.

The candidate does not establish uniform forward-coordinate control, multiplier moments, control of the coupled full tangent sources, or any full response/global canonical theorem. The imported premise remains conditionally assumed and independently uncertified by this audit.
