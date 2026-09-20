# Constructive rate for the maintained H3 dictionary

Status: internally derived theoretical result, 2026-09-20. No experiment,
maintained-file change, finite-width rate, or promotion is claimed. This route
uses the maintained H3 dictionary and its actual numeric order, including the
bounded-word code prefix. It does not replace that order by polynomial degree
in a newly chosen source list.

The result below supplies an explicit, extremely large staircase from H3 order
to a vanishing error. Its thresholds are fixed by integer recursions, before
any target trajectory is known. Finite initialized Gaussian expectations occur
in proof witnesses, but neither their values nor a target projection tail are
needed to choose the thresholds. The same witnesses control all required
projection sources on feature time [0,6], including the whole input circle.

## 1. Model and exact transformed equations

Use the canonical initialized action A0, with its actual adjoint and operator
norm at most 2, and g=(g1,g2) standard Gaussian. The one training direction is
e1 and its label is +1. Let

    F(z)=z/2+sinh(2z)/4,       J(g,v)=F^{-1}(F(g)+v).

Since F'=cosh^2>=1, F is a strictly increasing onto C-infinity function and

    |J(g,v)-g|<=|v|,      partial_v J=sech^2 J<=1.

For a scalar field V on population 1 put z=J(g1,V), w=(z,g2),

    h=tanh z,  A=A0+K,  Z=Ah,  H=tanh Z,
    Delta=c(1-H^2),  q=A*Delta.

The feature-time equations are

    V_s=q,        K_s=Delta tensor h,        c_s=H,       (1)
    V(0)=0, K(0)=0, c(0)=0.

They reconstruct z_s=sech^2(z)q and hence the canonical one-input physical
GF after ds/dt=2(1-f), f=<c,H>. This is an exact variable change. It retains
both orientations of A0 and the complete learned increment.

Here and below the raw error is the sum of the L2 norm of V, HS norm of K,
and L2 norm of c. For 0<=s<=6 the exact bounds are

    ||c||infinity<=s,  ||K||HS<=s^2/2,
    ||V||2<=s^2+s^4/8<=198,  ||w||2<200.                 (2)

These follow by integrating c_s, then K_s, then
||V_s||2<=(2+s^2/2)s. No tail statement is used.

For completeness (1) has a unique strong solution on this interval. On the
set ||c||infinity<=6, ||K||HS<=36 the action norm is at most 38. For two states
in this set, with raw distance e, their training fields satisfy

    ||h-hbar||2<=e,
    ||H-Hbar||2<=39e,
    ||Delta-Deltabar||2<=469e,
    ||q-qbar||2<=17828e.

The last line is 38*469e+6e. The rank-velocity difference is at most
475e and the readout-velocity difference at most 39e. Thus the vector field
is Lipschitz with L=20000. Its speed along the exact Euler constructions is
at most M=300. Exact Euler paths preserve ||c||infinity<=s and
||K||HS<=s^2/2. Their interpolants have a vector-field defect at most LMh
for maximal step h. Subtracting two interpolants and integrating
e'<=Le+LM(h+h') proves they are Cauchy, uniformly on [0,6]. Completeness
gives a limit; the closed readout bound passes through an almost-sure
subsequence. Lipschitz continuity passes the integral equation and gives
strong C1 regularity and uniqueness. Integrating its three equations gives
(2). This proof does not invoke local Lipschitz continuity of the original
untransformed row equation on an arbitrary L2 ball.

## 2. A bounded-word compiler for the nonlinear inverse gate

We give numerical constants to make effectiveness unambiguous; none are
optimized. Suppose ||V||2<=1500. For any |u1|,|u2|<=1 define

    Psi_u(g1,g2,V)=tanh(u1 J(g1,V)+u2 g2).

The training gate is u=e1. Let 0<lambda<=1 be a reciprocal power of 2 and set

    R=2^16/lambda,
    n=(2^8 R 2^(4R)/lambda)^2,
    P=100(n+1)^4.                                         (3)

There is a bounded initialized-word expression p_u(g1,g2,V), of at most P
additional grammar nodes, such that

    |p_u|<=1+lambda/16<2,
    ||p_u-Psi_u||2<=lambda.                               (4)

All its scalar coefficients are rational. A uniform bound on numerator and
denominator magnitudes is 2^(3n+10) R/lambda^2. This assertion holds for every
joint law of (g1,g2,V) with the stated individual L2 bounds; independence of
V and the seeds is unnecessary.

