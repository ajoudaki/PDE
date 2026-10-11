# A fixed-dimension source-rank obstruction to full polynomial onset

2026-10-11. Scoped mathematical route. No numerical experiments, manuscript
changes, or Git operations. The inputs are `WIDTH_UPGRADE.md`, the permitted
prior study's `HARMONIC_FIXED_DIMENSION_SCOPE.md`, and the current Harmonic
source/selection construction in `paper/compact_foundations.tex` and
`paper/compact_selected.tex`. This is an internally derived result, not an
independent promotion review.

The unchanged Harmonic source criterion and headline cannot have a sufficient
width polynomial jointly in inverse gap and inverse labels over the full
allowed small-label range, even with fixed \(d=m=L=2\). A finite Gram
argument proves this directly from initialized first-layer features. Neither
improved temporal analyticity, a residual clock, nor removal of redundant
temporal coefficients fixes this particular obstruction: it already occurs
at time zero.

The obstruction uses labels that shrink along the problem family. It does
**not** resolve the narrower fixed-label-to-gap-ratio question in the prior
scope note, and it is not an impossibility theorem for arbitrary compressed
predictors that avoid the paper's source-approximation requirement.

## 1. Exactly which class and width claim are tested

The current Harmonic model uses source spaces
\(E_j\subset\mathbb R^n\) that approximate, in coordinate norm, the
four families of `cp:source-families`, uniformly on the sphere and the source
time interval, including zero. In particular its first-layer space satisfies
\[
\text{for every }v\in S^{d-1},\qquad
\inf_{u\in E_1}\|h_0^{(1)}(v)-u\|_\infty\le\eta,
\qquad h_0^{(1)}(v)=\phi_1(W_0^{(1)}v).
\tag{1}
\]
The current tolerance in `cp:selected-tolerance` has \(\eta\le Y\),
where \(Y=\|y\|_2/\sqrt m>0\). The same inequality is present in
the general source-to-runtime transfer. No temporal approximation choice
changes the initialized feature family in (1).

Selection produces \(I_1\subset\{1,\ldots,n\}\) and a positive
metric \(M_1\) satisfying
\[
u_{I_1}^{\top}M_1u_{I_1}=\|u\|_2^2/n
\quad\text{for every }u\in E_1.
\tag{2}
\]
Thus restriction to \(I_1\) is injective on \(E_1\), and
\(\dim E_1\le|I_1|\). The current retained inventory contains at
least \(|I_1|\) real coordinates (indeed the first-layer weights alone
contain \(d|I_1|\)). A lower bound for actual source-space dimension
therefore gives a lower bound for current retained state, independently
of a coefficient-count upper bound.

Write
\[
\lambda=\gamma/m,\qquad z=Y/\lambda,\qquad \ell=\log(en).
\]
Here \(z\) denotes the label-to-gap ratio, not a preactivation. The
headline being preserved is
\[
S_n\le C(m+d)^2+
       (C/d)^{d+1}z^4\ell^{3d+2},
\tag{3}
\]
where \(S_n\) is the total retained real-coordinate count and \(C\)
may depend only on activations and depth. The tested polynomial-onset claim
has a polynomial \(P\), with parameter-independent coefficients once
activations and depth are fixed, that makes (1)--(3) hold with prescribed
fixed confidence at every width
\(n\ge P(m,d,\gamma^{-1},Y^{-1},\delta^{-1})\).
Other fixed accuracy parameters can be arguments of \(P\) without
changing the argument. Allowing an arbitrary label-dependent coefficient
inside \(P\) would be a different claim.

## 2. An admissible fixed-dimensional initialized kernel of unlimited rank

