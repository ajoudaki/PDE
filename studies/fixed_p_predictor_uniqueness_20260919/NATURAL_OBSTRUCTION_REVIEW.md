# Informed internal check of the canonical noise counterexample

2026-09-19. **Verdict: the specified canonical-start counterexample and scalar
isotropic-decay obstruction are mathematically supported, with the scope and
wording qualifications below.** No fatal or major proof gap was found in the
reviewed claims. This is an informed internal check, not an isolated independent
review, promotion approval, or an audit of every claim in the source report.

## Inputs, coverage, and isolation

The additional scientific input was the complete NATURAL_NOISE_OBSTRUCTIONS.md,
SHA-256
81a92c1dd43c3e5b48ddf71e7dbcbe745bc1617d49531f967f925e7ff1751bfe.
Earlier permitted scientific inputs were the complete MODEL_AND_GEOMETRY.md
and CANONICAL_FEATURES.md, with hashes recorded in NATURAL_PENALTY_ROUTE.md.
This reviewer had already authored that penalty route before receiving this
assignment, so the present check is explicitly informed.

The mathematical audit covers §1.1–§1.3, the qualifications of their claims in
the contract, §1's exact-scope paragraph and final ledger, and §5.2. The report
was read completely to check those scope qualifications; §§2–4, §5.1, §5.3,
and §6 were not exhaustively audited here. No other route or scientific source,
experiment, external material, or unrelated agent summary was retrieved.

The source author discloses exposure to unrelated completed-agent summaries
after deriving and reporting the principal constructions. This reviewer did
not retrieve those summaries and cannot certify what that exposure contained.
The derivation below is checkable from the permitted scientific inputs, but
neither this check nor the derivation restores the author's fully isolated
status. Only this review file was written; no Git-index operations occurred.

## 1. Cholesky coordinate blocks are preserved

This part is correct, including the original interleaved dictionary order.
To make the assertion directly checkable, use the canonical moments
\(v,\gamma,\beta\) and ridge \(\eta>0\), and put

\[
 \ell=\sqrt{v+\eta},\qquad
 s=\sqrt{\gamma+\eta-\beta^2/(v+\eta)}>0.
\]

In the original lower ordering \((1,h_1,h_2,T_1,T_2)\), the positive-diagonal
Cholesky factor has only the diagonal and the two additional entries

\[
 L_{31}=\beta/\ell,\qquad L_{42}=\beta/\ell
\]

when indices start at zero. Its diagonal is
\((\sqrt{1+\eta},\ell,\ell,s,s)\). Therefore the transformed fields are

\[
 b_1=\left(
 \frac1{\sqrt{1+\eta}},
 \frac{h_1}{\ell},\frac{h_2}{\ell},
 \frac{T_1-\beta h_1/(v+\eta)}s,
 \frac{T_2-\beta h_2/(v+\eta)}s
 \right).
\]

Permuting the last four coordinates into coordinate-pair order yields exactly
the claimed constant/pair-one/pair-two decomposition. Each nonconstant pair is
centered, bounded, and odd under its own simultaneous Gaussian-mark sign flip.
The two pairs are independent. The upper Cholesky factor is diagonal, giving
\(b_2=(1/\sqrt{1+\eta},dZ_1,dZ_2)\) with
\(d=(\tau+\eta)^{-1/2}\).

The raw contraction has support only from each upper coordinate to its matching
lower pair. Multiplication by \(L_2^{-1}\) and \(L_1^{-T}\) preserves that
support, so \(D\) has exactly the asserted two blocks. A lower-coordinate
permutation must also permute the columns of \(M\); doing so preserves the
physical Frobenius norm and every represented contraction. No implicit change
of the physical metric is being used.

## 2. Cancellation holds in the full physical hidden gradient

Let \(q(Z_2)=\tanh(\kappa_0Z_2)-bZ_2\), where
\(b=E[Z_2\tanh(\kappa_0Z_2)]/\tau\). The identities

