# Fresh isolated adversarial audit: positive-time middle curvature

Date: 2026-09-06.

Verdict: **PASS within the explicitly imported local scope. No required
mathematical correction found.** This verdict concerns the local route lemma
in the exact candidate identified below. It does not certify a global
two-label theorem, any excluded part of a dependency, or a finite-width
positive-time Hessian limit.

The lower-tail argument identifies actual limiting Euler sources, controls
the complete reverse source path uniformly in caps and mesh, and makes two
valid scalar Gaussian regressions. Its terminal forward map has a controlled
preimage of the target interval without needing injectivity. Both limit
passages have the correct closed-set inequality. At the reached state, the
rank-one test lines have ordinary scalar second derivatives using only
bounded L2 operator actions. The actual base-state sample symmetry gives the
claimed full-loss identity and the failure of local gradient Lipschitzness.

## 1. Isolation, source identity, and imported scope

I personally read all five mathematical files completely. The candidate has
478 lines, and its measured SHA256 matches the user-specified hash. All four
dependency hashes also match the candidate's Section 1. The complete source
inventory is:

1. `/tmp/l3-two-sample-proof-DLuelg/POSITIVE_TIME_MIDDLE_CURVATURE.md`
   (478 lines), called **C** below.

   SHA256: `9efd5283d35a493982f3a142332536d32a9905eff62cb44ea8793aaf001ea79a`

2. `/tmp/l3-two-sample-proof-DLuelg/TWO_SAMPLE_SHORT_RESPONSE_BOOTSTRAP.md`
   (352 lines), called **B** below.

   SHA256: `9305453f933ad30a0e813e4e97942ee9e00490ce726d70142b25c8f67a475170`

3. `/tmp/l3-two-sample-proof-DLuelg/SECH_LOCAL_JET_AND_SIGN_BRIDGE.md`
   (433 lines), called **J** below.

   SHA256: `65fab11c5892afe517fe4289450f0736bb137bb1a118e85f8ea8541e18a017f8`

4. `/tmp/l3-two-sample-proof-DLuelg/SAME_LABEL_GLOBAL_ASSEMBLY.md`
   (358 lines), called **A** below.

   SHA256: `510fd019c204e0e89e0c6bcb99c031a11de974b05323df1c016c72b263f64a44`

5. `/tmp/l3-standalone-proof-D6AW4s/L3_GLOBAL_SELF_CONTAINED_PROOF.md`
   (1789 lines), called **G** below.

   SHA256: `bebbb70a8f8da8fd2fa5304fc7af08026e72aef73e20f77f046509f87e63954e`

Line references below refer to these exact versions. No history, ledger,
other review, or other research file was opened. References and prior review
verdicts appearing inside the permitted files were not treated as premises.
No experiment, numerical simulation, external mathematical source, candidate
edit, or global theorem assumption was used. Only this review was written.

The dependency boundary is substantive:

- From B: the actual fixed finite two-sample Euler law, its source and
  response identities, both backward response estimates, and the Gaussian
  envelopes on feature time [0,3/2].
- From J: Sections 1-2 only insofar as they transfer that construction to
  the stated activation and supply the local construction, comparison, and
  symmetry. Its static jet enlargement, cubic estimates, and sign-change
  conclusions are unnecessary here and are not imported.
- From A: Sections 1-2 and the scalar-gradient and symmetry arguments in
  Section 3. The same-label lower fitting bound, its global clock, and
  subsequent physical finite-width results are not premises.
- From G: the elementary finite-program proof, common bounded actions and
  adjoints, and elementary limiting tools supporting the preceding local
  constructions. Its one-sample global theorem, transformed first
  coordinate, global clock, and nontriviality conclusions are not premises.

In particular, I did not follow the permitted files' citations to activation
design, initial control jets, exact two-sample reduction, nontriviality
supplements, or reviews. The activation facts and symmetry needed here can
be checked directly from C and the permitted local arguments.

## 2. Required findings versus optional findings

### Required findings

None. I found no false advertised local conclusion, missing essential
independence premise, unjustified uniformity, wrong limit inequality,
unavailable Lp operator action, or loss-normalization error in C.

This is a scoped acceptance of a modular lemma. It is not a claim that C
reproves every imported construction internally. The relevant constructions
are explicitly available in the permitted dependencies and are checked
below. No excluded global conclusion is needed to close the argument.

### Optional clarification O1: name the reverse-source event

C:259-272 constructs the intersection of (12) and (13), which depends only
on the reverse Gaussian source. C:276 and 332 abbreviate this as a reverse
source “satisfying (14).” Display (14) also mentions q, a computed field
that generally depends on the forward source.

For maximal precision one could name the original intersection E_R and
condition on zeta in E_R. On E_R, (14) holds for every forward source, as
C:270-272 explicitly proves. This is a notational clarification, not an
independence gap: the preceding construction already provides exactly the
source-measurable event required by the proof.

### Optional clarification O2: expand the nested approximation quantifiers

