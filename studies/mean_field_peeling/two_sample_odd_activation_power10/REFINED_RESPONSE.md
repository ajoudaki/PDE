# Refined nonlinear source forcing in the original feature time

This note proves the nonlinear forcing estimate needed by the independent
coefficient supersolution argument. It does not use a new activation,
initialization, objective, training rule, or auxiliary quadratic regularizer.
No existing proof file is changed.

All constants denoted C are finite absolute constants. They may depend on
the fixed affine numerical constants exp(1404), exp(1410), and on the fixed
number of samples/layers, but on no angle, dimension, mesh, cap, or gain
parameter a in [1/2,1]. Each use below involves finitely many sums/products,
a Neumann series of ratio at most 1/2, or a scalar Gaussian moment estimate.
Thus taking successive maxima/products specifies a single such constant;
there is no parameter-dependent exponential hidden in C.

Let r=sqrt(v), lambda=a^3 r, and define the actual endpoint size

    M=(3/(sqrt(2) lambda))^(1/4)>1.

Then S<=C M^4, the affine raw propagator is at most C M^5, all four raw
primal sizes are at most C M, and M<=24^(1/4) delta^(-1/8). These statements
also hold with fixed absolute multiplicative slack at the enlarged affine
Gaussian initialization scales used by the coefficient supersolution.
The raw discrepancy is at most C e M^12. The learned-moment coefficient
discrepancies are at most C e M^15 h_j at strict times, as established in
the original quantitative theorem. The only input from the separate new
supersolution proof is the coefficient box specified in Section 2.

The result proved here is

    forward strict derivative density defects <= C e M^39,
    backward complete time-row derivative defects <= C e M^43.       (A)

Both compare actual nonlinear derivatives with the affine derivative
formula at the SAME deterministic coefficient arrays. Adding the learned
moments gives forcing norm q<=C e M^43. Current diagonals and all past
formal source slots are retained.

## 1. Sharper affine transfers from the existing Gaussian probe identity

Use original feature time and the source notation of
POLYNOMIAL_RESPONSE_LEMMA.md. Let |U|d=max_{j<k}|U_kj|/h_j for strict
kernels, and |Q|r=max_k sum_{j<=k}|Q_kj| for causal kernels. The sample
block norm is the maximum absolute row sum; fixed sample-basis changes
cost only an absolute constant.

Besides the four derivative-only arrays F,V,T,W, use

    R1=(I-a^2 H_P B2)^(-1),
    R2=(I-a^2 A2 B3)^(-1).

Distinguish the forward and backward top orientations by

    Rtop=(I-A3 K3)^(-1),
    Ltop=(I-K3 A3)^(-1),
    L2=(I-a^2 B3 A2)^(-1),
    Utop=Rtop A3,
    K3=a^2 E H_c.

The affine estimates needed below are

| Quantity | Bound |
|---|---|
| A2,F strict densities | C M^5 |
| A3,V strict densities | C M^7 |
| B3,T strict densities / row norms | C M^5 / C M^9 |
| B2,W strict densities / row norms | C M^7 / C M^11 |
| R1,R2,Rtop,L2,Ltop row norms | C M^11 |
| Utop strict density / row norm | C M^9 / C M^13 |

The first four rows follow from the answer-specific affine probe costs
already proved in TWO_SAMPLE_SOURCE_BASELINE.md, replacing its exponential
raw propagator by C M^5. For example bottom transpose injection and output
H1 each have cost O(1), while middle transpose injection and output H2
have cost O(M). Learned moments add densities at most O(M^2),O(M^4),
O(M^2),O(M^4), respectively.

Here are complete additional probe costs for the last two rows. Every
injection is an independent Gaussian root inserted at the indicated
coordinate instruction, and the program is recomputed thereafter. The
same root may be reused at all selected times to bound a full absolute
row, exactly as in Sections 5--7 of TWO_SAMPLE_SOURCE_BASELINE.md.

| Injection and output | Update cost | Output state Lipschitz cost | Direct term |
|---|---:|---:|---:|
| Add to Z1 query; output Z1 | C M^2 | C | I |
| Add to Z2 query; output Z2 | C M | C M | I |
| Add to Z3 query; output Z3 | C | C M^2 | I |
| Add to delta2 after its gate; output delta2 | C M | C M | I |
| Add to delta3 after its gate; output delta3 | C M^2 | C | I |
| Add to delta3 after its gate; output Z3 | C M^2 | C M^2 | 0 |

