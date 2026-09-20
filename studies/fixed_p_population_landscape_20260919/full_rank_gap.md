# Final bounded attempt at the sample-count gap

2026-09-19. Informed post-freeze analysis. Authorized inputs were the prompt model, this route's `abstract_route.md` and `rank_one_exclusion.md`, and the complete `finite_sample_theorem.md`. No other study, scientific source, or experiment was used. Existing reports and proofs are unchanged.

**Conclusion.** This attempt does not remove the sample-count restriction for the actual full canonical dictionary. It isolates a concrete sufficient separation property, proves it for polynomial dictionaries and for a stated complex-continuation condition, and shows why a generic analytic factorization argument cannot supply it. The polynomial result is conditional; the allowed inputs do not establish that the full canonical initialized dictionary has that representation or the stated continuation property. The frozen lower moment theorem, including its unaudited Lyapunov and infinite-product dependencies, is not used as an accepted premise.

## 1. The precise reduced-model question

Let \(V\subset L^\infty(\Omega_2)\) be a finite-dimensional real space containing the constant function \(1\). For this section take the sample preactivations \(z_1,\ldots,z_m\in V\) to be independently trainable, along with \(c\in L^2(\Omega_2)\). Put

\[
H_i=\tanh z_i,\qquad f_i=\langle c,H_i\rangle,
\qquad r_i=f_i-y_i,\qquad L=\sum_i\mu_i r_i^2,
\]

where \(\mu_i>0\). Write \(\mathcal H=\operatorname{span}\{H_1,\ldots,H_m\}\).

At a local minimum, readout stationarity gives

\[
\sum_i\mu_i r_iH_i=0.                                    \tag{1}
\]

If \(r_i\ne0\), stationarity of the individually trainable \(z_i\) gives

\[
\langle c,v\operatorname{sech}^2z_i\rangle=0
\qquad(v\in V).                                          \tag{2}
\]

For any \(k\in\mathcal H^\perp\), a sufficiently small change \(c\mapsto c+tk\) preserves every prediction exactly and remains inside the original minimality ball. It is therefore another local minimum. Subtracting (2) at these two readouts gives

\[
\operatorname{sech}^2(z_i)V\subseteq\mathcal H
\qquad\text{for every }i\text{ with }r_i\ne0.              \tag{3}
\]

Every function here is in \(L^2\) because \(V\subset L^\infty\). The final inclusion follows by orthogonal decomposition, since the finite-dimensional space \(\mathcal H\) is closed. If a residual is nonzero, (1) additionally gives \(\dim\mathcal H\le m-1\). When \(m>\dim V\), the dimension of (3) alone gives no contradiction.

The following is a sufficient dictionary lemma, with no reference to targets or optimization:

> **Gate-separation property.** For every finite list \(z_1,\ldots,z_m\in V\) and every index \(i\),
> \[
> \operatorname{sech}^2(z_i)V
> \not\subseteq\operatorname{span}\{\tanh z_j:1\le j\le m\}.
> \tag{GS}
> \]

If (GS) holds, (3) proves that every reduced-model local minimum fits exactly, for arbitrary finite \(m\). This is a sufficient lemma, not claimed necessary: local-minimum information beyond (3) could conceivably prove the result even when (GS) fails.

Constant bad preactivations can also be excluded in this reduced model without (GS). If \(z_i=\kappa\) almost surely, (2) with \(v=1\) gives \(\mathbb E c=0\). Thus shifting this preactivation alone to \(\kappa+t\) preserves its prediction, which stays zero; the other predictions also remain fixed. The shifted points are local minima for small \(t\). Subtracting their readout stationarity equations gives

\[
\mu_i r_i[\tanh(\kappa+t)-\tanh\kappa]1=0.
\]

Strict monotonicity of \(\tanh\) contradicts \(r_i\ne0\). This argument uses independently available constant shifts of the individual preactivation. It is not automatically a physical perturbation of the original factorized model.

## 2. A concrete complex-continuation condition

Here is a sufficient condition for the nonconstant part of (GS). Assume the marks are represented by continuous functions of a latent variable \(X\) whose law has full support on an open set \(U\subset\mathbb R^s\). A continuous almost-sure identity then holds pointwise throughout \(U\): a nonzero value would persist on an open set of positive probability.

Fix a finite list \(z_j\in V\) and an index \(i\). Suppose one can find a real curve \(\gamma:J\to U\), where \(J\) is an open interval, and holomorphic continuations

