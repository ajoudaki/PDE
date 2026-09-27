# Can the neuron width be removed while retaining all training samples?

## Scope and correction

Use \(m\) for the number of training samples and \(n\) for hidden-layer
width. The fixed-kernel loss example

\[
 \dot r=-\frac2m\Theta r,\qquad
 \mathcal L=\frac1m r^\top r
\]

concerns the amount of **sample-indexed** information. It says that loss alone
may need \(m\) auxiliary coordinates. It gives no obstruction to eliminating
the neuron width \(n\) while allowing state size to depend on \(m\).

The width-only question is:

> For fixed sample count \(m\), depth, response-memory order \(P\), horizon and
> accuracy, can one replace all \(n\)-component neuron populations and the
> \(n\times n\) initialized operators by an autonomous state whose dimension
> does not grow with \(n\)?

The primary question is approximate compression. The complete positive
fixed-width construction, its finite-horizon proof, its Fourier whole-circle
readout and the exact width-uniform gap are stated in
[APPROXIMATE_SCALAR_POPULATION_COMPRESSION.md](APPROXIMATE_SCALAR_POPULATION_COMPRESSION.md).
The answer is: convergent scalar approximation is proved for every separately
fixed width; an economical cutoff uniform in dense Gaussian width remains
open; and unrestricted whole-function families admit a continuous
approximation lower bound. The exact results below are benchmarks and scope
boundaries, not substitutes for that approximate answer.

## 1. What counts as genuine width compression?

For each width \(n\), let the parent response-memory state satisfy

\[
 \dot S_n=F_{n,P}(S_n),
\]

and let \(O_n(S_n)\) be the requested training outputs, losses or fixed query
outputs. A genuine width-free closure of order \(K\) has

\[
 \dot q=G_K(q),\qquad \widehat O=R_K(q),
\]

where the number of real coordinates in \(q\) may depend on
\((m,P,\text{depth},K)\) but not on \(n\). Its initialization can use
width-normalized contractions of the realized network. It cannot hide all
neurons in an arbitrary-precision scalar, query the parent population during
training, or replay a recorded trajectory.

Exact width compression requires one finite \(K\) that works for every
admitted width. Approximate width compression on \([0,T]\) requires

\[
 \sup_{n\ge n_0}\sup_{t\le T}
 |\widehat O_{n,K}(t)-O_n(t)|
 \le \varepsilon_K(T),
 \qquad
 \varepsilon_K(T)\longrightarrow0,
 \tag{1}
\]

with \(K\) independent of \(n\). A theorem only saying that for each fixed
\(n\) some \(K(n,\varepsilon)\) works does not yet remove width.

## 2. Frozen features and NTK: exact width removal on a finite query set

Let \(f\in\mathbb R^m\) be the training outputs of a model linearized at
initialization,

\[
 f=f_0+J_0(\theta-\theta_0),
\]

where \(J_0\) is the frozen feature Jacobian. For unhalved mean squared loss,
gradient flow gives

\[
 \dot\theta=-\frac2mJ_0^\top(f-y).
\]

Therefore

\[
 \boxed{\dot f=-\frac2m\Theta(f-y),\qquad
        \Theta=J_0J_0^\top.}
 \tag{2}
\]

The \(m\times m\) matrix \(\Theta\) is constant. Once \(f_0\) and \(\Theta\)
have been computed, the neuron population and parameter dimension are
irrelevant to training-output dynamics. This is an exact \(n\)-free
autonomous system for the finite-width frozen-feature model itself.

For \(q\) fixed test inputs with frozen Jacobian \(J_*\), retain

\[
 \Theta_{*,X}=J_*J_0^\top.
\]

Their outputs obey

\[
 \dot f_*=-\frac2m\Theta_{*,X}(f-y).
 \tag{3}
\]

Thus any predeclared finite training/query set has exact state and runtime
independent of \(n\), after its kernels are initialized.

There is one important whole-function qualification. For an arbitrary new
input \(x\), finite-width prediction requires the empirical kernel section

\[
 k_n(x,X)=J_0(x)J_0(X)^\top
\]

and the initial function \(f_0(x)\). If the finite feature bank has been
discarded, these functions need not have an exact compact representation. In
an infinite-width NTK model with an explicit deterministic kernel, they can be
evaluated directly and the whole predictor is represented by \(m\)
coefficients. At finite width, exact whole-domain decoding may still retain
width-dependent kernel information even though training outputs do not.

This positive result is not evidence that feature-learning dynamics should
collapse to the same kernel system. It works precisely because the feature
Jacobian is frozen.

## 3. Linear feature learning: one hidden layer closes exactly

