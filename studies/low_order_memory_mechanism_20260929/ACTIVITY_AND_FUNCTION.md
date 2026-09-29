# Finite learning activity controls the entire predictor

Continuation, 29 September 2026. Parent derivation for MODEL.md. This result
concerns the finite autonomous tanh closure, any finite q, width n, sample
count m and depth L. It makes no dense comparison and assumes no independent
neurons. Norms and first/readout mobilities are those of MODEL.md.

## 1. Residual direction determines the path in activity

Let X denote the complete stored state: W1, w, tau and all B,C. On an
interval with rho>0, write e_a=r_a/rho, so m^{-1}sum e_a^2=1, and use
s=tau-1 as time. The exact equations become

    dW1/ds=-(2/m)sum_a e_a delta_a^1 x_a^T/sqrt(d),
    dw/ds=-(2/m)sum_a e_a h_a^L,
    dB_k/ds=h_a^(ell-1)
              -[kB_k+sum_(j<k)(2j+1)B_j]/(1+s),
    dC_k/ds=e_a delta_a^ell
              -[kC_k+sum_(j<k)(2j+1)C_j]/(1+s).

Thus the residual magnitude controls physical speed; its normalized
direction controls how credit is written along the activity path. The forward
memory update and interval dilation are independent of that direction. This is
an exact controlled-system representation, not a closed ODE for the residuals
alone: the fields still depend on X.

For a single sample before first fit, e is constant. All positive targets
therefore follow the same activity-parametrized path from the same initializer,
stopping at their first target level if that level is reached. Negative targets
follow the same hidden path with reversed readout: w -> -w, r -> -r,
delta -> -delta, leaving r delta and every C invariant. This statement uses
zero initial readout. The internal forward clock starts identically in both
runs. A target-independent path is not a proof that its training prediction
ever reaches an arbitrary prescribed level.

## 2. Explicit state and spatial bounds from an activity budget

Suppose a solution is followed while s<=S<infinity. Define R_x by
R_x^2=m^{-1}sum_a ||x_a||^2/d. Let K_ell=||W0_ell||_op for ell>=2 and
K_1=||W1(0)||_op/sqrt(n). All constants below are deterministic; the Gaussian
initializer is used only to produce the actual matrices, not in the proof.

Because tanh is bounded by one and the initial readout vanishes,

    ||w||/sqrt(n) <= 2s <= 2S.

Indeed integrate the readout equation and use Cauchy--Schwarz in samples:
m^{-1}sum |e_a| ||h_a^L||/sqrt(n)<=1.

Let beta_ell uniformly bound ||delta_a^ell||/sqrt(n) over the samples and
activity interval. One may choose the following descending recursion:

    beta_L=2S,
    M_ell=K_ell+2 beta_ell sqrt(S(1+S)),
    beta_(ell-1)=M_ell beta_ell,    ell=L,...,2.       (1)

Here M_ell bounds ||W_ell||_op, uniformly in q and n once the initial K's
and S are fixed. To prove it, define per-sample normalized memory energies

    EB_a=(1/(n tau))sum_k(2k+1)||B_(a,k)||^2,
    EC_a=(1/(n tau))sum_k(2k+1)||C_(a,k)||^2.

Orthogonal projection is a contraction. With the constant forward prefix and
zero backward prefix, this gives

    EB_a <= tau,
    (1/m)sum_a EC_a
       <= integral_0^s (1/m)sum_a e_a(v)^2
                         ||delta_a^ell(v)||^2/n dv
       <= S beta_ell^2.

The same bounds follow by integrating the exact memory energy law. Weighted
Cauchy--Schwarz over modes and then samples gives

    ||W_ell-W0_ell||_op
       <= (2/m)sum_a sqrt(EB_a EC_a)
       <= 2 beta_ell sqrt(S(1+S)).                   (2)

The actual transpose and |tanh'|<=1 imply the backward step in (1).
This is a descending estimate, so no unknown lower-layer bound is used to
bound a higher layer. Finally the first-layer update gives

    ||W1||_op/sqrt(n) <= K_1+2S beta_1 R_x.         (3)

