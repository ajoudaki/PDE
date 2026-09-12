# Internal check G: quantitative curvature drift

**Verdict: PASS for the stated reached-curve quantitative lemma.** I found no
substantive mathematical flaw in Q1–Q14 of the frozen candidate. The appended
source calculation supplies the fourth-moment bound actually needed in the
scalar Hessian comparison. The resulting operator-norm Lipschitz bound for
the prediction-kernel derivative and the finite risk remainder follow with
the displayed constants.

This is an internal mathematical check, not a promotion review. It does not
certify numerical values for the established source constants, establish a
negative cubic, or prove E₀. The proposed positive-risk implication remains
conditional on a separate strictly negative actual-neural cubic certificate.

Checked candidate: `QUANTITATIVE_CURVATURE_DRIFT.md`, SHA-256
`5bfd6b4c1683d172e3c7a543e8b9e7faa17b2b14f0299ea4242a3776cbcee7d5`.
The candidate was read completely, preserved unchanged, and its hash was
verified again after the mathematical reconstruction.

Checker: `/root/geometry_route`, 2026-09-12. I authored the earlier geometry
route and its G22 remainder identity; root authored this new candidate.
No other current follow-up or reviewer report was read for this check.

## 1. Q1–Q4: the appended source estimate

The cap needed here is the established cap on every ordinary historical and
current backward row. The argument does not assume a cap for the new
forward answer or a differentiated reverse answer.

Let `H` bound the full accumulated absolute control mass and readout
supremum, `D=B+H³`, and `Z=sum |gamma_j||Q_j|`. CT28 gives

\[
\mathbb E e^{\lambda Z}
 \le2\exp(\lambda HD+\lambda^2H^4/2).
\]

For the actual CT29 pulse envelope `E=exp(DH+2Z)`, substituting
`lambda=2p` and taking the p-th root gives exactly

\[
\|E\|_p\le2^{1/p}\exp(3DH+2pH^4).
\]

Thus the exponents in Q1 have the correct factor of `p`. Neither this
moment calculation nor the later Cauchy–Schwarz argument requires
independence of the query and its pulse envelope.

For `b_w=sum_i a_i phi'(w.u_i)Q_i u_i`, with `sum |a_i|<=M`, I reconstructed
the old-source differentiation before taking expectations. The three pieces
are the first gate derivative, the direct current reverse-source injection,
and the response-memory feature derivatives. Using CT29 and summing the
deterministic old injection masses gives their total expected absolute sums

\[
2MH\|E\|_2q_2,\qquad M,\qquad MDH\|E\|_1.
\]

The extra outside gate in `F_u(b)=phi'(w.u)(b_w.u)` contributes
`2MH||E||2 q2`, because `||b_w||2<=M q2`. These are exactly the four
contributions to Q3. In particular, the direct term is a sum of the absolute
coefficients of `b`, not a factor equal to the number of current queries.

Appending multiple current queries does not create an omitted old-source
response. The already constructed state is unchanged by those queries.
Each ordinary current query depends on its own current forward source and
the retained training history; it does not depend on another unused current
query. The distinct current reverse names must nevertheless remain in the
appended `F` expression, and the candidate does retain all of them. This
handles duplicated inputs and singular query Grams without merging names.

The extra forward call is a fixed finite program. Its input is built from
bounded smooth gates times ordinary query answers, precisely the products
covered by the fixed-program specialization A.2. All coefficient and
covariance values are frozen during named differentiation. The III.F source
rule therefore gives

\[
A_0F=\xi_F+\sum_p\alpha_p\delta_p,
\quad \operatorname{Var}(\xi_F)=\|F\|_2^2,
\quad\sum_p|\alpha_p|\le M C_\alpha.
\]

Every reverse input `delta_p` is bounded pointwise by `H`. The Gaussian
fourth norm is `3^(1/4)||F||2`, so Q4 follows with the stated constant.
The retained rank history gives `|K F|<=H²||F||2`; the current middle-gradient
combination gives `|b_K H1(u)|<=MH`. Adding these contributions gives exactly
`U4=H+3^(1/4)q2+H C_alpha+H²q2` and proves Q2.

I specifically checked the potential invalid shortcut `A0:L4 -> L4`.
No such boundedness is used. The new moment is obtained from the actual
initialized source rule, whose old reverse factors are still ordinary
bounded `delta` fields. The reverse action is not refreshed or replaced.

## 2. Passage to the reached state

