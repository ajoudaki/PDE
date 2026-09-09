# Explicit activation bounds at depths five, six, and every fixed finite depth

2026-09-07. This proof consists of this assembly, AFFINE_CERTIFICATE.md,
SOURCE_RESPONSE.md, and POPULATION_AND_MOMENTS.md. Review status is
recorded separately; earlier reviews are not mathematical premises.
All older theorem files remain unchanged.

## 1. The result and explicit constants

Let L count hidden layers. Define
\[
p_3=\frac{31}{8},\qquad p_4=\frac92,\qquad p_5=\frac{21}{4},
\qquad p_L=9-\frac{43}{2(L+1)}\quad(L\ge6),\qquad
E_L=2(L+1)p_L.                                           \tag{1}
\]
In particular E3=31, E4=45, E5=63, E6=83.

Here is an explicit numerical prefactor for every fixed L. Put
\[
b_L=2^{L-1}\sqrt{(L-1)!},\qquad
D_L=3\,2^{2L-2}\sqrt{2(L-1)!},\qquad
\eta_L={4\,4^{L-1}e^{-1}\over27\pi(4^{L-1}+1)^4}.        \tag{2}
\]
Retain the exact old constants
\[
C_0=1296000e^{1404},\quad C_z=1500C_0,\quad C_g=14400C_0,
\quad H=10^{30}(1+C_0+C_z+C_g+e^{1410})^4.                \tag{3}
\]
For L>=7 let
\[
\rho_L={1\over100(L+1)},\qquad B_L=4\sqrt{L(L-1)},
\]
\[
\mathcal C_L=e^{1/200}b_L\left[
 \sqrt L\,\operatorname{arsinh}(B_L)
 +{L\over2}\log(1+B_L^2)+{\rho_L\pi L\over2}\right]+2L,
\]
\[
H_L=\max\left\{H,10^{100}(8L)^L,{4\over\eta_L},
 \exp\big(\mathcal C_L+1000L^2\log(10L)\big)\right\}.
                                                               \tag{4}
\]
For 3<=L<=6 set H_L=H. These values also exceed the elementary
source and regression constants required below. Define
\[
                 c_L=H_L^{-100}D_L^{-2p_L}.              \tag{5}
\]
All constants in (1)--(5) depend only on L; c_L<1/4.

**Theorem.** For every fixed integer L>=3, every 0<delta<=1, every
fixed pair of deterministic inputs and binary labels satisfying
\[
\|x_i\|^2=d,\qquad |x_1^Tx_2/d|\le1-\delta,
\qquad y_i\in\{-1,1\},                                 \tag{6}
\]
every activation
\[
\phi_{a,e}(z)=az+e\arctan z,\qquad
\frac12\le a\le1,\qquad 0<e\le c_L\delta^{p_L}          \tag{7}
\]
has the full population/GF/raw-GD conclusions stated in Section 2.
For the requested convex mixture set a=1-theta and e=theta.

Moreover, the **same old** c_poly suffices in place of c_L for every
3<=L<=6. Here c_poly is exactly
\[
\min\{1/4,c_*,10^{-70}H^{-400}\},
\]
with c_* as defined in the immutable L3 power-ten proof, equation (1).
Only its displayed upper bound is used here. Consequently:

| Hidden depth | Sufficient bound with the unchanged old prefactor |
|---|---|
| 3 | 0<theta<=c_poly delta^(31/8) |
| 4 | 0<theta<=c_poly delta^(9/2) |
| 5 | 0<theta<=c_poly delta^(21/4) |
| 6 | 0<theta<=c_poly delta^(83/14) |

In particular **one choice theta<=c_poly delta^10 works at all four
depths 3,4,5,6**. This statement does not extend that same numerical
prefactor to all larger depths. For every fixed finite L, the common
exponent nine is sufficient with the explicit depth-dependent c_L,
because p_L<9 and delta^9<=delta^{p_L}. The stronger powers in (1)
are sufficient bounds, not a claim of optimality.

