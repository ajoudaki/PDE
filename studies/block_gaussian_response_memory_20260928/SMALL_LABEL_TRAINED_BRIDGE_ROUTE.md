# Small-label route: all-time control, the cubic Gaussian response, and the remaining trained bridge

Status: **the requested fixed-label $k^{-\beta}$ theorem is not proved**. This route proves an all-time small-label bound with a block-size-independent threshold, an $O(k^{-1})$ weak-error identity for the first nonlinear Gaussian response primitive, and, under ordinary zero-label differentiability, an $O(k^{-1})$ comparison of the complete cubic coefficient. It does not turn these into an untruncated trained comparison. The exact unresolved observable is identified in Section 7.

Scientific inputs were only the supervisor's assignment and `docs/notation.qmd`. No other study, experimental output, external source, or other agent's result was used. The required `solve-math-rigorously` and `investigate-conjectures` skills, including the latter's research-contract and adversarial-audit references, were read. This is a scoped theoretical route, not an independent review.

## 1. Contract and notation

Work first at $L=2$, with the precise globally trained architecture in the assignment. First-layer weights are independent standard Gaussians, as in the canonical convention. For a block of size $k$, let $A\in\mathbb R^{k\times k}$ have independent $N(0,1/k)$ entries. Its first-layer rows are independent of $A$. The block population is the limit $B\to\infty$ with $k$ fixed; every entry of the learned second matrix, including initially zero off-block entries, is trained.

Write $q_i(t,x)=z_i^{(1)}(t,x)$, $Z_j(t,x)=z_j^{(2)}(t,x)$, $H_i(t,x)=\tanh q_i(t,x)$, $S_j(t,x)=\tanh Z_j(t,x)$, and $w_j(t)$ for the readout. Expectations below are over one random block. Every coordinate average is displayed with its $1/k$ factor. Put

\[
d_j(t,x)=w_j(t)\tanh'(Z_j(t,x)),\qquad
G_{xa}=x^Tx_a/d,\qquad X_x=\|x\|/\sqrt d,\quad X=\max_a X_{x_a}.
\]

The labels have $Y=\|y\|_2/\sqrt m\le Y_*$, where $Y_*>0$ must be independent of $k,B,t$. The desired comparison is for this **fixed positive** label scale, uniformly for all physical time. The limit order is $B\to\infty$, then $k\to\infty$. Neither a frozen-feature model nor a finite label Taylor polynomial answers that question.

The assignment does not specify test-law moments. The training results and Gaussian primitive below need none. The explicit $L^2(\mu)$ remainder estimates in Sections 3–4 use
\[
\int X_x^2\,\mu(dx)<\infty.
\tag{1.1}
\]
They also give pointwise bounds without (1.1). This moment assumption is stated rather than silently added to the target.

All assertions about the block-population trajectory are conditional on a sufficiently regular solution of (2.2)–(2.3) obtained in the stated $B\to\infty$ limit. The finite-width identities and a priori estimates do not require that passage. This note does not prove block-population well-posedness or convergence as $B\to\infty$. Dense-flow identification and label differentiation are also stated where used. No quantitative trained Gaussian correlation estimate is assumed.

## 2. Exact global-training representation and kernel

At finite width $n=Bk$, write the second matrix as $W^{(2)}(t)=A_n+T_n(t)$, with $A_n$ the aligned block diagonal initialization. Its exact trained increment is
\[
T_n(t)=-\frac2m\sum_b\int_0^t r_b(s)
\frac{d_b(s)H_b(s)^T}{n}\,ds.
\tag{2.1}
\]
Thus this representation does not freeze off-block weights. In the block population the corresponding identities are
\[
\begin{split}
Z_j(t,x)&=(AH(t,x))_j
-\frac2m\sum_b\int_0^t r_b(s)d_j(s,x_b)
C^{11}_k(s,b;t,x)\,ds,\\
(W^{(2)}(t)^*d(t,x))_i
&=(A^Td(t,x))_i
-\frac2m\sum_b\int_0^t r_b(s)H_i(s,x_b)
C^{dd}_k(s,b;t,x)\,ds,
\end{split}
\tag{2.2}
\]
where
\[
C^{11}_k(s,b;t,x)=\mathbb E\frac1k\sum_iH_i(s,x_b)H_i(t,x),\qquad
C^{dd}_k(s,b;t,x)=\mathbb E\frac1k\sum_jd_j(s,x_b)d_j(t,x).
\]
Both directions use the same $A$. The backward coordinate is
\[
\delta_i^{(1)}(t,x)=\tanh'(q_i(t,x))
(W^{(2)}(t)^*d(t,x))_i.
\]
The remaining equations are
\[
\dot w_j=-\frac2m\sum_a r_aS_j(t,x_a),\qquad
\dot q_i(t,x)=-\frac2m\sum_a r_aG_{xa}\delta_i^{(1)}(t,x_a).
\tag{2.3}
\]

