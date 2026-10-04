# Fixed clipping: population construction and the unresolved width source

Status: internally derived partial result, not an established-book addition. This bounded route does **not** prove or disprove the requested root-width estimate. It proves that fixed positive clipping closes a deterministic regularity issue and gives a qualitative all-time population limit. The remaining quantitative issue is production of error by reused Gaussian actions, rather than its amplification by long physical time.

## Scope and sources

The target is the actual two-hidden-layer tanh, order-one memory closure, with independent Gaussian first rows and middle matrix, exactly zero readout and value initialization, matching initial keys, and clock one. The middle matrix is used with its actual transpose. Clipping is recursive, after each activation gate and before multiplying by the residual. No fresh-matrix, dense-training, frozen-feature, or linear-model substitution is made.

The assigned source scope was used: `paper/main.tex` for the model and raw moments; all of `paper/results.tex`, `paper/proof_alltime.tex`, and `paper/proof_tracking.tex` for the relevant theorem and its complete proofs; `docs/index.qmd` and `docs/notation.qmd`; the exact conditioning paragraphs and fixed-program quantitative-coupling proof in `docs/02-gaussian-reuse.qmd`; and the complete fixed-mesh identification/common-action/clipped-flow passages in `docs/03-local-population.qmd`, Sections 3–4 of the arctangent material. The latter supplies a method, not a theorem automatically applicable to this different model. No other study, archive, experiment, or Git history was read. The required solve-math-rigorously and investigate-conjectures skills and relevant contract/audit/proof-search references were read. No numerical experiment or Git operation was performed.

## 1. Exact normalized order-one system

Write \(u_a=x_a/\sqrt d\), \(X=\max_a\|u_a\|\), and
\(C_M(s)=\max(-M,\min(M,s))\), where \(M>0\) is fixed independently of width. Let \(A\in\mathbb R^{n\times d}\) be the first matrix and \(W_0\in\mathbb R^{n\times n}\) the initialized middle matrix.

At order one the paper's raw moments satisfy
\[
 \dot{\bar h}_a=\rho h_a,\qquad
 \dot{\bar\delta}_a=r_a d_a,\qquad \dot\tau=\rho.
\]
Thus the normalization
\[
 k_a=\bar h_a/\tau,\qquad v_a=-2\bar\delta_a
\]
gives, exactly,
\[
 B=W_0+\frac1{mn}\sum_a v_a k_a^T,
 \qquad \dot k_a=\frac\rho\tau(h_a-k_a),
 \qquad \dot v_a=-2r_a d_a.                       \tag{1}
\]
There is no extra factor of \(\tau\) in either the reconstruction or the value equation.

The other equations are
\[
\begin{gathered}
 z_a^{(1)}=Au_a,\quad h_a=\tanh z_a^{(1)},\quad
 z_a=Bh_a,\quad H_a=\tanh z_a,\quad
 f_a=w^TH_a/n,\\
 r_a=f_a-y_a,\qquad \rho=(m^{-1}\sum_a r_a^2)^{1/2},\\
 d_a=C_M(w\odot\operatorname{sech}^2 z_a),\qquad
 \ell_a=C_M(\operatorname{sech}^2 z_a^{(1)}\odot B^Td_a),\\
 \dot A=-\frac2m\sum_a r_a\ell_a u_a^T,
 \qquad \dot w=-\frac2m\sum_a r_a H_a .           \tag{2}
\end{gathered}
\]
Initially \(w=v_a=0\), \(k_a=h_a(0)\), and \(\tau=1\). The clipped upper field \(d_a\), not its uncut counterpart, enters the transpose call in (2).

## 2. The special tanh estimate

