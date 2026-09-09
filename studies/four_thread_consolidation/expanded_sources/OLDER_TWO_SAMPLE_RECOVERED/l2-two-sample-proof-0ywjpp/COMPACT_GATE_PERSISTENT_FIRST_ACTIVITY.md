# Persistent first-gate activity for actual two-sample depth-two dynamics

Bounded author sidecar, 2026-09-06. This proves a finite-width,
high-probability lower bound, uniform on each fixed finite time horizon,
for EACH sample's empirical first-gate square. It applies to the actual
gradient flow and exact simultaneous raw GD with eta=n^-2, including
the raw interpolation inside whole cells. It does not prove nonzero
motion, nonlazy dynamics, or a mean-field theorem. No experiments,
agents, external sources, or changes to the source notes were used.

## 1. Model, theorem, and probability quantifiers

Fix R>0 and a smooth even function p:R->R with p>0 on (-R,R),
p=0 outside [-R,R], and p>=0 everywhere. Set

    phi_1(z)=integral_0^z p(s) ds,   phi_2(z)=arctan(z).

Thus phi_1 is odd and bounded, and p(+-R)=0. Choose finite bounds

    |phi_ell|<=B_ell, |phi_ell'|<=P_ell,
    |phi_ell''|<=L_ell, ell=1,2,

with L_1>0. In particular p is L_1-Lipschitz. One may take
B_2=pi/2, P_2=1, L_2=2 and B_1=integral_0^R p(s)ds.
No monotonicity of p on either half of its support is assumed.

Fix deterministic inputs x_1,x_2 in R^d, independently of the
initialization, with

    ||x_1||^2=||x_2||^2=d,
    x_1^T x_2/d=rho in [-1,1),
    C=[[1,rho],[rho,1]],     y_1=1, y_2=-1.

There are two hidden layers of width n. The readout W^(3) is rescaled.
All initialization entries, including across blocks, are independent:

    W^(1)_ij(0)~N(0,1/d),
    W^(2)_ij(0)~N(0,1/n),
    W^(3)_i(0)~N(0,n^-2).

At each raw state define, for a=1,2,

    z^(1)_a=W^(1)x_a, h^(1)_a=phi_1(z^(1)_a),
    z^(2)_a=W^(2)h^(1)_a, h^(2)_a=phi_2(z^(2)_a),
    f_a=(W^(3))^T h^(2)_a/n, r_a=f_a-y_a,
    L=r_1^2+r_2^2, c_a=-2r_a,
    delta^(2)_a=W^(3) phi_2'(z^(2)_a),
    q_a=(W^(2))^T delta^(2)_a,
    delta^(1)_a=p(z^(1)_a)q_a.

Products of vectors here are coordinatewise. The raw GD updates are

    Delta W^(1)=(eta/d)sum_a c_a delta^(1)_a x_a^T,
    Delta W^(2)=(eta/n)sum_a c_a delta^(2)_a(h^(1)_a)^T,
    Delta W^(3)=eta sum_a c_a h^(2)_a,       eta=n^-2.       (1)

All right sides are evaluated at the old node. GF uses the same right
sides as derivatives, with eta removed. Between GD nodes, interpolate
the RAW parameters linearly and recompute hidden fields. In particular
z^(1) is exactly affine in each cell; h^(1) is recomputed as phi_1(z^(1)).

Write G_(a,i)=z^(1)_(a,i)(0). Define the following initialization sets
for rows i; for each ordered pair a,b with b!=a, when -1<rho<1 set

    S_a={i: |G_(a,i)|<=R/2,
              |G_(b,i)-rho G_(a,i)|>=3R}.                 (2)

At rho=-1 instead set

    S_0={i: |G_(1,i)|<=R/2}.                              (3)

Let Phi denote the standard Gaussian distribution function, put
m_0=2Phi(R/2)-1, and define

    m_rho=m_0 * 2[1-Phi(3R/sqrt(1-rho^2))], -1<rho<1,
    m_(-1)=m_0.                                         (4)

