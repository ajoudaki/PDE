# Fresh noise at exact p=1: escape, a population obstruction, and the missing global bridge

Author: independent scoped agent `noise_escape`. Frozen candidate, 2026-09-19.
This is study research, not established material or a promotion review.

## Scope and conclusion

The assigned question is whether arbitrarily small fresh noise makes cubic
stationary points escape, and whether this can support a zero-loss theorem for
the exact p=1 population optimizer. No definition or data for the suggested
`batches3` setting were supplied in this route's scientific scope, so no claim
specific to that setting is made. Statements about minibatches below concern
ordinary sampling of the displayed finite data.
Only `docs/observable_p1.md` and `docs/NOTATION.md` were scientific inputs. Both
were read completely. Required skills and workflow instructions were also read.
No other route or study was read, and no numerical experiment was run.

There are three different, rigorously separable answers.

1. A Gaussian perturbation with support on a nonzero cubic descent polynomial
   decreases loss with probability tending to one half as its amplitude tends
   to zero. This applies to an explicit cubic stationary point of exact p=1.
   A nonzero Hilbert-valued additive Brownian noise also exits every fixed
   bounded neighborhood almost surely, although exit alone need not decrease
   loss.
2. Independent fresh noise at each population mark has different semantics.
   At an explicit cubic stationary point of exact p=1, such noise can preserve
   an entire family on which every individual-example gradient is exactly zero.
   This remains true when all three parameter blocks are perturbed and for
   every minibatch size. Thus “any fresh noise removes cubic stationary traps”
   is false without specifying which population correlations the noise creates.
3. Neither positive local statement proves loss convergence to zero from the
   canonical initialization. Persistent noise can repeatedly increase loss at
   regular interpolating states. Annealing requires a separate argument that
   the noise still escapes all relevant nonglobal stationary sets before it
   becomes ineffective, plus global control of trajectories. No such argument
   is established here.

The explicit trapped state below is not the canonical initialization
`(w,c,M)=(G,0,D)`. It refutes a universal local escape claim, not convergence
from that particular initialization. The report retains the complete nonlinear
p=1 model throughout its substantive examples.

## 1. Exact population model and well-posed additive perturbations

Fix the exact bounded feature columns `b1,b2` in the assigned source, with
dimensions `K1=2d+1`, `K2=d+1`. Let

\[
\mathcal H=L^2(\Omega_1;\mathbb R^d)\oplus L^2(\Omega_2)
 \oplus\mathbb R^{K_2\times K_1},\qquad \theta=(w,c,M),
\]

with the population L2 and Frobenius inner products. For finite data
`(u_a,y_a,mu_a)`, `mu_a>=0`, `sum mu_a=1`, define

\[
a_a=E_1[b_1\tanh(w\cdot u_a)],\quad
h_a=\tanh(b_2^TM a_a),\quad f_a=E_2[c h_a],\qquad
\mathcal L=\sum_a\mu_a(f_a-y_a)^2.
\]

The population equations here are the expectation version of the source's
displayed finite equations; no finite-particle approximation is used. Put

\[
\upsilon_a=E_2[b_2c(1-h_a^2)],\quad
q_a=b_1^TM^T\upsilon_a.
\]

Differentiation under these finite expectations is justified by bounded
features and tanh derivatives, Cauchy–Schwarz for the L2 fields, and finiteness
of the data. The gradient is

\[
\begin{split}
\nabla_w\mathcal L&=2\sum_a\mu_a r_a
 (1-\tanh^2(w\cdot u_a))q_a u_a,\\
\nabla_c\mathcal L&=2\sum_a\mu_a r_a h_a,\\
\nabla_M\mathcal L&=2\sum_a\mu_a r_a\upsilon_a a_a^T,
\qquad r_a=f_a-y_a.
\end{split}
\]

These formulas define a locally Lipschitz map `H -> H`. Indeed `w -> a_a`
is Lipschitz by bounded `b1` and the one-Lipschitz property of tanh. On bounded
sets, `b2^T M a_a` and its changes are uniformly bounded pointwise; so are their
tanh and gate changes. The changes in `upsilon_a` are then bounded by the L2
change in `c` and the uniform change of the gate. In the `w` gradient, `q_a`
is bounded pointwise on bounded sets and the gate changes are bounded in L2
by `2|u_a| ||delta w||_2`. These estimates give local Lipschitz bounds for
each displayed component. No assertion of a globally C2 loss on L2 is needed.

