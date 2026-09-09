# Isolated adversarial review: positive-time middle curvature

Date: 2026-09-06.

## 1. Verdict and isolation boundary

**Scoped mathematical verdict: PASS for the advertised local conclusions.**
The independent-source construction, quantitative lower-tail argument,
passage to the actual local population flow, and two-sided unbounded
full-loss second directional derivatives are supported by the permitted
premises. I found no substantive gap requiring a new estimate or a new
mathematical premise.

**Literal-text qualification: one minor required correction.** The auxiliary
Gaussian-process lemma in candidate lines 178–182 needs the word
“centered.” Without it, that separately stated lemma is false. Every
process to which the candidate applies the lemma is already centered, so
this correction does not change the theorem, its proof strategy, or any
application. Section 15 below gives the exact correction and distinguishes
it from optional clarifications.

This is a local modular verdict, not approval of a global two-label
theorem. In particular, it does not establish global opposite-label
continuation, an all-time estimate, a finite-width positive-time Hessian
limit, or a bounded/Frechet Hessian on the entire raw Hilbert space.

I read the candidate and all four mathematical dependencies explicitly
listed in its Section 1 in full myself. I imported only the scopes listed
below. I did not read histories, ledgers, other review files, or additional
research documents. References to reviews inside the permitted documents
were not used as evidence. Documents mentioned only inside dependencies
were not opened or silently imported. No experiments, simulations, or
numerical proof tests were performed. The candidate was not edited.

The solve-math-rigorously skill governed the proof audit: in particular,
the report checks hypotheses, quantifiers, limiting operations, and exact
directional derivatives. It supplied no mathematical premise.

## 2. Exact source manifest and allowed imports

All five observed SHA256 values matched the candidate/user manifest.
Line references in this report refer to these exact versions.

1. Candidate:
   `/tmp/l3-two-sample-proof-DLuelg/POSITIVE_TIME_MIDDLE_CURVATURE.md`

   SHA256:
   `0b2999b92442dbbd1f43faff3202eb79a62453271b43f2d10a90e263fa34b78d`

   Read all 435 lines; reviewed all eight sections.

2. Short-response dependency:
   `/tmp/l3-two-sample-proof-DLuelg/TWO_SAMPLE_SHORT_RESPONSE_BOOTSTRAP.md`

   SHA256:
   `9305453f933ad30a0e813e4e97942ee9e00490ce726d70142b25c8f67a475170`

   Read all 352 lines. Imported the finite two-sample Gaussian Euler law,
   both backward response estimates, forward-memory bounds, and Gaussian
   query envelopes on feature time `[0,3/2]`. Its remarks about subsequent
   assembly are not independent premises.

3. Activation/local bridge:
   `/tmp/l3-two-sample-proof-DLuelg/SECH_LOCAL_JET_AND_SIGN_BRIDGE.md`

   SHA256:
   `65fab11c5892afe517fe4289450f0736bb137bb1a118e85f8ea8541e18a017f8`

   Read all 433 lines. Imported only Sections 1–2 insofar as they transfer
   the local response/construction argument to the specified activation,
   preserve common bounded operators and adjoints, remove cuts locally,
   and supply sample symmetry. No static jet law, cubic remainder,
   density bound for initial jets, or sign-change conclusion was imported.
   The optional enlargement for static jets in its Section 1 is not
   needed here.

4. Local assembly and scalar gradient:
   `/tmp/l3-two-sample-proof-DLuelg/SAME_LABEL_GLOBAL_ASSEMBLY.md`

   SHA256:
   `510fd019c204e0e89e0c6bcb99c031a11de974b05323df1c016c72b263f64a44`

   Read all 358 lines. Imported Sections 1–2 and only the symmetry and
   scalar-gradient arguments of Section 3. Did not import the same-label
   fitting lower bound, its global physical clock, later finite physical
   GD/GF conclusions, or its nontriviality claims.

5. Elementary construction and limiting tools:
   `/tmp/l3-standalone-proof-D6AW4s/L3_GLOBAL_SELF_CONTAINED_PROOF.md`

   SHA256:
   `bebbb70a8f8da8fd2fa5304fc7af08026e72aef73e20f77f046509f87e63954e`

   Read all 1789 lines. Imported only the elementary Gaussian finite-
   program, common-operator, and limiting tools used by the preceding
   dependencies: principally Sections 2–3 and the common-space/action
   construction in Section 5. Did not import its one-sample global theorem,
   special first-coordinate transformation, global fitting clock, or
   later nontriviality results. Its explicit elementary Gaussian-tail
   calculation can also be checked directly as done below.

The activation facts needed here require no unlisted activation-design
file. Direct differentiation gives

    phi(z) = 1 + 0.1 atan(sinh z),
    phi'(z) = 0.1 sech z,
    phi''(z) = -0.1 sech z tanh z.

Thus `5/6 < phi < 7/6`, `0 < phi' <= 1/10`, and
`|phi''| <= 1/5`; in fact the last bound is deliberately loose. The
smoothness/bounded derivatives used in the finite cut programs also hold.

## 3. What must be proved, and dependency sufficiency

