# What a terminal scalar state can decode

2026-09-25. Scoped theoretical assessment for the existing scalar-contraction
construction. Status: complete bounded derivation, internally checked by its
author; no experiment, implementation, or independent promotion review.
The first version was completed before receiving another route's findings.

## 1. Conclusion and scope

The terminal state is not automatically a set of trained neural weights.
The existing finite-horizon output theorem by itself proves neither a weight
inverse nor a new-angle readout. Nevertheless, pre-evolving a query mesh is
not mathematically necessary: a sufficiently rich training-only contraction
dictionary admits a terminal polynomial readout approximating the whole circle.
Section 4 gives a direct construction. Its coefficients are computed from
permitted bounds and a scalar approximation of tanh, with no trained trajectory
or test-angle responses. It can be coupled to the saturated scalar convergence
theorem, although neither the resulting cutoff nor numerical conditioning is
known to be practical.

These statements coexist with an exact obstruction. At every fixed diagram
cutoff K, there are finite-width stationary networks with identical retained
training-only contractions and different circle functions. Section 3 proves
this for an explicitly stated deterministic family; it does not concern the
one prescribed Gaussian realization or prove an almost-sure Gaussian claim.
Increasing the dictionary can improve approximate function recovery. No
dimension-counting argument establishes impossibility for the actual run.

The target used below is the old-clock, finite-n, fixed-P population closure
with its actual initialized W20 and W30. Its terminal reconstructed weights
are (W1, What2, What3, c). These are the population closure's weights, not
identically the dense-gradient-flow weights at finite P. Comparison to the
dense function has a separate P error and requires matched finite physical
time. No statement here proves accuracy at two models' different loss-based
stopping times or at an infinite-time fitted endpoint.

Scientific inputs were restricted to the four files listed in section 7,
all read completely. Required process inputs were the rigorous-math skill,
the conjecture skill, and its research-contract, evidence-ledger and
adversarial-audit references. No other study, prior route report, code,
experiment, or external scientific source was used.

## 2. Exact recovery is a question about fibers and permitted side information

Let X denote an admissible physical population state, A_K(X) its retained
diagram values and clock, and F(X) its entire circle function in
C(S^1). Include in A_K any additional initialization-dependent scalar
coefficients that a proposed decoder is permitted to inspect. A single-valued
exact decoder D_K exists on the image of A_K if and only if

    A_K(X)=A_K(Y) implies F(X)=F(Y).                    (1)

Necessity follows by evaluating D_K on the common aggregate. For sufficiency,
define D_K(q) to be F(X) for any X with A_K(X)=q; the implication makes this
independent of the choice. This is a set-theoretic criterion. Computability,
continuity and conditioning of D_K require further hypotheses.

For an approximate decoder and a pair in one fiber, the triangle inequality
gives

    max(||D_K(q)-F(X)||_infinity,
        ||D_K(q)-F(Y)||_infinity)
       >= (1/2)||F(X)-F(Y)||_infinity.                 (2)

The same logic applies to the map from admissible initializations to terminal
scalar-solver states. It is not enough to count coordinates: a restricted
reachable family might be much smaller than the ambient state space, and
arbitrary real encodings cannot be ruled out by informal counting.

All completely summed diagrams are invariant under consistent independent
permutations of neurons in each layer. Such permutations relabel W1, c,
the moment fields and both endpoints of the initialized matrices. Thus the
diagram dictionary cannot recover the original labelled weight arrays over
a family allowing this relabelling, even if every diagram is supplied.
The network function is unchanged by the same permutations, so this argument
does not obstruct function recovery or recovery of a representative network.
If labelled initialized matrices or a full seed are side information, the
admissible fiber must be defined conditional on that information instead.

For a single fixed initialization, data set and physical time T, uniqueness
of the parent ODE already defines one physical terminal state. Retaining the
whole initialization or a reproducible seed and replaying that ODE recovers
that state, up to numerical error. This uses the original evolution and its
population/matrix work; it is not an inverse supplied by the terminal scalar
compression. A decoder that simply hard-codes that one trajectory would
likewise evade the intended compression question. The present sources do
not establish an impossibility theorem for every efficient decoder on the
single initialized trajectory, nor an efficient exact decoder there.

