# Direct whole-circle RMS as a scalar aggregate observable

2026-09-25. Scoped theory assessment for the existing scalar compression of
the OLD activity-clock, finite-width, fixed-P response-memory system. This is
an internal author derivation, not an independent promotion review. No code,
experiment, archived result, or other study was read or run.

**Conclusion.** Whole-circle mean-square error can be a direct observable of
the scalar hierarchy. Recovering dense weights or evolving a passive test
grid is unnecessary for this particular number. The required extension
retains contractions integrated over a shared angle; products at the same
angle must remain coupled inside their integral. With that extension, the
finite-template estimates and the prescribed-finite-horizon convergence
proof for the saturated scalar variant still apply, at fixed finite width
and fixed history order. This proves an approximation-existence statement,
not a practical small closure, exact finite closure, or width-uniform result.

The four assigned scientific inputs do not specify the circle target
function g. In particular, they do not confirm that the original target is
a finite Fourier sum. The mathematical result below assumes a fixed bounded
measurable target and a specified bounded circle parametrization; effective
initialization additionally requires computable integrals or a specified
regular target representation. A finite Fourier target would satisfy this
extra requirement, but its use in the original experiment is not asserted.

## 1. Target and permitted information

Fix n, P, the finite training data, realized initialized matrices, and a
physical-time horizon T. The evolving network is exactly the fixed-P parent
in DEEP_CIRCLE_DERIVATION.md, equations (4)--(8), with the algebraic residual
RMS used at zero residual. All query responses use the same reconstructed
operators and their actual transposes. They never change the training
residuals, history sources, or clock.

Let theta lie in [0,2 pi), let dnu=dtheta/(2 pi), and let U(theta) be the
fixed normalized input curve. Assume U is bounded and measurable; the usual
circle parametrization is smooth. Let g be a fixed real bounded measurable
function on that circle. Define

    f(t,theta)=n^-1 sum_i c_i(t) h3_i(t,theta),
    E(t)=integral (f(t,theta)-g(theta))^2 dnu(theta),
    R(t)=sqrt(E(t)).                                      (1)

At fixed n the existing finite-horizon parent bounds, invoked explicitly in
SCALAR_COMPRESSION_BOUND_ASSESSMENT.md, bound all primitive training fields
and weights. The exact query responses satisfy |h_l(t,theta)|<=1. The
explicit parent RHS and bounded U then give uniform finite bounds on the
query velocities on [0,T]. Consequently E is differentiable and its
derivative can be passed through the integral: the difference quotients
are dominated by a constant on this probability space. No angular
derivative of g is needed.

Allowed preprocessing consists of contractions of the original initialized
network and the specified functions U,g. No trained trajectory supplies
coefficients or initial values. At every finite cutoff the running solver
stores finitely many real scalars and a finite coefficient table; it stores
neither an angular function nor neuron vectors. Retaining an angular
function as a single alleged scalar would violate this contract.

## 2. Exact energy velocity from the old population closure

Use the within-layer normalized pairings and history endpoint fields of
POPULATION_TO_AGGREGATES.md. For a training index a and query angle theta,
write

    C_l(theta,a)=mean_i h_l,i(theta) h_l,i(a),
    R_l(theta,a)=mean_i delta_l,i(theta) delta_l,i(a),
    S_l(a,theta)=mean_i Bbar_l,i(a) h_(l-1),i(theta),
    T_l(theta,a)=mean_i delta_l,i(theta) Abar_l,i(a),
    G(theta,a)=U(theta)^T U_a,

where l=2,3 for S_l,T_l and the mean is over the appropriate layer.
The symbol R_l is a backward-field pairing; R without a subscript is the
whole-circle RMS in (1). Put e(theta)=f(theta)-g(theta). The exact source
identity, applied at this query, is

    f_dot(theta)=-(2/M) sum_a r_a [C_3(theta,a)
                                  +G(theta,a)R_1(theta,a)]
       -(2/M) sum_(l=2,3;a) [r_a R_l(theta,a) S_l(a,theta)
           +rho T_l(theta,a)(C_(l-1)(theta,a)-S_l(a,theta))].       (2)

The source's C_(l-1)(a,theta) equals C_(l-1)(theta,a) by the symmetry of
the within-layer pairing. Differentiating (1) gives exactly

    E_dot=-(4/M) sum_a r_a integral e(theta)
                      [C_3(theta,a)+G(theta,a)R_1(theta,a)] dnu
       -(4/M) sum_(l=2,3;a) integral e(theta)
          [r_a R_l(theta,a) S_l(a,theta)
           +rho T_l(theta,a)(C_(l-1)(theta,a)-S_l(a,theta))] dnu.  (3)

These are scalar contractions. They are additional observables, rather
than functions determined automatically by E and the training loss.

For comparison, define the dense tangent expression at the same physical
state by

    K(theta,a)=C_3(theta,a)+G(theta,a)R_1(theta,a)
                        +sum_(l=2,3)R_l(theta,a)C_(l-1)(theta,a).

Rearranging (2), without any approximation, gives

    f_dot(theta)=-(2/M)sum_a r_a K(theta,a)
      +(2/M)sum_(l=2,3;a)(r_a R_l(theta,a)-rho T_l(theta,a))
                            (C_(l-1)(theta,a)-S_l(a,theta)).     (4)

