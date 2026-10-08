# A gap-free quantitative Gaussian response step

2026-10-07. Bounded proof attempt for one initialized matrix interface. The result is a finite-width coupling theorem for an independent forward-query batch followed by one reciprocal reverse-query batch. It is not yet a theorem for arbitrary alternating queries, a mesh-uniform neural computation, or all physical times.

Scientific inputs: the supervisor's assignment; the complete RESPONSE_GAUSSIAN_CLOSURE.md and this route's audit; FIXED_HISTORY_RATE.md and FIXED_HISTORY_RATE_AUDIT.md; ADAPTIVE_SIGNAL_CONCENTRATION.md and ADAPTIVE_SIGNAL_AUDIT.md. No external source, numerical experiment, other study, or other audit was used. All arguments below are supplied explicitly.

The main estimate is

\[
\mathbb E\left[\frac1n\|G^\top D-(HR+\Xi)\|_F^2\,\middle|\,H\right]
\leq \frac{M^2}{n}\bigl(2\operatorname{rank}Q+
\operatorname{rank}T\bigr).
\tag{1}
\]

Here the forward-query Gram matrix is $Q=H^\top H/n$, the rows of the reverse-query batch $D$ have Euclidean norm at most $M$, $R$ is its expected response to the forward Gaussian fields, and the independent primitive rows of $\Xi$ have the full uncentered reverse-query covariance $T$. Neither positive eigenvalues nor their reciprocals occur in the bound. Exact dependence and arbitrarily small positive eigenvalues are both allowed.

There are two distinct reference laws. The first uses the actual conditional covariance $H^\top H/n$ and gives (1) under mild differentiability plus bounded output. The second uses a fixed population covariance and requires an additional, explicitly stated response-stability estimate. Uniformly Lipschitz Jacobians are one sufficient condition for that extra estimate, not a necessary condition asserted here.

## 1. Setup and chronological scope

Let $G\in\mathbb R^{n\times n}$ have independent $N(0,1/n)$ entries. A matrix $H\in\mathbb R^{n\times k}$ supplies $k$ lower-population forward queries and is independent of $G$. Initially condition on $H$; it need not have independent rows. Define

\[
Q=\frac1nH^\top H,\qquad Y=GH.
\tag{2}
\]

The rows $Y_i\in\mathbb R^k$ are conditionally independent $N(0,Q)$ vectors. Let $Z_i$ be independent, identically distributed auxiliary upper-population roots, independent of $(G,H)$. A fixed local row circuit

\[
\Psi:\mathbb R^k\times\mathcal Z\longrightarrow\mathbb R^\ell
\]

forms a reverse-query batch $D\in\mathbb R^{n\times\ell}$ by

\[
D_i=\Psi(Y_i,Z_i),\qquad X=G^\top D.
\tag{3}
\]

Rows are identified with column vectors in expectations; in a matrix such as $D$, its $i$th row is $D_i^\top$. Assume

\[
\|\Psi(y,z)\|_2\leq M
\tag{4}
\]

and that $\Psi$ is continuously differentiable in $y$. Its values and derivatives satisfy the integration and boundary conditions for Gaussian integration by parts. For example, polynomial growth of the derivatives in $y$ with integrable auxiliary coefficients is sufficient. Only these integration conditions, rather than any global Hessian bound, are used in Sections 2–4.

All circuit coefficients are fixed during this block. They may be fixed functions of $H$ when working conditionally on $H$, provided (4) and the integration conditions hold. They are not estimated using the realized upper rows $(Y_i,Z_i)$ in the theorem as stated.

The forward inputs cannot depend on earlier answers from this same $G$. The reverse inputs may depend on all forward answers in their own upper row, but cannot depend on earlier reverse answers. The batches can be issued as sequential chronological instructions because their inputs have the stated dependencies. Thus this is genuinely a reciprocal, matrix-reusing program, but it has only one direction switch.

