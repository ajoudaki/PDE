# A width-uniform oracle with dense residuals and dense backward gates

The user permits choosing the oracle so that it isolates the difficult feedback
terms and helps bridge to the autonomous population closure. This note makes
that choice explicit: the oracle integrates its **own** response histories and
reconstructs its **own** learned matrices, but receives the dense residuals,
the old residual-speed clock, and the dense activation slopes used in
backpropagation. Supplying the slopes is additional to supplying the residuals.
It is not hidden in a stability assumption.

The result is a complete width-independent O(P^-1) trajectory estimate for
any fixed depth and finite training set, with tanh activations. The oracle
is a reference-driven dynamical system, not gradient flow of its own loss.
The general residual-only oracle, retaining all of its own backward gates,
is not proved by this theorem.

## 1. Setup and exact definition

Use L>=2 hidden layers, m training samples q_a=x_a/sqrt(d), scalar output,
and the canonical flow of the manuscript. Every neuron space carries a
probability measure. Its norm is population L2, or ||v||_2/sqrt(n) at width n.
For first-layer rows use the population L2 norm of the row's Euclidean norm.
Hidden increments are measured in Hilbert--Schmidt norm, equal to ordinary
Frobenius norm at finite width when u tensor v is represented by uv^T/n.
Initialized hidden operators are kept exactly and need only be bounded.

The dense trajectory supplies

\[
 r_a^D(t),\quad \rho_D(t)=
   (m^{-1}\sum_a(r_a^D(t))^2)^{1/2},\quad
 \tau(t)=1+\int_0^t\rho_D(s)\,ds,\quad
 D_{\ell,a}^D(t)=\operatorname{diag}\tanh'(z_{\ell,a}^D(t)).
 \tag{1}
\]

At population width, D means multiplication by the indicated dense field.
Its operator norm is at most one. These gates evolve with the dense network;
they are not frozen at initialization.

Oracle forward responses are computed from its own current weights:

\[
 \bar h_{1,a}=\tanh(\bar W_1q_a),\qquad
 \bar h_{\ell,a}=\tanh(\bar W_\ell\bar h_{\ell-1,a}).
\]

Its backward responses are defined by the supplied gates:

\[
 \bar\delta_{L,a}=D_{L,a}^D\bar w,\qquad
 \bar\delta_{\ell,a}
 =D_{\ell,a}^D\bar W_{\ell+1}^*\bar\delta_{\ell+1,a}.
 \tag{2}
\]

The first layer and readout obey

\[
 \dot{\bar W}_1=-\frac2m\sum_a r_a^D\bar\delta_{1,a}q_a^T,\qquad
 \dot{\bar w}=-\frac2m\sum_a r_a^D\bar h_{L,a}.
 \tag{3}
\]

Each hidden link stores its own first P old-clock Legendre moments of
bar h_(ell-1,a) and bar b_(ell,a)=r_a^D bar delta_(ell,a)/rho_D.
The forward unit prefix is h_(ell-1,a)(0); the backward prefix is zero.
The raw moment equations are exactly those of the paper, with rho=rho_D,
residual=r_a^D and the responses defined above. In population operator notation,

\[
 \bar W_\ell=W_{0,\ell}
 -\frac2m\sum_a\int_0^\tau
      (\Pi_P\bar b_{\ell,a})(\xi)
          \otimes(\Pi_P\bar h_{\ell-1,a})(\xi)\,d\xi .
 \tag{4}
\]

Equations (1)--(4) define the oracle. The raw moment ODE never divides by
rho_D. At a zero-residual initial dense state, the dense process and this
oracle both stay at their common initialization, giving zero error. Otherwise
one may work on intervals with rho_D>0; the bounds below and the dense
residual equation show that it cannot reach zero at a finite time.

The computed oracle prediction need not have residual r_a^D. The supplied
residual is a forcing input in its update, not an assertion about its loss.
For the joint clock, residual agreement alone would not synchronize the
response-speed term. The present theorem uses the old clock explicitly.

## 2. Statement

Assume the dense canonical tanh population flow exists regularly on [0,T].
Let

\[
 X=\max_a\|q_a\|,\quad
 R_0=\|w(0)\|_2,\quad
 K_{0,\ell}=\|W_{0,\ell}\|_{\rm op},\quad
 S=\int_0^T\rho_D(t)\,dt,\quad A=1+S .
\]

