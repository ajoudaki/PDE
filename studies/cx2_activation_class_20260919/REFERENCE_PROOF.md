# Fitted reference: signed symmetry, radial convexity, and continuation

Status: internally derived bounded-reference theorem and conditional unbounded-reference interface; not a complete theorem for every unbounded activation. No experiments or maintained-file changes were made.

The primary reference is the two-anchor, opposite-label dataset. A separate equal-label result is recorded below. The same nonaffine activation is used in both hidden layers throughout. The main new exact point is that the norm of the readout is convex in feature time. Consequently the signed feature norm cannot fall below its initial value along a strong symmetric reference flow. This gives a fitting rate without assuming that an individual hidden feature or kernel entry is monotone.

Scientific inputs used: `docs/NOTATION.md`; complete A.1–A.4, B.1, C.1–C.3 (including the weighted-loss correction) of `docs/global_nonlinear.md`; and Sections 1–4 of `docs/finite_dynamics.md`. No other study or proof route was consulted. The `solve-math-rigorously` and `investigate-conjectures` skills and their research-contract, adversarial-audit, and proof-search references were read.

## 1. Exact reference and its normalization

Let (u_a=x_a/\sqrt d\) be the actual input vector entering the first linear map. Take two perpendicular anchors of a common positive squared norm (g):

\[
u_1^Tu_2=0,\qquad |u_1|^2=|u_2|^2=g>0,
\qquad y_1=1,\quad y_2=-1.
\]

For normalized anchors (x_a=\sqrt d\,e_a), (g=1). If the phrase “anchors (e_a)” means the literal raw inputs (x_a=e_a), then (g=1/d). The proofs below keep this factor and do not silently renormalize the model.

Write (W\in L^2(\Omega_1;\mathbb R^d)) for a full first-layer row, (A=A_0+B:\mathcal H_1\to\mathcal H_2) for the middle action with (B) Hilbert–Schmidt, and (c\in\mathcal H_2) for the stored population readout. Here \(\mathcal H_\ell=L^2(\Omega_\ell)\), and (A^*) is the actual adjoint of (A). Set

\[
w_a=W\cdot u_a,\quad p_a=\phi(w_a),\quad z_a=Ap_a,
\quad H_a=\phi(z_a),\quad f_a=E_2[cH_a],
\quad \mathcal L=\tfrac12[(f_1-1)^2+(f_2+1)^2].
\tag{1}
\]

Initialization is exactly the stored-variance convention \((1,1/n,1/n^2)\), with mobilities \((n,1,n)\). Thus (W_0\) is a standard Gaussian row, (A_0) is the generated Gaussian action, and (c_0=0). In particular (w_{1,0},w_{2,0}\) are independent (N(0,g)). No bottom-row coordinates have been discarded: the orthogonal complement of \(\operatorname{span}\{u_1,u_2\}\) remains in (W) and is constant under training.

Assume \(\phi\in C^{1,1}(\mathbb R)\), \(D=\|\phi'\|_\infty<\infty\), and \(L=\operatorname{Lip}(\phi')<\infty\), with \(\phi\) nonaffine. The activation may be unbounded, nonodd, nonmonotone, or flat on intervals. Let

\[
h(W,A)=\tfrac12(H_1-H_2),\qquad b=E_2[ch].
\tag{2}
\]

The raw hidden tangent metric is

\[
\|(V,C)\|_{\rm hid}^2=E_1|V|^2+\|C\|_{\rm HS}^2.
\tag{3}
\]

Together with \(\|c\|_2^2\), this is the limiting metric of the stated finite mobilities. It is not a metric in which sample projections are independent coordinates without their factor (g).

## 2. Opposite-label symmetry does not require oddness

Let (R\) be the orthogonal involution of \(\mathbb R^d\) exchanging (u_1,u_2) and fixing their perpendicular complement. On raw states consider

\[
\mathscr Q(W,A,c)=(WR,A,-c).
\tag{4}
\]