## 3. An exact finite-cutoff collision with different circle outputs

Here the admissible family consists of deterministic finite networks with
the specified three tanh layers and fixed-P initialization rules. It is a
broad restart/initialization family, not the prescribed Gaussian draw.
Take K>=3, d=2, M=1, U(theta)=(cos(theta),sin(theta)), training angle zero,
label y=0, L=1, and any P>=1. Set

    n=2^(K-1),  W20=W30=I_n,  c_i=1,
    W1[i,:]=(0,b_i),
    A2=A3=B2=B3=0,  h1,train=h2,train=h3,train=0.       (3)

These are consistent initialized population states: at the training input
all activations vanish, and the required prefix B0 equals the zero activation.
The training residual is exactly zero. Consequently every physical weight,
response and moment velocity vanishes, as does the clock velocity. Both
dense gradient flow and every fixed-P closure remain at (3).

Construct two multisets of b values. For j=0,...,K, use b0+jh with
multiplicity binomial(K,j); assign the even j to the first multiset and
the odd j to the second. Each contains 2^(K-1) entries, since adding and
subtracting the binomial identities at 1 and -1 gives equal parity sums.
For every integer 0<=r<K,

    sum_(j=0)^K (-1)^j binomial(K,j)(b0+jh)^r=0.        (4)

One proof is that each forward difference lowers the degree of a polynomial
by at least one, so its K-fold forward difference is zero at degree below K.

For a connected diagram H with v vertices and e initialized edges, each
edge C=nI forces its two neuron indices to coincide. Connectivity forces all
indices to coincide. Any nonzero decoration in (3) is either the constant
c=1 or a power of b; the training-response/history decorations are zero.
Therefore every nonzero connected diagram has the value

    q_H=n^(e-v) sum_i b_i^r,                           (5)

where r is its number of second-column W1 decorations. Because
v+e+number_of_decorations<=K and v>=1, r<=K-1.
Equation (4) makes (5) identical in the two networks. Zero-valued diagrams,
static diagrams, training outputs and clocks coincide as well. This proves
equality of the entire specified cutoff dictionary, including cyclic graphs,
not merely equality of a few moments. Backward fields, if redundantly
included in the initial observable list, are identical constants here and
do not distinguish the pair.

At theta=pi/2 the outputs instead are the averages of

    phi(b)=tanh(tanh(tanh(b))).                         (6)

This function is smooth, bounded and nonconstant. Its Kth derivative cannot
vanish identically: repeated integration would make it a polynomial of
degree below K, whereas a bounded nonconstant polynomial on R cannot exist.
Choose b0 where phi^(K)(b0) is nonzero, and choose h>0 small enough that this
derivative has a constant nonzero sign on [b0,b0+Kh]. Repeated application
of the fundamental theorem of calculus gives

    sum_(j=0)^K (-1)^(K-j) binomial(K,j) phi(b0+jh)
      = integral_[0,h]^K phi^(K)(b0+s1+...+sK) ds.      (7)

The right side is nonzero. The two normalized sums of (6), and hence the
two circle functions, differ.

At zero residual the scalar generator vanishes, so both scalar terminal
states remain identical for every T. The same holds for saturation using
common sufficiently large bounds. Thus no exact universal new-angle decoder
from this fixed cutoff dictionary exists on this deterministic family.
Additional initialization-dependent side channels are excluded unless they
also agree for the pair; they cannot silently be appended to this conclusion.

The scope matters. The construction changes the initialization and lets n
grow with K. It is not a collision on the one prescribed initialized orbit,
not an almost-sure assertion for Gaussian matrices, and not a lower bound
bounded away from zero uniformly in K. It therefore does not contradict
approximation at fixed n as K increases, or the construction in section 4.
In particular, a different pair of labelled weights related only by neuron
permutations would not have proved the function claim above.

## 4. A constructive terminal readout without a query mesh

The full training-only dictionary already contains the ingredients of the
physical forward map: W1-column decorations, c, the learned factors A and B,
the initialized edges, and L. They can be combined at readout time using
polynomial approximations to tanh. Query-response species are unnecessary
for this construction. A small mean/Gram list alone need not contain the
required higher diagrams; the dictionary must include them before training.

