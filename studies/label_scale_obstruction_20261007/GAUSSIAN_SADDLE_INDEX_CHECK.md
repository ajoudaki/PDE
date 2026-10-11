# Check of the general-sample Gaussian saddle-index restriction

Status: internally checked, 2026-10-11. The Hessian index bound and the restricted zero-readout avoidance conclusion in the frozen source are correct. The center-stable obligation is discharged by the complete construction in the separately checked two-sample report; its argument is a general finite-dimensional lemma, not a two-sample population assumption. This is a reused-context scoped check, not an isolated review or promotion decision.

The conclusion remains narrower than the two-input theorem. At general sample count, finite bad limits with rank-one residual-weighted backward matrix are not excluded. Positive-loss escape to infinity is not excluded in either theorem.

## 1. Frozen inputs and scope

The complete new source was read. This check used only that source, the prior negative-route candidate, the completed center-stable/analytic-flow check, and its cited primary sources. No experiment or Git operation was used. No source artifact was edited.

SHA256:

- GAUSSIAN_SADDLE_INDEX.md: 1698097578a8ad9b179ef8e1051616e570ac03e66d53c5b24d03c20d8482e2bc.
- UNCONDITIONAL_NEGATIVE_ROUTE.md: b4b0cc177657f7bb985d7f6e3507d3aa6011b5840e030db962f1b5c114d5329a.
- TWO_SAMPLE_AVOIDANCE_CHECK.md: 9828515c484d7b35a6199168ab9b75de46c683945ef99bbb6d22c31f9c9e5a3c.

