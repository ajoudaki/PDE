# Exact production contraction for the hidden observables

The canonical Gaussian-program recurrence constructs ordinary Taylor
coefficients

\[
X(t)=\sum_{k\geq0}X_k t^k,
\qquad
Z(t)=\sum_{k\geq0}Z_k t^k
\]

on the column and row Gaussian spaces, respectively.  The fixed-order tensor-
program argument used for the feature jet identifies normalized empirical
averages of every polynomial state with the corresponding Gaussian
expectation.  Since the first-layer state is (X=u^2), coefficient extraction
therefore gives

\[
Q_1^{(k)}(0)=k!\,\mathbb E_C[X_k].
\]

Likewise, the second preactivation squared RMS is the normalized empirical
average of (z^2).  The recurrence state (Z) is precisely the limiting
second-preactivation coordinate, hence

\[
Q_2^{(k)}(0)
=k!\sum_{p+q=k}\mathbb E_R[Z_pZ_q].
\]

Both are terminal contractions of states already required by the feature
recurrence; neither changes the dynamics or adds a closure assumption.

At initialization, (X_0=u^2) for a standard Gaussian (u), so (Q_1(0)=1).
The innovation covariance of (Z_0) is

\[
\mathbb E_R[Z_0^2]=\mathbb E_C[X_0^2]=\mathbb E[u^4]=3,
\]

which gives (Q_2(0)=3).

There is also an exact finite-width Ward identity.  With

\[
Q_{1,n}=\frac1n\sum_j u_j^2,
\]

direct differentiation in the canonical metric gives

\[
n\langle\nabla f_n,\nabla Q_{1,n}\rangle=8f_n.
\]

Consequently the feature-ascent curve satisfies (Q_1'(t)=8F(t)), and

\[
Q_1^{(k)}(0)=8F^{(k-1)}(0)\qquad(k\geq1).
\]

The production code computes (Q_1) directly through order sixteen and uses
this identity only as a gate.  It reproduces the Campaign-1 (Q_1,Q_2)
prefix through order eight before accepting the new coefficients.  The
complete recurrence is run through degree seventeen to reproduce the frozen
feature jet, but no (F^{(19)}(0)) branch is attempted.

These identities certify fixed-order width-limit jets.  They do not by
themselves imply an all-order Stieltjes representation or a positive-time
trajectory limit.
