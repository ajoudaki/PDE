# One odd nonlinear activation for three samples at every finite depth

2026-09-08. This theorem permits an overall gain. It is not a theorem for
the unit-sum convex mixture. The gain exponent below is sufficient; its
optimality and its conservative numerical prefactor are not claimed.

## 1. Model and statement

Let 0<delta<=1. Fix three inputs x_i in R^d with ||x_i||²=d,
Gamma_ij=x_i^T x_j/d, and |Gamma_ij|<=1-delta for i!=j. Labels y_i are
arbitrary elements of {-1,1}. Let L>=2 be any fixed finite hidden depth.
Use independent Gaussian initialization

    W^1_jk ~ N(0,1/d), W^ell_jk ~ N(0,1/n) (2<=ell<=L),
    C_j ~ N(0,n^-2).

The network is z_i^1=W^1 x_i, h_i^ell=phi(z_i^ell),
z_i^ell=W^ell h_i^(ell-1), f_i=<C,h_i^L>_n, where <u,v>_n=u^Tv/n.
The loss is E=||f-y||²/2. The raw metric is

    (d/n)||Delta W^1||_F² + sum_(ell=2)^L ||Delta W^ell||_F²
      + ||Delta C||_n².

Both GF and simultaneous raw GD with physical step n^-2 train every
block in this metric. GD interpolates raw parameters linearly and
recomputes hidden fields from those interpolated parameters.

Define the absolute constants and the activation

    eta0 = 1/(108*pi*exp(1)),
    lambda = eta0*delta²/3 = delta²/(324*pi*exp(1)),
    a_delta = 10^10/lambda = 324*pi*exp(1)*10^10*delta^-2,
    phi_delta(z) = a_delta*(z+atan z).                         (1)

The same a_delta and the same activation are used at all hidden layers,
and for every L>=2. In particular there is no small nonlinear-to-linear
coefficient ratio: the ratio is one.

**Theorem.** In the canonical population construction associated with
this finite Gaussian initialization, (1) has the following properties.

1. A global strong C^1 raw-Hilbert GF exists. It is unique among strong
   solutions with bounded primal quantities on compact intervals, without
   sample symmetry restrictions. Continuation from any reached state is
   unique in that class.
2. Its loss satisfies, for every t>=0,

       E(t) <= (3/2) exp[-lambda*a_delta^(2L)*t].             (2)

3. For every fixed finite dataset, L and physical horizon, finite GF and
   the stated raw GD converge along the full width sequence in probability
   to this same population flow. This includes predictions, loss, all L+1
   true raw kernel blocks, same-layer hidden paths in W2 with the uniform
   path norm, uniformly-in-time joint hidden-state/velocity laws in W2,
   joint laws at finitely many times, second moments, integrated squared
   speeds, and fixed finite generated probes using either orientation of
   the adjacent actions. The initialized actions have genuine adjoints;
   learned increments are Hilbert--Schmidt. No cross-width operator-norm
   convergence is asserted.
4. For every sample i and hidden layer ell,

       inf_(t>=0) inf_(alpha,beta in R)
       E[phi_delta(z_i^ell(t))-alpha-beta*z_i^ell(t)]²
                    >= a_delta²*eta0/4 > 0.                 (3)

   Every hidden block and every sample's preactivation and feature field
   has a nonzero initial right second derivative. The initial hidden
   first derivatives are zero. For p=y/3 and the sum K of all raw kernel
   blocks,

       p^T K(t)p = p^T K(0)p + 18*t²*||V||_hidden²+o(t²),
       ||V||_hidden>0,                                      (4)

   with V defined in INITIAL_MOTION.md.

This is global population existence and fitting together with finite-width
convergence on each compact time interval. It makes no simultaneous
infinite-width/infinite-depth or infinite-time/width assertion. Assertion
(3) is an absolute regression gap; no depth-uniform relative fraction of
activation energy is asserted.

The proof uses cubic input features to obtain a depth-independent initial
Gram bound, large gain to keep the entire fitting path close to its own
nonlinear initialization, and a direct nonlinear source estimate to
construct that path. The normalization below changes neither the raw
metric nor the trained algorithm.

