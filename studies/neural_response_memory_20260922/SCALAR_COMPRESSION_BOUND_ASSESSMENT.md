# Scalar aggregate truncation: error transfer, structure, and the missing estimate

Theory assessment, 2026-09-25. Root owns this synthesis and its README entry.
The user asks whether the specified global-aggregate construction is principled
and whether the response-history error argument can establish controlled error
on every prescribed finite physical-time interval. This is a continuation of
the same study, explicitly referring to its scalar construction. No experiment
or solver implementation is part of this investigation.

## 1. Precise target and current conclusion

The supplied construction reduces the OLD activity-clock, finite-width,
fixed-P, three-hidden-layer tanh response-memory system. Its finite state m_P
includes actual neuron fields and the initialized matrices. The scalar target
is a fixed finite list of outputs, losses or other specified observables.
The second approximation keeps connected contraction diagrams of complexity
at most K and deletes a generator monomial whenever one of its connected
factors has complexity greater than K. It recomputes residuals and their RMS
from its own retained output coordinates. This exact rule is the object
assessed here; it is not replaced by a dense-network time-Taylor method.

The construction is principled as an exact derived hierarchy and an explicit
autonomous finite approximation with a named error source. Its zero-tail
rule does not yet have the mathematical protection of history orthogonal
projection. The finite-time STABILITY argument transfers; the source-error
bound does not follow from the parent theorem. There is nevertheless a new
positive result: at fixed finite n and P, all sufficiently inclusive cutoffs
exist on a common positive interval and converge there on every fixed output,
with an explicit geometric-times-polynomial bound in K. Section 7 proves it.
Neither a practically small cutoff nor convergence at every prescribed
finite T has been established for this neural deletion rule.

There is also a constructive repair. Evaluate that finite generator on
componentwise saturated aggregate values, with saturation thresholds obtained
from the parent initial-data bounds on a prescribed horizon T. This defines
a different, explicit autonomous scalar closure. It has global existence
for each cutoff and converges on every prescribed finite T as K increases.
Section 9 proves this without population refreshes, width-limit assumptions,
or a scalar realizability assumption. No practical efficiency or training
validation is claimed for either variant.

This distinction is substantive rather than terminological. Bounded smooth
underlying dynamics and an exactly derived aggregate hierarchy do not imply
convergence of zero-tail truncations. Section 5 gives a complete example.
Section 6 gives an exact simplification of the written diagram family, with
no new approximation. The proved fixed-n, fixed-P local convergence is
separate from all-finite-horizon and width-uniform accuracy. Section 8 gives
one precise additional lemma sufficient for the former. The scalarization
of the NEW clock is not yet specified
by the supplied compiler; that would require additional derivation.

## 2. What the construction preserves

The moments are genuine joint averages. For one sample with ||x/sqrt(d)||=1,
write B=B_(2,0), h=h_1 and delta=delta_1 (the backward signal without r).
The example

    q1=mean_i B_i h_i,
    q1_dot=rho mean_i h_i^2-2r mean_i B_i(1-h_i^2)delta_i

is the exact product rule under the existing fixed-P population law. The
compiler similarly differentiates contractions of initialized matrices and
their actual transposes. In finite width an initialized edge is C=nW0 and
each summed vertex has factor 1/n. Thus the two-vertex diagram is

    n^-2 sum_(i,j)u_i C_ij v_j=u^T W0 v/n.

Every assignment of neuron indices is included, including collisions.
Disconnected diagrams factor into the product of their connected components
because their summation indices are independent variables. This is an exact
algebraic factorization, not independence of random neuron fields or matrices.

These rules retain nonlinear gates, feature learning, moment dynamics, and
both orientations of the reused initialized matrices. After its permitted
initial contraction calculations, the finite scalar ODE uses only scalar
state and fixed scalar coefficients. It has a width-independent TYPE COUNT
at fixed K, P, data size and query count. The necessary K, initial evaluation
cost, numerical precision and error constants can nevertheless depend on
width; a small type count alone does not establish efficient compression.

The finite ODE is locally Lipschitz with the algebraic residual RMS and
history length L>=1. Zero residual remains stationary. But its moments need
not remain realizable by any neuron population: positivity of moment Grams,
activation constraints and the exact relations among contractions are not
automatically preserved by deleting terms. Consequently the parent physical
energy/compactness theorem cannot simply be applied to the scalar trajectory.

