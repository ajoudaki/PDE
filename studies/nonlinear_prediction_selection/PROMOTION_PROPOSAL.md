# Milestone A: nonlinear prediction selection — proposed C.4.9

Status: prepared concrete proposal; final v3 review gates are still in progress.
This proposal does not authorize or apply established-file edits.

## Scientific result and exact scope

For the original canonical two-hidden-layer, bias-free tanh network with
stored Gaussian variances `(1,1/n,1/n²)`, mobilities `(n,1,n)`, unhalved mean
square and physical GF, retain the actual finite Gaussian readout, full first
rows, initialized middle action and its true adjoint. Each actual run starts
from the original initialization and uses its fixed mixture throughout.

Take

\[
\nu_{\alpha,y}=\delta_{(\sqrt2(\cos\alpha,\sin\alpha),y)},\qquad
|\alpha-\pi/4|\le1/1216,\qquad 3/8\le y\le5/8.
\]

This rectangle has nonempty interior in input location and label; its inputs
are nonorthogonal to both reference anchors. The labels are admissible for
every fixed `Y >= 1`.

There are common constants `epsilon0,tau0,a,j>0`. Let `theta_dagger` be the
established fitted reference latent state. The selected finite episode solves

\[
\dot{\bar\theta}=-2(f_{\bar\theta}(u_\alpha)-y)
 \bigl(I-G_{\bar\theta}(G_{\bar\theta}^*G_{\bar\theta})^{-1}
 G_{\bar\theta}^*\bigr)g_{\bar\theta}(u_\alpha),
\qquad \bar\theta(0)=\theta_\dagger.
\]

Here `g_theta(u)` is the complete raw prediction gradient and `G_theta` contains
the two current anchor gradients. The full current state is `(w,K,c)` with
`A=A0+K`; all hidden fields and the projection evolve. The complete definitions,
initialized Gaussian carrier and unique strong construction are in the
[candidate](CANONICAL_ADDITION_v3.md). For every circle input,

\[
P_{\alpha,y}(\tau,\sqrt2u)
=\langle\bar c(\tau),\tanh((A_0+\bar K(\tau))
                         \tanh(\bar w(\tau)\cdot u))\rangle.
\]

The anchor predictions stay fixed in this selected equation. This constraint
comes from the fast reference-residual relaxation in original-mixture training;
it is not an imposed staged optimizer or frozen-feature approximation.

At physical horizon `T_epsilon=tau0/epsilon`, the original mixture population
prediction tends uniformly over the whole circle to `P_alpha,y(tau0)` as
epsilon tends to zero. Population convergence is uniform over the parameter
rectangle and over slow-time intervals `[tau_min,tau0]` with `tau_min>0`.
The proof supplies continuation through this horizon and the original
initial layer; convergence is not asserted at slow time zero.

The added-component risk gain is at least `a>0`, without multiplying it by
epsilon. The normalized average of the second-hidden squared differences at
the two anchors and added input is at least `j>0`, relative to the reference
endpoint on the same initialized carrier. Actual finite GF captures the whole
prediction and the internal observations in probability, taking width to
infinity first at each fixed positive epsilon, then epsilon to zero. The finite
hidden comparison trains both laws on exactly the same initial arrays and
observes them at the same finite `T_epsilon`; it assumes no finite-width endpoint.
Consequently risk gain at least `a/2` and hidden displacement at least `j/2`
hold with probability tending to one in that iterated order.

The new mathematical steps are an integrated-control Gaussian-source bound
uniform in physical horizon, protected-row endpoint conditioning, strong
constrained construction, actual-mixture continuation, a residual identity
selecting the slow clock, and an actual finite-GF same-array observation bridge.
These supply the nonlinear episode beyond the established finite-time response.
No decisive conditioning, tail or continuation premise is left assumed.

## Concrete proposed changes

Apply exactly [PROPOSED_EDITION_v3.patch](PROPOSED_EDITION_v3.patch):

