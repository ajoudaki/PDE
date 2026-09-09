# Three hidden layers: active proof contract and evidence

Destination continuation, 2026-09-05: a complete isolated audit of
the metric-projection gate test now refutes uniform primal-only RMS
Lipschitz stability on bounded, algebraically valid canonical states.
It makes no trained-trajectory or initialization-probability claim.
A separate complete isolated audit certifies an energy-compatible
auxiliary projection with an actual
O(1/R) mean-absolute middle-equation defect and cap-independent
finite-width energy/coercivity/clock bounds. Its fixed-width eventual
exactness is proved, but no width/cap interchange or population law.
The preceding exact filtered two-matrix Gaussian law and its growing-
clipped state/query comparison remain certified; the predictable
prior-use response is still uncontrolled. The full theorem remains open.

This is a research record, not a completed proof. The requested theorem has
not been established or disproved.

## Fixed target

One input and target, both 1; activation \(\phi(s)=\arctan s\).
The two hidden matrices are \(W^{(2)},W^{(3)}\), with independent entries
\(N(0,1/n)\). The first preactivation has independent \(N(0,1)\) entries.
The rescaled readout is \(W^{(4)}\), with independent \(N(0,n^{-2})\)
entries; its population initial value is zero. All initialization blocks
are independent.

The predictor is \(f_n=(W^{(4)})^\top h^{(3)}/n\), residual \(r_n=f_n-1\),
and loss \(r_n^2\). The hidden derivative vectors exclude the residual.
The finite gradient equations are
\[
\dot z^{(1)}=-2r_n\delta^{(1)},\qquad
\dot W^{(\ell)}=-\frac{2r_n}{n}\delta^{(\ell)}
 (h^{(\ell-1)})^\top,\quad \ell=2,3,\qquad
\dot W^{(4)}=-2r_nh^{(3)}.
\]
Exact GD is Euler for these raw parameter equations, with
\(\eta_n=n^{-2}\).

Completion requires an unconditional autonomous, uniquely restartable
population action flow, full-sequence joint convergence on every fixed
finite time interval, convergence of predictions, losses, all four raw
kernel blocks and hidden path/velocity measurements, and nontrivial
small-time feature learning. The final state has finitely many fields and
operators, not finitely many scalar coordinates. Both orientations of
both initial matrices must be preserved.

## Evidence and routes