All initial weights and moments agree with the dense initialization as in (4).
No zero-readout assumption is necessary for the P^-1 result.
Measure parameter differences by

\[
 d(\bar\theta,\theta)=
 \|\bar W_1-W_1\|_{\rm row,L^2}
 +\sum_{\ell=2}^L\|\bar W_\ell-W_\ell\|_{\rm HS}
 +\|\bar w-w\|_2 .
 \tag{5}
\]

Then the oracle exists uniquely through T for every P>=1 and

\[
 \sup_{t\le T}d(\bar\theta_P(t),\theta_D(t))
 \le \frac{C\,e^{\Lambda S}}{\sqrt{P(P+1)}}.
 \tag{6}
\]

Constants C and Lambda, constructed below, depend only on S, X, R_0,
the fixed depth and the initialized hidden operator norms. They do not
depend on P or the dimensions of the neuron spaces. Dense loss dissipation
also gives S<=T rho_D(0), where rho_D(0)<=R_0+label RMS.

This is an exact population theorem and a dimension-free finite-width
comparison theorem in the normalization (5). It does not cover the
unnormalized outer-weight error.

## 3. Bounds for the oracle, derived before any comparison

Because the residual forcing is prescribed and tanh is bounded,

\[
 \|\bar w(t)\|_2\le R:=R_0+2S.
\]

Set beta_L=R and, descending in layer, define

\[
 K_\ell=K_{0,\ell}+2\sqrt{AS}\,\beta_\ell,\qquad
 \beta_{\ell-1}=K_\ell\beta_\ell .
 \tag{7}
\]

These constants bound both dense and oracle states:

\[
 \|\bar W_\ell\|_{\rm op},\|W_\ell^D\|_{\rm op}\le K_\ell,\qquad
 \max_a\|\bar\delta_{\ell,a}\|_2,
 \max_a\|\delta_{\ell,a}^D\|_2\le\beta_\ell.
 \tag{8}
\]

Here is the noncircular induction. At the top, delta=D_L^D w gives beta_L.
Once beta_l is available, the normalized residuals c_a=r_a^D/rho_D satisfy
m^{-1}sum c_a^2=1, so the backward history has sample-averaged squared
L2 history norm at most S beta_l^2. Forward histories, including their
prefixes, have squared norm at most A. Projection contraction and
Cauchy--Schwarz over history and samples give

\[
 \|\bar W_\ell-W_{0,\ell}\|_{\rm op}
 \le 2\sqrt{AS}\,\beta_\ell.
\]

Equation (2) now gives beta_(l-1). For the dense matrix, direct integration
of its canonical update gives 2S beta_l, at most the same increment because
S<=sqrt(AS). This proves the induction for both processes. Also

\[
 \|\bar W_1(t)-W_1(0)\|_{\rm row,L^2}
 \le2SX\beta_1.
\]

For each finite P these bounds control all raw moment norms via their integral
representations. The denominator tau is at least one. The right-hand side of
the moment system is locally Lipschitz on its Hilbert state space with the
prescribed bounded multiplication gates. Dense L2-continuous preactivations
give strongly continuous multiplication gates: bounded slopes plus truncation
of a fixed L2 operand prove this from convergence in measure. The bounds on
moments and weights give uniform local Lipschitz and velocity bounds on the
visited bounded set, yielding continuation to T. Thus closure boundedness
and existence are conclusions, not hypotheses of (6).

## 4. A dimension-free accumulated compression defect

Let F_D(t,theta) be the canonical parameter update with supplied r^D and
supplied gates D^D, but with all forward responses and operator products
computed at theta. The oracle's physical weights satisfy

\[
 \dot{\bar\theta}=F_D(t,\bar\theta)+E,\qquad E_1=E_w=0 .
 \tag{9}
\]

At each hidden link the exact moment identity is

\[
 E_\ell=
 \frac{2\rho_D}{m}\sum_a
   (\bar b_{\ell,a}-\bar b_{\ell,a}^*)
       \otimes(\bar h_{\ell-1,a}-\bar h_{\ell-1,a}^*),
 \tag{10}
\]

