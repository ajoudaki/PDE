# Nonzero hidden descent at canonical order-one initialization

2026-09-19. This bounded followup uses only this study's
CANONICAL_FEATURES.md (SHA-256
b202a5344b2ba5bb845e2a907e3347467a7dc65115c68a155af9d367090b53f3)
and MODEL_AND_GEOMETRY.md (SHA-256
d3ed7af3baadbb55e190e2423f0751b11da5ba24ef0c8fcc5c47f627ef57ff89),
both read completely. It is a post-comparison author derivation, not an isolated
review. No experiment or outside scientific input is used.

The conclusion is that both hidden-block components of \(\nabla J(h_0)\) are
nonzero for the two canonical coordinate directions with every choice of binary
labels and positive masses. This persists on an open set of nearby two-input
configurations. The middle-block assertion also holds for every single effective
nonzero circle input. Consequently a flow whose hidden velocity at \(h_0\) is
\(-\nu\nabla J(h_0)\), with \(\nu>0\), moves both hidden blocks initially in the
two-coordinate example.
This is a statement about the \(J\)-driven hidden rule; it does not assert that
the original zero-readout squared-loss gradient flow has nonzero hidden velocity
at time zero.

## Two coordinate directions

Retain the exact canonical marks, ridge \(\eta=1/4096\), whitening, and initialized
matrix \(D\). The physical hidden Hilbert metric is
\(\|(\delta w,\delta M)\|^2=\|\delta w\|_{L^2}^2+\|\delta M\|_F^2\).
Consider the represented hidden path

\[
h(s)=(g,sD),\qquad s>0,\qquad h(1)=h_0.
\]

Only the moving matrix changes; none of the dictionary moments or ridge factors
is recomputed. Let \(b=F(1)>0\), where the continuous odd strictly increasing
function \(F\) and the independent symmetric upper coordinates
\(Z_i=\tanh\xi_i\), \(\xi_i\sim N(0,v)\), are proved in CANONICAL_FEATURES.md.
Linearity of the preactivation in \(M\), and \(F(0)=0\), give exactly

\[
H_{h(s)}(\sqrt2e_i)=\tanh(sbZ_i),\qquad i=1,2.
\]

These fields are independent and centered. Define

\[
a(s)=E[\tanh^2(sbZ)].
\]

For \(s>0\), \(a(s)>0\), and differentiation under the expectation yields

\[
a'(s)=2bE[Z\tanh(sbZ)\operatorname{sech}^2(sbZ)]>0.       \tag{1}
\]

Indeed the derivative integrand has absolute value at most \(2b\), which permits
dominated differentiation. It is strictly positive for every \(Z\ne0\);
\(P(Z=0)=0\) because \(\xi\) has a nondegenerate Gaussian density.

For arbitrary \(\mu_i>0\), \(\mu_1+\mu_2=1\), and \(y_i\in\{-1,1\}\), use the
weighted definitions from MODEL_AND_GEOMETRY.md:

\[
Y_i=\sqrt{\mu_i}y_i,\qquad
K_{h(s)}=\begin{pmatrix}\mu_1a(s)&0\\0&\mu_2a(s)\end{pmatrix}.
\]

Therefore the exact normalization is

