# Exact finite dynamics and the energy estimate

The conventions are those of [the shared notation](NOTATION.md). This chapter
proves finite identities for arbitrary depth and a fixed dataset. It also proves
global finite-width gradient-flow existence and width-independent finite-horizon
norm bounds. These statements do not by themselves identify an infinite-width
trajectory. No empirical assertion or population approximation is used here.

Sections 5–7 give separate one-sample, two-hidden-layer quadratic/identity
and differentiated RMS models: exact gradients, kernels, Lax identities,
balance laws and finite physical-flow continuation. Their state matrices
retain width; no population or spectrum-only closure is asserted.

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

## 5. Two-layer quadratic and identity reductions

Fix a width `n>=1`, one datum `x=1` in dimension one, a real label `y`, and
two hidden layers. Write the stored parameters as
`u=W^(1) in R^n`, `B=W^(2) in R^(n by n)`, and
`a=W^(3) in R^n`; the first matrix is identified with its sole column.
All three mobility multipliers are one. The parameter metric is

\[
 \frac{\|du\|_2^2}{n}+\|dB\|_F^2+\frac{\|da\|_2^2}{n}.
 \tag{8}
\]

In particular `B` already is the stored, scaled matrix: there is no further
width factor in `Bh`. If one instead stores `\mathsf W=\sqrt n B`,
(8) is `n^{-1}` times the Euclidean metric on `(u,\mathsf W,a)`.
The residual and loss are `r=f-y` and `\mathcal L=r^2`.
A prime below means the metric gradient of the output (unit feature ascent),
and the physical flow is always

\[
 \dot\theta=-2r\theta'.
 \tag{9}
\]

Thus the prime is an algebraic vector field. Its integral curves need not be
global, and no positive or invertible feature clock is assumed. The displayed
physical equations hold also when `r=0` or when the label has either sign.
No initialization distribution is assumed; in particular, no readout is reset
or replaced by its limiting value.

Let `Q(z)=z^2` and `I(z)=z`, coordinatewise. The strings `QI`, `IQ` and `QQ`
specify the first and second hidden activations, in that order. Set
`h=phi^(1)(u)`, `z=Bh`, `v=phi^(2)(z)`, `f=a^T v/n`.
The exact output-ascent fields and scalar kernel blocks are as follows;
the block order is first layer, middle matrix, readout.

\[
\begin{array}{c|c|c|c|c}
 &\text{auxiliary fields}&u'&B'&a'\\ \hline
QI&q=B^Ta&2u\odot q&a h^T/n&z\\
IQ&b=a\odot z,\ q=B^Tb&2q&2b h^T/n&z^2\\
QQ&b=a\odot z,\ q=B^Tb&4u\odot q&2b h^T/n&z^2
\end{array}
\tag{10}
\]

\[
\begin{array}{c|c|c|c}
 &K_1&K_2&K_3\\ \hline
QI&4(u^2)^Tq^2/n&\|a\|_2^2\|h\|_2^2/n^2&\|z\|_2^2/n\\
IQ&4\|q\|_2^2/n&4\|b\|_2^2\|h\|_2^2/n^2&\|z^2\|_2^2/n\\
QQ&16(u^2)^Tq^2/n&4\|b\|_2^2\|h\|_2^2/n^2&\|z^2\|_2^2/n
\end{array}
\tag{11}
\]

Squares and products between vectors in these formulas are coordinatewise.
To verify the first row, differentiate `f=a^TB(u^2)/n` to obtain
`df=z^T da/n+a^T(dB)h/n+(2u\odot B^Ta)^Tdu/n`.
The inverse metric (8) multiplies the `u,a` derivatives by `n` and leaves
the matrix derivative unchanged. For the other two rows,
`df=(z^2)^Tda/n+2(a\odot z)^T[(dB)h+Bdh]/n`, with
`dh=du` for `IQ` and `dh=2u\odot du` for `QQ`. This proves (10).
Taking the squared norm of each block of (10) in (8), using
`\|bc^T/n\|_F^2=\|b\|_2^2\|c\|_2^2/n^2`, proves (11).
Consequently, with `K=K_1+K_2+K_3`,

\[
 f'=K,\qquad \dot f=\dot r=-2rK,\qquad
 \dot{\mathcal L}=-4r^2K.
 \tag{12}
\]

### Isometric block matrices and the two Lax identities

For block operators, pass each neuron vector to ordinary Euclidean
coordinates by `\widehat v=v/\sqrt n`. Indeed
`\widehat v^T\widehat w=v^Tw/n`. A matrix acting between two neuron
spaces retains its numerical entries under these isometries; a map
`c\mapsto ca` from a scalar space has column `\widehat a`; and the
functional `v\mapsto h^Tv/n` has row `\widehat h^T`.
Thus transpose in the following matrices is ordinary Euclidean transpose.
This specifies all block weights, including the scalar blocks.

For `QI` define

\[
 \mathsf Q=[\widehat a\ \ B],\qquad
 S=\begin{pmatrix}0&\widehat h^T\\\widehat h&0\end{pmatrix},
 \quad J=\operatorname{diag}(-1,I_n),\quad
 \mathsf L=J\mathsf Q^T\mathsf Q.
 \tag{13}
\]

Equation (10) gives `\mathsf Q'=\mathsf Q S`: its first column is
`B\widehat h=\widehat z`, and the remaining columns are
`\widehat a\widehat h^T=a h^T/n`. Since `S^T=S` and `JS=-SJ`,

\[
 \mathsf L'=J(S\mathsf Q^T\mathsf Q+\mathsf Q^T\mathsf Q S)
            =\mathsf L S-S\mathsf L=[\mathsf L,S].
 \tag{14}
\]

The lower block of `\mathsf L e_0` is `\widehat q`, and
`h'=4h\odot q`. Hence `(h,\mathsf L)` has an exact autonomous
current-state equation on the states obtained from raw parameters. Its
output is `f=\widehat q^T\widehat h`. Writing
`g=\|a\|_2^2/n` and `C=B^TB`, which are respectively the top-left and
bottom-right blocks of `J\mathsf L`, its kernel is

\[
 K=\frac{h^TCh}{n}+g\frac{\|h\|_2^2}{n}
                  +4\frac{h^Tq^2}{n}.
 \tag{15}
\]

