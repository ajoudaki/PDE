# C-H3 route: finite short-time Duhamel computation

Date: 2026-09-12. Author: scoped independent agent `h3_shorttime_route`.
Status: first bounded theoretical assessment, not independently checked and not
an implemented or empirically validated solver. No neural training, canonical
trajectory, surrogate trajectory, or Gaussian quadrature was run. The numerical
values below are evaluations of displayed a priori formulas only.

## Conclusion

There is a concrete six-scalar autonomous candidate for a two-atom correlated
law: resum the initialized readout relaxation, and retain the quadratic forcing
that moves both hidden layers. Its initialization uses finitely many actual
forward/reverse Gaussian observations, including the transpose response terms.
At `Y=1, T=1/200`, conservative analytic error bounds are

| Observable or state | Absolute error bound |
|---|---:|
| First-layer paired RMS motion | 4.319e-8 |
| Upper-layer paired RMS motion | 1.299e-7 |
| Prediction, uniformly in the input direction | 8.515e-7 |
| First-row population L2 state | 4.319e-8 |
| Learned middle increment, HS norm | 1.096e-8 |

These bounds hold for every finite supported admitted law with labels bounded
by one, including nonorthogonal laws, and are independent of atom count. The
state and integration costs grow with atom count. They bound the same nonlinear
GF, not a substituted lazy target. Both hidden outputs of the candidate move.
They do not yet prove the bounds are small relative to the actual two RMS
signals: that requires certified evaluation of this candidate, which has not
been run. Nor does this fixed approximation give arbitrary requested accuracy.
Appending H2's dense dictionaries gives asymptotic convergence, but H2 supplies
no effective order or stopping certificate. Those are separate gaps.

## Scope and inputs

The assigned inputs were `H2_proposed_section_v3.md`, `docs/NOTATION.md`, and
established sections named as H2 dependencies. Read: H2 v3 in full; NOTATION in
full; global-nonlinear C.4.7.1–2 and C.4.7.8 parts 1–3,5–9; special-data
III.F.1–10. C.4.7.3–5 existence/tail/finite-network conclusions are used through
H2's stated dependency interface; their long proof bodies were not reread in
this scoped assessment. No trained passive-tail estimate is needed below.
On explicit supervisor expansion of scope, also read global-nonlinear A.3 in
full: it proves the sharp canonical initialized norm `||A0|| <= 2`. The looser
constant ten in III.F alone would not justify the numerical table above.
No H3 routes, other study material, history, or other findings were accessed.

Required skills read: `/etc/codex/skills/solve-math-rigorously/SKILL.md` and
`/etc/codex/skills/investigate-conjectures/SKILL.md`; the latter's
research-contract and adversarial-audit references. AGENTS and the research
workflow were read. No Git changes were made by this agent.

Input SHA256 hashes:

```
H2_proposed_section_v3.md c84617a514adaa43224c0f2990b75abb48eb92611ee3b45da753f47866ed90d2
docs/NOTATION.md 199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b
docs/global_nonlinear.md 947eb52f10a8ebcd4970fa2acb1d26cba25dc5d73e8839893d5d2f4e3f688161
docs/special_data_limits.md 5b7b48aa5deab320042217a6f284002366a683bf0f7f0b63c05d8167c526a489
```

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

## Effective law family and the H2 bridge

A concrete data family can be two atoms with positive specified masses, bounded
specified labels, and normalized directions in small arcs about e1 and e2,
restricted to H2's fixed ball. The second direction may rotate toward the first,
so the Gram off-diagonal is nonzero. Parameters can be rational or computable
with certified errors. The cost and all constants above do not rely on a
positive covariance eigenvalue. One can include more atoms at a declared cost.
For the full Borel ball, an effective integration representation with certified
law approximation is additional input; arbitrary Borel descriptions do not
constitute an algorithm. H2's radius is qualitative, so a completely numerical
membership test also needs an effective certified radius or an explicitly
promised in-ball family.

The natural H2 dictionary pilot contains h_a, D_ab, saturated P_ab, saturated
z_a, and optionally saturated versions of the leading V fields. Append this
fixed pilot to H2's nested dense enumeration and ridge scheme. The algebraic
density argument and all H2 convergence conclusions survive finite enrichment.
One can then evolve the full nonlinear H2 equations. The present Duhamel fields
give an explicitly computable short-time reference for estimating its initial
action omissions. They do not yet furnish an a posteriori bound for every
learned dictionary omission: that subtraction and its numerical constants must
still be supplied. In particular H2's target-dependent epsilon_N cannot be used
as a practical order selector.

For arbitrary requested epsilon there are two possible continuations, both open
in this assessment: prove computable tails for the appended H2 dictionary, or
derive a verified residual certificate for a finite H2 trajectory and search
orders until that certificate succeeds, with a separate proof of termination.
Qualitative convergence alone does not prove termination of such a certification
test. The six-state candidate has a fixed error floor; increasing arithmetic
precision cannot remove it.

## Audit, exact gaps, and cheapest next assessment

1. **Useful relative motion remains to be certified.** Evaluate the candidate
   paired RMS values and verify, for a preregistered nonorthogonal in-ball law,
   that each is comfortably larger than its analytic error plus quadrature and
   roundoff errors. Neither positivity at an unspecified t_a nor asymptotic
   O(t^2) alone supplies a numerical margin at T.
2. **Numerical integration is specified but not implemented.** Initial
   contractions and final observables are low-dimensional Gaussian integrals
   for m=2. A valid implementation needs Gaussian-tail truncation, interval
   quadrature, covariance-error propagation at singular cases, and arithmetic
   error control. Ordinary high-order quadrature differences are not a proof.
3. **All-time uniform numerical output is not automatic.** The analytic bounds
   are uniform for t<=T and all u, but computed point values need time/input
   interpolation certificates if the delivery target includes whole curves.
4. **Autonomy passes for the candidate; model closure is approximate.** b,beta
   determine its future without history. Its readout evolution is frozen while
   the output features move. The explicit comparison bounds justify that
   approximation on this horizon, but it is not an exact canonical GF closure.
5. **Arbitrary accuracy and broad observation graphs remain open.** This
   candidate certifies only the named prediction and hidden motion outputs.
   H2 supplies a separate asymptotic foundation for arbitrary fixed graphs;
   effective H2 completion remains necessary for full C-H3.
6. **The exact formula extension is narrow.** Formula (S5) has its bounded-word
   limiting proof above. Use the finite R version if initialization must be a
   literal finite alphabet program. Do not infer a general unbounded-action
   calculus from this one explicit formula.

The highest-leverage next authorized step is a bounded implementation of the
two-dimensional initialization integrals and three-dimensional training-output
integrals for one preregistered rotated two-atom law, together with interval
certificates. Its pass criterion should require prediction error below a named
absolute tolerance and both paired RMS lower bounds to exceed their total error
by a named factor, e.g. ten. No further trajectory or quadrature computation
is authorized or claimed by this first assessment.
