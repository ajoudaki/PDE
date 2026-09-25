# Positive theory route for the specified scalar graph truncation

2026-09-25. Scoped theory report, frozen before receiving other routes' results.
Scientific inputs read in full: `POPULATION_TO_AGGREGATES.md`,
`POPULATION_SCALAR_CONSTRUCTION_CHECK.md`, `MOMENT_CONSTRUCTION.md`, and
`DEEP_ACTIVATION_ERROR_THEOREM.md`. No other scientific files, experiments,
external sources, implementation, or Git operations were used. The required
rigorous-math and conjecture skills, including the research-contract and
adversarial-audit references, were read. This is an internal derivation, not
an independent promotion review.

**Conclusion.** The specified connected-diagram zero-tail compiler admits a
positive fixed-width result stronger than agreement of finite initial jets:
on a computable, possibly very short interval, its finite autonomous
truncations exist uniformly in cutoff and converge geometrically up to a
polynomial factor for every fixed output. This follows from a bounded
increase of total diagram size, a linear-in-size generator bound, and a
finite dependency-distance argument. It uses neither temporal analyticity
nor small raw boundary moments.

The argument does not prove convergence on every prescribed finite horizon.
One exact sufficient missing lemma is a cutoff-independent exponential bound
on the *scalar truncation trajectories* on that horizon. Under this lemma,
local convergence can be propagated across finitely many proof intervals
without changing the running scalar ODE or refreshing its state from the
population. The known bounds for the actual fixed-P population trajectory
do not establish that lemma. All constants here can depend on width and the
realized initialization. No width-uniform accuracy or population limit is
proved.

## 1. Contract and the extra graded facts supplied by the compiler

Fix finite n, P, M, d, a finite passive query set, the three-hidden-layer tanh
model, and a finite realized initialization. The target is the old-clock
fixed-P response-memory system in the supplied construction, with its actual
initialized operators and adjoints. The surrogate is precisely equations
(5)--(6) of `POPULATION_SCALAR_CONSTRUCTION_CHECK.md`: retain connected graphs
of size at most K, initialize their genuine scalar contractions, and delete
a generator monomial if any connected factor has size greater than K. Its
clock is L'=rho, with rho computed from its own training outputs. There are
no population restarts, future trajectory coefficients, fitted forcings,
or extra neuron state.

Write s(H)=|V(H)|+|E(H)|+|D(H)|. Every output f_a=q_(c h3,a) has size 3.
For the exact connected hierarchy write

    q_H' = sum_nu a_(H,nu)(rho,L,r) product_(J in C(H,nu)) q_J.       (1)

The construction explicitly gives a finite component-size increment. The
same finite rooted substitutions also give the following three facts:

1. There is a fixed integer delta_tot such that

       sum_(J in C(H,nu)) s(J) <= s(H)+delta_tot.                    (2)

   Indeed substitution removes one decoration and adds one graph from a
   finite list. Factoring the resulting disjoint union preserves its total
   size; deleting an undecorated isolated vertex only reduces it. Factors
   kept in the coefficient a, such as residuals, are not included in (2).

2. Each monomial has at most N_* connected factors, for a constant N_*
   independent of H and K. The original connected graph stays connected
   after a decoration replacement, apart from a possible removable isolated
   root; a finite substitution introduces only finitely many additional
   components.

3. Before combining equal terms, there are at most A_* s(H) terms. The
   product rule selects one of at most s(H) decorations, and each selected
   species has a fixed finite expansion. Combining terms cannot increase
   the sum of their absolute coefficient bounds.

All these constants are found by scanning the finite generator templates.
They depend on P, M, d and the finite query alphabet, but not K. A valid
component increment delta>=1 can be chosen at least delta_tot and at least
the component increment in the source. There is no assertion that these
constants are small.

Because all coefficient denominators are powers of L, for L>=1 and b>=1
the bounds |q_output|<=b^3 imply

    rho <= b^3+Y,    |r_a| <= b^3+max_a |y_a|,

