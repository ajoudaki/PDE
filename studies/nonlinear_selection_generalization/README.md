# Nonlinear selection generalization (milestone B)

Status: research and review complete at the declared finite-episode scope;
v2 is ready for promotion approval. Both fresh complete scientific reviews
and the separate fresh integration review PASS with no required corrections.
No unresolved gap remains within that scope. Nothing promoted; no established
file changed. V1's adverse review and explicit finite-cap repair are retained.

## Contract frozen before learning analysis

Work starts from established C.4.9 in `docs/global_nonlinear.md`, present at
HEAD `b14dc38bdca0c7835685e768e6ca0657d60cf10d`, SHA-256
`7633fb054cf02f2359b193fcb090634304cc1153f4d8f978fd0ac30789355465`.
No unpromoted milestone-A inputs are admitted. Scientific inputs are this
study and established book/code. All research sources and reports remain flat
here; generated checks go to `data/generated/nonlinear_selection_generalization/`.

Retain C.4.9's two-hidden-layer bias-free tanh model, independent stored
Gaussian variances (1,1/n,1/n^2), mobilities (n,1,n), division of the readout by
n, unhalved square loss, physical GF, full first rows, reused Gaussian middle
action and its actual adjoint. Every physical run uses its fixed mixture from
the original initialization. Anchors retain their exact known weights.

**Frozen task class.** Write x=sqrt(2)(cos(alpha),sin(alpha)), alpha modulo
2*pi, and let rho be normalized arc measure on the entire circle. Inputs have
density p with respect to rho, 1/2 <= p <= 2, integral p=1, and circular
Lipschitz constant at most D, where D>=0 is fixed. The support is the entire
circle and never shrinks. For an integer N>=0 and s>=1, set

q(alpha)=cos(alpha)^3-sin(alpha)^3 + sin(2*alpha)^2 v(alpha),

v(alpha)=sum_{k=0}^N [a_k cos((2k+1)alpha)+b_k sin((2k+1)alpha)],

sum_k (2k+1)^s (|a_k|+|b_k|) <= R <= 1/8.

The coefficients, N, R and s specify independently varying target shape and
complexity; they do not depend on any trained predictor. This is odd and
equals +1 and -1 at the two anchors. Noise satisfies E[xi|X]=0,
|xi| <= sin(2*alpha)^2/8 and E[xi^2|X] <= sigma^2 (sigma<=1/8).
Then |Y|<=1, hence this class is admitted for every supplied Y>=1:
|cos^3(alpha)-sin^3(alpha)| <= 1-sin(2*alpha)^2/4, while
|v|<=1/8 and the noise consumes at most the other 1/8 of that margin.
The class also admits the absolutely convergent infinite series with the same
weighted coefficient bound; truncation is an explicit approximation option.
Any later material change to this class must be recorded before deriving a
favorable conclusion. A robust subfamily may be identified inside this class.

Observations (X_i,Y_i) are iid only from the added law and independent of
initialization. Test error is ||f-q||^2_{L2(nu_X)}, subtracting irreducible
noise from squared risk. Whole-circle prediction remains an observable.

Required result: population and empirical nonlinear slow selection with
continuation/capture at t=tau/epsilon; explicit target-dependent approximation
or contraction; sampling and centered-noise control and an available stopping
rule; strict unseen-risk improvement and paired second-hidden displacement on
a robust subfamily; actual finite-GF transfer with width first, then epsilon
down to zero, then sample size increasing. A finite positive episode with a
declared approximation floor is sufficient. No training experiments or broad
computational campaign are authorized. Deterministic verification is allowed.

## Work and ownership

The root coordinator owns this README and the synthesis. Independent attempts
will receive fresh contexts, explicit input scopes and disjoint flat files.
Only the coordinator may stage or commit, under the shared pde-writer flock;
other tasks' modified and untracked paths remain untouched.

Required reading: AGENTS.md, both parts of RESEARCH_WORKFLOW.md, docs/README.md,
docs/NOTATION.md, complete C.4.9 and relevant complete established dependencies.
Skills: solve-math-rigorously and investigate-conjectures, including research
contract, proof-search orchestration, evidence and adversarial-audit references.

## Evidence and open obligations

The following first-round arguments are persisted as candidates, not yet
independently checked or promoted:

- [Population spectral route](attempt_population.md): signed-measure
  separation, continuum middle-gradient injectivity, a spectral contraction
  with a Fourier approximation floor, and robust risk/activation margins.
- [Finite-section oracle route](attempt_alternative.md): the same structural
  injectivity reached independently, a comparator oracle with nonlinear
  drift, and training/validation sampling options.
- [Finite target-mode route](attempt_finite_modes.md): root's direct
  degree-dependent contraction, using a finite space containing the
  established reference residual exactly. This avoids requiring an
  unknown Fourier-tail estimate for that reference residual.