The raw current operator `BB^T-aa^T/n` is also conserved: differentiating
the two products with (10) gives the same matrix
`(az^T+za^T)/n` in each case.

For `IQ` use a scalar as the last block and define

\[
 \mathsf P=\begin{pmatrix}B\\\widehat h^T\end{pmatrix},\qquad
 S=\begin{pmatrix}0&\widehat b\\\widehat b^T&0\end{pmatrix},
 \quad J=\operatorname{diag}(I_n,-1),\quad
 \mathsf L=J\mathsf P\mathsf P^T.
 \tag{16}
\]

Here `\mathsf P'=2S\mathsf P`: the top block is
`2\widehat b\widehat h^T=2b h^T/n`, and the last row is
`2\widehat b^TB=2\widehat q^T`. Differentiating, and again using
`JS=-SJ`, gives

\[
 \mathsf L'=2[\mathsf L,S].
 \tag{17}
\]

The upper block of `\mathsf L e_*` is `\widehat z`; the bottom-right
block of `J\mathsf L` is `\rho_h=\|h\|_2^2/n`, and its top-left block is
`C=BB^T`. Therefore `(a,\mathsf L)` closes on raw-image states:
`a'=z^2`, `b=a\odot z`, `f=a^Tz^2/n`, and

\[
 K=\frac{\|z^2\|_2^2}{n}
       +4\rho_h\frac{\|b\|_2^2}{n}+4\frac{b^TCb}{n}.
 \tag{18}
\]

These claims are exact block identities, not a reduction to a fixed number
of scalar coordinates. Their block matrices still have size `n+1`.
Multiplying their entire vector fields by `-2r` returns both systems to
physical time, including their output and kernel readouts.

For completeness the commutator laws do imply isospectrality without
assuming that `\mathsf L` is self-adjoint. Along a raw solution, either
physical law has the form `\dot{\mathsf L}=[\mathsf L,F(t)]`, with
`F=-2rS` for `QI` and `F=-4rS` for `IQ`. On any compact interval where
the raw solution exists, `F` is continuous and bounded. The integral
equation for `U'=-FU`, `U(0)=I`, has a unique solution: successive
integrations have norm bounded by `(Mt)^k/k!` when `\|F\|<=M`, so the
series converges uniformly, solves the equation, and gives uniqueness by
the same iterated difference bound. The equation `V'=VF`, `V(0)=I` has
the same construction. Differentiating `VU` gives zero, hence `VU=I`;
in finite dimension this also gives `UV=I`. Differentiation now yields
`(V\mathsf L U)'=0`, so
`\mathsf L(t)=U(t)\mathsf L(0)U(t)^{-1}`. Similarity preserves the
characteristic polynomial because
`det(\lambda I-U\mathsf L U^{-1})=det(\lambda I-\mathsf L)`.
The same argument applies to feature ascent on its interval of existence.

### The spectrum does not determine the instantaneous output velocity

For `QI` take `n=3`, `u=(1,\sqrt2,\sqrt3)`, `B=I_3`, and either

\[
 a_1=(1,0,0),\qquad a_2=(1/3,-2/3,2/3).
 \tag{19}
\]

Both states have `h=(1,2,3)`, `\|a_i\|_2^2=1`, and `a_i^Th=1`.
Thus their output is `f=1/3`. Put
`d=(1,1,-1)^T` and `O=I-2dd^T/3`. Since `d^Td=3`, multiplication
gives `O^TO=I`, `Oa_1=a_2`, and `Oh=h`. In isometric coordinates the
Gram matrix in (13) is

\[
 \mathsf Q_i^T\mathsf Q_i=
 \begin{pmatrix}1/3&a_i^T/\sqrt3\\a_i/\sqrt3&I_3\end{pmatrix}.
\]

Conjugating the first such Gram by `diag(1,O)` gives the second.
That conjugating matrix commutes with `J`; hence the two `\mathsf L_i`
are orthogonally similar and have the same spectrum. Nevertheless
`h^Ta_1^2/3=1/3` and `h^Ta_2^2/3=7/9`. Formula (15) gives
`K_1=68/9` and `K_2=28/3`, a difference of `16/9`.
For any common label other than `1/3`, (12) gives different instantaneous
physical output speeds. Thus retaining the spectrum, the actual current
`h`, and the output does not give a restart-sufficient state. This says
nothing against retaining the full operators in (13) or (16).

### Both squares: row and column balances

For `QQ`, (10) gives `h'=8h\odot q`. With the raw auxiliary matrix
`\mathsf W=\sqrt n B`, each row and column obeys

\[
 \left(n\sum_jB_{ij}^2-2a_i^2\right)'=0,\qquad
 \left(n\sum_iB_{ij}^2-\tfrac12u_j^2\right)'=0.
 \tag{20}
\]

Indeed the row derivative of `n\sum_j B_{ij}^2` is
`4b_i\sum_jB_{ij}h_j=4a_i z_i^2`, which cancels `(2a_i^2)'`.
The column derivative is `4h_j\sum_iB_{ij}b_i=4u_j^2q_j`, which
cancels `(u_j^2/2)'`. Equation (9) preserves these zero derivatives in
physical time. The identities assert no common block-Gram Lax law for `QQ`.

## 6. Differentiated RMS normalization at finite width

Keep exactly the finite metric, data and trained parameters in (8)–(9), but
now normalize the vector after each coordinatewise square. Fix
`\varepsilon>0`, and put

\[
 p=u^2,\quad \alpha=\sqrt{\|p\|_2^2/n+\varepsilon},\quad
 h=p/\alpha,\qquad
 z=Bh,\quad w=z^2,\quad
 \beta=\sqrt{\|w\|_2^2/n+\varepsilon},\quad v=w/\beta,
 \quad f=a^Tv/n.
 \tag{21}
\]

This is a different architecture from applying a scalar activation at each
coordinate: the denominators depend on all neurons. They are differentiated
as part of the network. Every parameter block is trained.

For any vector `x`, let
`N_\varepsilon(x)=x/\sigma`, `\sigma^2=\|x\|_2^2/n+\varepsilon`.
Direct differentiation gives

\[
 d\sigma=\frac{x^Tdx}{n\sigma},\qquad
 DN_\varepsilon(x)[dx]=\sigma^{-1}
       \left(I-\frac{N_\varepsilon(x)N_\varepsilon(x)^T}{n}\right)dx.
 \tag{22}
\]