\[
 Eq=0,\qquad E[qZ_2]=0,\qquad
 E[q\tanh(\kappa_0Z_2)]=\|q\|_2^2
\]

follow by oddness and orthogonal projection onto the one-dimensional span of
\(Z_2\). Strict positivity of \(\|q\|_2^2\) follows from positive density on
\((-1,1)\) and the nonzero cubic derivative of \(\tanh(\kappa_0 z)\). Thus the
noise direction is nonzero and is visible at the proposed query.

In the stated invariant family, the training lower feature has only pair-one
entries. Hence \(H(e_1)=\tanh(\kappa Z_1)\). For
\(c=C(Z_1)+Xq(Z_2)\), the hidden adjoint

\[
 U=E[c\,\operatorname{sech}^2(\kappa Z_1)b_2]
\]

has constant component zero and upper-coordinate-two component zero. The
coordinate-one component is

\[
 U_1=d\,E[C(Z_1)Z_1\operatorname{sech}^2(\kappa Z_1)],
\]

independent of \(X\). The cancellations use, respectively, oddness of \(C\),
\(Eq=0\), \(EZ_2=0\), and \(E[qZ_2]=0\). They hold for every current
\(\kappa\), rather than only at initialization.

The actual gradients then give

\[
 \dot M=2rUa^T,\qquad
 \dot w=2r\operatorname{sech}^2W\,(b_1^TM^TU)e_1,
 \qquad \dot C=2r\tanh(\kappa Z_1).
\]

Thus only the first middle block changes, and the lower increment is a
pair-one-dependent odd function in the first physical coordinate. In
particular, using the actual \(M^T\) does not introduce the untouched block.
The family is invariant under both the drift and the additive \(q\) noise.
There is no substituted independent backward matrix.

One useful clarification of the source's gradient notation is to define
\(\kappa\) on the ambient hidden space, not merely on the invariant family:

\[
 \kappa(h)=d\,e_{\mathrm{upper},1}^{\,T}M a_h(e_1).
\]

On the family this is the coefficient of \(Z_1\) in the training
preactivation. Since the other components of \(U\) vanish, the full physical
hidden differential of the prediction is exactly
\[
 D_h f[v]=\rho\,D\kappa[v],\qquad
 \rho=E[C(Z_1)Z_1\operatorname{sech}^2(\kappa Z_1)].
\]
This establishes the full-gradient norm in source equation (7); it is not
merely a derivative along a reduced coordinate curve.

## 3. Scalar monotonicity and exponential fitting close

With \(r=1-f(e_1)\), the reviewed equations are

\[
 \dot C(z)=2r\tanh(\kappa z),\quad
 \dot\kappa=2r\rho\|\nabla_h\kappa\|^2,\quad
 \dot r=-2r\{K(\kappa)+\rho^2\|\nabla_h\kappa\|^2\}.
\]

They include both the readout and hidden contributions to the prediction
derivative. On every compact interval of local existence the coefficient in
the last equation is finite, giving its integrating-factor solution and
\(r(t)>0\). Starting from \(\kappa_0>0\), positivity of \(\kappa\) implies
\(C_t(z)z\ge0\), hence \(\rho\ge0\) and \(\dot\kappa\ge0\). A first-exit
argument prevents \(\kappa\) from leaving the positive region. This is a valid
bootstrap, not an assumed persistent-kernel bound.

For \(t>0\), one in fact has \(C_t(z)z>0\) for every nonzero \(z\), and hence
\(\rho(t)>0\). Also \(\nabla_M\kappa=d\,e_{\mathrm{upper},1}a^T\ne0\):
if \(a=0\), then \(\kappa=0\), contrary to the established positivity.
Consequently \(\kappa\) strictly increases for positive times. The training
upper gate is not frozen.

Since \(\tanh^2(\kappa z)\) is nondecreasing in positive \(\kappa\), the lower
bound \(K(\kappa)\ge k_0=K(\kappa_0)>0\) follows. It gives

