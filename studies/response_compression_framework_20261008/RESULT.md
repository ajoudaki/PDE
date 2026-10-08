# Response compression: one organizing principle, two reduction mechanisms

## Recommended framing

The three constructions compress the forward and backward responses that
generate learning, rather than directly approximate an arbitrary dense
weight matrix. Legendre compresses their **history** while keeping neuron
coordinates. Harmonic and the new finite-panel Logarithmic construction
compress their **neuron-space geometry** and use the same selected-network
runtime. Their different source builders reflect different query contracts.

Thus the natural organization is two mechanisms, not three unrelated
algorithms and not a literal chain of increasingly truncated versions of
one optimizer:

- Temporal-memory compression: Legendre.
- Selected response-space compression, with two source builders:
  whole-sphere Harmonic and finite-panel Logarithmic.

This is a reformulation of the existing constructions. No error theorem,
sample exponent, width exponent, activation class, label allowance or
runtime is strengthened by this note. The current third method means the
new **coupled-reference, finite-panel, real-coordinate** construction with
third logarithmic power. It does not mean the older independent-reference
finite-word decoder that remains in the current paper.

## 1. The common exact object

Use the canonical width-\(n\), \(L\)-hidden-layer network on \(m\)
training inputs, with normalized input \(v=x/\sqrt d\), first matrix
\(W^{(1)}\), hidden matrices \(W^{(\ell)}\), and stored readout
\(w\). In formulas,

\[
 z^{(1)}(x)=W^{(1)}x/\sqrt d,\qquad
 z^{(\ell)}(x)=W^{(\ell)}h^{(\ell-1)}(x),\qquad
 h^{(\ell)}(x)=\phi_\ell(z^{(\ell)}(x)),\qquad
 f_n(x)=w^\top h^{(L)}(x)/n.
\]

The training residual is \(r_a=f_n(x_a)-y_a\). Backward responses exclude
this residual:

\[
 \delta_a^{(L)}=w\odot\phi_L'(z_a^{(L)}),\qquad
 \delta_a^{(\ell)}=\phi_\ell'(z_a^{(\ell)})\odot
          W^{(\ell+1)\top}\delta_a^{(\ell+1)}.
\]

Mean-square loss and mobilities \((n,1,\ldots,1,n)\) give, at a hidden link,

\[
 W^{(\ell)}(t)-W_0^{(\ell)}
 =-\frac2{mn}\sum_{a=1}^m\int_0^t
 r_a(s)\delta_a^{(\ell)}(s)h_a^{(\ell-1)}(s)^\top\,ds.
 \tag{1}
\]

This is integration of the exact dense flow, not an approximation. For
arbitrary vectors \(u\) and \(v\) in the adjacent neuron spaces, multiplication
and transposition give

\[
\begin{aligned}
 W^{(\ell)}(t)u
 &=W_0^{(\ell)}u-\frac2m\sum_a\int_0^t
 r_a(s)\delta_a^{(\ell)}(s)
       \frac{h_a^{(\ell-1)}(s)^\top u}{n}\,ds,\\
 W^{(\ell)}(t)^\top v
 &=W_0^{(\ell)\top}v-\frac2m\sum_a\int_0^t
 r_a(s)h_a^{(\ell-1)}(s)
       \frac{\delta_a^{(\ell)}(s)^\top v}{n}\,ds.
\end{aligned}
\tag{2}
\]

Forward evaluation and backpropagation therefore need the initialized
actions in both directions and the pairings of the relevant responses.
This is the shared information to preserve. It is not enough to preserve
only outputs, only forward features, or the eigenvalues of the initialized
weight matrices. An instantaneous rank-m update also does not imply that
the accumulated learned matrix has rank at most m.

## 2. Legendre: compress the integral, retain the ambient neurons

