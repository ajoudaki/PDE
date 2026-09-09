# Independent check of the three-sample large-gain bootstrap

Checked `/tmp/three_affine_route.md` against the exact raw metric and population equations in `studies/mean_field_peeling/two_sample_separated_angle_theorem/PROOF.md`. No sibling notes, reviews, or experiments were used.

**Verdict: PASS for the proposed large-gain, cap-uniform bootstrap, with one explicit truncation-definition clarification.** The note does not prove an uncut construction, a three-sample response theorem, uniqueness after cap removal, a finite-width bridge, or the unit-slope family. Its stated separation of those obligations is necessary and correct.

The truncation should be defined by

\[
\tau_N(q)=\max\{-N,\min\{q,N\}\},
\]

or the assumptions should explicitly include \(\|\tau_N\|_\infty\le N\). The displayed conditions “odd, 1-Lipschitz, and \(|\tau_N(q)|\le|q|\)” alone do not imply this: the identity function meets all three. The fixed-cap Lipschitz proof uses the missing boundedness. With the usual meaning of an actual cap, this is a definition clarification, not a failure of the route.

## Algebra and norms

1. The determinant identity is correct. Writing the three correlations as \(p,q,r\), direct expansion of both sides gives
   \[
   \det(\Gamma+\mathbf1\mathbf1^T)
   =4-2(p^2+q^2+r^2)+2(pq+pr+qr)+2pqr-2(p+q+r).
   \]
   Since \(\Gamma\succeq0\) and each \(1-\rho_{ab}\ge\delta\), its determinant is at least \(2\delta^3\). Trace 6 gives \(\lambda_1\lambda_2\le((\lambda_1+\lambda_2)/2)^2\le9\), hence the claimed lower eigenvalue bound. Also \(0\le\|u_1+u_2+u_3\|^2\le9-6\delta\), so the feasible range and \(m\le3/4\) are correct.

2. For \(\phi=a(1+z)\), the three initial feature Grams are
   \[
   a^2(\Gamma+J),\quad a^4\Gamma+(a^4+a^2)J,\quad
   a^6\Gamma+(a^6+a^4+a^2)J,
   \qquad J=\mathbf1\mathbf1^T.
   \]
   This verifies (2). On common initialized actions of norm at most 10, the successive perturbation bounds are exactly \(\pi/2,11\pi a/2,111\pi a^2/2\). Three columns contribute the stated factor \(\sqrt3\). The requirement \(a\ge700/\sqrt m\) suffices because \(111\pi\sqrt3<700\).

3. The first raw block controls every projected preactivation change without a dimension loss:
   \[
   \|(w-w_0)\cdot x_a\|_2
   \le\sqrt d\|w-w_0\|_2\le E.
   \]
   The normalized forward bounds \((5,58,641)\), normalized feature perturbation bounds \((2,50,1116)E\), and preactivation perturbation bounds \((1,25a,558a^2)E\) all follow with the stated initialized/current action constants 10 and 11. The chosen radius gives
   \(1116\sqrt3R<\sqrt m/4\), so (6) is valid with room to spare.

4. Backward bounds \((2a,44a^2,968a^3)\|C\|\) hold for both actual and capped gates. In the first raw gradient block, the \(1/d\) update and \(d\)-weighted metric cancel the input norm exactly. The three hidden block coefficients are therefore \(\sqrt3(968,220,116)\), as claimed, and
   \[
   968^2+220^2+116^2=998880<10^6.
   \]
   Thus 2000 in (8) is valid. The readout norm bound is \(641\sqrt3a^3\|r\|\); combining it with (8) and \(\|C\|\le R<1\) validates the deliberately loose constant 4000.

## Capped dissipation and existence

The capped vector field is not assumed to be a loss gradient. In the exact raw metric its chain rule is

\[
L'=-\|F_3r\|^2-\langle D_h,\widehat D_h\rangle_{\rm raw}.
\]

Bounding the second term in absolute value yields

\[
L'\le-a^6(m/16-4\cdot10^6R^2)\|r\|^2
\le-a^6m\|r\|^2/32,
\]