There is no finite-time explosion for an additive continuous H-valued forcing.
For completeness, set `A=||b1||_L2`, `B=||b2||_L2`,
`U=max_a |u_a|`, and `Y=max_a |y_a|`. Directly from the formulas,

\[
\begin{split}
\|\nabla_c\mathcal L\|_2&\le 2(\|c\|_2+Y),\\
\|\nabla_M\mathcal L\|_F&\le 2AB(\|c\|_2+Y)\|c\|_2,\\
\|\nabla_w\mathcal L\|_2&\le 2UAB(\|c\|_2+Y)\|c\|_2\|M\|_F.
\end{split}
\]

For `theta(t)=theta(0)-int_0^t grad L(theta(s)) ds+Z(t)`, local existence
and uniqueness follow by the contraction argument for an integral equation
with locally Lipschitz drift and continuous forcing. On each finite interval
the continuous `Z` is bounded. The first inequality and the integral Gronwall
inequality bound `c`; the second then bounds `M`; the third bounds `w`.
Consequently the local solution extends over that interval. This argument also
applies pathwise to additive Hilbert Brownian forcing with continuous paths.

Two natural stochastic optimizers covered below are exact gradient flow between
independent additive kicks, and

\[
d\theta_t=-\nabla\mathcal L(\theta_t)\,dt+\sigma\,dW_t^Q,
\]

where `W^Q` is an H-valued Brownian motion with a positive trace-class covariance
`Q`. These are changes of optimizer, not changes of p=1 architecture or a
global random-search replacement. The initial state is explicitly specified
for each result; statements from arbitrary states are not initialization
theorems for `(G,0,D)`.

## 2. What coherent additive noise proves locally

### Cubic descent probability

Let `V` be a finite-dimensional subspace of bounded field perturbations and
matrix perturbations. Suppose at `theta_*` the restriction of the loss has

\[
\mathcal L(\theta_*+v)=\mathcal L(\theta_*)+P_3(v)+o(\|v\|^3),
\quad v\in V,
\]

where `P3` is a nonzero homogeneous cubic polynomial. If `Z` is any centered
nondegenerate Gaussian in `V`, then

\[
\lim_{\varepsilon\downarrow0}
\mathbb P\{\mathcal L(\theta_*+\varepsilon Z)
                  <\mathcal L(\theta_*)\}=\tfrac12.
\]

Proof. For each fixed `Z`, the loss difference divided by `epsilon^3`
converges to `P3(Z)`. A nonzero polynomial is zero on a set of Lebesgue measure
zero: induct on dimension, treating it as a polynomial in the last variable;
outside the zero set of a nonzero coefficient polynomial, it has finitely many
roots, and integration over the remaining variables proves the claim. The
Gaussian has a density, so `P3(Z)` is nonzero almost surely. The symmetry
`Z ~ -Z` and oddness `P3(-Z)=-P3(Z)` give equal positive and negative
probabilities. Dominated convergence of the corresponding indicators completes
the proof. In particular the descent probability is at least `1/4` for all
sufficiently small positive amplitudes, with the threshold depending on the
particular cubic and remainder.

This is a one-kick descent theorem, not a theorem that the subsequent iterates
cannot return or approach a different stationary point. It requires no negative
Hessian eigenvalue.

### An explicit cubic in exact p=1

Let `theta_*=(0,0,0)` and suppose

\[
m_y:=\sum_a\mu_a y_a u_a\ne0.
\]

Choose any nonconstant lower feature `b1_j` and upper feature `b2_i`. They are
bounded, mean zero, and have positive squared expectations by the exact
Gaussian construction in the source. Set `v=m_y`, and consider

\[
w=\varepsilon A_0 b_{1,j}v,\qquad
c=\varepsilon C_0 b_{2,i},\qquad
M=\varepsilon B_0 e_i e_j^T.
\]

Here `A0,B0,C0` are scalar perturbation coordinates, not initialized population
operators. For every fixed triple, boundedness of the features gives

\[
\begin{split}
(a_a)_j&=\varepsilon A_0 E_1[b_{1,j}^2](v\cdot u_a)
              +O(\varepsilon^3),\\
f_a&=\varepsilon^3 A_0B_0C_0
 E_1[b_{1,j}^2]E_2[b_{2,i}^2](v\cdot u_a)+O(\varepsilon^5).
\end{split}
\]

The first identity is tanh's expansion in the lower argument. The upper
argument is of order `epsilon^2`; its cubic remainder, multiplied by `c`,
is of order `epsilon^7`, and the lower remainder supplies the displayed
`epsilon^5` error. Thus, with `K=E1[b1_j^2] E2[b2_i^2]>0`,

