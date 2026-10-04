# A shared spectral memory can remove sample-indexed moving state

Research result, 2026-09-29. This document records a new theoretical investigation, not a change to the paper or an established-book theorem. The fully specified network algorithm and its compact-time proof are in `CAUSAL_ROUTE.md`; the present document explains the mathematical choice, strengthens the norm interpretation, and records evidence and boundaries.

## 1. Main conclusion

The factor m in the current response-memory state count is not forced by the empirical gradient equation. It results from preserving a separate approximation to each sample's response history. A different causal representation can compress the *sum of all paired updates* directly, using one shared evolving spectral basis per hidden layer.

A deterministic construction stores O(LnR) learned hidden-state scalars, independent of m and of the number of elapsed steps. At fixed finite width and depth it approximates the original nonlinear gradient flow on [0,T], with a bound of the form

\[
\sup_{0\le t\le T}\sup_{x\in K}
 |\widehat f_{R,\eta}(t,x)-f_{\rm dense}(t,x)|
 \le C_{T,n,K}\bigl((R+1)^{-1}+\eta\bigr).
\tag{1}
\]

Here K is any fixed bounded test-input set, eta is the integration step, and R is the number of shared spectral modes, not the former per-sample Legendre order q. The constant is uniform over sample counts and datasets with uniformly bounded input norms and label RMS. For bounded smooth activations such as tanh, the estimate is available for every R>=1; for general locally C^{1,1} activations the common-region version applies once R and eta make its explicit first-exit bound small enough. At R>=n compression can be disabled, recovering ordinary Euler integration.

The construction is an autonomous, restartable **discrete** network evolution. Its factors change throughout training. It is not ordinary loss-gradient descent on low-rank factors. Its continuous-time limit at fixed R has not been proved to be a unique smooth ODE. Equation (1) proves joint approximation to gradient flow when the representation and integration resolutions are chosen appropriately; it does not silently replace that unresolved limit by an ODE.

This resolves explicit sample-indexed *moving-state* growth for a concrete finite-time approximation. The bounds do not yet show a useful R much smaller than n uniformly over widths, nor a width-uniform feedback constant. Static data and initialized matrices are retained, and full-batch computation still reads all samples.

## 2. Which norm actually expresses the proposed idea?

For an orthonormal functional basis, the squared coefficient l2 norm is the represented function's squared L2 norm. Rotating the basis leaves this unchanged. For a matrix of response features A, right multiplication by an orthogonal matrix Q likewise preserves ||AQ||_F. Thus merely searching over orthogonal bases to minimize l2 coefficient energy provides no compression mechanism.

An unrestricted adaptive basis also has a description cost: an m-component sample-space basis vector still costs m numbers. The basis should live in the adjacent neuron populations. For a learned matrix M, write

\[
 M=\sum_j c_j u_jv_j^T,\qquad \|u_j\|_2=\|v_j\|_2=1.
\]

The minimum coefficient l1 cost over all such decompositions is exactly the nuclear norm,

\[
 \inf\sum_j|c_j|=\|M\|_* =\sum_j\sigma_j(M).
\tag{2}
\]

Proof: let M=U Sigma V^T be a thin SVD and Q=UV^T. Then ||Q||op<=1 and <Q,M>=sum sigma_j. Every normalized atom satisfies |<Q,uv^T>|<=1, so every decomposition has sum |c_j|>=sum sigma_j. The SVD attains equality. The minimum number of atoms is rank(M). In the SVD, the coefficient l2 norm equals ||M||F and l0 counts the nonzero singular values.

Thus the principled analogue of sparse harmonic coefficients is **sparsity of paired singular directions**, with a nuclear-norm budget. These directions are adaptive population patterns rather than fixed Fourier frequencies. The atoms must be normalized; otherwise rescaling u or v makes the coefficient penalty meaningless.

## 3. Why the canonical updates supply an l1 budget

For one middle layer in the notation of the paper,

\[
 \dot W=-\frac{2}{mn}\sum_{a=1}^m r_a\delta_a h_a^T.
\tag{3}
\]

Each contribution is rank one, and ||uv^T||*=||u||2||v||2. Its accumulated atomic mass is

\[
 V(T)=\frac{2}{mn}\int_0^T\sum_a |r_a(t)|
             \|\delta_a(t)\|_2\|h_a(t)\|_2\,dt.
\tag{4}
\]