The Legendre model uses its own reconstructed network, not sampled future
dense histories. Its moving residual clock is
\(\tau(t)=1+\int_0^t\widehat\rho(s)ds\), where
\(\widehat\rho=\|\widehat r\|_2/\sqrt m\). Where this clock
advances, the histories in clock time are the forward feature and the
weighted backward response \(\widehat r_a\widehat\delta_a/
\widehat\rho\). The prefix on [0,1] is constant for the forward
history and zero for the backward history.

In this paragraph only, write \(h\) and \(b\) for those two histories
and \(P\) for orthogonal projection onto degree-below-\(q\) polynomials
on \([0,\tau]\).
Componentwise orthogonality gives the exact identity

\[
 \int_0^\tau bh^\top\,d\xi
 =\int_0^\tau(Pb)(Ph)^\top\,d\xi
  +\int_0^\tau(b-Pb)(h-Ph)^\top\,d\xi.
 \tag{3}
\]

The two cross terms vanish entry by entry because a retained scalar
polynomial is orthogonal to a discarded scalar history. Legendre stores
the unnormalized moments producing the first term. Both moment vectors
still have n coordinates. Differentiating the moments gives its existing
autonomous ODE; that ODE has no residual denominator and is regular at
zero residual. The exact defect is a product of endpoint projection
errors, not a newly assumed single source-error estimate.

The first weights and readout remain ordinary width-n moving arrays.
All initialized n-by-n hidden mixers remain fixed retained data.
Legendre consequently compresses moving history memory, not the whole
environment. Its proof and optimizer are not replaced by the selected
model's readout correction.

## 3. Harmonic and Logarithmic: one selected-network construction

The relevant alternative to retaining n-dimensional vectors is to build
a fixed low-dimensional source space at each layer. A source expansion
has the form

\[
 h^{(\ell)}(t,x)\ \approx\ \sum_{j=1}^R u_j^{(\ell)}b_j(t,x),
 \qquad u_j^{(\ell)}\in\mathbb R^n,
 \tag{4}
\]

and similarly for the other required sources. Here R is a local
coefficient-count bound, not the model's free order; the scalar basis
functions b_j determine which family is covered. Take the span of these
computed coefficient vectors, including paired initialized images and
the exact initialization additions. Select neuron indices I and a
positive metric M so that

\[
 (u_I)^\top Mv_I=\frac{u^\top v}{n}
 \quad\hbox{for all source-space vectors }u,v.
 \tag{5}
\]

This exact identity and the controlled source errors preserve the
pairings in (2). The initialized small mixers reproduce the paired
forward and transpose actions. Restriction to actual coordinates also
satisfies \(\phi(z)_I=\phi(z_I)\), so the nonlinear activation is
retained. The metric's comparison with a diagonal positive metric
controls these coordinatewise nonlinearities; arbitrary isometries alone
would not suffice.

Both constructions then use the same runtime on the certified positive
training-Gram branch: selected first and hidden
matrices, a raw readout, label deficits, metric adjoints, the positive
algebraic response Gram, and the corrected effective readout. The
correction enforces agreement between training predictions and the
retained deficits. It is essential: these prescribed directions are
not asserted to be ordinary gradient flow of the corrected predictor.

The source spaces, selected indices and initialized small arrays differ
between builders. "Same runtime" means identical construction rules and
equations applied to those different arrays, not identical compressed
trajectories. The original width-n bases, jets, quadratures and temporal
panels are discarded after setup; no time table drives the runtime.

### Builder A: whole-sphere Harmonic

The scalar basis in (4) consists of temporal Chebyshev polynomials times
real spherical harmonics. It covers time and every input direction at
once. The existing builder includes forward/backward sources and both
initialized image families over the sphere, plus the exact initialized
training features, constant and first-weight columns.

The price of certifying every possible query is the spatial harmonic
count. The current total retained width dependence is
\(O([\log(en)]^{3d+2})\), at dense-variability accuracy, with its existing
explicit activation/depth, label and sample/gap prefactors unchanged.
New query inputs need not be known during setup.

### Builder B: finite-panel Logarithmic

