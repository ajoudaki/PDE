# Response clocks: exact bounds and normalization limits

Status: scoped mathematical check for this study, 2026-09-25. This report uses only the supervisor's supplied setup and derives its claims directly. It is not an independent promotion review. No scientific sources or other study artifacts were retrieved.

The sample count is denoted by \(M\). To distinguish it from that count, the fixed positive block mobility is denoted by \(\mathsf A=\mathsf A^\top>0\). For a fixed finite bias-free tanh network, let
\[
\dot\theta=V(\theta)=-\mathsf A\nabla\mathcal L(\theta),
\qquad
\mathcal L=\frac1M\|r\|_2^2,
\qquad r=f(\theta)-y.
\]
Let \(\Psi:\mathbb R^P\to\mathbb R^N\) be the smooth map stacking the requested current forward and backward responses, including every requested sample, neuron, and layer. Write
\[
v(\theta)=D\Psi(\theta)V(\theta).
\]
The vector \(v\) is a current-state directional derivative. Its evaluation needs the current parameters, task, and gradient, with no future trajectory information.

## 1. Exact causal response clock

Fix a norm \(\|\cdot\|_*\) on the response space and set
\[
q(\theta)=\|v(\theta)\|_*,
\qquad
\tau(t)=\int_0^t q(\theta(s))\,ds.
\]
For every finite \(T\), there is a unique path \(Y:[0,\tau(T)]\to\mathbb R^N\) with
\[
\Psi(\theta(t))=Y(\tau(t)),
\qquad
\|Y(u_2)-Y(u_1)\|_*\le |u_2-u_1|.
\]
It is therefore Lipschitz and absolutely continuous. Wherever \(q(\theta(t))>0\),
\[
\frac{dY}{d\tau}
=\frac{D\Psi(\theta(t))V(\theta(t))}{q(\theta(t))},
\qquad
\left\|\frac{dY}{d\tau}\right\|_*=1.
\]
Unit speed holds almost everywhere on any nontrivial clock interval.

Proof. For \(t_1<t_2\),
\[
\|\Psi(\theta(t_2))-\Psi(\theta(t_1))\|_*
\le\int_{t_1}^{t_2}\|v(\theta(s))\|_*\,ds
=\tau(t_2)-\tau(t_1).
\]
Equal clock readings thus imply equal responses, making the factorization well defined even when the clock has flat intervals. Continuous \(\tau\) covers its interval, and the same inequality proves its Lipschitz property. Where \(q>0\), inverse differentiation proves the formula. The open set \(\{t:q(t)>0\}\) is a countable union of intervals; the lengths of their clock images sum to \(\int_0^Tq=\tau(T)\). The remaining clock values have measure zero, proving the almost-everywhere assertion.

The identical proof applies to any continuous current-state monitor \(\rho(\theta)\ge q(\theta)\), with \(\tau=\int\rho\), giving speed at most one. A positive guard \(\rho=\varepsilon+q\) yields a strictly increasing clock but forces an infinite all-time clock horizon. With the exact monitor, zero-speed intervals are collapsed. If \(q\equiv0\), the response is constant; division by its zero total length is unnecessary and undefined.

## 2. Minimal clock for simultaneous derivative caps

Given fixed caps \(b_i>0\), define
\[
q_{\rm cap}(\theta)=\max_{1\le i\le N}\frac{|v_i(\theta)|}{b_i}.
\]
The resulting factorization satisfies
\[
|Y_i(u_2)-Y_i(u_1)|\le b_i|u_2-u_1|,
\qquad |Y_i'|\le b_i\quad\text{a.e.}
\]
This monitor is pointwise minimal among absolutely continuous nondecreasing clocks admitting those Lipschitz caps. Indeed, any such factorization through a clock \(\sigma\) obeys
\[
|\Psi_i(\theta(t+h))-\Psi_i(\theta(t))|
\le b_i|\sigma(t+h)-\sigma(t)|.
\]
At differentiability points, division by \(|h|\) and passage to the limit yield
\[
|v_i(\theta(t))|\le b_i\dot\sigma(t),
\qquad \dot\sigma(t)\ge q_{\rm cap}(\theta(t)).
\]

