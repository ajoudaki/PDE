# Independent delay and metric route

Status: frozen independent prompt-only derivation, 2026-09-19. No experiments. This report uses only the supervisor's supplied mathematical inputs and the required research/mathematics process instructions. It does not independently establish the canonical closure or the corrected-optimizer theorem.

The supplied assumptions permit any diverging delay, including a log-log delay, for qualitative convergence to gradient flow on compact time intervals. This does **not** establish a substantive speedup at a fixed gradient-flow approximation tolerance. The activation time and its discounted intervention cost obey an exact logarithmic relation, and a fixed exponential rate generally comes with a growing all-time prefactor. The actual state-distance metric has an upper certificate from this construction, without a supplied matching lower bound.

## Contract and supplied input

Fix the canonical closure at either \(p=1\) or \(p=2\), its gradient-flow trajectory \(S_0(t)\), and its continuous nonnegative nonincreasing loss \(L_0(t)\), with \(L_{\rm init}=L_0(0)<\infty\). Let \(\lambda>0\) be fixed independently of \(\varepsilon\), and let the corrected optimizer have fixed correction strength \(\lambda/4\). The supplied theorem says that from each regular positive-Gram state at time \(s\), this optimizer has

\[
L(s+t)\le L(s)e^{-\lambda t}\qquad(t\ge0)
\]

and converges strongly to a finite fitted endpoint. Here “finite endpoint” means a finite limiting state as time tends to infinity; it does not assert hitting zero loss at a finite time.

The supplied singular-time condition is that the set \(\mathcal N\) of Gram-singular times on the GF trajectory is countable. Application of the supplied theorem additionally requires that \(S_0(t)\) is regular at the chosen nonsingular activation time. The prompt names the canonical regular flow but supplies no closure equations with which to reprove that regularity. All conclusions below using the theorem are conditional on this required regularity. If other irregular times exist, their avoidance requires a separate hypothesis.

Only physical continuous time is used. There is no time rescaling, increase in correction strength, altered canonical \(p\), or trajectory oracle. The algorithm runs the canonical GF equations before switching. Its only varying design choice below is its stated activation delay. No numerical cost or conditioning theorem is assumed.

## Construction and its exact GF phase

Let \(h(\varepsilon)\ge0\) be any deterministic function tending to infinity as \(\varepsilon\downarrow0\). Draw \(V\) uniformly from \((0,1)\), put

\[
A_\varepsilon=h(\varepsilon)+\frac V\lambda,
\]

follow GF through time \(A_\varepsilon\), and then use the supplied corrected optimizer initialized at \(S_0(A_\varepsilon)\). Choose the optional noise to be identically zero; this satisfies every proposed upper noise bound.

For each fixed \(\varepsilon\), \(A_\varepsilon\) has an absolutely continuous law. Each element of the countable set \(\mathcal N\) has probability zero, and countable additivity gives

\[
\mathbb P(A_\varepsilon\in\mathcal N)=0.
\]

Subject to the stated regularity, the corrected-optimizer theorem therefore applies almost surely. The resulting trajectory has a finite strong fitted endpoint, and

\[
S_\varepsilon(t)=S_0(t),\quad L_\varepsilon(t)=L_0(t)
\qquad(0\le t\le A_\varepsilon).
\]

Its certified exact-GF phase has duration \(A_\varepsilon\in(h,h+1/\lambda)\). This is not a claim that the two trajectories become different immediately after activation. The guarantee of exact agreement through a deterministic horizon \(T\) has probability

\[
\mathbb P(A_\varepsilon\ge T)=
\begin{cases}
1,&T\le h,\\
1-\lambda(T-h),&h<T<h+1/\lambda,\\
0,&T\ge h+1/\lambda.
\end{cases}
\]

Actual agreement can hold with greater probability because the corrected flow might coincide with GF after activation.

