# Internal comparison: finite target modes and sampling

Reviewer: `population_route`, author of the independent first-round population
attempt. This is the supervisor-authorized internal comparison after first-round
freezing, not an isolated promotion review. Date: 2026-09-12.

**Conclusion.** The finite target-space contraction and sampling lemma are
correct under their stated continuation and uniform comparison premises. I
found no coefficient, sign, missing cancellation, or noise-centering error in
their main inequalities. The finite target space containing `F_*-q0` exactly
is a useful improvement over bounding an unknown Fourier tail of that reference
residual. It gives a class/reference-only floor, with exact zero target tail
for each fixed finite coefficient cap. The candidate remains conditional until
the arbitrary-law construction/capture and its common constants are supplied.

Two notation/scope clarifications should be made when assembling the result:

1. Call the coefficient index cap `N`, rather than the literal trigonometric
   degree: the target `q_N` can have harmonic degree `2N+5`.
2. Use `tau` for the constrained episode clock in both lemmas. Their displayed
   equations use slow time; the actual physical stopping time is `T_*/epsilon`.

The robust family in the finite-mode file is robust in every fixed finite-`N`
coefficient space and in the whole admitted density class. Its stated proof
does not claim an open neighborhood in the infinite-series coefficient space.
Keep that scope explicit; it is sufficient for a robust subfamily of the frozen
class. No change to the frozen target class is needed.

## 1. Complete audited scope and provenance

New scientific inputs read completely:

- `attempt_finite_modes.md`, sections 1–6, SHA-256
  `543edb9a3def06e1dbe58fe89eb18d8f30482319d9de5a97f05cf4c8268a94e5`.
- `sampling_lemma.md`, all sections, SHA-256
  `02ba380b261f69295b6cfb92b32684ffdf9c2683a43130ded0b246de92c1a5d1`.

Own frozen attempt retained as an already read comparison input:
`attempt_population.md`, SHA-256
`cb2a143c127e98de13b56c702d7629307b70d793ce61aa6c8e95f8ac5879e116`.
No other attempt or study was read. The established dependencies and their
complete read coverage are recorded in section 1 of that own frozen attempt;
in particular C.4.9 and the approved III.F source/strong-calculus section were
read completely. The established file hashes remain

| Input | SHA-256 |
| --- | --- |
| global_nonlinear.md | `7633fb054cf02f2359b193fcb090634304cc1153f4d8f978fd0ac30789355465` |
| special_data_limits.md | `5b7b48aa5deab320042217a6f284002366a683bf0f7f0b63c05d8167c526a489` |

AGENTS.md and workflow Part 1 were reread before comparison. Required proof
and conjecture skills and their applicable references were already read in
this context. Checks were analytic reconstruction and adversarial boundary
cases; no experiments or external scientific searches were performed. Git
HEAD/index and this report's path status were checked before writing. Only
this report is written, with frozen inputs unchanged.

## 2. Signed-measure separation and the tensor/Fubini step

The proof does not infer continuum separation from finite Gram positivity.
It directly extends the protected-row event argument to a finite signed
measure. For a unit vector `v` with nonzero coordinates, the only possible
atoms are not perpendicular to `v`. The selected protected events therefore
give pointwise convergence of the bounded tanh features to the half-circle
sign function for total-variation-almost every input. Dominated convergence
for the total variation is legitimate even when the non-atomic part is
singular continuous. The Gaussian box need not be independent of the learned
envelope: its probability dominates the bad-envelope probability, which
already gives a positive intersection.

The Fourier coefficient is correctly normalized for normalized arc measure:

\[
 \widehat{\operatorname{sign}(\cos)}(j)
 =\frac{2\sin(j\pi/2)}{\pi j},\qquad j\ne0.
\]

It is nonzero at every odd frequency and zero at even frequencies. Oddness
of the signed measure supplies exactly the missing even coefficients.
The contained Fejer argument then proves uniqueness of the finite measure;
it does not require a pointwise Fourier series for the sign function.

