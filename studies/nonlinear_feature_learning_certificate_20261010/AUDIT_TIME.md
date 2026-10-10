# Audit of the fixed-time passage

Date: 2026-10-10. Scope: a fresh audit of the complete
`COMPATIBLE_RESULT.md`, concentrating on the passage from initialization
coefficients to fixed-time feature displacement, nonlinear affine-fit error,
and departure from the frozen initial tangent kernel. The Gaussian
backward-response positivity assertion is an input to the focused repair
below, not independently certified by this report.

Sources inspected: the complete candidate and `paper/compact.tex`; the
analytic-domain statement in `paper/compact_foundations.tex`; the local
population theorem C.1, relevant activity calculations in C.3, and the
directional-chain-rule argument in the three-hidden-layer activity section
of `docs/03-local-population.qmd`; and `docs/notation.qmd`. No other study or
prior verdict was consulted. The required rigorous-math and canonical-notation
skills, including the neural-network reference, were applied.

## Verdict

The fixed-time conclusions are repairable using the established local strong
population theorem. The current proof is incomplete at Section 7: analytic
scalar activations do not imply a smooth vector field on the stated
mean-square state space. Its population Taylor justification and the
displayed big-O remainders are consequently unsupported. This is a proof
gap, not a counterexample to the conclusions.

The finite-width cubic coefficient in (16) is correct for the paper's loss
and mobilities. It should be reconstructed in the population directly,
using the integral equations and a bounded-multiplier lemma. This gives
little-o remainders sufficient for one positive, width-independent interval.
It avoids both a smooth Nemytskii-map claim and an unjustified interchange of
width and short-time limits.

The affine-fit claim is valid once its sample index and continuity argument
are made explicit. The hidden-parameter displacement statement needs one
additional finite-width transfer argument because convergence of operators
in operator norm alone does not imply convergence of Hilbert--Schmidt norms.

## 1. The precise regularity issue

Even the bounded analytic function `tanh` does not define a Fréchet
differentiable Nemytskii map from an atomless (L^2) space to itself at zero.
For events (E_k) with probabilities tending to zero, set

\[
 u_k=\mathbf1_{E_k}.
\]

Then \(\|u_k\|_2\to0\), but the only possible derivative at zero is the
identity and

\[
 \frac{\|\tanh(u_k)-u_k\|_2}{\|u_k\|_2}
 =|\tanh(1)-1|>0.
\]

Thus scalar analyticity, even with all real derivatives bounded, does not
justify the candidate's claim that its population vector field is smooth.
The maintained proof itself avoids this claim: see
`docs/03-local-population.qmd`, “Strong limits without differentiability
assumptions on an L2 map,” especially the multiplier formula and the paragraph
explicitly distinguishing the curve chain rule from Fréchet differentiability.

Nor can the compression paper's holomorphy statement supply the missing
uniform Taylor estimate. Its advertised complex-time radii are proportional
to \(1/\sqrt{\log(en)}\) for the fixed problem; see the source proposition,
equations labelled `cp:source` and `cp:finite-time`. They shrink to zero.
Finite-width formulas with a remainder \(o_n(t^3)\) alone do not give a fixed
positive \(t\) uniformly in width.

## 2. A sufficient directional replacement

Use the paper's normalized inputs \(v_a=x_a/\sqrt d\), input Gram
\(G_{ab}=v_a^\top v_b\), mean squared loss,
unit mobility multipliers, and exact zero readout. Write \(\alpha=2/m\), and
write \(w(t)=W^{(L+1)}(t)\) for the population stored readout. Each layer has
its own \(L^2(\Omega_\ell)\) space. The initial operators are bounded and
retain their true adjoints. The local theorem gives continuity of fields in
these spaces and of operators in operator norm, together with the strong
integral equations.

The sole nonlinear limit fact needed is this: if \(X_t\to X_0\) in
probability, \(V_t\to V_0\) in \(L^2\), and \(g\) is bounded continuous, then

\[
 g(X_t)V_t\longrightarrow g(X_0)V_0\quad\text{in }L^2.
\]

Indeed, the part multiplying \(V_t-V_0\) is bounded by
\(\|g\|_\infty\|V_t-V_0\|_2\). For the other part, truncate the single
fixed field \(V_0\) at level \(M\), use bounded convergence in probability on
the truncated part, and bound the remainder by
\(4\|g\|_\infty^2\mathbb E[V_0^2\mathbf1_{|V_0|>M}]\).