where Y is the target-label RMS. The finite polynomial dependence of a on
rho and r, together with (2)--(3), therefore yields computable constants
A>0 and an integer D>=1 such that, for every retained equation,

    |F_(K,H)(q,L)| <= A s(H) b^(s(H)+D)
    whenever |q_J|<=b^s(J) for all retained J and L>=1.              (3)

Deleting terms does not increase this absolute bound. For example, if the
maximum coefficient degree in rho and residuals is R, one may enlarge
D to delta_tot+3R, and then further to at least 1. Coefficient constants
depending on labels are absorbed into A. This estimate is about absolute
values, so it assumes no Gaussian factorization or sign cancellation.

## 2. What boundedness of the actual population trajectory does give

The old-clock all-P corollary of `DEEP_ACTIVATION_ERROR_THEOREM.md` applies
to tanh, whose activation and first derivative are bounded by one. At every
fixed n, P and T, it supplies a global target solution and finite bounds for
the physical weights and clock on [0,T], derived from initialization and
data. Its bounded moment representations also bound every raw neuron
species in the compiler.

For clarity, put A_T=1+Tq_T, where q_T bounds rho. The forward raw moments
obey |B_(ell,k,a,i)|<=A_T because |h|<=1 and the shifted Legendre
polynomials have magnitude at most one. The backward raw moments have zero
prefix and satisfy

    |A_(ell,k,a,i)| <= sqrt(M) (A_T-1) B_ell,

where B_ell bounds the Euclidean norm of delta_(ell,a). This uses
|r_a|/rho<=sqrt(M) whenever rho>0; at zero residual the source is stationary.
First-layer weights and readout coordinates are bounded by their Euclidean
bounds. Passive responses remain tanh of the same reconstructed network,
so their magnitudes are at most one as well.

Consequently one can choose B>=1, from these bounds and
max_(ell,i,j)|n W_(ell,0)(i,j)|, so that every genuine target diagram obeys

    sup_(0<=t<=T) |q_H(X_(n,P)(t))| <= B^s(H).                       (4)

To verify (4), bound each edge and decoration by B in the normalized sum
defining q_H. There are n^|V(H)| summands and a prefactor n^-|V(H)|,
so no additional counting factor remains. This is deliberately a crude
fixed-n estimate; the edge maximum can grow with n.

Equation (4) bounds all true graph moments, but they need not decay with
size. More importantly, (4) does not hold automatically for the independent
scalar truncation, which need not be realizable by any neuron state.

## 3. A uniform local existence bound for every cutoff

Fix B as above and let b solve the scalar majorant equation

    b'=2A b^(D+1),    b(0)=2B.

Its explicit solution is

    b(t)=2B [1-2AD(2B)^D t]^(-1/D).

Set

    t_0 = [1-2^(-D)]/[2AD(2B)^D],    R=4B.                         (5)

Then b(t)<=R on [0,t_0]. Every zero-tail truncation with K>=3 exists
uniquely throughout [0,t_0] and satisfies

    |q_H^K(t)| < b(t)^s(H),    L^K(t)>=1.                           (6)

Here and below an interval can be intersected with [0,T]. To prove (6),
all diagram coordinates initially lie strictly below their barriers because
|q_H(0)|<=B^s(H)<(2B)^s(H). At a first contact of one coordinate with its
barrier, (3) gives the upper right derivative of its absolute value at most
A s(H)b^(s(H)+D), whereas the barrier derivative is
2A s(H)b^(s(H)+D). This contradicts first contact. There are only finitely
many coordinates at each K, so this first-contact argument is ordinary
finite-dimensional calculus. The clock remains at least one because
(L^K)'=rho^K>=0, and

    L^K(t) <= 1+t_0(R^3+Y)=:L_*.

For each fixed K these bounds keep the whole state in a compact subset of
the locally Lipschitz domain L>0. A finite maximal endpoint would have a
finite limit, since the bounded field makes the path Lipschitz there; local
existence from that limit extends it. Thus existence persists through t_0.
This also explains why the finite-dimensional Lipschitz constants are not
being assumed uniform in K.

## 4. Dependency propagation proves local output convergence

