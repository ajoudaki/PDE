# Fixed-depth extension of the near-quarter memory-order result

2026-10-03. Continuation of the same-width order investigation.
**Positive result, internally reconstructed.** The same-width,
near-quarter memory-order theorem extends to every fixed depth and to
smooth activations with bounded first three derivatives, including
unbounded activation values. Complete local and probability checks are
linked below. These are collaborative study research results, not
promotion into the maintained book or an edit to the manuscript.

## 1. Model and scope

Fix an integer number of hidden layers \(L\ge2\), a finite training
set \((x_a,y_a)_{a=1}^m\), and input dimension \(d\), independently
of width. The dense network has width \(n\) in every hidden layer:
\[
 z^{(1)}(x)=W^{(1)}x/\sqrt d,\qquad
 z^{(\ell)}(x)=W^{(\ell)}h^{(\ell-1)}(x),\qquad
 h^{(\ell)}(x)=\phi_\ell(z^{(\ell)}(x)),\qquad
 f(x)=w^\top h^{(L)}(x)/n.
\]
It has no biases. The initialization has independent \(N(0,1)\)
entries in \(W_0^{(1)}\), independent \(N(0,1/n)\) entries in
the other hidden matrices, and \(w_0=0\). Training is the paper's
squared-loss gradient flow with block mobilities
\((n,1,\ldots,1,n)\).

The comparison uses this dense network and the manuscript's actual
order-\(q\) autonomous Legendre response-memory closure, at the same
width and with the same initialization. Its clock remains
\[
 \dot\tau=\widehat\rho,\qquad \tau(0)=1,\qquad
 \widehat\rho^2=\frac1m\sum_a
       (\widehat f_{n,q}(t,x_a)-y_a)^2.
\]
The fixed initialized mixing matrices remain in the closure. No clipping,
frozen features, dense reference driving term, or altered clock enters
either trained algorithm. The dense histories used in the proof are
comparison functions only.

The activation condition is
\[
 \phi_\ell\in C^3(\mathbb R),\qquad
 \max_{1\le j\le3}\|\phi_\ell^{(j)}\|_\infty<\infty.
 \tag{1}
\]
Activation values may grow linearly; no bound on
\(\|\phi_\ell\|_\infty\) is imposed. For the automatic initialization
gaps below, use nonaffine activations. Examples include tanh, logistic
sigmoid, arctan, erf, sine, cosine, \(e^{-s^2}\), **softplus, GELU
and SiLU**. Monotonicity is unnecessary. The derivative conditions do
not include ReLU or leaky ReLU.

The extension beyond bounded values is proved in
[UNBOUNDED_ACTIVATION_CANDIDATE.md](UNBOUNDED_ACTIVATION_CANDIDATE.md);
that historical filename is retained, but its obligations are now
completed and checked.

The label RMS is
\(Y=(m^{-1}\sum_a y_a^2)^{1/2}\). It must be below a fixed positive
threshold depending on the data, depth, and activation bounds.
This threshold is independent of width, memory order, and training time.
For \(Y=0\), both paths are stationary and coincide exactly.

## 2. Data and initialization

The base comparison uses a positive limiting initialized feature Gram.
For the following fixed sphere datasets, it follows from the activation
assumptions and the exact data symmetries; it is not a new trajectory
hypothesis. Let \(\|x_a\|=\sqrt d\).

- With the same nonaffine activation satisfying (1) at every layer,
  distinct inputs that are not antipodal have a positive initial feature
  Gram already after the first layer.
- If that activation is odd, antipodal pairs require opposite labels.
  If it is even, they require equal labels. The exact signed or unsigned
  quotient preserves both training equations and the original clock.
- If that activation is neither even nor odd, any distinct sphere
  inputs, including antipodal pairs, have a positive feature Gram by
  the second hidden layer. The first Gram need not be positive definite.
  This case includes sigmoid, softplus, GELU and SiLU.
- Duplicate inputs require equal labels and can be combined with their
  fixed sample weights.

The complete proofs and layer-dependent variants are in
[ACTIVATION_EXTENSION_ROUTE.md](ACTIVATION_EXTENSION_ROUTE.md), checked in
[ACTIVATION_EXTENSION_CHECK.md](ACTIVATION_EXTENSION_CHECK.md).
No orthogonality is used. Constants need not stay bounded as distinct
data points approach a degeneracy. For arbitrary layer-dependent
activations outside those proved sufficient cases, retain the explicit
initial feature-Gram condition.

