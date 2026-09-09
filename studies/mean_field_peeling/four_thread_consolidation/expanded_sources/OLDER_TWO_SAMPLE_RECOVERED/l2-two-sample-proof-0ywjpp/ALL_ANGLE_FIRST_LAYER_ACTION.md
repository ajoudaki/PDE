# All-angle first-layer action and uniform integrability at L=2

Root draft, 2026-09-06. UNREVIEWED. This is an unconditional estimate
for actual finite-width gradient flow, with constants independent of
width and input angle. It is not a construction or uniqueness theorem
for a population limit. No experiments or external results are used.

The two scalar activations may differ. Assume phi_ell is C2 and

    |phi_ell|<=B_ell, |phi_ell'|<=P_ell, |phi_ell''|<=L_ell,
    ell=1,2,

with finite nonnegative constants. Arctan is an admissible nonlinear
choice. The result uses bounded activations, not any clipping of states
or gradients. Throughout, vector norms without a subscript are ordinary
Euclidean norms, matrix operator norms are spectral norms, and all
neuron averages are written with their explicit 1/n factor.

## 1. Model and statement

Fix x_1,x_2 in R^d with ||x_a||^2=d. Write C_ab=x_a^T x_b/d, so C
is positive semidefinite and ||C||_op<=2, including rho=+/-1. The
labels have absolute value one. There are two hidden layers of width n:

    z^(1)_a=W^(1)x_a, h^(1)_a=phi_1(z^(1)_a),
    z^(2)_a=W^(2)h^(1)_a, h^(2)_a=phi_2(z^(2)_a),
    f_a=(W^(3))^T h^(2)_a/n, r_a=f_a-y_a,
    delta^(2)_a=W^(3) phi_2'(z^(2)_a),
    q^(1)_a=(W^(2))^T delta^(2)_a,
    delta^(1)_a=phi_1'(z^(1)_a) q^(1)_a.

The rescaled readout is W^(3). Vector products in the delta definitions
are coordinatewise; the transpose query is ordinary matrix action.
The physical loss is L=r_1^2+r_2^2 and the flow is

    dot W^(1)=(1/d)sum_a c_a delta^(1)_a x_a^T,
    dot W^(2)=(1/n)sum_a c_a delta^(2)_a(h^(1)_a)^T,
    dot W^(3)=sum_a c_a h^(2)_a, c_a=-2r_a.            (1)

Assume ||W^(2)(0)||_op<=a and max_i |W^(3)_i(0)|<=b, where a,b
are fixed constants. No coordinate maximum of W^(1)(0) is assumed.
For every finite T there is a finite deterministic V_T depending
only on T,a,b and the activation bounds, such that the following
conclusions hold. It is independent of n,d,C and the label pattern.

For each neuron i put z_i=(z^(1)_{1,i},z^(1)_{2,i}), and similarly h_i.
Then

    (1/n)sum_i sup_(t<=T)|z_i(t)|^4
      <=(8/n)sum_i |z_i(0)|^4+128 B_1^2 T^2 V_T^2,             (2)
    (1/n)sum_i integral_0^T |dot z_i(t)|^3 dt
      <=8 B_1 P_1 V_T^2,                                    (3)
    (1/n)sum_i integral_0^T |dot h_i(t)|^3 dt
      <=8 B_1 P_1^4 V_T^2.                                  (4)

In particular these estimates hold for actual Gaussian initialization,
uniformly on events whose probabilities tend to one, and for every
input angle. They control joint same-neuron two-sample FIRST-layer
paths and velocities. No analogous Lp operator bound is asserted for
W^(2) or its transpose.

## 2. Global finite flow and bounded first reverse derivative

In finite dimensions the right side of (1) is continuously
differentiable, hence locally Lipschitz. Local existence and uniqueness
follow by contraction of the integral equation on a small closed ball.
Direct differentiation of the loss with the stated factors gives

    dot L=-d||dot W^(1)||_F^2/n-||dot W^(2)||_F^2
          -||dot W^(3)||^2/n.                                (5)

The metric on the right is a fixed positive Euclidean metric at each
finite n,d. On a finite interval its integrated squared speed is at
most L(0). Cauchy--Schwarz bounds displacement in that metric by
sqrt(T L(0)). Thus no finite-dimensional state can escape to infinity
at a finite time. The vector field is bounded on the resulting compact
ball, so the solution has an endpoint limit and the local contraction
extends it. This proves global finite flow, without assuming any
population existence or discrete loss decrease.

Here are explicit width-independent bounds. Define

    R_0=sqrt(2)(B_2 b+1), K_c=2sqrt(2) R_0,
    M=b+B_2 K_c T,
    A=a+B_1 P_2 (b K_c T+B_2 K_c^2 T^2/2).

