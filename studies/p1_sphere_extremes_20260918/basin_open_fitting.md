# A nonempty open fitting basin for every independent triple

Status: complete theorem candidate, frozen on 2026-09-18 before sharing.
This is an authorized follow-up using the exact continuous-carrier
framework, not an independent derivation of that framework. No numerical
work, finite population substitution, other basin-route report, or
external convergence theorem was used.

Scientific inputs: complete `basin_continuous_carrier.md`, the complete
`rank_one_nonlinear_obstruction.md` and its moment-realization argument,
and the already-read canonical p=1 population equations and physical
energy identity in `docs/observable_p1.md` and the permitted portions of
`docs/global_nonlinear.md`. The research and rigorous-mathematics skills
continue to apply.

## 1. Statement and state space

Fix any linearly independent unit directions u_1,u_2,u_3 in R3, positive
probability weights p_i, and labels y_i in {+1,-1}. Use the canonical
correlated dimension-three, order-one marks, ridge 1/4096, the complete
trainable 3 by 6 matrix and its actual transpose, and the unhalved square
loss in physical time. No rotation invariance or restricted matrix
dynamics is assumed.

Use exactly the compact carriers K_1,K_2, their full-support measures
nu_1,nu_2, and the separable Banach space from
`basin_continuous_carrier.md`:

\[
 X=C_{\rm odd}(K_1;\mathbb R^3)\times
       C_{\rm odd}(K_2;\mathbb R)\times\mathbb R^{3\times6},
 \quad
 \|(v,c,M)\|_X=\|v\|_\infty+\|c\|_\infty+\|M\|_F.       \tag{1}
\]

Here v=w-g is the lower displacement. The frozen carrier includes
z_i^0=tanh(g.u_i), and its exact current lower activations are
h_i=T(z_i^0,v.u_i), with
T(r,s)=(r+tanh(s))/(1+r tanh(s)). Almost surely this is
tanh((g+v).u_i). In particular |T|<=1 and 0<=partial_s T<=1,
including the compactified boundary. Write

\[
 a_i=E_1[b_1h_i],\quad H_i=\tanh(b_2^TMa_i),\quad
 f_i=E_2[cH_i],\quad r_i=f_i-y_i,\quad L=\sum_i p_i r_i^2.
                                                               \tag{2}
\]

**Theorem.** There is an explicitly specified finite fitted state
theta_* in X and a nonempty open forward-invariant neighborhood U of
theta_* such that every exact trajectory starting in U converges in X
to a fitted state. There are explicit positive constants gamma,C,
uniform over U, for which

\[
 L'(t)\le-2\gamma L(t),\qquad
 L(t)\le L(0)e^{-2\gamma t},\qquad
 \int_0^\infty\|\theta'(t)\|_Xdt
                      \le\frac C\gamma\sqrt{L(0)}.      \tag{3}
\]

Moreover, with the resulting endpoint theta_infinity,

\[
 \|\theta(t)-\theta_\infty\|_X
           \le\frac C\gamma\sqrt{L(0)}e^{-\gamma t}.    \tag{4}
\]

The endpoint may depend on the initial state. The assertion is an open
basin of the set of fitted states, not attraction to one distinguished
equilibrium. It is unconditional for every independent triple, but it
does not assert that the prescribed canonical point (0,0,D) lies in U
or in its backward reachable basin.

## 2. A concrete finite fitted state

Define the frozen mark bounds and lower covariance by

\[
 B_{1,\max}=\max_{K_1}|b_1|,\quad B_{2,\max}=\max_{K_2}|b_2|,\quad
 Q_1=E_1[b_1b_1^T],\quad q_1=\lambda_{\min}(Q_1)>0,
 \qquad\kappa=\frac{q_1}{2B_{1,\max}}>0.                \tag{5}
\]