## 2. Exact normalization

Write a=a_delta and set

    Z_i^ell=z_i^ell/a^(ell-1), H_i^ell=h_i^ell/a^ell,
    K_ell=a^(ell-1),
    psi_ell(z)=z+K_ell^-1 atan(K_ell*z),
    F_i=<C,H_i^L>, so f_i=a^L F_i.                          (5)

The raw parameters, including the ORIGINAL readout C, are unchanged.
Then Z^ell=W^ell H^(ell-1), H^ell=psi_ell(Z^ell). At the bottom it is
convenient only notationally to write u_i=x_i/sqrt(d) and w=sqrt(d)W^1:
the bottom raw metric becomes its normalized L2 metric and Z_i^1=w.u_i.

For an auxiliary control c with ||c||_1<=3, use the raw gradient field
sum_i c_i grad F_i. Its backward recursion is

    q_i^L=C, d_i^ell=psi_ell'(Z_i^ell)q_i^ell,
    q_i^ell=(W^(ell+1))*d_i^(ell+1).

The update is C'=sum_i c_i H_i^L, each middle block has derivative
sum_i c_i d_i^ell tensor H_i^(ell-1), and w'=sum_i c_i d_i^1 u_i.
All blocks have the same raw metric. Since grad f_i=a^L grad F_i,
physical GF is exactly this control field with c_i=-r_i after the time
change s=a^L t. Equivalently, on the accumulated residual clock

    v(t)=a^L integral_0^t ||r(u)||_1 du,

the control is c=-r/||r||_1 and has norm one. At r=0 the physical field
vanishes; no differentiability of this normalized control is used.

The clipped auxiliary backward gates used in this proof are

    D_(ell,R)(z,q)=q+g(K_ell*z)tau_R(q), g(x)=(1+x²)^-1,

where tau_R is smooth, odd, 1-Lipschitz, equals q for |q|<=R and obeys
|tau_R(q)|<=min(|q|,2R). They satisfy

    |D|<=2|q|, |D_q|<=2, |D_z|<=K_ell|q|,
    |D_z|<=2K_ell R, 1<=psi_ell'<=2.                       (6)

For fixed L,a,R the clipped raw field is locally Lipschitz. These are
auxiliary layer-scaled clips; removing them recovers exactly (5) and the
original raw flow. The original finite random readout is retained in
both actual training algorithms; C(0)=0 refers to its population limit.

## 3. Uniform initialization geometry

Put s_delta=delta(2-delta). For each i!=j set

    v_ij=(u_i-Gamma_ij*u_j)/sqrt(1-Gamma_ij²).

The vectors have norm one, are perpendicular to u_j, and satisfy
u_i.v_ij>=sqrt(s_delta). For {i,j,k}={1,2,3}, the unit tensor
R_i=u_i tensor v_ij tensor v_ik pairs to zero with u_j^tensor3 and
u_k^tensor3, and pairs to at least s_delta with u_i^tensor3. Therefore
for T=sum_i c_i u_i^tensor3, |c_i|s_delta<=||T||. Sum the three squared
inequalities to obtain

    Gamma^(circ3) >= s_delta² I/3 >= delta² I/3.            (7)

This allows singular Gamma. For G standard Gaussian and H3(G)=G³-3G,
Gaussian integration by parts twice gives

    E[atan(sigma G)H3(G)]
       = -2sigma³ E[G²/(1+sigma²G²)²].                      (8)

The cubic coefficient b3(sigma) is (8)/sqrt(6). Substituting x=sigma G
and restricting the integral to |x|<=1, for every sigma>=1,

    |b3(sigma)|
       = (2/sqrt(12*pi)) integral_R
            x²/(1+x²)² exp[-x²/(2sigma²)] dx
       >= (2/sqrt(12*pi))*exp(-1/2)*(1/6),
    b3(sigma)² >= eta0.                                    (9)