Consequently, if
\(X(t)=X_0+t^2R/2+o_{L^2}(t^2)\), bounded continuous \(\phi'\) gives

\[
 \phi(X(t))=\phi(X_0)+\frac{t^2}{2}\phi'(X_0)R+o_{L^2}(t^2).
 \tag{A}
\]

Apply the mean-value integral formula; its multiplier is uniformly bounded
and converges in probability to \(\phi'(X_0)\). This proves (A) along the
actual curve without asserting smoothness on an open \(L^2\) neighborhood.

Define the candidate's initial fields explicitly:

\[
 S=\sum_a y_aH_a^{(L)}(0),\qquad
 B_a^{(L)}=S\phi_L'(Z_a^{(L)}(0)),
\]

\[
 B_a^{(\ell)}
 =\phi_\ell'(Z_a^{(\ell)}(0))
       (W_0^{(\ell+1)})^*B_a^{(\ell+1)}.
\]

For clarity, the population backward fields at a general time are

\[
 \Delta_a^{(L)}(t)=w(t)\phi_L'(Z_a^{(L)}(t)),\qquad
 \Delta_a^{(\ell)}(t)=\phi_\ell'(Z_a^{(\ell)}(t))
                  (W^{(\ell+1)}(t))^*\Delta_a^{(\ell+1)}(t).
\]

The readout equation is
\(\dot w=-\alpha\sum_a r_aH_a^{(L)}\), where \(r=f-y\). It gives

\[
 \frac{w(t)}t\longrightarrow\alpha S.
\]

Using the multiplier fact at the top gate and then successively the actual
adjoints and lower gates proves

\[
 \frac{\Delta_a^{(\ell)}(t)}t\longrightarrow\alpha B_a^{(\ell)}
 \quad\text{in }L^2(\Omega_\ell),\qquad 1\le\ell\le L.
 \tag{B}
\]

For the first weight block, let \(b_1\in L^2(\Omega_1;\mathbb R^d)\)
be its row acceleration; for other layers let \(b_\ell\) be the
Hilbert--Schmidt operator acceleration. With
\((U\otimes V)q=U\mathbb E[Vq]\), their exact values are

\[
 b_1=\alpha^2\sum_a y_aB_a^{(1)}v_a^\top,\qquad
 b_\ell=\alpha^2\sum_a y_aB_a^{(\ell)}
                         \otimes H_a^{(\ell-1)}(0),\quad\ell\ge2.
 \tag{C}
\]

Equation (B), the integral updates, and continuity of the forward fields
give \(\dot W^{(\ell)}(t)/t\to b_\ell\). For \(\ell\ge2\), the convergence
holds in Hilbert--Schmidt norm, since
\(\|U\otimes V\|_{\rm HS}=\|U\|_2\|V\|_2\) and there are finitely many
samples. Integration gives

\[
 W^{(\ell)}(t)-W_0^{(\ell)}
 =\frac{t^2}{2}b_\ell+o(t^2)
 \tag{D}
\]

in these mobility spaces. For the first layer the same assertion follows by
integrating the explicit row update, even though C.1 records first
preactivations as its state variables.

Let \(R_a^{(\ell)}\) and \(A_a^{(\ell)}\) denote the preactivation and
activation accelerations. Forward substitution in (D) and (A) proves,
recursively,

\[
 \begin{aligned}
 R_a^{(1)}&=b_1v_a,\\
 R_a^{(\ell)}&=b_\ell H_a^{(\ell-1)}(0)
                         +W_0^{(\ell)}A_a^{(\ell-1)},\\
 A_a^{(\ell)}&=\phi_\ell'(Z_a^{(\ell)}(0))R_a^{(\ell)},
 \end{aligned}
\]

and

\[
 H_a^{(\ell)}(t)-H_a^{(\ell)}(0)
 =\frac{t^2}{2}A_a^{(\ell)}+o_{L^2}(t^2).
 \tag{E}
\]

Thus, conditional on the strict positivity established in the earlier
sections of the candidate,

\[
 \sum_a\mathbb E_\ell
  |H_a^{(\ell)}(t)-H_a^{(\ell)}(0)|^2
 =\frac{t^4}{4}\sum_a\|A_a^{(\ell)}\|_2^2+o(t^4),
 \tag{F}
\]

with a positive coefficient. This is the precise replacement for (17).
There is no width \(n\) on the left side of a population expansion.

## 3. Exact normalization of the cubic departure

Let

\[
 g=\|b_1\|_{L^2(\Omega_1;\mathbb R^d)}^2
           +\sum_{\ell=2}^L\|b_\ell\|_{\rm HS}^2.
\]

This is the population limit of
\(\|\ddot\theta_{{\rm hid},n}(0)\|_2^2\), with
\(\theta_{{\rm hid},n}=(W_n^{(1)}/\sqrt n,W_n^{(2)},\ldots,W_n^{(L)})\).
The candidate's positivity proof supplies \(g>0\).

The true mobility kernel has blocks

\[
 \begin{aligned}
 K^{(1)}_{ab}(t)&=G_{ab}\mathbb E_1[\Delta_a^{(1)}(t)\Delta_b^{(1)}(t)],\\
 K^{(\ell)}_{ab}(t)&=\mathbb E_{\ell-1}[H_a^{(\ell-1)}(t)H_b^{(\ell-1)}(t)]
                    \mathbb E_\ell[\Delta_a^{(\ell)}(t)\Delta_b^{(\ell)}(t)],
                    \quad 2\le\ell\le L,\\
 K^{(L+1)}_{ab}(t)&=\mathbb E_L[H_a^{(L)}(t)H_b^{(L)}(t)].
 \end{aligned}
\]

Define
\(Q^{(\ell)}_{ab}=\mathbb E_\ell[H_a^{(\ell)}(0)H_b^{(\ell)}(0)]\) and
\(D^{(\ell)}_{ab}=\mathbb E_\ell[B_a^{(\ell)}B_b^{(\ell)}]\).
Let \(K=\sum_{\ell=1}^{L+1}K^{(\ell)}\) and \(K_0=Q^{(L)}\). Equations
(B) and (E) give the finite-dimensional matrix expansion

\[
 K(t)=K_0+t^2K_2+o(t^2).
 \tag{G}
\]

The hidden blocks contribute \(g/\alpha^2\) to \(y^\top K_2y\): for
example, (C) gives
\(\|b_\ell\|^2=\alpha^4y^\top(Q^{(\ell-1)}\circ D^{(\ell)})y\), whereas
the kernel coefficient is
\(\alpha^2(Q^{(\ell-1)}\circ D^{(\ell)})\).

The readout block contributes the same amount. Indeed its quadratic
coefficient in direction \(y\) is

\[
 \left\langle S,\sum_a y_aA_a^{(L)}\right\rangle
 =\sum_a y_a\langle B_a^{(L)},R_a^{(L)}\rangle.
\]

Adjunction in the recursion for \(R\) gives, at each layer,

\[
 \sum_a y_a\langle B_a^{(\ell)},R_a^{(\ell)}\rangle
 =\frac{\|b_\ell\|^2}{\alpha^2}
    +\sum_a y_a\langle B_a^{(\ell-1)},R_a^{(\ell-1)}\rangle,
\]

with only the first term at layer one. Hence

\[
 y^\top K_2y=\frac{2g}{\alpha^2}.
 \tag{H}
\]

The population frozen-kernel predictor is
\(f_{\rm NTK}(t)=(I-e^{-\alpha K_0t})y\). Both predictors start from zero.
The established prediction equation \(\dot f=\alpha K(t)(y-f)\) gives the
exact integrated identity

\[
 f(t)-f_{\rm NTK}(t)
 =\alpha\int_0^t e^{-\alpha K_0(t-s)}
          (K(s)-K_0)(y-f(s))\,ds.
 \tag{I}
\]

Because \(f(s)\to0\), substitution of (G) into (I) gives

\[
 y^\top(f(t)-f_{\rm NTK}(t))
 =\frac{\alpha}{3}y^\top K_2y\,t^3+o(t^3)
 =\frac m3g\,t^3+o(t^3).
 \tag{J}
\]

The identical argument at fixed finite width proves candidate (16), including
its factor \(m/3\). Its remainder may depend on width, so (J), derived in
the population, is the necessary bridge to a fixed time.

## 4. Fixed-time finite-width transfer

The local theorem C.1 applies with Gaussian first roots, unit initialization
variances, zero readout, \(\omega_a=1/m\), and all \(\kappa_\ell=1\).
The strip derivative bound implies a bounded second real derivative by
Cauchy's formula on a smaller strip, so its real \(C^{1,1}\) hypotheses
hold. Its finite-GF consequence is explicitly explained immediately before
C.1. It supplies the needed positive interval without a Gram gap or
small-label hypothesis.

Since there are finitely many layers, (F) and (J) yield one deterministic
\(t_*>0\) and strict positive lower bounds at every \(0<t\le t_*\).
The local theorem's Wasserstein-2 convergence of the joint same-layer
training paths, with the uniform path norm, implies at each such fixed time

\[
 \frac1n\sum_a\|h_{n,a}^{(\ell)}(t)-h_{n,a}^{(\ell)}(0)\|_2^2
 \xrightarrow{\mathbb P}
 \sum_a\mathbb E_\ell|H_a^{(\ell)}(t)-H_a^{(\ell)}(0)|^2.
\]

This observable is continuous with quadratic growth in the joint path and
therefore includes the essential coupling of its initial and current values.
Choose each finite-width lower-bound constant strictly below the population
one. This proves the stated probability limit, for each fixed positive time.
It does not claim one finite-width event controlling relative errors down to
arbitrarily small times.

At zero readout the finite initial kernel is exactly the top feature Gram,
which converges to \(K_0\). Continuity of the matrix exponential on the fixed
sample space therefore gives uniform compact-time convergence of
\(f_{{\rm NTK},n}\) to \(f_{\rm NTK}\). Together with the local theorem's
prediction convergence and (J), this proves (3).

For completeness, hidden-parameter displacement requires more than operator
norm convergence. For \(\ell\ge2\), the exact finite identity is

\[
\begin{aligned}
 &\|W_n^{(\ell)}(t)-W_{n,0}^{(\ell)}\|_F^2\\
 &=\alpha^2\sum_{a,b}\int_0^t\!\int_0^t
 r_{n,a}(s)r_{n,b}(u)
 \frac{\delta_{n,a}^{(\ell)}(s)^\top\delta_{n,b}^{(\ell)}(u)}n
 \frac{h_{n,a}^{(\ell-1)}(s)^\top h_{n,b}^{(\ell-1)}(u)}n\,ds\,du.
\end{aligned}
\]

The local theorem gives convergence of each fixed-time contraction through
its correctly typed probe assertion, including the bounded gate factors in
backward fields. Its preliminary RMS/operator ball bounds the integrand on
an event of probability tending to one. Truncate off that event, apply
bounded convergence in expectation to the probability-convergent integrands,
and then integrate over \((s,u)\). The limit is the analogous population
Hilbert--Schmidt squared norm. The first block has the same formula with the
feature contraction replaced by \(G_{ab}\), and its norm is
\(\|W_n^{(1)}(t)-W_{n,0}^{(1)}\|_F^2/n\).
Equation (D) supplies the corresponding positive leading coefficients.

## 5. Nonlinear affine-fit error

The candidate should specify every sample marginal
\(Z_a^{(\ell)}(t)\), or explicitly define its intended mixture over samples.
For a scalar random variable \(Z\) of positive variance, least squares gives

\[
 \inf_{c,b\in\mathbb R}
    \mathbb E[(\phi_\ell(Z)-cZ-b)^2]
 =\operatorname{Var}(\phi_\ell(Z))
   -\frac{\operatorname{Cov}(Z,\phi_\ell(Z))^2}
          {\operatorname{Var}(Z)}.
 \tag{K}
\]

Every initial marginal has positive Gaussian variance. The error is strictly
positive there: zero would imply that the continuous nonaffine activation
equals an affine function almost surely on a distribution of full support,
hence everywhere. Analyticity is unnecessary for this particular step.

Mean-square continuity of \(Z_a^{(\ell)}(t)\), and global Lipschitz
continuity of \(\phi_\ell\), give continuity of all means and second
moments in (K), including the mixed moment by Cauchy--Schwarz. The variance
stays bounded away from zero on a small interval. Thus (K) stays positive on
that interval, uniformly over the finitely many pairs \((a,\ell)\).
This proves the intended form of (4). If a finite-width version is desired,
the same joint path Wasserstein-2 convergence transfers these moments and
therefore the empirical best-affine-fit error as well; the candidate currently
states (4) only for the population.

## Required edits to the candidate

1. Delete the assertion that the population vector field is smooth under
   scalar analyticity. Replace it with the multiplier and integral-equation
   argument (A)--(F).
2. Replace the population claims \(O(t^5)\), \(O(t^4)\) by
   \(o(t^4)\), \(o(t^3)\), respectively, and write the feature expression
   as a population expectation rather than a finite-width empirical sum.
3. Derive the normalized cubic coefficient through (G)--(J), or supply an
   equivalent complete argument. Do not pass a finite-width Taylor remainder
   through \(n\to\infty\).
4. State the exact mobility norms and include the double-integral transfer
   for hidden parameter increments.
5. Put the missing sample index into the affine-fit statement and give (K),
   including persistence of its positive denominator.

With these repairs, the time-promotion portion is complete, conditional on
the candidate's earlier strict-positivity claims. This report does not resolve
the separate arbitrary-depth Gaussian conditioning proof.
