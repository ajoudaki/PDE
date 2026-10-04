# Internal check of the large-label assessment

**Verdict: INTERNAL PASS for the claims as stated.** The one-sample scalar
fitting theorem is correct at arbitrary fixed depth. For two tanh hidden
layers, the prescribed-control fluctuation argument extends to every fixed
finite control interval, and the scalar comparison transfers it to
same-physical-time, all-time concentration about the stated finite-width
deterministic center. This is a fixed-confidence probability theorem. It does
not assert an unconditional all-time mean-square estimate, a population limit,
or a rate for the finite-width mean bias.

This check requires no mathematical repair to the candidate. I did not edit
it. The author incorporated the two suggested presentation clarifications:
the all-time query norm is now defined locally, and the independent-run
comparison explicitly uses the same width. The author also renamed the top
activation bound to \(B_\phi\), keeping it distinct from the query radius.
I reread the complete final candidate after these changes. Its SHA-256 is
`736ad09b8081657373ba98687cc32f52bfdc2db33d46c72c69e5ad85ce977208`.

## Scope and inputs

This is an internal scoped check, following an earlier prompt-only derivation
of the scalar theorem. It is not a fresh independent promotion review.

I read the complete candidate `LARGE_LABEL_ASSESSMENT.md` and the complete
same-study dependencies `FINITE_TAIL_ROUTE.md`,
`PASSIVE_QUERY_FLUCTUATIONS.md`, `CONTROLLED_FEEDBACK_STABILITY.md`, and
`POPULATION_CAVITY_ATTEMPT.md`. I checked the dense setting and mobility
normalizations in the authorized `paper/main.tex`. I applied the
canonical-notation skill, its neural-network reference, and the rigorous-math
skill. I did not consult other studies, prior check reports, experiments, or
Git history. The candidate author lists `AUTONOMOUS_SELF_AVERAGING.md` among
their own inputs; this check did not read or require that file. The
concentration consequence below is reconstructed directly from the supplied
dependencies.

For clarity, the all-time query norm used here is
\[
\mathcal E_\mu(f,g)
=\left(\int\sup_{t\ge0}|f(t,x)-g(t,x)|^2\,d\mu(x)\right)^{1/2},
\]
where \(\mu\) is a probability measure supported in
\(\|x\|/\sqrt d\le B\). It is not a supremum over the query ball.

## 1. Normalizations and label rescaling

