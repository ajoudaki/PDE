# Internal check of the orthogonal-query theorem

2026-10-01. **Verdict: PASS for Section 5, with the dependency and scope restrictions below.** No mathematical gap was found in its conditional finite-width estimate. Identification with the clipped population predictor uses the qualitative fixed-query convergence asserted in the assigned population note; this check does not independently certify the underlying Gaussian-program/population construction. This is an internal check, not a promotion review or a proof of the general population rate.

The complete scientific inputs read were `RESOLUTION_LOWER_ROUTE.md`, `FITTING_AND_THRESHOLD.md`, `CLIPPED_POPULATION_ROUTE.md`, and `CONCENTRATION_ROUTE.md`, all in this study. Current `AGENTS.md` and the required solve-math-rigorously skill were also read. No other study, book, manuscript, sibling report, history, or experiment was inspected. Although the target report lists `FULL_ERROR_CHECKPOINT.md` among its own inputs, that file was not assigned or read here; Section 5's checked argument does not require it.

## Exact statement checked

Use the actual model and canonical Gaussian initialization of the assigned notes, with cap \(M=1\), fixed training inputs and labels, and the small-label condition of `FITTING_AND_THRESHOLD.md`. Write

\[
U=\operatorname{span}\{u_1,\ldots,u_m\},\qquad
\mathcal G_n=\{\|W_0\|_{\rm op}\le K_0,
                   \ \Gamma_w(0)\succeq\lambda I_m\}.
\]

For every deterministic query with \(u_x\perp U\), and every width for which \(\Pr(\mathcal G_n)>0\), Section 5 proves

\[
\mathbb E\left[\sup_{t\ge0}|f_n(t,x)|^2\mid\mathcal G_n\right]
\le \frac{C Y^2}{n}.
\]

Here \(C\) can depend on \(K_0,\lambda\), but not on \(n,t,x\), or on the query magnitude. The supplied initial population Gram margin implies \(\Pr(\mathcal G_n^c)\le C_0/n\), so the positive-probability qualification is automatic for sufficiently large \(n\). Conditioning on a probability-zero event at an exceptional small width is not a defined assertion.

Together with the assigned qualitative fixed-query population convergence, this proves \(f_*(t,x)=0\) for all \(t\ge0\) and every such \(x\). For every deterministic Borel probability law supported on \(U^\perp\), integration of the squared temporal supremum has the same bound, with no moment condition on that law.

## Independence and the good event

The first-layer equation gives \(A(t)P_{U^\perp}=A_0P_{U^\perp}\) exactly. The closed training equations depend on the first matrix only through \(A(t)P_U\). Uniqueness and continuous dependence for the finite-dimensional, locally Lipschitz ODE imply that the training state

\[
(A(t)P_U,w(t),v(t),k(t),\tau(t))
\]

is measurable with respect to \(\mathcal F=\sigma(A_0P_U,W_0)\). This is the precise meaning of the target's statement about the other evolving variables: the full matrix \(A(t)\) retains its independent initial orthogonal component and is not itself \(\mathcal F\)-measurable.

Both parts of \(\mathcal G_n\) are \(\mathcal F\)-measurable. In particular, its Gram uses only training features \(\tanh(W_0\tanh(A_0u_a))\). Isotropy of each Gaussian first row makes its orthogonal projections independent; different rows and \(W_0\) are independent as well. Therefore

\[
H=\tanh(A_0u_x)
\]

has independent symmetric coordinates in \([-1,1]\) and is independent of \(\mathcal F\), including after conditioning the environment on \(\mathcal G_n\). No condition on the full first-matrix norm is part of this good event. Adding such a condition without another argument would generally destroy this exact product-law statement.

For each good environment, the actual query output is consequently

\[
F_t(H)=n^{-1}w(t)^T\tanh(B(t)H).
\]

This is a consequence of exact training-span invariance, with no replacement of the trained dynamics. It is odd in \(H\), so its conditional expectation vanishes at every time.

## Velocity estimates, with explicit constants

