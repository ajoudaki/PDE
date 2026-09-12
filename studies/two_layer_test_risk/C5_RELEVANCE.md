# C.5 relevance and placement assessment

Decision: **accept for narrow assembly as C.5**.

Selected title:

> C.5. Early test-risk advantage over frozen features at matched training loss

Selector: `/root/risk_promotion_placement`, independent of the result's
authorship and the updated C.5 assembly. Assessment recorded on
2026-09-12; the current coverage hashes below were obtained at
2026-09-12 14:35:36 UTC. This is the relevance and placement gate in
RESEARCH_WORKFLOW.md Part 2, step 1. It is not a scientific proof review,
an integration review, or evidence that those later gates have passed.
The selector must not serve as either of those reviewers.

## Inputs and assessment scope

The assessed scientific source is the study's signed candidate
`PROMOTION_SIGN_C4_V2.md`, SHA256
`dcb03d4c95a34c2ea3f616cc98ad30ea212abdc8e9dfe64624a666f4eee90bbc`.
Its complete model/theorem statement, comparator definition, finite-clock
scope and evaluated certificate conclusion were read. The source still
uses C.4 numbering; this assessment recommends an editorial relocation,
not a change to its scientific claim.

Current book coverage was assessed from the notation contract, the reading
guide's relevant scientific scope and roadmap, the global-nonlinear chapter's
structure and complete relevant statements/scope paragraphs in C.1, C.3,
C.4, C.4.5 and C.4.10, and targeted searches across the established chapters.
Those searches included matched/equal training loss, frozen/tangent risk
comparisons, the cubic risk difference and the displayed rational endpoint.
The complete code guide was read, together with the proposed certificate
tool guide and code-guide appendix. Candidate and code-reference searches
checked the old section labels relevant to relocation.

This coverage establishes relevance and placement; it does not assert a
fresh audit of the complete book, the candidate's proof bodies or the
executing arithmetic. No new coefficient calculation or training experiment
was performed. The study's proposal was used to identify proposed sources
and destinations; its reports of earlier passing reviews do not determine
this selection decision. No other study's research, chat or Git history
was read. The only output of this assignment is this report; no Git action
or established-file edit was made by the selector.

## Distinct value and duplication

The distinctive conclusion is a positive comparison of unseen-input risk
**at the same training loss**. C.3 supplies nonzero hidden activity and a
changing kernel, but those properties alone do not show a favorable
test-risk difference. C.4.1--C.4.4 supply local law stability, a precisely
ordered expected train--test-gap bound, approximation and an open active
family. C.4.5 supplies fixed-time risk reduction near a fitted reference.
C.4.10 supplies finite-episode learning for a declared regression family,
with approximation and sampling controls. These results do not already
prove the candidate's matched-loss comparison with frozen initial hidden
features. The current chapter explicitly distinguishes its risk results
from superiority over another training method.

The candidate removes the training-progress ambiguity by constructing a
unique loss-matching clock. It proves an actual population-flow expansion
with a controlled fourth-order remainder, and its finite arithmetic
certificate decides the sign of the remaining cubic coefficient. This is
a useful connection between learned hidden motion and a concrete unseen-risk
comparison, despite its narrow design and small local effect. The finite
GF/raw-GD capture makes the comparison relevant to the stated network regime.
No duplicate matched-loss sign theorem was identified in current coverage.

The result does not resolve the roadmap's class-level unknown-structure
discovery or depth-comparison milestones. Its selection does not justify
marking roadmap E or F complete, nor replacing the current C.4 account of
generalization with an earlier description of the book.

## Assumptions and useful limits

Retain the complete fixed-model opening: exactly two bias-free tanh hidden
layers, input dimension two, independent stored Gaussian variances
`(1,1/n,1/n^2)`, raw mobilities `(n,1,n)`, and full mean squared training
loss. Training uses the three angles `0,pi/5,-pi/5` with labels from
`cos(3 alpha)`; test risk is the squared error against that teacher under
uniform circle measure. The input Gram is correlated and rank two; no
whitening or Gram inversion is imposed on it.

The comparison model freezes both initial hidden layers and trains its
readout, retaining the same finite initial random readout. Its population
kernel equals the full initial population tangent kernel because the
limiting readout is zero. At finite width the hidden-parameter tangent
blocks need not vanish: the proved finite comparator contains only the
readout block, not the full finite initial tangent kernel. The selected
"frozen features" title states the proved comparator directly and avoids
that ambiguity. The population tangent interpretation remains useful in
the opening explanation, with its qualification explicit.

The signed conclusion is
`R(g_tau(t))-R(f_t) >= (27/200000)*t^3 > 0` on a width-independent positive
early interval. The exact coefficient bounds are
`27/100000 < chi < 273/1000000`; the initial risk is `1/2`, and the leading
effect is approximately `0.000272*t^3`. The time endpoint and finite
remainder constant are not numerically evaluated. Their existence is a
conclusion of the proposed flow proof, not an assumption requiring an
unknown trajectory oracle. They supply no practical effect-size guarantee.

Finite GF and raw GD with any deterministic vanishing step inherit the
positive sign in probability on every fixed `[delta,t0]`, with `delta>0`.
There is no finite-width sign uniform down to zero, quantitative width
rate, arbitrary shrinking `delta_n`, later-time dominance, iid-average
risk guarantee, sample-complexity theorem, growing-design result,
activation comparison or depth advantage.

## Smallest suitable destinations and maintenance cost