## 2. Exact model and complete conclusions

Write \(\rho=x_1^Tx_2/d\) and \(\Gamma_{ij}=x_i^Tx_j/d\).
At width n, initialize independently
\[
W^1_{ij}\sim N(0,1/d),\quad W^\ell_{ij}\sim N(0,1/n)
\ (2\le\ell\le L),\quad C_i\sim N(0,n^{-2}).
\]
With \(\langle u,v\rangle_n=u^Tv/n\), use
\[
z_i^1=W^1x_i,\quad h_i^\ell=\phi(z_i^\ell),\quad
z_i^\ell=W^\ell h_i^{\ell-1},\quad
f_i=\langle C,h_i^L\rangle_n,
\]
\[
b_i^L=C\phi'(z_i^L),\qquad
b_i^\ell=\phi'(z_i^\ell)(W^{\ell+1})^Tb_i^{\ell+1}.
\]
The loss is \(\mathcal L=\frac12\sum_i(f_i-y_i)^2\), and the raw
metric is
\[
\|d\Theta\|_{\rm raw}^2={d\over n}\|dW^1\|_F^2
 +\sum_{\ell=2}^L\|dW^\ell\|_F^2+\|dC\|_n^2.
\]
Thus, writing r_i=f_i-y_i, the physical flow is exactly
\[
\dot W^1=-d^{-1}\sum_i r_i b_i^1x_i^T,\quad
\dot W^\ell=-n^{-1}\sum_i r_i b_i^\ell(h_i^{\ell-1})^T,
\quad \dot C=-\sum_i r_i h_i^L.                          \tag{8}
\]
GD is simultaneous raw Euler with step n^-2. Interpolate raw parameters
linearly, recompute hidden fields, and use right hidden derivatives at
nodes and left derivatives at a terminal endpoint. The finite random
readout is retained throughout.

The conclusions are the following, with all width limits taken for
each fixed dataset, fixed L and fixed finite physical horizon T:

1. One autonomous global strong C1 population flow exists on L separate
   canonical neuron L2 spaces, with L-1 bounded initialized adjacent
   actions, their genuine adjoints and HS learned increments. It is
   unique against bounded-primal strong competitors on those spaces,
   including nonsymmetric ones, and restarts uniquely from reached states.
2. GF and the prescribed raw GD converge along the full width sequence
   in probability. Predictions, loss, all L+1 raw kernels and the stated
   generated action probes converge uniformly in time. Same-layer joint
   field/velocity laws converge in Wasserstein-2 uniformly in time and
   jointly at fixed finite collections of times, including second moments
   and integrated squared speeds. The two-sample (z,h) path law in each
   layer converges in Wasserstein-2 for the uniform path norm. There is
   no across-layer neuron pairing or across-width operator-norm claim.
3. Every layer and sample obeys, at every finite physical time,
   \[
   \inf_{\alpha,\beta}\mathbb E[
        \phi(z_i^\ell)-\alpha-\beta z_i^\ell]^2
                         \ge e^2\eta_L/4>0.             \tag{9}
   \]
   For the convex mixture through L6, the old constant
   \(\eta_*={4\cdot404e^{-1}\over27\pi405^4}\) from the
   L3 proof can replace eta_L. Every hidden raw block and every sample's
   layer preactivation and feature has nonzero initial acceleration;
   the projected total kernel changes to second order. Perpetual
   nonzero velocity is not asserted.
4. The loss satisfies
   \[
   \mathcal L(t)\le e^{-2a^{2L}\delta t}.                \tag{10}
   \]
   For the requested convex mixture and L<=6, this implies the old
   weaker bound exp(-delta t/32).

