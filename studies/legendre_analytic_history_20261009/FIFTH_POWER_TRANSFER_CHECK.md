# Bounded nonauthor check of the fifth-power prediction transfer

Date: 2026-10-10.

Reviewed input: the complete SHARPER_OBSTRUCTION_ROUTE.md with SHA-256
578b46258b1f5a1116b62630a0da7434f17bd1976e24a445b324120298b30e8b.

This is a bounded nonauthor check of the neural-output transfer. This agent did not author that transfer, but reused its existing context from the upper-bound route and had already checked the root's scalar cross-tail identities. It is therefore not a fresh isolated review or a promotion review. No other reviewer's report was read. The separate dense-variability upper certificate in ORIGINAL_METHOD_RESULT.md was not reviewed.

No blocking defect was found in the candidate's clock integral equations, dense-history estimates, Volterra bootstrap, or same-physical-time prediction argument. The calculation supports its \(q^{-5}\) lower bound on the stated initialization/fitting event, uniformly in width and sufficiently large order. The relative-variability conclusion remains conditional here on the separate upper certificate.

## Clock equations and uniform constants

For \(m=d=L=2\) and identity activations, the scaled equations
\[
\dot A=-B^\top cr^\top,\qquad
\dot B=-c(Ar)^\top,\qquad
\dot c=-BAr
\]
are correctly normalized. The original hidden reconstruction has coefficient \(2/(mn)=1/n\); the two history factors contribute \(n\), leaving exactly the matrix pairing in candidate equations (5)–(6), with coefficient one.

The initial residual is \(-y\). The uniform physical bounds give \(\|c(t)\|=O(t)\), and hence \(f(t)=A(t)^\top B(t)^\top c(t)=O(t)\), on a fixed short time interval, for every order. By choosing that interval sufficiently short for the fixed positive labels, both residual norms remain at least \(Y/2\). Each clock is then invertible there and reaches a common short clock interval. This justifies the denominator bound required in (4).

All vector-field product bounds are independent of width: \(A\) has two columns, \(B\) itself is used only in operator norm, and differences or positive-order derivatives of \(B\) are measured in Frobenius norm. Repeated differentiation of the dense clock equations uses these same bounds and the positive lower bound on \(\rho\). It supplies all fixed finite derivative orders needed for the Taylor remainders. No bound on \(\|B_0\|_F\) enters.

## Dense-history estimates

The globally constant forward term is reproduced by the projection. The backward history vanishes at the join, and the forward first derivative vanishes there because \(c(0)=0\). Subtracting the right Taylor jets through degree four therefore leaves globally \(C^4\) remainders. In the rescaled coordinate, the factors \(T/2\) in their derivatives remain bounded as \(T\downarrow1\).

Two applications of the Legendre operator are justified: the remainders and their needed derivatives match at the join, and the coefficient \(1-x^2\) removes the endpoint integration terms. Its spectral estimate gives the claimed \(q^{-4}\) remainder norm. Combined with the uniform truncated-power estimates, this proves
\[
\|Q_q b_D\|_2=O(q^{-3/2}),\qquad
\|Q_q h_D\|_2=O(q^{-5/2}),\qquad
\|H_q[b_D,h_D]\|_F=O(q^{-5}).
\]
The last bound uses the exact exceptional ramp/quadratic identity; ordinary Cauchy–Schwarz alone would give the weaker fourth power for that pair.

The interior expansion has the correct oscillatory coefficient. The other possible fifth-order terms are smooth. For the factorial-normalized truncated powers \(H_k=(x-\alpha)_+^k/k!\), their leading orthonormal coefficients are
\[
\begin{aligned}
H_1 &: -\sqrt{2/\pi}\,s^{3/2}j^{-2}\cos\chi_j,\\
H_2 &: -\sqrt{2/\pi}\,s^{5/2}j^{-3}\sin\chi_j,\\
H_3 &: \phantom{-}\sqrt{2/\pi}\,s^{7/2}j^{-4}\cos\chi_j .
\end{aligned}
\]
Thus the two smooth tail sums are respectively \(s^5q^{-5}/(5\pi)\) and \(-s^5q^{-5}/(5\pi)\), as stated. Their oscillatory sums are \(O(q^{-6})\) on the fixed interior interval.

These derivative asymptotics need not be obtained by differentiating an unspecified error in the leading formula for \(P_j\): the exact identity
\[
(1-x^2)P_j'=j(P_{j-1}-xP_j)
\]
first gives the leading derivative with a one-power-smaller error, and the Legendre equation and its differentiated recurrences give the higher derivatives used here. This verifies the candidate's derivative-asymptotic step directly. Pairing the forward \(q^{-4}\) remainder with the backward \(q^{-3/2}\) tail gives the claimed \(q^{-11/2}\) error. No derivative of that error is subsequently required.

## Bootstrap using only dense tails

