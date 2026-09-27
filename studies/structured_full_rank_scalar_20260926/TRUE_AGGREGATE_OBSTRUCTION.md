# What would obstruct an effective aggregate closure?

2026-09-27. Scoped theoretical analysis. No experiments. The model input is
Sections 1–3 of `AGGREGATE_SCALAR_CONSTRUCTION.md`, specifically the population
equations (1)–(2); its histogram construction is not an admissible answer here.
All conclusions below concern a fixed memory order H, the canonical Gaussian
initial law with c(0)=0, and one fixed training task, unless a different
quantifier is stated explicitly. These are internally checked results, not
promoted book material.

**Conclusion.** No obstruction to the requested general, effective,
finite-time aggregate approximation follows from moment nonclosure, from
the size of a full polynomial basis, or from indistinguishable arbitrary
initial laws. There is a precise reason: the canonical problem supplies one
reachable orbit, and its existing scalar clock L separates distinct states
on that orbit. This does not give an admissible constructive closure: using
the unknown orbit to define the clock's right-hand side is trajectory
playback. A general approximation lower bound remains open. A genuine
restricted limitation is proved below: raw first moments alone cannot
predict even the initial learning response.

## 1. Contract and quantifiers

Write the population state as X=(mu,L), where mu is the law of

    z=(G,w,c,A_0,...,A_{H-1},B_0,...,B_{H-1}).

The block dimension is s_H=k^2+k(3+2mH). The proposed retained scalars are
ordinary statistics q_j=E_mu[psi_j(z)], possibly together with the existing
clock L and a finite number of explicitly justified shared scalars. The
surrogate must have an autonomous, restartable ODE and predict f(t,u) on
every fixed finite interval [0,T]. Its initialization and coefficients must
come from the specified model, training data and Gaussian initial law,
without a fitted or encoded future population trajectory. Histogram masses,
distribution representations, representative particles and Monte Carlo
population evolution are excluded.

The central unresolved question is an effective construction with an
observable error at most epsilon, width-independent state and work, and
usable dependence on epsilon, k, m, H and T. It is not exact closure for
every initial law. The statements involving the exact population below
assume its classical, unique solution exists on the interval in question
and has the moments being used. No global well-posedness theorem is claimed
in this note.

## 2. A quantitative obstruction requires predictive ambiguity

Here is the elementary lower-bound mechanism, with all its hypotheses
visible. Let Q(X) be an encoder into R^N, and O(X) a scalar observable.
Suppose two admissible states X_1,X_2 satisfy

\[
 \|Q(X_1)-Q(X_2)\|\le\eta,
 \qquad |O(X_1)-O(X_2)|=\Delta.
\]

For every decoder D with Lipschitz constant K_D,

\[
 \max_{i=1,2}|O(X_i)-D(Q(X_i))|
 \ge \frac{(\Delta-K_D\eta)_+}{2}.
 \tag{4}
\]

Indeed, inserting the two decoded values into the output difference and
using the triangle inequality gives Delta at most the sum of the two
errors plus K_D eta. For eta=0 the decoder needs no regularity assumption.

For a restartable autonomous surrogate with K_F-Lipschitz vector field,
initialized at Q(X_i), the same argument gives at a future time tau

\[
 \max_i |O(\Phi_\tau X_i)-\widehat O_i(\tau)|
 \ge
 \frac{(\Delta_\tau-K_D e^{K_F\tau}\eta)_+}{2},
 \quad
 \Delta_\tau=|O(\Phi_\tau X_1)-O(\Phi_\tau X_2)|.
 \tag{5}
\]

To verify the only extra step, the two surrogate trajectories satisfy
\(d\|\widehat q_1-\widehat q_2\|/dt\le
K_F\|\widehat q_1-\widehat q_2\|\) in the upper derivative sense;
multiplication by exp(-K_F t) and integration give their distance at most
exp(K_F tau) eta. The hypotheses need hold on the region traversed by both
surrogates. Both exact restarts must be admissible for the target problem.

Thus a negative result needs an actual pair of admissible reachable states,
a controlled encoder separation, a lower-bounded future observable gap,
and, when the separation is nonzero, a restriction on decoder and vector
field conditioning. A mere missing moment supplies none of these bounds.

### What arbitrary-law moment matching really establishes

For fixed functions psi_1,...,psi_N, pick finitely many block states x_i
and real weights v_i, not all zero, such that

\[
 \sum_i v_i=0,
 \qquad \sum_i v_i\psi_j(x_i)=0\quad(1\le j\le N).
\]

Such a nonzero vector always exists with N+2 nodes, by the dimension bound
for N+1 homogeneous linear equations. Put
s=sum_i (v_i)_+=sum_i (-v_i)_+>0 and define probability measures

\[
 \mu_+=s^{-1}\sum_i(v_i)_+\delta_{x_i},
 \qquad
 \mu_-=s^{-1}\sum_i(-v_i)_+\delta_{x_i}.
\]

They have identical retained statistics. If the desired additional
expectation is E_mu[g], every estimator of it from those statistics has
worst error at least

\[
 \frac{|\sum_i v_i g(x_i)|}{\sum_i|v_i|}.
 \tag{6}
\]

