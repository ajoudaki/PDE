# Parameter-explicit costs: current decoder and earlier finite panel

2026-10-06. Author continuation of the same resource investigation.
This note separates new deterministic accounting from the inherited
stochastic source event. It is not promotion and does not make the source
success threshold effective. The aim is to expose, not rename, the
dependence previously hidden in fixed-problem constants.

The reporting interface is now [COST_CONTRACT.md](COST_CONTRACT.md).
It retains these internal resource powers, explicitly expands the evaluator
call/precision charges, exposes raw-label normalization and output-scale
costs, specifies linear-scratch collocation, and marks unproved numerical
panel-training costs as unresolved rather than constants. Its `C` is
universal; input/evaluator/certificate costs remain explicit additions.

## Shared setup and units

Use dense width `n`, training count `m`, input dimension `d`, fixed hidden
depth `L >= 2`, initial population feature-Gram gap `gamma > 0`, and label
RMS `Y`. The inputs have norm `sqrt(d)` and the training inputs span the
input space, so `m >= d`. Activations have the original strip analyticity
and bounded first derivative; their values need not be bounded. The
activation envelope `beta >= 10` is exactly the one in the integrated and
finite-panel statements. Keep the full original intersection of the dense
fitting, compact fitting, and source label allowances. The simpler existing
cap `Y <= (gamma/m) beta^(-30L)` is a separately identified display case,
not a replacement for that full allowance. The all-zero-label case needs
only the zero predictor.

For the older method, `p >= m` counts **all** predeclared points, including
training points. Passive-point labels are neither supplied nor used. The
new decoder has no `p`: it accepts a sphere input supplied after training
has begun. Both accuracy interfaces include every physical training time
and the limiting endpoint, but the panel norm and whole-sphere norm are
different. The panel method has matched-reference near-`1/n` error; the
unseen decoder has dense-pair upper-certificate-scale error.

An arithmetic operation on an exact real, a stored real coordinate, a
finite-precision bit, an activation-primitive call, a vector-field
evaluation, and a complete numerical training simulation are distinct
units. In particular a count for one evaluation of an ODE does not specify
a numerical step size or total time to simulate that ODE to a tolerance.

## Full-label finite-panel radius: no hidden sample/gap constant

The original finite-panel theorem uses the local proof quantities

\[
 S=16Ym/\gamma\le S_*^{\rm src}\le1,\qquad
 \chi=\min\{1,a/[4S^2 U_{\rm fin}(S)]\}.
\]

Here `a` is the activation strip half-width in the original convention,
and the source recurrence defining `U_fin` has only activation/depth
coefficients. Its monotonicity already showed that `chi` has an
activation/depth-only positive lower bound on the full label interval.
The following explicit power envelope avoids leaving even that coefficient
unnamed:

\[
\boxed{1\le\chi^{-1}\le\beta^{36L}.}
\tag{1}
\]

This deliberately loose activation exponent does not cost any new power
of `m`, `1/gamma`, `Y`, `d` or `p`.

### Proof of (1)

Use the power ledger in the authorized
`SIMPLE_CONSTANTS_SOURCE_CHECK.md`, Sections 1--3, **before** its
small-activity substitution. The base recurrences give

\[
 H_j\le3\beta^{2j},\quad f_j\le\beta^{3j-1},\quad
 K_{\rm src}\le\beta^{20L+2},\quad
 q_j\le\beta^{5L+3j-2},\quad T_Q\le\beta^{14L-3}.
\]

None of these five inequalities uses the smaller label cap. In the
finite-query recurrence, for `2 <= j <= L` and `S <= 1`, its bracket is
bounded by

\[
 H_{j-1}^2+f_{j-1}^2+S T_Q+S^2 H_{j-1}q_{j-1}
 \le9\beta^{4L-4}+\beta^{6L-8}
       +\beta^{14L-3}+3\beta^{10L-7}
 \le2\beta^{14L-3}.
\]

The last inequality follows by dividing by `beta^(14L-3)`; at
`L >= 2, beta >= 10`, the three extra ratios sum to less than one.
Consequently

\[
 U_j\le4\beta^{34L}+128\beta^{8L-5}+2
       \le5\beta^{34L},\qquad
 U_1\le4\beta^{20L+3}\le5\beta^{34L}.
\]