The second line is the history-closure contribution. Omitting it would
change the parent being scalarized. Dense gradient flow at this state uses
only the first line. Even for dense flow, whole-circle error against g need
not decrease: training uses the finite training set, not the circle integral.
No sign claim for (3) is warranted.

## 3. The new diagrams must remember shared angles

Split the desired energy into three exact scalar quantities:

    Q(t)=integral f(t,theta)^2 dnu(theta),
    J(t)=integral g(theta) f(t,theta) dnu(theta),
    G2=integral g(theta)^2 dnu(theta),
    E(t)=Q(t)-2J(t)+G2.                                  (5)

In particular,

    Q=n^-2 sum_(i,j) integral c_i h3_i(theta)
                                  c_j h3_j(theta) dnu(theta).   (6)

The two neuron indices in (6) are independently summed, including
collisions. Their shared theta is integrated only once. In general (6)
does not equal [integral f(theta)dnu(theta)]^2. This is the central change
needed in the original disconnected-diagram factorization.

Extend that compiler with the following finite alphabet:

* Neuron vertices keep their layer colors, primitive training decorations,
  and initialized edges C_l=n W_l0.
* Add angle vertices. Each angle vertex carries its own integration
  variable and normalized measure nu.
* A query decoration h_l(v,alpha) names both its neuron vertex v and its
  angle vertex alpha. It has one of three response species, not a separate
  species for each numerical value of theta.
* Fixed angle decorations are U_j(alpha), j=1,...,d, and g(alpha).
  They have zero time derivative. Constants and the original finite
  training-input coefficients need no angle vertex.

Thus a mixed diagram H with v neuron vertices and a angle vertices denotes

    q_H=n^-v sum_(neuron assignments) integral_[circle^a]
            (product initialized edges)
            (product primitive and query decorations)
            (product fixed angle decorations) dnu^a.          (7)

Connectivity is taken in the full incidence structure, including the
links from query decorations to their angle vertices. Independent angle
variables are renamed when taking a disjoint union. If this full structure
is disconnected, both its neuron sums and angle integrals factor exactly:

    q_(H1 disjoint-union H2)=q_H1 q_H2.                       (8)

This follows by separating the finite sums and applying iterated integration
to the bounded product. It uses no probabilistic independence of neural
fields. Two neuronal components sharing an angle vertex are not disconnected
for (8). Hence Q in (6) is one connected mixed contraction.

Define size to be the number of neuron vertices, angle vertices, initialized
edges, primitive/query decorations, and fixed angle decorations. A query
decoration and its specified angle incidence count together as one
decoration; there is no separate incidence weight. With this convention

    size(training output)=3, size(Q)=7, size(J)=5, size(G2)=3.

G2 is constant and may be stored as a scalar coefficient. Canonical
relabeling of both kinds of vertices leaves finitely many diagram types
of each bounded size, independently of n and of angular quadrature size.

Differentiate each dynamic decoration by the original compiler's RHS.
Ordinary training replacements have one neuron root. A query replacement
has two marked attachment sites, its neuron v and angle alpha: substitute
the query chain rule at that same alpha. Every new query decoration and
U_j factor inherits this alpha;
training fields keep their original finite sample index. No differentiation
introduces an integral over a newly chosen angle, no g derivative is taken,
and no angle is replaced by a fresh independent copy. All operator actions
use the original initialized edges in both orientations.

There are finitely many replacement templates, because d,M,P and the
network depth are fixed. Applying the product rule and (8) therefore gives
an exact infinite hierarchy of global scalar contractions. Every equation
is a finite sum of products of connected mixed contractions, with the same
coefficient class as before: residuals, rho, fixed data, and inverse powers
of L. The residuals and rho depend only on training output coordinates.
There is a fixed bound on the total size increase and on the number of
factors in a replacement. The number and absolute coefficient sum of
replacement terms in a size-s row are at most a constant times s.

For the factor-count assertion, a query replacement need not connect its
two marked sites. For example, a first-layer gate's constant term can give
a neuron factor times U_j(alpha). Removing the one old query incidence can
split an originally connected diagram into at most two components; the
fixed replacement adds only its bounded number of extra components. Thus
the connected-factor count remains bounded independently of s. Assuming
that every query replacement is a single connected rooted tree would miss
this case, but is unnecessary for the proof.

Starting from Q,J, each connected descendant contains at most one angle
vertex: differentiation reuses that angle and cannot create another one.
Training-only factors can detach. This restriction can reduce the dictionary,
but the general definition (7) already suffices for the theorem below.

The earlier neuronal forest-pruning lemma must not be applied by simply
declaring every mixed diagram a tree. Sharing an angle can create cycles in
the incidence structure. Nothing in the finite-template convergence proof
requires this new incidence graph to be a tree.

## 4. Finite scalar closure and its finite-horizon guarantee

Retain connected mixed diagrams of size at most K, with K>=7, and the
training outputs and clock. Apply exactly the original deletion rule:
delete a generator monomial if any connected factor exceeds K. This gives
a finite autonomous unsaturated ODE, whose exact remainder is the sum of
the deleted mixed-diagram monomials evaluated on the parent. Exact hierarchy
identities do not by themselves bound that remainder after propagation.

