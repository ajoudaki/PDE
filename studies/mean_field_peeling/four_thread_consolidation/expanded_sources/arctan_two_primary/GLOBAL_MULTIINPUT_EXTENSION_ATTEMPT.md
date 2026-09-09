# Global multi-input extension: checked progress and unresolved step

## Status

I have not proved the every-finite-horizon population limit for arbitrary nonorthogonal finite input configurations. The current local arctan proof does not imply it by restart or by the ordinary bounded-state continuation argument. Below is an exact sufficient missing estimate and a proof that it would close the global theorem. This is a conditional result, not an assertion that the estimate has been established.

All statements concern the same two-hidden-layer architecture and scaling as `/tmp/THREE_INPUT_LOCAL_LIMIT_PROOF.md`; replacing three inputs by any fixed finite number only changes constants.

## Bounds already available on every finite horizon

Boundedness of the activation gives, for finite GD, finite flow and population Euler,

\[
|r_{a,k}|\le |y_a|+\|\phi\|_\infty\|W_k^{(3)}\|_\infty,
\]

\[
\|W_{k+1}^{(3)}\|_\infty
\le\|W_k^{(3)}\|_\infty
+C\Delta(1+\|W_k^{(3)}\|_\infty).
\]

For every fixed \(T<\infty\), the resulting geometric sum bounds readout supremum and residuals uniformly for \(k\Delta\le T\). The rank-one matrix update then bounds \(\|W_k^{(2)}\|_{\rm op}\), and the first-layer update bounds root-mean-square velocities and displacements. In particular,

\[
\sup_{\Delta\le1}\max_{a,k:k\Delta\le T}
\mathbb E|P_{a,k}|^2\le C_T,
\qquad P_{a,k}=(W_k^{(2)})^*\delta_{a,k}^{(2)}.
\]

These bounds prevent norm blow-up of the displayed state variables. They do not establish a dimension-independent Lipschitz vector field, a mesh-uniform tail bound, or strong compactness of all needed quadratic measurements.

The problematic difference remains

\[
[\phi'(Z)-\phi'(\widetilde Z)]\widetilde P.
\]

An \(L^2\) bound on \(\widetilde P\) cannot bound its norm by a constant times \(\|Z-\widetilde Z\|_{L^2}\). Multiplication by an unbounded square-integrable random variable is not a bounded operator on \(L^2\).

## A sufficient global estimate weaker than Gaussian tails

The following condition is sufficient: for every fixed \(T<\infty\), there exist \(c_T,C_T>0\) such that

\[
\sup_{0<\Delta\le1}\max_{a,k:k\Delta\le T}
\mathbb E\exp(c_T|P_{a,k}|)\le C_T.
\tag{E}
\]

This is a condition on the already defined finite-mesh population Euler calculations, so it is not circularly assuming existence of a global population flow. Gaussian tails are not needed. Equivalently, it would suffice to prove suitable uniform moment growth \(\|P_{a,k}\|_{L^p}\le C_Tp\) for every \(p\ge2\). Bounds for each fixed moment without control of their growth do not imply (E).

Here is the complete extension argument conditional on (E). Since \(x^2\le C_c e^{cx/2}\) for \(x\ge0\), condition (E) implies

\[
\|P_{a,k}\mathbf1_{|P_{a,k}|>R}\|_{L^2}
\le D_Te^{-a_TR}
\]

for fixed positive \(a_T,D_T\). The localization estimate is therefore

\[
\|[\phi'(Z)-\phi'(\widetilde Z)]\widetilde P\|_{L^2}
\le C_TR\|Z-\widetilde Z\|_{L^2}+D_Te^{-a_TR}.
\]

On a subinterval of length \(h\), the Euler comparison argument gives

