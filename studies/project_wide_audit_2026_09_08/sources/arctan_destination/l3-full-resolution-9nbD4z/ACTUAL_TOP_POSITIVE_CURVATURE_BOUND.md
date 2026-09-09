# Actual top-curvature sign lag: a nonperturbative positive-part estimate

Scoped theorem; the independent review records its audited version.
This note bounds a
signed coefficient on the actual trained trajectories at positive times.
It is not a Taylor-coefficient calculation or a population continuation
theorem. It does not assume that readout and preactivation signs agree
coordinatewise.

The coefficient is \(W_i^{(4)}\phi''(z_i^{(3)})\), the top-activation
curvature contribution. The unbounded middle coefficient
\(q_i^{(2)}\phi''(z_i^{(2)})\) is a different object and is not controlled
by this result.

## Exact setup and deterministic velocity bound

Let \(\phi(z)=\arctan z\), \(c=\pi/2\), and fix width \(n\), feature
horizon \(S>0\), and initial hidden operator bound \(M\ge0\).
The prefix variable \(t\) in this note is feature time, not physical time.
All vector norms are ordinary Euclidean or maximum norms; all matrix
norms are ordinary operator or Frobenius norms. Put
\[
\varepsilon=\frac{\|W^{(4)}(0)\|_2}{\sqrt n}\le1,\qquad
\|W^{(2)}(0)\|_{\rm op},\|W^{(3)}(0)\|_{\rm op}\le M.
\tag{1}
\]
The hidden initial state may be arbitrary finite data for this
deterministic assertion. The canonical independent Gaussian
initialization is imposed below, not replaced by this larger class.