## 3. The oracle comparison transfers exactly

Fix n,P,K and a finite horizon T. The parent old tanh system exists through
T by the fixed-depth theorem. Let q_K(t) be its exact retained diagram values
together with L. Let G_K be the proposed finite scalar vector field, and let
eta_K be the sum of its deleted generator terms, evaluated on the parent
trajectory, with zero L component. Then exactly

    q_K_dot=G_K(q_K)+eta_K,
    qhat_K_dot=G_K(qhat_K),
    qhat_K(0)=q_K(0).                                      (1)

The remainder is explicit: if the exact equation for diagram H is
sum_nu a_Hnu(r,rho,L) product_(J in C(H,nu)) q_J, retain in eta_H precisely
those monomials with at least one |J|>K. Their component sizes are at most
K+Delta for the finite generator increment Delta. No parent trajectory or
unresolved term is supplied to the scalar solver.

Define the accumulated aggregate remainder

    B_K(t)=integral_0^t eta_K(s)ds,
    epsilon_K(T)=sup_(t<=T)||B_K(t)||_K.                    (2)

Here ||.||_K is a specified finite-dimensional norm. Subtracting (1) gives

    e_K(t):=qhat_K(t)-q_K(t)
      =-B_K(t)+integral_0^t[G_K(qhat_K(s))-G_K(q_K(s))]ds.  (3)

If G_K is Lambda_K-Lipschitz on the comparison region, iteration of the
integral inequality proves

    sup_(t<=T)||e_K(t)||_K<=epsilon_K(T) exp(Lambda_K T).   (4)

Alternatively, direct velocity forcing gives

    ||e_K(t)||_K<=integral_0^t exp(Lambda_K(t-s))
                                      ||eta_K(s)||_K ds.  (5)

Equation (4) can be useful when the remainder has cancellations. It does
not need a bound on eta_K_dot. Equations (4)--(5) are statements in aggregate
space; they do not invent a physical network realizing qhat_K.

The common-region requirement can be removed by a first-exit argument once
the forcing is small enough. Choose a compact region containing the entire
target q_K path with distance at least d_K>0 from its boundary, and lying
inside L>0. It can be bounded using finite-n parent field bounds and explicit
products defining each retained diagram. Apply (4) only until the scalar
path first exits. If epsilon_K(T) exp(Lambda_K T)<d_K, an exit contradicts
(4). For this fixed K the scalar state remains in a compact subset of its
locally Lipschitz domain, so it has a finite limiting state at a putative
maximal endpoint and extends. Thus the same condition proves existence
through T as well as the error estimate. A bare smallness assumption has
not been substituted for a derived neural-tail estimate.

Let S_K select the desired output coordinates, with norm at most c_K from
||.||_K to the chosen output norm. The sufficient convergence condition is

    c_K epsilon_K(T) exp(Lambda_K T) -> 0,                 (6)

together with the containment smallness just stated. For the maximum norm
on coordinates and the maximum norm on selected outputs, c_K=1. Weighted
norms must explicitly preserve output control; shrinking every weight to
make a remainder small is not a proof if c_K simultaneously diverges.

### A more focused comparison for a few outputs

When G_K is C1 on the comparison segments, define

    A_K(t)=integral_0^1 DG_K(q_K(t)+s e_K(t))ds.

Then e_K_dot=A_K e_K-eta_K. If U_K(t,s) is its fundamental propagator,

    S_K e_K(t)=-integral_0^t S_K U_K(t,s)eta_K(s)ds.        (7)

This is exact, not a linearization neglecting a nonlinear remainder: A_K
is the averaged Jacobian along the actual difference segment. Existence of
the finite propagator follows by iteration of its linear integral equation.
For the scalar RMS formula, C1 holds on segments with positive residual;
the Lipschitz formulation (3)--(5) also works at zero. Formula (7) itself
extends to zero using a bounded measurable secant matrix: telescope all
polynomial products and use

    ||u||-||v||=(u+v)^T(u-v)/(||u||+||v||),

with zero coefficient if both u and v vanish. This preserves the generator's
coordinate dependencies. The finite linear integral equation for U still
converges by its exponential-series bound.