For $Y_\ast\sim N(0,Q)$ and an independent $Z_\ast$ of the auxiliary-root law, define

\[
R_{aj}=\mathbb E[\partial_{y_a}\Psi_j(Y_\ast,Z_\ast)],
\qquad
T=\mathbb E[\Psi(Y_\ast,Z_\ast)\Psi(Y_\ast,Z_\ast)^\top].
\tag{5}
\]

Thus $R\in\mathbb R^{k\times\ell}$ and $T\in\mathbb R^{\ell\times\ell}$. These are population expectations conditional on the given $H$, not averages of the upper sample. Crucially, $T$ is uncentered: no subtraction of the mean of $\Psi$ is made. Write $r_H=\operatorname{rank}Q$ and $r_D=\operatorname{rank}T$. For any matrix $A$ with $n$ rows, use

\[
\|A\|_{F,n}^2=\frac1n\operatorname{tr}(A^\top A).
\tag{6}
\]

The inverse-free response return associated with this block is

\[
\overline X=HR+\Xi,
\tag{7}
\]

where, conditional on $H$, the rows of $\Xi$ are independent centered Gaussians with covariance $T$ and $\Xi$ is independent of all upper roots and forward fields $(Y,Z)$. When $H$ is random, this is conditional independence; $T$ itself may depend on $H$.

## 2. A covariance-weighted Gaussian coupling lemma

The following elementary estimate is the quantitative cancellation needed below. It is stronger than applying an unweighted square-root perturbation bound to covariance entries.

**Lemma 1.** Let $v_1,\ldots,v_n\in\mathbb R^d$ be independent copies of $v$, with $\|v\|_2\leq M$, and put

\[
B=\mathbb E[vv^\top],\qquad A_n=\frac1n\sum_i v_iv_i^\top.
\tag{8}
\]

There is a coupling of a sample-dependent centered Gaussian $\zeta_n$, having conditional covariance $A_n$, and a centered Gaussian $\zeta$ of covariance $B$ independent of the sample, for which

\[
\mathbb E\|\zeta_n-\zeta\|_2^2
\leq\frac{M^2\operatorname{rank}B}{n}.
\tag{9}
\]

The construction also gives, conditional on the sample,

\[
\mathbb E[\|\zeta_n-\zeta\|_2^2\mid v_1,\ldots,v_n]
\leq\operatorname{tr}\bigl[(A_n-B)B^\dagger(A_n-B)\bigr].
\tag{10}
\]

Here and below the dagger is the Moore–Penrose inverse, used only in the proof and coupling construction, not as a parameter in the resulting bound.

**Proof.** If $u\in\ker B$, then $\mathbb E(u^\top v)^2=0$, so $u^\top v=0$ almost surely. A finite basis of $\ker B$ therefore shows that $v$ and every $v_i$ lie in $E=\operatorname{range}B$ almost surely. If $E=\{0\}$, all variables in the lemma are zero. Otherwise restrict all the following operators to $E$, where $B$ is positive definite, and define

\[
C=B^{-1/2}A_nB^{-1/2}.
\]

For a fresh standard Gaussian $z$ on $E$, independent of the sample, set

\[
\zeta=B^{1/2}z,\qquad \zeta_n=B^{1/2}C^{1/2}z.
\tag{11}
\]

These have the asserted marginal and conditional covariances. In particular, the possibly noncommuting product $B^{1/2}C^{1/2}$ is used as a covariance factor; it is not asserted to equal the positive square root of $A_n$.

The scalar inequality $(\sqrt c-1)^2\leq(c-1)^2$ for $c\geq0$, applied in an eigenbasis of $C$, gives

\[
\begin{aligned}
\mathbb E_z\|\zeta_n-\zeta\|_2^2
&=\operatorname{tr}[B(C^{1/2}-I)^2]\\
&\leq\operatorname{tr}[B(C-I)^2]\\
&=\operatorname{tr}[(A_n-B)B^\dagger(A_n-B)].
\end{aligned}
\tag{12}
\]

