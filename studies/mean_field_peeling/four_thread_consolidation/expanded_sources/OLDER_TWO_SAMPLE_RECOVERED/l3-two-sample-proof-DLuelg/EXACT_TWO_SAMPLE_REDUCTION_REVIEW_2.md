# Adversarial review of the exact two-sample reduction

**Verdict:** The note passes as a scoped, conditional reduction and route-obstruction lemma. I found no substantive error in equations (1)–(15), the singular Gaussian estimate, or either deterministic feature-time bound. The population symmetry and population differential identities remain conditional on the premises the note explicitly lists. Nothing audited here establishes the remaining population construction, uniqueness, actual-response, or full-limit claims.

## Audit provenance and scope

- Sole mathematical input: `/tmp/l3-two-sample-proof-DLuelg/EXACT_TWO_SAMPLE_REDUCTION.md`.
- Source SHA-256: `432f98ff185c797901a81f83c72e4217395d0100f0804b0e609b98db83182e60`.
- Source length: 376 lines. The entire note was read and checked, including its opening scope and remaining obligations.
- I personally read the complete mandatory procedural skill `/etc/codex/skills/solve-math-rigorously/SKILL.md` and applied its requirements to track assumptions, expose nontrivial steps, check singular cases, and distinguish proved claims from conditional ones.
- No other project document, earlier report or proof, contract, or task history was consulted. No agents, experiments, numerical checks, or external mathematical sources were used. The calculations below are direct derivations from the note. File inspection and hashing were the only diagnostic operations.

The review first checks the metric and finite identities, then the two different symmetry arguments and the clock, then the chart obstruction, initialization estimate, and deterministic bounds. It does not infer a global theorem from these ingredients.

## 1. Raw scaling, metric gradients, and kernels

Source lines 11–79 are internally consistent. In particular, the readout is the rescaled variable appearing in both the output normalization and the metric; no further change of variables is implicit in the calculation.

Write the raw parameter metric as

\[
\langle U,V\rangle_G
=\frac d n\langle U_1,V_1\rangle_F
+\langle U_2,V_2\rangle_F
+\langle U_3,V_3\rangle_F
+\frac1n\langle U_4,V_4\rangle.
\]

The backward fields omit the output factor \(1/n\). Applying the chain rule to \(f_a=(W^{(4)})^Th_a^{(3)}/n\) therefore gives precisely the four coordinate differentials on lines 41–44. In ordinary Euclidean coordinates their gradients are

\[
\frac{\delta_a^{(1)}x_a^T}{n},\qquad
\frac{\delta_a^{(2)}(h_a^{(1)})^T}{n},\qquad
\frac{\delta_a^{(3)}(h_a^{(2)})^T}{n},\qquad
\frac{h_a^{(3)}}n.
\]

Inverting the metric multipliers \(d/n,1,1,1/n\) produces the metric gradients stated in the note:

\[
\nabla_G f_a=
\left(
\frac{\delta_a^{(1)}x_a^T}{d},
\frac{\delta_a^{(2)}(h_a^{(1)})^T}{n},
\frac{\delta_a^{(3)}(h_a^{(2)})^T}{n},
h_a^{(3)}
\right).
\]

Thus \(\nabla_G L=2\sum_a(f_a-y_a)\nabla_G f_a\). Multiplying the first block of the exact parameter GD update by \(x_b\) gives

\[
z_{b,+}^{(1)}-z_b^{(1)}
=-2\eta_n\sum_a(f_a-y_a)\delta_a^{(1)}
\frac{x_a^Tx_b}{d},
\]

which is (1), with \(\eta_n=n^{-2}\). This is exact because the first preactivation is linear in the first weight matrix. It is not an assertion that the entire nonlinear prediction has an exact first-order discrete update.

For the first kernel block, direct pairing gives

\[
\frac d n\left\langle
\frac{\delta_a^{(1)}x_a^T}{d},
\frac{\delta_b^{(1)}x_b^T}{d}
\right\rangle_F
=C_{ab}\frac{(\delta_a^{(1)})^T\delta_b^{(1)}}n.
\]

For either middle block the Frobenius pairing is

\[
\frac{(\delta_a^{(\ell)})^T\delta_b^{(\ell)}}n
\frac{(h_a^{(\ell-1)})^Th_b^{(\ell-1)}}n.
\]

For the readout block it is \((h_a^{(3)})^Th_b^{(3)}/n\). These establish every factor in (2). For any \(c\in\mathbb R^2\), each block satisfies