The result includes the full network and every fixed fully pruned
middle set. Let \(Q\) be its fixed diagonal zero-one mask, with \(Q=I\)
for the full network. Define
\[
\begin{gathered}
h^{(1)}=\phi(z^{(1)}),\quad z^{(2)}=W^{(2)}h^{(1)},\quad
h^{(2)}=Q\phi(z^{(2)}),\\
z^{(3)}=W^{(3)}h^{(2)},\quad h^{(3)}=\phi(z^{(3)}),\quad
\delta^{(3)}=W^{(4)}\odot\phi'(z^{(3)}),\\
q^{(2)}=(W^{(3)})^T\delta^{(3)},\quad
\delta^{(2)}=Q[\phi'(z^{(2)})\odot\tau(q^{(2)})].
\end{gathered}
\]
Here \(\tau:\mathbb R\to\mathbb R\) is any prescribed map satisfying
\(|\tau(v)|\le|v|\) and \(|\tau(v)-\tau(w)|\le|v-w|\), applied
coordinatewise; the identity is the uncut model. All trained updates
are retained:
\[
\begin{gathered}
(z^{(1)})'=\phi'(z^{(1)})\odot(W^{(2)})^T\delta^{(2)},\\
(W^{(2)})'=\delta^{(2)}(h^{(1)})^T/n,\quad
(W^{(3)})'=\delta^{(3)}(h^{(2)})^T/n,\quad
(W^{(4)})'=h^{(3)}.
\end{gathered}
\tag{2}
\]
Pruned rows and columns remain stored at their initial values and
frozen, as follows from these masked updates. The readout update
is unchanged.

Define constants depending only on \(S,M\):
\[
K_3=M+c(S+cS^2/2),\qquad
K_2=M+cK_3(S+cS^2/2),\qquad
K=c^2+K_3^2(c^2+K_2^2).
\tag{3}
\]
The integral readout update and \(|\phi|\le c,|\phi'|\le1\) give
\[
\frac{\|W^{(4)}(s)\|_2}{\sqrt n}\le\varepsilon+cs,\qquad
\frac{\|\delta^{(3)}(s)\|_2}{\sqrt n}\le\varepsilon+cs.
\]
Using \(\|uv^T/n\|_{\rm F}=\|u\|_2\|v\|_2/n\) in (2) then gives
\[
\|W^{(3)}(s)\|_{\rm op}
\le M+c(\varepsilon s+cs^2/2)\le K_3,
\]
\[
\frac{\|\delta^{(2)}(s)\|_2}{\sqrt n}
\le K_3(\varepsilon+cs),\qquad
\|W^{(2)}(s)\|_{\rm op}\le M+cK_3(\varepsilon s+cs^2/2)\le K_2.
\tag{4}
\]
These also bound Frobenius norms of the trained increments. The lower
velocity has Euclidean norm divided by \(\sqrt n\) at most
\(K_2K_3(\varepsilon+cs)\). Thus the locally Lipschitz finite-dimensional
system has no finite-time escape; the bounds apply to its unique
trajectory on \([0,S]\).

For \(D_\ell=\operatorname{diag}(\phi'(z^{(\ell)}))\), direct
differentiation of all trained factors yields
\[
(h^{(1)})'=D_1^2(W^{(2)})^T\delta^{(2)},\qquad
(z^{(2)})'=
\left(\frac{\|h^{(1)}\|_2^2}{n}I+
 W^{(2)}D_1^2(W^{(2)})^T\right)\delta^{(2)},
\]
\[
(z^{(3)})'=
\frac{\|h^{(2)}\|_2^2}{n}\delta^{(3)}
+W^{(3)}QD_2(z^{(2)})'.
\tag{5}
\]
No derivative of \(\tau\) is used. Equations (3)--(5) imply the actual
velocity bound with its initial-time factor:
\[
\frac{\|(z^{(3)})'(s)\|_2}{\sqrt n}\le K(\varepsilon+cs),
\qquad 0\le s\le S.
\tag{6}
\]
These deductions are deterministic for every \(Q\) and every allowed
\(\tau\); no probability event depending on their paths is introduced.

## Scalar sign-lag inequality

Let \(z:[0,t]\to\mathbb R\) be absolutely continuous, and set
\[
\bar a(v)=\int_0^v\phi(z(u))\,du,\quad
V(t)=\int_0^t|z'(u)|\,du,\quad
U(t)=\int_0^t u|z'(u)|\,du.
\]
Then for every \(0\le v\le t\),
\[
[\bar a(v)\phi''(z(v))]_+\le2V(t)U(t),
\qquad [x]_+=\max\{x,0\}.
\tag{7}
\]
To prove this, a positive left side requires
\(\bar a(v)z(v)<0\), since
\(\phi''(z)=-2z/(1+z^2)^2\). If \(z(v)>0\) and \(\bar a(v)<0\),
some \(u\le v\) has \(z(u)<0\), so \(|z(v)|\le V(v)\).
The same conclusion holds with both signs reversed. Also, in either case,
\[
|\bar a(v)|\le
\left|\int_0^v[\phi(z(v))-\phi(z(u))]\,du\right|
\le\int_0^v|z(v)-z(u)|\,du
\le\int_0^v u|z'(u)|\,du=U(v).
\]
The final inequality follows by integrating
\(|z(v)-z(u)|\le\int_u^v|z'(r)|\,dr\) and interchanging
nonnegative integrals. Consequently
\[
[\bar a(v)\phi''(z(v))]_+
\le\frac{2V(v)U(v)}{(1+z(v)^2)^2}\le2V(t)U(t).
\]
If the product is not positive, (7) holds by nonnegativity of the
right side. At \(v=0\), \(\bar a(0)=0\). No sign assumption on the
whole path is needed.

For \(a(v)=a(0)+\bar a(v)\), the elementary inequality
\([x+y]_+\le[x]_++|y|\) and \(|\phi''|\le2\) give
\[
\sup_{0\le v\le t}[a(v)\phi''(z(v))]_+
\le2|a(0)|+2V(t)U(t).
\tag{8}
\]
The initial term cannot be omitted when the readout is nonzero.

## Actual canonical positive-part and Hessian consequences

Apply (8) separately to each actual top neuron, using
\[
V_i^{(3)}(t)=\int_0^t|(z_i^{(3)})'(u)|\,du,\qquad
U_i^{(3)}(t)=\int_0^t u|(z_i^{(3)})'(u)|\,du.
\]
Minkowski's inequality and (6) show
\[
\frac{\|V^{(3)}(t)\|_2}{\sqrt n}
\le K(\varepsilon t+ct^2/2),\qquad
\frac{\|U^{(3)}(t)\|_2}{\sqrt n}
\le K(\varepsilon t^2/2+ct^3/3).
\tag{9}
\]
The time supremum is taken coordinatewise before summing. Cauchy--Schwarz
in (8), together with \(n^{-1}\sum_i|W_i^{(4)}(0)|\le\varepsilon\),
proves
\[
\begin{split}
\frac1n\sum_i\sup_{0\le v\le t}
[W_i^{(4)}(v)\phi''(z_i^{(3)}(v))]_+
\le 2\varepsilon+
2K^2(\varepsilon t+ct^2/2)
       (\varepsilon t^2/2+ct^3/3).
\end{split}
\tag{10}
\]
In particular, exactly zero readout gives
\[
\frac1n\sum_i\sup_{0\le v\le t}
[W_i^{(4)}(v)\phi''(z_i^{(3)}(v))]_+
\le\frac{K^2c^2}{3}t^5 .
\tag{11}
\]
This is a uniform-width inequality on an actual positive interval,
not an assertion about a coefficient at zero. It holds for all
\(t\in[0,S]\), with \(K\) depending on \(S,M\).

Now impose the canonical independent initialization:
\(z_i^{(1)}(0)\sim N(0,1)\), both hidden matrices have independent
\(N(0,1/n)\) entries, and \(W^{(4)}(0)=G^{(4)}/n\) with independent
standard Gaussian \(G_i^{(4)}\), independent of the hidden blocks.
For \(n\ge2\), on
\[
\|W^{(2)}(0)\|_{\rm op},\|W^{(3)}(0)\|_{\rm op}\le10,\qquad
\|G^{(4)}\|_2/\sqrt n\le2,
\tag{12}
\]
we have \(\varepsilon\le2/n\le1\). Hence (10) implies
\[
\frac1n\sum_i\sup_{0\le v\le t}
[W_i^{(4)}(v)\phi''(z_i^{(3)}(v))]_+
\le C_S(n^{-1}+t^5),\qquad 0\le t\le S.
\tag{13}
\]
Indeed the product in (10) is a fixed combination of
\(\varepsilon^2t^3,\varepsilon t^4,t^5\); the first two are at most
\(C_S/n\) on this event. The event (12) has probability at least
\[
1-4e^{-(25/2-2\log9)n}-e^{-(1-\frac12\log2)n}.
\tag{14}
\]
For completeness, a maximal \(1/4\)-separated spherical set has at most
\(9^n\) points by disjoint radius-\(1/8\) ball packing. It is a
\(1/4\)-net. Approximating both arguments of a bilinear form makes
its matrix operator norm at most twice its maximum over two such nets.
Each fixed Gaussian bilinear form has variance \(1/n\), so its two-sided
tail at \(M/2\) is at most \(2e^{-nM^2/8}\). Union over both matrices
and both nets gives the first error in (14) at \(M=10\).
Finally \(\mathbb E e^{\|G^{(4)}\|_2^2/4}=2^{n/2}\);
Markov's inequality at squared norm \(4n\) gives the second error.
No conditioning on (12) is used to claim a Gaussian trained law.

Because the estimates before (12) are deterministic, this single
initial event simultaneously controls every fixed mask \(Q\) and every
allowed clipping map \(\tau\), with the same \(C_S\). This particular
uniformity does not assert a uniform tail bound for \(q^{(2)}\).

The canonical estimate also holds in expectation, without restricting
to the good event. Here are the needed uniform-integrability details.
For unrestricted finite initial data let
\(M_0=\max(\|W^{(2)}(0)\|_{\rm op},\|W^{(3)}(0)\|_{\rm op})\)
and retain \(\varepsilon=\|W^{(4)}(0)\|_2/\sqrt n\), which may exceed
one. Replace (3) by the random polynomial bounds
\[
\begin{gathered}
K_3^{\rm ran}=M_0+c(\varepsilon S+cS^2/2),\\
K_2^{\rm ran}=M_0+cK_3^{\rm ran}(\varepsilon S+cS^2/2),\\
K^{\rm ran}=c^2+(K_3^{\rm ran})^2(c^2+(K_2^{\rm ran})^2).
\end{gathered}
\tag{14a}
\]
The identical deterministic proof establishes (10) with \(K^{\rm ran}\).
For the canonical matrices, the net bound above implies for \(r\ge10\)
\[
\mathbb P(M_0>r)\le4e^{2n\log9-nr^2/8}\le4e^{-r^2/16}.
\]
The last inequality uses \(r^2/16\ge2\log9\) and \(n\ge1\).
Tail integration therefore bounds every fixed positive moment of
\(M_0\), uniformly in width. For every positive integer \(k\),
\[
\mathbb E\varepsilon^{2k}
=n^{-3k}\prod_{j=0}^{k-1}(n+2j)\le C_k n^{-2k}.
\tag{14b}
\]
The product formula follows by differentiating
\(\mathbb E e^{\lambda\|G^{(4)}\|_2^2}=(1-2\lambda)^{-n/2}\)
at zero. Its finite derivatives are justified, for example, by
domination using any fixed \(0<\lambda<1/2\).
Thus every fixed moment of each polynomial in (14a) is uniformly
bounded. Expanding (10) gives terms
\[
2\varepsilon+(K^{\rm ran})^2\varepsilon^2t^3
+\frac{7c}{6}(K^{\rm ran})^2\varepsilon t^4
+\frac{c^2}{3}(K^{\rm ran})^2t^5.
\]
Cauchy--Schwarz, the fourth moment of \(K^{\rm ran}\), and (14b)
bound their expectations by \(C_S(n^{-1}+t^5)\), for \(t\le S\).
Consequently
\[
\mathbb E\left[\frac1n\sum_i\sup_{0\le v\le t}
[W_i^{(4)}(v)\phi''(z_i^{(3)}(v))]_+\right]
\le C_S(n^{-1}+t^5).
\tag{14c}
\]
The same measurable polynomial dominating variable works for every
mask and clipping. Thus (14c) is uniform over prescribed choices,
and remains valid for any choice for which the resulting trajectories
are measurable. No exchange with an uncountable supremum is needed.

There is also a precise top-input Hessian interpretation. For the full
network at a fixed time \(s\), regard the middle activation as a free
input \(u\), holding the current trained \(W^{(3)},W^{(4)}\) fixed:
\[
u\longmapsto\frac1n(W^{(4)}(s))^T\phi(W^{(3)}(s)u).
\]
At \(u=h^{(2)}(s)\), its ordinary Euclidean Hessian is
\[
\mathcal H^{(2)}(s)=\frac1n(W^{(3)}(s))^T
\operatorname{diag}(W^{(4)}(s)\odot\phi''(z^{(3)}(s)))W^{(3)}(s).
\tag{15}
\]
For a symmetric matrix \(H\), let \(H_+\) keep its positive eigenvalues
and replace its nonpositive eigenvalues by zero. Define the positive
semidefinite majorant of (15) by taking the positive part of the
diagonal before conjugating by \(W^{(3)}\). The Loewner inequality
\(\mathcal H^{(2)}\le P\), \(P\ge0\), implies
\(\operatorname{Tr}[(\mathcal H^{(2)})_+]\le\operatorname{Tr}P\):
project onto the positive eigenspace of \(\mathcal H^{(2)}\) and use
positivity of \(P\) on its orthogonal complement. Moreover
\[
\operatorname{Tr}P
=\frac1n\sum_i[W_i^{(4)}\phi''(z_i^{(3)})]_+
                    \|\text{row}_i(W^{(3)})\|_2^2
\le\frac{K_3^2}{n}\sum_i[W_i^{(4)}\phi''(z_i^{(3)})]_+.
\]
Thus (10)--(13) bound
\(\sup_{s\le t}\operatorname{Tr}[(\mathcal H^{(2)}(s))_+]\)
by \(K_3^2\) times their respective right sides.
The expectation bound \(C_S(n^{-1}+t^5)\) holds for this supremum
as well: use (14a), the same expansion, and the uniformly bounded
fourth moments of \(K_3^{\rm ran}\) and \(K^{\rm ran}\) (or their
higher fixed moments for their products).

In particular, for a fresh standard Gaussian vector \(\xi\) independent
of the actual network, conditioning on that network gives
\[
\mathbb E_\xi[(\xi^T\mathcal H^{(2)}(s)\xi)_+]
\le \operatorname{Tr}[(\mathcal H^{(2)}(s))_+] .
\tag{16}
\]
This follows pointwise from
\(\xi^TH\xi\le\xi^TH_+\xi\) and then
\(\mathbb E_\xi\xi\xi^T=I\). It describes an isotropic instantaneous
input probe, not a transported gradient-flow response.

The factor \(1/n\) in (15) is essential: for the metric
\(\|u\|_2/\sqrt n\), the curvature operator is \(n\mathcal H^{(2)}\).
Equation (13) controls its positive trace divided by \(n\); it does not
transfer the same \(n^{-1}+t^5\) scale to a width-independent positive
operator norm in the RMS metric. This does not exclude a different,
rougher operator bound from the coordinatewise readout estimate.
For a transported probe with conditional mean zero and conditional
covariance \(\Gamma\) given the actual network, its conditional positive
work is at most \(\operatorname{Tr}((\mathcal H^{(2)})_+\Gamma)\).
For conditional mean \(m\), replace \(\Gamma\) by
\(\Gamma+mm^T\). No uniform bound on these quantities follows from the
trace estimate without controlling the conditional second moment or
its alignment.

## Scope of the result

The proof uses the actual sign lag and actual preactivation movement.
It establishes a signed positive-part estimate for the top curvature,
uniform over width, time prefixes, masks and dominated 1-Lipschitz
clippings on a canonical event of probability tending to one.
It uses no external theorem, no finite-jet transfer and no experiment.
It does not establish coordinatewise nonpositivity, a bound on the
middle curvature multiplier, transported response amplitude, deletion
stability, population restartability or the requested global theorem.
