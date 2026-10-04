# Two-input stability from signed-activity differences

2026-10-03. Scoped theoretical work on the canonical width-n Gaussian
two-hidden-layer tanh network. This file belongs to the continuation in
`closure_sampling_20261003`. Its input boundary is the supervisor's model,
the canonical manuscript setting, and the four assigned existing one-input
and two-input notes. No experiment, trained trajectory evaluation, other
study, or Git operation is used. Canonical-notation and conjecture-audit
instructions apply. The lemma below was frozen before exchanging routes.

## 1. An all-time deterministic comparison lemma

Let E be a finite-dimensional normed space, F:E→R^m an observation,
and V(x):R^m→E a differentiable matrix of vector fields. Consider curves

\[
 \dot x=V(x)c,\quad c=y-F(x),\qquad
 \dot{\bar x}=V(\bar x)\bar c+e,\quad
 \bar c=y-F(\bar x)+d,\qquad x(0)=\bar x(0)=x_0.
 \tag{1}
\]

All norms on R^m are Euclidean. Assume throughout the curves and the
straight segments joining their states that

\[
 \|V\|\le M,\quad \|DV\|\le L,\quad
 \|V(x)-V_0\|\le C_0S,\qquad V_0=V(x_0),
\]
\[
 F(x)=L_0(x-x_0)+N(x),\quad F(x_0)=0,\quad
 \operatorname{Lip}(N)\le C_0S,\qquad
 K_0=L_0V_0=K_0^\top\succeq\gamma I.
 \tag{2}
\]

Assume also

\[
 \int_0^\infty(|c|+|\bar c|)\,dt\le S,
 \quad\int_0^\infty\|e\|\,dt\le\epsilon,
 \quad\sup_{t\ge0}|d(t)|\le\epsilon.
 \tag{3}
\]

The constants M,L,C_0,γ and \|L_0\| are fixed. There exist S_*>0
and C depending only on these constants such that S≤S_* implies

\[
 \sup_{t\ge0}\|x(t)-\bar x(t)\|
 +\sup_{t\ge0}\left|\int_0^t(c-\bar c)\,dv\right|
 \le C\epsilon.\tag{4}
\]

This compares the curves at the same physical time. It asserts no
path-independent parameterization by accumulated activities.

**Proof.** Define q=x−\bar x and p(t)=∫_0^t(c−\bar c)dv. On [0,T]
write D=sup\|q\| and P=sup|p|. Subtract (1), integrate, and integrate
the V(x)dp term by parts. The resulting identity is exact:

\[
 q(t)=V(x(t))p(t)
 -\int_0^t DV(x(v))\dot x(v)p(v)\,dv
 +\int_0^t[V(x(v))-V(\bar x(v))]\bar c(v)\,dv
 -\int_0^t e(v)\,dv.\tag{5}
\]

Since ∫\|\dot x\|≤MS, (2)–(3) give

\[
 \sup_{t\le T}\|q(t)-V_0p(t)\|
 \le (C_0+LM)SP+LSD+\epsilon,
\]
\[
 D\le \|V_0\|P+C_1S(P+D)+\epsilon.\tag{6}
\]

The observation equation gives

\[
 \dot p=-K_0p+\zeta,\qquad
 |\zeta(t)|\le C_2S(P+D)+(1+\|L_0\|)\epsilon.
\]

The symmetric positive gap implies \|e^{-K_0t}\|≤e^{-γt}.
Variation of constants, with p(0)=0, yields

\[
 P\le\gamma^{-1}\{C_2S(P+D)+(1+\|L_0\|)\epsilon\}.
 \tag{7}
\]

First absorb the C_1SD term in (6), obtaining D≤C_3P+2ε.
Then choose S_* so the coefficient of P after substitution into (7)
is at most 1/2. This proves (4) independently of T, and taking T→∞
finishes the proof. No absolute-integrability bound on c−\bar c is
used. In particular, signed residual components and their rotations cause
no difficulty.

## 2. Verification of the structural hypotheses for orthogonal inputs

Train on x_1=√2e_1 and x_2=√2e_2, with loss
\(\mathcal L=\tfrac12\sum_{a=1}^2(f_a-y_a)^2\). Let positive diagonal
neuron masses D_1,D_2 have total mass one. With

\[
 \Psi(a)=a/2+\sinh(2a)/4,\quad u_a=\Psi(Ae_a),\quad
 \sigma=\tanh\circ\Psi^{-1},\quad h_a=\sigma(u_a),
\]
\[
 z_a=Bh_a,\quad g_a=\tanh z_a,\quad
 \delta_a=w\odot\operatorname{sech}^2z_a,\quad
 f_a=w^\top D_2g_a,\quad c_a=y_a-f_a,
\]

use the state x=(u_1,u_2,B,w), norm

