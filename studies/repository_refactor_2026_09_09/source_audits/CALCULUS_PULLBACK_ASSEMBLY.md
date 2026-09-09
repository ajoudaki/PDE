# Calculus pullback source assessment and correction record

This is a source assessment and implementation draft, not an acceptance
review. The full substantive reads are listed below. SHA-256 values identify
the source bytes read; no historical experiment or training was rerun.

| Source | Fully read lines | SHA-256 |
|---|---:|---|
| `docs/NOTATION.md` | 1–98 | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |
| `code/README.md` | 1–271 | `b563a8a4fcebbb5fb634057f6cf09d32475462670002c8fbad0502f5c06482e0` |
| `studies/mfp_loss_gradient_time_doubling/LOSS_GRADIENT_EXPANSION.md` | 1–333 | `365dbc79a28d86db9474a12b3d65252c9641be05ed8781454ba2efa6be07702d` |
| `studies/mfp_loss_time_doubling/LOSS_TIMECHANGE_ANALYSIS.md` | 1–373 | `d88c9022a8afb31db27254f78c40238087ceea41d9ea34c8ce6c53ff380db1d7` |
| `studies/mfp_loss_gradient_flow_audit/LOSS_ORDER5_AND_MESH_STATUS.md` | 1–313 | `6916cc481a42390387d59b518e62646af1ab34231186746f2cc62c581931a67e` |
| `studies/mfp_loss_gradient_flow_audit/LOSS_ORDER5_INDEPENDENT_AUDIT.md` | 1–90 | `a4451d237391ddb6d89ebe7e5b7bec1cad423615c17c300e8ed9ac2e4d4636e3` |
| `studies/mfp_loss_gradient_flow_audit/LOSS_PAIRED_DISCREPANCY_AUDIT.md` | 1–330 | `978a72fbdf72c4d2972ea5ddba90931f03a4a336c07611a56138c0fb465ba326` |
| `studies/mfp_loss_gradient_flow_audit/EVIDENCE_LEDGER.md` | 1–76 | `17b7c2bdc7854c69a4b98f3a412e9420d6ba337b060d53ae3dd8010a6f9fca59` |
| `studies/mfp_loss_gradient_flow_audit/QUADRATIC_RELU_CT_HOSTILE_AUDIT.md` | 1–300 | `ba0db8ea53309a8f7d294bbcc6ccabce304b4fdde886ddac324175dda4a956ce` |
| `studies/mfp_loss_time_doubling/RELU_COMPACT_TIME_AUDIT.md` | 1–473 | `d4c44f13dc0b4b0e4cf03723a3e5b994bf7c7438b9f18ebdcf443847866f4282` |
| `studies/mfp_loss_time_doubling/RELU_JOINT_WIDTH_MESH_AUDIT.md` | 1–455 | `e6c3e6e5b89fe6241fb1fab686b0a82408ad49750badf40cdd20100ab3502ea4` |
| `studies/mfp_loss_time_doubling/RELU_NO_CONTINUOUS_LIMIT_TEST.md` | 1–336 | `15c1c094ec7e3ddfc8c46714be63ccebd47aeed946122a4a2ce11f46141ad70c` |
| `studies/mfp_loss_mesh_resolution/FINAL_X2_RELU_MESH_VERDICT.md` | 1–371 | `a32d762ae6f80597f065a25547e73387bc13d201c9285e263068c5c86342022f` |
| `studies/mfp_loss_mesh_resolution/FULL_RESOLUTION_AND_JOINT_SCALING.md` | 1–408 | `4de44bde79bb339e794b99bad1ccf22f4cc8f8a8b87104605b631e874fb351e7` |
| `studies/mfp_loss_mesh_resolution/INDEPENDENT_AUDIT.md` | 1–120 | `b49c13e4b97e2ec45534ba84aa82f6ed68a1361490a11a31864b7ad625381c5a` |
| `studies/mfp_loss_mesh_resolution/EVIDENCE_LEDGER.md` | 1–91 | `a24166edca7882885b0e51d507e2da402f17ad2ed9dc35791e048b90edd0e83c` |
| `studies/rcgc_compiler/rcgc_compiler.py` | 1–217 | `a8eb1fa1776cfd924719222d7204784b614f4eb5e1cabc40f5ecd6ed1878acce` |
| `studies/rcgc_compiler/test_rcgc_compiler.py` | 1–60 | `0fe24cfbb2e4a7f535f3b31b45819e3b57b0f25101fe2679c480d51a27ae7fab` |
| `studies/rcgc_compiler/README.md` | 1–22 | `43295ecde3800f6fb2f4da56eb98aac7d43be829c52954e4f14bdee811836994` |
| `studies/rcgc_compiler/VALIDATION_REPORT.md` | 1–28 | `9bb52837516bcb28140841b2c104712391b8f33fd0b20994a516d71b8921b6e9` |

