# Coordinator reconstruction: actual dense lower bounds and sphere upper bound

2026-10-04. Checker: coordinator. This is a collaborative internal check,
not an independent promotion review. The coordinator suggested the explicit
endpoint constants after independently reconstructing that part of the proof.
No code/training experiment was used. All checks below are mathematical.

## Frozen inputs and read coverage

* INTEGRATED_DENSE_LOWER_ROUTE.md, complete equations (1)--(40b), final
  scope/provenance; SHA-256
  `8069187d94d4b90acfaa1406b1ccbd6961a24c2fc6d21de8d9a3a651c1e16200`.
* INTEGRATED_DENSE_VARIABILITY_ROUTE.md, complete report; SHA-256
  `617c06e64b95a2910b4b07dfde1d5a44f1aa729a57150a1363a883a823084f24`.
* User-authorized prior study GENERAL_SELF_AVERAGING.md, complete report,
  including its good-pair derivation, scalar extension, Gaussian
  concentration proof, and physical-time modulus.
* DEPTH_EXTENSION_RESULT.md, complete scoped theorem and proof-input
  inventory, to check the inherited canonical model and broad activation
  hypotheses. The earlier full finite-carrier proof is an inherited checked
  dependency, not newly reproved by this reconstruction.
* Current docs/index.qmd and docs/notation.qmd, current root instructions,
  required canonical/neural notation, rigorous-proof and research skills.

## 1. Actual nonlinear finite-time lower bound

The network has two n-wide tanh layers, independent canonical Gaussian
initialization, zero readout and mobilities (n,1,n). Training inputs are
sqrt(d)e_a, a≤m, and the query is sqrt(d)e_{m+1}, with d≥m+1.
All labels are deterministic and 0<Y=||y||/sqrt(m). Full-sphere upper
theorems keep general geometry; orthogonality is used only for this lower
construction. The coordinate count d can grow without changing the proof,
since unqueried and untrained input columns never enter it.

The exact forward/backward equations and every factor 2,m,n in (3) were
rederived from the stated mean squared loss and mobilities. Monotonic
loss gives ||r||/sqrt(m)≤Y without a fitting assumption. On the stopped
event Wop≤11 and ||H2||op/sqrt(n)≤3,

* ||w||/sqrt(n)≤6Yt/sqrt(m) follows from the spectral, not Frobenius,
  training-feature bound. Coordinatewise |w_i|≤2Yt also holds.
* Each disjoint trained first-layer column has velocity (−2/m)r_aδ1_a.
  Squaring and summing therefore gives the crucial 1/sqrt(m) in (7).
* ||dot W||op≤2Y||w||/sqrt(n), using ||h1_a||≤sqrt(n).
* ||dot H2||F/sqrt(n)≤2Y||w||/sqrt(n)
  [sqrt(m)+121/sqrt(m)], which yields 732Y²t² after integration.

The margins at t0=1/sqrt(1464) are strict, so the stopped inequalities
extend throughout [0,t0]. The stronger time interval [0,m t0] follows
under mY≤1, since every exit margin is controlled by (mY)²(t/m)².
No time interval of that length is inferred from a fixed-time asymptotic.

For the readout remainder, direct subtraction gives (10). The linear
readout contraction term is bounded by 18s(t)/m, giving 54Yt²/(m sqrt(m)).
The feature-motion term integrates to 488Y³t³/sqrt(m). Keeping these
two powers before setting t=mτ is essential. The coefficients in (31c)
are 11·54=594 and 11·488=5368; the other two are 24 and 240.
Their sum at τ≤1,mY≤1 is below 7000, as asserted.

The unused Gaussian column g is independent of the entire training path.
The actual query map and its full nonlinear remainder are odd in g.
Their conditional Gaussian means are therefore exactly zero. Subtraction
of the exact input gradients gives the three bounds in (16), with one
bounded readout infinity norm in the gate-difference term. The argument
does not need a trained carrier maximum or an unproved mixed moment.
Conditional Poincare gives the squared-remainder bound. Applying it to
F² gives Var(F²)≤4L² EF²≤4L⁴ and hence EF⁴≤5L⁴.

