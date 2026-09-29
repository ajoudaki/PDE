# Independent check of the autonomous one-input theorem

Checked 28 September 2026. Frozen candidate:
`AUTONOMOUS_ONE_SAMPLE.md`, SHA256
`571c6eb4a31ae7195441713c584d5d3a87208be9c48b68927aa0145f717cd7a8`.
The hash was verified before reading the complete candidate. The full
`OLD_CLOCK_ROUTE.md` was available as the assigned dependency; the current
canonical model and notation were also in scope. The candidate's proof is
self-contained for its additional transform, Hilbert-space construction,
backward derivative estimate and step-tail bound. The
`solve-math-rigorously` skill was applied. I did not author the candidate,
read another check, run experiments, or use other studies. This is a scoped
independent internal check, not a promotion review.

**Verdict: PASS in the stated scope.** The fully autonomous old-clock
closure, with one normalized training input and two hidden tanh layers,
has width-independent and order-independent `O(P^-2)` parameter and test
prediction tracking at zero initial readout. The stated nonzero bounded
readout correction and its small Gaussian finite-width specialization also
follow. I found no material proof gap or incorrect constant. The result
does not establish arbitrary sample count, greater depth, or identification
of a Gaussian finite-width population operator.

## 1. Model and transformed coordinate

I checked the input normalization, mobilities, residual sign and all
rank-one factors. With `v=x/sqrt(d)` and `||v||=1`, the first-layer
equation implies

\[
 \dot u=\dot a\,v=-2r\operatorname{sech}^2(u)W^*\delta.
\]

The declared primitive satisfies

\[
 G'(s)=\tfrac12+\tfrac12\cosh(2s)=\cosh^2(s),
\]

so `dot eta=-2r W^*delta` has the exact sign and scaling. Orthogonal
first-row components are fixed; the reconstruction
`a=a_0+[U(eta)-u_0]v^T` therefore recovers every original first parameter.
This cancellation would acquire an input-norm factor without the stated
normalization, and does not directly extend to several nonorthogonal
training inputs. Neither extension is claimed.

`G` is an increasing onto map because its derivative is at least one and
its limits at the two ends of the real line are infinite with opposite
signs. Thus its inverse is globally 1-Lipschitz. The potentially
nonintegrable value `G(u_0)` is used only pointwise; `u_0` is finite almost
everywhere, and

\[
 |G^{-1}(G(u_0)+\eta)-u_0|\le|\eta|.
\]

Consequently `U(eta)-u_0` and `tanh(U(eta))` are legitimate globally
Lipschitz `L2` maps, with constants at most one. There is no hidden
exponential-moment assumption on `u_0`. No claim of Fréchet
differentiability of the tanh map on `L2` is needed.

The pointwise absolutely continuous representatives used in the proof
justify the inverse chain rule and recover the original first equation.
For completeness, the reverse implication needed for uniqueness in
original coordinates also holds: for any original-coordinate `L2`
solution, its integral first-layer equation gives an almost-everywhere
absolutely continuous scalar path `u(t)`. On each compact regular interval
the continuous middle operator and readout have bounded operator and
`L2` norms, so `q=W^*delta` is locally integrable in time with values in
`L2`. Each scalar `u` path has a compact real range; `G` has bounded
derivative on that range, so the ordinary scalar chain rule is applicable
without a population bound on `G'`. It gives

\[
 G(u(t))-G(u_0)=-2\int_0^t r(s)q(s)\,ds
 \quad\hbox{almost everywhere}.
\]

The right side is a norm-bounded Bochner `L2` integral. Therefore the
transformed increment belongs to `L2` and obeys `dot eta=-2rW^*delta`.
The original readout equation gives the same bound `||w||_infinity<=B`
as in the candidate, so this transformed solution also solves the clipped
`eta` system. Local uniqueness of that system now gives uniqueness of the
original solution. It would improve the
candidate's exposition to add this one sentence before asserting
uniqueness among original solutions; it is a proved implication, not an
additional hypothesis or gap.

## 2. Raw moments, exact source, and population existence

For shifted Legendre polynomials, the exact identity

\[
 x p_j'(x)=j p_j(x)+\sum_{i<j}(2i+1)p_i(x)
\]

gives the dilation coefficients in candidate (3). Differentiating raw
moments on `[0,tau]` gives the displayed insertion sources `|r|h` and
`r delta`; the latter is `|r|b` when the clock is valid. The initial
constant forward prefix has `H_0=h_0` and all higher moments zero; the
zero backward prefix has every `B_j=0`. The factor `-2/tau` and weights
`2j+1` in reconstruction are the correct orthogonal projection pairing.

