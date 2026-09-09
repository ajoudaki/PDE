# Fixed-depth check of the bounded-activation response method

This is an independent extension calculation, not a claim that the existing
three-input/two-hidden-layer file already proves a depth-uniform theorem.
The depth is fixed. Constants below can deteriorate with depth.

## Scope and conclusion

Fix a finite number of inputs and a finite number `L` of hidden layers.
Allow any normalized input Gram matrix, including a singular one. Assume
each hidden activation and its first two derivatives are bounded, with the
activation twice continuously differentiable. Assume zero readout, or an
independent initial readout with a fixed deterministic essential bound.
Middle initial matrices are independent Gaussian matrices with variance
`sigma_l^2/n`; first-layer roots are Gaussian with their actual input Gram
covariance. All learning-rate constants are fixed and positive.

Under these assumptions the response bootstrap below closes on a positive
time interval depending on depth, the activation bounds, the initial
readout bound, the initialization variances, labels, and the number of
inputs. No inverse input Gram matrix is used. The necessary new estimate is
an *entrywise* `O(Delta)` bound on forward-response coefficients. The
two-hidden-layer appendix's row-sum bound by itself does not suffice.

Combined with the same finite-program Gaussian oracle, common operator
realization, and reference-tail comparison used in the existing local
proof, this supplies its missing fixed-depth tail lemma. In particular the
comparison retains an arbitrary vanishing step size, not a condition
`Delta sqrt(n) -> 0`. This note checks that extension mechanism; it does not
establish literature novelty or an all-finite-time result.

## Notation and preliminary bounds

Write `H_l=phi_l(Z_l)`, `Z_l=B_l H_{l-1}` for `2<=l<=L`, and let `C` be
the readout. Put

    P_L=C,   P_j=B_{j+1}^* delta_{j+1},
    delta_j=phi_j'(Z_j) P_j.

Products here are coordinatewise except the displayed operator actions.
The first-layer Euler update contains the fixed input Gram matrix. Middle
updates are `-2 kappa_l Delta sum_a r_a delta_l,a tensor H_l-1,a`; the
readout update is `-2 kappa_out Delta sum_a r_a H_L,a`.

There are width- and mesh-independent RMS/operator bounds on `0<=t<=1`
(or any fixed finite horizon), on the usual bounded-initial-operator event.
Indeed bounded final activations give a discrete Gronwall bound on
`||C||_infty` and residuals. Then `delta_L` is bounded, which bounds `B_L`;
this bounds the RMS of `delta_L-1`, which bounds `B_L-1`, and so on downwards.
This induction is triangular in depth. Bounded activations bound every
outer-product source on its activation side. In particular all Gaussian
backward hats below have variances at most one common constant `K^2`.
Enlarge `K` to absorb the fixed number of inputs and all fixed parameters.

## Exact causal response equations

For each matrix `B_l,0`, introduce its forward Gaussian hats `xi^l_a,k`
and backward Gaussian hats `eta^l_a,k`, with covariances respectively
`sigma_l^2 E[H_l-1,a,k H_l-1,b,s]` and
`sigma_l^2 E[delta_l,a,k delta_l,b,s]`. At an intermediate layer, its
coordinate functions use the adjacent families `xi^j` and `eta^{j+1}`.
Different matrix/orientation Gaussian families can be represented
independently. This does not assert a natural pairing of neurons in
different layers. At the top include the independent readout root.

All derivatives below freeze the deterministic coefficients, contractions,
residuals, and covariance laws, as in the finite-program response rule.
Define

    A_l(ak;bs) = sigma_l^2 E[partial delta_l,a,k / partial xi^l_b,s], s<=k,
    C_l(ak;bs) = sigma_l^2 E[partial H_l-1,a,k / partial eta^l_b,s], s<k.

The exact local recursions are

    Z_l,a,k = xi^l_a,k + sum_(b,s<k) F_l(ak;bs) delta_l,b,s,
    P_l-1,a,k = eta^l_a,k + sum_(b,s<=k) R_l(ak;bs) H_l-1,b,s,

