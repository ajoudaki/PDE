# Independent reviews of the finite-width readout theorem

Reviewed file: READOUT_COERCIVITY.md.
SHA-256: 0bd062da74fbde03d41a125561beee7345915ea6aa0578ed8e7b81d2c9f08c53

Both reviewers were instructed to inspect only the candidate proof for
this audit, without other current notes, sources, reviews, or agent
messages. Neither reviewer received the other verdict.

- l3_coercivity_blind_audit_one: a fresh isolated agent; PASS, no
  mathematical gap in the finite-width scope.
- l3_blind_check_two: independently reviewed the new proof; PASS,
  no mathematical gap in the finite-width scope. This reviewer had
  earlier reviewed a different finite-width note in the task; it was
  not a fresh-context agent for this audit.

The reviews checked normalization, global finite-feature-time existence,
positive readout acceleration, convexity through possible zero
crossings, the explicit small-readout constants, the physical clock,
action and endpoint estimates, Gaussian initialization, lower-layer
second moments, and backward energy.

These verdicts certify the stated finite-width theorem only. They do
not certify the requested infinite-width theorem, which remains open
in this investigation.

## Exact GD

Initial complete candidate: /tmp/l3_exact_gd_coercivity_candidate.md.
SHA-256: 5eb4ef05b73858072ff8fbc412ed219a28deb2b3c59e6198eaa4265239b70de0.

Two independent reviewers, l3_coercivity_blind_audit_one and
l3_blind_algebra_audit, each returned PASS without a substantive repair.
They checked the candidate only, independently of each other.

The canonical rewrite EXACT_GD_COERCIVITY.md adds a self-contained
Gaussian initialization corollary and a closed expression for the width
threshold. Its SHA-256 is
fcac71917f0a0c60c4368d7c86167aae0689ae87778622ab8745ac213fa9c35c.
The same two reviewers independently read the complete current file and
returned PASS for every stated finite-width claim, including the new
corollary, threshold, and simultaneous all-iteration probability statement.
These final reviews were not fresh-context audits, but neither received
the other's verdict or other current research notes.

## Sign symmetry

l3_blind_check_one reviewed GAUGE_MEAN_REDUCTION.md alone, treating the
application's stated norm and horizon bounds as premises. The reviewer
requested that the generic concentration conclusion explicitly require a
high-probability invariant event. That qualification was added.
The reviewer then returned PASS for the revised lemma.
Final SHA-256:
ee87d4c9ed2c086244aa7cbb964e54bd360d8d5bffbbf00fb3e9d5a3f07ea007.

No reviewer has approved the requested all-finite-time three-layer
mean-field/gradient-flow theorem. It remains unresolved.

## New local population theorem

The current seven-file proof has the following hashes:

| File | SHA-256 |
| --- | --- |
| /tmp/L3_FIXED_MESH_SOURCE_IDENTIFICATION.md | ba5cd7a52674a2031bf18ccb633bbb6eeeadd8f2a207369b38695d66ec40c03a |
| LOCAL_THEOREM.md | 3182e140122332bb26621ae382f6b1baebf7aaea4b6de2791d8e8b8c94e3af9b |
| LOCAL_RESPONSE_BOOTSTRAP_AUDIT.md | 2a999c88df03e0344fe53f58c9d73e8ae4c6b4b79a860b531700060444fdbf47 |
| LOCAL_ACTION_SPACE_AND_FLOW.md | a61dda52b01e6f44c2bc5cb345d442e84ff6a7dd0de30bc709aa85bf18490482 |
| LOCAL_CUTOFF_BRIDGE.md | a872fb412273ad4674c4d53729a36dc7a81f1c6e6bd471bb80d7ee613f018960 |
| LOCAL_GRADIENT_STRUCTURE.md | aeeee314cda7ba82f24293afcd3af03abc13788bd5131109624f2d01b911ab13 |
| LOCAL_FEATURE_LEARNING.md | 4bf2940f3abeacbd49ff28f137a3882ff5db5bb85a10f57f374b518748e423a2 |

Scope: the explicit positive local interval \(T_0\), not every fixed
finite time. The source theorem discharges the scalar bootstrap's
representation premise; the action construction identifies those
laws on common spaces; the uniform tail estimate discharges the
cutoff comparison's premise. The resulting local theorem is
unconditional for the prescribed Gaussian network and exact GD.

Individual checks:

- l3_blind_algebra_audit independently passed the full fixed-mesh
  source theorem, then the coefficientwise local bootstrap.
- l3_coercivity_blind_audit_one independently passed the common
  action-space/fixed-clipping theorem and the full gradient note,
  also inspecting the comparison and tail arguments needed for
  uniqueness and restartability.

Combined checks, independently of one another:

- l3_blind_check_one read all seven files. It requested explicit
  raw-coordinate/physical-clock uniqueness and a convention for
  GD derivatives at mesh endpoints. Both were inserted. The
  reviewer then passed the complete assembled local theorem,
  including the kernel and affine-regression additions.
- l3_blind_check_two read all seven revised files and returned PASS
  for the entire local theorem without further corrections.

These reviewers were instructed to use only the supplied proofs
as mathematical input and received no other reviewer's verdict.
They had earlier worked on unrelated finite-width notes in this
task, so these were not fresh-context audits.

For an additional genuinely isolated review, the seven files were
concatenated into L3_LOCAL_COMPLETE_PROOF.md, with review-status
prose removed and the full lemma texts retained. Its hash is
f97148f84979ab5b8489927d477b6abb3d919e27fd457455f2e3b98416725de4.
The new agent l3_local_fresh_audit was spawned with no conversation
history and given only that complete candidate. It read the entire
document and returned PASS, with no material gap, for the explicit
local \(T_0\) theorem. It specifically checked the conditioning,
singular covariances, uniform bootstrap, cutoff comparison, exact
raw-GD interpolation, common actions, gradient, and path/velocity
claims. A second fresh-agent spawn was unavailable because the
agent thread limit had been reached.

