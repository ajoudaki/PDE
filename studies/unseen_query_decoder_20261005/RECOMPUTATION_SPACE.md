# Recomputing the dense flow with counted workspace

2026-10-06. Scoped theoretical continuation. Internal result; no promotion,
experiment, maintained-source edit, or Git operation.

There is a substantive space reduction short of a compressed late-query
model: on the inherited dense good event, the entire trained dense trajectory
can be evaluated to arbitrary inverse-polynomial accuracy with an absolute
polylogarithmic amount of **working** memory, provided its initial Gaussian
coordinates remain available through a repeatable coordinate interface.
The calculation retains feature learning and is uniform over physical time
and the sphere. It recomputes training when a query is evaluated; it is not an
autonomous continuing replacement network.

That initial-coordinate interface is a substantial input, containing
quadratically many independent random coordinates. It is not permitted as
uncounted storage in the requested compression theorem. The second result
below proves why a generic short-seed space generator does not eliminate it:
an unrestricted-time test with random access can recognize the generator's
entire support using little space. A third result shows that root-space
Lipschitz concentration alone cannot justify a generic small-space scalar
Gaussian quadrature. Neither obstruction is a lower bound for the actual
network prediction class.

## 1. Contract and inherited mathematical input

Let the fixed training data be $(v_a,y_a)$, with $v_a\in S^{d-1}$,
$1\leq a\leq m$, $m\geq d$, and $\operatorname{span}\{v_a\}=\mathbb R^d$.
Let $L\geq2$ be fixed. The network is

\[
 z^{(1)}(v)=Av,\quad
 z^{(\ell)}(v)=W^{(\ell)}h^{(\ell-1)}(v),\quad
 h^{(\ell)}(v)=\phi_\ell(z^{(\ell)}(v)),\quad
 f_n(t,v)=w^Th^{(L)}(v)/n.
\tag{1}
\]

The first weights are iid $N(0,1)$, the hidden weights iid $N(0,1/n)$,
and $w(0)=0$. The loss is $m^{-1}\sum_a r_a^2$, where
$r_a=f_n(t,v_a)-y_a$, with mobilities $(n,1,\ldots,1,n)$.
Consequently

\[
 \dot A=-\frac2m\sum_a r_a\delta_a^{(1)}v_a^T,\qquad
 \dot W^{(\ell)}=-\frac2{mn}\sum_a
          r_a\delta_a^{(\ell)}h_a^{(\ell-1)T},\qquad
 \dot w=-\frac2m\sum_a r_ah_a^{(L)}.
\tag{2}
\]

Here $\delta_a^{(L)}=\phi_L'(z_a^{(L)})\odot w$, and
$\delta_a^{(\ell)}=\phi_\ell'(z_a^{(\ell)})\odot
(W^{(\ell+1)})^T\delta_a^{(\ell+1)}$. Define the corresponding
backward carriers by $k_a^{(L)}=w$ and
$k_a^{(\ell)}=(W^{(\ell+1)})^T\delta_a^{(\ell+1)}$.

The authorized dense-comparison source supplies a good event on which,
uniformly for all time, the hidden operator norms, $\|A\|_F/\sqrt n$,
$\|w\|_2/\sqrt n$, and all sphere feature RMS norms have fixed bounds.
It also supplies

\[
 \max_{a,\ell,i,t}|k_{a,i}^{(\ell)}(t)|
       \leq C\sqrt{\log(en)},\qquad
 |\partial_t f_n(t,v)|\leq C e^{-\kappa t}
       \quad(v\in S^{d-1}),
\tag{3}
\]

where all constants may depend on the original fixed problem, including
its label allowance and Gram gap, but not on $n$. These are inherited
internally checked inputs. No smaller label allowance or additional
history-covariance gap is imposed here. Real bounded first and second
activation derivatives suffice for the reduction below; they follow from
the stated strip assumptions.

The independent-dense comparison has scale
$b_n=n^{-1/2}\exp(C\sqrt{\log(en)})\log(en)^{O(1)}$ in
$\sup_{t\in[0,\infty],\ v\in S^{d-1}}$. The present evaluator can make
its own numerical error $n^{-a}$ for any fixed $a>0$, so its numerical
error would be negligible at that scale. Its missing compact initialization
is not a numerical-error issue.

All live bits, loop indices, arithmetic precision, and recursive frames
are counted. The computational statement assumes that each fixed activation
and its first derivative can be evaluated on real arguments of magnitude
$n^{O(1)}$ to $b$ fractional bits using $O((b+\log n)^c)$ bits, for some
fixed activation-dependent $c$. Fixed data are supplied as rational
coefficients, with their bit lengths included in the problem-dependent
constant. A precision interface for nonrational data is also allowed
if it obeys this same polynomial space bound; that is an additional
computational input hypothesis. Bare
holomorphy does not imply this computability assumption: an activation
could contain an uncomputable real constant. There is no integration,
solution-map, or matrix-function oracle in the proposed evaluator.

The unseen query must likewise have repeatable coordinate precision access,
and the time input must provide precision access to $\min(t,T)$, with an
explicit symbol allowed for $t=\infty$. Their interface workspace counts.
Rational queries and capped times with counted input lengths give a finite-
input alternative. Query rounding is controlled by the projected predictor's
uniform Lipschitz bound on the radius-two input ball. Use one common
activation-evaluation exponent $c$ across the permitted layer family;
depth independence of the logarithmic exponent is relative to that bound.

