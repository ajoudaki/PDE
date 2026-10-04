# Explicit architecture dependence in all three compression bounds

2026-10-04. Continuation of the existing sampling study. This note quantifies
the constants in its current label, retained-size and prediction bounds;
it does not change the reference network or the autonomous compressed
optimizer. The component derivations and their reconstruction are linked
below. These are internal study results, not promoted manuscript claims.

The closed expressions here are deliberately conservative. Their purpose
is to leave **no unspecified depth, dimension or geometry dependence in
the three displayed bounds**, rather than optimize numerical dependence on
depth. The sufficiently-large-width threshold remains unquantified and
depends on the fixed architecture, data, labels and confidence.

## 1. Self-contained statement

Fix hidden depth \(L\ge2\), input dimension \(d\ge1\), and \(m\ge1\)
training inputs \(x_a\in\sqrt d\,S^{d-1}\). Put \(v_a=x_a/\sqrt d\).
The reference has width \(n\) in every hidden layer and forward map
\[
z_n^{(1)}(x)=A_nx/\sqrt d,\qquad
z_n^{(\ell)}(x)=W_n^{(\ell)}h_n^{(\ell-1)}(x),\qquad
h_n^{(\ell)}(x)=\phi_\ell(z_n^{(\ell)}(x)),\qquad
f_n(x)=w_n^\top h_n^{(L)}(x)/n.
\]
Initialization is independent Gaussian: entries of \(A_n(0)\) have law
\(N(0,1)\), entries of \(W_n^{(\ell)}(0)\) have law \(N(0,1/n)\),
and \(w_n(0)=0\). Training uses mean squared loss and the canonical
layer mobilities \((n,1,\ldots,1,n)\), in physical time.

Every activation is real on the real axis, holomorphic on the common
strip \(|\operatorname{Im}z|<a\), and satisfies
\(|\phi_\ell(z)|\le B_\phi\) there. The numbers \(a>0,B_\phi<\infty\)
are common activation-class bounds, not a depth-dependent list norm.
Define, entirely from these bounds,
\[
B=\max(1,B_\phi),\qquad
\beta=\max\{10,B,4B/a,32B/a^2,16/a\},\qquad
A_\phi=\beta^{1024}.
\tag{1}
\]

Define the limiting initialized feature covariance on the data recursively:
\[
Q^{(0)}_{ab}=v_a^\top v_b,\qquad
Q^{(\ell)}_{ab}=\mathbb E[\phi_\ell(Z_a)\phi_\ell(Z_b)],
\quad Z\sim N(0,Q^{(\ell-1)}).
\]
The unnormalized feature gap and label RMS are
\[
\gamma=\lambda_{\min}(Q^{(L)})>0,\qquad
Y=\left(m^{-1}\sum_{a=1}^m y_a^2\right)^{1/2}.
\]
Thus \(\gamma\) contains no additional division by \(m\). There is no
orthogonality condition on the inputs. The positive gap is still required;
it is not implied merely by assigning compatible labels.

One fully explicit sufficient label condition is
\[
\boxed{\quad Y\le\frac{\gamma}{m}\exp(-A_\phi^{L}).\quad}
\tag{2}
\]
For every fixed confidence \(1-\delta\), \(0<\delta<1\), there is a
finite \(n_0\), depending on the fixed quantities just specified, such
that for each \(n\ge n_0\), with probability at least \(1-\delta\) over
the reference initialization, the existing autonomous representation can
be constructed with total retained real coordinates bounded by
\[
\boxed{\quad
\operatorname{size}(C)\le
A_\phi^{Ld}(d+3)^{3d}
\left(\frac m\gamma\right)^2
[\log(en)]^{3d+2}+A_\phi m(d+1).
\quad}
\tag{3}
\]
Its prediction obeys
\[
\boxed{\quad
\sup_{t\in[0,\infty]}\sup_{\|x\|=\sqrt d}
|f_C(t,x)-f_n(t,x)|
\le
\frac{A_\phi^{L^2}Y}{\sqrt n}
\left(\frac m\gamma\right)^{3/2}.
\quad}
\tag{4}
\]
The suprema include the convergent fitted endpoints, and compare the two
flows at the same physical time. Both fit the training labels. If \(Y=0\),
the reference predictor is identically zero, and a constant-zero
representation handles that case separately.