The kernel terms are
\[
K^1_{ij}=\Gamma_{ij}\langle b_i^1,b_j^1\rangle_n,\qquad
K^\ell_{ij}=\langle b_i^\ell,b_j^\ell\rangle_n
              \langle h_i^{\ell-1},h_j^{\ell-1}\rangle_n,
\quad 2\le\ell\le L,
\quad K^{L+1}_{ij}=\langle h_i^L,h_j^L\rangle_n.          \tag{11}
\]
No limit is uniform over the infinite physical time axis or over
growing depth; the population trajectory itself is global.

## 3. Affine geometry, constants, and the intrinsic scale

Odd label folding preserves the exact finite raw loss. Reflection
exchanging the folded inputs and deterministic population contractions
give f_i=y_i g for the constructed limit, before uniqueness is invoked.
Feature time s uses the fixed-control field grad g, where
g=(1/2)sum_i y_i f_i. Let
\[
r=\sqrt{(1+y_1y_2\rho)/2},\quad \lambda=a^Lr,
\quad M=\left({3b_L\over2\lambda}\right)^{1/(L+1)}>1.    \tag{12}
\]
After dividing the first active projection by r and changing auxiliary
time to t=lambda s, the affine objective and exact raw equations are
\[
F=\langle D,A_L\cdots A_2p\rangle,
\quad p'=d_1,\quad A_j'=d_j\otimes x_{j-1},\quad D'=x_L,
\]
where x_1=p, x_j=A_jx_{j-1}, d_L=D and d_j=A_{j+1}^*d_{j+1}.

AFFINE_CERTIFICATE.md establishes canonical initialized action norm
at most two, using the stated Gaussian norm theorem with its hypotheses
checked. Adjacent Gram balances give
\[
\|p\|^2=1+c^2,\quad \|A_j\|^2\le c^2+4(L-j+1),
\quad(c^2)'=2F,\qquad c=\|D\|.
\]
The new all-radius bound follows by Cauchy in every gradient block:
\[
F'\ge F^2\left[{1\over c^2}+{1\over1+c^2}
                       +\sum_{k=1}^{L-1}{1\over4k+c^2}\right].
\]
Using F^2/c^2->1 at time zero and integrating with respect to c^2 yields
\[
F^2\ge c^2(1+c^2)\prod_{k=1}^{L-1}\left(1+{c^2\over4k}\right),
\quad F\ge c^{L+1}/b_L.                                \tag{13}
\]
Together with radial convexity c'>=1, this proves strong continuation
through the first affine hit g=3/2, with duration S and
\[
S\le2M^{L+1},\qquad M^{L+1}\le D_L\delta^{-1/2}.        \tag{14}
\]

The companion bounds the raw Hilbert Hessian using the actual separate
block norm bounds. For 3<=L<=6, on a radius-1/100 raw tube,
\[
\int\|\nabla^2F\|dt\le5100+L\log M.
\]
It checks all numerical forcing, probe and beta-family factors below
10^80 exp(5200)<H. At general fixed L the corresponding integral is
at most mathcal C_L+L log M on a tube of radius rho_L. Section 7 of
the companion gives explicit forcing and beta gaps, with every primitive
prefactor bounded by (4). In particular, uniformly in the backward cap,
\[
\|\Theta_e-\Theta_0\|_{\rm raw}\le H_L eM^{2L+2},\qquad
\|z_{e,i}^\ell-z_{0,i}^\ell\|_2\le H_L eM^{2L+\ell+1},
\quad |g_e(S)-3/2|\le H_L eM^{2L+1}.                   \tag{15}
\]
Original forward fields have bounded L2 norms H_L; incoming backward
fields have L2 norms at most H_L M^{L+1-ell}. These estimates are
proved before the coefficient-response argument.

The exact answer-probe normalization, including current direct terms
and both orientations, gives the following original-time exponents.
Set d0=L+1, t0=2L-1, and u_i=(2i-L-4)_+. Every local resolvent row
has bound H_L M^t0; local strict-transfer density has bound H_L M^u_i;
the local backward row at population i<L has exponent
b_i=4L-1-2i, and the top readout integration row has b_L=d0 in
this local notation. Adjacent beta gaps are at least
H_L^-1 M^{-(L-1)}. Every active strict transfer V_i, i<L, has lower
bound M^{-2(L+1)}h_j at source slot j. These are the precise premises
discharged for SOURCE_RESPONSE.md, with H_L substituted for that
companion's generic prefactor H.

