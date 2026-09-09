# Bounded sine: what chronological Picard expansion does and does not prove

2026-09-08. Independent bounded branch. Only `CONTRACT.md` was read from the development program. No experiments were run and no other development report is used.

## Conclusion and scope

For the explicitly different fixed activation

\[
\phi(s)=1+\tfrac12\sin s,
\]

the exact physical equations have a useful compact-time bounded-operator formulation for the return field \(q\). Its chronological linear expansion converges in \(L^2\) on every finite interval **when the physical coefficient paths have already been supplied**. This does not construct those paths or prove their uniqueness.

There is a precise obstruction to a proposed next step: expanding the nonlinearities into elementary differentials, estimating each differential by its absolute Gaussian moments, and expecting a factorial time-simplex denominator to yield subexponential tails. An actual elementary-differential family of the first-layer sine features has coefficient

\[
\frac{t^{2m}}{2^m m!}\,\phi^{(m)}(Z_i)\,\xi_i^m,
\qquad \xi_i=z_i''(0).
\]

The initial Gaussian matrix program makes \(\xi_i\), conditionally on the first-layer initial field, a Gaussian with a bounded mean and a variance bounded below on an event of fixed positive probability. Consequently, the sum of the absolute \(L^p\) norms of this family is at least \(\exp(c t^4p)\), for every fixed \(t>0\) and sufficiently large \(p\). This happens although the actual feature satisfies \(|h_i(t)|\le3/2\). Parallel branches, rather than a single chronological chain, are the reason that the denominator is \(2^m m!\), not \((2m)!\).

This is a proved obstruction to that absolute elementary-differential estimate. It is **not** a counterexample to physical source tails, to sine-preserving nonlinear Picard iteration, or to the contract's global convergence target. A source estimate and the strong identification/uniqueness bridge remain open. In particular, the report does not claim a global population theorem or the actual finite-width/GD joint limit.

## 1. Fixed model and the activation distinction

All three inputs, labels, initial distributions, trained blocks and raw metric are exactly those of the contract. Write \(u_i=x_i/\sqrt d\), \(\Gamma_{ij}=u_i^Tu_j\), and use normalized finite layer norms. The actual finite readout remains \(C_a(0)\sim N(0,n^{-2})\). The prescribed population initial readout is zero. No finite algorithm is changed to zero initialization in this report.

Here

\[
\tfrac12\le\phi\le\tfrac32,
\qquad \|\phi^{(m)}\|_\infty\le\tfrac12\quad(m\ge1).
\]

The coefficient \(1/2\) is fixed, independent of data, width and horizon. This activation has zeros and sign changes in its derivative; it does not inherit the monotonicity of the contract's principal affine–tanh mixture. Its nonlinearity is quantitative: for \(G\sim N(0,1)\),

\[
\mathbb E|\phi''(G)|^2=\frac{1-e^{-2}}8,
\qquad
\inf_{a,b}\mathbb E|\phi(G)-a-bG|^2
=\frac{1-e^{-2}-2e^{-1}}8>0.
\]

The second formula follows from \(\mathbb E\sin G=0\), \(\mathbb E[G\sin G]=e^{-1/2}\), and \(\mathbb E\sin^2G=(1-e^{-2})/2\). No feature-training or all-time kernel-floor conclusion follows from these initialization calculations alone.

## 2. Exact bounded-operator skeleton

The statements in this section are exact at finite width. They also hold on any interval on which a canonical strong population solution and its genuine adjoint have already been constructed.

Put \(B=3/2\), \(D=1/2\), \(R=\sqrt{2E(0)}\), and \(S=\sqrt3R\). Energy dissipation gives \(\sum_i|r_i(t)|\le S\) and

\[
\|A(t)\|_{\mathrm{op}}
\le \|A(0)\|_{\mathrm{op}}+\sqrt{TE(0)}=:M_A
\quad(0\le t\le T).
\]

The population increment \(U\), or its finite counterpart, has kernel

\[
\mathcal U_t(a,b)=-\int_0^t\sum_i r_i(s)b_i(s,a)h_i(s,b)\,ds.
\]

At finite width, \(A(t)-A(0)\) has entries \(\mathcal U_t(a,b)/n\); this is the normalization used in the kernel bounds below. Set

\[
M_C=\|C(0)\|_\infty+BST.
\]

Then, pathwise,

\[
\|C\|_\infty\le M_C,\quad
\|b_i\|_\infty\le DM_C,\quad
\|\dot C\|_\infty\le BS,
\]

