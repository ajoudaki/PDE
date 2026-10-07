# Internal reconstruction check of the implicit Harmonic setup synthesis

2026-10-06. Verdict: **PASS for the stated conditional exact-real result**.
No scientific correction to the frozen synthesis is required by this check.
The audit-status sentences and pending-status table can now be updated without
changing the scientific statement.

This is an internal integration check, not an independent promotion review.
The checker authored `IMPLICIT_HARMONIC_EXECUTION.md`, read the other two
components only after their freeze, and did not author the synthesis, sampler
or order recipe. The root's earlier audit identified a missing explicit
physical-time-to-affine-coordinate rescaling convention in the execution note;
the checker amended that convention and its cost before this frozen synthesis
was supplied. The checker therefore does not claim independence from that
execution argument or from the shared checked Taylor/backend/assembly inputs.

## 1. Exact versions and read coverage

The full scientific text, including proof and cost sections, was read in each
of the following four files. Tool-output truncation in the first combined
sampler/orders read was repaired by reading the omitted sampler ending and
order-recipe beginning. The subsequent order-recipe change was read directly;
it adds the original bounded-full-strip-first-derivative hypothesis explicitly.

| Frozen input | SHA-256 |
|---|---|
| `IMPLICIT_SETUP_RESULT.md` | `62aa72aa090e86439f075e218765ea2b97c833b6e523dfbb3ebb87653f368839` |
| `IMPLICIT_GAUSSIAN_SAMPLER.md` | `24eb0ab622156cd073bfdf457c3746bc02523bfac551e03f47bb8265206efd57` |
| `IMPLICIT_HARMONIC_EXECUTION.md` | `fe3e6dbcde65c050f63d58a6b8995c423d9fd1e2c87eddac8ad2fb391dc6ccf5` |
| `IMPLICIT_SETUP_ORDERS.md` | `3f5ff8a63c97ea76dda4890b0f464f05e8bb8576760cde93ff1f4c18d00a6009` |

The following already checked inputs were also read completely in the present
scoped task: `docs/notation.qmd`, `LOCAL_CONTINUATION_ASSEMBLY.md`,
`LOCAL_TAYLOR_ASSEMBLY_BRIDGE.md`, `LOCAL_CONTINUATION_SETUP.md`,
`LOCAL_ACTIVATION_BACKEND.md`, and `POLYNOMIAL_SETUP_QUADRATURE_ROUTE.md`.
Their hashes are recorded in the frozen execution note and were verified there.

For `RESULT.md`, SHA-256
`c2cbd1bb0e6a39de87181df89be977eaf2e272fda4f1459ac934396d84e1b278`,
the read scope was its complete source-family/exact-initialization,
supplied-budget, inventory/gate, coordinate-selection/metric,
factored-jet, geometric-basis, selection/assembly-cost, and relevant scalar
recurrence sections. For this integration check, the complete section
“Why the comparison exponent has numerical coefficients,” lines 5896–6114,
was additionally read to verify the synthesis's explicit error bound. The
source probability theorem and the rest of the integrated book-length proof
were inherited, not re-audited in full.

No other study, archived book, Git history, external research source, empirical
result, or unfrozen candidate was used. No numerical experiment or statistical
test was run. Actual read/check commands included `cat`, scoped `sed -n`,
`rg -n`, and `sha256sum` on the listed files. The displayed hashes were checked
against their contents before this report.

The required canonical-notation skill remained inaccessible, including an
escalated read. The root authorized the disclosed fallback to the explicit
user/repository requirements, maintained notation contract and accessible
rigorous-math skill. The conjecture skill's adversarial-audit reference was
also read for the scope and hidden-information checks.

## 2. Joint-law and final-output reconstruction

The sampler proof supplies a simultaneous, globally adaptive transcript law
for all hidden layers. Its conditional mean and remaining Gaussian component
are derived after conditioning on the full past; random query directions are
not incorrectly treated as unconditionally fixed. Both forward and transpose
updates preserve the compatibility relation between previously observed
actions. Their unused Gaussian components are independent of the newly exposed
reply by the explicit covariance/characteristic-function calculation. Singular,
zero and repeated directions are covered.

The interleaved-layer argument updates only the selected conditional matrix
factor. At bounded stopping, its final completion has the ordinary joint iid
entry law and agrees with every actual returned action. Completion is a
probability-space construction only, not an algorithmic generation of an
uncharged dense array. The completed matrices remain independent of the
querying algorithm's external randomness, which includes the explicit first
matrix's independent initialization.