The map
\[
 \Psi_M(z,p)=C_M(p\operatorname{sech}^2 z)
\]
satisfies
\[
 |\Psi_M(z,p)-\Psi_M(\widetilde z,\widetilde p)|
 \le |p-\widetilde p|+2M|z-\widetilde z|.         \tag{3}
\]
For fixed \(z\), clipping is nonexpansive and \(\operatorname{sech}^2z\le1\). For fixed \(p\), the clipped function is absolutely continuous. At almost every unsaturated point its derivative has absolute value
\[
 2|p\operatorname{sech}^2z\tanh z|\le2M;
\]
at saturated points its derivative is zero. Integrating this derivative and changing the two arguments separately proves (3).

This is stronger than merely bounding the output. It removes the unbounded carrier multiplier in the \(L^2\) difference estimate. A general bounded-derivative activation does not automatically satisfy (3); tanh's relation \(|\phi''|\le2\phi'\) is being used.

## 3. Finite activity and fitting without a gradient identity

Here is a deterministic estimate valid at finite width, and verbatim on the population spaces described below. Assume \(\|W_0\|_{\rm op}\le K\). Put
\[
 s(t)=\int_0^t\rho(a)\,da,
 \qquad Y=(m^{-1}\sum_a y_a^2)^{1/2}.
\]
All bounds below are on \(s\le s_0\le1\), and constants depend only on \(K,m,X\). In particular, these activity bounds use only \(|C_M(p)|\le|p|\), so their constants can be chosen independently of the positive cap.

The key equation has the exact formula
\[
 k_a(t)=\frac{h_a(0)+\int_0^t\rho(u)h_a(u)\,du}{1+s(t)},
\]
so \(\|k_a\|_\infty\le1\). The readout and top backward field obey
\[
 \|w(t)\|_\infty\le2s(t),\qquad
 \|d_a(t)\|_\infty\le2s(t).
\]
Since \(|r_a|\le\sqrt m\rho\), integration of (1) gives
\[
 \|v_a(t)\|_\infty\le
 4\sqrt m\int_0^t\rho(u)s(u)\,du=2\sqrt m\,s(t)^2.
\]
Consequently
\[
 \|B-W_0\|_{\rm op}\le2\sqrt m\,s^2,
 \qquad
 \frac{\|\ell_a\|_2}{\sqrt n}
 \le2(K+2\sqrt m s^2)s.                         \tag{4}
\]
The last inequality uses contraction by the gate and the clip, followed by the actual transpose operator bound. It does not replace the transpose by a Gaussian independent of the forward path.

Equation (2), Cauchy–Schwarz over the sample list, and (4) yield
\[
 \frac{\|\dot A\|_F}{\sqrt n}\le Cs\rho,
 \quad \frac{\|A-A_0\|_F}{\sqrt n}\le Cs^2,
 \quad \max_a\frac{\|h_a-h_a(0)\|_2}{\sqrt n}\le Cs^2.
\]
The key integral formula then gives
\[
 \max_a\frac{\|k_a-h_a(0)\|_2}{\sqrt n}\le Cs^3,
 \qquad \max_a\frac{\|\dot k_a\|_2}{\sqrt n}\le Cs^2\rho.
\]
Differentiating the finite-rank reconstruction and using
\(\|\dot v_a\|_2/\sqrt n\le4\sqrt m s\rho\) proves
\[
 \|\dot B\|_{\rm op}\le Cs\rho,
 \qquad
 \max_a\frac{\|\dot z_a\|_2+\|\dot H_a\|_2}{\sqrt n}
 \le Cs\rho.                                    \tag{5}
\]
Every factor in the outer-product differentiation is bounded above; no coordinate maximum of a Gaussian action is used.

Let
\[
 \Gamma_{ab}(t)=\frac{H_a(t)^TH_b(t)}{mn}.
\]
Integrating (5) gives \(\|\Gamma(t)-\Gamma(0)\|_{\rm op}\le Cs^2\). The exact prediction derivative is
\[
 \dot r=-2\Gamma r+e,
 \qquad e_a=\frac1n w^T\dot H_a,
 \qquad \|e\|_m\le Cs^2\rho.                    \tag{6}
\]
This identity explicitly retains the hidden-motion term; the clipped dynamics need not be a gradient flow.