No local PASS is being promoted to an all-finite-time PASS.

## Continuation reductions after the completed local theorem

These are separate lemmas and scope checks, not a completed global proof.
The independent checks below were performed by existing agents; they
were not new fresh-context audits. No agent was told to accept a result
because another reviewer had accepted it.

| File | SHA-256 |
| --- | --- |
| PRUNED_GAUSSIAN_SUBSET_BOUND.md | 383a12f3c5b459ec54927788a710fbea9e4d11b95ef83b0413c53dc5b2099787 |
| ENDPOINT_RESTART_REDUCTION.md | 26ed125b0aa5e93785db9007cd198897bf0ed0aeb445f8be15373d37e0b22bed |
| TOP_COUPLED_LOCALIZATION.md | 6ff9ef87b9f83053b9c6c876c516c2da12636c3668e63333674e1f34861dad82 |
| DELETED_QUERY_RESPONSE_AND_ENTROPY_AUDIT.md | 8b80cdb09a11bf53555d70f426ea06ca8db288a377b7a09ac728dcd0da3eaf66 |
| COVARIANCE_RESPONSE_INCREMENT_REDUCTION.md | d1e29b659c5fd7850736680ff686a8b45c1233656ba57729befd39675c2ce7cd |
| INVERSE_MIDDLE_METRIC_AUDIT.md | aa7f6438cbe615eb9675c33d5e907688a0d2a76bfa9dbb3af1f74f32808cd053 |
| GRADIENT_ACTION_VARIATIONAL_SCOPE.md | 9a72a55b0e6659844e39fc945ceb81b3fc1a7e9339c6b99f560535b1fb41b5f1 |
| STOCHASTIC_TAYLOR_UNIVERSALITY_APPLICABILITY.md | a0efcb883fe23423801e5854b2b97cc85fa6b6552f5a200c8ebf0954010135e7 |

l3_local_fresh_audit independently checked the entire fully pruned
Gaussian-subset proof and returned PASS. In particular it verified
deleted-column independence before norm conditioning, the common
polynomial bounds, the all-subset/time union bound, and postselection
validity. This review approves no full/pruned stability statement.
The same reviewer separately passed the appended extension to each
prescribed clipping level, with constants independent of that level.
It correctly does not claim one finite-width event simultaneous over
all real-valued clipping levels.

l3_endpoint_continuation independently checked TOP_COUPLED_LOCALIZATION.md
and returned PASS for its exact identities, comparison constants, and
limited independence claim. l3_local_fresh_audit also checked these
supporting calculations while reviewing the later entropy note.

l3_local_fresh_audit independently checked ENDPOINT_RESTART_REDUCTION.md
and DELETED_QUERY_RESPONSE_AND_ENTROPY_AUDIT.md and returned PASS. The
Osgood comparison is a valid theorem with an explicit uniform-envelope
premise; the Gaussian trace/directional response and pruning criteria
are valid sufficient reductions with unproved canonical premises.
The counterexamples in those notes concern only general inferences,
not the canonical three-layer network.

l3_gradient_uniqueness independently checked the final, complete
COVARIANCE_RESPONSE_INCREMENT_REDUCTION.md, including its added
supremum-time Gaussian estimates, and returned PASS. It verified
source measurability on the original generated spaces, consistency,
the Gaussian isometric extensions, adjoint identification, degenerate
covariance inequalities, learned-memory scaling, and mesh/clipping
uniformity. The transported-adjoint tail and tangent covariance are
not controlled by that result.

The root agent separately checked the full inverse-middle metric
identities and the gradient/action variational scope example. Their
conclusions are limitations of particular attempted estimates, not
negative theorems about the target.

The additional primary-source applicability note is an author-checked
hypothesis audit, not an independently certified theorem application.
It does not supply a global bridge. The all-finite-time canonical
MF/GF theorem remains unresolved.

## Canonical rare geometry and actual tangent responses

The following later lemmas address the canonical Gaussian lower
geometry and actual, rather than frozen-bulk, response. They still
do not form a complete global-continuation proof.

| File | SHA-256 |
| --- | --- |
| PRUNED_RARE_BLOCK_GEOMETRY.md | 71316052df34a348164ba02addd5478a4ecdd9bf5f26649535f2c047307d7c99 |
| ADAPTIVE_RARE_SELF_BLOCK_MODULUS.md | 3356d7f4063090dc79f7a856c0492ced304092c447b4996f258fb15c6d826db1 |
| DIRECT_SCALAR_PRUNED_REDUCTION.md | 31f84ed356d9f26eff58d2ca4b9f596c07ad1e265b3b825b6c5b3fd8feec3e39 |
| ACTUAL_BULK_GAUSSIAN_TANGENT_ENERGY.md | ce800c6f86550319b138bd8a1387f69a2f8a91cca5e0a20586d2aed2aeeebffe |
| TIME_ORDERED_PROBE_AND_SELF_RETURN_AUDIT.md | 2e9719c23de96d6c02a938c0bafbc18f0a13c55f7c9de646e50341efb212fb8a |
| ACTUAL_TWO_TIME_RARE_RETURN.md | 5107747cabffdd2f2e4be2775d151944a5484aa7ce49f4d840b20861c8000dce |

l3_local_fresh_audit independently passed the full pruned rare
geometry lemma: independence of both unused Gaussian blocks, signed
weighted-Gram concentration, subset/time uniformity, the scalar lower
bound 1/4, and the top diagonal derivative bound.

l3_endpoint_continuation independently passed the adaptive rare
self-block lemma: all-submatrix event, arbitrary adaptive signed
diagonals, level-set integration, actual/reference matrix expansion,
and the modulus at every state distance.

l3_local_fresh_audit independently passed the direct scalar/pruned
note, including the saturating displacement estimate, both exact
rank-memory identities, all coefficient-derivative terms, and the
conditional Gaussian path-supremum union bound.