Numerical upper bounds for the physical caps, carrier coefficient,
activation slope and second derivative, vector-field bound and Lipschitz
coefficient, and prediction/tail coefficients, together with a positive
lower bound for the decay rate, must be supplied to a uniform compiler.
Bounds derived by the displayed recurrences from supplied certificates
need not be separate inputs. For a fixed problem such rational bounds can be hardcoded, giving
an existential conditional evaluator. The inherited opaque constants alone
do not constitute an algorithm extracting these certificates. Their finite
descriptions and evaluation space count with the fixed problem data.

## 2. A globally controlled extension of the actual dense vector field

For a parameter difference $\theta-\widetilde\theta$, where
$\theta=(A,W^{(2)},\ldots,W^{(L)},w)$, use the norm

\[
 \|\theta-\widetilde\theta\|_{\mathrm{par}}
 =\frac{\|A-\widetilde A\|_F}{\sqrt n}
  +\sum_{\ell=2}^L\|W^{(\ell)}-\widetilde W^{(\ell)}\|_F
  +\frac{\|w-\widetilde w\|_2}{\sqrt n}.
\tag{4}
\]

The notation in (4) abbreviates an explicitly displayed block norm; it
does not change any finite RMS normalization.

Choose fixed caps strictly above the good-event bounds. Project $A$ onto
its Frobenius ball of radius $B_A\sqrt n$, and $w$ onto its Euclidean
ball of radius $B_w\sqrt n$. Project each hidden matrix onto the convex
operator-norm ball $\{W:\|W\|_{\rm op}\leq B_W\}$ using its Frobenius
metric. Write $\bar\theta$ for these projected parameters.

For completeness, if $W=U\operatorname{diag}(\sigma_i)V^T$, its last
projection is $P(W)=U\operatorname{diag}(\min(\sigma_i,B_W))V^T$.
For any $Q$ in the operator-norm ball,

\[
 \langle W-P(W),Q-P(W)\rangle_F
 =\sum_{\sigma_i>B_W}(\sigma_i-B_W)(u_i^TQv_i-B_W)\leq0.
\tag{5}
\]

Expanding squared distances shows that (5) characterizes the nearest
point. Applying (5) to two inputs and adding gives
$\|P(W)-P(V)\|_F^2\leq
\langle P(W)-P(V),W-V\rangle_F$, hence this projection is
Frobenius-nonexpansive. The two vector-ball projections have the same
property. Thus $\theta\mapsto\bar\theta$ is nonexpansive in (4).

Compute the training forward pass using $\bar\theta$. In its backward
pass replace each carrier by its coordinate clipping to $[-M_n,M_n]$,
where $M_n=C_0\sqrt{\log(en)}$ is above (3):

\[
 \widehat\delta_a^{(L)}
   =\phi_L'(\bar z_a^{(L)})\odot
                  \operatorname{clip}_{M_n}(\bar w),
\]
\[
 \widehat\delta_a^{(\ell)}
   =\phi_\ell'(\bar z_a^{(\ell)})\odot
       \operatorname{clip}_{M_n}
          ((\bar W^{(\ell+1)})^T\widehat\delta_a^{(\ell+1)}).
\tag{6}
\]

Also clip each computed training residual to a fixed interval containing
the actual good residuals, for example a slightly enlarged interval
$[-\sqrt mY,\sqrt mY]$, where
$Y=(m^{-1}\sum_a y_a^2)^{1/2}>0$. The zero-label case is identically
zero and needs no solver. Substitute these features, clipped residuals,
and backward fields into the right sides of (2). Call the resulting
autonomous vector field $F_n(\theta)$.

This extension has three useful properties:

\[
 \sup_\theta\|F_n(\theta)\|_{\mathrm{par}}\leq B,
 \qquad
 \|F_n(\theta)-F_n(\widetilde\theta)\|_{\mathrm{par}}
       \leq K_n\|\theta-\widetilde\theta\|_{\mathrm{par}},
 \qquad K_n\leq C(1+M_n).
\tag{7}
\]

Moreover, it agrees with the original vector field along every good
original trajectory.

Here is the estimate, including its width dependence. Projection gives
fixed matrix operator bounds and fixed first-layer/readout RMS bounds.
The real slope bound and linear growth of each $\phi_\ell$ then give
fixed forward feature RMS bounds at every training input and every point
of the unit sphere. Coordinate clipping contracts Euclidean norm, so
downward induction in (6) gives fixed backward RMS bounds, independent
of $M_n$. A rank-one matrix satisfies
$\|uv^T/n\|_F=(\|u\|_2/\sqrt n)(\|v\|_2/\sqrt n)$; this and the
residual caps prove the first assertion in (7).

Forward subtraction gives feature and preactivation RMS differences at
most $C\|\theta-\widetilde\theta\|_{\mathrm{par}}$. In a backward
gate difference, the factor multiplying the gate is bounded coordinatewise
by $M_n$. Therefore its RMS is at most
$C M_n\|\theta-\widetilde\theta\|_{\mathrm{par}}$. The difference
of the carrier inputs is bounded by

\[
 B_W\frac{\|\widehat\delta-\widehat{\widetilde\delta}\|_2}{\sqrt n}
 +\|\bar W-\bar{\widetilde W}\|_F
                   \frac{\|\widehat{\widetilde\delta}\|_2}{\sqrt n}.
\]

Clipping does not increase it. Downward induction thus gives a backward
RMS difference $C(1+M_n)\|\theta-\widetilde\theta\|_{\mathrm{par}}$;
there is one additive gate term at each layer, not a new factor $M_n$
per layer. Prediction and clipped-residual differences cost the same norm
with a fixed constant. Subtracting the rank-one terms proves the second
assertion in (7).