\[
\|\dot{\mathcal U}\|_\infty\le SBDM_C=:M_{\dot U},
\qquad
\|\mathcal U\|_\infty\le TM_{\dot U}.
\]

These estimates retain the small finite random readout. Its supremum tends to zero in probability, and these estimates can be used on events with bounded initial supremum and bounded initial operator norm. No event involving a trained-coordinate supremum is assumed.

Stack the three return fields in \(\mathbf q\in H_1^3\). Define the multiplication operator \(\mathcal D_t:H_1^3\to H_1^3\) by

\[
(\mathcal D_t\mathbf q)_i
=-\sum_j\Gamma_{ij}r_j\phi'(z_i)\phi'(z_j)q_j.
\]

Thus \(\dot{\mathbf h}=\mathcal D_t\mathbf q\) exactly, and

\[
\|\mathcal D_t\|_{2\to2}\le D^2S.
\]

Indeed, each component has norm at most \(D^2R\|\mathbf q\|_{H_1^3}\), using \(|\Gamma_{ij}|\le1\), and there are three components. Differentiating \(q_i=A^*b_i\) gives

\[
\dot q_i=g_i+A^*M_{C\phi''(v_i)}A(\mathcal D_t\mathbf q)_i,
\tag{2.1}
\]

where

\[
g_i=\dot U^*b_i+
A^*\left[\dot C\phi'(v_i)+C\phi''(v_i)\dot U h_i\right].
\tag{2.2}
\]

The same \(A=A(0)+U\) and its actual adjoint appear in every occurrence. There is no independence replacement.

Writing (2.1) as \(\dot{\mathbf q}=\mathcal L_t\mathbf q+\mathbf g_t\),

\[
\|\mathcal L_t\|_{2\to2}
\le M_A^2D^3M_CS=:K_T,
\tag{2.3}
\]

and one explicit source bound is

\[
\|\mathbf g_t\|_2\le\sqrt3\left[
M_{\dot U}DM_C+
M_A\left(BSD+M_CDM_{\dot U}B\right)
\right]=:G_T.
\tag{2.4}
\]

For example, \(\|\dot U h_i\|_\infty\le M_{\dot U}B\), and \(\|\dot U^*b_i\|_\infty\le M_{\dot U}DM_C\). This proves (2.4), without applying a Gaussian operator to an arbitrary bounded function and declaring its output bounded.

### Conditional linear chronological expansion

For supplied strongly measurable coefficient paths satisfying (2.3)–(2.4), the iterated integral operator

\[
(Vx)(t)=\int_0^t\mathcal L_sx(s)\,ds
\]

satisfies

\[
\|V^m x\|_{C([0,T];L^2)}
\le\frac{(K_TT)^m}{m!}\|x\|_{C([0,T];L^2)}.
\]

This follows by induction from the ordered simplex \(0<s_m<\cdots<s_1<t\). The series \(\sum_{m\ge0}V^m(q(0)+\int_0^\cdot g_sds)\) converges in \(C([0,T];L^2)\), solves the supplied linear equation, and is unique there; the difference of two solutions satisfies the same factorial estimate for every \(m\), hence vanishes. This is a complete conditional linear statement.

It does not close the nonlinear problem: \(\mathcal L_t\) and \(g_t\) contain the unknown \(z,v,C,U,r\). Supplying their actual future paths would be trajectory playback. Also, (2.3) is an \(L^2\) estimate and provides no width-independent \(L^p\) operator bound for \(p>2\).

## 3. The first return source is an actual Gaussian matrix program

This section constructs only an initialization program, so it presupposes no global solution. Let \(Z=(Z_1,Z_2,Z_3)\sim N(0,\Gamma)\), including singular \(\Gamma\), and define

\[
h_i(Z)=\phi(Z_i),\qquad H_{ij}=\mathbb E[h_i(Z)h_j(Z)].
\]

### Lemma 3.1: \(H\) is positive definite

The separation assumption makes the three \(u_i\) distinct modulo sign. If \(\sum_i a_i\phi(w^Tu_i)=0\) in Gaussian \(L^2(\mathbb R^d)\), continuity and the full support of the Gaussian law make it zero for every \(w\). Setting \(w=0\) gives \(\sum_i a_i=0\). Choose \(e\in\mathbb R^d\) outside the finitely many hyperplanes on which some \(\lambda_i=e^Tu_i\) is zero or some \(\lambda_i=\pm\lambda_j\). Such a choice exists because none of those hyperplanes is all of \(\mathbb R^d\). Then

\[
\sum_i a_i\sin(t\lambda_i)=0\quad\hbox{for every }t.
\]

Its first, third and fifth derivatives at zero give a Vandermonde system with determinant, up to sign,

\[
\lambda_1\lambda_2\lambda_3
\prod_{i<j}(\lambda_j^2-\lambda_i^2)\ne0.
\]

Thus every \(a_i=0\), which proves the lemma. This argument never inverts \(\Gamma\).

Let \(V\sim N(0,H)\), and put

\[
c(V)=\sum_\ell y_\ell\phi(V_\ell),\qquad
B_i(V)=c(V)\phi'(V_i).
\tag{3.1}
\]

Both \(B_i\) and all their derivatives of each fixed order are bounded. At the population initial state \(C=0\), the exact formal initial equations are

\[
\dot C(0)=c(V),\qquad
\dot U(0)=0,\qquad
q_i(0)=0,\qquad
\dot q_i(0)=A_0^*B_i(V)=:Q_i.
\tag{3.2}
\]

Here the last expression is defined by the actual finite initialization program, not by an abstract Gaussian operator chosen for convenience.

### Lemma 3.2: canonical law of \(Q\)

At a typical first-layer coordinate, the finite initialization program converges, jointly with \(Z\), to

\[
Q_i=\mu_i(Z)+G_i,
\qquad
\mu_i(Z)=\sum_\ell h_\ell(Z)\mathbb E[\partial_\ell B_i(V)],
\tag{3.3}
\]

where \(G\) is independent of \(Z\), centered Gaussian, with covariance

\[
S_{ij}=\mathbb E[B_i(V)B_j(V)].
\tag{3.4}
\]

Every fixed polynomial moment of this initialization program also converges. In particular, \(\mu\) is bounded.

**Proof.** Write \(A_{\alpha a}(0)=g_{\alpha a}/\sqrt n\). Conditional on the first-layer initialization, the rows

\[
V_\alpha=\frac1{\sqrt n}\sum_b g_{\alpha b}h(Z_b)
\]

are independent Gaussians with covariance \(H_n=n^{-1}\sum_bh(Z_b)h(Z_b)^T\). The law of large numbers for bounded variables gives \(H_n\to H\). For a fixed coordinate \(a\),

\[
Q_{i,n}^a=\frac1{\sqrt n}\sum_\alpha
g_{\alpha a}B_i(V_\alpha).
\]

One-dimensional Gaussian integration by parts in \(g_{\alpha a}\) gives its conditional mean exactly as

\[
\sum_\ell h_\ell(Z_a)
\mathbb E_{N(0,H_n)}[\partial_\ell B_i].
\]

Applying that integration by parts twice gives

\[
\mathbb E[g_{\alpha a}^2B_i(V_\alpha)B_j(V_\alpha)]
=\mathbb E_{N(0,H_n)}[B_iB_j]+O(n^{-1}),
\]

uniformly in the first-layer initialization, since \(h\) and the relevant derivatives are bounded. The centered row summands have uniformly bounded absolute moments of each fixed order. Their conditional covariance therefore tends to \(S\). Expanding a row characteristic function through its quadratic term, the remainder after scaling by \(n^{-1/2}\) is \(O(n^{-3/2})\); multiplying the \(n\) independent characteristic functions proves the conditional Gaussian limit. The limiting covariance is deterministic and its limiting mean depends on the selected first-layer coordinate only through \(Z_a\), proving (3.3).

For uniform integrability of a fixed even moment, expand the moment of the sum of the centered independent row summands. Terms with singleton indices vanish. A term in a moment of order \(2k\) has at most \(k\) distinct row indices, so its number of choices is at most \(n^k\), canceled by the normalization \(n^{-k}\). The fixed-order row moments bound all remaining terms. The conditional mean is uniformly bounded as well. Applying the same estimate to a larger even order gives uniform integrability, proving moment convergence. The argument also works jointly for any fixed finite set of coordinates; their off-diagonal innovation covariances vanish by the corresponding two-variable integration by parts. ∎

### Lemma 3.3: the innovation is nondegenerate for nonzero labels

Assume \(y\ne0\). Then \(S\) is positive definite.

**Proof.** Since \(H>0\), the Gaussian density of \(V\) is positive everywhere. The function \(c(v)\) is not identically zero: differentiating with respect to \(v_i\) would otherwise imply \(y_i\cos v_i=0\) for every \(v_i\), for each \(i\). If \(a^TSa=0\), continuity gives

\[
c(v)\sum_i a_i\cos v_i=0\quad\hbox{for all }v.
\]

There is an open box on which \(c\ne0\). On that box, differentiating with respect to \(v_i\) gives \(a_i\sin v_i=0\) throughout an interval, hence \(a_i=0\). ∎

If the label convention permits \(y=0\), the prescribed population zero-readout state is stationary. The obstruction below concerns the nontrivial case \(y\ne0\); it is not needed for the stationary case.

## 4. A parallel-branch family defeats the absolute moment majorant

At the population initial state, \(z_i'(0)=0\). Differentiating the exact first-layer equation once, or simply forming its formal initial jet, gives

\[
\xi_i:=z_i''(0)
=\sum_j\Gamma_{ij}y_j\phi'(Z_j)Q_j.
\tag{4.1}
\]

This is a finite initialization program involving the original matrix and its transpose. Equations (3.3)–(3.4) give its canonical limiting law. Conditional on \(Z\), \(\xi_i\) is Gaussian with a bounded mean and variance

\[
\sigma_i(Z)^2=a_i(Z)^TSa_i(Z),
\qquad
(a_i(Z))_j=\Gamma_{ij}y_j\phi'(Z_j).
\tag{4.2}
\]

Choose an index \(i\) with \(y_i\ne0\). Because \(\Gamma_{ii}=1\),

\[
\sigma_i(Z)^2\ge\lambda_{\min}(S)y_i^2\cos^2(Z_i)/4.
\]

The event

\[
\mathcal E_i=\{|\sin Z_i|\ge1/2,\ |\cos Z_i|\ge1/2\}
\]

has a fixed positive probability \(\varepsilon\), since \(Z_i\sim N(0,1)\), even when the joint \(Z\) is singular. On this event,

\[
\sigma_i(Z)\ge\sigma_*:=|y_i|\sqrt{\lambda_{\min}(S)}/4>0,
\qquad
|\phi^{(m)}(Z_i)|\ge1/4\quad(m\ge1).
\tag{4.3}
\]

### The exact elementary-differential coefficient

The Faà di Bruno expansion of \(h_i(t)=\phi(z_i(t))\) contains the elementary differential in which all \(m\) arguments of \(\phi^{(m)}\) receive \(z_i''(0)\). Its contribution to the formal time series is exactly

\[
T_m(t)=\frac{t^{2m}}{2^m m!}\phi^{(m)}(Z_i)\xi_i^m.
\tag{4.4}
\]

This follows directly by selecting the second-order jet in

\[
\frac{\phi^{(m)}(Z_i)}{m!}
\left(\tfrac12t^2z_i''(0)+\text{higher jets}\right)^m.
\]

Equivalently, in the derivative of order \(2m\), partition the differentiations into \(m\) unordered pairs. There are \((2m)!/(2^m m!)\) such partitions. The Taylor factor \(1/(2m)!\) leaves \(1/(2^m m!)\). In chronological language there are \(m\) parallel two-step branches; their causal partial order does not impose one total order on all \(2m\) vertices.

No time-analyticity assertion is being assumed here. Equation (4.4) specifies an elementary differential and its exact combinatorial coefficient. At finite width all jets exist. At the prescribed zero-readout population initialization these are formal Gaussian-program jets. In the actual finite initialization, the same elementary-differential expansion has a part independent of the initial readout, given by (4.1)–(4.4), and additional terms containing that readout. Thus the obstruction does not require replacing the actual finite initialization or proving an infinite Taylor expansion valid. It concerns a majorant that estimates the individual Gaussian-program differentials before any cancellations between them.

### Proposition 4.1: exponential growth in the moment order

For every fixed \(t>0\), there are \(c_t>0\), \(c_0>0\), and \(p_t<\infty\), depending only on the fixed data and \(t\), such that

\[
\sum_{m\ge1}\|T_m(t)\|_{L^p}
\ge c_0\exp(c_t p)
\quad(p\ge p_t).
\tag{4.5}
\]

One can take \(c_t\) proportional to \(t^4\), with a data-dependent positive proportionality constant.

**Proof.** If \(N\) is standard Gaussian, the evenness and convexity of \(x\mapsto|x|^r\), for \(r\ge1\), imply

\[
\mathbb E|\mu+\sigma N|^r\ge\sigma^r\mathbb E|N|^r.
\]

Use this conditionally on \(Z\), restrict to \(\mathcal E_i\), and apply (4.3). For \(p\ge2\) and \(m\ge1\),

\[
\|\phi^{(m)}(Z_i)\xi_i^m\|_p
\ge\frac14\varepsilon^{1/p}\sigma_*^m\|N\|_{mp}^m.
\tag{4.6}
\]

There is a universal \(c>0\) with \(\|N\|_r\ge c\sqrt r\) for \(r\ge2\), as follows, for example, by integrating the Gaussian moment over \([\sqrt r,\sqrt r+1/\sqrt r]\). Since \(m!\le m^m\), (4.4)–(4.6) give

\[
\|T_m(t)\|_p
\ge\frac{\sqrt\varepsilon}{4}
\left(a\sqrt{p/m}\right)^m,
\qquad a=c\sigma_*t^2/2.
\]

For \(a^2p\ge8\), choose \(m=\lfloor a^2p/4\rfloor\). Then \(m\ge a^2p/8\) and \(a\sqrt{p/m}\ge2\). This single summand is at least

\[
\frac{\sqrt\varepsilon}{4}
\exp\left(\frac{a^2\log2}{8}p\right),
\]

which proves (4.5). ∎

A compact-time subexponential tail estimate would imply a bound \(\|q_i(t)\|_p\le C_Tp\); for example, integrating \(\mathbb P(|X|>x)\le2e^{-x/K}\) gives \(\mathbb E|X|^p\le2K^p p!\). Proposition 4.1 shows that the absolute expansion majorant already fails this growth test for the internal feature \(h_i\), which is in fact bounded. It therefore cannot establish the required tail class merely from bounded sine derivatives and chronological factorials. A crude Gaussian-degree estimate of alternating return chains has the related form \((Cp)^k/k!\), whose sum is \(e^{Cp}\); the parallel-branch calculation above is stronger evidence because it identifies an actual same-model differential family and proves its moment growth.

The proposition is deliberately stated for the full-system elementary-differential method. It is not a lower bound on the true \(q\), and it does not prove that an appropriately regrouped expansion directly for \(q\) must fail. Cancellations can be substantial: summing the displayed family pointwise gives

\[
\sum_{m\ge0}T_m(t)
=\phi\bigl(Z_i+\tfrac12t^2\xi_i\bigr),
\]

with the natural \(m=0\) term, and this resummed expression is bounded by \(3/2\). This identity is just the entire sine series for the frozen initial jet, not an assertion that the full flow equals that expression. It pinpoints exactly what absolute differential estimates discard.

## 5. Why the remaining \(L^2\) argument is not a global bridge

The bounded-operator expansion in Section 2 is useful propagation control. It does not prove smallness of a new source caused by replacing the physical coefficients. For example, comparing two first-layer equations produces, besides terms linear in \(q-\widetilde q\), terms of the form

\[
(\phi'(z_i)-\phi'(\widetilde z_i))q_j.
\tag{5.1}
\]

Bounded \(\phi''\) gives pointwise control by \(D|z_i-\widetilde z_i||q_j|\), but two \(L^2\) factors need not have an \(L^2\) product. The energy estimate and (2.3) supply no bound for this multiplication operator on an arbitrary \(L^2\) ball. On reached physical paths one might prove a substantially better statement, but that is the missing source/stability result rather than a consequence of the conditional Dyson series.

Proposition 4.1 does not rule out direct strong convergence in \(L^2\): its majorant is finite for fixed \(p,t\), and failure of the desired large-\(p\) estimate is not failure of a fixed-\(p\) approximation. Conversely, convergence of each fixed Gaussian-program jet is not convergence of a time expansion or an autonomous approximation hierarchy. These limit operations must remain separate.

For completeness, finiteness of that particular majorant follows because (4.2) has a uniformly bounded mean and variance: \(\|\xi_i\|_r\le C\sqrt r\) for \(r\ge2\). Thus its \(m\)-th summand is at most \((Ct^2)^m(mp)^{m/2}/m!\), a summable sequence for fixed \(p,t\).

Three specific possibilities survive this audit:

1. A chronological expansion that resums bounded sine subtrees before taking moments, together with a new estimate for the remaining repeated-matrix return sources.
2. A physical cavity/response estimate that uses bounded \(C,h,b,U\) and preserves the correlations in (3.3), with constants controlled on every fixed horizon.
3. A direct Cauchy theorem for sine-preserving physical approximations that controls the products in (5.1) on reached states without first proving a subexponential-tail bound.

None is proved here. Merely asserting that all derivatives of sine are bounded supplies none of them.

### Bounded legal queries are an additional causal constraint

Both directions of the physical Gaussian-matrix program have bounded legal queries: the forward queries are \(h_i\), and the backward queries are \(b_i\). The available bounds are uniform in width on each fixed energy-stopped horizon. Also, all sine derivatives have fixed size, and each physical update has its actual time-integration factor. An arbitrary adapted bounded vector \(b\) is therefore a much larger class than a backward query reachable here. A concentration example that first probes the Gaussian matrix with an unbounded forward needle, or that first uses an unbounded backward probe, does not establish an obstruction for this branch. Nor may a vanishing bounded probe be amplified by inserting a discontinuous or arbitrarily high-gain operation that the physical equations do not contain. No such example is used in this report.

These restrictions leave room for a causal tail estimate beyond Proposition 4.1. Lemma 3.2 is positive evidence at the first nontrivial query: its source is already a Gaussian plus a bounded return correction. The following conditional implication makes one possible later target precise, without asserting the representation exists. Suppose actual Gaussian-program limits yield

\[
q_i(t)=\mathcal G_i(t)+
\sum_j\int_{[0,t]}h_j(s)\,R_{ij}(t,ds),
\tag{5.2}
\]

where \(\mathcal G_i(t)\) is centered Gaussian with variance at most \(M_C^2D^2\), and the signed response measures satisfy

\[
\sup_{i,t\le T}\sum_j\|R_{ij}(t,\cdot)\|_{\mathrm{TV}}
\le K_T<\infty.
\tag{5.3}
\]

Then, whether or not \(\mathcal G\) is independent of the features,

\[
\|q_i(t)\|_p\le C DM_C\sqrt p+BK_T.
\]

This implication is immediate from boundedness of \(h\) and Gaussian moments. However, deriving (5.2) canonically, preserving all repeated-matrix return terms, and proving a mesh-uniform physical-time bound (5.3) are missing theorems, not consequences of query boundedness alone. A response derivative through previous first-layer motion can encounter precisely the \(q\)-weighted products in (5.1); bounding only the primitive derivatives of sine omits that response. Thus neither a positive causal-tail theorem nor its impossibility has been established by this branch. The bounded legal-query restriction is a serious remaining discriminator, not something defeated by the absolute-tree calculation.

## 6. Claim ledger and strongest surviving objections

| Claim | Status | Evidence or missing bridge |
|---|---|---|
| Compact-time bounds for \(C,b,U\) and the exact \(L^2\) operator equation for \(q\) | Proved conditional on the physical solution existing on the interval; exact for every finite width | Section 2 and raw energy identity |
| Convergence and uniqueness of the linear chronological series with supplied coefficient paths | Proved | Explicit simplex estimate in Section 2 |
| Positive initial feature covariance for all admitted input Grams | Proved, including singular \(\Gamma\) | Lemma 3.1 |
| First true Gaussian return source has bounded mean plus independent Gaussian innovation | Proved for the initialization program | Lemma 3.2, retaining the same original matrix and its transpose |
| Innovation nondegeneracy for nonzero labels | Proved | Lemma 3.3 |
| Absolute elementary-differential/time-simplex majorant alone yields subexponential control | Refuted for that majorant | Proposition 4.1, on an actual internal feature family |
| Actual physical \(q\) has compact-time subexponential tails | Open | Need a source estimate preserving nonlinear cancellations and physical correlations |
| Sine-preserving nonlinear Picard scheme converges strongly for every finite horizon | Open | No closed reached-state estimate for (5.1) |
| Global autonomous canonical strong solution, bounded-primal uniqueness, restartability | Open | No construction/uniqueness bridge from conditional linear control |
| Full actual finite-width GF/raw-GD joint limit and named observables | Open | No uniform approximation or strong identification theorem supplied |

The strongest objection to treating the positive estimates as a global result is the unknown coefficient path in Section 2. The strongest objection to treating Proposition 4.1 as a negative theorem about the model is the exact bounded sine resummation after (4.6). Both objections are retained rather than hidden in constants or generic regularity language.

The narrow next mathematical target is a source estimate after bounded-sine subtrees have been resummed. A useful successful statement would control the true repeated-matrix return source, on energy-stopped physical paths, in a width-independent subexponential class on every finite horizon, or would replace that tail statement by a direct strong Cauchy estimate that handles (5.1). Until such a statement is proved, this branch supplies an exact skeleton and a proof-route obstruction, not a resolution of the contract.
