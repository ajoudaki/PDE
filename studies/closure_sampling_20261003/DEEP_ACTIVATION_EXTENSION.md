# Strip-holomorphic activations and the augmented insertion calculation

2026-10-03. Internally checked scoped continuation in
`closure_sampling_20261003`.
The source candidate was originally frozen as `DEEP_COMPLEX_SOURCE.md`, SHA-256
`8cb98569299501b6620c76b5186e4ee2fb74093d2ac3f8183717677b10723db4`.
This supplement was itself frozen at SHA-256
`2e772fff3b7074c8cd9f5cadf158b6cc39decb42c66eee43f381a5c15b1b22e0`.
Both complete inputs passed reconstruction in
[DEEP_COMPLEX_SOURCE_CHECK.md](DEEP_COMPLEX_SOURCE_CHECK.md), SHA-256
`b91d5730d35baf7a2c1ee544fd8c3bdca134ca0680e535eec850205770b88015`;
Section 9 checks this entire supplement. The present update records that
status and explicitly lists the forward applications of incoming-row
adjoint probes already allowed in the enlarged Gaussian event. The
historical hashes preserve the exact versions before these clarifications.
The original supplement left the source file unchanged. It uses its
complete derivation,
the previously authorized and completely read deep cavity route and two
checks, the current manuscript normalization, the first frozen depth note,
and the canonical-notation and rigorous-proof instructions. At that freeze,
no other new route or review finding had been read. The full linked check
was read before this status update. No experiment, Git operation, or
manuscript edit was performed.

The results here are: precise activation hypotheses replacing every use
of tanh in the deep source proof; a local augmented-graph remainder
lemma covering its new forward-response and angular observables; and a
finite-width nonzero feature-motion certificate at every hidden layer.
The latter has an additional nonconstant-activation assumption. Compression
itself does not require positive, monotone, or nowhere-vanishing slopes.
The complete complex-source proof and this supplement are now internally
checked. This status is distinct from an independent promotion review and
does not make either document established book or manuscript material.

## 1. Activation class and canonical flow

For each hidden layer `ell=1,...,L`, let `phi_ell` be holomorphic on

\[
 \mathcal S_a=\{z\in\mathbb C:|\Im z|<a\},\qquad a>0,
\]

real valued on the real axis, and satisfy

\[
 \sup_{\ell,z\in\mathcal S_a}|\phi_\ell(z)|\le B_\phi<\infty.
 \tag{1}
\]

Both `a` and `B_phi` are fixed independently of width. A point in
`|Im z|<=a/2` admits a complex disk of radius `a/4` inside the strip.
The Cauchy integral formula therefore gives, explicitly,

\[
 \sup_{\ell,\,|\Im z|\le a/2}|\phi_\ell^{(j)}(z)|
       \le j!B_\phi(4/a)^j,\qquad j=0,1,2,3,4.
 \tag{2}
\]

Thus bounded first four derivatives on a narrowed strip are consequences
of (1), rather than additional differentiability assumptions. More generally
one may assume the displayed holomorphic derivative bounds directly on
a fixed strip. Mere real `C^3` or `C^4` regularity does not imply (1)
and is insufficient for the analytic source construction.

Let `v_a=x_a/sqrt(d)` be fixed training inputs. The finite network is

\[
 z^{(1)}(v)=Av,\quad h^{(\ell)}(v)=\phi_\ell(z^{(\ell)}(v)),
 \quad z^{(\ell)}(v)=W^{(\ell)}h^{(\ell-1)}(v),\quad
 f(v)=w^\top h^{(L)}(v)/n.
 \tag{3}
\]

The second recurrence is for `ell>=2`. Initialization is the canonical
independent Gaussian law, and `w(0)=0`. Define the residual
`r_a=f(v_a)-y_a`, the negative physical residual coefficient
`c_a=-(2/m)r_a`, and

