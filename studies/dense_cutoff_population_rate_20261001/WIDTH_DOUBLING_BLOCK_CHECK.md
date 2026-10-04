# Reconstruction check of the autonomous block endpoint bridge

2026-10-03. Scoped internal check, not a promotion review.

Reviewed complete source: WIDTH_DOUBLING_BLOCK_ROUTE.md, SHA-256
452fffc78086900b9ccb550ee4903353dc542246c2153772b7a0f17bfcabacdf.

The full feedback-stability source was also read:
SELF_AVERAGING_FEEDBACK_ROUTE.md, SHA-256
b3709cac57c005b209dbcaf084848987ee4fe824de0f798d596db8caf6c3554a.
The previously read complete same-width concentration source is
GENERAL_SELF_AVERAGING.md, SHA-256
bfbc14cbb3cccf902420db74ca6e3627e341f27a84b52a229362848b376a56d5.
No other study, experiment, Git history or manuscript change is involved.

**Outcome:** the positive endpoint bridge follows from the stated physical
tube, carrier-maximum and same-width concentration results. The argument
does not supply a comparison across the interpolation interior and does
not prove the requested width-\(n\) versus width-\(2n\) theorem.

## 1. Model and scope reconstructed

Fix the same training inputs, weights \(p_a>0\), labels, activation class,
depth and canonical mobilities as in the source. The activations have
bounded first three derivatives and may have unbounded, linearly growing
values. The initial readout vanishes. Put
\[
 Y^2=\sum_a p_a y_a^2,\qquad D_p=\operatorname{diag}(\sqrt{p_a}).
\]
All matrices, residuals and positive-gap inequalities below are restricted
to the common compatible data quotient when the full training Gram is
singular for structural reasons. In particular, the source's notation
\(K\succeq\lambda I\) means the identity on that quotient, not a new
full-data positive-definiteness assumption. The common model preserves
the structural constraints, so averaging and subtracting its training
predictions keep the residual errors in this same space.

The shared-residual pair and two independent reference networks use the
same initial parameters block by block. Their predictions are respectively
\(\widetilde f_j\) and \(f_j\), \(j=1,2\), with width-\(n\) normalization.
Write
\[
 R=\frac{\widetilde f_1(X)+\widetilde f_2(X)}2-y,\qquad
 r_j=f_j(X)-y,\qquad \rho_j=\|D_pr_j\|_2 .
\]
The independent initializations are used only for the probabilistic input;
the comparison argument itself is deterministic.

## 2. Endpoint normalization check

At the zero-profile endpoint, diagonal hidden blocks have variance
\(2/(2n)=1/n\), and their hidden mobility coefficient is also \(1/n\).
Off-diagonal blocks vanish initially and have zero mobility forever.
Read-in and readout velocities have the canonical block coefficients.
The full prediction is precisely
\[
 F_{2n,0}=\frac{\widetilde f_1+\widetilde f_2}{2}.
\tag{C1}
\]
In block mobility coordinates
\(\Theta_j=(W_j^1,\sqrt nW_j^2,\ldots,\sqrt nW_j^L,w_j)\), with
\(g_{j,a}=\nabla_{\Theta_j}(nf_j(x_a))\), the equations are
\[
 \dot{\widetilde\Theta}_j=-2\sum_a p_aR_a\widetilde g_{j,a},
 \qquad
 \dot\Theta_j=-2\sum_a p_ar_{j,a}g_{j,a}.
\tag{C2}
\]
There is no missing factor \(1/2\) in (C2): the factor enters (C1), while
the full network's canonical endpoint mobility supplies the compensating
block learning coefficient. The residual is shared, so the two trained
tilded blocks are not independent.

## 3. Shared-pair fitting requires no tilded carrier maximum

For a prescribed common control with total variation at most \(S_*\),
bounded initial first-layer Frobenius RMS and hidden operator norms imply
bounded feature RMS by the forward recursion and linear activation
growth. Readout RMS is \(O(S_*)\), hence backward response RMS is
\(O(S_*)\). Integrating each hidden vector field gives normalized
hidden displacement and variation \(O(S_*^2)\). Small fixed \(S_*\)
closes the physical bounds uniformly in width.

