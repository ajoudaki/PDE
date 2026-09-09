# Middle curvature at positive local training time

Root candidate, 2026-09-06. UNVERIFIED. This is a modular local
distribution/regularity theorem, not a global two-label limit theorem.
No experiment or specialized external theorem is used. The point is to
test whether faster decay of an activation's derivatives at infinity
can remove the middle multiplier on the actually trained population.

Use phi(z)=1+0.1 atan(sinh z), three hidden layers and the two-sample
canonical Gaussian initialization. Inputs have RMS one, fixed correlation
rho in [-1,1); labels y_a are arbitrary signs. All weight normalizations,
the sum-of-two-squares loss and raw metric are specified below. Constants
may depend on the fixed data and the fixed positive observation time.

## 1. Exact imported local premises

The following mathematical sources, all read fully by the root, are the
explicit dependencies. Review verdicts are not mathematical premises.

- TWO_SAMPLE_SHORT_RESPONSE_BOOTSTRAP.md, SHA256
  9305453f933ad30a0e813e4e97942ee9e00490ce726d70142b25c8f67a475170:
  the finite Gaussian Euler program and both backward response estimates
  on feature time [0,3/2].
- SECH_LOCAL_JET_AND_SIGN_BRIDGE.md, SHA256
  65fab11c5892afe517fe4289450f0736bb137bb1a118e85f8ea8541e18a017f8:
  ONLY Sections 1-2 for transfer of that program to sech, common bounded
  operators, local cut removal, scalar gradient and sample symmetry.
  Its cubic-jet estimates and sign-change theorem are not used.
- SAME_LABEL_GLOBAL_ASSEMBLY.md, SHA256
  510fd019c204e0e89e0c6bcb99c031a11de974b05323df1c016c72b263f64a44:
  ONLY Sections 1-2 and the scalar-gradient and symmetry arguments in
  Section 3. No same-label fitting bound is used for opposite labels.
- /tmp/l3-standalone-proof-D6AW4s/L3_GLOBAL_SELF_CONTAINED_PROOF.md,
  SHA256 bebbb70a8f8da8fd2fa5304fc7af08026e72aef73e20f77f046509f87e63954e:
  ONLY the elementary finite Gaussian-program/common-operator construction
  and limiting tools used by the preceding dependencies.

Here are the precise consequences imported. The first population has
Gaussian pair (Z^(1)_(0,1),Z^(1)_(0,2)) with covariance C, C_aa=1,
C_12=rho. Initial operators W^(2)_0 and W^(3)_0 are the limits of
independent matrices with entries N(0,1/n), have operator norm at most
10, and act between three SEPARATE probability spaces with their actual
adjoints. Initially W^(4)=0. Current equations are

  H^(ell)_a=phi(Z^(ell)_a),
  Z^(2)_a=W^(2)H^(1)_a, Z^(3)_a=W^(3)H^(2)_a,
  delta^(3)_a=W^(4) phi'(Z^(3)_a),
  q^(2)_a=(W^(3))^*delta^(3)_a,
  delta^(2)_a=phi'(Z^(2)_a)q^(2)_a,
  q^(1)_a=(W^(2))^*delta^(2)_a,
  delta^(1)_a=phi'(Z^(1)_a)q^(1)_a.

Feature time s is the gradient-ascent time of

  f_a=E_3[W^(4)H^(3)_a],  g=(1/2)sum_a y_a f_a.

Thus

  (Z^(1)_b)'=(1/2)sum_a C_ba y_a delta^(1)_a,
  (W^(ell))'=(1/2)sum_a y_a delta^(ell)_a tensor H^(ell-1)_a,
                                                   ell=2,3,
  (W^(4))'=(1/2)sum_a y_a H^(3)_a.                    (1)

Here U tensor V maps B to U E[VB]; its finite counterpart is UV^T/n.
The matrix increments use Hilbert--Schmidt norm. First-field variations
use E[v^T C^(-1)v] when |rho|<1, or the one-field metric on (v,-v)
when rho=-1. Readout uses L2. At finite width the raw metric is

  d||dW^(1)||_F^2/n + ||dW^(2)||_F^2 + ||dW^(3)||_F^2
                                      + ||dW^(4)||_2^2/n.

