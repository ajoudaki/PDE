# Removing the superexponential angular prefactor

2026-10-04. Root author's independent candidate, frozen before exchanging
new findings with the three dimension routes. This is a refinement of the
current sampling study, not a new model or a promotion review. No experiment
was run. Scientific inputs are the complete current-study source and runtime
arguments listed in Section 6. Check status is recorded separately.

## 1. Statement and precise scope

Keep the canonical dense reference, autonomous corrected-readout compressor,
initialization, physical time, fixed data, activation class and probability
quantifiers of `ARCHITECTURE_CONSTANT_REFINEMENT.md`. In particular, with
v=x/sqrt(d),

\[
z^1=Av,\quad z^j=W^jh^{j-1},\quad h^j=\phi_j(z^j),\quad
f_n=w^Th^L/n.
\]

All hidden widths are n, L>=2, A(0) has iid N(0,1) entries, hidden W(0)
have iid N(0,1/n) entries independently, and w(0)=0. Training uses mean
squared loss on m fixed unit v_a with mobilities (n,1,...,1,n). Each
activation is real on the real axis and holomorphic and bounded by B_phi
on |Im z|<a. Put B=max(1,B_phi) and

\[
\beta=\max(10,B,s,t_\phi,16/a),
\]

where s,t_phi>=1 bound the first two activation derivatives on the inner
half strip. Taking s=max(1,4B/a), t_phi=max(1,32B/a^2) always suffices;
for tanh the previous verified choice beta=16 remains valid.

Define Q^0_ab=v_a^Tv_b and Q^j_ab=E[phi_j(Z_a)phi_j(Z_b)] with
Z~N(0,Q^{j-1}). Set gamma=lambda_min(Q^L)>0, Y=||y||_2/sqrt(m),
lambda=min(1,gamma/m), and ell_n=log(en). Under the unchanged condition

\[
Y\le(\gamma/m)\beta^{-62L},                                      \tag{1}
\]

the retained size bound improves to

\[
\operatorname{size}(C)\le
\beta^{82Ld}\frac{(d+3)^{2d-1}}{(d!)^2}
 (m/\gamma)^2\ell_n^{3d+2}+10m(d+1).                           \tag{2}
\]

In particular the simpler bound is

\[
\operatorname{size}(C)\le
\beta^{84Ld}(m/\gamma)^2\ell_n^{3d+2}+10m(d+1).                 \tag{3}
\]

The entire factor (d+3)^d in the previous simpler bound is absent.
The error is unchanged:

\[
\sup_{t\in[0,\infty]}\sup_{\|x\|=\sqrt d}|f_C(t,x)-f_n(t,x)|
\le\beta^{124L}Y(m/\gamma)^{3/2}/\sqrt n.                       \tag{4}
\]

Both predictors converge and fit. For each fixed architecture, compatible
data and confidence, these statements hold with that confidence for each
sufficiently large width. The width threshold is unquantified. They are not
uniform in growing d or L. All retained fixed and moving real coordinates
are counted; setup work and exact-real precision are not bounded. The
compressor remains the previously specified optimizer, not ordinary
gradient flow on an iid smaller network. Neither (3) nor this proof removes
the remaining beta^(84Ld) or the exponent 3d+2 on log(en).

## 2. The whole angular derivative has a better norm

Use the standard periodic parameterization

\[
v_d(\theta)=(\cos\theta_1,\sin\theta_1 v_{d-1}(\theta_2,\ldots)),
\qquad v_1=1.
\]

For d>=2 it covers the real unit sphere. Its analytic moving frame has
first column v_d and remaining columns w_1,...,w_{d-1}, constructed
recursively by adjoining the lower-dimensional frame and multiplying by
a plane rotation. Thus the complex matrix Q_d formed from those columns
is a product of d-1 complex plane rotations and fixed real orthogonal
matrices. A plane rotation at angle theta has Hermitian operator norm
exp(|Im theta|), so

\[
\|Q_d(\theta)\|_{\rm op}\le e^{\sum_j|\Im\theta_j|}.
\]

Direct differentiation of the recursive parameterization gives

