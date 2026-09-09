# Three-input L3 nonlinear-reference route, 2026-09-08

## Verdict and fixed target

No positive horizon-independent cutoff for the complete three-input theorem has been proved by this route. In particular, neither `theta <= c delta^p` for any finite p nor an exponential cutoff is currently justified. This is a failure to complete a sufficient theorem, not a counterexample for positive theta.

The model here has **three hidden layers**, activation `phi(z)=a z+e atan(z)` with `a=1-e`, `0<e<=1/2`, the original raw metric, all binary labels, and every realizable unit-input Gram satisfying `|Gamma_ij|<=1-delta`. Singular input Grams are included. The `three_sample_odd_activation_depth2/CONTRACT.md` is a different depth and supplies no theorem for the present question.

The mathematical sources read were:

- `odd_activation_lower_powers_three_inputs/THREE_INPUT_ANALYSIS.md`, in full;
- `odd_mixture_separation_quantitative/THREE_INPUT_GEOMETRY.md`, including initialization and its matching small-separation construction;
- the model, scope and affine clock in `two_sample_odd_activation_theorem/PROOF.md`;
- the controlled interval and global capped-flow argument in `three_sample_separated_angle_theorem/PROOF.md`;
- source-tail and continuation passages in `two_sample_odd_activation_theorem/SOURCE_AND_LIMIT_BRIDGE.md` and `odd_mixture_separation_quantitative/REPORT.md`.

No experiment, old-file edit or commit was performed.

## 1. What the existing sharp initialization estimate says

Writing `s_delta=delta(2-delta)` and `b_3=(1-2 E(1+G^2)^(-1))/sqrt(6)`, the third-chaos certificate gives

\[
 Q_1(0)\succeq e^2b_3^2s_\delta^2 I_3/3,
 \qquad Q_3(0)\succeq a^4 Q_1(0).
\]

For fixed `d>=2`, `0<delta<=1/4`, and `0<e<=1/2`, the infimum over admissible geometries of the first-feature minimum eigenvalue is bounded above and below by absolute constants times `e^2 delta^2`. This is a sharp statement about initialized feature conditioning. It is not a sufficient upper bound on e for the complete population theorem.

The positive lower bound at every e>0 removes initial cancellation. Taking e smaller simultaneously weakens the nonlinear margin. An affine perturbation argument cannot regard its reference margin as a positive delta-only number in the singular directions.

## 2. An exact Gram identity: readout linearity does not preserve initialized coercivity

Let `v` denote all hidden raw parameters and let `H(v): R^3 -> H_3` be the column operator whose columns are the final features. The predictor is `f=H(v)^* C`, the residual is `r=f-y`, and `Q=H^*H`. These identities hold on every already-existing strong solution with the scalar network chain rule. They do not construct that solution.

For a fixed vector c in sample space, differentiation gives

\[
 \frac{d}{dt}c^TQc
 =2\left\langle Hc,\,D(Hc)[\dot v]\right\rangle,
 \qquad
 \dot v=-\sum_i r_i\nabla_v\langle C,H_i\rangle .
 \tag{1}
\]

There is no positivity in the right-hand side of (1). The sign of the hidden tangent matrix alone does not fix it: positivity of the full prediction kernel implies monotone loss, not monotone feature Gram.

At `C(0)=0`, the exact initial identities are

\[
 \dot v(0)=0,\quad \dot C(0)=H_0y,
 \quad \ddot v(0)=D(Hy)_0^*H_0y
 =\nabla_v\tfrac12\|H(v)y\|^2\big|_{v_0}.
 \tag{2}
\]

Consequently the label projection obeys

\[
 \left.\frac{d^2}{dt^2}y^TQ(t)y\right|_{t=0}
 =2\|D(Hy)_0^*H_0y\|^2\ge0.
 \tag{3}
\]

Equation (3) concerns one projection and one initial derivative. It gives neither `Q(t)>=Q(0)` nor a lower bound in all sample directions.

A simple readout-linear model disproves any attempt to deduce matrix monotonicity from readout linearity, zero initial readout, and gradient flow alone. Let the hidden variable be a real number v, the readout be `(C_1,C_2)`, and let feature columns in `R^2` be

\[
 H_1(v)=(1+v,0),\qquad H_2(v)=(0,1-2v),
 \qquad y=(1,1),\quad v(0)=0,\ C(0)=0.
\]

Then `Q(0)=I_2`, `dot v(0)=0`, and (2) gives `ddot v(0)=1-2=-1`. Therefore

\[
 Q_{11}(t)=1-t^2+o(t^2),\qquad
 Q_{22}(t)=1+2t^2+o(t^2).
\]