This is (4) applied to their expectation difference. A nonzero numerator
is an additional requirement; when g is close to the span of 1,psi_j,
the bound can be small. Specifically, for every a_0,...,a_N,

\[
 \frac{|\sum_i v_i g(x_i)|}{\sum_i|v_i|}
 \le \max_i|g(x_i)-a_0-\sum_j a_j\psi_j(x_i)|.
\]

Equation (6) is a valid quantitative theorem for a class containing both
constructed laws. It is not a theorem about the fixed canonical Gaussian
flow: the constructed laws have not been shown to occur on that orbit.
Replacing them by distributions merely sharing a few Gaussian moments
does not establish reachability either. Any lower bound for a larger
initial-law class must be labeled as such.

## 3. The existing clock separates the canonical reachable orbit

**Proposition.** For the exact block population trajectory, if
L(t_1)=L(t_2) with 0<=t_1<t_2<=T, then the full population state is constant
on [t_1,t_2]. Consequently the clock separates every pair of distinct
states on this one reachable orbit.

**Proof.** Equation (2) gives

\[
 L(t_2)-L(t_1)=\int_{t_1}^{t_2}\rho(t)\,dt,
 \qquad
 \rho(t)=\left(m^{-1}\sum_a r_a(t)^2\right)^{1/2}\ge0.
\]

Continuity and equality of the clock endpoints imply rho=0 throughout
the interval. Then every r_a=0. All right-hand sides in (2) vanish:
the w and c equations have a factor r_a; A has factors r_a or rho;
B has a factor rho; G is static; and L has derivative rho. Every block
characteristic, its law, and L are therefore constant there. QED.

There are two consequences with different logical force.

1. Once L is retained, exact collisions of aggregate states at distinct
   reachable population states cannot be obtained merely by choosing two
   times on the fixed canonical orbit. Arbitrary-law moment nonclosure
   cannot repair this missing premise of (5).
2. Abstractly, each reachable state and each observable can be written as
   a function of L along that orbit. Defining
   \(F(\ell)=\rho(t)\) and \(D_u(\ell)=f(t,u)\) whenever L(t)=ell
   is unambiguous, even on plateaus, by the proposition. Then
   \(\dot\ell=F(\ell),\ \widehat f(u)=D_u(\ell)\)
   reproduces the orbit in a formal sense.

The second statement is **not an admissible construction**: F and D_u are
defined using the unknown target orbit, and no allowed finite procedure,
description size, evaluation cost, or regularity bound has been provided.
It identifies why an unrestricted state-dimension argument cannot settle
the effective problem. The difficulty lies in computing and representing
the aggregate vector field without that orbit, not in the topological
dimension of a single deterministic trajectory.

The observation does not prove that L is a well-conditioned coordinate.
Near small residuals its rate can be very small. Bounds on the necessary
right-hand side and decoder complexity, or on close encoded states via
(5), could still produce a substantive restricted lower bound. Those
bounds are absent from a bare moment-counting argument.

## 4. An actual canonical limitation: first moments alone

This result concerns a specific restricted encoder. It supplies a genuine
observable approximation gap, rather than just a failure of exact closure.

For every H>=1, all coordinate means of G,w,c,A_j,B_j remain zero under
the canonical Gaussian initialization. To see this, consider two maps on
one block:

\[
 \mathcal S_1(G,w,c,A,B)=(-G,w,-c,-A,B),
\]
\[
 \mathcal S_2(G,w,c,A,B)=(G,-w,-c,-A,-B).
\]

Both preserve the prescribed initial law. Under S_1, h_1 and S_j stay
unchanged; z_2,h_2,delta_2 change sign; V_j stays unchanged; and delta_1
stays unchanged because both G and delta_2 change sign. Under S_2, h_1
changes sign and B changes sign, so S_j stays unchanged; z_2,h_2,delta_2
change sign; V_j stays unchanged; and delta_1 changes sign. In either
case c^T h_2, hence f,r,rho and L, stay unchanged. Substitution into (2)
therefore gives exactly the corresponding transformed velocity. Uniqueness
preserves both distributional symmetries. The first gives E[G]=E[c]=E[A]=0,
and the second gives E[w]=E[c]=E[A]=E[B]=0.

Nevertheless, take the fully specified nontrivial task

\[
 k=m=1,\qquad u_1=(1,0),\qquad y_1=1.
\]

Let X be the first coordinate of w(0) and let G denote the scalar middle
block. They are independent standard Gaussians. At time zero A=c=0, so

\[
 h_2(0,u_1)=v:=\tanh(G\tanh X),\qquad
 \dot c(0)=2v.
\]

Since f=E[c h_2], differentiating at zero gives

\[
 f(0,u_1)=0,\qquad
 \partial_t f(0,u_1)=2\kappa,
 \quad \kappa=E[\tanh^2(G\tanh X)]>0.
 \tag{7}
\]

This differentiation does not require a bound on the derivative of h_2.
Indeed c(t)/t tends pointwise to 2v, h_2(t,u_1) tends to v and |h_2|<=1.
The integral equation for c gives |c(t)|/t bounded uniformly over blocks
on a sufficiently short time interval because the shared residual is
continuous and bounded there. Dominated convergence then proves (7).