Suppose \(\Gamma(0)\succeq\lambda I_m\), \(\lambda>0\). Choose \(s_0>0\) such that the Gram perturbation is at most \(\lambda/4\) and the final coefficient in (6) is at most \(\lambda/2\) whenever \(s\le s_0\). For \(\rho>0\), (6) gives
\[
 \dot\rho\le-\lambda\rho.
\]
If \(Y\le\lambda s_0/2\), stop provisionally at activity \(2Y/\lambda\). The preceding inequality implies
\[
 \rho(t)\le Ye^{-\lambda t},\qquad
 s(t)\le Y/\lambda,
\]
so the stop is never reached. The vector field is locally Lipschitz for \(\tau>0\), by (3); all variables stay bounded, with \(\tau\ge1\). Thus finite-width solutions extend globally. The same statement for \(Y=0\) is the stationary solution. All state coordinates converge as \(t\to\infty\), since their speeds are bounded by a constant times \(\rho\).

## 4. A genuine clipped population flow, and a qualitative all-time limit

Use two population spaces \(\mathcal H_1=L^2(\Omega_1)\) and \(\mathcal H_2=L^2(\Omega_2)\). The first Gaussian row is \(A_0\in L^2(\Omega_1;\mathbb R^d)\). The initialized action \(\mathscr W_0:\mathcal H_1\to\mathcal H_2\) and its true adjoint are constructed from the joint limits of finite Gaussian programs, not prescribed as independent random maps. At population level the state is
\[
 A\in L^2(\Omega_1;\mathbb R^d),\quad
 k_a\in\mathcal H_1,\quad v_a,w\in\mathcal H_2,\quad\tau\in\mathbb R,
\]
and
\[
 \mathscr B=\mathscr W_0+\frac1m\sum_a v_a\otimes k_a,
 \qquad (v_a\otimes k_a)g=v_a\mathbb E_1[k_ag].  \tag{7}
\]
Equations (1)–(2) are read using (7), population expectations instead of normalized sums, and \(\mathscr B^*\) for the transpose. Their prediction is deterministic: \(f_M(t,x)=\mathbb E_2[w(t)H(t,x)]\).

For clarity, the construction and limit argument have the following checked steps.

1. Include rational linear combinations, the initial Gaussian row, bounded smooth coordinate instructions, smooth approximations of \(\Psi_M\), and both directions of every required initialized-matrix call in a countable collection of finite programs. Every finite union is still a finite program. The fixed-Gaussian-computation lemma proved in `paper/proof_alltime.tex` therefore supplies consistent deterministic joint laws. Its hypotheses are satisfied: only one independent Gaussian matrix is reused; roots are independent of it; after freezing the finite scalar contractions all coefficients are deterministic; tanh and smooth approximations to (3) are globally Lipschitz.
2. Pass the finite operator bound \(\|W_0g\|_2/\sqrt n\le K\|g\|_2/\sqrt n\) and transpose identity to each finite generated span. Completion gives bounded common actions and their actual adjunction. A countable dense bounded-function family makes these completions the generated \(L^2\) spaces. This is the construction proved in the assigned common-action source, now with the two-layer instruction list above.
3. On bounded state sets with \(\tau\ge1\), the complete vector field is locally Lipschitz in the sum of its \(L^2\) state norms and the scalar clock distance. For (7), use \(\|u\otimes v-\widetilde u\otimes\widetilde v\|_{\rm op}\le\|u-\widetilde u\|_2\|v\|_2+\|\widetilde u\|_2\|v-\widetilde v\|_2\). The forward maps are Lipschitz, and both backward maps use (3). The finite-dimensional residual norm is Lipschitz as well. Integral iteration on a sufficiently short interval is consequently a contraction. Restarting while the state is bounded gives the unique strong solution.
4. The estimates (4)–(6) remain true with population norms. Strong absolutely continuous coordinates satisfy the activation chain rule: apply the scalar chain rule pointwise and integrate using the bounded activation derivative. The required scalar prediction product rule then follows from the Hilbert-space product rule. The same small-label condition gives a global solution, exponential fitting, and finite total variation.
5. On any fixed physical interval \([0,T]\), Euler error is \(C_{M,T}\Delta\), uniformly in width on the bounded initialization event. At a fixed finite mesh, freeze residuals and contractions at their deterministic population values. This produces a finite Gaussian program on the actual arrays. Its contraction errors converge to zero. The elementary difference bound for normalized pairings and a finite instruction induction transfer this convergence to the actual finite Euler scheme. This is a fixed-mesh statement; no rate uniform in mesh is asserted. First let width tend to infinity, then the Euler step tend to zero. Smooth approximations to hard clipping are removed using their uniform value error and the common Lipschitz bound (3). The result is compact-time convergence to the unique clipped population flow.
6. A fixed passive input adds only first-row projections and forward calls, so the argument applies to every fixed query \(x\). The speeds above imply
   \[
   |\partial_t f_{n,M}(t,x)|+|\partial_t f_M(t,x)|
   \le C(1+\|x\|/\sqrt d)\,Ye^{-\lambda t}.
   \]
   The uniform tail integral upgrades convergence at each fixed query to the supremum over all time. For a fixed probability law \(\mu\) of finite second moment, the same bound and truncation give
   \[
   \left(\int\sup_{t\ge0}|f_{n,M}(t,x)-f_M(t,x)|^2\,d\mu(x)\right)^{1/2}
   \xrightarrow{\mathbb P}0.                    \tag{8}
   \]

