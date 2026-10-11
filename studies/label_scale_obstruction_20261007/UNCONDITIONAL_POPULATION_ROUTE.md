# Correlated population construction: a uniform endpoint and the exact cap-removal gap

Status: new complete lemmas for a gradient-preserving capped construction and a quantitative finite-width transfer criterion; the uncut Gaussian theorem remains open. In particular, the tail estimate in (15) below is **not proved**. The result is not an unconditional fitting theorem. No experiment, external source, shared edit, or Git write was used.

This scoped attempt read the complete five assigned study inputs listed at the end, the maintained notation and index, and all of III.F.1–11 in `docs/12-three-sample-learning.qmd`. Required research, proof, and canonical-notation skills were applied. The author is the scoped `unconditional_population` agent. These new results have not received an independent check.

## 1. Exact model and a cutoff that preserves descent

Keep the study's notation: (X\in\mathbb R^{d\times m}) has unit columns (x_a),

\[
U=\tanh(AX),\quad z_a=Wu_a,\quad h_a=\tanh z_a,\quad
b_a=w\odot(1-h_a^2),\quad B_a=W^*b_a,
\]
\[
f_a=\langle w,h_a\rangle,\qquad r_a=f_a-y_a,\qquad
\mathcal L=\|r\|_2^2/m.
\tag{1}
\]

Population inner products are probability-normalized. At width (n), they are ordinary Euclidean inner products divided by (n), (W^*=W^\top), and (b\otimes u=bu^\top/n). The stored finite initialization is (A_{ij}\sim N(0,1)), (W_{ij}\sim N(0,1/n)), independently, and exactly (w=0). The parameter metric is the prescribed one with mobilities ((n,1,n)). In the maintained book's notation this is the unit-input convention obtained by replacing its normalized input (x_a/\sqrt d) with the present (x_a), and (A,W,w) are its first, second, and readout weights.

Let (\chi:[0,\infty)\to[0,1]) be smooth, equal to 1 on ([0,1]), and equal to 0 on ([2,\infty)). For a first-neuron backward tuple (B=(B_1,\ldots,B_m)\in\mathbb R^m), define

\[
\eta_R(B)=\chi(|B|/R),\qquad R\ge1.
\tag{2}
\]

The norm causes no nonsmoothness at zero because the function is constant near zero. There is a constant (C_\chi), independent of (R), such that

\[
|\eta_R(B)B|\le2R,\qquad
\operatorname{Lip}(B\mapsto\eta_R(B)B)\le C_\chi,
\]
\[
|(1-\eta_R(B))B|\le C_\chi(|B|-R)_+.
\tag{3}
\]

For the last inequality, use the mean-value estimate for (\chi) when (R<|B|<2R), and (|B|\le2(|B|-R)) when (|B|\ge2R).

The capped physical equations are

\[
\begin{aligned}
\dot A(\omega)&=-\frac2m\eta_R(B(\omega))
 \sum_a r_a\operatorname{sech}^2(A(\omega)\cdot x_a)B_a(\omega)x_a,\\
\dot W&=-\frac2m\sum_a r_a b_a\otimes u_a,\\
\dot w&=-\frac2m\sum_a r_a h_a.
\end{aligned}
\tag{4}
\]

The same scalar multiplies the whole first-row gradient. Consequently, if (G_A(\omega)=\nabla_A\mathcal L(\omega)) denotes the population first-layer gradient,

\[
\frac{d\mathcal L}{dt}
=-\int\eta_R(B)|G_A|^2
 -\|\nabla_W\mathcal L\|_{\rm HS}^2
 -\|\nabla_w\mathcal L\|_2^2\le0.
\tag{5}
\]

The finite formula uses its parameter metric and the normalized first-row sum. Equation (5) follows directly by substituting (4) into the scalar differential of the loss. It does not require (X^\top X) to be invertible. Clipping each (B_a) separately would not establish (5), since the first-layer squared-gradient expression contains cross-sample terms.

