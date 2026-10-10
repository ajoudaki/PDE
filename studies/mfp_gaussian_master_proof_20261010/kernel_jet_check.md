# Independent initialization-jet check

This scoped calculation uses the model supplied in the assignment and the required process and notation skills. No compiler artifact, other study, or external scientific source was read. During the calculation, the supervisor clarified that the first expected derivative should vanish only in the width limit and reported that the compiler had returned zero for that limit. Thus the generic first-derivative check was informed of the expected output; the identity-activation second coefficient was derived independently. This report concerns derivatives at initialization, with expectation taken before the width limit. It establishes no positive-time convergence theorem and no uniform Taylor remainder.

There are $m=2$ normalized inputs. The vectors $x_s:=\xi_s$ below are exactly the normalized input coordinates in the assignment; in the book's raw-input convention the corresponding vectors are $\sqrt2\,x_s$. No further input normalization is applied here. They are represented as column vectors

\[
x_1=(\alpha,0)^\top,\qquad x_2=(\beta,\gamma)^\top,
\qquad Q_{st}=x_s^\top x_t.
\]

Thus $Q_{11}=\alpha^2$, $Q_{12}=\alpha\beta$, and $Q_{22}=\beta^2+\gamma^2$. Let $y=(y_1,y_2)^\top$. Write $G=[U\ V]\in\mathbb R^{n\times2}$, $W=W^{(2)}\in\mathbb R^{n\times n}$, and $a\in\mathbb R^n$. Their entries are independent centered Gaussians, with variances $1,1/n,1$, respectively. Dots denote derivatives in the specified physical gradient-flow time. The loss is

\[
\mathcal L=\frac1{2m}\sum_{s=1}^m(f_s-y_s)^2.
\]

For the identity activation, the answer is

\[
\begin{aligned}
\lim_{n\to\infty}\mathbb E K_{12}(0)&=Q_{12}=\alpha\beta,\\
\lim_{n\to\infty}\mathbb E\dot K_{12}(0)&=0,\\
\lim_{n\to\infty}\mathbb E\frac{\ddot K_{12}(0)}2
&=\frac94(Qy)_1(Qy)_2\\
&=\frac94(\alpha^2y_1+\alpha\beta y_2)
  (\alpha\beta y_1+(\beta^2+\gamma^2)y_2).
\end{aligned}
\]

These formulas include degenerate inputs and zero labels without division by a data-dependent quantity.

## Exact identity-activation flow

In this section, all undisplayed time arguments are the current time until initialization is explicitly imposed. The forward pass is

\[
g_s=Gx_s=h_s^{(1)},\qquad h_s=Wg_s=h_s^{(2)},\qquad
f_s=\frac1n a^\top h_s,\qquad r_s=f_s-y_s,\qquad
K_{st}=\frac1n h_s^\top h_t.
\]

Define the two-dimensional vector and the two hidden-layer vectors

\[
b=\frac1m\sum_jr_jx_j,\qquad v=Gb,\qquad u=Wv.
\]

Differentiating the loss with mobility $n$ on $G,a$ and mobility (1) on $W$ gives exactly

\[
\dot G=-W^\top a b^\top,\qquad
\dot W=-\frac1n av^\top,\qquad
\dot a=-u.
\]

For the derivative calculation, introduce

\[
\begin{gathered}
P=\frac1nG^\top G,\quad M=\frac1nG^\top W^\top WG,
\quad C=WW^\top,\quad F=\frac1nG^\top W^\top a,\\
A=\frac1na^\top a,\quad D=\frac1na^\top Ca,
\quad p_s=b^\top Px_s,\quad q_s=b^\top x_s.
\end{gathered}
\]

Here $P,M\in\mathbb R^{2\times2}$, $F\in\mathbb R^2$, and $f_s=F^\top x_s$. The feature velocity and two matrix velocities are

\[
\dot h_s=-p_sa-q_sCa,\qquad
\dot C=-\frac1n(au^\top+ua^\top),\qquad
\dot P=-bF^\top-Fb^\top.
\]

The residual derivative is accounted for, rather than frozen. Indeed,

