# Smooth clipping: contraction of the prescribed-history Gaussian response map

2026-10-01. Scoped theoretical route. Scientific input: `SMOOTH_SETUP.md` and
the supervisor's prescribed two-population map. No other study, sibling
report, manuscript passage, experiment, or external theorem is an input.

**Conclusion.** The deterministic response map has a unique small-activity
fixed point in the domain specified below. The proof uses absolute sums of
history-coordinate derivatives through order three, not a history Gram
inverse. Singular covariance matrices are allowed. The upper response's
instantaneous atom is essential and is retained. The claim concerns the
prescribed-history map only: it does not identify finite-width populations,
prove a cavity estimate, or restore the random training residuals.

There is one regularity qualification. The phrase “appropriate finite-activity
variation” is made precise here as Lipschitz variation in the activity clock
for the supplied functions K and V. If only arbitrary bounded variation was
intended, the continuous-path domain below does not cover that larger class;
a domain allowing their jumps would be needed. This is an explicit assumption,
not a consequence of amplitude bounds alone.

## 1. The map and its domain

Write

\[
s(t)=\int_0^t\rho(u)\,du,\qquad S=s(\infty),\qquad
\lambda_a(s(t))=r_a(t)/\rho(t)
\]

at positive activity; the quotient is assigned zero where rho is zero.
Because the states and the prescribed coefficients are constant on a
zero-activity interval, the dynamics descend to x=s(t) in [0,S]. In this
note primes denote derivatives with respect to x, not physical-time dots.
Assume 0<S<=1, |lambda_a|<=sqrt(m), and lambda is measurable. Constants below
may depend on m,d,M, the inputs u_a, and fixed coefficient regularity bounds,
but not on S, a time mesh, or any covariance eigenvalue.

Put psi(z)=sech^2(z), and

\[
F(\alpha,p)=M\tanh\bigl(p\psi(\alpha)/M\bigr).
\]

The supplied K,V are deterministic and satisfy, for a fixed L,

\[
|K_{ba}(x)|\le1,\quad |V_{ba}(x)|\le Lx^3,\qquad
|K_{ba}(x)-K_{ba}(y)|+|V_{ba}(x)-V_{ba}(y)|\le L|x-y|.
\tag{1}
\]

Use the response decomposition

\[
\begin{aligned}
(R_h d)_a(x)&=\sum_b\int_0^x Q_{h,ab}(x,u)d_b(u)\,du,\\
(R_d h)_a(x)&=D_a(x)h_a(x)+
  \sum_b\int_0^x Q_{d,ab}(x,u)h_b(u)\,du.
\end{aligned}\tag{2}
\]

Thus R_d includes diag(D(x)) delta_x. This atom is not absorbed into a
Lebesgue density, and R_h has no atom.

For input laws H=(C_h,Q_h) and Dlaw=(C_d,D,Q_d), take centered Gaussian
histories gamma and xi with covariance C_h and C_d. The lower representative
also has a0~N(0,I_d), independent of xi. Upper and lower representatives are
on separate probability spaces. Their equations are

\[
\begin{aligned}
h_a&=\tanh(a\cdot u_a),&
p_a&=\xi_a+D_a h_a+\sum_b\int_0^xQ_{d,ab}(x,u)h_b(u)\,du
       +m^{-1}\sum_b k_bV_{ba},\\
a'&=-\frac2m\sum_b\lambda_b F(a\cdot u_b,p_b)u_b,&
k_a'&=\frac{h_a-k_a}{1+x},\\[1mm]
z_a&=\gamma_a+\sum_b\int_0^xQ_{h,ab}(x,u)d_b(u)\,du
        +m^{-1}\sum_bv_bK_{ba},&
d_a&=c_M(w\psi(z_a)),\\
w'&=-\frac2m\sum_b\lambda_b\tanh z_b,&
v_a'&=-2\lambda_a d_a.
\end{aligned}\tag{3}
\]

Here a(0)=a0, k_a(0)=tanh(a0.u_a), and w(0)=v(0)=0. All input law kernels,
lambda,K,V are held fixed when taking a single-representative derivative.
Recompute

\[
\begin{aligned}
C_h^{\rm out}(x,y)&=\mathbb E[h(x)h(y)^\top],&
R_h^{\rm out}&=\mathbb E D_\xi h,\\
C_d^{\rm out}(x,y)&=\mathbb E[d(x)d(y)^\top],&
R_d^{\rm out}&=\mathbb E D_\gamma d.
\end{aligned}\tag{4}
\]

The map is bipartite: Hout=L(Dlaw), Dlaw-out=U(H). This law-tuple notation
distinguishes the upper law from its scalar atom D_a.

For a causal matrix kernel Q, extended by zero to u>x, set

\[
\|Q\|_{\rm row}=\sup_x\max_a\sum_b\int_0^S|Q_{ab}(x,u)|\,du.
\]

Covariance norms are the maximum absolute entry over both times. Atom norms
are max_a sup_x |D_a(x)|. The two distances are

\[
\begin{aligned}
d_H(H,\widetilde H)
 &=\|C_h-\widetilde C_h\|_\infty
   +S^{-1}\|Q_h-\widetilde Q_h\|_{\rm row},\\
d_D(Dlaw,\widetilde{Dlaw})
 &=S^{-2}\|C_d-\widetilde C_d\|_\infty
   +S^{-1}\bigl(\|D-\widetilde D\|_\infty
        +\|Q_d-\widetilde Q_d\|_{\rm row}\bigr).
\end{aligned}\tag{5}
\]

The covariance kernels are symmetric positive semidefinite on every finite
set of time/sample indices. With constants L_h,B_h,L_d,B_d chosen below,
the domain is:

