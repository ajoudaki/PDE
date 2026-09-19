# Perturbed many-anchor continuation and actual query tails

Author derivation, 2026-09-19. This is a study-owned candidate, not an
established or independently reviewed theorem. Scientific inputs are the
study contract, `docs/NOTATION.md`, and the maintained proofs explicitly
cited below. No sibling research output is used.

## 1. Statement and conventions

Fix separately integers `1 <= m <= d`, labels `y_a in {-1,+1}`, and a
finite `T>0`. Write `v_a=e_a` and let `u_a in S^(d-1)` satisfy
`max_a |u_a-v_a| <= rho`. Both datasets have weights `p_a=1/m`.
The first weight row is `w`, the middle action is `A=A_0+K`, and the
stored readout is `c`. All three blocks are retained. The two neuron
spaces are separate; `A_0^*` is the actual adjoint of `A_0`.

The canonical initialized carrier is the generated Gaussian carrier of
special_data_limits III.F.1--7, with the complete root `g~N(0,I_d)`,
`K(0)=0`, `c(0)=0`, and `||A_0||op<=10`. Include a countable dense
sphere subset, rational meshes, and the finite observation programs in
its language; continuity then defines other deterministic inputs.
For `phi=tanh`, set

```
z1(u)=w.u, h1(u)=phi(z1(u)), z2(u)=A h1(u), h2(u)=phi(z2(u)),
f(u)=<c,h2(u)>, delta(u)=c phi'(z2(u)), Q(u)=A*delta(u),
r_a=f(u_a)-y_a.
```

The physical mean-loss field is

```
w' = -2 sum_a p_a r_a phi'(w.u_a) Q(u_a) u_a,
K' = -2 sum_a p_a r_a delta(u_a) tensor h1(u_a),
c' = -2 sum_a p_a r_a h2(u_a).                         (P1)
```

Here `(b tensor h)v=b<h,v>`. The raw Hilbert norm is the square sum of
the full row `L2(R^d)`, learned-increment HS, and readout L2 norms.
Use the equivalent sum distance
`d(theta,bar theta)=||w-bar w||2+||K-bar K||HS+||c-bar c||2`.
At finite width its three summands are respectively
`||w_n-bar w_n||F/sqrt(n)`, `||K_n-bar K_n||F`, and
`||c_n-bar c_n||2/sqrt(n)`. Rank matrices are `b h^T/n`.
These are precisely stored variances `(1,1/n,1/n^2)`, mobilities
`(n,1,n)`, and the unhalved mean squared loss.

The result proved below is: there are positive `rho=rho(T,m,d)` and
`h_*=h_*(T,m,d)` such that sufficiently fine raw Euler programs for
every such configuration have uniformly bounded named backward
coefficient rows, including every passive sphere query. They have
Gaussian marginal tails, uniformly in mesh, time node, and deterministic
input. They converge strongly to a unique canonical `C1` solution of
(P1) through T. Uniqueness holds against all strong raw competitors with
the same primitives and reached initial state, without imposing tails
on those competitors. Actual finite GF and raw GD with `eta_n -> 0`
have the same limit through T, retaining the random finite initial
readout. Their empirical tails satisfy the asymptotic high-probability
envelopes in Section 8. The GD improvement beyond the conservative
`eta_n sqrt(n)->0` is explicitly proved there and should receive
independent audit.

Only a reference learning/activity margin, if a learning conclusion is
desired, remains an input to the final corollary. Reference existence
and reference tails on every fixed T are proved here from maintained
results; no perturbed source-tail hypothesis is assumed.

## 2. Raw bounds and a one-reference estimate

Put

```
C=exp(2T)-1, R=exp(2T), M=10+2TRC,
W=sqrt(d)+2TRMC, V=2R(MC+C+1).                         (P2)
```

For every population raw Euler mesh of nonnegative steps `h_k` with
total length at most T, `||c_k||infinity<=C`, `|r_ka|<=R`,
`||K_k||HS<=2TRC`, `||A_k||op<=M`, `||w_k||2<=W`, and the sum
speed of its affine interpolant is at most V. Indeed
`||c_{k+1}||infinity+1 <= (1+2h_k)(||c_k||infinity+1)`.
The other inequalities follow by summing the rank norm identity and
`||Q||2<=MC`. No discrete energy inequality is used.

On any common bounded raw ball, for the two equal-weight configurations
with maximum input displacement `epsilon`, and any cutoff `b>=1`,

```
||F_U(theta)-F_V(bar theta)||sum
 <= C_raw [(1+b)(d(theta,bar theta)+epsilon)
            +tau_b(bar c)+sum_a p_a tau_b(bar Q(v_a))],    (P3)
tau_b(q)=||q 1_{|q|>b}||2.
```

This is also valid for two states with identical inputs, and in the
normalized same-width norms. Here and below HS refers only to K.
For completeness, a valid explicit constant on the ball (P2) is given
by

```
b0=2+M+W+C, a=b0(b0+1), b2=1+2a, b1=b0(b2+3),
A1=b0^2(b0^3+1)+(b0+1)b1+(b0+1)b0^2,
A2=b0(b0^3+1)+(b0+1)b2+(b0+1)b0^2,
A3=b0^3+1+(b0+1)a,
C_raw=2(A1+A2+A3)+4(b0+1)^2.                           (P4)
```

To verify this, at a matched pair with input distance e, forward
subtraction gives errors at most `b0(d+e)` for z1 and
`a(d+e)` for z2; the residual difference is at most `b0^3(d+e)`.
The only unbounded multiplier estimate required is

```
||[phi'(z)-phi'(bar z)]P||2
 <=2b||z-bar z||2+2tau_b(P).                             (P5)
```

Apply it first to `bar c` in delta, subtract the adjoint action, and
then apply it to `bar Q` in the first gate. The resulting upper and
lower backward differences are bounded by respectively
`b2(1+b)(d+e)+2tau_b(bar c)` and
`b1(1+b)(d+e)+2b0 tau_b(bar c)+2tau_b(bar Q)`.
Subtract the residual, backward, input-vector factors of the first
velocity separately. Subtract the three factors of each middle rank
and the two factors of the readout velocity. Their coefficients are
bounded by A1,A2,A3, and their combined tail coefficient by
`4(b0+1)^2`. The rank subtraction uses
`||a tensor b-a' tensor b'||HS <=||a-a'||2||b||2+||a'||2||b-b'||2`.
Averaging proves (P3). The argument is independent of row dimension:
`||Pu||L2(R^d)=||P||2|u|` and
`||bar w.(u-v)||2<=||bar w||2|u-v|` are the only vector facts.
This verifies, rather than assumes, the required specialization of
global_nonlinear C.4.1 and C.4.7.2.

