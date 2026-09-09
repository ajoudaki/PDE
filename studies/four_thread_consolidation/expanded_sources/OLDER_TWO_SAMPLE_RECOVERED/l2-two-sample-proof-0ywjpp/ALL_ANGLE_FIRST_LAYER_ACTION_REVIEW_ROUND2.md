# Isolated review of the all-angle first-layer action result

Reviewed on 2026-09-06. The sole mathematical input was the entire 283-line file `/tmp/l2-two-sample-proof-0ywjpp/ALL_ANGLE_FIRST_LAYER_ACTION.md`.

Verified source SHA256:

`9c0349c8aa76a6d7b260c34fd45a9e1d5dd8caf637a5ecbee0b16028bbd72ac9`

No prior review, project material, other mathematical file, experiment, agent, or external mathematical source was consulted. The procedural `solve-math-rigorously` skill was used. The candidate was not edited. The compactness verification below supplies an elementary argument rather than invoking an external compactness theorem for probability measures.

## Verdict and findings

**PASS for the stated finite actual-gradient-flow result and its stated first-path consequences.** Equations (1)–(11), the displayed constants, global finite-dimensional existence and uniqueness, both singular input angles, the initialization probability estimate, first-layer uniform integrability, and first-path quadratic-Wasserstein relative compactness check out under the stated assumptions. There is no required mathematical correction.

This verdict concerns the precise flow (1), which is gradient flow in the fixed parameter metric identified below. Its uniform deterministic estimates assume the stated initial bounds on the second-layer spectral norm and readout coordinate maximum. The path fourth-moment and compactness consequences additionally require a common initial empirical fourth-moment bound. The specified Gaussian initialization supplies these assumptions on the explicitly quantified events. No assertion about population-flow identification or uniqueness, a uniquely restartable population flow, or a GD/GF comparison is certified.

Required findings: none.

Optional presentation improvements, none affecting the verdict:

1. State the path space and its quadratic-Wasserstein metric explicitly, as below, and name the scalar moment constants differently from the input Gram matrix `C`.
2. Add the finite-approximation argument below after the path compactness discussion if the document is intended to contain every measure-compactness step without appealing to a known criterion. The existing step is mathematically sound but compressed.

## 1. Normalizations, loss metric, and finite flow

Take positive integers `n,d`, a finite horizon `T >= 0`, fixed labels with absolute value one, and the stated bounded `C^2` activations. The two activations need not agree. The bound on the second derivative of the first activation is sufficient for the regularity assertion, although its numerical value is not needed in the later moment constants. Arctan is admissible: one may take `B = pi/2`, `P = 1`, `L = 1`, since `|2s|/(1+s^2)^2 <= 1`.

Throughout this review, `||u||_n = ||u||_2/sqrt(n)` for a neuron vector. A first-layer sample pair has the ordinary Euclidean norm on `R^2`; there is no extra sample average. The path norm is

    S(g) = sup_{0 <= t <= T} |g(t)|,
    E_T = C([0,T]; R^2),
    d_infty(g,k) = S(g-k).

The parameter metric for a velocity triple is

    ||(U1,U2,U3)||_g^2
      = (d/n)||U1||_F^2 + ||U2||_F^2 + (1/n)||U3||_2^2.

Indeed, direct differentiation of `L = sum_a r_a^2`, with `c_a = -2r_a`, gives

    grad_W1 L = -(1/n) sum_a c_a delta1_a x_a^T,
    grad_W2 L = -(1/n) sum_a c_a delta2_a h1_a^T,
    grad_W3 L = -(1/n) sum_a c_a h2_a.

Thus the three velocities are respectively `-(n/d) grad_W1 L`, `-grad_W2 L`, and `-n grad_W3 L`. This proves exactly

    dot L = -(d/n)||dot W1||_F^2
            - ||dot W2||_F^2 - (1/n)||dot W3||_2^2.

There is no missing factor of two or neuron normalization in (5). Also, `(1/n) sum_i E_i` is exactly the integrated first term of this dissipation identity.

The vector field is `C^1` in finite-dimensional parameters, hence locally Lipschitz. On any interval of existence,

    integral ||dot W||_g^2 dt <= L(0),
    ||W(t)-W(s)||_g <= sqrt((t-s)L(0)).

If a maximal existence time were finite, all parameters would remain in a bounded ball for this positive definite metric. At fixed `n,d` that ball is a compact finite-dimensional set. The displayed increment bound gives an endpoint limit; the locally Lipschitz equation extends from that limit. This excludes a finite maximal time. The argument requires no width-uniform equivalence between this metric and an unweighted parameter norm. It proves the finite-flow assertion for every finite initial state.

