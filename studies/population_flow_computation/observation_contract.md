# Named observations and the current proof boundary

At a reached physical node t and a finite requested list U=(u_1,...,u_r), use
Euclidean metrics on the following SAME-layer joint tuples, and W2 between
their laws. The first coordinates g,w are two-component vectors.

    Layer 1: (g,w(t), H0(U), H(t,U), Q(t,U), A0*D(t,U), K*D(t,U)).
    Layer 2: (c(t), Z0(U), Z(t,U), V0(U), V(t,U), D(t,U),
              A0 H(t,U), K H(t,U)).

The typed learned-action terms are recovered from saved rank history:

    K H_u = sum_p gamma_p D_p <H_p,H_u>_1,
    K*D_u = sum_p gamma_p H_p <D_p,D_u>_2.

Subtract these from Z and Q to obtain the initialized-action fields. There is
no comparison of operators on unlike spaces and no pairing of a lower neuron
with an upper neuron merely because both arrays have P rows.

Requested tolerances are: prediction epsilon_f; W2 epsilon_1,epsilon_2 for
the two named tuples; and absolute epsilon_M for their named second moments,
including <H0_i,H_j>, <V0_i,V_j>, both squared hidden displacements,
cross-input pairs at the same neuron, <D_i,Z_j>, and <H_j,Q_i>. Gaussian
reuse requires these joint tuples, not their separate marginals. In the clean
limit the latter two link contractions obey actual adjunction after including
the same learned increment. Noisy training answers instead have the explicitly
derived s^2(beta-alpha) correction; it must not be tested against zero.

At a fixed numerical graph, append any finite list of retained H/D history
coordinates and centered source coordinates of the matching population to
the tuple. The generated_error_proof.md coupling and elementary W2 estimate
then control that entire finite joint law as P tends to infinity at fixed s,
with scalar-operation error tending to zero. The ideal source program retains
all formal source names, including duplicate inputs and singular clean Grams.
Response coefficients in the finite updates are weighted averages of those
same histories and directional fields. The one-direction probe fields are
auxiliary numerical variables; they are not a new physical population state
whose full history is asserted to converge as time is refined.

The implementation's paired_hidden_draws provides current/initial hidden
tuples and D/Q draws at a checkpoint; the other actions are the finite rank
contractions above. Its complete training histories are accessible in the
checkpoint. Multi-time passive joint draws across separate checkpoint calls
are not implemented: separately reseeding each time would not establish their
joint law. For any later extension, saved state snapshots, a single joint
Gaussian extension and all snapshot storage must be included explicitly.

Reached restart itself is implemented from current w,c,v_w,v_c, both entire
source/field/probe/innovation histories, covariance factors, physical step and
law configuration, rank weights and five full random-stream states. It does
not replay a missing trajectory or reset Gaussian reuse. It was checked
bitwise on the recorded numerical environment.

The full requested population contract -- uniform physical time through 40,
whole-circle prediction error with a computable useful resource rule, and
the prescribed internal tolerances under the same refinement -- remains open.
Fixed-graph joint convergence and the exact-state noisy-to-clean comparison
are separate proved/draft components; the implemented API does not yet accept
(epsilon_f,epsilon_1,epsilon_2,epsilon_M,b) and return a certified resource
choice. In particular no measured moment in validation is presented as a
certified population moment.

For clean passive D/Q observations, use the law-level two-stage Gaussian
recoupling in generated_theorem_check.md Section 4 and proof_corrections.md.
The numerical eigenvector factors need not converge under an identical raw
query seed. Their conditional laws have the required singular-covariance
continuity; passive Q has a weaker bound than the training graph. This does
not affect bitwise restart of an identical saved numerical state.

The delivered arithmetic backend supports float32 and float64 only. It does
not implement the arbitrary precision, certified elementary-function residuals
or certified Gaussian primitive coupling in the fixed-graph proof's precision
statement. That conditional arithmetic statement must not be described as an
implemented arbitrary-accuracy resource rule. This is a separate implementation
gap even if the exact-arithmetic statistical and time/noise limits are supplied.
