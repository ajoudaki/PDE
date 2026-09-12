# C-H2 candidate: finite observable action blocks with current populations

Candidate proof, not yet internally checked or promoted. Author/assembler:
`/root`, task `01a0966c-d650-7512-91e9-5fd0298c2ad4`, 2026-09-12.
This construction was developed before comparing the isolated route reports.

## 1. Statement and dependency scope

Use precisely C.4.7.8's model (H1)–(H3), loss, mobilities, canonical Gaussian
initialization, two separate population expectations, and joint observation
alphabet. Fix Y>=1, T=1/200 and rho=delta/2, where delta is its fixed positive
radius (H3). Let U_rho={mu: W1(mu,nu*)<rho}, with normalized-input-plus-label
cost on sqrt(2) S1 × [-Y,Y]. These constants never depend on approximation
order. Lowercase fields below are aliases for the notation contract's typed
population fields. All times are physical unhalved-loss GF times.

**Candidate theorem.** The construction below gives an increasing sequence of
finite-type autonomous population systems, initialized from finite canonical
Gaussian observable programs. Each system is uniquely well posed through T
and restartable from its own saved current population state. For each
separately fixed mu in U_rho, its predictions converge uniformly in time and
on the whole input circle to canonical nonlinear population GF. Every
separately fixed finite admissible C-H1 same-layer joint observation tuple
converges uniformly in time in Euclidean W2, including frozen/current pairs,
both action directions, bounded-gate pushforwards and quadratic contractions.
No numerical accuracy or resource rate is asserted.

The full established dependency packet is `dependencies_v1.md`; every one
of its seven excerpts is still literally contained in the maintained source.
The frozen `candidate_v3.md` is byte-identical to maintained C.4.7.8. We use
III.F.1–7 for finite Gaussian laws/common actions, III.F.8–10 for HS and
scalar gradient calculus, C.4.7.1–5 for the actual GF with uniform tails, and
C.4.7.8 parts 2–3,5–6,8 for its observation language, initialized generated
space, invariance and fixed activity family. Their complete proofs, not an
arbitrary-formal-hierarchy uniqueness assertion, are the positive inputs.
Gaussian calculus §§6,7.2,10 are respected obstructions, not positive premises.

The proof first builds bounded initialized observable bases. It evolves two
current populations and a finite block of action contractions, derives uniform
energy bounds, and compares directly on the canonical carrier against the
already identified actual GF. Strong approximation of compact sets controls
the omitted action and learned-increment sources; the reference tail estimate
controls error propagation. No infinite formal hierarchy is solved.

## 2. A deterministic finite dictionary and its joint initialization

Consider C-H1's alphabet at initialization: w=g, c=0 and A=A0. Replace real
scalar marks by rational marks and use a fixed countable dense set of circle
directions (e.g. rational stereographic parametrizations plus the omitted
point). The seed z20(v) is expanded as A0 tanh(g·v). Enumerate all finite
correctly typed graphs causally, including constants, affine operations,
sin,cos,tanh, bounded products, and both actions on bounded operands.
A concrete increasing finite prefix at stage N consists of all graphs with
at most N nodes using the first N rational marks and first N circle marks,
closed under their finite dependencies. Use a fixed ordering by size and then
lexicographic instruction/parent/mark indices. Retain the bounded outputs on
each population; constants occur first. Duplicate outputs are harmless.

Let V_l,N be the real span of this finite bounded output list on population l.
These spaces are nested. Obtain an orthonormal basis b_l,1,...,b_l,d_l by
Gram–Schmidt in the fixed order: subtract previous orthogonal components;
skip a vector if its exact squared L2 residual is zero; otherwise divide by
the positive square root of that squared norm. Each basis member is a finite
real linear combination of bounded words, hence is bounded. Its explicit
supremum envelope follows by the triangle inequality from syntax and the
computed coefficients. The spaces/bases depend only on initialization and N,
not on mu, the target path, a time discretization, or width. Nesting can be
implemented by extending the preceding basis in the same enumeration order.
For definiteness a global causal list ordered by first admission stage is used
when extending; within a stage the preceding lexicographic rule resolves ties.

