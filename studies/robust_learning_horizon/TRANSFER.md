# Quantitative transfer from the opposite-label reference

Author: `/root`. Candidate proof; the reference and response inputs named below
must pass complete independent review together with this argument.

## 1. Exact fields and comparison constants

Put `u=x/sqrt(2)` and `phi=tanh`. On the canonical two population spaces use
the full state `theta=(w,A,c)`, where `w in L2(Omega_1;R2)`,
`A:L2(Omega_1)->L2(Omega_2)` is bounded and `c in L2(Omega_2)`. Set

\[
 Z^1(u)=w\cdot u,\quad H^1(u)=\phi(Z^1(u)),\quad
 Z^2(u)=AH^1(u),\quad H^2(u)=\phi(Z^2(u)),\quad
 f(u)=\langle c,H^2(u)\rangle,
\]
\[
 r(u,y)=f(u)-y,\quad \delta^2(u)=c\phi'(Z^2(u)),\quad
 Q(u)=A^*\delta^2(u),\quad \delta^1(u)=\phi'(Z^1(u))Q(u).
\]

The unhalved mean-loss field, with exactly the prescribed mobilities, is

\[
 F_\lambda(\theta)=-2\left(
 \int r\delta^1u\,d\lambda,
 \int r\delta^2\otimes H^1\,d\lambda,
 \int rH^2\,d\lambda\right).                                      \tag{1}
\]

The rank-one action is `(v tensor h)g=v E_1[hg]`. The distance is

\[
 D(\theta,\bar\theta)=\|w-\bar w\|_{L^2(\Omega_1;\mathbb R^2)}
 +\|A-\bar A\|_{op}+\|c-\bar c\|_{L^2(\Omega_2)}.                 \tag{2}
\]

For two networks of the same width replace the three norms respectively by
`||W1-W1bar||F/sqrt(n)`, `||W2-W2bar||op`, and
`||W3-W3bar||2/sqrt(n)`; call this `D_n`. The finite rank is `v h^T/n`.
There is no comparison in operator norm across widths or carriers.

Here is an explicit version of the maintained C.4 transport lemma. Suppose
each individual state norm in (2) is at most `B=12`; the norms in this premise
are of each state component, not of a difference. Define
`tau_R(v)=||v 1_(|v|>R)||2` and

\[
 \mathcal T_R(\bar\theta)
 =\tau_R(\bar c)+\tfrac12\sum_{a=1}^2\tau_R(\bar Q(e_a)).
\]

For any probability law lambda on the binary observation space, any `R>=1`,
and the fixed reference nu_* of the question,

\[
 \|F_\lambda(\theta)-F_{\nu_*}(\bar\theta)\|_{(2)}
 \le 10^6\{(1+R)[D(\theta,\bar\theta)+W_1(\lambda,\nu_*)]
                         +\mathcal T_R(\bar\theta)\}.             \tag{3}
\]

This holds also in the normalized finite norms, with the same constant.
Here are arithmetic details making the constant checkable. For a coupling
pair `(u,y),(v,z)`, set `h=|u-v|`, `d=D`, and `l=|y-z|`. Then

\[
 \|Z^1-\bar Z^1\|_2\le B(d+h),\quad
 \|Z^2-\bar Z^2\|_2\le B(B+1)(d+h),\quad
 |r-\bar r|\le B^3(d+h)+l.                                      \tag{4}
\]

The bounds use `|phi|,|phi'|<=1` and `Lip(phi')<=2`. For any fixed reference
field v, splitting at `|v|=R` gives
`||[phi'(z)-phi'(zbar)]v||2 <=2R||z-zbar||2+2tau_R(v)`.
Writing `a=B(B+1)=156`, successive subtraction therefore gives

\[
 \|\delta^2-\bar\delta^2\|_2
 \le313(1+R)(d+h)+2\tau_R(\bar c),
\]
\[
 \|\delta^1-\bar\delta^1\|_2
 \le3792(1+R)(d+h)+24\tau_R(\bar c)+2\tau_R(\bar Q(v)).           \tag{5}
\]