Formula (7) shows why one need not approximate every large diagram accurately
to approximate a few outputs. One must instead control how the omitted
diagrams influence those outputs. Such a uniform propagator bound is still
an obligation; the formula itself is not an error certificate.

## 4. Why the history proof does not supply (6)

The parent history construction had two specific ingredients:

    orthogonal polynomial projection,
    D_f_dot=rho||f-fstar||^2.

History regularity controls projection tails, and the exact identity converts
them into an integrated physical-velocity defect. It also supplies the coarse
variation estimate needed to bound the new response clock. None of these
identities is an identity for deletion of connected graph monomials.

The graph-size cutoff is not an orthogonal spectral cutoff in a specified
Hilbert space. A high-degree moment is not inherently small: a population
concentrated at h=1 has mean h^k=1 for every k. Actual finite tanh values
are strictly below one, but the diagrams also contain unbounded outer/history
fields and initialized actions. There is no common demonstrated graph-tail
decay estimate from that elementary activation bound.

For finite n the parent theorem bounds every primitive field on [0,T].
If a primitive bound is B and an initialized-edge bound is C, it implies
only products of the form B^(number of decorations) C^(number of edges).
Those can grow with diagram size. Rescaling coordinates can turn individual
values into small numbers, but simultaneously changes generator coefficients
and stability constants. It does not bypass (6).

There are further distinctions:

* The graph-truncated state may cease to satisfy the neuron-level identities
  used by the parent energy theorem. A realizability-preserving mechanism
  or direct scalar stability estimate is therefore useful, but absent here.
* The number of equations grows with K. Local Lipschitz continuity at each K
  supplies no uniform Lambda_K and no uniform output propagator bound.
* Smooth trajectories in an adapted time coordinate do not by themselves
  make high population-degree or long initialized-action contractions small.
  P is a history resolution; K is a different approximation axis.
* The original clock's compiler uses tanh's exact finite response lift.
  The newer weighted clock contains a Gram state and a response-speed norm.
  Its scalar compiler and omitted terms must be derived before applying
  the new-clock parent error rate to a scalar solver.

There is a concrete limit to importing the neural energy argument. For
K>=3, the compiler retains the exact readout-energy identity

    (q_(c^2))_dot=-4 mean_a r_a f_a
                 =mean_a y_a^2-4 mean_a(f_a-y_a/2)^2.

It supplies an upper bound on q_(c^2), but an actual network also uses
q_(c^2)>=0 and f_a^2<=q_(c^2)q_(h3,a^2), with 0<=q_(h3,a^2)<=1. These
are realizability inequalities. The scalar deletion rule has not been shown
to preserve them. An upper bound on a scalar named q_(c^2) cannot replace
them if that scalar is allowed to become negative.

## 5. A rigorous warning example for zero-tail moment deletion

Consider a population of identical scalar states evolving by

    x_dot=-x^3, x(0)=1,
    x(t)=(1+2t)^(-1/2).                                  (8)

This is the gradient flow of the nonnegative potential x^4/4. The exact
trajectory is smooth, globally defined, bounded in [0,1] and has bounded
speed. Its odd moments m_j=E[x^(2j+1)] satisfy the exact connected one-vertex
hierarchy

    m_j_dot=-(2j+1)m_(j+1), m_j(0)=1.                     (9)

Keep m_0,...,m_N and delete the omitted m_(N+1) term, so m_N_dot=0.
Repeated integration gives

    m_0^N(t)=sum_(j=0)^N (-1)^j [binomial(2j,j)/2^j]t^j. (10)

Indeed the jth derivative at zero is
(-1)^j product_(k=0)^(j-1)(2k+1), and division by j! gives the coefficient.
For any fixed t>1/2 the ratio of successive absolute terms tends to 2t>1.
Thus m_0^N(t)-m_0^(N-1)(t) does not tend to zero: the truncations cannot
converge to the bounded exact observable. Already N=1 gives 1-t, eventually
negative despite positivity of the exact state.

This is a counterexample to an AUTOMATIC inference from a principled moment
hierarchy, bounded smooth dynamics and a finite zero-tail rule to arbitrary-
finite-horizon convergence. It is not a counterexample to the specified
neural compiler: its residual coefficients and factored products are different.
In this example the truncation happens to equal a time-Taylor polynomial;
that fact does not identify the study's neural aggregate closure with a
time-Taylor method or import the previously archived experiment.

