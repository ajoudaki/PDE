# Scoped audit of the bounded-moment tree construction

2026-09-27. Scope: `TRUE_AGGREGATE_CONSTRUCTIVE.md`, the stipulated block model,
and this route's own `TRUE_AGGREGATE_GAUSSIAN.md`. No other study, experiments,
or implementation was inspected. This is an internal scoped audit, not a
promotion review.

**Verdict:** one bounded-mark, fixed-finite-query hierarchy converges on every
finite horizon after the clock normalization in section 11 of the construction.
The normalized tree hierarchy and its bounded
closure give a substantive aggregate construction, not a renamed joint-law
grid. Its current proof does not give a useful polynomial accuracy cost for
the Gaussian population. Full-circle decoding and efficient initialization
also remain separate obligations. These conclusions do not establish an
impossibility theorem for a better aggregate closure.

## 1. Polynomial lift and tree normalization

The gate lift is exact. In particular the second gate derivative includes
both the derivative of 1/L and the global derivative

\[
\dot S_{j,a}=\mathbb E[k^{-1}(\dot B_j^Tx_a+B_j^T\dot x_a)].
\]

Omitting the second summand, or treating S as fixed during the local chain
rule, would change the dynamics. The draft retains both summands. The
square-root residual norm is used only as a Lipschitz coefficient, with no
division by or differentiation of that norm.

The degree counts 8 for dot x, 9 for the integrands of dot S, and 11 for dot h
are valid. For example the largest term in dot h contains root h^2, one
forward G edge, four x factors at the new first vertex, one transpose G edge,
and three c/h factors at the new second vertex. The sum is eleven. Thus
replacing a differentiated decoration raises total degree by at most ten.

For a tree with V formal vertices, the normalization k^(-V) is correct.
Consider just the normalized single-vertex mean of x. Its matrix-action term
contains

\[
\frac1k\sum_{i,\alpha}G_{\alpha i}d_\alpha P_i
 =kR_G^*\left[\frac1{k^2}\sum_{i,\alpha}
       \widetilde G_{\alpha i}d_\alpha P_i\right],
\]

where R_G^*=max(1,R_G), normalized G is G/R_G^*, and any other coordinate
normalizations are understood. The new normalized edge statistic therefore
carries coefficient kR_G^*. Two appended vertices give k^2 and two G factors
give (R_G^*)^2. This verifies the draft's warning that its absolute coefficient
bound contains kR_G and (kR_G)^2 scales; Gaussian cancellation has not been
assumed.

Formal vertices have unrestricted labels. Two distinct formal vertices may
receive the same numerical index. Thus the sum already includes diagonal
collisions and repeated uses of a matrix entry. Grafting introduces a new
formal vertex, not a new independent random variable. It preserves actual
G/G-transpose reuse and does not silently discard the order-one response
identified in the Gaussian-route note.

Differentiating a vertex decoration only grafts a finite rooted tree. The
global moments remain scalar coefficients. It never identifies two existing
formal vertices, so a connected tree remains a connected tree. The advertised
exponential-in-degree count of decorated plane trees is a valid conservative
bound, independent of k. Constants in the vector field are not independent
of k.

## 2. The saturation penalty supplies the needed uniform bound

Let pi project one scalar to [-1,1]. For a true moment q in this interval,

\[
\operatorname{sgn}(\widehat q-q)
                  (\widehat q-\pi(\widehat q))\ge0.
\]

Consequently the negative penalty contributes a nonpositive term to the
upper derivative of the absolute error. It also makes [-2,2] invariant when
its coefficient is the absolute RHS bound a times degree. The clipping of
children and coefficient moments is Lipschitz. Together with 0<ghat<=1,
this establishes global existence of the finite surrogate, even though its
coordinates need not be realizable moments of a probability law.

The absence of moment realizability is not an error: the claimed observables
are compared directly through the hierarchy. Realizability is not used to
bound the approximate high degrees; the explicit penalty provides that bound.

## 3. The finite-propagation argument checks out

Let E_d denote the maximal error through degree d, including the g error at
low degrees. With s=9 and r=10 the comparison has the stated form