where stars are current endpoint evaluations of the history projections.
This identity depends only on the moment integrals; it does not require
the supplied backward fields to be derivatives of the oracle forward map.

For any recorded history v write
D_v=||v-Pi_P v||^2_(L2(0,tau)).
Differentiating the least-squares error at its minimizing coefficients gives

\[
 \dot D_v=\rho_D\|v-v^*\|_2^2,\qquad D_v(0)=0.
 \tag{11}
\]

Terms differentiating the minimizing polynomial vanish by orthogonality.
Equations (10)--(11) and Cauchy--Schwarz give

\[
 \int_0^t\|E_\ell\|_{\rm HS}\,ds
 \le\frac2m\sum_a\sqrt{D_{b,\ell,a}D_{h,\ell-1,a}}.
 \tag{12}
\]

Only forward-history derivatives will be used. Put

\[
 Z_\ell(t)=\frac1m\sum_a\int_0^{\tau(t)}
          \|h_{\ell,a}'(\xi)\|_2^2\,d\xi.
\]

The Legendre H1 estimate, whose proof is given in DENSE_DRIVEN_ORACLE.md,
implies

\[
 \frac1m\sum_aD_{h,\ell,a}
 \le\frac{A^2 Z_\ell(t)}{4P(P+1)}.
 \tag{13}
\]

The first-layer equation yields Z_1<=Z_1^*=4S X^4 beta_1^2.
For deeper forward responses, endpoint evaluation on degree-below-P
polynomials has norm P/sqrt(tau). Indeed the squared norm is
sum_(k<P)(2k+1)/tau=P^2/tau, since p_k(1)=1.
Consequently, using (8), the sample RMS backward endpoint error is at most
(P+1)beta_l. Equations (10), (11), and (13) yield

\[
 \int_0^t\rho_D\|E_\ell/\rho_D\|_{\rm HS}^2\,ds
 \le\frac{P+1}{P}\beta_\ell^2 A^2 Z_{\ell-1}(t)
 \le2\beta_\ell^2 A^2 Z_{\ell-1}(t).
 \tag{14}
\]

The chain rule for the oracle's actual tanh forward activation, together
with (9) and |tanh'|<=1, therefore gives

\[
 Z_\ell(t)\le Z_\ell^*
 :=3\left[4S\beta_\ell^2+
       (K_\ell^2+2\beta_\ell^2A^2)Z_{\ell-1}^*\right].
 \tag{15}
\]

No derivative of the supplied gates is used. The endpoint factor P has
cancelled against the forward projection factor.

Finally, projection contraction gives
m^{-1}sum_a D_(b,l,a)<=S beta_l^2.
Substitute this and (13)--(15) into (12), and sum over hidden links:

\[
 \int_0^T\sum_{\ell=2}^L\|E_\ell(t)\|_{\rm HS}\,dt
 \le\frac{C}{\sqrt{P(P+1)}},\qquad
 C=A\sum_{\ell=2}^L\beta_\ell\sqrt{S Z_{\ell-1}^*}.
 \tag{16}
\]

This proves small accumulated absolute velocity error for the oracle's own
histories, without smooth backward histories or a zero-readout assumption.

## 5. The feedback estimate is now provable

Compare two physical states in the bounds (8), using the same prescribed
residuals and gates. Denote their distance (5) by d. The tanh forward
recursion gives

\[
 \max_a\|\Delta h_{\ell,a}\|_2\le U_\ell d,\qquad
 U_1=X,\quad U_\ell=K_\ell U_{\ell-1}+1.
 \tag{17}
\]

For backpropagation the common gates cancel in the difference; their operator
norm is at most one. Hence

\[
 \max_a\|\Delta\delta_{\ell,a}\|_2\le V_\ell d,\qquad
 V_L=1,\quad
 V_\ell=K_{\ell+1}V_{\ell+1}+\beta_{\ell+1}.
 \tag{18}
\]

For example,
Delta delta_l=D_l^D[W_l+1^* Delta delta_l+1+
Delta W_l+1^* delta_other,l+1]. There is no changed-gate multiplier.
Subtracting the gradient products and applying sample Cauchy--Schwarz gives