\[
\mathcal L(\theta)-\mathcal L(0)
=-2\varepsilon^3 A_0B_0C_0K\,\|m_y\|^2+O(\varepsilon^5).
\]

All first and second derivatives on this slice vanish and the cubic is
nonzero. The full gradient and Hessian at the origin vanish as well:
`|a_a|<=A|u_a| ||w||_2`, `||h_a||_2<=B ||M||_F |a_a|`, and
`|upsilon_a|<=B ||c||_2` in the gradient formulas show
`||grad L(theta)||=O(||theta||^2)` near zero. Thus the gradient is differentiable
at zero with derivative zero. Hence this is an actual p=1 stationary point with a cubic descent
direction. Independent Gaussian `A0,B0,C0` give the preceding one-half limit.
The directions are odd in their own original population marks, and the middle
entry is between nonconstant features; they also respect the sign symmetry
described in the source. This is not a scalar model substituted for p=1.

If `m_y=0`, this particular cubic vanishes. No general classification of higher
order stationary points is inferred.

### Repeated kicks and bounded-neighborhood exit

Two useful local conclusions need even less structure.

First, suppose `L(theta_*+h)<L(theta_*)` for a perturbation `h` in the support
of a kick law. By continuity choose `delta>0`, `rho>0`, and `eta>0` such that

\[
\|x-\theta_*\|<\delta,\quad \|z-h\|<\rho
\quad\Longrightarrow\quad
\mathcal L(x+z)\le\mathcal L(\theta_*)-\eta.
\]

If independent kicks have probability `p>0` of the ball `B(h,rho)`, then,
conditionally on any past for which the next pre-kick state is in
`B(theta_*,delta)`, the next kick reaches that lower loss with probability at
least `p`. Iterating conditional probabilities shows that the probability of
remaining in this neighborhood at all `n` pre-kick times while never achieving
that lower loss is at most `(1-p)^n`. Exact gradient-flow intervals between
kicks are allowed. The alternative “leaves the neighborhood” does not itself
certify descent.

A Gaussian series `Z=sum_j sqrt(q_j) g_j e_j` with every `q_j>0` and
`sum q_j<infinity` has full H support. To verify the needed small-ball fact,
approximate a target by its first `N` basis components. A finite Gaussian
vector has positive probability of a chosen small ball about those components.
Independently, the tail's squared norm has expectation `sum_{j>N} q_j`, so
Markov's inequality makes a sufficiently small tail event have positive
probability for sufficiently large `N`. Their intersection has positive
probability. Finite-rank noise is enough when `h` belongs to its range.

Second, let `sigma>0` and `Q!=0` in the diffusion above. Let `tau` be first
exit from the H ball of radius `R>0` about a fixed center, starting in the ball.
Choose a unit vector `e` with `q=<e,Qe>>0`. Local boundedness of the drift on
this ball follows from Section 1; write
`|<e,grad L>|<=B` there. For any `Delta>0`, set

\[
p=\mathbb P\!\left\{N(0,1)>
\frac{2R+B\Delta}{\sigma\sqrt{q\Delta}}\right\}>0.
\]

Then

\[
\mathbb P\{\tau>n\Delta\}\le(1-p)^n,
\qquad E\tau\le\Delta/p<\infty.
\]

Proof. On a path that stays in the ball throughout one block, its scalar
endpoint displacement is at most `2R`, and its scalar integrated drift is at
most `B Delta` in absolute value. The Brownian increment therefore cannot
exceed `2R+B Delta` after multiplication by `sigma sqrt(q)`. A larger
increment, independent of the past, forces exit during that block. Conditional
iteration gives the tail bound; integration of that bound gives the expectation.
This elementary argument needs neither a strict saddle nor full noise support.
It proves spatial exit, not useful loss progress. Its bound deteriorates as
`sigma` tends to zero; it supplies no uniform escape-time guarantee.

## 3. Exact obstruction for fresh independent population-mark noise

An atomless population does not admit an H-valued Gaussian with covariance the
identity on its infinite-dimensional L2 space. In an orthonormal basis such a
Gaussian would have independent standard-normal coordinates `g_j`. Almost
surely infinitely many satisfy `|g_j|>=1`: for each fixed starting index, the
probability that all subsequent coordinates have magnitude less than one is
the limit of powers of a number strictly less than one, hence zero. Its squared
Hilbert norm would therefore be infinite. Trace-class covariance, with decaying
coordinate variances, is essential for the H-valued Gaussian construction.
In particular, no positive trace-class covariance can bound below a positive
multiple of the identity in this space.

