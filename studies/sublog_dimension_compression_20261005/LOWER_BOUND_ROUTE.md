# Lower-bound route: analytic widths versus reachable trained trajectories

## Verdict

**Conditional theorem.** A rigorous joint time--sphere nonlinear-width
argument gives a retained-coordinate lower bound with logarithmic exponent
proportional to (d). For a fixed analytic time radius and a fixed analytic
spherical radius, the lower bound is

\[
 P\gtrsim [\log(1/\varepsilon)]^d,
\]

where (P) counts every retained numerical coordinate. If one inserts the
shrinking time and query radii proved for the source fields in
`UNBOUNDED_COMPRESSOR_BRIDGE.md`, the corresponding ambient analytic-class
count is

\[
 P\gtrsim [\log(en)]^{3d/2+1}
\]

at the requested accuracy. These are genuine lower bounds for stable
representations of the stated analytic function classes.

They are **not** lower bounds for the reachable canonical trained-network
trajectories. The supplied trajectory-variability theorem proves one scalar
fluctuation direction. It does not prove that reachable trajectories contain
the high-dimensional time--harmonic ball needed by the width argument. An
upper holomorphy bound cannot be inverted into such a reachability statement.
Consequently this route does not prove that the requested
(r(d)=o(d)) compression is impossible under the exact study contract.

The required canonical-notation skill at
`/home/amir/.codex/skills/explain-with-canonical-notation/SKILL.md` was present
but unreadable because of filesystem permissions, including after the
permitted elevated read attempt. The repository notation contract was
followed directly.

## 1. Contract for a stable coordinate representation

Let

\[
 \|F\|_*=
 \sup_{t\in[0,\infty]}\sup_{\|x\|_2=\sqrt d}|F(t,x)|.
\]

A (P)-coordinate autonomous representation stores a vector
(\theta\in\mathbb R^P). It contains all instance-dependent numerical data:
initial state, vector-field coefficients, decoder coefficients, metrics,
dictionaries, and mixers. Instance-dependent coefficients can be regarded as
state coordinates with zero velocity, so this convention does not omit fixed
retained numbers. A dimension-uniform rule generates an autonomous flow
(\Phi_t(\theta)) and a decoder (D), hence the realized trajectory

\[
 \mathcal G(\theta)(t,x)=D(\Phi_t(\theta),x).
\]

Restartability means that the current retained state determines every future
decoded value. Two stability models will be useful.

1. **Topological stability.** On the target family under consideration, the
   encoder (E:F\mapsto\theta) is continuous. No quantitative decoder bound
   is needed for the Borsuk--Ulam lower bound below.