Write `T=3/2`. In this report, `Kcap` denotes a cutoff level and `R`
always denotes the desired tail threshold. This separates two roles
which the candidate writes using the same letter.

The substantial conclusion is a joint lower bound, for each fixed small
positive `S`, sample `a`, nondegenerate interval `I`, and sign `sigma`:

    P(Z_a^(2)(S) in I, sigma q_a^(2)(S) > R)
        >= c_I exp(-C_I(R+1)^2),    R >= 1.

An unconditional lower tail for `q` would not suffice. Nor would a
positive-probability support argument without a quantitative probability
bound. The candidate provides both the joint constraint and the quadratic
Gaussian exponent.

The response dependency supplies, with both sample sums retained,

    |A_(ka,rb)| <= (3/4) Delta,
    sum_(r<=k,b) |B_(ka,rb)| <= 1.

Its proof closes the current rows in causal order: bottom forward
response, middle/top forward fields, top backward row, then middle
backward row. It does not use the current bottom row to establish itself.
The two-label factor `1/2` is retained in each learned memory; summing
over two samples changes `(3/4)Delta` into `(3/2)Delta`, as used in the
candidate. The stated margins `3067/3200 < 1` and
`71063018523/73728000000 < 97/100` leave room for the weak bounds used
here. The argument uses only the three activation bounds above, smooth
cuts, and zero readout, so the allowed activation transfer applies.

The local assembly supplies fixed-cap Euler convergence, common bounded
actions with actual adjoints, strong cut removal, and restart uniqueness
on the constructed feature interval. Its comparison coefficient is
linear in `Kcap`, while its reference tail is Gaussian. To see the relevant
decay directly, `E exp(q^2/16) <= 2` implies

    E[q^2 1_(|q|>u)] <= 64 exp(-u^2/32),
    ||(|q|-Kcap/2)_+||_2 <= 8 exp(-Kcap^2/256).

The second inequality follows by bounding the positive part by
`|q| 1_(|q|>Kcap/2)` and taking a square root. Hence factors
`exp(C Kcap)` in the comparison are absorbed. No opposite-label fitting
bound is needed for the local result.

The scalar-gradient argument extends to signed linear combinations of
the two predictors by linearity. The imported same-label lower bound on
the readout component of that gradient is not used for opposite labels.

**Assessment:** the allowed scopes contain the necessary local premises;
the candidate does not require any excluded jet or global theorem.

## 4. Source-group independence and frozen deterministic coefficients

Candidate lines 83–107 and Sections 4–5 are supported by the exact source
rule, rather than by an assertion that trained neurons are independent.

The short-response source law explicitly has four independent centered
Gaussian groups (lines 50–58). The two groups needed in population 2 are
the forward source for the initial second matrix and the reverse source
for the initial third matrix. Their complete finite arrays are independent;
time/sample coordinates within a group retain their full covariance.

This representation is justified in the elementary dependency as follows.

1. Conditional on earlier matrix queries, the unrevealed part of a
   Gaussian matrix is an orthogonal Gaussian residual. A new adaptive
   query is known given that transcript. Querying one matrix imposes a
   linear constraint only on its current conditional residual; the two
   matrix residuals remain conditionally independent.

2. A fixed-rank Gaussian projection removed at each call has normalized
   mean squared size at most its rank divided by width. At a fixed finite
   number of calls this disappears in empirical second moments. The
   fresh coordinate innovation is independent of the preceding scalar
   transcript.

3. Gaussian integration by parts converts the response coefficients
   into expected derivatives of the complete coordinate expression.
   A new source is a deterministic linear combination of previous
   sources in its own orientation plus an independent Gaussian
   innovation. Its covariance is the full second-moment Gram of its
   inputs. This preserves independence of distinct source groups.

4. Learned rank updates contribute the explicit deterministic memory
   terms. Restoring their finite empirical contractions is justified
   by finite-program Lipschitz comparison; it is not an assertion of
   independence for finite trained coordinates.

Relevant elementary-source locations are lines 313–425 and 429–475;
the two-sample instantiation is short-response lines 60–108.

For singular input Grams, the elementary proof adds independent small
query perturbations, proves the finite law at fixed perturbation, and
removes them using a same-matrix finite-program comparison and continuous
covariance square roots. The number of instructions remains fixed at
this stage. The block-diagonal Gaussian source covariance, and hence
independence of distinct groups, is preserved on removing perturbations.

Once this limiting finite-array law has been constructed, `A`, `B`, and
the covariance matrices are deterministic parameters of a probability
distribution. Conditioning on a source realization does not re-solve
the equations which selected those parameters. The candidate's source
variation is therefore legitimate. Differentiating their selection
equations would describe a different operation and is unnecessary.

The population-2 recursion is also genuinely causal. At node `k`, both
current preactivations use only past deltas; current features are then
computed; current reverse queries may use those features; current deltas
are computed last. Present-time entries of `B` do not create an implicit
equation for the current preactivations.

**Assessment:** no missing source-group independence, omitted trained
memory, or invalid self-consistency differentiation was found.

## 5. Cap- and mesh-uniform temporal increments

Candidate Section 3 does not infer a whole-path bound from marginal tails.
It first obtains a deterministic RMS increment bound. Here is a fully
explicit version of that step.