\[
\sup d\le
e^{C_T(1+R)h}
\bigl(d_{\rm start}
+C_T(1+R)(\Delta+\Delta')h
+D_The^{-a_TR}\bigr).
\]

Choose a fixed \(h>0\) with \(C_Th<a_T/2\). On the first interval, send both meshes to zero at fixed \(R\), then send \(R\to\infty\). The last term vanishes because its exponent is at most \(-a_TR/2+C_Th\). This proves that population Euler is Cauchy there. On the next interval its initial comparison error tends to zero by the preceding conclusion; the same limit argument applies. A finite partition covers \([0,T]\).

Passage to the integral equations works exactly as in the local proof. Condition (E) passes to the constructed flow by convergence in probability and Fatou. The same subinterval comparison proves uniqueness, using tails only for the constructed reference solution.

For actual GD, fix an oracle mesh and cutoff. The finite-program theorem supplies the oracle sampling errors and empirical tail bounds. Compare actual GD to the oracle on the same finite partition. The extra terms are the original vanishing readout initialization, \(\eta_n\), the coarse mesh, and fixed-mesh sampling errors. Take width to infinity, then mesh to zero, then cutoff to infinity on successive partition intervals. This proves the full joint limit for every \(\eta_n\to0\), on every fixed horizon, conditional on (E). The existing kernel, hidden-velocity and path-law arguments then apply.

This conditional conclusion does not assert positive-definite kernels forever, convergence to zero loss, or convergence as time tends to infinity. It gives existence and approximation on each finite horizon; the earlier strict activity results still concern small positive time.

## Why the present response proof does not establish (E)

The exact response representation is

\[
P_{a,k}=\eta_{a,k}+
\sum_{b,s\le k}A_{ak,bs}H_{b,s}^{(1)}
-2\Delta\sum_{b,s<k}r_{b,s}
\mathbb E[\delta_{b,s}^{(2)}\delta_{a,k}^{(2)}]H_{b,s}^{(1)}.
\]

Its Gaussian variance is bounded on every finite horizon, and the final trained-memory sum is bounded in absolute value by \(C_T\). Thus a sufficient missing response lemma would be

\[
\sup_{\Delta}\max_{a,k:k\Delta\le T}
\sum_{b,s\le k}|A_{ak,bs}|<\infty
\quad\text{for every }T<\infty.
\tag{A}
\]

This would in fact give Gaussian rather than merely exponential tails.

The local proof controls (A) jointly with the forward-response row sums \(\mathcal C_k\) and second-layer derivative sums \(V_k\). It uses

\[
\mathcal C_k\le CT\exp[CT(1+\mathcal A_{k-1})+CT^4],
\]

\[
V_k\le\max\{V_{k-1},1+C_1T(\mathcal C_k+C_0T)V_{k-1}\},
\qquad \mathcal A_k\le C_1TV_k.
\]

The step keeping \(V_k\le2\) explicitly requires a small-time coefficient below \(1/2\). On a general horizon these estimates no longer close. Merely iterating their bounds over \(T/\Delta\) steps can produce mesh-dependent growth. Keeping finer causal dependence gives coupled nonlinear integral inequalities for response kernels; no global bound for them has been proved here. An upper bound resembling \(A(t)\lesssim \exp(C\int_0^t A(s)\,ds)\) would still not suffice, because scalar comparison equations of that type can blow up in finite time.

## Why a naive restart is invalid

At a later time the current fields are correlated with the initial matrix through all previous forward and transpose uses. They are not fresh independent initialization roots. Consequently the independent-initial-root response lemma cannot simply be restarted with the old time reset to zero.

Nor does a tail estimate for \(P(t_0)\) imply a tail estimate for future \(P(t)\) merely because \(\|P(t)-P(t_0)\|_{L^2}\le C|t-t_0|\). An arbitrarily small \(L^2\) perturbation can have arbitrarily heavy tails. A restart proof would have to propagate the relevant derivative-response or exponential-moment control, including the past correlations. That is the missing substantive argument.

The autonomous equations do allow restart along the already constructed interval, because a reference continuation is already known there. This is different from proving existence beyond that interval for an arbitrary correlated endpoint state.

## Other bounds do not fill the gap by themselves

The finite loss identity controls average squared parameter speeds. It does not control exponential moments of individual backward coordinates. Bounded matrix operator norm and bounded coordinate input likewise do not force uniform exponential tails after adaptive reuse.

For example, take an independent first-population event of probability \(\varepsilon\), set \(V=\mathbf1_{\rm event}\), and query \(W_0^{(2)}V\). Its population response is \(\sqrt\varepsilon G_0\), where \(G_0\sim N(0,1)\). Query the transpose on the bounded vector \(U=\arctan(G_0)\), which can be formed by applying the fixed-for-\(\varepsilon\) function \(s\mapsto\arctan(s/\sqrt\varepsilon)\) to the forward response. Gaussian regression gives

\[
(W_0^{(2)})^*U
=\Gamma+\frac{c}{\sqrt\varepsilon}\mathbf1_{\rm event},
\qquad c=\mathbb E[G_0\arctan(G_0)]>0,
\]

where \(\Gamma\) is a Gaussian independent of the first-population event, with bounded variance. Both query inputs are uniformly bounded and the initial operator is bounded on \(L^2\), yet no common exponential-moment bound holds as \(\varepsilon\to0\). This is not a counterexample to the trained arctan dynamics: the nonlinear query used here has derivative of size \(\varepsilon^{-1/2}\). It demonstrates why additional derivative control, rather than operator and amplitude bounds alone, is essential.

The identity \(|\phi''(z)|\le\phi'(z)\) for arctan can improve a pointwise derivative coefficient from \(|P|\) to \(|\phi'(Z)P|\), a first-layer backpropagation scale. For nonsingular \(G\), the corresponding residual-weighted quantities are controlled by coordinate velocities using \(G^{-1}\); this particular reduction cannot be used unchanged when \(G\) is singular. Even in the nonsingular case, the existing energy bound is only mean-square integrated in coordinates. It does not yet control the exponential of that coordinatewise accumulated scale; no complete uniqueness/global-extension argument follows from this improvement alone.

## Checked external route

The noiseless global theorem in Nishiyama and Imaizumi, *High-Dimensional Limit of Stochastic Gradient Flow via Dynamical Mean-Field Theory*, arXiv:2602.06320, builds on a framework of the form

\[
\dot\theta=-h_t(\theta)-X^\top\ell_t(X\theta),
\]

with globally Lipschitz coordinate maps and derivatives (see its Assumption 2 and Theorem 1). It is not directly a theorem for the present multiplicative first-layer gate and trained middle matrix. Its hypotheses do not eliminate the problematic product displayed above. I have not obtained a verified external theorem that fills this gap.

Primary source: https://arxiv.org/html/2602.06320v1

## Bottom line

The existing proof establishes the local multi-input theorem. Every-finite-horizon multi-input convergence is rigorously reduced to a mesh-uniform exponential backward-moment bound such as (E), or the stronger response bound (A). Neither bound has been established globally here. Thus the arbitrary-input global theorem remains unproved by this attempt; global finite-width existence, bounded loss and bounded population state norms do not justify claiming it.