\[
D_\theta v_d=[w_1,\ldots,w_{d-1}]
\operatorname{diag}(1,\sin\theta_1,
 \sin\theta_1\sin\theta_2,\ldots).
\]

Since |sin(x+iy)|<=exp(|y|),

\[
\|D_\theta v_d\|_{\rm op}
\le e^{2\sum_j|\Im\theta_j|}\le2
\quad\text{if }\sum_j|\Im\theta_j|\le1/8.                    \tag{5}
\]

This uses a Hermitian operator norm bound, not the false assertion that a
complex orthogonal matrix is unitary. If theta=theta_R+ib, the simultaneous
straight path theta_R+i u b, 0<=u<=1, has

\[
\int_0^1\left\|\frac{d}{du}v_d(\theta_R+iub)\right\|_2du
\le2\|b\|_2\le2\sqrt{d-1}\|b\|_\infty.                      \tag{6}
\]

The previous proof paid d-1 by changing the angles one at a time. Equation
(6) pays only sqrt(d-1), provided the neural derivative is bounded in the
corresponding input-direction norm. The next section supplies that step;
separate coordinate angular bounds alone would not suffice.

## 3. Input-direction responses satisfy the same insertion estimates

Let U_*,V_* be the explicit coefficients from equations (14), (30)--(31)
of `EXPLICIT_SOURCE_CONSTANTS_ROUTE.md`, with the rescaled-budget
substitution in `LABEL_DEPTH_RESCALING_ROUTE.md`. They obey

\[
U_*,V_*\le\beta^{30L}\sqrt{d+3}.                              \tag{7}
\]

The residual-free training response bound remains
max|R_a^j|<=U_*S sqrt(ell_n), where S=16Y/lambda<=1.

For a fixed deterministic complex unit vector u, replace the source
partial_theta h^j in that proof by D_v h^j[u]. Write J_u^j=D_v z^j[u].
On the same stopped physical tube, its exact equations are