The unsaturated construction inherits the local convergence proof in
SCALAR_COMPRESSION_BOUND_ASSESSMENT.md, section 7. Its arbitrary-finite-T
convergence remains unproved without an additional stability estimate.
For the following saturated variant the necessary estimate can be supplied.

For the true parent trajectory through T choose B_T>=1 bounding every
primitive field, every entry of the fixed C_l, and the suprema of U_j and g.
The primitive-field bound is the initial-data bound used in section 9 of
the assigned assessment. The query h_l need only the bound one. Every
summand in (7) is at most B_T^size(H) in absolute value; the n^v summands
cancel the prefactor and nu^a has total mass one. Therefore

    |q_H(t)|<=B_T^size(H), 0<=t<=T, for every mixed diagram.    (9)

This verifies the one genuinely new envelope obligation. Constants can
depend strongly on n,P,T, the original weights, and ||g||_infinity.

Choose R>=B_T and S_H(z)=max(-R^size(H),min(z,R^size(H))). If G_K is the
deleted finite generator just specified, evolve

    z_H_dot=G_(K,H)(S(z),L_z),
    L_z_dot=rho(S(z_training outputs)), L_z(0)=1,              (10)

from the exact initial mixed contractions. The query/energy coordinates
never enter the training residuals. Read out

    Ehat_K=S_Q(z_Q)-2S_J(z_J)+G2,
    Rhat_K=sqrt(max(0,Ehat_K)).                              (11)

Here the saturation thresholds depend on the declared horizon. They are
fixed before evolving (10), rather than estimated from the future path.

**Finite-horizon theorem.** At fixed finite n,P and for every prescribed
T<infinity under the stated parent bounds, (10) is a globally existing
finite autonomous scalar system and

    sup_(t<=T)|Ehat_K(t)-E(t)| -> 0,
    sup_(t<=T)|Rhat_K(t)-R(t)| -> 0, as K -> infinity.         (12)

Proof of applicability and convergence: the finite templates just verified
give constants A,D,delta independent of K such that

    |G_(K,H)(z,L)|<=A s(H)b^(s(H)+D)
       if |z_J|<=b^s(J), b>=1, L>=1.                       (13)

The product-rule count gives the factor s(H); the bounded total-size
increment and finite residual degree give D. Static U,g decorations are
already included in the diagram sizes. Deletion cannot worsen the absolute
bound. Training outputs have size three, so rho<=b^3+Y, where Y is the
training-label RMS. Saturation gives bounded coordinate velocities and
0<=L_z_dot<=R^3+Y. Each finite ODE is locally Lipschitz on L>0 and cannot
escape in finite time. On [0,T], with c=AT R^D,

    |z_H(t)|<=R^s(H)(1+c s(H))<=[R(1+c)]^s(H).             (14)

The inequality is the binomial inequality for integer s(H)>=1. This is
the required K-independent exponential envelope. True contractions satisfy
S_H(q_H)=q_H by (9), and clipping is nonexpansive:

    |S_H(z_H)-q_H|<=|z_H-q_H|.                            (15)

Thus saturation has zero extra defect on the target. Set R_T=R(1+AT R^D)
and L_*=1+T(R^3+Y). For m>=3 let E_m be the maximum of the coordinate
errors divided by R_T^size and the clock error divided by L_*, through
size m. Both true and surrogate paths obey the envelope, hence E_m<=2.
Telescoping each product, using (15), and using the Lipschitz property of
the residual norm gives one C_T independent of m,K with

    E_m(t)<=E_m(s)+C_T m integral_s^t E_(m+delta)(u)du,
                                      m+delta<=K.        (16)

There is no deleted source in these interior rows: their factors all have
size at most m+delta. The bounded factor count and size increase in each
template justify C_T independent of K. Inverse powers of L are Lipschitz
on L>=1, and the clock equation uses only size-three training outputs.

For h with C_T delta h<1, iterate (16) r times on [s,s+h]. The final
remainder is at most

    2 binomial(r+ceil(m/delta)-1,r)(C_T delta h)^r.        (17)

The preceding terms are a finite linear combination of initial errors at
levels m,m+delta,...,m+(r-1)delta. This follows by integration over the
ordered r-simplex, whose volume is h^r/r!, and by bounding
product_(j<r)(m+j delta)/r! with the displayed binomial coefficient times
delta^r. First send K to infinity with r fixed. If every fixed level
converges at s, all preceding terms vanish. Then send r to infinity; (17)
vanishes because its binomial factor has polynomial growth. Exact
initialization starts this induction at s=0. Finitely many such proof
intervals cover [0,T], proving uniform convergence of each fixed coordinate.
The actual ODE is never restarted or refreshed. Apply this result to Q,J,
use (5), and then the RMS inequality in section 5. This proves (12).

The explicit cutoff proof in the assigned assessment also extends: replace
its output size three by m0=7. With

    N=max(1,ceil(16 C_T delta T)), a=ceil(7/delta),
    j=floor(K/(delta 2^N)), j>=a,

the same halving-of-controlled-levels argument gives

    sup_(t<=T)|Ehat_K-E|
      <=2N (R_T^7+2R_T^5) 4^(-j).                       (18)

This is the sum of the size-seven Q bound and twice the size-five J bound;
G2 is exact and static. An ordinary finite cutoff therefore suffices for
any prescribed energy or RMS tolerance. The constants and sufficient cutoff
can be prohibitively large. No practical efficiency claim follows.