The canonical lower law has a positive density on an open set in R6:
each original tanh-Gaussian pair has this property, the pairs are
independent, and the ridge Cholesky map is invertible. Consequently
Q_1 is positive definite. For any unit e in R6,

\[
 E|b_1\cdot e|\ge\frac{E|b_1\cdot e|^2}{B_{1,\max}}
                    \ge\frac{q_1}{B_{1,\max}}=2\kappa.  \tag{6}
\]

Let e_i, i=1,2,3, be the first three standard basis vectors in R6,
and set A_i=kappa e_i. For each i define on R6

\[
 F_i(\xi)=E_1\log\cosh(g\cdot u_i+b_1\cdot\xi).
                                                               \tag{7}
\]

The expectation is taken on the unchanged original Gaussian carrier;
its finite g is recovered almost surely from the compact carrier.
It is finite because log cosh(s)<=|s|, b_1 is bounded, and
E|g.u_i|<=1. Bounded tanh and its bounded first derivative permit
differentiation under this integral, giving

\[
 \nabla F_i=E_1[b_1\tanh(g\cdot u_i+b_1\cdot\xi)],
 \quad
 \nabla^2F_i=E_1[b_1b_1^T\operatorname{sech}^2
                                      (g\cdot u_i+b_1\cdot\xi)]\succ0.
                                                               \tag{8}
\]

Strict positivity follows because Q_1 is positive definite and the
gate is strictly positive at every finite Gaussian mark. The bound
log cosh(s)>=|s|-log 2 and (6) imply

\[
 F_i(\xi)-A_i\cdot\xi
       \ge\kappa|\xi|-E|g\cdot u_i|-\log2.              \tag{9}
\]

This continuous strictly convex function is coercive. It therefore has
a unique finite minimizer xi_i, and (8) gives grad F_i(xi_i)=A_i.
To make its finiteness quantitative, compare its value with its value
at zero in (9):

\[
                       |\xi_i|\le(2+\log2)/\kappa.      \tag{10}
\]

Independence of the u_i supplies dual vectors t_i in R3 with
t_i.u_j=delta_ij. Define

\[
 v_* =\sum_{i=1}^3t_i(b_1\cdot\xi_i),\qquad
 M_*=\kappa^{-1}[\,I_3\ \ 0\,].                        \tag{11}
\]

The displacement v_* is continuous and odd on K_1, with
||v_*||_infinity<=B_{1,max}(2+log2) sum_i|t_i|/kappa. Moreover
(g+v_*).u_i=g.u_i+b_1.xi_i, so its actual lower contractions are
a_i=A_i and M_*a_i=e_i in R3. No independent choice of unrealizable
lower moments has been made.

Write B_j=b_{2,j}. The three upper coordinates are independent, identically
distributed, symmetric, and nondegenerate. Hence, with

\[
 H_i^*(B)=\tanh B_i,\qquad
 \beta=E_2[\tanh^2 B_1]>0,\qquad
 c_* =\beta^{-1}\sum_{i=1}^3 y_iH_i^*,                  \tag{12}
\]

we have E H_i^*=0 and E[H_i^*H_j^*]=beta delta_ij. The readout c_*
is continuous, odd, and bounded by 3/beta. Equations (11)--(12)
therefore define theta_*=(v_*,c_*,M_*) in X and give

\[
                              f_i(\theta_*)=y_i.        \tag{13}
\]

All residuals vanish, so this is a stationary fitted state of the full
equations. The matrices in nearby initial states are arbitrary 3 by 6
matrices; the construction imposes no invariant rank or sparsity
restriction on their evolution.

## 3. Explicit constants and a local positive readout Gram

The following constants depend only on the declared marks and weights:

\[
 p_{\min}=\min_i p_i,\quad\gamma=\beta p_{\min}>0,
 \quad m_* =\sqrt3/\kappa=\|M_*\|_F,\quad C_*=3/\beta,
\]
\[
 D_H=B_{1,\max}B_{2,\max}(1+m_*),\quad
 \rho=\min\{1,\gamma/(4D_H)\},\quad
 R_M=m_*+1,\quad R_c=C_*+1,
\]
\[
 C=2\{1+B_{1,\max}B_{2,\max}R_c(1+R_M)\},\qquad
 K_f=1+C_*D_H.                                         \tag{14}
\]