C:237-242 is correct. It could state explicitly that for fixed S there is
Q_*(S) such that for every Q >= Q_*(S), there is M_*(Q,S) such that the
variance lower bound holds for every M >= M_*(Q,S). A mesh threshold uniform
in Q is neither provided nor needed. The probability constants, unlike the
mesh threshold, are uniform in both approximation parameters.

### Optional clarification O3: state C2 regularity on each test line

C:389-398 has enough hypotheses for its argument. An explicit sentence that
t maps to phi(Z+d_a t v), and hence its W^(3) image, is C2 into L2 for each
fixed bounded v would make the distinction between an ordinary second
derivative and only a second-order expansion immediate. The verification
in Section 9 below supplies this sentence without adding an assumption.

These optional points do not change the verdict or require a candidate edit.

## 3. Activation, metric, and local construction

For the activation in C,

    phi'(z) = (1/10) sech(z),
    phi''(z) = -(1/10) sech(z) tanh(z).

Thus phi' is strictly positive, bounded by e=1/10, and phi'' is bounded
in absolute value by c=1/5 (a deliberately loose bound). Since
|atan(sinh z)| < pi/2 < 5/3, the bounds m=5/6 < phi < 7/6=a follow.
Differentiating sech(z) times a polynomial in tanh(z) preserves this form,
so every fixed-order derivative needed for the fixed smooth programs is
bounded. No excluded activation-design source is needed.

The finite Frobenius normalization agrees with the population rank-one
action: U tensor V acts by U E[VB], and its finite representative is
UV^T/n. Its Hilbert--Schmidt norm is ||U||_2 ||V||_2. Initial Gaussian
actions are only required to be bounded operators; their learned increments
are Hilbert--Schmidt. These roles must not be interchanged.

For |rho|<1, the first-field metric E[v^T C^(-1)v] makes the first
gradient component C times the pair of scalar first-field derivatives.
This gives exactly the first equation of C:(1). At rho=-1, the admissible
pair is (v,-v), with the induced one-field metric. The same equation
preserves that subspace. No inverse of singular C is used. The other
components of grad g give the factors 1/2 and y_a displayed in C:(1).

The local construction is supported by A:32-183 and J:83-137. Its essential
facts can be checked without the same-label fitting argument:

1. Bounded features and gates first bound the readout, then W^(3), then
   W^(2), then the first-field velocities. Both cuts satisfy |tau_Q(q)| <=
   |q|, so these primal bounds do not grow with Q.
2. Fixed-cut differences use a pointwise bound only on the reference
   readout. For example, the top delta difference is the readout difference
   times the new gate plus the old bounded readout times the gate
   difference. It is bounded in L2 by the state discrepancy.
3. Each separate clipped gate-difference term costs at most a constant
   times Q. The propagated query difference is multiplied by a bounded
   gate, not by Q. Thus two clips give a coefficient C(1+Q), not C Q^2.
4. Picard iteration in the closed path set with |W^(4)(s)| <= as gives
   the cut solution and fixed-Q Euler convergence. This does not assert
   that the uncut field is locally Lipschitz on an open L2 neighborhood.
5. The two reference Gaussian tails give a forcing bounded by
   C exp(-Q^2/256). The asymmetric comparison yields an error bounded by
   C exp(CQ-Q^2/256). It is uniform in the larger cap. Multiplying it by
   the extra factor 1+Q needed for the backward fields still tends to zero.
6. Passing the integral equations therefore gives the actual uncut C1
   local path and strong convergence of its named fields. The same
   rank-one difference estimates in Hilbert--Schmidt norm give the raw
   affine Hilbert path, not just operator-norm convergence of increments.

This verifies the local existence and convergence premises C actually uses.
The imported arguments also discuss uniqueness, but C's proof does not need
to invoke uniqueness of an arbitrary uncut competitor to establish symmetry.

## 4. Actual Gaussian source identification and independence

This is the most consequential premise for C:96-119 and Sections 4-5.
Bounds on arbitrary deterministic A and B alone would not identify the
trained population, and independence of the initialized matrices alone
would not justify treating their trained queries as fresh Gaussians.
The permitted sources provide the missing identification explicitly.

### 4.1 Conditional residuals and the source representation

G:311-373 conditions an initial matrix on all previous forward and reverse
observations WV=Y and W^T U=Q. With nonsingular query Grams its residual is

    P_(U-perp) W_tilde P_(V-perp),

and its conditional mean is the two constraint-satisfying terms in G:(3.3).
For a new forward input h, the new Gaussian part is proportional to

    (||h_perp||/sqrt(n)) P_(U-perp) g.

The rank of the discarded projection is bounded by the fixed number of
previous queries. Its normalized squared error tends to zero. Conditional
Gaussian averaging and second-moment convergence then give the joint
same-population empirical law of the old tuple and new answer.

Adaptation does not invalidate this conditioning: at each call the input is
measurable with respect to the already exposed transcript. A new answer
places a linear constraint on the queried residual matrix. The two residual
matrices stay conditionally independent under this sequential construction.
This is an argument about actual reuse, rather than resampling the matrix.

G:375-427 then rewrites the conditional means as response terms. The key
identity is

    E[q_s h_perp] = E[zeta_s h_perp]
                 = sum_t E[u_s u_t] E[partial_(zeta_t) h_perp].

