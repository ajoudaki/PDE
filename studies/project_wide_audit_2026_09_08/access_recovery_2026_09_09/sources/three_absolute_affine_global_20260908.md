# Fixed affine reference a=b=1: global existence, exact balance defects, and convergence obligations

2026-09-08. Independent theoretical check for the newly authorized family

\[
 \phi_\theta(z)=(1-\theta)(a z+b)+\theta\arctan z,
\]

with a,b absolute positive constants. The calculations below take a=b=1. There are three hidden layers, all four original raw parameter blocks are trained, the canonical population readout is zero initially, and every three-input configuration with |Gamma_ij|<=1-delta and every binary label vector is retained. Old files were preserved and no trajectory experiment was run.

**Result:** global strong affine GF on every finite physical interval is elementary in the original raw Hilbert space. I also obtain an exact full-kernel lower bound in the augmented input Gram whenever the bottom incoming field is nonzero, and classify every stationary predictor: it either fits, is zero, or is the best constant predictor. But I do not obtain a uniform bounded affine trajectory and finite residual-L1 clock for all admissible triples. Standard augmentation changes the training metric/constraints; the usual homogeneous balance identities acquire explicitly nonzero bias terms. The closest primary global convergence theorem does not directly cover these fixed offsets, this depth, and the zero-readout population initialization.

## 1. Exact model, and an unconditional global affine construction

Use normalized inputs u_i=x_i/sqrt(d), and identify the first layer with a linear map W from their finite-dimensional span V into H_1, in the metric where ||dW||_HS is the original first-layer raw norm restricted to V. Initially W_0 is a Gaussian isometry on V, in the canonical population sense. Write e_ell for the constant-one vector in H_ell; each has norm one. The affine features are

\[
 H_{1i}=e_1+Wu_i,
 \quad H_{2i}=e_2+A H_{1i},
 \quad H_{3i}=e_3+B H_{2i},
 \quad f_i=\langle C,H_{3i}\rangle.
                                                               \tag{1}
\]

The current actions A and B are initialized bounded actions plus Hilbert-Schmidt changes. The state consisting of W-W_0, A-A_0, B-B_0 and C is a raw Hilbert space. The predictor and its raw gradient are polynomial maps on it, locally Lipschitz on bounded balls. Initialized action norms are at most 10; ||W_0||_HS^2=dim(V)<=3; C_0=0.

Let L=(1/2)||f-y||_2^2. Standard local ODE theory gives a unique strong affine GF. Its exact energy identity yields

\[
 \int_s^t\|\dot\Theta(\tau)\|_{raw}^2d\tau
       =L(s)-L(t)\le L(0)=3/2,
\]

\[
 \|\Theta(t)-\Theta(s)\|_{raw}
       \le\sqrt{(t-s)(L(s)-L(t))}
       \le\sqrt{3(t-s)/2}.                                   \tag{2}
\]

If its maximal endpoint T were finite, (2) would give a strong reached state as t approaches T, lying in the finite ball of radius sqrt(3T/2). Local existence there extends the solution, a contradiction. Thus the affine raw strong flow exists uniquely for all finite t. Its finite-T radius and action bounds depend only on T, the initialized bounds, and sample count. This argument does not require separation or a gain growing with delta.

This is an actual construction for theta=0. It is not a positive-theta source-tail construction. In particular the bound sqrt(3T/2) does not control the whole infinite-time path, and energy dissipation does not imply integral_0^infinity ||r||_1<infinity.

The same polynomial local Lipschitz bounds give ordinary uniform-mesh Euler comparison on every bounded physical interval. Canonical affine fixed-program/strong-limit construction and actual-adjoint identities therefore have a direct finite-T route. They do not turn the positive-theta controlled-source smallness condition into a horizon-independent one.

## 2. Full tangent kernel and a useful exact augmented-Gram lower bound

Put r=f-y,

\[
 g=\sum_i r_i u_i,\quad s=\sum_i r_i,\quad
 q_2=B^*C,\quad q_1=A^*q_2.
\]

The raw equations are

\[
 W'=-q_1\otimes g,\quad
 A'=-q_2\otimes(Wg+s e_1),
\]

\[
 B'=-C\otimes[A(Wg+s e_1)+s e_2],
\quad C'=-\{B[A(Wg+s e_1)+s e_2]+s e_3\}.                    \tag{3}
\]

For any fixed sample coefficient vector v, let d_v=sum_i v_i u_i and s_v=sum_i v_i. The complete kernel satisfies exactly

\[
\begin{aligned}
 v^TKv={}&\|q_1\|^2\|d_v\|^2
 +\|q_2\|^2\|Wd_v+s_v e_1\|^2\\
 &+\|C\|^2\|A(Wd_v+s_v e_1)+s_v e_2\|^2\\
 &+\|B[A(Wd_v+s_v e_1)+s_v e_2]+s_v e_3\|^2 .
\end{aligned}                                                \tag{4}
\]