The input set consists of the m training inputs and p additional passive
inputs, fixed before initialization. Passive labels are never supplied
and passive inputs contribute no training force. Instead of approximating
a function over the whole sphere, use an exact discrete input dictionary
and approximate each associated time curve. Forward sources and their
initialized images are required on the entire panel; backward sources
and their transpose images only on the training inputs.

The new residual-adapted temporal pieces exploit the growing complex-time
domain as the residual decays. This supplies the already proved
third-power retained bound. The input dictionary removes the global
spatial harmonic count; the adaptive temporal construction reduces the
former finite-panel fifth power to third power. These are two different
savings and should be explained separately.

The model still evaluates a network, not a stored list of endpoint
answers. Nevertheless its accuracy certificate is confined to the
declared panel; evaluability outside the panel is not a theorem of
accuracy there. Its input-span reduction is likewise exact only for the
promised panel and retains its separately counted input map.

## 4. A genuinely shared theorem interface for the last two

State the selected-source-to-dynamics result once, with the promised query
set explicit. Its hypotheses must include coordinate-error approximation
of every required source, exact paired computed mixer images, the exact
initialization additions, the source metric and diagonal comparison,
and the existing initialization/fitting/carrier/label conditions.

The deterministic argument then has the same sequence for both builders:
source approximation controls pairings, paired initialized actions and
integrated learned actions; corrected-readout stability controls feedback
through the compact optimizer; separate fitted-tail estimates extend the
comparison to all physical time and the endpoint. No source-error
derivative appears in this interface. Piecewise polynomial approximants
are therefore allowed without requiring their pieces to join analytically.

The source builders discharge these hypotheses separately. They do not
share the same analytic-domain theorem: one has joint time/input-tube
control, while the other has the enlarged time domain for declared
queries. Their width/confidence onsets and scalar-evaluation qualifications
must remain attached to the resulting statements.

For a clean main theorem both can retain the existing stronger target
Y/n, where Y is fixed label RMS. For m>=2 this is negligible relative
to the dense-pair discrepancy on the corresponding query set, using the
existing training-input lower witness. The supremum remains over the
whole sphere for Harmonic and over the finite panel for Logarithmic.
One can write the common norm using an explicit query set, without
pretending those two sets are equal.

Legendre belongs to the same response-based story, but uses its own
projection-defect and stability theorem. Do not insert it into the
selected-source theorem merely to make every line look identical.

## 5. One exact cosmetic improvement: a common polynomial language

The new temporal source proof uses degree-K Taylor polynomials separately
on its adaptive time intervals. Each such polynomial can instead be
written in a Chebyshev basis on the same interval. This requires no new
regularity theorem and changes neither the polynomial nor its error.

To check the source space, write a vector polynomial as a coefficient
matrix times its scalar monomial vector. The Chebyshev basis is related
to monomials by an invertible triangular matrix, because each degree-k
Chebyshev polynomial has a nonzero degree-k leading coefficient. The new
vector coefficients are consequently invertible scalar linear
combinations of the old ones, so their spans are identical. Applying a
fixed initialized mixer commutes with this scalar coefficient change,
preserving the exact paired images as well. Doing this independently on
each temporal piece preserves the span of their union.

Thus the exposition may consistently say:

- Harmonic: a global time-polynomial and spherical-harmonic dictionary.
- Logarithmic: a piecewise time-polynomial and discrete-input dictionary.

The initializer may continue computing Taylor jets and coefficients as
before. No retained-state improvement follows merely from the change of
basis; finite-precision conversion must have its errors charged if
actually performed. Legendre's orthogonal moment algorithm is not changed
to Chebyshev by this observation.

## 6. Resource and scope comparison

The table reports width dependence at the existing dense-variability
accuracy level. All other admissible parameters, including panel size
and confidence, are fixed here; their full existing formulas are not
replaced by universal constants.

