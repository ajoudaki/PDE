# Isolated adversarial audit of the two-sample reduction

Date: 2026-09-06.

Candidate: /tmp/l3-two-sample-proof-DLuelg/EXACT_TWO_SAMPLE_REDUCTION.md

Exact candidate SHA256:

    549babfdf7e654ca6bc1df1300fd3854d28fa70fa79241fbe059d88b704f22f0

The audited candidate has 319 lines and 13,276 bytes. Line references below refer to that file.

## Provenance and verdict

I read the candidate completely. It was my only mathematical source. I also read the mandatory procedural instructions at /etc/codex/skills/solve-math-rigorously/SKILL.md; those instructions concern proof and audit procedure and supplied no mathematical premises for this review. I did not read the referenced contract, another project document, a previous proof or review, or task history. I used no experiments, agents, or external mathematical sources. The additional calculations and counterexample below are deductions made for this audit. The candidate was not edited; its SHA256 was recomputed after drafting this review and was unchanged.

**Verdict: the quantitative calculations and the limited obstruction claims are sound under their relevant hypotheses, but the note needs corrections before it is a precise standalone reduction.** The main logical gap is in the intrinsic population symmetry argument: invariance of a uniqueness class does not by itself make the initial readout fixed by the symmetry. The clock also needs an explicit domain of invertibility. Finally, the zero-readout estimate in Section 6 does not directly establish its stated application to a nondegenerate Gaussian readout.

I found no erroneous factor in the raw gradients, the four kernels, the label-mode normalization, the arctan nonflattening calculation, the Gaussian contrast estimate, or the deterministic bound (15). In particular, the contrast lower bound remains valid at the singular endpoint \(\rho=-1\).

The following are the required substantive corrections or qualifications:

1. **Intrinsic symmetry, lines 116–126:** require that the initial readout is fixed, \(J_3W^{(4)}_0=\sigma W^{(4)}_0\), and specify the transformation and index ranges used for the hidden actions. Uniqueness must concern the same initial-value problem after transformation.
2. **Clock, lines 145–161:** state that reparameterization is valid where \(1-g\ne0\), and that an increasing feature clock requires \(g<1\). Establish or explicitly assume the intended initial condition \(g_0<1\).
3. **Initialization application, lines 269–306:** either restrict the application of (15) to exactly zero readout or extend its proof to a bounded initial readout norm. A complete extension is given below.
4. **Continuous-time scope, lines 46–67 and 100–109:** identify the time normalization in (3), distinguish it from exact discrete GD, and state existence/uniqueness assumptions when referring to a finite GF path law. Differentiability alone suffices for the differential identities, not for a unique flow.
5. **Gaussian scope and source dependence, lines 11, 103–105, 211–220, and 304–306:** state which initialization scalings and independence assumptions are used, and say explicitly that the deterministic-covariance Gaussian pairs in Section 5 are population limiting pairs. Later-layer finite pairs are only conditionally Gaussian.
6. **Minor domain precision:** state the binary-label assumption used in Section 2; for an angle family approaching \(\rho=1\) at fixed input dimension, require \(d\ge2\).

Item 5 includes an explicitly acknowledged dependency, not an accusation that the candidate concealed its reference to the contract. Under the requested isolation, agreement with that contract cannot be certified. The mathematical consequences can be audited conditionally, as done below.

The open items in lines 313–318 are not counted as defects merely because they remain open. This review does not demand construction of the uncut population flow, global uniqueness, finite-width convergence, or a full theorem.

## 1. Raw gradients, kernels, and first-layer geometry

### Coordinate and metric gradients: correct

