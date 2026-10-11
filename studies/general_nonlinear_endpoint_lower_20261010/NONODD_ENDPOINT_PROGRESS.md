# Removing oddness: endpoint extension and remaining obligation

2026-10-11. Continuation of the same endpoint study. No paper or book change.
The target is to remove oddness from **every** hidden activation, retaining
the proper-training-span/orthogonal-query geometry, the original label cap,
and the actual fitted endpoint. That full extension remains unproved.

There is, however, a complete endpoint extension allowing a nonodd final
hidden activation, and an arbitrary-depth comparison lemma that removes
oddness from every layer by retaining the trained feature means explicitly.
The latter comparator does not yet have the needed anti-concentration bound.
These two accomplishments must not be combined into a nonexistent full
endpoint theorem.

The inputs are the current paper setup and fitting proof, the same study's
`ODD_DEPTH_ENDPOINT.md`, and the new complete derivations
`NONODD_INNOVATION_ROUTE.md` and `NONODD_SCALAR_ROUTE.md`. The source-moment
route also reads the current `paper/compact_foundations.tex` in full. The
rigorous-math and canonical-notation instructions were applied. All new
notation below is local to the stated theorem and proof.

## 1. Endpoint theorem with an arbitrary last activation

Use the canonical dense network, initialization, and gradient flow of
`ODD_DEPTH_ENDPOINT.md`: first-layer entries are independent standard
Gaussians, hidden entries have variance \(1/n\), all blocks are independent,
the initial readout is zero, and

\[
h^{(1)}(x)=\phi_1(W^{(1)}x/\sqrt d),\qquad
h^{(j)}(x)=\phi_j(W^{(j)}h^{(j-1)}(x)),\qquad
f_n(x)=w^\top h^{(L)}(x)/n.
\]

Training minimizes \(m^{-1}\sum_a(f_n(x_a)-y_a)^2\) with block mobilities
\((n,1,\ldots,1,n)\). Let \(L,m\ge2\), let
\(\gamma=\lambda_{\min}(Q^{(L)})>0\), and retain
\(Y=\|y\|/\sqrt m>0\), \(\gamma/m\le1\), and

\[
Y\le(\gamma/m)\beta^{-30L}.
\tag{1}
\]

The activation assumptions and the envelope \(\beta\ge10\) are exactly
those in the odd-endpoint note and current compact paper: strip analyticity,
bounded first and second derivatives on the half strip, and bounded values
at zero. Values on the real axis need not be bounded.

Assume that \(\phi_1,\ldots,\phi_{L-1}\) are odd. No parity assumption is
made on \(\phi_L\). The variance qualification is now the **centered** one:
for a standard normal scalar \(G\),

\[
\operatorname{Var}\!\left[
 \phi_L\!\left(\sqrt{Q^{(L-1)}_{11}}G\right)\right]
\ge\beta^{-40L}.
\tag{2}
\]

Let the training inputs span a proper subspace and let \(v\) be a fixed unit
vector orthogonal to it. At every sufficiently large individual width, two
independent actual trained runs satisfy

\[
\Pr\left\{
 |f_n(\infty,\sqrt d\,v)-\widetilde f_n(\infty,\sqrt d\,v)|
 \ge
 \frac{
 \sqrt{\operatorname{Var}[\phi_L(\sqrt{Q^{(L-1)}_{11}}G)]
           \;y^\top(Q^{(L)})^{-1}y}}
 {2048\sqrt n},\quad\text{both runs fit}
 \right\}\ge\frac12.
\tag{3}
\]

All data, labels, activations, and depth are fixed before width increases.
The sufficient width remains unquantified. Equation (2) is not inferred
from a lower bound on the uncentered second moment: that inference is false
for general nonodd activations. It holds automatically for the concrete
families below, so they need no additional label restriction.

### Proof

Condition on the first-layer initialization restricted to the training span
and on all hidden mixers. Denote this information by \(\mathcal A_n\).
The training path and fitted weights are then fixed, whereas
\(Z=W^{(1)}_0v\sim N(0,I_n)\) is independent of \(\mathcal A_n\) and does
not move during training. The fitting event can be chosen using only
\(\mathcal A_n\), with probability tending to one.

Use the local constants \(\lambda,H,s,D_j,U_j,F_j,F,K_j,T_L,D\) defined in
Sections 1 and 3 of `ODD_DEPTH_ENDPOINT.md`. In particular

