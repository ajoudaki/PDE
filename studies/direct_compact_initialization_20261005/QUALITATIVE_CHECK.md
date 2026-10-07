# Independent check of the qualitative direct-initialization result

2026-10-05. **PASS for the exact qualitative statement below.** The candidate's minor notation collision was corrected and the correction independently checked. This is an isolated mathematical check, not a promotion review, a machine verification, or a proof of the strict root-width target.

## Scope and verdict

I checked the frozen `RESULT.md` and its two complete supporting notes against the supplied maintained-book passages. The statement that passes is this: for fixed orthogonal normalized training inputs, fixed labels with

\[
Y=\|y\|_2/\sqrt m,\qquad
0<Y\le\gamma/(1000m),\qquad
\gamma=\mathbb E\tanh^2(\sqrt{\mathbb E\tanh^2G}\,G'),
\]

the specified two-hidden-layer tanh flows, with zero initial stored readout and mean-loss mobilities \((N,1,N)\), converge in probability to one deterministic predictor, uniformly on the whole input sphere and all physical times including the fitted endpoint. Consequently, independently initialized widths \(n\) and any deterministic \(q(n)\to\infty\) have prediction difference tending to zero in that topology. The endpoint error is defined as \(+\infty\) outside the two proved high-probability initialization events. Zero labels give the identically zero flow.

The logarithmic-width choice gives the stated storage and evaluation costs, but no effective accuracy-dependent width. Nothing checked here establishes error \(C/\sqrt n\), a root-width expectation-bias estimate, a numerical step count, or a bit-complexity bound.

The required canonical-notation skill was attempted at `/home/amir/.codex/skills/explain-with-canonical-notation/SKILL.md`; the read returned `Permission denied`. I used the assignment's explicit fallback, the user's notation instructions, and the complete `docs/notation.qmd`. I also read and applied `solve-math-rigorously`. No study README, study history, prior verdict, other study, archived book, experiment, or Git operation was used. The supporting notes' author-check sections were supplied as parts of the complete frozen inputs; their claimed checks were not treated as evidence in place of the derivations below.

## Independent reconstruction of the deterministic estimates

Write \(u_a=x_a/\sqrt d\), let \(H\) have the top training features as columns, and put \(\lambda=\gamma/(4m)\). For mean squared loss \(\rho^2=\|r\|_2^2/m\), differentiating with the displayed block mobilities gives exactly

\[
-\frac d{dt}\rho^2
=\|\dot A\|_F^2/N+\|\dot W\|_F^2+\|\dot w\|_2^2/N.
\]

The tangent matrix is positive semidefinite and contains \(H^TH/N\) as its readout block. While \(H^TH/(Nm)\succ\lambda I\), the residual equation \(\dot r=-(2/m)Kr\) gives \(-\rho'\ge2\lambda\rho\). Let \(v=-\rho'\). The speed in the displayed metric is \(\sqrt{2\rho v}\le v/\sqrt\lambda\). Integration therefore gives total parameter length at most \(Y/\sqrt\lambda\), readout RMS at most that value, and \(\int_0^\infty\rho\le Y/(2\lambda)\), provided the stopped inequalities persist. The zero-residual case is an equilibrium and causes no division problem.

On the stopped region \(\|W\|_{\rm op}<11\), the exact equations and \(\|r\|_1/m\le\rho\) give

\[
\|\dot A\|_F/\sqrt N\le22\rho Y/\sqrt\lambda,
\qquad
\|\dot W\|_F\le2\rho Y/\sqrt\lambda.
\]

Thus the combined hidden speed is at most \(2\sqrt{122}\rho Y/\sqrt\lambda\), and each hidden displacement is bounded by

\[
D=\sqrt{122}Y^2/\lambda^{3/2}.
\]

For any unit query, expand its top preactivation difference using the current first feature and the initial mixer. Since \(\|W(0)\|_{\rm op}\le10\), its RMS change is at most \(D+10D=11D\). The perturbation of \(H/\sqrt{Nm}\) is also at most \(11D\), by summing the squared column estimates. Its initial smallest singular value is at least \(\sqrt{2\lambda}\).

The numerical margin closes without importing the different label condition in `DENSE_BIAS_ROUTE.md`:

\[
Y/\lambda\le1/250,
\qquad
11D\le\frac{11\sqrt{122}}{62500}\sqrt\lambda
< (\sqrt2-1)\sqrt\lambda.
\]

Also \(\lambda\le1/4\) gives \(D\le\sqrt{122}/125000<1\). Both exit barriers are therefore strict. Smooth finite-dimensional continuation and the bounded parameter length give global existence and a parameter endpoint on the stated initial event.

For a passive query the differentiated top feature has RMS speed at most

\[
\|\dot W\|_F+11\|\dot A\|_F/\sqrt N
\le244\rho Y/\sqrt\lambda.
\]

The readout derivative has RMS at most \(2\rho\). Consequently

\[
|\partial_t f_N(t,u)|\le(2+244Y^2/\lambda)\rho(t).
\]

Its integrated tail is \((1+122Y^2/\lambda)(Y/\lambda)e^{-2\lambda t}\), which is at most the claimed \((2Y/\lambda)e^{-2\lambda t}\), since \(Y^2/\lambda\le1/250000\). This bounds total prediction variation after time \(t\). The physical residual-fitting time is exactly \((2m/\gamma)\log(Y/\eta)\).

Finally, the first matrix satisfies \(\|A(t)\|_{\rm op}/\sqrt N\le2\sqrt d+D\). Passing a query difference through the two Lipschitz activations and the readout yields the claimed constant

\[
L=11(Y/\sqrt\lambda)(2\sqrt d+1).
\]

These constants are independent of width and hold at the parameter endpoint.

## Initialization and population identification

The initialization event has probability tending to one. Orthogonality gives iid first-layer rows with independent standard Gaussian training projections. Their bounded first-feature products converge to \((\mathbb E\tanh^2G)I_m\). Conditional on the first layer, second preactivation rows are independent Gaussian tuples with that empirical covariance; each averaged bounded top-feature product has conditional variance at most \(1/N\). Coupling fixed-dimensional Gaussian tuples through the continuous positive semidefinite square root identifies the limiting conditional means as \(\gamma I_m\). Entrywise convergence is operator convergence for fixed \(m\). The independent matrix-net bound is

\[
\Pr(\|W(0)\|_{\rm op}>10)
\le2\exp\{N(2\log9-100/8)\}\to0,
\]

and \(\|A(0)\|_F^2/N\to d\). Independence was used only for initialized rows, not trained coordinates.

The supplied B.1 proof applies with both activations tanh, \(\sigma_1=\sigma_2=1\), zero stored readout, orthogonal inputs, and sum-loss multipliers \(\kappa_1=\kappa_2=\kappa_3=1/m\). These multipliers reproduce the stated mean-loss physical clock. B.1 explicitly establishes the finite continuous-flow limit before its separate GD argument; no GD step restriction is being silently imposed on this continuous-flow theorem.

The passive-panel extension is justified, rather than assumed as a broader published theorem. All first-matrix updates lie in the training span, so exactly

\[
A_N(t)u=A_N(0)u+
\sum_a(u^Tu_a)[A_N(t)u_a-A_N(0)u_a].
\]

For a fixed finite panel, adjoin its initial projections to the iid first-layer root tuple. III.F permits arbitrary correlations within this tuple, including singular covariances, while preserving independence from the initialized mixer. At a fixed transformed Euler mesh, each passive query is a finite program: the displayed reconstruction, bounded tanh maps, the initialized matrix action plus the finite rank-one update expansion, and the normalized readout pairing. A.1 covers the continuous at-most-linear transform \(J\). Both matrix orientations remain the actions of the same matrix.

The B.1 same-root estimate controls clock differences, mixer operator differences and readout RMS differences. Since \(J\) is Lipschitz in its clock, the reconstruction transfers these controls to passive first fields; bounded forward factors then control the passive prediction. Thus its finite and population mesh errors are \(O_T(\Delta)\). The finite-program limit is taken at fixed mesh, then the mesh is removed. This yields convergence uniformly on a fixed physical horizon for each finite passive panel to deterministic predictions. Enlarging the panel does not change old finite predictions, so their limits are consistent. This identifies a common deterministic predictor and does not infer it merely from agreement of two random copies.

## Sphere, all times, and nonlinear motion

Start on a countable dense sphere subset. Finite-panel convergence and the event probability tending to one transfer the width-independent Lipschitz inequality to its deterministic limit. One may first use rational times and then compact-time continuity. The unique spatial Lipschitz extension is consistent with every finite passive panel. A finite spatial net gives whole-sphere compact-time error at most the panel error plus \(2L\) times its radius. The net is fixed before width tends to infinity.

Likewise, transfer the two-finite-time tail inequality on a countable dense set of times and inputs, then use continuity. The deterministic limit is uniformly Cauchy as time tends to infinity and has the same sphere-uniform tail. On the good event,

\[
\sup_{t\in[0,\infty],u}|f_N(t,u)-f(t,u)|
\le\sup_{0\le t\le T,u}|f_N(t,u)-f(t,u)|
+\frac{4Y}{\lambda}e^{-2\lambda T}.
\]

Fix \(T\) from the tolerance, then pass to the width limit. Applying this statement to both diverging widths and using a union bound proves the comparison. Independence is allowed but not necessary for this implication. Assigning error \(+\infty\) outside the proved initialization events makes the endpoint statement precise without asserting an endpoint for every Gaussian realization.

The hidden-learning certificate also checks. With initial first features \(H_a=\tanh G_a\), second fields \(Z_a\), and \(S=(2/m)\sum_b y_b\tanh Z_b\), strong bounded-multiplier continuity gives the second-order middle increment

\[
B=\frac2m\sum_a y_a[S\tanh'(Z_a)]\otimes H_a.
\]

Orthogonality of the \(H_a\) makes
\(\|B\|_{\rm HS}^2=(4\mathbb E\tanh^2G/m^2)\sum_a y_a^2\mathbb E[(S\tanh'(Z_a))^2]>0\) for nonzero labels. The actual adjoint pairing with \(H_a\) is \((2y_a/m)\mathbb E[Z\tanh Z\tanh'Z]\ne0\), so the first hidden field also moves whenever \(y_a\ne0\). Multiplication by the positive first gate cannot annihilate that field. III.F.8–9 supply the Hilbert–Schmidt integral and bounded-multiplier facts. These are strong initial increments; no global Fréchet derivative of the tanh map on an \(L^2\) ball is needed. The certificate concerns nonzero motion near initialization, not a positive lower speed at all later times.

## Cost, ancillary claims, and issues

The construction explicitly stores \(q^2+dq+q\) moving scalar parameters and \(m(d+1)\) fixed data coordinates. Gaussian initialization uses \(q^2+dq\) draws. Dense forward, backward, and rank-one-update arithmetic gives \(O(m(q^2+dq))\) per full-batch vector-field evaluation and \(O(q^2+dq)\) per test query. Sequential sample processing needs only \(O(q)\) additional scratch beyond parameters and derivative accumulators. The absence of a retained initialized copy is compatible with the autonomous current-state ODE. The numerical integration and real-arithmetic qualifications are stated correctly.

I read the complete analytic note and checked the claims summarized in `RESULT.md`: the one-sample feature-clock factorization, scalar all-time contraction transfer with compatible decoder, positive cubic coefficient from conditional Gaussian regression, and explicit noncommuting two-sample direction example. Their missing high-order uniform approximation and decoder remain explicit missing premises. Those calculations are not needed for the qualitative theorem. The user's separate source-space lower bound was not supplied among the frozen inputs, so this report does not independently certify the last paragraph's interpretation of that lower bound.

No substantive correction is required for the scoped qualitative theorem. The original `RESULT.md` Section 3 used \(g\) both for the scalar gap \(\gamma/(4m)\) and, in \(\dot g(t,u)\), for the vector top feature. The corrected candidate consistently renames only the scalar to \(\lambda\). I reread the complete corrected candidate, checked all of Section 3 against the preceding reconstruction, and verified the exact change by reversing this renaming and its necessary TeX spacing in memory: the resulting full-file SHA-256 equals the original reviewed hash. No mathematical claim, constant, or vector feature changed. The supporting dense note's two malformed opening inline-math delimiters were subsequently corrected. I inspected that line and reversed precisely those two inserted backslashes in memory; the resulting full-file SHA-256 equals the original reviewed dense-note hash. Both cosmetic issues are resolved, with no change to the mathematical verdict.

## Frozen-input record

All three study inputs and the notation contract were read completely. The other scientific reads were exactly the assigned slices. Whole-file SHA-256 values are included to identify their containing editions; slice hashes below identify the actual supplied book inputs. All sources stayed frozen during the initial check. After its completion, the requested notation correction changed `RESULT.md`, and two opening-delimiter insertions changed `DENSE_BIAS_ROUTE.md`. Both exact changes were independently verified against their original reviewed hashes. Every other scientific input hash was reconfirmed unchanged after the notation correction; no later changes to those inputs were reported.

| Input | SHA-256 |
| --- | --- |
| `RESULT.md`, current corrected candidate | `c196f9a76dd860da68157a311a053e0536155635718c18e600ec391327485e51` |
| `RESULT.md`, original reviewed candidate | `503d6dfe90b2c5bf7945f4af9265273d33fbb04f4ab6fca4262360bef6188300` |
| `DENSE_BIAS_ROUTE.md`, current corrected input | `61eb2f976597c42f3c52b7dce8b4843e8d75a584787a5b3d691695792deac1f1` |
| `DENSE_BIAS_ROUTE.md`, original reviewed input | `d30faa3a9f8ae141eadd345d5f36255f79d300861bf07003282f6ee17e94fc76` |
| `ANALYTIC_ROUTE.md` | `b7c22af45155649b96af027eb5adbd7cd80b7ef382532870df82ab17b4263185` |
| `docs/notation.qmd` | `78e11eb3dafc5321a8a3923742993c0bad78df53b0e80b6319f16e48f0131023` |
| `docs/04-continuing-flows.qmd`, whole file | `78728dbbcc551392f7dd6cf7b91bad42324e5b540655d4242e830e9c38774a43` |
| Same, lines 7–648 | `2456110f33dd90d821875aff356f6a0c2b83f0f7649ef9034558d0c5f5cffff7` |
| `docs/02-gaussian-reuse.qmd`, whole file | `a0f8175c8cd17c4d93aeb7174f2babe83e0917c4ed0f33862c7c9a89685d0a92` |
| Same, lines 1803–1823 | `fdd2f7faeb9795fa0ad0d5506b70b80ae0deb7952cef2214fc15497d728b7c64` |
| `docs/12-three-sample-learning.qmd`, whole file | `06d6e45f1d7d6c280fb0c5dcac3303b49d56bec4d4a7df632cd73af5091d1d15` |
| Same, lines 316–994 | `b8ae36f4139244d17c8657a7d7b240fc3b4bedba9548c4a2453fe8c1b19cde1b` |
| `/etc/codex/skills/solve-math-rigorously/SKILL.md` | `9be5cb903f8957c5da9e2acfb1302eba4ba45e3ef9d45e30b9740ad7dbc8cff7` |

Slice hashes use the exact newline-preserving output of `sed -n 'a,bp'`. This report is the only written artifact of the check.