Only \(A_\phi\) is an activation-class constant in (2)--(4); its explicit
definition is (1). Depth, dimension, sample count and the gap all appear
in the displayed expressions. This is not a depth-uniform theorem: the
depth costs are explicit, and the source proof still fixes depth before
taking width large. Nor is this a simultaneous event over all widths.

The construction is the existing selected-neuron network with fixed
non-diagonal neuron metrics, an internal residual and an algebraically
corrected readout. It has moving nonlinear hidden features and its own
autonomous optimizer. It is not asserted to follow ordinary reduced-model
gradient flow. The size counts both fixed and moving retained coefficients,
training data and solve caches. Exact-real preprocessing and precision
remain unbounded; no original-width arrays or stored reference trajectory
remain at runtime. These unchanged qualifications are part of the theorem.

## 2. Component estimates and normalization

For proof only put \(\lambda=\min(1,\gamma/m)\) and
\(\ell_n=\log(en)\). The following inputs are quantitative versions of
the existing source and runtime proofs:

* [EXPLICIT_LABEL_CONSTANTS_ROUTE.md](EXPLICIT_LABEL_CONSTANTS_ROUTE.md)
  gives a finite recurrence for the allowable source label coefficient.
  Its Gaussian budget, Hessian endpoint series and activity modulus have
  only activation/depth constants. The cross-check and reconciled source
  addendum bound that coefficient below by \(\exp[-\beta^{40L}]\).
* [EXPLICIT_SOURCE_CONSTANTS_ROUTE.md](EXPLICIT_SOURCE_CONSTANTS_ROUTE.md)
  and its normalization addendum use initialized mixer cap 8, real cap 9,
  complex cap 10, contour activity allowance \(S_{\rm src}=16Y/\lambda\),
  decay \(\rho\le Y e^{-\lambda t/4}\), and horizon
  \(T=32\lambda^{-1}\ell_n\). The resulting source-space dimension
  can be bounded by
  \[
  R\le R_0:=\beta^{50Ld}(d+3)^{3d/2}
                 \lambda^{-1}\ell_n^{3d/2+1}.
  \tag{5}
  \]
  This includes the exact initial sources, first-layer columns and constant
  vector. The numerical dimension budget \(R_0\) is at least \(d\) and
  \(m\). Its carrier coefficient satisfies \(K_{\rm src}\le\beta^{4L}\).
  For \(d=1\), the sphere consists of the two queries \(v=\pm1\).
  Use two time-only source families, one for each query, rather than a
  zero-angle chart pretending to cover both. The additional factor two
  is absorbed by the same displayed dimension envelope.
* [EXPLICIT_RUNTIME_CONSTANTS_ROUTE.md](EXPLICIT_RUNTIME_CONSTANTS_ROUTE.md)
  supplies explicit real fitting, comparison and endpoint-tail constants.
  For a source-interface coefficient \(K\), put
  \[
  X=64B_{\rm rt}(K+1),\quad
  Q=X^{16L+48},\quad
  B_{\rm rt}=\max(1,B_\phi,2B_\phi/a,8B_\phi/a^2)\le\beta.
  \]
  If \(Y/\lambda\le Q^{-1}\), it gives error at most
  \(40Q^2Y\lambda^{-3/2}/\sqrt n\), with source accuracy \(n^{-1}\).

There is a normalization correction to the last route's literal input
interface: its item 3 states a carrier bound proportional to the actual
integral \(\int_0^T\rho_n\), whereas the source proof uses an upper
activity allowance. No lower bound comparing actual activity with
\(Y/\lambda\) has been proved or is needed. The interface used here is
directly
\[
 M\le1+16K_{\rm src}(Y/\lambda)\sqrt{\ell_n}
       \le1+4K(Y/\lambda)\sqrt{\ell_n},
 \qquad K=8+4K_{\rm src}\le\beta^{5L}.
 \tag{6}
\]
This is exactly the bound used in the runtime route's subsequent
comparison. Its other interface errors are at most \(K n^{-1}\), and
initialized mixer norms are at most \(K\). No conclusion depends on the
stronger, unsupported actual-activity normalization.

## 3. Assembly with only an activation constant

