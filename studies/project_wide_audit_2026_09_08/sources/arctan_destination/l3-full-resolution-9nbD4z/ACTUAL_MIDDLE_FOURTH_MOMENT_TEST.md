# Actual middle fourth moment: direct Gaussian-column test

Status: **NO_CANONICAL_PROGRESS**. This bounded positive-time test does
not prove
\[
\sup_{n\ge1}\sup_{0\le s\le S}
 \mathbb E\frac1n\sum_i|q_i^{(2)}(s)|^4<\infty.
\]
It also gives no spacetime or expected path-supremum version. The exact
retained actual term is (8). No experiment, auxiliary trajectory,
initial-jet calculation, or weighted response-energy identity is used.
No independent audit is claimed.

The fixed target and complete continuation registry were read before
selecting this test. The model/path bounds were checked against Section 1
of ACTUAL_CANONICAL_MIDDLE_POSITIVE_CURVATURE.md (SHA256
9f0b1a3c6cc334e533e0623d5d2e15413324037f7887914874f08e91a320a23e)
and are reproduced below; its initial-law theorem is not needed.
ACTUAL_FULL_PAIR_GAUSSIAN_IBP.md was read to check overlap. This test
integrates a fourth power of the primal query and retains first flow
derivatives. No external theorem is invoked.

## Actual flow and elementary bounds

Fix $S<\infty$, $n\ge1$, and $\phi=\arctan$; put $a=\pi/2$.
All entries within and between the four initial blocks are independent:
\[
z_i^{(1)}(0)\sim N(0,1),\qquad
W_{ij}^{(\ell)}(0)\sim N(0,1/n)\quad(\ell=2,3),\qquad
W_i^{(4)}(0)=G_i^{(4)}/n,\quad G_i^{(4)}\sim N(0,1).
\]
Thus the readout variance is $n^{-2}$. Use finite transpose $T$ and
ordinary Euclidean, operator, and Frobenius norms as marked. Set
$h^{(\ell)}=\phi(z^{(\ell)})$ and
\[
\begin{gathered}
z^{(2)}=W^{(2)}h^{(1)},\qquad z^{(3)}=W^{(3)}h^{(2)},\\
\delta^{(3)}=W^{(4)}\odot\phi'(z^{(3)}),\qquad
q^{(2)}=(W^{(3)})^T\delta^{(3)},\qquad
\delta^{(2)}=\phi'(z^{(2)})\odot\tau(q^{(2)}),\\
(z^{(1)})'=\phi'(z^{(1)})\odot(W^{(2)})^T\delta^{(2)},\\
(W^{(2)})'=\delta^{(2)}(h^{(1)})^T/n,\qquad
(W^{(3)})'=\delta^{(3)}(h^{(2)})^T/n,\qquad
(W^{(4)})'=h^{(3)}.                                      \tag{1}
\end{gathered}
\]
Here $\tau(v)=v$ gives the canonical flow. The calculation also covers
each prescribed deterministic $C^1$ coordinate clipping satisfying
$|\tau(v)|\le|v|$ and $|\tau'(v)|\le1$. No derivative assertion is made
for a merely Lipschitz clipping. Primes mean feature-time derivatives.
The physical equations multiply (1) by $2(1-f_n)$, where
$f_n=(W^{(4)})^Th^{(3)}/n$; the residual $f_n-1$ is excluded from
every backward field.

