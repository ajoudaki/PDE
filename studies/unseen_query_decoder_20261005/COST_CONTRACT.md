# Cost contract: finite-panel and unseen-input logarithmic compression

2026-10-06. Bounded accounting cleanup of the existing constructions. This
document is the reporting interface for their costs; it does not assert a
new compression theorem, an effective stochastic width threshold, or a
finite-precision integration theorem for the older compact ODE.

**Every `C` and every constant implicit in `O` below is universal.** None
depends on width, data, confidence, activation, depth, precision, or a
chosen implementation. Nonuniversal evaluation and input costs appear as
separate cost functions or explicitly unresolved entries, never as `C`.

## 1. Setup and the meaning of activation dependence

Use dense width `n`, training count `m`, input dimension `d`, fixed depth
`L >= 2`, training population feature-Gram gap `gamma > 0`, label RMS
`Y = ||y||_2/sqrt(m)`, and failure probability `delta`. Inputs have norm
`sqrt(d)` and the training inputs span the input space, so `m >= d`.
For the old method, `p >= m` is the total number of predeclared training
and test inputs. Their test labels are never needed. The new method accepts
unseen sphere inputs without a predeclared panel.

Keep the original full dense/compact/source intersection of label
allowances. In particular `16Ym/gamma <= 1`; that necessary consequence
is not a substitute for the full allowance. The case `Y=0` has the exact
zero predictor, once that case is known from the supplied input interface.
No algorithm for deciding equality to zero from an arbitrary real oracle
is being supplied.

The common activation strip is `|Im z| < a`. The regularity parameter is
the original, explicit envelope

\[
\beta=\max\left\{10,1+\max_{j\le L}|\phi_j(0)|,16/a,
 \max_{j\le L,\,k=1,2}
 \sup_{|\operatorname{Im}z|\le a/2}|\phi_j^{(k)}(z)|\right\}.
\]

Thus `beta` is not an unspecified activation constant. Its displayed
powers are polynomial in `beta^L`, with the admittedly large degrees
shown below. Activation implementation complexity is a different issue
and is charged separately in Section 4.

Use just two shared logarithmic factors:

\[
 \ell=\log(en),\qquad
 Z=\ell+\log\!\left(e+
 \frac{(m+d+2)\beta^{100L}(1+m/\gamma)}{\delta}\right).
\]

The proofs are conditional on their inherited source/fitting events at
each sufficiently large individual width. Resource inequalities do not
assert that this success width is polynomial in the problem parameters.
The reference and accuracy contracts remain different: the panel method
approximates its specified dense realization on the declared panel at
near-`1/n` error; the new decoder approximates an independent dense
reference on the whole sphere at the dense-pair upper-certificate scale.
Both include the full physical trajectory and endpoint under their
respective mathematical/numerical interfaces.

## 2. Older predeclared-panel method

These are **real-coordinate and exact-real arithmetic counts**, not bit
counts, with unit-cost exact sign/equality comparisons for rank and
selection decisions. They use the counted collocation coefficient producer replacing
the original unquantified initial-jet recipe. All fixed matrices, data,
readout caches and live work arrays are included. Activation, square-root,
input and evaluator implementation costs are additional as stated below.

| Resource | Bound on the full original label allowance |
|---|---:|
| Selected width | `ceil(30000 beta^(36L) p ell^(5/2))` |
| Retained model and peak RHS/query workspace, real coordinates | `C(L+1)beta^(72L)p^2 ell^5 + Cp(d+1)` |
| Offline initialization, arithmetic | `CL beta^(400L){n^2[m(1+m/gamma)^4+p]+np^3}Z^8` |
| Peak offline initialization, real coordinates | `CL beta^(100L){n^2(1+m/gamma)Z^2+npZ^3+p^2Z^5}+Cp(d+1)` |
| One training vector-field evaluation, arithmetic | `CL beta^(72L)mp^2 ell^5` |
| Its activation/first-derivative calls | `CL beta^(36L)mp ell^(5/2)` |
| One declared-point query with current readout cached, arithmetic | `CL beta^(72L)p^2 ell^5` |
| Its activation calls | `CL beta^(36L)p ell^(5/2)` |
| Complete numerical training to a certified tolerance | **Not established by the existing result.** |
| Finite-bit initialization, training and query bounds | **Not established by the existing result.** |

