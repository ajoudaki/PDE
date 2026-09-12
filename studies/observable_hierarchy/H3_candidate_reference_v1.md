# Bounded C-H3 reference candidate for complete review

This candidate is a fixed-order approximation on physical [0,1/200]. It does
not assert an arbitrary-epsilon nonlinear-GF solver, effective nonorthogonal/
nonatomic family membership, or all admissible observation graphs. Review its
positive claims at this exact scope and assess the separate full-milestone
requirements in the neutral assignment.

The primary executable is H3_shorttime_solver.py with H3_shorttime_test.py.
The source-cap/comparison component is H3_stability_proof.md/H3_stability.py.
All necessary canonical dependency proofs are supplied in dependencies_v1.md.
H2_proposed_section_v3.md records the already established qualitative foundation;
no completed H2 audit is being reopened by numerical comparison.

## Model and numerical inputs

The evaluated law is exactly one half at (sqrt(2)e1,+1) and one half at
(sqrt(2)e2,-1). The requested observation times are 0,1/400,1/200, with restart
at 1/400. The finite-network interpretation retains the actual independent
random readout of variance 1/n^2; the population initialization c=0 is its
identified limit, not a replacement finite-network experiment.

## Exact target and finite candidate

Use H2's model, physical GF time, unhalved loss, initialization, separate
populations, and canonical actions. Let

    mu = sum_a p_a delta_(sqrt(2)u_a,y_a),
    p_a >= 0, sum_a p_a = 1, |u_a| = 1, |y_a| <= Y.

The target law must belong to H2's fixed admitted ball for its identification
with actual finite-network GF. None of the bounds below impose orthogonality,
minimum mass, distinct atoms, or invertibility of a Gram matrix. Existence of
the target and its energy identity are the established conclusions.

All fields in the next display are frozen initialized fields:

    h_a = tanh(g dot u_a),       l_a = phi'(g dot u_a),
    z_a = A0 h_a,               H_a = tanh(z_a),
    s_a = phi'(z_a),            D_ab = H_b s_a,
    P_ab = A0* D_ab,            C_ab = E2[H_a H_b].

The scalar state is `b in R^m, beta in R^(m x m)`, initially zero, with

    fF_a = sum_b C_ab b_b,
    rF_a = fF_a-y_a,
    b'_a = -2 p_a rF_a,
    beta'_ab = b'_a b_b.                                     (S1)

There is no time coordinate, past-state list, target coefficient, or training
oracle. This ODE is autonomous and globally well posed: the b equation is
linear, then beta has continuous forcing from b. Saving b and beta permits an
exact restart of this same candidate. The finite beta state is an ordinary
integrated dynamical variable; its dimension does not grow with elapsed time.

For analysis define

    cF = sum_b b_b H_b,
    dwB = sum_ab beta_ab l_a P_ab u_a,
    KB = sum_ab beta_ab D_ab tensor h_a.

The candidate's first hidden output at any u is

    H1B(u) = tanh(g dot u + dwB dot u).                       (S2)

Let `h_u=tanh(g dot u)`, `l_u=phi'(g dot u)`, `z_u=A0 h_u`.
Its upper output and prediction are

    z2B(u) = z_u + A0[l_u(dwB dot u)] + KB h_u,
    H2B(u) = tanh(z2B(u)),
    fB(u) = E2[cF H2B(u)].                                  (S3)

Operationally the middle term is the fixed finite sum

    sum_ab beta_ab (u_a dot u) V_uab,
    V_uab = A0[l_u l_a P_ab],

and `KB h_u=sum_ab beta_ab D_ab E1[h_a h_u]`. Thus no arbitrary-vector
action interface is needed after the finite initialized fields for a requested
input have been constructed. Their joint law is constructed from initialization,
not from a target path. A new query u changes the fixed observation law, not the
evolving state. First and initial/current upper coordinates are paired on their
same canonical populations.

