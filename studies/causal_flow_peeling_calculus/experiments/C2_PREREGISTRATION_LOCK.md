## C2 — Response-weighted bulk JVP occupation (locked before implementation)

Lock date: 2026-08-24. This section was written from the finite-model definition in the task, before inspecting any local experiment helper, prior result, or repository theory artifact. It is an empirical finite-width audit only; no outcome proves or disproves an infinite-width theorem.

### Decision question and claim level

For the exact depth-3 flow below, does the response-weighted bulk energy of the full-trajectory directional derivative at layer 2 remain width-stable through time 0.5, with no increasing alignment between response energy and rare large values of the same-trajectory field \(|r_2|\)? The tested claim is only finite-instance empirical support or disfavor for this mechanism/witness.

### Canonical model

At width \(n\), all vectors have length \(n\), \(G_1,G_2\in\mathbb R^{n\times n}\), and \(\langle a,b\rangle_n=n^{-1}\sum_i a_i b_i\). Independently at \(t=0\), \(u_i,A_i\sim N(0,1)\) and every persistent entry of \(G_1,G_2\) is \(N(0,1/n)\). The same realized matrices are reused in every transpose; no independent backward matrices are permitted. With \(\phi(s)=\arctan s\),

\[
z_1=u,\quad x_1=\phi(u),\quad z_2=G_1x_1,\quad x_2=\phi(z_2),\quad z_3=G_2x_2,\quad x_3=\phi(z_3),
\]
\[
b_3=A\phi'(z_3),\quad r_2=G_2^\top b_3,\quad b_2=\phi'(z_2)r_2,\quad r_1=G_1^\top b_2,\quad b_1=\phi'(u)r_1,
\]
\[
A'=x_3,\quad G_2'=b_3x_2^\top/n,\quad G_1'=b_2x_1^\top/n,\quad u'=b_1.
\]

No architecture, sign, transpose, scaling, distribution, or time horizon may be changed after this lock.

### Marked perturbation and full-trajectory JVP

The marked column is \(j=0\). Independently draw \(h\sim N(0,I_n)\), and set only
\[
\Delta G_2(0)_{:j}=h/\|h\|_2,
\]
with \(\Delta A(0)=\Delta G_1(0)=\Delta u(0)=0\) and all other columns of \(\Delta G_2(0)\) zero. Thus the actual column perturbation has Euclidean norm one, equivalently \(\langle |\sqrt n\,\Delta G_{2,:j}|^2\rangle_n=1\), fixing the persistent-matrix standardization. The tangent is evolved jointly with every primal state by differentiating the complete ODE at every integration stage. A frozen-state or endpoint-only derivative is forbidden.

The bulk index set is \(B=\{1,\ldots,n-1\}\), excluding the marked coordinate. The primary fields are
\[
V^{(r)}_k=D r_{2,k}(t)[\Delta G_2(0)],\qquad
V^{(b)}_k=D b_{2,k}(t)[\Delta G_2(0)],\qquad k\in B.
\]
\(V^{(r)}\) is primary because the proposed exponential occupation weight is a function of the same causal back-propagated field \(r_2\). \(V^{(b)}\) is a joint mechanism check because \(b_2=\phi'(z_2)r_2\) is the gated layer-2 field that drives \(G_1'\). The JVPs of \(z_2\) and \(x_2\) are secondary propagation diagnostics only (and are expected to be exactly zero at \(t=0\)); they cannot rescue a failed primary result.

### Fixed grid, replication, and integration

