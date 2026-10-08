# Exact spectral dynamics for two hidden linear layers

This is a restricted mechanistic example, not a solution of the nonlinear
deep-network closure problem. Both activations are linear, the readout starts
at zero, and there are exactly two hidden layers. Within this scope the
construction is exact for every finite width and every finite training and
passive evaluation panel. It eliminates evolving weight matrices and their
orientations, retaining a matrix-valued measure of energy and correlations
over the spectrum of one conserved operator.

The supervisor supplied the conserved-operator and spectral-measure route.
This note derives and checks it from the specified flow. Scientific inputs
were that assignment and the canonical conventions already read in this study;
no other study, literature, experiment, or Git operation was used. The optional
spectral coarsening result below is only a compact-time absolute-error theorem.
It is not an all-time or optimal-complexity approximation claim.

## 1. Model and a conserved operator

There are \(m\ge1\) training inputs and \(p-m\ge0\) passive inputs,
enumerated as \(v_1,\ldots,v_p\in\mathbb R^d\). Only the first \(m\)
have labels. Width is \(n\). Let

\[
A\in\mathbb R^{n\times d},\quad W\in\mathbb R^{n\times n},
\quad w\in\mathbb R^n,
\qquad h_a=Av_a,\quad z_a=Wh_a,\quad f_a=\frac1n w^\top z_a.
\]

Here \(h_a\) is the first hidden feature and \(z_a\) is also the second
hidden feature, since its activation is linear. On training indices set
\(c_b=y_b-f_b\), \(\alpha=2/m\), and
\(\mathcal L=m^{-1}\sum_{b=1}^m c_b^2\). The canonical mobilities
\((n,1,n)\) give

\[
\begin{aligned}
\dot A&=\alpha W^\top w\left(\sum_{b=1}^m c_bv_b\right)^\top,\\
\dot W&=\frac\alpha n w\left(\sum_{b=1}^m c_bh_b\right)^\top,\\
\dot w&=\alpha W\sum_{b=1}^m c_bh_b.
\end{aligned}
\tag{1}
\]

Let \(W(0)=G\) and \(w(0)=0\). Differentiating the two outer products in
the following expression gives cancellation term by term:

\[
\frac d{dt}\left(WW^\top-\frac1nww^\top\right)=0,
\qquad
WW^\top=D+\frac1nww^\top,\quad D=GG^\top.
\tag{2}
\]

For example, with \(g=\sum_bc_bh_b\),
\(\dot W W^\top+W\dot W^\top
=(\alpha/n)[w(Wg)^\top+(Wg)w^\top]\), exactly the derivative of
\(ww^\top/n\). No assumption on the input Gram or on singular values is
needed. The operator \(D\succeq0\) is fixed by initialization.

There is also a right-side balance law,

\[
W^\top W-\frac1nAA^\top
=G^\top G-\frac1nA(0)A(0)^\top.
\tag{3}
\]

Indeed \(\sum_bc_bh_b=A\sum_bc_bv_b\), and substitution into (1) makes
the two derivatives equal. Only (2) is needed for the spectral closure.

## 2. Feature similarities and independent linear modes

Define panel-wide observables

\[
S_{ab}=v_a^\top v_b,\qquad
C_{ab}=\frac1n h_a^\top h_b,\qquad
M=\frac1n\|w\|^2.
\]

Pad the training residual by zeros on passive indices, writing
\(\bar c=(c_1,\ldots,c_m,0,\ldots,0)^\top\in\mathbb R^p\), and put
\(d=S\bar c\), \(e=C\bar c\). These are actual residual-weighted
combinations of input and first-layer similarities.
Equation (1) gives

\[
\dot h_a=\alpha d_aW^\top w,
\qquad
\dot C=\alpha(df^\top+fd^\top),
\qquad
\dot M=2\alpha\bar c^\top f.
\tag{4}
\]

For the middle equation, differentiate \(h_a^\top h_b/n\) and use
\(w^\top Wh_b/n=f_b\). Differentiating \(z_a=Wh_a\) and using (2)
also gives

\[
\dot w=\alpha\sum_{b=1}^m c_bz_b,\qquad
\dot z_a=\alpha\big[e_aw+d_a(Dw+Mw)\big].
\tag{5}
\]

Choose an orthonormal eigenbasis of \(D\), with eigenvalues
\(\lambda_i\ge0\). Tildes denote coordinates in this fixed basis. At each
eigenvalue define

\[
\xi_i=(\widetilde w_i,\widetilde z_{1i},\ldots,
\widetilde z_{pi})^\top\in\mathbb R^{p+1}.
\]

