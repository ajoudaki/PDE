# Nuclear variation, causal compression, and the remaining sample dependence

Status: scoped theoretical analysis; internally derived, not independently reviewed or established book material. Scientific inputs were restricted to the supervisor's prompt. No other study, manuscript, code, experiment, or external scientific source was consulted. All mathematical claims used below are proved here.

## Contract and principal conclusion

The target is the original nonlinear deep-network gradient flow, with fixed depth \(L\), width \(n\), \(m\) training samples, fixed exact initial matrices \(W_{\ell,0}\), and middle-layer identity

\[
 \dot W_\ell(t)=-\frac{2}{mn}\sum_{a=1}^m
 r_a(t)\,\delta_{\ell,a}(t)h_{\ell-1,a}(t)^\top.
\]

Write \(A_\ell=W_\ell-W_{\ell,0}\). Only the learned corrections are compressed; exact initial operators and access to the training data are explicitly separate resources. The proposed approximation evaluates the original empirical gradient at its own current state. It does not add a regularizer, freeze features, linearize the network, or replace the target loss.

**Strong positive result.** A causal SVD-shrinkage algorithm compresses an incoming sum of rank-one matrices into rank \(r\), with uniform-prefix error at most \(V/(r+1)\) in operator norm and \(V/\sqrt{r+1}\) in Frobenius norm, where \(V\) is the sum of the incoming nuclear norms. It stores \(O(nr)\) learned scalars. Combined with an explicit Euler discretization of the original vector field, this gives a restartable, sample-independent learned-state approximation on a compact horizon, provided the atomic-gradient and stability bounds are uniform in \(m\). Those assumptions hold on a common bounded parameter region for an empirical average of uniformly bounded, uniformly Lipschitz per-sample vector fields. Their verification for the exact canonical scaling and activation remains a separate obligation.

This answers a stronger version of a static low-rank existence question, but it does not remove sample dependence from gradient evaluation time or automatically compress the source dataset. It also does not establish an autonomous continuous-time harmonic closure. The bounded-variation lower examples below show sharp generic rates; they are not claimed to be realized by the supplied nonlinear network without an additional construction.

## 1. What nuclear variation gives, sharply

For a matrix \(M\), let \(\|M\|_{\mathrm{op}}\), \(\|M\|_F\), and \(\|M\|_*\) denote respectively its largest singular value, square root of the sum of squared singular values, and sum of singular values. A rank-one matrix satisfies

\[
 \|uv^\top\|_* = \|uv^\top\|_F
 =\|uv^\top\|_{\mathrm{op}}=\|u\|_2\|v\|_2,
\]

because its only nonzero singular value is the displayed product.

Let \(A:[0,T]\to\mathbb R^{n\times n}\) be absolutely continuous, \(A(0)=0\), and

\[
 V=\int_0^T\|\dot A(t)\|_*\,dt<\infty.
\]

Integration and the triangle inequality give \(\|A(t)\|_*\le V\) for every \(t\). If \(A_r(t)\) retains its \(r\) largest singular values, then, for \(1\le r<n\),

\[
 \sup_{t\le T}\|A(t)-A_r(t)\|_{\mathrm{op}}
 \le\frac{V}{r+1},\qquad
 \sup_{t\le T}\|A(t)-A_r(t)\|_F
 \le\frac{V}{2\sqrt r}.
 \tag{1}
\]

Here the second bound is a valid upper bound for all \(n\), and its constant is optimal when \(n\ge2r\).

**Proof of the rates and optimality.** For decreasing singular values \(s_1\ge\cdots\ge s_n\ge0\), \((r+1)s_{r+1}\le\sum_i s_i\le V\). Put \(s=s_{r+1}\). Since \(s_i\le s\) for \(i>r\),

\[
 \sum_{i>r}s_i^2\le s\sum_{i>r}s_i
 \le s(V-rs)\le \frac{V^2}{4r}.
\]