The execution's realized rank is random. The synthesis correctly invokes the
sampler theorem at the deterministic per-mixer cap

\[
m+2J(m+N_x)(K+1)+2N+\min(n,R),
\]

then uses the pathwise actual-rank bound for operation counts. Thus the finite
budget hypothesis of the sampler theorem is satisfied before the computation,
without presuming a particular rank realization or conditioning on the good
source event.

For each panel, the grouped endpoint update has at most \(mK\) columns in
each factor. Current anchors therefore have the exact representation

\[
W_b^{(j)}=W_0^{(j)}+A_b^{(j)}B_b^{(j)T},\qquad
\operatorname{rank}(W_b^{(j)}-W_0^{(j)})\le bmK.
\]

This is a finite Taylor identity, not an assumption about the true continuous
flow's rank. The same finite coefficient contractions and polynomial
composition recurrences recover the explicit local jets. The frozen execution
now explicitly rescales raw coefficients by \(\Delta_b^c\) before applying
the affine-coordinate moment table. This closes the identified convention
issue; its extra arithmetic is absorbed by the charged source projection.

The matrix-access inventory includes exact original-activation initialization,
all local forward/transposed training and passive actions, initialized images
of global coefficients, and initialized images of complete final basis columns.
The last set is necessary and is not assumed available for free from paired
source coefficients. Given identical exact scalar conventions, the generators,
rank decisions, selector comparisons, tie-breaking, metrics and final mixer
arrays all agree under one completion coupling. The result therefore controls
the selected output jointly with the dense reference, not just separate
marginals of individual queried products.

No sampled operator-norm event is tested. Scalar width/order gates use supplied
certificates and explicit recurrences. The source event transfers by the joint
law and requires no rejection sampler or additional probability allowance.

## 3. Explicit error bound and original scope

The general inherited comparison is

\[
\|f_H-f_n\|_*
\le\mathcal A_n\eta+\mathcal D e^{-\gamma T/(4m)}.
\]

The full-interval numerical bounds in `RESULT.md` are

\[
\mathcal A_n\le
2000e^{44}\beta^{42L}\frac{Ym}{\gamma}
\left(1+\sqrt{\frac m\gamma}\right)
(1+\sqrt{\log(en)})e^{64\sqrt{\log(en)}},
\]
\[
\mathcal D\le236\beta^{9L}\frac{Ym}{\gamma}
\left(1+\sqrt{\frac m\gamma}\right).
\]

Substituting \(\eta=1/n\) and
\(T=32(m/\gamma)\log(en)\) gives

\[
e^{-\gamma T/(4m)}=e^{-8\log(en)}=(en)^{-8},
\]

and hence exactly equation (2) of the synthesis. Its numerical constants and
powers are copied correctly. It uses the full source/runtime label allowances;
the optional smaller beta-power label cap is not needed. At the original
horizon the sharper coefficient with 32 instead of 64 is available, but the
larger displayed bound is valid.

The order recipe preserves the full original interval, the source event,
the analytic gates and the partly existential width condition. It explicitly
retains unbounded activation values with bounded full-strip first derivative,
and the necessary safe-half-strip derivative bounds. Population moments and
the positive data gap are supplied analytic certificates; their computation
from an arbitrary function description is not charged as free arithmetic.

The whole sphere, the full nonnegative physical-time interval and the fitted
limit are inherited through the exact finite construction and comparison
theorem. A finite collection of setup nodes has not been substituted for that
observable. The numerical setup's polynomial activations are discarded; the
retained model uses the original activations and prescribed optimizer.

## 4. Work, peak memory and primitive-call audit

The synthesis's equations (4)–(8) match the frozen execution's query count,
full operation envelope, matched peak envelope, primitive inventories and
retained-storage bound. The copied geometry formulas use the same decision to
recompute spatial coordinates and harmonic values on every panel.

In particular, the count includes:

- The explicit \(n\)-by-\(d\) first matrix, training input Gram, passive
  input dot products, exact original initialized features and optional initial
  top-feature Gram/solve cache.
- The complete Gaussian transcript, current-panel contraction caches,
  degree-\(D\) online activation composition arrays, and accumulated
  \(JmK\)-column hidden increment factors.
- The \(J(J-1)\) accumulated-history action cost, not just the cost of
  appending new factors.