Write b_l for the column vector of basis functions and P_l,N for its L2
orthogonal projection. Record the two finite **joint** initial laws

  lambda_1,N = Law_1(b_1,g_1,g_2) on R^(d_1+2),
  lambda_2,N = Law_2(b_2) on R^d_2,

and the fixed contraction matrix

  D_N[i,j] = E_2[b_2,i (A0 b_1,j)].                         (1)

Compute all of these in one finite union of initialization programs, including
the calls A0 b_1,j and the reverse calls used inside the bases. The complete
rule is C-H1 (H6): each new oriented Gaussian source has the uncentered input
Gram as covariance, and its answer adds all earlier opposite-orientation
input fields times their expected frozen named-source derivative. Extend
singular Gaussian Grams by C-dagger and a nonnegative Schur complement as
proved there. Every integral here is a finite-dimensional Gaussian integral.
Gram–Schmidt is performed after those joint laws are computed; (1) uses the
same joint law, not an independently sampled second population coordinate.
The transpose D_N^T is the contraction matrix of the actual reverse action.
No independent reverse Gaussian matrix is introduced.

This is an exact-real population construction. It permits defined Gaussian
integrals and exact finite PSD linear algebra; no effective tolerance or
cost for nearly dependent bases is claimed. A floating prototype must expose
its rank tolerance and quadrature as additional approximations. They are not
part of this theorem and cannot silently choose its mathematical order.

### Density and the retained Gaussian action

Let H_l^obs be the initialized observable L2 spaces of C-H1 part 5. Rational
marks give the same spaces: approximate a fixed real marked graph inductively
in L2 using bounded action norms, Lipschitz elementary gates, locally bounded
syntax envelopes for products, and continuity of g·v and A0 tanh(g·v).
Thus every real finite word is measurable in the completed countable algebra.
Conversely its rational words are among the original words. Bounded word
spans are dense by the bounded Fourier-cylinder proof in C-H1 part 5; hence
P_l,N v -> v for every v in H_l^obs. Indeed approximate v by one finite span;
projection minimizes distance and the spans are nested.

These spaces reduce A0 with its adjoint, and the canonical GF starting at
initialization stays in them, with K(t) supported between them, by C-H1
(H11) and part 6's restarted-Euler comparison at s=0. This application uses
mu in U_rho and the complete initialized hierarchy, exactly within that
proved domain. It imposes no admissibility condition on a formal hierarchy.

On these spaces define only for analysis

  B_N = P_2,N A0 P_1,N = b_2^T D_N E_1[b_1 (·)].           (2)

Then ||B_N||<=2 and B_N->A0, B_N*->A0* strongly. For example
||B_N v-A0 v|| <=2||(P_1,N-I)v||+||(P_2,N-I)A0 v|| ->0.
The reverse proof uses adjunction. The bounds are uniform in N.
For any compact L2 set this convergence is uniform: choose a finite epsilon
net and use the uniform operator bound on the distance to that net.

## 3. The complete saved finite state and autonomous equations

The saved state is a real matrix M in R^(d_2 × d_1), and two current
probability populations

  Gamma_1 on R^(d_1+4), coordinates (b,g,w), w,g in R2,
  Gamma_2 on R^(d_2+1), coordinates (b,c), c in R.            (3)

Their static mark marginals are lambda_1,N and lambda_2,N. Initially
M=D_N, Gamma_1=Law(b_1,g,g), Gamma_2=Law(b_2,0). All entries of b and g
are frozen coordinates, not history. Their dimensions, every joint
correlation with current w or c, and d_1*d_2 matrix entries are counted in
(3). Each population is an actual finite-dimensional joint law, not separate
marginals. Static D_N and dictionary definitions are also saved fixed inputs.
There are two law-field types and one matrix; no field takes an arbitrary
function, raw matrix or unbounded vector as a mark. The input mark is u in
S1; the label y belongs to [-Y,Y].