The first equality uses the orthogonality to prior forward inputs; the
second is Gaussian integration by parts with all deterministic coefficients
fixed. Substitution cancels the old forward projection response terms.
The resulting answer is

    xi_h + sum_s u_s E[partial_(zeta_s) h].

The new source extends its own oriented source group by a deterministic
linear combination of old sources plus a fresh independent Gaussian.
Its covariance with an old source is E[h v_r], and its variance is E[h^2].
This proves the full uncentered input second-moment covariance rule and
independence of distinct oriented groups. It is not a rule subtracting the
squared response from the source variance.

In the middle population, xi in C is the forward W^(2)_0 group and zeta is
the reverse (W^(3)_0)^* group. They are different oriented groups on the
same population's joint coordinate law, so their complete finite
sample/time arrays are independent. The computed Z^(2) and q^(2) generally
are dependent, because their coordinate recursions couple the two groups.
C does not confuse these statements.

### 4.2 Singular source covariances and the actual trained recursion

G:429-475 treats singular query Grams by adding fresh small noise to the
inputs of a fixed program, proving the nonsingular law, and removing that
noise. The finite comparison costs C epsilon on the initial operator-norm
event. On the scalar side, covariance square roots are continuous, and the
finite bounded-derivative expressions and their expected derivatives pass
to the limit. This does not assume convergence of inverse Grams.

The hypotheses apply here at each fixed mesh and cap: the raw first update
uses a bounded gate times a clipped query; the middle delta has the same
form; the top readout is bounded by aS and its product can be smoothly
extended outside its attained range. Formal slots are retained when their
Gaussian variance vanishes. In particular zero initial readout makes the
actual initial backward fields zero, but does not set their reverse-source
formal derivatives to zero. B:130-140 checks this base case.

B:75-108 identifies the trained law by unrolling the actual matrices.
The learned forward memory is

    (Delta/2) y_b E[H_(k,a) H_(r,b)] delta_(r,b),

and the learned reverse memory is

    (Delta/2) y_b E[delta_(k,a) delta_(r,b)] H_(r,b).

Adding the initial-action response gives exactly B:(2), hence C:(2)-(4).
The sums include both samples and all available times. Forward memories
are strictly past-time; reverse memories include the present time. The
reverse derivative retains the current return through the other matrix.
Freezing finitely many contractions and restoring their empirical values
by the finite norm comparison does not change the limiting law.

The construction is applied only at fixed finite query count. No part of
C applies this induction directly with a query count growing with width.

### 4.3 Response bounds and their activation transfer

I checked the estimates imported from B, rather than assuming the law has
small responses. With A_0=3/2 as the response coefficient bound, the causal
order is A^(2), Z^(2), A^(3), Z^(3), delta^(3), B^(3), q^(2),
delta^(2), B^(2). Thus no current bottom response bound is assumed in
proving itself.

The raw first sensitivity has one injection Delta e/2. After the feature
gate it is Delta/200 times the Gronwall envelope E^(1). The two-sample
Gaussian maximum estimate and time Jensen give E E^(1)<6. Consequently

    |A^(2)| < (Delta/2)(49/36 + 3/50)
            < (Delta/2)(3/2).

For the middle total forward derivative row, there is one direct derivative
per output row. Summing the two update samples changes Delta/2 to Delta,
not to 2 Delta. Its envelope obeys

    E[(E^(2))^p] <= 4 exp(219p/400 + 3969p^2/1280000).

In particular E E^(2)<8 and ||E^(2)||_2<7/2. The reverse-source injection
then gives

    |A^(3)| < (Delta/2)(49/36 + 3/25)
            = (Delta/2)(1333/900)
            < (Delta/2)(3/2).

The top total delta derivative is bounded by (73/300)S times its forward
derivative row. Its Gronwall bound is exp(657/800)<5/2 on S<=3/2.
Including learned memories gives

    V_* = 73/80 + 147/3200 = 3067/3200 < 1,
    Q_* = ea(3/2) + a V_* = 24829/19200.

The completed past rows satisfy the same bounds. The current middle
derivative, including the current return, and Cauchy--Schwarz give

    U_k <= (7/2)(Q_*/5 + V_*/100) + (3/200) Q_*^2
         = 71063018523/73728000000 < 97/100.

Thus C's coefficient bounds follow with room to spare. These calculations
use only a, e, c and the specified smooth cuts. J:83-108 correctly transfers
them to sech; no arctangent-specific inverse coordinate or gate identity
is used in B.

Finally q=zeta+beta with |beta|<=a and Var(zeta)<=(7/40)^2 at either reverse
layer gives, without independence of beta and zeta,

    E exp(q^2/16)
      <= exp(49/288) (1-49/6400)^(-1/2) < 2.

Fatou after the stated strong limits gives the non-strict bound <=2 for
the actual local query. This is the upper-tail premise C needs.

### 4.4 The common operators are actual adjoints

