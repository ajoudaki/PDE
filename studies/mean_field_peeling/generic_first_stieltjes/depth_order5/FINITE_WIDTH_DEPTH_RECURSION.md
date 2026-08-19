# Exact finite-width depth recursion through order five

**Status:** exact algebra at every finite width.  This note contains no
large-width or Gaussian-normal-form claim.

Let \(M^\ell=W^\ell/\sqrt n\) for \(2\leq\ell\leq H\).  Along the exact
feature-ascent characteristic

\[
\dot\theta(t)=n\nabla f_n(\theta(t)),\qquad \theta(0)=\theta,
\]

write ordinary Taylor series

\[
z^\ell(t)=\sum_{k=0}^5z^\ell_k t^k,\quad
h^\ell(t)=\sum_{k=0}^5h^\ell_k t^k,\quad
a(t)=\sum_{k=0}^5a_k t^k,\quad
M^\ell(t)=\sum_{k=0}^5M^\ell_k t^k.
\]

For a scalar series \(x(t)=x_0+\sum_{k\geq1}x_kt^k\), define

\[
\Phi^{(r)}_k[x]
=\sum_{m=0}^k\frac{\phi^{(r+m)}(x_0)}{m!}
\!\!\sum_{\substack{i_1+\cdots+i_m=k\\i_j\geq1}}
x_{i_1}\cdots x_{i_m}.
\tag{1}
\]

The \(m=0\) inner sum is one when \(k=0\) and zero otherwise.  Formula (1)
is applied coordinatewise.  Put

\[
h^\ell_k=\Phi^{(0)}_k[z^\ell],
\qquad p^\ell_k=\Phi^{(1)}_k[z^\ell].
\tag{2}
\]

The exact forward convolution is

\[
z^\ell_k=\sum_{r+s=k}M^\ell_rh^{\ell-1}_s,
\qquad 2\leq\ell\leq H.
\tag{3}
\]

Define reverse preactivation sources by

\[
\delta^H_k=\sum_{r+s=k}a_rp^H_s,
\tag{4}
\]

\[
b^\ell_k=\sum_{r+s=k}(M^{\ell+1}_r)^T\delta^{\ell+1}_s,
\qquad
\delta^\ell_k=\sum_{r+s=k}p^\ell_r b^\ell_s,
\qquad 1\leq\ell<H.
\tag{5}
\]

After the degree-\(k\) forward and reverse passes are known, exact integration
of the parameter ODE gives

\[
a_{k+1}=\frac{h^H_k}{k+1},
\tag{6}
\]

\[
M^\ell_{k+1}
=\frac1{(k+1)n}\sum_{r+s=k}\delta^\ell_r(h^{\ell-1}_s)^T,
\qquad 2\leq\ell\leq H,
\tag{7}
\]

\[
z^1_{k+1}=\frac{Q^0}{k+1}\delta^1_k.
\tag{8}
\]

Finally,

\[
f_{n,k}=\frac1n\sum_{r+s=k}a_r^Th^H_s,
\qquad
D_n^kf_n=k!\,f_{n,k}.
\tag{9}
\]

Equations (1)--(9) are triangular in \(k\): one forward pass, one reverse
pass, and one parameter integration advance the coefficient degree by one.
They hold for every \(H,n\) and in particular produce \(D_n^5f_n\) without
forming fifth-order parameter tensors.

## Readout parity

Let \(S\) negate the initialized readout and leave every other parameter
fixed.  Then \(f_n\circ S=-f_n\).  Because \(S\) is orthogonal,

\[
(D_ng)\circ S=-\varepsilon\,D_ng
\quad\text{whenever}\quad g\circ S=\varepsilon g.
\]

Starting with \(\varepsilon=-1\) gives

\[
(D_n^kf_n)\circ S=(-1)^{k+1}D_n^kf_n.
\tag{10}
\]

Thus, under the symmetric Gaussian readout law,

\[
\mathbb E f_n=\mathbb E D_n^2f_n=\mathbb E D_n^4f_n=0
\tag{11}
\]

exactly at every width and every hidden depth.

## What remains for the Gaussian normal form

Only the initialized matrices \(M^\ell_0\) are dense random operators.
At fixed order five, each one appears in six chronological forward uses and
five chronological transpose uses.  Gaussianizing (3) and (5) must retain:

1. the fresh Gaussian sector for each use;
2. every response to an earlier opposite-orientation use;
3. every explicit rank-one update (7);
4. all covariances among same-orientation fresh sectors.

This is a finite triangular registry per matrix at fixed Taylor order.
Whether its contracted state is local in depth, and how quickly its fully
expanded terminal moment polynomial grows with \(H\), are separate questions
addressed by the depth-order-five compiler and hostile audit.