If normalized responses satisfy ||delta_a||/sqrt(n)<=D and ||h_a||/sqrt(n)<=H, then

\[
 V(T)\le 2DH\int_0^T \rho(t)\,dt,
 \qquad \rho^2=m^{-1}\sum_a r_a^2.
\tag{5}
\]

The 1/m normalization removes the count of examples from this bound. It bounds an average of contributions; it does not require the samples to be independent, orthogonal, or interchangeable.

For the dense flow, canonical energy dissipation additionally gives

\[
 \int_0^T\left[
 \frac{\|\dot W_1\|_F^2+\|\dot w\|_2^2}{n}
 +\sum_{\ell=2}^L\|\dot W_\ell\|_F^2\right]dt
 \le\mathcal L(0).
\tag{6}
\]

Hence each middle operator norm stays within sqrt(T L(0)) of its initial bound, and the normalized readout and first-layer norms obey the corresponding estimate. With bounded phi and phi', equation (5) consequently gives a source budget independent of width as well whenever those initial normalized bounds are uniform. This is a *compression-source* estimate; it is not yet width-uniform control of nonlinear feedback.

## 4. The causal compression rule and its proof

Keep a rank-at-most-R learned matrix M in skinny factors. Upon receiving one native rank-one update A, form the skinny representation of C=M+A. This has rank at most R+1. Let d=sigma_{R+1}(C), with d=0 if the rank is smaller, and replace all singular values sigma_j of C by

\[
 (\sigma_j-d)_+.
\tag{7}
\]

The result again has rank at most R. Every basis is recomputed within the span of the previously retained directions and the current response pair. No initialized direction dictionary constrains future motion.

This is a precise norm-based optimization. For fixed d>=0, the retained matrix is the unique minimizer

\[
 \underset{B}{\operatorname{argmin}}\;
 \tfrac12\|B-C\|_F^2+d\|B\|_*.
\tag{8}
\]

To verify (8) without an optimization theorem, let B be (7) and, for d>0, let Z=(C-B)/d. Its singular values are at most 1 and <Z,B>=||B||*. Nuclear/operator duality implies ||N||*>=<Z,N> for every N, so ||N||*>=||B||*+<Z,N-B>. Expanding the quadratic objective around B makes the linear term <B-C+dZ,N-B> vanish and leaves at least ||N-B||F^2/2. Thus B uniquely minimizes the objective. At d=0 the claim is immediate.

The choice d=sigma_{R+1}(C) is dictated by the storage cap. It is not a new penalty added to the network's training objective. Its perturbation of the original update is explicitly charged to the compression error.

If D=C-B is the discarded matrix, then

\[
 \|D\|_{\rm op}=d,\qquad
 \|D\|_F=\sqrt{R+1}\,d,\qquad
 \|B\|_*=\|C\|_*-(R+1)d.
\]

Therefore every insertion satisfies

\[
 \|M_{\rm new}\|_*+(R+1)d
 \le \|M_{\rm old}\|_*+\|A\|_*.
\]

Summing over arbitrary many insertions telescopes the stored nuclear norm. If S is the exact sum of the supplied atoms, which is used only in the proof, then

\[
 \sum d\le\frac{\sum\|A\|_*}{R+1},\qquad
 \|S-M\|_{\rm op}\le\frac{\sum\|A\|_*}{R+1},\qquad
 \|S-M\|_F\le\frac{\sum\|A\|_*}{\sqrt{R+1}}.
\tag{9}
\]

These bounds hold at **every prefix** and for atoms that depend on earlier retained states. There is no independence assumption and no per-step error multiplied by the number of steps. The norm budget pays for all discarded directions together.

An important distinction: repeated best-rank truncation does not have this particular accounting law. If it keeps diag(1,0) and repeatedly receives 0.02 e2 e2^T, hard rank-one truncation discards every increment; after 200 such increments the forgotten second diagonal entry is 4. Soft shrinkage spends down the first direction, eventually retaining the repeatedly supplied second direction. Its error here is 1. The deterministic verification reproduces this example; it is an algebra example, not a network training result.

## 5. Why this tracks learning, not just a matrix stream

For a step eta, freeze the current compressed network and stream all training samples. Form its own residual, forward responses and backward responses, and insert

\[
 A_{\ell,k,a}=-\frac{2\eta}{mn}\widehat r_{k,a}
          \widehat\delta_{\ell,k,a}\widehat h_{\ell-1,k,a}^T
\]