\[
 r(t)\le e^{-2k_0t},\qquad L(t)\le e^{-4k_0t},\qquad
 \|C_t\|_\infty\le k_0^{-1}.
\]

The cancellation of \(Xq\) is essential: these bounds and the entire
deterministic base flow are independent of the realized readout noise.

## 4. Global existence and physical-state convergence are justified

The source's continuation argument is sound. Here are explicit bounds
completing its “analogous integrable bound” step. Put

\[
 M_*=\|D\|_{\mathrm{op}}+\frac{B_1B_2}{k_0^2}.
\]

The adjoint satisfies \(\|U\|\le B_2/k_0\), so

\[
 \|\dot M\|_F\le\frac{2B_1B_2}{k_0}e^{-2k_0t},
 \qquad \|M_t\|_{\mathrm{op}}\le M_*,
\]

and the actual lower equation gives

\[
 \|\dot w\|_2\le
 \frac{2B_1B_2M_*}{k_0}e^{-2k_0t}.
\]

It follows that

\[
\begin{split}
 \|M_\infty-M_t\|_F&\le\frac{B_1B_2}{k_0^2}e^{-2k_0t},\\
 \|w_\infty-w_t\|_2&\le\frac{B_1B_2M_*}{k_0^2}e^{-2k_0t},\\
 \|C_\infty-C_t\|_\infty&\le k_0^{-1}e^{-2k_0t}.
\end{split}
\]

Bounded dictionary fields and bounded tanh derivatives make the drift locally
Lipschitz in the physical Hilbert norm on these bounded sets. The displayed
velocity bounds make the state Cauchy at any finite candidate maximal time;
the limit is an admissible finite-norm state where local existence restarts.
This proves continuation without appealing to compactness of a Hilbert ball.

For the stochastic extension, the explicit
\(X_t=\varepsilon\int_0^{t\wedge1}(1-s)dB_s\) has continuous, almost surely
bounded sample paths on every finite interval and is exactly constant after
time one. The constructed \(c_t=C_t+X_tq\), together with the deterministic
hidden flow, solves the full SDE. Local uniqueness follows by subtracting two
solutions driven by the same Brownian motion: the additive noise cancels, and
the locally Lipschitz drift gives the integral Gronwall estimate. Thus the
invariant construction identifies the actual canonical-start solution.
After time one the full physical state converges exponentially.

The uniform-circle predictor convergence also follows. For hidden states with
\(\|M\|_{\mathrm{op}}\le M_*\), the feature difference is bounded uniformly
over unit input directions by a finite multiple of
\(\|w-w'\|_2+\|M-M'\|_F\), using tanh Lipschitzness and bounded dictionaries.
Pairing with the bounded-in-time, finite-norm readout gives the claimed
uniform convergence, with a realization-dependent finite constant.

## 5. Query variance, Brownian scope, and balanced labels

The query at \(e_2\) sees only the unchanged lower coordinate and second middle
block. Therefore its hidden field is exactly
\(\tanh(\kappa_0Z_2)\) at every time. Independence and oddness remove the
\(C_t(Z_1)\) contribution, giving

\[
 f_t(e_2)=X_t\|q\|_2^2,\qquad
 \operatorname{Var}f_\infty(e_2)=
       \frac{\varepsilon^2}{3}\|q\|_2^4>0.
\]

The variance follows from a one-dimensional deterministic-integrand Itô
integral; the source provides the sufficient step-function derivation. There
is no Itô correction in the training prediction, since its dependence on the
forced readout coordinate vanishes identically. Multiplication of the
diffusion coefficient by the deterministic positive residual \(r(t)\) retains
strictly positive terminal variance exactly as claimed.

