# Independent lower-bound route

Frozen candidate, 2026-10-05. Author: scoped `dimension_lower` agent. Status:
the lemmas below have complete author derivations, but no independent check has
yet occurred. This is study material, not established book material.

The requested impossibility theorem is **not proved**. There is a rigorous
nonlinear-decoder lower-bound mechanism, but the required entropy or
small-ball estimate for actual learned neural trajectories is missing.
Moreover, at error proportional to the dense network's own root-width
fluctuations, tightness of those normalized fluctuations would prevent their
entropy from supplying a growing logarithmic lower bound. This is an
obstruction to that proof route, not a positive compression theorem.

## 1. Scope and the exact target

The scientific inputs were the supervisor's self-contained assignment, this
study's README, and `docs/notation.qmd`. No other route, study, archived book,
or maintained theorem chapter was read. Shared process instructions and the
`solve-math-rigorously` and `investigate-conjectures` skills, including the
research-contract and adversarial-audit references, were read. The required
canonical-notation skill at
`/home/amir/.codex/skills/explain-with-canonical-notation/SKILL.md` returned
permission denied; no accessible replacement was found in the available
skill directories. The explicit user rules and maintained notation contract
were applied instead.

A bibliographic search and the introduction/definitions of Petrova and
Wojtaszczyk's [Lipschitz widths](https://arxiv.org/abs/2111.01341) were consulted
to check the appropriateness of Lipschitz nonlinear decoders. No theorem from
that paper is imported: all inequalities used here are proved below. No
experiments or computation of network trajectories were performed.

Let

\[
 S_d=\{x\in\mathbb R^d:\|x\|_2=\sqrt d\},\qquad
 z^{(1)}(x)=W^{(1)}x/\sqrt d,\qquad
 z^{(\ell)}(x)=W^{(\ell)}h^{(\ell-1)}(x),\qquad
 h^{(\ell)}(x)=\phi^{(\ell)}(z^{(\ell)}(x)),
\]

where the last two definitions apply for hidden layers and $L\ge2$. The
prediction is

\[
 f_n(t,x)=\frac{(W^{(L+1)}(t))^T h^{(L)}(t,x)}n.
\]

The first matrix has independent $N(0,1)$ entries, hidden matrices have
independent $N(0,1/n)$ entries, and the stored readout is exactly zero at time
zero. This last convention is the assignment's explicit override of the
small random readout convention in the notation contract. There are $m\ge d$
correlated training inputs $x_a\in S_d$ that span $\mathbb R^d$. The loss is
$m^{-1}\sum_a(f_n(t,x_a)-y_a)^2$, and the block mobilities are
$(n,1,\ldots,1,n)$. Labels lie in the stated small-label regime and the
initialized feature Gram has the assumed positive gap. Activations are
nonlinear, analytic on a strip, with the prescribed bounded derivatives;
their values need not be bounded.

Write $F_n$ for the complete prediction trajectory when it exists in the
normed space of bounded functions on $[0,\infty]\times S_d$, with

\[
 \|F\|_{\infty}=\sup_{t\in[0,\infty],\,x\in S_d}|F(t,x)|.
\]

The value at infinity means the fitted endpoint if it exists. Any lower
bound can instead use one finite-time snapshot $f_n(t_*,\cdot)$: an all-time
approximation must approximate that snapshot. Thus the lower-bound lemmas
do not presuppose an all-time existence theorem. In the following, $X$ is
either this trajectory space or $C(S_d)$ with the supremum norm, and $F_n$
denotes the corresponding random observable.

For each fixed problem, width tends to infinity first. A failure probability
$\delta\in(0,1)$ is fixed. The central tolerance is
$\varepsilon_n=c_d n^{-1/2}$, with explicit discussion below of extra logarithms.
No claim here identifies this tolerance with the **actual** discrepancy of
independent dense runs. Such an identification requires a separate theorem.
Random observables and success events are assumed measurable throughout.