Here is the full construction. On [-1,1] let

    r_R(x)=R artanh(clamp(x,-tanh(1),tanh(1))).

Apply the tensor Bernstein polynomial of coordinate degree n, on [-1,1]^3,
to the continuous function

    Psi_u(r_R(x1),r_R(x2),r_R(x3)).

Its samples are replaced by rationals of denominator 16/lambda, within
lambda/16 of each exact sample. Such rationals can be obtained by certified
evaluation of the elementary functions and monotone bisection for F^{-1};
the sample values depend only on u,R,n, not on a target state. Substitute
x=(tanh(g1/R),tanh(g2/R),tanh(V/R)) in the resulting polynomial.

On the seed/field box |g1|,|g2|,|V|<=R this is the intended function.
Outside the box, the L2 error from replacing the inputs by their clamped
values is at most

    2 sqrt(2+1500^2)/R < 3002/R < lambda/16.

Indeed the output difference is at most 2 and a union bound followed by
Markov's inequality controls the exceptional probability. On the box,
|partial_g J|<=cosh^2 R<=exp(2R), |partial_V J|<=1, and
Lip(r_R)<=R cosh^2(1)<4R. Therefore the extended function is Lipschitz for
the l1 metric with constant 4R exp(2R). In the Bernstein representation,
the coordinate fluctuations have expected absolute value at most 1/sqrt(n)
(the variance of 2 Bin(n,t)/n is at most 1/n). Its uniform approximation
error is at most

    12 R exp(2R)/sqrt(n) < lambda/16,

using exp(2R)<=2^(4R). Rationalizing the samples adds at most lambda/16,
because the Bernstein weights are nonnegative and sum to one. The same
property proves the global bound in (4).

To compile, form each (1+x_i)/2 and (1-x_i)/2, its powers, their products,
the integer binomial factors, the rational sample factor, and the finite sum.
All products have bounded operands. There are (n+1)^3 terms and at most
3n powers per term, so P safely bounds the number of elementary grammar
nodes. Products of binomial coefficients are at most 2^(3n). This proves
the stated rational-size bound. The inverse F^{-1} occurs only in fixed
scalar polynomial coefficients: it is not a new runtime gate or mark.

## 3. Rational initialized-word Euler witnesses

Fix an integer k>=1 and write a=2^(-k). Define, using integers only,

    lambda=2^(-(k+400000)),
    Jstep=6/lambda,       h=lambda,
    m=2^(k+20).                                           (5)

The time grid is s_j=jh, 0<=j<=Jstep. The passive direction grid is all
v=(p/m,q/m), -m<=p,q<=m. It need not lie on the circle: it is used only
to approximate bounded passive observations; every unit direction is within
Euclidean distance 2/m of some grid point.

Construct the following initialized finite words, with V0=c0=K0=0. At step j
set h_j=p_e1(g1,g2,V_j), using (3)-(4). Store the learned increment in the
proof as

    K_j=h sum_(i<j) Delta_i tensor h_i.

For every contraction use a rational rho of denominator 1/lambda within
lambda of its exact finite-word Gaussian expectation. Form

    Z_j=A0 h_j + h sum_(i<j) Delta_i rho^h_ij,
    H_j=tanh Z_j,        Delta_j=c_j(1-H_j^2),
    q_j=A0* Delta_j + h sum_(i<j) h_i rho^Delta_ij,
    V_(j+1)=V_j+h q_j,       c_(j+1)=c_j+h H_j,             (6)

where rho^h approximates <h_i,h_j> and rho^Delta approximates
<Delta_i,Delta_j>. Define h_j,H_j,Delta_j also at the last grid point,
without advancing again. The exact initialized Gaussian source rule computes
every expectation here from a finite earlier word union. These are values of
finite initialized programs, not coefficients obtained from the exact trained
trajectory. For a rational selection with guaranteed error, approximate the
expectation to lambda/4 and choose a nearest dyadic multiple; thus no undecidable
exact rounding comparison is required.

Every operation in (6) belongs to the maintained grammar: h_j, H_j, c_j,
Delta_j are bounded; V_j and q_j may be L2 words; actions take bounded
operands only. The rank symbols are just a proof notation for the displayed
finite sums and are not stored as an unrestricted action oracle.

The deterministic bounds needed to justify (4) hold inductively:

    ||c_j||infinity<=s_j<=6,
    ||K_j||HS<=s_j^2<=36,
    ||V_j||2<=1440<1500.                                  (7)

