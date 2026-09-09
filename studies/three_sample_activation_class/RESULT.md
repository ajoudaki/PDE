# The activation-class extension

For the three-input, three-hidden-layer model in the complete manuscript, arctangent can be replaced by any nonconstant bounded function with two continuous bounded derivatives, after normalization and with a sufficiently small positive amplitude.

More precisely, suppose
\[
\|\psi\|_\infty,\ \|\psi'\|_\infty,\ \|\psi''\|_\infty\le1,
\qquad \psi\in C^2(\mathbb R),\qquad \psi\text{ nonconstant}.
\]
For each separation \(\delta>0\), the manuscript gives finite explicit constants \(a_{\delta,\psi}\ge2\) and \(e_{\delta,\psi}>0\) such that every fixed activation
\[
\phi(z)=a_{\delta,\psi}(1+z)+e\psi(z),\qquad 0<e\le e_{\delta,\psi},
\]
works for every fixed admissible input triple with normalized pairwise cosine at most \(1-\delta\) and binary labels. Thus it also covers the requested interval \((-1+\delta,1-\delta)\). The extra lower bound on cosine is unnecessary for this theorem.

The result includes global canonical population gradient flow with the stated uniqueness and continuation, joint compact-time limits for actual finite gradient flow and raw gradient descent, all four true kernel blocks, hidden path and velocity laws, persistent nonaffinity, nonzero initial motion in every hidden parameter block and every sample/layer field, and variation of the projected total kernel. Precise initialization, metric, observables and quantifiers are in Theorem M.1. Width convergence is for each fixed dataset and finite observation horizon.

The activation is an affine function plus the small bounded perturbation. The result does not remove the separation-dependent gain or establish the same theorem for a bounded activation used alone.

## Why the broader class works

The analytic estimates use only absolute bounds on \(\psi,\psi',\psi''\). Neither oddness nor monotonicity of the perturbation is needed. The full activation has \(\phi'\ge a/2>0\).

For a centered Gaussian triple of common marginal variance \(v\) and covariance \(Q\), project the features onto constants and Gaussian linear functions. The projected feature is
\[
\bigl(a+eE\psi(\sqrt vG)\bigr)
+\bigl(a+eE\psi'(\sqrt vG)\bigr)Z_i.
\]
Both coefficients are at least \(a/2\). Its residual is orthogonal to the projection, so the new feature Gram is at least \((a^2/4)(\mathbf1\mathbf1^T+Q)\). Three iterations, together with the elementary separated-triple bound, give
\[
K^4(0)\succeq \frac{\delta^2a^6}{256}I_3.
\]
This works even when the input Gram is singular.

Persistent nonaffinity needs a separate argument because a localized bounded function can lose its Gaussian regression margin as variance tends to infinity. Choose an interval \([-r,r]\) on which \(\psi\) has positive squared distance \(J\) from affine functions. Such an interval exists because a bounded nonconstant function cannot be globally affine. A lower bound for the Gaussian density on this interval gives
\[
\inf_{\alpha,\beta}E[\psi(\sigma G)-\alpha-\beta\sigma G]^2
\ge \frac{e^{-r^2/2}J}{\sqrt{2\pi}\sigma}
=\frac{c_\psi}{\sigma},\qquad \sigma\ge1.
\]
The three initialized standard deviations lie in \([1,5a^2]\). The resulting regression margin is therefore at least \(c_\psi/(5a^2)\). Its square root is stable under an \(L^2\) perturbation with a loss at most three times that perturbation's size. The controlled training argument bounds preactivation displacement by a constant times \(\delta^{-4}a^{-4}\). An explicit cubic lower bound on \(a\) makes this smaller than the permissible displacement, which is proportional to \(a^{-1}\). This closes the parameter selection without using any unknown trained trajectory.

Consequently every sample and hidden layer satisfies the all-time bound
\[
\inf_{t\ge0}\inf_{\alpha,\beta}
E[\phi(z_i^\ell(t))-\alpha-\beta z_i^\ell(t)]^2
\ge\frac{e^2c_\psi}{20a^2}>0.
\]
The remaining global, finite-algorithm and observation arguments are fully supplied in the manuscript, with the generalized gates and the explicit response constant chain. The initial-motion proof uses the positive full gate and \(\psi''\not\equiv0\), which is automatic for bounded nonconstant \(\psi\).

## Uniform function classes

There are also whole infinite-dimensional neighborhoods for which one shared \(a_\delta,e_\delta\) works and the nonaffinity coefficient is independent of \(\delta\). For example, start with \(\psi_0=\tfrac14\arctan\). Its Gaussian regression margin has a positive infimum over \(\sigma\ge1\). Distance to the affine regression subspace is 1-Lipschitz in the target function, so every sufficiently small \(C_b^2\) perturbation of \(\psi_0\) retains a common positive margin. This includes nonodd, nonmonotone perturbations with oscillatory tails. Part A provides the complete proof and common constant recipe.

Normalized \(\tanh z\), \(\sin z\), \(\cos z\), \(e^{-z^2}\), and any nonzero compactly supported \(C^2\) function are examples in the broad class.

Read [MANUSCRIPT.md](MANUSCRIPT.md) for the full self-contained theorem and proof, including every specialized dependency and explicit constant choice. This short account describes the proof's main new arguments; it does not replace that detailed proof.
