# Direct compact construction without a realized dense network

Started 2026-10-05 at the user's request. This is a new lead-author study.
It investigates whether the prediction path typically learned by the canonical
two-hidden-layer tanh network can be reproduced by a directly initialized,
autonomous compact model without ever constructing, training, querying, or
encoding a realized width-\(n\) network.

## Research contract

The reference has two width-\(n\) tanh hidden layers,
\[
h(x)=\tanh(Ax/\sqrt d),\qquad g(x)=\tanh(Wh(x)),\qquad
f_n(x)=w^\top g(x)/n,
\]
with independent \(A_{ij}\sim N(0,1)\),
\(W_{ij}\sim N(0,1/n)\), zero readout, mean-square gradient flow, and
block mobilities \((n,1,n)\). Start with fixed orthogonal inputs of norm
\(\sqrt d\) and sufficiently small fixed signed labels. Preserve nonlinear
hidden-feature learning; broaden the data class only after proving the bridge.
Write \(Y=\|y\|_2/\sqrt m\) for the label RMS.

The proposed compact model may use only the dataset, the architecture and
initialization law, the requested reference width or accuracy, and its own
randomness. It must have explicit computable initialization, autonomous and
restartable evolution, and a transparent cost and retained-state inventory.
It may not use realized width-\(n\) weights, features, derivatives, selected
coordinates, trajectory values, endpoints, population-response oracles,
time-indexed playback, or arbitrary-precision encodings of such information.

The primary target is, for an independent fresh dense run,
\[
\Pr\!\left\{
\sup_{t\in[0,\infty]}\sup_{\|x\|=\sqrt d}|f_C(t,x)-f_n(t,x)|
\le C_{\mathrm{data},\delta}/\sqrt n\right\}\ge1-\delta,
\]
with the coefficient independent of width and time and with polylogarithmic
retained storage in \(n\). Same physical time and the fitted endpoint are part
of the contract. A finite-time, endpoint-only, weaker-rate, or conditional
result is a separate claim, not a substitute.

The limit order is fixed data, fixed depth, and width tending to infinity.
The approximation must control the feedback of omitted information into future
feature learning. Agreement between two dense runs is not by itself a bias
bound relative to a deterministic trajectory.

## Authorized scientific inputs

The user explicitly authorized these external study files:

- `closure_sampling_20261003/STORAGE_QUADRATIC_IMPROVEMENT.md`
- `closure_sampling_20261003/SPHERICAL_SOURCE_DIMENSION_ROUTE.md`
- `closure_sampling_20261003/ERROR_PREFACTOR_GEOMETRIC_ROUTE.md`
- `integrated_general_compression_20261004/README.md`
- `orthogonal_tanh_time_legendre_20261005/README.md`

Their mathematical claims are usable only after reading their complete proofs,
relevant corrections, and check status. Directly linked proof/check artifacts
needed to determine the status of these named notes are within the user's
instruction to read the actual proofs and corrections; no unrelated study
history is an input. The maintained `docs/` edition and required shared
instructions are also available.

## Claim ladder and route registry

The final status of the primary theorem is **open**. Distinguish:

1. an exactly computable direct initialization and autonomous finite state;
2. well-posed nonlinear feature-learning dynamics of that state;
3. finite-time approximation to a deterministic population trajectory;
4. identification and quantitative bias of a fresh finite dense run;
5. stability on the width-dependent fitting horizon;
6. all-time comparison and fitted endpoint control;
7. moving-state, fixed-storage, initialization-work, and bit-cost bounds.

Independent first-round routes are:

| Route | Mechanism | Initial deliverable | Status |
|---|---|---|---|
| Population quadrature | Law-built finite nonlinear Galerkin/particle hierarchy | All-time qualitative convergence and fixed-error dense comparison | **Proved after clock repair; independently checked** |
| Symmetry reduction | Orthogonal tanh kernel and label perturbation | Direct \(m\)-state model with all-time population error \(CY^3\) | **Proved; independently audited** |
| Prediction-first | Exact tangent hierarchy and direct source candidate | Conditional construction and iid-sketch boundary | **Frozen; target bridges open** |
| Finite-width rate | Residual-damped kernel comparison | Strict-root onset fluctuation, \(O(n^{-1})\) onset bias, dynamic reduction | **Proved; internal check recorded separately** |
| Effective order | Population source, cubature, and precision audit | Generic storage and exact missing certificate | **Frozen; polylog root target open** |
| Adversarial audit | Bias, restartability, endpoint, and no-go boundaries | Independent reconstruction of the symmetry result | **Complete** |