| Construction | What is compressed | What remains | Certified query set | Width dependence |
| --- | --- | --- | --- | --- |
| Legendre | The temporal history of paired writes | Width-\(n\) response vectors and dense initialized mixers | Whole sphere | \(n^{5/4+o(1)}\) learned coordinates; \(O(n^2)\) additional fixed storage |
| Harmonic | Neuron-space geometry of the time/input response family | Selected network and its metrics | Whole sphere | \(O([\log(en)]^{3d+2})\) total retained real coordinates |
| Logarithmic, finite-panel | Neuron-space geometry of the declared curves, with adaptive temporal pieces | The same selected-network construction and metrics | Declared training/passive panel | \(O([\log(en)]^3)\) total retained real coordinates |

Storage counts do not become setup-time or bit-complexity results under
this unification. In particular, the finite-jet panel compiler may be
very expensive. The stronger reference-coupled panel result must not be
confused with the older decoder's independent-reference finite-word
contract. No neuron-coordinate reduction is necessary for Legendre's
whole-sphere query coverage; it retains the full initialized environment.

## 7. Proposed paper organization

The main mathematical story can focus on the last two constructions:

1. Learning as integrated forward/backward response pairings: equation (1).
2. A common selected-response-space model: metric, paired initialized
   actions, nonlinear gates and corrected autonomous dynamics, defined once.
3. One source-to-dynamics theorem, with an explicit query set.
4. Two source builders and resulting rows of the main compression theorem:
   whole-sphere Harmonic, and adaptive finite-panel Logarithmic.
5. Dense-variability calibration and separate retained/setup/query costs.

Legendre supplies the natural motivating example and a comparison method:
compressing history already saves moving state, but leaves dense mixers.
Its full construction and proof can remain in the appendix. This connects
all three without forcing three parallel optimizer definitions into the
main argument. Keep the existing method names; use the subtitles
"temporal memory", "whole-sphere response space" and "finite-panel
response space" to expose the distinction rather than renaming everything.

## 8. What is not newly proved

Applying the flaring-time improvement to full-sphere Harmonic is a useful
next question, but not an immediate consequence of this reformulation.
One must control the enlarged time domain uniformly over the complex
input tube and the required paired source families. Fixed-panel control
does not supply that theorem. No improved Harmonic exponent is claimed.

Nor do physical-time analytic expansions automatically make Legendre's
residual-clock histories endpoint-analytic; they include a normalized
residual direction and a fixed prefix. No improved Legendre order or
sample dependence is obtained by exchanging basis names. The immediate
benefits are an exact common formulation for the last two models and a
clean division between source construction and dynamical stability.

## Sources and check status

This is a presentation-level synthesis, not a fresh audit or promotion
of the source theorems. The lead and a fresh scoped reader independently
reconstructed the exact common integral, the different projection domains,
and the selected-network correspondence. The reader then checked the
panel/runtime equivalence and the limitation on transferring flaring
domains. The basis-change observation is proved directly in Section 5.

Actual source passages read for this synthesis:

- paper/methods.tex and paper/results.tex, complete; paper/main.tex setting.
- paper/integrated_appendix.tex: complete Legendre runtime (2250--2420),
  selected runtime (3195--3447), Legendre projection proof
  (10320--10530), selection proof (11409--11546), and source energy
  interface (11658--11789). The scoped reader also checked the complete
  source-expansion and applicable comparison passages.
- initialization_panel_compression_20261008/PANEL_BOUND.md: the source,
  selected-runtime and all-time interfaces in Sections 1--3, the
  variability distinction in Section 4, and exact input-span reduction
  in Section 9; these were also read in the preceding proof investigation.
- adaptive_clock_compression_20261008/RESULT.md and FLARING_ROUTE.md
  Section 7; the full proof and internal check were read in the immediately
  preceding investigation that established this result.

The existing analytic class allows unbounded activation values but retains
its strip and bounded-derivative requirements. No new label condition,
passive labels, future observed dense trajectory, or runtime source table
is introduced by this framing. The framing stage edited no existing paper,
code, experiment or source study. The user subsequently authorized its
implementation in the working paper; the current integration scope and
checks are recorded in [README.md](README.md).