\[
\lambda=\gamma/m,\qquad
K_j=s(8s)^{j-1},\qquad
D=120K_LF+36\sqrt2\,T_L\le\beta^{16L}.
\]

Write \(B_t=[h^{(L)}(t,x_a)]_{a=1}^m/\sqrt n\),
\(u_t=w_t/\sqrt n\),
\(u_*=B_0(B_0^\top B_0)^{-1}y\), and \(e=\|u_*\|\).
The readout-energy proof uses no oddness, so it gives

\[
\sup_t\|u_t\|\le3e,\qquad
\|u_\infty-u_*\|\le120Fe(Y/\lambda)^2,
\qquad e\le\sqrt2Y/\sqrt\lambda.
\tag{4}
\]

Every initialized query feature vector at a layer strictly below \(L\)
is odd in \(Z\), hence centered. The whole-feature subtraction argument
therefore remains valid through the **last** layer: its covariance estimate
is applied only to the input of a changed mixer, which belongs to an earlier
layer. It never requires that the output of the last activation be centered.
Explicitly, for \(j<L\), Gaussian Poincare and oddness give

\[
\mathbb E_Z\|E h_0^{(j)}\|^2\le K_j^2\|E\|_F^2.
\]

The displacement bound
\(\|W_\infty^{(j)}-W_0^{(j)}\|_F
\le4U_j(\sup_t\|u_t\|)Y/\lambda\)
and the forward recursion imply

\[
\|h_\infty^{(L)}-h_0^{(L)}\|_{L^2_Z}
\le4(\sup_t\|u_t\|)YT_L/\lambda.
\tag{5}
\]

Let \(F_n(Z)=u_*^\top h_0^{(L)}(Z)/\sqrt n\) be frozen-feature
interpolation and \(R_n=f_n(\infty,\sqrt d\,v)-F_n(Z)\).
For any scalar variable, write \(\|X\|_{2,c}=\|X-\mathbb E_ZX\|_2\).
Centering is an \(L^2\) contraction. Poincare applies to the changed
readout against \(h_0^{(L)}\) without a mean-zero assumption, while (5)
bounds the changed features. Thus exactly the previous constant gives

\[
\|R_n\|_{2,c}\le De(Y/\lambda)^2/\sqrt n.
\tag{6}
\]