l3_gradient_uniqueness independently checked the actual tangent
energy note and passed its equations, 1/n forcing, mixed covariance
energy, normalized-HS bridge, and stated integrability qualifications.
It requested an explicit distinction between ordinary Euclidean
vector norms and normalized vector norms in equation (9). The final
hashed file includes that clarification. It does not prove its
additional response moment inequality.

l3_local_fresh_audit independently checked the time-ordered and
initial self-return note. It requested that Gaussian integration
by parts require justified derivative expectations or retained cutoff
boundary terms, rather than mere integrability of the functional.
That correction was made and the reviewer confirmed PASS. The
initial conditional self-site sign is not a finite-time sign bound;
the localized Taylor coefficient is not a finite-time counterexample.

The separate short CANONICAL_PROBE_INITIAL_SELF_RETURN.md repeats the
initial-jet calculation for readability; the reviewed primary source
for this claim is the full time-ordered note listed above.

The two-time rare-return note is also checked directly by the root:
its operator estimate uses the bounded propagator and exact T_s R_t
composition, not a derivative of the activation gate in operator norm.
Its positive conclusion is about the symmetric part of the compressed
kernel. l3_gradient_uniqueness then independently read the complete
final note and returned PASS, including the added corollary for
disjoint rare supports using their jointly pruned union. It verified
the cross-time expansion, all-set/time probability scope, symmetric-part
coercivity, and the precise jointly pruned distance in that corollary.

These checks do not control rare-to-large-bulk transport, the actual
off-block residual, or the all-time mixed-response energy. None is
an all-finite-time theorem PASS.

## Single-pruned residual control and sharpened accumulated forcing

These new lemmas supersede only the earlier lack of a quantitative
off-block-residual estimate. They do not supersede the open status
of full-state stability or the all-finite-time target.

| File | SHA-256 |
| --- | --- |
| SINGLE_PRUNED_OFFBLOCK_OSGOOD.md | 0f907e82e212813ac3f97818b0fbd3db652ac1310b8629365b456b6cb68256c3 |
| SHARP_RARE_ACCUMULATED_FORCING.md | 3e5d7ad08462dc3161e195285b498ec4dac6d0e1627da15942c5593afe92cd63 |
| ACTUAL_PROBE_LEVERAGE_LOCALIZATION.md | 9518db9ad030d15d11ee792e42e8107a4fb865187f9611a2f2539abf363ddd96 |

l3_local_fresh_audit independently reconstructed the entire single-
pruned proof and returned PASS. It checked active-data conditioning
before the full norm event, all-set/time concentration, the sorted-
coordinate block inequality including its endpoints, the squared
adaptive-gate bound, and the exact actual residual decomposition.
The root requested an explicit ZERO-readout scope statement, which
the author added at a coordinated safe point. The reviewer approved
the final revised scope: this is a proxy lemma, not a global
transfer to the prescribed tiny Gaussian readout.

l3_gradient_uniqueness independently read the entire sharpened
accumulated-forcing proof authored by the root and returned PASS.
It checked the unused pruned transpose query, the necessary square-
root deletion term in the top comparison, the coordinatewise time
supremum, the elementary cubic inequality, ordinary Frobenius
scaling of the rank update, and probability allocation. In
particular the displayed logarithm with factor 30 dominates all
three allocated events. No edits were required.

The root read and checked the entire actual probe-leverage note.
Its conditional covariance estimates, small-support counting bound,
and integrated response estimate are elementary consequences of
the previously audited bounded maps and actual probe equation.
This is a root audit, not an additional independent-agent PASS.
The exceptional signed covariance is explicitly NOT bounded.

These reviews used existing agents, not new isolated fresh-context
agents. They approve their stated lemmas only. The full canonical
all-finite-time theorem remains unresolved and has no PASS.

## Moving-range response and active-primitive scope

| File | SHA-256 |
| --- | --- |
| ACTUAL_MOVING_RANGE_PROBE_NORMAL_FORM.md | 3fe2d0a2e3926ffa65fd6891a4631b809c7d346e5eae2cf967274a38c6d147a3 |
| ACTIVE_GATE_PRIMITIVE_AUDIT.md | 485853c417cababa0b7535dc2baba664e139d4d52fca75773f20da36a86598f1 |
| RECENT_CAVITY_THEOREM_SCOPE.md | f53181d23da03bc74cce1d7ad26f051711e0a89afb318c36cda8c30a1a67375c |

l3_local_fresh_audit independently reconstructed the complete moving-
range note and returned PASS for its limited claims. It checked the
coercivity premise from the actual readout theorem, including the
prescribed tiny-readout event, while keeping coordinate-readout bounds
as a separate stated premise. It verified all adjoints and moving-
projection derivatives, the ordinary-Euclidean-probe operator scale
1/n, the resulting controlled exceptional source and covariance, the
learned-rank identity, the ordered noncommuting factors in the equal-
time return, and past-time kernel differentiation without a derivative
of T_s. The root also read and checked the complete file.

This is an actual response estimate: one previously unbounded
exceptional component is controlled. It does not control subsequent
amplification through the range or its recycled memory. The remaining
signed covariance terms are retained explicitly.

The root read and checked ACTIVE_GATE_PRIMITIVE_AUDIT.md. Its exact
integration-by-parts and characteristic/rank identities do not bound
the active primitive. This is a recorded stalled route with preserved
algebra, not a negative theorem about the canonical network.

The recent-cavity note is a root primary-source applicability check
of the 2026 Dandi--Gamarnik--Pernice--Zdeborova theorem. Fixed iteration
counts and globally Lipschitz row maps do not supply the missing
unclipped continuous-time estimate. No complete external theorem
application is claimed.

## Actual rare derivative, nonnegative energy, and whole-path control

| File | SHA-256 |
| --- | --- |
| ACTUAL_RARE_BACKWARD_DERIVATIVE.md | e402abc3c591fb029bf82d6e7b97bc533003e79104aab1b6c4837b13ed040be8 |
| RARE_BACKWARD_ENERGY.md | 32675e45b51502fbc56ae69b15c840129a322115d12c5ec44fd11302e1fd645b |