The first uses |H_j|<=1. The second uses |h_i|<=2 and
h sum_(i<j) 2s_i<=s_j^2. For the third, the exact action on Delta_j
has norm at most 38*6=228, and the contraction-rounding error in q_j is
at most 2*6*lambda<=12. Integrate this bound over length 6. No probability
tail of V_j is assumed.

The error in the forward contraction sum relative to (A0+K_j)h_j is
bounded pointwise by 36lambda. The gate compiler adds L2 error at most
lambda. Relative to the exact vector field (1) at the witness state,
the upper-activation error is thus at most 74lambda and the Delta error
at most 888lambda. The q error is at most
38*888lambda+12lambda. The rank-velocity error is at most
2*888lambda+6lambda, and the readout-velocity error at most 74lambda.
Their sum is less than 40000lambda.

Consequently the grid raw error E_j against the exact solution satisfies

    E_(j+1)<=(1+Lh)E_j+40000h lambda+(LM/2)h^2,
    max_j E_j<=6 exp(120000)(40000+3000000)lambda
             <=2^(-100) a.                                (8)

For the last inequality it suffices to use exp(120000)<2^240000 and
6(3040000)<2^25. The very large additive 400000 in (5) is deliberate.
The local exact Euler remainder follows by integrating the L-Lipschitz field
along a target path of speed at most M=300. This establishes a quantitative
comparison, not merely convergence of each fixed Taylor coefficient.

At every s_j and passive grid direction v, also compile
p_v(g1,g2,V_j) and its A0 action. Include A0*Delta_j. Before the bounded
saturation in the next section, the union of all these words can be bounded
by the following completely predetermined size and rational coefficient bounds:

    W=100(Jstep+1)^2(m+1)^2(P+1),
    Acoef=2^(3n+10) R/lambda^2.                            (9)

Here W counts a causal DAG, with literal shared expressions used once.
Training sums cost at most a constant times Jstep^2; the passive queries cost
at most (Jstep+1)(2m+1)^2(P+1). Formula (9) exceeds both, including constants,
seeds, actions and update nodes. The contraction magnitudes are bounded by
4 and 36; their dyadic numerators, their products with h, and the gate
coefficients all fit the Acoef numerator/denominator bound.

## 4. Quantitative bounded approximants for unbounded action outputs

It would be invalid to obtain an L2 saturation rate for A0h from its L2 norm
alone. The finite-word witnesses allow a different argument with an explicit
fourth-moment bound. This is the step needed in addition to a gate compiler.

Consider any causal initialized grammar program of at most W nodes, whose
rational coefficient magnitudes are at most Acoef. Put

    E_0=max(2,W,Acoef),
    E_(r+1)=4(W+1)(Acoef+1)(E_r+1)^2,   0<=r<W,
    E=E_W.                                                 (10)

Then every node has L4 norm at most E. Every bounded node has supremum at
most E, and all first frozen named-source derivatives of all nodes have
supremum at most E.

Proof: the Gaussian roots have L4 norm below 2 and root derivatives bounded
by 1. Rational affine operations, elementary sin/cos/tanh gates, and bounded
products preserve the induction with the displayed recurrence. At an action
node on bounded operand b, the exact reused-action rule is a centered Gaussian
source of variance E[b^2], plus at most W earlier opposite-orientation operands
times expected first named-source derivatives of b. At the preceding bound
E_r, its L4 norm is at most 2E_r+W E_r^2. Its derivative with respect to a
formal source name is at most 1+W E_r^2; coefficients and covariances are
frozen when taking this derivative. All input operands in those response
terms are bounded. This verifies the induction. Neither independent reverse
actions nor nonsingular source Grams are assumed; the source rule remains
valid at singular covariances. Correlation among the Gaussian names does not
affect the triangle inequalities or the univariate Gaussian fourth moment.

For any real x and Rb>0,

    |x-Rb tanh(x/Rb)|<=x^2/Rb.

For |x/Rb|<=1 integrate 1-tanh'(y)=tanh^2(y)<=y^2; for larger absolute
arguments use |x-Rb tanh(x/Rb)|<=|x|<=x^2/Rb. Therefore every action witness X
above has the bounded-word approximation

    T_Rb X=Rb tanh(X/Rb),
    ||X-T_Rb X||2<=E^2/Rb,
    Rb=2^(k+10) E^2.                                      (11)

The saturation error is at most a/1024. Rb is an integer, so the new word
uses only three permitted nodes and rational scalings. This is a finite-
program moment estimate; it assumes no quantitative tail of the target or
of an H3 trajectory.