into working copies of each layer's shared memory. Accumulate the canonical first-layer and readout updates exactly. All evaluations within a pass use the same frozen current network; installing partial updates before evaluating later samples would be a different algorithm. At the end of the pass install the working factors and outer updates simultaneously.

For the original canonical vector field F, the resulting states satisfy the exact identity

\[
 \widehat\theta_k=\theta_0+\eta\sum_{j<k}F(\widehat\theta_j)-E_k,
\tag{10}
\]

where E has zero outer blocks and its middle blocks are the accumulated discards in (9). Thus no dense-network responses are needed in the implementation.

Use the normalized mixed norm

\[
 \|\Delta\theta\|_{\mathrm{mix}}=
 \max\{\|\Delta W_1\|_F/\sqrt n,
        \|\Delta w\|_2/\sqrt n,
        \max_{\ell\ge2}\|\Delta W_\ell\|_{\rm op}\}.
\]

Let a convex bounded region contain both paths, let K be a Lipschitz constant for F in this norm, let M bound ||F||mix there, and let b bound each layer's atomic mass per unit physical time. These constants can be chosen uniformly over m: network derivatives are bounded on the parameter/input region, and averages of |y_a| are at most the fixed label RMS bound. The complete construction and proof of such a region for locally C^{1,1} activations, using a first-exit argument, are in `CAUSAL_ROUTE.md` Sections 4--5. For bounded gates the following direct bounds remove the first-exit restriction altogether.

For the held numerical state theta_hat(t)=theta_hat_floor(t/eta), (10) differs from the canonical integral equation by at most Tb/(R+1)+eta M. Hence

\[
 e(t)\le\frac{Tb}{R+1}+\eta M+K\int_0^t e(s)\,ds,
 \qquad
 \sup_{t\le T}e(t)\le
 e^{KT}\left(\frac{Tb}{R+1}+\eta M\right).
\tag{11}
\]

The network's forward map is Lipschitz in this state norm on every bounded test-input set. Equation (1) follows. Integrating its square gives the same bound for prediction discrepancy in L2(mu) for any probability measure supported on that set. These are errors against the dense trained predictor, not a guarantee that either predictor generalizes to the unknown true labels.

### Direct bounded-gate bounds, for every rank and arbitrary bounded label RMS

Assume |phi|<=H, |phi'|<=s, H>0, and phi in C^{1,1}_loc. Let B0=||w0||/sqrt(n), Y be label RMS, and

\[
 \bar B=(B_0+Y/H)e^{2H^2T}-Y/H,\qquad \bar\rho=H\bar B+Y.
\]

The readout update gives B_{k+1}<=(1+2eta H^2)B_k+2eta HY, proving B_k<=bar B for k eta<=T. The same differential inequality applies to dense flow. Define the middle-layer bounds backwards, starting with an empty product at ell=L:

\[
 b_\ell=2\bar\rho H\bar B\,
      s^{L-\ell+1}\prod_{j>\ell} C_j,
 \qquad C_\ell=\|W_{\ell,0}\|_{\rm op}+T b_\ell.
\tag{12}
\]

This is an acyclic recursion. The backward bound is ||delta_ell||/sqrt(n)<=bar B s^{L-ell+1} product_{j>ell} C_j. The sketch's nuclear potential gives ||M_ell||*<=T b_ell, so ||W_ell||op<=C_ell. Dense integration obeys the same triangle bound. Finally

\[
 \|W_1\|_F/\sqrt n\le\|W_{1,0}\|_F/\sqrt n
 +2T\bar\rho X\bar B s^L\prod_{j=2}^L C_j.
\tag{13}
\]

These bounds define a convex product of norm balls containing both trajectories, uniformly in rank, sample count and step number. At fixed width it is compact. Local C^{1,1} regularity supplies finite K and M there. Therefore (11) is unconditional for the stated bounded-gate class, with no fitting or small-label assumption and no sufficient-rank condition. H=0 gives a constant-zero activation and a degenerate, directly handled network; it need not be treated through the displayed division by H.

If initial operator norms and normalized outer norms are bounded uniformly in n, equations (12)--(13), b and M can be bounded uniformly in n. The **feedback Lipschitz constant K need not be**. Gate differences multiplied by backward carriers remain the relevant obstruction. This argument does not claim to settle that width-uniform theorem.

