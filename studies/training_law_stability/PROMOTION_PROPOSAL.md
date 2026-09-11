# Concrete promotion proposal: local training-law stability

Proposed destinations: `docs/global_nonlinear.md` and `docs/README.md`.
No established file has been changed. User approval is pending.

The exact new mathematical source is [P2_ADDITION.md](P2_ADDITION.md), to be
appended as C.4 after C.3. Five precise chapter scope edits are recorded in
[P2_GLOBAL_EDITS.json](P2_GLOBAL_EDITS.json); their complete assembled result
is [P2_GLOBAL_EDITION.md](P2_GLOBAL_EDITION.md). The second destination would
become [P2_DOCS_README.md](P2_DOCS_README.md). All version identities are in
[P2_MANIFEST.json](P2_MANIFEST.json). The proposal does not change maintained
code, the notation guide, or the existing C.1–C.3 proofs.

The addition gives a common positive-time autonomous population evolution for
every law on the normalized input circle with labels bounded by Y, for exactly
two hidden tanh layers with the stated Gaussian initialization and raw metric.
It proves quantitative continuity of the complete first-row/operator/readout
state and the whole learned prediction function, with modulus
`C q exp(C sqrt(log(e/q)))` for joint input-label W1 distance `0<q<=1`.
The q=0 and larger-distance cases are explicit. No atom-weight, Gram-rank,
separation or input-label-correlation restriction is imposed.

Its consequences are the requested `C/m exp(C sqrt(log(em)))` replacement
bound, the same bound on `sup_t |E_S[R_mu(f_S(t))-Rhat_S(f_S(t))]|`, and
simultaneous sample/width/raw-GD-step consistency without relative growth
conditions. Both empirical training loss and population risk converge to the
population-flow risk. The same theorem contains an open family of laws with
positive finite-time averaged activation displacement in both hidden layers,
and transfers that displacement to the finite networks in probability.

This demonstrates coexistence of quantitative training-law stability and
nonvanishing nonlinear hidden learning. It does not establish fitting,
endpoint selection, useful risk reduction, excess risk, superiority over
another model, global-time control, or quantitative finite-width rates. The
statistical bound concerns the absolute value of the expected signed gap;
it is not an expected absolute gap or an expectation of a time supremum.
Activity is asserted only on the specified open family. The positive time
and activity constants are mathematically defined, without numerical
performance guarantees.

Independent [relevance screening](RELEVANCE.md) accepts this scope and
placement. The canonical source consolidates repeated proof arguments and
uses the existing complete Gaussian/response foundations. The standalone
input retains those complete proofs in [P2_DEPENDENCIES.md](P2_DEPENDENCIES.md),
so correctness does not depend on study history or prior verdicts.

The research result received two complete isolated acceptances with no
required corrections: [research review A](R1_REVIEW_A.md) and
[research review B](R1_REVIEW_B.md). The first canonical edition received
two scientific acceptances, but its [integration review](P1_INTEGRATION_REVIEW.md)
required two notation corrections. Both are corrected in P2; all original
P1 evidence is retained. The corrected proposed edition must receive two new
complete scientific reviews and a separate fresh integration review. Their
final original reports will be linked here before approval is requested.

[Standalone validation](P2_VALIDATION.md) passed with exact candidate-to-edition
correspondence, unchanged-content preservation, valid new links and equation
references, and no study dependencies in the new canonical proof. There are
no empirical claims or maintained APIs requiring training reproduction.
The unrelated exporter and unchanged book complement are outside validation.

Recommendation: promote exactly this scoped addition once its new scientific
and integration review gates pass and the user approves the frozen package.
Before applying approval, recheck live baselines/dependency hashes and the
shared Git index, use the common writer lock for the owned Git transaction,
and verify that the live result equals the reviewed edition byte for byte.
Changed scientific dependencies or content reopen review and approval.
