# Internal audit of the observable-generated polynomial state bound

2026-09-27. Scoped same-study mathematical crosscheck. Read complete
`NEXT_POLYNOMIAL_ROUTE.md`, `NEXT_GAUSSIAN_ROUTE.md`, the underlying
bounded-tree construction and audit, and the current-state aggregate
criterion in `TRUE_AGGREGATE_ASSESSMENT.md` section 1. No training,
experiment, external study, or promotion review was performed.

**Verdict:** the revised observable-generated construction proves a
polynomial scalar-state bound at fixed k,m,H and fixed finite assessment
horizon, conditional on the supporting Gaussian and degree-propagation
lemmas, which were also read and checked. The parallel-cutoff decoder is
causal and continuous, and the algebraic Gaussian error estimate follows.
This is not a theorem of useful practical compression or polynomial ODE
solver work. A small-degree definition issue was corrected during the
crosscheck: the hierarchy now starts at D>=9 so all coefficient-field
seeds exist.

## 1. Why the generated monomial family has the claimed closure property

The local coordinate dimension with one passive input is

\[
d=k^2+k(2m+3+2mH).
\]

Expanding exact output and feedback contractions into these labeled
coordinates gives a fixed finite seed family of degree at most nine.
Differentiate every selected constituent, add every child of degree at
most D, and repeat. A finite containing set exists, namely all monomials
of degree at most D in d coordinates. Therefore the procedure terminates.
At termination a missing child of a selected row necessarily has degree
greater than D. This is the property missing from the former output-only
selective refinement.

Possible paths which first leave the degree-D set and later return do
not invalidate the argument: their first step across the boundary is
exactly a bounded omitted source in the finite-propagation proof. The
comparison does not require retaining all monomials outside the reachable
set. Every moment used inside the coefficient fields belongs to the seed
family and is evolved by the same closure procedure.

The coefficient row sum grows at most linearly in the parent degree,
because that degree counts differentiated factors. At most two G entries
are inserted by one differentiation of the exact lifted local equations.
After dividing static mark coordinates by R, both row-sum and coefficient
Lipschitz envelopes are bounded by C_T(1+R)^2 times the parent degree.
Combining identical labeled monomials can reduce this absolute bound and
cannot enlarge it. Thus the degree proof applies directly to this new
hierarchy; it does not require treating it as numerically identical to the
older tree truncation.

The containing-set count is

\[
\#\{a\in\mathbb N^d:|a|\le D\}={D+d\choose d}=O_d(D^d).
\]

It is an upper bound for the selected coordinates, not their measured
count. The revised note preserves that distinction.

## 2. Uniformity over passive families

A local moment with training coordinates and one passive input differentiates
into moments with those same inputs only. The data sums use training
inputs, and a passive overlap field refers only to that passive input.
Consequently no row requires two distinct passive inputs.

Different passive families can discover additional training-only moments.
Their union still lies within the fixed training-only ambient basis, and
the exact derivative of a training-only moment has no passive dependence.
Identifying those coordinates therefore remains consistent. A row and its
coefficient fields involve only one passive family and the shared training
family, so taking the maximum over families introduces no factor M in
the row-sum or Lipschitz comparison. The quoted count

\[
{D+d_c\choose d_c}
 +M\left[{D+d\choose d}-{D+d_c\choose d_c}\right],
\qquad d_c=d-2k,
\]

is a valid ambient upper bound for the union.

## 3. The clock-selected cutoff gives the asserted rate

Each cutoff has its own population fields and its own normalization clock.
Those states cannot be shared across cutoffs. The construction correctly
shares only the physical-time clock used by the final decoder.

Take J=floor(log D), R_j=sqrt(j), and selection coordinate

\[
a_D(t)=\min\{J,\max\{1,\log D/[8C(t)]\}\}.
\]

Linear interpolation between the predictions for the adjacent cutoff
indices is continuous at every integer. All candidates have evolved from
the common starting time, so interpolation never calls an uninitialized
candidate or asks for past population information. Storing t with t'=1
makes this an autonomous readout from the current saved state. The
function C(t) comes from finite coefficient bounds and known comparison
constants, not from the trained target trajectory. A monotone smooth
majorant B(1+t)exp(Bt) is available because the normalized coefficient
dependence on the clock involves only finitely many inverse powers and
g>=exp[-(2+Y)t].

For any fixed T and sufficiently large D, every selected index satisfies

\[
\frac{\log D}{8C(T)}-1\le j
\le\frac{\log D}{8C(t)}+1.
\]

The first bound turns exp(-c_T R_j^2) into a constant times
D^{-c_T/(8C(T))}. The second gives

\[
C(t)(1+\sqrt j)^2\le \tfrac12\log D+4C(T).
\]

It follows both that the bounded-mark theorem applies and that its error
is at most

\[
e^{4C(T)}\sqrt D\,
   \exp[-e^{-4C(T)}\sqrt D],
\]

which is smaller than any fixed inverse power of D. This argument must
use the coefficient bound for the current time t; replacing it everywhere
by C(T) before selecting the cutoff would lose the estimate at earlier
times. The note makes the correct choice.

Taking M=D circle nodes adds O_T(D^{-1}). Convex interpolation in the
cutoff index adds no error amplification. Hence error <=A_T D^{-eta_T}
with positive eta_T. Together with N_D<=C_d D^{d+2}, this gives

\[
\text{error}\le A'_T N_D^{-\eta_T/(d+2)}.
\]

The inequality direction is valid: the state-count upper bound supplies
D>=(N_D/C_d)^{1/(d+2)}. Constants and exponents may depend very badly on
T,k,m,H. The ODE family and its size at fixed D do not depend on a design
horizon or elapsed time.

## 4. Admissibility and scope

The earlier Gaussian note excluded full joint-state basis enumeration.
The later aggregate assessment explicitly says that an infinite moment
sequence's ability to determine a law is not by itself disqualifying.
The revised construction generates only current observable/feedback
dependencies and does not store particles, law cells, initial-label
functions, density coefficients or a future trajectory. It is therefore
an aggregate-moment candidate under that operational criterion.

The proof does not show that its reachable family is substantially smaller
than the full ambient monomial set. Nor is its polynomial uniform in the
structural parameters: the exponent itself contains d. For k=4,m=2,H=1,
d=60, and the ambient degree-nine count is already 56,672,074,888.
This number is not an asserted actual retained count; it demonstrates
that the provided bound cannot establish practical efficiency.

The theorem supersedes the lack of a fixed-parameter polynomial
**state-count** certificate. It leaves useful approximation order,
conditioning and numerical solution cost unresolved. An initialization
algorithm or scalar-count theorem cannot establish a polynomial numerical
integration bound without a further stability and accuracy argument.