## 3. Quantitative conclusion

There are events \(\Omega_n\), with \(\Pr(\Omega_n)\to1\), on which
there are fixed
constants \(C_\mu,K\), independent of width, order and time, such that
simultaneously for every positive integer \(q\),
\[
 \left(\int\sup_{t\ge0}
   |\widehat f_{n,q}(t,x)-f_{n,D}(t,x)|^2\,d\mu(x)\right)^{1/2}
 \le C_\mu e^{K\sqrt{\log(e+n)}}
                 \frac{\sqrt{\log(e+q)}}{q^2}.
 \tag{2}
\]
Here \(\mu\) is any fixed query law with finite second moment.
The same event also bounds the normalized parameter distance
\[
 \sup_{t\ge0}\left[
 \frac{\|\widehat W^{(1)}-W_D^{(1)}\|_F}{\sqrt n}
 +\sum_{\ell=2}^L\|\widehat W^{(\ell)}-W_D^{(\ell)}\|_F
 +\frac{\|\widehat w-w_D\|_2}{\sqrt n}\right]
\]
by the right side of (2) with a fixed constant in place of \(C_\mu\),
and controls uniform absolute prediction error on any fixed bounded
query set. Here the closure's hidden matrices are its reconstructed
physical matrices, not independently trained variables.

Consequently, a fixed \(a>K/2\) and
\[
 q_n=\left\lceil n^{1/4}
                  e^{a\sqrt{\log(e+n)}}\right\rceil
       =n^{1/4+o(1)}=o(n)
 \tag{3}
\]
give a strict \(C_\mu/\sqrt n\) bound. Indeed the residual factor
is at most
\(C\sqrt{\log(e+n)}e^{-(2a-K)\sqrt{\log(e+n)}}\), which is
bounded independently of \(n\). The physical-time supremum includes
the fitted endpoint, since both paths converge by the preceding
small-label physical estimates.

At fixed confidence \(1-\delta\), the conclusion holds for
every \(n\ge N_\delta\). This means width-independent constants at
each width, not one event for infinitely many independent initializations.
The depth is arbitrary but fixed; neither the constants nor the
small-label threshold are asserted uniform as \(L\) grows.

## 4. Why greater depth is a substantive extension

Removing an interior neuron changes two parts of training: its activation
drives the layer above, and its backward response changes the updates
below. A complete deletion argument must retain both effects. Conditional
on the retained network, the neuron's incoming initialized row and
outgoing initialized column are independent Gaussian vectors. Linear
reinsertion produces quadratic terms with a normalized trace and mixed
bilinear terms with zero conditional mean. Uniform control estimates are
needed before the actual adaptive histories can be substituted.

The trace calculation uses the finite-rank structure of the
full-depth Hessian. Its large terms are local carrier diagonals between
bounded forward-response maps. Their averaged Schatten bounds depend on
the empirical carrier budget rather than its largest coordinate. Two
additional response factors appear at the trace endpoints; accounting
for both gives the bound \(CS+CS^3B\) under budget \(B\), where
\(S\) is a fixed multiple of \(Y\). The Gaussian reference supremum
has exponential moments growing only subpolynomially in \(B\).
The complete finite-block moment argument closes that budget by choosing
it first and then the label threshold. It is a proved event of
probability tending to one, not an additional moment assumption.

For unbounded activation values, the proof controls forward
preactivations and backward carriers together. On a temporary joint
budget, let \(Z_i\) be a neuron's running maximum preactivation and
\(U_i\) its running maximum backward carrier divided by \(S\).
After making \(S^2B\le1\), reinsertion gives
\[
 U_i\le G_{{\rm back},i}+C(1+Z_i)+o(1),\qquad
 Z_i\le G_{{\rm forward},i}+CS^2U_i+o(1).
\]
The two \(G\)'s are Gaussian reference-path suprema with controlled
exponential moments. The coefficient on the return from backward to
forward activity is \(CS^2\). Small labels let it be absorbed, bounding
both quantities by those Gaussian references. At the top layer the
readout obeys \(U_i\le C(1+Z_i)\), and the same absorption applies.
The local proof explicitly includes the omitted neuron's prediction in
both the retained residual gradient and the reverse force.

