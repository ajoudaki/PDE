# Reconstruction of general-data near-root self-averaging

2026-10-03. Internal collaborative check of the complete
GENERAL_SELF_AVERAGING.md, SHA256
bfbc14cbb3cccf902420db74ca6e3627e341f27a84b52a229362848b376a56d5.
The checker authored the deterministic input
SELF_AVERAGING_FEEDBACK_ROUTE.md, final hash
b3709cac57c005b209dbcaf084848987ee4fe824de0f798d596db8caf6c3554a,
and had already reconstructed the complete same-study fixed-depth
carrier and physical inputs. This is not an isolated promotion review.
No other agent's new sensitivity or energy attempt was read for this
check. No experiments, manuscript changes, or Git operations.

**Verdict: PASS for the stated near-root, fixed-confidence theorem.**
The result is
\[
 \mathcal E_\mu(f_n,f_n')
 \le C_{\delta,\mu}n^{-1/2}e^{K\sqrt{\log(e+n)}}
\]
with probability at least \(1-\delta\) for all sufficiently large
widths depending on \(\delta\). It is not a strict
\(C_{\delta,\mu}n^{-1/2}\) theorem. No unconditional all-time variance
or expected squared error of the original autonomous network is proved.
These distinctions are maintained correctly in the source.

## 1. Deterministic hypotheses and Gaussian coordinates

The model, canonical mobilities, Gaussian normalization, zero readout,
fixed depth, and \(C^3\) activation condition agree with the completed
depth theorem. Activation values may grow linearly. Its data assumptions
are either an explicit positive limiting feature-Gram gap or one of the
proved automatic-gap/parity-quotient cases. Labels are fixed and small.

The root vector
\[
 G=(W_0^1,\sqrt n W_0^2,\ldots,\sqrt n W_0^L)
 \in\mathbb R^{nd+(L-1)n^2}
\]
is a vector of independent standard Gaussians. The readout is zero and
adds no random coordinate. The proof uses a deterministic good set
\(\Omega_n\) with probability tending to one, on which both the
all-time physical bounds and the carrier maximum
\[
 M_n=C_0Y\sqrt{\log(e+n)}
\]
hold with fixed constants. No rate for
\(\mathbb P(\Omega_n^c)\to0\) is assumed.

For fixed positive sample weights, the exact residual damping matrix is
\(D_p\Lambda D_p\), with
\(D_p=\operatorname{diag}(\sqrt{p_a})\) and
\(\Lambda_{ab}=n^{-1}\langle\nabla_\Theta\mathcal F_a,
                              \nabla_\Theta\mathcal F_b\rangle\).
The source explicitly gives this convention. Therefore compatible data
quotients preserve the physical time and original residual RMS rather
than silently changing the training equation.

## 2. Pairwise stability is valid on the whole good set

For two roots in \(\Omega_n\), let \(D\) be the sum of the normalized
first-layer/readout discrepancies and ordinary hidden Frobenius
discrepancies. Forward subtraction uses only globally bounded slopes
and the two trajectories' operator/RMS bounds. Backward subtraction
puts the reference carrier in the gate-difference term, giving
\[
 \|\Delta\delta_a^\ell\|_{\rm rms}
 \le C[D_w+(M_n+Y)D_h].
\]
Only one trajectory's carrier maximum is needed. Product subtraction
of parameter gradients then bounds the tangent-matrix difference.
The source uses the looser valid estimate
\(\|\Delta\Gamma\|\le C(1+M_n)D\).

The two residuals initially agree because both readouts are zero.
Their exact difference satisfies
\[
 \dot e=-2\widetilde\Gamma e
          -2(\widetilde\Gamma-\Gamma)r,\qquad e(0)=0.
\]
The uniform tangent gap yields the exponentially decaying
nonautonomous propagator. Integration of its convolution gives
\[
 \int_0^t\|e(s)\|_m\,ds
 \le C(1+M_n)\int_0^t\rho(s)D(s)\,ds.
\]
Subtracting parameter equations and using this estimate gives Gronwall
against \(\rho(s)ds\), whose total mass is \(O(Y)\):
\[
 \sup_tD(t)\le Ce^{CY(1+M_n)}D(0),\qquad
 D(0)\le C_L\|G-\widetilde G\|_2/\sqrt n.
 \tag{A}
\]
The estimate holds for arbitrary pairs in the good set. The proof never
requires the line joining their parameter states to satisfy a Gram gap
or a carrier bound, and no small-distance bootstrap is hidden in (A).

For \(B(x)=1+\|x\|/\sqrt d\), forward query subtraction and the
readout product give the good-set Gaussian-root Lipschitz estimate
\[
 \sup_t|f_G(t,x)-f_{\widetilde G}(t,x)|
 \le B(x)\ell_n\|G-\widetilde G\|_2,\qquad
 \ell_n=Cn^{-1/2}e^{K_0\sqrt{\log(e+n)}} .
 \tag{B}
\]
The constants in this expression are deterministic.
Query carrier maxima are unnecessary: query backward RMS is controlled
by bounded slopes, hidden operators, and readout RMS.

The physical query gradient has normalized norm at most \(CB(x)\).
Its pairing with a training gradient therefore bounds the query speed
by \(CB(x)\rho(t)\). Consequently
\[
 |f_G(t,x)|\le CYB(x),\qquad
 |\partial_t f_G(t,x)|\le CYB(x)e^{-\kappa t}.
 \tag{C}
\]
These bounds establish the source's linear, rather than quadratic,
growth in query norm.

## 3. Time compactification and scalar extension

Put \(u=1-e^{-\kappa t}\), with \(u=1\) at the fitted endpoint.
Equation (C) gives
\[
 |f_G(t(u),x)-f_G(t(v),x)|\le CB(x)|u-v|,
 \quad G\in\Omega_n.
 \tag{D}
\]
The omitted factor \(Y/\kappa\) has been included in the fixed constant.
Integrability of all physical parameter speeds gives the endpoint; (D)
is valid there by taking the limit.

For the grid \(u_j=j/n\), extend each scalar value by
\[
 \widetilde F_{j,x}(G)
 =\inf_{H\in\Omega_n}
    \{f_H(t(u_j),x)+B(x)\ell_n\|G-H\|_2\}.
 \tag{E}
\]
For sufficiently large \(n\), \(\Omega_n\) is nonempty.
The prediction is bounded below on that set, and a fixed element gives
a finite upper bound for (E); thus the extension is finite everywhere.
For \(G\in\Omega_n\), (B) implies that every expression inside the
infimum is at least \(f_G(t(u_j),x)\), while \(H=G\) attains equality.
The triangle inequality proves its global \(B(x)\ell_n\)-Lipschitz
constant.

Clipping this auxiliary scalar extension to the interval
\([-CYB(x),CYB(x)]\) preserves agreement on \(\Omega_n\) and the
same global Lipschitz constant. This clipping is not applied to any
network or training signal. It makes the extension bounded and
integrable under the unrestricted Gaussian initialization law.

Measurability is valid. Every subset of finite-dimensional Euclidean
space has a countable dense subset in its relative metric. Fix one for
\(\Omega_n\), independently of the query. The Lipschitz property in
(B) implies that the infimum over this subset equals (E).
For each of its fixed roots, finite-time predictions are continuous in
the query; endpoint predictions are pointwise limits and hence Borel.
The countable infimum and the subsequent clipping are jointly Borel in
\((G,x)\). No uncountable measurability assumption is required.

Let \(F_{j,x}\) denote this clipped extension and put
\[
 c_{n,j}(x)=\mathbb E F_{j,x}(G).
\]
Its linear interpolation in \(u\) defines the deterministic center
\(c_n(t(u),x)\). The expectation here is of the scalar extension under
the full Gaussian law. It is neither a conditional expectation on
\(\Omega_n\) nor the mean of the actual autonomous predictor.

## 4. Dimension-independent concentration and the grid maximum

The source supplies a valid proof of Gaussian Lipschitz concentration.
For positive smooth \(h\), the Ornstein--Uhlenbeck identity is
\[
 \operatorname{Ent}(h)
 =\int_0^\infty
       \mathbb E\frac{\|\nabla P_t h\|^2}{P_t h}\,dt .
\]
Using \(\nabla P_t h=e^{-t}P_t\nabla h\), weighted
Cauchy--Schwarz inside the semigroup, its Gaussian invariance, and
\(\int_0^\infty e^{-2t}dt=1/2\), gives
\[
 \operatorname{Ent}(h)
 \le\frac12\mathbb E\frac{\|\nabla h\|^2}{h}.
\]
For \(h=e^{\lambda F}\), \(\|\nabla F\|\le l\), the resulting
inequality
\(\lambda\psi'(\lambda)-\psi(\lambda)\le\lambda^2l^2/2\),
\(\psi=\log\mathbb E e^{\lambda F}\), integrates to
\[
 \log\mathbb E e^{\lambda(F-\mathbb EF)}
 \le\lambda^2l^2/2.
\]
Both signs of \(\lambda\) give
\[
 \mathbb P(|F-\mathbb EF|>s)\le2e^{-s^2/(2l^2)}.
 \tag{F}
\]
Smooth bounded approximation establishes (F) for the bounded Lipschitz
extensions in (E). No factor depending on the Gaussian root dimension
enters.

A union bound over \(n+1\) grid values uses no independence between
them. With \(l=B(x)\ell_n\) and
\(A_x=\max_j|F_{j,x}-c_{n,j}(x)|\),
\[
 \mathbb P(A_x^2>s)\le
       \min\{1,2(n+1)e^{-s/(2l^2)}\}.
\]
Integration, split at \(2l^2\log(2n+2)\), gives
\[
 \mathbb E A_x^2\le C B(x)^2\ell_n^2\log(e+n).
 \tag{G}
\]
The tail integral after that split is at most \(2l^2\), as asserted
in the source.

## 5. Restricted expectation, query integration, and confidence

On \(\Omega_n\), (D) bounds the error between the actual prediction
and the linear interpolation of its own grid values by \(CB(x)/n\).
The difference between that interpolation and the center interpolation
is at most \(A_x\). Thus (G) gives
\[
 \mathbb E\left[
 {\bf1}_{\Omega_n}\sup_{t\in[0,\infty]}
       |f_n(t,x)-c_n(t,x)|^2\right]
 \le CB(x)^2[\ell_n^2\log(e+n)+n^{-2}].
 \tag{H}
\]
The integrand on the left is defined to be zero off the good set.
No fitted endpoint or integrability of the actual off-event trajectory
is assumed.

This is the essential probability distinction: the right-hand side
comes from the unconditional Gaussian concentration of the extension.
The left-hand side retains the good-set indicator. Removing that
indicator would not be justified by a merely qualitative
\(\mathbb P(\Omega_n^c)\to0\).

By joint measurability and Tonelli, (H) integrates against the query
law. Its only query factor satisfies
\[
 \int B(x)^2\,d\mu(x)
 \le2+2d^{-1}\int\|x\|^2\,d\mu(x)<\infty .
\]
There is no net over queries and no higher query moment assumption.

Fix \(0<\delta<1\). For sufficiently large width the good-set
complement has probability at most \(\delta/2\).
Apply Markov to the restricted integrated squared error at threshold
\[
 \frac{2C_\mu}{\delta}
       [\ell_n^2\log(e+n)+n^{-2}].
\]
The other failure probability is at most \(\delta/2\).
After taking square roots, absorb
\(\sqrt{\log(e+n)}\) into a fixed enlargement of the exponent
\(K_0\sqrt{\log(e+n)}\). This proves the source's center estimate
with constants independent of \(n\) and physical time.
The width threshold may depend on confidence, as stated.

Use this same deterministic center for both copies, take the one-copy
failure probability to be \(\delta/2\), and apply a union bound and
the triangle inequality in the query/time norm. This gives the claimed
independent-copy theorem. Independence is not required by the union
bound; the two correct marginal Gaussian laws suffice.

## 6. Rate, scope, and the strict obstruction

The bound is strictly weaker than root width: its factor
\(e^{K\sqrt{\log(e+n)}}\) is unbounded. Small fixed labels may reduce
\(K\), but do not make the factor constant unless further sensitivity
information is proved. For every fixed \(\varepsilon>0\), the
elementary inequality
\[
 K\sqrt{\log(e+n)}\le
       \varepsilon\log(e+n)+C_{\varepsilon,K}
\]
does give \(C_{\delta,\mu,\varepsilon}n^{-1/2+\varepsilon}\).
Neither this rewriting nor the concentration argument proves a strict
\(C_{\delta,\mu}n^{-1/2}\) bound.

The exact Gaussian sensitivity identity in the source is correct:
\[
 \nabla_G f_n(t,x)
       =P^\top J(t,0)^\top g_x(t)/n ,
\]
where \(P\) embeds the initialized random blocks into mobility-Euclidean
coordinates. A bound on the squared norm of this specific adjoint
response, with appropriate time increments and localization, could
give the strict rate. A normalized Hilbert--Schmidt estimate is
insufficient. The source's example
\[
 R=a_nuv^\top,\qquad g=\sqrt n\,u,\qquad
 a_n=e^{c\sqrt{\log(e+n)}}
\]
has \(\|R\|_{\rm HS}/\sqrt n\to0\), while
\(\|R^\top g\|/\sqrt n=a_n\to\infty\).
Every fixed normalized Schatten norm also tends to zero.
This verifies the failed inference; it is not a neural-network
counterexample, and the source does not claim that it is one.

The separately proved strict closure-to-dense tracking estimate can
be added by triangle inequality and a union of the good events.
It leaves the independent-copy comparison at the near-root rate.
The source correctly retains fixed depth, small fixed labels, and
the explicit/automatic initial Gram hypotheses, and distinguishes
moving state from the quadratic storage of the fixed mixers.

Finally, concentration around a finite-width center cancels common
bias between copies. It gives no numerical population-bias estimate.
The identity \( \mathbb E|f_n-f_n'|^2=2\operatorname{Var}(f_n)\)
requires a finite second moment at the fixed time and query in
question; it is correctly presented only with that qualification.
No statement about the unconditional all-time variance of the original
training flow is inferred from the restricted estimate (H).

No mathematical correction to the frozen candidate was required.
