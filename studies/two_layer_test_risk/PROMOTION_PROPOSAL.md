# Proposed book addition: controlled risk expansion at equal training loss

This proposal concerns the proved partial reduction, **not a theorem that
hidden learning improves test risk**. The bounded study leaves the exact
cubic coefficient's sign and nonvanishing open. No established file has
been edited.

## Concrete addition and value

Append [PROMOTION_C4.md](PROMOTION_C4.md), unchanged, after C.3 of
`docs/global_nonlinear.md`. It is a single 642-line proof subsection for the
fixed two-hidden-layer tanh, three-angle, uniform-circle model. It proves
unique training-loss matching and

\[
 \tau(t)=t+\beta t^3+O(t^4),\quad\beta>0,\qquad
 |R(g_{\tau(t)})-R(f_t)-\chi t^3|\le Mt^4.
\]

The appendix gives the complete initialization-only Gaussian formula for
`chi`, the actual-flow remainder proof, both matrix-response directions,
and the conditional implication from a subsequently proved strict sign.
It keeps the finite random readout and restricts finite matching/sign
transfer to fixed intervals away from zero. No numerical radius, width
rate or signed benefit is asserted. The distinct value is a controlled
comparison after accounting for training speed, beyond the existing
activity and path-capture results.

Append this exact sentence to the global-nonlinear chapter row in
`docs/README.md`:

> A fixed two-hidden-layer tanh design also admits a controlled cubic test-risk expansion at equal training loss; the coefficient's sign and nonvanishing remain open.

There are no code changes, empirical additions, numerical estimates,
duplicated activity proofs or altered older theorem statements. The prior
global chapter is preserved byte-for-byte as a prefix. The guide changes
one existing line only.

## Exact version and reproducible assembly

Candidate SHA-256:
`b807efbd793b5b6ebc67e7f673efbcae4a234eacd28e667c304597c51d7435d4`.
Proposed full global chapter SHA-256:
`5f31b500a60ad98fd9a200094f1169267a590a39015aaa53c8c222bc07cb3fc2`.
Proposed guide SHA-256:
`e92464827a2d277a57a356167190598f52425769e23e7538cd9e3cbbe7afb371`.

The exact frozen complete dependency packet, before/after guide, manifest
and standalone edition are under
`data/generated/two_layer_test_risk/promotion_v1/`.
They are reproducible from the retained source by:

```sh
python -B studies/two_layer_test_risk/assemble_promotion.py --output data/generated/two_layer_test_risk/promotion_v1_reproduction
```

The output name must be fresh. The assembler refuses changed scientific
base hashes, writes only the study's generated namespace and never edits
the live book. Unique proof source and the assembly method remain in the
study; the old dependencies are versioned maintained sources.

The integration review's original check source is retained byte-for-byte as
[check_promotion_integration.py](check_promotion_integration.py). It expects
to execute from the generated edition's `integration_scratch` directory.
After the fresh assembly above, reproduce that check with:

```sh
mkdir data/generated/two_layer_test_risk/promotion_v1_reproduction/integration_scratch
cp studies/two_layer_test_risk/check_promotion_integration.py data/generated/two_layer_test_risk/promotion_v1_reproduction/integration_scratch/check_integration.py
python -B data/generated/two_layer_test_risk/promotion_v1_reproduction/integration_scratch/check_integration.py
```

This preserves the original reviewer-executed source and keeps all generated
check results in the fresh run. Its SHA-256 is
`028cba4a0ff9c166c484dadbb290391fe1c25f6b5c7204a1c6e3d33616273727`.

The standalone edition has no study/history dependency. Its boundary and
local-link check passed for all 12 included source files. The candidate's
displayed math delimiters balance; the base chapter prefix, unchanged copied
files and one-line guide scope are verified separately. No code/empirical
addition exists, so no scientific training reproduction or new API test is
part of this proposal. The broader unchanged code library was not recertified.

## Gates and decision

Independent relevance selection: **NARROW / accepted for assembly**;
see [RELEVANCE.md](RELEVANCE.md). Internal proof checking is recorded in
[INTERNAL_REVIEW.md](INTERNAL_REVIEW.md), separately from promotion.

The two fresh complete scientific reviews are **ACCEPT**:
[review A](PROMOTION_REVIEW_A_V1.md) and
[review B](PROMOTION_REVIEW_B_V1.md). The separate fresh
[integration review](PROMOTION_INTEGRATION_V1.md) is **PASS**. All three
completed on the frozen bytes above, report no required corrections, and
retain full coverage, independent attacks and limitations. The coordinator
read every original report and verified all report/packet hashes. The
integration check independently confirmed the two-file scope, exact old
chapter preservation, equation references, dependency copies and standalone
boundary/link check. Precise older read scope and unread complement are in
the integration report; this is not a whole-book proof audit.

Recommendation: **approve this exact proof-only partial result**. It makes
the equal-training-loss comparison rigorous and isolates one explicit scalar
sign obligation. Approval must not describe it as a demonstrated test-risk
improvement. The study's inconclusive numerical diagnostics are excluded.

User approval is required before either established destination changes,
under RESEARCH_WORKFLOW Part 2, step 5. Approval does not substitute for the
scientific gates. All gates preceding approval are complete. If approved, integration must
recheck the live dependencies and preserve the exact reviewed edition.