Here C_* is a scalar upper bound for the readout norm ||c_*||_infinity.

Let d=||theta-theta_*||_X. Since T is 1-Lipschitz in its second
argument and the directions are unit,

\[
 |a_i-a_i^*|\le B_{1,\max}\|v-v_*\|_\infty,\qquad |a_i|\le B_{1,\max},
 \quad \|H_i-H_i^*\|_\infty\le D_Hd.                    \tag{15}
\]

For the last bound, split
M a_i-M_*a_i^*=(M-M_*)a_i+M_*(a_i-a_i^*), use the mark bounds,
and then use the 1-Lipschitz property of tanh.

Let P=diag(p_1,p_2,p_3), and define the weighted readout Gram

\[
 G_c(\theta)=P^{1/2}[E_2(H_iH_j)]_{ij}P^{1/2}.
                                                               \tag{16}
\]

The synthesis operator S_theta:R3->L2(nu_2),
S_theta z=sum_i sqrt(p_i) z_i H_i, has norm at most one by
Cauchy--Schwarz and sum_i p_i=1. Equation (15) gives
||S_theta-S_(theta_*)||<=D_Hd, and consequently

\[
 \|G_c(\theta)-G_c(\theta_*)\|_{\rm op}
       \le(\|S_\theta\|+\|S_{\theta_*}\|)
                                  \|S_\theta-S_{\theta_*}\|
       \le2D_Hd.                                      \tag{17}
\]

Since G_c(theta_*)=beta P, whenever d<rho,

\[
                         G_c(\theta)\succeq(\gamma/2)I_3.
                                                               \tag{18}
\]

This is a proved neighborhood property, not a hypothesis imposed on a
future trajectory. The same estimates give the local prediction bound

\[
              \sqrt{L(\theta)}\le K_f\|\theta-\theta_*\|_X,
                                                               \tag{19}
\]

by splitting f_i-f_i^*=E[(c-c_*)H_i]+E[c_*(H_i-H_i^*)]
and using ||c_*||_infinity<=3/beta.

## 4. Physical dissipation and X-norm speed on that neighborhood

On d<rho, the exact backward coefficients satisfy
|d_i|<=B_{2,max}R_c. The actual equations, including the full transpose,
and sum_i p_i|r_i|<=sqrt L therefore give

\[
 \|c'\|_\infty\le2\sqrt L,\qquad
 \|M'\|_F\le2B_{1,\max}B_{2,\max}R_c\sqrt L,\qquad
 \|v'\|_\infty\le2B_{1,\max}B_{2,\max}R_MR_c\sqrt L.
\]

Thus

\[
                              \|\theta'\|_X\le C\sqrt L. \tag{20}
\]

The loss still dissipates in the physical population-L2/Frobenius metric,
not the X norm. Write e=P^(1/2)r. Its readout contribution alone gives

\[
 L'=-\|v'\|_2^2-\|c'\|_2^2-\|M'\|_F^2
       \le-4e^TG_ce\le-2\gamma L.                       \tag{21}
\]

Both (20) and (21) hold pointwise throughout the same known neighborhood.
Their combination, rather than any equivalence between the two norms,
will give finite length in X.

## 5. Open trapping region, global existence, and fitted convergence

Define

\[
 \mathcal U=\left\{\theta\in X:
       \|\theta-\theta_*\|_X+
                     \frac C\gamma\sqrt{L(\theta)}<\rho\right\}.
                                                               \tag{22}
\]

Continuity of L makes U open. It contains theta_* and, by (19), the
explicit X ball of radius

