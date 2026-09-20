# C-X3 substantial training: reached estimates and the tail bottleneck

Frozen first-round scoped route, 2026-09-20. This is an author derivation,
not an independent review, an accepted substantial-training theorem, or a
promotion. No code, numerical experiment, or Git operation was performed.

**Conclusion.** At every separately fixed depth, bounded tanh gives global
raw-Euler bounds on every prescribed finite physical horizon, independently
of any response cap. Exponential RMS cutoff tails, weaker than Gaussian
tails, suffice for the entire raw comparison and hierarchy argument on any
such horizon. The exact sufficient condition furnished by the cutoff
argument is an Osgood integral; an integrable bound on the absolute response
rows is one further useful weakening of a uniform cap. Neither the maintained
C.2 proof nor raw energy proves that response bound at depth three through
the fitting horizon. Chronological subdivision does not remove this missing
source estimate.

## 1. Scope, inputs, and notation

The target is CONTRACT section 4 at L=3, with the identical target at every
separately fixed finite L if a depth induction closes. The model, Gaussian
initialization, unhalved probability-weighted squared loss, physical time,
both orientations of every initialized action, and full-row/HS metric are
unchanged. The present route concerns the upstream continuation/source
estimate, not a new architecture, optimizer, closure, or training law.

Complete allowed inputs read:

- CONTRACT.md;
- CH3_LOCAL_PROOF.md, all 777 lines;
- CH3_HIERARCHY_PROOF.md, all 738 lines;
- docs/NOTATION.md;
- docs/global_nonlinear.md, C.1--C.2, lines 2454--3440;
- docs/global_nonlinear.md, assigned C-H4 D.2--D.3 range, lines
  14300--15528, including its intervening explicit radius construction.

The solve-math-rigorously and investigate-conjectures skills were read and
applied, including the latter's research-contract and adversarial-audit
references. No other study, first-round route report, historical source, or
external theorem is an input. The parent requested this scoped assignment;
ordinary author startup reading was therefore not performed.

Write phi=tanh and G=phi'. On population ell,

    H1(u)=phi(w.u), Z1(u)=w.u,
    Zell(u)=Aell H(ell-1)(u), Hell(u)=phi(Zell(u)),
    PL(u)=c, Pell(u)=A(ell+1)* Delta(ell+1)(u),
    Deltaell(u)=G(Zell(u)) Pell(u).

Each Aell=Aell,0+Kell and its actual adjoint retain the same edge identity;
only Kell is Hilbert--Schmidt. The raw sum distance e is the sum of the
full-row L2 distance, all increment HS distances, and the readout L2
distance. Its squared Hilbert counterpart is the metric in CONTRACT.
For a scalar field V put tau_R(V)=||V 1_(|V|>R)||2.

The established local candidate supplies the exact one-reference mechanism:
on a common raw/action ball,

    ||F_mu(theta)-F_nu(theta_bar)||sum
      <= C(1+R)(e+W1(mu,nu))
         +C sum_ell integral tau_R(Pell_bar(v)) dnu(v,y),   (1)

for every R>=1. Only the barred reference needs tails. Below we make the
finite-horizon bounds and consequences of (1) explicit; we do not replace
its tail term by an unsupported function of e.

## 2. Global raw bounds for every original Euler program

Fix any T<infinity and any positive time steps whose total length is at
most T. Train any probability law with |y|<=1 on normalized inputs. Let
the initial action norms be at most m0, the initial directional row norm at
most w0, and the initial readout satisfy ||c0||infinity<=c0cap. The
population initialization has m0=10, w0=1, c0cap=0. All following estimates
hold before any Gaussian response or tail assertion.

Define the finite constants, in the indicated downward order,

    Cc=(1+c0cap) exp(2T)-1,       Cr=Cc+1,
    M_L=m0+2T Cr Cc,
    M_ell=m0+2T Cr Cc product_(j=ell+1)^L M_j,
                                      ell=L-1,...,2,
    Dw=2T Cr Cc product_(j=2)^L M_j.                     (2)

An empty product is one. At every node, and every recomputed affine raw
interpolation time,

    ||c||infinity<=Cc,       |r(u,y)|<=Cr,
    ||Aell||op<=M_ell,
    ||Kell||HS<=M_ell-m0,
    ||w-g||2<=Dw,           ||w||dir<=w0+Dw,
    ||Hell(u)||2<=1,
    ||Deltaell(u)||2, ||Pell(u)||2
        <=Cc product_(j=ell+1)^L M_j.                   (3)