The initialization events used here have probability tending to one: bounded Gaussian matrix operator norm, bounded first-row RMS, and the initial feature Gram gap. The Gaussian initialization covariance induction in `paper/proof_alltime.tex` supplies the last condition when its deterministic limiting Gram has the stated positive margin. The physical and population equations are exactly the same clipped order-one system throughout.

This proves existence, identification, uniqueness, and all-time qualitative convergence for the own clipped population predictor. It does not quantify (8).

## 5. A rigorous conditional rate-transfer lemma

The following elementary lemma isolates what finite activity can contribute to a rate. It is stated abstractly so that an unproved finite/population coupling is not hidden in its hypotheses.

Suppose \(E,U\ge0\) are locally absolutely continuous discrepancy functions, \(b\ge0\) is measurable and satisfies \(\int_0^\infty b\le S\), and for all \(t\) (with the differential inequality interpreted almost everywhere)
\[
 \begin{aligned}
 E(t)&\le a+C\int_0^t U(s)\,ds+C\int_0^t b(s)E(s)\,ds,\\
 D^+U(t)&\le-\kappa U(t)+Cb(t)E(t)+q(t),
 \end{aligned}                                  \tag{9}
\]
where \(\kappa>0\), \(a\ge0\), and \(q\ge0\) is integrable. Integration of the second inequality gives
\[
 \int_0^tU\le\frac{U(0)+C\int_0^t bE+\int_0^tq}{\kappa}.
\]
Substitution in the first inequality, followed by the integrating-factor proof of Gronwall, yields
\[
 \sup_{t\ge0}E(t)
 \le C_{\kappa,C}\left(a+U(0)+\int_0^\infty q\right)
       \exp(C_{\kappa,C}S).                       \tag{10}
\]
The integral of \(U\) has the corresponding bound. In particular, a root-width source in the parentheses stays root-width for all physical time, with no \(\exp(CT)\) loss. A passive-query Lipschitz estimate \(|\Delta f(t,x)|\le C(1+\|x\|)E(t)\) then supplies the requested finite-second-moment query norm.

For the target system, (3) removes the unbounded-carrier obstruction in constructing inequalities of type (9). However, applying (10) to finite width versus population still requires a compatible Gaussian proxy and a quantitative estimate for its source errors. Equation (10) does not itself construct that proxy or estimate those errors.

