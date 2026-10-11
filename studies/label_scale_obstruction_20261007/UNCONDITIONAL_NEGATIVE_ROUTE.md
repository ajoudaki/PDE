# Independent negative-first route: exclusions and two-input saddle avoidance

Status: independent theoretical route, 2026-10-11, including a subsequent positive pivot. For two distinct, nonantipodal unit inputs, Section 5 proves almost-sure avoidance of every finite bad critical limit under the actual Gaussian initialization with zero readout. Consequently any positive-loss failure must have parameter norm tending to infinity. This does not prove fitting or the requested unconditional nonfitting result. Scientific inputs are the supervisor's prompt, the derivations below, and the explicitly cited dynamical-systems results. No experiments were run, and no other study artifacts were read.

## Target and exact model

Fix unit inputs $x_a\in\mathbb R^d$, $a=1,\ldots,m$, and labels $y\in\mathbb R^m$, independently of width and initialization. Write $X=[x_1,\ldots,x_m]\in\mathbb R^{d\times m}$. At width $n$, the state and predictions are

\[
A\in\mathbb R^{n\times d},\quad W\in\mathbb R^{n\times n},\quad w\in\mathbb R^n,
\qquad U=\tanh(AX),\quad H=\tanh(WU),\quad f=H^\top w/n.
\]

The residual is $r=f-y$, the loss is $\mathcal L=\|r\|^2/m$, and the gradient-flow mobilities of $(A,W,w)$ are $(n,1,n)$. Initially the entries of $A$ are independent $N(0,1)$, the entries of $W$ are independent $N(0,1/n)$, these arrays are independent, and $w=0$. Let

\[
D^{(1)}=1-U^{\odot2},\qquad D^{(2)}=1-H^{\odot2}.
\]

Here powers and products marked by $\odot$ act entrywise. The exact equations are

\[
\begin{aligned}
\dot w&=-\frac2m Hr,\\
\dot W&=-\frac2{mn}\operatorname{diag}(w)D^{(2)}\operatorname{diag}(r)U^\top,\\
\dot A&=-\frac2m
\left[\left(W^\top\operatorname{diag}(w)D^{(2)}\operatorname{diag}(r)\right)\odot D^{(1)}\right]X^\top.
\end{aligned}
\]

The macroscopic negative target is a fixed admissible dataset and constants $\epsilon,p>0$ such that

\[
\liminf_{n\to\infty}\mathbb P\!\left[\lim_{t\to\infty}\mathcal L_n(t)\ge\epsilon\right]\ge p.
\]

The initial population feature Gram must be positive definite. Positive losses that vanish with $n$, engineered initializations whose Gaussian probability vanishes, and finite-time plateaus do not establish this target.

## 1. Global existence and a restriction on saturation explanations

Set $\mathcal L_0=\|y\|^2/m$. Loss dissipation gives

\[
-\dot{\mathcal L}
=n\|\nabla_A\mathcal L\|_F^2+\|\nabla_W\mathcal L\|_F^2+n\|\nabla_w\mathcal L\|^2
\ge\frac4{m^2n}\|Hr\|^2.
\tag{1}
\]

In particular $\|r(t)\|\le\|y\|$. With $C=2\|y\|/\sqrt m$, bounded activations imply

\[
\|w(t)\|_\infty\le Ct,\quad
\|\dot W(t)\|_F\le C\|w(t)\|_\infty,\quad
\|\dot A(t)\|_F\le C\sqrt n\|W(t)\|_{\rm op}\|w(t)\|_\infty.
\]

For the second inequality, bound the Frobenius norm of
$\operatorname{diag}(w)D^{(2)}\operatorname{diag}(r)$ by
$\sqrt n\|w\|_\infty\|r\|$, and use $\|U\|_{\rm op}\le\sqrt{nm}$.
For the third, also use $\|X\|_{\rm op}\le\sqrt m$. These inequalities bound all parameters on each finite time interval. The smooth vector field therefore has a global solution. The nonnegative decreasing loss has a limit.