For any two inputs x,x' in R^d, repeated use of the Lipschitz constant one
of tanh now yields

    |f_t(x)-f_t(x')|
      <= [2S (K_1+2S beta_1 R_x)/sqrt(d)]
          (product_(ell=2)^L M_ell) ||x-x'||.       (4)

The bound has no explicit q or n dependence. It is conditional on the
actual activity budget and initial operator bounds, and the displayed depth
recursion can be large. It is not a typical-case sharp bound or a proof that
S stays bounded. Even though learned matrix rank depends on q, every order
has this same valid class of spatial regularity bounds at a fixed activity
budget.

## 3. Finite total activity implies a terminal whole-input function

**Theorem.** For this finite tanh closure, if

    S_infinity=integral_0^infinity rho(t) dt < infinity,

then every stored coordinate and every physical weight converges to a finite
limit, the training residual tends to zero, and f_t converges uniformly on
every compact input set to the predictor defined by those limiting weights.
It also converges in L2(mu) for every probability measure mu on R^d. The
L2 conclusion does not require a finite second input moment, since outputs
are uniformly bounded. This is a conditional direct theorem, not an assertion
of finite activity for arbitrary datasets.

**Proof.** Bounds (1)--(3) bound the physical states throughout the trajectory.
The energy bounds above bound every B and C at any fixed finite q,n, and
1<=tau<=1+S_infinity. In activity coordinates each raw vector field displayed
in Section 1 is bounded: e_a has magnitude at most sqrt(m), responses and
moments are bounded, and denominators stay away from zero. Thus in physical
time each coordinate velocity has magnitude at most a fixed constant times
rho. Integrability implies each coordinate is Cauchy and has a finite limit.
Weight reconstruction is continuous since tau>=1. The residual map is
continuous in the weights, so rho has a limit. A positive limit contradicts
integrability; hence all training residuals tend to zero.

For a compact set contained in ||x||<=R, the first preactivation difference
between two states is bounded uniformly by R||Delta W1||_op/sqrt(d).
Successively propagate it using

    ||h_new^ell-h_old^ell||/sqrt(n)
      <= ||Delta W_ell||_op
         + ||W_old_ell||_op
                     ||h_new^(ell-1)-h_old^(ell-1)||/sqrt(n).

The bounded readout then gives uniform convergence of outputs. For arbitrary
mu, convergence is pointwise and |f_t|<=2S_infinity. Given a tolerance, split
the integral into a large compact ball of arbitrarily high mu mass and its
complement; use compact-uniform convergence on the ball and the common
output bound outside. This proves L2 convergence without an appeal to a
spatial mesh or input-moment hypothesis. QED.

At fixed q and n the same proof gives

    sup_(||x||<=R)|f_t(x)-f_infinity(x)|
       <= C_(R,q,n,S_infinity,initialization,data,L)
                      integral_t^infinity rho(u)du.             (5)

No width- or order-uniform claim is made for this convergence-rate constant.
Equation (4)'s spatial Lipschitz bound is separately uniform under its stated
initial-operator and activity bounds. Uniform convergence over unbounded
R^d does not follow from convergence of weights; compact-uniform and L2(mu)
are the asserted topologies.

## 4. Positive initial representation feedback at every depth

Now take one nonzero input x0, a fixed finite q, zero readout, and use
u=2 integral_0^t |r(v)|dv, twice the preceding activity. Consider the universal
positive-target path. Write theta for all hidden weights, M for the diagonal
hidden mobility (n on W1 coordinates, one on hidden-matrix coordinates), and
H(theta)=h^L_theta(x0). Put

    V(theta)=||H(theta)||^2/(2n),  H=H(theta0),
    b_x=D_theta h^L_theta(x)[M grad V(theta0)] at theta0,
    b=b_(x0), alpha=||H||^2/n.

These typed derivatives are ordinary finite-dimensional derivatives of the
static nonlinear feature map. At the universal path's origin,

    w(0)=0, w'(0)=H, theta'(0)=0,
    theta''(0)=M grad V(theta0), theta'''(0)=0.      (6)

For W1 this follows by differentiating delta once: its readout is uH to
first order, giving n grad_(W1)V. For a hidden link, B0/tau equals its
initial feature plus O(u^3), every B_k for k>0 is O(u^3), and every C_k
is O(u^2). Only C0 B0/tau contributes to the second derivative. Its C0
source is -delta/2 in the u clock, giving grad_(W_ell)V. The absence of
third derivatives follows from theta'(0)=0, w''(0)=0 and these same moment
orders: the direct hidden velocity is u times its initial value plus O(u^3).
The raw activity system is smooth near u=0 with tau=1+u/2, so Taylor
remainders are valid at fixed finite q,n.

Consequently, uniformly for x on each compact input set,

    theta(u)=theta0+(u^2/2)M grad V(theta0)+O(u^4),
    h_u^L(x)=H_x+(u^2/2)b_x+O(u^4),
    w(u)=u H+(u^3/6)b+O(u^5),
    F(u,x)=u kappa_x+u^3 c_x+O(u^5),              (7)

where H_x=h^L_(theta0)(x), kappa_x=H^T H_x/n and

    c_x=b^T H_x/(6n)+H^T b_x/(2n).

At the training input,

    F(u,x0)=alpha u+beta u^3+O(u^5),
    beta=(2/3) grad V(theta0)^T M grad V(theta0) >=0. (8)

The equality follows from H^T b/n=grad V^T M grad V. For tanh, x0!=0,
and the Gaussian initializer, H and the preceding layer's feature are
nonzero almost surely. The top hidden gradient
(H odot tanh'(z^L))(h^(L-1))^T/n is therefore nonzero almost surely,
so beta>0. This works at any fixed hidden depth L>=2 and finite width.

The result is an intrinsic statement about the first nonlinear response:
hidden learning initially moves uphill in the training feature's squared
norm, and strengthens prediction per unit accumulated learning activity.
It does not assert that V keeps increasing, that larger prediction means
better test risk, or that depth improves conditioning. The cubic coefficient
is identical for every fixed finite q; temporal order already one is enough
to carry this first feature-learning feedback loop.

If alpha>0, F'(u,x0)>alpha/2 on a sufficiently small interval. Every
sufficiently small positive target y has a unique level u_y there. Physical
time obeys u'=2(y-F(u,x0)); it approaches u_y exponentially and cannot cross
the equilibrium. Its whole-input terminal predictor has the expansion

    f_infinity^y(x)=y kappa_x/alpha
       +y^3[c_x/alpha^3-kappa_x beta/alpha^4]+O_K(|y|^5). (9)

Negative labels follow by readout sign reversal. Existence of u_y follows
from monotonicity and the intermediate value theorem; its expansion follows
by substitution u_y=y/alpha-beta y^3/alpha^4+O(y^5) in (7).
The error is uniform on compact test sets at fixed width, order and
initializer. The small-label threshold here is local and realization
dependent, not a width-uniform threshold. The cubic correction in (9)
vanishes at x0, but need not vanish elsewhere. This is a direct description
of how nonlinear learning first changes the interpolating function away
from the observed input.

## 5. A direct multi-input local fitting corollary

The local-return theorem in INTRINSIC_GEOMETRY_ROUTE.md also applies at the
prescribed initialization for the zero-label dataset. There w=0 and C=0,
all backward fields vanish, and the only nonzero prediction kernel block is
G0=H0^T H0/n, the initial last-feature Gram on the m training inputs. Thus
the theorem's coefficients are A=2G0/m and c=0. If G0 is positive definite,
its strict local contraction condition holds. The theorem consequently
gives a neighborhood of zero label vectors on which this exact finite
closure fits exponentially and has a finite terminal state and whole-input
predictor. This holds at arbitrary finite depth and fixed finite q,n.

The neighborhood depends on the realized initializer, data, width and order.
No Gaussian positive-definiteness theorem for arbitrary input configurations
is assumed here, and this does not give a width-uniform label threshold.
The observation is a deterministic corollary of the proved local trapping
argument; it does not replace general multi-input fitting by a claim about
the scalar benchmark.