The weighted tensor claim is also valid. At the endpoint the readout is
bounded by 10, so
`|delta_dagger(u,z)|<=10` for a jointly measurable representative. Thus
`delta_dagger(u,z) dmu(u)` is a finite measure for almost every `z`.
The map `u -> delta_dagger(u) tensor H1_dagger(u)` is Bochner integrable
against the finite variation measure, and its Hilbert–Schmidt kernel is in
`L2(Omega2 x Omega1)`. The tensor/kernel isometry follows by expanding norms
on finite tensor sums and completing, exactly as stated. Fubini gives a
zero first-layer kernel for almost every second-layer coordinate.

For clarity, the joint representative can be constructed relative to the
fixed finite measure `|mu|`: approximate the continuous `L2` field by simple
input fields, pass to a subsequence in the product measure, and retain the
finitely many anchor values separately. Negative inputs can be represented
using the exact evenness of `delta`. This avoids requiring one exceptional
set that works simultaneously for every possible signed measure.

The endpoint has `c_dagger!=0` because it fits an anchor. On the positive
measure set where the readout is nonzero, the upper gate is positive for
`|mu|`-almost every input and at each of the four named anchors, by finiteness
of the preactivations and Fubini. Hence the weighted zero measure implies
the original measure is zero. Neither injectivity of `A_dagger` nor any
independence between trained fields is used.

For the residual/anchor measure

\[
 \mu=r p_s\rho-\tfrac12\sum_a\beta_a
                              (\delta_{e_a}-\delta_{-e_a}),
\]

the density is `L1`, since `r` is `L2(p rho)` and `p` is bounded. Its
absolutely continuous and atomic parts cannot cancel as measures. Positivity
of `p_s` therefore gives `r=0`. This proves injectivity of even the projected
middle block. The oddness reduction uses that both residual and gradient are
odd, so their product is even; replacing `p` by `p_s` in a force is an exact
integral identity, not a replacement of the original data law.

## 3. Finite target space, density compactness, and approximation floor

The space

\[
 E_N=\operatorname{span}\{F_*-q_0,
  h\cos((2k+1)\alpha),h\sin((2k+1)\alpha):0\le k\le N\}
\]

is finite-dimensional even though its first generator may have infinitely
many Fourier modes. It is an analysis space containing one specified
reference function, not a finite-state surrogate for the unknown changed-law
trajectory. Its use respects target provenance. Linear dependencies can be
deleted using its fixed `L2(rho)` Gram; the nonzero mode `h cos(alpha)`
ensures the space is nonzero even if `F_*=q0`.

In an `L2(rho)`-orthonormal basis, `C_N(p)` is between `(1/2)I` and `2I`.
The full and hidden quadratic forms are positive on every nonzero vector by
the independently justified continuum injectivity. Their entries depend
continuously on `p` in uniform norm: the gradient kernels are bounded,
the basis functions are fixed bounded continuous functions, and the
integrals defining `T_p b_i` converge in the raw Hilbert norm.

The bounded Lipschitz density class is compact in uniform norm. Its
normalization and bounds are closed, and finite grids plus equicontinuity
give convergent subsequences. The constrained coefficient vectors obey
`|z|<=sqrt(2)`, while `z^T C_N(p)z=1` also prevents their limit from being
zero. Therefore the compact Rayleigh-quotient argument establishes the
positive minima `lambda_N` and `lambda_H,N`, uniformly over the entire
original density class, including the `D=0` case consisting only of the
uniform density. No uniform lower bound as `N` increases follows or is used.

For an infinite target, the weighted coefficient bound gives

\[
 \|q-q_N\|_\infty\le R/(2N+3)^s.
\]

Multiplication by `h=sin^2(2alpha)` costs at most one. Since
`F_*-q_N` lies in `E_N`, the distance of `r_0=F_*-q` from that space is
bounded by this target tail alone. For a target with coefficient cap `N`,
that distance is exactly zero; no approximation of `F_*` is necessary.
The full target may have degree `2N+5`, because multiplying the highest
odd frequency `2N+1` by `h=(1-cos(4alpha))/2` introduces shifts by four.
This is the reason for the terminology clarification in the conclusion.

## 4. Reconstruction of the nonlinear contraction algebra

Write `P=P_N`, `r=r_tau`, `E=||r||_p^2`,
`b=a_N+C_f V tau`, and `delta=C_d sqrt(V tau)`. Projection gives
`||(I-P)r||_p<=b`, while the moving-gradient comparison gives
`||T_theta-T_p||<=delta`. With `||T_p||<=L0`, the two completed-square
inequalities produce