Since `a^(-1) <= beta/16`,

\[
 \chi^{-1}=\max\{1,4S^2 U_{\rm fin}(S)/a\}
 \le\max\{1,(5/4)\beta^{34L+1}\}
 \le\beta^{36L}.
\]

Under the simpler original cap the sharper inherited value is `chi=1`.
No width-asymptotic absorption occurs in this proof.

## Finite-panel runtime: explicit small-degree bounds

Write `ell=log(en)`. The arithmetic implementation and constructive
selection are derived in [FINITE_PANEL_PARAMETER_COSTS.md](FINITE_PANEL_PARAMETER_COSTS.md).
On the simpler existing label cap, the maximum selected width is at most
`ceil(30000 p ell^(5/2))`. The full-label choice has the additional factor
`chi^(-1)`; substituting (1) bounds it by `beta^(36L)`.

The following counts include fixed matrices and live runtime workspace,
not just learned weights. Universal numerical constants in big-O do not
depend on any scientific parameter. Add the fixed activation evaluator's
description, workspace, and charged evaluation cost if not treated as a
primitive.

| Resource | Simpler existing label cap | Full original label allowance |
|---|---:|---:|
| Retained and live runtime real coordinates | `2^36 (L+1)p^2 ell^5 + 16p(d+1)` | `2^36 (L+1) beta^(72L)p^2 ell^5 + 16p(d+1)` |
| One training-vector-field evaluation, scalar arithmetic | `< 2^36 L m p^2 ell^5` | `< 2^36 L beta^(72L) m p^2 ell^5` |
| Its activation/first-derivative calls | `< 2^16 L m p ell^(5/2)` | `< 2^16 L beta^(36L) m p ell^(5/2)` |
| One declared-point query, current readout cached | `< 2^32 L p^2 ell^5` | `< 2^32 L beta^(72L) p^2 ell^5` |
| Its activation calls | `< 2^15 L p ell^(5/2)` | `< 2^15 L beta^(36L) p ell^(5/2)` |

The query's additional neuron scratch is at most `2q`; the complete peak
is already covered by the first row. If no current corrected-readout cache
is available, add one training forward pass and the training-Gram solve,
bounded by the training-vector-field row. A cache is refreshed once per
state and shared across queries at that state. Passive points need not
be reevaluated for a training update.

These are degree two in the total panel size for storage and a single
query, and degree three overall in sample counts for a training RHS.
The inverse-gap and label-size powers in these operation counts are zero.
Those parameters still occur in the error and width qualifications. Extra
stages of a numerical integrator must be counted; this table does not
specify how many stages/steps suffice for accurate numerical training.

## A counted coefficient producer for finite-panel initialization

The original initialization specified finite jet continuation and
quadrature, without a work bound. We can replace that **preprocessing
procedure**, without changing the selected source order or autonomous
runtime, by the explicit physical collocation algorithm in
[PHYSICAL_PARAMETER_ACCOUNTING.md](PHYSICAL_PARAMETER_ACCOUNTING.md).
The construction below is in exact-real arithmetic with activation and
first-derivative primitives. It is not a finite-bit implementation of
the selected model.

For this section let

\[
 Z=\log(en)+\log\!\left(e+
 \frac{(m+d+2)\beta^{100L}(1+m/\gamma)}\delta\right).
\tag{2}
\]

Here `0<delta<1` is the failure probability. This is a stated logarithmic
factor, not an arbitrary fixed-data constant. The panel producer needs only
the smaller version without its sample/dimension/confidence factors; using
this common larger factor permits comparison with the unseen decoder.
Fix the original finite-panel horizon `32(m/gamma)ell`. Let `K` be the
original degree in finite-panel RESULT (10), with
`alpha=chi/(128ell^(3/2))` and source amplitude `M_0 sqrt(n)`.
Choose `Q` to be the least power of two at least `2(K+1)`. In particular
`Q <= 4(K+1)`, and under exactly the displayed original degree-count gate,

\[
 K+1\le C\beta^{36L}\ell^{5/2},\qquad
 Q\le C\beta^{36L}\ell^{5/2}.
\tag{3}
\]

