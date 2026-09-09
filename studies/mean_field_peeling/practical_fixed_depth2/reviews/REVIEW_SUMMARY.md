# Isolated reviews of the partial cap-removal manuscript

2026-09-08. The input reviewed is [CAPS_MANUSCRIPT.md](../CAPS_MANUSCRIPT.md), a self-contained proof of global dissipative approximants and a **conditional** population continuation theorem. Its unproved exponential-tail premise and the requested actual finite-width GF/GD theorem are explicitly outside its conclusions. Acceptance below does not resolve the user's main goal.

The first pair of isolated readers read only the manuscript. They found two missing addition signs in the displayed chain rule and requested a more explicit sequential argument for real-valued cap parameters. Both mathematical explanations were already supported by the surrounding proof. The display and compactness explanation were corrected.

Two new readers then independently received only the corrected whole manuscript, without previous discussion, development notes, or review history. They performed no external-source lookup or experiment and made no edits to the input.

Final manuscript SHA256:

`c83bdce94e4655befbc35c88cafb19012c39a9fb2a3a08ced3ef216433acbaed`

| Fresh isolated review | Verdict |
|---|---|
| [CAPS_FINAL_ONE.md](CAPS_FINAL_ONE.md) | PASS, no objections |
| [CAPS_FINAL_TWO.md](CAPS_FINAL_TWO.md) | PASS, no objections |

The accepted claims are exactly Theorem 1 and Theorem 2 at their stated scopes. Theorem 1 supplies an unconditional energy-preserving approximation construction. Theorem 2 proves what an additional uniform exponential tail estimate would imply on the already-given population spaces. Neither reviewer supplied that missing estimate, Gaussian-action identification, or the full actual finite algorithm observation bridge. These remain open.

## Separate reviewed confinement lemma

The complete [PLATEAU_CONFINEMENT.md](../development/PLATEAU_CONFINEMENT.md) gives a deterministic control-independent first-row amplitude bound for three compactly supported gates, with rank-two and rank-three input geometry treated separately. Its population consequence assumes existing pathwise integral solutions. It does not claim population existence, source tails, uniqueness of the coupled population flow, or finite-width/GD convergence.

The first isolated reader accepted the deterministic proof but found that the population corollary needed an explicit almost-sure local absolute-continuity premise. That premise and the equivalent pathwise integral-equation condition were added; the elementary Euler observation was also made explicit for a nonzero gate. Two fresh readers then received only the whole corrected report, with no other reports, history, linked files or reviews. Both returned PASS with no required corrections.

Accepted confinement SHA-256:

`e66b09fd0b115113da658cff6a0e7f3da3ddbc5401360b275546cdacb027b5d3`

| Fresh isolated review | Verdict |
|---|---|
| [PLATEAU_CONFINEMENT_FINAL_TWO.md](PLATEAU_CONFINEMENT_FINAL_TWO.md) | PASS, no objections |
| [PLATEAU_CONFINEMENT_FINAL_THREE.md](PLATEAU_CONFINEMENT_FINAL_THREE.md) | PASS, no objections |

This acceptance certifies precisely the confinement report. The distinct plateau activation's other development notes and the full global joint-limit target have not acquired that status by association.