- Scalar temporal tables, the raw-to-affine coefficient rescaling, current
  spherical projection buffers, completed global coefficients, and exact
  initialized-image actions.
- Rank-aware source orthogonalization, the conservative \(Lnr^3\)
  barrier selector, final basis-image requests and \(nr^2\) contractions,
  source metrics/inverses, first-weight restriction, and final matrices/caches.
- Positive quadrature weight construction, node generation, separated harmonic
  normalizations and recurrences, original scalar activation calls, standard
  Gaussian draws, elementary function calls and scalar routine scratch.

The sampler stores only its query bases and images. No \(n\)-by-\(n\)
projector or conditional-mean matrix is formed. The low-rank history is kept
as factors and acted on by contractions. The final basis compression uses
sampler responses rather than accessing initialized entries. The source-event
certificate invokes theoretical caps rather than computing dense operator
norms. These observations eliminate the old mandatory \(n^2\) operation
and storage charges under this fresh-reference input contract.

This does not claim that the finite bounds are subquadratic for every possible
order: a large query count, large actual rank, or full-width output can make
them quadratic or larger. The synthesis states that limitation explicitly.

## 5. Reconstruction of the logarithmic specialization

At fixed admissible structural parameters, the checked backend gives
\(\widehat R_n^{-1}=O(\sqrt{\log(en)})\), so its explicit panel choice
has \(J=O(\log(en)^{3/2})\). The defect and source-accuracy budgets have
logarithms \(O(\log(en))\); therefore \(K=O(\log(en))\).
The activation approximation interval has size \(O(\sqrt{\log(en)})\),
and the inverse ellipse-width gap has the same order, giving
\(D=O(\log(en)^{3/2})\).

The source radii, weighted simplex and positive quadrature give
\(p+1,N_t=O(\log(en)^{5/2})\), and, for \(d\ge2\),
\(\ell_*,N_\theta,N_\varphi=O(\log(en)^{3/2})\).
The degree multiplicities yield
\(H_{\rm sph}=O(\log(en)^{3(d-1)/2})\); the angular tensor product
has the same bound. Consequently

\[
N,R,r,q,k_*=O(\log(en)^{3d/2+1}).
\]

The two-point convention gives the same result when \(d=1\).

The Gaussian action term is at most
\(O(n\log(en)^{3d+2})\). Accumulated-history actions and polynomial
activation arithmetic are at most
\(O(n\log(en)^{3d/2+7/2})\). Spatial-first projection is bounded by
the powers \(3d-1/2\) and \(3d/2+7/2\). The selector is
\(O(n\log(en)^{9d/2+3})\), which dominates all those width factors
for every fixed integer \(d\ge1\). The remaining scalar/final-small-matrix
terms are fixed powers of the logarithm and are eventually smaller than this
width-proportional bound. This verifies the stated work exponent.

For peak memory, transcript and source coefficients have exponent
\(3d/2+1\), while history and online activation arrays have exponent
\(5/2\). The latter is no larger because \(d\ge1\). The current spherical
projection buffer is also smaller. All remaining terms are \(O(n)\) or
fixed powers of \(\log(en)\). This verifies the peak-memory exponent
\(3d/2+1\). The final retained inventory has exponent \(3d+2\) and
contains neither the query transcript nor the temporary learned history.
The concrete \(d=2\) powers 12, 4 and 8 are correct.

The fixed-parameter specialization does not apply to arbitrary horizons or
accuracies outside that regime, or to growing dimension, depth or sample
count. Those cases retain the unsimplified finite formulas. Additional costs
of actual scalar value/sampling implementations remain explicitly separate.

## 6. Conclusion and inherited limitations

The frozen synthesis correctly composes the three components and inherits
the original accuracy, label, activation, retained-storage and confidence
qualifications. No additional scientific gap was found in this integration.
This verdict is conditional on the inherited source/comparison and previously
checked local Taylor/backend/assembly theorems; it is not their new independent
full review.

Finite precision, stable approximate rank decisions, Gaussian-conditioner
roundoff, bit complexity, an effective general confidence-to-width threshold,
and practical constants remain outside the result. Fresh implicit sampling is
not a conversion of a previously stored dense realization or a prescribed
entrywise pseudorandom seed. The near-linear upper bound is not strict linear
work or an optimality claim, and it does not prove a speedup over every implicit
dense training solver. All of these limits are accurately stated in the
synthesis.