\[
J_u^1=Au,\qquad J_u^j=W^j\operatorname{diag}(\phi'_{j-1})J_u^{j-1}.
                                                                    \tag{8}
\]

The first RMS bound is at most 10, below the old angular bound 20.
The old recurrence j_j=20(10s)^{j-1}, b_j=sj_j therefore bounds (8).
In mobility coordinates Theta=(A,sqrt(n)W^2,...,sqrt(n)W^L,w), put
q_u^j=D_v h^j[u]. Its parameter derivative has gate term

\[
\operatorname{diag}(\phi_j''J_u^j)D_\Theta z^j,
\]

whose normalized Hilbert--Schmidt norm is at most t_phi j_j P_j,
and the mixed hidden-weight term U_H q_u^{j-1}/sqrt(n), whose normalized
Hilbert--Schmidt norm is exactly ||q_u^{j-1}||_{2,n}<=b_{j-1}.
The propagated term costs 10s times the previous norm. At the first
layer the mixed map is U_A u, with normalized Hilbert--Schmidt norm
||u||_2=1, below the old angular value two. Consequently the old recurrence

\[
a_1=t_\phi j_1P_1+2s,\qquad
a_j=t_\phi j_jP_j+s(b_{j-1}+10a_{j-1})
\]

still applies. In particular the endpoint E_J and asymmetric Dyson trace
T_J=8f_*E_J are unchanged. The derivative u is held fixed when taking
parameter derivatives; no trainable input or derivative of u is inserted.

The omitted-root expansion uses the same forward observable q_u, with no
direct backward-observable trace. The centered Gaussian term has RMS at
most b_{j-1}, the same-root integral is bounded by S s M_n T_J, and the
learned-row term by S s M_n B b_{j-1}, exactly as for the old angular
source. Here M_n=K_src S sqrt(ell_n) is the training-carrier cap. Thus
the explicit V_j recurrence still bounds J_u, for each fixed u.
The first-layer Gaussian term Au has variance at most one per real or
imaginary part; its learned row is bounded by S s M_n. These are also
smaller than the terms already included in V_1.

To make the estimate simultaneous in u, take a deterministic 1/2-net of
the complex unit sphere (the real sphere in dimension 2d), of size at
most 5^(2d). Such a net follows by taking disjoint radius-1/4 balls at a
maximal separated set and comparing their volumes with the enclosing
radius-5/4 ball. The source proof's query/time mesh has at most n^(4d+3)
points eventually. The extra direction net is at most n^d for n>=25.
The same Gaussian multiplier G_d=8sqrt(d+3) has tail at most
4 exp[-16(d+3)ell_n], which dominates n^(5d+3). Fixed layer/sample
prefactors and the polynomial mesh's fixed constants are absorbed by
the existing eventual-width margin. No factor depending on d changes
G_d, V_*, or the small-label condition.

All off-grid response derivatives have the same sqrt(n) times a fixed
polylogarithmic bound: differentiating (8) and its parameter response
recurrence has precisely the old graph with fixed u in place of
partial_theta v, and omits the latter vector's angular derivative.
The deterministic initial-jet/local-insertion remainder estimates apply
to the same finite augmented graph with this replacement. Their strict
powers of n are unchanged; fixed directional-net multiplicities change
only the eventual width. Every cavity uses its own stopped parameters,
never conditioning an omitted root on full-network survival.

Finally a linear functional on C^d is bounded by twice its maximum over
this net. Applying that deterministic fact to each coordinate of (8)
gives the required simultaneous bound

\[
\max_{i,j,t,\theta}\|D_v z_i^j(t,v(\theta))\|_{\rm op}
\le2V_*\sqrt{\ell_n}.                                       \tag{9}
\]

The operator norm is for a scalar complex-linear functional. It exists
on the stopped tube because all gates have a strict strip margin. No
claim about a new uniform population law is used here.

## 4. Wider angular tube and unchanged source construction

For d>=2 take

\[
c_t=\min(1/8,a/(512U_*)),\qquad
c_a=\min(1/(8d),a/[512\sqrt{d-1}V_*]),
\quad r_t=c_t/\sqrt{\ell_n},\quad r_\theta=c_a/\sqrt{\ell_n}.
                                                                    \tag{10}
\]

The time rectangle is -r_t<=Re t<=T+r_t, |Im t|<=r_t, where
T=32lambda^{-1}ell_n. Every angle has imaginary part of magnitude at
most r_theta. Equations (6) and (9) bound the angular displacement of
each preactivation by 4sqrt(d-1)c_a V_*<=a/128. The two short time
pieces have total displacement at most 8c_t YS U_*<=a/64. Thus

\[
|z_i^j(t,\theta)-z_i^j(t_0,\Re\theta)|\le3a/128<a/32,          \tag{11}
\]

where t_0 is the closest real time in [0,T]. Repeat the stopped-domain
continuation with the extra finite direction-source stops in Section 3.
The training-carrier budgets and time-contour estimates do not depend
on angular width. The negative-Gram propagator on the short non-real
and backwards pieces still costs exp(C r_t)=1+o(1). The source maximum
and insertion stops close with the same strict margins and orders of
limits, and (11) closes the pole stop. This is a new continuation
argument, not an assertion that the enlarged domain was already proved.
No additional label restriction results.

For d=1 use both queries -1,+1 and only the time radius. All four old
source families remain holomorphic with coordinate bound M_0 sqrt(n),
M_0<=beta^(4L). From (7), beta>=10 and L>=2,

\[
c_t^{-1}\le\beta^{32L}\sqrt{d+3},\qquad
c_a^{-1}\le\beta^{32L}(d+3).                                 \tag{12}
\]

For example the nongeometric angular inverse is at most
32 beta^(30L+1)sqrt((d-1)(d+3)), bounded by (12); the other branch 8d
is smaller. The product of inverse radii is therefore

\[
c_t^{-1}c_a^{-(d-1)}\le\beta^{32Ld}(d+3)^{d-1/2}.              \tag{13}
\]

Use the identical weighted-degree Fourier construction of
`DIMENSION_PREFACTOR_OPTIMIZATION.md`, now at radii (10). With
alpha=c_t lambda/(128ell_n^(3/2)), r=c_a/sqrt(ell_n), epsilon=1/n,
P=6^d/(alpha r^{d-1}), and H=2log(16 M_0 sqrt(n)P/epsilon), its
coefficient tail outside alpha|k_0|+r||k'||_1<=H is at most epsilon/16.
Temporal evenness leaves at most

\[
N\le\frac{2^{d-1}[H+\alpha+(d-1)r]^d}{d!\alpha r^{d-1}}
\le64\,18^d\frac{c_t^{-1}c_a^{-(d-1)}}{d!}
 \lambda^{-1}\ell_n^{3d/2+1}.                                \tag{14}
\]

The last bound uses precisely the old eventual inequalities H<=7ell_n
and alpha+(d-1)r<1/4. The exact formula for H continues to include all
dimension/activation constants before those eventual simplifications.
We have not put any inverse radius into the width threshold.

The real source coefficients, up to epsilon accuracy, are constructed
from finitely many initial time jets using the same disk-to-rectangle
continuation and temporary Fourier quadrature. Applying the identical
linear coefficient map to each exact initialized pair (h,W_0h), or
(delta,W_0^Tdelta), preserves its matrix action exactly. Enlarging the
analytic radii only changes the retained index set; it introduces no
trajectory oracle and no retained grid. All discarded jets and setup
samples remain temporary, as in the existing resource contract.

Including all four families, the d=1 two-query case, the initialized
training features and first-weight columns, the maximum source rank obeys

\[
R\le8N+2m+d+1
\le\beta^{36Ld}\frac{(d+3)^{d-1/2}}{d!}
 \lambda^{-1}\ell_n^{3d/2+1}.                                \tag{15}
\]

For the additions in (15), set F_d=(d+3)^(d-1/2)/d!. AM--GM gives
F_d>=2^d/sqrt(d+3)>=1 for d>=1. Also m lambda<=B^2 from the Gram
trace, and d<=beta^(Ld). These absorb 2m+d+1 into the slack between
the numerical multiplier 512*18^d in (14) and beta^(4Ld).

## 5. Inventory and the precise gain

The inherited retained-coordinate inventory is
1020(L+1)R_0^2+10m(d+1), with R_0=max(R,d,m) and the same rank bound
as (15). The conversion lambda^{-2}<=B^4(m/gamma)^2 follows from
gamma/m<=B^2. Since
1020(L+1)B^4<=beta^(10Ld), squaring (15) proves (2).

To simplify the dimension factor, the elementary bound
log(d!)>=integral_1^d log x dx>=d log d-d gives

\[
F_d\le e^d(1+3/d)^d/\sqrt{d+3}
\le e^{d+3}/\sqrt{d+3}\le e^{4d}\le\beta^{Ld}.                \tag{16}
\]

Equations (2) and (16) prove (3), with the same beta^(84Ld) as the old
simplified theorem and no residual d^d factor. The runtime argument,
source tolerance 1/n, physical clock and endpoint continuation are
identical. Hence (1) and (4) follow without altered constants.

The gain comes from removing an unnecessary triangle inequality across
input directions. It is not evidence that analytic source rank is
dimension-free. The unavoidable-versus-avoidable status of beta^(Ld)
and the logarithmic width exponent require separate analysis.

## 6. Dependencies and internal check record

The current source dependencies are `EXPLICIT_SOURCE_CONSTANTS_ROUTE.md`,
`DEPTH_INDEPENDENT_EXPONENT.md`, `LABEL_DEPTH_RESCALING_ROUTE.md`, and
`DIMENSION_PREFACTOR_OPTIMIZATION.md`; the runtime/assembly dependencies
are `DEPTH_CONSTANT_SEPARATION.md` and
`ARCHITECTURE_CONSTANT_REFINEMENT.md`. Their earlier complete reads and
source hashes were reconciled at startup. Only Sections 2--4 above change
the mathematical proof. This candidate requires a separate reconstruction
before being marked internally checked. That reconstruction must check
the directional-source extension, complex angular frame, all-time
interface, factorial count, and every persistent dimension factor.