Although cF alone is a frozen-feature readout approximation, (S2)–(S3) retain
both nonlinear hidden motions and the initialized reverse Gaussian sources.
The theorem below compares them directly to the nonlinear target. The scheme
does not capture all feedback into c, and does not claim otherwise.

## Finite Gaussian law and cost reduction

The initial vector z is centered Gaussian with covariance `E1[h_a h_b]`.
Define the deterministic numbers

    k_ab = E2[s_a s_b],       j_ab = E2[H_b phi''(z_a)].

The source rule, with repeated indices interpreted as the sum of both formal
derivative paths, gives exactly

    P_ab = zeta_ab + h_b k_ab + h_a j_ab,                    (S4)
    E[zeta_ab zeta_cd] = E2[D_ab D_cd].

The centered Gaussian zeta group is independent of g and of the forward source
group. Thus `P_ab` is a Gaussian of variance at most one plus a function of g
bounded by two: `|k_ab|<=1`, `|j_ab|<=1`, since `||phi''||infty<1`.
The derivative response in (S4) is essential; resampling an independent reverse
operator or retaining only that response gives the wrong law.

The following useful formula uses a completed initialized action on a bounded
gate times one L2 field:

    V_uab = xi_uab + D_ab E1[l_u l_a],
    E[xi_uab xi_vcd] = E1[l_u l_a P_ab l_v l_c P_cd],
    E[xi_uab z_v] = E1[l_u l_a P_ab h_v].                    (S5)

Here all the xi and z variables are in the same forward Gaussian group.
To justify (S5) without silently enlarging the finite-word theorem, replace
P by `T_R(P)=R tanh(P/R)`. This is an admitted bounded word. Its only reverse
source derivative is `l_u l_a phi'(P/R)` in the ab slot. The source formula
therefore gives its forward answer with response
`D_ab E1[l_u l_a phi'(P_ab/R)]`. As R tends to infinity the inputs converge
in L2 by dominated convergence, the response coefficient converges to
`E1[l_u l_a]`, and all finite covariance entries converge. The positive Gaussian
square-root coupling from III.F.5 gives convergence of the finite Gaussian laws.
The bounded canonical action identifies the L2 limit with V. This proves (S5)
as an exact finite-dimensional formula for that completed action; it is not a
temporal series or a claimed general extension to arbitrary unbounded programs.

For strict finite-alphabet operation at a fixed cutoff R, use these saturated
inputs in (S3), retaining (S2) unchanged. The extra upper error is at most

    4 Y^2 t^2 (15^(1/6)+2)^3 / (3 R^2).                     (S6)

Indeed `|x-R tanh(x/R)|<=|x|^3/(3R^2)`: for nonnegative v,
`tanh(v)>=v-v^3/3` follows by differentiating and using `|tanh v|<=|v|`.
Also `||P_ab||6<=15^(1/6)+2`, `||A0||<=2`, and
`sum_ab |beta_ab|<=2Y^2t^2`. At R=1000, (S6) is below 1.518e-9 for the
displayed horizon. This version needs no unbounded operand instruction.

The unsaturated exact formula (S5) is especially cheap. Conditional on g, P is
Gaussian with known mean and covariance. Its products in (S5) can be integrated
over zeta analytically, leaving only two-dimensional Gaussian g integrals.
The k, j, C, and zeta covariance integrals have dimension at most m. For m=2,
all initialization contractions are therefore at most two-dimensional.

For each fixed u, the linear combination of the forward sources in (S3) is a
single Gaussian conditional on the initial z vector and z_u. Hence evaluating
its prediction or paired upper RMS requires at most m+2 independent Gaussian
coordinates, and at most m+1 for u among the support directions. At m=2 this
is three dimensions for each training-direction observable and at most four
for an arbitrary passive direction. For the first hidden output, condition on
g and aggregate its linear zeta combination to one Gaussian: three coordinates
suffice. This counts source dimensions, not a quadrature complexity theorem.
Singular covariance is handled by the finite PSD square-root construction;
no small Gram eigenvalue is divided by.