\[
 \|F_D(t,\theta)-F_D(t,\widetilde\theta)\|_{\rm sum}
 \le\rho_D(t)\Lambda\,d(\theta,\widetilde\theta),
\]
\[
 \Lambda=2\left[
   X V_1+\sum_{\ell=2}^L(V_\ell+\beta_\ell U_{\ell-1})+U_L
 \right].
 \tag{19}
\]

The sum norm is the one in (5). The constants in (19) have just been derived
from the operator bounds; uniform stability has not been assumed.

The dense flow itself satisfies
dot theta_D=F_D(t,theta_D): its supplied gates and residuals are its actual
ones. Subtract its integral equation from (9):

\[
 d(\bar\theta(t),\theta_D(t))
 \le\Lambda\int_0^t\rho_D(s)d(\bar\theta(s),\theta_D(s))\,ds
   +\int_0^t\sum_\ell\|E_\ell(s)\|_{\rm HS}\,ds.
\]

Iteration of this scalar integral inequality gives an amplification factor
at most exp(Lambda integral rho_D)=exp(Lambda S). Together with (16)
this proves (6), uniformly throughout [0,T].

## 6. Test outputs, width, and passage to the population target

For a test input x let X_x=||x||/sqrt(d), and define U_l(X_x) by (17) with
U_1=X_x. The same forward estimate and bounded top activations give

\[
 |\bar f_P(t,x)-f_D(t,x)|
 \le[1+R U_L(X_x)]\,d(\bar\theta_P(t),\theta_D(t)).
 \tag{20}
\]

The function U_L(X_x) is affine in X_x with constants depending only on the
hidden operator bounds. Equations (6), (20) prove uniform O(P^-1) prediction
error over any bounded input set, and L2(nu) prediction error for any test
distribution having finite second input moment. The difference of test
RMSEs against the same square-integrable target is at most this prediction
distance. This is not a claim about the dense model's generalization risk.

All inequalities are valid in probability-space Hilbert norms and their
finite-width RMS versions. No dimension enters their constants. Under
Gaussian initialization, initialized spectral/RMS bounds are interpreted
on uniform-probability events or with their moment bounds, rather than as
deterministic bounds on every Gaussian realization.

If dense width-n predictions converge to a population flow with error a_n(T)
in the same test norm, and the oracle at each width receives that dense
reference's signals, the triangle inequality gives

\[
 \sup_{t\le T}\|\bar f_{n,P}(t)-f_\infty(t)\|_{L^2(\nu)}
 \le a_n(T)+C_{T,\nu}/\sqrt{P(P+1)}
 \tag{21}
\]

on the stated uniform initialized-operator/RMS bounds. Existence of the
dense limit alone does not specify a rate for a_n(T).

## 7. What restoring the feedback would still require

The additional gate input is essential to the argument, and must not be
omitted from the oracle's description. If residuals alone are supplied, the
backward subtraction includes

\[
 [D_{\ell,a}(\bar\theta)-D_{\ell,a}(\theta_D)]q_{\ell,a}^D,\qquad
 q_{\ell,a}^D=(W_{\ell+1}^D)^*\delta_{\ell+1,a}^D
 \tag{22}
\]

(q_L^D=w_D at the top). RMS control of q_D does not make multiplication by
q_D bounded on L2. Supplying dense residuals cancels residual-difference
terms but does not cancel (22).

In contrast, the residual feedback itself is width-uniformly controlled
once a state discrepancy is controlled: (20) on the training set gives
||r(theta)-r(theta_D)||_(sample RMS)<=C d. Thus it can be included as another
linear term in the comparison inequality.

For the full old-clock closure, the same projection identities and physical
bounds give a width-independent accumulated defect estimate, as recorded
in OLD_CLOCK_ROUTE.md. Direct subtraction, isolating (22) with the dense
reference carriers, leaves an inequality of the form

\[
 \sup_{s\le t}d(\widehat\theta(s),\theta_D(s))
 \le C_T/P+
 C_T\int_0^t\rho_D(s)\sum_\ell
  \left(\frac1m\sum_a
    \|[D_{\ell,a}(\widehat\theta)-D_{\ell,a}(\theta_D)]
                 q_{\ell,a}^D\|_2^2\right)^{1/2}ds .
 \tag{23}
\]

