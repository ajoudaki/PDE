# Four-hidden-layer endpoint, nonaffinity, motion and limit bridge

Independent derivation, 2026-09-07. This note changes no existing theorem.
It concerns exactly two inputs with RMS norm one, |rho| <= 1-delta, both
binary label sectors, the activation phi(z)=az+e atan(z), 1/2 <= a <= 1,
0<e, and four hidden layers. The finite model has three independent
square Gaussian hidden matrices, the original first-layer scale 1/d,
the original random readout of variance n^-2, and the original raw
metric and simultaneous GD step n^-2. Population spaces remain separate.

The source construction and the quantitative affine comparison are
separate premises supplied by the new four-layer affine and response
lemmas. This note proves their remaining interfaces, rather than using
the three-layer theorem as a black-box four-layer statement. In
particular it does not select an amplitude uniformly in all depths.

Mathematical dependencies inspected:
- two_sample_odd_activation_theorem/PROOF.md (model and endpoint bridge);
- its SOURCE_AND_LIMIT_BRIDGE.md, especially sections 4--5;
- its INITIAL_MOTION_AND_NORMALIZATION.md, all sections;
- its sources/FIXED_CAP_VELOCITY_BRIDGE.md, especially sections 2--8;
- the generic finite conditioning and common-action passages of its
  sources/L3_LOCAL_COMPLETE_PROOF.md, as used by the new source lemma;
- the explicit eta_* Hermite certificate in
  two_sample_odd_activation_quantitative/PROOF.md and the new affine note.
Historical review outcomes are not premises.

## 1. Inputs required from the four-layer source and affine lemmas

On a compact feature-time interval [0,S], for every cap R, suppose the
new lemmas construct the actual capped population Euler laws with:

(a) a uniformly bounded raw primal ball with strict slack for all
sufficiently fine population Euler meshes;
(b) cap/mesh-uniform subGaussian coordinate bounds for the four incoming
fields C,q^3,q^2,q^1, including the actual matrix-reuse responses;
(c) a common affine comparison whose endpoint is g_0(S)=3/2, and
|g_R(S)-3/2|<1/4;
(d) a coupled preactivation discrepancy no larger than E_z in L2 for
every time, sample and layer, with E_z <= sqrt(eta_*)/2.

For example the new affine certificate gives E_z <= H e M^13 with its
sharper propagator, or the conservative H e M^18. Either is covered by
the old e <= c_poly delta^10 because M^100 <= 76^20 delta^-10 < H delta^-10
and c_poly <= 10^-70 H^-400. No new amplitude restriction is imposed by
this note. All statements are at fixed depth four and fixed dataset.

At a fixed cap the maps satisfy |phi'| <= 2, |phi''| <= e,
|D(z,q)| <= 2|q|, |D_q| <= 2, |D_z| <= 2eR, and linear growth.
Consequently the finite-program conditioning theorem for finitely many
independent Gaussian matrices applies to all three matrices and both
orientations. Singularity of a finite source covariance is handled by
its independent-query regularization; named source coordinates remain
distinct. The canonical action construction uses four L2 spaces and
three adjacent initialized actions. Finite normalized transpose
identities on a countable generated dense probe set give their actual
adjoints, and the finite operator-norm event supplies bounded extensions.
None of this requires coordinate pairing between different layers.

At a fixed cap the gate bounds above, bounded actions and rank-one
product inequalities make the raw Hilbert vector field locally Lipschitz
on each primal ball. The common initialized actions are fixed; their
learned increments belong to the Hilbert--Schmidt class. Picard iteration
therefore gives local strong solutions. The uniform Euler ball and its
strict slack, combined with the width-independent stopped Euler estimate,
continue each capped solution through S and give its strong raw Euler
limit. Thus that existence is a consequence of (a), not an extra unproved
strong-limit premise.

## 2. An improved affine variance bound retains the old eta_*

