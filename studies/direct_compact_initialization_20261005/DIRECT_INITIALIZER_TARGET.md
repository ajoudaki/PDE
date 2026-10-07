# Direct initialization at the old compact size

2026-10-05. Continuation of the same investigation. The requested construction
remains open. This note identifies an alternative to the population-bias
route, audits the old initializer, and records an exact Gaussian calculation
that a replacement initializer must respect. It does not claim an algorithm
with the requested accuracy-to-storage guarantee.

## Setup and the actual target

Use the user's two-hidden-layer tanh network, independent Gaussian first
weights of variance one, independent middle weights of variance `1/n`, zero
readout, squared mean loss, and block mobilities `(n,1,n)`. The fixed training
inputs have norm `sqrt(d)` and initially are orthogonal; labels are fixed,
signed, and satisfy the inherited small-label condition. Let

\[
 \|f-\widetilde f\|_*=
 \sup_{t\in[0,\infty]}\sup_{\|x\|_2=\sqrt d}
 |f(t,x)-\widetilde f(t,x)|.
\]

This includes the fitted endpoint and compares the same physical time.
Let `q` bound each hidden width of the retained compact model. The old runtime
then uses at most `dq+q^2+q+m` moving coordinates, fixed metrics of at most
`2q^2` coordinates, and `m(d+1)` data coordinates. Small training caches and
Gram solves do not change this order when `q>=m`. All initialization law
parameters, fixed metrics and decoder coefficients must be counted too.

The old source estimate has, for fixed dataset and architecture,
`q=O(log(en)^(3d/2+1))` and hence total retained storage
`O(log(en)^(3d+2))`. This is the inherited upper bound, not a claim that it
is globally optimal among arbitrary prediction representations. The present
objective is to keep this size while eliminating dense preprocessing.

## A virtual dense reference is sufficient

Suppose a directly generated compact model can be coupled in the proof to a
canonical width-`n` dense initialization, with small full-norm discrepancy.
The coupling may correlate those two proof objects. Take another canonical
dense initialization independently of the entire coupling. The triangle
inequality then gives

\[
 \text{direct-to-fresh-dense error}
 \le \text{direct-to-virtual-dense error}
       +\text{dense-to-independent-dense error}.
\]

The two failure probabilities add. The virtual dense model has to have the
canonical marginal law; its mere existence at a favorable exceptional
initialization is insufficient. No algorithm must generate it, and no
population trajectory or dense-to-population bias theorem is needed for this
implication. [VIRTUAL_REFERENCE.md](VIRTUAL_REFERENCE.md) proves the precise
coupling, approximate-law, and confidence statements.

In particular, directly sampling the **full joint law** of the old compact
initializer would suffice. Its deterministic autonomous evolution would then
have the old paired compact law. This would preserve its retained size and
runtime. This observation does not provide that sampler or bound its work.
Matching only the initialized feature Gram, a few matrix contractions, or
separate marginal laws is not the required joint-law assertion.

Full initializer-law matching is a sufficient route, not a necessary one.
A different architecture or deterministic initializer may instead prove its
own coupling to a canonical virtual dense run. Its coupling error need only
be comparable to dense variability; it need not preserve the old paired
construction's smaller error against a particular realization. This is the
precise relaxation allowed by the user's motivation.

The authorized integrated README reports old paired error `n^(-1+o(1))`
and dense-copy upper `n^(-1/2+o(1))`. Conditional on those source theorems
and on a successful direct sampler, the implication gives the latter rate,
not a strict `C/sqrt(n)` bound. This note does not reaudit those inherited
probability estimates or improve their rate. The stricter original request
and comparison at the available variability upper-bound scale stay distinct.

## What in the old initializer depends on the dense realization

The complete assigned `STORAGE_QUADRATIC_IMPROVEMENT.md`, its correction
report, and the spherical source proof were inspected. For one middle layer,
write `U_1,U_2` for source bases normalized by `U_l^T U_l/n=I`, `P_l`
for their selected rows, and `H_l` for their retained metrics. Its initial
reduced matrix is

\[
 B_C(0)=P_2\left(\frac{U_2^T W_0U_1}{n}\right)P_1^TH_1.
\]

The bases include source coefficients generated from the initialized neural
equations and their actual forward and transpose images. Selection and the
metric also depend on those bases. First weights are selected original rows.
Thus the four retained objects `A_C(0),B_C(0),H_1,H_2` have a correlated,
realization-dependent law. The source's finite initial-derivative algorithm
avoids trained-trajectory queries, but still uses the full initialized arrays.
Changing its input to the Gaussian law is a new construction problem.
Storing only a seed while regenerating and querying the original-width
network during setup would not eliminate that dependency.

