# A finite-order complex Gaussian correction bound

2026-10-07. Lead-author conditional lemma in the polynomial-width
continuation. This removes the need to absorb the complex-minus-real
Gaussian correction by sending width to infinity at a fixed moment order.
It does not quantify the local finite-neuron insertion theorem or establish
the full decoder's sufficient width. No experiment or promotion is involved.

## Scope and setup

Keep the model, data, activations, labels and training dynamics in
POLYNOMIAL_SOURCE_WIDTH.md unchanged. In particular, \(n\) is width,

\[
 \lambda=\gamma/m>0,\qquad Y=\|y\|_2/\sqrt m>0,\qquad
 S=16Y/\lambda\le S_*^{\rm src},\qquad \ell=\log(en).
\]

The source small-label allowance is its full original intersection, not a
new restriction. The strip-derivative envelope is the same \(\beta\ge10\)
as in that note, with \(L\ge2\). The zero-label flow is stationary.

This note uses only the current-study radius/source accounting and the
authorized integrated UNBOUNDED_COMPRESSOR_BRIDGE.md, especially its
Sections 5--8. The latter proves the stopped real Gaussian references and
displays the complex derivative recurrence. Its unquantified local
insertion constants are not treated as proved polynomial constants.

Let \(p\ge1\) be the integer moment order used to remove a joint budget.
For this lemma choose the physical complex-time half-width

\[
 r_t=\frac{c}{\sqrt\ell},\qquad
 c=\frac{1}{p\beta^{100L}(1+\lambda)}.                 \tag{1}
\]

Compared with the deterministic radius repair, the only additional
shrinkage is the explicit factor \(p\). The real source interval remains
\([0,32\ell/\lambda]\). All contour and pole margins of that repair
improve. Width is not required to be exponential in \(p\), \(m/\gamma\)
or an activation bound to make the Gaussian correction small.

The precise conditional conclusion is as follows. Condition on an
autonomous same-layer cavity, stopped or clamped by its own rules. Suppose
its real and complex coefficient paths satisfy the stopped derivative
bounds specified below. Let \(X\) be the supremum of the absolute
complex-minus-real pairing with one omitted Gaussian root, with a backward
pairing divided by \(S\). The same assertion holds for the sample RMS of
these suprema. Then, simultaneously for every \(n\ge1\),

\[
 \left(\mathbb E[e^{apX}\mid\text{cavity}]\right)^{1/p}
 \le \exp(\beta^{-10L}),\qquad 0\le a\le8.             \tag{2}
\]

The conditional hypothesis is substantive: a finite-width local insertion
and cavity-transfer event is still needed in the full proof. No conditioning
on full-network survival is allowed in (2).

## 1. An elementary rectangular Gaussian-process bound

Let \(G\) be a standard real Gaussian vector, and let \(b_z\) be a
deterministic complex vector indexed by a rectangle whose sides are at
most \(H\). Suppose