| Claim or route | Current status |
| --- | --- |
| Global finite-width existence and width-uniform primal/operator bounds | Proved; independently checked in /tmp/l3-extension-check-mj4s9q/VERIFIED_SCOPE.md |
| Copy the two-layer dimension-free local-Lipschitz proof | Invalid: a Gaussian first-Euler-state construction disproves that estimate |
| Old /tmp/L3_SELF_CONTAINED_PROOF.md | Not a proof of this contract; changes activation and horizon, and its main response estimate has an unclosed multiplication step |
| Fixed finite Gaussian calculations | Available source-identification mechanism; not by itself a continuous-time convergence theorem |
| Compact-feature-time derivative bound for \((W^{(3)})^\top\delta^{(3)}\) with bounded readout initialization | Derived from primal bounds; does not imply spatial tail control |
| Gaussian first-chaos covariance norm of response | Bounds its \(L^2\) size; does not bound absolute response coefficients or exponential tails |
| Continue from primal bounds, zero readout, and predictor positivity alone | Insufficient: a nongeneric but exactly reachable deterministic initialization produces a \(\sqrt n\) spike |
| Generic Hilbert gradient-flow/semiconvexity argument | Does not close the unbounded middle multiplier |
| Direct published continuous-time DMFT invocation | No applicable theorem found among the inspected primary sources; their hypotheses differ |
| Readout norm convexity in feature time | Proved and passed two independent reviews; gives global finite-width readout-kernel coercivity for zero or small readout |
| Prescribed Gaussian finite-width flow | With probability tending to one, a width-independent kernel lower bound, exponential loss decay, finite feature horizon, and exponential parameter convergence hold for all physical times |
| Lower-layer activation second moments and integrated backward energy | Proved from readout coercivity, bounded operator norms, and the exact feature action |
| Exact GD analogue at \(\eta_n=n^{-2}\) | Complete canonical finite-width optimization proof, including the prescribed Gaussian corollary, passed two independent full-file reviews. No GD-to-flow stability assertion follows merely from these bounds |
| Uniform concentration of signed empirical hidden means | Sign-symmetry reduction passed an independent review after making the high-probability premise explicit; separate from convergence of general empirical measurements |
| Fixed clipped three-layer source representation | Proved by conditioning and Gaussian integration by parts, including interleaved matrices/transposes, current-step return terms, singular covariances, and empirical feedback; independent full-file PASS |
| Mesh- and clipping-uniform local response tails | New coefficientwise bootstrap gives explicit positive \(S_0\) and Gaussian tails for the middle backward action; separately checked by an independent adversarial reviewer |
| Common three-layer action state and fixed-clipping flows | Constructed from consistent finite-program laws; both adjoints preserved; each fixed-clipping flow exists globally and has its width limit |
| Unconditional local uncut MF/GF and exact-GD limit | Consolidated in L3_LOCAL_COMPLETE_PROOF.md, with every representation/tail premise discharged; two independent combined reviews passed, followed by a complete PASS from l3_local_fresh_audit, spawned with no conversation history and shown only the consolidated proof |
| Local gradient structure and all-layer feature learning | Genuine HS/mean-square gradient proved; all three hidden layers move at order \(t^2\), all hidden kernel blocks are positive at order \(t^2\), total kernel changes, and affine-regression residuals remain positive |
| Current response atoms and own-site characteristic | Exact current coefficients and adjacent-time response coefficients stay bounded; arctangent removes current-site curvature. The contracted earlier-memory increment now has a uniform L2 bound, but its action on tangent fields remains uncontrolled |
| Bounded linear equation for the middle backward action | Exact frozen-generator norm bound holds; the coupled coefficient-difference term still contains the unbounded multiplier and does not supply stability |
| Three targeted primary global-DMFT routes | None applies unchanged: global-Lipschitz row-map, independent directed/noisy, or Gaussian-polynomial-Hamiltonian hypotheses fail; this is not a literature-wide impossibility assertion |
| Gated-field localization using q2 time variation and lower action | Exact signed localized power is \(O(R^{-1})\); an independently checked forced lower-subsystem construction shows that the shared first-layer cross term can cancel rare self-power. This defeats only a general deterministic implication, not the prescribed Gaussian/top-feedback theorem |
| Full Gaussian-initialized three-layer theorem | Unresolved |
| Strong finite endpoint and optimized cutoff comparison | ENDPOINT_RESTART_REDUCTION.md proves HS matrix limits, bounded-readout endpoint convergence, and C1 extension of the backward field along an existing path. An independently checked Osgood comparison needs only a uniform tail envelope of order exp[-c R/log R], but that comparator premise is not proved globally |
| Actual top virtual work and top-only deletion | TOP_COUPLED_LOCALIZATION.md gives exact top/lower identities and an all-finite-feature-time O(sqrt(p)) copied-top deletion estimate. Independently checked. The copied top still depends on deleted Gaussian columns through its supplied actual bulk trajectory |
| Fully pruned Gaussian queries, simultaneous over all small subsets | PRUNED_GAUSSIAN_SUBSET_BOUND.md proves a high-probability O(sqrt(p log(e/p))) bound, uniform in time and all subsets of size at most pn, for the fully pruned zero-readout network. Independent PASS. The full/pruned bulk comparison is a separate unproved obligation |
| Covariance-based response regularity | COVARIANCE_RESPONSE_INCREMENT_REDUCTION.md constructs the initial action as a Gaussian isometry plus the adjoint of the reverse Gaussian isometry. It controls contracted memory increments without absolute response-row bounds; neither this identity nor Gaussian source regularity controls the transported-adjoint tail |
| Logarithmically weakened deletion and directional Gaussian response criteria | DELETED_QUERY_RESPONSE_AND_ENTROPY_AUDIT.md gives independently checked sufficient reductions: bulk deletion error sqrt(p) log(1/p) loglog(1/p), or suitable normalized trace and Gaussian-direction Jacobian moments, would imply the Osgood tail condition. None of those new premises has been proved for the full network |
| Inverse-middle metric and natural-coordinate combination | INVERSE_MIDDLE_METRIC_AUDIT.md derives exact comparison identities. The inverse metric retains the middle gate term and introduces a lower multiplier; the natural coordinate retains a nonlocal commutator. Actual Gaussian small-time curvature has both signs. This is not a negative theorem about continuation |
| Additional stochastic Taylor universality source | STOCHASTIC_TAYLOR_UNIVERSALITY_APPLICABILITY.md checks Dembo--Gheissari's random-matrix diffusion class. Zero noise and block-symmetric disorder are compatible, but the drift is affine and the needed nonlinear directional-response bound is not supplied |
| Fully pruned rare-block mobility | PRUNED_RARE_BLOCK_GEOMETRY.md proves a simultaneous weighted Gaussian Gram bound. The incoming rare self-block is within O(sqrt(p log(e/p))) of a scalar alpha between 1/4 and a^2+1, uniformly in time; a signed top response block has the analogous approximation. Independent PASS. Actual unpruned gates are not independent of these rows |
| Adaptive actual rare self-block comparison | ADAPTIVE_RARE_SELF_BLOCK_MODULUS.md proves a uniform all-submatrix event and an arbitrary-adaptive-diagonal estimate. It controls the actual/reference rare self-block difference by C[omega(d)+p log(e/p)+o_n(1)], omega(d)=d(1+log_+(1/d)). Independent PASS. Neither off-block transport nor the state distance d is controlled by this lemma |
| Scalar rare displacement and accumulated rank forcing | DIRECT_SCALAR_PRUNED_REDUCTION.md proves exact finite-pair and integration-by-parts identities. Rare row training and rare transformed-bottom forcing are controlled by rare preactivation displacement and an explicit bulk residual, without requiring a tail bound on the instantaneous rare backward field. Independent PASS. The later single-pruned note now bounds that residual in terms of the full-state distance; active bulk feedback remains open |
| Actual single-column Gaussian tangent | ACTUAL_BULK_GAUSSIAN_TANGENT_ENERGY.md proves exact 1/n mean-square forcing under an independent derivative probe, a normalized-HS bridge to deleted-query Jacobians, and removal of the learned top history from the bad energy term. The actual mixed covariance pairing and its second-response contractions remain unbounded |
| Actual two-time rare return | ACTUAL_TWO_TIME_RARE_RETURN.md extends the self-block estimate to the actual bounded-part tangent propagator. At short time separation and small full/pruned distance, its compression to the same rare set is close to a positive scalar matrix. Disjoint rare-to-rare transfer follows by pruning their union. Rare-to-large-bulk transfer and multiplication by the middle curvature remain uncontrolled |
| Initial self-return sign and time-ordered expansion | TIME_ORDERED_PROBE_AND_SELF_RETURN_AUDIT.md proves a favorable conditional Gaussian sign for the principal initial self-site curvature. The exact tangent jet also has localized covariance, but its nonuniform remainder and lower-order readout energy prevent a finite-time counterclaim. Adaptive Wick contractions retain mixed second flow derivatives; ordinary pair counting does not close them |
| Single-pruned off-block residual | SINGLE_PRUNED_OFFBLOCK_OSGOOD.md proves rho_E <= C[sqrt(p log(e/p))+d_E sqrt(1+log_+(1/d_E))+o_n], uniformly over sets and time, for the zero-readout proxy. The new restricted-column/sorted-block argument uses only L2 backward bounds and a small L1 gate-difference product. Root-checked and independent full-file PASS. It does not bound the uncompressed active update |
| Sharpened accumulated rare forcing | SHARP_RARE_ACCUMULATED_FORCING.md combines the new residual bound with pruned Gaussian backward queries. The old p^(1/3) size term improves to sqrt(p log(e/p)), plus the same integral of the distance modulus. Independent full-file PASS. The bound is not a closed inequality for that distance |
| Actual probe covariance-support localization | ACTUAL_PROBE_LEVERAGE_LOCALIZATION.md proves that outside an explicit support of mass O(1/R), the actual signed energy contribution is at most C sqrt(R) Lambda and its time-integrated forcing is controlled. Root-checked. The exceptional signed covariance and mixed responses remain open |
| Actual moving-range probe normal form | ACTUAL_MOVING_RANGE_PROBE_NORMAL_FORM.md decomposes the true tangent into the moving lower-training range and its orthogonal complement. ACTUAL_WEIGHTED_ADDITIVE_PROBE_SOURCE.md strengthens its directly forced component: it stays purely in the top blocks, so its lower preactivation response and mixed curvature covariance are identically zero. The weighted additive source is controlled. Both notes have independent full-file PASS. The recycled response remains uncontrolled |
| Actual rare backward derivative | ACTUAL_RARE_BACKWARD_DERIVATIVE.md proves a simultaneous all-set/time estimate for the actual derivative by C[rare backward action + sqrt(h(p)) + mu(d_E) + width error]. Four explicitly independent pruned Gaussian coefficient families control the adaptive small-L1 gate products; actual rare self-feedback is retained. Root-checked and independent full-file PASS |
| Rare nonnegative backward energy and whole paths | RARE_BACKWARD_ENERGY.md absorbs that retained self-feedback through the exact arctangent scalar identity and integration by parts. It proves integral ||P_E delta2||_2^2/n <= C[h(p)+width error squared+integral mu(d_E)^2], and the same bound for integrated squared q2_E and z2_E derivatives and their coordinatewise maximal displacements. Independent full-file PASS, including the path corollary. The right side still contains d_E |
| Actual uncompressed gate bound | ACTUAL_WEIGHTED_GATE_HARDY_BOUND.md bounds the active gate-difference vector itself by the actual maximal backward path and a Hardy average over larger-deletion distance histories. No nested-reference event is needed. Independent full-file PASS, including the discrete width floor and the state hierarchy preserving its square root and nested time integral. The scalar leading term has Osgood size; the history term remains |
| Finite-floor Hardy-history obstruction | RARE_HARDY_HIERARCHY_COUNTEREXAMPLE.md gives the continuum diagnostic. FINITE_FLOOR_HARDY_HIERARCHY_COUNTEREXAMPLE.md proves that the actual scalar inequality (19) alone, with its exact Phi, discrete floors, zero width error and zero initial derivatives, permits a positive limiting error. It also allows any positive constant and delayed start. Root checked and independent full-file PASS. Neither family is a canonical-flow trajectory |
| Signed range scalar cancellation | ACTUAL_SIGNED_RANGE_INTEGRATING_FACTOR.md removes the principal scalar curvature from the actual range probe by c_E=D_E^{-1}a_E, retaining all off-block/memory terms and the weighted source. It exposes an actual primal-action/response-covariance pairing not bounded by the separate means. Root checked and independent full-file PASS. This is an identity/reduction, not a new closed response estimate |
| Full-backprop primitive response | ACTUAL_BACKPROP_PRIMITIVE_RESPONSE.md integrates the ENTIRE middle backprop variation before extracting the training range. Its exact bounded-memory representation removes the inverse gate from ALL non-curvature forcing, including the response-dependent part. The representation and source estimates are uniform over the prescribed C1 clipped family without clipped coercivity or second clipping derivatives. Root checked and genuinely fresh-context proof-only full PASS, including the clipped extension. The explicit signed residual/returned-response covariance remains unbounded |
| Exact off-diagonal primitive pairing | ACTUAL_PRIMITIVE_OFFDIAGONAL_PAIR.md proves all instantaneous diagonal self-pairs cancel, including for the prescribed clipping. The remaining actual term is an off-diagonal polarized covariance plus causal memory. Root derived and fresh-context proof-only PASS after narrowing the final trace-bound wording. An algebraic PSD example checks the absence of a general sign; it is not a canonical trajectory |
| Actual logarithmic Jacobian and probe distortion | LOGARITHMIC_NETWORK_COMPARISON.md proves the actual state Jacobian has nuclear norm O(n), hence O(1) width-normalized two-sided logarithmic singular distortion. Exact determinant bounds apply to both the full Gaussian column seed and the trained response increment. Root checked and independent full-file PASS. These logarithmic bounds do not control response trace moments or the alignment of the actual pruning source with expanding directions |
| Joint middle-input/top-query energy | JOINT_MIDDLE_QUERY_ENERGY_AUDIT.md gives exact tangent and full/pruned secant cancellations of the pure middle-input third derivative. The corrected query is already a bounded algebraic top-variation map; differentiating it leaves a mixed trained-top/actual-velocity product and the original mobility feedback. Root checked; independent helper checked the tangent and full finite-pair calculation. This tested joint energy does not improve global response closure |
| Time-analytic continuation from primal bounds | TIME_ANALYTICITY_DERIVATIVE_AUDIT.md computes the exact full-network fifth derivative at zero readout and a bounded-operator initialization family where it diverges as -c sqrt(n). Gaussian full support rules out a deterministic bound on the ENTIRE norm event, not a high-probability Gaussian bound. A separate saturated scalar Gaussian average is smooth but nonanalytic at zero. Root checked and fresh-context proof-only PASS. Typical-Gaussian analyticity remains unproved, not disproved |
| Actual second log-gate integration | ACTUAL_LOG_GATE_SECOND_IBP.md proves exponential spatial tails for maximal log-gate amplitude and a uniform inverse for I-diag(log D2)(A2/m1) under the uncut coercivity premise. Its exact second integration retains ordered off-diagonal gate products, a lower-gate mobility derivative, and the complete transformed residual/source. Root checked and fresh-context proof-only PASS. Invertibility is resolved, but no response estimate follows yet |
| Active gate primitive and recent cavity theorem | ACTIVE_GATE_PRIMITIVE_AUDIT.md records exact integration-by-parts identities but leaves an uncompressed product. RECENT_CAVITY_THEOREM_SCOPE.md checks the 2026 Dandi et al. primary theorem: fixed iteration counts and globally Lipschitz row maps do not yield the missing uncut continuous-time estimate. Neither route supplies global closure |
| Finite full/pruned backprop primitive | FINITE_PRUNED_BACKPROP_PRIMITIVE.md proves the nonlinear finite-pair counterpart of the full primitive, with bounded causal memory and an unweighted ordinary source. Its exact arctan divided-difference characteristic works for common merely Lipschitz clipping, without coercivity. Root authored/read; genuinely fresh-context proof-only PASS. The two signed finite-pair terms remain uncontrolled |
| Correct metric for the actual log-gate commutator | ACTUAL_LOG_GATE_COVARIANCE_COMMUTATOR.md cancels the commutator exactly, even with the actual adaptive probe covariance. A positive corrected-response energy controls the primitive, but retains symmetric log-derivative work, the actual lower mobility derivative, and the complete weighted source. Root checked and fresh-context proof-only PASS. This supersedes any suggestion that the commutator itself is unavoidable under every metric |
| Full polarized Gaussian integration by parts | ACTUAL_FULL_PAIR_GAUSSIAN_IBP.md keeps both orientations, learned increments, and smooth Gaussian localization. The orientations add rather than cancel mixed flow derivatives; a genuine two-neuron small-time jet proves a localized mixed sector nonzero. Root checked and fresh-context proof-only PASS. This is not an unlocalized sign result, uniform-bound failure, or canonical counterexample |
| Additional 2026 primary-source scope checks | RESNET_DMFT_PRIMARY_SCOPE.md checks Chaintron--Chizat--Maass: residual architecture, finite discrete training count, and conditional higher-moment arguments do not directly supply this GF limit; its depth ODE is not training time. ORTHOGONAL_SK_PRIMARY_SCOPE.md checks Theorem 2.4 of Fan et al.: fixed scalar drift plus fixed orthogonally invariant linear disorder differs from the trained composition here. Neither check is a full-paper audit or a literature-wide no-go |
| Actual Gaussian-divergence comparison | ACTUAL_GAUSSIAN_DIVERGENCE_SCOPE.md derives every raw-block trace and the correct Gaussian density derivative. Against the tiny-readout initialization law, actual full-state entropy is Theta(n^3) at small fixed positive times; a time-broadened independent readout reference leaves n log n+O(n). Root checked; fresh-context proof-only PASS after two wording fixes. This excludes only the proposed direct full-state likelihood argument, not a compressed-law comparison or global convergence |
| Actual hidden density and conditional entropy | ACTUAL_PROJECTED_DENSITY.md proves hidden absolute continuity at every fixed width/time for every deterministic readout, including zero, and hence the tiny Gaussian mixture. The exact finite hidden entropy is an O(n) term plus conditional readout entropy increase; its required upper bound remains open. Root checked and fresh-context proof-only PASS. A noncanonical projection example is explicitly not a canonical counterexample |
| Raw RMS-only Hessian and every-plane graph volume | ACTUAL_HIDDEN_GRAPH_VOLUME.md proves the raw Gaussian-coordinate full Jacobian has nuclear norm O(n) using only readout RMS. Every transported tangent plane has expected absolute log-volume change O(n). Hidden projection loses an exact factor in at most n directions, not controlled by that intrinsic bound. Root authored/checked and fresh-context final-hash PASS |
| Deterministic projection-angle occupation from norm bounds | PROJECTED_ANGLE_STRUCTURAL_COUNTEREXAMPLE.md disproves the proposed bound even for bounded analytic vector features, fixed dimensions, bounded J and nuclear Hessian action, and an everywhere-in-time invertible hidden projection on [0,4]. Root checked and fresh-context final-hash PASS. This is explicitly noncanonical and says nothing about Gaussian-averaged canonical distortion |
| Scalar-readout positive projection theorem | SCALAR_READOUT_PROJECTION_THEOREM.md proves global hidden diffeomorphism and divergence lower bounds for every bounded smooth scalar feature: arbitrary fixed readout in feature time, zero readout in forward physical time. Actual canonical n=1 entropy is bounded in those scopes. Actual output gradients do not commute almost surely at each fixed n>=2. Root checked/contributed and fresh-context final-hash PASS. No width-uniform projection or population conclusion follows |
| Scalar Schwarzian lifted to the full material Hessian | ACTUAL_SCHWARZIAN_MATERIAL_HESSIAN.md derives the complete actual B'=D^3F[b]. A bounded-primal canonical state has bounded B but positive and negative order-n quadratic values of B'-kappa B^2 for every fixed kappa. The exact physical-time version also fails. Root supplied/checked the state and physical extension; fresh-context full-file PASS. The witness is not reachable at positive time from zero readout and is not a typical-Gaussian obstruction |
| Counterexample to that theorem, or formal unprovability | Not obtained |