The example also explains why agreement of successively many initial
derivatives is insufficient. A local approximation theorem may be valid
while convergence on a larger fixed real-time interval fails.

The independent obstruction route gives a stronger complementary example
in `SCALAR_TAIL_OBSTRUCTION.md`, section 2. It uses particles
x_i_dot=-rho x_i^2, output q1=mean x_i, residual r=q1+1, rho=|r|, and the
exact clock L_dot=rho, with x_i(0)=a in (0,1). Connected moments obey
q_k_dot=-k rho q_(k+1). Zero-tail truncation keeps the residual, clock and
disconnected products exactly. The target is bounded, and its omitted
source is bounded by N(1+a)a^(N+1), which tends to zero. Nonetheless,
arbitrarily high odd cutoffs blow up before one fixed finite horizon.
The report solves this example explicitly and proves the claim. It shows
why even a small boundary source needs a compatible stability estimate.
This is also a generic proof-route counterexample, not an admissible neural
instance or an impossibility result for scalar compression.

## 6. An exact simplification: outputs generate forests, not arbitrary graphs

The full written dictionary includes arbitrary connected graphs. Its static
two-parallel-edge coordinate equals ||W0||_F^2 and diverges with width under
the canonical Gaussian initialization. That is an obstruction to a finite
coordinatewise population limit of the ENTIRE dictionary. It is not yet an
obstruction to scalar output approximation. Here the latter distinction can
be sharpened for the stated compiler.

**Forest preservation.** Start from ordinary output/mean/Gram observables
in the supplied construction, expanding backward fields as prescribed.
Every connected diagram generated by repeated differentiation is a tree.
Consequently, at any fixed K containing the requested output diagrams, the
zero-tail ODE for forest coordinates is an autonomous subsystem of the full
all-graph zero-tail ODE. Discarding all cyclic diagrams preserves its output
trajectory on the common existence interval, with the same initialization.

Proof: represent each neuron-valued expression by rooted diagrams, with one
unsummed root of the correct layer. A primitive field is a decorated single
root. A product of rooted trees uses fresh copies and identifies ONLY their
roots, yielding a rooted tree. An initialized action adds a new root and
one edge to the old root, again yielding a tree. Taking a normalized average
sums the root and gives an unrooted tree. Scalar factors are detached
components, and products of them are forests. Finite sums are treated term
by term. These operations generate every primitive RHS in the old tanh
response lift: learned actions are local factors times normalized pairings,
and the matrix-velocity/forward/backward recursions use the same operations.

For a scalar diagram, differentiating a decoration substitutes one of those
rooted expressions at its vertex. Its fresh attached trees meet the original
graph only at that one vertex; detached components remain separate. This
cannot create a cycle when the original graph is a tree. Starting output
diagrams have one vertex; the mean/Gram diagrams of expanded backward fields
also have this rooted-tree form. Induction proves the assertion. Index
collisions in the finite sums do not identify symbolic graph vertices and
therefore do not invalidate this argument.

Every retained forest equation in the full cutoff therefore contains only
forest factors. Its zero-tail deletion test uses the same component sizes
whether or not cyclic variables are stored. The two finite RHSs and initial
values on the forest subsystem are identical; local uniqueness proves equal
forest trajectories. This proves the pruning claim without a new model.

The lemma applies to the specified operations and output/mean/Gram starting
observables. It does not remove a cyclic observable deliberately requested as
an output, nor prove finite population limits or error bounds for all trees.
Tree branching, decorations and repeated operator use can still create
large moments and strong feedback. The improvement is an exact reduction
of unnecessary state, not a convergence theorem.

## 7. A proved local convergence theorem for the actual scalar construction

The independent positive and error-transfer routes both obtain a nonvacuous
result for the specified compiler. Here is a self-contained version using
the simpler direct dependency iteration. Fix finite n,P,M,d, the realized
initialization and a finite query list. Let s(H) denote the graph size.
Ordinary training and query outputs q_(c h3,a) have s=3.

### Generator bounds from the finite substitution grammar

One differentiated decoration is replaced by one of a finite list of rooted
templates. Hence there are constants independent of K and H such that:

* the sum of the connected factor sizes in a generator monomial is at most
  s(H)+delta_tot;
* each monomial has at most a fixed number N_* of connected factors;
* the number, and absolute coefficient sum after bounding the fixed
  coefficients, of terms in a size-s(H) equation is O(s(H)).

