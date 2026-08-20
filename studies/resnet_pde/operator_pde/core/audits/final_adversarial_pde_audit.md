# Final adversarial audit: genuine operator-Galerkin neural PDE

> **Compact-edition provenance note.** This audit was written against the
> original 689 MB release. Its present-tense inventory statements about raw
> traces, 61 NPZ archives, 2,000-replicate bootstrap arrays, and the former
> 136-file manifest refer to that full release, not to this compact
> source-first edition. This edition intentionally omits raw arrays while
> retaining the complete regeneration and evidence-verification code, compact
> summaries, figures, and audit text.

## Executive verdict

The new implementation crosses the literal threshold that the earlier
finite-matrix \(q/r\) experiments did not:

\[
\boxed{\text{a genuine, autonomous, width-independent neural PDE was
actually integrated.}}
\]

This is not a relabeling of a finite dense network.  The PDE state has no
network width \(n\), no original residual depth \(L\), and no
\(n\times n\) weight matrix.  Its characteristic velocity is explicit,
current-state local, and independent of every dense reference curve.  The
same finite operator coefficients define the forward action and its
transpose.  The finite-\(P\) dynamics are exactly a projected Euclidean
\(\mu\)P gradient flow and pass independent gradient, tangent-kernel,
positive-semidefiniteness, restart, and implementation-agreement tests.

The stronger identification claim does **not** pass:

\[
\boxed{\text{the experiment does not establish that this PDE is the
ordered }n\to\infty,\ L\to\infty,\ P\to\infty\text{ limit.}}
\]

The preregistered held-out reference is especially important.  Against
128 independent dense networks at \(n=256,L=32\), the primary \(P=5\)
PDE has the full-curve Gram-increment discrepancy

\[
7.2433433\times 10^{-3},
\]

which is \(1.1428\%\) of the PDE's \(0.6338011\) feature motion.  This is
small in effect size but statistically resolved relative to the finite
reference's Monte Carlo error: the pooled and block-stratified curvewise
95% thresholds in the final frozen ordered-limit audit are
\(5.0620\times10^{-3}\) and \(4.9812\times10^{-3}\), with
centered-bootstrap tail probabilities \(0.00300\) and \(0.00350\).
Therefore the release must say “close but
distinguishable at this finite \((n,L,P,N,M,R)\),” not “indistinguishable”
or “below the reference noise floor.”

The separately preregistered ordered-limit holdouts add the L-shaped steps
\((256,32)\to(512,32)\) and \((256,32)\to(256,64)\).  Their exact-network
Gram-increment Cauchy gaps are \(9.3504\times10^{-3}\) and
\(4.2263\times10^{-3}\), respectively.  Neither is statistically resolved:
the pooled/stratified 95% thresholds are
\((9.9672,10.3062)\times10^{-3}\) for width and
\((8.5680,8.9785)\times10^{-3}\) for depth.  The \(P=5\) PDE gap against
the pooled \(n=256,L=64,S=64\) reference is
\(6.5639\times10^{-3}\) and is not resolved; against the noisier
\(n=512,L=32,S=16\) reference it is \(9.8974\times10^{-3}\), narrowly above
that reference's \(9.2157\times10^{-3}\) threshold
(\(\widehat p=0.02799\)).  These mixed finite-grid outcomes do not identify
an ordered limit.

That finite discrepancy does not refute the candidate PDE.  The current
grid cannot separate finite width, finite residual depth, finite Hermite
order, depth discretization, cubature bias, and reference sampling error.
The measured discrepancy decreases substantially along the original
fixed-\(L=32\) width ladder through \(n=256\), while the small \(n=512\)
holdout is sampling-limited and does not continue that monotone curvewise
trend.  The paired-\(W\) diagnostic gives the required \(1/L\) conditional
variance scaling.  These are real positive signals, but they are not an
ordered-limit extrapolation.