## 2. A legitimate nonlinear representation class

An admissible surrogate has a fixed algorithm, an initialization encoder
using only the data and the initial dense weights, and a retained descriptor.
The descriptor includes every instance-specific fixed coefficient, the
current evolving state, and any instance-specific decoder instructions or
tables. It determines autonomous subsequent evolution and predictions, and
can restart from its current state. Retained computational workspace is
included in its size. A retained dense oracle, future trajectory values,
time-indexed playback, and arbitrary-real digit encoding are excluded.

The following are two explicit subclasses on which the bounds apply.

1. **Finite precision.** At most $p$ retained words, each with at most $b$
   bits, determine the surrogate. The decoder may be nonlinear, discontinuous,
   adaptive, or computationally expensive, subject to the counted workspace
   and provenance restrictions. For a fixed public algorithm there are at
   most $2^{pb}$ possible decoded trajectories. If several algorithms can be
   chosen using instance information, their description bits count too.
2. **Bounded Lipschitz decoding.** The full retained descriptor is a vector
   $u\in[-R,R]^p$. For the snapshot or trajectory being considered, its decoder
   $D:[-R,R]^p\to X$ satisfies
   $\|D(u)-D(v)\|_X\le\Lambda\|u-v\|_\infty$. The encoder need not be continuous.
   The constants $R$ and $\Lambda$ must be stated; they are not free hidden
   resources. For the logarithmic-exponent consequence below, require
   $\log(2+R\Lambda/\varepsilon_n)=O_d(\log n)$.

The second class includes nonlinear autonomous systems whose retained
parameters determine the selected observable with this stability bound.
It does not include every conceivable autonomous algorithm: an all-time
Lipschitz bound can fail even when a finite-time bound holds. If using a
single snapshot, only stability at that time is required.

For the proofs we allow **all** decoders satisfying the corresponding
cardinality or Lipschitz bound, even if some would violate autonomy or
provenance. Enlarging the class only makes a lower bound stronger; it never
licenses an inadmissible positive construction. The arguments do not
restrict the surrogate to a fixed linear basis.

## 3. Complete decoder lower bounds

For a subset $\mathcal F\subset X$, let $P(\mathcal F,r)$ be the largest number
of its elements with all pairwise distances strictly greater than $r$.
For the actual random observable define the concentration function

\[
 Q_n(r)=\sup_{g\in X}\Pr\{\|F_n-g\|_X\le r\}.
\]

The supremum allows every deterministic center, including centers outside
the reachable neural family. Logarithms are natural unless marked otherwise.

### Lemma 1: finite precision

If a $p$-word, $b$-bit representation approximates every $F\in\mathcal F$ to
error $\varepsilon$, then

\[
 pb\ge\log_2 P(\mathcal F,2\varepsilon).
\]

If it instead succeeds for the actual random $F_n$ with probability at least
$1-\delta$, then

\[
 pb\ge\log_2\frac{1-\delta}{Q_n(\varepsilon)}. \tag{1}
\]

**Proof.** There are at most $2^{pb}$ decoded observables. One decoded
observable cannot lie within $\varepsilon$ of two targets whose distance is
greater than $2\varepsilon$, by the triangle inequality. This proves the
packing assertion. For the probability assertion, success is contained in
the union of at most $2^{pb}$ radius-$\varepsilon$ balls. The union bound
gives $1-\delta\le2^{pb}Q_n(\varepsilon)$, which is (1). Independent public
randomization does not change this conclusion: condition on the public
random seed, apply the same union bound, and average. Randomness correlated
with the dense initialization is instance information and must be counted.
$\square$

### Lemma 2: bounded Lipschitz nonlinear decoding

Suppose $R,\Lambda>0$, and $D$ satisfies the preceding Lipschitz condition.
If every $F\in\mathcal F$ is within $\varepsilon$ of some $D(u)$, then