For each input u compute from the current state

  a(u) = integral b tanh(w·u) dGamma_1 in R^d_1,
  z(u,b) = b^T M a(u),  h(u,b)=tanh z(u,b),
  d(u) = integral b c [1-h(u,b)^2] dGamma_2 in R^d_2,
  q(u,b) = b^T M^T d(u),
  f_N(u) = integral c h(u,b) dGamma_2, r_N(u,y)=f_N(u)-y.   (4)

The law velocities act only on their moving coordinates:

  v_w(b,w) = -2 integral r_N(u,y)[1-tanh(w·u)^2]q(u,b)u dmu,
  v_c(b)   = -2 integral r_N(u,y)h(u,b) dmu,
  M'       = -2 integral r_N(u,y)d(u)a(u)^T dmu.            (5)

The population equations are the continuity equations

  partial_t Gamma_1 + div_w(v_w Gamma_1)=0,
  partial_t Gamma_2 + partial_c(v_c Gamma_2)=0.             (6)

Equivalently push the initial joint laws along the characteristics (5).
All integrals in (4)–(6) are declared finite population/data integrals, using
only the saved current state and fixed mu. No Gaussian action is queried
operationally: multiplying the explicitly stored finite M and taking the
specified b-contractions is the full action rule. No omitted hierarchy level,
cutoff limit, elapsed-time list or target path is in (4)–(6).

The mathematical role of M is the matrix of current action coefficients in
fixed **initialized observable bases**. In the common-carrier interpretation
it represents B_N+K_N with K_N=b_2^T(M-D_N)E_1[b_1(·)]. It is a finite
compression of a population action, and its evolution is the orthogonal
projection of the exact learned rank increment. It is not an initialized
n-by-n trainable middle array in new coordinates: N is unrelated to neuron
width, D_N is deterministic and built from limiting observable contractions,
and the two populations remain continuum laws with nonlinear coordinates
outside the basis spans. Neither population is a full parameter law; no
middle row or original matrix entries occur in its coordinate domain.
Quadrature of these fields is a separate numerical approximation, not a
replacement finite-network theorem.

## 4. Well-posedness, energy and own-state restart

For fixed N the basis envelopes L_l=(sum_i ||b_l,i||_infty^2)^(1/2) are finite.
Use characteristics on the fixed mark probability spaces lambda_l,N. Their
unknowns are w=g+v with v in L-infinity(lambda_1;R2), c in
L-infinity(lambda_2), and M in a finite Euclidean matrix space. The base g
is unbounded but fixed and square-integrable. On bounded sets of (v,c,M),
(4)–(5) are locally Lipschitz in these supremum/Euclidean norms. To verify
this, |tanh s-tanh t|<=|s-t| and Lip(1-tanh²)<=2 control every gate;
|b|<=L_l controls evaluation and integration; |u|=1; all remaining
operations are finite sums, products of bounded factors and probability
integrals. No estimate multiplies two unrestricted L2 variables. The local
Lipschitz constant may depend on N and these bounds but is finite.

Picard existence here needs no black box: on a closed radius-R ball of
continuous paths, integrate (5). If h times the local speed bound is smaller
than R and h times its Lipschitz constant is less than one, this integral
map preserves the ball and is a contraction. Successive iterates are Cauchy,
the complete Banach space supplies their limit, and the integral identity
and the same contraction prove existence and uniqueness. Repetition extends
until a bounded set could be left. Measurability follows from the continuous
operations and integration. Pushforward gives (6). Conversely in the declared
characteristic solution class (6) is exactly this construction; no claim of
uniqueness for pathological distributional solutions with uncontrolled moments
is needed.

