# Internal reconstruction of the general trajectory lower bridge

2026-10-04. Scoped internal check, not an independent promotion review.
The mathematical reconstruction below verifies the finite-query source
localization, the full recurrence-based label scope, the analytic
derivative-to-prediction step, and the composition with the general
innovation bound. The reviewed bridge has one literal formula correction:
insert `+` before its middle term in equation (6). Its approximation
section can use the current sharper Legendre order without changing the
argument; the exact replacement is recorded below. These corrections were
reported to the author before this report was written.

The conclusion is a lower bound for actual nonlinear predictions in the
same all-time sphere norm as the upper comparisons. No new scientific
hypothesis is needed beyond the specified inherited source insertion
interface, the existing fitting/source label allowances, positive
initialized covariance gap, and nonzero labels. The general positive
conclusion requires at least two training samples. The proof leaves the
stochastic source and central-limit width thresholds unquantified.

## 1. Inputs and exact versions

The table records the reviewed snapshots under their original names;
its hashes are not assertions about the edited current files. The former
sample-polynomial statement was removed during consolidation. Its order
formula is retained in [LEGENDRE_SAMPLE_EXPONENT_REFINEMENT.md](LEGENDRE_SAMPLE_EXPONENT_REFINEMENT.md),
(4); the current shared allowance is in [RESULT.md](RESULT.md), §6.

All inputs below belonged to this study. The first eight were read completely;
the comparison statement was used for its setup and §§1–2, and RESULT was
used for the common model, common allowance, and its raw compact comparison
(6). No source outside the supervisor's explicit scope was fetched. The
canonical-notation skill, its neural reference, and the rigorous-math
skill were read. This check treats the inherited local Gaussian insertion
theorem as its explicitly stated interface; it does not claim a fresh
review of that theorem's excluded source files.

| Input | SHA-256 |
|---|---|
| GENERAL_TRAJECTORY_LOWER_BRIDGE.md | `c6c53f4b062f29daaf1b7c0eaf427c354e6263a8a48322bf8db22a6777cc36a2` |
| GENERAL_INNOVATION_LOWER.md | `7d614fbe45b13770b45d314eab9b4f3a5c1c43103060be70c64f13cf7a94c553` |
| EARLY_VARIABILITY_AND_STORAGE.md | `54744f6e58fe0f03f0349041100664dbd55c1335e5edc80d574979b128d960ea` |
| ONSET_TO_TRAJECTORY_LOWER.md | `34db6bf196433afd1c042832063f9fcc5c578a8aa389ec891ba3312dd345b5cd` |
| UNBOUNDED_COMPRESSOR_BRIDGE.md | `63b0613ca4c028f780e3342fb3ddf21efc739fa9257f903691ee967276f8cc08` |
| SIMPLE_CONSTANTS_SOURCE_CHECK.md | `cc1096f354e38c97b5cab8fe2000323ca21811c9801a4a33a4c5dbaf0a08938a` |
| GENERAL_EXPLICIT_FITTING.md | `5c6f12b78847a2b2874c5bc82eb1cea5f4929ee071b114d09b098397c5e2b8d6` |
| LEGENDRE_SAMPLE_EXPONENT_REFINEMENT.md | `93f09aff3f97b13e0361494ce0c9c1ab89917e7dbef323216c850b6e2d96b8a4` |
| SAMPLE_POLYNOMIAL_STATEMENT.md (reviewed snapshot; removed) | `7e6a71ab6dcde97dcde66716165683a0bd9538a4c76496fb815d14f4ef9a8665` |
| RESULT.md | `1e0b1ee589367c1ab9ea69d523f6fff7e58cfa04de12c828bf9f460dce2537ec` |

## 2. Source localization and the physical time factor

Fix the activation functions, their strip width, hidden depth \(L\ge2\),
data, sample count \(m\), input dimension \(d\), and labels while width
\(n\) grows. Write \(\gamma>0\) for the unweighted final feature
covariance gap, \(\lambda=\gamma/m\), \(Y=\|y\|_2/\sqrt m>0\),
\(S=16Y/\lambda\), and \(\ell_n=\log(en)\).

