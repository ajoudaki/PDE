# A reduced activation potential: exact adjoints, and the evaluator bottleneck

2026-10-08. Bounded theoretical route, followed by one polynomial repair. This agent's context was reused from the initialization-compiler review; this is **not a fresh independent attempt**. No other live route was read before freezing this candidate. No experiments, maintained-code changes, paper edits, or Git writes were performed.

The useful exact construction is an autonomous Galerkin network whose activation is the gradient of a scalar potential. Its Hessian supplies the backward action automatically. This eliminates the need to impose a separate forward/backward interpolation rule. It does **not yet eliminate the original-width nonlinear evaluator**: the exact potential is a sum over all neurons. A finite polynomial potential removes that evaluator with explicit costs, but its generic coefficient count can exceed the existing quadratic-in-rank inventory. The same-scope all-time approximation theorem remains open.

## 1. Contract and input scope

Keep the stated Gaussian nonlinear deep network: first weights have variance one, hidden weights variance \(1/n\), the stored readout starts exactly at zero, the loss is \(m^{-1}\sum_{a=1}^m(f_a-y_a)^2\), and the block mobilities are \((n,1,\ldots,1,n)\). There are \(m\) training and \(p\) additional passive inputs, \(N=m+p\), normalized as \(v_i=x_i/\sqrt d\). The activation class includes real analytic functions on the specified complex strip with bounded derivatives there but possibly unbounded values on the real line. Preserve the existing label/gap allowance, physical time, and all-time panel prediction criterion.

The input premise supplies finite source spaces, constructible by finite zero-time jets, of dimension at most \(R\). Source error and coefficient production are distinct issues. The existing source construction and corrected-selector runtime are conditional inputs; their comparison theorem does not automatically apply to a different optimizer.

Actual scientific sources used are `docs/index.qmd`, `docs/notation.qmd`, the assignment and own README, and the previously read complete §§1–5 and §9 of `initialization_panel_compression_20261008/PANEL_BOUND.md` plus §§1–5 of its `INITIALIZATION.md` (including the added scalar-evaluation convention). No additional prior-study results are imported. Required rigorous-math, research-contract, adversarial-audit, and canonical neural-notation instructions were read. The source files' SHA-256 values at this work are:

- `docs/index.qmd`: `f7a21b794e21f145ebad87fb1d7bde05f5f55e5877c92440109c1b22232b06de`.
- `docs/notation.qmd`: `78e11eb3dafc5321a8a3923742993c0bad78df53b0e80b6319f16e48f0131023`.
- `INITIALIZATION.md`: `a7dd5c9d94db826dece7df1de832139ad6a00a2d5053abefbbd1c34e8f4f5e05`.
- `PANEL_BOUND.md`: `9622e6938eb19eb31965f004fab9b3f20b3ce544e135eb9f2fd72631a86051d9`.

The calculations below are author-derived and checked algebraically in this note; they have not received an independent review or promotion.

## 2. One scalar potential determines both nonlinear directions

For layer \(j\), let \(E_j\in\mathbb R^{n\times r_j}\), \(r_j\le R\), be a basis normalized by
\[
E_j^\top E_j/n=I_{r_j},\qquad
\Pi_j=E_jE_j^\top/n.
\]
Thus \(E_jx\) has dense RMS norm \(\|x\|_2\), and \(\Pi_j\) is the ordinary orthogonal projection onto the source space. The basis is fixed after initialization compilation. Temporarily retaining its \(nr_j\) entries is explicitly charged.

