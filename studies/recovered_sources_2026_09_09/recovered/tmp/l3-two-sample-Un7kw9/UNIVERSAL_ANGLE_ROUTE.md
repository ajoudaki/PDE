# Universal activation: contrast cancellation and its remaining obstruction

Status: **partial exact results; universal MF/GF/GD theorem OPEN**.
This note does not certify an activation for the full contract. It proves
an angle-independent curvature estimate at the natural interpolation
scale, an exact normalized contrast formulation, and two obstructions to
turning these into response continuation. In particular, failure of the
perturbative argument is not a nonexistence result for universal
activations.

The fixed candidate throughout is
\[
 \phi(z)=1+z+e\arctan z,\qquad e>0,\quad L=1+e.
\]
Every calculation below permits the single choice \(e=1/10\), with no
angle, width, horizon, or mesh dependence. This is a candidate, not a
proved universal witness.

I read both requested skills at `/etc/codex/skills` in full, including
the research-contract, evidence-ledger, adversarial-audit, and
proof-search-orchestration references. I read CONTRACT.md,
NEAR_AFFINE_RESPONSE_ROUTE.md, and SYMMETRY_RADIAL_CLOCK.md in full.
I also inspected the first 565 lines of the optional one-sample
OFFSET_ARCTAN_GLOBAL_THEOREM.md. No experiment, agent, or finite-width
endpoint construction is used. Only this output file is changed.

## 1. A necessary divergent scale, valid for every Lipschitz activation

This first result does not depend on the arctangent choice. Let \(\phi\)
have Lipschitz constant \(L>0\). Use opposite labels, absorb their overall
sign into the readout, and put
\[
 \delta=\sqrt{(1-\rho)/2}\in(0,1],\qquad
 v=(x_1-x_2)/2,\qquad D_\ell=(z_1^{(\ell)}-z_2^{(\ell)})/2.
\]
Let \(A,B\) denote the two current hidden operators and let \(C_0=0\).
For a population state define its raw displacement by
\[
 R^2=d\mathbb E\|w-w_0\|^2+
       \|A-A_0\|_{\rm HS}^2+\|B-B_0\|_{\rm HS}^2+\|C\|_2^2.
\]
Suppose \(\|A_0\|_{\rm op},\|B_0\|_{\rm op}\le K\), with \(K\ge1\).
The original Gaussian first-layer initialization gives
\(\|D_{1,0}\|_2=\delta\). Since \(\|v\|=\sqrt d\,\delta\),
\[
 \|D_1\|_2\le\delta(1+R),\quad
 \|D_2\|_2\le L(K+R)\|D_1\|_2,\quad
 \|D_3\|_2\le L(K+R)\|D_2\|_2.
\]
The projected feature is \(H=(h_1^{(3)}-h_2^{(3)})/2\), so
\(\|H\|_2\le L\|D_3\|_2\). Consequently, at **any such state**,
\[
 |g|=|\langle C,H\rangle|
 \le \delta L^3 R(K+R)^2(1+R)
 \le \delta L^3K^2(1+R)^4.                         \tag{1}
\]
No dynamical, response, Gaussian-tail, or sign assumption enters (1).

At interpolation \(g=b>0\), it follows that
\[
 R\ge\left[(b/(\delta L^3K^2))^{1/4}-1\right]_+ .    \tag{2}
\]
In particular, displacement at \(g=1\) must diverge at least as
\(\delta^{-1/4}=(2/(1-\rho))^{1/8}\). If a constructed strong uncut
feature gradient path reaches \(b\) at time \(S\), its exact energy
identity gives
\[
 R^2\le S\int_0^S\|\Theta'\|^2ds=S b,
\]
and hence
\[
 S\ge b^{-1}\left[(b/(\delta L^3K^2))^{1/4}-1\right]_+^2.
                                                               \tag{3}
\]
Thus a feature interval covering interpolation for all angles cannot
have a fixed finite length for **any fixed Lipschitz activation** in
this scaling. Its necessary growth is at least
\((1-\rho)^{-1/4}\). This is a route obstruction to copying the
one-sample fixed feature interval. The contract permits pair-dependent
feature times and bounds, so (1)--(3) do not obstruct the requested
universal activation theorem.

## 2. Exact normalized contrast, with no inverse-angle coefficients

