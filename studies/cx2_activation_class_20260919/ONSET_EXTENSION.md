# General C1,1 activations on the full C-H3 onset domain

Author proof, 2026-09-19; complete independent review pending. This proof
uses the complete maintained A.1–A.4, C.1–C.3 and Gaussian foundation
III.F, and the same-study CLOSURE_PROOF.md and PARTIAL_RESULT.md Section 3.
The law-completion details are supplied here. No near-orthogonality,
minimum atom mass, Gram inverse, bounded activation, oddness or higher
activation derivative is assumed.

## 1. Statement and exact equations

Fix a nonaffine phi in C1,1(R), with D=||phi'||infty<infinity and
L=Lip(phi')<infinity. C1,1 has the global meaning used in C.1. Both
hidden layers use this same phi. Put a=|phi(0)|+D; this also bounds
the values at zero of its smooth mollifications of scale at most one.
Training laws are arbitrary Borel probabilities on
Z=sqrt(2)S1 × [-1,1], with transport cost |u-v|+|y-z|, u=x/sqrt(2).
No sample-count parameter enters the population existence interval.

Use the bias-free model with stored Gaussian variances (1,1/n,1/n²),
physical mobilities (n,1,n), and unhalved mean squared loss. On the
canonical generated populations let A=A0+K, with the actual Gaussian
action and adjoint, ||A0||op<=10, full Gaussian row g~N(0,I2), and

    h(u)=phi(w.u), Z(u)=A h(u), H(u)=phi(Z(u)),
    d(u)=c phi'(Z(u)), q(u)=A* d(u),
    f(u)=E2[c H(u)], r(u,y)=f(u)-y.

The initial state is (w,K,c)=(g,0,0) in

    E=L2(Omega1;R2) ⊕ HS(H1,H2) ⊕ L2(Omega2).

Only K is HS; A0 is not represented by an HS matrix or kernel. The
strong raw equation is

    w'=-2 int r phi'(w.u) q(u) u dmu,
    K'=-2 int r d(u) ⊗ h(u) dmu,
    c'=-2 int r H(u) dmu.                                  (1)

There is T_phi>0, depending only on a,D,L and the fixed model constants,
on which every such law has a unique strong C1 solution of (1) on the
same canonical carrier. It is autonomous and uniquely restartable for
the remaining interval. The solution is continuous in its training law
in the sum norm on E, uniformly in time, has the exact gradient-energy
identity, and obeys uniform readout and law-integrated backward tails.
The finite GF/GD bridge, dense hierarchy, represented laws and numerical
scope are specified in Sections 5–7. No substantial fitting is asserted
at this onset time, and arbitrary laws need not move their hidden fields.

## 2. A common ball and tails before the time/law completion

Use the ball ||w||2<=3, ||K||HS<=1, ||c||2<=1. There ||A||op<=11.
Define

    H1=a+3D, H2=a+11D H1, R=H2+1,
    V=22R D²+2R D H1+2R H2,
    T_ball=min(1,1/[4(1+V)]).

For every finite probability law, all active h,H have norms at most
H1,H2, every residual has magnitude at most R, and ||d||2<=D.
The three velocity norms in (1) are bounded respectively by
22R D², 2R D H1, 2R H2. The HS rank bound is the exact identity
||d⊗h||HS=||d||2||h||2. Starting from (g,0,0), every raw Euler
program of total length at most T_ball stays strictly inside the ball:
each increment norm sum is at most V T_ball<=1/4. This is induction
over the actual nodes and does not assume a continuum flow or Euler
loss descent. It also covers arbitrary positive step lengths.

Apply maintained C.2 with depth two, probability weights, g=1 for the
input-Gram entry bound, unit initialization variances and mobilities,
standard Gaussian first projections, zero population readout, source
RMS bound max(H1,H2,D,11D²), and residual bound R. The last term
bounds the lower backward delta1=phi'(w.u)q, since ||q||2<=11D.
Every hypothesis of its
preliminary-ball clause has just been supplied. Its explicit cap choice
(33)–(35) gives T_resp>0 depending only on these constants. Let

    T_phi=min(T_ball,T_resp).

For each smooth mollification phi_e, C.2 gives common constants b,C>0
such that, for every finite law, every mesh node through T_phi and every
active input,

    E exp(b|c|²)<=C,       E exp(b|q(u)|²)<=C.               (2)

Neither C nor b nor T_phi depends on support size, individual atom
weights, Gram rank, mesh or mollification scale. This is exactly C.2's
weight-retaining response estimate, not a bound on a maximum over inputs
or Gaussian time histories. Its source formulas hold for C2 activations;
we use smooth approximations at this stage.

Here is a noncircular passage to the original C1,1 activation at a fixed
finite law and fixed finite mesh. A.1 constructs the original value
program directly. On the common action carrier, smooth mollifications
satisfy

    ||phi_e-phi||infty<=C D e,
    ||phi_e'-phi'||infty<=C L e,
    ||phi_e'||infty<=D, ||phi_e''||infty<=L.

Induct through the finite program. The bounded action is continuous in
L2; phi is Lipschitz with linear growth; c phi'(Z) is continuous in L2
under strong convergence of c,Z, by bounded-multiplier continuity
(III.F.9). HS rank updates and scalar contractions are continuous under
these same strong convergences. Thus every fixed node of the mollified
program converges strongly to the original node. Apply Fatou along an
almost-sure subsequence to transfer (2). No source coefficient or second
derivative is passed to a limit. The same argument applies to affine
Euler-state interpolation: append the final partial Euler step and use
C.2's arbitrary-step-length clause before removing mollification.

Consequently original-activation Euler programs have

    tau_R(c)+sum_a p_a tau_R(q(u_a)) <= C exp(-b' R²),
    tau_R(v)=||v 1_{|v|>R}||2,                             (3)

uniformly in law and mesh. Exponential square moments imply (3) by
integrating the elementary exponential tail bound, reducing b if needed.
This result is obtained before any Borel-law or continuum-time solution.

All programs needed here can be placed on one carrier. Take the countable
union of programs with rational input/label/weight/mesh approximations,
the mollifications, their finite unions and the smooth dictionary. III.F.7
constructs their two consistent generated populations and adjoints.
Continuity of each finite value program extends the construction to its
real finite parameters; completing the generated spaces includes the
strong limits below. Equivalently include the finitely or countably many
specific programs being compared before taking their limits. The common
isometry supplied by the same finite joint laws makes the result canonical.

## 3. Transport comparison in full-row/HS norm

Compare states theta,theta_bar in a fixed enlargement of the preceding
raw ball, with the same A0, at inputs u,v. Write e for their raw sum
distance and ell=|u-v|. Direct subtraction gives

    ||h_theta(u)-h_bar(v)||2 <=D(e+C ell),
    ||Z_theta(u)-Z_bar(v)||2 <=C(e+ell),
    |f_theta(u)-f_bar(v)| <=C(e+ell).

For any cutoff R>=1 the upper product estimate is

    ||c phi'(Z)-c_bar phi'(Z_bar)||2
    <=D||c-c_bar||2+LR||Z-Z_bar||2+2D tau_R(c_bar).          (4)

Subtracting the actual adjoints therefore gives
||q-q_bar||2<=C(1+R)(e+ell)+C tau_R(c_bar). The lower product
has the separate estimate

    ||phi'(w.u)q-phi'(w_bar.v)q_bar||2
    <=D||q-q_bar||2+LR||w.u-w_bar.v||2+2D tau_R(q_bar(v)).   (5)

The top cutoff in (4) is multiplied only by the bounded outside gate
in (5). The lower cutoff is added, not multiplied by it. Thus the final
coefficient is linear in R, not quadratic. Subtract each residual,
input direction and rank factor in (1). The rank difference is bounded
by ||d-d_bar||2||h||2+||d_bar||2||h-h_bar||2 in HS. Integrate
any coupling of mu,nu, and then minimize its transport cost. The result is

    ||F_mu(theta)-F_nu(theta_bar)||_E
      <=C(1+R)(e+W1(mu,nu))
        +C[tau_R(c_bar)+int tau_R(q_bar(v)) dnu].           (6)

This derivation requires tails only at the barred endpoint. It is also
valid at finite width, using row Frobenius norm divided by sqrt(n),
ordinary middle Frobenius norm, and readout Euclidean norm divided by
sqrt(n). For discrete data, couplings are probability matrices; the
proof has no inverse atom mass or support-count constant.

## 4. Strong Borel-law completion, tails and uniqueness

For two finite-law Euler interpolants of meshes h,h' and laws mu,nu,
apply (6) at their preceding nodes. Their raw velocities are bounded,
so replacing interpolants by nodes adds C(1+R)(h+h'). Use (3) at
the barred nodes, and integrate the elementary difference inequality:

    sup_(t<=T_phi) e(t)
      <=C exp(C(1+R)T_phi)
          [(1+R)(h+h'+W1(mu,nu))+exp(-b'R²)].             (7)

All constants are uniform over the finite laws. Given a Borel law,
finite partitions of the compact data domain supply finite laws converging
in W1. At fixed R send mesh/law discrepancies to zero, then R to infinity.
The Gaussian R² exponent dominates the linear propagation exponent, so
(7) proves a Cauchy family in C([0,T_phi];E). Completeness constructs a
limit independent of the chosen finite approximations, within the ball.

We justify passage of its equation, rather than inferring existence from
compactness. On a bounded raw set, forward maps are continuous in state
and input in L2. The upper product is continuous by III.F.9; then q is
continuous by the bounded adjoint. The lower product is continuous by
the same lemma. Rank products are continuous in HS. On the compact
limiting state path and compact input domain, these convergences are
uniform by a finite-net argument. All integrands of (1) are continuous
Banach-valued functions of input and label, with uniformly bounded norms.
For such a function G with modulus omega_G, any data coupling gives

    ||int G dmu-int G dnu||
      <=omega_G(a)+2||G||infty W1(mu,nu)/a,               (8)

by splitting transport distances above and below a>0. This proves
convergence of the law integrals. The integral equation passes to the
limit; its continuous velocity makes the solution strong C1.

Readout square-exponential moments pass by Fatou. For backward fields
use bounded continuous tests b_M(z)=min(exp(b z²),M). This function is
globally Lipschitz for fixed M. The just-proved uniform state/input L2
continuity gives uniform convergence of E b_M(q_j(t,u)) on u as the
state approximants converge. Apply (8), or weak convergence on the
compact data domain, to their changing law integrals. Monotone convergence
as M increases gives

    sup_t E exp(b|c_mu(t)|²)<=C,
    sup_t int E exp(b|q_mu(t,u)|²) dmu(u,y)<=C.             (9)

This is a law-integrated backward assertion. It does not assert a random
maximum, or a pointwise Gaussian tail for every passive input of a
nonatomic law. Cauchy–Schwarz in the data law gives the integrated
RMS cutoff bound needed in (6) and in the hierarchy proof.

Estimate (6) against this sole tail-bearing solution proves uniqueness
against any other strong solution on the carrier: a competitor's raw
norms are bounded on its compact interval, and sending R to infinity in
the difference inequality gives zero. At a reached state the same argument
on the remaining interval proves unique continuation. The equations use
only the current fields and action/adjoint, so this is autonomy and
reached-state restart, not a restart with fresh independent Gaussian roots.
Comparing two constructed laws similarly proves law continuity. A usable
qualitative modulus is the infimum over R>=1 of the right side of (7)
with only W1(mu,nu) in its first bracket.

The prediction chain rule uses A.4's scalar raw derivative for a bounded
Lipschitz activation derivative and III.F.9's strong-curve chain rule;
HS adjunction is III.F.8. Thus no C2 hypothesis from III.F.10 is imported.
Their integrands are continuous and uniformly bounded in L2/HS on
the compact time/input set; hence differentiation under the probability
law is justified by the integral difference quotient and its uniform
bound. They give exactly

    L_mu(t)+int_0^t (||w'||2²+||K'||HS²+||c'||2²) ds
      =int y² dmu<=1.                                    (10)

## 5. Actual finite GF/GD and observations

For each fixed width and Borel training law, the actual finite raw vector
field is locally Lipschitz in its finite parameters: phi and phi' are
Lipschitz, and compact data make the local product bounds uniform before
integration. The finite metric gradient identity bounds displacement by
sqrt(t L_n(0)) and increments between s,t by sqrt(|t-s|L_n(0)) in
that fixed positive metric. Finite-dimensional local continuation at
the resulting endpoint therefore gives global finite GF. This uses
C1,1 regularity and does not import a C2 ODE hypothesis.

Fix first a finite reference law, finite proof mesh and cutoff. A.1
identifies the complete finite oracle value program, including both
matrix orientations, its full first row and the finite rank updates.
Every scalar contraction has its population value in the limit; the
same-root proxy construction in PARTIAL_RESULT.md Section 3 then gives
consistent within-width parameters and velocities. Use continuous
quadratic cutoff ramps when transferring tails: for an oracle field v
and its recomputed proxy v_tilde on the same finite rows,
tau_(2R)(v_tilde)<=2||v_tilde-v||2+2||(|v|-R)_+||2.
The last squared ramp is continuous with at most quadratic growth, so
its empirical mean converges at this fixed program by A.1 and uniform
integrability. No hard-threshold continuity at an atom is assumed. Include the
actual initial readout additively in the proxy. Its normalized norm is
O_P(n^-1); the actual network never receives a zeroed initial readout.

The finite version of (6) compares the actual flow with that proxy.
If actual training laws lambda_n approach a fixed target mu, add the
transport cost to the fixed reference law, with tails only at the proxy.
Stop at first exit from a raw ball one unit larger than the constructed
path. At fixed reference law, proof mesh and cutoff, let width tend to
infinity. Then remove the reference-law/mesh errors and finally the
cutoff as in (7). This precludes exit and proves finite GF identification.
For exact simultaneous raw GD, velocities are evaluated at the preceding
actual node; their raw ball bound adds O((1+R)eta_n) to the same inequality.
Every eta_n->0 is therefore admitted. There is no discrete energy claim
or neuron-maximum bound in this argument.

This supplies convergence in probability for arbitrary deterministic
lambda_n->mu in W1 and n->infinity, with no relative restriction.
If actual empirical laws are random, independent of initialization,
and converge in W1 in probability, use the same inequality conditional
on their values; its constants are uniform. For iid samples on the
compact domain this convergence follows directly: partition into finitely
many cells of diameter<=a; each cell-frequency variance is at most 1/m,
so the expected total frequency discrepancy is at most the number of
cells divided by sqrt(m). Transport through their representative points
bounds W1 by 2a plus domain diameter times that discrepancy. First
send m to infinity at fixed partition, then a to zero. Consequently any
independent iid sample-count/width growth is permitted.

At fixed proof programs A.1 supplies every separately fixed declared
same-population observation graph; strong multiplier continuity and
the state/proxy comparison then remove the approximations. Admissible
graphs use globally Lipschitz coordinate operations of linear growth,
bounded multipliers and actual action/adjoint calls, and end in joint
laws with second moments or their continuous quadratic contractions.
They include the ordinary hidden/backward fields and fixed
initial/current activation pairs. They do not include arbitrary products
of two uncontrolled unbounded fields or increasing observation graphs.

Predictions have the common input modulus

    |f(u)-f(v)|<=||c||2 D²||A||op||w||2 |u-v|.             (11)

The finite and population raw balls bound this constant. Finite circle
nets upgrade fixed-query convergence to the whole-circle supremum,
uniformly in time. The same input/strong-state continuity and (8)
give data-averaged initial/current pair laws and second moments. Whole-
circle convergence and weak data convergence also pass training and
population losses to L_mu(t), uniformly on this interval. No cross-width
operator-norm convergence is used.

## 6. The dense hierarchy on Borel laws

Use the activation-independent smooth words and the complete Gaussian
source initializer of CLOSURE_PROOF.md. The prefix of bounded valid
codes through 16N is nested and cofinal; the ridge is 2^-N. Its density
and reducing-pair proof is unchanged: every finite word eventually
appears, and the ridge tends to zero. Neither rank deletion nor a
trajectory-selected dictionary is used. Each finite-law Euler
state starts in the dictionary's reducing spaces and preserves them:
their completed measurable spaces are closed under the relevant
coordinate operations, both initialized actions preserve the reducing
pair, and every learned rank has both factors in those spaces. Thus
w and c stay in their respective spaces and K=P2 K P1, where P1,P2
are the two orthogonal projections. Strong row/readout completion and
closedness of this HS block preserve these statements in the target.

Replace the finite training sums in that proof's autonomous equations by
law integrals. At fixed order the marks b1,b2 are bounded, while g has
finite second moment. The same characteristic fixed-point proof gives
local existence. Its energy identity bounds the dynamic row/readout/
matrix norms on every finite horizon by their initial norms plus sqrt(T).
Because the marks are bounded, these norm bounds bound M and the upper
preactivations uniformly over population marks and unit inputs. Linear
growth of phi then bounds c' in Linfty; the bounded mark/action formula
bounds (w-g)' in Linfty. These facts preclude finite-time escape in the
fixed-order characteristic space and yield global fixed-order existence.

The constructed target provides S in the full-row/HS topology. Its (9)
provides E with the data-integrated q tail, which is exactly the tail
integrated when subtracting (1). The target sets h(t,u),d(t,u) are compact
in L2, and K'(t) is compact in HS, by joint continuity on compact domains.
Strong convergence of the positive dictionary filters and both filtered
action directions is uniform on those compact sets. Therefore the
omitted forward, backward and HS sources in CLOSURE_PROOF.md tend to
zero uniformly in time and input. Its one-reference cutoff comparison,
with (9) integrated over mu, proves convergence of the finite hierarchy
to this same strong target. No tail premise on the projected flows is
needed. Equation (11) and the declared observation argument give whole-
circle predictions and initial/current pairs with second moments.

## 7. The full represented C-H3 family and numerical interface

Let U(s)=((1-s²)/(1+s²),2s/(1+s²)) and
R_*=[[3/5,-4/5],[4/5,3/5]]. For rational p in [1/3,2/3] and rational
interval endpoints a<=b,c<=d in [-1/20,1/20], use mass p on
(sqrt(2)U(S),+1) and mass 1-p on (sqrt(2)R_*U(V),-1), with uniform
conditional parameter laws, allowing degenerate point intervals.
These are precisely the C-H3 represented inputs. Since
|U(s)-e1|<=2|s|<=1/10, their cross-component inner products lie
between 2/5 and 4/5. The complete family lies in the theorem's all-law
domain; no radius or interval is reduced with hierarchy order.

The midpoint rule on m cells of an interval [a,b] has mean parameter
transport error (b-a)/(4m). Since |U'(s)|<=2 and each interval length
is at most 1/10, mixture transport error is at most 1/(20m), with
zero contribution from degenerate intervals. At fixed hierarchy order,
the bounded-mark characteristic proof is Lipschitz in this input-law
perturbation on its finite-horizon ball: subtract its three fields,
use their uniform input Lipschitz constants, and apply Gronwall.
This removes the input quadrature before taking outer hierarchy order.

NUMERICAL_EXTENSION.md implements this same generic hierarchy and proves
the remaining finite refinements. Its inverse-Cholesky coordinates are
an orthogonal change of the symmetric proof coordinates. At fixed N,
first remove arithmetic error, then the time mesh, input quadrature,
population replay P, initializer quadrature Q, and source regularization.
Finally send N to infinity. For literal finite arithmetic, consistent
locally uniform evaluators for phi and phi' must be supplied; an arbitrary
regular function need not be computable. There is no hierarchy-order rate,
arbitrary diagonal refinement, tolerance selector, finite-run accuracy
certificate or claim of practical cost to a requested accuracy.

Weighted C.3 supplies positive early paired motion at nonparallel atomic
members with nonzero labels. The law/paired continuity above preserves it
on a nearby represented subfamily, including short nonatomic arcs, as
spelled out in REVISED_RESULT.md. It is deliberately not asserted for
every Borel law: for instance identically zero labels can give a stationary
population initialization. This completes the onset claim at its stated
activation, input, time, observable and numerical scopes.