To see that no rank-\(r\) approximation beats the relevant singular tails, let \(B\) have rank at most \(r\), and let \(P\) project orthogonally onto its column space. Then

\[
 \|A-B\|_F^2\ge\|(I-P)A\|_F^2
 =\sum_i s_i^2\bigl(1-\|Pu_i\|_2^2\bigr)
 \ge\sum_{i>r}s_i^2.
\]

The final inequality holds because \(0\le\|Pu_i\|^2\le1\), their sum is at most \(r\), and putting total weight \(r\) on the \(r\) largest \(s_i^2\) maximizes the subtracted sum. For the operator norm, the span of the first \(r+1\) right singular vectors contains a unit vector \(x\in\ker B\), so \(\|(A-B)x\|=\|Ax\|\ge s_{r+1}\). Truncated SVD attains both bounds on the approximation error.

For sharp operator error, take \(A_*=(V/(r+1))I_{r+1}\oplus0\). For sharp Frobenius error, take \(A_*=(V/(2r))I_{2r}\oplus0\). The smooth paths \(A(t)=(t/T)A_*\) have nuclear variation \(V\). Their optimal endpoint errors are respectively \(V/(r+1)\) and \(V/(2\sqrt r)\). Thus \(r\asymp V/\varepsilon\) and \(r\asymp(V/\varepsilon)^2\) are unavoidable worst-case orders under this information alone. These are fixed-accuracy lower bounds, not objections based merely on exact rank.

If \(r<n<2r\), the isotropic rank-\(n\) example gives \(V\sqrt{n-r}/n\); the simpler dimension-free bound in (1) is sufficient here. If \(r\ge n\), no compression error is needed.

Choosing the SVD of the full current \(A(t)\) is causal as a mathematical map, but obtaining it from an uncompressed \(A(t)\) does not itself save memory. The next construction removes that particular gap for streamed increments.

## 2. A causal rank-\(r\) stream compressor

**Proposition 1.** Let \(X_j=u_jv_j^\top\in\mathbb R^{n\times n}\), \(j=1,2,\ldots\), be revealed sequentially; scalar coefficients can be absorbed into either factor. Fix \(1\le r<n\). There is a deterministic update maintaining a rank-at-most-\(r\) matrix \(B_j\), \(B_0=0\), for which every prefix obeys

\[
 \left\|\sum_{j=1}^N X_j-B_N\right\|_{\mathrm{op}}
 \le\frac{V_N}{r+1},\qquad
 \left\|\sum_{j=1}^N X_j-B_N\right\|_F
 \le\frac{V_N}{\sqrt{r+1}},
 \quad
 V_N=\sum_{j=1}^N\|X_j\|_*.
 \tag{2}
\]

**Construction and proof.** Form \(C_j=B_{j-1}+X_j\), whose rank is at most \(r+1\). Let \(d_j=\sigma_{r+1}(C_j)\), padding the singular list by zeros if necessary, and set

\[
 B_j=U_j\operatorname{diag}\bigl((\sigma_i(C_j)-d_j)_+\bigr)V_j^\top.
 \tag{3}
\]

The result has rank at most \(r\). Write \(E_j=C_j-B_j\). If \(d_j>0\), all \(r+1\) nonzero singular values of \(E_j\) equal \(d_j\); if \(d_j=0\), \(E_j=0\). Consequently,

\[
 \|E_j\|_{\mathrm{op}}=d_j,\quad
 \|E_j\|_F=\sqrt{r+1}\,d_j,\quad
 \|B_j\|_* =\|C_j\|_*-(r+1)d_j.
\]

The triangle inequality therefore yields

\[
 (r+1)d_j\le
 \|B_{j-1}\|_*+\|X_j\|_*-\|B_j\|_*.
\]

Summing telescopes to \((r+1)\sum_{j\le N}d_j\le V_N\). Since the exact residual is

