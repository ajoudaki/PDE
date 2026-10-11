# Arbitrary signed labels on a saturated initialization event

## Scope and status

This is a deterministic positive theorem for the exact finite-width, all-layer
gradient flow specified below. For every fixed label radius, its initialization
conditions hold on a nonempty open set for every finite set of distinct,
nonantipodal unit inputs and every width at least the sample count. Independent
canonical Gaussian initialization assigns that set positive probability.

The result does **not** establish high-probability fitting under canonical
Gaussian initialization. Its construction deliberately makes second-layer
features highly saturated, and the sufficient margin depends on the label
radius. It is a stable-feature benchmark, not a theorem about strongly moving
features or a label-independent saturation margin valid for arbitrarily large
labels.

Status: complete proposed proof, checked algebraically by its author; not yet
independently checked or promoted. No experiments were run. Scientific inputs
were the supervisor's self-contained model assignment only. Required process,
proof, conjecture, and canonical-notation instructions were also read. No other
study artifacts, book passages, or external scientific sources were used.

## Exact model and derivative identities

Let the fixed input matrix be
\(X=[x_1,\ldots,x_m]\in\mathbb R^{d\times m}\), with unit columns. Let
\(A\in\mathbb R^{n\times d}\), \(W\in\mathbb R^{n\times n}\), and
\(w\in\mathbb R^n\), where \(n\ge m\). All occurrences of \(\tanh\)
and its derivative on matrices are entrywise. Define

\[
U=\tanh(AX),\qquad H=\tanh(WU),\qquad
f=\frac1nH^\top w,\qquad r=f-y,\qquad
L=\frac1m\|r\|_2^2.
\]

The initial readout is \(w(0)=0\). The actual gradient flow, in physical time,
is

\[
\dot A=-n\nabla_A L,\qquad
\dot W=-\nabla_W L,\qquad
\dot w=-n\nabla_w L.
\]

For the matrix
\(E=(1-H^2)\odot(wr^\top)\in\mathbb R^{n\times m}\), direct
differentiation gives

\[
\begin{aligned}
\dot w&=-\frac2mHr,\\
\dot W&=-\frac{2}{mn}EU^\top,\\
\dot A&=-\frac2m\bigl[(1-U^2)\odot(W^\top E)\bigr]X^\top.
\end{aligned}
\tag{1}
\]

To make the residual estimate explicit, write \(u_a,h_a\) for the columns
of \(U,H\), and define the diagonal matrices

\[
D_{U,a}=\operatorname{diag}(1-u_a^2),\qquad
D_{H,a}=\operatorname{diag}(1-h_a^2),\qquad
v_a=D_{U,a}W^\top D_{H,a}w.
\]

The residual satisfies

\[
\dot r=-\frac2m\mathcal K r,
\]

where the symmetric matrix \(\mathcal K\in\mathbb R^{m\times m}\) has
entries

\[
\mathcal K_{ab}
=\frac{h_a^\top h_b}{n}
 +\frac{(w^\top D_{H,a}D_{H,b}w)(u_a^\top u_b)}{n^2}
 +\frac{(v_a^\top v_b)(x_a^\top x_b)}n.
\tag{2}
\]

Each term is a Gram matrix: it arises from the parameter derivatives of
\(f_a\) with the stated positive layer mobilities. Consequently

\[
\mathcal K\succeq\frac1nH^\top H,
\qquad
\dot L=-\frac4{m^2}r^\top\mathcal K r\le0.
\tag{3}
\]