The following elementary argument works for every fixed finite depth.
Use the normalized active affine gradient system with initial active
root p_0 having independent N(0,1) coordinates, independent initial
square Gaussian matrices A_2,...,A_L, and initial readout zero. Let
x_1=p and x_l=A_l...A_2 p. Positive time-step Euler updates are

    theta_{k+1}=theta_k+h_k grad F(theta_k),
    F=<D,A_L...A_2 p>_n,

with the appropriate raw metric factors. Every coordinate of grad F is
a polynomial with nonnegative scalar coefficients in the current
coordinates. Transposition, summation and the positive powers of n^-1
do not change that fact. Induction in k proves that each coordinate of
x_l(k) is a polynomial with nonnegative coefficients in the independent
centered Gaussian initialization entries. It contains its initial
chain polynomial x_l(0) with its unchanged positive coefficient.
Write x_l(k)=x_l(0)+P_l,k; P_l,k likewise has nonnegative coefficients.
Every Gaussian monomial expectation is nonnegative: an odd exponent
makes it zero, and otherwise it is a product of positive even moments.
Therefore, at each width and every fixed positive mesh,

    E ||x_l(k)||_n^2 >= E ||x_l(0)||_n^2 = 1.             (2.1)

The last equality follows successively by conditioning on each fresh
Gaussian matrix. This assertion concerns the normalized active affine
comparison, whose readout is defined to start at zero, not a change to
the target finite model's random readout.

Here passage to the population is justified at the fixed mesh. A finite
Euler program has finite polynomial degree. Its normalized norms are
bounded by a fixed polynomial in the initial Gaussian operator norms
and normalized root norms. These have width-uniform moments of every
fixed finite order (the elementary Gaussian net tail gives the former).
Hence the relevant second moments are uniformly integrable. The finite
source law, followed by the strong affine Euler limit, passes (2.1) to

    ||x_l(s)||_2^2 >= 1 for every s in [0,S].             (2.2)

The inactive root is independent of the active root and initial
matrices. Its learned matrix-chain correction has bounded ordinary
Frobenius norm at each fixed mesh, so its normalized conditional
second moment is O(1/n). Telescoping A_l...A_2 minus its initial product
shows that the inactive field stays equal to its initial chain; the
same conditioning shows zero active/inactive inner products. This is
the same finite-rank freezing proof with l-1 factors, here at most three.

The affine coordinate source program is linear in its Gaussian sources
with deterministic coefficients, so each affine preactivation remains
centered Gaussian. If v=(1+y_1 y_2 rho)/2, its marginal variance is

    Var Z_i^l(s)=a^(2(l-1))[v ||x_l(s)||_2^2+(1-v)].     (2.3)

Consequently Var Z_i^l >= a^(2(l-1)) >= 1/64 for l<=4. In particular the
old lower variance 1/404 remains valid at L4. This positivity argument
is stronger than a separate small/large-readout case bound and removes
any need to replace the old nonaffinity margin.

For clarity, write R(Z)=inf_{alpha,beta} E[atan Z-alpha-beta Z]^2.
The third-Hermite certificate gives, for sigma>=1/sqrt(404),

    R(sigma G) >= eta_* := 4*404*exp(-1)/(27*pi*405^4).  (2.4)

One can check its uniformity without a compact upper variance bound:
Gaussian integration by parts gives

 E[atan(sigma G)(G^3-3G)]
       = -2 sigma^3 E[G^2/(1+sigma^2 G^2)^2].

After substituting u=sigma G, the absolute value is an integral of the
nonnegative function 2u^2/(1+u^2)^2 against exp[-u^2/(2sigma^2)]/sqrt(2pi),
so it is increasing in sigma. At sigma=1/sqrt(404), restrict the original
Gaussian integral to |G|<=1, use its density lower bound exp(-1/2)/sqrt(2pi),
and E[(G^3-3G)^2]=6. This yields precisely (2.4).