Differentiating $f_k(t,x)=\mathbb E k^{-1}\sum_jw_jS_j(t,x)$ gives the exact kernel equation
\[
\dot f_k(t,x)=-\frac2m\sum_a K_k(t;x,a)r_a(t),
\tag{2.4}
\]
with
\[
\begin{split}
K_k(t;x,a)={}&Q_k(t;x,a)
+C^{11}_k(t,x;t,a)C^{dd}_k(t,x;t,a)\\
&+G_{xa}\mathbb E\frac1k\sum_i
\delta_i^{(1)}(t,x)\delta_i^{(1)}(t,x_a),\\
Q_k(t;x,a)={}&\mathbb E\frac1k\sum_jS_j(t,x)S_j(t,x_a).
\end{split}
\tag{2.5}
\]
For training arguments this is a sum of positive semidefinite Gram matrices: the middle term is the Gram matrix of the tensor products $H_a\otimes d_a$, and the last is the Gram matrix of $x_a/\sqrt d\otimes\delta_a^{(1)}$. In particular $K_k(t)\succeq Q_k(t)$.

Equation (2.2) follows directly from (2.1) by applying the rank-one increment to a vector and to its adjoint; no independence between trained forward and backward quantities was used. Passing the displayed empirical pairings to expectations is the only population-limit step in this representation.

## 3. An all-time small-label estimate, uniform in block size

Define the residual activity
\[
R(t)=\frac2m\sum_a\int_0^t|r_a(s)|\,ds.
\tag{3.1}
\]
Let $M=\|A\|_{\rm op}$. Its moments of every fixed order are bounded uniformly in $k\ge1$. Here is an elementary bound sufficient below. A $1/4$-net of the Euclidean unit sphere can be chosen with at most $9^k$ points, by disjoint-ball volume comparison. Approximating both unit vectors in $v^TAu$ by net points shows
\[
\|A\|_{\rm op}\le2\max_{u,v\text{ in the nets}}|v^TAu|.
\]
Every fixed $v^TAu$ is $N(0,1/k)$, so the Gaussian exponential bound and a union bound give
\[
\mathbb P(M>s)\le 2\,9^{2k}e^{-ks^2/8}.
\]
For $s\ge9$, this is at most $2e^{-ks^2/16}\le2e^{-s^2/16}$. Integrating $p s^{p-1}\mathbb P(M>s)$ gives
\[
\sup_k\mathbb E M^p<\infty
\quad\text{for each fixed }p<\infty.
\tag{3.2}
\]

Since $|\tanh|,|\tanh'|\le1$, (2.3) implies pointwise
\[
|w_j(t)|\le R(t),\qquad |d_j(t,x)|\le R(t).
\tag{3.3}
\]
The trained forward term in (2.2) has every coordinate bounded by
\[
\int_0^tR(s)\,dR(s)=R(t)^2/2.
\tag{3.4}
\]
The trained adjoint term has every coordinate bounded by
\[
R(t)\int_0^tR(s)\,dR(s)=R(t)^3/2.
\tag{3.5}
\]
Consequently, for each individual block,
\[
\frac{\|\delta^{(1)}(t,x)\|_2}{\sqrt k}
\le MR(t)+R(t)^3/2.
\tag{3.6}
\]
Since $|G_{xa}|\le X_xX$, integration of (2.3) gives
\[
\frac{\|q(t,x)-q(0,x)\|_2}{\sqrt k}
\le X_xX\left(\frac{MR(t)^2}{2}+\frac{R(t)^4}{8}\right).
\tag{3.7}
\]
The second-layer forward identity, (3.4), and the 1-Lipschitz property of tanh now imply
\[
\frac{\|Z(t,x)-Z(0,x)\|_2}{\sqrt k}
\le X_xX\left(\frac{M^2R(t)^2}{2}+\frac{MR(t)^4}{8}\right)+\frac{R(t)^2}{2}.
\tag{3.8}
\]
Taking the $L^2$ norm over blocks yields
\[
\left(\mathbb E\frac1k\|S(t,x)-S(0,x)\|_2^2\right)^{1/2}
\le \Theta_x(R(t)),
\tag{3.9}
\]
where, with constants $M_p=\sup_k\mathbb E M^p$,
\[
\Theta_x(R)=\left(\frac{X_xX\sqrt{M_4}}2+\frac12\right)R^2
+\frac{X_xX\sqrt{M_2}}8R^4.
\]
This estimate uses block moments, not the largest block norm; the latter diverges as $B\to\infty$ at fixed $k$.