Fix a finite horizon and bounds, uniform over the target trajectory,

    ||U(theta)||_2<=U_*,  ||W1||_op<=a1,
    ||What2||_op<=a2,  ||What3||_op<=a3,
    ||c||_2/sqrt(n)<=a_c.                             (8)

These are fixed-n bounds computed from permitted initial information and
the horizon, as required by the saturation theorem. They are not future
trajectory observations. Set R1=a1 U_*, R2=a2 sqrt(n), R3=a3 sqrt(n).

An explicit degree-m polynomial approximates tanh on [-R,R]. For R>0 let
s=(z+R)/(2R), and define

    p_(R,m)(z)=sum_(j=0)^m tanh(2R j/m-R)
                         binomial(m,j) s^j(1-s)^(m-j). (9)

For z in this interval the coefficients are convex weights. Hence |p|<=1.
If J has binomial(m,s) probabilities, the 1-Lipschitz property of tanh and
Cauchy--Schwarz give

    |p_(R,m)(z)-tanh(z)|
      <=2R E|J/m-s|
      <=2R sqrt(s(1-s)/m)<=R/sqrt(m).                 (10)

For R=0 take p=0 on its singleton domain. This proves both the approximation
and range bounds directly. The scalar nodes in (9) approximate an activation
function; they are not a mesh of test angles or evolved query responses.

Choose p1,p2,p3 with degrees m1,m2,m3 and errors eta1,eta2,eta3 given by
(10). Form the hypothetical physical readout

    v1(theta)=p1(W1 U(theta)),
    v2(theta)=p2(What2 v1(theta)),
    v3(theta)=p3(What3 v2(theta)),
    F_poly(theta)=c^T v3(theta)/n.                     (11)

All polynomial applications are componentwise. The convex range bound
ensures ||v1||_2,||v2||_2<=sqrt(n), so the intervals chosen above also contain
the approximate preactivations. Layerwise subtraction, the 1-Lipschitz
property of tanh and the operator norm bounds give

    ||v1-h1||_2<=sqrt(n) eta1,
    ||v2-h2||_2<=sqrt(n)(eta2+a2 eta1),
    ||v3-h3||_2<=sqrt(n)(eta3+a3 eta2+a3 a2 eta1).

Consequently, uniformly in the angle and through the chosen horizon,

    |F_poly(theta)-F(X)(theta)|
      <=a_c(eta3+a3 eta2+a3 a2 eta1).                 (12)

Equation (11) specifies the readout being represented, not an instruction
to reconstruct neuron arrays at runtime. Substitute exactly

    What_ell=W_ell0
      -(2/(MnL)) sum_(a,k<P)(2k+1) A_(ell,k,a) B_(ell,k,a)^T

into (11), then expand the three finite polynomials. Each initialized action
adds its actual edge; each learned action is a local A field times a
normalized B pairing; products merge roots of neuron-valued expressions;
the final normalized c pairing closes the remaining root. These are exactly
the construction note's diagram operations. Disconnected factors are products
of connected contractions. There are finitely many terms, so the expansion
is a finite expression

    D_poly(q,L;U)=sum_alpha U^alpha D_alpha(q,L),       (13)

where every D_alpha is polynomial in finitely many connected diagram values
and rational in L with only powers of L in denominators. All coefficients
come from the data, P and (9). There is a finite maximum diagram grade K0,
computable by performing this symbolic expansion. All these diagrams are
forests; a dictionary retaining all tree types through K0 suffices.

Thus for exact retained aggregate values and K>=K0, (13) equals (11)
identically. Increasing the three polynomial degrees makes (12) arbitrarily
small, at the cost of larger K0. This proves a query-free approximate
function decoder from appropriate finite global contractions. It does not
provide an exact finite polynomial identity for tanh or actual weights.