Work on the finite initial event that both operator norms are at most
10, and use RMS vector norms. Set

    Q4 = a T,
    M3 = 10 + a e Q4 T,
    M2 = 10 + a e^2 M3 Q4 T.

Zero initial readout and its Euler update give the coordinate bound
`|W4_k| <= a t_k <= Q4`. The rank-one update formulas then give, successively,

    ||W3_k||_op <= M3,
    ||delta3_(k,b)||_2 <= e Q4,
    ||q2_(k,b)||_2 <= M3 e Q4,
    ||delta2_(k,b)||_2 <= e^2 M3 Q4,
    ||W2_k||_op <= M2,
    ||q1_(k,b)||_2 <= M2 e^2 M3 Q4.

These estimates use `|tau_Kcap(q)| <= |q|`. They have no dependence on
either cutoff or on the number of mesh nodes.

Because `sum_b |C_ab|/2 <= 1`, first-field increments are bounded by
`V1 Delta`, where `V1=e^3 M2 M3 Q4`. Matrix increments obey

    ||W2_(k+1)-W2_k||_op <= Vw2 Delta,
    ||W3_(k+1)-W3_k||_op <= Vw3 Delta,
    Vw2 = a e^2 M3 Q4,    Vw3 = a e Q4.

The exact forward split in candidate lines 152–155, followed by the
Lipschitz bound on `phi`, gives preactivation increment constants

    V2 = a Vw2 + M2 e V1,
    V3 = a Vw3 + M3 e V2.

Finally,

    delta3_(k+1,b)-delta3_(k,b)
      = (W4_(k+1)-W4_k) phi'(Z3_(k+1,b))
        + W4_k[phi'(Z3_(k+1,b))-phi'(Z3_(k,b))],

so its RMS norm is at most

    D Delta,    D = a e + Q4 c V3.

Telescoping proves (7) for every pair of mesh nodes. The finite Gaussian
program gives convergence of the empirical square of this difference
at each fixed mesh/cap. Since the initial norm event tends to probability
one, the deterministic limiting second moment satisfies the same bound.
There is no need to condition the limiting source law on that event.

Using the full second-moment covariance identity,

    E|zeta_(k,b)-zeta_(j,b)|^2
      = E|delta3_(k,b)-delta3_(j,b)|^2,

gives (8). This identity would not be justified by replacing the input
Gram by a centered covariance, but the sources explicitly use full
second moments. Zero readout gives `zeta_(0,b)=0`.

**Assessment:** the temporal estimate is valid uniformly in width on the
initial norm event, and uniformly in both caps and all finite meshes.
No bound on a maximum of independent time slots is being smuggled in.

## 6. Gaussian chaining and residual projection

Linear interpolation of a finite Gaussian array is a continuous centered
Gaussian process. Within a mesh cell, an increment is a scalar multiple
of the adjacent-node increment; across cells, split at the intervening
nodes. The triangle inequality in `L2` then preserves the bound
`||zeta(t)-zeta(u)||_2 <= D|t-u|`.

For centered Gaussian variables of variances at most `v^2`, regardless
of dependence, the union bound gives

    P(max_(i<=N)|Y_i| > z) <= min(1, 2N exp(-z^2/(2v^2))).

Integrating this tail above and below `v sqrt(2 log(2N))` gives

    E max_(i<=N)|Y_i|^2 <= 2v^2(log(2N)+1).

At dyadic level `j`, the increment standard deviation is bounded by
`DS 2^(-j)` and there are at most a constant times `2^j` increments.
The `L2` norm of the maximum at that level is therefore at most
`C DS 2^(-j) sqrt(j+1)`. Summing these norms by Minkowski gives (9),
because that numerical series converges. Including endpoint `S` at
the initial level covers the right endpoint as well. Finite-dimensional
sample-path continuity justifies the dyadic reconstruction.

For regression on one terminal scalar `X`, write
`G(t)=zeta(t)-Cov(zeta(t),X)X/v`, where `v=E X^2>0`. For any two times,

    E|G(t)-G(u)|^2
      = E|zeta(t)-zeta(u)|^2
        - Cov(zeta(t)-zeta(u),X)^2/v
      <= D^2 |t-u|^2.

The same scalar is used for every coordinate of the residual array, so
this applies after interpolation and across both sample paths separately.
Each residual starts at zero. Taking the maximum over two samples costs
only a fixed factor, by bounding its square by the sum of the two squared
suprema. Markov therefore gives a cap/mesh-independent `B0` such that
the whole residual array is bounded by `B0` with probability at least
`1/2`.

This argument does not take a continuum Gaussian-process limit and does
not assume independence in time. Projection onto the single terminal
scalar does not increase the increment variance.

**Minor literal issue:** the standalone statement of (9) omits
“centered.” The proof itself correctly uses centered Gaussian maxima,
and all its actual applications are centered. See required correction R1.

## 7. Positive terminal variance, including rho = -1

For `|rho|<1`, the initial first-field pair has a positive density on
`R^2`. If a linear combination of its two features were zero almost
surely, continuity would make

    alpha phi(z1) + beta phi(z2) = 0

for all `z1,z2`. Varying `z1` and then `z2`, using that `phi` is
nonconstant, forces both coefficients to vanish. Thus its full feature
Gram is positive definite.

