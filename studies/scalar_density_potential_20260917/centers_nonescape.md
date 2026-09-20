# Centers, balance, and readout nonescape: bounded independent route

Status: exact reductions and a statewise obstruction; the unconditional trajectory claim remains open. This is a scoped, prompt-only theoretical route. No other study material, numerical experiment, or external source was used. The required research and rigorous-mathematics skills and their relevant process references were read.

The target is a data-defined global learning/potential statement from the stipulated Gaussian initialization, retaining both hidden-layer dynamics. A conditional readout bound, initial positive Gram matrix, or replacement of the evolving metric by a fixed metric does not resolve that target.

## 1. Exact induced metric and elementary barriers

Write \(v_i=x_i/\sqrt2\), \(u_i(g)=w(g)\cdot v_i\), and \(P=\operatorname{diag}(p_1,p_2,p_3)\). All vector inner products below use the three sample coordinates, while the parameter norms use the stipulated Gaussian probability spaces. Let

\[
K_{ij}(w)=\mathbb E_1[b_1^2\phi'(u_i)\phi'(u_j)]\,v_i\cdot v_j,
\qquad h_i=p_i r_i d_i.
\]

Differentiating \(a_i=\mathbb E_1 b_1\phi(u_i)\) and substituting the supplied flow gives exactly

\[
\dot a=-2MKh,\qquad \dot M=-2a^Th,
\qquad \dot s=-2(M^2K+aa^T)h.
\tag{1}
\]

In particular, the center metric is \(A=M^2K+aa^T\), and it continues to depend on the full first-layer state. The matrix \(K\) is positive semidefinite because

