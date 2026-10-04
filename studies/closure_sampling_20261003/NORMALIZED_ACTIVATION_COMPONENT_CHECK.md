# Internal reconstruction of normalized activation components

2026-10-04. Checker: scoped agent `critical_activation_geometry`.

Verdict: the new elementary conclusions in the two assigned frozen inputs are
correct in their stated activation classes. I found no wrong GELU moment,
variance gain, strip bound, or mixed-moment counterexample. The normalization
note's opening claim is slightly broader than the assumptions of its written
covariance proof; Section 2 below supplies the short proof extension. This
does not change any formula or example.

This is a cross-route internal check after my own independent route was frozen.
It is not an independent promotion review. I read both assigned inputs in full,
including their limitations and inherited interfaces, and no further scientific
files. The supervisor's bounded assignment was to check new elementary math;
the prior compression/source interfaces remain inherited and were not checked
against their underlying files. Required skills and instructions were already
read during the independent route and remain applicable.

## 1. Fixed inputs and coverage

The following SHA-256 values were verified before reading and checking:

| Frozen input | SHA-256 |
| --- | --- |
| `NORMALIZED_ACTIVATION_EXAMPLES_ROUTE.md` | `1e14c318bb8352007c8326d601cd654b865cf40c71d7f0156c2d50305510b4b8` |
| `BETA_ENVELOPE_AUDIT.md` | `42461b5f2381b337c2646ab7c5387921abf8b3e1f255df7160d5757025940d28` |

Both complete files were returned without truncation by their reads. I checked
all their newly derived elementary formulas, with particular attention to
exact GELU, complex strips, supremum rigidity, and mixed moments. I inspected
the erf calculation too; the supervisor is arranging an additional erf
reconstruction separately. I did not independently verify the correspondence
between quoted beta/source/runtime constants and the unavailable inherited
source files, or any all-time compression theorem.

## 2. General normalization and its precise regularity scope

Let \(Z\sim N(0,1)\). For a nonconstant smooth real function \(g\), write
\(\mu=\mathbb E g(Z)\), \(V=\operatorname{Var}(g(Z))\), and
\(D=\mathbb E g'(Z)^2\). If \(g'\) is bounded, then \(g\) has at most
linear growth, both moments are finite, and \(D>0\). Once \(V\le D\), the
two positive-output-rescaling normalizations are exactly
\[
\phi_\pm(x)=\frac{g(x)-\mu\pm\sqrt{D-V}}{\sqrt D}.
\]
The derivative condition fixes the multiplier to \(D^{-1/2}\); the value
condition fixes the squared Gaussian mean to \(1-V/D\). These substitutions
verify both required unit second moments without any centering assumption.

