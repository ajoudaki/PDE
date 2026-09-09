# Actual canonical middle curvature: a uniform positive-time test

Candidate two-note theorem, pending an isolated complete audit together
with GAUSSIAN_MIDDLE_CURVATURE_INITIAL_LAW.md. The only separate proof
dependency is the initial joint empirical-average law stated in Section 3.
The dynamical estimates below are proved directly from the canonical
tiny-readout trajectory, not by comparing it with an evolved zero-readout
trajectory or by transferring a finite Taylor jet.

The quantity under study is
\([q_i^{(2)}\phi''(z_i^{(2)})]_+\), where
\(q^{(2)}=(W^{(3)})^T\delta^{(3)}\).
It is the positive part of the actual middle curvature coefficient,
not the top coefficient \(W^{(4)}\phi''(z^{(3)})\).
The proposed conclusion is that its empirical mean has positive linear
onset on actual common feature-time intervals under the canonical law.
This rules out a fifth-order top-to-middle positive-part shortcut.
It is not a population continuation theorem or a counterexample to one.

## 1. Exact dynamics and deterministic path bounds

Let \(\phi=\arctan\), \(c=\pi/2\), and fix a feature horizon \(S>0\).
The first layer is the vector \(z^{(1)}=W^{(1)}\); the hidden matrices
are \(W^{(2)},W^{(3)}\); \(W^{(4)}\) is the rescaled readout vector.
Use ordinary Euclidean vector norms, ordinary matrix operator and
Frobenius norms, and finite transpose \(T\). Define
\[
h^{(\ell)}=\phi(z^{(\ell)}),\quad
z^{(2)}=W^{(2)}h^{(1)},\quad z^{(3)}=W^{(3)}h^{(2)},
\]
\[
\delta^{(3)}=W^{(4)}\odot\phi'(z^{(3)}),\quad
q^{(2)}=(W^{(3)})^T\delta^{(3)},\quad
\delta^{(2)}=\phi'(z^{(2)})\odot\tau(q^{(2)}).
\]
Here \(\tau\) is any fixed prescribed map with
\(|\tau(v)|\le|v|\) and \(|\tau(v)-\tau(w)|\le|v-w|\).
The identity gives the exact uncut model. There is no pruning mask.
Every trained block obeys its actual feature equation:
\[
\begin{gathered}
(z^{(1)})'=\phi'(z^{(1)})\odot(W^{(2)})^T\delta^{(2)},\\
(W^{(2)})'=\delta^{(2)}(h^{(1)})^T/n,\quad
(W^{(3)})'=\delta^{(3)}(h^{(2)})^T/n,\quad
(W^{(4)})'=h^{(3)}.
\end{gathered}
\tag{1}
\]
The estimates are in feature time \(s\), not physical time. The canonical
uncut physical flow is (1) times \(2(1-f)\), for
\(f=(W^{(4)})^Th^{(3)}/n\) and loss \((f-1)^2\).
No physical-clock or exact-GD convergence assertion is made here.

