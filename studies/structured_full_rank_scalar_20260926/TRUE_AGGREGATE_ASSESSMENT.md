# Aggregate-only compression: correction, new results, and unresolved efficiency

2026-09-27. Theory-only continuation of this study. No training runs, new
numerical experiments, book promotion, or Git writes were performed.

## Answer to the actual request

An effective aggregate-only approximation of the Gaussian-block population
closure has **not** been established. The previous histogram and moving-block
methods do not answer that request, and their numerical results must not be
presented as evidence that it has been achieved. A general impossibility
theorem has not been established either.

There is a substantive positive result from the present correction: a family
of directly evolved, observable-dependent moment contractions approximates
the model with bounded initial G on any prescribed finite horizon and
finite input panel. It has an algebraic observable-error bound versus scalar
state count at fixed parameters. This family neither evolves representatives
nor reconstructs a density. Its constants do not presently establish useful
efficiency for the actual Gaussian law, large block sizes, or the entire
circle. It is therefore a restricted theorem, not a completed solution to
the user's problem.

## 1. What counts as compression here

Fix block size k, memory order H, and m training samples. At original width
n=Nk, each initialization block G is k by k with independent N(0,1/k)
entries. Each block carries current first weights w, readout c, and memory
vectors A_j,B_j for j<H. The blocks interact through population averages.
The exact equations and canonical normalization are in sections 1–2 of
[AGGREGATE_SCALAR_CONSTRUCTION.md](AGGREGATE_SCALAR_CONSTRUCTION.md). Its
later histogram sections are not used by the new construction.

Allowed states are directly specified statistics such as

\[
 q_a=\mathbb E\left[\frac1k\sum_\alpha c_\alpha h_{2,\alpha}(u_a)\right],
 \qquad
 q_{ab}=\mathbb E\left[\frac1k\sum_i h_{1,i}(u_a)h_{1,i}(u_b)\right],
\]

and mixed contractions involving G, its actual transpose, current responses,
and current memories. The first displayed statistic is the network output.
The expectation is over the current block law; this notation does not mean
that the numerical solver stores that law.

The finite solver must initialize its statistics from the given initial law
and then evolve them autonomously. It may not maintain neurons, histogram
masses, density coefficients reconstructed at runtime, initial-label fields,
or a prerecorded future target trajectory. An invertible recoding of those
representations as numbers called moments is not additional compression.

A genuine moment hierarchy is not disqualified merely because its infinite
sequence could determine a probability law. The operational questions are
whether its finite equations directly evolve selected statistics, and what
observable error and total computation those equations guarantee.

## 2. A genuine positive construction for bounded initialization

The complete construction and proof are in
[TRUE_AGGREGATE_CONSTRUCTIVE.md](TRUE_AGGREGATE_CONSTRUCTIVE.md). Its final
extension, section 11, conditions G to a finite box and permits the full
Gaussian law of w(0). This is not the unbounded Gaussian law for G. The
proof uses tanh and a fixed finite panel of training and passive query
inputs. One unchanged family of ODEs converges on every prescribed finite
horizon; only the error constants depend on that horizon.

### Exact hierarchy