## 4. Source tails recovered from the primal bounds

For every fixed finite depth the exact source program has 2(L-1)
coefficient families: forward strict arrays A2,...,AL and backward
causal arrays BL,...,B2, in that chronological order. Covariances use
full second moments; each coefficient is its actual formal source
derivative plus its learned moment. All current transpose returns are
retained. SOURCE_RESPONSE.md states the equations, including the
recursive current returns, on L distinct neuron spaces.

At the same deterministic coefficient arrays, a local population obeys
\[
Z=\xi+K\delta,\quad q=\zeta+B\phi(Z),\qquad
R=(I-a^2KB)^{-1},\ L_0=(I-a^2BK)^{-1},\ U=RK.
\]
Put h=arctan Z and d_gate=(1+Z^2)^{-1}tau_R(q). The combinations
\[
Z_G=R\xi+aU\zeta,\qquad q_G=L_0\zeta+aBR\xi
\]
are centered Gaussian, although Z and q need not be. The exact identities
\[
Z-Z_G=eU[d_{gate}+aBh],\qquad
q-q_G=e[aBUd_{gate}+L_0Bh]                              \tag{16}
\]
and the already proved primal L2 bounds show that Z_G has bounded
variance and q_G has L2 norm O(M^{L+1-i}), provided
eH_L^20 M^{5L-2}<=1. Gaussian moments then give the corresponding
sqrt(p) bounds. Applying (16) again in Lp and absorbing its small
q term proves
\[
\|Z_i\|_p\le H_L^{12}\sqrt p,\qquad
\|q_i\|_p\le H_L^{12}M^{L+1-i}\sqrt p.                 \tag{17}
\]
This argument needs no independence between the Gaussian and nonlinear
remainders and is uniform in cap and sufficiently fine fixed mesh.

Formal differentiation freezes all deterministic arrays, covariances
and named slots. The exact cancellation is
\[
J-J_0=U[\Delta V I_\zeta+P J],\qquad
\partial\delta-\partial\delta_0=L_0[\Delta V I_\zeta+P J],
\]
\[
P=N+a\Delta V B+aB\Delta G+\Delta V B\Delta G.           \tag{18}
\]
Here N contains e times an incoming field. Both other B-gate terms
are retained, including full random sample-sector mixing. In particular
the improved q moments cannot replace their deterministic B-row power.
The strict derivative envelope and weighted marginal moment bounds
give complete backward defects
\[
\|J_j\|_{row}\le H_L^{40}eM^{Q_j},\qquad
Q_j=8L-3-2j\ (2\le j<L),\quad Q_L=5L-1.                \tag{19}
\]
The independently bounded learned moments are included. The companion
also proves each forward strict-density defect, with its actual h_j.

## 5. Controlling a chain of response terms without multiplying all bounds

Fix the inner beta reference. Positive affine coefficient recursion
gives A_{i+1}>=beta^2 V_i, where V_i=a^2R_iK_i. Hence
\[
R_{i+1}V_i\le(\beta^2a^2)^{-1}V_{i+1},\qquad
V_iL_{i+1}\le(\beta^2a^2)^{-1}V_{i+1}.                  \tag{20}
\]
Also R_i=I+V_iB_{i+1}. Expanding the rightmost factor of a product
and applying (20) repeatedly bounds a whole product by an identity
plus a sum of single strict transfers times backward rows. Thus the
row power for R_j...R_i and its reverse orientation is at most
\[
\min\{(j-i+1)t0,\ u_j+d0+b_i\}.                       \tag{21}
\]
The numerical chain factors, at most (8L)^L, are included in H_L.