At a common clock value, both states use their own physical trajectories and the same clock coordinate. Because their residuals are bounded away from zero, state subtraction controls the difference in \(b=c(r/\rho)^\top\). The differences vanish on the common prefix. Consequently their history \(L^2\) norms are bounded by a constant times the running state/time discrepancy \(E(T)\).

Expanding the bilinear projection pairing gives
\[
\begin{aligned}
H_q[\widehat b,\widehat h]-H_q[b_D,h_D]
={}&\int (Q_q\Delta b)(Q_qh_D)^\top\\
&+\int (Q_qb_D)(Q_q\Delta h)^\top
 +\int (Q_q\Delta b)(Q_q\Delta h)^\top.
\end{aligned}
\]
Projection contraction and the two dense-tail bounds prove
\[
\|H_q[\widehat b,\widehat h]-H_q[b_D,h_D]\|_F
\le C(q^{-3/2}E+E^2).
\]
This step uses no closure-history derivative. The integral equations then give the candidate's running-supremum inequality (19). On a first-exit interval \(E\le\eta\), choose \(C\eta\le1/4\) and then \(q\) large enough that \(Cq^{-3/2}\le1/4\). Absorption leaves an ordinary Gronwall inequality, giving \(E\le Cq^{-5}\). Choosing \(q\) larger if necessary improves \(E\le\eta\), so continuity closes the bootstrap throughout the fixed clock interval.

The pairing discrepancy is therefore \(O(q^{-13/2})\). The ordinary accumulated \(B\)-field difference has derivative \(O(q^{-5})\). The equations for \(A,c,t\) have no direct projection defect, so their difference derivatives are also \(O(q^{-5})\). These facts justify (20) and the smooth terms needed next.

## Same physical time and phase detection

Expand the prediction map at the dense state at common clock \(T\):
\[
\Delta f
=A_D^\top\Delta B^\top c_D
 +\Delta A^\top B_D^\top c_D
 +A_D^\top B_D^\top\Delta c
 +O(q^{-10}).
\]
Insert \(\Delta B=H_q[b_D,h_D]+S_B+O(q^{-13/2})\). Only the first term carries the leading rapid oscillation. All other displayed terms have derivatives \(O(q^{-5})\), because their difference factors and difference derivatives have that order and the dense coefficient derivatives are bounded.

To compare at the closure's physical time, subtract the dense time adjustment
\[
\dot f_n(t_D(T))\Delta t(T)+O(q^{-10}).
\]
The derivative of its linear term is \(O(q^{-5})\): both \(\Delta t\) and \(\Delta t'\) have that order, while the dense first two physical-time derivatives and \(t_D'\) are bounded. Thus candidate equation (21) is a same-physical-time statement with the claimed smooth remainder. Rapid derivatives of the discarded pairing remainder or of \(\Delta B\) are not needed.

The join jets are correctly converted from physical time:
\[
b_D'(1+)=-uy^\top/Y^2,\qquad
h_D''(1+)=B_0^\top uy^\top/Y^2.
\]
They give precisely
\[
C(T)=-\frac{T(T-1)^{3/2}\|y\|^2}{4\pi Y^4}\,uu^\top B_0.
\]
The direct prediction coefficient is \(V=A_D^\top C^\top c_D\). Its leading small-time term is the nonzero vector in (23). Indeed
\[
\|u\|^2=y^\top Gy\ge\|y\|^2/2,\qquad
\|Gy\|\ge\|y\|/2.
\]
The uniform \(O(t^2)\) remainder is dominated by its linear term on a sufficiently small fixed positive interval. Choosing the interior clock interval there gives a uniform positive lower bound for \(\|V(T)\|\), together with a uniform bound on \(V'\).

Adjacent opposite phases are separated by \(O(q^{-1})\). The smooth remainder changes by \(O(q^{-6})\) between them; replacing \(V(T_-)\) by \(V(T_+)\) costs the same order. Their difference therefore has leading term \(2q^{-5}V(T_+)\), while the uniform undifferentiated error is \(O(q^{-11/2})\). This proves that at least one of the two actual prediction errors has a fixed positive multiple of \(q^{-5}\).

The corresponding physical times lie in a common positive interval. In particular \(\rho\le Y\) and \(\rho\ge Y/2\) on the short tube imply
\[
\frac{T-1}{Y}\le t_{\rm Leg}(T)\le\frac{2(T-1)}Y.
\]
This verifies the width- and order-independent physical interval in the statement.

## Review conclusion and limits

The candidate's main transfer argument survives this bounded check. It avoids the principal possible failure modes: high derivatives of the closure, width-growing Frobenius norms of initialized mixers, comparison at different physical times, and cancellation by smooth readout or time corrections.

The \(q^{-5}\) lower bound excludes the paper's displayed absolute target unless \(q\) has the stated \(n^{1/10}\) scale, including its logarithmic factor. Excluding a relative-error statement with actual independent dense variability additionally requires the separate upper certificate; no assertion about that certificate's proof is made here. This report also does not upgrade the candidate to established book material or satisfy a fresh isolated promotion review.
