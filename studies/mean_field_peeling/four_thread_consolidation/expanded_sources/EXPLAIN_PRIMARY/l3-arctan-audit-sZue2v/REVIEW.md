# Independent review record

Target: the three-hidden-layer arctangent model with rescaled output initialization N(0,n^-2) per coordinate, hence zero limiting readout. Full unconditional population well-posedness and joint width/learning-rate convergence were requested. They were not established.

Three independent research routes examined deterministic stability/coordinate changes, Gaussian-response tail estimates, and older proposed proof arguments. None returned a complete proof. In particular, the older order-one Gaussian readout contract was not treated as interchangeable with the present zero limiting readout.

Two fresh reviewers were then given only EXACT_RESULTS_AND_GAP.md, without the conversation or other project notes. They audited the note, not a purported infinite-width proof.

Initial review found a tilded-signal typo in the truncation estimate and requested narrower language distinguishing vector-field continuity from solution-map stability. Both were corrected. The separate fixed-step probabilistic theorem was explicitly identified as not proved in the note.

Final verdicts on the corrected note:

- l3_blind_logic_audit: PASS for the corrected mathematical content, including finite equations, dissipation, global bounds, spike example, truncation estimate, and accurate unresolved status.
- l3_blind_algebra_audit: PASS for the revised internally verifiable mathematical claims, including metric scaling, Gaussian initialization assertions, and the same finite-width results and obstruction.

Neither verdict establishes the requested population theorem. External citations and historical provenance were outside these reviewers' permitted material. No formal machine verification was performed. The mathematical work here is a rigorously checked partial audit with a remaining proof obligation, not a completed L=3 extension.