**A wording qualification is needed for “bounded, arbitrarily small noise.”**
What is uniformly bounded and arbitrarily small is the diffusion coefficient
in the rank-one Hilbert-space noise operator:
\[
 \|\varepsilon(1-t)_+q\|_2\le\varepsilon\|q\|_2.
\]
The Brownian sample displacement has no deterministic bound proportional to
\(\varepsilon\), although it is almost surely finite on the compact forcing
interval. Nor is Brownian forcing a bounded-velocity ODE perturbation. The
source's explicit SDE and exact-scope paragraph make the intended meaning
recoverable, but its opening conclusion should say “bounded diffusion
coefficient” to avoid asserting a stronger noise class.

The example is compatible with ordinary label balance. Replace the single
example by

\[
 (\sqrt2e_1,+1,\tfrac12),\qquad
 (-\sqrt2e_1,-1,\tfrac12).
\]

Every represented predictor is odd, so its loss is exactly
\[
 \tfrac12(f(e_1)-1)^2+
 \tfrac12(f(-e_1)+1)^2=(f(e_1)-1)^2.
\]
Moreover \(Df(-e_1)=-Df(e_1)\), so the two individual square-loss gradients
are identical, not merely their average. Merging the compatible antipodal
constraints yields precisely the author's one-representative example. Thus
requiring equal counts or mass of positive and negative labels does not
exclude the counterexample.

This does not establish an obstruction for two or more distinct antipodal
classes, or for almost every dataset sampled from a continuous distribution.
If “balanced” were intended to impose such additional geometric restrictions,
the present example would not settle that stronger question. It does refute a
guarantee quantified over every finite compatible balanced dataset. Even in
the two-example balanced presentation, minibatch sampling produces no
randomness because the individual gradients coincide. The rank-one Brownian
forcing must not be called ordinary SGD noise.

## 6. The scalar decay obstruction is correct at its stated scope

For any locally integrable \(\lambda\ge0\), the scalar system

\[
 \dot r=2(1-r)-\lambda r,\qquad
 \dot z=-\lambda z,\qquad r(0)=0
\]

has unique absolutely continuous solutions by the integrating-factor formula.
Both \(r\ge0\) and \(u=1-r\ge0\) follow from their integrating-factor
solutions, so \(0\le r\le1\). The exact tangent solution is

\[
 z(t)=z(T)\exp\!\left[-\int_T^t\lambda(s)\,ds\right].
\]

Erasing every nonzero deposited tangent value therefore requires infinite
tail integral of \(\lambda\). If \(L(t)=(1-r(t))^2\le Ce^{-\eta t}\),
then \(u(t)\le\sqrt C e^{-\eta t/2}\), so \(u\) is integrable and
\(r(t)\to1\). Integrating the first equation gives

\[
 \int_T^t\lambda(s)r(s)\,ds
 =2\int_T^t u(s)\,ds-r(t)+r(T).
\]

The left side is monotone nonnegative and bounded by the right-side estimate.
Eventually \(r\ge1/2\), whence the nonnegative tail integral of \(\lambda\)
is finite. Local integrability controls the preceding finite interval.
Thus an exponential loss tail leaves a strictly positive fraction of every
nonzero tangent value. No monotonicity, differentiability, or convergence
assumption on \(\lambda\) was smuggled into this implication.

For the displayed schedule \(\lambda=1/(1+t)\), substitution verifies
\[
 u(t)=\frac{1+e^{-2t}}{2(1+t)},\qquad z(t)=\frac{z(0)}{1+t}.
\]
The loss is asymptotic to \(1/[4(1+t)^2]\), as claimed.

This is an exact obstruction for nonnegative scalar isotropic decay acting
simultaneously on the fitted and tangent coordinates. It does not exclude
direction-dependent penalties, compensated drift, constraints, or more general
coupled nonlinear selectors. The source states this limitation correctly.

## Review disposition

The checked claims can be used as internally supported study results with the
source's declared informed/nonisolated status retained. The source should
prefer “bounded diffusion coefficient” in its headline noise claim, and may
add the explicit ambient definition of \(\kappa\) and balanced antipodal
presentation above for clarity. These are precision improvements, not repairs
of the principal counterexample or scalar obstruction.