\[
 k_a^{(L)}=w,\quad
 \delta_a^{(\ell)}=\phi_\ell'(z_a^{(\ell)})\odot k_a^{(\ell)},
 \quad
 k_a^{(\ell)}=W^{(\ell+1)\top}\delta_a^{(\ell+1)}.
 \tag{4}
\]

The last recurrence is for `ell<L`. Loss `m^{-1} sum r_a^2` and
mobilities `(n,1,...,1,n)` give

\[
 \dot A=\sum_a c_a\delta_a^{(1)}v_a^\top,\quad
 \dot W^{(\ell)}=\frac1n\sum_a c_a\delta_a^{(\ell)}
                                      h_a^{(\ell-1)\top},\quad
 \dot w=\sum_a c_ah_a^{(L)}.
 \tag{5}
\]

The required data assumption is a fixed positive gap of the limiting
initialized readout-feature Gram. It is retained explicitly. Oddness of
tanh or orthogonality of inputs is not used to silently assert that gap
for another activation.

## 2. Replacement of all tanh-specific uses

The real fitting argument uses bounded activation values, bounded first
derivatives, fixed initialized operator bounds, and the initial Gram gap.
The bounds from (2) supply all of them. For a small residual-activity
interval, readout maximum is `CS`, all backward RMS norms are `CS`,
and hidden/first-weight displacement is `CS^2`. Forward Lipschitz bounds
keep the readout Gram nondegenerate. The residual tangent matrix is a
sum of gradient Grams, so it remains positive semidefinite regardless
of the signs or zeros of the slopes. This gives the same global fitting,
finite total residual activity, and query tails as before.

The activation at a complex preactivation is safe on a fixed strip. Choose
`b_0` with `8b_0<a/2` and replace each tanh gate bound by (2). Finite
differences and Taylor remainders follow by integrating derivatives along
segments whose imaginary parts stay in the larger strip. The augmented
calculation below proves that property for the relevant perturbed segments.

The initial forward Gaussian estimate remains valid: conditional on the
preceding features, every next initialized row is a centered Gaussian
with variance `||h||_2^2/n<=B_phi^2`. It does not require centered
activation values. The first initialized matrix supplies the usual Gaussian
row bounds. The initialized Gram law uses bounded-variable concentration
and continuity of the Gaussian feature expectation, with its assumed gap.
No identity `phi(0)=0` is needed. Deleting a neuron removes its activation
coordinate and the corresponding matrix row/column; it never means replacing
its preactivation by zero.

The exact forward responses and angular derivatives are

\[
 R_b^{(\ell)}(v)=D_\Theta z^{(\ell)}(v)\nabla_\Theta F_b,
 \quad Q_b^{(\ell)}(v)=\phi_\ell'(z^{(\ell)}(v))
                                      \odot R_b^{(\ell)}(v),
 \quad J_j^{(\ell)}=\partial_{\theta_j}z^{(\ell)}(v(\theta)),
 \tag{6}
\]

where `Theta=(A,sqrt(n)W^(2),...,sqrt(n)W^(L),w)` and `F_b=n f_b`.
Their exact recursions remain

