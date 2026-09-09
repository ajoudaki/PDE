# Two samples: an initial feature-learning certificate

Status: main derivation, not independently audited. This is an initial-law
lemma and a certificate for a sufficiently regular constructed path. It
does NOT construct the uncut path. CONTRACT.md fixes initialization,
sample normalization, and raw metric. The sole probabilistic dependency
is the fixed finite-program forward/transpose identification in
TWO_SAMPLE_SOURCE_BASELINE.md, Section 3, ultimately the stated local
proof. No nonlinear continuation conclusion is assumed.

Let phi(z)=1+z+epsilon arctan z with a fixed epsilon>0, and put
p_a=y_a/2. The proof works for every fixed rho in [-1,1), including
opposite labels and antipodal inputs. All expectations below are within
the displayed neuron population. Write W^(4)=C and
H=(y_1 H^(3)_1+y_2 H^(3)_2)/2. The scalar feature direction is the
gradient of g=E_3[C H] in the raw metric.

## 1. Initial forward pairs and the first transpose return

At layer one the Gaussian preactivation pair has covariance Gamma.
Its feature pair has strictly positive definite uncentered second-moment
matrix. Indeed, for -1<rho<1 a vanishing linear combination of the two
features would vanish on all R^2, which is impossible for a nonconstant
activation. At rho=-1, write phi(z)=1+psi(z) with psi odd and strictly
increasing. A vanishing combination of phi(Z),phi(-Z) would say
(u_1+u_2)+(u_1-u_2)psi(Z)=0, forcing u_1=u_2=0. Subsequent fresh forward
Gaussian calls thus give nondegenerate Gaussian preactivation pairs in
populations two and three. Their feature Gram matrices are positive
definite by the same full-support argument. All these variables have
every finite moment.

Define, in population three,

    beta^(3)_a = H_0 phi'(Z^(3)_{a,0}).

Their uncentered second-moment matrix S_3 is positive definite. To prove
this, suppose E[(u_1 beta^(3)_1+u_2 beta^(3)_2)^2]=0. The preactivation
pair has positive density everywhere. Continuity makes

    [p_1 phi(z_1)+p_2 phi(z_2)]
        [u_1 phi'(z_1)+u_2 phi'(z_2)] = 0

an identity on R^2. For each fixed z_2, the first factor, as a function
of z_1, is strictly monotone and has at most one zero. Thus the second
factor vanishes for every z_1 by continuity. Its derivative in z_1
gives u_1 phi''(z_1)=0. Since epsilon>0 and phi'' is not identically
zero, u_1=0. Positivity of phi' then gives u_2=0. This proves S_3>0.

The reused transpose of W^(3)_0 is NOT a fresh iid-coordinate claim.
The fixed-program rule gives the joint empirical-average limit

    (W^(3)_0)^* beta^(3)_a
       = G^(2)_a + sum_b H^(2)_{b,0}
                              E_3[partial_{z_b} beta^(3)_a],       (1)

where (G^(2)_1,G^(2)_2) is centered Gaussian with covariance S_3 and
independent of the initial population-two forward sources. The second
term is precisely the response forced by the previous two forward uses;
the first is the unexplored Gaussian randomness. Formula (1) uses full
second moments, not the residual after projection onto forward features.

For clarity the two derivatives in this expression are exactly

    partial_{z_b} beta^(3)_a
       = p_b phi'(z_b) phi'(z_a)
           + 1_{a=b} [sum_c p_c phi(z_c)] phi''(z_a).

They have finite expectations. The output beta is an unbounded smooth
coordinate instruction with polynomially bounded derivatives, so the
bounded-derivative version of the dependency is applied first to smooth
caps. Removal at this SINGLE fixed transcript is justified by Gaussian
moments and the matrix operator bound: forward cap differences vanish
in RMS; backward input differences vanish in RMS; the transpose changes
by at most its bounded operator norm times that RMS difference. The
displayed expected derivatives converge by Gaussian dominated bounds.
This is a fixed-transcript argument, not mesh-uniform removal.

## 2. The second transpose return cannot lose the noise

Set

    beta^(2)_a = phi'(Z^(2)_{a,0}) (W^(3)_0)^* beta^(3)_a.

