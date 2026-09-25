# Evolving response states: exact linear construction and nonlinear obligations

This is a scoped, theory-only route based exclusively on the supervisor's self-contained assignment. No book theorem, other study, numerical result, or outside scientific source was consulted. The investigation and rigorous-mathematics skills were applied. The proposed object is an autonomous, restartable state that stores the observable effect of past neuronal evolution. Its coefficients and initialization must come from the defining model and admissible initial data, never from the future target trajectory.

**Conclusion.** Finite response states are an exact mathematical alternative to retaining the entire history in a linear model. Small dimension is an additional, strong property: it requires compression of both the driven response and the initial hidden forcing. For nonlinear neural training, an exact history identity does not establish this property. A useful conditional route is to prove low observable memory complexity and stability of the coupled reduced dynamics. Neither requires a time-Taylor expansion; neither has been established here for dense neural training.

## 1. Exact elimination, including the initialization term

Let \(z(t)\in\mathbb R^n\) be resolved and \(y(t)\in\mathbb R^q\) hidden, with constant finite matrices
\[
\dot z=Az+By,\qquad \dot y=Cz+Dy,\qquad (z(0),y(0))=(z_0,y_0).
\]
Multiplying the second equation by \(e^{-Dt}\) and integrating gives
\[
y(t)=e^{Dt}y_0+\int_0^t e^{D(t-s)}Cz(s)\,ds.
\]
Consequently the exact resolved equation is
\[
\dot z(t)=Az(t)+g(t)+\int_0^t K(t-s)z(s)\,ds,
\quad g(t)=Be^{Dt}y_0,\quad K(t)=Be^{Dt}C. \tag{1}
\]
The kernel describes how earlier resolved motion returns through the hidden dynamics. The term \(g\) describes hidden information already present at initialization. Omitting it changes the system unless it vanishes or is represented elsewhere.

At an intermediate time \(t_0\), the same identity starts from \(y(t_0)\). Restarting from \(z(t_0)\) alone therefore usually loses relevant history. An auxiliary state is useful precisely because it carries this history forward without storing a trajectory.

## 2. Exactly when \(P\) scalar response coordinates suffice

Allow initial hidden states \(y_0=E\xi\), where \(E\in\mathbb R^{q\times d}\) is specified and \(\xi\in\mathbb R^d\) is admissible initial information. Consider
\[
\dot z=Az+Rm,\qquad \dot m=Tm+Sz,\qquad m(0)=J\xi,
\qquad m\in\mathbb R^P. \tag{2}
\]
Here \(P\) counts scalar coordinates, not blocks whose dimension is concealed. Eliminating \(m\) shows that (2) represents the hidden input-output map exactly, for every resolved input history and every \(\xi\), if and only if
\[
Re^{Tt}S=Be^{Dt}C,\qquad Re^{Tt}J=Be^{Dt}E
\quad\text{for all }t\ge0. \tag{3}
\]
This is a transferable representation of the hidden subsystem, a stronger contract than matching a single closed-system trajectory. Because finite matrix exponentials have convergent series, (3) is equivalent to
\[
RT^kS=BD^kC,\qquad RT^kJ=BD^kE\quad(k\ge0). \tag{4}
\]

There is an elementary exact dimension criterion. Define
\[
F=[C\ E],\qquad
V=\operatorname{span}\{D^k\operatorname{im}F:0\le k<q\},
\qquad
N=\bigcap_{0\le k<q}\ker(BD^k).
\]
By the characteristic polynomial identity for \(D\), powers of order at least \(q\) are combinations of the preceding powers. Thus \(V\) and \(N\) are invariant under \(D\). The minimum exact dimension is
\[
P_{\min}=\dim V-\dim(V\cap N). \tag{5}
\]
For sufficiency, take the response space to be the quotient \(V/(V\cap N)\). Define
\[
T[v]=[Dv],\quad R[v]=Bv,\quad Su=[Cu],\quad J\xi=[E\xi].
\]
Invariance makes these maps well defined; the unobservable directions in \(V\cap N\) contribute nothing to \(Be^{Dt}v\). These definitions give (3).

For minimality, form the finite block matrix
\[
\mathcal H=(BD^{i+j}F)_{0\le i,j<q}
=\begin{bmatrix}B\\BD\\\vdots\\BD^{q-1}\end{bmatrix}
\begin{bmatrix}F&DF&\cdots&D^{q-1}F\end{bmatrix}.
\]
The right factor has image \(V\), and the left factor restricted to \(V\) has kernel \(V\cap N\); hence \(\operatorname{rank}\mathcal H=P_{\min}\). Any realization (2) factors the same matrix through \(\mathbb R^P\), using (4), so its rank is at most \(P\). This proves (5) without assuming a realization theorem.