## 5. RMS, relative improvement, and fitting qualifications

The scalar closure need not preserve Ehat_K>=0. Set p=max(0,Ehat_K), and
suppose |Ehat_K-E|<=eta. Since E>=0, |p-E|<=eta. For a,b>=0,

    |sqrt(a)-sqrt(b)|^2<=|a-b|,

because |a-b|=|sqrt(a)-sqrt(b)|(sqrt(a)+sqrt(b)) and the second factor
is at least the first. Consequently

    |Rhat_K-R|<=sqrt(eta).                               (19)

To certify absolute RMS error epsilon without a positive residual floor,
an energy error bound epsilon^2 suffices. If R>0, the sharper identity
also gives |Rhat_K-R|<=eta/R. A uniform positive floor for R is not supplied
by the four inputs. Bounded g alone gives none: E=0 whenever f=g almost
everywhere, and the admissible bounded-target class includes such examples.
The nonzero-target case for the particular original experiment cannot be
decided without its missing target specification.

For a known positive reference RMS R_ref, define fractional RMS improvement
I=1-R/R_ref. Then

    |Ihat-I|<=sqrt(eta)/R_ref.                            (20)

Relative improvement is undefined when R_ref=0. To certify an improvement
of at least tau in [0,1], a sufficient energy inequality is

    Ehat_K+eta <= (1-tau)^2 R_ref^2.                      (21)

If instead an approximate function ftilde is available with
||ftilde-f||_(L2(nu))<=epsilon and ||f-g||_(L2(nu))<=B, expansion of the
square and Cauchy--Schwarz give

    | ||ftilde-g||_2^2-E | <=2B epsilon+epsilon^2.        (22)

This familiar residual bound is optional; the direct construction (11)
does not need an approximate function ftilde at all.

All estimates above are on a common physical-time interval. They do not
prove that training reaches a requested loss threshold or control two
models' different first hitting times. For example, if training outputs
have RMS prediction error at most epsilon_f, their training-residual RMS
values differ by at most epsilon_f. At a scalar stopping time within T,
sqrt(training loss_scalar)+epsilon_f<=tau certifies that the parent is
fitted to residual tolerance tau at that same time. Comparing separate
first threshold crossings requires additional crossing/stability control.

The fixed-P target remains distinct from dense training. If a parent
estimate gives ||f_P-f_dense||_(L2(nu))<=epsilon_P on the common horizon,
the reverse triangle inequality yields directly

    |Rhat_(P,K)-R_dense|<=sqrt(eta_(P,K))+epsilon_P.       (23)

The old-clock physical-state estimate reported in the assigned assessment
has the history rate C_T/sqrt(P(P+1)). Extending its readout to the circle
requires a uniform bounded-input readout constant; finite n, compact circle
inputs, bounded physical states, and |tanh'|<=1 supply that constant by
telescoping the three layer maps. The parent physical estimate itself is
used here as reported in that source, not independently re-proved. One
chooses P for the parent error, then K for that fixed P. Neither interchanging
the limits nor a width-uniform cutoff follows from (23).

## 6. Preprocessing and what this does not recover

The finite hierarchy requires initialized mixed integrals. In general these
are not available in elementary closed form, even when g is a finite Fourier
sum, because the initialized tanh responses enter them. They may be computed
once by angular integration. No passive test-grid response variables are
then evolved, and no neuron-level query pass is needed to report Ehat or
Rhat. This distinction removes a runtime test grid; it does not assert free
or exact finite-cost angular initialization.

The exact-initialization theorem treats these finitely many integrals as
specified real numbers, just as the original scalar construction treats
initial contractions. An effective numerical construction needs certified
approximations. For smooth specified U,g, every initialized integrand is a
finite smooth expression on a compact angle domain; derivative bounds from
the original weights and target give elementary integration error bounds.
For each fixed K, continuous dependence of the locally Lipschitz saturated
ODE bounds the propagated initialization error. One can therefore choose a
finite integration precision for any requested output tolerance. For an
arbitrary bounded measurable g given only by an evaluation oracle, this
computable-integration conclusion is unavailable without extra assumptions.

No dense weights, individual neuron labels, or arbitrary-angle function
are reconstructed by (11). Such reconstruction is a stronger request than
one scalar integral and is unnecessary to answer the RMS question. The
construction may nevertheless require many moments and expensive initial
contractions. Recoverability of dense parameters, the utility of a small
cutoff, width-independent accuracy, and existence of an infinite-population
dictionary remain separate open matters. In particular, adding the angle
integral does not cure the initialized-edge population-limit issues already
identified in the supplied scalar compiler.

## 7. Claim status and frozen provenance

| Claim | Status and scope |
|---|---|
| Energy identities (3)--(6) | Exact at finite n on the consistent old fixed-P parent |
| Mixed-diagram generator and shared-angle factorization | Exact finite algebra and bounded-integral identities |
| Finite type count at bounded cutoff | Proved; independent of n and angular sampling resolution |
| Saturated finite-T energy/RMS approximation | Proved under the parent bounds stated in the assigned assessment and bounded specified U,g |
| Unsaturated arbitrary-finite-T convergence | Open; the new observable does not remove its stability gap |
| Effective initialization for an arbitrary bounded oracle target | Not established; target representation/integration assumptions are needed |
| The original experiment used finite Fourier g | Not established by the permitted inputs |
| Practical small state, fitted endpoint, exact parameter recovery, width limit | Not established by this note |