\[
 \sum_{j=1}^N X_j-B_N=\sum_{j=1}^N E_j,
\]

both estimates in (2) follow by the corresponding triangle inequalities. In fact the argument controls the stronger accumulated discarded norm, \(\sum_j\|E_j\|_{\mathrm{op}}\le V_N/(r+1)\) and \(\sum_j\|E_j\|_F\le V_N/\sqrt{r+1}\).

An SVD factorization of \(B_{j-1}\), plus \(u_j,v_j\), reduces (3) to orthogonalizing two new directions and an SVD of a matrix of size at most \(r+1\). Thus storage is \(O(nr+r^2)=O(nr)\), including working factors when \(r<n\). No past atom, omitted coefficient, or future trajectory is retained. The update is invariant under choices of singular vectors in a tied singular subspace, because singular values tied at the cutoff are all sent to zero.

**Dense-increment extension.** The same result holds for arbitrary matrix increments, as an algebraic input-output guarantee. For \(C=B+X\), use \(d=\sigma_{r+1}(C)\) and (3). Put \(D=\|C\|_*-\|B_{\mathrm{new}}\|_*\). The discarded matrix has singular values \(\min(\sigma_i(C),d)\), so

\[
 D\ge(r+1)d,\qquad
 \|E\|_{\mathrm{op}}=d,\qquad
 \|E\|_F^2\le dD.
\]

Telescoping gives \(\sum D\le\sum\|X\|_*\) and \(\sum d\le V/(r+1)\). Cauchy–Schwarz gives \(\sum\|E\|_F\le\sqrt{(\sum d)(\sum D)}\le V/\sqrt{r+1}\). Dense incoming increments may themselves require dense processing/storage; the native rank-one implementation avoids that cost.

For a path of nuclear variation \(V\), feed increments \(A(t_j)-A(t_{j-1})\) to this extension. At grid times (2) holds with \(V_N\le V\). Between grid times hold \(B\) constant. If each interval has nuclear variation at most \(\eta\), the uniform-time errors are at most \(V/(r+1)+\eta\) and \(V/\sqrt{r+1}+\eta\). A causal schedule can stop an interval when its accumulated variation reaches \(\eta\). This statement assumes access to the incoming increments/variation; it is a tracking theorem, not by itself a closed simulation of unknown network dynamics.

## 3. Applying the compressor to the original nonlinear gradient

The native atomic nuclear budget of layer \(\ell\) is

\[
 V_{\ell,\mathrm{atom}}(T)
 =\frac{2}{mn}\int_0^T\sum_{a=1}^m
 |r_a(t)|\,\|\delta_{\ell,a}(t)\|_2\,
 \|h_{\ell-1,a}(t)\|_2\,dt.
 \tag{4}
\]

It bounds the actual nuclear variation by the triangle inequality. They need not be equal: cancellations between samples can make actual variation much smaller. A guarantee based on the native streaming implementation must use (4), not silently substitute the smaller quantity.

If throughout the region in question

\[
 \frac{\|\delta_{\ell,a}\|_2\|h_{\ell-1,a}\|_2}{n}\le C_\ell
 \quad\text{for every sample},
\]

then Cauchy–Schwarz for the empirical average gives

\[
 V_{\ell,\mathrm{atom}}(T)
 \le2C_\ell\int_0^T
 \left(\frac1m\sum_{a=1}^m r_a(t)^2\right)^{1/2}dt.
 \tag{5}
\]

If the true gradient flow decreases the empirical squared residual from a value at most \(E_0\), (5) gives \(V_{\ell,\mathrm{atom}}(T)\le2C_\ell T\sqrt{E_0}\). This dependence has no explicit \(m\). However, it is a bound along the true trajectory; a simulator also needs bounds in a neighborhood of that trajectory. Neither an uncontrolled \(C_\ell=C_\ell(m)\) nor a bound valid only at initialization supplies sample-uniform control.