Define the normalized readout energy $q(t)=\|w(t)\|^2/n$. Its exact evolution is

\[
\dot q=-\frac4m f^\top r
=\frac{\|y\|^2}{m}-\frac4m\|f-y/2\|^2
\le\mathcal L_0,
\qquad q(t)\le\mathcal L_0t.
\tag{2}
\]

Cauchy--Schwarz gives

\[
|f^\top r|^2
=|w^\top Hr/n|^2
\le q\,\|Hr\|^2/n.
\]

Combining this with (1)--(2), with the case $q=0$ understood directly from $f=0$, yields

\[
\int_1^\infty \frac{|f(t)^\top r(t)|^2}{t}\,dt<\infty
\qquad (y\ne0).
\tag{3}
\]

Consequently, if predictions converge to $f_\infty$, then

\[
f_\infty^\top(f_\infty-y)=0.
\tag{4}
\]

Indeed, a nonzero limit of the inner product would contradict the divergence of $\int_1^\infty dt/t$. This conclusion uses no feature-rank bound and permits diverging hidden parameters.

If the loss strictly decreases from $\mathcal L_0$ at some finite time, asymptotic alignment of predictions with the label line is sufficient for exact fitting:

\[
\operatorname{dist}(f(t),\operatorname{span}\{y\})\longrightarrow0
\quad\Longrightarrow\quad
\mathcal L(t)\longrightarrow0.
\tag{5}
\]

To prove (5) without assuming convergence of $f$, use (3) to select $t_k\to\infty$ with $f(t_k)^\top r(t_k)\to0$. Predictions are bounded because $\|r\|\le\|y\|$. A subsequence converges to $\alpha y$, where $\alpha(\alpha-1)\|y\|^2=0$. The case $\alpha=0$ contradicts the strict loss decrease, so $\alpha=1$. The full loss limit is therefore zero.

This rules out a positive-loss explanation consisting only of a wrong limiting scalar gain $f\to\alpha y$. It also rules out convergence of predictions into a subspace orthogonal to $y$, once strict loss decrease has occurred. It does **not** rule out convergence to a nontrivial projection of $y$ onto another subspace. Such a projection satisfies (4) and can leave a positive residual.

## 2. Strict saddles for linearly independent inputs

**Proposition.** Suppose $X$ has column rank $m$ and $n\ge m$. At every finite critical point with $r\ne0$ and $w\ne0$, the Hessian of $\mathcal L$ has a negative direction involving only $A,W$, with $w$ held fixed. Thus every critical point with $0<\mathcal L<\mathcal L_0$ is a strict saddle. The labels may have arbitrary magnitudes and signs, and the inputs may be arbitrarily strongly correlated subject to linear independence.

**Proof.** Choose $i$ with $w_i\ne0$, and define

\[
v_a=D^{(2)}_{ia}r_a,\qquad a=1,\ldots,m.
\]

At a finite state all entries of $D^{(2)}$ are strictly positive, so $v\ne0$. Stationarity in row $i$ of $W$ gives $Uv=0$. Therefore $\operatorname{rank}U<m\le n$, and there exists nonzero $q\in\ker U^\top$. Choose $j$ with $q_j\ne0$, and set

\[
b=X\bigl(D^{(1)}_{j,:}\odot v\bigr)\in\mathbb R^d.
\]

Since $X$ is injective on $\mathbb R^m$, $D^{(1)}_{j,:}$ is entrywise positive, and $v\ne0$, we have $b\ne0$.

Take $\Delta W=e_iq^\top$, and let $\Delta A$ have only row $j$ nonzero, equal to $b^\top$. The perturbation $W+s\Delta W$ leaves $WU$, and hence the loss, exactly unchanged when $A$ is fixed, because $q^\top U=0$. Thus

\[
D^2\mathcal L[\Delta W,\Delta W]=0.
\]