Suppose for $k\ge k_0$ the initial training feature Gram obeys
\[
\lambda_{\min}(Q_k(0)/m)\ge\lambda_0>0.
\tag{3.10}
\]
Section 5 proves initial $O(k^{-1})$ convergence and hence (3.10) from the specified positive limiting gap. Since $|S|\le1$, Cauchy–Schwarz gives
\[
|Q_k(t;a,b)-Q_k(0;a,b)|\le\Theta_{x_a}(R(t))+\Theta_{x_b}(R(t)).
\]
For an $m\times m$ matrix, its operator norm divided by $m$ is at most its largest absolute entry. Choose $R_*\le1$, independent of $k$, so that
\[
2\max_a\Theta_{x_a}(R_*)\le\lambda_0/2.
\]
As long as $R(t)\le R_*$, the training kernel has $K_k(t)/m\succeq(\lambda_0/2)I$. Thus (2.4) gives
\[
\frac{d}{dt}\frac{\|r(t)\|_2^2}{m}
=-\frac4{m^2}r(t)^TK_k(t)r(t)
\le-2\lambda_0\frac{\|r(t)\|_2^2}{m}.
\]
Consequently
\[
\frac{\|r(t)\|_2}{\sqrt m}\le Ye^{-\lambda_0t},\qquad
R(t)\le\frac{2Y}{\lambda_0}.
\tag{3.11}
\]
For $Y\le Y_*:=\lambda_0R_*/4$, the right side is at most $R_*/2$. A first-exit argument closes the bootstrap for all time. This establishes a label threshold and decay constants independent of $k,B,t$.

The same estimates hold at finite $B$, replacing the moments of $M$ by empirical block moments. At fixed $k$ those moments converge to their expectations. For dense width $n$, use one $n\times n$ Gaussian block: the net estimate gives $\mathbb P(\|A_n\|_{\rm op}>9)\to0$, and the initial Gram converges in probability to its Gaussian covariance formula. The inequalities therefore pass to the canonical dense limit whenever it is identified as the regular finite-width limit. This passage uses no trained Gaussian weak-error rate.

## 4. What all-time stability alone proves—and does not prove

The terms in (2.5) obey, for $R\le1$,
\[
|K_k(t;x,a)-Q_k(0;x,a)|\le C(1+X_xX)R(t)^2,
\tag{4.1}
\]
with $C$ independent of $k,t$. For completeness, the readout Gram term is bounded by (3.9); the second-layer term is at most $R^2$; and the absolute first-layer term is at most
\[
|G_{xa}|\,\mathbb E(MR+R^3/2)^2
\le|G_{xa}|(M_2R^2+M_1R^4+R^6/4).
\]
These are exactly the three contributions in (4.1).