For the first row, a Z1 perturbation changes the A update by B*D times
the perturbation, the B update by D times its A-image, and the D update
by its BA-image. Each costs C M^2. It has no immediate effect on the
affine first-layer backward gate. For the fourth row, delta2 changes
the first update through A* and the A update through H1, each by C M.
For the last two rows, delta3 changes the first update through A*B*,
the A update through B*delta3 and H1, and the B update through H2;
all costs are at most C M^2. This verifies the new entries directly.

A pulse at time j changes a later state by at most C h_j times its
update cost times M^5. Multiplying by the output cost gives strict
response density C M^7 for the first five rows and C M^9 for the last.
Summing h_j<=C M^4 gives the asserted row bounds after adding the direct
identity. With coefficients frozen, the formal response operators in
these six rows are exactly R1,R2,Rtop,L2,Ltop,Utop. Indeed adding to a
gate gives delta=affine_backward(Z)+injection, while Z=source+A delta;
solving gives the displayed backward resolvent and its strict forward
transfer. Adding to a Z query gives the corresponding forward resolvent.

The finite-program independent-root identity applies without alteration:
these are additive independent root instructions in a finite affine
program, whose coordinates remain affine in all formal source roots
when its coefficients and covariances are frozen. The derivative in the
new root equals the inserted amplitude times the named transfer; its
Gaussian covariance with the output identifies that transfer. The
primal comparison bounds that covariance; continuity at zero amplitude
at fixed mesh gives the reference formal derivative. No covariance
inverse, derivative/width-limit interchange, or growing transcript is
used. The refined affine propagator also controls the tube traversed by
small probe amplitudes. Therefore all constants above hold at the
common enlarged affine initialization scale.

## 2. The coefficient box and persistence of the transfer bounds

Exact sample exchange equivariance implies that every deterministic
coefficient block is diagonal in the mean/contrast basis. The random
local gates need not be diagonal in that basis. The source estimates
below retain their full two-by-two action.

The independent supersolution argument provides the following outer box.
In the active scalar sector, the entrywise absolute values of A2,A3 are
bounded by the corresponding coefficients of an enlarged affine
reference. The entrywise absolute values of B2,B3 are bounded by those
reference coefficients plus nonnegative causal arrays J2,J3 satisfying

    |J2|r+|J3|r <= c0 M^(-12),                       (B)

where c0 is a sufficiently small absolute constant. In the inactive
sector, A2,A3 have bounded absolute strict densities C, and
|B2|r+|B3|r<=c0 M^(-12). This is the precise box required here; a statement
only about the four separate coefficient norms is not a substitute.

All forward strict-density bounds and causal row bounds in the table
in Section 1 hold uniformly on this box, with larger absolute constants.
The affine backward strict-density bounds are not asserted on this box:
its arbitrary backward row errors can include current diagonals or
concentrate on an arbitrarily small past step. Only their complete row
bounds are used below. To verify the required bounds, positivity allows replacing
A and B entrywise by their majorants. At the resulting active majorant,
let a subscript b denote the enlarged affine reference. The identities

    F=F_b+F_b J2 F,
    V=V_b+V_b J3 V,
    R2=R2_b+V_b J3 R2,
    L2=L2_b+L2_b J3 V

give the claims. Specifically the strict-density Neumann ratios are
at most S |F_b|d |J2|r<=C c0 M^(-3) and
S |V_b|d |J3|r<=C c0 M^(-1). The row ratio for R2 is the latter one.
The last identity bounds L2 by C M^11+C M^11 c0 M^(-12) C M^11,
which is at most C' M^11. The analogous identity
R1=R1_b+F_b J2 R1 gives its row bound. Rtop,Utop,Ltop depend on A3
alone and are dominated directly by their reference values.
All these identities are finite causal matrix identities.

In the inactive sector the reference backwards vanish. The row norms
of its affine forward integration kernels are O(S), so its Neumann
ratios are at most C c0 M^(-8). Its forward transfers have density O(1),
its forward resolvents have row norm O(1), and the top active readout
projection vanishes there. Thus that sector also fits every table bound.
This proves the table for the full sample block norms.

## 3. Source moments using the exact same-array resolvents

The primal estimates give the following Gaussian source standard
deviations, independent of all response bounds:

    Z1_initial: C,   zeta1: C M^2,
    xi2: C M,        zeta2: C M,       xi3: C M^2.    (C)

Their arbitrary within-group correlations and singularities are retained.
A two-coordinate Gaussian vector of these scales has Lp norm at most
the same bound times C sqrt(p), p>=2. Only this elementary consequence
of the scalar Gaussian tail is used.