A clean nested Hermite check makes the uncertainty sharper rather than
removing it.  With an exact order-three Gauss--Hermite base rule and refined
fast QMC, increasing from the complete degree-one basis \(P=5\) to the
complete degree-two basis \(P=15\) changes the Gram surface by only
\(2.76\times10^{-3}\), but moves the finite-reference Gram-increment gap
from \(7.54\times10^{-3}\) to \(9.22\times10^{-3}\).  Thus the first valid
higher-order correction does not move the primary observable toward the
dense \(n=256,L=32\) mean.  Two basis levels cannot determine the
\(P\to\infty\) limit, but this negative direction must be reported.
For the fixed Sobol \(P=5\) and \(P=15\) pair used in the ordered audit,
\(P=15\) is statistically farther from all three pooled references:
\(n=256,L=32,S=128\), \(n=256,L=64,S=64\), and
\(n=512,L=32,S=16\).

## Scope and audit standard

I audited:

- `src/dense_pde/operator_galerkin.py`;
- `run_pde.py`;
- `theory/operator_galerkin_pde.md`;
- the dense reference implementation and its tests;
- the frozen protocol, release verifier, raw PDE/reference archives,
  processed tables, and figures;
- the independent derivation, numerical implementation, statistical
  analysis, and earlier hostile audit under `audits/`;
- the preregistered \(S=128\) held-out-reference update;
- the separately preregistered \(n=512,L=32,S=16\) and
  \(n=256,L=64,S=48\) ordered-limit holdouts.

The verdicts below mean:

- **PASS:** the hard property is directly established for the implemented
  finite PDE or archived experiment;
- **PARTIAL:** substantial evidence exists, but a necessary numerical or
  mathematical limit remains unresolved;
- **FAIL:** the release does not establish the stated stronger claim.  A
  FAIL on a limit claim is not a claim that the finite PDE code is wrong.

## Hard-gate table