The source-admissible Euler approximations retain a common carrier and
uniform query moments of every fixed order. Their current raw gradients
converge in `L2`; for first-row gradient combinations, interpolation with
the uniform higher moments gives the required `L4` convergence. Their
coefficient sums remain bounded, including the projected anchor weights.

Thus `F` converges in `L2`. The common bounded actual action and raw middle
increment convergence imply `V=b_KH1+A F` converges in `L2`. An almost-sure
subsequence and Fatou pass the uniform fourth-moment bound. This conclusion
does not presume `L4` convergence of `V`, which would be a different claim.

For an `L2(p rho)` coefficient, bounded continuous approximation followed by
quadrature is legitimate because the density is bounded above and below
on the compact circle. Approximation errors are controlled by the bounded
raw gradient kernel and Cauchy–Schwarz. If an approximant initially has a
slightly larger norm, rescaling it by a factor tending to one preserves
the common mass bound; taking the limit gives the stated bound at the
original coefficient norm. The two anchor atoms are retained separately.
This supplies every coefficient direction needed in Q5–Q14. No finite-width
fourth-moment convergence is asserted or needed in this population passage.

## 3. Q5–Q9: directions and scalar Hessian differences

For a unit prediction-space vector `v`, the unprojected force has raw norm
at most `L`. Since `||GM^-1||<=sqrt(2/k)`, its anchor multiplier has l1
norm at most `2L/sqrt(k)`. Thus the gradient-combination mass `m_d` is
correct. NSC28 and the projector derivative give
`sup_u ||d'_t(u)||<=A_s T_g(1+4L/sqrt(k))=J`, proving the operator-direction
raw Lipschitz bound used in Q6.

I checked the two directional preactivation subtractions explicitly:

* For `F_t(x_t)-F_s(x_s)`, the changed direction costs `J h`, and the changed
  gate costs `2||w_t-w_s||4 ||x_(s,w)||4`, giving exactly `VF h`.
* For `x_KH1+A F`, change its factors successively. The four costs are
  `J h`, `L Vw2 h`, `VK L h`, and `a_b VF h`, giving exactly `VV h`.

The state constants in Q5 are the NSC25–NSC28 bounds multiplied by the
actual control-mass bound `A_s`. Integrating the pointwise bounded readout
velocity gives the claimed supremum-norm readout difference; this does not
require a Banach-space derivative theorem in `Linfinity`.

Q7 agrees with the polarization of the actual raw scalar second derivative.
Its last lower-layer term uses the actual adjoint to rewrite the lower
activation curvature. It is a scalar form on gradient-combination
directions, not a bounded Hessian on every ambient raw L2 direction.

Every summand of the constant in Q8 has the necessary product bound:

| Scalar Hessian term | Difference costs for unit force directions |
|---|---|
| The two readout/upper mixed terms | `2[J Z2f+2m_d Vz Z2f+L VV] h` |
| Upper curvature | `[2Vc Z2f²+4H Vz Z4f²+4H VV Z2f] h` |
| The two middle mixed terms | `2[Vdelta L²+c_b J L+c_b L VF] h` |
| Lower row curvature | `[2VQ W4f²+4Vw4 q4 W4f²+4q4 J W4f] h` |

The upper gate difference uses the newly proved `L4` bounds on both
directional upper preactivations. The lower gate difference uses four `L4`
factors, whose reciprocal exponents sum to one. A changed row direction
needs only its raw `L2` difference and the `L4` bounds of `Q` and the
remaining row direction. The mixed readout gate difference uses the
bounded readout component `m_d`. These are valid telescoping bounds even
when some factors are evaluated at the other time endpoint.

The amplitude constant `C_H` follows from the corresponding undifferenced
products. The conservative `|phi'''|<=4` is valid for tanh. These estimates
prove Q9 without a higher-moment bound for a backward derivative and without
assuming a third population time derivative.

## 4. Q10–Q13: the controls and projector are included

Write the anchor coefficient as
`beta_t(v)=B_t* U_t(v)`, where `B_t=G_t M_t^-1` and
`U_t(v)=int v g_t p d rho`. Its derivative is the sum of the two factor
derivatives. With `||B'||<=A_s T_B`, `||U||<=L||v||`,
`||U'||<=A_s T_g||v||`, and `||B||<=sqrt(2/k)`, conversion from l2 to
l1 supplies exactly Q10's factor `sqrt(2)` and its `L_beta`.

The time-varying coefficient measure therefore has both the required mass
bound and a controlled change. Integrating the scalar Hessian differences
against one measure, then subtracting the two measures at the anchors,
gives `L_C=m_d L_H+L_beta C_H`. No derivative of the anchor coefficients
has been omitted in this step.