## 6. Cost, approximation axes, and limits

Moving hidden storage is O(LnR), plus O(nd+n) exact outer parameters and O(Ln) single-sample scratch. A second factor buffer and gradient accumulators change only constants. Fixed W0 storage remains O(Ln^2), and static dataset storage is separate.

For the simple implementation which shrinks after every atom, one insertion can be performed with skinny QR and a core SVD in O(nR^2+R^3). A full batch therefore costs O(Lmn^2+LmnR^2+LmR^3+mnd), including exact W0 actions. No n-by-n learned matrix is materialized. Batched co-occurring-direction shrinkage can reduce the sketch overhead by amortizing over O(R) atoms, but the included code implements the simpler per-atom version; an optimized runtime is not attributed to this code.

Equation (11) means that at fixed width and horizon the shared-mode requirement is O(epsilon^{-1}) in the operator-sensitive state/output estimate, with time step O(epsilon). The bare Frobenius streaming certificate is instead O(R^{-1/2}). Fixed-n norm equivalence can transfer the O(R^{-1}) trajectory rate to Frobenius norm with additional width-dependent constants; it does not make the matrix streaming lemma dimension-free at that faster rate.

The present response-memory clocks control the temporal approximation order q and obtain faster rates from regularity of separate histories. The shared spectral construction uses R collective response directions and does not automatically inherit the q^{-2} theorem. Combining their benefits needs another argument, not relabeling R as q.

Nor can a nuclear budget alone promise R^{-2}: for M=(V/(R+1))I_{R+1}, every rank-R approximation has operator error at least V/(R+1). The example proves a limit of the norm-only information. It does not assert that every such matrix path occurs in a particular canonical network. Under just a bounded Frobenius norm, M=(V/sqrt(N))I_N shows that rank truncation can leave almost all Frobenius energy when R<<N.

The correct resource suggested by this calculation is **the total paired learning activity and the spectrum of its accumulated interaction**, rather than the number of separately named training histories. It does not say that data complexity is irrelevant: more difficult tasks or longer fitting times can increase the required budget and stability amplification.

## 7. Primary precedent and novelty boundary

The singular-value shrinkage and nuclear-potential accounting are ingredients of co-occurring directions:

- Y. Mroueh, E. Marcheret, V. Goel, *Co-Occurring Directions Sketching for Approximate Matrix Multiply*, AISTATS 2017, Algorithm 2, Theorem 2 and its proof. Full nine-page primary paper inspected: https://proceedings.mlr.press/v54/mroueh17a/mroueh17a.pdf .

Our per-atom variant removes the (R+1)st singular value, rather than the median-based batched threshold used there. The bound above is proved directly for adaptive signed streams and then connected to this canonical self-interacting neural flow. The underlying matrix-sketching mechanism must not be presented as a new invention. This investigation has not established priority for the complete neural application relative to the full dynamical low-rank and gradient-compression literature. No broad novelty exclusion is asserted.

## 8. Actual verification and what remains

`spectral_memory.py` implements the skinny update. The deterministic command

```sh
OPENBLAS_NUM_THREADS=1 python -B studies/shared_response_basis_20260929/spectral_memory.py --out data/generated/shared_response_basis_20260929/algebra_001
```

completed with exit code 0 under NumPy 1.26.4. It checks 480 adaptive prefixes against independent dense SVD updates and uncompressed accumulators, including rectangular matrices, rank saturation, and signed sources depending on the retained state. Maximum discrepancy from the dense one-step oracle was 2.71e-14. The exact sharp diagonal example attains both streaming bounds. The repeated-small-update example yields operator errors 4 for hard truncation and 1 for shrinkage. Records are under the named generated directory. These are algebra and implementation checks, not a neural training benchmark or a numerical proof of the asymptotic theorem.

Three scoped proof routes were run independently initially: causal streaming/PSD lifting; functional bases/coresets; and norm limits. Their original results are retained in separate files. The source-level matrix lemma was independently recovered by the norm-limits route and cross-checked by the causal route. Complete argument review and any remaining objections are recorded in the study README.

Remaining research targets are: a useful practical rank on the paper's neural tasks; a unique continuous-time shared-mode law if a smooth ODE is required; improvement beyond R^{-1} using actual response structure; and width-uniform/all-time feedback. None is used as a premise of the finite-width, sample-uniform result above.