| Gate | Verdict | Audit finding |
|---|---|---|
| 1. Canonical dense model is locked | **PASS** | The reference is the fully dense residual-tanh network \(h^{\ell+1}=h^\ell+\gamma L^{-1}\tanh(W_\ell h^\ell)\), \(f=a^\top h^L/n\), with iid \(W_{\ell,ij}\sim N(0,\sigma_w^2/n)\) and ordinary Euclidean multipliers \(\eta_W=L,\eta_B=\eta_a=n\). All \(B,W,a\) blocks train. |
| 2. Literal width/depth-independent PDE | **PASS** | `PDESpec` has no \(n\) or original \(L\). The mathematical source coordinates are \((s,\theta,w)\in[0,1]\times\mathbb R^{d+1}\times\mathbb R^P\). \(N,M,R\) are numerical depth/cubature resolutions, not network width or original layer count. |
| 3. No dense microscopic state or action | **PASS** | The characteristic state is only `B`, `a`, and `c` with shape \((N,M,R,P)\). The PDE module allocates no two-neuron-index matrix, performs no dense \(W@u\), and loads no finite-network checkpoint. |
| 4. Explicit finite drift | **PASS** | The Liouville velocity \(V_j=-\gamma\sum_q e_q\beta_qH_{jq}\), forward depth equation, backward adjoint, \(B\)-flow, \(a\)-flow, initialization, and all moments are explicitly given and directly implemented. No unspecified tag compiler or hidden drift DAG remains. |
| 5. Autonomy and restartability | **PASS** | The RHS depends only on the current \((B,a,c)\), fixed compiler/quadrature, and current moments. Direct versus split integration agrees to roundoff. The loader hashes the full static compiler and every quadrature array; a same-shape wrong-seed restart is rejected. At a serialized positive-time state, changing \(y\) changes the drift exactly through the new current residual, with maximum linearity defect \(4.44\times10^{-16}\), while the forward/adjoint fields remain bitwise unchanged. A fresh \(0.2\)-time continuation under that changed target reduced loss monotonically from \(0.2950\) to \(0.07587\). |
| 6. Shared transpose / projected Onsager structure | **PASS** | The same row coefficients \(\sigma_w\epsilon+c\) define \(W_P\) and \(W_P^\ast\). Pairing defects are at roundoff, and an intentionally independently permuted backward row is detected. This proves the finite-\(P\) pairing; identifying it with the canonical dense conditional Onsager mean remains part of Gate 14. |
| 7. Standard Euclidean \(\mu\)P projection and normalization | **PASS** | Re-derivation gives \(\dot c_p=-\gamma\sum_qe_q\beta_qH_{pq}\) with no spurious \(1/N\); the depth metric contributes \(\gamma^2/N\) to the tangent kernel. Positive-time coordinate-gradient defects are at most \(1.41\times10^{-11}\), and the full energy-identity defect is \(7.62\times10^{-13}\). |
| 8. Exact PDE readouts and tangent kernel | **PASS** | Outputs and every depthwise \(3\times3\) hidden Gram are direct moments of the current PDE state. The same-system identity \(\dot f=-\Theta_Pe\) holds, \(\Theta_P\succeq0\), and \(\dot{\mathcal L}=-e^\top\Theta_Pe\). Across 20 perturbed states the largest directional defect was \(1.70\times10^{-10}\). |
| 9. Anti-oracle separation | **PASS** | The PDE source neither imports nor reads the dense reference, result tables, or target curves. The PDE run is completed before reference analysis. No coefficient fitting was performed in the held-out audit. Dense files enter only post hoc comparison code. |
| 10. Independent implementation reproducibility | **PASS** | Two independently written characteristic implementations agree, under identical tensor cubature, to \(2.78\times10^{-16}\) in outputs and \(8.88\times10^{-16}\) in every time/depth Gram entry. The main suite passed 12/12 tests and the independent suite 4/4 tests. |
| 11. Time integration and depth discretization | **PASS** | PDE RK4 \(dt=.02\) versus \(.01\) differs by \(6.83\times10^{-8}\) in output and \(1.09\times10^{-7}\) in Grams. \(N=16\) versus \(32\) differs by \(2.05\times10^{-4}\) and \(8.45\times10^{-4}\), respectively. An independent active-transient dense-reference spot check at \(n=64,L=32\) found \(dt=.02\) versus \(.005\) differences \(1.14\times10^{-7}\) in output, \(1.85\times10^{-7}\) in Grams, and \(5.91\times10^{-7}\) in the tangent kernel. These are well below the observed finite-reference Gram discrepancy. |
| 12. Cubature and Hermite-order convergence | **PARTIAL** | Isolated \(M\) and \(R\) refinements are at the \(10^{-3}\) Gram scale and independent QMC scrambles spread by \(2.13\times10^{-3}\). The low-order GH/QMC Gram difference is \(1.94\times10^{-2}\). A clean nested hybrid rule gives a \(P=5\to15\) Gram change \(2.761\times10^{-3}\); refining the \(P=15\) fast rule from \(R=128\) to \(256\) changes Grams by \(9.648\times10^{-4}\). This is a valid first basis step, but \(P=15\) moves the dense-reference Gram gap upward. The fixed Sobol \(P=15\) curve is statistically farther than \(P=5\) against all three ordered-audit references. A new complete-cubic \(P=35\) run has exact base cubature but underresolved \(R=128\) fast cubature (raw condition \(6.20\)); it moves farther away and is directional stress evidence, not a converged third level. There is not yet a cofinal \(P,M,R\) sequence. |
| 13. Dense finite-reference curve agreement | **PARTIAL** | The PDE predicts \(O(1)\) nonlazy feature motion and tracks every tested finite-reference Gram curve at roughly the one-percent scale. The \(P=5\) gap is resolved for \(n=256,L=32,S=128\), not resolved for pooled \(n=256,L=64,S=64\), and narrowly resolved for \(n=512,L=32,S=16\). Thus close finite-curve agreement is real, but exact finite-\((n,L)\) agreement is not. |
| 14. Identification with the ordered dense limit | **FAIL / OPEN** | A preregistered L-shaped audit now gives one width step at \(L=32\) and one depth step at \(n=256\); neither exact Cauchy gap is statistically resolved. This is useful finite-grid stability evidence, but there is still no width extrapolation at several fixed depths followed by a depth extrapolation. Trained iid-depth homogenization, survival of the conditional Onsager mean, and \(P\to\infty\) Hermite-tail control remain unproved. |
| 15. Global-time prediction | **PARTIAL** | The fixed PDE genuinely integrates through the active transient and remains flat from \(t=8\) to \(32\), with output/Gram drift below \(5\times10^{-13}\). Dense ensembles are directly compared only through \(t=8\), though they are already flat on \(t\in[4,8]\). This excludes a merely local Taylor fit but does not establish uniform accuracy on \([0,\infty)\) or on a restart neighborhood. |
| 16. Arbitrary-accuracy finite PDE existence | **FAIL / OPEN** | One explicit low-order finite PDE has been simulated. No cofinal convergent PDE sequence, effective residual certificate, or all-time uniform error theorem has been demonstrated. |
| 17. Equivalence to the earlier \(K/J/N\) response compiler | **FAIL / NOT CLAIMED** | The earlier note does not emit \(J_\ast\), tag/history tables, \(\Gamma\), or a finite drift. This release correctly presents a new Hermite/isonormal operator-Galerkin candidate, not a simulation of that prose-level compiler. |
| 18. Release-level reproducibility | **PASS** | Source, protocol, tests, raw traces, analyses, an exact-version `environment.json`, and an exact `requirements-lock.txt` are present. The full protocol includes the held-out \(S=128\) block, hybrid \(P\)-checks, and the preregistered ordered-limit holdouts. A 136-file SHA-256 manifest was frozen and passed a read-only checksum verification; the same pass ran all 12 main tests, all 4 independent tests, and the evidence verifier over 61 complete NPZ archives. Interrupted files remain outside the release. |