* H: C_h,aa(x,x)<=1, with no prescribed initial covariance; and
  C_h,aa(x,x)+C_h,aa(y,y)-2C_h,aa(x,y)<=L_h^2|x-y|^2.
  Each Q_h entry is bounded by B_h, is causal, and its zero-extended row is
  Lipschitz as an L1 function of the source time, with constant B_h.
* Dlaw: C_d,aa(x,x)<=L_d^2 x^2 and the same mean-square increment bound
  with L_d in place of L_h; D(0)=0 and D is Lipschitz with constant B_d;
  Q_d has the preceding causal density and L1-row bounds with B_d.

The bounds on rows use the displayed matrix row norm, with harmless fixed
m factors incorporated in B_h,B_d. Kernel functions are identified almost
everywhere in their source coordinate. A kernel is a continuous map from
[0,S] into that L1 space. These domains are convex and complete in (5): a
uniform covariance limit preserves positive semidefiniteness and all
increment inequalities; a uniform L1-row limit preserves causality,
Lipschitz continuity and the essential density bound. Atom limits preserve
their separate Lipschitz condition. Treating D(x)delta_x as an ordinary
Lipschitz row in total variation would be incorrect because atoms at
different times have disjoint support.

The lower output always has initial covariance
C0_ab=E[tanh(a0.u_a)tanh(a0.u_b)], so the fixed point has C_h(0,0)=C0.
Leaving this value unrestricted in the input domain permits comparison
with a positive semidefinite empirical initial covariance. There is no
assumption that such an empirical covariance equals C0 exactly.

## 2. Elementary uniform bounds and local well-posedness

All derivatives of F of any fixed order are bounded on R^2. To see the
point relevant here, put q=p psi(alpha)/M. Alpha derivatives produce
bounded logarithmic derivatives of psi multiplied by powers of q;
derivatives of tanh of positive order decay exponentially as |q| grows.
P derivatives supply factors psi/M. Thus every term is bounded, including
mixed derivatives through order three and the fourth-order terms if an
additional observable requires them. In particular, large realized xi
values do not destroy the drift derivative bounds.

The equations give the deterministic bounds

\[
|h_a|,|k_a|\le1,\qquad
|w(x)|\le c x,\quad |d_a(x)|\le |w(x)|\le cx,
\quad |v_a(x)|\le cx^2,
\tag{6}
\]

where c depends on m. Lower a and k have bounded activity velocities.
These bounds hold pathwise and do not require bounded Gaussian histories.

The covariance increment condition supplies continuous Gaussian versions.
One can first construct the Gaussian process on a countable dense time
set: give formal vectors e_(a,x) inner products C_ab(x,y), quotient its
null space, complete it, and apply independent standard Gaussians to an
orthonormal basis. The series defining each coordinate converges in L2.
This construction works when the covariance is singular. On a dyadic grid
the fourth moment of an increment of
mesh length delta is at most c delta^4. The expected largest increment at
level j is at most the fourth root of the sum of 2^j such fourth moments,
and is therefore at most cS 2^(-3j/4). This is summable. The dyadic process
extends uniformly almost surely, and its values agree in L2 with the
prescribed process at all times. The same argument gives finite moments
of the supremum and convergence of sampled step histories to the continuous
history in every fixed finite Lp norm. Higher Gaussian moments can be used
in the same calculation if needed.

For continuous xi, the lower equations are ordinary integral equations
with a Lipschitz state drift and a bounded causal memory kernel. Their
successive differences obey a Volterra integral bound and hence a bound
of the form c^j S^j/j!. This proves uniform convergence of Picard iterates
and uniqueness. Measurable lambda is allowed because it appears in the
integrated drift.

For the upper system, eliminate v in the equation for z:

\[
z_a(x)=\gamma_a(x)+\sum_b\int_0^x
\left[Q_{h,ab}(x,u)-\frac2m K_{ba}(x)\lambda_b(u)\right]d_b(u)\,du.
\tag{7}
\]

Together with the integral equation for w, this is again a Volterra
equation. On the slab |w|<=cS its integrands have bounded first derivatives.
The Picard map always respects this slab because tanh is bounded; its
successive differences have the same factorial bound. It gives a unique
continuous z and absolutely continuous w,v. This argument includes
singular Gaussian laws and uses no covariance factorization inverse.

## 3. Finite-mesh derivative sums

Take 0=x0<...<xN=S, with mesh steps Delta_i. Average lambda over each cell.
Use explicit Euler for the four differential equations and cell-integrated
response weights

\[
\mathsf Q_{ij}=\int_{x_j}^{x_{j+1}}Q(x_i,u)\,du,\qquad j<i.
\tag{8}
\]

The current lower field includes D(x_i)h_i; the current upper field contains
no current Q_h weight. Thus h_i depends only on xi_j with j<i, while d_i
depends on gamma_i as well as its past. Restrict to mesh steps <=1 so the
Euler k update is a convex combination. Constants below are uniform in
N and the step sizes.

For a vector observable X of its complete Gaussian history, define

\[
J_q(X)=\sum_{i_1,\ldots,i_q}\sum_{b_1,\ldots,b_q}
\left|\partial_{i_1b_1}\cdots\partial_{i_qb_q}X\right|,
\qquad q=1,2,3,
\tag{9}
\]

using the sum of absolute values in the finite output dimension. Supremum
over the realized history is understood in the following estimates. A
derivative with respect to a zero-variance coordinate is the derivative of
the defining smooth function on the ambient coordinate space; its Gaussian
law need not give that coordinate positive variance.

The estimates needed for covariance interpolation are

\[
\begin{array}{c|ccc}
 &q=1&q=2&q=3\\ \hline
h_i,k_i,a_i &cS&cS&cS\\
w_i,d_i &cS&cS&cS\\
v_i &cS^2&cS^2&cS^2
\end{array}
\tag{10}
\]

