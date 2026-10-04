# A quadratic-metric terminal certificate

Post-comparison derivation by scoped agent `scalar_control`, 2026-09-30.
Status: conditionally proved here, internally unchecked, not established or
promoted. This note follows the authorized comparison with
`TERMINAL_SCALAR_THEOREM.md`, SHA256
`2d89e4613b8f7729bb772a7da21b7453278735eb644583b189a95cdefc042ddd`.
The complete updated source was subsequently reread at SHA256
`fbb93521867a03c8a01ebe8c29f88d04b643cf3d6fa4af53151e13ddf4c6bde5`;
its expanded model statement and clarifications do not change the inputs
or conclusions used here.
It does not change that candidate or the frozen independent `CONTROL_ROUTE.md`.
The new scientific input was the complete terminal candidate; earlier inputs
were the study's exact-model README and this agent's own control derivation.
Current shared instructions were reread. No training experiment was run.

The Euclidean dissipation condition in the terminal candidate can be replaced
by a positive-definite quadratic certificate. This admits some nonnormal
generators for which Euclidean loss initially increases. The terminal model
and its moving state count do not change. The metric affects the certificate,
the permitted handoff radius and the explicit error constants.

## 1. The exact terminal setting

Use the actual finite-width q=1 model and its aggregate identity from the
terminal candidate, with its original physical time:

\[
\dot r=-C(X)r+\|r\|_2b(X),\qquad
L=\|r\|_2^2/m,\qquad
\dot\tau=\|r\|_2/\sqrt m.
\]

Reset a reached handoff to t=0. Put

\[
X_0=X(0),\quad r_0=r(0),\quad C_0=C(X_0),\quad b_0=b(X_0).
\]

Let a closed radius-a ball about X_0, in a specified full-state norm, lie in
the admissible domain tau>0. On that ball assume the same bounds as in the
terminal candidate:

\[
\|\dot X\|\le H\|r\|_2,\qquad
\|C(X)-C_0\|_{2\to2}+\|b(X)-b_0\|_2
\le J\|X-X_0\|.
\tag{1}
\]

The constants H,J are nonnegative. The exact full-state dynamics are locally
Lipschitz, and every state velocity vanishes at zero residual. These facts
follow from the q=1 residual factorization stated and derived in the terminal
candidate. No independent or resampled mixer is introduced here.

The frozen scalar model remains

\[
\dot{\widehat r}=T(\widehat r),\quad
T(u)=-C_0u+\|u\|_2b_0,\quad \widehat r(0)=r_0,
\tag{2}
\]
\[
\dot{\widehat\tau}=\|\widehat r\|_2/\sqrt m,\quad
\widehat\tau(0)=\tau_0,\qquad
\widehat L=\|\widehat r\|_2^2/m.
\tag{3}
\]

In particular the norm inside the frozen generator stays Euclidean. It is
not replaced by a quadratic norm, which would change the leading residual
equation and generally lose its matching initial velocity.

## 2. Explicit quadratic contraction certificates

Let P=P^T>0 be an m by m matrix. Define

\[
p_-:=\lambda_{\min}(P),\qquad p_+:=\lambda_{\max}(P),\qquad
\kappa:=\sqrt{p_+/p_-},
\]
\[
\|u\|_P:=\sqrt{u^TPu},\qquad
\|u\|_*:=\frac{\|u\|_P}{\sqrt{p_-}}.
\tag{4}
\]

The exact optimal norm-equivalence constants are

\[
\sqrt{p_-}\|u\|_2\le\|u\|_P\le\sqrt{p_+}\|u\|_2,
\qquad
\|u\|_2\le\|u\|_*\le\kappa\|u\|_2.
\tag{5}
\]

They are attained on eigenvectors for the corresponding extreme eigenvalues.
Scaling P by a positive constant leaves the normalized norm, kappa and the
certified margins unchanged; in (9), eta is scaled by the same constant.

The required certificate is any lambda>0 for which

\[
(u-v)^TP[T(u)-T(v)]\le-\lambda\|u-v\|_P^2
\qquad\text{for all }u,v\in\mathbb R^m.
\tag{6}
\]

Here are two directly checkable sufficient conditions, and an exact
finite-dimensional characterization of the best possible margin for fixed P.

### A spectral sufficient condition

Set