The uncut local population solution exists on [0,3/2], is a C1 curve in the raw
affine Hilbert state space, and is the strong limit of the cut flows; the named queries and
fields converge strongly as well. Fixed-cap Euler laws converge to their
cut flow as the mesh tends to zero, including joint time/field second
moments. No width-growing finite Gaussian-program assertion is imported.
All primal bounds on this feature interval are independent of the caps.
In particular |W^(4)(s)|<=as, where

  m=5/6, a=7/6, e=1/10, c=1/5,
  m<phi<a, 0<phi'<=e, |phi''|<=c.

On each finite Euler mesh t_k=k Delta, with zero readout, use the same
smooth odd one-Lipschitz cut tau_Q in the two sample components of each
backward layer, with |tau_Q(u)|<=|u|. The two layers may use different
caps; a common cap suffices in the limits below. Q denotes a cutoff,
whereas R below denotes a tail threshold. The second population has
the EXACT limiting coordinate law

  Z^(2)_(k,a)=xi_(k,a)+sum_(r<k,b) A_(ka,rb) delta^(2)_(r,b),
  q^(2)_(k,a)=zeta_(k,a)+sum_(r<=k,b) B_(ka,rb) H^(2)_(r,b),
  H^(2)_(k,a)=phi(Z^(2)_(k,a)),
  delta^(2)_(k,a)=phi'(Z^(2)_(k,a))tau_Q(q^(2)_(k,a)).       (2)

The two complete CENTERED Gaussian source groups xi and zeta are independent,
including all their sample/time coordinates; within each group retain
its entire possibly singular covariance. The coefficients are
deterministic. They include ALL learned rank memories, with

  |A_(ka,rb)| <= (3/2)Delta/2,
  max_(k,a) sum_(r<=k,b)|B_(ka,rb)| <= 1,                 (3)
  E[xi_(ka)xi_(rb)]=E[H^(1)_(k,a)H^(1)_(r,b)],
  E[zeta_(ka)zeta_(rb)]=E[delta^(3)_(k,a)delta^(3)_(r,b)]. (4)

The law also has E exp((q^(2)_(k,a))^2/16)<=2, which passes to every
fixed time of the uncut local solution. The construction establishes
joint empirical averages, not independence of finite trained neurons.
We vary source coordinates below with A,B and all covariances FIXED:
this is a conditional calculation within (2), not a change of their
self-consistency equations or of the actual initialized network.

We also use the following exact consequence of the equivariant finite
Euler construction and its deterministic predictor limits:

  f_a=y_a g on the local population trajectory.          (4a)

For completeness, after a simultaneous label/readout sign reversal it
suffices to use y=(1,sigma). Exchange the two first sample fields, keep
the hidden matrices fixed, and multiply the readout by sigma. The
backward fields are exchanged and multiplied by sigma; oddness of the
cuts preserves this rule. Since y_(3-a)=sigma y_a and C commutes with
sample exchange, the first-field and matrix updates are equivariant,
and the readout update transforms by sigma. The initialized Gaussian
pair is exchangeable and the other initialized blocks are invariant.
Finite predictors have the same law as (sigma f_2,sigma f_1); their
deterministic limits satisfy f_2=sigma f_1. Fixed-cap mesh and cut
removal preserve this identity, proving (4a). This argument requires
neither an exact finite samplewise clock nor uniqueness of an arbitrary
uncut competitor. It uses the actual finite Euler construction, not
arbitrary deterministic A,B satisfying only the numerical bounds (3).

## 2. Claims

There is S_0>0, depending on the fixed input and label configuration,
such that for every fixed S in (0,S_0], every sample a, every real
interval I with positive length, and either sign sigma in {-1,1},
there are positive finite constants c_I,C_I such that

  P{ Z^(2)_a(S) in I, sigma q^(2)_a(S)>R }
                         >= c_I exp(-C_I(R+1)^2), R>=1. (5)

The interval in (5) can be open or closed; the proof actually places Z
in a closed subinterval of its interior. Together with the imported
upper Gaussian tail this gives, for I compactly inside (1,2), Gaussian
upper and lower tails (with different constants) for

  y_a phi''(Z^(2)_a(S))q^(2)_a(S).                       (6)