`Q` is a discarded preprocessing quadrature count, not another retained
model order. Evaluate each source family at the `Q` Gauss--Chebyshev time
nodes. Compute their discrete cosine coefficients, and retain only
degrees zero through `K`, just as in the old source construction. Apply
identical linear operations to a preimage and its initialized mixer image.
The paired identities are then exact for the computed source vectors.

### Truncation, quadrature and physical-solver error

For each coordinate the exact time-Chebyshev coefficients have magnitude
at most `2M_0 sqrt(n) exp(-alpha j)`. The inherited choice of `K` gives

\[
 e^{\alpha K}\ge64M_0n^{3/2}/\alpha,
\]

and truncation error at most `1/(16n)`. At the `Q` root nodes, frequencies
alias only in the classes `2sQ +/- j`, with signs. For retained degrees
`0 <= j <= K`, summing these geometric tails bounds the total alias error
by

\[
 \frac{4(K+1)M_0\sqrt n\,e^{-\alpha(2Q-K)}}
 {1-e^{-2\alpha Q}}\le\frac1{256n}.
\tag{4}
\]

Indeed `2Q-K >= 3K+4`, the denominator is at least `1/2`, and
`K+1 <= 2 exp(alpha K)/alpha` for `0<alpha<=1`. The left side is thus
at most `16M_0 sqrt(n) exp(-2alpha K)/alpha`, which is at most
`alpha/(256M_0 n^(5/2)) <= 1/(256n)`.

The physical note proves that simultaneous coordinate errors in all four
source families, including initialized images, are bounded by
`beta^(100L)(sqrt(n)+Sn)` times the normalized physical parameter error.
Its explicit target

\[
 \text{physical parameter error}\le
 \frac{Y\beta^{-200L}}{(Q+1)n^3}
\tag{5}
\]

makes each node's coordinate error at most `1/(64Qn)`, using `S<=1`
and the inherited full-label bound `Y<=beta^(3L)`. A discrete cosine
coefficient amplifies maximum nodal error by at most two. Summing at most
`K+1 <= Q` retained coefficients therefore adds at most `1/(32n)`.
Its coefficient-arithmetic allowance can use another such fraction.
Together with (4) and the truncation error this is strictly below `1/n`.
No inverse power of `Y` or new width absorption is required. Initial
training features, first-weight columns and the constant are still added
exactly, preserving the initial Gram and original fitting allowance.

The solver runs once in increasing physical time. Sort the requested time
nodes, evaluate the source families as each containing patch is reached,
and accumulate the cosine sums. Old dense patches can then be discarded.
There is no need to retain the entire dense trajectory.

### Work and peak memory

The physical note's adaptive source solver uses at most
`C beta^(300L)(1+m/gamma)^3 Z^6` field evaluations and at most
`C beta^(100L)(1+m/gamma) Z^(3/2)` stages on a patch. The target (5)
replaces its logarithmic factor by one with an added `log(Q+1)`; (3)
bounds that new factor by a numerical multiple of (2).

Use the direct, non-fast-transform, linear-scratch implementation in
[COST_INTERFACE_PANEL.md](COST_INTERFACE_PANEL.md), Section 1: compute
cosine coefficients, integrate their recurrence, and evaluate one state
coordinate at a time. No quadratic-size integration-weight table is
retained. All collocation sums
cost at most

\[
 C L n^2\beta^{400L}m(1+m/\gamma)^4 Z^8.
\]