Here the linear state and residual terms have been absorbed by Gronwall.
One obtains (23) by writing
Delta delta_l=D_l(hat)[W_hat,l+1^* Delta delta_l+1+
Delta W_l+1^* delta_D,l+1]+Delta D_l q_D,l and then recursing downward.
The bounded activation gates multiply the recursively propagated errors;
only the displayed dense-carrier products remain.

Equation (23) identifies precisely the next obligation. A suitable bound for
these gate errors could be combined with the present theorem and the existing
compression estimate. No such bound for arbitrary correlated data and depth
is asserted here. A fixed-point argument or the assertion that both clocks
agree does not, by itself, bound (22).

## 8. Corollary: residual and old-clock feedback can be restored

There is a further exact consequence. Keep the supplied dense gates, but let
the oracle compute its own residual r_bar=f_bar-y and its own old clock
tau_bar=1+integral rho_bar. Use these in its moment insertions and updates.
Then the same width-independent O(P^-1) theorem holds on every fixed horizon.
This remains a gate-fed oracle, not the autonomous closure.

Here are the required estimates, without assuming that this modified process
remains close. Let Y be label RMS. The readout equation, regardless of the
backward gates in other layers, gives

\[
 \frac d{dt}\|\bar w\|_2^2
 =Y^2-\frac4m\sum_a(\bar f_a-y_a/2)^2\le Y^2.
\]

Consequently

\[
 \|\bar w\|_2\le R_*=\sqrt{R_0^2+TY^2},\qquad
 \bar\rho\le Q=R_*+Y,\qquad
 \int_0^T\bar\rho\,dt\le TQ .
\]

The dense flow obeys the same upper bounds. Replace S in the source proof by
TQ, replace R by R_*, and use the same downward bounds (7) and forward
derivative recursion (13)--(16), now in each process's own clock. The defect
identity and its integral bound do not compare the two clocks, so no clock
distance or Gram-matrix comparison is needed. Existence and continuation
follow by the same raw-moment argument. At zero residual, all raw moments
and outer-weight velocities vanish, so the physical state remains stationary
even if the supplied dense gates continue changing. Clock-coordinate estimates
can be applied on nonstationary intervals and extended to such an endpoint.

Let G_D(t,theta) denote the update using theta's own residual and the supplied
dense gates. On these bounds, residual differences satisfy

\[
 \|r(\theta)-r(\widetilde\theta)\|_{\rm sample,RMS}
 \le C_f d(\theta,\widetilde\theta),\qquad C_f=1+R_*U_L,
\]

where U_L is from the forward recurrence (17). At fixed responses, changing
the residual changes the sum norm of the update by at most C_r times its
sample RMS, with

\[
 C_r=2\left[X\beta_1+\sum_{\ell=2}^L\beta_\ell+1\right].
\]

Splitting a vector-field difference first at a common residual and then at
common responses therefore gives the derived bound

\[
 \|G_D(t,\theta)-G_D(t,\widetilde\theta)\|_{\rm sum}
 \le (Q\Lambda+C_r C_f)d(\theta,\widetilde\theta).
\]

The dense reference solves dot theta_D=G_D(t,theta_D). Applying its integral
comparison to the modified oracle gives

\[
 \sup_{t\le T}d(\bar\theta_P(t),\theta_D(t))
 \le e^{(Q\Lambda+C_rC_f)T}\,
        C/\sqrt{P(P+1)}.
\]

Thus both residual feedback and the old clock's response to that residual can
already be restored for this oracle. What remains external, and remains the
substantive missing part of the full closure theorem, is the dense
neuronwise backward gate field.

## 9. Check status

The coordinator derived (1)--(23) from the current manuscript's canonical
flow and moment identities, and the current study's complete projection
proof. The scoped agent independently checked the residual-only backward
subtraction and then, after receiving this explicit oracle design, checked
that its defect identity and common-gate stability argument do not need
gate derivatives or a gradient interpretation. Its report is
SHARED_RESIDUAL_MULTIINPUT.md. The agent also checked Section 8's readout
identity, use of separate clocks, and residual Lipschitz coefficient and
found no substantive correction needed. These are internal analytic checks, not a
promotion review. No training, new literature search, manuscript modification,
or Git commit is part of this result.