A scalar time change can make one aggregate norm constant. It cannot generally make every nonzero coordinate have the same prescribed speed: it preserves ratios \(v_i/v_j\), and simultaneous saturation would require all ratios \(|v_i|/b_i\) already to coincide.

For the RMS monitor
\[
q_{\rm RMS}=\left(\frac1N\sum_i v_i^2\right)^{1/2},
\]
the joint RMS speed is one, but individual bounds are only \(|Y_i'|\le\sqrt N\). More generally, \(q^2=\sum_i w_i v_i^2\), with \(w_i>0\), gives \(|Y_i'|\le w_i^{-1/2}\). Blockwise RMS choices must retain their corresponding block-size factors. The maximum monitor gives a bound of one for each coordinate independent of the coordinate count, but its clock length can depend on width. This is not a width-independent physical-time bound or a bound on normalized-interval complexity.

## 3. Square-root loss removes residual magnitude, not response speed variation

Let \(J_f=Df\) and
\[
u(t)=\int_0^t\sqrt{\mathcal L(\theta(s))}\,ds.
\]
Where \(\mathcal L>0\),
\[
\frac{d\Psi}{du}
=-\frac2{\sqrt M}D\Psi\,\mathsf A J_f^\top\frac r{\|r\|_2},
\]
and therefore
\[
\left\|\frac{d\Psi}{du}\right\|_*
\le\frac2{\sqrt M}\|D\Psi\,\mathsf A J_f^\top\|_{2\to *}.
\]
Residual magnitude cancels, while network Jacobians and residual direction remain. A global derivative bound under this clock needs an appropriate global bound on the displayed operator along the orbit. Unit joint speed and equal coordinate speeds do not follow from this identity.

The failure of a task-only bound is already visible in a bias-free two-hidden scalar network with unit normalizing factors and mobilities,
\[
f=a\tanh(w_2\tanh w_1),\qquad h_1=\tanh w_1.
\]
For one sample with input one,
\[
\frac{dh_1}{du}
=-2\operatorname{sign}(r)\,a w_2
\operatorname{sech}^2(w_2\tanh w_1)
\operatorname{sech}^4w_1.
\]
At \(w_1=w_2=1\), its magnitude grows without bound as the initial readout \(a\to\infty\), although a fixed target such as one is realizable. This disproves a uniform bound based only on the task across unrestricted initializations. It does not disprove a trajectory-dependent global bound for every fixed initialization, and it makes no almost-sure assertion about a specified Gaussian initialization law.

Task compatibility likewise does not imply finite square-root-loss time. Consider the bias-free two-hidden network
\[
h_1(x)=\tanh(W_1x/\sqrt d),\qquad
h_2(x)=\tanh(W_2h_1(x)),\qquad
f(x)=a^\top h_2(x)/n,
\]
with hidden width \(n\ge2\) and \(d\ge2\). Take the nonparallel data
\[
x_1=\sqrt d\,e_1,\quad x_2=\sqrt d\,e_2,
\qquad y_1=1,\quad y_2=2.
\]
This task is realizable. For any \(z,b>0\), choose the first two diagonal entries of \(W_1\) to be \(z\) and those of \(W_2\) to be \(b/\tanh z\), with all other entries zero. Then \(h_2(x_i)=\tanh b\,e_i\). Set \(a_i=n y_i/\tanh b\) for \(i=1,2\), with remaining entries zero.

Nevertheless, the all-zero state \(W_1=W_2=a=0\) is stationary: the readout derivatives vanish because \(h_2=0\), and the earlier-layer derivatives vanish because the readout is zero. Its loss is \(5/2\), so \(u(t)=\sqrt{5/2}\,t\) while all responses are constant. This is a measure-zero initialization under a nondegenerate Gaussian law. It refutes an inference based on compatibility and nonparallel data alone; it does not refute any claim proved almost surely for Gaussian initialization. At zero loss the gradient and every response velocity vanish.

## 4. Parameter metric arclength and finite physical time