Write `\Pi_h=I-hh^T/n` and `\Pi_v=I-vv^T/n`. These symmetric
matrices are positive definite, not generally idempotent. For a nonzero
`x`, the parenthesis in (22) is the identity perpendicular to `x`, and
has eigenvalue `1-\|x\|_2^2/(n\sigma^2)=\varepsilon/\sigma^2` on
its span. At `x=0` it is `I`. In particular both denominators in (21)
are at least `\sqrt\varepsilon`.

Define the current backward vectors

\[
 c=\Pi_v a=a-fv,\qquad b=\frac2\beta z\odot c,
 \qquad q=B^Tb,\qquad \widetilde q=\Pi_hq.
 \tag{23}
\]

The full differential is

\[
 df=\frac{v^Tda}{n}+\frac{b^T(dB)h}{n}
                      +\frac{(2u\odot\widetilde q)^Tdu}{n\alpha}.
 \tag{24}
\]

To obtain it, (22) first gives `a^Tdv/n=c^Tdw/(n\beta)` and
`dw=2z\odot dz`; next `dz=(dB)h+Bdh`,
`dh=\Pi_h dp/\alpha`, and `dp=2u\odot du`.
Symmetry of `\Pi_h` transfers it to `q`, giving (24). Therefore

\[
 a'=v,\qquad B'=b h^T/n,\qquad u'=2u\odot\widetilde q/\alpha,
 \tag{25}
\]
\[
 K_1=\frac{4\|u\odot\widetilde q\|_2^2}{n\alpha^2}
     =\frac4\alpha\frac{h^T\widetilde q^2}{n},\quad
 K_2=\frac{\|h\|_2^2\|b\|_2^2}{n^2},\quad
 K_3=\frac{\|v\|_2^2}{n}.
 \tag{26}
\]

The first equality and the squared norm of `B'` use exactly (8).
All terms are nonnegative, and (12) again holds for their sum. In particular
`r(t)=r(0)\exp(-2\int_0^tK(s)\,ds)` on every finite physical interval:
differentiate `r(t)\exp(2\int_0^tK)` to check the identity, including
`r(0)=0`. The residual keeps its sign.

### Feature equations, balances, and the finite reduced state

Let `\rho_h=\|h\|_2^2/n`. Differentiating (21) using (25) gives

\[
 p'=4p\odot\widetilde q/\alpha,\qquad
 \alpha'=4(h^2)^T\widetilde q/n,\qquad
 h'=\frac4\alpha\Pi_h(h\odot\widetilde q),
 \tag{27}
\]
\[
 z'=\rho_h b+B h',\qquad w'=2z\odot z',\qquad
 \beta'=\frac{2(z^3)^Tz'}{n\beta},\qquad
 v'=\frac2\beta\Pi_v(z\odot z').
 \tag{28}
\]

For example `\alpha'=h^Tp'/n=4(h^2)^T\widetilde q/n`, and
`h'=\Pi_h p'/\alpha` gives (27). The rank-one formula for `B'`
gives `B'h=\rho_h b`, which proves the first equation of (28); (22) proves
the remaining ones. One useful exact scalar contraction is

\[
 \frac{h^Tq}{n}=\frac{z^Tb}{n}
   =\frac{2\varepsilon f}{\beta^2},\qquad
 \widetilde q=q-\frac{2\varepsilon f}{\beta^2}h.
 \tag{29}
\]

Indeed `z^Tb/n=(2/\beta)(w^Ta/n-f w^Tv/n)` and
`w=\beta v`, `\|v\|_2^2/n=1-\varepsilon/\beta^2` give (29).
The row and column balance laws now have signed drifts:

\[
 \left(n\sum_jB_{ij}^2-2a_i^2\right)'=-4f v_i^2,
 \qquad
 \left(n\sum_iB_{ij}^2-\tfrac12u_j^2\right)'
       =\frac{4\varepsilon f}{\beta^2}h_j^2.
 \tag{30}
\]

For the row, the first derivative is `2b_i z_i=4v_i(a_i-fv_i)`;
subtract `4a_iv_i`. For the column it is `2h_jq_j`; subtract
`u_ju'_j=2h_j\widetilde q_j`, and then use (29). Multiplication by `-2r` converts
both signed drifts to physical time. The row drift does not generally
vanish when epsilon is set to zero at a state with nonzero denominators.
No epsilon-zero dynamics is part of the theorem.

The output-relevant bottom coordinate can be represented by `h`:

\[
 \rho_h=1-\varepsilon/\alpha^2<1,\qquad
 \alpha(h)=\sqrt{\varepsilon/(1-\rho_h)},\qquad
 \mathcal A_h=\frac4{\alpha(h)}\Pi_h\operatorname{diag}(h)\Pi_h.
 \tag{31}
\]

On a raw-image state `h>=0`; thus `\mathcal A_h` is positive
semidefinite, since
`x^T\mathcal A_h x=(4/\alpha)\sum_jh_j(\Pi_h x)_j^2>=0`.
Equations (27) and (26) become `h'=\mathcal A_hq` and
`K_1=q^T\mathcal A_hq/n`.
With a fixed finite matrix `B_0` and current increment `E=B-B_0`, the
reduced state `(a,h,E)` evolves by

\[
 z=(B_0+E)h,\quad v=N_\varepsilon(z^2),\quad f=a^Tv/n,
 \quad b=\frac2\beta z\odot(a-fv),
 \qquad
 a'=v,\quad E'=b h^T/n,\quad h'=\mathcal A_h(B_0+E)^Tb.
 \tag{32}
\]

This system is autonomous and restartable for states reached from finite
raw initial parameters. Here is the precise justification. Its vector
field is smooth on the open set `\|h\|_2^2/n<1`, because `\alpha(h)`
is smooth there and `\beta>=\sqrt\varepsilon`. A raw solution projects
to (32) by (27). Its reached states have `h>=0` and strict `\rho_h<1`.
The coordinate sign of `u_j` is preserved along any finite raw physical
interval: (25) and (9) have the form `\dot u_j=c_j(t)u_j` with continuous
`c_j`, whence `u_j(t)=u_j(t_0)\exp(\int_{t_0}^t c_j)` by
differentiation. In particular zero coordinates remain zero. At a reached
time, recover a finite raw lift from
`u_j=\operatorname{sign}(u_j(t_0))\sqrt{\alpha(h)h_j}`,
with zero when `h_j=0`, and `B=B_0+E`. The recovered squared vector
indeed has normalizer `\alpha(h)` because
`\alpha(h)^2\rho_h+\varepsilon=\alpha(h)^2`.

