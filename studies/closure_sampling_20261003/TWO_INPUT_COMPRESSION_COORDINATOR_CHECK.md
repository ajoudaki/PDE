# Coordinator reconstruction of the two-input compression result

2026-10-03. Complete-chain internal mathematical check, normalization
reconciliation, source-version record, and scope audit. The coordinator
authored the complex-source proof and contributed to the second-layer
feature-motion proof. This is therefore not an independent promotion review.
The separate reconstruction reports retain their own authorship and scope.

## 1. Contract, sources and reading coverage

This continues the existing neuron-sampling study. The present user asks
for a positive sublinear-state construction or a genuine state lower bound
for at least two training inputs, allowing sufficiently small fixed labels
but requiring both sign patterns. The previously authorized direct-dense
route is used. The realized reference has two hidden layers of width $n$,
tanh activation, canonical independent Gaussian initialization, zero
readout and the manuscript's gradient mobilities. Both selected input
positions and all geometry restrictions are explicit below.

The coordinator read the complete main construction, deterministic
stability/approximation proof, physical-time complex-source proof, feature
certificate, independent feedback route, independent label-series route,
and all three complete reconstruction reports. The final source edits and
their appended confirmations were read. The underlying manuscript and
book startup sources were already read completely and were hash-verified
unchanged; their current hashes are recorded below. The inverse-coordinate
complex strip from this study's earlier one-input proof was also previously
read completely and is unchanged. No external theorem or unrelated study
was newly imported to fill a proof obligation.

Final scientific sources:

| File | SHA-256 |
|---|---|
| `TWO_INPUT_CANONICAL_COMPRESSION.md` | `f96fe56c50381a6bc3fd9b51d9889edebf83b64e376ce8ab8d48ea11d8845568` |
| `TWO_INPUT_STABLE_GEOMETRY.md` | `708182a1b52269a76ac03ecc08b8436f39fe20c7173272df5d022f9c42b29068` |
| `TWO_INPUT_COMPLEX_SOURCE.md` | `a048017ae0f87d7efb4ce845a89a26e7cd93879e5b441c5107945d561a68f60e` |
| `TWO_INPUT_FEATURE_LEARNING.md` | `75d317cbcfca5cbf3f4a2b4e11a07bd094ab7daff78fcae204b19760db3fb8c7` |
| `COMPLEX_ACTIVITY_ROUTE.md` | `3190cbcef13c3089b2a475c297e9333e98ce3c01f69a686bde217cf87f193fe4` |
| `TWO_INPUT_FEEDBACK_STABILITY.md` | `40cb086eed2d24c06e9bfebb07956e605a0f9c22faf4c0f25cfca053678b4875` |
| `TWO_INPUT_LABEL_SERIES.md` | `8830045f2a1bb5eaa52101eb561d004bc9c84cdacc5961faee8e553badaeed60` |

Final separate reconstruction reports:

| File | SHA-256 |
|---|---|
| `TWO_INPUT_CANONICAL_COMPRESSION_CHECK.md` | `58a72d79f3deec468c8762d8de6e119de47b1966f749e425de0a4e6db8c7e9c7` |
| `TWO_INPUT_COMPLEX_SOURCE_CHECK.md` | `e677e69ba2b1efe0a743cd0fe8ff2b4970baef2a8209c99acb77f00b1a9bcfc0` |
| `TWO_INPUT_FEATURE_LEARNING_CHECK.md` | `b7c8920b6b413cf8000afb6a9301ea57088c0487cac0de3f69e6583b28fb75aa` |

Unchanged scientific context:

| File | SHA-256 |
|---|---|
| `paper/main.tex` | `60c43aa3a5a53a04a94cec27d72858f1a28b35ee6c17c52001c83612a396aa95` |
| `paper/proof_alltime.tex` | `f3f0a0f5d0f553ced7c7334863bc04734033d00ecef48cd2031194dda374035d` |
| `paper/proof_tracking.tex` | `e75f8122ab0ed0bc5f8c0b5f979b7e1a1b779c94440367d62d9a98892d3e53be` |
| `docs/index.qmd` | `f7a21b794e21f145ebad87fb1d7bde05f5f55e5877c92440109c1b22232b06de` |
| `docs/notation.qmd` | `78e11eb3dafc5321a8a3923742993c0bad78df53b0e80b6319f16e48f0131023` |

## 2. Normalization and exact scientific scope

The data are $x_a=\sqrt2e_a\in\mathbb R^2$, $a=1,2$, and
the query set is the whole circle $\sqrt2(\cos\theta,\sin\theta)$.
The loss is $\frac12\sum_a(f_a-y_a)^2$; equivalently the paper's
mean squared loss with $m=2$. With $c_a=y_a-f_a$ and
$\delta_a=w\odot\operatorname{sech}^2z_a$, the mobilities
$(n,1,n)$ give exactly

\[
 \dot A=\sum_a c_a[\operatorname{sech}^2(Ae_a)
                    \odot W^\top\delta_a]e_a^\top,
 \quad \dot W=n^{-1}\sum_a c_a\delta_ah_a^\top,
 \quad \dot w=\sum_a c_ag_a.
\]

There is no missing factor two or changed physical clock. The nonlinear
coordinate $u_a=\Psi(Ae_a)$, $\Psi'(s)=\cosh^2s$, cancels the
first-layer gate in the velocity, giving $\dot u_a=c_aW^\top\delta_a$.
This uses the orthogonality of the two inputs. For arbitrary nonorthogonal
inputs this cancellation is not simultaneous; no extension is inferred.

Labels are fixed independently of width and initialization and have
arbitrary direction in a sufficiently small Euclidean ball. The compressed
initialization depends on that specified label vector. The probabilistic
compression theorem is for each such fixed vector, not one sampler or
one probability event uniformly handling all future label choices.
The feature certificate alone has a stronger label-independent event.

## 3. The feedback estimate closes without commuting sample updates

I reconstructed the exact signed-integral comparison. With two curves
driven by their own residuals, define their state difference $q$ and
$p(t)=\int_0^t(c-\bar c)$. Integration by parts gives

\[
 q=V(x(t))p-\int DV(x)\dot x\,p
       +\int[V(x)-V(\bar x)]\bar c-\int e.
\]

On a tube of total residual length $S$, the difference from $V_0p$
is bounded by $CS(P+D)+\epsilon$, where $P,D$ are the corresponding
supremum norms. The observation decomposes as a fixed initial readout
linear map plus a remainder of Lipschitz constant $CS$. Consequently

\[
 \dot p=-G_0p+\zeta,\qquad
 |\zeta|\le CS(P+D)+C\epsilon.
\]

The initial Gram gap bounds the stable convolution by $1/\gamma$.
Small fixed $S$ absorbs both suprema and yields $D+P\le C\epsilon$,
independently of the interval length. The proof does not require
$\int|c-\bar c|$ to be small, fixed residual signs, or a fixed residual
ratio. Noncommuting sample fields are fully retained. This estimate is
stronger than merely changing the clock of a comparison.

I checked its weighted-network hypotheses directly. The exact adjoint is
$B^*=D_1^{-1}B^\top D_2$, and the matrix norm is
$\|D_2^{1/2}BD_1^{-1/2}\|_F$. Rank-one norms factor in these weights.
The regular coordinates give a bounded derivative of the residual-free
field using only the mixer operator norm and readout maximum, not a
maximum of the backward carrier. No minimum positive mass occurs.

The real residual tangent matrix is the sum of the readout Gram, a Gram
of tensor-product updates, and a nonnegative diagonal first-layer term.
Its initial Gram gap persists for small total activity. Exponential
fitting then bounds that activity by $C\|y\|$, closing the bootstrap
for the full, cavity and reduced models separately.

