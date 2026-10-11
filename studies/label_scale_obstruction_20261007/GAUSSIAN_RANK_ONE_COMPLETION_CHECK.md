# Check of rank-one completion and the full-rank convergence-or-escape consequence

Status: internally checked, 2026-10-11. The corrected frozen rank-one source passes this complete reused-context check. Its zero Hessian block and surjective mixed block are valid. Combined with the previously checked other-rank index bound, center-stable argument, and analytic-gradient alternative, they establish the finite-width almost-sure conclusion below. This is not an independent promotion review.

For full-column-rank inputs and

\[
n\ge\max\{1,2m-4\},
\]

positive limiting loss almost surely forces the parameter norm to tend to infinity. No finite bad critical limit remains as an alternative. This does not establish fitting or the occurrence of positive-loss escape.

No experiment, Git operation, or source modification was performed. Only this assigned check file was written.

## 1. Exact versions and theorem scope

The complete rank-one source was read after its matrix-typing correction and checked at the following frozen SHA256:

- GAUSSIAN_RANK_ONE_COMPLETION.md: 859bea4dfa94fbd6bc2937f5660a9eccef21ee1832aaa81d2d384e2834440379.

The earlier announced hash 0c54f5552f45168b6e7a28984643f9997a2da64ab20f88ba15a4ccc640ecfa45 is not the audited final version. In corrected equation (7), the coefficient is the matrix $-2\operatorname{diag}(t\odot Hr)$; a diagonal matrix multiplying a vector would have been ill-typed. The corrected formula has the required type and vanishes.

The other authorized inputs and their SHA256 values are:

- GAUSSIAN_SADDLE_INDEX.md: 0a47f283136137fad30edcd2c7a75812f6791a61d71d58fef5845e9d3c9bcc66.
- GAUSSIAN_SADDLE_INDEX_CHECK.md: 2e881bc514919bafa49a22da78410ab0baba84450d8188940ebd37c90a9aa193.
- TWO_SAMPLE_AVOIDANCE_CHECK.md: 9828515c484d7b35a6199168ab9b75de46c683945ef99bbb6d22c31f9c9e5a3c.
- UNCONDITIONAL_NEGATIVE_ROUTE.md: b4b0cc177657f7bb985d7f6e3507d3aa6011b5840e030db962f1b5c114d5329a.

Primary sources already read and checked for the needed theorems:

- [Eldering, invariant-manifold lecture notes, Section 3.1](https://www.jaapeldering.nl/files/lect-ICMC-invarmflds.pdf), PDF SHA256 e7c4e868a96880a8f24149528c842b61282f33e897a14e4bcdecc18f078d4c1b. The complete center-case regularity construction used here is supplied in Section 5 of TWO_SAMPLE_AVOIDANCE_CHECK.md; it completes the sketch in the lecture notes for the diagonalizable linearizations at issue.
- [Absil–Mahony–Andrews, Theorem 2.2 and proof](https://sites.uclouvain.be/absil/Publi/Convergence_SIOPT/13-60526.pdf), PDF SHA256 1705e38f0861337c25419735582c4b387f222a02d7e87702c9af8c07f3016795.
- [Authors' errata page](https://sites.uclouvain.be/absil/2005.901), retrieved HTML SHA256 d1932b7e03c719a2d0ea2cfa57f5db842cbf04f57db8d3b70b30803d99367c32. Its discrete-time Proposition 3.3 correction does not concern the continuous-time theorem used here.

Fix $m\ge1$, $X=[x_1,\ldots,x_m]\in\mathbb R^{d\times m}$ of column rank $m$, with unit columns, and a fixed nonzero label vector $y\in\mathbb R^m$. For finite width $n$, the parameters, forward pass, and loss are

\[
A\in\mathbb R^{n\times d},\quad W\in\mathbb R^{n\times n},
\quad w\in\mathbb R^n,\qquad
U=\tanh(AX),\quad z_a=Wu_a,\quad h_a=\tanh z_a,
\]
\[
H=[h_1,\ldots,h_m],\quad f=H^\top w/n,\quad r=f-y,\quad
\mathcal L=\|r\|^2/m.
\]

Here $u_a=U_{:,a}$, and tanh and its derivatives act entrywise.

The gradient-flow mobilities of $(A,W,w)$ are $(n,1,n)$. Initialization has independent $A_{ij}\sim N(0,1)$ and $W_{ij}\sim N(0,1/n)$, independent of each other, and exactly $w=0$. Set $\theta=(A,W,w)$, $N=nd+n^2+n$, and $\mathcal L_0=\|y\|^2/m$.

The assembled claim is, for each fixed width satisfying the displayed threshold,

\[
\mathbb P\{\theta(t)\to\theta_* \text{ finite critical},\
                         \mathcal L(\theta_*)>0\}=0,
\tag{1}
\]
\[
\mathbb P\{\mathcal L_\infty>0,\
                         \|\theta(t)\|\not\to\infty\}=0.
\tag{2}
\]

No large-width approximation or interchange of width and time limits is involved. Full column rank requires $d\ge m$ and is an essential restriction.

## 2. Coordinates, stationarity, and positive factorization

Full column rank makes $A\mapsto AX$ surjective onto $\mathbb R^{n\times m}$. Completing with unused input coordinates and applying the entrywise tanh diffeomorphism makes $U$ a free local coordinate. At a critical point the Hessian transforms by an invertible congruence: the additional chain-rule term is multiplied by the zero gradient. Thus its negative index can be computed in $(U,W,w)$ coordinates.

Let

\[
E_{ia}=\operatorname{sech}^2z_{ia}>0,\qquad
b_a=w\odot E_{:,a},\qquad T=[r_1b_1,\ldots,r_mb_m].
\]

Stationarity gives, with no missing normalizing factor affecting these zero identities,

\[
Hr=0,\qquad TU^\top=0,\qquad W^\top T=0.
\tag{3}
\]

The rank-one algebra needs only a finite critical point with $r\ne0$, $w\ne0$, and $\operatorname{rank}T=1$. In particular these conditions hold for the rank-one case in $0<\mathcal L<\mathcal L_0$.

Write $\mathcal S=\{a:r_a\ne0\}$, choose $a_0\in\mathcal S$, and put $t=b_{a_0}\ne0$. Rank one implies $b_a=\beta_at$ on $\mathcal S$. Choosing a row $i$ with $w_i\ne0$ proves

\[
\beta_a=\frac{E_{ia}}{E_{ia_0}}>0,\qquad
W^\top t=0.
\tag{4}
\]

No proportionality is asserted for columns outside $\mathcal S$. Zero coordinates of $w$ cause no difficulty: all corresponding coordinates of the $b_a$ vanish, while positivity of $\beta_a$ is witnessed by a nonzero readout coordinate.

Define fixed quantities at this critical point:

\[
s_a=\begin{cases}
\operatorname{sgn}(r_a)/\sqrt{\beta_a},&a\in\mathcal S,\\
0,&a\notin\mathcal S,
\end{cases}
\qquad C=\sum_{a\in\mathcal S}|r_a|\sqrt{\beta_a}>0.
\tag{5}
\]

In every Hessian calculation below, $s,\beta_a,t$ denote these fixed values; they are not differentiated along the perturbation.

## 3. The whole $n$-dimensional pure block vanishes

For $v\in\mathbb R^n$ set $\Delta U(v)=vs^\top$. Since $s\ne0$, this is an injective linear map and its image is an $n$-dimensional allowed tangent subspace. On $\mathcal S$,

\[
Df_a[\Delta U(v)]
=\frac{s_a}{n}b_a^\top Wv
=\frac{s_a\beta_a}{n}t^\top Wv=0.
\tag{6}
\]

Outside $\mathcal S$ the column perturbation is zero. Thus the entire prediction differential vanishes, including the coordinates where the residual is zero.

The squared-loss Hessian is

\[
D^2\mathcal L[\Delta\theta,\Delta\theta']
=\frac2m\sum_a
\left(Df_a[\Delta\theta]Df_a[\Delta\theta']
+r_aD^2f_a[\Delta\theta,\Delta\theta']\right).
\]

For two directions $\Delta U(v),\Delta U(v')$, the first term vanishes by (6). The second equals

\[
\frac2{mn}(Wv)^\top
\left[\sum_{a\in\mathcal S}r_as_a^2
\operatorname{diag}(w\odot\tanh''z_a)\right]Wv'.
\tag{7}
\]

Using $\tanh''z=-2\tanh z\,\operatorname{sech}^2z$ and
$w\odot E_{:,a}=\beta_at$, the matrix in brackets is

\[
\begin{aligned}
-2\operatorname{diag}
\left(t\odot\sum_{a\in\mathcal S}r_a\beta_as_a^2h_a\right)
&=-2\operatorname{diag}\left(t\odot\sum_a r_ah_a\right)\\
&=-2\operatorname{diag}(t\odot Hr)=0.
\end{aligned}
\tag{8}
\]

Here $\beta_as_a^2=1$ on $\mathcal S$ and $r_a=0$ outside it. This proves vanishing of the full bilinear pure Hessian block, not merely its diagonal entries. It does not claim constancy of predictions or loss along finite displacements.

## 4. Exact mixed derivative and its surjectivity

For a perturbation $(\Delta W,\delta w)$, define

\[
q(\Delta W)=
\sum_{a\in\mathcal S}r_as_a
\operatorname{diag}(w\odot\tanh''z_a)\Delta Wu_a,
\]
\[
G_i=\sum_{a\in\mathcal S}r_as_a E_{ia}
=\sum_{a\in\mathcal S}\frac{|r_a|E_{ia}}{\sqrt{\beta_a}}>0.
\tag{9}
\]

The prediction differential in the first argument $\Delta U(v)$ vanishes, so there is no Gauss–Newton mixed contribution, irrespective of the prediction differential in $(\Delta W,\delta w)$. Differentiating the prediction twice gives the three residual terms

\[
\frac{s_a}{n}\left[
b_a^\top\Delta Wv+
(Wv)^\top\operatorname{diag}(w\odot\tanh''z_a)\Delta Wu_a+
(Wv)^\top\operatorname{diag}(E_{:,a})\delta w
\right].
\]

After multiplying by $2r_a/m$ and summing,

\[
D^2\mathcal L[\Delta U(v),(\Delta W,\delta w)]
=\frac2{mn}v^\top
\left[C\Delta W^\top t+
W^\top\bigl(q(\Delta W)+G\odot\delta w\bigr)\right],
\tag{10}
\]

because $\sum_a r_as_ab_a=Ct$. All terms and factors match the corrected source.

Since each $G_i>0$, the choice $\delta w_i=-q_i(\Delta W)/G_i$ is legitimate, including when $w_i=0$. It cancels the entire correction inside $W^\top$. For any prescribed $d_0\in\mathbb R^n$, choose

\[
\Delta W=\frac{t d_0^\top}{C\|t\|^2}
\]

and then the preceding $\delta w$. The bracket in (10) becomes exactly $d_0$. The construction is linear in $d_0$, and $C,\|t\|^2,G_i$ are strictly positive finite numbers at the point. No inverse of $W$ or $\operatorname{diag}(w)$ appears.

Thus the mixed block against the $n$-dimensional subspace from Section 3 has row rank $n$. The parameter spaces used for the two blocks are independent: first-feature directions versus middle-weight/readout directions. Restricting the Hessian to their direct sum gives

\[
\begin{pmatrix}0&B\\ B^\top&J_0\end{pmatrix},
\qquad \operatorname{rank}B=n.
\]

If $BR=I_n$, then on the $n$-dimensional graph $(v,-\epsilon Rv)$ its quadratic form is

\[
-2\epsilon\|v\|^2+
\epsilon^2v^\top R^\top J_0Rv<0
\]

for all nonzero $v$ and sufficiently small $\epsilon>0$. Therefore the full loss Hessian has at least $n$ negative eigenvalues. This completes the rank-one lemma at every fixed width.

## 5. Other ranks and all-rank width threshold

For $g=\operatorname{rank}T\ge2$, the independently reconstructed bound in GAUSSIAN_SADDLE_INDEX_CHECK.md is

\[
\operatorname{index}_-(\nabla^2\mathcal L)
\ge g\bigl(n-\operatorname{rank}U\bigr)
\ge g(n-m+g).
\tag{11}
\]

Its hypotheses are exactly available: $U$ is free locally, $TU^\top=0$, and finite gates are strictly positive. In brief, directions $\Delta W=VQ^\top$ with columns of $Q$ spanning $\ker U^\top$ give a zero pure block. Its mixed block with arbitrary $\Delta U$ has coefficient $QV^\top T$, of rank $g(n-\operatorname{rank}U)$. Also $TU^\top=0$ makes the row spaces of $T,U$ orthogonal, hence $\operatorname{rank}U+g\le m$.

Let $n\ge\max\{1,2m-4\}$. If $m\ge3$, then $n-m+2\ge m-2>0$; if $m=2$, then $n-m+2=n>0$. For integers $g\ge2$, the expression in (11) increases with $g$, so

\[
g(n-m+g)\ge2(n-m+2)\ge n.
\tag{12}
\]

The final inequality is exactly $n\ge2m-4$. When $m=1$, $g\ge2$ is impossible. The rank-one proof covers $g=1$ without a width condition. Since $T\ne0$ whenever $0<\mathcal L<\mathcal L_0$, every relevant critical point consequently has at least $n$ negative Hessian directions under the stated threshold.

There is no missed small-$m$ case. In fact $f\ne0$ in this loss interval forces $\operatorname{rank}U\ge1$, so no such point exists at $m=1$, and at $m=2$ its rank $g$ cannot exceed one. The source's slightly weaker case split is nevertheless correct.

## 6. Zero-readout avoidance: every hypothesis remains valid

Let $D$ be the constant positive diagonal mobility matrix. The training linearization at a critical point is $-D\nabla^2\mathcal L$, similar to the symmetric matrix $-D^{1/2}\nabla^2\mathcal L D^{1/2}$. It is real diagonalizable, with at least $n$ positive eigenvalues by Section 5.

Section 5 of TWO_SAMPLE_AVOIDANCE_CHECK.md constructs, for exactly such a $C^2$ field and spectral split, an embedded local $C^1$ center-stable manifold of dimension at most $N-n$. It contains every forward orbit remaining in the small neighborhood and is tangent to the actual field there. Its two-weight differentiability proof explicitly covers zero eigenvalues. The present network field is real analytic, so its smoothness hypotheses hold.

Global forward existence can be proved directly from energy. Along the maximal forward solution,

\[
-\dot{\mathcal L}
=\frac{\|\dot A\|_F^2}{n}
+\|\dot W\|_F^2+\frac{\|\dot w\|^2}{n}.
\tag{13}
\]

The parameter length on $[0,T]$ in this constant mobility metric is at most $\sqrt{T\mathcal L(0)}$. If the maximal time were finite, the same Cauchy–Schwarz bound on a tail interval would make the parameter path Cauchy at that time. At fixed width the metric is equivalent to Euclidean norm, so the limit is finite; smooth local existence would extend the solution, a contradiction. Finite-time flow maps are therefore diffeomorphisms onto their open images. Global backward completeness is unnecessary.

On the initialization slice $M_0=\{w=0\}$, of dimension $N-n$, the field is

\[
V=(0,0,2Hy/m).
\]

Where $Hy\ne0$, this field is not tangent to $M_0$. Let $\Phi_t$ denote the actual time-$t$ flow. For any finite-time pullback $S$ of a local center-stable manifold, the identity
$D\Phi_t(p)V(p)=V(\Phi_t(p))$ gives $V(p)\in T_pS$. The dimension bound $\dim S\le\dim M_0$ therefore implies
$T_pM_0\not\subset T_pS$ at such an intersection. A scalar component of a local submersion defining $S$ has nonzero derivative on $M_0$. Its zero set is a hypersurface of $M_0$ containing the intersection, hence the intersection is slice-null.

The relevant critical set has a countable cover by its open trapping neighborhoods. An orbit converging to a critical point eventually stays in one of them, starting at some integer time. Countably many neighborhoods, times, and intersection charts consequently cover all such initial conditions by slice-null sets. This neither assumes isolated critical points nor takes an uncountable union of null basins.

Under the specified Gaussian law, $Hy\ne0$ almost surely. Conditional on invertible $W_0$, the full-column-rank assumption gives a density for $A_0X\in\mathbb R^{n\times m}$, and the map $Z\mapsto\tanh(W_0\tanh Z)$ is a diffeomorphism onto an open image. Thus $H_0$ has a density, while $\{H:Hy=0\}$ is a proper linear subspace. The law of $(A_0,W_0)$ also has a density on $M_0$.

It follows that

\[
\dot{\mathcal L}(0)=-\frac4{m^2n}\|H_0y\|^2<0
\]

almost surely. Any finite positive-loss critical limit is therefore in the interval $(0,\mathcal L_0)$ already handled. The slice-null argument proves (1) with no additional premise on the future trajectory.

## 7. General-$m$ analytic convergence-or-escape assembly

The already checked continuous-time theorem states that a global $C^1$ curve for a real-analytic objective, satisfying an eventual positive angle condition and “zero objective derivative implies zero velocity,” either has norm tending to infinity or converges to one finite point. It starts from any finite accumulation point; boundedness of the entire orbit is not required. [Absil–Mahony–Andrews, Theorem 2.2](https://sites.uclouvain.be/absil/Publi/Convergence_SIOPT/13-60526.pdf)

For every fixed $m,n$, transform

\[
\eta=D^{-1/2}\theta,\qquad
\widetilde{\mathcal L}(\eta)=\mathcal L(D^{1/2}\eta).
\]

The objective is real analytic on all of $\mathbb R^N$ because tanh is real analytic on the real line. Equation (13) provides global existence, and

\[
\dot\eta=-\nabla\widetilde{\mathcal L},\qquad
\dot{\widetilde{\mathcal L}}
=-\|\nabla\widetilde{\mathcal L}\|^2
=-\|\nabla\widetilde{\mathcal L}\|\|\dot\eta\|.
\]

Thus the angle condition holds with constant one, and zero loss derivative implies zero velocity. The theorem applies at arbitrary sample count without a new assumption.

A finite limit is critical: otherwise continuity keeps the gradient norm bounded below at late times, forcing the nonnegative loss to decrease at a strictly negative uniform rate indefinitely. The fixed positive matrix $D$ makes the $\theta$ and $\eta$ norms equivalent. Therefore every trajectory either has $\|\theta(t)\|\to\infty$ or converges to a finite critical point.

Combining this deterministic alternative with (1) gives (2). In particular, unbounded recurrence with a finite accumulation point is excluded; the remaining escape means the whole norm tends to infinity, not merely that its limsup is infinite.

## 8. Verdict and supersession boundary

The corrected source passes. The following potentially decisive issues were explicitly checked:

- Residual support is used consistently, with zero perturbation columns outside it.
- The positive proportionality factors and cancellation denominators do not require nonzero readout coordinates everywhere.
- The pure Hessian block vanishes bilinearly through $Hr=0$ and the tanh differential identity.
- The mixed Gauss–Newton term is zero against every second direction because the first prediction differential vanishes.
- The combined middle-weight/readout variation is surjective without inverting $W$.
- The width threshold covers $m=1,2$ as well as $m\ge3$.
- The center-stable, singular-slice, countable-cover, and analytic-flow hypotheses all match the actual finite-width flow.

The rank-one exception in GAUSSIAN_SADDLE_INDEX.md and its earlier check is now resolved under the combined theorem's assumptions. That earlier check remains a valid audit of its narrower source, but its list of unresolved finite critical ranks is superseded by this completion.

The established conclusion is: for full-column-rank $X$, arbitrary fixed nonzero labels, and $n\ge\max\{1,2m-4\}$, canonical Gaussian initialization with exact zero readout almost surely cannot converge to a finite bad critical point; positive limiting loss therefore forces $\|\theta(t)\|\to\infty$.

For $y=0$, zero readout already gives zero residual and the flow is stationary, so the same failure-mechanism implication holds vacuously. Thus its label scope can also be stated as arbitrary fixed labels.

It is still open here whether that escape can retain positive limiting loss, or whether fitting holds almost surely. The result does not cover dependent inputs, give a rate, produce a nonfitting Gaussian event, or imply parameter boundedness. No claim from finite critical-point algebra is being applied to a limit at infinity.

## 9. Final header-only version verification

On 2026-10-11, the final GAUSSIAN_RANK_ONE_COMPLETION.md was verified at SHA256 fb58eca18b958e720ca7cf6ab58e6eef849daa247f1e7b287a3896b7204ce60c. Replacing only its four-line internal-check status, report link, and non-promotion qualification by the original one-line candidate status reproduces SHA256 859bea4dfa94fbd6bc2937f5660a9eccef21ee1832aaa81d2d384e2834440379 exactly. Thus every byte outside that header, including all mathematics and scope restrictions, is unchanged from the audited version.

The relative link resolves to this report. Its referenced convergence-or-escape assembly is Section 7 above, and the internal-not-promotion qualification agrees with this check's declared scope. The PASS verdict and equations (1)–(2) apply to the final source version. No source modification was made during this verification.