This report extends the observable scope of the supplied saturation theorem;
it does not supersede the theorem's finite-width or practical limitations.
No empirical claim or independent promotion verdict is made. The completed
first report is frozen before sharing findings with other agents; later
collaborative corrections, if any, must be recorded as such.

Scientific inputs were read in full, and no links to other research sources
were followed. Read-version SHA256 hashes:

| Input | SHA256 |
|---|---|
| POPULATION_TO_AGGREGATES.md | 99cf7504e058e076d68ecd4e61c1493e7ce1d2c11dcf94f544012d507b529ebb |
| POPULATION_SCALAR_CONSTRUCTION_CHECK.md | 8a2e44ad6d50995ef626a65402babed19b761f9685d9ef91fb63de7633944383 |
| SCALAR_COMPRESSION_BOUND_ASSESSMENT.md | e80540f9052049ee6e805037af99a57a83aa9acd0d98a3ff1f42d2ff39cd5309 |
| DEEP_CIRCLE_DERIVATION.md | 17ffa7efe44d588a47b8f566c5cbdc72199e012ae058bab232427e6685203bd9 |

Required process inputs: solve-math-rigorously/SKILL.md;
investigate-conjectures/SKILL.md and its research-contract, evidence-ledger,
and adversarial-audit references. The supervisor's scoped input list replaced
ordinary author startup reading. This agent wrote only this report and made
no Git mutation. The supervisor owns the README and any synthesis.

## 8. Post-freeze collaborative audit of the selected Fourier design

The first independent direct-RMS report above was frozen at SHA256
87b9acfb27789e769bf763c0bd7d33f99229d2170e1cdec60b8eaa1e47378090.
After that freeze, the supervisor requested a complete audit of the root
synthesis and Fourier route, together with a proposed common-generator
organization. The user now selects the Fourier route. This addendum records
that collaborative check; it is not a new independent review and does not
retroactively attribute the shared design to the first report.

The two additional scientific files were read completely:

| Read version | SHA256 |
|---|---|
| SCALAR_CIRCLE_FUNCTION_READOUT.md | b09574355d4742cba2e6bc8331dfce8804a3e4b0a80db3836f43b5c0a63c6d32 |
| SCALAR_FOURIER_READOUT.md | c9191360c815dea1469ed2a7c060df24216273b988c55477d4c23d1b048a120a |

The first file is the complete synthesis version before its announced
rewrite around the selected Fourier organization. The audit conclusion is
positive with the explicit bookkeeping qualifications below. No experiment
or implementation was performed.

### 8.1 One common generator for the weighted blocks

Use the real weight list

    w in {1, cos(k theta), sin(k theta): 1<=k<=J}.

Choose one common list of connected single-angle diagram types D, with the
weight tag suppressed in the type name but retained in its size. All copies
have this same list, same cutoff, and same formal simplification rules.
Define the vector

    Q_w,D=integral w(theta) Phi_D(theta) dnu(theta),       (24)

where Phi_D is the normalized neuronal contraction including its static
input-coordinate factors. Keep the Fourier weight separate from those
factors. In particular, do not rewrite a product cos(theta)cos(k theta)
as a combination of neighboring weight tags before applying the cutoff.
Such a rewrite is mathematically possible, but it would give a different
organization and a potentially different finite truncation.

Differentiating a single-angle type produces no new angle. The one existing
angle vertex survives even if every dynamic query incidence is removed;
its fixed weight remains attached. After exact full-incidence factorization,
each monomial therefore consists of precisely one angular coordinate and
some training-only coordinates. It never has a product of two separately
integrated angular coordinates. This remains true for energy integrands
such as f(theta)^2, because their two output factors share this one angle.

More explicitly, each row has the form

    (Q_w,D)_dot=sum_nu a_Dnu(q_train,L)
                   [product training factors] Q_w,D'(nu).     (25)

The symbolic replacement and training factors do not depend on w: w has
zero time derivative and is transported unchanged through each replacement.
Collecting terms after the common deletion rule proves the finite identity

    Q_w_dot=A_K(q_train,L) Q_w                              (26)

for the unsaturated angular closure. Entries of A_K include the retained
training contractions, residual norm and inverse powers of L. The training
closure is still nonlinear and autonomous. Conditional linearity in Q_w
does not mean that the Fourier output coefficients alone close, or that
the underlying feature-learning dynamics are linear.

Pure static angular integrals must be included as coordinates with zero
derivative in (24). Examples are integral w(theta)p(U(theta))dnu. Without
them, a term of (25) can become a known mode-dependent forcing. If
Q_w=(V_w,b_w), with b_w constant, eliminating b_w gives

    V_w_dot=A_VV(q_train,L)V_w+A_Vb(q_train,L)b_w.          (27)

Thus (26) is homogeneous only for the extended block retaining these
constants. Keeping a static coordinate which happens to vanish for one
weight is harmless and preserves the common matrix. Eliminating it only
for that mode breaks the literally identical block representation.