Put \(S(t)=\int_0^t\rho(s)\,ds\), \(D=K_0+2\), and \(E=\dot B\). The fitting dependency gives

\[
S\le Y/\lambda\le1,\quad \|B\|_{\rm op}\le D,
\quad \|w\|_\infty\le2S,\quad
\|\dot w\|_\infty\le2\rho.
\]

The sample-average estimates used in the target are valid:

\[
\frac1m\sum_a\|\dot v_a\|_\infty\le4S\rho,
\qquad
\frac1m\sum_a\|v_a\|_\infty
\le4\int_0^t S(s)\rho(s)\,ds=2S(t)^2.
\]

Also \(\|k_a\|_\infty\le1\) and \(\|\dot k_a\|_\infty\le2\rho\), since \(\tau\ge1\). Thus the actual reconstruction derivative

\[
E=\frac1{mn}\sum_a(\dot v_a k_a^T+v_a\dot k_a^T)
\]

satisfies both

\[
\|E\|_{\rm op}\le8S\rho,
\qquad
\sup_{h\in[-1,1]^n}\|Eh\|_\infty
\le4S\rho+4S^2\rho\le8S\rho.
\]

The second bound uses the normalized row sums of these rank-one terms; an operator norm alone would not suffice. The target explicitly supplies this necessary stronger estimate.

For \(\psi=\operatorname{sech}^2\), the velocity as a function of fixed \(h\) is

\[
a_t(h)=\frac1n\left[\dot w^T\tanh(Bh)
                  +w^T(\psi(Bh)\odot Eh)\right].
\]