The Hilbert--Schmidt identity
`||delta tensor h||_HS=||delta||_(H2)||h||_(H1)` is valid even though
the fixed `W_0` is not Hilbert--Schmidt. At finite equal widths the
coordinate matrix is `delta h^T/n` and its Hilbert--Schmidt norm is
ordinary Frobenius norm, exactly as in candidate (9).

Clipping only the readout multiplier inside `delta` makes both transformed
vector fields locally Lipschitz on the stated Banach spaces. The product
estimate in the candidate controls the varying activation gate by the
fixed clipping bound; all other operations are bounded-operator actions,
finite sums of rank-one products, pairings, or Lipschitz activation maps.
Reconstruction is locally Lipschitz for every fixed `P` on `tau>0`.
Neither a width-uniform local existence interval nor a compactness claim
for an infinite-dimensional ball is used.

The readout calculation is exact:

\[
 2\langle w,-2(f-y)k\rangle=-4(f-y)f
 =y^2-4(f-y/2)^2.
\]

It remains valid in the clipped auxiliary system. It gives `R,Q,S,A`
without loss monotonicity. Pointwise integration of `dot w=-2rk` then
gives `||w||_infinity<=B_0+2S=B`, so clipping at `B+1` is inactive.
Clipping also never increases the pointwise magnitude of its argument,
so the intermediate bound `||delta||<=R` is valid before inactivity is
known.

Projection contraction bounds the learned closure operator by
`2R sqrt(SA)<=2AR`; dense history integration gives `2SR<=2AR`.
Thus `||W||_op<=K` and `||q||<=KR` on both paths. The finite list of
moments and all state velocities are bounded before any proposed finite
maximal endpoint. Integrating those velocity bounds gives a Cauchy limit
in the state Banach space. Its clock is at least one, and local existence
extends it. This proves the asserted global construction and handles the
infinite-dimensional continuation issue correctly.

At `r=0` every coordinate of the raw state has zero velocity. Local
uniqueness, also for the reversed autonomous equation, excludes reaching
such an equilibrium from a nonstationary path in finite regular time.
Thus a nonstationary path has constant residual sign, and its own clock
is a valid coordinate on every compact interval. This argument uses no
uniform positive lower bound on the residual. Initial zero residual is
correctly treated as stationary, including `w_0=y=0`.

## 3. Stability closes in the stated transformed norm

Every response bound in candidate (15) checks directly. In particular,

\[
 \widehat\delta-\delta
 = (\widehat w-w)\tanh'(\widehat z)
   +w[\tanh'(\widehat z)-\tanh'(z)]
\]

uses the derived bounded dense readout, and

\[
 \widehat q-q
 =\widehat W^*(\widehat\delta-\delta)
     +(\widehat W-W)^*\delta
\]

uses bounded operators and Hilbert--Schmidt differences. The initialized
carrier is never used as a multiplication operator. The first-layer
activation gate has disappeared exactly from the transformed velocity.

The constants `A_z,A_r,A_delta,A_q` are safe upper bounds. Summing the
three velocity inequalities gives exactly

\[
 L=2(KR+R+1)A_r+2Q(A_q+A_\delta+R+A_z).
\]

The differentiated reconstruction has the sole defect

\[
 E=2|r|(b-b^*)\otimes(h-h^*).
\]

There is no extra defect in `eta`: its equation remains the exact
transformed first-layer equation using the reconstructed `W`. The
integral comparison (18) and the exponential factor `exp(LT)` therefore
follow. This is a derived Lipschitz comparison on the actual uniformly
bounded transformed solutions, not an assumed original-coordinate tube
bound.

## 4. Projection energy, own-history derivatives and both prefix cases

The projection-energy identity applies to the closure's actual histories
in its own moving clock. Its prefix projection errors are zero. Thus

\[
 D_g(t)=\int_0^t|r(s)|\|g(s)-g^*(s)\|^2ds,
 \qquad
 \int_0^t\|E(s)\|_{\rm HS}ds\le2\sqrt{D_b(t)D_h(t)}.
\]

The endpoint errors in the time integral use the projection on each
current interval; the final `D_g(t)` is the final interval's projection
tail. The exact energy identity is what equates these quantities.
The candidate does not accidentally substitute a fixed final projection
inside the time integral.

The Legendre estimate has the correct factor
`tau^2/[4P(P+1)]`. It extends to Hilbert-valued histories by scalar
projections and monotone convergence. The own forward derivative is

\[
 h'=-2\operatorname{sgn}(r)\operatorname{sech}^4(u)q,
\]

so its squared derivative integral is at most `Z=4SK^2R^2`. This
matches the constant forward prefix continuously. The backward mass is
at most `SR^2`, proving the first accumulated-defect constant `C_1`.

The stronger argument is valid and not circular. Endpoint evaluation
gives `||b^*||<=PR`, hence `||b-b^*||<=(P+1)R`. Combining this with
the already proved forward projection tail gives