Append the complete theorem and certificate proof to
`docs/global_nonlinear.md` as C.5, after the existing C.4 branch. C.5 is the
unoccupied sibling slot in the current chapter; C.4 already contains the
training-law/generalization sequence. The candidate depends on C.1--C.3
and their stated foundations rather than on the C.4 branch. No existing
section needs renumbering. Change only the candidate's own C.4/C4 section
and equation references to the chosen C.5/C5 convention, plus corresponding
new tool references. Preserve existing C.4 references in the established
material.

Patch the **current** `docs/README.md` in place. The old proposed replacement
`PROMOTION_SIGN_DOCS_README.md` is 271 lines, whereas the assessed current
guide is 580 lines and includes substantial later C.4 and roadmap material.
Replacing it wholesale would lose established coverage. The needed changes
are a narrow addition to the opening scientific scope and global-nonlinear
chapter entry, a C.5 comparison sentence alongside the existing limitations,
and reconciliation of the computer-assisted-proof and final numerical
dependency statements. In particular the current blanket language about
code execution and generated coefficient tables must distinguish this
computer-assisted sign proof. Preserve the current roadmap and the precise
scopes of all existing C.4 results.

The following six-file optional tool is relevant because it regenerates
the finite sign certificate, including the loss-clock subtraction and all
declared approximation errors:

| New destination under `code/tools/two_layer_risk/` | Role |
|---|---|
| `certificate.py` | Compact `certify(output, target=26)` entry point and CLI for the fixed mathematical certificate |
| `certificate_kernel.cpp` | Executing finite-sum arithmetic kernel |
| `angle_error_bound.py` | Exact rational verification of the circle-rule error majorant |
| `check_driver.py` | Focused exact and independent supplied-contraction checks |
| `check_kernel.py` | Elementary-function and independent finite-tensor checks |
| `README.md` | Fixed model, supported platform, numerical contracts, fresh-output recipes and limits |

Append a short reference and reproduction section to the current
`code/README.md`. No change to the public `pde` API is needed. Keep the
certificate opt-in: ordinary library imports must not acquire a compiler
requirement. The stated Linux/C++17/IEEE arithmetic contract, Python/NumPy
requirements, exact rational decisions, resource limits and unsupported
platform failures are a real but bounded maintenance cost, justified by
the proof's finite-arithmetic dependence. This is not a general training
solver, parameter-search driver or general-purpose quadrature API.

The two proposed guide references to global-nonlinear C.4 and the grid-rule
docstring in `PROMOTION_certificate.py` must follow the C.5 relocation.
No numerical algorithm change is needed for placement. Later independent
reviews must verify standalone source completeness and the executing
arithmetic rather than rely on this relevance assessment.

## Current coverage hashes

These identify the established snapshot used for comparison. Hashing a
chapter listed below does not claim its complete proof body was rereviewed;
the reading and search scope is specified above.

| Established path | SHA256 |
|---|---|
| `docs/NOTATION.md` | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |
| `docs/README.md` | `d149815d53784b9093bf22608456a19eabfa91a2cca8c6f0d60df9a187ed313c` |
| `docs/arctan_limits.md` | `19f01b6112949f4d186ef17ff94415804830ed51a519b155ed45343c26cbbead` |
| `docs/continuous_depth.md` | `12be7aafbf37cb3651facdcac9c5333281b793c96b96a8a52a1232cd86ca006d` |
| `docs/finite_dynamics.md` | `a57d832a0ce0ad2bf40fa1ec574af787d05bade3264b619a8faca5545bc0012a` |
| `docs/finite_optimization_and_controls.md` | `80dcce91ed3cd8313654523725e28b312ab925376cd7a28d71323bed648a5628` |
| `docs/gaussian_calculus.md` | `d2f6a065432b5dadc7a1973f11b335cbd0f180caa29a81f863c58fff3ac5ef5e` |
| `docs/global_nonlinear.md` | `5c7f4cd85eebe73f497ff91cca4f3c525f158727c28b8a187a09add94e756483` |
| `docs/linear_dynamics.md` | `8de3beaca0cd6f970c27a25eb8c2bc4a1fefa2e7840bd97e7bccfc4f41281c1d` |
| `docs/special_data_limits.md` | `5b7b48aa5deab320042217a6f284002366a683bf0f7f0b63c05d8167c526a489` |
| `code/README.md` | `00f5070d35a3e9fb9d0e9886f0f6d9f680a8d34bb32307807d1f88afc807a774` |

The proposed six-file tool sources at selection time are identified below.
Editorial C.5 updates may change source/guide hashes; the frozen review
packet must record those new exact bytes.

| Study source | SHA256 |
|---|---|
| `PROMOTION_certificate.py` | `36dd0b21dea51647dcbb9aef7c958d8f2ddadc397529e629ada5b122af0d2810` |
| `certificate_kernel.cpp` | `9d7bbcd743e465ae0e4caacd0f1e670d78283e1388a2fe48bda6193ef0e66ad9` |
| `angle_error_bound.py` | `cc3d750d096212016534056d35d221d6e7840a4a9f192379d283c093b0f94149` |
| `PROMOTION_check_driver.py` | `1f70dda734e117dca6ed25e1f2656242fbb085ee8cd0fd6f7ee9b7de8da9a4e2` |
| `PROMOTION_check_kernel.py` | `cc7f3fded02082eee118b5eecd0f947f39486eef27ea47d8095a828d62790be1` |
| `PROMOTION_TOOL_GUIDE.md` | `6578bf5f1df4b5eaf525824075d7466b26cb7e2cd171310e377f06c7c8422571` |

The recommendation accepts this exact fixed-design comparison for assembly,
with the title and limited integration described above. It does not authorize
scientific expansion or replace the required fresh review and integration
gates for the final concrete C.5 edition.