It sends \((f_1,f_2)\) to \((-f_2,-f_1)\), preserves (1), and is an isometry of the raw metric. Hence its derivative intertwines the raw gradient vector field: this follows by differentiating \(\mathcal L\circ\mathscr Q=\mathcal L\) against each raw tangent vector and using orthogonality of \(\mathscr Q\). Both finite GF and simultaneous raw GD are therefore equivariant under (4).

The complete initialized finite arrays have invariant law under (4): the standard Gaussian first rows are invariant under (R), the middle matrix is unchanged, and the independent centered Gaussian readout is invariant under sign reversal. The fixed-program laws in A.1 retain this symmetry. Therefore deterministic canonical population predictions obey

\[
f_1=-f_2=b.
\tag{5}
\]

One can equivalently obtain (5) by induction in the population Euler programs on their common generated spaces and then pass to any unique strong limit. This argument uses the same array in both orientations, not an independently resampled reverse map. Beyond the interval of known uniqueness, symmetry requires either that same equivariant construction or uniqueness of the continued flow; it is not silently assumed for an arbitrary hypothetical branch.

By (5), \(r_a=y_a(b-1)\) and \(\mathcal L=(1-b)^2\). The *full* raw gradient then satisfies

\[
-\nabla\mathcal L=2(1-b)\nabla b,
\tag{6}
\]

because \(\nabla\mathcal L=\sum_a r_a\nabla f_a\) and \(\nabla b=\tfrac12(\nabla f_1-\nabla f_2)\). Thus (6) is an identity of full-row, middle-action, and readout vector fields, not only a derivative restricted to a symmetry submanifold.

## 3. A radial coercivity lemma for feature ascent

For a hidden tangent \((V,C)\), the strong directional derivative of (h) is the bounded linear map

