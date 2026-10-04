# Direct finite-cavity comparison with the Gaussian population

2026-10-03. Scoped continuation in the existing study. No experiments,
manuscript changes, or other studies were used. This is collaborative
research, not a promotion review. The source was initially developed independently;
root-agent messages on represented Gaussian responses were incorporated before
this freeze, so the final note is a collaborative construction.

**Conclusion.** The established carrier maximum permits a substantially
sharper finite insertion calculation: conditional Gaussian bounds can be
made uniform in arbitrary bounded insertion controls by bounding the
two-time response kernels first. The resulting local nonlinear insertion
remainder is
\(n^{-1/2}\exp\{C\sqrt{\log(e+n)}\}\), rather than the coarse
polynomial remainder used to establish the carrier theorem. This yields
explicit approximate Gaussian/response equations for a tagged neuron.
It does **not** yet identify their random covariance and response kernels
with the population kernels at that rate. A first-chaos representation
removes inverse Grams from the population response, and an exact first-step
calculation shows how represented responses can avoid an apparent fourth
activation derivative requirement. The general quantitative bias closure
remains open.

## 1. Contract and inputs

Keep the exact model of `DEPTH_EXTENSION_RESULT.md`: fixed depth \(L\),
fixed finite compatible sphere data, canonical independent Gaussian
initialization, zero stored readout, squared loss with mobilities
\((n,1,\ldots,1,n)\), and sufficiently small fixed labels. The
activations have bounded first three derivatives and may have linearly
growing values. The positive initialized feature-Gram condition is imposed
on the exact compatible data quotient as in that source. Write its fixed
positive sample weights as \(p_a\), with \(\sum_a p_a=1\).

The intended, still unresolved conclusion is
\[
 \left(\int\sup_{t\ge0}|f_n(t,x)-f_\infty(t,x)|^2\,d\mu(x)\right)^{1/2}
 \le C_{\delta,\mu}n^{-1/2}e^{K\sqrt{\log(e+n)}}
 \tag{1}
\]
with probability at least \(1-\delta\), for every sufficiently large
\(n\), and every fixed query law with finite second moment. No clipping
or additional trained-moment hypothesis is introduced.

The scientific inputs used here are the three assigned study sources,
the complete relevant finite insertion and unbounded-value calculations
in `DEPTH_RESPONSE_MODULUS.md`, `DEPTH_INSERTION_CHECK.md`, and
`UNBOUNDED_ACTIVATION_CANDIDATE.md`, the manuscript's model definition,
and the complete Gaussian-population construction and transfer argument
in `paper/proof_alltime.tex`, together with the whole-input passage in
`paper/proof_tracking.tex`. The global notation contract was read.

The local calculation below uses the existing full/cavity physical tube,
the already proved all-time forward and backward coordinate maximum,
and the older uniform fixed-deletion comparison. It does not claim to
reprove those inputs. In particular it uses the old, coarse insertion
result to establish its good cavity events before improving the insertion
rate. There is no bootstrap of the carrier theorem from the improved
rate.

## 2. The population object that must be matched

The manuscript constructs each initialized population operator and its
actual Hilbert-space adjoint from consistent finite Gaussian programs.
For a forward query \(h\) and reverse query \(u\), its source rule is
\[
 \mathscr W h=\xi_h+\sum_s u_s\,\mathbb E\partial_{\zeta_s}h,
 \qquad
 \mathscr W^*u=\zeta_u+\sum_r h_r\,\mathbb E\partial_{\xi_r}u.
 \tag{2}
\]
The sums run over earlier calls of the opposite orientation. Within each
orientation the source covariance is the corresponding input inner
product, for example
\(\mathbb E\xi_h\xi_v=\mathbb E hv\). Distinct source groups and
the roots are independent. Source derivatives hold previously computed
deterministic expectations and covariances fixed.

Finite population Euler programs use the same rank-one parameter updates
as the dense model, replacing normalized coordinate pairings by
expectations. The source covariances and the response coefficients are
computed causally. Small total residual activity gives uniformly bounded
Gaussian moments of the population fields. Euler consistency and a
reference-tail comparison construct a unique strong all-time operator
flow. The finite-array transfer first fixes the Euler program and then
sends width to infinity; it provides no width rate for a growing program.