There is nevertheless a precise and natural interpretation of fresh independent
noise *for each population mark*: enlarge each population probability space by
countably many independent standard Gaussian marks. Their expectations remain
part of the exact population expectation. This describes a distribution of
independently perturbed neurons, not a single common H-valued Gaussian draw.
The two operations have different covariance and averaging semantics.

Here is a counterexample within that interpretation. Begin at

\[
w_0=0,\qquad c_0=0,\qquad M_0=0.
\]

For every step `n`, append fresh lower vectors `xi_n~N(0,I_d)` independent of
the frozen lower features and all earlier lower marks, and fresh upper scalars
`zeta_n~N(0,1)` independent of the frozen upper features and earlier upper marks.
Use any finite deterministic noise amplitudes `sigma_n,tau_n` and any gradient
step sizes. Add `sigma_n xi_n` to `w` and `tau_n zeta_n` to `c`, either before
or after each gradient step. Allow any sequence of middle matrices, including
independent arbitrarily small full-matrix Gaussian kicks. Common matrix
randomness is independent of the individual population marks and is conditioned
on when taking population expectations.

At every finite step,

\[
w_n=\sum_{k<n}\sigma_k\xi_k,\qquad
c_n=\sum_{k<n}\tau_k\zeta_k,
\qquad f_a=0,\qquad \nabla\ell_a=0\quad\text{for every }a,
\]

where `ell_a=(f_a-y_a)^2`. The matrices `M_n` may be arbitrary as just stated.
In particular `L_n=sum_a mu_a y_a^2` forever.

Proof by induction. The lower field is symmetric about zero and independent of
`b1`, so for every `u_a`,

\[
a_a=E_1[b_1] E_1[\tanh(w_n\cdot u_a)]=0.
\]

Thus `h_a=0` and `f_a=0`, regardless of `M_n`. The upper readout has zero mean
and is independent of `b2`, so

\[
\upsilon_a=E_2[b_2c_n]=E_2[b_2]E_2[c_n]=0.
\]

The individual-example `c` gradient vanishes because `h_a=0`; its `M`
gradient vanishes because `a_a=upsilon_a=0`; its `w` gradient vanishes because
`q_a=0`. Hence the gradient step changes nothing, and the next fresh independent
Gaussian increments preserve symmetry, centering, and independence from the
frozen features. This proves the induction. Every finite step remains in H.
The same induction allows exact gradient-flow intervals, since their drift is
identically zero at each such state.

When `m_y!=0`, the starting point is exactly the cubic stationary point verified
in Section 2, with arbitrarily close lower-loss states, so it is not a local
minimum. That moment condition alone does not establish representability of
an arbitrary target. The following single-input example supplies an exactly
representable target for the obstruction: for a single nonzero input and
nonzero label, a finite zero-loss p=1 state exists:
choose `w=b1_j u`, `M=e_i e_j^T`; then `(a)_j>0`, and
`E2[b2_i tanh(b2_i (a)_j)]>0`. A scalar multiple of `c=b2_i` fits the label
exactly. The noise-only trajectory still has its original positive loss.

The gradient is zero separately for each datum. Therefore random batches of
three, random single examples, or any other minibatch rule cannot repair this
counterexample. It also survives omission of the constant feature and the
simultaneous sign-pairing symmetry, with each fresh mark included in the sign
negation.

For finite particle counts, empirical averages of these independent marks
usually do not vanish exactly. Those fluctuations can seed other behavior.
That observation supplies no exact-population escape theorem and no license
to interchange the population limit with infinite training time.

## 4. Fixed noise, annealing, and the global zero-loss claim

Fixed noise is incompatible with an absorbing interpolating state whenever
the perturbation affects predictions. This can be seen exactly, without an
Itô formula: at any interpolator `theta_*`, add only `epsilon Z z` to its
readout, for `Z~N(0,1)` and `z in L2(Omega2)`. Then

\[
\mathcal L(w_*,c_*+\varepsilon Zz,M_*)
=\varepsilon^2Z^2\sum_a\mu_a(E_2[z h_{*,a}])^2.
\]

Whenever the last sum is positive, every nonzero fixed amplitude produces
positive loss almost surely. This alone does not rule out loss convergence
along unbounded representations, where noise sensitivity might vanish.

