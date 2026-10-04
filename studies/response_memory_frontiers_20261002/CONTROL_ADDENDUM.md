# Controlled-flow candidate: clarifications after independent review

Date: 2026-10-02. This addendum leaves the frozen `CONTROL_CANDIDATE.md`
unchanged. It responds to the complete `CONTROL_PROOF_REVIEW.md`. Its theorem
is internally reviewed, not promoted established material.

The proof should establish the clock representation on compact subintervals
of a local maximal Caratheodory solution before applying the global bounds.
For a fixed order q the raw state is bounded on every such subinterval by
continuity. With rho_u squared equal to the sample mean of (u_a r_a)^2,
the inequality |u_a r_a| <= sqrt(m) rho_u implies that every raw velocity,
and every reconstructed physical velocity, is bounded by K_q rho_u there.
Hence ||theta(t)-theta(s)|| <= K_q[tau(t)-tau(s)]. The state and forward
features factor through Lipschitz functions of the clock, even when its
zero-speed set has positive measure and no interior. A generalized inverse
of the continuous nondecreasing clock defines measurable backward histories;
nontrivial clock fibers have a null set of clock values. This proves the
moment representations locally. The uniform physical and history bounds
then apply on the maximal interval and give global continuation through T.
This orders the proof without an additional assumption or a circular use of
global boundedness. Controls remain arbitrary bounded nonnegative measurable
functions, and all raw velocities vanish almost everywhere when rho_u=0.

The affine-history illustration in the candidate is an abstract statement
about orthogonal projection on an ordinary interval. It is not an exact
nonstationary example for the algorithm's constant forward prefix on [0,1].
A polynomial constant on that interval is constant everywhere. For example,
h(xi)=(xi-1)_+ on [0,2] has affine projection xi/2-1/4 and squared projection
error 1/24. Taking b=h gives pairing error 1/24. Constant forward features
still give exact reconstruction at every order, but that degenerate witness
does not demonstrate feature-learning utility.

For the finite-menu corollary, an empty surrogate feasible set means that
there is no selected certified action. If that set is nonempty but the
stricter true comparator set is empty, retention of the selected action is
still certified while the objective comparison is vacuous (minimum of the
empty set is +infinity). The theorem compares the same open-loop function
in both models; a common state-feedback rule is a different statement.

With B simultaneous trial branches, the shared hidden checkpoint must be
included in storage. Hidden-state savings against B independent dense
branches require 2mq/n < 1-1/B before workspace and controls. The moving
state comparison alone does not imply a one-branch total-memory saving.

The first pilot's preregistered gates were weaker than the intended mechanism:
accuracy and poor credit reconstruction could occur at different orders, and
the motion gate allowed either hidden layer rather than the compressed first
layer. The reported data do exhibit accuracy and poor credit reconstruction
at the same q=3 for every tested schedule, but the original feature-motion
gate does not establish first-layer motion. Only one closure was refined;
the first pilot therefore did not independently assess dense discretization
error. The next preregistration requires same-policy, same-order evidence,
first-layer motion in dense and memory trajectories, and refinements of both.
No first-pilot threshold or frozen text is retroactively changed.

The reviewed O(1/q) existence bound can have an impractically large exponential
stability constant. Empirical trajectory agreement and menu selection do not
provide the theorem's usable uniform certificate. The next test is an
empirical decision comparison, not certified safe control.

Sources: frozen candidate; complete independent CONTROL_PROOF_REVIEW.md;
CONTROL_PILOT_REPORT.md; own control_pilot.py. These introduce no new external
scientific claim.