The good trajectory activates none of these projections or clippings,
so uniqueness for the globally Lipschitz field identifies it with the
original trajectory. The extension is a device for evaluating the
original model on its good event; it does not assert a source theorem
for newly sampled clipped training dynamics.

The projected prediction map $\bar f_n(\theta,v)$, obtained from (1)
using $\bar\theta$, satisfies

\[
 \sup_{v\in S^{d-1}}
 |\bar f_n(\theta,v)-\bar f_n(\widetilde\theta,v)|
       \leq C\|\theta-\widetilde\theta\|_{\mathrm{par}}.
\tag{8}
\]

The proof is the same forward subtraction, paired with the bounded
readout RMS. No net, query carrier bound, or query-dependent event is
required in (8).

## 3. Recursive integration has only polylogarithmic depth

Put $\ell_n=\log(en)$, and choose $T=C_a\ell_n$ so that
$(C/\kappa)e^{-\kappa T}\leq n^{-a}/4$. For $0\leq t\leq T$, define Picard
iterates as vector-valued mathematical objects,

\[
 \theta_0(t)=\theta(0),\qquad
 \theta_{j+1}(t)=\theta(0)+\int_0^t F_n(\theta_j(s))\,ds.
\tag{9}
\]

They will be evaluated one coordinate at a time, not stored as vectors.
If $\theta(t)$ solves the extended ODE, boundedness and Lipschitzness give
by induction

\[
 \|\theta(t)-\theta_j(t)\|_{\mathrm{par}}
       \leq\frac{B K_n^j t^{j+1}}{(j+1)!}.
\tag{10}
\]

For $j=0$, integrate the bound $B$. Integrating $K_n$ times the previous
bound proves the next case. The factorial estimate
$j!\geq(j/e)^j$ shows that

\[
 J=C_a\bigl(K_nT+\ell_n\bigr)
       =O(\ell_n^{3/2})
\tag{11}
\]

with a sufficiently large fixed coefficient makes (10) at most a chosen
constant times $n^{-a}$. This is a global Picard argument; it does not
require a contraction over the whole interval. For a conservative integral
space count below one may round its bound up to $J=O(\ell_n^2)$.

Every $\theta_j$ is $B$-Lipschitz in time, because its derivative is
$F_n(\theta_{j-1})$. Thus the integrand in (9) is $K_nB$-Lipschitz
in the norm (4). A composite midpoint rule with $Q$ subintervals has
error at most $K_nBT^2/(2Q)$. Stream this rule using one loop index and
one accumulator for the requested coordinate, adding each term with its
weight $t/Q$. To evaluate its integrand,
evaluate the required coordinates of $\theta_j$ recursively. No full
iterate is retained.

If each iteration's quadrature, field evaluation, coordinate rounding,
and time rounding together contribute at most $\eta$ in (4), the worst
uniform accumulated error $e_j$ obeys

\[
 e_{j+1}\leq TK_n e_j+\eta,\qquad
 e_J\leq J(1+TK_n)^J\eta.
\tag{12}
\]

It is enough to take
$\eta=c n^{-a}/[J(1+TK_n)^J]$. Then

\[
 \log(\eta^{-1})=O(\ell_n^2\log\ell_n+\ell_n)
                  =O(\ell_n^3),\qquad
 \log Q=O(\ell_n^3).
\tag{13}
\]

The number of quadrature nodes can be immense while its counter and
the recursive integration depth remain polylogarithmic. Direct
coordinate errors of size $2^{-p}$ contribute at most $C_Ln2^{-p}$
to (4); hence a single grid precision $p=C_a\ell_n^3$ covers (12).
Integrands and accumulators have at most polynomial-in-$n$ magnitude,
so this also bounds their integer parts after harmless enlargement.
Quadrature times can be rounded to a common dyadic grid at the same
precision; their $B$-Lipschitz error is included in $\eta$.
Allocate rounding error to each of the $Q$ streamed contributions at
order $\eta/Q$, including the coordinate-to-parameter norm factor.
The extra $\log Q+O(\log n)$ precision bits remain within (13).

## 4. Spectral projection can itself be streamed in small space

The spectral projection in Section 2 must not be hidden in a primitive.
The following explicit construction supplies it. Its computational cost
is deliberately unconstrained.

Suppose an $N\times N$ matrix $W$, $N\leq n^{C}$, is available by a
repeatable coordinate procedure, its entries lie on a common finite grid,
and a known bound $R\geq\|W\|_{\rm op}+B_W$ is at most
$\exp(\ell_n^{O(1)})$. Form its symmetric dilation

\[
 H=\begin{pmatrix}0&W\\W^T&0\end{pmatrix}.
\]

Let $\psi(s)=\operatorname{clip}_{B_W}(s)$. Functional calculus for the
symmetric matrix $H$ shows that the upper-right block of $\psi(H)$ is
exactly the Frobenius projection of $W$ onto its operator-norm ball.
This follows by applying $\psi$ to the eigenvectors associated with
the singular-vector pairs of $W$.

The even $2\pi$-periodic function $g(\alpha)=\psi(R\cos\alpha)$
is bounded by $B_W$ and is $R$-Lipschitz. Let $q_D(\cos\alpha)$ be
its degree-$D$ Fejér trigonometric mean. It is an ordinary polynomial
in $\cos\alpha$, expressible as

\[
 q_D(x)=c_0+\sum_{j=1}^D c_jT_j(x),\qquad |c_j|\leq2B_W,
\tag{14}
\]

