# Isolated complete mathematical review — round 2

Candidate: `/tmp/l2-two-sample-proof-0ywjpp/ALL_ANGLE_RAW_GD_ACTION.md`  
SHA-256, verified before and after review: `95dd9f24b44245737bfd3cdcf4692383c24cacae84290d100deb2c21140a08e2`  
Review date: 2026-09-06.

The candidate was the only mathematical document consulted. No previous reports, other mathematical sources, project files, history, external heavy theorems, experiments, or agents were used. The procedural `solve-math-rigorously` skill was used to structure the verification. The candidate was not edited. Line references below refer to the candidate at the hash above.

## Verdict

**PASS for the stated finite-width theorem and its stated probabilistic consequences. No required mathematical corrections were found.**

The exact simultaneous updates are negative-gradient steps in the specified raw metric. The Hessian estimate includes all mixed and curvature terms and grows at most as `sqrt(n)`. The first-exit argument establishes descent without assuming the stability it is meant to prove. The reverse-query variation is controlled in empirical RMS, which is sufficient for the coordinatewise discrete-work absorption at `eta=n^-2`. Equations (2)–(4), including their displayed constants, hold for the actual raw linear interpolation. The proof remains valid when the two-input Gram matrix is singular.

The Gaussian event, its explicit failure bound, and the order of probability and cutoff limits at lines 270–271 are correct. The resulting path tightness is tightness of the empirical first-layer path measures in probability, with quadratic tails controlled in probability. This verdict does not establish a mean-field limit, identify a limiting evolution, compare GD with gradient flow, or provide expectation-level uniform integrability.

The detailed checks below also supply explicit choices for the otherwise generic variation constants and precise definitions for the tail functionals. These are verification details, not additional assumptions needed to repair the proof.

## 1. Setup, optimizer, and quantifiers

Lines 10–53 and 59–67 are consistent. Take positive integers `n,d`, a nonnegative finite horizon `T`, and the globally bounded `C^2` activations stated in the candidate. For a sample `a`, differentiating its prediction gives the Euclidean derivatives

    grad_(W1) f_a = delta1_a x_a^T/n,
    grad_(W2) f_a = delta2_a (h1_a)^T/n,
    grad_(W3) f_a = h2_a/n.

The raw metric has respective weights `d/n`, `1`, and `1/n`. Its inverse therefore gives

    grad_raw f_a = (delta1_a x_a^T/d,
                   delta2_a (h1_a)^T/n,
                   h2_a).

Since `c_a=-2r_a`, the full update direction is

    G_k := (W_(k+1)-W_k)/eta
         = sum_a c_(k,a) grad_raw f_(k,a)
         = -grad_raw L_k.

This checks every learning-rate and normalization factor in (1). In particular, the first-layer metric normalization is essential to the `1/d` in its update.

Initially, `|f_a|<=B_2 b`, hence `sqrt(L_0)<=sqrt(2)(B_2 b+1)=R_0`. Whenever the residual norm is at most `R=R_0+1`,

    sum_a |c_a| = 2 sum_a |r_a| <= 2 sqrt(2) R = K.

For `T>0`, set `N=ceil(T/eta)` and `H=T+1`. Then `1<=N` and `N eta<=H` for `n>=1`. All uses of the padded horizon are justified by this inequality. The separate treatment of `T=0` prevents any undefined terminal index in the work argument.

The constants and the sufficiently-large-width threshold depend only on `T,a,b` and the activation bounds. None of the estimates below introduces dependence on `d`, the input angle, the initial first-layer maximum, or the label pattern.

## 2. Stopped primal bounds and segment control

Lines 65–86 correctly include the candidate exit endpoint without presupposing a bound on its residual. Every update producing that endpoint starts at a node with residual norm at most `R`.

The readout update obeys

    ||Delta W3||_infinity <= eta K B_2.

Summing through at most `N` updates yields `||W3_k||_infinity<=b+H K B_2=M`. At an admissible old node,

    ||delta2_a||/sqrt(n) <= P_2 M,
    ||h1_a||/sqrt(n) <= B_1.

Consequently the operator norm of its second-layer increment is at most

    (eta/n) sum_a |c_a| ||delta2_a|| ||h1_a||
      <= eta K P_2 M B_1.