The last assertion is the product rule: choose one of at most s(H)
decorations, then one of its finitely many replacement terms. The original
connected graph stays connected under replacement at a single root; only
the fixed number of detached template factors can be additional components.
Factoring disconnected diagrams preserves total size, and removing an empty
isolated vertex only reduces it. These facts hold before collecting equal
graphs, so cancellation or type multiplicities are not being assumed.

Choose an integer delta>=1 that bounds the total-size increment and every
connected-component increment. Residual and rho coefficients depend only
on size-3 outputs and labels. With L>=1, every coefficient denominator is
bounded. Thus there are computable A>0 and integer D>=1, independent of K,
for which

    |(G_K)_H(q,L)|<=A s(H) b^(s(H)+D)
    if |q_J|<=b^s(J), b>=1, L>=1.                       (12)

Indeed rho<=b^3+Y and |r_a|<=b^3+max|y_a|; absorb the finite degrees of
these coefficient factors into D. Y is the label RMS. Deleting terms
cannot worsen the absolute bound. The constants depend on the finite
species/template list, including P and the data/query counts.

### A common interval of scalar existence

Fix a parent horizon T. Its finite-n bounds and fixed initialized entries
give B>=1 with |q_H(t)|<=B^s(H) for every genuine graph on [0,T]: bound
every summand by the corresponding product, and cancel the n^|V| summands
against the vertex normalization. This estimate may depend strongly on n.

Set b(0)=2B and b_dot=2A b^(D+1). Explicitly,

    b(t)=2B[1-2AD(2B)^D t]^(-1/D).

Let

    t0=[1-2^(-D)]/[2AD(2B)^D],    R=4B.

Then b<=R through t0. Every finite scalar cutoff K>=3 stays strictly inside
|qhat_H|<b^s(H): at a first contact, (12) bounds the outward speed by
A s(H)b^(s(H)+D), while the barrier has twice that derivative. All initial
inequalities are strict. Also

    1<=Lhat(t)<=L_*:=1+t0(R^3+Y).

For each finite K these bounds give a compact subset of L>0, so ordinary
local existence extends through min(T,t0). Thus the interval is independent
of K even though finite-dimensional Lipschitz constants need not be.

### High-complexity errors take many derivatives to reach an output

On the joint box |q_H|,|qtilde_H|<=R^s(H), 1<=L,Ltilde<=L_*, put

    E_m(t)=max( |Lhat-L|/L_*,
                 max_(s(H)<=m)|qhat_H-q_H|/R^s(H) ),    m>=3.

For all retained levels E_m<=2. Telescoping a generator monomial bounds
its difference by its fixed number of factors times R^(sum s(J)) times
E_(m+delta). Dividing by R^s(H) costs at most R^delta_tot. Differences
of residuals, rho and inverse powers of L obey the same estimate, since
rho is Lipschitz and L>=1. The O(m) row coefficient bound therefore gives
one C independent of m,K with

    max_(s(H)<=m)|G_H(qhat,Lhat)-G_H(q,L)|/R^s(H)
       <=C m E_(m+delta).

Increase C to include the clock equation. Every row of size m<=K-delta
has no deleted term. Since the initial values agree,

    E_m(t)<=C m integral_0^t E_(m+delta)(s)ds,
                                      m+delta<=K.       (13)

Iterate r=floor((K-m)/delta) times and use E_(m+r delta)<=2:

    E_m(t)<=2 (Ct)^r/r! product_(j=0)^(r-1)(m+j delta)
           <=2 binomial(r+a-1,r)(C delta t)^r,
           a=ceil(m/delta).                            (14)

The factorial is the volume of the ordered integration simplex. For each
fixed m the binomial prefactor grows polynomially in r. Consequently, on

    t_loc=min(T,t0,1/(2C delta)),

the requested output error satisfies the explicit bound

    max_a sup_(t<=t_loc)|fhat_a^K(t)-f_a(t)|
       <=2R^3 binomial(r+a-1,r) 2^(-r),
       r=floor((K-3)/delta), a=ceil(3/delta).             (15)

An empty product is one. This estimate applies to every K>=3 and tends
to zero. It proves convergence of evolved outputs, not just equality of
initial derivatives. A fixed finite K suffices for any given tolerance on
this interval; no population refresh or runtime neuron storage is used.
The bound may be extremely conservative, the interval may be very short,
and no width-independent K or numerical efficiency is asserted.