Define a primitive \(F_j(s)=\int_0^s\phi_j(u)\,du\), and the scalar reduced potential
\[
\Psi_j(x)=\frac1n\sum_{i=1}^n F_j((E_jx)_i),\qquad x\in\mathbb R^{r_j}.
\tag{1}
\]
Differentiating the finite sum gives
\[
\nabla\Psi_j(x)=\frac1nE_j^\top\phi_j(E_jx),\qquad
\nabla^2\Psi_j(x)=\frac1nE_j^\top
 \operatorname{diag}(\phi_j'(E_jx))E_j.
\tag{2}
\]
The Hessian is symmetric even when \(\phi_j\) is not monotone. No convexity assumption is made. If \(|\phi_j'|\le s\) on the real axis, its operator norm is at most \(s\), independently of width or basis coherence.

Use moving parameters
\[
A\in\mathbb R^{r_1\times d},\quad
B^{(j)}\in\mathbb R^{r_j\times r_{j-1}}\ (2\le j\le L),\quad
w\in\mathbb R^{r_L}.
\]
The reduced forward pass, residual, and loss are
\[
\begin{aligned}
z_i^{(1)}&=Av_i,&
z_i^{(j)}&=B^{(j)}h_i^{(j-1)},&
h_i^{(j)}&=\nabla\Psi_j(z_i^{(j)}),\\
f_i&=w^\top h_i^{(L)},&r_a&=f_a-y_a,&
\mathcal L&=\frac1m\sum_{a=1}^m r_a^2.
\end{aligned}
\tag{3}
\]
All variables in (3) belong to this reduced network. Its backward derivatives are
\[
\delta_a^{(L)}=\nabla^2\Psi_L(z_a^{(L)})w,\qquad
\delta_a^{(j)}=\nabla^2\Psi_j(z_a^{(j)})
 B^{(j+1)\top}\delta_a^{(j+1)}.
\tag{4}
\]
Ordinary Euclidean gradient flow of the stated loss is exactly
\[
\begin{aligned}
\dot A&=-\frac2m\sum_a r_a\delta_a^{(1)}v_a^\top,\\
\dot B^{(j)}&=-\frac2m\sum_a r_a\delta_a^{(j)}h_a^{(j-1)\top},\\
\dot w&=-\frac2m\sum_a r_a h_a^{(L)}.
\end{aligned}
\tag{5}
\]
Only training inputs enter these sums. Every backward direction is the actual derivative of the same forward map, rather than a separately fitted response. Equations (1)–(5) are autonomous and locally uniquely restartable wherever the activation is analytic. They contain no clock or prescribed target curve.

The initialization is
\[
A(0)=E_1^\top W_0^{(1)}/n,\quad
B^{(j)}(0)=E_j^\top W_0^{(j)}E_{j-1}/n,\quad w(0)=0.
\tag{6}
\]
An exact panel-span input projection may replace \(d\) by \(k\le\min(d,N)\), with its separately stored \(d\)-by-\(k\) input map, as in the already checked panel lemma.

There is no physical-time rescaling in (5). Indeed first-weight and readout lifts \(E_1A\) and \(E_Lw\) have squared parameter norms \(n\|A\|_F^2\) and \(n\|w\|_2^2\). A hidden increment lifted as \(E_j\Delta B^{(j)}E_{j-1}^\top/n\) has squared Frobenius norm \(\|\Delta B^{(j)}\|_F^2\). The canonical dense mobilities cancel exactly these factors.

## 3. Exact capture under an exact source-space hypothesis

Here is a precise conditional identity, not a claim that the finite analytic approximants have zero error. Suppose on an interval every dense panel feature \(h_i^{(j)}\) and training backward response \(\delta_a^{(j)}\) belongs to the corresponding source space. Suppose also that the spaces contain all required initialized actions \(W_0^{(j)}h_i^{(j-1)}\), \(W_0^{(j+1)\top}\delta_a^{(j+1)}\), and first initialized panel preactivations. Then the reduced system (3)–(6) reproduces the dense panel predictions on that interval.

To verify this, the dense learned hidden increment is
\[
W^{(j)}(t)-W_0^{(j)}
=-\frac2{mn}\sum_a\int_0^t
 r_a(s)\delta_a^{(j)}(s)h_a^{(j-1)}(s)^\top\,ds.
\tag{7}
\]
Under the hypothesis each outer factor lies in the relevant space. Therefore (7) has the lifted form \(E_j\Delta B^{(j)}E_{j-1}^\top/n\); the first/readout increments similarly lie in their prescribed spaces. The paired initialized-action hypotheses give the correct two directions of the fixed part. Forward projection then gives (3), and projected multiplication by \(\phi_j'\) gives the Hessian in (2), hence (4). Projecting the dense update gives exactly (5), with initialization (6). Local uniqueness identifies the trajectories, and continuation proves equality throughout the common interval.

One must keep the fixed initialized matrix bulk in this reasoning: the dense matrix need not equal \(E_jB^{(j)}E_{j-1}^\top/n\). Its omitted fixed part is invisible on the stated paired sources. The exact theorem does not assert equality after arbitrary dense restarts outside that source-compatible set.

With approximate source spaces, this proof instead generates projection defects. Bounding those defects and their propagation for the full label allowance is a required theorem. The existing corrected-selector optimizer has a different activation and an additional readout/residual mechanism; its all-time certificate cannot simply be attached to (5).

## 4. Why the potential is not yet a compressed evaluator

Equation (1) contains all \(n\) neuron rows. Directly evaluating its gradient or a Hessian-vector product costs \(O(nr_j)\) arithmetic plus \(n\) scalar activation/derivative evaluations, and requires \(nr_j\) retained basis entries. Giving this function a name does not remove those costs.

Even rank and exact inner products fail to specify it. Take \(n=4\), \(r=2\), and two normalized bases with columns \((\mathbf1,u)\), where respectively
\[
u=(-1,-1,1,1)^\top,\qquad
u=(-\sqrt2,0,0,\sqrt2)^\top.
\]
Both satisfy \(E^\top E/4=I_2\). For the admissible activation \(\phi(s)=s+\epsilon\sin s\), \(\epsilon>0\), the potential along \(x=(0,t)\) is respectively
\[
\Psi_1(0,t)=t^2/2+\epsilon(1-\cos t),\qquad
\Psi_2(0,t)=t^2/2+\frac\epsilon2(1-\cos(\sqrt2t)).
\tag{8}
\]
Their gradients already differ at cubic order: the second coordinate is \((1+\epsilon)t-\epsilon t^3/6+O(t^5)\) versus \((1+\epsilon)t-\epsilon t^3/3+O(t^5)\). Thus Gram-preserving spectral coordinates do not encode the reduced nonlinear law. This example is an algebraic obstruction to inference from rank/Gram data alone, not a counterexample to Gaussian-network compression. The activation is entire, has bounded derivatives on every fixed horizontal strip, and has unbounded real values, so the issue is not caused by specializing to bounded activations.

Replacing the sum in (1) by a small weighted set of neuron rows would give a useful potential cubature. But this is nonlinear coordinate quadrature/selection under another description. It would not answer the requested elimination of that mechanism.

## 5. Focused repair: a finite polynomial potential

Suppose a specified admissible coefficient domain ensures \(|(E_jx)_i|\le Z_j\). Let a scalar polynomial \(a_j\) of degree \(q_j\) satisfy
\[
\sup_{|s|\le Z_j}|a_j(s)-\phi_j(s)|\le\eta_0,
\qquad
\sup_{|s|\le Z_j}|a_j'(s)-\phi_j'(s)|\le\eta_1.
\tag{9}
\]
Let \(p_j'=a_j\), and replace \(\Psi_j\) by
\[
P_j(x)=\frac1n\sum_i p_j((E_jx)_i).
\tag{10}
\]
The same formula is now compiled as a multivariate polynomial and the basis is discarded. The forward/backward equations remain (3)–(5), with \(P_j\) replacing \(\Psi_j\). They are finite autonomous equations and still exactly differentiate one common loss.

The approximation bounds are dimension-free once (9) holds:
\[
\|\nabla P_j(x)-\nabla\Psi_j(x)\|_2\le\eta_0,
\qquad
\|\nabla^2P_j(x)-\nabla^2\Psi_j(x)\|_{\rm op}\le\eta_1.
\tag{11}
\]
For the first inequality, \(\|E_j^\top/n\|_{\rm op}=1/\sqrt n\) and the coordinate error vector has Euclidean norm at most \(\sqrt n\eta_0\). For the second, insert the diagonal derivative error between the normalized basis and its transpose, whose resulting operator norm is at most \(\eta_1\).

If \(p_j(s)=\sum_{k=0}^{q_j+1}c_{j,k}s^k\), the exact stored coefficient for a multi-index \(\alpha\in\mathbb N^{r_j}\), \(|\alpha|=k\), is
\[
c_{j,k}\frac{k!}{\alpha!}\frac1n
\sum_{i=1}^n\prod_{b=1}^{r_j}(E_j)_{ib}^{\alpha_b}.
\tag{12}
\]
These are initialization-computable moments of a basis already produced by the finite-jet compiler. No future observations enter. The activation-polynomial construction and its derivative backend must also be charged; (9) is not an uncounted function oracle.

The generic monomial inventory is
\[
D_j=\binom{r_j+q_j+1}{q_j+1}.
\tag{13}
\]
A sufficient retained inventory is the moving \(dr_1+\sum_{j=2}^Lr_jr_{j-1}+r_L\) parameters, their initialized coefficient data, \(\sum_jD_j\) potential coefficients, the input/output data, and ordinary feature/response workspace. No \(nR\) lifting basis remains. Straightforward gradient and Hessian-vector evaluation costs \(O(r_jD_j)\) per layer/input; matrix actions additionally cost \(O(R^2)\). Straightforward moment assembly costs at most \(O(\sum_jnr_jD_j)\), in addition to source-basis construction and scalar polynomial production. These are sufficient costs, not optimal circuit bounds.

For fixed \(q_j\ge2\), (13) can already grow faster than \(R^2\); increasing approximation degree is worse. The moment structure might permit a shorter circuit, but its existence and initialization construction would be an additional theorem. Low temporal response rank alone does not provide it.

Nor does the inherited strip give a width-free polynomial domain automatically. Set \(\Lambda_j=\max_i\|(E_j)_{i,:}\|_2\). A coefficient ball \(\|x\|_2\le B_j\) only guarantees \(Z_j\le\Lambda_jB_j\), and normalization alone allows \(\Lambda_j=\sqrt n\). The complex coefficient ball guaranteed to stay in the activation strip has imaginary radius at most \(a/\Lambda_j\). One also has the third-potential-derivative bound \(\|D^3\Psi_j\|\le t_2\Lambda_j\) from the same normalized-basis estimate. Thus neither multivariate analytic radius nor higher derivative control may silently be declared width-independent. Reachable-state structure could improve these estimates; such improvement is not proved here.

## 6. Precise remaining comparison theorem

The polynomial model is locally well posed because its vector field is polynomial. This alone proves neither bounded global existence nor fitting. Its global polynomial extrapolation can differ substantially from the original activation; an invariant admissible domain is a necessary part of an accuracy theorem.

A fully specified conditional comparison is available. Let \(F_\Psi,F_P\) be the parameter vector fields of (5), using \(\Psi\) and \(P\). Suppose both trajectories remain in a domain on \([0,T]\) on which \(F_\Psi\) is \(C\)-Lipschitz and \(\|F_P-F_\Psi\|\le\delta\), and suppose their initial parameter states agree. Direct integration of the difference gives
\[
\|\theta_P(t)-\theta_\Psi(t)\|
\le\delta\frac{e^{Ct}-1}{C},
\tag{14}
\]
with the quotient interpreted as \(t\) if \(C=0\). If the output maps on that domain have state Lipschitz constant \(B_f\) and same-state difference at most \(\delta_f\), their panel discrepancy on \([0,T]\) is at most
\[
\delta_f+B_f\delta(e^{CT}-1)/C.
\tag{15}
\]
The constants must come from the stated parameter domain, activation derivatives, and basis/moment bounds; they are not assumed independent of width. Bounds (11), propagated through the finite layer recursions, produce \(\delta,\delta_f\) when those quantities are controlled.

To compare to the dense network, add a proved dense-to-Galerkin source-defect bound to (15). To extend to all times, one sufficient additional hypothesis is a fitted prediction-tail bound for both the dense and polynomial models: \(\sup_{t\ge T}\max_i|f(t,v_i)-f(T,v_i)|\le B e^{-\sigma T}\), with explicit model-dependent \(B,\sigma>0\). The all-time error is then at most the compact-time error plus the two tail bounds. This follows by the triangle inequality at time \(T\); it is not supplied merely by local polynomial analyticity or loss dissipation.

Proving these domain/source/fitting properties under the **existing full label allowance**, without importing the coordinate selector's special corrected-readout argument unchanged, is an unresolved bridge. Tightening the labels or freezing the features would change the task and is not proposed as a solution here.

## 7. Claim status and stopping point

| Claim | Status and decisive qualification |
|---|---|
| A scalar projected potential gives exact adjoint-consistent nonlinear forward/backward maps | Exact identities (1)–(5) |
| Exact source-space closure reproduces dense panel flow in physical time | Conditional exact theorem proved in §3 |
| A finite polynomial potential gives an autonomous evaluator without retained dense bases | Explicit construction (9)–(13); all coefficient costs charged |
| Rank and Gram data alone determine that evaluator | False, by (8) |
| The potential can always be evaluated with \(O(R^2)\) or smaller retained data under the source hypothesis | Open; generic polynomial inventory does not establish it |
| This model has the existing full-allowance all-time dense accuracy and a better logarithmic power | Open; requires both a compact evaluator and the comparison/fitting bridge |

The highest-leverage next theorem for this route is a uniform compact representation of \(\Psi_j\), its gradient, and Hessian-vector action on the actually reachable reduced domain, with coefficients computable at initialization and size at most \(O(R^2)\). A proof about temporal output approximation alone does not imply that state-dependent nonlinear representation. Until it is supplied, the potential formulation is a consistent intrinsic dynamical skeleton and an explicit location of the remaining information, not a cheaper replacement for selection.