Additional scope comparisons read Gaussian chapter headings and lines
2434–2520, the advisory calculus discussion at lines 107–115, and the
response-compiler discussion at lines 245–249. These are bounded comparison
reads, not full reviews of those larger documents. The notation/code-guide
hashes are a read snapshot and may change during integration by another
agent. The exact-calculus implementation and its entire preexisting tests
were read before modification.

The correction ledger is:

| Claim | Present disposition | Dependency/supersession |
|---|---|---|
| Finite pullback word identity and rational temporal table | Exact under the explicit finite smoothness assumptions; fully rederived above | No neural or probabilistic dependency |
| Higher pullback coefficients are actual width-first neural coefficients | Excluded from this package | Requires the fixed loss-program DAG, flat metric/adjoint realization, population differentiability and terminal uniform integrability; the source audit makes these conditional |
| A continuous residual clock is an exact constant-step feature-GD substitution | Invalid | Raw GD recomputes its residual; (P3) retains it in the vector field |
| A finite order-five expansion decides mesh removal | Invalid implication | The fixed-order algebra survives, but the uncontrolled remainder and growing histories remain independent obligations |
| All nonlinear loss-mesh problems remain open | Superseded as a blanket historical summary | Later records distinguish a normalized-quadratic initial-layer obstruction, ReLU local scalar compactness, and open generalized-state identification; none is promoted here |
| Hard ReLU has the smooth cubic/order-five formula | Excluded | Missing boundary/indicator identification and smoothness; changing from half-loss to full loss does not repair it |
| Classical ReLU noncontinuation rules out every continuous Euler limit | Invalid implication | The later frozen occupation and local tightness records correct it; scalar tightness still does not imply unique generalized dynamics |
| The nested response/curvature compiler proves convergence or nonclosure | Excluded | The code emits syntax only; matrix-color labels identify a possible analytic obligation, not a theorem |

For the last item, the 217-line compiler's reusable candidate is the finite
recursion \(R_\ell=E_\ell+D_\ell G_{\ell+1}^T R_{\ell+1}
G_{\ell+1}D_\ell\). Its code does not define the derivatives represented
by \(E_\ell\), the held-fixed variables for \(R_\ell\), or a numerical
evaluation contract; its historical tests check emitted strings. A separate
typed finite Hessian-chain-rule specification would be needed before
promotion. It has lower immediate value than the complete pullback package
and is not implemented here.

The strongest surviving objection to a larger theorem is the absence of a
common reachable state and uniform source/response estimates. The cheapest
resolver for this bounded package is instead independent proof/code review
of (P1)–(P25), the two rational APIs and their exact tests. Opposite evidence
would change this finite algebra claim only; no claim about global nonlinear
closure, neural convergence, or nonsmooth model selection is being made.

## Isolated review correction

The first complete paired review required one domain repair: smoothness of
the squared loss does not guarantee a C3 predictor at zero residual. For
example f(w,a)=a|w|^3 is C2 while its squared loss a²w⁶ is smooth. Equations
(9.P18)–(9.P21) now explicitly assume a C3 predictor near the supplied state,
separately from the C6/C7 loss-field conditions for the Taylor remainder.
The generic pullback identities, coefficients and APIs are unchanged.
The first CLEAN and CORRECTIONS REQUIRED reports are both retained without
relabeling. A fresh complete pair receives the corrected version.