Under the separately identified simpler existing cap
`Y <= (gamma/m)beta^(-30L)`, remove the factors `beta^(36L)` from
selected width and runtime activation counts, and `beta^(72L)` from
runtime arithmetic/storage. This does not remove the displayed activation
factors from the preprocessing solver.

A query without a current corrected-readout cache additionally pays one
training forward pass and Gram solve, bounded by the RHS row. Querying
all `p` points pays for all `p` forward passes; the single-query row is
not a cost for the entire panel.

For an implemented integrator using `s` RHS calls per step and `N` steps,
multiply the RHS work and evaluator-call count by `Ns` and add the actual
linear-combination/controller work. Keeping `s` stage arrays also costs
`O(s)` times the moving-state size; a low-storage fixed-stage scheme may
reuse a fixed number of arrays. Here `s,N` are explicit local algorithm
choices, not constants absorbed in the table. No sufficient values of
them for the promised all-time approximation are proved by these counts.

The preprocessing memory row uses the nonmaterializing schedule in
[COST_INTERFACE_PANEL.md](COST_INTERFACE_PANEL.md): cosine coefficients,
their antiderivative, and polynomial evaluations are computed with linear
scratch in the collocation order. It does **not** cache a quadratic-size
table of integration weights. Caching that optional table requires adding
its actual squared-order memory. This fixes the earlier scheduling
ambiguity without increasing the achievable work or storage orders.

The same note counts square-root calls, Gaussian input/draw conventions,
activation calls, and exact rank/metric operations. Treating those calls
as unit primitives is an explicit computational model, not a theorem
about their bit complexity. Exact source dependence and selected metrics
do not yet have the finite-precision stability analysis needed to replace
the two unresolved rows above by major-parameter-only bounds.

## 3. New unseen-input response model

The following are **internal bit-space and bit-operation bounds** under
supplied activation/data precision interfaces. Multiply every row by
`C beta^(65000L)`, with universal `C`. Add the explicit interface costs
in Section 4; they are not included in this common multiplier.
The auxiliary normalized deterministic error exponent is fixed once at
the universal value `a_0=10`, not left as a hidden accuracy parameter.
An arbitrary user-variable tolerance is not the interface of this table.

| Resource | Internal bound |
|---|---:|
| Retained model bits | `(m+d+2)^23(1+m/gamma)^72 Z^144` |
| Retained plus peak training/query bits | `(m+d+2)^66(1+m/gamma)^204 Z^408` |
| Complete virtual-source initialization work | `n(m+d+2)^146(1+m/gamma)^454 Z^908` |
| Peak initialization bits | `n(m+d+2)^10(1+m/gamma)^31 Z^62+(m+d+2)^54(1+m/gamma)^168 Z^336` |
| All scheduled compact updates, excluding queries | `(m+d+2)^148(1+m/gamma)^460 Z^920` |
| One unseen-input query | `n(m+d+2)^189(1+m/gamma)^584 Z^1168` |

Initialization includes generation of the independent virtual source,
its completed finite computation, coefficient compilation and selection.
It does not read or reproduce a supplied realized dense matrix collection.
If reading such a collection is requested, its entry/bit input cost is
additional, and the matched-root accuracy task is not proved by this
construction.

The update row already includes every scheduled acquisition update through
the terminal time patch, not just one RHS evaluation. The source schedule,
finite iterations, rounding, and frozen tail are included. There is no
recalibration step. A query evaluates the current response circuit, not
a replay of the scalar training updates. Any number of requested queries
must be charged separately; their combined time is the sum of their costs.

