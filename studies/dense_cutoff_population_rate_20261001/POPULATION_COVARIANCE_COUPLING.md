# Gaussian path coupling without a history-Gram gap

2026-10-03. New unconditional auxiliary theorem for independent path
samples, developed by the coordinator during the direct population
comparison. This is not a theorem for the trained dependent neuron paths.
Its application to those paths is the remaining issue identified below.
The complete argument is given here; no external theorem about a width
rate is imported.

## 1. Finite-dimensional statement

Let \(X\) be a random vector in a finite-dimensional real inner-product
space. Let \(K\) be a fixed positive-definite matrix and suppose

\[
 X^\top KX\le B^2\quad\hbox{almost surely}.
 \tag{1}
\]

Define its second-moment matrix and the empirical second moment from
independent copies by

\[
 Q=\mathbb E[XX^\top],\qquad
 \widehat Q_n={1\over n}\sum_{r=1}^nX_rX_r^\top.
 \tag{2}
\]

No centering of \(X\) is required. The centered Gaussian sources below
have second moments (2), which is the convention for the manuscript's
forward source covariance.

For positive-semidefinite matrices \(Q,R\), write \(d_{\rm G}(Q,R)\)
for the infimum of \((\mathbb E\|U-V\|^2)^{1/2}\) over couplings of
centered Gaussian random vectors with covariances \(Q,R\).
Then

\[
 \mathbb E\,d_{\rm G}(Q,\widehat Q_n)^2
       \le {B^2\operatorname{tr}K^{-1}\over n}.
 \tag{3}
\]

The constant is independent of the dimension and of the smallest
positive eigenvalue of \(Q\). The statement includes singular \(Q\).

## 2. A deterministic Gaussian covariance estimate

First suppose \(Q\) is positive definite. Diagonalize it, with
eigenvalues \(\lambda_i>0\). For any \(R\succeq0\), put
\(\Delta=R-Q\). We prove

\[
 d_{\rm G}(Q,R)^2
 \le 2\sum_{i,j}{|\Delta_{ij}|^2\over\lambda_i+\lambda_j}.
 \tag{4}
\]

For \(0\le s<1\), set \(Q_s=(1-s)Q+sR\). The linear map
\(\mathcal L_{Q_s}:A\mapsto Q_sA+AQ_s\) on symmetric matrices is
positive definite for the Frobenius inner product. Let

\[
 A_s=\mathcal L_{Q_s}^{-1}\Delta.
\]

Solve the linear differential equation
\(dU_s/ds=A_sU_s\), with \(U_0\) centered Gaussian of covariance
\(Q\). Its covariance solves

\[
 {d\over ds}\mathbb E U_sU_s^\top
 =A_s\mathbb E U_sU_s^\top+\mathbb E U_sU_s^\top A_s.
\]

The matrix \(Q_s\) solves that same equation with the same initial
value. Uniqueness of this finite-dimensional linear equation gives
\(\mathbb E U_sU_s^\top=Q_s\). Its squared speed in \(L^2\) is

\[
 \mathbb E\|A_sU_s\|^2
 =\operatorname{tr}(A_sQ_sA_s)
 ={1\over2}\langle\Delta,\mathcal L_{Q_s}^{-1}\Delta\rangle_F.
 \tag{5}
\]

Since \(Q_s\succeq(1-s)Q\), for every symmetric matrix \(A\),

\[
 \langle A,\mathcal L_{Q_s}A\rangle_F
 =2\operatorname{tr}(A Q_s A)
 \ge(1-s)\langle A,\mathcal L_Q A\rangle_F.
\]

The variational identity

\[
 \langle V,\mathcal L^{-1}V\rangle
 =\sup_A\{2\langle V,A\rangle-\langle A,\mathcal L A\rangle\}
\]

therefore bounds (5) by
\((2(1-s))^{-1}\langle\Delta,\mathcal L_Q^{-1}\Delta\rangle_F\).
Minkowski's integral inequality gives

\[
 \|U_t-U_s\|_{L^2}
 \le\left({\langle\Delta,\mathcal L_Q^{-1}\Delta\rangle_F\over2}\right)^{1/2}
       \int_s^t(1-u)^{-1/2}\,du .
\]

Thus \(U_s\) has an \(L^2\) limit \(U_1\); its Gaussian law has
covariance \(R\). Taking \(s=0,t=1\), and using
\(\int_0^1(1-u)^{-1/2}du=2\), proves (4), because
\[
 \langle\Delta,\mathcal L_Q^{-1}\Delta\rangle_F
 =\sum_{i,j}{|\Delta_{ij}|^2\over\lambda_i+\lambda_j}.
\]
This is a coupling construction, rather than a continuity argument
for inverse history Grams.

## 3. The invariant weighted-moment bound

Independence in (2) gives

\[
 \mathbb E|\widehat Q_{n,ij}-Q_{ij}|^2
 ={1\over n}\operatorname{Var}(X_iX_j)
 \le {1\over n}\mathbb E X_i^2X_j^2.
 \tag{6}
\]

The following bound uses no common eigenbasis for \(K\) and \(Q\):