l3_local_fresh_audit independently reconstructed the entire rare
derivative proof and returned PASS. It verified all exact top and
bulk telescoping terms, the nonindependent rare self-return, each
of the four genuinely independent coefficient families, the distinct
active-data events for top and incoming queries, and the all-set/time
probability allocations. The finite-width second derivatives need
only the a.e. first derivative of a prescribed Lipschitz clipping.
The root read and checked the complete derivative proof.

l3_endpoint_continuation independently checked the energy proof
(1)--(9) and its full derivative dependency and returned PASS.
The root subsequently added the whole-coordinate-path corollary (10).
l3_local_fresh_audit then independently read the complete updated
energy file at the hash above and returned PASS. This check included
the clipped pairing with tau(q), the zero initial boundary, Young
absorption of the actual self-feedback, Euclidean normalization,
and the coordinatewise time supremum inside the empirical sum.
The corollary requires no new probability event.

These are existing-agent independent reviews, not fresh-context
reviews of a completed global theorem. Their approved scope is the
zero-readout full/pruned proxy, uncut or with the same prescribed
clipping. All bounds retain the full/pruned distance. No global
tiny-readout transfer, full-state closure, or all-finite-time theorem
has been certified.

## Actual weighted gate bound and the diagnostic hierarchy

| File | SHA-256 |
| --- | --- |
| ACTUAL_WEIGHTED_GATE_HARDY_BOUND.md | 73b5f44b4fc6796ab08078e2d845d20fc51378107a48bc0233ef81d08359ce41 |
| RARE_HARDY_HIERARCHY_COUNTEREXAMPLE.md | ba4d53b5844cc228b0058b4250e27d7ea0191adbb8893268e4ab3267a31e7800 |

l3_local_fresh_audit independently read the complete actual weighted-
gate proof and returned PASS. The root also read and checked it.
The review verified the prefix-time path estimate, discrete subset
floor, layer-cake identity, width factor min(1,na), common clipping,
and the squared-state comparison with its square root and nested
history intact. The leading logarithmic term has the claimed Osgood
size. The remaining Hardy average is not claimed to close.

The root independently read and verified the entire diagnostic
counterexample. In particular the exact constant identity
300^(3/2)/sqrt(12)=1500 makes its square-root lower bound equal the
flat-profile derivative. The same uniformly bounded, initially zero
family satisfies both displayed schematic inequalities on all
positive times but has a positive small-size limit.
This is a counterexample to those inequalities implying continuity,
not a canonical-network trajectory. A bridge to the exact discrete
floor in the actual hierarchy is recorded below.

## Exact finite-floor hierarchy obstruction

| File | SHA-256 |
| --- | --- |
| FINITE_FLOOR_HARDY_HIERARCHY_COUNTEREXAMPLE.md | ac079950b4cb061736400645d0efc647e3222e924633a4cf8191ae9e3e4698bc |

l3_local_fresh_audit independently verified the entire finite-floor
counterexample and returned PASS. The root also read and checked
the full file. The reviewer checked both floor regimes, the exact
Phi function and current-time cutoff, the constant Lambda=1800,
zero initial values and derivatives, and the order of limits.
The family satisfies the actual scalar inequality (19) with
C=1 and zero width error. The optional slow-clock and delayed-start
extensions were also checked.

This upgrades the previous continuum diagnostic to a genuine
obstruction to closure from the DERIVED SCALAR INEQUALITY alone.
Finite floors, smaller positive constants, and a preceding interval
of zero limiting error do not restore that implication. It remains
strictly a counterexample to a sufficient-proof route: none of the
artificial error profiles is claimed to solve the canonical state
equations or their retained signed identities.

## Actual signed range characteristic

| File | SHA-256 |
| --- | --- |
| ACTUAL_SIGNED_RANGE_INTEGRATING_FACTOR.md | 4c10c2cc562c387469c9da260e008a4e485ccd4e6af886b88a5ba1b3821a45b0 |

l3_local_fresh_audit independently read the complete note and
returned PASS; the root also read and checked it. The review
verified the actual scalar cancellation, all retained off-block
and recycled-memory terms, weighted-energy normalization, the
conditional majorant, and the primal-action implications.
The bounded response/history maps were distinguished from the
additive b T w0 source, which uses its own probe covariance bound.

The coordinate set is fixed in time and independent of the
realized auxiliary probe, although it may be selected from the
actual trajectory and its conditional covariance. The range
algebra concerns the uncut finite flow; the action consequences
retain the zero-readout scope of their sources. Neither a
weighted source bound nor an action–response covariance bound
was proved in the original version. The revised hash includes only
narrowing cross-references to the subsequently proved pure-top and
weighted-additive-source result below; the reviewer checked those
updates. This remains an audited exact identity/reduction, not
an upgraded global-response or continuation theorem.

## Pure-top source and full-backprop primitive response

| File | SHA-256 |
| --- | --- |
| ACTUAL_WEIGHTED_ADDITIVE_PROBE_SOURCE.md | 4da8640a8b40ccb22f835762413f1f2a9e11a6d067e54b998156d342fb0ba5f4 |
| ACTUAL_BACKPROP_PRIMITIVE_RESPONSE.md | 067e1bc7d38c7409dab9639f29f84543abd2d0b7a9b9d543f9a47a6747e54d1e |

The root read both complete proofs. l3_local_fresh_audit independently
reconstructed the pure-top invariance, exact zero lower response and
curvature covariance, weighted additive source, and autonomous lower
normal dynamics, and returned full PASS. This is an existing-agent
review, not a fresh-context review of the full theorem.

The root authored the full-backprop primitive note. l3_primitive_fresh
was spawned with fork_turns:none, shown only the candidate proof and
its cited dependencies, and returned complete proof-only PASS for
equations (1)--(20). The root then added the C1 clipping extension.
The same isolated reviewer checked the revised complete statement,
the actual clipping definition in LOCAL_CUTOFF_BRIDGE.md, and every
replacement and uniformity claim in (21)--(23), again returning PASS.
The final hash above includes that audited extension.