The first inequality is valid although $B$ need not commute with $C$: the difference of the two functions of $C$ is positive semidefinite, and its trace against $B\succeq0$ is nonnegative. The last equality follows by cyclically permuting factors in the trace on $E$.

Independence and centering of the summands in $A_n-B$ give the exact identity

\[
\begin{aligned}
&\mathbb E\operatorname{tr}[(A_n-B)B^\dagger(A_n-B)]\\
&\quad=\frac1n\left(
\mathbb E[\|v\|_2^2v^\top B^\dagger v]-\operatorname{tr}B
\right)\\
&\quad\leq\frac{M^2}{n}\mathbb E[v^\top B^\dagger v]
=\frac{M^2\operatorname{rank}B}{n}.
\end{aligned}
\tag{13}
\]

Thus no smallest positive eigenvalue is left in the estimate. This proves the lemma. ∎

The same construction can be applied independently to any number of Gaussian rows, conditional on the one shared sample. The population-covariance rows are then independent of the sample and of each other. Although the empirical-covariance rows share $A_n$, they are independent conditional on that sample.

For later use, boundedness can be replaced in this lemma by the explicit assumption

\[
\kappa_B:=\mathbb E[\|v\|_2^2v^\top B^\dagger v]<\infty.
\tag{14}
\]

The exact right-hand side in (13) is $(\kappa_B-\operatorname{tr}B)/n$. A gap-free unbounded-family result needs an independently verified uniform bound on this weighted fourth moment; naming it does not establish such a bound.

## 3. The reciprocal response theorem

**Theorem 2.** Under Section 1, the actual Gaussian matrix program $(H,Y,Z,D,X)$ and the inverse-free return (7) can be realized on one probability space, preserving their stipulated marginal laws, such that

\[
\mathbb E[\|X-\overline X\|_{F,n}^2\mid H]
\leq\frac{M^2}{n}(2r_H+r_D).
\tag{15}
\]

The rows of $\Xi$ are independent of $(Y,Z)$ conditional on $H$, as required by (7). The estimate is uniform over singular $Q,T$ and their positive eigenvalues; it also holds for a width-dependent family of such matrices and circuits with the same $M,k,\ell$.

### 3.1. Exact finite Gaussian conditioning

Let $P$ be the orthogonal projection in $\mathbb R^n$ onto the column space of $H$. Conditional on $(H,Y)$, the Gaussian matrix has the representation in distribution

\[
G=YH^\dagger+\widetilde G(I-P),
\tag{16}
\]

where $\widetilde G$ has independent $N(0,1/n)$ entries and is independent of the conditioned data. This follows row by row by decomposing a centered isotropic Gaussian vector into its projections onto $\operatorname{range}H$ and its orthogonal complement. The two Gaussian projections are independent because their cross-covariance is zero. This reasoning does not require $H$ to have full column rank.

Since $Z$ is independent and $D$ is a function of $(Y,Z)$, conditioning also on $Z$ leaves the same posterior law. Consequently,

\[
X=H A_n+(I-P)\Xi_n,
\qquad
A_n=Q^\dagger\frac{Y^\top D}{n},
\qquad
T_n=\frac{D^\top D}{n},
\tag{17}
\]

where, conditional on $(H,Y,Z)$, the rows of $\Xi_n$ are independent centered Gaussians with covariance $T_n$. The identity $(H^\dagger)^\top=H(H^\top H)^\dagger$ gives the mean in (17).

Use Lemma 1 with $v_i=D_i$, $B=T$, and $A_n=T_n$ to construct $\Xi_n$ and $\Xi$ simultaneously, applying its fresh Gaussian construction separately to each lower row. Then $\Xi$ has exactly the conditional independence specified in Section 1, and

\[
\mathbb E[\|\Xi_n-\Xi\|_{F,n}^2\mid H]
\leq\frac{M^2 r_D}{n}.
\tag{18}
\]