There is even an explicit elementary positive bound:

\[
 \kappa\ge
 \Pr(|G|\ge1)\Pr(|X|\ge1)\tanh^2(\tanh1)
 \ge \frac{2e^{-4}}{\pi}\tanh^2(\tanh1).
 \tag{8}
\]

For the last inequality, for a standard Gaussian Z,
\(\Pr(|Z|\ge1)\ge2\int_1^2(2\pi)^{-1/2}e^{-x^2/2}dx
\ge\sqrt{2/\pi}\,e^{-2}\).

If the retained state consists only of these exact coordinate means, and
the output decoder is a time-independent function of them, its predicted
output is a single constant. Equation (4), applied to times 0 and T,
therefore implies

\[
 \sup_{0\le t\le T}|f(t,u_1)-\widehat f(t,u_1)|
 \ge\tfrac12|f(T,u_1)|.
 \tag{9}
\]

By (7), there exists T_0>0 such that for every 0<T<=T_0 the lower bound
is at least kappa T/2; equivalently its small-T leading lower bound is
kappa T+o(T). Equation (8) makes the coefficient explicit. No explicit
numerical lower bound on T_0 is established here.

If approximate mean states remain within eta of the true zero vector and
the decoder is K_D-Lipschitz, the same proof gives
\((|f(T,u_1)|-2K_D\eta)_+/2\).

**Scope.** This rules out first-moment-only decoding with a vanishing
error at fixed such T. It does not rule out Gram statistics, mixed
statistics, a decoder that also uses L, or any of the user's broader
allowed classes. In particular E[c h_2] is already a mixed observable
that distinguishes the predictions. Its evolution may require further
statistics, but that additional issue is not resolved by (9).

## 5. Two further invalid upgrades to a general no-go

### Exact nonclosure is not a quantitative approximation obstruction

An unclosed term must be bounded in size and in its propagated effect on
the chosen observable. A nonzero instantaneous residual by itself does
not imply a fixed error: the scalar curve

\[
 q(t)=\frac{\delta}{\omega}(1-\cos\omega t)
\]

has derivative residual delta sin(omega t) relative to the zero vector
field, while its uniform error from the zero surrogate is at most
2 delta/omega. This elementary example is a logical check, not a proposed
replacement for the block model. Within the block model, a lower-bound
proof must still establish noncancelling, observable-relevant error
production and its persistence on the canonical reachable orbit.

### A full basis count does not settle accuracy cost

For fixed instantaneous state dimension s_H, the number of all monomials
of degree at most d is

\[
 N(d)=\binom{s_H+d}{d}=O_{s_H}(d^{s_H}).
\]

This counts one particular representation. It does not lower-bound the
number of adaptive functions, structured contractions or other ordinary
statistics needed to predict the selected outputs. Even for that
representation, an established error rate d^{-r} would yield a polynomial
accuracy count O(epsilon^{-s_H/r}); an established exponential rate in d
would yield a polylogarithmic count for fixed s_H. Neither convergence
rate is asserted here. The exponent and constants may make the count
unusable in k,m,H, which is a separate issue from impossibility.

If H=d=P, then s_H=a+bP with a=k^2+3k and b=2km, and

\[
 \binom{a+(b+1)P}{P}
 \le [e(a+b+1)]^P\qquad(P\ge1).
\]

Exponential state growth in P alone still does not imply superpolynomial
growth in 1/epsilon: if an independent theorem supplied error exp(-cP),
this displayed upper bound would be polynomial in 1/epsilon. Conversely,
without a rate theorem, a basis count does not establish a usable positive
result either. It is necessary to connect the count to a verified
observable error estimate at the same approximation order.

## 6. Remaining decisive obligation

A broad negative result must formalize the admissible function class and
its computational complexity, then establish a lower bound within that
class for the canonical orbit. Merely saying that coefficients depend on
the model and data is insufficient: solving the entire target trajectory
offline also formally depends only on the model and data. The intended
prohibition of such work must be reflected in allowable coefficient
construction, preprocessing work, right-hand-side evaluation, decoder
evaluation and numerical precision, not just the number of real state
coordinates.

Useful possible claims would be a lower bound for a specified bounded
degree aggregate family, a bounded contraction-order family, or a
uniformly conditioned family with bounded coefficient description and
evaluation complexity. Each would need a concrete canonical-flow
approximation gap, not an arbitrary-law moment witness. None is proved
by the generic observations audited here.

The present status is therefore:

- **Proved:** the quantitative ambiguity lemmas (4)–(6), the clock
  separation proposition, and the canonical first-moment limitation
  (7)–(9), each with its stated scope.
- **Rejected as an inference:** exact moment nonclosure, arbitrary-law
  indistinguishability, or full polynomial-basis size alone imply failure
  of effective approximate aggregates on the fixed canonical Gaussian
  task.
- **Open:** whether the permitted richer aggregates admit a practical
  width-independent polynomial-accuracy construction, or obey a matching
  effective-complexity lower bound.