Since L decreases, ||r(t)||<=R_0 and sum_a |c_a(t)|<=K_c.
Integrating the readout equation gives max_i|W^(3)_i(t)|<=M.
For a rank-one update the spectral and Frobenius norms both equal
the product of the Euclidean norms of its factors divided by n.
Integrating the resulting bound on dot W^(2), using the earlier
readout bound b+B_2 K_c t, proves ||W^(2)(t)||_op<=A.

Consequently, for each sample and t<=T,

    ||delta^(2)_a||/sqrt(n)<=P_2 M,
    ||q^(1)_a||/sqrt(n)<=Q:=A P_2 M,
    ||dot z^(1)_a||/sqrt(n)<=K_c P_1 Q.                       (6)

Set

    D_A=K_c P_2 M B_1, D_w=K_c B_2,
    D_Z=D_A B_1+A K_c P_1^2 Q,
    D_delta=D_w P_2+M L_2 D_Z,
    Q_1=D_A P_2 M+A D_delta.

The rank-one update gives ||dot W^(2)||_op<=D_A. The product rule
dot z^(2)_a=dot W^(2)h^(1)_a+W^(2)dot h^(1)_a, with
dot h^(1)_a=phi_1'(z^(1)_a)dot z^(1)_a, gives
||dot z^(2)_a||/sqrt(n)<=D_Z. Because W^(3) is bounded
COORDINATEWISE, differentiation of delta^(2) gives

    ||dot delta^(2)_a||/sqrt(n)
      <=D_w P_2+M L_2 D_Z=D_delta.

Finally differentiate the ACTUAL transpose query:

    dot q^(1)_a=(dot W^(2))^T delta^(2)_a
                   +(W^(2))^T dot delta^(2)_a.

This proves ||dot q^(1)_a||/sqrt(n)<=Q_1. In particular it involves
no product of an uncontrolled hidden reverse field with a hidden
velocity. The depth-two location of this query is important.

The residual derivative is also bounded. Its exact kernel equation is
dot r=-2Kr with

    K_ab=C_ab (delta^(1)_a)^T delta^(1)_b/n
       +[(delta^(2)_a)^T delta^(2)_b/n][(h^(1)_a)^T h^(1)_b/n]
       +(h^(2)_a)^T h^(2)_b/n.

Every entry has absolute value at most

    K_*=P_1^2 Q^2+P_2^2 M^2 B_1^2+B_2^2.

The operator norm of a two-by-two matrix with this entry bound is
at most 2K_*. Therefore ||dot r||<=4K_*R_0 and

    sum_a |dot c_a|<=K'_c:=8sqrt(2)K_*R_0.                    (7)

All these bounds hold on the whole finite interval of the actual flow.

## 3. Pointwise work identity and the moment gain

For each first-population neuron define its signed controlled reverse
pair v_{a,i}(t)=c_a(t)q^(1)_{a,i}(t), and the nonnegative number

    U_i=sum_a |v_{a,i}(0)|
             +integral_0^T sum_a |dot v_{a,i}(t)|dt.