where $T_j(\cos\alpha)=\cos(j\alpha)$. There is the elementary error
bound

\[
 \sup_{|x|\leq1}|q_D(x)-\psi(Rx)|
       \leq C(R+B_W)D^{-1/2}.
\tag{15}
\]

Indeed the normalized Fejér kernel is nonnegative, has integral one,
and away from zero is at most $C/[D\alpha^2]$ for
$|\alpha|\leq\pi$. On $|\alpha|\leq D^{-1/2}$ use the Lipschitz
bound $R D^{-1/2}$; on its complement use $2B_W$ times the kernel's
tail mass, at most $C D^{-1/2}$. These facts follow directly from
$D^{-1}|\sum_{j=0}^{D-1}e^{ij\alpha}|^2$ and its Fourier expansion.
Changing $D$ by one changes only the universal constants.

To obtain operator error $\xi$, choose $D\geq C(R+B_W)^2/\xi^2$.
The spectral theorem transfers (15) to $H/R$. Its coefficients are
one-dimensional integrals of $g(\alpha)\cos(j\alpha)$, times Fejér
weights. The integrands have Lipschitz constants at most $R+B_Wj$.
A streamed uniform quadrature with
$Q_c\geq C(R+B_WD)D/\xi$ nodes gives coefficient errors whose sum
is at most $\xi$. Its counters have $O(\log R+\log D+\log\xi^{-1})$
bits. Real cosine and the scalar clipping operation have elementary
finite-precision algorithms, for example argument reduction followed
by convergent Taylor series.

For a requested matrix entry, compute $T_j(H/R)$ by

\[
 T_0(X)=I,\quad T_1(X)=X,\quad
 T_{2r}(X)=2T_r(X)^2-I,\quad
 T_{2r+1}(X)=2T_r(X)T_{r+1}(X)-X.
\tag{16}
\]

At each multiplication stream the single intermediate matrix index.
The recursion has depth $O(\log D)$. Each exact $T_j(H/R)$ has
operator norm at most one. If all elementary arithmetic has error at
most $2^{-b}$, a conservative entrywise recursion gives total error
at most $(CN)^{C\log D}2^{-b}$; this follows by bounding each
matrix-product entry by its $N$ summands and inducting on the depth.
The final sum of $D+1$ bounded-coefficient terms adds only
$O(\log D)$ precision bits. Thus

\[
 b=O\bigl(\log\xi^{-1}+(\log N)(\log D)+\log D\bigr)
\tag{17}
\]

is sufficient. One does not expand the clipping approximation into
monomials with enormous binomial coefficients. Its Chebyshev
intermediates and Fourier coefficients have controlled magnitudes.

To request Frobenius projection error $\varepsilon$, set
$\xi=\varepsilon/\sqrt N$ and include the coefficient and arithmetic
errors in a fixed fraction of this budget. Then (15)--(17) give the
claimed coordinate evaluator, with stack space
$O((\log D)(b+\log N))$ beyond its matrix-entry subroutine.

More explicitly, for target Frobenius error $\varepsilon$, allocate
$\varepsilon/(4\sqrt N)$ each to the uniform polynomial error and the
sum of coefficient errors. Allocate $\varepsilon/(2N)$ to the numerical
error of every requested matrix entry. The first two are operator errors;
the last is entrywise. This distinction costs only $O(\log N)$ extra
bits in (17). It prevents an entrywise error from being incorrectly
converted using an operator-to-Frobenius factor.

There is an important precision issue when that subroutine is a
recursive Picard evaluator. Every virtual state coordinate is first
defined on the same fixed $p$-bit grid. All repeated requests for it
return the same rational. Matrix arithmetic then evaluates the
projection of this fixed approximate matrix, to higher internal
precision if needed. Nonexpansiveness bounds the effect of the
state-coordinate rounding by its Frobenius error. In particular,
the increased internal precision in (17) is **not** recursively
requested from a preceding Picard iterate. That would cause an
unjustified precision cascade. Returning a fixed $p$-bit rational and
padding it with zeros supplies its exact higher-precision value.

The simpler first-layer and readout projections use streamed sums of
squares and scalar square roots; they obey the same fixed-input-grid
rule. A forward or backward pass with fixed $L,m,d$ can evaluate any
requested scalar recursively, streaming every width index. Its depth
is a fixed multiple of the projection depth plus the Picard depth.
Along a complete recursive branch, the per-Picard network/projection stack
is multiplied by the Picard depth; Section 5 counts this product.
All ordinary scalar magnitudes are polynomial in $n$ on the projected
parameter domain, and the per-layer arithmetic accumulation costs
only $O_{L,m,d}(\log n)$ additional precision bits.

## 5. What the space theorem actually says

Assume initialization coordinates are reproducibly available to a
requested polynomial-logarithmic precision, without storing their
whole array in working memory. Count their evaluator space separately
as $S_0(n)$. They can be truncated at a polynomial magnitude cap;
this agrees with Gaussian initialization except on an additional
event whose probability tends to zero, and does not affect the
inherited good-path argument. Alternatively take the coordinate
magnitude bound as a deterministic input hypothesis.

The bounded field ensures every Picard iterate lies within distance
$BT$ of its initial state in (4). With polynomially bounded input
coordinates this supplies a polynomial bound $R$ for Section 4,
uniformly through every recursive call. By (13), use $p=O(\ell_n^3)$
fractional bits for virtual state coordinates. Then
$\log D=O(\ell_n^3)$ and $b=O(\ell_n^4)$ in (17). A projection
evaluation needs $O(\ell_n^7)$ bits of stack and scratch; the
$O(\ell_n^2)$ Picard levels give the conservative bound