## 2. Explicit constants and the actual reverse-query derivative

The bounds in source lines 81–141 are valid with the constants exactly as printed. Here is a verification retaining every factor.

Initially `|f_a| <= B2 b`, so `||r(0)||_2 <= R0 = sqrt(2)(B2 b+1)`. Dissipation implies, for all times,

    ||r||_2 <= R0,
    sum_a |c_a| <= 2sqrt(2)R0 = Kc.

The readout equation gives, coordinatewise,

    |dot W3_i| <= B2 Kc,
    max_i |W3_i(t)| <= b+B2 Kc t <= M,
    M = b+B2 Kc T.

For the second-layer update, each summand has spectral norm bounded by

    |c_a| ||delta2_a||_2 ||h1_a||_2/n.

Consequently

    ||dot W2(t)||_op <= B1 P2 Kc (b+B2 Kc t),
    ||W2(t)||_op <= A,
    A = a+B1 P2 (b Kc T+B2 Kc^2 T^2/2).

In particular, with `Q = A P2 M`,

    ||delta2_a||_n <= P2 M,
    ||q1_a||_n <= Q.

The exact first-layer equation is

    dot z1_a = sum_b C_ab c_b delta1_b.

Since `|C_ab| <= 1` and `||delta1_b||_n <= P1 Q`, this yields

    ||dot z1_a||_n <= Kc P1 Q,
    ||dot h1_a||_n <= Kc P1^2 Q.

In particular, (6) needs no additional factor of two: `Kc` already bounds the sum over the two samples.

Use the source's definitions

    D_A = Kc P2 M B1,
    D_w = Kc B2,
    D_Z = D_A B1+A Kc P1^2 Q,
    D_delta = D_w P2+M L2 D_Z,
    Q1 = D_A P2 M+A D_delta.

First, `||dot W2||_op <= D_A` and `max_i |dot W3_i| <= D_w`. Differentiating the second preactivation gives

    dot z2_a = dot W2 h1_a+W2 dot h1_a,
    ||dot z2_a||_n <= D_A B1+A Kc P1^2 Q = D_Z.

Next, using coordinatewise products,

    dot delta2_a
      = dot W3 phi2'(z2_a)+W3 phi2''(z2_a) dot z2_a.

The two coordinate maxima just proved give

    ||dot delta2_a||_n <= D_w P2+M L2 D_Z = D_delta.

Finally, differentiating the actual, time-dependent transpose query gives

    dot q1_a = (dot W2)^T delta2_a+W2^T dot delta2_a,
    ||dot q1_a||_n <= D_A P2 M+A D_delta = Q1.

This step is valid. In particular, multiplication by `W3` is controlled by its coordinate maximum, while each matrix action uses a spectral norm. No coordinate maximum of `q1`, no fourth moment of `q1`, and no product estimate for two merely RMS-controlled fields is used.

Differentiating the output gives precisely `dot r_a = sum_b K_ab c_b`, equivalently `dot r = -2Kr`, with kernel entries

    K_ab = C_ab (delta1_a)^T delta1_b/n
         + [(delta2_a)^T delta2_b/n][(h1_a)^T h1_b/n]
         + (h2_a)^T h2_b/n.

Each entry satisfies

    |K_ab| <= K_star,
    K_star = P1^2 Q^2+P2^2 M^2 B1^2+B2^2.

The Frobenius bound gives `||K||_op <= 2K_star`. Hence

    ||dot r||_2 <= 4K_star R0,
    sum_a |dot c_a| <= 2sqrt(2)||dot r||_2
                     <= 8sqrt(2)K_star R0 = Kc_prime.

Thus (7) also has the correct constants. All constants in this section depend only on `T,a,b` and the activation bounds, with the label magnitude already fixed to one.

## 3. Envelope, signed work identity, and singular Gram matrices

Put `v_{a,i}=c_a q1_{a,i}` and use the source's envelope

    U_i = sum_a |v_{a,i}(0)|
          + integral_0^T sum_a |dot v_{a,i}(t)| dt.

It bounds `sum_a |v_{a,i}(t)|` at every time. Applying the triangle inequality in the normalized neuron Euclidean norm, including its integral version, gives

    ||U||_n
      <= sum_a |c_a(0)| ||q1_a(0)||_n
         + integral_0^T sum_a
             (|dot c_a| ||q1_a||_n+|c_a| ||dot q1_a||_n) dt
      <= Kc Q+T(Kc_prime Q+Kc Q1) = V_T.

