# Exact finite dynamics and the energy estimate

The conventions are those of [the shared notation](NOTATION.md). This chapter
proves finite identities for arbitrary depth and a fixed dataset. It also proves
global finite-width gradient-flow existence and width-independent finite-horizon
norm bounds. These statements do not by themselves identify an infinite-width
trajectory. No empirical assertion or population approximation is used here.

## 1. Model and learning metric

Fix positive integers `L,m,d,n`, data `(x_a,y_a)` for `1<=a<=m`, and positive
constants `kappa_1,...,kappa_(L+1)`. Use the forward equations in NOTATION.md and
the mean squared loss

\[
\mathcal L_n=\frac1m\sum_{a=1}^m r_{n,a}^2,
\qquad r_{n,a}=f_{n,a}-y_a.
\]

Each activation is a real `C^2` function. The finite state consists of all raw
weight entries. Its gradient flow is `dot theta=-D grad mathcal L_n`, where
the constant diagonal operator `D` multiplies the first and last blocks by
`n kappa_1` and `n kappa_(L+1)`, respectively, and middle block `ell` by
`kappa_ell`. Gradients of matrix functions use the ordinary Frobenius pairing.

Backpropagation gives the exact derivatives

\[
\nabla_{W^{(1)}} f_{n,a}
=\frac{\delta_a^{(1)}x_a^T}{n\sqrt d},\qquad
\nabla_{W^{(\ell)}} f_{n,a}
=\frac{\delta_a^{(\ell)}(h_a^{(\ell-1)})^T}{n}\quad(2\le\ell\le L),
\qquad
\nabla_{W^{(L+1)}} f_{n,a}=\frac{h_a^{(L)}}n.
\tag{1}
\]

To verify (1), differentiate the readout first. Its derivative with respect to
`z_a^(L)` is `delta_a^(L)/n`. At a lower layer, differentiating
`z_a^(ell+1)=W^(ell+1) phi^(ell)(z_a^(ell))` multiplies this derivative by
`diag((phi^(ell))'(z_a^(ell))) (W^(ell+1))^T`, giving the stated backward
recursion. A variation of `W^(ell)` produces
`d z_a^(ell)=d W^(ell) h_a^(ell-1)`; at the first layer it produces
`d W^(1) x_a/sqrt(d)`. Taking their scalar products with `delta_a^(ell)/n`
proves all three formulas.

Consequently the exact physical flow is

\[
\begin{aligned}
\dot W^{(1)}&=-\frac{2\kappa_1}{m\sqrt d}
  \sum_a r_{n,a}\delta_a^{(1)}x_a^T,\\
\dot W^{(\ell)}&=-\frac{2\kappa_\ell}{mn}
  \sum_a r_{n,a}\delta_a^{(\ell)}(h_a^{(\ell-1)})^T
  &&(2\le\ell\le L),\\
\dot W^{(L+1)}&=-\frac{2\kappa_{L+1}}m
  \sum_a r_{n,a}h_a^{(L)}.
\end{aligned}
\tag{2}
\]

Exact GD of step `eta` adds `eta` times the right side of (2), with every
quantity evaluated at the same pre-update state. Recomputing one block before
updating the next would be a different algorithm.

## 2. Raw kernel blocks and dissipation

Define the mobility-weighted block kernel by
`K_(n,ab)^(ell)=<grad_(W^(ell)) f_(n,a),D_ell grad_(W^(ell)) f_(n,b)>`.
The identity `<u v^T,p q^T>_F=(u^T p)(v^T q)` and (1) give

\[
\begin{aligned}
K_{n,ab}^{(1)}&=\kappa_1\frac{x_a^Tx_b}{d}
                   \frac{(\delta_a^{(1)})^T\delta_b^{(1)}}n,\\
K_{n,ab}^{(\ell)}&=\kappa_\ell
 \frac{(h_a^{(\ell-1)})^T h_b^{(\ell-1)}}n
 \frac{(\delta_a^{(\ell)})^T\delta_b^{(\ell)}}n
 &&(2\le\ell\le L),\\
K_{n,ab}^{(L+1)}&=\kappa_{L+1}
                    \frac{(h_a^{(L)})^T h_b^{(L)}}n.
\end{aligned}
\tag{3}
\]

Each block is positive semidefinite: for any real sample coefficients `c_a`,
its quadratic form is the squared norm of
`D_ell^(1/2) sum_a c_a grad_(W^(ell)) f_(n,a)`.
With `K_n=sum_ell K_n^(ell)`, the chain rule now gives

\[
\dot f_{n,a}=-\frac2m\sum_b K_{n,ab}r_{n,b},\qquad
\frac{d}{dt}\mathcal L_n=-\frac4{m^2}r_n^T K_n r_n
=-\|D^{-1/2}\dot\theta\|_2^2.
\tag{4}
\]

In particular the last equality is the exact weighted energy identity

\[
\mathcal L_n(t)+\int_0^t\left[
 \frac{\|\dot W^{(1)}\|_F^2}{n\kappa_1}
 +\sum_{\ell=2}^{L}\frac{\|\dot W^{(\ell)}\|_F^2}{\kappa_\ell}
 +\frac{\|\dot W^{(L+1)}\|_2^2}{n\kappa_{L+1}}
\right]du=\mathcal L_n(0).
\tag{5}
\]

There is no factor of the residual inside `delta` or inside (3).

