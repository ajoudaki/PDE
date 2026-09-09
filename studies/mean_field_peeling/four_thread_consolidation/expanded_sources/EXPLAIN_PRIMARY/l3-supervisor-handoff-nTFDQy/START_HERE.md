# L=3 proof supervisor handoff — 2026-09-05

## User authority and immediate handoff state

The user explicitly asked: "Can you create a supervisor thread to take
things from here in the PDE project remotely located on blackchatgpt
rather than here? you must pause all operations, and create a thread
there with sufficient background details and information to resume
your job, and then pause all sub agents here".

The source task is 01a04927-31c8-79d1-bd23-8196b13a1d9b, titled
"Explain audited proof result", on remote-ssh-discovered:black-chatgpt-2,
saved project PDE-2, cwd /home/amir/Codes/PDE. Its shell hostname is
ubuntu22-black, Unix user codex-b. Its research and subagents are paused.
Do not restart or message them to resume. The destination requested is
saved project PDE on remote-ssh-discovered:black-chatgpt, NOT PDE-2.
This is a NEW supervisor task, not a claim to have migrated the source
task, its goal object, or its entire conversation.

Your first responsibility is to verify destination host/project and
recover this bundle. Report the recovery status to the source
coordinator using send_message_to_thread with the source host and ID,
then remain idle for the short final handoff confirmation. After that,
resume supervision on the destination only.

## Exact requested result — unchanged

The original user asked for the complete unconditional rigorous
three-hidden-layer analogue of the audited two-hidden-layer joint
mean-field/gradient-flow theorem. They explicitly requested persistence
as a /goal, independent isolated adversarial reviews of the complete
proof, and no conditional substitute. A negative resolution would need
an actual counterexample to the canonical theorem. Failure of a
proposed proof method is NOT such a resolution.

The full all-finite-time theorem is STILL OPEN. The complete local
theorem is proved and independently audited; it is not the requested
global result. The source goal was active at handoff. Do not mark it
complete or blocked, or infer impossibility from prolonged effort.
No budget was imposed. No new computational experiment is authorized.
Work is mathematical; normal read-only checks and independent proof
agents are authorized.

Required conclusion: a finite number of fields/operators (these need
not be finite-dimensional scalar state), well-defined autonomous and
uniquely restartable population gradient flow; full-sequence joint
exact-GD/MF/GF convergence on every finite physical horizon; prediction,
loss, both directions of both hidden matrices, all four raw kernel
blocks, hidden paths and velocities, and nontrivial feature learning.
Do not weaken the initialization, activation, clock, or observable
contract. Exact full target is in CONTRACT_AND_LEDGER.md, first 35 lines.

## Canonical network

One input, target 1, phi(z)=arctan(z). Width n in every hidden layer.
z^(1)=W^(1) is a vector. W^(2),W^(3) are n by n matrices.
W^(4) is the RESCALED output-weight vector throughout.

z^(2)=W^(2)h^(1), z^(3)=W^(3)h^(2), h^(ell)=phi(z^(ell)).
f_n=(W^(4))^T h^(3)/n, r_n=f_n-1, L_n=r_n^2.
delta^(3)=W^(4) odot phi'(z^(3)).
delta^(2)=phi'(z^(2)) odot (W^(3))^T delta^(3).
delta^(1)=phi'(z^(1)) odot (W^(2))^T delta^(2).
The residual is NOT inside delta.

Independent initialization:
z_0^(1),i ~ N(0,1);
W_0^(2),ij and W_0^(3),ij ~ N(0,1/n);
W_0^(4),i ~ N(0,1/n^2).
Population output weight initially zero.

Exact raw GD has eta_n=n^-2:
z^(1)+=z^(1)-2 eta_n r_n delta^(1);
W^(ell)+=W^(ell)-2 eta_n r_n delta^(ell)(h^(ell-1))^T/n,
ell=2,3;
W^(4)+=W^(4)-2 eta_n r_n h^(3).
Physical t=k eta_n. Raw parameters linearly interpolated; hidden
objects recomputed; derivative conventions are in the contract.

F(z)=z+z^3/3, x^(1)=F(z^(1)) is an EXACT continuous-time
coordinate change, NOT an exact change of raw GD.
Feature time satisfies ds/dt=2(1-f):
(x^(1))'=(W^(2))^T delta^(2);
(W^(2))'=delta^(2)(h^(1))^T/n;
(W^(3))'=delta^(3)(h^(2))^T/n;
(W^(4))'=h^(3); (z^(1))'=delta^(1).

