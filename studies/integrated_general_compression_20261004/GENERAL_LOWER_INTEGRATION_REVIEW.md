# Internal check of the general lower integration

2026-10-04. **PASS for the scoped integration.** No substantive mathematical
or scope defect was found in the versions identified below. This is an
internal integration check, not an independent promotion review or a fresh
verification of the excluded source theorems.

The scope was the eight study files in the final table. The canonical
notation skill, its neural-network reference, and the rigorous-math skill
were applied. The lower result, innovation proof, trajectory bridge and its
check, RESULT, sample-polynomial statement, and original explicit Legendre
comparison were read. The refined Legendre statement and order inversion
were checked for the interface used here; its full stability proof was not
re-audited. No other study, maintained-book source, experiment, or external
source was consulted. The initialized Gram CLT, fitting theorems, and
stopped Gaussian insertion interface remain inherited component results.
In particular the finite-query localization has a separate internal
reconstruction; this report verifies its use and critical constants rather
than claiming a new review of its excluded source inputs.

## 1. Model, geometry, and label scope

All integrated statements use the same width-\(n\) Gaussian model with
fixed hidden depth \(L\ge2\), zero initial readout, mean squared loss,
mobilities \((n,1,\ldots,1,n)\), and fixed inputs of norm \(\sqrt d\).
Write
\[
Y=\|y\|_2/\sqrt m>0,\qquad
\gamma=\lambda_{\min}(Q^L)>0,\qquad
\lambda=\gamma/m,\qquad \ell_n=\log(en).
\]
Here \(Q^L\) is the uncentered population feature second-moment matrix,
and \(y\ne0\) means the label vector is nonzero; individual components
may vanish. The gap does not contain a factor \(1/m\).

For the general lower result, \(m\ge2\) is necessary under the allowed
activation class. Arbitrary correlations and singular intermediate
Gaussian covariances are retained. No centered gap, orthogonality,
input-rank, label-sign, bounded-value, or trained-variance hypothesis is
introduced. Strip holomorphy with bounded first derivative gives at most
linear growth on the real line, so the required fourth moments are finite.
The fixed common strip and all derivative and source constants are part
of the activation data.

RESULT (3) imposes the existing intersection of dense, closure, compact,
and source label allowances. In particular its source condition is
\(S=16Y/\lambda\le S_*^{\rm src}\). The bridge uses the nondecreasing
response recurrence \(U_{\rm fin}(S)\) to define
\[
\chi_{\rm act}=
\min\left\{1,
\frac{a}{4(S_*^{\rm src})^2U_{\rm fin}(S_*^{\rm src})}\right\}>0.
\]
Thus the entire recurrence-based allowance permits the time coefficient
\(c=\chi_{\rm act}/\lambda\), with \(\chi_{\rm act}\) depending only
on activation data and depth. There is no additional sample or geometry
factor in this coefficient. Under the optional sufficient cap
\(Y/\lambda\le\beta^{-30L}\), the checked power envelope gives
\(\chi=1\). The main lower theorem does not replace the full allowance
by that smaller cap.

## 2. Quantitative composition

Let \(H_a=\phi_L(Z_a)\), where
\(Z\sim N(0,Q^{L-1})\), and let \(Q=\mathbb E HH^\top=Q^L\).
The common scalar marginal moments are
\[
q_0=1,\qquad
q_j=\mathbb E\phi_j(\sqrt{q_{j-1}}G)^2,\qquad
\mu_4=\mathbb E\phi_L(\sqrt{q_{L-1}}G)^4,
\quad G\sim N(0,1).
\]
They depend only on activations and depth. The positive final gap with
\(m\ge2\) excludes a zero penultimate variance and implies
\(q_L,\mu_4>0\).