Define
\[
p(t)=\|\dot\theta(t)\|_{\mathsf A^{-1}}
=\|\mathsf A^{1/2}\nabla\mathcal L(\theta(t))\|_2.
\]
Direct differentiation gives
\[
\dot{\mathcal L}=-p^2,
\qquad p=\sqrt{-\dot{\mathcal L}}.
\]
Thus parameter metric arclength is \(\int\sqrt{-\dot{\mathcal L}}\,dt\), rather than \(\int\sqrt{\mathcal L}\,dt\). Cauchy--Schwarz yields
\[
\int_0^T p(t)\,dt
\le\sqrt{T\,[\mathcal L(0)-\mathcal L(T)]}
\le\sqrt{T\mathcal L(0)}.
\]
Furthermore,
\[
q(\theta)
\le\|D\Psi(\theta)\mathsf A^{1/2}\|_{2\to *}\,p(\theta).
\]
Parameter arclength therefore controls the responses when their Jacobian is bounded along the orbit. The right-hand side is itself a causal monitor that bounds the exact response monitor.

The same energy identity rules out finite-time parameter escape. On any bounded physical-time interval the parameters remain in a bounded \(\mathsf A^{-1}\)-metric ball. Were the maximal existence time finite, the smooth vector field would be bounded and locally Lipschitz on a compact ball containing the orbit, the trajectory would have a finite limit, and local existence at that limit would extend it. Thus this finite-dimensional smooth gradient flow exists for every finite physical time. Each response Jacobian and response speed is bounded on every finite-horizon orbit, giving finite monitored length there.

This proves global existence, not convergence or successful training. The energy identity bounds \(\int_0^\infty p^2\), which does not by itself bound \(\int_0^\infty p\) or total response length.

## 5. All-time compact intervals require finite total variation

Write
\[
S_\infty=\int_0^\infty q(\theta(t))\,dt.
\]
The response-clock theorem holds on \([0,S_\infty)\) whether \(S_\infty\) is finite or infinite. If \(0<S_\infty<\infty\), the response has a unique Lipschitz extension to the terminal endpoint. Normalizing by
\[
\xi=2\tau/S_\infty-1
\]
gives a path on \([-1,1]\) with
\[
\left\|\frac{dY}{d\xi}\right\|_*\le S_\infty/2
\quad\text{a.e.}
\]
On a finite horizon use \(S_T=\tau(T)\) instead.

Finite total response variation is also necessary for a representation of the entire ordered response path by an absolutely continuous path on a compact interval: absolute continuity on a compact interval implies finite variation, and a continuous monotone reparameterization preserves variation. Consequently an infinite-length path cannot be compressed to a finite interval while retaining global absolute continuity or bounded derivatives. Parameter length can be infinite while the chosen response length is finite, so these conditions must not be conflated.

The accumulating monitor is causal. Exact normalization by \(S_\infty\) requires the unknown total length or an independently justified bound; this normalization is not an online theorem supplied by the monitor. Finite-horizon normalization is available after that horizon. Multiplying a monitor by a constant does not cure this issue, as made explicit below.

For completeness, an explicit sufficient condition for finite parameter length is an eventual inequality
\[
p(t)\ge c[\mathcal L(t)-\mathcal L_\infty]^\alpha,
\qquad c>0,\quad 0\le\alpha<1.
\]
On times with positive loss gap, substitute \(-\dot{\mathcal L}=p^2\) to obtain
\[
\int_t^\infty p(s)\,ds
\le\frac{[\mathcal L(t)-\mathcal L_\infty]^{1-\alpha}}
{c(1-\alpha)}.
\]
If the gap reaches zero, monotonicity forces subsequent \(p=0\), so the same conclusion applies. A bounded response Jacobian on the eventual orbit then gives finite response length. This is a sufficient hypothesis with a direct proof; this report does not establish that the training problem satisfies it.

## 6. What arclength minimizes after normalization

