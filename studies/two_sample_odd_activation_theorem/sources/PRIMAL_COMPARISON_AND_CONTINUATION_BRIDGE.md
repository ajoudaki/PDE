# Near-affine primal comparison and the continuation bridge

Status: main derivation, not independently audited. Part 1 is a direct
uniform-in-cap comparison. Parts 2--4 give explicit downstream arguments
under the response-tail premise stated there; they are not the requested
unconditional theorem. No claim that one epsilon works for all angles.
Use CONTRACT.md and the two baseline notes at their recorded hashes.

## 1. A direct comparison, without comparing bad multipliers

The raw Hilbert state consists of the first weight field, HS increments
of W^(2),W^(3) around their bounded initial actions, and C=W^(4).
For differences use the sum of sqrt(d)||dw||_L2, the two HS norms, and
||dC||_L2. This controls each first preactivation difference since
||x_a||/sqrt(d)=1. At finite width these are sqrt(d/n)||dW^(1)||_F,
the two ordinary Frobenius norms, and ||dC||/sqrt(n). Initial matrix
HS norms need not be bounded; only their operator norms are used.

Let V_{epsilon,R} be the feature vector field with p_a=y_a/2 and
D_{epsilon,R}(z,q)=q+epsilon tau_R(q)/(1+z^2) in every backward gate.
Suppose each first preactivation norm, both matrix operator norms, and
the readout norm are at most B>=1. The following inequalities hold on
that ball, in both finite normalized norms and population L2 norms.
Compare epsilon and zero at the SAME state. For 0<=epsilon<=1,

    ||H^1_e|| <=4B,       ||H^1_e-H^1_0|| <=2 epsilon,
    ||H^2_e|| <=7B^2,     ||H^2_e-H^2_0|| <=4 epsilon B,
    ||H^3_e|| <=10B^3,    ||H^3_e-H^3_0|| <=6 epsilon B^2.

These follow successively from |phi_e(z)-(1+z)|<=pi epsilon/2 and
the bounded matrix actions. Likewise |D_e,R(z,q)-q|<=epsilon|q|
gives successively

    ||delta^3_e|| <=2B,   ||delta^3_e-delta^3_0|| <=epsilon B,
    ||delta^2_e|| <=4B^2, ||delta^2_e-delta^2_0|| <=3epsilon B^2,
    ||delta^1_e|| <=8B^3, ||delta^1_e-delta^1_0|| <=7epsilon B^3.

For example the middle incoming q differs by at most epsilon B^2;
the middle gate adds at most 2epsilon B^2. No comparison of
phi'(Z_e)-phi'(Z_0) multiplied by an uncontrolled q occurs here.
The rank-one difference inequality now gives component differences
at most 7,14,11,6 times epsilon B^3, respectively. Thus

    ||V_{epsilon,R}(Theta)-V_0(Theta)|| <=40epsilon B^3,
    ||V_{epsilon,R}(Theta)|| <=50B^3.                     (1)

The sum-norm Lipschitz bound for V_0 on this ball is 9B^2, as follows
by the four component estimates in the source baseline (the first
field norm uses sum |p_a| ||x_a||/sqrt(d)=1). The same bound holds
in HS rather than operator differences, since rank-one HS norms
are products of field L2 norms and ||M||_op<=||M||_HS.

For affine and nonlinear Euler programs with the SAME initial state,
comparison until exit from the ball consequently gives

    E_{k+1}<=(1+9B^2 h_k)E_k+40epsilon B^3 h_k,
    max_{s_k<=S} E_k <=40epsilon B^3 S exp(9B^2 S).        (2)

The identical integral Gronwall bound holds for their strong flows.
Choose B so the affine flow has primal bound strictly below B/2 on
[0,S], and use affine Euler convergence for all sufficiently fine
meshes. If the right side of (2) is less than B/4, the usual first-exit
induction closes with a strict margin; this holds uniformly in R.
Fixed R vector fields are locally Lipschitz on the raw Hilbert state,
so they have local strong solutions and this comparison extends them
through S. A bounded vector field along a finite interval gives a strong
endpoint, and local Lipschitzness permits continuation at that endpoint.

The initial fields/operators can be realized on one common generated
space containing all the countably many cap/mesh programs and the
affine programs; this is the explicit common-action construction of
the baseline dependency. Thus (2) is a strong comparison on a common
space, not a comparison of marginal Gaussian covariances. A fixed
epsilon can be selected before this construction; no uncountable
simultaneous collection or width-dependent activation is necessary.

