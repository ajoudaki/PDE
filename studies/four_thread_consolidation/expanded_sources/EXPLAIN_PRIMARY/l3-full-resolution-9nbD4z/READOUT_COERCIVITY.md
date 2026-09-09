# Finite-width readout coercivity at three hidden layers

## Scope

This note proves unconditional finite-width statements for the arctangent
network, including zero and sufficiently small initial readout. It does
not prove population existence, uniqueness, or width convergence.

All vectors have length \(n\). The symbol \(\|\cdot\|_2\) always denotes
the ordinary Euclidean vector norm, \(\|\cdot\|_{\rm op}\) the induced
matrix norm, and \(\|\cdot\|_{\rm F}\) the Frobenius matrix norm.

## Exact feature flow and global finite-width existence

Let \(a=\pi/2\), \(\phi(x)=\arctan x\), and
\[
 \phi'(x)=\frac1{1+x^2}.
\]
The forward equations are
\[
 h^{(1)}=\phi(z^{(1)}),\qquad
 z^{(2)}=W^{(2)}h^{(1)},\qquad h^{(2)}=\phi(z^{(2)}),
\]
\[
 z^{(3)}=W^{(3)}h^{(2)},\qquad h^{(3)}=\phi(z^{(3)}),
 \qquad f=\frac1n(W^{(4)})^{\mathsf T}h^{(3)}.
\]
Here \(\phi\) is applied coordinatewise. Define the diagonal matrices
\[
 D_\ell=\operatorname{diag}\bigl(\phi'(z^{(\ell)}_i)\bigr),
 \qquad \ell=1,2,3,
\]
and the backward vectors
\[
 \delta^{(3)}=D_3W^{(4)},\qquad
 \delta^{(2)}=D_2(W^{(3)})^{\mathsf T}\delta^{(3)},\qquad
 \delta^{(1)}=D_1(W^{(2)})^{\mathsf T}\delta^{(2)}.
\]
Feature time \(s\) denotes ascent of \(f\), with the normalized metric
on vector blocks and the Frobenius metric on matrix blocks:
\[
 \frac{dz^{(1)}}{ds}=\delta^{(1)},\qquad
 \frac{dW^{(2)}}{ds}=\frac1n\delta^{(2)}(h^{(1)})^{\mathsf T},
\]
\[
 \frac{dW^{(3)}}{ds}=\frac1n\delta^{(3)}(h^{(2)})^{\mathsf T},
 \qquad \frac{dW^{(4)}}{ds}=h^{(3)}.                       \tag{1}
\]
This smooth finite-dimensional system has a unique solution for every
\(s\ge0\). Here is a direct no-escape proof. Set
\[
 b_4=\frac{\|W^{(4)}(0)\|_2}{\sqrt n},\qquad
 M_j=\|W^{(j)}(0)\|_{\rm op},\quad j=2,3.
\]
Since \(\|h^{(\ell)}\|_2/\sqrt n\le a\) and \(\|D_\ell\|_{\rm op}\le1\),
\[
 \frac{\|W^{(4)}(s)\|_2}{\sqrt n}\le b_4+as,
\]
\[
 \|W^{(3)}(s)\|_{\rm op}
 \le M_3+ab_4s+\frac{a^2s^2}{2}=:\mathcal M_3(s),
\]
\[
 \|W^{(2)}(s)\|_{\rm op}
 \le M_2+a\int_0^s\mathcal M_3(u)(b_4+au)\,du
 =:\mathcal M_2(s).
\]
The same bounds control the Frobenius norms of the matrix increments:
the Frobenius norm of \(uv^{\mathsf T}/n\) is
\(\|u\|_2\|v\|_2/n\). Finally,
\[
 \frac{\|z^{(1)}(s)-z^{(1)}(0)\|_2}{\sqrt n}
 \le\int_0^s\mathcal M_2(u)\mathcal M_3(u)(b_4+au)\,du.
\]
All right sides are finite polynomials on every bounded feature interval.
Thus no parameter can escape to infinity in finite feature time.

## Positive readout acceleration

Define the symmetric positive semidefinite matrices
\[
 A_2=\frac{\|h^{(1)}\|_2^2}{n}I
       +W^{(2)}D_1^2(W^{(2)})^{\mathsf T},                 \tag{2}
\]
\[
 A_3=\frac{\|h^{(2)}\|_2^2}{n}I
       +W^{(3)}D_2A_2D_2(W^{(3)})^{\mathsf T}.            \tag{3}
\]
Differentiating the forward equations using (1) gives exactly
\[
 \frac{dh^{(1)}}{ds}=D_1^2(W^{(2)})^{\mathsf T}\delta^{(2)},
 \qquad
 \frac{dz^{(2)}}{ds}=A_2\delta^{(2)},
\]
\[
 \frac{dz^{(3)}}{ds}=A_3\delta^{(3)},\qquad
 \frac{d^2W^{(4)}}{ds^2}
 =\frac{dh^{(3)}}{ds}=D_3A_3D_3W^{(4)}.                 \tag{4}
\]
In particular the matrix \(D_3A_3D_3\) in (4) is positive semidefinite.
This is positivity of a quadratic form, not preservation of coordinatewise
signs.

Let \(g(s)=\|W^{(4)}(s)\|_2/\sqrt n\). Wherever \(g>0\),
\[
 g'(s)=\frac{(W^{(4)})^{\mathsf T}h^{(3)}}{n g(s)}
       =\frac{f(s)}{g(s)}
\]
and
\[
 g''(s)=
 \frac{\|h^{(3)}\|_2^2/n-g'(s)^2
       +(W^{(4)})^{\mathsf T}D_3A_3D_3W^{(4)}/n}{g(s)}
 \ge0.                                                    \tag{5}
\]
The first two terms in the numerator have nonnegative sum by
Cauchy--Schwarz; the last term is nonnegative by (3).

The exact feature kernel is
\[
 \begin{aligned}
 \kappa(s):=\frac{df}{ds}
 &=\frac{\|h^{(3)}\|_2^2}{n}
   +\frac{(W^{(4)})^{\mathsf T}D_3A_3D_3W^{(4)}}n\\
 &=\frac{\|h^{(3)}\|_2^2}{n}
  +\frac{\|\delta^{(3)}\|_2^2\|h^{(2)}\|_2^2}{n^2}
  +\frac{\|\delta^{(2)}\|_2^2\|h^{(1)}\|_2^2}{n^2}
  +\frac{\|\delta^{(1)}\|_2^2}{n}.
 \end{aligned}                                           \tag{6}
\]

## Zero-readout theorem

Assume \(W^{(4)}(0)=0\) and
\[
 m_3:=\frac{\|h^{(3)}(0)\|_2^2}{n}>0.
\]
Then, for every \(s\ge0\),
\[
 \frac{\|W^{(4)}(s)\|_2}{\sqrt n}\ge s\sqrt{m_3},\qquad
 \frac{\|h^{(3)}(s)\|_2}{\sqrt n}\ge\sqrt{m_3},
 \qquad f(s)\ge m_3s,\qquad \kappa(s)\ge m_3.             \tag{7}
\]

Indeed \(W^{(4)}(s)=s h^{(3)}(0)+o(s)\) and
\((W^{(4)})'(s)=h^{(3)}(0)+o(1)\), so
\(g'(0+)=\sqrt{m_3}\). Convexity (5) gives
\(g'\ge\sqrt{m_3}\) and \(g\ge s\sqrt{m_3}\) until any possible
later zero of \(g\). The latter inequality rules out a first later zero.
Thus these inequalities hold for all \(s>0\). Now
\[
 \frac{\|h^{(3)}\|_2}{\sqrt n}\ge g',\qquad f=gg',
\]
which proves (7), including the kernel bound by (6).

The excluded case \(m_3=0\) has zero initial vector field. Its unique
finite-width solution is stationary.

For physical gradient flow of \((f-1)^2\), the feature clock is
\[
 \frac{ds}{dt}=2(1-f(s(t))),\qquad s(0)=0.                \tag{8}
\]
There is a unique \(s_*\in(0,1/m_3]\) with \(f(s_*)=1\), because
\(f(0)=0\) and \(f'\ge m_3\). The solution of (8) stays below \(s_*\)
at every finite physical time and increases to \(s_*\). In particular,
\[
 0<1-f(s(t))
 =\exp\left(-2\int_0^t\kappa(s(v))\,dv\right)
 \le e^{-2m_3t},                                        \tag{9}
\]
\[
 s(t)\le\frac{1-e^{-2m_3t}}{m_3}<\frac1{m_3}.             \tag{10}
\]
The loss is at most \(e^{-4m_3t}\).

## A quantitative extension to small nonzero readout

Fix constants \(0<b\le a\) and \(M_2,M_3\ge0\). Suppose
\[
 \frac{\|h^{(3)}(0)\|_2}{\sqrt n}\ge b,\qquad
 \|W^{(j)}(0)\|_{\rm op}\le M_j,\quad j=2,3.
\]
Define constants independent of \(n\):
\[
 L_3=M_3+a+\frac{a^2}{2},\qquad
 L_2=M_2+aL_3\left(1+\frac a2\right),
\]
\[
 B=a^2+L_3^2(a^2+L_2^2),\qquad
 s_0=\min\left\{1,\sqrt{\frac{b}{8aB}}\right\},\qquad
 \varepsilon_0=\min\left\{1,\frac{bs_0}{16}\right\}.        \tag{11}
\]
If
\[
 \varepsilon:=\frac{\|W^{(4)}(0)\|_2}{\sqrt n}
 \le\varepsilon_0,
\]
then for every \(s\ge0\),
\[
 \frac{\|h^{(3)}(s)\|_2}{\sqrt n}\ge\frac b2,\qquad
 \kappa(s)\ge\frac{b^2}{4}.                              \tag{12}
\]

To prove this, the polynomial estimates above give
\[
 \|W^{(3)}(s)\|_{\rm op}\le L_3,\qquad
 \|W^{(2)}(s)\|_{\rm op}\le L_2,\qquad
 \|D_3A_3D_3\|_{\rm op}\le B
 \quad(0\le s\le1).
\]
Equation (4) and
\(\|W^{(4)}(s)\|_2/\sqrt n\le\varepsilon+as\) therefore imply
\[
 \frac{\|h^{(3)}(s)-h^{(3)}(0)\|_2}{\sqrt n}
 \le B\left(\varepsilon s+\frac{as^2}{2}\right),          \tag{13}
\]
\[
 \frac{\|W^{(4)}(s)-W^{(4)}(0)-s h^{(3)}(0)\|_2}{\sqrt n}
 \le B\left(\frac{\varepsilon s^2}{2}
                         +\frac{as^3}{6}\right).         \tag{14}
\]
Since \(\varepsilon\le bs_0/16\le as_0\) and
\(Ba s_0^2\le b/8\), (13) gives
\[
 \frac{\|h^{(3)}(s)-h^{(3)}(0)\|_2}{\sqrt n}
 \le\frac{3b}{16}\quad(0\le s\le s_0).                   \tag{15}
\]
Thus the desired feature lower bound holds on \([0,s_0]\).

For continuation, (14) and the bound on the initial readout give
\[
 \frac{\|W^{(4)}(s_0)-s_0h^{(3)}(0)\|_2}{s_0\sqrt n}
 \le\frac b{16}+\frac b{12}=\frac{7b}{48}.
\]
In particular \(W^{(4)}(s_0)\ne0\). Combining this with (15),
\[
 \begin{aligned}
 g'(s_0)\ge{}&
 \frac{\|h^{(3)}(0)\|_2}{\sqrt n}
 -2\frac{\|W^{(4)}(s_0)-s_0h^{(3)}(0)\|_2}{s_0\sqrt n}\\
 &-\frac{\|h^{(3)}(s_0)-h^{(3)}(0)\|_2}{\sqrt n}\\
 \ge{}&b-\frac{7b}{24}-\frac{3b}{16}
 =\frac{25b}{48}>\frac b2.                               \tag{16}
 \end{aligned}
\]
Here the elementary inequality being used is
\(x^\top y/\|x\|_2\ge\|y\|_2-2\|x-y\|_2\) for nonzero
\(x\): write \(y=x+(y-x)\), use Cauchy--Schwarz, then
\(\|x\|_2\ge\|y\|_2-\|x-y\|_2\).
Apply it with \(x=W^{(4)}(s_0)/(s_0\sqrt n)\) and
\(y=h^{(3)}(0)/\sqrt n\), and bound the remaining feature difference
by Cauchy--Schwarz.
Convexity (5) now gives \(g'(s)\ge25b/48\) for all \(s\ge s_0\);
as in the zero-readout proof, this prevents a later zero of \(g\).
Together with (15) and \(\|h^{(3)}\|_2/\sqrt n\ge g'\), this proves
(12) on the entire feature half-line.

This corollary requires small normalized Euclidean readout norm only.
It imposes no coordinatewise bound on the initial readout.

Write \(f_0=f(0)\) and \(e_0=1-f_0\). The smallness assumptions ensure
\[
 |f_0|\le a\varepsilon\le\frac{a^2}{16}<1,
\]
so \(e_0>0\). There is a unique feature time \(s_*>0\) with \(f(s_*)=1\),
and physical gradient flow obeys
\[
 0<1-f(s(t))\le e_0e^{-b^2t/2},\qquad
 s(t)\le\frac{4e_0}{b^2}\left(1-e^{-b^2t/2}\right),
 \qquad s_*\le\frac{4e_0}{b^2}.                          \tag{17}
\]
These statements follow from (8) and (12) exactly as in (9)--(10).

## Exact action and uniform parameter displacement

For either initialization, (6) and the Frobenius norm of the rank-one
updates give
\[
 \begin{aligned}
 f(s)-f(0)=\int_0^s\Bigg[
 &\frac1n\left\|\frac{dz^{(1)}}{du}\right\|_2^2
 +\left\|\frac{dW^{(2)}}{du}\right\|_{\rm F}^2\\
 &+\left\|\frac{dW^{(3)}}{du}\right\|_{\rm F}^2
 +\frac1n\left\|\frac{dW^{(4)}}{du}\right\|_2^2
 \Bigg]\,du.
 \end{aligned}                                           \tag{18}
\]
Cauchy--Schwarz in the direct-sum parameter metric yields
\[
 \begin{aligned}
 &\frac{\|z^{(1)}(s)-z^{(1)}(0)\|_2^2}{n}
 +\|W^{(2)}(s)-W^{(2)}(0)\|_{\rm F}^2\\
 &\quad+\|W^{(3)}(s)-W^{(3)}(0)\|_{\rm F}^2
 +\frac{\|W^{(4)}(s)-W^{(4)}(0)\|_2^2}{n}
 \le s\,[f(s)-f(0)].
 \end{aligned}                                           \tag{19}
\]
Along the zero-readout physical trajectory the right side is at most
\(1/m_3\). Along the small-readout physical trajectory it is at most
\[
 \frac{4e_0^2}{b^2}.                                    \tag{20}
\]
Thus the two trained matrix corrections have uniformly bounded
Frobenius norms for all physical time, and therefore uniformly bounded
operator norms. The normalized first-layer and readout movements are
uniformly bounded as well.

For zero readout, one also has the coordinatewise estimate
\[
 |W^{(4)}_i(s(t))|\le as(t)\le\frac a{m_3}.
\]
For nonzero readout, the same statement holds for the increment
\(|W^{(4)}_i(s(t))-W^{(4)}_i(0)|\), with upper bound \(4ae_0/b^2\).

## Exponential convergence of every finite-width parameter

For compact notation in this paragraph, let
\(\theta=(z^{(1)},W^{(2)},W^{(3)},W^{(4)})\), and let
\(\|\theta-\widetilde\theta\|_{\rm par}^2\) denote the sum of the four
squared distances on the left of (19). Set \(k_0=m_3\) in the
zero-readout theorem, and \(k_0=b^2/4\) in the small-readout corollary.
Write \(e(t)=1-f(s(t))\), so
\[
 e(t)\le e_0e^{-2k_0t}.
\]
The lower bound \(\kappa\ge k_0\) and the identity \(f(s_*)=1\) give
\[
 s_*-s(t)\le\frac{e(t)}{k_0},\qquad
 \int_{s(t)}^{s_*}\|\theta'(u)\|_{\rm par}^2\,du=e(t).
\]
Therefore Cauchy--Schwarz bounds even the remaining parameter path length:
\[
 \int_{s(t)}^{s_*}\|\theta'(u)\|_{\rm par}\,du
 \le\sqrt{[s_*-s(t)]e(t)}
 \le\frac{e(t)}{\sqrt{k_0}}.                             \tag{21}
\]
The unique finite-width solution consequently converges to
\(\theta_\infty=\theta(s_*)\), with output \(f(\theta_\infty)=1\), and
\[
 \|\theta(s(t))-\theta_\infty\|_{\rm par}
 \le\frac{e_0}{\sqrt{k_0}}e^{-2k_0t}.                    \tag{22}
\]
Here uniqueness means that the given initial condition determines its
endpoint; it does not assert that the network has a unique minimizer.

## The prescribed Gaussian initialization

Independently initialize
\[
 z_i^{(1)}(0)\sim N(0,1),\qquad
 W_{ji}^{(2)}(0),W_{ji}^{(3)}(0)\sim N(0,1/n),\qquad
 W_i^{(4)}(0)\sim N(0,n^{-2}).
\]
Define positive deterministic constants recursively, with \(G\sim N(0,1)\):
\[
 m_1=\mathbb E[\arctan(G)^2],\qquad
 m_2=\mathbb E[\arctan(\sqrt{m_1}G)^2],\qquad
 m_3=\mathbb E[\arctan(\sqrt{m_2}G)^2].
\]
Every constant is positive because its Gaussian argument has positive
variance and \(\arctan x\ne0\) for \(x\ne0\). The law of large numbers
gives \(\|h^{(1)}(0)\|_2^2/n\to m_1\). Conditional on \(h^{(1)}(0)\),
the second-layer preactivations are independent Gaussians of variance
\(\|h^{(1)}(0)\|_2^2/n\). The conditional variance of the empirical
average of their squared activations is at most \(a^4/n\).
Its conditional mean is a continuous function of that variance,
by dominated convergence. Consequently
\(\|h^{(2)}(0)\|_2^2/n\to m_2\) in probability.
The identical argument conditioning on the second-layer activations
gives \(\|h^{(3)}(0)\|_2^2/n\to m_3\).

For either initial hidden matrix, a \(1/4\)-net of the Euclidean unit
sphere has at most \(9^n\) points. The operator norm is at most twice
the largest absolute bilinear form over two such nets. Each fixed
bilinear form has law \(N(0,1/n)\), so
\[
 \mathbb P(\|W^{(\ell)}(0)\|_{\rm op}>M)
 \le 2\,9^{2n}e^{-nM^2/8},\qquad \ell=2,3.
\]
In particular \(M_2=M_3=10\) bounds both norms with probability tending
to one. Also
\[
 \mathbb E\left[\frac{\|W^{(4)}(0)\|_2^2}{n}\right]=n^{-2},
\]
so its normalized Euclidean norm tends to zero in probability.
Apply the small-readout theorem with
\(b=\sqrt{m_3}/2\), the two fixed bounds 10, and the resulting fixed
positive \(\varepsilon_0\). All its hypotheses hold together with
probability tending to one. On that event its conclusions hold for
every physical time \(t\ge0\), with the width-independent kernel
lower bound \(k_0=m_3/16\). This is a finite-width optimization theorem;
it does not assume any infinite-width trained-state limit.

## Lower-layer second moments and backward energy

Let \(k_0\) be the applicable readout-kernel lower bound above, and
let \(\widehat M_2,\widehat M_3>0\) bound the hidden operator norms
along the physical trajectory. Such bounds follow from (19)--(20)
and the initial operator norms. Since \(|\arctan x|\le |x|\),
\[
 \frac{\|h^{(2)}\|_2^2}{n}\ge\frac{k_0}{\widehat M_3^2},
 \qquad
 \frac{\|h^{(1)}\|_2^2}{n}
 \ge\frac{k_0}{\widehat M_2^2\widehat M_3^2}.
\]
Indeed \(\|h^{(3)}\|_2\le\widehat M_3\|h^{(2)}\|_2\)
and \(\|h^{(2)}\|_2\le\widehat M_2\|h^{(1)}\|_2\).
These are second-moment bounds, not statements about empirical variance.
The feature action on \([0,s_*]\) equals \(e_0=1-f(0)\).
Using the third parameter block in (6) gives
\[
 \int_0^{s_*}
 \frac{\|(W^{(3)}(s))^{\mathsf T}\delta^{(3)}(s)\|_2^2}{n}\,ds
 \le\frac{\widehat M_3^4 e_0}{k_0}.
\]
This controls integrated squared size, not higher moments or products
with arbitrary perturbation vectors.

These finite-width conclusions do not supply a population stability
estimate: they do not bound the \(L^2\)-multiplier norm of a backpropagated
field, and they do not justify interchanging the width limit and
infinite physical time.