All these numbers are strictly positive for the indicated fixed angle.
Let

    E_n={||W^(2)(0)||_op<=8, ||W^(3)(0)||_infinity<=1},

    A_n(rho)=E_n intersect {|S_1|/n>=m_rho/2,
                            |S_2|/n>=m_rho/2}, -1<rho<1,
    A_n(-1)=E_n intersect {|S_0|/n>=m_0/2}.               (5)

THEOREM. For each T>=0 there is a deterministic finite V_T>0 and a
finite integer n_T, independent of n,d,rho, such that the following
holds. Define

    H=T+1, m=m_rho, M=2V_T/sqrt(m),
    delta=(R/2) exp(-2L_1 M H),
    p_delta=min_{|z|<=R-delta} p(z)>0,
    kappa_(T,rho)=(m/4) p_delta^2>0.                      (6)

On A_n(rho), GF at every width n and raw GD at every n>=n_T satisfy,
SEPARATELY for a=1,2,

    inf_{0<=t<=T} (1/n)sum_i p(z^(1)_(a,i)(t))^2
        >= kappa_(T,rho).                                (7)

For each scheme and each sample, there is a fixed subset of at least
nm/4 first rows whose preactivations remain in [-R+delta,R-delta]
throughout this horizon. For GD they remain there on all whole cells
needed to cover the horizon. The subsets may depend on the scheme
and horizon, but do not change with time inside that horizon.

More explicitly, set

    b_n=2exp[-(8-2log 9)n]+2n exp(-n^2/2),
    e_n(rho)=8(1-m_rho)/(n m_rho),       -1<rho<1,
    e_n(-1)=4(1-m_0)/(n m_0).

Then

    P(A_n(rho))>=1-b_n-e_n(rho).                          (8)

Thus, at each fixed T and rho, (7) holds for both schemes and both
samples together with probability tending to one as n grows. The
initialization event (5) itself is independent of T. For GF it works
for every finite T at the given width; for GD the sufficient width
threshold is chosen after T. This is not a positive constant uniform
over unbounded time, nor is a lower bound uniform over rho asserted.
In particular (4)'s interior-strip mass can be very small near an
endpoint. The probability estimate concerns each fixed deterministic
input pair, not inputs selected after inspecting initialization.

An exception-free deterministic claim over all Gaussian realizations
would be false: at any finite n there is positive probability that
every row starts with both |G_(a,i)|>=R. All such first rows are frozen
under (1) and GF, so both gate-square averages are identically zero.
The high-probability finite-width statement (7)--(8) is the claimed
actual lower bound.

## 2. Actual primal bounds and explicit admissible step conditions

This section and the next reproduce the needed estimates from the
three source notes, with common enlarged constants for the two schemes.
No limiting dynamics or assumed GD/GF comparison is used.

For fixed T>=0 set H=T+1 and, for GD, N=max(1,ceil(T/eta)); then
N eta<=H whenever eta<=1. Under E_n put

    R_0=sqrt(2)(B_2+1), R_*=R_0+1, K=2sqrt(2)R_*,
    W_*=1+B_2 K H,
    A=8+H K P_2 W_* B_1, Q=A P_2 W_*,
    J=B_1+A P_1, F=B_2+W_* P_2 J,
    F_2(n)=2P_2 J+W_* L_2 J^2
                       +W_* P_2(2P_1+A L_1 sqrt(n)),
    H_2(n)=4F^2+2sqrt(2)(R_*+1)F_2(n).                    (9)

These are finite and independent of angle and dimension; only the
displayed F_2,H_2 depend on width. In particular H_2(n)=O_T(1+sqrt(n)).
The two initial norms in E_n imply ||r(0)||<=R_0.

Use the fixed raw tangent metric

    ||V||_raw^2=d||V^(1)||_F^2/n
                       +||V^(2)||_F^2+||V^(3)||^2/n.

Differentiating f and L shows directly that (1) is
-eta grad_raw L and GF is -grad_raw L. Thus GF has

    dot L=-||grad_raw L||_raw^2.                          (10)

