# Three samples at depth two: proved statements and the unresolved full theorem

2026-09-08. L counts hidden layers, as in the preceding two-input theorem.
The exact model and requested scope are in CONTRACT.md. The activation is
phi_theta(z)=(1-theta)z+theta atan(z), with 0<theta<=1/2. The inputs have
unit RMS norm, arbitrary binary labels and |rho_ij|<=1-delta.

**The requested complete global population/GF/GD theorem with a polynomial
threshold theta<=c delta^p has not been established in this analysis.**
The old theta-independent loss-rate conclusion is false for the admitted
three-input configurations. Allowing a theta-dependent rate leaves a
substantive open problem; none of the results below disproves that version.
In particular no c,p pair is being claimed for the full theorem.

The mathematical companions contain complete derivations of the stated
partial results. REVIEW_STATUS.md records independent checks of these
claims and their scope; a passing review is not a proof of the open target.

## 1. Positive initialization with an explicit sharp scale

Let Q_2(0) denote the 3-by-3 Gram matrix of the initialized second hidden
features. Put a=1-theta and, for standard Gaussian G, define

\[
b_3=\frac{1-2\mathbb E(1+G^2)^{-1}}{\sqrt6}\ne0.
\]

For every admissible triple, including singular input Grams,

\[
Q_2(0)\succeq
\frac{a^2b_3^2}{3}\theta^2\delta^2(2-\delta)^2 I_3
\succeq
\frac{81e^{-1/4}}{230400\pi}\theta^2\delta^2 I_3.       \tag{1}
\]

No smaller upper threshold on theta is needed for (1). For every fixed
input dimension at least two, and 0<delta<=1/4, a matching family proves

\[
\inf_{\text{admissible triples}}\lambda_{\min}(Q_2(0))
                      =\Theta(\theta^2\delta^2),       \tag{2}
\]

with absolute constants for 0<theta<=1/2. This is an initialization
statement. It does not assert a lower bound on the trained Gram.

The proof in GEOMETRY_AND_NECESSARY_SCALES.md, Sections 1-2, constructs
dual tensors to show Gamma^{circ3} >= delta^2(2-delta)^2 I/3. The cubic
Gaussian component of arctangent then bounds the first feature Gram.
The first Gaussian component of the second activation preserves at least
the factor a^2. A symmetric, nearly collinear triple and a second-difference
estimate give the matching upper bound through the second hidden layer.

In particular, positive theta removes any representation obstruction:
the initialized hidden features already admit a readout that fits every
label vector. For example, writing H v=sum_i v_i h_i^2(0), the readout
C_*=H Q_2(0)^{-1}y satisfies H^*C_*=y. This is an expressivity witness,
not a claim about the jointly trained trajectory.

## 2. Why the affine argument and unchanged loss rate fail

Consider the equilateral planar triple

\[
u_1+u_2+u_3=0,\qquad u_i\cdot u_j=-1/2\ (i\ne j),
\qquad y=(1,1,1).                                     \tag{3}
\]

It obeys the requested closed separation condition whenever delta<=1/2.
At theta=0, every prediction is linear in the input, so its three-sample
sum is zero. At population initialization C=0, both the readout gradient
and every hidden gradient vanish. The affine population trajectory is
stationary at loss 3/2. No affine fitting clock exists for this example.

At theta>0 the initialization signal is positive by (1). Define
H_0=(1/3)sum_i h_i^2(0). Its squared norm is of order theta^2 at fixed
separation. Since only the readout kernel is nonzero at initialization,

\[
-\dot{\mathcal L}(0)=9\|H_0\|^2.
\]

Consequently, any bound with its exact initial prefactor,
L(t)<=L(0)exp(-kappa t), must satisfy

\[
\kappa\le 6\|H_0\|^2
\le\frac{3\pi^2}{2}\theta^2(1+2a)^2.                 \tag{4}
\]

Thus a positive rate depending only on delta cannot hold uniformly for
every 0<theta<=c delta^p. This argument does not preclude a rate depending
on theta, or a single activation choice with its own quantitative rate.

There is also a necessary fitting-time bound that does not assume an
exponential estimate with the exact initial prefactor. At every parameter
state in (3), put T_l=sum_i atan(z_i^l). Then

\[
\sum_i h_i^1=\theta T_1,\qquad
\sum_i h_i^2=\theta(aAT_1+T_2),\qquad \|T_l\|_2\le3\pi/2.
\]

If L<=3/8, Cauchy--Schwarz gives sum_i f_i>=3/2, and therefore

\[
\|C\|_2(1+a\|A\|)\ge\frac1{\pi\theta}.
\]

For raw distance R from the canonical initialized state, the joint raw
norm gives ||C||^2+||A-A_0||_{HS}^2<=R^2 and ||A_0||<=2. Hence

