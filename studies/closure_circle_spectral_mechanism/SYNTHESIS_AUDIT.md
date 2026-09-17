# Synthesis audit: closure order is not angular bandwidth

2026-09-14. Bounded same-study synthesis of the frozen `THEORY.md` and `NTK_THEORY.md`, after their separate derivations were completed. This is an internal consistency audit, not an independent blind review or a promotion. No new simulation, sibling empirical result, or other study was read. The small inequalities below sharpen the existing sparse-pair interpretation; they do not open a new research branch.

## Strongest defensible principle

**Closure order determines which initialized population interactions are retained. The angular spectrum of the learned function results from the initial kernel, the geometry of the observed labels, and subsequent changes in the kernel. No monotone relation between closure order and angular bandwidth follows.**

The exact architecture permits unbounded odd angular frequencies at each requested order, and forbids every even frequency at every state. N=2 adds only inactive even mark directions in the exact symmetric construction with matched ridge; N=3 and N=5 add odd mark directions. Those directions can modify low as well as high angular frequencies. The maintained N-dependent ridge and finite integration rules complicate direct order comparisons.

The non-bandlimited example in `THEORY.md` belongs to the representable state family. It was not shown reachable from prescribed initialization by the specified two-point gradient flow. It establishes that N is not an architectural Fourier cutoff. A claim about which frequencies training actually uses must come from the recorded trajectories, with numerical uncertainty and amplitude normalization reported.

## Consistency of the two kernel descriptions

Both derivations use normalized input u=x/sqrt(2), unhalved probability-weighted squared loss, and the small initial readout. Both conclude that only the readout tangent block survives initially. The full population initial kernel in `NTK_THEORY.md` is stationary; a finite-order closure's initial kernel need not be stationary. These are different reference kernels, with consistent definitions.

For equal-mass labels (-A,+A) at angles (mu-delta/2,mu+delta/2), put D_delta=k(0)-k(delta). The stationary frozen formula is

\[
f_t(\theta)=A\frac{1-e^{-D_\delta t}}{D_\delta}
\left[k(\theta-\mu-\delta/2)-k(\theta-\mu+\delta/2)\right].
\]

The training MSE is A^2 exp(-2D_delta t). Its complex Fourier coefficient is

\[
\widehat f_m(t)=-2iA\,e^{-im\mu}\widehat k_m
\sin(m\delta/2)\frac{1-e^{-D_\delta t}}{D_\delta}.
\]

These formulas agree with both reports after accounting for the reversed (+A,-A) labeling in the earlier example in `THEORY.md`. In particular, the real sine coefficient about mu has factor 4A hat k_m sin(m delta/2)/D_delta at the endpoint. The sign difference is a convention, not a discrepancy.

For this symmetric stationary frozen pair, every coefficient changes by the same time factor. Its normalized spectral power is time-independent. Changing delta changes the factor sin(m delta/2), so spacing can change normalized bandwidth even with no feature adaptation. Mirror oddness about mu holds for this stationary baseline. Only antipodal oddness is guaranteed for a fixed finite-order closure with coordinate-anchored initialization.

## Sparse observations couple Fourier modes even for a stationary kernel

For fixed stationary k and training atoms theta_a with masses p_a, the exact mode equation is

\[
\dot{\widehat f}_m=-2\widehat k_m
\sum_a p_a\bigl(f(\theta_a)-y_a\bigr)e^{-im\theta_a}.
\]

This follows by taking the Fourier integral of the finite sum in the prediction equation; there is no exchange of infinite sums. When f has an absolutely convergent Fourier series, as for the finite-state analytic circle functions, substitution gives

\[
\dot{\widehat f}_m=-2\widehat k_m\sum_\ell S_{\ell-m}\widehat f_\ell
+2\widehat k_m\sum_a p_a y_a e^{-im\theta_a},\qquad
S_j=\sum_a p_a e^{ij\theta_a}.
\]

For generic sparse atoms S_j is nonzero at many nonzero j. Consequently the training operator is not Fourier-diagonal. Uniform continuous-circle supervision would instead give S_j=0 for every nonzero integer j. Uniform finite grids still couple aliases. Stationarity of the kernel on the circle must therefore be distinguished from diagonal Fourier training dynamics under the actual data measure.

The nonlinear closure adds another change: its kernel K_t itself evolves and can be nonstationary. These effects should not be inferred from one another.