A query template has a neuron and an angle attachment site. Their removal
or separation can split an old connected component into at most two,
as already checked in section 3. This verifies the bounded-factor part of
the generator argument even when the resulting angular factor is purely
static. Treating every substitution as a connected one-root tree would
leave this step unjustified; both the detailed Fourier route and this
addendum explicitly cover it.

For literally identical whole blocks, the common dictionary must contain
the energy type in every mode copy if it contains it at w=1. Only its
zero-mode value is needed for the final energy readout, but the unused
copies integral w f^2 may remain in the state. An economical alternative
adds the energy type and its descendants only to the zero-mode block;
then that block is augmented, and one should not call all full blocks
identical or assign them a single matrix of the same dimensions.

### 8.2 Saturation, passivity, and grades

With the common dictionary, the clipped finite angular equations are

    Q_w_dot=A_K(S_train(q_train),L) S_ang(Q_w).             (28)

Because |w|<=1 for every listed weight, the same angle-coordinate caps
can be used across modes. Formula (28) is generally nonlinear in Q_w after
clipping; it is not an equation with one common linear propagator. The
common matrix-valued coefficient table nevertheless remains reusable.

All training coefficients, coordinate lists, cutoff decisions and valid
training caps must stay fixed when these passive blocks are added.
Changing a training cap to a larger value changes the finite training ODE,
even though the angular quantities still do not enter it. The root
synthesis correctly identifies this distinction. For the convergence proof,
one may take a larger common exponential envelope bounding the separate
training and angular caps without changing the actual caps in (28).

The inherited proof applies to (28). The same-angle generator has bounded
size increment, bounded factors per monomial and O(size) row growth. All
fixed Fourier weights are bounded by one. Saturation therefore bounds every
coordinate velocity, supplies the exponential envelope for the raw states,
and is the identity on the true mixed contractions. The error recursion
through levels m,m+delta is unchanged. The finite-horizon conclusion remains
conditional only on the upstream parent bounds already invoked by the
assigned assessment, not on a new assumed scalar-realizability property.

There is one grading correction when combining certificates from the two
routes. The Fourier report counts a weight tag even for w=1. With that
convention, training outputs have grade 3, Fourier output coordinates have
grade 5, and the energy type integral f^2 has grade 8:

    2 neuron vertices + 1 angle vertex + 4 dynamic decorations
                                      + 1 weight tag = 8.

The original direct-RMS report used no redundant tag for the unweighted
energy and therefore assigned it grade 7. Both conventions are valid, but
one certificate must use one convention consistently. For the selected
tagged Fourier-plus-energy design, use maximum readout grade s_*=8 and
K>=8. The formulas in the Fourier source using s_*=5 concern its Fourier
coefficient outputs alone. Replacing 5 by 8 in the same proved formula
controls the added energy output as well.

At fixed angular cutoff the number of stored angular coordinates scales
with the number of requested weight copies. Sharing A_K saves duplicate
symbolic coefficient tables, not the need to evolve each block's auxiliary
contractions. The construction makes no small-state or speedup guarantee.

### 8.3 Two RMS quantities and the energy-plus-Fourier identity

Let c_k=integral f exp(-ik theta)dnu and g_k=integral g exp(-ik theta)dnu.
The selected design can return the finite polynomial

    fhat_J(theta)=sum_(|k|<=J) chat_k exp(ik theta).         (29)

Its own exact squared error, using consistent reference data, is

    E_polynomial=||g||_2^2+sum_(|k|<=J)|chat_k|^2
                     -2 Re sum_(|k|<=J)chat_k conjugate(g_k).    (30)

This formula includes the reference's entire energy, including any modes
outside J. It needs no evaluation grid. Its comparison to the parent
network uses the Fourier approximation error, including the parent's
omitted spatial tail. The root and Fourier reports state this distinction
correctly.

Let A=integral f^2 dnu be the separate zero-mode energy coordinate.
If the specified reference satisfies g_k=0 for |k|>J_g and J>=J_g, then
the parent network's exact squared error is

    E_parent=A-2 Re sum_(|k|<=J_g)c_k conjugate(g_k)+||g||_2^2.   (31)

This follows by expanding ||f-g||_2^2 and inserting the finite Fourier sum
for g inside its cross term. It makes no assumption about the Fourier
support of f. All high-frequency learned energy remains inside A. Thus
approximating (31) needs coefficient errors and the energy-coordinate error,
but no learned-function Fourier-tail estimate.

Writing d_g=(sum_(|k|<=J_g)|chat_k-c_k|^2)^(1/2), Cauchy--Schwarz gives

    |Ehat_parent-E_parent|<=eta_A+2||g||_2 d_g,             (32)

where |Ahat-A|<=eta_A. The clipped square-root readout then has RMS error
at most sqrt(eta_A+2||g||_2 d_g). This use of the direct-energy observable
is compatible with the chosen Fourier function evaluator, while reporting
a different finite-cutoff metric from (30).

When g is supported within J, subtraction of the two approximate formulas
gives the exact algebraic diagnostic

    Ehat_parent-E_polynomial=Ahat-sum_(|k|<=J)|chat_k|^2.   (33)

With exact A and c, the right side is the nonnegative learned Fourier-tail
energy sum_(|k|>J)|c_k|^2. At a finite scalar cutoff it may be negative,
because the approximate moments need not be realizable. No positivity or
ordering of the two approximate RMS readouts should be assumed.