At `rho=-1`, write `b(G)=0.1 atan(sinh G)`. The two features are
`1+b(G)` and `1-b(G)`, with `E b=0` and `E b^2>0`. Their Gram is

    [[1+E b^2, 1-E b^2],
     [1-E b^2, 1+E b^2]],

whose eigenvalues are `2` and `2E b^2`. It is positive definite although
the raw Gaussian pair has rank one. This distinction is essential.

At initialization, the next forward pair has covariance equal to this
full feature Gram, hence is a nondegenerate Gaussian pair. Repeating the
same argument establishes positive-definite feature Grams at the next
two layers. In particular, for either sign configuration,

    ||V0||_2^2 = (1/4) y^T K3(0) y > 0,
    V0 = (1/2) sum_b y_b H3_(0,b).

Readout integration and strong feature continuity give
`W4(S)/S -> V0` in `L2`. Therefore, by shrinking a deterministic `S0>0`,
`||W4(S)||_2 >= S ||V0||_2/2` for every `0<S<=S0`. The first-feature
Gram remains positive definite by continuity of its entries, and
`|g(S)|<1/2` follows from `g(0)=0` and continuity. One can choose
`S0<T` without changing the claim.

Since `phi'(z)>0` at every finite `z`, a nonzero `L2` readout cannot
be annihilated almost surely by multiplication by `phi'(Z3_a(S))`.
Hence `v_a(S)=E delta3_a(S)^2>0` for both samples. This step requires no
pointwise lower gate bound and no sign-definiteness of the readout.

At this fixed `S`, strong cut removal first makes the cut terminal
second moment within, for example, `v_a(S)/4` of its uncut value.
For each such fixed cap, sufficiently fine meshes make their second
moments within another `v_a(S)/4`. Thus

    v0 = v_a(S)/2 <= E zeta_(M,a)^2 <= v1 = (eaS)^2

holds for all sufficiently large caps and then all sufficiently fine
meshes, with `v0,v1` independent of both. The required mesh threshold
may depend on the fixed cap. The candidate never needs otherwise.

**Assessment:** nondegeneracy covers all prescribed correlations and
both label modes. Constants need not be uniform as `rho -> 1` or
`S -> 0`. At `S=0` the reverse query is zero, so the strict positive-time
qualification is necessary. At excluded `rho=1` with opposite labels,
the readout mode could vanish identically; that configuration is not
being incorrectly included.

## 8. Reverse scalar regression and the large-query event

Take `X=zeta_(M,a)`, with variance `v in [v0,v1]`. Define for every
sample/time coordinate

    c_(k,b) = E[zeta_(k,b) X]/v,
    G_(k,b) = zeta_(k,b) - c_(k,b) X.

The joint vector `(X,G)` is Gaussian and all cross covariances vanish.
Its characteristic function therefore factors, proving independence
of the entire residual array from `X`, including for singular covariance
matrices. This needs no inverse of a time/sample Gram.

Cauchy–Schwarz gives

    |c_(k,b)| <= eaS/sqrt(v0) =: cstar.

Intersect the residual event from Section 6 with

    sigma X in [R+a+1, R+a+2].

The latter interval has length one, and its probability is at least

    (2 pi v1)^(-1/2) exp(-(R+a+2)^2/(2v0)).

By independence, the intersection has at least half that probability.
On it,

    max_(k,b)|zeta_(k,b)| <= cstar(R+a+2)+B0 =: B_R.

The deterministic row bound and bounded features imply, for every
possible forward-source realization,

    |q_(k,b)-zeta_(k,b)| <= a,
    sigma q_(M,a) >= R+1.

This is the decisive uniformity: the event can be defined entirely from
the reverse source, and every forward realization subsequently used to
place the preactivation preserves the query lower bound. No independence
of the *actual* response shift from `X`, or of the actual `q` from `Z`,
is needed.

**Assessment:** the reverse event has the claimed Gaussian lower cost
and controls the whole path uniformly in all relevant approximations.

## 9. Forward regression, source variation, and quantitative interval mass

Let `Xf=xi_(M,a)`. Its variance is
`vf=E(H1_(M,a))^2 in [m^2,a^2]`. Regression gives

    xi_(k,b) = d_(k,b) Xf + F_(k,b),
    |d_(k,b)| <= a^2/m^2 =: d0,
    d_(M,a)=1,    F_(M,a)=0.

The last identity holds identically for the regression residual. The
whole residual `F` is independent of `Xf`; both together are independent
of the reverse group. Thus the conditional law of `Xf`, given `F` and
the reverse group, is still `N(0,vf)`.

Even for singular source covariance, this variation stays within the
conditional Gaussian support: `(Xf,F)` has a product Gaussian law,
and `Xf` is a nondegenerate scalar. The pointwise estimates can be made
for every residual in its support; conditional probability assertions
need only hold almost surely in the conditioning variables.

Fix a residual and a reverse realization in the event of Section 8.
Let `Z_(M,a)(x)` be the output when `Xf=x`, holding all deterministic
coefficients and covariance parameters fixed. For every `x`,

    |q_(k,b)(x)| <= B_R+a,
    |delta_(k,b)(x)| <= e(B_R+a).