Let $\Delta U=D^{(1)}\odot(\Delta A X)$. The mixed derivative of the preactivation is $\Delta W\Delta U$; its first derivative in the $\Delta W$ direction is zero, so the second derivative of tanh contributes no additional term to the mixed derivative. The first prediction derivative in the $\Delta W$ direction is also zero. Hence

\[
\begin{aligned}
D^2\mathcal L[\Delta W,\Delta A]
&=\frac{2w_i}{mn}\sum_a r_aD^{(2)}_{ia}(q^\top\Delta U)_a\\
&=\frac{2w_iq_j}{mn}\sum_a v_aD^{(1)}_{ja}\,b^\top x_a\\
&=\frac{2w_iq_j}{mn}\|b\|^2\ne0.
\end{aligned}
\]

The Hessian restricted to these two directions has the form
$\left(\begin{smallmatrix}0&c\\c&d\end{smallmatrix}\right)$ with $c\ne0$, so its determinant is negative. It has a negative eigenvalue. Finally, $w=0$ would imply $f=0$ and $\mathcal L=\mathcal L_0$, proving the last assertion. Positive mobilities preserve negative curvature by congruence. $\square$

For these full-column-rank inputs, the stated Gaussian initialization has $\operatorname{rank}H(0)=m$ almost surely. Each row of $AX$ has a nondegenerate Gaussian density, and entrywise tanh is a diffeomorphism onto $(-1,1)^m$, so $U$ has rank $m$ almost surely for $n\ge m$. Conditional on such $U$, each row of $WU$ again has a nondegenerate Gaussian density, giving the claim for $H$. Therefore for $y\ne0$,

\[
\dot{\mathcal L}(0)=-\frac4{m^2n}\|H(0)y\|^2<0
\]

almost surely. Every eventual finite bad critical point is consequently in the strict-saddle class just proved.

## 3. What a finite bad minimum requires for dependent inputs

The mixed-derivative proof also gives an exact necessary condition without assuming $\operatorname{rank}X=m$. At a residual-positive local minimum with $w_i\ne0$, define $v_a=D^{(2)}_{ia}r_a$ as above. For every $j$ for which some $q\in\ker U^\top$ has $q_j\ne0$, positive semidefiniteness of the Hessian forces

\[
X\bigl(D^{(1)}_{j,:}\odot v\bigr)=0.
\tag{6}
\]

The indices excluded from this conclusion satisfy $e_j\in\operatorname{col}U$. There are at most $\operatorname{rank}U\le m-1$ such indices. Thus at least $n-m+1$ first-layer neurons satisfy (6).

Equivalently, freeze the coefficients of the analytic ridge combination

\[
G_i(u)=\sum_{a=1}^m r_aD^{(2)}_{ia}\tanh(u^\top x_a),\qquad u\in\mathbb R^d.
\]

Stationarity in $W$ gives $G_i(A_{j,:}^\top)=0$ for **every** $j$, and (6) gives
$\nabla G_i(A_{j,:}^\top)=0$ for at least $n-m+1$ neurons, for every active row $i$. A proposed finite bad-minimum mechanism on low-dimensional inputs must therefore produce this simultaneous critical-zero structure across essentially all first-layer neurons. This is a necessary condition, not an impossibility result: gradient flow can approach sets that had zero probability initially.

## 4. First-round bottleneck, refined for two inputs in Section 5

No fixed dataset and labels, Gaussian event of nonvanishing probability, and macroscopic residual lower bound have been established by this route.

For full-column-rank inputs the finite-critical-point obstruction is now explicit. If a trajectory is bounded and has a positive limiting loss, (1) gives a sequence of times with parameter gradients tending to zero. Compactness provides a finite critical accumulation point at that same loss. Strict initial decrease and the proposition force that point to be a strict saddle. A negative construction in this class must therefore establish either:

1. positive-probability capture by bad strict saddles despite hidden-parameter randomness and $w(0)=0$; or
2. escape of some parameters to infinity together with a residual bounded away from zero.