For a general specified g in L2, truncating only its correlation gives
the omitted squared-error term bounded by

    2||f||_2 ||g-g_(J_g)||_2.                              (34)

If the energy and chosen Fourier coordinates are the only evolved angular
observables, g does not enter their compiler at all. Therefore L2 reference
data suffice for (30)--(34); the stronger bounded-g assumption of the
direct g-weighted compiler is unnecessary for this particular organization.
The four original inputs still do not establish that the experiment's
actual g is bandlimited. Equation (31) must stay conditional until that
reference is specified or its definition is checked in an authorized scope.

Finally, the two sources use different epsilon conventions in their simple
coefficient estimates. If each complex coefficient has modulus error at
most epsilon, the coefficient L2 error is at most sqrt(2J+1)epsilon. If
the theorem instead bounds each stored real cosine/sine coordinate by
epsilon, then c_k=u_k-i v_k and conjugate symmetry give

    sum_(|k|<=J)|chat_k-c_k|^2<= (4J+1)epsilon^2.           (35)

Both stated estimates are correct under their respective definitions; they
must not be interchanged when presenting a quantitative certificate.

### 8.4 Audit disposition

The mixed-angle compiler, saturation proof transfer, spectral spatial-tail
bounds, and distinction between polynomial RMS and parent-network RMS pass
this scoped collaborative check. The proposed common A_K organization is
valid with a common unsimplified tagged dictionary and retained static
angle integrals. The required presentation qualifications are the grade-8
energy convention, the identical-block versus zero-mode-only enlargement
choice, unchanged training caps, and the real-versus-complex error constant.
No decoder, implemented solver, efficient cutoff, width-uniform theorem,
or fitted stopping-time guarantee is established by this audit.

## 9. Whole-candidate check of the final Fourier synthesis

The supervisor requested a further complete check of the final selected
design. This agent read all of SCALAR_CIRCLE_FUNCTION_READOUT.md at SHA256
786cff262ff17f22662c8ec922e19c86a18aec06e2759fb07b66fa731cf108cf,
then read the complete final clarification version at SHA256
c771be0dee6d4672fb9a6db7f3c64295bf63a0760e884285dd04a67ee1918a77.
The latter hash is the candidate covered by this verdict. The two added
clarifications explicitly restrict the selected blocks to one angle and
one weight tag, and justify transferring a physical-weight error bound
uniformly to the compact input circle.

**Verdict:** no correctness issue requiring revision was found in this
complete candidate under its stated fixed-n, fixed-P, finite-horizon and
inherited parent-bound assumptions. This is a version-specific internal
collaborative check, not an independent promotion review. No code or
experiment was run, and no further linked research files were read.

### 9.1 Complete design and theorem checks

The candidate now specifies the single-angle subfamily needed for its
matrix form. Starting Fourier and energy diagrams have exactly one angle;
replacement preserves that angle and its one unchanged test-weight tag.
Factoring full incidence components leaves one angular factor and ordinary
training factors. Thus the common homogeneous A_K is valid for the stated
identical dictionaries, with static angular integrals retained. The
candidate does not apply that claim to the optional general multi-angle
notation. Query replacements with two attachment sites, possible separation
into two components, and the bounded factor count are all accounted for.

The grade convention is now consistent throughout: Fourier readout grade
5, energy grade 8, identical energy-pattern copies in every mode, and
maximum requested grade 8 for the combined cutoff certificate. Training
caps and coefficients remain unchanged. Saturation makes the angular
equations nonlinear but preserves the common matrix-valued coefficient
table. The proof retains the initial-data envelope, bounded velocities,
nonexpansive clipping, interior error recursion, and finite proof-interval
continuation of the original checked theorem. The explicit grade-halving
bound is applied with its correct readout grade and no hidden runtime
refresh. The storage count and matrix-application count are stated only
for a fixed dictionary; they do not claim efficient approximation.

The Fourier approximation identities, H1 tail estimate, conservative
uniform tail estimate, Parseval reference-error formula, and separate
real-versus-complex coefficient error constants all check algebraically.
The candidate distinguishes polynomial RMS from the parent-network RMS
estimated using the energy coordinate. It retains the reference's complete
L2 norm and assumes finite target support only in the explicitly conditional
energy-plus-finite-correlation identity.

The new physical-weight-to-circle bridge is valid: take a compact finite-
dimensional parameter ball containing both compared trajectories and their
line segments. The neural readout is continuously differentiable on this
ball times the compact input circle. Its derivative norm has a finite
maximum there, and integration along each parameter segment proves a
uniform-in-angle Lipschitz bound. This converts the upstream physical-weight
estimate, not merely a finite training-output estimate, to the claimed
circle comparison. The upstream theorem remains an inherited input rather
than a theorem re-proved by this audit.

### 9.2 Explicit complex-strip proof

The candidate's new analytic-strip argument is valid for the specified
bias-free tanh network and sinusoidal circle. For real x,y,

    |tanh(x+iy)|^2=(sinh(x)^2+sin(y)^2)
                                  /(sinh(x)^2+cos(y)^2).

For |y|<=pi/4 the denominator is positive and its numerator is at most the
denominator, giving |tanh|<=1. Also

    |Im tanh(x+iy)|=|sin(2y)|/(cosh(2x)+cos(2y))<=2|y|,

