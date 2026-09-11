# Concrete promotion proposal: local training-law stability

Approved destinations: `docs/global_nonlinear.md` and `docs/README.md`.
Status: user-approved P2 incorporated exactly; see the
[integration record](PROMOTION_INTEGRATION.md) for approval and verification.

The exact new mathematical source is [P2_ADDITION.md](P2_ADDITION.md),
appended as C.4 after C.3. Five precise chapter scope edits are recorded in
[P2_GLOBAL_EDITS.json](P2_GLOBAL_EDITS.json); their complete assembled result
is [P2_GLOBAL_EDITION.md](P2_GLOBAL_EDITION.md). The second destination now
equals [P2_DOCS_README.md](P2_DOCS_README.md). All version identities are in
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
P1 evidence is retained. The corrected proposed edition received two fresh
complete scientific acceptances with no required corrections:
[P2 review A](P2_REVIEW_A.md) and [P2 review B](P2_REVIEW_B.md). The separate
fresh complete [P2 integration review](P2_INTEGRATION_REVIEW.md) also accepts,
with no required correction. The coordinator read all original reports in
full and verified their provenance and exact input hashes. The integration
review's generic role label is distinguished from its verified fresh process
identity in the study README and retained execution evidence.

[Standalone validation](P2_VALIDATION.md) passed with exact candidate-to-edition
correspondence, unchanged-content preservation, valid new links and equation
references, and no study dependencies in the new canonical proof. There are
no empirical claims or maintained APIs requiring training reproduction.
The unrelated exporter and unchanged book complement are outside validation.
The independent integration reviewer reproduced all six scientific artifacts
byte for byte and separately checked exact assembly and preservation. Before
integration, live dependencies and destination baselines matched the frozen
proposal. After integration, live destinations match the approved outputs.

Recommendation implemented: promote exactly this scoped P2 addition. Its
scientific and integration review gates passed, and the user approved this
package. The complete incorporated chapter has SHA-256
`1945ef5d407eafd534b32185e952fa3ed479605f3ffec09afd468b6266fd18d9`,
and the guide has SHA-256
`95b14c5a0430a783023d412d0103d8598a476963bad19180e2d4d0e2291bce3e`.
The integration rechecked live baselines/dependency hashes and the shared
index, verified exact correspondence, and uses the common writer lock for
the owned Git transaction. Future changes of scientific dependencies or
content are outside this package's approval and review identity.