\[
E_d(t)\le E_d(t_0)+ad\int_{t_0}^t E_{d+r}(v)\,dv
                       +bd\int_{t_0}^t E_s(v)\,dv.
\]

The omitted true children are bounded by one; the retained errors are bounded
by three. This is an explicit boundary source. It need not tend to zero in
an unweighted norm of the entire retained state.

Repeated substitution of the high-degree term produces exactly

\[
\frac{(at)^j}{j!}\prod_{\ell=0}^{j-1}(d+\ell r).
\]

For ar tau<=1/8 its sum is (1-ar tau)^(-d/r). The coefficient kernel on the
low-degree error is bounded by

\[
bd(1-ar\tau)^{-d/r-1}.
\]

To verify the boundary bound, put n=floor((M-d)/r) and h=ceil(d/r). The
coefficient at the first unestimated degree is at most

\[
8^{-(n+1)}{h+n\choose n+1}
 \le 8^{-(n+1)}2^{h+n}.
\]

For d<=M/4, this is bounded by C exp(-cM) with c independent of M,d.
Gronwall applied first at d=s gives the draft's slab estimate. Inserting it
into the other degrees gives C_1 exp(C_2 d) times the sum of the initial
error and the exponentially small boundary influence.

For completeness, the multi-slab induction can be stated without changing
the ODE. Set M_j=alpha^jD, neglecting integer floors. Suppose the error after
slab j-1 through degree M_(j-1) is at most

\[
C_{j-1}\exp[-\beta M_{j-2}],\qquad \beta=c_2/2.
\]

Apply the slab estimate with M=M_(j-1), d<=alpha M. Its two exponential
terms have exponents

\[
C_2\alpha M-\beta M/\alpha,
\qquad C_2\alpha M-c_2M.
\]

With alpha<=min(1/4,c_2/(4C_2)), both are at most -beta M. The constants
multiply over finitely many slabs. This proves the low-degree bound with
an exponent proportional to alpha^(J-1), including the supremum inside each
slab. The induction only reduces the range of degrees for which an error
estimate is available. It does not reset the numerical state, insert exact
moments, or obtain missing higher moments at a restart.

This argument also explains why a generic demand that the full retained-state
residual tend to zero would be too strong. A bounded error source far out in
degree can have vanishing influence on fixed low-degree observables.

## 4. Gaussian cutoff and the actual accuracy exponent

Write B for the exponential tree-count base, and retain the explicit proven
choices

\[
N_D\le B^{D+1},\qquad
\operatorname{error}\le C_J e^{-c_JD},\qquad
c_J=c_*\alpha^{J-1},\qquad
J\simeq 8arT.
\]

At a fixed cutoff, the certified accuracy exponent is

\[
p(R_G)=\frac{\log B}{c_J(R_G)}
\]

in a state-count bound of the form N<=A(R_G) epsilon^(-p(R_G)). This is
polynomial in 1/epsilon only while the cutoff is held fixed. For the explicit
choice above, alpha<=1/4 already makes 1/c_J grow at least geometrically in
the number of slabs. The two-edge terms in the present coefficient majorant
make a grow with (kR_G^*)^2. Enlarging the cutoff therefore degrades the
certified exponent.

Even under an optimistic, separately verified Gaussian tail-stability bound
requiring only R_G^2=O(log(1/epsilon)/k), a schematic quadratic coefficient
bound a=O(k^2R_G^2) gives J=O(kT log(1/epsilon)). With alpha bounded below by
a positive constant, the displayed proof can then require a degree of the
form epsilon^(-c) log(1/epsilon), rather than O(log(1/epsilon)). Exponential
tree count at that degree gives a superpolynomial guarantee. If alpha or C_J
also worsen with the cutoff, the current guarantee can be worse still.
These are consequences of the supplied sufficient bound, not lower bounds
on the actual approximation error or on every possible closure.

The general bookkeeping criterion is useful. If a bounded-law theorem gives

\[
N(\delta,R)\le A(R)\delta^{-p(R)},
\]

and cutoff removal asks for R=R_epsilon and delta comparable to epsilon,
then a polynomial certificate from this bound requires