where

    F_l = C_l - 2 kappa_l Delta r_b,s E[H_l-1,b,s H_l-1,a,k],
    R_l = A_l - 1_(s<k) 2 kappa_l Delta r_b,s E[delta_l,b,s delta_l,a,k].

These are the layerwise application of Tensor Programs III, Box 1,
Remarks 2.11--2.12, Theorem 2.10, https://arxiv.org/pdf/2009.10685.
For a fixed mesh/program length the coordinate expressions and their
first symbolic derivatives are polynomially bounded: activations and
their first two derivatives are bounded, and only finitely many products
and sums occur. Singular covariance is treated by symbolic slots; null
covariance directions give zero-norm combinations of source variables.

## Bootstrap quantities

For all times through the current step, bootstrap

    sum_(b,s<=k) |A_l(ak;bs)| <= a_l,
    |C_l(ak;bs)| <= c_l Delta,  s<k.

Then, with `f_l=c_l+K`,

    |F_l(ak;bs)| <= f_l Delta,
    sum_(b,s<=k)|R_l(ak;bs)| <= a_l+KT,
    |P_l-1,a,k - eta^l_a,k| <= K(a_l+T).

For any centered Gaussian variables `g_i` of variance at most `K^2`,
regardless of temporal dependence, Jensen gives

    E exp(q Delta sum_(u<k,a) |g_a,u|)
      <= 2 exp(K q^2 T^2),          k Delta<=T.

Here and below the same letter `K` may be increased a finite number of
times. Neither `K` nor the chosen bootstrap constants depends on mesh size.

## Forward-slot derivatives: bounds on a_l

For `2<=j<L`, let `V_j,k` be the maximum over inputs and times through `k`
of the sum of absolute derivatives of `Z_j` with respect to all its own
forward slots `xi^j`. The opposite family `eta^{j+1}` is held fixed.
The derivative of `P_j,a,u` has absolute row sum at most
`K(a_j+1+T)V_j,u`; hence that of `delta_j,a,u` is at most

    K(|eta^{j+1}_a,u|+a_j+1+1)V_j,u.

In this display `a_j+1` denotes the indexed constant `a_{j+1}`.
With `G_u=sum_a |eta^{j+1}_a,u|`, the entrywise bound on `F_j` implies

    V_j,k <= 1 + K f_j Delta sum_(u<k) (G_u+1+a_{j+1}) V_j,u.

The prefix maximum satisfies the same inequality because its right side
is increasing with the terminal time. Discrete Gronwall therefore gives

    V_j,k <= exp(K f_j [T(1+a_{j+1}) + Delta sum_(u<k) G_u]).

Jensen and Cauchy--Schwarz, including possible correlation with `G_k`, give
the following uniform bound on the response row sum:

    a_j <= K(1+a_{j+1})
       * exp(K f_j T(1+a_{j+1}) + K f_j^2 T^2).                 (A)

At the top, the readout derivative row sum is at most `KT V_L,k`.
Its initial bounded root is independent of the forward hats, and is held
fixed when differentiating. If its essential bound is `B_0`, the same
argument is deterministic and gives

    a_L <= K(B_0+1) exp(K f_L T(B_0+1)).                       (AT)

These displayed inequalities mean that their right sides bound the actual
quantities under the stipulated bootstrap caps on the other quantities.

## Single backward-slot derivatives: bounds on c_l

Fix one slot `eta^l_b,s`. Its direct derivative in `P_l-1,a,u` is precisely
`1_(a=b,u=s)`. The first time it can influence the next first-layer state
or a later forward-memory source is one Euler update later.

For `l=2`, differentiating the first-layer Euler equation and taking the
prefix maximum `D_k` of the absolute coordinate derivatives gives

    D_k <= K Delta
      * exp(K[T(1+a_2) + Delta sum_(u<k,a)|eta^2_a,u|]), k>s.

It is zero for `k<=s`. Here the Gram matrix is used only through bounded
entries. Thus

    c_2 <= K exp(KT(1+a_2)+KT^2).                             (C2)