Write d(Z,q)=g(Z) tau_R(q), so |d|<=|q|, and write h(Z)=arctan Z, so
|h|<=pi/2. The nonlinear source equations give exactly

    Z1=R1 Z1_initial+(F/a) zeta1
               +e(F/a^2)[d1+a B2 h1],
    Z2=R2 xi2+(V/a) zeta2
               +e(V/a^2)[d2+a B3 h2],
    Z3=Rtop xi3+e Utop[d3+a E H_c h3].              (D)

Here q1=zeta1+B2(a Z1+e h1),
q2=zeta2+B3(a Z2+e h2), and C=H_c(a Z3+e h3).
These identities apply at the actual deterministic coefficient arrays.
Let Zi,p denote the supremum over time of the Lp norm of Zi; this is a
supremum of deterministic norms, not a random supremum over sources.
Using the table in (D) gives

    Z1,p <= C M^11 sqrt(p)+C e M^20 Z1,p,
    Z2,p <= C M^12 sqrt(p)+C e M^20 Z2,p,
    Z3,p <= C M^13 sqrt(p)+C e M^17 Z3,p.

All constants are independent of p. For e<=c M^(-20), the terms on the
right containing Zi,p are absorbed, and consequently

    ||Z1_k||p <= C M^11 sqrt(p),
    ||Z2_k||p <= C M^12 sqrt(p),
    ||Z3_k||p <= C M^13 sqrt(p),

    ||q1_k||p <= C M^22 sqrt(p),
    ||q2_k||p <= C M^21 sqrt(p),
    ||C_k||p  <= C M^17 sqrt(p).                    (E)

For example the bottom forcing involving zeta1 costs |F|r M^2<=C M^11,
and its nonlinear self term costs |F|r |B2|r<=C M^20. The middle costs
are |R2|r M and |V|r M, hence M^12, while |V|r |B3|r is M^20. At the
top |Rtop|r M^2 is M^13 and |Utop|r |H_c|r is M^17. This checks every
power in (E). The same estimates bound features and deltas.

Expanding exp(Q^2/(C M^(2q))) in its power series and using the Lp
bounds proves a uniform subGaussian norm C M^q for each incoming
Q=|q1|,|q2|,|C|, with q=22,21,17 respectively. No operator is assumed
to preserve Lp tails merely because it is bounded in L2.

## 4. Exact derivative equations and their perturbative envelope

The three populations have the common formal structure

    Z=xi+K delta,      q=zeta+B H,
    H=phi(Z),          delta=D_cap(Z,q),

where (K,B) is (H_P,B2), (A2,B3), or (A3,E H_c). In the bottom equation
xi is its first root rather than a Gaussian forward-source family; in
the top equation zeta=0. Define

    R=(I-a^2 K B)^(-1),  U=R K,
    L=(I-a^2 B K)^(-1)=I+a^2 B U.

For the bottom/middle/top, |U|d is at most C M^u with u=5,7,9.
The middle/top |R|r,|L|r are at most C M^11; the bottom |R|r also is.
The respective |B|r exponents are b=11,9,4.

