# Noiseless SGF theorem: exact applicability boundary

Source checked: Nishiyama--Imaizumi, [arXiv:2602.06320v2](https://arxiv.org/html/2602.06320v2), Section 2, Assumptions 2.1--2.2, and Theorem 3.1.
This is a targeted applicability check, not a review of the entire paper.

Their channel dimension \(m\) is fixed. The trained array is
\(\theta\in\mathbb R^{d\times m}\), and one fixed random data matrix
\(X\in\mathbb R^{n\times d}\) supplies the two actions
\[
r=X\theta,\qquad
\dot\theta=-h_t(\theta)-\delta^{-1}X^\top\ell_t(r;z)
\]
in the noiseless case. The rowwise functions and specified derivatives
must satisfy the common Lipschitz bounds of Assumption 2.2.
Theorem 3.1 genuinely gives global existence and uniqueness when the
noise parameter is zero. It is not merely a local theorem in that case.

These premises do not directly encode the present network. Here two
trained hidden matrices enter nested forward and backward passes.
Expanding them into initialization plus updates introduces evolving
history contractions; it does not make the resulting dynamics one
fixed-channel rowwise function of \(X\theta\). Moreover, smoothness of
arctangent alone does not verify the needed uniform query derivative:
\[
\frac{\partial}{\partial z}
\left[\phi'(z)\odot b\right]
=\operatorname{diag}\!\left(\phi''(z)\odot b\right).
\]
An average-square bound on \(b\) does not bound this matrix in operator
norm uniformly in width.

Conclusion: no direct invocation has been established. A reduction or
extension proving those missing properties would be additional work.
This is neither a literature-wide exclusion nor a counterexample to the
canonical three-hidden-layer theorem. No experiment was performed.