## 3. Exact finite-program source equations

All assertions in this section are for a fixed finite program before
any uniform-in-mesh estimate. Put `mu_ka=h_k/m` and
`gamma_ka=-2mu_ka r_ka`. All current forward calls precede reverse
calls. A passive output is appended as one distinguished unused
current slot and does not change training. Earlier unused queries have
zero coefficients in later training expressions.

For past training slots p and a current query i=(k,u), the exact source
form is

```
z2_i = xi_i + sum_{p<k} F_i,p delta_p,
Q_i  = zeta_i + sum_{p<=k} D_i,p h1_p,
F_i,p = alpha_i,p + gamma_p E1[h1_i h1_p],
D_i,p = beta_i,p + 1_{p<k} gamma_p E2[delta_i delta_p],
alpha_i,p=E1[partial_{zeta_p}h1_i],
beta_i,p=E2[partial_{xi_p}delta_i].                       (P6)
```

The sole current term for a passive query is its distinguished slot,
`beta_i,i=E2[c_k phi''(z2_i)]`; other current terms are zero.
The centered Gaussian source groups have cross-program covariances

```
E2[xi_i xi_j]=E1[h1_i h1_j],
E1[zeta_i zeta_j]=E2[delta_i delta_j].                     (P7)
```

The reverse group is independent of the complete d-dimensional g.
The two source orientations are independent; actual answers are
dependent through their response terms. Formal source derivatives
freeze residuals, coefficients, contractions, and source covariances.
Named slots remain distinct at singular covariance.

The lower pulse `v_k;p=partial_{zeta_p}w_k`, zero for k<=s when
p=(s,b), obeys

```
v_{k+1;p}=v_{k;p}+sum_a gamma_ka u_a [
 phi''(w_k.u_a) Q_ka (u_a.v_{k;p})
 +phi'(w_k.u_a){1_{(k,a)=p}
       +sum_{q<=k}D_ka,q phi'(w_{t(q)}.u_q)(u_q.v_{t(q);p})}],
alpha_ku,p=E1[phi'(w_k.u) u.v_k;p].                       (P8)
```

The upper pulses are

```
C_k;p=sum_{q<k}gamma_q phi'(z2_q) U_q;p,
U_i;p=1_{i=p}+sum_{q<k}F_i,q V_q;p,
V_i;p=phi'(z2_i) C_k;p+c_k phi''(z2_i) U_i;p,
beta_i,p=E2[V_i;p].                                      (P9)
```

These formulas follow by expanding learned ranks and differentiating
their complete coordinate expressions. III.F.1--7 gives them first
with bounded-derivative coordinate maps. The fixed-program unbounded
product extension global_nonlinear A.2 applies to each raw program:
every extra product is a bounded smooth gate times Q; at a fixed
graph the Q expression is Gaussian plus a finite sum of bounded
features. Smooth product clipping gives polynomial envelopes for all
first source derivatives in the finite Gaussian/root list. Those
envelopes have every finite moment. Chronological covariance-square-root
coupling, dominated convergence, and coefficient induction remove the
clipping, including at singular covariance. A.1 and the finite same-array
RMS argument identify these values with the actual fixed-program limit.
Scalar contractions are recovered causally with the two-factor RMS
inequality. Thus (P6)--(P9) do not posit a law for a growing transcript.

## 4. An independent physical-clock reference anchor

For the orthogonal reference, B.1 with `kappa_1=kappa_2=kappa_3=1/m`
gives its unique global physical flow and strong clock-Euler limit.
Let `J_X=sech^2 J`, `J(0,g)=g`, and set

```
w_a=J(X_a,g_a) (a<=m),   w_a=g_a (a>m),
X'_a=-(2/m)r_a Q_a,
K'=-(2/m)sum_a r_a delta_a tensor h1_a,
c'=-(2/m)sum_a r_a h2_a.                                 (P10)
```

Since `|J_X|<=1`, the active feature derivative is `sech^4 J<=1`.
The full passive feature is
`tanh(sum_{a<=m}u_a J(X_a,g_a)+sum_{a>m}u_a g_a)`.
Its difference for the same roots is bounded in L2 by
`x=sum_{a<=m}||X_a-bar X_a||2`. This retains all unused row roots.
The passive derivative vector in the trained clock coordinates is
`phi'(w.u)(u_a phi'(w_a))_{a<=m}`, of Euclidean norm at most one.
Its difference is bounded pointwise by `4|w-bar w|`, because changing
the outer gate costs `2|u.(w-bar w)|` and changing the inner vector
costs at most `2|w-bar w|`.

Write `kappa=||K-bar K||HS`, `z=||c-bar c||2`. For two reference
clock states on (P2), put

```
V2=sum_a||z2_a-bar z2_a||2 <= Mx+m kappa,
D2=sum_a||delta_a-bar delta_a||2 <= m z+2C V2,
P2=sum_a||Q_a-bar Q_a||2 <= M D2+mC kappa,
S2=sum_a|r_a-bar r_a| <= m z+C V2.                       (P11)
```

The three velocity differences, in the norm `x+kappa+z`, are at most

```
(2/m)(MC S2+R P2),
(2/m)(C S2+R D2+RC x),
(2/m)(S2+R V2).                                         (P12)
```

Every term proportional to m in (P11) cancels against `1/m` in
(P12); the x terms have `1/m<=1`. Their sum is at most
`L(x+kappa+z)` for

```
L=100(1+M+C+R)^4, E=exp(LT),
P0=2(MC^2+2RMC+C^2+2RC+C+R),
K0=1+2C(M+1), B_cl=2C+T P0 K0 E.                         (P13)
```

These bounds also hold after adding a fresh root to one answer and
recomputing all descendants. The readout and rank bounds use bounded
tanh and gates, not energy. A reverse-answer pulse `epsilon e` at
p=(s,b) changes its clock immediately by at most
`2R mu_p |epsilon| ||e||2`. A forward pulse changes activation,
delta, residual, and reverse answer by at most respectively
`1,2C,C,2MC` times `|epsilon| ||e||2`. Subtraction in the three
updates therefore gives immediate clock/HS/readout distance at most
`P0 mu_p |epsilon| ||e||2`. Later passive delta differences are at
most K0 times that distance. Euler amplification is at most E.