### An exact reason that fresh small Gaussian mixers are not a substitute

For this paragraph let `u` be any deterministic Euclidean unit vector and
let `W` have independent `N(0,1/n)` entries. Set
`v=Wu/||Wu||_2`, an almost surely defined unit vector. These are the simplest
possible paired input/output source directions. Their reduced coefficient is

\[
 v^TWu=\|Wu\|_2,\qquad
 \mathbb E\|Wu\|_2^2=1,\qquad
 \operatorname{Var}(\|Wu\|_2^2)=2/n.
\]

Indeed the entries of `Wu` are independent `N(0,1/n)`; their squared sum
has the displayed moments. Chebyshev's inequality implies that this reduced
coefficient tends in probability to one. In contrast, for two deterministic
unit directions the corresponding coefficient is `N(0,1/n)` and tends to
zero. A size-one Gaussian with width-one variance would remain random of
order one and also have the wrong law. The adaptive output direction has
changed the coefficient distribution decisively.

This is not a no-go: the single coefficient can instead be drawn from its
chi law. It explains why the analogous, much more complicated *joint* law
must be generated for the nonlinear source families.

### The first backward response already contains a nonzero correction

Condition on a nonzero first-hidden vector `h`, independent of `W`, and
put `z=Wh`. If `b` is any measurable vector function of `z`, Gaussian row
projection gives

\[
 W^Tb\ \overset{\mathrm{law}}{=}
 h\frac{z^Tb}{\|h\|_2^2}
 +\frac{\|b\|_2}{\sqrt n}
 \left(I-\frac{hh^T}{\|h\|_2^2}\right)G,
 \qquad G\sim N(0,I_n),
\]

conditionally on `h,z`. To prove it, decompose each row of `W` into its
projection along `h` and its orthogonal component. Their covariance is zero,
so their joint Gaussian law makes them independent. The first component is
fixed by `z`; the remaining matrix has law
`W_tilde(I-hh^T/||h||_2^2)` with an independent Gaussian `W_tilde`.
Multiplication by `b` gives the formula and its conditional covariance.

For the zero-readout feature flow, the relevant first nonlinear response
contains `b=tanh(z) tanh'(z)` coordinatewise. Each nonzero coordinate
satisfies `z_i b_i>0`. Consequently the conditional mean term above does
not vanish almost surely. This response must not be replaced by a fresh
independent centered Gaussian. Later reuse creates further response and
innovation terms. The formula supplies one exact step, not a closed
polylogarithmic representation of all later steps.

## A genuine direct initializer exists for finite response programs

The maintained [Gaussian integration and adaptive initialization
section](../../docs/08-autonomous-computation.qmd#sec-docs-global-nonlinear-l13787)
constructs finite initialized response programs directly from Gaussian
quadrature, preserving named sources, their joint covariances, and frozen-
coefficient source derivatives. It appends the forward/backward reuse
corrections instead of resampling independent matrix actions. The main agent
read that complete section, its finite equations/assertion, and its complete
resource account; no code was executed.

This is useful constructive machinery, but it is not an accuracy-to-size
theorem for the present task. Its dictionary order, initializer quadrature,
evolution quadrature, regularization, time steps and arithmetic precision
are separate resolution parameters. Its retained marks and quadrature
particles cost storage in addition to the reduced mixer. The book's scoped
trajectory theorem uses nested limits and a specified short-time circle/data
setting, with small random finite readout rather than the exact zero finite
readout here. None of those scope differences is silently removed.

[DIRECT_GAUSSIAN_ATTEMPT.md](DIRECT_GAUSSIAN_ATTEMPT.md) records the direct
core calculation and the precise omitted-innovation issue. To use this route
at the old size, one still needs a quantitative source/quadrature selection
whose complete retained count is polylogarithmic and whose feedback error
stays at the requested scale throughout training. Fixed-program convergence
alone does not allow the number of sources to grow with `n` at that rate.

## Disposition

The virtual-reference interpretation is valid and eliminates an unnecessary
population-bias obligation for a law-matching route. It does **not** yet
eliminate the hard initializer problem. The old source-space construction
and the maintained direct Gaussian compiler are complementary tools, not a
proved composition at the requested rate and storage.

No direct algorithm with that complete guarantee has been obtained in this
continuation. No impossibility claim for designed compact initialization,
architecture or optimizer follows. In particular, the previous limitation
for an ordinary iid small network is not a limitation for these alternatives.

Root authored this note and checked the two elementary Gaussian calculations
by direct derivation. These are internal author checks, not an isolated
review, experiment, formal verification or promotion. The restricted skill
path remained unreadable; the prescribed notation and maintained notation
contract were used instead. All study/source authorizations are unchanged.
