# Exact endpoint identity and the unresolved fluctuation estimate

This note uses the canonical equations in `paper/compact.tex` and the complete
real fitting lemma and proof in `paper/compact_fitting.tex`. It changes neither
the dynamics nor the label cap. All conclusions below concern finite-width
networks on the paper's initialization/fitting event. The note does **not**
assert the requested general endpoint lower bound.

## 1. Setup

Use the paper's notation: normalized inputs are $v=x/\sqrt d$, hidden responses
are $h^{(\ell)}$, the residual-free backward responses are
$\delta^{(\ell)}$, and $f_n=w^\top h^{(L)}/n$. The initialization is independent
Gaussian in all hidden blocks and zero in the readout. Training uses mean
squared loss and the paper's block mobilities. Write $X=(x_1,\ldots,x_m)$.

Define the mobility-weighted tangent kernel, here a finite-width quantity, by

\[
\begin{split}
K_t(x,z)={}&\frac{h^{(L)}(t,x)^\top h^{(L)}(t,z)}n
 +\frac{\delta^{(1)}(t,x)^\top\delta^{(1)}(t,z)}n
                      \frac{x^\top z}{d}\\
&+\sum_{\ell=2}^L
 \frac{\delta^{(\ell)}(t,x)^\top\delta^{(\ell)}(t,z)}n
 \frac{h^{(\ell-1)}(t,x)^\top h^{(\ell-1)}(t,z)}n.
\end{split}
\]

The kernel follows by differentiating the prediction with respect to each
weight block and multiplying by that block's mobility. In particular the
hidden-matrix contribution has denominator $n^2$, not $n$. At time zero all
backward responses vanish, so $K_0$ is exactly the initial top-feature Gram
kernel. On the fitting event, $K_0(X,X)\succeq(\gamma/2)I_m$.

Define the readout-only endpoint on the **same initialized hidden network** by

\[
f_{\rm RF}(x)=K_0(x,X)K_0(X,X)^{-1}y.
\]

This is only a comparator. The actual network continues to train every hidden
block.

## 2. Exact identity

For every sphere query, the actual endpoint satisfies

\[
\begin{split}
f_n(\infty,x)-f_{\rm RF}(x)
=\frac2m\int_0^\infty
\big[&K_t(x,X)\\
&-K_0(x,X)K_0(X,X)^{-1}K_t(X,X)\big]
\big(y-f_n(t,X)\big)\,dt.
\end{split} \tag{1}
\]

Indeed the chain rule and the exact parameter flow give

\[
\partial_t f_n(t,x)=\frac2m K_t(x,X)(y-f_n(t,X)).
\]

The fitting lemma bounds the kernel uniformly in time and on the sphere,
and bounds $\|y-f_n(t,X)\|_2$ by
$\sqrt mY\exp(-\gamma t/(2m))$. Thus all integrals converge absolutely.
Integrating the displayed equation uses $f_n(0,x)=0$. Applying the same
equation on the training list and using exact interpolation gives

\[
y=\frac2m\int_0^\infty K_t(X,X)(y-f_n(t,X))\,dt.
\]

Multiplication by $K_0(x,X)K_0(X,X)^{-1}$ and subtraction prove (1).
Its integrand's bracket is exactly zero at time zero. It need not remain zero.

## 3. A deterministic cubic remainder, with its constants exposed

All symbols in this paragraph are local to this bound. Put $\lambda=\gamma/m$.
Use the fitting lemma's constants