The missing stability step involves
\[
\phi'(z^{(2)})\odot (W^{(3)})^\top\delta^{(3)}.
\]
Bounded average squared size of the backward field does not uniformly
control its multiplication by a varying activation derivative.
The new local bootstrap controls this field on a fixed explicit
positive interval and closes the complete local theorem. The remaining
obligation is now continuation of that result to every finite physical
time. Any global proof must either extend the trajectory-specific
control or establish stability by an argument that genuinely avoids
the multiplication estimate.

The older repository research program uses an order-one Gaussian readout
initialization, unlike the vanishing readout here. Its failed-route
examples and algebraic identities are useful, but its claims must not be
silently transferred between these two initializations.

## Causal update: off-block estimate versus full-state stability

- New evidence: the exact rare off-block residual is no longer merely
  an unspecified term. It has a proved logarithmic distance modulus.
  Pruned Gaussian backward queries also improve the accumulated rare
  training scale to square-root rare-set size, up to that modulus.
- Validity scope: zero-readout finite-width proxy, full versus genuinely
  fully pruned; all sets and all times on a common finite feature
  horizon; either uncut or the same prescribed clipping on both.
- Claims upgraded: rare residual control and accumulated rare forcing.
- Claims unchanged: all-finite-time population continuation, uniquely
  restartable dynamics, global tiny-readout/GD transfer. Their full-state
  stability premise remains unproved.
- Superseded conclusion: the earlier statement that the rare off-block
  residual itself had no quantitative estimate. It is now bounded in
  terms of d_E; this does not supersede the open status of d_E.
- Newly exposed dependency: the active gate-difference product enters
  the active rank update and the full bottom transpose action without
  the Gaussian compression used in the new estimate. Its accumulated
  effect must be bounded. The response route isolates the corresponding
  uncontrolled contribution on an adaptive small covariance support.
- Authorized next branch: a signed/accumulated active-feedback estimate
  using the new rare bound, or an actual exceptional probe-response
  estimate. No new simulation is authorized or performed.

## Causal update: actual rare derivative, energy, and response component

- New evidence: the actual rare backward derivative is controlled by
  its own rare backward action plus a logarithmic distance modulus.
  Pairing with the actual bounded rare activation absorbs that
  self-feedback and proves a nonnegative spacetime-energy estimate.
  This is stronger than controlling only a signed accumulated update.
- New response evidence: the part driven directly outside the moving
  lower-training range now has a bounded exceptional covariance
  pairing. This is an actual derivative-probe result, not an inference
  obtained by differentiating a primal estimate.
- Exact scope of the rare estimates: zero-readout full/pruned proxy;
  the same prescribed clipping in both networks is also allowed.
  The event is simultaneous over sets and time, not over all clipping
  choices. Tiny-readout transfer has not been inferred.
- Claims upgraded: actual rare derivative and nonnegative rare energy;
  one previously uncontrolled exceptional response component.
- Claims unchanged: a closed full/pruned state comparison, full
  clipped-family stability, all-finite-time population continuation,
  and global tiny-readout/exact-GD transfer.
- Still unclosed: the uncompressed active gate-difference update,
  or equivalently a sufficiently strong estimate for the actual
  recycled-range covariance. The newly proved energy retains
  integral mu(d_E)^2 and is not a bound on d_E itself.
- Next authorized resolver: combine rare energy with a genuinely
  closed bulk comparison, or control the remaining signed range
  response. Exact primitive identities already recorded do not
  accomplish either step. No simulation or target change is authorized.

## Superseding refinement: the active update now has a history estimate

The active gate-difference vector is no longer wholly unestimated.
ACTUAL_WEIGHTED_GATE_HARDY_BOUND.md adds and subtracts the actual
backward query, applies the newly proved maximal-path subset estimate,
and integrates over the levels of the squared gate difference.
This bounds the uncompressed vector without another Gaussian query.

The remaining quantity is explicit: a Hardy average of
Phi(Y_r(u)) over deletion sizes r, integrated over earlier time u.
The actual squared-state inequality retains the square root of
this history. Its leading logarithmic term is Osgood, but that fact
does not remove the history term. Independent diagnostic testing
produces a flat positive error profile for the corresponding
continuum inequalities. No canonical counterexample is inferred.

Thus the next resolver is stronger signed or coordinate-dynamical
information than this absolute weighted majorization, or an actual
recycled-range response estimate. Merely iterating the schematic
Hardy bound is not justified as a closure argument.

The discrete-floor bridge has now passed independent full-file review.
This supersedes the narrower caveat that only a continuum schematic
inequality had been tested. The construction satisfies the exact
scalar finite hierarchy with C=1 and epsilon_n=0, yet
lim_{p downarrow 0} lim_n Y_{p,n}(t)>0. A slow clock handles any
positive constant; a delayed clock preserves a prior zero-error
interval. Thus the failure cannot be repaired just by keeping the
finite floor, tightening that constant, or invoking the completed
local theorem. The canonical signed equations are not satisfied
by this artificial family and remain an available source of new
information. The full canonical theorem remains unresolved.

## Superseding refinement: primitive response removes the weighted-source gap

The directly forced orthogonal response is now proved to be purely top-layer,
not merely to have bounded exceptional covariance. Its lower preactivation
response is exactly zero. This controls the inverse-gate-weighted additive
source in the older moving-range characteristic.

A different primitive, the time integral of the FULL middle-backprop
variation, goes further. Its exact integration-by-parts representation has
bounded causal memory and leaves every non-curvature source unweighted.
The resulting response-dependent source estimate uses only the common
primal bounds and the response energy itself. A fresh-context reviewer
checked the complete proof and the extension to the actual C1 clipped
family. No inverse lower mobility or clipped coercivity is needed.