\[
 p\ge
 \frac{\log P(\mathcal F,4\varepsilon)}
 {\log(2+2R\Lambda/\varepsilon)}. \tag{2}
\]

If the approximation succeeds for random $F_n$ with probability at least
$1-\delta$, then

\[
 p\ge
 \frac{\log((1-\delta)/Q_n(2\varepsilon))}
 {\log(2+2R\Lambda/\varepsilon)}. \tag{3}
\]

**Proof.** Divide each coordinate interval $[-R,R]$ into
$N=\lceil2R\Lambda/\varepsilon\rceil$ equal pieces, and use their endpoints.
There are $N+1\le2+2R\Lambda/\varepsilon$ endpoints per coordinate. Every
descriptor has a grid point within $\varepsilon/\Lambda$ in the maximum
norm, so its decoded output is within $\varepsilon$ of a decoded grid point.
Consequently every successfully approximated target lies in a
radius-$2\varepsilon$ ball centered at one of at most
$(2+2R\Lambda/\varepsilon)^p$ outputs. Such a ball contains at most one member
of a strictly $4\varepsilon$-separated target set, proving (2). Its probability
mass is at most $Q_n(2\varepsilon)$, so the union bound proves (3).
If $R=0$ or $\Lambda=0$, the decoder has one output and the direct one-ball
statement replaces these formulas. $\square$

These bounds apply to total retained parameters, not only evolving state.
Allowing exponentially large $\Lambda$ or an unbounded parameter range can
destroy the claimed parameter-count consequence. Merely saying “nonlinear
decoder” or “continuous decoder” does not establish (2) with a useful
denominator. The finite-precision lemma avoids that regularity issue.

## 4. What would produce a dimension-linear logarithmic exponent?

Here is a precise **conditional** route. It makes the missing neural
reachability statement explicit instead of replacing it by generic
analytic-function entropy.

Let $\mathcal P_k(S_d)$ be the restrictions to $S_d$ of real polynomials of
total degree at most $k$. For $d\ge2$ its dimension is

\[
 M_d(k)=\binom{d+k}{d}-\binom{d+k-2}{d}
       =\binom{d+k-1}{d-1}+\binom{d+k-2}{d-1}. \tag{4}
\]

