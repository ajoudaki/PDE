# Reconstruction of the first nonlinear profile coefficient

This is a complete internal reconstruction of PROFILE_FIRST_FEEDBACK.md,
read as a newly authorized same-study input on 2026-10-01. The scope is two
tanh hidden layers, one normalized training input, zero readout, the driver
\(b(u)=u\), and the two-block Gaussian variance/mobility profile from
DECISIVE_CONDITIONAL_ROUTE.md. No experiment, other-study input, manuscript
edit, or Git write was used.

**Outcome: the stated initial-coefficient result reconstructs.**
The exact third prediction derivative is \(4E_c\), the conditional Gaussian
second moment retains the order-one response mean, and differentiating the
block-empirical expression gives an \(O(1/N)\) profile contrast at this
second activity coefficient. This is neither positive-activity control of
the response contrast nor a trained-width theorem.

## 1. Direct differentiation checks the factor four

Use \(a,h,d,z,g,\psi,T,q_i\) exactly as defined in the candidate:
\[
h=\tanh a,\quad d=1-h^2,\quad z=W_0h,\quad
g=\tanh z,\quad \psi(z)=g\odot(1-g^2),\quad
T=W_0^\top\psi(z),\quad
q_i=\frac1N\sum_jc_{ij}h_j^2.
\]
At zero readout, the first hidden velocities are zero, while
\(w'(0)=g\). Thus \(\delta'(0)=\psi(z)\),
\[
W''(0)=c\odot(\psi(z)h^\top)/N,\qquad
a''(0)=d\odot T,\qquad h''(0)=d^2\odot T.
\]
Every factor is evaluated at initialization in these formulas. The first
top-preactivation derivative vanishes and
\[
z''(0)=\operatorname{diag}(q_i)\psi(z)+W_0(d^2\odot T).
\]
Consequently
\[
\frac1N g^\top g''(0)
=\frac1N\sum_iq_i\psi(z_i)^2+\frac1N\sum_jd_j^2T_j^2
=E_c.
\tag{1}
\]
This can verify the prediction derivative without the tangent-energy
description. Since \(w'=g\), \(w''(0)=g'(0)=0\), and
\(w'''(0)=g''(0)\), differentiating \(f=w^\top g/N\) three times yields
\[
f'''(0)=\frac1N[g''(0)^\top g+3g^\top g''(0)]=4E_c.
\tag{2}
\]
Similarly \(f''(0)=0\). For the activity derivative
\(q_N=f'\), this is exactly \(q_N'(0)=0\) and \(q_N''(0)=4E_c\).
The residual-free driver matters: these are activity derivatives, not
physical-time derivatives with extra residual factors.

The candidate's second derivation also checks. The readout energy
\(\|g\|^2/N\) contributes \(2E_c\) to its second derivative. The two initially
zero hidden gradient energies contribute respectively
\(2N^{-1}\sum_iq_i\psi(z_i)^2\) and
\(2N^{-1}\sum_jd_j^2T_j^2\), giving the other \(2E_c\).

## 2. Conditional Gaussian second moment

Condition on the first roots \(a\). For each row \(i\), let
\(X=W_{0,ij}\) and \(Z=z_i\). They are centered jointly Gaussian with
\[
\operatorname{Var}(X)=c_{ij}/N,\qquad
\operatorname{Var}(Z)=q_i,\qquad
\operatorname{Cov}(X,Z)=c_{ij}h_j/N.
\]
Gaussian integration by parts, applied once and twice, gives
\[
\mathbb E[X\psi(Z)\mid a]=\frac{c_{ij}h_j}{N}\alpha(q_i),
\]
\[
\mathbb E[X^2\psi(Z)^2\mid a]
=\frac{c_{ij}}N\beta(q_i)
 +\frac{c_{ij}^2h_j^2}{N^2}\gamma(q_i).
\tag{3}
\]
These formulas also hold when a variance vanishes, by continuity, and
require no inverse covariance. The functions \(\alpha,\beta,\gamma\) are
the Gaussian expectations explicitly defined in the candidate.

Different rows are conditionally independent. Therefore
\[
\mathbb E[T_j^2\mid a]
=\sum_i\mathbb E[X_i^2\psi(z_i)^2\mid a]
 +\left(\sum_i\mathbb E[X_i\psi(z_i)\mid a]\right)^2
 -\sum_i\left(\mathbb E[X_i\psi(z_i)\mid a]\right)^2.
\]
Substituting (3) gives precisely candidate equation (2). In particular,
the square of the summed row means is retained; deleting it would lose an
order-one response term. The term
\(\gamma(q_i)-\alpha(q_i)^2\) has the correct sign and normalization.

## 3. Every two-block normalization