\[
\dot f_s=-b^\top(M+AP+DI_2)x_s,
\qquad
\dot b=-S(M+AP+DI_2)b,
\qquad S=\frac1m\sum_jx_jx_j^\top.
\]

Consequently, $\dot q_s=\dot b^\top x_s$ and

\[
\dot p_s=\dot b^\top Px_s+b^\top\dot P x_s.
\]

Differentiating the feature velocity now gives the exact acceleration

\[
\ddot h_s
=-\dot p_sa-\dot q_sCa
+p_su+q_sCu
+q_sa\frac{a^\top u}{n}+q_sAu.
\tag{1}
\]

The last two terms arise from the motion of the shared matrix $C$. Omitting that motion changes the second coefficient.

## Gaussian matrix moments and remainder control

All quantities in the rest of this section are at initialization. Write $W=X/\sqrt n$, where $X$ has independent standard Gaussian entries. Direct Gaussian pairing gives

\[
\mathbb E\frac{\operatorname{tr}C}{n}=1,\qquad
\mathbb E\frac{\operatorname{tr}C^2}{n}=2+\frac1n,
\qquad
\mathbb E\frac{\operatorname{tr}C^3}{n}=5+\frac6n+\frac4{n^2}.
\tag{2}
\]

Here is an explicit pairing derivation. The first trace has $n^2$ terms, each with expectation (1), and normalization $n^{-2}$. The second trace is

\[
\frac1{n^3}\sum_{i,j,a,b}
X_{ia}X_{ja}X_{jb}X_{ib}.
\]

Its three pairings leave $3,2,3$ free indices, respectively, giving $2+1/n$. For the third trace the six positions are

\[
(1,2,3,4,5,6)
=(X_{ia},X_{ja},X_{jb},X_{kb},X_{kc},X_{ic}),
\]

with normalization $n^{-4}$. Pairing equal matrix entries identifies both their row and column indices. The fifteen pairings group as follows:

| Number of free indices | Pairings |
| --- | --- |
| $4$ | $12\mid 34\mid 56, 12\mid 36\mid 45, 14\mid 23\mid 56, 16\mid 23\mid 45, 16\mid 25\mid 34$ |
| $3$ | $12\mid 35\mid 46, 13\mid 24\mid 56, 13\mid 26\mid 45, 15\mid 23\mid 46, 15\mid 26\mid 34, 16\mid 24\mid 35$ |
| $2$ | $13\mid 25\mid 46, 14\mid 25\mid 36, 14\mid 26\mid 35, 15\mid 24\mid 36$ |

Thus their contributions are $5n^4+6n^3+4n^2$, proving the last formula in (2). The numerical values (2) and (5) reflect repeated uses of the same matrix.

For completeness, the finite-moment bounds needed below do not require a spectral-limit theorem. In the pairing expansion of $n^{-1}\operatorname{tr}C^k$, the identified row-column graph is connected and has at most $k$ distinct edges and $k+1$ vertices. Each of its $(2k-1)!!$ pairings therefore contributes at most (1) after normalization. Products of traces satisfy the same bound component by component. Hence all fixed moments of normalized traces are uniformly bounded. Conditional Gaussian moment formulas then give uniform fixed-moment bounds for the normalized quadratic and bilinear forms in this calculation.

In particular, for every fixed finite moment order, $P-I_2=O_{L^p}(n^{-1/2})$ and $F=O_{L^p}(n^{-1/2})$. The first estimate follows by expanding centered averages of independent row products: a nonzero term must repeat every participating row index. For the second, condition on $G,W$: each component of $F$ is Gaussian in $a$, with variance $\|WG e_\nu\|^2/n^2$, whose fixed moments are $O(n^{-p})$ at order $p$. The preceding trace bounds justify this last estimate. The same conditioning gives

\[
\begin{aligned}
\mathbb E\left(\frac{a^\top h_s}{n}\right)^2
&=\frac{Q_{ss}}n,\\
\mathbb E\left(\frac{a^\top Ch_s}{n}\right)^2
&=\frac{Q_{ss}}n\left(5+\frac6n+\frac4{n^2}\right).
\end{aligned}
\tag{3}
\]