To use independently evolved scalar states, fix the polynomials first.
The saturated theorem in SCALAR_COMPRESSION_BOUND_ASSESSMENT.md, section 9,
states convergence of every fixed diagram and the clock, uniformly on the
finite horizon as K tends to infinity. It applies to the training-only
dictionary and its fixed readout diagrams. Evaluating (13) on clipped scalar
coordinates gives a continuous function of finitely many converging values;
L>=1 prevents singular denominators. More quantitatively, on the fixed
coordinate bounds, every partial derivative of the finite expression (13)
is bounded uniformly for ||U||<=U_*. The segment integral formula gives a
finite constant C_poly with

    sup_theta |D_poly(qhat,Lhat;U(theta))
                    -D_poly(q,L;U(theta))|
      <=C_poly max(|Lhat-L|,
                    max_(H used in (13)) |qhat_H-q_H|). (14)

Clipping cannot increase coordinate error against a target inside the
thresholds. Combining (12)--(14) establishes arbitrary-accuracy whole-circle
readout for fixed n,P,T: select activation degrees, then select a large
enough scalar cutoff. If only the original unsaturated closure is used, its
proved scalar convergence and therefore this inference are local in time;
arbitrary T still requires the stated scalar stability assumption.

The parent dense-to-population approximation remains a third term. A
uniform weight estimate together with bounds (8) transfers uniformly over
the circle by the same layerwise subtraction. If only a finite-list output
estimate is available, that estimate alone does not supply the required
whole-circle parent comparison. At a matched time the intended bound is

    circle error <= population-to-dense circle error
                   + activation-polynomial error (12)
                   + scalar-coordinate readout error (14).         (15)

The readout can be synthesized after training if its required diagrams were
already retained. A terminal state with cutoff K cannot retroactively provide
missing higher diagrams. For a prescribed tolerance, a safe construction
chooses the readout and required cutoff before the scalar evolution, while
allowing the requested angle to arrive afterwards. Query storage is removed;
finite representation and error planning remain.

## 5. Representative populations and what additional information they require

A representative physical population would provide an ordinary new-angle
forward pass, but it is a further inverse problem. Moment matching is not
yet a decoder theorem. The scalar ODE can leave the realizable moment set,
so an exactly matching neural population might not exist. Even when it
exists, (1)--(7) show that exact matching of a finite dictionary need not
identify the function. A regularizer or selection rule defines a particular
representative but does not by itself identify the original fitted function.

For a useful approximate representative, one sufficient certificate would
be: match all contractions used by (13) within a stated tolerance; impose
the same physical bounds (8); and control clock error. Equation (14), plus
the two physical polynomial errors from (12), then bounds the difference
between the representative and the target functions. This is a sufficient
condition, not an algorithm proving existence or efficient reconstruction.
It also cannot recover individual labelled neurons from invariant moments.

Separate marginal laws or within-layer Gram matrices are insufficient to
prescribe the necessary coupling with initialized matrices. For example,

    mean_j u_j (W20 v)_j

depends on the joint placement of u and v relative to that same W20, not
just their separate marginal moments. Both forward and reverse actions use
the identical realized operator. Gaussian initialization does not permit
independently resampling this coupling after training. A representative
population needs matched joint operator-decorated contractions, or a new
proved approximation of their effect. Storing actual initialized matrices,
actual neuron factors and outer fields instead recovers the already-known
population model and its corresponding storage cost.

Learning a decoder on externally generated pairs of scalar states and dense
networks is a possible new empirical method, but its parameters then come
from trained trajectories. It is not the present initial-data-only theorem.
Likewise, retaining the seed and replaying a population trajectory can answer
post-hoc angles but does not show that the terminal compressed state alone
contains a cheap inverse. Retaining just a scalar history does not solve this
automatically: one must specify the additional reconstruction dynamics and
prove that its input history is sufficient. Re-evolving an augmented scalar
system with a new query requires the new query contractions at initialization
and another evolution; it is a valid alternative when those initial data are
available, not an instantaneous terminal-state decoder.

## 6. Claim ledger and remaining bottleneck

| Claim | Status | Exact scope |
|---|---|---|
| All invariant diagrams recover original labelled weights | Falsified | Family allowing consistent neuron relabelling, without labelled side information |
| Every fixed K exactly determines every circle function | Falsified | Explicit deterministic stationary family (3)--(7), width may depend on K |
| No finite aggregate representation can approximate arbitrary angles | Falsified | Polynomial contraction decoder (9)--(14), with initial-data bounds and sufficiently rich retained dictionary |
| Saturated scalar evolution supports arbitrary-accuracy terminal circle readout | Exact under the cited scalar theorem | Fixed finite n,P,T, adequate cutoff chosen in advance, bounds (8), all required tree contractions retained |
| Practical compact decoder for the prescribed run | Open | Cutoff, symbolic growth, large polynomial coefficients, conditioning and numerical error are uncontrolled |
| Exact inverse on the one prescribed Gaussian trajectory | Open | Neither the permutation argument nor stationary-family collision settles it |
| Finite-horizon results identify fully fitted infinite-time networks | Unsupported | Endpoint and stopping-time estimates remain separate |