The check includes the PLUS sign in the integration-by-parts memory,
the exact diagonal-time kernel, all Gaussian probe normalizations,
pure-top source invariance, and absence of an inverse gate on the
response-dependent ordinary source. The extension uses tau' only;
no second clipping derivative or clipped coercivity is assumed.
Uniformity concerns the bounded representation maps and source bound,
NOT a uniform bound on the response amplitude. The remaining signed
residual/returned-response covariance is explicit and uncontrolled.

## Actual logarithmic network comparison

| File | SHA-256 |
| --- | --- |
| LOGARITHMIC_NETWORK_COMPARISON.md | adc98d1f9fe2c23560afc649e9107e2125a87aca1c94ee5db9a4f43e7034f480 |

The root read the complete note and checked its equations.
l3_local_fresh_audit independently reconstructed the exact row-log
identity, rank bound 6n, nuclear bound Cn, log-determinant derivative,
two-sided singular distortion, full Gaussian seed and trained-increment
determinants, and the actual full/pruned mean-value source; full PASS.
The prescribed smooth-clipping extension was included in the review.

The normalization distinguishes the nonzero full initial matrix seed
from the zero-initial trained increment. No response trace bound is
inferred from either determinant. The exact nonlocal weighted row
pair and the pruning-source/propagator alignment remain unestimated.
This is another scoped lemma audit, not certification of the requested
global population theorem.

## Off-diagonal primitive identity

| File | SHA-256 |
| --- | --- |
| ACTUAL_PRIMITIVE_OFFDIAGONAL_PAIR.md | f7f1b24a4f53cacdf0f86258eafb9b4ae86473b894d70fc9346af0726697df04 |

The root derived and wrote this note. l3_pair_identity_fresh was
spawned with fork_turns:none and shown only the proof and its cited
primitive dependency. It independently checked every normalization,
the clipped split-free equation, the symmetrized and polarized sums,
exact cancellation of all i=j terms, and the signed PSD example.
It requested a precision fix: the original broad trace-bound wording
had to distinguish finite-width coefficient-dependent bounds from
the unproved width-uniform response-closing bound. The root applied
that fix and the two suggested notation definitions. The isolated
reviewer reread the revised file at the hash above and returned PASS.

This certifies an exact identity, not a favorable sign or a closed
response estimate. The PSD example tests only an algebraic implication;
it is not claimed to be a canonical Gaussian-network trajectory.

## Joint input/query energy test

| File | SHA-256 |
| --- | --- |
| JOINT_MIDDLE_QUERY_ENERGY_AUDIT.md | 2052f2e13249c4876e5045dda1ab035e24c11e6d28f34fede5dea615e2ad45a5 |

The root read and checked the entire note. The author's independent
helper l3_gradient_uniqueness/joint_top_middle_audit derived the tangent
cancellation and independently passed complete finite-pair sections
3--4, including the nine remainder terms, rank-two interpolation,
pruned mobility, small-L1 input bound, and exact joint-energy equality.
This is a scoped helper audit, not a fresh-context audit of the global
theorem. The mixed trained-top product and original mobility-feedback
term remain. Keeping the corrected query algebraic avoids the new
product but supplies no new lower feedback estimate.

## Time-derivative and Gaussian-averaging scope audit

| File | SHA-256 |
| --- | --- |
| TIME_ANALYTICITY_DERIVATIVE_AUDIT.md | 81a570015e8aec4cb0810dc75ec3d68764e8a54633ce7af5f8c7a7844bed9e98 |

The root independently derived the general fifth-derivative jet and
checked the complete explicit matrix construction and scalar coefficient
argument. It then read the full frozen note. l3_time_analyticity_fresh
was spawned with fork_turns:none, shown only this self-contained proof,
and returned full PASS at the hash above. The reviewer checked every
trained block, the normalized gradient metric, the exact coefficient
-9(pi/4)^7/16, Gaussian full-support scope, bounded rational derivatives,
differentiation under expectation, and zero Taylor radius at zero.

The network example refutes only a deterministic width-uniform fifth-
derivative bound throughout the entire primal-norm event. Its Gaussian
neighborhood probabilities are not bounded below uniformly in width.
The scalar example is not an identified network observable and says
nothing about nonanalyticity at positive times. Neither is a negative
theorem about canonical typical-Gaussian continuation.

## Actual second log-gate integration

| File | SHA-256 |
| --- | --- |
| ACTUAL_LOG_GATE_SECOND_IBP.md | cd162a86090a6ef025bededd06b0cb723368006befeba2939bfe23a094fe4210 |

The root derived the log-amplitude tail and suggested the absolute
log-gate choice, proving the uniform inverse by SPD similarity. It
then read and checked the entire author's frozen note.
l3_log_gate_fresh was spawned with fork_turns:none, shown only the
candidate and permitted its cited dependencies, and returned full
PASS. The reviewer checked the amplitude/variation distinction,
all matrix ordering and signs, the inverse under UNCLIPPED coercivity,
the exact diagonal commutator, the Gaussian coefficient claim versus
the value of the commutator, and the lower-gate term in the mobility
derivative. No fixes were needed.

The new inverse bound is unconditional on the explicitly stated
uncut primal/coercivity event. No clipped coercivity is inferred.
Neither that inverse nor the exponential log-amplitude tail bounds
the retained ordered, mobility, residual, or transformed-source
response terms. This is not a negative theorem about the network.

## Finite nonlinear primitive, correct commutator metric, and full Gaussian pair

| File | SHA-256 |
| --- | --- |
| FINITE_PRUNED_BACKPROP_PRIMITIVE.md | 4ed5dfe0d63ed1108dff35841cb603523f06e2c34f806face02fe1d42602cc5a |
| ACTUAL_LOG_GATE_COVARIANCE_COMMUTATOR.md | 5770d934df3840184d0b19bc3a15eae82290cc879201fe862786ba56d24c6c76 |
| ACTUAL_FULL_PAIR_GAUSSIAN_IBP.md | 73a855fcd5dbb63dcdb5ed4e8bc60eba6f0274b21962ff88417166a169148efd |