The initial a_i,k_i dependence on a0 is not included in these history
derivatives. All constants are uniform in a0.

Here are the derivative recurrences establishing (10). For a composition
f(Y), the absolute tensor sums of orders one, two and three are bounded by

\[
A_1J_1(Y),\qquad
A_1J_2(Y)+A_2J_1(Y)^2,\qquad
A_1J_3(Y)+3A_2J_1(Y)J_2(Y)+A_3J_1(Y)^3,
\tag{11}
\]

where A_j bounds the coordinate sums of the jth derivatives of f in its
fixed-dimensional state variables. Formula (11) follows by differentiating
once, twice and three times and summing absolute values; the three middle
terms at order three are the three choices of the paired derivative.

For the lower system, let J_q be the largest state sum up to node i. The
field sums satisfy

\[
\begin{aligned}
J_1(p_i)&\le m+cS J_1,\\
J_2(p_i)&\le cS(J_2+J_1^2),\\
J_3(p_i)&\le cS(J_3+J_1J_2+J_1^3).
\end{aligned}\tag{12}
\]

Indeed the only history coordinate entering p directly is xi_i; the
remaining terms have total coefficient mass O(S), or O(S^3) for V. The
state drift derivatives are globally bounded by the preceding F bound.
While all three state sums are at most one, (11)-(12) bound their Euler
increments by c Delta_i. Induction therefore keeps all three sums below
cS<1 for sufficiently small S. This proves the first line of (10) without
any dependence on the number of source coordinates.

For the upper system, z is linear in gamma,d,v. With maxima over preceding
nodes, its order-q sum obeys

\[
J_q(z)\le m\mathbf 1_{q=1}+cS J_q(d),
\qquad J_q(v)\le cS J_q(d).
\tag{13}
\]

The refined composition bound for the top clip is essential. For
f(w,z)=c_M(w psi(z)), every pure-z derivative of positive order vanishes
at w=0. Mixed w,z derivatives of each fixed order are bounded uniformly
for |w|<=c and all real z, since psi and its derivatives are bounded and
the w range is bounded. The mean-value formula in w therefore gives
|partial_z^k f(w,z)|<=c_k|w|<=c_k S for k=1,2,3. A derivative involving
at least one w differentiation only needs an O(1) bound. A generic O(1)
bound for all pure-z derivatives would lose the required factor S.

For q=1, integration of w' and differentiation of d=c_M(w psi(z)) give

\[
J_1(w)\le cS J_1(z),\qquad
J_1(d)\le cJ_1(w)+cS J_1(z).
\]

Consequently J_1(d)<=cS+cS^2J_1(d), which closes for small S. Inductively
at q=2,3, all lower-order terms in the derivative of d contain either w
or a positive-order derivative of w, and are therefore O(S). Equations
(11) and (13) give

\[
J_q(w)\le cS(1+S J_q(d)),\qquad
J_q(d)\le c[J_q(w)+S J_q(z)+S].
\]

Again J_q(d)<=cS+cS^2J_q(d); then J_q(w)<=cS and J_q(v)<=cS^2.
This proves all remaining entries of (10).

The same recurrences with one fixed past source j instead of summing it
give the sharper first-derivative estimates

\[
|\partial_{\xi_{jb}}h_i|\le c\Delta_j\quad(j<i),
\qquad
|\partial_{\gamma_{jb}}d_i|\le c\Delta_j\quad(j<i).
\tag{14}
\]

For the upper estimate, the source first enters w with weight Delta_j,
v with weight O(S Delta_j), or the field through a response weight
O(Delta_j) multiplied by an O(S) instantaneous derivative of d_j. Its
propagation is bounded by the same causal recurrences. The current
derivative is exactly

\[
\partial_{\gamma_{ib}}d_{ia}
 =\delta_{ab}\,c'_M(w_i\psi(z_{ia}))w_i\psi'(z_{ia}).
\tag{15}
\]

Equation (15), of size O(S), is the atom that cannot be dropped.

## 4. Covariance interpolation with singular covariances

For two finite-dimensional centered Gaussian covariances Gamma_0,Gamma_1
and a C2 scalar function f, first add epsilon I to both covariances. Along
Gamma_theta=(1-theta)Gamma_0+theta Gamma_1+epsilon I, differentiating the
Gaussian density gives

\[
\frac d{d\theta}\mathbb E f(X_\theta)
 =\frac12\sum_{ij}(\Gamma_1-\Gamma_0)_{ij}
       \mathbb E[\partial_{ij}f(X_\theta)].
\tag{16}
\]

The density derivative equals one half the indicated constant-coefficient
second spatial derivative of that density; two integrations by parts give
(16). Integrating theta and then letting epsilon decrease to zero is
legitimate for bounded f and bounded derivatives, by coupling each
epsilon-regularized Gaussian to its unregularized version plus independent
sqrt(epsilon) noise. It follows that

\[
|\mathbb E f(X_1)-\mathbb E f(X_0)|
\le\tfrac12\|\Gamma_1-\Gamma_0\|_{\max}
     \sup_\theta\mathbb E\sum_{ij}|\partial_{ij}f(X_\theta)|.
\tag{17}
\]

No eigenvalue appears in this bound. Apply (17) also to every first
derivative of an observable and sum over its response index; the needed
quantity is then its absolute third-derivative sum. This is why (10),
rather than a bounded derivative in a normalized L2 operator norm, is the
relevant statement.

In particular, (10) and the product rule give

\[
J_2(h_i h_j^\top)\le cS,\qquad
J_2(d_i d_j^\top)\le cS^2.
\tag{18}
\]

For lower representatives these bounds hold conditionally on a0, so one
can subsequently average a0. For upper responses use J_3(d)<=cS. For
lower responses use J_3(h)<=cS. Absolute sums of expected first-derivative
differences are bounded before passing to response-density notation.