In particular `lambda_min Q(t)<lambda_min Q(0)` for all sufficiently small positive t. This example is not asserted to be the particular Gaussian-initialized L3 network. It identifies which additional architecture-specific argument would be required before a Gram-propagation claim could be used for that network.

## 3. Exact null-direction tangent bound on bounded raw states

A useful new consequence of the Gram-null decomposition is a bound on the **full raw tangent kernel**, not only on predictions.

Let `v in ker Gamma` now denote a fixed sample coefficient vector. Put

\[
 T_\ell=\sum_i v_i\arctan z_i^\ell.
\]

The exact activation decomposition yields

\[
 v^Tf=eN_v,\qquad
 N_v=\langle C,a^2BA T_1+aB T_2+T_3\rangle.
 \tag{4}
\]

Let `R` be raw distance from canonical initialization and set `U=11+R>=1`. The initialized first projected norms are one, initialized action norms are at most ten, and `C_0=0`. Thus the projected first-layer norms, `||A||`, `||B||`, and `||C||` are at most U; also `||h_i^1||<=U`, `||h_i^2||<=U^2`, since `phi` is 1-Lipschitz and vanishes at zero.

Write a hidden raw perturbation as `(dw,dA,dB)` and let
`p_w=sqrt(d)||dw||_2`, `p_A=||dA||_HS`, and `p_B=||dB||_HS`. Boundedness of the arctangent derivative and of `phi'` gives

\[
 \|T_\ell\|_2\le\tfrac\pi2\|v\|_1,
\]

\[
 \|dT_1\|_2\le\|v\|_1p_w,
 \quad \|dT_2\|_2\le\|v\|_1U(p_A+p_w),
 \quad \|dT_3\|_2\le\|v\|_1U^2(p_B+p_A+p_w).
 \tag{5}
\]

For example `dz_i^2=dA h_i^1+A phi'(z_i^1)dz_i^1`, which proves the middle inequality. The next layer gives the final inequality in exactly the same manner. The scalar differentiation below is valid by the existing weighted scalar chain rule; it does not require a Frechet derivative of the full Nemytskii feature map on all of L2.

Differentiate (4), distribute the action derivatives, and use (5). The coefficient of `p_w` is at most `3 ||v||_1 U^3`; that of `p_A` is at most `(pi/2+2)||v||_1 U^3`; that of `p_B` is at most `(pi+1)||v||_1 U^3`. The readout perturbation coefficient is at most `(3pi/2)||v||_1 U^2`. Since each block perturbation norm is bounded by the full raw norm and U>=1, their sum gives

\[
 |dN_v|\le(6+3\pi)\|v\|_1U^3\|d\Theta\|_{\rm raw}
 \le16\|v\|_1U^3\|d\Theta\|_{\rm raw}.
 \tag{6}
\]

Let `K` be the sum of the four raw kernel blocks. By its gradient-Gram definition and (4)-(6),

\[
 v^TKv=\|\nabla_\Theta(v^Tf)\|_{\rm raw}^2
 \le256e^2\|v\|_1^2(11+R)^6.
 \tag{7}
\]

For `||v||_2=1` this is at most `768 e^2(11+R)^6`. Thus at a bounded raw state the complete tangent kernel in an affine-null direction becomes small with e; adding hidden kernel blocks does not supply an e-independent coercivity margin on an e-independent raw ball.

This is an upper bound, not a failure of positive coercivity. Together with the previously proved fitting-distance bound `R>=(pi e)^(-1/3)-11` in the equilateral equal-label case, it explains why a successful reference must retain nonlinear dynamics over a growing state range.

## 4. Why a single-residual clock does not extend by notation

On a true strong flow, `dot r=-K r`. As long as r is nonzero, its unit direction `q=r/||r||_2` satisfies exactly

\[
 \dot q=-(I-qq^T)Kq.
 \tag{8}
\]

Positivity of K implies loss decay but does not set the right side of (8) to zero. Generic three-input folded Grams have no transitive permutation symmetry, so no symmetry forces a constant residual direction. A Gram-null decomposition gives an exact algebraic relation (4); it does not turn the true vector-residual dynamics into ascent of one fixed scalar objective.

For the symmetric equilateral case, the existing scalar lemma does supply a conditional nonlinear clock `S<=||H_0||^(-2)`, with `||H_0||=Theta(e)` at fixed separation. It is conditional on the strong construction and has size `Theta(e^(-2))`. Inserting this into the current affine controlled-source condition

\[
 e\le[2K\exp(KS)]^{-1}
\]

is not a solution. Even with fixed `K>=k_0>0`, it would require `e exp(c/e^2)<=C`, which fails as e tends to zero. Permitting the constants to deteriorate with the large raw ball cannot repair this particular implication.