In particular both signs of (6) are essentially unbounded at EVERY
such fixed positive feature time. They are not caused solely by large
preactivation values; (5) confines the preactivation to an ordinary
fixed interval where the activation is curved.

At each of these states the scalar loss has second directional
derivatives, on a class of bounded rank-one hidden-matrix directions,
whose positive and negative values are unbounded over unit directions.
Consequently its raw L2/Hilbert--Schmidt gradient is not locally Lipschitz
at that actual state. The local uncut flow nevertheless exists under
the imported premises. No uniqueness or restartability theorem is proved
by this document; non-Lipschitzness alone does not disprove either.
This claim is not a counterexample to that flow or to the global target.

## 3. A mesh- and cap-independent Gaussian path bound

First verify a temporal covariance estimate for zeta using only primal
bounds. In a finite raw Euler system on [0,3/2], with initial hidden
operator norms at most 10, readout increments are bounded coordinatewise
by a Delta. Current readout is at most as. Successively bounding the
rank-one increments gives deterministic bounds for both hidden operator
norms. The top delta has RMS at most eaS; hence q^(2), delta^(2),
q^(1), and the bottom raw Euler velocity have bounded RMS, independently
of either cap, since |tau_Q(q)|<=|q|.

Therefore between adjacent nodes the RMS changes of each raw first
field are at most C Delta, and matrix increments have operator norm at
most C Delta. For each forward layer use the exact split

  W_(k+1)h_(k+1)-W_k h_k
       =(W_(k+1)-W_k)h_(k+1)+W_k(h_(k+1)-h_k).

Bounded features, bounded gates, and the preceding RMS increment show
that all forward preactivations change by at most C Delta in RMS.
Finally split the top delta difference into the readout difference
times the new gate and the old bounded readout times the gate difference.
Its RMS is at most D Delta for a deterministic D. Telescoping gives

  ||delta^(3)_(k,a)-delta^(3)_(j,a)||_2 <= D|t_k-t_j|.     (7)

At fixed mesh and caps the empirical second moments converge to the
finite Gaussian program. The initial norm event has probability tending
to one, so (7) passes to that law. Constants are uniform in mesh/caps.
The covariance rule (4) now gives

  (E|zeta_(k,a)-zeta_(j,a)|^2)^(1/2) <= D|t_k-t_j|,
  zeta_(0,a)=0.                                         (8)

Linearly interpolate this FINITE Gaussian array between its nodes.
Its increments still obey (8), by adding within-cell and full-cell
increments and the triangle inequality in L2. It is a continuous
Gaussian process; no limiting Gaussian path theorem is being assumed.

We use this elementary estimate: if a centered continuous finite-dimensional
Gaussian process G on [0,S] starts at zero and has increment standard
deviation at most D|t-u|, then

  (E sup_(t<=S)|G(t)|^2)^(1/2) <= C D S.                (9)

To prove it, approximate each time by its successive dyadic left
endpoints. Continuity expresses G(t) as the sum of its dyadic increments
(include the endpoint S in the level-zero bound). At level j there are
at most 2^(j+1) increments, each of standard deviation at most DS2^(-j).
For N centered Gaussians, not necessarily independent, of variance at
most v^2, the exponential-moment Gaussian bound and a union bound give
P(max|G_i|>u)<=min(1,2N exp(-u^2/(2v^2))). Integration of this bound
gives E max|G_i|^2<=2v^2(log(2N)+1). Minkowski's inequality and
sum_j 2^(-j)sqrt(j+1)<infinity prove (9). Applying it to both samples
costs only a fixed factor. The same proof works for any orthogonal
Gaussian residual after projecting onto a single scalar Gaussian:
projection can only decrease increment variances.

## 4. A large reverse source with controlled whole path

Fix S>0 sufficiently small for the following elementary nondegeneracy.
At initialization the first feature Gram is positive definite: if
|rho|<1 this follows from positive Gaussian density and nonconstant phi;
if rho=-1, the features are 1+b(G),1-b(G) with nonconstant odd b.
The next two Gaussian forward pairs are consequently nondegenerate,
and their feature Grams are positive definite by the same argument.
Thus V_0=(1/2)sum_a y_a H^(3)_(0,a) has positive squared norm for
either label mode. From (1), W^(4)(S)/S tends in L2 to V_0.
Choose S_0 so small that W^(4)(S) is nonzero in L2 for every
0<S<=S_0, the first feature Gram remains positive definite, and |g(S)|<1/2.
Strict positivity of phi' then implies

  v_a(S)=E[(delta^(3)_a(S))^2]>0.                       (10)