## Read order and authority

Extract proof-artifacts.tar.gz to a new private working directory;
do not overwrite existing remote files or assume equal /tmp paths
belong to the same filesystem/user. Its contents use relative paths.
The main directory is l3-full-resolution-9nbD4z.

Read in order:
1. This file.
2. CONTRACT_AND_LEDGER.md and CONTINUATION_ROUTE_REGISTRY.md in full.
3. NEXT_PROOF_OBLIGATION.md and REVIEW.md.
4. L3_LOCAL_COMPLETE_PROOF.md when using the established local theorem.
5. The exact route dependencies needed for the next new attempt.

The compact route registry prevents repeating exhausted calculations.
All four master files include the latest zero-readout-reachable
Hessian result. The newest Gaussian-action Lp draft is NOT yet audited
or entered into those master ledgers; see below.

The archive also includes the original L2 audited proof and its review
directory, L3_FIXED_MESH_SOURCE_IDENTIFICATION.md, and a few external
historical dependencies. L3_SELF_CONTAINED_PROOF.md is an INVALID older
easier-model/gapped attempt, NOT an authority. The repository's
studies/d3_arctan_closure_program uses O(1) readout and is a DIFFERENT
model. Never silently substitute either.

## What is already proved and what is missing

The complete local theorem has all local premises discharged, two
independent combined PASS reviews and a fresh complete-proof-only PASS.
L3_LOCAL_COMPLETE_PROOF.md SHA256:
f97148f84979ab5b8489927d477b6abb3d919e27fd457455f2e3b98416725de4.

For every fixed clipping level, the population flow is globally
wellposed and is the finite-width limit. Global finite-width GF/GD
optimization, coercivity, readout control, loss decay, and bounded
total feature time are also proved. They DO NOT establish the uncut
global population limit or its restartability.

The unresolved comparison term is
[phi'(z^(2))-phi'(z_tilde^(2))]
 odot (W_tilde^(3))^T delta_tilde^(3).
RMS bounds do not control this multiplication operator. A tail envelope
exp[-c R/log(e+R)] uniformly over actual clipped continuations would
suffice by an already proved Osgood argument. Its global premise is
open. Equivalent sufficient criteria are not progress unless an
actual canonical response is newly controlled.

Strong endpoints of an existing path are proved, but do not establish
existence or uniqueness after that endpoint. Fixed-mesh Gaussian
identification is proved, but cannot replace mesh-uniform continuation.

## Most recent completed results

INTEGRATED_INITIAL_QUERY_COMPRESSION.md:
SHA256 2c97e9fe8c4e9b3a66d7efdf80f825f8c7bb6275649518c47fc001aef6b57c73.
Full isolated audit PASS. Integrating delta^(2) makes all four initial
matrix arguments in the exact state equations time-Lipschitz:
h^(1), integral delta^(2), h^(2), delta^(3). All trained rank memories
are retained and have explicit uniform-path continuity bounds.
Sampling the actual path does NOT establish finite-transcript
measurability or autonomous approximation stability. The bad multiplier
remains; velocities/first kernel also need a derivative bridge.

ACTUAL_ZERO_READOUT_REACHABLE_HESSIAN.md:
SHA256 59b2bc2d3ee1fcfd3f4f118780b624986fc01aa4f2f7d7a8cea2eec18ca88b93.
Full isolated audit PASS without corrections. A positive bulk channel
makes the rare-coordinate material-Hessian witness reachable from
exactly zero readout in uniformly bounded positive feature/physical
time. Primal norms are bounded on the whole segment; full Hessian B
is bounded at the terminal state only. Nevertheless a unit Rayleigh
quotient of B'-kappa B^2 is at least c epsilon^2 n-C_kappa for every
fixed kappa. Physical clock corrections are bounded, with the same
failure. This refutes a primal-only deterministic pointwise signed
bound EVEN on zero-readout-reachable trajectories.
Initial hidden states are deterministic and correlated, NOT the
prescribed independent Gaussians. No typical-Gaussian or population
failure, or failure under extra Hessian-history assumptions, follows.

