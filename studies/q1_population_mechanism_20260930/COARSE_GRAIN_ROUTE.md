# Independent route: signed geometry, exact lumping, and controlled spatial coarse-graining

Status: first independent theoretical note, 2026-09-30. Internally derived, not independently reviewed or promoted. No experiments were performed. Scientific input was only the supervisor's q1 system; no book passages, other studies, or other agents' findings were consulted.

The strongest result here is a deterministic, autonomous particle approximation of the **finite q1 system itself**, with particle count independent of sample count. Its mechanism is spatial regularity of the evolving memory fields after an exact label symmetry quotient. A sharper, width-uniform result is available for the instantaneous omitted memory covariance. A width-uniform stability theorem for the autonomous approximation remains open under only the stated Gaussian initialization.

## 1. Contract and canonical system

Inputs satisfy \(\|x\|_2=\sqrt d\), labels are \(y\in\{-1,1\}\), and the empirical data law is initially arbitrary. Write \(\mathbb E\) for its average; all statements below also admit a probability law on the input sphere. The width is \(n\). The fixed matrix \(W_0\in\mathbb R^{n\times n}\) is never replaced. Initial conditions are \(w(0)=0\), \(v_{x,y}(0)=0\), \(k_{x,y}(0)=h(0,x)\), \(\tau(0)=1\), with the supplied Gaussian laws for \(A_0,W_0\). Deterministic claims apply to every finite realization of these matrices.

For column vectors, define
\[
\begin{aligned}
h(x)&=\tanh(Ax/\sqrt d),&
M&=\mathbb E[vk^T]/n,& B&=W_0+M,\\
z(x)&=Bh(x),&g(x)&=\tanh z(x),&f(x)&=w^Tg(x)/n,\\
r(x,y)&=f(x)-y,&d(x)&=w\odot(1-g(x)^2),\\
\ell(x)&=(1-h(x)^2)\odot B^Td(x),&
\rho&=(\mathbb E r^2)^{1/2},&\alpha&=\rho/\tau.
\end{aligned}
\]
The exact equations are
\[
\dot\tau=\rho,\quad
\dot k=\alpha(h-k),\quad
\dot v=-2rd,\quad
\dot w=-2\mathbb E[rg],\quad
\dot A=-2\mathbb E[r\ell x^T/\sqrt d].
\tag{1}
\]
No dense reference flow is used. Neither moving \(A\) nor either tanh is frozen or linearized.

The approximation will retain \(A,w,\tau\), two \(n\)-vectors per retained input representative, its location, and its probability mass. Locations and masses are computed from the initial dataset/law, without observing the future trajectory. There is no time-dependent forcing, hidden full dataset after preprocessing, or uncounted learned basis. The given dense fixed mixer still costs \(n^2\) storage/operations if explicitly stored; the claim concerns **learned state**, of size \(nd+2np+n+1\), plus \(O(pd+p)\) fixed data coefficients. The guarantee is on a specified finite horizon \([0,T]\). No all-time, width-limit, or uniform-in-dimension conclusion is claimed.