The smooth finite-dimensional vector field is locally Lipschitz,
so contraction of its integral equation gives a unique local solution.
On any finite interval (10) bounds its integrated squared raw speed
by L(0). Cauchy--Schwarz bounds raw displacement by sqrt(t L(0)).
At fixed n,d this confines the parameters to a compact ball up to any
putative finite terminal time. The vector field is bounded there,
the solution has an endpoint limit, and local existence extends it.
This proves global finite-width GF. Its residual bound, integrated
readout equation, and integrated rank-one W^(2) equation yield

    sum_a |c_a|<=K, ||W^(3)||_infinity<=W_*,
    ||W^(2)||_op<=A,
    ||delta^(2)_a||/sqrt(n)<=P_2 W_*,
    ||q_a||/sqrt(n)<=Q                                  (11)

through T (and also through H with these same constants).

For GD, suppose there is a first node through N with ||r||>R_*.
Every preceding old node has sum_a|c_a|<=K. Summing the readout
updates gives W_*, and summing rank-one operator norm increments
gives A, up to and INCLUDING that candidate node. Convexity gives
these two bounds on all the corresponding raw segments. Bounded
gates then give the two reverse RMS bounds in (11) on those segments.

Here are sufficient checks for actual GD descent, rather than an
assumption that the candidate exit does not occur. For a raw unit
tangent V, put

    alpha_1=sqrt(d/n)||V^(1)||_F,
    alpha_2=||V^(2)||_F, alpha_3=||V^(3)||/sqrt(n).

Each alpha is at most one. Input normalization and (11) give

    ||D_V z^(1)_a||/sqrt(n)<=alpha_1,
    ||D_V z^(2)_a||/sqrt(n)<=B_1 alpha_2+A P_1 alpha_1,
    |D_V f_a|<=F.