The finite generator templates yield a second estimate on the box
|q_H|,|qtilde_H|<=R^s(H), 1<=L,Ltilde<=L_*:

    max_(s(H)<=m) |F_H(q,L)-F_H(qtilde,Ltilde)|/R^s(H)
       <= C m E_(m+delta),                                         (7)

for a computable C independent of m and K, where m>=3 and

    E_m = max( |L-Ltilde|/L_*,
               max_(s(H)<=m) |q_H-qtilde_H|/R^s(H) ).              (8)

The clock equation satisfies the same bound after increasing C. Here is a
direct verification. For one generator monomial, telescope the difference
of its at most N_* factors. Each telescoped term is bounded by
R^(sum_J s(J)) E_(m+delta). Division by R^s(H), followed by (2), costs at
most R^delta_tot. Coefficient differences obey the same bound: rho is
Lipschitz in the training-output vector, each residual is affine in an
output, and L^-p is Lipschitz on L>=1 with derivative bounded by p.
Their needed input differences are controlled by R^3 E_(m+delta) and
L_* E_(m+delta). The number and absolute coefficient bounds of all terms
are O(m). Finally,

    |rho(q)-rho(qtilde)| <= max_a |f_a-ftilde_a| <= R^3 E_m,

which controls the clock. Smoothness of rho at zero is unnecessary.

Compare the exact diagram values and clock with the cutoff-K trajectory.
They agree initially. Every row of size at most K-delta has no omitted
term. On the interval in section 3, (7) therefore gives

    E_m(t) <= C m integral_0^t E_(m+delta)(s) ds,
          3<=m, m+delta<=K.                                      (9)

For every retained level E_m<=2, by (4),(6) and the clock bound. Iterating
(9) r times, with r=floor((K-m)/delta), yields the explicit estimate

    E_m(t) <= 2 (Ct)^r/r! product_(j=0)^(r-1)(m+j delta)
           <= 2 binom(r+a-1,r) (C delta t)^r,
               a=ceil(m/delta).                                (10)

The factor t^r/r! is the volume of the ordered r-fold integration simplex.
For the second inequality use m+j delta<=delta(a+j). The binomial factor
grows polynomially in r for each fixed m. Thus for

    0<=t<=t_loc:=min(T,t_0,1/(2C delta)),                           (11)

every fixed coordinate converges uniformly as K tends to infinity. In
particular,

    max_a sup_(t<=t_loc) |f_a^K(t)-f_a(t)|
       <= 2R^3 binom(r+a-1,r) 2^-r,
       r=floor((K-3)/delta), a=ceil(3/delta).                      (12)

The same conclusion holds for every included passive output. For any
prescribed epsilon>0, (12) provides a finite sufficient K. That K is fixed
for the whole interval, and the surrogate remains one autonomous scalar
system. Its dimension at each fixed K is independent of n, but the
sufficient K, t_loc, and constants can depend on n through B.

This proves convergence of evolved solutions, not merely equality of a
finite number of time derivatives. It also shows why failure of the full
retained-state defect norm to shrink need not prevent low-output convergence:
the defect starts at a boundary far from a fixed low diagram.

## 5. An exact sufficient lemma for arbitrary finite T

The following additional property would upgrade the local theorem to every
prescribed finite horizon without any population refresh:

**Uniform exponential-envelope property.** For the prescribed n, P and T,
there is a finite R_T>=1 independent of K, such that on each cutoff's
maximal existing interval through T,

    |q_H^K(t)| <= R_T^s(H) for every retained H.                    (13)

It suffices to require this for all sufficiently large K. The analogous
bound for the actual trajectory is already supplied by (4); enlarge R_T
to include it. Property (13), together with L'=rho, proves continuation of
every such finite truncation through T by the compact-continuation argument
in section 3. It also gives a constant C_T in (7), independent of K, on the
entire interval.

Here is a complete argument that (13) suffices for convergence through T.
Choose a proof interval length h with C_T delta h<1. Suppose the errors
of every fixed diagram and the clock converge to zero at its left endpoint
s. Repeating the integral iteration with nonzero initial errors gives, for
any fixed r and sufficiently large K,

    sup_(s<=t<=s+h) E_m(t)
    <= sum_(j=0)^(r-1) [(C_T h)^j/j!
           product_(i=0)^(j-1)(m+i delta)] E_(m+j delta)(s)
       +2 binom(r+a-1,r)(C_T delta h)^r.                           (14)