Use \(\|a\|_n=\|a\|_2/\sqrt n\), \(\|A\|_{F,n}=\|A\|_F/\sqrt n\), ordinary operator/nuclear norms for matrices, and normalized input distance
\[
\operatorname{dist}(u,u')=\|u-u'\|_2/\sqrt d.
\]

## 2. An exact label quotient

**Proposition 1 (signed-input reduction).** Replace every sample \((x,y)\) by
\[
u=yx,\qquad \widetilde k=yk,\qquad \widetilde v=yv,
\tag{2}
\]
and give every transformed sample target \(+1\). Keep \(A,w,\tau,W_0\) unchanged. This is an exact conjugacy of (1). Thus the whole q1 flow, including its clock, depends on the labeled data only through the pushforward probability law
\[
\lambda=(x,y\mapsto yx)_\#\mathbb P.
\tag{3}
\]

**Proof.** For any current \(A,B,w\), oddness of tanh gives \(h(-x)=-h(x)\), \(g(-x)=-g(x)\), \(f(-x)=-f(x)\). Consequently \(d(-x)=d(x)\) and \(\ell(-x)=\ell(x)\). At \(u=yx\), the transformed residual is
\[
\widetilde r(u)=f(yx)-1=y(f(x)-y)=yr(x,y).
\]
The rank-one memory product is unchanged, \(\widetilde v\widetilde k^T=vk^T\), so \(B\) is unchanged. The \(k,v\) equations transform as
\[
\dot{\widetilde k}=\alpha(h(u)-\widetilde k),\qquad
\dot{\widetilde v}=-2\widetilde r\,d(u).
\]
Also \(\widetilde r g(u)=rg(x)\), \(\widetilde r\ell(u)u^T=r\ell(x)x^T\), and \(\widetilde r^2=r^2\). These identities verify all remaining equations and initial conditions. \(\square\)

**Exact lumpability consequence.** Equal signed inputs have equal \(h,k,v,g,r,d,\ell\) for all times by uniqueness. Their probability masses can be added. In particular, \((x,+1)\) and \((-x,-1)\) share one exact collective memory after the transformation. Arbitrary rotations do not provide an analogous fixed-realization quotient: the same realized \(A_0,W_0\) are part of the object and generally break those symmetries. Rotation invariance in distribution is insufficient for exact sample lumping.

All subsequent statements use the all-positive formulation with data law \(\lambda\); write \(r(u)=f(u)-1\).

### Complementary exact reduction for repeated inputs and label noise

Without transforming inputs, let \(\mu\) be the marginal input law and \(\eta(x)=\mathbb E[y\mid x]\). Memories \(k\) are identical at fixed \(x\) across labels, because their initial data and forcing are label-independent. Define \(\bar v(x)=\mathbb E[v\mid x]\). Then
\[
M=\int \bar v(x)k(x)^T\,\mu(dx)/n,
\qquad
\dot{\bar v}(x)=-2(f(x)-\eta(x))d(x).
\tag{4}
\]
The \(A,w\) equations use residual \(f-\eta\), while the exact clock is
\[
\rho^2=\int\big[(f-\eta)^2+1-\eta^2\big],d\mu.
\tag{5}
\]
This follows by conditional expectation in (1); it uses no closure assumption. Thus duplicated label variants at one input need only one mean \(v\), but replacing them by an ordinary soft-label loss clock discards the nonnegative term \(1-\eta^2\). The pair consisting of the marginal measure \(\mu\) and signed label measure \(\nu(dx)=\eta(x)\mu(dx)\) is sufficient information. Proposition 1 gives a different, often smaller, representation exploiting oddness.

## 3. Global bounds and pathwise spatial regularity

Fix \(T<\infty\), let \(S=\|W_0\|_{\rm op}\), \(a_0=\|A_0\|_{F,n}\), and define the nondecreasing deterministic envelopes
\[
q_t=e^{2t}-1,\quad R_t=e^{2t},\quad V_t=\tfrac12q_t^2,\quad
B_t=S+V_t,\quad a_t=a_0+SV_t+\tfrac12V_t^2.
\tag{6}
\]
Here \(B_t\) is a scalar bound, not the matrix \(B\).

**Lemma 2 (a priori bounds).** Every solution of (1) satisfies
\[
\begin{gathered}
\|h(u)\|_\infty,\|g(u)\|_\infty,\|k(u)\|_\infty\le1,\\
\|w\|_\infty\le q_t,\quad |r(u)|\le R_t,\quad \rho\le R_t,
\quad 1\le\tau\le1+q_t/2,\\
\sup_u\|v(u)\|_\infty\le V_t,\quad
\|M\|_{\rm op}\le V_t,\quad\|B\|_{\rm op}\le B_t,
\quad\|A\|_{F,n}\le a_t.
\end{gathered}
\tag{7}
\]

**Proof.** The \(k\) equation is a convex relaxation because \(\alpha\ge0\); equivalently
\[
k(t,u)=\frac{h(0,u)+\int_0^t\rho(s)h(s,u)\,ds}{\tau(t)}.
\tag{8}
\]
Writing \(b=\|w\|_\infty\), one has \(|f|\le b\), \(\rho\le1+b\), and the upper Dini derivative \(D^+b\le2(1+b)\). Integrating yields \(b\le q_t\) and the clock bound. Each coordinate obeys \(|\dot v_i|\le2R_tq_t\); since \(V_t'=2R_tq_t\), this gives the \(v\) bound. A rank-one term obeys
\(\|vk^T/n\|_{\rm op}=\|v\|_n\|k\|_n\le V_t\), which bounds \(M,B\). Finally \(\|d\|_n\le q_t\), \(\|\ell\|_n\le B_tq_t\), and
\[
\|\dot A\|_{F,n}\le2R_tB_tq_t=B_tV_t'.
\]
Integrating \((S+V_t)V_t'\) proves the last bound. \(\square\)

These estimates also give global existence. For a population law, solve the integral equations in the Banach space of continuous \(k,v\) fields on the compact input sphere, together with finite-dimensional \(A,w,\tau\). On each bounded set with \(\tau\ge1\), tanh, products, integration, and the \(L^2(\lambda)\) norm defining \(\rho\) are locally Lipschitz. Successive approximation on a sufficiently short interval is a contraction and gives a unique local solution. Bounds (7) prevent escape from every finite-time bounded set, allowing continuation. The same argument applies directly to finite data. If the law has smaller support, restriction of these continuous fields supplies its solution.

**Lemma 3 (width-controlled spatial regularity along one trajectory).** For any two signed inputs \(u,u'\),
\[
\begin{aligned}
\|h(t,u)-h(t,u')\|_n&\le a_t\operatorname{dist}(u,u'),\\
\|k(t,u)-k(t,u')\|_n&\le L_k(t)\operatorname{dist}(u,u'),\\
\|v(t,u)-v(t,u')\|_n&\le L_v(t)\operatorname{dist}(u,u'),
\end{aligned}
\tag{9}
\]
where
\[
L_k(t)=\frac{a_0+\int_0^t\rho(s)a_s\,ds}{\tau(t)}\le a_t,
\qquad
L_v(t)=\int_0^t2q_s(2+3q_s)B_sa_s\,ds.
\tag{10}
\]
There is no explicit width or sample-count factor in these bounds; dependence on initialization is through \(a_0,S\).

**Proof.** The derivative of tanh has absolute value at most one, giving
\[
\|h(u)-h(u')\|_n\le\|A\|_{F,n}\operatorname{dist}(u,u').
\]
Equation (8) gives the \(k\) bound. The same fixed matrix \(B(t)\) acts on both inputs, hence
\[
\|g(u)-g(u')\|_n\le B_ta_t\operatorname{dist}(u,u'),
\quad
|r(u)-r(u')|\le q_tB_ta_t\operatorname{dist}(u,u').
\]
Using \(|g_i^2-g_i'^2|\le2|g_i-g_i'|\),
\[
\|d(u)-d(u')\|_n\le2q_tB_ta_t\operatorname{dist}(u,u').
\]
Therefore
\[
\|\dot v(u)-\dot v(u')\|_n
\le2\big[q_t^2+2R_tq_t\big]B_ta_t\operatorname{dist}(u,u')
=2q_t(2+3q_t)B_ta_t\operatorname{dist}(u,u').
\]
Initial \(v\) vanishes, so integration gives (10). \(\square\)

The mechanism is common-input filtering and smooth forcing, not attraction to a same-label synchronized manifold. The \(k\) equation damps initial differences by \(1/\tau\), but continually receives the different nonlinear features. The \(v\) equation has no damping term at all.

## 4. Exact cluster identities and a quadratic covariance remainder

Partition signed-input space into cells \(C_j\) of mass \(\pi_j>0\), \(j=1,\ldots,p\). Let \(\mathbb E_j\) denote conditional expectation and set
\[
K_j=\mathbb E_j k,\quad U_j=\mathbb E_j v,\quad H_j=\mathbb E_j h,
\quad
\mathcal C_j=\frac1n\mathbb E_j[(v-U_j)(k-K_j)^T].
\]
Then, exactly,
\[
M=\sum_j\pi_j U_jK_j^T/n+\sum_j\pi_j\mathcal C_j,
\tag{11}
\]
\[
\dot K_j=\alpha(H_j-K_j),\qquad
\dot U_j=-2\mathbb E_j[rd].
\tag{12}
\]
If \(\operatorname{Cov}_j(X,Y)=\mathbb E_j[(X-\mathbb E_jX)(Y-\mathbb E_jY)^T]/n\), differentiation gives
\[
\dot{\mathcal C}_j
=-2\operatorname{Cov}_j(rd,k)
 +\alpha\operatorname{Cov}_j(v,h)-\alpha\mathcal C_j,
\qquad \mathcal C_j(0)=0.
\tag{13}
\]
The two covariance production terms are the exact obstruction to closing cluster means. Equation (12) also needs \(H_j\) and the nonlinear average \(\mathbb E_j[rd]\). Replacing these by center evaluations is an approximation whose error must be controlled.

**Theorem 4 (quadratic omitted-memory estimate).** Choose a representative \(c_j\) in each cell, and put
\[
\delta^2=\sum_j\pi_j\mathbb E_j\operatorname{dist}(u,c_j)^2.
\]
The rank-at-most-\(p\) matrix \(M_p^{\rm mean}=\sum_j\pi_jU_jK_j^T/n\) satisfies the nuclear-norm estimate
\[
\|M-M_p^{\rm mean}\|_*
\le L_v(t)L_k(t)\delta^2.
\tag{14}
\]
In particular the operator and Frobenius errors, and the \((p+1)\)-st singular value of \(M\), obey the same upper bound.

**Proof.** For independent conditional copies \(u,u'\),
\[
\mathcal C_j=\frac1{2n}\mathbb E_j[(v(u)-v(u'))(k(u)-k(u'))^T].
\]
The nuclear norm of the displayed rank-one matrix divided by \(n\) is the product of normalized vector norms. By (9),
\[
\|\mathcal C_j\|_*
\le\tfrac12L_vL_k\mathbb E_j\operatorname{dist}(u,u')^2
\le L_vL_k\mathbb E_j\operatorname{dist}(u,c_j)^2.
\]
For the last inequality, expand the square in Euclidean space:
\(\tfrac12\mathbb E\|u-u'\|^2=\mathbb E\|u-\mathbb Eu\|^2\le\mathbb E\|u-c_j\|^2\).
Sum with weights \(\pi_j\). The operator/Frobenius inequalities follow from each norm being bounded by the nuclear norm; the singular-value claim follows because adding an error matrix of operator norm \(\varepsilon\) to a rank-\(p\) matrix leaves its \((p+1)\)-st singular value at most \(\varepsilon\). One direct proof of the latter restricts to the kernel of the rank-\(p\) matrix, a subspace of codimension at most \(p\), and uses the min-max characterization of singular values. \(\square\)

For a circle, equal angular cells give \(\delta\le\pi/p\); hence (14) is \(O(p^{-2})\). For a fixed \((d-1)\)-sphere, spatial covering gives \(\delta=O_d(p^{-1/(d-1)})\), and the covariance error is \(O_{T,d,a_0,S}(p^{-2/(d-1)})\). This conclusion concerns the exact cluster means on the exact trajectory; it is not yet an autonomous closure theorem.

## 5. A concrete autonomous closure and its full error bound

Choose signed-input representatives and weights from the initial law, and define
\[
\widehat\lambda=\sum_{j=1}^p\pi_j\delta_{c_j}.
\tag{15}
\]
Run **the very same q1 equations (1)** on this weighted all-positive dataset, using the same \(A_0,W_0\), \(\widehat w_0=0\), \(\widehat\tau_0=1\), \(\widehat v_j(0)=0\), and \(\widehat k_j(0)=\tanh(A_0c_j/\sqrt d)\). Every average in the new equations is \(\sum_j\pi_j(\cdot)\). This is autonomous and restartable from its finite state. It preserves the nonlinear moving features and fixed mixer exactly within the reduced system.

The following theorem works with any coupling \(\gamma\) of \(\lambda,\widehat\lambda\). Denote
\[
\delta=\left(\int\operatorname{dist}(u,u')^2\,d\gamma\right)^{1/2}.
\tag{16}
\]
An input partition supplies such a coupling directly. Minimizing (16) is optional.

**Theorem 5 (finite-horizon autonomous approximation, uniform in sample count).** Let
\[
\begin{aligned}
e(t)={}&\|A-\widehat A\|_{F,n}+\|w-\widehat w\|_n+|\tau-\widehat\tau|\\
&+\left(\int\|k(u)-\widehat k(u')\|_n^2d\gamma\right)^{1/2}
+\left(\int\|v(u)-\widehat v(u')\|_n^2d\gamma\right)^{1/2}.
\end{aligned}
\tag{17}
\]
Set \(R=R_T\), \(q=q_T\), \(V=V_T\), \(a=a_T\), \(b=1+S+V\), and
\[
C=64(1+\sqrt n)(1+a)R^2b^2.
\tag{18}
\]
Then
\[
\sup_{0\le t\le T}e(t)
\le\big[(1+a_0)e^{CT}-1\big]\delta.
\tag{19}
\]
For predictions at the **same arbitrary test input** \(x\) on the sphere,
\[
\sup_{t\le T,x}|f(t,x)-\widehat f(t,x)|
\le(1+2qb)\big[(1+a_0)e^{CT}-1\big]\delta.
\tag{20}
\]
Also \(\|M-\widehat M\|_{\rm op}\le(1+V)e\). These constants are deliberately loose but completely specified. They have no dependence on \(m\), on the number of occupied cells, or on the population law. Their explicit \(\sqrt n\) dependence is a real limitation of this proof.

**Proof.** All envelopes (7) apply to both systems. Write \(A_e,w_e,K_e,V_e,\tau_e\) for the five nonnegative terms in (17). Let \(H,G,D,L\) be the \(L^2(\gamma)\) norms of the paired differences of \(h,g,d,\ell\), respectively, and let \(J\) be that of the residual difference. Directly,
\[
\begin{aligned}
H&\le A_e+a\delta,\\
\|M-\widehat M\|_{\rm op}&\le V_e+VK_e,\\
G&\le (S+V)H+V_e+VK_e,\\
J&\le w_e+qG,\qquad D\le w_e+2qG.
\end{aligned}
\tag{21}
\]
For example, split \(vk^T-\widehat v\widehat k^T=(v-\widehat v)k^T+\widehat v(k-\widehat k)^T\), integrate under the coupling, and use Cauchy-Schwarz to obtain the second line. The other inequalities follow from tanh being 1-Lipschitz, \(|\widehat w_i|\le q\), and the definition of normalized norms.

For the backpropagated field, split the difference in \((1-h^2)\odot B^Td\). Since pointwise \(\|h-\widehat h\|_\infty\le\sqrt n\|h-\widehat h\|_n\), one obtains
\[
L\le(S+V)D+q(V_e+VK_e)+2\sqrt n\,q(S+V)H.
\tag{22}
\]
This is the sole source of the explicit width loss in (18).

Differencing the five evolution equations, pairing their averages using \(\gamma\), and using \(\|u\|/\sqrt d=1\), gives upper Dini derivative inequalities
\[
\begin{aligned}
D^+A_e&\le2\{q(S+V)J+RL+Rq(S+V)\delta\},\\
D^+w_e&\le2(J+RG),\\
D^+K_e&\le RH+2(J+R\tau_e),\\
D^+V_e&\le2(qJ+RD),\\
D^+\tau_e&\le J.
\end{aligned}
\tag{23}
\]
For the \(k\) line, write the difference equation as
\[
\Delta\dot k=-\alpha\Delta k+\alpha\Delta h
+(\alpha-\widehat\alpha)(\widehat h-\widehat k).
\]
The first term decreases the squared \(L^2\) norm, the last field has norm at most two, and
\(|\alpha-\widehat\alpha|\le|\rho-\widehat\rho|+R\tau_e\le J+R\tau_e\)
because both clocks are at least one. This proves the third line, including its behavior at a zero norm by upper Dini derivatives. For the last line, the reverse triangle inequality for the residual \(L^2\) norm gives \(|\rho-\widehat\rho|\le J\).

To check the scalar constant without suppressing dependence, put \(E=e+\delta\) and \(a_+=1+a\). Equations (21)-(22) imply
\[
H\le a_+E,\quad G\le2a_+bE,\quad
J\le3a_+RbE,\quad D\le5a_+RbE,\quad
L\le(6+2\sqrt n)a_+Rb^2E.
\]
The respective five lines of (23) are bounded by
\[
(20+4\sqrt n)a_+R^2b^2E,\quad
10a_+RbE,\quad9a_+RbE,\quad16a_+R^2bE,\quad3a_+RbE.
\]
Their sum is at most \(CE\). Initially only the \(k\) comparison is nonzero, with \(e(0)\le a_0\delta\). Integrating
\(D^+e\le C(e+\delta)\)
gives (19).

For a common test input, the feature difference is at most \(A_e\), so the corresponding \(g\) difference is at most \((S+V)A_e+V_e+VK_e\le2be\). Splitting \(w^Tg-\widehat w^T\widehat g\) gives (20). The memory estimate was already obtained in (21). \(\square\)

### Consequences and the exact complexity statement

For every fixed \(n,d,T,A_0,W_0\) and desired prediction error \(\varepsilon>0\), choose a spatial net whose covering radius is
\[
\delta\le\frac{\varepsilon}
{(1+2qb)[(1+a_0)e^{CT}-1]}.
\tag{24}
\]
Map each signed input to a nearest net point and add its mass. The resulting \(p\)-particle system proves a constructive approximation statement uniformly over every sample count and every probability law on the sphere. For a circle, \(p\le\lceil\pi/\delta\rceil\) suffices using equal angular cells, with the harmless convention \(p\ge1\). For fixed \(d\ge2\), \(p=O_d(\delta^{-(d-1)})\) suffices: cover the sphere by the \(2d\) graph patches where a specified signed coordinate has magnitude at least \(1/\sqrt d\); on each patch the graph map is \(\sqrt d\)-Lipschitz, and a grid in its \(d-1\) free coordinates gives this count. For \(d=1\), the sphere contains only two points and exact merging gives \(p\le2\).

The fixed geometric net is data-independent. Only its cell masses depend on the law. Thus no learned or task-dependent uncounted function basis is being assumed. Empty cells may be omitted. The empirical preprocessing is a single data pass; thereafter only representatives and masses are used. For an abstract population law, the theorem requires access to these finitely many cell probabilities; it does not claim they can be computed without a specification or oracle for that law.

The bound proves sample-count-independent compression, not that its conservative \(p\) is small on every finite dataset. It is useful structurally for \(m\to\infty\), for clustered signed data, and for sufficiently large \(m\) at fixed accuracy/horizon. The worst-case constants can make its numerical particle count impractical. The quadratic rate (14) for the exact mean approximation is stronger than the first-order autonomous rate (19); the proof does not transfer that quadratic rate to the particle dynamics.

The population result is direct: no interchange of \(m\to\infty\) and \(n\to\infty\) is needed. Moreover, if empirical signed laws converge to a population law in normalized quadratic transport distance, (19)-(20) give convergence of their q1 flows for each fixed width and horizon.

## 6. What blocks an immediate width-uniform theorem

Equation (22) concerns a true nonlinear feedback, the change of \(1-h^2\) multiplying \(B^Td\). Spectral control of \(B\) and normalized Euclidean control of \(d\) do not, by themselves, bound the coordinates of \(B^Td\) uniformly in width.

There is a precise conditional improvement. If both flows satisfy
\[
\sup_{t\le T,u}\|B(t)^Td(t,u)\|_\infty\le J_T,
\tag{25}
\]
with a constant independent of width (it suffices to have this bound on the hatted flow in the chosen split), then (22) improves to
\[
L\le(S+V)D+q(V_e+VK_e)+2J_TH.
\tag{26}
\]
Repeating the displayed proof gives the same theorem with, for example,
\[
C_{\rm uniform}=64(1+a)R^2b^2(1+J_T),
\tag{27}
\]
which has no explicit \(n\) dependence. This is an exact conditional theorem, not evidence that (25) holds for the supplied random initialization. A bound on \(S\) alone cannot justify (25). Bounding the absolute column sums of \(W_0\) would give a deterministic estimate but loses width control for Gaussian mixers. Establishing an appropriate reachable-state replacement for (25), or avoiding the coordinate supremum by a stronger stability norm and justified moment estimates, is the decisive unresolved bridge.

The source estimate (14) does not require (25). Consequently the route distinguishes two statements that should not be conflated:

1. Along every q1 trajectory, nearby signed inputs produce nearby memory fields, and their discarded covariance is small with constants controlled by \(a_0,S,T\).
2. A separately evolving compressed q1 trajectory stays close, uniformly in width.

The first is proved here. The second is proved at fixed width, and conditionally under (25) uniformly in width. This is a source-versus-propagation distinction, not an assumed low-rank explanation.

## 7. Counterexamples to label-only synchronization and careless closure

### Same label does not imply the same memory forcing

Take \(n=1,d=2\), equal sample masses, \(x_1=\sqrt2e_1\), \(x_2=\sqrt2e_2\), both labels \(+1\), \(A_0=(a,b)\) with \(0<a<b\), and \(W_0=c>0\). This is an open positive-probability set under the prescribed Gaussian initialization. Put
\[
h_i=\tanh(A_{0,i}),\quad g_i=\tanh(ch_i),\quad s=g_1+g_2>0.
\]
At time zero, \(\dot w(0)=s\), \(\dot v_i(0)=0\), and differentiation of \(\dot v_i=-2r_iw(1-g_i^2)\) gives
\[
\ddot v_i(0)=2s(1-g_i^2),\qquad
v_i(t)=s(1-g_i^2)t^2+O(t^3).
\tag{28}
\]
Since \(g_1^2\ne g_2^2\), the two memory values separate at order \(t^2\) despite identical labels and identical initial \(v\). Also \(k_i(0)=h_i\) are already different. If both samples are merged into one cluster, its omitted covariance satisfies
\[
\mathcal C(t)=\tfrac14s\big[(1-g_1^2)-(1-g_2^2)\big](h_1-h_2)t^2+O(t^3),
\tag{29}
\]
which is nonzero. Thus the manifold “one memory per label” is not invariant, even at width one, and covariance is generated immediately from a perfectly zero \(v\)-covariance initial condition.

### Antipodal data do not automatically share a label mode

If signed-input law \(\lambda\) is centrally symmetric, then \(\mathbb E g(0,u)=0\) by oddness. The exact solution is
\[
w(t)=0,\quad v(t,u)=0,\quad A(t)=A_0,\quad
k(t,u)=h(0,u),\quad\rho(t)=1,\quad\tau(t)=1+t.
\tag{30}
\]
Substituting in every equation verifies this, and uniqueness identifies the trajectory. In the original representation this includes equal masses of opposite labels at the same input. Collapsing the label noise to soft target zero while also replacing the clock by \(\|f-\eta\|_{L^2}\) would predict \(\rho=0\), contradicting (30). The clock discrepancy matters whenever the same reduction is used in a larger system with nonzero evolving memories.

### Exact rank is not an autonomous sufficient statistic

Even if \(M\) is known exactly, the individual fields enter its derivative:
\[
\dot M=-2\mathbb E[rd\,k^T]/n
+\alpha\mathbb E[vh^T]/n-\alpha M.
\tag{31}
\]
The two cross-moments are not determined by \(M\) as an algebraic matter. Likewise cluster means require (12)-(13). Thus a spectral rank bound, an SVD of the realized \(M(t)\), or the exact mean representation in (11) does not alone define a restartable reduced model. The weighted q1 system in Section 5 supplies such a model and pays an explicit stability error.

## 8. Claim ledger and next bottleneck

| Claim | Status | Exact boundary |
|---|---|---|
| Binary labels can be absorbed into signed inputs | Proved, exact | Uses odd tanh architecture with no biases and the supplied equations |
| Identical signed inputs lump with summed mass | Proved, exact | Finite realization, same fixed mixer |
| Label variants at one input reduce to mean label plus noise contribution to clock | Proved, exact | Equations (4)-(5), not an ordinary soft-label clock |
| Same-label samples synchronize | False as a general claim | Explicit positive-probability initialization counterexample (28) |
| Nearby signed inputs have nearby moving memory fields | Proved | Compact-time bounds (9)-(10), no frozen features |
| Exact cluster mean memory has rank \(\le p\), quadratic covariance error | Proved | Nuclear bound (14); exact means themselves are not autonomous |
| Weighted \(p\)-sample q1 is an autonomous approximation independent of \(m\) | Proved at fixed width | Full state/prediction estimates (19)-(20) |
| Same autonomous approximation has width-uniform stability | Conditional/open | Proved under (25); Gaussian reachable-state justification absent |
| Small practical \(p\) for all distributions or all time | Unsupported | Curse of input dimension and large finite-horizon constants remain |
| Compression demonstrates an emergent universal task mode | Not established | Proven mechanism is signed spatial regularity, not label synchronization |

The highest-leverage next theoretical step is a reachable-state estimate for the nonlinear backpropagated field in (25), or a stability argument controlling the same product without coordinate maxima. This would decide whether the constructive population approximation can be made uniform in width. It should preserve the same Gaussian mixer, both moving nonlinear layers, and the actual q1 clock; replacing any of those would answer a different question.