## 4. Evaluators, actual inputs, labels and output formats

For this section let `T_phi,data(b)` and `S_phi,data(b)` denote nondecreasing upper
bounds on the work and scratch of one supplied activation/first-derivative
or fixed-data access, at the requested precision and bounded argument
length. This is an explicit **cost function of the supplied code/data**,
not a constant or a consequence of the regularity envelope. Universal
arithmetic, cosine, Gaussian-generation and small-matrix routines are
already counted internally. Retained evaluator code and original data
descriptions must be added to storage whenever retained.

One common sufficient precision/argument-length allowance for the new
model is

\[
 b=\left\lceil C\beta^{3511L}(m+d+2)^{11}
             (1+m/\gamma)^{34}Z^{68}\right\rceil.
\]

The universal numerical coefficient is fixed large enough for the
previously specified error allocation. Choosing this common upper
allowance, rather than the smaller source precision, gives the following
safe additional work:

| Phase | Evaluator/data work to add |
|---|---:|
| Initialization | `Cn beta^(2709L)(m+d+2)^9(1+m/gamma)^27 Z^54 T_phi,data(b)` |
| All compact updates | `C beta^(3311L)(m+d+2)^11(1+m/gamma)^33 Z^66 T_phi,data(b)` |
| One unseen query, including coefficient preparation | `Cn beta^(6220L)(m+d+2)^20(1+m/gamma)^61 Z^122 T_phi,data(b)` |

Add `S_phi,data(b)` to the corresponding peak memory, not its value
multiplied by the number of sequential calls. If an implementation retains
caches across calls, count those caches as well. The derivation and the
smaller phase-specific precision choices are in
[COST_INTERFACE_EVALUATORS.md](COST_INTERFACE_EVALUATORS.md).

The following costs are also explicit additions, **not universal constants**:

- reading the original finite input descriptions and supplied dense root
  when applicable;
- producing and, if required, verifying the input certificates (including
  activation bounds and a Gram-gap lower bound), with their actual peak
  workspace;
- acquiring a new query and a requested time to the counted precision;
- writing the requested output representation;
- retaining any original input, activation code or certificate description
  which the implementation continues to use.

The costs of supplied numerical certificates are zero *beyond reading
them* only if they are indeed supplied and no algorithmic verification
is demanded. Computing a population Gram gap or certifying a strip bound
is not silently included as a free quadrature or optimization oracle.
These acquisition costs have not been bounded from the bare mathematical
assumptions.

There is also a real `Y` dependence at the raw-data interface. To obtain
the normalized labels to `b` fractional bits from absolute-precision
access to the original labels, a sufficient raw precision is

\[
 b+\lceil\log_2(16\sqrt m)\rceil
   +\lceil\log_2\max\{1,1/Y\}\rceil.
\]

Thus absence of an internal inverse-label polynomial is not a claim of
free normalization of arbitrarily tiny labels. Retain or access the output
scale `Y` with an explicitly counted representation. A floating scale has
an exponent-description cost growing as `log(2+|log Y|)` as well as its
mantissa; an original exact rational description may be much larger.
Fixed-point output with accuracy relative to `Y` needs the corresponding
extra leading fractional positions. The input/output interface must choose
and pay for one of these conventions; the algorithmic tables alone do not.
We keep these costs visible before applying width restrictions. On a
source domain where `n^(-1) <= Y`, the additional logarithm can already
be dominated by `log n`; these explicit additions do not disprove the
existing bound on that restricted domain.

There cannot be a uniform evaluator-cost theorem from `beta` alone for
the full mathematical activation class. For example, `phi(x)=sin(x)+c`
with a noncomputable real `0<c<1` is nonlinear, analytic, and has one
uniform strip/derivative envelope, but a precision evaluator at zero
would compute `c`. Even when the chosen activation is computable, its
description and evaluation algorithm must be specified before replacing
the explicit evaluator functions above by numerical polynomial bounds.
This explains the computational interface; it is not a new activation
restriction on the original exact-real theorem.

