# Multi-input, all-time small-label tracking for general activations

Continuation, 28 September 2026. The object is the unchanged autonomous
old-clock response-memory closure at arbitrary fixed finite depth and sample
count. This note combines the activation-general source bounds, a local
derivative-modulus comparison, and a Gaussian initialization argument. It does
not change the paper or maintained book. The full component derivations are
`ACTIVATION_SMALL_LABEL_ROUTE.md`, `ACTIVATION_LOCAL_MODULUS.md`, and
`ACTIVATION_INITIAL_GRAM.md`; their scope and verification are recorded in
the study README.

## 1. Activation class and exact theorem

Different hidden layers may use different functions. Assume for every layer

\[
 \phi_\ell\in C^{1,1}_{\mathrm{loc}}(\mathbb R),\qquad
 s_\ell:=\sup_{u\in\mathbb R}|\phi_\ell'(u)|<\infty.
 \tag{1}
\]

Thus the derivative is locally Lipschitz and the activation has a globally
bounded slope. The activation itself may be unbounded:
`|phi_l(u)|<=|phi_l(0)|+s_l|u|`. No oddness, monotonicity, analyticity,
strictly positive derivative, globally bounded second derivative, or common
activation across layers is required for the deterministic theorem.

Use the canonical network and squared loss

\[
 h_{1,a}=\phi_1(W_1x_a/\sqrt d),\quad
 h_{\ell,a}=\phi_\ell(W_\ell h_{\ell-1,a}),\quad
 f_a=w^Th_{L,a}/n,\quad r_a=f_a-y_a,\quad
 \rho=\left(m^{-1}\sum_a r_a^2\right)^{1/2}.
\]

Backward responses exclude the residual:
`delta_L=w odot phi_L'(z_L)` and
`delta_l=phi_l'(z_l) odot W_(l+1)^T delta_(l+1)`.
The canonical block mobilities remain `(n,1,...,1,n)`; the first-layer,
hidden-layer and readout velocities are respectively

\[
 -\frac2m\sum_a r_a\delta_{1,a}(x_a/\sqrt d)^T,\qquad
 -\frac2{mn}\sum_a r_a\delta_{\ell,a}h_{\ell-1,a}^T,\qquad
 -\frac2m\sum_a r_a h_{L,a}.
 \tag{2}
\]

The closure retains the exact initialized hidden matrices and uses its own
residual clock `tau=1+integral rho`. For each hidden link/sample it retains
`P` forward and backward Legendre moments. They evolve by

\[
 \dot M_k=q-\frac\rho\tau
       \left[kM_k+\sum_{j<k}(2j+1)M_j\right],
\]

with forward source `q=rho h_(l-1,a)` and backward source
`q=r_a delta_(l,a)`. The forward degree-zero moment starts at the initial
activation; the remaining forward and all backward moments start at zero.
Reconstruction is

\[
 \widehat W_\ell=W_{0,\ell}
 -\frac2{mn\tau}\sum_{a=1}^m\sum_{k<P}(2k+1)
                 M^b_{\ell,a,k}(M^h_{\ell-1,a,k})^T.
 \tag{3}
\]

The outer parameters follow (2), evaluated at the reconstructed network.
No activation truncation or supplied dense response is introduced.

Fix depth, data, and positive bounds `K,R_0,lambda`. Assume the initialized
physical network satisfies

\[
 \max_{\ell\ge2}\|W_{0,\ell}\|_{\rm op}\le K,\qquad
 \max_a\frac{\|W_{1,0}x_a/\sqrt d\|_2}{\sqrt n}\le R_0,
\]
\[
 \Gamma_w(0):=\frac{H_L(0)^TH_L(0)}{mn}\succeq\lambda I_m,
 \qquad B_0:=\|w_0\|_2/\sqrt n\le Y,
 \quad Y:=\left(m^{-1}\sum_a y_a^2\right)^{1/2}.
 \tag{4}
\]