The original whole-sphere event cannot simply be restricted to a training
query and thereby acquire a larger time domain. The candidate does the
necessary additional work: it reruns source §§6–8 with finitely many fixed
real queries, omits the frame mesh and angular derivatives, and retains
the mixed-response insertion identities. Source (25) uses
\(16\sqrt{d+3}\) only for the Gaussian union over frames. The remaining
grid has at most \(n^{10}\) points eventually, with all data fixed. The
replacement coefficient 64 gives the valid union bound
\[
4n^{10}\exp[-(64^2/4)\ell_n]=o(1).
\]
The off-grid increment is
\(n^{-2}\sqrt n\,\operatorname{polylog}n=o(1)\).
Neither a union over deletion subsets nor conditioning on full-network
survival is introduced. The inherited control-uniform insertion event and
the fixed-common-cavity moment argument retain their roles.

Let \(U_{\rm fin}(S)\) denote the candidate's explicit recurrence (9).
Its coefficients are exactly the source response coefficients, with 64
substituted in the centered Gaussian term. They do not depend on the
sample count or the input dimension. The resulting stopped response bound
\[
\max_{v,a,j}\|R_a^{(j)}(v)\|_\infty
\le S U_{\rm fin}(S)\sqrt{\ell_n}
\]
is sufficient to rerun the time-pole improvement. In particular, for
\[
0<c\le\frac{a}{64YSU_{\rm fin}(S)}
       =\frac{a}{4\lambda S^2U_{\rm fin}(S)},\qquad
r_n=c/\sqrt{\ell_n},
\]
the total short-time preactivation increment is at most
\(8cYSU_{\rm fin}\le a/8\). No angular increment is present.
The source's explicit width gates remain necessary:
\[
n^{-1}\le Y,\qquad
\sqrt{\ell_n}\ge
c\max\{8,\lambda,4\mathcal K/\log2,32YSD_W\}.
\]
They preserve residual growth, activity, operator, and pole margins. The
complex-minus-real coefficient radii still vanish at every fixed \(c\),
so the source's budget-removal limit is unchanged. Thus this argument
does establish the larger finite-query rectangle with probability tending
to one; it does not silently assume it.

Every term of \(U_{\rm fin}(S)\) is nondecreasing in \(S\). Therefore
on the entire original allowance \(S\le S_*^{\rm src}\), the explicit
constant
\[
\chi_{\rm act}=
\min\left\{1,
\frac{a}{4(S_*^{\rm src})^2U_{\rm fin}(S_*^{\rm src})}\right\}>0
\]
depends only on the activations and depth, and permits
\[
c=\chi_{\rm act}/\lambda,
\qquad r_n=\frac{\chi_{\rm act}m}{\gamma\sqrt{\ell_n}}.
\]
The cap is on the dimensionless training-time factor \(\chi\), not
on the physical coefficient \(c\). Replacing \(c\) by
\(\min(1,c)\) would lose the sample/gap cancellation and is unnecessary.
For the simpler cap \(Y/\lambda\le\beta^{-30L}\), the recorded
power estimates give \(U_{\rm fin}\le\beta^{26L}\) and
\[
\frac{a}{4S^2U_{\rm fin}}
\ge\frac{\beta^{34L-1}}{64}>1.
\]
Thus \(\chi=1\) is valid there. This power simplification is optional;
it does not reduce the general recurrence-based scope.

## 3. Innovation and the resulting prediction lower bound

Define the scalar initialized variance recursion
\[
q_0=1,\qquad q_j=\mathbb E\phi_j(\sqrt{q_{j-1}}G)^2,
\qquad G\sim N(0,1),
\]
and \(\mu_4=\mathbb E\phi_L(\sqrt{q_{L-1}}G)^4\).
Unit input norms make these quantities activation/depth constants. For
\(m\ge2\) and positive final gap, \(q_L,\mu_4\) are positive.
Linear growth makes \(\mu_4\) finite.