\[
                  \varepsilon=
             \frac{\rho}{2(1+(C/\gamma)K_f)}>0           \tag{23}
\]

around theta_*. In particular U is nonempty and all its points have
distance less than rho from theta_*.

Fix theta(0) in U. The exact X flow exists through every finite time
by the supplied continuous-carrier existence proof. Until a hypothetical
first exit from the radius-rho ball, set q(t)=sqrt(L(t)). Where q>0,
(21) implies q'<=-gamma q. If q reaches zero, the entire vector field
is zero, and uniqueness makes the state stationary thereafter. Thus
integration across either case gives

\[
 q(t)\le q(0)e^{-\gamma t},\qquad
 \int_0^t Cq(s)ds\le\frac C\gamma\{q(0)-q(t)\}.         \tag{24}
\]

Using (20), the triangle inequality, and (24),

\[
 \begin{split}
 \|\theta(t)-\theta_*\|_X+\frac C\gamma q(t)
 &\le\|\theta(0)-\theta_*\|_X+
                         \int_0^t Cq(s)ds+\frac C\gamma q(t)\\
 &\le\|\theta(0)-\theta_*\|_X+\frac C\gamma q(0)<\rho.
 \end{split}                                             \tag{25}
\]

The strict initial margin is retained. A first exit would have distance
rho by continuity and contradict (25). Hence no exit occurs, and
(25) proves that U itself is forward invariant. In particular the
positive Gram bound (18) is established for every future reached state,
as a conclusion of trapping.

Equations (21), (24), and (20) now hold for all time and imply (3).
The integral of ||theta'||_X is finite. Since X is complete, the
trajectory is Cauchy at infinity and has an endpoint theta_infinity
in X. Continuity of the finitely many predictions and exponential
loss decay give L(theta_infinity)=0. Integrating (20) from t to infinity
gives (4). Passing to the limit in (25) also shows that the endpoint
has distance strictly less than rho from theta_* and therefore belongs
to U.

One can enlarge this open basin without any new convergence argument:
if Phi_T is the exact time-T map, then

\[
                \mathcal B=\bigcup_{T\ge0}\Phi_T^{-1}(\mathcal U)
                                                               \tag{26}
\]

is open by finite-time continuous dependence, nonempty, and forward
invariant. Every point of B enters U after a finite time and then
converges in X to a fitted endpoint with an exponential tail. No claim
is made that B exhausts all fitting initial states.

## 6. Scope and audit

The neighborhood and rate are derived from the constructed current
state, bounded scalar gates, exact mark integrals, and a first-exit
argument. No future lower bound on a feature Gram or endpoint Jacobian
was assumed. Existence and X convergence concern the exact separable
continuous-carrier population flow, with every moving block trained.

The constants in (14), (22), and (23) depend only on the canonical marks
and p_min; they do not deteriorate with the geometry of an independent
triple. The fitted center itself can have large displacement when the
input matrix is nearly singular, through the dual vectors in (11).
This distinction is essential: a uniform local attraction radius around
these possibly distant centers does not imply attraction from the
canonical initialization.

An infinite-dimensional family of nearby fitted endpoints is expected:
readout variations orthogonal to all three H_i^* leave the fitted
predictions unchanged at fixed v_*,M_*. Accordingly the theorem promises
convergence to a fitted state, exactly as stated, and does not promise
that every nearby trajectory converges to theta_* itself.

The result proves an unconditional nonempty open fitting basin for
every independent triple. It leaves both the size of the full global
basin and membership of the fixed canonical initialized point unresolved.

Notation-only correction after the initial freeze, 2026-09-18: renamed
the deterministic mark supremum bounds from B_1,B_2 to B_{1,max},B_{2,max},
retaining B_j for the random upper coordinates. No mathematical statement,
constant value, inequality, or proof step changed. The original frozen
file's SHA256 was
`de275622152fdc18fa81eba0e6adc73d8fff6fb35ed634bef8429ddee9802821`.
