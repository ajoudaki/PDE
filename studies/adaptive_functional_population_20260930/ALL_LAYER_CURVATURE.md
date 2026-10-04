# All-layer curvature and backward variation

Scoped theory attempt, 2026-09-30. The scientific input was the supervisor's
assignment. No experiments or scientific retrieval were performed.

**Exposure note.** After the derivations and first draft were complete, the
supervisor reported that a current book section already contains learned
reverse-memory smoothing and an adapted Gaussian-column obstruction. This
agent did not open that section or import its arguments. The corresponding
results below were independently derived before that notice; they should
not be reported as newly discovered relative to the maintained book.

## Conclusion and contract

The canonical gradient flow has more width-uniform structure than its energy
bound alone suggests: bounded readout coordinates, bounded hidden operator
norms, a nuclear-norm bound for every learned hidden matrix, and an
\(L^2\to L^\infty\) bound for its transpose. Every forward field and the top
backward field has bounded variation in normalized population \(L^2\),
uniformly in width. These statements hold on a fixed finite horizon,
conditional on bounded initial hidden operator norms, an event with a direct
Gaussian probability bound.

They do **not** alone yield quadratic centroid error for all backward
fields. The first missing estimate concerns products of a preactivation
variation and a correlated Gaussian backpropagated field. A bounded-state
example shows that bounded hidden operators and bounded readout coordinates
do not make backward responses uniformly Lipschitz in the normalized
parameter metric. It is not a reachable-trajectory counterexample.

The target remains the canonical fixed-depth network on \(0\le t\le T\),
with all forward and backward functions approximated, width-uniform
constants, and finite descriptors independent of data count. Population
\(L^2\) is admissible; uniform input error is stronger. A function such as
\(x\mapsto z_l(t,x)\) is not one finite scalar descriptor, and dense parameter
snapshots are not the requested efficient full-history encoding.

## 1. Exact finite-time bounds

All hidden widths are \(n\). Let \(P\) denote the population law, write
\(r_t=f_t-y\), and set
\[
 \mathcal L(t)=\mathbb E_P r_t^2,\qquad
 B_j=\|\phi^{(j)}\|_\infty\quad(0\le j\le3).
\]
Assume these bounds are finite, \(\|x\|/\sqrt d\le R\), and \(w(0)=0\).
Write
\[
 \|v\|_{p,n}=(n^{-1}\sum_i|v_i|^p)^{1/p},\qquad
 \|v\|_{p,P,n}=(\mathbb E_P\|v(x)\|_{p,n}^p)^{1/p},
 \qquad \langle u,v\rangle_n=u^\mathsf Tv/n .
\]
Let \(G_l=W_l(0)\) for \(l\ge2\). The speed in the gradient-flow metric is
\[
 e(t)^2=\|\dot W_1\|_F^2/n+
          \sum_{l=2}^L\|\dot W_l\|_F^2+\|\dot w\|_2^2/n .
\]
Differentiating the loss using the assigned gradients gives
\[
 \dot{\mathcal L}=-e^2,\qquad
 \int_0^T e^2\,dt\le\mathcal L(0),\qquad
 \int_0^T e\,dt\le\sqrt{T\mathcal L(0)}.                 \tag{1}
\]
In particular, \(\mathcal L(t)\le\mathcal L(0)=\mathbb E y^2\). Bounded
activations and the readout equation give, coordinatewise,
\[
 |\dot w_i|\le2B_0\sqrt{\mathcal L(0)},\qquad
 \|w(t)\|_\infty\le M:=2B_0T\sqrt{\mathcal L(0)}.       \tag{2}
\]
For hidden matrices,
\[
 \sup_{t\le T}\|W_l(t)\|_{\rm op}
 \le K_l:=\|G_l\|_{\rm op}+\sqrt{T\mathcal L(0)}.       \tag{3}
\]
Indeed, integrate \(\|\dot W_l\|_{\rm op}\le\|\dot W_l\|_F\le e\).

Define
\[
 p_L=w,\qquad p_l=W_{l+1}^{\mathsf T}\delta_{l+1}
 \quad(l<L),\qquad \delta_l=\phi'(z_l)\odot p_l.
\]
Starting with \(D_L=B_1M\), put \(D_l=B_1K_{l+1}D_{l+1}\). Diagonal
multiplication and the Euclidean matrix norm prove
\[
 \sup_{t,x}\|\delta_l(t,x)\|_{2,n}\le D_l,\qquad
 \sup_{t,x}\|p_l(t,x)\|_{2,n}\le K_{l+1}D_{l+1}
 \quad(l<L).                                         \tag{4}
\]
These bounds are uniform in input and hence imply population bounds.