The final bound for Pell is valid because |G|<=1; at ell=L it is the
readout bound. The full-row bound is ||w||2<=||g||2+Dw, not a replacement
of the full row by its training projections.

Here is the proof, including the absence of a depth feedback loop in (2).
If C_k=||c_k||infinity, bounded hidden outputs give |f_k|<=C_k and

    C_(k+1)+1 <=(1+2h_k)(C_k+1).

Multiplication and 1+x<=exp(x) yield C_k<=Cc. Consequently every residual
is bounded by Cr. At the top hidden edge,

    ||K_L,k+1-K_L,k||HS
       <=2h_k Cr ||Delta_L,k||2 ||H_(L-1),k||2
       <=2h_k Cr Cc.

Summing proves the M_L bound. If the action bounds above edge ell are
known, downward backpropagation gives

    ||Deltaell,k||2<=Cc product_(j=ell+1)^L M_j,

and the rank identity ||a tensor b||HS=||a||2 ||b||2 gives the next line
of (2). This induction uses only actions strictly above the edge being
bounded. Finally the full-row increment has norm at most
2h_k Cr ||Delta1,k||2, because |u|=1 and the data law has mass one.
Summation proves Dw. No smallest mass, source rank, or sample-count
constant enters. An affine interpolation time is the same prefix with
one shortened last Euler step, proving the interpolation assertion.

The proof is identical for normalized finite arrays: the rank matrix is
a b^T/n and its ordinary Frobenius norm is
(||a||2/sqrt(n))(||b||2/sqrt(n)). The row/readout metrics have the
corresponding RMS factors. Thus (2)--(3) are also global bounds for the
actual simultaneous raw-GD algorithm, rather than for a modified update.
They may be extremely large as T or L increases; they are finite and
independent of width and number of elapsed steps.

For the prescribed stored finite readout, with independent entries
N(0,n^-2),

    P(||c_n(0)||infinity>1)<=2n exp(-n^2/2) ->0.          (4)

The initialized action norms are <=10 with probability tending to one,
by the norm bound already used in CH3_LOCAL_PROOF. For fixed d the first
directional row norm is <=2 with probability tending to one. Therefore
the same deterministic constants with c0cap=1, w0=2 control actual GD
with probability tending to one. If its final full update passes T, use
T+1 once its step is <=1. The random readout itself is retained exactly;
the event (4) is only a bound on it.

For an already constructed strong population solution, energy gives the
better bounds

    loss(t)+integral_0^t ||theta'(s)||raw^2 ds=loss(0)<=1,
    ||theta(t)-theta(0)||raw<=sqrt(t),
    ||c(t)||infinity<=2t.                               (5)

It also gives ||theta(t)-theta(s)||raw<=sqrt(t-s), hence a raw endpoint
at any finite endpoint of its existence interval. These facts do not
construct a continuation from that endpoint: the vector field is continuous
but is not known to be locally Lipschitz on arbitrary raw L2 states.
The global Euler bound (2) is useful precisely because it does not assume
the desired strong solution or its energy identity first.

## 3. An explicit finite-horizon comparison constant

Choose B>=2 dominating the action norms, readout L2 norm, residual
absolute bound, directional row norm, and one for both paths. Constants
from (2)--(3) supply such a B uniformly over all Euler programs being
compared. Let

    F=(B+1)^L,
    C=100(L+1)^2 (B+1)^(2L+3).                          (6)

This C is one permissible, deliberately loose constant in (1).
To check the depth and cutoff dependence, couple (u,y) with (v,z), set
h=|u-v| and l=|y-z|, and let p_ell=||Zell(u)-Zell_bar(v)||2.
Successive factor subtraction gives

    p_1<=e+Bh,
    p_ell<=e+B p_(ell-1)<=F(e+h),
    |r-r_bar|<=(B+1)F(e+h+l).                           (7)

All reference deltas have L2 norm <=B^L. At a gate, |G|<=1 and
Lip(G)<=2 give exactly

    ||[G(Z)-G(Z_bar)]P_bar||2
       <=2R||Z-Z_bar||2+2 tau_R(P_bar).                 (8)