Then (5) is the linear mode equation

\[
\dot\xi_i=\mathcal A_{\lambda_i}\xi_i,\qquad
\mathcal A_\lambda
=\alpha\begin{pmatrix}
0&\bar c^\top\\
e+(\lambda+M)d&0_{p\times p}
\end{pmatrix}.
\tag{6}
\]

The coefficients are shared nonlinear functions of the aggregate state, but
the dependence on a mode's own coordinates is linear. The fixed eigenvalue
\(\lambda\) measures the initialized middle layer's gain in that mode;
\(M\) is the common additional gain created by readout energy through (2).
These are not necessarily stable harmonic oscillators: the residual-weighted
coefficients can have either sign. Dissipation is a property of the coupled
training loss, checked below.

## 3. Closed matrix-valued spectral measure

Define a symmetric positive-semidefinite matrix-valued measure on
\([0,\infty)\) by

\[
\Sigma_t(d\lambda)=\frac1n\sum_{i=1}^n
\xi_i(t)\xi_i(t)^\top\,\delta_{\lambda_i}(d\lambda).
\tag{7}
\]

Its indices are \(0,1,\ldots,p\): index zero denotes readout, and index
\(a\ge1\) denotes the second-layer feature for panel input \(a\).
This definition does not depend on choices within degenerate eigenspaces.
More intrinsically, if \(P_D(E)\) is the orthogonal spectral projector of
\(D\) on a set \(E\), and \(X=[w,z_1,\ldots,z_p]\), then

\[
\Sigma_t(E)=\frac1n X(t)^\top P_D(E)X(t).
\]

Thus the measure records energy and cross-correlations at each initialized
gain, rather than learned matrix entries or eigenvector orientations.
Its exact closed evolution is

\[
\dot C=\alpha(df^\top+fd^\top),\qquad
\dot\Sigma(d\lambda)
=\mathcal A_\lambda\Sigma(d\lambda)
+\Sigma(d\lambda)\mathcal A_\lambda^\top
\tag{8}
\]

with reconstruction

\[
M=\int\Sigma_{00}(d\lambda),\qquad
f_a=\int\Sigma_{0a}(d\lambda),\qquad
c_b=y_b-f_b\ (b\le m),\qquad d=S\bar c,\ e=C\bar c.
\tag{9}
\]

The measure equation means the same equality after integration against any
bounded test function; for its finite spectral support it is simply one
matrix ODE at each distinct eigenvalue. Equation (6) proves (8) by
differentiating each \(\xi_i\xi_i^\top\). Conversely, (8)–(9) determine
all coefficients and all future reduced motion from the current reduced
state, labels, input Gram, and fixed spectral locations. There are no later
dense-network queries.

For any fixed coefficient path, each atom evolves as
\(\Sigma_j(t)=F_j(t)\Sigma_j(0)F_j(t)^\top\), where
\(\dot F_j=\mathcal A_{\lambda_j}F_j\), \(F_j(0)=I\).
This proves preservation of positive semidefiniteness, including rank-deficient
atoms. Inputs on the passive panel enter evaluated correlations and outputs
but never acquire a residual or an update force.

If there are \(s\le n\) distinct eigenvalues, the literal reduced state has
at most

\[
\frac{p(p+1)}2+s\frac{(p+1)(p+2)}2
\]

moving scalar coordinates, plus the fixed eigenvalues, input Gram, and labels.
Ranks and other compatibility conditions can reduce this count. For fixed
panel size it is linear in the number of spectral atoms, rather than storing
the \(n\times n\) learned middle matrix. It remains width dependent when
the initialized spectrum has \(n\) distinct values. This exact result does
not by itself give a width-independent finite state.

## 4. Initialization and its Gaussian law

The exact finite-width initial state is

\[
C_{ab}(0)=\frac1n(A_0v_a)^\top(A_0v_b),\qquad
\Sigma_0(d\lambda)=\frac1n\sum_i
\begin{pmatrix}0\\ \widetilde z_i^0\end{pmatrix}
\begin{pmatrix}0\\ \widetilde z_i^0\end{pmatrix}^{\!\top}
\delta_{\lambda_i}(d\lambda),
\]

where \(z_a^0=GA_0v_a\) and
\(\widetilde z_i^0=(\widetilde z_{1i}^0,\ldots,
\widetilde z_{pi}^0)^\top\). In particular \(M(0)=f(0)=0\).

Suppose \(A_0\) has iid standard Gaussian entries and is independent of
\(G\). Conditional on \(G\), in any eigenbasis selected from \(G\),
the vectors \(\widetilde z_i^0\) are independent centered Gaussian panel
vectors with