A more persistent version applies to exact all-block gradient flow between
fresh readout kicks `epsilon Z_n`, where `Z_n` are independent centered
L2-valued Gaussians with covariance `Q_c`. Suppose for some datum with
`mu_a>0`, all sufficiently late pre-kick feature states satisfy

\[
\langle h_a,Q_c h_a\rangle\ge v_0>0.
\]

Conditioned on the past, the post-kick residual of this datum is normal with
an arbitrary mean and variance at least `epsilon^2 v0`. A normal interval of
fixed length has maximal mass when centered at its mean (differentiate its
integral with respect to the interval center). Therefore for every `b>0`,

\[
\mathbb P\{\mathcal L_{n,+}\ge\mu_a b^2\mid\text{past}\}
\ge 2\bigl[1-\Phi(b/(\varepsilon\sqrt{v_0}))\bigr]>0.
\]

Repeated conditional multiplication shows that these positive-loss events
occur infinitely often almost surely: the probability of avoiding them for
all steps after any fixed index is zero, and one takes the countable union over
indices. Thus the post-kick losses cannot converge to zero under this variance
condition. For a strictly positive covariance `Q_c`, the condition holds in a
neighborhood of any finite interpolator with a nonzero label: its corresponding
`h_a` is nonzero, so its quadratic form is positive, and the features depend
continuously on the state. This is a conditional obstruction for the actual
p=1 optimizer, not a frozen-feature optimization theorem.

Annealing can remove this obstruction, but requires additional work. The local
diffusion bound in Section 2 gives a success probability depending on the noise
amplitude; with decaying amplitudes these probabilities can be summable. The
conditional-product argument then no longer proves almost-sure escape. The
completely degenerate cubic point exhibited above has no linearly unstable
Hessian direction, so a theorem proved only for negative Hessian eigenvalues
cannot be invoked to fill this gap.

Zero loss also requires data compatibility. For every p=1 state, `f(0)=0` and
`f(-u)=-f(u)`, by oddness of both tanh layers. Duplicate or sign-paired inputs
with incompatible labels cannot have zero loss. Compatibility alone has not
been proved sufficient for this optimizer, and no assumption of a uniformly
positive feature Gram or global gradient-dominance bound is silently made.

For an affirmative canonical-initialization theorem, the unresolved bridges
are consequently precise:

- specify the data class and prove attainable zero loss in exact p=1;
- specify whether randomness is common field noise, independent population-mark
  noise, data sampling, or some combination, and its covariance and annealing;
- prove avoidance of every accessible positive-loss stationary set, including
  degenerate sets, under that exact noise mechanism;
- rule out approach to positive-loss states at infinity or other failures of
  the compactness needed to pass from trajectory estimates to limit states;
- show that the noise-induced loss increments vanish strongly enough to obtain
  loss convergence, rather than merely occasional escape or a best-ever value.

This route closes a local question and exposes a model-specific noise
obstruction. It leaves global zero-loss convergence from `(G,0,D)` open.

## Provenance and check status

The complete arguments above were derived and manually checked by the author;
no independent scientific review is claimed. Checks included the individual
per-example gradients, the cubic coefficient and powers of epsilon, feature
positivity, trace-class versus population-mark semantics, the conditional
probability iterations, and the distinction between the displayed counterexample
initialization and the canonical initialization. No external specialized theorem
was invoked; local integral-equation contraction, elementary Gaussian facts,
Gronwall, Cauchy–Schwarz, Markov, and dominated convergence are used in the
forms stated or applied above.

Input hashes at derivation:

```
0f9c0ab9d1bcd6acd844cfce52e00d94c063843fcf80d27e7ba2b7ea6ebdfbba  docs/observable_p1.md
199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b  docs/NOTATION.md
0906284c80dced0b2ee1beaf7c5f160a12d17f41afd060a536eeac0903406f85  RESEARCH_WORKFLOW.md
HEAD 019e3630237e33f58b9636c0aa67a039bebf0182
```

Before writing, the Git index was empty; unrelated modified paths were left
untouched. Only this assigned report was written. A metadata-only agent-list
query unexpectedly included an unrelated completed review summary; it was
disclosed to the supervisor and not used as scientific input. No other route's
approach or verdict was read before freezing this report.

Post-freeze correction by the lead, following isolated review: the sentence
in Section 3 that treated m_y!=0 as implying representability was narrowed.
The moment condition proves cubic descent only; the immediately following
single-input construction proves representability for that example. No
equation or stochastic argument changed. The original frozen report hash
was fd1f2cc0341d31b69ececd768b7d2bdcfb7b50dda4f4fc7219060555a497a3de.