\[
\sup_{\epsilon\downarrow0}
\frac{\log A(R_\epsilon)
      +p(R_\epsilon)\log(1/\epsilon)}{\log(1/\epsilon)}<\infty.
\]

The draft has not established this condition. A statement that Gaussian tail
mass tends to zero cannot replace it. Moreover, tail mass alone does not
bound the dynamics error: changing the law changes the shared population
fields and hence the motion of every retained block. A separate stability
argument for Gaussian cutoff removal is still necessary.

## 5. Horizon, initialization, and query scope

The initial argument normalized using a prescribed T. Section 11 of the
construction now supersedes that restriction with an explicit clock-based
normalization, audited in section 6 below. The resulting ODE and initial
moments do not depend on T; its accuracy constants still do. Restart remains
from the saved finite state alone.

The final revised Legendre bounds also check directly. The history formulas
use polynomials bounded by one on their argument interval. Therefore
|c|<=2(L-1), |B_j|<=L, and
|A_{j,a}|<=integral 2sqrt(m)rho(s)(L(s)-1) ds
=sqrt(m)(L-1)^2. From rho<=2(L-1)+Y, scalar comparison gives
L-1<=Y(exp(2t)-1)/2. This removes artificial exponential dependence on H
from the local coordinate normalization, while retaining its dependence
on the design horizon and the G-dependent coefficient bounds.

The corrected initialization discussion is sound. At any fixed seed, a tree
contraction with unrestricted labels can be evaluated by leaf-to-root messages.
For a vertex v with parent p, the message is

\[
m_{v\to p}(i_p)=\frac1k\sum_{i_v}
 \widetilde G_{i_p i_v}\Phi_v(i_v)
        \prod_{w\text{ child of }v}m_{w\to v}(i_v),
\]

with edge orientation chosen according to the two populations. The root
contraction is its normalized sum without a parent edge. This is exactly
the original unrestricted-label sum, including collisions. It takes
O(k^2(D+1)) arithmetic operations per tree after the local gate tables have
been formed. Coincident-label partitions are unnecessary for that fixed-seed
evaluation. Integrating this result over k^2+2k Gaussian seed coordinates is
a different problem; the draft does not yet give an efficient general method.

A fixed finite query list is also a real restriction. Adding a passive query
after training requires the mixed passive/training moments that would have
evolved during training. They cannot in general be recovered from the saved
training-only low moments. Running a separate passive closure from time zero
for each chosen query is a finite-query solution, not a demonstrated universal
decoder from one saved scalar state. The proposed Fourier query construction
is a concrete possible extension, but the draft correctly leaves its coupled
degree/Fourier error estimate unproved.

## 6. Final extension: normalization by the clock

The section 11 formulas have been checked directly. Write

\[
\zeta=cg/2,\qquad \alpha_j=A_jg^2/\sqrt m,
\qquad \beta_j=B_jg,\qquad g=1/L.
\]

The history bounds verified above give |zeta|<=1-g,
|alpha_j|<=(1-g)^2, and |beta_j|<=1 at all times. Put

\[
F_b=\mathbb E[k^{-1}\zeta^Th_b],\qquad
R_b=2F_b-gy_b=gr_b,\qquad
\sigma=\left(m^{-1}\sum_bR_b^2\right)^{1/2}=g\rho.
\]

Differentiating these rescaled local coordinates gives

\[
\begin{aligned}
g'&=-\sigma g,\\
\zeta'&=-m^{-1}\sum_bR_bh_b-\sigma\zeta,\\
\alpha_{j,b}'&=(2/\sqrt m)R_b\zeta\odot(1-h_b^2)
 -\sigma[(j+2)\alpha_{j,b}+\sum_{i<j}(2i+1)\alpha_{i,b}],\\
\beta_{j,b}'&=\sigma[x_b-(j+1)\beta_{j,b}
                         -\sum_{i<j}(2i+1)\beta_{i,b}].
\end{aligned}
\]

The extra two and one in the memory decay coefficients are exactly the
derivatives of g^2 and g. With
s_j=E[beta_j^T x/k] and t_j=E[alpha_j^T(zeta odot(1-h^2))/k], the original
shared fields become S_j=s_j/g and V_j=2sqrt(m)t_j/g^3. Therefore the first
gate equation has the stated g^(-2) forward coefficient and g^(-4) memory
coefficient. The second preactivation is