Let $r_k^{\rm lin}(t)=-e^{-2Q_k(0)t/m}y$, and define the frozen-feature predictor by
\[
\dot f_k^{\rm lin}(t,x)=-\frac2m\sum_aQ_k(0;x,a)r_{k,a}^{\rm lin}(t),\qquad f_k^{\rm lin}(0,x)=0.
\]
For $e=r_k-r_k^{\rm lin}$, variation of constants gives
\[
e(t)=-\frac2m\int_0^t e^{-2Q_k(0)(t-s)/m}
[K_k(s)-Q_k(0)]r_k(s)\,ds.
\]
Using (3.10), (3.11), and (4.1),
\[
\frac{\|e(t)\|_2}{\sqrt m}
\le\frac{2C}{\lambda_0}R(\infty)^2Y e^{-\lambda_0t},\qquad
\int_0^\infty\frac{\|e(t)\|_2}{\sqrt m}\,dt
\le\frac{2C}{\lambda_0^2}R(\infty)^2Y.
\tag{4.2}
\]
Integrating the test equation and using $|Q_k(0;x,a)|\le1$ then proves
\[
\sup_{t\ge0}|f_k(t,x)-f_k^{\rm lin}(t,x)|
\le C(1+X_xX)Y^3.
\tag{4.3}
\]
Under (1.1), the same holds in $L^2(\mu)$.

Initial-kernel $O(k^{-1})$ convergence, combined with the same stable linear comparison, gives
\[
\sup_{t\ge0}\|f_k^{\rm lin}(t)-f_\infty^{\rm lin}(t)\|_{L^2(\mu)}\le CY/k.
\]
Thus this argument yields only
\[
\sup_{t\ge0}\|f_k(t)-f_\infty(t)\|_{L^2(\mu)}
\le C(Y/k+Y^3).
\tag{4.4}
\]
This is a genuine nonlinear all-time estimate, but its $Y^3$ term stays fixed as $k\to\infty$. It is **not** the requested bridge.

There is no all-time propagation obstruction once an appropriate kernel source estimate is proved. Indeed, if two training kernels have $K(t)/m\succeq\lambda I$, the fundamental solution of $\dot u=-(2/m)K(t)u$ contracts by $e^{-2\lambda(t-s)}$: differentiate $\|u\|_2^2$ to obtain this bound. Applying it to the difference equation shows that a weighted-integrable train/test kernel defect of order $k^{-\beta}$ produces an all-time output defect of the same order. The missing estimate concerns production of that kernel defect.

## 5. Exact Gaussian response primitive and its $k^{-1}$ weak error

The following calculation is not an independence approximation.

Let $H_1,\ldots,H_k\in[-1,1]^p$ be iid row feature vectors, with fixed finite $p$, independent of $A$. Put $Z_j=\sum_iA_{ji}H_i$. Let $D_i=D(H_i)$ with $|D_i|\le D_0$, and let $U,V:\mathbb R^p\to\mathbb R$ have bounded derivatives through order five. Set
\[
C_k=\frac1k\sum_iH_iH_i^T,\quad
\overline D_k=\frac1k\sum_iD_i,\quad
S_k=\frac1k\sum_iD_iH_iH_i^T.
\]
Define
\[
\mathcal R_k(D;U,V)=\mathbb E\frac1k\sum_iD_i
\left(\sum_jA_{ji}U(Z_j)\right)
\left(\sum_\ell A_{\ell i}V(Z_\ell)\right).
\tag{5.1}
\]
For a covariance $C\succeq0$, write $\mathbb E_C$ for Gaussian expectation with law $N(0,C)$. Let $\widehat{\mathcal R}_k$ denote the random coordinate average whose expectation defines (5.1). Conditional on $H_1,\ldots,H_k$,
\[
\begin{split}
\mathbb E[\widehat{\mathcal R}_k\mid H]={}&
\overline D_k\,\mathbb E_{C_k}[UV]\\
&+(1-k^{-1})\,S_k:
\bigl(\mathbb E_{C_k}\nabla U\otimes\mathbb E_{C_k}\nabla V\bigr)\\
&+k^{-1}S_k:\mathbb E_{C_k}\nabla^2(UV).
\end{split}
\tag{5.2}
\]

**Proof.** Gaussian integration by parts in the single scalar $A_{ji}$ gives
\[
\mathbb E[A_{ji}U(Z_j)\mid H]
=\frac1kH_i^T\mathbb E_{C_k}\nabla U.
\]
Applying it twice gives
\[
\mathbb E[A_{ji}^2F(Z_j)\mid H]
=\frac1k\mathbb E_{C_k}F
+\frac1{k^2}H_i^T\mathbb E_{C_k}\nabla^2F\,H_i.
\]
These follow by integrating the derivative of the $N(0,1/k)$ density; bounded derivatives make the boundary terms vanish. For $j\ne\ell$, rows $j,\ell$ are conditionally independent, so use the product of the first identity. For $j=\ell$, use the second identity with $F=UV$. Summing the $k(k-1)$ off-diagonal row pairs and the $k$ diagonal pairs, with the outer $k^{-1}\sum_iD_i$, gives (5.2). This argument does not invert $C_k$ and works when it is singular. $\square$

