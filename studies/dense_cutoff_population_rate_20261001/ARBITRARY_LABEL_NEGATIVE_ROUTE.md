# Arbitrary fixed labels: scalar obstruction to a negative example

Status: frozen independent theoretical route, 2026-10-03. No canonical slower-than-root-width counterexample is established here. The new proved statement is a deterministic extension of the one-sample obstruction to **unbounded activation values**, together with its exact extension to any invariant scalar direction in the training predictions. It excludes trapping, loss of scalar transversality, and finite-control blow-up before fitting in those directions. It does not exclude transverse multi-sample instability or prove a population width rate.

## Scope and sources

The requested negative witness would fix depth, finite compatible sphere data, labels of arbitrary fixed magnitude, layer activations in $C^3$ with globally bounded first three derivatives, a fixed query $x$, and canonical Gaussian initialization with zero readout. It would establish, for some $\alpha>0$, a nonvanishing probability of

\[
\sup_{t\ge0}|f_n(t,x)-f_\infty(t,x)|\gtrsim n^{-1/2+\alpha},
\]

where $f_\infty$ is the canonical dense population predictor. An unrelated scalar gradient system, labels depending on width, or an exact architectural training nullspace is not an admissible witness. The limiting initial feature Gram retains a positive gap on the compatible training quotient.

Scientific inputs read were the setting and population paragraphs in `paper/main.tex`, the all-time theorem statement and explanation in `paper/results.tex`, initialization and the first fitting estimates in `paper/proof_alltime.tex`, `docs/index.qmd`, `docs/notation.qmd`, and the complete same-study `LARGE_LABEL_ASSESSMENT.md` and `LARGE_LABEL_ASSESSMENT_CHECK.md`. The required canonical-notation, rigorous-math, and conjecture-investigation instructions were applied. No other study, other new route, external theorem, or experiment was used. Initial HEAD was `4dfa5c1ef2c5b920eda2bbc84316b189b97da92e`; only this file is owned by this route.

## Canonical model and the scalar identity

Write the first weight matrix as $A\in\mathbb R^{n\times d}$, hidden matrices as $W^{(\ell)}\in\mathbb R^{n\times n}$, and readout as $w\in\mathbb R^n$. The forward pass is

\[
z_a^{(1)}=Ax_a/\sqrt d,\qquad
z_a^{(\ell)}=W^{(\ell)}h_a^{(\ell-1)},\qquad
h_a^{(\ell)}=\phi_\ell(z_a^{(\ell)}),\qquad
f_a=w^\top h_a^{(L)}/n.
\]

The loss is $\mathcal L=m^{-1}\sum_a(f_a-y_a)^2$, and the parameter mobility $M$ has blocks $n,1,\ldots,1,n$. Thus the canonical dynamics are $\dot\theta=-M\nabla\mathcal L$. For a parameter displacement $v$, define its mobility norm by

\[
\|v\|_{M^{-1}}^2
=\frac{\|v_A\|_F^2+\|v_w\|_2^2}{n}
 +\sum_{\ell=2}^L\|v_{W^{(\ell)}}\|_F^2.
\tag{1}
\]

Fix real coefficients $c_a$ with $m^{-1}\sum_a c_a^2=1$. Define the actual scalar prediction and its last-layer feature by

\[
P(\theta)=\frac1m\sum_a c_af_a(\theta)
=\frac{w^\top H(\theta)}n,
\qquad
H(\theta)=\frac1m\sum_a c_a h_a^{(L)}(\theta).
\tag{2}
\]

Consider its controlled ascent curve

\[
\theta'=M\nabla P,\qquad w(0)=0,
\tag{3}
\]

where prime denotes the control coordinate $u$, not physical time. This is a curve in the actual dense parameter space, retaining all hidden weight updates. In particular $w'=H$. Suppose

\[
Q_0=\|H(0)\|_2^2/n>0.
\tag{4}
\]

On its interval of existence, the chain rule gives

\[
P'=\|\theta'\|_{M^{-1}}^2\ge\|H\|_2^2/n.
\tag{5}
\]

