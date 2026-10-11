# Check of two-sample avoidance from exact zero readout

Status: internally checked, 2026-10-11. The conclusions of Section 5 of the frozen source survive this audit. No fatal algebraic, measure-theoretic, or dynamical gap was found. The center-stable citation is less complete than the source's wording suggests: its relevant differentiability argument is sketched. Section 5 below supplies that argument under the analytic vector field actually used here. This is a reused-context scoped check, not a fresh isolated review and not a promotion decision.

The result is a failure-mechanism restriction, not a fitting theorem:

\[
\mathbb P\{\mathcal L_\infty>0,\ \|\theta(t)\|\not\longrightarrow\infty\}=0
\]

for every fixed width and every two nonparallel unit inputs. It leaves positive-loss escape unresolved. No experiment, Git operation, or modification of the source note was performed.

## 1. Scope, frozen inputs, and exact statement

The scientific inputs for this check are the complete assigned note and the cited primary sources below. No other study or another agent's draft was used in this check. Required research, rigorous-proof, and canonical-notation instructions were applied.

SHA256 values:

- Assigned source, UNCONDITIONAL_NEGATIVE_ROUTE.md: b4b0cc177657f7bb985d7f6e3507d3aa6011b5840e030db962f1b5c114d5329a.
- [Eldering, Lecture notes on invariant manifolds, 9 November 2016](https://www.jaapeldering.nl/files/lect-ICMC-invarmflds.pdf), PDF bytes: e7c4e868a96880a8f24149528c842b61282f33e897a14e4bcdecc18f078d4c1b. Read the cutoff discussion and complete Section 3.1, printed pages 8–13.
- [Absil, Mahony, and Andrews, SIAM Journal on Optimization 16(2), 531–547 (2005)](https://sites.uclouvain.be/absil/Publi/Convergence_SIOPT/13-60526.pdf), PDF bytes: 1705e38f0861337c25419735582c4b387f222a02d7e87702c9af8c07f3016795. Read Lemma 2.1, Theorem 2.2, and the complete proof on printed pages 533–535.
- [Authors' article and errata page](https://sites.uclouvain.be/absil/2005.901), retrieved HTML bytes: d1932b7e03c719a2d0ea2cfa57f5db842cbf04f57db8d3b70b30803d99367c32. The correction concerns discrete-time Proposition 3.3, not the continuous-time theorem used here.

Fix $n\ge1$, $d\ge2$, two unit vectors $x_1,x_2\in\mathbb R^d$ with $x_1\ne\pm x_2$, and $y\in\mathbb R^2\setminus\{0\}$. Thus $X=[x_1,x_2]$ has rank two. The parameters and forward pass are

\[
A\in\mathbb R^{n\times d},\quad W\in\mathbb R^{n\times n},
\quad w\in\mathbb R^n,\qquad
U=\tanh(AX),\quad H=\tanh(WU),\quad
f=H^\top w/n,\quad r=f-y,\quad \mathcal L=\|r\|^2/2.
\]

Write $\theta=(A,W,w)\in\mathbb R^N$, $N=nd+n^2+n$, and let $D$ be the diagonal mobility matrix with entries $n$ on $A,w$ and $1$ on $W$. The flow is $\dot\theta=-D\nabla\mathcal L$. Initialization is independent $A_{ij}\sim N(0,1)$, $W_{ij}\sim N(0,1/n)$, and exactly $w=0$. All probability statements below are at this fixed width. No width limit is needed.

The checked conclusions are

\[
\mathbb P\{\theta(t)\to\theta_* \text{ finite},\
                  \nabla\mathcal L(\theta_*)=0,\
                  \mathcal L(\theta_*)>0\}=0,
\tag{1}
\]
\[
\mathbb P\{\mathcal L_\infty>0,\
                   \|\theta(t)\|\not\to\infty\}=0.
\tag{2}
\]

The proof has four distinct bridges: strict initial loss decrease; classification and an index bound at all relevant critical points; a null intersection of their center-stable sets with $w=0$; and an analytic-flow convergence alternative.

## 2. Global flow, initial decrease, and the useful part of Section 2

For general sample count $m$, loss dissipation and bounded tanh give, with $C=2\|y\|/\sqrt m$ at zero readout,

\[
\|r(t)\|\le\|y\|,\quad
\|\dot w(t)\|_\infty\le C,\quad
\|\dot W(t)\|_F\le C\|w(t)\|_\infty,\quad
\|\dot A(t)\|_F\le C\sqrt n\,\|W(t)\|_{\rm op}\|w(t)\|_\infty.
\tag{3}
\]

For example, writing $b_a=w\odot(1-h_a^2)$,

\[
\|\dot W\|_F
\le\frac2{mn}\sum_a|r_a|\|b_a\|\|u_a\|
\le\frac2m\|w\|_\infty\sum_a|r_a|
\le C\|w\|_\infty.
\]

The corresponding rowwise formula for $\dot A$ gives the last bound in (3). Thus $w$ grows at most linearly and $W,A$ have finite bounds on each finite interval. This excludes finite-time blowup of the smooth ODE. The same argument works from any finite initial state after replacing $\|y\|$ by $\|r(0)\|$ and including $\|w(0)\|_\infty$. Consequently finite-time flow maps are defined everywhere forward, are injective local diffeomorphisms, and have smooth inverses on their open images. No global backward completeness is assumed.

At $w=0$ and $m=2$,

\[
\dot\theta=(0,0,Hy),\qquad
\dot{\mathcal L}(0)=-\|H(0)y\|^2/n.
\tag{4}
\]

The event $H(0)y=0$ is Gaussian-null at every $n$, including $n=1$. Indeed, $W$ is invertible almost surely. Conditional on such a $W$, $AX$ has a density on $\mathbb R^{n\times2}$ because $X^\top X\succ0$. The map

\[
Z\longmapsto\tanh\!\bigl(W\tanh Z\bigr)
\]

is a smooth diffeomorphism onto an open image: each tanh map is an entrywise diffeomorphism, and multiplication by invertible $W$ is invertible on each column. Therefore $H$ has a conditional density, whereas $\{H:Hy=0\}$ is a proper linear subspace. This proves strict initial decrease almost surely. Any positive limiting loss is then strictly below $\mathcal L_0=\|y\|^2/2$.

The source's general strict-saddle proposition is correct for its stated $n\ge m$ hypothesis. At a finite critical point with $r\ne0,w_i\ne0$, set

\[
v_a=(1-H_{ia}^2)r_a.
\]

Stationarity in row $i$ of $W$ implies $Uv=0$, with $v\ne0$. If $X$ has rank $m$ and $n\ge m$, choose $q\in\ker U^\top\setminus\{0\}$, $q_j\ne0$, and

\[
b=X\bigl((1-U_{j,:}^2)\odot v\bigr)\ne0.
\]

The directions $\Delta W=e_iq^\top$ and $\Delta A_{j,:}=b^\top$ satisfy

\[
D^2\mathcal L[\Delta W,\Delta W]=0,\qquad
D^2\mathcal L[\Delta W,\Delta A]
=\frac{2w_iq_j}{mn}\|b\|^2\ne0.
\tag{5}
\]

Thus a negative direction exists. Section 5 does not improperly use $n\ge2$ at $n=1$: only the earlier identity $Uv=0$, valid for every $n$, is needed for its classification. The stronger index bound below replaces (5).

For completeness, Section 1's readout identity also has the right normalization:

\[
q=\|w\|^2/n,\qquad
\dot q=-4f^\top r/m\le\|y\|^2/m.
\]

Together with loss dissipation this gives its weighted integrability assertion. Neither that assertion nor its prediction-alignment corollary is needed for (1)–(2).

## 3. Classification of relevant finite critical points

Consider a finite critical point with $0<\mathcal L<\mathcal L_0$. Necessarily $f\ne0$ and $w\ne0$. An active row $i$, meaning $w_i\ne0$, gives $Uv=0$ with nonzero $v\in\mathbb R^2$. Hence $\operatorname{rank}U\le1$, and $f\ne0$ excludes rank zero.

If $u_1=0$, then $u_2\ne0$. Row-$i$ stationarity in $W$ gives $(1-H_{i2}^2)r_2u_2=0$, hence $r_2=0$ and $f=(0,y_2)$. If $u_2=0$, the result is $f=(y_1,0)$.

Otherwise $u_2=cu_1$ for some $c\ne0$. Put $z_i=(Wu_1)_i$. At every active row, readout and middle-weight stationarity imply

\[
r_1\tanh z_i+r_2\tanh(cz_i)=0,\qquad
r_1\operatorname{sech}^2z_i+
cr_2\operatorname{sech}^2(cz_i)=0.
\tag{6}
\]

Neither residual coordinate can vanish, since the second equation would then force both to vanish. Some active row has $z_i\ne0$, or both predictions would be zero. Eliminating the two nonzero residuals in that row yields

\[
\tanh(cz_i)\operatorname{sech}^2z_i
=c\tanh z_i\operatorname{sech}^2(cz_i),
\qquad
\sinh(2cz_i)=c\sinh(2z_i).
\]

For $v>0$, $(\sinh v/v)'=(v\cosh v-\sinh v)/v^2>0$, because the numerator starts at zero and has derivative $v\sinh v>0$. Evenness therefore forces $|c|=1$. Write $c=s\in\{-1,1\}$. Then $r_1+sr_2=0$ and $f_2=sf_1$. The resulting necessary list is exactly

\[
(y_1,0),\quad(0,y_2),\quad
\left(\frac{y_1+y_2}{2},\frac{y_1+y_2}{2}\right),\quad
\left(\frac{y_1-y_2}{2},-\frac{y_1-y_2}{2}\right).
\tag{7}
\]

Only entries with loss in $(0,\mathcal L_0)$ enter the subsequent argument. This is a complete list of possibilities, not a statement that every listed prediction is realized by a critical point at every width.

## 4. At least $n$ negative Hessian directions

### 4.1 Signed-diagonal case

Suppose $u_2=su_1$. Injectivity and oddness give $Ax_2=sAx_1$. Since $X$ has rank two, the vectors

\[
p=(Ax_1+sAx_2)/2,\qquad a=(Ax_1-sAx_2)/2
\]

are independent linear coordinates on the part of $A$ acting on the input span. Completing them with the unused coordinates gives an invertible linear parameter change.

Define $F(p)=w^\top\tanh(W\tanh p)/n$ and

\[
f_s=(f_1+sf_2)/2,\quad f_d=(f_1-sf_2)/2,\quad
y_s=(y_1+sy_2)/2,\quad y_d=(y_1-sy_2)/2.
\]

Then

\[
f_s=\frac{F(p+a)+F(p-a)}2,\quad
f_d=\frac{F(p+a)-F(p-a)}2,\quad
\mathcal L=(f_s-y_s)^2+(f_d-y_d)^2.
\tag{8}
\]

At the point in question, $a=0$, $f_s=y_s\ne0$, and $f_d=0$ with $y_d\ne0$. Parity gives $\nabla_af_s=0$ and $\nabla_a^2f_d=0$. Stationarity gives $-2y_d\nabla_af_d=0$. Every term in the $a,a$ block of the loss Hessian therefore vanishes. Splitting the remaining coordinates into a vector $v$ gives

\[
\nabla^2\mathcal L=
\begin{pmatrix}0&B\\B^\top&C\end{pmatrix},
\qquad
B=-2y_d\,D_v(\nabla_af_d).
\tag{9}
\]

Set $u=\tanh p$, $z=Wu$,
$D_1=\operatorname{diag}(\operatorname{sech}^2p)$,
$D_2=\operatorname{diag}(\operatorname{sech}^2z)$,
and $t=D_2w\ne0$. At $a=0$,

\[
\nabla_af_d=D_1W^\top t/n.
\]

With $p$ fixed its variation is

\[
\delta(\nabla_af_d)=\frac1nD_1
\left[\delta W^\top t+
W^\top\operatorname{diag}(w\odot\tanh''z)\delta Wu+
W^\top D_2\delta w\right].
\tag{10}
\]

This is surjective onto $\mathbb R^n$. Explicitly, for any $v_0\in\mathbb R^n$, take

\[
\delta W=\frac{t v_0^\top}{\|t\|^2},\qquad
\delta w=-D_2^{-1}
\operatorname{diag}(w\odot\tanh''z)\delta Wu.
\]

The bracket in (10) becomes $v_0$, and $D_1$ is invertible. Since $y_d\ne0$, $B$ has row rank $n$. This cancellation remains valid when $W$ is singular.

### 4.2 Axis case

Suppose $Ax_2=0$, and use $a=Ax_2$ while holding $Ax_1$ fixed. Here $f_1=y_1\ne0$, $f_2=0$, and $y_2\ne0$. The function $f_2(a)$ is odd, whereas $f_1$ is independent of $a$. Stationarity implies

\[
\nabla_af_2=W^\top w/n=0.
\]

The $a,a$ Hessian block again vanishes. Its mixed block is $-y_2D_v(\nabla_af_2)$, and

\[
\delta_W(\nabla_af_2)=\delta W^\top w/n
\]

is surjective since $w\ne0$. Interchanging the samples handles the other axis.

### 4.3 Inertia and mobility

For any block matrix (9) with $\operatorname{rank}B=n$, choose a right inverse $R$ with $BR=I_n$. On the $n$-dimensional subspace $(a,-\epsilon Ra)$,

\[
(a,-\epsilon Ra)^\top
\begin{pmatrix}0&B\\B^\top&C\end{pmatrix}
(a,-\epsilon Ra)
=-2\epsilon\|a\|^2+\epsilon^2a^\top R^\top CRa<0
\]

for sufficiently small fixed $\epsilon>0$. Thus the Hessian has at least $n$ negative eigenvalues. Invertible coordinate changes preserve this count. The flow linearization

\[
J=-D\nabla^2\mathcal L
\]

is similar to the symmetric matrix $-D^{1/2}\nabla^2\mathcal L D^{1/2}$, so it has at least $n$ positive eigenvalues, with multiplicities counted, and is real diagonalizable.

At $n=1$ there are in fact no relevant finite critical points: signed-diagonal stationarity forces $Wt=0$, hence $W=0$, contradicting $f\ne0$; the axis case gives the same contradiction from $Ww=0$. The claimed index statement is harmlessly vacuous there.

## 5. Center-stable source check and the needed regularity

Eldering's cutoff/Perron construction supplies bounded-orbit containment and flow invariance. However, printed page 13 treats $C^1$ regularity for nonnegative center-stable growth rates by a sketch, not the preceding ordinary implicit-function proof. The latter chooses a negative weight and does not directly cover center directions. The following specialization completes that detail using the present $C^2$ vector field and diagonalizable linearization. No stronger smoothness is needed. [Primary source, Section 3.1](https://www.jaapeldering.nl/files/lect-ICMC-invarmflds.pdf)

At an equilibrium translate the point to zero and make a fixed invertible linear change so the linear part is $\operatorname{diag}(J_{\rm cs},J_{\rm u})$, with

\[
\|e^{J_{\rm cs}t}\|\le C\quad(t\ge0),\qquad
\|e^{-J_{\rm u}t}\|\le Ce^{-\lambda t}\quad(t\ge0)
\]

for $\lambda>0$. The unstable dimension is $k\ge n$. Write the nonlinear remainder as $F=(F_{\rm cs},F_{\rm u})$, with $F(0)=DF(0)=0$.

Multiply it by a smooth cutoff supported in a ball of radius $2r$ and equal to one in the ball of radius $r$. For small $r$, the resulting $F$ has arbitrarily small global first derivative, say $\|DF\|_\infty\le\delta$, and finite global second-derivative bound $K$. This follows from $DF(z)\to0$ and $F(z)=o(\|z\|)$; the factors $1/r$ from differentiating the cutoff are canceled by these small quantities. The second derivative need only be finite, not small.

Choose $0<2\rho<\lambda$. For curves $z:[0,\infty)\to\mathbb R^N$, define

\[
\|z\|_\sigma=\sup_{t\ge0}e^{-\sigma t}\|z(t)\|,
\qquad \sigma\in\{\rho,2\rho\}.
\]

Define the linear integral operator

\[
(\mathcal K q)_{\rm cs}(t)=
\int_0^t e^{J_{\rm cs}(t-s)}q_{\rm cs}(s)\,ds,\qquad
(\mathcal K q)_{\rm u}(t)=
-\int_t^\infty e^{J_{\rm u}(t-s)}q_{\rm u}(s)\,ds.
\]

It satisfies

\[
\|\mathcal K\|_{\sigma\to\sigma}
\le C\left(\frac1\sigma+\frac1{\lambda-\sigma}\right).
\tag{11}
\]

For each center-stable initial coordinate $\xi$, solve

\[
z_\xi(t)=(e^{J_{\rm cs}t}\xi,0)+\mathcal K[F(z_\xi)](t).
\tag{12}
\]

Choose $\delta$ so that the nonlinear term is a contraction with constant at most $1/2$ in both weighted spaces. Equation (12) then has a unique solution in the $\rho$ space; it is also the unique solution in the $2\rho$ space. Moreover

\[
\|z_{\xi+h}-z_\xi\|_\rho\le C_0\|h\|.
\tag{13}
\]

To prove differentiability rather than assume it, define $q_{\xi,h}$ as the unique solution

\[
q_{\xi,h}=(e^{J_{\rm cs}t}h,0)
+\mathcal K[DF(z_\xi)q_{\xi,h}].
\]

It is linear in $h$ and has $\|q_{\xi,h}\|_\rho\le C_0\|h\|$. Taylor's formula and (13) give

\[
\|F(z_{\xi+h})-F(z_\xi)
-DF(z_\xi)(z_{\xi+h}-z_\xi)\|_{2\rho}
\le \frac K2 C_0^2\|h\|^2.
\]

Subtracting the equations and inverting the same contraction in the $2\rho$ space proves

\[
\|z_{\xi+h}-z_\xi-q_{\xi,h}\|_{2\rho}\le C_1\|h\|^2.
\tag{14}
\]

Also, the difference of the two linear-response equations, bounded using
$\|DF(z_{\xi'})-DF(z_\xi)\|\le K\|z_{\xi'}-z_\xi\|$, yields

\[
\|q_{\xi',h}-q_{\xi,h}\|_{2\rho}
\le C_2\|\xi'-\xi\|\|h\|.
\tag{15}
\]

Evaluation at time zero is bounded in either space. Therefore
$\alpha(\xi)=(z_\xi)_{\rm u}(0)$ is $C^1$, with
$D\alpha(\xi)h=(q_{\xi,h})_{\rm u}(0)$ by (14), continuously by (15). At $\xi=0$, $z_0=0$ and $DF(0)=0$, so $\alpha(0)=D\alpha(0)=0$.

Its graph is an embedded $C^1$ manifold of dimension $N-k$. Every bounded forward orbit inside the uncut radius-$r$ neighborhood solves (12): variation of constants in the unstable component, with terminal time tending to infinity, removes the terminal term using its exponential decay. Such an orbit therefore starts on this graph by uniqueness.

The cutoff vector field is globally Lipschitz, so its flow exists in both time directions. Every finite time shift of a curve in the $\rho$ space remains in that space, including a finite backward extension. Uniqueness in (12) then proves invariance of the graph under that cutoff flow. Inside the radius-$r$ neighborhood the original field equals the cutoff field. Restricting the graph to this open neighborhood gives the needed local manifold, with the original vector field tangent at every point. This proves all manifold properties used below, including the center case.

## 6. Slice-null intersections and the countable cover

Let

\[
M_0=\{(A,W,w):w=0\},\qquad \dim M_0=N-n.
\]

For each relevant bad critical point $q$, choose an open neighborhood $O_q$ and the local manifold $S_q\subset O_q$ just constructed. Then $\dim S_q\le N-n$, the vector field $V=-D\nabla\mathcal L$ is tangent to $S_q$, and every orbit staying in $O_q$ for all positive times starts in $S_q$.

For an integer $\ell\ge0$, let $\Phi_\ell$ denote the actual finite-time flow and set

\[
S_{q,\ell}=\Phi_\ell^{-1}(S_q).
\]

This is a $C^1$ embedded manifold, possibly empty, since $\Phi_\ell$ is a diffeomorphism onto an open image. It has the same dimension as $S_q$ wherever nonempty. The autonomous-flow identity

\[
D\Phi_\ell(p)V(p)=V(\Phi_\ell(p))
\tag{16}
\]

shows $V(p)\in T_pS_{q,\ell}$ at every $p\in S_{q,\ell}$. Thus no unsupported claim of global invariance of a truncated local manifold is being used.

At $p\in M_0$ with $H(p)y\ne0$, equation (4) gives
$V(p)=(0,0,H(p)y)\notin T_pM_0$. Consequently

\[
T_pM_0\not\subset T_pS_{q,\ell}.
\tag{17}
\]

Indeed, if inclusion held, the inequality $\dim S_{q,\ell}\le\dim M_0$ would force equality of tangent spaces, contradicting $V(p)\in T_pS_{q,\ell}$ and $V(p)\notin T_pM_0$.

Locally write $S_{q,\ell}=\{F=0\}$ for a $C^1$ submersion $F$. Its tangent space is $\ker DF(p)$. Equation (17) means $D(F|_{M_0})(p)\ne0$. At least one scalar component has nonzero derivative on $M_0$; its zero set is locally a codimension-one $C^1$ submanifold of $M_0$. It contains the intersection, so that intersection is Lebesgue-null in $M_0$. Second countability gives a countable chart cover of these intersection points.

Notice the exact strength: (17) is weaker than full transversality, but it is sufficient. A plain ambient strict-saddle avoidance theorem would not be sufficient for this singular initialization.

The bad critical set, as a subspace of Euclidean space, is second countable and Lindelof. Its open cover by the neighborhoods $O_q$ therefore has a countable subcover $\{O_{q_j}\}_{j\ge1}$. If an orbit converges to a bad critical point $q_*$, choose $j$ with $q_*\in O_{q_j}$. Since this neighborhood is open, convergence gives an integer $\ell$ such that

\[
\Phi_t(p)\in O_{q_j}\quad\hbox{for every }t\ge\ell.
\]

The orbit from $\Phi_\ell(p)$ is bounded and remains in that neighborhood, so it lies on $S_{q_j}$. Thus

\[
\{p\in M_0:H(p)y\ne0,\ \Phi_t(p)\to\hbox{a relevant bad critical point}\}
\subset
\bigcup_{j,\ell}\bigl(S_{q_j,\ell}\cap M_0\cap\{Hy\ne0\}\bigr).
\tag{18}
\]

This is a countable union of slice-null sets. The Gaussian law of $(A,W)$ is absolutely continuous on $M_0$, and the remaining set $\{Hy=0\}$ is null by Section 2. Strict initial loss decrease excludes all critical limits at loss $\mathcal L_0$ or above. This proves (1). It does not require isolated critical points or a countable critical set.

## 7. Analytic convergence alternative and its hypotheses

Theorem 2.2 of Absil–Mahony–Andrews applies to a $C^1$ curve for an analytic objective with an eventual positive angle condition and “zero objective derivative implies zero velocity.” It gives norm tending to infinity or one finite limit, without coercivity, boundedness, or isolated critical points. [Primary theorem and proof](https://sites.uclouvain.be/absil/Publi/Convergence_SIOPT/13-60526.pdf)

For the present fixed width, set

\[
\eta=D^{-1/2}\theta,\qquad
\widetilde{\mathcal L}(\eta)=\mathcal L(D^{1/2}\eta).
\]

Then $\dot\eta=-\nabla\widetilde{\mathcal L}(\eta)$ and

\[
\dot{\widetilde{\mathcal L}}=-\|\nabla\widetilde{\mathcal L}\|^2
=-\|\nabla\widetilde{\mathcal L}\|\|\dot\eta\|.
\tag{19}
\]

The angle constant is exactly one; $\dot{\widetilde{\mathcal L}}=0$ implies $\dot\eta=0$. Tanh is real analytic on the whole real line, so $\widetilde{\mathcal L}$ is real analytic on $\mathbb R^N$. Section 2 proves global existence. All theorem hypotheses hold.

For a finite accumulation point $\eta_*$, put $E(t)=\widetilde{\mathcal L}(\eta(t))-\widetilde{\mathcal L}(\eta_*)\downarrow0$. The local analytic gradient inequality $\|\nabla\widetilde{\mathcal L}\|\ge cE^\mu$, $\mu<1$, gives, while $E>0$ and the orbit remains nearby,

\[
-\frac d{dt}\frac{E^{1-\mu}}{c(1-\mu)}
=\frac{\|\nabla\widetilde{\mathcal L}\|^2}{cE^\mu}
\ge\|\dot\eta\|.
\]

An entry sufficiently close to $\eta_*$ has remaining allowed length smaller than its distance to the neighborhood boundary. It cannot exit and has a finite limit. If $E$ reaches zero, (19) makes the orbit stationary. Thus unbounded recurrence with a finite accumulation point is excluded.

A finite limit is critical here: if $\nabla\widetilde{\mathcal L}(\eta_*)\ne0$, continuity makes $\|\nabla\widetilde{\mathcal L}(\eta(t))\|$ bounded below for all sufficiently large times, and (19) would force $\widetilde{\mathcal L}\to-\infty$, contradicting its nonnegativity. Since $D$ is fixed and positive, the norms of $\eta$ and $\theta$ are equivalent. Combining this alternative with (1) proves (2).

The [authors' erratum](https://sites.uclouvain.be/absil/2005.901) addresses an exit-by-large-step defect in discrete-time Proposition 3.3. No part of that proposition is used above.

## 8. Objections resolved and exact remaining scope

| Objection | Resolution |
|---|---|
| The rank argument silently requires $n\ge2$. | Only $Uv=0$ is used in the two-sample classification; it holds for every $n$. The $n=1$ bad class is empty. |
| A signed-diagonal critical point might have a nonzero $a,a$ Hessian block. | Parity, the fitted common mode, and stationarity of the unfitted mode eliminate every term in that block. |
| Singular $W$ prevents the mixed derivative from being surjective. | The explicit combined $\delta W,\delta w$ choice in (10) cancels the troublesome term without inverting $W$. |
| A density in hidden parameters is insufficient for saddle avoidance. | Correct in general. Here the $n$-direction index bound and the nonzero normal flow at $w=0$ give slice-null intersections directly. |
| The manifold argument assumes full transversality. | It needs only a nonzero scalar defining derivative on $M_0$, which (17) proves. |
| Uncountably many saddle basins invalidate the measure-zero union. | A countable cover by trapping neighborhoods and integer entrance times gives (18). |
| Local invariance is lost under finite-time pullback. | Tangency follows from (16); global invariance of the local piece is unnecessary. |
| The cited center-stable proof is incomplete in the center case. | Its regularity step is sketched; Section 5 supplies the needed two-weight proof under the present hypotheses. |
| Analytic convergence only applies to bounded orbits. | The checked theorem starts from one accumulation point and excludes unbounded recurrence as well. |
| The analytic paper has an erratum. | It concerns a separate discrete-time proposition, not the continuous-time result used. |

Conclusion: equations (1)–(2) are established by the reconstructed argument. The meaningful remaining obstruction is precisely positive-loss escape to infinity. The check supplies no bound on its probability, no proof that it happens, and no all-data fitting theorem. It should not be described as unconditional fitting or as a macroscopic nonfitting construction.