Let d_ell be the delta difference. The top and lower recurrences are

    d_L<=e+2R p_L+2tau_R(c_bar),
    d_ell<=B d_(ell+1)+B^L e+2R p_ell+2tau_R(Pell_bar).

Since each B^j<=F for 0<=j<=L, these imply

    d_ell<=4L F^2(1+R)(e+h)
                  +2F sum_(j=ell)^L tau_R(Pj_bar).     (9)

In every velocity block subtract the residual, then the delta, then its
bounded hidden factor; the row block also subtracts the unit input.
Use the HS rank-difference identity for each edge. The coefficients of
(1+R)(e+h+l) are bounded by sums of

    B^L(B+1)F,  4BLF^2,  B^(L+1)F,  (2B+1)F.

There are L+1 blocks and the outside factor is two. The constant in (6)
dominates their sum and the tail coefficients. Integrate over the coupling
and minimize its cost to prove (1). In particular there is one cutoff
factor R at all fixed depths, not R^(L-1).

The same derivation permits a projection or velocity defect bounded by
delta and an input-law discrepancy q. After increasing delta by a fixed
known factor if needed, the comparison has the general form

    D^+ e(t)<=C[(1+R)(e(t)+delta)+tau(t,R)], R>=1,        (10)

where delta is constant over the comparison interval and includes the
data-law, mesh, projection, or uniform velocity-defect source. Initial
error is kept as e(0), not set to zero at later times. Equation (10)
also holds for the norm of the difference of strong curves almost
everywhere, including its upper-derivative interpretation at zero.

## 4. Exact Osgood criterion for the cutoff information

Suppose first that tau(t,R)<=tau(R), where tau is nonnegative,
nonincreasing, and tends to zero. Define the scalar modulus

    omega(s)=inf_(R>=1) [(1+R)s+tau(R)],  s>=0.           (11)

It is finite, nondecreasing and concave, since it is the infimum of
positive-slope affine functions. It satisfies omega(0)=0, omega(s)>=2s,
and is continuous for s>0. It is continuous at zero: choose R with small
tau(R), then let s decrease at that fixed R.

Set u=e+delta. Taking the infimum in (10) gives u'<=C omega(u) almost
everywhere. For a fixed b>0 define

    I(x)=integral_x^b ds/omega(s),  0<x<=b.              (12)

If

    integral_(0+) ds/omega(s)=infinity,                 (13)

then, until the first exit above b,

    I(u(t))>=I(u(0))-Ct.                               (14)

Indeed the derivative of I(u) is -u'/omega(u)>=-C; if u reaches zero,
apply the same argument to u+epsilon and then let epsilon decrease.
The inverse of the decreasing function I therefore bounds u(t) by a
quantity tending to zero uniformly on each finite horizon as u(0)->0.
For sufficiently small initial source this bound itself excludes exit
above b. It proves uniqueness, continuous dependence and vanishing-error
convergence on every finite horizon permitted by the tail hypothesis.

This criterion is sharp for conclusions based only on (10). If (13)
fails, the inverse of

    x -> integral_0^x ds/[C omega(s)]

defines a nonzero solution of u'=C omega(u) issuing from zero; adjoining
an arbitrary initial zero interval gives delayed solutions. Every one
obeys u'<=C[(1+R)u+tau(R)] for every R. Thus those inequalities alone
cannot force zero error. This is not a counterexample to neural-flow
uniqueness; it identifies the exact logical strength of the cutoff method.

For the envelope tau(R)=M exp(-a R^beta), a,M,beta>0, one has, for small s,

    omega(s) comparable to s [log(M/s)]^(1/beta).        (15)

For the upper bound choose R=[2log(M/s)/a]^(1/beta), enlarged to one;
the tail term is s^2/M. For the lower bound divide at
R0=[log(M/s)/(2a)]^(1/beta). Above R0 the linear term is >=sR0;
below it the tail is >=sqrt(Ms), which exceeds sR0 for sufficiently
small s. Substitution z=log(M/s) in (13) now proves that (13) holds
exactly when beta>=1. Gaussian tails are more than necessary. Exponential
tails are the threshold within this stretched-exponential family.

The exact criterion (13) also admits some slower tails. For example
tau(R)=exp[-a R/log(e+R)] gives a modulus comparable, near zero, to

    s log(1/s) log log(1/s),

