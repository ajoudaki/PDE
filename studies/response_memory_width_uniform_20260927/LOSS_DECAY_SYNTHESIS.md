# When does the closure have finite total learning activity?

28 September 2026. Continuation of the time-uniformity question in this study.
This is an internally checked theoretical result, not a promoted theorem.
The inputs are the current manuscript, this study's old-clock estimates, and
the two scoped derivations linked below. No new training was run.

## Answer and scope

Input separation and realizability alone do not guarantee fitting for every
initialization or every finite closure. The explicit orthogonal-data example
in [LOSS_DECAY_OBSTRUCTION.md](LOSS_DECAY_OBSTRUCTION.md) has constant positive
loss for every order. Its hidden matrices are invertible and its data are
exactly realizable by the same architecture.

That example is exceptional under Gaussian initialization. It does not settle
the intended high-probability or population question. The positive result of
this turn goes further in that direction:

For fixed nonzero inputs with no two proportional, fixed depth, canonical
independent Gaussian initialization and tanh, there is a positive,
width-independent label-size threshold such that, with probability tending
to one as width increases, **every old-clock order P >= 1** has vanishing
training loss and bounded total residual RMS activity, uniformly in width
and order. This is a small-label theorem, not an arbitrary-label theorem.

The deterministic activity proof, including its constants and the small
nonzero-readout extension, is in
[LOSS_DECAY_ACTIVITY_BOOTSTRAP.md](LOSS_DECAY_ACTIVITY_BOOTSTRAP.md).
The initial Gaussian Gram statement needed to apply it is proved here.

## 1. Initial population features separate nonparallel inputs

Let v_a=x_a/sqrt(d), a=1,...,m. Assume d>=2, all v_a are nonzero,
and v_a is not a scalar multiple of v_b for a!=b. In particular this
excludes parallel and antiparallel pairs. No quantitative angular lower
bound is needed for the qualitative conclusion at fixed data.

Define the initial covariance matrices recursively by

\[
 Q^{(1)}_{ab}
 =\mathbb E_{g\sim N(0,I_d)}
       [\tanh(g^\top v_a)\tanh(g^\top v_b)],
 \qquad
 Q^{(\ell)}_{ab}
 =\mathbb E_{Z\sim N(0,Q^{(\ell-1)})}
       [\tanh Z_a\tanh Z_b].
 \tag{1}
\]

Each Q^(ell) is strictly positive definite.

**First layer.** Suppose c^T Q^(1)c=0. The nonnegative integrand implies
sum_a c_a tanh(g^T v_a)=0 for almost every Gaussian g. The function is
continuous and Gaussian measure has full support, so it vanishes for every
g in R^d. Replacing g by Rg and letting R grow gives

\[
 \sum_a c_a\operatorname{sign}(g^\top v_a)=0
 \tag{2}
\]

whenever none of the inner products is zero.

Fix an index a. Inside the hyperplane v_a^perp, each other hyperplane
v_b^perp cuts a proper linear subspace: otherwise v_b would be proportional
to v_a. A finite union of proper linear subspaces cannot exhaust v_a^perp.
Choose g_* in this hyperplane outside all the others. Moving a sufficiently
small distance from g_* to its two sides changes only the a-th sign in (2).
Subtracting those two equations gives 2c_a=0. This works for every a, hence
c=0 and Q^(1) is positive definite.

**Higher layers.** If Q^(ell-1) is positive definite, Z has full support
in R^m. A null vector of Q^(ell) would imply
sum_a c_a tanh(z_a)=0 for all z. Set every coordinate except z_a to zero
and vary z_a. Then c_a=0. Induction completes the proof. For a single
nonzero input the same conclusion is immediate, including in dimension one.

This proof concerns the initialized feature covariance. It does not claim
that its smallest eigenvalue remains bounded below during arbitrary training.

## 2. The finite-width initial Gram converges to this matrix

Let H_ell be the n by m matrix of initialized hidden responses, with
samples as columns, under the manuscript's independent Gaussian
initialization. Define Q_n^(ell)=H_ell^T H_ell/n.

At the first layer its rows are independent and identically distributed,
and their entries have absolute value at most one. For every a,b the
variance of (Q_n^(1))_(ab) is at most 1/n. Chebyshev's inequality and a
union bound over the fixed m^2 entries prove Q_n^(1) -> Q^(1) in
probability, also in operator norm.

Condition on H_(ell-1). Because the new weight matrix is independent and
has entries N(0,1/n), the rows of its preactivation matrix are independent
N(0,Q_n^(ell-1)) vectors. The same conditional variance bound shows