The root authored and checked the finite-pair primitive note.
l3_finite_primitive_fresh was spawned with fork_turns:none and shown
only the candidate and its cited dependencies. It reconstructed the
full nonlinear average-product equations, the retained quadratic
finite-pair memory term, the plus-memory sign, and the exact arctan
divided-difference characteristic. The root added the precise rare
Gaussian-source dependency and rho=0 convention requested for a
self-contained use of that bound. The final version passed. Common
merely Lipschitz clipping requires no clipping derivative or coercivity.
The two signed energy terms remain unestimated.

The root read and checked the entire log-metric note.
l3_commutator_metric_fresh, spawned with fork_turns:none and shown
only the proof and permitted dependencies, returned PASS with no fixes.
It checked the ordinary trace normalization, C-skew commutator, double
commutator sign, positive corrected-response metric, complete energy
derivative, every C' term, actual covariance jet, and symmetry scope.
The cancellation is real; the remaining symmetric/source energy is
not bounded. No clipped-coercivity or tiny-readout jet is inferred.

The root read and checked the entire full-pair IBP note.
l3_pair_ibp_fresh_audit, spawned with fork_turns:none and shown only
the proof and permitted dependencies, returned PASS with no fixes.
It reconstructed the Gaussian localization, all n factors, both
orientation sums, learned-increment derivatives, lower-Gaussian IBP,
and the positive n=2 t^5 coefficient. The example establishes only
localized nonvanishing of a mixed sector, not an unlocalized sign or
failure of a uniform bound. Smoothness is needed for this calculation;
no merely C1 clipping extension is claimed.

These are three scoped lemma audits. They do not certify the complete
all-finite-time population theorem, which remains unproved and unrefuted.

## Two additional primary-source scope checks

| File | SHA-256 |
| --- | --- |
| RESNET_DMFT_PRIMARY_SCOPE.md | 2509a7bb5922efe5b789268ca74527e33d62b0731d8c43467a899b74ec5f0d74 |
| ORTHOGONAL_SK_PRIMARY_SCOPE.md | 5a03cc54e7d469e184dd47ebd13b494991c1f19b16abeebd8ca8058fd4db3a86 |

l3_resnet_source_scope inspected the primary slides and relevant PDF
statements/proofs of Chaintron--Chizat--Maass. The root read the complete
scope note and independently checked the PDF's Theorems 1.1 and 2.5 and
Lemma 5.10, plus the primary HTML's architecture and analogous product
calculation. The note pins PDF page references because its HTML rendering
differs in displayed date/numbering. Finite training-step scope and the
required conditional moments prevent direct invocation here. The large-D
part itself is unclipped, and trainable embeddings are discussed; those
are not used as blanket exclusions.

The root checked Assumptions 2.1--2.2 and Theorem 2.4 of Fan et al. against
the primary HTML. The fixed scalar nonlinearity plus fixed linear disorder
does not match this trained composition; zero noise is explicitly allowed.

These are limited applicability checks, not complete paper audits or
proof-only theorem certifications. No external theorem is invoked to close
the canonical global-continuation gap.

## Actual Gaussian-divergence and reference-law scope

| File | SHA-256 |
| --- | --- |
| ACTUAL_GAUSSIAN_DIVERGENCE_SCOPE.md | 024d8fc5097a35c5556d98b1956abfa06f130fee256d696af5475c896ebacd01 |

The root proposed the density-route test and the time-broadened-reference
refinement, then read and independently checked the entire proof.
l3_density_fresh_audit was spawned with fork_turns:none and shown only
the proof and its explicit mathematical dependencies. It reconstructed
all equations (1)--(24), the full trained-block trace, Gaussian whitening,
expectation bounds, actual tiny-readout small-time growth, physical clock,
both broadened references, and the projection/smoothing distinctions.

The reviewer requested two precision fixes: replace a claim about
disjoint supports by the actual mutual-singularity measure statement,
and specify fixed small positive time for the quoted smoothing scale.
The root applied both; the reviewer reread the final file at the hash
above and returned full PASS. It explicitly checked that physical
backward completeness is not needed for change of variables on the
forward image.

This certifies an actual-network obstruction to the proposed full-state
Gaussian likelihood shortcut. It does not bound a compressed-query
likelihood, rule out a projected distributional argument, or establish
either the canonical global theorem or a counterexample to it.

## Actual hidden density and every-plane intrinsic volume

| File | SHA-256 |
| --- | --- |
| ACTUAL_PROJECTED_DENSITY.md | e41b9a5a5239172b40b9cfb2f5b40d4a975c98f19dae618ea207972aa379e9cd |
| ACTUAL_HIDDEN_GRAPH_VOLUME.md | 7b70789e567d8c17d0f6ad1c7b4ab703fc9d0ed385863bf38bb8f81b80eeff7e |

The root developed the canonical analytic-nondegeneracy argument and
read and checked the complete projected-density proof. The reviewer
l3_projected_fresh_audit was spawned with fork_turns:none and received
only the candidate proof and its explicit dependencies. It checked
normalization, entropy finiteness and signs, weak conditional moment
laws, the covariance flux, physical time, the analytic critical-set
argument, local inverses, branchwise response equations, and area/coarea.
The root also read the required analytic-dependence theorem in Teschl's
author-hosted text and all of Mityagin's four-page zero-set proof.

The fresh reviewer requested that a generic fold/noninjectivity claim
be completed or narrowed. The revised bounded-feature example uses
single strict-sign smooth bumps, an even cutoff, and an explicit
symmetry/intermediate-value proof of global hidden noninjectivity.
The opening now states only the demonstrated branchwise limitation,
not a canonical-mixture entropy sign. A strictly positive lower bound
on the absolute projected determinant is the ruled-out generic claim.
The reviewer checked the final file at the hash above and returned PASS.