This is a convenient scalar envelope, not a replacement for a network
state or a modified gradient. It obeys sum_a|v_{a,i}(t)|<=U_i.
Minkowski's integral inequality, (6)--(7), and the bound on dot q give

    [(1/n)sum_i U_i^2]^(1/2)
       <=K_c Q+T(K'_c Q+K_c Q_1)=:V_T.                       (8)

One can verify Minkowski here directly by duality with Euclidean unit
vectors and Cauchy--Schwarz; no independent-coordinate assumption is
involved. Both c and q are differentiable, so dot v=dot c q+c dot q.

Let w_i(t) be row i of W^(1). For this row set

    E_i=integral_0^T d||dot w_i(t)||^2 dt.

The exact first equations imply the pointwise identity

    d||dot w_i||^2
      =sum_(a,b) C_ab v_{a,i}phi_1'(z^(1)_{a,i})
                              v_{b,i}phi_1'(z^(1)_{b,i})
      =sum_a v_{a,i} dot h^(1)_{a,i}.                        (9)

The left side is nonnegative even for negative input correlation.
Integration by parts on the right side, and |h^(1)|<=B_1, give

    0<=E_i<=B_1 sum_a(|v_{a,i}(T)|+|v_{a,i}(0)|)
                   +B_1 integral_0^T sum_a |dot v_{a,i}|
           <=2B_1 U_i.                                      (10)

This LINEAR dependence on the envelope U_i, rather than a quadratic
one, is the moment gain. It uses actual time regularity of q, not a
sign restriction, alignment assumption, frozen history, or a bound on
q as a multiplication operator on L2.

Let d_i be the two-vector with entries v_{a,i}phi_1'(z^(1)_{a,i}).
Then dot z_i=C d_i and d||dot w_i||^2=d_i^T C d_i. Since the
eigenvalues of C are in [0,2],

    |dot z_i|^2<=2d||dot w_i||^2,
    |dot z_i|<=2P_1 U_i.                                    (11)

These statements do not use C inverse, and remain valid at both
singular angles. Thus integral |dot z_i|^2<=4B_1 U_i.
Multiplying by the second inequality in (11) proves
integral |dot z_i|^3<=8B_1P_1 U_i^2, and averaging proves (3).
The chain rule gives |dot h_i|<=P_1|dot z_i|, proving (4).

Also sup_t|z_i(t)|<=|z_i(0)|+sqrt(2T E_i).
The elementary inequality (a+b)^4<=8(a^4+b^4), followed by (10),
gives

    sup_t|z_i(t)|^4<=8|z_i(0)|^4+128 B_1^2 T^2 U_i^2.

This proves (2). The same reasoning gives a cubic space-time bound on
sqrt(d)||dot w_i||, but that extra assertion is not needed here.

## 4. Canonical initialization and exact consequences

Under the canonical independent initialization W^(1)_ij~N(0,1/d),
W^(2)_ij~N(0,1/n), W^(3)_i~N(0,n^-2), each initial first pair is
centered Gaussian of covariance C and different first rows are iid.
The Gaussian moment calculation is

    E|z_i(0)|^4=3+3+2(1+2rho^2)=8+4rho^2<=12.

Its empirical average converges in probability to this expectation.
More explicitly E|z_i(0)|^8<=8 E(G_1^8+G_2^8)=1680, so Chebyshev
bounds the probability that the empirical fourth moment exceeds 13
by 1680/n, uniformly over deterministic normalized input pairs. The
inputs here are fixed independently of the Gaussian initialization.
The initial Gaussian
matrix has spectral norm at most 8 with probability tending to one:
take a 1/4-net of the unit sphere with at most 9^n points (disjoint
radius-1/8 balls inside a radius-9/8 ball). Approximating both vectors
shows ||W^(2)_0||_op<=2 max_(u,v in net)|u^T W^(2)_0 v|.
Each scalar has variance 1/n, so the Gaussian exponential Markov bound
and a union bound give failure probability at most
2 exp(-(8-2log9)n). The readout maximum exceeds 1 with probability
at most 2n exp(-n^2/2), by the same scalar bound. Independence between
these events is not needed.

Take a=8,b=1 above. For each deterministic normalized input pair there
is an event E_n(x_1,x_2) on which the empirical initial fourth moment
is at most 13 and (2)--(4) have deterministic bounds depending only on
T and the activation bounds. Uniformly over dimension and such pairs,

    P(E_n(x_1,x_2)^c)<=1680/n+2exp(-(8-2log9)n)+2n exp(-n^2/2).

This is uniform probability over fixed input choices, NOT a single
event controlling every possible input pair in the same realization.
For each fixed pair its initialization event works for every finite T.

For deterministic families retain a common bound on the empirical
INITIAL fourth moment; the preceding Gaussian events supply it.
These bounds imply uniform integrability of the first-layer squared
path norm and of the first-layer squared velocities in space-time.
Explicitly, a fourth path bound C implies

    (1/n)sum_i sup_t|z_i(t)|^2 1_{sup_t|z_i(t)|>R}<=C/R^2,

and the cubic velocity bound implies

    (1/n)sum_i integral |dot z_i|^2 1_{|dot z_i|>R}<=C/R.

The same statements hold for the activation paths and velocities,
using bounded phi_1 and its bounded derivative. Moreover, Holder's
inequality gives for each neuron

    |z_i(t)-z_i(s)|<=|t-s|^(2/3)
                            (integral_0^T |dot z_i|^3)^(1/3).

Thus the empirical joint two-sample first-path laws give arbitrarily
large mass to sets with bounded initial values and bounded Holder
2/3 seminorm. Such sets have compact closure in the uniform path norm:
on each finer finite time grid extract convergent subsequences in a
bounded Euclidean box, then use the common modulus of continuity to
upgrade grid convergence to uniform convergence. A diagonal argument
over the grids proves this directly. The fourth path bound controls
the second-moment tails in that norm. Consequently these first-path
laws are relatively compact for quadratic Wasserstein convergence
(equivalently, weak subsequential compactness plus uniform second-
moment tails). In the Gaussian setting this means containment in a
fixed relatively compact family with probability tending to one, not
an almost-sure assertion across all widths. This is compactness, not
identification or uniqueness.

Nothing here controls a whole-space Lp action of W^(2) or (W^(2))^T,
gives positive-time Gaussian tails for q^(1), proves the raw GD/GF
comparison for general angles, or constructs a uniquely restartable
population flow. In particular the general-angle multiplier in a
comparison of two different flows has not been bounded. The new
conclusion is an actual, unconditional finite-GF moment estimate for
first hidden paths and velocities, beyond primal RMS control.