\[
Z_j(\zeta)=z_j(\gamma(\zeta))
\]

to a connected complex domain \(D\) containing \(J\). Suppose there is \(\zeta_0\in D\) such that

\[
\cosh Z_i(\zeta_0)=0,\qquad Z_i'(\zeta_0)\ne0,             \tag{4}
\]

and for every \(j\),

\[
\cosh Z_j(\zeta_0)=0\quad\Longrightarrow\quad
Z_j'(\zeta_0)\ne0.                                      \tag{5}
\]

Then

\[
\operatorname{sech}^2z_i\notin\mathcal H.                 \tag{6}
\]

Indeed, a contrary identity in \(L^2\) holds on \(U\), hence on the real curve, and therefore extends as a meromorphic identity throughout \(D\). The zeros of \(\cosh z\) are simple: they are \(i\pi(n+1/2)\), and \(\sinh\) is nonzero there. Conditions (4)–(5) therefore imply that \(\operatorname{sech}^2Z_i\) has a double pole at \(\zeta_0\), whereas every \(\tanh Z_j\) has at most a simple pole. A finite linear combination cannot match the double pole. Since \(1\in V\), (6) implies the failure of the inclusion in (3).

This is an explicit pole-order criterion, rather than an appeal to generic rank. Proving such a continuation and pole-avoidance condition for the complete canonical dictionary would close the nonconstant-preactivation part of the reduced-model argument. Real analyticity on the real carrier, by itself, does not establish (4)–(5).

## 3. Complete conditional result for polynomial dictionaries

**Proposition.** Let \(X\) have full support on an open set \(U\subset\mathbb R^s\). Suppose \(V\subset L^\infty\) is a finite-dimensional space represented by real polynomials in \(X\), contains \(1\), and contains at least one nonconstant polynomial. Then (GS) holds. Consequently every local minimum of the independently trainable reduced model in section 1 has zero loss, for every finite sample count.

The boundedness assumption concerns the actual law of \(X\); for example \(X\) can range over a bounded open box. The polynomial extension outside that box is used only to continue an exact functional identity, not to change the carrier or trainable parameter domain.

**Proof for nonconstant \(z_i\).** Choose a real affine line \(\gamma(t)=x_0+t\xi\) with a segment in \(U\), such that the restriction \(P_i(t)=z_i(\gamma(t))\) is nonconstant. Such a line exists: a nonconstant polynomial has a nonzero first derivative at some point of any nonempty open set on which it is nonconstant, and one may choose \(\xi\) in a direction of nonzero derivative. Every other \(P_j(t)=z_j(\gamma(t))\) is also a polynomial, possibly constant.

