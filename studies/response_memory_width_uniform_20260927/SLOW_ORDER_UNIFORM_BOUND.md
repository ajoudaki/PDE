# Slow memory growth: all-time discrepancy with a dense-only width remainder

28 September 2026. Continuation of the width-uniform response-memory study.
This note retains exactly zero initial readout and fixed, positive small
labels. It changes neither the algorithm nor the paper/book. The conclusions
below are deductions from the study's small-label source, damping, and
Gaussian finite-program results. They do not provide a numerical concentration
rate in width.

## 1. Model, discrepancy, and conclusion

Fix a finite dataset of size m, a fixed input dimension, and fixed hidden
depth L. The activation is tanh. First-layer entries are independent N(0,1),
initialized hidden entries are independent N(0,1/n), and the stored readout
is exactly zero. Use the canonical block mobilities (n,1,...,1,n), squared
loss averaged over the m samples, and the original autonomous old-clock
Legendre closure. Dense flow and every closure order share the same initialized
arrays. In this note q is the actual number of moments, denoted P in earlier
study files; it is not a new auxiliary scaling parameter.

Assume the limiting initial readout-feature Gram is positive definite. The
label RMS Y is one fixed number in (0,Y_*], with the same width-independent
small-label threshold needed for the all-time activity and Gaussian results.
Let G_n be the common initial operator/feature-Gram event. Its probability
tends to one. All deterministic estimates below are on G_n; no common
almost-sure event across infinitely many widths is asserted.

Use the normalized physical-parameter distance

\[
 d_n(\widehat\theta,\theta_D)=
 \frac{\|\widehat W_1-W_{1,D}\|_F}{\sqrt n}
 +\sum_{\ell=2}^L\|\widehat W_\ell-W_{\ell,D}\|_F
 +\frac{\|\widehat w-w_D\|_2}{\sqrt n},
 \qquad E_n(q)=\sup_{t\ge0}d_n(\widehat\theta_{n,q}(t),\theta_n^D(t)).
\]

There is a nonnegative random quantity a_n, defined solely from the dense
trajectory and the initialized arrays, such that a_n tends to zero in
probability and, simultaneously for every integer q>=1 on G_n,

\[
 E_n(q)\le C\Phi(q^{-1}+a_n),\qquad
 \Phi(s)=s\exp\!\left(K\sqrt{\log(e+1/s)}\right),\quad \Phi(0)=0.
 \tag{1}
\]

Here C,K are independent of n,q and physical time. They depend on the fixed
model/data, initial bounds and Gram gap. Equivalently, subadditivity of Phi gives

\[
 E_n(q)\le \frac{C}{q}\exp\!\left(K\sqrt{\log(e+q)}\right)+b_n,
 \qquad b_n=C\Phi(a_n)\longrightarrow0\quad\hbox{in probability}.
 \tag{2}
\]

For every fixed 0<gamma<1, a simpler consequence is

\[
 E_n(q)\le C_\gamma\bigl(q^{-\gamma}+a_n^\gamma\bigr).
 \tag{3}
\]

The remainder is independent of order and involves no closure trajectory.
It is a proof quantity, not an extra input supplied to the implemented
closure. There is no claimed n^(-1/2), or other explicit width rate, for it.

## 2. Existing inputs, in the exact forms used

The source and damping inputs are proved in SMALL_LABEL_ENERGY.md and
SMALL_LABEL_ALLTIME_SYNTHESIS.md.
On G_n, dense and all finite-order closures remain on one physical bounded
region for all time. The dense residual decays exponentially; both paths'
total activity and parameter variation are bounded independently of n,q. The
actual physical closure obeys dot(theta_hat)=F_n(theta_hat)+E_q, with

\[
 \int_0^\infty\|E_q(t)\|_{\rm sum}\,dt\le C/q,
 \qquad \rho_D(t)\le C e^{-\lambda t},\qquad
 \int_0^\infty\rho_D(t)\,dt\le C.
 \tag{4}
\]

The constants absorb the fixed positive label RMS. They do not absorb width.
The actual-path comparison obtained by damping the residual discrepancy is

\[
 d_n(t)\le C/q+C\int_0^t\rho_D(s)
                 [d_n(s)+G_q(s)]\,ds,
 \tag{5}
\]

