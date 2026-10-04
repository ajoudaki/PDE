# Internal reconstruction of the Gaussian covariance coupling lemma

2026-10-03. Scoped internal check requested by the coordinator. This is a
collaborative research check, not an isolated promotion review. The checker
previously discussed the invariant weighted Cauchy--Schwarz calculation
with the coordinator and then read the complete frozen source.

Source: `POPULATION_COVARIANCE_COUPLING.md`, SHA-256
`7dd7fa1bc90fc6a957438131be2856b4dfae2256b06e265cf0a25e9baf6cc34e`.
No experiments were used.

**Verdict: PASS for the stated auxiliary theorem.** Independent random
paths with an almost-sure bound in the stated stronger Hilbert norm have
a root-width Gaussian source coupling, including singular covariances.
The source correctly excludes its application to trained dependent neuron
paths and does not claim the neural population rate.

## 1. Deterministic covariance interpolation

Let \(Q\) be positive definite and \(R\) positive semidefinite. Put
\(\Delta=R-Q\), \(Q_s=(1-s)Q+sR\), and let
\(\mathcal L_{Q_s}A=Q_sA+AQ_s\) on symmetric matrices with the
Frobenius inner product. For \(s<1\) this operator is positive definite.
With \(A_s=\mathcal L_{Q_s}^{-1}\Delta\), the linear equation
\(U_s'=A_sU_s\) preserves Gaussianity. Its covariance obeys the same
linear equation as \(Q_s\), with the same initial value \(Q\), because
\(A_sQ_s+Q_sA_s=\Delta=Q_s'\). Thus its covariance is exactly
\(Q_s\).

Its squared mean speed is
\[
 \mathbb E\|A_sU_s\|^2
 =\operatorname{tr}(A_sQ_sA_s)
 =\tfrac12\langle\Delta,\mathcal L_{Q_s}^{-1}\Delta\rangle_F.
 \tag{1}
\]
Since \(Q_s\succeq(1-s)Q\), the quadratic form of
\(\mathcal L_{Q_s}\) is at least \((1-s)\) times that of
\(\mathcal L_Q\). Applying the variational characterization of its
inverse gives a factor \((1-s)^{-1}\) in (1). Integrating the square
root of this bound gives an \(L^2\)-Cauchy path at \(s=1\), since
\(\int_0^1(1-s)^{-1/2}ds=2\). The limit is Gaussian with covariance
\(R\). In an eigenbasis of \(Q\), with eigenvalues \(\lambda_i\),
this proves
\[
 d_{\rm G}(Q,R)^2
 \le2\sum_{i,j}\frac{|\Delta_{ij}|^2}{\lambda_i+\lambda_j}.
 \tag{2}
\]
The constant 2 is consistent with the factor \(1/2\) in (1) and
the squared path-length integral. No continuity of a history-Gram
pseudoinverse is used.

## 2. Independent empirical covariance and the invariant weight

For independent copies of \(X\), with
\(Q=\mathbb E XX^\top\) and
\(\widehat Q_n=n^{-1}\sum_rX_rX_r^\top\),
\[
 \mathbb E|\widehat Q_{n,ij}-Q_{ij}|^2
       \le n^{-1}\mathbb E X_i^2X_j^2.
 \tag{3}
\]
Let \(K\) be positive definite and suppose
\(X^\top KX\le B^2\) almost surely. The source's invariant bound
checks without requiring \(K\) and \(Q\) to commute:
\[
 \begin{aligned}
 \sum_{i,j}\frac{\mathbb E X_i^2X_j^2}{\lambda_i+\lambda_j}
 &\le\tfrac12\mathbb E(X^\top Q^{-1/2}X)^2\\
 &\le\tfrac{B^2}{2}\mathbb E
        [X^\top Q^{-1/2}K^{-1}Q^{-1/2}X]
 =\tfrac{B^2}{2}\operatorname{tr}K^{-1}.
 \end{aligned} \tag{4}
\]
The first inequality is the arithmetic-geometric mean inequality for
the eigenvalues. The second applies Cauchy--Schwarz to
\(K^{1/2}X\) and \(K^{-1/2}Q^{-1/2}X\). The covariance identity
and cyclic trace give the equality. Combining (2)--(4) yields
\[
 \mathbb E d_{\rm G}(Q,\widehat Q_n)^2
                  \le B^2\operatorname{tr}(K^{-1})/n.
 \tag{5}
\]

The random vector need not have mean zero: \(Q\) is its second-moment
matrix. The Gaussian source is centered with covariance \(Q\), as
required by the manuscript's source rule.

## 3. Singular ranges

If \(v\in\ker Q\), then
\(\mathbb E\langle v,X\rangle^2=0\), so \(X\) lies in the
range of \(Q\) almost surely. A finite-dimensional kernel basis makes
this a simultaneous statement. Every empirical covariance therefore
has its range in that same subspace. Apply (2) there. Define
\(Q^{-1/2}\) to vanish on the kernel only in (4); its last trace is
then \(\operatorname{tr}(K^{-1}P_Q)\), where \(P_Q\) is the
range projection. This is at most \(\operatorname{tr}K^{-1}\).
The weighted Cauchy--Schwarz step uses the original full positive matrix
\(K\), so no commutation or invariance of the range under \(K\)
is needed. This verifies the source's singular-case argument.

## 4. Hilbert and time-supremum topology

Let \(H\) be separable, and let \(K\) be positive self-adjoint with
an orthonormal eigenbasis, bounded away from zero, and
\(\operatorname{tr}K^{-1}<\infty\). Under
\(\|K^{1/2}X\|_H\le B\), projection onto the first \(d\)
eigenvectors preserves the bound and does not increase the inverse trace.
The finite-dimensional result is consequently uniform in \(d\).

The deterministic covariance and each empirical covariance have finite
trace. Coupling an \(H\)-valued Gaussian with its projection gives
mean squared error equal to the corresponding covariance trace tail.
This tends to zero for both covariances, for each empirical realization.
The triangle inequality makes the finite-dimensional Gaussian coupling
distances converge to their Hilbert-space counterparts; Fatou passes
the expectation bound. This argument requires no compactness of a
history-Gram inverse and handles the empirical covariance's finite rank.

For time paths, take the base Hilbert space to be \(H^1([0,T])\)
and choose \(K\) to add one derivative. A bounded extension to a
periodic interval gives the Fourier construction, with inverse
eigenvalues summable in one temporal dimension. Its stronger norm is
equivalent to \(H^2\), with fixed \(T\)-dependent constants.
Evaluation at a time is continuous on \(H^1\), so the covariance
of the resulting Gaussian process at two times is exactly
\(\mathbb E[X(t)X(s)]\), despite representing the covariance
operator with the \(H^1\) inner product.

The elementary estimate
\[
 \|u\|_\infty
 \le T^{-1/2}\|u\|_{L^2(0,T)}
           +T^{1/2}\|u'\|_{L^2(0,T)}
 \tag{6}
\]
shows that the Hilbert coupling controls the squared time supremum.
Select a point where \(|u|\) is at most its RMS, integrate \(u'\),
and use Cauchy--Schwarz to verify (6). Thus an almost-sure \(H^2\)
bound on independent sampled paths gives the stated root-width
time-supremum Gaussian coupling. A logarithmic horizon introduces the
declared time-dependent constants; it does not invalidate the lemma.

## 5. Scope retained

Independence is used exactly in (3). Dependent trained neurons add the
cross-neuron covariance terms written in the source, and neither
Gaussian-root concentration of individual entries nor the one-neuron
cavity identity automatically controls their weighted sum near small
eigenvalues. The source also does not claim the almost-sure \(H^2\)
envelope for actual trained paths. These are real application obligations,
correctly separated from the checked auxiliary probability theorem.