\[
c^TK^{(\ell)}c
=\left\|\sum_a c_a\nabla_G^{(\ell)}f_a\right\|_G^2\geq0.
\]

This also proves positivity when \(C\) is singular or has negative off-diagonal entries; entrywise positivity is unnecessary.

Along the finite metric gradient flow, the chain rule now yields

\[
\dot f_a=-2\sum_bK_{ab}(f_b-y_b),\qquad
\dot L=-4(f-y)^TK(f-y).
\]

The physical time convention \(t=k\eta_n\) is consequently consistent with (3). Differentiability of \(\phi\) suffices for these chain-rule identities along an existing differentiable trajectory. If \(\phi\in C^2\), the finite loss is \(C^2\), so its metric gradient is \(C^1\) and locally Lipschitz. This supplies local existence and uniqueness in finite dimensions, with conclusions restricted to the maximal existence interval unless further bounds are proved. The note makes this restriction.

The population qualification at lines 77–79 is essential and correctly retained: a formal finite gradient calculation alone does not construct a population Hilbert-space vector field or justify differentiation there.

## 2. Exact first-layer geometry, including the singular case

Source lines 81–91 are correct. Every update row is a linear combination of \(x_1^T,x_2^T\), so its orthogonal component is fixed under both GD and GF.

For \(-1<\rho<1\), let \(X=[x_1\ x_2]\) and let a row variation have sample values \(v=(v_1,v_2)\). The unique row in the input span with those values is

\[
w=v(X^TX)^{-1}X^T,
\qquad
\|w\|^2=v(X^TX)^{-1}v^T
=\frac1d vC^{-1}v^T.
\]

Multiplication by \(d/n\) and summation over rows gives (4). This is the induced metric on the sample coordinates, not the ordinary Euclidean metric on two independent sample fields. In particular, replacing \(C^{-1}\) by the identity at correlated inputs would be incorrect; the note does not do so.

At \(\rho=-1\), equal input norms give \(x_2=-x_1\). The admissible variation is constrained by \(v_2=-v_1\). For one row it is \(w=v_1x_1^T/d\), with squared norm \(v_1^2/d\), so the metric becomes \(\|v_1\|^2/n\). The singular statement is therefore correct on its admissible one-dimensional sample subspace. It does not assert that arbitrary \((v_1,v_2)\) remain independent coordinates at this endpoint.

## 3. Finite symmetry and conditional population symmetry

### 3.1 Label normalization and finite exchange symmetry

Source lines 95–128 correctly distinguish symmetry of a law from invariance of an individual state.

Under \((y,W^{(4)})\mapsto(-y,-W^{(4)})\), the predictions, residuals, and all backward \(\delta\)-fields change sign. A hidden update contains a residual times a backward field and is unchanged. The readout update contains only the residual times the forward feature and changes sign. Hence the loss and the dynamics transform as claimed. The centered independent Gaussian readout law, as well as zero readout, supports the reduction to \(y=(1,\sigma)\). This uses no oddness of the activation.

Because \(\rho<1\), \(x_1-x_2\neq0\) and the reflection \(R\) is well defined. In fact

\[
\|x_1-x_2\|^2=2d(1-\rho),\qquad
2v(v^Tx_1)=x_1-x_2,
\]

which proves \(Rx_1=x_2\); the other identity follows likewise. The statement includes \(\rho=-1\).

Right multiplication by \(R\) preserves the first Frobenius norm, and multiplication of the readout by \(\sigma\) preserves its norm. Thus \(S\) is an involutive isometry of the specified metric. Its hidden fields exchange the sample index at every layer, yielding

\[
f_a(S\theta)=\sigma f_{3-a}(\theta).
\]

For \(y=(1,\sigma)\), the two residuals consequently exchange with a factor \(\sigma\), so the sum of their squares is preserved. Differentiating the loss invariance in an arbitrary direction \(h\) gives

\[
\langle\nabla_G L(S\theta),Sh\rangle_G
=\langle\nabla_G L(\theta),h\rangle_G.
\]

Isometry and invertibility imply the gradient equivariance in the note. GD therefore commutes with \(S\) algebraically; finite GF commutes with it by uniqueness. Local existence and possible maximal intervals are respected by this transformation.

An isotropic Gaussian row multiplied by a fixed orthogonal \(R\) remains a Gaussian row with covariance \(I/d\), hence with the same independent-coordinate law. Row independence and block independence are preserved. The independent centered readout is also invariant under its optional sign. These facts establish (6), on the applicable path intervals.

