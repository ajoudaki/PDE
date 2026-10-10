# Polynomial bounds for frozen-top NTH in the feature-learning scaling

For the subsequent general-input, two-hidden-layer **tanh** investigation,
see [TANH_RESULT.md](TANH_RESULT.md). Its fixed-order theorem does not yet
resolve the nonlinear growing-order storage question. The theorem below
remains specific to its stated linear-activation witness.

The later [NONLINEAR_RESULT.md](NONLINEAR_RESULT.md) proves a growing-order
obstruction for a fixed nonlinear first activation from the family
\(z+\varepsilon\sin z\), with a trained linear second layer. Its necessary
direct-array size is \(\exp(c\log n/\log\log n)\) along a specified width
sequence, for almost every fixed activation parameter. This rules out
fixed-power polylog budgets on that nonlinear witness; it does not resolve
two tanh layers or prove an \(\Omega(n)\) bound.

Status: proved for the stated construction and internally checked, 2026-10-10.
This is not promoted material or a completed independent promotion review.
This is a lower bound for a specified truncation rule. The storage consequence
is for its explicit tensor-array implementation, not every possible encoding
or every autonomous compressed model. No claim about optimal compression or
about the native Gaussian-readout NTK scaling is made.

## 1. Statement and scope

Take two training inputs `x1=sqrt(2)e1`, `x2=sqrt(2)e2` in dimension two,
two hidden layers of width n>=2, identity activations at both layers, labels
`(eta,0)`, and zero readout. First weights have independent `N(0,1)` entries;
the second matrix has independent `N(0,1/n)` entries. All blocks are
independent. Use the canonical block mobilities `(n,1,n)` and half-MSE.
The maintained chapter uses full MSE: doubling the vector field only rescales
physical time and leaves every complete-trajectory assertion below unchanged.

Fix any `0<eta<=10^(-62)`. This is a single width-independent label choice,
not a label shrinking with n. The activation is entire with derivative one,
the population feature Gram is the identity, and `m=d=L=2`, `gamma=1`.
With strip width two its activation constant in the maintained convention
is `beta=10`. Thus `Y=eta/sqrt(2)` satisfies the chapter's small-label condition.
This is an admissible *linear-activation witness* in that class, not a claim
that the same quantitative obstruction is proved for every nonlinear activation.