The innovation proof's distribution-free truncation is valid. To see its
critical quantitative step, set
\[
c_0=Qy,\quad A=\|c_0\|_2,\quad T=\operatorname{tr}Q,
\quad D=T-c_0^\top Qc_0/A^2,\quad M_4=\mathbb E\|H\|_2^4.
\]
The squared area between \(c_0\) and \(H\) is at most
\(\|H(H^\top y)-c_0\|_2^2\|H\|_2^2\). Truncation at squared
radius \(2M_4/D\) gives
\[
\operatorname{tr}\operatorname{Cov}(HH^\top y)
\ge\frac{A^2D^2}{4M_4}.
\]
All denominators are positive because \(D\ge(m-1)\gamma>0\).
Also \(M_4\le m^2\mu_4\), \(T=mq_L\), and, with
\(N=y^\top Q^2(TI-Q)y=A^2D\),
\[
N\ge(m-1)\gamma A^2,\qquad
N\ge\gamma^2(T-\gamma)\|y\|_2^2.
\]
For the second inequality, the minimum of \(\xi^2(T-\xi)\) over
\([\gamma,T-\gamma]\) is \(\gamma^2(T-\gamma)\).
Using \(T-\gamma\ge(m-1)q_L\) and
\((m-1)^2/(4m^2)\ge1/16\) recovers the integrated trace bound
\[
\operatorname{tr}\operatorname{Cov}(HH^\top y)
\ge\frac{\gamma^3q_L}{16\mu_4}\|y\|_2^2.
\]
Selecting a largest diagonal variance therefore gives a deterministic
training index \(a\) with
\(\operatorname{Var}(H_aH^\top y)\ge
\gamma^3q_LY^2/(16\mu_4)\). The inherited covariance recursion has
a positive semidefinite last-layer innovation. Its contraction and the
two independent copies' onset factor \(8/m^2\) give
\[
\sqrt n\,[\dot f_n(0,x_a)-\dot{\widetilde f}_n(0,x_a)]
\Longrightarrow N(0,\sigma_a^2),\qquad
\sigma_a\ge\frac{Y\gamma^{3/2}}m
                  \sqrt{\frac{q_L}{2\mu_4}}.
\]
The chosen index does not depend on the sampled initialization.

On the inherited finite-query source event, the actual prediction
difference has a bounded holomorphic extension containing the
parameter-two ellipse for \([0,r_n]\), where
\(r_n=\chi_{\rm act}/(\lambda\sqrt{\ell_n})\) in the full range.
The Chebyshev truncation and endpoint derivative inequality yield
\[
\sup_{0\le t\le r_n}|g(t)|
\ge\frac{r_n}{2N^2}|g'(0)|-24M2^{-N}.
\]
Taking \(N=\lceil2\ell_n/\log2\rceil\le4\ell_n\) and using the
bridge's explicit remainder test gives lower coefficient
\(u\chi_{\rm act}\sigma_a/(64\lambda)\). Consequently
\[
\frac{u\chi_{\rm act}\sigma_a}{64\lambda}
\ge\frac{u\chi_{\rm act}}{64\sqrt2}
       \sqrt{\frac{q_L}{\mu_4}}Y\sqrt\gamma.
\]
This verifies the cancellation of \(m\) and the power
\(\gamma^{3/2}/\gamma=\sqrt\gamma\). The integrated coefficient
\(u\chi_{\rm act}\sqrt{q_L/\mu_4}/128\) is a valid conservative
choice. Under the simple cap, \(\chi_{\rm act}\) is replaced by one.
No upper label cap was substituted for the actual factor \(Y\).

For \(u=u_\delta=\Phi^{-1}(1/2+\delta/4)\), the limiting Gaussian
event has probability \(1-\delta/2\). Subtracting the vanishing source
failures and allowing the CLT convergence error gives probability at
least \(1-\delta\) at each sufficiently large individual width.
Independence between these events is unnecessary. The sufficient width
may depend on all fixed data and remains unquantified.

The argument gives a positive value on the compact real interval
\([0,r_n]\). Since both initial predictions are zero, a witnessing
time is strictly positive. The query is a training input, where both
fitted endpoints agree with the label. The conclusion is therefore a
transient lower bound in the same all-time sphere norm; it is not an
endpoint or pointwise-in-time ratio statement.

## 3. Compression and convergence of the ratios

The two admissibility ranges use the appropriate order formulas:

- In the full recurrence-based range, use RESULT §4 and
  EXPLICIT_LEGENDRE_COMPARISON (6), with its square-root logarithm.
- Under the optional beta cap, use SAMPLE_POLYNOMIAL_STATEMENT (5),
  whose sharper inversion has a quarter power of the logarithm.

