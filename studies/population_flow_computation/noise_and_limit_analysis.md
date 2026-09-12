# What query noise does and does not require

Author: coordinator. Status: internal proof draft, not independently reviewed.
This note isolates the noise-to-clean comparison from empirical Gaussian
computation. It neither supplies a useful time-40 resource certificate nor
identifies an arbitrary empirical array with a canonical action state.

## Exact comparison objects

Fix a finite probability law on S1 times [-Y,Y] and a finite physical Euler
mesh of total duration T<=40. The clean population Euler graph uses the
established A0 and its actual adjoint, with (w,K,c) initially (g,0,0).
An auxiliary noisy graph uses these same actions and extra independent
standard Gaussian coordinate roots on the output population of each call.
Its forward answer is A H+s epsilon, its backward answer is A*D+s eta,
where A=A0+K and D=c phi'(A H+s epsilon). It computes its own residuals
and updates all three blocks simultaneously, with the physical factor -2.
Only action answers, not raw parameters, receive numerical noise. All
expectations in this paragraph define comparison objects; implementing them
is the separate sampling problem.

The III.F construction admits these finite extra Gaussian roots. At fixed
graph, source expressions use the combined centered sources B=xi+s epsilon,
T=zeta+s eta, whose covariances are E[H_iH_j]+s^2 delta_ij and
E[D_iD_j]+s^2 delta_ij. Their response terms differentiate the combined
source coordinates while fixing all scalar coefficients. The initialized
operator in the auxiliary graph remains A0; the noisy answers as a whole
are not an adjoint operator pair. In particular their mixed contraction
defect is s^2(beta-alpha), as proved separately in source_regression_audit.md.

At any fixed graph all scalar coordinate functions and their required
directional derivatives have finite polynomial Gaussian envelopes.
This follows by induction: tanh and its derivatives are bounded, forward
and backward source answers add a Gaussian coordinate and finitely many
earlier fields with deterministic coefficients, and a differentiated
product increases the finite envelope degree. Thus the expectations and
response identities used to define the comparison graph exist. This is
not a uniform-in-graph envelope bound.

## A direct noise defect without noisy-path tail assumptions

Suppose at a noisy graph node ||A||<=M, ||c||infinity<=C, and all residuals
in the noisy evaluation have absolute value <=R=C+Y. Set s<=1. Write
z=A H, z_s=z+s epsilon, V=phi(z), V_s=phi(z_s), and let clean fields at
this SAME state carry no subscript. Since ||epsilon||2=||eta||2=1,

    ||V_s-V||2 <= s,
    |f_s-f| <= C s,
    ||D_s-D||2 <= 2 C s,
    ||(A*D_s+s eta)-A*D||2 <= (2 M C+1)s.

Here |phi|,|phi'|<=1 and |phi''|<=2; ||D||2<=C and ||Q||2<=MC.
Subtract each residual-weighted update using the noisy residual for the
field difference and the clean field for the residual difference. The
sum of the lower-L2, middle-HS and upper-L2 velocity defects is at most

    Lnoise s,
    Lnoise = 2 { R(2MC+2C+2) + C(MC+C+1) }.                 (1)

The lower field is phi'(w.u)Q u, whose two bounded factors have norm at
most one. The middle field is D tensor H, with ||H||2<=1. The upper field
is V. Summing the three estimates gives exactly (1); no independence of
epsilon and an evolved field was used.

Uniform elementary node bounds exist for BOTH graphs. Write
C_T=Y(exp(2T)-1), R_T=C_T+Y. The readout recursion obeys
||c_next||infinity <= ||c||infinity+2h(||c||infinity+Y), so
||c||infinity<=C_T. Rank updates give
||A||<=2+2T R_T C_T=:M_T. The noisy lower row satisfies
||w||2<=sqrt(2)+2T R_T(M_T C_T+1). These estimates use bounded
activations and s<=1; they require neither a noisy energy identity nor
noisy Gaussian-tail estimates. Their magnitudes at T=40 are impractical.

## Propagation relative to the clean graph

Assume the fixed law and mesh lie in a C.4.7 family on which clean Euler
queries have a uniform tail estimate

    integral tau_U(Q_clean) dmu <= TQ(U),
    TQ(U) <= Cq exp(-cq U^2) for U>=U0.                    (2)

Use the one-reference sum-L2/HS comparison, with the CLEAN graph as the
reference. There are a(U)=a0+a1 U and a fixed finite Lnoise from (1)
such that the two node-state discrepancies obey

    d_next <= (1+h a(U)) d + h {Lnoise s+4R_T TQ(U)}.

The row, action and readout bounds above apply to every node. Starting at
zero discrepancy and multiplying the scalar recurrence gives

    max_nodes d <= T exp(T a(U)) {Lnoise s+4R_T TQ(U)}.     (3)

The same bound applies to affine interpolants in the raw state norm by
convexity. For every fixed U, first send s to zero. Then send U to infinity;
the negative quadratic in (2) dominates the linear exponent in (3).
Thus the exact noisy graph converges to the clean graph uniformly over
the admitted sufficiently fine meshes, under the stated clean source cap.
No source-tail bootstrap on the noisy graph is needed for this particular
comparison. Requested tolerances can be allocated by explicitly searching
U and then s IF computable constants for (2) and admission are supplied.

Same-state clean passive prediction uses A H, without extra observation
noise. For two same-action-carrier states in this bounded set,

    sup_u |f_theta(u)-f_bar(u)|
      <= ||c-cbar||2 + C_T (||K-Kbar||HS+M_T||w-wbar||2).

The paired initialized/current hidden fields use the very same initialized
action and roots in both comparison graphs. Lower fields converge by the
Lipschitz activation; upper fields by bounded actions and the preceding
factor subtraction. Current D and Q converge using bounded c and its
strong L2 convergence. These are same-carrier proof comparisons, not
operator-norm coupling of unrelated representative arrays.

## The missing assembly for the actual solver

The implemented statistical system does not literally act by A0 on its
empirical arrays. Its covariance and response moments are estimated from
its generated trajectory. Equation (3) applies only AFTER that numerical
process has been compared with the exact noisy source graph. A proof of
that comparison must preserve both orientation source histories and their
responses. Independent fresh Gaussian answers with matching marginals
would not supply it.

For a fixed mesh, positive s and finite list of named observations, a
coupling to independent deterministic-coefficient copies is the proposed
route for the persistent representative scheme. Its constants may depend
on the graph length and s. Fixed-graph convergence, together with (3) and
C.4.7 completion, suggests an ordered limiting construction, but a useful
computable simultaneous refinement rule requires all constants and all
observation/precision errors to be evaluated. A nonquantitative diagonal
choice is not the requested certificate.

The following still must not be inferred from this note:

* A finite feasible (P,h,s,quadrature order,precision) achieving error 0.1
  or 0.02 through physical time 40.
* Certified empirical paired hidden laws or response fields at that budget.
* A computable admission radius merely because an existence theorem names one.
* A whole-circle/time supremum bound merely from checking a finite plot grid.
* Population existence for a broader law or longer time because the numerical
  recurrence can be run there.