Width removal is not limited to frozen features. Consider a two-factor linear
network

\[
 A=VW,\qquad
 W\in\mathbb R^{n\times d_{\rm in}},\quad
 V\in\mathbb R^{d_{\rm out}\times n},
\]

with any differentiable loss \(\ell(A)\). Put

\[
 G=\nabla_A\ell(A),\qquad
 B=VV^\top,\qquad C=W^\top W.
\]

Euclidean gradient flow is

\[
 \dot V=-GW^\top,\qquad \dot W=-V^\top G.
\]

The product rule gives the exact autonomous system

\[
\boxed{
\begin{aligned}
 \dot A&=-BG-GC,\\
 \dot B&=-GA^\top-AG^\top,\\
 \dot C&=-G^\top A-A^\top G.
\end{aligned}}
\tag{4}
\]

Every matrix in (4) lives in the input or output dimension; none has a hidden
width index. Since \(G\) is computed from \(A\) and the retained dataset, (4)
is an exact width-free feature-learning closure. It also reconstructs the
entire linear predictor \(x\mapsto Ax\), not merely its training values.
Different block mobilities or normalizations insert known scalar factors and
do not change the closure mechanism.

The reason this works is algebraic: differentiating the product and the two
endpoint Gram matrices creates no new kind of matrix.

## 4. Adding another linear factor generically creates a spectral population

Now take a scalar-input/scalar-output three-factor model

\[
 f=a^\top M u
\]

with \(a,u\in\mathbb R^n\), \(M\in\mathbb R^{n\times n}\). Suppress the
known loss-dependent common scalar factor and write the exact gradient
directions as

\[
 \dot a=gMu,\qquad
 \dot u=gM^\top a,\qquad
 \dot M=gau^\top.
\tag{5}
\]

Define

\[
 C=MM^\top-aa^\top,\qquad
 \delta=\|a\|^2-\|u\|^2,\qquad
 v=Mu,\qquad q=\|a\|^2.
\]

Direct differentiation shows that \(C\) and \(\delta\) are constant and

\[
 \dot a=gv,\qquad
 \dot v=g\,[C+(2q-\delta)I]a,\qquad
 f=a^\top v.
\tag{6}
\]

Equation (6) is an exact reduction, but it is not generally finite scalar
compression independent of \(n\). Diagonalizing the fixed symmetric matrix
\(C\) shows that the evolution depends on the spectral measure of the initial
pair \((a(0),v(0))\) relative to \(C\). A generic finite-width \(C\) has \(n\)
distinct eigenvalues with nonzero weights, so its exact spectral measure has
up to \(n\) atoms.

Equivalently, repeated differentiation generates the Krylov quantities

\[
 a(0)^\top C^k a(0),\quad
 a(0)^\top C^k v(0),\quad
 v(0)^\top C^k v(0),\qquad k=0,1,\ldots.
\tag{7}
\]

At finite width, Cayley--Hamilton closes this list after at most \(n\) spectral
degrees, not after a width-independent number. At Gaussian infinite width,
the empirical spectral measure can converge to a deterministic continuous
measure, but the exact state is then a pair of functions of the spectral
variable. Width has disappeared while an infinite-dimensional population
state remains.

This distinction persists at greater fixed linear depth. The natural exact
limit is an operator/word state generated by the initialized matrices and
their adjoints. It is width independent as a Hilbert-space object, but not a
finite list of scalars. Special balanced, isotropic or low-spectral-rank
initializations can collapse it further; generic Gaussian initialization does
not supply that finite collapse.

Spectral quadrature is nevertheless a principled approximation: approximate
the fixed measure in (6) by \(K\) nodes and evolve the two fields on those
nodes. Its order can be independent of \(n\) when quadrature error and
nonlinear feedback are controlled uniformly. This is approximation of a
spectral population, not an exact finite closure.

## 5. What this says about general nonlinear populations

The three benchmarks give the correct hierarchy of possibilities.

1. **Frozen features:** finitely many sample kernels close exactly.
2. **A special trainable algebra:** the two-factor linear model closes through
   finitely many endpoint matrices.
3. **Generic deeper linear learning:** width is replaced by a spectral or
   operator population, not by finitely many scalars.
4. **Nonlinear feature learning:** pointwise gates and reused forward/adjoint
   actions add further moment and response hierarchies.

For a general population ODE, a finite collection of aggregates closes
exactly only when its projected velocity is constant on aggregate fibres:

\[
 A(S)=A(\widetilde S)
 \Longrightarrow
 DA(S)F(S)=DA(\widetilde S)F(\widetilde S).
\tag{8}
\]

