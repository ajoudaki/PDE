# Scoped independent check of the all-time routes

Date: 2026-10-10. This check used only the complete frozen
`ALLTIME_SOURCE_ROUTE.md` and `GENERAL_SCOPE_CHECK.md`, the supervisor's neutral
assignment, and the required mathematical-proof and canonical-notation skills.
It did not read the paper, book, code, other routes, study history, or other
studies; it ran no experiments and made no Git changes. Architecture and
initialization assumptions are checked as stated in these two inputs, not
independently against the paper.

Reviewed SHA-256 hashes:

- `ALLTIME_SOURCE_ROUTE.md`:
  `ade475661cd15f93e783fd914b6466063d4d82836fc29f945b42b01622e4a975`.
- `GENERAL_SCOPE_CHECK.md`:
  `26ac3a59aa71e3d31c3d826fad66e6c212f6e1c6a57ae9e06bd41c8be69b9c69`.

The targeted mathematical claims are valid under their displayed assumptions.
This is a scoped check of conditional results and a special-case obstruction;
the requested general all-time sample-compression theorem remains unproved.

## Nonlinear initial-ball certificate

Here sample norm is empirical RMS, \(A_0\) is the initialized positive definite
kernel, \(\Lambda=\|A_0\|\), \(G=\|A_0^{-2}y\|_m\), \(B_R\) bounds the prediction
Jacobian on the initial parameter ball, and \(b_R\) bounds
\(A_0^{-2}(A(\theta)-A_0)\) there. The residual equation is exactly
\(\dot r=-2A(\theta)r\) for the full averaged square loss.

The semigroup envelope
\[
\|A_0^2e^{-2A_0t}\|\le k(t)
=\frac{\Lambda^2}{(1+\Lambda t)^2}
\]
is correct: \(\lambda e^{-\lambda t}\le\lambda/(1+\lambda t)
\le\Lambda/(1+\Lambda t)\). Moreover \(\int k=\Lambda\), and splitting the
convolution at \(t/2\) gives \(k*k\le8\Lambda k\). The factor two in the residual
equation therefore gives precisely \(q=16\Lambda b_R\). The stopped Volterra
estimate yields
\[
\|r(t)\|_m\le\frac{Gk(t)}{1-q},\qquad
\int_t^\infty\|\dot\theta(u)\|\,du
\le\frac{2B_R\Lambda G}{(1-q)(1+\Lambda t)}.
\]
Thus the strict radius condition in the input closes the continuation
argument, proves fitting and parameter convergence, and gives the stated
compact-query tail bound, including the limiting predictor. The singular
extension correctly requires a fixed invariant range; it does not allow
uncontrolled kernel rank creation. Positive definiteness of this zero-readout
kernel requires \(m\le n\).

The added eigenbasis certificate is also correct. For empirical-orthonormal
eigenvectors, set \(r_i=\langle e_i,r\rangle_m\) and
\(V=\sum_i|r_i|/\lambda_i\). Its upper derivative obeys
\[
D^+V\le-2(1-\eta_R)\sum_i|r_i|.
\]
Integration gives activity \(S/[2(1-\eta_R)]\) and parameter length
\(B_RS/(1-\eta_R)\), with no missing factor. Continuity of the predictor at
the parameter limit plus integrable residual norm gives fitting. This argument
does not provide a sample-uniform tail rate. The final wording correctly calls
this an alternative test: the two sufficient tests are not shown to be ordered,
and conversion between their spectral and weighted absolute norms can introduce
dimension factors.

The displayed derivative envelopes and Gaussian net bounds have the claimed
normalizations. In particular the second activation derivative accounts for
the \(\sqrt n\) factor, and the generic drift estimate still loses
\(\lambda_{\min}(A_0)^{-2}\). No argument here bounds the inverse source norm
or inverse-weighted leakage uniformly in the sample count.

## Relative comparison and its limitation