For every fixed \(T<\infty\), eventually \(h(\varepsilon)\ge T\), so the trajectories are exactly equal on \([0,T]\). This proves compact-uniform convergence wherever the family is defined, without a stability estimate. For a prescribed countable sequence \(\varepsilon_n\downarrow0\), the almost-sure activation statements hold simultaneously, including when one common \(V\) couples the sequence. For a continuum of parameters, “for each \(\varepsilon\), almost surely” does not itself give a common full-probability event for all \(\varepsilon\). No such uncountable interchange is needed for the fixed-parameter estimates or sequential convergence. A simultaneously admissible continuum construction would require a specified selection or exceptional-parameter convention.

## Exponential rate, exact prefactor, and fitting time

For almost every valid realization,

\[
L_\varepsilon(t)\le
\begin{cases}
L_0(t),&t\le A_\varepsilon,\\
L_0(A_\varepsilon)e^{-\lambda(t-A_\varepsilon)},&t\ge A_\varepsilon.
\end{cases}
\]

The first line is equality. In particular,

\[
L_\varepsilon(t)\le L_{\rm init}e^{-\lambda(t-A_\varepsilon)_+}
\le eL_{\rm init}e^{\lambda h(\varepsilon)}e^{-\lambda t}.
\tag{1}
\]

Thus the tail rate \(\lambda\) is fixed; a sufficient deterministic all-time prefactor is \(eL_{\rm init}e^{\lambda h}\).

There is also an exact expression for the smallest all-time prefactor at this rate:

\[
K_\varepsilon
:=\sup_{t\ge0}e^{\lambda t}L_\varepsilon(t)
=K_0(A_\varepsilon),\qquad
K_0(a):=\max_{0\le t\le a}e^{\lambda t}L_0(t).
\tag{2}
\]

Indeed, continuity makes the finite-interval maximum exist. The GF prefix forces the right side as a lower bound on \(K_\varepsilon\); on the tail the theorem gives
\(e^{\lambda t}L_\varepsilon(t)\le e^{\lambda A_\varepsilon}L_0(A_\varepsilon)\le K_0(A_\varepsilon)\), giving the reverse inequality. No prefactor divergence follows solely from decreasing loss. It does follow whenever \(\sup_{t\ge0}e^{\lambda t}L_0(t)=\infty\).

For a fixed positive loss tolerance \(\delta\), define

\[
\tau_\varepsilon(\delta)=\inf\{t\ge0:L_\varepsilon(t)\le\delta\}.
\]

If \(L_{\rm init}\le\delta\), this time is zero. Otherwise, using \(\log_+x=\max\{0,\log x\}\) for \(x>0\) and \(\log_+0=0\), the tail estimate proves

\[
\tau_\varepsilon(\delta)
\le A_\varepsilon+\frac1\lambda\log_+\frac{L_0(A_\varepsilon)}\delta
\le h(\varepsilon)+\frac{1+\log_+(L_{\rm init}/\delta)}\lambda.
\tag{3}
\]

If GF has already reached \(\delta\) by activation, the first fitting time is its GF fitting time, independently of the later switch. Consequently (3) does not imply that fitting time actually diverges. Let \(\ell=\lim_{t\to\infty}L_0(t)\), which exists by monotonicity. If \(\ell>\delta\), GF never reaches the tolerance and the exact GF prefix yields the additional lower bound

\[
A_\varepsilon\le\tau_\varepsilon(\delta)
\le A_\varepsilon+\frac1\lambda\log\frac{L_{\rm init}}\delta.
\tag{4}
\]

Thus, on a GF trajectory with a positive loss floor above the target, fitting time has exactly the delay's growth up to a bounded additive term.

Equations (3)–(4) concern a fixed fitting tolerance. If instead the target is \(\delta_\varepsilon=\varepsilon^q\), \(q>0\), the supplied exponential estimate only certifies

\[
\tau_\varepsilon(\varepsilon^q)
\le h(\varepsilon)+\frac q\lambda\log\frac1\varepsilon+O(1).
\tag{5}
\]

The theorem alone supplies no faster joint-accuracy guarantee; (5) is an upper bound and is not a universal lower bound on the actual optimizer.