Write \(N=2n\). For \(j\) in block \(A\), the two row types give
\[
\frac1N\sum_i c_{ij}\beta(q_i)
=(1-s)\beta_A+s\beta_B,
\]
\[
\frac1N\sum_i c_{ij}\alpha(q_i)
=(1-s)\alpha_A+s\alpha_B,
\]
and, with \(C_A=\gamma(\widetilde Q_A)-\alpha_A^2\),
\[
\frac1{N^2}\sum_i c_{ij}^2
 [\gamma(q_i)-\alpha(q_i)^2]
=\frac2N[(1-s)^2C_A+s^2C_B].
\tag{4}
\]
The formulas for \(j\) in block \(B\) exchange \(s\) and \(1-s\).
The last factor \(2/N\) follows from \(n\) rows of each type and squared
profile entries \(4(1-s)^2,4s^2\).
Multiplying by \(N^{-1}\sum_{j\in A}d_j^2h_j^2=U_A/2\)
therefore leaves the coefficient \(U_A/N\) in the final line of candidate
equation (3), rather than \(U_A/(2N)\). All four lines of that equation
match the conditional mean obtained from (1), (3), and (4).

The conditional row variances are exactly
\(\widetilde Q_A=(1-s)Q_A+sQ_B\) and
\(\widetilde Q_B=sQ_A+(1-s)Q_B\); they lie in \([0,1]\).

## 4. Taylor cancellation and derivative interchange

Each block triple \(X_A=(Q_A,V_A,U_A)\) is the average of \(n\) iid bounded
triples, and both blocks have deterministic mean \(x_*\). Thus
\[
\mathbb E(X_A-x_*)=\mathbb E(X_B-x_*)=0,\qquad
\mathbb E\bigl(\|X_A-x_*\|^2+\|X_B-x_*\|^2\bigr)\le C/n.
\tag{5}
\]
Tanh and all its fixed derivatives are bounded. Gaussian covariance
differentiation consequently makes the fixed derivatives of
\(\alpha,\beta,\gamma\) used in the argument bounded on \([0,1]\), including
at zero. For example, a variance derivative of \(\mathbb EH(\sqrt qG)\)
is \(\frac12\mathbb EH''(\sqrt qG)\). Repeated application supplies the
needed orders without a singular square-root bound.

Candidate equation (3) has the exact form
\[
\mathbb E[E_c\mid a]=F_s(X_A,X_B)+N^{-1}G_s(X_A,X_B).
\]
The Hessian of \(\partial_sF_s\) in the six empirical coordinates is bounded
uniformly on their compact domain and \(s\in[0,1/2]\). At equal means,
\[
F_s(x_*,x_*)=(Q_*+V_*)\beta(Q_*)+U_*\alpha(Q_*)^2
\]
is independent of \(s\), so the constant term of the Taylor expansion of
\(\partial_sF_s\) is zero. Its linear term has zero expectation by (5).
The expected absolute remainder is at most \(C/n=2C/N\).
The derivative \(\partial_sG_s/N\) is bounded by \(C/N\).
Using \(q_N''(0)=4E_c\) proves
\[
\left|\partial_s\mathbb E q_N''(0)\right|\le C/N.
\tag{6}
\]

The initial derivative formulas contain bounded activation functions and
finite-degree Gaussian factors. Their moments and profile derivatives are
finite uniformly on the compact profile interval for fixed width.
Alternatively, their exact bounded empirical-triple representation directly
justifies differentiating the expectation at the required stage. Thus
the passage to \(\partial_s\mathbb E q_N''(0)\) is valid, including the
degenerate block endpoint by continuity. The exact interpolation identity
identifies (6) with the second activity coefficient of the normalized local
edge-response contrast.

The zeroth coefficient is the separately checked initialization contrast.
The first coefficient vanishes because \(q_N'(0)=0\) for every profile.
There is no bound here on growth of higher coefficients, no exchange with
an infinite power series, and no positive-activity interval conclusion.

## Inputs, status, and hash

The canonical-notation and rigorous-math skills were applied. The complete
newly authorized candidate and the author's already-developed
DECISIVE_CONDITIONAL_ROUTE.md were the scientific inputs to this check.
The coordinator's earlier brief description of the calculation was also
received; the formulas above were reconstructed directly from the complete
candidate. This is not an independent promotion review.

Frozen candidate SHA-256:

    0d6ca7ac3f49fe19ddf684ed31e7d780d19d4abbeecf260bfe9256a45b30a896  PROFILE_FIRST_FEEDBACK.md

No substantive algebraic, scaling, or expectation-interchange gap was found.
The open hypothesis remains propagation of the local response contrast
through a fixed positive activity interval.