## Why this is genuinely a PDE

Let \(\theta=(B_i(0),a_i(0)/A)\sim\mu\), and let
\(\{\phi_j\}_{j=1}^P\) be the fixed Hermite family.  The retained action of
one dense row on a slow field \(v\) is

\[
(W_Pv)(\theta,w)
=\sum_{j=1}^P w_j\langle\phi_j,v\rangle_\mu .
\]

The current row coefficient has law \(\rho_{s,t}^{\theta}(dw)\), initially
\(N(0,\sigma_w^2I_P)\), and obeys

\[
\partial_t\rho_{s,t}^{\theta}
+\nabla_w\!\cdot(\rho_{s,t}^{\theta}V)=0,
\qquad
V_j=-\gamma\sum_qe_q\beta_q
\langle\phi_j,h_q\rangle_\mu .
\]

The transpose used by the backward field is

\[
(W_P^\ast\psi)(\theta)
=\sum_j\phi_j(\theta)
\int \mu(d\theta')\int w_j\psi(\theta',w)
\,\rho_{s,t}^{\theta'}(dw).
\]

This gives exactly

\[
\langle W_Pv,\psi\rangle_{\mu\otimes\rho}
=\langle v,W_P^\ast\psi\rangle_\mu .
\]

The characteristic code represents the current conditional law with fixed
quadrature labels \((\theta,\epsilon)\) and learned coordinates
\(c\in\mathbb R^P\), where \(w=\sigma_w\epsilon+c\).  The large number of
quadrature characteristics does not turn this into a finite dense network:
there is no pairwise particle matrix and every interaction is through
population moments.  Increasing \(M,R,N\) refines numerical integration of
the same finite-\(P\) PDE.

## Evidence that is strong

### Algebra and implementation

- Shared forward/transpose pairing holds to roundoff.
- Weighted coordinate finite differences validate \(B,a,c\) velocities at
  a generic positive-time, nonorthogonal, nonunit-parameter state.
- The same-system energy and tangent-kernel identities hold at positive
  time and under random state perturbations.
- Direct and serialized restart continuations agree to roundoff.
- A wrong quadrature seed with identical state shapes is rejected.
- At one serialized positive-time state, changing the target by a generic
  three-coordinate perturbation changed the \(B,a,c\) velocity with norms
  \(1.107,1.103,7.198\), respectively.  The change agreed with the
  label-separated residual formula to \(4.44\times10^{-16}\); the
  forward/adjoint fields, which do not depend on \(y\) at fixed state,
  agreed exactly.  Continuing the same finite PDE for \(0.2\) training-time
  units under the changed target reduced loss monotonically from \(0.2950\)
  to \(0.07587\), with negative analytic loss derivative throughout.
- Every audited PDE archive labels and stores only the declared
  \((N,M,R,P)\) characteristic state.
- Two independent solvers reproduce the same finite-cubature equation to
  roundoff.

### Nonlocal-in-training-time behavior

The primary PDE moves its hidden Gram by
\[
0.6338011
\]
and fits the residual, so it is not a frozen or lazy kernel trajectory.
Without changing \(P,N,M,R\), it remains flat for an additional 24 units:

\[
\max_{8\le t\le32}\|f(t)-f(8)\|
=4.996\times10^{-13},
\]

\[
\max_{8\le t\le32,s}
\|G(s,t)-G(s,8)\|_F
=4.236\times10^{-13}.
\]

The dense references are also operationally flat by \(t=4\) to \(8\).
This is persuasive evidence that the success is not a local training-time
Taylor approximation.

### Homogenization diagnostic

Pairs sharing \(B(0),a(0)\) and redrawing every \(W_\ell\) give fitted
conditional-variance slopes

\[
\begin{array}{c|cc}
&t=0&t=0.5\\ \hline
H_L&-1.0193&-1.0039\\
P_0&-0.9993&-0.9924 .
\end{array}
\]

Thus the fast-layer variance behaves as \(1/L\), including after training
begins, as required for \(L^{-1/2}\) RMS cancellation.  This is a
well-targeted necessary diagnostic.  It is not a trained propagation-of-
chaos theorem.

### Width trend

Using Gram increments to remove independent initialization offsets, the
PDE/reference sup discrepancies at fixed \(L=32\) are approximately

| width/reference | Gram-increment gap |
|---|---:|
| \(n=64,S=64\) | \(2.464\times10^{-2}\) |
| \(n=96,S=48\) | \(1.169\times10^{-2}\) |
| \(n=128,S=96\) | \(9.255\times10^{-3}\) |
| \(n=256,S=128\) | \(7.243\times10^{-3}\) |
| \(n=512,S=16\), held out | \(9.897\times10^{-3}\) |

The monotone decrease through \(n=256\) is encouraging.  The much smaller
held-out \(n=512\) ensemble does not continue it: its gap is dominated by an
early-time maximum, while its terminal gap is only
\(3.993\times10^{-3}\).  The exact \(n=512\)-versus-\(n=256\) Cauchy gap is
not statistically resolved.  These noisy curvewise norms are not a signed
asymptotic expansion and cannot support an \(n\to\infty\) extrapolation.

## The held-out results change the statistical wording

### Enlarged \(n=256,L=32\) reference

The first \(S=64\) comparison gave a Gram-increment gap
\(6.731\times10^{-3}\), just below its estimated 95% curvewise sampling
threshold \(7.392\times10^{-3}\).  A protocol was then frozen before a new
64-seed block with `seed_start=10000` was read.

Pooling all 128 distinct seeds gives:

| Quantity | Value |
|---|---:|
| output sup gap | \(1.0753\times10^{-2}\) |
| loss-of-mean sup gap | \(1.8457\times10^{-3}\) |
| absolute-Gram sup gap | \(1.9408\times10^{-2}\) |
| Gram-increment sup gap | \(7.2433\times10^{-3}\) |
| tangent-kernel sup gap | \(3.3404\times10^{-2}\) |
| Gram-increment gap / PDE feature motion | \(1.1428\%\) |

Only the preregistered primary Gram-increment metric is statistically
resolved by both bootstrap schemes.  Output, loss, absolute Gram, and
tangent-kernel discrepancies remain below their respective bootstrap
thresholds.  Leave-one-block-out Gram-increment gaps range from
\(6.731\times10^{-3}\) to \(7.852\times10^{-3}\), so the primary result is
not driven by one block.

The maximum Gram-increment discrepancy occurs at the terminal stored time
\(t=8\) and terminal depth \(s=1\).  It is therefore a learned-feature
discrepancy, not an initialization offset.

### Preregistered L-shaped width/depth audit

Before either new archive was read, the audit fixed the two held-out blocks,
the two unchanged Sobol PDE files, every metric, interpolation rule,
subblock, bootstrap scheme, seed, and decision rule.  Both archives passed
full decompression, exact metadata/seed/shape checks, exact recomputation of
stored means and SEMs, finiteness, Gram/kernel PSD, and \(t=4\to8\)
plateau checks.

The exact Cauchy results are:

| Finite step | Gram-increment gap | pooled 95% | stratified 95% | Decision |
|---|---:|---:|---:|---|
| \(n:256\to512\) at \(L=32\) | \(9.3504\times10^{-3}\) | \(9.9672\times10^{-3}\) | \(1.0306\times10^{-2}\) | not resolved |
| \(L:32\to64\) at \(n=256\) | \(4.2263\times10^{-3}\) | \(8.5680\times10^{-3}\) | \(8.9785\times10^{-3}\) | not resolved |

This is evidence of finite-grid Cauchy stability, especially in depth.  It
is not evidence that either gap is zero.  The \(n=512\) result has only 16
members; its two predeclared eight-seed halves give width gaps
\(1.1139\times10^{-2}\) and \(8.5894\times10^{-3}\).

For the fixed PDEs:

| Reference | \(P=5\) gap | \(P=5\) decision | \(P=15\) gap | \(P=15\) decision |
|---|---:|---|---:|---|
| \(n=256,L=32,S=128\) | \(7.2433\times10^{-3}\) | resolved | \(9.2020\times10^{-3}\) | resolved |
| \(n=256,L=64,S=64\) | \(6.5639\times10^{-3}\) | not resolved | \(8.4811\times10^{-3}\) | resolved |
| \(n=512,L=32,S=16\) | \(9.8974\times10^{-3}\) | narrowly resolved | \(1.1730\times10^{-2}\) | resolved |

The signed \(P=5\) minus \(P=15\) improvements are
\(-1.959,-1.917,-1.833\)\(\times10^{-3}\), respectively.  Their
preregistered percentile intervals lie strictly below zero under every
available pooled and stratified scheme.  Thus the unfavorable \(P=15\)
direction is stable across these three finite references.  This table uses
the fixed Sobol files
`pde_QMC_P5_N16_M256_R128_s20260723_dt0p02_T8.npz` and
`pde_QMC_P15_N16_M256_R128_s20260723_dt0p02_T8.npz`; it must not be
conflated with the separate nested-hybrid \(P\) sequence below.

## Remaining blockers

### 1. No statistically resolved ordered width-then-depth target

The target order is \(n\to\infty\) at each fixed \(L\), then
\(L\to\infty\).  The held-out audit supplies only the L-shaped finite grid

\[
(256,32)\longrightarrow(512,32),
\qquad
(256,32)\longrightarrow(256,64).
\]

Both Cauchy gaps are below their two-reference 95% thresholds, but failure
to resolve a gap is not proof that it is zero.  There is no \((512,64)\)
point, second width step, second depth step, or fixed-\(L\) width
extrapolation.  The grid cannot decide whether the finite PDE gap shrinks,
persists, or changes sign in the ordered limit.

### 2. Hermite and cubature convergence are not cofinal

There is now one clean \(m=3\) basis step.  A hybrid rule uses an
order-three tensor Gauss--Hermite base cubature, which integrates the full
degree-two Hermite Gram exactly, and Sobol fast-row cubature.  It gives

| Comparison | Output | all-depth Gram | tangent kernel |
|---|---:|---:|---:|
| nested \(P=5,R=128\) vs \(P=15,R=128\) | \(1.124\times10^{-3}\) | \(2.761\times10^{-3}\) | \(2.070\times10^{-2}\) |
| \(P=15,R=128\) vs \(P=15,R=256\) | \(6.045\times10^{-4}\) | \(9.648\times10^{-4}\) | \(7.680\times10^{-3}\) |

The refined \(P=15,R=256\) rule is well conditioned
(\(\kappa_{\rm fast}=1.373\)) and has exact base-basis Gram to roundoff.
Nevertheless, its dense \(S=128\) Gram-increment gap is
\(9.223\times10^{-3}\), or \(1.460\%\) of its feature motion, versus
\(7.540\times10^{-3}\), or \(1.190\%\), for the matched hybrid \(P=5\)
run.  The first higher-order correction therefore moves away from the
finite dense reference on the primary metric.  This does not disprove
\(P\)-convergence, but it eliminates the favorable interpretation that the
observed \(P=5\) gap is already shrinking under the first valid basis
refinement.

The independently based Sobol-base \(P=15,M=256,R=128\) run gives almost
the same conclusion: its dense Gram-increment gap is
\(9.202\times10^{-3}\), and its full Gram surface differs from the hybrid
\(P=15,R=128\) result by only \(5.16\times10^{-4}\).  Thus the unfavorable
first \(P\)-step is not explained by the hybrid base rule alone.

Two cubic runs require different labels.  The old
\(P=35,M=64,R=64\) run is severely underresolved in both base and fast
cubature and must remain excluded.  A new hybrid complete-cubic run uses
exact order-four tensor base quadrature at \(M=256\), so its base Hermite
Gram is exact to \(3.8\times10^{-15}\).  Its \(R=128\) fast covariance,
however, has raw condition number \(6.20\) before whitening and has no
same-\(P\) \(R\)-refinement.  It gives

\[
\max_{t,s}\|\Delta G_{\rm inc}^{P=35}\|_F
=1.3731\times10^{-2}
\]

against the \(S=128\) dense reference, or \(2.192\%\) of its feature
motion, and differs from hybrid \(P=15,R=128\) by
\(6.14\times10^{-3}\) in Grams.  The direction continues away from the
finite dense mean, but the magnitude cannot be interpreted as a converged
cubic correction until the \(P=35\) fast cubature is refined.
No outcome-triggered \(R=256\) rerun was added after seeing this curve;
that preserves the audit protocol but leaves the cubic magnitude unresolved.

The independent GH3/QMC difference is also larger than the primary finite-
reference gap, although it compares unequal cubature resolutions.  A
credible arbitrary-accuracy claim requires same-\(P\) fast-cubature
convergence at \(P=35\) and a stable cofinal continuation.

### 3. The central homogenization theorem is still missing

At fixed finite \(L\), \(W_\ell^\top\beta_\ell\) has a centered column-
cavity innovation with \(O(1)\) coordinate variance.  The PDE keeps the
conditional/shared-transpose mean and assumes the centered innovations
cancel under the \(1/L\) residual accumulation.  The paired-\(W\) result is
strong numerical support, but trained global feedback can correlate
layers.  A proof needs trained iid-depth propagation of chaos or a
martingale/cavity bound uniform over the relevant training trajectory.

### 4. No uniform restart-neighborhood theorem

Serialization proves semigroup behavior for the same PDE state and
compiler.  It does not prove approximation of every nearby dense state or
every positive-time restart in a width-independent neighborhood.  That
robustness is needed to exclude all trajectory-specific coincidences in a
mathematical all-time theorem.

### 5. No outgoing residual certificate

The near-unit `projected_energy` only measures how much of the simulated
slow hidden field lies in the retained span.  It does not measure omitted
transpose innovations, all high Hermite modes, or high-to-low feedback.
It is not an a posteriori certificate for the dense-model error.

## Exact claim language

### Supported

> We directly simulated an explicit, autonomous, width-independent
> Hermite/isonormal operator-Galerkin Liouville PDE derived from the
> standard dense Euclidean-\(\mu\)P residual-tanh architecture.  Its
> finite-\(P\) flow has the correct projected Euclidean gradient structure,
> shared forward/transpose operator, PSD tangent kernel, and restart
> semigroup.  At \(P=5,N=16,M=256,R=128\), it predicts substantial nonlazy
> feature motion and reaches a genuine plateau.  Against a preregistered
> \(n=256,L=32,S=128\) ensemble through \(t=8\), its full Gram-increment
> surface differs by \(7.243\times10^{-3}\), or \(1.14\%\) of feature
> motion, and that finite-reference discrepancy is statistically resolved.
> A preregistered L-shaped audit found exact width and depth Cauchy gaps
> \(9.350\times10^{-3}\) and \(4.226\times10^{-3}\), neither statistically
> resolved.  The \(P=5\) gap is not resolved against pooled
> \(n=256,L=64,S=64\), but is narrowly resolved against the noisier
> \(n=512,L=32,S=16\) reference.  A fixed Sobol \(P=15\) curve is
> statistically farther from all three pooled references; a clean nested
> hybrid \(P=15\) refinement likewise does not reduce the finite-reference
> Gram discrepancy, and an underresolved complete-cubic stress run
> continues in the same unfavorable direction.  The \(1/L\)
> conditional-variance diagnostic remains encouraging.  Identifying the
> PDE with the ordered dense limit and proving arbitrary-accuracy/all-time
> convergence remain open.

### Not supported

Do not claim any of the following:

- “The PDE has been proven or numerically identified as the canonical
  ordered dense limit.”
- “The PDE and dense curves are indistinguishable” or “the discrepancy is
  below statistical noise.”
- “The PDE is converged to arbitrary accuracy in \(P,N,M,R\).”
- “Uniform accuracy on \([0,\infty)\) has been established.”
- “Near-unit projected energy certifies the omitted hierarchy.”
- “This simulates the earlier \(K/J/N\) response-word compiler.”
- “The evidence is overwhelming” without immediately quantifying the
  resolved \(1.14\%\) finite-reference discrepancy and the unresolved
  \(P\)/cubature and ordered-limit axes.

## Re-executed checks

The hostile audit directly reran or independently recomputed:

- 12 main PDE/reference unit tests: all passed;
- 4 tests from the independent implementation: all passed;
- the final 136-file SHA-256 manifest: every checksum passed;
- the release evidence verifier after the final freeze: passed for all 61
  complete NPZ archives and reproduced the four ordered-limit headline
  distances;
- same-shape, wrong-seed restart: correctly rejected with
  `restart static compiler/quadrature hash mismatch`;
- same-state changed-target RHS test: the velocity changed only through the
  new residual, with maximum componentwise linearity defect
  \(4.44\times10^{-16}\);
- the full \(S=128\) pooled and stratified 2000-replicate bootstrap in
  memory: reproduced the archived thresholds and tail probabilities
  exactly;
- both ordered-limit raw archives: independently reproduced their SHA-256
  hashes, seed sequences, means, SEMs, PSD checks, plateau diagnostics,
  exact Cauchy gaps, PDE gaps, maximum locations, and deterministic
  sensitivity-subblock gaps;
- six dispersed bootstrap replicates from each primary one-reference,
  two-reference Cauchy, and \(P=5\)-versus-\(P=15\) improvement
  distribution: reconstructed independently from the member trajectories
  and frozen RNG rules, agreeing with the archived values to at worst
  \(4.53\times10^{-16}\); all reported 95% quantiles and decisions were
  then recomputed from the archived 2,000-replicate arrays;
- the clean nested \(P=5\to15\) hybrid comparison and the \(P=15\)
  \(R=128\to256\) refinement directly from the raw arrays;
- the complete-cubic \(P=35\) archive's metadata, conditioning, identities,
  feature motion, and finite-reference curves;
- an independent dense-reference RK4 refinement on \(t\in[0,2]\) at
  \(n=64,L=32\): \(dt=.02\) versus \(.005\) differed by
  \(1.14\times10^{-7}\) in outputs, \(1.85\times10^{-7}\) in Grams, and
  \(5.91\times10^{-7}\) in the tangent kernel;
- primary curve metrics, feature motion, plateau drift, finite-width
  trend, and dense \(t=4\to8\) flatness directly from raw arrays.

## Final classification

\[
\boxed{
\begin{array}{l}
\textbf{PASS: }\text{a real finite neural PDE was simulated correctly;}\\
\textbf{PARTIAL: }\text{it tracks the observed dense curves closely and
globally through plateau;}\\
\textbf{OPEN: }\text{its convergence to the canonical ordered dense limit
and arbitrary-accuracy closure.}
\end{array}}
\]

This is the strongest honest result presently supported.  It is a major
advance over the finite-matrix surrogate, but not yet a numerical
resolution of the original PDE-existence conjecture.