Let
\[
C=\mathbb E HH^T,\qquad \overline D=\mathbb E D(H),\qquad
S=\mathbb E[D(H)HH^T].
\]
Then
\[
\mathcal R_\infty(D;U,V)=
\overline D\,\mathbb E_C[UV]
+S:\bigl(\mathbb E_C\nabla U\otimes\mathbb E_C\nabla V\bigr)
\tag{5.3}
\]
obeys
\[
|\mathcal R_k(D;U,V)-\mathcal R_\infty(D;U,V)|\le C_{p,D_0,U,V}/k.
\tag{5.4}
\]

Here are the details of the weak-error step. If $g$ has bounded derivatives through order four, its Gaussian covariance functional $\Psi_g(C)=\mathbb E_Cg$ has, along every positive semidefinite line segment, directional derivatives
\[
D\Psi_g(C)[E]=\frac12\sum_{ab}E_{ab}\mathbb E_C\partial_{ab}g,
\quad
D^2\Psi_g(C)[E,F]=\frac14\sum_{abcd}E_{ab}F_{cd}\mathbb E_C\partial_{abcd}g.
\tag{5.5}
\]
For positive definite covariance, differentiate the Gaussian density (whose covariance derivative equals one half of its spatial second derivative) and integrate by parts twice. Adding $\epsilon I$, using the displayed derivative bounds, and sending $\epsilon\downarrow0$ proves the formula on semidefinite segments. Thus the second derivative is bounded without any lower covariance eigenvalue.

The leading two terms in (5.2) are a smooth function $F(C_k,\overline D_k,S_k)$ with bounded second derivative on the convex hull of their possible values. For the gradient expectations this uses derivatives of $U,V$ through order five. Each entry of $(C_k,\overline D_k,S_k)$ is an empirical average of bounded iid variables. The first-order Taylor term about its mean has expectation zero, while the sum of entry variances is $O(1/k)$. Taylor's integral remainder therefore gives
\[
|\mathbb EF(C_k,\overline D_k,S_k)-F(C,\overline D,S)|\le C/k.
\]
The explicit $1/k$ terms in (5.2) are bounded by $C/k$. This proves (5.4).

Taking $g(z)=\tanh z_a\tanh z_b$ in the same empirical-covariance argument proves
\[
Q_k(0;x,a)=\mathbb E\Psi_g(C_k),\qquad
|Q_k(0;x,a)-\Psi_g(C)|\le C/k.
\tag{5.6}
\]
The bound is uniform in $x$ because all entries of the first-layer feature vector remain bounded by one. In particular the limiting training Gram gap implies (3.10) for sufficiently large $k$.

The second term of (5.3) is an order-one Gaussian transpose response. Dropping it by treating $A$ as independent of its own forward features changes the limiting cubic dynamics.

## 6. The complete cubic coefficient uses only the primitive above

Scale the labels as $y=\theta\widehat y$, with $\|\widehat y\|_2/\sqrt m=1$. The symmetry $(\theta,w,q,Z)\mapsto(-\theta,-w,q,Z)$ makes $f$ odd and both hidden preactivations even in $\theta$. At any fixed finite time, ordinary parameter differentiability gives coefficients
\[
r=\theta\rho+\theta^3\eta+o(\theta^3),\quad
w=\theta v+O(\theta^3),\quad
q=q^0+\theta^2q^{[2]}+o(\theta^2),\quad
Z=Z^0+\theta^2Z^{[2]}+o(\theta^2).
\tag{6.1}
\]
No uniform Taylor remainder in $k,t$ is asserted here.