Their higher fixed moments have the corresponding $n^{-p/2}$ bounds. Equation (3) is one place where the third shared-matrix moment is useful, although the value of the second coefficient itself uses only the first two trace moments.

Set

\[
b_0=-\frac1m\sum_jy_jx_j,\qquad
q_s^0=b_0^\top x_s=-\frac{(Qy)_s}{m},\qquad u_0=WGb_0.
\]

Since $b=b_0+SF$, the preceding bounds imply

\[
b-b_0=O_{L^p}(n^{-1/2}),\qquad
p_s-q_s^0=O_{L^p}(n^{-1/2}),\qquad
q_s-q_s^0=O_{L^p}(n^{-1/2}).
\tag{4}
\]

All coefficients $\dot p_s,\dot q_s$ in (1) have uniformly bounded fixed moments, by their displayed exact formulas. Equations (3), (4), and Hölder's inequality therefore justify every replacement used below in $L^1$, including replacement of $u$ by $u_0$ within a normalized pairing. This controls the finite-order expectation limits without asserting a positive-time limit.

## Evaluation of the three coefficients

Independence of $G,W$ gives exactly $\mathbb E K_{st}(0)=Q_{st}$ at every width. Also,

\[
\dot K_{st}
=-p_s\frac{a^\top h_t}{n}-q_s\frac{a^\top Ch_t}{n}
 -p_t\frac{a^\top h_s}{n}-q_t\frac{a^\top Ch_s}{n}.
\]

Equations (3), (4) make its expectation tend to zero. This is not an exact finite-width parity cancellation. In fact the exact finite-width answer is

\[
\mathbb E\dot K_{st}(0)
=-\frac2m\left[
\left(\frac3n+\frac2{n^2}\right)(Q^2)_{st}
+\frac{\operatorname{tr}Q}{n^2}Q_{st}\right].
\tag{5}
\]

One derivation is the readout-conditioning identity in the next section specialized to the identity activation. Its two needed expectations are

\[
\begin{aligned}
\mathbb E[h_j^\top Ch_t]&=(2n+1)Q_{jt},\\
\mathbb E\left[\frac{g_j^\top g_s}{n}\,h_j^\top h_t\right]
&=(n+1)Q_{js}Q_{jt}+Q_{jj}Q_{st}.
\end{aligned}
\]

For the second equality, first integrate over $W$, replacing $h_j^\top h_t$ by $g_j^\top g_t$, and pair the four entries of $G$. Substitution gives (5). Labels cancel from (5) because their conditional contribution is odd in $a$.

For the second derivative, first use the exact velocity formula:

\[
\frac{\dot h_s^\top\dot h_t}{n}
=p_sp_tA+(p_sq_t+q_sp_t)D
+q_sq_t\frac{a^\top C^2a}{n}.
\]

By (2), (4), and readout conditioning,

\[
\lim_{n\to\infty}\mathbb E\frac{\dot h_s^\top\dot h_t}{n}
=q_s^0q_t^0(1+2+2)=5q_s^0q_t^0.
\tag{6}
\]

Now pair (1) with $h_t/n$. The two dotted-coefficient terms vanish in expectation by (3). So does the term containing

\[
\frac{a^\top u}{n}\frac{a^\top h_t}{n},
\]

because $a^\top u/n=b^\top F=O_{L^p}(n^{-1/2})$. For the three remaining terms, (4) reduces the calculation to

\[
q_s^0\,\mathbb E\left[
\frac{u_0^\top h_t}{n}
+\frac{u_0^\top Ch_t}{n}
+A\frac{u_0^\top h_t}{n}\right].
\]

The three expectations are $q_t^0,(2+1/n)q_t^0,q_t^0$, respectively. The first two follow by integrating $G$ and using (2); the third also uses independence of $a$ from $G,W$. Therefore

\[
\lim_{n\to\infty}\mathbb E\frac{\ddot h_s^\top h_t}{n}
=4q_s^0q_t^0.
\tag{7}
\]

Finally, differentiating the kernel twice and applying (6), (7) gives