Here the integral lower bound uses (1+x²)²<=4 and integral_-1^1 x²dx=2/3.
For sigma=1 the cubic chaos of psi_1(G)=G+atan G is b3(1)H3(G)/sqrt(6).
The remaining chaos is orthogonal across all three sample coordinates:
E[H3(Z_i)H3(Z_j)]/6=Gamma_ij³ and Gaussian conditional expectation gives
the same cubic projection coefficient for cross terms. Thus the first
normalized feature Gram obeys

    Q_1(0) >= b3(1)² Gamma^(circ3) >= lambda I.              (10)

At each next initialized layer the normalized Gaussian preactivation
triple has covariance Q_(ell-1)(0) and equal positive marginal variance
q. The linear Gaussian regression coefficient of psi_ell is

    c=E[Z psi_ell(Z)]/q >=1.

The residual is orthogonal to every coordinate of that Gaussian triple,
so Q_ell(0)>=c² Q_(ell-1)(0)>=Q_(ell-1)(0). Consequently

    Q_L(0)>=lambda I                                      (11)

for every L>=2, with the same lambda. In raw variables each initialized
preactivation has variance at least a^(2(ell-1)), hence at least one.

## 4. Explicit controlled primal bounds

Let

    T0=12/lambda, S=a^-L*T0, F=8^L.                        (12)

The source lemma in SOURCE_RESPONSE.md applies on this control interval
because

    a=10^10/lambda >=10^8(1+12/lambda).                      (13)

For completeness the independent primal estimates used here do not
assume source bounds or a clipped energy identity. The canonical
initialized action norms are at most 2, and it suffices to bound them
by 3. Finite initialized norms <=3 and first projection norms <=2 hold
with probability tending to one. Stop at hidden joint raw displacement
D=1. All current adjacent norms are then <=4 and bottom projection
norms <=3. Using (6),

    ||H_i^ell||_2<=8^ell, ||q_i^ell||_2<=8^(L-ell)||C||_2,
    ||C(v)||_2<=3Fv,
    D(v)<=3sqrt(L)F²v².                                    (14)

For instance each individual hidden block speed is bounded by F||C||
when ||c||_1<=3: 3*2*8^(L-ell)*8^(ell-1)<=F, with the same bound for the
bottom block. Summing squares over the L blocks and integrating C gives
an even smaller constant than in (14). On a positive Euler mesh use
sum_j h_j v_j<=v_k²/2. Thus the estimates exclude a first discrete
overshoot as well as a continuous first exit. The finite zero-readout
comparison program obeys them; for the actual finite C(0) its vanishing
initial norm is added until the fixed-cap bridge removes that error.

Telescoping each forward layer against its own initialized state gives

    ||Z_i^ell-Z_i^ell(0)||_2<=4*8^(ell-1)D,
    ||H_i^ell-H_i^ell(0)||_2<=8^ell D.                      (15)

Indeed the preactivation difference is at most
8^(ell-1)D+3*2 times the preceding preactivation difference; the displayed
bound is preserved by induction and holds at ell=1. With Q_L the
normalized top feature Gram, (14)-(15) yield

    ||Q_L-Q_L(0)||op <=6F²D
                    <=18sqrt(L) F^4 S².                    (16)

Let J_h be the true hidden differential of F=(F_1,F_2,F_3), and U_h,R
the clipped hidden direction map from coefficient vectors. Each
sample's hidden gradient has joint norm at most sqrt(L)F||C||. Since
there are three samples, both operator norms are <=sqrt(3L)F||C||,
and therefore

    ||J_h U_h,R||op <=3L F²||C||²
                    <=27L F^4 S².                         (17)

Finally, (15) and a>=1 give a bound in ORIGINAL preactivation coordinates:

    max_(i,ell) ||z_i^ell-z_i^ell(0)||_2
         <= a^(L-1)F D <=3sqrt(L)(512/a)^L T0²/a.            (18)

All these estimates are uniform in cap and apply to every control prefix.

Here is an explicit arithmetic check with comfortable slack, uniform in
L>=2. We have 0<lambda<1 and a=10^10/lambda. For 0<q<=1/4, the sequence
Lq^L decreases for L>=2, and sqrt(L)q^L<=Lq^L<=2q². Consequently

    18sqrt(L)(4096/a²)^L T0²
       <=36*(4096/a²)²*(144/lambda²) <lambda/4,
    27L(4096/a²)^L T0²
       <=54*(4096/a²)²*(144/lambda²) <lambda/4,
    3sqrt(L)(64/a²)^L T0² <1/4,
    3sqrt(L)(512/a)^L T0²/a
       <=6*(512/a)²*(144/lambda²)/a <sqrt(eta0)/2.            (19)