In particular, with M=||W||_op,

\[
 s_v^2\le2\|Wd_v+s_v e_1\|^2+2M^2\|d_v\|^2.
\]

Consequently

\[
 K\succeq\min\left\{\frac{\|q_1\|^2}{1+2M^2},
                           \frac{\|q_2\|^2}{2}\right\}
                     (\Gamma+11^T).                         \tag{5}
\]

Since ||q_1||<=||A|| ||q_2||, a slightly weaker convenient version is

\[
 \boxed{\quad K\succeq
 \frac{\|q_1\|^2}{1+2\|W\|^2+2\|A\|^2}(\Gamma+11^T).
 \quad}                                                       \tag{6}
\]

To verify (6), the coefficient in its denominator is at least 1+2M^2 and at least 2||A||^2; compare separately with the two terms in the minimum in (5). The assertion is also valid when q_1=0.

For separated unit triples, Gamma+11^T >= (delta^2/4)I by the elementary three-input geometry lemma. Thus a lower bound on the evolving q_1, together with controlled W and A, would give a genuine full-kernel gap including the previously null direction. Equation (6) uses the evolving first layer and actual adjoints; it is not a frozen-feature estimate.

The effective affine predictor has the form

\[
 f(u)=\langle W^*q_1,u\rangle+\beta_0,
 \qquad \beta_0=\langle q_1,e_1\rangle
                  +\langle q_2,e_2\rangle+\langle C,e_3\rangle.
                                                               \tag{7}
\]

A quantitative nonzero linear predictor therefore gives ||q_1||>=||W^*q_1||/||W||. The issue is ensuring this on the required global path; a decrease of loss below its initial value alone can be due to the intercept in (7).

## 3. Homogeneous augmentation fails as a dynamical identification

A hidden affine layer can be written algebraically as

\[
 \begin{pmatrix}H_{\ell}\cr1\end{pmatrix}
 =\begin{pmatrix}A_\ell&e_\ell\cr0&1\end{pmatrix}
                 \begin{pmatrix}H_{\ell-1}\cr1\end{pmatrix}.
                                                               \tag{8}
\]

But in the original problem the last column and last row in (8) are fixed. Ordinary deep-linear GF trains those entries and changes the metric. The original flow is a constrained block-projected gradient flow of that augmented product. Removing the projection is not a harmless reparameterization.

One can see the failure directly without invoking a theorem. Equations (3) imply the following operator identities:

\[
 \frac d{dt}(A^*A-WW^*)
       =-s(q_1\otimes e_1+e_1\otimes q_1),
\]

\[
 \frac d{dt}(B^*B-AA^*)
       =-s(q_2\otimes e_2+e_2\otimes q_2),
\]

\[
 \frac d{dt}(CC^*-BB^*)
       =-s(C\otimes e_3+e_3\otimes C).                         \tag{9}
\]

These are exact identities of bounded operators with differentiable Hilbert-Schmidt changes. In the first identity, A^*A has the extra term -s(q_1 tensor e_1+e_1 tensor q_1), whereas WW^* does not. The other two follow by the identical cancellation at their respective layer.

Thus ordinary balancedness is false unless the residual sum vanishes identically. This is not the case initially for three binary labels: sum_i y_i is ±1 or ±3.

There is a nontrivial surviving statement. Let P_ell=I-e_ell tensor e_ell. The compressions

\[
 P_1(A^*A-WW^*)P_1,\quad
 P_2(B^*B-AA^*)P_2,\quad
 P_3(CC^*-BB^*)P_3                                      \tag{10}
\]

are conserved. This controls the action parts away from the constant directions. For example,

\[
 \|AP_1\|^2\le\|W\|^2+
       \|P_1(A_0^*A_0-W_0W_0^*)P_1\|.
                                                               \tag{11}
\]

It does not control A e_1, B e_2, or their coupled mean components. Those are exactly the additional variables introduced by fixed offsets. A proof using (10) must also bound them.

## 4. Classification of all affine stationary predictors

This gives a sharper convergence target than an unspecified saddle issue.

**Lemma.** Suppose Gamma+11^T is positive definite. At every stationary raw state of (1), either f=0, f=y, or f=(mean y)1.

**Proof.** If C=0, then f=0. Suppose C is nonzero. Stationarity of B in (3) gives H_2 r=0. Stationarity of C then yields

\[
 0=H_3r=B H_2r+s e_3=s e_3,
\]