## 5. Perturbing deterministic response inputs

Use a line segment between two response inputs, leaving the Gaussian
history fixed. Set

\[
e=\|D-\widetilde D\|_\infty+
          \|Q_d-\widetilde Q_d\|_{\rm row},\qquad
\eta=\|Q_h-\widetilde Q_h\|_{\rm row}.
\]

Differentiate the mesh recursions in the line parameter theta. For the
lower system the forcing in p_theta has size at most ce, and its propagated
state contribution is O(S e). A further history derivative has total
forcing O(e): its terms are a bounded second derivative of the drift
times the theta variation and the first history variation, or a changed
response coefficient applied to that history variation. Summing their
absolute values and integrating the Euler increments proves

\[
|h_\theta|+J_1(h_\theta)\le cS e.
\tag{19}
\]

For the upper system the direct forcing in z_theta is at most cS eta,
because it is delta Q_h applied to d. Its first-history-derivative sum has
the same bound because J_1(d)<=cS. The equations for w_theta,v_theta and
d_theta then give, successively,

\[
|z_\theta|+J_1(z_\theta)\le cS\eta,
\qquad
|d_\theta|+J_1(d_\theta)\le cS^2\eta.
\tag{20}
\]

To check closure in (20), its right-hand side before absorption also has
cS times the d_theta norm in the z equation, and cS times the z_theta norm
in the d equation. Their product is cS^2. Equations (19)-(20) are uniform
in the histories and the mesh. The covariance variation in d d^top is
therefore at most cS^3 eta.

Combining (17)-(20), first changing covariance and then response inputs,
gives the finite-mesh bounds

\[
\begin{aligned}
\|\delta C_h^{\rm out}\|_\infty+
 \|\delta R_h^{\rm out}\|_{\rm row}
 &\le cS\bigl(\|\delta C_d\|_\infty+e\bigr),\\
S^{-2}\|\delta C_d^{\rm out}\|_\infty+
 S^{-1}\|\delta R_d^{\rm out}\|_{\rm row+atom}
 &\le c\|\delta C_h\|_\infty+cS\eta.
\end{aligned}\tag{21}
\]

For discrete responses, row+atom is exactly the sum of absolute response
weights, with the current weight separated as in (15). Thus (21) controls
the desired kernel norm, not merely tests against one history direction.

## 6. Continuum responses and invariant regularity

The limiting response densities can also be constructed directly. In the
lower system, a source perturbation in xi_b at u enters the a equation
with density

\[
-\frac2m\lambda_b(u)F_p(a(u)\cdot u_b,p_b(u))u_b.
\tag{22}
\]

For x>u its propagation solves the differentiated state equation, including
the current D(x)h(x) term and the Q_d memory. Its coefficients are bounded,
so the propagated state response is bounded uniformly, and its x
derivative is bounded uniformly. Applying the derivative of tanh gives
a pathwise h-response density of size c and an expected Q_h-out whose
zero-extended row is Lipschitz in L1. The changing interval u<x contributes
at most c|x-y|. There is no current atom because h is a state variable.
Also h has a deterministic Lipschitz constant, so C_h-out has the required
mean-square Lipschitz bound.

For the upper system define its pathwise instantaneous coefficient

\[
A_a(x)=c'_M(w(x)\psi(z_a(x)))w(x)\psi'(z_a(x)),
\qquad
B_a(x)=c'_M(w(x)\psi(z_a(x)))\psi(z_a(x)).
\]

For u<x let W_b(x,u), V_ab(x,u), Z_ab(x,u), and T_ab(x,u) denote the
regular response densities of w,v_a,z_a,d_a to gamma_b(u). Differentiating
(3) gives the complete regular response equations

\[
\begin{aligned}
W_b(x,u)&=-\frac2m\lambda_b(u)\psi(z_b(u))
 -\frac2m\int_u^x\sum_a\lambda_a(v)\psi(z_a(v))Z_{ab}(v,u)\,dv,\\
V_{ab}(x,u)&=-2\lambda_a(u)A_a(u)\delta_{ab}
 -2\int_u^x\lambda_a(v)T_{ab}(v,u)\,dv,\\
Z_{ab}(x,u)&=Q_{h,ab}(x,u)A_b(u)
 +\sum_c\int_u^xQ_{h,ac}(x,v)T_{cb}(v,u)\,dv
 +\frac1m\sum_cK_{ca}(x)V_{cb}(x,u),\\
T_{ab}(x,u)&=B_a(x)W_b(x,u)+A_a(x)Z_{ab}(x,u).
\end{aligned}\tag{23}
\]

The response outputs are

\[
D_a^{\rm out}(x)=\mathbb EA_a(x),\qquad
Q_{d,ab}^{\rm out}(x,u)=\mathbb ET_{ab}(x,u).
\tag{24}
\]

Equations (23) imply |W|<=c, |V|,|Z|<=cS, |T|<=c. The O(S) bound on V
uses its initial source A(u)=O(S); the O(S) bound on Z uses both the first
term Q_h A and the integrated regular response. In particular (24) has
the advertised density and atom sizes.

We spell out current-time regularity because a total-variation size bound
alone would not establish a continuum domain. The z increment satisfies

\[
\|z(x)-z(y)\|_{L^2}
\le\|\gamma(x)-\gamma(y)\|_{L^2}
  +cS\|Q_h(x,\cdot)-Q_h(y,\cdot)\|_{L^1}
  +cS|x-y|+cS^2 L|x-y|
\le c|x-y|.
\tag{25}
\]