This proves a fluctuation-scale remainder, rather than the insufficient
width-independent Taylor error. At t=mτ the bound is
7000 sqrt(m)Y τ²/sqrt(n), and the full query map has Gaussian Lipschitz
constant 66 sqrt(m)Y τ/sqrt(n).

## 2. Initial variance and probability conversion

The lower features for training and query coordinates have iid bounded
rows and independent centered columns. Union Hoeffding at tolerance
epsilon/(m+1)^(3/2) yields (19) exactly. The operator and Frobenius
square-root comparisons in (20) use that QI commutes with every C;
the weaker denominator sqrt(Q) is valid even at the minimal eigenvalue.

The comparison of the whole row function
(sum y_a tanh Z_a)tanh Z_query uses L2 for one term and fourth moments
for the other. The fourth-moment bound 3||y||⁴ follows by expanding
independent centered bounded summands. Together with the Gaussian fourth
moment this yields 1+sqrt(3), as in (21). Centering is an L2 contraction,
so the row standard deviation is at least (3/4)q||y||; retaining
(1/2)q||y|| in (22) is safe.

Conditional independence of upper Gaussian rows gives variance/n, not
an assumed independence of trained neurons. Averaging on the event in
(19) proves (23). The training-only bad event is removed using |K_y|≤Y
and its explicitly stated exponentially small probability. This explains
why the 1/(mn) in the second width inequality is required.

Both steps of the training feature spectral event were reconstructed:
off-diagonal lower correlations ≤1/(4m), conditional Gaussian covariance
derivative of tanh products bounded by one, and second Hoeffding control
of the upper empirical Gram. Gershgorin gives 3/2, below the squared
cap four. The Gaussian matrix-net factor 2 and tail coefficient
cW=100/8−2log9 are consistent with 1/4 nets of both unit spheres.

For independent copies the centered cross term vanishes even after the
training-good indicators, because the indicators are independent of the
unused query Gaussians. The second moment on the joint event is at least
the single-run lower bound when P(T)≥1/2. Inequality
|a−b|⁴≤8(|a|⁴+|b|⁴) gives the factor80. Applying the elementary
second/fourth moment argument to D²1_good yields exactly

\[
 t_*=\min\{1464^{-1/2},q/28000\},\quad
 c=qt_*/(4\sqrt2),\quad p=q^4/(81920\,66^4).
\]

Therefore the actual same-time all-sphere trajectory discrepancy exceeds
c sqrt(m)Y/sqrt(n) with probability at least p at time mt_*, under
mY≤1 and the explicit width conditions (25). This is uniform in m and
d≥m+1 in the displayed region. It is not an endpoint result for m>1.

## 3. Endpoint reconstruction and explicit constants

For one input, the dense feature-clock ODE (33) is independent of label
size before the scalar clock stopping point. On W0op≤10 its real motion
for u≤1 satisfies Wop≤11, ||w||∞≤u,
||a−a0||RMS≤11u²/2 and ||h2−h20||RMS≤61u².
The three nonnegative terms in df/du are exactly (35); all n factors
follow from the canonical mobility convention.

Let g0=(1/2)E tanh²(sqrt(Q/2)Z) and u0=g0^(1/4)/16.
Since 61/256<1/4, the feature Gram remains ≥g0/2 for u≤u0.
For y≤g0^(5/4)/32 there is a unique interpolating u∞≤2y/g0.
The scalar physical clock approaches it exponentially; this proves actual
infinite-time existence and convergence on the stated training event.