\[
\operatorname{Cov}(\widetilde z_i^0\mid G)=\lambda_i S.
\tag{10}
\]

Indeed the rows of \([A_0v_1,\ldots,A_0v_p]\) are independent Gaussian
vectors of covariance \(S\). Left multiplication by \(U^\top G\)
gives cross-row covariance
\((U^\top GG^\top U)_{ij}S=\delta_{ij}\lambda_iS\).
Joint Gaussianity turns zero cross-covariance into independence; when
\(\lambda_i=0\) the vector is identically zero.

The conditional mean measure is consequently

\[
\mathbb E[\Sigma_0(d\lambda)\mid G]
=\begin{pmatrix}0&0\\0&\lambda S\end{pmatrix}
\left(\frac1n\sum_i\delta_{\lambda_i}(d\lambda)\right).
\]

Replacing the realized measure by this mean is an approximation. Expectations
do not commute with the nonlinear coefficients in (8).
Also, \(C(0)\) is not independent of \(\Sigma_0\). If \(G\) is invertible,

\[
C_{ab}(0)=\int\lambda^{-1}\Sigma_{0,ab}(d\lambda),\qquad a,b\ge1.
\tag{11}
\]

To verify (11), use \(h_a^0=G^{-1}z_a^0\) and
\(G^{-\top}G^{-1}=(GG^\top)^{-1}\). For square iid Gaussian \(G\),
invertibility holds almost surely: each successive column has probability
zero of lying in the span of the preceding columns. For singular \(G\),
first-layer components in its right nullspace are absent from \(z^0\), so
\(C(0)\) must be retained separately as specified.

## 5. Observable kernel, additional constraints, and exact equivalence

Define two more spectral moments, evaluated directly from the retained measure:

\[
Z_{ab}=\int\Sigma_{ab}(d\lambda),\qquad
H=\int\lambda\Sigma_{00}(d\lambda).
\]

Integrating the \((0,a)\) entry of (8) gives

\[
\dot f=\alpha\mathcal K\bar c,\qquad
\mathcal K=Z+MC+(H+M^2)S.
\tag{12}
\]

The three terms are the exact contributions of readout learning, middle-layer
learning, and first-layer learning. For example,
\(H+M^2=n^{-1}\|W^\top w\|^2\) follows from (2).
On states produced by the network, \(C,Z,S\succeq0\) and \(M,H\ge0\);
therefore the training block of \(\mathcal K\) is positive semidefinite and

\[
\dot{\mathcal L}
=-\frac4{m^2}c^\top\mathcal K_{\mathrm{tr},\mathrm{tr}}c\le0.
\tag{13}
\]

The reduced equations also preserve a panel-wide balance law. Let \(S^+\)
be the inverse of \(S\) on its range and zero on its nullspace. Actual
panel outputs lie in \(\operatorname{range}S\), and
\(C\) has both row and column spaces in that range. These properties are
preserved by (8): \(d,e\) lie in the same range and the initial mode feature
vectors do too. Using (4),

\[
\frac d{dt}\operatorname{tr}(S^+C)
=2\alpha f^\top S^+S\bar c
=2\alpha\bar c^\top f=\dot M.
\]

Thus \(\operatorname{tr}(S^+C)-M\) is constant, including when \(S\) is
singular. Separately, (2) conserves
\(\|W\|_F^2-M=\operatorname{tr}D\).

When \(D\) is positive definite, even \(C\) can be reconstructed from
the spectral measure. Define

\[
\chi=\int\lambda^{-1}\Sigma_{00}(d\lambda),\qquad
t_a=\int\lambda^{-1}\Sigma_{0a}(d\lambda),\qquad
J_{ab}=\int\lambda^{-1}\Sigma_{ab}(d\lambda).
\]

Then the exact compatibility identity is

\[
C=J-\frac{tt^\top}{1+\chi}.
\tag{14}
\]

To derive it, (2) makes \(W\) invertible and
\(C_{ab}=n^{-1}z_a^\top(WW^\top)^{-1}z_b\).
Direct multiplication verifies

\[
(D+ww^\top/n)^{-1}
=D^{-1}-\frac{D^{-1}ww^\top D^{-1}/n}
{1+w^\top D^{-1}w/n},
\]

which yields (14). The denominator is at least one. The right-hand side is
positive semidefinite: it is the Schur complement of the positive block
matrix \(\int\lambda^{-1}\Sigma+\operatorname{diag}(1,0,\ldots,0)\).
One may therefore use (14) instead of evolving \(C\), although inverse
spectral weights can be sensitive to eigenvalues near zero.