\[
\begin{aligned}
\lim_{n\to\infty}\mathbb E\frac{\ddot K_{st}(0)}2
&=\lim_{n\to\infty}\mathbb E\left[
\frac{\ddot h_s^\top h_t+h_s^\top\ddot h_t}{2n}
+\frac{\dot h_s^\top\dot h_t}{n}\right]\\
&=(4+5)q_s^0q_t^0
=\frac9{m^2}(Qy)_s(Qy)_t.
\end{aligned}
\]

Thus residual motion has been included exactly; it drops out of this particular limiting second kernel coefficient through the small pairings in (3), not through an assumption that residuals are constant.

## Why the first expected coefficient vanishes for nonlinear activations

Return to the supplied nonlinear forward pass, writing $g_s=\phi(Gx_s)$, $h_s=\phi(Wg_s)$, and $f_s=a^\top h_s/n$. Let $\theta$ be the vector of entries of $G,W$, let $J_s=\partial h_s/\partial\theta\in\mathbb R^{n\times(2n+n^2)}$, and let $\mathsf M$ be the diagonal hidden-parameter mobility matrix: $n$ on the $G$ coordinates and $1$ on the $W$ coordinates. These objects depend on the hidden weights but not on $a$. The exact kernel gradient and hidden flow imply

\[
\mathbb E_a[\dot K_{st}\mid G,W]
=-\frac1{mn^3}\sum_j\left[
h_j^\top J_j\mathsf M J_s^\top h_t
+h_j^\top J_j\mathsf M J_t^\top h_s\right].
\tag{8}
\]

Indeed, $\dot K_{st}=-(1/m)\sum_j(f_j-y_j)\nabla_\theta K_{st}^\top\mathsf M J_j^\top a/n$, while

\[
\nabla_\theta K_{st}=\frac{J_s^\top h_t+J_t^\top h_s}{n},
\qquad
\mathbb E_a[(f_j-y_j)a\mid G,W]=\frac{h_j}{n}.
\]

Only the label-dependent part cancels by centering of the readout. The output-dependent part produces (8).

To display its scaling, define diagonal matrices

\[
D_s^{(1)}=\operatorname{diag}\phi'(Gx_s),\qquad
D_s^{(2)}=\operatorname{diag}\phi'(Wg_s).
\]

Direct differentiation of the two layers gives

\[
\frac1nJ_j\mathsf M J_s^\top
=Q_{js}D_j^{(2)}WD_j^{(1)}D_s^{(1)}W^\top D_s^{(2)}
+\frac{g_j^\top g_s}{n}D_j^{(2)}D_s^{(2)}.
\tag{9}
\]

For example, assume $\phi$ is smooth and $\phi'$ is bounded; then $\phi$ has at most linear growth. Gaussian conditioning gives uniformly bounded fixed moments of $\|g_s\|/\sqrt n$ and $\|h_s\|/\sqrt n$. To avoid invoking a spectral-norm theorem, use

\[
\|W\|_{\mathrm{op}}^2
\leq (\operatorname{tr}C^k)^{1/k}
=n^{1/k}\left(\frac{\operatorname{tr}C^k}{n}\right)^{1/k}
\]

for any fixed integer $k>1$. The pairing bounds above and Hölder's inequality applied to (8), (9) then give

\[
|\mathbb E\dot K_{st}(0)|
\leq C_k n^{-1+1/k}+C_k n^{-1}\longrightarrow0.
\]

The constants depend on the fixed inputs, activation, moment order, and $m$, but not on $n$. A sharper uniform operator-norm moment estimate yields $O(n^{-1})$; that sharper bound is not needed or used here.

More generally, any regularity and moment assumptions that make the normalized pairings in (8), (9) grow sublinearly give the same zero limit. Mere smoothness without integrability assumptions is insufficient: a smooth function can grow fast enough to make the Gaussian expectations undefined.

The nonlinear conclusion established here is therefore the vanishing width-limit first expected jet under explicit sufficient moment control. Neither centered readout symmetry alone nor this finite-order calculation establishes nonlinear positive-time convergence.