The gradient and diagonal Hessian formulas in the target are correct. Using \(\|\psi\|_\infty\le1\), \(\|\psi'\|_\infty\le2\), \(\|\psi''\|_\infty\le6\), one obtains the explicit uniform bounds

\[
\|\nabla_h a_t(h)\|_2
\le(34D+16)\frac{\rho}{\sqrt n},
\]

\[
|\partial_{jj}a_t(h)|
\le(100D^2+64D)\frac{\rho}{n}.
\]

Indeed the gradient's three terms are bounded by

\[
2D\rho/\sqrt n,\qquad
32DS^2\rho/\sqrt n,\qquad
16S^2\rho/\sqrt n.
\]

The three diagonal Hessian terms are bounded by

\[
4D^2\rho/n,\qquad
96D^2S^2\rho/n,\qquad
64DS^2\rho/n.
\]

Here each column of \(B\) has Euclidean norm at most \(D\), and each column of \(E\) at most \(8S\rho\). The mixed column product is controlled by Cauchy–Schwarz. These estimates do not differentiate a clipping map: the fixed-environment query output is smooth in \(h\).

There is one harmless typesetting defect in the target's displayed gradient: `\left{` should be `\left\{`.

## Resampling and the temporal supremum

Let \(K_1=34D+16\) and \(K_2=100D^2+64D\). For any product law on \([-1,1]^n\), coordinate replacement and the diagonal Hessian estimate give

\[
|a_t(H)-a_t(H^{(j)})|
\le2|\partial_j a_t(H)|+2K_2\rho/n.
\]

After squaring and summing, the replacement-variance inequality yields

\[
\operatorname{Var}_H a_t(H)
\le4(K_1^2+K_2^2)\frac{\rho(t)^2}{n}.
\]

This does not substitute a Euclidean Lipschitz constant into an unjustified dimension-free concentration theorem for arbitrary product laws. The diagonal second-derivative bound is essential to the presented resampling argument.

For completeness, the replacement inequality follows by writing \(a-\mathbb Ea\) as the martingale differences for successively revealed coordinates. For the \(j\)-th difference, conditional Jensen bounds its second moment by

\[
\mathbb E\left[\left(a-\mathbb E[a\mid H_{-j}]\right)^2\right]
=\frac12\mathbb E[(a(H)-a(H^{(j)}))^2].
\]

Independence of the coordinates identifies this conditional expectation with the appropriate martingale difference after projection onto the first \(j\) coordinates. Orthogonality of the differences then gives the asserted sum.

Symmetry of the product law makes \(a_t\) odd and gives \(\mathbb E_Ha_t=0\). Moreover

\[
|a_t(h)|\le2\rho+16S^2\rho\le18\rho
\]

for every \(h\in[-1,1]^n\), so the velocity is absolutely integrable at every such \(h\). Since \(F_0=0\), Minkowski on finite intervals followed by monotone convergence gives

\[
\begin{aligned}
\left(\mathbb E_H\sup_{t\ge0}|F_t(H)|^2\right)^{1/2}
&\le\int_0^\infty\|a_t(H)\|_{L^2(H)}\,dt\\
&\le2\sqrt{K_1^2+K_2^2}\frac{Y}{\lambda\sqrt n}.
\end{aligned}
\]

Continuous paths permit the temporal supremum to be taken over nonnegative rational times, ensuring measurability. Averaging this estimate over good training environments introduces no factor \(1/\Pr(\mathcal G_n)\): the bound already holds for almost every such environment with the same constant.

## Population identification and integration over queries

The finite-width result and the assigned good-event probability bound give, for fixed \(t,x\) and any \(\varepsilon>0\),

\[
\Pr\{|f_n(t,x)|>\varepsilon\}
\le\Pr(\mathcal G_n^c)+\frac{CY^2}{n\varepsilon^2}
\longrightarrow0.
\]

The qualitative fixed-query result of `CLIPPED_POPULATION_ROUTE.md`, Section 4, identifies the same random variables' deterministic probability limit as \(f_*(t,x)\). Uniqueness of a probability limit therefore forces \(f_*(t,x)=0\). This uses only fixed-time convergence; the stronger all-time convergence stated in the dependency is unnecessary for this identification. It does not obtain a rate by inference from qualitative convergence: the quantitative bound was proved first, directly at finite width.

The deterministic conclusion holds for every fixed \(t,x\) under consideration. Thus there is no uncountable intersection of random exceptional sets needed to identify the population function. Finite-width outputs are jointly continuous in \(t,x\), so their squared temporal suprema are jointly measurable. Tonelli applied to any fixed probability law supported on \(U^\perp\) yields

\[
\mathbb E\left[\int\sup_{t\ge0}|f_n(t,x)-f_*(t,x)|^2\,d\mu(x)
              \mid\mathcal G_n\right]
\le \frac{CY^2}{n}.
\]

No independence across different queries is used. The constant is independent of query magnitude because the proof uses only product symmetry and \(|H_j|\le1\).

## Consistency checks and restrictions

The directly relevant assertions in Sections 2, 3, 4, and 6 are consistent:

- The clipped tanh-gate map has the stated global value Lipschitz bound. The scalar corner example has exactly root-width bias and does not establish slower bias.
- Kernel directions of a fixed finite-dimensional raw covariance are exact almost-sure kernel directions of its empirical covariance. The upper tanh-layer extension follows from Gaussian support and continuity, as written. These initial facts make no assertion about dynamically adapted histories.
- Integrating the exponential query-velocity bound gives the stated logarithmic-horizon reduction. It does not supply a rate on that growing horizon.
- Bounded readout and tanh imply the uniform error envelope \(4Y/\lambda\). A fixed finite-second-moment law has tail mass \(o(R^{-2})\), giving the claimed \(o(n^{-1/2})\) contribution beyond query norm \(\sqrt n\).

The checked theorem remains restricted to passive deterministic queries orthogonal to the fixed training span, canonical isotropic independent Gaussian first rows, the stated training-measurable good event, and the small-label fitting regime. It is a conditional all-time second-moment bound, not an unconditional all-time bound, a spatial supremum, a bound for arbitrary initialization-dependent selected queries, or the general-query root-width population theorem. When \(U=\mathbb R^d\), its only query is zero and the output vanishes exactly.

The finite-width theorem is self-contained given the verified deterministic fitting estimates. Its assertion about the specifically named population predictor remains dependent on the population note's qualitative identification theorem and should carry that dependency explicitly in any further use.