For the two self-adjoint positive semidefinite generators on the same sample
Hilbert space, let \(e=\widehat r-r\),
\(a^2=\langle e,Be\rangle_m\), and
\(b^2=\langle r,Ar\rangle_m\). The assumed mixed relative-form bound gives
\[
\frac d{dt}\|e\|_m^2
\le-4a^2+4\zeta ab\le\zeta^2b^2,
\qquad
\int_0^\infty b^2\,dt\le\|y\|_m^2/4.
\]
Consequently the constant \(\zeta/2\) is valid, including the stated squared
initial-error extension. Noncommutation causes no missing term. The sufficient
common-reference form bound yields \(\zeta=\xi/c\) as claimed. The hypothesis
forces equal nullspaces by testing vectors in either kernel's nullspace.

This controls empirical RMS predictions only. It neither proves whole-sphere
control nor makes a subset-driven residual generator self-adjoint in the full
empirical metric. Limits of arbitrary time-dependent residual systems are not
established by the comparison estimate itself; the input correctly qualifies
its endpoint statement.

The two-parameter nonlinear least-squares example is valid. Its invariant
region is compact, its relative kernel distortion is at most \(\eta+\eta^2\),
and its initial source norm equals one for every positive source exponent.
Nevertheless \(\dot v=-2\varepsilon s_0\), \(s_0\ge0\), and
\(v(\infty)=-\eta\log\cosh1\) give exactly the stated slow residual activity
\(\eta\log\cosh1/(2\sqrt\varepsilon)\). This disproves the proposed abstract
activity implication; it is not a counterexample within the prescribed deep
Gaussian architecture or a storage lower bound.

## Deep-linear empirical-measure discontinuity

The change from the original full square loss to the half-square loss is now
explicit and correct: the original trajectory at time \(t\) is the displayed
trajectory at time \(2t\). It leaves all-time suprema and endpoints unchanged.

The balancedness matrices are conserved. Their eigenvalue conditions define
an open event containing identity initial hidden matrices, so its probability
is positive under the stated nondegenerate Gaussian laws. Backward induction
gives \(\sigma_{\min}(A_\ell)^2\ge1/2\) and
\(FF^\top\succeq2^{-L}I\). Homogeneity gives the stated linear-in-time bound
on squared parameter norm, hence global existence. Readout dissipation gives
exponential loss decay for each fixed \(p>0\); for the limiting single-point
measure it gives exponential decay of its one residual. The velocity is a
polynomially bounded product of parameters and an exponentially decaying
gradient vector, so parameters converge in both cases.

Reflecting the second column of the first Gaussian matrix preserves both its
law and the event, leaves single-point training unchanged, and reverses the
limiting prediction \(Z\) at the second coordinate input. Thus
\(\mathbb P(E\cap\{Z\le0\})\ge\mathbb P(E)/2>0\). On that same event all
\(p>0\) fit the rare point to \(Y\), while the limiting dataset predicts
\(Z\le0\), proving an all-time sphere discrepancy at least \(Y\) even though
\(W_1(\mu_p,\mu_0)=\sqrt2p\to0\).

The distinct-input construction is valid. Symmetric clusters cancel the
off-diagonal covariance and their mean second coordinate; hence
\[
u_{*,2}=\frac{pY}{p+(1-p)S_m}\longrightarrow Y
\quad(p=1/m,\ S_m\le m^{-4}).
\]
The covariance is positive definite. Applying readout dissipation to excess
loss gives exponential convergence to this unique linear least-squares
predictor, even though the minimum training loss need not be zero. The
measure distance bound \(m^{-2}+\sqrt2/m\) is correct. The discrepancy lower
bound of \(Y\) is a limit as \(m\to\infty\), not a claim at every finite \(m\).

The example establishes failure on a positive-probability event at fixed
\(n=d=2\), using a single query on the prescribed sphere. It does not establish
a large-width, high-probability obstruction or exclude a theorem whose allowed
failure event contains this event. Its exact covariance/label-moment runtime
also confirms why empirical-measure discontinuity is not an impossibility
theorem for sample compression. Finite-support aggregation is likewise exact
for the nonlinear class, conditional only on existence of the reference flow.

No substantive mathematical error was found in the targeted conclusions. The
missing general theorem still requires an initialization-checkable nonlinear
stability/source estimate, an autonomous compressed realization, and the
requested query-domain and width-dependent guarantees. These are not supplied
by the conditional certificates or the special-case counterexample.