This verifies (8). Differentiability follows from the finite flow and the activation assumptions. There is no independence assumption in this estimate.

For one row, let `X` have columns `x1,x2` and let `d_i` be the vector with entries `v_{a,i} phi1'(z1_{a,i})`. Then

    C = X^T X/d,
    dot w_i^T = X d_i/d,
    dot z_i = C d_i.

It follows that

    d ||dot w_i||_2^2 = d_i^T C d_i
      = sum_a v_{a,i} phi1'(z1_{a,i}) dot z1_{a,i}
      = sum_a v_{a,i} dot h1_{a,i}.

This proves the signed, pointwise work identity (9). Individual summands need not be nonnegative, but their sum is nonnegative because `C` is positive semidefinite. No absolute value can be substituted for `v` inside this identity; the candidate keeps its sign correctly.

Integration by parts gives

    E_i = [sum_a v_{a,i} h1_{a,i}]_0^T
          - integral_0^T sum_a dot v_{a,i} h1_{a,i} dt.

Thus

    0 <= E_i
      <= B1 (sum_a |v_{a,i}(T)|+sum_a |v_{a,i}(0)|
             + integral_0^T sum_a |dot v_{a,i}| dt)
      <= 2 B1 U_i.

This verifies the crucial linear estimate (10), with no loss of a factor.

The Gram matrix has entries `[[1,rho],[rho,1]]` and eigenvalues `1+rho,1-rho` in `[0,2]`. Therefore `C^2 <= 2C` as quadratic forms, giving

    |dot z_i|^2 = d_i^T C^2 d_i <= 2d_i^T C d_i,
    |dot z_i| <= ||C||_op |d_i| <= 2P1 U_i.

These are exactly (11). At `rho=1`, `d_i^T C d_i=(d_{1,i}+d_{2,i})^2`; at `rho=-1`, it is `(d_{1,i}-d_{2,i})^2`. At either endpoint `|C d_i|^2=2d_i^T C d_i`. Thus the same bounds hold even if this action vanishes through cancellation. No inverse, pseudoinverse, or lower eigenvalue bound is present. The corresponding constraints `z2=z1` or `z2=-z1` are also consistent with the actual first-layer equation; no symmetry of the activation or agreement between labels is required.

## 4. Fourth path moments and cubic velocities

Integrating the first inequality in (11) and then (10) gives

    integral_0^T |dot z_i|^2 dt <= 2E_i <= 4B1 U_i.

Multiplying this by the pointwise bound `sup_t |dot z_i| <= 2P1 U_i` yields

    integral_0^T |dot z_i|^3 dt <= 8B1 P1 U_i^2.

Averaging and using `(1/n) sum_i U_i^2 <= V_T^2` proves (3). The joint two-sample chain rule has Euclidean operator bound `P1`, so

    |dot h_i| <= P1 |dot z_i|,
    (1/n) sum_i integral_0^T |dot h_i|^3 dt
      <= 8B1 P1^4 V_T^2.

The power `P1^4` in (4) is correct.

For the path bound,

    sup_t |z_i(t)| <= |z_i(0)|+sqrt(2T E_i).

Using `(a+b)^4 <= 8(a^4+b^4)` gives

    sup_t |z_i(t)|^4
      <= 8|z_i(0)|^4+32T^2 E_i^2
      <= 8|z_i(0)|^4+128B1^2 T^2 U_i^2.

This proves exactly (2). The factor 128 includes both the two-sample Gram bound and the fourth-power sum inequality.

The additional sentence in source line 205 is also correct. If `s_i=sqrt(d)||dot w_i||`, then `sup_t s_i <= sqrt(2)P1 U_i` and `integral s_i^2=E_i`. Consequently

    (1/n) sum_i integral_0^T s_i^3 dt
      <= 2sqrt(2) B1 P1 V_T^2.

These arguments use no division by `B1`, `P1`, `U_i`, or an eigenvalue of `C`; zero bounds and zero-action cases cause no exception. At `T=0` the integral claims are immediate.

## 5. Gaussian calculation and probability quantifiers

This part applies to exactly the independent initialization specified in source lines 209–210, including `Var(W3_i)=n^(-2)`. It does not assert the same readout-maximum event for a different readout scaling.

For any deterministic normalized input pair, the initial pairs are independent across rows, with law `N(0,C)`. Write one pair as

    Z1=G, Z2=rho G+sqrt(1-rho^2) H,

with independent standard Gaussians. This formula remains valid at both singular angles. It gives `E[Z1^2 Z2^2]=1+2rho^2`, and hence

    E|Z|^4 = 3+3+2(1+2rho^2) = 8+4rho^2 <= 12.

