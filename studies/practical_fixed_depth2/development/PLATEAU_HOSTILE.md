# Independent hostile development: protected plateau features

2026-09-08. This note was developed from `CONTRACT.md`, without reading another route's mathematical report. No experiments were used. It tests the original, jointly trained, two-hidden-layer field; it does not freeze a training block by changing the architecture.

## Conclusion and claim level

A fixed bounded smooth activation with two different plateaus really does produce an invariant positive first-layer sample-feature Gram. This remains true for the admitted singular input Grams. The mechanism also yields a useful coercive energy estimate and an exact representation of integrated backward sources.

However, a positive protected feature Gram does **not** imply a positive true kernel, fitting, a residual clock integrable on the half-line, nondegenerate temporal innovations, or uniform integrability of the reused Gaussian-matrix sources. There are exact trajectories of the original finite model, with positive protected Gram, on which every training block follows its prescribed field and mixed labels are never fitted. Such trajectories occur on positive-probability finite Gaussian-initialization events. These events do not refute the required full-sequence convergence in probability or a typical population result.

Bounded activation supplies a separate, stronger compact-time fact: the readout, backward gate field, learned operator kernel, and explicit learned-operator returns have uniform pointwise bounds. The remaining unresolved source estimates concern the **actual reused initial Gaussian matrix**. The observations below do not complete or contradict the global population/finite-width target.

## 1. An explicit distinct fixed activation

Let

\[
\rho(s)=\begin{cases}\exp[-1/(1-s^2)],&|s|<1,\\0,&|s|\ge1,\end{cases}
\qquad I=\int_0^1\rho(s)\,ds,
\]

and define

\[
\phi(z)=1+I^{-1}\int_0^{z/2}\rho(s)\,ds.
\]

This is a single fixed \(C^\infty\) activation, independent of data, width, separation and horizon. It equals zero on \(( -\infty,-2]\), equals two on \([2,\infty)\), and is strictly increasing between the plateaus. It is distinct from the contract's affine–tanh activation. Its height and transition width are moderate fixed constants. For example,

\[
0\le\phi\le2,\qquad
\|\phi'\|_\infty=\frac{e^{-1}}{2I}
\le e^{1/3}<1.4,
\]