Return to the stated arctangent candidate. Write
\[
 m=(x_1+x_2)/2,\quad \mu=\sqrt{(1+\rho)/2},\quad
 U=w\cdot m/\mu,\quad V_1=w\cdot v/\delta.
\]
Omit \(U\) when \(\mu=0\). The two input directions are orthogonal;
on their span the raw first-layer metric is exactly
\(\|dU\|_2^2+\|dV_1\|_2^2\). Initially the retained \(U,V_1\)
are independent standard Gaussians. The component of \(w\) orthogonal
to both inputs is frozen and plays no role in the objective.

Define the scalar common and normalized contrast maps
\[
 P_\delta(M,V)=\frac{\phi(M+\delta V)+\phi(M-\delta V)}2,
 \qquad
 Q_\delta(M,V)=\frac{\phi(M+\delta V)-\phi(M-\delta V)}{2\delta}.
                                                               \tag{4}
\]
The exact forward equations are
\[
 M_1=\mu U,\qquad
 M_2=A P_\delta(M_1,V_1),\quad V_2=A Q_\delta(M_1,V_1),
\]
\[
 M_3=B P_\delta(M_2,V_2),\quad V_3=B Q_\delta(M_2,V_2),
 \qquad g=\delta G_\delta,quad
 G_\delta=\langle C,Q_\delta(M_3,V_3)\rangle.          \tag{5}
\]
These are the original network equations in different coordinates;
both initial matrix orientations and all common fields remain.

