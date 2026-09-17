# First-layer balance and its angular perturbation defect

2026-09-16. Root's analytic route, frozen before comparison with the
independent mode and orthogonal-endpoint routes. Scientific inputs:
docs/NOTATION.md, the exact closure equations in docs/global_nonlinear.md
C.4.7.9 and C.4.7.10 C.1/D.3, docs/observable_p1.md, and this study's
proved three-coordinate flow. This is a continuation of the potential
question. No experiment or external convergence theorem is used.

## 1. Exact model and all three tangent contributions

Take m finite unit inputs u_i in R^d, equal probabilities 1/m and arbitrary
fixed labels. The applications here have m=3 and unit labels. Keep the
canonical initialized joint marks and moving w,c,M. Write

    z_i=w.u_i, H_i^1=tanh(z_i), a_i=E1[b1 H_i^1],
    Z_i^2=b2^T M a_i, H_i^2=tanh(Z_i^2), f_i=E2[c H_i^2],
    d_i=E2[b2 c sech^2(Z_i^2)], q_i=b1^T M^T d_i,
    r_i=f_i-y_i.

The physical gradients are

    grad_c f_i=H_i^2,
    grad_M f_i=d_i a_i^T,
    grad_w f_i=sech^2(z_i) q_i u_i.

All gradients use the fixed population-L2/Frobenius metric. Their full
Gram (without a data-probability factor) is therefore EXACTLY

    K_ij = E2[H_i^2 H_j^2]
         + (a_i.a_j)(d_i.d_j)
         + (u_i.u_j) E1[sech^2(z_i) sech^2(z_j) q_i q_j].       (1)

Each of the three matrices in (1) is positive semidefinite, although
individual off-diagonal entries can have either sign. Formula (1) follows
by taking the inner product of the three displayed gradients, using
<d_i a_i^T,d_j a_j^T>F=(d_i.d_j)(a_i.a_j). For signed predictions
m_i=y_i f_i with unit labels, conjugate K by diag(y). Their exact dynamics
is m_dot=-(2/m)diag(y)K diag(y)(m-1). No layer is frozen.

The third term is first-layer interaction, including both its input angle
and the backward fields passed through the actual M transpose. The second
term couples retained first-layer features a_i to upper backward fields
d_i. Consequently an upper-hidden activation Gram alone discards two
positive sources of full residual-direction dissipation.

One useful bound is available when the input Gram G_ij=u_i.u_j is positive
definite, as for small perturbations of d=m orthogonal inputs. For every
real vector x,

    x^T K^(w) x
      =E1 |sum_i x_i sech^2(z_i)q_i u_i|^2
      >=lambda_min(G) sum_i x_i^2 E1[sech^4(z_i)q_i^2].         (2)

This is the ordinary input Gram inequality inside the expectation. It
also holds after label conjugation. At an orthogonal reference it is an
equality. Thus first-layer training can protect disagreement directions
even when the upper activation Gram is poorly conditioned. To turn (2)
into a uniform rate, the indicated backward energies must themselves
remain controlled below; that is not assumed or proved here. At c=0
they vanish, whereas the initialized upper activation Gram is positive
for the reference triple. This explains why the contributions should be
combined rather than treating any one as sufficient at every time.

## 2. A new exact lower-layer/middle-layer invariant at orthogonality

Define the current-state quantity

    B(S)=||M||F^2-E1 sum_i sinh^2(w.u_i).                       (3)

It is finite on every finite-time initialized characteristic solution.
Indeed w=g+v with bounded v on each such interval, and each g.u_i is a
unit-variance Gaussian. Exponential Gaussian moments control sinh and
its derivatives. The finite-time velocity envelopes justify
differentiation under the expectation by an integrable Gaussian majorant.

For the middle block, direct use of its physical equation gives

    (||M||F^2)_dot
      =-(4/m) sum_j r_j d_j^T M a_j
      =-(4/m) sum_j r_j E1[tanh(z_j) q_j].                     (4)

For the first-layer term, z_i_dot=-(2/m)sum_j r_j G_ij
sech^2(z_j)q_j. Consequently

    (E1 sum_i sinh^2 z_i)_dot
      =-(2/m) sum_ij r_j G_ij
                    E1[sinh(2z_i) sech^2(z_j) q_j].           (5)

Since G_jj=1 and sinh(2z_j)sech^2(z_j)=2tanh(z_j), subtraction
of (5) from (4) proves the exact identity

    B_dot=(2/m) sum_(i!=j) r_j G_ij
                   E1[sinh(2z_i) sech^2(z_j) q_j].            (6)

For mutually orthogonal unit inputs all terms on the right vanish.
Thus B is CONSERVED along the full trained closure, for any labels.
Its initialized value is explicit:

    B(S0)=||D||F^2 - m (exp(2)-1)/2,                          (7)

because E sinh^2 G=(E cosh(2G)-1)/2=(exp(2)-1)/2.

This is a genuine relation between first-layer motion and middle-layer
growth, absent from the previous scalar contrast argument. It is not
itself a nonnegative Lyapunov potential or a loss bound: it is an exact
balance law that helps identify what geometry-dependent corrections
would have to cancel or exploit.

## 3. The perturbation terms are explicit

For a perturbation u_i(epsilon) approaching the fixed orthogonal input
vectors, with the dictionary held fixed, write
G=I+epsilon A+O(epsilon^2), where A is symmetric with zero diagonal.
Equation (6) identifies the first-order defect: each new cross-input
coefficient A_ij multiplies the current mixed statistic

    r_j E1[sinh(2z_i) sech^2(z_j) q_j].                       (8)

