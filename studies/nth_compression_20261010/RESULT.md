# NTH compression: exact counts, quantitative implications, and unresolved scope

Status, 2026-10-10: **partial result, not a same-scope compression theorem**.
The geometric-tail estimate used in the earlier conversation was hypothetical;
it is not a proved NTH guarantee and is not used below. We give exact storage,
the algebraic consequences of the published truncation statement, a complete
deterministic finite-panel comparison theorem, and two proved qualifications.
We do not claim an unconditional Gaussian feature-learning theorem, an
activation-only error constant, or an audited all-time test guarantee from NTH.

The main source is Huang–Yau, *Dynamics of Deep Neural Networks and Neural
Tangent Hierarchy*, [ICML 2020](https://proceedings.mlr.press/v119/huang20l/huang20l.pdf).
The accessible full proof is
[arXiv:1909.08156v1](https://arxiv.org/pdf/1909.08156), not a verified final
ICML supplement. Its cached PDF SHA256 is
`2036ab63a3e9ff20fa04c3f8d137dae385b9ba743b41a35aed1a92143e5fc91c`.
See [SOURCE_AUDIT.md](SOURCE_AUDIT.md) for the complete scoped source check.

## 1. Exact construction and costs

Let `n` be width, `m >= 2` the training count, `p` the number of passive query
inputs supplied at initialization, `d` the input dimension, `L` hidden depth,
and `q >= 2` the largest retained hierarchy rank. Queries never enter the loss.

The source's network, in these symbols, is

\[
h^{(0)}=x,\qquad h^{(\ell)}=n^{-1/2}\phi(W^{(\ell)}h^{(\ell-1)}),
\qquad f=w^\top h^{(L)}.
\]

The first matrix is `n by d`, the remaining hidden matrices are `n by n`,
and the readout has length `n`. All entries have independent Gaussian
initializations of fixed variance. Every parameter has Euclidean mobility
one for the loss \(\mathcal L=(2m)^{-1}\sum_{a=1}^m(f(x_a)-y_a)^2\).
This is not the maintained book's feature-learning metric and zero readout.
For sphere data use `x/sqrt(d)` as the source's input; this preserves the
input angles, not the training metric of the other model.

Writing all parameters as \(\theta\), define

\[
K^{(2)}(x,z)=\nabla f(x)^\top\nabla f(z),\qquad
K^{(r+1)}(x_1,\ldots,x_r,z)
=\nabla K^{(r)}(x_1,\ldots,x_r)^\top\nabla f(z).
\]

The chain rule gives, exactly,

\[
\dot f(x)=-\frac1m\sum_a K^{(2)}(x,x_a)(f(x_a)-y_a),
\quad
\dot K^{(r)}(x_1,\ldots,x_r)
=-\frac1m\sum_a K^{(r+1)}(x_1,\ldots,x_r,x_a)(f(x_a)-y_a).
\]

The closure copies all its retained initial values from the actual dense
initialization, freezes rank `q`, and evolves predictions and lower ranks
by the same equations with the closure residual. It needs train-only tensors
and slices with the first slot a passive query and every other slot training.
No future dense parameter is an initialization input.

### Proposition 1: direct-array storage

Without exploiting algebraic symmetries, the exact array counts are

\[
\begin{aligned}
\text{moving coordinates}&=(m+p)\sum_{j=0}^{q-2}m^j,\\
\text{fixed tensor coordinates}&=(m+p)m^{q-1},\\
\text{total, including labels and retained inputs}
&=(m+p)\sum_{j=0}^{q-1}m^j+m+(m+p)d.
\end{aligned}
\]

Thus total storage is at most
\(2(m+p)m^{q-1}+m+(m+p)d\). Each moving derivative contracts over
`m` residuals, so direct right-hand-side evaluation costs a constant times
\((m+p)m^{q-1}\) arithmetic operations. At `q=2`, the moving predictions
have `m+p` coordinates and the total is
\((m+p)(m+1)+m+(m+p)d\). The train-only frozen matrix can instead use its
symmetry to store `m(m+1)/2` entries. Higher tensors are not generally fully
symmetric; a binomial symmetric-tensor count is not justified.

Proof: a rank-`r` tensor requires `(m+p)m^(r-1)` entries. Sum the retained
ranks and the prediction vector; multiply the moving count by `m` for the
contractions. The geometric sum is bounded by twice its largest term for
`m >= 2`.

These are real-coordinate and per-RHS counts. They do not bound coefficient
precision, the cost of dense initialization, high-order automatic
differentiation, or the number of numerical time steps. Dense parameter
storage is exactly \(nd+(L-1)n^2+n\). A claimed compression also has to compare
the preceding retained count against this number. Merely eliminating `n`
from the display does not establish a saving for every `(n,m,q)`.

## 2. The literal published theorem's quantitative consequence

This section is an implication of the **stated external theorem**, not an
independently repaired version of its stochastic proof. Its exact untracked
dependencies cannot be renamed as activation-only constants.

Let `s` be its fixed regularity budget and let `q <= s` be even. The activation
has bounded derivatives through order `2s+1`; its value need not be bounded.
Input norms are bounded above and away from zero. For each
`1 <= j <= min(m,2s+1)`, every `j` distinct normalized input columns must have
smallest singular value at least a specified positive number `c_j`.
Let \(\lambda>0\) be a lower bound for the realized initial training NTK
eigenvalue. This is not an automatic renaming of the other model's population
feature-Gram gap \(\gamma\).

Name the source's constants `A,c,C,C'` without assigning them invented
dependence. They depend on fixed rank/regularity, depth, activation and data
conditioning; the proof also uses a bound on initial residual RMS. Its
training-RMS statement becomes

\[
\sup_{t\le T}\frac{\|f(t)-f_q(t)\|_2}{\sqrt m}
\le \frac{A(1+T)T^{q-1}}{n^{q/2}}
       \min\left(T,\frac m\lambda\right),                    \tag{1}
\]

on its claimed event and when

\[
T\le\min\left\{
\frac{c\sqrt{\lambda n/m}}{[\log n]^C},\quad
\frac{n^{s/[2(s+1)]}}{[\log n]^{C'}}\right\}.                \tag{2}
\]

At the precision \(n^{-1/2}\), the sufficient condition from (1) is exactly

\[
n^{(q-1)/2}\ge
A(1+T)T^{q-1}\min\left(T,\frac m\lambda\right),             \tag{3}
\]

along with (2). This follows by multiplying (1) by \(\sqrt n\); no
geometric-in-order convergence assumption has been inserted.

For example, take \(q=2\), \(T=(m/\lambda)h\), `h >= 1`, and `T >= 1`.
Then the three sufficient inequalities are

\[
\begin{aligned}
n&\ge4A^2(m/\lambda)^6h^4,\\
n&\ge c^{-2}(m/\lambda)^3h^2[\log n]^{2C},\\
n&\ge[(m/\lambda)h[\log n]^{C'}]^{2(s+1)/s}.
\end{aligned}                                               \tag{4}
\]

The online train-only storage is `m^2+2m`, or `m^2+2m+md` including inputs.
The first inequality in (4) is the precision requirement, the next two
are the two separate time-validity requirements. They cannot be dropped.

For any one fixed even `q`, taking `s=q` in the literal statement,
\(m/\lambda\ge1\), and \(T=(m/\lambda)\log(en)\), algebraically sufficient
conditions can be written

\[
n\ge C\left(\frac m\lambda\right)^{\max\{3,\,2(q+1)/(q-1)\}}
              [\log(en)]^C.                                \tag{5}
\]

Here `C` is emphatically a **source-background constant**, not an absolute
constant or one depending only on the activation. Enlarging a log exponent
absorbs the time logs and the source's two horizon exponents. Examples are

| Fixed order | Train-only retained order | Sufficient power of `m/lambda` in width, before log factors | Necessary dimension under source assumptions |
|---|---|---|---|
| 2 | `m^2+md` | 6 | `d >= min(m,5)` |
| 4 | `m^4+md` | `10/3` | `d >= min(m,9)` |
| 6 | `m^6+md` | 3 | `d >= min(m,13)` |

Each row is a consequence for a separately fixed order. Their constants
are not uniform over the rows, much less over `q=q(n)`. The proof of the odd
kernel improvement also needs one more higher-rank bound than the minimal
stated budget transparently supplies; increasing `s` can provide that bound,
but changes the data/derivative requirements. See the source audit.

Equation (1) is not a test error, not a uniform-input bound, not an all-time
bound, and not a dense-pair lower bound. To turn its RMS into a maximum over
the training points one can multiply its right side by `sqrt(m)`. That
changes (3) and the required width. Passive queries require an additional
comparison; it is supplied deterministically next, without assuming its
stochastic hypotheses have been established.

## 3. A complete deterministic finite-panel theorem at order two

This is a proved comparison theorem. The unresolved Gaussian source bounds
are explicit hypotheses, not hidden inside its conclusion.

Use the same half-MSE and effective kernel convention. Fixed positive
mobilities can also be absorbed in the parameter inner product. Suppose the
dense trajectory exists through `T`, the prediction functions are `C^3` in a
parameter neighborhood of that trajectory (so the hierarchy through rank
four and its chain-rule identities exist), and put
\(R=\|f(0)-y\|_2/\sqrt m\). Assume the initial train kernel satisfies
\(K^{(2)}_0\succeq\lambda I\), `lambda > 0`. On all slices with one first
slot in the training/query panel and the other slots training, suppose

\[
|K^{(2)}_0|\le M,\qquad
|K^{(3)}_0|\le B_3/n,\qquad
\sup_{0\le t\le T}|K^{(4)}_t|\le B_4/n.                    \tag{6}
\]

All inequalities are entrywise absolute bounds. The constants `M,B_3,B_4`
are declared inputs to the theorem; no width-independent bound for them is
asserted for the feature-learning network.

Define `u` by the order-two NTH, copying the initial predictions and freezing
all its train and query–train kernel entries at their actual initial values.
Then

\[
\sup_{t\le T}\max_{x\text{ in panel}}|f(t,x)-u(t,x)|
\le
\frac{1+M\min(T,m/\lambda)}{n}
\left(\frac{R^2B_3T^2}{2}+\frac{R^3B_4T^3}{6}\right).       \tag{7}
\]

In particular, the exact sufficient condition for `n^(-1/2)` panel accuracy is

\[
\sqrt n\ge[1+M\min(T,m/\lambda)]
\left(\frac{R^2B_3T^2}{2}+\frac{R^3B_4T^3}{6}\right).       \tag{8}
\]

If all the hypotheses hold on an event of probability `1-delta`, so does
the conclusion. The theorem does not manufacture that event. Retained
storage is the exact `q=2` count in Proposition 1, independent of `T`.

### Proof

The train kernel is a Gram matrix, so the dense loss is nonincreasing and
\(m^{-1}\sum_a|f_a(t)-y_a|\le R\). Integrating the exact hierarchy twice gives

\[
|K^{(3)}_t|\le(B_3+RB_4t)/n,\qquad
|K^{(2)}_t-K^{(2)}_0|\le(RB_3t+R^2B_4t^2/2)/n.             \tag{9}
\]

For the train error `e=f-u`,

\[
\dot e=-K^{(2)}_0e/m-(K^{(2)}_t-K^{(2)}_0)(f-y)/m,
\qquad e(0)=0.
\]

Using `||A||op <= m max|A_ab|`, positivity of the fixed train kernel, and
variation of constants, gives

\[
\frac{\|e(t)\|_2}{\sqrt m}
\le\int_0^t e^{-\lambda(t-s)/m}
\frac{R^2B_3s+R^3B_4s^2/2}{n}\,ds.                       \tag{10}
\]

For any panel input `x`, subtraction of its prediction equations yields

\[
\dot e_x=-\frac1m\sum_a(K^{(2)}_t(x,x_a)-K^{(2)}_0(x,x_a))(f_a-y_a)
          -\frac1m\sum_aK^{(2)}_0(x,x_a)e_a.
\]

Consequently its absolute error is at most the integral of the polynomial
forcing in (10), plus \(M\int_0^t\|e(s)\|_2/\sqrt m\,ds\).
Interchanging two nonnegative integrals in (10) bounds the latter integral
by `min(T,m/lambda)` times the integral of that forcing. The forcing integrates
to \((R^2B_3T^2/2+R^3B_4T^3/6)/n\), proving (7). This also applies when `x`
is a training point, so no missing `sqrt(m)` enters the panel maximum.

This proof is independent of the disputed probabilistic or differentiability
steps in the source. However, (6), especially the time-dependent fourth-order
bound on mixed slices, is precisely the missing bridge for a full theorem.

## 4. Raw-input conditioning cannot be replaced by the feature gap

### Proposition 2

For every fixed positive hidden depth with tanh activation there are unit
input data with three samples, positive population feature-Gram gap, and
singular raw input Gram. Moreover, nonsingular perturbations can have raw
conditioning tending to zero while their feature gaps remain uniformly
positive. Thus the source's `c_j` cannot be subsumed in a positive lower
feature-gap assumption alone.

Proof. In dimension two take `v1=e1`, `v2=e2`, and
`v3=(e1+e2)/sqrt(2)`. Their raw column matrix has rank two. The three
first-layer random features are

\[
\tanh(G_1),\quad\tanh(G_2),\quad\tanh((G_1+G_2)/\sqrt2),
\]

where `G1,G2` are independent standard Gaussians. If a real linear combination
has zero `L2` norm, continuity and full support imply the combination vanishes
for all real `(G1,G2)`. Taking one derivative in each coordinate forces the
coefficient of the third feature to be zero, because tanh's second derivative
is not identically zero. Taking separate derivatives then kills the other
two coefficients. Their Gram is positive definite.

For any subsequent layer, its Gaussian preactivation has full support because
the preceding Gram is positive definite. A linear combination of tanh of its
three separate coordinates vanishes identically only if all coefficients
vanish, by coordinate differentiation. Induction gives a positive feature
Gram at every fixed depth.

For the perturbation embed in dimension three and replace the third input
by `(e1+e2+epsilon e3)/sqrt(2+epsilon^2)`. For nonzero epsilon the raw columns
are independent, with minimum singular value tending to zero. Bounded
continuous tanh and Gaussian covariance continuity show the layer Grams
converge to those at epsilon zero. Their smallest eigenvalues therefore stay
above half their positive limiting values for sufficiently small epsilon.
The readout contribution to a limiting NTK is this feature Gram, so the same
example also prevents controlling raw conditioning by a lower NTK gap.

This is not a failure example for the NTH algorithm. It proves that the
extra hypothesis in the published theorem is genuinely extra, even for
fixed `m,d,L` and an admissible analytic activation.

## 5. The source's dense-pair benchmark is different

### Proposition 3

Consider the source's independent standard Gaussian hidden weights and
standard Gaussian readout, a fixed unit input, and any Lipschitz continuous
activation not identically zero. For each fixed depth, the difference of
two independent initialized predictions converges in distribution to a
nondegenerate centered Gaussian. In particular, full-trajectory dense-pair
variability is bounded below by a positive, width-independent number at
every fixed confidence. It is not a shrinking `n^(-1/2)` benchmark.

Proof. Define local scalar variances

\[
v_0=1,\qquad v_\ell=\mathbb E[\phi(\sqrt{v_{\ell-1}}G)^2],
\qquad G\sim N(0,1).
\]

They are finite and positive. At each layer, conditional on the preceding
feature vector, the `n` new preactivations are independent Gaussians with
variance equal to its squared norm. The conditional average of their
squared activations converges to the displayed expectation. Lipschitz growth
gives a fourth-moment bound `C(1+v^2)`, so conditional variances of these
averages are `O(1/n)` on bounded preceding-norm sets. Induction, continuity
of the Gaussian expectation, and tightness of the preceding norm show
\(\|h^{(L)}(x)\|_2^2\to v_L\) in probability.

Conditionally on both networks' last feature vectors, their initial prediction
difference is exactly Gaussian with variance the sum of those two squared
norms. Hence its limit is `N(0,2v_L)`.

More quantitatively, eventually with probability at least `1-delta/2`, the
conditional variance is at least `v_L`. A centered Gaussian of variance at
least `v_L` has probability at most `2a/sqrt(2 pi v_L)` of lying in `[-a,a]`.
Taking \(a=\delta\sqrt{\pi v_L/8}\) bounds this probability by `delta/2`.
Thus, for each fixed `0<delta<1` and all sufficiently large individual widths,

\[
\Pr\!\left\{
\sup_{t\in[0,T]}\max_{x\text{ in a panel containing the fixed input}}
|f_n(t,x)-\widetilde f_n(t,x)|
\ge\delta\sqrt{\pi v_L/8}\right\}\ge1-\delta.
\]

Here \(\widetilde f_n\) denotes the second independent dense network, not a
closure. The trajectory inequality is asserted for trajectories defined on
`[0,T]` with those initializations; Lipschitz activation alone in this
initialization proposition is not a claim of classical GF well-posedness.
Only time zero was used. This is not an endpoint theorem. Different fixed
positive initialization variances enter the scalar recursion and final
Gaussian variance explicitly. Zero readout invalidates this argument and
changes the benchmark; it cannot be substituted without revisiting the
NTH estimates.

## 6. What remains unresolved

The literal published statement yields equations (1)–(5), not a common-scope
competitor theorem for the maintained compression result. In particular:

- Its metric, normalization and readout law differ from the feature-learning
  model, even when the dense parameter count is the same.
- Its constants conceal depth, hierarchy order and input conditioning. No
  proved bound here replaces them by an activation-dependent base to an
  explicit power of `L` and polynomial factors in `m/gamma`.
- The source's prediction theorem controls train RMS over a finite horizon;
  its query construction is not accompanied by the needed mixed-kernel error
  theorem. The deterministic transfer above identifies the precise missing
  estimates without declaring them available.
- The inspected proof drops a logarithmic factor in its truncation estimate;
  its Gaussian-max assertion is incompatible with the declared
  stretched-exponential failure probability. Rank-revealing and
  iterated-integral repairs would also need to be supplied for the proof
  steps identified in the source audit. These observations do not prove the
  finite-horizon fixed-order conclusion false at fixed confidence.
- There is no proved growing-order error theorem here for the canonical
  feature-learning network. The earlier `m^{O(log n)}` forecast is withdrawn
  as a theorem claim.

The correct comparison entry is therefore **not yet certified at the same
scope**. Propositions 1–3 and the conditional finite-panel theorem are complete
arguments for their stated claims. They do not close the requested unconditional
compression theorem. No existing paper result has been edited or weakened.

## Check record

Root derived Propositions 1–3 and the mixed-panel transfer; the scoped
`nth_explicit_source` agent separately checked these statements and their
complete displayed proofs after writing the source audit. Its check covered
the exact counts, equations (3)–(5) and all three table exponents, absence of
a missing `sqrt(m)` in (7), the double-integral coefficient, the conditioning
example, and the `delta/2` Gaussian small-ball constant. It found no
mathematical error and requested the smoothness, trajectory-existence, and
independent-copy clarifications now incorporated above. This is an internal
consistency check, not the repository's independent promotion review. The
source stochastic estimates and the requested full-scope theorem remain
unresolved as explicitly stated in Section 6.