where \(I\ge \frac12e^{-4/3}\). All higher derivatives are bounded. Write \(M=\|\phi\|_\infty=2\), \(L=\|\phi'\|_\infty\), and \(R_*=2\).

The following geometric argument applies equally to any bounded smooth activation with distinct constant values \(a_-\ne a_+\) outside a fixed interval \([-R_*,R_*]\).

## 2. The protected Gram is genuinely positive

Set \(u_i=x_i/\sqrt d\), so \(\|u_i\|=1\), and use the rescaled first-layer variable \(w=\sqrt d W\). At initialization define

\[
F=\{\omega_1:|w_0(\omega_1)\cdot u_i|>R_*\text{ for every }i\},
\quad P=1_F,
\quad g_i=P\phi(w_0\cdot u_i).
\]

Here \(P\) acts by multiplication on the first-layer Hilbert space. The protected Gram is

\[
Q_{ij}=\langle g_i,g_j\rangle_{H_1}.
\]

**Lemma 1.** The population matrix \(Q\) is positive definite for every admitted input triple, including singular input Grams.

**Proof.** Work in the linear span of the inputs. No two input vectors are parallel, since their correlations have absolute value strictly less than one. For each \(i\), choose a vector \(v\perp u_i\) with \(v\cdot u_j\ne0\) for both \(j\ne i\). Such a vector exists: each forbidden condition is a proper subspace of \(u_i^\perp\), and a real vector space is not the union of finitely many proper subspaces.

Choose \(B>R_*\), then choose \(N\) so large that

\[
N|v\cdot u_j|>R_*+B|u_i\cdot u_j|\qquad(j\ne i).
\]

The points \(Nv+Bu_i\) and \(Nv-Bu_i\) belong to open protected plateau cells. Their feature vectors differ by exactly \((a_+-a_-)e_i\): sample \(i\) switches plateau, while the other two samples stay on their respective plateaus. Both open cells have positive Gaussian probability in the input span. If \(a^TQa=0\), then \(a\cdot g=0\) almost surely and therefore on each of these constant-feature cells. Subtraction gives \((a_+-a_-)a_i=0\). Doing this for each \(i\) gives \(a=0\). ∎

There is also a separation-dependent uniform constant. Let

\[
\mathcal G_\delta=\{\Gamma\succeq0:\Gamma_{ii}=1,
\ |\Gamma_{ij}|\le1-\delta\ (i\ne j)\}.
\]

The matrix \(Q\) is continuous as a function of \(\Gamma\), including at singular matrices. Indeed, centered Gaussian vectors converge weakly when their covariance matrices converge; the integrand defining each entry is bounded, and its only discontinuities lie on \(Z_i=\pm R_*\), which have probability zero because every marginal is standard normal. The set \(\mathcal G_\delta\) is compact and Lemma 1 applies everywhere on it. Thus

\[
\lambda_\delta:=\min_{\Gamma\in\mathcal G_\delta}
\lambda_{\min}(Q(\Gamma))>0.
\]

This is a proved positive constant, not a useful numerical lower bound. No activation coefficient is being chosen through it.

For finite width, let \(P_n\) select the initialized protected neurons and define

\[
(Q_n)_{ij}=\frac1n\sum_{k=1}^n
1_{F_k}h_{i,k}(0)h_{j,k}(0).
\]

The summands are iid and bounded by \(M^2\) in absolute value. Consequently

\[
\mathbb E\|Q_n-Q\|_F^2\le\frac{9M^4}{n},
\qquad
\mathbb P\{Q_n\not\succeq\tfrac12\lambda_\delta I\}
\le\frac{36M^4}{n\lambda_\delta^2}.
\]

These statements use only first-layer Gaussian initialization.

## 3. Invariance uses the actual first-layer equation

The rescaled finite equation, and the analogous equation along any field-defined population path, are

\[
\dot w=-\sum_i r_i\phi'(w\cdot u_i)q_i u_i.
\]

At a protected initial neuron all three gates vanish. Keeping this neuron's \(w\) fixed is therefore an exact solution of its equation even though all other neurons and all other training blocks continue evolving. Finite-dimensional local uniqueness gives

\[
Pw(t)=Pw_0,\qquad Ph_i(t)=g_i\quad(t\ge0).
\]

For a population path the same conclusion is conditional only on enough integrability to interpret the displayed field, for example

\[
\int_0^T\sum_i |r_i(t)|\|q_i(t)\|_{H_1}\,dt<\infty.
\]

Fubini gives pointwise integrable forcing coefficients almost everywhere. Since \(\phi'\) is Lipschitz, the pointwise difference from the constant solution satisfies an ordinary integral Gronwall inequality with these coefficients. It is zero. This proves an invariant of an existing strong solution; it does not construct that solution.

Thus, writing \(H_{ij}(t)=\langle h_i(t),h_j(t)\rangle\),

\[
H(t)=Q+\big[\langle(1-P)h_i(t),(1-P)h_j(t)\rangle\big]
\succeq Q\succeq\lambda_\delta I.
\]

The corresponding finite statement holds with \(Q_n\).

## 4. Two exact consequences stronger than mere invertibility

Use normalized finite Hilbert spaces, or the actual population spaces when a solution has been constructed. Write \(A=A_0+U\), and let

\[
G:\mathbb R^3\to H_1,\qquad Ge_i=g_i,
\qquad G^*G=Q.
\]

The exact operator equation is

\[
\dot U=-\sum_i r_i\,b_i\otimes h_i.
\]

**Coercivity of individual backward forces.** Projection on the protected input subspace gives

\[
\|\dot U\|_{HS}^2\ge\|\dot U P\|_{HS}^2
=\sum_{ij}Q_{ij}r_i r_j\langle b_i,b_j\rangle
\ge\lambda_\delta\sum_i r_i^2\|b_i\|^2.
\]

The last inequality follows by diagonalizing \(Q\), or applying \(Q\succeq\lambda_\delta I\) to the Gram matrix of the vectors \(r_i b_i\). The exact energy identity therefore implies

\[
\int_0^T\sum_i r_i(t)^2\|b_i(t)\|^2\,dt
\le\frac{E(0)-E(T)}{\lambda_\delta}
\le\frac{E(0)}{\lambda_\delta}.
\tag{4.1}
\]

This removes cancellation among sample forces, including when the input Gram is singular. It does not bound \(\|b_i\|\) by itself where \(r_i\) is small, nor does it bound \(\int_0^\infty|r_i|\).

**An exact primitive identity.** Since \(\langle h_i(t),g_j\rangle=Q_{ij}\),

\[
\frac d{dt}(UGQ^{-1})=-\sum_i r_i b_i e_i^T.
\]

Using \(U(0)=0\),

\[
J_i(t):=\int_0^t r_i(s)b_i(s)\,ds
=-U(t)GQ^{-1}e_i.
\tag{4.2}
\]

In particular,

\[
\|J_i(t)-J_i(s)\|
\le\lambda_\delta^{-1/2}\|U(t)-U(s)\|_{HS}
\le\sqrt{\frac{(t-s)(E(s)-E(t))}{\lambda_\delta}}.
\]

The primitive identity does not control arbitrary time-dependent multipliers of \(r_i b_i\). Inserting moving first-layer gates and integrating by parts introduces their derivatives and hence the backward source again.

## 5. Bounded activation controls all explicit learned-operator returns

This part does not require the protected Gram. Define the physical residual clock

\[
\mathcal R(t)=\int_0^t\sum_i|r_i(s)|\,ds.
\]

Energy monotonicity gives the compact-time estimate

\[
\mathcal R(t)\le\sqrt{6E(0)}\,t.
\]

If \(c_0=\|C(0)\|_\infty\), then the **actual** readout equation implies

\[
\|C(t)\|_\infty\le c_0+M\mathcal R(t),
\qquad
\|b_i(t)\|_\infty\le L(c_0+M\mathcal R(t)).
\tag{5.1}
\]

The learned operator has the integral kernel

\[
u_t(\omega_2,\omega_1)=
-\sum_i\int_0^t r_i(s)b_i(s,\omega_2)h_i(s,\omega_1)\,ds.
\]

It follows pointwise that

\[
\|u_t\|_\infty
\le ML\left(c_0\mathcal R(t)+\frac M2\mathcal R(t)^2\right)
=:\mathcal U(t).
\tag{5.2}
\]

In the finite model the corresponding kernel is \(nU_{jk}\), since the actual update contains \(1/n\). Thus (5.2) respects the contract's normalization and retains simultaneous training of \(W,A,C\).

On probability spaces,

\[
\|Uh_i\|_\infty\le M\mathcal U(t),
\qquad
\|U^*b_i\|_\infty
\le L(c_0+M\mathcal R(t))\mathcal U(t).
\tag{5.3}
\]

For population initialization \(C(0)=0\), these simplify to

\[
\|u_t\|_\infty\le\tfrac12M^2L\mathcal R^2,
\quad
\|Uh_i\|_\infty\le\tfrac12M^3L\mathcal R^2,
\quad
\|U^*b_i\|_\infty\le\tfrac12M^3L^2\mathcal R^3.
\]

Finite small random readout initialization is retained: \(c_0\) is finite for every finite realization and tends to zero in probability under \(C_j(0)\sim N(0,n^{-2})\). The latter follows, for example, by the union bound and the standard Gaussian tail bound.

These are conditional a priori estimates on existing paths, with bounds independent of width on bounded-energy initialization events. They do not presuppose a finite half-line residual clock.

They sharply locate the unclosed terms:

\[
v_i=A_0h_i+Uh_i,
\qquad q_i=A_0^*b_i+U^*b_i.
\]

The explicit \(U\)-returns are bounded. The reused \(A_0\)-actions still need their actual Gaussian-program source/adjoint analysis. Replacing them by an arbitrary easier operator would change the target.

## 6. A positive protected Gram cannot imply a true kernel floor

Here is a counterexample **inside the original finite model**, even with its stipulated Gaussian initialization.

Fix mixed labels and a width for which the initialized first-layer feature matrix has rank three and its protected Gram is positive. Such first-layer configurations have positive probability: Lemma 1 supplies finitely many open protected cells whose feature vectors span \(\mathbb R^3\), and independent neurons can fall into those cells. Additional neurons can be arbitrary.

Conditional on any such initialized feature matrix, every second-layer row has a centered Gaussian preactivation vector with positive-definite covariance \(H_n\). Hence the event

\[
v_{j,i}(0)>R_*\qquad\text{for every second-layer row }j
\text{ and sample }i
\tag{6.1}
\]

has strictly positive conditional probability. On (6.1), all second-layer features are the same plateau value \(M\), and all second-layer derivative gates are zero. Consequently

\[
b_i=0,\quad q_i=0,\quad \dot W=0,\quad\dot A=0.
\]

The readout still follows its **original** equation. Writing \(s(t)=\langle C(t),1\rangle_n\),

\[
f_i(t)=Ms(t),\qquad
\dot s=-M\sum_i(Ms-y_i).
\]

Therefore \(f_i(t)\to\bar y=\frac13\sum_i y_i\), and

\[
E(t)\longrightarrow\frac12\sum_i(y_i-\bar y)^2>0.
\]

The true first and second kernel blocks vanish, while the readout block is \(M^2\mathbf1\mathbf1^T\), of rank one. The protected first-layer Gram remains positive at all times.

The event respects the small Gaussian readout initialization; no special readout value is required. It also works for singular input Grams, because the feature rank argument did not require nonsingular input geometry.

**Exact consequence:** there is no deterministic implication from a positive protected first-layer Gram to a positive full sample kernel, global fitting, or a finite half-line residual clock.

**Limitation:** this is a rare finite-width initialization event; its probability is not bounded away from zero as width grows. It neither contradicts convergence in probability nor proves that a population solution fails to fit. The principal contract does not require fitting in the first place.

A related tempting inference is independently false. A second-layer row that is initially on plateaus need not stay there merely because its own parameter derivative vanishes. Its preactivation derivative contains

\[
\dot v_{j,i}=(\dot A h_i)_j+(A\dot h_i)_j.
\]

The second term remains. The globally saturated event (6.1) is invariant because it makes **all** backward signals vanish and hence also freezes \(h\). A row-by-row second-layer protection argument does not have this property.

## 7. Further invalid implications and the surviving source gap

### 7.1 Current Gram versus temporal innovation

Protected components cancel from temporal differences:

\[
P(h_i(t)-h_i(s))=0.
\]

Thus \(H(t)\succeq Q\) gives no positive lower bound for the Gram of feature increments or for a Gaussian innovation conditioned on earlier forward actions. For example, constant-in-time features have a positive current three-sample Gram but a singular six-vector Gram at two times. In a genuine Gaussian-program expansion, inverses or innovation bounds involving the whole causal history require a separate argument.

### 7.2 A protected additive source is not automatically independent noise at the current state

The decomposition

\[
A_0h_i(t)=A_0g_i+A_0(1-P)h_i(t)
\]

is exact. At initialization the Gaussian matrix restrictions to the protected and unprotected column spaces are independent, conditional on the initialized first layer. However, the evolving unprotected features depend on the backward signals, which depend on \(A_0g_i\). One cannot condition on the trained state and retain independence of the first term without proof. Nor does independence of primitive Gaussian sources make an adaptive shift independent of those sources.

### 7.3 Bounded inputs and Gaussian spectral norm do not give source-tail control

Here is an exact warning involving the **actual Gaussian matrix law**, not an easier replacement operator. Let

\[
(A_0)_{jk}=G_{jk}/\sqrt n,\qquad b_j=\tanh(G_{j1}).
\]

Then \(|b_j|\le1\), but

\[
(A_0^Tb)_1=\frac1{\sqrt n}\sum_{j=1}^nG_{j1}\tanh(G_{j1}),
\qquad
\frac{(A_0^Tb)_1}{\sqrt n}\longrightarrow
\mu:=\mathbb E[G\tanh G]>0
\]

in probability. Consequently, for every fixed threshold \(K\),

\[
\liminf_{n\to\infty}\frac1n\sum_{k=1}^n
|(A_0^Tb)_k|^2\mathbf1_{\{|(A_0^Tb)_k|>K\}}
\ge\mu^2
\]

in probability, in the sense that the displayed quantity exceeds every constant smaller than \(\mu^2\) with probability tending to one. The normalized second moment contains a spike and is not uniformly integrable. A bounded feature family with a positive protected Gram can coexist with this construction; that Gram places no restriction on the chosen dependence of \(b\) on this matrix column.

**Scope of this warning:** this \(b\) is not asserted to be reachable as \(\phi'(v_i)C\) from the contract's physical initialization at a fixed horizon. It refutes a proposed deduction from bounded \(b\), the Gaussian matrix law, and operator-norm/Gram bounds alone. Proving that physical training cannot build such concentration is precisely a reachable-source or sensitivity estimate; it cannot be omitted.

### 7.4 Ambient strong continuity is not a local Lipschitz bound

Even if an actual canonical realization provides a bounded initial operator on the relevant Hilbert closure, the first-layer comparison contains

\[
\big(\phi'(z)-\phi'(\widetilde z)\big)q.
\]

A fixed \(q\in L^2\) and bounded continuous gates give continuity by dominated convergence and approximation. A bound proportional to \(\|z-\widetilde z\|_2\), uniform on an \(L^2\) ball of \(q\)'s, does not follow. Compact support of \(\phi'\) does not by itself bound \(q\) on the active set. This is relevant to uniqueness and to removal of truncation: bounded activation repairs several forward growth terms, but it is not an ambient Hilbert-space local-Lipschitz theorem.

## 8. Initial positivity and the exact remaining obligation

At population initialization, \(C=0\), so the true kernel is its readout block. The initial second-layer Gaussian vector has covariance \(H(0)\succeq Q\succ0\). Its density is positive everywhere. If

\[
\mathbb E\left(\sum_i a_i\phi(V_i)\right)^2=0,
\]

continuity and full support imply \(\sum_i a_i\phi(v_i)=0\) for every \(v\in\mathbb R^3\). Varying one coordinate and using nonconstancy of \(\phi\) forces each \(a_i=0\). Thus the initial readout kernel is positive definite. Continuity extends positivity over some local interval for any already-established continuous solution. This argument contains no all-time lower bound.

The most useful proved package is therefore:

1. fixed moderate bounded smooth nonlinearity;
2. invariant \(H(t)\succeq Q\succ0\), including singular input geometry;
3. individual-force action bound (4.1) and exact primitive identity (4.2);
4. compact-time pointwise bounds (5.1)–(5.3), retaining small finite readout initialization and every original training block;
5. initial positive true readout kernel.

The decisive unproved bridge is a compact-time, physically reachable bound or direct comparison theorem for the true reused Gaussian sources and their adjoints, strong enough for uniqueness/continuation and full-sequence convergence of the stated kernel and field-law observables. No result above supplies that bridge. In particular, the protected Gram must not be cited as if it did.