and its reciprocal still has divergent integral. To verify the comparison,
the inverse of R/log(e+R) at a large value z lies between fixed positive
multiples of z log z: substitution gives log(e+z log z) between
log z and 2log z for all sufficiently large z. Apply the two-cutoff
argument used for (15). Replacing that logarithmic denominator by
[log(e+R)]^(1+epsilon), epsilon>0, gives a finite Osgood integral.
These examples describe the envelope criterion, not established reached
tails of the neural system.

## 5. Exponential tails: explicit modulus and actual slab patching

Assume tau(t,R)<=M exp(-aR) with a>0, M>=1. For 0<u<=1 take

    R=1+a^(-1)log(M/u).

Then tau<=exp(-a)u and (10) yields

    u' <=(C/a)u log(H/u),       H=M exp(3a).             (16)

The constant 3a bounds the two linear cutoff terms and exp(-a).
Writing y=log(H/u), one obtains y'>=-(C/a)y and hence

    u(t)<=H [u(s)/H]^(exp[-C(t-s)/a]).                  (17)

The assertion is valid while u<=1. Requiring its right side at T to be
less than one closes that condition by first exit. For any desired
0<epsilon<1, the completely explicit sufficient source condition is

    e(0)+delta <= H (epsilon/H)^(exp(CT/a)).             (18)

Thus the modulus remains positive at every finite T, despite its
deterioration with the horizon. For source sequences tending to zero,
condition (18) eventually holds for each fixed epsilon.

The chronological-slab version is also valid and needs no error reset.
Choose a finite partition with each length h<a/(2C). On a single slab,
fixed-cutoff Gronwall gives

    sup e <= exp[C(1+R)h] e_left
       +Ch exp[C(1+R)h][(1+R)delta+M exp(-aR)].          (19)

For a convergent sequence, first take its limit at fixed R, using the
already proved e_left->0; then send R->infinity. The remaining tail
factor decays because Ch<a. This proves vanishing error on the slab.
Induction over the finitely many slabs proves it on [0,T]. Each approximate
trajectory continues its own state, and its actual endpoint error enters
the first term of the next application of (19). No intermediate target
state is an input. Formula (17) is a quantitative version of this argument.

This patching result propagates **comparison convergence under the stated
tail bound**. It does not propagate the tail bound itself.

## 6. Time-integrated source control is sufficient

There is a useful relaxation of a uniform exponential prefactor. Suppose

    tau(t,R)<=M(t) exp(-aR),    a>0, M(t)>=1,
    integral_0^T log M(t) dt <=B_M<infinity.             (20)

The envelope may depend on the Euler program provided the displayed
integral bound is uniform. Taking
R=1+a^(-1)log(M(t)/u(t)) in (10) gives, for u<=1,

    u'<=A u log(1/u)+b(t)u,
    A=C/a,       b(t)=(C/a)log M(t)+3C.

For y=log(1/u), multiply y'>=-Ay-b(t) by exp(At) and integrate:

    u(t)<=exp[integral_0^t exp(-A(t-s))b(s)ds]
                      u(0)^(exp(-At))
         <=exp[(C/a)B_M+3CT] u(0)^(exp(-CT/a)).          (21)

The last bound supplies the same first-exit argument and finite-horizon
convergence. All integrals and exponents in this assertion are ordinary
deterministic numbers, not maxima of random source histories.

To connect (20) with the Gaussian-source calculus, suppose the exact
Euler representation on every edge has, at time t, the backward response
row bound

    sum_(b,s<=k) |A_response^(ell)_(ak,bs)| <=Bresp(t),   (22)

uniformly over passive outputs and program resolutions. Here the source
coefficients include the variance factor, which is one for the contract.
The source RMS bounds (3) give a common finite S, and the learned
coefficients have total absolute row sum <=J T, where

    J=2 Cr S^2.

The exact C.2 representation is therefore

    Pell(t,u)=eta(t,u)+Jell(t,u),
    Var(eta(t,u))<=S^2,
    |Jell(t,u)|<=D(t):=Bresp(t)+JT,  ell<L.             (23)

The last bound uses |H|<=1. No independence between eta and Jell is
needed to deduce tails from this representation. Set sigma=1+S and
a=1/(32 sigma^2). Gaussian integration gives, for R>=2D(t),

    tau_R(Pell)<=4(sigma+D(t)) exp[-R^2/(32 sigma^2)].   (24)