\[
\begin{gathered}
s=\max\{1,\max_\ell\sup_{|\operatorname{Im}z|\le a/2}|\phi_\ell'(z)|\},
\qquad H=\max_{0\le j\le L}\sqrt{Q^{(j)}_{11}},\\
D_\ell=s(9s)^{L-\ell},\qquad
F=s^2\left[(9s)^{2L-2}+4H^2\sum_{j=0}^{L-2}(9s)^{2j}\right],\\
B=28HF+4\left(D_1^2+4H^2\sum_{\ell=2}^LD_\ell^2\right).
\end{gathered}
\]

These constants depend only on activations and depth. The diagonal population
variances depend only on the unit input norm, not the training geometry.
Since $Q^{(0)}_{11}=1$, $H\ge1$; the paper assumes $\lambda\le1$.
The fitting lemma gives

\[
\frac{\|h_0^{(L)}(x)\|} {\sqrt n}\le\frac{3H}2,
\quad\frac{\|h_t^{(L)}(x)\|}{\sqrt n}\le2H,
\quad\frac{\|h_t^{(L)}(x)-h_0^{(L)}(x)\|}{\sqrt n}
\le8FY^2\lambda^{-3/2},
\]

and $\|w_t\|/\sqrt n\le2Y/\sqrt\lambda$. Backward propagation gives
$\|\delta^{(\ell)}(t,x)\|/\sqrt n\le2D_\ell Y/\sqrt\lambda$.
Subtracting the readout kernel, and bounding the hidden contributions in the
definition of $K_t$, therefore gives

\[
\sup_{t,x,z}|K_t(x,z)-K_0(x,z)|\le B Y^2\lambda^{-3/2}. \tag{2}
\]

For the readout term the coefficient is
$(2H+3H/2)8F=28HF$. The first-layer hidden term is at most
$4D_1^2Y^2/\lambda$ and the remaining terms sum to at most
$16H^2Y^2\lambda^{-1}\sum_{\ell=2}^LD_\ell^2$.
Using $\lambda\le1$ proves (2).

Let $b=BY^2\lambda^{-3/2}$ in the next estimates only. Then

\[
\begin{gathered}
\|K_t(x,X)-K_0(x,X)\|_2\le\sqrt m\,b,\qquad
\|K_t(X,X)-K_0(X,X)\|_{\rm op}\le mb,\\
\|K_0(x,X)K_0(X,X)^{-1}\|_2
\le\frac{9H^2\sqrt m}{2\gamma}.
\end{gathered}
\]

Writing the bracket in (1) as the first kernel difference minus
$K_0(x,X)K_0(X,X)^{-1}$ times the training-kernel difference, its Euclidean
norm is at most $\sqrt m\,b(1+9H^2/(2\lambda))$. Also

\[
\int_0^\infty\|y-f_n(t,X)\|_2\,dt\le2\sqrt mY/\lambda.
\]

Consequently

\[
\sup_{\|x\|=\sqrt d}|f_n(\infty,x)-f_{\rm RF}(x)|
\le4B\left(1+\frac{9H^2}{2\lambda}\right)
        \frac{Y^3}{\lambda^{5/2}}. \tag{3}
\]

This is a genuine estimate for all-hidden nonlinear training, but it is
**independent of width**. It is not a bound on random fluctuations of the
remainder, and must not be used as one.

## 4. Why (3) cannot transfer a root-width lower bound

For two independent runs, put $R_n=f_n(\infty,\cdot)-f_{\rm RF}$ and define
$\widetilde R_n$ in the other run. The exact decomposition is

\[
f_n(\infty,\cdot)-\widetilde f_n(\infty,\cdot)
=f_{\rm RF}-\widetilde f_{\rm RF}+R_n-\widetilde R_n.
\]

Even if the first difference has a proved lower scale $cY/\sqrt n$, (3)
only bounds the second difference by a constant times $Y^3$. For a fixed
positive label size this upper bound is larger than $Y/\sqrt n$ eventually.
Shrinking $Y$ with width would change the user's scope and is not a repair.

Moreover, bounding $R_n-\widetilde R_n$ merely by $O(Y/\sqrt n)$ would
not suffice: the remainder can be correlated with the comparator and might
cancel its leading fluctuation. One needs a suitably smaller *relative*
bound or a direct proof that the trained endpoint fluctuation is nonzero.
An endpoint functional central limit theorem with nonzero variance on at least
one separated query would suffice, but no such theorem is proved here.

No conclusion of impossibility follows from this gap. The frozen-feature
comparator's nondegeneracy and actual endpoint nondegeneracy are different
claims.