since \(4\cdot10^6R^2=m/100<m/32\). There is no hidden sign assumption. The scalar loss is differentiable along the strong raw-state path: bounded activation derivatives give the coordinate chain rule, and the scalar pairings with fixed \(L^2\) reverse fields justify differentiation by truncating those fields and passing to the limit. This does not require the activation Nemytskii map to be Fréchet differentiable from \(L^2\) to \(L^2\).

Because \(L=\|r\|^2/2\), the residual exponent is \(-\lambda t\), not \(-\lambda t/2\). Initial readout zero and three labels in \(\{-1,1\}\) give \(\|r(0)\|=\sqrt3\). Integrating the speed yields exactly

\[
E(t)\le128000\sqrt3/(a^3m)<R/2.
\]

Before continuation is proved, (11) should be read on every stopped prefix, with \(\int_0^t\|r\|\le\tau_0\); the integral to infinity follows after global existence. This is a harmless ordering convention and does not create circularity.

For the explicit bounded truncation,

\[
\|g(z)\tau_N(q)-g(\widetilde z)\tau_N(\widetilde q)\|_2
\le N\|g'\|_\infty\|z-\widetilde z\|_2
 +\|q-\widetilde q\|_2.
\]

All remaining operations are Lipschitz coordinate maps or bounded bilinear actions/pairings/outer products on bounded raw balls. Thus the fixed-cap field is locally Lipschitz in the stated Hilbert state. The strict stopped bound prevents exit. At a hypothetical finite maximal time the bounded velocity makes the state Cauchy; its limit remains inside the ball, where local existence extends it. This proves the claimed global fixed-cap existence without assuming an uncut flow.

## Arbitrary controlled affine reference

For every measurable \(\|\gamma(s)\|_2\le1\), the affine field has uniform bounded-ball Lipschitz constants and speed at most \(4000a^3\). Local solutions of the integral equation follow by contraction even though time dependence is only measurable. On duration at most \(\tau_0\), the integrated speed is less than \(R/2\), giving continuation through the entire prescribed clock interval. No sign, alignment, symmetry, or loss property of \(\gamma\) is needed.

The same estimate holds for Euler prefixes whose total clock duration is at most \(\tau_0\): induction controls each node and the segment from that node using the total accumulated step length. No small-step assumption is needed for this particular displacement estimate. This proves the conditional Euler-prefix premise stated in the note; it does not independently bound the residual-clock duration of a discretized physical flow.

For an actual residual clock, coefficients can be extended by zero beyond its image if needed, including when its endpoint corresponds to \(t\to\infty\). The arbitrary-control argument already covers this extension.

## Nonaffinity and final parameter selection

Initial preactivations remain centered Gaussian under the usual initial covariance recursion. For centered Gaussian \(Z\), write \(\phi(Z)=a+[aZ+e\arctan Z]\). The bracket is odd and has magnitude at least \(a|Z|\), so the next preactivation variance is
\(\mathbb E\phi(Z)^2\ge a^2+a^2\mathbb EZ^2\). This verifies the lower standard-deviation bound 1 in every layer.

The regression formula for \(\mathcal R(\sigma G)\) is correct. It is continuous, positive for every finite \(\sigma>0\), and converges to
\(\pi^2/4-\pi/2>0\) as \(\sigma\to\infty\). Thus \(\eta_*>0\). The cited stability estimate with initial standard deviation at least 1 gives the stated threshold \(t_*\) and margin \(\eta_*/4\).

The worst preactivation displacement is

\[
558a^2\frac{128000\sqrt3}{a^3m}
=\frac{71424000\sqrt3}{am}.
\]

The original numerical choice of \(a\) need not itself satisfy the nonaffinity threshold for very small \(\delta\), but Section 6 explicitly enlarges it. A concrete final choice is

\[
a\ge\max\left\{\frac{10^6}{\sqrt m},
\frac{142848000\sqrt3}{m t_*}\right\}.
\]

This leaves every earlier estimate valid and makes the final displacement at most \(t_*/2\). Consequently all three samples and all layers have activation regression error at least \(e^2\eta_*/4\) for every fixed \(e>0\), uniformly in time and finite cap. Strong-limit passage is valid conditional on the separately required strong uncut construction. No Gaussianity at trained times is used.

The remaining response, cap-removal, uniqueness, width/GD, and initial-motion tasks must remain explicitly separate. No additional flaw in this bounded lemma was found.