G:623-680 constructs each population separately from consistent finite
same-layer laws. The chosen coordinate family is dense in its L2 space.
The finite Gaussian operator norm event passes to every rational input
combination, giving ||W_0 U||_2 <= 10 ||U||_2. Exact finite transpose
pairings pass to the corresponding limiting second moments. Density then
extends both actions and proves that the reverse action is the Hilbert
adjoint. A:34-43 implements the same construction with the two-sample root.

This supports both the temporal estimates and the adjunction used later
in the Hessian formula. It supplies L2-to-L2 boundedness only. It does not
identify neuron indices between different populations or supply an Lp
operator theorem.

## 5. Uniform temporal and Gaussian path bounds

C:163-219 passes this check. Here is a fully quantitative way to see why
neither the mesh nor a cap enters its constant.

Let T_0=3/2 and use finite RMS norms on the initial operator-norm event.
Set

    M_3 = 10 + e a^2 T_0^2/2,
    M_2 = 10 + e^2 a^2 M_3 T_0^2/2.

Since Delta sum_(r<k) t_r <= t_k^2/2, the Euler rank-one updates imply
||W^(3)_k||_op <= M_3 and ||W^(2)_k||_op <= M_2. At each node,

    |W^(4)_k| <= a t_k,
    ||delta^(3)_(k,a)||_2 <= e a t_k,
    ||q^(2)_(k,a)||_2 <= M_3 e a t_k,
    ||delta^(2)_(k,a)||_2 <= e^2 a M_3 t_k,
    ||q^(1)_(k,a)||_2 <= e^2 a M_2 M_3 t_k.

The first-field velocity is bounded by e times the last quantity, since
the absolute row sum of C/2 is at most one. Both raw matrix increments
are bounded by their delta norm times a Delta. Neither estimate uses a
pointwise bound on either backward query.

Let V_1=e^3 a M_2 M_3 T_0. Successive forward splits as in C:178-179 give
adjacent-node bounds V_2 Delta and V_3 Delta for the second and third
preactivations, where one possible choice is

    V_2 = e^2 a^3 M_3 T_0 + M_2 e V_1,
    V_3 = e a^3 T_0 + M_3 e V_2.

The top delta split consequently gives

    ||delta^(3)_(k+1,a)-delta^(3)_(k,a)||_2
       <= (ea + a T_0 c V_3) Delta.

This provides a finite deterministic D for C:(7). The same constants
work for all meshes and both caps. At each fixed program the empirical
squared differences converge to deterministic second moments, while the
norm event has probability tending to one. Therefore their limiting
values satisfy the same deterministic inequality; conditioning the
limiting source law on the norm event is unnecessary.

The covariance rule now gives

    E|zeta_(k,a)-zeta_(j,a)|^2
       = ||delta^(3)_(k,a)-delta^(3)_(j,a)||_2^2.

Zero readout gives zeta_(0,a)=0. Linear interpolation preserves the L2
increment bound: subdivide an increment at mesh endpoints and sum the
within-cell and full-cell bounds. This yields D|t-u| for every t,u.

For the finite interpolated Gaussian process, the dyadic argument in C
is dimension-independent. If N centered Gaussian variables have variances
at most v^2, their union bound gives

    E max_i |G_i|^2 <= 2v^2(log(2N)+1).

At dyadic level j the resulting L2 norm is bounded by a constant times
DS 2^(-j) sqrt(j+1). These bounds are summable. Minkowski's inequality,
continuity, and the endpoint S contribution give C:(9). Correlation between
increments is allowed throughout. For two samples use the sum of their
squared supremum bounds.

For regression on any scalar X, the residual increment is the orthogonal
projection of the original increment onto the orthogonal complement of X
in Gaussian L2. Its variance is no larger. The residual process starts at
zero and obeys the same dyadic estimate. No Gaussian process limit, growing
mesh union bound, or independent-increment assertion is hidden here.

## 6. Nondegeneracy and the reverse-source conditioning

### 6.1 Positive variance at every sufficiently small positive time

C:223-242 does not assume that an opposite-label readout is positive.
It uses the weaker and sufficient assertion that it is nonzero in L2.

For |rho|<1, the initial first Gaussian pair has positive density on R^2.
If alpha phi(G_1)+beta phi(G_2)=0 almost surely, continuity implies the
identity for every pair of real arguments. Varying one argument and using
the nonconstancy of phi forces alpha=beta=0. Thus its feature Gram is
positive definite.

At rho=-1 write b(G)=(1/10)atan(sinh G). The two features are
(1+b(G),1-b(G)), with E b=0 and E b^2>0. Their Gram has eigenvalues
2 and 2 E b^2. It is positive definite even though the preactivation
pair has singular covariance. Applying the initial forward covariance
rule gives a nondegenerate second Gaussian pair; the same argument gives
a positive definite second feature Gram and then a nondegenerate third
Gaussian pair and positive definite third feature Gram.

For every allowed label vector y,

    ||V_0||_2^2 = (1/4) y^T K^(3)_0 y > 0.