The Gaussian comparison route has four audited notes:
PANAHI_EULER_PERTURBATION_SIZE.md: frozen time-regular histories give
small raw/integrated perturbations even K~n^2, sigma=n^-1/4.
PANAHI_CAUSAL_ADAPTATION_ISOMETRY_TEST.md: frozen isometry is false
for causal histories; correction still vanishes in its example.
PANAHI_ADAPTIVE_GRAM_MARTINGALE.md: adaptation IS controlled by a
two-half-step matrix martingale under actual effective rank
r log^2(n)=o(n). This estimate is proved, not still an open suggestion.
PANAHI_SMALL_JITTER_RANK_INFLATION.md: vanishing sigma-scale jitter
can make actual ranks full and integrated forcing macroscopic.
The actual trained rank premise AND nonlinear removal remain open.
Primary source's complex-continuation claim is unproved and unused.
Nishiyama--Imaizumi's noiseless theorem is genuinely global but no
valid reduction of this trained nested architecture has been proved.
Exact sources, hypotheses and hashes are in the master notes.

## Pending work at the exact pause boundary

GAUSSIAN_ACTION_LP_OBSTRUCTION.md was just produced by
l3_gaussian_action_lp_test. The user paused work before the root could
read it or commission an isolated review. Treat it as UNVERIFIED.
The agent was interrupted. No local agent should resume.

Its reported construction uses only three calls to W_0^(3) and its
transpose, no extra independent output seed:
Y=W_0^(3)1; e_epsilon=psi(Y/epsilon), even smooth compact bump;
v_epsilon=E[e_epsilon^2];
q=(W_0^(3))^*e_epsilon= sqrt(v_epsilon) G;
h_epsilon=tanh(q/sqrt(v_epsilon)).
Claimed next forward population law:
W_0^(3)h_epsilon = sigma H +
   c e_epsilon/sqrt(v_epsilon),
c=E sech^2(G)>0, sigma^2=E tanh^2(G), H independent of Y.
This would imply Lp norm >=const epsilon^(1/p-1/2) for p>2 despite
bounded input, ruling out a WHOLE-SPACE L-infinity->Lp or Lp->Lp
shortcut on the canonical generated action space.
Coordinate-map Lipschitz constants grow with epsilon; it is not a
trained-trajectory counterexample. Verify both the exact conditioning
and common-space inclusion. Audit with a fresh-context agent shown
only the candidate and explicit dependencies before promotion.

## Research discipline and user exposition requirements

Use solve-math-rigorously and investigate-conjectures skills, including
their required references, when resuming. Use teach-technical-math
for explaining the source. Read skill instructions yourself.
Do not spawn agents to interpret skill instructions for you.

Agents reviewing a candidate must be isolated (fork_turns:none), see
only the proof and explicit dependencies, and be asked to seek gaps.
Fix and repeat until clean. A lemma PASS is not a full theorem PASS.
Maintain source version/status and exact hash provenance.
No new numerical experiments are authorized.

The user is an ML theory researcher, not a functional analyst. Use
canonical W^(ell), z_k^(ell), h_k^(ell)=phi(z_k^(ell)); always retain
layer indices and write phi' explicitly. Finite transpose ^T,
population adjoint ^*. Use ordinary norms and explicit 1/n and
1/sqrt(n), no redundant aliases or normalized-inner-product notation.
Finite lower-case coordinates, population capitalized coordinates.
Keep neuron populations separate. After matrix reuse, prove joint
empirical-average convergence; do not claim finite coordinates iid
or call the argument a CLT. Give concrete forward/transpose examples
before abstract induction. Few headings, cohesive derivations,
minimal new symbols, no boxes, and no conditional result presented
as the full goal. Explain that new reused-matrix output equals the
response forced by previous uses plus unexplored Gaussian randomness.

## Safe continuation protocol

Do not repeat exhausted routes listed in the registry. Choose a
genuinely new canonical estimate or actual counterexample route.
Do not alter the model to obtain an easier theorem. Preserve unrelated
Git/user changes; no commits, branch switches, destructive operations,
or source-task migrations are requested. Research files can live in a
private writable directory on the destination.

The source task is intentionally paused by the user. The old goal
object is not transferred by creation of this new supervisor, and no
tool has marked the mathematical goal achieved or blocked. Continue
the user-authorized research only from the destination after confirming
the handoff.