Terms with negative top index are zero. To verify (4), the unrestricted
polynomial space has dimension $\binom{d+k}{d}$. Its restriction kernel is
exactly $(\|x\|_2^2-d)$ times the degree-at-most-$k-2$ polynomials. For the
nontrivial inclusion, divide a vanishing polynomial by the monic polynomial
$x_d^2+\sum_{j<d}x_j^2-d$, treating it as a polynomial in $x_d$. The remainder
is $a(x')x_d+b(x')$. Evaluation at
$x_d=\pm\sqrt{d-\|x'\|_2^2}$ for $\|x'\|_2<\sqrt d$ forces $a=b=0$ on an
open set, hence identically. Polynomial division preserves the claimed total
degree bound on the quotient. Subtracting dimensions and applying Pascal's
identity proves (4). In particular, for fixed $d$,

\[
 M_d(k)\sim\frac{2}{(d-1)!}k^{d-1}\quad(k\to\infty). \tag{5}
\]

Use normalized surface measure on $S_d$, and choose an orthonormal basis
$e_1,\ldots,e_{M_d(k)}$ of $\mathcal P_k(S_d)$. Define the coefficient map
$T_k:C(S_d)\to\mathbb R^{M_d(k)}$ by
$[T_kf]_j=\int_{S_d}f(x)e_j(x)\,d\sigma(x)$. Orthogonal projection and the
normalization of $\sigma$ give

\[
 \|T_kf-T_kg\|_2\le\|f-g\|_{L^2(\sigma)}
                    \le\|f-g\|_\infty. \tag{6}
\]

**Conditional hypothesis.** For the actual family $\mathcal F_n$ of neural
snapshots that a uniform representation must cover, suppose

\[
 T_k\mathcal F_n\supset c_{n,k}+e^{-\alpha_d k} B_2^{M_d(k)} \tag{7}
\]

for the degrees used below, where $B_2^M$ is the Euclidean unit ball and
$\alpha_d>0$ is independent of $n$. This means independently variable
coefficient directions in the reachable family, not merely nonzero
coefficients of one function.

For $r>4\varepsilon$, a maximal strictly $4\varepsilon$-separated subset of
$rB_2^M$ covers that ball by closed radius-$4\varepsilon$ balls. Comparing
Euclidean volumes therefore gives at least $(r/(4\varepsilon))^M$ points.
Choose one neural preimage for each projected point in (7). Inequality (6)
preserves their separation in the supremum norm, and hence

\[
 \log P(\mathcal F_n,4\varepsilon)
 \ge M_d(k)\log\frac{e^{-\alpha_d k}}{4\varepsilon}. \tag{8}
\]

Take
$k=\lfloor\log(1/\varepsilon)/(2\alpha_d)\rfloor$. Then
$e^{-\alpha_d k}\ge\sqrt\varepsilon$, and the right side of (8) is at least

\[
 M_d(k)\bigl(\tfrac12\log(1/\varepsilon)-\log4\bigr)
 \ge b_d(\log(1/\varepsilon))^d \tag{9}
\]

for sufficiently small $\varepsilon$, with $b_d>0$ depending on $d$ and
$\alpha_d$. For example, once the floor and the final $\log4$ cost at most
factors of two, (4) gives the explicit permissible lower constant
$[4(d-1)!(4\alpha_d)^{d-1}]^{-1}$. The threshold also depends on $d$ and
$\alpha_d$.

At $\varepsilon=c_dn^{-1/2}$, (2) and a polynomial bound on $R\Lambda$ imply
$p=\Omega_d((\log n)^{d-1})$. For $b=O_d(\log n)$, Lemma 1 gives the same
word-count exponent. The finite-precision bit bound itself is
$\Omega_d((\log n)^d)$.

This is already a lower bound for nonlinear decoders. The sphere has
dimension $d-1$, which explains the parameter exponent $d-1$, rather than
blindly counting ambient monomials as $k^d$. As $d\to\infty$, $(d-1)/d\to1$.
Nothing in this argument supplies joint $d,n$ uniformity: the factorial,
$\alpha_d$, and large-$n$ thresholds have material dimension dependence.
For $d=1$ the sphere has two points and (5) is not the relevant asymptotic.

**Missing bridge.** No argument in the assignment or in this route proves
(7) for actual Gaussian-initialized learned trajectories. Strip analyticity
is an upper regularity constraint. It supplies neither independently
adjustable reachable coefficients nor an amplitude lower bound. Even if
(7) held over all initializations in the support, it would be a worst-case
statement and would not prove a high-probability Gaussian lower bound.
For that conclusion, a sufficient replacement is the genuinely
distributional estimate

\[
 Q_n(2\varepsilon_n)
 \le\exp[-b_d(\log n)^d]. \tag{10}
\]

Together with (3), (10) would prove the desired exponent within the
specified Lipschitz class. No such estimate is established here.

## 5. Why root-width random harmonics can fail decisively

### Lemma 3: tight normalized fluctuations have bounded root-scale entropy

Suppose there are deterministic centers $F_n^0\in X$ such that
$Z_n=\sqrt n(F_n-F_n^0)$ is uniformly tight in the norm of $X$: for every
$\eta>0$ there is a compact $K_\eta\subset X$ satisfying
$\inf_n\Pr(Z_n\in K_\eta)\ge1-\eta$. Then, for every fixed $c>0$ and
$\eta\in(0,1)$, there is an integer $N(c,\eta)$ independent of $n$ such that
$F_n$ is covered, with probability at least $1-\eta$, by
$N(c,\eta)$ balls of radius $c/\sqrt n$. In particular,

\[
 Q_n(c/\sqrt n)\ge\frac{1-\eta}{N(c,\eta)}>0. \tag{11}
\]

**Proof.** Cover compact $K_\eta$ by finitely many radius-$c$ balls, with
centers $z_1,\ldots,z_N$. The translated and scaled centers
$F_n^0+z_j/\sqrt n$ cover the event $\{Z_n\in K_\eta\}$ at radius $c/\sqrt n$.
The union has probability at least $1-\eta$; therefore some ball has mass
at least $(1-\eta)/N$. $\square$

The conclusion is about entropy, not implementation. Its centers could be
complicated functions, and an encoder choosing a center could require
future trajectory information. Consequently Lemma 3 is **not** an
initialization-only autonomous compression scheme. It does prove that the
growing small-ball exponent (10) is incompatible with uniform tightness at
the same tolerance. It likewise bounds the minimum covering size of a
high-probability subset by an $n$-independent number, for fixed $d,c,\eta$.

Uniform tightness of the actual nonlinear network's complete normalized
trajectory is an unproved condition here. In particular, a finite-time
central limit theorem would not establish tightness over all physical times
and the endpoint. If tightness fails, that failure must be established in
the norm and scale of the requested theorem before it can supply the
missing entropy. If only a snapshot is used for a lower bound, tightness of
that snapshot suffices to obstruct this route there.

The dependence on failure probability matters. Lemma 3 fixes $\eta$.
An increasing-confidence requirement $\delta_n\to0$ can demand larger
compact sets and need not have an $n$-independent covering size. A lower
bound exploiting that demand is a different, explicitly quantified claim.

A direct coefficient calculation shows the same scale issue. Suppose,
only as a fluctuation model, degree-$k$ random coefficients have standard
deviation $n^{-1/2}e^{-\alpha_d k}$. At tolerance $\varepsilon_n$, the
individual coefficients above that tolerance satisfy

\[
 k\lesssim\alpha_d^{-1}
       \log\frac{n^{-1/2}}{\varepsilon_n}.
\]

For $\varepsilon_n=c n^{-1/2}$ this does not grow with $n$. For
$\varepsilon_n=n^{-1/2}(\log n)^{-\beta}$ it grows only like
$\log\log n$. A degree proportional to $\log n$ would require accuracy a
polynomial factor finer than root width. Counting individually visible
coefficients is not a full entropy proof, since many small coefficients can
accumulate; Lemma 3 is the precise statement that avoids that loophole.

If the permitted error is $n^{-1/2}$ times a positive power of $\log n$,
normalized accuracy becomes coarser, strengthening the obstruction under
the same tightness hypothesis. If “actual self-variability” is instead
interpreted as a realized random pairwise discrepancy, its occasional small
values must be handled in the probability specification; it cannot simply
be substituted for a deterministic tolerance in these bounds.

## 6. An exact identity from the actual deep network

This calculation keeps the dense model and all hidden layers. Define the
initial feature kernel

\[
 K_n(x,x')=\frac{h^{(L)}(0,x)^Th^{(L)}(0,x')}n.
\]