For arbitrary finite initial data put
\[
M=\max_{\ell=2,3}\|W^{(\ell)}(0)\|_{\rm op},\qquad
\varepsilon=\frac{\|W^{(4)}(0)\|_2}{\sqrt n},\qquad
\alpha=\|W^{(4)}(0)\|_\infty.
\]
These definitions impose no upper bound on \(\varepsilon,\alpha\).
In particular \(\varepsilon\le\alpha\le\sqrt n\,\varepsilon\).
Define the finite nonnegative constants
\[
\begin{gathered}
K_3=M+c(\varepsilon S+cS^2/2),\\
K_2=M+cK_3(\varepsilon S+cS^2/2),\\
J=K_3(c^2+K_2^2),\qquad K=c^2+K_3J.
\end{gathered}
\tag{2}
\]
They are polynomials in \(M,\varepsilon\), with coefficients depending
only on \(S\). The readout equation and \(|\phi|\le c\), \(|\phi'|\le1\)
give
\[
\frac{\|\delta^{(3)}(s)\|_2}{\sqrt n}
\le\frac{\|W^{(4)}(s)\|_2}{\sqrt n}\le\varepsilon+cs,\qquad
\|W^{(4)}(s)\|_\infty\le\alpha+cs.
\tag{3}
\]
Using \(\|uv^T/n\|_{\rm F}=\|u\|_2\|v\|_2/n\) in (1) yields
\[
\|W^{(3)}(s)-W^{(3)}(0)\|_{\rm F}
\le c(\varepsilon s+cs^2/2),\quad
\|W^{(3)}(s)\|_{\rm op}\le K_3,
\]
\[
\frac{\|\delta^{(2)}(s)\|_2}{\sqrt n}\le K_3(\varepsilon+cs),
\quad
\|W^{(2)}(s)-W^{(2)}(0)\|_{\rm F}
\le cK_3(\varepsilon s+cs^2/2),\quad
\|W^{(2)}(s)\|_{\rm op}\le K_2.
\tag{4}
\]
The first-layer velocity divided by \(\sqrt n\) is at most
\(K_2K_3(\varepsilon+cs)\).
At each fixed width, the vector field is locally Lipschitz, including
the Lipschitz clipping. Local existence and uniqueness follow from the
contraction of its integral equation on a sufficiently short interval
in a finite-dimensional ball. The displayed bounds keep every parameter
entry in a bounded set on a prescribed finite horizon. A hypothetical
finite endpoint then has a state limit, since the vector field is
bounded on that compact set, and local existence extends it.
Thus (1) has a unique trajectory through \([0,S]\).

Differentiating only the forward factors gives the exact identities
\[
(z^{(2)})'=
\left[\frac{\|h^{(1)}\|_2^2}{n}I+
W^{(2)}\operatorname{diag}(\phi'(z^{(1)})^2)(W^{(2)})^T\right]\delta^{(2)},
\]
\[
(z^{(3)})'=\frac{\|h^{(2)}\|_2^2}{n}\delta^{(3)}
+W^{(3)}\operatorname{diag}(\phi'(z^{(2)}))(z^{(2)})'.
\tag{5}
\]
No derivative of \(\tau\) is used. Consequently
\[
\frac{\|(z^{(2)})'(s)\|_2}{\sqrt n}\le J(\varepsilon+cs),\qquad
\frac{\|(z^{(3)})'(s)\|_2}{\sqrt n}\le K(\varepsilon+cs).
\tag{6}
\]
Integration bounds the corresponding displacements by
\(J(\varepsilon s+cs^2/2)\) and \(K(\varepsilon s+cs^2/2)\).

## 2. A direct Duhamel remainder for the actual middle query

Let \(g(v)=\phi'(v)\phi(v)\) and define the initial hidden-block query
\[
u_n^{(2)}=(W^{(3)}(0))^T g(z^{(3)}(0)).
\tag{7}
\]
This is a function only of the original hidden initialization, not an
extra random readout seed. We use
\[
|g|\le c,\quad |g'|=|(\phi')^2+\phi\phi''|\le1+2c,\quad
|\phi''|\le2,\quad
|\phi'''(v)|=\frac{|-2+6v^2|}{(1+v^2)^3}\le8.
\tag{8}
\]
In particular \(\|u_n^{(2)}\|_2/\sqrt n\le Mc\).

Differentiate the actual query, retaining the trained \(W^{(3)}\):
\[
\begin{split}
(q^{(2)})'
={}&h^{(2)}\frac{\|\delta^{(3)}\|_2^2}{n}
+(W^{(3)})^Tg(z^{(3)})\\
&+(W^{(3)})^T
\bigl[W^{(4)}\odot\phi''(z^{(3)})\odot(z^{(3)})'\bigr].
\end{split}
\tag{9}
\]
The first term is exactly \(((W^{(3)})')^T\delta^{(3)}\); the other
terms come from
\((\delta^{(3)})'=g(z^{(3)})+
W^{(4)}\odot\phi''(z^{(3)})\odot(z^{(3)})'\).
Thus (9) also holds for merely Lipschitz clipping.

For \(A=c^2+M(1+2c)K\), (4), (6), and (8) give
\[
\frac{\|(W^{(3)}(s))^Tg(z^{(3)}(s))-u_n^{(2)}\|_2}{\sqrt n}
\le A(\varepsilon s+cs^2/2).
\tag{10}
\]
Indeed the trained-matrix increment contributes at most
\(c^2(\varepsilon s+cs^2/2)\); the change of \(g\) contributes at most
\(M(1+2c)K(\varepsilon s+cs^2/2)\).
The other two terms of (9) have norms divided by \(\sqrt n\) bounded by
\[
c(\varepsilon+cs)^2,\qquad
2K_3K(\alpha+cs)(\varepsilon+cs).
\]
Also \(\|q^{(2)}(0)\|_2/\sqrt n\le M\varepsilon\).
Integrating (9)--(10) therefore proves, for every \(0\le s\le S\),
\[
\frac{\|q^{(2)}(s)-s u_n^{(2)}\|_2}{\sqrt n}\le R(s),
\tag{11}
\]
where the explicit nonnegative remainder is
\[
\begin{split}
R(s)={}&M\varepsilon+
c\left(\varepsilon^2s+\varepsilon c s^2+\frac{c^2s^3}{3}\right)\\
&+A\left(\frac{\varepsilon s^2}{2}+\frac{cs^3}{6}\right)\\
&+2K_3K\left(\alpha\varepsilon s+
\frac{c(\alpha+\varepsilon)s^2}{2}+\frac{c^2s^3}{3}\right).
\end{split}
\tag{12}
\]
The initial readout has not been set to zero or hidden in a
width-dependent Taylor remainder.

Define the empirical positive parts
\[
B_n(s)=\frac1n\sum_i[q_i^{(2)}(s)\phi''(z_i^{(2)}(s))]_+,\qquad
c_n=\frac1n\sum_i[(u_n^{(2)})_i\phi''(z_i^{(2)}(0))]_+.
\tag{13}
\]
The map \(x\mapsto[x]_+\) is 1-Lipschitz. Separate the query change
from the change of \(\phi''\), then use Cauchy--Schwarz and (6), (8):
\[
\begin{split}
|B_n(s)-s c_n|
&\le 2\frac{\|q^{(2)}(s)-s u_n^{(2)}\|_2}{\sqrt n}\\
&\quad+8s\frac{\|u_n^{(2)}\|_2}{\sqrt n}
\frac{\|z^{(2)}(s)-z^{(2)}(0)\|_2}{\sqrt n}\\
&\le 2R(s)+8McJ\,s(\varepsilon s+cs^2/2).
\end{split}
\tag{14}
\]
These inequalities are pathwise, simultaneous in \(s\), and use
constants independent of the choice of allowed fixed clipping.
For \(M\le M_*,\varepsilon\le1,\alpha\le1\), collecting the explicit
terms in (12)--(14) yields
\[
|B_n(s)-s c_n|\le C_{S,M_*}
(\varepsilon+\alpha s^2+s^3),\qquad 0\le s\le S.
\tag{15}
\]
For example, \(\alpha\varepsilon s\le S\varepsilon\),
\(\varepsilon^2s\le S\varepsilon\), and
\(\varepsilon s^2\le S^2\varepsilon\); every remaining term has one
of the two displayed time powers. Equations (2) bound all coefficients
uniformly under these restrictions.

## 3. Canonical initialization and the required initial law

The canonical initial blocks are mutually independent:
\[
z_i^{(1)}(0)\sim N(0,1),\quad
W_{ij}^{(\ell)}(0)\sim N(0,1/n)\ (\ell=2,3),\quad
W_i^{(4)}(0)=G_i^{(4)}/n,\quad G_i^{(4)}\sim N(0,1).
\tag{16}
\]
Independence and identical distribution here concern initialization
only, not trained or reused-matrix coordinate outputs.

The companion GAUSSIAN_MIDDLE_CURVATURE_INITIAL_LAW.md, frozen at SHA256
e028b6146db23f21ba0b35a876e997ff20d89ab3da8edcaa8f3e11e7db1417bb,
is required to prove the following statement. For independent standard Gaussians
\(G_1,G_2,G_3,G\), put
\[
m_1=\mathbb E\phi(G_1)^2,\quad
Z^{(2)}=\sqrt{m_1}G_2,\quad m_2=\mathbb E\phi(Z^{(2)})^2,\quad
Z^{(3)}=\sqrt{m_2}G_3,
\]
\[
\beta=\frac{\mathbb E[Z^{(3)}g(Z^{(3)})]}{m_2},\qquad
\sigma^2=\mathbb E[g(Z^{(3)})^2],\qquad
c_*=\mathbb E\left[
\left[\phi''(Z^{(2)})(\beta\phi(Z^{(2)})+\sigma G)\right]_+\right].
\tag{17}
\]
Then \(m_1,m_2,\sigma,c_*>0\) and \(c_n\to c_*\) in probability
and in \(L^1\). The expectation in the last definition means expectation
of the positive part. The independent \(G\) describes unexplored
conditional Gaussian randomness in the reused hidden matrix, not a
change of the readout initialization.
Until this complete dependency is verified, the deductions invoking it
remain candidate deductions.

Here are the probability and integrability details for applying (14)
directly to (16). On the initial event
\[
\Omega_n=\{M\le10,\ \|G^{(4)}\|_2/\sqrt n\le2\},
\tag{18}
\]
one has \(\varepsilon\le2/n\), \(\alpha\le2/\sqrt n\).
For \(n\ge4\), (15) therefore gives
\[
|B_n(s)-s c_n|\le C_S
(n^{-1}+n^{-1/2}s^2+s^3),\quad 0\le s\le S,
\tag{19}
\]
on the same event for every allowed fixed clipping.
Moreover
\[
\mathbb P(\Omega_n^c)\le
4e^{-(25/2-2\log9)n}+e^{-(1-\frac12\log2)n}.
\tag{20}
\]
To check this without a source theorem, a maximal \(1/4\)-separated
spherical set is a \(1/4\)-net with at most \(9^n\) points by disjoint
radius-\(1/8\) ball packing. Approximate both arguments of a bilinear
form using this net; the two errors are at most half the operator norm,
so that norm is at most twice the net maximum. For a fixed pair of unit
vectors a canonical Gaussian matrix bilinear form has variance \(1/n\),
and its two-sided tail at \(r/2\) is at most \(2e^{-nr^2/8}\), by its
Gaussian exponential moment and Markov's inequality. Union over both
matrices and both nets gives
\[
\mathbb P(M>r)\le4e^{2n\log9-nr^2/8}.
\]
Use \(r=10\) for (20). For the readout,
\(\mathbb E e^{\|G^{(4)}\|_2^2/4}=2^{n/2}\);
Markov's inequality at squared norm \(4n\) gives its stated error.

For \(r\ge10\), the same matrix bound is at most \(4e^{-r^2/16}\);
tail integration thus bounds every fixed moment of \(M\) uniformly in
width. Differentiating the Gaussian squared-norm exponential moment
at zero gives, for integers \(k\ge1\),
\[
\mathbb E\varepsilon^{2k}
=n^{-3k}\prod_{j=0}^{k-1}(n+2j)\le C_k n^{-2k},\qquad
\mathbb E\alpha^{2k}\le n^k\mathbb E\varepsilon^{2k}
\le C_k n^{-k}.
\tag{21}
\]
Differentiation is justified by domination with a squared-norm
exponential moment at a fixed positive parameter less than \(1/2\).
All fixed moments of the polynomial constants in (2), (10) and (14)
are consequently uniformly bounded, using Cauchy--Schwarz for their
mixed moments.

For any such polynomial factor \(P\), Cauchy--Schwarz gives
\[
\mathbb E[|P|\varepsilon]\le C_S/n,\quad
\mathbb E[|P|\varepsilon^2]\le C_S/n^2,\quad
\mathbb E[|P|\alpha]\le C_S/\sqrt n.
\]
Also \(\alpha\varepsilon\le\sqrt n\,\varepsilon^2\) gives
\(\mathbb E[|P|\alpha\varepsilon]\le C_S n^{-3/2}\).
Apply these estimates to the unrestricted (12)--(14), not just on
\(\Omega_n\), to obtain
\[
\mathbb E|B_n(s)-s c_n|\le
C_S(n^{-1}+n^{-1/2}s^2+s^3),\qquad 0\le s\le S.
\tag{22}
\]
This holds uniformly over prescribed clippings, including any
measurably selected fixed clipping, because the same measurable
initial-data polynomial dominates (14). No uncountable supremum is
interchanged with expectation.

## 4. Actual positive-time consequences and their limits

Take \(S=1\), and let \(C_1\) be the deterministic constant in (19).
The companion's \(c_*>0\) permits a fixed \(s_0\in(0,1]\) with
\(C_1s_0^2\le c_*/8\). For any fixed \(a\in(0,s_0]\), on the measurable
initial event \(\Omega_n\cap\{c_n\ge3c_*/4\}\), equation (19) gives
\[
\frac{B_n(s)}s\ge\frac{3c_*}{4}
-C_1(n^{-1}/a+n^{-1/2}s_0+s_0^2),
\qquad a\le s\le s_0.
\]
For all sufficiently large \(n\), depending on \(a\), the two
width-dependent terms times \(C_1\) sum to at most \(c_*/8\).
The event has probability tending to one. On it, simultaneously for
every allowed fixed clipping and every \(s\in[a,s_0]\),
\[
B_n(s)\ge\frac{c_*}{2}s.
\tag{23}
\]
This is an actual common positive interval after the width limit,
not a width-dependent Taylor neighborhood. It does not assert (23)
down to arbitrarily small \(s\) uniformly in \(n\).

The positive part is not carried by a vanishing fraction of middle
coordinates on these events. For \(S=1\), set
\[
D=2(1+c)[10+c(1+c/2)].
\]
Increasing the deterministic width threshold so that \(2/n\le a\),
(3)--(4) give for \(a\le s\le s_0\)
\[
\left(\frac1n\sum_i
|q_i^{(2)}(s)\phi''(z_i^{(2)}(s))|^2\right)^{1/2}
\le 2K_3(\varepsilon+cs)\le Ds.
\]
Let \(p_n(s)\) be the fraction of indices with
\(q_i^{(2)}(s)\phi''(z_i^{(2)}(s))\ge c_*s/4\).
The positive-part mean on its complementary indices is at most
\(c_*s/4\). Cauchy--Schwarz on the selected indices, together with
(23), therefore yields
\[
\frac{c_*s}{2}\le B_n(s)\le\frac{c_*s}{4}
+Ds\sqrt{p_n(s)},\qquad
p_n(s)\ge\left(\frac{c_*}{4D}\right)^2>0.
\tag{23a}
\]
This is simultaneous in the same time prefixes and allowed fixed
clippings. It is a positive fraction of scalar curvature coefficients,
not a claim about eigenvalues of a full parameter Hessian.

The expectation version follows with the explicit error:
\[
\mathbb E|B_n(s)-s c_*|
\le C_S(n^{-1}+n^{-1/2}s^2+s^3)+s\,\mathbb E|c_n-c_*|.
\tag{24}
\]
In particular, for each fixed \(s>0\),
\[
c_*s-C_Ss^3\le\liminf_{n\to\infty}\mathbb E B_n(s)
\le\limsup_{n\to\infty}\mathbb E B_n(s)\le c_*s+C_Ss^3.
\tag{25}
\]
The constants are uniform over allowed fixed clippings; (25) also
allows a prescribed width-dependent sequence of such maps.
Taking \(n\to\infty\) first and then \(s\downarrow0\) proves
\[
\lim_{s\downarrow0}\liminf_{n\to\infty}\frac{\mathbb E B_n(s)}s
=\lim_{s\downarrow0}\limsup_{n\to\infty}\frac{\mathbb E B_n(s)}s
=c_*>0.
\tag{26}
\]
Equation (25) alone does not assert convergence in \(n\) at fixed
positive time; its nonzero \(s^3\) error must not be discarded.

Consequently neither coordinatewise nonpositivity of the middle
coefficient nor a canonical mean positive-part bound of fifth order
can be obtained by transplanting the top-layer sign-lag argument.
For any fixed finite proposed coefficient of \(s^5\), choose a small
fixed \(s\le s_0\) where it is less than \(c_*s/2\); (23) contradicts
that bound with probability tending to one. The expectation version
is likewise contradicted by (25) for sufficiently small fixed \(s\).

This does not rule out a positive Gronwall constant, cancellation with
other signed work, or stronger actual response estimates. The coefficient's
positive part is not the Hessian quadratic form of an actual response.
No transported covariance bound, uniform tail envelope, population
restartability, full joint limit, or negative canonical resolution
is established here.