Let S be the affine first hit of g_0=3/2. The audited radial/affine
baseline supplies a finite S and a finite primal bound. Equation (2)
and the same-state query estimates imply O(epsilon) strong differences
in every forward/backward query and their scalar second moments,
uniformly in R and sufficiently fine mesh. Shrinking a fixed epsilon
once makes g_{epsilon,R}(S)>5/4 for all R. The shrinkage can depend on
the fixed input pair, since S and B do. No universality follows.

## 2. The precise additional premise and removal of auxiliary caps

RESPONSE-TAIL PREMISE: for some fixed positive epsilon as above, the
actual nonlinear feature Euler programs on [0,S] satisfy mesh- and
cap-independent Gaussian tail bounds for each sample's incoming
q^(1), q^(2), and the shared C, in the following norm form:

    sup_{R,k,a} || |Q_{R,k,a}| 1_{|Q_{R,k,a}|>u} ||_L2
          <= C exp(-c u^2),  u>=u_0.                    (3)

Q ranges over those three groups; constants may depend on S,epsilon,
and the input pair. Appropriate changes of c,C convert subGaussian
Lp bounds into (3): Markov with p proportional to u^2 bounds tails,
and integration bounds their second moment. This premise must be
proved for the actual nonlinear programs, not all inputs of an
initial Gaussian action. NONLINEAR_RESPONSE_PERTURBATION.md supplies
this proof with precisely the bounded affine premise established in
Part 1 and the two baseline notes. Fixed-cap Euler convergence passes (3) to
their strong feature flows (use continuous truncated-square bounds).

For R'>=R, or for R'=infinity, the exact asymmetric gate difference is

 D_{e,R'}(z_A,q_A)-D_{e,R}(z_B,q_B)
  =(q_A-q_B)+e g'(z_A)[tau_{R'}(q_A)-tau_{R'}(q_B)]
    +e[g'(z_A)-g'(z_B)]tau_R(q_B)
    +e g'(z_A)[tau_{R'}(q_B)-tau_R(q_B)],                 (4)