Let $r_a=f_n(t,x_a)-y_a$, and let $\delta_a^{(\ell)}$ have the maintained
backpropagation meaning, so
$\delta_a^{(L)}=W^{(L+1)}\odot(\phi^{(L)})'(z_a^{(L)})$ and lower layers are
obtained with the actual transposed hidden matrices. Gradient flow is

\[
 \dot W^{(L+1)}=-\frac2m\sum_a r_a h_a^{(L)},\qquad
 \dot W^{(1)}=-\frac2{m\sqrt d}\sum_a r_a\delta_a^{(1)}x_a^T,
\]

\[
 \dot W^{(\ell)}=-\frac2{mn}\sum_a
       r_a\delta_a^{(\ell)}(h_a^{(\ell-1)})^T,
       \qquad 2\le\ell\le L.
\]

At zero readout, every $\delta_a^{(\ell)}$ vanishes. Thus all hidden
velocities vanish at time zero, while
$\dot W^{(L+1)}(0)=(2/m)\sum_a y_a h_a^{(L)}(0)$. Differentiating the actual
prediction gives the exact identity

\[
 \partial_t f_n(0,x)=\frac2m\sum_a y_a K_n(x,x_a). \tag{12}
\]

In addition, $\partial_t h^{(\ell)}(0,x)=0$ at all layers. One further
differentiation yields