The root authored and independently checked the raw-Hessian/graph-volume
note. l3_graph_volume_fresh was spawned with fork_turns:none and given
only the proof and explicit dependencies. It checked all trained-block
second variations, the RMS-only nuclear bound, arbitrary transported
tangent volumes, Gaussian expectations, the physical rank-one term,
the exact projection determinant, and the branchwise Riccati equation.
Its sole observation was to specify that projection lacks a volume
LOWER bound: the upper bound follows from the already proved intrinsic
bound. The root corrected that wording, and the reviewer confirmed
final-hash PASS above.

These reviews certify only the stated density identities, qualitative
absolute continuity, intrinsic-volume estimate, and explicit structural
example. No canonical projection-angle estimate, O(n) hidden entropy,
adaptive-query control, or full global theorem is certified.

## Deterministic angle test and scalar-readout positive theorem

| File | SHA-256 |
| --- | --- |
| PROJECTED_ANGLE_STRUCTURAL_COUNTEREXAMPLE.md | 62467a4467817ff2c6583e663b7b0735ebc650a21a09acb3abcff46dd809722d |
| SCALAR_READOUT_PROJECTION_THEOREM.md | 365b73f71843bf64bde13166ca56845653003b0519ae6cbe5dd49d0ca62680a1 |

The root proposed the bounded-J/nuclear-action test, then read and
independently checked the complete counterexample. l3_angle_fresh_audit
was spawned with fork_turns:none and read only the candidate. It checked
the tangent and transported-frame equations, all phase transfers, the
exact autonomous realization, positivity of both projected tangent
blocks throughout [0,4], the fixed nuclear action, global existence,
and the analytic Gaussian-mollification refinement with uniform
constants. It returned PASS without fixes and separately confirmed the
hash above. Invertibility is proved at every time in the stated horizon,
not asserted for every future time in the analytic examples.

The counterexample has bounded analytic vector features and bounded
first derivatives, fixed dimensions d=m=2, bounded reference states,
and bounded integral nuclear Hessian action, but arbitrarily large
time-integrated projection-angle loss. It is not the canonical arctan
network and gives no canonical Gaussian-average or entropy lower bound.
It exhausts only that proposed deterministic norm-only implication.

The root checked the scalar gradient-orbit argument, contributed to
the quantitative entropy and fixed-physical-time tests, and read the
entire resulting note. The root then added and independently derived
the actual n>=2 output-gradient noncommutation calculation.
l3_scalar_projection_fresh_audit was spawned with fork_turns:none,
shown only the final candidate, and returned full PASS at the hash above
without corrections. It verified completeness without bounded
derivatives, global orbit maps, all critical cases, determinant bounds,
both feature-time directions, the separate zero-readout physical proof,
actual n=1 polynomial estimates, entropy integrability and mixing, and
the fixed-pair analytic noncommutation consequence.

The positive projection theorem is scalar-readout only. Canonical n=1
has feature-time coverage for its Gaussian scalar readout; the physical
part covers zero readout, not the canonical nonzero width-one Gaussian
readout. For n>=2 only noncommutation is proved, not a projected
singularity or a lower bound on commutator size. These audits do not
upgrade the requested all-width all-finite-time MF/GF theorem.

## Complete material Hessian and the scalar-Schwarzian test

| File | SHA-256 |
| --- | --- |
| ACTUAL_SCHWARZIAN_MATERIAL_HESSIAN.md | 41086c4aa7d2f9432cfcac91b45485713ee292d6fcf7ef11588177c42b1a10ac |

The root proposed the signed-Hessian test and supplied the explicit
canonical bounded-state family, then independently checked the full
material derivative and both exact quadratic evaluations. The root
derived and appended the physical-time extension, retaining the
residual rank-one correction and both clock factors.

l3_schwarzian_fresh_audit was spawned with fork_turns:none and read
only the candidate and its explicit ACTUAL_HIDDEN_GRAPH_VOLUME.md
dependency. It checked all raw-coordinate scalings, every trained
matrix/readout derivative, the exact positive and negative quotients,
uniform bounds on B, and the full physical derivative and norm values.
It returned final full-file PASS at the hash above without corrections.

The scope check was explicit: the f=0,c=1 witness cannot be reached at
positive feature or physical time from zero readout. Full Gaussian
support provides no high-probability or expectation contradiction.
The audit certifies failure of the proposed instantaneous bound on
the stated ambient primal-bounded class, not failure of a canonical
trajectory-specific estimate, global MF/GF convergence, or autonomy.

## Frozen Gaussian comparison: growing horizon and actual temporal scope

| File | SHA-256 |
| --- | --- |
| PANAHI_EULER_PERTURBATION_SIZE.md | 5c5b7a7fe40a670da99f3d188c7bbbba22b969ef1cecdeb21ac6027f7538809b |
| PANAHI_GAUSSIAN_COMPARISON_SCOPE.md | b1cd3f9f4f3e2ddd38e7a506fea613b71201786cdc8b6fb38a99328e6509366a |
| NISHIYAMA_IMAIZUMI_PRIMARY_SCOPE.md | 164bfada3dda1524ffab1bfb86cf8c8c870ace3aa0e4e4e3362dcfb14090ff89 |

The root read the primary Panahi setup, perturbation, matching mechanism,
and Theorem 2 assumptions. The source-scope agent additionally checked
the primary PDF and its fixed-query-count Appendix C argument. This is
an applicability inspection, not a full audit of that external paper.
The Nishiyama--Imaizumi note likewise records only its checked setup,
regularity assumptions, and noiseless-global theorem scope.

The new mathematical candidate was developed by the comparison agent,
with root contributions to the effective-rank optimization, Gaussian
maximum estimate, and complete appended canonical temporal calculation.
The root independently checked the entire final candidate.

l3_frozen_comparison_fresh_audit was spawned with fork_turns:none and
shown only the candidate and its explicit primary-source dependency.
It returned full scoped PASS at the exact hash above without corrections.
It checked all Gaussian isometries and normalizations, both triangular
orientations, repeated-query Cholesky formulas, floors and optimization,
integrated and raw maxima, rates, every canonical derivative, and the
distinction between frozen and adaptive histories.