Neither mechanism is proved. Conversely, a general strict-saddle avoidance theorem for initializations with a density in *all* parameters cannot simply be applied: the prescribed initialization is supported on the submanifold $w=0$. Boundedness of parameters has not been established either. These are substantive gaps, not consequences of the initial Gram condition.

For dependent or low-dimensional inputs, finite bad minima additionally require the critical-zero structure in Section 3. To turn that geometry into the requested negative theorem still requires a basin estimate under the actual Gaussian initialization and an asymptotic residual lower bound uniform in width. Showing only that this geometry exists, or that an engineered basin is open at each fixed width, does not supply either requirement.

The sharpest unresolved question at this stage was whether an initially full-rank Gaussian feature ensemble can dynamically collapse, with nonvanishing probability as width grows, into this critical-zero structure or a saturated state while retaining macroscopic residual. Section 5 removes finite bad critical limits for two inputs; it leaves escape to infinity unresolved.

## 5. Two inputs: finite bad limits have Gaussian probability zero

Assume now $m=2$, $x_1\ne\pm x_2$, and $y\ne0$. The unit-norm assumption makes $x_1,x_2$ linearly independent. No assumption is imposed on their correlation or the signs, relative magnitudes, or overall scale of the labels. The argument applies at every fixed width $n\ge1$.

**Theorem.** Under the initialization in Section 1,

\[
\mathbb P\!\left[
\theta(t)\longrightarrow\theta_*\text{ for a finite critical point with }\mathcal L(\theta_*)>0
\right]=0,
\tag{7}
\]

where $\theta=(A,W,w)$ denotes all parameters. In fact,

\[
\mathbb P\!\left[
\mathcal L_\infty>0\ \text{and}\ \|\theta(t)\|\not\longrightarrow\infty
\right]=0.
\tag{8}
\]

Thus the singular initialization $w(0)=0$ does not cause finite bad critical limits in the two-input problem. Equation (8) is a failure-mechanism theorem; it does not rule out parameter escape and is not an unconditional fitting theorem.

### 5.1 Exact classification of finite bad critical predictions

At a critical point with $0<\mathcal L<\mathcal L_0$, we have $w\ne0$ and $f\ne0$. The proof in Section 2 gives $\operatorname{rank}U<2$, while $f\ne0$ excludes rank zero. If $U_{:,1}=0$, stationarity in an active row of $W$ gives $r_2=0$; the predictions are therefore $f=(0,y_2)$. If $U_{:,2}=0$, they are $f=(y_1,0)$.

Otherwise write $U_{:,2}=cU_{:,1}$ with $c\ne0$. Put $z=(WU_{:,1})_i$. Readout stationarity and stationarity in any active row $i$, meaning $w_i\ne0$, give

\[
r_1\tanh z+r_2\tanh(cz)=0,
\qquad
r_1\operatorname{sech}^2z+c r_2\operatorname{sech}^2(cz)=0.
\tag{9}
\]

Both residual coordinates are nonzero in this case. Some active row has $z\ne0$, since otherwise $f=0$. Eliminating the residuals in that row gives

\[
\sinh(2cz)=c\sinh(2z).
\]

The function $\sinh u/u$, with its continuous value at zero, is even and strictly increasing on $u>0$: its derivative has numerator $u\cosh u-\sinh u$, which vanishes at zero and has positive derivative $u\sinh u$. Hence $|c|=1$. Writing $c=s\in\{1,-1\}$, (9) gives $r_1+s r_2=0$, and oddness gives $f_2=s f_1$. Thus the complete list is

\[
(y_1,0),\quad (0,y_2),\quad
\left(\frac{y_1+y_2}{2},\frac{y_1+y_2}{2}\right),\quad
\left(\frac{y_1-y_2}{2},-\frac{y_1-y_2}{2}\right).
\tag{10}
\]