## 4. Complex response bounds are finite-network estimates

The lower and upper neuron-deleted networks retain normalization $n$ and
use their own residuals. The real comparison controls their difference
from retained full states at ordinary Euclidean scale $C\|y\|$.
Their independence from the omitted initial Gaussian column or row is
therefore exact; the construction never copies the full residual into a
cavity and then claims independence.

Complex time is handled only on short vertical segments anchored at the
real physical solution. Real damping supplies exponentially small residuals
at each anchor; bounded complex growth over the short segment costs a
fixed factor, not $e^{CT}$. The raw full-field factor $\sqrt n$ is
cancelled by the normalized prediction perturbation factor $1/\sqrt n$
in the full/cavity feedback comparison.

Stopped Gaussian references use each cavity's own retained initialization
and stopping domain. Query references additionally condition only on
the retained initial read-in event. The full-network events are intersected
after applying the conditional Gaussian tail. Reinsertion errors have
size $C(Y+YM)$, with carrier cap $M=AY\sqrt{\log(en/\eta)}$;
the feedback ratio $CYM/M=CY$ closes at fixed small label size.

For passive circle queries, the first-layer gates are controlled before
forming their response sources. Gaussian bounds control derivatives of
the upper query preactivation before its tanh is evaluated. Integrating
those derivatives vertically in time and angle gives the upper pole
margin. This avoids assuming the query analyticity being proved.

All source claims concern the actual finite initialized model. Neither a
population law nor clipping appears in the algorithm or the estimate.

## 5. Initial information, small response spaces and cubature

The initial-derivative construction is explicit. A conformal disk map
permits continuation of the initial Taylor germ over a time rectangle.
Its required derivative order can be exponentially large in
$(\log n)^{3/2}$. Finite combinations of those initial derivatives compute
approximate values at interpolation nodes; no trained path is queried.
Time and angle interpolation then retain only

\[
 p=O(\log^{5/2}n),\qquad L=O(\log^{3/2}n),\qquad
 (p+1)(2L+1)=O(\log^4n)
\]

vector coefficients. Applying identical scalar operations to paired
sources preserves their $W_0$ or $W_0^\top$ action exactly. The possibly
enormous temporary derivative list and full-width arrays are discarded.
This is legitimate only for the stated after-setup real-coordinate count;
it supplies no practical setup, bounded setup workspace, or precision theorem.

Positive cubature matches the products of the response-space basis
coordinates and the constant. The selected weights remain positive and
have total mass one, using $O(\log^8 n)$ nodes per layer. The projected
initial mixer preserves both actions on the paired source coefficients
and exactly preserves the initial training-feature Gram.

I checked that no logarithmic factor leaks into the final error constant.
The large $C\sqrt{\log n}$ complex source bound is used only to choose
polynomial degrees. Actual real pairing defects involve bounded forward
features, $O(Y)$ readout/backward responses, and coordinate errors
$\epsilon=C/\sqrt n$. The fixed mixer is controlled in operator norm.
Learned forward and reverse defects integrate against residual activity
$O(Y)$, yielding $C\epsilon$ with a width-independent constant.

## 6. Autonomous comparison, endpoint and feature motion

The selected reference matrix has the exact integrated rank-one form with
the selected positive pairing. Its forward, reverse and output defects
are all $C\epsilon$. The reverse defect also bounds its retained
regular-coordinate displacement by $CY^2+CY\epsilon$; this still lies
in an $O(Y)$ structural tube for $\epsilon\le1$.

The reference velocity defect is bounded by $C\epsilon|c_n(t)|$,
and its observation defect is $C\epsilon$. Thus the real comparison
applies to the compressed network's own residuals at the same physical
time. It gives error $C\epsilon$ through $T=C\log(en/\eta)$.
Each model separately has query tail $CYe^{-\kappa T}$ after that time.
Choosing the fixed multiplier in $T$ large covers every later time and
both fitted limits. No model is artificially stopped or frozen at $T$.