For completeness, the event is contained in
|eta|>R-D(t)>=R/2. For a standard normal Z, the inequalities
1_(|Z|>b)<=exp[(Z^2-b^2)/4],
E exp(Z^2/4)=sqrt(2), and
E Z^2 exp(Z^2/4)=2sqrt(2)
bound the squared tail of (sigma|Z|+D(t)); taking a square root gives
(24) with the displayed loose constant. The readout tail vanishes
above Cc.

With R0(t)=max(1,2D(t),Cc), a permissible aggregate exponential envelope is

    M(t)=4L(1+sigma+D(t)+Cc) exp[a R0(t)].               (25)

For R>=R0, use R^2>=R in (24). For 1<=R<R0, the ordinary L2 bound
sigma+D(t)+Cc is dominated by M(t)exp(-aR). The sum over all layers
is included in (25). Since log(1+D)<=D and
R0<=1+2D+Cc, the explicit choice

    K=log[4L(1+sigma+Cc)]+a(1+Cc)+(1+2a)JT

gives

    log M(t)<=K+(1+2a)Bresp(t).                         (26)

Consequently the weaker reached estimate

    sup_(admitted Euler programs)
       integral_0^T Bresp(t) dt <infinity               (27)

is enough for the entire Osgood comparison/completion argument. A uniform
source-row cap implies (27), but is not required by this argument.
The normalized single-pulse C coefficients remain relevant for *proving*
(22) or (27); they are not themselves an additional term in the raw
stability estimate.

Neither (22) nor (27) is established here through the depth-three fitting
horizon. On the CH3 onset interval, C.2 proves a uniform cap, so all these
weakened criteria do hold there at L=3 and every fixed L.

## 7. What follows if the reached tail criterion is supplied

Suppose a training-law class admits finite-law approximations inside the
same class and its original, unreset Euler programs satisfy either the
uniform Osgood envelope (11)--(13) or the uniform integrated envelope (20)
on [0,T]. The following are consequences, rather than extra assumptions.

First compare two such Euler paths on the common initialized carrier.
Their preceding nodes differ from their interpolants by a constant times
their maximal mesh size, because (3) bounds every raw velocity. Apply
(10) with delta equal to the two mesh sizes and the law distance. Equations
(14) or (21) make them Cauchy in C([0,T];raw space). HS completeness and
the bounded-multiplier continuity argument in CH3_LOCAL_PROOF pass the
integral equations to a strong solution. The pointwise cutoff tail passage
uses the Lipschitz map V -> (|V|-R)_+ and

    tau_(2R)(V)<=2||(|V|-R)_+||2.

Uniform tails pass immediately in the uniform-envelope case. For uniqueness
in the time-integrated case, comparison against the approximating reference
Euler paths already suffices: let their mesh and state error decrease in
(21), whose integrated bound is uniform. Thus no unjustified pointwise
limit of the functions M(t) is needed. The same comparison gives law
continuity, uniqueness against any bounded strong raw competitor, and
same-law reached-state restart. A competing continuous strong path on a
compact interval is bounded, so it supplies the other comparison ball.

One can also obtain a target envelope explicitly. For an approximating
sequence j define the soft tail

    S_(j,r)(t)=sum_ell integral
        ||(|P_(ell,j)(t,u)|-r)_+||2 dmu_j(u,y), r>=1.

Define S_r(t) with the limiting fields and law. Strong raw convergence,
bounded-multiplier continuity and compactness of the time/input domain
give uniform L2 convergence of each backward field over that domain.
To verify this uniformity, a contrary sequence (t_j,u_j) has a convergent
subsequence; use raw convergence at t_j and joint state/input continuity
at its limit. The positive-part map is 1-Lipschitz, so the soft tail
functions converge uniformly in (t,u) at each fixed r. The limiting
function of input is continuous, hence its integrals against mu_j converge
to its integral against mu. A finite time net gives the uniform-time
version if desired. Therefore S_(j,r)(t)->S_r(t) for every t,r.

