# Linear physical-time final audit 03

**Provenance:** final clean-room referee; no repository access and no
communication with other agents. It received only the strengthened common
physical-time theorem after feature-globality had been removed.

**Date:** 2026-08-24  
**Verdict:** **accept**.

The referee independently verified the following substantive leaves.

1. With
   \((b\otimes_nx)z=b\langle x,z\rangle_n\), the rank-one Frobenius,
   Hilbert--Schmidt, and nuclear norms all equal
   \(\|b\|_n\|x\|_n\). Thus finite and Fock updates have identical
   scaling.
2. The residual energy gives
   \[
    \int_0^T e^2K\,dt\le e(0)^2/(4\eta),\qquad
    \int_0^T\|\dot\theta\|\,dt
       \le |e(0)|\sqrt{\eta T}
   \]
   for every endpoint or matrix block. This supplies global physical-time
   continuation and the common high-probability localization balls.
3. Fixed Picard iterates remain in the finite algebra of rooted source-word
   vectors and rank-one tensors. Every fixed contraction is a continuous
   function of finitely many rooted Grams; finite slab composition and
   same-space Picard tails avoid every cross-width vector subtraction.
4. At fixed depth, \(K\) and all forward/backward products are uniformly
   Lipschitz on localized endpoint/trace-norm balls, using
   \(\|P\|_{\rm op}\le\|P\|_1\).
5. If \(h=\dot P\) has trace-norm Lipschitz constant \(L\), the \(N\)-cell
   left-Riemann integral has rank at most \(N+1\) and trace error at most
   \(LT^2/(2N)\). The nuclear best-rank identity and finite-factor Gram
   continuity close the uniform trace-tail claim.
6. The probability order is legitimate: localize first, choose deterministic
   Picard/Riemann accuracies on that ball, invoke finite-Gram convergence,
   and then remove the localization error.

The only requested manuscript additions were definitions of the finite
prediction, normalized outer product, and the continuous grammar of a
compiled signature. The first two already appear in the parent research
contract; the theorem's rooted-action topology supplies the third. These
are definitional clarifications, not missing mathematical lemmas.

The acceptance is specifically for autonomous physical time. It does not
reverse the separately proved finite-feature-time blow-up at \(H\ge2\).