An invariant parametric law, an invariant observable algebra, or a finite
predictive state can make (8) hold. Exchangeability, Gaussian initialization
and smooth activation do not make it automatic.

A basic nonlinear example demonstrates the generic issue. For
\(\dot x_i=-x_i^3\), the moments satisfy

\[
 \dot\mu_p=-p\mu_{p+2}.
\]

The mean trajectory over arbitrary initial empirical measures depends on an
unbounded moment sequence. Replacing the \(n\) particles by finitely many
moments is not exact uniformly over those populations. Neural gates produce
the same kind of degree growth, while initialized matrix reuse also generates
two-sided operator words.

This is a general obstruction, not a no-go theorem for the particular reached
Gaussian family of the response-memory network.

## 6. An exact width-only no-go theorem with one sample

The preceding moment example still leaves open whether some clever nonlinear
finite encoder could close even when ordinary moments do not. A simple tanh
feature-learning model rules this out under a natural state-universal
contract.

The general certificate is a Lie-rank test. If \(O(S)=R(A(S))\) and
\(DA(S)F(S)=G(A(S))\) for an exact \(K\)-dimensional smooth closure, then every
Lie derivative of the output factors through the same state:

\[
 \mathcal L_F^jO(S)=\Psi_j(A(S)).
\]

Hence, for every finite \(J\),

\[
 \operatorname{rank}D\bigl(O,\mathcal L_FO,\ldots,
                    \mathcal L_F^JO\bigr)\le K.
 \tag{W0}
\]

Finding output jets with differential rank growing with width therefore rules
out every smooth fixed-dimensional encoder, not only a selected moment
dictionary.

Take one scalar training sample, fixed unit readout, and

\[
 f_n(w)=\frac1n\sum_{i=1}^n\tanh w_i,\qquad
 r=f_n-y,\qquad \mathcal L=r^2.
 \tag{W1}
\]

With canonical width mobility \(n\),

\[
 \dot w_i=-2r(1-\tanh^2w_i).
 \tag{W2}
\]

Introduce \(q\) by \(\dot q=-2r\). Where \(r\ne0\), it is a local time
coordinate. Setting \(z_i=\tanh w_i\) gives

\[
 \frac{dz_i}{dq}=(1-z_i^2)^2,\qquad
 f_n=\frac1n\sum_i z_i.
 \tag{W3}
\]

Define

\[
 p_0(z)=z,\qquad p_{k+1}(z)=(1-z^2)^2p_k'(z).
 \tag{W4}
\]

Then the exact output jets are

\[
 \frac{d^kf_n}{dq^k}(0)=\frac1n\sum_i p_k(z_i(0)).
 \tag{W5}
\]

Induction gives \(\deg p_k=3k+1\) with nonzero leading coefficient. Hence
\(p_0',\ldots,p_{n-1}'\) have distinct degrees
\(0,3,\ldots,3(n-1)\) and are linearly independent. There are therefore
points \(z_1,\ldots,z_n\in(-1,1)\) for which