1. Append the complete canonical C.4.9 and insert its scope sentence in
   `docs/global_nonlinear.md`.
2. Add matching navigation/scope text to the two relevant entries of
   `docs/README.md`, using [the complete proposed guide](PROPOSED_GUIDE_v1.md).

The explicit edit specification is [PROPOSED_EDITS_v3.json](PROPOSED_EDITS_v3.json).
The proposed addition uses established dependencies in their existing locations;
it does not depend on study files, conversation history or generated arrays.
The notation contract, existing proofs and maintained code are preserved.

| Reviewed object | SHA-256 |
|---|---|
| Complete canonical addition v3 | `c858c7b41d90b490871450b8bf7494afe8c6cd7f39bebd3f1faa89f3604a5879` |
| Concrete proposed patch | `ce121bad1089ca01e471c5c0a20fbfb8ef58f428258eba6b36ae9dd7e7b5b573` |
| Assembled proposed global chapter | `7633fb054cf02f2359b193fcb090634304cc1153f4d8f978fd0ac30789355465` |
| Complete proposed guide | `d5ecdfd35fbddd511d98dccd148a9a9e840f5a4c814658f930c5732bab218bc5` |

The [review manifest](REVIEW_MANIFEST_v3.json) and
[dependency manifest](DEPENDENCY_MANIFEST_v1.json) retain every input fingerprint.
The [standalone edition](../../data/generated/nonlinear_prediction_selection/standalone_v3/docs/global_nonlinear.md)
is available for inspection before any established edit.

## Review and validation record

Independent [relevance screening](RELEVANCE_SCREENING.md) accepted the complete
combination for C.4.9, with this minimal destination and exact finite-episode scope.
The initial packet received [A's PASS](ADVERSARIAL_A_v1.md) and
[B's required correction](ADVERSARIAL_B_v1.md). The latter identified a false
auxiliary assertion for repeated inputs. [The correction](CORRECTION_v2.md)
adds pairwise distinctness in two sentences; the actual law family already
satisfies it. The old packet and adverse report remain unchanged and are not
used as acceptance evidence for v3.

The original [integration review](INTEGRATION_REVIEW_v1.md) required explicit
finite RMS normalization in the comparison proof. [Correction v3](CORRECTION_v3.md)
defines normalized hard/soft tails, displays finite rank/hidden factors, and
uses continuous soft-tail convergence. The theorem and all limits are unchanged.
This adverse report and all superseded packets are retained.

Two new complete isolated v3 mathematical reviews and a new separate integration
review are in progress. They receive frozen complete inputs and no prior verdicts.
Final acceptance requires all their original reports and coordinator provenance
checks; this proposal's status will be updated only after those gates close.

[Standalone validation v3](STANDALONE_VALIDATION_v3.md) passed. It constructed a
fresh documentation-only edition, verified frozen and live dependency hashes,
checked all new links and mathematical delimiters, reversed the chapter delta
to recover older content, and preserved every other documentation file byte for
byte. The exact rational reference certificate was independently rerun with
Python 3.10.12, standard library only, and exited zero. Its printed values are
`[0.392108947877, 0.396376711612, 0.233120735618, 0.339792209687, 0.631761866359]`;
assertions use exact rational comparisons, not those rounded decimals.
No training experiment was run or claimed.

## Limits and approval boundary

The result is a fixed positive episode on an open one-atom parameter family.
The constants may be numerically impractical. It does not assert a final
changed-law endpoint, useful simultaneous width rates, raw GD, a first-hidden
margin, the necessity or superiority of hidden adaptation, or out-of-sample
generalization. Those are outside this milestone's resolved target.

Once all final reviews pass, the recommendation is to approve precisely this
C.4.9 and guide package. Approval under Part 2.5 of `RESEARCH_WORKFLOW.md` must
precede changing established files. After approval, recheck dependencies and
concurrent changes, apply only the reviewed patch, verify live files against
these proposed hashes, and retain the correspondence record and scoped commit.
A changed scientific dependency or package requires renewed review and approval.