The fresh-root extraction in C.4.5.2 is applicable with these verified
constants. To specify its hypotheses: clip the full Gaussian root
smoothly at fixed level, and use a readout clip inactive on a
neighborhood of [-C,C]. Clock derivatives of all active and passive
features remain bounded independently of root clipping. At each fixed
graph every source derivative has a finite deterministic bound.
Chronological covariance-square-root coupling removes the root clip
and makes the named coefficients continuous as epsilon tends to zero.
At fixed mesh and fixed nonzero epsilon first take width to infinity.
The fresh root e is independent of every source group and the original
roots in its coordinate expression. Conditional Gaussian integration
by parts gives
`E[e V^epsilon]=epsilon E[partial_slot V^epsilon]`.
The unforced expression is independent of e. Cauchy--Schwarz in the
joint fixed-program limit, then division by |epsilon|, then epsilon
to zero, prove

```
|alpha^cl_ku,sb|<=2R E mu_sb,
|beta^cl_ku,sb|<=P0 K0 E mu_sb (s<k),
|beta^cl_ku,ku|<=2C.                                    (P14)
```

Thus every reference clock mesh has passive beta row sum at most B_cl.
There is no inference of a transverse derivative from values on a
singular support. In particular, with
`D_cl=B_cl+2RC^2T`, its reverse answers have form
`Q=G+J0`, `Var G<=C^2`, `|J0|<=D_cl`; forward answers have analogous
Gaussian-plus-bounded form from the alpha bound in (P14).

These tails pass to the actual reference flow before constructing any
raw source cap. Adjoin refining clock programs to the common carrier.
Equation (P7) implies
`||zeta_delta-zeta_delta'||2=||delta-delta'||2` and
`||xi_h-xi_h'||2=||h-h'||2`. Clock-Euler strong convergence, its
bounded readout and bounded actions imply convergence of h and delta
uniformly in time. Hence the source assignments converge in L2 to
Gaussian sources with the limiting Gram covariances. Subtracting them
from the convergent actual queries gives an L2 limit of the uniformly
bounded remainder, which has the same bound by an almost surely
convergent subsequence. The same passive-input estimates and compact
sphere extend this from a dense set to every deterministic u. Thus
the actual reference already has uniform individual Gaussian tails
through T. This argument does not import the two-anchor risk or
feature-clock estimates of C.4.5.2.

## 5. Raw reference cap

We first record estimates under a temporary cap B on every previously
constructed passive beta row. They are used here and in Section 6.
Put

```
D=B+2RC^2T,
L_p(B)=4R exp(6RDT+8R^2 p T^2 C^2),
f_B=L_1(B)+2R, d0=2RT+2C.                              (P15)
```

Equations (P6)--(P7) give
`Q_ku=zeta_ku+J_ku`, `|J_ku|<=D`, `Var(zeta_ku)<=C^2`.
For every lambda>=0, Jensen with weights `mu_ja/sum_j h_j` gives

```
E exp(lambda sum_{j<k,a}mu_ja |Q_ja|)
 <=2 exp(lambda TD+lambda^2 T^2 C^2/2).                   (P16)
```

No independence between these Q fields is used. In (P8), put
`M_k;p=max_{s<j<=k}|v_j;p|`, where the norm is Euclidean in R^d.
The direct pulse is at most `2R mu_p`; the propagation factor at j
is at most `1+2Rh_j(D+2sum_a p_a |Q_ja|)`. Pathwise iteration,
then (P16), gives

```
||M_k;p/mu_p||Lp<=L_p(B),
|alpha_ku,p|<=L_1(B)mu_p, |F_ku,p|<=f_B mu_p.             (P17)
```

This holds for every fixed finite p>=1. For the upper rows, sum the
absolute values of (P9) over named sources. If Umax_k is the largest
such U row through k, its C row is at most `2RT Umax_k`, and its V
row is at most `d0 Umax_k`. Hence

```
Umax_k<=1+f_B d0 sum_{j<k}h_j Umax_j<=exp(f_B d0 T),
sum_p|C_k;p|<=2RT exp(f_B d0 T),
sum_p|V_ku;p|<=d0 exp(f_B d0 T).                         (P18)
```

These are pointwise inequalities. They only use past lower rows when
constructing the current upper row. The absolute bounds do not select
a cap by themselves, and no fixed point inequality in B is used.

Let `F0(z)=z/2+sinh(2z)/4`, so `F0'=1/phi'`. For each of the m
trained reference coordinates, raw Euler is
`w^+_a=w_a+h b_a phi'(w_a)`, `b_a=-(2/m)r_a Q_a`.
Its exact transformed defect is

```
R_h(w,b)=F0(w+h b phi'(w))-F0(w)-h b
 =h^2 b^2 phi'(w)^2 int_0^1(1-s)F0''(w+s h b phi'(w))ds.
                                                               (P19)
```

The inequalities
`phi'(w)^2|F0''(w+z)|<=2e^(2|z|)` and
`phi'(w)^2|F0'''(w+z)|<=4e^(2|z|)`, together with
`|phi''|<=2phi'`, give for an absolute constant c0

```
|R_h|<=c0 h^2 b^2 e^(2h|b|),
|partial_w R_h|<=c0 h^2 b^2(1+h|b|)e^(2h|b|),
|partial_b R_h|<=c0 h^2 |b|(1+h|b|)e^(2h|b|).             (P20)
```

These follow by differentiating the integral in (P19), preserving its
cancellation, rather than separately bounding F0 at its two endpoints.
For every named lower pulse p,

```
|partial_p R_h|<=c0 h^2(1+h|b|)e^(2h|b|)
                    (b^2|partial_p w|+|b||partial_p b|). (P21)
```

Here is the complete m-coordinate summation. Restrict hmax<=min(1,T).
Under the temporary raw cap, each b has all Lp and scalar exponential
moments, uniformly in its time and anchor, because it is a deterministic
multiple of a Gaussian-plus-bounded Q. For instance
`||b||Lp <=(2R/m)(C||N(0,1)||Lp+D)` and
`E e^(lambda |b|)<=2 exp(2lambda RD/m+2lambda^2 R^2 C^2/m^2)`.
Thus (P20) summed over the m coordinates and steps gives