If the hypotheses are uniform in passive input, replace the integral in
this definition by sup_u, separately for each ell. The same uniform field
convergence proves convergence of these suprema. In that variant assume
the corresponding sum of passive tail suprema is bounded by
M_j(t)exp(-ar); the row certificate (22)--(25) supplies precisely this.
The integrated-law version is sufficient for fixed-law state stability;
the passive version additionally supplies the law-uniform comparison.

Set

    M_*(t)=max(1,sup_(r rational,r>=1) exp(ar) S_r(t)).

This is measurable. For every finite rational cutoff set its maximum is
the limit of the corresponding proxy maxima, each bounded by M_j(t).
Increase the finite set to all rational cutoffs to obtain

    M_*(t)<=liminf_j M_j(t),
    integral_0^T log M_*(t)dt <=liminf_j integral_0^T log M_j(t)dt
                             <=B_M.                    (27a)

The integral inequality is Fatou applied to the nonnegative functions
log M_j. Countably many cutoff exceptional sets can be removed once.
Continuity in r extends the soft-envelope bound from rational to all
r>=1. Let S0 be a common bound on the sum of ordinary L2 norms in the
same integrated or passive sense, supplied by (3). For R>=2,
tau_R(target)<=2 S_(R/2)(t), while for 1<=R<2 the tail is <=S0.
Consequently a target envelope valid almost everywhere in t is

    tau_R(target)<=M_target(t) exp[-(a/2)R],
    M_target(t)=(2+S0) exp(a) M_*(t),
    integral_0^T log M_target(t)dt
       <=B_M+T[a+log(2+S0)].                           (27b)

Thus program-dependent integrated certificates pass to the actual strong
target with explicit constants, without postulating convergence of the
source coefficients or their envelopes. The almost-everywhere envelope
is sufficient for all integral comparison arguments.

Second, the fixed-program finite-network bridge extends without changing
the Gaussian matrix identities or the limit order. Fix one finite reference
law, one sufficiently fine finite proof mesh and one cutoff before taking
width to infinity. Its finite-program Gaussian identification, actual-rank
proxy, and additive retained finite readout are exactly those of
CH3_LOCAL_PROOF section 8. The only previous local ingredients in the
raw-GD/proxy comparison were a common raw bound and the reference tail
estimate. The first is now (2)--(4), and the second is the stipulated
finite-horizon source result. For a fixed mesh, empirical cutoff moments
converge; hence all finite sums in the integrated version converge too.
Then refine the proof mesh/law and remove the cutoff, using the uniform
Osgood or integrated estimate.

One detail matters in the integrated case: no empirical exponential bound
uniform in an n-dependent cutoff has been asserted. At a fixed reference
mesh, the scalar actual-to-proxy distances are uniformly bounded and
uniformly Lipschitz by (3). From any proposed failing subsequence take a
uniformly convergent scalar subsequence, and simultaneously pass the
finitely many empirical reference cutoff moments for each integer cutoff.
The limit distance obeys the integral comparison at every such fixed
cutoff. All integer cutoffs can be retained by a diagonal subsequence;
the moment convergence in probability can first be made almost sure on
that subsequence. Passing the same integrated inequality on rational
subintervals gives the almost-everywhere differential bound for all
integer cutoffs. Rounding the optimizing R in section 6 upward to the next integer
adds at most C u, absorbed by replacing 3C with 4C. Apply (21) to this
limiting scalar inequality, and only then refine the reference mesh. This
proves the probability statement using fixed-program cutoff convergence,
rather than assuming finite-width exponential tails.

In particular, this conditional bridge needs only

    eta_n ->0                                                   (28)

for the actual raw GD. There is no width-dependent restriction merely to
keep actual GD in a bounded raw ball. The fixed graph is still fixed before
the width limit; nothing applies a finite-program theorem to a transcript
growing with width. Finite GF uses its energy bound in place of the Euler
bound. Whole-input predictions, paired initial/current laws and the admitted
same-layer observations follow from the same compact-reference observation
argument as in CH3_LOCAL_PROOF. This is a conditional extension of that
bridge, not an unconditional long-horizon capture theorem.

Third, CH3_HIERARCHY_PROOF section 5 supplies its vanishing projection
source epsilon_N and its order-uniform raw/action bounds. Replace its
Gaussian-tail Gronwall conclusion by (14), (17), or (21). Its closures
converge through T while evolving their own states throughout. No tail
assumption on the projected trajectories is introduced. All fixed-order
inner numerical limits remain the already specified limits; the new
bottleneck is the source estimate for the common target.