Conditionally on the initial population-two forward pair, its covariance
is diag(phi'(Z^(2)_{1,0}),phi'(Z^(2)_{2,0})) S_3 diag(phi').
Since phi'>=1, its minimum eigenvalue is at least lambda_min(S_3)>0.
Consequently its uncentered second-moment matrix S_2 is positive definite.

Reusing the transpose of W^(2)_0 in turn gives

    (W^(2)_0)^* beta^(2)_a
       = G^(1)_a + sum_b H^(1)_{b,0}
                         E_2[partial_{xi^(2)_b} beta^(2)_a],       (2)

where G^(1) has covariance S_2 and is independent of the initial
population-one root pair. The derivative in (2) freezes all deterministic
response coefficients and covariances from (1); it includes the actual
dependence of its response term on H^(2). The Gaussian source G^(2) is
an independent named source in this derivative. All expressions have
finite moments; the same finite-transcript cap argument justifies (2).
Define beta^(1)_a=phi'(Z^(1)_{a,0}) (W^(2)_0)^* beta^(2)_a.

## 3. Nonzero acceleration in every hidden parameter block

The following tensors and first-layer field are well-defined:

    V^(1) = (1/d) sum_a p_a beta^(1)_a x_a,
    V^(2) = sum_a p_a beta^(2)_a tensor H^(1)_{a,0},
    V^(3) = sum_a p_a beta^(3)_a tensor H^(2)_{a,0}.         (3)

A population tensor u tensor v acts on w as u E[v w]. Finite tensors
are u v^T/n. Its HS norm is the product of the two ordinary L2 norms.

The hidden feature map H has bounded linearization J_0 from the raw
hidden metric to population-three L2; direct differentiation and
adjunction give V=J_0^* H_0. This is a bounded directional linearization
with a strong path chain rule, not a claim of Frechet differentiability
of a nonlinear L2 Nemytskii map.

Both V^(2),V^(3) have strictly positive HS norm. For each, the squared
norm is sum_{a,b} p_a p_b E[beta_a beta_b] E[H_a H_b]. Both Gram
matrices are positive definite, and diag(p) is invertible, so this
equals the positive trace of the product of two positive definite
matrices. For V^(1), conditional covariance from (2) gives

    d E_1 ||V^(1)||^2
       >= lambda_min(S_2) sum_a p_a^2 ||x_a||^2/d
       = lambda_min(S_2)/2 > 0.                           (4)

This bound does not invert Gamma and holds for antipodal inputs.

On any constructed strong feature path for which the initial backward
fields satisfy delta^(ell)_a(s)=s beta^(ell)_a+o_L2(s), (3) implies

    hidden_state(s)=hidden_state(0)+(s^2/2)V+o(s^2),
    C(s)=s H_0+o_L2(s).                                  (5)

These initial derivative limits follow, for example, when the path is
strongly continuous in state, C(s)/s->H_0 in L2, and gates are bounded
and continuous: apply the fixed-factor multiplier convergence backwards,
using bounded current operators and phi'>0. Thus a C1 strong solution
with C'=H suffices; an Lp-in-time differentiability assumption is not
silently required. The hidden vector field divided by s converges by
the rank-one difference bound. Integrating proves (5).

In particular every hidden parameter block moves at order s^2. This is
not a kernel or frozen-hidden-layer limit; epsilon stays strictly
positive independently of width and physical time.

## 4. Hidden features and the kernel also move

The initial hidden preactivation acceleration in sample a at layer one
is sum_b Gamma_ab p_b beta^(1)_b. Conditionally on Z^(1)_0, its variance
is at least lambda_min(S_2) sum_b Gamma_ab^2 p_b^2 phi'(Z_b)^2, hence
at least lambda_min(S_2)/4. It is nonzero for each sample.

Let U^(ell)_a denote the acceleration of Z^(ell)_a obtained by applying
the forward linearization to V, and use phi'(Z^(ell)_{a,0}) U^(ell)_a
for the feature acceleration. Product rules and adjunction give

    sum_a p_a E_2[beta^(2)_a U^(2)_a]
         = d E_1||V^(1)||^2 + ||V^(2)||_HS^2 > 0,
    sum_a p_a E_3[beta^(3)_a U^(3)_a]
         = ||V||_hidden^2 > 0.                            (6)

For the first equality, expand U^(2)_a=V^(2)H^(1)_a+
W^(2)_0[phi'(Z^(1)_a)(V^(1) dot x_a)]. The two terms give the two
squared norms by (3). The second equality adds the third matrix block
to the same calculation. Thus at least one sample acceleration in each
upper layer is nonzero. The initialization/sample-reflection symmetry
maps their joint law by exchanging samples, and maps U to the exchanged
U. Their squared norms are equal. Both sample accelerations are
therefore nonzero. Since phi'>=1, every hidden feature acceleration
is nonzero as well.

Finally the projected output kernel and total kernel satisfy

    kappa_4(s)=E_3[H(s)^2]
        =kappa_0+s^2 ||V||_hidden^2+o(s^2),
    kappa(s)=kappa_0+2s^2 ||V||_hidden^2+o(s^2).             (7)

Indeed H(s)=H_0+(s^2/2)J_0 V+o_L2(s^2), and
E[H_0 J_0 V]=||J_0^*H_0||^2=||V||^2. The sum of the three hidden
kernel blocks is the squared hidden gradient, s^2||V||^2+o(s^2).
The strong path chain rule gives the expansion of H from (5), or by
integrating H'=J_s hidden_state'. Bounded gates and fixed-factor
convergence suffice for J_s V->J_0 V.

The physical clock has s(t)=2t+o(t) initially, so the same conclusions
hold at positive sufficiently small physical times. Equation (7) is a
strict feature-learning certificate, not a claim that every separate
hidden velocity is nonzero at every later time. The latter stronger
property is not proved here. Nonaffinity of the activation under the
hidden distributions for ALL finite times is a separate requirement;
the affine-baseline nondegeneracy/approximation-error argument in
SYMMETRY_RADIAL_CLOCK.md supplies it only after nonlinear comparison
and continuation have actually been constructed.