## 5. A target-independent threshold in the actual H3 order

After saturation, at most 4W nodes are needed; all rational numerators and
denominators have magnitude at most

    Afinal=max(Acoef,Rb).

Set

    M_0=(4Afinal+4)^2,
    M_(r+1)=64(M_r+1)^2,        0<=r<4W,
    N_k=max(M_(4W),2^(k+10)).                              (12)

Equations (3),(5),(9)-(12) are an explicit integer recipe for N_k. They use
no moment values or exact trajectory values.

To verify the code bound, a signed rational with numerator and denominator
bounded by Afinal has rational-index code below M_0: its signed-numerator
index is at most 2Afinal and its denominator-minus-one at most Afinal, and
Cantor pairing is bounded by the square of their sum plus one. If prior word
codes and rational indices are at most M_r, every unary or binary instruction
has code at most 64(M_r+1)^2, directly from n=4+8k+j and the Cantor pairing
formula in C.4.7.9 / C.4.7.10.B. Induction gives (12). DAG sharing does not
change this argument: each node's tree code is formed from the earlier codes.

Every bounded output with code at most N is retained by the H3 code-prefix
rule, unless it is already a literally retained core feature. Dependencies
alone are not counted as retained features; the witnesses themselves have
bounded output codes below N_k. Each witness is ONE raw retained feature,
not an arbitrary expansion with an unbounded coefficient norm.

Let Q_l,N denote the maintained positive contraction with
eta_N=1/[1024(N+1)^2]. For a retained raw feature psi,

    ||(I-Q_l,N)psi||2<=sqrt(eta_N)/2=1/[64(N+1)].           (13)

Indeed use its coefficient vector with one entry 1 in the standard ridge
estimate. Thus ||(I-Q)v||2 is at most the L2 distance from v to a witness,
plus the right side of (13), without a Gram eigenvalue assumption.

For any s in [0,6], use the preceding time-grid point. The target raw movement
is at most 300lambda. For any unit u, use the closest passive square-grid
point: its lower feature error is at most 200*(2/m)=400/m<a/1024, by (2).
At grid points, (4),(8) give lower-feature error at most E_j+lambda;
the training Delta error is at most 469E_j+888lambda. Its time modulus is
at most 469*300lambda. The A0 and A0* images multiply these bounds by at
most 2. The saturation adds at most a/1024. The margins in (5),(8) therefore
give, for every N>=N_k, all four estimates

    sup_(s,u) ||(I-Q1,N)h(s,u)||2 <= a,
    sup_s     ||(I-Q2,N)Delta(s)||2 <= a,
    sup_(s,u) ||(I-Q2,N)A0 h(s,u)||2 <= a,
    sup_s     ||(I-Q1,N)A0*Delta(s)||2 <= a.                (14)

Here h(s,u)=tanh(w(s) dot u); Delta is the training upper backward field.
All target-dependent quantities have disappeared from the right sides and
from the order-selection recipe. This proves quantitative error production.

In particular, with B_N=Q2,N A0 Q1,N,

    sup_(s,u)||(B_N-A0)h(s,u)||2<=3a,
    sup_s||(B_N*-A0*)Delta(s)||2<=3a,
    sup_s||Q2,N K_s Q1,N-K_s||HS<=7a.                    (15)

The first two use contraction and ||A0||<=2. The last uses
K_s=Delta tensor h, ||h||2<=1, ||Delta||2<=6, and subtracts its two factors.
Consequently the feature-time three-source quantity rho_N(6) is at most 13a.
For the normalized statement define the final threshold

    mathcal_N_k=N_(k+4).                                  (15a)

Then every N>=mathcal_N_k satisfies rho_N(6)<=2^(-k), since 13/16<1.
This finite shift changes neither the construction nor its target independence.
For physical time the last bound is at most 14a while 0<=f<=1, since
K_t=2(1-f)K_s. Thus the three maintained physical source defects have sum
at most 20a on every physical interval whose feature clock stays below 6.

## 6. Direct closure and fixed-physical-time conclusion

This section makes explicit that the source estimate controls the maintained
autonomous closure, rather than only a finite-word approximation.

In feature time the maintained closure, lifted to the common carrier, has

    (V_N)_s=A_N*Delta_N,
    (K_N)_s=Q2,N(Delta_N tensor h_N)Q1,N,
    (c_N)_s=H_N,             A_N=B_N+K_N.