For example the largest numerator in the first two lines is less than
1.4*10^11, whereas a^4*lambda²=10^40/lambda². The last line is at most
3*10^8*lambda/10^30. These inequalities also verify the stopped primal
ball premise with strict slack. By (11), (16), (17),

    Q_L >=3lambda I/4, ||J_h U_h,R||op<=lambda/4.            (20)

## 5. Global fitting for clipped flows and the nonlinear source estimate

The clipped physical raw direction is -a^L times the normalized update
field with coefficients r. Differentiating the actual predictions
f=a^L F along that direction gives exactly

    rdot=-a^(2L)(Q_L+J_h U_h,R)r.                           (21)

The hidden contribution need not be symmetric or positive. Its absolute
operator bound in (20) is enough. Before v(t) reaches S,

    (d/dt)||r||² <= -lambda*a^(2L)||r||²,
    ||r(t)||<=sqrt(3)exp[-lambda*a^(2L)t/2],
    v(t)<=a^L*sqrt(3) integral_0^infinity ||r(t)||dt
         <=6/(lambda*a^L)=S/2.                             (22)

Thus the controlled-budget stop cannot occur. Bounded clipped raw
speeds give a strongly Cauchy endpoint at any finite maximal physical
time; local Lipschitz existence from that endpoint continues the path.
Every clipped population flow is global. This did not assign the true
loss-energy identity to a clipped update.

The key new analytic estimate is proved in SOURCE_RESPONSE.md. In the
normalization (5), with F=8^L, it constructs the ACTUAL strict forward
response densities and causal backward rows on every positive mesh,
uniformly in the incoming-field caps. Its constants obey

    alpha_ell=32^ell*3F²,
    b_ell=2048^(L-ell+1)B0, B0<=4F*T0/a,
    alpha_ell S b_ell
       <=24576*(1048576/a)^L*64^-ell*T0²/a.                 (23)

Condition (13) makes the last product <10^-10 and the associated
random derivative exponential parameter <10^-8 at every layer and
every finite depth. The crucial estimate retains actual Gaussian
covariances and current transpose returns: at the SAME source arrays,
the Gaussian part of q_ell has scale controlled by its already proved
raw L2 scale plus b_ell/K_ell. The bounded forward nonlinear remainder
atan(K_ell Z)/K_ell compensates the curvature K_ell. Strict production
then improves each coefficient radius, rather than assuming it remains
bounded. The proof supplies full local identities and constants.

Rewriting a fine physical Euler mesh by h_j=a^L Delta t_j||r_j||_1 and
c_j=-r_j/||r_j||_1 reproduces its normalized clipped updates. Freeze
these deterministic causal contractions in named-source derivatives.
The strict budget S/2 and fixed-cap Euler convergence imply sum h_j<S
on sufficiently fine meshes on each physical horizon. The source
lemma therefore yields, for fixed L,a, constants M,c>0 independent of
physical time and cap, for all normalized incoming fields Q,

    sup_(R,t) ||Q_R(t)||_p<=M sqrt(p), p>=2,
    sup_(R,t) ||Q_R(t)1_(|Q_R(t)|>u)||_2<=M exp(-cu²).       (24)

No temporal independence and no random time-maximum bound is used.

## 6. Global population and finite-algorithm bridges

POPULATION_LIMITS.md states the finite-depth bridge precisely and checks
its hypotheses here. Its local source is the finite adaptive Gaussian
conditioning construction in the existing self-contained manuscript,
foundations.md, together with the fully derived cap/velocity/path
arguments in velocity.md. Those arguments handle finitely many named
independent matrices by induction, and apply to the layer-dependent
bounded-derivative psi_ell in (5). The following are the substantive
verification steps, not additional assumptions.