For scalar ascent of (g=m^{-1}\sum_a\sigma_af_a), use exactly the same first-row multiplier and replace (-2r_a) by (\sigma_a\in\{-1,1\}) in (4). This is a controlled auxiliary dynamics. The original network is recovered only when (\eta_R\equiv1); the cutoff is not silently included in the target theorem.

## 2. Complete fixed-cutoff population construction and identification

**Lemma 1.** For every fixed (R<\infty), every fixed finite dataset, and every fixed label vector, the capped scalar and physical equations have unique global strong population solutions on the common generated Gaussian spaces of maintained III.F. Their initialized finite-width counterparts converge on every fixed compact horizon in predictions and all contractions forming the readout-plus-middle kernel. The empirical coordinate laws of their backward tuples (B), including second moments, converge as well. The constants in this lemma may depend on (R).

Here is a direct proof with the relevant theorem hypotheses checked. Use the affine state space

\[
L^2(\Omega_1;\mathbb R^d)
\times[W_0+\mathcal S_2(L^2(\Omega_1),L^2(\Omega_2))]
\times L^2(\Omega_2).
\tag{6}
\]

The maintained construction gives a common bounded initialized action (W_0), with norm at most 10, and its actual Hilbert adjoint. Its first root is (A(0)\sim N(0,I_d)); the top readout root is zero. These roots are independent of the initialized matrix. A correlated or singular input tuple (A(0)\cdot x_a) is permitted by III.F.1 and III.F.5.

Temporarily replace (w) in (b_a) by a smooth bounded clip equal to (w) on ([-P,P]). Leave (w) in the prediction unchanged. On every bounded state ball, the forward fields and (b_a,B_a) are Lipschitz in the norm of (6), by bounded activations, bounded activation derivatives, the clipped-readout bound, and bounded operator norms. The map

\[
(p,B)\longmapsto\eta_R(B)
  \sum_a c_a\operatorname{sech}^2(p\cdot x_a)B_ax_a
\tag{7}
\]

is globally Lipschitz for bounded scalar coefficients (c_a): differentiating in (p) costs at most (C R), by (3), and differentiating in (B) costs a constant independent of (R). Scalar feedback through the residual is locally Lipschitz by Cauchy–Schwarz. Rank-one velocities are Lipschitz in Hilbert–Schmidt norm because

\[
\|b\otimes u-\widetilde b\otimes\widetilde u\|_{\rm HS}
\le\|b-\widetilde b\|_2\|u\|_2
  +\|\widetilde b\|_2\|u-\widetilde u\|_2.
\]

Picard contraction therefore gives a unique local strong solution on the open Hilbert state space. On a scalar horizon ([0,S]),

\[
\|w(s)\|_\infty\le s,\quad
\|W(s)-W_0\|_{\rm HS}\le s^2/2,\quad
\|A'(s)\|_{L^2(\mathbb R^d)}\le s(10+s^2/2).
\tag{8}
\]

For the last bound use unit inputs, Cauchy–Schwarz, (0\le\eta_R\le1), and (\|B_a\|_2\le s\|W\|_{\rm op}). Choose (P>S+1); its clip never acts. The bounds preclude finite-time norm escape, so scalar continuation is global.

For physical flow put (Y=\|y\|_2). While its readout clip is inactive, (5) gives (\|r\|_2\le Y). Hence on ([0,T]),

\[
\|w(t)\|_\infty\le P_T:=2TY/\sqrt m,
\qquad \|W(t)-W_0\|_{\rm HS}\le P_T^2/2.
\tag{9}
\]

The first-layer speed is bounded in (L^2) by the residual, operator, and readout bounds. Taking the auxiliary readout clip above (P_T+1) excludes its first activation and permits continuation through (T). This proves global physical existence. The chain rules and scalar Fréchet differentiability used in (5) are exactly III.F.9–10, with tanh's bounded first two derivatives; they assert neither an uncut (L^2) vector-field Lipschitz bound nor an unproved existence theorem.