## The amplitude–frequency tradeoff behind close opposite labels

An exact interpolant using only the first harmonic is

\[
f(\theta)=A\frac{\sin(\theta-\mu)}{\sin(\delta/2)}.
\]

Its circle maximum is A/sin(delta/2), while its normalized RMS frequency is exactly one. Thus arbitrarily close opposite labels can be fit without increasing frequency, at the cost of arbitrarily large off-support amplitude.

A bounded amplitude or energy constraint changes this conclusion. Define the normalized circle norm by ||f||_2^2=(2pi)^{-1} integral |f|^2. Let f be continuously differentiable and antipodally odd, interpolate (-A,+A) at separation 0<delta<=pi, and put

\[
k_{\rm rms}^2=\frac{\sum_m m^2|\widehat f_m|^2}{\sum_m|\widehat f_m|^2}
=\frac{\|f'\|_2^2}{\|f\|_2^2}.
\]

The equality is Parseval applied to f and f'; it applies to the analytic finite-state predictions here. Integrating f' along the short arc and applying Cauchy–Schwarz gives 4A^2 <= delta integral_arc |f'|^2. Since f'(theta+pi)=-f'(theta), the translated arc contributes the same integral, and the two arcs are disjoint apart from endpoints. Hence integral_arc |f'|^2 <= pi ||f'||_2^2 and

\[
k_{\rm rms}\,\|f\|_2\ge \frac{2A}{\sqrt{\pi\delta}}.
\]

If ||f||_2<=B, or more restrictively sup|f|<=B, this gives k_rms >= 2A/(B sqrt(pi delta)). This is a frequency-versus-amplitude constraint, not a constraint involving N. It is deliberately weaker than sharp bandlimited derivative inequalities and requires no external approximation theorem.

For an actual odd trigonometric polynomial of maximum positive frequency K, with K odd, an elementary Fourier constraint is also available. Write its sine coefficients about mu as b_m. The interpolation difference is 2 sum_(odd m<=K) b_m sin(m delta/2)=2A, and Parseval gives sum b_m^2<=2||f||_2^2. Cauchy–Schwarz therefore gives

\[
A^2\le2\|f\|_2^2\sum_{\substack{1\le m\le K\\m\text{ odd}}}\sin^2(m\delta/2)
\le\frac{\|f\|_2^2\delta^2 K(K+1)(K+2)}{12}.
\]

The last step uses |sin x|<=|x| and sum_(odd m<=K) m^2=K(K+1)(K+2)/6. With ||f||_2<=B this implies K(K+1)(K+2)>=12A^2/(B^2 delta^2). Neither this finite-cutoff bound nor the RMS bound makes closure order a bandwidth parameter. Approximate interpolants replace 2A by their actual output difference in the proof.

## Attribution and wording for the eventual results

Let f_N be the nonlinear closure predictor, f_F,N its own initialized frozen-kernel predictor, and f_F,infinity the full limiting initial-kernel predictor. At the same time, inputs, and labels,

\[
f_N-f_{F,\infty}=(f_N-f_{F,N})+(f_{F,N}-f_{F,\infty}).
\]

The first difference isolates departure from that closure's frozen initial features; the second isolates the initial-kernel approximation. The two function differences can reinforce or cancel, so norms should not be treated as additive contributions. A discrepancy from the full NTK alone cannot identify feature adaptation.

Report common-time comparisons and matched-fit normalized shapes separately. Kernel drift and paired hidden movement substantiate a changed mechanism, but gain or speed can change while normalized circle shape barely changes. Post-training Fourier or tanh templates describe shape; they do not establish a mechanism or an optimization principle. Without labels away from the observed atoms, smoother curves or smaller overshoot are geometric properties rather than demonstrated improvements in generalization.

No contradiction was found between the frozen candidate reports. Their shared unresolved question is whether controlled trajectories display order-dependent changes in normalized circle geometry beyond their own initialized frozen kernels; this audit does not prejudge that empirical result.

Frozen input SHA-256:

```text
a7686b0155bd34eb01ac8431fd187c42ac235d3d1703b269cdc789f9f8c92414  THEORY.md
6ce8d478bf8373d5adde95b088f5185bf0e4078f192b7677ed1f2a2531f2234f  NTK_THEORY.md
```