There is `Y_*>0`, independent of width and order, such that for
`0<Y<=Y_*<=1`, every dense flow and every finite-order closure exist for all
physical time, converge to interpolating parameters, and satisfy

\[
 \widehat\rho_P(t)\le\widehat\rho_P(0)e^{-\kappa t},\qquad
 \rho_D(t)\le\rho_D(0)e^{-\kappa t},\qquad
 \int_0^\infty(\widehat\rho_P+\rho_D)dt\le CY,
 \tag{5}
\]

where `kappa>0,C` are independent of `n,P,Y` in this range. Their top-feature
Grams stay above `lambda I/2`. At `Y=0`, condition `B_0<=Y` makes both
systems stationary and fitted.

The proof also supplies a constant `R`, independent of width and order,
bounding every training preactivation RMS on both paths. Set

\[
 \ell_n=\max_{1\le\ell\le L}
   \operatorname{Lip}\bigl(\phi_\ell';[-R\sqrt n,R\sqrt n]\bigr),
 \qquad \chi_n=\ell_n\sqrt n\,Y^2.
 \tag{6}
\]

Each `ell_n` is finite by (1). In the normalized parameter discrepancy

\[
 d_n(t)=\frac{\|\widehat W_1-W_{1,D}\|_F}{\sqrt n}
       +\sum_{\ell=2}^L\|\widehat W_\ell-W_{\ell,D}\|_F
       +\frac{\|\widehat w-w_D\|_2}{\sqrt n},
\]

there are constants `A,a>=1`, independent of width, order and time, such that

\[
 \sup_{t\ge0}d_n(t)
 \le A e^{a(Y+\chi_n)}
 \left\{
   \frac{B_0Y^{3/2}}{P^{3/2}}+
   \frac{Y^{5/2}\sqrt{1+\chi_n^2+\log(e+P)}}{P^2}
 \right\}.
 \tag{7}
\]

In particular a joint choice

\[
 P\ge\lceil e^{2a\chi_n}\rceil
 \tag{8}
\]

gives `sup_(t>=0)d_n(t)<=C/P`, with `C` independent of `n,P,t`.
At exactly zero readout the smaller sufficient threshold is

\[
 P\ge\lceil(1+\chi_n)e^{a\chi_n}\rceil.
 \tag{9}
\]

The theorem is uniform on these joint width/order regions. It is not a
statement uniform over unrestricted pairs `(n,P)`. Constants and `Y_*`
depend on the fixed depth, data, the initialization bounds in (4), the
activation values at zero and global slope bounds. Gate curvature enters
through (6); no width dependence is hidden in `Y_*`.

## 2. Why unbounded activations are allowed

The previous tanh proof used `|h|<=1`. Here stop on the fixed tube

\[
 \|W_\ell\|_{\rm op}<K+1\quad(\ell\ge2),\qquad
 \max_a\|z_{1,a}\|_2/\sqrt n<R_0+1.
\]

Linear growth supplies deterministic feature RMS bounds, recursively:

\[
 M_1=|\phi_1(0)|+s_1(R_0+1),\qquad
 M_\ell=|\phi_\ell(0)|+s_\ell(K+1)M_{\ell-1}.
 \tag{10}
\]

Let `Q=1+M_L`, choose an activity cap `S=cY` with fixed
`c=4Q/lambda`, and put `A_S=1+S`. The readout equation gives
`B(t)<=Y+2M_L S=O(Y)`. Backpropagation then gives
`max_a ||delta_(l,a)||_2/sqrt(n)<=beta_l=O(Y)` on the tube.
Projection contraction in (3) yields

\[
 \|\widehat W_\ell-W_{0,\ell}\|_F
 \le2M_{\ell-1}\beta_\ell\sqrt{A_SS}=O(Y^{3/2}),
\]

and the first preactivation displacement is `O(Y^2)`. Both are strictly
inside the tube for a width/order-independent small-label threshold.

The exact projection-energy identities do not depend on the activation.
Writing `b_(l,a)=(r_a/rho)delta_(l,a)` on the physical history and zero on
the prefix, the physical defect is

\[
 E_\ell=\frac{2\rho}{mn}\sum_a
       (b_{\ell,a}-b_{\ell,a}^*)
       (h_{\ell-1,a}-h_{\ell-1,a}^*)^T,
 \qquad E_1=E_w=0.
 \tag{11}
\]

Stars mean projection evaluated at the current endpoint. For each raw
squared history tail, `dot D_h=rho||h-h*||_2^2`, and likewise for `b`.
Consequently the integral of the absolute defect is bounded by twice the
product of the forward and backward `L2` tails, with sample normalization
`1/(mn)`.

Define the forward derivative energy

\[
 Z_\ell=\frac1{mn}\sum_a\int_0^\tau
                    \|\partial_\xi h_{\ell,a}\|_2^2d\xi.
\]

The forward chain rule, bounded slopes, (11), and the weighted Legendre
tail inequality give the stopped bounds

\[
 Z_\ell\le CY^3,\qquad
 \int e_E\,dt\le CY^3/P,\qquad
 \|\Gamma_w(t)-\Gamma_w(0)\|_{\rm op}\le CY^2.
 \tag{12}
\]

Here `e_E=sum_(l>=2)||E_l||_F`. The derivative-energy recursion is recorded
explicitly in `ACTIVATION_SMALL_LABEL_ROUTE.md`; it multiplies the tanh
recursion only by the fixed slope and feature bounds in (10). In particular
it uses no bound on `phi''`.

The endpoint Legendre kernel has `L1` norm at most `C sqrt(P)`, while a
continuous `H1` history has endpoint error at most
`C sqrt(tau/P)||h'||_L2`. Apply these to the backward and forward histories
in (11). Their powers of `P` cancel and (12) gives

\[
 e_E(t)\le CY^{5/2}\rho(t),\qquad
 \|JE(t)\|_m\le CY^{7/2}\rho(t).
 \tag{13}
\]

The extra factor `Y` comes from the backward response in each hidden-block
output differential; unbounded features contribute only `M_(l-1)`.
The exact residual equation is
`dot r=-2Gamma r+JE`, with `Gamma>=Gamma_w`. Shrink `Y_*` so that the
Gram drift in (12) is below `lambda/2` and the forcing coefficient in (13)
is below `lambda/2`. Then `dot rho<=-lambda rho/2` on the stopped interval.
Its integrated activity is at most `2QY/lambda=S/2`, a strict cap margin.
The matrix and first-layer margins above exclude all tube exits.
At fixed `n,P` the raw moment ODE is locally Lipschitz, with bounded
coordinates on the cap; continuation proves (5) for every order.
Physical velocity is integrable, so parameters converge and their residual
limits vanish. The same proof with `E=0` treats dense flow.

## 3. Curvature changes the order requirement, not the activity argument

All preactivation coordinates lie in `[-R sqrt(n),R sqrt(n)]`. A locally
Lipschitz derivative composed with an absolutely continuous coordinate is
absolutely continuous and its time derivative is bounded almost everywhere
by `ell_n` times the coordinate speed. Thus no classical second derivative
at every point is needed.

From (13) and the canonical updates,
`||dot z_(l,a)||_2/sqrt(n)<=CY rho`. Full backward carriers have ordinary
supremum norm at most their Euclidean norm, hence at most `C sqrt(n)Y`.
Differentiating backpropagation through fixed depth therefore gives

\[
 \max_{\ell,a}\frac{\|\dot\delta_{\ell,a}\|_2}{\sqrt n}
           \le C(1+\chi_n)\rho.
 \tag{14}
\]

The only gate multiplication loss is
`ell_n * sqrt(n)Y * CYrho`. No bounded activation-coordinate assumption
is used. Moreover `||dot r||_m<=C rho`, so the normalized residual direction
`c=r/rho` obeys `||dot c||_m<=C`. It follows that

\[
 \frac1{mn}\sum_a\int_0^T\|\dot b_{\ell,a}\|_2^2dt
       \le CY^2(T+1+\chi_n^2).
 \tag{15}
\]

To handle the infinite physical interval, subtract the initial backward
prefix jump, of RMS at most `CB_0`, and freeze the continuous remainder
after time `T`. The remaining clock mass is at most `rho(T)/kappa` by
(5). The weighted Legendre derivative energy of the frozen history is
bounded by (15), since `tau(t)-tau(s)<=rho(s)/kappa` cancels the inverse
clock speed in the change of variables. Choose
`T=(2/kappa)log(e+P)`. The resulting backward and forward tails are

\[
 Q_b\le C\left\{\frac{B_0}{\sqrt P}
       +\frac{Y\sqrt{1+\chi_n^2+\log(e+P)}}P\right\},\qquad
 Q_h\le CY^{3/2}/P.
 \tag{16}
\]

Their product bounds `integral_0^infinity e_E`, giving the bracket in (7).
The prefix step bound uses a ramp of width `tau/P`, whose direct `L2`
error and projected derivative error are both `O(P^-1/2)`.

For feedback, split parameter differences into hidden/first-layer error
`x` and readout error `z`. Forward differences are at most `Cx` in RMS.
Subtracting backpropagation using the full dense carrier in each gate
difference yields

\[
 \max_{\ell,a}\frac{\|\widehat\delta_{\ell,a}-\delta_{\ell,a,D}\|_2}
                         {\sqrt n}
 \le C\{z+Yx+\ell_n\sqrt nYx\}.
 \tag{17}
\]

The positive closure Gram damps the prediction discrepancy. Integrating
its exact equation first, then inserting that bound into the parameter
equations, gives

\[
 d_n(t)\le C\int_0^t e_E(s)ds+
 C(1+\ell_n\sqrt nY)\int_0^t\rho_D(s)d_n(s)ds.
 \tag{18}
\]

Since `integral rho_D<=CY`, Gronwall in dense activity gives the factor
`exp(CY+C chi_n)` in (7). This proof does not assume width-independent
feedback stability; it pays for the displayed gate modulus and then
absorbs that factor with the joint order choice.

For (8), multiply (7) by `P`, use `Y<=1`, `B_0<=Y`, and
`a chi_n<=log(P)/2`. The remaining factors are bounded by constants times
`1` and `(1+log(e+P))/sqrt(P)`, uniformly for `P>=1`. If `B_0=0`, the
first term is absent and the order in (9) suffices. The complete
coefficient-by-coefficient comparison is in `ACTIVATION_LOCAL_MODULUS.md`.

## 4. When canonical Gaussian initialization supplies the assumptions

The deterministic theorem assumes an initial feature-Gram gap; this is
not automatically true for every activation and dataset. A broad sufficient
condition is:

- inputs are fixed, nonzero, and pairwise nonproportional;
- the first activation is continuous, globally Lipschitz and nonpolynomial
  (equivalently nonaffine within the globally Lipschitz class);
- later activations are continuous, globally Lipschitz and nonconstant.

Under independent canonical Gaussian initialization, the initial top
feature Gram converges in probability to a positive-definite matrix.
The initial operator and first-preactivation RMS bounds also hold with
probability tending to one, and the canonical stored readout has
`B_0=O_probability(1/n)`. Thus, for each fixed `0<Y<=Y_*`, (4) holds on
events of probability tending to one, and all order/time claims hold
simultaneously on those events.

Here is why the richness condition is sufficient. A first-layer Gram
dependence would imply `sum_a c_a phi_1(w dot x_a)=0` for every `w`, by
continuity and full support of the Gaussian law. For a nonzero coefficient
`c_a`, take directional differences perpendicular to every other input,
one at a time. Pairwise nonproportionality lets each such direction have
nonzero pairing with `x_a`. All other ridges are annihilated, so every
mixed `(m-1)`-st difference of `phi_1` vanishes. Mollification and the
one-variable derivative test then force `phi_1` to be a polynomial of
degree at most `m-2`, a contradiction. The one-sample case follows directly
from nonzero input and a nonzero activation.

At every later layer the preactivation Gaussian has full covariance.
If `sum_a c_a phi_l(z_a)` vanished everywhere, varying one coordinate
while holding the others fixed would force every coefficient to vanish
because `phi_l` is nonconstant. Conditional row averaging and finite fourth
moments from linear growth prove finite-width Gram convergence through
fixed depth. The complete elementary proof is in `ACTIVATION_INITIAL_GRAM.md`.

These are sufficient geometry/richness conditions. If a different activation
or dataset directly satisfies (4), the deterministic theorem still applies.
For example linear first-layer features can satisfy the gap for linearly
independent training inputs, although they cannot supply it for every large
finite dataset. Compatible symmetry subspaces can also be treated when the
predictions and labels are known to remain in that fixed subspace.

## 5. Common activations and the boundary of the result

The following all have bounded slope and globally Lipschitz derivative:
tanh, logistic sigmoid, arctangent, sine, cosine, erf, softsign, softplus,
exact GELU `x Phi(x)`, SiLU `x sigmoid(x)`, and ELU with unit negative
branch coefficient. Fixed gains, offsets, finite linear combinations, and
fixed layer-dependent choices preserve the regularity class. To use the
Gaussian gap corollary, check the resulting first function remains
nonpolynomial and each later function remains nonconstant.

For softplus, the slope is sigmoid and its derivative is bounded by `1/4`.
For GELU, `phi'=Phi+x varphi` and `phi''=(2-x^2)varphi`; both are bounded.
For SiLU, `phi'=sigmoid+x sigmoid'` and
`phi''=2 sigmoid'+x sigmoid''`; exponential decay of the sigmoid derivatives
at both ends bounds these expressions. Unit-coefficient ELU has derivative
`exp(x)` for negative `x` and `1` for nonnegative `x`: it is Lipschitz
despite the jump in the second derivative. Softsign has derivative
`(1+abs(x))^-2`, also Lipschitz. These examples require no analytic activation
assumption in either the tracking or Gaussian-Gram argument.

For globally Lipschitz derivatives, `ell_n<=H` uniformly, so the original
small-label tanh joint scaling is preserved, up to activation-dependent
constants: `log(P)>=C sqrt(n)Y^2` suffices. With only local Lipschitz
derivative the more general modulus in (6) is necessary in this proof.
For instance `phi(x)=integral_0^x sin(u^2)du` has bounded slope and local
derivative Lipschitz constant at most `2R sqrt(n)` on the theorem's range;
the sufficient exponent is then `C nY^2`.

Exact ReLU, leaky ReLU, and standard SELU have a derivative jump. They are
outside (1). Their initial Gaussian Grams may satisfy the nondegeneracy
lemma, but that alone does not prove uniqueness of the nonsmooth closure or
the backward-history regularity required for (7). Smooth approximations
are covered with their actual curvature constants; this is not a theorem
for the nonsmooth limit.

Nor does arbitrary `C^{1,1}_loc` without a global slope bound follow from
this argument. That larger class occurs in the paper's fixed-width compact-
time theorem, where derivative bounds on a width-dependent compact set
are sufficient. The new all-time theorem instead needs width-independent
feature and backward RMS bounds before establishing the activity cap.
Polynomial or faster growth would require an additional moment/continuation
argument. No impossibility of such a future extension is claimed.

## 6. Prediction interpretation

If the initial first-layer Frobenius norm divided by `sqrt(n)` is uniformly
bounded (as it is with high probability under canonical Gaussian
initialization), the activity bound keeps it bounded for all time. On any
fixed bounded test-input set, linear growth and bounded slopes then give
uniform test feature RMS and prediction-difference bounds. Consequently
the joint `C/P` estimate also holds uniformly over that test set and all
time, with a constant depending on its radius. Integration gives the same
order for RMS discrepancy under any probability test measure on that set.
The reverse triangle inequality bounds the difference of the two test
RMSEs to any square-integrable target. These are comparisons to the dense
network's learned predictor, not a claim that either predictor's population
risk is itself small.