This yields the actual dense-network bound
\[
 \sup_{t\ge0}\max_{a,\ell,i}|k_{D,a,i}^{(\ell)}(t)|
 \le CS\sqrt{\log(e+n)}
\]
on events of probability tending to one. The finite-width forward
preactivation maximum has the corresponding
\(C\sqrt{\log(e+n)}\) bound. These are conclusions for the original
unclipped trajectory, not assumptions on a population limit.

The deterministic comparison needs only the resulting actual dense
carrier maximum. It records a dense backward response in the closure's
own clock, compares it to the closure's backward response, and absorbs
the resulting discrepancy for sufficiently large \(q\). This keeps
the \(q^{-2}\) projection order at every fixed depth.

For fixed \(L,m,d\), the moving state at (3) has
\(2(L-1)mnq_n+n(d+1)+O(1)=n^{5/4+o(1)}\) coordinates.
The initialized hidden mixing matrices are still stored and used.

These are same-width closure-to-dense statements. They do not establish
a strict root-width dense-to-population rate, remove the small-label
assumption, prove a pure \(O(n^{1/4})\) memory order, or establish
optimality. The manuscript and maintained book are unchanged.

## 5. Proof and check record

- [DEPTH_TRACKING_ROUTE.md](DEPTH_TRACKING_ROUTE.md) and
  [DEPTH_TRACKING_CHECK.md](DEPTH_TRACKING_CHECK.md): complete deterministic
  implication from an actual dense carrier envelope, including the
  simultaneous-in-order corollary.
- [DEPTH_RESPONSE_MODULUS.md](DEPTH_RESPONSE_MODULUS.md) and
  [DEPTH_RESPONSE_MODULUS_CHECK.md](DEPTH_RESPONSE_MODULUS_CHECK.md):
  conditional time modulus, Gaussian entropy, and endpoint trace.
- [ACTIVATION_EXTENSION_ROUTE.md](ACTIVATION_EXTENSION_ROUTE.md) and its
  check linked above: initialization gaps and exact parity quotients.
- [DEPTH_CAVITY_ROUTE.md](DEPTH_CAVITY_ROUTE.md) and
  [DEPTH_CAVITY_PROBABILITY_CHECK.md](DEPTH_CAVITY_PROBABILITY_CHECK.md):
  exact bidirectional finite deletion and completed carrier-budget
  probability argument for bounded activation values.
- [DEPTH_INSERTION_CHECK.md](DEPTH_INSERTION_CHECK.md): coordinator's
  complete local reconstruction, including the linear-growth extension.
- [UNBOUNDED_ACTIVATION_CANDIDATE.md](UNBOUNDED_ACTIVATION_CANDIDATE.md),
  [UNBOUNDED_INSERTION_CHECK.md](UNBOUNDED_INSERTION_CHECK.md), and
  [UNBOUNDED_ACTIVATION_CHECK.md](UNBOUNDED_ACTIVATION_CHECK.md):
  completed joint-budget extension, including the top-layer residual
  offset, both actual-amplitude traces, and the full probability chain.

All checks are internal collaborative research checks, not promotion
reviews. No numerical experiment was used.

The principal source versions are:

| Source | SHA-256 |
|---|---|
| DEPTH_TRACKING_ROUTE.md | f06f6c1acc75c1841f7898dcccb3a88a1f8b7724c53f8dbbe688f46305162e0c |
| DEPTH_CAVITY_ROUTE.md | e8f9f43c137a9c74b751cbd2e54cf5a2b13f090c560d912b4b17994c53bc1478 |
| DEPTH_RESPONSE_MODULUS.md | e32e3608e5a02d6f9aefb88cf77890f9110a8d65bede6faedf2f215d84dc6d24 |
| UNBOUNDED_ACTIVATION_CANDIDATE.md | e939e971d7a9e1b884b42d73d3ce65f5b1f548d9e25ab9cfe76c0502aa591713 |
| UNBOUNDED_INSERTION_CHECK.md | bec5707fccc99597570ce51c94d3a487fd0b1ede14578617275cb708fdd95578 |
| ACTIVATION_EXTENSION_ROUTE.md | 82f3d3a747b2a48a6addbff5cee904527b058b392bd2fde809a83bd0878d3b7c |