An empty product is one. First send K to infinity at fixed r: every term
in the finite sum tends to zero by the induction hypothesis. Then send r
to infinity: the remaining geometric-polynomial term tends to zero.
The initial interval has zero initial errors, so the induction starts.
Finitely many intervals cover [0,T], proving uniform convergence of every
fixed output and the clock on the whole horizon.

The intermediate exact states in this proof are comparison objects only.
No value at an intermediate time is supplied to the scalar solver. The
cutoff is fixed at initialization and its autonomous evolution runs
uninterrupted. Thus proof continuation and population-based restarting are
different operations.

Property (13) is a sufficient stability lemma, not claimed necessary. A
weaker bound controlling only the generator-reachable coordinates, or a
direct low-output propagator estimate, could also work. But a bound only on
the actual population state leaves precisely the unproved step that (13)
fills. The majorant in section 3 gives (13) only on its short interval.

## 6. Why current information does not extend the theorem to arbitrary T

The scalar majorant b'=2A b^(D+1) has finite blowup time. The target's
global boundedness does not permit resetting b to a small value after that
time, because the scalar trajectory is not known to satisfy the target's
realizability or energy constraints. Conversely, the failure of this
majorant beyond t_0 does not prove that the scalar truncation diverges.

There is a simple obstruction to any argument using only graded locality
and boundedness of the true flow. Consider u'=-u^2, u(0)=1. Its true
solution u(t)=1/(1+t) remains bounded for all positive time. The moments
q_k=u^k satisfy q_k'=-k q_(k+1), with size increase one and row growth k.
Zero-tail truncation at K sets q_K'=0 and gives

    q_1^K(t)=sum_(j=0)^(K-1)(-t)^j.

This identity follows by solving successively downward from q_K(0)=1,
or by differentiating the finite polynomial and using the hierarchy.
For t>1 its terms do not approach zero, so these cutoffs do not converge;
at t=1 they alternate between zero and one. The example is not a
counterexample to the specified neural compiler. It proves that the two
structural inputs used in the local proof cannot by themselves establish
an arbitrary-horizon theorem.

Likewise, an analytic finite-n vector field gives only local complex-time
analyticity; even a real solution without real-time singularities can have
finite Taylor radius. No analyticity-to-global-truncation step is used here.

The one unconditional all-time degenerate case is zero initial residual:
the genuine system is stationary, every scalar generator term vanishes at
the consistently initialized zero-residual state, and the locally unique
zero-tail solution is the same constant state for every cutoff containing
the outputs. This does not address nontrivial training.

## 7. Width, alternative closures, and the remaining claim levels

For each K, the type list is independent of n. The majorant B includes
initialized C=nW0 entries and can depend strongly on n; therefore this
report does not provide a single K(epsilon,T) that works independently of
width. The supplied construction also exhibits a raw static diagram equal
to ||W0||_F^2, which diverges with Gaussian width. An infinite-population
theorem would require a suitable dictionary, normalization or reachable
subfamily and uniform bounds in addition to the finite-n work above.

Changing the closure to impose realizability, projection onto a bounded
moment region, a centered or orthogonal diagram basis, damping of a
boundary band, or a learned reconstruction could plausibly supply a better
stability mechanism. Each changes the specified zero-tail witness and
introduces a new consistency error. None is silently substituted here or
claimed to work. Reinitializing moments from a population trajectory would
violate the stipulated autonomous-compression contract.

The strongest proved statement in this route is consequently fixed-n,
fixed-P local convergence with an explicit error bound and a fixed finite
scalar autonomous state. The strongest arbitrary-T statement proved here
is conditional on (13). Proving or replacing that scalar-trajectory bound
is the decisive positive-route obligation for the present witness; the
finite-time population history-projection theorem does not discharge it.

## 8. Post-freeze collaborative synthesis check