Define random path-bound constants
\[
M=\max_{\ell=2,3}\|W^{(\ell)}(0)\|_{\rm op},\quad
B=\|W^{(4)}(0)\|_\infty+aS,\quad
K_3=M+aSB,\quad K_2=M+aSK_3B.
\]
The readout integral and rank-one updates in (1) give, for $s\le S$,
\[
\begin{gathered}
\|W^{(4)}(s)\|_\infty\le B,\quad
\|\delta^{(3)}(s)\|_2/\sqrt n\le B,\quad
\|W^{(\ell)}(s)\|_{\rm op}\le K_\ell\quad(\ell=2,3),\\
\|(z^{(1)})'(s)\|_2/\sqrt n\le K_2K_3B.                 \tag{2}
\end{gathered}
\]
Indeed $\|(W^{(3)})'\|_{\rm F}\le aB$ and
$\|(W^{(2)})'\|_{\rm F}\le aK_3B$. These bounds keep every parameter
bounded on each finite horizon at fixed width. Local existence follows
by contraction of the finite-dimensional integral equation. Its bounded
vector field supplies a limit at any finite endpoint and extends the
solution. The uncut vector field is smooth; with the specified clipping
it is $C^1$. Differentiating that integral equation gives continuous
first initial-data derivatives, bounded on compact initial-data sets
at fixed width and horizon.

Every fixed moment of $M,B,K_2,K_3$ is bounded uniformly in $n$.
A $1/4$-net of the unit sphere has at most $9^n$ points by disjoint
$1/8$-ball packing. Approximating both arguments of a bilinear form
bounds its operator norm by twice its net maximum. Each Gaussian
bilinear form here has variance $1/n$; its exponential-moment tail
and a union bound give
\[
\mathbb P(M>x)\le4\exp(2n\log9-nx^2/8).
\]
For $x\ge10$ this is at most $4e^{-x^2/16}$, which gives the moments.
Also
\[
\mathbb E(\|G^{(4)}\|_2/n)^{2k}
=n^{-2k}\prod_{r=0}^{k-1}(n+2r)\le C_k n^{-k}.
\]
This follows by differentiating
$\mathbb E e^{t\|G^{(4)}\|_2^2}=(1-2t)^{-n/2}$ at zero; domination
holds in a smaller neighborhood of zero. Since
$\|W^{(4)}(0)\|_\infty\le\|G^{(4)}\|_2/n$, this handles $B$.
Polynomial expansion and Cauchy--Schwarz handle products. Below $C_S$
depends only on $S$, the fixed activation and this initial law, never
on width or the chosen clipping or its cap.

Separate the original matrix action and its actual trained shift:
\[
\begin{split}
v^{(2)}(s)&=(W^{(3)}(0))^T\delta^{(3)}(s),\\
q_i^{(2)}(s)&=v_i^{(2)}(s)+b_i^{(2)}(s),\\
b_i^{(2)}(s)&=\int_0^s h_i^{(2)}(u)
       \frac{\delta^{(3)}(u)^T\delta^{(3)}(s)}n\,du,\\
|b_i^{(2)}(s)|&\le aSB^2,\qquad
\|v^{(2)}(s)\|_2/\sqrt n\le MB.                         \tag{3}
\end{split}
\]
In particular $\mathbb E\sup_{s\le S}\max_i|b_i^{(2)}(s)|^4\le C_S$.
Write $m_{4,n}(s)=n^{-1}\sum_i|v_i^{(2)}(s)|^4$, a scalar moment.
The crude bound $m_{4,n}(s)\le nM^4B^4$ proves integrability at each
fixed width but retains a factor $n$. The bounded shift (3) does not
supply the missing fourth moment of $v^{(2)}$.

## Exact sensitivity of the actual input

