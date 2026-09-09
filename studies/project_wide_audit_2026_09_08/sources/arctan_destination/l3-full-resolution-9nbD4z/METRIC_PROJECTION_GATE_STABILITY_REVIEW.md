# Independent hostile proof-only audit

## Current verdict

**PASS for the complete revised candidate at SHA-256 713f889141f56ee900c49e9b4478133035d8de7dd0156680869a73761a9b647a. No required fixes remain.**

This verdict covers the entire file: the general fixed-SPD diagonal iff global-Lipschitz classification, the fixed-width canonical embedding, the complete width-varying state construction in all of Section 5, and its normalization and general-radius limitations. It is not restricted to the leading two-coordinate example.

The revised file was read completely and rechecked. It now explicitly states “For \(u\in K_R\)” before the optimality biconditional (1). All projection candidates used later satisfy this condition, and the complete argument passes with no scope or result change. This remains an algebraic state/mapping audit, with no trajectory, initialization-probability, reachability, or actual-flow conclusion.

## Superseded provenance: original literal FAIL, correction verified

The earlier literal FAIL applied only to candidate SHA-256

0f3dde70860be93fccfba9b1cf837fa68a69472bbfb2bb3a9a41d7d02e4ea428

That version omitted an explicit feasibility qualification in (1). The user corrected the sentence immediately before (1), on line 20 of the revised candidate, to include “For \(u\in K_R\)”. The auditor did not edit the candidate.

The revision identity was independently checked: replacing only the literal phrase “For \(u\in K_R\), its optimality condition is” by the original “Its optimality condition is” in a read-only stream reproduced SHA-256 0f3dde70860be93fccfba9b1cf837fa68a69472bbfb2bb3a9a41d7d02e4ea428. The complete revised file itself hashes to 713f889141f56ee900c49e9b4478133035d8de7dd0156680869a73761a9b647a. Thus no other candidate content changed.

The revised, qualified statement (1) is equivalent to the following fully explicit form:

\[
u=P_M(d)
\quad\Longleftrightarrow\quad
\left[
u\in K_R
\ \text{and}\
\langle M(u-d),v-u\rangle\geq0
\quad\text{for every }v\in K_R
\right].
\tag{1-corrected}
\]

For historical clarity, without that qualification one can choose \(n=1\), \(M=[1]\), and \(u=d=2R\). The inequality is then zero for every \(v\in[-R,R]\), whereas \(P_M(d)=R\ne u\). This counterexample to the old unrestricted equivalence is excluded by the revised domain \(u\in K_R\). Every actual application of (1) checks that its proposed \(u\) is in the box. The formal defect is resolved and is not a current failure.

The original literal FAIL is preserved here solely as superseded provenance. The current verdict is PASS.

## Scope, identity, and method

The candidate audited in full is:

/tmp/l3-supervisor-recovery-59x8oL/l3-full-resolution-9nbD4z/METRIC_PROJECTION_GATE_STABILITY_TEST.md

Its revised SHA-256, independently computed before rereading the complete revised contents, is

713f889141f56ee900c49e9b4478133035d8de7dd0156680869a73761a9b647a

The skill /etc/codex/skills/solve-math-rigorously/SKILL.md was read completely first. The only mathematical source then read was the specified candidate, first at its original hash and subsequently in its entirety at the revised hash. This report uses direct algebra, differentiation, finite-dimensional quadratic minimization, and elementary limits. There were no experiments, numerical simulations, external sources, inherited reviews, ledgers, repository operations, source-task operations, or energy arguments. The revision comparison used only read-only text substitution and hashing.

The object audited is the projection of the raw backward field defined in (23), with the residual excluded. The full-state distance is precisely (49). “Complete state” refers to the network equations (22)–(23), with independently specified parameter values at each endpoint; it does not add any initialization, training, trajectory, or probability constraint.

The reconstruction below checks the general fixed-SPD classification, both fixed-width counterexamples, the entire width-varying construction, the exact active sets, every stated forward and backward relation, all asserted bounds, and both normalization limitations. It also computes a positive finite limit for \(nD_n\), strengthening the candidate's order estimate and checking all nonzero terms in that distance separately.

## 1. Projection optimality, the valid signal estimate, and the two-coordinate formula

Write

\[
J_d(u)=\tfrac12(u-d)^TM(u-d),\qquad
P_M(d)=\mathop{\rm argmin}_{u\in[-R,R]^n}J_d(u).
\]

For \(R>0\) the box is nonempty and compact. The objective is continuous, so it attains its minimum. For distinct \(u,v\) and \(0<s<1\),

\[
J_d((1-s)u+sv)
=(1-s)J_d(u)+sJ_d(v)
-\tfrac12s(1-s)(u-v)^TM(u-v),
\]

and the subtracted quantity is strictly positive. Thus the minimizer is unique.

For a feasible minimizer \(u\), differentiating \(J_d(u+s(v-u))\) at \(s=0+\) yields the inequality in (1-corrected). Conversely, for feasible \(u,v\),

\[
J_d(v)-J_d(u)
=\langle M(u-d),v-u\rangle
+\tfrac12(v-u)^TM(v-u).
\]

The inequality together with feasibility implies minimality and uniqueness. Feasibility is now explicitly required immediately before (1); the only omission identified in the superseded version is resolved.

Let \(u=P_M(d)\), \(\widetilde u=P_M(\widetilde d)\), \(e=u-\widetilde u\), and \(r=d-\widetilde d\). The two variational inequalities give

\[
e^TMe\leq r^TMe.
\]

Cauchy–Schwarz for the inner product \(\langle a,b\rangle_M=a^TMb\) gives

\[
e^TMe\leq(r^TMr)^{1/2}(e^TMe)^{1/2}.
\]

If \(e=0\), the required estimate is immediate. Otherwise division gives \(e^TMe\leq r^TMr\). With \(cI\preceq M\preceq CI\),

\[
\|P_M(d)-P_M(\widetilde d)\|_2
\leq\sqrt{C/c}\,\|d-\widetilde d\|_2.
\]

