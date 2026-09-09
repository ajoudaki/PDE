# Moderate sine activation: independent adversarial and constructive route

2026-09-08. No experiments. No review verdict was used as a mathematical premise. This report neither proves the requested unconditional strong population theorem nor gives a counterexample to the actual initialized neural trajectories.

## 1. Exact activation and scope

Write the prescribed activation, without modifying its amplitude, as

\[
\Phi(z)=A z+B\sin(2z),\qquad
D=\sqrt{1+\tfrac4{25}v},\quad
A=\frac{1-\frac45e^{-2}}D,\quad B=\frac{2}{5D},
\]
\[
v=\frac{1-e^{-8}}2-4e^{-4}.
\]
Then

\[
\Phi'(z)=A+2B\cos(2z),\quad
m:=A-2B>0,\quad L:=A+2B<\infty,\quad
\|\Phi''\|_\infty=4B.
\]
Indeed \(A-2B=[1/5-(4/5)e^{-2}]/D>0\), since \(e^2>4\).
The activation is globally bi-Lipschitz, smooth, odd, and an affine function plus a bounded perturbation. These properties alone do not supply any of the reachability estimates below.

The model is exactly the two-input, three-hidden-layer Gaussian network and raw metric in `studies/mean_field_peeling/two_sample_activation_design/PROOF.md`, Section 1. Population incoming fields are

\[
q_i^3=C,\quad b_i^3=\Phi'(z_i^3)q_i^3,\quad
q_i^2=(W^3)^*b_i^3,\quad b_i^2=\Phi'(z_i^2)q_i^2,\quad
q_i^1=(W^2)^*b_i^2,\quad b_i^1=\Phi'(z_i^1)q_i^1.
\]
The two original finite residuals remain in every physical update.

## 2. Exact unconditional finite-width bounds

Every finite-width GF has a smooth finite-dimensional vector field. Its true raw-gradient energy identity is

