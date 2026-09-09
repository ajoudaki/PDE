## Necessary fitting distance and time for a vanishing odd perturbation

Fix a hidden depth \(L\ge2\), and use the activation
\(\phi_\theta(z)=(1-\theta)z+\theta\arctan z\),
\(0<\theta\le1/2\), in every hidden layer. Take three unit directions
\(u_1+u_2+u_3=0\), \(u_a^Tu_b=-1/2\) for \(a\ne b\), and labels
\(y_a=1\). Thus \(x_a=\sqrt d\,u_a\) gives the canonical input
normalization in each \(d\ge2\). This is correlated, rank-two data.
Use the half-sum loss \(\mathcal E=\tfrac12\sum_a(f_a-1)^2\).

This is a conditional theorem on given population spaces. Let each adjacent
\(W^{(\ell)}:L^2(\Omega_{\ell-1})\to L^2(\Omega_\ell)\)
be bounded, with initial norm at most a fixed \(M\ge0\), and let its learned
increment be Hilbert--Schmidt. The first preactivations are linear in the
inputs, and the stored population readout \(W^{(L+1)}\) starts at zero.
The joint raw distance \(R\) is the square root of the sum of the squared
first-row \(L^2\) distance, squared Hilbert--Schmidt adjacent increments,
and squared readout \(L^2\) distance. Every estimate below applies on these
spaces without a trained Gaussian-law assumption. The choice \(M=2\)
recovers the displayed numerical constants below; that choice is an explicit
initial-action hypothesis, not a Gaussian norm theorem imported here.
No finite random readout is replaced by zero, and no finite-width or
population-existence conclusion is asserted.

Let \(S_\ell=\sum_{a=1}^3 H_a^{(\ell)}\) and
\(T_\ell=\sum_{a=1}^3\arctan Z_a^{(\ell)}\), in their own layer
spaces. With \(a_\theta=1-\theta\), input linearity gives exactly

\[
 S_1=\theta T_1,\qquad
 S_\ell=a_\theta W^{(\ell)}S_{\ell-1}+\theta T_\ell,
 \qquad \|T_\ell\|_{L^2(\Omega_\ell)}\le3\pi/2.
 \tag{F.1}
\]

Iterating this identity and using the operator norm at each step proves

\[
 \|S_L\|_{L^2}\le\frac{3\pi\theta}{2}
 \sum_{k=1}^L a_\theta^{L-k}
                 \prod_{j=k+1}^L\|W^{(j)}\|_{\rm op}.
 \tag{F.2}
\]

The empty product is one. If a state reaches \(\mathcal E\le3/8\),
Cauchy–Schwarz gives \(|\sum_a(f_a-1)|\le3/2\), hence
\(\sum_a f_a\ge3/2\). Pair this sum with the readout in (F.2):

\[
 \|W^{(L+1)}\|_{L^2}
 \sum_{k=1}^L a_\theta^{L-k}
                 \prod_{j=k+1}^L\|W^{(j)}\|_{\rm op}
 \ge\frac1{\pi\theta}.
 \tag{F.3}
\]

Since \(\|W^{(L+1)}\|_{L^2}\le R\) and
\(\|W^{(j)}\|_{\rm op}\le M+R\), this implies

\[
 R\sum_{k=0}^{L-1}[a_\theta(M+R)]^k\ge(\pi\theta)^{-1}.
 \tag{F.4}
\]

In particular successful states leave every fixed raw ball as
\(\theta\downarrow0\) at fixed \(L,M\). For \(M=2\),
\(R L(2+R)^{L-1}\ge(\pi\theta)^{-1}\), and therefore

\[
 R\ge[(\pi L\theta)^{-1/L}-2]_+.
 \tag{F.5}
\]

Here \([x]_+=\max\{x,0\}\); we used
\(R(2+R)^{L-1}\le(2+R)^L\).

The sharper leading distance constant is independent of the fixed \(M\).
Set \(c=\|W^{(L+1)}\|_{L^2}\) and
\(d_j=\|W^{(j)}-W^{(j)}(0)\|_{\rm HS}\) for \(2\le j\le L\).
Their squared sum is at most \(R^2\). Expand the upper bound on the left
of (F.3) with \(\|W^{(j)}\|\le M+d_j\). Its sole term of degree
\(L\) is at most \(c\prod_{j=2}^L d_j\); the remaining finite sum is at
most \(C_{L,M}(1+R)^{L-1}\). Arithmetic–geometric mean on the \(L\)
nonnegative squared factors gives

\[
 c\prod_{j=2}^L d_j\le (R^2/L)^{L/2}.
\]

Thus for every family of successful states with \(\theta\downarrow0\),

\[
 \liminf_{\theta\downarrow0}\theta^{1/L}R
 \ge\sqrt L\,\pi^{-1/L}.
 \tag{F.6}
\]

Indeed along any subsequence with bounded \(\theta^{1/L}R\), multiply
(F.3) by \(\theta\); the lower-degree remainder tends to zero. If there
is no such subsequence the inequality is automatic.

Suppose further that an existing strong physical gradient flow reaches this
loss at time \(T\), and satisfies the actual raw-metric energy identity

\[
 \mathcal E(t)+\int_0^t\|\dot\Theta(v)\|_{\rm raw}^2dv
 =\mathcal E(0)=3/2.
 \tag{F.7}
\]

Here the raw norm is precisely the product Hilbert norm defining \(R\).
The chord bound gives \(R(T)^2\le(3/2)T\). For \(M=2\), (F.5) yields
\(T\ge\tfrac23[(\pi L\theta)^{-1/L}-2]_+^2\); for every fixed \(M\),

\[
 \liminf_{\theta\downarrow0}\theta^{2/L}T
 \ge\frac{2L}{3}\pi^{-2/L}.
 \tag{F.8}
\]

A first-exit argument gives a stronger time order when \(L>2\). Put
\(B_{L,M}=\sum_{k=0}^{L-1}(M+1)^k\) and assume
\(\theta<1/(\pi B_{L,M})\). Formula (F.4) excludes a successful state
with \(R\le1\), so continuity gives a first time \(t_1\le T\) with
\(R(t_1)=1\). At that time the readout norm is at most one and every
adjacent norm is at most \(M+1\). Formula (F.2) and the exact loss expansion
give

\[
 \mathcal E(0)-\mathcal E(t_1)
 =\sum_a f_a(t_1)-\tfrac12\sum_a f_a(t_1)^2
 \le\frac{3\pi\theta}{2}B_{L,M}.
\]

On the other hand (F.7) gives
\(1=R(t_1)^2\le t_1[\mathcal E(0)-\mathcal E(t_1)]\). Therefore

\[
 T\ge\frac{2}{3\pi B_{L,M}\theta},\qquad
 M=2:\quad T\ge\frac{4}{3\pi(3^L-1)\theta}.
 \tag{F.9}
\]

At fixed \(L>2\), this implies \(\theta^{2/L}T\to\infty\) along
every successful family. At \(L=2\), (F.8) has the stronger leading
constant \(4/(3\pi)\). No monotonicity of distance, uniqueness, or
sample-symmetric trajectory is used. These are necessary scales conditional
on successful fitting; they give no matching upper bounds or global flow.
They exclude a fitting rate with both a positive rate and a finite prefactor
uniform in \(\theta\) on this data class, while allowing rates that depend
on \(\theta\) or a theorem choosing one fixed positive \(\theta\).