\[
 Q_n^{(\ell)}-\mathcal T(Q_n^{(\ell-1)})
 \longrightarrow0
 \quad\text{in probability},\qquad
 \mathcal T(Q)_{ab}=\mathbb E[\tanh Z_a\tanh Z_b],\
 Z\sim N(0,Q).
 \tag{3}
\]

The map T is continuous on positive semidefinite matrices: couple
Z=Q^(1/2)G using one standard Gaussian G, use continuity of the matrix
square root and tanh, and then bounded convergence. Induction in the fixed
number of layers proves Q_n^(L) -> Q^(L) in probability.

The readout contribution to the canonical gradient-flow Gram is

\[
 \Gamma_{w,n}(0)=\frac{H_L^\top H_L}{mn},\qquad
 \lambda_*=\lambda_{\min}(Q^{(L)}/m)>0.
 \tag{4}
\]

The eigenvalue inequality
|lambda_min(A)-lambda_min(B)| <= ||A-B||_op gives

\[
 \Pr\{\lambda_{\min}(\Gamma_{w,n}(0))\ge\lambda_*/2\}
 \longrightarrow1.
 \tag{5}
\]

No independence of neurons after training, Monte Carlo approximation of a
trained population, or exchange of training-time limits was used.

## 3. Width-independent initialization events

For completeness, the initialized hidden operator norms are bounded with
probability tending to one. For an n by n matrix W with independent
N(0,1/n) entries, fix 1/4-nets of the two unit spheres. A maximal separated
set and the disjoint-ball volume argument give nets of size at most 9^n.
Approximating both vectors in the bilinear form gives
||W||_op <= 2 max_(u,v in nets)|u^T Wv|. Each such bilinear form is
N(0,1/n), so the Gaussian exponential bound and a union bound yield

\[
 \Pr\{\|W\|_{\rm op}>K\}
 \le 2\exp(2n\log 9-nK^2/8).
 \tag{6}
\]

In particular K=10 works, simultaneously for all the finitely many hidden
links with probability tending to one.

For the stored readout convention w_(0,i)~N(0,n^-2), put
B_0=||w_0||_2/sqrt(n). Then E B_0^2=n^-2. For any fixed positive
Y=||y||_m, Markov's inequality gives

\[
 \Pr\{B_0>Y\}\le\frac1{n^2Y^2}.
 \tag{7}
\]

Consequently the event

\[
 \lambda_{\min}(\Gamma_{w,n}(0))\ge\lambda_*/2,\qquad
 \max_{\ell\ge2}\|W_0^{(\ell)}\|_{\rm op}\le10,\qquad B_0\le Y
 \tag{8}
\]

has probability tending to one. No independence between these three events
is needed.

## 4. Gaussian all-order, small-label fitting theorem

Fix the above data and depth. Set lambda_0=lambda_*/2 and K=10.
The deterministic activity theorem supplies a number
Y_*>0 depending only on these constants, depth and
X=max_a ||x_a||/sqrt(d), with the following property.
For any fixed labels with 0<Y=||y||_m<=Y_*, on event (8) the original
autonomous old-clock closure satisfies, simultaneously for every P>=1,

\[
 \int_0^\infty\rho_{n,P}(t)\,dt
 \le \frac{3Y}{\lambda_0},\qquad
 \rho_{n,P}(t)\longrightarrow0,\qquad
 \sup_{t\ge0}\tau_{n,P}(t)\le1+\frac{3Y}{\lambda_0}.
 \tag{9}
\]

Its physical parameters converge to an interpolating limit. The accumulated
absolute memory-velocity defect also satisfies

\[
 \int_0^\infty
       \sum_{\ell=2}^L\|E_{\ell,n,P}(t)\|_F\,dt
 \le \frac{C(4Y/\lambda_0)}{\sqrt{P(P+1)}},
 \tag{10}
\]

Here C is the common deterministic majorant obtained from the activity
note's Section 2 recursions by setting B_0=Y and every K_ell=10.
All those recursions are nondecreasing in these nonnegative inputs, so
this one C bounds every realization on (8); it has no width or order
dependence.
For an exactly zero initialized readout, the deterministic theorem improves
(9)'s activity bound to 3Y/(2 lambda_0).

To see the mechanism, stop when activity reaches S=4Y/lambda_0. The
old-clock estimates show that the hidden Gram drift is O(S^2), the
integrated weight-velocity defect is O(S^3/P), and its contribution to the
residual equation is O(S^4/P). Taking Y small keeps the top Gram at least
lambda_0/2 and the integrated residual perturbation at most Y.
The initial residual is at most 2Y, so the integrated residual equation
gives activity at most 3Y/lambda_0=3S/4. This excludes the first exit.
The full inequalities and continuation argument are in the activity note.