Each choice of the nonzero signs gives a raw lift. Any such lift projects
to the same locally unique reduced solution: local uniqueness follows
from the smooth reduced vector field by the integral-equation contraction
on a small closed ball inside `\rho_h<1`. The raw global physical continuation
proved below provides its continuation at every later finite time and
preserves `h>=0,\rho_h<1` there. Consequently the reduced future and its output
do not depend on the recovered signs. This argument concerns reached raw
states; it claims neither a solution on `\rho_h=1` nor global feature-ascent
existence. The source matrix `B_0` still has size `n` and is not a
width-independent Gaussian operator construction.

## 7. Global finite physical flow for these models

For each fixed width and finite initial state, all models above have a
unique physical solution for every `t>=0`. The mixed polynomial losses are
smooth, and the normalized loss is smooth because epsilon is positive.
Thus their physical vector fields are locally Lipschitz. Local existence
and uniqueness follow by contraction for the integral equation on a closed
ball of continuous paths: choose its time length so the field stays in
the ball and its Lipschitz constant times that length is less than one.
No distributional initialization hypothesis enters this argument.

For any solution interval, (8), (9), and `f'=K` give

\[
 \frac{\|\dot u\|_2^2}{n}+\|\dot B\|_F^2+
       \frac{\|\dot a\|_2^2}{n}=4r^2K=-\dot{\mathcal L}.
 \tag{33}
\]

After integration, Cauchy–Schwarz in the metric (8) yields, for `s<t`,

\[
 \left(\frac{\|u(t)-u(s)\|_2^2}{n}
       +\|B(t)-B(s)\|_F^2
       +\frac{\|a(t)-a(s)\|_2^2}{n}\right)^{1/2}
 \le\sqrt{(t-s)(\mathcal L(s)-\mathcal L(t))}
 \le\sqrt{(t-s)\mathcal L(0)}.
 \tag{34}
\]

If a maximal forward solution ended at finite `T`, (34) would make its
parameters Cauchy as `t` increased to `T`. For fixed `n` this metric is
equivalent to the Euclidean metric, so they have a finite limit. Local
existence at that limit extends the solution beyond `T`; local uniqueness
joins the extensions. This contradiction proves the assertion. Equation
(34) controls normalized parameter displacements, not coordinate maxima,
kernel uniform integrability, a population limit, or arbitrary-step GD.

## 8. Frozen quadratic reduction and joint initial layers

The results in Sections 8–9 concern one sample, `d=m=1`, `x_1=y_1=1`,
and two hidden layers. They use **order-one stored readout initialization**,
not the small stored readout used in the nonlinear limit theorems. They
separate a joint width/step obstruction for a frozen-bottom quadratic model
from a finite-width classical ReLU obstruction and a positive local
compactness theorem for actual ReLU Euler outputs. None replaces a theorem
about genuinely nonlinear training on correlated data.

Write `u=W^(1)`, `W=W^(2)` and `a=W^(3)` for finite arrays of sizes `n`,
`n` by `n`, and `n`. Thus

\[
 h^{(1)}=\phi(u),\qquad z^{(2)}=Wh^{(1)},\qquad
 h^{(2)}=\phi(z^{(2)}),\qquad f_n=a^Th^{(2)}/n.
\]

In Sections 8–9 the loss is the **half-square loss**
\(\ell_n=(f_n-1)^2/2\), and the residual remains \(r_n=f_n-1\).
The mobilities of the three stored blocks are \((n,1,n)\). Time is the
physical clock for this half loss. For the book's full one-sample squared
loss the same trajectories run twice as fast: an Euler step \(\eta\) for
the full loss equals a step \(2\eta\) here.

### 8.1 Exact frozen-feature reduction and arbitrary joint steps

First fix any deterministic bottom feature vector \(h^{(1)}\in\mathbb R^n\)
and train only \(W,a\), using the top activation \(\phi(z)=cz^2\), where
\(c=1/\sqrt3\). Put

\[
 Q=\frac{\|h^{(1)}\|_2^2}{n},\qquad z=Wh^{(1)},\qquad
 f_n=\frac c n\sum_{i=1}^n a_i z_i^2.
\]

The parameter derivatives are

\[
 \frac{\partial f_n}{\partial a_i}=\frac c n z_i^2,
 \qquad
 \frac{\partial f_n}{\partial W_{ij}}=
       \frac{2c}{n}a_i z_i h_j^{(1)}.
\]

Consequently an exact simultaneous raw Euler step of size \(\eta>0\),
with \(s=\eta(1-f_n)=-\eta r_n\), gives the closed update

\[
 a_i^+=a_i+cs z_i^2,\qquad
 z_i^+=z_i+2cQs a_i z_i.                              \tag{8.1}
\]

Indeed \(W^+=W+(2cs/n)(a\odot z)(h^{(1)})^T\), and multiplying by the
unchanged \(h^{(1)}\) gives the second equation. Both right sides use the
same pre-update state; there is no continuous-flow approximation in
(8.1). The raw kernel for the two trained blocks is also exactly

\[
 K_n=\frac{c^2}{n}\sum_i z_i^4+
            \frac{4c^2Q}{n}\sum_i a_i^2z_i^2.          \tag{8.2}
\]

The first term is \(n\|\nabla_a f_n\|_2^2\), and the second is
\(\|\nabla_Wf_n\|_F^2\). Thus the associated smooth finite flow satisfies
\(\dot f_n=(1-f_n)K_n\) and \(\dot\ell_n=-(1-f_n)^2K_n\).
These identities hold for every finite frozen vector, including \(Q=0\).
They assert neither a discrete energy inequality nor population convergence.

For the probabilistic theorem, specialize to

\[
 h_j^{(1)}=cu_j^2,\qquad u_j\sim N(0,1),\qquad
 W_{ij}(0)\sim N(0,1/n),\qquad a_i(0)\sim N(0,1),     \tag{8.3}
\]