There are bounds independent of N that prevent finite-time escape in the raw
norm. With b_l orthonormal, the coefficient representation is isometric:
||K_N||HS=||M-D_N||F. Let L_N=integral(f_N-y)^2 dmu. The scalar gradient
calculus gives precisely (5), with the middle gradient restricted to
V_2,N tensor V_1,N and unrestricted w,c gradients. Direct differentiation
under these bounded characteristic integrands and adjunction yields

  L_N' = -||w_N'||2² - ||M'||F² - ||c_N'||2².               (7)

For the middle block, variation delta M gives
  delta f = d(u)^T delta M a(u),
so its loss gradient is 2 integral r_N d a^T. For w, propagating this
scalar pairing back through M gives the q and lower gate in (5); for c it
gives h. These derivations also verify the factors and the actual transpose.
Initially L_N=integral y² dmu<=Y². Thus integral|r_N| dmu<=Y, and

  ||c_N(t)||infty <=2Yt,
  ||M-D_N||F <=2Y²t², ||B_N+K_N||op <=2+2Y²t²,
  ||w_N(t)||2 <=sqrt(2)+4Y²t²+2Y⁴t⁴.                       (8)

Indeed ||a||<=||tanh(w·u)||2<=1, ||d||<=||c_N||2<=2Yt.
The M speed is at most 4Y²t. The row L2 speed is at most
4Y²t(2+2Y²t²); integrate for (8). On a fixed finite interval the row
supremum increment speed is at most 4Y²t L_1 ||M||op, since
|q|<=L_1||M||op||d||, and ||M||op<=2+2Y²t². Thus v,c,M remain bounded
in the local-existence norms on each finite interval. Their bounded speeds
give Cauchy endpoints there and the local argument extends them. In particular
the system exists uniquely through T.

At any reached time, save (3), M and its fixed marks. Restart the same
characteristic equation using that current joint law: w and c may be treated
as initial coordinate labels for the characteristic proof, but no extra
saved field is needed. Their current conditional distributions are already
in (3). The row drift is uniformly Lipschitz in w on the bounded M,c region,
and the readout drift is independent of its individual c coordinate, so
couple equal current coordinates and repeat the preceding estimates. Uniqueness
identifies the continuation with the original restriction. Bounds use the
remaining horizon and the saved finite energy/readout bound, with no query
of the original path or elapsed history. Initial g is retained solely to
reconstruct initial/current observations. Both equations and observation maps
are autonomous, and field domains do not grow at a restart.

## 5. Direct convergence and identification with actual GF

Fix one admitted mu. Realize every finite initialization dictionary on the
canonical carrier. Solve the characteristic equations there; by uniqueness
their laws are exactly (3)–(6). The finite fields are measurable functions of
their finite marks and initial g. Compare with the canonical established
solution (w,K,c) for this same mu, whose readout, energy and exponential
backward tails are supplied by C.4.7. Let A=A0+K and A_N=B_N+K_N.
Use the sum error

  e_N(t)=||w_N-w||2+||K_N-K||HS+||c_N-c||2.                 (9)

The operator difference A_N-A need not go to zero in operator norm; it is
never included as a small term in (9). Define the following **proof errors**
from the existing target, not inputs to (4)–(6):

  eps_N = sup_(t<=T,u) ||(B_N-A0)H1(t,u)||2
        + sup_(t<=T,u) ||(B_N*-A0*)Delta2(t,u)||2
        + sup_(t<=T) ||P_2,N K'(t)P_1,N-K'(t)||HS.          (10)

Then eps_N->0. The first two target argument sets are compact in L2 because
their fields are jointly continuous on [0,T]×S1; bounded multiplier
continuity proves this also for Delta2. Uniform strong approximation from
(2) applies. For the last term, K' is a continuous HS curve supported
between H_l^obs. Finite-rank tensors are dense in HS by its square-summable
matrix coefficients. P_l,N converges strongly, so it approximates every
such tensor and then every HS operator, using its contraction norm. A finite
net of the compact K' curve makes this uniform. This proves small **error
production**, not a hypothesis of small unknown hierarchy tails. The actual
scheme uses every integer N with no schedule selected from (10).