Summing proves `||W2_k||_op<=a+H K P_2 M B_1=A`, including the candidate exit endpoint. Convexity gives the same bounds on both raw parameters throughout the intervening line segments. At any such parameter value, recomputing the hidden fields gives

    ||delta2_a||/sqrt(n) <= P_2 M,
    ||q1_a||/sqrt(n) <= A P_2 M = Q.

No linear interpolation of a nonlinear hidden field is used in these assertions. No bound on `W1`, `z1`, or a coordinatewise reverse field is needed here.

## 3. Complete raw-metric Hessian check

Lines 90–123 contain a valid bilinear Hessian estimate. To check all terms, write `p_U=U1 x_a` and `p_V=V1 x_a`, and let

    alpha = (sqrt(d/n)||V1||_F, ||V2||_F, ||V3||/sqrt(n)),
    beta  = (sqrt(d/n)||U1||_F, ||U2||_F, ||U3||/sqrt(n)).

For unit raw tangents, the sums of their squared components are at most one; bounding each component by one, as the candidate does, is legitimate. Input normalization gives

    ||p_V||/sqrt(n) <= alpha_1,
    ||D_V z2_a||/sqrt(n) <= B_1 alpha_2 + A P_1 alpha_1.

With `J=B_1+A P_1`, differentiation of the readout then gives

    |D_V f_a|
      <= B_2 alpha_3 + M P_2(B_1 alpha_2+A P_1 alpha_1)
      <= B_2+M P_2 J = F_*.