Take \(n,d\) to be positive integers, with the layer sizes implicit in the candidate: \(W^{(1)}\in\mathbb R^{n\times d}\), \(W^{(2)},W^{(3)}\in\mathbb R^{n\times n}\), and \(W^{(4)}\in\mathbb R^n\). Products with \(\phi'\) in the backward fields are componentwise.

The coordinate gradients obtained from the chain rule are

\[
 \nabla^{\rm coord}_{W^{(1)}}f_a=\frac{\delta^{(1)}_a x_a^T}{n},
 \qquad
 \nabla^{\rm coord}_{W^{(\ell)}}f_a
 =\frac{\delta^{(\ell)}_a(h^{(\ell-1)}_a)^T}{n}
 \quad(\ell=2,3),
 \qquad
 \nabla^{\rm coord}_{W^{(4)}}f_a=\frac{h^{(3)}_a}{n}.
\]

Inverting the four metric coefficients \(d/n,1,1,1/n\) gives exactly the four blocks in lines 41–44. No extra factor of \(n\) belongs inside a backward field.

For \(L=\sum_a(f_a-y_a)^2\), its metric gradient is

\[
 \operatorname{grad}L=2\sum_a(f_a-y_a)\operatorname{grad}f_a.
\]

Consequently the stated discrete parameter update implies

\[
 \Delta z^{(1)}_b
 =-2\eta_n\sum_a
 \frac{x_a^Tx_b}{d}(f_a-y_a)\delta^{(1)}_a,
\]

which verifies (1) exactly. This first-layer preactivation identity is an exact discrete identity because \(z^{(1)}_b\) is linear in \(W^{(1)}\).

The equality of the stipulated update with an update in the unavailable contract is outside this audit. Conditional on the metric and update declared here, the calculation is correct.

### Four kernel blocks: correct, including negative input correlation

For the first block, the pairing is

\[
 \frac dn
 \left\langle\frac{\delta^{(1)}_a x_a^T}{d},
                  \frac{\delta^{(1)}_b x_b^T}{d}\right\rangle_F
 =C_{ab}\frac{\langle\delta^{(1)}_a,\delta^{(1)}_b\rangle}{n}.
\]

The Frobenius pairing of two rank-one matrices yields the product of their two vector pairings, giving both middle blocks in (2). The readout block is

\[
 \frac1n\langle h^{(3)}_a,h^{(3)}_b\rangle.
\]

Thus each matrix is a Gram matrix in its parameter block. More explicitly, for any \(\alpha\in\mathbb R^2\),

\[
 \alpha^T K^{(\ell)}\alpha
 =\left\|\sum_a\alpha_a\operatorname{grad}_{\ell}f_a
  \right\|_{\ell}^2\ge0.
\]

This remains true when \(C_{12}<0\), including \(\rho=-1\). Entrywise negativity does not invalidate positive semidefiniteness.

### Equation (3): correct for a specified gradient-flow time

If \(t\) denotes the time of

\[
 \dot\theta=-\operatorname{grad}L,
\]

then the chain rule gives

\[
 \dot f=-2K(f-y),\qquad
 \dot L=2(f-y)^T\dot f=-4(f-y)^TK(f-y)\le0.
\]

If this is the continuous time associated with the GD step \(\eta_n=n^{-2}\), the convention is \(t=k\eta_n\). If instead the differential equation is written with \(-\eta_n\operatorname{grad}L\) per unit time, both right-hand sides acquire a factor \(\eta_n\).

These equations are not exact prediction-update or loss-monotonicity statements for discrete GD. For a nonlinear network, changing all parameter blocks simultaneously introduces nonlinear changes in the prediction. The candidate should state the GF/time convention at line 62, rather than leave the transition from a discrete update implicit.

Along an existing differentiable solution, differentiability of \(\phi\) suffices for the displayed finite-dimensional chain-rule identities. It does not, by itself, establish existence or uniqueness of that solution. For example, \(\phi\in C^2\) makes the finite parameter vector field locally Lipschitz. The shifted arctan used later meets this condition.

The population caveat in lines 65–67 is appropriate: the finite calculations do not establish that infinite-dimensional products, derivatives, or adjoints have the required domains and integrability.

### First-layer metric and endpoint: correct

For \(-1<\rho<1\), let \(u\) be one row of a first-layer variation, and let \(v=(v_1,v_2)=uX\). The unique row in \(\operatorname{span}\{x_1,x_2\}\) having these values is

\[
 u=v(X^TX)^{-1}X^T.
\]

Its squared Euclidean norm is

\[
 \|u\|^2=v(X^TX)^{-1}v^T
 =\frac1d vC^{-1}v^T.
\]

Multiplication by \(d/n\) and summation over rows gives (4). If an orthogonal component is allowed, its squared metric norm must be added; the candidate correctly excludes it in this formula. The raw first-layer gradient lies in the input span, so existing orthogonal components remain fixed.

At \(\rho=-1\), equality in the norm/inner-product relation gives \(x_2=-x_1\). Admissible sample variations satisfy \(v_2=-v_1\). Their in-span row is \(u=v_1x_1^T/d\), and its metric contribution is \(v_1^2/n\). Summing gives the asserted \(\|v_1\|^2/n\). An inverse of the singular matrix \(C\) is neither used nor needed.

## 2. Finite and population symmetry

### Global sign and sample exchange: correct under joint initialization invariance

The reduction to \(y=(1,\sigma)\) presupposes that both original labels belong to \(\{-1,1\}\). That label domain should be stated. The argument does not reduce arbitrary real labels to this form.

Under simultaneous sign change of the labels and readout, predictions and residuals change sign, and all the residual-free backward fields change sign. The products defining hidden loss gradients are therefore unchanged; the readout loss gradient changes sign. This verifies the global sign argument.

Since \(\rho<1\), \(x_1-x_2\ne0\). With \(v\) and \(R\) as in the candidate,

\[
 \|x_1-x_2\|^2=2d(1-\rho),\qquad
 v^Tx_1=\frac{d(1-\rho)}{\|x_1-x_2\|}
       =\frac{\|x_1-x_2\|}{2}.
\]

Hence \(Rx_1=x_2\), and likewise \(Rx_2=x_1\). This includes \(\rho=-1\). Orthogonality of \(R\) preserves the first-block Frobenius metric, and the sign change preserves the readout metric, so \(S\) is indeed an isometry.

Successive forward substitution proves

\[
 f_a(S\theta)=\sigma f_{3-a}(\theta).
\]

For \(y=(1,\sigma)\), the transformed residuals are

\[
 (r_1(S\theta),r_2(S\theta))=(\sigma r_2(\theta),\sigma r_1(\theta)),
\]

which proves \(L(S\theta)=L(\theta)\). Differentiating this identity through an isometry gives

\[
 \operatorname{grad}L(S\theta)=S\operatorname{grad}L(\theta).
\]

Discrete GD therefore commutes with \(S\) exactly. For GF, the transformation takes solutions to solutions. It gives a commuting solution map and hence the path-law statement (6) when the relevant initial-value problem has a unique solution, or when a specified solution selection is itself equivariant. Existence of a nonunique solution alone is insufficient for a selected path law.

The random initialization must be invariant jointly, not merely block by block in its marginal laws. Independent isotropic first-layer rows, fresh independent hidden matrices, and an independent centered Gaussian readout suffice. Isotropic first-layer marginals alone would not suffice if their coupling to the hidden matrices were arbitrary. The candidate's references to fresh Gaussian matrices support the intended independent setup, but it should be stated explicitly without relying on the unavailable contract.

### Equality in law versus equality on each realization: correctly distinguished

Equation (6) does not imply \(f_2=\sigma f_1\) for a finite realization. The candidate is explicit and correct about this.

If the prediction paths converge to a deterministic limit in a topology for which the exchange map is continuous, their invariant laws converge to an invariant point mass. Thus the limiting path is fixed by exchange, giving \(f_2=\sigma f_1\). Convergence in probability to a deterministic path, or the analogous deterministic finite-dimensional limits at each time, provides the corresponding precise interpretation.

A random limit with an invariant law need not be fixed on each outcome. The candidate correctly refuses that inference. Deterministic prediction symmetry alone also does not construct neuron-space involutions or prove all the operator identities in (7).

### Intrinsic population argument: missing initial fixed-point premise

Uniqueness compares solutions with the same initial condition. Invariance of the admissible class under a transformation is not enough: the transformation must also fix the prescribed initial state.

In particular, (7) asserts, already at time zero,

\[
 J_3W^{(4)}_0=\sigma W^{(4)}_0.
\]

This condition is not explicitly among the premises in lines 116–121. Saying that the uniqueness class is invariant under \(W^{(4)}\mapsto\sigma J_3W^{(4)}\) does not imply it. A centered Gaussian law being invariant under sign is also insufficient. Even zero initial predictions would be insufficient: they are scalar orthogonality conditions, not this readout identity.

A concrete counterexample to the premises with the readout condition omitted is available inside the finite-dimensional version of the same equations. Take one neuron per layer, \(d=1\), \(x_1=1,x_2=-1\), \(\sigma=-1\), shifted arctan activation, all hidden weights zero initially, and a nonzero scalar readout \(w_0\). Take every neuron-space involution to be the identity. The hidden intertwining and initial sample-exchange relations hold. The smooth finite initial-value problem is locally unique in the class of smooth finite solutions, a class preserved by the combined sample/sign transformation. Nevertheless,

\[
 f_1(0)=f_2(0)=w_0,
\]

so \(f_2(0)=-f_1(0)\) is false. The transformed solution has initial readout \(-w_0\); uniqueness of the original initial-value problem cannot identify these two solutions. This example addresses the stated intrinsic implication, not any unprovided additional condition in the contract.

If “invariant class” was intended to mean a class that already includes and preserves the prescribed initial data, then the missing readout equality is implicit in that interpretation. It should still be stated explicitly. Likewise, if “initial actions intertwine” was intended to include the readout with a specified output sign action, that definition is needed.

A precise corrected formulation uses the pullback actions of the measure-preserving involutions and the transformation

\[
 \widetilde Z^{(1)}_1=J_1Z^{(1)}_2,\qquad
 \widetilde Z^{(1)}_2=J_1Z^{(1)}_1,
\]
\[
 \widetilde W^{(\ell)}=J_\ell W^{(\ell)}J_{\ell-1}
 \quad(\ell=2,3),\qquad
 \widetilde W^{(4)}=\sigma J_3W^{(4)}.
\]

Require the initial state to be fixed by this entire transformation, including the readout. Require that the constructed equations and their solution class are preserved and that the same initial-value problem has a unique solution in that class. The transformed solution then equals the original one.

The index range for the hidden intertwining formula should be \(\ell=2,3\) in this formulation. If the full first-layer action is included, define the input action \(J_0=R\) and impose the corresponding first-layer fixed-point condition. The notation \(J_0\) is otherwise undefined in the candidate. For conclusions only about sample fields, inactive orthogonal first-layer components can be excluded from the reduced state.

Under these corrected premises, (7) follows. For instance,

\[
 H^{(3)}_2=J_3H^{(3)}_1,\qquad
 f_2=\langle W^{(4)},J_3H^{(3)}_1\rangle
    =\langle J_3W^{(4)},H^{(3)}_1\rangle
    =\sigma f_1.
\]

Here the inner product is normalized as appropriate to the neuron space. A measure-preserving involution has a self-adjoint isometric pullback and commutes with componentwise activation. Those facts justify this calculation. Construction of the spaces and uniqueness remain the explicitly marked obligations; no proof of those obligations is being demanded.

## 3. Label-mode normalization and clock

### Factors in (8)–(10): correct

Define the ambient scalar function

\[
 g(\theta)=\frac{f_1(\theta)+\sigma f_2(\theta)}2
\]

before restricting to a symmetric path. On such a path, \(f_2=\sigma f_1\), so \(g=f_1\) and \(r=(g-1)y\). Consequently

\[
 -\operatorname{grad}L
 =-2(g-1)(\operatorname{grad}f_1+\sigma\operatorname{grad}f_2)
 =4(1-g)\operatorname{grad}g.
\]

This verifies (8) as a full ambient gradient identity at those parameter states. In particular, one must not first replace the ambient function by \(f_1\) and then differentiate that different extension. The candidate avoids that error.

Taking half the label-weighted sum of the previously verified gradient blocks gives all three lines of (9), including the \(1/2\) in the first-layer equation and the \(1/2\) in each rank-one update. Along the independently defined feature ODE \(\theta'=\operatorname{grad}g\),

\[
 g'=\|\operatorname{grad}g\|^2
 =\frac14\sum_{a,b}y_ay_bK_{ab}
 =\frac14y^TKy.
\]

Thus (10) is correct. The factor is \(1/4\), not \(1/2\). As a further normalization check, if \(Ky=\lambda y\), then \(\|y\|^2=2\) gives

\[
 g'=\lambda/2,\qquad
 \dot g=2\lambda(1-g).
\]

The normalized readout contribution is likewise \(y^TK^{(4)}y/4\), which is the normalization used in (14).

### Domain of the time change: must be added

Equation (8) is valid even at \(g=1\). Deriving (9) from a physical trajectory by dividing by \(ds/dt=4(1-g)\), however, is valid only where \(1-g\ne0\).

For an increasing feature clock, require \(g<1\). Along a regular symmetric physical flow, put

\[
 A(t)=\|\operatorname{grad}g(\theta(t))\|^2.
\]

Then

\[
 \dot g=4(1-g)A(t),\qquad
 1-g(t)=(1-g(0))
 \exp\left(-4\int_0^t A(u)\,du\right)
\]

whenever the integral is finite. Thus an initial value \(g(0)<1\) preserves the required sign on such intervals. If \(g(0)>1\), the proposed clock decreases. If \(g(0)=1\), the physical loss gradient vanishes and the clock is constant; it does not provide a reparameterized feature trajectory.

The candidate should establish or assume \(g(0)<1\), and say that the inverse clock is used only on intervals with \(g<1\). A zero initial readout suffices. A zero deterministic population prediction can also suffice, but its derivation requires the initialization scaling.

For example, if initial readout entries are independent, centered, have a fixed finite variance \(\tau^2\), and are independent of bounded hidden features, then

\[
 \mathbb E[f_a(0)^2\mid H^{(3)}]
 =\frac{\tau^2}{n^2}\|h^{(3)}_a\|^2
 \le\frac{\tau^2a^2}{n}.
\]

This proves zero deterministic limiting predictions in probability under those explicit assumptions. It does not prove the initial neuron-space readout parity required for (7).

If a feature solution approaches \(g=1\), recovering physical time requires

\[
 t(s)=\int_0^s\frac{du}{4(1-g(u))}.
\]

Its behavior at the endpoint is a separate question. The candidate properly marks construction up to the relevant feature level as unfinished, but should not implicitly invert the clock at that level.

At finite width, the ODE \(\theta'=\operatorname{grad}g\) is a legitimate auxiliary ODE for any parameters. Its identification with the physical residual-driven trajectory requires label-mode residuals. The candidate's warning in lines 162–164 correctly prevents assigning this scalar clock to a general finite GD/GF trajectory.

## 4. First-layer cancellation and nonflattening

### Equations (11) and (13): correct

For the shifted arctan,

\[
 \phi'(z)=\frac{\epsilon}{1+z^2}>0,\qquad
 F'(z)=\frac{1+z^2}{\epsilon}=\frac1{\phi'(z)}.
\]

Multiplying the first-layer component of (9) by \(F'(z_b)\) proves (11). The diagonal ratio is one, and the off-diagonal ratio is exactly

\[
 \frac{\phi'(z_a)}{\phi'(z_b)}
 =\frac{1+z_b^2}{1+z_a^2}.
\]

This is unbounded on \(\mathbb R^2\). For example, fix \(z_a=0\) and let \(|z_b|\) increase. When \(-1<\rho<1\), a centered Gaussian pair with covariance \(C\) has positive density everywhere, so there is no deterministic essential upper bound for the ratio at initialization. This does not say that a finite collection of realized ratios is infinite, or that probabilistic moment estimates are impossible.

At \(\rho=0\), the off-diagonal coefficient in (11) is zero, so its unbounded ratio is irrelevant. At \(\rho=-1\), the constrained sample values satisfy \(z_2=-z_1\), and the derivative is even. For \(b=1\), \(y=(1,\sigma)\), \(C_{11}=1\), and \(C_{12}=-1\), (11) becomes

\[
 (F(z_1))'=\frac12(q_1-\sigma q_2),
\]

exactly as in (13). The differentiated relation for sample 2 is consistent with \(F(-z)=-F(z)\). No endpoint contradiction arises.

### Integrability obstruction in (12): correct within its stated scope

Write \(A(z)=C\operatorname{diag}(\phi'(z_1),\phi'(z_2))\). For \(0<|\rho|<1\), \(A(z)\) is invertible. If \(D\Psi(z)A(z)=B\) with constant invertible \(B\), set \(\Phi=B^{-1}\Psi\). Then

\[
 D\Phi(z)=A(z)^{-1}
 =\operatorname{diag}(F'(z_1),F'(z_2))C^{-1}.
\]

The order of the two factors here is essential and is correct in the candidate. Since

\[
 C^{-1}=\frac1{1-\rho^2}
 \begin{pmatrix}1&-\rho\\-\rho&1\end{pmatrix},
\]

the first row requires

\[
 \partial_1\Phi_1=\frac{F'(z_1)}{1-\rho^2},
 \qquad
 \partial_2\Phi_1=-\frac{\rho F'(z_1)}{1-\rho^2}.
\]

For a \(C^2\) chart, equality of mixed partials gives

\[
 0=-\frac{\rho F''(z_1)}{1-\rho^2}.
\]

For arctan, \(F''(z_1)=2z_1/\epsilon\). Every nonempty open subset of \(\mathbb R^2\) contains a point with \(z_1\ne0\), so there is no such chart even on a nonempty open set. In particular, there is none on all of \(\mathbb R^2\).

For a general \(C^2\) activation with positive derivative, the reciprocal derivative is \(C^1\). If it is nonconstant on \(\mathbb R\), its derivative is nonzero somewhere, so the same argument excludes a chart defined on all of \(\mathbb R^2\). This verifies the generalization at lines 197–198 with the global domain specified in lines 183–184.

One should not strengthen that generalization to exclude every local chart for every such activation: an activation can have a derivative that is constant on an interval and nonconstant elsewhere. A chart may then exist on a rectangle lying inside that interval. The arctan statement is stronger because its reciprocal derivative is not constant on any open interval.

The calculation excludes simultaneous constant-coefficient flattening of the two forcing columns. It does not exclude a different nonlinear representation, a useful estimate along the actual coupled trajectory, or construction of a population dynamics. The candidate correctly limits its conclusion to a chart obstruction.

## 5. Initial Gaussian contrast, including the singular endpoint

### Initialization law and finite/population distinction

The covariance recursion used here is correct under the following explicit sufficient forward initialization assumptions:

\[
 W^{(1)}_{ij}\ \text{independent }N(0,1/d),\qquad
 W^{(2)}_{ij},W^{(3)}_{ij}\ \text{independent }N(0,1/n),
\]

with the matrices independent of one another. These are conditions under which the candidate's assertions hold, not a claim about the contents of the unread contract.

For a fresh hidden matrix and fixed preceding features, each row's sample pair is centered Gaussian with conditional covariance

\[
 \Sigma^{(\ell)}_{ab,n}
 =\frac1n\langle h^{(\ell-1)}_a,h^{(\ell-1)}_b\rangle.
\]

Distinct new rows are conditionally independent. This verifies the conditional claim in lines 215–217.

At finite width, the conditional covariance above is a random matrix before conditioning, and the unconditional preactivation pair is generally a Gaussian mixture, not a Gaussian pair with deterministic covariance. For a single coordinate with random conditional variance \(Q\), for example,

\[
 \mathbb E[U^4]=3\mathbb E[Q^2],
\]

whereas a centered Gaussian with variance \(\mathbb E Q\) has fourth moment \(3(\mathbb E Q)^2\). These differ when \(Q\) is nonconstant.

Accordingly, lines 212–214 should begin “In the population initialization limit, for each hidden layer ...”. Reading them as unconditional finite-width assertions would be false.

The stated induction to a population limit is valid for the bounded activation used here. At layer 1, the pairs are independent with covariance \(C\), so bounded feature second moments converge by averaging. At each later layer, conditional averaging has variance of order \(1/n\) for bounded test functions. Its conditional mean is the corresponding Gaussian integral at \(\Sigma_n\); this integral converges when \(\Sigma_n\) converges, including at singular covariance matrices. One can see the latter by representing the pair as \(\Sigma_n^{1/2}G\) for a standard Gaussian vector \(G\) and using continuity and bounded convergence.

Thus the deterministic covariance recursion and bounded joint sample-pair averages follow through the three forward layers. This reasoning uses fresh matrices and does not establish any training-time or backward-field Gaussian law. The candidate does not claim that it does.

The covariance of the new preactivations is the preceding features' **second-moment matrix**, not their centered covariance. The constant shift in \(\phi\) makes this distinction material; the candidate uses the correct quantity.

### Uniform scalar bounds: correct

For \(0<\epsilon\le1/10\),

\[
 1-\frac{\pi}{20}<\phi(z)<1+\frac{\pi}{20},
 \qquad
 \frac{\pi}{20}<\frac16.
\]

Hence \(m=5/6\), \(a=7/6\) are valid strict bounds, and \(0<\phi'(z)\le\epsilon\).

At layer 1, each Gaussian preactivation has variance \(1\le a^2\). At each later initial layer, its variance is a preceding feature second moment and is at most \(a^2\). For the sample difference, the same covariance recursion gives

\[
 \mathbb E[(Z^{(\ell)}_1-Z^{(\ell)}_2)^2]
 =D_{\ell-1},
\]

with \(D_0=2(1-\rho)\). This establishes all hypotheses needed at every step of the proposed recursion.

### The lower bound and its constants: correct

Let \(U,V\) be any centered jointly Gaussian pair with marginal variances at most \(a^2\), allowing singular covariance. Let

\[
 D=\mathbb E(U-V)^2,\qquad
 E=\{\max(|U|,|V|)>M\}.
\]

The activation difference is

\[
 |\phi(U)-\phi(V)|
 =\epsilon|\arctan U-\arctan V|
 \le\epsilon|U-V|,
\]

which proves the upper bound \(\epsilon^2D\).

On \(E^c\), the entire interval between \(U\) and \(V\) lies in \([-M,M]\). Integrating the derivative \(1/(1+z^2)\) along that interval gives

\[
 |\arctan U-\arctan V|
 \ge\frac{|U-V|}{1+M^2}.
\]

The centered Gaussian exponential-moment bound gives each two-sided marginal tail at most \(2e^{-M^2/(2a^2)}\). Taking the union of the two events gives

\[
 \mathbb P(E)\le4e^{-M^2/(2a^2)}.
\]

No independence between \(U\) and \(V\) is used here. A zero-variance marginal causes no problem.

Since \(U-V\) is itself centered Gaussian,

\[
 \mathbb E(U-V)^4=3D^2.
\]

Cauchy–Schwarz therefore gives

\[
 \mathbb E[(U-V)^2\mathbf1_E]
 \le \sqrt{3D^2}\sqrt{4e^{-M^2/(2a^2)}}
 =2\sqrt3\,D e^{-M^2/(4a^2)}.
\]

Putting \(M=4a\) gives precisely \(2\sqrt3 e^{-4}D\), not an exponent of \(-8\). Consequently

\[
 \mathbb E[(\phi(U)-\phi(V))^2]
 \ge
 \epsilon^2
 \frac{1-2\sqrt3e^{-4}}{(1+16a^2)^2}D.
\]

The numerator is positive. Thus the stated constant \(c>0\) is valid. If \(D=0\), the difference vanishes almost surely and both upper and lower bounds are zero; the proof never divides by \(D\).

Applying this inequality three times gives

\[
 c^3\epsilon^6D_0\le D_3\le\epsilon^6D_0.
\]

For opposite labels, the readout part of \(\|\operatorname{grad}g\|^2\) is

\[
 \left\|\frac{H^{(3)}_1-H^{(3)}_2}{2}\right\|_{L^2}^2
 =\frac{D_3}{4}.
\]

Substituting \(D_0=2(1-\rho)\) gives exactly (14), with both displayed factors \(1/2\) correct.

### Explicit check at \(\rho=-1\): no loophole

At the first layer, write \(U\sim N(0,1)\) and \(V=-U\). Then \(D_0=4\) and

\[
 H^{(1)}_1-H^{(1)}_2=2\epsilon\arctan U,\qquad
 D_1=4\epsilon^2\mathbb E[(\arctan U)^2]>0.
\]

The argument above applies directly to this singular Gaussian pair.

There is also no requirement that later pairs remain perfectly anticorrelated. If \(v=\mathbb E[(\arctan U)^2]>0\), the first-layer feature second-moment matrix is

\[
 \begin{pmatrix}
 1+\epsilon^2v&1-\epsilon^2v\\
 1-\epsilon^2v&1+\epsilon^2v
 \end{pmatrix},
\]

whose two eigenvalues are \(2\) and \(2\epsilon^2v\), both positive. The shift in the activation supplies the common mode. The second-layer Gaussian pair is therefore nondegenerate under the stated recursion.

It follows that (14) is strictly positive for every allowed \(\rho<1\), including \(-1\). At the excluded endpoint \(\rho=1\), the two inputs coincide and the contrast is zero, consistent with the bounds.

For equal labels, \((H^{(3)}_1+H^{(3)}_2)/2>m\) pointwise, so its squared \(L^2\) norm is at least \(m^2\), as claimed. Neither this calculation nor the initial contrast recursion proves a training-time lower bound in the opposite-label case. Also, (14) bounds the readout contribution; it is not an upper bound on the full label-mode kernel. The candidate's explicit initial-only qualification is appropriate.

## 6. Deterministic feature-time obstruction

### All estimates (15) and its prerequisites are correct for zero readout

Interpret “bounded by \(a\)” as \(|\phi|\le a\), and use \(|\phi'|\le b\). Let

\[
 \|u\|_n=\frac{\|u\|_2}{\sqrt n},\qquad
 \|W^{(1)}\|_*=\sqrt{\frac dn}\|W^{(1)}\|_F.
\]

For the finite auxiliary feature flow and \(\sigma=-1\),

\[
 (W^{(4)})'=\frac{h^{(3)}_1-h^{(3)}_2}{2},
 \qquad
 \|(W^{(4)})'\|_n\le a.
\]

Starting from zero readout gives \(\|W^{(4)}(s)\|_n\le as\le aS\). Consequently

\[
 \|\delta^{(3)}_a(s)\|_n\le abS.
\]

For a rank-one update, \(\|uv^T/n\|_{\rm op}=\|u\|_n\|v\|_n\). Taking the norm of the half-sum of its two sample terms therefore gives

\[
 \|(W^{(3)})'\|_{\rm op}\le a^2bS,
\]

and integration over an interval of length at most \(S\) gives

\[
 \|W^{(3)}(s)\|_{\rm op}
 \le M_0+a^2bS^2=M_3(S).
\]

Using the sharper pointwise readout bound \(as\) would improve a numerical factor, but the looser bound in the candidate is valid.

Backpropagating once gives

\[
 \|\delta^{(2)}_a(s)\|_n
 \le b\,M_3(S)\|\delta^{(3)}_a(s)\|_n
 \le ab^2M_3(S)S.
\]

Thus

\[
 \|(W^{(2)})'\|_{\rm op}\le a^2b^2M_3(S)S,
 \qquad
 \|W^{(2)}(s)\|_{\rm op}
 \le M_0+a^2b^2M_3(S)S^2=M_2(S).
\]

Backpropagating again gives

\[
 \|\delta^{(1)}_a(s)\|_n
 \le ab^3M_2(S)M_3(S)S.
\]

The exact norm of the first-layer sample-gradient block is

\[
 \left\|\frac{\delta^{(1)}_a x_a^T}{d}\right\|_*
 =\|\delta^{(1)}_a\|_n,
\]

because \(\|x_a\|^2=d\). The feature gradient is the half-sum with signs. The triangle inequality therefore gives the claimed first-layer speed bound and, after integration,

\[
 \|W^{(1)}(s)\|_*
 \le M_1+ab^3M_2(S)M_3(S)S^2=M_1(S).
\]

The input difference satisfies \(\|x_1-x_2\|=\sqrt{2d(1-\rho)}\), so

\[
 \|z^{(1)}_1-z^{(1)}_2\|_n
 \le \frac{\|W^{(1)}\|_F}{\sqrt n}\|x_1-x_2\|
 \le M_1(S)\sqrt{2(1-\rho)}.
\]

Applying the three Lipschitz activations and the two hidden operator bounds yields

\[
 \|h^{(3)}_1-h^{(3)}_2\|_n
 \le b^3M_3(S)M_2(S)M_1(S)\sqrt{2(1-\rho)}.
\]

Finally, the definition \(g=(f_1-f_2)/2\) and Cauchy–Schwarz give

\[
 |g(s)|
 \le \frac12\|W^{(4)}(s)\|_n
             \|h^{(3)}_1(s)-h^{(3)}_2(s)\|_n,
\]

which is exactly (15). The order of the matrix factors is immaterial for these scalar norm products. Every power of \(a,b,S,n,d\) in the stated bound is accounted for.

No pathwise sample symmetry is needed for this finite auxiliary-flow estimate. In particular, it remains valid even though \(g\) need not equal \(f_1\) at finite width.

### Finite global existence and the obstruction's quantifiers

For a smooth activation, the finite vector field is locally Lipschitz. The preceding estimates hold on any existing portion of a solution inside a bounded feature interval. They bound the first-layer and readout Euclidean norms directly; the hidden operator bounds also bound the hidden Frobenius norms for fixed finite \(n\). Thus the solution stays in a bounded subset of the finite parameter space on each bounded interval.

A locally Lipschitz vector field is bounded and admits continuation near a compact set containing that trajectory. A finite maximal endpoint would therefore contradict these bounds and local continuation. This verifies the finite global-existence assertion in lines 300–301. It does not establish infinite-dimensional existence or uniform control of backward random fields in a population space.

Fix \(S<\infty\) and fixed bounds \(a,b,M_0,M_1\) independent of \(\rho\). The right-hand side of (15) tends to zero as \(\rho\uparrow1\), uniformly in \(s\le S\). Consequently, for \(\rho\) sufficiently close to one, the feature trajectory cannot have \(g=1\) anywhere on \([0,S]\).

If

\[
 T_\rho=\inf\{s\ge0:g(s)=1\}
\]

with the infimum defined as \(+\infty\) when the set is empty, this proves that no finite bound for \(T_\rho\) can hold uniformly as \(\rho\uparrow1\) within such a family. It does not assume eventual hitting.

At finite width, fitting both labels implies \(g=1\); the converse need not hold because an off-mode prediction component may remain. Thus excluding \(g=1\) is sufficient for this necessary obstruction to fitting.

At fixed dimension, a continuously varying angle family requires \(d\ge2\). If \(d=1\) and both norms are \(\sqrt d\), the only correlations are \(1\) and \(-1\); the allowed set \(\rho<1\) then contains only \(-1\). The statement about approaching one is vacuous in that case. This is a minor domain qualification, not a counterexample to the intended obstruction.

The result concerns the auxiliary feature time. It gives neither an angle-dependent population convergence theorem nor a scalar physical clock for arbitrary finite trajectories. The candidate correctly acknowledges both limitations.

### The Gaussian-readout application needs correction

The proof just verified assumes exactly \(W^{(4)}_0=0\). Earlier, the note describes a centered Gaussian readout, without stating that it is degenerate at zero. A nondegenerate centered Gaussian vector is not zero, and the fact that its normalized initial predictions may converge to zero does not make its normalized parameter norm vanish.

Accordingly, the sentence about the “canonical Gaussian initialization” in lines 304–306 is not a justified application of (15) from the premises stated in this isolated note. If the intended canonical readout is exactly zero, say so. If it is nonzero, the following extension repairs the issue completely at the deterministic level.

Assume

\[
 \|W^{(4)}_0\|_n\le R_0
\]

for a constant \(R_0\) independent of \(\rho\), and retain the stated hidden and first-layer initial bounds. Define

\[
 B(S)=R_0+aS,
\]
\[
 \widetilde M_3(S)=M_0+ab\,S B(S),
\]
\[
 \widetilde M_2(S)
 =M_0+ab^2\,S\,\widetilde M_3(S)B(S),
\]
\[
 \widetilde M_1(S)
 =M_1+b^3\,S\,\widetilde M_2(S)\widetilde M_3(S)B(S).
\]

Indeed, the readout bound becomes \(\|W^{(4)}(s)\|_n\le B(S)\). The three corresponding backward bounds are

\[
 \|\delta^{(3)}_a\|_n\le bB(S),\quad
 \|\delta^{(2)}_a\|_n\le b^2\widetilde M_3(S)B(S),\quad
 \|\delta^{(1)}_a\|_n
 \le b^3\widetilde M_2(S)\widetilde M_3(S)B(S).
\]

Multiplication by a feature norm at most \(a\), followed by integration over length \(S\), proves the two hidden bounds. Integration of the first-layer metric speed proves its bound. The same forward Lipschitz calculation then gives

\[
 \sup_{0\le s\le S}|g(s)|
 \le
 \frac{B(S)}2 b^3\widetilde M_3(S)
 \widetilde M_2(S)\widetilde M_1(S)
 \sqrt{2(1-\rho)}.
\]

At \(R_0=0\), these constants reduce exactly to the candidate's constants and bound. At any fixed finite \(R_0\), the same angle obstruction and finite-existence argument hold.

This repair uses no centering, independence, sample symmetry, or Gaussianity of the readout. Those assumptions matter only if one then wants to prove that a specific random initialization satisfies the norm bounds with high probability.

For clarity, under the sufficient Gaussian scalings stated in Section 5 of this review, and with independent readout entries \(N(0,\tau^2)\) for a fixed \(\tau\), such bounds are available:

\[
 \frac dn\|W^{(1)}_0\|_F^2\longrightarrow d,\qquad
 \frac1n\|W^{(4)}_0\|^2\longrightarrow\tau^2
\]

in probability by averaging independent Gaussian squares, with \(d\) fixed. Hence one can choose \(M_1>\sqrt d\) and \(R_0>\tau\).

A bounded high-probability hidden operator norm can also be checked without assuming an unspecified matrix theorem. A \(1/4\)-net of the unit sphere in \(\mathbb R^n\) can be chosen with at most \(9^n\) points, by packing disjoint balls of radius \(1/8\). For an \(n\times n\) matrix \(W\) with independent \(N(0,1/n)\) entries, each fixed unit-vector pairing \(u^TWv\) is \(N(0,1/n)\). Approximation by nets on both spheres gives

\[
 \|W\|_{\rm op}
 \le2\max_{u,v\ \text{in the nets}}|u^TWv|.
\]

The scalar Gaussian tail bound and a union bound therefore imply

\[
 \mathbb P(\|W\|_{\rm op}>8)
 \le 2\,81^n e^{-8n},
\]

which tends to zero. Applying this to both hidden matrices supplies, for example, \(M_0=8\) with probability tending to one. These conditional calculations justify the type of norm assertion made by the candidate once its actual Gaussian scaling is explicitly supplied. They do not verify an unread initialization specification.

## 7. Claim scope and final disposition

The following distinctions survive the adversarial checks:

- Exact raw finite parameter calculus does not supply population analytic justification.
- Finite symmetry is a path-law statement under joint initialization invariance and an appropriate solution map. A deterministic prediction limit has pathwise prediction symmetry; a random limit need not.
- Full intrinsic population symmetry needs a fixed initial state and uniqueness for that same initial-value problem.
- The normalized feature vector field is valid as an auxiliary gradient field. Its identification with physical time is conditional on residual symmetry and an invertible clock.
- The nonflattening result rules out the specified simultaneous constant-forcing chart, not the dynamics.
- The Gaussian estimate proves a positive initial readout contrast of order bounded above and below by constants times \(\epsilon^6(1-\rho)\). It proves no persistent opposite-label kernel lower bound.
- The deterministic estimates exclude a common bounded feature interval for fitting increasingly coincident opposite-label inputs under uniform initial norm bounds. They do not rule out longer angle-dependent trajectories.

The note explicitly leaves local/clipped population construction, global response estimates, off-mode finite-width control, nontriviality, and full-limit obligations open. None of those is being reclassified here as an error in a theorem the note did not claim to prove.

**Disposition:** retain the displayed quantitative bounds and the limited route-obstruction conclusions. Amend the intrinsic symmetry premises, clock domain, and initialization application as above; make the finite/population and time-normalization qualifications explicit. With those changes, the audited content is a valid conditional reduction and deterministic obstruction note. Without them, the unqualified sentence that the symmetry identities are “available” overstates what the stated intrinsic premises establish.