\[
\mu_P:=\lambda_{\min}\!\left(
 P^{-1/2}\frac{PC_0+C_0^TP}{2}P^{-1/2}\right),\qquad
\beta_P:=\frac{\|b_0\|_P}{\sqrt{p_-}}.
\tag{7}
\]

If mu_P-beta_P>0, condition (6) holds with

\[
\lambda=\mu_P-\beta_P.
\tag{8}
\]

Indeed, for e=u-v and delta=||u||_2-||v||_2,

\[
e^TP[T(u)-T(v)]
=-e^T\frac{PC_0+C_0^TP}{2}e+(e^TPb_0)\delta.
\]

The first term is at most -mu_P||e||_P^2. The reverse triangle inequality,
(5), and the P-inner-product Cauchy--Schwarz inequality give

\[
|(e^TPb_0)\delta|
\le\|e\|_P\|b_0\|_P\|e\|_2
\le\beta_P\|e\|_P^2.
\]

This proves (8). P=I recovers precisely the Euclidean margin in the original
terminal theorem.

### A matrix-inequality sufficient condition

Alternatively, a supplied P>0, lambda>0 and scalar eta>0 certify (6) if

\[
\begin{pmatrix}
C_0^TP+PC_0-2\lambda P-\eta I_m & Pb_0\\
b_0^TP & \eta
\end{pmatrix}\succeq0.
\tag{9}
\]

For fixed lambda, this is a linear matrix inequality in P and eta. It is
a sufficient certificate; no necessity claim is made for the existence of
one common eta. Its conclusion can hold even when the elementary bound
(8) does not give a positive margin.

To prove the implication, minimize the block quadratic form in its last
scalar coordinate. Since eta>0, (9) yields

\[
C_0^TP+PC_0-2\lambda P
\succeq\eta I_m+\eta^{-1}Pb_0b_0^TP.
\]

For every e,

\[
2|e^TPb_0|\|e\|_2
\le\eta\|e\|_2^2+\eta^{-1}(e^TPb_0)^2.
\]

Use this bound and |delta|<=||e||_2 in twice the identity preceding (8).
The result is (6), with all factors of two as stated. For a concrete gain
over (8), take P=I, C_0=diag(10,1), b_0=(2,0)^T. Bound (8) gives -1, whereas
lambda=1/2 and eta=1 make the Schur-complement residual in (9) diag(14,0),
which is positive semidefinite.

### Exact margin for a fixed P

Define

\[
\gamma_P:=\min_{\|e\|_P=1}
\left[e^T\frac{PC_0+C_0^TP}{2}e
      -|e^TPb_0|\|e\|_2\right].
\tag{10}
\]

The minimum exists by continuity on the compact P-unit sphere. Condition
(6) holds exactly when lambda<=gamma_P. Sufficiency is the reverse triangle
inequality used above. For necessity, fix a nonzero e. If e^TPb_0>=0, take
u=e,v=0; if e^TPb_0<0, take u=0,v=-e. In each case u-v=e and the norm
difference has the sign attaining |e^TPb_0|||e||_2. Homogeneity then yields
(10). Formula (10) is a finite-dimensional, potentially nonconvex verification
problem; (8) and (9) offer simpler sufficient certificates.

## 3. Terminal theorem in the certified metric

Assume (1), and let P>0 and lambda>0 satisfy (6), as can be checked using
(8) or (9). Put

\[
R_*:=\|r_0\|_* =\frac{\|r_0\|_P}{\sqrt{p_-}},
\qquad J_*:=\kappa J.
\tag{11}
\]

Suppose

\[
\frac{2HR_*}{\lambda}<a,\qquad
\frac{2J_*HR_*}{\lambda}<\frac\lambda2.
\tag{12}
\]

Then the exact full q=1 state stays in the ball for all physical t>=0 and
converges to a finite state with zero residual. Both residual systems satisfy

\[
\|r(t)\|_2\le\|r(t)\|_*
\le R_*e^{-\lambda t/2},\qquad
\|\widehat r(t)\|_2\le\|\widehat r(t)\|_*
\le R_*e^{-\lambda t}.
\tag{13}
\]

At equal physical times, a pointwise error bound is

\[
\|r(t)-\widehat r(t)\|_2
\le\|r(t)-\widehat r(t)\|_*
\le\frac{4J_*H R_*^2}{\lambda^2}
\left(e^{-\lambda t/2}-e^{-\lambda t}\right).
\tag{14}
\]