For either prescription, the underlying deterministic upper envelope is
\(E_n(q)=C_n\sqrt{\log(eq)}/q^2\), on one event valid for every
admissible integer order. The prescribed base order satisfies
\(E_n(q_n)\le Y/\sqrt n\) and \(q_n=n^{1/4+o(1)}\); this is a
bound on the envelope itself, not merely on an observed error.
For \(q_n'=\lceil q_n\ell_n^{3/2}\rceil\),
\[
\frac{E_n(q_n')}{E_n(q_n)}
\le\ell_n^{-3}
\sqrt{\frac{\log(eq_n')}{\log(eq_n)}}
\le2\ell_n^{-3}
\]
eventually, since the logarithm ratio tends to one. This proves the
stated \(2Y/(\sqrt n\ell_n^3)\) bound. The order introduces no new
probability union. Its moving count remains
\(n(d+1)+1+2(L-1)mnq_n'=n^{5/4+o(1)}\), and the additional
\((L-1)n^2\) fixed mixer entries remain disclosed.

The unchanged compact bound, divided by the positive lower scale, is a
fixed multiple of
\[
n^{-1/2}\ell_n^{5/2}e^{a_0+b_0\sqrt{\ell_n}}
+n^{-15/2}\ell_n^{5/2},
\]
which tends to zero. Its full retained storage is still
\(O_{\rm fixed}(\ell_n^{3d+2})\).

More precisely, for any fixed failure probability \(\eta>0\), the
lower bound supplies a positive fixed coefficient and an event of
probability at least \(1-\eta\) eventually. On its intersection with
the comparison events, both error/discrepancy ratios are bounded by
deterministic sequences tending to zero. Thus for every \(b>0\),
the limiting upper probability that either ratio exceeds \(b\) is at
most \(\eta\). Sending \(\eta\downarrow0\) proves convergence in
probability. This also shows that the zero-denominator event has
probability tending to zero, so any fixed convention there is harmless.
A lower bound at just one fixed confidence would not alone prove this
convergence; the available all-confidence statement supplies what is needed.

## 4. Necessary size within the canonical dense family

Fix \(0<\delta<1/2\) and a fixed nondegenerate task. Suppose along
widths tending to infinity that the canonical independent-copy
discrepancy is at most \(\varepsilon\) with probability at least
\(1-\delta\). Its intersection with the lower event has probability
at least \(1-2\delta>0\). Therefore the deterministic thresholds must
satisfy
\[
n\ell_n^5\ge c_{\phi,L,\delta}^2Y^2\gamma\,
\varepsilon^{-2}.
\]
This justifies the necessary-width claim with the actual label and gap
factors. For completeness, its logarithmic inversion is valid without
assuming an upper bound on width. If \(n\ge\varepsilon^{-2}\), the
claimed lower bound on \(n\) already holds. Otherwise
\(\ell_n\le1+2\log(1/\varepsilon)\), so the last display gives
\[
n\gtrsim_{\rm fixed}
\frac{\varepsilon^{-2}}{\log(1/\varepsilon)^5}.
\]
Since the canonical dense parameter count is
\((L-1)n^2+n(d+1)\) with \(L\ge2\), the necessary count is
\(\Omega_{\rm fixed}(\varepsilon^{-4}/
\log(1/\varepsilon)^{10})\). This statement concerns large-width
sequences and independent-copy accuracy inside this specified dense
family. It gives no universal dimension, approximation, or bit lower
bound for other representations. The Legendre and compact counts remain
sufficient constructions, with moving and full retained resources
distinguished.

The remaining limitations are stated consistently: fixed-data asymptotics,
the existing small-label allowance, an unquantified stochastic/CLT width,
logarithmic loss in the lower rate, no sharp sample or conditioning
calibration, and no general endpoint lower bound. The strict-root dense
upper theorem remains open. Zero labels and constant final activations
in the one-sample case are correctly excluded from the positive claim.

## 5. Final reviewed versions

Hashes are SHA-256 of the study files used in this check. The bridge check
records an earlier version and its then-pending typographical correction;
the bridge version below already contains the required plus in (6) and
the two-range Legendre prescription. Historical hashes in that earlier
check are not substituted for the versions reviewed here.

| Input | SHA-256 |
|---|---|
| GENERAL_VARIABILITY_LOWER_RESULT.md | `bd009395a1b5d6c53b798094f80dfeee3d64fdc90de4a14e32c4f9fab1d8ab92` |
| GENERAL_INNOVATION_LOWER.md | `7d614fbe45b13770b45d314eab9b4f3a5c1c43103060be70c64f13cf7a94c553` |
| GENERAL_TRAJECTORY_LOWER_BRIDGE.md | `32da5b9db05797d5f5405c22ad708ecc0f74e4247aabe13ff16cfb9f448fd372` |
| GENERAL_TRAJECTORY_LOWER_BRIDGE_CHECK.md | `4c7107e0ad489fbd91f9d961798dfbba2e1d3ecd5831c0f3989fae279ead3737` |
| RESULT.md | `eb039b9b9c006a8f68a3b56d8d05d6f2e2ab9fe9010861d6d54076b254218040` |
| SAMPLE_POLYNOMIAL_STATEMENT.md | `049fa7094ce8d651bc8952fe26ea0fc660da955962552879a91eb1f88bde0900` |
| LEGENDRE_SAMPLE_EXPONENT_REFINEMENT.md | `93f09aff3f97b13e0361494ce0c9c1ab89917e7dbef323216c850b6e2d96b8a4` |
| EXPLICIT_LEGENDRE_COMPARISON.md | `7834b325b31aa667d9c751a2c180439399433d82d77cdd078b38ea54e0168a1c` |
