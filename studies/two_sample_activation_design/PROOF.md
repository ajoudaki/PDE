# Broad activation shapes for the two-input global population limit

2026-09-08. Mathematical extension. Review status is recorded separately
in REVIEW_STATUS.md. The companion proofs form part of this argument.
Supplied mathematical lemmas, not historical review verdicts, are its
dependencies.

## 1. Exact model and the essential theorem

Fix \(0<\delta\le1\), \(x_1,x_2\in\mathbb R^d\) with
\(\|x_i\|^2=d\), \(|\rho|\le1-\delta\), \(\rho=x_1^Tx_2/d\),
and \(y_i\in\{-1,1\}\). Initialize independent entries
\[
 W^1_{ij}\sim N(0,1/d),\quad W^2_{ij},W^3_{ij}\sim N(0,1/n),
 \quad C_i\sim N(0,n^{-2}).
\]
At width \(n\), use
\[
 z_i^1=W^1x_i,\quad h_i^\ell=\phi(z_i^\ell),\quad
 z_i^2=W^2h_i^1,\quad z_i^3=W^3h_i^2,\quad
 f_i=\langle C,h_i^3\rangle_n,\quad r_i=f_i-y_i,
\]
where \(\langle u,v\rangle_n=u^Tv/n\). The backward fields are
\[
 b_i^3=C\phi'(z_i^3),\quad
 b_i^2=\phi'(z_i^2)(W^3)^Tb_i^3,\quad
 b_i^1=\phi'(z_i^1)(W^2)^Tb_i^2.
\]
The loss is \(\mathcal L=(r_1^2+r_2^2)/2\) and the raw metric is
\[
 \|d\Theta\|_{\rm raw}^2
 =\frac dn\|dW^1\|_F^2+\|dW^2\|_F^2+\|dW^3\|_F^2+\|dC\|_n^2.
\]
Its exact physical gradient flow is
\[
 \dot W^1=-d^{-1}\sum_i r_i b_i^1x_i^T,\quad
 \dot W^\ell=-n^{-1}\sum_i r_i b_i^\ell(h_i^{\ell-1})^T
 \quad(\ell=2,3),\qquad \dot C=-\sum_i r_i h_i^3.
\]
Raw GD is simultaneous Euler for these equations with step \(n^{-2}\).
Raw parameters are interpolated linearly; hidden fields are recomputed
from them. At nodes use right velocities, terminal-left at the final
endpoint. The finite readout is retained throughout.