* Finite clipped programs have bounded C^1 coordinate derivatives,
  deterministic causal scalar contractions, finitely many independent
  Gaussian matrices used in both orientations, and the required
  singular-query regularization. They give common L2 layer spaces,
  bounded initialized actions and genuine adjoints. Their learned
  rank-one integrals are Hilbert--Schmidt.
* (14), (19), (22) give global clipped reference paths, compact-time
  bounds and strict continuation slack. (23)-(24) give the cap-independent
  tails required for removal. The one-sided gate comparison has one
  factor R, not R^L, and uses tails of the reference only. Its error is
  C_T exp(C_T R-cR²). Hence clipped paths and their raw velocities are
  uniformly Cauchy in the raw Hilbert norm on each compact interval.
* The same comparison against any bounded-primal uncut competitor proves
  uniqueness and reached-state restart, with its own residual vector.
  No folding/exchange symmetry, positive input-Gram assumption or
  affine fitting clock is used.
* At fixed cap, coarse-mesh fixed-program width convergence and
  width-independent raw Euler stability give the finite GF/GD limits.
  The independent finite random readout has RMS O_P(n^-1), which is
  retained before this comparison. Ordered truncations for each appended
  true-backward and velocity product give the true raw kernels and
  velocity laws. State/velocity compactness and integrated speed bounds
  give the path laws. All iteration counts are finite once L and the
  observation horizon are fixed.

Taking the strong cap limit in (22) proves (2). The limiting vector
field is the actual raw gradient by the scalar predictor differential
and genuine adjunction, so its exact energy identity also holds.
POPULATION_LIMITS.md spells out the estimates, observation definitions
and the order of limits; no different training scheme is substituted.

## 7. Absolute nonaffinity and initial motion

For a square-integrable real X, write

    R(X)=inf_(alpha,beta) E[atan X-alpha-beta X]².

Every optimal regression slope can be chosen in [0,1]. When Var(X)>0,
this follows from the independent-copy identity for covariance and
0<=(atan x-atan y)/(x-y)<=1; when Var(X)=0 choose slope zero. If b is
such a slope at Y, the function atan x-bx is 1-Lipschitz, and testing
Y's optimal affine predictor at X shows

    sqrt(R(X)) <= sqrt(R(Y))+||X-Y||_2.

Interchanging X and Y proves that sqrt(R) is 1-Lipschitz under L2
coupling. By the cubic test (8)-(9), R(sigma G)>=eta0 for every sigma>=1.
Combine the initialized variances after (11) with (18)-(19) to get
R(z_i^ell(t))>=eta0/4, first for every clipped path and then for its
strong limit. Absorbing the linear a*z into the free affine predictor
gives (3).

INITIAL_MOTION.md proves (4) and all individual initial-motion claims
by induction on initialized Gaussian queries. Positive top feature
Gram and the nonconstant positive activation derivative give a positive
definite top backward Gram. Actual transpose returns preserve a fresh
positive Gaussian covariance at every lower layer. Each new forward
acceleration query has a Gaussian innovation orthogonal to the original
forward features, of strictly positive variance; it cannot cancel with
the current backward return. This supplies every sample's motion for
generic triples without permutation symmetry.

## 8. Scope and comparison with the convex mixture

Excluding rho=-1 removes the direct antipodal oddness obstruction.
It does not imply positive input-Gram eigenvalues for three inputs:
three planar unit vectors at angles 120 degrees still sum to zero.
Nevertheless (7)-(10) show that their nonlinear initialized features
are independent. There is no counterexample here to the positive odd
convex mixture.

The new theorem uses a second device: a large overall gain. In (1),
phi_delta=2a_delta*[(1/2)z+(1/2)atan z]. Dividing by 2a_delta changes
the hidden features at every layer and changes their raw gradient
dynamics. Thus the theorem neither establishes an energy-normalized
activation nor proves a threshold for the exact unit-sum mixture.

The power delta^-2 in the sufficient gain is derived explicitly, uniformly
over all fixed finite depths. No matching necessary gain lower bound is
proved; the initialized cubic separation scale delta² is a different
claim whose sharpness does not establish gain optimality. A numerical
prefactor of approximately 2.77*10^13 in (1) is deliberately conservative.
