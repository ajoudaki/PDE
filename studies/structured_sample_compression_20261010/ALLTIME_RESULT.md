# Attempt at the general all-time sample-compression theorem

2026-10-10. Continuation explicitly requested by the user. The target is an
initialization-only, autonomous, sample-compressed version of the actual
Gaussian deep feature-learning flow, retaining the original activation class
(unbounded values permitted), fixed nonzero label scale, full training horizon,
and the methods' respective query domains. Fixed and moving storage count.
The desired new structural factor must not merely rename m/gamma or assume
the approximation property of the future trajectory.

## Bottom line

The requested general, sharp, unconditional compression theorem has not
been established. In particular there is no justified replacement of m by
a latent dimension, label bandwidth, or effective rank in the paper's three
storage formulas. No paper result or scope has been changed.

This attempt does establish two useful initial-data sufficient certificates
for all-time nonlinear training, a gap-free dissipative comparison lemma,
and genuine deep-network counterexamples to absolute geometric/quadrature
stability. The certificates do not yet have sample-uniform bounds derived
from the proposed smooth-label or latent-data hypotheses. The counterexamples
are not impossibility results for sample compression.

## 1. An initial source can replace the worst eigenvalue in an activity estimate

Use the canonical network and mobility-normalized parameter tuple from
THIRD_AXIS. Write J_theta for its prediction derivative, with Euclidean
parameter norm and normalized empirical sample norm. Its adjoint includes
the empirical factor 1/m. Define A(theta)=J_theta J_theta^*; at zero-readout
initialization its entries are h_a(0)^T h_b(0)/(nm). Then exactly

\[
 \dot r=-2A(\theta)r,\qquad
 \dot\theta=-2J_\theta^*r,\qquad
 -\partial_t\|r\|_m^2=\|\dot\theta\|^2.
\]

Assume the realized A_0 is positive definite. In one fixed empirical
orthonormal eigenbasis, write its eigenvalues as lambda_j and label
coefficients as y_j. Fix a radius R around the initialized parameters and
define the following static quantities:

\[
 S=\sum_j\frac{|y_j|}{\lambda_j},\qquad
 B_R=\sup_{\|\theta-\theta_0\|\le R}\|J_\theta\|,
\]
\[
 \eta_R=\sup_{\|\theta-\theta_0\|\le R}
 \max_j\sum_i
 \frac{|\langle e_i,(A(\theta)-A_0)e_j\rangle_m|}{\lambda_i}.
\]

If eta_R<1 and B_R S/(1-eta_R)<R, the actual nonlinear flow is global,
fits, converges in parameter space and satisfies

\[
 \int_0^\infty\|r(t)\|_m\,dt
 \le\frac{S}{2(1-\eta_R)},\qquad
 \int_0^\infty\|\dot\theta(t)\|\,dt
 \le\frac{B_RS}{1-\eta_R}.
\]

This statement does not assume future trajectory behavior. Its proof uses
the weighted absolute residual potential sum_j |r_j|/lambda_j, whose
upper derivative is at most -2(1-eta_R)sum_j|r_j|. The resulting path bound
prevents exit from the initial ball. Smoothness gives global continuation;
finite path length gives a parameter limit, and integrable residual norm
forces its residual to be zero. The complete argument is in
ALLTIME_SOURCE_ROUTE, Section 3.

The useful mechanism is that the label's actual modal coefficients enter
S, rather than every coefficient being charged the smallest eigenvalue.
At this zero-readout initialization, positive definiteness also requires
m<=n; the certificate does not remove that restriction.
The unresolved quantity eta_R measures how the nonlinear model can create
activity in weak modes. Neither it nor S has been bounded independently
of m for the intended data class. The eigenbasis can itself cost m^2 to
store, and this certificate alone is not a runtime.

A second certificate in the same section uses ||A_0^(-2)y||_m and a
stronger inverse-weighted drift bound to prove explicit t^(-2) residual
and t^(-1) parameter/output tails. It supplies a precise initial-data
version of the finite-time-to-all-time bridge, but its generic estimates
again contain inverse gaps and do not preserve the old width exponents.

## 2. All-time comparison can use dissipation instead of residual activity

Let r'=-2Ar and rhat'=-2B rhat start at -y in the same empirical Hilbert
space, with continuous self-adjoint positive semidefinite A(t),B(t).
Suppose, for every u,v,t,

\[
 |\langle u,(A-B)v\rangle_m|
 \le\zeta\langle u,Bu\rangle_m^{1/2}
           \langle v,Av\rangle_m^{1/2}.
\]

Then

\[
 \sup_{t\ge0}\|\widehat r(t)-r(t)\|_m\le\zeta Y/2.
\]

The proof completes the square in the error energy derivative and uses
integral_0^infinity <r,Ar>_m dt <=Y^2/4. It needs no positive gap,
commuting eigenvectors or exponentially growing stability factor.
This is an exact propagation theorem, not a construction theorem.