## 5. The actual missing nonlinear theorem

A sufficient proof cannot stop at the sharp `e^2 delta^2` initialization margin. One viable nonlinear-reference route would need all of the following, with constants independent of width, cutoff and physical horizon:

1. A reference containing the positive nonlinear signal in `ker Gamma`, and a proof that the true vector-residual path stays in its admitted state/source region. Any radius and clock may depend on e and delta; their dependence must be inserted in the next steps rather than suppressed.
2. A trained source-response estimate for that nonlinear reference which remains valid at the required growing radius and clock. In particular it must replace, rather than merely reuse with theta-dependent S, the present smallness criterion involving `e exp(KS)`.
3. Uniform source tails sufficient for cap removal and uniqueness against bounded-primal nonsymmetric strong competitors, plus reached-state restart.
4. A trained-law nondegeneracy argument at each finite time, followed by the original full-sequence finite-GF/raw-GD and observable bridges with their hypotheses verified.

A proposed time-dependent positive lower bound on the full kernel could help establish residual-clock control, but it would not alone establish points 2-4. Likewise, the energy bound of already-existing strong GF is not a construction of that GF in the raw infinite-dimensional state space.

**Current mathematical conclusion:** the sharp result available on this route is the initialized `e^2 delta^2` conditioning scale and the new exact tangent bound (7). There is no proved three-input activation cutoff whose small-delta exponent can yet be optimized. The two-input `delta^2` theorem cannot be transferred to this class by choosing e still smaller.

## 6. Interval thresholds, one witness, and order-one activations

Two questions must be distinguished:

- **An interval theorem:** find `eta(delta)>0` such that *every* `0<e<=eta(delta)` has the full result.
- **A witness theorem:** choose one `e=e(delta)` with the full result. This witness need not be small and need not imply an interval down to zero.

Neither has been established for three inputs by the current route. The small-e affine obstruction does not refute the possibility of a constant witness `e(delta)=e_0`; in particular, it is not a reason to assume the best witness should tend to zero. A constant witness would answer the user's small-delta question more strongly than a vanishing polynomial, provided the full theorem were proved.

I checked the bounded endpoint `e=1`, namely pure arctangent, separately. An existing theorem in `nonlinear_activation_operator_ide/ARCTAN_THEOREM_AND_PROOF.md` proves global feature/physical dynamics and width limits for **one sample and two hidden layers**. It uses a natural coordinate and a preserved Gaussian readout envelope; its displayed initialization has a standard Gaussian readout and its observable statement is also narrower. That is not a theorem for three inputs and three hidden layers under the present initialization and complete observable contract. Its proof cannot simply be cited after changing the depth and sample count.

Pure arctangent does provide the exact compact-clock pointwise estimate

\[
 |C(s)-C(0)|\le (\pi/2)S
 \quad\text{when }\int_0^S\sum_i|c_i(s)|\,ds\le S,
\]

because `C'=sum_i c_i atan z_i^3`. With `C(0)=0`, the top backward field is pointwise bounded on that clock. But the next incoming field is

\[
 q_i^2=B_0^*\delta_i^3+(B-B_0)^*\delta_i^3.
\]

The trained part is controlled by its rank-one integral. The first term is an adaptively queried initialized transpose; bounded input and an L2 operator bound do not imply the source-tail estimate required for the nonlinear multiplier `q_i^2 phi''(z_i^2)`. This is the depth-three middle-adjoint tail issue explicitly recorded in `leaky_arctan_depth3_operator_ide/ACTIVATION_COMPARISON.md`. No full pure-arctangent L3 three-input theorem was found in the local mathematical sources.

The distinction is structural even at the bottom natural coordinate. For one input, `dot z=phi'(z)q` is linearized by `Theta'(z)=1/phi'(z)`. For multiple correlated inputs, the projected update contains the vector fields

\[
 V_i(z)=\Gamma e_i\,\phi'(z_i).
\]

For `i!=j` their Lie bracket is

\[
 [V_i,V_j]
 =\Gamma_{ij}\{\Gamma e_j\,\phi''(z_j)\phi'(z_i)
              -\Gamma e_i\,\phi''(z_i)\phi'(z_j)\},
\]

which need not vanish. Thus a scalar coordinate change applied independently to each projected sample does not reproduce the one-input cancellation for a general correlated Gram. This does not rule out a different joint transformation.

**Final status of the endpoint check:** pure arctangent and fixed mixtures remain possible constant-witness routes. Their boundedness or derivative floor does not currently discharge the full three-input L3 proof obligations. The strongest honest conclusion is absence of a proved global cutoff or witness, rather than an asserted asymptotic exponent.