For fixed (R), the field has a width-independent Lipschitz constant on these bounded state sets. Its exact Euler error on ([0,T]) is (C_{R,T}\Delta), since the one-step error is at most half the product of its speed and Lipschitz bounds times (\Delta^2), and the discrepancy recurrence is summed by Gronwall. Include a bounded readout clip above the preceding trajectory bound for the Euler comparison as well; a small-mesh first-exit argument supplies a common larger state ball.

Every fixed Euler transcript meets III.F.1–7: its coordinate instructions are globally (C^1) with bounded derivatives, including (7); it reuses only (W_0,W_0^*); and learned actions unroll into finitely many rank-one terms with causal scalar contractions. Arbitrary correlated roots are allowed. There are no inverse Grams or residual divisions. III.F first identifies the fixed transcript as width tends to infinity. Sending the proof mesh to zero using the common Euler estimate identifies the constructed strong flow. This limit order never applies the theorem to a transcript growing with width.

Observations (h_a,b_a,u_a,B_a) are Lipschitz on these bounds. Their fixed-time empirical laws and pairwise contractions therefore converge, with the same mesh argument. The norm of (\dot B_a=\dot W^*b_a+W^*\dot b_a) is bounded on each compact interval, uniformly in width and, in fact, independently of (R): (\dot A,U',W',w') have the cap-independent bounds above, and the readout is pointwise bounded. A finite time net gives uniformity in time. This also gives uniform convergence of any fixed-threshold backward tail norm, since (B\mapsto(|B|-K)_+) is 1-Lipschitz. This proves the lemma.

## 3. Simplex endpoint and capture margins uniform in the cutoff

**Lemma 2.** Let (m\ge3), and let (v_1,\ldots,v_m) be unit regular-simplex vertices. Set (x_a=\sigma_av_a), (y_a=a\sigma_a), with (a>0) and any sign vector (\sigma). Every capped population flow of Lemma 1 fits exponentially. Its scalar target is reached at a finite feature time, and its readout-plus-middle kernel at that endpoint has a positive lower bound independent of (R). There is one physical time (T), also independent of (R), at which every capped population snapshot meets a strict deterministic capture condition for the **uncut** finite-width flow.

This last assertion is about numerical snapshot inequalities; it is not yet a coupling of those snapshots to the uncut finite network.

Oddness absorbs signs exactly. The capped first-row multiplier is preserved: (b_a) and (B_a) are unchanged by (x_a\mapsto\sigma_ax_a), while (u_a,h_a), and the scalar coefficients acquire the matching signs. Thus it suffices to work with (x_a=v_a) and labels (a\mathbf1).

The initialized law and both capped fields respect every simplex sample permutation. The limit in Lemma 1 is deterministic, so population predictions are equal, (f_a=g), and the readout-plus-middle kernel is permutation invariant. This uses symmetry in law followed by deterministic identification; no finite Gaussian realization is assumed to be symmetric.

Put (\bar h=m^{-1}\sum_a h_a), (q_0=\|\bar h(0)\|_2^2), and (Q=\|w\|_2^2). Distinct nonantipodal unit inputs have linearly independent tanh ridge functions by the Vandermonde argument in `INTRINSIC_SYMMETRY_ROUTE.md`, Section 4. Hence the initialized first-feature Gram is positive definite, the initialized top preactivation tuple is a nonsingular Gaussian, and (q_0>0): (z\mapsto m^{-1}\sum_a\tanh z_a) is a nonzero continuous function under a full-support Gaussian law.

The capped scalar ascent still satisfies

\[
w'=\bar h,\qquad Q'=2g,\qquad
g'=\|\bar h\|_2^2+\|\nabla_Wg\|_{\rm HS}^2
 +\int\eta_R(B)|\nabla_Ag|^2\ge\|\bar h\|_2^2,
\qquad g^2\le Q\|\bar h\|_2^2.
\tag{10}
\]

At zero readout, hidden velocities vanish; thus (g=q_0s+o(s)) and (Q=q_0s^2+o(s^2)). On a positive interval for (g),

\[
(Q/g^2)'=-2(Qg'-g^2)/g^3\le0.
\]