In particular the two-atom state has six scalar coordinates, two for b and four
for beta. It is not a finite-width neural network. For general m the m^2 reverse
fields and their covariance array must be counted; this route does not supply
dimension-free data-law integration.

## Explicit nonlinear remainder inequalities

The proof uses integral identities and bounded scalar gates, never temporal
analyticity or convergence of a temporal Taylor expansion. Set `T=1/200` but
keep Y explicit. The elementary bounds `|phi|<=1`, `|phi'|<=1`, and
`Lip(phi')<=1` are valid for tanh.

The target energy identity gives `integral|r|dmu<=Y` and
`||c(t)||infty<=2Yt`. Integrating the middle and first-row equations then gives

    ||K(t)||HS <= 2Y^2t^2,
    ||w(t)-g||2 <= W(t) := 4Y^2t^2+2Y^4t^4,
    sup_u ||Z2(t,u)-z_u||2 <= Z(t) := 10Y^2t^2+4Y^4t^4.    (S7)

The last line uses `A0[H1-h_u]+K H1`, and the preceding row bound integrates
`2Y(2+2Y^2t^2)(2Yt)`. These calculations control the full row vector norm.

The frozen readout also dissipates its squared loss, because
`cF'=-2 sum_a p_a rF_a H_a`. Consequently

    sum_a p_a |rF_a| <= Y,
    ||b'||1 <= 2Y,  ||b||1 <= 2Yt,
    ||cF||infty <= 2Yt,  sum_ab |beta_ab| <= 2Y^2t^2.       (S8)

Let `Ec(t)=||c(t)-cF(t)||2` and `F(t)=sup_u|f(t,u)-fF(u)|`, where
`fF(u)=E2[cF tanh(z_u)]`. Subtracting the two readout equations gives

    Ec'(t) <= 2 Ec(t)+2Y(1+2t)Z(t),
    F(t) <= Ec(t)+2Yt Z(t).                                 (S9)

For the first inequality, write the readout derivative difference as changed
residual times initial H plus unchanged target residual times changed H. The
prediction residual difference costs Ec plus `2Yt Z`. Integrating this scalar
inequality yields, for `0<=t<=T`,

    a = 4Y^2+2Y^4 T^2,
    b0 = 10Y^2+4Y^4 T^2,
    c0 = (2Y/3)(1+2T)b0 exp(2T),
    W(t)<=a t^2,  Z(t)<=b0 t^2,  Ec(t)<=c0 t^3.             (S10)

For a direction u set `dF(u)=cF phi'(z_u)` and `qF(u)=A0*dF(u)`. The
Gaussian-plus-bounded-response argument in (S4) applies also to passive u.
For every t>0, `qF(u)/(2Yt)` has a representation as a Gaussian of variance
at most one plus an independent-root-dependent term bounded by two. Uniformly
in u and all b satisfying (S8), at R>2,

    tau_R := {2[(R+2) varphi(R-2)+5 Phi(-(R-2))]}^(1/2)

bounds its L2 tail outside absolute value R. Here varphi and Phi are the
standard Gaussian density and distribution. This follows from
`(|G|+2) 1_(|G|>R-2)` and integrating its square. The Gaussian and root shift
need not be independent for this domination; the initialized construction
does in fact supply their independence.

The exact and frozen upper backward fields satisfy

    ||d2-dF||2 <= Ec+2Yt Z,
    ||q-qF||2 <= 2Ec+4Yt Z+4Y^3t^3.                         (S11)