The dense setting uses unhalved mean-square loss, readout
\(f=w^\top h^{(L)}/n\), and block mobilities
\((n,1,\ldots,1,n)\). With one sample, the physical equation is
\[
\dot\theta=2(y-f)M\nabla_\theta f.
\]
Consequently the candidate's control coordinate has
\(\dot u=2(y-f)\), and the controlled curve is
\(\theta'=M\nabla_\theta f\). Its readout equation is exactly
\(w'=h^{(L)}\); each hidden matrix retains the factor \(1/n\).

Under \(y=c\widetilde y\), \(w=c\widetilde w\), the residual and every
residual-free backward field both gain a factor \(c\). Dividing the readout
equation by \(c\) removes its overall factor, whereas the hidden equations
retain \(c^2\). The candidate's Section 1 is correct: a common time change
cannot eliminate this relative learning-rate change.

## 2. Scalar fitting, continuation, and signs

Write \(P(u)=f(\theta(u))\),
\(R(u)=\|w(u)\|_2/\sqrt n\), and
\(Q_0=\|h^{(L)}(0)\|_2^2/n>0\). The exact energy identity is
\[
P'=\|\theta'\|_{M^{-1}}^2
\ge \|h^{(L)}\|_2^2/n.
\]
All lower-parameter gradients vanish at zero readout, so
\(P'(0)=Q_0\), not merely \(P'(0)\ge Q_0\).

If the top activation is bounded by \(B_\phi\), then on every positive local
control interval
\[
\|w(u)\|_\infty\le B_\phi u,\qquad
0\le P(u)\le B_\phi^2u,\qquad
\int_0^U\|\theta'\|_{M^{-1}}^2du\le B_\phi^2U.
\]
For a putative finite maximal endpoint \(U_*\), parameter increments on
\([s,t]\subset[0,U_*)\) have norm at most
\(B_\phi\sqrt{U_*(t-s)}\). Thus the state has a finite limiting value, and
the locally Lipschitz finite-dimensional vector field continues it. This
proves global existence in the control coordinate. Globally bounded
activation derivatives are unnecessary for this continuation argument.

For \(u>0\), positivity of \(P\) and \(R\) first holds near zero and
then persists. The exact calculation is
\[
R'=P/R,\qquad
P'\ge P^2/R^2=(R')^2,\qquad
R''=\frac{P'-(R')^2}{R}\ge0.
\]
The one-sided limit is \(R'(0+)=\sqrt{Q_0}\), giving
\(R'\ge\sqrt{Q_0}\), \(P'\ge Q_0\), and
\(P(u)\ge Q_0u\). The proof does not divide by zero at initialization.

For \(y>0\), there is a unique fitted coordinate
\(u_*\le y/Q_0\). The physical residual obeys
\(\dot r=-2P'(u)r\), with \(r=f-y\), so the residual, loss, and
integrated-residual bounds in (6) all have the correct factors of two.
Convergence of \(u(t)\) to \(u_*\), followed by continuity of the finite
controlled curve, proves convergence of all parameters to a fitted state.
Uniqueness here concerns the point on this controlled curve, not every
possible fitted network parameter state.

Changing \((y,w)\) to \((-y,-w)\) preserves the hidden physical
dynamics and reverses the output. This verifies the negative-label reduction
for arbitrary smooth hidden activations. Zero label is stationary. The
candidate correctly asserts a lower bound on the last-feature energy, without
asserting that this energy itself is monotone.

## 3. Extending the fluctuation proof to finite control horizon

In this section there is one normalized training input,
\(\|x_0\|^2/d=1\), two tanh hidden layers, and the single prescribed
control \(b(u)=u\), \(0\le u\le S<\infty\).

The transformed equations in the dependencies are exact. Their estimates
that used \(S\le1\) used it to suppress factors of \(S\), not to absorb
a feedback error. Replacing these constants by finite functions of \(K,S\)
is valid for the following reasons.

1. The deterministic tube is
   \(\|w\|_\infty\le S\),
   \(\|W-W_0\|_F\le S^2\), and
   \(\|W\|_{\rm op}\le K+S^2\). The transformed activation
   \(\psi=\tanh\circ F^{-1}\) remains globally 1-Lipschitz.
   The normalized state differences therefore satisfy Gronwall bounds with
   finite constants depending on \(K,S\), independently of width and of
   the first-root values.

2. Deleting a column retains normalization \(n\). With
   \(q_i=\|W_{0,i}\|+S^2/\sqrt n\), the retained normalized state
   difference is bounded by \(C_{K,S}q_i/\sqrt n\). The direct missing
   preactivation contribution has norm at most \(q_i\). This gives the
   same cavity decomposition for training and passive-query carriers, with
   an \(O_{B,K,S}(1)\) remainder on the original operator event.

3. Conditional on deterministic first roots and the other initialized
   columns, the omitted column remains \(N(0,I_n/n)\). The cavity response
   has RMS at most \(S\), and its RMS time increment is at most
   \(C_{B,K,S}|u-v|\). Hence its Gaussian pairing has variance at most
   \(S^2\) and increment standard deviation at most
   \(C_{B,K,S}|u-v|\). Dyadic time nets have \(O(2^\ell)\) points;
   their maximal increments have \(L^p\) norm bounded by
   \(C_{B,K,S}2^{-\ell}(\sqrt p+\sqrt{\ell+1})\).
   Summation proves all coordinate moments and a square-exponential tail.
   There is no need to insert a random control into this statement.

4. Projection onto the operator ball is used only for the proof. On its
   complement, the projected carrier is bounded by
   \(C_{K,S}\sqrt n\); its transformed coordinate displacement has the
   same form. Thus fourth-moment contributions are bounded by a polynomial
   in \(n\) times \(e^{-cn}\), and every fixed linear-exponential
   displacement moment is bounded using
   \(\exp(C_{K,S,p}\sqrt n-cn)\). These are uniform finite constants.
   No conditional Gaussian assertion is made about the projected matrix on
   this complement.

5. The matrix response and first-root response estimates in
   `PASSIVE_QUERY_FLUCTUATIONS.md` use precisely these finite moments. The
   root weights \(e^{2|U|}\) and \(e^{4|U|}\) remain integrable for
   every fixed \(S\). Root perturbations are deterministic before averaging
   over the matrix, so the argument does not replace a random multiplier
   norm by the average of its diagonal entries. The two Gaussian variance
   inequalities therefore still give
   \(\operatorname{Var}(\partial_u f_n^{\Pi,u}(x))\le C_{B,K,S}/n\).

6. The centered prediction starts at zero. The deterministic inequality
   \(\sup_{u\le S}|g(u)|^2\le S\int_0^S|g'(u)|^2du\) then gives
   the full-interval fluctuation bound. Since both original and projected
   prescribed-control outputs are bounded by \(S\), projection removal
   costs at most \(C S^2e^{-cn}\). Tonelli yields the query-integrated
   statement. No time discretization, coordinate maximum loss, or smallness
   absorption enters this proof.

For completeness, the deterministic derivative bound needed both here and
in scalar query transfer can be made explicit. Let
\(c=x_0^\top x/d\), so \(|c|\le B\). The passive tangent pairing has
three terms as in (6) of `PASSIVE_QUERY_FLUCTUATIONS.md`; their absolute
values are bounded respectively by
\(1\), \(S^2\), and \(B(K+S^2)^2S^2\). Therefore
\[
\sup_{u\le S}|\partial_u f_n^{\Pi,u}(x)|
\le 1+S^2+B(K+S^2)^2S^2.
\]
The same bound holds for the original initialization on its operator event.
For the training query take \(B=1\). This justifies differentiation under
expectation and supplies the required width-independent query Lipschitz
constant. It is not obtained solely from the scalar lower derivative bound.

## 4. Initial energy and the deterministic reference

Write \(Y=|y|\). The following comparisons use the positive-label controlled
curve; for negative labels, the established sign symmetry multiplies both
query predictors by \(-1\) and leaves their absolute errors unchanged.

The positive initial-energy limit used in Section 5 is a finite Gaussian
initialization calculation, independent of any dynamical population theorem.
Let \(Z\sim N(0,1)\) and
\[
q_1=\mathbb E\tanh^2 Z>0,
\qquad q_2=\mathbb E\tanh^2(\sqrt{q_1}Z)>0.
\]
The first-feature energy converges to \(q_1\). Conditional on the first
features, the initialized second preactivations are independent Gaussians
with that empirical variance. Their bounded squared tanh values have
conditional empirical variance at most \(1/n\). Continuity of the scalar
Gaussian expectation therefore gives \(Q_0\to q_2\) in probability.

The projected and original initial energies agree on the operator event and
both lie in \([0,1]\). Hence
\(\mathbb E Q_{0,\Pi}\to q_2\). Choose a fixed \(0<q<q_2\);
for all sufficiently large widths both
\(\mathbb E Q_{0,\Pi}\ge q\) and
\(\Pr(Q_0\ge q)\to1\) hold.

The scalar theorem applies at almost every projected Gaussian initialization, so
\[
\bar P_n'(u)=\mathbb E P_{n,\Pi}'(u)
\ge\mathbb E Q_{0,\Pi}\ge q.
\]
The finite-interval derivative bound above justifies the equality. One could
instead take expectations of the strong-monotonicity inequality and avoid
differentiation under expectation. The reference clock is consequently
well defined and stays in \([0,Y/q]\). Its mean query predictor is a
deterministic function for each finite \(n\), bounded in absolute value by
\(Y/q\). It is not asserted to be the mean of the autonomous network.

## 5. All-time probability transfer and the exceptional event

Set \(S=Y/q\) and
\(G_n=\{\|W_0\|_{\rm op}\le K,\ Q_0\ge q\}\).
The probability of its complement tends to zero. On \(G_n\), both clocks
stay in \([0,S]\), and the scalar divided difference is at least \(q\).
Thus
\[
\sup_{t\ge0}|u_n(t)-\bar u_n(t)|
\le q^{-1}\sup_{u\le S}|P_n(u)-\bar P_n(u)|.
\]
The factor two from the physical equations cancels against the integral of
the damping kernel; there is no missing factor of two in this estimate.

Writing
\(\bar f_n^u(x)=\mathbb E f_{n,\Pi}^u(x)\) and using the preceding
query derivative bound \(L_{B,K,S}\), the actual query error on \(G_n\)
is bounded by
\[
\sup_{u\le S}|f_n^u(x)-\bar f_n^u(x)|
+\frac{L_{B,K,S}}q
 \sup_{u\le S}|P_n(u)-\bar P_n(u)|.
\]
The prescribed-control fluctuations apply to both terms. Replacing the
original mean by the projected mean costs only \(CSe^{-cn}\). Squaring,
integrating over queries, and taking expectation proves the candidate's
truncated estimate
\[
\mathbb E[\mathbf1_{G_n}\mathcal E_\mu(f_n,\bar f_n)^2]
\le C_{B,K,Y,q}/n.
\]

For every \(\delta>0\), choose \(n_\delta\) so that
\(\Pr(G_n^c)\le\delta/2\) for \(n\ge n_\delta\), and choose
\(A_\delta^2\ge2C_{B,K,Y,q}/\delta\). Then
\[
\Pr\left\{\mathcal E_\mu(f_n,\bar f_n)>A_\delta/\sqrt n\right\}
\le\Pr(G_n^c)+\frac{C_{B,K,Y,q}}{A_\delta^2}
\le\delta.
\]
This is an unconditional probability statement about actual training. It
does not bound the contribution of \(G_n^c\) to the full mean-square
expectation. No inverse moment of \(Q_0\) is needed for the stated result;
such a moment argument would be needed for a stronger claim that integrated
unrestricted all-time errors using the crude bound \(Y/Q_0\).

For two independent runs at the same width, their deterministic center is
the same. The triangle inequality and a union bound give the stated
root-width run-to-run comparison. Independence is not needed for that union
bound. Comparing different widths would additionally require controlling
their different deterministic centers, which is not proved here.

All these steps use finite controlled curves, initial Gaussian moments, and
scalar contraction. They do not invoke small-label population convergence
at an arbitrary label. Constants may grow with \(Y\), while remaining
independent of width and physical time for each fixed \(Y\).

## 6. Critical diagnostic and remaining scope

For the diagnostic loss, differentiation gives exactly
\(\dot a=(Y-1)a-a^3+\varepsilon\). If \(Y<1\), its equilibrium near
zero has derivative \((1-Y)^{-1}\) with respect to \(\varepsilon\).
At \(Y=1\) and \(\varepsilon>0\), the trajectory from zero increases to
\(\varepsilon^{1/3}\), producing \(n^{-1/6}\) when
\(\varepsilon=n^{-1/2}\). For fixed \(Y>1\), the positive equilibrium
selected by a positive perturbation converges to \(\sqrt{Y-1}\), whereas
the zero-perturbation trajectory remains at zero. These conclusions follow
from the scalar vector-field signs and its positive root.

The candidate repeatedly and correctly excludes this diagnostic from the
canonical dense-network hypotheses. It is a different smooth least-squares
system, with a perturbation parameter chosen as a function of \(n\); it
does not produce a random-width neural-network lower bound. Section 6
therefore does not undermine the one-sample theorem or establish a
slower-than-root canonical dense example.

The checked conclusions retain their stated limits: two hidden tanh layers
for the fluctuation theorem, one normalized training input for the scalar
all-time transfer, finite-width deterministic centering, fixed-confidence
probability rather than unrestricted mean square, and no population-bias
rate. Multi-sample large-label stability remains outside this argument.