At the supervisor's explicit request, after this route froze, I read
`SCALAR_COMPRESSION_BOUND_ASSESSMENT.md` and `SCALAR_TAIL_OBSTRUCTION.md`
completely. This is a collaborative internal check, not an independent
promotion review. No experiment or other scientific input was added.

The final checked synthesis has SHA256

    bb8358a8a91cb2624a3ad7999a20403750fb2348d39184fd7ac01e698d0cc3dc

The checked obstruction report has SHA256

    7d143fcb1cb7afb33e9cb5777a447353baa6d2a4bf5d077e68ddb8b081ceda22

**Verdict: PASS for the claims and boundaries stated in that synthesis
version.** I checked the accumulated-defect bootstrap, the exact secant
propagator at zero residual, the scalar readout-energy identity and its
realizability limitation, both generic obstruction examples, forest
preservation and its exact-subsystem qualification, the graded local theorem
and constants, arbitrary-T continuation under the exponential envelope,
and the transfer to dense outputs. The synthesis correctly leaves the
arbitrary-T neural zero-tail theorem open, and does not infer uniformity in
width, population convergence, all-time accuracy, or small practical state.

Two presentation corrections were requested against the previously read
version d199c9dc57476448a5834e34ca59d0d4be7fed7dc51c98aa4c984406749cd53d,
and both were verified in the checked version above: the elementary
history-pairing example now specifies the zeroth forward moment and its
normalized input, and section 8 explicitly defines the global error
normalization using R_T and L_*,T=1+T(R_T^3+Y). The latter is also the
normalization intended in section 5 of this route: replace R,L_* in (8)
by those horizon-wide bounds before using the remainder constant 2 in
(14). Neither correction changes the mathematical conclusion.

The obstruction report's residual-dependent example was checked directly:
its odd-cutoff activity polynomial stays positive, its inverse clock has
finite integral, the dominated integral gives the stated finite limiting
blow-up time, and its true boundary source decays exponentially. It is
correctly classified as a generic proof-route obstruction rather than a
realization of the neural model. The forest lemma was separately checked
against the finite-root grammar: only fresh nonroot indices are attached,
so arbitrary finite-width index collisions do not create symbolic cycles.

## 9. Post-freeze quantitative continuation under a uniform envelope

The supervisor subsequently requested an explicit finite-T cutoff bound
from the bounded graded-error recursion. The following lemma sharpens the
qualitative continuation in section 5. It does not establish the missing
envelope for the original zero-tail neural closure.

Assume throughout [0,T] that the normalized errors satisfy E_m<=2,
E_m(0)=0 and, at every interval starting time s,

    E_m(t)<=E_m(s)+C m integral_s^t E_(m+delta)(u)du,
                   m>=3, m+delta<=K.                             (15)

These are precisely the estimates already proved under a uniform
exponential envelope, using the global normalization specified in section
8 above. Let

    c=C delta,    N=max(1,ceil(16cT)),    h=T/N,
    a=ceil(3/delta),
    J_0=floor(K/delta),    J_j=floor(J_0/2^j), 0<=j<=N.

For C=0 the errors vanish identically, so suppose C>0. If J_N>=a, then

    sup_(t<=T) E_3(t) <= 2N 4^(-J_N),
    J_N=floor(K/(delta 2^N)).                                    (16)

In particular, when |output error|<=R_T^3 E_3, the explicit output bound is

    max_a sup_(t<=T)|f_a^K(t)-f_a(t)|
       <=2N R_T^3 4^(-floor(K/(delta 2^N))).                      (17)

Here N is independent of K; its dependence on the horizon and generator
bound can make this estimate very conservative.

Proof. Put x_k=E_(delta k), k>=a, so (15) has row coefficient c k.
Suppose at one interval's left endpoint that x_k<=epsilon for all
a<=k<=J. Let J'=floor(J/2). For a<=k<=J', iterate (15) r=J-k times,
using x_J<=2 for the remainder. With lambda=ch<=1/16, this gives

    sup_(s<=t<=s+h) x_k(t)
    <=epsilon sum_(l=0)^(r-1) binom(k+l-1,l) lambda^l
       +2 binom(J-1,J-k) lambda^(J-k)
    <=epsilon (1-lambda)^(-k)+2*2^J lambda^(J-k).                 (18)