## Quantitative calibration without relabeling

Measure deviation in a fixed state norm by

\[
D(S_\varepsilon,S_0)
=\int_0^\infty\lambda e^{-\lambda t}
\min\{1,\|S_\varepsilon(t)-S_0(t)\|\}\,dt.
\]

This is a discounted integral metric on continuous paths. It need not metrize compact-uniform convergence for arbitrary paths; narrow spikes can have small integral. The present construction has the stronger compact-uniform conclusion directly from its exact prefix.

Define the discounted indicator of activation by

\[
Q_\varepsilon
=\int_0^\infty\lambda e^{-\lambda t}\mathbf1_{\{t\ge A_\varepsilon\}}\,dt
=e^{-\lambda A_\varepsilon}
=e^{-\lambda h(\varepsilon)-V}.
\tag{6}
\]

This counts the time during which correction is enabled; it need not measure a nonzero correction magnitude. Since the paths agree before activation and the metric's integrand is bounded by one,

\[
D(S_\varepsilon,S_0)\le Q_\varepsilon\le e^{-\lambda h(\varepsilon)},
\qquad
\mathbb E D(S_\varepsilon,S_0)
\le\mathbb E Q_\varepsilon
=(1-e^{-1})e^{-\lambda h(\varepsilon)}.
\tag{7}
\]

For each realization, the exact invariant calibration is

\[
A_\varepsilon=\frac1\lambda\log\frac1{Q_\varepsilon}.
\tag{8}
\]

Therefore an almost-sure guarantee \(Q_\varepsilon\le\rho\), \(0<\rho<1\), holds precisely when
\(h(\varepsilon)\ge\lambda^{-1}\log(1/\rho)\). Necessity here concerns \(Q\): if \(e^{-\lambda h}>\rho\), a positive interval of \(V\)'s near zero violates the bound. If only \(\mathbb E Q_\varepsilon\le\rho\) is required, the exact condition is
\(h(\varepsilon)\ge\max\{0,\lambda^{-1}\log((1-e^{-1})/\rho)\}\).

At a fixed intervention tolerance, choosing a slower function of the label \(\varepsilon\) does not improve (8). In the positive-floor case of (4), it gives the matching fitting-time statement

\[
\frac1\lambda\log\frac1{Q_\varepsilon}
\le\tau_\varepsilon(\delta)
\le\frac1\lambda\log\frac1{Q_\varepsilon}
+\frac1\lambda\log\frac{L_{\rm init}}\delta.
\tag{9}
\]

For the state metric \(D\), using (7) as a certificate likewise requires a logarithmic delay to certify a specified tolerance \(\rho\). This is a statement about the certificate. It is **not** a necessary condition for actual \(D\le\rho\): (7) provides no lower bound on \(D\). For example, the supplied assumptions allow a trajectory on which the corrected flow equals GF, in which case \(D=0\) despite \(Q>0\). More generally the magnitude and duration of post-activation separation have not been controlled. An impossibility claim at fixed actual state error would require additional dynamical information, such as a proved separation bound on a specified interval after activation.

The prefactor also has a transparent calibration. Equations (2) and (6) give

\[
\frac{L_0(A_\varepsilon)}{Q_\varepsilon}
\le K_\varepsilon\le\frac{L_{\rm init}}{Q_\varepsilon}.
\tag{10}
\]

If \(\ell>0\), replace the lower numerator by \(\ell\): the best all-time exponential prefactor grows like \(1/Q_\varepsilon\), up to fixed factors. This is an unavoidable recorded quantity for these plateau trajectories, even though the correction strength and exponential rate are fixed. A common prefactor \(K\) independent of \(\varepsilon\) is possible only if GF itself satisfies \(L_0(t)\le Ke^{-\lambda t}\): every fixed \(t\) eventually lies in an exact prefix. Conversely, that GF envelope bounds (2), so this condition is sufficient for the delayed family's prefactors.

## Log-log schedules and the qualitative loophole

For sufficiently small \(\varepsilon\), choose