For clarity, finite-width equivalence follows from ordinary ODE uniqueness,
not only from matching first derivatives. For each fixed initialized network,
there are finitely many atoms. Equations (8)–(9) form a polynomial ODE in
their symmetric entries and in \(C\), hence are locally Lipschitz. The exact
network observables solve this ODE with exactly the stated initial data.
Therefore every reduced solution with those data agrees with them for as long
as either solution exists. Compatibility, positivity of \(C\), and all
passive outputs are inherited throughout that interval. If (14) is used,
the rational denominator stays positive and the same uniqueness argument
applies. Arbitrary unrelated initial matrices are not claimed to correspond
to a network.

In fact the original finite-width linear gradient flow exists for all forward
times. With the mobility operator \(\mathsf M=\operatorname{diag}(n,1,n)\)
on parameter blocks, its energy identity is

\[
-\dot{\mathcal L}
=\dot\theta^\top\mathsf M^{-1}\dot\theta
=\frac1n\|\dot A\|_F^2+\|\dot W\|_F^2
+\frac1n\|\dot w\|^2.
\tag{15}
\]

Since the loss is nonnegative,
\(\int_0^T\|\dot\theta\|^2dt\le n\mathcal L(0)\) on every finite
existence interval. Cauchy--Schwarz bounds parameter displacement over
\([s,t]\) by \(\sqrt{n\mathcal L(0)}\sqrt{t-s}\). At a hypothetical finite
maximal time the parameters therefore have a finite limit. The polynomial
vector field is locally Lipschitz there and extends the solution, a
contradiction. The exact reduced solution consequently exists and agrees for
all \(t\ge0\). This proves global existence and equivalence, not uniform
boundedness as \(t\to\infty\) or convergence to zero training loss.

## 6. A complete but limited spectral coarsening result

There is an elementary compact-time approximation that replaces the exact
spectral locations by a finite mesh. It uses the realized initial measure,
including its finite-width fluctuations, rather than a population mean.

Assume \(\operatorname{spec}D\subset[0,\Lambda]\). Partition this interval
into bins of diameter at most \(\delta\), select one representative in each
bin, and move each initial matrix mass to its bin representative. Sum masses
whose representatives coincide. Retain the same \(C(0),S,y\), and evolve
(8)–(9), including the separate equation for \(C\). The number of atoms is
at most \(1+\lceil\Lambda/\delta\rceil\).

For every fixed physical horizon \(T<\infty\), this construction has error
\(O_T(\delta)\) in \(C,M,f,Z\) if \(\delta\) is sufficiently small.
The constants may depend on \(T,m,p,S,y,\Lambda,\operatorname{tr}C(0)\),
but not on width. Here are bounds and a stability argument establishing that
claim, including existence of the approximate system up to \(T\).

Write \(\mathcal L_0=\mathcal L(0)\). Equation (15) gives

\[
\begin{aligned}
M(t)&\le T\mathcal L_0,\\
\operatorname{tr}C(t)&\le
C_T:=\left(\sqrt{\operatorname{tr}C(0)}
+\sqrt{\|S\|}\sqrt{T\mathcal L_0}\right)^2,\\
\operatorname{tr}\!\int\Sigma_t(d\lambda)&\le
B_T:=T\mathcal L_0+
\left(\sqrt\Lambda+\sqrt{T\mathcal L_0}\right)^2C_T.
\end{aligned}
\tag{16}
\]

For the second bound, stack the panel inputs as columns of \(V\), use
\(\|V\|^2=\|S\|\), and bound
\(\|(A(t)-A_0)V\|_F/\sqrt n\) by
\(\sqrt{\|S\|T\mathcal L_0}\). For the third, use
\(\|W(t)\|\le\sqrt\Lambda+\sqrt{T\mathcal L_0}\) and
\(\sum_a\|Wh_a\|^2/n\le\|W\|^2\operatorname{tr}C\).

To compare exact and coarsened states, temporarily split every coarsened mass
back into its original initial summands, all evolving at the same representative
within a bin. Their sum exactly follows the coarsened equation because its
matrix evolution is linear at each fixed spectral location. Let
\(\Sigma_i(t),\widehat\Sigma_i(t)\) denote these paired masses, initially
equal, at locations differing by at most \(\delta\). Define

\[
E(t)=\|C(t)-\widehat C(t)\|_F
+\sum_i\|\Sigma_i(t)-\widehat\Sigma_i(t)\|_*,
\]