The conclusion is integrability of residual RMS, precisely the decay
condition needed to stop the old clock at a finite limit. It is stronger
than merely asserting loss -> 0. It does not assert exponential decay.
The case y=0,w_0=0 is stationary with zero loss; the theorem above makes
no extra claim about a nonzero readout and exactly zero labels.

## 5. What remains unresolved

The small-label restriction is substantive. Scaling labels changes the
network's feature-learning trajectory, so it cannot be removed by declaring
it a normalization convention. At arbitrary label sizes, the present
argument does not keep the top-feature Gram positive along training.

A second positive result in the activity note says that, at fixed width,
if dense flow converges to an interpolating parameter state with strictly
positive readout Gram, then every sufficiently high closure order also
fits and has finite activity. It proves closure decay rather than assuming
it, but its dense regular-fit hypothesis and sufficient-order threshold are
not consequences of input separation alone.

Neither result proves that every fixed order fits arbitrary compatible
labels under Gaussian initialization, nor that the original joint clock
has finite total length. For that clock, integrable residual alone does
not automatically control its additional response-variation contribution.
The arguments here concern the actual old-clock closure.

Finite total activity and (10) settle two ingredients of an all-time
approximation theorem. They do not themselves settle width-uniform
feedback stability. A bound such as exp(H integral(rho_dense+rho_closure))
still requires a justified, width-uniform H in the state norm being used.
The current study has not proved that bound for general Gaussian deep
training. This note must not be used to claim a completed unrestricted
all-time tracking theorem.

## 6. The saddle question does not replace the activity argument

The stationary example in the obstruction note is a strict saddle.
With its symmetric matrix H_0, label vector y=(2,-1)^T and H_0 y=0, put

\[
 H_\epsilon=H_0+\epsilon I_2,\qquad
 W_{1,\epsilon}=Q(H_\epsilon)\ \text{entrywise},\qquad
 W_{2,\epsilon}=I_2,\qquad w_\epsilon=2\epsilon y,
 \tag{11}
\]

where Q(s)=atanh(atanh(s)). For sufficiently small epsilon all its
arguments remain in the domain of this smooth inverse map. The actual
top features are exactly H_epsilon, hence

\[
 f_\epsilon=\epsilon H_\epsilon^\top y=\epsilon^2y,\qquad
 \mathcal L_\epsilon=(1-\epsilon^2)^2\mathcal L_0<\mathcal L_0
 \quad(0<|\epsilon|\text{ sufficiently small}).
 \tag{12}
\]

At the critical base point, the second derivative of this loss along
the smooth path equals the parameter Hessian quadratic form in its
initial tangent. It is -4 L_0=-10. Thus negative curvature is already
present at second order. A pure readout variation outside ker(H_0^T)
has positive curvature as well.

There is also a broader zero-readout observation. For an analytic tanh
network, if the labels are realizable and nonzero, no zero-readout
parameter point can be a local minimum. Let v collect the hidden
parameters and H(v) their top-feature matrix. The analytic vector
c(v)=H(v)y is not identically zero: at an interpolator (v_*,w_*),
w_*^T H(v_*)y=n||y||_2^2>0. A real analytic function that vanishes on
an open ball vanishes on its connected domain (continue its zero
power series along overlapping balls). Therefore every neighborhood of
any v_0 contains a v with c(v)!=0. At that v, take w=eta c(v).
The loss difference from the original zero-readout value is exactly

\[
 \mathcal L(v,\eta c(v))-\|y\|_m^2
 =-\frac{2\eta}{mn}\|c(v)\|_2^2
   +\frac{\eta^2}{mn^2}\|H(v)^\top c(v)\|_2^2.
 \tag{13}
\]

For sufficiently small positive eta this is negative, and w can
simultaneously be made arbitrarily small. This proves the claimed
zero-readout statement, including cases where the first descending
perturbation appears beyond second order. It is not a theorem excluding
all positive-loss local minima at arbitrary nonzero readouts.

Even eliminating every positive-loss critical point would not establish
the required residual integrability. The scalar least-squares loss
L(z)=z^4 has only its zero-loss global minimum as a critical point, but
its gradient flow from z_0!=0 is

\[
 z(t)=\frac{z_0}{\sqrt{1+8z_0^2t}},\qquad
 \sqrt{\mathcal L(t)}=\frac{z_0^2}{1+8z_0^2t},\qquad
 \int_0^\infty\sqrt{\mathcal L(t)}\,dt=\infty.
 \tag{14}
\]

This is a logical counterexample to inferring finite activity from loss
landscape topology alone, not a claim that this scalar flow is the neural
closure. The feature-Gram and integrated-defect argument above directly
addresses the stronger quantity required by the old clock.
