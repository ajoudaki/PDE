# A gap-free second forward response step

2026-10-07. A bounded extension of GAP_FREE_RESPONSE_STEP.md: one independent forward batch, one reverse batch, and one further forward batch at the same initialized Gaussian interface. This note proves a normalized mean-square, root-width coupling for this three-query-block program. It does not prove a growing-history or all-time theorem.

Scientific inputs: the supervisor's assignment, this route's GAP_FREE_RESPONSE_STEP.md, and the previously read RESPONSE_GAUSSIAN_CLOSURE.md and FIXED_HISTORY_RATE.md with their audits. No outside study, literature, experiment, or further query round was used.

There are two results. The first conditions on an arbitrary independent input matrix $H$ and uses its empirical design law. The second, under additional uniform derivative regularity and bounded iid input rows, compares to the fixed population response law. Neither result uses a positive history-Gram eigenvalue lower bound. Exact dependent queries remain allowed.

## 1. Program and its inverse-free target

Let $G\in\mathbb R^{n\times n}$ have independent $N(0,1/n)$ entries. Let $H\in\mathbb R^{n\times k}$ be independent of $G$. First condition on $H$, which may be deterministic and need not have iid rows. If $H$ is a function of a larger independent input/root seed, one may condition on that complete seed throughout; the same uniform bounds and Gaussian matrix marginal hold. Upper roots $Z_i$ and lower roots $V_i$ are iid within their respective row families, with the two families independent of one another and of $(G,H)$ and that input seed.

The actual chronological program is

\[
Y=GH,\qquad D_i=\Psi(Y_i,Z_i),\qquad X=G^\top D,
\qquad U_i=\Phi(H_i,X_i,V_i),\qquad F=GU.
\tag{1}
\]

The row dimensions are $H_i,Y_i\in\mathbb R^k$, $D_i,X_i\in\mathbb R^\ell$, and $U_i,F_i\in\mathbb R^q$. Rows in expectations are regarded as column vectors. The circuit coefficients are fixed; they are not empirical functions of realized rows. Assume