\[
3R+\tfrac12R^2\ge\frac1{\pi\theta},\qquad
R\ge\sqrt{9+\frac2{\pi\theta}}-3.                    \tag{5}
\]

For any true strong GF that reaches this loss at time T, its energy
identity and path-length inequality give R^2<=3T/2. It follows that

\[
T\ge\frac23\left(\sqrt{9+\frac2{\pi\theta}}-3\right)^2,
\qquad
\liminf_{\theta\downarrow0}\theta T\ge\frac4{3\pi}.   \tag{6}
\]

Here an infinite fitting time also satisfies the lower bound. Equations
(5)-(6) require no assertion that fitting or a global population solution
actually occurs. They exclude a theta-independent convergence estimate
with any fixed finite prefactor that would imply bounded fitting time.
They also show why reducing theta cannot preserve a uniformly bounded
neighborhood of the stationary affine reference through successful fitting.

## 3. What two hidden layers simplify, and what remains

SOURCE_AND_CONTINUATION.md derives the exact L=2 source system from the
same finite Gaussian-conditioning construction used in the old theorem.
There is only one initialized adjacent matrix, but two coupled response
families remain. In abbreviated causal notation they enter as

\[
Z^1=Z^1_0+\mathcal P b^1,\quad
q^1=\zeta+\mathsf B\phi(Z^1),\quad
Z^2=\xi+\mathsf A b^2,\quad
C=\mathcal H\phi(Z^2),
\]

where b^1=phi'(Z^1)q^1 and b^2=phi'(Z^2)C in the uncut equations.
The forward coefficient mathsf A is an expected bottom source derivative
plus a learned moment; mathsf B is an expected top source derivative plus
a learned moment. The latter includes the actual current return
diag E[phi''(Z^2)C]. All sample and temporal covariance entries are kept.

On a bounded raw path and bounded response-coefficient prefix, the
companion proves explicit subGaussian moment and derivative estimates,
without an affine comparison and without a small-theta hypothesis.
However, its produced response bounds do not close those two coefficient
prefix bounds on arbitrary prescribed horizons. The missing estimate is
a noncircular bound on reachable past source derivatives, or another
tail/regularity estimate strong enough to remove the incoming-field caps.

The true finite-width GF is global by its exact energy identity and
finite-dimensional continuation. For an already existing true strong
population GF, energy similarly supplies raw bounds and strong endpoints.
These facts alone do not construct or continue a strong infinite-dimensional
solution: a bounded L2 ball gives no uniform incoming-field tails, and the
uncut multiplier C phi''(Z) is not bounded on such balls. Ordinary backward
caps make a locally Lipschitz field, but they are not the true loss gradient
and cannot simply inherit its energy identity.

Thus source continuation is an actual missing implication, not a
technicality supplied by reducing the hidden depth from three to two.
Even closing it would leave the generic three-residual fitting and trained
nonaffinity conclusions to be justified.

## 4. A nonlinear reference that does retain the missing signal

NONLINEAR_REFERENCE.md investigates an alternative rather than merely
rejecting the affine reference. Freeze the initialized nonlinear first
features, retain their positive Gram Q, make only the top activation
affine, and train the adjacent action and readout. In normalized coordinates
B=AHQ^{-1/2}, this different reference model has the exact invariant

\[
BB^*-C\otimes C=P_E.
\]

It fits globally and obeys a genuine output-Gram lower bound a^2Q. Its
factor sizes are O(theta^{-1/2}delta^{-1/2}), consistent with (5).

This reference does not prove the requested jointly trained theorem.
The companion gives explicit equilateral reference states with a fixed
mean prediction j in (0,1), where the omitted true first-layer physical
force has a nonzero limit as theta decreases to zero. It includes the
actual top nonlinearity when computing this force. A comparison requiring
a uniformly vanishing field defect therefore does not apply. The result
does not exclude a different comparison or a proof treating bottom-layer
dynamics at leading order.

For the symmetric equilateral true model there is also a conditional
nonlinear scalar-clock lemma: if its strong ascent trajectory continues
through the first hit of prediction one, radial monotonicity yields

\[
\mathcal L(t)\le\tfrac32\exp\left[
-\tfrac23 a^2b_3^2\theta^2\delta^2(2-\delta)^2t\right].
\]

GEOMETRY_AND_NECESSARY_SCALES.md, Section 5, proves this implication and
the physical clock inversion. The continuation premise is explicit;
generic triples need not have the symmetry needed for a scalar clock.

## 5. Final scope

The positive complete result established here is the sharp initialized
top-Gram estimate (1)-(2), supplemented by the necessary state and time
scales, exact source equations and conditional bounds, and the separately
identified reference-model theorem. The full joint global population/GF/GD
threshold theta<=c delta^p remains unproved for three inputs at L=2 under
only the stated pairwise separation. No counterexample to that qualitative
positive-theta theorem has been found. The proofs do rule out carrying
over the earlier theta-independent quantitative loss rate.