with all displayed initialization variables independent. The bottom vector
is frozen permanently. Conditional on it, the pairs
\((a_i(0),z_i(0))\) are independent across rows, with independent coordinates
of laws \(N(0,1)\) and \(N(0,Q_n)\), where
\(Q_n=n^{-1}\sum_j c^2u_j^4\).

**Frozen-bottom joint-step theorem.** Let \(\eta_n>0\) be any deterministic
sequence tending to zero, without a restriction on its rate relative to
\(n\). Iterate (8.1), recomputing the loss residual at every step. For
\(0<\delta<1\), define

\[
 \tau_n(\delta)=\eta_n\inf\{k\ge0:|f_n^k|\ge\delta\},
 \qquad \inf\varnothing=+\infty.
\]

Then \(\tau_n(\delta)\to0\) in probability. With the raw parameters
linearly interpolated and the network and half loss recomputed, both the
predictor and loss undergo a fixed change at times tending to zero.
They cannot converge in probability uniformly on any \([0,T]\), \(T>0\),
to continuous paths with their initialized traces \(0\) and \(1/2\).

The proof controls all negative rows from their initial values, without a
union bound over steps, and uses a fixed favorable Gaussian tail block for
the positive growth.

First, the elementary Gaussian identities \(\mathbb EG^4=3\) and
\(\mathbb EG^8=105\) give

\[
 \mathbb E Q_n=1,\qquad
 \operatorname{Var}(Q_n)=\frac{32}{3n},\qquad
 \mathbb E(f_n^0)^2=\frac{\mathbb E Q_n^2}{n}
   =\frac1n\left(1+\frac{32}{3n}\right).              \tag{8.4}
\]

For the last identity condition on the bottom vector, use independence of
the centered readouts to eliminate cross terms, and use
\(\mathbb E[z_i(0)^4\mid h^{(1)}]=3Q_n^2\) and \(3c^2=1\).
Thus \(Q_n\to1\) and \(f_n^0\to0\) in probability.

Fix \(T>0\) and suppose no grid hit occurs through time \(T\). Every
step starting before that time then has

\[
 (1-\delta)\eta_n\le s_k\le(1+\delta)\eta_n.          \tag{8.5}
\]

In particular, each \(a_i^k\) increases. Let
\(a_{i,-}^0=\max\{-a_i^0,0\}\). While \(a_i^k<0\),
\(|a_i^k|\le a_{i,-}^0\), and (8.1) yields

\[
 |z_i^{k+1}|\le |z_i^k|
       \exp\{2cQ_n(1+\delta)\eta_n a_{i,-}^0\}.
\]

If a row is negative at step \(k\), it was negative at every earlier step.
Multiplying these inequalities therefore proves, at all \(k\eta_n\le T\),

\[
 a_i^k(z_i^k)^2\ge
 -a_{i,-}^0(z_i^0)^2
   \exp\{4cQ_n(1+\delta)T a_{i,-}^0\}.               \tag{8.6}
\]

After a row becomes nonnegative, the same inequality holds because its
left side is nonnegative.

On \(Q_n\in[1/2,2]\), write \(z_i^0=\sqrt{Q_n}v_i\). Conditional on the
bottom vector, \(a_i^0,v_i\) are independent standard Gaussians. Define

\[
 B_T=1+4c\,\mathbb E\!\left[
       G_-e^{8c(1+\delta)T G_-}\right],\qquad
 G_-=\max\{-G,0\},\quad G\sim N(0,1).                 \tag{8.7}
\]

This is finite: every polynomial times \(e^{b|G|}\) is integrable, as follows
by completing the square in the Gaussian density. The conditional mean of
\(c a_{i,-}^0(z_i^0)^2e^{4cQ_n(1+\delta)T a_{i,-}^0}\) is at most
\(2c\mathbb E[G_-e^{8c(1+\delta)TG_-}]\), strictly below \(B_T\).
Its conditional second moment is uniformly bounded on \(Q_n\in[1/2,2]\)
by the same Gaussian integrability and \(\mathbb Ev_i^4=3\).
Conditional Chebyshev, followed by (8.4), proves that with probability
tending to one

\[
 \frac c n\sum_i a_{i,-}^0(z_i^0)^2
          e^{4cQ_n(1+\delta)T a_{i,-}^0}\le B_T.       \tag{8.8}
\]

This is one event determined by initialization. By (8.6), on survival it
bounds the total contribution of all currently negative rows below by
\(-B_T\) at every grid time under consideration.

For a fixed number \(b>1\), retain the rows

\[
 \mathcal I_b=\{i:a_i^0\in[b,b+1],\ v_i\in[b,b+1]\},
 \qquad p_b=\Pr\{G\in[b,b+1]\}^2>0.
\]

Conditionally, \(|\mathcal I_b|\) is binomial with parameters \(n,p_b\).
Its variance bound \(np_b(1-p_b)\) shows
\(|\mathcal I_b|/n\ge p_b/2\) with probability tending to one. These rows
remain in the positive quadrant before an output hit. Put
\(\gamma=c(1-\delta)\). On \(Q_n\ge1/2\), (8.1) and (8.5) give, for
\(y_i^k=\min\{a_i^k,z_i^k\}\),

\[
 y_i^{k+1}\ge y_i^k+\gamma\eta_n(y_i^k)^2,
 \qquad y_i^0\ge b/\sqrt2.                            \tag{8.9}
\]

For the scalar recursion \(y^+=y+\gamma\eta_n y^2\), while \(0<y<M\)
and \(\gamma\eta_n M\le1\),

\[
 \frac1y-\frac1{y^+}
 =\frac{\gamma\eta_n}{1+\gamma\eta_n y}
 \ge\frac{\gamma\eta_n}{2}.
\]

The scalar map is increasing on \([0,\infty)\), so it bounds (8.9) below.
Summing reciprocals shows that every selected row reaches level \(M\) no
later than \(2\sqrt2/(\gamma b)+\eta_n\), unless the output already hit.
A row already above \(M\) requires no waiting; after reaching \(M\) it
stays above it while survival continues.

Choose \(b>\max\{1,4\sqrt2/(\gamma T)\}\), and then the finite constant

\[
 M=\left(\frac{2(B_T+2\delta)}{cp_b}\right)^{1/3}.
\]

Both depend on \(T,\delta\), not on \(n\). Eventually
\(\gamma\eta_n M\le1\), and the common level is reached before \(T\).
If no output hit had occurred, (8.8) and the favorable-row count would give