Also `(Z1^2+Z2^2)^4 <= 8(Z1^8+Z2^8)` and a standard Gaussian has eighth moment 105 (successive integration by parts gives the even-moment recurrence). Therefore

    E|Z|^8 <= 1680.

For the empirical fourth moment `F_n`, row independence gives

    Var(F_n) <= 1680/n,
    P(F_n>13) <= 1680/n,

because `13-E|Z|^4 >= 1`. This verifies both the constant and the uniformity. If the deterministic input pair varies with `n`, the precise convergence statement is `F_n-(8+4rho_n^2) -> 0` in probability; no convergence of `rho_n` is needed for the event bound.

For `W2(0)`, take a deterministic maximal `1/4`-separated subset of the unit sphere. It is a `1/4`-net. Disjoint open balls of radius `1/8` centered at its points fit inside the ball of radius `9/8`, giving cardinality at most `9^n`. Approximating both unit vectors in a bilinear form gives

    ||W2(0)||_op <= 2 max_{u,v in the net} |u^T W2(0) v|.

For fixed net points, this scalar is centered Gaussian with variance `1/n`. Completing the square in its exponential moment and applying Markov's inequality gives the two-sided tail `2 exp(-n t^2/2)`. At `t=4`, the union bound therefore gives

    P(||W2(0)||_op>8)
      <= 2 (9^n)^2 exp(-8n)
      = 2 exp(-(8-2log 9)n).

Here `8-2log 9>0`. For the readout,

    P(max_i |W3_i(0)|>1) <= 2n exp(-n^2/2).

These constants are all correct. Independence between the three good events is unnecessary.

Precisely, define

    E_n(x1,x2) = {F_n<=13, ||W2(0)||_op<=8,
                 max_i |W3_i(0)|<=1},
    epsilon_n = 1680/n+2 exp(-(8-2log 9)n)+2n exp(-n^2/2).

For every `n,d` and every deterministic pair with `||x_a||^2=d`,

    P(E_n(x1,x2)^c) <= epsilon_n -> 0.

The bound is uniform over those choices. On this same event, use `a=8,b=1`; all finite horizons and all allowed label patterns satisfy the deterministic estimates, with constants depending on the horizon and activation bounds alone. In particular, the event does not need to be reselected for each `T`.

This is a uniform bound on the failure probability for each fixed input choice. It is not a probability bound for the union of failures over every possible input pair in one initialization. It does not cover input choices selected using the initialization. It also does not give an almost-sure eventual assertion across widths from the displayed failure bound alone. The candidate states these limitations correctly. On-event moment bounds should likewise not be silently replaced by unconditional expectation bounds over all initializations.

## 6. Uniform integrability and first-path W2 compactness

Fix `T` and common initial bounds `a,b` and

    (1/n) sum_i |z_i(0)|^4 <= F.

Define scalar constants, distinct from the Gram matrix,

    M4_T = 8F+128B1^2 T^2 V_T^2,
    J3_T = 8B1 P1 V_T^2.

For the empirical pair-path law `mu_n=(1/n) sum_i delta_{z_i(.)}` on `E_T`, the verified estimates imply

    integral S(g)^4 dmu_n(g) <= M4_T,
    (1/n) sum_i integral_0^T |dot z_i|^3 dt <= J3_T.

The exact quadratic-Wasserstein metric meant here is

    W2(mu,nu)^2 = inf_{pi coupling mu,nu}
                    integral d_infty(g,k)^2 dpi(g,k).

Its second moment is measured about the zero path. All empirical measures in question belong to this space, since their fourth path moments are finite.

For every `R>0`, pointwise truncation gives

    integral S(g)^2 1_{S(g)>R} dmu_n(g) <= M4_T/R^2,
    (1/n) sum_i integral_0^T
      |dot z_i|^2 1_{|dot z_i|>R} dt <= J3_T/R.

These establish the two claimed uniform-integrability statements. The velocity statement uses the measure `(1/n) sum_i delta_i` times Lebesgue measure on `[0,T]`, of total mass `T`; it is not a claim about a supremum of velocity over time. The bounds are uniform over the deterministic family or over the realizations restricted to the stated good events.

For activation pairs, `sup_t |h_i(t)| <= sqrt(2)B1`, so their fourth path moments are at most `4B1^4`, and their squared path norms have zero tails past `sqrt(2)B1`. Their velocity tail bound is

    (1/n) sum_i integral_0^T
      |dot h_i|^2 1_{|dot h_i|>R} dt
      <= 8B1 P1^4 V_T^2/R.