## 8. A precise sufficient extension to every prescribed finite horizon

Suppose, in addition, that for the prescribed n,P,T a finite R_T>=1 exists,
independent of K, such that on every sufficiently large cutoff's maximal
existing interval through T,

    |qhat_H^K(t)|<=R_T^s(H) for every retained H.         (16)

Enlarge R_T to include the true graph envelope. The clock equation bounds
Lhat through T, so (16) also proves finite-dimensional continuation through
T. The telescoped difference estimate above now holds on all of [0,T]
with one C_T independent of K. In this section redefine E_m with R_T in
place of R and L_*,T=1+T(R_T^3+Y) in place of L_*. Thus E_m<=2 holds on
the entire horizon. These facts suffice for arbitrary-finite-
horizon convergence, without restarting or modifying the scalar algorithm.

For completeness, choose h>0 with C_T delta h<1. If every fixed-coordinate
error tends to zero at the left endpoint s, the same iteration, with
nonzero initial errors, gives for any fixed r and sufficiently large K

    sup_(s<=t<=s+h) E_m(t)
     <=sum_(j=0)^(r-1) [(C_T h)^j/j!
              product_(i=0)^(j-1)(m+i delta)] E_(m+j delta)(s)
       +2 binomial(r+a-1,r)(C_T delta h)^r.              (17)

First send K to infinity at fixed r; each term in the finite sum vanishes.
Then send r to infinity; the remaining term vanishes. Initialization starts
the induction, and finitely many proof intervals cover [0,T]. No exact
intermediate aggregate is supplied to the running solver. The same fixed-K
autonomous solution is compared throughout; the subdivision is only a proof.

Thus (16) is a concrete sufficient stability lemma. The parent physical
theorem proves an analogous envelope for true contractions, not for
independently evolved scalar coordinates. The local barrier of section 7
blows up in finite time and cannot be reset using true population bounds
without proving containment. This is the unresolved step. A weaker bound
only on output-reachable trees, or a direct propagated-defect estimate,
could replace (16); its necessity is not claimed. No explicit arbitrary-T
rate in K is asserted merely from the qualitative continuation proof.

## 9. A stabilized scalar variant with an unconditional finite-horizon theorem

The unresolved envelope in section 8 can be enforced by a simple change of
the approximation. This result concerns the following SATURATED variant,
not the original zero-tail equations. Fix n,P,initialization,data,queries
and T. Compute a finite B_T>=1 from the parent initial-data bounds such that

    |q_H(t)|<=B_T^s(H),   0<=t<=T,

for all true diagrams. As before, a maximum bound on primitive species and
on initialized entries nW0 suffices. The parent old-clock tanh theorem gives
these bounds for every P. This is permitted initial preprocessing; evaluating
the future population trajectory is not an input to the algorithm.

Choose R>=B_T and define scalar clipping functions

    S_H(z)=max(-R^s(H),min(z,R^s(H))).                  (18)

Retain exactly the same diagrams as in the zero-tail compiler and initialize
their exact contractions. Replace its RHS by

    z_H_dot=G_(K,H)(S(z),L_z),
    L_z_dot=rho(S(z_outputs)),   L_z(0)=1.              (19)

All scalar coefficient evaluations, including residuals, use the clipped
output coordinates. Declare the reported prediction to be S_f(z_f), so
the residual is computed from the reported prediction. Here s(f)=3 for the
ordinary outputs. Static graphs remain constant with zero derivative; they
are initially within their thresholds. Clock L_z is not clipped.

This is a finite autonomous ODE with a locally Lipschitz RHS on L_z>0.
Clipping is a specified deterministic operation, not a fitted model or an
oracle forcing. It uses no additional neuron state or matrix actions after
initialization. Its number of evolving scalar coordinates is unchanged.

### Existence and uniform envelopes

For L_z>=1, equation (12) bounds every RHS by

    |z_H_dot|<=A s(H)R^(s(H)+D),
    0<=L_z_dot<=R^3+Y.                                (20)

These are finite constants for every finite K, independent of z. Thus every
cutoff exists for all physical time. On the prescribed interval, writing
c=AT R^D and h=s(H)>=1, integration gives

    |z_H(t)|<=R^h(1+c h)<=[R(1+c)]^h,                 (21)
    1<=L_z(t)<=1+T(R^3+Y).