\[
 \|\Delta x\|=\|\Delta u_1\|_{D_1}+\|\Delta u_2\|_{D_1}
 +\|\Delta B\|_{\rm HS}+\|\Delta w\|_{D_2},
\]

where \(B^*=D_1^{-1}B^\top D_2\) and
\(\|B\|_{\rm HS}=\|D_2^{1/2}BD_1^{-1/2}\|_F\).
The exact vector field V_a has u_a block B^*δ_a, the other u block
zero, B block δ_a h_a^T D_1, and w block g_a. Thus
\(\dot x=\sum_a c_aV_a(x)\). At w_0=0, V_{a,0} has only the
w block g_{a,0}.

For residual length \(s(t)=\int_0^t|c(v)|dv\le S\), bounded tanh
and the rank-one norm identity give

\[
 \|w\|_\infty\le\sqrt2S,\quad
 \|B-B_0\|_{\rm HS}\le CS^2,\quad
 \sum_a\|u_a-u_{a,0}\|_{D_1}\le C_KS^2.
 \tag{8}
\]

Consequently \(\|g_a-g_{a,0}\|_{D_2}\le C_KS^2\).
On the convex tube described by these inequalities, σ and its first
derivatives are bounded on the real axis. The finite-difference calculation
in the one-input weighted stability note, applied separately to each a,
gives \(\|DV_a\|\le C_K\), with no carrier-coordinate bound and no
minimum neuron mass. Also \(\|V_a-V_{a,0}\|\le C_KS\).

Define the fixed linear observation

\[
 (L_0\Delta x)_a=g_{a,0}^\top D_2\Delta w.
\]

Then \(L_0V_0=(g_{a,0}^\top D_2g_{b,0})_{a,b}\), the initial
readout Gram. The remainder is explicitly

\[
 N_a(x)=w^\top D_2(g_a-g_{a,0}).\tag{9}
\]

Its derivative in the w block has norm O(S²). Its derivatives in the
u and B blocks have norm O(S), because \|w\|_∞≤√2S and the
forward feature map is Lipschitz in the displayed normalized norms on
the operator tube. Hence \(\operatorname{Lip}(N)\le C_KS\).
This verifies every structural hypothesis of the lemma whenever the
initialized Gram has a fixed gap. No derivative of the tangent kernel,
no bound on a diagonal carrier multiplier, and no commutation of V_1,V_2
has been assumed.

The same verification applies to the canonical full model with
D_1=D_2=I/n and B=W. It also applies to unequal-width or singleton-deleted
models with normalization n: the remaining masses then sum to at most one,
which only improves these estimates.

## 3. Small-label fitting, tails, and autonomous singleton cavities

The initial Gram condition also verifies the residual-length hypothesis.
For the weighted model, direct differentiation of f gives

\[
 \dot c=-K(x)c,
\]
\[
 K_{ab}=\langle g_a,g_b\rangle_{D_2}
 +\langle\delta_a,\delta_b\rangle_{D_2}
                  \langle h_a,h_b\rangle_{D_1}
 +\mathbf1_{a=b}\|\operatorname{sech}^2(Ae_a)
                                      \odot B^*\delta_a\|_{D_1}^2.
 \tag{10}
\]

Each summand matrix is positive semidefinite. For the second, its quadratic
form is the squared Hilbert--Schmidt norm of
\(\sum_a v_a\delta_a h_a^\top D_1\); the final term is diagonal
and nonnegative. Thus K dominates the readout Gram. Equations (8) and
the bound on g−g_0 keep that Gram above γI/2 while s≤S_0, for a
fixed sufficiently small S_0. Hence, on this interval,

\[
 |c(t)|\le |y|e^{-\gamma t/2},\qquad
 s(t)\le2|y|/\gamma.\tag{11}
\]

Choose |y|≤γS_0/4. The last inequality prevents the supposed first
exit s=S_0, while (8) prevents finite-time state escape. Therefore (11)
holds globally. The state has a fitted limit, and its normalized distance
to that limit is at most C|y|e^{-γt/2}. Every real-circle query is
Lipschitz in the state on the same tube: Ψ^{-1} is 1-Lipschitz,
the two first-layer columns enter with coefficients cosθ,sinθ, and
the remaining forward maps have uniformly bounded real derivatives.
Consequently every query prediction has a tail bounded by
C|y|e^{-γt/2}, uniformly in θ. These arguments allow either sign
for each label, including a zero component.