This specifies a coupling of the actual answers, not just an approximate posterior. If one also wants the whole original matrix on this coupled space, the conditional law (16) can be completed explicitly. Given an admissible $\Xi_n$ and $D$, take

\[
\widetilde G^\top=\Xi_nD^\dagger+W^\top(I-P_D),
\tag{19}
\]

where $P_D$ projects onto the column space of $D$ and $W$ has independent $N(0,1/n)$ entries, independently of every variable already constructed. Each row of $\Xi_n$ lies in the row space of $D$ almost surely, because its conditional covariance is $D^\top D/n$. Conditional on $(H,Y,Z)$, (19) has exactly the independent-entry Gaussian law: its two terms are independent centered Gaussian projections with covariances $P_D/n$ and $(I-P_D)/n$ in each row. Also $\widetilde G^\top D=\Xi_n$. Inserting (19) in (16) therefore gives the original joint law of $(G,H,Y,Z)$, including independence of the originally independent inputs. Its coupling with $\Xi$ may of course be nontrivial; no independence of the target primitive from the entire realized $G$ is required or claimed.

### 3.2. Singular Stein identity and the response mean

For clarity, the needed integration-by-parts identity is

\[
\mathbb E[Y_\ast\Psi(Y_\ast,Z_\ast)^\top]=QR.
\tag{20}
\]

Write $Y_\ast=L g$, where $LL^\top=Q$ and $g$ is a standard Gaussian on the support dimension. Integration by parts in each scalar $g_j$ gives

\[
\mathbb E[g_j\Psi(Lg,Z_\ast)^\top]
=\mathbb E[\partial_{g_j}\Psi(Lg,Z_\ast)^\top].
\]

The chain rule and multiplication by $L$ prove (20). The regularity in Section 1 justifies the boundary terms and integration. This proof includes singular $Q$ without an approximation by positive definite covariances.

Let $B_n=Y^\top D/n$. Since every $Y_i$ lies in $\operatorname{range}Q$ almost surely and $H$ annihilates $\ker Q$,

\[
\|H(A_n-R)\|_{F,n}^2
=\|Q^{\dagger/2}(B_n-QR)\|_F^2.
\tag{21}
\]

The terms $Q^{\dagger/2}Y_iD_i^\top$ are independent, their mean is $Q^{1/2}R$, and their squared Frobenius norms are bounded by $M^2\|Q^{\dagger/2}Y_i\|_2^2$. Therefore

\[
\begin{aligned}
\mathbb E[\|H(A_n-R)\|_{F,n}^2\mid H]
&\leq\frac{M^2}{n}\mathbb E\|Q^{\dagger/2}Y_\ast\|_2^2\\
&=\frac{M^2r_H}{n}.
\end{aligned}
\tag{22}
\]

The possibly large entries of $A_n-R$ are never estimated separately. Their effect is measured only after multiplication by the actual query matrix $H$, which gives precisely the covariance-weighted norm in (21).

### 3.3. Orthogonality and the quantitative bound

Subtract (7) from (17):

\[
X-\overline X
=H(A_n-R)-P\Xi+(I-P)(\Xi_n-\Xi).
\tag{23}
\]

The last term is spatially orthogonal to each of the first two. Moreover, conditional on $(H,Y,Z)$, $\Xi$ is centered, so the expected inner product of $H(A_n-R)$ and $P\Xi$ vanishes. Since the rows of $\Xi$ are independent with covariance $T$,

\[
\mathbb E[\|P\Xi\|_{F,n}^2\mid H]
=\frac{r_H\operatorname{tr}T}{n}
\leq\frac{r_HM^2}{n}.
\tag{24}
\]

Use (18), (22), and contraction by $I-P$ in (23). Their three contributions give (15). ∎