2. **Metric stability.** The codes lie in a bounded cube
   ([-R,R]^P), and
   \[
   \|\mathcal G(\theta)-\mathcal G(\theta')\|_*
   \le \Lambda\|\theta-\theta'\|_\infty .
   \tag{1}
   \]
   A polynomially conditioned representation satisfies
   \(\log(1+R\Lambda/\varepsilon)le C_{\rm stab}
   \log(B/\varepsilon)\), where (B) is the amplitude of the target class.

The second model permits a discontinuous encoder, including discrete
selection, but controls the range and conditioning of the retained code. No
claim is made here that the existing selected-neuron preprocessing has been
proved to satisfy either stability model uniformly. That separate inclusion
is necessary before this can be a no-go theorem for that model class.

## 2. A self-contained joint time--sphere width lower bound

Restricting the complete trajectory norm to one finite time interval can only
weaken it. Rescale that interval to (s\in[0,1]), and use

\[
 \psi_k(s)=\sqrt2\sin(\pi k s),\qquad k\ge1.
\]

The functions (\psi_k) are orthonormal in (L^2[0,1]) and vanish at both
ends, so the perturbations below do not exploit incompatible initial or final
values. For (d\ge2), let
(Y_{\ell,j}), (1\le j\le h_{d,\ell}), be a real orthonormal basis of
degree-(\ell) spherical harmonics on (S^{d-1}), with normalized surface
measure. The number of harmonics through degree (K) is

\[
 D_{d,K}=\sum_{\ell=0}^K h_{d,\ell}
 ={K+d-1\choose d-1}+{K+d-2\choose d-1}.
 \tag{2}
\]

For analytic radii (\tau,\rho>0) and amplitude (B>0), define the spectral
analytic ellipsoid

\[
 \mathcal A_{\tau,\rho}(B)=
 \left\{
 g=\sum_{k\ge1}\sum_{\ell\ge0}\sum_{j=1}^{h_{d,\ell}}
 a_{k\ell j}\psi_kY_{\ell,j}:
 \sum_{k,\ell,j}e^{2(\tau k+\rho\ell)}|a_{k\ell j}|^2\le B^2
 \right\}.
 \tag{3}
\]

Exponential spectral weights imply normal convergence on every strictly
smaller complex time strip and spherical tube: temporal modes grow
exponentially in (k), spherical harmonics grow exponentially in (ell),
and their multiplicities grow only polynomially. Thus (3) is a concrete
analytic trajectory class, not merely a smoothness class.

Fix integers (K_t,K_x\ge1), and let

\[
 M=K_tD_{d,K_x},\qquad
 A=B e^{-\tau K_t-\rho K_x}.
 \tag{4}
\]

The Euclidean coefficient ball of radius (A) in the span of
(\psi_kY_{\ell,j}), (1\le k\le K_t), (0\le\ell\le K_x), lies inside
(\mathcal A_{\tau,\rho}(B)). Orthonormality and
(\|g\|_\infty\ge\|g\|_{L^2}) imply

\[
 \|g_a-g_b\|_\infty\ge\|a-b\|_2.
 \tag{5}
\]

### Topological form

Suppose a (P)-coordinate representation approximates every member of this
coefficient ball with error strictly below (A), and its encoder is
continuous on the ball. Then

\[
 P\ge M.
 \tag{6}
\]

Indeed, if (P<M), Borsuk--Ulam applied to the boundary
(S^{M-1}(A)) gives (a) with (E(a)=E(-a)). Both targets are decoded from
the same code, while their (L^2) distance is (2A). Approximation with
error less than (A) contradicts the triangle inequality. This proof does
not rely on linearity of the representation, decoder regularity, or a bit
model.

### Packing form with a stable decoder

A maximal (4\varepsilon)-separated subset of the coefficient ball has at
least

\[
 \left(\frac{A}{4\varepsilon}\right)^M
 \tag{7}
\]

members when (A>4\varepsilon), by the elementary volume-covering argument
in (\mathbb R^M). If every target is approximated within (\varepsilon),
their decoded codes are separated by at least
(2\varepsilon/\Lambda). A cube ([-R,R]^P) contains at most
((1+R\Lambda/\varepsilon)^P) such separated points. Therefore

\[
 P\ge
 \frac{M\log(A/(4\varepsilon))}
      {\log(1+R\Lambda/\varepsilon)}.
 \tag{8}
\]

This is the precise place where decoder conditioning and code range enter.

Set (H=\log(B/\varepsilon)) and, when (H) is large enough, choose

\[
 K_t=\left\lfloor\frac{H}{4\tau}\right\rfloor,
 \qquad
 K_x=\left\lfloor\frac{H}{4\rho}\right\rfloor.
 \tag{9}
\]

Then (A\ge\sqrt{B\varepsilon}). Both (6) and, under polynomial
conditioning, (8) give

\[
 P\ge c_{d,C_{\rm stab}}
 \frac{[\log(B/\varepsilon)]^d}{\tau\rho^{d-1}}.
 \tag{10}
\]

For example, once the two floor arguments are at least two, (2) yields the
explicit bound

\[
 M\ge
 \frac{H^d}{8^d(d-1)!\,\tau\rho^{d-1}}.
 \tag{11}
\]

For (d=1), (S^0) has two points and no growing angular hierarchy. Using
the two point values with the temporal modes gives
(P\gtrsim\log(B/\varepsilon)/\tau), again exponent (d=1).

At

\[
 \varepsilon_n=\frac{C_{\rm task}}
 {\sqrt n[\log(en)]^{5/2}},
 \tag{12}
\]

fixed (B,\tau,\rho>0) give (H=\tfrac12\log n+O(\log\log n)), hence

\[
 P\gtrsim_{\rm task}[\log(en)]^d.
 \tag{13}
\]

Thus a stable representation of the entire joint analytic ball cannot have
a logarithmic exponent (o(d)).

## 3. Relation to the existing source count

The source bridge proves, after its time change, a Fourier decay radius

\[
 \tau_n\asymp [\log(en)]^{-3/2}
\]

and a spherical harmonic decay radius

\[
 \rho_n\asymp [\log(en)]^{-1/2}.
\]

Substitution into (10), with (H\asymp\log(en)), gives for (d\ge2)

\[
 \frac{H^d}{\tau_n\rho_n^{d-1}}
 \asymp [\log(en)]^{3d/2+1}.
 \tag{14}
\]

For (d=1), it gives (H/\tau_n\asymp[\log(en)]^{5/2}). These are exactly
the logarithmic powers of the source-mode upper count in equations (35)--(36)
of the bridge. This agreement verifies that the joint time--sphere counting
mechanism is dimensionally sharp for the *ambient spectral ellipsoid*.

It does not invert the bridge. The bridge establishes that four particular
dense source families lie in an analytic ball and therefore admit a finite
expansion. It does not establish that those source families range over a ball
of coefficients of dimension (14). Containment supplies an upper width; only
an embedded ball or an entropy lower bound supplies a lower width.

Nor does (14) by itself force the quadratic storage exponent (3d+2). It
forces the indicated number of independent coordinates for the generic
analytic family. Squaring a selected-neuron width is a feature of the current
mixer representation, not a universal lower-bound operation.

## 4. Exact reachability lemma needed for the dense trajectories

The missing bridge can be stated without ambiguity. For the fixed data,
labels, activation and depth in the study, let (f_{n,\omega}) be the
canonical trained predictor from initialization (\omega). Choose the
time--harmonic block in Section 2 and denote its orthogonal projection by
(\Pi_n). A sufficient **reachable harmonic ball lemma** would provide:

1. an integer (M_n=K_{t,n}D_{d,K_{x,n}});
2. a continuous map (u\mapsto\omega_n(u)) from
   (B_2^{M_n}(1)) to legitimate canonical initializations, all remaining
   inside the required fitting and Gram-gap success regime;
3. a scale (b_n>0), a baseline trajectory, and remainders (r_n(u)) such
   that
   \[
   \Pi_n\{f_{n,\omega_n(u)}-f_{n,\omega_n(0)}\}
   =b_n\sum_{\nu=1}^{M_n}u_\nu e_\nu+r_n(u),
   \tag{15}
   \]
   where (e_\nu=\psi_kY_{\ell,j}), and
   \[
   \|r_n(u)-r_n(v)\|_{L^2}
   \le\frac{b_n}{2}\|u-v\|_2
   \quad\text{for all }u,v;
   \tag{16}
   \]
4. (b_n>2\varepsilon_n) for the continuous-encoder conclusion, or enough
   amplitude and probability thickness to combine (7)--(8) with the chosen
   stable-decoder model.

Equations (15)--(16) give

\[
 \|f_{n,\omega_n(u)}-f_{n,\omega_n(v)}\|_*
 \ge\frac{b_n}{2}\|u-v\|_2,
 \tag{17}
\]

so Section 2 applies directly. A spectrally refined version may replace
(b_n) by lower singular values
(b_n e^{-\tau k-\rho\ell}). The resulting dimension is governed by

\[
 \tau k+\rho\ell
 \lesssim\log(b_n/\varepsilon_n).
 \tag{18}
\]

This formula exposes an important scale issue. If (b_n\asymp1), then
(log(b_n/\varepsilon_n)\asymp\log n) and the desired logarithmic-power
lower bound follows. If the only reachable variation has the natural
finite-width size (b_n\asymp n^{-1/2}), then

\[
 \log(b_n/\varepsilon_n)\asymp\log\log n,
\]

so fixed spectral radii yield only a power of (log\log n), not a power of
(log n). A lower bound calibrated merely to finite-width randomness is
therefore not automatically strong enough to match the ambient analytic
width.

For a probabilistic no-go theorem matching the existing high-probability
upper result, the lemma also needs a measure statement: the embedded ball, or
uniformly thick neighborhoods of a large packing within it, must carry enough
Gaussian initialization probability that a compressor cannot discard all
hard points inside its allowed failure probability. Membership in the full
support of the Gaussian law is not enough.

## 5. What the supplied dense-variability theorem proves

`GENERAL_VARIABILITY_LOWER_RESULT.md` proves that, for two independent dense
runs and (m\ge2), with fixed positive probability,

\[
 \|f_n-\widetilde f_n\|_*
 \gtrsim_{\rm task}
 \frac1{\sqrt n[\log(en)]^{5/2}}.
 \tag{19}
\]

The proof obtains a nonzero scalar Gaussian fluctuation of the initial
prediction derivative at at least one deterministic training input and then
transfers it to an actual positive-time prediction. Its quantitative moment
bound is a trace lower bound. It supplies none of the following ingredients
of (15)--(16):

- a common witnessing time for a high-dimensional family;
- independent temporal modes;
- spherical harmonic modes away from the finite training set;
- a lower singular-value bound for a coefficient map;
- a nonlinear remainder bound on a coefficient ball;
- probability thickness of such a ball.

Full input span and the positive feature-Gram gap do not repair this gap. They
control the finite training geometry and fitting, not the harmonic rank of the
query function on the whole sphere. Nonaffinity guarantees genuine feature
motion, but it supplies no quantitative lower tail for harmonic coefficients.
The permitted analytic activation class gives upper coefficient decay only;
it allows nonlinear coefficients to decay extremely rapidly. Adding a lower
spectral-tail assumption would materially strengthen the fixed target scope.

Equation (19) does have one modest representation consequence. A single
initialization-independent, task-only trajectory cannot approximate both
independent runs below a sufficiently small constant multiple of (19): on the
intersection of the two success events, the triangle inequality would
contradict (19). Thus some initialization-dependent retained information is
necessary. This rules out a zero-coordinate surrogate at that scale, but it
does not imply that (P\) grows with (n), let alone with exponent
proportional to (d).

## 6. Why an unrestricted coordinate count is vacuous

Without stability or precision restrictions, cardinality defeats every
coordinate lower bound. A real number can encode an entire trajectory. A
second clock coordinate with \(\dot s=1\), together with a discontinuous
lookup decoder, gives autonomous playback; more elaborate encodings can fold
the clock into the code. This violates the scientific contract but uses only
finitely many real coordinates.

Decoder Lipschitzness alone is also insufficient if the code range is
unbounded. A finite packing can be placed at arbitrarily distant points on
one real axis. As accuracy decreases, an unbounded axis can trace increasingly
long nets of a compact target set. Conversely, a bounded code without decoder
conditioning can hide the same information at arbitrarily fine scales.

The valid alternatives are therefore exactly the mechanisms used above:

- continuity of the encoder on a genuinely reachable coefficient ball, which
  makes topological dimension visible; or
- bounded code range together with a quantitative all-time decoder/flow
  condition, which makes metric entropy visible; or
- an explicit bit/precision model; or
- a direct combinatorial lower bound inside a completely specified
  selected-neuron architecture.

Counting only moving coordinates while omitting instance-dependent metrics,
mixers, dictionaries, or decoder parameters would not meet the study's size
definition.

## 7. Claim boundary and highest-leverage next step

The established statements are:

1. joint time--sphere analytic balls have nonlinear stable width at least
   order \([\log(B/\varepsilon)]^d\) for fixed radii;
2. using the bridge's shrinking radii gives the ambient-class mode count
   \([\log(en)]^{3d/2+1}\);
3. actual dense trajectories exhibit at least one fluctuation at the requested
   scale, so a task-only trajectory is inadequate.

The unresolved statement is the reachable harmonic ball lemma
(15)--(16), with the probability qualification required by the canonical
Gaussian initialization. This is a major logical obstruction, not a technical
remainder estimate. The highest-leverage next action for this lower-bound
route is to study the singular spectrum of the map from initialization
perturbations to the joint time--sphere predictor coefficients and determine
whether it has a uniformly thick block above the requested error. Without
that result, a generic analytic entropy calculation cannot answer the study's
question.