These are its original equations after the same exact row variable change;
no runtime gate or basis is changed. Its contraction bounds give
||c_N||infinity<=s, ||K_N||HS<=s^2/2, ||A_N||<=38 on [0,6].
Using (15) and the notation e_N for the transformed raw error, subtraction
gives

    ||H_N-H||2<=39e_N+3a,
    ||Delta_N-Delta||2<=469e_N+36a,
    ||A_N*Delta_N-A*Delta||2<=17828e_N+1371a.

The middle-velocity difference is at most 475e_N+43a and the readout-
velocity difference at most 39e_N+3a. Therefore

    e_N'<=20000(e_N+a),     e_N(0)=0,
    sup_(s<=6)e_N(s)<=120000 exp(120000)a.                 (16)

The finite closure is globally defined and its equations have the exact
gradient interpretation established in C.4.7.9 / C.4.7.10.B; alternatively
their fixed finite bounded-mark characteristic equations give existence.
The transformed equations need no projected-trajectory tails.

The whole-circle prediction subtraction, using (15), gives

    sup_(s<=6,u)|f_N(s,u)-f(s,u)|
       <=235 sup_s e_N(s)+18a
       <=Cfeat a,       Cfeat=30000000 exp(120000).        (17)

For a completely explicit physical-time statement, take T=3. Along either
feature flow, the training f starts at zero and is nondecreasing: differentiating
it in feature time gives the sum of the squared norms of its three gradient
blocks (the middle block has the two Q contractions). Thus the physical clock
s'=2(1-f(s)) stays nonnegative and s(t)<=2t<=6. It cannot cross its first
root f=1, by uniqueness of this scalar Lipschitz ODE. The same holds for s_N.

On [0,6], both exact and closure whole-circle predictions have feature-time
Lipschitz constant at most 71000. One direct bound is
||w_s||2<=228, ||K_s||HS<=6, ||c_s||2<=1, giving
|partial_s f(u)|<=1+6(6+38*228)=52021<71000.
The clock subtraction and Gronwall therefore give

    sup_(t<=3)|s_N(t)-s(t)|
       <=6 exp(426000) Cfeat a,

    sup_(t<=3,u)|f_N(t,u)-f(t,u)|
       <=Cphys a,
    Cphys=Cfeat[1+426000 exp(426000)].                     (18)

This is an explicit vanishing order-to-error relation on the fixed positive
physical interval [0,3]. It concerns the exact mathematical H3 closure;
population integration, initializer quadrature, arithmetic, time stepping,
and neural width remain separate limits. The small finite random readout is
not redefined: its maintained population limit is the zero initial c used
here. The argument compares the canonical population flows with the actual
Gaussian action, and makes no new finite-width identification claim.

The sequence N_k is increasing and unbounded. Define k(N) as the largest k>=1
with N>=N_k when this set is nonempty. Equations (17),(18) give the staircase
bound Cphys*2^(-k(N)); below N_1 the crude bound 12 suffices, and this may
also be used to cap the staircase. This is a mathematical rate, not a useful
computational cost estimate: the first threshold is already enormous.

## 7. Scope and checks

- Polynomial degree N by itself is not the reason this proof works. New
  action-word features in the numeric prefix are essential. The proof makes
  no claim that increasing only the fixed four/two-variable polynomial core
  is dense in all dynamically relevant observable variables.
- The Bernstein/Euler construction is a proof witness for projection sources.
  It does not replace the autonomous H3 equations by Euler prediction playback.
- All thresholds depend only on k and the fixed horizon 6. Rational expectation
  values alter the witnessing words within an already bounded grammar class;
  they do not alter N_k.
- The action-saturation step is supported by the proved finite-program L4
  estimate. An L2 bound alone would not justify it.
- No source-control assumption, unknown target tail, Gram lower bound, small
  hidden feature motion, independent reverse action, or truncation of learned
  ranks is used.
- The proof establishes a deliberately slow rate, not sharpness, monotone
  errors as N increases, practical order selection, or all-training-time
  same-physical-time accuracy. A separate clock argument can strengthen the
  last scope if its hypotheses and constants are proved.

Maintained inputs used: docs/NOTATION.md; docs/global_nonlinear.md
C.4.7.8, C.4.7.9 and C.4.7.10.A-B (grammar, exact Gaussian source rule,
bounded initialized action, ridge filters, closure equations and comparison
identities); docs/observable_p1.md for the distinction between p=1 core
features and higher action-word enrichments. The proof above supplies its
own elementary approximation estimates rather than invoking an external
approximation theorem without hypotheses.