Set
\[
 a=\tfrac12[\phi'(M+\delta V)+\phi'(M-\delta V)],\qquad
 b=\frac{\phi'(M+\delta V)-\phi'(M-\delta V)}{2\delta}.
\]
Direct differentiation, including both factors of \(\delta\), gives
\[
 D(P_\delta,Q_\delta)=
 \begin{pmatrix}a&\delta^2 b\\ b&a\end{pmatrix},\qquad
 1\le a\le L,\qquad
 b=\frac{-2e M V}{[1+(M+\delta V)^2][1+(M-\delta V)^2]}.
                                                               \tag{6}
\]
In particular the contrast-to-common derivative is \(\delta^2 b\),
whereas the common-to-contrast derivative is \(b\). Using
\(\|\phi''\|_\infty\le2e\) and
\(\|\phi'''\|_\infty=2e\), we obtain the pointwise bounds
\[
 |b|\le2e|V|,\qquad
 |\partial_M^2 Q_\delta|\le2e|V|,\qquad
 |\partial_M\partial_V Q_\delta|\le2e,
 \qquad |\partial_V^2Q_\delta|\le2e\delta^2|V|.        \tag{7}
\]
Taylor's formula with its integral remainder also gives
\[
 |P_\delta(M,V)-\phi(M)|\le e\delta^2V^2,
 \quad
 |Q_\delta(M,V)-\phi'(M)V|\le(e/3)\delta^2|V|^3.      \tag{8}
\]
These are angle-uniform coordinate estimates for fixed \(e\).
The respective \(L^2\) rates in (8) require fourth and sixth moments
of \(V\). At a fixed \(L^2\) state, convergence still follows by
dominated convergence using \(|Q_\delta|\le L|V|\); no such moment
rate or uniformity over an \(L^2\) ball follows automatically.

Because the coordinate metric is unchanged, the scalar feature equation
is exactly
\[
 \frac{d\Theta}{ds}=\delta\nabla G_\delta(\Theta).
\]
With \(u=\delta s\), it becomes
\[
 \frac{d\Theta}{du}=\nabla G_\delta(\Theta),
 \qquad\hbox{interpolation occurs at }G_\delta=1/\delta. \tag{9}
\]
At \(\delta=0\), the forward equations (5) become the tangent network
with common map \(\phi(M)\) and contrast map \(\phi'(M)V\).
Its common-field gradients contain products such as
\(CV\phi''(M)\); this is a nonlinear model for every fixed \(e>0\).
Rescaling therefore removes inverse-angle coefficients from the
coordinate maps, but does not reduce the task to a bounded target
problem or an affine ODE. Moreover \(CV\) need not belong to \(L^2\)
when \(C,V\in L^2\), so (9) does not establish gradient convergence
on arbitrary Hilbert balls as \(\delta\downarrow0\).

## 3. A new cancellation estimate for the actual curvature returns

Use the exact population exchange involution from
SYMMETRY_RADIAL_CLOCK.md, on any constructed symmetric state. For
opposite labels, common preactivations \(M_\ell\) are even, contrasts
\(D_\ell\) and \(C\) are odd. Here "even" and "odd" refer to this
measure-preserving involution, not to a neuron identification across
layers.

Let \(q_{a,\ell}\) denote the input to the gate \(\phi'(z_a^{(\ell)})\):
\(q_{a,3}=C\), \(q_{a,2}=B^*\delta_a^{(3)}\), and
\(q_{a,1}=A^*\delta_a^{(2)}\). Put
\[
 q_{M,\ell}=(q_{1,\ell}+q_{2,\ell})/2,\qquad
 q_{D,\ell}=(q_{1,\ell}-q_{2,\ell})/2.
\]
Their parities are odd and even, respectively. Thus the scalar
curvature return splits **exactly** as
\[
 \begin{split}
 \mathbb E[q_{1,\ell}\phi''(M_\ell+D_\ell)]
 ={}&\tfrac12\mathbb E q_{M,\ell}
      [\phi''(M_\ell+D_\ell)-\phi''(M_\ell-D_\ell)]\\
 &+\tfrac12\mathbb E q_{D,\ell}
      [\phi''(M_\ell+D_\ell)+\phi''(M_\ell-D_\ell)].
 \end{split}                                                    \tag{10}
\]
For the first summand the bounded third derivative gives
\[
 |\text{first summand}|
 \le2e\mathbb E|q_{M,\ell}D_\ell|
 \le2e\|q_{M,\ell}\|_2\|D_\ell\|_2.                 \tag{11}
\]
This bound uses second moments only. It retains the cancellation that
is lost in the estimate \(2e\mathbb E|q_{1,\ell}|\).

At a state of raw displacement \(R\), the same forward argument as
in section 1 and bounded backward gates give, for \(\ell=1,2,3\),
\[
 \|D_\ell\|_2\le\delta L^{\ell-1}(K+R)^{\ell-1}(1+R),
 \quad
 \|q_{M,\ell}\|_2\le L^{3-\ell}(K+R)^{3-\ell}R.
\]
Their product has the **same total degree in all three layers**:
\[
 |\text{first summand of (10)}|
 \le2eL^2\delta R(1+R)(K+R)^2.                      \tag{12}
\]
In particular, under the additional bound \(R\le M_*\delta^{-1/4}\),
\[
 |\text{first summand}|
 \le2eL^2M_*(1+M_*)(K+M_*)^2,                       \tag{13}
\]
uniformly over every angle. The scale in this conditional bound agrees
with the necessary scale (2). This is a genuine angle-independent
curvature estimate at that scale, rather than a choice of \(e(\rho)\).
An upper bound of that scale for the nonlinear trajectory has not been
proved here.

At the top, \(q_{D,3}=0\), so (11)--(13) control the entire instantaneous
curvature return \(\mathbb E[C\phi''(z_1^{(3)})]\). The corresponding
sample-2 return is its negative. They do not control the entire top
response row, which also contains responses through the evolving
readout and earlier source times.

At the lower layers the second summand in (10) remains. Already
\[
 q_{D,2}=B^*\left[C\,
       \frac{\phi'(M_3+D_3)-\phi'(M_3-D_3)}2\right]. \tag{14}
\]
Extracting an \(O(\delta)\) factor in its \(L^2\) norm requires a
bound on the product of \(C\) with the gate difference. Equation
(11) controls a scalar contraction; it does not supply this product
bound through a bounded \(L^2\) action.

Here is an explicit obstruction to obtaining it from Hilbert bounds
and symmetry alone. Let \(E_+,E_-\) have probability \(\eta/2\), and
let the involution swap them. On these sets take respectively
\[
 C=\pm\eta^{-1/2},\qquad D=\pm1,\qquad M=1,
\]
with \(C=D=0\) elsewhere and \(M=1\) everywhere. Then
\(\|C\|_2=1\), \(\|D\|_2=\sqrt\eta\), and all required parities
hold. But the absolute gate difference divided by two is \(2e/5\)
on both sets, so
\[
 \left\|C\frac{\phi'(M+D)-\phi'(M-D)}2\right\|_2=2e/5. \tag{15}
\]
It does not vanish with \(\|D\|_2\). Taking \(\delta=\sqrt\eta\)
also gives \(\|D/\delta\|_2=1\). Thus normalization alone does not
repair the product estimate. These are test fields, not asserted
reachable Gaussian-network states. The example identifies why a
reachable-state tail or mixed-moment theorem is still needed.

## 4. Exact restoring sign, and why it is not yet a dissipativity proof

For unnormalized contrast
\(F(M,D)=[\phi(M+D)-\phi(M-D)]/2\), direct algebra gives
\[
 \partial_MF=
 \frac{-2e MD}{[1+(M+D)^2][1+(M-D)^2]},\qquad
 M C\partial_MF=
 \frac{-2e CD M^2}{[1+(M+D)^2][1+(M-D)^2]}.           \tag{16}
\]
Thus, for a frozen local readout with \(CD\ge0\), this curvature
term decreases the squared common coordinate. Its sign is independent
of the angle and of the size of the readout. This is a plausible
source of stability beyond a small-perturbation proof.

However, the corresponding pointwise sign is already absent at a
middle layer of the affine Gaussian baseline. This can be checked
without a numerical experiment or a nonlinear approximation claim.
For \(e=0\), opposite labels, and feature time near zero,
\[
 C(s)=sD_{3,0}+o(s),\qquad
 q_{M,2}(s)=sB_0^*B_0D_{2,0}+o(s)\quad\hbox{in }L^2.
\]
The initialized vector \(D_{2,0}\) is independent of \(B_0\) and has
limiting variance \(\delta^2\). Gaussian conditioning gives the
joint coordinate law
\[
 D_{2,0}=\delta X,\qquad
 B_0^*B_0D_{2,0}=\delta(X+Y),\qquad X,Y\stackrel{\rm iid}{\sim}N(0,1).
                                                               \tag{17}
\]
For completeness, at finite width put \(d=D_{2,0}\), \(y=B_0d\).
Conditional on \(d,y\), the mean of \(B_0^Ty\) is
\(d\|y\|^2/\|d\|^2\), and its remaining Gaussian covariance is
\((\|y\|^2/n)P_{d^\perp}\). The two norm ratios converge to
\(1\) and \(\delta^2\); the removed one-dimensional projection
vanishes in empirical RMS. This proves (17) using only one fixed
Gaussian transcript, not a width-limit construction of a flow.

The event \(X(X+Y)<0\) consists of two wedges of total angle
\(\pi/2\) in the rotationally invariant \((X,Y)\) plane. Therefore
\[
 \mathbb P\{D_{2,0}(B_0^*B_0D_{2,0})<0\}=1/4.        \tag{18}
\]
The product convergence implied by the preceding \(L^2\) expansions,
and the absence of an atom at zero in (17), also give a limiting
negative-sign fraction of \(1/4\) as \(s\downarrow0\).
The middle-layer local curvature summand consequently cannot be
treated as pointwise restoring merely from the affine baseline,
exchange symmetry, or positivity of the activation derivative.
Its average product is positive, so (18) does not refute a more
careful averaged dissipativity estimate. Nor does an affine sign
calculation prove a failure of the nonlinear dynamics.

## 5. Exact research status and the remaining implication

| Claim | Status | Scope / remaining dependency |
|---|---|---|
| Necessary displacement and feature-time divergence, (1)--(3) | Proved | Every fixed Lipschitz activation; constructed gradient path only for the time bound |
| Normalized maps and derivatives, (4)--(9) | Proved | Exact coordinates; gradient statement for each fixed positive angle |
| Odd-sector curvature cancellation, (10)--(12) | Proved | Symmetric states with bounded actions and the stated second moments |
| Angle-independent curvature bound at \(R=O(\delta^{-1/4})\), (13) | Exact under assumptions | The nonlinear radius upper bound is not established |
| Complete top instantaneous curvature return controlled | Proved | Does not include the full causal response row |
| Hilbert bounds plus symmetry imply the needed lower-layer product estimate | Falsified | Counterexample (15); no assertion about reachable states |
| Pointwise nonnegative middle contrast/backward product in the Gaussian affine baseline | Falsified | Exact negative fraction \(1/4\), (17)--(18) |
| Fixed activation gives uncut response continuation to each pair's target | Open | Lower-layer even backward component and full causal derivative rows remain uncontrolled |
| Full original joint MF/GF/exact-GD, nonlazy kernels, and positive nonlinear approximation error at all finite physical times | Open | None of these downstream bridges is supplied here |

The focused surviving route is an **averaged or tail-controlled estimate
for (14) and its causal source derivatives**, retaining the signed
common/contrast structure. It must use properties of actually reached
Gaussian-program fields strong enough to exclude (15), without imposing
the false pointwise sign excluded by (18). A bound on instantaneous
expected curvature alone is insufficient: the formal response recursion
also multiplies curvature by random past-source derivatives. Pair-dependent
finite constants are permitted; an angle-dependent choice of \(e\) is not.

The radial lower bound continues to give a finite pair-dependent
pre-target feature budget **on a constructed strong uncut branch**.
Its energy endpoint does not supply the missing response continuation.
No finite-width primal endpoint is used to define an uncut population
solution in this note. The existing angle-specific perturbation route
is neither upgraded nor refuted by these calculations.