All formulas remain valid at rank zero. If $Q=0$, then $H=Y=0$ and the only error being bounded is the replacement of the random reverse covariance by $T$. If $T=0$, then $D=0$ almost surely; (20) implies $HR=0$, so both actual and reference returns vanish.

The smooth off-support extension of $\Psi$ can change individual entries of $R$ when $Q$ is singular. It cannot change $HR$: two extensions agreeing on the Gaussian support have expected-gradient difference annihilated by $Q$, by (20), and hence by $H$. Thus the observable response return is extension-invariant.

## 4. Which part of arbitrary chronological conditioning is already gap-free?

The fresh projection loss itself never needs a history-Gram gap. For any past-measurable orthogonal projection $P_{\mathrm{past}}$ and a fresh standard Gaussian $\xi\in\mathbb R^n$ independent of that past,

\[
\mathbb E\left[\frac1n\|P_{\mathrm{past}}\xi\|_2^2
\mathrel{\big|}\mathrm{past}\right]
=\frac{\operatorname{rank}P_{\mathrm{past}}}{n}.
\tag{25}
\]

Indeed, the conditional covariance of $\xi$ is the identity, so the numerator's conditional expectation is $\operatorname{tr}P_{\mathrm{past}}$. More generally, fresh independent Gaussian rows with feature covariance $T$ give rank times $\operatorname{tr}T/n$, exactly as in (24). A history can be exactly redundant or nearly dependent without changing this identity.

This isolates three gap-free ingredients in Theorem 2: the projected fresh noise, the response regression error measured after multiplication by $H$, and the empirical-to-population primitive covariance coupling. The proof works because, after conditioning on $H$, the upper rows used to estimate the latter two objects are independent copies. Arbitrary alternating queries remove precisely that simple independence; (25) alone does not repair their entire comparison proof.

## 5. Transfer to a fixed population covariance

Theorem 2 conditionally uses $Q=H^\top H/n$. The following corollary makes the stronger, distinct comparison to a deterministic population law.

Assume now that the lower rows are independent copies

\[
H_i=h(U_i)\in\mathbb R^k,\qquad \|h(U_i)\|_2\leq B,
\qquad Q_0=\mathbb E[h(U)h(U)^\top],
\tag{26}
\]

with the whole lower-root sample independent of $G$ and the upper roots. The same fixed circuit $\Psi$ is used for every $H$. Let $Y_0\sim N(0,Q_0)$, independent of $Z_\ast$, and define

\[
R_0=\mathbb E[\nabla_y\Psi(Y_0,Z_\ast)],\qquad
T_0=\mathbb E[\Psi(Y_0,Z_\ast)\Psi(Y_0,Z_\ast)^\top].
\tag{27}
\]

Our gradient convention in (27) places the input index first, so it is the $k\times\ell$ matrix used in (5).

For a realized $H$, Lemma 1 gives a coupling of $Y_H\sim N(0,Q)$ and $Y_0\sim N(0,Q_0)$ whose conditional squared cost is

\[
\delta_H^2:=\mathbb E[\|Y_H-Y_0\|_2^2\mid H],
\qquad
\mathbb E\delta_H^2\leq\frac{B^2\operatorname{rank}Q_0}{n}
\leq\frac{B^2 k}{n}.
\tag{28}
\]

The $Y_0$ marginal does not depend on $H$. Choose the fresh Gaussian seeds independently of the complete lower-root sample and upper roots. Independent copies of these seeds in Lemma 1 yield upper rows $(Y_i,Y_{0,i})$ that are independent conditional on $H$, with $Y_0$ independent of the whole lower-root sample. The same upper roots $Z_i$ can be used on both sides. Write $R_H,T_H$ for (5) with covariance $Q$.

**Response-stability assumption.** For the couplings in (28), assume constants $L_0,L_1$ independent of $H,n$ satisfy

\[
\begin{aligned}
\mathbb E[\|\Psi(Y_H,Z_\ast)-\Psi(Y_0,Z_\ast)\|_2^2\mid H]
&\leq L_0^2\delta_H^2,\\
\|R_H-R_0\|_F^2&\leq L_1^2\delta_H^2.
\end{aligned}
\tag{29}
\]