\[
 S_0(n)+O_{L,m,d,a,\mathrm{data},\phi}
    \left(\ell_n^{\max\{10,\,4c+2\}}\right).
\tag{18}
\]

The slack in this exponent covers scalar evaluators and loop arithmetic;
it is not an optimized estimate. Its exponent is independent of $L,m,d$
and depends at most on the chosen activation-evaluation complexity.
Large constants can depend on the fixed original problem. The exponent
does not count a real or integer with arbitrarily many bits as one word.

Initial-coordinate rounding must also be budgeted. By global Lipschitz
stability, an initial norm error $\varepsilon_0$ is magnified by at most
$e^{K_nT}$. All coordinate blocks together have polynomially many
entries. Consequently $O(\ell_n^{3/2}+a\ell_n)$ input precision bits
already make this contribution at most $n^{-a}$; the larger common
$p$ above is sufficient. This argument does not require the rounded
initial condition itself to satisfy the original good event.

Compute the approximate iterate at $\min(t,T)$, and evaluate the
projected prediction at the supplied $v$. Equations (8), (10), and
(12), with suitably divided error budgets, give

\[
 \sup_{t\in[0,\infty],\ v\in S^{d-1}}
       |f_n(t,v)-\widehat f_n(t,v)|\leq n^{-a}
\tag{19}
\]

on the inherited good event and the initialization truncation event.
For $t\geq T$, integrate (3) to bound the difference from $f_n(T,v)$;
the same argument includes $t=\infty$. The numerical estimates were
uniform for $0\leq t\leq T$, and (8) was uniform on the sphere.
Thus no growing query union, population limit, or history-Gram
conditioning enters (19).

This is a proved conditional **recomputation** theorem. It genuinely
removes the need to store the evolving $O(n^2)$ dense state. It retains
the initialization interface, uses the whole training dataset and
training equations at decoding time, and freezes evaluation after $T$.
It is not an autonomous nonlinear compressed dynamics, nor a proof of
the requested total-storage theorem. If replay of training is disallowed,
it fails that contract directly. If every retained initialization bit
counts, (18) offers no polylogarithmic total bound until $S_0$ and the
information behind the interface have been replaced by a valid compact
construction.

## 6. Why a one-pass generator guarantee does not remove initialization

The issue is random access, not merely a long random tape.

Let $G:\{0,1\}^s\to\{0,1\}^{N}$ be a generator whose coordinate
$G(z)_i$ can be computed using $w$ working bits from a seed $z$ and
index $i$. There is a deterministic random-access test using
$O(s+w+\log N)$ bits which accepts a tape $u$ exactly when
$u\in\operatorname{range}(G)$.

The test enumerates the $2^s$ seeds. For each seed it scans
$i=1,\ldots,N$ and compares $u_i$ with $G(z)_i$. It accepts upon one
complete match and rejects after all seeds fail. It stores one seed,
one coordinate index, a match flag, and the coordinate evaluator's
workspace. Therefore

\[
 \mathbb P\{\text{test accepts }G(Z)\}=1,\qquad
 \mathbb P\{\text{test accepts }U\}
       \leq2^{s-N},
\tag{20}
\]

for independent uniform seed $Z$ and uniform $N$-bit tape $U$.
No runtime limit is used. The random-access ability lets the test read
the same tape again for every candidate seed. A read-once test cannot
perform these scans after its random tape has been discarded.

Consequently a theorem about fooling one-pass space-bounded random
computations cannot be invoked for the recursive dense evaluator merely
because its working memory is small. That evaluator repeatedly reads
the same initialized matrix entries. A generator tailored to this
specific network computation might still work, but it needs a separate
approximation theorem for this observable class. Equation (20) rules
out a generator claimed to fool all tests within the displayed support
test's workspace, including a blanket assertion covering every
polylog-space random-access test. It does not rule out all task-specific
generators.

The parameter qualification matters. The support test uses space at
least comparable to the seed length $s$. If a proposed generator for
space $S$ has seed length $s>S$, for example $s=S\log N$, this particular
test may not belong to its promised space-$S$ class. No lower bound
excluding every parameterized random-access generator follows from
(20). The route still needs an applicable generator theorem with its
actual access pattern, seed length, evaluator space, error, and runtime
quantifiers; a one-pass guarantee by itself does not supply those facts.

There is an even simpler distinction at the level of initialization
laws. The number of independent Gaussian root coordinates is

\[
 D_n=nd+(L-1)n^2.
\]

Their signs are $D_n$ independent fair bits. A deterministic $s$-bit
seed produces at most $2^s$ sign strings, so its total-variation
distance from the iid Gaussian sign law is at least
$1-2^{s-D_n}$. Thus a short finite seed cannot recreate the original
iid Gaussian initialization law. Matching the trained prediction to
near-root accuracy is weaker than matching that law; this sign argument
does not prove a prediction lower bound.

Fresh random signs on every recursive read also fail: a repeated
coordinate must retain its original value, and every matrix transpose
must refer to the same matrix. Resampling silently replaces the
specified trained network by a different process.

## 7. A scalar expectation does not automatically have a small-space integrator

There is a precise black-box obstruction to deriving the desired
evaluator solely from the inherited Gaussian Lipschitz bound.

Suppose a deterministic finite-bit quadrature procedure queries at most
$M$ points $x_1,\ldots,x_M$ in $\mathbb R^D$ and is told zero at every
query. Its next query can depend on all answers so far; the all-zero
transcript still defines a fixed query set $\mathcal X$. Both

