# Internal check of the quadratic-metric terminal certificate

Check date: 2026-09-30.

Candidate: the complete `TERMINAL_METRIC_EXTENSION.md`.

Frozen candidate SHA256:

`1e71fddd6926827eab60e259d11750f663d8ea722a8c89bfbf61674aad8c87b7`

Allowed dependency: the previously checked complete
`TERMINAL_SCALAR_THEOREM.md`, revised SHA256

`fbb93521867a03c8a01ebe8c29f88d04b643cf3d6fa4af53151e13ddf4c6bde5`.

Verdict: **PASS for the stated conditional finite-width metric extension.**
The contraction certificates, exact fixed-metric margin, normalization,
source bound, continuation argument, all error constants, and both matrix
examples are correct. No mathematical correction is required.

This was a bounded internal mathematical check using the repository
instructions and the previously read `solve-math-rigorously` skill. No
other study, route, study README, external source, or numerical experiment
was used. The candidate was not edited. This is not a promotion review or
approval.

## Metric normalization and contraction

For symmetric positive-definite \(P\), the spectral inequalities

\[
p_-\|u\|_2^2\le u^TPu\le p_+\|u\|_2^2
\]

give exactly the candidate's norm equivalence, including its direction:

\[
\|u\|_2\le\|u\|_*:=\frac{\|u\|_P}{\sqrt{p_-}}
\le\kappa\|u\|_2,\qquad \kappa=\sqrt{p_+/p_-}.
\]

The extreme eigenvectors attain the constants. The normalization by
\(\sqrt{p_-}\), rather than \(\sqrt{p_+}\), is what permits the state
speed and the physical loss/clock bounds below without additional factors
of \(\kappa\).

Let \(S=(PC_0+C_0^TP)/2\), \(e=u-v\), and
\(\delta=\|u\|_2-\|v\|_2\). Since \(|\delta|\le\|e\|_2\),

\[
e^TP[T(u)-T(v)]=-e^TSe+(e^TPb_0)\delta.
\]

The generalized spectral lower bound is
\(e^TSe\ge\mu_P\|e\|_P^2\). Also,

\[
|(e^TPb_0)\delta|
\le\|e\|_P\|b_0\|_P\|e\|_2
\le\frac{\|b_0\|_P}{\sqrt{p_-}}\|e\|_P^2.
\]

This proves the spectral certificate (8) with exactly the stated
\(\beta_P\). At \(P=I\), it reduces to the previously checked Euclidean
certificate. The norm in \(T\) remains Euclidean throughout; the metric
does not change the terminal model or its matching initial residual
velocity.

Scaling \(P\) to \(cP\), \(c>0\), leaves \(\|\cdot\|_*\),
\(\kappa\), \(\mu_P\), \(\beta_P\), and all contraction rates unchanged.
Scaling \(\eta\) to \(c\eta\) scales the complete LMI by \(c\), also
preserving its validity.

## Matrix inequality and exact fixed-metric margin

Because \(\eta>0\), the Schur complement of the lower-right block in
(9) gives

\[
2S-2\lambda P\succeq
\eta I+\eta^{-1}Pb_0b_0^TP.
\]

Thus for every \(e\),

\[
2e^TSe-2\lambda\|e\|_P^2
\ge\eta\|e\|_2^2+\eta^{-1}(e^TPb_0)^2
\ge2|e^TPb_0|\|e\|_2.
\]

Substituting into twice the contraction identity proves (6). The sign of
the off-diagonal block and every factor of two in (9) are correct. With
\(C_0,b_0,\lambda\) fixed, all block entries are affine in \(P,\eta\),
as claimed. The candidate makes only a sufficient-certificate claim for
this LMI.

For the LMI example \(P=I\), \(C_0=\operatorname{diag}(10,1)\),
\(b_0=(2,0)^T\), \(\lambda=1/2\), \(\eta=1\), the Schur-complement
residual is

\[
\operatorname{diag}(20,2)-I-I-
\operatorname{diag}(4,0)=\operatorname{diag}(14,0)\succeq0.
\]