This is an explicit conditional hypothesis, not an inference from mere continuity of the responses. For example, it holds if $\Psi$ is uniformly $L_0$-Lipschitz in $y$ and its Jacobian is uniformly $L_1$-Lipschitz in $y$ in Frobenius norm. The second assertion then follows by Jensen's inequality applied to the coupled Jacobians. More specialized circuits can establish (29) directly without a global Jacobian-Lipschitz assumption.

**Corollary 3.** Under (26)–(29) and Section 1, the whole reciprocal block has a coupling to the deterministic-covariance reference fields

\[
D_{0,i}=\Psi(Y_{0,i},Z_i),\qquad
X_0=HR_0+\Xi_0,
\tag{30}
\]

where $Y_{0,i}$ are independent $N(0,Q_0)$ rows independent of the lower roots, and $\Xi_{0,i}$ are independent $N(0,T_0)$ rows independent of all upper fields and lower roots. It satisfies

\[
\begin{aligned}
\mathbb E\|Y-Y_0\|_{F,n}^2&\leq B^2k/n,\\
\mathbb E\|D-D_0\|_{F,n}^2&\leq L_0^2B^2k/n,\\
\mathbb E\|X-X_0\|_{F,n}^2&\leq C_{\mathrm{block}}/n,
\end{aligned}
\tag{31}
\]

with the explicit choice

\[
C_{\mathrm{block}}
=2M^2(2k+\ell)
+2(B^2L_1^2+L_0^2)B^2k.
\tag{32}
\]

No positive eigenvalue of $Q_0,Q,T_H,T_0$, and no innovation lower bound, occurs in this constant.

**Proof.** Only the primitive-noise transfer and its joint independence need further care. Given $H$, use the coupling in (28) with a common independent $Z_\ast$ to obtain a pair

\[
d_H=\Psi(Y_H,Z_\ast),\qquad d_0=\Psi(Y_0,Z_\ast).
\]

Their full uncentered block second-moment matrix is positive semidefinite. Therefore a centered Gaussian pair $(\xi_H,\xi_0)$ exists with that block covariance: explicitly, diagonalize this nonnegative matrix and multiply its positive square root by a fresh standard Gaussian vector. Its marginals have covariances $T_H,T_0$, and

\[
\mathbb E[\|\xi_H-\xi_0\|_2^2\mid H]
=\mathbb E[\|d_H-d_0\|_2^2\mid H]
\leq L_0^2\delta_H^2.
\tag{33}
\]

Use independent copies of this pair for the lower rows, independent of the actual upper data conditional on $H$. The $\Xi_0$ marginal law is the same product Gaussian law for every $H$, so $\Xi_0$ is independent of $H$ as well as of all upper fields. This conditional construction does not assert that $\Xi_H$ and $H$ are independent; their covariance $T_H$ depends on $H$.

One can now perform the local coupling in Theorem 2 using these already coupled $\Xi_H$ rows. Indeed, on the support of $T_H$, the vector $T_H^{\dagger/2}\Xi_{H,i}$ is standard Gaussian, independent of the upper data conditional on $H$. It can serve as the fresh $z$ in (11), with $B=T_H$ and $A_n=T_n$. The sample covariance is supported in that same subspace almost surely. Thus the desired empirical-covariance noise $\Xi_n$ can be constructed from $\Xi_H$ without disturbing the joint coupling with $\Xi_0$. Completing $G$ by (19) preserves the exact dense program marginal.

Let $\overline X_H=HR_H+\Xi_H$. Theorem 2 gives

\[
\mathbb E\|X-\overline X_H\|_{F,n}^2
\leq M^2(2k+\ell)/n.
\tag{34}
\]