Two consequences matter for neuronal compression:

* If \(y_0=0\), use \(F=C\). Only hidden directions reachable from resolved forcing and visible through \(B\) matter.
* If all hidden initial states are allowed, use \(E=I_q\). Then \(V=\mathbb R^q\), so \(P_{\min}=q-\dim N\). The driven kernel may have a small realization while initial hidden information requires many more coordinates.

Even scalar \(z\) need not give small \(P\). Let \(D\) have \(q\) distinct real eigenvalues, and choose scalar-output \(B\) and scalar-input \(C\) with nonzero products in every eigendirection. Then \(K(t)\) contains \(q\) distinct exponentials with nonzero coefficients. The Vandermonde factors of \(\mathcal H\) are invertible, giving \(P_{\min}=q\) already with zero hidden initialization. Small observable dimension and low rank of a single coupling matrix do not establish low memory dimension.

## 3. Rational transfer means rational in a transform variable

For complex \(p\) with sufficiently large real part,
\[
\widehat K(p)=\int_0^\infty e^{-pt}K(t)\,dt
=B(pI-D)^{-1}C.
\]
The integral identity follows by integrating the derivative of \(e^{-(pI-D)t}\); exponential decay at infinity holds in this half-plane. Equation (3) is equivalent to equality of the two rational matrix functions
\[
B(pI-D)^{-1}C=R(pI-T)^{-1}S,
\qquad B(pI-D)^{-1}E=R(pI-T)^{-1}J. \tag{6}
\]
Necessity follows by transforming (3); conversely, expansion for large \(|p|\) gives (4), hence (3). The least realization dimension of the combined strictly proper rational matrix \(B(pI-D)^{-1}[C\ E]\) is exactly (5), often called its McMillan degree. The rank argument above specifies this notion rather than relying on the name.

The variable \(p\) is the Laplace frequency, **not physical time**. A rational function of \(p\) corresponds to sums of exponential-polynomial kernels in time. For instance a scalar pole \(-a\) produces a response coordinate
\[
\dot m=-am+sz,
\]
and repeated poles can require chains producing \(t^j e^{-at}\). This is an evolution law for stored response, not a rational fit to \(z(t)\), and not a truncated time-Taylor series. A matrix-valued simple pole may require more than one scalar coordinate according to its residue rank.

Finite-dimensionality alone supplies a rational transfer function; it does not supply a low-degree one. A continuous distribution of hidden relaxation rates generally yields a nonrational transform and cannot be represented exactly by a finite constant-coefficient linear response state. Approximation is a separate question.

## 4. A constructive approximation that does not use Taylor analyticity

The following is a conditional example, not an assertion about the neuronal generator. Suppose the observable kernel and hidden initialization admit the known representations
\[
K(t)=\int_{[0,\infty)}e^{-at}\,d\nu_K(a),\qquad
g(t)=\int_{[0,\infty)}e^{-at}\,d\nu_g(a), \tag{7}
\]
where \(\nu_K\) is a finite matrix-valued measure and \(\nu_g\) a finite vector-valued measure. Their total variations use compatible operator/vector norms. Crucially these measures must be constructed from the defining dynamics and admissible initialization, not estimated from the future solution.

Choose a cutoff \(L\), partition \([0,L]\) into \(N_b\) intervals of diameter at most \(\delta\), and choose a representative \(a_i\) in each interval. Set
\[
W_i=\nu_K(I_i),\qquad v_i=\nu_g(I_i),\qquad
\dot m_i=-a_i m_i+W_i z,\quad m_i(0)=v_i,
\qquad \dot z=Az+\sum_i m_i. \tag{8}
\]
Each \(m_i\in\mathbb R^n\); the total auxiliary dimension is \(P=nN_b\). Eliminating these states gives the quadrature kernels and initialization terms simultaneously.

For \(0\le t\le H\), the mean value theorem gives
\(|e^{-at}-e^{-a_it}|\le H|a-a_i|\). Thus, for either measure \(\nu\),
\[
\sup_{0\le t\le H}\left\|
\int e^{-at}\,d\nu(a)-\sum_i e^{-a_it}\nu(I_i)
\right\|
\le |\nu|((L,\infty))+H\delta |\nu|([0,L]). \tag{9}
\]
Finite variation makes the tail vanish as \(L\to\infty\); then \(\delta\to0\) gives uniform convergence, including at initialization. A bound independent of network width would require a width-independent total-variation bound and a uniform tail function for both measures. This is an explicit additional hypothesis, not a consequence of finite total variation for each width separately.