For fixed `v`, differentiate `D_t v=Pi_t U_t(v)` along the actual curve.
Its normal derivative component is orthogonal to `D_t w`. The tangent
part is the projected scalar Hessian with measure `mu_t(v)`, applied to
`theta'=-2D_t r_t`. Pairing with `D_t w` gives the first term in Q11;
pairing the derivative of `D_t w` with `D_t v` gives the other. Thus both
the factor `-2` and the two trilinear terms are correct. This is the full
projected kernel, not an unprojected or readout-only formula.

For unit `v,w`, one term changes by at most
`R[L_C+2 C_C L²]|t-s|`: use trilinearity to separate the time change of
the form from `r_t-r_s`, and use risk dissipation for `||r_t||<=R`.
The two terms in Q11, each with factor two, give exactly
`Lambda_1=4R[L_C+2 C_C L²]`.

Taking the supremum over unit prediction vectors proves the operator-norm
claim. If the source derivative is first interpreted almost everywhere
from its strong absolute continuity, Q9–Q11 give a continuous
operator-valued representative for that derivative. Integrating its
bilinear pairings identifies it with the derivative of `K_t` everywhere,
including the right derivative at zero. Thus no `K''` is silently assumed
when passing from Q11 to the operator-norm Lipschitz bound Q12.

All tested directions use one fixed prediction space for a fixed task and
density. Uniformity across the declared families follows because the
displayed constants depend only on the common source tube, anchor gap,
state bounds, and label bound. The support-count independence survives the
weighted source sums in Q3. The proof does not provide a simultaneous
width/contamination rate or uniform finite-width initialization event.

## 5. Q14 and the precise conclusion

The frozen G22 remainder uses the time-kernel variation bound
`Gamma=2LJ` and the derivative drift modulus. Substituting Q13 produces
exactly Q14. If `C_p(r0)<=-c_*`, its main term is at least `8c_* T²`.
For `T<=1`, the Q14 remainder is at most

\[
R^2T^3(2\Lambda_1+8L^2\Gamma+\Gamma^2).
\]

The candidate's proposed conditional upper bound on `T` makes this at
most `4c_* T²`. Therefore the claimed remaining margin `4c_* T²` has
the correct factor. The shared initial predictor, metric, and canonical
slow clock are unchanged. Substitution into G24 similarly controls the
previously defined scalar-clock/component remainder but does not determine
its beneficial sign.

The result replaces an unspecified modulus by a finite explicit expression
in the established constants. Several of those constants are unevaluated
and extremely large; this internal PASS is not a numerical enclosure or a
claim of a practical episode. There is still no `c_*`, positive component
coefficient, sampled advantage, or completed E₀ theorem.

## 6. Actual inputs and check record

Read completely: the frozen candidate. Established dependency read coverage
is the complete scope already recorded in `ROUTE_GEOMETRY.md` §7: C.4.9 and
C.4.10, A.1–A.4, C.4.5.1 §§1–3 and its rational certificate, C.4.5.2 §§1–4,
and `special_data_limits.md` III.F in full, together with the complete
notation contract and required skills/process references. Their hashes are
unchanged, so no changed instruction or scientific source required rereading.

Hashes verified during this check:

| Input | SHA-256 |
|---|---|
| Candidate | `5bfd6b4c1683d172e3c7a543e8b9e7faa17b2b14f0299ea4242a3776cbcee7d5` |
| `docs/global_nonlinear.md` | `5c7f4cd85eebe73f497ff91cca4f3c525f158727c28b8a187a09add94e756483` |
| `docs/special_data_limits.md` | `5b7b48aa5deab320042217a6f284002366a683bf0f7f0b63c05d8167c526a489` |
| `docs/NOTATION.md` | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |
| `RESEARCH_WORKFLOW.md` | `8b36d7dfc1ad881fcb6bfe32274a5e50c5125b33d68dbcf7c3937f7f6c21ce12` |

Actual checks were the algebraic and functional-analytic reconstructions
above, including zero coefficient mass, signed coefficients, repeated current
queries, rank-deficient Gaussian sources, arbitrary unit prediction
directions, and zero residual. No numerical experiment, symbolic tool, or
formal proof checker was used. No other current route or review content
was accessed. The candidate, earlier frozen artifacts, established sources,
shared notes, and Git index were preserved; only this check report was
written. Metadata-only HEAD was
`88172930b86b57f302ae53d0ae28c8bcc33838e4`, with no staged paths.

There are no required scientific corrections from this internal check.
