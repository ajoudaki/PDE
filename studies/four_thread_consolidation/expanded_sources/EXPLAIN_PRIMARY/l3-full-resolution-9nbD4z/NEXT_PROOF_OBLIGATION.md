# The remaining global continuation obligation

Current checkpoint (2026-09-05): the global theorem remains open.
The latest exact formulations are FINITE_PRUNED_BACKPROP_PRIMITIVE.md
(actual finite errors with unweighted source) and
ACTUAL_LOG_GATE_COVARIANCE_COMMUTATOR.md (the commutator cancels, but
the complete energy remains uncontrolled). The full polarized Gaussian
exchange test has been completed and does not cancel its mixed responses.
The actual full-state density shortcut also fails against the tested
Gaussian references. See the final sections below and the compact
CONTINUATION_ROUTE_REGISTRY.md; do not repeat their superseded tests.

Update: the first positive interval is now proved, not assumed.
LOCAL_THEOREM.md assembles the fixed Gaussian source representation,
common action spaces, a mesh- and clipping-uniform Gaussian tail
bootstrap, removal of clipping, actual-GD convergence, local
uniqueness/restartability, gradient structure, and feature learning.
Two independent combined reviews returned PASS, followed by a
complete PASS from a fresh-context agent shown only the consolidated
proof. The remainder concerns extension beyond that local interval.

Neither finite-width optimization theorem in this directory is a proof of
the requested infinite-width, continuous-time limit. This note records
the exact outstanding step so that later work does not restart already
completed calculations or confuse optimization with population closure.

The prescribed vanishing readout is important. For that initialization
the finite-flow and exact-GD theorems now give, with probability tending
to one, width-independent bounds on the entire physical orbit:
operator norms, readout amplitude increments, finite feature-time
horizon, positive readout kernel, and convergence to an interpolator.
The flow additionally gives the exact total action identity and lower
second moments in every hidden layer.