Routes remain independent until their first concrete candidates are frozen.
No experiment is authorized in this initial theory round; deterministic algebraic
checks are allowed. Failure of one witness is not an impossibility theorem for
all direct prediction-based representations.

## Process and repository safety

Startup HEAD is `907f4598d836d5efcc2c1e656d1aa43d8fb072ef`; the shared
index is empty. Existing dirty integrated-compression, compact-refinement,
orthogonal-tanh, and unrelated Quarto files are preserved. This study owns only
its flat folder and any future generated products under
`data/generated/direct_compact_construction_20261005/`. No Git-index mutation,
commit, book edit, code edit, or promotion is authorized.

The conjecture-investigation and rigorous-math skills are in force. The required
`explain-with-canonical-notation` skill is filesystem-permission inaccessible;
the user's explicit minimal-symbol requirement and `docs/notation.qmd` are the
fallback. The coordinator owns this README and synthesis. Scoped route authors
must record complete input scope and write only their assigned files.

## Artifacts

- `RESULT.md`: integrated statement, equations, costs, and claim boundary.
- `POPULATION_ROUTE.md`: direct nonlinear construction and qualitative proof.
- `POPULATION_CHECK.md`: independent reconstruction and the required
  orthogonal-tanh clock correction.
- `SYMMETRY_ROUTE.md`: explicit \(m\)-state frozen-feature theorem.
- `ADVERSARIAL_AUDIT.md`: independent check and finite frozen-flow reduction.
- `FINITE_WIDTH_RATE.md`: strict-root onset theorem and exact all-time dynamic
  reduction.
- `FINITE_WIDTH_CHECK.md`: independent check of the finite-width theorem.
- `EFFECTIVE_DIRECT_ORDER.md`: effective-order, cubature, bit-cost, and
  complex-pole audit.
- `PREDICTION_ROUTE.md`: exact prediction hierarchy and conditional
  prediction-first construction.

## Current outcome

The central strict-root, fixed-label, polylogarithmic-storage theorem remains
open. The strongest unconditional direct nonlinear result is an explicit
law-only autonomous hierarchy with trainable hidden blocks. It converges to
the nonlinear population feature-learning flow on the entire time interval,
whole sphere, and endpoint, and it is within every
fixed tolerance of a fresh dense run for all sufficiently large widths. Its
order selector and cost as a function of tolerance are non-effective.

The explicit \(m\)-state frozen-feature predictor \(\bar f\) obeys

\[
 \Pr\!\left\{\|\bar f-f_n\|_*
 \le C_{\mathrm{data},\delta}
       \left(\frac{Y}{\sqrt n}+Y^3\right)\right\}\ge1-\delta .
\]

Here \(\|\cdot\|_*\) is the supremum over the entire training interval,
including the fitted endpoint, and over the whole input sphere.
It is a complete direct-to-dense theorem but freezes hidden features; for
fixed labels its certified bound retains the nondecaying \(Y^3\) term. The
onset finite-width fluctuation and bias are respectively \(O(n^{-1/2})\) and
\(O(n^{-1})\).
The unresolved dense-to-population step is dynamic, and the unresolved direct
construction step is an effective growing-order source/cubature certificate.

At dictionary rank \(q\) and at most \(p\) quadrature nodes per population,
the proved finite nonlinear model stores
\(O(p(q+d)+q^2+m(d+1))\) real scalars. No proved bound yet selects \(q\) or
\(p\) from \(n\). Conditional on an effective rank-\(q\) source certificate,
generic positive moment cubature gives \(p=O(q^2)\). Matching the existing
realization-dependent \(O([\log(en)]^{3d+2})\) storage needs both an effective
\(q=O([\log(en)]^{3d/2+1})\) population source theorem and a law-built
source-compatible \(p=O(q)\) sparsification; neither is currently proved.