```
sum_k sum_{a<=m}||R_{h_k}(w_ka,b_ka)||Lp
 <= C_def(B,p,m,T) hmax.                                 (P22)
```

For p0=(s,b), at its injection time all `partial_p0 w_sa=0` and
`partial_p0 b_sa=-(2/m)r_sb 1_{a=b}`. Divide (P21) at this step by
`mu_p0=h_s/m`; the factor `h_s^2(2/m)/(h_s/m)` is `2h_s`.
There is only one nonzero direct coordinate, so its normalized Lp
contribution is bounded by a constant times h_s. At every later step,
(P8),(P17), and the D row bound give, for each trained a,

```
||partial_p0 w_ka/mu_p0||Lp<=L_p(B),
||partial_p0 b_ka/mu_p0||Lp<=(2R/m)D L_p(B).
```

Use Hölder in (P21), with higher fixed moments supplied by the displayed
Gaussian exponential bound and (P17), then sum each of the m coordinate
norms and use `sum_k h_k^2<=T hmax`. This proves

```
(1/mu_p0) sum_{k>=s}sum_{a<=m}||partial_p0 R_{h_k,a}||Lp
 <= C_def'(B,p,m,T) hmax.                                (P23)
```

The constants are finite sums and products of c0, m, R, C, D,
`L_{4p}(B)`, Gaussian moments of fixed order, and the displayed
exponential moments with lambda a fixed multiple of p. This specifies
all their dependencies. Neither a pointwise maximum of Gaussian
histories nor division by a vanishing mesh length survives. The d-m
untrained reference coordinates have zero defect and zero pulse.
There is no upper-source derivative of this lower-population defect:
the coordinate expression only depends on g and zeta when coefficients
are frozen.

Compare raw reference Euler and clock reference Euler on a common mesh.
There is a deterministic `eta_h ->0` controlling their raw state
distance independently of a raw source cap. To prove this, compare raw
Euler to the actual reference using (P3), the reference-flow Gaussian
tails proved in Section 4, and its affine-to-left-endpoint movement
at most Vhmax. For a fixed cutoff b the distance is bounded by
`C_T exp(C_T(1+b))[(1+b)hmax+exp(-a_T b^2)]`.
First optimize b tending slowly to infinity as hmax tends to zero.
Compare clock Euler to that same actual flow using (P11)--(P12): its
bounded-speed Lipschitz field gives global error at most `C_T hmax`.
The scalar bound on J converts clock distance to raw distance. These
two comparisons define the required eta_h.

Now set `X^r_a=F0(w^r_a)-F0(g_a)`, and let X^c be clock Euler. The
raw recurrence for X is exactly (P10) with defect (P19). Its source
pulse chi is `partial_zeta X`. Let `J_q^r,J_q^c` be the row vectors
of the first feature's clock derivatives. Their sup norms in the
dual of the clock sum norm are <=1, and their L2 difference is
bounded by `4||w^r-w^c||2<=4eta_h`. The two differentiated clock
recursions are exactly

```
chi^r_{k+1;p}=chi^r_{k;p}+sum_a gamma^r_ka e_a [1_{(k,a)=p}
            +sum_{q<=k}D^r_ka,q J_q^r chi^r_{t(q);p}]
            +partial_p R_k,
chi^c_{k+1;p}=chi^c_{k;p}+sum_a gamma^c_ka e_a [1_{(k,a)=p}
            +sum_{q<=k}D^c_ka,q J_q^c chi^c_{t(q);p}].     (P24)
```

Use the coordinate l1 norm for chi in this display. The clock reference
cap gives the pointwise bound
`max_j |chi^c_j;p|_1/mu_p <=2R exp(2R D_cl T)`.
The raw propagation in (P24) has deterministic coefficient at most
`2Rh_kD` in the maximum l1 norm. The residual coefficients differ by
at most `C_T mu_ka eta_h`; the learned part of a D row differs by
at most `C_T eta_h`. Denote the beta-row discrepancy by E_k,
taking the supremum over the same passive sphere input.
Subtraction of (P24), (P23), and deterministic discrete Gronwall give

```
||max_{j<=k}|chi^r_j;p-chi^c_j;p|_1||2/mu_p
 <=C_B(eta_h+hmax+sum_{j<k}h_j E_j).                      (P25)
```

Here and in this paragraph C_B depends only on B,m,d,T. To see that
the forcing has the claimed form, telescope gamma, D and J one at a
time, multiply each changed coefficient by the unchanged bounded
normalized clock pulse, and sum `sum_a mu_ka=h_k`; the defect sum
is exactly (P23). No raw pulse supremum has been assumed bounded.
Taking expected outside-gate derivatives, then summing `sum_p mu_p<=T`,
gives the same bound for the alpha row discrepancy. Learned F terms
are bounded by the elementary field discrepancy eta_h. Finally
subtract (P9), sum the absolute source derivatives, and use (P18).
Its strictly-past convolution has density `f_B mu_q`, so a second
discrete Gronwall gives

```
E_k<=C_B(eta_h+hmax+sum_{j<k}h_j E_j).                     (P26)
```

For explicit verification of this last step, the differences obey
`dU=sum dF bar V+sum F dV`,
`dC=sum (d gamma phi'(bar z)bar U+gamma dphi'(z)bar U+
gamma phi'(z)dU)`, and
`dV=phi'(z)dC+dphi'(z)bar C+c phi''(z)dU+
[dc phi''(bar z)+c dphi''(z)]bar U`.
The barred derivative row is bounded pointwise, the gate differences
are L2-bounded by eta_h, and every memory coefficient has its time/atom
mass. Summing these inequalities gives (P26) without a current E_k
on its right side.

Choose the temporary cap `B=B_cl+1`. At a first potentially failing
raw row, all estimates above use only previously capped raw rows.
Gronwall in (P26) bounds that row's discrepancy by
`C_B exp(C_BT)(eta_h+hmax)`. Choose `h_*>0`, also at most min(1,T),
so this is <=1/2 for all hmax<=h_*. Then the current raw row is
at most `B_cl+1/2<B`; it cannot fail. The initial readout and beta
row are zero. Hence all reference raw Euler programs with hmax<=h_*
have the passive cap

```
B_*=B_cl+1.                                              (P27)
```