\[
h(\varepsilon)=\frac1\lambda\log\log\frac1\varepsilon.
\]

Then the fixed-tolerance time bound in (3) is
\(\lambda^{-1}\log\log(1/\varepsilon)+O(1)\), but the available state-error certificate is only

\[
D\le\frac1{\log(1/\varepsilon)},
\qquad
K_\varepsilon\le eL_{\rm init}\log\frac1\varepsilon.
\]

An iterated-log delay gives correspondingly slower growth in the label, an even more slowly vanishing certificate, and its corresponding prefactor. For instance \(\lambda h=\log\log\log(1/\varepsilon)\) gives \(D\le1/\log\log(1/\varepsilon)\).

These are honest statements about the weak qualitative requirement, but changing \(h\) alone produces the same family of physical delayed trajectories with a different parameter label. Put \(\eta=e^{-\lambda h(\varepsilon)}\). In terms of the certified accuracy \(\eta\), every such schedule has

\[
h=\lambda^{-1}\log(1/\eta),\qquad
\tau_\varepsilon(\delta)\le\lambda^{-1}\log(1/\eta)+O(1).
\]

Accordingly the log-log formula cannot be presented as a substantive answer to a requirement explicitly forbidding reparameterization. It gives a valid qualitative family and exposes why an invariant approximation tolerance must be specified. It does not rule out a distinct construction that improves actual state error after activation.

Qualitative convergence also singles out no slowest diverging delay. Given any admissible \(h\to\infty\),

\[
\widetilde h=\lambda^{-1}\sqrt{\lambda h}
\]

still tends to infinity and obeys \(\widetilde h/h=(\lambda h)^{-1/2}\to0\). Both satisfy the compact-time requirement. Thus there is no optimal slowest divergence under that requirement alone. On a GF plateau, (4) transfers this fact to fixed-tolerance fitting times for this delayed family.

## Noise and computational limitations

The zero-noise construction already proves the stated existence claims. A bound \(\|\eta_\varepsilon(t)\|\le\varepsilon\sqrt{L_\varepsilon(t)}\) does not by itself determine the effect of noise injected into optimizer dynamics: the noise's location, sign in the energy identity, and relevant operator bounds would be needed. No dynamical noise robustness is asserted here.

If instead this bound refers only to an additive observation perturbation in the same norm as the metric, it has a direct elementary interpretation. Since \(L_\varepsilon(t)\le L_{\rm init}\), the perturbed reported state \(\widehat S_\varepsilon=S_\varepsilon+\eta_\varepsilon\) satisfies

\[
\sup_{t\le T}\|\widehat S_\varepsilon(t)-S_0(t)\|
\le\varepsilon\sqrt{L_{\rm init}}\quad(T\le h),
\qquad
D(\widehat S_\varepsilon,S_0)
\le\varepsilon\sqrt{L_{\rm init}}+Q_\varepsilon.
\]

The latter follows from the triangle inequality and
\(\min(1,a+b)\le\min(1,a)+b\). For an additive residual observation with the normalization \(L=\|r\|^2\), the reverse triangle inequality and triangle inequality give
\((1-\varepsilon)_+^2L\le\|r+\eta\|^2\le(1+\varepsilon)^2L\).
These statements are conditional on the described observation interpretation, and should not be transferred to dynamical noise.

Finally, almost-sure Gram invertibility is qualitative. It supplies neither a uniform smallest-eigenvalue bound, a finite expected inverse-Gram norm, a uniform endpoint norm, nor a numerical step-count estimate. Each claim of practical complexity must state and prove its own quantitative conditioning and discretization hypotheses. Randomizing activation avoids a countable set of exact singularities; it does not bound the cost of approaching those singularities.

The conclusions established from the supplied theorem are therefore the arbitrary-delay family, its exact prefix and fixed tail rate, the prefactor and fitting-time bounds, and the intervention calibration. A substantive sublogarithmic improvement at a fixed actual GF state tolerance remains unproved; neither its success nor a general impossibility follows from the supplied input.