This supersedes the old statement that weighted ordinary source terms are
an independent obstacle in every characteristic formulation. The remaining
obstacle in the new coordinate is precisely the signed residual/returned-
response covariance; no closed bound for it has been obtained.

The independently audited logarithmic-Jacobian note also gives a new
actual-network bound: the sum of logarithmic singular distortions is O(n).
This controls the number of strongly distorted directions, not the response
trace or the actual forcing's component in those directions. It is not a
substitute for the missing signed estimate. Full continuation, global
tiny-readout transfer, and the requested all-time theorem remain open.

## Causal update: finite errors, correct metric, and full Gaussian pair

The full/pruned nonlinear comparison now has the same useful unweighted
ordinary source as the derivative-probe comparison. Its exact bounded-memory
representation retains a quadratic finite-pair term that vanishes only in
the infinitesimal calculation. The arctan divided difference removes the
principal same-coordinate curvature without differentiating the clipping.
This strengthens the representation to actual finite errors; it does not
bound the two remaining signed terms or the full error.

The commutator in the second log-gate calculation is not intrinsically
uncontrollable: the mobility metric cancels its same-vector pairing, and a
positive metric for the corrected response cancels it while controlling the
primitive. The resulting complete energy still contains symmetric gate
work, the lower mobility derivative, and the weighted full source. Thus
the earlier ordered-commutator obstruction is narrowed, not a global
response theorem established.

The proposed FULL polarized Gaussian integration-by-parts test has now
been performed. Exchange of the two middle coordinates makes the mixed
second-response sectors add. Lower-matrix integration produces higher
responses. A smooth localized actual-network example proves that one such
sector is genuinely nonzero; it does not rule out a useful unlocalized
estimate or cancellation with other dynamical terms.

All three scoped notes have independent fresh-context proof-only PASS
reports recorded in REVIEW.md. None upgrades all-finite-time continuation,
global tiny-readout transfer, or exact-GD/population identification.
Do not repeat the tested exchange-cancellation proposal or treat the
removed commutator as an unavoidable obstruction. The new finite signed
error equation and the surviving full metric energy are the precise
remaining mathematical objects.

## Causal update: the complete-state density reference does not solve the gap

The actual ordinary divergence and hidden Gaussian-energy change are both
O(n), but the correct whitening multiplies the readout by n. Consequently
the full likelihood against the initialization law includes
n^3 times the change in the mean squared readout. The actual prescribed
tiny-readout flow has order-one readout size at fixed small positive time,
giving an order-n^3 entropy and typical likelihood cost. Broadening the
independent reference readout to variance n^-2+s^2 changes this to
(n/2)log(1+n^2 s^2)+O(n), rather than a width-independent likelihood.

This is a new actual-network scope calculation, not an inference from
an arbitrary adaptive counterexample. It defeats a direct passage from
the earlier O(n) Jacobian-trace bound to the desired query likelihood
bound. Projection can remove the large cost, but its conditional density
and transport divergence must then be estimated separately. The full
transcript together with an initial Gaussian column is singular against
their product law, since the initial column can be recovered from the
invertible flow. A genuinely compressed transcript can behave differently.

No conclusion about canonical global convergence or its impossibility
follows from these reference-law facts. No new experiment was run.

## Causal update: actual hidden density and intrinsic graph volume

ACTUAL_PROJECTED_DENSITY.md now proves that, at every fixed width and
finite feature or physical time, the hidden marginal has a density.
This holds for every fixed initial readout, including exactly zero,
and therefore for the canonical tiny Gaussian readout. The proof uses
actual analytic dependence and a nonzero hidden determinant at
W^(2)=W^(3)=0. It does not assume global invertibility of the hidden
projection. This supersedes any unresolved qualitative hidden-density
premise, but not the quantitative density or compressed-query premise.

For the actual nondegenerate initialization, the exact hidden relative
entropy is a controlled O(n) term plus
H_dif(W^(4)(s)|hidden(s))-H_dif(W^(4)(0)).
The conditional-entropy increase has not been bounded above by O(n).
The weak conditional-mean equation retains its covariance flux. The
zero-readout full joint law is still singular; hidden absolute continuity
does not justify an unsmoothed zero-to-tiny global transfer.

ACTUAL_HIDDEN_GRAPH_VOLUME.md strengthens the raw Hessian calculation:
in coordinates (z^(1),sqrt(n)W^(2),sqrt(n)W^(3),W^(4)), the full
feature-time Jacobian has nuclear norm O(n) using only readout RMS and
the existing operator bounds. Every transported tangent plane therefore
has intrinsic log-volume change O(n), also in expectation. This is
stronger than a full-flow determinant bound and does not need readout
maximum-coordinate control. The physical-time rank-one term is retained.

For the transported hidden plane, projection loses an exact factor
product_j sqrt(1-a_j^2), where at most n singular values a_j belong to
the readout part of an orthonormal tangent frame. Intrinsic-volume control
does not give a lower bound on this factor. A realizable NONCANONICAL
bounded-feature gradient example proves genuine hidden noninjectivity
and a singular hidden Jacobian while the full flow remains regular.
It establishes no canonical entropy sign, width-uniform failure, or
counterexample to the target theorem.

Both complete scoped notes passed separate fresh-context proof-only
reviews at the hashes in REVIEW.md. The all-finite-time theorem, global
tiny-readout transfer, and unique autonomous global continuation remain
unproved and unrefuted.

## Causal update: norm-only angle control is insufficient, scalar case is positive

The next proposed deterministic estimate has now been tested, not left
as a suggested resolver. Even bounded analytic feature maps with common
bounded J and bounded integral nuclear A can keep a hidden tangent
direction arbitrarily close to vertical for a whole fixed time interval.
The constructed hidden Jacobian remains invertible throughout [0,4].
Thus neither isolated-singularity removal nor time integration repairs
a projection-angle bound from those norm assumptions alone.
PROJECTED_ANGLE_STRUCTURAL_COUNTEREXAMPLE.md is an independently
fresh-context audited, fully realizable NONCANONICAL example. No
Gaussian-average failure or canonical counterexample follows.

There is a genuine positive distinction at scalar readout. For any
bounded smooth h, the exact dynamics x'=c grad h,c'=h remain on a
complete gradient orbit. Its orbit derivative p satisfies p''=H'p,
H'=|grad h|^2>=0, and p(0)=1,p'(0)=0. Hence p>=1 in both feature-time
directions, and the hidden map is globally invertible with
log det P>=integral div(full flow). A separate fixed-physical-time
argument proves the corresponding determinant bound for c_0=0.
SCALAR_READOUT_PROJECTION_THEOREM.md proves actual n=1 Gaussian entropy
bounds and integrability in precisely these scopes; it too has a
fresh-context proof-only PASS.

For the canonical vector readout, the different output-gradient fields
do not commute almost surely at each fixed n>=2. An explicit nonzero
analytic component proves that fact; it gives no uniform size estimate
and does not establish focusing. The scalar orbit proof therefore cannot
be extended merely by assuming independent commuting gradient clocks.

This round changes those two proposed mechanisms, not the full target.
Any projection route now needs genuinely canonical probabilistic or
signed information and an actual link to the required adaptive queries.
No conditional result has been promoted to completion.

## Causal update: a scalar arctan sign does not bound the full Hessian evolution