Here is an elementary probability estimate for (3). For an \(n\times n\)
matrix \(G\) with iid \(N(0,1/n)\) entries, two \(1/4\) sphere nets can each
have at most \(9^n\) elements. A maximal separated set has this cardinality
by packing disjoint radius \(1/8\) balls inside the radius \(9/8\) ball.
Approximating both arguments of \(u^\mathsf TGv\) gives
\(\|G\|_{\rm op}\le2\max_{\rm nets}|u^\mathsf TGv|\). Each fixed bilinear
form is \(N(0,1/n)\), so
\[
 \Pr(\|G\|_{\rm op}>a)
 \le2\exp\{2n\log9-na^2/8\}.                          \tag{5}
\]
Taking \(a=8\) and a union bound over the fixed number of hidden matrices
gives width-independent constants in (2)--(4), except on an event of
probability at most \(2(L-1)e^{-n(8-2\log9)}\).
This says nothing about independence of trained fields and initial matrices.

## 2. Extra structure of the learned hidden matrices

For \(l\ge2\), integrating the exact flow gives
\[
 A_l(t):=W_l(t)-G_l
 =-2\int_0^t\mathbb E_P\left[
      r_s\,\frac{\delta_l(s,x)h_{l-1}(s,x)^\mathsf T}{n}\right]ds. \tag{6}
\]

For any vector \(v\), Cauchy--Schwarz first in neuron index and then in \(P\)
gives, coordinatewise,
\[
 \begin{split}
 |[A_l(t)^\mathsf Tv]_j|
 &\le2B_0\int_0^t
       \mathbb E_P[|r_s|\,|\langle\delta_l(s,x),v\rangle_n|]\,ds\\
 &\le S_l\|v\|_{2,n},\qquad
 S_l:=2B_0T\sqrt{\mathcal L(0)}D_l .
 \end{split}
\]
Consequently
\[
 \|A_l(t)^\mathsf T\|_{(2,n)\to\infty}\le S_l.        \tag{7}
\]
The same proof without time integration gives
\(\|\dot W_l(t)^\mathsf T\|_{(2,n)\to\infty}
 \le2B_0\sqrt{\mathcal L(0)}D_l\).
Thus a large concentrated coordinate of \(p_{l-1}\) must come from
\(G_l^\mathsf T\delta_l\), rather than from the learned transpose.

The nuclear norm of each source in (6) is
\[
 \left\|\frac{\delta_lh_{l-1}^\mathsf T}{n}\right\|_*
 =\|\delta_l\|_{2,n}\|h_{l-1}\|_{2,n}\le D_lB_0 .
\]
Triangle inequality and Cauchy--Schwarz in \(P\) therefore prove
\[
 \sup_{t\le T}\|A_l(t)\|_*\le S_l.                    \tag{8}
\]
If \(A_l^{(k)}\) retains the largest \(k\) singular values, then
\[
 \|A_l-A_l^{(k)}\|_{\rm op}\le\frac{S_l}{k+1},\qquad
 \|A_l-A_l^{(k)}\|_F\le\frac{S_l}{\sqrt{k+1}}.        \tag{9}
\]
For \(k<n\), use
\(\sigma_{k+1}\le S_l/(k+1)\) and
\(\sum_{j>k}\sigma_j^2\le\sigma_{k+1}\sum_{j>k}\sigma_j\);
for \(k\ge n\) the error is zero.

Equation (9) is a static low-rank approximation theorem. It does not prove
closed causal evolution for the factors, preservation of all backward
responses, or an efficient encoding of the complete history.

## 3. Variation already controlled by energy

Put \(q_l=\dot z_l\), \(u_l=\dot h_l\). Exactly,
\[
 q_1=\dot W_1x/\sqrt d,\qquad
 u_l=\phi'(z_l)\odot q_l,\qquad
 q_l=\dot W_lh_{l-1}+W_lu_{l-1}\quad(l\ge2).         \tag{10}
\]
Thus
\[
 \|q_1\|_{2,n}\le Re,\qquad
 \|q_l\|_{2,n}\le B_0e+K_l\|u_{l-1}\|_{2,n},\qquad
 \|u_l\|_{2,n}\le B_1\|q_l\|_{2,n}.                 \tag{11}
\]
Every forward field therefore has variation at most
\(C\int_0^T e\le C\sqrt{T\mathcal L(0)}\), uniformly in input in normalized
\(L^2\), and also in joint population-neuron \(L^2\).

