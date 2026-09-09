# Exact raw GD: all-angle first-layer action and moment bounds

Root draft, 2026-09-06. UNREVIEWED. This is a standalone finite-width
estimate, not a population-limit or GD/GF-comparison theorem. It treats
the exact updates, not transformed Euler or clipping. No experiment,
external theorem, or population existence assumption is used.

## 1. Model and claim

Two inputs x_a in R^d have ||x_a||^2=d, and C_ab=x_a^T x_b/d.
Thus C is positive semidefinite, with spectral norm at most 2, including
aligned and antiparallel inputs. Labels satisfy |y_a|=1. The two
activations may differ and obey

    phi_ell in C2, |phi_ell|<=B_ell,
    |phi_ell'|<=P_ell, |phi_ell''|<=L_ell, ell=1,2.

At width n the matrices W^(1),W^(2) have shapes n by d, n by n,
and W^(3) is the rescaled readout vector. At each node compute

    z^(1)_a=W^(1)x_a, h^(1)_a=phi_1(z^(1)_a),
    z^(2)_a=W^(2)h^(1)_a, h^(2)_a=phi_2(z^(2)_a),
    f_a=(W^(3))^T h^(2)_a/n, r_a=f_a-y_a, L=sum_a r_a^2,
    delta^(2)_a=W^(3)phi_2'(z^(2)_a),
    q^(1)_a=(W^(2))^T delta^(2)_a,
    delta^(1)_a=phi_1'(z^(1)_a)q^(1)_a, c_a=-2r_a.

With eta=n^-2, the exact simultaneous raw updates are

    W^(1)+=W^(1)+(eta/d)sum_a c_a delta^(1)_a x_a^T,
    W^(2)+=W^(2)+(eta/n)sum_a c_a delta^(2)_a(h^(1)_a)^T,
    W^(3)+=W^(3)+eta sum_a c_a h^(2)_a.              (1)

Assume ||W^(2)_0||_op<=a and max_i|W^(3)_{0,i}|<=b, where a,b
do not depend on n. No maximum bound on z^(1)_0 is assumed. For
every T<infinity and all sufficiently large n (threshold depending
only on T,a,b and the activation bounds), the iterates through
ceil(T/eta) have nonincreasing loss and uniform readout, operator,
and RMS reverse-field bounds. For their RAW linear interpolation,
write z_i(t)=(z^(1)_{1,i}(t),z^(1)_{2,i}(t)) and h_i similarly,
recomputing h_i=phi_1(z_i). There is a finite constant V_T, independent
of width, input angle, dimension, and label pattern, such that

    (1/n)sum_i sup_(t<=T)|z_i(t)|^4
       <=(8/n)sum_i|z_i(0)|^4+512 B_1^2(T+1)^2 V_T^2,           (2)
    (1/n)sum_i integral_0^T |dot z_i(t)|^3dt
       <=16 B_1 P_1 V_T^2,                                  (3)
    (1/n)sum_i integral_0^T |dot h_i(t)|^3dt
       <=16 B_1 P_1^4 V_T^2.                                (4)

These are bounds for the actual prescribed GD clock and interpolation.
They do not assert that these iterates converge to finite or population
GF at a general angle.

## 2. Stopped primal bounds independent of width

The case T=0 is immediate. In what follows T>0, so ceil(T/eta)>=1.

The raw parameter tangent metric is

    ||V||_raw^2=d||V^(1)||_F^2/n+||V^(2)||_F^2+||V^(3)||^2/n.

The direction of (1), divided by eta, is exactly -grad_raw L by
differentiating the prediction. Initially sqrt(L_0)<=R_0, where
R_0=sqrt(2)(B_2 b+1). Stop just before the first node with residual
norm greater than R=R_0+1. Up to and INCLUDING that candidate exit
node, every preceding update has sum_a |c_a|<=K=2sqrt(2)R.
Put H=T+1, allowing eta<=1. Summing the exact readout updates gives

    max_i|W^(3)_{k,i}|<=M=b+B_2 K H.

Summing the rank-one updates, whose operator norms equal the products
of the two RMS factor norms, gives a finite bound

    ||W^(2)_k||_op<=A=a+H K P_2 M B_1.             (5)

These deliberately enlarged bounds apply at every endpoint up to
the candidate exit. Along each raw segment both quantities also obey
(5), by convexity of the corresponding norms. At those endpoints and
along these segments,

    ||delta^(2)_a||/sqrt(n)<=P_2 M,
    ||q^(1)_a||/sqrt(n)<=Q=A P_2 M.               (6)

The last statement evaluates the hidden fields at the segment's raw
parameters, not by hidden interpolation. It uses only bounded gates.

## 3. A raw-metric Hessian bound and actual descent

Let a raw tangent V have norm at most one and define
alpha_1=sqrt(d/n)||V^(1)||_F, alpha_2=||V^(2)||_F,
alpha_3=||V^(3)||/sqrt(n). Each alpha is at most one. Input
normalization gives

    ||D_V z^(1)_a||/sqrt(n)<=alpha_1,
    ||D_V z^(2)_a||/sqrt(n)<=B_1 alpha_2+A P_1 alpha_1.