If only the integrated Euler certificate is available, compare the closure
first against an exact reference Euler path of fixed mesh h. Strong filter
convergence is uniform on that fixed path's compact field sets, and its
finitely many rank velocities give a projection source epsilon_(N,h)->0
as N->infinity. The preceding-node error is O(h), so (21) bounds the
closure-to-reference error by a common constant times
(h+epsilon_(N,h))^(exp(-CT/a)). First let N increase at fixed h and then
let h decrease. The reference Euler path already converges strongly to
the target. This proves order convergence without an unjustified claim
that a pointwise response-row envelope passes to the target.

For scale, if a uniform exponential certificate with computable a,M and
the reference fitting bound loss_*(T)<=1/8 were supplied, (17) would give
an explicit positive law radius with fitting slack. On the common B ball
let P=(B+1)^(L+1). Forward and input subtraction give

    |loss_mu(T)-loss_*(T)|
       <=2(B+1)P [e(T)+W1(mu,nu_*)].                    (29)

For a support radius rho around the matching axes, the same-label coupling
has W1<=rho. Let epsilon_fit=[32(B+1)P]^(-1). It is enough to choose

    rho <=H (epsilon_fit/H)^(exp(CT/a)).                 (30)

Then (29) costs at most 1/16, giving loss_mu(T)<=3/16<1/4. This is a
finite expression once the certificate constants are known. It is not
presently an unconditional supported radius: existence and source control
for the nearby laws must still be proved. Raw closeness to the reference
alone does not provide that missing fact.

## 8. Why C.2 does not itself extend by chronological slabs

C.2 uses the original independent Gaussian actions and roots, and bounds
the expected derivatives with respect to all the named source slots of
the original program. At a reached time s>0, w(s), c(s), and K(s) depend
on those same initialized matrices. Their law is not another independent
Gaussian initialization. Their marginal tail bounds do not specify their
derivatives in the old slots. Consequently C.2 cannot be invoked afresh
from that current state under its literal initialization hypotheses.

A correct slab proof would continue the original source representation.
For old slots it must propagate nonzero inherited derivative rows; it must
also bound the new source pulses. These derivative quantities may be
proof certificates without being retained numerical state, so the need to
bound them does not conflict with the desired autonomous closure. But
they are extra estimates, not consequences of autonomy.

Even the literal cap inequalities expose the limitation of simply choosing
larger caps on a larger interval. Write C>=1 for the fixed constant in
C.2 equations (28),(32), f2=c2+J, d1=1+a2, and d2>=1. Demanding that the
respective displayed upper bounds be below the proposed caps implies

    a2>=C exp(C T c2),
    c2>=C exp(C T a2).                                  (31)

For a2, discard the other positive exponent terms and use f2>=c2 and
d2>=1. For c2 use f1=1 and d1>=a2. Let b=(a2+c2)/2. Convexity of exp
in (31) gives

    b>=C exp(C T b).

Since the maximum of b exp(-CTb) over b>=0 is 1/(eCT), this sufficient
cap system has no solution when

    T>1/(e C^2).                                       (32)

This does not prove the actual response blows up. It proves that those
particular bounds cannot be globalized merely by increasing their caps.
The obstruction already applies to the generic two-layer C.2 estimates,
although the maintained C-H4 uses additional reference/source structure
to obtain its much longer result.

Chronological shortening replaces T by a short increment in new growth
terms but introduces inherited response prefactors. To obtain arbitrary
finite continuation one must prove that the resulting allowable slab
lengths have a divergent sum, or prove a direct integrated estimate such
as (27). Existence of a positive continuation length at each finite cap
does not imply this: a scalar majorant x'=x^2 has positive local existence
at every finite x but a finite explosion time. For example, cap doubling
M_j=2^j M0 with admissible increments proportional to 1/M_j yields a finite
total time. This is an illustration of the missing nonexplosion inference,
not a derived Riccati equation for the neural response.

At L=3 the specific problematic field is

    Delta2=G(Z2) A3* [c G(Z3)].                          (33)

The bounded readout controls the top operand. The A3* response produces
an unbounded P2, and its product with the changing intermediate gate
introduces the |P2| term in both forward-row and lower-pulse derivative
estimates. The response feedback through the distinct second edge must
be retained. Treating this as a fresh Gaussian answer, or using the
two-layer bound with an invented bounded intermediate readout, would
change the problem.