For `l>=3`, put `j=l-1`. The derivative of `delta_j,a,u` is at most

    K 1_(a=b,u=s)
      + K(|eta^l_a,u|+1+a_l) max_(v<=u,c)|partial Z_j,c,v|.

Consequently the entrywise `F_j` estimate and discrete Gronwall give

    D_k <= K f_j Delta
      * exp(K f_j[T(1+a_l)+Delta sum_(u<k,a)|eta^l_a,u|]), k>s.

Applying the bounded activation derivative and taking expectation yields

    c_l <= K(c_{l-1}+K)
       * exp(K(c_{l-1}+K)T(1+a_l)+K(c_{l-1}+K)^2T^2).         (C)

The crucial factor `Delta` comes from the single source pulse, not from
an assumption on Gaussian maxima.

## Closing all constants without a circular choice

Choose upper caps `c_2,c_3,...,c_L` successively, each at least four times
the `T=0` right side of (C2) or (C), using the previously chosen lower-layer
cap. Next choose `a_L,a_L-1,...,a_2` successively, each at least four times
the `T=0` right side of (AT) or (A), using the already chosen higher-layer
cap. All these choices are finite because depth is fixed. Finally choose
`T_0>0` so every exponential factor in these finitely many inequalities is
at most two for `T<=T_0`. All bounds then improve their bootstrap caps by
a factor of at least two.

This can be made a literal induction over the time step: construct current
forward states and their `C_l` coefficients bottom-up, using backward
coefficients only from earlier times. Then construct current backward
states and `A_l` coefficients top-down. The bounds for `C_l` may use the
current lower-layer `C_l-1`, already constructed, and those for `A_l` may
use the current upper-layer `A_l+1`, also already constructed. No estimate
requires a not-yet-constructed current coefficient of its own kind/layer.

Hence every backward field is a Gaussian of bounded variance plus a
uniformly bounded response remainder. There exist `c,C>0` such that

    sup_mesh sup_(k Delta<=T_0) max_(j<L,a) E exp(c|P_j,a,k|^2) <= C.

## Why this is enough for the existing local comparison

Forward differences are bounded by `K` times the state distance (first
coordinates in RMS, matrices in operator norm, readout in RMS). In the
backward comparison the only problematic product is

    [phi_j'(Z_j)-phi_j'(Z_j,ref)] P_j,ref.

Truncating the reference field at level `R` bounds it by
`KR ||Z_j-Z_j,ref||_2` plus its Gaussian RMS tail. Recursing through the
layers adds these terms; it does not multiply them by a new factor `R`
at each layer, since the multiplier on the backward-field difference is
the bounded `phi_j'`. Thus the vector-field comparison is of the form

    ||F(state)-F(reference)||
       <= K(1+R) distance + K exp(-c R^2).

All fine-mesh state velocities are bounded uniformly in dimension by the
preliminary operator/RMS estimates. The original fixed-oracle-mesh,
fine-actual-step, and Gaussian-tail order of limits therefore applies with
depth-dependent constants, retaining `eta_n -> 0`. One must still state
the original convergence topology and allowable probe hypotheses; this
tail calculation does not upgrade them to convergence of arbitrary
unbounded test functions or all higher path moments.

## Scope exclusions

For unbounded hidden activations the bounded response remainder above is
lost. Merely replacing it with a row-sum estimate does not restore this
proof. A simultaneous sub-Gaussian-field/response bootstrap could be a
separate route for smooth globally Lipschitz activations, but is not proved
by the bounded-activation argument here. In particular this note does not
certify arbitrary-depth GELU.

ReLU also lacks the bounded continuous second derivative used in the
sensitivity and reference-product comparisons. Its kink requires a
separate argument, such as appropriate weak-derivative and margin/tail
control. This is a proof limitation, not evidence that a ReLU population
limit fails. No arbitrary-growth activation class can be asserted without
initial moment restrictions; for example `exp(z^4)` need not even have a
finite Gaussian second moment.

The existing orthogonal-input, two-hidden-layer scalar-flow transform is
a distinct result which can allow unbounded first activation, including
GELU under its derivative assumptions. It should not be silently promoted
to this arbitrary-geometry/fixed-depth theorem.