The exact mixed derivative of the second preactivation is

    D_U D_V z2_a
      = V2[phi1'(z1_a) p_U]
        + U2[phi1'(z1_a) p_V]
        + W2[phi1''(z1_a) p_U p_V].

Products inside brackets are componentwise. In the empirical RMS norm, the first two terms are bounded by

    P_1(alpha_2 beta_1 + beta_2 alpha_1).

For the last term, the elementary product estimate

    ||p_U p_V||_2 <= ||p_U||_2 ||p_V||_2

gives the RMS bound `A L_1 sqrt(n) alpha_1 beta_1`. This is the only width-growing contribution needed in this calculation.

There are exactly four terms in the mixed prediction derivative:

    D_U D_V f_a
      = (V3)^T[phi2'(z2_a) D_U z2_a]/n
        + (U3)^T[phi2'(z2_a) D_V z2_a]/n
        + (W3)^T[phi2''(z2_a)(D_U z2_a)(D_V z2_a)]/n
        + (W3)^T[phi2'(z2_a) D_U D_V z2_a]/n.

The readout/hidden cross terms together are bounded by `2 P_2 J`. The top curvature term is bounded by

    M L_2 (||D_U z2_a||/sqrt(n))(||D_V z2_a||/sqrt(n))
      <= M L_2 J^2.

This uses the coordinatewise bound `||W3||_infinity<=M`, as required; an RMS bound alone would not justify this particular estimate. The last term is bounded by

    M P_2(2P_1+A L_1 sqrt(n)).

Adding these contributions gives exactly (7). This expansion includes the first-layer curvature, both first-/second-layer cross contributions, the top-layer curvature, and both readout cross contributions. There is no omitted simultaneous-update or mixed-layer term.

## 4. Residual bootstrap and actual discrete descent

Lines 125–147 close the stopping argument. At an admissible old node,

    ||G_k||_raw <= K F_*.

The gradient bound for each prediction holds throughout the raw segment by the independently established `A,M` bounds. Integrating the directional derivative along that segment gives, for `0<=s<=1`,

    |f_a(W_k+s eta G_k)-f_a(W_k)| <= eta K F_*^2.

Thus the residual norm is at most `R+sqrt(2) eta K F_*^2`, including at the candidate exit endpoint. Choosing `sqrt(2) eta K F_*^2<=1` bounds the residual on the entire segment by `R+1` without first assuming descent.

For unit raw tangents the loss Hessian satisfies

    ||D^2 L||_raw
      <= 2 sum_a ||grad_raw f_a||_raw^2
         + 2 sum_a |r_a| ||D^2 f_a||_raw
      <= 4 F_*^2 + 2 sqrt(2)(R+1) F_**(n)
      = H_*(n).

Applying the one-dimensional integral Taylor identity on this same segment gives

    L_(k+1)
      <= L_k - eta ||grad_raw L_k||_raw^2
         + (eta^2/2) H_*(n) ||grad_raw L_k||_raw^2.

Therefore `eta H_*(n)<=1` proves (9). Applying this at every step through a proposed first exit yields `L_(k+1)<=L_0<=R_0^2`; this contradicts the exit criterion `sqrt(L)>R_0+1`. The endpoint and segment estimates used in this reasoning were obtained without bounding the new residual, so the argument is not circular.

Since `H_*(n)=O(1+sqrt(n))`, both small-step requirements hold at `eta=n^-2`. Summing (9) also gives the valid finite-horizon check

    sum_(k=0)^(N-1) eta ||grad_raw L_k||_raw^2 <= 2 L_0.

The later coordinatewise work estimate is stronger in the direction needed for cubic velocities; it is not being inferred merely from this averaged dissipation bound.

## 5. Controlled-query variation in RMS

Lines 156–190 are correct. Here is one explicit choice of constants, showing that the generic `C_T` hides no width dependence. Write `||u||_n=||u||_2/sqrt(n)` and define

    D_1 = K P_1 Q,
    D_W = K P_2 M B_1,
    D_3 = K B_2,
    D_z = D_W B_1 + A P_1 D_1,
    D_delta = P_2 D_3 + M L_2 D_z,
    D_q = D_W P_2 M + A D_delta,
    D_c = 4 K F_*^2,
    D_v = D_c Q + K D_q.

The first-layer increment follows directly from the Gram entries `|C_ab|<=1`:

    ||Delta z1_a||_n <= eta D_1.

The exact difference identity

    Delta z2_a = (Delta W2) h1_(k,a) + W2_(k+1) Delta h1_a

includes the cross increment and gives `||Delta z2_a||_n<=eta D_z`. Similarly,

    Delta delta2_a
      = (Delta W3) phi2'(z2_(k,a))
        + W3_(k+1)[phi2'(z2_(k+1,a))-phi2'(z2_(k,a))]

gives `||Delta delta2_a||_n<=eta D_delta`. The exact transpose difference then yields

    ||Delta q1_a||_n
      <= ||Delta W2||_op ||delta2_(k,a)||_n
         + ||W2_(k+1)||_op ||Delta delta2_a||_n
      <= eta D_q.

This is strictly an `l^2` operator estimate. It does not assume any higher-moment mapping property of the transpose.

The segment prediction bound in the previous section gives `sum_a |Delta c_a|<=eta D_c`. For `v_(k,a)=c_(k,a) q1_(k,a)`, use

    Delta v_a = (Delta c_a) q1_(k,a) + c_(k+1,a) Delta q1_a.

After descent is established, both endpoints satisfy the residual bound. Consequently

    sum_a ||Delta v_a||_n <= eta(D_c Q+K D_q)=eta D_v,
    sum_a ||v_(0,a)||_n <= K Q.

Applying the triangle inequality in empirical RMS to the nonnegative envelope at lines 181–182 proves

    ||U||_n <= K Q+(N-1)eta D_v <= K Q+H D_v.

Thus one can take `V_T=K Q+H D_v`; alternatively, the candidate's common `C_T` can be enlarged to cover `D_v` and all preceding increment constants. The consequences

    sum_a |v_(k,a,i)| <= U_i,
    max_i U_i <= sqrt(n) V_T

are valid for every update node `0<=k<=N-1`. There is no assumption of independence of evolved neurons, and no width-independent coordinate maximum is asserted.

## 6. Pointwise work identity and absorption

Lines 194–222 prove the required coordinatewise action bound. To avoid confusing the input dimension with the candidate's coefficient vector, denote that vector in this review by

    s_(k,i,a)=v_(k,a,i) phi1'(z1_(k,a,i)).

The exact first-layer row velocity is `(1/d)sum_a s_(k,i,a) x_a`. Hence

    e_(k,i) = d ||(w_(k+1,i)-w_(k,i))/eta||^2
            = s_(k,i)^T C s_(k,i),
    Delta z_i = eta C s_(k,i).

Because `C` is positive semidefinite with eigenvalues at most two, `C^2<=2C` as quadratic forms. This proves all of (11), including

    |Delta z_i|^2 <= 2 eta^2 e_(k,i).

Taylor's scalar remainder for each activation is at most `(L_1/2)|Delta z_(a,i)|^2`. Multiplying by the possibly signed controls and summing gives

    sum_a v_(k,a,i) Delta h1_(a,i) = eta e_(k,i)+R_(k,i),
    |R_(k,i)|
      <= (L_1/2)sum_a |v_(k,a,i)| |Delta z_(a,i)|^2
      <= L_1 eta^2 U_i e_(k,i).

For `A_i=sum_k eta e_(k,i)`, summing this estimate yields

    sum_k sum_a v_(k,a,i) Delta h1_(a,i)
      >= (1-eta L_1 U_i) A_i.

The pointwise absorption is valid because

    eta L_1 U_i <= L_1 V_T n^(-3/2) <= 1/2

for all sufficiently large widths. It does not replace a coordinatewise estimate by an average: the intermediate deterministic bound `max_i U_i<=sqrt(n)V_T` explicitly supplies the required maximum.

The discrete summation-by-parts formula displayed in the candidate is exact. Let `s_0=sum_a |v_(0,a,i)|` and `D=sum_(k=1)^(N-1)sum_a |v_(k,a,i)-v_(k-1,a,i)|`, so `U_i=s_0+D`. Its upper bound is

    B_1(sum_a |v_(N-1,a,i)|+s_0+D)
      <= B_1(U_i+U_i)=2B_1 U_i.

Combining the lower and upper bounds proves `A_i<=4B_1 U_i`, exactly (13). The signs of the controls do not affect this argument. If `U_i=0`, all update coefficients vanish and `A_i=0`, so no division by a potentially zero quantity is involved. For `N=1`, both variation sums are empty and the formulas remain valid.

## 7. Raw interpolation and all displayed moment constants

Lines 224–239 correctly use raw first-layer interpolation: `z_i(t)` is affine on each mesh cell because `W1(t)` is affine and the inputs are fixed. Its cell velocity is `C s_(k,i)`. Since

    |s_(k,i)| <= P_1 sum_a |v_(k,a,i)| <= P_1 U_i,

the pointwise speed is at most `2P_1 U_i`. Equation (11) also gives

    integral_0^(N eta) |dot z_i|^2 dt <= 2 A_i.

Therefore

    integral_0^(N eta) |dot z_i|^3 dt
      <= (2P_1 U_i)(2A_i)
      <= 16 B_1 P_1 U_i^2.

Averaging and using `||U||_n<=V_T` proves (3) with its stated constant. The recomputed activation is absolutely continuous and satisfies

    dot h_i = diag(phi1'(z_i)) dot z_i

almost everywhere. Its cubic integral is at most `P_1^3` times the preactivation cubic integral, proving exactly the coefficient `16 B_1 P_1^4 V_T^2` in (4).

For the path maximum, Cauchy–Schwarz and `T<=H` give

    sup_(t<=T)|z_i(t)| <= |z_i(0)|+sqrt(2H A_i).

Raising to the fourth power and using `(a+b)^4<=8(a^4+b^4)` yields

    sup_(t<=T)|z_i(t)|^4
      <= 8|z_i(0)|^4+32H^2 A_i^2
      <= 8|z_i(0)|^4+512B_1^2 H^2 U_i^2.

This verifies the `8` and `512` in (2). The estimates were proved on all `N` full cells and restrict to `[0,T]`, so a partial terminal cell causes no error. Values assigned to velocities at the finitely many mesh endpoints do not change any integral. No interpolation of hidden activations is substituted for the recomputed activation.

For completeness, all width requirements can be made simultaneous. Write

    F_**(n)=f_0+f_1 sqrt(n),
    f_0=2P_2 J+M L_2 J^2+2M P_2 P_1,
    f_1=M P_2 A L_1,
    H_0=4F_*^2+2sqrt(2)(R+1)f_0,
    H_1=2sqrt(2)(R+1)f_1.

It suffices to take integer `n` at least the maximum of

    1,
    (sqrt(2) K F_*^2)^(1/2),
    (2H_0)^(1/2),
    (2H_1)^(2/3),
    (2L_1 V_T)^(2/3).

The second entry ensures the residual-segment condition; the next two ensure `H_0/n^2+H_1/n^(3/2)<=1`; the last ensures work absorption. All constants are defined before this choice and independent of width. This confirms the exact finite-width quantifier asserted in Section 1.

## 8. Singular Gram matrices and all-angle scope

Write `rho=C_12`. The Gram matrix is

    C = [[1,rho],[rho,1]],    -1<=rho<=1,

with eigenvalues `1+rho` and `1-rho`. Every use of the input geometry is justified either by `|C_ab|<=1`, `||C||_op<=2`, or `C^2<=2C`. No inverse, pseudoinverse, positive lower eigenvalue, or angle-dependent constant is used.

At alignment, `rho=1`, the energy and velocity are

    e=(s_1+s_2)^2,
    dot z=(s_1+s_2,s_1+s_2).

At antiparallel alignment, `rho=-1`, they are

    e=(s_1-s_2)^2,
    dot z=(s_1-s_2,-s_1+s_2).

In both cases `|dot z|^2=2e`, even when nonzero coefficients cancel in the Gram kernel. These are exactly the degenerate cases needed by the work proof. The actual identities between the two first-layer preactivations imposed by `x_2=+x_1` or `x_2=-x_1` are preserved by the raw updates and interpolation. Conflicting labels do not affect the estimates; no zero-loss or fitting conclusion is claimed.

## 9. Gaussian event and its exact probability bound

Lines 243–264 give a valid elementary event estimate, including singular angles and deterministic input pairs varying with width.

For the second layer, a maximal `1/4`-separated subset of the unit sphere is a `1/4`-net. The disjoint radius-`1/8` balls around its points lie inside the radius-`9/8` ball, giving at most `9^n` points by volume comparison. For any matrix `W`, approximating each of two unit test vectors by this net gives

    ||W||_op <= 2 max_(u,v in net) |u^T W v|.

Indeed the total approximation error is at most `(1/4+1/4)||W||_op`. For each deterministic pair of net vectors, `u^T W2_0 v` is centered Gaussian with variance `1/n`. The Gaussian moment-generating function and Markov's inequality give

    P(|u^T W2_0 v|>4) <= 2 exp(-8n).

Union over at most `9^(2n)` test pairs yields exactly

    P(||W2_0||_op>8) <= 2 exp(-(8-2log 9)n).

For the readout, the variance is `n^-2`, so the scalar tail at level one is at most `2exp(-n^2/2)`. Union over its `n` coordinates gives the stated `2n exp(-n^2/2)`.

For a deterministic normalized input pair, the initial first-layer row pairs are independent across neurons and centered Gaussian with covariance `C`. Their marginals are standard normal. To verify the fourth moment, represent a pair as

    (G, rho G+sqrt(1-rho^2) H)

with independent standard normals `G,H`, including `rho=+/-1`. This gives `E[z_1^2 z_2^2]=1+2rho^2` and therefore

    E|z_i(0)|^4=3+2(1+2rho^2)+3=8+4rho^2<=12.

The elementary inequality `(u+v)^4<=8(u^4+v^4)` for nonnegative `u,v`, applied to the two squared coordinates, gives

    E|z_i(0)|^8 <= 8(E G^8+E G^8)=1680.

Here `E G^8=105` follows directly by Gaussian integration by parts, using `E G^(2m)=(2m-1)E G^(2m-2)`. No independence between the two coordinates is needed for this upper bound. Independence of rows gives variance of their empirical fourth moment at most `1680/n`. Since its mean is at most 12, Chebyshev yields

    P((1/n)sum_i |z_i(0)|^4>13) <= 1680/n.

Define the precise event

    E_n = {||W2_0||_op<=8}
          intersect {||W3_0||_infinity<=1}
          intersect {(1/n)sum_i |z_i(0)|^4<=13}.

A union bound proves

    P(E_n^c) <= 1680/n
                +2exp(-(8-2log 9)n)
                +2n exp(-n^2/2).

Mutual independence of these three events is not needed. The displayed bound is uniform over each deterministic choice of normalized inputs, even when their dimension or angle changes with width. It does not give an event holding simultaneously for every input pair or for input pairs selected after observing the initialization. The candidate expressly respects this distinction.

## 10. Uniform integrability in probability and path tightness

Lines 266–280 are valid with the following precise empirical interpretation. Fix `T`, set `a=8,b=1`, and take widths above the deterministic threshold already verified. On `E_n`, let

    C_path=104+512B_1^2 H^2 V_T^2,
    C_vel=16B_1 P_1 V_T^2,
    C_hvel=16B_1 P_1^4 V_T^2.

Then the empirical mean of `||z_i||_infinity^4` is at most `C_path`, while the empirical cubic velocity integrals are at most `C_vel` and `C_hvel` for `z` and the recomputed `h`, respectively.

For a cutoff `r>0` (renamed here to distinguish it from the residual stopping level), define

    F_n^path(r)
      = (1/n)sum_i ||z_i||_infinity^2
                      1_{||z_i||_infinity>r},

    F_n^vel(r)
      = (1/n)sum_i integral_0^T |dot z_i(t)|^2
                                  1_{|dot z_i(t)|>r} dt.

On `E_n` the elementary cutoff inequalities give

    F_n^path(r)<=C_path/r^2,
    F_n^vel(r)<=C_vel/r.

Replacing `dot z` by `dot h` gives the analogous bound with `C_hvel`. A quadratic path tail defined by a supremum of pointwise truncated values is also bounded by the displayed path functional.

For either functional and any `epsilon>0`, choose `r` large enough that its deterministic bound is at most `epsilon`. Then for all sufficiently large widths,

    P(F_n(r)>epsilon)<=P(E_n^c).

Taking the width limsup and then the cutoff limit proves exactly the assertion at lines 270–271. No expectation on `E_n^c` enters this argument, so it proves no expectation-level uniform integrability. The `O(1/n)` failure term also supplies no summable bound across all widths; no almost-sure all-width conclusion follows from this event calculation.

To verify the path tightness statement directly, set

    mu_n=(1/n)sum_i delta_(z_i(.))

as a random probability measure on `C([0,T];R^2)`. Absolute continuity and Hölder's inequality give, for each path,

    [z_i]_(2/3)^3 <= integral_0^T |dot z_i(t)|^3 dt,

where the left side is the cube of the `2/3` Hölder seminorm. Thus its empirical mean is at most `C_vel` on `E_n`. For `L>0`, let

    K_L={gamma: ||gamma||_infinity<=L and [gamma]_(2/3)<=L}.

This set is compact in the uniform topology: the common Hölder bound controls errors between sufficiently fine time-grid values, bounded grid values admit finite approximations, and uniform limits preserve both defining bounds. Completeness of continuous paths under the uniform norm then gives compactness. This uses no population existence or evolution theorem.

On `E_n`,

    mu_n(K_L^c)<=C_path/L^4+C_vel/L^3.

For each desired mass tolerance, choosing `L` sufficiently large makes this bound smaller than that tolerance; the probability that the bound fails tends to zero with `P(E_n^c)`. This proves tightness in probability of the empirical first-path measures in the stated uniform topology. The previously verified path quadratic tails supply the stated second-moment control. This assertion concerns empirical measures, not a width-independent bound on every individual neuron's path.

For deterministic families with uniformly bounded initial empirical fourth moments and the stated initial operator/readout bounds, the same argument is deterministic for all sufficiently large widths. The probabilistic conclusion adds only the Gaussian event estimate to these deterministic bounds.

## 11. Required corrections versus optional improvements

### Required mathematical corrections

None. Every requested part of the finite-width argument has been checked: optimizer scaling, raw Hessian terms, segment residual control, first-exit descent, exact product differences, transpose RMS variation, the controlled-query envelope, coordinatewise work absorption, all three raw interpolation bounds, singular Gram angles, the Gaussian event and its constants, and the scope of the probabilistic tail and tightness conclusions.

### Optional presentation improvements

1. Define `rho=C_12` before the Gaussian fourth-moment formula. Its intended meaning is recoverable, and its omission does not change the estimate.
2. Write the two tail functionals explicitly and name the empirical path measure in Section 6. The formulas in Section 10 of this review make the existing interpretation precise.
3. State the short Hölder-seminorm and compact-set argument behind the final tightness sentence. It follows from the established estimates, as verified above.
4. If a completely explicit width threshold is desired, display one choice of the variation constant and the simultaneous small-step conditions. Sections 5 and 7 above provide such choices. Optimal constants are unnecessary for the asserted result.

These are optional clarifications, not missing estimates or changes to the theorem's scope. No candidate edit is required for the mathematical verdict. The candidate's explicit exclusions of a joint MF/GF theorem, population-law identification, uniqueness/restart, and second-layer/reverse-field tail control must remain part of the interpretation of this result.