The initialized readout-feature Gram changes by at most \(CS_*^2\),
because its two feature factors have bounded RMS and feature displacement
is \(O(S_*^2)\). Starting with an averaged initial margin and reducing
\(S_*\) preserves a gap \(\lambda>0\). Each weighted tangent \(K_j\)
dominates its weighted readout-feature Gram. Thus, for
\(\widetilde{\overline K}=(\widetilde K_1+\widetilde K_2)/2\),
\[
 \partial_t(D_pR)=-2\widetilde{\overline K}D_pR,\qquad
 \widetilde{\overline K}\succeq\lambda I .
\tag{C3}
\]
Consequently \(\|D_pR(t)\|\le Ye^{-2\lambda t}\), and the total common
control variation is at most \(Y/\lambda\). The strict choice
\(Y/\lambda<S_*/2\) prevents a first exit. This proves the required
global shared-pair tube and convergence using only physical RMS/operator
bounds and the initial Gram margin. The averaged output fits; no claim
that either tilded block separately fits is needed.

## 4. One-sided gate subtraction and tangent differences

Let \(D_j=D_{j,h}+D_{j,w}\) be the source's sum of normalized parameter
differences, and \(D=D_1+D_2\). Forward subtraction gives normalized
training-feature error \(CD_{j,h}\). For each layer, subtract the
backward gates as
\[
 \widetilde\delta-\delta
 =\phi'(\widetilde z)\odot(\widetilde k-k)
    +[\phi'(\widetilde z)-\phi'(z)]\odot k .
\tag{C4}
\]
Only the reference \(k\) multiplies the gate difference. Its coordinate
bound \(M\), bounded \(\phi''\), and forward subtraction give the gate
term \(CM D_{j,h}\). The remaining backward matrix difference is bounded
by \(CS D_{j,h}\), using reference response RMS and physical matrix
operators. Descending the finite number of layers gives
\[
 \frac{\|\Delta g_{j,a,h}\|_2}{\sqrt n}
      \le C[D_{j,w}+(M+S)D_{j,h}],\qquad
 \frac{\|\Delta g_{j,a,w}\|_2}{\sqrt n}\le CD_{j,h}.
\tag{C5}
\]
The \(M\) terms add over layers; they do not multiply, since each term
in (C4) is a direct forward difference times a reference carrier.

The physical hidden-gradient RMS is \(CS\), and readout-gradient RMS is
bounded. Subtracting their quadratic tangent pairings therefore gives
\[
 \|\widetilde K_j-K_j\|_{\mathrm{op}}
   \le C[(1+SM)D_{j,h}+SD_{j,w}]
   \le C(1+SM)D_j,\qquad \|K_j\|_{\mathrm{op}}\le C .
\tag{C6}
\]
No carrier maximum for the tilded state, and no segment joining the
two states, enters this derivation.

## 5. Exact residual forcing and the Gronwall closure

Define
\[
 \xi_j=D_pr_j,\quad
 s=\frac{\xi_1+\xi_2}{2},\quad
 d=\frac{\xi_1-\xi_2}{2},\quad
 e=D_pR-s,\quad \overline K=\frac{K_1+K_2}{2}.
\]
The reference residual equations yield
\[
 \dot s=-2\overline Ks-(K_1-K_2)d.
\]
Combining with (C3) gives
\[
 \dot e=-2\widetilde{\overline K}e
       -2(\widetilde{\overline K}-\overline K)s
       +(K_1-K_2)d,\qquad e(0)=0.
\tag{C7}
\]
The sign and coefficient of the last term are correct. Bounding the
individual \(K_j\) suffices; no small tangent difference between the
independent reference blocks has been assumed.