where G_q is the sum over hidden layers (with maximum over the finite samples)
of the RMS norm of

\[
 [\tanh'(\widehat z_{\ell,a})-\tanh'(z_{\ell,a,D})]k_{\ell,a,D},
 \qquad k_{\ell,a,D}=W_{0,\ell+1}^T\delta_{\ell+1,a,D},\quad \ell<L.
\]

The top initial carrier is zero because the readout starts at zero. The
learned part of each remaining backward carrier is coordinatewise bounded
by its exact integral representation and has already been included in the
first term in the integrand of (5). This is why only initialized branches
appear above.

The dense Gaussian input, proved in SMALL_LABEL_GAUSSIAN.md, is uniform-in-time
exponential-square integrability of the population carriers. Subtracting the
bounded learned branch gives the same type of bound for the initialized
carriers k. GENERAL_GAUSSIAN_TRANSPORT.md supplies fixed finite Gaussian
program approximation and the one-reference cutoff estimate. These transfer
fixed-cutoff dense empirical tails on each fixed finite horizon. No estimate
uniform in a growing cutoff or growing transcript is assumed.

## 3. A deterministic bound in terms of dense empirical tails

For an integer M>=1 define

\[
 H_n(M,t)=\sum_{\ell<L}\max_a
 \frac{\|k_{\ell,a,D}(t)\mathbf1_{|k_{\ell,a,D}(t)|>M}\|_2}{\sqrt n},
 \qquad Z_n(M)=\int_0^\infty\rho_D(t)H_n(M,t)\,dt
 \tag{6}
\]

on G_n, and set Z_n(M)=0 off G_n. Both are nonnegative and nonincreasing
in M. The ordinary operator and backward RMS bounds give Z_n(M)<=C on G_n.

Split a carrier at absolute value M. The Lipschitz gate bound and the forward
parameter-difference recurrence give

\[
 G_q(t)\le C M d_n(t)+C H_n(M,t).
\]

Insert this in (5), use (4), and apply the scalar integral integrating factor.
For each finite terminal time the forcing integral is nondecreasing; passing
to its increasing all-time limit is legitimate. Thus, simultaneously in q,M,

\[
 E_n(q)\le C e^{K M}\left(q^{-1}+Z_n(M)\right)
                       \quad\hbox{on }G_n.
 \tag{7}
\]

The exponential here is in the chosen carrier cutoff M, not in sqrt(n).
No cancellation or independence of the actual gate error is asserted.

## 4. Fixed-cutoff finite-width transfer and one dense-only remainder

There exist C_0,c>0 such that for each fixed integer M and eta>0,

\[
 \Pr\{Z_n(M)>C_0e^{-cM^2}+\eta\}\longrightarrow0.
 \tag{8}
\]

The distinction between (8) and an assumed trained finite-network tail
theorem is essential. Here is the ordered-limit proof.

Fix M and a finite horizon T. Approximate the dense population by a fixed
Gaussian reference program on a fine time mesh, evaluated on the actual
initialized arrays. Its recomputed finite-list carrier moments and continuous
quadratic majorants of cutoff tails converge by the fixed-program theorem.
The dense population exponential-square bound controls each limiting tail
by C exp(-c M^2), with constants independent of T.

The actual dense finite flow is close to the affine reference parameters on
[0,T] by the previously proved one-reference comparison. Backward subtraction
at a separate auxiliary cutoff R bounds its carrier discrepancy by
C_T[(1+R)d+H_reference(R)], plus the time-mesh and program discrepancies.
The initialized action has bounded operator norm, so this also bounds the
initialized carriers k in RMS. First take width to infinity at the fixed
program, then refine that program and its mesh, and finally increase R.
The reference comparison has amplification exp(C_T R), which is dominated
by its Gaussian tail exp(-cR^2) for the fixed T. Hence the carrier mismatch
can be made arbitrarily small. The elementary inequality

\[
 \|u\mathbf1_{|u|>2M}\|_{\rm RMS}
 \le 2\|u-v\|_{\rm RMS}
       +2\|v\mathbf1_{|v|>M}\|_{\rm RMS}
\]