\[
 \begin{aligned}
 \sum_{i,j}{\mathbb E X_i^2X_j^2\over\lambda_i+\lambda_j}
 &\le {1\over2}\mathbb E
       \left(\sum_i{X_i^2\over\sqrt{\lambda_i}}\right)^2\\
 &={1\over2}\mathbb E(X^\top Q^{-1/2}X)^2\\
 &\le {B^2\over2}\mathbb E[
          X^\top Q^{-1/2}K^{-1}Q^{-1/2}X]\\
 &={B^2\over2}\operatorname{tr}K^{-1}.
 \end{aligned}
 \tag{7}
\]

The first inequality is \(\lambda_i+\lambda_j\ge
2\sqrt{\lambda_i\lambda_j}\). The third is Cauchy--Schwarz applied to
\(K^{1/2}X\) and \(K^{-1/2}Q^{-1/2}X\), followed by (1).
The last equality is the covariance identity and cyclicity of trace.
Combining (4), (6), and (7) proves (3).

If \(Q\) is singular, \(X\) lies in its range almost surely, because
\(\mathbb E\langle v,X\rangle^2=0\) for each vector in its kernel.
The empirical matrix has range in that same subspace. Apply (4) on
this range, and use the inverse square root as zero on the kernel.
The last trace in (7) becomes
\(\operatorname{tr}(K^{-1}P)\), where \(P\) is the orthogonal
projection onto the range of \(Q\); it is at most
\(\operatorname{tr}K^{-1}\). The weighted Cauchy--Schwarz inequality
still uses the full positive matrix \(K\). This proves the singular
case without assuming a lower eigenvalue bound.

## 4. Hilbert-space and path versions

Let \(H\) be a separable real Hilbert space. Let \(K\) be positive
self-adjoint with an orthonormal eigenbasis, bounded below by a
positive constant, and with
\(\operatorname{tr}K^{-1}<\infty\). Suppose
\(\|K^{1/2}X\|_H\le B\) almost surely.
Then (3) holds for the Gaussian coupling distance in \(H\).

Indeed project onto the first \(d\) eigenvectors of \(K\). The
projected version of (1) still has bound \(B\), and
\(\operatorname{tr}(K_d^{-1})\le\operatorname{tr}K^{-1}\).
Thus (3) holds uniformly in \(d\). Both the deterministic covariance
and every empirical covariance have finite trace. Coupling a
Gaussian vector with its orthogonal projection proves convergence
of their laws in the Gaussian coupling distance: its squared
projection error is the corresponding covariance trace tail.
For the empirical covariance this holds for each sample, since it
is a finite sum of rank-one operators. The triangle inequality
therefore passes the distances to their limits; Fatou's lemma
passes the expectation bound. This proves the claim.

Here is a version that controls the time supremum. On \([0,T]\),
use a real trigonometric basis with frequencies proportional to
\(k/T\), or an equivalent sine/cosine realization after a bounded
extension to a periodic interval. Give \(H=H^1([0,T])\) its
Fourier norm and let \(K\) add one further derivative. Then
\(\operatorname{tr}K^{-1}<\infty\), with a constant depending only
on \(T\), and \(\|K^{1/2}X\|_H\) is an \(H^2\) norm.
The elementary one-dimensional inequality

\[
 \sup_{t\in[0,T]}|u(t)|
 \le T^{-1/2}\|u\|_{L^2(0,T)}
      +T^{1/2}\|u'\|_{L^2(0,T)}
 \tag{8}
\]

holds for absolutely continuous \(u\): select a point whose
magnitude is at most \(T^{-1/2}\|u\|_2\), then integrate \(u'\)
and use Cauchy--Schwarz. Thus a Gaussian coupling in \(H^1\)
also controls the mean squared time supremum.
For independent random paths with an almost-sure \(H^2\) bound,
their empirical-covariance Gaussian source process and the
population-covariance Gaussian source process admit a root-width
coupling in this time-supremum sense. The constants depend on
the path bound and \(T\), not on history-Gram eigenvalues.

For a logarithmic horizon, rescaling to a fixed interval or keeping
the polynomial factors in (8) makes this use precise. This paragraph
does not assert an \(H^2\) envelope for the actual trained neuron
paths; that needs its own proof.

## 5. Why this does not yet settle the network

The independent samples in (2) are essential to the step (6).
The trained neurons reuse their random matrices and are dependent.
For their empirical covariance, even after centering at its actual
finite-width expectation, the variance contains

\[
 {1\over n^2}\sum_{r\ne s}
 \operatorname{Cov}(X_{r,i}X_{r,j},X_{s,i}X_{s,j}).
 \tag{9}
\]

Controlling this term in the weighted sum
\((\lambda_i+\lambda_j)^{-1}\), and identifying the associated
represented responses, has not been proved here. Absolute
entrywise concentration is not automatically the required weighted
estimate near small covariance eigenvalues. Nor may the actual
trained paths be declared independent because a one-neuron cavity
has conditionally Gaussian fields.

The theorem repairs one specific proposed obstruction: temporal
regularity can indeed give root-width Gaussian path coupling
without a minimum history-Gram eigenvalue, and the argument does
not confuse a Fourier basis with a covariance eigenbasis.
It remains an auxiliary probability theorem, not a completed
dense-to-population comparison.