The same recursions, with finite differences, give width-uniform forward
Lipschitz bounds between states whose hidden operator norms are bounded,
in the parameter metric
\[
 \|\Delta\theta\|_H^2
 =\|\Delta W_1\|_F^2/n+
   \sum_{l=2}^L\|\Delta W_l\|_F^2+\|\Delta w\|_2^2/n. \tag{12}
\]
They also give the scalar output bound if the readout normalized \(L^2\)
norms are bounded. This is a first-order statement.

For the top backward field,
\[
 \dot\delta_L
 =\phi''(z_L)\odot q_L\odot w+\phi'(z_L)\odot\dot w. \tag{13}
\]
Using (2) and (11) yields \(\|\dot\delta_L\|_{2,n}\le Ce\), uniformly in
input. Next,
\[
 \dot p_{L-1}=\dot W_L^\mathsf T\delta_L+
                      W_L^\mathsf T\dot\delta_L,
 \qquad \|\dot p_{L-1}\|_{2,n}\le Ce.
\]
The exact general derivative is
\[
 \dot\delta_l=\phi''(z_l)\odot q_l\odot p_l+
                           \phi'(z_l)\odot\dot p_l. \tag{14}
\]
At \(l=L-1\), Hölder therefore proves
\[
 \|\dot\delta_{L-1}\|_{1,n}
 \le B_2\|q_{L-1}\|_{2,n}\|p_{L-1}\|_{2,n}
       +B_1\|\dot p_{L-1}\|_{2,n}\le Ce.             \tag{15}
\]
This controls normalized neuron \(L^1\), uniformly in input, and joint
population-neuron \(L^1\). It does not establish joint \(L^2\). At the next
backward step the term \(G_{L-1}^\mathsf T\dot\delta_{L-1}\) requires more
than the proved \(L^1\) bound.

## 4. Precise multiplication, tail, and curvature conditions

Norms in this section may be on the joint neuron-input probability space.
The basic product estimate is
\[
 \|u\odot v\|_2\le\|u\|_4\|v\|_4.                  \tag{16}
\]
Two normalized \(L^2\) bounds alone are insufficient: for
\(u=v=\sqrt n\,e_1\), both norms are one while
\(\|u\odot v\|_{2,n}=\sqrt n\).