The highest-leverage distinction is therefore the requested deliverable:
an actual network inverse is an additional reconstruction problem; an
approximate evaluable circle function already has a theoretical route from
the existing aggregate ingredients. The latter needs no mesh of evolved
test inputs, but it can still require an impractically large and ill-conditioned
dictionary. The present analysis does not assert computational savings.

## 7. Frozen input provenance

| Input | SHA256 |
|---|---|
| POPULATION_TO_AGGREGATES.md | 99cf7504e058e076d68ecd4e61c1493e7ce1d2c11dcf94f544012d507b529ebb |
| POPULATION_SCALAR_CONSTRUCTION_CHECK.md | 8a2e44ad6d50995ef626a65402babed19b761f9685d9ef91fb63de7633944383 |
| SCALAR_COMPRESSION_BOUND_ASSESSMENT.md | e80540f9052049ee6e805037af99a57a83aa9acd0d98a3ff1f42d2ff39cd5309 |
| DEEP_CIRCLE_DERIVATION.md | 17ffa7efe44d588a47b8f566c5cbdc72199e012ae058bab232427e6685203bd9 |

Only SCALAR_DECODER_LIMITS.md was written by this scoped author. No Git
mutation or experiment was performed. This is an internal research artifact,
not an established-book addition or an independent promotion review.

## 8. Post-freeze audit of the selected Fourier route

2026-09-25. The supervisor subsequently selected the direct Fourier route
and authorized complete reads of SCALAR_FOURIER_READOUT.md and
SCALAR_CIRCLE_FUNCTION_READOUT.md. This section is a collaborative audit
after the preceding report was frozen; it is not part of its independent
first derivation. The versions audited were respectively
`c9191360c815dea1469ed2a7c060df24216273b988c55477d4c23d1b048a120a`
and `b09574355d4742cba2e6bc8331dfce8804a3e4b0a80db3836f43b5c0a63c6d32`.
No scientific input beyond these two additionally assigned reports was read.

### Integrated compiler and convergence check

The Fourier report supplies a valid finite-template extension of the original
compiler. The necessary distinctions are explicit: a shared angular variable
keeps disconnected neuron contractions inside one integral; only angle-free
components may be factored out; query responses use the actual population
weight velocities; and no query term enters the training residuals. These
rules preserve the intended target and require no evolving quadrature mesh.
Angular integration at initialization remains a separate cost and numerical
error. Exact initial integrals are an assumption of the displayed theorem.

The convergence argument is adequate under the inherited initial-data physical
bounds. A fixed tagged angular contraction has a product bound B^s because
the measure has mass one and all sine/cosine factors and Fourier weights are
bounded by one. A substitution changes only one decoration and uses one of
finitely many templates. The bounded total-size increment, bounded factors
per monomial and linear row growth therefore persist. Clipped scalar inputs
give an explicit envelope on every finite interval, while clipping fixes
the target and cannot increase its coordinate error. The existing dependency
iteration consequently applies to each fixed tagged contraction. The proof
uses subdivisions only for comparison and supplies no intermediate exact
target values to the solver.

Training autonomy alone does not guarantee exactly the same finite numerical
training law after augmentation. The original training dictionary, monomial
deletion decisions and clipping thresholds must be preserved. The root
synthesis explicitly records this requirement. A larger common bound may be
used in the proof without changing those existing thresholds. Purely passive
coordinates may receive their own valid thresholds.