The source proves \(V\le D\), and affinity in the equality case, when both
\(g'\) and \(g''\) are bounded. I reconstructed its covariance derivative:
for independent standard \(X,Y\), put \(Y_r=rX+\sqrt{1-r^2}Y\).
Differentiation of \(\mathbb E g(X)g(Y_r)\) and integration by parts in
\(X,Y\) cancel the two terms containing \(g(X)g''(Y_r)\). The result is
\(\mathbb E g'(X)g'(Y_r)\). Both marginals are standard normal, so its
absolute value is at most \(D\), and integration over \(0\le r\le1\)
gives the claimed covariance and deficit identities.

Here is the missing extension to the opening statement's bounded-first-
derivative hypothesis. Choose a nonnegative smooth compactly supported
mollifier \(\rho_\varepsilon\), of integral one and support
\([-\varepsilon,\varepsilon]\), and set
\(g_\varepsilon=g*\rho_\varepsilon\). If \(|g'|\le M\), then
\[
|g_\varepsilon'|\le M,\qquad
|g_\varepsilon''|\le M\|\rho_\varepsilon'\|_{L^1},\qquad
|g_\varepsilon(x)|\le |g(0)|+M(|x|+\varepsilon).
\]
The source's proof applies to each \(g_\varepsilon\). As
\(\varepsilon\downarrow0\), both \(g_\varepsilon(x)\to g(x)\) and
\(g_\varepsilon'(x)\to g'(x)\) pointwise. The displayed bounds allow
Gaussian dominated convergence of the value and derivative moments.
They also allow dominated convergence over \(r\in[0,1]\) in the identity
\[
D_\varepsilon-V_\varepsilon
=\frac12\int_0^1
 \mathbb E[(g_\varepsilon'(X)-g_\varepsilon'(Y_r))^2],dr.
\]
Thus exactly the same identity holds for \(g\). If its left side is zero,
some \(r\in(0,1)\) has zero integrand. The joint Gaussian density is
strictly positive on \(\mathbb R^2\); continuity of \(g'\) then forces
\(g'(x)=g'(y)\) for all \(x,y\). Hence \(g\) is affine. This proves the
broader claim with its equality case, without a bound on \(g''\).

The frozen normalization source prints a literal comma before `dr` in its
deficit integral (6). This is a harmless typography issue: the intended
Lebesgue integral in \(r\) and its mathematics are unambiguous. I left the
frozen input unchanged.

The source's consequences for odd nonaffine functions, nonzero input scaling,
identity, and \(x+\varepsilon\tanh x\) all follow: oddness survives nonzero
input scaling and implies \(\mu=0\), so \(\mathbb E g(Z)^2<D\) in each
nonaffine case. For the near-identity example,
\(\mathbb E Z\tanh Z=\mathbb E\operatorname{sech}^2 Z\) follows from one
Gaussian integration by parts, giving exactly the two quadratic polynomials
in \(\varepsilon\) in the source. Their difference is
\(\varepsilon^2(D_{\tanh}-Q_{\tanh})>0\).

For erf at input scale \(\alpha>0\), direct differentiation and integration
by parts reproduce
\[
\mathbb E[Z\operatorname{erf}(\alpha Z)e^{-\alpha^2Z^2}]
=\frac{2\alpha}{\sqrt\pi(1+2\alpha^2)\sqrt{1+4\alpha^2}},
\]
and therefore the derivative of its value second moment is
\(8\alpha/[\pi(1+2\alpha^2)\sqrt{1+4\alpha^2}]\). Differentiating the
source's arcsine formula gives this same expression; both value moments
vanish at zero. The derivative second moment is the stated one-step Gaussian
integral. I found no normalization or input-scale discrepancy.

## 3. Exact GELU reconstructed from elementary Gaussian integrals

Write \(\varphi(x)=(2\pi)^{-1/2}e^{-x^2/2}\),
\(\Phi(x)=\int_{-\infty}^x\varphi(u)du\), and \(g(x)=x\Phi(x)\).
Then
\[
g'=\Phi+x\varphi,\qquad
g''=(2-x^2)\varphi,\qquad
g'''=(x^3-4x)\varphi.
\]
The density \(\varphi^3\) is a positive multiple of the centered Gaussian
density of variance \(1/3\). Its integral is
\[
I_0=\int\varphi(x)^3dx=\frac1{2\pi\sqrt3},
\]
so its second, fourth, and sixth moments are respectively
\(I_0/3,I_0/3,5I_0/9\). Also
\(\mathbb E\varphi(Z)=1/(2\sqrt\pi)\), and
\(\mathbb E[Z^2\varphi(Z)]=1/(4\sqrt\pi)\).

Gaussian integration by parts gives
\(\mathbb E g(Z)=\mathbb E\varphi(Z)=1/(2\sqrt\pi)\).
The variable \(\Phi(Z)\) is uniform on \((0,1)\), since
\(\mathbb P(\Phi(Z)\le u)=u\); hence \(\mathbb E\Phi(Z)^2=1/3\).
Put
\[
J_1=\int x\Phi(x)\varphi(x)^2dx,\qquad
J_3=\int x^3\Phi(x)\varphi(x)^2dx.
\]
Using \((\varphi^2)'=-2x\varphi^2\) and vanishing Gaussian boundary terms,
\[
J_1=\frac12I_0,\qquad
J_3=J_1+\frac12\int x^2\varphi(x)^3dx
=\frac23I_0.
\]
Expansion of \(g'^2\), and two Gaussian integrations by parts for
\(\mathbb E[Z^2\Phi(Z)^2]\), now give
\[
\begin{aligned}
Q=\mathbb E g(Z)^2&=\frac13+2I_0-2J_1
 =\frac13+I_0,\\
D=\mathbb E g'(Z)^2&=\frac13+2J_1+I_0/3
 =\frac13+\frac43I_0.
\end{aligned}
\]
Therefore \(D-Q=I_0/3=1/(6\pi\sqrt3)\), as stated. With
\(\mu=1/(2\sqrt\pi)\) and \(c=1/(6\pi\sqrt3)\), the raw offsets are
\(b_\pm=-\mu\pm\sqrt{\mu^2+c}\), and
\(\phi_\pm=(g+b_\pm)/\sqrt D\) satisfies both unit moments exactly.

The input-scale obstruction also checks directly. For
\(g_\alpha(x)=x\Phi(\alpha x)\), let
\(I=\mathbb E\varphi(\alpha Z)^2=[2\pi\sqrt{1+2\alpha^2}]^{-1}\).
The Gaussian density in
\(\mathbb E[Z\Phi(\alpha Z)\varphi(\alpha Z)]\) has logarithmic
derivative \(-(1+\alpha^2)x\), so integration by parts gives this
expectation as \(\alpha I/(1+\alpha^2)\). The other needed integral is
\(\mathbb E[Z^2\varphi(\alpha Z)^2]=I/(1+2\alpha^2)\). Substitution gives
\[
D_\alpha-Q_\alpha
=\frac{\alpha^2 I}{1+2\alpha^2}
=\frac{\alpha^2}{2\pi(1+2\alpha^2)^{3/2}}>0.
\]
Thus a nonzero input scale and output multiplier without an offset cannot
normalize exact GELU. The same calculation depends only on \(\alpha^2\)
and also covers negative nonzero scales if needed.

The curvature moments used for the correlation derivatives are
\[
\mathbb E g''(Z)^2
=I_0(4-4/3+1/3)=3I_0=\frac{\sqrt3}{2\pi},
\]
and
\[
\mathbb E g'''(Z)^2
=I_0(5/9-8/3+16/3)
=\frac{29}{18\pi\sqrt3}.
\]
Dividing by \(D\) gives both coefficients in the source. Neither depends
on the offset.

## 4. GELU variance gains, including both signs

Define the scalar variance map
\(V_\phi(q)=\mathbb E\phi(\sqrt q Z)^2\) for \(q>0\). Its derivative at
one is
\[
V_\phi'(1)=\mathbb E[Z\phi(Z)\phi'(Z)]
=\mathbb E\phi'(Z)^2+\mathbb E[\phi(Z)\phi''(Z)].
\]
The first equality differentiates in \(q\); the second is Gaussian
integration by parts. For the GELU branches, linear growth of \(\phi\)
and bounded real derivatives justify both operations. From the integrals
above,
\[
\mathbb E g''(Z)=\frac3{4\sqrt\pi},\qquad
\mathbb E[g(Z)g''(Z)]=2J_1-J_3=\frac1{6\pi\sqrt3}=c.
\]
Consequently
\[
V_{\phi_\pm}'(1)
=1+\frac{c+3b_\pm/(4\sqrt\pi)}D.
\]
Since \(b_+>0\), the plus gain exceeds one. For the minus branch let
\(A=1/(4\pi)\). Its numerator after the one is
\(c-(3/2)\sqrt A(\sqrt A+\sqrt{A+c})\). It is negative since
\(c<3A\). Its absolute value is at most
\(3A-c/4<1/3<D\), using
\(\sqrt{A(A+c)}\le A+c/2\). Thus the minus gain is strictly between zero
and one. Independent quadrature and finite differences gave respectively
`1.11349206382` and `0.49718401063`, agreeing with the source.

These are variance-direction gains. They do not contradict unit tangent
covariance gains on the unit sphere, and neither sign proves a statement
about all-time finite-width network training.

## 5. Complex strips and rigidity of a derivative supremum of one

For \(z=x+iy\),
\[
|\cosh z|^2=\sinh^2x+\cos^2y,\qquad
|\sinh z|^2=\sinh^2x+\sin^2y.
\]
For \(|y|<\pi/4\), their ratio bounds \(|\tanh z|\) by one, and
\(|\operatorname{sech}^2z|\le2\). This proves the tanh and near-identity
derivative certificates after their stated output rescalings.

For \(\operatorname{erf}(\alpha z)\), the modulus of its derivative is
\((2\alpha/\sqrt\pi)e^{-\alpha^2x^2+\alpha^2y^2}\), which gives the
source's strip bound. Integrating vertically from the real axis gives
bounded values on each fixed finite strip.

For GELU, on \(|y|<a\),
\[
|\varphi(z)|\le\frac{e^{a^2/2}}{\sqrt{2\pi}}e^{-x^2/2},\qquad
|\Phi(z)|\le1+\frac{ae^{a^2/2}}{\sqrt{2\pi}}.
\]
The second bound comes from the vertical integral and \(0\le\Phi(x)\le1\).
Using \(|z|\le|x|+a\) and
\(\sup_x |x|e^{-x^2/2}=e^{-1/2}\), I recover
\[
|g'(z)|\le1+\frac{e^{a^2/2}}{\sqrt{2\pi}}(2a+e^{-1/2}).
\]
Both normalized GELU branches therefore satisfy the inherited strip-derivative
hypothesis. Entire holomorphy does not make the derivative uniformly bounded
over increasing strip widths. Applying Cauchy's integral formula to
\(\phi'\) on a disk of radius \(a/4\) centered in \(|\operatorname{Im}z|\le a/2\)
gives exactly \((j-1)!s(4/a)^{j-1}\) for \(|\phi^{(j)}|\). Each disk
lies strictly inside the original strip, so there is no boundary assumption.

If a normalized continuously differentiable activation satisfies
\(\sup_{\mathbb R}|\phi'|\le1\), its derivative unit second moment makes
\(|\phi'|=1\) Gaussian-almost everywhere, hence everywhere by continuity.
Connectedness of the real line then gives a constant sign, so
\(\phi(x)=\pm x+b\). Its value unit second moment forces \(b=0\). The
strict derivative-supremum statement for every nonaffine normalized example
is therefore correct.

Likewise, when the derivative is bounded, strict convexity applied to
\(|\phi'|^2\) gives \(\mathbb E|\phi'|^p>1\) for every \(p>2\) in the
nonaffine case. Independent scalar gates multiply these moments exactly.
The source correctly refrains from equating this scalar product with a dense
matrix Jacobian or a Schatten-moment lower bound. The fixed-order polynomial
depth proof via the chain rule also checks: every nonidentity increment at
derivative order \(j\) has polynomial degree at most \(j-2\) in depth,
so summation yields degree at most \(j-1\). This says nothing uniform in
\(j\), and its stated restriction is necessary.

## 6. The beta audit's new Gaussian and mixed-moment calculations

The algebraic redundancy
\(\max(10,32B/a^2)\ge\sqrt{320B}/a>16/a\) follows from
\(\max(u,v)\ge\sqrt{uv}\) and \(B\ge1\). This verifies the new
redundancy assertion, conditional on the inherited displayed definition;
it does not verify that definition's source provenance.

For independent-vector Gaussian mixing, each row pairing with a deterministic
or independent vector \(q\) has variance \(\|q\|_2^2/n\), independently
over rows. The ratio of squared norms is therefore \(\chi_n^2/n\).
For the adaptive vector \(q=r_1/\|r_1\|_2\), defined almost surely, the
first row contributes \(\|r_1\|_2^2\), while the remaining rows contribute
conditionally \(\chi_{n-1}^2/n\). The means tend to one and their variances
are at most \(2/n\). Chebyshev proves the sum tends to two in probability.
Thus the distinction between given-vector and operator bounds is correct
without invoking any random-matrix limit theorem.

For a centered Gaussian pair with \(\mathbb EZ^2=1\),
\(\mathbb EJ^2=v\), \(\mathbb EZJ=c\), substitute
\(J=cZ+\sqrt{v-c^2}U\), with \(U\) independent standard normal. The
cross term vanishes, and the result is
\[
\mathbb E[\phi'(Z)^2J^2]
=v+c^2(\mathbb E[Z^2\phi'(Z)^2]-1).
\]
This expression is finite in the bounded-derivative classes under discussion.
It would need extended-value care if used solely under \(\phi'\in L^2\)
without a bound on the mixed moment.

For the audit's normalized cosine example, with \(u=\omega^2\),
\[
\operatorname{Var}(\cos(\omega Z))
=\frac{(1-e^{-u})^2}{2},\qquad
A_\omega^2\operatorname{Var}(\cos(\omega Z))
=\frac{\tanh(u/2)}u<\frac12.
\]
These identities verify the real output offset and value normalization.
The derivative normalization and radial mixed moment follow from
\(\mathbb E[Z^2\cos(bZ)]=(1-b^2)e^{-b^2/2}\), giving precisely
\(1+4\omega^2/(e^{2\omega^2}-1)>1\). This is a valid bounded entire
radial-direction example and is not a tangent-sphere counterexample.

For the spike family, write
\(c_k=(1+4k^2)^{1/4}\) and
\(\psi_k(x)=c_k\int_0^x e^{-k^2t^2}dt\). The source's real supremum
bound is the squared Gaussian half-integral,
\(\pi\sqrt{1+4k^2}/(4k^2)\). Its logarithmic derivative is negative for
\(k>0\), and its value at \(k=2\) is less than one. Oddness therefore
makes the specified offset real and the value second moment exactly one.
The vertical strip integration is legitimate for the entire primitive and
gives its stated bound. Constants depend on \(k\), as disclosed.

Since \(\phi_k'=c_k e^{-k^2x^2}\) and
\(\phi_k''=-2k^2xc_k e^{-k^2x^2}\), elementary Gaussian integrals give
\[
\mathbb E\phi_k'(Z)^2=1,\qquad
\mathbb E\phi_k'(Z)^4=\frac{1+4k^2}{\sqrt{1+8k^2}},\qquad
\mathbb E\phi_k''(Z)^2=\frac{4k^4}{1+4k^2}.
\]
All three formulas and their divergence conclusions are correct. For
\(Q=\phi_k'(Z)U\), independence and the Gaussian moments
\(\mathbb EU^2=1\), \(\mathbb EU^4=3\) give exactly the stated tangent
second and fourth moments. Taking equal product factors gives
\(\sqrt{\mathbb EQ^4}\), which is unbounded across the activation family.
It refutes a bound based on the two scalar normalization equations alone;
the text properly does not identify the equal factors with an actual
training response.

The differentiated layer product rule is algebraically correct. Hölder's
bound \(\|R\odot J\|_{2,n}\le\|R\|_{4,n}\|J\|_{4,n}\) is direct
Cauchy--Schwarz. The mobility-coordinate training law and its coefficient
\(2/m\) are inherited interfaces, not independently re-established in this
bounded check. No step in the new examples proves either unavoidable
exponential all-time behavior or a polynomial all-time compression bound.

## 7. Executed arithmetic checks, including a failed quadrature attempt

I ran Python with NumPy 1.26.4 and SciPy 1.13.0 from the checkout root.
The checks used `scipy.integrate.quad`, absolute and relative tolerances
`2e-12`, `limit=400`, and the real integration interval `[-12,12]`.
They are arithmetic sanity checks, not numerical substitutes for the exact
proofs above. No files or generated datasets were produced.

Independent quadrature reproduced the seven GELU quantities
\(\mu,Q,D,\mathbb E g'',\mathbb E gg'',\mathbb E(g'')^2,
\mathbb E(g''')^2\) with absolute errors at most `1.11e-16` against their
closed forms. The central difference
\([V_\phi(1+10^{-5})-V_\phi(1-10^{-5})]/(2\cdot10^{-5})\)
agreed with the two exact variance gains to `1.15e-11` and `1.82e-11`.
The same script verified scaled GELU at input scales `0.2,1,3` and the
cosine normalization and mixed moments at frequencies `0.2,1,3`, all within
`2e-11`.

The first script exited with status one on the spike test at `k=20`.
Inspection found that adaptive quadrature in the original variable returned
zero for the very narrow nonnegative curvature integrand, whose value is
zero at the origin. It had missed the peak; this was a numerical integration
failure, not a discrepancy in the formula. I retained that outcome here.
Changing variables to \(t=kz\) resolved it. The exact second, fourth, and
curvature moments for `k=2,5,20` were then recovered within `2e-9`; the
corrected script exited with status zero. The failed direct curvature value
at `k=20` was `0.0`; the transformed and exact values were both
`399.75015615240477`.

The essential corrected spike check is reproducible with:

```python
import math
from scipy.integrate import quad
pdf = lambda z: math.exp(-z*z/2) / math.sqrt(2*math.pi)
for k in (2., 5., 20.):
    c = (1 + 4*k*k)**0.25
    dp = lambda z: c * math.exp(-k*k*z*z)
    dpp = lambda z: -2*k*k*z*dp(z)
    exact = (1., (1+4*k*k)/math.sqrt(1+8*k*k),
             4*k**4/(1+4*k*k))
    fs = (lambda z: dp(z)**2,
          lambda z: dp(z)**4,
          lambda z: dpp(z)**2)
    actual = [quad(lambda t: f(t/k)*pdf(t/k)/k, -12, 12,
                   epsabs=2e-12, epsrel=2e-12, limit=400)[0]
              for f in fs]
    for observed, expected in zip(actual, exact):
        assert abs(observed-expected) < 2e-9
```

The GELU quadrature check can be reproduced by defining `g(z)=z*ndtr(z)`,
`gp(z)=ndtr(z)+z*pdf(z)`, `gpp(z)=(2-z*z)*pdf(z)`, and
`gppp(z)=(z**3-4*z)*pdf(z)`, then integrating each displayed moment times
`pdf(z)` with the same settings. Its observed core values were:

| Quantity | Independent quadrature |
| --- | ---: |
| \(\mu\) | 0.282094791774 |
| \(Q\) | 0.425221482570 |
| \(D\) | 0.455850865649 |
| \(\mathbb E g''\) | 0.423142187661 |
| \(\mathbb E gg''\) | 0.030629383079 |
| \(\mathbb E(g'')^2\) | 0.275664447711 |
| \(\mathbb E(g''')^2\) | 0.296084036430 |

Before writing I checked HEAD, tracked-worktree status, and the common index.
HEAD remained `4dfa5c1ef2c5b920eda2bbc84316b189b97da92e`, the index was empty,
and unrelated tracked changes were not read or touched. Only this assigned
report was written. Neither frozen input was edited. Their hashes were checked
again after the reconstruction; the report hash is supplied separately to
the supervisor.
