# First raw metric and the residual-weighted first kernel

Root draft, 2026-09-06. UNREVIEWED. This is an elementary consequence
of explicitly stated joint first-position/velocity compactness, not a
mean-field theorem. It identifies two additional observables without
assuming any unweighted reverse-field moment. No external theorem is
invoked. All norms below are ordinary norms.

Fix two deterministic inputs x_1,x_2 in R^d with squared norms d and
Gram matrix C_ab=x_a^T x_b/d. Write X=[x_1,x_2]. Suppose each first
weight row follows the exact two-sample raw rule

    dot W^(1)_{n,i} = (1/d) X d_{n,i},
    d_{n,i,a}=c_{n,a} delta^(1)_{n,a,i},
    z_{n,i}=(z^(1)_{n,1,i},z^(1)_{n,2,i})=X^T W^(1)_{n,i}.

Here rows are written as column vectors for these three formulas only.
The controls c_{n,a}=-2r_{n,a} contain residuals; delta does not.
All row trajectories satisfy the integral evolution equation and are
absolutely continuous. In GF the formulas hold at every time. For exact raw GD they hold
almost everywhere on each raw affine cell with node controls/deltas.
Let v_{n,i}=dot z_{n,i}. Consequently

    v_{n,i}=C d_{n,i},
    d |dot W^(1)_{n,i}|^2=d_{n,i}^T C d_{n,i}.        (1)

For fixed -1<rho<1, C is positive definite. Hence

    d_{n,i}=C^(-1)v_{n,i},
    dot W^(1)_{n,i}=(1/d) X C^(-1)v_{n,i},
    d |dot W^(1)_{n,i}|^2=v_{n,i}^T C^(-1)v_{n,i}.    (2)

All operator constants in these formulas are finite for the fixed
input pair. They need not remain bounded as rho approaches an endpoint.

At rho=-1 assume the exact anti-odd network invariance: both hidden
activations odd, their derivatives even, labels (1,-1), x_2=-x_1.
For every raw parameter state forward fields are opposite, readout
predictions are opposite, deltas and reverse fields are equal, and
controls are opposite. Thus d_{n,i}=(b,-b), v_{n,i}=2d_{n,i}.
Put C^+=C/4. Then (2) remains valid with C^+ in place of C^(-1):
X C^+v/d is the actual row velocity and d times its ordinary squared
row norm is v^T C^+v=|v|^2/2. This is one first-weight-row energy,
not twice it.
No assertion here covers rho=1.

For both cases write D=C^(-1) or C^+, respectively. Suppose a
deterministic sequence of empirical joint laws

    mu_n=(1/n) sum_i delta_(z_{n,i}(.),v_{n,i}(.))

converges in quadratic Wasserstein distance on
C([0,T];R^2) times L^2([0,T];R^2), using squared metric
||z-z'||_infty^2+||v-v'||_L2^2. Suppose also the time-integrated mean
squared velocity is uniformly bounded. The latter already follows
from this Wasserstein convergence, but it is stated to expose its use.
Then the following conclusions hold.

First, joint laws of raw first-weight increments and velocities
converge in the corresponding C times L^2 topology, since the maps

    (z,v) -> ((1/d) X D [z(.)-z(0)], (1/d) X D v(.))

are fixed bounded linear maps. To verify the assertion directly,
apply this map to couplings whose expected squared input distance
tends to zero; their expected squared output distance is bounded by
a fixed constant times that input cost. No identification of original
neuron indices across widths is claimed. The unchanged orthogonal
part of an initial row is not reconstructed from the two evaluations;
to include full rows one must include that initial part in the joint
law separately. Increments and velocities need no such extra premise.

Second, the raw first-matrix kinetic energy has no defect:

    lim_n (d/n) integral_0^T ||dot W^(1)_n(t)||_F^2 dt
      = integral E_mu[v(t)^T D v(t)] dt.                 (3)

Indeed |u^T D u-v^T D v| is at most
||D||_op |u-v| (|u|+|v|); Cauchy--Schwarz in time and in a coupling
proves convergence. The same proof holds on every fixed measurable
time subset, since restriction decreases the L^2 coupling error.

Third, define the NODE-residual-weighted first raw kernel

    J_{n,ab}(t)=c_{n,a}(t)c_{n,b}(t) K^(1)_{n,ab}(t)
      = C_ab (1/n) sum_i d_{n,i,a}(t)d_{n,i,b}(t),
    K^(1)_{n,ab}=C_ab (1/n)sum_i
                       delta^(1)_{n,a,i}delta^(1)_{n,b,i}.  (4)

For GD these are node deltas/controls throughout a cell, not the
recomputed nonlinear interpolation kernel. This distinction matters.
The entire two-by-two matrix J_n converges in L^1([0,T]) to

    J_ab(t)=C_ab E_mu[(D v(t))_a (D v(t))_b]             (5)

for almost every time. Precisely, J is the expectation of the
matrix-valued L^1 function C_ab(Dv)_a(Dv)_b. The product map from
L^2 velocity paths to matrix-valued L^1 is continuous by the estimate
below and has norm bounded by a constant times ||v||_L2^2, so this
expectation exists. No evaluation functional at a fixed time on L^2
is being assumed.

To prove this, couple v_n and v with L^2 mean-square error tending
to zero, and set e_n=Dv_n, e=Dv. For every a,b,

    integral |E[e_{n,a}e_{n,b}]-E[e_a e_b]| dt
     <= ||e_n-e||_(L2(dt times coupling))
          (||e_n||_(L2(dt times coupling))
                         +||e||_(L2(dt times coupling))).

The right side tends to zero. This proves the full matrix claim
without evaluating a velocity at a prescribed time. Also, summing
the entries of J_n in (4) recovers the averaged first raw speed in (1),
and summing (5) recovers E_mu[v^T D v] since D C D=D. This is an
algebraic speed identity. In particular it is not an exact nonlinear
loss-dissipation identity for raw affine GD interpolation: there the
loss derivative pairs the current gradient with the node velocity.

These statements remain only subsequential compactness consequences
if the supplied joint laws have only W2 subsequential compactness.
Under the deterministic premise, each limiting measure and its kernel
are deterministic, although different subsequences may have different
limits and the particle law may be non-Dirac. Its population force
equation is not identified. For explicitly random arrays these
continuous-map conclusions inherit an explicitly supplied W2
convergence-in-probability premise. Compact containment alone supplies
no convergence in probability or unique limit. An additional argument
identifying the limit would be required; deterministic coupling algebra
alone does not provide a new probability quantifier.

In particular (5) does NOT give the unweighted first kernel where a
control vanishes. There is no division by c in the proof. Nor does it
control the difference between node and recomputed GD kernels, higher
reverse-field moments, the second hidden layer, population uniqueness,
or any all-angle joint GD/GF/MF conclusion. These remain separate
obligations. The first compactness notes are relevant sources for
the premise, not an assertion that these missing obligations follow.