The spectral certificate instead gives \(1-2=-1\). Thus the asserted gain
is real. As an additional algebraic check, the exact fixed-
\(P\) margin in this example is
\(\min_{0\le x\le1}(1+9x^2-2x)=8/9\), consistent with the LMI's
positive but conservative choice \(1/2\).

The exact characterization (10) is also correct. Sufficiency follows from
the reverse triangle bound already used. For necessity, hold any nonzero
displacement \(e\) fixed. If \(e^TPb_0\ge0\), choose \(u=e,v=0\),
which attains \(\delta=\|e\|_2\). If \(e^TPb_0<0\), choose
\(u=0,v=-e\), which attains \(\delta=-\|e\|_2\). In either case
\(u-v=e\) and the nonlinear term attains its upper bound
\(|e^TPb_0|\|e\|_2\). Dividing by \(\|e\|_P^2\) and minimizing over
the compact \(P\)-unit sphere proves that (6) holds exactly when
\(\lambda\le\gamma_P\). There is no unattained norm-difference bound
hidden in this characterization.

## Source bound, bootstrap, and continuation

The centered aggregate bound (1) implies

\[
\|E(t)\|_2\le J\|X(t)-X_0\|\|r(t)\|_2.
\]

With \(q=\|X-X_0\|\), \(z=\|r\|_*\), norm equivalence gives

\[
\|E(t)\|_*\le\kappa Jq\|r\|_2\le J_*qz,
\qquad J_*:=\kappa J.
\]

Only one factor of \(\kappa\) is required here. The conversion from the
Euclidean residual norm to \(z\) has constant one. Rescaling contraction
(6) by \(p_-\) and pairing the forcing with the residual in the normalized
metric gives

\[
D^+z\le-(\lambda-J_*q)z.
\]

On the interval stopped at ball exit or \(J_*q=\lambda/2\), this implies
\(z\le R_*e^{-\lambda t/2}\), where the initial norm is exactly
\(R_*:=\|r_0\|_P/\sqrt{p_-}\). The state speed then yields

\[
q(t)\le H\int_0^t\|r(s)\|_2\,ds
\le\frac{2HR_*}{\lambda}(1-e^{-\lambda t/2}).
\]

Both strict inequalities in (12) therefore rule out the corresponding
exits. The resulting state trajectory lies in a smaller closed ball
strictly inside the supplied admissible ball. Since the state dimension
is finite, this is a compact subset of the locally Lipschitz domain.
The field is bounded there, so at a hypothetical finite maximal existence
time the trajectory has a limit; local existence from that limit would
extend it. This proves all-time continuation.

The state speed is integrable. In particular its limiting tail distance
is at most \(2HR_*e^{-\lambda t/2}/\lambda\). Thus the full state
converges, and continuity of its residual map proves interpolation at the
limit. The frozen model is globally Lipschitz and contractive in the
metric, giving its decay bound in (13).

At zero residual the full and frozen residual fields vanish. If
\(r_0=0\), both solutions are stationary and all stated errors vanish.
When \(J=0\), the margin stopping condition can simply be omitted and
the aggregate frozen residual dynamics are exact. When \(H=0\), the full
state is stationary; a nonzero residual would contradict positive
contraction under the other hypotheses. These cases introduce no
division by zero or unproved continuation assertion.

## Residual, loss, and clock constants

For \(e(t)=\|r(t)-\widehat r(t)\|_*\), the same metric contraction
inequality gives

\[
D^+e\le-\lambda e+\|E(t)\|_*,\qquad e(0)=0.
\]

The source estimate and bootstrap bound imply

\[
\|E(t)\|_*\le\frac{2J_*H}{\lambda}R_*^2e^{-\lambda t/2}.
\]

Integrating against \(e^{-\lambda(t-s)}\) gives

\[
e(t)\le\frac{4J_*H}{\lambda^2}R_*^2
\left(e^{-\lambda t/2}-e^{-\lambda t}\right),
\]

which is (14), since \(\|r-\widehat r\|_2\le e\).
The exponential difference has maximum \(1/4\), proving (15). Both
Euclidean residual norms are bounded by \(R_*\); factoring their squared
norm difference proves the cubic bound (16) with the stated coefficient.