Its initial limit is (1/q_0), so (g'\ge\|\bar h\|_2^2\ge q_0). This also excludes a later first zero of (g). Each cap therefore has a unique target time (s_R\le S_0:=a/q_0). With (M_0=10+S_0^2/2), the bounds (\|w\|_\infty\le S_0), (\|W\|_{\rm op}\le M_0) hold throughout all target paths.

The checked quantitative simplex lemma in `INTRINSIC_ENDPOINT_CHECK.md` applies to each constructed endpoint. Its full assumptions hold: linear first layer, bounded middle action, finite preactivations, permutation-invariant readout-plus-middle kernel, and mean prediction (g=a>0). In particular the endpoint least eigenvalue is at least

\[
\kappa_0:=\min\left\{
\frac{ma^2}{S_0^2},\quad
\frac{a^4\operatorname{sech}^4(\sqrt2S_0M_0/a)}
 {4S_0^2M_0^2(m-1)(1+2S_0)^2}
\right\}>0.
\tag{11}
\]

There is no hypothesis on first-layer support or response kernels here. Every constant in (11) is independent of the cap.

The cap-independent strong speed bounds in (8), the pointwise readout bound, and bounded activation derivatives give a common Lipschitz constant for the readout-plus-middle kernel along the scalar paths. The physical path is the time change (\dot s=2(a-g(s))): direct substitution into the capped equations and their uniqueness verify this identity. Therefore

\[
a-g(s(t))\le ae^{-2q_0t},\qquad
0\le s_R-s(t)\le[a-g(s(t))]/q_0.
\tag{12}
\]

The second estimate integrates (g'\ge q_0) between (s(t)) and (s_R). Thus the physical kernel is uniformly close to its endpoint kernel at sufficiently large fixed (T), and its residual tends uniformly to zero over the cap family.

For completeness, the uncut deterministic capture test needed here has width-independent constants. At a reference finite state with readout bound (S_0+1), operator bound (M_0+1), and readout-plus-middle kernel at least (\kappa_0 I/2), normalized feature differences in a parameter ball of radius (\rho) obey

\[
\|\Delta u_a\|_2\le\rho,\quad
\|\Delta h_a\|_2\le C\rho,\quad
\|\Delta b_a\|_2\le C\rho.
\]

The third bound writes (\Delta b_a=\Delta w(1-h_a^2)+w_*[(1-h_a^2)-(1-h_{*,a}^2)]), using the bounded reference readout. Tensor-product differences then give a ball radius (\rho_0>0), depending only on (m,S_0,M_0,\kappa_0), on which (K_{\rm R+W}\succeq\kappa_0 I/4). If the center residual norm is less than (\rho_0\sqrt{\kappa_0}/2), exact uncut gradient flow cannot exit this ball: while its kernel bound holds,

\[
\|\dot\theta\|_{\rm par}
\le-\frac2{\sqrt{\kappa_0}}\frac d{dt}\|r\|_2.
\]

The total remaining length is less than (\rho_0), and exact finite loss dissipation gives exponential fitting. Equations (11)–(12) choose a single (T) so that every cap snapshot obeys these inequalities with a strict margin. This proves Lemma 2.

## 4. A precise sufficient estimate for removing the cutoff

The next statement isolates the missing **dynamical** estimate, not a future full-support premise. Fix any finite physical horizon (T), fixed (X,y), and a high-probability initialization norm bound (\|W_0\|_{\rm op}\le10). Bars denote the exact finite capped solution at level (R), and unbarred fields the exact uncut solution from the same finite initialization. Both have the common bounds (9), because both dissipate the loss.

Define

\[
E_n(t)=\frac{\|U-\bar U\|_F^2}{n}
 +\|W-\bar W\|_F^2+\frac{\|w-\bar w\|_2^2}{n},
\qquad
\tau_{R,n}(t)=\left[\frac1n\sum_j
 (|\bar B_j(t)|-R)_+^2\right]^{1/2}.
\tag{13}
\]

Here (\bar B_j\in\mathbb R^m) is the backward tuple at first neuron (j), and all ordinary Frobenius/Euclidean normalizations are explicit. Constants below depend on (T,m,X,y,\chi), not on (n,R).

**Lemma 3.** There are (C_1,C_2<\infty), independent of (R\ge1), such that

\[
\sup_{t\le T}E_n(t)
\le C_1e^{C_2R}\int_0^T\tau_{R,n}(t)\,dt.
\tag{14}
\]

To prove it, let (\Gamma=X^\top X), (D_a=1-u_a^2). The uncut first-feature equation is

\[
\dot u_a=-\frac2mD_a\sum_b\Gamma_{ab}r_bD_bB_b.
\]

The capped version inserts (\eta_R(\bar B)) into the corresponding row expression. Forward differences and the pointwise readout bounds give

\[
\|\Delta H\|_F/\sqrt n+\|\Delta b\|_F/\sqrt n
 +\|\Delta B\|_F/\sqrt n+|\Delta r|
\le C\sqrt{E_n}.
\]

Split the first-feature difference into terms changing (r,B), terms changing gates with the capped reference (\bar B), and the removed reference velocity. The first group and the (W,w) equations contribute at most (CE_n) to (E_n'). Since each gate is Lipschitz in (u_a\in[-1,1]), the second group contributes at most

\[
\frac Cn\sum_j|U_j-\bar U_j|^2|\bar B_j|.
\]

On (|\bar B_j|\le2R) this is (CR E_n). On its complement use (|U_j-\bar U_j|\le2\sqrt m) and (|\bar B_j|\le2(|\bar B_j|-R)_+); Cauchy–Schwarz bounds this part by (C\tau_{R,n}). For the removed velocity, (3) gives norm at most (C\tau_{R,n}); its pairing with the feature difference is at most (C\sqrt{E_n}\tau_{R,n}). All states and hence (E_n) have a common bound on this fixed interval, so this term is also at most (C\tau_{R,n}). Thus

\[
E_n'\le C(1+R)E_n+C\tau_{R,n},\qquad E_n(0)=0.
\]

Gronwall proves (14). No tail assertion for the uncut trajectory, raw-preactivation comparison, or inverse input Gram is used.

Let (B^{(R)}(t)) denote the backward tuple of the constructed capped population flow. Lemma 1 identifies the fixed-(R) limit of the integral in (14). Consequently the explicit condition

\[
\liminf_{R\to\infty}e^{C_2R}
\int_0^T
\|(|B^{(R)}(t)|-R)_+\|_{L^2(\Omega_1)}\,dt=0
\tag{15}
\]

implies arbitrarily accurate comparison of the actual uncut finite-width flow to a fixed capped population snapshot, in the order: select a finite (R), then send width to infinity. A uniform sub-Gaussian tail for the cap family would imply (15). A bounded (L^2) norm does not imply it.

For the signed-simplex family, apply (15) only at the single (T) provided by Lemma 2. Predictions and (K_{\rm R+W}) are Lipschitz in the bounded-feature state distance in (13). Moreover, the accumulated residual clocks differ by at most (C_T\sup_{t\le T}\sqrt{E_n(t)}). Their exact bounds supply the required readout supremum and operator bounds at (T). Select a cap for which (14) is below the uniform strict capture margin, then send width to infinity at that fixed cap. The actual uncut finite network enters the deterministic capture ball with probability tending to one, and its own infinite-time limiting loss is exactly zero on that event.

This implication requires neither construction of the full uncut population trajectory nor a width-first interpretation of infinite-time fitting. It gives a particularly economical missing estimate: (15) at one finite horizon would already close the signed-simplex fitting theorem. It is still an unverified assumption for the canonical Gaussian model.

### A stronger tail premise also constructs the uncut strong path

The precise construction implication can also be proved. Suppose on each fixed horizon there are constants (C,c>0), independent of both cap (R\ge1) and threshold (K\ge1), such that

\[
\sup_{R\ge1}\sup_{t\le T}
\|(|B^{(R)}(t)|-K)_+\|_2\le Ce^{-cK^2}.
\tag{17}
\]

Then the common-space capped paths converge strongly to an uncut solution on that horizon, and their predictions and readout-plus-middle kernels converge uniformly. No additional response representation is necessary. Here is the argument, to distinguish what (17) actually supplies from an unsupported appeal to a tail bound.

Compare two capped paths at levels (R,Q), on the common generated spaces, using the same bounded-feature error as (13). Repeat the proof of Lemma 3 with an independent splitting threshold (K). Now subtract the two cutoff defects separately. Bounds (3) and (17) give

\[
\sup_{t\le T}E_{R,Q}(t)
\le C_Te^{C_TK}
 \bigl(e^{-cK^2}+e^{-cR^2}+e^{-cQ^2}\bigr).
\tag{18}
\]

First choose a fixed large (K), then let (R,Q\to\infty), then let (K\to\infty). This proves the uniform Cauchy property for (U,W,w). Their limits preserve the pointwise bounds on (U,w), and (B=W^*b) converges uniformly in (L^2) by the forward/backward difference estimates.

The raw first-layer paths are also strongly Cauchy. For their velocities, split a difference of 
\(\operatorname{sech}^2(A\cdot x_a)B_a=(1-u_a^2)B_a\)
into the difference in (B_a), the difference in the bounded gate multiplied by a reference (B_a), and the cutoff defect. Below threshold (K), the second term is at most (C K\|U^{(R)}-U^{(Q)}\|_2); above it, boundedness of both gates and (17) bound the term by (Ce^{-cK^2}). The cutoff defects tend to zero by (3) and (17). Thus the raw first-layer velocities are uniformly Cauchy in (L^2), after taking the same order of limits, and integrating gives convergence of (A) in (C([0,T];L^2)). Lipschitzness of tanh identifies the already obtained feature limit with (\tanh(AX)).

Every limiting velocity is the uncut velocity: the forward maps and learned-action integrals are strongly continuous, the previous gate-splitting argument handles the only unbounded multiplier, and the cutoff defects vanish. The resulting path is strongly (C^1), since the uncut vector field is continuous in this state space by the bounded-multiplier lemma III.F.9. Its original Gaussian roots and action are unchanged.

The same difference argument proves uniqueness against another strong solution on the horizon with the same initial state and the finite physical/scalar bounds: split the troublesome gate difference using the constructed solution as the reference. It inherits (17), by continuity of every fixed-threshold tail norm under strong (L^2) convergence. The comparison has no cutoff defects, so the bound is (C_Te^{C_TK-cK^2}), which tends to zero. Equality of (U,W,w) then gives equality of the raw first-layer velocities and roots, hence equality of (A).

Finally, (14) and fixed-cap width identification give convergence of the actual uncut finite-width (U,W,w) observations to this uncut population path, uniformly on the horizon, by first choosing a cap and then width. The raw first-layer comparison uses the preceding gate-splitting argument and the fixed-cap backward tail convergence. This proves the requested compact-time construction/identification **under (17)**. Neither (17) nor its weaker one-horizon consequence (15) has been established here for correlated Gaussian training.

## 5. Why the available Gaussian estimates do not prove (15)

The orthogonal proof removes the bottom gate exactly by 
\(\xi_a=\zeta(Ax_a)\), with (\zeta'=\cosh^2\). For correlated data, this introduces ratios

\[
\frac{\operatorname{sech}^2(Ax_b)}
 {\operatorname{sech}^2(Ax_a)},
\]

which are unbounded. The correlated capped equations instead have first-state Lipschitz constant of order (R), from (7).

Repeating the scaled Gaussian-matrix sensitivity argument of the complete `GAUSSIAN_NONORTHOGONAL_EXTENSION.md`, Section 3, now gives constants of the form

\[
C_{R,T}(L)\le C_T\exp\{C_T R+C_TL^2\},
\qquad L=\|W_0\|_{\rm op}.
\tag{16}
\]

Indeed the only new variational term is the derivative in (A) of (7), bounded by (CR); the derivative in (B) is cap-independent by (3). The direct forcing of one Gaussian matrix entry remains (O(n^{-1/2})), because (u,b) are pointwise bounded, while an arbitrary Frobenius perturbation has (O(1)) forcing. Gronwall gives (16). Integration by parts retains the learned-rank-one correction exactly as in that source. It therefore bounds the conditional mean of each capped (B_{a,j}) by (C_Te^{C_TR}), and Gaussian concentration gives a variance proxy of at most (C_Te^{C_TR}) after adjusting constants.

These are meaningful fixed-(R) bounds, but at a threshold proportional to (R) their estimates are ineffective: their mean bound and standard-deviation bound can grow exponentially in (R). Substituting them into the left side of (15) does not produce convergence to zero. This is a failure of this estimate, not evidence that the actual tails are large.

Nor can III.F's bounded common action repair the step: it supplies 
\(\|B^{(R)}\|_2\le\|W\|_{\rm op}\|b\|_2\), uniformly in (R), but no rate of tail decay. Even uniform square-integrability without an exponential rate would not imply (15), because its stability factor is (e^{C_2R}). Treating (W_0^*b) as independent Gaussian noise would discard its adaptive response and is invalid.

Thus this route establishes a complete gradient-preserving correlated cap family, deterministic compact-time identification for each fixed cap, cap-independent finite scalar endpoints and simplex capture margins, and the exact comparison inequality (14). The unresolved bridge is a cap-removal estimate such as (15), or another argument that replaces it. No unconditional uncut population construction, arbitrary-label theorem, or actual-Gaussian counterexample is claimed.

## Input provenance

The five assigned study inputs were read completely:

- `INTRINSIC_SYMMETRY_ROUTE.md`, SHA-256 `95db9ed7d65408d7b229cbc86f35ec944dc7f5f8b214e1c359c02f28c4193c18`.
- `INTRINSIC_ENDPOINT_ROUTE.md`, SHA-256 `b4c64992bf2fb556f28cb1f3b155833331c001e95a31468e3c499f6cfa659bc9`.
- `INTRINSIC_ENDPOINT_CHECK.md`, SHA-256 `77f5daf7e15a3dc2a5fc1a0c71ba8832d6bdc0e487760aa02e1e35b6bc76dfec`.
- `GAUSSIAN_POSITIVE_GEOMETRY.md`, SHA-256 `d220fba99906085e9770aceb33b939b5d0cfa2bb2bc005909f31fe2449afa574`.
- `GAUSSIAN_NONORTHOGONAL_EXTENSION.md`, SHA-256 `37a4f9fea1e64c2404c066358a82f2611f733c6496512d6179bef501424f9b11`.

Maintained scientific dependencies: `docs/index.qmd`, `docs/notation.qmd`, and complete III.F.1–11 of `docs/12-three-sample-learning.qmd` (whole-file SHA-256 `6811e9e8c0557416920c9a1bd8a144807c4f3a9d4aaac134259130c81c7f148d`). A keyword scan of the maintained continuation chapters located their explicit orthogonal/nonlinear restriction; no further theorem from those chapters is imported. No other study or archived book was read. Repository HEAD at the metadata check was `ef8362764b4eb8144d7af8d6f8db080fdaaf82ca`. The existing dirty worktree was preserved, and only this assigned file was written.
