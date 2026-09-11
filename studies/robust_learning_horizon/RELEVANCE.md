# Independent relevance and placement screening

Selector: `/root/selector`. Date: 2026-09-11.
Decision: **accept the stated narrow result for canonical assembly**.
This is a relevance decision under RESEARCH_WORKFLOW.md Part 2, step 1,
not a scientific PASS, promotion approval, or permission to change the book.

The selector did not author, repair, or assemble the mathematical components
and is distinct from `/root`, `/root/reference`, and `/root/response`.
The assignment was to compare the proposed result with maintained coverage,
assess value, scope, assumptions, duplication and maintenance cost, and
identify the smallest suitable destination. No scientific reviewer report
or prior verdict was used. No mathematical verification or reproduction is
claimed by this screen. Only this report was written; Git and canonical
files were not changed.

## Selected scope

The package is an explicit fixed-accuracy result for two tanh hidden layers,
the canonical independent Gaussian initialization with variances
`(1,1/n,1/n²)`, the unhalved mean squared loss, mobilities `(n,1,n)`, and
actual simultaneous raw GD. The finite initial readout remains present.

Its reference is the equally weighted orthogonal pair with labels `+1,-1`.
The proposed reference result gives global autonomous population dynamics,
exponential fitting, and a whole-circle endpoint characterized by the
actual feature equation stopped when its contrast reaches one. For each
fixed binary-label law at joint Wasserstein distance less than
`exp(-exp(3000))` from that reference, the proposed finite-network result
gives, with probability tending to one, whole-circle prediction error at
most `1/4` relative to the reference endpoint, and empirical and population
risks at most `1/4`, at the preceding GD node of physical time `T=40`.
The required step condition is `eta_k sqrt(n_k)->0`. Deterministic empirical
approximations and independent iid sampling are both included; there is
no relative sample/width growth condition. A separate conclusion bounds
each paired hidden-activation squared displacement below by `10^-13` at
physical time `1/200`.

These are the statements selected for assembly. In particular, the new
perturbed-law assertion is a fixed-error finite-network comparison. It
does **not** construct a unique population trajectory for the perturbed
law through time 40, identify that law's endpoint, or provide convergence
to the reference endpoint with error tending to zero at fixed nonzero
law distance.

## Distinct value and overlap

| Maintained coverage | What is already present | Distinct proposed addition |
|---|---|---|
| Global nonlinear B.1 | Global two-hidden activation-transform dynamics at orthogonal fixed data, including tanh, with finite GF/raw-GD approximation. The theorem does not itself give fitting for every admitted activation and label choice. | Opposite-label tanh reference fitting with an explicit useful time and a flow-defined whole-circle endpoint. The reference is a specialization plus additional results, not a new general B.1 theorem. |
| Global nonlinear C.4.1–C.4.3 | Local law stability, whole-circle prediction comparison, expected signed-gap control, and simultaneous sampling/width/raw-GD consistency for arbitrary bounded-label laws. | A quantitative transfer lasting through a specified substantial risk reduction, using the long reference tail estimate. The new risk threshold is absent from the maintained local theorem. |
| Global nonlinear C.4.4 | Paired motion of both hidden representations on an open family near an equal-label reference, at a positive time and margin defined from its actual flow. | A separately proved opposite-label certificate with explicit time and margin, transferred to the same family used for the risk assertion. It must remain an early-time statement. |
| docs/README.md, prescribed-accuracy discussion | The general logical implication from compact-time approximation plus fitting to prescribed finite-time accuracy. | A concrete model, horizon, law radius, endpoint observable and two risk bounds meeting that implication. The logical strategy itself is not new coverage. |
| Special-data and finite-controls families | Other activations, fixed datasets, conditional results, or finite fitting without the present population/algorithm scope; special-data J.1 also exposes limits of general coordinate and tail arguments. | This package keeps the ordinary tanh model and transfers beyond orthogonal support. It neither subsumes the other models nor settles their broader global correlated-data questions. |

The addition addresses the book's stated interest in learned predictions
on passive inputs and in useful risk, while retaining the ordinary
initialization, full first rows, both directions of the same middle action,
and training of both hidden layers. This is sufficient distinct theoretical
value for assembly despite its severe quantitative limitation. No literature
priority claim is part of this finding.

## Assumptions and practical scope

The transport-ball hypothesis is restrictive but explicit and not vacuous
at the statement level. The theorem supplies correlated two-atom and
nonatomic examples, including small label noise and contamination. The
reference's orthogonality and equal weights are not assumptions on the
perturbed laws. No support-cardinality, Gram-invertibility, deterministic
label, or lower atom-weight condition may enter the assembled conclusion.
The endpoint is specified through an initial-value problem with the actual
initialized Gaussian action; it is not an externally supplied trained
predictor or an assumed successful continuation. Whether the component
proofs establish these facts is reserved for the scientific reviews.

The radius is far below any practical data tolerance. Together with the
absence of quantitative width, sample-size and failure-probability bounds,
it gives an explicit existence certificate rather than a usable finite
resource guarantee. The law remains extremely close to the labelled
reference pair. This limitation must appear alongside the theorem and in
its guide summary, rather than only in a proof footnote.