because the denominator is at least one and |sin(2y)|<=2|y|. These bounds
do not require a bound on the real part x.

At theta+i eta, the input imaginary part is bounded in the infinity norm
by b sinh(|eta|), with b=||u_c||_infinity+||u_s||_infinity. Multiplication
by the real weight matrices and the preceding imaginary-part estimate
give layer preactivation bounds

    b a1 sinh(|eta|),
    2b a1 a2 sinh(|eta|),
    4b a1 a2 a3 sinh(|eta|).

For D=b a1 max(1,2a2,4a2a3)>0 and sigma=asinh(pi/(8D)), all three are
at most pi/8 on the closed sigma strip. The induction is legitimate: the
first bound puts layer one inside the region where the tanh inequalities
hold, after which they imply the second bound, and then the third. The
strict margin to pi/4 persists on a slightly larger strip, so all composed
functions are holomorphic on a neighborhood of the closed sigma strip.
Their activations have modulus at most one, giving |f|<=||c||_1/n.
If D=0, either the input curve or W1 is identically zero under these valid
norm bounds; with no biases, the entire response and output are zero.

The Fourier contour shifts have the correct directions and signs: shift
downward for positive k and upward for negative k. Periodicity cancels the
vertical contour sides, giving |c_k|<=A_T exp(-sigma |k|). Summing the
geometric series for squared coefficients or absolute coefficients gives
both tails in candidate equation (7a), including their sqrt(2) and 2
prefactors and their respective denominators. These bounds are uniform
through T when a1,a2,a3,A_T are uniform parent bounds. They do not imply
any useful width-uniform strip, as the candidate explicitly states.

The A_T symbol may use any known upper bound for the displayed supremum.
For example, the true parent's outer-weight equation gives

    d/dt (||c||_2^2/n)=-4 mean_a r_a f_a
                     <=mean_a y_a^2=Y^2.

Cauchy--Schwarz therefore permits the initial-data upper bound

    A_T<=sqrt(||c(0)||_2^2/n+T Y^2).

This observation confirms that defining the analytic bound requires no
future-trajectory oracle. The candidate already states that parent bounds
supply these constants; no amendment is required for this choice.

### 9.3 Energy-tail certificate

Put delta=c_(<=J)-chat_(<=J). Parseval gives

    T_J=A-||c_(<=J)||_l2^2>=0,
    That_J=Ahat-||chat_(<=J)||_l2^2.

Subtraction and direct expansion give

    That_J-T_J=(Ahat-A)
                +2 Re <chat_(<=J),delta>+||delta||_l2^2.

Thus |delta|_l2<=d and |Ahat-A|<=epsilon_A imply exactly the candidate's
equation (15),

    |That_J-T_J|<=epsilon_A+2||chat_(<=J)||_l2 d+d^2.

Consequently the displayed nonnegative upper bound for T_J is valid, and
the function-error squared is at most that bound plus d^2 by the exact
orthogonal decomposition. The certificate must use certified coordinate
errors, as the candidate states. Merely observing a small or negative
That_J gives no theorem. Clipping a possibly negative energy-error estimate
before taking its square root is likewise justified by the nonexpansiveness
and one-half Holder estimates already checked in this report.

### 9.4 Polynomial-decoder qualification

The new brief decoder alternative correctly removes an overly strong
reading that every circle predictor requires new angular coordinates.
Its summarized approximation can be checked directly without following
the additional file link: for x in [-R,R], put p=(x+R)/(2R) and let
B have the binomial law with parameters m,p. The Bernstein polynomial

    p_m(x)=E[tanh(-R+2RB/m)]

lies in [-1,1], and tanh's real Lipschitz constant one gives

    |p_m(x)-tanh(x)|<=2R E|B/m-p|
                    <=2R sqrt(p(1-p)/m)<=R/sqrt(m).

For R=0 the activation is exactly zero and needs no approximation. At
positive preactivation bounds, the range property keeps the next layer's
polynomial preactivation within the corresponding row-sum bound. Iterating
the tanh Lipschitz estimate gives the three-layer readout error bound

    (||c||_1/n)(delta3+a3 delta2+a3 a2 delta1),

where delta_l is that layer's uniform activation approximation error.
Each polynomial forward pass expands into finitely many rooted products,
actual initialized actions, and learned A/B pairings, followed by a global
readout contraction. These are existing tree-contraction expressions, with
powers of L in their scalar coefficients. For sinusoidal inputs the result
is a finite trigonometric polynomial. Therefore a sufficiently rich retained
training dictionary can support this approximate terminal readout, with a
separate approximation and aggregate-error bound. This does not contradict
the selected direct spectral design, does not reconstruct labelled weights,
and does not supply unavailable contractions to an arbitrary small state.

The linked SCALAR_DECODER_LIMITS.md itself was outside this final audit's
input request and was not read. The check here concerns the mathematical
summary actually included in the complete frozen candidate. No claim about
that linked report's complete contents or review status is made.

All previous limits remain explicit in the checked candidate: fixed finite
width, prescribed finite time, initialization integrals, potentially enormous
cutoffs, separate P/K/J errors, no empirical speedup, and no proof of
loss-threshold hitting-time comparison. This completes the whole-candidate
internal check at the final hash recorded above.