Freeze all deterministic coefficients and covariances. Let J be the
formal derivative of Z with respect to one source direction, and write
Ixi,Izeta for the direct derivatives of its named source instructions.
Put

    G=aI+DeltaG,     Vgate=aI+DeltaV,
    Lgate=e diag(g'(Z) tau_R(q)),
    P=Lgate+a DeltaV B+a B DeltaG+DeltaV B DeltaG.

Products here are causal operators: gates are block diagonal in time.
Uniformly in the cap,

    |DeltaG_k|,|DeltaV_k| <= C e,
    |Lgate_k| <= C e Q_k.

The exact derivative equations, after solving their affine parts, are

    J=Jaff+U[DeltaV Izeta+P J],
    Jaff=R Ixi+a U Izeta,                           (F)

    derivative(delta)-derivative_affine(delta)
           =L[DeltaV Izeta+P J].                   (G)

For (G), first subtract the affine output and use
Delta(delta)=DeltaV Izeta+P J+a^2 B(J-Jaff); then substitute (F).
This identity is why one must apply the backwards resolvent before
bounding the final output. Bounding B(J-Jaff) separately would lose
nine unnecessary powers of M in the middle layer.

For a single bottom or middle transpose source at time j, (F) has direct
forcing bounded by C M^u h_j, with J_k=0 for k<=j. Its perturbative
source injection U DeltaV Izeta obeys the same h_j bound. For a complete
middle or top forward-source row, the direct forcing has row norm at
most C M^11. Pad rows with zeros before comparing different times.
Strictness of U and (F) imply

    |J_k| <= C M^u h_j E_k   (one transpose source),
    |J_k,bullet|r <= C M^11 E_k (one full forward-source row),

    E_k=exp{C e M^u sum_{r<k}h_r(Q_r+M^b)}.         (H)

Indeed the term Lgate J contributes e Q_r times the current derivative;
the remaining terms in P have a deterministic bound C e M^b times the
maximum of prior derivative norms. Multiplying by |U_kr|<=C M^u h_r
and applying the elementary causal product majorant
prod_r(1+l_r)<=exp(sum_r l_r) proves (H). No supremum of Q over times
is introduced. The source-time factor h_j is retained in the initial
forcing and every subsequent update.

For the three populations, the stochastic exponents after time
integration have the powers

    u+4+q = 31,32,30,

and the deterministic exponents u+4+b are 20,20,17. Hence e<=c M^(-32)
controls every required fixed moment of E_k. To check this with arbitrary
source correlations, Jensen with weights h_r/S gives

    exp(t sum h_r Q_r)
      <= 1-s_k/S+sum_{r<k}(h_r/S)exp(t S Q_r).

The subGaussian bounds (E) and the scalar inequality
uQ<=Q^2/L^2+u^2 L^2/4 bound every fixed moment of the right side whenever
e M^(u+4+q) is bounded. In particular moments through order eight are
uniformly bounded after decreasing c. Holder then gives

    E[Q_r E_r] <= C M^q,

and retains both a source-time Q_j and a terminal Q_k whenever they
occur. Current multipliers are not absorbed into a past-time supremum
or omitted.

## 5. The four coefficient defects, including current diagonals

For a bottom or middle single transpose source, subtract the first
line of (F) and use (H). The expected preactivation derivative defect
is at most

    C e M^(2u+4+q) h_j.

The direct e U injection is smaller. Multiplication by the feature
gate G changes this by at most C e M^u h_j. The forward coefficient
derivative defects therefore have strict density at most

    C e M^36 for A2,       C e M^39 for A3.          (I)

For the middle/top backwards output, use (G) with Izeta=0 for the full
forward-source derivative row. The exact row estimate is

    E|L P J|r <= C e |L|r M^11(M^q+M^b).

For the Lgate term sum the deterministic time-row weights of L, use
E[Q_r E_r]<=C M^q, and |J_r,bullet|r<=C M^11 E_r. For the other three
terms in P, use |B|r<=C M^b and E E_r<=C. This proves

    C e M^43 for B2,       C e M^39 for B3.          (J)

This is an estimate of the complete expected formal derivative time
row, including j=k. It bounds the sum of absolute expected entries by
the expected absolute row, so it directly implies the required
coefficient estimate.

One can separately record the sharper current entries for use in the
coefficient supersolution. The exact source rules give

    (B3_kk)_ij=1_{i=j} E Lgate3_k,i,
    (B2_kk)_ij=1_{i=j} E Lgate2_k,i
       +(B3_kk)_ij E[Vgate2_k,i G2_k,j].

The raw primal bounds give ||C||2<=C M and ||q2||2<=C M^2, hence
|B3_kk|<=C e M and |B2_kk|<=C e M^2. These sharper diagonal estimates
are optional: both are already part of (J). The gates multiplying the
second diagonal expression are bounded uniformly in e<=1.

The strict learned-moment errors are <=C e M^15 h_j. Summing them in
a backwards time row costs S<=C M^4, giving C e M^19. Consequently the
full coefficient equation has forcing, in forward strict density and
backward arbitrary row norm,

    q <= C e M^43.                                 (K)

This proves (A) and the source forcing claim on the box (B), whenever
e<=c M^(-32). It is uniform in cap and sufficiently fine mesh and
uses the actual source equations with all four independent Gaussian
groups, all named slots, both orientations, and learned memories.

## 6. Combination with the independent coefficient supersolution

The independent supersolution argument is to supply the following
implication with absolute constants: forcing q<=c M^(-34) yields a
strictly interior instance of the box (B), starting from the affine
solution and continuing along amplitude homotopy. This note does not
replace that implication by a raw tangent estimate.

Given that implication, (K) shows that

    e<=c M^(-77)

already meets the forcing smallness after reducing c to absorb the
finite absolute constants. In particular the simpler target

    e<=c M^(-80)

has three spare powers. It simultaneously meets all moment/derivative
conditions above and all existing primal, endpoint, nonaffinity
conditions. Since M<=24^(1/4) delta^(-1/8), a sufficient angle-only
choice is e<=c' delta^10, with c'=c/24^20 after including the fixed
primal constant. These constants are absolute. The exact best exponent
is not asserted; 77/8 is only the formal sufficient exponent resulting
from the two displayed component bounds if the coefficient box closes
at its stated non-strict threshold.

Once the coefficient supersolution is supplied, (E) gives the cap/mesh
uniform incoming subGaussian estimates. The previously proved cap
removal, physical clock, canonical strong-flow uniqueness and restart,
full-width GF/raw-GD limits, all action/kernel/path/velocity conclusions,
initial motion and nonaffinity bridges therefore require no further
angle-dependent restriction.

## 7. Numerical prefactor ledger retaining the previous c_poly

Let H=C_B from equation (15) of the old quantitative PROOF.md:

    H=10^30(1+C0+Cz+Cg+exp(1410))^4.

In particular H>=10^30. Each reference density/row/probe prefactor in
Section 1, S/M^4, each Gaussian source standard-deviation prefactor,
and each learned-moment comparison prefactor are at most H. To verify
this for the additional probes, the injection/output products above
have degree at most four in the primal constant and multiply only one
exp(1410) propagator constant; the explicit primal size constants are
less than 10^3. They are therefore dominated by the displayed 10^30
and fourth power. The source and comparison prefactors already in the
old proof are included directly in H. The passage from delta-powers to
actual-M powers costs only absolute factors from
lambda=3/(sqrt(2)M^4) and a in [1/2,1], which are absorbed by the same
10^30 slack.

Use the outer radius

    |J2|r+|J3|r <= H^(-10) M^(-12).

The two Neumann ratios in Section 2 are then at most H^(-8)M^(-3)
and H^(-8)M^(-1), respectively. The inactive ratio is even smaller.
All outer source transfers in the Section 1 table, including row norms
|F|r<=H^2 M^9 and |V|r<=H^2 M^11, are consequently bounded by H^2
times their tabulated power. The bounds for L2 and the analogous
reverse resolvents use their exact identities, as in Section 2.

The following deliberately rounded ledger makes the remaining constant
selection explicit. Fixed sums, gains a^(-j) with j<=4, two-sample
norm conversions, and numerical constants <=10^6 are each absorbed
by at most one extra factor H.

| Quantity after the indicated step | Sufficient prefactor |
|---|---:|
| Primitive Gaussian Lp inputs | H^2 |
| Three value inequalities: leading and e times self terms | H^6 |
| Z1,Z2,Z3 after absorption | H^7 |
| Incoming Q1,Q2,C Lp bounds | H^10 |
| Incoming subGaussian scales | H^11 |
| Derivative envelope base in (H) | H^3 |
| Derivative exponential rate, before the time sum | H^6 |
| Expected Q_r times its derivative envelope | H^12 |
| Single-transpose preactivation defect | H^20 |
| Feature derivative defects | H^21 |
| Backward derivative time-row defects | H^19 |
| All derivative and learned-moment forcing combined | H^30 |

Here the value absorption needs e H^6 M^20<=1/2. The derivative
moment calculation is valid under

    e H^22 M^32 <= 1.                              (L)

Indeed rate H^6, duration prefactor H, and subGaussian prefactor H^11
produce H^18 before the fixed-moment constants. The spare H^4 ensures
that moments through order eight of each envelope are at most two.
Holder then bounds E[Q_r E_r] by H^12 M^q. For the largest forward
defect multiply U's H^2, the duration H, the envelope base H^3 and
this Q moment H^12; their product is H^18 and the remaining finite
sums fit H^20. For the largest backwards defect multiply L's H^2,
the envelope base H^3 and the Q moment H^12, giving H^17, which
fits H^19 after sums. This proves the last three ledger entries,
rather than inserting a parameter-dependent unknown constant there.
The condition (L), since H>=10^30 and M>1, also implies the value
absorption with ample slack.

Thus a numerical version of (K) is

    q <= H^30 e M^43.                              (M)

If the independent supersolution uses q<=H^(-16) M^(-34), the old
numerical coefficient is more than sufficient with the new angle
power. Specifically, from M<=24^(1/4)delta^(-1/8),

    e<=10^(-70)H^(-400)delta^10
      <=10^(-70)H^(-400)24^20 M^(-80)
      <=10^(-70)H^(-399)M^(-80),

because 24^20<H. This implies (L), and (M) gives

    q<=10^(-70)H^(-369)M^(-37)
       < H^(-16)M^(-34).

Therefore the previous explicit c_poly=min(1/4,c_*,10^(-70)H^(-400))
can be retained for the new e<=c_poly delta^10 conclusion once the
independent supersolution lemma with the displayed threshold is
included. This numerical ledger does not require improving the huge
angle-independent coefficient; it improves the angle power.