## 3. Global finite-width existence

For every finite initial state the flow (2) has a unique solution for all
`t>=0`. Indeed its vector field is locally Lipschitz: the finite composition
defining the loss is `C^2`. The local existence argument is the contraction
mapping for the integral equation on a closed ball of continuous curves, with
time small enough that the locally bounded Lipschitz field maps the ball into
itself and has contraction constant less than one. This also gives uniqueness.

On any interval of this solution, (5) and Cauchy–Schwarz imply

\[
\|D^{-1/2}(\theta(t)-\theta(s))\|_2
\le\sqrt{t-s}\left(\int_s^t
             \|D^{-1/2}\dot\theta(u)\|_2^2du\right)^{1/2}
\le\sqrt{(t-s)\mathcal L_n(0)}.
\tag{6}
\]

If its maximal forward endpoint were a finite `T`, (6) would make `theta(t)`
Cauchy as `t` tends to `T`. The metric in (6) is equivalent to the Euclidean
metric at fixed `n`, since all mobilities are positive. Its limit is a finite
state. The same local contraction construction at that state extends the
solution past `T`, a contradiction. This proves global existence without a
bounded-activation assumption. It does not assert global stability of GD.

For each `t<=T`, applying (6) blockwise gives

\[
\frac{\|W^{(1)}(t)-W^{(1)}(0)\|_F}{\sqrt n}
\le\sqrt{\kappa_1T\mathcal L_n(0)},\quad
\|W^{(\ell)}(t)-W^{(\ell)}(0)\|_F
\le\sqrt{\kappa_\ell T\mathcal L_n(0)},\quad
\frac{\|W^{(L+1)}(t)-W^{(L+1)}(0)\|_2}{\sqrt n}
\le\sqrt{\kappa_{L+1}T\mathcal L_n(0)}.
\tag{7}
\]

The middle inequality applies to `2<=ell<=L`. It also bounds the operator
norm of each trained middle increment, since operator norm is at most
Frobenius norm. For arbitrary `s<t`, the corresponding bounds hold with
`T` replaced by `t-s`; thus these parameter paths have a uniform square-root
modulus when initial loss is uniformly bounded.

## 4. What is uniform in width

Suppose now the first derivatives of all activations are bounded, the fixed
inputs have bounded RMS norm, and the initial first/readout RMS norms and
middle operator norms are at most a constant independent of `n`. Assume also
`mathcal L_n(0)<=C`. Then on every finite `[0,T]` all preactivation,
activation and backward-vector RMS norms, and every entry of (3), are bounded
by a finite constant independent of `n`.

Here is the complete induction. From (7) the first Frobenius norm divided by
`sqrt(n)`, readout RMS and middle operator norms are bounded. Therefore

\[
\frac{\|z_a^{(1)}\|_2}{\sqrt n}
\le\frac{\|W^{(1)}\|_F}{\sqrt n}\frac{\|x_a\|_2}{\sqrt d},\qquad
\frac{\|z_a^{(\ell)}\|_2}{\sqrt n}
\le\|W^{(\ell)}\|_{\rm op}
       \frac{\|h_a^{(\ell-1)}\|_2}{\sqrt n}.
\]

If `b_ell=sup |(phi^(ell))'|`, the fundamental theorem of calculus gives
`|phi^(ell)(z)|<=|phi^(ell)(0)|+b_ell |z|`. The triangle inequality transfers
each preactivation RMS bound to an activation RMS bound and closes the forward
induction. The reverse induction is

\[
\frac{\|\delta_a^{(L)}\|_2}{\sqrt n}
\le b_L\frac{\|W^{(L+1)}\|_2}{\sqrt n},\qquad
\frac{\|\delta_a^{(\ell)}\|_2}{\sqrt n}
\le b_\ell\|W^{(\ell+1)}\|_{\rm op}
               \frac{\|\delta_a^{(\ell+1)}\|_2}{\sqrt n}.
\]

Cauchy–Schwarz in each pairing in (3) proves the kernel-entry bounds. The
depth is fixed; this argument supplies no depth-uniform constants.

These initial bounds hold with probability tending to one for the independent
Gaussian initialization in NOTATION.md. First-block squared RMS is a sum of
`nd` Gaussian squares divided by `n` and tends to `d` by the elementary law
of large numbers; stored-readout squared RMS tends to zero. For a middle
matrix, a `1/4`-net of the unit sphere has at most `9^n` points, by disjoint
radius-`1/8` balls and a volume comparison. Approximating both vectors in a
bilinear form by net points bounds the operator norm by twice the largest net
bilinear form. Each fixed form is `N(0,1/n)`. The Gaussian exponential bound
and a union bound give

\[
\mathbb P(\|W^{(\ell)}(0)\|_{\rm op}>M)
\le 2\,9^{2n}e^{-nM^2/8}.
\]

Choose fixed sufficiently large `M` and use a union bound over the fixed depth.
The forward induction at time zero then bounds the initial activations, and
`|f_(n,a)(0)|<=||W^(L+1)(0)||_2 ||h_a^(L)(0)||_2/n` bounds initial loss.
This supplies the claimed high-probability initial event.

Uniform RMS bounds do not control multiplication by an unbounded coordinate
function in the population space. Thus (5)–(7) establish useful a priori
estimates but do not replace the source-identification and response-stability
proofs needed for a nonlinear population theorem.