Consequently,

\[
\sup_{t\ge0}\|r(t)-\widehat r(t)\|_2
\le\frac{\kappa JH}{\lambda^2}R_*^2,
\tag{15}
\]
\[
\sup_{t\ge0}|L(t)-\widehat L(t)|
\le\frac{2\kappa JH}{m\lambda^2}R_*^3,
\tag{16}
\]
\[
\sup_{t\ge0}|\tau(t)-\widehat\tau(t)|
\le\frac{4\kappa JH}{\sqrt m\lambda^3}R_*^2.
\tag{17}
\]

If only the initial Euclidean residual R=||r_0||_2 is used, then R_*<=kappa R
gives the weaker but explicit bounds

\[
\sup\|r-\widehat r\|_2\le\frac{\kappa^3JH}{\lambda^2}R^2,
\quad
\sup|L-\widehat L|\le\frac{2\kappa^4JH}{m\lambda^2}R^3,
\quad
\sup|\tau-\widehat\tau|\le
\frac{4\kappa^3JH}{\sqrt m\lambda^3}R^2.
\tag{18}
\]

Using R_* retains information about the orientation of r_0. For asymptotic
statements such as a cubic loss error as R tends to zero, the displayed
certificate constants must remain bounded with a positive lambda; the
pointwise inequalities themselves state all dependencies even if P varies.

Zero H or J is permitted. If r_0=0, both systems are stationary and the
error bounds are zero. The theorem does not assert that Euclidean loss is
monotone: R_* can exceed R, allowing a transient increase below the certified
envelope.

### Proof

Write q(t)=||X(t)-X_0|| and z(t)=||r(t)||_*. Define the deviation from the
frozen generator by

\[
E(t)=-(C(X(t))-C_0)r(t)+\|r(t)\|_2(b(X(t))-b_0).
\]

By (1) and (5),

\[
\|E(t)\|_*\le\kappa J q(t)\|r(t)\|_2
\le J_*q(t)z(t).
\tag{19}
\]

Contraction (6), rescaled by p_-, and T(0)=0 imply the upper-Dini inequality

\[
D^+z\le-(\lambda-J_*q)z.
\tag{20}
\]

At positive z this follows by differentiating the norm. At zero residual
the full field is zero, so the inequality extends without division by zero.
Stop the solution before either the ball boundary or J_*q=lambda/2. On
this interval z<=R_*exp(-lambda t/2), and the state speed gives

\[
q(t)\le H\int_0^t\|r(u)\|_2du
\le\frac{2HR_*}{\lambda}(1-e^{-\lambda t/2}).
\tag{21}
\]

The strict inequalities (12) rule out both exits. Thus the solution remains
in a compact subset of the admissible finite-dimensional domain. Local
Lipschitz existence and boundedness allow continuation for every physical
time. Its speed is integrable by (13), so X(t) converges; continuity and
r(t)->0 give an interpolating limit.

The frozen T is globally Lipschitz, because the Euclidean norm is
1-Lipschitz. Its P-contraction with zero proves its bound in (13) and global
existence. The exact and frozen initial residual velocities agree, since
E(0)=0. In particular introducing P has not altered the terminal evaluator.

Let e(t)=||r(t)-rhat(t)||_*. Contraction gives

\[
D^+e\le-\lambda e+\|E(t)\|_*,\qquad e(0)=0.
\]

Equations (19), (21) and (13) imply, after dropping a factor at most one,

\[
\|E(t)\|_*\le\frac{2J_*H}{\lambda}R_*^2e^{-\lambda t/2}.
\]

Multiplication by the integrating factor and direct integration give

\[
e(t)\le\frac{4J_*H}{\lambda^2}R_*^2
(e^{-\lambda t/2}-e^{-\lambda t}).
\]

One can justify this inequality at e=0 by a regularized norm or an upper-Dini
comparison; no differentiability of the norm at zero is assumed. The
maximum of u-u^2 on [0,1] is 1/4, proving (15). Also

\[
|L-\widehat L|
\le\frac{\|r\|_2+\|\widehat r\|_2}{m}
      \|r-\widehat r\|_2
\le\frac{2R_*}{m}e,
\]

which proves (16). Integrating (14) gives

\[
\int_0^\infty\|r-\widehat r\|_2dt
\le\frac{4J_*H}{\lambda^3}R_*^2.
\]