Here are the complete comparison subtractions. Bounds (8) and the target
energy bounds give one common raw/action ball, depending only on Y,T.
The forward differences obey, uniformly in u,

  ||H1_N-H1||2 <=e_N,
  ||Z2_N-Z2||2 <=C e_N+eps_N,
  ||H2_N-H2||2+|f_N-f| <=C(e_N+eps_N).                      (11)

In the second line write A_N(H1_N-H1)+(K_N-K)H1+(B_N-A0)H1.
In the last line subtract c_N-c first and multiply the hidden difference
by the bounded reference c. The upper backward subtraction gives

  ||Delta2_N-Delta2||2 <=C(e_N+eps_N),
  ||Q_N-Q||2 <=C(e_N+eps_N),                               (12)

because c is bounded and
Q_N-Q=A_N*(Delta2_N-Delta2)+(K_N-K)*Delta2
                         +(B_N*-A0*)Delta2.
For the first backward gate at every R>=1,

 ||phi'(w_N·u)Q_N-phi'(w·u)Q||2
 <= C(e_N+eps_N)+2R e_N+2 tau_R(Q(t,u)).                   (13)

This splits the unchanged target Q at |Q|=R. Only the target needs tails;
no moment bound for arbitrary approximate action outputs has been assumed.

The row velocity difference follows by subtracting residual and then the
backward field in (5). Residuals are bounded on the common raw ball and
||Q_N||2 is bounded, so its norm is bounded by
C(1+R)(e_N+eps_N)+C integral tau_R(Q(t,u)) dmu.
The readout difference uses (11). For the middle difference use

 K_N' - K' = P_2,N(F_K(w_N,A_N,c_N)-F_K(w,A,c))P_1,N
                         +(P_2,N K'P_1,N-K').            (14)

The projected exact rank is precisely (5), since its two coefficients
are d(u) and a(u). HS contraction and the two-factor rank difference
bound reduce its first term to (11)–(12) and residual differences; its
second is bounded by eps_N. Thus almost everywhere

 e_N' <= C(1+R)(e_N+eps_N)+C M exp(-aR), R>=1, e_N(0)=0.  (15)

The constants a,M are the established target tails, uniform on the fixed
family; the constants C use only (8), Y,T. Norms of C1 Hilbert curves are
absolutely continuous and their upper derivatives are bounded by the norm
of the derivative, which justifies (15) even at a zero component norm.

Set v=e_N+eps_N+eta for eta>0. While 0<v<=1 choose
R=1+a^(-1)log(1/v), giving v'<=L v log(e/v) with one finite L independent
of N. Integrate exactly: z=log(e/v) satisfies z'>=-Lz, hence

 e_N(t)+eps_N+eta <=exp(1-alpha(t))(eps_N+eta)^alpha(t),
 alpha(t)=exp(-Lt)>0.                                    (16)

For small eps_N+eta the bound stays below one through T, so first exit
validates its use. Send eta to zero. Since eps_N->0, sup_t e_N(t)->0.
The case eps_N=0 follows by the same positive eta argument. This comparison
identifies the limiting dynamics **with the existing canonical GF itself**;
it does not appeal to uniqueness for arbitrary formal hierarchy solutions.
Although (10) is useful for the proof, none of its target-dependent errors or
constants is used to initialize, select, or evolve any approximation order.
Equation (11) proves the required uniform-in-time whole-circle prediction
convergence on the same fixed law ball and interval.

## 6. All declared observation maps and second moments

On (3), seeds w,g,c are the displayed current/frozen coordinates. The frozen
upper seed at any v is reconstructed by

  z20_N(v,b_2)=b_2^T D_N integral b_1 tanh(g·v) dlambda_1,N. (17)