\[
\|\Psi(y,z)\|_2\leq M,\qquad
\|\Phi(h,x,v)\|_2\leq N,
\qquad
\|\Phi(h,x,v)-\Phi(h,x',v)\|_2\leq L\|x-x'\|_2.
\tag{2}
\]

Both circuits are continuously differentiable in the Gaussian arguments that are differentiated below, and Gaussian integration by parts is justified. Bounded first derivatives suffice; the same polynomial-growth/integrability convention as in GAP_FREE_RESPONSE_STEP.md also suffices for $\Psi$. The Lipschitz condition in (2) bounds the operator norm of $\partial_x\Phi$ by $L$.

Put

\[
Q=H^\top H/n,\quad
R=\mathbb E[\nabla_y\Psi(Y_\ast,Z_\ast)],\quad
T=\mathbb E[\Psi(Y_\ast,Z_\ast)\Psi(Y_\ast,Z_\ast)^\top],
\tag{3}
\]

where $Y_\ast\sim N(0,Q)$. Our Jacobian convention places the input coordinate first, so $R$ is $k\times\ell$. Let $\Xi$ have iid $N(0,T)$ rows, independent of all upper primitives and roots conditional on $H$. The lower reference fields are

\[
\overline X=HR+\Xi,\qquad
\overline U_i=\Phi(H_i,\overline X_i,V_i).
\tag{4}
\]

Define the deterministic conditional means, response, and full uncentered query pairing by

\[
\begin{aligned}
\mu_i&=\mathbb E[\overline U_i\mid H],\\
S&=\frac1n\sum_i
 \mathbb E[\nabla_x\Phi(H_i,R^\top H_i+\Xi_i,V_i)\mid H],\\
\mathcal Q_H
&=\frac1n\sum_i\mathbb E\left[
 \begin{pmatrix}H_i\\\overline U_i\end{pmatrix}
 \begin{pmatrix}H_i\\\overline U_i\end{pmatrix}^{\!\top}
 \mathrel{\Big|}H\right].
\end{aligned}
\tag{5}
\]

Assemble the means $\mu_i^\top$ into the rows of the matrix $\mu\in\mathbb R^{n\times q}$. Here $S$ is $\ell\times q$ and $\|S\|_{\mathrm{op}}\leq L$. The first derivative in $S$ holds $H,R,T$ and every population coefficient fixed. It is the response to the lower primitive $\Xi$, since $\partial_\Xi\overline X=I$.

The upper primitive pair $(Y_i,\eta_i)$ has covariance $\mathcal Q_H$, independently across upper rows. Its family is independent of $(\Xi,V,Z)$ conditional on $H$, except of course that $D$ is formed from $(Y,Z)$. The inverse-free second forward target is

\[
\overline F=\eta+DS.
\tag{6}
\]

Thus $\eta$ is colored with the already existing forward primitive $Y$. It is not an independent redraw with just the new query variance. The covariance in (5) is uncentered. Equations (3)–(6) are the prescribed scalar response law for this three-block program, conditional on the empirical design $H$.

Write $\|A\|_{F,n}^2=\|A\|_F^2/n$ for a matrix with $n$ rows.

**Theorem 1.** There is a coupling preserving the actual iid Gaussian matrix marginal and all the conditional primitive independence just specified, such that

\[
\begin{aligned}
\mathbb E[\|X-\overline X\|_{F,n}^2\mid H]
 &\leq M^2(2k+\ell)/n,\\
\mathbb E[\|U-\overline U\|_{F,n}^2\mid H]
 &\leq L^2M^2(2k+\ell)/n,\\
\mathbb E[\|F-\overline F\|_{F,n}^2\mid H]
 &\leq C_\ast/n,
\end{aligned}
\tag{7}
\]

where one deliberately coarse universal choice is

\[
C_\ast=1200\left[
L^2M^2(2k+\ell)
+N^2(1+k+k\ell+\ell+q)\right].
\tag{8}
\]

The constants contain no positive eigenvalue of any query covariance. No bound on individual rows of $H$ is needed for this conditional theorem.

## 2. Two elementary covariance facts

We use the coupling lemma proved in GAP_FREE_RESPONSE_STEP.md, in a slightly more general form. Let $v_i$ be independent, not necessarily identically distributed vectors with $\|v_i\|\leq B$, and let

\[
A_n=\frac1n\sum_i v_iv_i^\top,\qquad
A=\mathbb E A_n.
\]

On $\operatorname{range}A$, set $C=A^{-1/2}A_nA^{-1/2}$. With a fresh standard Gaussian $g$ on this support, the pair

\[
\zeta=A^{1/2}g,\qquad
\zeta_n=A^{1/2}C^{1/2}g
\tag{9}
\]

has conditional covariances $A,A_n$, and

\[
\mathbb E\|\zeta_n-\zeta\|^2
\leq\mathbb E\operatorname{tr}[(A_n-A)A^\dagger(A_n-A)]
\leq B^2\operatorname{rank}A/n.
\tag{10}
\]

For completeness, independence makes the weighted variance a sum of individual variances. Dropping their negative mean-square terms bounds it by

\[
\frac1{n^2}\sum_i
\mathbb E[\|v_i\|^2v_i^\top A^\dagger v_i]
\leq\frac{B^2}{n}\operatorname{tr}(A^\dagger A).
\]

The support assertion follows because a covariance-null direction has zero squared inner product with every $v_i$ almost surely. The first inequality in (10) is the scalar inequality $(\sqrt c-1)^2\leq(c-1)^2$ applied to $C$ and traced against $A$, exactly as in the earlier proof. All zero-rank cases are interpreted on the zero-dimensional support.

We also need a dual form that never estimates an inverse on its own. For any jointly centered Gaussian pair $(a,b)$, let

\[
A_a=\mathbb E[aa^\top],\qquad K=\mathbb E[ab^\top].
\]

Projection of $b-a$ onto the linear span of $a$ gives

\[
\operatorname{tr}[(K-A_a)^\top A_a^\dagger(K-A_a)]
\leq\mathbb E\|b-a\|^2.
\tag{11}
\]

One can verify this without assuming an invertible covariance: the best linear prediction is $(K^\top-A_a)A_a^\dagger a$ on the support, its residual is orthogonal in $L^2$ to that prediction, and their squared norms add. This proves (11). It is the regression counterpart of the covariance-factor estimate (10).

## 3. Preserve the first return and the exact Gaussian posterior

Let $P$ be the orthogonal projection onto $\operatorname{range}H$ and let $P_D$ project onto $\operatorname{range}D$. Use exactly the first-return coupling of GAP_FREE_RESPONSE_STEP.md. In particular, put

\[
T_n=D^\top D/n,\qquad
B_n=Q^\dagger Y^\top D/n.
\]

Conditional on the upper data $(H,Y,Z)$, couple iid Gaussian rows $\Xi_{n,i}\sim N(0,T_n)$ with $\Xi_i\sim N(0,T)$ using (9). This gives

\[
X=HB_n+(I-P)\Xi_n,\qquad
\mathbb E[\|X-\overline X\|_{F,n}^2\mid H]
\leq M^2(2k+\ell)/n.
\tag{12}
\]

The population-covariance rows $\Xi_i$ are independent of the entire upper data conditional on $H$. Their covariance-factor coupling with $\Xi_n$ is Gaussian conditional on that data. Write

\[
K_n=\mathbb E[\Xi_{n,i}\Xi_i^\top\mid H,Y,Z],\qquad
\delta_T^2=\mathbb E[\|\Xi_{n,i}-\Xi_i\|^2\mid H,Y,Z].
\]

The row index does not affect these quantities, and

\[
\mathbb E[\delta_T^2\mid H]\leq M^2\operatorname{rank}T/n.
\tag{13}
\]

The unused Gaussian matrix degrees of freedom can still be completed as

\[
G=YH^\dagger
+D T_n^\dagger\frac{\Xi_n^\top}{n}(I-P)
+(I-P_D)W(I-P),
\tag{14}
\]

where $W$ has independent $N(0,1/n)$ entries conditional on all the data so far. To check the posterior and its normalization, first write

\[
\widetilde G^\top=\Xi_nD^\dagger+W^\top(I-P_D).
\]

Conditional on the upper data, the two terms are independent Gaussian row projections with covariances $P_D/n$ and $(I-P_D)/n$. Thus $\widetilde G$ has the iid Gaussian law and $G=YH^\dagger+\widetilde G(I-P)$ has exactly the Gaussian posterior given $GH=Y$. Its reverse answer is (12). This proves the original iid $G$ marginal, including its original independence from $H,Z,V$.

The completion $W$ will be coupled to the second forward primitive at the moment that forward query is answered. At that point both $U$ and $\overline U$ are already known. We will preserve the conditional iid law of $W$ given the entire past, rather than conditioning that residual on an unrevealed future primitive and incorrectly declaring it fresh.

## 4. The two response means have gap-free errors

Temporarily apply $G$ to $\overline U$, and set

\[
a_n=H^\dagger\overline U,\qquad
a=H^\dagger\mu,\qquad
E=(I-P)\overline U.
\]

Equation (14) gives the exact identity

\[
G\overline U
=Ya_n+D T_n^\dagger\frac{\Xi_n^\top E}{n}
+(I-P_D)WE.
\tag{15}
\]

### 4.1. The repeated forward projection

Let $\epsilon=\overline U-\mu$. Its rows are independent and centered conditional on $H$, and are independent of $Y$. Also $\mathbb E\|\epsilon_i\|^2\leq N^2$. Therefore

\[
\begin{aligned}
\mathbb E[\|Y(a_n-a)\|_{F,n}^2\mid H]
&=\mathbb E[\|P\epsilon\|_{F,n}^2\mid H]\\
&\leq N^2\operatorname{rank}P/n.
\end{aligned}
\tag{16}
\]

The equality follows from the conditional covariance $Q$ of each row of $Y$. The inequality follows by expanding the squared norm of a deterministic projection of independent centered rows. No bound on the entries of $a$ or $a_n$ is taken.

### 4.2. The second reciprocal mean

Conditional on $(H,Y,Z)$, the rows $(\Xi_{n,i},\Xi_i,V_i)$ are independent. Gaussian integration by parts, applied to the joint pair and the circuit in (4), gives

\[
\mathbb E\left[\frac1n\Xi_n^\top\overline U
 \mathrel{\Big|}H,Y,Z\right]=K_n S.
\tag{17}
\]

Whiten only on the support of $T_n$. Since $\overline U_i$ is bounded by $N$, the centered empirical fluctuation obeys

\[
\mathbb E\left[
\left\|T_n^{\dagger/2}
 \left(\frac{\Xi_n^\top\overline U}{n}-K_nS\right)\right\|_F^2
 \mathrel{\Big|}H,Y,Z\right]
\leq N^2\operatorname{rank}T_n/n.
\tag{18}
\]

The part removed by $I-P$ has the bound

\[
\begin{aligned}
\left\|T_n^{\dagger/2}\frac{\Xi_n^\top P\overline U}{n}\right\|_F^2
&\leq N^2\frac{\|P\Xi_n T_n^{\dagger/2}\|_F^2}{n},\\
\mathbb E\left[
\left\|T_n^{\dagger/2}\frac{\Xi_n^\top P\overline U}{n}\right\|_F^2
 \mathrel{\Big|}H,Y,Z\right]
&\leq N^2\operatorname{rank}P\operatorname{rank}T_n/n.
\end{aligned}
\tag{19}
\]

The first inequality uses $\|\overline U\|_{\mathrm{op}}\leq N\sqrt n$. It does not assume that $\overline U$ is independent of $\Xi_n$.

Finally, the mean-correction mismatch is controlled in the correct weighted norm:

\[
\begin{aligned}
\|D(T_n^\dagger K_n-I)S\|_{F,n}^2
&=\|T_n^{\dagger/2}(K_n-T_n)S\|_F^2\\
&\leq L^2\delta_T^2.
\end{aligned}
\tag{20}
\]

The equality uses $D$ to annihilate covariance-null directions. Inequality (11), followed by $\|S\|_{\mathrm{op}}\leq L$, proves the last line. Thus even this apparently inverse-weighted correction is controlled by the original covariance coupling cost.

Combining (18)–(20), using the three-term squared triangle bound, and then (13) yields

\[
\mathbb E\left[
\left\|D T_n^\dagger\frac{\Xi_n^\top E}{n}-DS\right\|_{F,n}^2
 \mathrel{\Big|}H\right]
\leq\frac{3}{n}\left[N^2\ell(1+k)+L^2M^2\ell\right].
\tag{21}
\]

## 5. The new colored primitive without a residual-Gram gap

A direct application of (10) to residual rows $\overline U_i-H_i a$ is needlessly fragile: their deterministic projection means need not be uniformly bounded row by row. The following mean/centered-fluctuation split removes that issue.

Define

\[
r=(I-P)\mu,\qquad
A=\frac1n\sum_i\mathbb E[\epsilon_i\epsilon_i^\top\mid H],\qquad
B=r^\top r/n+A.
\tag{22}
\]

Let $P_r$ project onto $\operatorname{range}r$, and put $P_\ast=P+P_r$. These are orthogonal projections because $H^\top r=0$. Their ranks satisfy

\[
\operatorname{rank}P_r\leq q,\qquad
\operatorname{rank}P_\ast\leq k+q,\qquad
\operatorname{tr}B\leq N^2.
\tag{23}
\]

Take a fresh iid Gaussian matrix $W_0$, independent of the entire past. Apply (9)–(10) to the independent, centered, bounded rows $\epsilon_i$, with $\|\epsilon_i\|\leq2N$. For each upper row, this couples a Gaussian answer of covariance $\epsilon^\top\epsilon/n$ to a fresh $N(0,A)$ primitive. Assemble those primitives as $\zeta_A$. Complete a matrix $W_1$ satisfying

\[
W_1\epsilon=J,\qquad
\mathbb E[\|J-\zeta_A\|_{F,n}^2\mid H]
\leq4N^2\operatorname{rank}A/n,
\tag{24}
\]

while retaining the iid Gaussian law of $W_1$ conditional on the entire past. An explicit completion is

\[
W_1=J\epsilon^\dagger+W_2(I-P_\epsilon),
\]

where $W_2$ is a fresh iid Gaussian matrix. Conditional on the past, $J$ has exactly covariance $\epsilon^\top\epsilon/n$ in each independent row, so its projected term and the independent complementary term have the required covariances. This is the same elementary posterior completion as in Section 3.

The target $\zeta_A$ is chosen independent of all past data, row by row, and independent of $W_0$. Now set

\[
W=W_0P_\ast+W_1(I-P_\ast),\qquad
\zeta_r=W_0r,\qquad
\zeta=\zeta_r+\zeta_A.
\tag{25}
\]

Conditional on the entire past, $W_0,W_1$ are independent iid Gaussian matrices, so $W$ has the same iid Gaussian law. Thus this is an admissible choice for the still-unused completion in (14). Both $\zeta_r$ and $\zeta_A$ are fresh Gaussian primitives independent of the past, with covariances $r^\top r/n$ and $A$, and they are independent of one another. Consequently $\zeta$ has iid $N(0,B)$ rows and is independent of $(Y,Z,\Xi,V)$ conditional on $H$.

Since $E=r+(I-P)\epsilon$, the exact difference is

\[
WE-\zeta
=W_0P_r\epsilon+(W_1\epsilon-\zeta_A)-W_1P_\ast\epsilon.
\tag{26}
\]

For any deterministic projection $P_0$, independence and centering of the rows of $\epsilon$ imply

\[
\mathbb E\|P_0\epsilon\|_{F,n}^2
\leq N^2\operatorname{rank}P_0/n.
\]

Conditional on the past, either $W_0$ or $W_1$ is an iid Gaussian matrix, so multiplication by it preserves the expected normalized squared norm of a fixed matrix. This is sufficient even though $W_1\epsilon$ is coupled with $\zeta_A$. Equations (23)–(26) therefore give

\[
\mathbb E[\|WE-\zeta\|_{F,n}^2\mid H]
\leq3N^2(k+6q)/n.
\tag{27}
\]

The remaining left projection costs only its rank, because $\zeta$ is independent of $D$:

\[
\begin{aligned}
\mathbb E[\|(I-P_D)WE-\zeta\|_{F,n}^2\mid H]
&\leq 2\mathbb E[\|WE-\zeta\|_{F,n}^2\mid H]
 +2\mathbb E[\|P_D\zeta\|_{F,n}^2\mid H]\\
&\leq N^2(6k+36q+2\ell)/n.
\end{aligned}
\tag{28}
\]

Finally define

\[
\eta=Ya+\zeta.
\tag{29}
\]

Its cross-covariance with $Y$ is $Qa=H^\top\mu/n$, and its covariance is

\[
a^\top Qa+B
=\mu^\top P\mu/n+\mu^\top(I-P)\mu/n+A
=\frac1n\sum_i\mathbb E[\overline U_i\overline U_i^\top\mid H].
\]

Thus (29) has exactly the colored primitive covariance (5), including in singular cases. Its entire primitive family is independent of the lower primitive family and both external-root families, as required. The actual fields $D=\Psi(Y,Z)$ and $\overline F=\eta+DS$ need not be Gaussian or independent of those roots; no such claim is made.

## 6. Restore the actual nonlinear query and finish Theorem 1

Combining (15), (16), (21), and (28) gives

\[
\mathbb E[\|G\overline U-\overline F\|_{F,n}^2\mid H]
\leq C_{\mathrm{alg}}/n,
\tag{30}
\]

where one valid bound is

\[
C_{\mathrm{alg}}
=N^2(21k+9k\ell+15\ell+108q)+9L^2M^2\ell.
\tag{31}
\]

The Lipschitz condition yields the second line of (7) directly from (12). Dependence between this query error and $G$ must still be respected when multiplying it by $G$.

Here an elementary operator-norm tail suffices. A $1/4$-net of the unit sphere can be chosen with at most $9^n$ points: take a maximal separated set and compare volumes of disjoint radius-$1/8$ balls inside the radius-$9/8$ ball. Approximating both unit vectors in a bilinear form gives

\[
\mathbb P\{\|G\|_{\mathrm{op}}>t\}
\leq2\exp(2n\log9-nt^2/8).
\tag{32}
\]

Indeed each fixed unit-vector bilinear form is $N(0,1/n)$, whose two-sided tail is at most $2e^{-ns^2/2}$, obtained from its Gaussian moment generating function and Markov's inequality. The double-net approximation loses a factor two.

For $t\geq8$, integrate (32) to obtain

\[
\mathbb E[\|G\|_{\mathrm{op}}^2\mathbf1_{\{\|G\|_{\mathrm{op}}>8\}}]
\leq144e^{-(8-2\log9)n}\leq144/n.
\tag{33}
\]

On the complementary event, use $\|G\|_{\mathrm{op}}^2\leq64$. On the exceptional event use the deterministic bound $\|U-\overline U\|_{F,n}\leq2N$. Consequently

\[
\mathbb E[\|G(U-\overline U)\|_{F,n}^2\mid H]
\leq\frac{64L^2M^2(2k+\ell)+576N^2}{n}.
\tag{34}
\]

The conditional iid Gaussian marginal of $G$ is what justifies (32)–(34); no independence between $G$ and the query error was assumed. Applying the two-term squared triangle bound to (30) and (34) proves the last line of (7) with (8). This completes Theorem 1.

## 7. A fixed-population version under uniform derivative stability

The target in Theorem 1 depends on the realized independent design $H$. The following additional hypotheses allow comparison to a deterministic population law as well.

Assume the rows $H_i=h(A_i)$ are iid and $\|h(A_i)\|\leq B$. In addition to (2), suppose $\Psi$ is uniformly $L_\Psi$-Lipschitz in $y$ and its Jacobian is uniformly $J_\Psi$-Lipschitz in Frobenius norm. Suppose the Jacobian $\nabla_x\Phi$ is uniformly $J_\Phi$-Lipschitz in $x$, with Frobenius norm on the Jacobian. These bounds are uniform over the other root arguments and $h$. They are sufficient conditions for the comparison below, not a claim that this derivative regularity is necessary.

Define the fixed population law by

\[
\begin{aligned}
Q_0&=\mathbb E[hh^\top],&Y_0&\sim N(0,Q_0),&D_0&=\Psi(Y_0,Z),\\
R_0&=\mathbb E\nabla_y\Psi(Y_0,Z),&
T_0&=\mathbb E[D_0D_0^\top],&\xi_0&\sim N(0,T_0),\\
x_0&=R_0^\top h+\xi_0,&u_0&=\Phi(h,x_0,V),&
S_0&=\mathbb E\nabla_x\Phi(h,x_0,V).
\end{aligned}
\tag{35}
\]

The upper joint primitive pair $(Y_0,\eta_0)$ has covariance

\[
\mathcal Q_0=\mathbb E\left[
\begin{pmatrix}h\\u_0\end{pmatrix}
\begin{pmatrix}h\\u_0\end{pmatrix}^{\!\top}\right],
\qquad f_0=\eta_0+D_0S_0.
\tag{36}
\]

The lower primitive $\xi_0$, upper primitive family $(Y_0,\eta_0)$, and external root families are independent in their stipulated populations. The repeated use of $h$ and the colored upper covariance retain their proper within-population dependence.

**Theorem 2.** Under these hypotheses, the actual program (1) can be coupled to independent row copies of the respective population laws in (35)–(36), using the original lower $H_i$ and roots $V_i,Z_i$, with normalized mean-square errors at most $C/n$ for $Y,D,X,U,F$. The finite constant $C$ depends only on

\[
k,\ell,q,B,M,N,L,L_\Psi,J_\Psi,J_\Phi,
\tag{37}
\]

not on any positive covariance eigenvalue. This is a coupling theorem; the fixed population law itself is the causal scalar response law, not a law with empirically fitted coefficients.

### 7.1. Lower-law and response transfer

The first covariance coupling gives a population Gaussian pair at covariances $Q=H^\top H/n$ and $Q_0$ with conditional squared cost $\delta_H^2$ satisfying

\[
\mathbb E\delta_H^2\leq B^2k/n.
\tag{38}
\]

The derivative regularity gives $\|R-R_0\|_F^2\leq J_\Psi^2\delta_H^2$. Gaussianize the full uncentered joint second moments of the coupled pair of $\Psi$ outputs. This provides a Gaussian pair $(\xi_H,\xi_0)$ with covariances $T,T_0$ and cost at most $L_\Psi^2\delta_H^2$. Such Gaussianization is elementary: the joint second-moment matrix is positive semidefinite, so multiplying its positive square root by independent standard normals constructs the pair.

This lower pair can be attached to the already constructed $\Xi$ in Theorem 1, independently of all upper primitive variables conditional on $H$. Define

\[
A_\mathrm{low}=B^2J_\Psi^2+L_\Psi^2.
\]

Then the coupled conditional lower laws satisfy

\[
\frac1n\sum_i\mathbb E\|R^\top H_i+\xi_H-(R_0^\top H_i+\xi_0)\|^2
\leq A_\mathrm{low}\delta_H^2,
\tag{39}
\]

where expectations in this display are conditional on $H$. The corresponding $u$-law cost is at most $L^2A_\mathrm{low}\delta_H^2$.

Let $S_{H,0}$ be the average over the actual $H_i$ of the expected Jacobian at $R_0^\top H_i+\xi_0$. Jensen's inequality and the derivative bound give

\[
\|S-S_{H,0}\|_F^2\leq J_\Phi^2 A_\mathrm{low}\delta_H^2.
\]

The terms in $S_{H,0}$ are iid functions of $H_i$, and their Frobenius norms are at most $\sqrt{\min(\ell,q)}L$. The sample-mean variance identity therefore yields

\[
\mathbb E\|S-S_0\|_F^2\leq C_S/n,
\quad
C_S=2J_\Phi^2 A_\mathrm{low}B^2k+2\min(\ell,q)L^2.
\tag{40}
\]

### 7.2. Transfer the entire colored upper family, not just its new variance

Let $\mathcal Q_{H,0}$ be the empirical average over $H_i$ of the conditional second moments of $(H_i,u_0)$, with the fixed lower population coefficients. Coupling the two lower query tuples with the same $H_i$ and the lower Gaussian pair above, then Gaussianizing their joint second moments, couples centered Gaussians at $\mathcal Q_H$ and $\mathcal Q_{H,0}$ with squared cost at most $L^2A_\mathrm{low}\delta_H^2$.

The remaining comparison of $\mathcal Q_{H,0}$ and $\mathcal Q_0$ is also gap-free. Here each summand of $\mathcal Q_{H,0}$ is a random positive-semidefinite matrix $A_i$ with $\operatorname{tr}A_i\leq B^2+N^2$, iid across input rows, and $\mathbb E A_i=\mathcal Q_0$. The proof of (10) extends to these matrices because

\[
\operatorname{tr}(A_i\mathcal Q_0^\dagger A_i)
=\operatorname{tr}(\mathcal Q_0^\dagger A_i^2)
\leq(B^2+N^2)\operatorname{tr}(\mathcal Q_0^\dagger A_i).
\]

Consequently the covariance-factor coupling cost is at most

\[
(B^2+N^2)\operatorname{rank}\mathcal Q_0/n
\leq(B^2+N^2)(k+q)/n.
\]

The two Gaussian couplings can be joined at their common middle Gaussian marginal. In a singular case, use the ordinary Gaussian conditional distribution on its support and an independent complementary innovation; the resulting joint distribution has the prescribed pair marginals. The squared triangle inequality gives a coupling of the entire upper pair $(Y,\eta)$ to $(Y_0,\eta_0)$ with

\[
\mathbb E\bigl[\|Y-Y_0\|_{F,n}^2+
\|\eta-\eta_0\|_{F,n}^2\bigr]\leq C_Q/n,
\]

where

\[
C_Q=2L^2A_\mathrm{low}B^2k+2(B^2+N^2)(k+q).
\tag{41}
\]

This is a transfer of the full colored family. Coupling only the marginal new variance would not suffice.

The transfer can be attached after Theorem 1's exact dense coupling has been constructed. Conditional on $H$, its coefficients are deterministic, and its upper Gaussian variables depend only on the existing upper primitive family and extra fresh randomness. The existing upper family is independent of the entire lower primitive/root sample. Hence this attachment preserves that independence. The new upper marginal covariance is the fixed $\mathcal Q_0$, so the new family is also independent of $H$. Likewise the lower $\xi_0$ marginal covariance is the fixed $T_0$. Thus the final reference families have their required joint independence, not just individually correct covariances.

This final transfer is an existence coupling, not an assertion that the two models' Gaussian innovations are matched online at every earlier event. It never reconditions the dense matrix or uses a future primitive to justify a past residual being fresh. The causal construction and exact matrix marginal were already settled in Sections 3–6.

### 7.3. Finish the population comparison

Using the same $Z_i$ in $D_i$ and $D_{0,i}$ gives

\[
\mathbb E\|D-D_0\|_{F,n}^2\leq L_\Psi^2 C_Q/n.
\]

The two target forward answers differ by

\[
\overline F-F_0=(\eta-\eta_0)+(D-D_0)S+D_0(S-S_0).
\]

Therefore (40)–(41), $\|S\|_{\mathrm{op}}\leq L$, and $\|D_{0,i}\|\leq M$ imply

\[
\mathbb E\|\overline F-F_0\|_{F,n}^2
\leq\frac{3[(1+L^2L_\Psi^2)C_Q+M^2C_S]}{n}.
\tag{42}
\]

Combine this with (7). The comparisons for $X,U$ follow from (39), (38), (7), and the Lipschitz bound on $\Phi$; those for $Y,D$ have just been displayed. This proves Theorem 2 with explicit finite combinations of the constants in (8), (39)–(42).

## 8. Scope, dependence, and remaining work

Theorems 1–2 establish root-width normalized field coupling for exactly one additional alternating round. By Markov's inequality this yields fixed-confidence $O_{\mathbb P}(n^{-1/2})$ errors with the displayed gap-free constants. Inverse-polynomial failure probability with only logarithmic losses has not been proved here.

The mechanism behind the estimate is specific and reusable: estimate regression only after multiplication by its query matrix; bound the reverse covariance-factor mismatch by a dual Gaussian projection inequality; split a new row circuit into its deterministic mean and centered independent fluctuations; and pay finite-rank projection losses directly. All matrix inverses appearing in this proof act only on supports and disappear from the final constants.

The conditional result does not require $H$ to have well-conditioned or even full-rank columns. The population theorem additionally requires bounded iid input rows and uniform derivative stability. The actual unbounded neural backward carriers do not automatically satisfy the bounded circuit assumptions (2). Extending the argument to them requires explicit weighted moments or a justified tail/truncation estimate; no clipping of the actual program has been performed here.

At the next alternating round, the relevant inputs will depend on additional already conditioned Gaussian directions, and the independent centered-row representation used here must be established anew. The present note does not give an induction for arbitrarily many alternating rounds, a uniform dependence on query count, continuous-time passage, or an all-time dense-variability guarantee. It removes one more concrete local obstruction without changing the original labels or network-depth assumptions.