The bad product is still
\[
 \delta^{(2)}
 =\phi'(z^{(2)})\odot
 (W^{(3)})^\top
 [W^{(4)}\odot\phi'(z^{(3)})].
\]
For two states, the gate-difference part is exactly
\[
 [\phi'(z^{(2)})-\phi'(\widetilde z^{(2)})]\odot
 (\widetilde W^{(3)})^\top\widetilde\delta^{(3)}.
\]
Let \(R>0\). Its normalized Euclidean norm is bounded by
\[
 2R\,\frac{\|z^{(2)}-\widetilde z^{(2)}\|_2}{\sqrt n}
 +2\left(\frac1n\sum_i
 \left|[(\widetilde W^{(3)})^\top
            \widetilde\delta^{(3)}]_i\right|^2
 \mathbf 1_{\{
 |[(\widetilde W^{(3)})^\top\widetilde\delta^{(3)}]_i|>R
 \}}\right)^{1/2}.
\]
This follows by splitting coordinates above and below \(R\), using
\(|\phi''|\le2\) below the threshold and boundedness of \(\phi'\)
above it. The comparison state, not the unknown exact state, may be
put in the tail-bearing position.

The current average-squared-size and integrated-action bounds do not
make the final tail term vanish uniformly over width and proof mesh.
A Gaussian tail estimate has now been proved uniformly over the
actual clipped population-Euler comparators for \(S\le S_0\).
It beats the \(e^{CR}\) amplification in the cutoff comparison and
closes the first local interval. A corresponding all-horizon
estimate remains unproved. This is a sufficient route, not an
assertion that Gaussian tails are necessary for the target theorem.

The natural first Euler state already has an unbounded Gaussian
component in this backward field. That disproves an ambient
width-independent Lipschitz estimate, not a tail estimate, a
time-integrated stability estimate, or the target theorem itself.

Changing from physical time to feature time or to predictor/action
time does not by itself close the argument. In a parameter variation,
the middle curvature contains
\[
 \frac1n\sum_i
 \phi''(z_i^{(2)})
 [(W^{(3)})^\top\delta^{(3)}]_i
 (\text{variation of }z_i^{(2)})^2.
\]
The identity
\(\phi''(z)/\phi'(z)=-2z/(1+z^2)\), whose absolute value is at most one,
replaces its coefficient by a bounded factor times \(\delta^{(2)}\).
Action controls the latter in mean square, but multiplication by the
squared variation would still require additional control of that
variation. A signed estimate along the actual causal perturbations
could be enough; no such estimate has been established.

Safe next routes must preserve both Gaussian matrices and their reused
transposes, exact arctangent, all trained blocks, and the prescribed
initialization. They must prove either the missing trajectory-specific
tail bound, an adequate signed stability estimate, or a different
well-posedness and convergence mechanism. A fixed-program limit,
successful finite-width optimization, an easier initialization, or a
counterexample outside Gaussian-initialized training is not a
substitute for that obligation.

The current and immediately next-time scalar response coefficients
are bounded on every finite feature horizon by exact identities.
GLOBAL_RESPONSE_CONTINUATION_AUDIT.md identifies the remaining
earlier-time response term. A later covariance argument in
COVARIANCE_RESPONSE_INCREMENT_REDUCTION.md now controls that term
after contraction against the actual backward history in L2. It does
not control the same row against the tangent history, which has a
different covariance. The local first-exit bound on complete
absolute response rows must not be silently iterated across time:
its constants could deteriorate, and no nonaccumulation theorem
has been proved.

The exact field
\((W^{(3)})^*\delta^{(3)}\) also obeys a linear inhomogeneous
equation with a bounded operator generator once the entire
coefficient path is fixed. Comparing two coupled coefficient paths
introduces the unestimated coefficient difference applied to the
reference backward field. PRIMARY_DMFT_APPLICABILITY.md records
this identity and three primary-source hypothesis checks.

A new route should target global continuation, not reprove the
now-closed local Gaussian identification, local GD bridge, or
finite-width optimization results. Current status: the complete
all-finite-time theorem is neither proved nor refuted.

The most recent alternative was gated-field localization. If
\(q=(W^{(3)})^*\delta^{(3)}\), truncating its large coordinates
and integrating against \(dH^{(2)}/ds\) gives signed power
\(O(R^{-1})\), using the already known \(q,q'\) mean-square
bounds. Its positive rare-coordinate power can be canceled by
the cross term between rare-driven and bulk-driven first-layer
velocities. GATED_LOCALIZATION_AUDIT.md gives an exact lower
training subsystem exhibiting this cancellation with bounded
operators, norms, derivative, and action. The forcing is external
and initialization non-Gaussian, so it is not a counterexample to
the goal. A successful version must exploit the actual top
feedback and canonical Gaussian law, not these deterministic
bounds alone.

## New continuation mechanisms, with their premises separated

ENDPOINT_RESTART_REDUCTION.md strengthens the endpoint statement:
the existing solution has strong HS matrix-increment limits, an
L-infinity readout limit, and a C1 backward-field extension to any
finite maximal endpoint. Existence on a right neighborhood still
does not follow from this continuity.

The same note proves an optimized comparison criterion. If the
clipped continuation family has a common L2 tail envelope G(R), the
state-error modulus can be taken as

    rho(u)=C u+C inf_{R>=1}(R u+G(R)).

The divergence of integral_(0+) du/rho(u) proves cutoff Cauchy
convergence, existence, and uniqueness. In particular a uniform
envelope exp[-c R/log(e+R)] suffices; Gaussian tails are stronger than
necessary. This is a proved sufficient implication, not an
established envelope for the canonical continuation.

There is now a concrete probabilistic input for a full-pruning route.
PRUNED_GAUSSIAN_SUBSET_BOUND.md constructs, for every middle set E,
the complete network with both its middle activation and backward
gate deleted on E. Its top backward field is independent of the
deleted initial Gaussian columns. A subset-entropy union bound
proves, simultaneously for all |E|<=pn and all times on a fixed
feature horizon, a normalized query bound of order
sqrt(p log(e/p)), plus a term vanishing with n. This simultaneous
event permits selection of E after observing the original network.

TOP_COUPLED_LOCALIZATION.md proves that deleting E from a copied
top input changes the actual top block by O(sqrt(p)), with constants
depending only on primal bounds. But this copied top is driven by
the ACTUAL bulk middle path, which can depend on the deleted
columns. It is not the independent FULLY pruned network. Substituting
one for the other would be the missing proof, not a notation change.

DELETED_QUERY_RESPONSE_AND_ENTROPY_AUDIT.md shows that a full/pruned
bulk-input estimate as weak as

    C sqrt(p) log(e/p) log log(e^e/p)

would already close the Osgood tail route when combined with the
simultaneous Gaussian lemma. Alternatively, it gives exact
normalized Jacobian-trace and random Gaussian-direction moment
conditions sufficient for the same tails. Bounded mutual
information alone is explicitly insufficient. A successful next
round should estimate this actual bulk response, or find a genuinely
different uniqueness mechanism. Repeating the already proved
local bootstrap or the Gaussian subset union bound will not resolve
the goal.

## New canonical rare-block and causal-response tools

The next round must use these new facts rather than repeat their
proofs. PRUNED_RARE_BLOCK_GEOMETRY.md exploits independence of BOTH
deleted incoming W_0^(2) rows and deleted outgoing W_0^(3) columns
from the fully pruned trajectory. For all small sets E simultaneously,
the reference rare self-block of

    A_2 = mean((h^(1))^2) I
             + W^(2) diag(phi'(z^(1))^2) (W^(2))^T

is close to alpha_E I_E, where 1/4<=alpha_E<=a^2+1. The error is
O(sqrt(p log(e/p))) plus a finite-width term. This lower bound follows
from phi(z)^2+phi'(z)^2>=1/4, not an assumed population rank.

ADAPTIVE_RARE_SELF_BLOCK_MODULUS.md then replaces the reference gate
by the actual adaptive gate. A simultaneous Gaussian submatrix bound
and integration over level sets give a rare self-block change
O(omega(d)+p log(e/p)+o_n(1)). It is an actual conditional-on-closeness
geometry estimate; it does not establish closeness.

DIRECT_SCALAR_PRUNED_REDUCTION.md provides a different use of that
geometry than an instantaneous Lipschitz estimate. With genuine
pruned rare preactivation zhat_E and e=z_E-zhat_E, write exactly

    e'=alpha_E delta_E+rho,
    rho=(A_2,EE-alpha_E I)delta_E
              +P_E A_2(I-P_E)delta^(2)-zhat_E'.

The note controls rare displacement by the Gaussian reference
supremum, the residual rho, and a saturating p^(1/3) term. Exact
integration by parts then controls accumulated rare row updates and
accumulated rare forcing of X^(1), without bounding delta_E tails.
Its remaining term is the off-block bulk response in rho. A small
operator norm for the self-block does not estimate that term.

ACTUAL_BULK_GAUSSIAN_TANGENT_ENERGY.md gives another targeted route.
An independent Gaussian perturbation of one initial top column has
mean-square forcing O(1/n). Its scaled response energy controls the
normalized HS Jacobian and therefore the trace/directional quantities
from the earlier Osgood criterion. The sole bad energy pairing
contains an explicit mixed covariance of the actual causal tangent.
The bounded learned top history is harmless. Gaussian integration by
parts for the initial matrix leaves mixed SECOND flow responses;
calling those independent noise would be invalid.

The high-leverage next work is therefore either the actual off-block
response in the scalar/rank-memory comparison, or a signed estimate
for the actual mixed probe covariance with its own-site cancellation
retained. A generic gradient/action counterexample, a further norm
bound on the same initial Gaussian queries, or a new sufficient
criterion without estimating one of those quantities will not close
the global theorem.

The actual two-time kernel now has a further controlled part.
ACTUAL_TWO_TIME_RARE_RETURN.md writes

    K(s,t)=T_s U_L(s,t) R_t,
    T_s R_t=<H1(s),H1(t)> I
                      +W2(s) D1(s)^2 W2(t)^*.

The bounded propagator differs from the identity by O(s-t), so the
same rare-set compression of K(s,t) is close to its pruned scalar
center, with error

    r_n(p)+C_S[(s-t)+omega(d_E(s))+d_E(t)+h(p)+q_n].

Here r_n is the already proved reference Gram error, h(p)=p log(e/p),
and q_n is its stated vanishing probability term. The center remains
positive at short lag. For disjoint E,F with a small union D, applying
the estimate to the jointly pruned reference for D also bounds
P_E K P_F: the scalar term vanishes under the two projections.
The needed distances are to that jointly pruned network. This still
does not give a small rare-to-large-bulk bound or a bound after
multiplying by the unbounded middle curvature. It must not be
mistaken for a bound on the full tangent propagator.

TIME_ORDERED_PROBE_AND_SELF_RETURN_AUDIT.md also verifies a favorable
conditional Gaussian sign for the principal INITIAL self-site
curvature. Conditioning is only on lower initialization and the
initial top forward answer, not on an operator-norm event. The
localized tangent jet does not disprove a finite-time covariance
bound because the full probe energy already has a lower-order
readout term and no needed uniform remainder is proved. The useful
target is to retain the own-site sign/cancellation while estimating
actual off-site and two-time returns, not to assume that the initial
sign persists.

## Off-block residual now controlled; the remaining term is active feedback

SINGLE_PRUNED_OFFBLOCK_OSGOOD.md advances the rare-comparison route.
For the zero-readout full/pruned proxy, it now proves

    ||rho_E||_2/sqrt(n)
        <= C[sqrt(p log(e/p))+mu(d_E)+nu_n],
    mu(d)=d sqrt(1+log_+(1/d)).

This holds simultaneously over all sets and times, without assuming
d_E is small and without a backward-field tail premise. It also
holds for each same prescribed clipping in both networks.
It is not a claim of a global tiny-random-readout transfer.

The new mechanism uses the SINGLE E-pruned reference throughout.
Its deleted Gaussian rows are independent of

    C_E = D1hat^2 What2^* (I-P_E).

Uniform restricted-column bounds for W20,E C_E P_F apply to every
adaptive F. Sorting any vector v into equal-sized magnitude blocks
gives

    ||W20,E C_E v||_2/sqrt(n)
      <= C[Q sqrt(h(p))+ell sqrt(log(eQ/ell))+width error],

where ||v||_2/sqrt(n)<=Q and mean|v|<=ell. Apply this to

    v=(I-P_E)(D2-D2hat) q2hat.

Its L2 norm need not be small, but its averaged L1 norm is O(d_E).
Squaring the adaptive lower-gate difference before applying the
all-submatrix estimate gives the same mu(d_E) modulus for the
actual/reference off-block operator. This is stronger than the old
rare self-block modulus and actually estimates the residual.

SHARP_RARE_ACCUMULATED_FORCING.md further improves the rare forcing
term from p^(1/3) to sqrt(h(p)). The unused pruned backward query
has the Gaussian subset bound and

    ||P_E q2||_2/sqrt(n)
          <= C[sqrt(h(p))+nu_n+d_E].

In the scalar amplitude bound let J=int alpha ||P_E q2||_2/sqrt(n).
Then (p J)^(1/3)<=sqrt(p)+J. This closes the improved bound

    rare accumulated row training + rare accumulated bottom forcing
       <= C[sqrt(h(p))+width error+int mu(d_E)].

The statement is a genuine relative estimate, NOT a closed inequality
for d_E. The exact remaining terms are

    v tensor h1

in the ACTIVE W2 update and

    ((I-P_E) What2)^* v

in the full first-layer update. Those terms lack the small-set
Gaussian compression above. Their accumulated effect, not another
estimate of rho_E, is the next needed resolver.

ACTUAL_PROBE_LEVERAGE_LOCALIZATION.md gives a compatible narrower
response target. Define ell_j=n E_probe(gamma_j^2+zeta_j^2) and
E_R={ell_j>R Lambda}, where Lambda=n E_probe||y||^2. This adaptive
set has mass <=C/R. Its complement has signed curvature contribution
<=C sqrt(R) Lambda and a controlled integrated response. The
exceptional signed contribution can still carry all covariance
mass. The rare primal estimates cannot simply be differentiated to
bound it. Its actual signed/accumulated response is the alternative
next resolver.

## Latest derivative and energy advance

ACTUAL_RARE_BACKWARD_DERIVATIVE.md proves, on a common all-set/time
event for the zero-readout proxy and the same prescribed clipping,

    ||P_E q2'||_2/sqrt(n)
       <= C[||P_E delta2||_2/sqrt(n)
                        +sqrt(h(p))+mu(d_E)+epsilon_n].

The actual rare self-return is retained, not treated as independent.
The proof uses four right coefficient families, each independent of
the deleted TOP Gaussian columns; the incoming velocity query uses
its different, correct active-data event.

RARE_BACKWARD_ENERGY.md pairs the rare scalar equation with q2_E,
or with tau(q2_E) in the clipped case, then integrates by parts against
the bounded actual rare activation. The zero initial readout removes
the initial boundary. Young's inequality absorbs the retained rare
backward action and proves

    integral ||P_E delta2||_2^2/n
       <= C[h(p)+epsilon_n^2+integral mu(d_E)^2].

The derivative and scalar identities consequently control the
integrated squared derivatives of q2_E and z2_E, and the coordinatewise
time maxima of q2_E and of the displacement z2_E-z2_E(0), by the same
right side. This still depends on d_E: it is not full-state stability.

The next deletion resolver is genuinely UNCOMPRESSED active feedback.
One concrete test is whether the new relative energy can close a
simultaneous hierarchy of single- and union-pruned comparisons.
Replacing its right side by a small quantity without proving d_E
small would be circular.

ACTUAL_MOVING_RANGE_PROBE_NORMAL_FORM.md supplies a separate actual
response advance. Let R map a middle response into the lower training
state, J=(R*R)^(-1)R*, P=RJ, and split the actual probe as y=Ra+w.
The lower activation moment makes R*R uniformly invertible.
The directly forced part w0 of w has probe-map operator norm O(1/n),
so n E_probe |(T w0)_j|^2 <= C for every coordinate.
Its signed curvature pairing is therefore controlled on every
adaptive exceptional set. What remains is a and the memory driven
back by a, not this direct orthogonal source.

ACTIVE_GATE_PRIMITIVE_AUDIT.md records exact but unclosed
integration-by-parts formulas for the active gate primitive.
RECENT_CAVITY_THEOREM_SCOPE.md records why the new 2026 primary
cavity theorem does not directly close the unclipped flow.
Do not repeat either as a new successful route.

## Latest resolver: absolute Hardy iteration is not sufficient

ACTUAL_WEIGHTED_GATE_HARDY_BOUND.md now controls the uncompressed
active gate vector itself. Add and subtract the actual q2 in
v=(D2-D2hat)tau(q2hat), and weight its actual maximal-time path by
w=|D2-D2hat|^2. The empirical mean of w is O(y_E), where y_E is
the squared HS/product state distance. Layer cake over its levels
uses only the already proved actual all-subset query event.

The resulting state hierarchy (19) has a genuine Osgood leading
term Phi(y)=y[1+0.5 log_+(1/y)]. Its remaining term is

    integral_0^t sqrt{
       Y_p(s) s integral_0^s
          H_{min(1,C0 Y_p(s)),n}[r -> Phi(Y_r(u))] du
    } ds.

The finite Hardy map retains its lower floor max(a,1/n). No
nested-pruned event, lost time supremum, or replacement of this
size average by its value at r=a is used in the proof.
The full actual estimate and hierarchy passed independent review.

FINITE_FLOOR_HARDY_HIERARCHY_COUNTEREXAMPLE.md now proves that this
EXACT SCALAR HIERARCHY alone cannot establish small-deletion
continuity. With theta(t)=t^2/(1+2t^2), set

    Y_{p,n}=theta(t) h(floor(np)/n)+exp[-1800/theta(t)^5]

for p>=1/n and zero below. It has zero initial values and
derivatives and is uniformly bounded. It satisfies inequality
(19) with C=1 and zero width error, but has a positive limiting
profile. Both finite-floor regimes are explicitly proved.
The construction also survives any positive constant via a slow
clock, and a delayed start preserves a prior zero-error interval.
Root and an independent agent checked the complete proof.

DO NOT keep iterating that scalar hierarchy as though a missing
Gronwall manipulation will close it. The new necessary resolver
must use canonical information discarded by this absolute
majorization: signed gate/response structure or a genuinely
stronger bound on the actual response. This artificial profile
does not refute the network theorem or the proved local result.

## Signed range identity now available; do not mistake it for a bound

ACTUAL_SIGNED_RANGE_INTEGRATING_FACTOR.md records an exact
fixed-coordinate-set calculation for the actual uncut derivative
probe. In the moving training-range coordinate a, retain

    h_E=P_E[(Acal-alpha_E I)a+integral N a].

This includes rare self-block error, rare-to-large-complement
transport, and recycled normal memory. If
r_E=ghat_E+rho_E, D=phi'(z2), and beta=phi''(z2)/phi'(z2),
the actual scalar identity gives

    alpha_E q2 phi''(z2)=(log D)'−beta r_E.

Hence c_E=D_E^{-1}a_E obeys exactly

    c_E'=-beta r_E c_E+beta q2_E h_E+D_E^{-1}P_E F.

The principal scalar curvature cancels without differentiating
alpha_E, Acal, or a primal norm inequality. The remaining signed
energy has residual/response and returned-response pairings plus
the weighted source; they are not assigned a favorable sign.

The new primal derivative/energy estimate controls the mean of

    ell_j^E=integral(|q2_j'|^2+|r_E,j|^2).

The actual response instead needs its pairing with

    U_j(t)=n E_probe|c_E,j(t)|^2,

or with the coordinatewise supremum of U. A small mean of ell
and a bound on the mean of U do not control their pairing.
The source also retains D^{-1}=1+z2^2. This note is an exact
identity/reduction, not a newly proved response bound.

All differentiated coordinate supports in that note are fixed
in time. The state-space training-range projector already moves
and its derivatives are included. A time-moving exceptional
coordinate support needs its own membership/weight derivative
terms; it cannot be inserted by setting P_E'=0.

## Superseding primitive coordinate: ordinary source terms are now controlled

ACTUAL_WEIGHTED_ADDITIVE_PROBE_SOURCE.md proves that the directly
forced normal response w0 stays purely in the top two blocks.
Thus T w0=0 and its mixed curvature covariance is exactly zero,
strengthening the earlier coordinate-variance estimate. The
inverse-gate-weighted ADDITIVE source is also now bounded.

ACTUAL_BACKPROP_PRIMITIVE_RESPONSE.md then replaces the old range
coordinate by the time integral a_delta of the ENTIRE variation of
delta2. Its exact integration-by-parts representation is

    y=y0+R a_delta+integral U0 S a_delta,
    T y=A2 a_delta+integral N0 a_delta,

where y0 is purely top-layer and every displayed propagation map
is bounded by the common primal constants. In particular the PLUS
memory sign and the exact diagonal-time kernel are proved, not
formal response approximations.

For c_E=D_E^{-1}P_E a_delta, the resulting equation is

    c_E'=-beta r_E c_E+beta q2_E h_E+P_E u,

where h_E retains all nonscalar instantaneous and memory response,
and u is the FULL top-query variation. Its normalized conditional
Gaussian second moment is bounded by

    C[1+A_delta(t)+integral_0^t A_delta(s) ds],
    A_delta=n E_probe ||a_delta||_2^2/n.

There is NO inverse gate on this source, including its response-
dependent part. Young's inequality controls its energy pairing
by the same response energy. This removes an actual prior gap.
For E equal to the whole layer, A_delta<=n E_probe||c_E||_2^2/n.

The complete representation/source theorem, including extension
to the prescribed C1 clipped family, passed a fresh-context
proof-only audit. In that extension q2 in the curvature is replaced
by tau(q2), and u by diag(tau'(q2)) times the actual query variation.
No tau'', inverse lower mobility, or clipped coercivity is needed.

The remaining exact term is the signed covariance pairing

    -mean(beta r_E U)+mean(beta q2_E V),
    U_j=n E_probe c_E,j^2,
    V_j=n E_probe[c_E,j h_E,j],

with tau(q2_E) for the clipped family. No closed bound on this
pair has been proved. It is the current response resolver; do not
reintroduce the now-removed ordinary weighted-source premise.

LOGARITHMIC_NETWORK_COMPARISON.md supplies a separate, independently
audited actual-network estimate: the state Jacobian has nuclear
norm O(n), so the width-normalized sum of log cosh(log singular
value) is bounded on finite intervals. Exact covariance determinant
bounds hold for both the full Gaussian column seed and the trained
response increment. These do not bound the response trace: a few
directions can have large amplitude. The exact full/pruned source
is small, but may align with those directions in its coupled
propagator. That alignment, or the signed pair above, is still open.

The full canonical theorem remains neither proved nor refuted.

## More precise current signed term; joint top energy does not close it

ACTUAL_PRIMITIVE_OFFDIAGONAL_PAIR.md removes dependence on an
arbitrary scalar split. On the whole middle layer, with g=q2 or
tau(q2), z=z2, D=phi'(z), and a_delta=Dc, the exact primitive is

    c'=u+beta(g zeta-z' c),
    zeta=A2 D c+memory, z'=A2 Dg.

For Sigma_ij=n E_probe[c_i c_j] and K2=W2 D1^2 W2*, its
instantaneous signed contribution is exactly

    (1/n) sum_ij K2_ij D_i D_j [
      z_i g_j Sigma_ii+z_j g_i Sigma_jj
                          -(z_i g_i+z_j g_j)Sigma_ij].

Every diagonal term i=j vanishes, without approximating K2's
diagonal. A fresh-context reviewer checked the complete identity
and the clipped case. The actual off-diagonal polarized covariance
and causal memory, not an own-coordinate diagonal curvature, are
the remaining terms. K2 positive semidefinite alone does not give
a sign; the note's tiny algebraic example makes no network claim.

JOINT_MIDDLE_QUERY_ENERGY_AUDIT.md tests adding the actual top-query
variation to a joint energy. Subtracting its top input-Hessian
response cancels the pure middle-input third derivative. The
corrected query is already bounded algebraically by top parameter
variation; differentiating it instead introduces a mixed top-
parameter/actual-velocity product. The exact finite full/pruned
energy still contains the actual lower mobility difference. This
tested energy does not close the primitive covariance and should
not be repeated as an unexamined cancellation proposal.

TIME_ANALYTICITY_DERIVATIVE_AUDIT.md independently tests a different
route. For the full raw lower-parameter gradient system with zero
readout, the exact fifth prediction derivative contains a cubic
backward-query contraction. An explicit all-block network family
with initial operator norms below 2 makes it grow like -c sqrt(n).
It lies in the usual deterministic primal-bound class. Gaussian
full support gives positive-probability neighborhoods at fixed n,
but NOT a uniform failure probability. Thus primal bounds alone
cannot give a deterministic uniform factorial derivative estimate.

The same audited note gives a bounded arctan-saturated scalar
Gaussian average that is smooth but nonanalytic at zero, with
all finite derivative exchanges justified. It is not the network.
A typical-Gaussian analytic-continuation route would need genuinely
new derivative/averaging bounds; neither finite-width analyticity
nor the local theorem supplies them automatically. This does not
refute canonical continuation or analyticity at positive times.

## Second log-gate test and next canonical resolver

ACTUAL_LOG_GATE_SECOND_IBP.md proves a potentially useful stronger
spatial fact: if X_i=sup_{s<=S}|log(phi'(z2_i(s)))|, then

    mean exp(X_i)<=C_S,
    mean X_i^2 1_{X_i>R}<=C_S exp(-R/2).

This follows from the already bounded mean of sup_s z2_i(s)^2.
Total variation of the log gate has only a mean-square bound;
these two quantities must not be conflated.

Under the actual UNCLIPPED lower coercivity premise, set
C=A2/m1>=I, L=log D2<=0, B=diag(L)C, and eta=(I-B)a_delta.
SPD similarity proves ||(I-B)^-1||<=sqrt(cond C)<=C_S.
The proposed correction is therefore genuinely invertible,
with eta(0)=0 even though L(0) need not be zero.

Its exact derivative still contains

    eta'=(I-B)F-diag(L)C'a_delta
                    -diag(L)C diag(L')C a_delta.

F retains the response-dependent residual and memory. The
diagonal of the ordered commutator is

    sum_{j!=i} (K2_ij^2/m1^2)(L_i L_j'-L_i' L_j),

and C' contains the actual lower multiplier
W2 diag(2 phi'(z1)^2 phi''(z1) q1) W2*/m1. Neither term
has a width-uniform response bound. Nonzero Gaussian initial
off-diagonal coefficients do not imply a nonzero loop; at zero
readout L'(0)=0. A fresh-context reviewer checked the entire note.

This second integration is stopped at those exact retained terms.
The next pass should not repeat its inversion or discard ordering.
The proposed full symmetrized Gaussian test has now been completed;
the following update supersedes that proposed next step.

The present goal turn made progress on exact source control and
response structure, but did not prove or disprove the complete
canonical all-finite-time theorem. Its status remains ACTIVE.

## Current update: finite primitive and metric; exchange test completed

FINITE_PRUNED_BACKPROP_PRIMITIVE.md extends the full primitive to the
actual nonlinear full/pruned pair. If a is the integral of the entire
middle-backprop difference, its exact bounded-memory representation
controls the state by the ordinary squared size of a and the deletion
source. The new finite-pair diagonal factor is

    M_i=1+(z_i^2+z_i zhat_i+zhat_i^2)/3,  c_i=M_i a_i.

The exact equation is

    c'=u-A_gate h+
       [(M_z/M)r_1+(M_zhat/M)r_2]c.

Here u is the clipped full/pruned query difference, h is the non-scalar
return of the primitive, and r_1,r_2 are the two actual non-scalar
primal velocities. All are defined in the note, with no frozen-network
substitution. The ordinary energy pairing with u is controlled by
the response energy plus rho log(e/rho) and the width error. The two
remaining signed terms are NOT controlled. Common merely Lipschitz
clipping is allowed; no coercivity or clipping derivatives enter.
This is a fresh-context audited finite-error identity, not closure.

ACTUAL_LOG_GATE_COVARIANCE_COMMUTATOR.md supplies a real cancellation:
for C=A2/m1, L=diag(log D2), B=LC, B0=L'C and Q=[B,B0],

    Q* C=-C Q.

Thus a* C Q a=0 for every actual probe. For eta=(I-B)a,
G=C(I-B)^-1 is positive, eta*G eta>=||a||_2^2, and
eta*G Q a=0. This supersedes any blanket claim that Q necessarily
survives every energy. The FULL energy derivative still contains
symmetric L' work, C', and CP times the complete source. It is not
estimated merely by the inverse or amplitude-tail bounds.

ACTUAL_FULL_PAIR_GAUSSIAN_IBP.md performs the previously proposed
full i,j-exchange test. Both orientations add the mixed second flow
derivatives. Lower Gaussian integration generates third derivatives.
An actual n=2 positive t^5 jet gives a nonzero smooth localized mixed
sector even in neighborhoods with the prescribed tiny readout.
It does not give the sign of the unlocalized Gaussian mean, a failure
of a uniform estimate, or a counterexample to the canonical theorem.
The finite learned increments and all localization derivatives are
retained. No merely C1 clipping extension is asserted for this
higher-derivative calculation.

All three new scoped notes passed independent fresh-context proof-only
audits. Next work needs genuinely new control of the actual finite
signed pair or the complete metric energy, not the already tested
exchange-only cancellation. The global theorem remains OPEN.

## Additional distinct route tested: actual Gaussian density transport

ACTUAL_GAUSSIAN_DIVERGENCE_SCOPE.md tests whether the already proved
O(n) ordinary Jacobian trace controls an actual likelihood ratio. It does
not, for the proposed full-state reference. Correct whitening is
(z1,sqrt(n)W2,sqrt(n)W3,nW4). The exact log likelihood against the
initialization law is

    (n^3/2)[||W4(s)||_2^2/n-||W4(0)||_2^2/n]+E_s,
    |E_s|<=n P_S(initial operator norms, initial readout RMS).

The actual tiny-readout network has ||W4(s)||_2/sqrt(n)>=c s with
probability tending to one at each fixed sufficiently small positive
time. Thus entropy and typical log likelihood are order n^3.
Changing the independent readout reference variance to n^-2+s^2
instead gives entropy (n/2)log(1+n^2 s^2)+O_S(n).

The proof is root-checked and has a fresh-context proof-only PASS. It retains
the actual trained matrices, zero-versus-tiny distinction, and physical
clock. A marginal or compressed query law is NOT lower-bounded by the
full-state entropy; its law must be analyzed separately. Nor is the
linear Gaussian probe covariance determinant the same density object.
Do not recycle full-state Liouville control as the missing query-tail
proof. A compressed distributional route is still logically possible,
but no new premise sufficient to close it has been proved.

## Current refinement: hidden density exists; quantitative projection is open

ACTUAL_PROJECTED_DENSITY.md discharges qualitative hidden absolute
continuity for the actual canonical flow at every fixed n and finite
time, including zero initial readout. Analyticity and the stationary
point W^(2)=W^(3)=0 show that the hidden determinant is nontrivial;
countably many local inverse branches then prove absolute continuity.
No width-uniform analytic radius, density bound, or global inverse is
asserted.

The same note derives an exact finite conditional-entropy identity:

    D(hidden_s || hidden_initial_Gaussian)
      = O_S(n) + H_dif(readout_s | hidden_s)-H_dif(readout_0).

The controlled term is two-sided, and all entropies are finite for the
canonical tiny Gaussian initialization. The unresolved upper bound is
on the displayed conditional-entropy increase. Merely bounding the
unconditional readout RMS leaves n log n. Differentiating a conditional
mean does not remove its actual conditional-covariance flux.

ACTUAL_HIDDEN_GRAPH_VOLUME.md proves a width-uniform normalized
intrinsic-volume bound for EVERY transported tangent plane, using the
actual raw Gaussian-coordinate Hessian and only readout RMS. For the
hidden-initial tangent plane T=[P;R], orthonormalize T to Q=[Q_H;Q_C].
Then exactly

    |det P| = sqrt(det(T^T T)) sqrt(det(I_n-Q_C Q_C^T)).

The first factor has expected absolute log O(n). The second represents
at most n projection angles and is not quantitatively controlled.
When P is invertible its loss is (1/2)log det(I_n+K K^T), K=R P^-1.
K is a single inverse-branch derivative, not the mixed conditional-mean
derivative or a conditional covariance. Branch weights must be retained.

Both notes have fresh-context proof-only PASS reports. Their smooth
bounded-feature NONCANONICAL example establishes actual hidden
noninjectivity and zero projected determinant despite full-flow
regularity. It is not a canonical counterexample or a mixture-entropy
sign result. Do not repeat a generic gradient-form no-fold argument.

Further density-route work must estimate a genuinely canonical
projection/conditional quantity and then show how it controls the
needed adaptive query. Another equivalent sufficient condition is not
closure. The finite signed-pair and complete metric-energy routes remain
available only with new estimates; the complete target remains OPEN.

## The next deterministic angle test is now resolved

Do not repeat the proposal that bounded J and integral nuclear A alone
control time-integrated log det(I+KK^T). It is false, even with bounded
analytic features, fixed d=m=2, a bounded reference trajectory and P
invertible at every time in [0,4]. In the audited autonomous example,
one slope is coth(epsilon) throughout [3,4] before analytic smoothing;
the analytic approximation retains a comparable slope and all common
norm bounds. The integral diverges like log(1/epsilon).

This is a deterministic norm-only obstruction, NOT a canonical or
Gaussian-average counterexample. It removes this proposed shortcut,
not all projection-density methods.

SCALAR_READOUT_PROJECTION_THEOREM.md supplies a separately audited
positive check: every bounded smooth scalar feature has globally
invertible hidden feature-time maps at fixed c_0. The scalar orbit
derivative gives a complete-divergence determinant lower bound.
Zero-readout forward physical time has its own first-zero argument
and determinant estimate. Canonical n=1 entropy follows from explicit
polynomial bounds, with feature-time Gaussian readout mixing justified.
Arbitrary nonzero-readout physical injectivity is not established.

The scalar argument cannot simply be reused with commuting output
gradients: an actual analytic calculation proves noncommutation almost
surely at each fixed n>=2. This is not a width-uniform commutator bound
or a projected-singularity result.

The next substantial resolver must estimate an actual canonical
signed response/finite-pair term or a canonical averaged projection
quantity with a proved adaptive-query consequence. General volume
control, qualitative density, scalar readout, and another equivalent
sufficient condition do not settle it. The complete all-finite-time
theorem remains unproved and unrefuted; the active goal is not complete.

## Additional tested route: material Hessian and the arctan Schwarzian

The scalar identity phi''' phi'-(3/2)(phi'')^2=-2(phi')^4 suggested a
signed bound on B'-kappa B^2 for the symmetric actual raw Jacobian B.
This exact deterministic test is now resolved negatively on the
bounded-primal state class. ACTUAL_SCHWARZIAN_MATERIAL_HESSIAN.md gives
the full material derivative and an explicit canonical state with
bounded B but opposite order-n quadratic divergences for every fixed
kappa. A separately derived exact physical-time calculation retains
the residual rank-one correction and has the same conclusion.

Do not repeat a scalar-to-matrix Schwarzian inference or try to repair
it merely by changing the fixed coefficient of B^2. Off-diagonal
positive mobility permits q_i z_i'<0 and prevents that implication.
The counterexample is NOT a prescribed-Gaussian high-probability state;
it is specifically not reachable at positive time from zero readout.
It leaves a trajectory-specific probabilistic signed estimate open.

The new note has a genuinely fresh-context full-file PASS at the hash
in REVIEW.md. The central resolver remains a quantitative estimate on
the actual trained Gaussian response or finite-pair error, not another
ambient primal-bound argument. The full goal is still ACTIVE.

## New comparison route: the frozen growing-horizon noise size is resolved

PANAHI_EULER_PERTURBATION_SIZE.md has a fresh-context proof-only PASS.
For frozen time-Lipschitz query histories it controls both matrix
orientations and all query times, even K~n^2, via regularized effective
rank. The actual top-matrix histories have the required temporal
regularity on the primal event. The lower uncut backward history does
not yet have a width-uniform Euclidean derivative estimate.

Do not repeat the raw ||Gamma|| growth argument as an exclusion: it is
overcome for these frozen histories. Nor may adaptive coefficients be
frozen by conditioning while keeping Gamma independent. The later
causal test proves an explicit correction to that isometry. The
subsequent Gram martingale now supplies a different adaptive estimate,
as recorded below. Even small forcing does not alone supply unique
restart.

The exact finite perturbed comparison in the primary source may be
used as a mechanism, but its fixed-query-count stability bounds and its
unproved complex-continuation claim cannot close this gap by invocation.
The completed local theorem remains the strongest full canonical limit
theorem established here; the all-finite-time goal is unchanged.

## Superseding comparison obligation: actual rank, not frozen independence

PANAHI_ADAPTIVE_GRAM_MARTINGALE.md is proved and independently audited.
The matrix B=sum t_i Gamma_ij s_j^T is exposed in two half-steps per
query, in the exact source order. Both left and right predictable
variations are controlled by the actual regularized Gram ranks.
On a rank event with r log^2(n)=o(n), both covariance perturbations
vanish uniformly over polynomial query horizons. Its finite probability
bound is P(rank event AND bad noise)<=alpha, not a claim that the
rank event itself has high probability.

The next new resolver must control the actual perturbed histories'
ranks (or replace that premise), and still address nonlinear stability
and removal. PANAHI_SMALL_JITTER_RANK_INFLATION.md proves that
uniformly vanishing sigma-scale jitter can make these ranks full
and keep raw AND integrated Gamma perturbations macroscopic at K=n^2.
Hence do not apply the frozen time-regular bound merely by discarding
small direct query noise. The example is not a canonical trajectory.

PANAHI_CAUSAL_ADAPTATION_ISOMETRY_TEST.md separately shows why the
frozen identity itself fails even for rank-one causal slow histories;
it does NOT refute the now-proved adaptive bound. All three additional
notes have complete final fresh-context PASS reports in REVIEW.md.
The actual canonical all-finite-time MF/GF theorem remains unproved
and unrefuted; none of these lemmas completes the active goal.

## Integrated-query test: regular state arguments do not yet give a transcript

INTEGRATED_INITIAL_QUERY_COMPRESSION.md has a fresh-context full PASS.
All initial-matrix arguments in its exact integral state equations are
time-Lipschitz after introducing the lower backward primitive. The
complete trained-matrix memories have verified uniform-path continuity
bounds. Do not reintroduce memory discontinuity or the temporal roughness
of the unintegrated lower backward argument as defects of this exact
state representation.

The actual resolver is still a causal approximation AND its stability.
A finite net sampled from the true path does not make that path's
query values functions of the retained finite Gaussian transcript.
The nonlinear primitive comparison contains the same middle gate
multiplier, and derivative convergence is separately needed for the
specified velocities/raw kernel. Mere consistency, a supplied-trajectory
net, or time-Lipschitz bounds alone cannot close the requested theorem.

## Superseding Hessian scope: a zero-readout-reachable witness now exists

ACTUAL_ZERO_READOUT_REACHABLE_HESSIAN.md has passed a fresh-context
full-file audit. Its positive bulk channel leaves the rare order-n
positive material-Hessian term intact while allowing a uniform
backward passage to exactly zero readout. The reconstructed actual
feature and physical trajectories have the stated primal bounds on
their entire segments and bounded B at their terminal states.
Consequently zero-readout reachability alone does not imply the tested
pointwise signed bound. Do not repeat that proposed repair.

The earlier counterexample remains unreachable; this NEW construction
removes that specific limitation. It does not have the prescribed
Gaussian initialization, bound B over the entire segment, or test
extra assumptions involving its history. An actual Gaussian-typical
signed/response estimate remains a possible resolver. No negative
theorem about the requested population limit follows.