so s=0. If q_1 is nonzero, stationarity of W gives g=0. Positive definiteness of Gamma+11^T implies r=0 from ||g||^2+s^2=0. If q_1=0, (7) shows that f is constant; since s=0 its value is mean y. This proves the alternatives.

For three binary labels, the stationary loss levels are consequently:

- 0 at interpolation;
- 3/2 when f=0;
- 0 if all labels agree, or 4/3 for the best constant predictor when labels are mixed.

At canonical initialization K(0)=Gamma+3(11^T), since the three initialized affine feature Gram recursions each add 11^T. The kernel is positive definite, so the initial loss decreases strictly. This excludes a bounded convergent trajectory from ending at the zero-predictor level. For mixed labels, a proved crossing below loss 4/3 would exclude every nonoptimal stationary predictor. Such a crossing has not been proved here, nor has global boundedness.

The best-constant stationary points actually exist in the architecture, so they cannot be omitted from a general theorem. Take A=B=0, C=(mean y)e_3, and arbitrary W. Then H_2=H_3=e, the residual sum is zero, and every block in (3) vanishes. For mixed labels the loss is 4/3. This is not canonical Gaussian initialization and is not a counterexample to its convergence; it demonstrates why a global PL claim for all affine states cannot follow from separation alone.

## 5. What the primary global-convergence theorems do establish

Chizat--Colombo--Fernandez-Real--Figalli, *Infinite-width limit of deep linear neural networks*, Theorem 2.3 and Proposition 5.5, prove exponential convergence for a particular unbalanced muP limit. Their proof obtains a nonzero effective predictor after an initial loss decrease, bounds the first-layer squared norm by a constant plus the integrated residual norm, and bootstraps a time-dependent coercivity inequality to exponential decay. This is directly relevant machinery. The rigorous principal model has two hidden layers and a nonzero Gaussian readout in its coefficient system. Section 6 explicitly labels its arbitrary-depth development formal. Fixed hidden offsets are absent. [Primary author-hosted paper](https://people.math.ethz.ch/~afigalli/papers-pdf/Infinite-width-limit-of-deep-linear-neural-networks.pdf), equations (5.17)--(5.23), Section 6.

The predictor-norm bootstrap is a plausible method to extend, but (7)--(9) show the exact changes needed here: a nonzero intercept does not force nonzero q_1, and the fixed offsets add uncontrolled constant-direction terms. Its theorem cannot be quoted as already proving the required reference.

Bah--Rauhut--Terstiege--Westdickenberg, *Learning deep linear neural networks: Riemannian gradient flows and convergence to global minimizers*, Theorem 5, proves global boundedness and convergence to a critical point for unconstrained finite-dimensional homogeneous matrix factorizations under a full-rank data condition. Theorem 38 gives almost-everywhere conclusions, with the possible rank of the limiting optimum not generally identified for depth at least three. Its hypotheses do not cover the constrained matrices (8), infinite initialized action norm in Hilbert-Schmidt topology, or a deterministic canonical limit with exactly zero readout. [Primary full text](https://arxiv.org/html/1910.05505v4), Theorems 5 and 38.

Du--Hu, *Width Provably Matters in Optimization for Deep Linear Neural Networks*, Theorem 4.1, proves a strong Gaussian-initialized wide-network convergence statement, but its equation (1) and update (2) use unscaled iid Gaussian parameters with one common Euclidean learning rate, and its readout is an ordinary nonzero Gaussian factor. The original normalized-action raw metric becomes layer-dependent after that reparameterization; the reference here also has fixed offsets and zero limiting readout. Therefore its theorem does not yield the desired maximal-update affine GF by simply sending width to infinity. [Primary conference paper](https://proceedings.mlr.press/v97/du19a/du19a.pdf), Section 3.2 and Theorem 4.1.

An almost-sure finite-width saddle-avoidance assertion alone would also not supply a width-uniform time, radius, or canonical-limit statement. These must be checked rather than inferred from the word Gaussian.

## 6. Exact status for the positive-theta goal

For a=b=1, the affine global strong flow itself is now completely justified by (1)--(3), and the augmented-Gram coercivity (5)--(6), compressed balances (10), and stationary-level classification are concrete additional structure.

What is still required to use this as a horizon-independent controlled-source reference is a uniform-in-geometry-at-fixed-delta bound on the affine raw trajectory and its residual-L1 clock. The elementary finite-T energy bound does not establish it. No primary theorem checked has all the necessary hypotheses. The classification in Section 4 makes the mixed-label bottleneck precise: boundedness and escape below the best-constant loss level would eliminate nonoptimal stationary limits, but they remain proof obligations.

Accordingly this note is not a completed positive-theta theorem, and it does not claim that the new fixed-offset family fails. It identifies a more favorable reference problem and supplies exact lemmas for an attempted completion.