This first bootstrap uses only the independently proved physical-clock
anchor and its actual-flow tails. It involves no perturbed-law tails.

## 6. Perturbed source cap with an explicit positive radius

Set `B=B_*+1`, and define the following constants from (P2),(P15):

```
D=B+2RC^2T, Q24=24C+D, P=L_24(B), f=L_1(B)+2R,
d0=2RT+2C, U0=exp(f d0 T), V0=d0 U0,
I4=2exp(6RDT+32R^2T^2C^2).                               (P28)
```

Run the perturbed and reference raw programs on the same mesh and
canonical source carrier, with identical names and masses h/m. Let
`eta=max_k d(theta_k,bar theta_k)`, `epsilon=max_a|u_a-v_a|`,
`delta=eta+epsilon<=1`, and `I=delta^(1/16)`. Define E_k as the
supremum beta-row discrepancy over pairs of passive outputs (u,v)
with `|u-v|<=epsilon`, pairing the distinguished current slots and
all past training slots. This includes each active pair and the
same passive input pair. Because all inputs are uniformly close,
there is no rare far atom and no unweighted transport cost.

Use the temporary cap B on previous nearby rows. Put

```
h1=1+W, z2=1+M h1, a2=1+2C z2, q2=M a2+C, r2=1+C z2,
G=1+24h1+q2(1+2Q24)+r2,
J=2T r2 C^2+4RTC a2, F2=2r2+4R h1.                       (P29)
```

In the first-failure argument at row k, every use of a Q24 moment or of
the Q L12 interpolation below is at a training query with time j<k,
feeding the lower-pulse recurrence. Those rows have already passed the
cap. The current passive row needs only the unconditional L2 forward,
delta and Q comparisons and bounded upper gates. Its own Gaussian Q
moment bound is a conclusion after its beta row passes, not a premise
in the comparison of that row.

At every paired output, telescoping gives L2 differences of z1,h1,z2,
delta,Q bounded by respectively `h1 delta,h1 delta,z2 delta,
a2 delta,q2 delta`, and residual difference at most r2 delta.
The first-layer phi' and phi'' gate differences have L12 norm at
most GI: interpolate their L2 differences with their bounded norms;
`|phi'''|<=6` suffices. For Q, interpolation of L2 with L24 gives
`||Q-bar Q||12 <=(q2 delta)^(1/11)(2Q24)^(10/11)<=GI`.
The L24 bound follows from `Q=Gaussian+bounded` under the temporary
cap, with `||N(0,1)||24<=24`. Also
`|gamma_p-bar gamma_p|<=2mu_p GI`, and

```
sum_q|D_ku,q-bar D_kv,q|<=E_k+J delta.                    (P30)
```

Indeed the changed gamma contraction costs `2T r2 C^2 delta`,
and the two changed delta factors cost `4RTC a2 delta`.

For clarity the full lower-pulse comparison constants are

```
J0=2G(1+2R),
Alow=18R G Q24 P+2R P(5G D+J), Zlow=2R P,
Cv=I4(J0+T Alow+Zlow), Calpha=Cv+(G+1)P,
Fdiff=Calpha+F2.                                        (P31)
```

Subtract (P8), placing all differences of the evolving pulse itself
in the unbarred propagation. Its coefficient is
`2Rh_j(D+2sum_a p_a|Q_ja|)`. The normalized direct pulse is
`-2r_sb u_b phi'(z1_sb)`; its L4 difference is <=J0 I.
In the local term, the varied factors are `r,u,phi'',Q,u`, then
one unchanged normalized reference pulse. Before the common factor
`2h_j P`, their five bounds are
`2GQ24,2RQ24,RGQ24,2RG,2RQ24`, times I. Their sum is
at most `9RGQ24 I`. Hölder with three L12 factors gives the L4
estimate used here. In the memory term the varied factors are
`r,u,phi',D,phi'_q,u_q`; the five non-D differences cost
`5RGDP I` and the D difference costs `RP(E_j+JI)`, before
the factor `2h_j`. Therefore the total forcing, apart from the
single direct injection, has L4 norm at most
`h_j Alow I+h_j Zlow E_j`.

The product of all propagation factors is at most
`exp(2RDT+4R sum_ja mu_ja |Q_ja|)`. By (P16) its L4 norm is
at most I4. Pathwise iteration followed by Holder L4 times L4
into L2 proves

```
||max_{j<=k}|v_j;p-bar v_j;p|||2/mu_p
 <=Cv(I+sum_{j<k}h_j E_j).                               (P32)
```

Changing the outside gate and input in the expectation defining alpha
costs at most `(G+1)P mu_p I`; hence, writing
`G_k=I+sum_{j<k}h_j E_j`,

```
|alpha_ku,p-bar alpha_kv,p|<=mu_p Calpha G_k,
|F_ku,p-bar F_kv,p|<=mu_p Fdiff G_k.                      (P33)
```

The additional learned contribution in the second line is at most
`mu_p F2 delta`, from its changed residual and two changed h1 factors.
The estimates only use `|u|=|v|=1` and Euclidean vector inequalities;
the first-row pulse remains the full R^d vector throughout.

For the upper comparison set

```
AU=T Fdiff V0, AC=2T U0(r2+2R z2),
AV=U0(4RT z2+2+6C z2),
Vforce=AC+AV+2(RT+C)AU, Vprop=2f(RT+C),
Csrc=1+Vforce exp(Vprop T).                              (P34)
```

Let Ucal_k,Vcal_k be suprema over the paired passive outputs of
the L2 norms of the sums of absolute U- and V-source differences,
and let Ccal_k be the analogous readout derivative row norm.
The exact subtractions after (P26), (P18), and (P33) give

```
Ucal_k<=AU G_k+f sum_{j<k}h_j Vcal_j,
Ccal_k<=AC I+2R sum_{j<k}h_j Ucal_j,
Vcal_k<=Ccal_k+2C Ucal_k+AV I.                           (P35)
```

The U direct impulses cancel. In C, the changed gamma costs
`2T r2 U0 delta`, and the changed gate costs `4RT z2 U0 delta`.
In V, the changed outside phi' costs `4RT U0 z2 delta`, and
the changed c and phi'' cost `(2+6C z2)U0 delta`. These are
all the forcing terms in (P35). A double time sum is at most T
times its single sum, and G_k is nondecreasing. Substitution yields
`Vcal_k<=Vforce G_k+Vprop sum_{j<k}h_j Vcal_j`.
Two discrete Gronwall estimates therefore give