transfers the tail estimate to the actual dense carrier. Halving the fixed
cutoff only changes c. A finite time grid and the same preceding-node
comparison control the finite interval; no continuity of an indicator law
or quantitative convergence in width is needed.

The late interval has the deterministic bound

\[
 \int_T^\infty\rho_D(t)H_n(M,t)\,dt\le C e^{-\lambda T},
\]

uniform in n,M on G_n. Choose T large after fixing the desired tolerance,
and then use the preceding finite-program construction. This proves (8).
In particular the constants C_0,c do not grow with the physical horizon.

Now define the dense-only floor

\[
 a_n=\sup_{M\in\mathbb N,\ M\ge1}
             \bigl(Z_n(M)-C_0e^{-cM^2}\bigr)_+.
 \tag{9}
\]

It is bounded and measurable. To prove a_n->0 in probability, fix eta>0
and choose J with C_0 exp(-cJ^2)<eta/2. For M>=J, each positive excess in
(9) is at most Z_n(J), which is at most eta with probability tending to one
by (8). For the finitely many M<J, each excess tends to zero in probability
by (8). A finite union bound proves the assertion. This proves simultaneous
control in cutoff; it does not assume a quantitative uniform cutoff theorem.

## 5. Optimizing the cutoff

Equations (7)--(9) give

\[
 E_n(q)\le C e^{KM}\left(q^{-1}+a_n+C_0e^{-cM^2}\right).
 \tag{10}
\]

Put s=q^(-1)+a_n. Choose an integer M>=1 large enough that
C_0 exp(-cM^2)<=s. Rounding up costs only a fixed multiplicative constant;
one can take M<=C+C sqrt(log(e+1/s)). Substitution proves (1).
Since a_n is uniformly bounded, there is no large-s issue.

The factor exp(K sqrt(log(e+1/s))) decreases with s, so
Phi(x+y)<=Phi(x)+Phi(y) for nonnegative x,y. This proves (2) without claiming
that Phi itself is increasing everywhere. For gamma<1, on every fixed bounded
interval of s,

\[
 \Phi(s)/s^\gamma
 =s^{1-\gamma}\exp(K\sqrt{\log(e+1/s)})
\]

is bounded: as s tends to zero its logarithm tends to minus infinity, because
the negative term (1-gamma)log(s) dominates the square-root logarithm.
Finally (x+y)^gamma<=x^gamma+y^gamma proves (3).

## 6. What this says for slowly growing orders

For every deterministic q_n->infinity, (1) proves E_n(q_n)->0 in probability
on G_n; since Pr(G_n^c)->0, the same holds without conditioning. For example,
q_n=ceil(log(e+n)) gives the explicit decomposition

\[
 E_n(q_n)\le
 \frac{C}{\log(e+n)}\exp\!\left(K\sqrt{\log(e+\log(e+n))}\right)+b_n,
 \qquad b_n\to0\quad\hbox{in probability}.
 \tag{11}
\]

It is not valid to discard b_n or to assign it a Monte Carlo power of n.

There is also a nonconstructive but stronger joint-scaling consequence.
For any prescribed divergent cap r_n, one can choose deterministic integers
q_n->infinity with q_n<=r_n eventually such that, for each fixed 0<gamma<1,

\[
 \Pr\{E_n(q_n)>C_\gamma q_n^{-\gamma}\}\longrightarrow0.
 \tag{12}
\]

Indeed choose strictly increasing widths N_j so that, for every n>=N_j,
Pr(G_n^c or a_n>1/j)<=1/j and r_n>=j. This is possible by convergence in
probability and r_n->infinity. Put q_n=max{j:N_j<=n} after the first threshold.
On the resulting event of probability at least 1-1/q_n, a_n<=1/q_n, and
(3) proves (12), increasing the constant by a factor two. The same event
gives the rate simultaneously for every order 1<=q<=q_n.

Taking N_j>=j^4 permits q_n<=n^(1/4); a still slower prescribed cap is also
allowed. This does not prove that the explicit choice q_n=n^(1/4), log(n),
or log(log(n)) satisfies the pure power rate. Those choices all satisfy
(1)--(3) with their common vanishing width remainder. The selected schedule
in (12) may need to grow slower, and its width thresholds are not quantified.

### A confidence bound uniform over widths and simultaneous in order