\[
\mathcal J_{W,A}(V,C)
=\tfrac12\sum_{a=1}^2 y_a\phi'(z_a)
\left[Cp_a+A\{\phi'(w_a)(V\cdot u_a)\}\right].
\tag{7}
\]

Its adjoint applied to (c) has blocks

\[
(\mathcal J^*c)_W
=\tfrac12\sum_a y_a\phi'(w_a)A^*[c\phi'(z_a)]\,u_a,
\qquad
(\mathcal J^*c)_A
=\tfrac12\sum_a y_a[c\phi'(z_a)]\otimes p_a.
\tag{8}
\]

Each term is well defined: activation derivatives are bounded, (A) and (A^*) are bounded, (p_a,c\) are in (L^2), and a rank-one operator has Hilbert–Schmidt norm \(\|u\|_2\|v\|_2\). Formula (8) follows by moving the actual (A) across the same-layer pairing. Formula (7) is a strong chain rule along differentiable curves; no Fréchet differentiability of the activation map on all of (L^2) is claimed. A.4 justifies both this chain rule and the scalar Fréchet gradient of (b).

On any strong feature-time interval let

\[
c_s=h,\qquad (W,A)_s=\mathcal J^*c,
\qquad c(0)=0.
\tag{9}
\]

The chain rule gives

\[
c_{ss}=h_s=\mathcal J\mathcal J^*c,
\quad b=\langle c,c_s\rangle,
\quad b_s=\|h\|_2^2+\|\mathcal J^*c\|_{\rm hid}^2.
\tag{10}
\]

These are exact identities for (C^{1,1}) activations; they do not differentiate \(\phi'\).

**Lemma.** If \(q_0=\|h(0)\|_2^2>0\), every such strong flow satisfies

\[
\|h(s)\|_2^2\ge q_0,\qquad b_s(s)\ge q_0,
\qquad b(s)\ge q_0s.
\tag{11}
\]

**Proof.** Write \(N(s)=\|c(s)\|_2\). Near zero, \(c(s)=s h(0)+o_{L^2}(s)\), so (c(s)\ne0). Also \((N^2)'=2b\) and \(b_s\ge0\), with (b(0)=0); once (N) is positive it cannot return to zero. Hence for every (s>0) in the interval,

\[
N'=b/N,
\qquad
N''=\frac{\|h\|_2^2+\|\mathcal J^*c\|_{\rm hid}^2}{N}
-\frac{\langle c,h\rangle^2}{N^3}\ge0.
\tag{12}
\]

The last inequality is Cauchy–Schwarz. From (c(s)/s\to h(0)) and (h(s)\to h(0)), \(N'(s)\to\sqrt{q_0}\) as (s\downarrow0\). Convexity gives \(N'\ge\sqrt{q_0}\) and (N\ge s\sqrt{q_0}\). Since \(N'\le\|h\|_2\), both the first inequality of (11) and \(b=NN'\ge q_0s\) follow. Equation (10) gives the remaining inequality. \(\square\)

This lemma concerns the norm of the *signed mean* (h). It does not assert that \(\|H_a(s)\|_2\), individual kernel entries, or individual feature displacements are monotone.

## 4. Positivity of the initial signed feature

Let \(G\sim N(0,g)\), \(\mu=E\phi(G)\), and \(v=\operatorname{Var}(\phi(G))\). Continuity and nonconstancy of \(\phi\), together with the full support of (G), give (v>0). The first feature Gram is

\[
Q=vI_2+\mu^2\mathbf1\mathbf1^T\succ0.
\tag{13}
\]

The initialized upper preactivation pair \(Y=(Y_1,Y_2)=(A_0p_{1,0},A_0p_{2,0})\) is centered Gaussian with covariance (Q), by the initial independent forward Gaussian call. It has a strictly positive density on \(\mathbb R^2\). Consequently

\[
q_0=\tfrac14 E[(\phi(Y_1)-\phi(Y_2))^2]>0.
\tag{14}
\]

Indeed vanishing of (14), continuity, and full support would imply \(\phi(s)=\phi(t)\) for all (s,t), contradicting nonconstancy. Linear growth of \(\phi\) supplies the required Gaussian second moments. This establishes the actual initialization constant, without an arbitrary lower bound uniform over the activation class.

## 5. Fitting on every interval of strong continuation

Suppose the canonical symmetric physical flow exists strongly through a finite (T). Its scalar prediction derivative, from (6), is

\[
b_t=2(1-b)K,
\qquad K=\|h\|_2^2+\|\mathcal J^*c\|_{\rm hid}^2.
\tag{15}
\]

On a compact strong interval (K) is continuous and finite. Solving this scalar equation gives

\[
1-b(t)=\exp\left(-2\int_0^tK(u)\,du\right)>0.
\tag{16}
\]

Therefore (s(t)=\int_0^t2(1-b(u))\,du\) is strictly increasing, and its change of variables gives (9). The radial lemma applies on its entire image and yields

\[
\mathcal L(t)\le e^{-4q_0t}.
\tag{17}
\]

For the explicit activation-dependent horizon

\[
T_\phi=\frac{\log 8}{4q_0},
\tag{18}
\]

strong continuation through (T_\phi) implies \(\mathcal L(T_\phi)\le1/8<1/4\). The conclusion is not obtained by assuming a lower bound on the trained kernel: (11) proves the necessary lower bound from the exact dynamics.

**Unconditional bounded subclass.** If \(\phi\) is also bounded, B.1 supplies a unique global strong flow with the actual middle action and adjoint. Its summed-loss statement converts to the mean loss by the factor (1/2) in time. For (g\ne1), write the first raw anchor coordinate as \(v_a=w_a/\sqrt g\) and apply B.1 with first activation \(v\mapsto\phi(\sqrt g\,v)\); this is exactly the original same-activation network in raw coordinates, not a change of its dynamics. Its first-layer derivative remains bounded and Lipschitz. All B.1 hypotheses are met, including the vanishing stored Gaussian readout. Thus (17)–(18) are a complete fitted-reference result for every bounded, nonaffine activation in the stated (C^{1,1}) class.

**Unbounded class.** C.1 supplies the canonical unique strong flow only on an activation-dependent local interval. Equations (14), (17), and (18) do not prove that this interval reaches (T_\phi). In particular an arbitrarily small multiple of an activation can make (q_0) arbitrarily small; no identification of the local theorem's lifetime with (18) is available.

## 6. A smaller sufficient continuation interface

For perpendicular anchors the first-layer scalar gate can be removed even when it has zeros. Let \(\mathscr I(\tau,z)\) solve

\[
\partial_\tau\mathscr I=\phi'(\mathscr I),\qquad \mathscr I(0,z)=z.
\]

B.1 proves global scalar existence and

\[
|\mathscr I(\tau,z)-\mathscr I(\widetilde\tau,z)|\le D|\tau-\widetilde\tau|,
\quad |\mathscr I(\tau,z)|\le |z|+D|\tau|.
\tag{19}
\]

Set \(w_a=\mathscr I(X_a,w_{a,0})\). For mean loss the transformed physical equations are

\[
\dot X_a=-g r_a A^*\delta_a,
\quad \dot A=-\sum_a r_a\delta_a\otimes p_a,
\quad \dot c=-\sum_a r_a H_a,
\quad \delta_a=c\phi'(z_a).
\tag{20}
\]

The factor (g) occurs only in the clock equation. The full raw first row is recovered as

\[
W=W_0+\sum_a (w_a-w_{a,0})u_a/g.
\tag{21}
\]

Fix (T<\infty). Construct the ordinary population Euler programs for (20) on common generated spaces. Here “ordinary” means that the original activation is used, with no replacement of either matrix orientation. The following two quantitative assumptions are sufficient for strong continuation through (T):

1. Every sufficiently fine Euler program through (T) has a common bound (M_T) on the clock (L^2) norms, middle operator norm, and readout (L^2) norm.
2. For some \(\lambda_T>0\) and finite (B_T), their readout nodes satisfy
   \[
   \sup_{\Delta,k\Delta\le T}E_2e^{\lambda_T|c_k^\Delta|}\le B_T.
   \tag{22}
   \]

The fixed-program existence needed here follows from A.1 directly: \(\mathscr I\) is continuous with a linear envelope, and the backward product \(c\phi'(z)\) is also continuous with a linear envelope in its arguments. Population contractions at each fixed step are deterministic finite scalars. A.1 constructs all required values and actual adjoint actions; no named-source derivative formula for \(\mathscr I\) is being assumed.

**Proof of sufficiency.** Compare same-root states using clock (L^2) distance, trained-middle Hilbert–Schmidt distance, and readout (L^2) distance; call their sum (d\). Rank-one increment estimates control the Hilbert–Schmidt distance as well as the operator distance. On the common ball, (19) makes (p_a,z_a,H_a,f_a,r_a) Lipschitz in (d). Only the top backward product needs localization:

\[
\|c\phi'(z)-\widetilde c\phi'(\widetilde z)\|_2
\le D\|c-\widetilde c\|_2
+LR\|z-\widetilde z\|_2
+2D\|\widetilde c\mathbf1_{|\widetilde c|>R}\|_2.
\tag{23}
\]

The true adjoint is bounded and the first gate is absent from (20), so substitution into all three equations gives

\[
\|F(\theta)-F(\widetilde\theta)\|
\le C_T(1+R)d+C_T\|\widetilde c\mathbf1_{|\widetilde c|>R}\|_2.
\tag{24}
\]

Only the reference readout has been localized. There is no tail hypothesis on \(A^*\delta_a\). Assumption (22) implies

\[
\|c\mathbf1_{|c|>R}\|_2\le C_{\lambda_T,B_T}e^{-\lambda_T R/4},
\tag{25}
\]

because (x^2\le C_{\lambda_T}e^{\lambda_T x/2}\) for (x\ge0\), followed by the exponential Markov bound. The Euler velocities are uniformly bounded on the common ball. Comparing two interpolants on an interval of length \(\tau\) gives

\[
\sup d\le C e^{C_T(1+R)\tau}
\left[d_{\rm start}+(1+R)(\Delta+\Delta')
+e^{-\lambda_T R/4}\right].
\tag{26}
\]

Choose \(C_T\tau<\lambda_T/4\). For fixed (R), first send both meshes to zero; then send (R\to\infty\). This proves Cauchy convergence on the first interval. Repeat on finitely many intervals: their initial distances have already converged to zero before removing (R). Completeness and continuity of the bounded-multiplier products pass the integral equations to a strong solution. Fatou transfers (22) at each time to the reference solution. The same one-reference estimate proves uniqueness against any other bounded strong solution, without requiring its tails. The scalar flow identity and the integrable-coefficient argument of B.1 recover the unique raw first-layer equation through (21). This proves the interface.

For the fitted reference it is enough to establish these assumptions through (T_\phi) in (18). A Gaussian readout tail is stronger than necessary; an exponential tail suffices by subdividing time in (26).

This is a genuine reduction of the localization requirement, but (22) has not been proved globally here. The local response theorem C.2 supplies stronger tails only on its short initial interval. The interface also explicitly retains the Euler norm bound; it is not silently inferred from a formal energy calculation on a solution that has not yet been constructed.

## 7. What energy provides, and what it does not

Along an existing raw strong physical solution, A.4 gives the exact energy identity

\[
\mathcal L(t)+\int_0^t
\left(E_1|\dot W|^2+\|\dot A\|_{\rm HS}^2+\|\dot c\|_2^2\right)du=1.
\tag{27}
\]

Consequently each raw increment is bounded by \(\sqrt t\), and the full raw state is Cauchy at a finite maximal endpoint. Bounded derivatives and linear growth then bound all forward/backward (L^2) norms, middle operator norms, and clock norms on finite existing intervals. These are the population analogues of the finite-dynamics energy estimates, justified by the actual raw gradient.

Neither (27) nor endpoint completeness gives local existence at an arbitrary reached (L^2) state. In (23), bounded (L^2) norm alone gives no uniform rate for the last tail. C.1 cannot simply be restarted by declaring the reached action independent of new Gaussian roots. Thus the unresolved continuation implication is precise: finite-horizon energy control must be supplemented by a valid source/tail or alternative stability construction at reached states. No finite-width global existence statement resolves this population implication by itself.

## 8. Activity, nonaffinity, and the endpoint distinction

C.1 plus the corrected weighted C.3 statement applies to the present class locally: the inputs are nonparallel, Gaussian variances and mobilities are positive, the population readout is zero, and both labels are nonzero. Its coefficients use \(p_a=\omega_a y_a=y_a/2\). Both initial hidden marginals are nondegenerate Gaussian; since \(\phi\) is continuous and nonaffine,

\[
\inf_{\alpha,\beta}E[(\phi(Z)-\alpha Z-\beta)^2]>0
\tag{28}
\]

at initialization. The covariance formula for the best affine fit and (L^2) continuity keep these errors positive on a sufficiently short common interval.

For each sample and each hidden layer, C.3's weighted correction gives an (L^2) expansion

\[
H_a^{(\ell)}(t)-H_a^{(\ell)}(0)
=t^2V_a^{(\ell)}+o_{L^2}(t^2),\qquad
\|V_a^{(\ell)}\|_2>0.
\tag{29}
\]

Hence the paired activation displacement is strictly positive for all sufficiently small positive (t). It is the paired law of initial and current coordinates that is used in (29), not merely a change in an unpaired marginal distribution. The upper-layer positivity retains the independent unused Gaussian component from the actual initial forward/reverse/forward calculation, so flat gates are allowed.

Statements (28)–(29) are local. The supervisor's final scope explicitly accepts early positive-time paired activity and visited-law nonaffinity; these statements therefore meet those two obligations. They do not assert either observable specifically at the possibly much later fitting time (T_\phi\). Reached preactivation laws are not automatically Gaussian. Positive integrated hidden motion through (T_\phi) also follows once continuation is known, because the integral contains the nonzero local motion in (29).

## 9. Regularity and smoothing audit

The local existence and local activity used above inherit the explicit C.1 smoothing construction: for a smooth compactly supported probability mollifier,

\[
\|\phi_\varepsilon-\phi\|_\infty\le C D\varepsilon,
\quad \|\phi_\varepsilon'-\phi'\|_\infty\le C L\varepsilon,
\quad \|\phi_\varepsilon'\|_\infty\le D,
\quad \|\phi_\varepsilon''\|_\infty\le L.
\tag{30}
\]

C.2's local response estimates are uniform in these bounds; C.1's one-reference comparison then passes to the original activation. Initial (q_{0,\varepsilon}\to q_0>0\): the first features converge in (L^2), their finite covariance matrices converge, the Gaussian square-root coupling gives (Y_\varepsilon\to Y\) in (L^2), and the uniform activation approximation plus the common Lipschitz constant passes (14) to the limit. Thus positivity is not lost by this passage.

The radial proof (7)–(17) uses only strong chain rules with bounded continuous \(\phi'\); no second derivative appears. The bounded global theorem B.1 and the conditional interface (19)–(26) also work directly at (C^{1,1}), using the scalar Lipschitz ODE and A.1's continuous value instructions. No unavailable global response theorem is inferred from (30). If one instead attempts a global proof by smoothing source derivatives, one must establish the continuation bounds uniformly in the smoothing scale; the local uniformity in C.2 alone does not provide that.

## 10. Equal-label and balanced-label scope

For (m\) perpendicular equal-length anchors with all (y_a=1\), permutation symmetry gives (f_a=b). Replace (2) by \(h=m^{-1}\sum_aH_a\). Equations (7)–(18) hold with every signed half-sum replaced by that mean. Initial positivity follows from the full-support upper Gaussian tuple: if \(\sum_a\phi(Y_a)=0\) identically, varying one coordinate would make \(\phi\) constant. Thus the same bounded fitted-reference theorem and unbounded continuation gap hold.

The same symmetry argument extends to an even number of anchors with equally many (+1) and (-1) labels. Permutations within each class make its predictions constant; exchanging the two classes and negating (c) makes those two constants opposite. Then \(h=m^{-1}\sum_a y_aH_a\), (f_a=y_ab\), and the radial lemma applies. This is a claim for balanced signs on perpendicular, exchangeable anchors only. Arbitrary mixed labels, unequal class sizes, unequal label magnitudes, and nonorthogonal data have not been treated.

## 11. One additional row-removal partial

This section assesses a different possible continuation mechanism. It proves a Gaussian bound for the row-independent driving signal, and locates exactly the reinsertion estimate still missing. It does not use the desired population continuation as an assumption.

At finite width, fix an upper row (j) and delete its output contribution and trainable readout coordinate. Keep the original normalization (1/n), all lower neurons, and all other upper rows. Denote this deleted-row gradient flow by a superscript ((-j)). Its loss remains a nonnegative square loss, so the finite-dimensional energy proof gives a global flow and

\[
\int_0^T\frac{\|\dot W^{(1),(-j)}(t)\|_F^2}{n}\,dt
\le\mathcal L_n^{(-j)}(0).
\tag{31}
\]

This argument extends directly to (C^{1,1}): the finite raw field is locally Lipschitz by its displayed finite products and the Lipschitz activation derivatives; differentiation of the (C^1) loss gives the same energy identity. No classical second derivative is needed.

Let (a_{0,j}\in\mathbb R^n\) be the initialized middle row, with iid (N(0,1/n)) coordinates, and let (p_a^{(-j)}(t)=\phi(W^{(1),(-j)}(t)u_a)\). The deleted-row trajectory is independent of (a_{0,j}). Conditionally on that complete trajectory,

\[
G_{j,a}(t)=a_{0,j}\cdot p_a^{(-j)}(t)
\tag{32}
\]

is a centered Gaussian process. Its sample paths are absolutely continuous. Since

\[
\frac{\|\dot p_a^{(-j)}(t)\|_2^2}{n}
\le D^2g\frac{\|\dot W^{(1),(-j)}(t)\|_F^2}{n},
\tag{33}
\]

the conditional expected squared norm of the Gaussian Hilbert vector

\[
\mathscr G_j=
\big(G_{j,a}(0),\sqrt T\,\dot G_{j,a}|_{[0,T]}\big)_{a=1,2}
\in\mathbb R^2\oplus L^2([0,T];\mathbb R^2)
\]

is at most

\[
M_T^{(-j)}
=\sum_a\frac{\|p_a^{(-j)}(0)\|_2^2}{n}
+2TD^2g\,\mathcal L_n^{(-j)}(0).
\tag{34}
\]

On an initialization event measurable without (a_{0,j}), the right side is bounded by a deterministic constant, uniformly in (n), with probability tending to one for any fixed (j). To check this, the Gaussian lower-row law bounds initial activation RMS, while the deleted readout RMS tends to zero and the remaining middle operator norm is bounded with probability tending to one; these are the same finite initialization estimates as the allowed energy source. No simultaneous assertion over all (j) is needed for this partial.

For completeness, if a finite-rank centered Gaussian Hilbert vector has covariance eigenvalues \(\lambda_i\ge0\) with \(\sum_i\lambda_i\le M\), then

\[
E\exp(\|\mathscr G\|^2/(4M))
=\prod_i(1-\lambda_i/(2M))^{-1/2}\le e^{1/2}.
\tag{35}
\]

Indeed \(-\log(1-x)\le2x\) for \(0\le x\le1/2\). The case (M=0) is identically zero. Finally,

\[
\sum_a\sup_{t\le T}|G_{j,a}(t)|^2
\le2\sum_a\left(|G_{j,a}(0)|^2+T\int_0^T|\dot G_{j,a}(t)|^2dt\right),
\tag{36}
\]

so (34)–(36) give a conditional subGaussian envelope for the *entire path* of the independent driver (32). This is stronger than a bound at each single time and uses only finite energy and genuine row independence.

The actual row query, however, also contains

\[
a_{0,j}\cdot[p_a(t)-p_a^{(-j)}(t)].
\tag{37}
\]

No estimate for (37) with an adequate deterministic linear-growth constant has been derived. A direct perturbation of the coupled backward field contains, in its smooth version,

\[
\delta\{c_k\phi'(z_{k,a})\}
=\phi'(z_{k,a})\,\delta c_k
+c_k\phi''(z_{k,a})\,\delta z_{k,a}
\tag{38}
\]

for all remaining rows (k). The (C^{1,1}) difference version is exactly the last two terms of (23). Energy bounds the readout RMS, but does not bound this multiplier on the perturbation in RMS. A leave-one-row-out argument could still succeed if it proves that this particular perturbation remains sufficiently spread across the other rows; such a statement is an additional causal response estimate, not a consequence of (31).

Thus this route has an exact Gaussian forcing lemma but an unresolved reinsertion estimate. This is not a no-go result for row removal, and it does not reject the possibility that signed energy or a specific response identity controls (37). The proof supplied so far neither establishes that identity nor permits dropping the term (38).

## 12. First-round conclusion

The route proves an exact fitting mechanism and a complete bounded-activation fitted reference for the primary opposite-label pair, without oddness or monotonicity. Early paired activation motion and visited-law nonaffinity meet the final requested scope through the weighted C.3 result. The unbounded class has a strictly smaller sufficient continuation interface: transformed Euler norm control plus exponential tails of the readout alone. The global interface remains unproved. The additional row-removal calculation proves Gaussian control of the independent forcing path, but still requires control of its reinsertion correction.

Recommended route status: retain the radial lemma as proved; mark the full unbounded reference as conditional on the explicit continuation interface. Reopen the global construction only with a new bound proving (22), an alternative comparison theorem, or an actual reached-state construction. No additional polishing of (10) can close that gap.