\[
 h_0(x)=0,\qquad
 h_1(x)=\min\{1,\operatorname{dist}(x,\mathcal X)/\sqrt n\}
\tag{21}
\]

are bounded by one and $n^{-1/2}$-Lipschitz, and both agree with the
entire transcript. For $Z\sim N(0,I_D)$,

\[
 \mathbb E h_1(Z)
 \geq1-\sum_{j=1}^M\mathbb P\{\|Z-x_j\|_2<\sqrt n\}
 \geq1-M(en/D)^{D/2}\qquad(D>n).
\tag{22}
\]

For the last inequality, for any center $x$ and $u>0$,

\[
 \mathbb P\{\|Z-x\|_2^2<n\}
 \leq e^{un}\mathbb E e^{-u\|Z-x\|_2^2}
 \leq e^{un}(1+2u)^{-D/2}.
\]

Complete the square in the Gaussian integral to obtain the second
inequality; its omitted center-dependent factor is at most one.
Choosing $u=(D/n-1)/2$ gives a bound no larger than $(en/D)^{D/2}$.

For $D\asymp n^2$ and $\log M=\log(n)^{O(1)}$, (22) tends to one.
Thus these two integrands have almost unit-separated Gaussian
expectations despite identical query answers and the same root-scale
Lipschitz bound. No such quadrature can uniformly approximate both to
error less than, say, $1/3$.

Why this is relevant to counted space requires a model qualification.
For a uniform deterministic finite-state arithmetic or Turing
computation using $S$ total working bits, fixed polynomial-length
read-only data, and no free external clock, a halting all-zero oracle
run has at most $2^{O(S+\log n)}$ configurations before one repeats.
Otherwise determinism would repeat the same future forever. Hence it
makes at most that many point queries. With $S=\log(n)^{O(1)}$,
the preceding lower bound applies. A point-query interface must not
hide a writable high-dimensional point array or let a streaming output
tape be reread without counting it. An arbitrary-real machine with
unbounded information in one scalar is outside this statement.

The obstruction concerns deterministic black-box integration. It is
not a claim that Gaussian integration always requires $D$ stored
coordinates, nor that every specially structured integrand is hard.
The function (21) has not been represented by the specified deep
training dynamics. Its role is exact: Gaussian concentration and a
small Lipschitz constant alone cannot be the missing constructive
integration theorem. A successful center evaluator must exploit more
of the actual network structure.

## 8. Research status and remaining obligation

| Claim | Status and scope |
|---|---|
| Globally bounded $O(\sqrt{\log n})$-Lipschitz extension agreeing on original good paths | Proved here from the inherited physical/carrier event |
| Uniform inverse-polynomial dense prediction evaluation in polylog working memory, given repeatable initialization coordinates | Proved here under the explicit activation/data computability model |
| Spectral projection evaluator without a matrix-function oracle | Constructed and precision-counted here |
| A fixed short-seed generator fools every unrestricted-time random-access test with workspace $O(s+w+\log N)$ | Refuted by support recognition (20); not a lower bound against every parameterized generator |
| Root-scale Lipschitz concentration alone supplies a generic small-space deterministic Gaussian integrator | Refuted in the stated black-box finite-bit model by (21)--(22) |
| Initialization-dependent polylog total-state, late-query decoder for the actual model | Open |
| Autonomous continuing replacement with no replay of training | Not supplied by this recomputation construction |

The space reduction supersedes only a potential *implementation*
obstruction to recomputing the dense path: polynomially many small time
steps and their long naive recursion are not inevitable. It does not
supersede the missing Gaussian-program population bridge in
`POPULATION_DECODER.md`, and it does not need that bridge.

The specific new missing obligation is to replace repeatable dense
initialization access by an admissible compact object while controlling
the actual prediction. Possible statements would be a generator theorem
for this particular recursively evaluated trained-network class, or a
structure-specific small-space Gaussian expectation algorithm. Generic
space pseudorandomness and concentration do not supply either statement.

## 9. Provenance

Scientific inputs read completely: the current-study
`POPULATION_DECODER.md`, the explicitly authorized
`integrated_general_compression_20261004/GENERAL_DENSE_COMPARISON.md`,
and `docs/notation.qmd`. The dense-comparison source's links to other
studies were not followed. No other study, archived book material,
source history, or experiment was read or run. All computational
complexity assertions used above have self-contained proofs; no
unverified external derandomization theorem is invoked.

Process instructions read: `investigate-conjectures`, its
research-contract, evidence-ledger, and adversarial-audit references,
and `solve-math-rigorously`. The required canonical-notation skill at
`/home/amir/.codex/skills/explain-with-canonical-notation/SKILL.md`
again returned `Permission denied`; its neural-network reference was
unavailable. The supplied canonical-presentation instructions and
maintained notation contract were applied directly. The supervisor
requested the strong model in which peak decoder workspace counts;
training replay remains an explicitly flagged contract issue.

## 10. Follow-up: bounded independence and polynomial degree

The supervisor requested a separate, network-specific audit of whether
$k$-wise Gaussian initialization or a polynomial surrogate could remove
the initial-coordinate interface. This section gives the degree
calculation. It does not use the generic support-recognition obstruction
as its conclusion.