\[
\begin{aligned}
 \|T_\theta r\|^2
 &\ge\tfrac12\|T_p r\|^2-\delta^2E\\
 &\ge\tfrac14\|T_pPr\|^2
                 -\tfrac12\|T_p(I-P)r\|^2-\delta^2E\\
 &\ge(\lambda_N/4-\delta^2)E
                  -(\lambda_N/4+L_0^2/2)b^2.
\end{aligned}
\]

The last line uses orthogonality in the `p`-weighted function norm, not
orthogonality of their images under `T_p`. Thus cross-mode cancellation is
explicitly bounded, with the correct coefficient `L0^2/2`.

When `C_d^2 V T<=lambda_N/8`, the exact unhalved-loss identity gives

\[
 E'\le-(\lambda_N/2)E
                +(\lambda_N+2L_0^2)(a_N+C_fVT)^2.
\]

The ratio of constant forcing to contraction coefficient is

\[
 A_N(T)=2(1+2L_0^2/\lambda_N)(a_N+C_fVT)^2,
\]

which agrees with the frozen statement. Multiplication by
`exp(lambda_N tau/2)` gives the stated bound. Every use of the endpoint
operator is accompanied by its moving-operator error; the training equation
has not been frozen. Constants `V=2(sqrt(10)+2)L1` and
`B0=sqrt(10)+1` are valid from the unit raw ball and `|q|<=1`.

The floor depends on the class, truncation index, reference quantities, and
declared episode length. It is not the final trained risk by definition.
For infinite targets it can be large, and the proof does not show that
some increasing sequence of indices makes the ratio `a_N^2/lambda_N`
vanish. This limitation is correctly acknowledged. For fixed finite `N`,
`a_N=0` and the positive episode can always be shortened to put the floor
below a fixed positive initial-error margin.

## 5. Robust family and stopping information

At the central angle, the frozen finite-mode family has
`q(pi/4)>=b=R/(2sqrt(2))-R/8>0`, while `F_*(pi/4)=0`. The derivative
bound uses `s>=1` essentially:

\[
 \|v'\|_\infty\le\sum_k(2k+1)(|a_k|+|b_k|)\le R.
\]

Since `||q0'||<=6`, `||h'||<=2`, and `||v||<=R`, the claimed
7-Lipschitz target bound is valid. The reference is 76-Lipschitz in angle,
so the residual is 83-Lipschitz. The arc of radius `b/166` has normalized
measure `b/(166*pi)`. Including the lower input density and squared
residual gives

\[
 E(0)\ge (b/(166\pi))\,(1/2)\,(b^2/4)
             =b^3/(1328\pi)=e_0.
\]

The final time restriction gives
`A_N(T_*)<=e0/2` with the displayed factor four inside the square root.
Thus its gain margin

\[
 a_*=(1-e^{-\lambda_N T_*/2})e_0/2>0
\]

is correct. Taking half of the specified positive minimum is a deterministic
choice independent of the unknown `q`, `p`, and observations. The density
minimum already removed dependence on `p`. The remaining dependence is on
class parameters and established reference constants. The stop is theoretical
and presently uses unevaluated endpoint constants; an implementable numerical
evaluation has not been proved. More importantly, `T_ball` must be supplied
by the separate continuation proof. Until then both the stop and its gain
remain conditional, as the frozen file states.

The family is nonempty for every `R>0` and fixed `N>=0`; its center uses
only the index-zero modes and leaves coefficient-budget slack. It has
nonempty relative interior within that finite coefficient space. At `R=0`
the strict margin vanishes, so no strict conclusion is available by this
argument. The zero-noise and `N=0` cases otherwise cause no problem.

## 6. Sampling, centered noise, and an explicit sufficient sample threshold

The sampling lemma evaluates random fluctuations along the deterministic
population path, where independence is available. Its conditional variance
calculation for the centered noise is valid: iid observation pairs imply
conditional independence of their labels given their inputs, and the
conditional means vanish. `d_tau(X_i)` depends on the input and population
path, not on the individual noise realization. Thus

\[
 \mathbb E\|I_m(\tau)\|^2\le L_g^2B_0^2/m,
 \qquad
 \mathbb E[\|N_m(\tau)\|^2\mid X_1,\ldots,X_m]
                       \le L_g^2\sigma^2/m.
\]