The two clock derivatives differ by at most ||r-rhat||_2/sqrt(m), proving
(17) at the same physical time. Both clocks have finite limits; for example,
the exact clock increment is at most 2R_*/(sqrt(m)lambda). This proves all
assertions without identifying trajectories by activity time.

## 4. Coverage of nonnormal stable linear parts

The certificate is not restricted to matrices with positive Euclidean
symmetric part. If every eigenvalue of C_0 has positive real part, choose
any Q=Q^T>0 and define

\[
P=\int_0^\infty e^{-C_0^Tt}Qe^{-C_0t}\,dt.
\tag{22}
\]

This integral converges: in finite dimension a Jordan decomposition bounds
each exponential by a polynomial times e^(-alpha t), for some alpha>0.
For nonzero v the integrand v^Te^(-C_0^Tt)Qe^(-C_0t)v is strictly positive
at t=0 and continuous, so P>0. Differentiating the integrand and integrating
from zero to infinity yields

\[
C_0^TP+PC_0=Q.
\]

Consequently

\[
\mu_P=\tfrac12\lambda_{\min}(P^{-1/2}QP^{-1/2})>0.
\]

For b_0 sufficiently small that beta_P<mu_P, (8) applies even if
sym(C_0) has a negative eigenvalue. This proves the claimed nonnormal
coverage. Positive stability of C_0 alone does not control the norm term:
already in one dimension C_0=1 and b_0=2 give growth for positive residual.
Neither (8) nor the theorem silently assumes away that term.

### An explicit generator with increasing Euclidean loss

For m=2 take

\[
C_0=\begin{pmatrix}1&4\\0&1\end{pmatrix},\qquad
b_0=\begin{pmatrix}1/100\\0\end{pmatrix},\qquad
P=\begin{pmatrix}1/2&-1\\-1&9/2\end{pmatrix}.
\tag{23}
\]

Direct multiplication gives C_0^TP+PC_0=I_2. The eigenvalues of P are
p_+=(5+2sqrt(5))/2 and p_-=(5-2sqrt(5))/2, both positive, and

\[
\kappa=2+\sqrt5,\qquad \mu_P=\frac1{5+2\sqrt5}.
\]

Since beta_P<=kappa||b_0||_2, a valid positive margin is

\[
\lambda=\frac1{5+2\sqrt5}-\frac{2+\sqrt5}{100}>0.
\tag{24}
\]

The positivity follows from (5+2sqrt(5))(2+sqrt(5))=20+9sqrt(5)<100.
By contrast sym(C_0) has minimum eigenvalue -1, so the original Euclidean
certificate fails even with b_0=0.

For r_0=(1,-1)^T, however,

\[
\left.\frac{d}{dt}\|\widehat r\|_2^2\right|_{t=0}
=-2r_0^TC_0r_0+2\|r_0\|_2r_0^Tb_0
=4+\frac{\sqrt2}{50}>0.
\]

The Euclidean loss therefore initially increases, while the certified
quadratic norm decreases exponentially. Multiplying r_0 by any positive
scalar preserves this sign and can make the residual arbitrarily small.
This is an algebraic terminal-generator example, not a claim that the
specific C_0,b_0 is reached by the prescribed q=1 Gaussian initialization.

## 5. State, provenance, and limits of the extension

The online model still has m moving residual scalars, or m+1 with the clock,
with O(m^2) work per evaluation and m^2+m frozen coefficients C_0,b_0.
P is a handoff certificate and need not be retained or evolved by that
model; if stored, it adds m(m+1)/2 fixed scalars. It can be verified using
only the finite aggregate data at the handoff and a supplied candidate P.

The result weakens the particular Euclidean terminal hypothesis, allowing
nonnormal effects and transient Euclidean loss growth while retaining
all-time physical residual/loss/clock accuracy. It does not prove that a
certificate exists at a state reached from initialization. It does not
construct handoff coefficients from a compressed early model, bound the
early approximation source, establish subquadratic initialization-to-end
state complexity, prove a q=1 population limit, or give width-uniform H,J,P
or lambda. Those claims remain separate.

The argument was self-audited for the Euclidean norm inside T, all metric
conversion factors, the factors of two in (9), small-tail continuation,
same-physical-time clock comparison, P-scale invariance, zero-residual and
zero-H/J cases, and the explicit 2-by-2 example. No independent check has
yet been performed; the note remains internally unchecked.