There is also a weaker continuity route that does not require a full
\(L^4\) bound. If a response error contains
\(p[\phi'(z)-\phi'(\widetilde z)]\), split the event \(|p|\le K\) from its
complement. Bounded and Lipschitz \(\phi'\) yield
\[
 \|p[\phi'(z)-\phi'(\widetilde z)]\|_2
 \le B_2K\|z-\widetilde z\|_2+
       2B_1\|p\,1_{\{|p|>K\}}\|_2.                 \tag{17}
\]
A width-uniform squared-tail modulus for the *reachable* pre-multiplier
fields would consequently give uniform continuity. A mere bounded second
moment gives no such tail modulus. Even a tail modulus would not itself
give quadratic error.

For quadratic centroid error, let \(\mu\) be a positive finite measure of
mass \(m>0\), and let
\(\bar z=m^{-1}\int z\,d\mu\), \(\bar p=m^{-1}\int p\,d\mu\).
Pointwise Taylor expansion, first-moment cancellation, and Minkowski prove
\[
 \left\|\int\phi(z)\,d\mu-m\phi(\bar z)\right\|_2
 \le\frac{B_2}{2}\int\|z-\bar z\|_4^2\,d\mu.        \tag{18}
\]
For the backward local map, expand \(\phi'(z)\) about \(\bar z\) and write
\(p=\bar p+(p-\bar p)\). The two first-order terms integrate to zero.
The remainder obeys
\[
 \begin{split}
 &\left\|\int\phi'(z)\odot p\,d\mu
                   -m\phi'(\bar z)\odot\bar p\right\|_2\\
 &\quad\le\frac{B_3}{2}\|\bar p\|_4
                         \int\|z-\bar z\|_8^2\,d\mu
       +B_2\int\|z-\bar z\|_4\|p-\bar p\|_4\,d\mu .
 \end{split}                                      \tag{19}
\]
Indeed, the first remainder is bounded pointwise by
\((B_3/2)|z-\bar z|^2|\bar p|\), whose \(L^2\) norm is at most
\((B_3/2)\|z-\bar z\|_8^2\|\bar p\|_4\); the second is bounded by
\(B_2|z-\bar z||p-\bar p|\), to which (16) applies.

Thus \(L^8\)-small preactivation segments, \(L^4\)-small pre-multiplier
segments, and bounded \(L^4\) pre-multipliers give a width-uniform quadratic
remainder. Separate moment bounds are sufficient, not necessary: direct
mixed estimates on \(p(z-\bar z)^2\) could replace them.

Signed history measures require an explicit positive/negative split or
another justified construction. Applying (18)--(19) separately to the two
parts is valid, with total-variation mass in the error estimate. An
arbitrary signed barycenter need not lie inside its segment. Input-dependent
or vector-valued coefficients also need a finite representation; they are
not free scalar state variables.

For completeness, parameter-space curvature has the same issue. Along a
straight interpolation \(\theta(\alpha)=\theta+\alpha V\), primes denote
\(\alpha\)-derivatives:
\[
 \begin{aligned}
 z'_l&=V_lh_{l-1}+W_lh'_{l-1},&
 z''_l&=2V_lh'_{l-1}+W_lh''_{l-1},\\
 h''_l&=\phi''(z_l)(z'_l)^2+\phi'(z_l)z''_l,\\
 p'_l&=V_{l+1}^\mathsf T\delta_{l+1}
                          +W_{l+1}^\mathsf T\delta'_{l+1},&
 p''_l&=2V_{l+1}^\mathsf T\delta'_{l+1}
                          +W_{l+1}^\mathsf T\delta''_{l+1},\\
 \delta''_l&=\phi'''(z_l)(z'_l)^2p_l+\phi''(z_l)z''_lp_l
            +2\phi''(z_l)z'_lp'_l+\phi'(z_l)p''_l.
 \end{aligned}                                    \tag{20}
\]
Products are coordinatewise. At the first layer
\(z'_1=V_1x/\sqrt d,z''_1=0\); at the top
\(p_L=w,p'_L=V_w,p''_L=0\).

One explicit sufficient package for a uniform Hessian bound is, with
\(s=\|V\|_H\),
\[
 \|z'_l\|_8\le Cs,\quad \|z''_l\|_4\le Cs^2,\quad
 \|p_l\|_4\le C,\quad \|p'_l\|_4\le Cs,             \tag{21}
\]
together with bounded hidden operators throughout the interpolation.
The first three terms of \(\delta''_l\) are then bounded in \(L^2\) by
\(Cs^2\). The last is handled by backward induction using
\(\|V_l\|_{\rm op}\le s\); first backward derivatives are bounded from the
same package. Forward second derivatives obey the displayed \(h''_l\)
formula. This proves
\(\|h''_l\|_2+\|\delta''_l\|_2\le C_Ls^2\), conditional on (21).

Equation (21) is **not** a consequence of the preceding energy estimates.
Gaussian matrices are not width-uniform operators on normalized \(L^p\)
for arbitrary \(p>2\). For example, if \(g\) is their first row, choose
\(v_j=\operatorname{sign}(g_j)\). Then \(\|v\|_{p,n}=1\), whereas
\((Gv)_1=\sum_j|g_j|\), so
\(\|G\|_{(p,n)\to(p,n)}\ge n^{-1/p}\sum_j|g_j|\).
The latter is of order \(n^{1/2-1/p}\) in probability by the same
variance calculation used below in (23). Higher moment propagation requires control on the
specific correlated fields actually generated by the flow, not a global
Gaussian matrix estimate.

Even higher moments proved on the actual path would not automatically
justify the off-path parameter interpolations in (21). Field centroids
(18)--(19) avoid that assertion but leave their finite encoding unresolved.

## 5. Counterexamples to norm inferences; no reachable-path counterexample

Uniform \(L^2\to L^2\) curvature already fails for one activation. At
\(z=a\mathbf1\) with \(\phi''(a)\ne0\), take \(v=\sqrt n\,e_1\). Then
\[
 \|v\|_{2,n}=1,\qquad
 \|D^2\phi(z)[v,v]\|_{2,n}=|\phi''(a)|\sqrt n.       \tag{22}
\]
This does not contradict first-layer row-centroid estimates, which control
each row's displacement rather than one global normalized \(L^2\) distance.

A stronger bounded-state example concerns backward continuity. Use \(L=2\),
\(d=1,x=1,\phi=\tanh\). Let \(W_1=0\), let \(G=W_2\) have iid \(N(0,1/n)\)
entries, and choose \(w_i=\operatorname{sign}(G_{i1})\).
At this state \(h_1=z_2=0\), so \(\delta_2=w\) and
\((p_1)_1=\sum_i|G_{i1}|\).
Change only the first row of \(W_1\) from zero to fixed \(a\ne0\). Then
\[
 (\delta_1^{\rm new})_1
 =\operatorname{sech}^2(a)
    \sum_i|G_{i1}|\operatorname{sech}^2(G_{i1}\tanh a)
 \le\operatorname{sech}^2(a)\sum_i|G_{i1}|.
\]
Consequently
\[
 \|\delta_1^{\rm new}-\delta_1\|_{2,n}
 \ge\tanh^2(a)n^{-1/2}\sum_i|G_{i1}|,\qquad
 \|\theta^{\rm new}-\theta\|_H=|a|/\sqrt n.          \tag{23}
\]
Writing \(G_{i1}=Z_i/\sqrt n\), the first lower bound converges in probability
to \(\tanh^2(a)\mathbb E|Z|>0\), because the variance of
\(n^{-1}\sum|Z_i|\) is \(\operatorname{Var}(|Z|)/n\). Meanwhile (5) bounds the
hidden operator with probability tending to one. Readout coordinates are
bounded by one, and the learned matrix is zero, so its smoothing and nuclear
norm estimates also hold.

This falsifies the inference from those state bounds to a width-uniform
backward modulus in \(\|\cdot\|_H\) over arbitrary states. It does not
falsify such a modulus on the actual trained paths. The construction uses a
zero first layer and an adversarial readout correlated with one Gaussian
column. From \(W_1=0,w=0\) in this example, all activations and velocities
vanish, so that readout is not generated. A neural-path counterexample
would have to honor Gaussian first-layer initialization, a fixed permitted
population, and the entire coupled dynamics.

It is unjustified to apply independent-vector Gaussian estimates to
\(G_l^\mathsf T\delta_l(t,x)\) after training. Conversely, an adversarial
correlation possible in an ambient state ball is not evidence that the flow
creates it.

## 6. Claim status and remaining bottleneck

| Claim | Status | Scope |
|---|---|---|
| Hidden operator and backward \(L^2\) bounds | Proved | Fixed depth and horizon, Gaussian event (5), zero readout |
| Learned transpose \(L^2\to L^\infty\) estimate | Proved | Exact canonical gradient flow |
| Learned nuclear norm and static rank tails | Proved | Exact canonical gradient flow |
| All forward and top backward \(L^2\) variation | Proved | Uniform input, hence population |
| Penultimate backward \(L^1\) variation | Proved | Does not imply \(L^2\) variation |
| Quadratic centroid bounds with higher moments | Proved conditional estimate | Equations (18)--(19), positive measures or explicit sign split |
| Arbitrary-state backward continuity from the listed norm bounds | Falsified | Equation (23), not a trained-path example |
| Reachable higher moments or uniform squared-tail modulus | Open | Must preserve Gaussian/trained-field correlations |
| Efficient finite causal encoder for all response histories | Open | Neither static rank bounds nor function-valued centroids suffice |

The highest-leverage remaining target is a reachable-field estimate:
width-uniform population \(L^4\) control of \(p_l\), plus integrable
variation bounds for \(p_l\) in \(L^4\) and \(z_l\) in \(L^8\), would support
the local quadratic mechanism in (19). Direct mixed-product bounds could
be weaker and more useful. A squared-tail modulus as in (17) would already
supply a meaningful weaker continuity result, without claiming the desired
quadratic rate.

The exact learned-transpose smoothing isolates the unresolved contribution
in the correlated frozen Gaussian action. A conditional-independence or
leave-one-coordinate argument must prove its replacement error along the
coupled flow.

Even resolving this moment issue would close only the curvature/variation
gap. A complete encoder must construct finite descriptors for those fields,
control the history-source residual and its propagation, account for signed
weights and coefficient storage, and evolve from retained state. The
first-layer \(O(nd\,\varepsilon^{-1/2})\) count therefore does not yet extend
to arbitrary depth by this route. Failure of a global Hessian bound is not
an impossibility theorem for adaptive or weighted representations.