Only entries with loss strictly between zero and $\mathcal L_0$ are relevant. The classification concerns finite critical points, not limits with diverging parameters.

### 5.2 Every such critical point has at least $n$ negative directions

For the case $U_{:,2}=sU_{:,1}$, injectivity and oddness of tanh imply $Ax_2=sAx_1$. Use the independent linear coordinates

\[
p=(Ax_1+sAx_2)/2,\qquad a=(Ax_1-sAx_2)/2
\]

for the part of $A$ acting on the input span. The remaining input directions have no effect on the loss. Define

\[
F(p;W,w)=w^\top\tanh(W\tanh p)/n,
\quad f_s=(f_1+s f_2)/2,\quad f_d=(f_1-s f_2)/2,
\]

and similarly $y_s=(y_1+s y_2)/2$, $y_d=(y_1-s y_2)/2$. Then

\[
f_s=\frac{F(p+a)+F(p-a)}2,\qquad
f_d=\frac{F(p+a)-F(p-a)}2,\qquad
\mathcal L=(f_s-y_s)^2+(f_d-y_d)^2.
\]

At the critical point, $a=0$, $f_s=y_s\ne0$, $f_d=0$, and $y_d\ne0$. The first expression is even in $a$, the second odd. Moreover stationarity implies $\nabla_a f_d=0$. Consequently the Hessian, split into the $n$ coordinates $a$ and all remaining coordinates, has the block form

\[
\nabla^2\mathcal L=
\begin{pmatrix}0&B\\B^\top&C\end{pmatrix}.
\tag{11}
\]

We show that $B$ has row rank $n$. At $a=0$, write

\[
u=\tanh p,\quad z=Wu,\quad D_1=\operatorname{diag}(\operatorname{sech}^2p),\quad
D_2=\operatorname{diag}(\operatorname{sech}^2z),\quad t=D_2w\ne0.
\]

Then $\nabla_a f_d=D_1W^\top t/n$. Variations in $w$ span $D_1\operatorname{col}W^\top$. Variations in $W$ have the form

\[
\delta(\nabla_a f_d)
=\frac1nD_1\left[\delta W^\top t+
W^\top\operatorname{diag}\bigl(w\odot\tanh''z\bigr)\delta W u\right].
\tag{12}
\]

The first term $\delta W^\top t$ ranges over all of $\mathbb R^n$, since $t\ne0$. The second term lies in $\operatorname{col}W^\top$ and can be canceled using a readout variation. Since $D_1$ is invertible, the combined derivative is surjective. Its nonzero multiplier in $B$ is $-2y_d$, proving the rank claim.

For an axis case, say $Ax_2=0$, take $a=Ax_2$ while holding $Ax_1$ fixed. At $a=0$, $f_2=0$ is odd in $a$, $f_1=y_1$, and stationarity gives $W^\top w=0$. The same block form (11) holds. Here

\[
\nabla_a f_2=W^\top w/n,\qquad
\delta_W(\nabla_a f_2)=\delta W^\top w/n,
\]

which is surjective because $w\ne0$. The other axis is identical after interchanging the samples.

Finally, a symmetric block matrix (11) with $B$ of row rank $n$ has at least $n$ negative eigenvalues. Choose a linear right inverse $R$ of $B$. On the $n$-dimensional subspace consisting of vectors $(a,-\varepsilon Ra)$, its quadratic form is

\[
-2\varepsilon\|a\|^2+\varepsilon^2(Ra)^\top C(Ra),
\]

which is strictly negative for every $a\ne0$ when $\varepsilon>0$ is sufficiently small. Invertible coordinate changes and the positive mobility matrix preserve the number of negative directions by congruence.

### 5.3 Avoidance from the zero-readout slice