For arbitrary nonnegative complete-row defects J_j, keep the forward
arrays at the inner reference and define backward excesses recursively:
\[
\Delta_L=J_L,\qquad
\Delta_i=J_i+a^2L_i\Delta_{i+1}R_i^*.                   \tag{22}
\]
This is an exact backward supersolution. Scale all J's by alpha in
[0,1] and impose simultaneously V_i^*<=2V_i and
\[
\|\Delta_i\|_{row}\le H_L^{-20}M^k,
\qquad k=\min(L-2,4).                                 \tag{23}
\]
Since A_{i+1}>=beta^2 V_i^*/2, (20)--(21) also hold for starred
products with finite factors at most 8 per step. Identities R*=I+V*B*
and L*=I+B*V* preserve the local row power t0 because
max_{i<L}(u_i+d0)+k<=t0. No small inverse assumption is used: all
strict-causal Volterra inverses at fixed mesh are finite polynomials.

The contribution of J_j to the bottom excess has exponent
\[
Q_j+2\min\{(j-2)t0,\ u_{j-1}+5L-4\}.                 \tag{24}
\]
For every forward loop V_i Delta_{i+1} V_i, both strict sides
compress by (20), preserving source-step densities. Its relative
bound, including the active lower density and beta slack, requires
only eH_L^60 M^{12L-5}<=1. Direct forward defects require less.
These inequalities strictly improve V_i^*<=2V_i and (23), so the
auxiliary homotopy closes.

For the actual coefficient homotopy, the outer box explicitly bounds
the positive transfer built from absolute active arrays by 2V_beta,out.
This is essential for the larger row radius (23). On this box the
source estimates apply. Chronological comparison with the inner
supersolution puts all actual coefficients, and their positive
transfers, strictly inside the outer box. The inactive sector has a
separate small backward box and explicit increasing forward margins;
SOURCE_RESPONSE.md constructs its finite triangular supersolution
without dividing by the inactive variance. First exit is impossible.

The exact arithmetic is:

| L | Maximum backward-excess power from (24) | k | Forward restriction | Sufficient E_L |
|---|---:|---:|---:|---:|
| 3 | 24 | 1 | 31 | 31 |
| 4 | 47 | 2 | 43 | 45 |
| 5 | 66 | 3 | 55 | 63 |
| 6 | 87 | 4 | 67 | 83 |
| L>=6 | 18L-21 | 4 | 12L-5 | 18L-25 |

For general L>=6 the j=5 term attains 18L-21; the companion bounds
every other term explicitly. Every value, derivative, learned-moment,
inactive-sector, beta-slack and supersolution restriction is implied by
\[
                        eH_L^{100}M^{E_L}\le1.         \tag{25}
\]
This proves the complete cap/mesh-uniform source construction.

## 6. Closing the constants and the full population theorem

Equations (5), (7) and (14) give directly
\[
eH_L^{100}M^{E_L}
\le c_LH_L^{100}D_L^{E_L/(L+1)}=1.                     \tag{26}
\]
The unused powers in the preceding estimates make all required
inequalities strict. In particular (15) is below half the raw tube
radius, its endpoint discrepancy is below 1/4, and its preactivation
discrepancy is below sqrt(eta_L)/2. To check the last claim, (25)
gives H_L e M^{3L+1}<=H_L^-99, and H_L>=4/eta_L. The explicit
H also satisfies this requirement for L<=6. The old eta_* may be
used for convex gains through L6 by the stronger variance bound below.

For 3<=L<=6, D_L<=D_6<48000 and E_L/(L+1)<=83/7<12.
Since 48000^12<H, the old coefficient satisfies
\[
c_{poly}H^{100}D_L^{E_L/(L+1)}
 \le10^{-70}H^{-299}<1.                                \tag{27}
\]
This proves the unchanged-prefactor assertions, with the smaller
exponents in the table, as well as the original power ten.