This audit certifies a frozen-forcing theorem and its stated network
premise implication. It does not certify adaptive comparison, removal
of clipping, global state convergence, or autonomous unique restart.

## Two exact scope tests for the comparison route

| File | SHA-256 |
| --- | --- |
| PANAHI_CAUSAL_ADAPTATION_ISOMETRY_TEST.md | 1031c8fd75aba6ef2965fc0a624cffacbd150b31787cac493f26c9437dc441a6 |
| PANAHI_SMALL_JITTER_RANK_INFLATION.md | 16ef6bcbd50681f46c45d1399e0496c9d42baa87a37880bfefa8b220efc8a1be |

The root proposed an exact two-query causal test. The comparison agent
independently derived it and extended it to arbitrary width and fixed
physical horizon. The root checked the resulting note completely.
l3_causal_isometry_fresh_audit, spawned with fork_turns:none and shown
only that candidate and its primary source, returned full scoped PASS
at the recorded hash without corrections. The rank-one smooth causal
example has explicit nonzero centering and second-moment corrections;
these still vanish with width and do not refute an adaptive bound.

The root separately derived the small-jitter rank-inflation example
and wrote its complete elementary Gaussian proof. The independent
l3_jitter_rank_fresh_audit read only the candidate and its frozen-lemma
dependency. It passed every probabilistic and algebraic assertion but
correctly flagged an overbroad scope sentence in the initial hash:
very rapidly decaying sigma can restore temporal Lipschitz bounds.
The root corrected the sentence to distinguish the regularization
regimes, including an explicit adjacent-slope calculation. The reviewer
then rechecked the COMPLETE revised candidate and returned full scoped
PASS at the final hash above.

The jitter example proves that uniformly small sigma-scale query
changes can produce full effective rank and nonvanishing raw AND
integrated covariance perturbations when K=m^2. It is a frozen
algebraic example, not the actual canonical perturbed trajectory.
Neither scoped test settles the requested all-time MF/GF theorem.

## Adaptive Gram martingale: causal dependence handled directly

| File | SHA-256 |
| --- | --- |
| PANAHI_ADAPTIVE_GRAM_MARTINGALE.md | 6cec745dde896fa2932592b126f48488618cd426a45de1fa03598fd467bdb4b5 |

The root derived the exact two-half-step matrix representation, its
left/right variation bounds, both query decompositions and residuals,
and the stopped/truncated Freedman route. The comparison agent
independently checked the filtration and algebra, supplied the full
candidate with explicit constants and scope, and froze it.
The root read the complete candidate and checked Tropp's primary
Corollary 1.3, including every premise used here.

l3_adaptive_gram_fresh_audit was spawned with fork_turns:none and read
only the candidate and its cited primary Panahi/Tropp sources.
It returned full scoped PASS at the hash above without corrections.
The reviewer verified prefix Cholesky consistency, exact causality,
both noise identities, every martingale and moment assertion, stopping
before each potentially offending half-step, Gaussian-symmetric
truncation, both distinct variation bounds, Freedman constants and
hypotheses, and all remainder/maximal bounds.

Its certification explicitly concerns the intersection probability
P(rank event AND bad noise)<=alpha. The proof handles adaptation
under that rank premise; it does not prove the rank event has high
probability for the actual perturbed neural network, remove clipping
or regularization, or establish the all-time MF/GF theorem.

## Integrated initial-query compression

| File | SHA-256 |
| --- | --- |
| INTEGRATED_INITIAL_QUERY_COMPRESSION.md | 2c97e9fe8c4e9b3a66d7efdf80f825f8c7bb6275649518c47fc001aef6b57c73 |

The root proposed compressing the integrated lower backward argument;
the route agent derived the full integral skeleton and explicit
rank-memory continuity bounds. Before audit the root required a fully
finite self-contained setup and the user's canonical notation, with
ordinary transposes and every normalization explicit. The root then
read and checked the entire revised candidate.

l3_integrated_query_fresh_audit was spawned with fork_turns:none and
shown only the candidate and its specified derivative-bound dependency.
It returned full scoped PASS at the exact hash above, without changes.
It verified all triangular integrals, retained rank histories, both
orientations, all four derivative bounds, covering counts, and the
memory estimates including the factor two in the R^(1) estimate.

The audit also verified the limits of the inference: physical-time
causality is not finite-transcript measurability; bounded Lipschitz paths
need not be strongly compact; the primitive comparison retains the
middle multiplier; and uniform primitive convergence does not yield
derivative or first-kernel convergence. This is not a full global
canonical limit audit.

## Zero-readout-reachable material-Hessian counterexample

| File | SHA-256 |
| --- | --- |
| ACTUAL_ZERO_READOUT_REACHABLE_HESSIAN.md | 59b2bc2d3ee1fcfd3f4f118780b624986fc01aa4f2f7d7a8cea2eec18ca88b93 |

The root proposed the positive bulk channel and checked the full
resulting candidate, including the uniform inverse-flow construction.
The route agent independently derived every terminal field, the
complete Rayleigh formula, explicit bootstrap constants, and the
physical-clock derivative. No experiment was used.

l3_reachable_hessian_fresh_audit was spawned with fork_turns:none and
shown only the candidate and its listed mathematical dependencies.
It returned full scoped PASS at the hash above without corrections.
It verified canonical Gaussian-coordinate scaling, the rare/bulk
orthogonality, all trained-matrix contributions, the target Hessian
bound, the exact positive leading coefficient, every backward
bootstrap margin, finite-width continuation to zero readout, and
all physical Jacobian corrections.

The certification is deterministic and trajectory-specific only in
the stated zero-readout-reachability sense. Primal bounds hold on the
whole constructed segment; bounded B is asserted only at its endpoint.
The initial hidden state is not the prescribed Gaussian draw. Neither
Gaussian-typical failure, a population counterexample, nor failure
under extra Hessian-history controls is certified.