Consequently d has L2-Lipschitz increments, A has L1-Lipschitz increments,
and B has L2-Lipschitz increments. For the regular response, compare (23)
at x,y after zero extension in u. The moving source strip has measure
|x-y|. W's remaining row difference is an integral over the intervening
time interval of its bounded right-hand side, giving c|x-y|; V gives
cS|x-y|. The first term of Z has row difference at most
cS ||Q_h(x,.)-Q_h(y,.)||_1. In its integral term, integrate first in the
source u; sup_v ||T(v,.)||_1<=cS gives the same bound. Its K V term is
controlled by the preceding V estimate and (1). Thus Z has row difference
at most cS|x-y|. In T=B W+A Z, use these row bounds and Cauchy-Schwarz
for the coefficient increments. After expectation the Q_d-out row
difference is at most c|x-y|. This proves all the claimed Dlaw-output
regularity conditions.

Choose L_h,B_h first large enough for the lower output bounds. Those
bounds are independent of the chosen Dlaw-domain constants once
S B_d is sufficiently small. Choose L_d,B_d next large enough for
(6),(23)-(25), with these fixed H constants. Finally decrease S so that
all absorption bounds and S B_d smallness hold. This order avoids a
circular choice of domain constants. The map preserves the resulting
nonempty domain; constant C_h=C0 with Q_h=0 and zero Dlaw give one
admissible initial tuple.

## 7. Passage from meshes and contraction

For each fixed admissible input, couple its mesh Gaussians by sampling the
continuous versions already constructed. Cell-averaged lambda converges
in L1. Cell-averaging the source variable of Q converges in L1 uniformly
in current time: each current-time row belongs to a compact subset of L1,
because the row map is Lipschitz on a compact interval; source averaging
is a contraction in L1 and converges for each member of that compact set,
so a finite-net argument makes convergence uniform over the set. Replacing
current time by its left mesh endpoint adds at most the row Lipschitz
constant times the mesh size.

These facts and uniform continuity of the sampled Gaussian paths imply
uniform convergence of the Euler state equations to (3). Explicitly,
the difference is bounded by the accumulated input/quadrature error plus
c times its Volterra integral; iterating this inequality bounds it by
the input error times exp(cS). Bounded h,d,w,v and the deterministic drift
bounds then give covariance convergence uniformly in both times after
expectation.

For responses, divide each past discrete derivative by its cell length
as in (14). Their equations are the cell discretizations of (22)-(23).
Their source terms converge in L1: bounded state coefficients converge
uniformly in probability and in every finite Lp norm, lambda is averaged
in L1, and Q rows are averaged as above. The same integral comparison
therefore proves convergence of expected response rows in uniform L1
and convergence of the expected atom uniformly. This argument uses the
explicit source equations; it does not infer response convergence just
from convergence of the state values. It also identifies the output
as the derivative with input laws held fixed. Direct differentiation of
the integral equations gives the same derivative: their bounded second
and third derivative recursions justify the difference quotient and
its remainder by the corresponding Volterra estimate.

Consequently (21) passes to the continuum. In the normalized distances
(5), for constants c_L,c_U independent of S,

\[
d_H(L(Dlaw),L(\widetilde{Dlaw}))\le c_L S\,
                 d_D(Dlaw,\widetilde{Dlaw}),
\qquad
d_D(U(H),U(\widetilde H))\le c_U\,d_H(H,\widetilde H).
\tag{26}
\]

Choose S small enough that c_L c_U S<1, in addition to the earlier bounds.
The square of the full map (H,Dlaw)->(L(Dlaw),U(H)) is a contraction with
factor c_L c_U S in max(d_H,d_D). A Cauchy sequence of its iterates
converges in the complete domain; (26) shows that the limit is its unique
fixed point. Applying the unsquared map to that limit gives another fixed
point of the square, so uniqueness makes it a fixed point of the original
map as well. Equivalently, the original map is a contraction of factor
sqrt(c_L c_U S) in the weighted distance

\[
\max\left\{d_H,\sqrt{c_LS/c_U}\,d_D\right\}.
\]

This establishes existence and uniqueness of the prescribed-history law
fixed point, including its activity endpoint x=S. At S=0 the equations
are constant, the upper response and covariance vanish, and no normalized
distance is needed.

## 8. Passive velocity observables and Gaussian moment envelopes

The lower activity velocity at training sample a is the bounded observable

\[
q_a(x)=-\frac2m\sum_b\lambda_b(x)(u_a\cdot u_b)
 \psi(a(x)\cdot u_a)F(a(x)\cdot u_b,p_b(x)).
\tag{27}
\]

It satisfies h'_a=q_a almost everywhere. With prescribed lambda, it is a
passive observable: it is not added to the feedback system (3). By the
same product and composition bounds, its absolute history derivative sums
of orders one, two and three are bounded by c rather than cS. Its current
xi derivative is an atom with coefficient

\[
-\frac2m\lambda_b(x)(u_a\cdot u_b)
 \psi(a(x)\cdot u_a)F_p(a(x)\cdot u_b,p_b(x)).
\tag{28}
\]

Its regular past response is also retained. Covariances Ehh,Ehq,Eqq and
the response E D_xi q can be appended without changing the fixed point.
Equations (17),(19) and the direct current dependence in (27) yield

\[
\|\delta(Ehq,Eqq,\mathbb E D_\xi q)\|
\le c(\|\delta C_d\|_\infty+e)
\le cS\,d_D(Dlaw,\widetilde{Dlaw}),
\tag{29}
\]

where covariance sup norms and the unnormalized atom-plus-row response
norm are used. Since lambda may merely be measurable, no time continuity
of q or of its atom is asserted. These objects exist pointwise where
lambda is specified and as measurable, essentially bounded time-indexed
statistics. One can construct the associated joint Gaussian fields
(G_h,G_q) without inverting any Gram matrix: view h_a(x) and q_a(x) as
vectors in the lower representative's L2 probability space, choose an
orthonormal basis of their separable closed span, and apply independent
standard Gaussian coordinates to their basis expansions. This defines
the fields in L2 and jointly in time/probability on the finite interval.
Their covariance is precisely the corresponding raw second-moment block.

