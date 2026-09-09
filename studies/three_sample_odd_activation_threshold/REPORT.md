# What can currently be proved about a three-input activation threshold

2026-09-08. The target is fixed in [CONTRACT.md](CONTRACT.md).
The full three-input, three-hidden-layer theorem remains open. This
investigation does not establish any positive sufficient theta_delta,
whether polynomial, exponentially small, or constant. It also does not
establish that such a coefficient fails to exist. The unresolved step
precedes optimization of an asymptotic exponent.

The current two-input delta-squared theorem remains unchanged. The
older complete three-input theorem uses an offset and large gain and
does not cover the present activation. A separate two-hidden-layer
three-input contract is not a theorem for the original depth.

## 1. The two different asymptotic quantities

Write
\[
 \phi_\theta(z)=(1-\theta)z+\theta\arctan z,
 \qquad 0<\theta\le1/2,
 \qquad \Gamma_{ij}=x_i^Tx_j/d.
\]
For the first initialized feature Gram Q_1(0), the existing geometry
proof gives
\[
 Q_1(0)\succeq
 \frac{b_3^2}{3}\theta^2\delta^2(2-\delta)^2 I_3,
 \quad b_3=\frac{1-2\mathbb E(1+G^2)^{-1}}{\sqrt6}\ne0.
 \tag{1}
\]
It also gives Q_3(0) >= (1-theta)^4 Q_1(0). For every fixed dimension
d>=2, uniformly in 0<theta<=1/2 and 0<delta<=1/4,
\[
 \inf_{\substack{\|x_i\|^2=d\\|\Gamma_{ij}|\le1-\delta\ (i\ne j)}}
 \lambda_{\min}(Q_1(0))\asymp\theta^2\delta^2.       \tag{2}
\]
The constants in the comparison are absolute. The lower bound comes
from cubic tensor lifting and the third Gaussian Hermite coefficient;
the matching upper bound comes from a planar three-point second
difference. These statements are proved in
[the geometry source](../odd_mixture_separation_quantitative/THREE_INPUT_GEOMETRY.md)
and [the corrected three-input analysis](../odd_activation_lower_powers_three_inputs/THREE_INPUT_ANALYSIS.md).

Thus every positive theta in this range gives positive initialization
Gram; there is no small-theta upper restriction for that assertion.
Choosing theta asymptotic to delta^p makes the worst initial eigenvalue
asymptotic to delta^(2p+2). Equation (2) is sharp for initialization.
It is not a sufficient theta scaling law for trained dynamics.

The requested full result instead needs one theta_delta>0 fixed before
the dataset and physical horizon, and the entire strong-flow and
finite-algorithm limit conclusion. An interval assertion for every
0<theta<=theta_delta is stronger than a single successful witness.
Neither has been established here for the complete admissible
three-input class in the small-delta regime. A fixed order-one witness
has not been proved either.

## 2. Fixed separation does not bound the input spectral gap

The equilateral planar triple has all off-diagonal correlations -1/2
and an input-Gram null vector (1,1,1). It is admissible for every
delta<=1/2. For equal labels, the affine population initialized with
C=0 is stationary: the feature sum is zero, hence the readout
derivative is zero; all hidden derivatives contain C and vanish.
This defeats the affine learning clock used by the two-input proof.
It is not a positive-theta counterexample.

Even excluding exact singularity would not provide a delta-only
spectral lower bound. For eta>0 consider in dimension three
\[
 u_1=(1,0,0),\quad u_2=(-1/2,\sqrt3/2,0),\quad
 u_3=\frac{(-1/2,-\sqrt3/2,\eta)}{\sqrt{1+\eta^2}}.
\]
Their absolute pairwise correlations are at most 1/2, and the vectors
are linearly independent. With
v=(1,1,sqrt(1+eta^2)), their weighted sum is (0,0,eta), so
\[
 0<\lambda_{\min}(\Gamma)
 \le\frac{v^T\Gamma v}{\|v\|^2}
 =\frac{\eta^2}{3+\eta^2}\longrightarrow0.             \tag{3}
\]
Consequently an affine-reference estimate depending on an additional
input spectral gap cannot become uniform merely from the user's
pairwise condition. This applies even at a fixed delta such as 1/4.

## 3. New small-separation fitting obstruction

Here and below, a fitting statement is conditional on reaching the
specified loss. The bare global-flow/population-limit statement does
not itself assert eventual zero training loss. These bounds obstruct
fitting-based proof methods; they do not disprove global dynamics.

For 0<delta<=1/4 set c=1-delta and s=sqrt(1-c^2), and take
\[
 u_+=(c,s),\quad u_0=(1,0),\quad u_-=(c,-s),
 \qquad y=(1,-1,1).
\]
The pairwise condition holds, and v=(1,-2c,1) is a Gram-null vector.
Let R be the canonical raw Hilbert distance of a parameter state from
initialization. The first initialized action has norm one, the other
two have norms at most ten, and the population readout is zero.
Then loss at most 3/8 implies
\[
 R>(10\theta\sqrt\delta)^{-1/4}-11.                    \tag{4}
\]