In particular, if \(\|y\|_2\le Y\), then \(\|r(t)\|_2\le Y\).
The flow exists for every finite positive time. Indeed, (1),
\(\|U\|_{\rm op},\|H\|_{\rm op}\le\sqrt{nm}\), and
\(\|\tanh'\|_\infty\le1\) give

\[
\begin{aligned}
\|\dot w\|_2&\le2\sqrt{n/m}\,Y,\\
\|\dot W\|_F&\le\frac2{\sqrt{nm}}\|w\|_2Y,\\
\|\dot A\|_F&\le\frac2m\|W\|_{\rm op}\|w\|_2Y\|X\|_{\rm op}.
\end{aligned}
\]

These successively bound \(w,W,A\) on every bounded time interval. The
smooth vector field therefore has no finite-time escape.

## An explicit initialization theorem

Put \(U_0=\tanh(A_0X)\), \(Z_0=W_0U_0\), and suppose every entry of
\(Z_0\) has magnitude at least \(R>0\). Let

\[
S=\operatorname{sign}(Z_0)\in\{-1,1\}^{n\times m},\qquad
\lambda=\lambda_{\min}\!\left(\frac1nS^\top S\right)>0,
\qquad B=\|W_0\|_{\rm op},\qquad K=\|X\|_{\rm op}.
\]

Define \(\beta=\operatorname{sech}^2(R/2)\). Assume the following explicit
inequalities hold for a fixed \(Y\ge0\):

\[
\begin{aligned}
2\sqrt m\,e^{-R}&\le\frac{\sqrt\lambda}{2},\\
\frac{16m\beta Y^2}{\lambda^2}&<1,\\
\frac{16\sqrt{nm}\,\beta Y^2}{\lambda^2}
\left[m+(B+1)^2K^2\right]&<\frac R2.
\end{aligned}
\tag{4}
\]

**Theorem.** For every \(y\in\mathbb R^m\) with \(\|y\|_2\le Y\),
the exact flow (1), initialized at \((A_0,W_0,0)\), satisfies

\[
L(t)\le L(0)e^{-\lambda t/m}\qquad(t\ge0).
\tag{5}
\]

In addition, all parameters converge to finite limits, and their total
movements obey

\[
\begin{aligned}
\sup_{t\ge0}\|w(t)\|_2
&\le\frac{4\sqrt{nm}\,Y}{\lambda},\\
\sup_{t\ge0}\|W(t)-W_0\|_F
&\le\frac{16m\beta Y^2}{\lambda^2},\\
\sup_{t\ge0}\|A(t)-A_0\|_F
&\le\frac{16\sqrt{nm}(B+1)\beta Y^2K}{\lambda^2}.
\end{aligned}
\tag{6}
\]

The last two right-hand sides also bound the corresponding integrals of
velocity norms. The first bounds the integral of \(\|\dot w\|_2\).

**Proof.** Begin on the maximal time interval on which

\[
\|W(t)-W_0\|_F<1,
\qquad
\|W(t)U(t)-Z_0\|_F<R/2.
\tag{7}
\]

The interval contains time zero. On it, every second-layer preactivation
retains its initial sign and has magnitude greater than \(R/2\). Hence

\[
\|1-H^2\|_{\max}\le\beta,
\qquad
\|H-S\|_F\le2\sqrt{nm}\,e^{-R}.
\]

For a unit vector \(q\in\mathbb R^m\), the triangle inequality gives

\[
\frac{\|Hq\|_2}{\sqrt n}
\ge\frac{\|Sq\|_2}{\sqrt n}
  -\frac{\|H-S\|_{\rm op}}{\sqrt n}
\ge\sqrt\lambda-2\sqrt m\,e^{-R}
\ge\frac{\sqrt\lambda}{2}.
\]

Thus \(H^\top H/n\succeq(\lambda/4)I_m\). Combining with (2)-(3)
shows, throughout this interval,

\[
\|r(t)\|_2\le Y e^{-\lambda t/(2m)},\qquad
\int_0^t\|r(s)\|_2\,ds\le\frac{2mY}{\lambda}.
\tag{8}
\]

The readout equation and \(\|H\|_{\rm op}\le\sqrt{nm}\) give

\[
\int_0^t\|\dot w(s)\|_2\,ds
\le2\sqrt{n/m}\int_0^t\|r(s)\|_2\,ds
\le\frac{4\sqrt{nm}Y}{\lambda}.
\tag{9}
\]

Since \(\|E\|_F\le\beta\|w\|_2\|r\|_2\), equations (1),
(8), and (9) yield

\[
\begin{aligned}
\int_0^t\|\dot W(s)\|_F\,ds
&\le\frac{2\beta}{\sqrt{nm}}
 \sup_{0\le s\le t}\|w(s)\|_2
 \int_0^t\|r(s)\|_2\,ds
\le\frac{16m\beta Y^2}{\lambda^2},\\
\int_0^t\|\dot A(s)\|_F\,ds
&\le\frac{2\beta(B+1)K}{m}
 \sup_{0\le s\le t}\|w(s)\|_2
 \int_0^t\|r(s)\|_2\,ds
\le\frac{16\sqrt{nm}(B+1)\beta Y^2K}{\lambda^2}.
\end{aligned}
\tag{10}
\]

Here \(\|W\|_{\rm op}\le B+1\) follows from (7), while the first-layer
activation derivative requires only its global bound by one.

The first-layer activation is Lipschitz, so

\[
\|U(t)-U_0\|_F
\le\|(A(t)-A_0)X\|_F
\le K\|A(t)-A_0\|_F.
\]

Using the exact identity
\(WU-W_0U_0=(W-W_0)U_0+W(U-U_0)\), we obtain

\[
\begin{aligned}
\|WU-Z_0\|_F
&\le\sqrt{nm}\|W-W_0\|_F
 +(B+1)K\|A-A_0\|_F\\
&\le\frac{16\sqrt{nm}\,\beta Y^2}{\lambda^2}
\left[m+(B+1)^2K^2\right]
<R/2.
\end{aligned}
\]

The second condition in (4) likewise makes the first inequality in (7)
strict by a fixed margin. Continuity prevents a finite exit from (7).
Therefore (8)-(10) hold globally, proving (5)-(6). The finite integrals of
the velocity norms make all parameter trajectories Cauchy as
\(t\to\infty\), proving convergence. The limiting network interpolates
because (5) forces the residual to zero. This also covers \(Y=0\), for
which the trajectory is constant. ∎

## Why the sufficient event is nonempty for the stated data class

Assume the unit inputs are pairwise distinct and no pair is antipodal.
First construct \(A_*\) for which \(U_*:=\tanh(A_*X)\) has column
rank \(m\).

Choose \(a\in\mathbb R^d\) outside the finitely many hyperplanes

\[
a^\top x_j=0,\qquad
a^\top(x_j-x_k)=0,\qquad
a^\top(x_j+x_k)=0\quad(j\ne k).
\]

Each displayed normal vector is nonzero under the input assumptions, so
such an \(a\) exists. The numbers \(b_j=a^\top x_j\) are nonzero and
have pairwise distinct absolute values.

The functions \(t\mapsto\tanh(tb_j)\) are linearly independent. To see
this, absorb the signs of \(b_j\) into the coefficients and order their
positive magnitudes as \(0<c_1<\cdots<c_m\). If
\(\sum_j\alpha_j\tanh(tc_j)=0\) for all real \(t\), taking
\(t\to\infty\) gives \(\sum_j\alpha_j=0\). The identity becomes

\[
0=\sum_j\alpha_j\bigl[\tanh(tc_j)-1\bigr].
\]

Multiplication by \(e^{2c_1t}\) and the identity
\(\tanh(s)-1=-2/(e^{2s}+1)\) give \(\alpha_1=0\). Repeating this
argument after removing the first term gives every coefficient zero.

It follows that the vectors
\((\tanh(tb_1),\ldots,\tanh(tb_m))\), as \(t\) ranges over the
reals, span \(\mathbb R^m\): otherwise a nonzero vector orthogonal to
their span would contradict the established functional independence.
Choose \(m\) values of \(t\) giving independent vectors, and use the
corresponding rows \(ta^\top\) in \(A_*\). If \(n>m\), fill the
remaining rows arbitrarily. Then \(U_*\) has column rank \(m\).

Next choose any \(S\in\{-1,1\}^{n\times m}\) of column rank \(m\).
Such a matrix exists: its first row can be all ones; for each
\(k=2,\ldots,m\), row \(k\) is all ones except for a minus one in
column \(k\). Subtracting row one from these rows proves that the first
\(m\) rows are independent. Extra rows can be arbitrary sign rows.

With the left inverse
\(U_*^+=(U_*^\top U_*)^{-1}U_*^\top\), set

\[
W_*(R)=2R S U_*^+.
\]

Then \(W_*(R)U_*=2RS\) and
\(\|W_*(R)\|_{\rm op}=2R\|SU_*^+\|_{\rm op}\). The quantities
\(n,m,K,\lambda,Y,U_*\) are fixed as \(R\) increases. Since
\(\operatorname{sech}^2(R/2)\le4e^{-R}\), all three inequalities
in (4) hold strictly for sufficiently large finite \(R\). In particular,
the final left-hand side is bounded by a fixed constant times
\(e^{-R}(1+R^2)\), whereas its right-hand side is \(R/2\).

At this center the initial margins are \(2R\), exceeding the theorem's
required margin \(R\). Continuity therefore supplies a nonempty open
neighborhood of \((A_*,W_*(R))\) where the sign matrix remains \(S\),
the initial margins exceed \(R\), and all inequalities (4) remain true.
The same neighborhood works simultaneously for every
\(\|y\|_2\le Y\).

## Canonical Gaussian interpretation and the remaining gap

The canonical law has independent entries

\[
(A_0)_{ij}\sim N(0,1),\qquad
(W_0)_{ij}\sim N(0,1/n),\qquad w_0=0.
\]

Its joint density for \((A_0,W_0)\) is strictly positive everywhere in
the finite-dimensional parameter space. It therefore assigns the open
initialization neighborhood just constructed a strictly positive
probability. This is a statement under the original Gaussian law, without
freezing layers or changing the optimizer. The theorem is conditional on
a specially favorable event in that law.

Nothing in this proof makes that probability close to one, uniformly
positive in width, or independent of the label radius. The Gaussian
density contains the factor
\(\exp[-n\|W_*(R)\|_F^2/2]\) at the constructed center, while its
norm grows linearly in \(R\). A support argument cannot furnish the
requested high-probability guarantee by itself.

The mechanism here is explicit saturation trapping: a full-rank sign code
gives a readout spectral gap, and exponentially small hidden-layer
derivatives keep that code fixed while the readout learns the labels.
The gap is proved from initial-state inequalities, rather than assumed
along the trajectory. For typical canonical Gaussian states with modest
logits, the small derivative factor used in (10) is absent. Increasing
width does not replace it in these estimates; their factors
\(\sqrt{nm}\) and the dependence on \(Y^2\) remain. This is the precise
limitation of this proof route, not evidence that typical Gaussian flows
fail to fit.
