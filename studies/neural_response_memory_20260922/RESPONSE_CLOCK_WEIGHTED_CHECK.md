# Weighted-measure response-clock check

This is a scoped algebraic check from the supervisor's stated equations, including the subsequently supplied finite tanh response equations. No other scientific inputs or experiments were used. The `solve-math-rigorously` skill supplied the proof-checking procedure. This is an internal check, not an independent promotion review.

**Conclusion.** The moment equations, initialization, cancellation of the clock from the reconstructed weight derivative, and resulting explicit clock ordering are correct. A prefix of positive Lebesgue measure makes the exact Gram matrix positive definite at every finite clock value and finite polynomial order. Arclength control makes the actual response histories Lipschitz in the clock, but the artificial zero prefix for the normalized residual response retains its jump. Weighted polynomial approximation gives a finite-clock reconstruction bound despite that jump. None of these statements supplies a uniform condition-number bound, a bound on total clock length, global passage through residual zeros, a population theorem, or a computational speedup.

## Setup and exact moment equations

Fix a finite polynomial order \(P\geq1\), and work on a classical finite-dimensional solution interval on which the residual RMS \(\rho(t)>0\). Let

\[
q(t)=1+\int_0^t g(s)\,ds,\qquad g\geq\rho>0.
\]

All assertions below at time \(t\) require \(q(t)<\infty\). Record actual samples at the unchanging historical coordinate \(\tau=q(s)\). On the prefix \(0\leq\tau<1\), set \(h(\tau)=h_0\), \(u(\tau)=0\), and \(d\mu=d\tau\). On actual history set

\[
h(q(s))=h(s),\qquad u(q(s))=\frac{r(s)\delta(s)}{\rho(s)},
\qquad d\mu(q(s))=\rho(s)\,ds.
\]

The same notation denotes the time history and its clock parametrization. The value assigned exactly at \(\tau=1\) does not affect a moment: the measure has no atom there. The measure on \(0\leq\tau\leq q(t)\) has density (1) on the prefix and \(\rho/g\leq1\) on actual history. In particular its mass is

\[
m(t)=1+\int_0^t\rho(s)\,ds\leq q(t).
\]