For the lower gate, cut off only the explicitly known qF:

    ||[phi'(w dot u)-l_u]qF||2
          <= 2Yt[R W(t)+tau_R].                             (S12)

This is the critical estimate. It multiplies the L2 row difference by a
bounded reference on the cutoff event, and uses a Gaussian tail otherwise.
It never estimates a product of two arbitrary L2 errors. No trained-tail or
unknown trajectory-dependent constant occurs.

Let `Ew=||w-g-dwB||2` and `EK=||K-KB||HS`. The derivatives of dwB and KB
are exactly the target first-row and middle equations with r, gates, hidden
fields, and c replaced by their frozen-readout counterparts. Subtract them,
first changing residual, then backward field, then the relevant hidden gate.
Using (S9)–(S12) gives

    Ew' <= (4Y+8Yt)Ec +(8Y^2t+16Y^2t^2)Z
                  +8Y^4t^3+4Y^2R tW+4Y^2t tau_R,
    EK' <= (2Y+4Yt)Ec +(4Y^2t+8Y^2t^2)Z+4Y^2tW.           (S13)

For example the row's three terms are bounded by `8Yt F`,
`2Y(2Ec+4YtZ+4Y^3t^3)`, and `4Y^2t(RW+tau_R)`. The middle subtraction
costs `4YtF+2Y(Ec+2YtZ)+4Y^2tW`; the rank norm is the product of its two
L2 norms. This checks every coefficient and each use of the actual adjoint.

Define

    Cw = (4Y+8YT)c0 +(8Y^2+16Y^2T)b0 +8Y^4+4Y^2R a,
    CK = (2Y+4YT)c0 +(4Y^2+8Y^2T)b0 +4Y^2a.

Integration of (S13), with zero initial errors, gives

    Ew(t) <= Cw t^4/4 +2Y^2 tau_R t^2,
    EK(t) <= CK t^4/4.                                      (S14)

The approximate row has an explicit L4 bound. From (S4),
`||qF(u)||4 <= 2Yt(3^(1/4)+2)`. Minkowski applied to its integrated row
velocity therefore gives

    ||dwB||_(L4;R2) <= d0 t^2,
    d0 = 2Y^2(3^(1/4)+2).                                  (S15)

The scalar first-order spatial expansion of tanh has pointwise remainder
at most `|increment|^2/2`, because `Lip(phi')<=1`. Apply it to the known
dwB, not to an unrestricted target L2 increment. Subtract first H1B from
the target H1, costing Ew, and then linearize H1B. Equations (S3),(S7) give

    sup_u ||Z2(t,u)-z2B(u)||2
       <= EZ(t):=2Ew(t)+d0^2 t^4+EK(t)+2Y^2 a t^4,
    sup_u ||H1(t,u)-H1B(u)||2 <= Ew(t),
    sup_u ||H2(t,u)-H2B(u)||2 <= EZ(t),
    sup_u |f(t,u)-fB(u)| <= c0 t^3+2Yt EZ(t).                (S16)

The `d0^2` term includes the norm-two initialized action and the one-half
spatial remainder. The last term in EZ bounds `K(H1-h_u)`. All outputs share
their exact initial fields, so the same errors apply to paired RMS motion:
take the L2 norm on the product of the data-input law and its own population,
then use the reverse triangle inequality. The two populations are never
paired to one another.

For Y=1,T=.005,R=10 the constants are

    a=4.00005, b0=10.0001, c0=6.80107246841131,
    tau_R=3.5703706611381e-7,
    Cw=276.279140772382, CK=70.1387703861909,
    Ew(T)<=4.31864675989903e-8,
    EK(T)<=1.09591828728423e-8,
    EZ(T)<=1.29823047719270e-7,
    Ec(T)<=8.50134058551414e-7,
    sup_u|f-fB|<=8.51432289028607e-7.

These values were evaluated with Python's elementary math functions. No claim
of outward-rounded machine certification is attached to their last digits;
the rounded-up headline values are mathematical targets for interval checking.
The general symbolic formulas specify all dependence on Y and T. Larger Y
can make the route quantitatively useless on the unchanged horizon.

## Sharpened analytical bounds

The preceding integral comparisons admit the following sharper constants. Put

    L=4/(3sqrt(3)), sigma=sqrt(.52), T=.005,
    kappa=sigma+(10+4T^2)T^2,
    a=4 kappa+2 kappa^2 T^2,
    z=2a+2 kappa,
    c=(2/3)(1+2T)z exp(2T).

The bound `Lip(phi')<=L` follows by maximizing `2h(1-h^2)` on [0,1].
Also `q=E tanh^2G <= E min(G^2,1)=1-2varphi(1)<.52`; integration by
parts gives the equality, and the last strict inequality is checked with
outward arithmetic. For every initial input, `||H2(0,u)||2<=sqrt(q)<=sigma`.
Using the preliminary Z bound (S7) once in the readout equation yields

    ||c(t)||2 <= 2 kappa t.

Thus integrating middle and row velocities again gives

    ||K||HS <= 2 kappa t^2,
    ||w-g||2 <= a t^2,
    sup_u ||Z2-z_u||2 <= z t^2,
    ||c-cF||2 <= c t^3.

The frozen readout obeys `||cF||2<=2 sigma t`. For its reverse query
normalized by 2t, the Gaussian standard deviation is at most sigma and the
bounded response magnitude is at most `S=1+L sigma`: the forward derivative
coefficient is at most one, and the other is bounded by
`L E|H_b|<=L sigma`. This remains true for correlated support directions.

At cutoff R=8, set d=(R-S)/sigma and

    tau^2 <= 2[(sigma^2 d+2 sigma S)varphi(d)
                    +(sigma^2+S^2)varphi(d)/d].

The upper Gaussian tail has been replaced by Mills' bound `Phi(-d)<=varphi(d)/d`.
Consequently this is an upper bound on the squared normalized query tail.
Mills' bound follows by replacing one by x/d in its positive tail integral.

The row subtraction's changed-residual term now uses `||qF||2<=4 sigma t`;
its learned-action term uses `||K||op||d2||2<=4 kappa^2t^3`. The middle
subtraction uses `||dF||2<=2 sigma t` and `||d2||2<=2 kappa t`. Thus

    Cw=(4+8 sigma T)c+(8L+16 sigma T)z+8 kappa^2+4LRa,
    CK=(2+4 sigma T)c+(4L+8 sigma T)z+4 kappa a,
    Ew(t)<=Cw t^4/4+2tau t^2,
    EK(t)<=CK t^4/4.

The known Duhamel row increment satisfies
`||dwB||4<=d0 t^2`, with `d0=2(3^(1/4)sigma+S)`. Using the exact spatial
remainder constant L/2 gives

    EZ(t)<=2Ew(t)+L d0^2 t^4+EK(t)+2 kappa a t^4,
    sup_u |f(t,u)-fF(t,u)| <= (c+2z)t^3.                    (N1)

The latter prediction estimate concerns the exact frozen-kernel observation
fF, not fB. It is an admitted, cheaper approximation for prediction alone;
the paired hidden outputs still include the nonzero nonlinear Duhamel motion.
No zero hidden motion is substituted into the paired-motion metric.
Every bound is uniform in time on the unchanged [0,T] and in the whole circle.
The interval preflight obtained

    Ew(T)<2.185161e-8,
    EK(T)<6.348280e-9,
    EZ(T)<6.472138e-8,
    sup_(t<=T,u)|f-fF|<2.416665e-6.

The lower and upper RMS measurements below require additional, explicitly
controlled spatial linearization errors, not included in EZ itself.

## One-dimensional initialized contractions

Let `h=tanh G`, `l=1-h^2`, and let `z~N(0,q)`, `H=tanh z`, `s=1-H^2`.
All expectations below are scalar one-dimensional Gaussian integrals. Define

    q=E h^2, k=E H^2,
    m=E l^2, n=E l^2 h^2,
    alpha=1-4k+3E H^4,
    gamma=(1-k)^2,
    v=E H^2s^2+kE s^2,
    V=(E l^4)(v+gamma^2q)+alpha^2 E l^4h^2.                (N2)

At the reference the two initial forward sources are independent N(0,q).
Set `U1=(H1-H2)s1`. The exact reverse source formula is

    P1=A0*U1=zeta1+alpha h1-gamma h2,
    Var(zeta1)=v.

Independence of zeta and g and oddness give `E[l1^4 P1^2]=V`.
For `J1=A0(l1^2P1)`, the forward source formula from the preceding finite-law derivation gives

    J1=xi+m U1,
    Var(xi)=V,
    Cov(xi,z1)=alpha n,
    Cov(xi,z2)=-gamma qm.

The source xi is correlated with z1,z2. Define

    A=alpha n/q, B=-gamma m, C=q+m.

Conditioning the joint Gaussian xi on z1,z2 gives mean `A z1+B z2` and
independent residual variance `V-q(A^2+B^2)`. Expanding
`E s1^2 [xi+C(H1-H2)s1]^2` and integrating the independent second coordinate
gives

    F=V E s^2 + A^2(E z^2s^2-qE s^2)
       +2C[A E zHs^3-B(E s^3)(E zH)]
       +C^2[E H^2s^4+kE s^4].                              (N3)

The B-squared term cancels between the conditional mean and residual variance.
The negative sign before B is essential: it arises from the -H2 part of U1.
An independent exact rational four-point product-law test checks this expansion
against the unexpanded squared conditional expression. It verifies the algebra,
not the Gaussian model by itself; that identification is the source-rule proof.

The readout state at the reference has `b1=b, b2=-b`, and its initialized upper
Gram is k times the identity. Hence

    b'=1-kb, beta'=b'b, b(0)=beta(0)=0.

The stored scalar beta is the diagonal beta of the full six-scalar candidate;
its off-diagonal entries are -beta. The exact current-state update used is

    b_new=exp(-k h)b_old+(1-exp(-k h))/k,
    beta_new=beta_old+(b_new^2-b_old^2)/2.                   (N4)

It retains the previous interval errors. The implementation performs one step
to .0025, saves its b,beta intervals, then uses those intervals for the second
step. A separate direct interval formula checks overlap with the restarted
result; this overlap is a sanity check in addition to the algebraic semigroup
identity. The formulas do not invoke any target trajectory or elapsed list.

The leading RMS outputs are `beta sqrt(V)` and `beta sqrt(F)`. Pairing is with
the same initial neuron coordinate throughout, not an independently coupled
initial marginal. Both support directions have the same squared norms, so
these are the correct training-averaged RMS values for their respective leading
increments.

For the extra spatial errors, use `||U1||2<=sqrt(1.04)`, `|U1|<=2`,
`|alpha|<=1`, and `0<=gamma<=1`. The alpha bound follows by inspecting
`(1-H^2)(1-3H^2)`, whose absolute value is at most one. Thus

    P4=3^(1/4)sqrt(1.04)+2 >= ||P1||4,
    R4=1.04+2*3^(1/4)sqrt(1.04)+2 >= ||qU1+J1||4.

For the second bound, J1's Gaussian source has variance
`E(l1^2P1)^2 <= ||P1||2^2 <=4||U1||2^2`; its response mU1 is bounded by two;
and qU1 is bounded by 1.04. The spatial tanh remainders therefore imply

    |D1_true-beta sqrt(V)| <= Ew + (L/2) beta^2 P4^2,
    |D2_true-beta sqrt(F)| <= EZ + (L/2) beta^2 R4^2.        (N5)

The moment and beta intervals are then included directly. These estimates
remain below the fixed RMS error limits when the preflight moment widths are
inserted. The retained errors are relative to the original initialization,
not reset to zero at restart.

## Outward arithmetic and quadrature proof

`H3_shorttime_solver.py` uses only Python standard-library Decimal and Fraction;
there is no dependency on mpmath, flint, scipy, or empirical quadrature differences.
Every arithmetic endpoint operation is followed by `next_minus` or `next_plus`.
Decimal exp and sqrt are correctly rounded; they are likewise widened by one
decimal ulp. Integer powers are implemented by these widened multiplications,
not by a general transcendental power function. Constants are exact decimal
rationals except pi, which is enclosed by

    pi=16 arctan(1/5)-4 arctan(1/239).

Each arctangent uses 64 exact rational alternating-series terms plus the next
term as a rigorous remainder. The identity follows from the tangent addition
formula and the signs/ranges of the two angles. Input q is an interval; its
square root and every upper Gaussian moment propagate this interval directly.
No covariance eigenvalue inversion occurs. The sole division by q is gated
by its certified positive lower bound; the kernel k is likewise positive before
the current-state update divides by it.

For a moment `E[z^a P(tanh z)]`, `z=sigma x`, the integrated function on the
standard Gaussian line is

    rho(x) sigma^a x^a P(tanh(sigma x)), a in {0,1,2}.

If Q is its polynomial factor in (x,h,sigma), differentiating it together with
rho applies the exact polynomial rule

    Q -> partial_x Q+sigma(1-h^2)partial_h Q-xQ.

Four exact integer-coefficient applications are used. With `0<=sigma<=1` and
`|h|<=1`, each monomial x^j rho(x) is bounded by the table
`(1,1,1,1,1,2,5)` for j=0,...,6. These bounds are verified in outward arithmetic
from its maximum at sqrt(j), or at zero for j=0. The sum of absolute polynomial
coefficients times these bounds is a rigorous supremum for the fourth
derivative. The largest value among used moments is 788640.

For completeness, the Simpson bound used requires no unverified numerical
library theorem. On [-h,h], its fourth-order Peano kernel, normalized to h=1,
is

    K(v)=(1-v)^4/24-[(1-v)^3+4(-v)_+^3]/18,
    -1<=v<=1.

For v>=0 it is `-(1-v)^3(1+3v)/72`; it is even on the negative half.
It is nonpositive and its absolute integral is 1/90. Applying the scalar
fourth-order integral remainder, with Simpson annihilating all cubic terms,
therefore bounds a panel error by `h^5 sup|f''''|/90`. Summing N/2 panels on
[0,R] and doubling for the even full-line integrand yields

    error <= R^5 sup|f''''|/(90 N^4).

The standard Gaussian tails, with `|P(tanh z)|<=1` for all the particular
nonnegative factored integrands used, are bounded by

    2rho(R)/R                        (a=0),
    2rho(R)                          (a=1),
    2rho(R)(R+1/R)                   (a=2).

These follow from Mills' inequality and one integration by parts. Since
sigma<=1, they also bound z^a. The tails add [0,bound]; quadrature remainder
adds a symmetric interval. Every Simpson weight is nonnegative, so interval
summation directly propagates all evaluation and initial-q uncertainties.
Roundoff is already included at each operation, rather than added as an
unverified last-digit tolerance.

At R=8,N=8192, the largest Simpson bound is below 6.376e-8 for an individual
initialized moment. Its effect on RMS is much smaller because the RMS output
is multiplied by beta, approximately T^2/2. The Gaussian tail bounds are below
1e-12. The implementation records the complete individual error budgets.


## Saved-state and numerical scope

The corrected executable stores interval endpoints for b,beta and the seven
initialized scalar contractions. The JSON checkpoint also stores exact rational
elapsed time, horizon 1/200, precision 60, and the original initialization as
the cumulative analytical error origin. Loading preserves every decimal endpoint.
It rejects nonfinite or reversed intervals, missing coefficients, nonpositive
q,k,V,F lower bounds, wrong precision/origin, and times outside the horizon.
The elapsed time chooses the cumulative analytical error envelope; it is not
an input to the autonomous coefficient vector field. Previous numerical
uncertainty is propagated by interval operations and is not reset on reload.

The driver writes its midpoint checkpoint, reloads it, and advances the
reloaded current state. The direct formula's interval is an additional sanity
check; the semigroup identity and directed arithmetic, rather than agreement,
justify restart. Nine deterministic tests include independent rational
arithmetic checks, exact contraction algebra, zero-variance integration,
nonzero-width serialization and boundary rejection.

This executable supports the fixed reference and named scalar observations.
The general finite-law equations above are mathematically specified but are
not a certified numerical API for arbitrary finite or nonatomic laws.
The L2/HS remainder bounds are fixed-order errors that do not vanish as the
quadrature panels or numerical precision increase. General same-layer joint
observation tuples are not implemented. No full C-H3 completion is asserted.

## Uniform time evaluation and the combined reference interface

The integrated driver H3_reference_solver.py combines the two initialized
components and checks their numerical compatibility. It writes and reloads
both the midpoint checkpoint and the circle kernel, then evaluates the future
prediction from those current records. Its prediction() adds the cumulative
analytical envelope to the numerical circle enclosure. Source/state provenance
is a premise of loading certified data; arbitrary invented coefficient files
are not validated certificates.

A small additional bound makes the circle readout-width budget uniform in
time, rather than merely checking three output times. The initialized k interval
is numerically checked to lie inside (.23,.24) with width d<3e-10. For a closed
step of length h, the exponential interval has width at most h d. The interval
for (1-exp(-kh))/k has width at most 2h d/.23, by changing numerator and
reciprocal separately and using 1-exp(-kh)<=kh. Starting at zero, at most two
steps of total length <=T have b upper endpoint at most (.24/.23)T plus
arithmetic reserve, below .006. Consequently their width is at most

    (.006+2/.23) T d + 1e-40 < 1.4e-11.

The 1e-40 allowance dominates all endpoint roundoff in these two scalar steps:
at precision 60, fewer than 100 elementary endpoint operations on magnitudes
bounded by two have aggregate absolute rounding error below 1e-54. A rational
step length is first enclosed by the same outward arithmetic. All initialization
uncertainty is already present in d. This proves that the 1e-8 radius budget
for circle observation is valid for arbitrary rational query times, using one
step before the midpoint and a second partial step after its saved state.
The coefficient formula is continuous in time; arbitrary computable times can
also be enclosed to any additional required time error. The stated uniform
mathematical bound uses the exact scalar formula for every real t in [0,T].
It does not depend on a finite time grid or temporal analyticity.

This is a bounded-reference convenience layer. It implements no higher-order
nonlinear refinement and expands neither the admitted law family nor the
observation alphabet of the underlying component.

## Resource and numerical claims to reproduce

The primary reference calculation uses 60 decimal digits, 8192 Simpson
subdivisions on [0,8] for each Gaussian stage, streamed moment sums, and exact
closed-form coefficient steps. Its reported final true paired RMS enclosures,
rounded outwards, are [4.4732053e-6,4.5182496e-6] and
[6.6076920e-6,6.7410684e-6]. Reported absolute errors are below 2.252213e-8 and
6.668817e-8. The prediction at e1 has reported enclosure
[.0011791368,.0011839702], with numerical-plus-analytic error below 2.416667e-6.
These are candidate claims to reproduce and verify from the complete producer,
not supplied numerical premises of its mathematical proof.

One execution is bounded by one core, 8 GiB resident memory and 900 seconds.
The recorded primary execution took 6.169790 seconds (6.166815 initialization,
.002975 evolution/checkpoint/observations), peak RSS 17836 KiB. A fresh
independent reproduction may have different timing; report actual values.
The two independent review reproductions have one run each; use a fresh
study-owned generated directory. No training campaign is authorized.

From the repository root, replacing FRESH by the assigned new run name:

```
python -B studies/observable_hierarchy/H3_shorttime_test.py
python -B studies/observable_hierarchy/H3_circle_kernel_test.py
python -B studies/observable_hierarchy/H3_reference_solver.py --output data/generated/observable_hierarchy/H3_FRESH
python -B studies/observable_hierarchy/H3_stability.py --output data/generated/observable_hierarchy/H3_FRESH_stability
```

The separate whole-circle observation extension, if included in the frozen
manifest, supplies its own complete proof, code, tests and reproduction command.