Fix the ordered response curve over a horizon, possibly infinite if all the following integrals are finite, and write \(v(t)=\|\dot\Psi(t)\|_*\) in this paragraph. Let a nonnegative clock rate \(g\) have
\[
0<S=\int g(t)\,dt<\infty,
\qquad \tau(t)=\int_0^t g(s)\,ds,
\qquad x=\tau/S\in[0,1].
\]
Assume the clock represents the curve by an absolutely continuous factorization, with stationary intervals allowed to collapse. Ratios at \(v=g=0\) contribute zero; a nonzero speed with zero clock rate on a set of positive measure is inadmissible for the stated finite-energy factorization. The normalized speed and energy are
\[
\left\|\frac{d\Psi}{dx}\right\|_*=\frac{S v(t)}{g(t)},
\qquad
E_g=\int_0^1\left\|\frac{d\Psi}{dx}\right\|_*^2dx
=S\int\frac{v(t)^2}{g(t)}\,dt.
\]
For a Euclidean or weighted RMS norm this is the usual unweighted derivative contribution to the \(H^1\) energy. The inequality below also holds for any fixed norm.

Let \(A=\int v(t)\,dt\) be the curve length. Cauchy--Schwarz gives
\[
A^2
=\left(\int\frac v{\sqrt g}\sqrt g\,dt\right)^2
\le\left(\int\frac{v^2}{g}\,dt\right)\left(\int g\,dt\right)
=E_g.
\]
For a nonconstant curve, equality holds precisely when \(g=c v\) almost everywhere for some constant \(c>0\), including zero clock rate on stationary intervals. Thus arclength minimizes this normalized unweighted derivative energy and makes the normalized joint speed equal to \(A\) almost everywhere. If strictly positive clock rate is required on positive-length stationary intervals, the minimum need not be attained in that restricted class; the collapsed-interval arclength clock still attains it in the stated class.

Arclength also minimizes the worst normalized derivative. Indeed,
\[
\operatorname*{ess\,sup}_{x\in[0,1]}
\left\|\frac{d\Psi}{dx}\right\|_*
\ge\int_0^1\left\|\frac{d\Psi}{dx}\right\|_*dx
=A,
\]
and constant arclength speed attains the lower bound. If \(A=\infty\), no compact-interval factorization can have finite unweighted derivative energy or finite maximum speed.

For any \(c>0\), replacing \(g\) by \(cg\) gives
\[
\tau_c=c\tau,\qquad S_c=cS,\qquad \tau_c/S_c=\tau/S.
\]
The normalized curve, its derivative energy, and its maximum normalized speed remain unchanged. A constant rescaling can change derivative caps in the unnormalized clock but cannot improve the normalized Legendre representation.

This variational claim does not extend automatically to the weighted Legendre seminorm. For example, the scalar curve from zero to one has normalized arclength representation \(Y(x)=x\), for which
\[
\int_0^1x(1-x)|Y'(x)|^2dx=1/6.
\]
The same ordered curve has the smooth strictly increasing representation
\[
\widetilde Y(x)=2x-3x^2+2x^3,
\qquad \widetilde Y'(x)=2-6x+6x^2\ge1/2,
\]
and direct polynomial integration gives
\[
\int_0^1x(1-x)|\widetilde Y'(x)|^2dx=13/105<1/6.
\]
Thus even with a regular positive alternative clock, arclength need not minimize the Legendre-weighted derivative energy. Nor does the unweighted optimality calculation establish optimal endpoint error or optimal higher derivatives.

The exact monitor guarantees Lipschitz regularity. It need not preserve higher smoothness: zero-speed points can become corners after arclength reparameterization. Exponential Legendre convergence, a width-independent truncation bound, finite all-time length, and successful training all require additional arguments.

## 7. Scoped audit of the initial synthesis

At the supervisor's explicit request, this agent subsequently read only sections 1, 2, 3 and the claim-status paragraph of `RESPONSE_CLOCK_DESIGN.md`. The audited initial file had SHA-256

`e1a118ecd28d937f76e805a638a9ebed89601ebbc9742b0af665c1e82e358145`.

Outcome: the mathematical claims in sections 1--3 are supported, with two recommended precision edits. The optimization class should allow a nonnegative clock rate, positive on the moving part, because a rate declared strictly positive everywhere cannot attain the stated collapsed-interval minimizer when stationary intervals have positive length. The projection notation should specify that \((F_T)_P\) keeps modes \(0,\ldots,P-1\), with integer \(P\ge1\), to match the displayed tail starting at \(k=P\). Neither issue changes the theorem when these conventions are explicit. The supervisor plans to make these wording changes after the scoped reports; this hash records the version actually audited.