Let \(p_k\) be the shifted Legendre polynomial with \(p_k(1)=1\), and set \(p=(p_0,\ldots,p_{P-1})^\top\), \(e=p(1)=\mathbf1\). The supplied identity \(xp'(x)=Tp(x)\) has \(T_{kk}=k\), \(T_{kj}=2j+1\) for \(j<k\), and zero entries for \(j>k\). Define

\[
H=\int h(\tau)p(\tau/q)^\top\,d\mu(\tau),\quad
U=\int u(\tau)p(\tau/q)^\top\,d\mu(\tau),\quad
G=\int p(\tau/q)p(\tau/q)^\top\,d\mu(\tau).
\]

Here \(H\in\mathbb R^{d_h\times P}\), \(U\in\mathbb R^{d_u\times P}\), and \(G\in\mathbb R^{P\times P}\). If multiple samples \(a\) have the same insertion measure and clock, they share \(G\).

At a fixed historical coordinate,

\[
\frac{d}{dt}p(\tau/q)=-\frac{g}{q}Tp(\tau/q).
\]

Differentiating the finite integrals therefore gives, with \(\alpha=g/q\),

\[
\dot H=\rho h e^\top-\alpha HT^\top,\qquad
\dot U=\rho u e^\top-\alpha UT^\top
       =r\delta e^\top-\alpha UT^\top,
\]

\[
\dot G=\rho ee^\top-\alpha(TG+GT^\top).
\]

Continuous finite-time histories and a finite clock justify differentiation on each compact solution interval; the same formulas hold almost everywhere under absolute continuity and the corresponding integrability assumptions.

At \(t=0\), shifted Legendre orthogonality on the prefix yields exactly

\[
q=1,\qquad H=[h_0,0,\ldots,0],\qquad U=0,\qquad
G=D:=\operatorname{diag}_{k=0}^{P-1}\frac1{2k+1}.
\]

## Positive definiteness and projection identities

For every nonzero \(v\in\mathbb R^P\), the polynomial \(v^\top p(\tau/q)\) is nonzero and cannot vanish on the entire prefix interval. Consequently

\[
v^\top Gv\geq\int_0^1|v^\top p(\tau/q)|^2\,d\tau>0.
\]

Thus \(A=G^{-1}\) exists for finite \(q,P\). More specifically,

\[
q\int_0^{1/q}p(x)p(x)^\top\,dx\preceq G\preceq qD.
\]

The lower bound is positive definite at a fixed \(q,P\); it need not be uniformly useful as either grows. Exact positive definiteness does not establish numerical conditioning or its preservation by a time discretization.

The functions

\[
h_P(\tau)=HA p(\tau/q),\qquad u_P(\tau)=UA p(\tau/q)
\]

are the componentwise \(L^2(\mu)\) orthogonal projections onto polynomials of degree at most \(P-1\). Their endpoint values are \(h_p=HAe\), \(u_p=UAe\). Define

\[
S=UAH^\top,\qquad \mathcal J=\int u h^\top\,d\mu.
\]

Projection orthogonality gives

\[
S=\int u_Ph_P^\top\,d\mu
 =\int u h_P^\top\,d\mu
 =\int u_P h^\top\,d\mu,
\]

\[
\mathcal J-S=\int(u-u_P)(h-h_P)^\top\,d\mu.
\tag{1}
\]

No unweighted orthogonality is assumed for actual history. The matrix \(G\) supplies the appropriate weighted inner product.

## Cancellation and the weight defect

The inverse derivative is

\[
\dot A=-A\dot G A=-\rho Aee^\top A+\alpha AT+\alpha T^\top A.
\]

Substituting into \(\dot S=\dot UAH^\top+U\dot A H^\top+UA\dot H^\top\), the terms \( -\alpha UT^\top AH^\top\) and \(+\alpha UT^\top AH^\top\) cancel, as do \(+\alpha UATH^\top\) and \(-\alpha UATH^\top\). The remaining terms are

\[
\dot S=\rho\bigl(u h_p^\top+u_p h^\top-u_p h_p^\top\bigr).
\tag{2}
\]

For \(c=2/(nM)\) and \(\widehat W=W_0-c\sum_aS_a\), the discrepancy from the intended middle-layer update evaluated at the same current state is exactly

\[
\dot{\widehat W}-\left(-c\rho\sum_a u_a h_a^\top\right)
=c\rho\sum_a(u_a-u_{p,a})(h_a-h_{p,a})^\top.
\tag{3}
\]

The sign in the proposed defect is therefore correct. At initialization \(h_p=h_0\), \(u_p=0\), so (2) gives \(\dot S(0)=\rho(0)u(0)h_0^\top\). The initial middle-layer update is exact even if \(u(0)\ne0\).

Cancellation means that the instantaneous reconstructed derivative at the current state contains no \(g\). The accumulated state and the locations of later inserted points still depend on the past clock choices.

## Explicit finite tanh response ordering

For the supplied depth-three finite model, use \(h_a=h_{1,a}\), \(\delta_a=\delta_{2,a}\), and \(u_a=r_a\delta_{2,a}/\rho\), with \(\rho^2=M^{-1}\sum_a r_a^2\). The equations supplied for this check are

\[
\dot W_1=-\frac{2}{M\sqrt d}\sum_a r_a\delta_{1,a}x_a^\top,
\qquad \dot W_3=-\frac2M\sum_a r_a h_{2,a},
\]

\[
\delta_{1,a}=(1-h_{1,a}^2)\odot\widehat W^\top\delta_{2,a},
\qquad \delta_{2,a}=W_3\odot(1-h_{2,a}^2).
\]

Let \(V=\dot{\widehat W}\) be evaluated from (2). Then the following are explicit current-state computations:

\[
\dot h_{1,a}=(1-h_{1,a}^2)\odot\frac{\dot W_1x_a}{\sqrt d},
\]

\[
\dot h_{2,a}=(1-h_{2,a}^2)\odot(Vh_{1,a}+\widehat W\dot h_{1,a}),
\]

\[
\dot f_a=\frac{\dot W_3^\top h_{2,a}+W_3^\top\dot h_{2,a}}n,
\qquad \dot r_a=\dot f_a,
\qquad \dot\rho=\frac{M^{-1}\sum_a r_a\dot f_a}{\rho},
\]

\[
\dot\delta_{2,a}=\dot W_3\odot(1-h_{2,a}^2)
-2W_3\odot h_{2,a}\odot\dot h_{2,a},
\]

\[
\dot u_a=\frac{\dot r_a\delta_{2,a}+r_a\dot\delta_{2,a}}{\rho}
-u_a\frac{\dot\rho}{\rho}.
\tag{4}
\]

Thus the computation order is: current forward/backward responses and moment projections; \(V,\dot W_1,\dot W_3\); response derivatives and (4); the chosen \(g\); finally \(\dot q,\dot H,\dot U,\dot G\). No \(\dot G\) is needed to obtain (4). There is no implicit clock equation in this ordering.

If derivatives of \(\delta_1\) are additionally needed, they too are explicit:

\[
\dot\delta_{1,a}=-2h_{1,a}\odot\dot h_{1,a}\odot(\widehat W^\top\delta_{2,a})
+(1-h_{1,a}^2)\odot(V^\top\delta_{2,a}+\widehat W^\top\dot\delta_{2,a}).
\]

For finite dimensions, inversion is smooth on \(G\succ0\), and these response formulas are smooth on \(\rho>0\). Euclidean norms and finite maxima used for the clock are locally Lipschitz. Hence the complete resulting right-hand side is locally Lipschitz on that open state domain, giving a unique local solution through each admissible state. This is a local conclusion, without a global continuation assertion.

For another model or greater depth, the same conclusion requires checking that all reconstructed weight derivatives are first computable without \(g\), after which the ordinary finite forward and backward differentiation graph may be traversed. The prompt alone does not establish a separate arbitrary-depth approximation theorem.

## What the arclength clock controls

Fix positive scales \(L_{h,a},L_{u,a}\), and stack

\[
z=\bigl((h_a/L_{h,a})_a,(u_a/L_{u,a})_a\bigr).
\]

Choosing \(g=\rho+\|\dot z\|_2\) after the preceding calculations gives

\[
\left\|\frac{dz}{dq}\right\|_2=\frac{\|\dot z\|_2}{\rho+\|\dot z\|_2}\leq1.
\]

It follows by integration that every actual \(h_a\) is \(L_{h,a}\)-Lipschitz in \(q\), and every actual \(u_a\) is \(L_{u,a}\)-Lipschitz. A finite maximum of the corresponding block rates can replace the stacked Euclidean rate if only the individual block caps are desired. An arbitrary weighted norm requires using its explicit block-domination constants; a unit bound for every unscaled block does not follow from every weighting.

The constant prefix joins \(h_a\) continuously at \(q=1\), so \(h_a\) has the same Lipschitz bound on the whole encoded interval. The zero prefix for \(u_a\) generally jumps by \(u_a(0)\) at \(q=1\). The whole encoded \(u_a\) is piecewise Lipschitz, not globally Lipschitz. Adding a derivative-based clock does not remove this jump.

If instead \(g=\rho\), then \(d\mu=d\tau\) throughout the full encoded interval and

\[
G=qD.
\]

This also follows directly from the Gram ODE because \(TD+DT^\top=ee^\top-D\): its diagonal entries are \(2k/(2k+1)\) and its off-diagonal entries are one. The usual unweighted shifted Legendre formula is recovered for this special clock. The adaptive clock generally has a nonconstant weight and does not have that orthogonality.

## A weighted finite-clock approximation bound

Here is one elementary, deliberately nonoptimal bound; it is not an asserted spectral rate. Fix a time, write \(N=P-1\geq1\), and let \(L_h,L_u\) be the clock Lipschitz constants of a particular pair of histories. Put \(b=\|u(0)\|_2\), and define the vector \(L^2(\mu)\) projection errors \(E_h=\|h-h_P\|_{L^2(\mu)}\), \(E_u=\|u-u_P\|_{L^2(\mu)}\). Then

\[
E_h\leq \frac{L_h q\sqrt m}{2\sqrt N},
\qquad
E_u\leq \frac{L_u q\sqrt m}{2\sqrt N}
       +b\sqrt{2q}\,N^{-1/4}.
\tag{5}
\]

To prove the continuous part, normalize \(x=\tau/q\in[0,1]\). A function that is \(L\)-Lipschitz in \(\tau\) becomes \(Lq\)-Lipschitz in \(x\). Its Bernstein polynomial of degree \(N\) is the expectation of its value at \(K/N\), where \(K\) has the binomial distribution with parameters \(N,x\). The Euclidean approximation error is bounded by

\[
Lq\,\mathbb E|K/N-x|
\leq Lq\sqrt{x(1-x)/N}\leq Lq/(2\sqrt N).
\]

Multiplication by \(\sqrt m\), followed by the least-squares optimality of the weighted projection, gives the continuous contribution in (5). This proof works for vector functions by applying the triangle inequality inside the expectation.

For the jump, decompose

\[
u(\tau)=v(\tau)+u(0)\mathbf1_{\{\tau\geq1\}},
\]

where \(v=0\) on the prefix and \(v=u-u(0)\) on actual history. Then \(v\) is globally \(L_u\)-Lipschitz. Set \(a=1/q\) and let \(B_N\) be the Bernstein polynomial of \(\mathbf1_{\{x\geq a\}}\). For \(x\ne a\), its error is a binomial threshold-crossing probability. Its absolute value is at most

\[
\min\left\{1,\frac{1}{4N|x-a|^2}\right\},
\]

because a crossing requires \(|K/N-x|\geq|x-a|\), and Markov's inequality applied to the square uses variance \(x(1-x)/N\leq1/(4N)\). The squared error is no larger than the absolute error. Its integral over \(x\in[0,1]\) is at most its integral over the real line, namely \(2/\sqrt N\). Since \(d\mu\leq d\tau=q\,dx\), the jump approximation has \(L^2(\mu)\) error at most \(b\sqrt{2q}N^{-1/4}\). Adding it to the continuous approximation and using projection optimality proves (5).

Finally, (1) and Cauchy--Schwarz yield the useful reconstruction estimate

\[
\|\mathcal J-S\|_F\leq E_uE_h.
\tag{6}
\]

Indeed the Frobenius norm of an outer product is the product of the Euclidean norms, so its integral is bounded by the product of the two \(L^2\) norms. Equations (5)--(6) prove convergence of the projected cross-history at fixed finite \(q\), including the prefix jump. Their constants depend on the clock horizon, history scales, and initial jump. A sequence of adaptive closures indexed by \(P\) needs uniform control of those quantities before this can be used as a convergence theorem for that sequence.

These \(L^2\) statements do not themselves make the endpoint defect (3) small. At \(t=0\), for example, \(u_p=0\) for every \(P\), even when the actual \(u(0)\ne0\). For a general polynomial approximant \(v\), endpoint control instead has the form

\[
\|h(q)-h_p\|_2\leq\|h(q)-v(q)\|_2
+\sqrt{e^\top G^{-1}e}\,\|h-v\|_{L^2(\mu)},
\]

and similarly for \(u\). The endpoint evaluation factor is an additional quantity requiring analysis.

An alternative route to trajectory convergence can use (6) directly in the integrated weight equation: \(\widehat W=W_0-c\sum_a\mathcal J_a+c\sum_a(\mathcal J_a-S_a)\). If all other weight equations are exact at the current reconstructed state, the original finite vector field is Lipschitz with constant \(L\) on a common region, and the full additive integral-equation error is uniformly at most \(\varepsilon_P\) on \([0,T]\), comparison gives a trajectory error at most \(\varepsilon_P e^{LT}\). Those common-region and uniform-error assumptions are additional proof obligations; they have not been established here.

## Boundaries of this check

- The division by \(\rho\) and its derivative is valid only on \(\rho>0\). Even when \(u\) stays bounded as the residual approaches zero, its derivative need not have finite total variation. No continuation convention at a zero is specified by these equations.
- Finite physical time and positive residual before an endpoint do not imply finite clock length at that endpoint. For example, a residual vector proportional to \(e^{-1/(T-t)^2}(\cos(1/(T-t)),\sin(1/(T-t)))\) extends smoothly to zero at \(T\), but its normalized direction makes infinitely many turns and has infinite arclength. This is a kinematic example showing why regular residuals alone are insufficient; it is not claimed to be a trajectory of the supplied network.
- On each compact interval where the finite state remains regular and \(\rho\) remains positive, the rates above are finite and the local clock construction applies. A bound on \(\int\|\dot z\|\,dt\), or on \(q(T)\), requires further dynamical information. Energy control of an unnormalized residual does not by itself provide that bound.
- The common Gram matrix adds a \(P\times P\) state and linear solves. No numerical stability, runtime, memory advantage, width independence, or favorable order-versus-accuracy complexity was measured or proved. A large clock or polynomial order can make the monomial-equivalent polynomial geometry poorly conditioned despite exact positive definiteness.
- These are finite-sample, finite-width statements. Population versions, infinite-width limits, uniform sample/width constants, and interchanges of limits require separate integrability, regularity, and stability assumptions.

## Additional scoped audit of the design note

The supervisor subsequently authorized reading only sections 4, 6, 7, and the claim-status passage of RESPONSE_CLOCK_DESIGN.md. The audited snapshot's SHA-256 was 30beb2f34dc8b1d176002800e7ee8920c711964c11bc24e18bd7d5563ceeb99f.

Section 4 has the correct lower-triangular indices and source factors: a column \(k\) of \(HT^\top\) is \(\sum_{j\leq k}T_{kj}H_j\). For the unweighted moving-coordinate history \(b=(r\delta)/g\), its stated derivative \(db/dL=(r\delta)^{\cdot}/g^2-(r\delta)\dot g/g^3\) is correct wherever the rate is differentiable. It correctly identifies the potential clock dependence of that history and the resulting additional causality obligation.

Section 6's matching-prefix repair is exact for the physical integral. For the weighted version, initialize \(U=[u(0),0,\ldots,0]\), retain the stated \(H,G\), and reconstruct

\[
\widehat W=W_0-c\sum_a\bigl(S_a-u_a(0)h_a(0)^\top\bigr).
\]

The prefix contribution is the constant rank-one matrix \(u_a(0)h_a(0)^\top\), its subtraction restores the original initial weight, and its time derivative is zero. Thus cancellation and causality persist. Both histories now join continuously, and the jump term in (5) is unnecessary. This is a different finite-order closure from the original zero-prefix closure and has not been compared experimentally here.

Section 7's orientation, Gram equations, cancellation, positive-definiteness argument, and causal order agree with this check. Two precision changes were sent to the supervisor: specify the polynomial argument as \(p(\xi/L(t))\), with stored actual coordinate \(\xi=1+\tau(s)\); and require the selected stacked norm to dominate each scaled block norm, for example a Euclidean stack or the maximum of the block Euclidean norms. Without the latter convention, an arbitrary weighted norm does not imply the asserted individual derivative caps.

The assigned passages make no unjustified transfer of uniform-Legendre spectral rates to the weighted measure. Their limited claim of a derived possible finite solver, with conditioning, length, and tracking still open, is appropriate. The claim-status assertion about weighted Gram reconstruction and derivative cancellation is supported. Unrelated theorems mentioned in the status passage were outside this audit's supplied mathematical inputs and were not checked.

The final assigned sections were reread after correction. The reviewed design SHA-256 is 3a54e6207cd208e00c2ccbd066484bd7c79ed1065aca60250ae8ceaf89affd8d. The polynomial argument and block-norm domination are now explicit, and section 7 gives the correct matching-prefix initialization and constant subtraction. Those scoped corrections are resolved; the algebraic, causality, prefix-repair, and claim-limitation conclusions above apply to this final snapshot. No additional scientific sections were read.