## 9. Raw norm or small raw error cannot replace a reached-tail proof

Here is a precise nearby-state obstruction, at the actual L=3 edge types.
It is an obstruction to an inference about arbitrary raw states, not a
claim that such a perturbation is reached by training.

Take a source-good raw state and a finite collection of active inputs
u_1,...,u_m. Suppose d=Delta3(u_1) is nonzero. Since the readout is bounded,
d is bounded. Let V be the span of the bounded fields H2(u_a) in population
2. The canonical population contains a nondegenerate initial forward
Gaussian coordinate X, from A2,0 tanh(g.u_1). After dividing by its
positive standard deviation, X is standard normal. The generated L2
space contains Q=exp(X^2/8), by bounded truncation and density. It obeys

    E Q^2=E exp(X^2/4)<infinity,
    E Q^4=E exp(X^2/2)=infinity.

Subtract its orthogonal projection on V and normalize:

    q=(Q-Proj_V Q)/||Q-Proj_V Q||2.

The projection is a finite linear combination of bounded H2 fields and
is therefore bounded. Thus the denominator is positive, q lies in L2,
q is orthogonal to every active H2, and q is not in L4. This uses no
inverse input Gram; the finite-dimensional Hilbert projection exists
also when the listed fields are linearly dependent.

Perturb only the learned top edge by the HS rank

    delta K3=epsilon (d/||d||2) tensor q.                 (34)

Its HS norm is epsilon. At every active input, delta K3 H2(u_a)=0, so
all forward fields, predictions, readout values and risks stay exactly
the same. At u_1 the top delta also stays the same, whereas

    P2_new(u_1)=P2_old(u_1)+epsilon ||d||2 q.             (35)

The old source-good P2 has finite L4 norm; q does not. If the new P2
were in L4, subtraction in (35) would put q in L4, a contradiction.
In particular the new P2 has no exponential RMS-tail bound. Its action
norm changes by at most epsilon, and the readout remains bounded.

This verifies, with the correct action and actual adjoint of the same
rank perturbation, that bounded actions, bounded readout, and arbitrarily
small raw error do not imply even finite fourth moment of P2. Matching
the forward predictions and risk does not repair the inference. The
example is deliberately outside the reached-state claim. The required
theorem must exclude it using the chronological neural dynamics, rather
than silently asserting a property of the entire raw ball.

## 10. Frozen claim status and the remaining proof obligation

| Claim | First-round status | Exact support or limitation |
|---|---|---|
| Global raw Euler bounds at every fixed L,T | Proved | Downward triangular recursion (2)--(3) |
| High-probability global raw bounds for actual GD | Proved | Same finite-array calculation and (4) |
| Exact adequate tail criterion for this cutoff method | Proved | Osgood condition (11)--(14), with scalar sharpness |
| Exponential-tail finite-horizon patching with no resets | Proved | (17)--(19) |
| Integrable response-shift envelope suffices | Proved conditionally on (22)/(27) | (20)--(27) |
| Conditional every-vanishing-step GD and hierarchy extension | Proved implication | Section 7, original fixed-program limit order |
| Local criterion at L=3 and every fixed L | Supplied by allowed local source | C.2/CH3 source caps on their onset interval |
| Gaussian or Osgood source control through fitting at L=3 | Open, major | Neither C.2 cap selection nor energy bounds proves it |
| Positive supported fitting neighborhood and full contract | Not established here | Needs reached reference and nearby-law source certificate |
| Finite-time source blowup or falsity of C-X3 | Not established | (32) concerns a proof route; (35) concerns arbitrary states |

The weakest explicit sufficient next target furnished by this route is:
for original, unreset reference Euler programs through a justified fitting
horizon T_fit, prove a resolution-independent bound on the time integral
of the absolute backward response rows (27), or prove a directly adequate
Osgood tail envelope without those rows. Then establish a quantitative
nearby-law source estimate under a temporary cap/envelope, as C-H4 does
at two layers, and close its first-exit argument on a computably positive
supported radius. An existing strong reference curve with raw energy
alone does not discharge either of those source obligations.

No result from another first-round route has been incorporated in this
frozen report.