The readout integral and L2 continuity give W^(4)(s)/s -> V_0. Therefore
||W^(4)(s)||_2 >= s ||V_0||_2/2 for all sufficiently small s>0.
Continuity of the first feature Gram and of g, with g(0)=0, allows one
common S_0 in (0,3/2] on which K^(1)(s) stays positive definite and
|g(s)|<1/2. Every preactivation is finite almost surely because it is in
L2. Since phi'>0 at every finite argument, multiplication by this gate
cannot annihilate a nonzero readout. Thus v_a(s)>0 for both samples at
every s in (0,S_0].

This verifies the full stated time quantifier. It does not give a positive
variance lower bound uniform as s decreases to zero, nor is one required.
The exclusion of rho=1 is necessary for the opposite-label argument:
identical inputs would make that initial label mode vanish.

At fixed S, write v_a(S)=v_*>0. Strong cut convergence first makes the
cut terminal second moment at least 3v_*/4 for every sufficiently large
cap. At each such fixed cap, mesh convergence makes it at least v_*/2 for
every sufficiently fine mesh. This proves exactly the nested lower bound
v_0=v_*/2 used in C. The upper bound v_1=(eaS)^2 is pointwise-primal and
holds for all these approximations. No circular lower-tail assertion is
used to establish this variance.

### 6.2 Regress the entire reverse array, not just its endpoint

For X=zeta_(M,a), define

    c_(k,b)=Cov(zeta_(k,b),X)/v,
    G_(k,b)=zeta_(k,b)-c_(k,b)X,
    v=E X^2 in [v_0,v_1].

The joint vector (X,G) is Gaussian and has zero cross covariance. Its
characteristic function factors into those of X and G, which proves
independence even when the covariance of G is singular. By Cauchy--Schwarz,

    |c_(k,b)| <= eaS/sqrt(v_0).

The residual increment variances decrease under this regression. Section 5
therefore provides a deterministic B_0, uniform in cap and mesh, such that
P(max_(k,b)|G_(k,b)|<=B_0)>=1/2. At the selected endpoint the residual
actually vanishes, which causes no difficulty.

Define the reverse-source event explicitly by

    E_R = {max_(k,b)|G_(k,b)|<=B_0}
          intersect {sigma X in [R+a+1,R+a+2]}.

The two events are independent. A uniform scalar density lower bound gives

    P(E_R) >= [2 sqrt(2 pi v_1)]^(-1)
              exp(-(R+a+2)^2/(2v_0))
            >= c exp(-C(R+1)^2).

On E_R,

    max_(k,b)|zeta_(k,b)|
      <= (eaS/sqrt(v_0))(R+a+2)+B_0 =: B_R.

Because the reverse response row sums are at most one and features have
absolute value at most a, the deterministic recursion gives
|q_(k,b)-zeta_(k,b)|<=a for every realization of the forward source.
In particular sigma q_(M,a)>=R+1 on E_R for every forward realization.
This verifies C:(11)-(14) with B_R<=C(R+1). It avoids assuming independent
time slots or estimating the growing array by a mesh-dependent union bound.

## 7. Forward regression, quantitative preimages, and the lower bound

The second conditioning step in C:274-346 is valid independently of the
first one. The complete forward source is independent of the reverse
source, and X_f=xi_(M,a) has variance

    v_f = E[(H^(1)_(M,a))^2] in [m^2,a^2].

Regress its full array as xi=d X_f+F. Gaussian regression gives
F independent of X_f, while independence of the source groups gives
(F,X_f) independent of zeta. Hence X_f remains N(0,v_f) when conditioning
jointly on F and zeta. Its scalar variance is never a conditional variance
of a trained preactivation.

The covariance bound gives |d_(k,b)|<=a^2/m^2=d_0. At the selected endpoint,
d_(M,a)=1 and F_(M,a)=0. The support of the residual law is contained in
this hyperplane. For every residual in that support, varying X_f=x remains
a legitimate parametrization of its conditional Gaussian law. Even if all
other source coordinates are determined by X_f, this step still works.

Fix zeta in E_R and such an F. The source coefficients and covariances are
held fixed. This defines a continuous finite causal recursion in x. The
current reverse query may depend on the current feature, but that feature
is already computed from strictly earlier deltas; there is no implicit
same-time fixed-point problem.

For all x, |q_(k,b)(x)|<=B_R+a and |delta_(k,b)(x)|<=e(B_R+a). Summing
the two-sample forward memories gives

    |Z_(M,a)(x)-x|
      <= (A_0 Delta/2)(2M)e(B_R+a)
      = A_0 S e(B_R+a) = D_R,

where A_0=3/2 and D_R<=C(R+1). There is no residual term at this endpoint,
because F_(M,a)=0. Other entries of F may be arbitrarily large. This is
why the proof needs no small-ball probability for the growing forward
residual array.