Here `n>=m>=d` already follows on the positive empirical training-Gram
event. Generating the panel families costs at most
`CQ[L n^2(K_solver+p)+pdn]`, and naive cosine summation at most
`CnpLQ^2`. Exact-real spectral sparsification, the metric correction,
and reduced mixer formation cost
`CL[n^2 R+nR^3+R^3]+C m^2d`, where the source-rank budget is
`R<=3077 beta^(36L)p ell^(5/2)`. Selection uses the constructive
[Batson--Spielman--Srivastava vector sparsifier](https://arxiv.org/pdf/0808.0163),
with the exact-isometry metric correction proved in the panel-cost note.
Combining these terms gives the following full-label arithmetic bounds:

\[
\boxed{
 W_{\rm init}\le
 C L\beta^{400L}
 \left\{n^2\left[m(1+m/\gamma)^4+p\right]+np^3\right\} Z^8.
}
\tag{6}
\]

\[
\boxed{
 M_{\rm init}\le
 C L\beta^{100L}
 \left\{n^2(1+m/\gamma)Z^2+npZ^3+p^2Z^5\right\}
 +Cp(d+1).
}
\tag{7}
\]

The memory unit in (7) is real coordinates. Activation calls and universal
scalar operations fit the arithmetic order in (6) when counted as the
stated primitives; fully charged evaluator costs must be added. Input
storage is explicit. This is offline initialization, not an online speedup;
in particular the bound has an `n^2` times logarithmic-factor term.

The displayed gap degree four comes from a deliberately direct collocation
implementation, not a lower bound. At fixed `gamma`, its combined sample
degree can be five because `m(1+m/gamma)^4` includes `m^5/gamma^4`.
The panel-selection term has degree three in `p`. No exponential dependence
on `m`, `1/gamma`, `Y` or `d` occurs in these operation counts.

## Unseen-input compiler: parameter expansion boundary

The companion [COMPILER_PARAMETER_ACCOUNTING.md](COMPILER_PARAMETER_ACCOUNTING.md)
gives absolute-constant downstream formulas in the actual program counts
and logarithmic cap/conditioning certificates. Its post-freeze addendum
composes their numerical certificates with the explicit physical program.
The coefficient-generation, finite-precision and sampling algorithms are
large-degree polynomials. This is not a fourth-degree result.

For clarity, the local compiler count can be bounded by
`M <= C beta^(301L) (m+d+2)(1+m/gamma)^3 Z^6`, and its logarithmic
numerical certificate by
`Theta <= C beta^(200L)(1+m/gamma) Z^2`.
They are only substitution variables in this paragraph, not new global
problem parameters. Normalized labels and a separately retained output
scale remove divisions by small `Y` from the internal row graph. Data
access and the encoding of that scale remain charged under the stated
input interface; arbitrary real-number inputs are not declared finite bit
strings by this normalization.

Substitution into the counted compiler formulas yields the following
conservative table. **Multiply every row by the explicit common factor
`C beta^(65000L)`, where `C` is universal**, and add the supplied input,
certificate and primitive costs described below.

| Resource | Parameter-explicit algorithmic bound |
|---|---:|
| Retained model bits | `(m+d+2)^23 (1+m/gamma)^72 Z^144` |
| Retained plus peak training/query bits | `(m+d+2)^66 (1+m/gamma)^204 Z^408` |
| Complete virtual-source warmup work | `n(m+d+2)^146 (1+m/gamma)^454 Z^908` |
| Peak temporary warmup bits | `n(m+d+2)^10 (1+m/gamma)^31 Z^62 + (m+d+2)^54 (1+m/gamma)^168 Z^336` |
| All compact acquisition updates, excluding queries | `(m+d+2)^148 (1+m/gamma)^460 Z^920` |
| One unseen-input query | `n(m+d+2)^189 (1+m/gamma)^584 Z^1168` |

These bounds include rounded training-data literals and numerical query
workspace: `m(d+1)` is at most a quadratic in the counted program size,
and its required precision is below the query precision already counted.
Keeping `m+d+2` exposes dimension explicitly. Because `d<=m`, one can
replace it by a numerical multiple of `m` without changing any conclusion.
All powers of the displayed scientific parameters are absolute. There
is no label-size inverse polynomial in these internal counts. The
activation/depth factor is polynomial in `beta^L`, but with a very large,
unoptimized degree. None of this is a practical-efficiency assertion.

For example the retained row is the product
`M^23 Theta^3`: its gap power is `3*23+3=72`, logarithmic power
`6*23+2*3=144`, and activation power is `301*23+200*3=7523`, below
65000. The query row similarly has powers `3*189+17=584`,
`6*189+2*17=1168`, and `301*189+200*17=60289`. The other rows follow
the same direct multiplication; no coefficient is traded against `n`.

The bound is for the specified activation/data-primitive computational
model. Add the finite problem/certificate description length when retained,
its acquisition/verification work, and the explicitly charged evaluator
calls and single-call workspace in the compiler note (33). An arbitrary
activation evaluator cannot have its implementation size/time bounded
solely by the analytic envelope `beta`. This qualification is shared with
the preceding theorem, not a new bounded-activation assumption.
Obtaining a query's coordinates to the prescribed context precision also
has its own input-access work and workspace. The counted rounded `d`-word
query buffer is not a bound on an arbitrary original input encoding or
its precision evaluator.

[COST_INTERFACE_EVALUATORS.md](COST_INTERFACE_EVALUATORS.md) expands
the evaluator counts and required precision into the same major parameters.
It also exposes the extra raw-label access precision as `Y` decreases and
the output-scale description cost. Thus the internal absence of an inverse
`Y` power is not a claim of cost-free tiny-label input/output.

The bound on all updates also bounds one update. There is no recalibration
step. Warmup generates an independent original-law virtual source; it does
not read and reproduce a specified realized dense root. The old panel
construction, by contrast, does use its specified dense reference and
retains its sharper matched-root accuracy.

## Accuracy and sufficient widths have not become uniform in parameters

The finite-panel error on the full original label interval remains

\[
 C\beta^{42L}Y\frac m\gamma
 \max\!\left(1,\sqrt{\frac m\gamma}\right)
 \frac{(1+\sqrt{\log(en)})e^{32\sqrt{\log(en)}}}{n}.
\tag{8}
\]

It is uniform over the predeclared panel and all physical times, and is
smaller in probability than the actual dense-pair trajectory discrepancy
for fixed admissible nonzero-label data with `m>=2`. Under the simpler
cap the earlier sharper numerical error formula is unchanged. The new
coefficient producer fits inside the same source tolerance, so no new
error theorem or label restriction is needed.

The unseen decoder retains its same all-sphere/all-time dense-pair
**upper-certificate-scale** interpretation. Its numerical ridge and roundoff
are controlled using explicit, possibly very large circuit-propagation
bounds. The much smaller physical propagation bound used for the statistical
root-width remainder remains the inherited one. A crude inverse-noise
circuit bound must not be substituted for that physical bound: it is a
precision certificate, not a useful statistical error estimate.

Three width qualifications remain distinct:

1. The fitting, finite-query source, and insertion probability events,
   including their displayed deterministic gates and their unquantified
   stochastic success width. For instance the panel source still requires
   `n^(-1) <= min(1,Y,16Ym/gamma)` and its complex-time strip gates.
   The new numerical scheduling does not make those scientific events
   effective or polynomial in all problem parameters.
2. Explicit numerical/sampling conditions. The block sampler needs
   `n >= 512 max(K_*,1)`, where `K_*` is the computed information budget
   in compiler (19), not an unknown problem constant. A conservative
   sufficient version after substitution is
   `n >= C delta^(-1) beta^(4000L)(m+d+2)^11(1+m/gamma)^34 Z^68`.
   Gaussian sampling and projection/certificate guards are also checked
   by the displayed numerical construction.
3. The inherited comparison of the statistical logarithmic root-width
   remainder with the chosen dense-pair certificate. Its fixed-label
   eventual absorption is not a parameter-uniform onset theorem. In
   particular a full polynomial sufficient width as `Y` tends to zero
   is not established here. Eventual dense-quadratic work also requires
   that the displayed query prefactor times `Z^1168` be at most a
   constant multiple of `n`; it is not asserted at practical widths.

Thus the new result exposes polynomial **algorithmic resource factors**
above the existing success thresholds. It does not claim a low-degree
unseen decoder, a polynomial all-parameter success width, a finite-bit
panel-training theorem, or a numerical integration step count for the
panel ODE. These are not consequences of the old logarithmic exponents.

## Checks and provenance

The three source notes were derived in scoped author routes with disjoint
initial inputs and write ownership. The lead read their complete final
derivations and checked their composition. The panel route subsequently
reconstructed the full-label radius envelope, aliasing/node-error budget,
runtime constants and warmup assembly; its recorded post-freeze check is
at the end of `FINITE_PANEL_PARAMETER_COSTS.md`. The physical-program
route separately checked the composed coefficient producer and work/space
bounds, including the original horizon and exact paired-image convention.
The compiler route subsequently checked the expanded unseen table and
explicit sampler-width substitution. These are bounded author cross-checks,
not isolated reviews of every inherited stochastic theorem or promotion.

The computational audit deliberately separates exact-real coordinate
counts, precision-counted numerical work with external primitives, and
fully charged input/evaluator costs. No experiment, executable compressor,
practical cost benchmark, maintained-book edit, or Git mutation is claimed.