The infinite-series identity in the final line is elementary: multiply k
copies of the geometric series for (1-lambda)^(-1); the coefficient of
lambda^l counts k-tuples of nonnegative integers summing to l, which is
binom(k+l-1,l). The binomial remainder is bounded by 2^J because every
binomial coefficient is at most the sum of its row.

Since k<=J/2 and lambda<=1/16, the remainder in (18) is at most
2*2^(-J), which is at most 2*4^(-J'). The amplification factor is at most
(16/15)^J'. If epsilon=2(j-1)4^(-J), then

    epsilon (16/15)^J' <=2(j-1)4^(-J'),

because J>=2J' and 16/15<=4. Thus throughout the jth proof interval

    x_k(t)<=2j4^(-J_j),    a<=k<=J_j.                             (19)

Initialization supplies epsilon=0 for the first interval. Induction proves
(19) for all N intervals. Since J_j>=J_N and j<=N, the bound in (16)
holds on all earlier intervals as well. Finally E_3<=E_(delta a)=x_a,
so (16) and (17) follow. No intermediate exact state is supplied to the
surrogate, and K is fixed throughout the full evolution.

For example, a sufficient integer cutoff for a prescribed output tolerance
epsilon>0 under these hypotheses is

    K >= delta 2^N max(a,ceil(log_4(2N R_T^3/epsilon))).          (20)

This is an explicit existence/error estimate for any family satisfying the
uniform envelope and graded recursion. Applying it to a modified closure
requires separately verifying those hypotheses; applying it to the original
zero-tail family still requires the missing envelope lemma.

## 10. Collaborative check of the stabilized variant and final synthesis

The supervisor subsequently added an explicitly different saturated scalar
variant and incorporated section 9's quantitative continuation argument.
I read the new construction, existence and consistency proofs, final
cutoff certificate, and changed leading and concluding claims, in addition
to the complete earlier synthesis checked in section 8. The current final
checked `SCALAR_COMPRESSION_BOUND_ASSESSMENT.md` has SHA256

    e80540f9052049ee6e805037af99a57a83aa9acd0d98a3ff1f42d2ff39cd5309

**Verdict: PASS for the full stated synthesis, including its unconditional
fixed-n, fixed-P, prescribed-finite-T convergence theorem for the declared
saturated variant and its explicit cutoff bound.** This remains a
collaborative internal check, not an independent promotion review.

The key new verification is that evaluating the finite generator at clipped
connected coordinates bounds each row by A s(H)R^(s(H)+D), independently
of the evolving raw coordinates. The clock remains at least one and grows
at most linearly. Hence every finite saturated system exists globally, and
on [0,T] its raw coordinates satisfy the explicit exponential envelope
R_T^s(H), with R_T=R(1+AT R^D). The genuine target lies inside the static
thresholds computed from initial-data bounds, so clipping creates exactly
zero additional target defect. Its contraction inequality relative to that
target preserves the graded error recursion, including the nonlinear
residual and clock feedback. No scalar realizability condition is used.

I rechecked the final halving proof and all floors in equations (24)--(25):
the working levels are E_(delta k), k>=ceil(3/delta); each proof interval
halves only the controlled grade range; the terminal grade condition keeps
all levels admissible; the estimates control each full interval, not only
its endpoint; and E_3<=E_(delta ceil(3/delta)) transfers the result to all
included training and query outputs. The fixed scalar cutoff is never
changed during evolution, and no intermediate population state is supplied.

The scope qualifications are correct. Thresholds, generator constants and
the sufficient K can depend on width, P, initialization, data and horizon.
The constructive theorem concerns the saturated variant; convergence on
every prescribed finite T for the original unsaturated neural zero-tail
family remains open. Neither practical efficiency, uniform-in-width state
size for a requested error, a population limit, nor all-time-uniform
accuracy follows. The two-stage dense-output conclusion is valid with the
specified order: choose P first using the parent old-clock theorem, then
choose the saturated scalar cutoff for that fixed P and the same T.
