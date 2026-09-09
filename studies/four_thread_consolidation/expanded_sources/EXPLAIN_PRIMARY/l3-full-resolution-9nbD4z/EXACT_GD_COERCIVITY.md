# Exact finite-width GD with three hidden layers

This note proves a deterministic theorem for exact GD, followed by a
self-contained corollary for the prescribed Gaussian initialization.
The theorem gives uniform coercivity, convergence to the target, and
convergence of every finite-width parameter. It makes no assumption
about a trained-state limit as the width tends to infinity.

## Network and exact updates

All vectors have length \(n\). The norm \(\|\cdot\|_2\) is the ordinary
Euclidean vector norm and \(\|\cdot\|_{\rm op}\) is the induced matrix
norm. Set
\[
a=\pi/2,\qquad \phi(x)=\arctan x,\qquad
\phi'(x)=\frac1{1+x^2}.
\]
The state is
\(\theta=(z^{(1)},W^{(2)},W^{(3)},W^{(4)})\), with forward equations
\[
h^{(1)}=\phi(z^{(1)}),\qquad
z^{(2)}=W^{(2)}h^{(1)},\qquad h^{(2)}=\phi(z^{(2)}),
\]
\[
z^{(3)}=W^{(3)}h^{(2)},\qquad h^{(3)}=\phi(z^{(3)}),\qquad
f=\frac{(W^{(4)})^{\mathsf T}h^{(3)}}n.
\]
The activation is applied coordinatewise. Define
\[
D_\ell=\operatorname{diag}\bigl(\phi'(z_i^{(\ell)})\bigr),
\qquad \ell=1,2,3,
\]
\[
\delta^{(3)}=D_3W^{(4)},\qquad
\delta^{(2)}=D_2(W^{(3)})^{\mathsf T}\delta^{(3)},\qquad
\delta^{(1)}=D_1(W^{(2)})^{\mathsf T}\delta^{(2)}.
\]
An index \(k\) denotes the exact discrete iteration. With
\(\eta=n^{-2}\), the updates under consideration are
\[
z_{k+1}^{(1)}
=z_k^{(1)}-2\eta(f_k-1)\delta_k^{(1)},
\]
\[
W_{k+1}^{(\ell)}
=W_k^{(\ell)}-\frac{2\eta(f_k-1)}n
  \delta_k^{(\ell)}(h_k^{(\ell-1)})^{\mathsf T},
\qquad \ell=2,3,
\]
\[
W_{k+1}^{(4)}
=W_k^{(4)}-2\eta(f_k-1)h_k^{(3)}.                         \tag{1}
\]
For the proof define the computational step lengths and clock
\[
\alpha_k=2\eta(1-f_k),\qquad
s_0=0,\qquad s_k=\sum_{j<k}\alpha_j.
\]
These definitions do not change the algorithm. In particular, (1) is
exactly equivalent to
\[
z_{k+1}^{(1)}=z_k^{(1)}+\alpha_k\delta_k^{(1)},\qquad
W_{k+1}^{(\ell)}
=W_k^{(\ell)}+\frac{\alpha_k}n
  \delta_k^{(\ell)}(h_k^{(\ell-1)})^{\mathsf T},
\]
\[
W_{k+1}^{(4)}=W_k^{(4)}+\alpha_kh_k^{(3)}.               \tag{2}
\]
The proof establishes \(\alpha_k>0\) for every iteration; positivity
is not assumed in the definition of exact GD.

## Deterministic theorem

For every \(0\le M<\infty\) and \(0<b\le a\), there are explicit
constants \(\varepsilon_0(M,b)>0\), \(N(M,b)<\infty\), and
\(V(M,b)<\infty\) with the following property. If \(n\ge N(M,b)\) and
\[
\|W_0^{(2)}\|_{\rm op},\ \|W_0^{(3)}\|_{\rm op},
\frac{\|z_0^{(1)}\|_2}{\sqrt n}\le M,\qquad
\frac{\|W_0^{(4)}\|_2}{\sqrt n}\le\varepsilon_0,\qquad
\frac{\|h_0^{(3)}\|_2}{\sqrt n}\ge b,
\]
then all iterations of (1) satisfy
\[
f_k<f_{k+1}<1,\qquad
\frac{\|h_k^{(3)}\|_2}{\sqrt n}\ge\frac b2,\qquad
0<1-f_k\le(1-f_0)(1-\eta b^2/4)^k.                      \tag{3}
\]
Moreover,
\[
\sum_{k\ge0}\alpha_k\le\frac{8(1-f_0)}{b^2},\qquad
\sum_{j\ge k}\alpha_j\le\frac{8(1-f_k)}{b^2}.            \tag{4}
\]
The entire parameter sequence converges to a finite endpoint
\(\theta_\infty\), with \(f(\theta_\infty)=1\). Define the explicit
state distance
\[
\begin{aligned}
d(\theta,\widetilde\theta)=\max\Big\{&
\frac{\|z^{(1)}-\widetilde z^{(1)}\|_2}{\sqrt n},
\ \|W^{(2)}-\widetilde W^{(2)}\|_{\rm op},\\
&\|W^{(3)}-\widetilde W^{(3)}\|_{\rm op},
\ \frac{\|W^{(4)}-\widetilde W^{(4)}\|_2}{\sqrt n}\Big\}.
\end{aligned}
\]
Then
\[
d(\theta_k,\theta_\infty)\le\frac{8V(1-f_k)}{b^2}.       \tag{5}
\]
All constants are independent of the width. A coordinatewise bound on
\(W_0^{(4)}\) is not required.

The proof first bounds arbitrary positive-step paths of bounded
computational clock length. It then derives an exact feature increment
with a controlled Taylor remainder and proves that a regularized
readout norm has an almost increasing slope. This supplies the feature
lower bound needed to close the exact-GD induction.

## Constants and bounds on the computational clock

Set
\[
S=\frac{32}{b^2},\qquad Q=1+aS,\qquad
R_3=M+aQS,\qquad R_2=M+aR_3QS,
\]
\[
L=a^2+R_3^2(a^2+R_2^2),\qquad
V=\max\{a,aQ,aR_3Q,R_2R_3Q\}.                           \tag{6}
\]
Consider, temporarily, any finite sequence of updates (2) with
nonnegative step lengths, cumulative sum at most \(S\), the stated
initial hidden-matrix bounds, and
\(\|W_0^{(4)}\|_2/\sqrt n\le1\). Then
\[
\frac{\|W_k^{(4)}\|_2}{\sqrt n}\le Q,\qquad
\|W_k^{(3)}\|_{\rm op}\le R_3,\qquad
\|W_k^{(2)}\|_{\rm op}\le R_2.                          \tag{7}
\]
Indeed, \(\|h_k^{(\ell)}\|_2/\sqrt n\le a\). The readout increment
has Euclidean norm at most \(a\alpha_k\sqrt n\).
The operator norms of the third- and second-layer increments are
bounded by \(\alpha_k\) times
\[
a\,\frac{\|W_k^{(4)}\|_2}{\sqrt n},
\qquad
a\|W_k^{(3)}\|_{\rm op}
  \frac{\|W_k^{(4)}\|_2}{\sqrt n},
\]
respectively. Summing these three estimates successively proves (7).
Also
\(\|z_{k+1}^{(1)}-z_k^{(1)}\|_2/\sqrt n\le\alpha_kR_2R_3Q\).
The same estimates hold along each straight Euler segment whose
computational clock is at most \(S\).

For explicit derivative bounds define scalar constants
\[
v=R_2R_3Q,\qquad A_2=aR_3Q,\qquad A_3=aQ,\qquad
v_2=aA_2+R_2v,
\]
\[
u_2=2v_2^2+2A_2v+2R_2v^2,\qquad
v_3=aA_3+R_3v_2,\qquad
B=v_3^2+A_3v_2+\frac{R_3u_2}{2}.
\]
Also define
\[
D=2aL+B,\qquad B_f=Q(aL+B),\qquad K_*=a^2+LQ^2,
\]
\[
t_0=\min\left\{1,\frac S4,\sqrt{\frac{b}{384aL}}\right\},
\qquad \lambda=\frac{bt_0}{32},\qquad
\varepsilon_0=\min\left\{1,\frac1{2a},\frac{bt_0}{32}\right\}.
                                                                    \tag{8}
\]
The scalar \(\lambda>0\) regularizes the readout norm. Choose \(N\) so
that, for every \(n\ge N\), the number \(A=4n^{-2}\) satisfies
\[
A\le\min\left\{t_0,\frac{\lambda}{a},\frac S2\right\},
\qquad
2Bt_0A\sqrt n\le\frac b{64},\qquad
DSA\sqrt n\le\frac b4,
\]
\[
B_fA\sqrt n\le\min\left\{\frac{b^2}{8},1\right\},
\qquad
2n^{-2}(K_*+1)\le\frac12.                               \tag{9}
\]
These are explicit inequalities involving only \(M,b,n\).
Such an integer \(N\) exists because \(A\sqrt n=4n^{-3/2}\)
and \(A=4n^{-2}\) tend to zero.
For example, the following closed expression suffices:
\[
N=\left\lceil\max\left\{
1,\sqrt{4/t_0},\sqrt{4a/\lambda},\sqrt{8/S},
(512Bt_0/b)^{2/3},(16DS/b)^{2/3},
(32B_f/b^2)^{2/3},(4B_f)^{2/3},
2\sqrt{K_*+1}
\right\}\right\rceil .
\]

## Exact directional identity and feature increment

Let \(G(\theta)\) be the tuple multiplying \(\alpha_k\) in (2):
\[
G(\theta)=\left(
\delta^{(1)},\quad
\frac{\delta^{(2)}(h^{(1)})^{\mathsf T}}n,\quad
\frac{\delta^{(3)}(h^{(2)})^{\mathsf T}}n,\quad
h^{(3)}
\right).
\]
The directional derivative of the third-layer feature is
\[
Dh^{(3)}(\theta)G(\theta)=P(\theta)W^{(4)},               \tag{10}
\]
where the matrix is
\[
\begin{aligned}
P=D_3\Bigg[
&\frac{\|h^{(2)}\|_2^2}{n}I\\
&+W^{(3)}D_2\left(
\frac{\|h^{(1)}\|_2^2}{n}I+
W^{(2)}D_1^2(W^{(2)})^{\mathsf T}
\right)D_2(W^{(3)})^{\mathsf T}
\Bigg]D_3.
\end{aligned}                                                        \tag{11}
\]
Here is the chain-rule calculation. A dot in the next three displays
means a directional derivative along \(G\), at one state:
\[
\dot h^{(1)}
=D_1^2(W^{(2)})^{\mathsf T}D_2(W^{(3)})^{\mathsf T}D_3W^{(4)},
\]
\[
\dot z^{(2)}
=\left(\frac{\|h^{(1)}\|_2^2}{n}I+
 W^{(2)}D_1^2(W^{(2)})^{\mathsf T}\right)
 D_2(W^{(3)})^{\mathsf T}D_3W^{(4)},
\]
\[
\dot z^{(3)}
=\frac{\|h^{(2)}\|_2^2}{n}D_3W^{(4)}
  +W^{(3)}D_2\dot z^{(2)},\qquad
\dot h^{(3)}=D_3\dot z^{(3)}.
\]
Each diagonal \(D_\ell\) has operator norm at most one. Formula (11)
therefore proves
\[
P\succeq0,\qquad \|P\|_{\rm op}\le L                    \tag{12}
\]
on all paths bounded in (7).

For a frozen Euler segment
\(\theta(u)=\theta+uG(\theta)\), with
\(0\le u\le\alpha_k\) and cumulative clock at most \(S\), primes in
the following bounds mean derivatives with respect to \(u\):
\[
\frac{\|(h^{(1)})'\|_2}{\sqrt n}\le v,\qquad
\frac{\|(h^{(1)})''\|_2}{\sqrt n}\le2\sqrt n\,v^2,
\qquad
\frac{\|(z^{(2)})'\|_2}{\sqrt n}\le v_2,
\]
\[
\frac{\|(h^{(2)})''\|_2}{\sqrt n}\le\sqrt n\,u_2,\qquad
\frac{\|(z^{(3)})'\|_2}{\sqrt n}\le v_3.
\]
To verify these estimates, use \(|\phi'|\le1\), \(|\phi''|\le2\),
the product rule, and
\[
\frac{\|w\odot w\|_2}{\sqrt n}
\le\sqrt n\left(\frac{\|w\|_2}{\sqrt n}\right)^2.
\]
The frozen matrix velocities have operator norms at most \(A_2,A_3\).
In particular,
\[
(z^{(2)})''
=2(W^{(2)})'(h^{(1)})'+W^{(2)}(u)(h^{(1)})'',
\]
which gives the two contributions \(2A_2v+2R_2v^2\) in \(u_2\).
The activation's second derivative contributes \(2v_2^2\).
The identical product rule at the third layer gives
\[
\sup_{0\le u\le\alpha_k}
\frac{\|(h^{(3)})''(u)\|_2}{\sqrt n}
\le2\sqrt n\,v_3^2+2\sqrt n\,A_3v_2
   +\sqrt n\,R_3u_2
=2B\sqrt n.
\]
Taylor's formula with its integral remainder, together with (10),
now gives the exact relation
\[
h_{k+1}^{(3)}
=h_k^{(3)}+\alpha_kP_kW_k^{(4)}+e_k,\qquad
\frac{\|e_k\|_2}{\sqrt n}\le B\sqrt n\,\alpha_k^2.        \tag{13}
\]
Thus \(e_k\) is a feature remainder vector.

Using the exact readout update in (2), (13) yields
\[
f_{k+1}-f_k=\alpha_kK_k+\rho_k,
\]
\[
K_k=\frac{\|h_k^{(3)}\|_2^2}{n}
    +\frac{(W_k^{(4)})^{\mathsf T}P_kW_k^{(4)}}n,
\qquad
\frac{\|h_k^{(3)}\|_2^2}{n}\le K_k\le K_*,              \tag{14}
\]
\[
|\rho_k|\le B_f\sqrt n\,\alpha_k^2.
\]
Indeed, the exact scalar remainder is
\[
\rho_k
=\frac{\alpha_k^2}{n}(h_k^{(3)})^{\mathsf T}P_kW_k^{(4)}
 +\frac1n(W_{k+1}^{(4)})^{\mathsf T}e_k.
\]
The first term has absolute value at most \(\alpha_k^2aLQ\), and
the second at most \(\alpha_k^2QB\sqrt n\), proving the claim.

## An almost increasing readout slope

We first prove a statement independent of the residual: on any finite
positive-step Euler path (2), with \(\alpha_k\le A\), total clock at
most \(S\), and the theorem's initialization, one has
\(\|h_k^{(3)}\|_2/\sqrt n\ge b/2\) at every node.

Interpolate the readout linearly in the computational clock:
\[
W^{(4)}(s)
=W_k^{(4)}+(s-s_k)h_k^{(3)}
\quad\text{for }s\in[s_k,s_{k+1}].
\]
Define
\[
g(s)=\sqrt{\frac{\|W^{(4)}(s)\|_2^2}{n}+\lambda^2}.
\]
On every open segment,
\[
g''(s)=
\frac{\displaystyle
\frac{\|h_k^{(3)}\|_2^2}{n}g(s)^2
-\left(\frac{(W^{(4)}(s))^{\mathsf T}h_k^{(3)}}n\right)^2}
{g(s)^3}\ge0                                             \tag{15}
\]
by Cauchy--Schwarz. At a knot, (13) gives
\[
\begin{aligned}
g'(s_{k+1}+)-g'(s_{k+1}-)
&=\frac{(W_{k+1}^{(4)})^{\mathsf T}
       (\alpha_kP_kW_k^{(4)}+e_k)}
       {n\,g(s_{k+1})}\\
&\ge-D\sqrt n\,\alpha_k^2.                              \tag{16}
\end{aligned}
\]
For the inequality, expand \(W_{k+1}^{(4)}\) using (2).
The term
\(\alpha_k(W_k^{(4)})^{\mathsf T}P_kW_k^{(4)}/(n\,g(s_{k+1}))\)
is nonnegative by (12). The \(e_k\) term is at least
\(-\|e_k\|_2/\sqrt n\). For the remaining term use
\[
\frac{\|W_k^{(4)}\|_2}{\sqrt n\,g(s_{k+1})}
\le1+\frac{\alpha_ka}{\lambda}\le2.
\]
Its absolute value is at most \(2aL\alpha_k^2\), which, together
with (13) and \(n\ge1\), proves (16).

For every node with \(s_k\le2t_0\), telescoping (13) gives
\[
\begin{aligned}
\frac{\|h_k^{(3)}-h_0^{(3)}\|_2}{\sqrt n}
&\le Ls_k(\varepsilon_0+as_k)+B\sqrt n\,A s_k\\
&\le6aLt_0^2+2Bt_0A\sqrt n
\le\frac b{32}.                                        \tag{17}
\end{aligned}
\]
Here \(\varepsilon_0\le at_0\), the definition of \(t_0\) bounds
the first summand by \(b/64\), and (9) bounds the second by \(b/64\).
In particular the desired feature lower bound holds on this initial
interval.

If the path extends beyond \(2t_0\), let \(k_0\) be the first node
with \(s_{k_0}\ge t_0\). Since every step is at most \(A\le t_0\),
\[
t_0\le s_{k_0}\le2t_0.
\]
The readout update, (17), and
\(\|W_0^{(4)}\|_2/\sqrt n\le bt_0/32\) imply
\[
\frac{W_{k_0}^{(4)}}{s_{k_0}}=h_0^{(3)}+u,\qquad
\frac{\|u\|_2}{\sqrt n}\le\frac b{16},
\]
\[
h_{k_0}^{(3)}=h_0^{(3)}+w,\qquad
\frac{\|w\|_2}{\sqrt n}\le\frac b{32},\qquad
\frac{\lambda}{s_{k_0}}\le\frac b{32}.
\]
For the bound on \(u\), divide
\[
W_{k_0}^{(4)}
=W_0^{(4)}+\sum_{j<k_0}\alpha_j h_j^{(3)}
\]
by \(s_{k_0}\): the initial readout contributes at most \(b/32\),
and the weighted average of the feature differences contributes at
most \(b/32\).

Write \(H=\|h_0^{(3)}\|_2/\sqrt n\ge b\). The preceding three bounds
give a strictly positive numerator in the expression for \(g'\), and
\[
\begin{aligned}
g'(s_{k_0}+)
&=\frac{(W_{k_0}^{(4)})^{\mathsf T}h_{k_0}^{(3)}}
        {n\,g(s_{k_0})}\\
&\ge\frac{H^2-3Hb/32-b^2/512}{H+3b/32}
\ge\frac{463}{560}H\ge\frac{3b}{4}.                    \tag{18}
\end{aligned}
\]
For the denominator, use
\(g(s_{k_0})/s_{k_0}\le H+b/16+b/32\).
For the second inequality in (18), the numerator is at least
\((463/512)H^2\) and the denominator at most \((35/32)H\).

Equations (15)--(16), together with
\(\sum_j\alpha_j^2\le A\sum_j\alpha_j\le AS\), now imply at every
later node
\[
g'(s_k+)\ge\frac{3b}{4}
 -D\sqrt n\sum_j\alpha_j^2
\ge\frac{3b}{4}-DSA\sqrt n\ge\frac b2.
\]
On the other hand, Cauchy--Schwarz gives
\[
g'(s_k+)
=\frac{(W_k^{(4)})^{\mathsf T}h_k^{(3)}}{n\,g(s_k)}
\le\frac{\|h_k^{(3)}\|_2}{\sqrt n}.
\]
This proves the feature lower bound at every node. At a final node,
the symbol \(g'(s_k+)\) denotes the displayed algebraic expression,
equivalently the derivative of a further linear readout segment with
slope \(h_k^{(3)}\); no additional parameter update is needed.

## The exact-GD induction and endpoint

Initially \(|f_0|\le a\varepsilon_0\le1/2\); hence
\(1-f_0\in[1/2,3/2]\). Suppose a finite exact-GD prefix satisfies
\[
f_0\le f_k<1,\qquad
s_k\le\frac8{b^2}(f_k-f_0)
\le\frac{8(1-f_0)}{b^2}\le\frac S2.                     \tag{19}
\]
This holds at \(k=0\). Then
\[
0<\alpha_k=2n^{-2}(1-f_k)\le A,\qquad
s_{k+1}\le S.
\]
The positive-step path bounds and the preceding feature lemma apply.
Using (9) and (14), we obtain
\[
\frac{b^2}{8}\alpha_k
\le f_{k+1}-f_k
\le\alpha_k(K_*+1)
\le\frac{1-f_k}{2}.                                    \tag{20}
\]
In detail, \(K_k\ge b^2/4\) and
\(|\rho_k|/\alpha_k\le B_fA\sqrt n\le b^2/8\) give the lower bound.
The other part of (9) gives
\(|\rho_k|/\alpha_k\le1\) and
\(\alpha_k(K_*+1)=2n^{-2}(1-f_k)(K_*+1)\le(1-f_k)/2\).
Thus \(f_k<f_{k+1}<1\), and summing the lower bound in (20) gives
\[
s_{k+1}\le\frac8{b^2}(f_{k+1}-f_0)
\le\frac{8(1-f_0)}{b^2}\le\frac S2.
\]
This closes (19) for every iteration and prevents escape from the
bounded computational-clock region used in the proof.

Substituting \(\alpha_k=2\eta(1-f_k)\) into the lower bound in (20)
yields
\[
1-f_{k+1}\le(1-\eta b^2/4)(1-f_k).
\]
Consequently \(f_k\to1\), and (3) follows. Summing (20) from \(k\)
to infinity proves both estimates in (4). Every state increment in
the distance \(d\) is at most \(V\alpha_k\), by (6)--(7).
The summability in (4) makes the parameter sequence Cauchy in its
finite-dimensional state space. Its limit is finite, the tail sum
gives (5), and continuity of the forward equations gives
\(f(\theta_\infty)=1\). The given initial condition determines this
endpoint; no uniqueness among all interpolating parameter states
is asserted.

The summable physical-time quantity is
\[
\sum_{k\ge0}\eta(1-f_k)=\frac12\sum_{k\ge0}\alpha_k.
\]
The sum of the fixed physical-time steps, \(\sum_{k\ge0}\eta\),
is infinite. At the physical times \(t_k=k\eta\), (3) also gives
\[
1-f_k\le(1-f_0)e^{-b^2t_k/4}.
\]

## The prescribed Gaussian initialization

Independently initialize all coordinates and matrix entries as
\[
z_{i,0}^{(1)}\sim N(0,1),\qquad
W_{ji,0}^{(2)},W_{ji,0}^{(3)}\sim N(0,1/n),\qquad
W_{i,0}^{(4)}\sim N(0,n^{-2}).                           \tag{21}
\]
With an independent auxiliary \(G_0\sim N(0,1)\), define positive
deterministic constants
\[
m_1=\mathbb E[\arctan(G_0)^2],\qquad
m_2=\mathbb E[\arctan(\sqrt{m_1}G_0)^2],\qquad
m_3=\mathbb E[\arctan(\sqrt{m_2}G_0)^2].
\]
Each is positive because its Gaussian argument has positive variance
and \(\arctan x\ne0\) for \(x\ne0\).

Take \(M=10\) and \(b=\sqrt{m_3}/2\), and use the resulting
deterministic \(\varepsilon_0,N,V\) from (6)--(9). With probability
tending to one as \(n\to\infty\), all hypotheses of the deterministic
theorem hold simultaneously. Therefore, with that probability, all
iterations of exact GD with \(\eta=n^{-2}\) satisfy
\[
f_k<f_{k+1}<1,\qquad
\frac{\|h_k^{(3)}\|_2^2}{n}\ge\frac{m_3}{16},
\]
\[
0<1-f_k\le(1-f_0)(1-\eta m_3/16)^k,\qquad
\sum_{j\ge k}\alpha_j\le\frac{32(1-f_k)}{m_3}.           \tag{22}
\]
Every parameter converges to its finite-width interpolating endpoint,
with the uniform distance estimate (5).

Here is an independent verification of the initialization assertion.
The independent bounded variables
\(\arctan(z_{i,0}^{(1)})^2\) have common mean \(m_1\) and variance
at most \(a^4\). Chebyshev's inequality yields
\(\|h_0^{(1)}\|_2^2/n\to m_1\) in probability.
Conditional on \(h_0^{(1)}\), the second-layer preactivations are
independent centered Gaussians with common variance
\(\|h_0^{(1)}\|_2^2/n\). Their empirical squared-activation average
has conditional variance at most \(a^4/n\) and conditional mean
\[
\mathbb E\left[
\arctan\left(\frac{\|h_0^{(1)}\|_2}{\sqrt n}G_0\right)^2
\ \middle|\ h_0^{(1)}
\right].
\]
The function \(u\mapsto\mathbb E[\arctan(\sqrt u\,G_0)^2]\)
is continuous on \(u\ge0\), by bounded convergence. Conditional
Chebyshev followed by this continuity proves
\(\|h_0^{(2)}\|_2^2/n\to m_2\) in probability. Conditioning on
\(h_0^{(2)}\) gives the identical argument for
\(\|h_0^{(3)}\|_2^2/n\to m_3\). In particular its required lower
bound holds with probability tending to one.

For either initial hidden matrix, choose a maximal \(1/4\)-separated
subset of the Euclidean unit sphere. It is a \(1/4\)-net and has at
most \(9^n\) points: the disjoint radius-\(1/8\) balls around its
points lie in a radius-\(9/8\) ball, and comparison of their volumes
gives this bound. Approximating each of the two unit vectors in a
maximizing bilinear form by a net point gives
\[
\|W_0^{(\ell)}\|_{\rm op}
\le2\max_{u,v\ \text{in the net}}
|u^{\mathsf T}W_0^{(\ell)}v|.
\]
For fixed unit \(u,v\), the bilinear form has law \(N(0,1/n)\).
The Gaussian tail estimate and a union bound therefore give
\[
\mathbb P\bigl(\|W_0^{(\ell)}\|_{\rm op}>M\bigr)
\le2\,9^{2n}e^{-nM^2/8},\qquad \ell=2,3.
\]
This tends to zero at \(M=10\).
Also \(\|z_0^{(1)}\|_2^2/n\to1\) in probability, since its mean
is \(1\) and its variance is \(2/n\). Finally,
\[
\mathbb E\left[\frac{\|W_0^{(4)}\|_2^2}{n}\right]=n^{-2},
\qquad
\mathbb P\left(\frac{\|W_0^{(4)}\|_2}{\sqrt n}
                   >\varepsilon_0\right)
\le\frac{1}{n^2\varepsilon_0^2}.
\]
A union bound combines all the initialization events, and the
deterministic width condition holds for every sufficiently large
\(n\). This proves the corollary without using a flow theorem.

The width threshold in this note is material: the fixed prescription
\(\eta=n^{-2}\) does not by itself prevent overshoot at every small
width under an arbitrary initial operator-norm bound \(M\).
The theorem proves exact finite-width optimization. It does not
prove gradient-flow/GD state closeness, convergence of the trained
states as width tends to infinity, a population endpoint, or an
interchange of infinite width and infinite physical time.