First, the covariance trace gives \(\gamma\le B^2\). In particular
\[
\lambda\ge\frac{\gamma}{mB^2},\qquad
\lambda^{-p}\le B^{2p}(m/\gamma)^p\quad(p>0).
\tag{7}
\]
Condition (2) implies
\[
Y/\lambda\le B^2e^{-\beta^{1024L}}
                      \le e^{-\beta^{40L}}.
\]
For \(L\ge2,\beta\ge10\), the last inequality follows from
\(\beta^{1024L}-\beta^{40L}\ge2\log\beta\).
This closes the explicit source label conditions. Also, using (6),
\[
X\le\beta^{7L},\qquad
Q\le\beta^{280L^2},\qquad
Q^{-1}\ge e^{-\beta^{40L}}.
\tag{8}
\]
Indeed \(16L+48\le40L\), and
\(280L^2\log\beta\le\beta^{40L}\). Thus the deterministic runtime
label condition is satisfied too. For nonzero fixed labels enlarge
\(n_0\) to ensure \(n^{-1}\le Y\), as required by that proof.

For storage, every selected layer has at most \(9R_0\) coordinates.
Counting the moving mixers and first layer, readout and residual,
the fixed metrics and their inverses, optional initialized mixer copies,
training features and backward-response caches, and the \(m\)-dimensional
solve arrays gives the conservative bound
\[
\operatorname{size}(C)
\le1020(L+1)R_0^2+10m(d+1).
\tag{9}
\]
For clarity, at most three square arrays per layer for its metric,
inverse and a spare copy cost \(243LR_0^2\); two adjacent-layer mixer
arrays cost \(162(L-1)R_0^2\); four feature/response caches per sample
and layer cost \(36LR_0^2\), since \(m\le R_0\); a dozen
\(m\)-square solve arrays cost \(12R_0^2\). First-layer, readout and
residual arrays, including a fixed first-layer copy, cost at most
\(40R_0^2\), since \(d,m\le R_0\). These fit strictly within (9).
More scratch is unnecessary and can be reused. Real coordinate storage,
not integer index bit complexity, is the resource being counted.

Insert (5) and (7) into (9). For \(L\ge2,d\ge1,\beta\ge10\),
\(1020(L+1)B^4\le\beta^{10Ld}\), so the leading coefficient is at
most \(\beta^{110Ld}(d+3)^{3d}\). This is bounded by the coefficient
in (3). The additive term is also bounded because \(A_\phi\ge10\).

For prediction, the runtime comparison and (7)--(8) give
\[
40Q^2B^3\le\beta^{562L^2}\le A_\phi^{L^2},
\]
which proves (4), including its stated factor of \(Y\). The runtime
proof uses an exact cancellation between the residual discrepancy's
least-norm feature lift and the raw readout discrepancy. Its exponent
depends on bounded activity rather than elapsed time. The real tails
after \(T\) are explicitly controlled by
\(4T_1Y\lambda^{-3/2}e^{-\lambda t/4}\), so enlarging the source
horizon to the chosen \(T\) preserves the same all-time bound.

## 4. What this quantification does and does not improve

The sample/gap powers and \(3d+2\) logarithmic exponent are the sharpest
currently recorded in this study's dimension-based strict-root-width
statement. The architecture coefficients in (1)--(4) are **not** claimed
sharp. In particular \(e^{-A_\phi^L}\) is a convenient, very conservative
closed lower choice for the admissible label coefficient, not evidence
that such a severe depth restriction is necessary. The finite recurrences
in the component notes give better evaluable constants if needed.

No additional sample-count factor or orthogonality assumption has been
introduced. No width-dependent clipping or modification of the reference
model occurs. But bounded holomorphy, a positive limiting initialized
feature gap, fixed architecture/data and small labels remain assumptions.
The construction is an existence result with an unquantified \(n_0\).
Explicit coefficients in (2)--(4) must not be confused with a quantitative
width threshold or a theorem for growing depth/dimension.

## 5. Verification records

The initially frozen component versions were:

| Component | SHA-256 |
| --- | --- |
| Explicit label route | `0fa619fde5966b55287eaaef6d3c59cc11e3d858964d989741556e173aadcb94` |
| Explicit source route before normalization addendum | `959d325966a88496fd3050295d853c068b16f57e6c0e14ce23fcdb49043e9860` |
| Explicit runtime route | `775ed6756af7de018c961173b850ad69930a71e4273c669bfe71c93182987bcd` |

The source normalization addendum records its changes after independent
routes were frozen. The separate algebraic and assembly reconstruction is
[EXPLICIT_LABEL_SOURCE_CHECK.md](EXPLICIT_LABEL_SOURCE_CHECK.md).
These checks quantify the existing source/insertion interfaces; they do
not replace their complete prior proofs, constitute promotion review, or
assert a sharp width threshold. No numerical experiments were used.