There are `2M` terms in the terminal forward memory, each coefficient
at most `(3/4)Delta` in magnitude. Since `F_(M,a)=0`,

    |Z_(M,a)(x)-x| <= (3/2)S e(B_R+a) = D_R.

This bound is uniform in `x` and in all other forward residual values.
An uncontrolled terminal residual would invalidate the next density
bound, but the scalar regression cancels exactly that residual.

For two scalar values, define
`E_k=max_(j<=k,b)|Z_(j,b)(x)-Z_(j,b)(x')|`. Then

    |q_(r,b)(x)-q_(r,b)(x')| <= e E_r,
    |delta_(r,b)(x)-delta_(r,b)(x')|
       <= [c(B_R+a)+e^2] E_r = L_R^0 E_r.

The first term in the second bound changes the gate while keeping a
query fixed; the second changes the query through a one-Lipschitz cut.
Thus no factor of `Kcap` occurs. The direct source change is at most
`d0|x-x'|`, and summing the two samples gives

    E_k <= d0|x-x'| + (3/2)Delta L_R^0 sum_(r<k) E_r,
    E_M <= d0 exp((3/2)S L_R^0)|x-x'| = L_R |x-x'|.

Consequently `D_R <= C(R+1)` and `L_R <= C exp(C(R+1))`, uniformly in
caps, meshes, and conditioning residuals. All constants here may depend
on the already fixed `S` and configuration.

Choose `[b-h,b+h]` inside the interior of `I`, with `h>0`. The displacement
bound gives output at most `b-1` at `x=b-D_R-1` and at least `b+1` at
`x=b+D_R+1`. Continuity therefore produces some `x0` between those
points with output `b`. Global surjectivity also follows from the same
bounded-displacement property, but only this one crossing is needed.

On the scalar interval

    |x-x0| <= r_R := min(1/2, h/(2L_R)),

the output lies in `[b-h/2,b+h/2]`, and

    |x| <= |b|+D_R+3/2,
    r_R >= c exp(-C(R+1)).

The conditional Gaussian density on that interval is at least

    (sqrt(2 pi) a)^(-1)
       exp(-(|b|+D_R+3/2)^2/(2m^2)).

Multiplying by its length `2r_R` yields the claimed conditional lower
bound `c exp(-C(R+1)^2)`. The linear exponential loss from the Lipschitz
constant is absorbed in the quadratic exponent for `R>=1`.

No measurable choice of `x0` is necessary. The conditional probability
is the integral, against a scalar Gaussian density, of the indicator
of the continuous map's fixed closed preimage. For each fixed residual
and reverse realization that preimage contains an interval of the
specified length in the specified bounded region. This uniform lower
bound on its integral is measurable and can be integrated over `F`.

Finally integrate over the reverse event. Its probability has a
Gaussian lower bound, and the query lower bound holds for every forward
value. Multiplication of the two probability bounds retains the form
`c exp(-C(R+1)^2)`.

**Assessment:** continuity alone would be insufficient quantitatively;
the uniform displacement bound, uniform exponential Lipschitz bound,
and scalar Gaussian density supply exactly what is missing from a mere
support/surjectivity argument. They are all present and valid here.

## 10. Order of limits and closed events

For fixed `S`, `I`, sign, and threshold `R`, use the closed set

    F_R = [b-h/2,b+h/2] x {q : sigma q >= R+1}.

Its lower probability bound holds for every sufficiently large `Kcap`
and then every sufficiently fine mesh, with constants independent of
both. The precise order is:

1. The finite-width Gaussian-program identification is used only at
   each fixed mesh and cap.
2. For each sufficiently large fixed cap, let `Delta=S/M -> 0` to
   obtain the cut terminal law.
3. Remove the cap using the joint strong convergence of the terminal
   fields and queries.

For probability laws `mu_j -> mu` weakly and a closed set `F`, the
correct inequality is `mu(F) >= limsup_j mu_j(F)`. To verify it here,
the bounded continuous functions

    f_k(x) = max(0, 1-k dist(x,F))

majorize `1_F` and decrease to it. Thus
`limsup_j mu_j(F) <= integral f_k dmu` for each `k`; let `k -> infinity`.
Neither boundedness of `F` nor zero boundary mass is required.

Apply this argument twice with the same closed `F_R`. The final event
is contained in the desired event because its interval lies inside `I`
and `sigma q >= R+1` implies `sigma q > R`. No lower bound is passed
directly through an open-set inequality with the wrong direction.

The proof may be repeated for arbitrary fixed `R>=1` with the same
constants. It is not necessary to interchange `R -> infinity` with any
of the approximation limits, or to construct a common almost-sure event
simultaneously for uncountably many times or intervals.

**Assessment:** both limiting passages and all quantifier orders are
valid. There is no width-dependent number-of-queries assumption.

## 11. Curvature multiplier tails

Let `J` be a fixed closed interval of positive length in `(1,2)`. Define
`kappa=min_(z in J)|phi''(z)|>0`. On this interval `phi''<0`; also
`|phi''|<=c` everywhere. If

    M_a = y_a phi''(Z_a^(2)(S)) q_a^(2)(S),

then, for either desired multiplier sign `eta`, choose query sign
`sigma=-eta y_a` and query threshold `R/kappa`. The joint tail theorem
gives

    P(Z_a^(2)(S) in J, eta M_a > R)
        >= c_J exp(-C_J(R+1)^2),    R>=1,

after changing finite constants. The required query threshold is in the
allowed range since `kappa<1`.

The upper envelope gives, globally and hence also on the interval,

    P(|M_a|>R) <= P(|q_a^(2)(S)|>R/c)
                 <= 2 exp(-R^2/(16c^2)).

Both signs are essentially unbounded even after imposing the fixed
preactivation interval. If one wants the tails conditional on being
in `J`, divide by its positive probability; this changes only constants.
There is no claim of a precise Gaussian asymptotic, common upper/lower
rate constant, or Gaussian distribution for the trained multiplier.

## 12. Raw metric and exact unit sample-isolating directions

The relevant population parameter space is the affine Hilbert space of
raw first-field variations, Hilbert–Schmidt increments of the second
and third matrices, and `L2` readout variations. The initialized operators
themselves need not be Hilbert–Schmidt; only variations and trained
increments use that norm.

For `|rho|<1`, the prescribed first-field squared norm is
`E[v^T C^(-1)v]`. To check its raw scaling, put the input rows in `X`,
so `XX^T=dC` for RMS-one inputs. For a raw row variation producing
first-field pair `v`, the minimum Euclidean row norm is
`v^T(XX^T)^(-1)v`; multiplication by `d` gives `v^T C^(-1)v`.
Summing rows and dividing by width is exactly the first block of the
finite metric. Orthogonal first-weight directions are frozen and are
irrelevant to this test.

At `rho=-1`, first-field variations have the form `(v,-v)`, and the
raw quotient metric is `E v^2`, with no extra factor two. Equivalently,
the pseudoinverse of `C=[[1,-1],[-1,1]]` is `C/4`, and
`(v,-v)^T(C/4)(v,-v)=v^2`. No inverse of the singular `C` is being used.

At the reached state the first-feature Gram `K` is positive definite.
With the candidate's selector

    B_a = sum_b (K^(-1))_(ab) H1_b / sqrt((K^(-1))_(aa)),
    d_a = 1/sqrt((K^(-1))_(aa)),

matrix multiplication gives

    E B_a^2 = 1,
    E[B_a H1_b] = d_a 1_(a=b).

`B_a` is bounded, since it is a finite linear combination of bounded
features, and `d_a>0`. For any bounded `v in L2(Omega2)` of norm one,
let the full raw direction `U` have only one nonzero block,

    U_W2 = v tensor B_a.

Then `||U||_raw=||v tensor B_a||_HS=1`. Its finite counterpart has
entries `v_i B_j/n`, so

    ||v B^T/n||_F^2
       = ((1/n)sum_i v_i^2) ((1/n)sum_j B_j^2).

This verifies the normalization without an extra width factor.
The whole direction leaves the first-field block zero, so the
antiparallel first-field metric causes no additional issue.

Along the actual parameter line `W2(h)=W2+h(v tensor B_a)`, all other
parameter blocks are fixed and

    Z2_b(h) = Z2_b + h d_a v 1_(a=b).

The other sample is therefore unchanged on the entire line, not merely
to first order. The selector, the event used to define `v`, and the
direction are fixed at the base state; they are not differentiated.

This parameter perturbation is distinct from the earlier conditional
source variation. No finite-program law or covariance identity is
assumed to persist along this parameter line.

## 13. Existence and value of the exact second directional derivative

Set `z=Z2_a`, and use a real line parameter `h`. Since `v` is bounded,
`v^2 in L2`, and the map

    h -> phi(z+h d_a v)

is twice continuously differentiable into `L2`. Its derivatives are
`d_a phi'(z+h d_a v)v` and `d_a^2 phi''(z+h d_a v)v^2`.
Bounded derivatives of the activation and dominated convergence justify
these formulas. Applying the bounded current `W3` gives an `L2` curve
`z3(h)` with

    u := z3'(0) = d_a W3[phi'(z)v],
    w := z3''(0) = d_a^2 W3[phi''(z)v^2].

No `L4 -> L4` or `L2 -> L4` property of `W3` is assumed.

To verify an ordinary scalar second derivative, rather than only a
formal second-order expansion, consider

    F(h) = E_3[W4 phi(z3(h))].

The readout is fixed and satisfies `|W4|<=aS`. First differentiation
gives

    F'(h) = E_3[W4 phi'(z3(h)) z3'(h)].

To differentiate this at zero, split its difference quotient into

    E_3[W4 phi'(z3(h)) (z3'(h)-u)/h]