Lift the current activations into local variables. Since
\(\tanh'=1-\tanh^2\), their derivatives, the readout derivatives, and the
memory derivatives are polynomials in the lifted local coordinates, with
coefficients determined by a fixed list of scalar averages and the clock.
The derivative of every shared forward overlap is included; it is not
silently frozen.

Start from the contractions defining the desired outputs and the feedback.
Differentiating one factor replaces it by finitely many local factors and
forward/backward matrix contractions. These operations generate decorated
bipartite trees: edges are entries of G and vertices carry current response
or memory factors. Numerical index collisions are included in each sum.
Consequently the construction preserves G/G-transpose reuse.

For the final construction, use the existing clock to normalize the current
local fields as c/(2L), A_j/(sqrt(m)L^2), and B_j/L. The exact Legendre
history identities imply that all these coordinates have magnitude at most
one at every time, for every memory order. Normalize G by its fixed bound.
Normalize each tree contraction as an average of products of these fields,
so that its absolute value is at most one. Its expected value is one scalar
q_gamma.
Trees of degree at most R obey an exact hierarchy of the form

\[
 \dot q_\gamma
   =\sum_\eta a_{\gamma\eta}(q_{\rm low},1/L)q_\eta,
 \qquad \deg\eta\le\deg\gamma+10.
\]

Only moments of degree at most nine are needed inside the coefficients.
For fixed bounded-model parameters, the absolute coefficient sum and its
Lipschitz bound grow at most linearly with the degree of gamma. The number
of listed tree statistics is at most B^(R+1), where B depends on memory
order and the number of input colors. This count does not involve original
width. Block size enters the coefficient and error constants.

### Finite autonomous ODE and the role of boundedness

Retain trees through degree R and set omitted children to zero. In the
right-hand side, project every retained approximate moment to [-1,1]. Add
an outward penalty -a(1/L) deg(gamma)(qhat_gamma-clip(qhat_gamma)), with an
explicit coefficient envelope for the normalized equations. This gives
a locally Lipschitz autonomous ODE with invariant bounds |qhat_gamma|<=2.
Its state need not be realizable as the moments of any probability law;
no probability law is reconstructed. Projection and the penalty leave the
exact physical moments unchanged in the untruncated hierarchy.

The boundedness is a mathematical component of the approximation, not an
assumption that high-order moments are small. The discrepancy at the
truncation boundary may remain order one. Its influence on low-degree
observables is controlled by the number of differentiation steps needed
to reach them.

In particular, degree-wise errors satisfy an integral comparison of the
form

\[
 E_d(t)\le E_d(t_0)
    +a d\int_{t_0}^t E_{d+10}(s)\,ds
    +b d\int_{t_0}^t E_9(s)\,ds.
\]

On a sufficiently short interval, iterating this inequality yields an
exponentially small boundary influence on degrees well below R. The proof
then repeats that estimate on finitely many intervals, using only a smaller
fraction of available degrees at each step. The ODE is never reset and no
new population information is supplied between intervals.

This establishes, for the fixed bounded model,

\[
 \max_a\sup_{t\le T}|\widehat f_R(t,u_a)-f(t,u_a)|
       \le C_T e^{-c_T R},\qquad c_T>0.
\]

Together with the exponential state count, this gives an algebraic
error-versus-state-count bound for the prescribed sequence. It also bounds
training-loss discrepancy. The constants can be extremely unfavorable. The
final clock normalization removes the horizon-dependent coefficients used
in the initial proof: the same autonomous ODE applies for all times, while
the finite-horizon analysis controls its inverse-clock coefficients using
a positive lower bound on 1/L. This is a derived construction, not a tested
implementation.

This is stronger than exact moment identities or a local Taylor expansion.
It is weaker than useful compression for the Gaussian target.

### Why this is not naive moment truncation

A bounded true trajectory alone does not make ordinary truncation converge
globally. For example, x'=-x^2 with x(0)=1 has exact moments M_j=x^j and
M_j'=-j M_{j+1}. Setting M_{R+1}=0 gives

\[
 \widehat M_1(t)=\sum_{j=0}^{R-1}(-t)^j,
 \qquad
 |\widehat M_1(t)-x(t)|=\frac{t^R}{1+t}.
\]

It diverges as R grows whenever t>1, despite the bounded exact solution.
This refutes that particular truncation, not moment compression generally.
The bounded finite-propagation argument above supplies the ingredient that
this naive truncation lacks.

## 3. Why the Gaussian claim still does not follow

The bounded theorem has an accuracy cost schematically of the form

\[
 N(\varepsilon,R_0)\lesssim
       A(R_0)\varepsilon^{-p(R_0)},
\]

where R_0 denotes the cutoff on G. Recovering Gaussian initialization
requires increasing R_0 as accuracy improves. Even a cutoff of order
sqrt(log(1/epsilon)) makes the exponent p(R_0) depend on epsilon if the
proved constants deteriorate with R_0. A polynomial result at each fixed
cutoff is therefore not a polynomial result for the Gaussian problem.
The present proof has precisely this deterioration. This is a limitation
of the bound, not a proof that the actual approximation must fail.

Other costs remain visible. Tree expectations at initialization are known
finite integrals; an individual tree can be evaluated by leaf elimination
in O(k^2 R) work at a given initial block. However, straightforward certified
quadrature of all those expectations retains a k^2+2k-dimensional cost.
The fixed-panel theorem also does not provide an arbitrary-input decoder.
A proposed Fourier extension has not been proved and is not counted as a
solution here.

Thus the current construction supplies genuine aggregate coordinates and a
restricted finite-time theorem, but not a justified small numerical model.
No new experiment has been run to imply otherwise.

## 4. A concrete obstruction to a Gaussian-state shortcut

[TRUE_AGGREGATE_GAUSSIAN.md](TRUE_AGGREGATE_GAUSSIAN.md) proves an actual
Gaussian-initialized, feature-learning calculation, valid for every memory
order. Use one nonzero label y and one input u. Write a_j=w_j(0)u,
h_j=tanh(a_j), Q=k^(-1)sum_j h_j^2, and

\[
 \psi(z)=\tanh z\,\operatorname{sech}^2z,
 \qquad \chi(Q)=\mathbb E[\psi'(\sqrt Q Z)],\quad Z\sim N(0,1).
\]

Canonical initialization has c(0)=0. Direct differentiation and Gaussian
integration by parts give

\[
 \mathbb E[w_j''(0)\mid w(0)]
    =4y^2\operatorname{sech}^2(a_j)\,u\,h_j\chi(Q).
\]

The 1/k factor from Gaussian integration by parts cancels against a sum
over k rows. The response is order one. Treating the reused transpose as
independent of its current backward response would delete this term.

There is a stronger test of the proposed Gaussian simplification. Let
a_j(t)=w_j(t)u and

\[
 \kappa_4(t)=\mathbb E[a_j(t)^4]
                -3\mathbb E[a_j(t)^2]^2.
\]

For every nonzero input, including a unit-circle input,
\(\kappa_4(0)=\kappa_4'(0)=0\) but \(\kappa_4''(0)<0\), with a strictly
negative bound independent of k. This follows from the fact that
g(a)=tanh(a)sech^2(a)/a is positive and strictly decreasing in |a|,
and chi(Q)=E[Z^2 g(sqrt(Q)Z)] is positive and decreasing. A size-biased
Gaussian covariance identity gives the sign and the k-uniform bound.

Thus current first-layer preactivations do not remain Gaussian even at
the leading feature-learning order. This does not merely note that tanh
of a Gaussian is non-Gaussian. It rules out using initialization Gaussianity
alone to set all current higher cumulants to zero. No uniform-in-k
positive-time Taylor remainder or general output-error lower bound is
claimed from this derivative calculation.

## 5. Why this still is not an impossibility theorem

The user permits an increasing sequence of genuine aggregate statistics.
Nonzero higher cumulants do not prevent such a sequence from converging.
Neither exact nonclosure nor failure of a specific Gaussian or mean-only
ansatz demonstrates an error floor for all richer aggregate systems.

[TRUE_AGGREGATE_OBSTRUCTION.md](TRUE_AGGREGATE_OBSTRUCTION.md) makes the
lower-bound obligation precise. A chosen encoder must fail to distinguish
admissible states whose future target outputs differ, or a quantified
computational/algebraic restriction must force approximation error on the
canonical reachable trajectories. Arbitrary probability laws with matched
moments are not enough: they have not been shown to arise in this problem.

In fact the existing clock separates distinct states on one fixed canonical
orbit: equality of L at two times implies zero residual throughout the
intervening interval and therefore no evolution. This observation does not
provide a scalar solver, because defining its coefficients from that unknown
orbit would be prohibited trajectory playback. It does explain why a bare
information-dimension argument cannot settle the effective question.

## 6. Current judgment and evidence status

The Gaussian-block change removes one obstacle: it turns the initialized
matrix action into a local finite-dimensional block operation. It does not
by itself eliminate the nonlinear response correlations inside those blocks.
The former claim that this change essentially completed scalar compression
was unsupported.

The new bounded-moment construction is a genuine aggregate route and gives
reason not to infer impossibility. It does not justify claiming that a
small set of such aggregates will be accurate for the tested Gaussian
tasks. The decisive unresolved issue is controlling low-observable error
with useful cost for the unbounded Gaussian model, including initialization
and queries. The requested complete resolution remains open.

The new results are author derivations with internal cross-checks, not
established book results or independent promotion reviews. The constructive
note and its separate internal audit carry the detailed assumptions and
proof. Historical histogram and moving-population results are preserved
only as evidence about the methods actually tested.
