# Neural covariance contraction and the limits of zero-readout cancellation

2026-10-07. Scoped author continuation, with the original dense nonlinear
model, label intersection, whole sphere, all physical times and fitted
endpoint unchanged. No experiment, implementation, Git operation or promotion.

**Outcome.** A scalar covariance comparison can be proved from a weaker
condition than a uniform $O(1/n)$ Hessian operator bound: it suffices to
control the downstream carriers in counting $L^p$ at
$p\asymp\log(n/R)$, or to control the diagonal of the propagated
covariance. The resulting bound is
$CY(R/n)\sqrt{1+\log(n/R)}$. The supplied quadratic-exponential
training-carrier estimate verifies the carrier condition for the final
layer. It does not verify it for passive earlier-layer covariance hybrids.

There is also an actual neural calculation, not an arbitrary row-program
example: for a two-hidden-layer network with
$\phi_1=\tanh$, $\phi_2(z)=\sqrt{1+z^2}$, and positive small labels,
the first nonzero training jet has a positive conditional weak covariance
bias of order $Y/n$. Thus zero initial readout does not give an exact
vanishing identity. This example is compatible with, and does not refute,
the desired decoder accuracy. No complete decoder theorem is obtained.

## 1. Contract and normalization

Use unit inputs $v=x/\sqrt d$. The actual dense network is

\[
 z^{(1)}(v)=Av,\qquad
 z^{(j)}(v)=W^{(j)}h^{(j-1)}(v),\qquad
 h^{(j)}(v)=\phi_j(z^{(j)}(v)),\qquad
 f_n(v)=\frac1n w^\top h^{(L)}(v).
 \tag{1}
\]

The middle recurrence starts at $j=2$. The initialized entries of $A$
are independent $N(0,1)$; those of each hidden $W^{(j)}$ are
independent $N(0,1/n)$; all blocks are independent; and $w(0)=0$.
The training loss is $m^{-1}\sum_a r_a^2$, where
$r_a=f_n(v_a)-y_a$, and the mobilities are
$(n,1,\ldots,1,n)$. In particular,

\[
 \dot A=-\frac2m\sum_a r_a\delta_a^{(1)}v_a^\top,\qquad
 \dot w=-\frac2m\sum_a r_a h_a^{(L)},\qquad
 \dot W^{(j)}=-\frac2{mn}\sum_a
       r_a\delta_a^{(j)}h_a^{(j-1)\top},
 \quad
 \delta_a^{(j)}=\phi_j'(z_a^{(j)})\odot k_a^{(j)},
 \tag{2}
\]

with $k_a^{(L)}=w$ and
$k_a^{(j)}=W^{(j+1)\top}\delta_a^{(j+1)}$.
Write $Y=\|y\|_2/\sqrt m>0$; the zero-label branch is exactly zero.

The target remains the supplied independent-dense-pair upper certificate

\[
 b_n=\frac{c_0Y}{\sqrt n}
 e^{c_1Y^2\sqrt{\log(en)}}
 \sqrt{8\log\frac{8(n+1)(1+2n)^d}{\delta_0}}
 +\frac{c_2Y}{n}.
 \tag{3}
\]

Its inherited constants and scientific width conditions are not altered.
The source's current passive bound includes
$CY\mathcal P\sqrt{(K_*+R+1)/n}$; its implemented prior-block
estimator has the separate, larger
$CY\mathcal P\sqrt{(R+1)(K_*+1)/n}$ term. Here $R$ counts
named history fields and $K_*$ is the supplied prefix information
certificate. This note concerns the covariance contribution to the first
of these errors. It supplies no posterior evaluator or new resource claim.

## 2. The exact downstream covariance contraction

Fix a completed physical history and an incoming passive field for one
hidden layer $\ell$. At this stage the exact conditional answer has
mean $m_\ell\in\mathbb R^n$ and covariance

\[
 \Gamma=vI-K,\qquad 0\preceq K\preceq vI,\qquad
 \operatorname{rank}K\le R\le n.
 \tag{4}
\]

Only in this section $v\ge0$ denotes variance, not an input. If
$v=0$ or $R=0$, there is no covariance defect. For the interpolation
let $X_s\sim N(m_\ell,\Gamma+sK)$, $0\le s\le1$.
The remaining conditional Gaussian matrices are independent of $X_s$
and can first be held fixed. Write them, including their learned mean
displacements, as $M^{(j)}$, $j>\ell$. Any fresh additive query noises
are held fixed too.

