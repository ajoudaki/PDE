# Quantitative finite Gaussian program route

Initial independent result frozen 2026-10-01. Status: candidate proof, awaiting
independent reconstruction. This document uses only the assigned current paper
files, in particular `paper/proof_alltime.tex`, `paper/proof_tracking.tex`,
`paper/results.tex`, and the setting in `paper/main.tex`. No other study or
route findings were read. The supervisor independently proposed the same
regularization mechanism after this route had reached it; subsequent messages
suggested a compatible parameter budget and assigned the final all-time
transfer to the supervisor. No experiments were run.

## Claim and scope

There is a quantitative finite-program lemma with constants exponential in a
fixed polynomial of the instruction budget. It does **not** require a lower
bound on the original query covariances. The regularization is solely a proof
device; the finite network and response-memory closure remain unchanged.

For the paper's population Euler reference with at most `N` scalar/vector
instructions, clip every training backward product at carrier magnitude `N`
and add independent input noise of amplitude `exp(-N^2)` to each initialized
matrix query, in either orientation. All deterministic coefficients are the
original population Euler coefficients. For sufficiently large `N`, the
modified population program differs from the original one by at most

\[
 \eta_N=C e^{-cN^2}
 \tag{1}
\]

in the maximum nodewise scalar `L^2` norm. On the actual finite arrays, the
modified program admits a coupling to coordinatewise iid copies of its scalar
population law such that

\[
 \max_v\|v_n-v^*_n\|_2/\sqrt n
       \le e^{CN^5}n^{-1/4},
 \qquad
 \Pr(\text{failure})\le e^{CN^5}n^{-1/2}+Ce^{-cn},
 \tag{2}
\]

provided `log n >= C N^5`. The same event can include at most `N^2` additional
scalar empirical tests of the following forms: pairings of two nodes, squared
norms, and squared positive-part carrier tails. Errors in these empirical
quadratic quantities relative to the modified population expectation are at
most `exp(C N^5)n^{-1/4}`. The corresponding tail-norm errors are at most
`exp(C N^5)n^{-1/8}`. Constants depend on the fixed problem, not on `N,n` or
the actual covariance eigenvalues.

For example, `N <= C (log n)^(1/32)` makes all these errors at most `n^(-1/16)`
and the failure probability at most `n^(-1/4)`, after increasing the fixed
width threshold. The numerical exponent `5` is deliberately loose.

The lemma treats any one normalized passive input with constants independent
of that input: divide all of its forward fields by
`s_x=1+||x||/sqrt(d)` and use the map `u -> phi(s_x u)/s_x`, whose value at
zero and Lipschitz constant are uniform in `x`. Passive queries require no
derivative of that map. A finite collection of probes is allowed when its
instructions and tests fit in the budget.

## 1. Program model and counting

Instructions comprise independent Gaussian root coordinates; deterministic
linear combinations; coordinate maps; and applications of an initialized
matrix or its actual transpose. Each Gaussian matrix has entries `N(0,1/n)`.
The matrices are reused. A linear combination may equivalently be expanded
into additions and scalar multiplications; count all such edges if necessary.

At `K` Euler nodes and fixed `L,m,d`, expanding the learned rank-one actions
uses `O(K^2)` instructions for training plus any fixed list of passive inputs.
The scalar coefficients are frozen at population values. The total absolute
coefficient in a training memory sum is bounded by `C sum alpha_k <= C`.
Normalized passive queries have the same bound, by Cauchy--Schwarz against
their uniformly bounded population RMS. For `P` passive inputs, the elementary
count is `C K^2(1+P)`; it is sufficient to take any deterministic upper bound
`N` for that number and the added Gaussian roots.

Clipped products are

\[
 (z,p)\longmapsto g_\ell(z)\operatorname{clip}_N(p).
\]

They satisfy

\[
 |g(z)\operatorname{clip}_N(p)
  -g(z')\operatorname{clip}_N(p')|
 \le jN|z-z'|+s|p-p'|.
 \tag{3}
\]

Thus every coordinate instruction has a global Lipschitz bound `C N^2` and
intercept bound `C N^2`; this intentionally overestimates the actual bounds.
No classical second derivative is used in the quantitative argument.

## 2. Explicit scalar regularization bias

The current paper constructs joint scalar laws for finite unions of programs
on common population spaces with initialized operators of norm at most `K_0`.
Use that construction for the original and modified program together. This
is an application of its **qualitative** finite-program theorem at each fixed
`N`, not an assertion of a quantitative width rate from that theorem.

The original reference training carriers have the uniform population bound

\[
 \|P\,1_{|P|>B}\|_2\le C e^{-cB^2}.
 \tag{4}
\]