Integration of the pointwise residual error gives

\[
\int_0^\infty\|r-\widehat r\|_2\,dt
\le\frac{4J_*H}{\lambda^3}R_*^2.
\]

The clock speeds use the Euclidean norms, whose difference is bounded by
the Euclidean residual error. Division by \(\sqrt m\) gives (17),
including the limiting clock difference. The exact clock increment is
at most \(2R_*/(\sqrt m\lambda)\); the frozen one is at most
\(R_*/(\sqrt m\lambda)\). No clock reparameterization is used.

Finally, substituting \(R_*\le\kappa R\) into (15)–(17) gives exactly
the powers \(\kappa^3,\kappa^4,\kappa^3\) in (18). The small-tail
hypotheses must still be verified using \(R_*\), or conservatively by
substituting \(\kappa R\) there as well. Uniform cubic asymptotics require
uniform bounds on the displayed constants and a contraction rate bounded
away from zero; the candidate explicitly preserves this requirement.

## Stable nonnormal matrices and the explicit example

If all eigenvalues of \(C_0\) have positive real parts, its matrix
exponential has a polynomial-times-decaying-exponential bound from its
finite Jordan decomposition. This proves convergence of (22). For every
nonzero \(v\), the integrand in its quadratic form is continuous and
strictly positive at zero, so \(v^TPv>0\). Differentiating the integrand
and integrating its derivative gives

\[
C_0^TP+PC_0=Q.
\]

This yields the stated strictly positive \(\mu_P\). For fixed \(P\),
\(\beta_P\) tends to zero with \(b_0\), proving the claimed coverage
for sufficiently small norm-term coefficients. Positive stability of
\(C_0\) alone is insufficient: the scalar example \(C_0=1,b_0=2\)
has \(T(r)=r\) for positive \(r\), as stated.

For the explicit nonnormal example (23), direct multiplication gives

\[
PC_0=\begin{pmatrix}1/2&1\\-1&1/2\end{pmatrix},\qquad
C_0^TP=\begin{pmatrix}1/2&-1\\1&1/2\end{pmatrix},
\]

so their sum is \(I_2\). The trace and determinant of \(P\) are
\(5\) and \(5/4\), giving

\[
p_\pm=\frac{5\pm2\sqrt5}{2},\quad
\kappa=2+\sqrt5,\quad
\mu_P=\frac1{5+2\sqrt5}.
\]

The bound \(\beta_P\le\kappa\|b_0\|_2\) proves the proposed margin
(24). It is positive because
\((5+2\sqrt5)(2+\sqrt5)=20+9\sqrt5<100\).
The Euclidean symmetric part is
\(\begin{pmatrix}1&2\\2&1\end{pmatrix}\), whose eigenvalues are
\(3,-1\); hence the Euclidean certificate does fail.

For \(r_0=(1,-1)^T\),
\(C_0r_0=(-3,-1)^T\), \(r_0^TC_0r_0=-2\), and
\(r_0^Tb_0=1/100\). Consequently

\[
\left.\frac{d}{dt}\|\widehat r(t)\|_2^2\right|_{t=0}
=4+\frac{\sqrt2}{50}>0,
\]

exactly as claimed. Positive scaling of \(r_0\) scales this derivative
by the square of the scale factor, preserving its sign. There is no
conflict with metric contraction because the metric norm and Euclidean
norm need not decrease together. The example is expressly a terminal
generator example, not a proof that these coefficients are reached by the
prescribed q=1 initialization.

## Scope of the checked result

The extension preserves the same finite scalar evaluator and adds only a
certificate. It contains the Euclidean certificate as \(P=I\) and
mathematically admits additional aggregate generators, including ones with
transient Euclidean loss growth. The stated fixed and moving storage counts
are correct; storing symmetric \(P\) would add \(m(m+1)/2\) fixed numbers,
but the evaluator itself does not need it after certification.

Existence of a certificate at a reached q=1 state, construction of handoff
aggregates from initialization, control of an earlier approximation,
population well-posedness, and width-uniform constants remain separate
questions. The candidate makes no unsupported claim on these points.