The decisive supported conclusion is narrow and exact: arbitrarily small,
eventually vanishing, genuine rank-one Brownian readout noise can leave a
random limiting predictor from canonical initialization, even while the
original full physical gradient drift fits exponentially and its state
converges. Neither this example nor the scalar decay argument proves failure
of every noisy optimizer, of ordinary SGD on general datasets, or of the
original deterministic canonical initial-value problem.

## 7. Scoped closure: bounded random-ODE extension

After the core review above, the supervisor supplied an amended source with
SHA-256
890de9f524fe6777ce9e54e97245f9b8be80a14bc892d88d7f31fd3be01dd010.
This reviewer verified that hash and read the complete added “Bounded
random-ODE corollary” in §1.3, its surrounding Brownian argument, its scope
qualification, and the amended provenance paragraph. The earlier review
retains its original frozen-source coverage. This appendix is an informed
check of the supplied extension, not an additional isolated review.

**The bounded-velocity extension is correct.** Conditional on the random sign
\(\xi\in\{-1,+1\}\), solve the ordinary physical-state ODE with additional
readout velocity

\[
 \varepsilon\xi(1-t)_+q.
\]

Its norm is deterministically bounded by \(\varepsilon\|q\|_2\), it is
continuous in time, and it vanishes at and after time one. The complete
canonical initialization is unchanged. The already checked adjoint
cancellation holds for every scalar \(X\), so the hidden state, readout
component \(C\), and training residual coincide with the deterministic base
flow for both sign realizations. The only new equation is

\[
 \dot X=\varepsilon\xi(1-t)_+,\qquad X(0)=0.
\]

It has the claimed explicit solution and endpoint

\[
 X_t=\varepsilon\xi
       \left[(t\wedge1)-\frac{(t\wedge1)^2}{2}\right],
 \qquad X_\infty=\frac{\varepsilon\xi}{2}.
\]

The canonical query identity remains \(f_t(e_2)=X_t\|q\|_2^2\).
Because the two signs have equal probability,

\[
 \operatorname{Var}f_\infty(e_2)
    =\frac{\varepsilon^2}{4}\|q\|_2^4>0.
\]

Existence, uniqueness, exponential training loss, full-state convergence, and
uniform predictor convergence follow from the previously checked invariant
decomposition and explicit bounded \(X_t\); no stochastic differential
existence theorem is needed for this version.

For the residual-vanishing velocity
\(\varepsilon\xi r(t)(1-t)_+q\), the same cancellation leaves \(r\)
deterministic, continuous, and strictly positive on \([0,1]\), with
\(r\le1\). Consequently the velocity has the same deterministic norm bound,
and

\[
 X_\infty=\varepsilon\xi I,\qquad
 I=\int_0^1r(s)(1-s)\,ds>0,\qquad
 \operatorname{Var}f_\infty(e_2)=\varepsilon^2I^2\|q\|_2^4>0.
\]

This checks both newly displayed variance formulas, including their factors.
The balanced antipodal presentation in §5 of this review applies without
change.

This extension closes the **coverage** limitation identified in §5: the
obstruction now holds for uniformly bounded, finite-duration random ODE
velocities as well as for Brownian forcing with bounded diffusion
coefficient. The two variants have different laws: a two-point random
endpoint for the ODE and a Gaussian endpoint for the Brownian SDE. The
original Brownian wording qualification remains a useful precision note; one
should not describe its sample velocity as uniformly bounded.

The ODE forcing is an external random forcing indexed by an independent
random sign. It is not asserted to be a Brownian diffusion, a martingale
increment process, or ordinary minibatch noise. Also it is invisible to the
original loss gradient along the constructed family, but need not be tangent
to an augmented selection objective. The source's final corollary paragraph
correctly preserves that distinction. The valid conclusion is therefore the
failure of a guarantee based only on smallness and disappearance of noise,
even with a deterministic bound on the perturbation velocity. No blanket
failure theorem for designed selection drifts follows.