Let \(C\subset\mathbb C\) be the union of the zeros of \(P_j'\) over the nonconstant restrictions. It is finite. For every integer \(n\), the nonconstant polynomial equation

\[
P_i(\zeta)=i\pi(n+\tfrac12)
\]

has a complex solution. Solutions corresponding to distinct right sides are distinct, so there are infinitely many such points. Choose one outside \(C\). At this point (4) holds, and (5) holds for each nonconstant \(P_j\). A constant \(P_j\) is real, so its \(\cosh\) never vanishes. The complex-continuation criterion applies with \(D=\mathbb C\), proving (6), and hence (GS) for this index.

**Proof for constant \(z_i\).** Here \(\operatorname{sech}^2z_i\) is a positive constant. Choose a nonconstant polynomial \(v\in V\) and a real affine line on which its restriction \(Q(t)\) is nonconstant, with a segment in \(U\). If the inclusion in (GS) held, restriction and analytic continuation would give, for all real \(t\),

\[
\operatorname{sech}^2(z_i)Q(t)=\sum_j\beta_j\tanh P_j(t).
\]

The right side is bounded by \(\sum_j|\beta_j|\) on the real line. The nonconstant polynomial on the left is unbounded. This contradiction establishes (GS) also in the constant case. \(\square\)

This proposition does not require the vector of polynomial marks to have full-dimensional density: its image may lie on a low-dimensional polynomial surface. It does require a polynomial representation, or a separate replacement for the continuation argument. No such representation for the complete canonical initialized dictionary is established by the authorized inputs of this attempt.

## 4. Why analyticity alone does not give the simple gate-separation argument

Even the weaker assertion \(\operatorname{sech}^2z_i\notin\mathcal H\) is false for bounded analytic correlated marks. Let \(G\) be a scalar standard Gaussian, \(X=\tanh G\), and retain

\[
b_2=(1,X,Q(X)),\qquad
Q(X)=\operatorname{arctanh}\big(\operatorname{sech}^2(X+2)\big).
\]

All three marks are bounded and real analytic on \(-1<X<1\); the extra mark is also a bounded smooth function of \(G\). Indeed \(1<X+2<3\), so the argument of \(\operatorname{arctanh}\) lies in a compact subinterval of \((0,1)\). The retained constant and continuous \(\tanh\)-Gaussian coordinate are present. Take

\[
z_1=X+2,\qquad z_2=Q(X).
\]

Then, exactly,

\[
\tanh z_2=\operatorname{sech}^2z_1.
\tag{7}
\]

Thus analyticity and a continuous coordinate do not justify separating the constant-direction gate from the original feature span. In complex continuation, the composed function on the right of (7) really does have a double pole; it is not legitimate to assume that \(\tanh\) of an arbitrary analytic preactivation has only simple poles. A zero of the composed denominator can have higher multiplicity.

This example does **not** disprove (GS): it establishes only membership of one gate direction, not the full inclusion \(\operatorname{sech}^2z_1V\subseteq\mathcal H\). It is also not a bad local minimum of the stipulated model. Its exact force is to block a blanket simple-pole assertion for arbitrary analytic correlated marks.

## 5. Higher variations do not follow from the flat readout directions alone

For a bad sample in the reduced model, stationarity gives \(\langle c,v\phi'(z_i)\rangle=0\). Its second loss variation along \(z_i+tv\) is therefore

\[
\frac{d^2L}{dt^2}\bigg|_{t=0}
=2\mu_i r_i\langle c,v^2\phi''(z_i)\rangle\ge0.
\tag{8}
\]

At the prediction-preserving readouts \(c+\varepsilon k\), \(k\in\mathcal H^\perp\), the same inequality becomes

\[
r_i\langle c+\varepsilon k,v^2\phi''(z_i)\rangle\ge0
\quad\text{for all sufficiently small }\varepsilon.
\]

If the value at \(\varepsilon=0\) is strictly positive, this inequality allows a nonzero coefficient of \(\varepsilon\). It does not force \(v^2\phi''(z_i)\in\mathcal H\). Thus the first-derivative inclusion (3) cannot simply be iterated to all higher gates. A valid iteration would need an additional exact flat path or a proof that the relevant lower-order curvature vanishes.

The following complete example shows the logical obstruction even with a common bounded analytic feature map, independently trainable sample parameters, and an unrestricted linear readout. It is deliberately stated outside the special \(\tanh(b\cdot\theta)\) family.

Let \(a=1/2\), \(s=\tanh\theta\), and define the bounded analytic map \(h:\mathbb R\to\mathbb R^2\) by

\[
h(\theta)=\big(1-s(s^2-a^2)^2,\ (s^2-a^2)^3\big).
\]

For independent \(\theta_1,\theta_2\) and \(c=(c_0,c_1)\), set \(f_i=c\cdot h(\theta_i)\) and use targets \((0,2)\). At

\[
\theta_1=-\operatorname{arctanh}a,\qquad
\theta_2=\operatorname{arctanh}a,\qquad c=(1,0),
\tag{9}
\]

both feature vectors equal \((1,0)\), both predictions equal \(1\), and the loss is \(2\).

For any nearby parameter point, writing \(s_i=\tanh\theta_i\),

\[
f_i-c_0=(s_i^2-a^2)^2
\big[-c_0s_i+c_1(s_i^2-a^2)\big].                         \tag{10}
\]

At the base point the bracket for sample 1 equals \(a>0\), while the bracket for sample 2 equals \(-a<0\). By continuity these signs persist in a product neighborhood of (9). Equation (10) gives \(f_1\ge c_0\ge f_2\) throughout that neighborhood. If \(m_0=(f_1+f_2)/2\) and \(d_0=(f_1-f_2)/2\ge0\), then

\[
f_1^2+(f_2-2)^2
=2(m_0-1)^2+2(d_0+1)^2\ge2.
\]

Therefore (9) is a positive-loss local minimum. The second feature coordinate vanishes to order three at both sample parameters. Changing \(c_1\) leaves the base predictions exactly unchanged; its higher-order effect does not overcome the protected quadratic sign in (10).

Nearby full feature rank is also available: keep \(s_2=a\) and change \(s_1\) slightly so that \(s_1^2\ne a^2\). Then the second coordinate of \(h(\theta_1)\) is nonzero, whereas \(h(\theta_2)=(1,0)\), so the two feature vectors are linearly independent and the targets can be interpolated by some readout. This does not destroy the local minimum because that interpolating readout need not stay close to \((1,0)\).

This is a counterexample to the **general analytic-feature argument**, not to the original tanh-mark architecture. It establishes that bounded analyticity, independently trainable sample parameters, flat null-readout directions, and nearby interpolation points collectively still do not imply the required landscape theorem. Specific structure of \(\tanh(b\cdot\theta)\) must be used.

## 6. Transfer back to the finite factorization

There are two logically separate transfer issues.

First, in an abstract reduced factorization with genuinely free \(a_i\in\mathbb R^{q_1}\), a full matrix \(M:\mathbb R^{q_1}\to\mathbb R^{q_2}\), and \(q_1\ge q_2\), one can prove \(r_id_i=0\) for arbitrary \(m\), with

\[
d_i=\mathbb E[b_2c\phi'(b_2^TMa_i)].
\]

If \(\ker M\ne\{0\}\), choose \(v\ne0\) in that kernel and change one column \(a_i\mapsto a_i+tv\). This preserves every prediction exactly. Matrix stationarity at the two local minima differs by

\[
2t\mu_i r_id_iv^T=0,
\]

which gives \(r_id_i=0\). If \(\ker M=\{0\}\), the inequality \(q_1\ge q_2\) forces \(q_1=q_2\) and \(M\) invertible; independent moment-column stationarity \(r_iM^Td_i=0\) again gives \(r_id_i=0\). Applying this conclusion after each null-readout perturbation gives the full gate inclusion (3). Hence (GS), if established for the upper dictionary, excludes bad minima of this free-moment factorization without a sample bound.

This argument is complete for the stated reduced variables. In the actual model, the \(a_i\) come jointly from one physical \(L^2\) field. The exact independent column changes in the preceding paragraph have not been established by the accepted inputs for the unrestricted regime. The frozen moment-interior/local-lifting theorem would address this, but its external dependencies have not been independently audited and it is not imported here as proved. Therefore the reduced-factorization result alone is not a physical landscape theorem.

There is one direct physical special case. If the effective matrix from \(B_1\) onto the effective upper coefficient space \(B_2\) is surjective, the small-set condition (6) of `finite_sample_theorem.md` already implies \(r_id_i=0\): it says \(r_iM^Td_i\) annihilates \(B_1\), while \(d_i\in B_2\), and surjectivity makes the effective transpose injective. Readout-null changes keep the matrix fixed and give (3). Thus (GS) would settle this surjective physical case for arbitrary sample count without the lower moment theorem. The general nonsurjective case still needs a valid physical argument or an independently audited local lift.

Second, none of these factorization steps proves (GS) for the complete canonical mark space. Section 3 verifies it for polynomial spaces with latent open support. Section 4 shows why the same pole sentence cannot be substituted for a verification when arbitrary analytic initialized words are retained. These are independent gaps: resolving the lower transfer does not resolve upper gate separation, and resolving gate separation does not automatically supply admissible physical moment perturbations.

## 7. End of this bounded attempt

| Statement | Status |
|---|---|
| Necessary full-gate inclusion in the independent-preactivation model | Proved here |
| Constant bad preactivations excluded in that model | Proved here |
| Concrete complex-continuation condition excludes nonconstant bad preactivations | Proved here |
| Polynomial dictionaries with latent open support satisfy (GS) | Proved here, conditional dictionary class |
| Free-moment factorization with \(q_1\ge q_2\) forces full-gate inclusion for every finite \(m\) | Proved here |
| General bounded analyticity plus flat readout paths proves no bad minima | Falsified as a generic inference by section 5 |
| Arbitrary analytic marks make the constant-direction gate independent of the output features | Falsified by section 4 |
| Full canonical dictionary satisfies (GS), or an adequate weaker local-minimum lemma | Open in this attempt |
| Unrestricted physical local-minimum theorem for the original fixed dictionary | Open in this attempt |

The precise next analytical obligation is a dictionary-specific gate-separation proof (or a stronger use of the local-minimum equations), together with a valid physical transfer in the nonsurjective factorization case. No density-of-full-rank argument is used to claim either obligation is solved.