Whole-circle error is relative to the learned reference endpoint. It is
not a uniform-circle teacher-risk guarantee. The risk is evaluated under
the fixed nearby law and its empirical approximation. The theorem's
initial binary-label risk tends to one, so its `1/4` threshold is a
substantial reduction, but the package neither compares with a linear or
frozen-feature method nor establishes that feature motion causes the
reduction. Its activity bound does not assert persistent motion, motion at
time 40, or a quantitative nonaffinity bound along the whole trajectory.
The probabilities are for each fixed law and sequence, not uniform failure
bounds over the entire transport ball. Arbitrary accuracy for one fixed
perturbed law remains outside the selected scope.

## Smallest destination and maintenance cost

Use one new proof unit **C.4.5 in docs/global_nonlinear.md**, following the
existing law-stability and activity material. A suitable scope description
is “Fixed-accuracy prediction and risk near an opposite-label reference.”
Keep its reference fitting/endpoint argument, targeted response estimate,
finite comparison, numerical margins and paired activity proof together.
Use maintained B.1, C.4 and Gaussian-program results as explicit dependencies;
do not copy their complete existing proofs into a second maintained place.

The only other necessary destination is a concise update to the global
nonlinear row and scope discussion in **docs/README.md**. Preserve the broad
all-law local theorem separately from the narrow time-40 finite-network
guarantee. Qualify existing C.4 sentences saying there is no risk reduction
or endpoint result as applying to C.4.1–C.4.4. Do not silently broaden
B.1's input geometry or C.4's local population existence conclusion.
No shared notation change, new chapter, or maintained network API is indicated.

Maintenance cost is material: the result adds reference analysis and a
long source-response argument for one small neighborhood. It is justified
only as this single complete scoped unit. The rational constant certificate
and its mathematical bounds are proof dependencies and must remain complete
and executable without study paths or generated output. The supplied source
can accompany the proof; it does not by itself justify a new public library
API. The assembled scientific review must include that source, the producer
of its stated constants, and all full dependency bodies. Repeating the same
reference argument separately in B.1 or special_data_limits.md would add
maintenance cost without additional value.

Proceed to assembly and the workflow's fresh complete scientific reviews.
This screen supplies neither of those reviews, the independent integration
review, nor user approval. A required scientific correction blocks the
current package; retain adverse evidence and follow the workflow for the
corrected candidate rather than treating this selection as mathematical
acceptance.

## Read coverage and source versions

HEAD at completion: `7cf8c26e1fc9b7ad91085ddcd42896f120280d20`; the shared
index was empty. Unrelated working changes were preserved.

Read in full: AGENTS.md; RESEARCH_WORKFLOW.md Parts 1–2; docs/README.md;
docs/NOTATION.md; code/README.md; this study's README.md; and all five
candidate inputs listed below. REFERENCE.md was reread completely after
the final certificate-domain correction to `[0,18]`.

Maintained scientific scope read in full for comparison: global_nonlinear.md
B.1 and C.4.1–C.4.4, including their introductory statements and proofs.
Additional coverage screening read the special_data_limits.md opening
coverage/convention material and J.1, the finite_optimization_and_controls.md
opening scope, and the linear_dynamics.md opening scope/model. Targeted
text searches and docs/README.md supplied the wider coverage inventory.
The remaining chapter bodies and code implementations were not audited;
this is not a whole-book proof or code review.

SHA-256 of the complete candidate inputs screened:

| Input | SHA-256 |
|---|---|
| THEOREM.md | `46bb60ec5a867badd2bd3f9f7fe727f17c4a16fa5b34fabe94e288da7a3ad2d1` |
| REFERENCE.md | `0ada1a68210ca6bed95fbce997fca8053018e943eda8cee1632ac6aef3e1a6bf` |
| RESPONSE.md | `96be804c16c7abb62f93fa7d94a3013b08bf595dde4c15a0a367f02d43f9150b` |
| TRANSFER.md | `859b59ba8bbab4a6772b3c1e878ed1752bf151db5742ce53247a0a299851fca3` |
| certify_reference.py | `f61103c86b278da16334f30e7af2961c41b4bcaae7062c5b8433fe4eef7a2036` |

Maintained comparison versions:

| File | SHA-256 |
|---|---|
| AGENTS.md | `a5e5b3749d9e9ee088c659bc2cf4ddb2d88adf371d98bf34140ded532020a517` |
| RESEARCH_WORKFLOW.md | `4323e5ada1a4875af2c8121c742c50f07d8ff5b569c3aa71e11ef9a14605b442` |
| docs/README.md | `95b14c5a0430a783023d412d0103d8598a476963bad19180e2d4d0e2291bce3e` |
| docs/NOTATION.md | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |
| docs/global_nonlinear.md | `1945ef5d407eafd534b32185e952fa3ed479605f3ffec09afd468b6266fd18d9` |
| docs/special_data_limits.md | `5b7b48aa5deab320042217a6f284002366a683bf0f7f0b63c05d8167c526a489` |
| docs/linear_dynamics.md | `8de3beaca0cd6f970c27a25eb8c2bc4a1fefa2e7840bd97e7bccfc4f41281c1d` |
| docs/finite_optimization_and_controls.md | `80dcce91ed3cd8313654523725e28b312ab925376cd7a28d71323bed648a5628` |
| code/README.md | `00f5070d35a3e9fb9d0e9886f0f6d9f680a8d34bb32307807d1f88afc807a774` |