Let the order-q NTH copy the initialized dense predictions and hierarchy
tensors through rank q, freeze rank q, and evolve every lower rank using its
own residual. This is the frozen-top construction of Huang--Yau, equation (15)
of [the ICML paper](https://proceedings.mlr.press/v119/huang20l/huang20l.pdf),
applied to the actual feature-learning metric, not their different scaling.
Only that definition is imported; all estimates below are derived here.

Let

\[
D_n=\sup_{t\ge0}\sup_{\|x\|=\sqrt2}
       |f_n(t,x)-\widetilde f_n(t,x)|
\]

for an independently initialized dense copy. Let `E_n(q)` denote the same
error norm between the order-q closure and its dense reference, counting
nonexistence of the closure on the whole trajectory as failure. The lower
bound actually uses just its first training prediction on a fixed short
interval; it therefore applies to any claimed sphere or training/query-panel
guarantee containing that point.

### Main conclusion: strengthened polynomial lower bound

The stronger source calculation in
[STRONGER_SOURCE.md](STRONGER_SOURCE.md) retains the second hidden matrix's
motion. It improves the omitted derivative by a factorial and replaces the
previous subpolynomial necessary size by a polynomial one. Define explicitly

\[
\kappa_\eta=16\left[1+\log\frac{2^{20}}\eta+\log\frac83\right],
\qquad
C_\eta=\log\left(\frac{2^{23}e^2\kappa_\eta^2}{\eta}\right).
\]

On one event of probability at least `1-C exp(-cn)`, simultaneously for all
q>=2, with `j=2 floor(q/2)+1`,

\[
E_n(q)\ge\frac1{8\kappa_\eta}e^{-C_\eta j}.
\tag{S1}
\]

The all-time dense comparison proved in Section 5 is
`D_n=O_P(n^(-1/2))`. Therefore any deterministic order sequence achieving
`E_n(q_n)<=A D_n` with a fixed positive success probability at every
sufficiently large width, for a fixed finite A, must satisfy

\[
\liminf_{n\to\infty}\frac{q_n}{\log n}\ge\frac1{2C_\eta},
\qquad
\text{direct-array retained state}\ge
n^{\log2/(2C_\eta)-o(1)}.
\tag{S2}
\]

This is a positive polynomial exponent, **not** an Omega(n) lower bound.
For example, at the admissible fixed label eta=10^(-62), its exponent is
approximately 0.0019649183. The whole-sphere trajectory norm, physical-time
comparison, passive-query consequence, and all representation qualifications
are unchanged. The full factorial-source and analytic-remainder proofs are
in STRONGER_SOURCE; Sections 2 and 5 below supply their initialization and
dense-variability dependencies.

### A sublinear retained-array upper bound on this same witness

There is also an upper bound, proved in
[POLYNOMIAL_UPPER.md](POLYNOMIAL_UPPER.md), for exactly this model, loss,
initialization, and frozen-top rule. Simultaneously for every q>=2 on the
same good initialization event, the closure exists globally, reaches the
same fitted predictor, and obeys

\[
E_n(q)\le24576\eta(128\eta)^{q-1}.                 \tag{S3}
\]

This bound controls the entire physical-time trajectory on the input sphere,
using the closure's own residual; it is not a comparison of source clocks.
For the actual independent dense pair, an elementary small-ball argument gives

\[
\Pr\left\{D_n\ge\frac{\eta^2}{2^{33}n^4}\right\}
\ge1-\frac{8+2e}{n}-C e^{-cn}.                   \tag{S4}
\]

This deliberately coarse lower bound suffices to choose

\[
q_n=\max\left\{2,1+\left\lceil
\frac{5\log n+\log(3\cdot2^{46}/\eta)}
     {\log(1/(128\eta))}\right\rceil\right\}.
\tag{S5}
\]

With probability at least `1-(8+2e)/n-C exp(-cn)`, it gives
`E_n(q_n)<=D_n/n`. Its retained array count is bounded by the explicit expression

\[
2^{q_n+1}-2\le
8\left(\frac{3\cdot2^{46}}\eta\right)^{
\log2/\log(1/(128\eta))}
n^{5\log2/\log(1/(128\eta))}.
\tag{S6}
\]

For the existing witness's fixed label range eta<=10^(-62), the exponent
in (S6) is less than 1/20. Thus, on this witness, even an Omega(n)
retained-array lower bound is false. This is retained state **after** the
initialized tensors have been obtained, not a preprocessing work or peak-memory
bound. Both the lower and upper bounds concern literal tensor arrays, not an
optimal encoding. Their polynomial exponents need not match.

This does not disprove a stronger **worst-case** lower bound elsewhere in the
admissible class. The separate bounded nonlinear search
[STRONG_NONLINEAR_SEARCH.md](STRONG_NONLINEAR_SEARCH.md) proves a shrinking
individual source-analyticity radius for one admissible activation, but also
exhibits why averaging can remove such an obstruction. It establishes no
stronger canonical NTH prediction or storage lower bound. The worst-case
Omega(n), superpolynomial, and exponential questions remain unresolved.

### Earlier weaker estimate, retained as a valid intermediate bound

The following estimate and its Sections 3--4 proof remain valid, but are
superseded as the headline necessary order and size by (S1)--(S2).

There are absolute positive constants `c,C` and a constant `C'_eta`, independent
of n and q, such that, on one event of probability at least `1-C exp(-cn)`,
simultaneously for all q>=2, with `j=2 floor(q/2)+1`,

\[
E_n(q)\ge
\exp\{-j\log j-2j\log\log(ej)-C'_\eta j\}.              \tag{1}
\]

Moreover `D_n=O_P(n^(-1/2))` for the whole sphere and the entire trajectory,
including the common fitted endpoint. Consequently, if

\[
\limsup_{n\to\infty}\frac{q_n\log q_n}{\log n}<\frac12,
\]

then for every fixed comparison factor `A<infinity`,

\[
\Pr\{E_n(q_n)\le A D_n\}\longrightarrow0.              \tag{2}
\]

In particular, a deterministic order choice achieving any fixed positive
success probability for a constant-factor dense-pair comparison at every
sufficiently large width must satisfy

\[
\liminf_{n\to\infty}\frac{q_n\log q_n}{\log n}\ge\frac12,
\qquad
q_n\ge\left(\frac12-o(1)\right)\frac{\log n}{\log\log n}.\tag{3}
\]

The direct tensor-array implementation stores at least `2^(q-1)` coordinates
even if an identically zero odd top rank is omitted. Its declared moving
arrays have at least `2^(q-2)` coordinates, allowing the same simplification.
For that implementation, (3) gives

\[
\text{retained coordinates}\ge
\exp\!\left\{\left(\frac{\log2}{2}-o(1)\right)
                         \frac{\log n}{\log\log n}\right\}.\tag{4}
\]

This earlier necessary size grows faster than every fixed power of log n.
It is itself subpolynomial; the sharper necessary polynomial size is (S2).
Neither is a sufficient size or a lower bound for an algebraically compressed
implementation.

## 2. Metric normalization and a high-probability initialization event

Set `B=W1/sqrt(n)`, `W=W2`, and `c=u/sqrt(n)`. The function and training metric
become

\[
f(v)=c^\top WBv,\qquad v=x/\sqrt2,
\qquad \mathcal L=\tfrac14\sum_{a=1}^2(f(e_a)-y_a)^2,
\]

with Euclidean Frobenius metric on all three blocks. Both B and W have
independent `N(0,1/n)` entries and `c(0)=0`. This is exactly the original
canonical network under a change of stored coordinates, not a new model.

Use the initialization event

\[
\tfrac12 I\preceq B^\top B\preceq2I,\qquad
\|W\|_{\rm op}\le4,\qquad
\sigma_{\min}(WB)\ge\tfrac34.                            \tag{5}
\]

It has probability at least `1-C exp(-cn)` for absolute c,C. Here is an
elementary verification. For an n-by-2 matrix G with iid `N(0,1/n)` entries,
each fixed unit v has `n||Gv||^2` distributed as chi-square with n degrees
of freedom. The moment-generating function `(1-2t)^(-n/2)` and exponential
Markov give exponential tails for any fixed deviation. A fixed 1/8-net of
the unit circle converts these bounds into
`||G^T G-I||op<=1/6` with exponentially high probability: for a symmetric
matrix A, the maximum of `|v^TAv|` on this net is at least
`(1-2/8)||A||op`. Take fixed-direction deviation 1/8.

Conditional on B, write its thin factorization `B=UR` with U orthonormal.
The independent matrix WU is again an n-by-2 iid `N(0,1/n)` matrix.
The two preceding Gram events give
`sigma_min(WB)>=sqrt(5/6)sqrt(5/6)=5/6>3/4`.
For W itself, a 1/4-net of the n-sphere has at most `9^n` points and
`||W||op<=4/3 max_net||Wv||`. The chi-square upper tail at squared norm nine
is at most `exp[-(8-log9)n/2]`; the union bound is exponentially small
because `(8-log9)/2-log9>0`. This proves (5).

## 3. An omitted derivative bounded below at every order

For a training index a put `V_a=grad f(e_a)` in the normalized Euclidean
metric. Define `K2(a,b)=D f(e_a)[V_b]` and append indices by
`K(r+1)(a1,...,ar,b)=D K_r(a1,...,ar)[V_b]`.

At zero readout every odd-rank tensor is zero. Indeed reflection `c -> -c`
makes f odd, its unit-residual vector field reverse parity appropriately,
and each directional derivative toggles the parity of the preceding scalar
function. Thus K2 is even, K3 odd, and so on. This also shows that order
`2k+1` NTH is exactly order `2k` NTH: its frozen top tensor is zero, making
the rank-2k tensor constant.

For even q, repeated differentiation of the exact and truncated hierarchy
at zero shows that their prediction jets agree through degree q, while

\[
\partial_t^{q+1}(f_1-f_{q,1})(0)
=\left(\frac\eta2\right)^{q+1}K_{q+2}(1,\ldots,1)(0).   \tag{6}
\]

To check the index and coefficient: at the top retained rank, the first
derivative difference is zero because K(q+1)(0)=0. Its first nonzero
derivative is the second, namely `(eta/2)^2 K(q+2)(1,...,1)`.
Each lower equation propagates this first nonzero derivative once, multiplying
by `eta/2`. Terms differentiating residuals contain only earlier differences,
which vanish. There are q-1 further equations down to the prediction.
The second label is zero, so every appended index in this first discrepancy
must be 1. This gives (6), without combinatorial or sign loss.

We next lower-bound its tensor deterministically on (5). Follow unit-residual
gradient ascent for the first prediction, using an auxiliary source variable s.
Writing `a=B e1`, it obeys

\[
a'=W^\top c,\qquad W'=ca^\top,\qquad c'=Wa.             \tag{7}
\]

The other column of B is fixed. By orthogonal changes of hidden coordinates,
put the initialized W into diagonal singular-value form. Simultaneous row
and column sign changes then make every entry of the initialized a
nonnegative, while preserving the nonnegative diagonal W. Initially c=0.
In these coordinates all Taylor coefficients of (7), and of `c^TWa`, are
nonnegative: the Taylor recurrence is sums and products with positive
integer divisors. Suppressing the equation W'=ca^T can only decrease those
coefficients, coefficient by coefficient.

With W frozen, setting `M=W^T W`, the output is

\[
\frac12 a^\top \sqrt M\sinh(2s\sqrt M)a.
\]

This identity is interpreted by its entire matrix power series, including
zero eigenvalues. Therefore for odd `j=q+1`,

\[
K_{q+2}(1,\ldots,1)(0)
\ge 2^{j-1}a^\top M^{(j+1)/2}a\ge\frac18.              \tag{8}
\]

For the last step, (5) implies `1/2<=||a||^2<=2` and
`a^TMa=||Wa||^2>=1/2`. Applying convexity of `x -> x^k` to the spectral
probability measure with weights `|a_i|^2/||a||^2` gives
`a^TM^k a>=||a||^2 (a^TMa/||a||^2)^k>=2^(-1)4^(-k)`.
Substitution of `k=(j+1)/2` proves (8).

Consequently the error derivative in (6) is at least `(eta/16)^j`.
No growing-order Gaussian concentration or exchange of width/order limits
was used: this is deterministic and simultaneous in q on (5).

## 4. From the omitted derivative to actual trajectory error

The complete dimension-free analytic argument is in
[ANALYTIC_ROUTE.md](ANALYTIC_ROUTE.md). Its inputs are just the deterministic
polynomial network and `max(||B0||op,||W0||op)<=4`, not a population theorem.
It establishes the following two facts.

1. The dense predictions and every frozen-top NTH prediction are holomorphic
   on a common disk about physical time zero of radius `R=1/8192`, and have
   absolute value at most one there, uniformly in n and q. The finite NTH
   equations are equivalent to a finite ordered-Volterra expansion using
   their own residual. Ordered Lie derivatives of the cubic prediction
   grow at most as `32*4^k*(k+2)!`; the time-simplex factor `1/k!` yields a
   summable majorant on a sufficiently small disk, uniformly in the cutoff.
2. If a scalar holomorphic error on this disk is bounded by two and has
   its j-th derivative at zero at least `a^j`, for fixed a>0, then
   its supremum on `[0,R/4]` is at least
   `exp[-j log j-2j log log(ej)-C_a j]`.

For clarity, the second assertion does not infer a function gap from a jet
without a remainder estimate. Take its Taylor polynomial of degree N.
Cauchy's coefficient bound gives error at most `(2/3)4^(-N)` on `[0,R/4]`,
while its j-th derivative at zero is exactly that of the original function
if N>=j. Expanding this polynomial in Chebyshev polynomials and using
`|T_k^(j)(1)|<=k^(2j)/j!` bounds its endpoint derivative by
`(2N/j!)(8N^2/R)^j` times its supremum. This factorial is important.
At `N=ceil(A_a j log(ej))` the Taylor tail is small enough to give the
asserted estimate. Every constant and inequality is detailed in the analytic
route, without importing an endpoint inequality for complex coefficients.

In fact, with `j=2 floor(q/2)+1`, define the local integer

\[
N=\left\lceil32\left[1+\log\frac{2^{20}}\eta+
                    \log\frac83\right]j\log(ej)\right\rceil.
\]

The fully explicit bound before logarithmic simplification is

\[
E_n(q)\ge\frac{(\eta/2^{20})^j j!}{4N^{2j+1}}.          \tag{1a}
\]

Apply these facts to (6)--(8) with `a=eta/16`. This proves (1), with a
physical-time witness and a constant independent of n and q. It also gives
existence of all closures on the short interval needed for the obstruction.
This weaker proof is retained only as an intermediate estimate. The sharper
factorial derivative and linear-in-j Taylor degree in STRONGER_SOURCE prove
(S1), rather than replacing the physical-time argument with a source-clock
comparison.

## 5. Entire-trajectory variability of two dense networks

We prove `D_n=O_P(n^(-1/2))` directly, without importing a dense variability
theorem from a different model or study. All constants below are deliberately
loose finite absolute constants; eta is fixed. This part uses small eta,
not any asymptotic dependence of eta on n.

The finite dense flow exists at all finite times even outside the good event:
the Euclidean gradient-flow identity gives
`integral_0^T ||dot X||_H^2 dt <= L(0)` and hence
`||X(T)-X(0)||_H <= sqrt(T L(0))`. On each finite time interval this precludes
escape to infinity for a polynomial, locally Lipschitz vector field. Fitted
limits and the estimates below are asserted on the good event. A missing
fitted limit can be counted as failure off that event without affecting the
asymptotic probability conclusions.

### 5.1 Global fitting and bounds near initialized parameters

For parameter increments use the ordinary sum-of-squared-Frobenius norm,
denoted `||.||_H`. All perturbed initializations in this section also keep
the readout exactly zero. Although initialized W has Frobenius norm of order sqrt(n),
its operator norm is bounded on (5). In any H-ball of radius 1/100 about
an initialization within distance 1/100 of (5), every block has operator
norm at most five, and

\[
\sigma_{\min}(WB)>\tfrac12,
\quad \|J\|_{H\to\mathbb R^2}\le100,
\quad \|DJ\|_{H\times H\to\mathbb R^2}\le50,           \tag{9}
\]

where `J=D(f1,f2)`. The singular-value assertion follows from
`||Delta(WB)||op<=||Delta W||op||B||op+||W||op||Delta B||op`
and the product increment: a total parameter displacement at most 2/100
changes WB by at most `8(2/100)+(2/100)^2<1/4` from a point of (5).
The J bound follows from its three gradient blocks, each of norm at most
25, giving `sqrt(6)*25<100`. The Hessian consists of six trilinear product
terms, giving `6 sqrt(2)*5<50`.

The readout part of the tangent kernel `K=JJ^T` is `(WB)^T(WB)`, so
`K>=I/4` there. The exact equations give

\[
\dot r=-Kr/2,\qquad \|r(t)\|_2\le\eta e^{-t/8},
\qquad \|\dot X(t)\|_H\le50\eta e^{-t/8}.             \tag{10}
\]

The resulting total parameter displacement is at most `400 eta<1/100`.
A first-exit argument closes the ball assumption for all time. The polynomial
ODE therefore exists globally, the parameters converge, and training
predictions converge to `(eta,0)`. Since every prediction is linear in v
and the two training inputs form its coordinate basis, this is also the
whole-sphere fitted predictor.

### 5.2 Sensitivity to the Gaussian initialization

Differentiate the real gradient flow with respect to a hidden-parameter
initial perturbation `Z(0)`; the initial readout remains zero. In (9)--(10),

\[
\dot Z=-J^TJZ/2-\tfrac12\sum_a r_a\nabla^2 f_a\,Z.
\]

Taking its inner product with Z discards the negative Gram term and gives
`d||Z||_H/dt<=25 eta e^(-t/8)||Z||_H`. Thus
`||Z(t)||_H<=exp(200 eta)||Z(0)||_H<=2||Z(0)||_H`.
Since `delta f(0)=0`, differentiation of the residual equation gives

\[
(\delta f)'=-K\delta f/2-(\delta K)r/2,
\qquad \|\delta K\|_{\rm op}\le20000\|Z(0)\|_H.
\]

Variation of constants with the Gram gap yields

\[
\begin{aligned}
\|\delta f(t)\|_2
&\le10000\eta t e^{-t/8}\|Z(0)\|_H,\\
\|\delta\dot f(t)\|_2
&\le10^8\eta(1+t)e^{-t/8}\|Z(0)\|_H.                 \tag{11}
\end{aligned}
\]

These local derivatives also give global Lipschitz bounds on the good set
(5). For two initialized points at H-distance at most 1/100, integrate
(11) along their joining line, which lies in the neighborhood just proved.
For a pair farther apart, use (10) and their common endpoint instead:
the prediction difference is at most `2 eta e^(-t/8)`, and the velocity
difference at most `10000 eta e^(-t/8)`. After division by their distance,
these are bounded by the same envelopes

\[
L_f(t)=10^4\eta(1+t)e^{-t/8},\qquad
L_{\dot f}(t)=10^8\eta(1+t)e^{-t/8}.                   \tag{12}
\]

The standardized Gaussian initial coordinates are multiplied by `1/sqrt(n)`
to form B,W. Each scalar component in (12) is therefore Lipschitz with
constant `L(t)/sqrt(n)` on the good subset of standard Gaussian space.

### 5.3 Concentration uniformly over the whole half-line

A Lipschitz real function on a subset of Euclidean space has an extension
with the same Lipschitz constant: take
`inf_z [F(z)+Lip||x-z||]`, with z in that subset. Apply this separately
to each prediction component at each t, and to each velocity component.
One can take the infimum over a countable dense subset, so these extensions
are measurable jointly with t. They need not be derivatives of one another
off the good set; on that set they equal the actual predictions and velocities.

For a standard Gaussian vector G, a Lipschitz scalar F obeys
`Var F(G)<=Lip(F)^2`. One direct proof uses the Gaussian averaging semigroup
`P_sF(x)=E F(e^(-s)x+sqrt(1-e^(-2s))G)`: Gaussian integration by parts gives
`Var F=2 integral_0^infinity E||grad P_sF||^2 ds`; differentiation under
the average gives `||grad P_sF||<=e^(-s)Lip(F)`, and integration gives the
claim. Smooth bounded approximations justify both identities for Lipschitz
F by dominated convergence under the Gaussian measure.

Let the two independent initializations both satisfy (5). Their vector
prediction difference g obeys `g(0)=0` and

\[
\sup_{t\ge0}\|g(t)\|_2^2
\le\int_0^\infty(\|g(t)\|_2^2+\|\dot g(t)\|_2^2)\,dt.\tag{13}
\]

This follows by integrating the derivative of `||g||^2` and using
`2|g dot g'|<=||g||^2+||g'||^2`. For the Lipschitz extensions the independent
pair difference has second moment twice the variance. Summing the two
components and applying Tonelli to (13) gives

\[
\mathbb E[\mathbf1_{\text{both good}}D_n^2]
\le\frac4n\int_0^\infty(L_f(t)^2+L_{\dot f}(t)^2)\,dt
\le\frac{7\cdot10^{18}\eta^2}{n}.                     \tag{14}
\]

Here `integral_0^infinity(1+t)^2 exp(-t/4)dt=164`, and
`sup_{||v||=1}|g dot v|=||g||_2` identifies the sphere norm exactly.
The exponentially small bad-set probability and Markov's inequality prove
the asserted `O_P(n^(-1/2))` bound. This argument controls the entire
trajectory and endpoint, not just an early compact interval.

## 6. Consequences and limitations

Let the deterministic right side of (1) be b_n at order q_n. If
`limsup q_n log q_n/log n<1/2`, then `sqrt(n)b_n -> infinity`.
For each fixed A,

\[
\Pr\{E_n(q_n)\le A D_n\}
\le C e^{-cn}+\Pr\{\sqrt n D_n\ge\sqrt n b_n/A\}\to0.
\]

This proves (2). If the liminf in (3) failed, a subsequence with limsup
strictly below 1/2 would contradict any fixed positive eventual success
probability. Standard inversion of `q log q` gives the second part of (3).
For direct arrays with two samples, the retained tensor counts are
`2+sum_(r=2)^q 2^r=2^(q+1)-2`, excluding inputs and labels; the declared
lower-level array count is `2^q-2`. For the effective even order
`q_eff=2 floor(q/2)`, the corresponding moving-array count is
`2^(q_eff)-2`. These imply (4). Odd ranks initialized to zero may be
omitted or reduced to the preceding even order; this changes constants,
not the asymptotic conclusion.

There is no information-theoretic storage conclusion. Tensor identities,
compressed tensor formats, implicit coefficient generation, or a different
top closure are not excluded. Indeed [SCALAR_ROUTE.md](SCALAR_ROUTE.md)
gives a shallow scalar example where the same frozen-top rule needs
growing order while a different exact autonomous model has constant state.
The current deep witness is linear in its input and uses orthogonal data;
that is a valid counterexample to a uniform class-wide claim, but not
evidence that generic nonlinear data require this size. The construction
does train both hidden layers in the feature-learning metric.

The lower bound is not a contradiction of Huang--Yau's native theorem:
its parameter scaling/readout law differ. Nor is it an obstruction to the
maintained compression constructions, which use different closures.

### A fixed unseen-query panel also witnesses the obstruction

Take the two normalized passive queries `(e1+e2)/sqrt(2)` and
`(e1-e2)/sqrt(2)`, distinct from both training inputs. The exact predictor
is linear in the query, and the NTH predictor is linear in its first input
slot as well: all initialized hierarchy entries have this property, and the
query evolution preserves it. If the two training prediction errors are
`e1(t),e2(t)`, the two query errors are `(e1(t)+e2(t))/sqrt(2)` and
`(e1(t)-e2(t))/sqrt(2)`. Their maximum absolute value is at least
`|e1(t)|/sqrt(2)`. Thus the same necessary-order conclusion holds when
the comparison norm uses only these two unseen queries, with an immaterial
factor `1/sqrt(2)` in the lower bound. Their labels are never used, and
their inputs may be declared before initialization. The dense-pair query
discrepancy is bounded above by the whole-sphere D_n already controlled.

## Check record

Root derived the deep source-coefficient positivity, physical jet discrepancy,
global fitting, Gaussian sensitivity and all-time comparison. The scoped
`nth_lower_analytic_check` route supplies the uniform-cutoff analytic bound
and derivative-to-real-interval estimate; its named helper and complete input
scope are recorded in that file. Root read and checked the complete argument.
The scoped `nth_lower_scalar` agent then checked this assembled result and
the analytic dependency, including the probability event, source positivity,
jet order, all-time Gaussian sensitivity and passive-query consequence.
Its report [DEEP_CHECK.md](DEEP_CHECK.md) found no blocking mathematical gap
and requested the explicit global-existence and odd-order storage clarifications
now incorporated. Root separately verified the maintained-book normalization,
activation constant and small-label interface, which were outside that checker's
scientific input scope. No numerical experiments or promotion review were run.

For the strengthening, root read the complete STRONGER_SOURCE,
POLYNOMIAL_UPPER, and STRONG_NONLINEAR_SEARCH arguments. The lower-bound
reconstruction checks the matrix invariants, coefficientwise tangent
comparison, factorial physical-time derivative, and all-order real-interval
remainder estimate. The upper-bound reconstruction checks the ordered
integrals, kernel symmetry, small-action bootstrap for each model's own
residual, moving-state remainder, global error absorption, and actual-pair
small-ball estimate. The nonlinear search remains an auxiliary source result,
not a canonical complexity theorem. These are scoped internal checks only.
The additional full upper-bound check is
[SAME_STUDY_CHECK.md](SAME_STUDY_CHECK.md). Its sole requested synthesis
correction, distinguishing the new polynomial lower bound from the superseded
subpolynomial estimate, is incorporated. Root read that complete report.
