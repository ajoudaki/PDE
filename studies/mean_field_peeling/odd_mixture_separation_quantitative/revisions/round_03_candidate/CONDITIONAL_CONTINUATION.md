# A conditional continuation criterion for three inputs

**Scope and conclusion.** This note concerns the canonical three-hidden-layer population raw GF with three unit-RMS inputs and the exact odd activation
\[
\phi(z)=az+e\arctan z,\qquad a=1-e,\qquad 0<e<1/4.
\]
It uses the model and local machinery in this report, especially Appendix C, Parts F/R/V; the offset activation appearing in the reproduced Appendix C is replaced throughout by the displayed odd activation. No affine-training assumption, Gram invertibility, global generic-three-input existence, or numerical evidence is used.

The focused route is to retain the decay of arctangent curvature in the nonlinear source equations. It does **not** presently close from the finite-horizon raw energy bound. The precise obstruction is the multiplier \(Q g'(Z)\) in a response equation, where \(g(z)=(1+z^2)^{-1}\): large incoming \(Q\) need not occur at large \(Z\). Below is an explicit raw-state obstruction to an ambient estimate, together with a complete conditional lemma showing that **exponential**, rather than Gaussian, reference tails would already suffice. Neither statement proves that the obstruction occurs along the canonical reached trajectory.

## 1. Exactly what raw energy supplies

On any existing strong uncut solution,
\[
L(t)+\int_0^t\|\dot\theta(s)\|_{\rm raw}^2\,ds=L(0),
\qquad
\|\theta(t)-\theta(0)\|_{\rm raw}\le\sqrt{tL(0)}.
\]
At canonical initialization \(L(0)=3/2\). Consequently, on each finite physical horizon before a possible endpoint, all forward fields and all incoming fields
\[
\mathscr Q=\{C,q_i^2=B^*[C\phi'(z_i^3)],
q_i^1=A^*[\phi'(z_i^2)q_i^2]:1\le i\le3\}
\]
have bounded \(L^2\) norms; the initialized actions are bounded and learned increments are Hilbert–Schmidt. The controls satisfy \(\|r(t)\|_1\le3\), so physical-time source equations have a finite controlled clock on a fixed horizon.

A small additional endpoint conclusion is valid: if a strong solution exists on \([0,T_*)\), \(T_*<\infty\), raw energy makes its state strongly Cauchy as \(t\uparrow T_*\). It therefore has an endpoint \(\theta_*\) in the affine raw Hilbert space. The uncut raw field is continuous there: forward maps are locally Lipschitz, backward multiplication is strongly continuous by F.5, and rank-one products are continuous. Thus \(F(\theta(t))\to F(\theta_*)\), and the solution extends as a \(C^1\) curve to the **closed** interval \([0,T_*]\). This does not construct a solution beyond \(T_*\), nor prove uniqueness from \(\theta_*\). Local existence for a merely continuous vector field in an infinite-dimensional Hilbert space cannot be inserted here.

## 2. The exact nonclosed response term

At a gate \(\delta=\phi'(Z)Q\), with all deterministic source coefficients and covariances frozen as required by F/R,
\[
\partial_\eta\delta
 =\phi'(Z)\partial_\eta Q+e g'(Z)Q\,\partial_\eta Z,
\qquad g'(z)=-\frac{2z}{(1+z^2)^2}.                 \tag{E.1}
\]
This is the uncut version of R.44/R.49. If \(J=\partial_\eta Z\), the backward response coefficient in R.12 contains
\[
                      e E[g'(Z)QJ].                         \tag{E.2}
\]
The current source derivative has \(J=1\), so its curvature contribution is bounded by \(e\|g'\|_\infty\|Q\|_2\). This verifies that the immediate transpose return alone is not the obstruction. Propagating a past response requires (E.1) repeatedly. Cauchy–Schwarz bounds (E.2) using \(\|Q\|_2\|J\|_2\), but the next \(L^2\) response estimate requires
\[
\|g'(Z)QJ\|_2^2
 =4E\left[\frac{Z^2Q^2J^2}{(1+Z^2)^4}\right].       \tag{E.3}
\]
Neither bounded \(\|Q\|_2\) nor bounded \(\|J\|_2\) controls (E.3). A direct Hölder estimate instead asks for \(L^4\) control of both factors, and iterating generates higher moments. Retaining curvature decay simply replaces this by a joint weighted-moment obligation; no available raw-energy identity supplies that obligation.

For the simplest algebraic witness take a uniform \(U\in(0,1)\), \(Z=1\), and \(Q=J=U^{-1/3}\). Then \(Q,J\in L^2\), but \(g'(Z)QJ\notin L^2\). The same obstruction is visible in the pathwise response envelope from R.50: knowing \(E\int_0^T Q(t)^2dt<\infty\) gives \(\int_0^T|Q(t)|dt<\infty\) almost surely, but gives no integrability of
\[
               \exp\left(c e\int_0^T|Q(t)|dt\right).
\]
Such exponential integrability is exactly the step used to take expectations of the response envelope. This is an obstruction to this estimate, not a demonstrated law of an actual canonical response.

The circularity remains even though finite-program source variances are bounded by primal norms. Under already bounded response rows, R.38–R.41 give Gaussian-scale coordinate moments. The raw variance bound does not first bound those rows: their past terms contain (E.2). The finite-cap probe argument in V.3 does bound them, but its raw stability constant depends on the cap through \(eR\).

## 3. Curvature decay does not repair the ambient raw-ball estimate

The preceding separation of \(Z\) and \(Q\) can occur inside the actual affine raw state space, with its canonical initialized actions; arbitrary alternative initialized operators are unnecessary.

Fix a nonzero layer-two feature \(h\in H_2\), for example the initialized feature of one sample. Set
\[
 B=B_0+(\mathbf1-B_0h)\otimes h/\|h\|_2^2.
\]
Then \(B-B_0\) is Hilbert–Schmidt and \(Bh=\mathbf1\). The canonical layer-three space contains a nondegenerate Gaussian initial forward answer, hence a uniform variable \(U\) obtained by its Gaussian distribution function. Choose the permissible raw readout \(C=U^{-1/3}\in H_3\). At this state the selected top preactivation is identically one, whereas its incoming field is \(C\), with polynomial tails. All primal raw quantities are finite, and
\[
                        C\phi''(1)=-(e/2)C
\]
is unbounded. Let \(E_n=\{C>n\}\), fix \(t\ne0\) small with \(\phi'(1+t)\ne\phi'(1)\), and perturb only
\[
                 B_n-B=t\mathbf1_{E_n}\otimes h/\|h\|_2^2.
\]
These perturbations converge to zero in Hilbert–Schmidt norm. Nevertheless, the ratio of the selected top-backward-field change to the raw perturbation satisfies
\[
\frac{\|C[\phi'(1+t\mathbf1_{E_n})-\phi'(1)]\|_2}
 {\|B_n-B\|_{\rm HS}}
\ge n\|h\|_2\frac{|\phi'(1+t)-\phi'(1)|}{|t|}\longrightarrow\infty.
\]
Thus even this backward observation is not locally Lipschitz at every bounded-primal raw state. On the sets causing failure, the preactivation stays at the fixed value one. This construction is **not** a reached-state counterexample and does not disprove canonical global continuation. It does rule out deriving the needed estimate from an ambient raw bound alone without additional canonical structure.

## 4. Conditional lemma: exponential reference tails suffice on any finite horizon

**Lemma E.1.** Fix \(0<e<1/4\) and \(0<T<\infty\). Suppose the canonical finite-cap reference flows \(\theta_R\) exist on \([0,T]\), share initialization and initialized actions, and have a common primal bound. The incoming fields at a cap state are
\[
 q_i^{2,R}=B_R^*D_R(z_i^{3,R},C_R),\qquad
 q_i^{1,R}=A_R^*D_R(z_i^{2,R},q_i^{2,R}),\qquad
 \mathscr Q_R=\{C_R,q_i^{2,R},q_i^{1,R}:1\le i\le3\}.
\]
Assume that the following bound holds for some finite \(A\ge1,c>0\), independent of \(R\):
\[
\sup_{R,t\le T,Q\in\mathscr Q_R(t)}
     \|Q\mathbf1_{\{|Q|>u\}}\|_2\le A \exp(-cu)
                       \qquad(u\ge1).                       \tag{E.4}
\]
Then these references converge uniformly in raw state and raw direction to a strong uncut flow on \([0,T]\). That flow is unique against every bounded-primal strong uncut competitor with the same initialization. The argument imposes no smallness relation between \(e\) and \(T\). Consistent assumptions for all finite horizons yield a global flow and unique continuation from its reached states.

**Proof.** For any two gate caps \(R',R\ge M\ge1\), including an infinite cap, splitting according to \(|\bar q|\le M\) gives
\[
|D_{R'}(z,q)-D_R(\bar z,\bar q)|
\le |q-\bar q|+C eM|z-\bar z|
                  +4e|\bar q|\mathbf1_{\{|\bar q|>M\}}.     \tag{E.5}
\]
Indeed both clips equal the identity on the first set; on the second, their absolute values are at most \(|\bar q|\), and \(g\) is bounded. The map in its incoming variable is 1-Lipschitz because \(a+e=1\) and the clips have derivative bounded by one.

Propagating (E.5) through the three backward stages, with V.8–V.9 for the forward maps and rank-one velocities, gives for the raw sum distance \(d(t)=\|\theta_{R'}(t)-\theta_R(t)\|_{\rm sum,raw}\)
\[
D^+d(t)\le K\big[(1+eM)d(t)+eA \exp(-cM)\big],
              \qquad 1\le M\le\min(R,R').                   \tag{E.6}
\]
Only the reference tails occur. The same inequality holds against an uncut bounded-primal competitor; its primal bound changes \(K\).

Let \(R\) denote the smaller finite cap, set \(\varepsilon_R=A\exp(-cR)\), and put \(u=d+\varepsilon_R\). While \(u\le A\exp(-c)\), choose the admissible moving threshold
\[
                         M=c^{-1}\log(A/u).
\]
Since \(u\ge\varepsilon_R\), this threshold is at most \(R\). Equation (E.6) yields, after increasing a constant depending only on the stated bounds,
\[
                 D^+u\le K_1u\log(\exp(1)A/u).
\]
With identical initialization, \(u(0)=\varepsilon_R\). Integration, or setting \(v=\log(\exp(1)A/u)\), gives
\[
\sup_{t\le T}d(t)
\le \exp(1)A\exp\left[-(1+cR)\exp(-K_1T)\right].             \tag{E.7}
\]
For sufficiently large \(R\), this estimate remains inside the stipulated threshold range on the whole interval, justifying the stopping argument. It tends to zero for every fixed \(T\). This is the Osgood estimate for the modulus \(s\log(1/s)\).

To obtain convergence of directions, use the field version of (E.6) with a fixed threshold \(M=\alpha R\), where \(0<\alpha<\exp(-K_1T)\). The distance contribution is a polynomial factor times the decaying bound (E.7), while the tail term is \(A\exp(-c\alpha R)\). Both vanish uniformly. Completeness gives uniform limits of states and directions; their integral identity proves a strong \(C^1\) path. Applying the same field estimate with the uncut gate identifies its direction. Comparing any strong uncut competitor to these references proves uniqueness.

At a reached time \(t_0\), the discrepancy from the cap reference is already exponentially small in \(R\) by (E.7). The identical Osgood calculation starting with this exponentially small discrepancy still tends to zero on every finite subsequent interval. This proves the asserted continuation uniqueness. ∎

Condition (E.4) follows, for example, from a uniform \(\|Q\|_p\le Kp\) bound for all \(p\ge2\), or a uniform positive exponential moment. Ordinary finite \(L^p\) bounds are insufficient for this particular argument. The constants in (E.4) may depend on \(T\); \(e\) need not.

**Remaining obligation.** Prove at least the exponential-tail property (E.4), or another Osgood modulus, for the canonical references without cap-dependent constants. The curvature-weighted product (E.3) is the concrete nonclosed term in the tested route. Its control would need a reached-state correlation/response estimate beyond finite-horizon raw energy. No global three-input source-regularity claim is established here.