\[
 R_b^{(1)}(v)=\delta_b^{(1)}v_b^\top v,
 \quad
 R_b^{(\ell)}(v)=\delta_b^{(\ell)}
       \frac{h_b^{(\ell-1)\top}h^{(\ell-1)}(v)}n
              +W^{(\ell)}Q_b^{(\ell-1)}(v),
\]
\[
 J_j^{(1)}=A\partial_{\theta_j}v,
 \quad
 J_j^{(\ell)}=W^{(\ell)}
    [\phi_{\ell-1}'(z^{(\ell-1)})\odot J_j^{(\ell-1)}].
 \tag{7}
\]

Their endpoint derivatives, Hessian decomposition, and normalized Schatten
estimates use only products, transposes, the strip derivative bounds, and
RMS/coordinate bounds. They contain no division by `phi'`. The same is
true of both directions of the Gaussian cavity construction, the real-plus-
vertical variational estimate, the empirical carrier budget, the triangular
row trace estimates, and the initial-jet interpolation construction.

In particular, the first-layer change of variable involving `cosh^2`
in the earlier two-layer proof is not used in this deep route. Neither
`tanh'=1-tanh^2`, saturation with a particular sign, oddness, parity in
activity, injectivity, monotonicity, nor a lower bound on the slope is used.
All constants in the deep source proof may be enlarged to depend on the finite
bounds in (2). The powers of `log n` and the state-count argument do not
change. This establishes the activation replacement at every deterministic
and analytic step actually used by that proof.

## 3. An augmented graph for the new insertion observables

The following local lemma makes the passive-observable extension explicit.
It applies on a common stopped cavity/full prefix. It does not itself prove
the independent Gaussian event supplying the first variations.

Fix a cavity state and any fixed collection of training inputs and passive
queries, including complex angular values in the proposed query strip.
Construct the following graph in this order:

1. forward preactivations and features `z,h`;
2. backward carriers and responses `k,delta`, descending from the readout;
3. forward responses `R,Q` by (7), ascending through the layers;
4. angular responses `J,phi'(z) odot J`, ascending through the layers.

For each fixed query and driving sample this is an acyclic finite graph.
Its number of stages depends on depth and the fixed number of inputs, not
on width. The only primitive operations are bounded holomorphic scalar
gates, coordinate products, hidden matrix/transpose actions, and normalized
scalar pairings. An unbounded preactivation is used only as a scalar gate
argument, never as an unexplained coordinate multiplier.

Let `Lambda_n=C(log(en))^C`, where the constants may depend on fixed
depth/data/strip bounds and may increase finitely many times below. At the
reference, suppose hidden operator norms and vector RMS norms have their
physical bounds, while `k,R,J` have coordinate maxima at most `Lambda_n`.
Assume all reference preactivations lie in `|Im z|<=2b_0`.

Write the parameter perturbation as `V+U`. Here `V` is the first insertion
variation generated by the omitted Gaussian roots, and `||U||_2<=u` is
the unknown nonlinear state remainder, measured in mobility coordinates.
Suppose

\[
 \|V\|_2\le n^\alpha,\qquad \alpha=1/100,
\]

and the first variation of every displayed vector node, including direct
linear root sources, has Euclidean norm at most `Lambda_n n^alpha`
and coordinate maximum at most `Lambda_n n^{-beta}`, with
`beta=1/10`. No coordinate bound on the parameter matrix `V_H` is required.
All such matrix products retain their explicit factor `1/sqrt(n)`.

**Local augmented-graph lemma.** If `u<=n^{-1/25}`, then every displayed
vector node, after subtracting its reference value and its complete first
variation in `V+U`, has Euclidean remainder at most

\[
 E_n(u)=\Lambda_n\left[
 n^{\alpha-\beta}+n^{-\beta}u+u^2
 +n^{-1/2}(n^{2\alpha}+n^\alpha u+u^2)+n^{-1/2}\right].
 \tag{8}
\]

The last term permits the exact learned-column/row and missing-pairing
sources of the neuron deletion. The nodewise first variation produced by
`U` has Euclidean norm at most `Lambda_n u`, by differentiating the same
graph. Thus each full retained vector-node difference is bounded in
coordinate maximum by

\[
 \Lambda_n(n^{-\beta}+u)+E_n(u)=o(1).
 \tag{9}
\]

The lemma includes the `R` and `J` coordinates needed to transfer the
new full/cavity caps. It does not replace their first variation by a
crude global parameter derivative estimate.

## 4. Proof by the primitive operations

For clarity, a first variation always means the derivative at the cavity
reference with the controls held fixed. At the end, the uniform control
event permits substitution of the actual adaptive controls. The zero-source
cavity and every base coefficient remain functions of retained initialization.

**Linear propagation from `U`.** Differentiate each primitive operation.
A hidden matrix variation is `U_H/sqrt(n)`. Acting on a reference vector
of bounded RMS costs at most `C||U_H||_F`; transpose actions have the
same bound. A gate derivative is bounded by (2). A changed gate times
a carrier, forward response or angular response costs its reference
coordinate maximum, at most `Lambda_n`. A normalized pairing with a
reference vector of norm `C sqrt(n)` costs the varying vector norm
divided by `sqrt(n)`. In (7), multiplication of this scalar by a reference
response of norm `CS sqrt(n)` cancels that denominator. Finite induction
through the graph proves the asserted `Lambda_n u` bounds. This explains
every possible dimension factor in that linear estimate.

**Scalar gate.** Let the increment of its argument be
`v+u_0+e`, where `v` is the first variation from `V`, `u_0` the
first variation from `U`, and `e` a previously bounded graph remainder.
Before the node is evaluated, `||v||_infty<=Lambda_n n^{-beta}`,
`||v||_2<=Lambda_n n^alpha`, and `||u_0||_2<=Lambda_n u`.
The complex second-order integral formula, using (2), gives a pointwise
remainder bounded by a constant times `|v+u_0+e|^2`. Its basic terms obey

\[
 \|v^{\odot2}\|_2\le\|v\|_\infty\|v\|_2
                         \le\Lambda_n n^{\alpha-\beta},
\]
\[
 \|v\odot u_0\|_2\le\Lambda_n n^{-\beta}u,
 \qquad \|u_0^{\odot2}\|_2\le\Lambda_n u^2.
 \tag{10}
\]

The terms involving `e` have the same or smaller order after enlarging
`Lambda_n`: `E_n(u)=o(1)`, the first-variation coordinate maximum is
small, and there are only finitely many graph stages. The linear propagation
of `e` is also bounded by a fixed strip derivative. For a gate `phi'`
one uses `phi'''`; for its differentiated form one uses the bounded
fourth derivative available in (2). No real ordering or sign enters.
The reference strip and the coordinate-small increments ensure that the
entire scalar joining segment lies in `|Im z|<8b_0`. Thus the Taylor
formula does not presume an unverified parameter-space strip.

**Coordinate product.** If both factors vary, subtract the reference and
both first-order terms. The product of their two first variations from
`V` has Euclidean norm at most `Lambda_n n^{alpha-beta}` by putting
one factor in coordinate maximum and the other in Euclidean norm.
The `V-U` and `U-U` products give the other two terms of (10).
A reference factor times a previously bounded remainder costs at most
its reference coordinate maximum, a fixed polylogarithm. This proves the
rule for `phi'(z) odot k`, `phi'(z) odot R`, and `phi'(z) odot J`.
It is essential that the linear variations of both factors are included
in the Gaussian coordinate event; the weaker estimate `n^alpha u`
would not justify (8).

**Matrix or transpose action.** The cross term between a matrix increment
and a vector increment has norm at most

\[
 \frac{\|V_H+U_H\|_F}{\sqrt n}\,
                 \|\Delta v\|_2
 \le\Lambda_n n^{-1/2}(n^{2\alpha}+n^\alpha u+u^2),
 \tag{11}
\]

up to previously bounded remainders. The same estimate holds for a
transpose action. Reference operators propagate a vector remainder by a
fixed constant. A matrix increment acting on an already bounded remainder
has the additional `n^{-1/2}(n^alpha+u)` factor and is smaller. This
accounts for every learned hidden action in both directions of the graph.

**Normalized pairing and its product with a response.** For
`G=h_b^T h_x/n`, the pure product error from first variations has size
at most `Lambda_n(n^{2alpha}+n^alpha u+u^2)/n`. A feature remainder
paired with a reference feature costs `C E_n(u)/sqrt(n)`. The linear
pairing variation is at most `Lambda_n(n^alpha+u)/sqrt(n)`.
Multiplying its scalar second remainder by a reference `delta` of norm
`CS sqrt(n)` gives a vector of size bounded by (8). Multiplying the
scalar first variation by a changed response gives the matrix-cross scale
(11). Finally a response remainder times the bounded reference pairing
costs its own norm. This proves the rule for the first term in the
`R` recursion (7), without allowing a hidden `sqrt(n)` loss.

The first-layer formulas for `z` and `J` are linear. The first-layer `R`
is a fixed scalar input pairing times a backward response. Applying the
four rules, first forward, then backward, then to `R`, then to `J`,
proves (8)--(9). The order is finite and has no same-stage circularity. ∎

## 5. Exact direct sources for all augmented nodes

The preceding graph can represent the actual deleted-neuron observations,
not only arbitrary nearby parameter states. This identifies the source
terms that must appear in the enlarged Gaussian event.

Delete neuron `i` in layer `j<L`. Its independent initialized outgoing
column is `x`, and, when `j>=2`, its independent incoming row transposed
is `y`. Use rectangular retained layers and normalization `n` throughout.
For each training input the ordinary forward graph has external source

\[
 e_a=x h_{a,i}^{(j)}+O_{\ell^2}(n^{-1/2}\Lambda_n)
\]

at layer `j+1`; the backward graph has external source

\[
 q_a=y\delta_{a,i}^{(j)}+O_{\ell^2}(n^{-1/2}\Lambda_n)
 \tag{12}
\]

in its lower carrier at layer `j-1`. The second is absent for `j=1`.
The actual learned-column and incoming-row bounds are respectively
`CS^2/sqrt(n)` and `CSM_n/sqrt(n)`, with `M_n=CS log(en)`;
multiplication by bounded/polylogarithmic scalar controls yields (12).
These are the exact two directions of the deletion, not independent
substitutes for the trained matrices.

At a passive query, the forward source is the same `x` times the deleted
query activation. At the next layer, the forward-response graph has the
additional sources

\[
 x Q_{b,i}^{(j)}(v)
       +\delta_b^{(j+1)}\frac{h_{b,i}^{(j)}h_i^{(j)}(v)}n
       +O_{\ell^2}(n^{-1/2}\Lambda_n).
 \tag{13}
\]

The first term is the omitted component in `W Q`. The second is exactly
the missing scalar contribution to the training/query feature pairing
in (7). Its Euclidean norm is at most `CS/sqrt(n)`, because the two
activation coordinates are bounded and the response RMS is `CS`.
For angular responses, the corresponding direct source is

\[
 x\partial_{\theta_s}h_i^{(j)}(v)
                         +O_{\ell^2}(n^{-1/2}\Lambda_n).
 \tag{14}
\]

There is no normalized-pairing term in (14). Below the deleted layer,
any reverse effect on `R` is already supplied by the actual backward
source `q_a` in (12), followed by the `R` recursion. There is no omitted
extra independent force.

On the stopped domain, every scalar coefficient of `x` or `y` in
(12)--(14) has a fixed polylogarithmic cap. Its derivative along a
one-dimensional real-plus-vertical contour is at most `sqrt(n) Lambda_n`,
by differentiating the same graph with the bounded state speed and the
stopped diagonal maxima. For a fixed query-angle grid, these controls
therefore belong to the same one-dimensional Lipschitz control class as
the original insertion argument. Its net entropy is still
`n^{5/8} polylog(n)`, since only finitely many controls have been added.
A polynomial grid in the fixed number of complex angle and terminal-time
coordinates adds only `O(log n)` to log cardinality. Actual controls may
be root dependent; the Gaussian event is established uniformly before
substitution. This is why no Gaussian law is asserted for an adaptive
full-network vector.

For clarity, the enlarged linear Gaussian event also includes
`D_Theta z^(q)(v) C_a^T y` and `D_Theta h^(q)(v) C_a^T y` for all
relevant lower layers, where `C_a=D_Theta h_a^(j-1)` and `y` is the
incoming-row root at deleted layer `j`. With retained initialization and
controls fixed, both are bounded linear maps of the same independent
Gaussian root. Their coordinate and Euclidean bounds are those already
used for the first variations. These finitely many additional maps do
not change the control entropy. They explicitly supply the forward probes
when the variation of a lower derivative map is applied to `C_a^T y`.

For deletion at the top hidden layer `j=L`, there is no outgoing root.
Deleting the readout coordinate gives prediction offset
`d_a=w_i h_{a,i}^{(L)}/n` and the exact retained equation

\[
 \dot\Theta_{\rm ret}
 =-\frac2m\sum_a(r_a^0+d_a)
             [\nabla F_a^0+C_a^\top q_a],\qquad
 C_a=D_\Theta h_a^{(L-1)},\quad
 q_a=W_{i,:}^{(L)\top}\delta_{a,i}^{(L)}.
 \tag{15}
\]

The autonomous cavity uses `r_a^0` from its own retained forward pass.
The omitted-coordinate amplitudes have `|d_a|<=CS/n` and
`|delta_{a,i}^{(L)}|<=CS`. Thus the added offset-gradient force has
Euclidean size at most `CS/sqrt(n)`, and its product with the reverse
probe is at most `CS^2/n`. Integration over `O(log n)` and the weak
variational amplification keep both inside the insertion error. The
reverse source and its direct effect on the lower `R` graph remain;
they are the incoming-root terms used in the top-row trace estimate.
This treatment does not freeze or externally supply the cavity residual.

## 6. Closing the nonlinear state remainder with the graph bound

The raw training vector field depends only on `z,h,k,delta`, not on the
extra passive `R,J` nodes. Its gradient blocks are

\[
 \nabla_AF_a=\delta_a^{(1)}v_a^\top,\quad
 \nabla_{H^{(\ell)}}F_a=
            \delta_a^{(\ell)}h_a^{(\ell-1)\top}/\sqrt n,
 \quad \nabla_wF_a=h_a^{(L)}.
 \tag{16}
\]

The graph estimates and the normalized outer-product identity give a
pure gradient remainder at most `Lambda_n E_n(u)`. Each quadratic
changed-hidden-factor product retains `1/sqrt(n)`. The first and last
gradient blocks are already among the bounded vector nodes.

One can close the residual adaptation without a global Hessian shortcut.
Since `f=w^T h^(L)/n`, its pure scalar remainder is bounded by

\[
 C\frac{E_n(u)}{\sqrt n}
       +\frac{\Lambda_n}{n}(n^{2\alpha}+n^\alpha u+u^2).
 \tag{17}
\]

Multiplying (17) by the reference gradient norm `C sqrt(n)` gives
at most `Lambda_n E_n(u)`. The product of a residual first variation,
of size `Lambda_n(n^alpha+u)/sqrt(n)`, with a gradient first variation,
of size `Lambda_n(n^alpha+u)`, has the same bound. This is weaker
than the sharper normalized Hessian remainder in the original source,
but retains sufficient negative powers and explicitly accounts for
adaptation of the residual.

The reverse force in (12) still requires the independent-row probe
calculation. A reference lower adjoint probe has coordinate maximum
`n^{-beta}` and bounded Euclidean norm. Along a parameter displacement
of size `n^alpha+u`, its changed gate is multiplied by that reference
coordinate bound, while a changed hidden matrix carries `1/sqrt(n)`.
Descending through the lower network gives probe difference at most

\[
 \Lambda_n[n^{-\beta}(n^\alpha+u)
                     +n^{-1/2}(n^\alpha+u)].
 \tag{18}
\]

The resulting reverse nonlinear term is bounded by a polylogarithm times
`n^{2alpha-beta}` and the corresponding mixed terms. This is the same
independent-probe mechanism as in the authorized prior local proof; the
new `R,J` observables do not add a force to the training ODE.

Integrate the resulting remainder bound along the contour. Terms with a
reference residual integrate against mass `CS`; even if the weaker
unweighted bound (17) is used, the contour length is only `O(log n)`.
The propagator costs at most `n^{1/1000}`. At a possible first hit of
`u=n^{-1/25}`, the largest powers are

\[
 n^{2\alpha-\beta}=n^{-0.08},\qquad u^2=n^{-0.08},\qquad
 n^{\alpha-\beta}=n^{-0.09},\qquad n^{2\alpha-1/2}=n^{-0.48}.
\]

After the propagator and all logarithms, each is `o(n^{-0.04})`.
The small direct sources (12)--(15) are smaller still. This contradicts
the first hit. Substituting the resulting `u` bound into (9) gives
retained-coordinate differences at most `C_r n^{-1/30}` after absorbing
polylogarithms, including all `R,J` nodes. This supplies the new local
observable interface needed for simultaneous query-pole and response-cap
transfer. It is a local statement on common stopped prefixes, with exactly
the conditional Gaussian first-variation event of the insertion method.

## 7. Feature motion at every hidden layer

Compression only needs (1) and the initial Gram gap. A nonzero feature-
motion certificate needs an additional assumption: each `phi_ell` is
nonconstant. Take orthogonal normalized inputs `v_a=e_a`, `m<=d`,
a nonzero label vector, and an initialized feature Gram `G_0` with a
positive gap.

Because a nonconstant holomorphic function has a derivative whose zeros
are isolated, each real derivative-zero set is discrete. Every first
preactivation at a nonzero input has a continuous Gaussian distribution.
Inductively, the preceding activation vector is nonzero almost surely:
a nonconstant analytic activation has a discrete zero set, and the next
initialized row has a nondegenerate Gaussian distribution whenever that
vector is nonzero. Therefore, for all finitely many training coordinates
and layers, every initialized slope is nonzero almost surely. The square
Gaussian hidden matrices are also invertible almost surely. These claims
are about random initialized values, not a nowhere-vanishing activation.

At time zero all hidden velocities vanish. Set

\[
 v=\dot w(0)=\frac2m\sum_b y_b h_b^{(L)}(0),\qquad
 d_a^{(\ell)}=\dot\delta_a^{(\ell)}(0),\qquad
 p_a^{(\ell)}=\dot k_a^{(\ell)}(0).
 \tag{19}
\]

The Gram gap gives `||v||_2^2/n=(2/m)^2 y^T G_0 y>0`. Differentiating
(4) at zero readout yields

\[
 p_a^{(L)}=v,\qquad
 d_a^{(\ell)}=\operatorname{diag}(\phi_\ell'(z_a^{(\ell)}(0)))
                         p_a^{(\ell)},\qquad
 p_a^{(\ell)}=W_0^{(\ell+1)\top}d_a^{(\ell+1)}.
 \tag{20}
\]

Every map in this backward product is invertible almost surely. Hence
`d_a^(1)` is nonzero for every training input. With `c_a(0)=2y_a/m`,

\[
 \ddot A(0)e_a=c_a(0)d_a^{(1)},\qquad
 \ddot W^{(\ell)}(0)=\frac1n\sum_a c_a(0)d_a^{(\ell)}
                                              h_a^{(\ell-1)}(0)^\top.
 \tag{21}
\]

Thus `ddot A(0)` is nonzero, since at least one label is nonzero and
the input columns are separate.

There is an exact identity certifying motion at every hidden layer:

\[
 \sum_a c_a(0)\frac{p_a^{(\ell)\top}\ddot h_a^{(\ell)}(0)}n
 =\frac{\|\ddot A(0)\|_F^2}{n}
               +\sum_{s=2}^\ell\|\ddot W^{(s)}(0)\|_F^2>0.
 \tag{22}
\]

To prove it, all initial hidden velocities are zero, so

\[
 \ddot h_a^{(\ell)}
  =\phi_\ell'(z_a^{(\ell)})\odot
   [\ddot W^{(\ell)}h_a^{(\ell-1)}
                          +W_0^{(\ell)}\ddot h_a^{(\ell-1)}].
\]

Pair with `c_a(0)p_a^(ell)/n` and sum. By (20)--(21), the first
term is `||ddot W^(ell)||_F^2`, and the second becomes the same
pairing one layer below. At the first layer it equals
`||ddot A||_F^2/n`. Iteration proves (22). No sign condition on any
slope or curvature is used.

For each hidden layer, (22) implies that at least one training feature
has nonzero second time derivative. Analyticity then gives nonconstant
feature motion near time zero. This is an exact finite-width certificate;
it does not supply a width-independent lower bound on displacement or
acceleration.

The extra nonconstant hypothesis is necessary for such a general feature
certificate. With one sample and constant nonzero activations, the initial
readout Gram can have a positive gap, the readout can fit the label, and
all hidden features remain constant. Compression may hold in that case,
but hidden feature motion does not.

## 8. Preserving this certificate in the selected weighted network

The polynomial-log source spaces may be enlarged by a fixed finite number
of initialized vectors without changing their asymptotic dimension. Include
`d_a^(ell)` from (19) in the space of layer `ell`, and include the paired
vectors `W_0^(ell+1)T d_a^(ell+1)` in the preceding space. Initial training
features are already included. These vectors use only initialization and
labels and are computed by (19)--(20).

The positive cubature and projected initialized matrices preserve the
paired reverse actions exactly. Thus the smaller network's initial
`dot w`, `dot delta`, and `dot k` are the corresponding restrictions
of the original ones, by downward induction in (20). Its `ddot A`
columns are the restrictions in (21). Since `d_a^(1)` belongs to its
cubature space, the weighted norm of every such column is preserved.
In particular `||ddot A_C||_{D_1,F}>0`.

The weighted version of (22), using the actual weighted adjoints and
Hilbert--Schmidt norms of the weighted dynamics, is

\[
 \sum_a c_a(0)\langle p_{C,a}^{(\ell)},
                  \ddot h_{C,a}^{(\ell)}(0)\rangle_{D_\ell}
 =\|D_1^{1/2}\ddot A_C(0)\|_F^2
       +\sum_{s=2}^\ell\|\ddot B_C^{(s)}(0)\|_{\rm HS}^2>0.
 \tag{23}
\]

Its proof is the same adjoint pairing calculation, with the rank-one
weighted update identity at each layer. It does not require the compressed
matrices to be square or invertible. Consequently the autonomous selected
network has nonzero feature motion in every hidden layer. All added stored
initialization data are discarded after the reduced matrices and masses
are formed; only the usual weighted network state and fixed masses remain.

## 9. Nonmonotone examples and an automatic orthogonal-data gap

The extension includes `phi_ell(z)=sin z` at every layer. Indeed
`|sin(x+iy)|^2=sin^2 x+sinh^2 y<=cosh^2 a` on `|y|<a`.
Its derivative changes sign and has infinitely many real zeros. These
facts do not affect the compression argument or the almost-sure initialized
feature certificate above.

More generally, for linearly independent training vectors, nonconstant
activations in this class make the initial limiting Gram gap automatic.
The first Gaussian preactivation covariance is then positive definite.
For any positive definite covariance `Q`, a Gaussian vector `Z~N(0,Q)`
has positive density on all of `R^m`. If a real vector `c` satisfies

\[
 E\left[\left(\sum_a c_a\phi(Z_a)\right)^2\right]=0,
\]

continuity and full support imply `sum_a c_a phi(z_a)=0` for every
`z in R^m`. Varying one coordinate and using nonconstancy gives `c_a=0`
for each `a`. Thus the feature second-moment matrix is positive definite.
This argument propagates through the fixed number of layers. Bounded
activation values and conditional iid Gaussian rows then give convergence
of the empirical Grams to those positive definite matrices. In particular
all the orthogonal-input nonconstant activation cases used for (22) have
a fixed initial gap with probability tending to one.