For the C^{1,1} activation class the same assertion for each fixed original
Euler program follows by mollifying the activation, applying the paper's
uniform smooth-program bound, and passing through its finite list of value
instructions. This passage uses bounded slope, Lipschitz derivative, a
cutoff against the smoothed reference carriers, and then Fatou. It needs no
uniform-in-program mollification estimate here.

At a matrix call, adding a fresh scalar Gaussian root `epsilon chi` costs at
most `K_0 epsilon` in population `L^2`. At a clipped product, (3) propagates
the previous discrepancies and clipping the *original* carrier adds at most
`s ||P 1_{|P|>N}||_2`. Every other instruction is Lipschitz. If `E_j` is the
maximum discrepancy through instruction `j`, chronological induction gives

\[
 E_j\le C N^2 E_{j-1}+C(\epsilon+e^{-cN^2}),\qquad E_0=0.
\]

With `epsilon=exp(-N^2)`, this yields

\[
 E_N\le (C N^2)^{N+1}(e^{-N^2}+C e^{-cN^2})
       \le C e^{-c' N^2}.
\]

Only training carrier products are clipped; passive activations do not need
clipping. This avoids requiring sub-Gaussian constants uniform over
unnormalized passive inputs. This proof also transfers the bound to any
continuous tail norm by its 1-Lipschitz dependence on its scalar argument.

## 3. Conditioning without a hidden spectral hypothesis

At **each** matrix call, use a new Gaussian root independent of the entire
previous computation, including previous roots. Write the queried input as

\[
 h=h_0+\epsilon\chi.
\]

For the scalar query variables `v_1,...,v_p` in one orientation, the squared
distance of `v_j` from the span of its predecessors is at least `epsilon^2`.
Indeed the fresh `chi_j` is independent of those predecessors and of
`h_{0,j}`, has mean zero and variance one. Its contribution to the squared
distance is orthogonal and exactly `epsilon^2`.

A crude population RMS bound for every modified node is

\[
 B=(C N^2)^{N+1}.
 \tag{5}
\]

To prove (5), propagate the common population operator bound through matrix
calls, the global coordinate Lipschitz/intercept bounds through coordinate
instructions, and the deterministic coefficient sums through linear
combinations. The fresh Gaussian roots have RMS one. This uses no inverse
covariance bound.

For every query Gram `G_p=(E[v_i v_j])`, its successive Schur complements
are at least `epsilon^2`, hence

\[
 \det G_p\ge\epsilon^{2p},\qquad
 \operatorname{tr}G_p\le pB^2,
 \qquad
 \lambda_{\min}(G_p)\ge
       \frac{\epsilon^{2p}}{(p B^2)^{p-1}}.
\]

Since `p<=N`, both orientations of every matrix satisfy the common bound

\[
 \lambda_{\min}(G_p)\ge\gamma:=e^{-C N^3}.
 \tag{6}
\]

The same fresh root shows that the variance of the new Gaussian innovation
at each call is at least `epsilon^2`. This latter fact is the reason the
coupling does not lose a square-root exponent at every instruction.

## 4. Scalar regression construction and fourth moments

Use the conditional Gaussian formula proved in the current paper. For a
forward call with old constraints `WV=Y` and `W^T U=Q`, write

\[
 G=E[V^T V],\quad H=E[U^T U],\quad
 \alpha=G^{-1}E[V^T h],\quad h_\perp=h-V\alpha,
\]

where the notation denotes scalar query Gram matrices and scalar vectors,
not width-dependent matrices. The limiting call is represented by

\[
 y=Y\alpha+U\beta+\sigma g,\quad
 \beta=H^{-1}E[Q^T h_\perp],\quad
 \sigma=\|h_\perp\|_2,
 \tag{7}
\]

with a fresh standard Gaussian `g` at the output layer. Empty query lists
contribute zero. Reverse calls use the transposed formula. All coefficients
in (7) are deterministic. The existing finite-program result identifies
this regression law with the modified program's population law because its
query Grams are positive definite by (6).

From (5)--(6), coefficient absolute sums are at most

\[
 A_0=(C N B/\gamma)^C,
\]

after increasing the fixed exponent to handle `h_perp=h-V alpha`. Also
`sigma<=B`. Minkowski's inequality, (7), and the coordinate Lipschitz bounds
give, by induction over at most `N` instructions,

\[
 M_4:=\max_v\|v\|_{L^4}\le
       (C N^2 A_0 B)^{C N}\le e^{C N^4}.
 \tag{8}
\]

This is an intentionally wasteful bound. It is independent of the actual
small eigenvalues of the original, unregularized program.

## 5. Coupling to iid scalar arrays

Construct the actual program and its scalar iid reference together. The
root Gaussian arrays are shared exactly. When a matrix answer is revealed,
the conditional Gaussian formula supplies a new independent standard
Gaussian vector `g` at its output layer. Use its coordinates for the new
scalar variables in (7). Previous scalar arrays depend on earlier roots and
innovations, so these reference arrays remain iid across coordinates within
each layer. Coefficients in their recursion are deterministic population
coefficients; finite-array empirical contractions do not enter them.

For `t=n^(-1/4)`, impose the following finitely many events.

1. Every scalar iid empirical pairing needed in a regression differs from
   its scalar expectation by at most `t`.
2. The same holds for the extra squared-norm, pairing, and squared-tail
   tests selected in advance, at most `N^2` tests in total.
3. Each removed conditional noise projection has normalized norm at most
   `t`, and each fresh noise vector has normalized norm at most two.
4. All initialized matrix operator norms are at most the fixed `K_0`.

There are `O(N^2)` pairings. Each has variance at most `M_4^4/n`, by
Cauchy--Schwarz and independence across coordinates. The squared-tail test
`(|v|-M)_+^2` has the same variance bound, uniformly in its threshold.
Chebyshev and a union bound give failure at most

\[
 C N^2 M_4^4/(n t^2)\le e^{C N^4}n^{-1/2}.
 \tag{9}
\]

For a conditional orthogonal projection onto at most `N` known directions,

\[
 E[\|P g\|_2^2/n\mid\text{past}]\le N/n.
\]

Markov at threshold `t^2`, followed by a union bound over calls, gives
`C N^2/(n t^2)`. Gaussian norm and initialized-operator failures cost
`C N e^{-cn}`. No independence between the projection events is needed.

Let `e_j` be the maximum normalized coupling error through instruction
`j`. On the event just constructed, any empirical pairing of two actual
nodes differs from its population counterpart by at most

\[
 t+C(B+1)e_j+e_j^2,
 \tag{10}
\]

using Cauchy--Schwarz and the analogous reference empirical RMS bounds.
Consequently all actual Gram perturbations have operator norm at most
`C N(B+1)(e_j+t)` while `e_j<=1`. Stop this induction if that quantity first
exceeds `gamma/2`. Below the stop,

\[
 \|G_n^{-1}\|\le2/\gamma,\qquad
 \|G_n^{-1}-G^{-1}\|
      \le 2\gamma^{-2}\|G_n-G\|.
 \tag{11}
\]

Apply (10)--(11) first to `alpha`, then to `h_perp`, then to `beta`. Expanding
each product gives, with a fixed sufficiently large numerical exponent,

\[
 |\alpha_n-\alpha|+|\beta_n-\beta|
       +|\sigma_n^2-\sigma^2|
 \le (C N B/\gamma)^C(e_j+t).
 \tag{12}
\]

For example, the alpha difference is
`(G_n^{-1}-G^{-1})s+G_n^{-1}(s_n-s)`, where the norms of `s,s_n` are bounded
by `C N(B+1)^2`; the h-perpendicular difference is the query difference
plus the two terms from subtracting `V_n alpha_n-V alpha`; the beta and
variance estimates repeat these two product subtractions. Every expression
involves a fixed number of such operations, which justifies a fixed
exponent in (12), independent of the number of instructions.

Since the **population** innovation satisfies `sigma>=epsilon`,

\[
 |\sigma_n-\sigma|
  =\frac{|\sigma_n^2-\sigma^2|}{\sigma_n+\sigma}
  \le\epsilon^{-1}|\sigma_n^2-\sigma^2|.
 \tag{13}
\]

No lower bound on `sigma_n` is needed for this inequality. The exact finite
conditional answer is

\[
 Y_n\alpha_n+U_n\beta_n+\sigma_n P_{U_n^\perp}g.
\]

Subtract (7) coordinatewise, use the removed-noise event, and apply
(12)--(13). Coordinate and linear instructions obey the easier Lipschitz
bound. Thus every instruction obeys

\[
 e_{j+1}\le A(e_j+t),\qquad
 A=(C N B/(\gamma\epsilon))^C\le e^{C N^3}.
 \tag{14}
\]

Starting from zero root discrepancy,

\[
 e_N\le (2A)^{N+1}t\le e^{C N^4}n^{-1/4}.
 \tag{15}
\]

When `log n >= C N^5`, the right side is smaller than
`gamma/[4 C N(B+1)]`. Hence the stopped induction never stops. This proves
the coupling estimate and its stated probability, with the larger common
exponent `C N^5` absorbing all auxiliary factors.

For a tail norm the map `v -> (|v|-M)_+` is 1-Lipschitz, so replacing the
actual array by its iid reference costs at most `e_N`. Replacing the iid
squared norm by its expectation costs at most `sqrt(t)` in norm, because
`|sqrt(a)-sqrt(b)|<=sqrt(|a-b|)`. For a pairing, Cauchy--Schwarz costs
`C(B+1)e_N+e_N^2+t`. This establishes the additional test assertions in
(2). Expectations may then be compared with the **original** population
program using (1) and the original and modified RMS bounds.

## 6. How this produces an all-time width rate

This paragraph records the transfer budget; the supervisor owns the final
all-time reconstruction. It is not used to prove the finite-program lemma.

Let `K=floor((log(e^e+n))^(1/128))`. Use a population Euler program with

\[
 T=a\sqrt{\log K},\qquad
 h=T/K,\qquad R=A\sqrt{\log K}.
 \tag{16}
\]

Here `R` is the comparison cutoff, distinct from the much larger program
clipping cutoff `N`. Take `N<=C K^3`; this allows at most `K`
passive probes and all elementary memory summands. In particular
`N^5<=C(log n)^(15/128)`, so (2) and all required tail tests have polynomially
small width error and polynomially small failure probability.

Quantitative proxy consistency follows from the exact braces in the paper's
dense-carrier-transfer proof: empirical pairings are now controlled by (2),
the changed population expectations by (1), fresh query noise by
`K_0 epsilon ||chi||_n`, and clipped-gate omissions by the tail tests.
Fixed-depth recomputation against the proxy nodes uses the same one-reference
cutoff inequality as the paper. Thus its compact-time comparison can be
made explicit in the form

\[
 E_{n,T}\le C T e^{C(1+R)T}
       [(1+R)(h+\xi_n)+e^{-cR^2}],
 \qquad \xi_n\le n^{-1/16}+C e^{-cN^2}.
 \tag{17}
\]

Choose `A` first so `c A^2>2`, then choose `a>0` so the coefficient of
`log K` in `C R T` is below `1/8`. The factors `T`, `1+R`, and `exp(C T)`
are `K^{o(1)}`. Therefore (17) is at most `C K^{-1/2}` for all sufficiently
large `n`. Population Euler error has the same bound without `xi_n`.

For all integer carrier cutoffs up to `N`, include the tail tests with
half-integer thresholds in the program event. Between mesh nodes, use the
parameter-speed bound and the one-reference cutoff inequality. The
1-Lipschitz positive-part tail then gives, uniformly on `[0,T]`,

\[
 H_n(M,t)\le C e^{-cM^2}+C K^{-c_0}.
\]

For `M>N`, monotonicity controls the tail by the result at `N`; the Gaussian
tail at `N` is absorbed into the error. Integrate against `rho_D` using
bounded total activity. The remaining activity after `T` is at most
`C e^{-kappa T}`. Thus the natural candidate conclusion is

\[
 a_n\le C\exp[-c\sqrt{\log\log(e^e+n)}]
 \quad\text{with probability at least }1-Cn^{-c'}.
 \tag{18}
\]

The exact paper definition `b_n=C Phi(a_n)`, where
`Phi(u)=u exp(K sqrt(log(e+1/u)))`, preserves this rate after decreasing `c`:
the positive correction in `log Phi(a_n)` has size
`O((log log n)^(1/4))`, smaller than the negative square-root term.

For fixed bounded input sets a net of mesh `K^{-c_d}` has polynomially many
points. Apply separate single-probe programs and a union bound over that net;
its full set of instructions need not fit in one `N<=C K^3` program. For a general finite-second-moment law, the
supervisor's normalized single-probe argument permits Fubini and Markov with
constants uniform in the probe. This avoids imposing a quantitative tail
condition on the test law. The precise probability/exponent loss in this
last step belongs in the final transfer proof, not in the fixed-program
lemma itself.

## Checks and remaining audit items

- Zero carriers and exact repeated queries cause no singularity after the
  fresh input noise. Both orientations are regularized; no inverse of an
  original singular Gram is taken.
- Fresh query noise supplies an innovation floor even when its unperturbed
  query lies exactly in the previous span. This floor is used in (13).
- The Gaussian removed projection can be dependent on the computation;
  its conditional rank bound is all the proof uses.
- Original and modified population programs are compared using the same
  initialized operator and its true adjoint, not independently sampled
  forward and reverse operators.
- Coordinatewise iid scalar arrays are a coupling target, not a claim that
  trained finite network coordinates are independent.
- `N` grows with width, but every constant in the finite induction has an
  explicit bound in `N`; the paper's qualitative convergence theorem is
  used only to identify fixed-program scalar laws and common operators.
- The program contains causal population coefficients as a proof proxy.
  It is not asserted to be the proposed autonomous closure or a numerical
  algorithm.
- The candidate claims an explicit slow shape, not a polynomial width rate.
  Its huge thresholds and constants are unsuitable for numerical accuracy
  budgets without substantial sharpening.
- The main independent-audit targets are the conditional regression coupling
  with reused matrices, the finite-program elementary instruction count,
  and the uniform proxy-consistency estimate (17). The full claim should
  remain labelled candidate until these are reconstructed independently.