\[
 \partial_t^2 f_n(0,x)
 =-\frac4{m^2}\sum_{a,b}K_n(x,x_a)K_n(x_a,x_b)y_b. \tag{13}
\]

Indeed, at time zero the derivative of the readout equation is
$\ddot W^{(L+1)}=-(2/m)\sum_a\partial_tf_n(0,x_a)h_a^{(L)}$, since the terms
containing $\partial_t h_a^{(L)}$ vanish. In the second derivative of the
prediction the other two terms contain either the zero readout or a zero
hidden velocity. Substitution of (12) proves (13).

These identities do not freeze feature learning at positive times: the
hidden accelerations can be nonzero, and later terms contain their effects.
They show that a proposed early-time lower bound first encounters a
structured deep random-feature kernel, not an arbitrary analytic function.

### A nonlinear activation with an explicitly structured initial limit

For the allowed illustrative activation $\phi^{(\ell)}(z)=\sin z$, set
$k_0(c)=c$ and $q_0=1$, where $c=x^Tx'/d$. Define recursively

\[
 k_\ell(c)=e^{-q_{\ell-1}}\sinh(k_{\ell-1}(c)),\qquad
 q_\ell=k_\ell(1)=\frac{1-e^{-2q_{\ell-1}}}{2}. \tag{14}
\]