The time integral costs exactly `T^2` after Cauchy–Schwarz and Tonelli.
The two Markov bounds and union bound give the stated `eta_m`. No supremum
over time of independent samples, union over a time mesh, or independence
of the empirical path is assumed. If `sigma=0`, its centered noise is zero
almost surely, and the separate noise failure allowance can be omitted.

Subtracting states first under the empirical law is the correct use of the
uniform one-reference premise. The remaining law difference is exactly
`-2 I_m+2 N_m`. The needed premise must hold for that empirical law with
the population path on the tail-bearing side; it is explicitly stated this
way and cannot be replaced by a weaker same-law-only assertion.

For `omega(z)=z sqrt(log(e/z))`, differentiating
`sqrt(log(e/Z))` gives a lower derivative bound `-K/2`. The threshold
`sqrt(log(e/eta))>1+KT/2` guarantees the squared quantity stays positive
and the comparison remains below one. The formula for `O_T` and the
sub-power loss relative to `m^(-1/2)` are correct. The raw-to-prediction
and prediction-to-risk inequalities use the correct constants.

The sufficient finite sample threshold left for assembly can already be
written in terms of the named constants. Let the desired total failure
probability be `delta` and choose positive `delta_I,delta_N` with
`delta_I+delta_N<=delta` (or only `delta_I=delta` if `sigma=0`). Put

\[
 z_*:=\min\{1/2,\ a_*/[4(B_f+1)L_f]\},
 \qquad
 \eta_*:=e\exp\left[-\left\{
       \sqrt{\log(e/z_*)}+KT_*/2\right\}^2\right],
\]
\[
 m\ge\left\lceil\left[
 \frac{2T_*L_g}{\eta_*}
    \left(\frac{B_0}{\sqrt{\delta_I}}
               +\frac{\sigma}{\sqrt{\delta_N}}\right)
                         \right]^2\right\rceil.
 \tag{MC1}
\]

Take at least one sample if the ceiling is zero. Zero denominators do not
occur: in the noiseless case omit the second summand altogether.
The definition gives `O_(T_*)(eta_*)=z_*`, and `z_*<=1/2` ensures the
strict Osgood threshold. Monotonicity gives `O_(T_*)(eta_m)<=z_*`.
Consequently the additive population-test-risk error of the empirical
selected predictor is at most `a_*/2`, leaving gain at least `a_*/2`
with probability at least `1-delta`. This threshold is finite under the
stated premises and uses no target observations to choose the stop.

The source event is uniform over the whole episode, so it remains valid
at a data-dependent stopping time. Any learning guarantee at such a stop
must still use the population bound at that time, or its worst case over
the allowed positive interval. The lemma does not incorrectly equate that
bound with its terminal value. A deterministic `T_*` avoids that issue.

## 7. What the comparison does and does not close

The two audited candidates give a sound conditional population/empirical
learning argument on the fixed finite-`N` robust family, with explicit
symbolic class/reference constants and the sample threshold (MC1).
The finite target-space route is preferable for assembling this particular
learning claim: its exact reference generator removes a needless spectral
tail from the floor and requires no infinite-dimensional spectral theorem.

These are still required for a complete milestone:

- The common arbitrary-law nonlinear construction, original-mixture
  continuation/capture, and the constants used in `T_ball` and `K`.
- A finite paired-hidden activation-displacement proof. Hidden-gradient
  injectivity alone is insufficient; the fixed-readout contrast and
  derivative-continuity mechanism in the population attempt is a compatible
  candidate, to be checked in the assembled argument.
- The actual finite-GF bridge, conditioning on every fixed sample at fixed
  positive epsilon, followed by epsilon decreasing and only then sample
  size increasing. The sampling lemma's bounded conditional-probability
  integration is valid under that bridge and does not reverse these limits.
- Explicit integration of raw sampling error into the selected paired-hidden
  observable if the milestone claims its empirical margin. The existing raw
  error controls provide the needed input, but the observable inequality must
  be written with its actual normalization and evaluation law.

No mathematical change is required to the two principal frozen inequalities.
The clock/index terminology and conditional stopping interpretation above
should be preserved in the next assembled version. This report supplies an
internal analytic check only and does not replace independent complete
promotion reviews.