For another raw unit tangent U, the mixed second differential is

    D_U D_V z^(2)_a
      =V^(2)[p(z^(1)_a)U^(1)x_a]
       +U^(2)[p(z^(1)_a)V^(1)x_a]
       +W^(2)[p'(z^(1)_a)(U^(1)x_a)(V^(1)x_a)].

Its RMS norm is at most 2P_1+A L_1 sqrt(n): the product inequality
is ||uv||/sqrt(n)<=sqrt(n)(||u||/sqrt(n))(||v||/sqrt(n)).
The two readout cross terms in D_U D_V f contribute at most 2P_2 J.
The top curvature term contributes at most W_* L_2 J^2, using the
coordinatewise readout bound and Cauchy--Schwarz on the two hidden
differentials. The remaining pairing contributes at most
W_* P_2(2P_1+A L_1 sqrt(n)). Hence |D_U D_V f_a|<=F_2(n).

At an admissible old node the update direction has raw norm <=K F.
The segment residual norm is therefore at most
R_*+sqrt(2)eta K F^2. If

    sqrt(2)n^-2 K F^2<=1,     n^-2 H_2(n)<=1,             (12)

then the raw Hessian of L on the segment has norm at most H_2(n),
since D^2L=2sum_a(Df_a tensor Df_a+r_a D^2f_a). Integral Taylor
expansion along the segment gives

    L_(k+1)<=L_k-(eta/2)||grad_raw L_k||_raw^2.

Applied successively through the candidate node this contradicts
L_(k+1)>R_*^2>R_0^2>=L_0. Thus no exit occurs, and (11) and descent
hold for the actual iterates through N. No clipping or changed update
is involved. Conditions (12) hold for all sufficiently large n by
the explicit growth of H_2(n).

## 3. The row envelope, without independence assumptions

Use normalized vector norm ||v||_n=||v||/sqrt(n), and define the
following additional constants, common to both schemes:

    D_A=K P_2 W_* B_1, D_w=K B_2,
    D_Z=D_A B_1+A K P_1^2 Q,
    D_delta=D_w P_2+W_* L_2 D_Z,
    Q_1=D_A P_2 W_*+A D_delta,
    D_c=4K F^2,
    V_T=KQ+H(D_c Q+K Q_1)>0.                             (13)

For GF, the actual equations, the product rule, and (11) imply

    ||dot W^(2)||_op<=D_A,
    ||dot W^(3)||_infinity<=D_w,
    ||dot z^(1)_a||_n<=K P_1 Q,
    ||dot z^(2)_a||_n<=D_Z,
    ||dot delta^(2)_a||_n<=D_delta,
    ||dot q_a||_n<=Q_1.                                  (14)

For the last line specifically use
dot q_a=(dot W^(2))^T delta^(2)_a+(W^(2))^T dot delta^(2)_a.
The preceding line uses the coordinatewise bound W_*; no unproved
multiplication-operator bound on a hidden reverse field is needed.
Also ||dot W||_raw<=KF and ||grad_raw f_a||_raw<=F, so
|dot f_a|<=KF^2 and sum_a|dot c_a|<=D_c.

For GD the corresponding finite differences, divided by eta, obey
exactly the same upper constants at the nodes. Indeed

    Delta z^(2)_a=Delta W^(2) h^(1)_(k,a)
                 +W^(2)_(k+1)(h^(1)_(k+1,a)-h^(1)_(k,a)),

    Delta delta^(2)_a
       =Delta W^(3) phi_2'(z^(2)_(k,a))
        +W^(3)_(k+1)[phi_2'(z^(2)_(k+1,a))
                                 -phi_2'(z^(2)_(k,a))],

    Delta q_a=(Delta W^(2))^T delta^(2)_(k,a)
                            +(W^(2)_(k+1))^T Delta delta^(2)_a.

Using the endpoint bounds and Lipschitz constants in this order
gives ||Delta z^(2)_a||_n<=eta D_Z,
||Delta delta^(2)_a||_n<=eta D_delta and
||Delta q_a||_n<=eta Q_1. Integration of Df along the raw segment
also gives sum_a|Delta c_a|<=eta D_c.

For a first row i put v_(a,i)=c_a q_(a,i). Define the actual GF envelope
and the actual GD envelope separately by

    U_i^GF=sum_a |v_(a,i)(0)|
                 +integral_0^T sum_a |dot v_(a,i)(t)|dt,

    U_i^GD=sum_a |v_(0,a,i)|
                 +sum_(k=1)^(N-1)sum_a|v_(k,a,i)-v_(k-1,a,i)|.
                                                               (15)

The last sum is empty if N=1. These are nonnegative bounds on the
actual controls, not modified parameters or restrictions on training.
For the relevant times, or old nodes k=0,...,N-1, respectively,

    sum_a |v_(a,i)|<=U_i,
    (1/n)sum_i U_i^2<=V_T^2,
    max_i U_i<=sqrt(n)V_T.                               (16)

To verify the averaged bound, the triangle inequality in normalized
Euclidean norm gives ||sum_a|v_(a,i)(0)||_n<=KQ. The product rule
dot v=dot c q+c dot q bounds the normalized norm of the sum of
absolute derivatives by D_c Q+KQ_1. Integrate this bound for GF.
For GD use

    Delta v_a=(Delta c_a)q_(k,a)+c_(k+1,a)Delta q_a

and the same norm inequality, then sum at most N-1 increments, whose
total duration is <=H. This proves (16) with (13). The integral norm
inequality follows directly from finite-dimensional duality and
Cauchy--Schwarz. No independence of U_i, the initial strips, or the
evolved rows has been assumed.

In addition to (12), choose n_T so that, for every n>=n_T,

    L_1 V_T n^-3/2<=1/2.                                (17)

Such a finite n_T exists and is independent of angle and dimension.
Then each GD row has eta L_1 U_i<=1/2 by (16). This proves the step
condition needed below even if the strip-dependent cutoff M is very
large. In particular there is no need to assume eta L_1 M<=1/2.

## 4. A scalar distance barrier for GF and exact whole GD cells

For |x|<R define d(x)=R-|x|. Lipschitz continuity and p(+-R)=0 give

    0<=p(x)<=L_1 d(x).                                  (18)

Suppose x follows dot x=p(x)v(t) while it stays in (-R,R), with
|v(t)|<=U. The function d(x(t)) is absolutely continuous and obeys,
almost everywhere,

    (d(x(t)))' >= -|dot x(t)| >= -L_1 U d(x(t)).

Multiplying by exp(L_1 U t) and integrating gives

    d(x(t))>=d(x(0)) exp(-L_1 U t).                       (19)

Consequently an initially interior scalar coordinate cannot reach
either boundary at a finite time on which the control is so bounded.
This proof does not require a sign for v or differentiability of |x|
at zero; its Lipschitz chain inequality holds almost everywhere.

For the exact scalar GD cell x_theta=x_k+theta eta p(x_k)v_k,
0<=theta<=1, suppose |v_k|<=U and s=eta L_1 U<=1/2. The triangle
inequality and (18) give

    R-|x_theta|>=d(x_k)-theta eta p(x_k)|v_k|
                 >=(1-theta s)d(x_k)>0.                  (20)

Thus the entire cell stays interior. Inductively, for t=(k+theta)eta,

    d(x_theta)>=d(x_0)(1-s)^k(1-theta s)
                  >=d(x_0) exp[-2L_1 U (k+theta)eta].     (21)

For the last inequality, log(1-u)>=-2u on 0<=u<=1/2:
the derivative of log(1-u)+2u is (1-2u)/(1-u)>=0 and the value
at zero is zero. Apply this to s and theta s. Equations (20)--(21)
are statements about the exact raw cell; no interpolated nonlinear
gate or transformed Euler scheme has been substituted.

## 5. Interior angles: a separate protected strip for each sample

Fix -1<rho<1 and an ordered pair a,b with b!=a. For a row write
z_a=z^(1)_(a,i), z_b=z^(1)_(b,i), v_a=c_a q_(a,i), and similarly
for b. Both actual schemes have the exact first-pair equations

    dot z_a=p(z_a)v_a+rho p(z_b)v_b,
    dot z_b=rho p(z_a)v_a+p(z_b)v_b                      (22)

for GF, and the corresponding increments eta times their old-node
right sides for GD. This follows by multiplying the first raw update
by the two fixed inputs, so it uses the physical first layer.

Consider a row initially in S_a. Its initial invariant candidate
e_0=G_b-rho G_a obeys |e_0|>=3R, and

    |G_b|>=3R-|rho|R/2>R.

As long as b is outside the active interval, p(z_b)=0, and (22) gives

    dot(z_b-rho z_a)=0,
    dot z_a=p(z_a)v_a.                                  (23)

For GF start in the open region |z_a|<R, |z_b|>R and stop at its
first exit, if any, before T. Before exit, (19) gives

    R-|z_a(t)|>=(R/2)exp(-L_1 U_i t).

Meanwhile (23) and |z_a|<R give

    |z_b(t)|=|e_0+rho z_a(t)|
                  >=3R-|rho|R>2R.                       (24)

If a first exit occurred at finite time, continuity would preserve a
strict interior margin for a and the strict exterior margin for b
at that time. This contradicts exit. Thus (23)--(24) hold throughout
[0,T]. This first-exit argument closes the dependence between the
invariant and the assumption that b is inactive.

For GD suppose inductively that at node k, a is interior, b is
exterior, and z_(k,b)-rho z_(k,a)=e_0. The old-node value p(z_(k,b))
is zero, so along the whole raw cell

    z_(k+theta,a)=z_(k,a)+theta eta p(z_(k,a))v_(k,a),
    z_(k+theta,b)-rho z_(k+theta,a)=e_0.                  (25)

Condition (17) allows (20) with U=U_i, keeping a interior on that
whole cell. The invariant in (25) then gives (24) on the whole cell
as well. This proves the induction through all N cells, and (21)
gives, for 0<=t<=N eta,

    R-|z_a(t)|>=(R/2)exp(-2L_1 U_i t).                   (26)

In particular a never loses its own gate even inside a cell and b
never contributes a first-gate force to that row. Nothing in the
proof treats the remaining network controls as frozen between GF
times; the bounds use their actual envelope. For GD their old-node
values are precisely those prescribed by the simultaneous update.

This argument has been proved for either specified ordered pair.
It gives a bound for a=1 using S_1 and a bound for a=2 using S_2,
without converting any summed two-sample gate bound into individual
pathwise bounds.

## 6. The singular antiparallel angle

If rho=-1, then

    ||x_1+x_2||^2=2d+2rho d=0,

so x_2=-x_1. Consequently z^(1)_2=-z^(1)_1 at EVERY raw state,
including every interpolated GD state. Since p is even, (22) reduces
for z=z^(1)_(1,i) to the exact scalar equations

    dot z=p(z)(v_1-v_2),
    Delta z=eta p(z_k)(v_(k,1)-v_(k,2)).                 (27)

The effective control has absolute value at most |v_1|+|v_2|<=U_i.
There is no additional factor of two to insert into the scalar step
condition. For every row in S_0, (19) and (21), respectively, give
the same central-distance estimates as above, under (17) for GD.
They apply to both samples because |z_2|=|z_1|, with p(z_2)=p(z_1).
This uses a physical identity, not a distributional sample symmetry
or an inverse of the singular input Gram matrix. No residual-sign
or reverse-field-sign assumption is needed.

## 7. Gaussian occupancy and deterministic removal of large envelopes

Each initial first pair (G_1,G_2) is centered Gaussian with covariance
C, since it is the pair of inner products of one Gaussian W^(1) row
with the fixed inputs. Distinct pairs are independent across rows.
For -1<rho<1 and a specified ordered pair a,b, the two Gaussian
variables G_a and G_b-rho G_a have covariance zero, variances 1 and
1-rho^2, respectively. Their joint Gaussian characteristic function
therefore factors, proving independence. It follows directly that

    P(i in S_a)=P(|G_a|<=R/2)
                  P(|G_b-rho G_a|>=3R)=m_rho>0.

At rho=-1 the pair is (G,-G), and P(i in S_0)=m_0>0. Positivity
follows from the strictly positive one-dimensional Gaussian density
on every finite open interval and on both tails beyond a finite
threshold. Thus it also covers arbitrarily small but fixed R>0.

For each of the specified sets S its membership indicators are iid
Bernoulli(m). Consequently

    E(|S|/n)=m, Var(|S|/n)=m(1-m)/n,
    P(|S|/n<m/2)<=4(1-m)/(n m).                          (28)

The last inequality is Chebyshev, obtained by applying Markov to
the squared deviation from m. Union bound over S_1,S_2 gives the
interior-angle error in (8). At rho=-1 there is only one count, giving
the smaller error stated there. No independence between the two
counts is needed.

For completeness the norm-event error in (8) follows as follows.
A maximal 1/4-separated subset of the Euclidean unit sphere in R^n
is a 1/4-net with at most 9^n points, by comparing disjoint radius-1/8
balls with the radius-9/8 ball containing them. Approximating both
unit vectors in a bilinear form shows

    ||W^(2)(0)||_op<=2 max_{u,v in the net}|u^T W^(2)(0)v|.

Each tested form is N(0,1/n). The Gaussian exponential moment,
E exp(lambda Z)=exp(lambda^2 Var(Z)/2), and optimized exponential
Markov bound give P(|Z|>=s)<=2exp[-s^2/(2Var(Z))]. At s=4,
union bound over at most 9^(2n) pairs yields

    P(||W^(2)(0)||_op>8)<=2exp[-(8-2log 9)n].

The same tail calculation for the readout variance n^-2 gives
P(||W^(3)(0)||_infinity>1)<=2n exp(-n^2/2). Combining these with
(28) proves (8). Independence from the first-row counts is not needed
for this union bound, although initialization does supply it.

Now work deterministically on A_n(rho), for either one of the actual
schemes. By (16), for M in (6),

    (1/n)#{i: U_i>M}<=V_T^2/M^2=m/4.                    (29)

For -1<rho<1 retain

    I_a=S_a intersect {i:U_i<=M},  a=1,2.

Their separate counts obey

    |I_a|/n>=|S_a|/n-#{i:U_i>M}/n>=m/4.                 (30)

At rho=-1 retain I_0=S_0 intersect {i:U_i<=M}, with the same count
bound, and use it for both samples. This subtraction is valid even
if every large-envelope row was selected adversarially from a strip.
In particular U_i can depend on all weights and the entire actual
trajectory; no conditional independence or conditional probability
estimate for it is asserted.

For each retained row GF has distance at least
(R/2)exp(-L_1 M T)>=delta. For GD, N eta<=H and (26) or (27) give
distance at least (R/2)exp(-2L_1 M H)=delta on all N full cells.
Because 0<delta<=R/2 and p is continuous and strictly positive in
(-R,R), it attains a strictly positive minimum p_delta on the compact
interval [-R+delta,R-delta]. Combining this with (30) gives, for
each a and every indicated time,

    (1/n)sum_i p(z^(1)_(a,i)(t))^2
       >= (1/n)sum_{i in I_a}p(z^(1)_(a,i)(t))^2
       >= (m/4)p_delta^2.

At rho=-1 replace I_a by I_0 in this display. This proves (6)--(7),
including their pathwise, uniform-in-time quantifiers. The same
initialization event supplies the proof for both schemes, even though
their actual envelopes and retained sets may differ.

## 8. Scope and exact provenance

The new conclusion is a persistent positive fraction of first rows
with their specified sample's gate bounded away from zero, and hence
a positive average gate square for each sample. Here “trainable” means
that these gates have not saturated. The actual first-layer force
contains c_a q_a and the contributions of both samples; this proof
does not lower-bound those factors or exclude cancellation. It proves
no nonzero first motion, no nonlazy behavior, no positive lower bound
for a reverse-field-weighted tangent kernel, and no mean-field
identification, uniqueness, or GD/GF comparison. No finite-program
response calculation is being asserted as a finite-width result.

Only the following three supplied files were read, in full. They are
author drafts marked unreviewed or not independently audited; the
present sidecar does not confer an independent-audit status on them.
All estimates needed here are reproduced above.

1. `/tmp/l2-two-sample-proof-0ywjpp/COMPACT_GATE_RAW_GD_AND_GAUSSIAN_PATHS.md`
   - Section 1, especially (1): activation assumptions, canonical
     initialization, rescaled model, exact raw updates and clock.
   - Section 2, through (4)--(5): stopped primal controls, raw-metric
     Hessian/descent calculation, and exact first-pair equations.
   - Section 3, especially (8)--(9) and its scalar cases: the discrete
     distance-barrier idea and exterior-gate excursion invariant.
   - Section 4, (11): explicit Gaussian initial norm-event estimate.
   The present proof uses a scalar per-sample strip argument; it does
   not infer individual lower bounds from that note's non-entry into
   the doubly saturated set, feature Gram bounds, or tail estimates.

2. `/tmp/l2-two-sample-proof-0ywjpp/ALL_ANGLE_FIRST_LAYER_ACTION.md`
   - Section 2, (5)--(7) and the displayed D_A,D_w,D_Z,D_delta,Q_1:
     finite-GF continuation, primal bounds, and differentiation of
     the actual first transpose query.
   - Section 3, definition of U_i and (8): the GF row envelope with
     a width-uniform empirical square bound.
   Here (13) uses enlarged common constants and bounds variation of
   c through the raw prediction differential instead of that note's
   explicit residual-kernel bound. The derivation is supplied above.

3. `/tmp/l2-two-sample-proof-0ywjpp/ALL_ANGLE_RAW_GD_ACTION.md`
   - Sections 2--3, (5)--(9): actual GD primal bounds, the raw-metric
     Hessian bound, and the first-exit descent closure.
   - Section 4, exact finite differences and (10): the actual node
     envelope and max_i U_i<=sqrt(n)V_T.
   - Section 5: raw first preactivations are affine inside cells;
     its scale eta L_1 max_i U_i=O_T(n^-3/2) motivates (17).
   No discrete work estimate or path compactness assertion is needed
   for the new gate lower bound.

New work in this sidecar consists of the ordered-sample Gaussian
strip occupancy, its invariant-based scalar reduction with a closed
first-exit/whole-cell argument, the quantitative distance margin,
the deterministic removal of large envelopes, and the resulting
separate sample bounds with explicit probability and step conditions.
The rho=-1 argument uses the physical antiparallel identity and one
center count. Neither case invokes sample exchangeability to deduce
two pathwise bounds from a summed-gate bound.