The Fourier reconstruction, Parseval RMS identity, H1 tail bound and direct
integrated-energy formulas are valid with their stated normalizations. If
epsilon controls each stored real sine/cosine coordinate, the squared
coefficient error is at most (4J+1)epsilon^2, as the Fourier report states.
The root's (2J+1)epsilon^2 formula is valid when epsilon instead bounds the
complex coefficient error; these two meanings must not be interchanged.
Likewise its diagram convention counts query-angle incidence links, whereas
the Fourier report's convention omits that charge. Grade 5 for the Fourier
output belongs to the latter convention; use the actual grade s_* if the
former convention is retained.

### A common matrix for passive modes before clipping

The proposed shared-block organization is exact for the family generated
by the requested Fourier outputs. Restrict its angular coordinates to one
angle variable with one static Fourier-weight tag w. Use the same list of
integrand types and the same grade cutoff for every tag. Retain static
angular integrals, including

    Q_w[p]=integral p(cos(theta),sin(theta)) w(theta) dmu,

as zero-derivative coordinates. Keeping these coordinates matters when a
derivative term loses all its query decorations: its last angular factor
is still Q_w[p], rather than a mode-dependent inhomogeneous coefficient.

Every differentiated monomial then has exactly one angular factor with
the original tag w, times a finite product of training-only contractions.
No operation differentiates w or depends on its frequency. Collecting the
coefficient of each angular factor therefore gives

    dot Q_w = A_K(q_train,L) Q_w.                      (16)

Here A_K is a finite matrix whose entries are prescribed polynomial/rational
expressions in the training contractions, residuals, RMS and L. Residual
RMS is the same locally Lipschitz scalar function used by the original
compiler. The matrix is identical for w=1, cos(k theta), sin(k theta).
Static coordinates have zero rows. Exact initialization, which differs
between tags, carries their frequency dependence.

This conclusion uses the one-angle generated family, not an arbitrary
enlargement containing multiple coupled angle variables. The latter is
unnecessary here and can admit products of multiple angular blocks. It
also requires keeping the tag symbolic: rewriting products with w as
frequency shifts is another representation and conceals the common form.

With clipping, the correct passive law is

    dot Z_w=A_K(S_train(Z_train),L) S_angle(Z_w),       (17)

with the autonomous training law and its original thresholds unchanged.
Using grade-dependent passive thresholds shared across Fourier tags makes
S_angle identical in every block, since all these weights have sup norm at
most one. Equation (17) is generally nonlinear in Z_w. It must not be called
a common linear propagator or treated by unmodified superposition after
clipping. What is shared is its coefficient matrix and clipping rule.

For each fixed K, omitting passive clipping would still give a globally
defined linear equation conditional on the bounded-input training law:
its coefficients are bounded on each finite interval and successive integral
iteration is bounded by an exponential series. That observation gives no
envelope uniform in K and does not replace the saturation convergence proof.

The finite-template constants can be chosen independent of the number of
Fourier tags for this particular organization: every block has identical
rows, all tags have magnitude at most one, and a row never sums over tags.
The state count nevertheless grows with the number of modes. Converting a
uniform per-coordinate error into whole-function error also introduces the
mode-count factors above. No mode-count-independent runtime or total error
is inferred.

### Scope correction concerning post-training readouts

Statements that these integrated coordinates must be initialized before
evolution are correct for the selected direct integrated-observable solver.
They must not be strengthened to say that every function readout needs a
query-specific augmented state in advance. Sections 4--5 of this report
already give an alternative from sufficiently rich existing training-only
contractions. In particular, its polynomial in U becomes a finite
trigonometric polynomial when U=u_c cos(theta)+u_s sin(theta): substitute
cos(theta)=(exp(i theta)+exp(-i theta))/2 and
sin(theta)=(exp(i theta)-exp(-i theta))/(2i) in each finite monomial.
All resulting Fourier coefficients are then finite algebraic functions of
the existing terminal aggregates. No extra mode evolution is needed for
that alternative, provided all required contractions were retained.

Thus the selected Fourier solver directly evolves its requested coefficients;
the polynomial decoder can instead derive approximate coefficients after
training from a sufficiently rich dictionary. An arbitrary insufficient
terminal dictionary supports neither conclusion automatically. Neither
method reconstructs actual neural weights. No issue found in this audit
invalidates the direct Fourier existence theorem under its stated inherited
bounds; the important corrections concern block linearity after clipping,
normalization/grade bookkeeping, and the scope of the before-training claim.
