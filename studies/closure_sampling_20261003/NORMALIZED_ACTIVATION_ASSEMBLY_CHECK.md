# Coordinator reconstruction: normalization and depth gains

2026-10-04. Internal reconstruction, not promotion. The user clarified the
normalization to mean E[phi(Z)^2]=E[(phi'(Z))^2]=1 for Z~N(0,1), with no
zero-mean condition on phi(Z). All conclusions here use that condition.
This continues the same activation/depth-constant question and changes no
reference dynamics or established compression bound.

## 1. Complete sources read and source separation

The coordinator read the complete frozen sources:

| Source | SHA-256 |
| --- | --- |
| CRITICAL_NORMALIZATION_GEOMETRY_ROUTE.md | 410da51621c61e2f4b5785b6a26c24a3d4c3c3464a2599daf65aaed17b5b3d6e |
| NORMALIZED_ACTIVATION_EXAMPLES_ROUTE.md | 1e14c318bb8352007c8326d601cd654b865cf40c71d7f0156c2d50305510b4b8 |
| BETA_ENVELOPE_AUDIT.md | 42461b5f2381b337c2646ab7c5387921abf8b3e1f255df7160d5757025940d28 |

The separate root-authored candidate NORMALIZED_ERF_COMPLEX_GAIN_ROUTE.md
is frozen at 8368603ca1a6bd449dc478810befce7aa62dc8cc1dc05869c9a68114a19599ef.
It is not represented as independently checked by its author. Its dedicated
reconstruction was read completely at
64f52fe5da392d84cca38fc4e8db297f0b0cea5620e7fe83e84f3b4805347989.
It closes the finite-width complex moment bridge using strict covariance
neighborhoods and a truncated conditional law of large numbers. The
unbounded activation extension
and current explicit compression interfaces are reused from the complete
unchanged prior reads in this task; none of their numerical constants are
silently generalized by these new initialization calculations.

The geometry author received prompt-only scientific inputs. The examples
author received the named existing class-extension and architecture notes.
The envelope author received seven named prior same-study proof notes.
Each new candidate was frozen before cross-route exchange. Subsequent
checks may use those frozen sources and state that exposure explicitly.
The complete later NORMALIZED_ACTIVATION_COMPONENT_CHECK.md was read at
be30d018ab41d3c7ad196bb013dead0f47c5cd903b1fe3f0412f4002abb2726b.
It reconstructs the new scalar mathematics in the examples and beta audit.
Its mollification argument supplies the bounded-first-derivative version
of the normalization proof advertised in the examples' opening paragraph;
this assembly and synthesis already used the explicitly proved bounded
first/second-derivative version. No example or formula changes. The report
also preserves a diagnosed narrow-peak quadrature failure and its corrected
variable substitution; all substantive claims have exact proofs independent
of quadrature. The frozen candidates remain unchanged.

## 2. Geometry reconstruction

The first-layer convention in the geometry note is exactly the canonical
one after substituting v=x/sqrt(d). Its optional centered Gaussian readout
is used only to explain an initialized covariance; it does not replace
the actual trained network's zero readout in any compression claim.

The Hermite proof supplies the needed completeness and integration-by-parts
dependencies instead of merely invoking a theorem. For the cutoff argument,
Gaussian polynomial integrability and Cauchy--Schwarz control the extra
boundary term with derivative O(1/R). Parseval then gives p_k>=0,
sum p_k=1 and sum k p_k=1. The correlated generating-function calculation
and L2 approximation justify F(c)=sum p_k c^k on the whole interval.
The derivative norm identities require exactly the stated Gaussian Sobolev
regularity; the converse identification of phi'' uses distributional
derivatives on compact intervals, where the Gaussian density is bounded
above and below. No Gaussian boundary term is assumed without a cutoff.

The centering conclusion applies only when E phi=0 is additionally imposed.
The user did not impose it. The normalized noncentered examples obey the
identity (E phi)^2=sum_(k>=2)(k-1)p_k and are therefore consistent.
The sine example is genuinely bounded on each finite horizontal strip;
the polynomial and rapidly oscillating entire examples are outside the
bounded-strip-derivative class and are not imported into its all-time theorem.
In particular the infinite-curvature example disproves only a claim based
on analyticity and the two moments alone, not the prior strip hypothesis.

For the sphere feature map the tensor derivative norms were checked
termwise. First-order tensor placements are orthogonal. Second-order
acceleration consists of -k x^tensor(k) plus coefficient-two terms for
each unordered pair of tangent placements, giving k+3k(k-1). Summation
therefore yields squared norms 1 and 1+3L chi_2. The polarized Hessian
covariance gives exactly
L chi_2 ||v||^2||w||^2+(1+2L chi_2)(v dot w)^2. The same sums dominate
difference quotients, so the claimed Hilbert derivatives exist. These
statements concern the deterministic limiting feature map and are not
unqualified uniform finite-width trained derivative bounds.

The Gram-gap proof is also valid for negative off-diagonal correlations.
For C>=eta I with unit diagonal, B=C-eta I is positive semidefinite and
C^circ(k)=B^circ(k)+[1-(1-eta)^k]I for k>=1. Tensor Gram matrices prove
the positivity of B^circ(k); the k=0 term is the all-ones matrix. The
scalar inequality 1-(1-eta)^k>=k eta/[1+(k-1)eta] follows by integrating
the derivative of (1-eta)^(-(k-1)), and Jensen uses the probability
weights k p_k. This proves the explicit bound
gamma_L>=(gamma_0^-1+L chi_2)^-1 when gamma_0>0.

For the asymptotic statement, positive gamma_0 ensures every off-diagonal
input correlation lies strictly between -1 and 1. Each bracket
(k-1)-kc+c^k in F(c)-c is strictly positive for c<1. The critical quadratic
expansion then gives reciprocal increments tending to chi_2/2, followed
by gamma_L~2/(chi_2 L) for fixed m>=2. The finite-dimensional operator
error is o(1/L); Rayleigh quotients justify eigenvalue transfer. The linear,
m=1, duplicate/antipodal and infinite-curvature cases are separated in the
candidate. The initial-gap bound is an optional scoped result: it is not
added as a restriction to the original compatible-data compression theorem.

## 3. Activation examples and envelope audit

The Gaussian interpolation proof of Var(g)<=E g'^2 uses precisely bounded
first/second derivatives and linear growth; the two second-derivative
integration-by-parts terms cancel. The deficit integral and positive
bivariate density prove the equality case. Thus the two offsets in the
normalization formula are exact, and no centering assumption is introduced.

The exact GELU moment values were reconstructed by Gaussian integration:
mu=1/(2 sqrt(pi)), Q=1/3+1/(2 pi sqrt(3)),
D=1/3+2/(3 pi sqrt(3)). Their difference is positive. Both normalized
offsets, the strip derivative bound, and the scalar variance derivatives
follow by direct substitution. Root independently evaluated the closed
constants with Python's math module; the values agreed with the route.
This is arithmetic verification, not a network experiment.

The bounded-strip derivative argument for GELU uses integration vertically
from the real axis, where Phi is bounded by one; its other derivative
term uses sup |x|exp(-x^2/2)=exp(-1/2). This verifies membership in the
qualitative unbounded-value extension without pretending the bounded
activation value B_0 is finite. The centered rescaled GELU would not
satisfy both normalization conditions; the displayed output offsets matter.

The exact formula V'(1)=1+E[phi phi''] shows why the two moment equalities
alone do not ensure variance stability. The GELU plus/minus branch signs
can be certified without decimals, as done in the source. The second and
third derivative Gaussian integrals are consistent with its fixed-order
composition formulas. Those polynomial-in-depth formulas do not sum an
infinite response expansion.

The beta audit correctly separates numerical floors, deterministic
operator/metric gains, strip radii, and independent-vector Gaussian gain.
The inequality max(10,32B/a^2)>=sqrt(320B)/a>16/a proves the claimed
redundancy only for the Cauchy-based definition. It does not make the
inverse strip radius disappear. A matrix-adapted first-row direction has
squared gain tending to two, so unit average gain cannot replace the
operator cap even at initialization.

The cosine and Gaussian-primitive examples satisfy the two moments by
direct characteristic-function or square-completion identities. Their
curvature/fourth-moment values were reconstructed, including the actual
independent first-layer angular tangent Q=phi'(Z)U. The audit carefully
does not identify a generic equal-product example with the actual training
response R. The missing trained quantity is the genuinely mixed product
phi''(z) R J in normalized RMS, which the two scalar moments do not control.

There is a decisive elementary limitation for the old beta definition:
if E phi'^2=1 and sup_R|phi'|<=1, then continuity and full Gaussian support
force |phi'|=1 everywhere. Continuity fixes its sign; hence phi(x)=+/-x+b.
E phi^2=1 forces b=0. Every normalized nonlinear activation therefore
has real derivative supremum strictly greater than one. If it is bounded,
its value supremum is also strictly greater than one: equality with the
unit second moment would otherwise force constant magnitude, contradicting
the derivative condition. Removing numerical floors cannot make this
supremum-based beta equal one for a nonlinear normalized activation.

## 4. Exact finite-network variance reconstruction

The later complete candidate NORMALIZED_VARIANCE_FLUCTUATIONS_ROUTE.md was
read at SHA-256
2debe995c6f02d92f26f992a6c9d643fa4ef0c2bcf72ec63ed2068ac984d2406.
The root suggested the finite-network variance question after the examples
route was frozen. Its check is collaborative, not independently promoted.

At one fixed query the conditional variance of each fresh Gaussian row is
exactly the preceding empirical feature second moment q. Thus the scalar
Markov transition is exact in distribution and includes variance zero.
There is no independence assumption about trained weights; the result
concerns initialization only. Conditional on q in a compact neighborhood
of one, linear growth of phi makes the third absolute centered moment of
phi(sqrt(q)Z)^2 uniformly bounded. The characteristic-function Taylor
remainder is consequently O(n^-3/2) per summand, uniformly on that compact.
Conditioning on preceding innovations yields limiting independent Gaussian
increments. Tightness and differentiability of V give the claimed linear
recursion G_l=V'(1)G_(l-1)+xi_l at each fixed depth. The exact form and
hypotheses of the ordinary characteristic-function continuity criterion
are stated and met; no trained-population comparison is imported.

Convergence of actual variance needs more than the distributional limit.
The candidate supplies it under bounded H'' for H=phi^2. That makes V
globally Lipschitz on q>=0; quadratic growth of H yields bounded fourth
moments of q at fixed depth and the exact independent-sum fourth-moment
identity yields bounded fourth moments of the innovations. Induction then
bounds E[|sqrt(n)(q-1)|^4] uniformly in n at each fixed depth. Truncation
proves the required first/second moment convergence. Bounded H'' is
explicitly verified for both GELU branches and holds for the bounded erf
example as well. It is not inferred for every linear-growth activation.

The signs and exact expressions for V'(1) in the GELU application agree
with the preceding full examples reconstruction. The innovation variance
is the displayed finite Gaussian integral, and is strictly positive by
continuity/full Gaussian support and the nonzero derivative moment. The
identity check independently gives Var(q_n,L)=(1+2/n)^L-1, reproducing
the limit 2L. The plus GELU branch thus has exponential depth growth of
this finite-network feature-norm variance coefficient, while the minus
branch is bounded. This is not a lower bound on output error, because
the stored readout is zero at initialization.

For the normalized erf, the root separately computed the exact innovation
variance. Let alpha=pi/(2 sqrt(3)), so the squared erf scale is 3 alpha
and b^2=1-alpha. The erf of a standard Gaussian divided by sqrt(2) is
uniform on [-1,1], with moments 0,1/3,0,1/5 through order four. Expanding
(sqrt(3 alpha)U+b)^4 gives E phi^4=1+4 alpha-(16/5)alpha^2. Combined
with V'(1)=1/2, this verifies synthesis (12). All limits first hold with
fixed depth. Studying the resulting coefficients as L grows does not
exchange width and depth limits.

## 5. Claim boundary

These checks support exact activation-level and initialization-geometry
results. The same physical-time, all-time compression problem remains
open with polynomial-only depth coefficients. No result here makes the
trained neuron law standard Gaussian, preserves normalized moments during
training, or bounds all adaptive response products from marginal moments.
No compression lower bound is inferred from sensitivity growth or from a
failed proof envelope. The existing explicit compression statements remain
unchanged. Numerical covariance sanity checks in the geometry candidate
are supplementary arithmetic checks, not evidence of trained behavior.
