# Independent isolated adversarial audit

Candidate: `/tmp/l3-two-sample-proof-DLuelg/CONVEX_GATE_CURVATURE_ACTION.md`

Exact candidate SHA256:

```text
f83192ffc92fa36aeabe4cd6042b3c5291cd7180a78064dbc8d35bf1682b0ce0
```

The candidate was read in full. Line references below refer to that exact file. This audit used only the candidate and direct symbolic reasoning: no other project files, history, reviews, mathematical references, external sources, experiments, or other agents. The candidate was not edited.

## Verdict and severity

**Conditional pass.** The shifted-softplus inequalities, bounded-class obstruction, first-field metric including the antiparallel endpoint, rank-one modal identity, weighted integrated top-curvature estimate, and middle-layer coefficients are correct. The initialization Gram-positivity and individual-feature nonaffinity arguments are also correct under the stated Gaussian initialization and sample-symmetry premises, with the centering clarification discussed below.

**Required mathematical corrections: none found for the stated conditional result.** In particular, no counterexample was found to (11) under the candidate's existing-path, energy, and symmetry hypotheses. This verdict does not establish that those hypotheses are realized globally, or that a population path is identified with a finite-width limit.

The optional findings concern the exact scope of symmetry, explicit state-space and Gaussian-mean conventions, the distinction between the exact middle product and its auxiliary upper bound, historical-source weights, and undefined contextual examples. They should not be promoted into failures of the proved conditional estimate. Conversely, the stronger claims ruled out below are not consequences of this pass.

## 1. Scalar activation calculations: pass