No derivative at \(t=0\) appears in (9). For a nonnegative scalar measure with all moments finite, differentiation under the integral is justified by the corresponding moment bound, and
\[
K^{(k)}(0+)=(-1)^k\int a^k\,d\nu(a).
\]
If \(\limsup_k((\int a^k\,d\nu)/k!)^{1/k}=\infty\), these derivatives have a Taylor series of radius zero. Inequality (9) still applies. Therefore zero Taylor radius does not obstruct this conditional approximation in values on a compact interval. It does obstruct equality with a fixed finite linear model having an entire-time output. Convergence of values here makes no claim about convergence of all derivatives.

If the rates also obey \(a\ge a_*>0\), then
\[
\int_0^\infty|e^{-at}-e^{-bt}|\,dt=|a^{-1}-b^{-1}|
\le |a-b|/a_*^2.
\]
This supplies an \(L^1\) kernel approximation from the same partition; the discarded tail contributes at most \(\int_{(L,\infty)}a^{-1}\,d|\nu|(a)\). Such estimates are relevant to persistent-time stability. Rates accumulating at zero can destroy integrability even when compact-time approximation remains valid.

The missing scientific input is whether the actual neuronal response has a representation resembling (7), or some other uniformly compressible observable response operator. Diagonalizing a full microscopic matrix after solving the target evolution would not solve this problem. Even an exact rank reduction may reduce storage while leaving ambient-size coefficient computation; admissible coefficient construction needs its own argument.

## 5. Kernel accuracy must survive feedback

Let \(z\) solve (1) and \(z_P\) solve its approximation using \(K_P,g_P\), with identical \(z_0\). Write \(e=z-z_P\) and
\[
\dot e=Ae+K_P*e+r,
\qquad r=(g-g_P)+(K-K_P)*z. \tag{10}
\]
For a fixed horizon \(H\), assume \(\sup_{t\le H}\|z(t)\|\le M_H\). Integrating (10), exchanging the order of the absolutely integrable convolution integrals, and using the integral Gronwall inequality yields
\[
\sup_{t\le H}\|e(t)\|
\le e^{(\|A\|+\|K_P\|_{L^1(0,H)})H}
\left(\|g-g_P\|_{L^1(0,H)}
+M_HH\|K-K_P\|_{L^1(0,H)}\right). \tag{11}
\]
Indeed the integrated feedback is bounded by
\((\|A\|+\|K_P\|_1)\int_0^t\|e(s)\|ds\), while the integrated source is bounded by the parenthesis. Iteration of this scalar inequality gives the displayed exponential. Consequently uniform kernel and initial-forcing approximations on compact intervals, with bounded coefficients and target state, imply compact-interval trajectory approximation. This is the bridge from (9) to dynamics.

For an all-time bound, suppose instead the approximate resolved response to additive forcing has a matrix resolvent \(\mathcal R_P\) satisfying
\[
\mathcal R_P'=A\mathcal R_P+K_P*\mathcal R_P,
\quad\mathcal R_P(0)=I,
\quad\|\mathcal R_P(t)\|\le C_*e^{-\gamma t},
\]
with \(C_*,\gamma>0\) uniform in the approximation family. Substitution and interchange of convergent convolutions verifies
\(e(t)=\int_0^t\mathcal R_P(t-s)r(s)ds\). If \(\sup_{t\ge0}\|z(t)\|\le M\), then
\[
\sup_{t\ge0}\|e(t)\|
\le\frac{C_*}{\gamma}
\left(\|g-g_P\|_{L^\infty(0,\infty)}
+M\|K-K_P\|_{L^1(0,\infty)}\right). \tag{12}
\]
Small source error and stable propagation are separate requirements. Stable eigenvalues of the hidden matrix \(T\) alone do not establish either a stable coupled system or a moderate \(C_*\); feedback and nonnormal transient amplification matter.

## 6. Plateaus are compatible with response states

For a known constant resolved drive \(b\), the affine version of (2) is
\[
\dot z=b+Az+Rm,\qquad \dot m=Tm+Sz.
\]
If \(T\) is invertible, an equilibrium satisfies
\[
m_*=-T^{-1}Sz_*,\qquad
0=b+(A-RT^{-1}S)z_* . \tag{13}
\]
If the full block matrix \(\begin{psmallmatrix}A&R\\S&T\end{psmallmatrix}\) has all eigenvalues with negative real part, it is invertible and its matrix exponential decays; subtracting the unique equilibrium proves exponential convergence. Any continuous readout then plateaus. The homogeneous system can converge to zero, or can retain a nonzero constant component under suitable neutral modes, but an arbitrary nonzero equilibrium should not be silently assumed in the strictly stable homogeneous case.