\[
z^TKz=\mathbb E_1\left[b_1^2\left|\sum_i z_i\phi'(u_i)v_i\right|^2\right].
\]

The exact dissipation is

\[
-\dot L=4h^TAh+4\left\|\sum_i p_i r_i H_i\right\|_2^2.
\tag{2}
\]

Equations (1)–(2) retain both hidden layers; they do not close autonomously in \(s,c\).

At initialization \(L(0)=1\). If the initial readout velocity is nonzero, then \(L(t)<1\) for every \(t>0\): strict decrease holds initially and monotonicity then preserves the strict inequality. At any state with \(M=0\), all outputs vanish and \(L=1\). Since the supplied \(M_0>0\), continuity therefore gives

\[
M(t)>0\quad\text{for every finite }t.
\tag{3}
\]

The same argument excludes \(a(t)=0\) at finite positive times. Neither assertion supplies an all-time positive lower bound. Initial linear independence of the three \(H_i\) suffices for nonzero initial readout velocity, because all \(p_i y_i\) are nonzero.

## 2. Why the usual balance identity does not hold

Direct differentiation gives

\[
\frac12\frac d{dt}\|c\|_2^2=-2\sum_i p_i r_i f_i,
\qquad
\frac12\frac d{dt}M^2=-2\sum_i p_i r_i s_i d_i.
\]

Consequently

\[
\frac d{dt}(\|c\|_2^2-M^2)
=-4\sum_i p_i r_i\,
\mathbb E_2 c\,[\tanh(bs_i)-bs_i\operatorname{sech}^2(bs_i)].
\tag{4}
\]

The bracket has the sign of \(bs_i\), but neither \(c\) nor the individual residuals have a supplied sign restriction. Thus (4) is not a conserved quantity or a signed inequality.

The defect is small in a precisely limited sense near zero. For real \(z\),

\[
|\tanh z-z\operatorname{sech}^2z|\le \frac23|z|^3.
\]

For \(z\ge0\), this follows by differentiating the left-hand expression, obtaining \(2z\operatorname{sech}^2z\tanh z\le2z^2\), and integrating from zero; oddness gives the other half-line. Set \(B=\|b\|_\infty\) and \(A_0=\mathbb E_1|b_1|\), so \(|s_i|\le A_0|M|\). Cauchy–Schwarz then yields

\[
\left|\frac d{dt}(\|c\|_2^2-M^2)\right|
\le\frac83 B^3A_0^3|M|^3\|c\|_2\sqrt L.
\tag{5}
\]

This is an exact bound, but no integrability of its right-hand side follows from the supplied dissipation. Treating (5) as an asymptotic balance law would assume the missing result.

A corresponding pointwise Euler identity for the first layer is impossible for three pairwise nonparallel directions. Such an identity would need a vector field \(F(w)\in\mathbb R^2\) satisfying

\[
F(w)\cdot v_i=\frac{\tanh(w\cdot v_i)}{\operatorname{sech}^2(w\cdot v_i)}
=\tfrac12\sinh(2w\cdot v_i),\qquad i=1,2,3.
\tag{6}
\]

Since \(v_1,v_2\) are independent, write \(v_3=\lambda v_1+\mu v_2\). Pairwise nonparallelness gives \(\lambda\mu\ne0\). With \(u=w\cdot v_1\), \(v=w\cdot v_2\), (6) would imply

\[
\sinh(2\lambda u+2\mu v)=\lambda\sinh(2u)+\mu\sinh(2v)
\]

for all \(u,v\). The mixed cubic coefficient on the left is nonzero, while the right has no mixed term. This contradiction rules out this pointwise homogeneity-based construction. It does not rule out a nonlocal or trajectory-specific invariant.

## 3. Positivity of the readout is not a sufficient invariant

Oddness permits the exact sign transformation \(v_i\mapsto y_i v_i\), \(a_i\mapsto y_i a_i\), \(s_i\mapsto y_i s_i\), \(f_i\mapsto y_i f_i\), after which all targets are \(+1\). The readout remains odd in \(b\), since it starts at zero and its velocity is a combination of odd functions.

Suppose \(c(b)\ge0\) for \(b>0\), with \(c\) nonzero, and suppose two transformed centers satisfy \(0<s_i<s_j\). Symmetry of the law of \(b\) gives

\[
f_j-f_i=2\int_0^B c(b)[\tanh(bs_j)-\tanh(bs_i)]\,\rho(b)\,db>0,
\]

where \(\rho\) is the positive density of \(b\) on its interior. Therefore such a readout cannot fit equal positive labels at distinct finite positive centers. A proof using this cone must additionally prove controlled center coalescence or escape, or must allow the signed readout cancellations needed for distinct-center interpolation. Positivity alone leaves the main difficulty intact.

## 4. Exact low-loss, arbitrarily small-dissipation states

The following construction is a rigorous obstruction to a loss-only dissipation inequality on the entire low-loss state set. It is not a trajectory counterexample.

### 4.1 Hermite interpolation in the readout space

For three nonzero centers with distinct absolute values, the six functions

\[
H_{s_i}(b)=\tanh(bs_i),\qquad
J_{s_i}(b)=b\operatorname{sech}^2(bs_i),\qquad i=1,2,3,
\tag{7}
\]

are linearly independent in \(L^2(\rho)\).

To prove this, suppose \(\sum_i[u_i H_{s_i}+v_i J_{s_i}]=0\) in that space. The density is positive on an interval containing zero. The continuous analytic function in question therefore vanishes throughout that interval. Write

\[
\tanh z=\sum_{k\ge0}t_kz^{2k+1}.
\]

The first six coefficients are

\[
1,-\tfrac13,\tfrac2{15},-\tfrac{17}{315},
\tfrac{62}{2835},-\tfrac{1382}{155925},
\]

all nonzero; they follow recursively from \(T'=1-T^2\), \(T(0)=0\). Comparing the first six coefficients gives

\[
\sum_i [u_i s_i+v_i+2kv_i](s_i^2)^k=0,
\qquad k=0,\ldots,5.
\tag{8}
\]

Let \(z_i=s_i^2>0\), \(A_i=u_i s_i+v_i\), and \(B_i=2v_i\). Equation (8) says that the functional

\[
Q\longmapsto\sum_i[A_iQ(z_i)+B_i z_i Q'(z_i)]
\]

vanishes on every polynomial of degree at most five. The map from such polynomials to their three values and three derivatives at the distinct nodes \(z_i\) is bijective: its kernel would have three double roots and hence degree at least six. Thus all \(A_i,B_i\) vanish, and then all \(u_i,v_i\) vanish.

The Gram matrix of (7) is consequently positive definite. For every prescribed \(F\in\mathbb R^3\), there is a finite-norm odd \(c\), in the span of (7), satisfying

\[
\mathbb E cH_{s_i}=F_i,\qquad
\mathbb E cJ_{s_i}=0,\qquad i=1,2,3.
\tag{9}
\]

The second set of equations says exactly \(d_i=0\).

### 4.2 Hidden parameters can stay bounded, with \(M=M_0\)

Take admissible inputs

\[
v_i=(\xi_i,\sqrt{1-\xi_i^2}),\qquad
(\xi_1,\xi_2,\xi_3)=(1/4,1/2,3/4),
\]

with the supplied labels \(+,+,-\) and any supplied \(q\in(0,1)\). The directions are pairwise nonparallel.

This data example also has three distinct nonzero absolute centers at the prescribed initialization. Indeed, for \(U_\xi=\xi g_1+\sqrt{1-\xi^2}g_2\), Gaussian integration by parts in \(g_1\) and \(g_2\) gives

\[
\frac d{d\xi}\mathbb E[b_1\tanh U_\xi]
=\mathbb E[b_1'(g_1)\operatorname{sech}^2U_\xi]>0.
\]

The terms involving the second derivative of tanh cancel. The expectation is zero at \(\xi=0\), so it is positive and strictly ordered at the three displayed values. The initial three readout features are therefore independent by the argument in Section 4.1.

To keep every constructed state in the bounded-displacement class obeyed by the flow at finite times, take a smooth even cutoff \(\chi\in[0,1]\), equal to one on \([-1,1]\) and zero outside \([-2,2]\). For \(0<\varepsilon<e^{-1}\), put

\[
R_\varepsilon=\sqrt{10\log(1/\varepsilon)},\qquad
\chi_{R_\varepsilon}(u)=\chi(u/R_\varepsilon),
\]

and consider the states

\[
w_\varepsilon(g)=
\left([1-(1-\varepsilon)\chi_{R_\varepsilon}(g_1)]g_1,g_2\right),
\qquad M_\varepsilon=M_0.
\tag{10}
\]

These first-layer states satisfy

\[
\|w_\varepsilon\|_2\le\sqrt2,\qquad
\|w_\varepsilon-g\|_\infty\le2R_\varepsilon<\infty.
\]

They preserve odd parity in the first Gaussian coordinate and leave the fixed set \(g_1=0\) unchanged. They are not asserted to be reachable. The bounded-displacement constant may grow with \(\varepsilon^{-1}\); each individual state's displacement is bounded. The cutoff corrects the earlier unbounded-displacement ambient contraction \(\widetilde w_\varepsilon=(\varepsilon g_1,g_2)\).

The elementary Gaussian Chernoff bound gives

\[
\mathbb P(|g_1|>R_\varepsilon)
\le2e^{-R_\varepsilon^2/2}=2\varepsilon^5.
\]

Indeed, \(\mathbb E e^{tG}=e^{t^2/2}\), and Markov's inequality with \(t=R_\varepsilon\) bounds each one-sided tail. The cutoff state agrees with \(\widetilde w_\varepsilon\) on \(|g_1|\le R_\varepsilon\). Boundedness of tanh and \(b_1\) therefore yields, for every sample direction,

\[
|a_i(w_\varepsilon)-a_i(\widetilde w_\varepsilon)|
\le2\|b_1\|_\infty\mathbb P(|g_1|>R_\varepsilon)
\le4\|b_1\|_\infty\varepsilon^5.
\]

Taylor expansion for \(\widetilde w_\varepsilon\), with bounded derivatives of tanh and finite Gaussian moments, followed by this \(O(\varepsilon^5)\) cutoff estimate, gives

\[
a_{i,\varepsilon}=\varepsilon C\xi_i
\mathbb E\operatorname{sech}^2(\sqrt{1-\xi_i^2}\,G)
+O(\varepsilon^3),
\qquad C=\mathbb E[b_1g_1]>0.
\tag{11}
\]

The constant term is zero because \(\mathbb E b_1=0\); the quadratic term is zero because \(b_1g_1^2\) is odd in \(g_1\). The displayed leading coefficient is strictly increasing in \(\xi\in(0,1)\): its first factor increases strictly, and its expectation increases because \(\operatorname{sech}^2z\) strictly decreases with \(|z|\). Consequently the centers \(s_{i,\varepsilon}=M_0a_{i,\varepsilon}\) are positive, nonzero, pairwise distinct, and of order \(\varepsilon\), for sufficiently small positive \(\varepsilon\).

Fix any \(\ell\in(0,p_{\min})\). Choose a residual vector \(\delta_\varepsilon\) satisfying

\[
\sum_i p_i\delta_{i,\varepsilon}s_{i,\varepsilon}=0,
\qquad
\sum_i p_i\delta_{i,\varepsilon}s_{i,\varepsilon}^3=0,
\qquad
\sum_i p_i\delta_{i,\varepsilon}^2=\ell.
\tag{12}
\]

The first two rows have rank two, since the three squared centers are distinct. Their one-dimensional nullspace can therefore be normalized to satisfy the last equality. The residual components are uniformly bounded by \(\sqrt{\ell/p_i}\).

Use (9) to choose \(c_\varepsilon\) with \(F_i=y_i+\delta_{i,\varepsilon}\) and all \(d_i=0\). At these states,

\[
L=\ell,\qquad \dot w=0,\qquad \dot M=0.
\tag{13}
\]

The first two terms of the tanh expansion cancel by (12). Boundedness of \(b\) and the centers therefore gives

\[
\dot c_\varepsilon
=-2\sum_i p_i\delta_{i,\varepsilon}\tanh(bs_{i,\varepsilon})
=O_{L^2}(\varepsilon^5).
\tag{14}
\]

Thus the total dissipation is \(O(\varepsilon^{10})\), while the loss is the fixed positive number \(\ell<p_{\min}\). In contrast, the readout norm necessarily diverges: since \(|\delta_i|<1\), every \(|F_i|\) is bounded below by \(1-\sqrt{\ell/p_{\min}}>0\), and

\[
|F_i|\le\|c_\varepsilon\|_2\|H_{s_i}\|_2
\le B|s_i|\,\|c_\varepsilon\|_2.
\]

Hence \(\|c_\varepsilon\|_2\ge C_\ell/\varepsilon\).

This proves that no inequality \( -\dot L\ge\Psi(L)>0\) can hold on all finite states with \(0<L<p_{\min}\), even if the first-layer norm is uniformly bounded and \(M\) is fixed at its positive initialization. The same construction excludes a positive data-only rate for a differentiable scalar potential \(V=F(L)\) with finite positive \(F'(\ell)\) and \(F(\ell)>0\), when claimed on that entire state set. It does not exclude such a bound on the actual reachable trajectory, or for a potential retaining additional state.

## 5. Saturation is not itself a verified escape trajectory

There is another reason not to identify bounded readout norm with bounded centers. For a fixed odd readout that is \(C^3\) near zero, let \(c_1=c'(0)\), let \(\rho_0=\rho(0)>0\), and define

\[
F_\infty=\mathbb E[c(b)\operatorname{sign}b],\qquad
\kappa=2\rho_0\int_0^\infty u(1-\tanh u)\,du>0.
\]

For positive \(s\to\infty\), a change of variables \(u=bs\) yields

\[
f(s)=F_\infty-\kappa c_1s^{-2}+O(s^{-4}),\qquad
d(s)=2\kappa c_1s^{-3}+O(s^{-5}).
\tag{15}
\]

The density is even and smooth near zero, so \(c(b)\rho(b)=c_1\rho_0b+O(b^3)\). Outside a fixed neighborhood of zero, the tanh defect and its derivative decay exponentially, which justifies the stated remainders for a fixed \(L^2\) readout with the stated local regularity. Uniform use along a trajectory would require uniform versions of these hypotheses; none is supplied.

This shows how different large positive centers can produce nearly equal outputs with bounded readout. However, retaining the first hidden layer changes the naive escape picture. To see the scale of that correction, suppose the transformed labels are all \(+1\), all \(a_i>0\) stay away from zero, and the leading common output has equilibrated so that \(\sum_i p_i r_i=O(M^{-4})\). Write \(D=\kappa c_1\), \(m_2=\sum_i p_i a_i^{-2}\). Formula (15) then gives the following diagnostic leading terms:

\[
\dot M=4D^2M^{-5}
\left[\sum_i p_i a_i^{-4}-m_2^2\right]+O(M^{-7}),
\tag{16}
\]

\[
\dot a=-4D^2M^{-4}K
\bigl(p_i[m_2a_i^{-3}-a_i^{-5}]\bigr)_{i=1}^3
+O(M^{-6}).
\tag{17}
\]

The leading \(M\)-drift is nonnegative, but the first-layer center changes occur one power of \(M\) faster. Therefore freezing \(a\) to infer a polynomial-decay countertrajectory would discard a potentially decisive mechanism. Degeneration of \(K\), time variation of the readout near \(b=0\), and center equalization must all be resolved before drawing a trajectory conclusion. Equations (16)–(17) are a conditional asymptotic diagnostic, not a proved long-time regime of the initialized flow.

## 6. Exact remaining gap and route disposition

The permitted stationary-loss lemma says that once the actual trajectory has \(L(T)<p_{\min}\), a finite \(\liminf_{t\to\infty}\|c(t)\|_2\) is sufficient for \(L(t)\to0\). This route has not proved either subthreshold entry or that readout bound from the prescribed data and initialization.

The major unresolved implication is a trajectory-specific exclusion of large signed readout cancellations, or another mechanism that controls their contribution while keeping the evolving first-layer metric. The arbitrary-state construction above shows why bounds using only the loss, bounded hidden parameters, and a positive \(M\) cannot supply that exclusion. It does not show that the initialized flow ever approaches those constructed states.

Route status: blocked at the reachability/nonescape step. Reopen only with an actual sign-variation restriction on the generated readout, a coercive trajectory identity beyond the failed homogeneity balance, or an estimate tying readout norm growth to a quantified loss decrease. No unconditional exponential potential or global learning theorem has been established here.