\[
J(h(s))=\frac12Y^TK_{h(s)}^{-1}Y
       =\frac{y_1^2+y_2^2}{2a(s)}
       =\frac1{a(s)},\qquad
\frac{d}{ds}J(h(s))\bigg|_{s=1}=-\frac{a'(1)}{a(1)^2}<0. \tag{2}
\]

In particular the two-input value is \(1/a(s)\); the value \(1/(2a(s))\) applies
to one effective binary-labeled input. Positive masses cancel from both formulas.

The positive-Gram neighborhood and differentiability of \(J\) are established
in MODEL_AND_GEOMETRY.md. Its chain rule and the stated physical metric make
(2) precisely

\[
\langle\nabla_M J(h_0),D\rangle_F=-\frac{a'(1)}{a(1)^2}<0. \tag{3}
\]

Thus \(D\ne0\), \(\nabla_MJ(h_0)\ne0\), and

\[
\|\nabla_MJ(h_0)\|_F\ge
\frac{a'(1)}{a(1)^2\|D\|_F}>0.
\]

If a hidden evolution satisfies \(\dot h(0)=-\nu\nabla J(h_0)\), \(\nu>0\), then
\(\dot M(0)\ne0\). Differentiability gives
\(M(t)=D-\nu t\nabla_MJ(h_0)+o(t)\), so \(M(t)\ne D\) for all sufficiently small
positive \(t\).

## The first-layer component is nonzero as well

Now vary the first layer alone, along \(\widetilde h(s)=(sg,D)\), \(s>0\).
This is an admissible Hilbert-space path, since \(E|g|^2=2\).
The exact raw-contraction derivation in CANONICAL_FEATURES.md, section 1, uses
the fixed odd strictly increasing bounded function \(\chi\) and gives

\[
H_{\widetilde h(s)}(\sqrt2 e_i)=\tanh(k(s)Z_i),\qquad
k(s)=\frac{E[\chi(G)\tanh(sG)]}{\tau+\eta},\qquad k(1)=b.
\]

Indeed lower coordinates from the other independent coordinate pair have zero
contraction with \(\tanh(sg_i)\), and the two contractions from coordinate \(i\)
combine into \(\chi(g_i)\), exactly as in equations (3)–(6) of that source.
No initialization coefficient is changed.

Since \(\chi\) is odd and strictly increasing, \(\chi(G)G>0\) almost surely.
Thus \(k(s)>0\) and

\[
k'(s)=\frac{E[\chi(G)G\operatorname{sech}^2(sG)]}{\tau+\eta}>0.
\]

The derivative is dominated by
\(\|\chi\|_\infty |G|/(\tau+\eta)\), which is integrable. With
\(\widetilde a(s)=E\tanh^2(k(s)Z)\), another bounded differentiation gives

\[
\widetilde a'(1)
 =2k'(1)E[Z\tanh(bZ)\operatorname{sech}^2(bZ)]>0.
\]

The same independent centered fields make the weighted Gram diagonal. Therefore
\(J(\widetilde h(s))=1/\widetilde a(s)\) for every binary label pair, and

\[
\langle\nabla_wJ(h_0),g\rangle_{L^2}
 =-\frac{\widetilde a'(1)}{a(1)^2}<0,\qquad
\|\nabla_wJ(h_0)\|_{L^2}\ge
\frac{\widetilde a'(1)}{\sqrt2\,a(1)^2}>0.
\]

Together with (3), this proves both separate hidden gradients are nonzero.
Any differentiable flow with initial hidden velocity
\(-\nu\nabla J(h_0)\), \(\nu>0\), consequently moves both hidden blocks for all
sufficiently small positive times, by the same first-order expansion.

## Persistence for nearby input configurations

For \(u\in S^1\), put \(r(u)=(F(u_1),F(u_2))\). Along the same scaling path,

\[
H_s(u)=\tanh(s\,r(u)\cdot Z),\qquad
\partial_sH_s(u)=(r(u)\cdot Z)\operatorname{sech}^2(s\,r(u)\cdot Z).
\]

The vector \(r(u)\) is continuous and bounded on the circle, and \(Z\) is bounded.
Hence these fields and their scaling derivatives are bounded uniformly for
nearby \(s\) and all \(u\), and vary continuously pointwise with \((s,u)\).
Dominated convergence shows that the unweighted two-input Gram \(G(s)\) and
its scaling derivative \(G'(s)\) depend continuously on the pair of inputs.
At \((u_1,u_2)=(e_1,e_2)\) and \(s=1\), \(G(1)=a(1)I>0\). For nearby pairs
the minimum eigenvalue remains positive, since
\(\lambda_{\min}(G)\ge a(1)-\|G-a(1)I\|_{\mathrm{op}}\).
Matrix inversion is continuous there, as follows also from
\(G^{-1}-G_0^{-1}=G^{-1}(G_0-G)G_0^{-1}\).

For every positive choice of masses, let \(W=\operatorname{diag}(\sqrt{\mu_i})\).
The exact identities \(K=WGW\), \(Y=Wy\) imply

\[
J=\frac12y^TG^{-1}y,\qquad
\partial_sJ=-\frac12y^TG^{-1}G'G^{-1}y.                 \tag{4}
\]

The right side is continuous in the input pair and equals the same strictly
negative number (2) at \((e_1,e_2)\) for all four binary label choices. Intersecting
the four corresponding open neighborhoods gives one open neighborhood in which
\(\partial_sJ|_{s=1}<0\) for every binary label choice. This conclusion holds for
all strictly positive masses, since (4) is mass-independent. Thus it covers
nearby nonorthogonal input pairs as well as the coordinate pair. It concerns two
effective examples; adding additional distinct inputs is not justified by this
continuity argument.

The first-layer scaling derivative persists in a possibly smaller neighborhood
by the same argument. Explicitly, its lower coefficient and derivative are
\(E_1[b_1\tanh(sg\cdot u)]\) and
\(E_1[b_1(g\cdot u)\operatorname{sech}^2(sg\cdot u)]\).
The latter is bounded in integrand norm by \(B_1|g|\), uniformly on the circle.
Dominated convergence makes both coefficients continuous in \((s,u)\).
The fixed bounded upper marks then give continuity of the upper fields, their
scaling derivatives, and hence the expression (4). Intersecting the four
binary-label neighborhoods for this path with those for the middle path proves
that both hidden-block gradients remain nonzero on one open neighborhood.

## One effective input

For any \(u\in S^1\), \(r(u)\ne0\). The upper variable \(Q=r(u)\cdot Z\) is bounded
and is nonzero almost surely: the zero set of this nonzero linear form is a line,
which has measure zero under the upper law's density on the open square.
Consequently

\[
a_u(s)=E\tanh^2(sQ)>0,\qquad
a_u'(s)=2E[Q\tanh(sQ)\operatorname{sech}^2(sQ)]>0
\quad(s>0).
\]

For the single effective constraint with binary label \(y\), the same mass
cancellation gives

\[
J(h(s))=\frac1{2a_u(s)},\qquad
\langle\nabla_MJ(h_0),D\rangle_F
   =-\frac{a_u'(1)}{2a_u(1)^2}<0.
\]

This includes compatible repeated or antipodal observations after the merging
specified in MODEL_AND_GEOMETRY.md. The result proves a concrete nonzero
middle-matrix descent direction; it asserts no uniform lower bound over all
datasets or an endpoint description for any training rule.