The innovation calculation is valid for the uncentered covariance.
For the last Gaussian feature vector \(H\), put
\(Q=\mathbb E HH^\top\), \(c=Qy\), \(A=\|c\|_2\),
\(T=\operatorname{tr}Q\),
\(D=T-c^\top Qc/A^2\), and \(M_4=\mathbb E\|H\|_2^4\).
The area identity and truncation at squared radius \(2M_4/D\) give
\[
\operatorname{tr}\operatorname{Cov}(H H^\top y)
\ge \frac{A^2D^2}{4M_4}.
\]
Here \(D\ge(m-1)\gamma>0\), so the radius is legitimate.
Also \(M_4\le m^2\mu_4\), \(T=mq_L\), and, with
\(N=y^\top Q^2(TI-Q)y=A^2D\),
\[
N\ge(m-1)\gamma A^2,
\qquad N\ge\gamma^2(T-\gamma)\|y\|_2^2.
\]
The second bound follows by minimizing \(\xi^2(T-\xi)\) on
\([\gamma,T-\gamma]\); its smaller endpoint value is
\(\gamma^2(T-\gamma)\). Multiplying the two inequalities and
using \(T-\gamma\ge(m-1)q_L\) proves that a deterministic
training query \(v_a\) satisfies
\[
\operatorname{Var}(H_aH^\top y)
\ge\frac{\gamma^3q_L}{16\mu_4}Y^2.
\]
The initialized covariance recursion has a positive semidefinite added
last-layer innovation. The exact zero-readout derivative and independence
of the two runs consequently give
\[
\sqrt n\,[\dot f_n(0,v_a)-\dot{\widetilde f}_n(0,v_a)]
\Longrightarrow N(0,\sigma_a^2),\qquad
\sigma_a^2\ge\frac{\gamma^3q_LY^2}{2m^2\mu_4}.
\]
The query is fixed by the population quantities and labels; there is no
random post-selection of a query before applying this scalar CLT.

For completeness, the exact covariance differential required here is
\[
(T_jE)_{ab}=
\tfrac12E_{aa}\mathbb E[\phi_j''(Z_a)\phi_j(Z_b)]
+E_{ab}\mathbb E[\phi_j'(Z_a)\phi_j'(Z_b)]
+\tfrac12E_{bb}\mathbb E[\phi_j(Z_a)\phi_j''(Z_b)].
\]
The missing plus in the reviewed bridge (6) is a typographical error,
not a permissible product of the first two terms.