Use the same activation in each of two layers:
\[
\phi(u)=u+\cos u.
\tag{4}
\]
It is entire, real on the real axis, nonaffine, and has bounded first and
second derivatives on every strip of finite width. For example, on
\(|\operatorname{Im}u|<1\),
\(|\phi'(u)|\le1+\cosh1\) and \(|\phi''(u)|\le\cosh1\).
Its activation envelope \(\beta\) is fixed and finite; unbounded
activation values are expressly allowed by the paper.

Let \(g\sim\mathcal N(0,I_2)\) and let \(v,w\) be real unit vectors.
With \(c=v^\top w\), Gaussian symmetry makes the mixed linear/cosine
terms vanish. The cosine product identity and the Gaussian characteristic
function give
\[
\begin{split}
K(v,w)&:=\mathbb E[\phi(g^\top v)\phi(g^\top w)]\\
&=c+\tfrac12\{e^{-(2-2c)/2}+e^{-(2+2c)/2}\}
=c+e^{-1}\cosh c.
\end{split}
\tag{5}
\]

For any integer \(J\ge1\), choose directions
\[
v_j=(\cos\theta_j,\sin\theta_j),\qquad
\theta_j=\frac{j\pi}{2(J+1)},\quad 1\le j\le J.
\tag{6}
\]
Their squared first coordinates \(a_j=\cos^2\theta_j\) are distinct.
Let \(K_J=(K(v_i,v_j))_{i,j=1}^J\). This matrix is positive definite.

To prove it, for real coefficients \(b_1,\ldots,b_J\), expand (5):
\[
b^\top K_Jb
=\left\|\sum_jb_jv_j\right\|_2^2
+e^{-1}\sum_{k=0}^{\infty}\frac1{(2k)!}
       \left\|\sum_jb_jv_j^{\otimes2k}\right\|_2^2.
\tag{7}
\]
The tensor power at \(k=0\) is the scalar one. Equation (7) follows
from \(\langle v_i^{\otimes 2k},v_j^{\otimes 2k}\rangle
=(v_i^\top v_j)^{2k}\); absolute convergence permits summing the finite
quadratic form termwise. All terms are nonnegative. If (7) is zero, the
component of each tensor with all coordinate indices equal to one gives
\[
\sum_{j=1}^J b_ja_j^k=0,\qquad k=0,\ldots,J-1.
\]
The Vandermonde determinant is \(\prod_{i<j}(a_j-a_i)\ne0\), so
all \(b_j\) vanish. Consequently
\[
\mu_J:=\lambda_{\min}(K_J)>0.
\tag{8}
\]
The positive number \(\mu_J\) may be extremely small; no quantitative
lower bound in \(J\) is needed. Once \(J\) is fixed, it is independent
of width, training inputs, labels, and the training Gram gap.

## 3. A simultaneous lower bound for every approximate source space

The rows \(g_i\) of \(W_0^{(1)}\in\mathbb R^{n\times2}\) are
independent \(\mathcal N(0,I_2)\). Form
\[
H_{ij}=\phi(g_i^\top v_j),\qquad
G_{n,J}=H^\top H/n.
\tag{9}
\]
This Gram uses the fixed test directions (6), which are available because
Harmonic promises the whole sphere. They are not extra training data and
receive no labels.

There is a simple quantitative event:
\[
\Pr\{G_{n,J}\succeq(\mu_J/2)I_J\}
\ge1-\frac{128J^4}{n\mu_J^2}.
\tag{10}
\]
Indeed \(|\phi(G)|\le|G|+1\) for real standard Gaussian \(G\), so
\[
\mathbb E|\phi(G)|^4\le8(\mathbb E|G|^4+1)=32.
\]
Cauchy--Schwarz bounds the second moment of every product
\(H_{ia}H_{ib}\) by 32. Independence of rows and Chebyshev's inequality
give
\[
\Pr\{|(G_{n,J}-K_J)_{ab}|>\mu_J/(2J)\}
\le\frac{128J^2}{n\mu_J^2}.
\]
Union over the \(J^2\) entries and use
\(\|G_{n,J}-K_J\|_{\rm op}\le J\max_{a,b}|(G_{n,J}-K_J)_{ab}|\).
This proves (10).

On the event in (10), every space \(E\subset\mathbb R^n\) satisfying
(1) at the \(J\) test directions must have
\[
\dim E\ge J\qquad\text{whenever}\qquad
\eta<\sqrt{\mu_J/(2J)}.
\tag{11}
\]
For otherwise choose approximants \(u_j\in E\) with coordinate error
at most \(\eta\), and let \(A=H/\sqrt n\),
\(B=[u_1,\ldots,u_J]/\sqrt n\). Then
\(\operatorname{rank}B<J\) and \(\|A-B\|_F\le\sqrt J\eta\).
Take a unit vector \(b\in\ker B\). By (10),
\[
\sqrt{\mu_J/2}\le\|Ab\|_2
=\|(A-B)b\|_2\le\sqrt J\eta,
\]
contradicting (11). If an infimum in (1) is written without a minimizer,
use errors \(\eta+\varepsilon\) and let \(\varepsilon\downarrow0\).

This conclusion is simultaneous over **all** source spaces, including
spaces and selected supports chosen after seeing the dense initialization.
No union bound over candidate spaces and no concentration hypothesis for
later trained features are used. It is a lower bound on actual approximate
source rank, not on the number of coefficients produced by a particular
temporal approximation.

## 4. A necessary stretched-exponential gate for the unchanged headline

Fix a proposed activation/depth coefficient \(C>0\) in (3), and let
\[
J=\lfloor16C\rfloor+2,\qquad
\Delta_C=J-16C>1,\qquad A_C=(C/2)^3.
\tag{12}
\]
For \(m=d=2\), (3) reads
\[
S_n\le16C+A_Cz^4\ell^8.
\tag{13}
\]
When \(Y<\sqrt{\mu_J/(2J)}\), the current \(\eta\le Y\) and
(10)--(11) force \(\dim E_1\ge J\). By (2), \(S_n\ge J\).
Thus, on the event in (10), simultaneous source compliance and the unchanged
headline require
\[
A_Cz^4\ell^8\ge\Delta_C,
\qquad
\ell\ge c_Cz^{-1/2},\quad
c_C=(\Delta_C/A_C)^{1/8}>0.
\tag{14}
\]
Equivalently,
\[
n\ge\exp(c_Cz^{-1/2}-1).
\tag{15}
\]
This gate is necessary for the present source-space/selection class whenever
the small-label condition above holds and the initialized Gram event occurs.
It does not come from the original short-contour gate. Enlarging the
temporal analytic domain or reducing temporal coefficient redundancy leaves
it unchanged.

For example, at confidence \(1-\varepsilon\), the event in (10) holds
once \(n\ge128J^4/(\varepsilon\mu_J^2)\). This auxiliary threshold
depends only on the fixed \(C\) and activation, not on the shrinking
labels or gap. If (14) fails at such a width, the probability that an
initializer simultaneously meets the source criterion and headline is at
most \(\varepsilon\).

## 5. An admissible joint gap/label family at fixed dimension

Take two unit training inputs in \(\mathbb R^2\) with correlation
\(c_0\in(0,1)\) tending to one, and \(L=2\) with activation (4).
The corresponding population feature Gram at layer \(j\) is
\(\left(\begin{smallmatrix}q_j&c_j\\c_j&q_j\end{smallmatrix}\right)\),
where the initial input Gram has \(q_0=1\) and
\[
q_{j+1}=q_j+e^{-q_j}\cosh q_j,\qquad
c_{j+1}=c_j+e^{-q_j}\cosh c_j.
\tag{16}
\]
These formulas follow by the same Gaussian calculation as (5), now with
common variance \(q_j\). For \(0\le c<q\), the map
\(c\mapsto c+e^{-q}\cosh c\) is strictly increasing, so
\(0<c_j<q_j\) at each layer. The smallest final Gram eigenvalue is
\(\gamma=q_2-c_2>0\). Continuity of (16) gives
\(\gamma\downarrow0\) as \(c_0\uparrow1\). Let
\[
\lambda=\gamma/2,\qquad z=\lambda,\qquad Y=\lambda^2,
\qquad y_1=y_2=Y.
\tag{17}
\]
Eventually \(0<\lambda\le1\) and \(z\le\beta^{-60}\), so every
current label/gap hypothesis is met. The normalization of the original
inputs is \(x_a=\sqrt2\,v_a\), exactly as in the paper.

Fix any proposed polynomial sufficient width in
\(\gamma^{-1},Y^{-1}\), with all other parameters and a positive
confidence fixed. Along (17), it is bounded by a fixed power of
\(\lambda^{-1}\). Choose widths above that polynomial and still of
polynomial size, for example \(n_\lambda=\lceil\lambda^{-A}\rceil\)
for a sufficiently large fixed \(A\). Then
\[
\ell_\lambda=O(\log(1/\lambda)),\qquad
z^4\ell_\lambda^8=\lambda^4O(\log(1/\lambda)^8)\longrightarrow0,
\]
while \(Y\to0\) and the probability in (10) tends to one. Equations
(11)--(13) are therefore incompatible with probability tending to one.
More explicitly, the necessary width gate (15) becomes
\[
n\ge\exp(c_C/\sqrt\lambda-1),
\tag{18}
\]
which exceeds every fixed polynomial in \(\gamma^{-1}\) and
\(Y^{-1}=\lambda^{-2}\). This disproves the proposed full polynomial
onset for the unchanged source criterion and retained headline, even with
fixed dimension and sample count. It does not rely on any contested
quantitative stopped-source lemma.

The use of varying datasets and labels here tests the proposed uniform
parameter-dependent threshold: it would apply at every admissible dataset
and every width above its prescribed polynomial. It does not contradict the
paper's original eventual theorem for each separately fixed dataset and
positive label size; that theorem permits a threshold as large as (18).

## 6. What this settles, and what it does not

The root cause is the factor \(z^4\) in the retained-state term. At widths
polynomial in shrinking \(z^{-1}\), that term tends to zero, leaving a
constant total state allowance. Yet the unchanged absolute source criterion
asks a fixed nonpolynomial initialized feature family to be approximated
with error at most \(Y\to0\). Its actual approximate rank cannot remain
bounded. The whole-sphere promise makes the finite test set (6) available
regardless of training sample count.

Consequently, the following proposed repairs cannot establish a full
polynomial onset while retaining (1)--(3): changing the temporal clock,
enlarging the temporal complex domain, using adaptive temporal panels,
eliminating linearly dependent temporal coefficients, or merely fixing
\(d\). These changes leave the time-zero rank requirement intact.

The conclusion has explicit limits:

- It uses \(z\to0\). The prior fixed-\(z>0\), small-gap question is
  still open. The headline's logarithmic term then grows, so (14) is a
  constant gate rather than an exponential inverse-gap gate.
- It does not assert failure at fixed positive \(Y\). The label cap
  itself bounds \(\lambda^{-1}\) when \(Y\) is held fixed. A theorem
  allowing an arbitrary nonpolynomial coefficient depending on that fixed
  \(Y\) is not refuted by this family.
- It concerns the source approximation and exact source-metric mechanism
  in the present construction. An output-level compression proof that
  avoids (1), or a modified source criterion weighted by labels or
  observability, would require a separate analysis. This note does not
  prove such a method impossible, nor authorize changing the user's scope.
- It is stronger than a coefficient-count diagnosis but does not provide
  a quantitative rank-growth law in \(J\). The finite positive
  \(\mu_J\) suffices to exclude every polynomial onset over the stated
  shrinking-label range.

Thus fixing dimension removes neither the original proof's fixed-\(z\)
contour gap nor this independent obstruction to a full-label-range
polynomial-onset theorem with unchanged source requirements and headline.