For the difference to (30), the noise is conditionally centered, so the cross term vanishes. Also $\|Q\|_{\mathrm{op}}\leq B^2$. Hence

\[
\begin{aligned}
\mathbb E[\|\overline X_H-X_0\|_{F,n}^2\mid H]
&=\operatorname{tr}[(R_H-R_0)^\top Q(R_H-R_0)]
+\mathbb E[\|\Xi_H-\Xi_0\|_{F,n}^2\mid H]\\
&\leq(B^2L_1^2+L_0^2)\delta_H^2.
\end{aligned}
\tag{35}
\]

Integrating (35), applying (28), and using the squared triangle bound with factor two together with (34) proves (31)–(32). The first two bounds in (31) follow directly from the row couplings in (28)–(29). ∎

The lower reference rows $(H_i,X_{0,i})$ are independent copies of their fixed population law. The upper reference rows $(Y_{0,i},Z_i,D_{0,i})$ are also independent copies, and the two reference populations are independent. This is the scalar Gaussian response law of this finite reciprocal program, not a reference with coefficients borrowed from a realized future dense trajectory.

## 6. Interpretation, probability level, and extensions actually justified

### 6.1. Root-width accuracy without a hidden spectral constant

For every fixed failure probability $\delta\in(0,1)$, Markov's inequality applied to (31) gives, for example,

\[
\mathbb P\{\|X-X_0\|_{F,n}>\sqrt{C_{\mathrm{block}}/(n\delta)}\}
\leq\delta.
\tag{36}
\]

Thus the normalized root-mean-square field error is $O_{\mathbb P}(n^{-1/2})$, with the displayed constants independent of spectral gaps. The theorem does not by itself give probability $1-n^{-r}$ with only polylogarithmic losses. Choosing $\delta=n^{-r}$ in (36) would lose a power, so that stronger claim would require an additional tail argument.

Means of the fields inherit the same mean-square coupling bound by Cauchy–Schwarz. For a fixed finite list of pairings, use

\[
\begin{aligned}
\left|\frac1n A^\top B-\frac1n A_0^\top B_0\right|
&\leq\|A-A_0\|_{2,n}\|B\|_{2,n}
+\|A_0\|_{2,n}\|B-B_0\|_{2,n}.
\end{aligned}
\tag{37}
\]

The reference rows here have finite moments of all needed orders: $H,D_0$ are bounded and $Y_0,X_0$ have Gaussian moments with fixed finite coefficients. Bounds (31) also bound the actual second moments. Taking expectations in (37) therefore gives $O(n^{-1/2})$ error for the coupled pairings. Independent reference-row sampling contributes an additional $O(n^{-1/2})$ expected absolute error relative to the population pairing, by the elementary variance-of-a-sample-mean identity. These last sample-pairing constants depend on fourth moments of the reference rows. To claim a uniform gap-free pairing bound for a varying circuit family, those fourth moments must also be bounded uniformly; a global uniform Lipschitz bound on $\Psi$ gives a uniform bound on $R_0$ and is one sufficient condition. The conditional hypothesis (29) alone is not used to assert an otherwise unproved fourth-moment bound.

If $k,\ell$ or circuit bounds are allowed to vary with width, (15) and (32) remain their actual bounds. Their explicit dimension dependence must then be paid. A finite-program theorem with these constants is not automatically a mesh-uniform statement.

### 6.2. An exact weighted-moment form for unbounded reverse circuits

The boundedness assumption is convenient, not an essential algebraic feature. Assume explicitly that $T$ is finite, $R$ is well defined, and the Stein identity holds. With the same independence hypotheses, define

\[
\begin{aligned}
K_H&=\mathbb E[\|Q^{\dagger/2}Y_\ast\|_2^2
\|\Psi(Y_\ast,Z_\ast)\|_2^2],\\
K_D&=\mathbb E[\|\Psi(Y_\ast,Z_\ast)\|_2^2
\Psi(Y_\ast,Z_\ast)^\top T^\dagger\Psi(Y_\ast,Z_\ast)].
\end{aligned}
\tag{38}
\]