Put $R(u)=\|w(u)\|_2/\sqrt n$. Where $R>0$, differentiation and Cauchy–Schwarz give

\[
R'=P/R,
\qquad
P'\ge \|H\|_2^2/n\ge P^2/R^2=(R')^2,
\qquad
R''=\frac{P'-(R')^2}{R}\ge0.
\tag{6}
\]

At initialization $w(u)=uH(0)+o(u)$, hence $R'(0+)=\sqrt{Q_0}$. Convexity first holds on the positive interval starting at zero; it implies $R(u)\ge u\sqrt{Q_0}$, so this interval cannot end by $R$ returning to zero. Therefore throughout the positive existence interval,

\[
R'\ge\sqrt{Q_0},\qquad
\|H(u)\|_2^2/n\ge Q_0,\qquad
P'(u)\ge Q_0,\qquad
P(u)\ge Q_0u.
\tag{7}
\]

These are exact identities and inequalities for every smooth network linear in its readout. They do not use a bound on activation values or their derivatives.

## New continuation argument: bounded target replaces bounded activation

**Proposition.** Assume only that the finite network defines a $C^2$ prediction map, so (3) is locally well posed. For every finite $Y>0$, (3) reaches one unique point $u_*>0$ with $P(u_*)=Y$, before any possible controlled blow-up. Moreover,

\[
u_*\le Y/Q_0,
\qquad
\int_0^{u_*}\|\theta'(u)\|_{M^{-1}}\,du
\le \frac{Y}{\sqrt{Q_0}}.
\tag{8}
\]

**Proof.** Before its first hit of $Y$, (5) implies

\[
\int_0^u\|\theta'(v)\|_{M^{-1}}^2\,dv=P(u)<Y.
\tag{9}
\]

If a finite maximal control time $U$ were reached before the hit, then for $s<t<U$,

\[
\|\theta(t)-\theta(s)\|_{M^{-1}}
\le\sqrt{(t-s)[P(t)-P(s)]}
\le\sqrt{Y(t-s)}.
\tag{10}
\]

Thus the finite-dimensional parameter vector has a finite limit at $U$. Local existence at that limiting state continues the solution, contradicting maximality. A solution cannot instead avoid the target for all $u\le Y/Q_0$, by (7) and continuity. Strict positivity of $P'$ gives uniqueness of the hit. Finally Cauchy–Schwarz, (9), and $u_*\le Y/Q_0$ give

\[
\int_0^{u_*}\|\theta'\|_{M^{-1}}du
\le\sqrt{u_*P(u_*)}\le Y/\sqrt{Q_0}.
\]

This proves the proposition. In particular, no assertion that the ascent curve exists for every $u\ge0$ is needed or made. With unbounded activation values that stronger statement can fail.

## One datum at every fixed depth and every fixed label

For $m=1$, $c_1=1$, let the label first be $y=Y>0$. Define physical time by

\[
\dot u=2[Y-P(u)],\qquad u(0)=0.
\tag{11}
\]

The scalar solution stays below $u_*$, increases to $u_*$, and (3) composed with (11) is exactly the canonical dense gradient flow. The error $e(t)=Y-P(u(t))$ satisfies

\[
\dot e=-2P'(u(t))e\le-2Q_0e.
\]

Consequently

\[
|f_n(t,x_1)-y|\le |y|e^{-2Q_0t},\qquad
2\int_0^\infty|f_n(t,x_1)-y|dt=u_*\le |y|/Q_0,
\tag{12}
\]

and every parameter converges to the finite fitted state $\theta(u_*)$. Its total physical parameter path length is at most $|y|/\sqrt{Q_0}$ in (1). Negative labels follow by reversing the readout and label; this preserves all hidden trajectories and reverses predictions. Zero label is stationary. If $Q_0=0$, initialization is stationary and the conclusion fails for nonzero label; this case is excluded by the assumed gap.