where g=arctan. The incoming difference coefficient is at most 2;
the z difference coefficient is at most 4eR; and the last term is
bounded by 2e|q_B|1_{|q_B|>R}. Successively substitute the forward
state bounds and then the three backward gates. At each stage the
previous incoming error is multiplied only by a bounded matrix norm
and 2, not by R. The new R factor multiplies a forward-state error
which already has an R-independent bound. Thus

    ||V_{e,R'}(Theta_A)-V_{e,R}(Theta_B)||
       <= C_B(1+eR)||Theta_A-Theta_B||
          +C_B e sum_Q || |Q_B|1_{|Q_B|>R} ||_L2.         (5)

This holds if both states have bounded primal sizes, with no tail
condition on A. All rank products use L2 times L2 in HS norm. It also
proves local Lipschitzness for each fixed R on arbitrary raw states.

Combining (3),(5) and Gronwall gives

    sup_{s<=S} ||Theta_{R'}(s)-Theta_R(s)||
          <= C exp(C(1+eR)S-cR^2).                      (6)

Hence the cap family converges strongly on the full fixed interval,
including matrix increments in HS norm. Formula (5) and the Gaussian
tail imply uniform convergence of the vector fields as well. The
limit is a C1 strong solution of the uncut, autonomous raw gradient
equation. An arbitrary competing bounded-primal strong solution on
a compact interval is compared to Theta_R by (5) with R'=infinity.
It has the same initial state and requires no tail hypothesis of its
own. Sending R to infinity proves uniqueness.

The same argument proves uniqueness after any reached time s_0: the
initial discrepancy of the cap reference from the reached uncut state
obeys (6), and multiplication by exp(CR(S-s_0)) still makes it vanish.
The already constructed path supplies existence after reached states.
No claim of local existence at every point of the full L2 state space
is needed or made. Initial actions remain part of the finite collection
of state operators; there is no external trajectory oracle.

Symmetry passes from the Euler constructions, so f_a=y_a g on this
path. It is a true uncut gradient path and the radial argument applies.
It has a first hit s_*<S of g=1, with positive projected kernel bounded
below by its initial value. The physical clock ds/dt=2(1-g) covers all
finite t and stays below s_*. This constructs one uniquely restartable
population physical flow, conditional precisely on (3).

## 3. Why the genuine two-residual finite dynamics also matter

The finite system is NOT exactly symmetric and cannot use that scalar
clock. At fixed R, define its physical vector field using both actual
residuals, with D_{e,R} in each backward gate and the original readout
update. On a bounded primal ball, its vector field is Lipschitz with
constant C_B(1+eR): predictions are locally Lipschitz by forward
propagation and Cauchy--Schwarz. The same asymmetric estimate (5)
holds for physical fields, with changed B-dependent constants. There
is still only one linear R loss.

The population physical fixed-cap reference exists for every finite
T. Indeed its symmetric feature path satisfies g_R(0)=0 and
g_R(S)>5/4. Let s_R be its first hit of 1. Before it, 1-g_R>0, so
t(s)=integral_0^s du/[2(1-g_R(u))] is increasing. The bounded derivative
of g_R implies 1-g_R(s)<=M_R(s_R-s); hence t diverges at s_R. This
does not assume g_R is a gradient ascent or monotone. Its inverse
reparametrizes the symmetric cap feature path into the two-residual
physical field. The uniform primal bound and tails are inherited from
the entire feature interval [0,S].

For fixed R and physical T, the finite fixed-cap physical GF/Euler
programs converge to this reference as follows. At each fixed mesh,
finite-program joint empirical second moments identify all forward,
backward, velocity, and kernel slots, with residual contractions frozen
causally. To obtain bounded finite matrix operators, do not assume
operator-norm convergence of trained matrices. Unroll them: the initial
operators have bound 10 with probability tending to one; their learned
increments are bounded by the sum of step size times the product of
the two update-factor RMS norms. Those finitely many norms converge
to the reference norms. Refining the mesh gives their integrals, bounded
by C_B T because all update norms are bounded on the population path.
The first and readout fields have converging norms at those nodes.
This supplies a finite-width primal ball of radius B_T with slack,
uniformly over sufficiently fine meshes (width tends to infinity first).

On that larger ball, deterministic Euler--flow error is at most
C_{B_T,R,T}|mesh|, independent of width. The proof is the integral
local defect bound (1/2)L M h^2 and discrete Gronwall. A stopped
comparison plus the just-certified norm slack prevents exit. Taking
width to infinity at fixed mesh, then mesh to zero, therefore identifies
the actual finite fixed-cap physical GF on [0,T]. It likewise handles
any sufficiently fine Euler step including eta_n=n^-2. This is a
triangular convergence argument, not a growing-transcript Gaussian
identification claim.

For clarity, uniform-in-time tail convergence of the reference incoming
Q is available at fixed R. Its L2 time modulus follows from the locally
Lipschitz D_{e,R}, bounded vector field, and bounded matrix actions.
The positive-part tail norm ||(|Q|-u)_+||_L2 is 1-Lipschitz in Q. A
finite time net and fixed-program second-moment convergence thus give
uniform-time convergence of these tail norms. Using a threshold u=R/2
dominates the raw |Q|1_{|Q|>R} tail up to a factor 2, retaining Gaussian
decay in the population reference by (3).

Compare the actual uncut finite GF against its SAME-WIDTH physical
fixed-cap reference, using (5). Until exit from a larger primal ball,
the error is bounded by an exp(C_{B_T,T}R) factor times the reference
tail error. Take width to infinity at fixed R, use (3), then send R
to infinity. The result tends to zero, and the strict state/length
margin prevents exit with probability tending to one. This proves
full-sequence joint convergence in probability; no subsequence choice
of population solutions is involved.

For raw exact GD, compare its parameter interpolation directly to the
same finite fixed-cap GF. Its derivative at time t is the uncut vector
field at the preceding GD node k eta_n. Apply the asymmetric estimate
there against the cap reference at k eta_n. The difference from the cap
reference derivative at t is at most L_R M_R eta_n. Thus the same
stopped Gronwall estimate has one extra vanishing C_{R,T} eta_n term.
This avoids any n-dependent Lipschitz constant of the uncut field.
No F-coordinate correction arises: the raw algorithm is exactly Euler
for the physical raw equations. Hidden objects are recomputed from
the raw interpolation, as required by the contract.

## 4. Observables and nontriviality obligations

Strong parameter-state comparison implies forward-field convergence by
the Lipschitz activation and bounded actions. The asymmetric gate
estimate and the reference tails give all backward fields and raw
velocities. Matrix increments converge in HS and both matrix directions
on converging L2 probes follow from their uniform operator bounds.
Products of two converging L2 fields have converging expectations, so
all four 2-by-2 raw kernels, including off-diagonals, are retained.

The same claim for hidden velocities uses the actual product/chain rule.
For example dot Z^2_a=dot W^2 H^1_a+W^2[phi'(Z^1_a) dot Z^1_a].
FIXED_CAP_VELOCITY_BRIDGE.md supplies the fixed-cap empirical law and
uniform-time reference tails. Its exact deterministic comparison (33)
says that two bounded states/directions with discrepancies a,b have
total hidden-velocity error at most

    K[b+(1+M)a+sum_{ell,a} ||(|P_ref^(ell)_a|-M)_+||_L2],

where P_ref is the reference PREACTIVATION velocity, and K depends only
on bounded primal/raw-direction sizes and the activation, not on the
cap or the truncation level M. Its proof is the three-layer product
rule, truncating the reference factor in a gate difference. This is
also valid at finite width with RMS norms.

There is an important ordering point in removing R for velocities:
do NOT assume the explicit fixed-cap velocity moment constants grow
slowly enough in R. Instead, population cap paths and raw directions
already converge uniformly in the strong state norm to the uncut path
and direction, by (5)--(6) in physical time. The uncut forward chain
rule gives continuous L2 hidden velocities. Apply the deterministic
comparison with the UNCUT population velocity as reference. Its compact
L2 time image has uniformly vanishing tail norms: cover that image by
a finite L2 net and use that the positive-part tail norm is 1-Lipschitz.
First send R to infinity at fixed M, then send M to infinity. This
proves uniform strong convergence of population cap hidden velocities
to the uncut hidden velocities. In particular their tail norms are
uniformly vanishing as M grows for all sufficiently large R.

For the finite uncut system versus its same-width cap reference, raw
state AND raw-direction errors have width-limit upper bounds tending
to zero with R; (5) bounds the latter by C(1+eR) times (6) plus the
Gaussian tail. Apply the deterministic velocity comparison with that
finite cap reference. At fixed R,M its empirical velocity tail norms
converge uniformly in time by the fixed-cap bridge. Take width to
infinity, then R to infinity at FIXED M, using the population velocity
convergence just proved, and finally M to infinity. All error terms
vanish. This supplies the uncut hidden-velocity convergence without
any uncontrolled product of a cap-dependent moment constant and an
R-dependent state error. Node conventions are right derivatives,
terminal left derivatives, including the actual directions of the
raw interpolated GD rather than the vector field at its current state.

The hidden preactivation and feature PATH laws converge in
W_2(C([0,T])) with its supremum norm, not only in finite-time laws.
Here is the extra tight approximation needed for that assertion.
For any scalar absolutely continuous path x and its piecewise-linear
interpolant I_h x on a uniform observation grid of mesh at most h,

    sup_t |x(t)-I_h x(t)|^2 <=4h integral_0^T |x'(t)|^2 dt.

This follows on each grid interval by Cauchy--Schwarz applied to the
two increments from its endpoints, then bounds their interval energy
by the total energy. Averaging over finite neurons, or over a population,
gives a squared path-space W_2 coupling cost at most 4h times integrated
RMS speed squared. On the stopped bounded primal balls all those speeds
are uniformly bounded by forward product rules and bounded gates,
including the raw GD directions. The no-exit estimates already proved
remove the stopping with probability tending to one. At fixed h, joint
node empirical W_2 convergence passes through the linear interpolation
map into C([0,T]). Let h decrease to zero in the triangle inequality.
This proves the claimed path-space W_2 convergence for both samples
jointly in each layer. Integrated squared velocities converge by the
uniform-time velocity law and bounded second moments.

All-time strict nonaffinity is furnished, for the angle-specific route,
by the audited baseline Gaussian nondegeneracy on [0,S]. Its best affine
arctangent approximation error has a positive minimum. The strong
O(epsilon) state comparison in Part 1 preserves that positive error
for sufficiently small fixed epsilon. For phi_e the error is epsilon^2
times the arctangent error, so it is positive uniformly on the full
feature interval and hence at every finite physical time.

INITIAL_FEATURE_LEARNING.md separately proves the positive initial
acceleration of every hidden block and every sample's hidden features,
and a strictly changing projected kernel, for each fixed epsilon>0.
These arguments must be included and audited together with the final
existence proof. An affine comparator is not an admissible final model;
epsilon may never tend to zero with width or time. Even after all these
bridges are certified, an angle-specific epsilon would remain an
intermediate result, not the user's universal-activation target.
