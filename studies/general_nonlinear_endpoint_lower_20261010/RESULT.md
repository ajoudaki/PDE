# General nonlinear fitted-endpoint variability

## Latest result: the paper's full nonaffine activation class

The all-layer extension is proved, retaining the proper-training-span and
orthogonal-query geometry of the preceding endpoint theorem. Every hidden
layer may use an arbitrary activation that is not affine on the real axis
in the compact paper's strip-analytic, bounded-strip-derivative class, and
different layers may use different activations. Activation values remain allowed to be
unbounded. The canonical Gaussian initialization, fully trainable hidden
weights, positive feature-Gram gap and original sufficient label cap

\[
0<Y\le(\gamma/m)\beta^{-30L}
\]

are unchanged. For a unit vector $v$ orthogonal to the training span,
fixed before initialization, and every fixed $0<\delta<1$, there is a
constant $C>0$, independent of width, such that

\[
\Pr\left\{
 |f_n(\infty,\sqrt d\,v)-\widetilde f_n(\infty,\sqrt d\,v)|
       \ge\frac C{\sqrt n},\quad\text{both runs fit}
\right\}\ge1-\delta
\]

at every sufficiently large individual width. The coefficient and onset
width may depend on the fixed data, labels, activations, depth and
confidence. Relative to the paper's activation class, **the only added
activation assumption is that every layer activation is nonaffine**. There
is no centering, normalization, oddness, extra label smallness condition or
bounded-value assumption. The width threshold remains unquantified. This
also gives the supremum bound over separated test directions containing
the orthogonal query; it is a fitted-endpoint result, not a bound at all
training times.

The proof and complete dependency links are in
[GAUSSIAN_ORACLE_ENDPOINT.md](GAUSSIAN_ORACLE_ENDPOINT.md). It approximates
the actual fitted parameters to $O(n^{-16})$ using only a polylogarithmic
number of initialized-matrix actions. Exact conditioning on those actions
leaves fresh Gaussian directions in every hidden layer. A projected
innovation argument and a nonlinear Hermite/Stein argument prove the
endpoint fluctuation directly, avoiding the earlier unresolved comparison
to frozen features. Nonconstancy gives the layerwise innovation constants;
nonaffinity gives a strictly positive higher-Hermite variance in the final
readout. Compactness makes both bounds uniform over all conditioned means
and noise scales that occur in the proof. The auxiliary approximation is
not a replacement for the actual dense model in the theorem.

Separate reconstruction reports cover the numerical oracle module,
projected-Gaussian lemmas and complete assembly. The activation
generalization is reconstructed in `GENERAL_ACTIVATION_ENDPOINT_CHECK.md`.
The result is internally checked, not promoted; paper and book files are
unchanged. Full-span training configurations remain outside this theorem.

## Current target and status

The final user clarification asks only about the fitted endpoint. Let
$\mathcal X_\varepsilon$ be the subset of the input sphere whose normalized
directions have distance at least $\varepsilon>0$ from both signs of every
training direction, assumed nonempty. The target is

\[
\mathbb P\left\{
 \sup_{x\in\mathcal X_\varepsilon}
 |f_n(\infty,x)-\widetilde f_n(\infty,x)|\ge\frac{C}{\sqrt n},
 \quad\text{both runs fit}
\right\}\ge p
\]

for every sufficiently large individual width, with positive $C,p$ depending
only on the fixed problem and never on width. The original two-tanh endpoint
result has fixed-positive-probability scope; a prescribed-confidence version
would be an additional strengthening. Every layer is nonaffine and belongs
to the compact paper's strip-analytic, bounded-derivative activation class.
The positive training feature-Gram gap, nonzero fixed labels, and existing
small-label cap remain unchanged. Training directions are pairwise distinct
up to sign. Full-span training is allowed.

Status: **the general trained-endpoint lower bound is not proved or disproved**.
A transient request for a lower bound at every training time was withdrawn;
`ALL_TIME_OBSTRUCTION.md` is irrelevant to this restored endpoint-only target.