\[
z_{2,a}=Gx_a-\frac{2}{\sqrt m g^2}
                     \sum_j(2j+1)\alpha_js_{j,a}.
\]

Differentiating 2/(sqrt(m)g^2) contributes the stated positive 2sigma factor
inside the negative memory bracket in dot h. The largest resulting inverse
clock power is g^(-6), from the g^(-2) factor times the g^(-4) term in dot s.
No new local variable or moment type is introduced. The degrees 8,9,11 and
the degree increment r=10 remain valid.

The coefficient envelope a(g)=C(1+g^(-6)) consequently bounds the absolute
row sum in the normalized hierarchy. Its Lipschitz comparison bound on
g>=g_0 can use C'(1+g_0^(-7)); differentiating the inverse clock powers costs
at most one additional inverse power. These constants may depend on k,m,H,
query count, label bound and the matrix cutoff, but not on D or a design T.

For the clipped surrogate, |F_b|<=1, so sigma<=2+Y whenever 0<ghat<=1.
Hence

\[
e^{-(2+Y)t}\le\widehat g(t)\le1.
\]

Use a(ghat) times degree as the outward penalty coefficient. At either
moment-box face its negative term still dominates the clipped RHS. In the
error inequality its contribution is still nonpositive: the exact moment
lies in [-1,1], regardless of the positive value of a(ghat). There is no
extra penalty-coefficient error to estimate. The clock lower bound prevents
any finite-time coefficient singularity. Thus the same finite ODE is globally
well posed, and the previous finite-propagation proof applies on each [0,T]
with constants evaluated at g_0=exp[-(2+Y)T]. This proves the claimed single
hierarchy with compact-horizon convergence.

Finally f_a=2F_a/g. Since both clocks have the same positive lower bound,

\[
|f_a-\widehat f_a|
\le2e^{(2+Y)T}|F_a-\pi(\widehat F_a)|
       +2e^{2(2+Y)T}|g-\widehat g|.
\]

Thus the output decoder preserves exponential degree convergence on every
fixed finite horizon. This lemma repairs the horizon-dependent family issue;
it leaves the matrix-cutoff dependence of the accuracy exponent intact.

The final finite-precision initialization refinement also checks. Over J
slabs, an initial coordinate error eta_D is amplified by at most

\[
C_1(T)^J\exp\left[C_2D\sum_{j=1}^J\alpha^j\right]\eta_D
 \le C_T\exp[(c_2/3)D]\eta_D.
\]

Indeed C_2 alpha<=c_2/4 and alpha<=1/4 imply
C_2 alpha/(1-alpha)<=c_2/3. With the universal c_2=log(2)/(2r) and r=10,
the fixed schedule eta_D=exp(-D) therefore gives an exponentially decaying
initialization contribution for every fixed T. The initializer, as well as
the ODE, can be chosen without a design horizon. This is an accuracy schedule,
not a polynomial-work guarantee for computing all those initial moments.

The final finite-query corollary also checks: w is absent after the initial
gates are formed, so w(0) need not be truncated in the target. For bounded G,
the local gates and normalized states remain bounded with fully Gaussian w(0).
Numerically cutting off w only for the initial expectation integrals creates
an initial moment error at most twice the omitted probability mass. The
remaining Gaussian evolution question is therefore the unbounded G, not
the first-weight tail. This does not supply a full-circle saved-state decoder.

## Final claim calibration

- The bounded-support construction is a valid substantive route to finite
  aggregate statistics, with autonomous feature learning and actual matrix
  reuse.
- Its degree proof controls a distant bounded boundary source, rather than
  assuming an unjustified small full-state residual.
- One unchanged finite-query hierarchy now works on every finite horizon.
  Its polynomial accuracy-versus-state-count bound still has a fixed matrix
  cutoff and an exponent depending on that cutoff and the assessed horizon.
- Useful Gaussian complexity, efficient initialization, and a common saved
  state decoding all circle queries remain open.

No additional experiment is needed to establish these scope limits; they are
visible in the formulas and quantifiers of the construction.