Fix $s\in[0,S]$. Set
$\partial_{ji}=\partial/\partial W_{ji}^{(3)}(0)$, holding all other
initial coordinates fixed. Define, for each $i$, the $n\times n$ array
\[
\rho_{kj}^{(3;i)}
=\partial_{ji}\delta_k^{(3)}
 -h_i^{(2)}W_k^{(4)}\phi''(z_k^{(3)})\mathbf1_{\{k=j\}}.       \tag{4}
\]
Differentiating $z^{(3)}=W^{(3)}h^{(2)}$ separates the direct term
$\mathbf1_{\{k=j\}}h_i^{(2)}$ and gives the exact remaining response:
\[
\begin{split}
\rho_{kj}^{(3;i)}={}&\phi'(z_k^{(3)})\partial_{ji}W_k^{(4)}\\
&+W_k^{(4)}\phi''(z_k^{(3)})
 \left\{\sum_\ell\partial_{ji}
    [W_{k\ell}^{(3)}-W_{k\ell}^{(3)}(0)]h_\ell^{(2)}
 +\sum_\ell W_{k\ell}^{(3)}\phi'(z_\ell^{(2)})
                              \partial_{ji}z_\ell^{(2)}\right\}.
                                                               \tag{5}
\end{split}
\]
The actual histories in (5) obey
\[
\begin{aligned}
\partial_{ji}W_k^{(4)}(s)
 &=\int_0^s\phi'(z_k^{(3)}(u))\partial_{ji}z_k^{(3)}(u)\,du,\\
\partial_{ji}[W_{k\ell}^{(3)}(s)-W_{k\ell}^{(3)}(0)]
 &=\frac1n\int_0^s\left[
  (\partial_{ji}\delta_k^{(3)})h_\ell^{(2)}
  +\delta_k^{(3)}\phi'(z_\ell^{(2)})\partial_{ji}z_\ell^{(2)}
                         \right](u)\,du,\\
\partial_{ji}z^{(2)}
 &=(\partial_{ji}W^{(2)})h^{(1)}
   +W^{(2)}[\phi'(z^{(1)})\odot\partial_{ji}z^{(1)}],\\
\partial_{ji}\delta^{(2)}
 &=\phi'(z^{(2)})\odot\tau'(q^{(2)})\odot\partial_{ji}q^{(2)}
   +\phi''(z^{(2)})\odot\tau(q^{(2)})\odot\partial_{ji}z^{(2)}.
                                                               \tag{6}
\end{aligned}
\]
The first two parameter equations in (1), differentiated with zero
initial variations, define the two lower responses in (6). For the
uncut flow its last term is precisely
$\phi''(z^{(2)})\odot q^{(2)}\odot\partial_{ji}z^{(2)}$.
All trained layers and their increments remain present.

## Fourth-power Gaussian calculation and its stopping term

Let $x$ be the vector of all raw initial coordinates. Choose a smooth
nonincreasing $\eta:[0,\infty)\to[0,1]$, equal to one on $[0,1]$
and zero on $[4,\infty)$, and set $\chi_L=\eta(\|x\|_2^2/L^2)$
for $L\ge1$. Then $\chi_L\uparrow1$ and
$|\partial_{ji}\chi_L|\le C/L$. On its compact support every first
flow derivative above is bounded at fixed $n,S,L$.

For a compactly supported $C^1$ function $F$, integration against the
one-dimensional $N(0,1/n)$ density gives
$\mathbb E[W_{ji}^{(3)}(0)F]=n^{-1}\mathbb E\partial_{ji}F$:
the density derivative is $-nw$ times that density, and the boundary
term vanishes. Apply this with
$F=\chi_L\delta_j^{(3)}(v_i^{(2)})^3$, and use
\[
\partial_{ji}v_i^{(2)}
=\delta_j^{(3)}+\sum_kW_{ki}^{(3)}(0)\partial_{ji}\delta_k^{(3)}.
\]
Summing over $i,j$ gives
\[
\mathbb E[\chi_Lm_{4,n}]
=\mathcal A_{n,L}+\mathcal D_{n,L}
 +\mathcal R_{n,L}+\mathcal E_{n,L},                         \tag{7}
\]
with exact retained actual history term
\[
\mathcal R_{n,L}(s)=\frac1{n^2}\mathbb E\!\left[\chi_L
 \sum_{i,j}\left\{
 (v_i^{(2)})^3\rho_{jj}^{(3;i)}
 +3(v_i^{(2)})^2\delta_j^{(3)}
          \sum_k W_{ki}^{(3)}(0)\rho_{kj}^{(3;i)}
                    \right\}\right].                       \tag{8}
\]
All factors in (8) are evaluated at $s$, except the indicated initial
matrix. The other terms contain no flow derivatives:
\[
\begin{aligned}
\mathcal A_{n,L}
 &=3\mathbb E\left[\chi_L
       \frac{\|\delta^{(3)}\|_2^2}{n}
       \frac{\|v^{(2)}\|_2^2}{n}\right],\\
\mathcal D_{n,L}
 &=\frac1{n^2}\mathbb E\left[\chi_L\sum_{i,j}
 h_i^{(2)}W_j^{(4)}\phi''(z_j^{(3)})
 \left\{(v_i^{(2)})^3
  +3(v_i^{(2)})^2\delta_j^{(3)}W_{ji}^{(3)}(0)\right\}\right],\\
\mathcal E_{n,L}
 &=\frac1{n^2}\sum_{i,j}\mathbb E\left[
    (\partial_{ji}\chi_L)\delta_j^{(3)}(v_i^{(2)})^3\right].
                                                               \tag{9}
\end{aligned}
\]
The contact term satisfies
$0\le\mathcal A_{n,L}\le3\mathbb E[M^2B^4]\le C_S$.
Using $|h_i^{(2)}|\le a$ and
$|W_j^{(4)}\phi''(z_j^{(3)})|\le2B$, the two pointwise contributions
to $\mathcal D_{n,L}$, before expectation and multiplication by
$\chi_L$, have absolute values at most
\[
2aB\,m_{4,n}^{3/4},\qquad
\frac{6a}{n}MB^2m_{4,n}^{1/2}.                         \tag{10}
\]
For the second bound, pair the vector with coordinates
$h_i^{(2)}(v_i^{(2)})^2$ against
$(W^{(3)}(0))^T[W^{(4)}\odot\phi''(z^{(3)})\odot\delta^{(3)}]$.
Their Euclidean norms are at most $a\sqrt{nm_{4,n}}$ and
$2MB^2\sqrt n$, and (9) supplies $3/n^2$.
Maximizing $tx^3-\epsilon x^4$ and $tx^2-\epsilon x^4$ for $x\ge0$
with a fixed sufficiently small $\epsilon>0$ gives
\[
|\mathcal D_{n,L}|
\le\tfrac12\mathbb E[\chi_Lm_{4,n}]+C_S,                 \tag{11}
\]
uniformly in $n,L,s\le S$ and in the allowed clipping. The remaining
polynomials are constant multiples of $B^4$ and $n^{-2}M^2B^4$,
whose expectations were proved bounded.

At fixed $n,s$, $\mathcal E_{n,L}\to0$: its cutoff derivative
vanishes pointwise and the other factors have integrable polynomial
bounds from (2)--(3). The same bounds give dominated convergence for
the left side of (7), $\mathcal A_{n,L}$, and $\mathcal D_{n,L}$.
Consequently the signed aggregate
\[
\mathcal R_n(s):=\lim_{L\to\infty}\mathcal R_{n,L}(s)       \tag{12}
\]
exists at each fixed width and time by (7). This does not establish
absolute integrability of either response summand separately, a
width-uniform bound on (12), or interchange with a width limit.

The direct terms have been absorbed in (11), but (8), with the actual
input sensitivities (5)--(6), remains unestimated. Boundedness of
$\delta^{(3)}$ cannot be differentiated into a bound on its response.
The factor involving $\partial_{ji}z^{(2)}$ includes both trained
lower blocks and the middle multiplier in (6). Neither its weighted
trace in (8) nor its weighted directional contraction is controlled
by the primal bounds proved here. No sign or independence of these
actual factors has been established. Time integration retains the
same unestimated contraction integrated in time.

This finishes the bounded test with **NO_CANONICAL_PROGRESS**.
It is a failed estimate of the requested actual moment, not a
sufficient-criterion theorem or a counterexample to that moment.
No all-finite-feature-time fourth-moment bound, clipping-uniform such
bound, Osgood tail, or full canonical continuation theorem was obtained.
