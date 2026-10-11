# Adversarial audit: dynamical low-rank training

Source: Schotthöfer et al., *Low-rank lottery tickets*, NeurIPS 2022, published main pp. 1–13 and supplement pp. 14–23. This root reconstruction reread both in full; it is a second check, not a blind review of the earlier REDUCTIONS report. No code or experiment was rerun.

## What is genuinely established and assumed

The geometric construction is substantive: replace the full matrix gradient by its tangent projection on a rank manifold, and integrate the factors using a basis-update/Galerkin method robust to small singular values. Factors, rather than full matrices, suffice for its updates. For square width n and rank r, retained factors cost O(nr+r²) per layer; QR work costs O(nr²), besides minibatch gradient work. Rank adaptation does not prove that r remains small.

The indispensable approximation assumption is supplement P2, p.14: the normal component of the *full* gradient field is at most ε near the reference trajectory. It is not derived for ordinary randomly initialized deep-network training. P1 requires bounded and Lipschitz gradient fields; despite the prose saying “locally,” its displayed quantifiers range over all matrices. Such bounds are not automatic for common deep networks globally. A bounded invariant region would be a legitimate additional route, but is not supplied here.

Theorem 1 further assumes exact integration of the three factor substeps. The numerical experiments also use Euler and Adam. The geometric error theorem cannot be quoted without those numerical qualifications. The source treats one layer with other matrices as parameters; extension to jointly changing layers needs a coupled-field estimate, not merely separate constants at fixed other layers.

## Confirmed missing time dependence in Theorem 1

Main p.5 says the three global error constants depend only on the boundedness and Lipschitz constants, not on terminal time. Supplement p.16 obtains the global error by ordinary Lipschitz accumulation of the local error. That argument supplies a factor depending on the terminal time, generally (exp(C₂T)−1)/C₂, rather than an all-time bound.

This is independently confirmed by its own cited dependency: Ceruti–Lubich, *An unconventional robust integrator for dynamical low-rank approximation*, arXiv:2010.02022, Theorem 2 p.4 explicitly includes T in the constants and restricts the step times to at most T; Theorem 4 p.6 imports that bound verbatim. The relevant theorem statements and §3.4 proof were inspected directly. This dependency was checked selectively, not claimed as a full-paper audit. The two DLRT main statements were also checked in the rendered PDF.

The problem is not just a loose reconstruction. Here is a smooth bounded-gradient counterexample to the printed time-independent reading, within the abstract matrix hypotheses used by its proof. Write E₂₂ for the matrix with a single 1 in position (2,2), and start both flows from diag(1,0). Use the nonnegative loss

\[
\mathcal L(W)=\varepsilon\log\cosh(1-W_{22}),\qquad
F(W)=\varepsilon\tanh(1-W_{22})E_{22},\quad 0<\varepsilon\le1.
\]

Its gradient field is globally bounded and Lipschitz with common bounds 1, independent of ε. P2 holds everywhere with bound ε, since an orthogonal projection cannot increase the norm. At the rank-one starting matrix the field is entirely normal. Both K and L substeps are constant, so the new spaces in Algorithm 1 remain span(e₁); the S substep is also constant. This remains true with basis augmentation, when “basis for the range” in lines 11 and 13 is read literally. The algorithm therefore remains at diag(1,0), with zero truncation error. An implementation that arbitrarily completes a rank-deficient QR to a larger space is a different choice; the fixed-rank version has no such ambiguity.

The full gradient flow is diag(1,a(t)), where

\[
a(t)=1-\operatorname{arsinh}\!\left(e^{-\varepsilon t}\sinh 1\right).
\]

At T=ε⁻¹ log(sinh(1)/sinh(1/2)), the matrix error is 1/2. Taking step size η=ε and the closest grid time changes this error by at most ε². The claimed bound with constants depending only on the common field bounds would instead be O(ε). Thus terminal-time dependence cannot be omitted. This does **not** invalidate the usual finite-horizon low-rank integrator theorem; it invalidates treating the printed bound as an infinite-horizon one.

## Confirmed overstatement in Theorem 2

Main p.5 asserts positive descent constants independent of iteration and step size. Supplement p.17 actually defines the descent coefficient as the minimum projected-gradient norm over the current substep. It depends on the current state and may be zero. At a stationary point, a strictly positive uniform descent coefficient is impossible, even for zero truncation tolerance. The valid conclusion is descent by the integral of the squared projected gradient, up to the truncation error. This repair preserves a useful result, but not the printed uniform positive decrement.

Supplement §6.4 also identifies a stationary tangent projection with an optimal low-rank network minimizing the full gradient norm. The variational principle minimizes over tangent **velocities at a fixed matrix**; it does not minimize over matrices. No global low-rank optimality follows from it. This is an unsupported interpretation, not needed for the factor algorithm.

## Empirical evidence and its limits

The experiments provide meaningful task-accuracy and runtime evidence, including deep networks and ImageNet. They do not measure a same-initialization predictor-path error against independent dense-seed variability. Supplement p.18 explicitly counts training parameters using *converged* ranks and notes larger counts in early epochs; those tables are not peak-memory guarantees. Table 3 also shows rank choices at which the method is slower than dense training. These qualifications should accompany practical claims, not erase the successful results.

## Positioning consequence

This is a genuine predecessor for compressed nonlinear training and deserves prominent citation. Its conditional geometric theorem assumes the small normal defect that makes low-rank shadowing possible, and its proof is finite-horizon. It does not derive a width-dependent rank sufficient for a canonical dense trajectory, a polylogarithmic retained state, a fitted-limit prediction guarantee, or a comparison below actual dense-run discrepancy. Our comparison should emphasize deriving compressibility and controlling accumulated errors, not claim that autonomous compressed nonlinear training was previously absent.