\[
 \int_1^{\tau(t)}\|E/|r|\|_{\rm HS}^2d\xi
 \le4(P+1)^2R^2D_h(t)
 \le R^2A^2\frac{P+1}{P}Z\le I.
\]

This checks the exact cancellation of the endpoint factor and the
constant `I=2R^2A^2Z`. The next two estimates then give

\[
 \int\|W'\|_{\rm HS}^2\le8R^2S+2I,
 \qquad
 \int\|z'\|^2\le16R^2S+4I+2K^2Z=V.
\]

Finally, `w'=-2 sign(r) k` and the bounded readout imply

\[
 \delta'=w'\tanh'(z)+w\tanh''(z)z',\qquad
 \int\|\delta'\|^2\le8S+8B^2V=J.
\]

All divisions by `|r|` occur only on a single regular nonstationary
clock path. The estimates after changing coordinates are independent of
its minimum residual. The candidate's pointwise absolutely continuous
representatives justify the chain and product rules, and the resulting
square-integrable derivatives give the claimed Bochner `H1` regularity.

At zero readout, `delta_0=0`, so `b=sign(r)delta` joins its zero prefix
continuously. Its derivative energy is `J`; applying the same Legendre
bound to both histories gives

\[
 \int_0^T\|E\|_{\rm HS}dt
 \le\frac{A^2\sqrt{ZJ}}{2P(P+1)}.
\]

This is the accumulated absolute velocity defect, which is exactly what
the stability comparison needs. It is stronger than a signed matrix
reconstruction error.

For nonzero readout, the decomposition
`b=c+sign(r(0))delta_0 1_(xi>1)` leaves `c` continuous across the
prefix and with the same derivative bound. The step estimate is valid
for every `P>=1` and `tau>=1`: if its nonzero interval has length below
`a=tau/P`, approximation by zero suffices; otherwise a ramp of length
`a` has step error at most `sqrt(a)` and projection error at most
`sqrt(a)/2`. This verifies the factor `3/2` in (27).

Multiplying the resulting backward tail by the forward tail yields
exactly

\[
 \frac{A^2\sqrt{ZJ}}{2P(P+1)}
 +\frac{(3/2)A^{3/2}\|\delta_0\|\sqrt Z}
        {\sqrt{P^2(P+1)}}.
\]

Thus both `C_2` and `C_(3/2)` in (7) check. Taking the better of this
estimate and the mass-based estimate is valid, proving all of (8).

## 5. Original parameters, predictions and Gaussian quantifiers

The inverse-transform contraction gives
`||a_hat-a||_(row,L2)=||u_hat-u||_(L2)<=||eta_hat-eta||_(L2)`.
Consequently all three original parameter blocks are controlled with
the stated first-layer/readout RMS and unnormalized hidden Frobenius
scaling. No comparison of first backward fields is needed, and the
candidate correctly refrains from asserting their linear `L2` rate.

For a test input, the first-preactivation difference equals
`(u_hat-u)(x^T x'/d)` exactly. The middle operator and readout estimates
then give (30); `||x||/sqrt(d)=1` supplies the displayed bound on this
input factor. Minkowski and the reverse triangle inequality justify
the `L2(nu)` and test-RMSE claims with the stated finite second input
moment. These are dense-tracking statements, as the candidate says.

The Gaussian operator estimate uses two `1/4` nets and the correct
bilinear variance `1/n`. Choosing a sufficiently large fixed cutoff
makes its failure probability exponentially small in `n`. For stored
readout `w_0=g/n`, with standard independent Gaussian coordinates,

\[
 R_0=\frac{\|g\|_2}{n\sqrt n},\qquad
 B_0=\frac{\max_i|g_i|}{n}.
\]

The events `R_0<=2/n` and `B_0<=1` have exponentially small failure
probability for large `n` by, respectively, a Gaussian squared-norm
tail and the union bound `2n exp(-n^2/2)`. On these events all constants
other than the displayed `||delta_0||` factor have a common deterministic
bound, and `||delta_0||<=R_0<=2/n`. This proves (32), with no missing
factor of `sqrt(n)`.

The candidate appropriately separates pathwise bounded-operator
population construction from identification of the Gaussian limit. It
does not convert an exponentially growing Gronwall constant into an
unsupported all-moments assertion. The fixed-width high-probability
events have the advertised width-independent deterministic constants;
they are not events covering every Gaussian realization.

## 6. Scope of the pass

All formulas (3)--(32) pass the analytic check under the stated one-input,
two-hidden-layer, normalized-input and bounded-readout assumptions. The
zero-readout population statement and the canonical small-readout
finite-width statement are kept separate correctly. The candidate is a
complete autonomous theorem in this restricted scope. It leaves the
arbitrary-depth and arbitrary-finite-data theorem open. No change to the
maintained manuscript, code or scientific book is justified by this
internal check alone.