For x and x', let E_k be the maximum preactivation difference over both
samples and nodes through k. The reverse row sum and Lipschitz activation
give |q_(r,b)(x)-q_(r,b)(x')|<=e E_r. Splitting the middle delta difference
between the gate and the clipped query gives

    |delta_(r,b)(x)-delta_(r,b)(x')|
      <= [c(B_R+a)+e^2] E_r = L_R^0 E_r.

One uses |tau_Q(q)|<=|q| in the first term and the one-Lipschitz property
of tau_Q in the second. Thus

    E_k <= d_0|x-x'| + A_0 Delta L_R^0 sum_(r<k) E_r,
    E_M <= d_0 exp(A_0 S L_R^0)|x-x'| = L_R|x-x'|.

The maximum over earlier output times only increases the positive sum,
so this discrete Gronwall application is valid. Also
1<=L_R<=C exp(C(R+1)), uniformly in cap, mesh, and F.

Let [b-h,b+h] lie inside the interior of the desired interval I. The
terminal map x -> Z_(M,a)(x) is continuous and stays within D_R of x.
It consequently takes a value at most b-1 at b-D_R-1 and at least b+1
at b+D_R+1. The intermediate value theorem supplies a preimage x_0 of b
in this bracket. No monotonicity, positive derivative, inverse function
theorem, or one-to-one assertion is being used.

With r_R=min(1/2,h/(2L_R)), the entire interval [x_0-r_R,x_0+r_R] maps
into [b-h/2,b+h/2]. Its length is 2r_R>=c exp(-C(R+1)), and its points
have |x|<=|b|+D_R+3/2. The scalar Gaussian density on that region is at
least

    [sqrt(2 pi)a]^(-1)
       exp(-(|b|+D_R+3/2)^2/(2m^2)).

Multiplying length and density gives the conditional lower bound
c exp(-C(R+1)^2). The factor exp(-C(R+1)) from the interval length is
absorbed into the quadratic exponent. Thus the quantitative preimage
argument preserves Gaussian-order lower tails, not merely positivity.

There is no measurable-selection omission. The recursion is a measurable
function of (x,F,zeta); integrating the indicator of its closed target
interval against the fixed scalar density gives a measurable conditional
probability. For each fixed (F,zeta) the existence of one interval of the
displayed length gives the same lower bound on that integral. A measurable
choice of its center is unnecessary.

Integrating over F and the event E_R gives C:(20), because its terminal
query inequality already holds for all x and F. The two lower bounds
multiply, changing only their finite constants. Only v and v_f were
inverted. A singular time/sample covariance creates no obstruction.

## 8. Both limit passages and the middle multiplier

Fix S, I, sample, sign, and tail threshold R. Use the fixed closed set

    F_R = [b-h/2,b+h/2] times {q: sigma q >= R+1}

in the two terminal coordinates (Z^(2),q^(2)). The probability estimate
from Section 7 holds for all sufficiently large caps and then all
sufficiently fine meshes, with the same positive constants.

For each fixed such cap, joint terminal laws converge as the mesh tends
to zero. If mu_n converges weakly to mu and F is closed, define
h_j(x)=max(0,1-j dist(x,F)). Then 1_F<=h_j, h_j is bounded continuous,
and h_j decreases to 1_F. Consequently

    limsup_n mu_n(F) <= integral h_j dmu

for each j, and bounded convergence gives limsup_n mu_n(F)<=mu(F).
This is precisely the inequality needed to preserve a lower bound on
the probabilities of a closed set. Its direction in C:350-355 is correct.
The argument allows the unbounded closed set F_R and boundary atoms.

Apply it first to the mesh limit at fixed cap, then to the strong joint
cut-removal limit of (Z^(2),q^(2)). The constants are uniform for both
passages. No convergence of the regressed source processes, their
coefficients, or their conditional laws is required. Only the two terminal
computed fields are passed to the limit. The query margin R+1 implies the
strict inequality >R, and the fixed closed preactivation interval is inside
I. This proves C:(5) for open, closed, or other nondegenerate real intervals.

On a fixed nondegenerate compact interval J inside (1,2), let

    kappa = min_(z in J) [-phi''(z)] > 0,
    M_a = y_a phi''(Z^(2)_a(S)) q^(2)_a(S).

For either sign eta, choose the query sign sigma=-eta y_a. On J,

    eta M_a = [-phi''(Z^(2)_a)] sigma q^(2)_a.

Applying (5) at threshold T/kappa therefore gives a Gaussian-order lower
bound for P(Z^(2)_a in J, eta M_a>T), for T>=1. Conversely,
|M_a|<=c|q^(2)_a| and the imported exponential-square bound give

    P(eta M_a>T) <= 2 exp(-T^2/(16c^2)).

This proves the two signs and the Gaussian upper/lower tail assertion in
C:362-369. Constants may depend on S, J, and the fixed configuration; the
claim does not require matching upper and lower exponents.

In particular M_a is essentially unbounded in both signs even after
restricting Z^(2)_a to J. The scalar M_a is in L2, because phi'' is bounded
and q^(2)_a is in L2. Its multiplication action has no bounded extension on
all L2 from its natural domain. Gaussian integrability and essential
boundedness are different properties; the faster sech decay does not imply
the latter for this actual trained law.

## 9. Ordinary directional second derivatives with only L2 actions

Fix a reached state at S in (0,S_0]. Let K be its first feature Gram.
The vector of coefficients in C:376 is the a-th row of K^(-1), divided
by sqrt((K^(-1))_(aa)). Direct multiplication by K gives

    E[B_a^2]=1,
    E[B_a H^(1)_b]=d_a 1_(a=b),
    d_a=1/sqrt((K^(-1))_(aa))>0.

B_a is bounded, since it is a fixed finite linear combination of bounded
features. This remains valid at rho=-1: it is the positive feature Gram
K being inverted, not the singular first-preactivation covariance C.

For each fixed v in L2(Omega_2) intersect L-infinity(Omega_2) with
||v||_2=1, set T_v=v tensor B_a. This direction is an admissible
Hilbert--Schmidt increment with norm one, hence a raw unit direction.
Its bounded rank-one kernel uses the two separate populations. Along the
line W^(2)+t T_v, all other parameter blocks are held fixed, and exactly

    Z^(2)_b(t)=Z^(2)_b+t d_a v 1_(a=b).

The other sample is unchanged along the whole line, not just to first
order. For the selected sample, the L2 curve

    h(t)=phi(Z^(2)_a+t d_a v)

is C2, with derivatives d_a phi'(Z^(2)_a+t d_a v)v and
d_a^2 phi''(Z^(2)_a+t d_a v)v^2. Indeed v^2 is in L2, and bounded
continuous derivatives together with dominated convergence give these
L2 derivatives and their continuity. Boundedness of v is used for each
fixed direction; no bound uniform over all chosen directions is needed.

Applying the bounded operator W^(3):L2(Omega_2)->L2(Omega_3) proves that
z(t)=W^(3)h(t) is C2 into L2 with

    u=z'(0)=d_a W^(3)[phi'(Z^(2)_a)v],
    b=z''(0)=d_a^2 W^(3)[phi''(Z^(2)_a)v^2].

These are C:(21). Both operator inputs are in L2. No L4 bound for u is
available from this calculation, and none is needed.

To check the last activation, write w=W^(4)(S), which is fixed on the
entire test line and satisfies ||w||_infinity<=aS. Define

    P(t)=E_3[w phi(z(t))].

The L2 curve chain rule gives P'(t)=E[w phi'(z(t))z'(t)]. Its derivative
at zero can be obtained from the exact decomposition

    (P'(t)-P'(0))/t
      = E[w phi'(z(t)) (z'(t)-u)/t]
        + E[w u (phi'(z(t))-phi'(z(0)))/t].