For clarity put, locally,
\(v_L=\operatorname{Var}[\phi_L(\sqrt{Q^{(L-1)}_{11}}G)]\) and
\(e_0^2=y^\top(Q^{(L)})^{-1}y\).
Take two independent unused columns \(Z,Z'\) with the same active
initialization. Oddness through layer \(L-1\) makes the population
last-layer query preactivations mutually independent and independent of
all training preactivations. The paired interpolation influence therefore
has variance

\[
\mathbb E[(H_*-H_*')^2(H^\top(Q^{(L)})^{-1}y)^2]
=2v_Le_0^2.
\tag{7}
\]

The conditional anti-concentration theorem of
`NONODD_INNOVATION_ROUTE.md`, equation (9), is proved by a conditional
top-row triangular CLT followed by the elementary two-replica inequality.
It applies to (7). With its \(\delta=1/4\), its radius is
\(\sqrt\pi\,\sqrt{v_L}e_0/(512\sqrt n)\).
Consequently at the smaller radius
\(r_n=\sqrt{v_L}e_0/(1024\sqrt n)\), with active probability at least
\(7/8\), eventually,

\[
\sup_a\Pr_Z\{|F_n(Z)-a|\le r_n\mid\mathcal A_n\}\le1/4.
\tag{8}
\]

Intersect with the fitting event and with \(e\le\sqrt2e_0\), losing
only \(o(1)\) active probability. The latter follows from initialization
Gram convergence. Conditional Chebyshev and (6) imply

\[
\Pr_Z\{|R_n-\mathbb E_ZR_n|>r_n/2\mid\mathcal A_n\}
\le8\cdot1024^2D^2(Y/\lambda)^4/v_L\le1/8.
\tag{9}
\]

For the last inequality it suffices that
\(D(Y/\lambda)^2/\sqrt{v_L}\le1/8192\).
Equations (1)--(2) give the stronger bound
\(D(Y/\lambda)^2/\sqrt{v_L}\le\beta^{-24L}\).
For every center \(a\), the triangle inequality, (8), and (9) now give

\[
\Pr_Z\{|f_n(\infty,\sqrt d\,v)-a|\le r_n/2
              \mid\mathcal A_n\}\le3/8.
\]

Condition additionally on the entire independent second run and use its
endpoint value as \(a\). Its fitting event has probability tending to one.
The probability of separation and fitting is at least
\((7/8-o(1))(5/8)-o(1)=35/64-o(1)>1/2\), eventually.
The separation threshold is \(r_n/2\), proving (3).

### Concrete nonodd activations, including unbounded ones

Take arbitrary mixtures of the previously checked tanh, arctan, sine, erf,
arsinh, and \(z+\tanh z\) in layers \(1,\ldots,L-1\).
Their diagonal recursion gives \(Q^{(L-1)}_{11}\ge32^{-(L-1)}\).
For completeness the two additional monotone examples obey, for
\(0\le t\le1\),
\(\operatorname{erf}(t)\ge(2/\sqrt\pi)(t-t^3/3)\ge t/2\) and
\(\operatorname{arsinh}(t)\ge t/\sqrt2\).
Together with oddness, monotonicity, and
\(\mathbb E[G^2\mathbf1_{|G|\le1}]>1/8\), these give the same recursion
\(\mathbb E\phi(\sqrt qG)^2\ge\min(q,1)/32\) as the other checked families.
Here a layerwise mixture means a choice of one listed function per layer,
not an arbitrary linear combination of functions.
The final activation can be any of

\[
\operatorname{softplus}(z)=\log(1+e^z),\qquad
\operatorname{SiLU}(z)=\frac{z}{1+e^{-z}},\qquad
\operatorname{GELU}(z)=z\Phi(z),
\]

where \(\Phi\) is the standard Gaussian distribution function.
Each satisfies \(\phi(z)-\phi(-z)=z\), hence is \(z/2\) plus an even
function. Gaussian even and odd functions are orthogonal, including after
centering the even part. It follows that

\[
\operatorname{Var}[\phi(\sqrt qG)]\ge q/4.
\]

Thus (2) holds: its left side is at least
\(32^{-(L-1)}/4\ge32^{-L}\ge\beta^{-40L}\).
All three functions are nonaffine and unbounded. They belong to the paper's
strip class: softplus has a holomorphic logarithm on \(|\Im z|<1\), since
\(1+e^z\) has positive real part there; SiLU has no poles on this strip.
Their first two derivatives are bounded on its half strip, as their logistic
factors are bounded and the remaining factors containing \(z\) decay
exponentially as \(|\Re z|\to\infty\). GELU is entire, with
\(\phi'=\Phi+z\varphi\) and \(\phi''=(2-z^2)\varphi\), where
\(\varphi(z)=(2\pi)^{-1/2}e^{-z^2/2}\).
On any fixed horizontal strip the polynomial-Gaussian terms are bounded;
\(\Phi(x+iy)=\Phi(x)+i\int_0^y\varphi(x+iu)du\) is bounded there too.
Their actual derivative envelopes are included in \(\beta\) as usual.

This is not a theorem for a network using GELU, SiLU, or softplus in **every**
layer.

## 2. What is now available without oddness anywhere

1. `NONODD_INNOVATION_ROUTE.md`, equation (9), proves frozen-feature
   anti-concentration conditional on the **entire training initialization**,
   at arbitrary fixed depth for general admitted activations. Its positive
   root-width scale is obtained from a paired population variance.
2. `NONODD_SCALAR_ROUTE.md`, Section 5, proves the same sharp centered
   root-width endpoint comparison as in the odd argument, but with a
   **mean-adapted** comparator. It keeps each actual trained mean as an
   explicit bias and only freezes the centered mixing operation.
3. `NONODD_MOMENT_ROUTE.md` extracts width-independent all-time empirical
   readout moments from the current source proof, and closes the former
   two-layer unbounded-activation moment gap for a weaker scalar comparison.

The objects in items 1 and 2 are different. In item 2 the biases depend on
the trained network; its top rows are not conditionally iid under the
conditioning used in item 1's CLT. Furthermore, for nonodd activations an
uncentered feature second moment need not lower-bound the random query
innovation. A proof must control that same innovation through the adapted
means, or prove fitted-output anti-concentration directly. None of the
current estimates supplies that missing step under the unchanged cap.

There is no counterexample here to the requested fully nonodd endpoint
lower bound. The explicit examples in the route notes only invalidate
particular proposed shortcuts. No new label restriction, centered-activation
replacement, or readout-only conclusion is offered as the requested answer.