Define
\[
 \mathcal A=\{\psi\in C^2(\mathbb R):
 |\psi(0)|\le1,\ \|\psi'\|_\infty\le1,\ \|\psi''\|_\infty\le1\}.
 \tag{1}
\]
Then \(|\psi(z)|\le1+|z|\). Boundedness of the shape, oddness,
monotonicity, analyticity and tail limits are not required.

**Theorem A (one uniform coefficient for global dynamics).**
There is an explicit universal \(c_{\rm dyn}>0\), defined in (4),
such that every fixed
\[
 a\in[1/2,1],\quad \psi\in\mathcal A,\quad
 0<e\le c_{\rm dyn}\delta^{31/8},\qquad
 \phi(z)=az+e\psi(z)                                     \tag{2}
\]
used in all three hidden layers has these properties:

1. There is one autonomous global strong population loss flow on the
   canonical generated Gaussian action spaces. It is unique against
   bounded-primal strong competitors on the same spaces, including
   nonsymmetric ones, and continues uniquely from reached states.
   Its state is a first-layer field, two bounded actions with actual
   adjoints and Hilbert--Schmidt learned increments, and a readout field.
   The state is infinite-dimensional.
2. On each fixed physical interval \([0,T]\), actual finite GF and
   raw GD converge jointly, along the full width sequence in probability,
   to this flow. Predictions, loss and all four true raw kernel blocks
   converge uniformly in time. Both orientations of the actions are
   retained on generated probes. At each layer the joint two-sample
   preactivation/feature path law converges in
   \(\mathcal W_2(C([0,T];\mathbb R^4))\), with supremum norm.
   Same-layer fields and recomputed velocities converge jointly in
   \(\mathcal W_2\), uniformly in time and at any fixed finite collection
   of times. Second moments and integrated squared speeds converge.
3. The population predictions satisfy \(f_i=y_i g\), and
   \(\mathcal L(t)\le\exp(-\delta t/2048)\).

The coefficient is independent of the shape within \(\mathcal A\),
actual angle, labels, dimension, width, caps, meshes and horizon.
Convergence constants may depend on the fixed shape, data and \(T\).
There is no probability supremum over this class or over the infinite
time half-line, and no cross-width operator-norm convergence assertion.

## 2. Additional nonaffinity and initial feature learning

For \(G\sim N(0,1)\), define
\[
 \mathcal R_\psi(Z)=\inf_{\alpha,\beta}
 E[\psi(Z)-\alpha-\beta Z]^2,\qquad
 \eta_\psi=\min_{1/\sqrt{404}\le\nu\le260}\mathcal R_\psi(\nu G).
 \tag{3}
\]
Every globally nonaffine \(\psi\in\mathcal A\) has \(\eta_\psi>0\).

**Theorem B (persistent nonaffinity).** For a globally nonaffine
shape in Theorem A, impose additionally
\(e\le c_{\rm NL}(\psi)\delta^{31/8}\), with (4). Then
\[
 \inf_{t\ge0,i,\ell}\inf_{\alpha,\beta}
 E[\phi(z_i^\ell(t))-\alpha-\beta z_i^\ell(t)]^2
 \ge e^2\eta_\psi/4>0.
\]

Every globally nonaffine shape in Theorem A also has nonzero population
initial acceleration in every hidden parameter block and every
sample/layer's preactivation and feature. The readout has nonzero initial
velocity, and the projected total kernel changes at small positive time.
This initial-motion statement needs no additional \(\eta_\psi\) cutoff.
It does not assert nonzero hidden velocity at every later instant.

Thus global dynamics has a shape-uniform coefficient; the quantitative
persistent nonaffinity margin has a separate shape obligation.

## 3. Explicit sufficient constants

Set
\[
 C_0=1296000\exp(1404),\quad C_z=1500C_0,\quad C_g=14400C_0,
\]
\[
 H=10^{30}[1+C_0+C_z+C_g+\exp(1410)]^4,\qquad K=H^2,
\]
\[
 c_{\rm dyn}=\min\left\{
 \frac14,\frac1{2C_0(8\sqrt2)^3},
 \frac1{4C_g(8\sqrt2)^{11/4}},
 \frac12\,24^{-31/4}K^{-46}\right\},\qquad
 c_{\rm NL}(\psi)=
 \frac{\sqrt{\eta_\psi}}{4C_z(8\sqrt2)^{7/2}}.             \tag{4}
\]
These numbers are positive and chosen before the data. The coefficient
rule is polynomial in separation, but its numerical prefactor is still
extremely small. It is sufficient, not necessary or optimal, and does
not certify a practically moderate nonlinear amplitude.

## 4. Detailed proof components and their interfaces

The architecture is: control an affine reference up to prediction
\(3/2\); preserve its endpoint margin under the nonlinear perturbation;
bound every actual source-response coefficient; remove auxiliary caps;
convert its first-fitting feature interval to all physical times; then
apply the exact finite-algorithm and observable comparisons.

The complete extra derivations are in these companions:

- [SHAPE_SYMMETRY.md](SHAPE_SYMMETRY.md), Sections 2--4, proves sample
  symmetry for arbitrary scalar activations, with different fixed bases
  for forward and backward sample slots. This replaces odd label
  folding. It also bounds actual affine Gaussian marginal standard
  deviations in \([1/\sqrt{404},260]\), independently of \(\delta\).
- [LINEAR_GROWTH.md](LINEAR_GROWTH.md), Sections 2--4, derives the raw
  perturbation constant, forward/prediction bounds and all learned
  Gram discrepancies for linearly growing shapes. It uses raw typed
  coordinates without dividing by a small inactive sample variance.
- LINEAR_GROWTH.md, Sections 5--6, proves the source-value inequalities
  and verifies the derivative/sector interfaces, including current
  transpose returns and arbitrary causal backward row errors.
- SHAPE_SYMMETRY.md, Sections 5 and 7, and LINEAR_GROWTH.md,
  Sections 1, 6 and 7, establish regression, initial motion, and
  uniform shape subclasses.

The specialized inherited mathematical lemmas are the affine
balance/primal proof in ../two_sample_odd_activation_quantitative,
the affine transfer, response and sector proofs in
../two_sample_odd_activation_power4, and the generic source/action,
cap, physical and observable proofs identified in SHAPE_SYMMETRY.md.
Their exact files and hashes are listed in DEPENDENCIES.json.
Only the exact normalized equations are imported from the older
NORMALIZED_GATES_AND_PRIMALS note; its intrinsic moment inference is
replaced by the direct raw proof.

Here is the complete assembly. Define
\[
 v=(1+y_1y_2\rho)/2,\quad \lambda=a^3\sqrt v,\quad
 M=[3/(\sqrt2\lambda)]^{1/4}.
\]
This is the actual endpoint scale, with
\(1<M\le24^{1/4}\delta^{-1/8}\). The affine feature interval has
duration \(S\le M^4\), with each dataset stopped at its own first
hit \(g=3/2\). Polynomial Hilbert-space local existence and the
gradient-energy endpoint estimate give affine continuation to that hit.
The exact balances and integrated curvature supply the inherited
affine/source certificate.

For linearly growing shapes the same-state raw forcing is at most
\(40eb^3\), as derived in LINEAR_GROWTH.md Section 2.
Only the affine field is differentiated in the comparison.
The old raw tube also bounds the normalized active first root by \(b\);
this bound is used for the affine prediction comparison, not inferred
from the unnormalized sample projections.
The resulting estimates are
\[
 E_{\rm raw}\le C_0e\lambda^{-3},\qquad
 \max_{i,\ell}\|z_{i,e}^\ell-z_{i,0}^\ell\|_2
       \le C_ze\lambda^{-7/2},\qquad
 |g_{e,R}(S)-3/2|\le C_ge\lambda^{-11/4}.                 \tag{5}
\]
Since \(\lambda\ge\sqrt\delta/(8\sqrt2)\), the first three entries
of \(c_{\rm dyn}\) close the raw radius-one tube and give
\(g_{e,R}(S)\ge5/4\), uniformly in the cap.

The direct raw typed calculation gives learned-moment strict density
errors at most \(KeM^{15}\) and complete backward row errors at most
\(KeM^{19}\). It avoids the invalid inference
\(e/\sqrt\delta\lesssim eM^4\) when the inactive variance can vanish
independently of \(v\).

The affine transfer certificate and the positive sector supersolution
concern affine arrays, so they are unchanged by the shape. On their
coefficient box, the newly checked value equations give, for \(p\ge2\),
\[
 \|q_k^1\|_p\le K^{10}M^{15}\sqrt p,\quad
 \|q_k^2\|_p\le K^{10}M^{13}\sqrt p,\quad
 \|C_k\|_p\le K^{10}M^{11}\sqrt p.
\]
Bounded \(\psi'\) and \(\psi''\) give the same random derivative
envelope, whose moments are bounded if \(eK^{22}M^{19}\le1\).
After controlling the envelope, Cauchy--Schwarz uses the smaller
actual primal \(L^2\) bounds \(KM^3,KM^2,KM\). The complete
coefficient forcing is therefore
\[
 q_{\rm def}\le K^{30}eM^{19}.
\]
The supplied sector supersolution closes if
\(q_{\rm def}\le K^{-16}M^{-12}\). Its hypotheses retain signs,
both sample sectors, all past named source slots, current returns
and the single-source time-step factor; the companions check each
shape substitution. Our choice gives
\[
 eM^{31}\le K^{-46}/2,\quad
 eK^{22}M^{19}\le K^{-24}M^{-12}/2<1,\quad
 q_{\rm def}\le K^{-16}M^{-12}/2.                        \tag{6}
\]
Continuity in amplitude at fixed cap and sufficiently fine fixed mesh,
followed by a first-exit contradiction, proves cap- and mesh-uniform
source bounds. These yield Gaussian tails for the actual incoming
fields; the tails are conclusions rather than assumptions.

The supplied asymmetric cap comparison has error
\(C\exp(CR-cR^2)\) on this feature interval and requires tails only
of the reference. It constructs a strong uncut autonomous
feature-gradient path through \(S\). Its sample symmetry gives
\(f_i=y_i g\). At its first hit \(s_*<S\) of \(g=1\), bounded
\(g'\) implies \(1-g(s)\le C(s_*-s)\). Hence
\[
 t(s)=\int_0^s[2(1-g(u))]^{-1}\,du
\]
diverges at \(s_*\). Its inverse converts the feature gradient into
exactly the physical loss flow for every \(t\ge0\).
The initialized odd/even Gaussian decomposition gives
\(\kappa(0)\ge\delta/8192\); the strong radial identity gives
\(g_s'\ge\kappa(0)\). Thus
\(\dot{\mathcal L}=-4g_s'\mathcal L\) proves Theorem A's rate.

The physical comparisons retain both actual finite residuals.
On each fixed \([0,T]\), their cap-removal cost is
\(C_T\exp(C_TR-cR^2)\), so no additional activation restriction
depends on \(T\). They prove uniqueness against nonsymmetric
bounded-primal strong competitors and reached-state restart.
Width is taken at fixed cap and auxiliary mesh; deterministic Euler
estimates remove that mesh; then the cap is removed. Actual raw GD
adds the prescribed \(C_{R,T}n^{-2}\) reference error.

The fixed-cap observation bridge uses linear growth, bounded first
two derivatives and its named product-query truncations, all checked
here. For velocities, first fix a reference-velocity truncation,
remove the cap, then remove that truncation, using the compact
\(L^2\) time image of the uncut velocity. The grid inequality
\(\|x-I_hx\|_\infty^2\le4h\int_0^T|x'|^2\) upgrades finite-time
laws to the path-space Wasserstein laws. Kernel contractions use
converging same-layer \(L^2\) factors. This proves the asserted
observable scope, rather than deducing it from raw energy alone.

No step so far uses nonaffinity or \(\eta_\psi\), so the whole
class \(\mathcal A\) shares \(c_{\rm dyn}\). For Theorem B,
the affine variance interval makes \(\eta_\psi>0\). Square-root
regression error is 2-Lipschitz under coupled \(L^2\) distance.
Equation (5) and \(c_{\rm NL}\) give
\(\mathcal R_\psi(z)\ge\eta_\psi/4\). Absorbing the affine part
gives exactly the factor \(e^2\). This holds through \(S\), hence
at every physical time. Initial motion uses
\(\phi'\ge1/4\), nonconstant \(\phi'\), and the actual Gaussian
transpose returns as proved in SHAPE_SYMMETRY.md Section 7.
It imposes no quantitative \(\eta_\psi\) cutoff. Both theorems follow.

## 5. Improvements and the remaining practical question

The class includes normalized sine, cosine, tanh, smooth compactly
supported shapes, softplus and \(\sqrt{1+z^2}\).
Any finite bounds on \(|\psi(0)|,\|\psi'\|_\infty,\|\psi''\|_\infty\)
can be normalized by dividing by their maximum and one.
ReLU itself is not \(C^2\) and is not covered.
Uniform open subclasses with common nonaffinity margins are
constructed in LINEAR_GROWTH.md Section 7.

[AFFINE_POSITIVITY.md](AFFINE_POSITIVITY.md) separately proves an
algebraic affine response certificate, avoiding an exponential
propagator estimate. It is not used to claim a better prefactor in
(4); its proposed improved nonlinear closure remains provisional.

[RELATIVE_NONLINEARITY.md](RELATIVE_NONLINEARITY.md) proves
\(\mathcal N_\phi(Z)\le(e/(a-e))^2\) for this class on every
nondegenerate input law. Thus our tiny prefactor does not certify
substantial relative nonlinearity. A calibrated moderate sine
candidate has an exact approximately 6.4 percent initialized
nonlinear fraction at every layer and a well-conditioned initialized
kernel, proved in [SINE_INITIALIZATION.md](SINE_INITIALIZATION.md).
Its global trained limit at that moderate coefficient is open.

[BOUNDED_ACTIVATION_ROUTE.md](BOUNDED_ACTIVATION_ROUTE.md) proves
finite-horizon pointwise bounds on the readout and learned reverse
memories for bounded activations. It isolates the remaining reused
Gaussian-action tail problem. Its counterexample to deriving tails
from bounded input, energy and exchangeability alone is not a
counterexample to the actual neural dynamics. This investigation
does not establish the moderate-amplitude global theorem.