where \(\|\cdot\|_*\) is the matrix trace norm. During a bootstrap interval
with \(E\le1\), (16) bounds the approximate \(C\) norm by \(C_T+1\)
and its total positive matrix mass by \(B_T+1\). Positive semidefiniteness
of its atoms follows from their Lyapunov equation regardless of whether its
separately evolved \(C\) is positive.

All coefficients in (6) are polynomials of these bounded aggregate moments
and affine in \(\lambda\in[0,\Lambda]\). Hence there are finite constants
\(A_T,L_T^{(1)},L_T^{(2)},L_T^{(3)}\), depending only on the displayed
bounded region and fixed data, such that the coefficient norm is at most
\(A_T\), a paired coefficient difference is at most
\(L_T^{(1)}E+L_T^{(2)}\delta\), and the difference of the two \(C\)
velocities is at most \(L_T^{(3)}E\). These constants can, explicitly, be
chosen as maxima of the finite polynomial derivatives on that compact region.

Subtract the paired matrix equations and use
\(\|PQ\|_*\le\|P\|\|Q\|_*\). Summing over atoms and using the
bound \(B_T+1\) on their total positive trace gives an integral inequality

\[
E(t)\le\int_0^t[L_TE(s)+D_T\delta],ds,
\]

for finite width-independent \(L_T,D_T\). For example,
\(L_T=L_T^{(3)}+2A_T+2L_T^{(1)}(B_T+1)\) and
\(D_T=2L_T^{(2)}(B_T+1)\) suffice. Therefore
\(E(t)\le D_T\delta,t e^{L_Tt}\). Taking
\(\delta\le[2(1+D_TT e^{L_TT})]^{-1}\) keeps \(E\le1/2\), closes
the bootstrap, and prevents finite-time escape of the coarsened polynomial
ODE on \([0,T]\). Each stated observable is an entry or a fixed linear
combination of the controlled moments, proving its \(O_T(\delta)\) error.

This gives a finite spectral discretization for fixed absolute accuracy and
fixed horizon, with initial dense spectral computation explicitly required.
The bound gives no subpolynomial-in-width complexity at error
\(n^{-1/2}\): first-order binning would require a mesh on that scale.
Analytic quadrature might improve this rate, but no such assertion is proved.
The coarsening also need not preserve the compatibility identity (14) or exact
loss dissipation; its guarantees here are the proved compact-time existence
and error bounds. No all-time error claim is inferred from exact all-time
equivalence of the uncoarsened model.

## 7. Why nonlinear gates destroy this simple conserved spectrum

Suppose the second-layer activation is nonlinear. Then
\(z_b=Wh_b\), \(h_b^{(2)}=\phi(z_b)\), and the relevant updates become

\[
\dot W=\frac\alpha n\sum_b c_b
(w\odot\phi'(z_b))h_b^\top,\qquad
\dot w=\alpha\sum_b c_b\phi(z_b).
\]

Consequently the derivative of the operator in (2) is

\[
\frac\alpha n\sum_b c_b\left[
(w\odot\phi'(z_b))z_b^\top
+z_b(w\odot\phi'(z_b))^\top
-\phi(z_b)w^\top-w\phi(z_b)^\top\right],
\]

which is generally nonzero. Linear activation makes \(\phi'(z_b)=1\)
and \(\phi(z_b)=z_b\), giving the exact cancellation; a sample-dependent
coordinate gate does not.

Even if only the first layer is nonlinear and the second remains linear,
so that (2) still holds, the feature-motion calculation acquires operators
\(W D_aD_bW^\top\), where
\(D_a=\operatorname{diag}\phi'(z_a^{(1)})\). These operators are generally
not determined by \(GG^\top\), readout energy, and scalar sample Grams.
They couple the fixed spectral directions through the moving gates. Thus the
mode equation (6) no longer follows. The spectral construction isolates a
real mechanism of deep linear learning; it does not remove the nonlinear
response information identified elsewhere in this study.

## 8. Check status and interpretation

The checked claims are exact finite-width equations (1)–(14), all-time
existence and equivalence for the prescribed initialization, the conditional
Gaussian initialization law, and the explicitly limited compact-time
coarsening estimate. The author checked matrix orientations, width factors,
passive-index roles, repeated and zero eigenvalues, initial-state dependence,
the inverse-spectrum compatibility identity, and the energy and stability
bounds. This is a scoped candidate awaiting comparison or independent checking.

The state has a physical interpretation that does not require retaining an
evolving learned matrix: first-layer similarities interact with modewise
readout/feature energy at the conserved initial gains. Its exact spectral
measure can still have \(n\) atoms, and its nonlinear extension remains open.