Provided these are finite, precisely the preceding proof gives

\[
\mathbb E[\|X-\overline X\|_{F,n}^2\mid H]
\leq\frac{K_H+r_H\operatorname{tr}T+K_D-\operatorname{tr}T}{n}.
\tag{39}
\]

The last two terms arise from the nonnegative quantity in (13); the whole right-hand side is nonnegative. Under (4), $K_H\leq M^2r_H$ and $K_D\leq M^2r_D$, which recovers the simpler bound after dropping the negative trace term.

Formula (39) is a conditional route for the actual unbounded neural fields. It is not a certification that their weighted constants are uniform: a linear Gaussian value envelope alone controls ordinary moments, but does not immediately control every normalized direction represented by $T^\dagger$ uniformly over a varying circuit family. Truncation plus an explicit population tail estimate, or a direct weighted estimate, would have to be proved for that family. No clipping of the target dense program has been silently introduced here.

### 6.3. Why an unweighted covariance argument is insufficient

In one dimension, the squared optimal Gaussian coupling distance between $N(0,\varepsilon)$ and a point mass at zero is exactly $\varepsilon$, so the root-mean-square distance is $\sqrt\varepsilon$. An entrywise covariance perturbation of size $\varepsilon$ alone cannot imply a field coupling error of order $\varepsilon$, even for the identity field.

There is also no general covariance-Lipschitz weak estimate for bounded Lipschitz tests. For $a(x)=\min\{|x|,1\}$ and a standard normal $g$,

\[
\mathbb E[a(\sqrt\varepsilon\,g)]
=\sqrt\varepsilon\,\mathbb E|g|+o(\sqrt\varepsilon)
=\sqrt{2\varepsilon/\pi}+o(\sqrt\varepsilon).
\tag{40}
\]

The first asymptotic follows by dominated convergence after division by $\sqrt\varepsilon$, since $\min(|g|,\varepsilon^{-1/2})\leq|g|$. Lemma 1 succeeds because sample covariance fluctuations are controlled in their own covariance-weighted norm, not because the square-root map is uniformly Lipschitz at a singular covariance. Assumption (29) likewise makes its additional population response stability explicit instead of assuming it from covariance-entry convergence.

## 7. What this resolves, and the next unresolved step

This note proves an actual finite-program quantitative comparison, not only a formal cancellation in the limiting equations. Its response is the total derivative of the prescribed upper row circuit, with its deterministic coefficients held fixed. The primitive covariance is the full uncentered query pairing. Both singular response means and singular primitive covariances are treated directly. The constants in (15) and (32) contain no smallest positive Gram eigenvalue.

The result does not yet cover an additional forward query formed from $X=G^\top D$, followed by further alternating queries. In that next round, the lower inputs depend on the same Gaussian matrix and on the empirical covariance coupling. The relevant weighted sample fluctuations can no longer be replaced by the independent-row calculation (13) or (22) without a new argument. A same-coefficient uniform concentration estimate for bounded circuits does not, on its own, establish the required coupling stability or uniform control in covariance-normalized directions.

Similarly, empirical shared coefficients introduce dependencies not present in Section 1. They require a stability estimate for the coefficient map and for the resulting response circuit, not merely permission to freeze coefficients when taking a formal local derivative.

The next bounded proof obligation is therefore one more direction switch at this same interface, retaining exact dependent queries and estimating response errors only in the query-weighted norm. It is not an unrestricted leap from (15) to a full neural all-time theorem. Fixed nonzero labels, network depth, and physical-time restrictions have not been altered by this local result.

Scoped audit: GAP_FREE_RESPONSE_AUDIT.md reconstructs the complete frozen
proof. Its conditioning, Gaussian-completion, root-independence and
finite-moment wording corrections are incorporated here. The audit does
not certify a further adaptive round or a full-trajectory result.