## 5. Orders, thresholds and the exact remaining boundary

Every executed temporal order is charged: the physical horizon, patch
count, collocation degree, finite Picard count, source coefficient degree,
quadrature node count, coefficient generation and storage, selection rank,
Gaussian cutoff, sampling blocks, matrix iterations, precision, and seed
generation. There is no spatial harmonic expansion in either of these two
models. The unseen decoder's proof grids are not enumerated; their log
cardinality contributes to the counted precision and sampling blocks.
Neither high-order activation jets nor posterior Fourier integration is
executed by the current costed algorithms.

For the panel, the following sufficient conditions expose all its original
deterministic construction gates in the major parameters:

\[
 n^{-1}\le\min\{1,Y,16Ym/\gamma\},\qquad
 \log(en)\ge\beta^{50L}(1+m/\gamma)^2.
\]

The elementary recurrence check is in `COST_INTERFACE_PANEL.md`, Section 4.
This is a deliberately loose sufficient envelope, not a necessary condition
or a polynomial bound on width: it can require exponentially large `n`.
For a strict width reduction, also check
`ceil(30000 beta^(36L)p ell^(5/2)) < n`. These displayed gates do not
certify the stochastic source event.

The explicit unseen sampling condition remains

\[
 n\ge C\delta^{-1}\beta^{4000L}(m+d+2)^{11}
       (1+m/\gamma)^{34}Z^{68}.
\]

This does not replace the unquantified stochastic source/fitting threshold
or the inherited statistical-error comparison threshold, which may depend
on the complete dataset, activations, `Y`, depth, confidence and panel.
Those unknown thresholds are not constants inside a resource bound and
must not be reported as polynomially controlled. Likewise the elementary
eventual comparison `n Z^1168 = o(n^2)` for fixed parameters is not a
useful finite-width dense-cost guarantee. Its actual prefactor and external
evaluator costs must be included when checking a particular width.

Accordingly the resolved claim is a transparent cost interface for the
existing algorithms, including the small memory-scheduling repair. The
following stronger claims remain unavailable, not hidden in notation:

1. a finite-bit, accuracy-certified full simulation of the old compact ODE;
2. a uniform cost for arbitrary supplied activation/data evaluators and
   for obtaining the scientific certificates;
3. an effective all-parameter width threshold for the inherited accuracy
   and probability guarantees.

No new proof search for these claims is part of this bounded cleanup.

## Check status

The supporting evaluator and panel-interface derivations are scoped author
work in this study. The lead read both completely, reconstructed their
order/precision arguments, and checked all twelve resource/evaluator
exponent substitutions by integer arithmetic. Scoped whitespace checks
passed for the three new interface files.

A fresh bounded check, [COST_CONTRACT_CHECK.md](COST_CONTRACT_CHECK.md),
read the complete three-file candidate and its explicitly assigned source
notes. It reconstructed the linear-scratch Picard implementation,
normalization work/precision, expanded exponents and deterministic width
gates. It requested four specification corrections: fix the accuracy
exponent at 10; state exact comparisons in the panel machine model; charge
requested-time access; and qualify the tiny-label encoding statement before
applying source-width gates. All four were incorporated and rechecked,
with no unresolved finding in that bounded scope. The report preserves
initial and corrected hashes; its own SHA-256 is
`20601db76f9d1d68f3e878e25e8a29cc0ecd0a9cd17ad8f453d8a51c46f22772`.
This paragraph is a subsequent provenance addition to the checked contract,
not a change to its scientific statements.

These checks do not reprove the inherited stochastic source/decoder
theorems, supply the missing panel numerical-training theorem, or promote
the result. No experiment, implementation benchmark, maintained book/code,
unrelated study, or Git state was changed. The required canonical-notation
skill remained permission-inaccessible; the explicit user/repository
notation rules were used instead, with the rigorous-math and research-audit
skills applied to keep claim levels and computational units separate.