This extends the prior deterministic one-sample result from bounded top activations to the entire activation class in the assignment, and in fact to arbitrary finite-network $C^2$ activations. It supplies no new stochastic width theorem.

For the stipulated bounded derivative class, (8) also places all visited states in a width-independent normalized tube whenever $Q_0\ge q>0$, the initial hidden operator norms are bounded, and $\|A(0)\|_F/\sqrt n$ is bounded. Indeed each normalized block displacement is at most $Y/\sqrt q$; hidden operator increments are bounded by their Frobenius norms. Linear activation growth then bounds all forward RMS fields recursively, and the bounded derivatives and bounded readout RMS bound all backward RMS fields recursively. These bounds imply a width-independent bound on $\|\theta'\|_{M^{-1}}$ along the stopped curve and on the control derivative of each fixed bounded query. For the latter, the chain rule gives

\[
\left|\frac{d}{du}f_n(u,x)\right|
\le \|M^{1/2}\nabla f_n(u,x)\|_2\,
    \|\theta'(u)\|_{M^{-1}},
\tag{13}
\]

and each gradient block is a normalized outer product of the already bounded forward and backward RMS fields. These statements bound the vector-field value and the observable derivative. They do not assert a width-independent Lipschitz constant for the full nonlinear vector field.

## Consequence for a symmetry-based saddle construction

Suppose the labels have the fixed form $y_a=Yc_a$ and a canonical finite or population trajectory has the exact invariant prediction relation

\[
f_a(t)=c_aP(t)\quad\text{for all }a,t.
\tag{14}
\]

Then $r_a=c_a(P-Y)$ and substitution in the canonical gradient equation gives precisely

\[
\dot\theta=2(Y-P)M\nabla P.
\tag{15}
\]

Thus the symmetry-reduced trajectory is the same scalar controlled ascent, not an arbitrary scalar least-squares dynamical system. If its initial projected feature energy $Q_0$ is positive, it cannot approach a stationary point with $P<Y$, nor can its fitted scalar equation have a zero derivative. At a fitted controlled state,

\[
P'(u_*)\ge Q_0>0.
\tag{16}
\]

In particular, the cubic critical-response example from the prior assessment cannot be embedded merely by declaring a symmetric scalar order parameter to be the training prediction. The linear readout and zero-readout initialization force (5)–(7), which that proposed embedding must satisfy.

The population use of this statement has an explicit boundary: the same algebra applies to a differentiable canonical Hilbert-space curve, replacing normalized finite pairings by the corresponding layer expectations and using actual adjoints. Its local existence and continuation must be supplied by the canonical population construction. The finite-dimensional continuation proof (10) alone does not establish local well-posedness of a nonlinear population vector field in an $L^2$ topology. This note does not invent that missing theorem.

The obstruction is also narrower than a theorem against all symmetry breaking. Relation (14) must hold; a multi-dimensional invariant prediction subspace need not satisfy it. Furthermore, (16) controls the scalar training direction, not the other eigenvalues of the entire trained feature Gram. A finite-width perturbation may leave (14), so transverse stability, an eventual singular transverse Gram, and passive-query response remain separate obligations.

## Search outcome and remaining decisive gap

This route considered nonzero-residual saddle trapping along an exact population symmetry direction, a scalar critical fitted endpoint, and controlled blow-up caused by linearly growing activation values. The first two mechanisms violate (7) when the symmetry leaves one training direction; the third cannot precede a finite scalar target by (9)–(10). This is an obstruction for these particular mechanisms, not a proof of the desired root-width rate.

No actual canonical negative witness was obtained. A surviving construction needs at least one ingredient not controlled above: genuinely multi-directional residual dynamics; degeneracy and amplification transverse to a fitted scalar path; or a rigorously identified finite-width mean bias slower than root width. In every case one must still construct the canonical population trajectory and connect the mechanism to a fixed-query prediction lower bound with nonvanishing probability. These bridges remain open here.

The positive proposition and its proof are a new author derivation, not independently checked or promoted material. No numerical experiment, CPU fallback, or Git mutation was performed.