For each fixed finite set of inputs, $K_n(x,x')\to k_L(x^Tx'/d)$ in
probability. Here is a direct proof at the level used in this statement.
If $(U,V)$ is centered Gaussian with common variance $q$ and covariance $s$,
the identity $\sin U\sin V=[\cos(U-V)-\cos(U+V)]/2$ and the Gaussian
characteristic function give
$\mathbb E[\sin U\sin V]=e^{-q}\sinh s$.
At layer one the rows are independent, so the empirical product average
has variance at most $1/n$ and converges to (14). At a higher layer,
conditional on previous features, different rows again give independent
centered Gaussian vectors whose covariance is exactly the preceding
empirical Gram. Their sine-product averages have conditional variance at
most $1/n$. The conditional expectation is a continuous function of the
preceding variances and covariance (with unequal variances the prefactor is
$e^{-(q+q')/2}$). Induction, the preceding convergence, and the conditional
variance bound prove the asserted finite-set convergence. No uniform
sphere or all-time limit is asserted by this argument.

Consequently the limiting initial velocity at finitely many test inputs is

\[
 \frac2m\sum_a y_a k_L(x^Tx_a/d). \tag{15}
\]

It is evaluated by a fixed depth-$L$ scalar recursion and the retained
training vectors and labels. Its analytic coefficients are linked by (14);
they are not independent degrees of freedom. The example therefore
demonstrates why a large polynomial or harmonic expansion does not itself
give a nonlinear-description lower bound. It is not a surrogate for the
positive-time learned network and makes no claim about compressing that
trajectory.

This example also accommodates correlated spanning data and a positive
limiting initial feature Gram. At the first layer, if inputs are distinct
up to sign, a nonzero combination $\sum_a v_a\sin(g^Tx_a/\sqrt d)$ cannot
vanish identically: choose a direction whose projections of all $\pm x_a$
are distinct; restriction to that direction gives distinct exponentials,
which are linearly independent by the Vandermonde determinant of their
derivatives at zero. If its Gaussian squared expectation were zero,
continuity and the strictly positive Gaussian density would force that
combination to vanish everywhere, a contradiction. Thus the Gram is
positive definite. At subsequent layers a positive definite preceding
Gram gives a nondegenerate Gaussian vector with positive density on
$\mathbb R^m$; a nonzero function $\sum_a v_a\sin z_a$ cannot vanish
identically, by differentiation in a coordinate with $v_a\ne0$.
Induction proves positivity. Distinct non-antipodal spanning correlated
inputs exist with $m=d$. Entrywise convergence in a fixed $m$ then gives a
positive finite-width Gram gap with probability tending to one: the
operator norm of the difference is at most $m$ times its largest absolute
entry, and the smallest eigenvalue can decrease by at most that operator
norm. This argument supplies no universal lower gap constant across data
sets.

### Derivative separation is not prediction separation at the same scale

Even a lower bound for (12) needs a transfer argument. Suppose two actual
trajectories have zero initial prediction, initial velocity difference of
norm $a$, and each has second derivative norm at most $B$ on $[0,T]$.
Taylor's integral formula and the triangle inequality give

\[
 \|f(t)-g(t)\|_\infty\ge ta-Bt^2.
\]

If $a/(2B)\le T$, taking $t=a/(2B)$ gives separation at least $a^2/(4B)$.
Thus this crude transfer takes velocity separation $a$ to prediction
separation of order $a^2$, not $a$. Root-width velocity fluctuations only
produce order-$1/n$ separation by this argument, below the requested
root-width tolerance. A sharper transfer would need a bound on the
**difference** of remainders at the same fluctuation scale, or another
uniform-in-width control. Neither is assumed or proved here. In particular,
uniform approximation of function values does not imply uniform
approximation of their time derivatives.

## 7. What is proved, and the bottleneck that remains

The exact statements established by the displayed arguments are:

- A finite-precision lower bound, and a bounded Lipschitz nonlinear-decoder
  lower bound, in terms of the actual observable's packing or small-ball
  probabilities. They count fixed information as well as dynamic state.
- A conditional $\Omega_d((\log n)^{d-1})$ word/parameter lower bound if the
  actual neural family has the projected balls (7), or if its distribution
  satisfies (10), with the stated precision/stability restrictions.
- A rigorous obstruction to obtaining (10) from tight root-width
  fluctuations at a fixed multiple of their scale.
- Exact initial-velocity and initial-acceleration formulas for the actual
  zero-readout deep gradient flow, plus a structured nonlinear-activation
  example showing why nonzero analytic modes need not be independent
  information.

The positive initialized feature Gram controls the finite training
observations. The spanning assumption prevents a trivial restriction to a
proper linear input subspace. Neither property proves independently
variable off-training harmonic coefficients. Analyticity likewise gives
upper approximation estimates, not coefficient richness. Full support of
the Gaussian parameter law only makes rare deterministic weight patterns
possible; it does not assign them enough probability for a fixed-$\delta$
lower bound. The actual pushforward law under learned dynamics is the
missing object.

The next mathematical discriminator for this route is precise: determine
whether normalized actual prediction fluctuations are tight in the
whole-sphere, all-time norm at the claimed self-variability scale, or prove
a failure of tightness with a quantitative small-ball estimate strong
enough for (3). If tightness holds, a logarithmic-exponent impossibility
result must instead use an explicit computational/representation obstruction
for the deterministic learned limit, a stricter accuracy requirement, an
increasing-confidence requirement, or a different source of complexity.
None may be silently substituted for the present contract.

No universal impossibility theorem for the requested dense feature-learning
family, and no autonomous sublinear-exponent construction, follows from
this route. The strongest conclusion is the exact conditional reduction
and the identified root-scale obstruction.