\[
 \det[p_k'(z_i)]_{0\le k<n,\ 1\le i\le n}\ne0.
 \tag{W6}
\]

Suppose an exact scalarization on an open state set had a fixed dimension
\(K\), independent of \(n\):

\[
 a(0)=E_n(w(0)),\qquad \dot a=G_n(a),\qquad f_n=H_n(a),
 \tag{W7}
\]

where the smooth maps themselves may depend on \(n\). On
\(H_n(a)-y\ne0\), it can be reparametrized by the same clock,

\[
 \frac{da}{dq}=\frac{G_n(a)}{-2(H_n(a)-y)}.
\]

Thus the first \(n\) \(q\)-jets of its output factor smoothly through the
\(K\)-dimensional initial state. Their differential rank is at most \(K\).
But (W5)--(W6), together with \(dz_i/dw_i>0\), show that the true jet map has
rank \(n\) at the displayed state. Consequently

\[
 \boxed{K\ge n.}
 \tag{W8}
\]

This proves that no exact smooth, restartable scalar closure of fixed
dimension can work uniformly in width on an open family of nonlinear neuron
populations, even with \(m=1\) and without \(W_0\). It excludes arbitrary
smooth finite encoders, rather than only a chosen moment list.

The maintained observable-closure theory gives a complementary
architecture-level result: no fixed finite list of bounded-degree tensor
contractions with polynomial or analytic autonomous dynamics closes uniformly
in width on an open state set. Repeated Lie derivatives create connected
contraction graphs of unbounded complexity, and those graphs remain
independent at sufficiently large width.

The scope is essential. The theorem does not prove nonclosure on one
prescribed Gaussian-initialized trajectory, nor does it rule out finite
accuracy. In the model above, approximate the empirical initial law of the
\(z_i\) by \(K\) weighted atoms and evolve those atoms under (W3). Since the
characteristic vector field is Lipschitz on \([-1,1]\),

\[
 |f_\mu(q)-f_{\mu_K}(q)|
 \le e^{C|q|}W_1(\mu,\mu_K).
 \tag{W9}
\]

One-dimensional quantization gives \(W_1=O(K^{-1})\) on the bounded interval,
independently of the original width. Coupling back through
\(\dot q=-2(f-y)\) preserves a finite-horizon bound by Gronwall. Exact
width-free closure is therefore generically impossible while approximate
width compression can remain fully principled.

## 7. Status for the response-memory population closure

For fixed \(m,P\) and depth, the current parent closure retains finitely many
neuron fields per sample and layer. Its scalar construction differentiates
their normalized contractions and the contractions containing \(W_0\) and
\(W_0^\top\). This produces:

* an exact countable forest hierarchy for the requested output/Gram
  observables;
* finite cutoffs whose coordinate **type count** is independent of \(n\); and
* a clipped cutoff theorem giving output convergence on every prescribed
  finite interval when the aggregate cutoff tends to infinity at each fixed
  \(n\).

The familiar tangent hierarchy gives a compact schematic view. Ignoring the
already separated finite-\(P\) reconstruction defect, training outputs obey

\[
 \dot f_a=-\frac2m\sum_b\Theta_{ab}r_b.
\]

Both \(f\) and the \(m\times m\) tangent kernel \(\Theta\) are neuron-free
aggregates. In an NTK model, \(\dot\Theta=0\), so the hierarchy stops. Under
feature learning, differentiation has the schematic form

\[
 \dot\Theta_{ab}
 =-\frac2m\sum_c r_c\,T_{abc},
\]

where \(T\) is a third-order contraction of parameter derivatives and current
responses. Differentiating \(T\) generates higher sample-indexed contractions.
At every fixed level their count depends on \(m\) and the level, not on \(n\).
The forest hierarchy used in this study is a typed version that also preserves
history moments and shared \(W_0/W_0^\top\) reuse. The width question is
therefore exactly whether this sample-indexed hierarchy has a uniform tail,
not whether neuron-free coordinates can be written down at all. Its coordinate
count can still grow combinatorially with \(m,P\) and cutoff order, so
width-free does not automatically mean economical.

In the NTK scaling, feature-motion terms vanish with width and the hierarchy
collapses to the frozen \(m\times m\) kernel. The canonical scaling used by
the response-memory study deliberately keeps feature motion of order one. Its
infinite-width object is therefore a moving population or operator law, rather
than automatically a finite kernel ODE. Taking \(n\to\infty\) removes particle
discretization; it does not by itself turn that limiting law into finitely
many scalars.

Therefore population-to-scalar compression is mathematically possible in the
following fixed-width sense: for each fixed \(n,m,P,T,\varepsilon\), a finite
autonomous scalar cutoff exists whose requested outputs approximate the parent
closure to accuracy \(\varepsilon\).

What is not proved is the width-free statement (1). The present constants and
required cutoff may depend on \(n\). Consequently the theorem does not yet say
that one fixed scalar model size works as width increases.

There are concrete reasons this uniform step is difficult:

* differentiating low-order moments creates higher gated mixed moments;
* the same initialized Gaussian operator must be reused in both directions;
* for a generic \(W_0\), an active vector with nonzero components in every
  singular direction generates the full cyclic space
  \[
  h,\;(W_0^\top W_0)h,\ldots,(W_0^\top W_0)^{n-1}h;
  \]
  hence any exact fixed **linear action subspace** containing that vector is
  generically width sized; and
* small hierarchy boundary terms can be amplified by nonlinear feedback.

The cyclic-space observation explains why another fixed neuron dictionary is
the wrong route. It does not rule out nonlinear scalar aggregates, because a
scalar system need not reconstruct every action vector.

## 8. A precise sufficient theorem for true width-free scalarization

The existing clipped-hierarchy proof would become width uniform under three
additional estimates. Let \(H\) index output-reachable forest diagrams and
\(|H|\) denote their complexity. It is enough to establish, for every fixed
horizon \(T\),

1. a true-diagram envelope
   \[
   \sup_n\sup_{t\le T}|q_H^{(n)}(t)|\le R_T^{|H|};
   \tag{9}
   \]
2. the same envelope for the clipped cutoff systems, with generator
   dependency and Lipschitz constants independent of \(n\); and
3. width-uniform initialization of every fixed finite diagram list, either
   from the realized contractions or from a controlled population limit.

The hierarchy comparison would then have the normalized form

\[
 E_s^{(n)}(t)
 \le C_Ts\int_0^t E_{s+\Delta}^{(n)}(u)\,du,
\tag{10}
\]

where \(C_T,\Delta\) do not depend on \(n\). Iterating (10) through the
distance from the requested output to the cutoff yields

\[
 \sup_n\sup_{t\le T}
 |\widehat O_{K}^{(n)}(t)-O_P^{(n)}(t)|
 \le \varepsilon_K(T),
\qquad \varepsilon_K(T)\to0.
\tag{11}
\]

Equation (11) is exactly the desired width-removal theorem while retaining all
\(m\) samples. The missing work is therefore identifiable: replace
entrywise/maximal bounds involving the realized \(W_0\) by normalized
population, operator and Gaussian-concentration estimates strong enough to
make (9)--(10) uniform.

The exponential envelope in (9) is sufficient but may be too strong for raw
unbounded Gaussian marks at arbitrarily high diagram order: Gaussian
\(p\)-norms grow like \(\sqrt p\). A viable proof may instead use
order-dependent weights \(\omega_{|H|}\) reflecting Gaussian or factorial
moment growth and establish the analogue of (10) after dividing each
coordinate by \(\omega_{|H|}\). Hypercontractive or Hermite-chaos estimates
are natural candidates. This changes the bookkeeping and possible cutoff
rate, but not the need to control both hierarchy-tail production and its
nonlinear amplification.

An alternative sufficient route is a finite causal realization of the
initialized Gaussian source/response system. Its state size may depend on
\(m,P\) but not \(n\). This requires a controlled predictive-rank tail and a
current-state coefficient law; one-time Gaussian covariance is insufficient.

## 9. A moving representative-population alternative

Instead of going directly to scalars, one may approximate each empirical
neuron law by \(K\ll n\) weighted representative states. Each representative
would carry its responses over all \(m\) samples and all \(P\) history
coordinates, and would move under the reduced dynamics. This does not freeze
neuron directions.

Such a method is principled only after the initialized-operator coupling has
been expressed through a valid common Gaussian source/response law or another
closed population operator. Independently subsampling neurons, redrawing
\(W_0\), or applying a linear sketch before a pointwise activation does not
preserve the parent dynamics. Under a Lipschitz population law in a Wasserstein
or suitable weak metric, particle/quantization error could be propagated on a
finite horizon, giving \(K=K(\varepsilon,m,P,T)\) independent of \(n\). The
required closed law and stability estimate are not currently available for
the full finite-width response-memory system.

## 10. Resolution

* **NTK/frozen features:** yes. Training outputs and any predeclared finite
  query set have an exact \(n\)-independent kernel ODE. Exact finite-width
  whole-domain evaluation may still require the feature bank.
* **One-hidden-layer linear network:** yes. The exact closure (4) removes
  width while retaining feature learning.
* **Generic deeper linear network:** not as a fixed finite scalar system.
  Width is naturally replaced by a spectral measure or operator population.
  Finite spectral quadrature can be a convergent approximation.
* **General nonlinear feature population:** no universal exact smooth finite
  scalar closure on an open state family. The one-sample tanh theorem
  (W1)--(W8) forces state dimension at least \(n\). Restricted invariant
  families and finite-accuracy approximations remain possible.
* **Current response-memory closure:** a fixed-\(n\) convergent scalar
  hierarchy exists, but an economical cutoff uniform in \(n\) is open. The
  precise positive target is (9)--(11), not another frozen neuron dictionary.

The strongest next width-only theory project is to prove or disprove the
uniform forest envelopes in (9) for fixed \(m,P,T\). The strongest practical
intermediate project is a moving representative population coupled to an
exact shared initialized-operator transcript. Both begin from the successful
response-memory closure and preserve its evolving learned directions.

## Claim status

Exact here: NTK finite-query closure, two-factor linear closure, the
three-factor invariants and spectral reduction, the aggregate fibre criterion,
the one-sample tanh jet-rank obstruction, its moving-atom approximation
estimate, and the implication from uniform hierarchy estimates (9)--(10) to
width-uniform convergence.

Established internally elsewhere in this study: the finite-width forest
hierarchy and clipped finite-horizon convergence at each fixed \(n\), together
with the two-sided initialized-operator consistency and cyclic-subspace
obstruction.

Open: width-uniform scalar cutoff for the nonlinear response-memory closure,
a small causal realization of reused \(W_0\), and a closed representative-law
solver with a propagated error bound.