The integrated feature error is 61u∞³/3. The fitted interpolation identity
gives |y−u∞G_n|≤244u∞³/3. Combining them gives
||w∞−(y/G_n)h20||RMS≤2440 y³/(3g0⁴).
The exact unused-query gradient subtraction has coefficients
11·2440/3, 2 and40 after bounding g0≤1; their sum is less than9000.
Thus the full nonlinear endpoint remainder has conditional L2 size
≤9000 y³/(g0⁴ sqrt(n)), uniformly in width.

The initialization event has complement at most
2exp(−cW n)+exp(−nQ²/2)+exp(−2ng0²).
The specified additional width inequality makes its contribution to the
initial kernel variance at most q²/(16n). It follows that

\[
 y_*=\min\{g_0^{5/4}/32,\ g_0^2\sqrt{q/72000}\},\qquad
 c_\infty=q/(8\sqrt2),\quad
 p_\infty=q^4g_0^4/(1310720\,22^4)
\]

are valid explicit constants for the actual fitted independent-copy
lower bound. The denominator identity is 64²·4·80=1310720.
Negative y follows from the exact w,y sign symmetry, with hidden paths
unchanged. This proof does not rely on an interchange of the width and
time limits or on a width-independent O(y³) error.

**Verdict for lower source: internally reconstructed, all displayed
finite-time/sample and one-input endpoint claims pass.** Constants are
very conservative. No high-confidence lower quantile as δ↓0 is proved;
the result uses the explicit fixed positive probabilities above.

## 4. Whole-sphere near-root upper bound

The inherited good-pair Lipschitz estimate is pointwise uniform over a
bounded query ball, with Gaussian-root Lipschitz constant
ell_n=C exp(K0 sqrt(log(e+n)))/sqrt(n). The inherited physical tube
also bounds query gradients directly:
||Aᵀδ1/n||≤(||A||F/sqrt(n))(||δ1||/sqrt(n))≤C.
This bound uses only RMS quantities and bounded real slopes, so unbounded
activation values cause no new problem on a bounded query ball.

The physical speed bound CY exp(−kappa t) becomes a fixed Lipschitz
modulus in u=1−exp(−kappa t), including u=1. A sphere 1/n net with
at most(1+2n)^d points and n+1 time points has cardinality N_n as stated.
For each scalar grid value, McShane extension from the same good set is
globally ell_n-Lipschitz and agrees with the actual flow there. Countable
dense subsets justify measurability. Truncating the auxiliary scalar
extension preserves these properties and is not clipping the algorithm.

The Gaussian concentration proof is included in the fully read inherited
source. Two scalar tails and a union bound yield
4N_n exp(−z²/(8ell_n²)); z=ell_n sqrt(8log(8N_n/δ)) gives δ/2.
Both original roots lie on the good set with probability at least1−δ/2
for sufficiently large n. Interpolation of the actual functions using
their joint modulus adds C/n. This verifies (7) and the near-root (8).

The exact root-width target is not a consequence: the factor
exp(K sqrt(log n)) is unbounded. The root's reconstruction of the
adjoint energy sign in (14), covariance normalization in (13), and
carrier-square mixed term (16) agrees with the report. The rank-one
alignment example correctly refutes an inference from averaged Schatten
or marginal carrier moments alone, while making no neural lower-rate claim.

**Verdict for topology improvement: internally reconstructed as an
implication of the inherited broad small-label good-pair theorem.**
It does not supply newly explicit general label constants, a strict
root-width rate, or a population-bias bound.

## 5. Overall limitation

The lower construction can be intersected with any inherited all-time
fitting event of probability tending to one, losing at most its vanishing
failure probability. It does not change general upper-theorem geometry.
The lower coefficient sqrt(m)Y is genuinely visible in the actual
trajectory at t=mt_*; the initialized response note is not needed for
that proof. For the one-input endpoint theorem, fitting is proved within
the same event directly.

This check closes these bounded mathematical components. It does not close
the requested fully explicit, sharp, unbounded-activation theorem package.