\[
 f_n^k\ge \frac{cp_b}{2}M^3-B_T=2\delta,
\]

a contradiction. The intersection of the three initialization events
\(Q_n\in[1/2,2]\), (8.8), and the favorable-row count has probability
tending to one. Consequently \(\Pr\{\tau_n(\delta)>T\}\to0\). Since this
holds for every \(T>0\), the hitting-time assertion is proved.

On \(|f_n^0|<\delta/2\), continuous raw-parameter interpolation reaches
one of \(\delta,-\delta\) during the first crossing step, at a time no
later than \(\tau_n(\delta)\). At that time its predictor differs from its
initial value by at least \(\delta/2\). Its loss differs from \(1/2\) by
at least \(\delta-\delta^2/2>0\), while its initial loss tends to \(1/2\)
by (8.4). If these paths converged uniformly in probability to a continuous
initialized path, evaluation at these times tending to zero would instead
make both changes vanish. For a random continuous proposed limit the same
argument holds: its modulus of continuity tends to zero almost surely,
and hence in probability. This proves the asserted obstruction.

### 8.2 Freezing a layer supplies no pathwise lower comparison

The theorem just proved does not transfer by deleting the bottom update
from a fully trained trajectory. An exact one-step counterexample explains
why. This paragraph uses the separate deterministic width-one model with
raw activation \(\phi(z)=z^2\), so

\[
 f(a,w,u)=aw^2u^4.
\]

A feature-ascent step of size \(s>0\) and unit mobilities is

\[
 a^+=a+sw^2u^4,\qquad w^+=w+2sawu^4,\qquad
 u^+=u+4saw^2u^3.                                    \tag{8.10}
\]

The frozen-bottom step omits the last update. Fix any \(\varepsilon>0\),
put \(a=-1\), and choose positive \(u,w\) by

\[
 R=\frac{1/2+\varepsilon}{s},\qquad
 u^2=\frac{\rho}{R},\qquad w^2=\frac{R^2}{\rho}.
\]

Then \(w^2u^2=R\), \(w^2u^4=\rho\), and
\(u^+/u=-1-4\varepsilon\). The two updates have identical \(a^+,w^+\).
Choose \(\rho>0\) small enough that \(s\rho<1\) and
\(0<2s(\rho/R)^2<1\). The frozen output is

\[
 f_{\mathrm{frozen}}^+=(-1+s\rho)\rho
              \{1-2s(\rho/R)^2\}^2<0,
 \qquad |f_{\mathrm{frozen}}^+|\le\rho.
\]

The full output equals \((1+4\varepsilon)^4f_{\mathrm{frozen}}^+\),
which is strictly smaller. Taking also
\((1+4\varepsilon)^4\rho<\delta\) keeps the initial output and both
terminal outputs inside \((-\delta,\delta)\). This works for every
\(s>0\), with an \(s\)-dependent state. It refutes the pathwise deletion
inequality; it is not a typical-Gaussian-trajectory counterexample.
The arbitrary joint-step theorem for the fully trained quadratic network
is not supplied by this section.

## 9. ReLU classical-flow and Euler boundaries

### 9.1 A reached finite-width obstruction to classical ReLU flow