The primary source versions already checked in full for the needed results are [Eldering, Section 3.1](https://www.jaapeldering.nl/files/lect-ICMC-invarmflds.pdf), PDF SHA256 e7c4e868a96880a8f24149528c842b61282f33e897a14e4bcdecc18f078d4c1b, and [Absil–Mahony–Andrews, Theorem 2.2 and proof](https://sites.uclouvain.be/absil/Publi/Convergence_SIOPT/13-60526.pdf), PDF SHA256 1705e38f0861337c25419735582c4b387f222a02d7e87702c9af8c07f3016795. The prior check records the separately inspected erratum and fills the center-stable regularity sketch.

Fix $X\in\mathbb R^{d\times m}$ of column rank $m$, with unit columns, and fixed $y\in\mathbb R^m\setminus\{0\}$. Thus this statement requires $d\ge m$; it is not a low-intrinsic-dimension theorem. At fixed width $n$,

\[
U=\tanh(AX),\quad H=\tanh(WU),\quad
f=H^\top w/n,\quad r=f-y,\quad
\mathcal L=\|r\|^2/m.
\]

The dimensions are $A\in\mathbb R^{n\times d}$, $W\in\mathbb R^{n\times n}$, $w\in\mathbb R^n$. The flow mobilities are $(n,1,n)$. Initialization is independent $A_{ij}\sim N(0,1)$, $W_{ij}\sim N(0,1/n)$, and exactly $w=0$. Write $\mathcal L_0=\|y\|^2/m$.

At a finite critical point define

\[
T=\operatorname{diag}(w)
\bigl[1-\tanh^2(WU)\bigr]\operatorname{diag}(r)
\in\mathbb R^{n\times m},\qquad g=\operatorname{rank}T,
\tag{1}
\]

where the bracket is entrywise. The assertions under check are:

\[
\operatorname{index}_-(\nabla^2\mathcal L)
\ge g\bigl(n-\operatorname{rank}U\bigr)
\ge g(n-m+g)
\tag{2}
\]

at each critical point with $0<\mathcal L<\mathcal L_0$, and, for $m\ge3$, $n\ge2m-4$,

\[
\mathbb P\{\theta(t)\to\theta_*\text{ finite critical},\
\mathcal L(\theta_*)>0,\ \operatorname{rank}T(\theta_*)\ge2\}=0.
\tag{3}
\]

Here the negative index counts eigenvalues with multiplicity.

## 2. Coordinate and stationarity checks

Since $X$ has rank $m$, each row map $A_{j,:}\mapsto A_{j,:}X$ is surjective. Completing it by coordinates on the orthogonal complement of the input span produces invertible linear coordinates on $A$. Entrywise tanh then gives a smooth local coordinate change from $AX$ to $U\in(-1,1)^{n\times m}$. Every $\Delta U\in\mathbb R^{n\times m}$ is therefore an allowed tangent variation. No lower bound on its coordinate Jacobian is needed at a fixed finite state.

At a critical point a smooth invertible coordinate change transforms the Hessian by congruence. The additional second-derivative term is multiplied by the gradient, which vanishes. Thus negative index can be computed in $(U,W,w)$ coordinates; the unused $A$ coordinates contribute only zeros.

Let $Z=WU$. The loss differential is

\[
D\mathcal L[\Delta Z]
=\frac2{mn}\langle T,\Delta Z\rangle_F.
\]

Consequently stationarity gives exactly

\[
TU^\top=0,\qquad W^\top T=0.
\tag{4}
\]

The loss interval forces $w\ne0$ and $r\ne0$. Since every finite top tanh gate is strictly positive, choosing $i,a$ with $w_i\ne0,r_a\ne0$ gives $T_{ia}\ne0$. Hence $g\ge1$. From $TU^\top=0$, the row spaces of $T$ and $U$ are orthogonal subspaces of $\mathbb R^m$:

\[
\operatorname{rank}U+g\le m.
\tag{5}
\]

No orthogonality of the inputs themselves is assumed.

## 3. Exact mixed-block rank and negative index

Put $h=n-\operatorname{rank}U\ge0$ and choose $Q\in\mathbb R^{n\times h}$ with orthonormal columns spanning $\ker U^\top$. If $h=0$, the first inequality in (2) is the trivial nonnegative lower bound; the argument below is understood on the zero-dimensional flat subspace.

For $V\in\mathbb R^{n\times h}$ set $\Delta W=VQ^\top$. Then $\Delta WU=0$, so changing $W$ anywhere in this whole affine subspace leaves $WU$ and the predictions unchanged when $U,w$ are fixed. The Hessian restricted to two such $W$ directions is zero, not merely zero on each coordinate axis.

For an independent arbitrary $\Delta U$, the two-parameter preactivation is

\[
(W+s\Delta W)(U+t\Delta U)
=WU+tW\Delta U+st\Delta W\Delta U.
\]

The first preactivation derivative in $s$ is zero. The loss Gauss–Newton mixed term and the term involving $\tanh''$ both vanish. The remaining mixed derivative is

\[
\begin{aligned}
D^2\mathcal L[\Delta W,\Delta U]
&=\frac2{mn}\langle T,\Delta W\Delta U\rangle_F\\
&=\frac2{mn}\langle QV^\top T,\Delta U\rangle_F.
\end{aligned}
\tag{6}
\]

The normalizing factor $2/(mn)$ is correct and nonzero. The linear map $V\mapsto V^\top T$ has rank $hg$. To see this without a genericity premise, write the $h$ columns of $V$ as $v_1,\ldots,v_h$. The corresponding rows of $V^\top T$ are $v_j^\top T$, each of which ranges independently over the $g$-dimensional row space of $T$. Multiplication by $Q$ is injective because $Q^\top Q=I_h$. Thus (6) has rank exactly $hg$.

Restrict the full Hessian to the direct sum of this flat $W$ subspace and all $U$ directions. Its matrix is

\[
\begin{pmatrix}0&B\\B^\top&C\end{pmatrix},
\qquad \operatorname{rank}B=hg.
\tag{7}
\]

Choose an $hg$-dimensional subspace of the first block on which $B^\top$ is injective. For vectors $(v,-\epsilon B^\top v)$ the quadratic form is

\[
-2\epsilon\|B^\top v\|^2
+\epsilon^2(B^\top v)^\top C(B^\top v)
\le(-2\epsilon+\epsilon^2\|C\|)\|B^\top v\|^2<0
\]

for small enough $\epsilon>0$ and $v\ne0$. This directly constructs an $hg$-dimensional negative subspace. The full Hessian therefore has at least $hg$ negative eigenvalues, even after reinstating the omitted parameter directions. Combining with (5) gives both inequalities in (2).

This proof holds the readout fixed while constructing the negative subspace. It does not require that the trained $W$ be invertible, that $T$ have generic rank, or that the neuron gates be uniformly bounded below over time.

## 4. Width threshold and the initialization slice

When $m\ge3$ and $n\ge2m-4$, the quantity $n-m+2$ is at least $m-2>0$. For integers $g\ge2$, $g(n-m+g)$ increases with $g$, so

\[
g(n-m+g)\ge2(n-m+2)\ge n.
\tag{8}
\]

Thus every relevant critical point with $g\ge2$ has at least $n$ negative Hessian directions.

Let $N=nd+n^2+n$ and let $D$ again denote the positive diagonal mobility matrix. The linearization $-D\nabla^2\mathcal L$ is similar to
$-D^{1/2}\nabla^2\mathcal L D^{1/2}$, a symmetric matrix. It is real diagonalizable and has at least $n$ strictly positive eigenvalues.

The complete local manifold construction in Section 5 of TWO_SAMPLE_AVOIDANCE_CHECK.md applies verbatim: it uses only a $C^2$ vector field with this diagonalizable spectral split, not the number of samples. It yields a $C^1$ local center-stable manifold of dimension at most $N-n$, tangent to the original flow, containing every forward orbit staying in its bounded neighborhood.

The singular initialization slice is $M_0=\{w=0\}$, with dimension $N-n$. At every point of it,

\[
V=(\dot A,\dot W,\dot w)=(0,0,2Hy/m).
\tag{9}
\]

When $Hy\ne0$, $V$ is not tangent to $M_0$. For any finite-time pullback $S$ of a local center-stable manifold, flow equivariance gives $V(p)\in T_pS$ at $p\in S$. Since $\dim S\le\dim M_0$, at an intersection point with $Hy\ne0$,

\[
T_pM_0\not\subset T_pS.
\]

A local submersion defining $S$ therefore has some scalar component with nonzero derivative on $M_0$. Its zero set is a hypersurface in $M_0$ containing the intersection. This makes the intersection slice-null. Full transversality is not claimed or needed.

The general finite-horizon bounds in Section 2 of the earlier check apply to any fixed $m$ and give a global forward flow, so the finite-time pullbacks are valid local diffeomorphic pullbacks. Countably many critical-point neighborhoods cover the relevant critical set, even though that set need not be closed or countable. Integer entrance times and countably many intersection charts then cover every convergent orbit under consideration by slice-null sets.

Finally, $Hy\ne0$ almost surely under the prescribed initialization. Conditional on invertible $W_0$, $A_0X$ has a density in $\mathbb R^{n\times m}$. The map $Z\mapsto\tanh(W_0\tanh Z)$ is a diffeomorphism onto an open image, so $H_0$ has a density. The set $\{H:Hy=0\}$ is a proper linear subspace. This argument works even when $n<m$; it does not require $H$ to have full column rank.

Thus

\[
\dot{\mathcal L}(0)=-\frac4{m^2n}\|H_0y\|^2<0
\]

almost surely. Every positive finite critical limit has loss strictly below $\mathcal L_0$, and the preceding countable slice-null argument proves (3).

## 5. Exact conclusion and boundaries

The rank-dependent bound (2) is established for every finite critical point in the stated loss interval, with no width threshold. The threshold in (8) is a sufficient condition turning it into the $n$-direction count needed for the singular-slice argument.

For $m\ge3$, $n\ge2m-4$, and full-column-rank $X$, equation (3) is therefore established without an additional neural-dynamics assumption. Combining it with the already checked analytic-flow alternative gives the precise almost-sure restriction:

\[
\mathcal L_\infty>0
\ \Longrightarrow\
\left[
\|\theta(t)\|\to\infty
\quad\text{or}\quad
\theta(t)\to\theta_*,\
\nabla\mathcal L(\theta_*)=0,\
\operatorname{rank}T(\theta_*)=1
\right].
\tag{10}
\]

This does not say either remaining alternative occurs with positive probability. The analytic-flow theorem excludes a third possibility of recurrent finite accumulation without convergence.

There are two essential boundaries:

- At a relevant critical point, $\operatorname{rank}U\ge1$ because $f\ne0$. For $g=1$, the flat-block estimate is at most $n-1$ and therefore does not by itself reach the dimension threshold. This is a limitation of this lower bound, not evidence that rank-one saddles are attracting.
- If $X$ is rank deficient, $\Delta U$ is not an arbitrary tangent variation. The mixed rank computation in Section 3 no longer proves (2). The theorem is not applicable to $m>\operatorname{rank}X$.

The two-input result is stronger in a different direction: its separate classification supplies $n$ negative directions even in the rank-one case and removes every finite bad critical limit at every width. The present general-sample result removes only those finite bad limits with $g\ge2$ under the stated width condition. Neither result proves unconditional fitting, excludes positive-loss parameter escape, supplies a convergence rate, or constructs a canonical-Gaussian nonfitting event.

No blocking objection remains for the claims actually stated in the frozen general-sample source.

## 6. Final-version verification

On 2026-10-11, the complete status-cleaned GAUSSIAN_SADDLE_INDEX.md was reread at SHA256 0a47f283136137fad30edcd2c7a75812f6791a61d71d58fef5845e9d3c9bcc66. The verdict above applies to this final source version.

The only changes from the originally checked source are four status/dependency passages: the opening internal-check status and report link; the link to the completed center-stable construction; removal of the corresponding conditional/pending wording; and the final link to the checked two-input argument. Reversing exactly those four substitutions in memory reproduces the original SHA256 1698097578a8ad9b179ef8e1051616e570ac03e66d53c5b24d03c20d8482e2bc. This verifies byte-for-byte that the mathematical statements, assumptions, formulas, and remaining boundaries are unchanged.

Both relative Markdown links resolve to the named reports in this same study folder. The stated Section 5 of TWO_SAMPLE_AVOIDANCE_CHECK.md is the complete center-stable construction, including its two-weight $C^1$ argument. That report remains at SHA256 9828515c484d7b35a6199168ab9b75de46c683945ef99bbb6d22c31f9c9e5a3c. Its diagonalizable-linearization specialization is exactly sufficient here. The internal-check status is supported and expressly distinguished from independent promotion review. No new scientific objection was introduced by the cleanup.