```
E_k<=Csrc(I+sum_{j<k}h_j E_j)
   <=Csrc exp(Csrc T)(eta+epsilon)^(1/16).                (P36)
```

Crucially, the first inequality has no current unknown E_k on its
right. Its current lower response uses earlier updates, and its
upper memory is strictly earlier. This proves the source comparison
under a temporary cap rather than assuming the new row is capped.

We next bound eta independently of that cap. For the reference raw
program let

```
D_*=B_*+2RC^2T, H=4(1+C+D_*), S=32(1+C)^2,
Gamma=T C_raw.                                          (P37)
```

For `b>=max(1,C,2D_*)`, its tails obey
`tau_b(bar Q)<=H exp(-b^2/S)` and `tau_b(bar c)=0`.
Indeed `Q=G+J0`, `Var G<=C^2`, `|J0|<=D_*`; the Gaussian
integrals `E exp(G0^2/4)=sqrt(2)` and
`E G0^2 exp(G0^2/4)=2sqrt(2)` give
`tau_b(Q)<=4(C+D_*)exp(-(b-D_*)^2/(8C^2))` when C>0.
The stated weaker version follows, including smaller b after the
specified threshold. Applying (P3) to the two same-mesh programs
and summing the recurrence gives

```
eta<=Gamma exp(Gamma(1+b))[(1+b)epsilon+H exp(-b^2/S)].    (P38)
```

Only the reference program supplies tails in this calculation.
The actual program needs just its unconditional raw bounds (P2).

Here is one explicit positive radius. Set

```
Z=16[4+(T+1)Csrc], z=exp(-Z), A=1+Gamma+H+Z,
b=4SA, X=Gamma(1+b), rho=exp(-Z-4-2X).                   (P39)
```

All constants are finite and determined by T,d and the already proved
reference cap; h_* may also depend on fixed m. We have S>=1, so
this b exceeds `max(1,C,2D_*)`. If epsilon<=rho, the law term
in (P38) is at most `z e^-4 X e^-X<z/4`. For the tail term,

```
log(4Gamma H)+X+Z
 <2+2Gamma+H+Z+Gamma b
 <=2A+4SA^2<=6SA^2<16SA^2=b^2/S.
```

Here `log Gamma<=Gamma` holds for every Gamma>0. Thus that term
is below z/4, eta<z/2, and epsilon<=rho<z/2. Consequently
`delta<z<1`, validating the assumed interpolation range. Equation
(P36) is then less than
`Csrc exp(T Csrc) exp(-Z/16)=Csrc exp(-4-Csrc)<1/4`.
At a first potentially failed nearby beta row, all preceding rows
obey B, and the same-input pair (u,u) shows its row is less than
`B_*+1/4<B`. This contradiction closes the second bootstrap.
Initialization has zero beta. Hence every nearby raw Euler program
with hmax<=h_* has the uniform passive cap B through T.

The radius (P39) is independent of neural width, mesh, elapsed step
count, observation order, and numerical closure resolution. Its size
is a qualitative existence certificate. It is not claimed practical.

## 7. Strong completion and reached tails

The cap just proved applies also at every affine interpolation time:
stop the programme at its preceding node and append the corresponding
shorter final step. That is an admitted mesh, and recomputing the
features at its endpoint gives exactly the interpolated-state query.
For all these states, every deterministic sphere input has

```
Q^h(t,u)=zeta^h(t,u)+J^h(t,u),
Var(zeta^h(t,u))<=C^2, |J^h(t,u)|<=D,
z2^h(t,u)=xi^h(t,u)+I^h(t,u),
Var(xi^h(t,u))<=1, |I^h(t,u)|<=C f_B T.                 (P40)
```

The source variances and their full cross-time/input/program
covariances are those in (P7). Nothing asserts independence of a
remainder from its source, or a tail for a maximum over the sphere.
In particular set

```
H_B=4(1+C+D), S_B=32(1+C)^2, b_B=max(1,C,2D).
```

Then uniformly in h,t,u,
`tau_b(Q^h(t,u))<=H_B exp(-b^2/S_B)` for b>=b_B.
The same calculation gives a Gaussian envelope for z2, using its
variance bound one and remainder bound `C f_B T`. The readout is
bounded. The first-row fields also have uniform Gaussian-type
moment growth: from their actual update,

```
|w^h(t)-g|<=2R sum_{j,a}mu_ja |Q_ja|,
||w^h(t)||Lp(R^d)<=||g||Lp(R^d)+2RT(C||G0||Lp+D).         (P41)
```

For p>=2, `||g||Lp(R^d)<=sqrt(d)||G0||Lp` by Minkowski on the
squared coordinates, and `||G0||Lp<=c sqrt(p)` for an absolute c
(the even integer Gaussian moment formula and monotonicity suffice).
Thus the Lp norms in (P41) grow at most a constant times sqrt(p).
Markov at an even p proportional to a large threshold squared gives
an exponential-in-threshold-squared tail, also for every first
preactivation. This is a statement about each deterministic t,u;
it uses no Gaussian process maximum.