For the lower, middle and readout integrands, respectively, the coefficients
of `(1+R)(d+h+l)` before the overall factor 2 are at most

\[
 B^2(B^3+1)+(B+1)3792+(B+1)B^2,
\]
\[
 B(B^3+1)+(B+1)313+(B+1)B^2,
 \qquad B^3+1+(B+1)a.
\]

Twice their sum is less than `10^6`. The total reference-tail coefficient
is at most `4(B+1)(B+1)=676`, also below `10^6`. These decompositions include
the explicit changed input vector in `r delta^1 u`. Integrating the estimates
against a coupling and taking the infimum of its cost proves (3).
No maximum over actual observations, positive Gram eigenvalue or atom-weight
bound occurs. The full Gaussian row enters (4) only through its L2 norm.

For same-input prediction and activation comparisons on this ball,

\[
 \sup_u|f_\theta(u)-f_{\bar\theta}(u)|\le2B^2D,
 \quad\sup_u\|H^\ell_\theta(u)-H^\ell_{\bar\theta}(u)\|_2
 \le(B+1)D\quad(\ell=1,2).                                    \tag{6}
\]

Every such predictor has `|f|<=B` and Lipschitz constant at most `B^3` in u.
Thus its binary squared-loss integrand has joint Lipschitz constant

\[
 L_{risk}=2(B+1)B^3=44928,\qquad
 |R_\lambda(f)-R_\rho(f)|\le L_{risk}W_1(\lambda,\rho).           \tag{7}
\]

## 2. Actual finite reference GF and uniform observable passage

Let `bar theta_n(t)` be the actual finite gradient flow on nu_*, started from
exactly the same three initialized arrays as the network to be compared.
In particular its finite readout is not zero. Finite dynamics §§1–4 gives
global existence and the exact raw-metric energy identity. With probability
tending to one, initialization satisfies

\[
 \|W^1_0\|_F/\sqrt n\le2,\quad\|W^2_0\|_{op}\le3,\quad
 \|W^3_0\|_2/\sqrt n\le1/4,\quad\|W^3_0\|_\infty\le1.
                                                                    \tag{8}
\]

The first/readout assertions follow from Gaussian second moments and the
Gaussian union bound; the sharp matrix bound is proved in global-nonlinear
A.3. Initial loss is at most `25/16`. Up to `T=40`, every block displacement
in its raw metric is at most `sqrt(40*25/16)<8`, by energy and Cauchy–Schwarz.
Consequently each reference component norm is strictly below 11. Its readout
coordinate bound is at most `1+2T sqrt(25/16)=101`, because the mean absolute
residual is bounded by the square root of the nonincreasing loss. These
bounds apply to the actual finite flow, including its nonzero readout.

For this particular reference, B.1 applies with two orthogonal inputs,
sigma_1=sigma_2=1, beta=1, both activations tanh and kappa_i=1/2 to convert
its sum loss into the present mean loss. Its construction uses the same
fixed first Gaussian pair and initialized action with its actual adjoint.
Its unique population flow is the one in REFERENCE.md. The two active lower
projections determine the full first row since they are precisely its two
columns. Thus all passive circle inputs are evaluated using the same trained
row, without creating extra training observations.

We spell out the additional uniform observations needed here. At fixed
auxiliary transformed mesh Delta, append finitely many passive forward
evaluations and the active queries `Q_a=A* [c phi'(Z2_a)]` to B.1's oracle
program. Its value theorem A.1 and complete III.F fixed-program construction
give the joint node laws and second moments. The readout product can be
clipped beyond its proven coordinate bound, so it is globally Lipschitz in
its varying arguments. The transformed same-root comparison bounds the
finite-flow/mesh error uniformly in width; learned action differences use
operator norm. Its forward estimates also control the passive directions.
The Q difference is bounded in L2 by