One useful sufficient statistical input would control, at root width, the empirical contractions and initialized-matrix-call errors of the prescribed-coefficient population Euler programs, uniformly as the physical mesh tends to zero and the terminal horizon grows, with errors integrated against the residual activity. Such a theorem concerns a deterministic-coefficient Gaussian program before the actual empirical residual feedback is restored. It is therefore a substantive statistical claim, not a reformulation of prediction convergence. None of the assigned sources establishes this input for the present clipped closure.

## 6. Why the available fixed-program rate does not close the theorem

The relevant quantitative proof in `docs/02-gaussian-reuse.qmd`, Sections 5.9–5.11, obtains root-width errors for a separately fixed feature-ascent program by using a positive minimum history-Gram gap, Schur-complement lower bounds, and a finite moment tower. Its constants depend on the program length and step. Its model also has order-one random readout and a prescribed feature-ascent step, so the strict-rank theorem cannot be imported into the present zero-readout, clipped, residual-driven program.

There is a concrete obstruction to making its *uniform Gram-gap argument* work merely by citing finite activity. Let \(H(t)\) be any query history in a Hilbert space and assume \(\|H(t+\Delta)-H(t)\|_2\le L\Delta\). For the Gram of these two query columns,
\[
 G_\Delta=
 \begin{pmatrix}
 \|H(t)\|_2^2&\langle H(t),H(t+\Delta)\rangle\\
 \langle H(t),H(t+\Delta)\rangle&\|H(t+\Delta)\|_2^2
 \end{pmatrix},
\]
the Rayleigh quotient at \((1,-1)/\sqrt2\) gives
\[
 \lambda_{\min}(G_\Delta)
 \le\tfrac12\|H(t+\Delta)-H(t)\|_2^2
 \le\tfrac12L^2\Delta^2.                         \tag{11}
\]
Thus, if it is invertible, \(\|G_\Delta^{-1}\|_{\rm op}\ge2/(L^2\Delta^2)\). For the present learned histories, (5) makes the difference even smaller late in training. If two columns agree exactly, the Gram is singular. Keeping a fixed positive clipping threshold changes neither conclusion.

In the fixed-program coupling, inverse differences are bounded by
\(A^{-1}(B-A)B^{-1}\), while innovation square-root differences divide by the square root of a lower Schur bound. Both estimates therefore lose their uniform constants on a refining history. Simply discarding exactly repeated columns does not treat arbitrarily close columns. Fixed-program removal of singularity by auxiliary input noise also takes limits in the order width, then noise; it does not supply a root-width bound uniform in a vanishing noise level.

Equation (11) refutes only this naive proof step, not the desired theorem. Inverse-free response formulas, cancellations between small innovations and large regression coefficients, or a quantitative continuous-history argument might still produce a bounded source estimate. Such a cancellation estimate has not been proved here.

A second logical gap remains even if Gaussian concentration establishes \(f_{n,M}-\mathbb E f_{n,M}=O_{\mathbb P}(n^{-1/2})\): it does not bound the bias \(\mathbb E f_{n,M}-f_M\). For example, the abstract sequence \(f_M+n^{-1/4}+n^{-1/2}Z\) has root-width centered fluctuations and converges to \(f_M\), but its population error is not root width. This is a counterexample to that inference only; it is not asserted to be a trajectory of (1)–(2).

## Route verdict

Proved within this route: exact normalization; the tanh clipping Lipschitz bound; deterministic small-label finite activity and fitting; a compatible, uniquely restartable clipped population construction and qualitative all-time finite-width prediction convergence; and the abstract activity-weighted rate-transfer lemma.

Not proved: the mesh- and horizon-uniform root-width source/bias estimate for the reused Gaussian action. Fixed \(M>0\) removes an important deterministic regularity obstacle but does not, by itself or by any result supplied here, establish the requested \(O_{\mathbb P}(n^{-1/2})\) all-time population error. The broad rate conjecture remains open in this bounded attempt. Reopen this route upon a quantitative compatible Gaussian-program estimate that controls nearly dependent continuous histories without losing a mesh-dependent constant.