For any square-integrable real Z, an optimal regression slope for atan Z
belongs to [0,1]: the independent-copy covariance formula and
0 <= (atan u-atan v)/(u-v) <= 1 prove this, with slope zero admissible
when Var Z=0. For each such slope, z -> atan z-beta z is 1-Lipschitz.
Taking infima over intercepts and these slopes in the triangle inequality
therefore gives, for any coupling,

    |sqrt(R(Z))-sqrt(R(Z_0))| <= ||Z-Z_0||_2.           (2.5)

Premise (d) now gives R(Z_i^l)>=eta_*/4. Absorbing the linear activation
part into the affine approximant proves

 inf_{alpha,beta} E[phi(Z_i^l)-alpha-beta Z_i^l]^2
                 >= e^2 eta_*/4 > 0                 (2.6)

for every sample, layer and feature time. This persists under the strong
cap limit, and therefore at every finite physical time.

## 3. Strong cap removal, uniqueness and reached-state restart

Let X_R denote a capped state and let X_A be a state with cap R'>=R,
allowing the uncut gate R'=infinity. On a common bounded primal ball,
forward expansion through four layers gives

    sum_{l,i} ||Z_A^l-Z_R^l||_2 <= K_b ||X_A-X_R||_raw.

The exact asymmetric gate decomposition has the bound

 ||D_{R'}(Z_A,q_A)-D_R(Z_R,q_R)||_2
 <= 2||q_A-q_R||_2 + 2eR||Z_A-Z_R||_2
               +2e || |q_R| 1_{|q_R|>R} ||_2.         (3.1)

For the top incoming field q^4=C, start with ||Delta C||_2. At every
lower incoming field,

 ||Delta q^l||_2 <= ||A_{l+1,A}||op ||Delta delta^{l+1}||_2
                  +||Delta A_{l+1}||HS ||delta_R^{l+1}||_2.

Inserting (3.1) successively for l=4,3,2,1 gives

 ||V_{R'}(X_A)-V_R(X_R)||raw
 <= K_b(1+eR)||X_A-X_R||raw
       +K_b e sum_{Q=C,q^3,q^2,q^1} || |Q_R|1_{|Q_R|>R} ||_2. (3.2)

There is only one R factor. The R coefficient multiplies the forward
state discrepancy, already bounded before the reverse induction; a
reverse discrepancy is multiplied by at most twice a bounded action.
The rank-one update comparison adds finitely many product inequalities
and no additional R factor. All these inequalities hold equally in the
finite normalized model.

The source premise gives the reference tails K exp(-cR^2). Gronwall
and a strict stopping margin imply

 sup_{s<=S} ||X_{R'}(s)-X_R(s)||raw
       <= K exp[K(1+eR)S-cR^2] -> 0.                  (3.3)

The same estimate (3.2) gives convergence of raw directions. Hence the
limit is a strong C1 path solving the uncut equations on [0,S]. It is
autonomous because its direction is the uncut raw field at its state.
No arbitrary-state L2 local-Lipschitz claim for the uncut gate is needed.

For an arbitrary bounded-primal uncut strong competitor on the same
action spaces, apply (3.2) with that competitor as A and the constructed
cap path as reference. Only the latter needs tails. With identical
initial states (3.3) gives equality as R goes to infinity. For physical
solutions retain each state's two separate residuals: their difference
is Lipschitz on the primal ball, and the same bound becomes (3.2) with a
larger K_{b,T}. Therefore uniqueness includes nonsymmetric competitors.
Starting this argument at a reached time proves uniqueness of restart;
existence of that restart is supplied by the already constructed path.
This asserts existence from reached states, not from arbitrary L2 states.

## 4. Scalar symmetry, global physical time and the loss rate

Because phi and every cap are odd in the required variables, replacing
(x_i,y_i) by (y_i x_i,1) is an exact raw loss identity, at every finite
width. An orthogonal input reflection exchanges the two folded inputs.
The Gaussian initialization and every finite Euler program are equivariant
under that reflection. Limiting scalar contractions are deterministic,
so both folded population predictions agree. This proves, for the
constructed cap paths and their strong limit,

    f_i=y_i g,  g=(1/2)sum_i y_i f_i,  loss=(1-g)^2.

This argument establishes symmetry before invoking uncut uniqueness.
With p_i=y_i/2, feature time uses Theta'=grad g in the uncut case and
the capped feature field V_R otherwise. The exact physical field on
these symmetric paths is 2(1-g)V_R, with both original residuals retained.

For each cap and the uncut path, g(0)=0 and g(S)>5/4 by premise (c).
Let s_* be the first hit of one. On [0,s_*) one has g<1. Boundedness of
g' on [0,S] implies 1-g(s) <= K(s_*-s). Thus

    t(s)=integral_0^s du/[2(1-g(u))] -> infinity

as s increases to s_*. Its inverse defines the physical path for every
finite t and solves ds/dt=2(1-g). No monotonicity of the capped g is used.
All physical times inherit the compact feature-interval primal and tail
bounds. This constructs global strong C1 physical solutions.

For the uncut path one also obtains a quantitative rate. Write H(theta)
=sum_i p_i h_i^4, so g=<C,H>. Let J be its bounded hidden directional
linearization along the strong path. The trajectory chain rule is valid
in L2 because phi' is bounded and continuous; its product with a fixed
L2 factor is continuous by truncation. Actual adjoints give

    C'=H,  hidden_theta'=J* C,  C''=J J* C.

Consequently ||C|| is convex (differentiate sqrt(||C||^2+epsilon^2) and
let epsilon decrease to zero), and its initial right slope is ||H_0||.
Thus ||H||>=||H_0|| and g'=||grad g||raw^2>=kappa_0:=||H_0||^2.
Initialized forward Grams satisfy q_l +/- c_l >= a^2(q_{l-1}+/-c_{l-1}),
by oddness and phi'>=a. At L4 this gives

    kappa_0=(q_4+y_1y_2 c_4)/2 >= a^8 delta/2.

Differentiating the physical loss yields

    loss(t) <= exp(-4 kappa_0 t) <= exp(-2 a^8 delta t). (4.1)

For all a in [1/2,1], the common rate is delta/128. For the requested
convex mixture a=1-theta with theta<=c_poly<=1/4, one has a>=3/4 and
2a^8>1/32, so the old loss bound exp(-delta t/32) remains valid at L4.
The compact-gain theorem and the near-identity convex specialization
must not be conflated when quoting this numerical rate.

## 5. Every initial hidden block and every sample-layer accelerates

This part only needs e>0, |rho|<1 and the constructed regular path.
At initialization every feature Gram is positive definite: a zero
linear combination of phi(U),phi(V) for a nondegenerate Gaussian pair
would hold at every real pair by full support and continuity, and
separate differentiation contradicts phi'>0. Induction through all
three fresh forward matrices proves this at all four hidden layers.

Put D_i^l=phi'(Z_i^l(0)), H_0=sum_i p_i h_i^4(0), and

    beta_i^4=H_0 D_i^4,
    beta_i^l=D_i^l A_{l+1,0}* beta_i^{l+1}, l=3,2,1,
    S_l=E_l[beta^l (beta^l)^T].

First S_4 is positive definite. A null vector u would give everywhere

 [p_1 phi(z_1)+p_2 phi(z_2)] [u_1 phi'(z_1)+u_2 phi'(z_2)]=0.

For fixed z_2 the first factor has at most one zero in z_1. Continuity
forces the second factor to vanish for every pair; differentiating in
z_1 and using phi'' not identically zero gives u_1=0, then u_2=0.

The three complete initialization transpose identities are, successively,

 A_{l+1,0}* beta_i^{l+1}
   =G_i^l+sum_j h_j^l(0) T^{l+1}_{ij},
 T^{l+1}_{ij}=E_{l+1}[partial_{xi_j^{l+1}} beta_i^{l+1}],
 Cov(G^l)=S_{l+1},  l=3,2,1.                          (5.1)

G^l is independent of the local initialized forward pair. Its covariance
is the full second moment S_{l+1}, not a residual covariance after
regression on forward features. Named Gaussian arguments, deterministic
response coefficients and covariance parameters are frozen in the formal
derivative. In particular at both middle populations the derivative
includes the actual h^{l+1}-dependence of the already present response
term. Products in this fixed finite initialization transcript can be
smoothly truncated first; Gaussian moments and bounded activation
derivatives justify their removal. The generic finite conditioning law
therefore proves (5.1) for the actual reused matrix, not a fresh surrogate.

Conditionally on the local forward pair,

 Cov(beta^l | Z^l)=diag(D^l) S_{l+1} diag(D^l)
                   >= a^2 lambda_min(S_{l+1}) I.

Induction proves S_3,S_2,S_1 positive definite. Define hidden raw blocks

 V^1=(1/d)sum_i p_i beta_i^1 x_i,
 V^l=sum_i p_i beta_i^l tensor h_i^{l-1}(0), l=2,3,4.

If F_{l-1} is the preceding feature Gram, then

 ||V^l||HS^2=tr(S_l diag(p) F_{l-1} diag(p))>0.

At the first layer the same identity uses the input Gram Gamma and the
raw factor d. Both matrices are positive definite, so every hidden raw
block is nonzero. No input covariance inverse is used.

The strong backward equations and bounded gates give

 C(s)=sH_0+o_L2(s),  b_i^l(s)=s beta_i^l+o_L2(s).

Thus the hidden state satisfies

 hidden_theta(s)=hidden_theta(0)+(s^2/2)V+o_raw(s^2).    (5.2)

Let U_i^l denote its corresponding preactivation acceleration. The
forward recurrence is

 U_i^1=sum_j Gamma_ij p_j beta_j^1,
 U_i^l=V^l h_i^{l-1}(0)+A_{l,0}(D_i^{l-1} U_i^{l-1}).

Adjunction and the beta recursion give, successively for every l,

 sum_i p_i <beta_i^l,U_i^l>_l
                   =sum_{j=1}^l ||V^j||raw^2 > 0.     (5.3)

Hence some sample accelerates in each layer. After label folding the
input reflection exchanges the samples and preserves the objective and
initial law; it therefore equates their squared acceleration norms.
In the original label sectors multiplying a field by y_i does not alter
its norm. Both sample accelerations are nonzero. Since D_i^l>=a, each
feature acceleration D_i^l U_i^l is nonzero too.

Writing V=J_0*H_0, equation (5.2) and the trajectory chain rule give

 H(s)=H_0+(s^2/2)J_0 V+o_L2(s^2),
 kappa_readout(s)=kappa_0+s^2||V||raw^2+o(s^2),
 kappa_total(s)=kappa_0+2s^2||V||raw^2+o(s^2).           (5.4)

The hidden projected kernels contribute the other s^2||V||^2 term.
Since s'(0)=2, physical hidden block and sample preactivation/feature
accelerations are respectively 4V,4U_i^l,4D_i^l U_i^l, and

 kappa_total(t)=kappa_0+8t^2||V||raw^2+o(t^2).

The readout has physical initial velocity 2H_0 and physical initial
acceleration -4 kappa_0 H_0, both nonzero. These are block and sample
statements, not claims that every scalar parameter coordinate moves or
that velocity stays nonzero at every later time.

## 6. Finite GF, simultaneous raw GD, all five kernels and path laws

At any fixed cap and fixed physical mesh the Gaussian conditioning law
applies to a finite transcript with all three matrices and both actual
residuals. Exact rank-one unrolling bounds each current action by its
initialized norm plus the sum of products of the update-factor RMS
norms; adding the third matrix adds precisely one such finite sum.
A larger primal ball with slack contains the coarse finite references
with probability tending to one. On this ball the capped raw field is
bounded and Lipschitz with constants independent of width. Its Euler
local defect is at most KM h^2/2; stopped Gronwall removes the auxiliary
mesh and identifies fixed-cap finite GF.

The finite form of (3.2) compares genuine uncut GF to this same-width cap
reference. Send width to infinity at a fixed cap, transfer its reference
tail norms by the fixed-cap law, then send the cap to infinity. The
Gaussian tail defeats exp(K_T R), and the strict stopping margin excludes
exit. At any fixed width GF itself cannot have a finite-time raw-norm
blowup: the loss identity bounds integral ||dot theta||raw^2 by its
initial loss, and Cauchy--Schwarz bounds finite-time raw displacement.
Local smooth finite-dimensional existence then continues it.

For genuine raw GD the interpolant direction is the uncut field at the
preceding node. Comparing to the fixed-cap reference incurs an additional
K_{R,T} eta_n, uniformly in width, and eta_n=n^-2 tends to zero. This
uses the exact five raw blocks and does not replace the algorithm by a
scalar clock or a different metric. It also avoids invoking a Gaussian
conditioning theorem for a growing transcript. The initialized finite
readout remains iid N(0,n^-2); its normalized RMS is O_P(n^-1), so the
fixed-program stability limit is the zero population readout. These
arguments use the full width sequence in probability.

The five raw kernel contributions, including all off-diagonal entries,
are now

 K^1_ij=Gamma_ij <b_i^1,b_j^1>_1,
 K^l_ij=<b_i^l,b_j^l>_l <h_i^{l-1},h_j^{l-1}>_{l-1}, l=2,3,4,
 K^5_ij=<h_i^4,h_j^4>_4.

They, predictions and loss converge uniformly on each fixed [0,T] by
products of the converging L2 fields and the bounded-action comparisons.
Both initialized and trained orientations on their generated probes
are retained. No cross-width operator-norm convergence is asserted.

For completeness the extra velocity layer does not require an unproved
Lp bound for an initialized Gaussian action. At fixed cap, primary
source response rows obey the same nonlinear independent-Gaussian probe
bound Kh_j for past slots and K for current slots. This follows from
capped raw Lipschitz stability with an inserted Gaussian answer, followed
by Gaussian integration by parts with all contractions frozen. The
all-index derivative seminorm R(F)=sum_eta |partial_eta F| obeys the
four-layer causal inequalities

 R(Z^l_k) <= 1+K sum_{j<k}h_j R(delta^l_j),
 R(C_k) <= K sum_{j<k}h_j R(H^4_j),
 R(q^l_k) <= 1+K R(H^l_k)+K sum_{j<k}h_j R(H^l_j),
 R(H^l_k) <= 2 R(Z^l_k),
 R(delta^l_k) <= 2eR R(Z^l_k)+2 R(q^l_k),

with the evident root adjustment at l=1 and q^4=C. Taking the maximum
of the forward seminorms and C, substituting the reverse inequalities,
and exchanging the two strict sums gives U_k<=K+K sum_{j<k}h_j U_j.
Discrete Gronwall gives a mesh-uniform pathwise bound on every primary
derivative row. The same inequalities with Lp norms give primary
moments K sqrt(p). Constants here may depend on the fixed cap and T.

Write P^l=dot Z^l and U^l=phi'(Z^l)P^l. The exact recursions are

 P^1=dot w x,
 P^l=dot A_l H^{l-1}+A_l U^{l-1}, l=2,3,4.

Append observations after the complete primary transcript, in the order
A_{2,0}U^1, A_{3,0}U^2, A_{4,0}U^3; add learned increments explicitly.
These queries do not feed back into training. At each layer the initial
action source is a Gaussian gamma^l with variance E|U^{l-1}|^2, with its
full cross moments with earlier forward queries, plus the actual formal
response-weighted old reverse inputs. The new gamma^l is a separate named
forward argument, so its formal reverse-source derivatives vanish.

Inductively P^{l-1} has bounded Lp moments and its needed local reverse
source derivative row has finite expected absolute sum. Then

 partial_eta U^{l-1}
 =phi''(Z^{l-1})P^{l-1} partial_eta Z^{l-1}
                     +phi'(Z^{l-1}) partial_eta P^{l-1}

has bounded expected row sum by the primary pathwise bound. Thus the new
response row is bounded. Its scalar formula expresses P^l as a Gaussian
source plus a bounded deterministic row of primary delta fields and
rank-update terms whose scalar contractions are bounded. Hence P^l has
Lp norm K sqrt(p). Its local reverse-source derivatives are bounded by
the primary derivative row, because its response coefficients and named
new gamma^l are frozen. This closes the induction through the third
observational query. In particular node fourth moments are bounded at
each fixed cap uniformly in the auxiliary mesh.

To apply the original bounded-derivative conditioning theorem rigorously,
first use phi'(Z) tau_M(P) in each query. Its first derivatives are bounded
at fixed M. Remove the query clips in layer order using the bounded
initialized L2 actions, the just-derived derivative-row domination, and
Gaussian covariance square-root continuity. Expected source derivatives
converge by dominated convergence, including at singular source laws.
For a later query keep its outer clip fixed while removing earlier inner
clips, then remove that outer clip. This proves the asserted joint W2
laws for all three observations without assuming Lp boundedness of a
Gaussian operator or applying the theorem directly to unbounded products.

Finally the deterministic four-layer product-rule comparison is

 ||velocity_A-velocity_B||sum,2
 <= K[d_1+(1+M)d_0+sum_{l,i}||(|P^l_{B,i}|-M)_+||_2],  (6.1)

where d_0,d_1 are raw state and raw direction differences. At a gate
product split phi'(Z_A)P_A-phi'(Z_B)P_B into its bounded-gate difference
in P and a gate difference times P_B; truncate only that reference P_B.
Every layer adds one M d_0 term and propagates earlier errors through
bounded actions. It never multiplies two M factors.

The uncut population velocity is L2-continuous by the trajectory chain
rule and has compact L2 time image. Its positive-part L2 tails vanish
uniformly: that tail map is 1-Lipschitz, and a finite L2 net reduces the
claim to finitely many fixed variables. Apply (6.1) first to cap versus
uncut population paths, sending cap to infinity at fixed M and then M
to infinity. For finite paths take width first at fixed cap and M, then
the cap limit at fixed M, then the final M limit. This proves uniform-time
joint same-layer W2 velocity laws and joint W2 laws at any fixed finite
set of times, including second moments and integrated squared speeds.
No control of the growth of cap-dependent fourth-moment constants is
required. GD uses the actual recomputed hidden fields along the raw
interpolant, right derivatives at nodes and terminal-left derivatives.

For each layer the joint two-sample preactivation/feature path law lies
in W2(C([0,T];R^4)) with the supremum norm. To obtain it, use fixed-grid
joint W2 convergence and

 ||x-I_h x||_infinity^2 <= 4h integral_0^T |x'(t)|^2 dt.

Average this inequality over neurons and use the established integrated
speed bounds, then send the grid size to zero. This is a same-layer path
law, not an across-layer neuron coupling or a continuous-path velocity
law. Every convergence assertion fixes the dataset, finite depth four,
and finite physical horizon before sending width to infinity.

## 7. Audit conclusion

With the quantitative four-layer source/affine premises in Section 1,
all remaining requested L4 conclusions follow without changing c_poly,
the exponent ten, or the old eta_* nonaffinity margin. The requested
convex family also retains the old exp(-delta t/32) loss bound. For the
full gain interval the safe uniform rate is instead exp(-delta t/128).

No new four-layer endpoint, initial-motion, finite-conditioning, cap,
velocity or topology obstruction was found. This is a bounded component
proof; it is not an independent final audit of the separate quantitative
source supersolution and its exponent arithmetic. In particular it
provides no common admissible activation coefficient for every finite
depth. Vanishing initial kernels/regression margins with depth would
exclude depth-uniform positive numerical bounds, but would not refute
that distinct common-coefficient qualitative theorem.