When the memory is integrable, \(-RT^{-1}S=\widehat K_P(0)=\int_0^\infty K_P(t)dt\). Thus plateau location is sensitive to the zero-frequency memory response. Good agreement over a short initial interval need not control it. A credible neuronal closure must preserve the relevant equilibrium relations and stability or dissipation; the mere appearance of a numerical plateau is not validation.

## 7. What changes for nonlinear, nonstationary neural histories

For a general full state \(X\) with \(\dot X=\mathcal F(X)\), an exact finite response state \(\Psi(X)=(z(X),m(X))\) must satisfy
\[
D\Psi(X)\mathcal F(X)=\overline{\mathcal F}(\Psi(X)) \tag{14}
\]
on the admissible reachable set, with the desired observable also determined by \(\Psi(X)\). For differentiable \(\Psi\) and a locally Lipschitz reduced field, the chain rule and uniqueness show that (14) gives autonomous, restartable dynamics. Necessarily, two reachable full states with the same \(\Psi\) must give the same projected instantaneous velocity. Finding two such states with different projected velocities falsifies that exact closure. This criterion excludes naming a few statistics without closing their evolution.

Eliminating nonlinear hidden variables generally gives a functional of the whole resolved history and initial hidden state, not a stationary convolution. Even a linear time-dependent hidden equation gives
\[
K(t,s)=B(t)U(t,s)C(s),\qquad
g(t)=B(t)U(t,0)y_0,
\]
where \(\partial_tU(t,s)=D(t)U(t,s)\) and \(U(s,s)=I\). A time-dependent finite response realization must factor this two-time kernel as
\(R(t)\Phi_T(t,s)S(s)\), with compatible initial forcing. A single rational function of a Laplace variable no longer characterizes this problem.

The decisive obstacles for neuronal history are:

1. **State dependence.** Response operators change as forward and backward states evolve. Reading their coefficients from the true trajectory would be oracle playback. Coefficients must be functions of retained states and permitted fixed model information.
2. **New information generation.** Differentiating retained statistics can generate further mixed responses and correlations. Smallness of their coefficients individually does not bound their collective feedback.
3. **Initialization.** Even a compressible driven response can have a high-dimensional observable initial forcing. A law-based limit must also explain what initialization fluctuations can be discarded.
4. **Moving modes.** A state-dependent response basis acquires derivative terms from motion of that basis. Dropping those terms is an additional approximation requiring an estimate.
5. **Spectral and nonnormal tails.** Many observable timescales, transient amplification, and slow modes near zero can make required dimension grow with horizon or accuracy.
6. **Nonlinear identifiability.** Low rank of a linearized response at one state does not imply that one finite state works on the whole reachable nonlinear set.
7. **Nonanalytic initialization.** A fixed finite linear realization is analytic in time. A finite nonlinear realization with analytic field and analytic readout is locally analytic as well. An exactly nonanalytic population observable would therefore require a nonanalytic reduced field/readout, a limiting family without uniform analytic control, or an infinite state. Compact-time value approximation by finite analytic models is still possible, as (9) illustrates.

Response coordinates should consequently be interpreted as evolving sufficient statistics of the observable history, analogous in role to position and velocity, rather than as retained time derivatives. Their number is controlled by the dimension of information affecting future observables, not by the order to which an initial Taylor calculation can be carried out.

## 8. Claim status and next proof obligation

| Claim | Status and scope |
|---|---|
| Exact history equation (1), including initialization | Proved for the constant-coefficient finite linear model. |
| Exact minimum response dimension (5) | Proved for its entire hidden input-output map and specified initial subspace. |
| Finite response states imply rational Laplace transfer | Proved in (6); this says nothing about rational time curves. |
| Compact-time approximation without Taylor convergence | Proved under the finite-measure representation and uniform tail assumptions in (7)–(11). |
| Stable all-time approximation and plateaus | Conditional on the explicit source, equilibrium, and coupled stability assumptions in (12)–(13). |
| Width-independent low-dimensional neuronal closure | Open; no dense neural model has been shown to satisfy these assumptions here. |

The strongest surviving obstruction is that the observable response complexity, including initial forcing, grows with the ambient neural system or with the requested horizon. The strongest plausible favorable mechanism is a uniformly small tail of the observable hidden response together with stable feedback. Neither a local derivative calculation nor small output dimension distinguishes these alternatives.

The highest-leverage next theoretical obligation is to specify one model-derived response state and bound its omitted contribution to the exact resolved equations over a stated reachable class. Such a result must specify the observable norm, horizon, initialization law, dimension bound, coefficient construction, and feedback stability. Only then can one formulate a non-vacuous assertion that \(P=P(\varepsilon,H,\text{fixed structural data})\) remains independent of neural width. A universal low-\(P\) assertion over arbitrary hidden dynamics is already contradicted by the distinct-exponential family above; this does not refute compression for a properly restricted neuronal class.