For this fixed S, cut removal and then fixed-cap mesh convergence give
E[(delta^(3)_(M,a))^2]>=v_0:=v_a(S)/2>0 for every sufficiently large
common cap and then every sufficiently fine mesh Delta=S/M. Its upper
bound is v_1=(eaS)^2. Thresholds may depend on S and the configuration;
all estimates below depend only on v_0,v_1,D and fixed constants, not
on the subsequently chosen cap or mesh.

Put X=zeta_(M,a), v=E X^2. For every source coordinate write its exact
Gaussian regression as

  zeta_(k,b)=c_(k,b) X+G_(k,b),
  c_(k,b)=E[zeta_(k,b)X]/v.                              (11)

The entire residual array G is independent of X: the joint Gaussian
characteristic function factors because all its covariances with X
are zero. This remains valid for singular source covariances. By
Cauchy--Schwarz, |c_(k,b)|<=eaS/sqrt(v_0). The interpolated residual
starts at zero and inherits increment estimate (8). Equation (9) and
Markov's inequality give a constant B_0 such that

  P(max_(k,b)|G_(k,b)|<=B_0)>=1/2.                      (12)

For a desired sign sigma and R>=1, restrict

  sigma X in [R+a+1,R+a+2].                             (13)

The density of N(0,v), v in [v_0,v_1], gives probability at least
c exp(-C(R+1)^2). This event is independent of (12). Their intersection
therefore has probability at least c exp(-C(R+1)^2), and on it

  max_(k,b)|zeta_(k,b)| <= B_R <= C(R+1),
  sigma q^(2)_(M,a) >= R+1.                             (14)

The second assertion uses (2)-(3) and |H^(2)|<=a, hence
|q^(2)_(M,a)-zeta_(M,a)|<=a. It holds for EVERY realization of the
independent forward source xi, not just its original realization.

## 5. An independent forward source places the preactivation in I

Condition on the complete reverse source satisfying (14). Let
X_f=xi_(M,a). By (4), its variance v_f satisfies m^2<=v_f<=a^2.
Regress the whole forward source onto this scalar:

  xi_(k,b)=d_(k,b) X_f+F_(k,b),
  |d_(k,b)|<=a^2/m^2=:d_0,
  d_(M,a)=1, F_(M,a)=0.                                 (15)

The residual array F is independent of X_f. The whole forward group
is independent of the reverse group. Fix any value of F in its regression
support, so F_(M,a)=0; this holds almost surely under its law. Varying X_f=x
with all deterministic coefficients fixed defines a continuous finite
recursion (2), which we now control uniformly.

First, on (14), every q^(2) coordinate is bounded by B_R+a, whatever x
and F are. Thus |delta^(2)|<=e(B_R+a). The first equation in (2) gives

  |Z^(2)_(M,a)(x)-x| <= (3/2)S e(B_R+a)=:D_R<=C(R+1). (16)