For tightness, let `H_i` be the Holder `2/3` seminorm of `z_i`. Holder's integral inequality gives

    |z_i(t)-z_i(s)|
      <= |t-s|^(2/3) (integral_0^T |dot z_i|^3 dt)^(1/3),
    (1/n) sum_i H_i^3 <= J3_T.

For positive `R,H`, set

    K_{R,H} = {g in E_T: |g(0)|<=R, [g]_{2/3}<=H}.

Then

    mu_n(K_{R,H}^c) <= F/R^4+J3_T/H^3.

This proves uniform tightness. Indeed, on `K_{R,H}` the supremum norm is at most `R+H T^(2/3)`, and the time modulus is common. Extraction on a nested sequence of finite grids, followed by that modulus bound, gives a uniformly convergent subsequence of any sequence in the set. The defining inequalities are preserved by uniform limits, so this set itself is compact. At `T=0`, compactness is simply boundedness of the initial values in `R^2`.

For completeness, the following verifies the probability-measure compactness step without importing a heavy theorem. Given any small `eta>0`, the fourth-moment bound and tightness allow a compact set `K` such that

    sup_n integral_{K^c} S(g)^2 dmu_n(g) <= eta^2.

To see this, first choose `B` with `M4_T/B^2 <= eta^2/2`, and then choose a compact `K` with `sup_n mu_n(K^c) <= eta^2/(2B^2)`. Split the displayed integral into `S>B` and `S<=B`.

Cover `K` by finitely many balls of radius `eta` in the uniform norm. Map paths in `K` to a chosen covering center and all paths outside `K` to the zero path. This gives a finite-support approximation to every `mu_n` with transport cost at most `2eta^2`. The set of laws on these finitely many centers and the zero path is compact in W2: convergence of its finitely many weights gives a coupling whose cost is bounded by the squared diameter times half the sum of the absolute weight differences. Consequently the original family is totally bounded in W2.

There is also an elementary limit argument for the present empirical measures. From any W2-Cauchy subsequence choose a further subsequence of finite-support laws with consecutive W2 distances at most `2^(-j)`. Optimal couplings exist here by compactness of finite arrays of coupling weights. Realize these consecutive couplings as a Markov chain `G_j` of paths with finitely supported marginals, by their conditional transition probabilities. Then

    sum_j (E d_infty(G_j,G_{j+1})^2)^(1/2) < infinity.

The sum of the distances is finite almost surely, because its expectation is finite. Completeness of `E_T` gives a limiting continuous path `G`. The triangle inequality in L2 and Fatou's inequality give

    (E d_infty(G_j,G)^2)^(1/2)
      <= sum_{k>=j} (E d_infty(G_k,G_{k+1})^2)^(1/2) -> 0.

The law of `G` has finite second moment by comparison with `G_1`, and these couplings prove W2 convergence. This proves relative compactness of the empirical path-law family. It also validates the candidate's use of weak subsequential compactness together with uniform second-moment tails in this setting; tightness alone would not have supplied the W2 conclusion.

Activation paths and joint `(z,h)` paths cause no additional gap. The map `g -> phi1(g)` is `P1`-Lipschitz in the uniform metric. With Euclidean norm on `R^4`, the map `g -> (g,phi1(g))` is `sqrt(1+P1^2)`-Lipschitz. Pushing forward couplings proves the corresponding W2 bounds, so both kinds of first-layer path laws inherit relative compactness. This is a statement about the two sample evaluations of the first layer, not a compactness claim for the ambient first-layer weight rows when `d` varies.

In the Gaussian setting take `F=13,a=8,b=1`, so `M4_T=104+128B1^2 T^2 V_T^2`. The closure of the resulting deterministic family of empirical path laws is a fixed W2-compact set, say `mathcal K_T`, independent of `n,d`, angle, and label pattern. Thus the precise consequence is

    P(mu_n not in mathcal K_T) <= epsilon_n -> 0

for each deterministic normalized input pair, uniformly over those pairs and dimensions. The same initialization event works for every finite horizon, with a possibly different compact set for each horizon. This proves exactly the high-probability compact containment stated in the candidate.

## Scope of certification

The finite-flow estimate, signed work mechanism, moment gain, Gaussian event bound, first-layer uniform integrability, and first-path W2 compactness are certified as stated. The candidate appropriately stops at compactness: it establishes no identification of a population evolution, population uniqueness, restartability, general-angle comparison of distinct flows, raw GD/GF comparison, whole-space Lp action of the second-layer matrix or its transpose, or positive-time Gaussian reverse-field tails. No such additional claim is included in this PASS verdict.