There are two decisive limitations. First, it controls empirical training
RMS, not the sphere supremum. Second, its uniform bilinear hypothesis
forces ker(A)=ker(B): test u in ker(B) and then v in ker(A).
Consequently it cannot directly certify dropping sample rank from a
positive definite A. A useful application to sample compression must be
source-restricted or otherwise account for discarded directions. Neither
that application nor the required nonlinear kernel comparison is proved.

## 3. Why absolute sample approximation fails over all time

GENERAL_SCOPE_CHECK proves a same-architecture example with any fixed
L>=2, n=d=2, identity activation, zero readout, all layers trained with
the prescribed mobilities, and a positive-probability Gaussian event.
Inputs lie on the fixed analytic circle
x(s)=sqrt(2)(cos(s),sin(s)); labels are the fixed constant Y>0.

Training puts fraction 1-p at the first coordinate direction and fraction
p at the second. At every p>0, both directions are eventually fitted on
the stated event. At p=0, the predictor at the untrained second direction
has a symmetric limiting law. On an event of probability at least half
the positive initialization-event probability, it is nonpositive.
Therefore deleting mass p causes all-time test error at least Y, although
the input Wasserstein distance is only sqrt(2)p. Taking p=1/m realizes
an ordinary empirical dataset. A proved variant replaces the repeated
points by distinct points of the same analytic curve.

The proof supplies the parameter balance invariants, lower singular-value
bound, global existence, convergence, and Gaussian symmetry argument; it
does not assume convergence of deep linear training as an external result.
The half-loss calculation differs from the paper only by a stated factor-two
time change, which does not change any all-time conclusion.

This is a fixed-width positive-probability failure of a uniform absolute
data-perturbation argument. It is not a large-width high-probability storage
lower bound. The linear feature Gram is singular when m>2, so it is not
a counterexample to the previous full-gap/small-label theorem. It tests
replacing that theorem's hypotheses by simple data geometry alone.

ALLTIME_GEOMETRY_ROUTE supplies a complementary near-duplicate example:
normalized circle inputs arbitrarily close together, constant labels,
two trained hidden layers and permitted affine activation. Merging the
two points leaves a transverse test response that the full dynamics
eventually removes. Its explicit lower bound is independent of separation.
This rules out a cluster-diameter-only all-time error estimate, not every
possible representation of those samples.

Neither example refutes sample compression: affine networks have exact
sample sufficient statistics, which preserve the small but important
moments rather than discarding them because their absolute size is small.

## 4. Fully unconditional all-time sample reductions that do follow

For arbitrary permitted activations, at most R distinct input locations
can be represented exactly by R inputs, their mean labels and frequency
weights. The entire dense trajectory agrees, on every query, for every
time. Sample storage is R(d+2) real coordinates, plus one optional scalar
for the irreducible label variance in the reported loss. This is finite
support, not a continuous-manifold theorem.

For affine activations, at every width and depth, the exact dynamics depend
on the dataset only through its second input moments, input mean,
label-input moments and label mean. An explicit inventory is

\[
 \frac{d(d+1)}2+2d+1
\]

real coordinates, plus the optional label second moment. All parameter
blocks still evolve by the original nonlinear factorized gradient flow.
The dense parameter count (L-1)n^2+n(d+1) has not been compressed by this
sample theorem. For bias-free identity activation the input mean and label
mean are unnecessary, leaving d(d+1)/2+d moments. These statements are
proved in the route notes and remain restricted activation subclasses.

The prior finite-horizon theorem in RESULT remains valid for the full
activation class and Lipschitz latent data. It is not promoted to all time
or to the paper's sharp combined width/sample rates by this attempt.

## 5. Explicit dependence rather than a renamed hidden constant

ALLTIME_SOURCE_ROUTE, Section 4, provides deterministic layer recurrences
for feature, derivative and second-derivative bounds, with every n, L and
activation factor exposed, and elementary Gaussian operator bounds showing
d and confidence dependence. The generic inverse-drift bound it obtains is

\[
 b_R\le\frac{2BHR}{\lambda_{\min}(A_0)^2},
\]

where B,H are the explicit first/second derivative envelopes there.
This is exactly where generic use of the existing assumptions reintroduces
bad conditioning. Calling b_R a new data-complexity constant would not by
itself remove that dependence. A width threshold or structural constant
allowed to grow with m also cannot support a uniform growing-m conclusion
without an explicit limit-order statement.

The main open theorem is thus genuinely narrower and better identified:
derive source-sensitive control of the nonlinear weak-mode feedback and
its test extension from quantitative initial data conditions, and construct
the associated finite sample-mode update without retaining the full data.
Only after that step can one claim the desired combined storage formula
for Legendre, Harmonic or Taylor. No such formula is asserted here.