- Widths: \(n\in\{128,256,512,1024\}\).
- Observation times: \(t\in\{0,0.25,0.5\}\).
- Main ensemble: 48 independent model/direction replicates per width, generated from root seed 20260824 with a documented deterministic seed map. The first and second 24 replicates are preassigned confirmation halves.
- Main solver/state dtype: classical fixed-step RK4 with \(\Delta t=1/64\), float32 CUDA state and tangent arithmetic. All reductions and exponential-weight diagnostics are evaluated after conversion to float64; weights are never clipped.
- Mesh control: the first 8 seeds at widths 256 and 1024 rerun with RK4 \(\Delta t=1/128\), float32 CUDA.
- Precision control: the same first 8 seeds and canonical initial variates at widths 256 and 1024 rerun with RK4 \(\Delta t=1/64\), float64 CUDA.
- Tangent validation: the first 4 seeds at width 128 in float64, comparing the evolved tangent with central finite differences of the entire integrated trajectory at perturbation sizes \(2^{-7}\) and \(2^{-9}\).
- There is no post-result width, time, \(\lambda\), seed, or solver search. The terminal stop is the grid above plus the preauthorized controls.

### Preregistered weights and unweighted normalization

The nonzero test values are \(\lambda\in\{0.05,0.10,0.20\}\), with \(\lambda=0\) retained as the baseline. These are fixed before seeing any field values. For each primary field, replicate, width, and time, define without self-normalizing by the weights
\[
M_V(\lambda;n,t)=n\left\langle e^{\lambda r_{2,k}(t)^2}|V_k(t)|^2\,1_{\{k\in B\}}\right\rangle_n
=\sum_{k\in B}e^{\lambda r_{2,k}(t)^2}|V_k(t)|^2.
\]
This exact sum is the primary scaling observable. In particular, it is not divided by \(\sum e^{\lambda r_2^2}\), by an effective sample size, or by \(M_V(0)\).

For the separate factorization diagnostic, let \(\bar w_B=(n-1)^{-1}\sum_{k\in B}e^{\lambda r_{2,k}^2}\) and
\[
F_V=M_V(\lambda)/(M_V(0)\bar w_B).
\]
For each instance, 32 independently seeded permutations of the bulk weights give \(M_V^{\rm shuf}\) and \(F_V^{\rm shuf}\). This shuffle preserves the realized weight and response-energy marginals but destroys coordinate alignment. The alignment contrast is the pooled log ratio between the true moment and the mean shuffled moment. As a diagnostic sensitivity check only, a rank-aligned positive control pairs the largest weights with the largest \(|V|^2\).

### Rare-event and contribution diagnostics

For contributions \(c_k=e^{\lambda r_{2,k}^2}|V_k|^2\), record the unrounded sum, maximum contribution fraction \(\max_kc_k/\sum_kc_k\), and relative effective sample size
\[
\mathrm{rESS}=\frac{(\sum_kc_k)^2}{(n-1)\sum_kc_k^2}.
\]
Also record the fractions of unweighted response energy \(\sum|V|^2\) lying in the largest 5% and (for \(n\ge256\)) largest 1% of coordinates ranked by \(|r_2|\), plus the same weighted-contribution tail fractions. Report arithmetic mean, median, 10/90% quantiles, and the two fixed replication halves. Weight-only ESS and maximum weight share are nuisance diagnostics.

### Estimation and fixed discriminators

For every \((V,t,\lambda>0)\) primary cell:

1. Estimate a width exponent \(\beta\) by ordinary least squares of \(\log[48^{-1}\sum_s M_{V,s}(\lambda;n,t)]\) on \(\log n\), using all four locked widths.
2. Estimate the alignment level \(a_n=\log[(\sum_sM_{V,s})/(\sum_s\overline{M}^{\rm shuf}_{V,s})]\) and its width slope \(\alpha\) on \(\log n\).
3. Use 5,000 seed-level bootstrap resamples within width. Familywise 95% one-sided bounds across the 18 primary cells are formed with the bootstrap maximum-deviation statistic. Seeds, permutations, bootstrap seed 20260825, formulas, and all raw per-instance summaries are retained.

An **empirical pass** requires all numerical-validity gates and, simultaneously across both primary fields, all times, and all three nonzero \(\lambda\)'s:

- the familywise upper bound for \(\beta\) is at most 0.20;
- the familywise upper bound for \(\alpha\) is at most 0.10 and that for \(a_{1024}\) is at most 0.15;
- at \(\lambda=0.20,n=1024\), the median contribution rESS is at least 0.05 and the median maximum contribution share is at most 0.10;
- neither fixed 24-replicate half has point estimates beyond the fail thresholds below.

An **empirical fail** requires all numerical-validity gates and a replicated adverse pattern: in at least two adjacent \(\lambda\)'s for the same field/time, either the cellwise 95% lower bound for \(\beta\) exceeds 0.30, or both the lower bound for \(\alpha\) exceeds 0.15 and the lower bound for \(a_{1024}\) exceeds 0.30. The same sign and the relevant point-estimate threshold must occur in both preassigned replication halves. A median maximum contribution share above 0.20 at \(\lambda=0.20\) that also increases by at least a factor 1.5 from width 512 to 1024 in both halves is an alternative replicated rare-dominance fail.

Every other statistically valid result is **inconclusive**, including a mixed result between \(r_2\) and \(b_2\). Exact factorization is described separately: it is called compatible only where the familywise interval for the true-versus-shuffled log contrast contains zero and lies inside \([-0.15,0.15]\); otherwise it is reported as resolved positive/negative alignment or inconclusive, without overriding the occupation verdict.

### Numerical-validity gates

- CUDA must be available and all announced production runs must execute there. No nonfinite state, tangent, contribution, or unclipped exponential weight is allowed. No trajectory may have an absolute state/tangent entry above \(10^6\).
- At width 128, time 0.5, the fine central-difference JVP relative \(\ell_2\) error for each of the bulk \(r_2,b_2,z_2,x_2\) fields must be at most \(2\times10^{-4}\), and it may not exceed 1.2 times the coarse-step error (an absolute-error floor of \(10^{-12}\) is used only in this ratio).
- For every paired mesh-control trajectory and each primary field/time, the relative \(\ell_2\) difference between \(\Delta t=1/64\) and \(1/128\) must be at most \(5\times10^{-4}\). The corresponding \(M_V\) relative difference at every locked \(\lambda\) must be at most 0.5%.
- For every paired precision-control trajectory and each primary field/time, float32 versus float64 relative \(\ell_2\) difference must be at most \(10^{-3}\), and the corresponding \(M_V\) relative difference must be at most 1%. Canonical initial normal variates and perturbation directions must be shared before casting.
- At least 46 of 48 main trajectories per width must be valid. If a validity gate fails, the scientific outcome is inconclusive; the failed diagnostic is reported, and no unregistered repair run is permitted.

### Interpretation ledger

- Pass: finite-width empirical support through \(t=0.5\) for the specified response-weighted occupation/factorization mechanism in this exact witness; not convergence and not a theorem.
- Fail: empirical disfavor for this mechanism/witness on the locked grid; it does not refute a broader closure or existence claim.
- Inconclusive: the finite grid, Monte Carlo precision, or numerical controls do not discriminate.

The rank-aligned control, \(z_2/x_2\) propagation fields, and any visual trend not named above are descriptive only.

### Post-lock, pre-run analytic caveat (not a gate change)

After this design was frozen but before any C2 code was executed, an analytic
correction established that already at finite \(n\) and \(t=0\), conditional
on \(u,G_1,G_2\), \(r_{2,i}\) is Gaussian in \(A\) with variance
\(S_i=\sum_m G_{2,mi}^2\phi'(z_{3,m})^2\), and \(S_i\) has unbounded support.
Consequently \(\mathbb E\exp(\lambda r_{2,i}^2)=\infty\) for every
\(\lambda>0\). This is a proof-level falsifier of any annealed or uniform
square-exponential moment premise, regardless of the numerical outcome.
The locked square-exponential grid and gates remain unchanged to avoid a
post-hoc pivot. Any finite-run C2 classification therefore applies only to
the deliberately finite, typical-sample diagnostic and cannot be cited as
support for uniform integrability or a theorem.