The factor \(1/\sqrt6\) in the Legendre estimate is correct. To verify it explicitly, let \(p_k\) be the shifted Legendre polynomials with
\[
\int_0^1p_kp_j\,dx=\frac{\mathbf1_{k=j}}{2k+1},
\qquad
-[x(1-x)p_k']'=k(k+1)p_k,
\]
and let \(c_k=(2k+1)\int_0^1F(x)p_k(x)\,dx\) in the fixed Hilbert response space. Integration by parts has no boundary term because \(x(1-x)p_k'\) vanishes at both endpoints. It gives
\[
\int_0^1x(1-x)F'p_k'\,dx
=\frac{k(k+1)}{2k+1}c_k.
\]
The derivatives \(p_k'\), \(k\ge1\), are orthogonal in the weighted scalar space, with squared norms \(k(k+1)/(2k+1)\). Bessel's inequality therefore yields
\[
\sum_{k\ge1}\frac{k(k+1)}{2k+1}\|c_k\|_*^2
\le\int_0^1x(1-x)\|F'\|_*^2dx.
\]
Parseval for the shifted Legendre basis and \(k(k+1)\ge P(P+1)\) for \(k\ge P\) give
\[
\|F-F_P\|_{L^2}^2
\le\frac{1}{P(P+1)}\int_0^1x(1-x)\|F'\|_*^2dx.
\]
For normalized arclength, \(\|F'\|_*=\ell_T\) almost everywhere and \(\int_0^1x(1-x)dx=1/6\). Thus
\[
\|F-F_P\|_{L^2}\le\frac{\ell_T}{\sqrt{6P(P+1)}}.
\]
All uses of integration by parts are valid for \(F\in H^1([0,1])\), including the Lipschitz arclength path.

The endpoint order claimed in the synthesis can also be checked independently, without retrieving the existing moment-route source. Define
\[
H_P(x)=\frac{p_{P-1}(x)+p_P(x)}2.
\]
The polynomial identities give \(H_P(0)=0\), \(H_P(1)=1\), and
\[
H_P'=\sum_{k=0}^{P-1}(2k+1)p_k.
\]
Integration by parts therefore proves the exact endpoint identity
\[
F(1)-F_P(1)=\int_0^1H_P(x)F'(x)\,dx.
\]
Orthogonality gives
\[
\|H_P\|_{L^2}^2
=\frac14\left(\frac1{2P-1}+\frac1{2P+1}\right)
=\frac{P}{4P^2-1}.
\]
Consequently the normalized arclength endpoint bound is
\[
\|F(1)-F_P(1)\|_*
\le\ell_T\sqrt{\frac{P}{4P^2-1}},
\]
which is the stated \(O(\ell_T/\sqrt P)\) order.

The global compact-clock variation necessity in section 3 is also correct. If an absolutely continuous compact-interval path represents every point of the original ordered response path through a continuous monotone clock, every finite original partition maps to an ordered compact-interval partition. Its sum of increments is bounded by the variation of the compact-interval path, which is at most the integral of its derivative norm. Infinite original total variation is therefore impossible. Conversely finite monitored length gives the Lipschitz terminal extension proved in section 5 of this report.

The claim-status paragraph correctly separates these finite-system results from width-uniform length, population control, closure guarantees, and comparative benchmark performance. Its claims concerning arbitrary-clock history equations, fourth-root-loss estimates, and Gram reconstruction lie outside this agent's authorized audit scope and were not checked here. This is a scoped internal check, not an independent promotion review.

Follow-up verification: the same authorized scope was reread after the supervisor's precision edits. The file SHA-256 is now

`3a54e6207cd208e00c2ccbd066484bd7c79ed1065aca60250ae8ceaf89affd8d`.

Both requested conventions are explicit in that version, and section 1 explicitly states positive definite mobility. The scoped conclusions above remain valid. This report's realizable stationary example has also been corrected to the exact supplied canonical scaling \(h_2=\tanh(W_2h_1)\), \(f=a^\top h_2/n\), with \((W_2)_{ii}=b/\tanh z\) and \(a_i=ny_i/\tanh b\). No additional scientific inputs were retrieved.