The metric is identical on the two sides of this comparison. Since the diagonal multiplier \(\phi'(z)\) has entries in \((0,1]\), (3) follows with constant \(\sqrt{C/c}\), independently of dimension. The larger constant \(C/c\) is also valid because \(C/c\geq1\). There is no assertion here about two different metrics.

For the two-coordinate formula, write

\[
M=\begin{pmatrix}\alpha&b\\b&m\end{pmatrix}\succ0,\quad
\beta=b/m,\quad S=\alpha-b^2/m.
\]

Here \(m>0\), and evaluating the quadratic form on \((1,-b/m)\) proves \(S>0\). If \(d_1>R\) and \(w=d_2+\beta(d_1-R)\in(-R,R)\), then \(u=(R,w)\) is feasible and

\[
u-d=(R-d_1,-\beta(R-d_1)),\qquad
M(u-d)=(S(R-d_1),0).
\]

For every feasible \(v\), both \(S(R-d_1)<0\) and \(v_1-R\leq0\), so their product is nonnegative. Hence \(u=P_M(d)\). This calculation is exact; it uses no comparison between an inverse-matrix entry and a reciprocal diagonal entry. It also works when \(b<0\), provided the explicitly stated free-coordinate condition holds.

Boundary attacks: the lemma deliberately assumes strict inequalities. The same formula can still be valid at some equality cases, but none is needed. Every subsequent construction verifies its strict conditions rather than assuming that an active set persists in a limit.

## 2. Fixed two-dimensional counterexample and general diagonal classification

### 2.1 The explicit fixed matrix

For \(0<c<C\), let \(m=(C+c)/2\), \(b=(C-c)/2\), and \(\beta=b/m\). The vectors \((1,1)\) and \((1,-1)\) have eigenvalues \(m+b=C\) and \(m-b=c\), respectively. Thus the spectral interval is exact and \(\beta\in(0,1)\).

With \(z=(1,0)\) and \(q_t=(2Rt,-\beta R(t-1))\),

\[
d=(Rt,-\beta R(t-1)).
\]

The first coordinate exceeds \(R\) for \(t\geq2\), and the candidate free coordinate is zero. The projection is \((R,0)\).

At \(\widetilde z_t=(1+1/t,0)\), put

\[
D_t=1+1/t+1/(2t^2),\qquad
k_t=\frac{1+1/(2t)}{D_t}.
\]

Then

\[
\widetilde d_1=\frac{Rt}{D_t}=Rt-Rk_t,\qquad
\widetilde d_2=-\beta R(t-1).
\]

The identity follows from \(t(D_t-1)=1+1/(2t)\). Since \(D_t-(1+1/(2t))=1/(2t)+1/(2t^2)>0\), one has \(0<k_t<1\) and \(k_t\to1\). Therefore

\[
\widetilde d_1>R(t-1)\geq R,\qquad
\widetilde d_2+\beta(\widetilde d_1-R)=-\beta Rk_t\in(-R,0).
\]

The projection is exactly \((R,-\beta Rk_t)\), including at \(t=2\). The input distance is \(1/t\), because the two signals are equal. The quotient is \(\beta Rt k_t\to\infty\).

This is a failure for a single fixed, well-conditioned matrix, not a comparison of varying metrics. It establishes the claimed counterexample for every fixed \(R>0\) and every nontrivial prescribed spectral interval \(c<C\).

### 2.2 Diagonal sufficiency

When \(M\) is diagonal with positive entries, the minimization separates into scalar minimizations. Each coordinate is

\[
H(z,q)=\operatorname{clip}_{[-R,R]}\!\left(\frac{q}{1+z^2}\right).
\]

For fixed \(q\), this function is locally absolutely continuous in \(z\). At an unsaturated point,

\[
|\partial_zH|
=\frac{2|z|}{1+z^2}\left|\frac{q}{1+z^2}\right|
\leq R.
\]

On each open saturated interval the derivative is zero. Equality \(|q|/(1+z^2)=R\) occurs at at most two points for fixed \(q\), since \(R>0\), so these boundary points cause no gap in the almost-everywhere derivative argument. Integrating gives \(|H(z,q)-H(\widetilde z,q)|\leq R|z-\widetilde z|\). For fixed \(z\), clipping is 1-Lipschitz and the multiplier \(1/(1+z^2)\leq1\), giving the scalar signal bound.

Applying these two bounds coordinatewise gives the vector bounds \(R\|\Delta z\|_2\) and \(\|\Delta q\|_2\). The triangle inequality and then scalar Cauchy–Schwarz yield

\[
\|F_M(z,q)-F_M(\widetilde z,\widetilde q)\|_2
\leq R\|\Delta z\|_2+\|\Delta q\|_2
\leq\sqrt{R^2+1}\sqrt{\|\Delta z\|_2^2+\|\Delta q\|_2^2}.
\]

No dependence on the sizes of the positive diagonal entries is needed. This covers dimension one and the case \(c=C\), since those spectral bounds force \(M=cI\).

### 2.3 Necessity for every non-diagonal SPD matrix

Suppose a fixed SPD matrix has an off-diagonal entry. Choose an index \(i\) for which \(M_{Fi}\ne0\), with \(F\) its complement. For every nonzero \(w\) supported on \(F\), \(w^TM_{FF}w>0\); hence \(M_{FF}\) is invertible. Define

\[
v=M_{FF}^{-1}M_{Fi}\ne0,\qquad
S=M_{ii}-M_{iF}M_{FF}^{-1}M_{Fi}.
\]

The vector with coordinates \((1,-v)\) is nonzero, and its quadratic form under \(M\) is \(S\), proving \(S>0\). No sign or size assumption on individual entries of \(v\) is used.

For \(t>1\), choose \(z_i=1\), \(z_F=0\), \(q_i=2Rt\), and \(q_F=-vR(t-1)\). The proposed projection \(u_i=R,u_F=0\) is feasible, and its gradient is \(S(R-Rt)\) in coordinate \(i\) and zero in every coordinate of \(F\). Thus it is the unique projection.

Keep this signal fixed and perturb \(z_i\) to \(1+h\). Write

\[
d_i(h)=\frac{2Rt}{1+(1+h)^2},\qquad
w_F(h)=d_F+v(d_i(h)-R).
\]

At \(h=0\), \(d_i(0)>R\) and \(w_F(0)=0\). For this fixed \(t\), continuity gives an open interval on which \(d_i(h)>R\) and every coordinate of \(w_F(h)\) lies strictly in \((-R,R)\). The same gradient computation verifies the full projection on that interval. Since \(d_i'(0)=-Rt\),

\[
\frac{d}{dh}u_F(h)\bigg|_{h=0}=-Rt\,v.
\]

A joint global Lipschitz constant would bound the derivative along this unit-speed input line, so would satisfy \(L\geq Rt\|v\|_2\) for every \(t>1\). This is impossible. The permitted interval in \(h\) need not be uniform in \(t\); the argument uses a derivative at each fixed \(t\), which is enough to contradict a global constant.

Thus the claimed iff classification holds for every fixed SPD matrix, not just for matrices having an isolated two-dimensional block.

### 2.4 Bounded-signal and radius limitations

For \(g=\phi'\), \(|g'|=|\phi''|\leq1\), and

\[
g(z)\odot q-g(\widetilde z)\odot\widetilde q
=(g(z)-g(\widetilde z))\odot q
+g(\widetilde z)\odot(q-\widetilde q).
\]

If both signals have coordinate bounds \(Q\), its norm is at most \(Q\|\Delta z\|_2+\|\Delta q\|_2\). Applying the fixed-metric projection estimate proves (11). In particular the mapping is locally Lipschitz for fixed dimension and fixed metric. A bound on signal RMS alone does not provide such a width-independent \(Q\).

For \(R=0\), the box is the singleton zero and the projection is constant, so the classification must be restricted to \(R>0\), as it is. For \(R<0\), the stated interval does not define a nonempty box. These cases do not supply counterexamples to the actual theorem.

## 3. Fixed-width canonical embedding, including feedforward consistency

Let \(c_0=\pi/4\) and

\[
B=\begin{pmatrix}0&4/\pi\\-2/\pi&2/\pi\end{pmatrix}.
\]

At \(z^{(1)}=(1,1)\), \(h^{(1)}=c_0(1,1)\), \(c_1=\|h^{(1)}\|_2^2/2=c_0^2\), and the squared gate matrix is \(I/4\). For the rotation \(Q_\theta\) in the candidate and \(W^{(2)}=BQ_\theta\),

\[
M^{(2)}=c_0^2I+\tfrac14BQ_\theta Q_\theta^TB^T
=c_0^2I+\frac1{\pi^2}
\begin{pmatrix}4&2\\2&2\end{pmatrix}.
\]

Thus column rotation preserves the mobility exactly because this lower gate is scalar. This is not a claimed invariance for non-scalar lower gates.

The added block has trace \(6/\pi^2\), determinant \(4/\pi^4\), and eigenvalues \((3\pm\sqrt5)/\pi^2\). Consequently the two spectral bounds in (15) and the operator-norm identity

\[
\|W^{(2)}\|_{\rm op}^2=4(3+\sqrt5)/\pi^2
\]

are exact. The free-coordinate coefficient is

\[
\beta=\frac{2/\pi^2}{c_0^2+2/\pi^2}
=\frac{32}{\pi^4+32}\in(0,1).
\]

Multiplying out the forward relation gives

\[
BQ_\theta c_0(1,1)^T
=(\cos\theta+\sin\theta,\sin\theta)^T.
\]

At \(\theta=0\) and \(\theta=1/t\), with the common signal from (6), set \(s=\sin(1/t)\), \(r=\cos(1/t)\). The rare raw input at the second state is

\[
d_1=\frac{Rt}{1+sr},\qquad
d_2=-\frac{\beta R(t-1)}{1+s^2}.
\]

Indeed \((r+s)^2=1+2sr\). Subtracting the base values gives \(\Delta d_1=-RA_t\), \(\Delta d_2=\beta RB_t\), with \(A_t,B_t\) as defined in the candidate. Therefore the free projected coordinate is exactly \(\beta R(B_t-A_t)\).

For \(t\geq2\), \(0<s<1/t\), \(0<r<1\), and hence \(0<sr<1/t\). It follows that

\[
d_1>\frac{Rt^2}{t+1}>R,\quad
0<A_t<1,\quad
0<B_t<(t-1)/t^2<1.
\]

Thus \(|\beta(B_t-A_t)|<\beta<1\). All projection conditions hold at every indicated endpoint, not just eventually. The limits \(A_t\to1\), \(B_t\to0\) follow from \(t\sin(1/t)\to1\), \(r\to1\), and the displayed bound on \(B_t\).

For the input difference, \(t(r-1)\to0\) and \(ts\to1\), giving

\[
t\|\Delta z^{(2)}\|_2\to\sqrt2.
\]

The output distance tends to \(\beta R\), so (21) is correct. If the varying weight is added to the input norm,

\[
(Q_\theta-I)^T(Q_\theta-I)=4\sin^2(\theta/2)I
\]

implies \(\|\Delta W^{(2)}\|_F\leq\|B\|_F/t\). The enlarged distance still tends to zero at rate at most \(1/t\). The lower state and the signal are unchanged. Section 4 therefore proves its whole stated claim, while correctly leaving the upper signal arbitrary at this stage.

## 4. Width-varying lower state: exact geometry and scales

In the remaining reconstruction, \(R=1\), \(n\geq4\), \(m=n-2\), and \(\rho=1/4\), unless explicitly rescaled.

### 4.1 Rotation, forward state, and fixed mobility

The vectors \(a=(0,0,1,\ldots,1)^T/\sqrt m\) and \(b=e_2\) are orthonormal. Relative to the ordered basis \((a,b)\), the map in (24) has matrix

\[
\begin{pmatrix}\cos\alpha&-\sin\alpha\\
\sin\alpha&\cos\alpha\end{pmatrix}.
\]

It is orthogonal on that plane and is the identity on its orthogonal complement. In particular it fixes \(e_1\). Applying it to
\(\mathbf1_n=e_1+b+\sqrt m\,a\) gives

\[
Q_\alpha\mathbf1_n
=e_1+(\cos\alpha+\sqrt m\sin\alpha)b
+(\sqrt m\cos\alpha-\sin\alpha)a.
\]

Multiplication by \(c_0\operatorname{blockdiag}(B,I_m)\) yields

\[
z^{(2)}(\alpha)
=\left(L_n(\alpha),\frac{L_n(\alpha)-1}{2},
c_0T_n(\alpha),\ldots,c_0T_n(\alpha)\right)^T,
\]

with exactly the \(L_n,T_n\) in (25). Both the sign of the rotation and the factor \(1/2\) in the second rare coordinate are correct.

The first layer is \(z^{(1)}=\mathbf1_n\), \(h^{(1)}=c_0\mathbf1_n\), so \(c_1=c_0^2\) and its squared gate is \(I_n/4\). Consequently

\[
M_n=c_0^2I_n+\tfrac14W^{(2)}_0(W^{(2)}_0)^T
\]

is independent of the rotation. It is the rare block (14) together with the bulk block \((c_0^2+1/4)I_m\), with no rare-to-bulk coupling. The rotation mixes columns, but orthogonality removes it before this product is formed.

The singular values of \(W^{(2)}_0\) are those of \(B\) and the value 1. Thus the operator norm \(K_2\), the spectrum in (27), and the spectral bounds in that display are correct and independent of \(n\). The lower bound \(c_0^2\) is deliberately nonsharp but positive.

### 4.2 Small-angle estimates and ordinary Frobenius distance

At \(\alpha_n=1/n\), write \(x=x_n=L_n(1/n)-1\) and \(T=T_n(1/n)\). The identity \(1-\cos u=\sin u\tan(u/2)\) gives

\[
x=\sin(1/n)\left(\sqrt m-\tan(1/(2n))\right)>0.
\]

For positivity, \(\sqrt m\geq\sqrt2\) and \(\tan(1/(2n))\leq\tan(1/8)<1\). Also

\[
x<\sqrt m/n<1/\sqrt n,\qquad \sqrt n\,x\to1.
\]

The last limit follows by separating \(\sqrt n(\cos(1/n)-1)\to0\) from \(\sqrt{nm}\sin(1/n)\to1\).

Both \(1-\cos(1/n)\) and \(\sin(1/n)/\sqrt m\) are positive, so \(T<1\), and

\[
0<1-T\leq\frac1{2n^2}+\frac1{n\sqrt m}.
\]

At \(n\geq4\), the right-hand side is less than \(1/32+1/4<1\), proving \(T>0\). This establishes all assertions in (28).

Let \(P=aa^T+bb^T\). On the rotation plane,

\[
(Q_\alpha-I)(Q_\alpha-I)^T=4\sin^2(\alpha/2)P.
\]

Using cyclicity of the finite-dimensional trace,

\[
\begin{aligned}
\|\Delta W^{(2)}\|_F^2
&=4\sin^2(1/(2n))
\left(\|W^{(2)}_0a\|_2^2+\|W^{(2)}_0b\|_2^2\right)\\
&=4\sin^2(1/(2n))(1+20/\pi^2).
\end{aligned}
\]

Here \(W^{(2)}_0a=a\), while \(W^{(2)}_0b\) has first two entries \(4/\pi,2/\pi\). Hence (29) is exact in ordinary, unnormalized Frobenius norm and

\[
n\|\Delta W^{(2)}\|_F\to a_*:=\sqrt{1+20/\pi^2}>0.
\]

This is the step that prevents an erroneous extra factor \(\sqrt n\).

The second-layer difference is \((x,x/2,c_0(T-1),\ldots,c_0(T-1))\), so

\[
\|\Delta z^{(2)}\|_2^2=\tfrac54x^2+mc_0^2(T-1)^2.
\]

The bulk norm satisfies

\[
\sqrt m\,c_0|T-1|
\leq c_0\left(\frac{\sqrt m}{2n^2}+\frac1n\right)=O(n^{-1}).
\]

Thus \(n\|\Delta z^{(2)}\|_2^2\to5/4\), proving (30), and activation Lipschitz continuity proves the stated upper bound for \(\Delta h^{(2)}\). More precisely, differentiation at the two rare base coordinates gives

\[
\sqrt n\,\Delta h^{(2)}_1\to\tfrac12,\quad
\sqrt n\,\Delta h^{(2)}_2\to\tfrac12,\quad
n\|\Delta h^{(2)}\|_2^2\to\tfrac12.
\tag{A}
\]

The bulk contribution to the last limit vanishes by the preceding bound. This additional identity will check the full distance, including activations.

## 5. Width-varying projection: full active-set verification

The common query is

\[
q_n^{(2)}=(2\sqrt n,-\beta(\sqrt n-1),\rho,\ldots,\rho)^T.
\]

Its squared RMS is exactly

\[
\frac{\|q_n^{(2)}\|_2^2}{n}
=4+\beta^2(1-1/\sqrt n)^2+\rho^2(1-2/n)
\leq4+\beta^2+\rho^2.
\]

At the base point, the first two raw coordinates are \((\sqrt n,-\beta(\sqrt n-1))\). The first is greater than 1, and the free-coordinate expression is zero. All bulk raw coordinates equal \(\rho/(1+c_0^2)\in(0,1)\). Thus the claimed full base projection is exact.

At the perturbed point, the coordinates \(z_1^{(2)}=1+x\), \(z_2^{(2)}=x/2\), \(z_j^{(2)}=c_0T\) give

\[
d_1=\frac{\sqrt n}{1+x+x^2/2}=\sqrt n-A_n,
\]
\[
d_2=-\frac{\beta(\sqrt n-1)}{1+x^2/4}
=-\beta(\sqrt n-1)+\beta E_n,\qquad
d_j=\frac{\rho}{1+c_0^2T^2}\quad(j\geq3).
\]

The factor of two in the first raw coordinate cancels exactly against \(1+(1+x)^2=2(1+x+x^2/2)\). The definitions of \(A_n,E_n\) in the candidate therefore give the exact identity

\[
d_2+\beta(d_1-1)=\beta(E_n-A_n).
\]

For every \(n\geq4\), positivity of \(x\) implies \(A_n,E_n>0\), and

\[
\frac{A_n}{\sqrt n\,x}
=\frac{1+x/2}{1+x+x^2/2}<1,\qquad
E_n<\frac{\sqrt n\,x^2}{4}<\frac1{4\sqrt n}.
\]

Thus \(A_n<1\), \(E_n<1\), and

\[
d_1=\sqrt n-A_n>\sqrt n-1\geq1,\qquad
|\beta(E_n-A_n)|<\beta<1.
\]

The first inequality remains strict at the smallest permitted width \(n=4\). In the rare block, the first gradient component is \(S(1-d_1)<0\), while the second is zero. The second projected coordinate has distance greater than \(1-\beta\) from either boundary. In the bulk, \(0<d_j\leq\rho<1\), so the projected value equals \(d_j\), its gradient component is zero, and its distance from the upper boundary is at least \(1-\rho\). The mobility has no coupling between these blocks. These checks verify the corrected variational inequality in all \(n\) coordinates and prove both vectors in (35).

For the asymptotic separation, \(\sqrt n\,x\to1\) and \(x\to0\) give \(A_n\to1\); the displayed estimate gives \(E_n\to0\). The two-coordinate projected difference is \((0,\beta(E_n-A_n))\), of norm tending to \(\beta\).

For completeness,

\[
|\phi''(s)|=\frac{2|s|}{(1+s^2)^2}\leq1,
\]

because \(2|s|\leq1+s^2\). Hence the bulk projected difference has ordinary Euclidean norm at most

\[
\sqrt m\,\rho c_0|T-1|
\leq\rho c_0\left(\frac{\sqrt m}{2n^2}+\frac1n\right)=O(n^{-1}).
\]

The disjoint coordinate supports give the exact decomposition

\[
\|\Delta u_R^{(2)}\|_2^2
=\beta^2(E_n-A_n)^2
+m\rho^2\left(\frac1{1+c_0^2T^2}-\frac1{1+c_0^2}\right)^2.
\]

Therefore \(\|\Delta u_R^{(2)}\|_2\to\beta>0\), and its RMS is asymptotic to \(\beta/\sqrt n\), as claimed. There is no hidden scalar-inverse estimate, no reliance on a merely limiting active set, and no cancellation between rare and bulk contributions to this norm.

## 6. Complete upper layers and all forward/backward relations

### 6.1 Third-layer matrix and exact signal realization

Let

\[
v_n=(2,-\beta(1-1/\sqrt n),0,\ldots,0)^T,\qquad
e=\mathbf1_n/\sqrt n,
\]
\[
W^{(3)}=\rho P_{\rm bulk}+ev_n^T.
\]

Since \(\|e\|_2=1\), the rank-one matrix has operator norm \(\|v_n\|_2\). The triangle inequality gives

\[
\|W^{(3)}\|_{\rm op}
\leq\rho+\|v_n\|_2
\leq\rho+\sqrt{4+\beta^2}=K_3.
\]

The first summand has nonzero entries only in columns \(3,\ldots,n\), and the second only in columns 1 and 2. Their Frobenius inner product is zero. Thus

\[
\|W^{(3)}\|_F^2
=\rho^2m+\|v_n\|_2^2,
\]

which verifies (38)–(39). Disjoint column support is used for the Frobenius identity only; it is not being misused to assert orthogonality of the ranges.

For each endpoint, first compute \(z^{(3)}=W^{(3)}h^{(2)}\) and then choose the parameter values

\[
W_i^{(4)}=1+(z_i^{(3)})^2.
\]

These choices are consistent: the third preactivation depends on \(W^{(1)},W^{(2)},W^{(3)}\), not on the readout, so there is no circular definition. The two readouts need not coincide; their distance must be included, and is included below.

At a specified endpoint, the readout is held fixed in partial differentiation. Therefore

\[
\delta_i^{(3)}
=W_i^{(4)}\phi'(z_i^{(3)})
=\frac{1+(z_i^{(3)})^2}{1+(z_i^{(3)})^2}=1
\]

exactly, and

\[
(W^{(3)})^T\delta^{(3)}
=\rho P_{\rm bulk}\mathbf1_n+\sqrt n\,v_n
=q_n^{(2)}.
\]

This verifies both the rare coordinates and every bulk coordinate of (41) at both endpoints. In particular, \(\Delta\delta^{(3)}=\Delta q^{(2)}=0\) exactly.

### 6.2 Explicit full forward values

The input is \(x=1\) and \(W^{(1)}=\mathbf1_n\), so \(z^{(1)}=W^{(1)}x=\mathbf1_n\) and \(h^{(1)}=c_0\mathbf1_n\). The already checked rotation gives \(z^{(2)}=W^{(2)}h^{(1)}\) and \(h^{(2)}=\phi(z^{(2)})\).

Writing

\[
\tau_n(\alpha)=
\frac{2\phi(L_n(\alpha))
-\beta(1-1/\sqrt n)\phi((L_n(\alpha)-1)/2)}{\sqrt n},
\quad
H_n(\alpha)=\phi(c_0T_n(\alpha)),
\]

direct multiplication by \(W^{(3)}\) gives

\[
z_i^{(3)}(\alpha)=\tau_n(\alpha)\quad(i=1,2),\qquad
z_j^{(3)}(\alpha)=\tau_n(\alpha)+\rho H_n(\alpha)\quad(j\geq3).
\]

The bulk diagonal term contributes nothing to the first two rows and contributes \(\rho h_j^{(2)}\) to each bulk row. This verifies every coordinate of (42). Then \(h^{(3)}=\phi(z^{(3)})\) and \(f=(W^{(4)})^Th^{(3)}/n\) finish all forward equations.

### 6.3 Partial derivatives and normalization

Treat all four weights as independent network parameters when computing derivatives at either endpoint. From \(f=(W^{(4)})^Th^{(3)}/n\), the chain rule gives

\[
n\nabla_{h^{(3)}}f=W^{(4)},\qquad
n\nabla_{z^{(3)}}f=W^{(4)}\odot\phi'(z^{(3)})=\delta^{(3)},
\]
\[
n\nabla_{h^{(2)}}f=(W^{(3)})^T\delta^{(3)}=q^{(2)},\qquad
n\nabla_{z^{(2)}}f=\phi'(z^{(2)})\odot q^{(2)}=d^{(2)}.
\]

These are precisely the three derivative identities following (23). There is no missing factor of \(n\) in the declared raw-field convention.

One can also complete the ordinary chain to the first layer, without imposing any new assumptions. Define \(q^{(1)}=(W^{(2)})^Td^{(2)}\) and \(d^{(1)}=\phi'(z^{(1)})\odot q^{(1)}=\tfrac12q^{(1)}\). Then

\[
n\nabla_{h^{(1)}}f=q^{(1)},\qquad
n\nabla_{z^{(1)}}f=d^{(1)}.
\]

The parameter derivatives are

\[
\nabla_{W^{(4)}}f=h^{(3)}/n,\quad
\nabla_{W^{(3)}}f=\delta^{(3)}(h^{(2)})^T/n,\quad
\nabla_{W^{(2)}}f=d^{(2)}(h^{(1)})^T/n,\quad
\nabla_{W^{(1)}}f=d^{(1)}x/n.
\]

Thus there is no missing lower-layer consistency condition in the ordinary backward chain. These derivative identities do not assert that the projected field is an ordinary derivative.

Differentiating the identity \(W^{(4)}=1+(z^{(3)})^2\) along the constructed family would instead compute a total derivative involving changes in a parameter. That is a different operation. The candidate explicitly uses partial derivatives with weights fixed and separately includes the actual readout change in the state distance and prediction change. This distinction is correct, not a loophole.

## 7. Actual uniform bounds, readout distance, and positive prediction

### 7.1 Bounds are on the stated norms

Since \(|\phi(s)|<\pi/2\),

\[
|\tau_n(\alpha)|\leq\frac{\pi(1+\beta/2)}{\sqrt n},\qquad
|H_n(\alpha)|<\pi/2.
\]

For \(n\geq4\), every third-layer coordinate is therefore bounded in absolute value by

\[
Z=\frac{\pi(1+\beta/2)}2+\frac{\rho\pi}2.
\]

It follows pointwise that \(1\leq W_i^{(4)}\leq1+Z^2\). This gives both the readout RMS and coordinate bounds in (45), rather than merely an assumed bound on the backward signal.

The complete bounds claimed in the candidate follow as follows:

| Quantity | Bound independent of width | Verification |
| --- | --- | --- |
| \(\|W^{(1)}\|_2/\sqrt n,\ \|z^{(1)}\|_2/\sqrt n\) | \(1\) | Both vectors are \(\mathbf1_n\). |
| \(\|W^{(2)}\|_{\rm op}\) | \(K_2\) | Exact singular values and orthogonal column rotation. |
| \(\|W^{(3)}\|_{\rm op}\) | \(K_3\) | Rank-one operator norm and triangle inequality. |
| \(\|W^{(2)}\|_F/\sqrt n,\ \|W^{(3)}\|_F/\sqrt n\) | \(K_2,K_3\) | Sum of squared singular values is at most \(n\|W\|_{\rm op}^2\). |
| \(\|W^{(4)}\|_2/\sqrt n,\ \|W^{(4)}\|_\infty\) | \(1+Z^2\) | Coordinatewise bound above. |
| \(\|z^{(2)}\|_2/\sqrt n\) | \(3/2\) | \(1+x<3/2,\ x/2<1/4,\ 0<c_0T<c_0<1\), and the base coordinates obey the same bound. |
| \(\|z^{(3)}\|_2/\sqrt n\) | \(Z\) | Pointwise bound. |
| \(\|h^{(\ell)}\|_2/\sqrt n\), all three layers | \(\pi/2\) | Range of arctangent. |
| \(\|\delta^{(3)}\|_2/\sqrt n\) | \(1\), exactly | \(\delta^{(3)}=\mathbf1_n\). |
| \(\|q^{(2)}\|_2/\sqrt n,\ \|d^{(2)}\|_2/\sqrt n\) | \(\sqrt{4+\beta^2+\rho^2}\) | Exact query norm and gate magnitude at most 1. |
| \(\|u_R^{(2)}\|_2/\sqrt n\) | \(1\) | Membership in the box with \(R=1\). |
| \(c_1\) | \(c_0^2>0\), exactly | \(\|h^{(1)}\|_2^2/n=c_0^2\). |

If one includes the additional raw lower chain above, its RMS is also bounded:
\(\|q^{(1)}\|_2/\sqrt n\leq K_2\sqrt{4+\beta^2+\rho^2}\) and the bound for \(d^{(1)}\) is half of this. No small difference for these additional fields is asserted.

The unnormalized sizes are not all bounded: \(\|W^{(1)}\|_2=\sqrt n\), \(\|W^{(4)}\|_2\geq\sqrt n\), and both hidden Frobenius norms grow at order \(\sqrt n\), since \(\rho>0\). The candidate does not assert otherwise. Its uniform hidden operator bounds and normalized primal bounds are compatible with ordinary Frobenius distances between the paired hidden matrices. Bounds on the points and the choice of distance must not be conflated.

Also \(\|h^{(1)}\|_2/\sqrt n=c_0\), and

\[
\frac{\|h^{(2)}\|_2^2}{n}
=\frac{\phi(L_n)^2+\phi((L_n-1)/2)^2}{n}
+\frac mn\,\phi(c_0T_n)^2
\longrightarrow\phi(c_0)^2>0
\]

at each endpoint. There is no vanishing lower feature RMS.

### 7.2 Readout differences are paid for

The fixed \(W^{(3)}\) and activation Lipschitz bound imply

\[
\frac{\|\Delta z^{(3)}\|_2}{\sqrt n}
\leq K_3\frac{\|\Delta h^{(2)}\|_2}{\sqrt n}=O(n^{-1}),\qquad
\frac{\|\Delta h^{(3)}\|_2}{\sqrt n}=O(n^{-1}).
\]

Since both third-layer endpoints lie in \([-Z,Z]^n\),

\[
|\Delta W_i^{(4)}|
=|z_i^{(3)}(1/n)+z_i^{(3)}(0)|\,|\Delta z_i^{(3)}|
\leq2Z|\Delta z_i^{(3)}|.
\]

Taking Euclidean norms proves (44). This is an actual bound on the changed readout parameter, not a decision to treat it as fixed.

### 7.3 Prediction is nonzero and has the claimed limit

Let \(g(s)=(1+s^2)\phi(s)\). Each rare coordinate contributes \(g(\tau_n)/n\) and each bulk coordinate contributes \(g(\tau_n+\rho H_n)/n\). This proves the exact formula (46).

At both endpoints, \(\tau_n\to0\), \(T_n\to1\), and \(H_n\to\phi(c_0)\). Thus

\[
f_n\to f_*=(1+k^2)\phi(k),\qquad k=\rho\phi(c_0)>0.
\]

The function \(g\) is continuous, and all of its arguments lie in a fixed bounded interval, so there is no hidden unbounded-contribution issue in the two rare coordinates. Since \(0<\phi(c_0)<c_0<1\) and \(\rho=1/4\), \(0<k<1/4\), whence

\[
0<f_*<(1+1/16)/4=17/64<1.
\]

The candidate's fixed interval \([f_*/2,(1+f_*)/2]\) therefore contains both predictions for all sufficiently large widths.

In fact both predictions are positive for every \(n\geq4\). At the base state \(\tau_n=2c_0/\sqrt n>0\). At the perturbed state the numerator defining \(\tau_n\) exceeds \(\pi/2-1/4>0\), since \(\phi(1+x)>\pi/4\), \(\phi(x/2)<x/2<1/4\), and \(\beta(1-1/\sqrt n)<1\). Also \(H_n>0\). Thus all third preactivations, their arctangents, and the readout entries are positive. Only the eventual uniform upper separation from 1 relies on the limit.

Finally, decomposing the prediction change into the changed readout and changed activation gives

\[
|\Delta f|
\leq\frac{\|\Delta W^{(4)}\|_2}{\sqrt n}
\frac{\|h^{(3)}(1/n)\|_2}{\sqrt n}
+\frac{\|W^{(4)}(0)\|_2}{\sqrt n}
\frac{\|\Delta h^{(3)}\|_2}{\sqrt n}
=O(n^{-1}).
\]

This verifies (48) with the correct factors of \(1/n\) and without imposing cancellation.

## 8. Full-state distance and exact Lipschitz-ratio scale

The candidate's distance contains normalized \(W^{(1)},W^{(4)}\), ordinary Frobenius distances for \(W^{(2)},W^{(3)}\), normalized preactivation and activation distances at all three layers, and the scalar prediction distance.

The first-layer weights, input, first preactivation, first activation, and third-layer matrix are exactly unchanged. The preceding calculations prove that each other component is \(O(n^{-1})\) in the norm used in (49). Their number is fixed, so \(D_n=O(n^{-1})\). Equation (29) gives a component asymptotic to \(a_*/n>0\), proving the matching lower bound.

The following independent calculation verifies every nonzero component and provides a sharper certificate. Define

\[
\gamma=1-\beta/2>0,\qquad k=\rho\phi(c_0),\qquad
g'(k)=1+2k\phi(k).
\]

From differentiability of arctangent and \(\sqrt n\,x_n\to1\),

\[
n\Delta\tau_n
=\sqrt n\left(2[\phi(1+x_n)-\phi(1)]
-\beta(1-1/\sqrt n)\phi(x_n/2)\right)
\longrightarrow\gamma.
\]

Also \(n|T_n-1|\leq1/(2n)+1/\sqrt m\to0\), so \(n\Delta H_n\to0\). Therefore the common bulk third-layer difference satisfies \(n\Delta z_j^{(3)}\to\gamma\), and its base value tends to \(k\). For the two rare coordinates, \(n\Delta z_i^{(3)}=n\Delta\tau_n\to\gamma\), but their number is fixed.

Combining these observations with (A) and the difference of squares gives

\[
\begin{array}{rl}
n^2\|\Delta W^{(2)}\|_F^2&\longrightarrow a_*^2,\\
n\|\Delta z^{(2)}\|_2^2&\longrightarrow 5/4,\\
n\|\Delta h^{(2)}\|_2^2&\longrightarrow 1/2,\\
n\|\Delta z^{(3)}\|_2^2&\longrightarrow \gamma^2,\\
n\|\Delta h^{(3)}\|_2^2&\longrightarrow \gamma^2/(1+k^2)^2,\\
n\|\Delta W^{(4)}\|_2^2&\longrightarrow 4k^2\gamma^2.
\end{array}
\tag{B}
\]

For example, each bulk activation difference has \(n\Delta h_j^{(3)}\to\gamma\phi'(k)=\gamma/(1+k^2)\), and there are \(n-2\) identical such coordinates. Each bulk readout difference has

\[
n\Delta W_j^{(4)}
=(z_j^{(3)}(1/n)+z_j^{(3)}(0))\,n\Delta z_j^{(3)}
\to2k\gamma.
\]

The rare readout changes are \(O(n^{-3/2})\), since their preactivations are \(O(n^{-1/2})\) and their changes are \(O(n^{-1})\), and hence do not alter the last limit in (B).

The exact prediction formula similarly gives

\[
n\Delta f
=2\Delta g(\tau_n)+(n-2)\Delta g(\tau_n+\rho H_n)
\longrightarrow\gamma g'(k).
\tag{C}
\]

Here \(g'(s)=1+2s\phi(s)\), the first term tends to zero, and the second follows from the common bulk difference and the mean value formula. This also checks the contribution from changing the readout along the family.

Substituting (B)–(C) into every term of (49) yields

\[
nD_n\longrightarrow\Lambda>0,
\]
\[
\Lambda^2
=a_*^2+\frac54+\frac12
+\gamma^2\left(
1+\frac1{(1+k^2)^2}+4k^2+[1+2k\phi(k)]^2
\right).
\tag{D}
\]

All summands correspond to explicitly included variables; none has been discarded as external data. In particular \(\Lambda\) is finite, and its positivity already follows from \(a_*^2>0\).

Combining (D) with \(\|\Delta u_R^{(2)}\|_2\to\beta\) proves the sharper ratio statement

\[
\frac{\|\Delta u_R^{(2)}\|_2/\sqrt n}{D_n}
\sim\frac{\beta}{\Lambda}\sqrt n\to\infty.
\]

This proves both sides of the order claim in (50). It audits the full Section 5 extension, not only the leading two-coordinate output.

The related metric statements also hold:

- Adding the RMS distances of \(q^{(2)}\) and \(\delta^{(3)}\) changes nothing, since these differences are zero.
- Dividing hidden-matrix distances by \(\sqrt n\) decreases the denominator, so the divergent lower bound persists. The retained second-layer state term also supplies a positive \(1/n\) scale for that full distance.
- Keeping only the primal parameter terms still leaves a distance asymptotic to \(\sqrt{a_*^2+4k^2\gamma^2}/n\), so the divergence persists.
- A product output norm which includes the stated layer-2 RMS as a component is at least that component and inherits the obstruction.

These results concern one family of fixed bounds large enough to contain the stated constants. They do not assert a counterexample in every arbitrarily small prescribed norm ball.

Adding the RMS distance of \(d^{(2)}\) itself to the input would be a different claim: its ordinary difference tends to 1, so that added term has size \(1/\sqrt n\). The candidate does not claim that this or all possible backward-variable distances vanish. Its asserted zero differences are specifically \(q^{(2)}\) and \(\delta^{(3)}\).

## 9. Normalization limitations and arbitrary fixed radius

### 9.1 Ordinary readout distance

The bulk calculation above proves

\[
\sqrt n\,\|\Delta W^{(4)}\|_2\to2k\gamma>0.
\]

Thus the ordinary readout distance is \(\Theta(n^{-1/2})\), whereas its RMS distance is \(\Theta(n^{-1})\). If a replacement input distance contains the unnormalized readout norm, the quotient has asymptotic upper bound \(\beta/(2k\gamma)\). For the precise modification of (49) that only removes the readout's normalization, all other terms are smaller, and the quotient actually tends to \(\beta/(2k\gamma)\).

This agrees with the candidate. It supplies neither a divergent quotient for that modified distance nor a proof that the mapping is uniformly Lipschitz for that distance.

### 9.2 Projecting the ordinary derivative or another smaller scaling

At the two endpoints, the ordinary derivative is \(d^{(2)}/n\), not \(d^{(2)}\). For \(n\geq4\), its first coordinate is at most \(1/\sqrt n\leq1/2\), the second has absolute value less than \(\beta/\sqrt n<1\), and the bulk entries are at most \(\rho/n<1\). Thus it already lies in \(K_1\), at every permitted width, which is stronger than the candidate's eventual statement.

For any feasible input \(w\), \(J_w(w)=0\) and positive definiteness implies \(P_M(w)=w\). Consequently the projection on these ordinary derivatives is exactly the identity, regardless of the non-diagonal metric.

Equations (33) give

\[
\Delta d_1^{(2)}=-A_n\to-1,\qquad
\Delta d_2^{(2)}=\beta E_n\to0,
\]

and the bulk difference has Euclidean norm \(O(n^{-1})\). Therefore \(\|\Delta d^{(2)}\|_2\to1\). The projected ordinary-derivative output RMS is asymptotic to \(n^{-3/2}\), and its quotient against (49) is asymptotic to \(1/(\Lambda\sqrt n)\to0\).

As an additional scaling check, projecting \(d^{(2)}/\sqrt n\) also gives the identity at these states: the first base coordinate is exactly 1, the perturbed first coordinate is less than 1, and every other coordinate has absolute value less than 1. Its output RMS difference is asymptotic to \(1/n\), so the quotient tends to \(1/\Lambda\), not infinity. Thus no normalization-independent gradient claim can be inferred.

The audited divergent quotient is specifically for \(P_{M_n}(d^{(2)})\), with residual excluded and no extra factor inside the projection. No conclusion about adding a residual inside a nonlinear projection is established or needed.

### 9.3 Any fixed \(R>0\)

Keep the entire lower construction and the angle \(1/n\) unchanged. Choose a fixed \(0<\rho<\min\{R,1/4\}\), and replace the two rare query entries by

\[
(2R\sqrt n,-\beta R(\sqrt n-1)).
\]

Replace \(v_n\) by \(Rv_n\) in the rank-one part of \(W^{(3)}\). Then \((W^{(3)})^T\mathbf1_n\) gives exactly this rescaled query with bulk entries \(\rho\). Define \(z^{(3)}=W^{(3)}h^{(2)}\) and \(W^{(4)}=1+(z^{(3)})^2\) again, so \(\delta^{(3)}=\mathbf1_n\) remains exact.

The rare raw inputs scale by \(R\), the rare projected outputs are exactly

\[
(R,0),\qquad (R,\beta R(E_n-A_n)).
\]

The active-coordinate inequality is \(R(\sqrt n-A_n)>R\); the free-coordinate margin is at least \(R(1-\beta)\). The bulk raw values are at most \(\rho<R\), giving a margin at least \(R-\rho>0\). All active-set checks therefore survive for every \(n\geq4\).

The query RMS is bounded by

\[
\sqrt{R^2(4+\beta^2)+\rho^2},
\]

and the upper operator bound can be taken as \(\rho+R\sqrt{4+\beta^2}\). The coordinate bound on \(z^{(3)}\) can be taken as

\[
Z_R=\frac{R\pi(1+\beta/2)}2+\frac{\rho\pi}2.
\]

The same actual readout bounds follow with \(Z_R\) in place of \(Z\). All constants are finite for fixed \(R\), and the mobility remains unchanged.

The rare contribution \(\tau_n\) is multiplied by \(R\) and still tends to zero. The positive bulk limit is \(k=\rho\phi(c_0)>0\), so the prediction limit is still \((1+k^2)\phi(k)\in(0,17/64)\). In the distance calculation, replace \(\gamma\) by \(R\gamma\) in the upper-layer terms of (D), while the second-layer and matrix terms stay the same. Hence \(D_n\sim\Lambda_R/n\) for a positive finite \(\Lambda_R\), and the projected-field RMS is asymptotic to \(\beta R/\sqrt n\). The ratio is asymptotic to \((\beta R/\Lambda_R)\sqrt n\).

This proves the stated extension for every fixed positive \(R\). It does not claim uniform constants as \(R\) itself varies with width.

## 10. Hostile checks, claim boundaries, and final disposition

The main attempted failure modes and their outcomes are:

| Attempted objection or counterexample | Outcome |
| --- | --- |
| Use an infeasible \(u=d\) in the variational inequality | Succeeded only against the superseded unqualified version; the revised statement explicitly requires \(u\in K_R\), excluding this objection. |
| Diagonal metric, dimension one, or degenerate spectral interval \(c=C\) | Not counterexamples: the candidate explicitly puts these in the Lipschitz case. |
| Non-diagonal SPD matrix without a decoupled two-coordinate block | Covered by the full complementary-block Schur argument; no positivity of the coupling vector is assumed. |
| Very large or signed entries of \(M_{FF}^{-1}M_{Fi}\) | Do not invalidate the local argument: the feasible interval may depend on \(t\) and the fixed matrix. |
| Cross an active-set boundary at the smallest admitted \(t\) or width | Fails: strict feasibility and gradient signs are verified for all \(t\geq2\), \(n\geq4\). |
| Column rotation changes the metric | Fails here because the lower squared gate is exactly \(I/4\), and the relevant product contains \(QQ^T\). |
| Charge an extra \(\sqrt n\) in the hidden-matrix distance | Fails: the exact rotation-plane trace gives (29) in ordinary Frobenius norm. |
| Upper signal is external rather than produced by the network | Fails for Section 5: the fixed \(W^{(3)}\) and actual readout parameters yield \(\delta^{(3)}=\mathbf1_n\) and the prescribed \(q^{(2)}\) exactly. |
| Changing readout is omitted or has too large an RMS change | Fails: the readout is included in (49), and its RMS change is asymptotic to \(2k\gamma/n\). |
| Prediction vanishes or relies on cancellation | Fails: the positive bulk gives \(f_*>0\); in fact every endpoint prediction is positive. |
| Bounded signal RMS supplies the coordinate bound needed in (11) | Fails: the two rare query entries have order \(\sqrt n\). |
| Interpret the same example with ordinary readout distance | Removes the divergent ratio for this family; this is explicitly acknowledged in Section 5.7. |
| Interpret the field as the ordinary derivative \(d^{(2)}/n\) | Removes the obstruction for this family; projection is the identity and the quotient tends to zero. |
| Infer a counterexample in an arbitrarily small initialization neighborhood | Not supported or claimed; readout coordinates are at least 1 and the bounds describe one algebraic family. |

The example satisfies the concrete forward and backward equations it states. It does not establish that these states arise from a prescribed initialization, occur with any probability, are reachable along a flow, are training iterates, or violate a canonical trained-trajectory theorem. Positive prediction and bounded state norms do not establish any of those additional claims. No such claim is made in the candidate. There is also no tiny-readout-initialization premise: \(W_i^{(4)}\geq1\) throughout.

The word “fixed” for the mobility has its correct scope: at each width the two endpoints have exactly the same \(M_n\), and the spectral constants are uniform in width. Matrices of different dimensions are not asserted to be literally identical.

The mathematical disposition, covering the entire candidate, is:

- Section 1: existence, uniqueness, the now explicitly feasible optimality equivalence (1), nonexpansiveness, and signal estimates all pass.
- Sections 2–3: the fixed example, general SPD diagonal iff classification, and bounded-coordinate correction pass.
- Section 4: the canonical fixed-width embedding, full lower feedforward identity, exact metric invariance, active-set proof, and matrix-distance statement pass.
- Sections 5.1–5.7: all forward/backward equations, exact rotation and mobility, query RMS, complete projection, operator and primal bounds, actual readout changes, positive prediction, full distance, \(\sqrt n\) quotient, alternative-normalization limitations, and every fixed-\(R>0\) rescaling pass.
- Section 6: the combined mathematical conclusions and the exclusion of trajectory, reachability, initialization-probability, and dynamics conclusions are supported.

The sole correction from the original audit has been implemented and independently verified. There is no outstanding unchecked full-state extension and no remaining repair. The current verdict is PASS for the entire revised candidate at SHA-256 713f889141f56ee900c49e9b4478133035d8de7dd0156680869a73761a9b647a. The original 0f3dde70860be93fccfba9b1cf837fa68a69472bbfb2bb3a9a41d7d02e4ea428 literal FAIL is superseded provenance only.

The auditor did not edit the candidate. Final candidate and report SHA-256 values are reported separately after the report is complete; the report does not attempt to contain its own hash.