\[
 \|A-\widetilde A\|_{op}\|c\|_2+
 \|\widetilde A\|_{op}
 (\|c-\widetilde c\|_2+2\|\widetilde c\|_\infty
                                  \|Z^2-\widetilde Z^2\|_2).
                                                                    \tag{9}
\]

First take width to infinity with Delta fixed, then remove Delta. This proves
the fixed-time joint second-moment limits for Q, the forward fields and paired
initial/current activations. It does not apply a finite-program theorem to
the growing actual GD transcript.

The passage is uniform in physical time. On (8), the reference has uniformly
bounded raw velocities on `[0,40]`, by (1) and the preceding bounds. Strong
curve differentiation gives `dot Z2=dot A H1+A phi'(Z1)dot Z1`, and
`dot delta2=dot c phi'(Z2)+c phi''(Z2)dot Z2`. Their L2 norms are uniformly
bounded using `|c|<=101`. Differentiating `Q=A*delta2` then bounds its L2
time-Lipschitz constant independently of width. The population proof is
identical. Norms of positive-part cutoffs of Q inherit this Lipschitz constant.
A fixed finite time grid followed by its refinement therefore extends every
needed cutoff second-moment comparison uniformly in time. Forward evaluations
are Lipschitz in input with constants bounded by the state norms. A fixed
finite input net, after the time net, proves

\[
 \sup_{t\le40,u\in S^1}|\bar f_n(t,u)-f_*(t,u)|\longrightarrow0
                         \quad\text{in probability}.              \tag{10}
\]

The same argument for the bounded squared displacement integrand, retaining
the same neuron at time zero and current time in the fixed programs, gives

\[
 \sup_{t\le40,u}\left|\frac1n
 \|\bar h^\ell_n(t,u)-h^\ell_n(0,u)\|_2^2
 -\mathbb E_\ell|H^\ell_*(t,u)-H^\ell_0(u)|^2\right|
 \longrightarrow0\quad\text{in probability}.                       \tag{11}
\]

Here no individual finite neuron is coupled with an invented population neuron.

The response proof supplies, on the reference feature segment through its
interpolating endpoint, `Q_a=G_a+E_a`, with `G_a` centered Gaussian of variance
at most 16, `|E_a|<=M_Q`, and

\[
 M_Q=225400e^{2880}+180<e^{2893}.                                  \tag{12}
\]

Also `|c_*|<=10`. For `R>=4M_Q+20`, elementary Gaussian integration gives

\[
 \sup_{t\le40}\mathcal T_R(\bar\theta_n(t))
 \le H e^{-R^2/4096}+o_{\mathbb P}(1),\qquad H=16(4+M_Q).          \tag{13}
\]

Every `o_P(1)` here is at fixed R and on one fixed reference. To check the
constants, if `G` has variance at most `sigma²`, then
`E exp(G²/(4sigma²))<=sqrt(2)`. Splitting `Q=G+E` and using
`x²<=8sigma² exp(x²/(8sigma²))` bounds
`tau_r(Q)<=8(sigma+M_Q)exp(-r²/(64sigma²))` for `r>=2M_Q`.
At finite width `tau_R(Q_n)<=2||(|Q_n|-R/2)_+||2` and this latter norm
converges uniformly in time to its population counterpart by (9) and the
time-grid argument. Take sigma=4 and r=R/2. The readout has no tail at
R>101 at finite width on (8). Our final R is much larger. This proves (13).

## 3. Raw GD comparison, stopping, and limit order