The last inequality in (21) is the binomial inequality (1+c)^h>=1+ch.
Thus R_T=R(1+AT R^D) is an explicit K-independent exponential envelope.
No moment-realizability assertion is used.

### Consistency and convergence

The true target lies inside every saturation threshold throughout [0,T],
so S_H(q_H(t))=q_H(t). Its exact retained equations are therefore

    q_K_dot=G_K(S(q_K),L)+eta_K,

with precisely the same zero-tail source eta_K as before. Saturation creates
zero additional source when evaluated on the target. Moreover,

    |S_H(z_H)-q_H|<=|z_H-q_H|.                         (22)

Apply the telescoping generator estimate to the clipped inputs S(z) and
the genuine target q. Both satisfy an exponential envelope, and (22)
controls their difference by the raw scalar error. Using the global
normalizations R_T and L_*,T from section 8, one obtains exactly the same
interior error recursion (13), with a constant C_T independent of K.
All levels obey E_m<=2 by (21). The proof-interval argument (17) now has
all its hypotheses established, so for every fixed finite output list,

    max_a sup_(t<=T)|S_f(z_f^K(t))-f_(P,a)(t)| -> 0
                                        as K -> infinity.          (23)

In fact the raw retained output coordinates converge too, and every fixed
diagram and the clock converge. Equation (22) transfers raw-coordinate
convergence to the reported clipped predictions. Fixed T is arbitrary;
the thresholds may depend on T, n and P. This is not an all-time-uniform
or width-uniform accuracy assertion.

### A constructive finite-cutoff certificate

The positive route sharpened the proof to an explicit bound. Write

    N=max(1,ceil(16 C_T delta T)),    a=ceil(3/delta),
    J=floor(K/(delta 2^N)).

Whenever J>=a, the reported output discrepancy obeys

    max_a sup_(t<=T)|S_f(z_f^K(t))-f_(P,a)(t)|
       <=2N R_T^3 4^(-J).                              (24)

For all K>=3 the elementary bound 2R_T^3 also holds. Thus (24) gives
an explicit sufficient cutoff for any tolerance epsilon>0:

    K>=delta 2^N max(a,ceil(log_4(2N R_T^3/epsilon))).  (25)

Here is the quantitative continuation argument. Divide [0,T] into N proof
intervals of length h=T/N and let lambda=C_T delta h<=1/16. Put
x_k=E_(delta k) for k>=a. If x_k<=epsilon at an interval's beginning for
a<=k<=J0, repeated substitution r=J0-k times yields, for
a<=k<=J1=floor(J0/2),

    sup x_k <=epsilon sum_(i=0)^(r-1)
                    binomial(k+i-1,i)lambda^i
               +2 binomial(J0-1,J0-k)lambda^(J0-k)
             <=epsilon(1-lambda)^(-k)
               +2*2^J0 lambda^(J0-k).

The geometric-series product gives the displayed infinite sum; the
binomial coefficient is at most its row sum. Since k<=J0/2, the last
term is at most 2*2^(-J0)<=2*4^(-J1), and the amplification is at most
(16/15)^J1. If epsilon=2(j-1)4^(-J0), this amplification is bounded by
2(j-1)4^(-J1), because J0>=2J1 and 16/15<4. The interval's bound is
therefore 2j4^(-J1).

Start with zero initial error and J0=floor(K/delta), then halve the
controlled grade cutoff on each of the N proof intervals. After j steps
the bound is 2j4^(-floor(K/(delta 2^j))). If the final grade reaches a,
all the intermediate ones do, and their bounds are at most the final one.
Since E_3<=E_(delta a), multiplying by R_T^3 proves (24). The actual
scalar cutoff stays fixed throughout; only the proof's controlled range
shrinks. For C_T=0 the error recursion gives zero error directly.

The constants and sufficient K are computed from initial bounds, T and
the finite generator templates. No observation of the exact trajectory is
required. The factor 2^N can make the bound prohibitively conservative;
the exponential decay in K at fixed n,P,T is not a useful complexity claim.