\[
\mathcal L_n(t)+\int_0^t\|\dot\Theta_n(s)\|_{\rm raw}^2 ds
=\mathcal L_n(0),
\]
\[
\|\Theta_n(t)-\Theta_n(0)\|_{\rm raw}
\le\sqrt{t\mathcal L_n(0)}.
\]
Thus there is no finite-time raw escape, so finite-width GF is global. At each fixed \(T\), current middle action norms are bounded by their initialized operator norms plus \(\sqrt{T\mathcal L_n(0)}\). Forward induction uses \(|\Phi(z)|\le L|z|\), and backward induction uses \(|\Phi'|\le L\). These give dimension-independent compact-time bounds on all normalized forward/backward second moments and true raw kernel blocks on the usual high-probability initialization event. Here \(\mathcal L_n(0)\to1\).

These are bounds on actual finite trajectories. They do not imply strong canonical compactness, tail uniform integrability, uniqueness, or the finite-width limit.

## 3. Reference-only comparison with one truncation factor

Let \(X,Y\) be two states on one canonical raw ball, or at the same finite width and initialization. There is a constant \(C_M\), depending on the ball, activation and fixed dataset, such that, with \(a=\|X-Y\|_{\rm raw}\),

\[
\sum_{i,\ell}(\|z_i^\ell(X)-z_i^\ell(Y)\|_2+
\|h_i^\ell(X)-h_i^\ell(Y)\|_2)+\sum_i|r_i(X)-r_i(Y)|
\le C_M a. \tag{3.1}
\]
This follows by the exact decomposition
\((W-\bar W)h+\bar W(h-\bar h)\), the HS-to-operator bound, and Lipschitzness of \(\Phi\).

For a smooth clip \(\tau_R\) with \(|\tau_R|\le|q|\), \(|\tau_R'|\le1\), \(\tau_R(q)=q\) on \(|q|\le R\), and \(|\tau_R|\le2R\), use precisely

\[
D_R(z,q)=Aq+2B\cos(2z)\tau_R(q).
\]
At each layer the capped incoming field is recursively recomputed using the capped higher backward field. In particular, the tail assumption below is about these actual recursively computed inputs.

For \(R_1,R_2\ge u\), including infinite caps,

\[
|D_{R_1}(z,q)-D_{R_2}(\bar z,\bar q)|
\le L|q-\bar q|+8Bu|z-\bar z|
+C_B|\bar q|\mathbf1_{|\bar q|>u}. \tag{3.2}
\]
To prove this, first change \(q\) inside \(D_{R_1}\), using its \(q\)-Lipschitz constant \(L\). In the remaining difference replace both clips by \(\tau_u(\bar q)\); outside \(|\bar q|\le u\) this costs at most a fixed multiple of \(B|\bar q|\), and the retained gate difference is bounded by \(4B|z-\bar z|\,2u\). Every tail belongs to the reference \(Y\).

Start at \(q^3=C\). Applying (3.2), then descending using

\[
\|q_i^\ell(X)-q_i^\ell(Y)\|_2
\le C_M a+C_M\|b_i^{\ell+1}(X)-b_i^{\ell+1}(Y)\|_2,
\]
shows

\[
\sum_{i,\ell}\|b_{R_1,i}^\ell(X)-b_{R_2,i}^\ell(Y)\|_2
\le C_M(1+u)a+C_M\sum_{i,\ell}
\|q_{R_2,i}^\ell(Y)\mathbf1_{|q_{R_2,i}^\ell(Y)|>u}\|_2.
\]
The factor \(u\) multiplies only a forward difference at each descent; it never multiplies the preceding backward discrepancy. Thus the factor remains linear in \(u\), not cubic in \(u\). Rank-one gradient difference estimates and (3.1) yield

\[
\|F_{R_1}(X)-F_{R_2}(Y)\|_{\rm raw}
\le C_M(1+u)a+C_M\sum_{i,\ell}
\|q_{R_2,i}^\ell(Y)\mathbf1_{|q_{R_2,i}^\ell(Y)|>u}\|_2.
\tag{3.3}
\]
Here \(F_R\) is the actual physical capped loss vector field. The full actual residual difference was retained.

## 4. A conditional global theorem requiring only exponential tails

This section supplies a sufficient hypothesis, not a proof of that hypothesis. The exponential-tail Osgood optimization itself has an existing antecedent in `studies/mean_field_peeling/practical_fixed_depth2/development/ENERGY_ROUTE.md`, Section 7, equations (20)--(25), for different depth-two energy-preserving caps. What is derived here is its exact three-hidden-layer, recursively componentwise-capped and scalar-raw-cutoff version for the prescribed activation; the Osgood device is not claimed as an entirely new idea.

Fix \(T\). Let \(\chi_M\) be a smooth function of the squared raw increment norm, taking values in \([0,1]\), equal to one on a prescribed ball and zero outside a slightly larger ball. Consider the global fixed-cap population ODEs

\[
\dot X_R=\chi_M(X_R)F_R(X_R),\qquad X_R(0)=0
\]
for increments from the canonical initialization. Fixed-cap local Lipschitzness and this scalar cutoff give global solutions; bounded action norms follow from the cutoff radius. The cutoff is a causal scalar contraction at fixed finite programs. No energy dissipation of these capped paths is assumed.

Assume that their actual incoming fields satisfy

\[
\sup_{R\ge1,\,t\le T,\,i,\ell}
\|q_{R,i}^\ell(t)\mathbf1_{|q_{R,i}^\ell(t)|>u}\|_2
\le K_T e^{-c_Tu},\qquad u\ge0. \tag{ET}
\]
The constants can depend on the fixed activation, dataset, horizon and cutoff radius, but not the cap. Gaussian tails are unnecessary here.

Multiplying (3.3) by the common cutoff adds only a term \(C_Ma\), because all capped fields have uniform raw bounds on this ball. Let \(a(t)=\|X_{R_1}(t)-X_{R_2}(t)\|_{\rm raw}\), \(R=\min(R_1,R_2)\), \(\eta=e^{-c_TR}\). Then for every \(0\le u\le R\),

\[
D^+a\le C[(1+u)a+e^{-c_Tu}]. \tag{4.1}
\]
Set \(z=a+\eta\). While \(z\le1\), choose
\(u=c_T^{-1}\log(1/z)\in[0,R]\). Equation (4.1) gives

\[
D^+z\le C_1z\log(e/z).
\]
With \(w=\log(e/z)\), this implies \(w(t)\ge w(0)e^{-C_1t}\), or

\[
\sup_{t\le T}a(t)
\le e\exp[-c_TR e^{-C_1T}] \tag{4.2}
\]
for all sufficiently large \(R\), the right side itself ensuring that \(z\le1\). This proves uniform Cauchy convergence on arbitrary finite horizons. The same comparison with a fixed fraction of \(R e^{-C_1T}\) in place of \(u\) makes the raw velocities Cauchy as well.

To identify the limit vector field, at each fixed reference cap compare the limit state with that cap using (3.3) and then let the cap increase. Bounded-multiplier continuity identifies all uncapped backward products. The limit is a strong \(C^1\) solution of

\[
\dot X=\chi_M(X)F_\infty(X).
\]
The true loss now obeys its exact identity

\[
\dot{\mathcal L}=-\chi_M\|\nabla\mathcal L\|_{\rm raw}^2,
\quad
\int_0^T\|\dot X\|_{\rm raw}^2dt
\le\int_0^T\chi_M\|\nabla\mathcal L\|_{\rm raw}^2dt
\le\mathcal L(0)=1.
\]
Consequently \(\|X(t)\|\le\sqrt T\). Choose \(\chi_M=1\) on a ball of radius strictly greater than \(\sqrt T\), with a larger support radius. The cutoff is then inactive along the constructed limit. This removes the stopping device without assuming a false capped energy identity or using arbitrary prescribed residual controls.

For uniqueness, compare any bounded-primal strong uncut competitor to the same capped reference by (3.3). The competitor has infinite cap and needs no tail estimate. The regularized Osgood argument yields equality with the limit. At reached times it also gives unique continuation, because the initial cap discrepancy in (4.2), though enlarged by another Osgood exponent, still vanishes. Integer horizons therefore produce a single global canonical strong physical solution.

The existing fixed-cap finite-program, mesh and generated-probe construction applies to this fixed \(\Phi\): its value has linear growth and its first two derivatives are bounded; at each fixed cap all required coordinate derivatives are bounded. If the supplied finite-algorithm and observable bridges are reassembled with (4.2) replacing Gaussian cap removal, they yield the same compact-time full-sequence joint GF/GD conclusions. Their cap comparison is one-reference sided; no tail hypothesis is required for actual finite uncut competitors after fixed-cap reference tails have been transferred by finite-program convergence. This report proves the core population conditional implication, not a completed independent audit of every such observable bridge.

The main unsolved assertion is (ET), or a weaker sufficient modulus. None of the preceding finite-width energy estimates proves it.

## 5. A prescribed-activation focusing example on raw balls

This is an ambient construction, not a trajectory or a counterexample to the desired theorem.

Keep the two lower layers at their exact initialized values. Let \(h=h_1^2\) be the first sample's initialized second-layer feature, so \(\|h\|_n^2\to1\). Let \(G=W_0^3\), independent of the lower layers, and take a column \(J\), either fixed or uniform independently. Write \(g_i=\sqrt n\,G_{iJ}\), iid standard Gaussians. Choose target top preactivations

\[
z_i=\begin{cases}0,&g_i\ge0,\\ \pi/2,&g_i<0,\end{cases}
\qquad
P=\frac{(z-Gh)\otimes h}{\|h\|_n^2}.
\]
The tensor convention is \(u\otimes h=uh^T/n\). Thus \((G+P)h=z\) exactly, and

\[
\|P\|_F=\|P\|_{\rm op}
=\frac{\|z-Gh\|_n}{\|h\|_n}=O_{\mathbb P}(1).
\]
Choose \(C=\mathbf1+C_0\), a raw readout displacement exactly one from the actual tiny initialized readout. For sample 1,

\[
\Phi'(z_i)=A+2B\operatorname{sign}(g_i).
\]
Consequently the immutable transpose contribution satisfies

\[
\frac{(G^*[\Phi'(z)C])_J}{\sqrt n}
=\frac1n\sum_i g_i[A+2B\operatorname{sign}(g_i)]+o_{\mathbb P}(1)
\longrightarrow 2B\sqrt{2/\pi}>0. \tag{5.1}
\]
The tiny-readout correction is bounded by the initialized operator norm times \(L\|C_0\|_n\), hence vanishes in this normalization. The learned transpose correction is

\[
P^*[\Phi'(z)C]
=h\,\frac{\langle z-Gh,\Phi'(z)C\rangle_n}{\|h\|_n^2}.
\]
Its scalar coefficient is \(O_{\mathbb P}(1)\), and \(h_J/\sqrt n\to0\) in probability. Thus (5.1) holds for the full \(q_1^2=(G+P)^*[\Phi'(z)C]\) as well.

All raw increments, action norms, normalized forward/backward second moments, and the two-sample loss are bounded in probability. The second sample shares the same new matrix and is controlled by its operator norm; it need not be assigned a separate activation or matrix. Nevertheless, for every fixed threshold \(u\),

\[
\liminf_{n\to\infty}\frac1n\sum_j(q_{1,j}^2)^2
\mathbf1_{|q_{1,j}^2|>u}\ge\frac{8B^2}{\pi}>0
\]
in the usual probabilistic lower-bound sense. Because \(\Phi'\ge m>0\), the corresponding middle backward field retains a square-tail defect at least \(m^2 8B^2/\pi\).

For random \(J\), the construction can be made invariant under the middle-layer neuron permutations. Exchangeability therefore does not repair the inference. The construction proves only that raw energy-ball bounds, a bounded sine perturbation, positive derivatives, and exchangeability cannot imply the needed tail estimate for all ambient states. Reachability by true GF is an additional and unresolved restriction.

## 6. Weak compactness does not identify this exact loss

Here is an exact failure of weak lower semicontinuity of the original two-sample loss on its ambient raw Hilbert state space, again not along initialized trajectories.

The initialized second-layer sample Gram is positive definite when \(|\rho|<1\). Choose dual fields \(h_1^\#,h_2^\#\) satisfying
\(\langle h_i^\#,h_j^2\rangle=\delta_{ij}\). Any prescribed pair of \(L^2\) top preactivation fields is realizable from the initialized top action by a sum of two HS rank-one increments.

Use \(C=y_1\mathbf1\), and set the base top preactivation of sample 1 to \(z_*=1/A\), sample 2 to \(\Phi^{-1}(y_1y_2)\). Since \(A>2/\pi\), one has \(0<z_*<\pi/2\), and so
\(\Phi(z_*)=1+B\sin(2/A)>1\). For a simple bound proving \(A>2/\pi\), note \(v<1/2\), \(D<\sqrt{27/25}<26/25\), \(e^{-2}<1/7\), hence \(A>(31/35)(25/26)>4/5>2/\pi\).

Let \(R_k\) be mean-zero Rademacher fields with \(R_k\rightharpoonup0\) in the nonatomic top-layer \(L^2\) space; for instance an orthonormal Rademacher sequence. Perturb only the top action by

\[
\Delta W_k^3=\frac\pi4 R_k\otimes h_1^\#.
\]
These HS increments converge weakly to zero. The sample-1 prediction becomes exactly

\[
y_1E\Phi(z_*+\tfrac\pi4R_k)
=y_1\{A z_*+B\sin(2z_*)\cos(\pi/2)\}=y_1.
\]
The second prediction remains \(y_2\). Therefore every perturbed state has zero loss, while its weak limit has strictly positive loss. The true raw loss is not weakly lower semicontinuous on this ambient Hilbert space. An unqualified weak-compactness/minimizing-movement existence argument is consequently unavailable. This does not exclude stronger compactness of the actual approximants.

## 7. Positive derivative does not make the raw gradient locally Lipschitz or semiconvex

The same dual-field device isolates the first sample's top preactivation. At an ambient state with \(C=G\), a centered unit Gaussian top-layer field, take its top preactivation constant \(z_* =\pi/4\); make the second sample's top preactivation constant too. Then both predictions are zero and the residuals are \(-y_i\). Take \(y_1=1\), which is enough to refute an activation-uniform ambient statement.

For variations of only the first top preactivation, the restricted first loss is

\[
E(z)=\tfrac12(\langle G,\Phi(z)\rangle-1)^2,
\quad \nabla_z E=r(z)G\Phi'(z).
\]
It has a continuous \(L^2\) gradient, but is not locally Lipschitz at the stated base. Fix a small nonzero scalar \(s\) with
\(|\Phi'(z_*+s)-\Phi'(z_*)|\ge c|s|\). Let
\(E_R=\{G>R\}\), \(h_R=s\mathbf1_{E_R}\). Then \(\|h_R\|_2\to0\), while

\[
\|G[\Phi'(z_*+h_R)-\Phi'(z_*)]\|_2
\ge cR\|h_R\|_2.
\]
The residual change is
\((\Phi(z_*+s)-\Phi(z_*))E[G\mathbf1_{E_R}]\). Its contribution to the gradient difference, divided by \(\|h_R\|_2\), tends to zero by Gaussian square-tail integrability. Thus the gradient-to-state difference quotient is unbounded. Embedding through \(h_R\otimes h_1^\#\) changes raw norms only by fixed positive factors and gives the same conclusion for the full network gradient block.

For semiconvexity, take \(E_R=\{G<-R\}\) and the unit direction
\(v_R=\mathbf1_{E_R}/\sqrt{P(E_R)}\). Its second directional derivative is

\[
E''(z_*)[v_R,v_R]
=\big(E[G\Phi'(z_*)v_R]\big)^2
- E[G\Phi''(z_*)v_R^2]
=\big(E[G\Phi'(z_*)v_R]\big)^2
+4B E[G\mid G<-R]\to-\infty.
\]
The first term tends to zero because it is bounded by a constant times \(E[G^2\mathbf1_{G<-R}]\). Hence no finite lower Hessian bound, and no local semiconvexity constant, holds in this ambient raw norm. This refutes importing a generic locally-Lipschitz or semiconvex Hilbert-gradient theorem merely from positivity of \(\Phi'\).

## 8. Source inspection and remaining conclusion

The following actual mathematical sources were inspected, excluding review verdicts:

- `two_sample_activation_design/PROOF.md` and the exact initialized sine formulas;
- `two_sample_odd_activation_theorem/sources/SYMMETRY_RADIAL_CLOCK.md`, including its proof of scalar Frechet C1 regularity, strong path chain rule, radial coercivity, and explicit reached-state continuation gap;
- the fixed-program and local source-response passages of `two_sample_separated_angle_theorem/sources/L3_LOCAL_COMPLETE_PROOF.md`;
- `activation_class_all_depths/BRIDGE.md`, especially Sections V.1--V.5 and V.8--V.9;
- `three_sample_near_identity_all_depths/ENERGY_GALERKIN_ROUTE.md`;
- `practical_fixed_depth2/development/ENERGY_ROUTE.md`, including the Section 7 antecedent of the exponential-tail Osgood optimization;
- the actual two-hidden-layer arctangent theorem and its bounded-readout/natural-coordinate proof mechanism;
- `tanh_depth3_operator_ide/RESEARCH_REPORT_2026-08-22.md`, including its adaptive-transpose and response-hierarchy calculations.

The arctangent two-layer theorem is not applicable: it uses a different depth, a bounded readout increment supplied by a bounded activation, and a scalar natural-coordinate mechanism. The positive derivative of this sine activation supplies an invertible scalar coordinate change, but it neither bounds the readout pointwise nor removes the two-input coupling and repeated Gaussian transposes. No inspected stronger theorem supplies (ET) for the present activation.

There is a rigorous conditional route with an exponential, rather than Gaussian, tail requirement; there is no established unconditional proof of that requirement at the prescribed amplitude. Conversely, the ambient focusing and Hilbert examples above are not reached-state counterexamples, so they do not establish that the desired global limit is false.