Actual finite raw GD is exactly
`theta_(j+1)=theta_j+eta F_lambda(theta_j)` for (1). It does not update a
transformed clock. For completeness its states have a width-independent
bound on every fixed horizon, for any probability law. If c_j is its readout
RMS, then `1+c_(j+1)<=(1+2eta)(1+c_j)`. Hence `c_j<=2e^(2(T+1))` for
initial c_0<=1 and nodes through T+eta, eta<=1. Writing this bound as C_T,
the middle norm is at most `3+2(T+1)(C_T+1)C_T=:A_T`, and the full-row RMS
is at most `2+2(T+1)(C_T+1)A_T C_T`. These estimates follow directly from
successive raw increments, not a GD energy inequality.

Sharper constants in the comparison come from stopping at the first time
`D_n(theta_GD(t),bar theta_n(t))=1`. Before that time both states have
individual norms at most B=12. The GD preceding-node state also lies there:
its preceding time has not exited. Both interpolant speeds on this prefix
are bounded by

\[
 V=2(B+1)(B^2+B+1)=4082.
\]

At time t the GD preceding state differs from its interpolant by at most
V eta. Apply (3) against the actual reference GF at t, integrate the velocity
difference, and use (13). Initial distance is exactly zero. With
`K=40*10^6=40000000` and `q=W1(lambda,nu_*)`, Gronwall gives, on the stopped
interval,

\[
 \sup_{t\le40}D_n(\theta_{GD}(t),\bar\theta_n(t))
 \le K e^{K(1+R)}\{(1+R)(q+V\eta)
                           +H e^{-R^2/4096}+o_{\mathbb P}(1)\}.   \tag{14}
\]

The supremum in (14) is first understood up to the stopping time. If its
right side is strictly less than one, continuity excludes that stopping
time, and the estimate holds through 40. All probabilities in (14) come from
initialization and the one fixed reference; the bound otherwise applies to
every actual law with the displayed q. A stochastic actual law is therefore
handled on its event controlling q, without any law-dependent width theorem.

The limit order is: fix T, the reference, the cutoff R and an auxiliary
accuracy; establish the reference GF observations by fixed transformed mesh,
width limit, then mesh removal; use those resulting reference statements in
(14) and send the actual width to infinity and its step to zero. Auxiliary
proof meshes never become actual GD steps. No transformed Euler increment is
claimed to equal a raw GD increment; (14) compares actual raw GD directly to
actual raw GF. The sufficient condition `eta_k sqrt(n_k)->0` requested in
the primary theorem is permissible. In fact this particular final comparison
uses only `eta_k->0`, because B.1 is used for the reference GF, not for an
actual reference GD sequence.

## 4. Remaining assembly interface

The numerical error tolerance, the exact certified radius, activity time and
positive activity margin are fixed in THEOREM.md using REFERENCE.md and
RESPONSE.md. For any tolerance d0<1, it suffices to choose R and delta with

\[
 K H\exp(K(1+R)-R^2/4096)\le d_0/4,\qquad
 K(1+R)\exp(K(1+R))\delta\le d_0/4.                             \tag{15}
\]

Then for any deterministic empirical sequence lambda_k with
`W1(lambda_k,mu)->0`, `W1(mu,nu_*)<delta`, the positive excess of the full
time-uniform same-width state distance over d0/2 tends to zero in probability.
There is no assertion that perturbed trajectories converge to a unique global
population trajectory. Equations (6), (7), (10), (11) transfer the observable
conclusions without that assertion.

For iid empirical laws of sizes m_k->infinity, independent of initialization,
`W1(lambda_k,mu)->0` in probability. A direct proof partitions the compact
observation space into finitely many Borel cells of diameter epsilon, moves
each law to the same representatives at cost at most epsilon, and bounds the
remaining transport by half the diameter (at most 4) times the sum of cell
mass discrepancies. Each empirical cell mass has variance at most 1/(4m_k).
First send m_k to infinity at fixed partition, then epsilon to zero. A union
bound with the initialization/reference events proves the same joint limits
for arbitrary width/sample growth rates. This gives probability tending to
one for every fixed mu and sequence. No numerical finite-width rate, almost
sure joint convergence or uniform failure probability over laws is asserted.
