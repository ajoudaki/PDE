# Audit: efficient computation of the projected infinite-width limit

Public source: Yang, Santacroce and Hu, *Efficient Computation of Deep Nonlinear Infinite-Width Neural Networks that Learn Features*, ICLR 2022, [official record](https://openreview.net/forum?id=tUMr0Iox8XW). The user supplied the complete 24-page proceedings PDF. The coordinator read every page, including Appendices A–F; two separately scoped readers checked the construction and costs. This closes the PDF-access gap in the initial REDUCTIONS report. No code was executed or training reproduced. This is a source audit, not a new audit of our manuscript.

## Exact object and assumptions

The method changes **both initialization and optimization**. It does not derive low rank for an ordinary iid-Gaussian dense network. For a fixed Gaussian matrix \(\Omega\in\mathbb R^{n\times r}\), its hidden matrices have the form

\[
W^{(\ell)}=n^{-1}\Omega A^{(\ell)\top}\phi(B^{(\ell)}\Omega^\top).
\]

Thus their rank is at most \(r\), and hidden preactivations lie in the column space of \(\Omega\). Initial matrices \(A,B\) have a fixed row count, denoted \(M\) in the paper. The optimizer explicitly projects each hidden update back into that space. These are structural choices, not an assumption subsequently proved to hold along unrestricted dense SGD. Appendix A allows biases, minibatches, learning-rate multipliers and untied Gaussian matrices without removing that distinction.

Theorems 3.4–3.5 assume a polynomially bounded second derivative of the activation and an appropriately differentiable loss. For a fixed training routine of finitely many updates, fixed \(r,M\), width-independent learning rates, and a fixed query, the output converges almost surely as \(n\to\infty\). Constants/rates uniform in a growing number of updates are not supplied. The theorem is conditional on the finite coefficient initialization; drawing those coefficients randomly leaves finite-dimensional randomness in the limit. Exact ReLU experiments do not literally satisfy the stated classical second-derivative hypothesis.

## Mechanism, reconstructed

Write \(h^{(\ell)}=\Omega g^{(\ell)}\). Gaussian averaging reduces each forward layer to evaluations of the two-variable Gaussian activation kernel \(V_\phi\), followed by multiplication by \(A^{(\ell)\top}\). For ReLU these expectations have familiar closed forms; for a general activation numerical integration is an additional resource, not automatically unit cost.

At a finite width, let \(G_n=\Omega^\top\Omega/n\). The exact projected backpropagation relation is

\[
n\Pi_\Omega\nabla_h\mathcal L
=\Omega G_n^{-1}\nabla_g\mathcal L,
\]

when \(\Omega\) has full column rank. The law of large numbers gives \(G_n\to I\). This explains why the limiting projected gradient becomes an ordinary coefficient gradient. Each example then adds a rank-one source: append the backward coefficient to \(A\), append the forward coefficient to \(B\). The first-layer coefficient is instead updated by accumulation. The appended old rows remain frozen. The source's tensor-program argument provides the fixed-program convergence; it does not prove a canonical-dense-to-projected approximation.

This is a substantial simplification of a **different feature-learning limit**. It should neither be dismissed as a frozen-kernel method nor described as a proved compressor of the usual deep Gaussian reference. The paper itself says similarity to the unprojected maximal-update limit at large \(r\) is a belief motivated by experiments, not a theorem.

## Retained state and work, with the growing history exposed

Use \(L\) for the number of hidden layers, \(d\) for input dimension, and \(d_{\rm out}\) for output dimension. After \(T\) batches of size \(S\), the displayed bias-free arrays contain

\[
dr+(M+ST)\bigl[(2L-1)r+d_{\rm out}\bigr]
\]

real coefficients. Biases add \(Lr+d_{\rm out}\). This count includes the frozen appended history: freezing a row does not remove its storage or its role in future evaluation. It is independent of the original width, but grows **linearly with the number of training examples processed**.

With unit-cost scalar kernel evaluation, a batch at update \(t\) requires work of order

\[
S\{dr+(M+St)[(2L-1)r+d_{\rm out}]\},
\]

and a new query uses the same expression without the initial factor \(S\). Summing over updates gives quadratic-in-\(T\) work. The shallow discussion on p. 4 explicitly states linear-in-\(T\) memory and quadratic-in-\(T\) time. These are derived array counts, not lower bounds against all conceivable implementations. No certified compression of this appended history is supplied.

## Proof and experiment findings

The main finite-step construction and projected-gradient mechanism survive the checked reconstruction. Appendix F.1 prints an ill-typed identity equating a Hilbert-space projected gradient to a coordinate-space gradient: a factor \(\Gamma\) is missing. Its proof also prints a minimum where an argmin is required. The repaired identity is \(\Pi_V\nabla\mathcal L(\Gamma b)=\Gamma\nabla_b\mathcal L(\Gamma b)\); the chain rule establishes it directly. These are localized repairable errors, not evidence against the limit theorem. A shallow projection normalization and one readout normalization also require care when copying formulas literally; the general coordinate derivation above is the consistent version.

Table 1 selects best test accuracies over architectures and hyperparameters: CIFAR10 61.50% for the limit versus 61.31% for the finite maximal-update network; Omniglot 91.46% versus 91.22%, while the finite projected network reaches 92.21%. These results support a useful feature-learning computational model, but do not establish universal superiority or prediction-level fidelity to a particular dense seed. Small differences need uncertainty estimates before being treated as decisive. Reported two-hidden-layer seconds per epoch are 160.99 versus 7.72 on CIFAR10 and 313.4 versus 32.38 on Omniglot for infinite projected versus ordinary finite maximal-update training. Width removal is therefore not synonymous with practical speedup in these reported configurations.

## Verdict and positioning

High confidence in the model change, update mechanism, explicit state growth, and fixed-horizon quantifiers. The tensor-program master theorem is a dependency, not re-proved here; a separate TP audit checks its applicable statement. Experiments were read, not reproduced.

The strongest contrast is: **this work makes a deliberately projected infinite-width feature learner computable; our manuscript claims a bounded retained state that shadows an ordinary finite dense reference throughout fitting.** No theorem here equates those two reference systems, lets \(r\to\infty\) recover the ordinary limit with a quantitative rate, truncates the growing history, or bounds error against actual independent dense-run discrepancy. Those are major substantive differences in what is established, not minor notational qualifications or evidence of misconduct.