A new test used the exact negative-Schwarzian identity
phi''' phi'-(3/2)(phi'')^2=-2(phi')^4. It does not imply the proposed
uniform signed bound for the actual matrix-valued material Hessian.
ACTUAL_SCHWARZIAN_MATERIAL_HESSIAN.md derives the complete raw
Gaussian-coordinate B'=D^3F[b], including both trained weight matrices,
their transpose derivatives, and every readout and mixed-block term.

At an explicit bounded-primal canonical state, B itself is bounded in
operator norm. For two unit directions the quadratic values of
B'-kappa B^2 diverge with opposite signs at order n for every fixed
real kappa. The reason is concrete: the positive middle mobility
mI+W^(2)D_1^2(W^(2))^T need not preserve the sign of each coordinate.
At z^(2)=0, the middle Hessian coefficient vanishes, while its derivative
-2 q_i z_i' can be positive of order n. The actual mixed terms have
been evaluated, not omitted. The full physical Jacobian, with its
rank-one residual correction and material clock, has the same failure.

This refutes the proposed estimate on the bounded ambient state class
only. The example has f=0 and readout equal to one, and cannot be reached
at positive time from exactly zero readout. Gaussian full support does
not turn it into a typical-trajectory or expectation obstruction.
The fresh proof-only reviewer passed the complete note and its physical
extension at the exact hash recorded in REVIEW.md. No all-time
population or unique-continuation claim is upgraded or refuted.

## Causal update: a new comparison mechanism has small frozen perturbations

The primary Panahi comparison exactly matches a finite perturbed
Gaussian-query process. Its fixed-query-count perturbation removal does
not by itself cover continuous training time. However, the raw growing
Gaussian-matrix norm was too coarse to judge that route.

PANAHI_EULER_PERTURBATION_SIZE.md proves exact Gaussian identities in
both directions for histories frozen independently of the auxiliary
Gaussian array. A time-Lipschitz history has regularized effective rank
at most min(K,1+2(K M^2 T^2/sigma^2)^(1/3)). For K~n^2 and
sigma=n^-1/4, this gives expected squared integrated supremum
O(n^-1/6) and expected squared raw-query maximum O(n^-1/6 log n).
Additive regularization noise also vanishes. Repeated-history Cholesky
factors are evaluated exactly, including the strict reverse-time
triangular convention.

The root appended all actual canonical derivatives needed to locate
the temporal premise: h^(1), h^(2), and delta^(3), divided by sqrt(n),
are time-Lipschitz on the existing primal-bounded event. For the uncut
lower backward delta^(2), the direct product calculation controls only
the normalized L1 time derivative. Clipping gives a Euclidean bound
with a constant growing as 1+R. Thus the frozen top-matrix forcing is
covered, not the full adaptive comparison.

A new isolated reviewer read only the candidate and its cited primary
source and returned full scoped PASS at the hash in REVIEW.md.
In the perturbed process the queries depend on the auxiliary Gaussian
array; conditioning on those queries does not justify the frozen
isometry. Causal covariance control and nonlinear perturbation removal
remain required. No all-time theorem, unclipped stability, or unique
autonomous continuation is inferred.

Two targeted source checks are recorded separately. Panahi's unproved
complex-continuation claim is unused. Nishiyama--Imaizumi's noiseless
theorem really is global, but no reduction of the present trained
composition to its fixed-channel rowwise Lipschitz model is established.
Neither source-scope observation is a negative theorem about the target.

## Causal update: adaptation is controlled under its actual rank premise

The comparison route progressed beyond the preceding frozen calculation.
PANAHI_CAUSAL_ADAPTATION_ISOMETRY_TEST.md constructs bounded, rank-one,
time-Lipschitz causal queries with exact nonzero mean and second-moment
corrections. The corrections are at the natural 1/n scale and still
vanish with width; this falsifies frozen conditioning, not an adaptive
bound. An isolated reviewer passed the complete calculation.

PANAHI_ADAPTIVE_GRAM_MARTINGALE.md then resolves the adaptive covariance
step under an explicit actual-history rank bound. Prefix-consistent
Cholesky columns t_i,s_i obey sums t_i t_i^T<=I and s_i s_i^T<=I.
The exact accumulated matrix sum t_i Gamma_ij s_j^T is a martingale
when each fresh row is revealed before its fresh column. Its two
predictable variations are at most 2 r_omega I and 2 r_theta I.
The two query perturbations equal this matrix acting on the current
query, plus an explicitly small fresh Gaussian remainder.
Predictable rank stopping, symmetric truncation, and the verified
rectangular matrix Freedman inequality give a uniform bound whenever
r log^2(n)=o(n), with polynomial query horizon. A fresh-context auditor
checked the entire candidate and primary dependencies and passed it.

Do not leave the adaptive covariance bound on the list of wholly open
steps: the exact scoped estimate above is now proved. Its ACTUAL rank
premise and nonlinear perturbation removal remain open.

PANAHI_SMALL_JITTER_RANK_INFLATION.md explains why the rank premise
cannot be silently transferred from a smooth path to a nearby noisy
one. With K=m^2, theta_l=sigma U_l/sqrt(m), and constant omega_l,
the histories converge uniformly to zero as sigma->0 but their
regularized effective rank divided by m tends to one. Both the final
raw Gamma perturbation norm squared and its integrated norm squared
converge to strictly positive constants. The proof is elementary and
received a complete fresh-context PASS after one scope correction
distinguishing the regularization/time-Lipschitz regimes.

This last example is a frozen algebraic test, not the actual trained
canonical history. No canonical failure, global limit, or restart
theorem is inferred. The completed local theorem remains the strongest
full canonical limit result. All exact final hashes are in REVIEW.md.

## Causal update: primitive query compression is exact, but not a causal bridge

INTEGRATED_INITIAL_QUERY_COMPRESSION.md preserves the complete finite
feature dynamics and both trained matrix histories while introducing
a^(2)(s)=integral_0^s delta^(2)(u)du. The first transformed coordinate is
x^(1)=x0^(1)+(W0^(2))^T a^(2)+R^(1), with
R^(1)(s)=integral h^(1)(u) [(a^(2))'(u)]^T
                  [a^(2)(s)-a^(2)(u)]/n du.
All other rank memories are retained explicitly.

The only initial-matrix state arguments are h^(1),a^(2),h^(2),delta^(3).
Each is time-Lipschitz in Euclidean norm divided by sqrt(n) on the
existing primal event. Integration by parts gives explicit Lipschitz
bounds for M^(2) and R^(1) under uniform approximation of uniformly
Lipschitz paths; M^(3) has its ordinary integral bound.
Thus neither discarded rank memory nor temporal roughness of a supplied
state path is the remaining issue in this representation.

A separate isolated reviewer checked the full canonical finite
derivation, all normalized constants, and the scoped limitations and
returned PASS. Actual query values at mesh points were generated using
unrecorded matrix uses between them; they are not thereby measurable
from the retained finite-query transcript. An autonomous finite-call
approximation still needs stability, and the exact primitive difference
retains [phi'(z^(2))-phi'(z_tilde^(2))] q_tilde^(2).
Uniform approximation of the primitive also does not prove convergence
of its derivative, needed for hidden velocities and the first raw
kernel block. No all-time canonical claim has been upgraded.

## Zero-readout reachability does not repair the primal-only Hessian bound

ACTUAL_ZERO_READOUT_REACHABLE_HESSIAN.md adds a positive bulk channel
to the earlier rare-coordinate material-Hessian construction. For
every fixed sufficiently small positive epsilon and every even n>=4,
the terminal state is reached from exactly zero readout in a positive
feature-time interval bounded above and below independently of width.
All original primal bounds hold throughout that segment. The complete
Hessian B is uniformly bounded at the terminal state, but a unit
Rayleigh quotient of B'-kappa B^2 grows at least c epsilon^2 n-C_kappa
for every fixed real kappa. The physical-time Jacobian has the same
failure: all residual-clock corrections are bounded at that state.

The root checked the entire construction. An isolated reviewer shown
only the candidate and explicit dependencies returned full scoped PASS.
This supersedes only the old witness's zero-readout-unreachability
limitation. The initial hidden matrices here are deterministic and
correlated, not independently Gaussian. No Gaussian-typical failure,
fixed-time convergence failure, or failure under additional
Hessian-history assumptions is proved. The all-time goal remains open.

## Destination update: generated-action higher moments

GAUSSIAN_ACTION_LP_OBSTRUCTION.md is now independently audited at SHA256
66bab078eb40ac789cf4f818485db07aaec7c1b4f6c9b3b5eb254d5d89bf322c.
Its three-query construction proves that the same canonical initial
action, and its adjoint, have no bounded L-infinity-to-Lp or Lp-to-Lp
restriction for any finite p>2 on the entire generated coordinate spaces.
The output's population Lp norm grows at least as epsilon^(1/p-1/2),
although every input is bounded by one. Exact Gaussian conditioning
retains the return from the previous transpose use; the final Gaussian
innovation is generated by the matrix and is not an extra root.

Claim rung: a proof-route obstruction on the full generated spaces.
Status: proved, root checked and fresh-context complete PASS.
The coordinate sensitivities grow with epsilon, and no trained-flow
reachability is asserted. Thus the canonical global theorem and every
actual trained-tail or response-amplitude obligation remain unchanged.
The former unaudited status in the handoff is superseded; the proof
itself is unchanged. The complete review and exact dependency hashes
are in ../GAUSSIAN_ACTION_LP_REVIEW.md and REVIEW.md.

## Destination update: actual squared-log response bounds

ACTUAL_SQUARED_LOG_RESPONSE.md now has an isolated complete PASS at
SHA256 d416464bf1b5e4a792bb6937f0f7eec0e5d19cd70ca05816d02f011bf64547f0.
The full canonical raw-coordinate Hessian has Frobenius norm O(sqrt(n))
on the proved primal event. Every initially isometric rectangular
homogeneous response obeys sum(log sigma_j)^2 <= C n (Delta s)^2.
This includes actual Gaussian top-column derivatives and the specified
trained-increment logarithmic covariance bound. It retains all trained
blocks and the fixed-physical-time clock derivative.

ACTUAL_CLOCK_RANK_ONE_RESPONSE.md (SHA256
a3e093852f07d58b474197fd4781dfb69830203a21eda7e788d45af27f28f0bd)
has an isolated complete PASS after correcting its covariance wording
to distinguish n nonzero eigenvalues from N-n ambient zeros.
The exact feature/physical propagator difference has rank at most one.
Interlacing and bounded total feature time give an all-physical-time
bound after excluding the largest and smallest singular values.
The same event covers every reached starting time and initial isometry.

ACTUAL_LOG_RESPONSE_METRIC_TRANSFER.md (SHA256
29304fb9771653257d3d638908ad4a08aca60690ce3ff4a9f2edfe73bf4bca0e)
also has an isolated complete PASS. The exact endpoint conjugacy for
F(z^(1)) costs only O(n) squared logarithmic energy by first-layer RMS.
It transfers the estimates to the original transformed metric and
retains the 1/sqrt(n) scaling of the actual Gaussian column response.
The root read all completed reviews and verified final hashes.
Full provenance is in REVIEW.md and the three separate review files.

Claim rung: actual canonical finite-width response-spectrum estimates.
No width-uniform normalized amplitude/trace, hidden projection, coupled
source alignment, or population continuation follows. Even these
squared-log bounds allow an isolated exp(C sqrt(n)) amplification.
The complete global goal remains open.

ACTUAL_ONE_SIDED_CLOCK_RESPONSE.md now has a fresh-context complete PASS
at SHA256 f5d813af3bb195ba6b5d1829f02556d6a57bf803e3f1d9b883ad3983929e4b5c.
The negative semidefinite physical clock correction can be discarded
in an UPPER positive-log energy derivative. Thus EVERY expanding
direction is included in an all-physical-time squared-log bound.
Only the smallest singular value is excluded from the two-sided bound;
the actual flow direction contracts with the residual, proving that
an all-time two-sided bound without any exclusion cannot hold.
Regularized squared logarithms of ALL trained-increment response
singular values are bounded uniformly over physical time, in both
raw and transformed metrics, with the correct Gaussian column scaling.
The complete review includes (8a)--(8b), the full dependency checks,
and all quantifiers. No mathematical correction was required.

This supersedes the two-extreme limitation of the earlier clock
estimate, not the open amplitude/trace or global population obligation.
The canonical theorem remains open, and the destination goal is active.

## Destination update: actual canonical Gaussian signed-work coefficient

CANONICAL_GAUSSIAN_SIGNED_WORK_JET.md has passed a complete independent
audit together with both proof dependencies. It concerns the actual
full signed primitive work, after averaging all initial top-matrix
Gaussian column probes:
\[
\mathscr W_n(s)=\frac1n\sum_i\mathbb E_\xi
c_i^T\operatorname{diag}(\beta(z^{(2)}))
\bigl(q^{(2)}\odot\zeta_i-(z^{(2)})'\odot c_i\bigr),\qquad
\beta=\phi''/\phi',\quad
c_i=\operatorname{diag}(\phi'(z^{(2)}))^{-1}
\int_0^s\operatorname{var}_i\delta^{(2)}.
\]
Here \(\zeta_i=\operatorname{var}_i z^{(2)}\) is the complete trained
response, including retained lower memory. The probe is
\(\xi e_i^T/\sqrt n\) in \(W^{(3)}_0\). No trained matrix is resampled.
Under the exact prescribed independent Gaussian initialization,
\([s^5]\mathscr W_n\to J_*>0\) in probability, with the explicit
constant in the combined note.

GAUSSIAN_SIGNED_PRIMITIVE_WORK_JET.md first proves the zero-readout
coefficient: convergence in probability and L1, and strictly positive
expectation for every n>=2. Its two exact Gaussian conditional laws
retain all covariance cross terms and the finite-width product bias.
Conditional Poincare estimates control the actual random coefficient.
TINY_READOUT_SIGNED_JET_TRANSFER.md then proves an O_P(1/n) difference
of fifth coefficients on coupling zero and canonical tiny readout.
The coefficient is polynomial of degree at most six in readout
amplitude. Exact finite-jet expansion extracts polynomial empirical
contraction prefactors, permitting primary Tensor Programs III v3,
Theorem 2.10 to apply to parameterless programs. Conditional Gaussian
quadratic-form tightness is proved separately; fixed Vandermonde
interpolation bounds all coefficients. No expected-moment theorem or
empirical-scalar-feedback extension is assumed.

Claim rung: actual canonical finite-initial-coefficient theorem.
Status: proved, root checked, complete isolated combined PASS.
The reviewer was shown only the proof and explicit mathematical
dependencies and verified the versioned primary source independently.
Exact proof/review/source hashes are recorded in REVIEW.md.
No numerical experiment was used.

This excludes exact cancellation of the whole signed work as a local
identity on canonical events of probability tending to one. It does
not exclude a nonpositive whole function at tiny readout, since lower
time coefficients may be nonzero. No canonical L1 or finite-width
expectation sign, uniform Taylor remainder, common positive-time sign,
response-amplitude bound, or global counterexample is inferred.
The prior localized two-neuron calculation is no longer the strongest
noncancellation evidence; its different scope remains valid. Positive
upper Gronwall estimates and the full global theorem remain open.

## Destination sharp fractional-gate update

SHARP_FRACTIONAL_GATE_QUERY_BOUND.md has passed a full isolated audit
on its explicit zero-readout common event and established prefix,
primal-comparison, and state-energy inputs. The exact finite fractional
selection bound replaces the earlier Hardy size integral by linear
interpolation of \(\Phi(Y_r)\) at the two size-grid points adjacent to
the actual gate mass \(a\). It also replaces the extra-log entropy
term by \(h(a)=a\log(e/a)\). Adaptive weights need no independence:
this is a deterministic inequality for every weight vector after the
common event is fixed. Fractional mass below \(1/n\) gives
\(na\,\Phi(Y_{1/n})\), not zero.

The remaining hierarchy contains
\[
\int_0^t\left\{Y_p(s)s\int_0^s
\mathcal I_n(\min\{1,C_0Y_p(s)\},u)\,du\right\}^{1/2}ds,
\]
where \(\mathcal I_n\) interpolates the values of \(\Phi\).
SHARP_SIZE_COMPOSITION_HIERARCHY_TEST.md has a separate complete
isolated PASS: even this stronger scalar hierarchy admits a bounded
finite-floor family with zero initial value and derivative, uniform
deletion continuity on an initial interval, and a later positive
small-deletion limit. Its construction uses zero width error. This
refutes sufficiency of that scalar inequality, not the network theorem.
The former Hardy bound is no longer the strongest gate estimate;
its insufficiency was not itself a proof that the sharper one fails.
The new independent construction supplies that separate check.

Current additional candidates, not yet certified:
CANONICAL_TINY_READOUT_RARE_PATH.md and
CANONICAL_FRACTIONAL_GATE_HIERARCHY.md directly treat actual and pruned
flows sharing \(G^{(4)}/n\), and are in a complete combined audit.
SHORT_HORIZON_SIZE_COMPOSITION_TEST.md strengthens the scalar
counterexample to any prescribed positive horizon and any prescribed
shorter controlled interval; a separate fresh audit is in progress.
Do not promote either pending claim from the already completed audits.
Exact frozen hashes and reviewer assignments are in REVIEW.md and the
destination research journal. The full theorem remains open.

## Final certification of this cycle: direct canonical positive-time estimates

The pending statuses in the preceding update are superseded.
CANONICAL_TINY_READOUT_RARE_PATH.md and the corrected
CANONICAL_FRACTIONAL_GATE_HIERARCHY.md have passed a complete isolated
audit of the entire chain, including all eight explicit dependencies.
The direct actual/pruned comparison uses the SAME prescribed
\(W^{(4)}_0=G^{(4)}/n\); no evolved zero-to-tiny transfer is assumed.
It proves the rare derivative, residual, energy, maximal-path prefix,
full-state comparison, and relative accumulated rank-memory estimates.

Conditional on all hidden initialization, the actual initial query
has covariance at most \(M^2n^{-2}I\). A simultaneous subset bound,
proved before intersecting the readout good event, gives
\[
\frac{\|P_Eq^{(2)}(0)\|_2^2}{n}
\le Cn^{-2}[h(|E|/n)+\epsilon_n^2].
\]
The nonzero initial boundary contributes \(CtI_E\) to rare energy
and unsuppressed initial mass to the query prefix, where \(I_E\)
is the left side above. This leads to the direct weighted estimate
\[
\frac1n\sum_iw_iq^{(2)}_{*,i}(t)^2
\le C\left[(t^2+n^{-2})
\{h(a)+\epsilon_n^2\min(1,na)\}
+t\int_0^t\mathcal I_n(a,u)\,du\right],
\quad a=\frac1n\sum_iw_i,\quad 0\le w_i\le1.
\]
Every weight vector is allowed on the common all-set/time event.
All trained blocks are retained. Constants are uniform for one
prescribed common clipping, not a simultaneous event over all maps.
For \(M=10,\eta=1/n\), the event probability tends to one and
\(\epsilon_n\to0\). The comparison histories remain on the right side.

SHORT_HORIZON_SIZE_COMPOSITION_TEST.md also passed its separate
complete isolated audit. For EVERY prescribed \(T,C>0,C_0\ge1\)
and \(0\le L<T\), its exact finite-floor scalar family satisfies the
resulting hierarchy with zero width error and uniform deletion
continuity through \(L\), yet has a strictly positive singleton and
iterated small-deletion limit at \((L+3T)/4<T\).
This excludes sufficiency of the scalar hierarchy even on arbitrarily
short horizons; it does not assert realizability by canonical dynamics.

Claim rung: newly controlled actual canonical relative query/path
estimates, plus a scalar route obstruction. Cycle status: PROGRESS.
The requested uncut population continuation, restartability, full joint
limit and observable contract remain unproved and unrefuted.
Exact final hashes and correction provenance are in REVIEW.md.

## Actual signed top-curvature estimate

ACTUAL_TOP_POSITIVE_CURVATURE_BOUND.md now has a complete isolated
scoped PASS. Its final proof hash is
af07fcbd7f937206858e942aa2b9e728734db908205112227191d54c1fd09c4c;
its final review hash is
629e595fdab4ce0350f542ef3793cffe3685939820d0a69c5a7cc59736d62b80.
For feature time \(s\le S\), the actual canonical trajectories satisfy
\[
\mathbb E\left[\frac1n\sum_i\sup_{0\le u\le s}
[W_i^{(4)}(u)\phi''(z_i^{(3)}(u))]_+\right]
\le C_S(n^{-1}+s^5).
\]
The same bound holds on an explicitly proved initial-norm event with
exponentially small failure probability, simultaneously for all fixed
middle masks and all prescribed dominated 1-Lipschitz clippings.
No adaptive Gaussian-path event is needed for this particular estimate.
Its deterministic zero-readout version is \(C_{S,M}s^5\), uniformly
over width and initial hidden operator norms at most \(M\).

The argument uses actual sign lag and integrated actual top velocity,
not a Taylor jet. After bounding the initial-readout contribution
separately, positivity of the accumulated-readout contribution requires
its sign to disagree with the current preactivation. This controls
the positive trace of the Euclidean top-input Hessian, with
the essential output factor \(1/n\). It does not transfer the same
scale to the RMS operator norm or to a transported response's work.
Conditional second-moment/alignment information is still missing there.
In particular, \(q^{(2)}\phi''(z^{(2)})\), the problematic middle
coefficient, is not controlled by this top-layer result. The full
canonical global theorem remains open. This is a scoped actual
positive-time estimate, not a conditional replacement for that theorem.

Its independently audited companion ACTUAL_TOP_CURVATURE_SIGN_LAG.md
has proof hash
3bc7787c0da406fe06503f5cc91ca350e53df918d4581dfb66eabfde596a0925
and review hash
b192b3e8228c99d3a2e769c148828b028606bae937d29abd48f17992117fd74d.
A compact deterministic width-two family, started at exactly zero
readout and evolved with every canonical parameter block trained,
has a strict top-coordinate sign lag. At \(s_\epsilon=2\sqrt{\epsilon/L_0}\),
\[
\frac12\sum_{i=1}^2
[W_i^{(4)}(s_\epsilon)\phi''(z_i^{(3)}(s_\epsilon))]_+
\ge \frac{L_0^2}{768}s_\epsilon^5,
\qquad L_0>0.
\]
Uniform fixed-width Taylor remainders and a common existence interval
are proved, so this is an actual positive-time witness. It rules out
coordinatewise nonpositivity and any deterministic uniform \(o(s^5)\)
improvement over that compact zero-readout family. The corresponding
physical-time statement uses the exact clock \(ds/dt=2(1-f)\).
The first layer is the canonical vector, not an auxiliary matrix lift.

Openness gives a positive-probability event at fixed width two under
the full canonical Gaussian law, with readout near zero, and separately
under its deterministic-zero-readout variation. No probability bound
uniform in width or shrinking time is proved. The construction does
not prove Gaussian-expectation sharpness, population failure, or failure
of the requested theorem. Both scoped results are now certified;
the main continuation gap and complete local theorem are unchanged.

## Actual canonical middle positive curvature: complete two-note PASS

The initial-law and actual-time notes are now jointly certified:

- GAUSSIAN_MIDDLE_CURVATURE_INITIAL_LAW.md:
  e028b6146db23f21ba0b35a876e997ff20d89ab3da8edcaa8f3e11e7db1417bb.
- ACTUAL_CANONICAL_MIDDLE_POSITIVE_CURVATURE.md:
  9f0b1a3c6cc334e533e0623d5d2e15413324037f7887914874f08e91a320a23e.
- ACTUAL_CANONICAL_MIDDLE_POSITIVE_CURVATURE_REVIEW.md:
  e94f48cb01b0fa0997915072da35e65fb6afda2816787b3d859bee390054b153.

Define \(u_n^{(2)}=(W_0^{(3)})^T[\phi'(z_0^{(3)})\odot\phi(z_0^{(3)})]\).
The joint empirical law of \((z_{0,i}^{(2)},u_{n,i}^{(2)})\) converges
in probability and \(L^1\) for every continuous test of at most quadratic
growth. Its population second coordinate is
\(\beta\phi(Z^{(2)})+\sigma G\), with \(\sigma>0\) and \(G\)
independent of \(Z^{(2)}\). This is the response forced by the earlier
forward query plus unexplored conditional Gaussian randomness, not
independence of the original reused coordinate outputs or a new seed.
In particular
\[
c_n=\frac1n\sum_i[u_{n,i}^{(2)}\phi''(z_{0,i}^{(2)})]_+
\longrightarrow c_*>0
\]
in probability and \(L^1\).

For the actual trajectories started at the prescribed tiny readout,
let \(B_n(s)=n^{-1}\sum_i[q_i^{(2)}(s)\phi''(z_i^{(2)}(s))]_+\).
An exact Duhamel calculation proves
\[
|B_n(s)-s c_n|\le C_S(n^{-1}+n^{-1/2}s^2+s^3),\quad 0\le s\le S,
\]
on a common high-probability initial-norm event; the same bound holds
in expectation. The proof keeps every trained term and directly bounds
the nonzero initial query. It is not a zero-readout flow comparison
or a finite-jet transfer. Constants and the event are uniform over
all prescribed fixed dominated 1-Lipschitz clippings.

There is a fixed \(s_0>0\) such that, for every fixed \(0<a\le s_0\),
with probability tending to one, simultaneously in those clippings
and all \(s\in[a,s_0]\), one has \(B_n(s)\ge c_*s/2\).
A fixed positive fraction of coordinates have
\(q_i^{(2)}(s)\phi''(z_i^{(2)}(s))\ge c_*s/4\).
Thus top-layer fifth-order suppression does not extend to this middle
coefficient. The width limit followed by the small-feature-time limit
of \(\mathbb E B_n(s)/s\) is \(c_*>0\).

No fixed-positive-time population law follows from the retained
\(C_Ss^3\) error. The positive fraction concerns scalar coefficients,
not full-Hessian eigenvalues or their actual-response quadratic form.
No positive Gronwall bound is refuted. The global continuation,
restartability and joint exact-GD/MF/GF target remain open.

### Auxiliary residence-time inference: rejected, not a canonical result

MIDDLE_RESIDENCE_TIME_TEST.md passed a complete isolated audit. It is
a prescribed-input auxiliary ODE, not the actual trained network.
Its fixed mobility is \(I+vv^{\mathsf T}\), with norm three and
strictly positive scalar part. Its query starts at zero and has
width-uniform normalized Euclidean query and derivative bounds.
All normalized state and velocity bounds hold on each fixed horizon.
Nevertheless coherent bulk motion holds one coordinate at positive
curvature throughout positive times, and its actual coupled response
grows as \(\exp(c_S\sqrt n)\). An independent bounded Gaussian source
with zero initial response gives the same failure; the review also
verifies a source vanishing linearly at zero.

Thus temporal RMS bounds plus positive bounded mobility alone do not
supply a residence or response-amplitude estimate. No trained upper
query, evolving lower mobility, canonical initialization event, or
canonical response law is constructed. No network failure probability
or global-theorem conclusion follows. This cycle made no new canonical
continuation estimate and is recorded as NO_CANONICAL_PROGRESS.

Proof SHA256:
ed8826fbddbaa0f7710f0fcd0a8496dcb9819f02f75749fb380e437fc120eee0.
Review SHA256:
83b63b6a1a8cc75a70aff974938500fec14ad193676b0086960dcd340bef477f.
The full goal remains active and unchanged.

### Causal filtered-query approximation: complete scoped PASS

A complete isolated combined audit covers the causal filtered-query
algorithm, its deterministic canonical-clipped stability proof, and
the growing-clipping synthesis. The algorithm retains both initial
matrices and both orientations, all learned rank memories, and the
canonical Gaussian seeds including the tiny readout. Its two warmup
forward fields are noisy, not hidden exact initialization calls.

With feature mesh n^(-2), comparison noise n^(-1/4), and filter scale
n^(-1/8), two adaptive-martingale passes give actual effective rank
O_S(n^(11/12) log(e+n)^(4/3)) and raw query errors divided by sqrt(n)
at most O_S(n^(-1/24) log(e+n)^(8/3)+n^(-1/4)).
The first pass uses the universal rank ceiling; it bounds this
algorithm's own states and time increments. The second uses the
resulting deterministic rank bound. No frozen-history independence,
resampling, or supplied true trajectory is used.

For a deterministic common clipping with cap R, the full evolving
state error against the canonical clipped finite-width feature flow
is bounded by C_(S,M)(1+R) exp(C_(S,M)(1+R)) times the sum of filter,
mesh, query and warmup errors. Feedforward filter contraction avoids
an exponential in the inverse filter scale. All pre-step trained
memories are retained. For any prescribed cap R_n=o(log n), including
caps tending to infinity, the combined mesh-state error is
n^(-1/24+o(1)) on events of probability tending to one.
The probability statement is for each deterministic choice of map
or sequence of maps, not simultaneously for every map.

This is a new causal finite-transcript approximation bridge to
canonical CLIPPED dynamics, not merely consistency on a supplied path.
It resolves the rank premise for this specified filtered algorithm,
even with identity in the rank statement. It does not resolve ranks
of the original unfiltered perturbed histories. Identity is excluded
from the bounded-clipping stability and diagonal-transfer statements.
Two growing-clipped trajectories being close does not remove clipping,
establish a common limiting law, prove autonomous restart, or give
the requested physical-time/exact-GD/kernel/velocity conclusions.
No primary-source multi-matrix distribution or complex-continuation
theorem is invoked to supply those missing implications.

Exact-hash certification:

- CAUSAL_FILTERED_QUERY_RANK.md:
  7406ffb9c24e8359e7e188c70eb3863ff5aeb9179df3d7bba92103b98aedcfd1.
- FILTERED_QUERY_CLIPPED_STABILITY.md:
  cecfa8670609c13b345d2c73f1a2c772082fe1253f684ab0db4e345d82b2094b.
- FILTERED_QUERY_GROWING_CLIP_TRANSFER.md:
  c1d5d50c8720cb3285c3aa15608b08cb9b0bfde968951c33cbe0338df1548fcd.
- CAUSAL_FILTERED_QUERY_COMBINED_REVIEW.md:
  4e700b4568df01f61ce41fdeb4a812b3db83c6d670331b5dec5defccd48582ed.

The root read the complete 801-line final combined report and verified
all candidate, dependency and review hashes. The final candidate-status
sentences are historical and superseded by this certification.
This cycle is SCOPED_COMPARISON_PROGRESS: an actual initialized
evolving-state bridge, not a new uncut tail bound or full resolution.
The original model, initialization, clock and observable target are
unchanged. No numerical experiment or source-task resumption occurred.

### Exact coupled Gaussian transcript law: complete scoped PASS

FILTERED_TWO_MATRIX_GAUSSIAN_LAW.md now has a complete isolated PASS,
including its application of the three frozen comparison dependencies.
The proof reconstructs every forward/transpose covariance for the
regularized causal rule, including the strict reverse triangle. An
elementary sequential Gaussian-posterior argument turns those frozen
covariance identities into equality of the actual adaptive joint laws.
Both interacting matrices and noisy warmups are included in one
chronology. No source distribution theorem, differentiability
assumption on the query maps, or complex continuation is needed.

This equality holds at every finite width and finite query count,
including the full growing mesh. It preserves all transcript-computed
registers, learned matrix increments, activations and middle queries,
jointly with the non-matrix seeds. It does NOT preserve the initial
hidden matrices as observed coordinates or provide a pathwise
identification between original and replacement processes.

In the replacement realization, the actual middle query is exactly
the response forced by previous Gaussian uses, plus the full trained
upper-memory shift, plus a fresh conditionally centered Gaussian vector.
On the high-probability tiny-readout event, the fresh vector has
conditional covariance at most (B_4^2+2 sigma^2) I, with
B_4=1+(S+1) pi/2. Every coordinate of the trained-memory shift is
bounded by (S+1)(pi/2) B_4^2. These are actual clipping-uniform bounds.
The remaining predictable response m_l^(2), displayed in candidate
(13), has NOT been bounded. No full-query tail estimate follows.

The growing-cap canonical comparison can be augmented by the maximum
ordinary middle-query error divided by sqrt(n), with no extra clipping
factor. Thus, for each prescribed admissible clipping sequence with
R_n=o(log n), expectations of bounded 1-Lipschitz tests of the whole
mesh state and middle query differ between the canonical clipped flow
and the replacement array by at most n^(-1/24+o(1))+2p_n, where p_n is
the preceding three-note failure bound. Both arrays depend on width;
this is not convergence to an identified population process.

Proof SHA256:
db98d04b7f92c8d341ab0e0f54defd845e37750decc0b8c62e33f1b278aecb33.
Complete review FILTERED_TWO_MATRIX_GAUSSIAN_LAW_REVIEW.md SHA256:
cd714a8ec227b630d0e9cbe8bba8e5d5f9938aea6f30808d2551d28a70d9ce87.
Root read all 387 final review lines and rechecked the proof and all
three dependency hashes. No required mathematical fixes were found.

Read the candidate tail bound with x>=0. Its statement that the full
query has no established Gaussian law means no UNCONDITIONAL Gaussian
law: conditional on its specified enlarged past, (15) is Gaussian with
the displayed predictable mean and covariance. Those conditional laws
do not transfer to the canonical filtration by the test comparison.
These two non-blocking clarifications are recorded without changing
the frozen proof. Coordinate independence, all-call tails, uniform
integrability and arbitrary tail-indicator transfer are not asserted.

Classification: SCOPED_REPRESENTATION_PROGRESS. The exact reduction
obligation is discharged for THIS filtered rule, not for unrelated
query algorithms. The next missing estimate is the actual forced
response, followed by a valid uncut continuation argument. Identity
is allowed in the exact law, not in its canonical clipped comparison.
The full physical-time/GD/MF/GF, restart, kernel and velocity theorem
remains open. The original unlimited goal stays active.

### Energy-compatible projection: new weak-source estimate, complete PASS

ENERGY_COMPATIBLE_LOWER_PROJECTION.md has a complete isolated PASS:
proof d2d10248021a9cb01ab8a6f2358ecfbef4ce6abdad8107654e00dfa38870abb5;
review ENERGY_COMPATIBLE_LOWER_PROJECTION_REVIEW.md
fe57cb8727b7042672777ba211468226bbe1d61c9406c0cf9c5479dabf9c09b8.
Root read all 777 final report lines and verified both final hashes.
The full nine-section note, not merely its projection lemma, is certified.

This is a new auxiliary family, not a change to the canonical target.
It uses the exact canonical initialization, upper updates and forward
constraints. Its lower field u_R is the projection of full delta^(2)
onto [-R,R]^n in the positive metric
M=||h^(1)||^2 I/n + W^(2) diag(phi'(z^(1))^2) (W^(2))^T.
The same u_R drives z^(1) and W^(2); no residual enters the field.

On one canonically initialized event of probability tending to one,
for all sufficiently large widths and every positive cap simultaneously,
the auxiliary finite-width flow is globally unique in feature time.
Energy, primal/operator bounds, positive first-layer activation norm,
and full-query time-RMS regularity are cap independent on finite feature
horizons. Prediction is increasing. The exact physical clock has a
cap-independent bound S_dagger on its total feature time.

The new source estimate is for the actual second-preactivation equation:
e_R=M(delta^(2)-u_R), (z^(2))'=M delta^(2)-e_R.
Projection complementarity gives the exact nonnegative work excess
u_R^T e_R/n = R ||e_R||_1/n. Thus
integral_0^S ||e_R||_1/n ds <= D(S)/R.
Every bounded measurable vector test and every empirical scalar
middle-coordinate test with bounded derivative has that same defect
bound. After multiplying by the actual physical clock factor, its
absolute integral over all physical time is <=D(S_dagger)/R.
This is an actual small source in one canonical equation evaluated
at the auxiliary state, not a comparison to a supplied true path.

At each fixed n, R>=sqrt(n) A3(S) B(S) makes the projection inactive
throughout [0,S]. With S=S_dagger the auxiliary trajectory is exactly
the canonical finite-width physical flow for every physical time.
The proved sufficient threshold grows with width; its necessity is
not asserted and no interchange of limits follows.

The new vanishing source is mean absolute/spacetime L1, NOT RMS/L2.
Its support can shrink while retaining squared energy; its work excess
need not vanish uniformly when width grows with cap. At fixed width
both are eventually exactly zero, as the last paragraph proves.
This is the review's optional scope clarification, recorded without
changing the frozen proof. The first two earlier proof versions are
superseded, not separately promoted.

No fixed-cap population flow for this nonseparable projection, uniform
state stability, uncut population limit, or full kernel/velocity/GD
theorem is proved. Existing coordinate-clipping theorems cannot be
applied to this different rule without a new argument.
Classification: SCOPED_AUXILIARY_SOURCE_PROGRESS. The original full
goal remains active, neither completed nor refuted.

### Metric-projection gate stability: complete scoped obstruction PASS

METRIC_PROJECTION_GATE_STABILITY_TEST.md, all 893 lines, now has a
complete isolated PASS at the corrected final proof hash
713f889141f56ee900c49e9b4478133035d8de7dd0156680869a73761a9b647a.
METRIC_PROJECTION_GATE_STABILITY_REVIEW.md, all 916 lines:
2fd070f36e56250a7be4e38b7cdf2e417ea7b52983e60ea0193d022d91663476.
Root read the complete final report and verified both hashes.
The formerly pending mapping audit is superseded. Its sole required
correction explicitly restricts the projection variational equivalence
to feasible u in the box; every application already checked feasibility.

For each fixed positive cap and fixed positive-definite metric M,
P_M(phi'(z) odot q) is globally jointly Lipschitz in (z,q) if and
only if M is diagonal. Fixed-metric nonexpansiveness in the raw input,
the q-only bound, and bounded-coordinate-q local bounds remain valid.
This does not contradict finite-dimensional local well-posedness.

The full Section 5 construction gives pairs of complete algebraically
valid network states at increasing widths. Both hidden operator norms,
all primal vector RMS norms, readout coordinate bounds and middle-query
RMS are uniformly bounded. Prediction stays in a fixed positive interval
below 1 for all sufficiently large widths. At each width the two lower
metrics are exactly equal with width-independent spectral bounds.
All forward and backward equations hold: the actual upper parameters
give delta^(3)=1 and the same q^(2)=(W^(3))^T delta^(3) in the pair.

The full input distance includes ordinary Frobenius hidden-matrix
differences, RMS input/readout and every hidden-state difference, and
prediction difference. It is Theta(1/n), while the projected middle-field
RMS difference is Theta(1/sqrt(n)); their quotient is Theta(sqrt(n)).
Adding q^(2) and delta^(3) differences does not help because both are
zero. The changed readout IS included in this distance. Including the
raw delta^(2) difference, using ordinary rather than RMS readout distance,
or projecting delta^(2)/n would be different claims not refuted by this
example. The residual remains outside every backward field.

These are deterministic static states, not the prescribed Gaussian
initialization, a reachable trained path, or a positive-probability
training event. The example disproves the proposed deterministic
primal-only uniform Lipschitz shortcut, not the canonical theorem,
all weaker stability moduli, or all enriched-state constructions.
The positive energy-compatible source theorem is unchanged. No fixed-cap
population law for its nonseparable rule or strong unclipping bridge
has been proved. Classification: SCOPED_STABILITY_ROUTE_OBSTRUCTION;
no canonical continuation estimate or counterexample follows.
All destination agents in this audit cycle are closed. Full goal ACTIVE.