Let $H_i(x)=\tanh q_i^0(x)$, $S_j(x)=\tanh Z_j^0(x)$, and
\[
C^{11}(b,x)=\mathbb E[H_i(x_b)H_i(x)].
\]
Then
\[
\rho(t)=-e^{-2Q_k(0)t/m}\widehat y,\quad
c_b(t)=-\frac2m\int_0^t\rho_b(s)\,ds,\quad
v_j(t)=\sum_bc_b(t)S_j(x_b).
\tag{6.2}
\]
Define
\[
J_{bc}(t)=-\frac2m\int_0^t\rho_b(s)c_c(s)\,ds,
\quad u_{bc}(z)=\tanh z_c\,\tanh' z_b,
\quad D_{xb,i}=\tanh'(q_i^0(x))\tanh'(q_i^0(x_b)).
\]
Differentiating (2.2)–(2.3) at $\theta=0$ gives exactly
\[
q_i^{[2]}(t,x)=\sum_{bc}J_{bc}(t)G_{xb}
\tanh'(q_i^0(x_b))(A^Tu_{bc}(Z^0))_i,
\]
and
\[
Z^{[2]}(t,x)=\sum_{bc}J_{bc}(t)
\left[G_{xb}A D_{xb}A^Tu_{bc}(Z^0)
+C^{11}(b,x)u_{bc}(Z^0)\right].
\tag{6.3}
\]
The second term is precisely the contribution from globally learned second-layer entries. The first is the first-layer feature-motion response.

Write $K_k=Q_k(0)+\theta^2K_k^{[2]}+o(\theta^2)$. The three parts of $K_k^{[2]}(t;x,a)$ are:

1. The coefficient of the readout feature Gram,
   \[
   \mathbb E\frac1k\sum_j\left[
   \tanh'(Z_j^0(x))Z_j^{[2]}(t,x)S_j(x_a)
   +S_j(x)\tanh'(Z_j^0(x_a))Z_j^{[2]}(t,x_a)\right].
   \tag{6.4}
   \]
2. The second-layer tangent term,
   \[
   C^{11}(x,a)\,\mathbb E\frac1k\sum_j
   v_j(t)^2\tanh'(Z_j^0(x))\tanh'(Z_j^0(x_a)).
   \tag{6.5}
   \]
3. The first-layer tangent term,
   \[
   G_{xa}\,\mathcal R_k\left(D_{xa};
   v(t,\cdot)\tanh'(\cdot_x),
   v(t,\cdot)\tanh'(\cdot_a)\right),
   \tag{6.6}
   \]
   where $v(t,z)=\sum_bc_b(t)\tanh z_b$.

In (6.4), substitute (6.3). Every $ADA^T$ term becomes (5.1), with $U(z)=\tanh'(z_x)\tanh(z_a)$ or the interchanged version and $V=u_{bc}$. Every other term is an ordinary Gaussian covariance functional. Since $\tanh'(q)=1-\tanh^2(q)$, each $D_{xb,i}$ is a bounded function of the iid first-layer feature row, exactly as required in Section 5.

It follows from (5.4)–(5.6) that the complete coefficient kernel has an $O(k^{-1})$ comparison, uniformly in time. To verify time uniformity rather than assume it: the initial gap gives exponential decay of $\rho$, hence uniform boundedness of $c,J$. Duhamel's formula for the difference of the two initial-kernel semigroups gives an $O(k^{-1})$ bound for $\rho_k-\rho_\infty$ in both $L^\infty_t$ and $L^1_t$. Integrating (6.2) then gives $c_k-c_\infty=O(k^{-1})$; integrating the defining product for $J$ gives the same for $J_k-J_\infty$. Substituting these estimates into the finite sums (6.4)–(6.6) proves
\[
\sup_{t\ge0}|K_k^{[2]}(t;x,a)-K_\infty^{[2]}(t;x,a)|
\le C(1+X_xX)/k.
\tag{6.7}
\]

The cubic training coefficient and its test prediction obey stable linear equations
\[
\dot\eta=-\frac2mQ_k(0)\eta-\frac2mK_k^{[2]}(t)\rho,
\quad\eta(0)=0,
\tag{6.8}
\]
\[
\dot f_k^{[3]}(t,x)=-\frac2m\sum_a
\left[Q_k(0;x,a)\eta_a(t)+K_k^{[2]}(t;x,a)\rho_a(t)\right],
\quad f_k^{[3]}(0,x)=0.
\tag{6.9}
\]
Their forcing is integrable because $K_k^{[2]}$ is bounded and $\rho$ decays. Apply the convolution bound used in (4.2), first to (6.8) and then to the difference of its $k$ and infinite equations. It gives an $O(k^{-1})$ bound for $\eta_k-\eta_\infty$ in $L^1_t$. Integrating (6.9) proves
\[
\sup_{t\ge0}|f_k^{[3]}(t,x)-f_\infty^{[3]}(t,x)|
\le C(1+X_xX)/k.
\tag{6.10}
\]

These equations rigorously define the cubic coefficient limit. Identifying it with one sixth of the third label derivative of an independently defined canonical dense population flow additionally requires compatibility of that flow with differentiation at zero label. That is an ordinary zero-label regularity/identification condition, not a trained quantitative Gaussian-correlation estimate; it has been made explicit rather than inferred merely from existence. The primitive theorem (5.4) does not require this identification.

## 7. Exact unresolved trained observable

At nonzero labels let
\[
D_i^t(x,a)=\tanh'(q_i(t,x))\tanh'(q_i(t,x_a)),\qquad
u_j^t=d_j(t,x),\qquad v_\ell^t=d_\ell(t,x_a).
\]
The $A/A^T$ part of the trained first-layer kernel is
\[
\mathcal R_k^t(x,a)=\frac1k\sum_{i,j,\ell}
\mathbb E\left[A_{ji}A_{\ell i}D_i^t(x,a)u_j^tv_\ell^t\right].
\tag{7.1}
\]
With sufficient ordinary derivative integrability, Gaussian integration by parts gives the exact identity
\[
\mathcal R_k^t(x,a)=
\frac1{k^2}\sum_{i,j}\mathbb E[D_i^tu_j^tv_j^t]
+\frac1{k^3}\sum_{i,j,\ell}
\mathbb E\,\partial_{A_{ji}}\partial_{A_{\ell i}}
\left(D_i^tu_j^tv_\ell^t\right).
\tag{7.2}
\]
For complete precision without an integrability assumption, multiply the product by a smooth compactly supported cutoff in the Gaussian coordinates: (7.2), with the cutoff inside both terms and inside the differentiated product, is then exact. Removing the cutoff requires the displayed derivative integrability. No $k$-rate follows from that ordinary integrability.

The derivatives in (7.2) act on the entire causal trajectory driven by that block's $A$; the deterministic population correlation fields are held fixed as the other arguments of its solution map. For the frozen-feature inputs of Section 5, the first-layer factors are independent of $A$ and a row $j$ depends only on its own Gaussian row. Then (7.2) reduces to the finite list in (5.2); the leading zero-label response has precisely this form. For the untruncated trained fields at nonzero labels neither simplification is true.

For example, the second-derivative product contains the exact term
\[
\mathcal M_k(t;x,a)=\frac1{k^3}\sum_{i,j,\ell}
\mathbb E\left[
(\partial_{A_{ji}}D_i^t(x,a))\,
u_j^t\,(\partial_{A_{\ell i}}v_\ell^t)
\right].
\tag{7.3}
\]
It vanishes in the untrained primitive because $D_i$ then does not depend on $A$. Under the label expansion, $\partial_A D_i^t=O(\theta^2)$, $u_j^t=O(\theta)$, and $\partial_Av_\ell^t=O(\theta)$, so this is a fourth-order kernel contribution and a fifth-order output contribution. The $k^3$ summands match the $k^{-3}$ prefactor; small-label power counting alone gives no $k$-decay. There are also derivative-of-$D$ terms of second order, cross-row response products, and second derivatives of $u,v$. They must be treated together or with proved cancellations.

One sufficient missing source estimate is a uniform $O(k^{-1})$ weak comparison for the aggregate trained response
\[
\Gamma_k(t;x,a)=\frac1{k^3}\sum_{i,j,\ell}
\mathbb E\,\partial_{A_{ji}}\partial_{A_{\ell i}}
\left(D_i^t(x,a)d_j(t,x)d_\ell(t,x_a)\right),
\tag{7.4}
\]
together with the first term of (7.2), the forward-feature terms, and the terms involving the trained increment in (2.2). A residual-weighted time-integral estimate suffices; the stronger pointwise-in-time version is not essential. The comparison must be for the fully self-consistent trajectories at the same fixed labels, or be proved first for common causal forcing and then closed by a small-activity contraction.

The particularly concrete next obstruction after the cubic calculation is (7.3). A rate estimate for its difference from the corresponding dense response, or a demonstrated cancellation with the other terms of (7.4), is absent. It cannot be replaced by a norm bound of order $Y^4$, since that would leave a fixed $Y^5$ output discrepancy. Nor is an $O(k^{-1})$ estimate for each fixed label coefficient enough without uniform control of the untruncated remainder.

## 8. Why a convergent label expansion is not supplied by smooth tanh dynamics

There is a simple exact obstruction to the inference “analytic tanh plus Gaussian moments implies a positive uniform Taylor radius.” Let $G\sim N(0,1)$ and
\[
F(s)=\mathbb E\tanh^2(sG).
\]
Every real derivative of $\tanh^2$ is bounded: successive differentiation produces a polynomial in $\tanh$, using $\tanh'=1-\tanh^2$. For each fixed derivative order, domination by a constant times $|G|^q$ therefore justifies differentiation under expectation at $s=0$. If
\[
\tanh^2z=\sum_{q\ge0}a_qz^{2q}
\]
near zero, the Taylor coefficients of $F$ are $a_q\mathbb EG^{2q}$.

The complex function $\tanh^2z$ has nearest nonremovable poles at $z=\pm i\pi/2$, because $\cosh z=0$ there and $\sinh z\ne0$. Its Taylor radius is therefore $\pi/2$; equivalently,
\[
\limsup_{q\to\infty}|a_q|^{1/(2q)}=2/\pi.
\]
Gaussian integration by parts gives $\mathbb EG^{2q}=(2q-1)!!$. At least $\lfloor q/2\rfloor$ factors in this product are at least $q$, so
\[
(\mathbb EG^{2q})^{1/(2q)}\ge q^{\lfloor q/2\rfloor/(2q)}\longrightarrow\infty.
\]
On a subsequence the roots $|a_q|^{1/(2q)}$ are bounded below by a positive constant. Hence the Taylor series of $F$ has radius zero. $F$ is smooth on the real line but is not represented by its Taylor series on any positive interval around zero.

This is not a counterexample to the requested block-to-dense theorem; it is a counterexample to an attempted justification for summing the label expansion. It also explains why estimates growing with Gaussian high moments must be examined before declaring a response series convergent.

Truncating to $\|A\|_{\rm op}\le M_0$ has exponentially small discarded block probability in $k$, by Section 3, and may be useful. It does not by itself give the missing analytic argument: an operator bound controls coordinate RMS, whereas a common complex strip for coordinatewise tanh requires coordinatewise control of the imaginary perturbations. Such a conversion can cost $\sqrt k$. A proposed real small-activity fixed-point contraction would still need the weak Gaussian source comparison in (7.4). Such a full path-space contraction is not proved in this note; the kernel-level propagation estimate in Section 4 is proved.

## 9. Claim accounting and deep extension

| Claim | Status |
|---|---|
| Exact globally trained $L=2$ rank-one/Volterra identities and kernel | Proved algebraically; population passage as stated |
| Uniform small-label threshold, residual decay, integrated residual bound | Proved for block populations; dense inheritance under the stated limit identification |
| Initial feature-kernel $O(k^{-1})$ error without covariance inverses | Proved |
| Gaussian $A/A^T$ cubic response primitive including its response term | Proved, with $O(k^{-1})$ weak error |
| Full cubic coefficient comparison uniformly in time | Proved for the coefficient equations; dense derivative identification stated separately |
| Fixed-label, untruncated $O(k^{-\beta})$, $\beta>2/3$ | Open |
| Conjecture falsified | No |

For $L>2$, each Gaussian hidden matrix and its transpose creates additional response contractions, and first-layer feature changes propagate through several trained layers. The bounded-activation activity estimates suggest finite-depth bounds using fixed moments of products of Gaussian operator norms, but this note does not prove those bounds or a deep comparison. In particular the $L=2$ primitive cannot simply be iterated with “independent Gaussian layers”: trained forward and backward fields depend on each matrix in both directions. No deep extension is claimed.

The surviving major gap is a quantitative weak comparison for the nonlinear trained Gaussian response aggregate (7.4), already visible in the new fifth-order output contribution (7.3). All-time residual control and the exact cubic calculation remove two potential ambiguities but do not close that gap.