In the first term, (z'(t)-u)/t -> b in L2. The gate converges in
probability and is uniformly bounded, so the expectation tends to
E[w phi'(z(0))b]. In the second term put

    a_t=(z(t)-z(0))/t,
    k_t=integral_0^1 phi''(z(0)+r(z(t)-z(0))) dr.

Then a_t -> u in L2, |k_t|<=c, and k_t -> phi''(z(0)) in probability.
The product converges in L2: write

    a_t k_t-u phi''(z(0))
       = (a_t-u) k_t + u[k_t-phi''(z(0))].

The first summand tends to zero by the uniform bound; for the second,
truncate the fixed u in L2 and then use bounded convergence in probability.
Since w u belongs to L2, its pairing converges. This proves the ordinary,
two-sided derivative of P', with value

    P''(0)=E[w phi'(z(0))b]+E[w phi''(z(0))u^2].

The square u^2 only needs to be in L1 here, since w phi'' is bounded.
There is no application of W^(3) to u^2 and no L2-to-Lp operator claim.
This is stronger than merely identifying a formal Taylor coefficient.

The alternative scalar cross-remainder estimate in C:409-413 is also
correct: for z(t)=z(0)+tu+r_t, subtract the linear r_t contribution
and use the Lipschitz bound on phi'. Its absolute value is at most

    c ||w||_infinity
       (|t| ||u||_2 ||r_t||_2 + ||r_t||_2^2/2).

Here ||r_t||_2=O(t^2), so it is o(t^2). The displayed factor |t| is
essential and is present. The derivative argument above, rather than an
unsupported equivalence between Peano expansions and ordinary derivatives,
already establishes the required ordinary second derivative.

Adjunction in the first term uses the genuine delta^(3)_a and the L2
input phi''(Z^(2)_a)v^2. Multiplying by y_a/2 therefore gives exactly

    D^2 g[T_v,T_v]
      = (d_a^2/2) E_2[M_a v^2]
        + (y_a d_a^2/2) E_3[
            w phi''(Z^(3)_a)
            (W^(3)[phi'(Z^(2)_a)v])^2].

The second term has absolute value at most

    (d_a^2/2) aS c ||W^(3)||_op^2 e^2,

uniformly over these unit directions, as in C:(23).

For any N>0, the positive and negative tail events of M_a each have
positive probability. For example, with E_N={M_a>N}, choose
v_N=1_(E_N)/sqrt(P(E_N)). This field is individually bounded and has
unit L2 norm. Its squared weight gives E[M_a v_N^2]>N. The analogous
negative event gives a value below -N. These expectations are finite
because M_a is in L2 and each v_N^2 is bounded. Thus D^2 g has both
unbounded signs after adding the uniformly bounded top term.

The order of quantifiers is legitimate: fix a bounded direction, take its
ordinary line derivative, and only then vary N. No uniform L-infinity
bound over the test directions or uniform second-order remainder is claimed.

## 10. Actual base-state symmetry and the full loss

The symmetry in C:(4a) is a property of the actual initialized Euler
construction, not of arbitrary coefficient arrays satisfying (3).
For y=(1,sigma), let pi exchange the samples. Transform the raw first
fields by pi, leave both hidden matrices unchanged, and multiply the
readout by sigma. Forward fields exchange; deltas and reverse queries
exchange and acquire the factor sigma. Oddness of both cuts preserves
this rule.

The matrix velocity is invariant under the transformation, since
y_(pi(b))=sigma y_b and the backward field contributes another factor
sigma. The readout velocity transforms by sigma. For the first fields,
C commutes with the sample permutation, giving the same covariance-weighted
update after exchange. These facts verify equivariance of the actual
simultaneous Euler updates, including at rho=-1.

The initialized first pair is exchangeable, the hidden matrices have the
same unchanged joint law, and zero readout is invariant. The finite
predictor pair consequently has the same distribution as
(sigma f_2,sigma f_1). Its deterministic fixed-program limits must equal
their transformed values, so f_2=sigma f_1 in the population construction.
The fixed-cap mesh limit and cut removal preserve the identity. A global
label/readout sign reversal covers the other two label choices. Hence

    f_a = y_a g

at every reached local base state. This argument uses neither pathwise
finite-width residual equality nor a uniqueness theorem for arbitrary
uncut population solutions.

The scalar predictor gradients exist in the raw affine Hilbert space.
The imported proof in A:196-210 expands the scalar pairing from the top
down, with a fixed old L2 backward factor. Truncation bounds its remainder
by C R ||v||_2^2 plus C ||B 1_(|B|>R)||_2 ||v||_2. Letting the increment
tend to zero and then R tend to infinity gives Fréchet differentiability.
Matrix/readout cross increments are quadratic, and bounded-gate products
with fixed L2 factors give gradient continuity. This proof does not need
Fréchet differentiability of the activation map from all L2 to L2.

For the particular unit directions above there is also the direct bound

    D f_a[T_v] = d_a E_2[delta^(2)_a v],
    D f_b[T_v] = 0 for b != a,
    sum_b (D f_b[T_v])^2 <= d_a^2 ||delta^(2)_a||_2^2.

Thus the first-derivative contribution to the full loss is uniformly
bounded at this state, without any Hessian bound.

Now differentiate the actual full loss along the test line before using
symmetry. With L=sum_b(f_b-y_b)^2,

    D^2 L[T_v,T_v]
      = 2 sum_b (D f_b[T_v])^2
        + 2 sum_b (f_b-y_b) D^2 f_b[T_v,T_v].

At the base state f_b-y_b=y_b(g-1), and by definition
sum_b y_b D^2 f_b=2 D^2 g. Therefore

    -D^2 L[T_v,T_v]
      = 4(1-g) D^2 g[T_v,T_v]
        - 2 sum_b (D f_b[T_v])^2.

This verifies the sign and factor 4 in C:(24). The relation f_b=y_b g
was not differentiated along the perturbation line; it generally does
not hold on that line. Since 1-g>1/2, the nonzero coefficient of D^2 g
and the bounded first-derivative term preserve both unbounded signs of
D^2 L (with the signs exchanged relative to the leading D^2 g term).

If grad L were Lipschitz with finite constant L_0 on a neighborhood of
the reached state theta, then for each fixed unit T_v and sufficiently
small nonzero t,

    |<grad L(theta+t T_v)-grad L(theta),T_v>/t| <= L_0.

Passing to the ordinary scalar second derivative gives
|D^2 L[T_v,T_v]|<=L_0 for every such direction, contradicting the
unbounded values. In fact the same argument rules out a finite centered
Lipschitz bound against theta. It does not require a Hessian operator
defined on every direction in the Hilbert space.

## 11. Local physical time and final scope decision

At the reached symmetric state, scalar differentiability and the residual
identity give

    -grad L = 2(1-g) sum_a y_a grad f_a
            = 4(1-g) grad g.

Thus the constructed feature path can be reparametrized locally by
ds/dt=4(1-g). Since |g|<1/2 throughout the chosen short interval,
the inverse time obeys

    t(S)=integral_0^S [4(1-g(u))]^(-1) du,
    S/6 <= t(S) <= S/2.

In particular each fixed positive S corresponds to a deterministic
positive physical time. This uses only the local population path and
its actual symmetry. It supplies no finite-width samplewise clock and
no global opposite-label continuation.

The scope advertised in C:463-478 is respected. The proof shows that
this activation's faster derivative decay does not remove the actual
middle multiplier's two essential tails on the proved short positive-time
interval. It does not establish or refute global response bounds, global
two-label convergence, uniqueness by itself, nonuniqueness, or a
finite-width fixed-positive-time Hessian divergence statement. Local
existence from the imported cut construction is compatible with the
proved failure of local gradient Lipschitzness.

**Final disposition:** accept this exact candidate as the stated modular
local route lemma. Required findings: none. Optional findings: O1-O3 above.
No conclusion outside the explicitly checked imported scope is promoted
by this audit.