The cancellation of F_(M,a) in (15) is essential here; no bound on F is
needed. For two values x,x', put E_k=max_(j<=k,b)|Z_(j,b)(x)-Z_(j,b)(x')|.
The second equation in (2) and the gate Lipschitz bound imply

  |q_(r,b)(x)-q_(r,b)(x')|<=e E_r,
  |delta_(r,b)(x)-delta_(r,b)(x')|
                  <=[c(B_R+a)+e^2]E_r=:L_R^0 E_r.      (17)

This uses the cutoff's one-Lipschitz property for the query difference
and |tau_Q(q)|<=|q| for the separate gate difference; no derivative of
A,B or a covariance is taken. Equation (3) then gives

  E_k <= d_0|x-x'|+(3/2)Delta L_R^0 sum_(r<k)E_r,
  E_M <= d_0 exp((3/2)S L_R^0)|x-x'|=:L_R|x-x'|,
  1<=L_R<=C exp(C(R+1)).                                (18)

The middle inequality follows by induction from
(1+(3/2)Delta L_R^0)^k<=exp((3/2)t_k L_R^0).

Choose a fixed closed interval [b-h,b+h] inside the interior of I,
where h>0. By (16), at x=b-D_R-1 the output Z_(M,a)(x) is at most b-1;
at x=b+D_R+1 it is at least b+1. The intermediate value theorem gives
x_0 in that bounded interval with Z_(M,a)(x_0)=b. For

  |x-x_0|<=r_R:=min(1/2,h/(2L_R)),

the output lies in [b-h/2,b+h/2]. No measurable selection of x_0 is
required: the measurable preimage of this fixed closed interval has
Gaussian measure at least that of one such interval. All these x lie
in |x|<=|b|+D_R+3/2, and r_R>=c exp(-C(R+1)).

The density of X_f, with variance in [m^2,a^2], is bounded below there
by

  (sqrt(2pi)a)^(-1)
    exp[-(|b|+D_R+3/2)^2/(2m^2)].

Therefore, conditionally on ANY F and ANY reverse source in (14),

  P{Z^(2)_(M,a) in [b-h/2,b+h/2] | F,zeta}
                           >=c exp(-C(R+1)^2).          (19)

Together with (14), this proves uniformly in the relevant caps/meshes

  P{Z^(2)_(M,a) in [b-h/2,b+h/2],
                         sigma q^(2)_(M,a)>=R+1}
                           >=c exp(-C(R+1)^2).          (20)

The constants may be enlarged when multiplying the two lower bounds.
Singular time/sample covariances never cause an inverse-Gram problem:
only the scalar variances v and v_f, explicitly bounded away from zero,
were divided by.

## 6. Passage to the actual local population law

For fixed sufficiently large cap, let Delta=S/M tend to zero. The joint
law of the two named terminal coordinates converges to that of the cut
flow. The event in (20) is closed in R^2, so its limiting probability is
at least the limsup of the preceding probabilities. This elementary
closed-set inequality follows by dominating its indicator by continuous
functions max(0,1-j dist(x,F)), then letting j tend to infinity.
Next send the cap to infinity, using the joint strong local convergence
and the same closed-set inequality. Constants in (20) do not depend on
either limit. The resulting event lies inside the event in (5), because
its query threshold is R+1 and its preactivation interval lies in I.
This proves (5) along the actual uncut local flow.

For (6), fix a closed interval inside (1,2). There phi'' has one sign
and its absolute value is between two positive finite constants, since
phi''=-0.1 sech(z)tanh(z). Apply (5) with the appropriate query sign and
threshold divided by the lower derivative bound. Its Gaussian lower
bound follows. The upper bound follows from bounded phi'' and
E exp((q^(2)_a)^2/16)<=2, by exponential Markov. In particular both
essential tails are unbounded. The lower bound is not an assertion of
independence between the evolved preactivation and reverse query.

## 7. The full loss's second directional derivative at the reached state

Fix 0<S<=S_0 and freeze the state there. Let K_ab=E_1[H^(1)_a H^(1)_b],
positive definite by the choice of S_0. For a chosen sample a define

  B_a=(sum_b (K^(-1))_ab H^(1)_b)/sqrt((K^(-1))_aa),
  d_a=1/sqrt((K^(-1))_aa).

Then E B_a^2=1 and E[B_a H^(1)_b]=d_a 1_(a=b). For ANY bounded
second-population field v of L2 norm one, perturb ONLY W^(2) in the
rank-one direction v tensor B_a. Its Hilbert--Schmidt norm is one.
All raw first fields, W^(3) and the readout remain fixed along this
test line. The preactivation variations are

  D Z^(2)_b=d_a v 1_(a=b),
  D Z^(3)_a=d_a W^(3)[phi'(Z^(2)_a)v],
  D^2 Z^(3)_a=d_a^2 W^(3)[phi''(Z^(2)_a)v^2].            (21)

The other sample is unchanged on this entire line. Because v is bounded,
its square is in L2, so the last formula makes sense. Scalar Taylor
expansion with bounded derivatives proves the second-order expansion
of H^(2) in L2. The bounded operator W^(3) transfers it to Z^(3).

At the last activation the scalar pairing has an ordinary second
derivative even though D Z^(3) need not be in L4. Write the L2 curve
there as z(t), with z'(0)=u and z''(0)=b. The first derivative of its
scalar pairing is E[W^(4)phi'(z(t))z'(t)]. In the difference quotient
of this expression at zero, the term involving (z'(t)-u)/t tends in
L2 to b. The other term pairs W^(4)u in L2 with

  [phi'(z(t))-phi'(z(0))]/t
    =[(z(t)-z(0))/t] integral_0^1
        phi''(z(0)+v(z(t)-z(0)))dv.

The first factor converges in L2 to u; the second is uniformly bounded
and converges in probability to phi''(z(0)). Truncating the fixed L2
factor proves strong L2 convergence of their product. The derivative
is E[W^(4)phi'(z(0))b]+E[W^(4)phi''(z(0))u^2]. Equivalently, for
z(t)=z(0)+tu+r_t with ||r_t||_2=O(t^2), the scalar Taylor cross
remainder is bounded by

  c||W^(4)||_infinity
       (|t| ||u||_2 ||r_t||_2+||r_t||_2^2/2)=o(t^2).

The factor |t| is retained. Thus (21) gives the following exact
ordinary second directional derivative:

  D^2 g[v tensor B_a,v tensor B_a]
    =(y_a d_a^2/2)E_2[phi''(Z^(2)_a)q^(2)_a v^2]
     +(y_a d_a^2/2)E_3[W^(4)phi''(Z^(3)_a)
                           (W^(3)[phi'(Z^(2)_a)v])^2]. (22)

Adjunction in the first term uses phi''(Z^(2)_a)v^2 in L2 and the
actual delta^(3) in L2. The second term has absolute value at most

  (d_a^2/2) aS c ||W^(3)||_op^2 e^2,                  (23)

uniformly over these unit directions. The first term in (22) has both
unbounded signs over that class: choose v to be the indicator of an
event where y_a phi''(Z^(2)_a)q^(2)_a exceeds any fixed level, divided
by the square root of its positive probability. Such v is individually bounded,
has L2 norm one, and its squared weight averages the multiplier over
exactly that event. No common L-infinity bound over the chosen directions
is claimed. Use the negative tail for the other sign.

The scalar predictor gradients are bounded at this fixed primal state:
forward linearization uses bounded gates/features, bounded operators and
the L2 readout; adjunction yields a finite raw gradient norm. Thus the
sum of their squared first directional derivatives is uniformly bounded
over the displayed unit directions. Equation (4a) gives f_a=y_a g at
the BASE STATE for either label configuration, not along the perturbation
line. Differentiate the full sum L=sum_a(f_a-y_a)^2 along that line and
only then substitute its base-state residuals. The exact scalar identity is

  -D^2 L[v,v]=4(1-g)D^2 g[v,v]-2 sum_a(D f_a[v])^2.      (24)

Here v in (24) denotes the full raw test direction just constructed,
not an identification of the three neuron populations. Since |g|<1/2,
(22)-(24) prove both unbounded signs of the full loss's second
directional derivative on unit directions. If its raw gradient were
Lipschitz on a neighborhood of this state with a finite constant L_0,
each such second directional derivative would have magnitude at most
L_0: pair the gradient difference along the test line with its fixed
unit direction, divide by the line parameter and pass to zero. This
contradicts the unbounded values just proved.

Finally the local physical clock is ds/dt=4(1-g)>0, so the reached
states in this theorem occur at deterministic positive physical times
t(S)=integral_0^S [4(1-g(u))]^(-1)du. This is a local statement only.
No exact samplewise finite-width clock or global physical continuation
is asserted for opposite labels.

## 8. Scope for activation design

The proof of (5) uses bounded positive features, bounded first two
derivatives, the actual independent forward/reverse Gaussian sources,
the two local deterministic response bounds, and positive terminal
reverse variance. It does NOT use slow tails of arctan derivatives.
In particular the sharper sech tail does not make the actually trained
middle multiplication operator bounded, even away from feature time zero.

The result does not rule out a global response/tail estimate, nor show
that the target is false. Gaussian tails are compatible with the local
existence premise already in use, and non-Lipschitzness alone says nothing
against uniqueness. No infinite-time result,
finite-width fixed-positive-time Hessian divergence, or global opposite-
label limit is claimed here. This supporting document is not the user's
requested final single-document proof.