For an upper velocity observable of the form

\[
O(x)=w(x)\psi(z_a(x))G_{q,a}(x),
\tag{30}
\]

G_q is a passive jointly Gaussian coordinate correlated with gamma=G_h.
On every mesh, the absolute Hessian sum of (30) is bounded by
cS(1+|G_q(x)|). This follows by differentiating its single linear G_q
factor and using (10) for the other factor. Its higher derivatives of any
fixed needed order have the same type of envelope after the corresponding
finite-order jet estimate. Derivatives of its square have a quadratic
Gaussian envelope. Bounded q makes every G_q marginal variance bounded
uniformly. Gaussian moments therefore bound the expected derivative sum
in (17), and justify the epsilon limit and integration by parts by
truncation followed by dominated convergence. A deterministic global
Hessian bound is unnecessary for this passive extension.

If a covariance comparison is conditional on an environment, the same
argument applies conditionally provided the conditional fields really are
centered Gaussian and their conditional variances have a uniform bound.
The resulting conditional bias is bounded by c times the conditional
covariance error. If that error is random, its L2 norm can then be taken,
or Cauchy-Schwarz can be used with a derivative envelope whose second
moment is uniformly bounded. This is a conditional interpolation lemma;
it does not establish those conditional Gaussian or covariance-error
hypotheses for the finite-width network.

## 9. What an all-time width theorem still needs

This contraction supplies deterministic stability of a candidate law map.
It supplies neither a root-width source term nor finite-width
identification. In particular a root-width error for a predictor at each
fixed prescribed history is not enough by itself for restoration of
random training histories or a supremum over physical time.

A useful source statement has the physical-velocity form

\[
\dot e(t)=\text{controlled propagation terms}+\rho(t)\,\varepsilon_n(t),
\qquad
\sup_t\|\varepsilon_n(t)\|_{L^2}\le c/\sqrt n,
\tag{31}
\]

with the specified joint or conditional uniformity needed for an adaptive
history. For deterministic prescribed rho, Minkowski's inequality gives

\[
\left\|\sup_{T\ge0}\left|\int_0^T
 \rho(t)\varepsilon_n(t)\,dt\right|\right\|_{L^2}
\le\int_0^\infty\rho(t)\|\varepsilon_n(t)\|_{L^2}\,dt
\le cS/\sqrt n.
\tag{32}
\]

Thus pointwise-in-time root-width control of the **activity-normalized
velocity source** can be sufficient; a pointwise root-width state or
predictor comparison does not imply (31). With random rho_n, one needs a
joint estimate for rho_n epsilon_n, a conditional estimate with a valid
activity bound, or a pathwise/uniform-history source estimate. Multiplying
two separate marginal moment bounds does not establish it. Dissipative
training stability, removal of the initialized fitting-event conditioning,
and a valid finite-width cavity/source theorem remain separate obligations.

No conclusion here relies on the smooth top clip becoming exactly inactive.
When an actual prediction derivative is evaluated, its upper factor remains
w psi(z), as required by `SMOOTH_SETUP.md`; the passive observable (30)
uses that unclipped factor.

## 10. Dependence on prescribed coefficient histories: a precise boundary

The fixed-history argument also permits bounded measurable coefficients
alpha in [0,1] and beta_a with |beta_a|<=sqrt(m), with the memory equation
k'_a=alpha(h_a-k_a)/tau for a prescribed tau>=1. In (3), replace lambda
by beta. None of the derivative-sum estimates differentiates alpha,beta
or divides by them.

Thus two physical histories can be placed on the common clock

\[
x(t)=\int_0^t(\rho_1+\rho_2)(u)\,du,\qquad
\beta_{ia}=r_{ia}/(\rho_1+\rho_2),\quad
\alpha_i=\rho_i/(\rho_1+\rho_2).
\]

At a zero denominator all these coefficients are defined as zero. The
clock has length at most 2S, and

\[
\int|\beta_1-\beta_2|\,dx=\int|r_1-r_2|\,dt,\qquad
\int|\alpha_1-\alpha_2|\,dx=\int|\rho_1-\rho_2|\,dt.
\tag{33}
\]

This removes the apparent singularity of differentiating r/rho. It does
not, by itself, prove that every output-law or predictor error is bounded
solely by an integrated coefficient discrepancy.

There is a concrete reason for this restriction. At a current time,
with representative states held fixed, an arbitrary perturbation of K
changes the upper predictor F_a=E[w tanh(z_a)] by

\[
\partial_{K_{ba}(x)}F_a(x)
   =m^{-1}\mathbb E[w(x)\psi(z_a(x))v_b(x)].
\tag{34}
\]

This is generally nonzero and of size O(S^3). A current K error therefore
produces an O(S^3|delta K(x)|) algebraic term in addition to integrated
state errors. Likewise V changes the instantaneous lower p and the
passive q observable directly. Even uniformly Lipschitz coefficient
histories can have a late triangular perturbation of height epsilon and
duration proportional to epsilon: its integrated magnitude is O(epsilon^2)
while (34) gives an O(epsilon) instantaneous variation when its coefficient
is nonzero. Bounds based only on an integral of rho times the coefficient
error do not cover such arbitrary histories.

A suitable restoration argument can retain these algebraic terms or use
the structural equations making K,V themselves functions of the evolving
population states. A coupling on common population probability spaces
would be another possible route, once its identification with this law
fixed point is proved. Neither that identification nor the full causal
coefficient-history stability theorem is established in this scoped note.
They should not be inferred merely from fixed-history contraction (26).

## 11. Deterministic derivative majorants for random input-law errors