- [Statistical lemma](sampling_lemma.md): root's separate input/noise Hilbert
  variance argument and explicit Osgood propagation on the slow horizon.
- [Continuation route](attempt_continuation.md): complete candidate for
  bounded Borel-law construction, original-mixture continuation, selection
  and actual finite-GF capture.

The independent agents started with fork_turns="none" and did not read each
other's attempts before freezing. All three independently identified the
same protected-row/sign-Fourier mechanism; their approximation methods
differ. No failed mechanism is being presented as a false target.
After population_route froze its candidate, it was assigned an internal
audit of the root's frozen finite-mode and statistical files. This later
comparison is explicitly not an independent promotion review.

The post-freeze internal comparisons are preserved in
[finite modes and sampling](internal_modes_check.md) and
[sampling/continuation interface](internal_sampling_interface.md). They check
the principal algebra and supply explicit stability, source-radius and
positive-horizon constants. Root's [combined bounds](combined_bounds.md)
close the robust stopping, hidden contrast and sample threshold interfaces.
These are author-side checks, not promotion reviews. Root read all three
initial attempts and both full internal reports. Root saw the continuation
file's final twenty lines shortly before its author marked the file frozen;
root is an assembler, and this does not count as independent blind review.

A fresh independent selector, who authored no result, read its scoped inputs
and accepted one C.4.10 for assembly: [neutral assignment](relevance_assignment.md),
[full disposition](relevance_report.md), report SHA-256
`020c126d5d0d537ca9881320056fa877e2b7a5742ac75021c9beb949b64773ff`.
The selected scope is bounded-law capture, continuum separation, finite-mode
nonlinear approximation, separated input/noise sampling, and a robust
unseen-risk/paired-hidden corollary. Redundant spectral/oracle developments
remain study results. The first owned scoped commit is
`eecb6433c8c6f7a73596488aa90f82f7c9d93082`.

The established exact rational reference certificate was rerun successfully:
[check source](check_reference_certificate.py), generated report
`data/generated/nonlinear_selection_generalization/reference_check_20260912_01/reference_certificate.json`.
Python 3.10.12, all exact assertions passed; output was
`[0.392108947877, 0.396376711612, 0.233120735618, 0.339792209687, 0.631761866359]`.
Reproduce with
`python3 studies/nonlinear_selection_generalization/check_reference_certificate.py data/generated/nonlinear_selection_generalization/<fresh-directory>`.
No training experiment was run.

The original [v1 C.4.10](candidate_addition_v1.md) and
[v1 reading-guide addition](candidate_docs_README_v1.md) were frozen under
[v1 scientific manifest](scientific_manifest_v1.json), commit
`13dd024d516f490ea85d5c65878125f089f37f7e`. The
[standalone edition checks](edition_validation_v1.md) passed within their
declared deterministic scope. There is no identified
persistent GF obstacle warranting a change of algorithm. The canonical
assembly uses one source-based gradient modulus consistently for continuation,
sampling and hidden contrast, replacing redundant endpoint constants.
Fresh reviewers `scientific_review_v1_a` and `scientific_review_v1_b` each
received the [same neutral assignment](scientific_assignment_v1.md) and
complete frozen dependency bodies, with no internal verdicts or author history.
Fresh `integration_review_v1` received the separate
[integration assignment](integration_assignment_v1.md) and
[assembled-edition manifest](integration_manifest_v1.json), without the other
reviewers' findings. Root has read all three reports completely; original
reports and evidence remain unchanged. Review A required the explicit zero
higher-coefficient condition that the robust proof uses. Review B and integration
passed their interpreted finite-cap scope, which does not override A's objection.

Current gate: [v2 C.4.10](candidate_addition_v2.md),
[unchanged guide scope](candidate_docs_README_v2.md), and
[complete frozen v2 packet](scientific_manifest_v2.json). The
[revision record](revision_v2.md) gives the exact six-line correction,
original report hashes, new deterministic checks and fresh-review identities.
Reviewers `scientific_review_v2_c`, `scientific_review_v2_d`, and
`integration_review_v2` completed their isolated reviews and all passed. Root
read each original report completely and checked its provenance, hashes,
coverage and retained deterministic evidence. The
[final review record](final_review_record_v2.md) fixes the exact accepted
scope, report hashes and unchanged source/edition checks. The
[concrete promotion proposal](promotion_proposal_v2.md) recommends the appended
C.4.10 and three reading-guide additions. The v2 packet was committed as
`b384475316cc0e18bab14438f0140f8f2ede6c9a`.
Next action: obtain user approval of this reviewed package. After approval,
recheck dependencies and concurrent changes, apply the exact reviewed edition,
verify live correspondence and make a scoped integration commit.
No established file may change before those gates and user approval.