Fix 0<delta<1. There is a deterministic decreasing sequence
alpha_N(delta)->0 satisfying

\[
 \sup_{n\ge N}\Pr\{a_n>\alpha_N(\delta)\}\le\delta.
 \tag{13}
\]

For an elementary construction, let D bound all a_n, choose increasing
N_j such that sup_(n>=N_j)Pr{a_n>1/j}<=delta, and set alpha_N=D before
N_1 and alpha_N=1/j for N_j<=N<N_(j+1). This is justified by a_n->0 in
probability and supplies the needed monotonicity. Initial repeated bounds
can be replaced by min(D,1/j) without changing the inequality.

The earlier deterministic estimate (6) of SMALL_LABEL_ALLTIME_SYNTHESIS.md,
with fixed labels absorbed into constants, reads

\[
 E_n(q)\le C q^{-1} e^{k\sqrt n}.
 \tag{14}
\]

Fix gamma in (0,1), choose a sufficiently small c_*>0, and put
N(q)=max(1,floor(c_* log^2(e+q))). For n<=N(q), choosing
k sqrt(c_*)<1-gamma in (14) proves E_n(q)<=C_gamma q^(-gamma).
A harmless adjustment covers bounded q and the max(1,...).

For any fixed n, on the single event a_n<=alpha_n(delta), every q with
n>N(q) satisfies a_n<=alpha_(N(q))(delta). Combine (3) in this region with
(14) in its complement. Thus, for every fixed gamma in (0,1),

\[
 \sup_{n\ge1}\Pr\left\{G_n\cap
  \left[\exists q\ge1:\ E_n(q)>
  C_\gamma\{q^{-\gamma}+\alpha_{N(q)}(\delta)^\gamma\}\right]\right\}
 \le\delta.
 \tag{15}
\]

This is a genuine width-independent confidence envelope, simultaneous over
all orders and physical times, and its right-hand error threshold tends to
zero with q. The unquantified dependence of alpha_N on N prevents a numerical
power-law order guarantee from being read into (15). The supremum of
probabilities is not an event asserting success jointly at all widths.

## 7. Prediction and scope

On any fixed bounded test-input set, forward subtraction and the common
all-time operator/readout bounds give sup_x|f_hat(t,x)-f_D(t,x)|<=C_test d_n(t).
Thus (1)--(3) and (12) also hold for the all-time supremum of test-prediction
discrepancy, test L2 discrepancy under any probability law supported there,
and the absolute difference of the two test RMSEs against a fixed
square-integrable target. These are errors relative to the dense predictor,
not a guarantee of small risk against the unknown target function.

This result strengthens the previous all-time qualitative statement by an
explicit order envelope and a dense-only width remainder. It is compatible
with the earlier exponential-order C/q certificate. It does not establish
a floor-free C/q rate for arbitrary width/order pairs, an explicit power of
n for the remainder, a rate for every prescribed slow schedule, a general-
activation version of the Gaussian transfer, or the joint-clock theorem.

## 8. Inputs and check status

The companion derivation SLOW_ORDER_GAUSSIAN_ROUTE.md develops the Gaussian
tail-transfer route. SLOW_ORDER_TRANSFER_ROUTE.md records a separate weaker
deduction from the earlier horizon-transfer estimates, its confidence
moduli, and a logical example showing why those transfer estimates alone
do not imply a polynomial rate. The new Gaussian argument uses additional
already-proved structure: all-time residual damping and uniformly sub-Gaussian
dense population carriers. It therefore does not contradict that example.

The coordinator read both complete companion derivations and checked the
deterministic damping/cutoff argument against the original energy estimate,
fixed-program and carrier-subtraction transfer against the Gaussian transport
proof, finite-head/tail quantifiers, integer-cutoff optimization, and diagonal
construction. The Gaussian-route author separately read this synthesis and
checked its core proof; both scoped authors checked the confidence-bound
quantifiers. Their clarification that the small-width branch needs only
C_gamma q^(-gamma), rather than an exact C/q branch, is incorporated above.
The check did not reopen every underlying book proof. These are internally
checked study deductions from the stated existing inputs, not independent
promotion reviews. No training, external search, Git mutation, or maintained
paper/book change is part of this continuation.