## Earlier actual-endpoint extension: arbitrary fixed depth, odd activations

The requested activation/depth extension of the old endpoint example now has
a positive result **retaining its orthogonal-query geometry**. Suppose the
training directions span a proper subspace and $v$ is a fixed unit vector
orthogonal to it. For arbitrary fixed depth, arbitrary nonzero labels under
the paper's existing cap, and arbitrary layerwise mixtures of
$\tanh z$, $\arctan z$, $\sin z$, $\operatorname{erf}z$,
$\operatorname{arsinh}z$, and $z+\tanh z$,

\[
 \mathbb P\left\{
 |f_n(\infty,\sqrt d\,v)-\widetilde f_n(\infty,\sqrt d\,v)|
 \ge\frac{\sqrt{Q^{(L)}_{11}\,y^\top(Q^{(L)})^{-1}y}}{8\sqrt n},
 \quad\text{both runs fit}\right\}\ge\frac12
\]

at every sufficiently large individual width. This is the **actual nonlinear
trained endpoint**; no hidden layer is frozen. Values may be unbounded, as
the last two activations illustrate. An unquantified width threshold remains.
Since $\lambda_{\max}(Q^{(L)})\le\operatorname{tr}Q^{(L)}
=mQ^{(L)}_{11}$ and $\|y\|_2^2=mY^2$, the displayed lower threshold is
at least $Y/(8\sqrt n)$. Thus this simpler threshold is valid too.

The proof in `ODD_DEPTH_ENDPOINT.md` also covers every odd activation in the
paper's class satisfying $Q^{(L)}_{11}\ge\beta^{-40L}$; the listed families
have the stronger elementary bound $Q^{(L)}_{11}\ge32^{-L}$. The audit also
checks the two additional examples erf and arsinh: both are odd and monotone,
have bounded derivative on a common strip, and obey $\phi(u)\ge u/2$ for
$0\le u\le1$, so the same scalar-variance recursion applies. Odd activations
normalized to unit layerwise Gaussian second moment are covered as well.
Without that variance qualification the note states its extra sufficient
activation-dependent label cap explicitly; it does not pretend the original
cap implies it automatically. The proof passed the fresh isolated
reconstruction in `ODD_DEPTH_ENDPOINT_CHECK.md`, including the simpler
$Y/(8\sqrt n)$ consequence and the erf/arsinh examples.

The new mechanism is a sharp comparison of the fitted readout to the
initialization-feature interpolating readout, followed by a Gaussian-query
$L^2$ estimate of the **whole nonlinear endpoint correction at scale
$1/\sqrt n$**. It bypasses a deep conditional covariance lower bound. The
frozen-feature comparator is used in the proof, not substituted for the
trained model in the conclusion.