**Proposition 2: a closed discrete simulator.** Consider the complete parameter state \(\Theta\), with vector field \(F(\Theta)\) given by the original empirical loss. Some matrix blocks are compressed as \(W_{\ell,0}+B_\ell\); all remaining parameters are included in the state and evolved normally. Choose either operator or Frobenius norm on each matrix block and an appropriate norm on other blocks, and use the sum of block norms, denoted \(\|\cdot\|\). Assume on a convex region containing the exact trajectory and the numerical iterates that

1. \(\|F(\Theta)-F(\Theta')\|\le K\|\Theta-\Theta'\|\);
2. \(\|F(\Theta)\|\le M_F\);
3. the sum over compressed layers and native sample atoms of their nuclear norms per unit time is at most \(M\), uniformly in \(\Theta\).

The constants must be uniform in \(m\) for the claimed sample-independent rank. For a step size \(\tau=T/N\), evaluate every native sample gradient at a frozen copy of the current approximate state \(\widetilde\Theta_k\). Feed its \(\tau\)-scaled rank-one matrix increments into Proposition 1, starting from the existing correction in each layer. Evolve the uncompressed parameters by the same frozen-state Euler step. Then

\[
 \max_{0\le k\le N}\|\widetilde\Theta_k-\Theta(k\tau)\|
 \le e^{KT}\left(MT\,c_r+\frac12 KM_FT\tau\right),
 \tag{6}
\]

where \(c_r=(r+1)^{-1}\) for the operator block norm and \(c_r=(r+1)^{-1/2}\) for the Frobenius block norm. If the approximation is held constant between steps, add \(M_F\tau\) to the right side for a uniform-time bound. These conclusions require no target-trajectory oracle.

**Proof.** Let \(D_k\) be the sum of all discarded matrices during step \(k\), inserted in their corresponding state blocks. The algorithm has the exact identity

\[
 \widetilde\Theta_{k+1}
 =\widetilde\Theta_k+\tau F(\widetilde\Theta_k)-D_k.
\]

The telescoping nuclear potentials continue across steps. Applied separately to each compressed layer and then summed, Proposition 1 gives

\[
 \sum_{k=0}^{N-1}\|D_k\|\le MTc_r.
\]

The exact solution satisfies

\[
 \Theta((k+1)\tau)=\Theta(k\tau)+\tau F(\Theta(k\tau))+R_k,
 \qquad \|R_k\|\le\tfrac12 KM_F\tau^2,
\]

because the integral of \(F(\Theta(t))-F(\Theta(k\tau))\) is bounded by \(\int_0^\tau KM_Fs\,ds\). Thus, for \(e_k=\|\widetilde\Theta_k-\Theta(k\tau)\|\),

\[
 e_{k+1}\le(1+K\tau)e_k+\|D_k\|+\tfrac12 KM_F\tau^2.
\]

Starting from \(e_0=0\), iterating and using \((1+K\tau)^N\le e^{KT}\) proves (6). Between steps, exact movement is bounded by \(M_F\tau\).

If the constants are only available on a fixed tube around the exact trajectory, use this proof up to the first numerical exit. Choosing the right side of (6) smaller than the tube radius rules out that exit; a convex enclosing region, or Lipschitz estimates valid for the relevant pairs, justifies the comparisons. This is a conditional bootstrap, not permission to assume an arbitrary simulator stays bounded.

For example, choose \(\tau\) so the Euler and interpolation terms total at most \(\varepsilon/2\), and then choose

\[
 r+1\ge\frac{2e^{KT}MT}{\varepsilon}
 \quad\text{or}\quad
 r+1\ge\left(\frac{2e^{KT}MT}{\varepsilon}\right)^2
\]

for respectively operator or Frobenius control. If this exceeds width, retain the exact learned matrix. Otherwise learned matrix storage is \(O(Lnr)\), independently of \(m\). This is a genuine alternative to keeping \(O(Lmnq)\) sample-indexed time moments.

**Where the uniform assumptions come from.** If \(F_m=(1/m)\sum_a f(\Theta,z_a)\), and every data point \(z_a\) lies in a fixed class on which \(f\) is uniformly bounded and uniformly \(K\)-Lipschitz in parameters on a common region, then averaging preserves those bounds: apply the triangle inequality to the average and its differences. A uniform bound on the native rank-one atom norms gives assumption 3 in the same way. For a fixed finite width, smooth activation, bounded data, and a fixed bounded parameter region, such bounds can be proved by differentiating the actual network. Their dependence on width, initial operator norms, activation derivatives, and the region radius must be displayed; smoothness alone is not a width-uniform theorem. Nonsmooth activations require an additional stability argument and are not covered merely by asserting differentiability.

**A fixed-width smooth-gradient corollary.** Suppose, additionally, that the complete flow is Euclidean gradient flow for a nonnegative empirical loss \(\mathcal E_m=m^{-1}\sum_a e(\Theta,z_a)\), that data lie in a fixed compact finite-dimensional set, that \(e\) is \(C^2\) in parameters with continuous derivatives jointly in parameters and data, and that the native atom factors are jointly continuous. Initial parameters are fixed independently of \(m\). Then for each fixed \(n,L,T\), the required common-region bounds exist uniformly in \(m\). Indeed compactness gives \(E_*=\sup_z e(\Theta_0,z)<\infty\), and

\[
 \frac{d}{dt}\mathcal E_m(\Theta(t))
 =-\|\dot\Theta(t)\|_2^2,\qquad
 \|\Theta(t)-\Theta_0\|_2
 \le\sqrt{t\int_0^t\|\dot\Theta(s)\|_2^2ds}
 \le\sqrt{TE_*}.
\]

On a closed Euclidean ball enlarged by a positive margin, times the compact data set, the continuous per-sample first and second derivatives and atom factors are bounded. Finite-dimensional norm equivalence converts these to the block norm used in Proposition 2; the conversion may depend on \(n,L\), but not on \(m\). Empirical averaging preserves the bounds. Choosing the approximation error smaller than the margin (with the same norm-equivalence factor if needed) closes the numerical bootstrap. For a fixed positive-definite constant gradient metric \(D\), namely \(\dot\Theta=-D\nabla\mathcal E_m\), the same calculation uses \(\|\dot\Theta\|_{D^{-1}}^2\) for dissipation and gives Euclidean displacement at most \(\sqrt{\lambda_{\max}(D)TE_*}\). The metric must have an \(m\)-uniform bound.

This proves that sample-count dependence is not intrinsically necessary in the smooth fixed-width setting. It does not supply useful width-uniform constants, a favorable numerical rank at large width, or a nonsmooth-activation theorem. Those remain the substantive specialization questions.

**Causality and cost.** The gradient of each sample is evaluated at the frozen step state, not at the partially compressed candidate; otherwise the displayed Euler identity would fail. Keeping both factorizations costs only a constant multiple of \(O(Lnr)\). One sample's forward/backward values can be computed and discarded, using transient \(O(Ln)\) activation storage for an ordinary chain. A restart at a step boundary needs the factor state, other parameters, step information, fixed initial operators, and dataset access. It needs no per-sample history. Arithmetic still processes \(m\) samples per step; applying the exact initial operators still costs their own operations/storage. The result is about learned-state memory, not sample-independent runtime or total input information.

No continuous-time rank-manifold equation or uniqueness of a fixed-rank limiting flow is asserted. A finite-step restartable solver with certified error already establishes the stated approximation result. The shrinkage is numerical state compression; the target remains the original loss.

## 4. Operator, action, and Frobenius metrics are different contracts

For any test vector \(x\),

\[
 \|(A-B)x\|_2\le\|A-B\|_{\mathrm{op}}\|x\|_2.
\]

For sample vectors \(h_a\),

\[
 \left(\frac1m\sum_a\|(A-B)h_a\|_2^2\right)^{1/2}
 \le\|A-B\|_{\mathrm{op}}
 \left(\frac1m\sum_a\|h_a\|_2^2\right)^{1/2}.
 \tag{7}
\]

Thus the \(1/r\) rate directly controls normalized action if feature norms are normalized accordingly. An unnormalized \(\|h_a\|\asymp\sqrt n\) inserts a \(\sqrt n\) factor in absolute action error; it cannot be dropped by terminology. Uniform action on every unit vector is exactly operator error. Action on a restricted finite set can be much easier and does not imply operator control.

If all relevant vectors belong to a known \(k\)-dimensional subspace with projector \(P\), then \(AP\) has rank at most \(k\) and agrees with \(A\) on that subspace. This does not automatically establish closed network accuracy: features and adjoints move under parameter perturbations, and the same action set need not remain valid in the compressed dynamics.

A genuine exact geometry is available when every right factor of the original gradient belongs to the same fixed subspace: \(h_{\ell-1,a}(t)=Ph_{\ell-1,a}(t)\). Then \(\dot A_\ell=\dot A_\ell P\), and \(A_\ell(0)=0\) implies \(A_\ell=A_\ell P\), hence rank at most \(k\). The analogous statement holds for a common left-factor subspace. Approximate concentration also has a direct source estimate:

\[
 \|A_\ell(T)(I-P)\|_*
 \le\frac{2}{mn}\int_0^T\sum_a |r_a|
 \|\delta_{\ell,a}\|_2\|(I-P)h_{\ell-1,a}\|_2\,dt.
 \tag{8}
\]

The same bound holds at every earlier time with the truncated integral. Equation (8), followed by a stability estimate, is a stronger geometry-dependent route than a norm bound alone. A time-varying small instantaneous subspace does not imply a small common subspace: successively directing rank-one increments along distinct coordinate pairs produces a high-rank integral. Variation controls the fixed-accuracy damage of such rotations, as Propositions 1–2 quantify.

## 5. What sparse or harmonic coefficient assumptions do and do not buy

These conclusions concern a declared coefficient basis or dictionary. They are not consequences of nonlinear gradient flow unless a separate argument establishes the coefficient bounds along the relevant states.

**An \(\ell_0\) bound.** At most \(s\) nonzero coefficients give an exact \(s\)-term representation, provided the actual support and coefficients are available. Pointwise sparsity in time need not bound the union of supports over time. Sparsity says nothing about the largest active harmonic index. For example every coordinate vector \(e_j\) is 1-sparse and has \(\ell_1\) and \(\ell_2\) norm one, while it escapes every fixed finite cutoff as \(j\) increases. Consequently a fixed harmonic degree cannot be selected from any of these three unweighted bounds alone.

**An \(\ell_1\) bound in an orthonormal basis.** If \(\sum_j|c_j|\le C\), retaining the \(r\) largest coefficients gives

\[
 \|c-c^{(r)}\|_2\le\frac{C}{2\sqrt r},\qquad
 \|c-c^{(r)}\|_\infty\le\frac{C}{r+1}.
\]

The proof is exactly the sorted-tail argument of Section 1, and the equal-coefficient examples make the constants sharp when sufficiently many coordinates are available. Thus adaptive support selection really can remove ambient cardinality from approximation counts. Rejecting this possibility merely because a fixed cutoff fails would be incorrect.

For a general Hilbert-space dictionary \(\phi_j\) with \(\|\phi_j\|\le1\), orthogonality is not necessary for a weaker \(C/\sqrt r\) approximation. Let \(f=\sum_j c_j\phi_j\) with \(S=\sum_j|c_j|\le C\). If \(S>0\), sample independent atoms \(Z=S\,\mathrm{sign}(c_J)\phi_J\), with \(\Pr(J=j)=|c_j|/S\). Then \(\mathbb EZ=f\), \(\mathbb E\|Z\|^2\le S^2\), and

\[
 \mathbb E\left\|\frac1r\sum_{i=1}^r Z_i-f\right\|^2
 =\frac1r\bigl(\mathbb E\|Z\|^2-\|f\|^2\bigr)
 \le\frac{C^2}{r}.
\]

The cross terms vanish by independence and zero mean. Therefore some combination of at most \(r\) dictionary atoms has error at most \(C/\sqrt r\). If \(S=0\), use the zero approximation. This is an existence result using the full coefficient distribution; by itself it is not a causal closure or a procedure for discovering coefficients from compressed network states.

**An \(\ell_2\) bound alone.** Let \(c_j=C/\sqrt N\) on \(N\) coordinates. Then \(\|c\|_2=C\), but the error of the best \(r\)-term approximation is \(C\sqrt{1-r/N}\). For any fixed \(r\), this approaches \(C\) as \(N\to\infty\). There is no uniform adaptive \(\ell_2\)-tail convergence over an \(\ell_2\) ball. The same construction with \(A=(C/\sqrt N)I_N\) shows that a Frobenius bound alone does not yield dimension-independent low-rank Frobenius accuracy. It does yield operator error at most \(C/\sqrt{r+1}\), because \((r+1)s_{r+1}^2\le C^2\), with equality for \(r+1\) equal singular values. Metric choice therefore changes the conclusion materially.

**Weighted smoothness.** If a fixed orthonormal harmonic basis satisfies

\[
 \sum_j w_j^2|c_j|^2\le C^2,\quad
 1\le w_1\le w_2\le\cdots\to\infty,
\]

then the fixed-cutoff tail satisfies \(\sum_{j>r}|c_j|^2\le C^2/w_{r+1}^2\). This follows by replacing every tail weight by its minimum. A Fourier weight of order \(s\) on a fixed \(d\)-dimensional domain gives cutoff error of order \(J^{-s}\), with order \(J^d\) retained modes, hence a mode-count rate of order \(r^{-s/d}\). To verify the latter claim, retain the integer frequency cube \(|k_i|\le J\), which has \((2J+1)^d\) modes; every omitted frequency has Euclidean norm greater than \(J\), so its weight is at least a constant times \(J^s\). Constants, domain dimension, and the smoothness norm must be uniform. If the coordinate domain itself grows with \(m\), this argument has not removed sample difficulty.

**Basis cost and feedback.** An adaptive harmonic support must be encoded. Among \(D\) orthonormal atoms, the \(D\) possible vectors \(e_j\) are separated by \(\sqrt2\). Any finite-bit code achieving error less than \(1/\sqrt2\) on all of them must use at least \(D\) distinct codewords, hence at least \(\log_2D\) bits in the worst case. Unbounded support indices therefore cannot be treated as constant-cost coefficients. Dense rank-one directions similarly require their vector coordinates; the \(O(nr)\) count explicitly includes them. A coefficient tail estimate must also be transported through the nonlinear flow in the chosen observable norm; a static \(\ell_1\) bound does not establish a closed multiplication/composition algebra or control the stability constant.

Finally, an \(\ell_2\) bound over \(D\) coefficients only gives \(\ell_1\le\sqrt D\,\ell_2\) by Cauchy–Schwarz. Inserting that into an \(\ell_1\) theorem can conceal the very dimension being removed. The empirical \(1/m\) normalization in (4)–(5) is different: it bounds an averaged absolute residual by an averaged square residual and does not introduce \(\sqrt m\).

## 6. Source information and horizon are real costs, but not blanket no-go results

**Data access.** Removing sample-indexed learned history leaves the original samples, labels, and their empirical weights as external inputs. Proposition 2 can reread them each step. Claiming total memory independent of \(m\) requires either a streaming/replay model or a certified finite summary. Arbitrary-precision scalar encodings of the entire dataset are excluded.

It would also be wrong to assert that fixed-accuracy simulation must always retain all \(m\) samples. For example, suppose data live in \([-R,R]^d\), and the per-example vector field \(f(\Theta,z)\) is uniformly \(L_z\)-Lipschitz in \(z\) and \(K\)-Lipschitz in \(\Theta\) on the relevant region. Partition the data cube into cells of diameter at most \(\eta\). Store one representative \(z_c\) and its empirical mass \(p_c\) for every occupied cell. Then

\[
 \left\|\frac1m\sum_a f(\Theta,z_a)-\sum_c p_cf(\Theta,z_c)\right\|
 \le L_z\eta.
\]

Two flows with identical initialization consequently satisfy

\[
 \|\Theta(t)-\Theta_{\mathrm{summary}}(t)\|
 \le
 \begin{cases}
 L_z\eta(e^{Kt}-1)/K,&K>0,\\
 L_z\eta t,&K=0.
 \end{cases}
\]

One obtains this by integrating the difference inequality \(e(t)\le\int_0^t(Ke(s)+L_z\eta)ds\), or differentiating the upper envelope. A cube grid of side at most \(\eta/\sqrt d\) has at most \((1+2R\sqrt d/\eta)^d\) cells, independent of \(m\). Finite-precision masses introduce an additional explicitly controllable error. This is certified quadrature for the original target, not an exact-gradient implementation; it is optional and unnecessary for Proposition 2. Its curse of dimension and uniform data-regularity requirement are genuine. If the contract requires exact evaluation of the empirical gradient at each approximate state, retain dataset access instead.

**Time and stability.** Even the favorable native budget (5) can grow linearly in \(T\), while the general flow comparison contributes \(e^{KT}\). A loss that decreases does not by itself imply contractive parameter dynamics. For a concrete scalar squared nonlinear loss,

\[
 \mathcal E(x)=\tfrac14(x^2-1)^2,\qquad
 \dot x=-\mathcal E'(x)=x-x^3,
\]

the solution \(x(t)=0\) has infinitesimal sensitivity \(\partial x(t)/\partial x(0)=e^t\), obtained by differentiating the ODE at zero. The loss is nonnegative and decreases along gradient flow; nearby initial conditions in \((-1,1)\) remain bounded. Thus loss dissipation alone does not eliminate growth of perturbations. This example illustrates a necessary stability obligation; it is not offered as a sample-compression lower bound for the specified architecture.

Similarly, a constant independent of the symbol \(m\) can still depend on increasingly difficult data through feature/adjoint norms, conditioning, input dimension, label magnitude, required horizon, or activation regularity. A meaningful uniform theorem states a fixed admissible data/initialization class and bounds those quantities before taking the supremum over sample size. Under such a class, empirical averaging itself does not force sample-count dependence.

## 7. Bounded-scope verdict and next proof obligation

The generic nuclear-variation route supports sample-independent approximate learned matrix state; it does not support a no-go conclusion. Its sharp accuracy orders are \(r^{-1}\) for operator/action control and \(r^{-1/2}\) for Frobenius control. The explicit causal shrinkage construction attains those orders while using the original empirical gradients, and a complete conditional error argument closes a discrete simulator.

The claims established here are algebraic compression, sharp variation-only rates, and conditional compact-horizon simulation. It remains open within this input scope whether the canonical network's full parameter metric, activation assumptions, and scaling yield the needed width- and sample-uniform neighborhood bounds at useful constants; whether a desired harmonic representation has uniform weighted/\(\ell_1\) control and causal coefficient evolution; and whether stronger invariant feature geometry gives materially better ranks.

The highest-leverage next proof obligation is to specialize Proposition 2 to the exact canonical network: prove explicit common-region bounds on its native atomic budget and on the original vector field in the metric that controls the required observable. That bridge would turn a general low-rank streaming route into a theorem for the intended network without introducing a modified training objective.
