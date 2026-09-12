# Complete isolated adversarial mathematical review A — candidate v3

Reviewer: /root/adversarial_a_v3. Review date: 2026-09-12.

Final verdict: **PASS for the exact frozen mathematical addition and scope edits.**
No required mathematical correction or unresolved objection remains in this
review. This verdict concerns the specified finite nonlinear episode and its
iterated finite-GF capture. It is not an integration review, permission to
promote, a changed-law endpoint theorem, or a quantitative width estimate.

## Assignment, independence, and actual input scope

I received only the fresh neutral assignment and its permitted packet. My
identity is distinct from the coordinator, three component authors, selector,
and all earlier reviewers listed in REVIEW_ASSIGNMENT_v3.md. I did not inspect
earlier candidates, corrections, reports, the study README, author components,
history, other studies, or other tasks. I did not communicate scientific
findings with another reviewer. I did not delegate any part of this complete
review. The packet was evaluated without a supplied desired verdict.

I read AGENTS.md and RESEARCH_WORKFLOW.md completely, using their independent
isolated review scope. I read solve-math-rigorously/SKILL.md and
investigate-conjectures/SKILL.md, and the latter's research-contract,
adversarial-audit, and decisive-experiments references. The latter reference
was applied to the expressly authorized deterministic certificate, not to a
training experiment. No external theorem was imported, no guide link was
followed, and no external scientific retrieval was needed.

The only writes were this original report and files in
data/generated/nonlinear_prediction_selection/adversarial_a_v3/. I made no
Git operation and no established-file edit.

## Complete read coverage and truncation repairs

The following are actual complete readings, including the proof bodies,
not a list of files whose existence or hashes alone were checked.

| Frozen input | Complete lines read | Actual reading and repairs |
|---|---:|---|
| REVIEW_ASSIGNMENT_v3.md | 1–97 | Complete first read. |
| CANONICAL_ADDITION_v3.md | 1–2329 | An initial batched output was truncated. I repaired it with complete 1–330 and 331–950 reads, then read 951–1590 and 1591–2329 in full. |
| PROPOSED_EDITS_v3.json | 1–16 | Complete reread after the initial batch truncation. |
| PROPOSED_GUIDE_v1.md | 1–285 | Complete full output; then exact comparison with the frozen guide. |
| DEPENDENCIES_GLOBAL_v1.md | 1–8901 | Read 1–1100; repaired that output's central truncation by overlapping 380–465 and 465–650 reads. Then read 1101–1700, 1701–2300, 2301–2900, 2901–3500, 3501–4100, 4101–4700, 4701–5300, 5301–5900, 5901–6500, 6501–7100, 7101–7700, 7701–8300, and 8301–8901, all completely. |
| DEPENDENCIES_GAUSSIAN_v1.md | 1–550 | Read the full file; its center was truncated. Repaired with complete overlapping 145–184 and 180–390 reads, covering the conditioning-to-common-carrier transition and source proof. |
| DEPENDENCY_GUIDE_v1.md | 1–284 | Complete full output. |
| DEPENDENCY_NOTATION_v1.md | 1–98 | Complete reread after the initial batch truncation. |
| DEPENDENCY_MANIFEST_v1.json | 1–44 | Complete reread. |
| REVIEW_MANIFEST_v3.json | 1–42 | Complete reread. |
| verify_reference_certificate.py | 1–58 | Complete reread, independent execution, and exact comparison to the included dependency code. |

The global excerpts explicitly contain source ranges 1840–2461,
2462–3440, 3836–4947, and 5269–11439 of the named source version.
The Gaussian excerpt explicitly contains 3785–4326. Those are the packet's
frozen excerpts; I did not open the live source files to widen the scope.
The packet includes more established claims than the new theorem needs. I
read those included bodies, but the dependency conclusions used for my
verdict are identified below. Unrelated chapter descriptions in the guide,
and source portions absent from the packet, were context rather than
unrestricted whole-book audit targets.

## Mathematical contract and normalization audit

The object is the actual bias-free network with two tanh hidden layers:
u=x/sqrt(2), h1=tanh(W1 u), h2=tanh(W2 h1), and f=(W3)^T h2/n.
The entire first row has two independent standard Gaussian coordinates.
The stored initialization variances are 1, 1/n, and 1/n², respectively,
with all entries and blocks independent. The mobilities are (n,1,n).
The objective is the unhalved probability mean of squared residuals and
t is physical GF time.