Now use \(\phi(z)=cz_+\), \(c=\sqrt2\), where \(z_+=\max\{z,0\}\),
and train all three blocks. A prescribed kink convention is a fixed real
number \(\sigma\) assigned to \(\phi'(0)\), with derivatives \(0\) on
negative inputs and \(c\) on positive inputs. Write

\[
 \delta^{(2)}=a\odot\phi'(z^{(2)}),\qquad
 \delta^{(1)}=\phi'(u)\odot W^T\delta^{(2)}.
\]

The convention defines the pointwise vector field

\[
 \dot a=(1-f_n)h^{(2)},\qquad
 \dot u=(1-f_n)\delta^{(1)},\qquad
 \dot W=\frac{1-f_n}{n}\delta^{(2)}(h^{(1)})^T.       \tag{9.1}
\]

By a solution of this field we mean an absolutely continuous parameter path
satisfying (9.1) almost everywhere. Nonexistence in this class includes
nonexistence of an ordinary classical continuation. It says nothing about
a differential inclusion with an additional selection rule.

**Classical ReLU obstruction.** For every fixed \(\sigma\in\mathbb R\),
already at width \(n=2\), there is an open set of initial parameters of
positive Gaussian probability whose smooth trajectory reaches a gate
where (9.1) has no absolutely continuous continuation. The Gaussian law
is independent \(u_j,a_i\sim N(0,1)\), \(W_{ij}\sim N(0,1/2)\).
No probability bound uniform in width is asserted.

To prove this, at a contact point take

\[
 u=(1,1),\quad W=\frac1{\sqrt2}
       \begin{pmatrix}1&-1\\2&0\end{pmatrix},\quad
 a_1=-\lambda/c,\quad a_2=1/(4c),\qquad \lambda>1/8.
\]

Then \(h^{(1)}=(c,c)\), \(z^{(2)}=(0,2)\), \(f_2=1/4\).
When the slope used at the first top gate is \(v\), differentiation of
\(z^{(2)}=Wh^{(1)}\) gives

\[
 \dot z^{(2)}=(1-f_2)
 \left\{\frac{\|h^{(1)}\|_2^2}{2}\delta^{(2)}
             +W\operatorname{diag}(\phi'(u)^2)W^T\delta^{(2)}\right\}.
\]

Here \(\|h^{(1)}\|_2^2/2=2\),
\(WW^T=\left(\begin{smallmatrix}1&1\\1&2\end{smallmatrix}\right)\),
and \(\phi'(u)^2=(2,2)\). The first normal component is therefore

\[
 \dot z_1^{(2)}=\frac34\{4a_1v+2a_2c\}.
\]

Its negative-side, positive-side and convention-assigned values at contact
are respectively

\[
 p=\frac38>0,\qquad
 q=\frac34(1/2-4\lambda)<0,\qquad
 v_0=\frac34(1/2-4\lambda\sigma/c).                   \tag{9.2}
\]

Choose \(\lambda>1/8\) avoiding the at most one value for which \(v_0=0\).
All other gates are strictly positive. The formulas for each adjacent sign
cell and for the gate itself vary continuously in the remaining parameters.
A sufficiently small neighborhood of this contact therefore has constants
\(\gamma,\gamma_0>0\) such that

\[
 \dot z_1^{(2)}\ge\gamma\quad(z_1^{(2)}<0),\qquad
 \dot z_1^{(2)}\le-\gamma\quad(z_1^{(2)}>0),\qquad
 |\dot z_1^{(2)}|\ge\gamma_0\quad(z_1^{(2)}=0).        \tag{9.3}
\]

If an absolutely continuous solution started on this gate, continuity would
keep it in the neighborhood for a short time. Put \(w=|z_1^{(2)}|\).
It is absolutely continuous, and \(w'\le-\gamma\) almost everywhere on
\(\{w>0\}\). It has derivative zero almost everywhere on \(\{w=0\}\):
at every differentiable accumulation point of a level set the derivative
vanishes by difference quotients, while its isolated points form a
countable set. Integration from the contact gives

\[
 0\le w(t)\le-\gamma\,|\{s\in[0,t]:w(s)>0\}|.
\]

Thus \(w\equiv0\). The derivative of \(z_1^{(2)}\) is then zero almost
everywhere, contradicting the third inequality in (9.3).

The failure is reached from an open set, not just from the contact surface.
Perturb the first row to \((1+\epsilon,-1)/\sqrt2\); then
\(z_1^{(2)}=\epsilon>0\). In a fixed small ball about the contact, the
plus-cell field is smooth, its norm is bounded by a finite \(M\), and its
normal component is at most \(-\gamma\). Choose \(\epsilon\) sufficiently
small that \(2\epsilon/\gamma\) is less than the distance to the ball's
boundary divided by \(M\). A small open neighborhood of this perturbed
state still has \(0<z_1^{(2)}<2\epsilon\), stays away from every other
gate, and reaches \(z_1^{(2)}=0\) before it can exit the ball. Local smooth
ODE existence and continuation inside the sign cell follow from its
locally Lipschitz polynomial field; bounded speed precludes escape before
the stated hit. The contact lies in (9.3), so continuation fails there.
Independent nondegenerate Gaussian coordinates have a strictly positive
density everywhere in this finite parameter space, giving positive
probability to that open set.

### 9.2 Positive local compactness for every ReLU Euler step sequence

For this theorem impose \(|\sigma|\le c=\sqrt2\), keep all three blocks
trained, and initialize independently by
\(u_j,a_i\sim N(0,1)\), \(W_{ij}\sim N(0,1/n)\).
The exact Euler step for (9.1) is

\[
 a^+=a-\eta r_nh^{(2)},\qquad
 u^+=u-\eta r_n\delta^{(1)},\qquad
 W^+=W-\frac{\eta r_n}{n}\delta^{(2)}(h^{(1)})^T.     \tag{9.4}
\]

Let \(F_n(t)\) be the predictor recomputed from the linearly interpolated
raw parameters, and let \(J_n(t)=(F_n(t)-1)^2/2\). For every deterministic
\(\eta_n>0\) tending to zero, their joint laws are tight in
\(C([0,T_0];\mathbb R^2)\), where

\[
 T_0=\frac1{384\cdot6^4}.                              \tag{9.5}
\]

Every subsequential distributional limit consists of continuous paths with
\(F(0)=0\), \(J(0)=1/2\). The same holds if one instead linearly
interpolates the grid predictors, the grid losses, or both. No determinism,
uniqueness, full parameter-state compactness, tangent-kernel convergence,
or extension beyond \(T_0\) is asserted.

The proof needs neither differentiability at a gate nor energy dissipation
for the Euler scheme. Set

\[
 R=\max\left\{1,\frac{\|a\|_2}{\sqrt n},
                   \frac{\|u\|_2}{\sqrt n},\|W\|_{\mathrm{op}}\right\}.
\]

The Lipschitz constant \(c\) of ReLU and the bound \(|\phi'|\le c\) imply

\[
 \frac{\|h^{(1)}\|_2}{\sqrt n}\le cR,\quad
 \frac{\|h^{(2)}\|_2}{\sqrt n}\le2R^2,\quad
 \frac{\|\delta^{(2)}\|_2}{\sqrt n}\le cR,\quad
 \frac{\|\delta^{(1)}\|_2}{\sqrt n}\le2R^2.
\]

Hence \(|f_n|\le2R^3\) and \(|r_n|\le3R^3\). The rank-one norm identity
\(\|vw^T/n\|_{\mathrm{op}}=\|v\|_2\|w\|_2/n\), together with
(9.4), bounds each of the three parameter increments in its displayed
norm by \(6\eta R^5\). Therefore, pathwise,

\[
 R^+\le R+6\eta R^5.                                  \tag{9.6}
\]

Let \(R_*=6\), \(S=12\), \(T_*=1/(192\cdot6^4)=2T_0\).
On the initialization event

\[
 \mathcal E_n=\left\{
   \|a^0\|_2/\sqrt n\le2,\quad \|u^0\|_2/\sqrt n\le2,
   \quad\|W^0\|_{\mathrm{op}}\le6\right\},             \tag{9.7}
\]

induction gives \(R_k\le S\) at every grid time \(k\eta_n\le T_*\).
Indeed, if all preceding states satisfy that bound, telescoping (9.6)
gives

\[
 R_k\le R_*+6k\eta_nS^5
       \le R_*+6T_*(2R_*)^5=2R_*=S.
\]

The event (9.7) has probability tending to one. For the first two
conditions the empirical mean of Gaussian squares has mean one and
variance \(2/n\), so Chebyshev applies. For the matrix condition there is
an elementary finite-net argument. Choose a maximal \(1/4\)-separated
set on the unit sphere. The disjoint radius-\(1/8\) balls about its points
lie in the radius-\(9/8\) ball, so its size is at most \(9^n\); maximality
makes it a \(1/4\)-net. For fixed unit vectors \(x,y\),
\(y^TW^0x\sim N(0,1/n)\). Exponential Markov applied to the Gaussian
moment generating function gives
\(\Pr\{|y^TW^0x|>3\}\le2e^{-9n/2}\). The union bound for two such nets
then gives

\[
 \Pr\left\{\max_{x,y\text{ in the net}}|y^TW^0x|>3\right\}
 \le2\,81^n e^{-9n/2}\longrightarrow0.
\]

Approximating two maximizing unit vectors by net points changes the bilinear
form by at most \(\|W^0\|_{\mathrm{op}}/2\). Hence
\(\|W^0\|_{\mathrm{op}}\le2\max_{x,y\text{ in the net}}|y^TW^0x|\),
which proves the final initialization bound.

For all sufficiently large \(n\), \(\eta_n\le T_0\), so every endpoint
needed to interpolate through \(T_0\) lies before \(T_*\). Raw linear
interpolation preserves the bound \(R\le S\) by convexity of the three
norms. Within one grid cell, its three parameter velocities in those norms
are at most \(6S^5\). For times \(t,s\) in that cell, ReLU Lipschitzness
and the product difference \(W(t)h^{(1)}(t)-W(s)h^{(1)}(s)\) give

\[
 \frac{\|h^{(1)}(t)-h^{(1)}(s)\|_2}{\sqrt n}
       \le6cS^5|t-s|,
\]
\[
 \frac{\|z^{(2)}(t)-z^{(2)}(s)\|_2}{\sqrt n}
       \le12cS^6|t-s|,
 \qquad
 \frac{\|h^{(2)}(t)-h^{(2)}(s)\|_2}{\sqrt n}
       \le24S^6|t-s|.
\]

A final product difference in \(a^Th^{(2)}/n\) proves

\[
 |F_n(t)-F_n(s)|\le(12S^7+24S^7)|t-s|
                    \le60S^7|t-s|.
\]

Summing over intervening cells gives the same bound for arbitrary times.
Thus on \(\mathcal E_n\),

\[
 \sup_{t\le T_0}|F_n(t)|\le2S^3,\qquad
 |F_n(t)-F_n(s)|\le60S^7|t-s|.                         \tag{9.8}
\]

Uniformly bounded functions with a common Lipschitz constant form a compact
subset of \(C([0,T_0])\): convergence on a countable dense set is obtained
by successive bounded subsequences, and the common modulus extends it to
uniform convergence and a continuous limit. The squared-loss map sends
this set continuously to another compact set. Since
\(\Pr(\mathcal E_n)\to1\), (9.8) proves asymptotic tightness of the
pair. To include any finite set of smaller widths, restrict their Gaussian
initial parameters to a sufficiently large bounded set. Repeated use of
(9.6) bounds their finitely many Euler states and parameter velocities,
yielding their own compact sets by the same argument. A finite union is
compact. This proves tightness of the entire sequence. The usual weak
compactness theorem for tight probability measures on the complete
separable space \(C([0,T_0];\mathbb R^2)\) then supplies convergent
subsequences.

At initialization, condition first on \(u\). Writing
\(Q_n=\|\phi(u)\|_2^2/n\), the independent Gaussian rows give
\(z_i^{(2)}\mid u\sim N(0,Q_n)\). Symmetry and \(c^2=2\) imply
\(\mathbb E[\phi(z_i^{(2)})^2\mid u]=Q_n\), and \(\mathbb E Q_n=1\).
Conditioning next on the two hidden blocks and using the independent
centered readouts proves

\[
 \mathbb E(F_n(0))^2
 =\frac1{n^2}\mathbb E\|h^{(2)}(0)\|_2^2=\frac1n.
\]

Therefore \(F_n(0)\to0\) in probability. Evaluation at time zero is
continuous in the uniform topology, so every weak subsequential limit has
\(F(0)=0\), and the loss relation gives \(J(0)=1/2\).

Finally the grid predictor interpolation has the same endpoint Lipschitz
bound as (9.8). It differs from the raw-parameter predictor by at most
\(2\cdot60S^7\eta_n\) on \(\mathcal E_n\), since both agree at the left
endpoint of each cell. The loss map is Lipschitz on the bounded output
interval. For grid predictors \(x,y\), the linear interpolation of their
losses differs from the loss of their linear interpolation by exactly
\(\lambda(1-\lambda)(x-y)^2/2\), at cell fraction \(\lambda\in[0,1]\).
It is at most \((x-y)^2/8\), hence uniformly \(O(\eta_n^2)\) on the same
event. These differences vanish in probability, proving all interpolation
variants stated above.

### 9.3 A frozen gate retains occupation information

An elementary local model further separates classical noncontinuation from
Euler compactness. Freeze two normal velocities \(p>0>q\), choose the
standard contact convention \(v(0)=p\), and consider

\[
 z_{k+1}=z_k+\eta\{p+(q-p)I_k\},\qquad I_k=\mathbf1_{\{z_k>0\}}.
\]

Its strip \(\eta q<z\le\eta p\) is invariant: below or at zero add
\(\eta p\), and above zero add \(\eta q\). Every initial point enters
this strip after finitely many steps by repeated motion toward zero.
Inside it, put

\[
 \lambda=\frac p{p-q},\qquad
 x_k=\frac{z_k/\eta-q}{p-q}\in(0,1].
\]

The update gives exactly \(x_{k+1}=x_k+\lambda-I_k\), including a visit
to zero under the stated convention. Consequently, on every finite window
of length \(N\),

\[
 \left|\sum_{k=j}^{j+N-1}I_k-N\lambda\right|
   =|x_j-x_{j+N}|<1.                                  \tag{9.9}
\]

Thus a gate initialized in the strip has \(z=O(\eta)\) uniformly in time,
while its occupation converges to a binary mixture with weights
\(1-\lambda,\lambda\). All its positive integer gate moments converge to
\(\lambda\), since \(I_k^r=I_k\) for every integer \(r\ge1\).
Replacing the binary gate by its scalar mean instead gives second moment
\(\lambda^2\), which is different for \(0<\lambda<1\).

Joint moments also need separate information. For \(p=-q\), two identical
nonboundary phases produce identical alternating gates and average product
\(1/2\); two phases differing by half the strip's circle length produce
complementary gates and average product zero. Their marginal occupations
are both \(1/2\). These are exact frozen scalar examples, not claimed
reachable configurations of the random network. In a neural kernel, squares
of \(a\odot\phi'(z^{(2)})\) and of its reused transpose action can detect
such second and joint moments.

The ReLU local compactness theorem therefore does not identify a generalized
population flow or its loss law uniquely. Conversely, the reached classical
obstruction does not preclude continuous scalar Euler subsequences. Neither
statement resolves the fully trained quadratic arbitrary-step problem.