The following version of the flow center-stable manifold theorem is used: near an equilibrium of a $C^2$ vector field on $\mathbb R^N$ with $k$ unstable eigenvalues, counted with multiplicity, there is a $C^1$ locally flow-invariant embedded manifold of dimension $N-k$ containing every forward trajectory that stays in a sufficiently small neighborhood. This includes zero eigenvalues among the center-stable directions. The cutoff and Perron construction, including containment of forward bounded orbits and flow invariance, is given in [Eldering, Section 3.1](https://www.jaapeldering.nl/files/lect-ICMC-invarmflds.pdf).

In the present problem $N=nd+n^2+n$. The vector field is analytic; its linearization at a critical point is minus a positive mobility matrix times the Hessian, and is similar to a symmetric matrix. Section 5.2 therefore supplies at least $n$ unstable eigenvalues. Each local center-stable manifold has dimension at most $N-n$.

Let $M_0=\{w=0\}$, an $(N-n)$-dimensional linear subspace. At any point of $M_0$ with $Hy\ne0$, the flow vector is

\[
V=(0,0,Hy),
\]

because $m=2$. It is nonzero and not tangent to $M_0$.

Every finite-time inverse image of a local center-stable manifold is again a $C^1$ manifold of dimension at most $N-n$, on the open set where the inverse flow is defined. Its tangent space contains $V$, by local flow invariance. At an intersection point with $M_0$ and $Hy\ne0$, its tangent space consequently cannot contain $T M_0$: inclusion would force equality of dimensions and tangent spaces, contradicting $V\notin T M_0$.

This makes each intersection null for Lebesgue measure on $M_0$. In detail, express the inverse-image manifold locally as the zero set of a $C^1$ submersion. Its derivative restricted to $M_0$ is nonzero. At least one scalar component therefore has a nonzero derivative on $M_0$; the implicit-function theorem contains the intersection in a hypersurface of $M_0$. Countably many coordinate charts suffice.

To cover all finite bad limits, cover their critical set by their trapping neighborhoods and take a countable subcover, using the second-countability of Euclidean space. A trajectory converging to any covered critical point eventually remains inside one selected neighborhood. At some integer time it therefore belongs to the corresponding center-stable manifold. Taking the countable union over neighborhoods and integer times proves that convergence to a finite bad critical point has zero Lebesgue measure on the part of $M_0$ where $Hy\ne0$.

Finally the Gaussian law on $(A,W)$ has a density on $M_0$. Conditional on an invertible $W$, which occurs almost surely, the matrix $AX\in\mathbb R^{n\times2}$ has a density because $X$ has rank two. Entrywise tanh, multiplication by $W$, and entrywise tanh again are diffeomorphisms onto open images, so $H$ has a density. For fixed $y\ne0$, the condition $Hy=0$ is a proper linear subspace and thus null. Almost surely the initial loss strictly decreases, excluding critical limits at loss $\mathcal L_0$. This proves (7).

### 5.4 Why positive-loss failure now requires escape to infinity

A real-analytic gradient flow either has parameter norm tending to infinity or converges to a finite point, provided it is globally defined. The slightly more general angle-condition statement and proof are [Absil, Mahony, and Andrews, Theorem 2.2](https://sites.uclouvain.be/absil/Publi/Convergence_SIOPT/13-60526.pdf). Their published correction concerns the separate discrete-time Proposition 3.3, which is not used here.

To check the assumptions, let $D$ be the constant positive diagonal mobility matrix and set $\eta=D^{-1/2}\theta$. Then

\[
\dot\eta=-\nabla_\eta\mathcal L(D^{1/2}\eta).
\]

The transformed loss is real analytic, the angle condition holds with constant one, zero loss derivative implies zero velocity, and Section 1 proves global existence. Hence a trajectory not satisfying $\|\theta(t)\|\to\infty$ has a finite limit, necessarily critical. Combining this with (7) proves (8).

The remaining two-input question is now specifically whether the canonical random trajectory can escape to infinity while retaining positive limiting loss. Neither the readout identity (3) nor the finite critical classification (10) settles that question. A diverging trajectory has no finite critical point to which (9)--(12) can be applied without additional estimates.