\[
 \sup_z\|b_z\|_2\le D,\qquad
 \|b_z-b_{z'}\|_2\le K\|z-z'\|_2.
\]

For \(X=\sup_z|G^\top b_z|\), put

\[
 M=256D\sqrt{\log(e+HK/D)}.                            \tag{3}
\]

Zero \(D\) is interpreted as the identically zero process. For positive
\(D\),

\[
 \mathbb EX\le M,\qquad
 \mathbb E e^{uX}\le\exp(uM+2u^2D^2),\quad u\ge0.     \tag{4}
\]

Here is a direct derivation, including the entropy dependence. First use
real coefficients. Cover the rectangle at mesh sizes proportional to
\(D2^{-j}/K\), starting at \(j=0\), and connect each point at level
\(j\) to a nearest point at level \(j-1\). One may choose at most
\(4(1+HK/D)^2 4^j\) mesh points. The connected increment standard
deviation is at most \(3D2^{-j}\), after harmlessly refining the mesh
by an absolute factor. For \(N\) centered Gaussians of standard deviation
at most \(s\), the exponential moment and union bound give

\[
 \mathbb E\max_{i\le N}|Z_i|\le s\sqrt{2\log(2N)}.
\]

At the initial mesh the standard deviation is at most \(D\). Summing
the connected increment bounds uses
\(\sum_{j\ge1}2^{-j}=1\) and
\(\sum_{j\ge1}2^{-j}\sqrt j\le2\). It bounds the expected real
absolute supremum by
\(128D\sqrt{\log(e+HK/D)}\). The numerical factor 128 also
covers the initial mesh and a rectangle smaller than the first mesh.
Continuity follows from the finite-dimensional Lipschitz coefficient
map, so limits of the nested meshes recover the supremum.

Apply this estimate separately to the real and imaginary parts and use
\(|G^\top b|\le|G^\top\Re b|+|G^\top\Im b|\). Their sum is
at most \(2D\)-Lipschitz in \(G\). Gaussian Lipschitz concentration
(derived by the Gaussian semigroup calculation in
EXPLICIT_FITTING_WIDTH.md, Section 2) gives the moment bound in (4).
Alternatively the true complex absolute supremum is already at most
\(\sqrt2D\)-Lipschitz; the weaker \(2D\) bound is sufficient.

If \(X_a\) are these suprema for different samples but the same root,
with the same \(D,K,H\), their RMS
\(\bar X=(m^{-1}\sum_aX_a^2)^{1/2}\) is also at most
\(2D\)-Lipschitz. Since \(\operatorname{Var}(X_a)\le4D^2\),

\[
 \mathbb E\bar X\le(M^2+4D^2)^{1/2}\le M+2D,
 \qquad
 \mathbb E e^{u\bar X}
       \le\exp(u(M+2D)+2u^2D^2).                      \tag{5}
\]

No independence between samples is used. The same proof works for a root
with covariance \(I/n\) when coefficient norms are the normalized
Euclidean norms \(\|\cdot\|_2/\sqrt n\).

## 2. The stopped source gives the required coefficient norms

The source's derivative estimate contains its joint-budget coefficient
\(\eta>0\). The unchanged label allowance gives
\(S^2/\eta\le1\). Retaining the exact logarithm of its fixed budget
when necessary, or taking the weaker original gate
\(\ell\ge\max(e^2,2048e^2L)\), yields the displayed source estimate

\[
 \|\partial_t\delta_a^{(j)}\|_{2,n}
 \le J\rho\,[1+(S^2/\eta)\log(e+\ell)],\qquad
 \rho=\|f-y\|_2/\sqrt m.                             \tag{6}
\]

The weaker gate just mentioned is at most \(n\ge\exp(CL)\) with
an absolute \(C\), hence a fixed power of \(\beta^L\). It is not an
exponential-in-gap or exponential-in-sample condition. To claim (2) for
all widths one uses the version retaining \(\log(2\mathcal B)\),
where \(\mathcal B=1024e^2L\): replace the bracket in (6) by

\[
 A=1+\frac{S^2}{\eta}
          [4+\log(2\mathcal B)+\log\ell].             \tag{7}
\]

Indeed the interpolation exponent
\(\max\{4,\log(2\mathcal B\ell)\}\) is no greater than the
bracketed expression in (7), and
\((2\mathcal B\ell)^{1/\max\{4,\log(2\mathcal B\ell)\}}
\le e\). The original restriction
\(S^2\Lambda/\eta\le1\),
\(\Lambda=\log(e+\mathcal B)+\log(1/\eta)\), gives

\[
 A\le8[1+\log(e+\ell)].                              \tag{8}
\]

Here \(\eta\le1\), \(\Lambda\ge1\), and
\(\log(2\mathcal B)\le\Lambda+\log2\) suffice. Thus no
depth-dependent factor needs to be hidden in the logarithmic bracket.

For clarity the required derivative coefficient can be bounded explicitly.
The finite-query response envelope is \(U_{\rm fin}\le\beta^{72L}\);
the forward-response coefficients satisfy the same larger bound.
The source recursion is

\[
 J_L=2sH_L+4etN_*,\qquad
 J_j=10sJ_{j+1}+2s^3k_{j+1}^2H_j+4etN_*,
\]

with \(s,t\le\beta\), \(H_j\le\beta^{3L}\),
\(k_j\le\beta^{5L}\), and \(N_*\le\beta^{72L}\).
Each forcing term and \(J_L\) are at most \(\beta^{75L}\).
Summing at most \(L\) terms, each multiplied by at most
\((10s)^{L-1}\le\beta^{2L}\), gives

\[
 \max_jJ_j\le\beta^{78L}.
\]

Enlarging to \(J=\beta^{80L}\) also bounds the normalized forward
coefficient derivatives, their difference from the real anchor, and the
absolute numerical factors below. Derivatives on the short complex pieces
use \(\rho\le2Y\), exactly as in the radius repair.

For each point \(z\) in the rectangle, subtract the coefficient at its
nearest real anchor in \([0,32\ell/\lambda]\). The anchor map is
Lipschitz, including at the two endpoints. Integrating at most two short
pieces and differentiating this difference gives the following safe bounds
for backward coefficients divided by \(S\), and also for forward ones:

\[
 D=\frac{\lambda cJ A}{\sqrt\ell},\qquad
 K=\lambda J A,\qquad
 H=\frac{64\ell}{\lambda}+\frac{4c}{\sqrt\ell}.       \tag{9}
\]

The factors in (9) dominate \(4Y/S=\lambda/4\) from the backward
derivative and \(4YS=\lambda S^2/4\le\lambda/4\) from the forward
one. The same bounds hold after a cavity's own Lipschitz clamping, when
the stipulated stopped coefficient derivative bounds hold. Failed own
initializations are assigned zero reference paths before the Gaussian root
is integrated, as in the source proof.

## 3. No exponential width is needed at the chosen moment order

Put \(r=\lambda^{-1}\) only within this calculation. Substitution of
(1) into (9) gives

\[
 D\le\frac{\beta^{-20L}}{p(1+r)}\frac A{\sqrt\ell},
 \qquad
 \frac{HK}{D}=64p\beta^{100L}(1+r)\ell^{3/2}+4.        \tag{10}
\]

For \(u=\log\ell\ge0\), elementary differentiation gives

\[
 (2+u)e^{-u/2}\le2,\qquad
 (2+u)^{3/2}e^{-u/2}\le4.
\]

Since \(\log(e+\ell)\le2+\log\ell\), (8) implies
\(A\le16\log(e+\ell)\). In particular

\[
 D\le\frac{32\beta^{-20L}}p.                         \tag{11}
\]

The logarithm in (3) is bounded by

\[
 6+100L\log\beta+\log p+\log(1+r)+2\log(e+\ell).
\]

Use the subadditivity of the square root, the preceding two elementary
bounds, \(\sqrt{\log p}/p\le1\), and
\(\sqrt{\log(1+r)}/(1+r)\le1\). Also
\(\sqrt{100L\log\beta}\le\beta^{2L}\) for
\(\beta\ge10,L\ge2\). These give the deliberately loose absolute
bound

\[
 M+2D\le2^{16}\beta^{-18L}.                           \tag{12}
\]

For example, before the factor \(256\) in (3), the bracket from these
five square-root terms is bounded by
\(32(\sqrt6+\beta^{2L}+1+1)+64\sqrt2\), all multiplied by
\(\beta^{-20L}\). This is below \(2^{16}\beta^{-18L}\)
after restoring that factor and \(2D\).

Applying (4) or (5) with \(u=ap\), and taking the \(p\)-th root, yields

\[
 \left(\mathbb E e^{apX}\right)^{1/p}
 \le\exp\{a2^{16}\beta^{-18L}
                +2^{11}a^2\beta^{-40L}/p\}
 \le\exp(\beta^{-10L}),\qquad 0\le a\le8.            \tag{13}
\]

The final inequality follows from \(\beta\ge10,L\ge2\): after
division by \(\beta^{-10L}\), its two terms are at most
\(2^{19}10^{-16}\) and \(2^{17}10^{-60}\), respectively.
This proves (2), including the sample RMS version. All parameter factors
in this calculation are displayed. In particular the long physical time
interval contributes only \(\log(1+r)\), multiplied by
\((1+r)^{-1}\); it does not require exponentially large width.

## 4. What changes in the algorithm, and what is still missing

The radius repair without \(p\) left the old Taylor step unchanged. The
finite-order refinement here does not make that same claim. Its normalized
radius is

\[
 r_\tau=\frac1{p\beta^{100L}(1+m/\gamma)\sqrt\ell}.
\]

Taking the old certified step divided by \(p\) is sufficient. The number
of patches is at most \(p\) times its previous ceiling; the logarithm in
the local degree gains only \(O(\log p)\). These are explicit costs,
not a free change of radius. At

\[
 p=\max\left\{1,
 \left\lceil\frac{\log(4emL/\delta)}
                       {\log(64e^2)}\right\rceil\right\},
\]

they introduce logarithmic factors in sample count and confidence, not a
new power of \(\log n\) at fixed problem parameters. The exact final
resource table must be recomposed if this route is used. This conditional
lemma alone does not supersede the current checked table.

The remaining requirements are explicit finite-width local insertion,
common-cavity comparison and their exceptional probabilities. In
particular the Gaussian correction bound proved here does not imply that
the random cavity coefficient paths obey (9) with the required probability.
It proves the finite-order moment once those stopped-path estimates are
available. Nor does it address the separate passive-decoder bias and
dense-error absorption condition.

The displayed entropy estimate, derivative recurrence, parameter
cancellations, confidence-order moment bound and extra patch factor are
author-checked derivations. The bounded independent reconstruction in
FINITE_COMPLEX_MOMENT_GATE_CHECK.md checks this conditional lemma, not
the full source composition. Its first frozen version was subsequently
changed only to restore inline math delimiters and add this status link.