For clarity, autonomous singleton deletion fits precisely into (1), rather
than using residual coefficients from the full network as an external
cavity control. All normalizations stay n. A lower deletion removes
column i and its two first-layer coordinates. In the retained full state,
the top preactivation differs from the cavity's forward expression by
\(e_a^z=W_{:,i}h_{a,i}\). The initialized column norm and the learned
rank-one formula imply \(\|e_a^z\|_2\le C_K\). Thus, in the normalized
state norm, the residual-free vector-field discrepancy is at most C/√n.
Its actual velocity discrepancy has integral at most CS/√n. The
prediction discrepancy at an identical retained state is at most CS/√n,
because \|w\|_∞≤CS. Applying the lemma with x equal to the autonomous
cavity and \bar x equal to the full retained path gives

\[
 \sup_{t\ge0}\|x(t)-\bar x(t)\|\le CS/\sqrt n.
 \tag{12}
\]

The cavity's initial readout Gram differs from the full one by O(n^{-1/2}),
since deletion changes each initial top feature by normalized norm
O(n^{-1/2}). Its fixed gap and its own fitting estimate (11) therefore
hold for sufficiently large n. Its initialization and its own residual
equations are independent of the omitted Gaussian column.

An upper deletion removes row j and the readout coordinate w_j. It has
no retained forward discrepancy. Its extra full lower velocity for sample
a is \(c_aW_{j,:}^\top\delta_{a,j}\), of normalized norm at most
CS|c_a|/√n. The missing prediction is w_jg_{a,j}/n, bounded by
CS/n. Hence the lemma gives the sharper bound

\[
 \sup_{t\ge0}\|x(t)-\bar x(t)\|
 \le C(S^2/\sqrt n+S/n).\tag{13}
\]

The upper cavity's initial Gram differs only by O(1/n), its own
residual equations are autonomous, and it is independent of the omitted
Gaussian row. Multiplying (12)–(13) by √n recovers the ordinary
Euclidean/Frobenius scale with the hidden block represented as H=√nW.
These are deterministic comparisons on the initialized operator-norm
event. No conditional Gaussian assertion is made about an adaptive full
carrier; Gaussian estimates can instead use the independent cavity.

## 4. A small retained source space from possibly enormous initial jets

This section is a general approximation lemma, conditional only on its
explicit complex rectangle. It does not assert that the two-input source
rectangle has already been proved.

Let a vector-valued source R(t,θ) be jointly holomorphic and bounded in
coordinate supremum by M on a neighborhood of

\[
 -r\le\Re t\le T+r,\quad |\Im t|\le r,
 \qquad |\Im\theta|\le r_\theta,
 \tag{14}
\]

where T≥r>0, 0<r_θ≤1, and R is 2π-periodic in θ. For every
0<ε≤M there is a tensor polynomial, algebraic of degree p in t and
trigonometric of degree L in θ, approximating R on [0,T]×R with
coordinate error at most Cε, where

\[
 p\le C\frac Tr\log\!\left(\frac{CM T}{\epsilon r}\right),
 \qquad
 L\le C r_\theta^{-1}
               \log\!\left(\frac{CM}{\epsilon r_\theta}\right).
 \tag{15}
\]

Every retained vector coefficient is a finite linear combination of
\(\partial_t^kR(0,\theta_\nu)\), at the deterministic angles
\(\theta_\nu=2\pi\nu/(2L+1)\), with 0≤k≤J for an explicit finite
J. The scalar coefficients depend only on T,r,r_θ,M,ε. No trained
snapshot is an input to this construction.

Here is the complete coefficient construction. Put

\[
 v=\pi T/(8r),\quad b=\tanh v,\quad
 \alpha=\tanh(v+\pi/4),\quad \eta=b/\alpha,
 \quad \psi(\xi)=\frac{\xi-\eta}{1-\eta\xi},
\]
\[
 z(\xi)=\frac T2+\frac{2r}{\pi}
           \log\frac{1+\alpha\psi(\xi)}{1-\alpha\psi(\xi)}.
 \tag{16}
\]

The logarithm is the analytic branch equal to a real number at ξ=0.
The disk automorphism ψ maps the unit disk into itself. The logarithm
maps the disk of radius α into imaginary range (−π/2,π/2),
and its real magnitude is bounded by 2 artanh α. Thus z maps the
unit disk inside (14), and z(0)=0. For t∈[0,T], let ξ(t) be
its real inverse. Explicitly, with

\[
 q(t)=\alpha^{-1}\tanh\frac{\pi(t-T/2)}{4r},\qquad
 \xi(t)=\frac{q(t)+\eta}{1+\eta q(t)},
\]

we have 0≤ξ(t)≤ξ_*:=2η/(1+η²)<1. Define d_*=1−ξ_*.
The identity

\[
 \alpha-b=\frac{\sinh(\pi/4)}{\cosh(v+\pi/4)\cosh v}
\]

shows \(d_*=(1-\eta)^2/(1+\eta^2)\ge c e^{-CT/r}\).

For every θ in the closed angular strip, form the degree-J Taylor
polynomial in ξ of R(z(ξ),θ). Its jth coefficient is explicitly

