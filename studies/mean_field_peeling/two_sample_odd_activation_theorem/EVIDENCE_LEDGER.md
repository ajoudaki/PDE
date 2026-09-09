# Evidence ledger

2026-09-07. No numerical experiment supplies any claim in this extension.
The complete proof has passed three fresh independent adversarial reviews
at the final file hashes. Review outcomes are recorded separately from
proof dependencies in REVIEW_STATUS.md and REVIEW_CERTIFICATE.json.

| Claim | Level | Evidence and dependencies | Current status |
|---|---|---|---|
| Odd-network label folding preserves the exact raw finite loss and GF/GD | Exact finite identity | AFFINE_CORE §1; both forward and backward sign factors | Proved; independently audited |
| One affine feature interval reaches prediction 3/2 with bounds depending only on delta | Strong existence and deterministic bounds | AFFINE_CORE §§3--4; polynomial field, radial norm convexity, energy endpoint extension | Proved; independently audited |
| Every affine sample/layer preactivation is centered Gaussian with variance at least delta/32 | Exact population property | AFFINE_CORE §5; independent inactive root, finite conditional estimates, fixed-program and Euler limits | Proved; independently audited |
| The nonlinear source-response threshold is uniform for zero offset and every gain in [1/2,1] | Construction and approximation control | SOURCE_AND_LIMIT_BRIDGE §§1--3; attached source and controlled-response recurrences, current returns included | Proved; independently audited |
| One positive e_delta gives a global autonomous strong uncut population loss flow and unique reached-state continuation | All finite physical horizons, one trajectory | PROOF §§4--5; endpoint margin, exact scalar clock, asymmetric comparison | Proved; independently audited |
| The original finite GF and raw GD step n^-2 converge jointly along the full width sequence | Identification with original algorithms | PROOF §5; SOURCE_AND_LIMIT_BRIDGE §5; both actual finite residuals and small random readout retained | Proved; independently audited |
| Four raw kernels, canonical actions/adjoints, hidden path and stipulated state/velocity laws converge in their stated topologies | Observable convergence | PROOF §2 and §5; ordered cap/velocity truncation limits and path interpolation estimate | Proved; independently audited |
| All sample/layer activation-regression errors stay at least e^2 eta/4 at every finite physical time | Uniform nonlinear nondegeneracy | AFFINE_CORE §6 and PROOF (23); explicit compact Gaussian margin plus strong comparison | Proved; independently audited |
| Every hidden block and every sample/layer has nonzero initial acceleration; projected kernel changes | Initial feature learning | INITIAL_MOTION_AND_NORMALIZATION §§1--5; full second-moment transpose sources and both responses | Proved; independently audited |
| A nontrivial convex mixture of z and arctan z suffices | Existence of requested witness | PROOF (3), parameter rectangle and e_delta<=1/4 | Proved; independently audited |
| A positive mixture with exact unit Gaussian energy also suffices | Existence of normalized witness | PROOF (4), §6; coefficients remain in the proved rectangle | Proved; independently audited |
| A nontrivial literal convex mixture also has exact unit Gaussian energy | Proposed stronger conjunction | Strict pointwise contraction, INITIAL_MOTION_AND_NORMALIZATION §7 | Falsified |
| One odd activation satisfies the older one-sided separation including antipodal equal labels | Proposed stronger data class | Oddness forces f(-x)=-f(x); H is identically zero for that label pair | Falsified; old obstruction remains valid |
| Under the same absolute-correlation separation, an odd or normalized activation satisfies the complete three-input theorem | Stronger extension | Not proved by a two-input reflection/clock argument | Open; outside this proof |

## Supersession and boundaries

The old two-input offset theorem and the old three-input large-gain
theorem remain unchanged. Their proof files and source hashes are not
modified. This extension narrows the two-input data class to exclude
both correlation endpoints and then proves a new zero-offset family.

The earlier statement that normalization was not justified by the
large-gain three-input proof remains correct. The present two-input
normalization conclusion follows from a fresh theorem uniform in a
compact interval of linear coefficients, not an invariance of the old
raw dynamics under scaling the activation.

No optimal coefficient, useful numerical lower bound, threshold
monotonicity, one activation for every positive delta, perpetual
nonzero hidden velocity, trained energy conservation, or infinite-time
uniform width convergence is claimed.

All three independent reviewers read the four complete mathematical
files and inspected the underlying source proofs. A local statement
that conflated the capped feature field with the uncut gradient was
corrected; the downstream cap-clock argument already used the correct
field. Missing LaTeX separator backslashes were also restored. Each
reviewer checked the revisions and verified the final hashes. No
remaining proof obligation was identified for this two-input theorem.