This odd theorem does **not** cover raw GELU, SiLU, softplus, sigmoid,
arbitrary shifted activations, or full-span data. The new partial extension
below permits several of them in the last hidden layer.
`DEPTH_COVARIANCE_ROUTE.md` and
`PRODUCT_QUERY_ROUTE.md` show that specific covariance/perturbation steps
fail for noncentered activations; they do not disprove an endpoint theorem
for those activations. A targeted primary-literature check also found no
ready-made arbitrary-depth, adaptive-training covariance theorem: the
relevant result in
[Schröder et al., Theorem 4.4 and Appendix B](https://arxiv.org/html/2402.13999v2)
is a two-layer covariance approximation, not the needed trained endpoint
lower bound. It is not used as a premise of the new proof.

## Earlier last-layer extension and comparison-route limitation

The initial 2026-10-11 continuation retained the proper-span/orthogonal-query
geometry and sought to remove oddness from every layer, not merely
boundedness of activation values. The following narrower theorem predates
the full nonaffine-class result above. Its comparison-route gap is bypassed
by the new oracle argument, not silently assumed away.

`NONODD_ENDPOINT_PROGRESS.md` gives a complete proof of the following narrower
actual-endpoint extension, checked independently in `NONODD_ENDPOINT_CHECK.md`:

- Layers \(1,\ldots,L-1\) may use arbitrary mixtures of the previously checked
  odd families.
- The final hidden activation may be **GELU, SiLU, or softplus**, including
  their unbounded values.
- The existing small-label condition is unchanged. For two independent
  actual trained networks, at every sufficiently large individual width,
  \(\Pr\{|f_n(\infty,\sqrt d\,v)-\widetilde f_n(\infty,\sqrt d\,v)|
  \ge C/\sqrt n,\ \text{both fit}\}\ge1/2\), with a positive coefficient
  depending on the fixed problem but not width.

The exact coefficient and proof are in that note. More generally it permits
any last activation in the paper's class whose **centered Gaussian variance**
is at least \(\beta^{-40L}\). This must not be replaced by an uncentered second
moment lower bound. For the three named activations it follows automatically
because their odd part is \(z/2\).

There is also substantive arbitrary-depth progress with **no oddness
assumption at any layer**. `NONODD_INNOVATION_ROUTE.md` proves conditional
root-width anti-concentration for frozen-feature interpolation, given all
active initialization. `NONODD_SCALAR_ROUTE.md`, Section 5, proves a sharp
root-width centered comparison between the actual endpoint and a comparator
that retains the actual trained means as biases while freezing centered
mixing. This recovers the odd proof's stability constant, with no additional
label cap. `NONODD_MOMENT_ROUTE.md` also closes a previous two-layer
unbounded-activation moment gap using actual training-source moments.

The missing step is not hidden: the mean-adapted comparator is **different
from frozen-feature interpolation**. Its trained biases couple the initialized
rows, so the frozen-feature CLT does not give its anti-concentration. Nor does
the top uncentered second moment ensure a useful lower bound on its query
fluctuations. A direct fluctuation lower bound for this comparator or the
actual fitted predictor is still needed. Explicit counterexamples in the
route notes reject two tempting uniform covariance/moment shortcuts, not the
desired endpoint theorem itself.

## What the analysis resolves

### Nonaffinity removes initialization feature degeneracy

For every finite list of unit directions distinct up to sign, the population
feature Gram is strictly positive definite after every nonlinear layer. This
includes a separated query added to any full-span training configuration.
Bounded real derivative plus nonaffinity implies nonpolynomiality; directional
derivatives isolate any purported linear relation between the first-layer
ridge functions and would force the activation to be polynomial. Full support
of the later Gaussian vectors then propagates strict positivity.

This is proved in Sections 2--3 of `LINEAR_RESPONSE_ROUTE.md`, with an
independently derived Taylor-coefficient proof in `OBSTRUCTION_ROUTE.md`.
These are population statements, not finite empirical full-rank assertions
when the number of queried points exceeds the width.

### The frozen-initialization endpoint has a root-width lower bound

Under the stated data and activation assumptions, the actual finite-depth
initialized network's **readout-only** fitted predictor has nonzero
root-width variability at every fixed separated query. Its positive
coefficient is obtained from the conditional variance of the final Gaussian
query coordinate given its training coordinates. Conditioning on preceding
layers and controlling a triangular central limit expansion proves a
fixed-confidence lower bound without needing a full depth-wise Gram CLT.

This is proved in Sections 4--6 of `LINEAR_RESPONSE_ROUTE.md`. It permits
unbounded activation values because bounded derivatives imply at most linear
growth and all required Gaussian moments are finite. Labels are arbitrary
nonzero vectors. Constants may depend on the actual activation, labels, data,
query and confidence. **This comparator freezes hidden features and is not
the requested nonlinear dense endpoint.**

### A general-activation covariance lemma strengthens one old proof step

`POSITIVE_ROUTE.md` proves a width-independent covariance gap for
$\phi(WZ)$ with an independent standard Gaussian vector $Z$, for every
nonaffine globally Lipschitz analytic activation and every matrix $W$ in a
fixed small Frobenius neighborhood of an initialized Gaussian mixer. The
proof uses its complete high-order Hermite tail rather than one specially
chosen tanh coefficient. The permitted matrix movement does not need to
shrink with the size of a particular nonlinear coefficient. A conditional
endpoint moment argument also removes oddness and bounded-value assumptions.

This lemma requires the stated independent Gaussian query representation.
It does not assert that such a representation exists after general deep
training or for full-span training data.

## The remaining substantive gap

The original two-tanh endpoint proof conditions on an untouched first-layer
Gaussian block orthogonal to the training span. With full-span training,
that block does not exist. Nonparallel query geometry establishes fresh
nonlinear randomness at initialization, but it does not preserve its
independence from the subsequent training path.

Section 3 of `POSITIVE_ROUTE.md` gives an exact admitted tanh example in which
a Gaussian matrix direction invisible to the initial training features enters
their second time derivative and the training prediction's third derivative.
Thus conditioning on the initial training features cannot be substituted for
conditioning on the whole training trajectory. This is a counterexample to
that proposed proof step, not to the desired endpoint theorem.

`ENDPOINT_IDENTITY.md` derives the exact actual-endpoint decomposition into
initial-feature interpolation and a nonlinear training correction. The
fitting estimates give a fully explicit correction of order $Y^3$, with
constants polynomial in $m/\gamma$ and activation/depth constants, uniform
in width. At fixed positive $Y$, that does not control fluctuations of order
$Y/\sqrt n$. The correction and initialization-kernel fluctuations could be
correlated; an absolute small-label estimate cannot rule out cancellation.

To finish the full-scope requested theorem, one needs a fluctuation-scale endpoint
argument for the actual trained network and a proof that at least one
separated query retains nonzero fluctuation. A scalar endpoint central limit
theorem with positive variance at one such query would suffice; a functional
CLT is not necessary. No such bridge for general non-odd activations and
full-span training is supplied by these notes. The odd orthogonal-query
extension above resolves only its stated subclass. No smaller
label cap, width-dependent labels, frozen-feature replacement, or transient
lower bound is being substituted for the requested result.

A separate direct route, `DIRECT_ROUTE.md`, proves finite-width smoothness
and the derivative formula for the actual fitted parameter map. Although
many random hidden-parameter directions survive interpolation, this does
not show that any separated query detects them at the required scale.
Its explicit second/fourth-moment criterion would imply the target, but
those width-uniform moment bounds have not been established. This route
therefore does not bypass the same substantive missing nondegeneracy.

## Checks and disposition

- `NONODD_ENDPOINT_CHECK.md` reconstructs the final-layer-nonodd actual
  endpoint theorem, its conditional transfer, constants, and concrete
  activation examples. Its PASS does not remove oddness at earlier layers.
- `NONODD_COMPARISON_CHECK.md` checks the arbitrary-depth mean-adapted
  comparison and scalar reduction. The needed hidden-layer index range was
  made explicit and the final correction rechecked. It does not certify
  anti-concentration for the mean-adapted comparator.
- `NONODD_ROUTE_CHECK.md` checks the conditional frozen-feature fluctuation
  argument, extraction of moments from the existing source proof, and the
  precisely scoped shortcut counterexamples. Its source-moment verdict is
  an extraction check, not a new full audit of the entire source proof.
- `ODD_DEPTH_ENDPOINT_CHECK.md` independently reconstructs the actual trained-
  endpoint extension, its conditioning, readout comparison, fluctuation-scale
  remainder, conditional normal approximation, activation examples and
  probability constants. Its PASS concerns only that stated subclass.
- `ENDPOINT_IDENTITY_CHECK.md` reconstructs the exact finite-width identity,
  the mobility and sample factors, and every coefficient in its cubic bound.
- The activation/initialization partial lemmas passed the separate scoped
  reconstruction in `PARTIAL_RESULTS_CHECK.md`, tied to its recorded source
  hashes. That review concerns the
  displayed lemmas only, not a proof of the unresolved endpoint theorem.
- The paper, the established book, the old study, and the Git index are
  unchanged. No numerical experiment was run.