To make the deterministic-limit implication precise, let \(T(f_1,f_2)=(\sigma f_2,\sigma f_1)\). If the finite paths converge in distribution to a deterministic path in a path space on which \(T\) is continuous, their invariant laws converge to \(\delta_f=T_\#\delta_f=\delta_{Tf}\). Thus \(Tf=f\). The same argument works at each fixed time if only deterministic pointwise limits are at issue. A random invariant law need not be supported on the fixed states of \(T\). The note states exactly this distinction and does not infer pathwise finite symmetry.

### 3.2 Population involutions and the entire initial state

Source lines 130–155 give a sufficient conditional argument, not a construction of the premises.

A pullback \(Ju=u\circ j\) by a measure-preserving involution satisfies

\[
J^2=I,\qquad \langle Ju,Jv\rangle=\langle u,v\rangle,
\qquad J^*=J,
\qquad J(\phi\circ u)=\phi\circ(Ju),
\]

whenever the displayed functions belong to the relevant spaces. The last identity is the precise meaning needed for the note's phrase “commutes with coordinate functions”; a wording clarification is recommended below.

Each initial-state condition is used, not just equality of the two prediction laws:

- \(J_1Z^{(1)}_{1,0}=Z^{(1)}_{2,0}\) and \(J_1^2=I\) fix both transformed first-layer sample fields.
- \(J_\ell W^{(\ell)}_0=W^{(\ell)}_0J_{\ell-1}\) implies \(J_\ell W^{(\ell)}_0J_{\ell-1}=W^{(\ell)}_0\), fixing both hidden operators.
- \(J_3W^{(4)}_0=\sigma W^{(4)}_0\) implies \(\sigma J_3W^{(4)}_0=W^{(4)}_0\), fixing the readout. Zero readout meets this condition for either sign.

The state representation here uses the first-layer sample fields. If frozen orthogonal first-layer coordinates are also retained, the transformation can be extended as the identity on those coordinates; they introduce no moving state omitted from the argument. On the active first-layer metric, sample exchange preserves \(C^{-1}\) because the swap matrix commutes with \(C\). At \(\rho=-1\), it preserves the constrained metric instead.

Under the explicitly assumed invariance of the equations and uniqueness class, the transformed solution therefore solves exactly the same initial-value problem. Uniqueness makes it identical to the original solution. The resulting operator intertwining and pointwise-function identity propagate the first-layer exchange through layers 2 and 3. At the readout,

\[
f_2=\langle W^{(4)},J_3H_1^{(3)}\rangle
=\langle J_3W^{(4)},H_1^{(3)}\rangle
=\sigma f_1.
\]

This proves every conclusion in (7), subject to the premises. Finite invariant laws do not themselves supply these common neuron spaces, fixed initial operators, or uniqueness in an uncut population class. The note explicitly leaves those obligations separate. Its compatibility sentence at lines 152–155 is not used as an existence theorem in this audit.

## 4. Full-gradient label mode and invertibility of the clock

Source lines 159–196 are correct. For gradient calculations, use the globally defined scalar function

\[
g(\theta)=\frac{f_1(\theta)+\sigma f_2(\theta)}2.
\]

The equality \(g=f_1\) is only its value on the symmetric path. One must not replace its full gradient by \(\nabla_G f_1\). With this distinction,

\[
\nabla_G g=\frac12\sum_a y_a\nabla_G f_a,
\qquad
\nabla_G L
=2(g-1)\sum_a y_a\nabla_G f_a
=4(g-1)\nabla_G g
\]

at every state on that path. This establishes (8) in the full raw metric, without taking a gradient of a restriction in an unspecified metric.

Let \(A(t)=\|\nabla_G g(\theta(t))\|_G^2\). The chain rule gives

\[
\dot g=4(1-g)A(t),\qquad
\frac{d}{dt}(1-g)=-4A(t)(1-g).
\]

Multiplying by the integrating factor proves the stated exponential identity. In particular, for \(g(0)=0\), on any compact physical interval \([0,T]\) with \(\int_0^T A(u)\,du<\infty\),

\[
1-g(t)\geq \exp\!\left(-4\int_0^T A(u)\,du\right)>0.
\]

Set \(s(0)=0\) and \(s(t)=4\int_0^t(1-g(u))\,du\). Its derivative is strictly positive and bounded away from zero on such a compact interval. It is therefore invertible onto its image, and the chain rule gives

\[
\frac{d\theta}{ds}=\nabla_G g,
\qquad
\frac{dt}{ds}=\frac1{4(1-g(\theta(s)))}.
\]

For a general initial symmetric prediction, \(g(0)<1\) gives the same positive-clock conclusion; \(g(0)>1\) gives a locally invertible decreasing clock while the integral remains finite. At \(g(0)=1\) the proposed clock vanishes and cannot be divided out. The note excludes division at a zero clock and uses the intended zero population readout for its positive-clock claim.

Substituting the metric gradient blocks yields the factor \(1/2\) in every part of (9), including the first-layer sample equation. Replacing normalized finite pairings by expectations yields the stated population rank-one expressions if the products, adjoints, and differentiation are defined as assumed. Furthermore,

\[
\frac{dg}{ds}=\|\nabla_G g\|_G^2
=\frac14\sum_{a,b}y_ay_b\langle\nabla_G f_a,\nabla_G f_b\rangle_G
=\frac14y^TKy,
\]

which is (10).

For completeness, the exact global inverse-clock condition is worth spelling out. Given a regular feature trajectory while \(g<1\),

\[
t(s)=\frac14\int_0^s\frac{du}{1-g(\theta(u))}.
\]

This recovers physical time only over the image of this integral. Covering all physical times requires this image to be unbounded, as well as a constructed feature trajectory. If a finite first level time \(s_*\) has a regular extension to \(g(s_*)=1\) and \(g'\leq M<\infty\) near \(s_*\), then

\[
1-g(s)=\int_s^{s_*}g'(u)\,du\leq M(s_*-s),
\]

so \(t(s)\to\infty\). If instead the feature trajectory exists for all \(s\geq0\) and remains below 1, zero initial readout and \(g'\geq0\) give \(0\leq g<1\), hence \(t(s)\geq s/4\to\infty\). Merely approaching level 1 at an unconstructed or singular endpoint does not supply either conclusion.

The note makes no global inversion assertion of the latter kind. Lines 191–196 correctly require further feature-flow construction and explicitly prohibit assigning this scalar physical clock to a generic finite trajectory with a nonzero off-mode residual.

## 5. Coordinate cancellation and the nonflattening claim

Source lines 200–239 are correct with the domain distinction described below.

For \(\phi(z)=1+\epsilon\arctan z\),

\[
\phi'(z)=\frac\epsilon{1+z^2},\qquad
F'(z)=\frac{1+z^2}\epsilon=\frac1{\phi'(z)}.
\]

Multiplication of the first-layer feature equation by \(F'(z_b^{(1)})\) gives (11) exactly. For unequal sample indices the derivative ratio is

\[
\frac{\phi'(z_a)}{\phi'(z_b)}
=\frac{1+z_b^2}{1+z_a^2}.
\]

It is unbounded on \(\mathbb R^2\). For \(-1<\rho<1\), the first-layer Gaussian covariance \(C\) is positive definite, so its density is positive everywhere. Every sufficiently large-ratio open set has positive probability. There is consequently no deterministic essential bound obtained from input normalization. This does not imply infinite Gaussian moments or prove divergence of the actual dynamics, and the note does not claim either.

To test (12), put \(\widetilde\Psi=B^{-1}\Psi\). Because \(C\) and the positive diagonal derivative matrix are invertible,

\[
D\widetilde\Psi
=\operatorname{diag}(F'(z_1),F'(z_2))C^{-1}.
\]

The first row would therefore satisfy

\[
\partial_1\widetilde\Psi_1=\frac{F'(z_1)}{1-\rho^2},
\qquad
\partial_2\widetilde\Psi_1=-\frac{\rho F'(z_1)}{1-\rho^2}.
\]

Equality of the mixed derivatives forces

\[
0=-\frac{\rho F''(z_1)}{1-\rho^2}.
\]

The second row similarly forces \(\rho F''(z_2)=0\). For shifted arctan, \(F''(z)=2z/\epsilon\). If \(0<|\rho|<1\), a putative chart would have to be supported where both coordinates vanish, which contains no nonempty open set. Thus this activation admits no such chart even locally on a nonempty open domain. In particular, the precise global-domain impossibility asserted in (12) holds.

For a general \(C^2\) activation with \(\phi'>0\), \(F'=1/\phi'\) is \(C^1\). If it is nonconstant on \(\mathbb R\), the mean value theorem implies \(F''\neq0\) somewhere. Consequently no chart satisfying (12) can be defined on all of \(\mathbb R^2\). This verifies the note's generalization with the domain stated in (12). A stronger assertion ruling out every local chart for every such activation would be false: an activation can be affine on an interval and nonlinear elsewhere, and a constant Jacobian works on the square of that interval. The wording can make this distinction more explicit, but the displayed global-domain claim needs no correction.

At \(\rho=0\), the cross-forcing coefficient is zero and the componentwise chart works. At \(\rho=-1\), the independent two-coordinate chart problem no longer applies: \(z_2^{(1)}=-z_1^{(1)}\), and evenness of the shifted-arctan derivative gives

\[
(F(z_1^{(1)}))'
=\frac12\left(q_1^{(1)}-\sigma q_2^{(1)}\right),
\]

which is (13). The obstruction is to flattening both arbitrary forcing directions as in (12), not to the existence of another estimate, a constrained reduction, or a limiting flow.

## 6. Initial Gaussian laws and the contrast estimate

### 6.1 Initialization limit and fresh matrices

Source lines 243–255 correctly restrict the Gaussian claim to the population initialization limit.

At layer 1, different rows give independent Gaussian pairs with covariance \(C\). Conditional on all preceding features, each row of a fresh matrix \(W^{(\ell)}\), \(\ell=2,3\), gives a centered Gaussian pair with covariance

\[
Q^{(\ell-1)}_{n,ab}
=\frac1n\sum_i h^{(\ell-1)}_{a,i}h^{(\ell-1)}_{b,i}.
\]

Distinct current rows are conditionally independent because their Gaussian weights are independent. No unconditional Gaussian claim is needed at finite width.

The covariance convergence can be justified directly. At layer 1, each empirical feature product is bounded and is averaged over independent rows, so its variance is \(O(n^{-1})\). At a later layer, conditional independence gives the same variance bound for a bounded empirical test function around its conditional mean. If the preceding empirical covariance converges to a deterministic matrix \(Q\), that conditional mean converges to the expectation under \(N(0,Q)\). Indeed, Gaussian pairs can be represented as \(Q_n^{1/2}G\); continuity of the nonnegative matrix square root and bounded continuity of the test function give convergence of the expectations, including when \(Q\) is singular. Apply this to \(\phi(U)\phi(V)\) and the other feature products and iterate through the two fresh matrices. Conditional variance bounds and a finite union bound also give joint convergence of the finitely many layerwise empirical averages needed here.

Thus the stated limiting covariance recursion follows. It is a recursion in uncentered feature second moments, not centered feature covariances: preactivations have mean zero because the fresh weights are centered, even though shifted-arctan features have nonzero means. The note uses the correct second moments. This initialization argument neither involves backward matrix reuse nor justifies a Gaussian description after training.

### 6.2 Constants and the singular-pair lower bound

For \(0<\epsilon\leq1/10\), \(|\arctan z|<\pi/2\) gives

\[
\frac56<1+\epsilon\arctan z<\frac76,
\qquad |\phi'(z)|\leq\epsilon.
\]

Hence \(m=5/6\), \(a=7/6\) are valid. The first preactivation marginal variance is 1, which is at most \(a^2\); later marginal variances are feature second moments and are also at most \(a^2\). The variance of the sample difference in layer \(\ell\) is exactly \(D_{\ell-1}\), with \(D_0=2(1-\rho)\).

Consider any centered Gaussian pair \((U,V)\), including a singular pair, with marginal variances at most \(a^2\). Put \(Z=U-V\) and \(D=\mathbb EZ^2\). The Lipschitz bound gives

\[
\mathbb E(\phi(U)-\phi(V))^2\leq\epsilon^2D.
\]

For the lower bound, let \(E=\{\max(|U|,|V|)>4a\}\). A centered scalar Gaussian with variance \(v\leq a^2\) has upper tail at \(M\) at most \(\exp(-M^2/(2a^2))\): apply Markov's inequality to its exponential, whose expectation is \(\exp(v\lambda^2/2)\), and take \(\lambda=M/a^2\). Applying this to both signs of both marginals gives

\[
\mathbb P(E)\leq4e^{-8}.
\]

The Gaussian fourth moment is \(\mathbb EZ^4=3D^2\), including \(D=0\); for positive \(D\) it follows by scaling a scalar standard Gaussian and differentiating its moment generating function four times at zero. Thus Cauchy–Schwarz gives

\[
\mathbb E[Z^2\mathbf1_E]
\leq(3D^2)^{1/2}(4e^{-8})^{1/2}
=2\sqrt3e^{-4}D.
\]

On \(E^c\), the interval between \(U\) and \(V\) lies inside \([-4a,4a]\). Integrating the derivative of arctangent along that interval gives

\[
|\arctan U-\arctan V|
\geq\frac{|U-V|}{1+16a^2}.
\]

Consequently

\[
\mathbb E(\phi(U)-\phi(V))^2
\geq\frac{\epsilon^2}{(1+16a^2)^2}
\left(D-\mathbb E[Z^2\mathbf1_E]\right)
\geq c\epsilon^2D,
\]

with exactly

\[
c=\frac{1-2\sqrt3e^{-4}}{(1+16a^2)^2}>0.
\]

No independence between \(U\) and \(V\), two-dimensional density, or positive determinant was used. In particular, at \(\rho=-1\) the first layer has \((U,V)=(G,-G)\), \(D_0=4\), and

\[
D_1=4\epsilon^2\mathbb E[(\arctan G)^2]>0.
\]

The general lower bound applies at this singular first layer and then at each later layer. It also remains valid when \(D=0\), because both sides are zero.

Iterating the two-sided inequality through three hidden layers gives

\[
c^3\epsilon^6\,2(1-\rho)
\leq D_3\leq\epsilon^6\,2(1-\rho).
\]

For the opposite-label mode, the readout part of \(\|\nabla_G g\|^2\) is \(D_3/4\), producing exactly (14), including the factor \(1/2\) in both bounds. This is positive for every allowed \(\rho<1\), including \(-1\), and degenerates as \(\rho\uparrow1\), which is consistent with indistinguishable inputs. For the same-label mode, the averaged readout feature is at least \(m\) pointwise, so its squared \(L^2\) norm is at least \(m^2\).

At the intended zero population readout, all hidden backward fields vanish initially, so the readout contribution is also the entire initial label-mode gradient norm squared, assuming the population gradient is defined. The note only needs the stated readout contribution. Neither the Gaussian recursion nor its lower bound persists automatically along training. The note correctly restricts (14) to initialization.

## 7. Deterministic feature-time obstruction: zero and nonzero readout

Source lines 301–368 are valid for the auxiliary finite feature flow \(\theta'=\nabla_G g\) defined by (9), with \(g=(f_1-f_2)/2\). This finite vector field is well defined even when the finite physical residual is not in the label mode. It should not be confused with an exact clock transformation of a generic finite GD/GF trajectory; the note already warns against that inference.

Use the normalized vector norm \(\|u\|_n=\|u\|_2/\sqrt n\), and let \(R(s)=\|W^{(4)}(s)\|_n\). Here “bounded by \(a\)” means \(|\phi|\leq a\), as required for the norm estimates. For the specified shifted arctan this holds with the preceding value of \(a\).

The deterministic backward and velocity estimates are

\[
\begin{aligned}
\|h_a^{(\ell)}\|_n&\leq a,\\
\|\delta_a^{(3)}\|_n&\leq bR,\\
\|\delta_a^{(2)}\|_n&\leq b^2\|W^{(3)}\|_{\rm op}R,\\
\|\delta_a^{(1)}\|_n&\leq b^3\|W^{(2)}\|_{\rm op}
                                   \|W^{(3)}\|_{\rm op}R,\\
\|(W^{(4)})'\|_n&\leq a,\\
\|(W^{(3)})'\|_{\rm op}&\leq abR,\\
\|(W^{(2)})'\|_{\rm op}&\leq ab^2\|W^{(3)}\|_{\rm op}R,\\
\frac{\sqrt d}{\sqrt n}\|(W^{(1)})'\|_F
&\leq b^3\|W^{(2)}\|_{\rm op}\|W^{(3)}\|_{\rm op}R.
\end{aligned}
\]

For the two middle velocities, this uses
\(\|uv^T/n\|_{\rm op}=\|u\|_n\|v\|_n\), followed by the triangle inequality over the two samples and their factor \(1/2\). For the first-layer velocity, each raw gradient block has metric norm

\[
\frac{\sqrt d}{\sqrt n}\left\|
\frac{\delta_a^{(1)}x_a^T}{d}\right\|_F
=\|\delta_a^{(1)}\|_n,
\]

because \(\|x_a\|=\sqrt d\). These calculations verify the dimension and width factors used in the note.

### 7.1 Zero readout

If \(R(0)=0\), then \(R(s)\leq as\leq aS\). Integrating each velocity bound using its maximum on \([0,S]\), in the order readout, layer 3, layer 2, layer 1, gives

\[
\begin{aligned}
M_3(S)&=M_0+a^2bS^2,\\
M_2(S)&=M_0+a^2b^2S^2M_3(S),\\
M_1(S)&=M_1+ab^3S^2M_2(S)M_3(S).
\end{aligned}
\]

These are valid upper bounds for the corresponding operator norms and first-layer metric norm. A sharper integration would improve some constants, but no missing factor invalidates the deliberately loose estimates.

The input difference gives

\[
\|z_1^{(1)}-z_2^{(1)}\|_n
\leq\frac{\|W^{(1)}\|_F}{\sqrt n}\|x_1-x_2\|
\leq M_1(S)\sqrt{2(1-\rho)}.
\]

Applying the three activation Lipschitz bounds and the two hidden operator bounds yields

\[
\|h_1^{(3)}-h_2^{(3)}\|_n
\leq b^3M_3(S)M_2(S)M_1(S)\sqrt{2(1-\rho)}.
\]

Finally,

\[
|g(s)|
=\left|\frac{(W^{(4)})^T(h_1^{(3)}-h_2^{(3)})}{2n}\right|
\leq\frac{aS}{2}b^3M_3(S)M_2(S)M_1(S)
\sqrt{2(1-\rho)},
\]

which is exactly (15). There is no use of an angle-dependent inverse covariance, a positive activation lower bound, or a special initial alignment in this estimate.

### 7.2 Nonzero readout

If \(R(0)\leq R_0\), the same readout estimate gives \(R(s)\leq B(S)=R_0+aS\). The same sequential integrations then give precisely

\[
\begin{aligned}
\widetilde M_3(S)&=M_0+abS B(S),\\
\widetilde M_2(S)&=M_0+ab^2S\widetilde M_3(S)B(S),\\
\widetilde M_1(S)&=M_1+b^3S\widetilde M_2(S)
                                      \widetilde M_3(S)B(S).
\end{aligned}
\]

Substituting these bounds in the preceding sample-difference argument proves

\[
|g(s)|\leq\frac{B(S)}2b^3\widetilde M_3(S)
\widetilde M_2(S)\widetilde M_1(S)\sqrt{2(1-\rho)}.
\]

At \(R_0=0\), all four expressions reduce exactly to the zero-readout bounds, including \(M_1(S)\). The extension does not assume zero initial predictions or initial sample symmetry. It is a statement about the auxiliary feature field, so no nonzero-readout scalar physical clock is silently required.

### 7.3 Global existence of these finite feature flows

For a smooth activation, or already \(\phi\in C^2\) with the boundedness assumptions used above, the finite feature vector field is locally Lipschitz. If a maximal solution had a finite right endpoint \(T\), the preceding bounds with \(S=T\), applied on every shorter subinterval, would bound all its raw coordinates. For fixed finite \(n,d\), operator bounds on the middle matrices imply Frobenius bounds by \(\|W\|_F\leq\sqrt n\|W\|_{\rm op}\). The first layer and readout are directly bounded as well.

Thus the trajectory remains in a bounded subset of a finite-dimensional space. Its closure is compact; the continuous vector field is bounded there, so the trajectory has a limit at \(T\). Local existence at that limit extends the solution past \(T\), a contradiction. This establishes the claimed existence on every bounded feature interval. It does not construct a population limit or prove that any of these finite feature trajectories reaches \(g=1\).

### 7.4 Gaussian initial norm bounds

The probability statements on lines 351–358 have the correct scaling in the fixed-dimension regime of the conclusion.

Writing \(W^{(1)}_{ij}=G_{ij}/\sqrt d\),

\[
\frac d n\|W^{(1)}_0\|_F^2
=\frac1n\sum_{i=1}^n\sum_{j=1}^d G_{ij}^2,
\]

whose expectation is \(d\) and variance is \(2d/n\). For fixed \(d\), Chebyshev's inequality therefore gives convergence in probability to \(d\) and establishes the claimed bound for any fixed \(M_1>\sqrt d\). This is not an unqualified statement for arbitrary simultaneous growth of \(d\) and \(n\); the note's angle-family conclusion expressly fixes \(d\).

For the rescaled Gaussian readout,

\[
\mathbb E\frac{\|W^{(4)}_0\|^2}{n}
=\frac1n\,n\,n^{-2}=n^{-2}.
\]

Markov's inequality gives \(\mathbb P(R(0)>1)\leq n^{-2}\), verifying \(R_0=1\).

A maximal \(1/4\)-separated set of unit vectors is a \(1/4\)-net. Disjoint balls of radius \(1/8\) about its points lie in the ball of radius \(9/8\), so volume comparison bounds its size by \(9^n\). For fixed nets \(N_1,N_2\), approximation of both arguments of the bilinear form gives

\[
\|W\|_{\rm op}
\leq\max_{u\in N_1,v\in N_2}|u^TWv|+\frac12\|W\|_{\rm op},
\]

and hence the factor 2 asserted in the note. For fixed unit \(u,v\), \(u^TWv\) is Gaussian of variance \(1/n\). A union bound at threshold 5 yields

\[
\mathbb P(\|W\|_{\rm op}>10)
\leq 2\,9^{2n}\exp(-25n/2)
=2\,9^{2n}\exp(-100n/8).
\]

The exponential rate is negative because \(2\log9<25/2\). For the two matrices together the failure bound is at most twice this quantity. Combining it with the first-layer and readout estimates gives the asserted simultaneous high-probability event. Its definition contains no input angle, so the norm event is uniform over the input pairs under consideration.

### 7.5 Quantifiers of the angle obstruction

For either readout initialization, fix \(S<\infty\), \(d\), the activation bounds, and the initial norm bounds. The established estimate has the form

\[
\sup_{0\leq s\leq S}|g(s)|\leq A(S)\sqrt{2(1-\rho)},
\]

where \(A(S)<\infty\) is independent of \(\rho\) and \(n\). If \(A(S)>0\), choosing \(1-\rho<1/(2A(S)^2)\) makes the right side strictly less than 1. If \(A(S)=0\), the exclusion of \(g=1\) is immediate. Consequently the first hitting time of \(g=1\), defined as infinity when no hit occurs, exceeds every fixed \(S\) for all sufficiently close angles under those bounds. This proves exactly the claimed absence of a uniform upper bound on the required feature time.

In fixed \(d\geq2\), such input families exist; for example, use \(x_1=\sqrt d\,e_1\) and \(x_2=\sqrt d(\rho e_1+\sqrt{1-\rho^2}\,e_2)\). In \(d=1\), equal nonzero input norms allow only correlations \(1\) and \(-1\), and the note excludes 1. Its vacuity observation is correct.

Exact fitting of the opposite labels would imply \(g=1\), so excluding this level excludes fitting on the specified feature interval. The converse is not claimed: for a nonsymmetric finite state, \(g=1\) alone need not mean both samples are fitted. Nor does this argument bound physical time for a generic finite trajectory. Constants depending on fixed \(\rho<1\), longer feature times, and a future globally stable population limit all remain possible.

## 8. Corrections, precision edits, and remaining obligations

**Required mathematical corrections:** None to the displayed identities, estimates, or scoped conclusions under their stated premises.

The following small wording changes would make the boundaries harder to misread:

1. At lines 131–133, replace “commutes with coordinate functions” by the explicit pointwise-composition identity \(J_\ell(\phi\circ u)=\phi\circ(J_\ell u)\), and similarly for any other scalar function used. Pullback need not commute with multiplication by a fixed noninvariant coordinate function. The proof uses pointwise composition, for which the assertion is correct.
2. At lines 228–230, state explicitly that the general-activation conclusion rules out a chart defined on all of \(\mathbb R^2\). For shifted arctan, the stronger impossibility on every nonempty open set is valid. Nonconstancy of \(1/\phi'\) somewhere is not enough for that stronger local assertion for an arbitrary activation.
3. At line 352, insert “for fixed \(d\), as \(n\to\infty\).” This is already the regime of lines 360–363, but placing it next to the convergence statement removes a possible dimensional ambiguity.
4. If the clock discussion is expanded, include \(t(s)=\frac14\int_0^s(1-g(u))^{-1}du\) and distinguish local invertibility from covering all physical times. A regular finite feature endpoint at level 1 gives divergence as proved above; a singular or unconstructed endpoint requires further work. The current note does not assert the missing global conclusion.

These are precision edits, not repairs of a failed reduction. In particular, no nonsingularity assumption should be added to the Gaussian estimate, no pathwise finite symmetry should be substituted for (6), and no angle-independent fitting bound should be inferred from initial contrast positivity.

The opening scope and final obligations are consistent with the verified mathematics. The note has not proved the construction of a common population state and its invariant uniqueness class, a two-sample local or clipped convergence theorem, global actual-response estimates, finite-width control of the off-mode residual, nontriviality along training, or the requested full-limit conclusions. Its finite feature-flow existence result is valid and does not discharge those population obligations. The initial contrast estimate and the deterministic time obstruction are compatible: the former is strictly positive for each fixed distinct pair, while both allow degeneration as the inputs approach one another.

This review supplies an external audit of this exact hashed reduction note only. It is not evidence that any of its expressly remaining obligations have been completed.