There are two different degree notions. A polynomial's **total degree**
counts every power. Its **coordinate support per monomial** counts the
number of distinct initialized Gaussian coordinates occurring in that
monomial. If random coordinates have the correct individual Gaussian
marginals and every set of at most $k$ coordinates is independent,
then they reproduce the Gaussian expectation of any integrable polynomial
whose monomials use at most $k$ distinct coordinates. This follows by
factoring the expectation of each monomial over its distinct coordinates
and summing. Total degree at most $k$ is sufficient, but can be wasteful.
Finite-seed implementations also require a finite-precision marginal
construction and moment-error control; exact continuous Gaussian
marginals are not generated from a finite uniform seed.

For scale comparison, polynomial hashing over a finite field with
distinct coordinate labels evaluates
$a_0+a_1u+\cdots+a_{k-1}u^{k-1}$, with independent uniform field
coefficients $a_j$. Any $k$ labeled values are independent uniform
because their Vandermonde matrix is invertible. The retained seed has
$k\log_2|\mathbb F|$ bits. Coordinatewise transforms to a finite
Gaussian grid preserve $k$-wise independence, with a separate marginal
error. If $b$ bits describe that marginal grid, the usual field size
choice gives a seed scale $O(k(\log D_n+b))$. Thus a polylogarithmic
$k$ with an absolute exponent would suffice for the storage count of
this construction; a depth-dependent or much larger $k$ does not
establish the user's requested count.

### 10.1 Initial features already retain a depth-dependent degree

Replace each activation by a polynomial of degree $q\geq2$, with
nonzero highest coefficient, for this algebraic audit. Treat all hidden
initialization entries as variables. The first preactivation has degree
one, so the top-feature total degree obeys

\[
 D_1=q,\qquad D_\ell=q(1+D_{\ell-1}),\qquad
 D_L=q+q^2+\cdots+q^L.
\tag{23}
\]

The leading homogeneous polynomial is nonzero for nonzero inputs and
nonzero leading activation coefficients: taking the highest activation
power in every layer produces it, and a single nonzero chain supplies
a nonzero coefficient. Width normalizations are fixed scalars and do
not affect degree.

Zero initial readout does not suppress this feature-degree dependence.
At time zero, all hidden parameter derivatives vanish, while
$\dot w=(2/m)\sum_a y_a h_a^{(L)}$. Therefore exactly

\[
 \partial_t f_n(0,v)
 =\frac2m\sum_a y_a
          \frac{h_a^{(L)}(0)^T h^{(L)}(0,v)}n.
\tag{24}
\]

For the polynomial activations its total degree is at most $2D_L$,
and is exactly $2D_L$ whenever the leading homogeneous kernel combination
does not cancel. For instance, a single nonzero positive label evaluated
at its training input has a leading sum of squares, which is nonzero.
This is an algebraic statement about the surrogate; it is not a claim
that polynomial activations of degree $q\geq2$ satisfy the original
globally bounded-slope hypothesis.

Counting distinct coordinates sharpens the first bounded-independence
requirement. A monomial of one top feature has at most

\[
 s_L=d q^{L-1}+\sum_{j=1}^{L-1}q^j
          =O_d(q^{L-1})
\tag{25}
\]

distinct root coordinates. Expand the $q$ powers at each layer as a
tree. There are at most $q^{L-1}$ first-layer row occurrences, each
using at most $d$ first-layer coordinates; the hidden-edge occurrences
are bounded by $q+\cdots+q^{L-1}$. Repeated indices only reduce the
number of distinct roots. Consequently $k=2s_L$ suffices to reproduce
the expectation of (24) for the exact-marginal idealization. Using
$k=2D_L$ is sufficient but unnecessarily pessimistic.

The growth in (25) can be present, not just an artifact of this upper
count. At sufficiently large width, choose disjoint children throughout
the expansion tree. Even using just one nonzero input coordinate per
first-layer row gives $q^{L-1}$ distinct first-layer roots and
$q+\cdots+q^{L-1}$ distinct hidden roots, with nonzero coefficient.
The square in a self-kernel contains the square of such a monomial,
which still has that many distinct coordinates and a nonzero Gaussian
moment. This shows that the full polynomial is not, as an algebraic
identity, a sum solely of monomials with a bounded number of root
coordinates independent of depth. It does not by itself prove that
every smaller-$k$ law gives a substantial prediction error: aggregate
coefficients, width suppression, and cancellations still matter.

### 10.2 Degree needed by the elementary strip approximation

The available real global extension permits individual preactivations
as large as $R_n=C\sqrt n$. It supplies an RMS bound, not a coordinate
bound independent of $n$. For a strip-holomorphic activation with
bounded strip slope, approximation on $[-R,R]$, $R\geq1$, by the
elementary Chebyshev truncation has the estimate

\[
 \sup_{|x|\leq R}|\phi(x)-p_q(x)|
       \leq C(1+R)^2 e^{-c q/R}.
\tag{26}
\]

To see the width of its complex domain, parametrize the Bernstein ellipse
by $z=(R/2)(w+w^{-1})$. Take
$\log|w|=\operatorname{arcsinh}(a/(2R))\asymp R^{-1}$, placing the
ellipse inside a fixed smaller activation strip. The strip slope gives
$|\phi(z)|\leq C(1+R)$ there. Cauchy's coefficient bound and summation
of the resulting geometric tail prove (26). A slightly smaller ellipse
also controls the derivative approximation; the necessary logarithmic
precision adjustment does not change the powers below.

Thus this particular uniform construction uses

\[
 q=O\left(R\,[\log(\varepsilon^{-1})+\log(1+R)]\right)
\tag{27}
\]

for error $\varepsilon$. On the whole extended domain and with
$\varepsilon=n^{-a}$, this is $q=O(\sqrt n\log n)$, already far
outside a polylog degree certificate.