POPULATION_AND_MOMENTS.md supplies the full fixed-L bridge, using the
actual generic Gaussian-conditioning theorem from the earlier proof.
It applies to the finite list of L-1 independent initial matrices,
each used in both orientations, and handles singular source laws by
finite-query regularization. Finite transpose identities on generated
spaces give genuine adjoints. Fixed-cap bounded derivatives and the
strict affine tube yield capped strong solutions and Euler limits.

The asymmetric backward comparison multiplies forward-state errors
by one factor (1+eR), independently of the number of backward steps.
With (17), its cap error is bounded by
C exp(C(1+eR)S-cR^2), tending to zero for each fixed L. States and
directions converge strongly to an autonomous uncut C1 feature path
through g(S)>5/4. The same estimate, retaining both physical residuals
and using tails only from the reference, proves uniqueness against
nonsymmetric bounded-primal competitors and restart from reached states.

At the first hit s_* of g=1, bounded g' makes
\(\int_0^s[2(1-g(u))]^{-1}du\) diverge. Its inverse gives the global
physical flow. Radial convexity and the initialized inequality
\(q_L\pm\chi_L\ge a^{2L}(1\pm\rho)\), where
\(q_L=\mathbb E[(h_1^L)^2]\) and
\(\chi_L=\mathbb E[h_1^Lh_2^L]\) at initialization, give (10).

Width is taken at fixed cap and finite auxiliary transcript; deterministic
stopped Euler comparison removes the mesh, then reference tails remove
the cap. The raw-GD consistency error is C_{L,R,T}n^-2. The finite
readout has RMS O_P(n^-1) and is retained until its zero population
limit. Appending L-1 clipped velocity queries in layer order and
removing their clips in the specified order gives the fixed-cap velocity
laws. The deterministic comparison uses a single reference-velocity
truncation factor; compactness of the uncut L2 time image removes it.
L2 products give (11), second moments and integrated speeds; fixed-grid
joint W2 convergence and the path interpolation inequality give the
same-layer path laws. No growing-transcript theorem is used.

Finally, positive Wick expansion of finite affine Euler programs and
inactive-field freezing give Gaussian affine marginal variance at least
a^{2(ell-1)}. The third-Hermite bound is eta_L, and the square root of
the arctangent regression residual is 1-Lipschitz in L2 coupling.
Equation (15) therefore gives (9). For a>=3/4 and ell<=6, the variance
is greater than 1/404, retaining the old eta_*.

The top initialization backward full second-moment Gram is positive
definite because phi' is positive and nonconstant. Each of the L-1
actual reused transpose formulas has a Gaussian term with the full
preceding backward second moment, plus its complete derivative response.
Conditional covariance propagates positivity down every layer. Its
positive contraction with the preceding forward Gram proves nonzero
acceleration of each hidden block. Adjunction and exchange then prove
both sample accelerations in every layer. With V the aggregate hidden
feature-time acceleration,
\[
\kappa(s)=\kappa(0)+2s^2\|V\|^2+o(s^2),\qquad
\kappa(t)=\kappa(0)+8t^2\|V\|^2+o(t^2),\quad\|V\|>0.
\]
This completes all parts of the theorem.

## 7. Depth dependence and limits of the result

For L>=6, p_L increases to nine. Thus (5) proves an explicit
depth-dependent prefactor with a depth-independent sufficient exponent
nine. The prefactor is conservative: its logarithm satisfies
\[
\log(c_L^{-1})=O\!\left(2^L\sqrt{(L-1)!}\,L\log L
                              +L^2\log L\right).
\]
This is an upper bound on the size of the sufficient restriction, not
a necessary deterioration. It proves neither optimality of p_L nor
impossibility of much better depth dependence.

No common positive prefactor for all finite depths is established here.
The previously proved convex initialization asymptotic q_L~1/(2theta L)
rules out the stated positive depth-uniform loss-rate and regression
margin bounds, but does not rule out one common activation yielding the
qualitative theorem at every finite L. That question remains open.