Set J=B_1+A P_1 and F_*=B_2+M P_2 J. The prediction differential
therefore obeys |D_V f_a|<=F_* for unit V, or
||grad_raw f_a||_raw<=F_*.

For another unit tangent U with factors beta_1,beta_2,beta_3,

    D_U D_V z^(2)_a
      =V^(2)[phi_1'(z^(1)_a)U^(1)x_a]
       +U^(2)[phi_1'(z^(1)_a)V^(1)x_a]
       +W^(2)[phi_1''(z^(1)_a)(U^(1)x_a)(V^(1)x_a)].

The product of two vectors has RMS norm at most sqrt(n) times the
product of their RMS norms. Thus the last display's RMS norm is
at most P_1(alpha_2 beta_1+beta_2 alpha_1)
+A L_1 sqrt(n)alpha_1 beta_1. The mixed prediction derivative has
four terms: the two readout/hidden cross terms, the top curvature
term, and the pairing of W^(3)phi_2' with the last display. Bound
the top curvature using the COORDINATEWISE bound M and Cauchy--Schwarz.
This gives

    |D_U D_V f_a|
      <=2P_2 J+M L_2 J^2+M P_2(2P_1+A L_1 sqrt(n))
      =:F_{**}(n).                                         (7)

This calculation accounts for every second derivative and uses the
specified raw metric. Its only width growth is at most sqrt(n).

The update direction at an admissible old node has raw norm at most
sum_a |c_a| F_*<=K F_*. Along its segment the bound F_* remains
valid by (5). Hence the residual norm along that segment is at most
R+sqrt(2)eta K F_*^2. For sufficiently large n this is at most R+1.
Since

    D^2 L=2sum_a (D f_a tensor D f_a+r_a D^2 f_a),

the raw Hessian norm along the segment is at most

    H_*(n)=4F_*^2+2sqrt(2)(R+1) F_{**}(n)<=C_T(1+sqrt(n)).    (8)

Apply the scalar integral Taylor formula along that segment, with
update -eta grad_raw L. For eta H_*(n)<=1 it yields

    L_{k+1}<=L_k-(eta/2)||grad_raw L_k||_raw^2.              (9)

The condition holds for eta=n^-2 at all sufficiently large n,
uniformly up to the candidate exit. By induction (9) keeps
L_{k+1}<=L_0<=R_0^2 at that node, contradicting exit above R_0+1.
Thus no exit occurs through the padded horizon. All primal bounds
(5)--(6) and (9) are now unconditional under the initial norm bounds.
This is a closed first-exit proof, not an assumed GD stability premise.

## 4. Total variation of the controlled reverse queries

All quantities in this section are computed at nodes of the actual
uncut iterates. Constants below are finite and independent of n.
Their precise optimal values are unnecessary; the displayed bounds
show that such constants exist.

From (1),

    ||Delta W^(2)||_op<=eta K P_2 M B_1,
    ||Delta W^(3)||_infinity<=eta K B_2,
    ||Delta z^(1)_a||/sqrt(n)<=eta K P_1 Q.

Since phi_1 is P_1-Lipschitz, the exact product difference
z^(2)_{k+1}-z^(2)_k=Delta W^(2) h^(1)_k+
W^(2)_{k+1}(h^(1)_{k+1}-h^(1)_k) gives

    ||Delta z^(2)_a||/sqrt(n)<=eta C_T.

The Lipschitz bound L_2 on phi_2', and bounded readout at both
endpoints, then give ||Delta delta^(2)_a||/sqrt(n)<=eta C_T.
Use the ACTUAL transpose difference

    Delta q^(1)_a=(Delta W^(2))^T delta^(2)_{k,a}
                    +(W^(2)_{k+1})^T Delta delta^(2)_a

to get ||Delta q^(1)_a||/sqrt(n)<=eta C_T. There is no assumption
on an Lp action of the transpose. The segment bound on Df from
Section 3 also gives sum_a|Delta c_a|<=eta C_T.

For N=ceil(T/eta), put v_{k,a,i}=c_{k,a}q^(1)_{k,a,i}, and

    U_i=sum_a |v_{0,a,i}|+
                    sum_(k=1)^(N-1) sum_a|v_{k,a,i}-v_{k-1,a,i}|.

An empty sum is zero. Minkowski and the preceding node estimates give

    [(1/n)sum_i U_i^2]^(1/2)<=K Q+(T+1)C_T=:V_T.            (10)

In particular sum_a|v_{k,a,i}|<=U_i, and max_i U_i<=sqrt(n)V_T.
This estimate does not claim that individual neurons are independent
or that the envelope is bounded uniformly coordinatewise in n.

## 5. Discrete work, absorption, and the raw interpolation

Let w_{k,i} denote row i of W^(1)_k and put

    A_i=sum_(k=0)^(N-1) eta d||(w_{k+1,i}-w_{k,i})/eta||^2.

Write e_{k,i}=d||(w_{k+1,i}-w_{k,i})/eta||^2. At a node, with
d_{k,i,a}=v_{k,a,i}phi_1'(z^(1)_{k,a,i}), the exact update gives

    e_{k,i}=d_{k,i}^T C d_{k,i},
    Delta z_i=eta C d_{k,i},
    |Delta z_i|^2<=2eta^2 e_{k,i}.                          (11)

Taylor's formula for each scalar activation has remainder at most
(L_1/2)|Delta z^(1)_{a,i}|^2. Consequently

    sum_a v_{k,a,i}(h^(1)_{k+1,a,i}-h^(1)_{k,a,i})
       =eta e_{k,i}+R_{k,i},
    |R_{k,i}|<=L_1 eta^2 U_i e_{k,i}.                       (12)

Since eta L_1 max_i U_i<=L_1 V_T n^-3/2, it is at most 1/2
for all sufficiently large n. Sum (12), keep the error on the left,
and apply discrete summation by parts. The latter sum is

    sum_a [v_{N-1,a,i}h^(1)_{N,a,i}-v_{0,a,i}h^(1)_{0,a,i}]
      -sum_(k=1)^(N-1)sum_a
            (v_{k,a,i}-v_{k-1,a,i})h^(1)_{k,a,i},

whose upper bound is 2B_1 U_i. Thus

    (1/2)A_i<=2B_1 U_i, or A_i<=4B_1 U_i.                   (13)

For the actual raw interpolation, z_i is affine on each cell, so
|dot z_i|<=2P_1 U_i and integral_0^(N eta)|dot z_i|^2<=2A_i.
Combining with (13) gives

    integral |dot z_i|^3<=16 B_1 P_1 U_i^2.

The recomputed activation obeys |dot h_i|<=P_1|dot z_i| almost
everywhere on the same interpolation. This proves (3)--(4), including
partial terminal cells. Also

    sup_(t<=T)|z_i(t)|<=|z_i(0)|+sqrt(2(T+1)A_i),

so (a+b)^4<=8(a^4+b^4) and (13) prove (2).
One-sided values of velocities at mesh nodes do not affect these
integrated estimates; either right-interior/left-terminal convention
is consistent with the asserted raw interpolation.

## 6. Gaussian initialization and limitations

For independent W^(1)_ij~N(0,1/d), W^(2)_ij~N(0,1/n), and
W^(3)_i~N(0,n^-2), the assumptions hold with a=8,b=1 on events
whose probabilities tend to one. Indeed a 1/4 sphere net with at
most 9^n points, approximation of both test vectors, and the scalar
Gaussian exponential bound give

    P(||W^(2)_0||_op>8)<=2 exp(-(8-2log9)n),
    P(max_i |W^(3)_{0,i}|>1)<=2n exp(-n^2/2).

The net-size bound follows by placing disjoint radius-1/8 balls
around a maximal 1/4-separated set inside the radius-9/8 ball.
The scalar tail bound follows from E exp(lambda G)=exp(lambda^2
Var(G)/2) and optimizing lambda. Finally the iid first-row pairs
have E|z_i(0)|^4=8+4rho^2<=12 and a finite eighth moment, so their
empirical fourth moment converges in probability by Chebyshev.

For each deterministic input pair, intersect the two initial norm
events with {(1/n)sum_i |z_i(0)|^4<=13}. The failure probability is at
most 1680/n+2exp(-(8-2log9)n)+2n exp(-n^2/2), by Chebyshev and
E|z_i(0)|^8<=8 E(G_1^8+G_2^8)=1680. This probability bound is uniform
over deterministic normalized input pairs, not a simultaneous event
over inputs chosen after seeing initialization.

On these events (2)--(4) bound the empirical first-path quadratic
tail by C/R^2 and the first-velocity quadratic space-time tail by C/R.
Thus, for either empirical tail functional F_n(R) and every epsilon>0,

    lim_(R->infinity) limsup_(n->infinity)
                  P(F_n(R)>epsilon)=0.

This is empirical uniform integrability IN PROBABILITY, not a bound
on exceptional-event expectations. Deterministically the same bounds
hold for any family with the stated initial norm bounds and a uniform
empirical initial fourth moment. The cubic velocity estimate also
bounds the path Holder 2/3 seminorm in empirical third moment. Together
these yield first-path tightness in probability in the uniform topology
of C([0,T];R^2), with second-moment control. No almost-sure statement
across every width or expectation-level uniform integrability is made.

This proof does not identify a subsequential population law, establish
uniqueness or restart at a general angle, show raw GD follows GF there,
or control all second-layer and reverse-field moment tails. Neither
these estimates nor nonincreasing discrete loss establish the full
joint MF/GF theorem. The result is a width-uniform, all-angle positive
estimate for the exact requested raw optimizer and first-layer paths.