The first-layer feature-motion proof pairs a regular-coordinate Taylor
expansion with a bounded initialized test. The nonlinear remainder is
estimated in normalized $L^1$ using the known $L^2$ increment, not an
unproved fourth moment. Its initialized $2\times2$ moment matrix
converges to a positive scalar multiple of identity.

The second-layer proof keeps the initial readout velocity as a fixed
test but uses current gates. Its derivative is a sum of a squared mixer
update and nonnegative first-layer terms, plus $O(Y^4t^2)$. An initial
bounded moment-matrix gap makes the mixer square at least $cY^4$ on a
fixed short interval, uniformly over label signs. Integration and
Cauchy--Schwarz yield feature-tuple motion at least $cY^2$ in both layers
at a fixed positive time. The source pairing and own-state errors transfer
these bounds to the reduced model for each fixed nonzero $y$ at large width.
The transfer threshold is not uniform over labels shrinking to zero.

For a joint probability statement including compression and feature motion,
allocate half the failure budget to each event and enlarge the width
threshold. Replacing $\eta$ by a fixed fraction affects only fixed
constants in the logarithmic state count. There is no endpoint-feature
displacement lower bound or claim about unspecified test labels.

## 7. Independent attempts, revisions and validation

The initial stability, label-series and geometric attempts began in fresh
contexts with separate artifacts and scoped inputs. Their later exchange
and reconstruction were collaborative. The independent label-series route
establishes a finite-order time-mode reduction and a local complex label
disk but does not close the stronger label-domain bound it sought. It is
not a dependency of the completed physical-time proof. No failed route is
presented as a negative state-compression theorem.

The complete-chain checker reconstructed all three main proof files and
their final revisions. The separate source checker reconstructed the whole
complex proof and the supporting stability/approximation material without
using the other verdict. The feature checker reconstructed both lower
bounds and the weighted transfer. All reports found no blocking gap in
their final stated scope.

Actual corrections were the restriction $0<\epsilon\le M$ in the
general approximation lemma, two missing TeX backslashes, and explicit
good-read-in conditioning for the query references. Reports retain the
original checked hashes and final-version confirmations. The synthesis
claim audit also corrected a statement about scalar clocks: noncommutation
prevents path-independent accumulated-activity coordinates, rather than
preventing scalar reparameterization of a fixed trajectory.

Static validation checked all new two-input source/check Markdown files
for control characters, balanced display/inline TeX delimiters, and broken
relative Markdown links. It found no issue. Hashes were obtained with
`sha256sum`; no executable numerical experiment was run. Mathematical
reproduction consists of the full proofs and their retained reconstructions.

HEAD remains `4dfa5c1ef2c5b920eda2bbc84316b189b97da92e`. The shared
Git index was empty and is untouched. Existing changes to `paper/main.pdf`
and the unrelated structured-study README were preserved. All new research
and notes remain in this designated study; no paper, book, maintained code,
other study source, commit, push or remote was changed.

## 8. Accepted conclusion and limits

**Internally checked positive existence theorem:** for the orthogonal pair
on the circle, either label sign pattern and arbitrary fixed sufficiently
small label magnitudes, the actual realized canonical width-$n$ dense
network has an autonomous weighted representation with
$C\log^{16}(en/\eta)=o(n)$ total retained moving and fixed real coordinates
and all-circle, all-physical-time prediction error $C/\sqrt n$, including
fitting, at confidence $1-\eta$. Both hidden layers retain feature motion
at a scale independent of width for fixed nonzero labels.

The theorem is not conditional on a new unknown response regularity or
stability hypothesis. It does retain the explicit input geometry, tanh,
two hidden layers, small labels, sufficiently large width, and unrestricted
exact-real setup. Nonorthogonal configurations, other depths/activations,
efficient preprocessing, finite precision and unchanged order-$q$ neuron
compression are not resolved. No promotion is implied by the internal checks.