Starting from $z^{(\ell)}=z\in\mathbb R^n$, run the remaining forward
network with its smooth passive caps $\psi_j$. Define its normalized
output and its normalized backward carriers by

\[
 F_\ell(z)=\frac1n (w/Y)^\top h^{(L)}(z),\qquad
 k^{(L)}=w/Y,\qquad
 k^{(j)}=M^{(j+1)\top}
                 [\psi_{j+1}'(z^{(j+1)})\odot k^{(j+1)}].
 \tag{5}
\]

These $k^{(j)}$ are the carriers for this frozen passive continuation;
they are not asserted to be training carriers. Define the input-to-layer
Jacobians, each an $n\times n$ matrix, by

\[
 J_\ell=I,
 \qquad J_j=M^{(j)}\operatorname{diag}(\psi_{j-1}'(z^{(j-1)}))
                    J_{j-1},\quad j>\ell.
 \tag{6}
\]

The chain rule gives the exact Hessian identity

\[
 D^2F_\ell(z)=\frac1n\sum_{j=\ell}^L
 J_j^\top\operatorname{diag}
       (k^{(j)}\odot\psi_j''(z^{(j)}))J_j.
 \tag{7}
\]

To verify every term, vary the initial $z$ in two directions. The first
variation at layer $j$ is $J_j$ applied to the direction. The second
variation of that layer's activation is the sum of its propagated incoming
second variation and $\psi_j''$ times the product of its two first
variations. Propagating each newly created term to the readout gives
the scalar coefficient $k^{(j)}/n$. Summing over the layer at which
the second variation is created proves (7). All other nodes are affine.

For independent standard Gaussian vectors $g,h$, write
$X_s=m_\ell+\Gamma^{1/2}g+\sqrt sK^{1/2}h$.
For $s>0$, differentiating its expectation gives
$\mathbb E[\nabla F_\ell(X_s)^\top K^{1/2}h]/(2\sqrt s)$.
Integration by parts in $h$ changes this to
$\mathbb E\operatorname{tr}(KD^2F_\ell(X_s))/2$.
Substitute (7) and integrate in $s$ to obtain

\[
 \mathbb EF_\ell(X_1)-\mathbb EF_\ell(X_0)
 =\frac1{2n}\int_0^1\sum_{j=\ell}^L
 \mathbb E\sum_{i=1}^n
 k_i^{(j)}\psi_j''(z_i^{(j)})
          (J_jKJ_j^\top)_{ii}\,ds.
 \tag{8}
\]

All fields inside the integral are evaluated at $X_s$. For fixed
matrices the caps have bounded derivatives and the readout is finite, so
differentiation and Gaussian integration by parts are justified. For
random remaining matrices it suffices that the right side after taking
absolute values is integrable. Conditional Gaussian matrices have all
finite moments, and the finite-depth bounds used below give that
integrability whenever their displayed carrier condition holds. Singular
endpoint covariances are handled by adding an independent Gaussian of
variance $\varepsilon I$, applying the same identity, and taking
$\varepsilon\downarrow0$ by domination.

Formula (8) is the exact object that needs estimating. It can be much
smaller than 
$\operatorname{tr}K\sup_z\|D^2F_\ell(z)\|_{\rm op}$.
It also shows that zero readout at physical time zero does not cancel the
two Hessian terms from different later layers: their carriers evolve
away from zero, and no opposite-sign identity appears in (7).

## 3. An $R/n$ estimate from counting moments or diagonal influence

For $p\ge2$, write
$\|k\|_{p,n}=(n^{-1}\sum_i|k_i|^p)^{1/p}$.
For any matrix $J$, put $d_i=(JKJ^\top)_{ii}\ge0$.
Equation (4) gives

\[
 \max_i d_i\le v\|J\|_{\rm op}^2,\qquad
 \sum_i d_i\le vR\|J\|_{\rm op}^2.
 \tag{9}
\]

If $q=p/(p-1)$, then
$\sum_i d_i^q\le(\max_i d_i)^{q-1}\sum_i d_i$.
Hölder and (9) therefore prove

\[
 \sum_i |k_i|d_i
 \le v\|J\|_{\rm op}^2 R^{1-1/p}n^{1/p}\|k\|_{p,n}.
 \tag{10}
\]

No eigenvalue lower bound, independence of $k,J,K$, or coordinate
maximum was used. Suppose $a_2=\max_j\|\psi_j''\|_\infty$, and
the actual conditional passive interpolation satisfies

\[
 \int_0^1\sum_{j=\ell}^L
 \mathbb E[\|J_j\|_{\rm op}^2\|k^{(j)}\|_{p,n}]\,ds
 \le A\sqrt p.
 \tag{11}
\]

Then (8)--(10) imply

\[
 |\mathbb EF_\ell(X_1)-\mathbb EF_\ell(X_0)|
 \le\frac{a_2vA}{2}\frac Rn (n/R)^{1/p}\sqrt p.
 \tag{12}
\]

Choose $p=\max\{2,\log(n/R)\}$. The factor
$(n/R)^{1/p}$ is at most $e$, giving

\[
 |\mathbb EF_\ell(X_1)-\mathbb EF_\ell(X_0)|
 \le C a_2vA\frac Rn\sqrt{1+\log(n/R)}.
 \tag{13}
\]

Multiplication by $Y$ converts (13) to prediction units. This is a
conditional theorem, with the full expectation and parameter dependence
in (11) explicit. A fixed-order $L^p$ theorem with an unspecified
width threshold depending on $p$ cannot justify its growing choice
of $p$.

There is a different sufficient condition requiring no high carrier
moments. If, for this same interpolation,

\[
 (J_jKJ_j^\top)_{ii}\le D_jR/n
 \quad\hbox{for every }i,\qquad
 \int_0^1\mathbb E\|k^{(j)}\|_{1,n}\,ds\le B_j,
 \tag{14}
\]

then (8) gives the sharper bound
$a_2R\sum_jD_jB_j/(2n)$. The diagonal premise concerns the
propagated covariance itself. Coordinate bounds on unwhitened history
columns do not imply it: nearly dependent columns can have concentrated
normalized differences. The positive training feature-Gram gap is not
a gap for that history space.

### What the actual training budget supplies

Section 12 of the authorized UNBOUNDED_COMPRESSOR_BRIDGE.md supplies,
on its inherited source event, a running training budget of the form

\[
 \frac1n\sum_i\exp\{\eta_2|w_i(t)/S|^2\}\le\mathcal B_2,
 \qquad S=16Ym/\gamma,
 \tag{15}
\]

simultaneously through all physical time. The stronger full budget
includes training preactivations and carriers as well. From
$x^p\le[p/(2e\eta_2)]^{p/2}e^{\eta_2x^2}$,

\[
 \|w(t)/Y\|_{p,n}
 \le \frac{16m}{\gamma}
       \sqrt{\frac p{2e\eta_2}}\,\mathcal B_2^{1/p}.
 \tag{16}
\]

For a last-layer interpolation $J_L=I$ and $k^{(L)}=w/Y$
are fixed. Thus (11) follows from (16), and (13) is proved there
without a uniform Hessian bound. A finite source readout whose normalized
RMS discrepancy is at most $n^{-10}$ has an additional counting
$L^p$ discrepancy at most $n^{-19/2}$, using its Euclidean norm;
this does not change the conclusion on the coupled good event.

For earlier layers, (16) alone is insufficient. Their $k^{(j)}$
in (11) use an unseen query and a covariance-interpolated preactivation,
then the remaining conditional matrices. Those vectors are absent from
the training budget (15). Neither conditioning that budget on an
arbitrary prefix nor inserting a good-event indicator proves (11).
The right side of (8) integrates over all its Gaussian interpolation.
The supplied source theorem explicitly excludes a passive or marked
response conclusion from its optional quadratic-exponential budget.

The operator factors in (11) are not the decisive obstacle. Bounded
passive slopes give a finite product of remaining matrix operator norms.
For a posterior centered Gaussian matrix whose entry covariance is
dominated by $I/n$, a fixed bilinear form has variance at most $1/n$.
Two sphere $1/4$-nets of size at most $9^n$, followed by the Gaussian
tail bound, give a uniform finite fourth moment of its operator norm.
Adding the bounded conditional mean and applying Hölder over fixed
depth bounds the requisite finite operator moments. What is missing is
their product with the passive carriers at $p\asymp\log(n/R)$,
with no uncounted tail or conditioning cost.

## 4. A nonzero weak bias in an actual nonlinear training jet

This calculation tests the claimed cancellation using legitimate neural
fields. It is not a lower bound for the full decoder.

Take $d=m=L=2$, training inputs $v_1=e_1,v_2=e_2$, unseen input
$v_*=(e_1+e_2)/\sqrt2$, and labels $y_1=y_2=\varepsilon>0$
within the original label intersection. Thus $Y=\varepsilon$. Let

\[
 \phi_1(z)=\tanh z,\qquad \phi_2(z)=\sqrt{1+z^2},
 \tag{17}
\]

using the analytic square-root branch positive on the real axis. Both
are holomorphic with bounded first derivative on a common sufficiently
small open strip, for example
$|\operatorname{Im}z|<1/4$. The second activation has unbounded
values. On the real axis,

\[
 \phi_2'(z)=\frac z{\sqrt{1+z^2}},\qquad
 \phi_2''(z)=(1+z^2)^{-3/2}>0.
 \tag{18}
\]

The population top-feature Gram is positive definite: the first-layer
training covariance is $qI_2$, with
$q=\mathbb E\tanh(G)^2>0$. The second-layer Gaussian training
coordinates are independent, and the smaller eigenvalue of the top
Gram is $\operatorname{Var}(\sqrt{1+qG^2})>0$. Thus no data or
activation assumption is evaded.

At initialization set

\[
 h_a=\tanh(Av_a),\quad H=[h_1,h_2],\quad
 h_*=\tanh(Av_*),\quad z_a=W^{(2)}h_a,
 \]
\[
 a_i=\phi_2(z_{1,i})+\phi_2(z_{2,i}),\qquad
 \dot w_i(0)=\varepsilon a_i,\qquad
 u_i=\phi_2'(z_{1,i})\dot w_i(0).
 \tag{19}
\]

Here $a_i\ge2$. Since all initial hidden velocities are zero,
$u=\dot\delta_1^{(2)}(0)$, and
$W^{(2)\top}u=\dot k_1^{(1)}(0)$. These are exact fields of the
first nonzero training jet. The hidden layers subsequently move; no
frozen-feature model replaces the flow.

Consider its legitimate matrix-call history consisting of the training
forward answers $W^{(2)}H$ and the first reverse jet answer

\[
 b=W^{(2)\top}u+\sigma\xi,\qquad \xi\sim N(0,I_n),
 \tag{20}
\]

where $\xi$ is independent and $0\le\sigma\le C_\sigma\varepsilon$.
The noiseless choice is the exact neural derivative; positive noise
is an allowed auxiliary observation of that derivative. No passive query
answer has been observed. The input $u$ is measurable from the preceding
forward answers, so ordinary conditional Gaussian regression applies.

Let $P_H$ be the orthogonal projection onto the column span of $H$,
and put $q_*=(I-P_H)h_*$, $v_n=\|q_*\|_2^2/n$. Conditional on
$A,W^{(2)}H$, the remaining matrix is
$n^{-1/2}G(I-P_H)$ plus its known mean, with independent standard
Gaussian entries in $G$. Conditional also on (20), its action on
$h_*$ has covariance

\[
 \Gamma_n=v_n(I-\theta_n P_u),\quad
 P_u=uu^\top/\|u\|_2^2,\qquad
 \theta_n=\frac{\|u\|_2^2}{\|u\|_2^2+n\sigma^2}.
 \tag{21}
\]

Indeed its covariance with the reverse observation is
$u q_*^\top/n$; the reverse covariance on the residual subspace is
$(\|u\|_2^2/n+\sigma^2)I$. Subtraction of their covariance
product gives (21). The exceptional cases $u=0$ or $v_n=0$ have
probability tending to zero; the argument below verifies nondegeneracy.

Write the conditional mean as $m_n$, and restore the rank-one covariance
$K_n=v_n\theta_nP_u$. The actual prediction's initial physical derivative
at the query is the function

\[
 F^{\rm jet}(z)=\frac1n\dot w(0)^\top\phi_2(z),\qquad
 \dot f_n(0,v_*)=F^{\rm jet}(W^{(2)}h_*).
 \tag{22}
\]

Gaussian interpolation and (18) give the exact strict inequality

\[
 \begin{aligned}
 &\mathbb E F^{\rm jet}(N(m_n,v_nI))
      -\mathbb E F^{\rm jet}(N(m_n,\Gamma_n))\\
 &\quad=\frac1{2n}\int_0^1\sum_i
       \dot w_i(0)(K_n)_{ii}
       \mathbb E\phi_2''(X_{s,i})\,ds>0,
 \end{aligned}
 \tag{23}
\]

whenever $u\ne0$ and $v_n>0$. Unlike a generic rank-one matrix
example, its readout and covariance direction have exactly the neural
provenance (19)--(20). The activation's linear growth and bounded second
derivative justify all expectations and integrations in (23).

### Its typical size is exactly $Y/n$

There are constants $0<c<C<\infty$, independent of $n$ and of
$0<\varepsilon$ with $\sigma/\varepsilon\le C_\sigma$, such
that, with probability tending to one, the difference in (23) lies in
$[c\varepsilon/n,C\varepsilon/n]$.

Here are the quantitative ingredients, including why they are available.
The three bounded first-layer row functions

\[
 \tanh A_1,\quad\tanh A_2,\quad
                 \tanh((A_1+A_2)/\sqrt2)
\]

are linearly independent in Gaussian $L^2$. An almost-everywhere linear
relation would, by continuity and full support, hold everywhere. Setting
$A_2=0$ and comparing the linear and cubic Taylor coefficients forces
the first and third coefficients to vanish; the second then vanishes.
Their population Gram is positive definite. The ordinary iid law of
large numbers consequently gives $v_n\to v_*>0$, bounded coefficients
in the projection of $h_*$ onto $H$, and a training covariance
$H^\top H/n\to qI_2$.

Conditional on these first features, the rows $(z_{1,i},z_{2,i})$
are independent centered Gaussian pairs with that covariance. Let
$u_i^0=u_i/\varepsilon=\phi_2'(z_{1,i})a_i$. Their polynomial
moments are uniformly bounded when the covariance lies in a compact
neighborhood of $qI_2$. Conditional Chebyshev and convergence of
Gaussian moments give constants $c_1,C_1>0$ such that

\[
 c_1\le n^{-1}\sum_i(u_i^0)^2\le C_1,
 \qquad n^{-1}\sum_i a_i(u_i^0)^2\le C_1
 \tag{24}
\]

with probability tending to one. Choose a fixed rectangle
$1\le z_1\le2,\ |z_2|\le1$. It has positive limiting Gaussian
probability, and $a,u^0$ are bounded there with $|u^0|$ bounded
away from zero. The same conditional law of large numbers gives

\[
 \sum_{i\ {m in\ this\ rectangle}}(u_i^0)^2
        \ge c_1 n,
 \tag{25}
\]

after decreasing $c_1$. Formula (24) and the noise bound keep
$\theta_n$ uniformly positive.

The conditional mean from the reverse observation has the representation

\[
 m_{n,i}=\beta_n^\top(z_{1,i},z_{2,i})
       +\sqrt{v_n\theta_n}\,(u_i^0/\|u^0\|_2)G_0,
 \qquad G_0\sim N(0,1),
 \tag{26}
\]

where $\beta_n=(H^\top H)^{-1}H^\top h_*$ is bounded and
$G_0$ is independent of the preceding forward history. This follows
by standardizing $q_*^\top b$, whose conditional variance is
$v_n(\|u\|_2^2+n\sigma^2)$.
On $|G_0|\le\sqrt n$, an event with probability tending to one,
(24)--(26) bound $|m_{n,i}|$ by a fixed constant on the selected
rectangle. Every interpolation variance is at most $v_n\le1$.
Thus $\mathbb E\phi_2''(X_{s,i})\ge c_2>0$ on those indices:
restrict its defining Gaussian to $|G|\le1$ and use (18).

Since $\dot w_i(0)\ge2\varepsilon$, (21), (24)--(25) give the
lower bound $c\varepsilon/n$ in (23). Since
$0<\phi_2''\le1$, (21) and the second bound in (24) give its
upper bound $C\varepsilon/n$. This proves the claimed order.

This calculation is at an exact initialization jet and its indicated
matrix-call history. It is not a comparison for the full rounded source
prefix, not a uniform positive-time lower bound, and not a lower bound
for every compact decoder. A small-time expansion at each fixed width
alone would not justify a width-uniform positive-time conclusion. Its
precise force is to disprove an exact cancellation based solely on
zero readout, even for fields reached by the nonlinear neural equations.

## 5. Remaining implications and their exact strength

The neural structure improves the question from a generic Hessian bound
to (8), with two concrete sufficient routes (11) and (14). The final
layer has the claimed $R/n$, up to a square-root logarithm, on the
inherited training-carrier event. For earlier layers neither sufficient
route is verified by the assigned inputs.

Even a proof of (11) at every layer would close only one component of
the original task. Three additional obligations remain as already exposed
by the supplied weak and polynomial-onset notes:

1. The empirical-to-population recursion requires derivative fluctuation
   and second-order remainder bounds for the actual whitened finite
   history marks. Training carrier moments do not supply moments of
   arbitrary whitened temporal-jet directions or their products.
2. A conditional-mean comparison must be transferred to the dense center
   at unchanged confidence and certificate. The current common-event
   conditional mass is $1-q_0$ with fixed $q_0$. That supports
   interval intersection, but a bounded scalar mean can still have an
   $O(q_0)$ error. The weak estimate (8) alone does not remove that
   term or provide a direct quantile theorem.
3. The actual query samples the finite prior. A sharper Gaussian weak
   theorem does not evaluate posterior expectations or erase prior versus
   posterior bias. Any replacement evaluator must be explicit and have
   its state, precision, randomness, query work and scratch charged.

If all added errors were $Y n^{-1}$ times fixed-degree polynomials
in the existing parameters and $Z$, absorption into (3) would have a
polynomial sufficient onset in those coefficients and $c_0^{-1}$, by
the $c_0Y/\sqrt n$ lower envelope of (3) and
an elementary bound of a fixed logarithmic power by a fractional power
of $n$. This does not require enlarging the final certificate or
changing its logarithmic powers. But the coefficient control, the three
other bridges above, and the inherited scientific source gates remain
separate. In particular the supplied notes do not quantify the original
parameter dependence of $c_0^{-1}$. Equation (13) alone proves none of
these remaining conclusions.

The route should therefore be recorded as a **bounded partial result**,
not a neural obstruction and not a completed polynomial-onset theorem.
Its next specific mathematical premise is a posterior-valid passive
carrier estimate (11), including the interpolation and exceptional tails,
or a direct diagonal estimate (14). The genuine neural calculation
(23) shows that the expected attainable order is a small nonzero weak
bias, rather than a symmetry forcing it to vanish.

## 6. Provenance and checks

Only the eleven assigned scientific sources were read, including the
two integrated-study paths explicitly authorized by the supervisor. No
linked other-study source, sibling's new result, or review was fetched.
The conjecture, rigorous-proof and canonical-notation skills and the
neural reference were read and applied. All new checks were symbolic:
the second-variation expansion (7), Hölder contraction (10), Gaussian
regression (21), and the positivity and typical-order proof (23)--(26).
This is author work, not an independent reconstruction or promotion.

| Assigned source | SHA-256 |
|---|---|
| WEAK_PASSIVE_WIDTH_ROUTE.md | `f1a9d820711f436e7d17ad0a5a66937b004f3e9e4f099ef784805443142dbc73` |
| POLYNOMIAL_ACCURACY_ONSET.md | `5cc5fa8b166acde7169b5a839aa71acf69e6e3d8e25840c53bf10509680beb50` |
| FAST_FINITE_SOURCE_BRIDGE.md | `7ef69972a213fb26b77cd1c0ed4dcbd8b7d12f9e3b06906f351f7443f79894e6` |
| FAST_FINITE_PASSIVE.md | `7f298bc637afffc207375692ee725290e752cdeb818b42f82563646f74416777` |
| FAST_FINITE_POSTERIOR.md | `f3cc565c52e848611d576d877ca893964cf45a74fb35f86c0494fbe8b09413db` |
| FAST_SCALAR_FORCING.md | `6b74c2a49046bdce4d30b0bf46535ddbc6498332b91fb3d516fefb0bd09f23bb` |
| GAP_REFINED_PHASE_COSTS.md | `817617951efb926d2729cd7f20eaccf7cb5c4e25e17eb531502c8b2618e017bc` |
| GROWING_PROGRAM_STABILITY.md | `a3ef83a059912c93c451d065d23d269f3607d2c64b15cd5b7e4bcc558e1c7215` |
| ROOT_RESPONSE_AND_COVARIANCE.md | `fc5aeaaf56dc9c4e55f71eb40e81ed6fcede8c21f1eab715617654e60d66deea` |
| integrated GENERAL_DENSE_COMPARISON.md | `ab97a860d7a6e175905a6848a9126ca8a194e08f52764738e94dcde2675100a9` |
| integrated UNBOUNDED_COMPRESSOR_BRIDGE.md | `e018f0291b4456913a6541d5db7d90a678c4564928edcd5f47dd8c5326336f5d` |

Only NEURAL_WEAK_ERROR_ROUTE.md was written. The resource table, original
label intersection, scientific widths and final decoder status are unchanged.