and

    E_3[W4 u (phi'(z3(h))-phi'(z3(0)))/h].

The first term tends to `E_3[W4 phi'(z3(0)) w]`. For the second, write
the gate difference quotient as the product of
`(z3(h)-z3(0))/h -> u` in `L2` and the integral of `phi''` along that
preactivation increment. The latter factors are uniformly bounded by
`c` and converge in probability to `phi''(z3(0))`. Multiplication by a
bounded converging factor preserves strong `L2` convergence, by
truncating the fixed limiting `L2` factor. Thus that quotient converges
in `L2` to `phi''(z3(0))u`. Pairing with `W4 u in L2` gives

    F''(0) = E_3[W4 phi''(Z3_a) u^2]
             + E_3[W4 phi'(Z3_a) w].

This explicitly justifies the second derivative with only `u in L2`.

For completeness, the Taylor cross-error sentence in candidate lines
373–375 can be quantified as follows. If
`z3(h)=z3(0)+h u+r_h`, where `||r_h||_2=O(h^2)`, then

    |E W4[phi(z3(0)+h u+r_h)-phi(z3(0)+h u)
                         -phi'(z3(0))r_h]|
      <= c ||W4||_infinity
           (|h| ||u||_2 ||r_h||_2 + ||r_h||_2^2/2)
      = O(|h|^3).

The line parameter in the first product is useful to display; an
`O(||u||_2 ||r_h||_2)` estimate alone would only be `O(h^2)`.
The sharper estimate follows from the candidate's existing hypotheses,
as the direct derivative proof above also shows.

Now `delta3_a=W4 phi'(Z3_a)` and `q2_a=(W3)^*delta3_a`. The quantity
`phi''(z)v^2` is in `L2`, so actual adjunction gives

    D^2 g[U,U]
      = (d_a^2/2) E_2[y_a phi''(Z2_a) q2_a v^2]
        + (y_a d_a^2/2) E_3[W4 phi''(Z3_a)
                                (W3[phi'(Z2_a)v])^2].

This is exactly (22), including the sample factor `1/2` and the factor
`d_a^2`. The second term has absolute value at most

    Ctop = (d_a^2/2) aS c ||W3||_op^2 e^2,

uniformly over the unit directions under consideration. It needs no
fourth moment because the squared `W3` output is integrable and its
coefficient is bounded.

For any `N>0`, choose the positive-probability event
`E_N^+={Z2_a in J, M_a>N}` and set
`v_N^+=1_(E_N^+)/sqrt(P(E_N^+))`. It is a bounded field of `L2` norm
one. Its bound may depend on `N`, which is permitted. The multiplier
pairing is finite and exceeds `N`, giving

    D^2 g[U_N^+,U_N^+] >= d_a^2 N/2 - Ctop.

Use `E_N^-={Z2_a in J, M_a<-N}` for the opposite inequality

    D^2 g[U_N^-,U_N^-] <= -d_a^2 N/2 + Ctop.

Thus `D^2 g` has both unbounded signs on these unit raw directions.
These are population directions; no assertion about their realization
or convergence at finite width is needed.

## 14. Full loss, symmetry, and the local physical clock

The permitted symmetry argument is valid in both label modes. For
labels `(1,sigma)`, exchange the sample roots and multiply the readout
by `sigma`. The root law is invariant; backward fields acquire the
same sign, and odd cuts preserve the cut equations. The deterministic
population prediction limits consequently satisfy
`f2=sigma f1`. Global simultaneous label/readout reversal covers the
remaining two sign choices. Cut removal preserves the identity.
Thus at the reached state

    f_b = y_b g,
    f_b-y_b = y_b(g-1).

This is an identity at states on the symmetric trajectory. It is not
assumed on the sample-isolating perturbation line. In fact that line
generally breaks sample symmetry.

Differentiate the actual scalar loss along the line:

    D^2 L[U,U]
       = 2 sum_b (D f_b[U])^2
         + 2 sum_b (f_b-y_b) D^2 f_b[U,U].

Since `g=(1/2)sum_b y_b f_b` as a scalar function of parameters,
`D^2 g=(1/2)sum_b y_b D^2 f_b` for these directions, without imposing
any off-trajectory symmetry. Substitute the base-state residuals to get

    -D^2 L[U,U]
       = 4(1-g) D^2 g[U,U] - 2 sum_b (D f_b[U])^2.

This verifies the sign and factor four in (24). Replacing the loss on
the perturbation line by `2(1-g)^2` would give an unjustified derivative
calculation; the candidate instead retains the correct sum of squared
individual first derivatives.

There is a particularly direct bound for this nonnegative term on the
chosen directions:

    D f_a[U] = d_a E_2[delta2_a v],
    D f_b[U] = 0  for b != a,
    sum_b (D f_b[U])^2 <= d_a^2 ||delta2_a||_2^2.

Hence it is bounded uniformly in `N` even though the indicators defining
the directions have increasing pointwise bounds. As `1-g>1/2`, the
positive and negative sequences of `D^2 g` give, respectively, negative
and positive unbounded sequences of `D^2 L`.

The scalar predictors have continuous raw Hilbert gradients by the
permitted top-down scalar remainder argument. Its fixed old backward
coefficients belong to `L2`; truncating each coefficient first proves
the small scalar remainder, and adjunction identifies the gradient.
This assertion is consistent with the failure of unrestricted Frechet
differentiability of the activation map from `L2` to `L2`.

If the raw loss gradient were Lipschitz in a neighborhood of the reached
state with constant `L0`, every fixed unit direction above would satisfy

    |<grad L(theta+hU)-grad L(theta), U>/h| <= L0

for sufficiently small nonzero `h`. The ordinary second derivative
proved in Section 13 is the limit of this expression. The unbounded
directional values contradict that bound. Indeed a bound on gradient
differences just from this base state would already lead to the same
contradiction. The conclusion concerns the gradient of the scalar loss,
not merely an isolated term in a formal Hessian.

Finally, along the symmetric feature trajectory,

    grad L = 2 sum_b (f_b-y_b) grad f_b
           = 4(g-1) grad g.

Thus `ds/dt=4(1-g)` is the correct local physical clock for the
sum-of-two-squares loss. On the chosen interval, `2<4(1-g)<6`, so

    S/6 <= t(S) = integral_0^S [4(1-g(u))]^(-1) du <= S/2.

In particular the observation time is deterministic and positive.
Only this local time change is needed. There is no exact finite-width
samplewise clock being inferred and no global opposite-label continuation.

Local restart uniqueness remains compatible with the non-Lipschitz
gradient. The imported proof obtains uniqueness by comparison with
bounded cut references and Gaussian tails; it does not invoke a locally
Lipschitz uncut vector field on arbitrary raw `L2` neighborhoods.

## 15. Required versus optional corrections

### R1 — required minor correction to the standalone Gaussian lemma

Location: candidate lines 178–182, Section 3, statement preceding (9).

Replace

> if a continuous finite-dimensional Gaussian process G on [0,S] starts
> at zero and has increment standard deviation at most D|t-u|

by

> if a centered continuous finite-dimensional Gaussian process G on
> [0,S] starts at zero and has increment standard deviation at most D|t-u|

Reason: take `G(t)=A t+t Z` with `Z~N(0,1)`. It starts at zero and has
increment standard deviation `|t-u|`, so `D=1`, but

    (E sup_(t<=S)|G(t)|^2)^(1/2) = S sqrt(A^2+1).

No universal `C` in (9) controls this for arbitrary `A`. This is a
counterexample to the literal auxiliary statement, not to the candidate's
local theorem. Its `zeta` source and projected residual `G` are centered
at every use. Inserting that existing hypothesis resolves the issue
without any new argument or weakened conclusion.

### Optional clarifications — no new mathematical obligation

1. **Separate cutoff and threshold notation.** Use `Kcap` for the smooth
   cuts and retain `R` for the desired tail level. The current proof is
   cap-uniform and its intended quantifiers are recoverable, but using
   the same letter invites an incorrect diagonal-limit interpretation.

2. **Display the line parameter in the Taylor cross bound.** At lines
   373–375, use the explicit `O(|h| ||u||_2 ||r_h||_2+||r_h||_2^2)`
   bound from Section 13 of this report. One may instead give the direct
   derivative-of-first-derivative calculation there. This makes clear
   that the result is an ordinary scalar second directional derivative
   and needs no `L4` bound on the propagated direction. The required
   stronger estimate follows directly from the existing assumptions.

3. **Make the base-state use of symmetry explicit.** Add that `f_b=y_b g`
   is used only for the residual coefficients at the reached state when
   deriving (24), not as an identity on the perturbation line. The
   candidate's formula is already correct.

4. **Clarify the meaning of “bounded directions.”** Each indicator
   direction belongs to `L-infinity`, but there is no common
   `L-infinity` bound over the sequence of unit raw directions. The
   candidate's construction already has exactly this meaning.

5. **Clarify time regularity and constants.** At lines 72–73, say that
   `s -> theta(s)` is a `C1` curve in the raw affine Hilbert state space,
   rather than wording that could be read as `C1` dependence of the
   uncut vector field on the state. Constants in (5) may depend on the
   fixed time, interval, correlation, label configuration, sample, and
   sign. Finite minima/maxima can make them common to the two samples
   and two signs if desired; no uniformity as `S -> 0` is proved.

6. **Use almost-sure conditional language where desired.** “Any value
   of F” means any value in the regression support, or almost every
   conditioning value for a regular conditional probability. The
   deterministic bounds are stronger than needed and are uniform on
   that support, so no measurable-selection or singular-support gap
   results from the existing wording.

No additional correction to the advertised theorem, raw metric, factors
in (21)–(24), limit order, or endpoint range is required by this audit.

## 16. Calibrated scope of acceptance

The accepted implication is:

    permitted local Gaussian-program / common-operator premises
      -> for every sufficiently small fixed positive feature time,
         Gaussian lower tails of the actual middle query while the
         middle preactivation lies in any fixed nondegenerate interval
      -> two-sided essentially unbounded middle curvature multiplier
         on a fixed interval of nonzero activation curvature
      -> unbounded positive and negative full-loss second directional
         derivatives on unit bounded rank-one raw directions
      -> failure of a locally Lipschitz raw loss gradient at that state.

This does not assert independence of trained neurons or of evolved
preactivation/query pairs, a common almost-sure statement over all times,
exact Gaussian tail asymptotics, a bounded Hessian operator, or any
finite-width Hessian divergence theorem. It does not contradict the
permitted local existence/restart argument. It supplies no global
opposite-label estimate and does not resolve or refute the global target.

The audit supports this modular theorem, with the minor centering
correction R1, at the exact candidate hash recorded above.