There is a necessary distinction between a uniform total derivative sum
and a deterministic entrywise majorant. The former alone would give
E sup_(x,y)|delta C(x,y)|, whereas a cavity estimate may supply only
sup_(x,y) E|delta C(x,y)|. Those quantities cannot be interchanged. The
particular equations here admit the stronger majorants described next.

### Positive tensor construction

Fix the mesh, the output node, and an ordered tuple I of Gaussian
history indices (node,sample). For every state or field variable X_i,
construct a deterministic nonnegative tensor b_Xi[I] dominating the
absolute derivative with that index tuple. All realized histories, a0,
and all admissible response inputs share the same tensor. For q=1,2,3,
use the full partition chain rule

\[
b_{f(X)}[I]
 =\sum_{\pi\in\mathcal P(I)}\;
   \sum_{\text{argument choices}}
     c_{f,\pi,\text{choices}}
       \prod_{B\in\pi}b_{X_{\text{choice}(B)}}[I_B],
\tag{35}
\]

where P(I) partitions the ordered slots, not their numerical index values.
The coefficient is a uniform bound for that partial derivative of f.
The finite sum over argument components is retained. Use addition for
sums, multiplication by the absolute deterministic coefficient for linear
terms, and the source tensor

\[
e_{ia}[I]=\mathbf 1_{|I|=1}\mathbf 1_{I=((i,a))}
\tag{36}
\]

for xi_ia or gamma_ia. All state history tensors at initialization are zero.

For clarity, the lower field construction is, componentwise,

\[
b_{p_{ia}}[I]=e_{ia}[I]+B_d x_i b_{h_{ia}}[I]
 +B_d\sum_{j<i,b}\Delta_j b_{h_{jb}}[I]
 +\frac{Lx_i^3}{m}\sum_b b_{k_{ib}}[I].
\tag{37}
\]

Construct b_h from b_a by (35). Construct the drift tensor from b_a,b_p
by (35), using the global derivatives of F and the bound on lambda.
The next a tensor is its current tensor plus Delta_i times this drift
tensor. The k tensor uses its corresponding linear and tanh terms. This
is a finite causal recursion for every index tuple, not an optimization
over the realized input.

For the upper system use

\[
\begin{aligned}
b_{z_{ia}}[I]&=e_{ia}[I]
 +B_h\sum_{j<i,b}\Delta_j b_{d_{jb}}[I]
 +m^{-1}\sum_b b_{v_{ib}}[I],\\
b_{w_{i+1}}[I]&=b_{w_i}[I]+c\Delta_i
       \sum_{b,\pi\in\mathcal P(I)}\prod_{B\in\pi}b_{z_{ib}}[I_B],\\
b_{v_{i+1,a}}[I]&=b_{v_{ia}}[I]+c\Delta_i b_{d_{ia}}[I].
\end{aligned}\tag{38}
\]

Construct b_d from b_w,b_z with (35). For the function
c_M(w psi(z)), every coefficient with derivatives only in z is bounded
by cS on |w|<=cS; coefficients containing a w derivative are bounded by c.
Use these different bounds in (35). Constants in (37)-(38) depend only
on the fixed domain constants and the model data.

Summing (35) over every ordered index tuple factorizes each product over
its disjoint slots. The sums consequently satisfy exactly the positive
versions of (11)-(13). Their total masses have all the bounds (10).
This proves a single deterministic majorant whose sum is cS; it is
stronger than saying that each realized derivative tensor separately has
total mass cS.

Repeated numerical source indices remain allowed. For example, two
current source factors e_i[(j,b)]e_i[(k,c)] in the second derivative of
one Euler drift contribute
Delta_i times the two Kronecker deltas. Summing over i puts that mass on
j=k=i with one factor Delta_i, not Delta_i^2. Formula (35) preserves all
such diagonal identifications. Replacing the tensors by products of
independent source-time densities would incorrectly lose these terms.

Fixing one history source (j,b), before summing the other slots, gives
the refinement

\[
\begin{aligned}
\sum_{I:\,|I|=q-1}b_{h_i}[(j,b),I]&\le c\Delta_j,
 &&j<i,\\
\sum_{I:\,|I|=q-1}b_{d_i}[(j,b),I]&\le c\Delta_j,
 &&j<i,\\
\sum_{I:\,|I|=q-1}b_{d_i}[(i,b),I]&\le cS,
 &&q=1,2,3.
\end{aligned}\tag{39}
\]

Indeed a past fixed source first enters either an Euler update with its
factor Delta_j or an integrated response weight bounded by B Delta_j.
The positive causal propagation in (37)-(38) preserves that factor.
Several occurrences of the same source at its first update still have
only this one factor, as just explained. The remaining-slot recurrences
are (11)-(13) with an inhomogeneous term c Delta_j. A current upper source
enters only d_i=c_M(w_i psi(z_i)), and its pure-z derivative coefficients
have the factor S. This proves (39), including mixed repeated indices.

Products h_i h_k and d_i d_k use the usual subset version of the product
rule and the deterministic zeroth-order bounds 1 and cS. Their Hessian
majorants therefore have total masses cS and cS^2. A response observable
uses the same third-order tensor with one distinguished response slot.
It can either be summed as in (10) or fixed as in (39). Thus the positive
majorants cover covariance outputs, atom outputs, and regular response
outputs with a source fixed or integrated.

### Random covariance comparison without a random supremum

Suppose two input covariances are measurable with respect to an
environment E. Conditional on E, perform Gaussian interpolation, with
all the deterministic response inputs or E-measurable response inputs
held fixed. They must satisfy the same deterministic domain bounds.
Let b_f[ij] be the preceding deterministic Hessian majorant. Then

\[
|\mathbb E[f(X_1)\mid E]-\mathbb E[f(X_0)\mid E]|
\le\tfrac12\sum_{ij}b_f[ij]|\delta\Gamma_{ij}|.
\tag{40}
\]