\[
 A_j(\theta)=
 \sum_{k=0}^j\frac{\partial_t^kR(0,\theta)}{k!}
                       [\xi^j]z(\xi)^k.
 \tag{17}
\]

Cauchy's formula gives \|A_j\|_∞≤M. Therefore its value
\(Q_J(t,\theta)=\sum_{j=0}^JA_j(\theta)\xi(t)^j\)
has error at most \(M e^{-d_*(J+1)}/d_*\) on the entire real
time interval, uniformly also for complex θ. Choose

\[
 J+1\ge d_*^{-1}
       \log\frac{4M(p+1)}{d_*\epsilon}.
 \tag{18}
\]

This guarantees error at most ε/[4(p+1)]. The construction uses
only initial derivatives even when J is extraordinarily large.

Now take Chebyshev--Lobatto nodes
\(t_j=T[1+\cos(j\pi/p)]/2\), 0≤j≤p, and interpolate the
*computed numbers* Q_J(t_j,θ). These numbers are evaluations of (17),
not evaluations of R at trained times. The discrete cosine transform
gives p+1 vector coefficients. Each coefficient has magnitude at most
twice the largest nodal value; consequently perturbing all nodal values
by δ changes the interpolant by at most 2(p+1)δ on [0,T].
Thus the replacement of R(t_j,θ) by Q_J(t_j,θ) costs at most ε/2.

For completeness, the exact interpolant of R has error bounded by
\(CM(T/r)e^{-cpr/T}\). To see this, use the Bernstein ellipse with
parameter exp(cr/T), for a fixed small c. Its scaled image lies inside
the rectangle (14). The Laurent coefficients after the substitution
\(t=T[1+(\zeta+\zeta^{-1})/2]/2\) are bounded by
M exp(−ckr/T). On the Lobatto grid every omitted cosine mode aliases
to a mode of degree at most p with amplitude at most one, so the
interpolation error is at most twice the geometric tail of those
coefficients. This proves the bound and the first choice in (15).

Finally apply the trigonometric interpolant on the 2L+1 angles θ_ν.
The time polynomial is analytic in θ and bounded by M+Cε on its
strip, uniformly for real t. Moving the Fourier integral to either
strip boundary bounds its kth coefficient by
(M+Cε)exp(−|k|r_θ). Aliasing on the equispaced angular grid bounds
the interpolation error by twice the Fourier tail. This proves the
second choice in (15). Both interpolation steps are fixed linear
operations, so all final coefficients have the finite initial-derivative
form asserted above.

In particular, if

\[
 T=C\log(en),\quad r,r_\theta\ge c/\sqrt{\log(en)},
 \quad M\le C\sqrt{\log(en)},\quad \epsilon=c/\sqrt n,
\]

then p=O((log n)^{5/2}), L=O((log n)^{3/2}), and the number of
retained vector coefficients is O((log n)^4). The raw initial derivative
order can be as large as exp(O((log n)^{3/2})) times a power of log n;
all those intermediate derivatives and scalar combination coefficients
are discarded after the final vectors are formed.

The construction preserves paired mixer actions exactly at the coefficient
level. Applying the same scalar linear operations to R and W_0R gives
coefficient pairs v and W_0v. Applying them to D and W_0^T D gives
d and W_0^T d. Uniform approximation of each paired source is still
needed, but no separate projection or trained-path evaluation enters.

Under the existing positive cubature construction, two source dimensions
O((log n)^4) give O((log n)^8) selected neurons in each layer and
O((log n)^16) total moving and fixed stored real coordinates. This is the
complexity consequence of the general rectangle hypothesis (14); the
two-input source theorem and full construction are linked below.
Exact-real setup work and numerical conditioning are
unbounded under the inherited contract; counting them would require a
different resource theorem.

## 5. Current status

Proved here are the deterministic all-time stability lemma, its real
weighted-network hypotheses, small-label fitting and query tails,
autonomous singleton deletion comparisons, and the finite initial-jet to
small retained polynomial-space map. `TWO_INPUT_COMPLEX_SOURCE.md` now
supplies the high-probability physical-time complex rectangle (14) for
the actual two-input sources. `TWO_INPUT_CANONICAL_COMPRESSION.md`
supplies the paired cubature defects and complete reduced-model theorem.
The complete chain was reconstructed in `TWO_INPUT_COMPLEX_SOURCE_CHECK.md`
and `TWO_INPUT_CANONICAL_COMPRESSION_CHECK.md`. These are internal
collaborative checks, not independent promotion reviews or established
book material. The restriction 0<ε≤M above resolves the general
approximation lemma's minor logarithm-domain defect identified in checking;
the requested ε proportional to n^{-1/2} was already in that range.