Its time derivative is zero. Use the original affine, sin,cos,tanh and bounded
product instructions on the appropriate population. For an action input V
on population 1 define its output on population 2 to be
b_2^T M integral b_1 V dGamma_1; the reverse output is
b_1^T M^T integral b_2 V dGamma_2. The marks and any required current
coordinates are evaluated in the **same** population joint law at every
occurrence. These are finite integrals with a declared kernel, not an action
oracle receiving an undeclared external vector. A separately fixed graph
may use its finite scalar/input marks and a finite union of outputs. Its
joint law is the pushforward of (3); requesting more output coordinates
does not enlarge the evolving state.

We prove convergence inductively on any such fixed graph, uniformly in time.
The seed convergence is (9), exact g, and the strong-compact argument for
(17). The readout is bounded by 2YT at all orders, as is the target.
Every bounded node consequently has a common finite syntax envelope across
N and t at its fixed marks. Affine and Lipschitz unary operations preserve
L2 convergence. A bounded product uses
||V_N W_N-VW||2<=||V_N||infty||W_N-W||2+||W||infty||V_N-V||2.
For an action node use

 A_N V_N-A V=A_N(V_N-V)+(K_N-K)V+(B_N-A0)V.                (18)

The first two terms vanish by the uniform action bounds and (9). The
last vanishes uniformly on the compact target L2 curve V(t), by (2).
The identical proof with actual adjoints handles every reverse node.
Frozen upper inputs use (17). All target node curves are L2 continuous
by the same finite induction. A bounded continuous gate times a named L2
field converges uniformly on these compact curves: truncate that target
field, use bounded convergence on the bounded part, and control the tail
uniformly by a finite L2 net. This is the established strong multiplier
lemma, not an L2 algebra assertion.

For a tuple (V1,...,Vk) on one population, pair the approximate and target
values on that same canonical carrier. Then

 W2(Law(V_N),Law(V))² <=sum_i ||V_i,N-V_i||2²,             (19)

uniformly in t. This is the stated C-H1 Euclidean W2 interpretation, not
independently coupled marginals. For each quadratic contraction
|E U_N V_N-E UV|<=||U_N-U||2||V_N||2+||U||2||V_N-V||2,
so its convergence and the needed second moments follow as well. Initial
and current hidden fields in the same tuple give the correct paired
observations and displacements. Arbitrarily nested but separately fixed
admitted actions are covered by (18), without a growing-program theorem.

The canonical limit has the actual finite-network interpretation from
C.4.7.5 and C-H1. That theorem retains the actual finite Gaussian readout:
its RMS tends to zero and its supremum satisfies
P(max_i|W3_i|>epsilon)<=2n exp(-n²epsilon²/2). No finite network is initialized
with zero readout here. Our population initialization c=0 is precisely its
limit. The closure order limit is a population approximation; no joint
order/width rate or cross-carrier operator-norm convergence is asserted.

## 7. Nontrivial family, activity, and limitations

Because rho<delta and T is unchanged, C-H1 part 8 supplies the same common
positive activity time t_a in (0,T). Its positive paired hidden squared
displacements and nonaffinity bounds persist throughout U_rho. The ball
contains the explicit small rotated two-atom laws and the small-arc nonatomic
laws constructed there. Equations (19) and the bounded hidden gates make the
paired displacements converge to those positive values for every fixed law.
The interval and radius never shrink with order, and no reference prediction
or fitted coefficient appears in the vector field.

The equations make sense for every bounded-label data law, with the same
initialization, and the fixed-order population well-posedness proof is not
restricted to the small ball. Only convergence to canonical nonlinear GF and
the activity guarantee are asserted on the declared family and interval.
We assert asymptotic convergence, not monotonic error reduction at every
successive order, a uniform rate over the law ball, practical quadrature,
useful accuracy, or a time-40 certified solver. The exact population fields
are allowed at C-H2; their dimension, joint dependence, rank conditioning,
quadrature and finite precision remain serious C-H3 costs.