Clipping is not justified as an optimal statistical closure. Its proved role
is stability plus exact consistency on the reference family. It supplies
an affirmative existence theorem for finite scalar compression, while
leaving the practical accuracy, cutoff size, initialization cost, numerical
conditioning and the original unsaturated neural solver to further study.

## 10. Connecting a scalar estimate to dense outputs

Use the same physical-time interval for each comparison. Suppose a scalar
error estimate establishes, for fixed n,P,T,

    sup_(t<=T)||fhat_(P,K)(t)-f_P(t)|| <= delta_(P,K)(T).

The proved old-clock parent theorem and local Lipschitz output readout give

    sup_(t<=T)||fhat_(P,K)(t)-f_dense(t)||
       <= delta_(P,K)(T)+C_T/sqrt(P(P+1)).               (26)

For a separately derived scalarization of the new clock, the corresponding
parent term would be C_T/[P(P+1)]. The current compiler is not that solver.
A valid iterated approximation would choose P for the parent error, then K
for that fixed P. A common choice of K as P grows needs additional uniform
estimates and cannot be inferred from separate fixed-P statements.

For the saturated old-clock variant, section 9 now makes this iterated
approximation unconditional at fixed finite width and finite T: choose P
for the desired history error, then K for the scalar error on that same T.
This proves existence of a finite scalar approximation to the named dense
outputs at any prescribed tolerance. It proves neither a useful state count
nor a width-independent choice of the two cutoffs.

For one input with exact residual r and prediction error e,

    |(r+e)^2-r^2|<=2|r||e|+|e|^2.

Hence an output error bound epsilon and residual bound B imply per-input
loss error at most 2B epsilon+epsilon^2, and the same bound for mean loss
when these bounds are uniform across training samples. More generally RMS
prediction error epsilon and RMS residual B give the same mean-loss bound
by Cauchy--Schwarz. Other observables need their own readout/error estimate.

For a fixed query grid, include the query outputs in the scalar state from
initialization. A whole-input function additionally needs a spatial estimate;
for a Lipschitz target and grid covering radius h, add its Lipschitz constant
times h. Finite-time tracking does not by itself control differing loss-based
stopping times or fitted endpoints.

## 11. Evidence and scope

Root read the complete population-to-aggregate synthesis, scalar compiler,
finite-closure check, aggregate-equation report, and moment construction, and
the already checked parent depth/activation theorem. The earlier 198 algebra
comparisons support the first aggregate equations; no new numerical replay
or training validation is asserted here. Their recorded existence is not
evidence for zero-tail accuracy or cutoff convergence.

The scientific source hashes are:

* POPULATION_TO_AGGREGATES.md:
  99cf7504e058e076d68ecd4e61c1493e7ce1d2c11dcf94f544012d507b529ebb
* POPULATION_SCALAR_CONSTRUCTION_CHECK.md:
  8a2e44ad6d50995ef626a65402babed19b761f9685d9ef91fb63de7633944383
* POPULATION_FINITE_CLOSURE_CHECK.md:
  6b55326a806d8f7953703390793041f7ad1aeecc49375e911ff52b7480664f1a
* POPULATION_AGGREGATE_EQUATIONS_CHECK.md:
  799bf10a740c7ed627bd76430ffb9c5ac9ca45f7c95012bdee723a492ccac447
* DEEP_ACTIVATION_ERROR_THEOREM.md:
  57e6e16b9af6ea32dd3cbc266f1c5b9054ae63219ce8e191bffdb3b87f44d8dd

Fresh scoped routes independently assessed error transfer, positive convergence
mechanisms and truncation obstructions and froze their first reports before
cross-route exchange:

* `SCALAR_ERROR_TRANSFER.md`: accumulated-defect bootstrap, exact secant
  propagator, alternative local convergence proof, two-stage error, and
  post-freeze independent audit of the explicit saturation repair.
* `SCALAR_POSITIVE_ROUTE.md`: finite-template majorant, direct dependency
  iteration, conditional arbitrary-T continuation, and the explicit
  finite-horizon cutoff bound (24)--(25).
* `SCALAR_TAIL_OBSTRUCTION.md`: residual/clock-preserving generic blow-up
  example and the neural readout-energy limitation.

Their assignments specify permitted current-study inputs; no other study or
archived experiment is an input. Post-freeze cross-checks are collaborative
checks, not independent promotion reviews. Results and complete checks are
linked from the README when finished.
This is internal research, not promotion into the established book.