Here is the estimate behind (4). Put N=||sqrt(d)w||_op,
A_*=||A||, B_*=||B||, C_*=||C||_2, and
T_l=atan(z_+^l)-2c atan(z_0^l)+atan(z_-^l). Since both phi_theta
and arctangent are 1-Lipschitz,
\[
 \|T_l\|_2\le2\sqrt{2\delta}P_l+\pi\delta,
 \qquad (P_1,P_2,P_3)=(N,A_*N,B_*A_*N).
\]
The exact Gram-null identity gives, with a=1-theta,
\[
 \sum_i v_i h_i^3
 =\theta(a^2BAT_1+aBT_2+T_3).
\]
Taking norms yields
\[
 |v^Tf|\le\theta C_*\bigl[
 6\sqrt{2\delta}B_*A_*N+
 \pi\delta(1+B_*+B_*A_*)\bigr]
 <10\theta\sqrt\delta(11+R)^4.                         \tag{5}
\]
The last step uses N<=1+R, A_*,B_*<=10+R, C_*<=R, and
6sqrt(2)+3pi/11<10. Low loss gives ||r||_2<=sqrt(3)/2 and
\[
 v^Tf\ge2+2c-\|v\|_2\|r\|_2
 \ge7/2-\sqrt{18}/2>1.
\]
This and (5) prove (4). A true strong GF obeying the energy identity
and reaching this loss at time T must consequently satisfy
\[
 T\ge\frac23[(10\theta\sqrt\delta)^{-1/4}-11]_+^2.     \tag{6}
\]
This follows from R<=sqrt(T(L(0)-L(T)))<=sqrt(3T/2).
The [geometry route](routes/GEOMETRY.md) gives the detailed proof,
the strictly separated variant, and its assumptions.

The existing equilateral example separately requires
R>=(pi theta)^(-1/3)-11. Therefore a fitting-radius estimate uniform
over datasets must accommodate both theta^(-1/3) and
(theta sqrt(delta))^(-1/4), up to constants and additive offsets.
These lower bounds are not asserted sharp and do not forbid a choice
theta=delta^p: the target permits delta-dependent trajectory constants.

## 4. Why the investigated routes do not yet prove a cutoff

**Nonlinear reference.** The initial feature Gram is positive, but its
time-derivative identity supplies no positive-semidefinite sign, and
no architecture-specific monotonicity or uniform coercivity estimate
has been established along the generic three-residual flow. In the
symmetric equilateral case the
existing scalar lemma gives a clock certificate proportional to
theta^(-2), conditional on strong construction. Substitution into the
available affine-response restriction produces the circular sufficient
condition theta exp(c/theta^2)<=C, which fails as theta goes to zero.
This calculation invalidates that certificate, not the desired theorem.

There is also a new upper bound on the complete four-block raw tangent
kernel K. At any raw state of distance R from initialization, every
v in ker(Gamma) satisfies
\[
 v^TKv\le256\theta^2\|v\|_1^2(11+R)^6.                \tag{7}
\]
To see the amplitude factor, differentiate the exact identity
v^Tf=theta<C,a^2BA T_1+aB T_2+T_3>. Bounded gate derivatives and
the raw action norms give a derivative norm of the expression after
theta at most 16||v||_1(11+R)^3. Squaring gives (7), since K is
the Gram of the four raw predictor gradients. The
[nonlinear-reference route](routes/NONLINEAR_REFERENCE.md) derives
each block estimate and states the scalar differentiability used.
Thus including hidden kernel blocks cannot supply a theta-independent
null-direction coercivity margin on a theta-independent bounded raw
region. Equation (7) is an upper bound and does not rule out positive
theta-dependent coercivity.

**Direct energy construction.** An existing true GF has a bounded raw
path on every finite interval by its energy identity. This does not
construct or continue a strong solution for the uncut infinite-dimensional
field. The existing incoming-field clips are locally Lipschitz but
are not gradients of the loss. Energy-preserving clipping of whole
gradient blocks need not regularize unbounded multipliers. Galerkin
energy gives weak compactness, without the strong convergence and
nonlinear-product control needed here.

**Gaussian regression.** Integration by parts can bound the combined
initialized response in L2 without an inverse covariance. The
separately named derivative coefficients need not have bounded rows,
and the associated transport into actual query fields is only an L2
isometry. It gives no uniform higher-moment or tail bound. Nearly
singular temporal query covariances are not controlled by spatial
pairwise separation. This leaves the canonical source-tail requirement
unresolved, rather than proving the regression approach impossible.
The [direct-source route](routes/DIRECT_SOURCE.md) proves the regression
bound, treats singular covariance, and gives an explicit counterexample
to inferring uniform higher moments from this L2 transport alone.

**Transport of the initialization estimate.** A bounded raw-L2
neighborhood does not preserve the O(delta) first-layer Gram-null
arctangent remainder used in the sharp initialization calculation.
The geometry route constructs bounded raw-L2 changes concentrating on
an event of probability delta, for which the remainder is
Omega(sqrt(delta)). This is a raw-ball counterexample, not a reachable
GF counterexample. A stronger moment or reachable-state estimate is
needed to use the initialization Taylor scale during training.

**Order-one nonlinearity.** The available pure-arctangent theorem is
for one sample and two hidden layers, with a different readout
initialization and observable scope. It cannot supply a constant
theta witness for this problem. Bounded arctangent output controls
the readout on compact residual clocks, but does not by itself control
the adapted initialized transpose in the middle of three hidden layers.

## 5. Research conclusion

The strongest sharp asymptotic statement currently established is
the initialization law (2). There is no proved sufficient amplitude
asymptotic for the complete three-input theorem. In particular neither
a polynomial cutoff nor an exponentially small cutoff may presently
be advertised as sufficient.

The next substantive obligation is a reachable source-tail/strong
continuation mechanism for the actual three-sample depth-three flow,
or a nonlinear reference supplying that mechanism. It must remain
valid on arbitrary finite physical intervals for one fixed positive
theta_delta. After it is proved, the original uniqueness, cap removal,
trained nonaffinity and full GF/raw-GD observable bridges still need
their hypotheses checked.

[EVIDENCE_LEDGER.md](EVIDENCE_LEDGER.md) records the route outcomes and
[REVIEW_STATUS.md](REVIEW_STATUS.md) records checks of the partial
mathematical statements. No full-theorem proof certificate is issued.