From (C2), split each parameter-velocity difference into
\((R-r_j)\widetilde g_j+r_j(\widetilde g_j-g_j)\).
Since \(D_p(R-r_1)=e-d\) and \(D_p(R-r_2)=e+d\), (C5) gives
\[
 D(t)\le C\int_0^t(\|e\|+\|d\|)\,du
       +C(1+M)\int_0^t(\rho_1+\rho_2)D\,du .
\tag{C8}
\]
The propagator for the first term of (C7) contracts at rate \(2\lambda\).
Using (C6), \(\|s\|\le(\rho_1+\rho_2)/2\), and integrating the exponential
kernel gives
\[
 \int_0^t\|e\|\,du
 \le C(1+SM)\int_0^t(\rho_1+\rho_2)D\,du
       +C\int_0^t\|d\|\,du .
\tag{C9}
\]
This uses a nonnegative integrand, so Tonelli is valid already on finite
intervals. With \(S\) fixed small, substitution in (C8) yields an
integrable Gronwall coefficient \(C(1+M)(\rho_1+\rho_2)\). Its integral
is at most \(CS(1+M)\). The inhomogeneity
\(J(t)=\int_0^t\|d(u)\|\,du\) is nondecreasing. Thus
\[
 \sup_{t\ge0}D(t)\le Ce^{CS(1+M)}J(\infty).
\tag{C10}
\]
The proof does not absorb \(SM\) as a small constant. It retains its
width-dependent contribution inside the exponential, exactly as needed
for the near-root conclusion.

## 6. All-time and query-law estimates

Let \(\epsilon=\sup_t\|d(t)\|\). Reference fitting gives
\(\|d(t)\|\le Ye^{-\kappa t}\), so direct splitting at
\(\kappa^{-1}\log(Y/\epsilon)\), when \(0<\epsilon<Y\), gives
\[
 J(\infty)\le \frac{\epsilon}{\kappa}
             [1+\log_+(Y/\epsilon)] .
\tag{C11}
\]
The cases \(\epsilon=0\) and \(\epsilon\ge Y\) have the interpretations
stated in the source. The right side is nondecreasing in \(\epsilon\):
its derivative below \(Y\) is \(\log(Y/\epsilon)\), and above \(Y\)
it is one. Replacing \(\epsilon\) by an upper bound is therefore valid.

For arbitrary \(x\), put \(B(x)=1+\|x\|/\sqrt d\). Forward subtraction
and linear growth give query feature RMS \(CB(x)\) and feature-difference
RMS \(CB(x)D_{j,h}\). Prediction product subtraction then gives
\[
 \sup_t|\widetilde f_j(t,x)-f_j(t,x)|
       \le CB(x)\sup_tD_j(t).
\tag{C12}
\]
Hence the time supremum remains inside the query-law integral, and only
\(\int B(x)^2\,d\mu(x)<\infty\) is needed. Parameter convergence extends
the same bound to the fitted limits without exchanging a supremum and
an expectation.

## 7. Probability bookkeeping and claim boundary

On the finite intersection of reference good events, the carrier theorem
gives \(M=CS\sqrt{\log(e+n)}\). The same-width theorem applied to the
training query law bounds
\[
 \epsilon\le C_\delta n^{-1/2}
                       e^{K_0\sqrt{\log(e+n)}}.
\]
Indeed its metric controls the weighted Euclidean norm uniformly in
time, because a supremum of a finite sum is no larger than the sum of
coordinatewise suprema. Its factor \(1/2\) is absorbed into constants.
The initial physical and Gram events also have probability tending to
one. At fixed requested confidence, a finite union bound therefore
suffices for all sufficiently large \(n\); no quantitative complement
probability is needed.

Equations (C10)–(C11) multiply this rate by
\(e^{CS(1+M)}\) and at most a logarithm. Both are absorbed into
\(e^{K\sqrt{\log(e+n)}}\). Equations (C1) and (C12) prove
\[
 \mathcal E_\mu\left(F_{2n,0},\frac{f_1+f_2}{2}\right)
 \le C_{\delta,\mu}n^{-1/2}e^{K\sqrt{\log(e+n)}} .
\tag{C13}
\]
Here
\(\mathcal E_\mu(f,g)^2=\int\sup_{t\in[0,\infty]}|f(t,x)-g(t,x)|^2d\mu(x)\).
Applying the same-width theorem also at the query law \(\mu\), or at its
mixture with the training law, proves the comparison with either \(f_j\).
Zero labels give stationary zero readouts and exact equality.

The checked proof establishes a fixed-confidence high-probability
endpoint bridge. It does not provide an unconditional expected error,
does not turn the trained shared-residual blocks into independent
trajectories, and does not estimate
\(\mathcal E_\mu(F_{2n,1/2},F_{2n,0})\). The remaining covariance/mobility
comparison and the deterministic center shift are correctly left open
by the reviewed source. No substantive correction to that source was
found in this reconstruction.