For p>=1, Minkowski's inequality gives

\[
\left\|\mathbb E[f(X_1)\mid E]-\mathbb E[f(X_0)\mid E]\right\|_{L^p(E)}
\le\tfrac12\sum_{ij}b_f[ij]\|\delta\Gamma_{ij}\|_{L^p(E)}
\le\tfrac12\Bigl(\sum_{ij}b_f[ij]\Bigr)
          \sup_{ij}\|\delta\Gamma_{ij}\|_{L^p(E)}.
\tag{41}
\]

The supremum is outside the expectation. For response comparisons, first
retain their output source slot in the deterministic third-order tensor,
then sum or integrate that slot. Tonelli and Minkowski give the analogous
bound, or (39) gives a pointwise source-density bound. There is no need
for a bound on the expected supremum of the covariance error.

### Random response-input comparison

The same construction applies to parameter variations; one must retain
the locations of their insertions. To see this explicitly, append one
distinguished parameter-derivative slot theta to the tensors and use
(35) with exactly one block containing theta. If the history tuple I is
empty or consists of one source, the direct lower forcing is

\[
|\delta D_{ia}|\,b_{h_{ia}}[I]
 +\sum_{j<i,b}|\delta\mathsf Q_{d,ij,ab}|\,b_{h_{jb}}[I],
\tag{42}
\]

in addition to the unchanged coefficients applied to the theta state
tensors. Here b_h[empty]=1. The corresponding upper forcing is

\[
\sum_{j<i,b}|\delta\mathsf Q_{h,ij,ab}|\,b_{d_{jb}}[I],
\tag{43}
\]

with b_d[empty]=cS. All subsequent factors are the deterministic positive
tensors (35)-(38). Consequently each output variation is a deterministic
nonnegative linear combination of absolute response-input differences,
including its direct current-row terms and its propagated earlier-row
terms. Equations (42)-(43) specify the insertion positions and are not
replaced by a sample-dependent supremum.

More explicitly, define the deterministic input-error numbers

\[
\begin{aligned}
e_p&=\sup_i\max_a\left(
 \|\delta D_{ia}\|_{L^p}
 +\sum_{j<i,b}\|\delta\mathsf Q_{d,ij,ab}\|_{L^p}\right),\\
\eta_p&=\sup_i\max_a\sum_{j<i,b}
                  \|\delta\mathsf Q_{h,ij,ab}\|_{L^p}.
\end{aligned}\tag{44}
\]

Take Lp norms in each positive recurrence before taking its deterministic
supremum over output nodes. Minkowski applies to each finite sum; every
coefficient multiplying a random error is a deterministic majorant.
The proof of (19)-(20) is then unchanged and yields

\[
\begin{aligned}
\sup_i\left(\|\delta h_i\|_{L^p}
       +\sum_j\|\delta\partial_{\xi_j}h_i\|_{L^p}\right)
 &\le cS e_p,\\
\sup_i\left(\|\delta d_i\|_{L^p}
       +\sum_j\|\delta\partial_{\gamma_j}d_i\|_{L^p}\right)
 &\le cS^2\eta_p.
\end{aligned}\tag{45}
\]

The sums include sample indices and the instantaneous upper response.
Gaussian conditional averaging, if present, is an Lp contraction and
does not enlarge these estimates. Thus random response errors require
sup_i sum_j ||error_ij||_Lp, not ||sup_i sum_j |error_ij|||_Lp.

One can also keep a source j fixed. Use (39) for every tensor in
(42)-(43), retaining the direct insertion at row/source (i,j). If the
regular input densities have essential pointwise Lp error at most B,
then ||delta mathsf Q_ij||_Lp<=Delta_j B. The resulting regular output
density errors are bounded by c(e_atom+SB) for the lower response and
cS^2 B for an upper Q_h perturbation. The upper atom perturbation is at
most cS^3B. These follow by the same positive recurrences after the fixed
factor Delta_j is divided out. In particular a direct Q_h(i,j) insertion
in the regular upper response has coefficient A_i A_j=O(S^2); it is
explicitly present, not smoothed over its target or source time.

For continuum random kernels, replace sums in (44) by

\[
\sup_x\max_a\left(\|\delta D_a(x)\|_{L^p}
 +\sum_b\int_0^x\|\delta Q_{d,ab}(x,u)\|_{L^p}\,du\right),
\quad
\sup_x\max_a\sum_b\int_0^x
                   \|\delta Q_{h,ab}(x,u)\|_{L^p}\,du.
\tag{46}
\]

Cell integration is compatible with these quantities by Minkowski.
The positive recursions converge through the same integral equations
used in Section 7; Tonelli applies because every majorant is nonnegative.
Equivalently, retain (42)-(43) as direct current-row integrals and their
Volterra iterates. Their deterministic total masses obey (45), and no
exchange of a random supremum with expectation occurs.

Combining (41),(45) gives (21),(26) with every covariance norm replaced by
the supremum of entrywise Lp errors, and every response norm replaced by
(46). The assertion is conditional on the conditional Gaussian comparison
being valid and on the input response coefficients obeying the stated
deterministic bounds; this section does not prove those cavity hypotheses.

For the passive observable (30), the same positive tensors give
entrywise envelopes b0[I]+b1[I]|G_q|, whose separate total masses are cS.
A uniform conditional variance bound for G_q turns their conditional
expectations into deterministic majorants b0[I]+c b1[I], so (40)-(41)
remain valid. If only an unconditional moment bound is available, use
Holder's inequality at each entry with the matching moments of that
entry's covariance error and the Gaussian envelope. In particular one
must not claim an L2 bias estimate from two merely L2 factors without
the additional conditional bound or higher moments.