Thus a direct quantitative comparison must control both the source
covariances and the response in (2). Replacing the reverse initialized
matrix action by fresh independent noise would omit the second term and
change the target.

## 3. A uniform Gaussian-kernel lemma

Write
\[
 A_n=\exp\{C\sqrt{\log(e+n)}\},\qquad
 \varepsilon_n=n^{-1/2}\exp\{C'\sqrt{\log(e+n)}\}.
 \tag{3}
\]
Constants in different occurrences may be enlarged a fixed number of
times. Polynomial logarithmic factors and products of a fixed number
of these envelopes remain of the displayed form.

Condition on a cavity initialization. Let \(x,y\) be its independent
omitted \(N(0,I_n/n)\) vectors. Suppose a fixed finite list of
matrix-valued kernels \(K(t,s)\), \(0\le s\le t\le T_n\), has
operator norm at most \(A_n\), output dimension at most \(Cn^c\),
and time Lipschitz constants at most \(n^cA_n\), with
\(T_n=C_T\log(e+n)\). Include analogous one-time kernels.
Then, for any fixed \(D>0\), outside a conditional event of probability
at most \(n^{-D}\),
\[
 \sup_{t,s}\|K(t,s)x\|_\infty\le\varepsilon_n,
 \quad
 \sup_{t,s}\|K(t,s)x\|_2\le C A_n,
 \tag{4}
\]
where the second bound only requires bounded operator norm and
\(\|x\|_2\le C\). For square kernels \(R\) with these bounds,
\[
 \sup_{t,s}\left|x^\top R(t,s)x-\frac1n\operatorname{tr}R(t,s)\right|
 +\sup_{t,s}|x^\top R(t,s)y|\le\varepsilon_n.
 \tag{5}
\]

Here is the quantitative proof. At a fixed node each coordinate in (4)
has variance at most \(A_n^2/n\). The Gaussian quadratic-form bound,
using \(\|R\|_{\rm HS}\le\sqrt n A_n\), has tail
\[
 2\exp\left[-c\min\left\{\frac{nu^2}{A_n^2},
                                       \frac{nu}{A_n}\right\}\right].
 \tag{6}
\]
Take \(u=C_DA_n\sqrt{\log(e+n)/n}\). A sufficiently fine
polynomial time grid contains only polynomially many nodes and
coordinates; the Gaussian and quadratic tails dominate that count.
On \(\|x\|_2+\|y\|_2\le C\), interpolation from a mesh
\(n^{-c'}\), with fixed sufficiently large \(c'\), costs less than
\(u\). The trace interpolation follows from
\(|\operatorname{tr}R|/n\le\|R\|_{\rm op}\). This proves the
lemma, absorbing its logarithm into \(\varepsilon_n\).

The useful consequence is uniformity over **all** scalar controls of
bounded amplitude. For \(|a(s)|\le M_n\),
\[
 \left\|\int_0^tK(t,s)x\,a(s)\,ds\right\|_\infty
 \le T_nM_n\sup_{t,s}\|K(t,s)x\|_\infty.
 \tag{7}
\]
Likewise the centered quadratic integral is bounded by
\(T_nM_n\) times (5). Controls can be chosen after observing
\(x,y\); no control net or time regularity of the controls is needed.
This statement applies to kernels of the *linearized cavity equation*.
It is not a assertion that the entire nonlinear forced trajectory is
linear in its controls.

## 4. Application to the exact finite insertion

Delete neuron \(i\) of an interior layer \(j\), removing its incoming
row and outgoing column. All normalizations remain \(n\). Use the
mobility coordinates
\(\Theta=(W^{(1)},\sqrt nW^{(2)},\ldots,\sqrt nW^{(L)},w)\),
and put \(\mathcal F_a=n f_a\). A superscript \(0\) below denotes
the autonomous rectangular cavity. Set
\[
 d_a=\delta_a^{(j+1),0},\qquad
 B_a=D_\Theta d_a,\qquad C_a=D_\Theta h_a^{(j-1),0},
 \qquad E_a=D_{e_a}d_a,
 \tag{8}
\]
where \(e_a\) is an external preactivation at layer \(j+1\).
The exact retained equation has both the forward source \(e_a\) and
reverse source \(q_a\):
\[
 \dot\Theta=-2\sum_a p_a r_a
 \left[\nabla_\Theta\mathcal F_a(\Theta,e)
       +D_\Theta h_a^{(j-1)}(\Theta)^\top q_a\right].
 \tag{9}
\]
For the full trajectory, the leading sources are
\(e_a=x_i h_{a,i}^{(j)}\) and
\(q_a=y_i\delta_{a,i}^{(j)}\). Learned incoming/outgoing increments
give additional sources of Euclidean size
\(n^{-1/2}\operatorname{polylog}n\), by the exact update integrals
and the already established coordinate maxima.

Let \(J(t,s)\) be the cavity variational propagator. The negative
gradient-Gram contribution to its generator is contractive. The remaining
Hessian has operator norm at most \(C(1+\sqrt{\log(e+n)})\),
multiplied by the integrable residual. Consequently
\[
 \sup_{s\le t}\|J(t,s)\|_{\rm op}\le A_n.
 \tag{10}
\]
The complete linear insertion is
\[
 V(t)=\sum_a\int_0^tJ(t,s)
 \{[P_a(s)+Q_a(s)]x_i a_a(s)+T_a(s)y_i b_a(s)\}\,ds,
 \tag{11}
\]
where \(a_a=h_{a,i}^{(j)}\), \(b_a=\delta_{a,i}^{(j)}\), and
\[
 P_a=-\frac{2p_a}{n}\nabla\mathcal F_a d_a^\top,
 \qquad Q_a=-2p_a r_a^0 B_a^\top,
 \qquad T_a=-2p_a r_a^0 C_a^\top.
 \tag{12}
\]
The term \(P_a\) is retained: it is the derivative of the adaptive
residual and has no residual prefactor. Its integral is bounded over
\(T_n\), costing at most an additional \(\log n\). It may be
discarded only later from a normalized trace, where its rank is one.

The kernels obtained by applying a forward Jacobian or backward derivative
to (11), and the direct external-field terms, satisfy the lemma. Their
operator norms are \(A_n\): forward Jacobians have bounded norm,
backward derivatives have polynomial logarithmic norm, and (10) controls
the propagator. Their time moduli are polynomial in \(n\). Indeed the
physical speeds give coordinate speeds bounded by
\(\sqrt n\operatorname{polylog}n\); differentiating the forward
and backward derivative recursions uses derivatives of the activation
only through order three. The generator identities
\(\partial_tJ=D F_0(t)J\),
\(\partial_sJ=-J D F_0(s)\) control the remaining time derivatives.
The incoming-row adjoint probes are bounded linear transforms of \(y_i\)
and are included in the same Gaussian event.

It follows that all linear forward, backward and readout variations have
Euclidean norm at most \(A_n\) and coordinate maximum at most
\(\varepsilon_n\). This holds for arbitrary actual controls within
their proved \(C\sqrt{\log(e+n)}\) amplitudes.

For completeness the nonlinear closure can be checked without hiding a
growing linear coefficient. Write
\(U=\Theta-\Theta^0-V\), \(u=\sup_{s\le t}\|U(s)\|_2\).
For a linear field variation \(v\) and a remainder field \(u_0\),
\[
 \|v\odot v\|_2\le\varepsilon_n A_n,
 \quad \|v\odot u_0\|_2\le\varepsilon_n\|u_0\|_2,
 \quad \|u_0\odot u_0\|_2\le\|u_0\|_2^2.
 \tag{13}
\]
Changed-matrix products retain \(n^{-1/2}\). Descending the backward
recursion adds only polynomial logarithmic carrier factors. For the
reverse force, the reference lower adjoint probe has coordinate maximum
\(\varepsilon_n\). The checked probe subtraction gives, with
\(N=A_n+u\), a derivative difference bounded by
\[
 C\{\varepsilon_n(N+N^2)+(N+N^2)/\sqrt n\}.
 \tag{14}
\]
The scalar residual's second Taylor remainder is
\(A_nN^2/n\). Multiplying by the original gradient, of norm
\(C\sqrt n\), gives \(A_nN^2/\sqrt n\); the product of first
residual and gradient variations has the same scale. This accounts for
the residual terms without their own activity prefactor. Integrating
those over \(T_n\), the residual-weighted terms over bounded activity,
and applying (10), gives after enlarging the envelope
\[
 u\le A_n\{n^{-1/2}+n^{-1/2}u+u^2\}.
 \tag{15}
\]
At the proposed first attainment \(u=2A_n/\sqrt n\), the last two
terms are \(o(A_n/\sqrt n)\), because any fixed product of the
envelopes is \(n^{o(1)}\). Continuity therefore proves
\[
 \sup_{t\le T_n}\|\Theta(t)-\Theta^0(t)-V(t)\|_2
 \le n^{-1/2}e^{C\sqrt{\log(e+n)}}.
 \tag{16}
\]
It also proves this rate for the nonlinear forward and backward
reconstruction remainders. Coordinate differences between the retained
full fields and cavity fields have this rate, whereas their ordinary
Euclidean differences may be \(A_n\).

There is no conditioning on a full-network good event in (4)--(6).
The Gaussian bounds are applied conditional on the cavity roots, with
deterministic constants on the cavity's own good set. The existing coarse
fixed-deletion comparison transfers the established full-network
coordinate maximum and tube to every singleton cavity on one event of
probability tending to one. Conditional exceptions can then be unioned
over the \(Ln\) deletions by choosing \(D>3\). Intersecting these
events afterward preserves the argument. This avoids needing a numerical
rate for the complement of the older carrier event.

The first layer omits the incoming-row term and uses its exact Gaussian
input root. At the top layer the omitted prediction offset
\(w_i h_{a,i}^{(L)}/n\) multiplies both the retained gradient and
reverse force. Its Euclidean forcing is
\(n^{-1/2}\operatorname{polylog}n\), already allowed in (15).
No outgoing Gaussian column is introduced at that layer.

The same event can include scalar prediction linear kernels. Their
Gaussian scale is \(A_n/n\), since the prediction gradient is
\(\nabla\mathcal F_a/n\). The scalar quadratic Taylor error and
the contribution of (16) are also \(A_n/n\). Thus deleting one
neuron changes each **training** prediction by at most
\(n^{-1}e^{C\sqrt{\log(e+n)}}\) on this logarithmic horizon.
This last statement is not asserted uniformly over arbitrary query laws.

Choose \(C_T\kappa>3\). The crude physical coordinate-tail estimates
already used in the study extend (16)'s coordinate consequences past
\(T_n\), at a smaller error. No bound on infinite-time integration
of the residual-free term \(P_a\) is needed.

## 5. Explicit approximate scalar response equations

Suppress the cavity superscript on the coefficients defined in (8), and
set
\[
 \begin{aligned}
 Q^h_{ab}(t,s)&=\frac1n h_a^{(j-1),0}(t)^\top h_b^{(j-1),0}(s),\\
 Q^\delta_{ab}(t,s)&=\frac1n d_a(t)^\top d_b(s),\\
 R^h_{ab}(t,s)&=\frac1n\operatorname{tr}[C_a(t)J(t,s)C_b(s)^\top],\\
 R^\delta_{ab}(t,s)&=\frac1n\operatorname{tr}[B_a(t)J(t,s)B_b(s)^\top],\\
 e_a(t)&=\frac1n\operatorname{tr}E_a(t).
 \end{aligned} \tag{17}
\]
All these are functions of retained initialization. Conditional on it,
\[
 \xi_{a,i}(t)=y_i^\top h_a^{(j-1),0}(t),\qquad
 \zeta_{a,i}(t)=x_i^\top d_a(t)
 \tag{18}
\]
are independent centered Gaussian groups with covariances \(Q^h\)
and \(Q^\delta\), respectively.

Equations (11), (5), and the exact integrated incoming/outgoing updates
give, uniformly on \([0,T_n]\),
\[
 \begin{aligned}
 z_{a,i}^{(j)}(t)
 &=\xi_{a,i}(t)-2\sum_b p_b\int_0^t r_b^0(s)
       [Q^h_{ab}(t,s)+R^h_{ab}(t,s)]
                     \delta_{b,i}^{(j)}(s)\,ds+O(\varepsilon_n),\\
 k_{a,i}^{(j)}(t)
 &=\zeta_{a,i}(t)+e_a(t)h_{a,i}^{(j)}(t)
       -2\sum_b p_b\int_0^t r_b^0(s)
       [Q^\delta_{ab}(t,s)+R^\delta_{ab}(t,s)]
                     h_{b,i}^{(j)}(s)\,ds+O(\varepsilon_n).
 \end{aligned} \tag{19}
\]
The omitted cross forms in \(x_i,y_i\) have zero conditional mean
and are bounded by (5). The forward field has no instantaneous reverse
term because lower activations change through their parameter history.
The backward field has the direct derivative \(E_a\), producing its
instantaneous term. The normalized trace containing \(P_b\) is at
most \(A_n/n\), since \(P_b\) has rank one; only this trace, not
its contribution to (11), has been absorbed into the error.

Replacing full normalized pairings and residuals in the exact learned
row/column integrals by their cavity counterparts costs
\(O(\varepsilon_n)\), by (16), RMS bounds, the coordinate controls,
and the logarithmic time horizon. This explains the cavity versions of
the coefficients in (19).

These are quantitative **random cavity equations**. They are not yet
the deterministic population equations. To use them for (1), one must
show that their covariance/response data form an approximate population
fixed point and then prove stability of that fixed point. Bounding the
traces or proving concentration of their finite-width centers does not
identify those centers.

## 6. A response representation without inverse covariance

There is an exact invariant version of the second term in (2). Fix one
finite list of forward source variables \(\xi_r\), and let \(h_r\)
be the corresponding population query fields. Their Gram matrices agree.
Consequently the map
\[
 T\left(\sum_r c_r\xi_r\right)=\sum_r c_rh_r
 \tag{20}
\]
is a well-defined isometry of their linear spans, including singular
Grams. Let \(\Pi_1\) be orthogonal projection onto the span of these
Gaussian variables in their scalar \(L^2\) space. Gaussian integration
by parts gives
\[
 \sum_r h_r\,\mathbb E\partial_{\xi_r}u
       =T\Pi_1u,
 \qquad \|T\Pi_1u\|_2\le\|u\|_2.
 \tag{21}
\]
To verify the identity without an inverse, pair
\(\sum_r\xi_r\mathbb E\partial_{\xi_r}u\) with every
\(\xi_s\). Integration by parts makes this pairing equal to
\(\mathbb E\xi_su\), which characterizes the orthogonal
projection. Null covariance directions represent zero feature vectors in
(20), so no coefficient along a null direction is needed.

This is an exact representation and a contraction at fixed source and
feature spaces. It does not itself give a comparison estimate when both
the source span and the feature realization change with width. Such a
transport estimate must preserve their joint typed laws; covariance
matrices alone do not specify how the represented response correlates
with existing feature fields.

## 7. An explicit response closure test under only C3

The apparent derivative loss is real for a naive coefficient metric:
twice differentiating the Gaussian expectation of a factor
\(\phi''(Z)\) would ask for \(\phi''''\). It is not automatically
an obstruction for a represented response.

For an exact first Euler update at the top layer, take one training
sample and step length \(\eta\). At initialization the stored
readout is zero, so hidden weights do not move in this step and
\[
 w_1=2\eta y\phi(G_q),\qquad
 \delta_1=2\eta y\phi(\xi_0)\phi'(\xi_1),
 \tag{22}
\]
where \(G_q\sim N(0,q)\), \(q>0\), and the repeated forward
call has \(\xi_0=\xi_1=G_q\) and \(h_0=h_1\). The source
covariance is singular. Nevertheless its represented response is
\[
 2\eta y h_0\,\mathbb E[(\phi'(G_q))^2+\phi(G_q)\phi''(G_q)]
 =\frac{2\eta y h_0}{q}\,
                \mathbb E[G_q\phi(G_q)\phi'(G_q)].
 \tag{23}
\]
This is one-dimensional Gaussian integration by parts. It is well-defined
for the allowed linear growth and bounded derivatives. On any fixed
interval \(0<c\le q\le C\), the right side is Lipschitz in \(q\),
by differentiating the Gaussian density; all required weighted moments
are finite. It needs no fourth activation derivative.

The cancellation persists when a new small direction is present. Let
\(v\perp h_0\) be a unit feature vector, put
\(h_1=h_0+\epsilon v\), and couple sources by
\(\xi_0=G_q\), \(\xi_1=G_q+\epsilon g\), where \(g\) is an
independent standard normal. For the same scalar expression in (22),
the coefficient multiplying \(h_0\) in the represented response is
\[
 \mathbb E[\phi'(G_q)\phi'(G_q+\epsilon g)
             +\phi(G_q)\phi''(G_q+\epsilon g)]
 =q^{-1}\mathbb E[G_q\phi(G_q)\phi'(G_q+\epsilon g)].
 \tag{24}
\]
Taylor's formula applied to \(\phi'\), using bounded \(\phi'''\)
and the zero mean of \(g\), bounds the change in (24) by
\(C\epsilon^2\). The remaining term is
\(\epsilon v\,\mathbb E[\phi(G_q)\phi''(G_q+\epsilon g)]\),
whose coefficient is bounded. Thus the represented response behaves
regularly through this rank change. An argument requiring separate
second covariance derivatives of every response coefficient misses this
cancellation.

This test is an exact local calculation. It does not prove that every
time-history response admits a uniformly bounded integration-by-parts
formula of this kind.

## 8. Remaining bias obstruction and a covariance-coupling caution

A successful continuation of this route needs a quantitative estimate for
the *represented* response in (21), compatible with the empirical
covariance kernels in (17) and the nonlinear scalar histories in (19).
It must account for the variation of the response traces, rather than
merely bound them by a constant. The needed conclusion has the schematic
form
\[
 \text{finite self-consistency defect}
 \le n^{-1/2}e^{C\sqrt{\log(e+n)}},
 \tag{25}
\]
in a specified metric controlling the population response map. Equations
(16) and (19) identify and bound a local source of this defect; they do
not establish (25) for the entire population fixed point.

Temporal regularity can help Gaussian covariance coupling. A direct
assignment of Fourier decay bounds to covariance eigenvectors would be
invalid, because those bases need not agree. The following invariant
calculation, suggested by the coordinator and checked here, removes that
particular objection for independent sampling. Let \(X\) be a
finite-dimensional path representation with \(Q=\mathbb E XX^\top\),
let \(K\) be any positive definite matrix, and assume
\(X^\top KX\le B^2\) almost surely. In an eigenbasis of \(Q\),
with positive eigenvalues \(\lambda_i\),
\[
 \begin{aligned}
 \sum_{i,j}\frac{\mathbb E X_i^2X_j^2}{\lambda_i+\lambda_j}
 &\le\frac12\mathbb E(X^\top Q^{-1/2}X)^2\\
 &\le\frac{B^2}{2}\mathbb E
       [X^\top Q^{-1/2}K^{-1}Q^{-1/2}X]
 =\frac{B^2}{2}\operatorname{tr}(K^{-1}P_Q).
 \end{aligned} \tag{26}
\]
Here inverses of \(Q\) act only on its range and \(P_Q\) is that
range projection. The first inequality is
\(\lambda_i+\lambda_j\ge2\sqrt{\lambda_i\lambda_j}\);
the second is weighted Cauchy--Schwarz with \(K\); the last uses the
covariance identity and cyclicity of trace. Null coordinates of \(X\)
vanish almost surely. Thus an empirical covariance from independent
copies has expected quadratic covariance error at most
\(B^2\operatorname{tr}(K^{-1})/(2n)\) in this weighted metric.
No common basis or relative fourth-moment bound is assumed.

A temporal Sobolev choice of \(K\) can have summable inverse trace.
For the actual finite network, however, the paths are dependent, and a
proof-only truncation or good-set extension must preserve the needed
covariance algebra. Equation (26) does not supply that dependent
finite-network estimate. Nor do absolute carrier tails alone give the
almost-sure Sobolev bound in (26). These remain application obligations;
the earlier common-basis objection is resolved for the independent
bounded-Sobolev-norm calculation.

There are also two scope requirements for a final theorem. First,
localization to a good event whose probability tends to one must not
silently become an unconditional expectation estimate with a root-width
error; the bad-event probability has no supplied numerical rate.
Second, fixed training or test lists do not by themselves imply (1).
A query-wise comparison must retain a squared bound proportional to
\((1+\|x\|/\sqrt d)^2\), or another argument using only the
authorized second query moment. Polynomially growing weak-test
derivatives cannot be integrated by adding higher moments of \(\mu\).

The present status is therefore: the local finite insertion estimate and
the equations (19) have a near-root remainder; the first-chaos response
identity and the singular first-step cancellation are exact; the
quantitative identification of the random cavity kernels with the
canonical Gaussian operator population, and hence (1), remain open.