One can give the route its more favorable hypothetical domain
$R=C\sqrt{\log(en)}$. With inverse-polynomial activation accuracy,
(27) then gives $q=O(\log(en)^{3/2})$. This simultaneous trained
coordinate bound is an additional assumption for the audit; it is
not supplied by the physical RMS estimates alone. Even on this
favorable domain, the certificate (25) becomes

\[
 k=O_{L,d}\bigl(\log(en)^{3(L-1)/2}\bigr)
\tag{28}
\]

for the first prediction derivative. This exponent is not absolute
over all fixed depths. Equations (26)--(28) describe a sufficient
layerwise polynomial construction, not an optimal approximation-degree
lower bound for every permitted activation or for the full prediction.
More special activations can have faster approximation; a new direct
approximation of the joint network observable could also be better.

### 10.3 Picard composition versus time Taylor jets

Treat the readout, as well as all hidden parameters, as polynomial
variables. For degree-$q$ activations, the predictor has degree

\[
 P=1+D_L.
\]

Differentiation with respect to a parameter lowers total degree by one.
Consequently the squared-loss gradient vector field has degree at most

\[
 r=2P-1.
\tag{29}
\]

Multiplicative width and learning-rate normalizations do not change
this count. The unprojected polynomial Picard iterates therefore satisfy

\[
 \deg_G\theta_{j+1}\leq
       \max\{1,r\deg_G\theta_j\},
 \qquad \deg_G\theta_j\leq r^j.
\tag{30}
\]

The actual zero-readout first iterate has degree at most $D_L$, with
unchanged hidden blocks. This improves its first factor but not the
multiplicative recurrence for subsequent iterates. Integrating a
polynomial coefficient in time does not lower its root degree.
The general bound is algebraically sharp for polynomial ODEs, as the
scalar example $\dot u=u^r$ shows. Sharpness for that scalar equation
is not offered as a realizable lower bound for the present network.

With $J=O(\log(en)^{3/2})$, even a fixed $q>1$ produces the
upper certificate $r^J=\exp(O_L(\log(en)^{3/2}))$. If $q$ grows as
in the favorable regime above, it becomes
$\exp(O_L(\log(en)^{3/2}\log\log(en)))$. A moment-matching argument
which asks for independence up to this degree does not give a
polylogarithmic seed.

High-order time jets have a better single-patch count. For the polynomial
vector field $F$, let $\mathcal D_F p=\sum_i F_i\partial_i p$ act on
a polynomial $p$ in the parameters. It satisfies

\[
 \deg(\mathcal D_F p)\leq\deg p+r-1.
\]

The order-$j$ derivative of a parameter coordinate along the flow is
$\mathcal D_F^j\theta_i$; induction gives degree at most
$1+j(r-1)$. The order-$j$ prediction derivative has degree at most
$P+j(r-1)$. Thus one order-$K$ Taylor step has parameter-map degree

\[
 B_K=1+K(r-1),
\tag{31}
\]

which is linear in $K$, rather than exponential. This is a real
improvement over the unreduced Picard polynomial.

However, evaluating $H$ restarted Taylor patches means composing their
parameter maps. The corresponding sufficient total-degree bound is

\[
 \deg_G\theta_{\rm final}\leq B_K^H,
 \qquad \deg_G f_{\rm final}\leq P B_K^H.
\tag{32}
\]

For the candidate analytic schedule $H=O(\log(en)^{3/2})$ and
$K=O(\log(en))$, even fixed $q>1$ gives the certificate
$\exp(O_L(\log(en)^{3/2}\log\log(en)))$. Replacing multiple patches
by one global Taylor polynomial would require convergence out to
$T=O(\log n)$, while the inherited local radius is of order
$1/\sqrt{\log n}$. The available radius does not justify that
replacement.

The coordinate-support count can always be bounded by the smaller of
the total degree and the number $D_n$ of initialized coordinates. This
does not give a polylog bound after the repeated compositions in (30)
or (32). Better bounds might exploit the normalized sums over neurons
and show that the large-support monomials have collectively negligible
expectation or variance. No such estimate follows from the degree
calculation. Dropping those terms would be a new approximation with a
new source-error obligation.

The actual globally controlled evaluator additionally uses coordinate
clipping and spectral projections. They are not polynomial maps.
Inserting Section 4's explicit high-accuracy polynomial projection
inside it would introduce its very large degree as an additional
composition factor. The calculation (29)--(32) grants the route the
simpler unprojected polynomial dynamics; it is not hiding a polynomial
representation of these safeguards. Avoiding their degree cost by
restricting to a good event would require proving an appropriate
good-event theorem for the proposed bounded-independence law.

### 10.4 Consequence of the audit

The elementary proposal "approximate each activation by a polynomial,
use $k$-wise initialization, and match all resulting monomials" does
not presently certify an absolute polylogarithmic seed. Its first
obstruction is a depth-dependent coordinate-support degree already
visible in (24)--(28); its long-time obstruction is repeated composition
in (30) or (32). These are exact algebraic counts and sufficient
moment-matching requirements, not a proof that no more selective
$k$-wise construction can work.

A successful refinement would need a quantitative bound on the
collective contribution of high-coordinate-support terms for the
actual nonlinear learned flow, uniform through the growing time
construction and all sphere queries. Alternatively it would need a
direct low-degree approximation of the final predictor with computable
coefficients and controlled propagation. Truncating Gaussian degree
after every layer or Picard iteration does not itself prove such an
estimate: nonlinear products can bring discarded components back into
low-degree coefficients. The initial-coordinate replacement remains
open after this bounded follow-up.