I derived the block updates from this normalization. The first and readout
loss derivatives carry 1/n, canceled by their mobility n. The middle
derivative remains a rank uv^T/n. Thus the scalar prediction gradient
in the raw metric is exactly

g_u = (phi'(w.u) Q(u) u, delta(u) tensor H1(u), H2(u)).

The finite squared metric is
||dW1||F²/n + ||dW2||F² + ||dc||2²/n. The corresponding population
metric uses row L², increment HS, and readout L². Only K=A-A0 is HS.
The actual adjoint of A0+K is retained in Q. There is neither a hidden
rescaling of the middle block nor an independent reverse Gaussian matrix.

The parameter rectangle is closed and compact, with nonempty interior
in the two atom parameters; the open family claimed in the guide is
supplied by that interior. It is not an open neighborhood in the space
of all probability laws. Its added direction is distinct from and
nonantipodal to the two axes, with both coordinates nonzero. Its labels
are in [3/8,5/8], so the bounds use labels of absolute value at most one.

The limiting state is an infinite-dimensional raw operator/field state.
No finite scalar closure is claimed. Its coefficients depend on the
current state, atom, and initialized action. The reference endpoint is
prescribed by a separately constructed autonomous feature equation, not
by an oracle for the unknown contaminated trajectory.

## Established dependencies actually used and checked

### Gaussian law, singular queries, and canonical actions

I checked III.F.1–III.F.11 in the supplied Gaussian body. The conditional
matrix formula is the minimum-Frobenius-norm solution of WV=Y and W^T U=Q
plus the Gaussian residual on the doubly orthogonal subspace. The adaptive
conditioning induction conditions each input on the old transcript before
revealing its answer. This is the relevant justification for matrix reuse.

In the nonsingular step, the fixed-rank projection of fresh output noise has
expected normalized squared norm rank(U)/n. Removing that projection yields
the claimed joint empirical law and second moments; conditional independent
fresh coordinates supply the bounded-test variance estimate. The source
response formula follows from Gaussian integration by parts and cancellation
of the old forward projection terms, with uncentered input Gram matrices as
centered source covariances.

For singular Grams, fresh independent noise on each query input gives a
positive Schur complement at each fixed noise level. Same-array RMS errors
are bounded before that noise is removed. In the scalar recursion the
positive-semidefinite square roots, rather than pseudoinverses, converge.
The deterministic derivative envelopes make expected named derivatives
continuous in this fixed-graph limit. Separate formal names remain meaningful
on singular support, although individual transverse derivatives need not be
determined by the unforced value law alone.

The countable union of programs and their joint laws gives the prescribed
generated spaces. Bounded action inequalities and exact finite transpose
pairings pass to the dense span, then its L² closure. III.F.8 gives the HS
rank norm and pairing identities used by every matrix comparison here.
III.F.9–10 prove strong multiplier and curve differentiation rules, and
the scalar weighted Taylor argument proves the true scalar raw gradient.
These suffice without an ambient L²-valued Frechet derivative.

The global excerpt's A.1–A.2 supplies the extra fixed-program value and
named-derivative extension for unbounded backward products. I checked the
causal clipping order, linear value envelopes, polynomial source-derivative
envelopes, finite Gaussian moments, and uniform integrability at each fixed
graph. No uniform growing-transcript statement follows from that lemma
alone or is used as such by this candidate. A.3 proves the initialized
canonical action bound two by Gaussian comparison and Poincare; its
finite high-probability bound is sufficient for the finite proofs.

### Reference clock, fitting, endpoint, and full-row capture

The needed reference construction is B.1 specialized to two orthogonal
axes, tanh, and half the sum-loss mobility constants, together with
C.4.5.1. I checked that the transformed clock field is Lipschitz on
bounded same-root clock/action/readout sets, the readout supremum and
action bounds prevent finite feature-time escape, and the scalar
representation returns the actual raw equation. HS increment convergence
uses the same rank inequality as the operator proof.

The reference symmetry is a symmetry of the generated joint law, giving
f(e1)=b=-f(e2) and f(Pu)=-f(u). It is not asserted for an individual finite
sampled network. The exact feature equations imply
b_s=||h||²+||J* c||²=||theta_s||raw². The convexity calculation for
||c|| gives b_s>=m, with m>=1/10 furnished by the certificate.
Hence a unique first b=1 time exists by feature time ten.

The physical clock ds/dt=2(1-b) has the correct mean-loss factor. Its
inverse diverges at the first fitting level because b_s is bounded
on that compact segment; the physical residual remains strictly positive.
The estimates e(t)<=exp(-t/5) and
||theta_*(t)-theta_dagger||raw<=sqrt(10)e(t) then follow from the
feature energy identity and Cauchy–Schwarz. The resulting bounds on
A,c,w and the 76 input-Lipschitz estimate are exactly those used in B.
The swap symmetry makes the predictor vanish on the bisector.

C.4.5.2 proves the quantitative fixed reference source cap by finite
fresh-answer forcing, width first, source extraction, and forcing second.
I checked the root-clipping argument and the difference between derivative
continuity at a fixed graph and the later mesh-uniform pulse estimate.
The readout remains bounded under forcing because tanh stays bounded;
no energy identity is presumed for a forced program. Gaussian-plus-bounded
query representations pass to the existing feature flow by the cross-program
source isometry. B.1 and C.4.5.2–3 provide actual finite reference capture
on each separately fixed physical horizon, including paired observations,
with the actual small Gaussian readout.

### Whole-reference query envelope used for endpoint independence

The needed additional input is C.4.6.S40–S44. I checked its included
finite cavity argument S11–S39 rather than assuming a norm bound implies
the envelope. Deleting one initialized column keeps the learned K,
residual feedback, and both matrix orientations. The difference estimate
uses the full A in the first reverse-error term; its remaining cavity
Gaussian probe is conditionally independent of the deleted column.
The conditioning event is the cavity-good event, not an event depending
on that column.

The time/input L²-Lipschitz cavity fields give a Gaussian increment metric.
The supplied dyadic grid and scalar union bounds prove the Gaussian
maximum moment bound. The column-deletion stability estimate then transfers
it to the actual reference query coordinate. The auxiliary finite feature
flow on [0,10] has elementary bounds independent of fitting and width.
Its fixed-mesh width capture, followed by mesh removal, transfers every
finite rational query list. Bounded tests and monotone convergence give
the one countable envelope N with ||N||p<=C_* sqrt(p).
L² continuity extends each deterministic query equivalence class, and
Fubini gives the simultaneous active-clock bound. No independence of N
and the Gaussian first roots is established or needed.

### Raw cutoff, source recursions, and approximation interfaces

The one-reference comparison in C.4.1, its HS upgrade in C.4.7.2, and
the complete C.4.7.N5–N8 source recursions were checked. Each lower
cutoff appears additively; bounded adjoints and gates do not multiply
the cutoff into a power growing with depth. The source proof retains
the mass of every old pulse and its distinguished current diagonal.
The raw-to-clock defect and differentiated defect estimates N32–N51
provide the specific algebra used in candidate A.4.

I also read all the contained continuation, response, and nonlinear
variation proofs through the end of C.4.7. Their fixed time 40
changed-law conclusion is not a premise that grants this candidate
existence on 1/epsilon horizons. The new construction in C.6 must and
does supply that bridge separately. The homogeneous tangent propagator
and finite data-derivative theorem of C.4.6 are not substituted for a
nonlinear flow or used to extrapolate a Taylor series to slow times.

## Adversarial attacks on the new proof

### A. Integrated-control source cap: PASS

I attacked the source theorem with vanishing reference coefficients,
genuinely new controls, cancellations within an interval, duplicate
inputs, singular covariance, many old slots, passive diagonals, and
large physical pauses.

The common measure ds=sum_j(|a_j|+|a_*j|)dt is legitimate for
deterministic integrable controls. Flat parts have no state change.
Exact integrated coefficients have total mass at most 2L_*+q, and
their difference mass is at most q even when coefficients change
sign inside a cell. The normalizing mass m_p=|gamma_p|+|bargamma_p|
gives |gamma_p-bargamma_p|/m_p<=1 and sum m_p e_p=q_disc.
This avoids division by a zero reference coefficient. If both vanish,
the slot is omitted or has zero propagation. If only the reference
coefficient vanishes, the injection costs m_p e_p and remains controlled.

CT12–CT16 are the differentiated finite causal program with coefficients,
covariances, contractions, and controls held fixed. The current c,w use
only the past. A current upper query has precisely one direct source
derivative; duplicate inputs do not create additional current terms.
Old passive calls were not used by an update and therefore have zero
future formal derivative. I checked the zero-control induction: its
lower pulse never injects, its alpha into later queries is zero, and
the only upper direct value cannot propagate through a zero update/F
coefficient. Padding consequently cannot accumulate a spurious row cap.

CT17 uses cross-program input contractions on the finite union and
gives the exact Gaussian difference norm. It is not a claim that a
covariance square root is Lipschitz at rank loss. The branch's expression
uses its own named slots, while cross covariances couple the two lists.
This preserves every old initialized source.

The reference raw anchor is not obtained by reparametrizing raw Euler
as exact clock Euler. CT18 first has a bounded-clock Lipschitz
comparison with bounded c and K on feature length at most ten.
Fresh-answer forcing changes later observed fields by the original
source mass times a mesh-independent constant. The A supplement
justifies the width-first and forcing-second extraction of CT21:
root clipping makes the fixed program admissible, source derivatives
have an envelope independent of that root clip, and finite covariance
square-root continuity removes the clip. The inserted fresh root
enters as slot+qz, so E[zV^q]=q E[partial_slot V^q] at each fixed q.
This also works at a variance-zero slot.

For raw Euler, CT22–CT23 follow by differentiating the canceled Taylor
integral, not by estimating the exponentially large primitive terms
separately. After division by the injecting mass h_s/2, the direct
defect is O(h_s). Later normalized pulses have bounded fixed moments,
and sum h_k²<=L_* h_max. In transformed lower pulses the propagation
has bounded clock gates and deterministic D rows, with no Q multiplier.
The resulting CT25 is causal: current alpha precedes current beta,
and only earlier raw Q caps enter. A sufficiently small fixed mesh
therefore transfers the clock cap to raw reference Euler.

For the changed controls, CT26 supplies raw bounds independently of
the cap. Under a temporary beta cap, Q=zeta+J has Gaussian variance
bounded by L² and |J|<=B+L³. Jensen applied to the integrated absolute
query sum, rather than its maximum, proves CT28. The normalized lower
pulse envelope CT29 then has all fixed moments. The upper derivative
row equations give pointwise row bounds and the old-source density
bound CT31.

I checked that raw proximity CT34 precedes the changed-program cap.
The update subtraction CT33 puts all coefficient changes against
bounded gradients; only reference controls multiply gradient differences.
Consequently only the two already bounded reference-axis tails enter.
The Gaussian tail beats the linear cutoff amplification and yields
Phi(q_disc)->0 with no mesh-error floor.

The transport estimate CT36 retains every old source mass. In CT40,
the direct discrepancy costs e_p; update coefficient changes sum to
q_disc. The explicit product subtraction requires at most three
L12 factors and an L4 amplification factor. Interpolating L2
differences with the temporary L24 bound gives exponent 1/11;
bounded gates give exponent at least 1/6. Both support the stated
weaker 1/16. The deterministic D-row sum permits Minkowski before
summing past-gate differences, without a random maximum of query
differences. Summing over p uses sum m_p e_p=q_disc. CT43 then uses
pointwise upper derivative row bounds and |F_iq|<=C_B m_q.
Its direct current impulses cancel. Its recurrence has only past W_j
and E_j, so Gronwall yields CT36 at the first possibly failing row.

Choose B=B_*+1 and q small after fixing that B. CT45 improves the
row discrepancy to at most 1/2, closing the first-failure argument.
The Gaussian remainder yields CT7 without independence of zeta and J.
All constants depend on accumulated control length, not elapsed
physical time or the least nonzero coefficient. None of these steps
uses a population source estimate uniformly over random finite-network
feedback controls.

### B. Endpoint conditioning and finite hidden learning: PASS

The strongest dependence objection is that N in (2.3) can depend on
the first roots. The proof handles that obstruction: for a distant
Gaussian box about rv, its probability is bounded below by a quantity
of order exp(-O(r²)), whereas P(N>r²)<=exp(-O(r⁴)). Their intersection
therefore has positive probability without independence. On it, the
primitive's derivative on a unit neighborhood of each root grows
exponentially in r and dominates the allowed 5r² clock change.
This proves the uniform small displacement (2.4).

Any putative linear relation among the endpoint first features
would thus imply the sign relation (2.5) for every admissible v.
Crossing the line perpendicular to one input changes only that input's
sign because the list is distinct and nonantipodal. Choosing points
off the coordinate axes is possible even when the crossing line is
an axis. Subtraction forces every coefficient to vanish.

The fitted reference readout is nonzero. Since its finite-valued
upper preactivations have strictly positive sech² gates, each
delta_i is nonzero in L². The first-feature Gram inequality applied
at each upper-population coordinate, then integrated, gives (2.7).
This proves independence of the middle gradient blocks without
assuming injectivity of the trained action. Input continuity and
compactness of the angle interval make both factors defining kappa
in (2.8) have strictly positive minima.

For d_alpha=Pi g_alpha, its representation has coefficients
t=(-beta_1,-beta_2,1), hence |t|>=1. The middle-block Gram gives
||d_alpha,K||HS²>=kappa; this is stronger than a readout-only
nonzero projection. The stated T0 coefficient upper bound follows
from ||M^-1||<=1/kappa and ||G||<=sqrt(2)L0.

I checked the endpoint state/input modulus carefully because a product
of two arbitrary L² increments would be invalid. The upper backward
subtraction uses c_dagger as the fixed bounded factor. The lower gate
difference is bounded in L4 by a constant times the square root of
its L² preactivation difference, and multiplies the established
endpoint Q in L4. This yields (3.3), the inverse/projector estimates,
and (3.6). These bounds need no evolved L-infinity-small readout
difference and no uncontrolled bilinear L² product.

The hidden contrast O_alpha fixes the endpoint readout and coefficients
and depends only on hidden parameters. Its derivative at the endpoint
is -2r_dagger ||d_alpha,H||²>=5kappa/8. Its derivative along the reached
nonlinear field has the displayed square-root raw-distance modulus.
The first-exit radius and the independently constructed positive
existence time retain its sign on a fixed nonzero interval. This
does not infer finite motion merely from an initial formal derivative.

The risk calculation gives exactly
(r²)'=-4r²||Pi g_alpha||². The radius guarantees |r|>=5/32 and
||Pi g_alpha||²>=kappa/4. Their product yields
a=25kappa tau0/1024. The hidden contrast and Cauchy–Schwarz give
|Delta O|²<=30T0² J2 and therefore
j=(5kappa/16)² tau0²/(30T0²). Both are strictly positive and
independent of width and epsilon. The hidden statistic compares
the endpoint with the adapted state on the same carrier, so it
does not count the reference's earlier activity.

### C. Constructed continuation and singular slow limit: PASS

The potential failure here is to start from a fitted endpoint with no
proved source history or to assume a mixture trajectory exists on the
horizon being estimated. The construction avoids both.

The anchor Gram is uniformly invertible in a raw neighborhood by B's
gradient continuity. Formula (16) represents the projected field as
three controlled prediction gradients with a uniformly bounded
coefficient vector. The one-reference Gaussian-tail estimate gives
the Osgood modulus omega(z)=z sqrt(log(e/z)); its reciprocal has
divergent integral at zero. Integrating the scalar comparison after
the substitution sqrt(log(e/Z)) proves (13), so continuity alone is
not being promoted to uniqueness.

Constrained Euler programs start at increasingly accurate finite
reference prefixes. Their full controls include the omitted physical
reference suffix when measured against a_*. The appended absolute mass,
prefix error, and reference suffix fit strictly within the source
tube before its tails are used. Their bounded accumulated speed keeps
them inside the invertible-Gram region. Osgood comparison makes these
programs Cauchy uniformly in atom parameters and mesh; the finite
unions live on the common carrier. Joint field continuity passes the
integral equation, and soft-tail convergence transfers the Gaussian
query bounds. The constructed path is strong C1. Uniqueness compares
any competing strong raw solution against this tail-bearing path,
so no hidden extra tail hypothesis is imposed on competitors.

I checked every derivative needed in the residual identity. Along a
reached controlled curve, w' is in L4 with norm <=C m(t), c' is
pointwise bounded by m(t), and K' is HS. The strong activation,
delta, and Q derivatives in (24) are therefore integrable in L².
The only new row-gradient product in (25) is w'Q, controlled by
L4 times L4. Coordinatewise absolutely continuous representatives
and Fubini justify the chain and fundamental-theorem identities
also for integrable controls. Finite-dimensional matrix absolute
continuity and the Gram gap justify B' and ||B'||<=Cm(t).
There is no ambient C2 assumption.

For original-mixture Euler through a separately fixed b, direct
bounded-tanh recurrences first give raw and supremum-readout bounds.
Comparison with the actual reference uses only reference tails and
proves (32a). The actual integrated coefficient discrepancy (32b)
then tends to zero; raw proximity alone is not substituted for that
control condition. This obtains the mixture prefix cap before its
Euler Cauchy completion.

After b, the stopped finite recursion uses inner and outer state
and source thresholds. A partial affine step is itself a valid
appended partial Euler update, so SCT supplies its recomputed-query
L4 bounds. The strong derivative proof applies to its fixed node
velocity. A second integration gives
|R_k|<=C h_k²(|r_k|+epsilon)² in (32c). For small h,
I-h(1-epsilon)M has norm at most 1-2kappa h; the quadratic
remainder is absorbed to obtain (32d). Telescoping yields
sum h_k|r_k|<=C|r_b|+C epsilon(t_N-b), without an O(hT)
accumulated residual defect.

Together with the full remaining reference control mass this proves
(33) and excludes first exit through b+tau0/epsilon. The choices
are b large, epsilon and mesh small, and a fixed positive tau0
small enough for the common margins. At every fixed epsilon the
physical horizon is finite; capped Euler Cauchy completion constructs
the actual mixture solution from the original initialization.
Thus the later continuous residual estimates are applied to a
trajectory already obtained by a noncircular discrete argument.

I independently checked the exact residual algebra:

theta'=-(1-epsilon)Gr-2epsilon v,
r'=-(1-epsilon)Mr-2epsilon G*v,
and consequently theta'=epsilon V+B r'.

The normalization of the two anchor masses accounts for the factor
1-epsilon. With ||B'||<=C(|r|+epsilon), residual decay bounds
the integrated B'r term by
C(|r_b|²+epsilon|r_b|+epsilon²(t-b)).
The Hilbert absolutely continuous product rule gives (36).
On shifted slow time its error is uniformly bounded by the prefix
endpoint error, |r_b|, |r_b|², and epsilon. At fixed b the limsup
is O(exp(-b/5)); Osgood stability first takes epsilon to zero
and then b to infinity. Replacing tau by tau-epsilon b recovers
original physical time uniformly for tau bounded away from zero.
The missing convergence at tau=0 is explicitly excluded and is
necessary. No actual run was pretrained or reset.

The forward bounded-action estimates are uniform in the circle
input, so raw selection implies the specified whole-circle
prediction and L² hidden-field convergence. The scale 1/epsilon
comes from the exact remaining projected force, not from a
first-order law response extrapolated beyond its fixed horizon.

### D. Actual finite GF, readout, and joint observations: PASS

At each fixed positive epsilon, I checked the proof with
T=tau0/epsilon treated as a separately fixed finite number.
The actual finite smooth GF is global by the raw energy length
bound and finite-dimensional continuation. The bounds on its
readout supremum, action, and raw velocity follow from the actual
initialization and loss. They are not claimed to supply query tails.

The small stored Gaussian readout is present in both actual GF and
its finite proxy. Its maximum and RMS vanish in probability.
For a fixed finite proxy graph, comparison with the zero-limiting-
readout oracle uses cutoffs of the oracle L² fields and their
second-moment laws. It does not use an unproved width-independent
finite-dimensional Lipschitz constant. The fixed-graph causal
contraction passage and actual transpose/rank expansions are covered
by the included Gaussian value proof and the explicit cutoff
induction. The resulting finite coefficient errors vanish at fixed
mesh.

The hard-tail passage is valid because it is dominated by a
continuous soft-tail observation at half the cutoff. Uniformity
over proxy interpolation time is obtained by a fixed additional
time grid and raw/forward/Q continuity with bounded readout;
population affine states have the SCT bounds. No theorem is
applied to a transcript growing with width.

In the actual-to-proxy estimate all unbounded multiplying factors
are on the proxy side. The finite rank Frobenius identity is
||ab^T/n||F=(||a||2/sqrt(n))(||b||2/sqrt(n)).
Prediction residual errors are controlled by the raw distance,
the finite frozen-coefficient error, and the O(h) preceding-node
defect. Thus the exponential amplification is linear in the
cutoff. At fixed epsilon,T, the population Gaussian tail beats
that amplification. One can choose a finite cutoff first, a
sufficiently fine finite mesh second, and then width large;
strong population Euler completion identifies the desired path.
This proves the iterated limit and supplies no simultaneous
epsilon-width rate.

Input Lipschitz constants use the entire first-row RMS, the middle
operator norm, and the readout RMS. Fixed circle and time nets
therefore promote fixed-program observations to C([0,T]xS1)
prediction convergence. Joint mixture/reference proxy programs
use the same original arrays. Paired upper-hidden products are
joint same-layer second moments; same-width hidden RMS comparison
and Cauchy–Schwarz pass them to the actual finite flows.
Only after this fixed-epsilon width limit is the population
reference sent to its endpoint as epsilon decreases.

The final risk gain is on the added atom itself, without an
epsilon factor. Continuity of the bounded squared residual and
the paired hidden norm transfers the positive margins to the
probability-one-in-the-iterated-limit statement. No individual
finite neuron is assigned an artificial population counterpart.

## Assembly and scope checks

The exact replacement sentence in PROPOSED_EDITS_v3.json occurs once in
the frozen global excerpt. The new section heading occurs once in
the candidate, and its displayed link slug agrees with that heading.
The JSON appends the reviewed candidate to the named global chapter
and replaces the guide with the reviewed guide; notation and code
are explicitly unchanged.

I read both guides in full. An exact text comparison showed that the
only changes are the two instances of the specified C.4.9 summary.
Removing those additions restores the frozen guide byte for byte.
The summaries preserve the open single-atom parameter scope, finite
episode, original fixed-mixture GF, whole-circle observable, paired
second-hidden activity, and width-first order. They do not advertise
a final changed-law endpoint or out-of-sample risk guarantee.

All scientific dependencies used above are included in the frozen
proof bodies. Historical v1 filenames refer to unchanged frozen
dependencies and navigation files; the canonical scientific argument
does not rely on author artifacts, historical verdicts, or those
filenames as mathematical assumptions. Local equation numbering is
scoped by proof unit as declared. There is no blocking missing
definition or unresolved scientific reference.

## Exact certificate: command, environment, output, and semantics

I independently executed the authorized unmodified script once, with
working directory /home/amir/Codes/PDE and exact command:

    /usr/bin/python studies/nonlinear_prediction_selection/verify_reference_certificate.py

Python was 3.10.12 (main, Aug 31 2026, 10:18:17), GCC 11.4.0.
The platform was Linux-5.15.0-151-generic-x86_64-with-glibc2.35.
The script uses the Python standard-library Fraction implementation;
there is no floating-point dependency in the assertions and no random seed.
Exit status was 0; stderr was empty. Exact printed output:

    [0.392108947877, 0.396376711612, 0.233120735618, 0.339792209687, 0.631761866359]

The five numbers are readable float summaries of exact rational
lower/upper bounds. The operative assertions certify q>.39,
q<.4, v>.2, a0>.3, r0>.6, along with the stated elementary
tail and endpoint-error margins. I checked the mathematics of
the exponential series remainder, alternating arctangent bounds,
Machin identity, density bounds, monotone gate evaluation, missing
Gaussian tail, and outward summand rounding. In particular the
denominator 1-x/82 is positive on every used argument, including
18, and the missing tail beyond four is paid for in the q upper
bound. Since .624²<.39 and .633²>.4, the scale substitutions
have the correct monotone directions. Therefore m=v/2>=.1
is justified without a trained-flow computation.

I also extracted the complete embedded Python block from the frozen
global dependency and compared it exactly with the script after its
two provenance comments: they are identical.

Saved command evidence is in the assigned scratch directory:

- certificate_environment.json
- certificate_stdout.txt
- certificate_stderr.txt
- certificate_exit_status.txt
- hashes_initial.json
- packet_verification.json
- hashes_final.json

The packet verification also records: embedded certificate equality
true; old replacement count one; new guide passage count two;
unchanged guide complement equality true; candidate heading count one.
This deterministic checking was not a training experiment.

## Component verdicts and remaining objections

| Component | Verdict | Completion evidence |
|---|---|---|
| Architecture, initialization, raw metric, loss, physical clock | PASS | Direct block-gradient and finite rank normalization audit. |
| Contained Gaussian source/action dependencies | PASS for required uses | Full conditioning, singular-query, common-carrier, value/derivative, HS and scalar-chain proofs read and checked. |
| Reference flow, endpoint, source envelope | PASS | Full clock, fitting, cavity, envelope and finite-reference bridge bodies checked; exact certificate rerun. |
| A: integrated-control source transport | PASS | Zero/new/duplicate slots, normalized old-source pulses, causal bootstrap, and raw-to-clock defects checked. |
| B: uniform endpoint conditioning and finite margins | PASS | Dependent-envelope intersection argument, tensor Gram inequality, compact minima, exact nonlinear risk and hidden contrast identities checked. |
| C: constrained construction, mixture continuation, slow selection | PASS | Osgood uniqueness, full-prefix source history, discrete pre-existence residual contraction, strong product rule, and ordered initial-layer limit checked. |
| D: actual finite GF and paired whole-circle observations | PASS | Actual-readout oracle comparison, finite soft tails, cutoff/mesh/width order, full-row input nets and same-array joint laws checked. |
| Exact scope edits and guide additions | PASS | Full reads and exact unchanged-complement comparison. |

No unresolved objection remains. The theorem's finite episode,
nonquantitative constants, separately fixed atom in the finite probability
limit, exclusion of slow time zero, and absence of a simultaneous
epsilon-width rate are material scope limitations already stated in
the candidate, not hidden hypotheses added by this review.

I did not infer a final endpoint for the contaminated law, generalization
to a different test law, superiority over frozen-feature models,
arbitrary data-family continuation, raw GD capture on this slow scale,
or a uniform finite-width endpoint. None is needed for the stated theorem.

## Fingerprints and completion

All manifest-listed inputs were checked at the start and again after
complete reading and mathematical audit, and rechecked immediately at
report completion. All hashes match the frozen manifest and the
initially observed versions. The review manifest itself was also
unchanged. The exact hashes follow.

| Input | SHA-256 |
|---|---|
| REVIEW_ASSIGNMENT_v3.md | 7c31e8ba586e28769352704c70c8b98bfdfbf32924a9b9de7daee23cc4204cec |
| CANONICAL_ADDITION_v3.md | c858c7b41d90b490871450b8bf7494afe8c6cd7f39bebd3f1faa89f3604a5879 |
| PROPOSED_EDITS_v3.json | 46e1c92ed0d6c78940c8a7f60a966ca357e1883317ba8bb3cc977493da40e73f |
| PROPOSED_GUIDE_v1.md | d5ecdfd35fbddd511d98dccd148a9a9e840f5a4c814658f930c5732bab218bc5 |
| DEPENDENCIES_GLOBAL_v1.md | 6ebdaf1a3b28bdd07244a7b8c1bb882a36c7c525c4170cd25af4d7661ab7d942 |
| DEPENDENCIES_GAUSSIAN_v1.md | c95e358f6bb9741858e6293dabacf4fee01927a23cda1289cd3cd17e85a1ee77 |
| DEPENDENCY_GUIDE_v1.md | 5210ccd284ea79215d81c18f2fba93762538cfb1bb5b6b295c6e33e558225e1f |
| DEPENDENCY_NOTATION_v1.md | 199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b |
| DEPENDENCY_MANIFEST_v1.json | 75f8b2ae6716fb88d8f89306b78a104a2bffc62e1bf67bb64474b8298d5b415a |
| verify_reference_certificate.py | 07c51c139ebf66912ef7b730201dcc71581b11355dd29dbee6140bf2bba63118 |
| REVIEW_MANIFEST_v3.json | 394c052a06f241d36dd9b502dff26b121796323787c2608a50e6b5f9bb61608e |

Completed at 2026-09-12T10:39:38.126714+00:00.
The complete original report is retained at studies/nonlinear_prediction_selection/ADVERSARIAL_A_v3.md. Final verdict: **PASS**.