We construct the strong flow directly from the Gaussian tails, so
there is no small tail-exponent versus T condition. Let U,V be two
admitted configurations, q=max_a|u_a-v_a|, and let their Euler
interpolants have mesh maxima h,h'. The raw distance of preceding
nodes is at most the interpolated-state distance plus V(h+h').
Apply (P3) to those nodes and integrate. For every b>=b_B,

```
sup_{t<=T} d(theta_U^h(t),theta_V^{h'}(t))
 <=Gamma exp(Gamma(1+b))
     [(1+b){q+V(h+h')}+H_B exp(-b^2/S_B)].                (P42)
```

Define Omega(s) as the infimum of the right-hand expression with
`q+V(h+h')` replaced by s, truncated above by the common raw diameter,
and define Omega(0)=0. Then Omega(s)->0. For example at small s>0
choose `b=max(b_B,sqrt(2S_B log(1/s)))`; its right side is
`O_T((1+sqrt(log(1/s))) exp(C_T sqrt(log(1/s))) s)`.
This is at most `C_H sqrt(s)` for a finite constant C_H depending
only on the fixed displayed constants, because
`-x/2+C_T sqrt(x)+log(1+sqrt(x))` is bounded above for x>=0.
Thus a Holder modulus is available, but no numerical rate in a
closure order is inferred.

Taking U=V proves the affine Euler curves Cauchy in
`C([0,T];L2(R^d) directsum HS directsum L2)`. Completeness supplies
a limit theta_U with the prescribed initial state and retained
Gaussian primitives. Every component satisfies the bounds (P2).
For the readout, an almost surely convergent subsequence at a fixed
time preserves `|c(t)|<=C`; L2 time continuity and a dense time
set give a jointly measurable version with that bound.

The vector field is continuous in the raw state along these limits.
Forward fields are L2 continuous by bounded actions and Lipschitz
activation. Subtracting delta and Q uses the bounded readout in the
varying gate product. More generally, at a fixed state a bounded
continuous multiplier converging in probability converges strongly
when applied to its fixed L2 factor: truncate that factor, use
bounded convergence in probability on the truncated part, then
remove the truncation. Apply this to the first gate times Q.
Rank differences are HS continuous by the rank identity. Since
there are finitely many training atoms, the whole field is continuous.
Its continuity is uniform along the compact limiting time path:
otherwise times of a fixed error have a convergent subsequence and
continuity at their limiting state gives a contradiction.
Consequently the preceding-node fields converge uniformly to the
continuous limiting field. Passing the Euler integral equation to
the limit yields

```
theta_U(t)=(g,0,0)+int_0^t F_U(theta_U(s))ds.             (P43)
```

This is a strong C1 equation, with one-sided endpoint derivatives.
The coordinate operations do not need to be Frechet differentiable
as L2-valued maps. The scalar-gradient theorem III.F.10 applies to
the finite sum loss: tanh has bounded first and second derivatives,
the learned increments are HS, the action and its actual adjoint
are retained, and every field lies in its indicated L2 population.
Its gradient is precisely minus (P1). Hence

```
L_U(t)+int_0^t ||theta'_U(s)||raw^2 ds=L_U(0)=1,
||c_U(t)||infinity<=2t.                                  (P44)
```

The latter follows pointwise from
`sum_a p_a|r_a|<=sqrt(L_U)<=1` in the readout equation.

The Gaussian decompositions pass to this actual reached flow, not
just a marginal subsequence. Include all refining Euler programs
in the common Gaussian language. Their source cross covariance
(P7) makes the forward-source assignment an L2 isometry on the
span of its h1 inputs and the reverse-source assignment an L2
isometry on the span of its delta inputs. In particular a source
difference has precisely the L2 norm of the corresponding input
difference. The limit is therefore independent of the refining
mesh. State convergence and the common readout supremum give
uniform L2 convergence, in time and input, of h1,delta,z2,Q:
for example

```
||delta-bar delta||2 <=||c-bar c||2
       +2C(||K-bar K||HS+M||w-bar w||2),
||Q-bar Q||2 <=M||delta-bar delta||2+C||K-bar K||HS.        (P45)
```

The bounds are uniform over |u|=1. Thus the sources converge too.
Their finite-dimensional distributions are centered Gaussian and
their covariance matrices converge; the limiting source is Gaussian
with the exact limiting Gram covariance. Independence of zeta from
the full root g persists in these joint limits. Subtracting sources
from fields passes both remainder bounds of (P40) to the actual
flow, by an almost surely convergent subsequence of the L2 error.
This supplies actual reached active and passive Gaussian tails with
the same constants. A countable dense time/input set and L2
continuity provide jointly measurable representatives, sufficient
for every time or input integral. The uniform tail bounds hold for
each deterministic t,u with a constant independent of both.

Law continuity follows by sending h,h' to zero in (P42). The same
configuration modulus holds for the full row, K, and c. Whole-sphere
prediction satisfies

```
sup_u |f_theta(u)-f_bar theta(u)|
 <=[1+C(M+1)] d(theta,bar theta).                         (P46)
```

For reached uniqueness, let another strong raw solution share the
same state and primitives at time s. Its continuous path is bounded
on [s,T]. Enlarge the raw constant in (P3) to cover both paths,
keeping the constructed solution as the tail-bearing endpoint.
No pointwise readout bound or tail hypothesis is needed for the
competitor. Fixed-cutoff Gronwall at zero initial discrepancy gives
`d(t)<=C_T exp(C_T(1+b)) H_B exp(-b^2/S_B)`.
Sending b to infinity proves equality. Restriction of (P43) supplies
existence from every reached endpoint. Thus restart uses the
current fields and fixed action primitives, not old clocks or
newly sampled Gaussian directions.

Finally, these estimates include actual fixed finite Euler programmes
in the precise width-limit sense. At each fixed mesh their same-layer
node tuples, including any fixed passive queries, converge in W2
by Section 3; the actual finite initial readout has RMS and supremum
tending to zero and is handled additively by finite-program induction.
For `v_b(q)=q-clip_b(q)`, the map is 1-Lipschitz and
`tau_{2b}(q)<=2||v_b(q)||2<=2tau_b(q)`. Thus, at each fixed finite
node/query set and each fixed b>=b_B, their actual empirical tails
are bounded in probability by
`2H_B exp(-b^2/S_B)+o_P(1)` at threshold 2b. Compact input nets
extend this to the sphere because their Q fields are uniformly
L2-Lipschitz in u on the common ball. Interpolation in time is
handled by its uniformly bounded raw speed and (P45). This is an
asymptotic finite-width tail envelope, not an assertion that a
trained finite-width coordinate is Gaussian or that arbitrary
growing transcripts satisfy a fixed-program theorem.

## 8. Actual finite GF and raw GD

The supplied companion `FINITE_CAPTURE_PROOF.md`, author freeze
SHA256 `b3285d52c1685c67ef8931483545869d5f9d8942566d86ac8229a7f1dea86367`,
has now been read in full. Its sole population input (F1) is supplied
by (P2),(P40)--(P45), including strong Euler convergence, complete
fixed-program laws, uniform marginal Gaussian Q tails, and fractional
final steps. For its tail statement at every R>=1, enlarge the
prefactor to cover `1<=R<b_B`, using `||Q||2<=MC`; the exponent
may remain `1/S_B`. This verifies every hypothesis of that unit.

Its Sections 2--4 establish width-independent raw bounds and a
comparison to one fixed proxy programme, with no actual-trajectory
tail assumption. The sole raw-GD discrepancy is movement from the
interpolated state to its preceding actual node, at most `V_T eta_n`
in the raw sum norm. The proxy has an independently fixed mesh h
and Gaussian marginal tails from its finite-program limit. The
one-reference estimate gives error at most

```
T exp(C_T(1+b)T)
 {C_T(1+b)V_T(h+eta_n)+C_T B1 exp(-a1 b^2)+o_P(1)}.       (P47a)
```

Choose b first, then a fixed h, and finally width. Every probability
error concerns that fixed programme. Thus the proved sufficient
raw-GD condition is `eta_n->0`, and actual finite GF is the same
argument with eta_n=0. In particular the conservative condition
`eta_n sqrt(n)->0` also suffices. Raw parameters are interpolated
and hidden quantities recomputed. The finite random readout is
retained throughout.

We give explicitly the actual finite tail consequence, beyond the
proxy-tail use needed for capture. At every fixed cutoff b>=b_B and
every epsilon>0, for actual finite GF or those raw-GD sequences,

```
Pr{sup_{t<=T,u in S^(d-1)} tau_{2b}(Q_n(t,u))
          >2H_B exp(-b^2/S_B)+epsilon} ->0,              (P47)
```

and the analogous forward-query envelope follows from (P40). Here
tau is the actual empirical neuron RMS tail. At each fixed input,
the companion's joint W2 convergence identifies the empirical L2
norm of `v_b(Q_n)=Q_n-clip_b(Q_n)`, uniformly in time. Its limiting
norm is at most `tau_b(Q)<=H_B exp(-b^2/S_B)`. All Q fields on
the common finite raw/readout ball satisfy

```
||Q_n(t,u)-Q_n(t,v)||RMS
 <=2 C_fin M_fin^2 W_fin |u-v|.                           (P47b)
```

This follows successively from h1 Lipschitzness, the bounded action,
the upper gate Lipschitz constant two, and the adjoint bound. The
population has the analogous modulus. Since v_b is 1-Lipschitz,
a finite sphere net extends convergence of these positive-part
norms to every u. A finite time net is equally valid, using the
bounded raw speed and (P45); the companion already supplies the
fixed-input time-uniform version. Finally
`tau_{2b}(Q_n)<=2||v_b(Q_n)||RMS` proves (P47).
For z2, the input Lipschitz constant is `M_fin W_fin`, and its
Gaussian-plus-bounded envelope from (P40) gives the same proof.
For z1 or the complete row, (P41) gives a Gaussian-type marginal
envelope, while fixed-tuple W2 convergence and the analogous
positive-part argument give its empirical counterpart. The finite
readout is bounded on the high-probability raw ball.
These are actual reached-field empirical tail envelopes. They do
not assert that trained finite coordinates are Gaussian or that
their exponential moments are bounded uniformly in finite width.

The finite crude ball must use distinct constants from (P2): on the
high-probability initialization event `||A_0,n||op<=10`,
`||w_0,n||F/sqrt(n)<=sqrt(d)+1`, `||c_0,n||infinity<=1`,
one may take `S_fin=T+1`, `C_fin=2exp(2S_fin)-1`,
`R_fin=2exp(2S_fin)`, `M_fin=10+2S_fin R_fin C_fin`, and
`W_fin=sqrt(d)+1+2S_fin R_fin M_fin C_fin` for raw GD with
eta_n<=1 and raw Euler. The slack interval covers the last actual
GD node used to interpolate T. Actual finite GF is globally defined
by its exact finite
gradient energy identity and has a compatible common raw ball.
These separate constants prevent silently resetting the actual
finite readout to zero.

The companion's Section 5 proves the observation conclusion for any
separately fixed
finite correctly typed program of the full w,c, named h1,z2,h2,delta,Q
fields, initialized generated probes, A_0/A_0*, and current A/A*,
K/K* actions, globally Lipschitz coordinate maps, and bounded
continuous gates multiplying named L2 fields. Joint same-population
W2 laws and quadratic contractions hold, including paired initialized
and current observations. No uniform claim
over all observation words, or arbitrary unbounded coordinate
products, is part of this interface.

## 9. Transfer of reference learning and paired activity margins

This unit proves continuation for every prescribed finite T. To use
it for a learning statement, supply a reference margin
`L_ref(T)<1/4` and positive paired hidden displacement at a specified
`t0 in (0,T]`; their proofs are logically separate. Equation (P42)
gives `sup_t d(theta_U,theta_ref)<=Omega(rho)` after shrinking the
radius if needed. In addition to (P46), changing an evaluated input
costs at most `CMW rho` for prediction. Hence

```
|L_U(T)-L_ref(T)|
 <=2R{[1+C(M+1)]Omega(rho)+CMW rho} ->0.                 (P48)
```

This uses identical labels and the equal-weight pairing; both
residuals have magnitude at most R. Paired hidden displacement is a
quadratic contraction of initialized and current bounded hidden
features. Strong state convergence, Lipschitz hidden maps and
input continuity make each such fixed finite collection continuous,
so a strict positive reference margin persists for a smaller
positive radius. The precise learning/activity constants and their
finite-network transfer are assembled by the supervisor's separate
reference and assembly units. They are not hypotheses in the source
bootstrap or the strong-flow construction above.

## 10. Dependency and failure audit

The causal order is: canonical fixed-program calculus; unconditional
raw/clock balls; independent physical-clock cap; actual reference
Gaussian tails by source isometry; raw-reference comparison plus
summed named-clock defects; raw-reference cap; unconditional raw
comparison to that cap; supported-input coefficient perturbation;
perturbed cap; strong completion and actual reached Gaussian tails.
In particular the two bootstraps do not use the current unproved
row, and closeness to one reference is never substituted for
convergence of changed-law programmes.

Full row coordinates and passive sphere directions survive every
step. There is one retained Gaussian action and its adjoint; learned
increments are HS but the initialized action is not assumed HS.
No Gram inversion or rank lower bound is used. The constants need
not be uniform when m or d grow. Source-moment estimates refer to
individual queries or time/atom-weighted sums, not to a Gaussian
history maximum. Limits involving finite-width programmes keep
the programme fixed before taking width to infinity. The actual
finite-GF/GD step is supplied by the complete frozen capture unit
identified and hypothesis-checked in Section 8. Learning/activity
margins remain a separate reference input to Section 9, rather than
an unproved premise of continuation. All units remain author
candidates pending independent review.