It is not a raw hidden distance. It contains the first input's activation,
the second input's first-layer gate, its residual, and its backward field
through both moving hidden blocks. Evaluating the smooth integrands at
the reference trajectory gives the first-order coefficient on a fixed
finite horizon; the exact identity (6) does not require a Taylor expansion.

Here is a nonformal finite-horizon statement. If max_(i!=j)|G_ij|<=epsilon
and the canonical trajectories are followed through a fixed T, the usual
uniform finite-time bounds give finite constants A_T,Q_T with
||w-g||infinity<=A_T and max_j||q_j||infinity<=Q_T. For unit u,

    E1 |sinh(2w.u)| <= exp(2A_T) E exp(2|G|), G~N(0,1).

Let C_T be Q_T times the right side. Using sech^2<=1 and
(1/m)sum_j |r_j|<=sqrt(L) in (6) gives

    |B_dot| <= 2(m-1)epsilon C_T sqrt(L),
    |B(t)-B(0)| <= 2(m-1)epsilon C_T integral_0^t sqrt(L(s)) ds. (9)

The constants are uniform over these unit-input perturbations on [0,T]
at the fixed prescribed p=1 dictionary, by the canonical finite-time
envelopes; they are not uniform in closure order. For unit labels L<=1, so this
is at most 2(m-1)epsilon C_T T. It is NOT an all-time smallness estimate:
no uniform control of C_T or the displayed integral has been supplied.

## 4. Why a lower-activation-only correction cannot universally cancel it

This is a narrow integrability result for a particular natural ansatz,
not a no-go theorem for general potentials. Assume m=d and the inputs
are linearly independent, so z=(w.u_i)_i is a coordinate system on w.
Seek a C2 scalar function J(z) such that replacing sum sinh^2 z_i by
J(z) in (3) cancels the middle-block derivative POINTWISE, coefficient
by coefficient for arbitrary residual/backward drives.

Writing (5) with grad J shows that this cancellation requires

    G grad_z J(z) = (sinh(2z_1),...,sinh(2z_m))^T,
    grad_z J(z) = G^(-1) sinh(2z).                           (10)

The necessity here concerns this pointwise, arbitrary-drive matching
requirement; no claim is made that actual canonical backward drives
can be chosen independently. It is also sufficient for that requirement.

For i!=j the two mixed derivatives demanded by (10) are

    partial_j partial_i J =2(G^(-1))_ij cosh(2z_j),
    partial_i partial_j J =2(G^(-1))_ij cosh(2z_i).             (11)

Equality for every z forces (G^(-1))_ij=0. Since diag G=1, this
occurs for all pairs precisely when G=I. At first order,
G^(-1)=I-epsilon A+O(epsilon^2), so a putative J=J0+epsilon J1
would require grad J1=-A sinh(2z). Its off-diagonal curl is already
nonzero when A_ij!=0 and cosh(2z_i)!=cosh(2z_j).

Therefore a universal correction depending only pointwise on the lower
preactivations cannot preserve this exact balance after a generic angular
perturbation. A potential may instead involve M, the backward fields,
population couplings, a nonconstant metric, or inequalities rather than
exact cancellation. These possibilities are not excluded. This identifies
a concrete reason to search for forward/backward terms, as the user suggests.

## 5. The corresponding first-layer coordinate metric

Continue to assume m=d and an invertible input-coordinate matrix, as
in Section 4. This ensures that these coordinates retain every row direction.

The transformed coordinates rho_i=T(z_i),

    T(z)=z/2+sinh(2z)/4,     T'(z)=cosh^2 z,

are often useful because T'(z_i)sech^2(z_i)=1. For orthogonal inputs
their driven equations separate by input. For general full-rank G,

    rho_i_dot=-(2/m)sum_j r_j G_ij
                   cosh^2(z_i) sech^2(z_j) q_j.              (12)

The physical metric under this coordinate change is exact. If
D(z)=diag(sech^2(z_i)), then dz=D d rho, and

    |d w|^2=d z^T G^(-1)d z
           =d rho^T D G^(-1)D d rho.                        (13)

This shows precisely how input angles and activation gates interact in
first-layer geometry. It does not license ignoring metric motion. Along
a trajectory the coefficient matrix in (13) has derivative

    D_dot G^(-1)D + D G^(-1)D_dot,
    (D_dot)_ii=-2 sech^2(z_i)tanh(z_i) z_i_dot.               (14)

Any quadratic distance based on (13) must include (14), together with
the two derivatives of its displacement vector. The entries can be
small in saturated regions. Equation (13) remains exactly the local
physical metric in the changed coordinates, but a bare shrinking
coordinate quadratic does not prove physical convergence without the
appropriate comparison and variation terms.

## Conclusions at the actual proved scope

Equations (1), (2), (6), (9), (11) and (13)--(14) are derived identities
or estimates for the exact closure with their stated hypotheses. They
identify previously unused first-layer dissipation and explicit
geometry-dependent balance defects. They do not prove an exponentially
decreasing generic potential. The unrestricted cancellation obstruction
concerns only the pointwise lower-only primitive ansatz, not a coupled
full-state Lyapunov function.

Post-audit clarification: the fresh review examined the pre-clarification
SHA-256 297cb7217b9318422548d0965b55e8e5f8588bf6b23ad69eafb2972f6ac3c3aa.
Its three scope clarifications above make explicit actual-vector
perturbations, fixed-dictionary envelopes and m=d in the metric formula.
No numbered formula or mathematical conclusion changed. The complete
review is perturbation_lower_balance_audit.md.