For this section only write (p=\phi'), (c=\phi''). From (1),

\[
p(z)=\frac{\sigma(z)}{10},\qquad
c(z)=\frac{\sigma(z)(1-\sigma(z))}{10}
     =p(z)-10p(z)^2.
\]

At every finite real argument, (0<\sigma<1). Thus (0<p<1/10), (0<c\leq1/40), and (\phi>1); the weaker displayed floor (\phi\geq1) is valid. The curvature maximum occurs at (z=0). The activation is strictly increasing and strictly convex. It is unbounded above and has at most linear growth, for example

\[
1<\phi(z)\leq1+\frac{\log 2+|z|}{10}.
\]

An exact factorization verifies the difference estimate without any restriction on the attained preactivations:

\[
c(x)-c(y)
 =[p(x)-p(y)]\{1-10[p(x)+p(y)]\}.
\]

Since (p(x)+p(y)\in(0,1/5)), the factor in braces has absolute value at most one. This proves (3), including (x=y).

Also (c=(1-\sigma)p\leq p). For (x<y),

\[
0<p(y)-p(x)=\int_x^y c(z)\,dz
 \leq\int_x^y p(z)\,dz=\phi(y)-\phi(x).
\]

Interchanging the endpoints proves (4) in every ordering. All factors (1/10), (10), and (1/40) are correct. No compact-range argument or configuration-dependent parameter is hidden here.

## 2. Impossibility in the specified bounded class: pass

The proof at lines 40–63 uses exactly the stated class: bounded, nondecreasing, nonconstant (C^2(\mathbb R)) activation with bounded derivative. It does not assume in advance that the second derivative is bounded.

Here is the complete chain of implications, including the potentially delicate endpoint step.

1. Monotonicity and differentiability imply (p=\psi'\geq0). Bounded monotonicity gives finite endpoint limits, and the fundamental theorem of calculus followed by exhaustion of the real line gives
   \(\int_{\mathbb R}p=\psi(+\infty)-\psi(-\infty)<\infty\).
2. If (5) held with finite (C\geq0), fixing a finite (y\) would give
   \( |p'(x)|\leq |p'(y)|+C(\|p\|_\infty+|p(y)|)\).
   Hence (p\) would be globally Lipschitz and uniformly continuous.
3. If (p\) failed to tend to zero at either end, uniform continuity would provide intervals of a common positive radius on which (p\geq\epsilon/2\), centered at a sequence escaping that end. A disjoint subsequence would contradict integrability. Thus both tails tend to zero.
4. Nonconstancy gives (p(x_*)>0\) somewhere. Both tails eventually lie below, say, (p(x_*)/2\), so continuity on a remaining compact interval supplies a positive attained global maximum (M=p(x_0)\). Since (p\in C^1\), (p'(x_0)=0\).
5. Therefore \(|p'(x)|\leq C|p(x)-M|\). On the right of (x_0\), let
   \(F(x)=\int_{x_0}^x|p(u)-M|\,du\).
   Then \(F\geq0\), \(F(x_0)=0\), and \(F'\leq CF\), so \(e^{-C(x-x_0)}F\) is nonincreasing from zero and must vanish. Applying the same argument to (t\mapsto p(x_0-t)\) proves constancy on the left as well.
6. The resulting positive constant (p\equiv M\) contradicts its finite integral.

The (C=0\) case is covered. A negative proposed constant cannot rescue (5): for unequal values of (p\), its right side would be negative; constant (p\) is already inconsistent with the bounded, nonconstant activation. There is no missing strict-monotonicity, analyticity, or bounded-curvature hypothesis.

The conclusion concerns domination (5) only. The candidate correctly does not turn it into a nonexistence assertion for gradient flows.

The named arctan and sech-gate illustrations are less self-contained than this theorem; see optional finding O5. Their names are not needed anywhere in the accepted proof.

## 3. State spaces, reverse fields, raw metric, and energy: pass

### State-space check

In the stated (L^2\) field/readout setup, start with (Z^{(1)}_a\in L^2(\Omega_1)\) and (W^{(4)}\in L^2(\Omega_3)\). Linear growth sends each first field to (H^{(1)}_a\in L^2\). Boundedness of (W^{(2)}\), then of (W^{(3)}\), propagates this property through both forward layers. The scalar output exists by Cauchy–Schwarz.

Multiplication by (\phi'\) is bounded on each (L^2\) space with multiplier norm at most (1/10\). A bounded operator has a bounded adjoint. These facts propagate (L^2\) membership backwards through every displayed (q\) and (\delta\). The same argument with (\|\phi''\|_\infty\leq1/40\) gives (M^{(3)}_\pm\in L^2\). No independence across neuron populations is needed.

This verifies membership, not differentiability of the population vector field or global existence. The candidate explicitly makes the chain rule and energy identity premises. Making the initial memberships explicit would improve the wording at lines 97–98; see O2.

### Raw first-field metric and the endpoint

For a normalized two-row input map (A\) with (AA^T=C\), a first-field velocity (v\) is induced by a raw input-weight velocity (h\) satisfying (Ah=v\). When \(|\rho|<1\), the minimum-norm representative is (h=A^TC^{-1}v\), and

\[
\|h\|^2=v^TC^{-1}v
 =\frac{v_1^2-2\rho v_1v_2+v_2^2}{1-\rho^2}.
\]

This is the induced metric on the represented sample fields. Invisible weight directions add a nonnegative norm in a full weight description; the feature gradient lies in the represented input span. There is no missing sample factor (1/2\) in this field metric. The (1/2\) belongs in the objective (g\) and consequently in its gradient.

With (v_+=(v_1+v_2)/2\) and (v_-=(v_1-v_2)/2\), the same expression is

\[
\frac{2v_+^2}{1+\rho}+\frac{2v_-^2}{1-\rho}.
\]

At \(\rho=-1\), admissible velocities are exactly \((v,-v)\). Their raw squared norm is (v^2\), as stated. Equivalently, on this range

\[
C^+=\frac14\begin{pmatrix}1&-1\\-1&1\end{pmatrix},
\qquad (v,-v)^TC^+(v,-v)=v^2.
\]

One must not use an ordinary inverse at that endpoint, admit arbitrary off-range field velocities, or replace the one-field norm by (2v^2\).

The first-field differential of (g\) has sample coefficient \((\delta^{(1)}_1,-\delta^{(1)}_2)/2\). Its Riesz representative is precisely the first-field equation in (6). In modal form its velocities are

\[
(Z^{(1)})'_+=\frac{1+\rho}{2}\delta^{(1)}_-,\qquad
(Z^{(1)})'_- =\frac{1-\rho}{2}\delta^{(1)}_+.
\]

The corresponding raw energy is

\[
\frac{1+\rho}{2}\|\delta^{(1)}_-\|_2^2
 +\frac{1-\rho}{2}\|\delta^{(1)}_+\|_2^2.
\]

At \(\rho=-1\), this reduces to \(Z'=\delta^{(1)}_+=(\delta^{(1)}_1+\delta^{(1)}_2)/2\) and raw energy \(\|\delta^{(1)}_+\|_2^2\). Thus (6) and the singular-endpoint metric agree exactly.

### Hidden matrices, readout, and energy

For the stated rank-one convention, ( (u\otimes v)h=u\mathbb E[vh]\). On a uniform source population of size (n\), this is represented in sample-value coordinates by (uv^T/n\). Here (n\) is the source width. For unequal source and target widths, the operator Hilbert–Schmidt norm is computed using the respective probability-normalized inner products, not an unadjusted coordinate Frobenius norm.

The hidden-matrix gradient of (g\) is \(\frac12\sum_a y_a\delta^{(\ell)}_a\otimes H^{(\ell-1)}_a\). The (L^2\) readout gradient is (V^{(3)}\). These agree with (6); no residual multiplier is present or needed for feature time.

Under the assumed chain rule, these gradients yield (g'=\|\theta'\|_{\rm raw}^2\). Integrating from (g(0)=0\) gives (7), including (0\leq g(S)\leq1\). The upper bound is a hypothesis along the specified interval, not a proved consequence of the feature-gradient equations alone.

## 4. Modal rank-one identity and top curvature action: pass

For real (L^2\) spaces,

\[
\langle u\otimes v,\widetilde u\otimes\widetilde v\rangle_{\rm HS}
 =\langle u,\widetilde u\rangle\langle v,\widetilde v\rangle.
\]

Expanding the half-sums and half-differences gives

\[
\tfrac12(\delta_1\otimes H_1-\delta_2\otimes H_2)
 =\delta_-\otimes U+\delta_+\otimes V.
\]

No factor two is missing. Its squared norm has exactly the two terms in (9), plus

\[
2\mathbb E_\ell[\delta_-\delta_+]
  \mathbb E_{\ell-1}[UV].
\]

Since \(\mathbb E_j[UV]=(\mathbb E_jH_1^2-\mathbb E_jH_2^2)/4\), (8) removes the cross term for hidden layers \(\ell=2,3\). This is an identity of tensor products between the original populations; it is not a probabilistic independence factorization. The warning about arbitrary finite realizations is correct. Symmetry at layer three is unnecessary and is not supplied by (8); see O1.

At the top layer, write (w=W^{(4)}\), (p_a=\phi'(Z^{(3)}_a)>0\), and (c_a=\phi''(Z^{(3)}_a)>0\). Then

\[
|M_-|=\frac{|w|}{2}|c_1-c_2|
 \leq\frac{|w|}{2}|p_1-p_2|=|\delta_-|,
\]

and

\[
|M_+|=\frac{|w|}{2}(c_1+c_2)
 \leq\frac{|w|}{2}(p_1+p_2)=|\delta_+|.
\]

These hold for either sign of (w\), and when (w=0\). The common readout and the positivity of the gates are used correctly.

Consequently, at each time where the assumed gradient equation holds,

\[
\begin{aligned}
\|M^{(3)}_-\|_2^2+\kappa_2\|M^{(3)}_+\|_2^2
&\leq\|\delta^{(3)}_-\|_2^2
       +\kappa_2\|\delta^{(3)}_+\|_2^2\\
&\leq\|U^{(2)}\|_2^2\|\delta^{(3)}_-\|_2^2
       +\kappa_2\|\delta^{(3)}_+\|_2^2\\
&=\|(W^{(3)})'\|_{\rm HS}^2
 \leq\|\theta'\|_{\rm raw}^2.
\end{aligned}
\]

The second inequality uses the probability normalization and (U^{(2)}\geq1\). Integrating proves (11) exactly, with its time-dependent weight \(\kappa_2(s)\). No lower bound on that weight, upper feature bound, time-horizon factor, or (1/(1-\rho)\) constant was inserted.

The estimate's numerical constant is uniform in (S\) and \(\rho<1\), conditional on all premises holding on the interval under consideration. It asserts neither existence on a common interval for all correlations nor a nondegenerate plus-mode estimate as the weight vanishes.

As an elementary check on the importance of retaining the weight, the abstract choices \(\kappa=\epsilon^2\) and (m=1/\epsilon\) on a unit time interval give \(\int\kappa m^2=1\) but \(\int m^2=\epsilon^{-2}\). This is a counterexample to extracting an unweighted conclusion from a weighted inequality alone, not a constructed counterexample trajectory. The candidate does not make that extraction.

## 5. Exact middle product and the remaining moment issue: pass with clarification

Let (p_a=\phi'(Z^{(2)}_a)\) in this paragraph. Since (r_a=1-10p_a\),

\[
\frac{r_1\delta_1-r_2\delta_2}{2}
 =r_+\delta_-+r_-\delta_+,
\qquad r_-=-5(p_1-p_2).
\]

Using (4) and (H_1-H_2=2V\) gives

\[
|r_-|\leq5|H_1-H_2|=10|V|.
\]

Thus every coefficient and half-mode factor in (12) is correct. The actual upper bound that produces the problematic auxiliary product is

\[
|r_+\delta_-+r_-\delta_+|
 \leq|\delta_-|+10|V^{(2)}\delta^{(2)}_+|.
\]

The exact second summand is (r_-\delta_+\), not (V\delta_+\) with coefficient one. Where (V\ne0\), it can also be written

\[
r_-\delta_+
 =-10\frac{p_1-p_2}{H_1-H_2}\,V\delta_+,
\]

with the quotient in ((0,1]\); where (V=0\), the summand is zero. There is no permitted replacement of (V^{(2)}\) by the previous-layer contrast (V^{(1)}\).

A direct symbolic cancellation example checks why the top difference domination does not transfer through independent sample backpropagated factors. Take

\[
Z^{(2)}_1=-\log3,\quad Z^{(2)}_2=\log3,
\quad q^{(2)}_1=3,\quad q^{(2)}_2=1.
\]

Then (p_1=1/40\), (p_2=3/40\), and (\delta_1=\delta_2=3/40\), so (\delta_-=0\). But (r_1=3/4\), (r_2=1/4\), and the middle curvature difference is (3/160>0\). This is a pointwise counterexample to a scalar inequality allowing unrestricted sample-dependent (q_1,q_2\). It is not asserted to be a full trajectory satisfying all the candidate's premises. It shows why the common-multiplier proof of (10) cannot simply be copied.

The warning that two separate second moments cannot control an (L^2\) product is correct. On the probability space ((0,1)\), let (X(t)=Y(t)=t^{-1/3}\). Both second moments equal (3\), whereas

\[
\mathbb E|XY|^2=\int_0^1t^{-4/3}\,dt=\infty.
\]

This directly refutes the inference from (X,Y\in L^2\) to (XY\in L^2\), without any experiment or claim to a network realization. The action bound at layer two supplies \(\kappa_1\|\delta^{(2)}_+\|_2^2\), which is not the mixed moment \(\mathbb E_2[(V^{(2)})^2(\delta^{(2)}_+)^2]\).

There is an important limitation on the negative statement: (0<r_+<1\) and (|r_-|<1/2\). Therefore the **exact** middle curvature difference is already in (L^2\) at every time under the stated field memberships, and

\[
\|r_+\delta_-+r_-\delta_+\|_2
 \leq\|\delta_-\|_2+\tfrac12\|\delta_+\|_2.
\]

What is not provided is the desired uniformly controlled integrated action/response bound for that unweighted plus term or for the correlated auxiliary product. The candidate's literal claim about (V\delta_+\) is correct, but it should not be read as failure of (L^2\) membership of the exact curvature field. This motivates O3.

The historical-source warning is also justified. For example, a bilinear historical pairing of the plus mode would naturally require the complementary weighted moment

\[
\left|\int_0^S\mathbb E_3[M^{(3)}_+ B]\,ds\right|
\leq
\left(\int_0^S\kappa_2\|M^{(3)}_+\|_2^2ds\right)^{1/2}
\left(\int_0^S\frac{\|B\|_2^2}{\kappa_2}\,ds\right)^{1/2},
\]

where the second expression must be meaningful and finite, including treatment of zero weights. For an (L^2\) norm of a product, the requirement is instead a mixed moment such as \(\int\mathbb E[M^2B^2]\). Equation (11) alone supplies neither kind of missing information. No historical-response or Hessian conclusion follows from it.

## 6. Initialization, Gram positivity, and nonaffinity: pass

### Nonaffinity of an individual feature

If (G\) is any nondegenerate scalar Gaussian and \(\phi(G)=aG+b\) almost surely, continuity and the strictly positive Gaussian density imply \(\phi(z)=az+b\) at every real (z\). Indeed, a point of nonzero difference would have an open neighborhood of nonzero difference and positive probability. This contradicts \(\phi''>0\). The argument applies to noncentered as well as centered nondegenerate Gaussians.

### Nonsingular first Gaussian pair

For \(|\rho|<1\), the input Gaussian pair has a positive density on \(\mathbb R^2\). If the uncentered feature Gram were singular, some nonzero coefficient vector (a\) would have

\[
\mathbb E[a_1\phi(G_1)+a_2\phi(G_2)]^2=0.
\]

Continuity and full support would force the expression in brackets to vanish everywhere on \(\mathbb R^2\). Holding one coordinate fixed and varying the other forces (a_1=0\), then (a_2=0\), because \(\phi\) is nonconstant. This is a contradiction. No centering or centered-covariance substitution for the feature Gram is used in this argument.

### Antiparallel first Gaussian pair

For the stipulated pair \((G,-G)\),

\[
D(G):=\phi(G)-\phi(-G)=G/10,
\qquad
T(G):=\phi(G)+\phi(-G)
 =2+\frac15\log(2\cosh(G/2))\geq2.
\]

For centered (G\) of variance one, the pair of features is exchangeable; its Gram has the form \(\bigl(\begin{smallmatrix}a&b\\b&a\end{smallmatrix}\bigr)\), and its eigenvalues are exactly

\[
\lambda_+=a+b=\tfrac12\mathbb ET^2\geq2,
\qquad
\lambda_-=a-b=\tfrac12\mathbb ED^2=\frac1{200}>0.
\]

The normalization is correct: \(\kappa_1=\mathbb E(D/2)^2=1/400\), rather than (1/200\). All these moments are finite by linear growth.

The candidate does not explicitly state the Gaussian means. If (8) is retained at initialization, its antiparallel instance supplies the missing centering implication: for (G=m+X\), (X\sim N(0,1)\), the map \(A(m)=\mathbb E\phi(m+X)^2\) is strictly increasing. Since \(-G\) has the law \(-m+X\), equality of the feature second moments gives \(A(m)=A(-m)\), hence (m=0\). Thus exchangeability is valid under the retained hypotheses. Covariance (C\) alone would not justify it for an arbitrary noncentered Gaussian. This is an optional explicitness issue, not a counterexample satisfying (8); see O4.

Strict positivity of the antiparallel Gram also has a proof that avoids exchangeability entirely. Any almost-sure zero combination extends to all real (z\); writing it in terms of the positive even function (T(z)\) and the nonzero odd function (D(z)\), evaluation at (z\) and \(-z\) forces both coefficients to vanish.

### Recursive Gaussian law and readout label modes

A Gaussian pair with covariance equal to the finite, positive-definite preceding uncentered feature Gram is nonsingular. The preceding full-support argument then proves the next feature Gram positive definite. Iterating twice verifies the claims at layers two and three, provided the stated recursive Gaussian initialization is imposed. Each marginal variance is positive, so the individual-feature nonaffinity argument also applies at each layer.

With the prescribed (L^2\) readout metric, the initial readout kernel is (K_{ab}=\mathbb E_3[H^{(3)}_aH^{(3)}_b]\). Positive definiteness gives (y^TKy>0\) for both (y=(1,1)\) and (y=(1,-1)\), indeed for every nonzero vector. For the candidate's half-difference objective, the readout contribution is (y^TKy/4=\kappa_3>0\). With zero initial readout, all the hidden reverse fields vanish initially; along the assumed regular path, (g'(0)=\kappa_3\).

An important adversarial distinction is that **the first antiparallel contrast itself is affine**, namely (G/10\). The proved nonaffinity is that of each individual activated Gaussian, not that of every sample linear combination or every label mode. Positive Gram definiteness does not contradict this affine contrast. The candidate displays the identity and does not explicitly claim nonaffinity of every contrast, so this is not a required correction.

Initial kernel positivity proves neither a uniform lower eigenvalue bound along the path nor later all-layer motion, later nonaffine laws, or every-time nonfreezing. The candidate expressly leaves these matters open.

## 7. Scope and claim discipline

The restrictions at lines 3–7, 100–126, 168–172, 183–190, and 218–228 are consistent with the proof actually supplied.

- The existing path, energy identity, upper bound on (g\), and time-dependent sample symmetry are hypotheses, not derived global facts.
- The finite-width rank-one normalization at lines 108–109 is an algebraic coordinate statement. It is not an identification of empirical dynamics with the population path.
- There is no physical-time residual cancellation, finite-width scalar clock, joint empirical convergence proof, or reference-cut removal in the argument.
- Strict convexity and initial Gaussian nonaffinity are not used to assert later nonfreezing.
- The weighted top-curvature estimate is not promoted to a full historical-response estimate, a Hessian sign, or a complete two-sample theorem.

The references to an established short-response proof and to a desired two-sample theorem do not define either object in this file. Under the required isolation, claims about the contents of that earlier proof cannot be independently verified. The loss of a uniform feature ceiling is directly verified, and the candidate does not import the unnamed proof's constants. The final statement about not giving a counterexample can safely be read as saying that the documented gaps do not themselves construct a counterexample; it is not evidence proving an unstated target theorem.

## 8. Optional findings and concrete edits

### O1 — State the symmetry index range explicitly

**Location:** lines 134–142.

Change “Relation (8) gives (\mathbb E_\ell[U^{(\ell)}V^{(\ell)}]=0\)” to “For (\ell=1,2\), relation (8) gives ...”, and optionally repeat “(\ell=2,3\)” beside (9). Equation (8) supplies no third-layer orthogonality. Only the supplied first- and second-layer instances are needed for the proof, so this is a quantifier clarification rather than a defect in (9) or (11).

### O2 — Make the (L^2\) starting state explicit

**Location:** lines 72–98 and 100–113.

Explicitly state (Z^{(1)}_a(s)\in L^2(\Omega_1)\), (W^{(4)}(s)\in L^2(\Omega_3)\), and that the existing regular path has the time regularity needed for the stipulated integrated chain rule. These are the natural domains already indicated by the field/readout metrics and the regular-path premise. Linear growth cannot establish (L^2\) membership without an (L^2\) input to begin with. This clarification should not be replaced by a claim that the defined vector field automatically produces such a path.

### O3 — Separate the exact middle field from its auxiliary product bound

**Location:** lines 174–190.

A precise replacement for the product warning would be: “The exact remainder is (r_-\delta^{(2)}_+\), with (|r_-|\leq\min\{1/2,10|V^{(2)}|\}\). It belongs to (L^2\) under the assumed field memberships, but the desired action estimate is not obtained: the bound involving (V^{(2)}\delta^{(2)}_+\) requires a mixed moment unavailable from the two separate second moments.” This preserves the valid obstruction without implying that the exact curvature field lacks (L^2\) membership.

### O4 — Spell out the Gaussian-mean convention and the nonaffinity target

**Location:** lines 199–218.

Writing (G\sim N(0,1)\) and specifying centered recursive Gaussian pairs would make the intended initialization immediately explicit. Alternatively, retain the existing hypotheses and explain the inference from (8) at the antiparallel endpoint. Do not infer exchangeability from covariance alone. “Each individual activated Gaussian is nonaffine” would also make clear that the explicitly affine antiparallel contrast is allowed.

### O5 — Define the named illustrative activations or make their property conditional

**Location:** lines 65–67.

No formula for “shifted sech-gate” appears in the permitted source, so its exact named-instance assertion cannot be checked independently. State the activation/gate formula, or state the illustration conditionally: “For an even gate with odd derivative nonzero at (x\ne0\), the pair (x,-x\) violates (3).” The general bounded-class theorem is fully proved without either named example. Likewise, claims about the unnamed previous proof remain contextual and unverified in this isolated review.

### O6 — Specify which historical quantity is missing

**Location:** lines 187–190.

For a bilinear spacetime pairing, specify the second moment of the source, with the inverse contrast weight for the plus mode. For an (L^2\) product, specify a mixed moment or sufficient stronger bounds; an arbitrary additional moment of the sensitivity alone need not suffice when curvature is controlled only in (L^2\). The current text makes no false sufficiency claim, but “an additional moment” leaves this distinction implicit.

## Final disposition

The candidate proves a valid conditional, weighted top-curvature-action estimate for the fixed shifted-softplus activation and correctly identifies the limits of that estimate. Its bounded-class obstruction and initialization statements survive the adversarial checks above. No required correction to the central mathematics was found. The optional edits improve literal scope and self-containment; none establishes global existence, finite-width identification, control of the remaining response terms, or a complete theorem.
