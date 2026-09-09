# Three hidden layers: active proof contract and evidence

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