On the two-copy localized event, the complex output difference is bounded
by \(M=2SH_L^2\le32\beta^{6L}Y/\lambda\). The parameter-two
Bernstein ellipse for \([0,r_n]\) lies strictly inside the rectangle.
Its Chebyshev coefficient tail is at most \(2M2^{-N}\); its derivative
tail uses the exact identity
\(\sum_{k>N}k^2 2^{-k}=2^{-N}(N^2+4N+6)\).
The endpoint polynomial inequality \(|P'(-1)|\le N^2\|P\|_\infty\)
holds also for complex coefficients by interpolation and the triangle
inequality. These facts give
\[
\sup_{0\le t\le r_n}|g_n(t)|
\ge\frac{r_n}{2N^2}|g_n'(0)|-24M2^{-N}.
\]
Taking \(N=\lceil2\ell_n/\log2\rceil\le4\ell_n\) yields
the candidate's (23), including its coefficient 768. The explicit
remainder test (25), with coefficient 49152, is correct.

Let
\[
\mathcal D_n=\sup_{t\in[0,\infty]}\sup_{\|v\|=1}
 |f_n(t,v)-\widetilde f_n(t,v)|,
\qquad u_\delta=\Phi^{-1}(1/2+\delta/4),
\]
where \(0<\delta<1\) and \(\Phi\) is the standard normal CDF.
Combining the time coefficient and variance lower bound proves that,
at every sufficiently large individual width, with probability at least
\(1-\delta\),
\[
\mathcal D_n\ge
\frac{u_\delta\chi_{\rm act}}{64}
\sqrt{\frac{q_L}{2\mu_4}}\,
\frac{Y\sqrt\gamma}{\sqrt n\,\ell_n^{5/2}}.
\]
Under the simple cap, replace \(\chi_{\rm act}\) by one. The
\(m^{-1}\) in the onset standard deviation cancels the \(m\) in
the training time radius, and \(\gamma^{3/2}/\gamma=\sqrt\gamma\).
Thus the displayed constant has no hidden sample-count, input-dimension,
gap, label-amplitude, or label-direction dependence. The eventual width
may depend on all those fixed parameters.

No independence between the source event and the derivative is used:
subtract its vanishing failure probability from the CLT event. The
limiting Gaussian probability is \(1-\delta/2\), leaving a positive
margin to obtain \(1-\delta\) eventually. The witness is transient;
fitted values agree at every training input. This neither proves a strict
root-width lower bound nor a fitted-endpoint lower bound. For \(m=1\),
the constant-activation counterexample remains valid.

## 4. Current Legendre order and comparison to actual noise

Use the current sample-polynomial statement, not its older superseded
order envelope. With its \(P_n\) and
\[
Q_n=\max\{3,P_n,n^{1/4}\sqrt{P_n}\},\qquad
q_n=\left\lceil4Q_n[\log(e+Q_n)]^{1/4}\right\rceil,
\]
the simultaneous-in-order bound is
\[
E_n(q)=\frac{Y P_n\sqrt{\log(eq)}}{q^2},\quad q\ge P_n,
\qquad E_n(q_n)\le\frac{Y}{8\sqrt n}.
\]
The latter, stronger coefficient follows from the complete refinement
proof, although the statement safely enlarges it to \(Y/\sqrt n\).
Set \(q_n'=\lceil q_n\ell_n^{3/2}\rceil\). Because
\(q_n=n^{1/4+o(1)}\),
\[
\frac{\log(eq_n')}{\log(eq_n)}\longrightarrow1,
\qquad
E_n(q_n')\le\frac{2Y}{\sqrt n\,\ell_n^3}
\]
eventually. This uses one event valid for every order, so the larger
order introduces no probability union. Relative to the positive lower
threshold just proved, the error ratio is at most a fixed coefficient
times \(\ell_n^{-1/2}/\sqrt\gamma\), which tends to zero with the
problem fixed. The same proof works for the candidate's older order,
but the current quarter-log order avoids an unnecessary logarithm.

For a finite-width target \(\eta P/(\sqrt n\ell_n^{5/2})\), where
\(P>0\) is a lower-threshold coefficient and \(\eta>0\), a compatible
explicit inversion is
\[
Q=\max\left\{3,P_n,n^{1/4}\ell_n^{5/4}
                      \sqrt{\frac{Y P_n}{\eta P}}\right\},
\qquad q=\left\lceil4Q[\log(e+Q)]^{1/4}\right\rceil.
\]
The same endpoint logarithm calculation gives
\(E_n(q)\le YP_n/(8Q^2)\), below the target. This retains the
quarter-log inversion and the absorption condition \(q\ge P_n\).

For the compact model, its unchanged raw bound is
\[
\|f_C-f_n\|_*
\le C_{\rm out}n^{-1}e^{a_0+b_0\sqrt{\ell_n}}
          +C_{\rm tail}e^{-8\ell_n}.
\]
Dividing by \(P/(\sqrt n\ell_n^{5/2})\) gives an upper bound by
\[
\frac{C_{\rm out}}P n^{-1/2}\ell_n^{5/2}
e^{a_0+b_0\sqrt{\ell_n}}
+\frac{C_{\rm tail}}P n^{-15/2}\ell_n^{5/2}\longrightarrow0.
\]
The candidate's additional deterministic tests (36) imply a prescribed
relative target and are sufficient as written. No source refinement or
extra compact storage is needed.

Consequently, on events of probability at least \(1-\delta\) at every
sufficiently large individual width, both approximation errors divided
by the actual dense-copy discrepancy tend to zero through the displayed
deterministic bounds. Equivalently, with any convention on the
zero-discrepancy event, these error/discrepancy ratios converge to zero
in probability: for each fixed \(\delta>0\), use its lower coefficient,
then send \(\delta\) down to zero after the width limit. A fixed
positive lower coefficient alone would not give probability tending to
one. The joint comparison remains valid by a finite union of vanishing
source failures.

The Legendre moving count stays \(n^{5/4+o(1)}\); its fixed mixers
retain \((L-1)n^2\) coordinates. The compact retained count stays at
its existing polylogarithmic bound with the actual \((Ym/\gamma)^4\)
factor. These are sufficient counts, not representation lower bounds.
The finite-query proof improvement does not reduce the whole-sphere
compressor's dimension-dependent storage. The sharper numerical Legendre
corollary uses its stated simple label cap; the general lower theorem
retains the original recurrence-based source and real-fitting cap.

## 5. Audit disposition

The mathematical mechanisms and all quantitative cancellations needed for
the requested general lower bound pass this internal reconstruction. The
candidate's missing plus in (6) must be fixed before its formulas are used
literally. Its §5 should point to the current quarter-log Legendre order
when presenting the strongest existing storage prescription. Neither
correction requires a stronger source event, a smaller observation norm,
an odd or bounded activation, a centered covariance assumption, orthogonal
training data, a trained CLT, or an infinitesimal-label limit.

The remaining qualifications are substantive: fixed-data asymptotics,
\(m\ge2\) for gap-only nondegeneracy, the inherited explicit small-label
allowances, unquantified stochastic/CLT success width, a logarithmic loss,
and no endpoint or universal storage lower bound.
