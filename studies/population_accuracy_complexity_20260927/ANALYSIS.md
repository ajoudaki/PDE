# One target for width, memory order, and computational cost

Date: 2026-09-27. This is an analysis, not a modification of the paper or a new
training experiment. The full primary PDFs, including supplements, were
retrieved and converted to local text. See the source inventory below.

## 1. The common question

Fix the training inputs and labels, their averaging convention, input dimension
`d`, hidden depth `H >= 2`, tanh activations, the initialization law, and the
canonical feature-learning mobilities. Use the SAME initialization law at every
comparison, including the readout law. In particular, a vanishing readout and
an order-one stored readout do not generally give the same limiting training
kernel, even when both give initial predictions tending to zero.

Write the finite network as

\[
h_1=\tanh(W_1x/\sqrt d),\qquad
h_\ell=\tanh(W_\ell h_{\ell-1}),\qquad
f_n(x)=w^\top h_H/n.
\]

For mean squared training loss, the parameter mobility is
`D_n = diag(n I, I, ..., I, n I)`. There are `m` training samples.
The target is the prediction `f_infinity(t,x)` of the corresponding population
flow, on a horizon on which that flow exists. Existence for arbitrary depth and
arbitrary data on every finite horizon is itself stronger than the general
local population theorem in the maintained book. The comparison assumes the
specified target exists on the chosen interval; it does not change its scaling.

For a test probability measure `Q`, define

\[
E_Q(\widetilde f;T)
=\sup_{0\le t\le T}\|\widetilde f(t,\cdot)-f_\infty(t,\cdot)\|_{L^2(Q)}.
\tag{1}
\]

On the circle, `Q` is uniform angular measure. This is prediction RMSE relative
to the population predictor. For random approximations, a common statistical
criterion is `(E_initialization E_Q^2)^(1/2)`; high-probability versions can also
be used. A bound on the entire interval implies the corresponding bound at T.

For any label function `y_test` in `L^2(Q)`, the reverse triangle inequality gives

\[
\sup_{t\le T}|\operatorname{RMSE}_Q(\widetilde f(t),y_{test})
-\operatorname{RMSE}_Q(f_\infty(t),y_{test})|
\le E_Q(\widetilde f;T).
\tag{2}
\]

Thus the same approximation estimate controls the discrepancy in test RMSE.
It does not assert that the population predictor itself has small label error.
For MSE, at each time the difference is at most
`2 RMSE_Q(f_infinity,y_test) E_Q + E_Q^2`.

We count stored real numbers and ordinary dense arithmetic. Let `K=T/h` denote
the number of physical time-grid steps and `S` the number of Monte Carlo paths
in a limiting-process solver. `S` is not finite-network width `n`. For a solver
that iterates over the whole time grid, cost per step means total work divided
by K, explicitly identified as amortized. No method gets exact expectations,
initial higher kernels, matrix factorizations, or solver iterations for free.

## 2. The exact decomposition for response memory

Couple a response-memory closure to its width-n dense network through the SAME
initial arrays. Let

\[
a_T(n)=E_Q(f_n;T),\qquad
b_T(n,P)=\sup_{t\le T}\|\widehat f_{n,P}(t)-f_n(t)\|_{L^2(Q)}.
\]

Then, pathwise,

\[
E_Q(\widehat f_{n,P};T)\le a_T(n)+b_T(n,P).
\tag{3}
\]

This also holds after taking the square mean over initialization, by Minkowski.
There is no extra independent sampling error solely because the closure stores
more moments: comparison to the coupled dense network already accounts for its
width. Moment order controls a different approximation.

The current manuscript gives, for each fixed width and realized initialization,
and for all sufficiently large P,

\[
b_T^{old}(n,P)\le {A_T(n)\over\sqrt{P(P+1)}},\qquad
b_T^{joint}(n,P)\le {B_T(n)\over P(P+1)}.
\tag{4}
\]

Constants also depend on data, depth, initialization, and the test set or
distribution. The finite-width theorem's parameter norm is a product of
unnormalized Frobenius/Euclidean norms. Its proof does not establish constants
uniform in n. A square-mean bound additionally needs integrable random
constants; alternatively one can use their high-probability quantiles.

### Transfer from parameter error to the entire test function

For bounded operator and normalized vector norms, set

\[
d_n(\theta,\theta')=
{\|W_1-W_1'\|_F\over\sqrt n}
+\sum_{\ell=2}^H\|W_\ell-W_\ell'\|_{op}
+{\|w-w'\|_2\over\sqrt n}.
\]

Tanh is 1-Lipschitz and bounded by one. For inputs with `||x||/sqrt(d)<=X`,

\[
{\|h_1-h_1'\|_2\over\sqrt n}\le X{\|W_1-W_1'\|_F\over\sqrt n},
\]
\[
{\|h_\ell-h_\ell'\|_2\over\sqrt n}
\le \|W_\ell-W_\ell'\|_{op}
+\|W_\ell'\|_{op}{\|h_{\ell-1}-h_{\ell-1}'\|_2\over\sqrt n},
\]
\[
|f_n-f_n'|\le {\|w-w'\|_2\over\sqrt n}
+{\|w'\|_2\over\sqrt n}{\|h_H-h_H'\|_2\over\sqrt n}.
\tag{5}
\]

Induction gives `sup_x |f_n-f_n'| <= C_X d_n`. This controls the whole compact
input set, not just training inputs, and hence every supported Q. The original
fixed-width parameter bound implies (4), since operator norm is at most
Frobenius norm. A continuum test set need not be included in training.

### What the population-scale prediction would be

If (i) dense population fluctuations satisfy `a_T(n) <= C_T/sqrt(n)` in the
chosen probabilistic norm, and (ii) the closure estimates hold uniformly in n
in a population-normalized metric, then

\[
E_Q^{dense}\le C_T n^{-1/2},\quad
E_Q^{old}\le C_T(n^{-1/2}+P^{-1}),\quad
E_Q^{joint}\le C_T(n^{-1/2}+P^{-2}).
\tag{6}
\]

These are the useful leading-order comparison laws. They are conditional
population statements, not the current manuscript's unconditional theorem.
Constants for the three methods need not coincide. A larger joint-clock
constant can outweigh its better exponent at small P.

## 3. A sharper bound for the existing joint clock

The paper defines `Psi` by concatenating the forward histories and the
residual-normalized backward histories

\[
b_{\ell,a}=r_a\delta_{\ell,a}/\rho,
\qquad \rho=(m^{-1}\sum_a r_a^2)^{1/2},
\]

and uses `g = rho + ||dot(Psi)||_2`. For an ensemble of n order-one neuron
responses, that Euclidean norm normally grows like `sqrt(n)`, with m and H fixed.
Its clock length is therefore not naturally invariant under changing width.
Indeed its current accumulated-defect bound is

\[
{\Lambda_T^2(\Lambda_T-1)\over4nmP(P+1)}.
\tag{7}
\]

Even in the favorable situation `Lambda_T=O_T(sqrt(n))`, this particular bound
scales as `sqrt(n)/P^2`, before stability amplification. This is an avoidable
loss in that estimate, rather than a necessary penalty of the algorithm.

### Weighted approximation using actual history mass

Let `M_T=1+integral_0^T rho dt` be the inserted measure's total mass. Unlike
clock length, this quantity does not count the response-speed term. Set
`F(xi)=Psi(xi)/sqrt(nm)` on the clock interval, including its constant matching
prefix. The existing clock makes F Lipschitz with constant at most
`1/sqrt(nm)`.

For a Hilbert-valued L-Lipschitz function on `[0,tau]`, there is a polynomial
q of degree at most P-1 with

\[
\sup_{0\le\xi\le\tau}\|F(\xi)-q(\xi)\|\le C_J L\tau/P,
\tag{7a}
\]

where `C_J` is independent of the number of coordinates. For completeness,
write `G(theta)=F(tau(1+cos(theta))/2)`, an even periodic Lipschitz function
with Lipschitz constant at most `L tau/2`. Convolve it with the positive
normalized trigonometric polynomial

\[
J_N(\theta)=Z_N^{-1}
\left({\sin(N\theta/2)\over\sin(\theta/2)}\right)^4.
\]

Its degree is `2N-2`. The elementary bounds on the sine ratio give
`Z_N` between constant multiples of `N^3`, and
`integral |theta| J_N(theta) dtheta <= C/N`: split the integrals at `1/N`,
using the ratio bound `min(N,pi/|theta|)` and its lower bound `cN` near zero.
The convolution error is at most the Lipschitz constant times that first
moment. Evenness makes the result a polynomial in `cos(theta)`, hence in xi.
Choose `N=floor((P+1)/2)`; the degree is at most P-1 and `N>=P/2` for P>=2.
A constant polynomial covers P=1. The triangle inequality for the Hilbert norm
proves the same estimate for all coordinates together. This proves (7a).

The closure uses the best polynomial approximation in its weighted L2 norm,
so its error is no larger than this candidate's weighted error. Consequently,

\[
{1\over nm}\sum_{\ell,a}(D_h+D_b)
\le {C_J^2M_T\tau_T^2\over nmP^2},
\]
\[
\boxed{\int_0^T\sum_\ell\|E_\ell\|_Fdt
\le {C_J^2M_T\over P^2}
\left({M_T\over\sqrt{nm}}
+\int_0^T{\|\dot\Psi(t)\|_2\over\sqrt{nm}}dt\right)^2.}
\tag{7b}
\]

The second inequality uses the paper's exact projection-error/defect identity
and `tau_T=M_T+integral ||dot(Psi)|| dt`. There is now no spurious square-root
width factor. This bound applies to the ORIGINAL joint clock and algorithm.
It uses a comparison polynomial for the proof; it does not replace the
Legendre coordinates in the algorithm.

If normalized response total variation, history mass, and feedback stability
are bounded uniformly in n and P on the comparison tube, (7b) yields the
desired width-uniform P^-2 trajectory rate. These remain conditional
population estimates: the manuscript's compact-ball argument proves the
needed quantities finite at fixed n, not uniform as n grows.

### An optional RMS-clock variant

An alternative clock with a more transparent population interpretation is

\[
\boxed{g=\rho+
\left[{1\over nm}\sum_{\ell=2}^H\sum_{a=1}^m
(\|\dot h_{\ell-1,a}\|_2^2+\|\dot b_{\ell,a}\|_2^2)\right]^{1/2}.}
\tag{8}
\]

Depth could also be averaged; it is fixed here. This changes only the norm
used for the clock, not the weighted-moment construction, matching prefixes,
Gram matrix, or explicit physical-velocity cancellation. It is an implementable
variant, not a claim that the existing manuscript/code already uses this norm.

Here is the normalized projection calculation. With `lambda_P=P(P+1)`, let
`D_h,D_b` be the weighted history projection errors in the paper. The exact
defect identity implies

\[
\int_0^T\sum_\ell\|E_\ell\|_Fdt
\le {2\over nm}\sum_{\ell,a}\sqrt{D_hD_b}
\le {1\over nm}\sum_{\ell,a}(D_h+D_b).
\]

In clock (8), `Psi/sqrt(nm)` has speed at most one. The Legendre derivative
estimate, and the fact that the inserted measure is dominated by clock length,
therefore give

\[
{1\over nm}\sum_{\ell,a}(D_h+D_b)
\le {\tau_T^2(\tau_T-1)\over4\lambda_P}.
\tag{9}
\]

If the clock lengths and feedback stability constants are bounded uniformly
in n, this is the desired uniform `P^-2` defect and trajectory estimate.
This is a second way to remove a spurious dimension factor. Neither
normalization nor the sharper estimate (7b) alone proves uniform feedback
stability or response-variation control.

For the old clock the analogous normalized calculation needs only bounded
backward RMS and bounded forward-history derivative energy. In the identity
`2/(nm) sum sqrt(D_h D_b)`, both history energies scale proportionally to n,
which cancels the explicit `1/n`; forward projection supplies `1/P`.
Thus the projection mechanism itself is consistent with a width-independent
`1/P` bound. Stability remains a distinct obligation.

## 4. Dense width error and its interpretation

The expected finite-width expansion in a regular feature-learning regime is

\[
f_n=f_\infty+n^{-1/2}Z+n^{-1}\beta+\cdots.
\tag{10}
\]

It predicts order `n^-1/2` prediction RMSE, order `n^-1` squared prediction
discrepancy, and often order `n^-1` ensemble bias. The last two must not be
reported as an `n^-1` prediction-RMSE bound. Some observables can have a
vanishing leading fluctuation; this is a generic scale, not a universal lower
bound. Bordelon--Pehlevan's finite-width DMFT paper derives the fluctuation
covariance perturbatively and explicitly discusses the absence of a general
rigorous remainder theorem (2023 paper, main text and Appendix D).

The maintained book supplies qualitative finite-width convergence in probability
to its local nonlinear population flow, including passive probes, via a
fixed-coarse-mesh oracle and then a mesh limit. Its error term is `o_P(1)` at
fixed coarse mesh; it supplies no explicit power of n. Its special global
continuation results have narrower hypotheses. These are the author's
unpublished maintained results, not an external publication.

One cannot substitute either of the following without changing the model:

* Nguyen--Pham, Theorem 15 and Corollary 17, give quantitative deep mean-field
  approximations under their neuronal embedding and averaging parametrization.
  With comparable widths their general statement has a rate
  `n^-c1 sqrt(log n)` with an unspecified `c1 in (0,1/2)`, plus a step term.
  Their width-independent weight assumptions apply to internal `1/n` averaging;
  reproducing our `1/sqrt(n)` Gaussian operator would make those weights scale
  with `sqrt(n)` and lose those uniform assumptions.
* Agazzi--Mosig Garcia--Trevisan, Theorem 1.2, gives `n^-1/2` normalized Wasserstein
  rates for Lipschitz NETSOR Gaussian-process executions. Its program class and
  Gaussian execution do not supply a rate for our nonlinear, transposed,
  training-adapted muP response history. Its introduction explicitly separates
  the feature-learning setting from the setting it treats.

The 2025 Chen--Yang--Zhao--Gu paper analyzes feature nondegeneracy at infinite
width. Its convergence corollary concerns the error signal if the limit stops
changing; it is not a finite-width approximation-rate theorem.

### From pointwise width estimates to whole-space RMSE

If
`E sup_{t<=T}|f_n(t,x)-f_infinity(t,x)|^2 <= C_T(x)^2/n`
and `C_T` is square integrable under Q, then Tonelli and `sup integral <= integral
sup` give

\[
\mathbb E E_Q(f_n;T)^2\le {1\over n}\int C_T(x)^2dQ(x).
\tag{11}
\]

Thus passing to whole-circle RMSE does not take another square root or change
the width exponent. It requires bounds that cover test inputs, rather than a
training-loss-only theorem.

For compact-input uniform absolute error, a stronger uniform concentration
estimate can be combined with a spatial net. If the difference has Lipschitz
constant bounded by `C_T` and pointwise sub-Gaussian deviations, a net of mesh
`n^-1/2` in a fixed-dimensional compact domain gives a high-probability bound
of order `sqrt((d_input log n + log(1/delta))/n)`. On the circle the intrinsic
dimension is one. Without that concentration hypothesis, this rate does not
follow from a pointwise second-moment bound alone.

Qualitative uniform convergence needs less. Tanh gives bounded normalized
readout norms on finite horizons; bounding internal operator norms successively
backward from the output, and then the first-layer norm, gives spatial
equicontinuity on bounded inputs. Finite-probe population convergence plus a
finite-net argument then gives whole-compact convergence on the interval
covered by that population theorem, without specifying its n-rate.

## 5. NTH on exactly the same dynamics

NTH is not frozen NTK. Its lowest truncation freezes the tangent kernel; higher
truncations evolve it and capture feature learning. The question is what
controls truncation when feature learning remains order one at infinite width.

### Exact matched hierarchy

For constant canonical mobility `D_n`, define

\[
K^{(2)}(x,z)=\nabla f(x)^\top D_n\nabla f(z),\qquad
K^{(r+1)}(x_1,\ldots,x_{r+1})
=\nabla K^{(r)}(x_1,\ldots,x_r)^\top D_n\nabla f(x_{r+1}).
\]

Direct differentiation of gradient flow gives

\[
\dot f(x)=-{2\over m}\sum_a r_aK^{(2)}(x,x_a),\qquad
\dot K^{(r)}=-{2\over m}\sum_a r_aK^{(r+1)}(\ldots,x_a).
\tag{12}
\]

This is an exact hierarchy for OUR network. Retain through order p and set
`dot(K_tilde^(p))=0`. NTK is `p=2` in the source's kernel-index convention.
We distinguish this tensor order p from history moment order P.

The direct implementation stores `sum_{r=2}^p m^r` initial/evolving tensor
entries and m predictions. Its top tensor is fixed. For `m>=2`, total state
including fixed coefficients is `O(m^p)`, and an RHS contraction costs `O(m^p)`.
For `m=1` the corresponding sums grow linearly in p instead. These are direct
implementation costs, not lower bounds against all possible tensor structure.

### A same-target truncation estimate (derived here)

Include a compact test set in the first argument, with remaining arguments
restricted to training inputs. Let `B_r` bound the absolute exact kernel
`K^(r)` on this set and on `[0,T]`. Let R bound both the true and truncated
training residuals in maximum norm on a stopped comparison interval. Both
hierarchies start from the same initial kernels. Write `e_f` for the maximum
prediction discrepancy and `e_r` for the corresponding kernel discrepancy.
From (12),

\[
e_p(t)\le 2RB_{p+1}t,
\]
\[
e_r(t)\le\int_0^t(2R e_{r+1}(s)+2B_{r+1}e_f(s))ds,
\quad 2\le r<p,
\]
\[
e_f(t)\le\int_0^t(2R e_2(s)+2B_2e_f(s))ds.
\]

Substitute the inequalities from the top down. The p-fold integral of the
top forcing contributes `B_(p+1)(2Rt)^p/p!`. Each feedback term contributes a
convolution with kernel `2 B_(k+2) (2R(t-s))^k/k!`, for `0<=k<=p-2`.
Bound those kernels by their values at T and use Gronwall:

\[
\boxed{\sup_{t\le T}e_f(t)
\le B_{p+1}{(2RT)^p\over p!}\exp(L_{p,T}T),\qquad
L_{p,T}=2\sum_{k=0}^{p-2}B_{k+2}{(2RT)^k\over k!}.}
\tag{13}
\]

To remove an assumed truncated-residual bound, choose R one larger than the
dense residual maximum and stop at error one. Whenever the RHS of (13) is
strictly below one, first exit cannot occur. The remaining finite tensor
variables are bounded by their triangular integral recurrences, so the
truncated ODE continues through T. This is a genuine finite-time conditional
bound. It does not assume that the kernel is frozen or that feature learning
is small in n. Its useful content depends on controlling `B_r` as r grows.

For example, suppose uniformly in width

\[
B_r\le M A^{r-2}(r-2)!\qquad(r\ge2).
\]

If `q_T=2RAT<1`, then `L_(p,T)<=2M/(1-q_T)` and (13) gives

\[
\sup_{t\le T}e_f(t)
\le {M\over A}\,{q_T^p\over p}\,
\exp\left({2MT\over1-q_T}\right).
\tag{14}
\]

Thus geometrically accurate NTH is possible in an analytic, sufficiently short
activity regime even with substantial feature learning. Tanh's analyticity
does not automatically make `q_T<1` on every desired horizon or make these
constants uniform in width. Larger intervals require additional analysis;
the frozen-top truncation alone supplies no such continuation of its order
convergence. If instead `B_r<=M A^(r-2)` for every r, factorial decay follows
on every finite horizon. These are sufficient alternatives, not assumptions
established for our trained tanh networks.

At width n the matched population error is therefore

\[
E_Q^{NTH}(n,p;T)\le a_T(n)+\varepsilon_{NTH}(n,p,T),
\tag{15}
\]

where (13) is an explicit candidate upper bound for the second term. With
population initialization one removes `a_T(n)` but must compute/approximate
the initial population kernels and control the resulting coefficient errors.

### What the published theorem actually supplies

Huang--Yau Theorem 2.6 uses width m and sample count n; reversing those letters
to our convention, its training RMS bound for even p has the scale

\[
{(1+T)T^{p-1}\over n^{p/2}}\min\{T,m/\lambda\},
\quad
T\le\min\left\{
{c\sqrt{\lambda n/m}\over(\log n)^C},
{n^{p/[2(p+1)]}\over(\log n)^{C'}}\right\}.
\tag{16}
\]

This is its standard/NTK-scaling finite-network truncation theorem, not a
population-RMSE theorem for canonical feature learning. Its proof uses small
higher kernels. Replacing the mobility in (12) changes their size. Assumption
2.2 also demands independence of small subsets of inputs, which fails for
three vectors in the two-dimensional circle setup. The hierarchy still makes
sense there. Equation (2.11) supplies passive-test equations but is not itself
a uniform whole-input-space error theorem. These are limits on transferring
the bound, not arguments that NTH cannot learn features.

### Getting a full fitted function from NTH

There is a useful direct alternative to evolving a mesh of test inputs. Put
`u_a(t)=-2 r_tilde_a(t)/m`. Define iterated residual integrals

\[
I_\varnothing=1,\qquad
\dot I_{a_1\cdots a_k}=u_{a_1}(t)I_{a_2\cdots a_k}(t),
\qquad I_{a_1\cdots a_k}(0)=0.
\]

Repeatedly integrate the triangular passive-test hierarchy. Exactly for the
order-p truncation,

\[
\widetilde f_p(T,x)=f_0(x)+
\sum_{k=1}^{p-1}\sum_{a_1,\ldots,a_k}
K_0^{(k+1)}(x,x_{a_1},\ldots,x_{a_k})
I_{a_1\cdots a_k}(T).
\tag{17}
\]

This can represent the entire test function with `O(m^(p-1))` additional
coefficients, using evaluable initial kernel functions. It avoids a spatial
mesh or replaying residual histories for each new query. It does not avoid
the exponentially many training-word coefficients or the cost of evaluating
the initial higher kernel functions. If these come from a finite initialization,
that original network or an equivalent representation must remain available for
previously unseen queries. Population initial kernels can instead be computed
analytically or numerically when feasible. Their setup cost is separate and
can be substantial. This gives NTH its strongest fair function-prediction
interpretation without pretending it reconstructs the trained weights.

## 6. Runnable TP and DMFT descriptions

TP IV supplies a limiting stochastic process for canonical feature learning.
It is not, by itself, a low-cost numerical solver: its Algorithm 1 asks for
expectations of recursively defined nonlinear random variables. Section 8
discusses the growth of exact symbolic computation. Nonlinear Gaussian
expectations must actually be integrated or sampled.

Bordelon--Pehlevan's 2022 DMFT gives an implementation of the same limiting
process after matching scalings and initial conditions. This is a fair numerical
backend for both descriptions. The comparison should not artificially charge
TP for exponential symbolic expansion if we allow DMFT to sample equivalent
expectations. Conversely, exact TP convergence does not certify a numerical
sampling solver's accuracy.

The parameter mapping is explicit. In their notation take `gamma=sqrt(n)` and
set our internal `W_l=U_l/sqrt(n)` for their variance-one matrices U; leave the
input matrix and readout coordinates unchanged. Their output then becomes
`w^T h/n`. Their mobility n on U induces mobility one on W, while the input
and readout mobilities remain n. This is precisely our canonical flow (with
the same loss-averaging convention). The readout initialization variance must
still be matched, including a zero/vanishing readout if that is the chosen
study setup. Matching initial predictions alone would not suffice.

Appendix B, Algorithm 1, can be implemented as follows:

1. On K times and m samples, keep forward/backward covariances and response
   matrices, each indexed by pairs `(sample,time)`.
2. Given those matrices, integrate the training-prediction equation.
3. Factor Gaussian covariance matrices and draw S representative noise paths.
4. Solve each path's causal forward/backward Volterra equations and their
   Jacobian response equations.
5. Average the required products and derivatives, update the kernels, and
   iterate to the requested numerical tolerance.

Let `q=mK` and I be the number of full-grid sweeps. The published table gives
kernel memory `O(H q^2)` and total work `O(H q^3)`, suppressing sampling count
and iteration count. For an ordinary dense implementation of Algorithm 1,
factorization costs `O(q^3)` per layer; each sampled path and covariance outer
product costs `O(q^2)`; full samplewise response Jacobians can be obtained by
dense causal triangular solves in `O(q^3)` per path. A conservative explicit
bound, restoring numerical accuracy resources, is

\[
\text{work over }[0,T]=O(IH(S+1)m^3K^3).
\tag{18}
\]

It is attainable with peak memory `O(Hm^2K^2)` by processing full paths and
their Jacobians one at a time and accumulating averages. Batching S paths can
increase workspace to `O(Sm^2K^2)` for explicit Jacobians. Kernel storage alone
already grows quadratically with the time grid. Amortized work per physical
step is `O(IH(S+1)m^3K^2)` for this implementation. These are arithmetic counts
for a specified implementation, not lower bounds. A more efficient response
estimator can improve the S-dependence, but must have its own variance and
conditioning analysis; it is not justified by treating derivatives as free.

The practical expected accuracy model for a stable consistent solver is

\[
E_Q^{TP/DMFT}\lesssim C_T
\left(S^{-1/2}+h^r+\text{solver tolerance}\right),
\tag{19}
\]

where r is the time-integration/quadrature order. Unlike finite-network width
sampling, S samples the limiting process itself. The S term also covers
Monte Carlo estimation of outputs. The constant must cover stability of
feedback, response estimation, and covariance operations. Uniform control as
K grows is an assumption here, not a consequence of a fixed-grid CLT.

One precise sufficient route is a contraction estimate for the discretized
self-consistency map `F_h` in the norm controlling the desired outputs.
If it has constant kappa<1, its sampling approximation has uniform error zeta,
and the computed solution has residual at most eta, then

\[
\|q_{computed}-q_h\|\le{\zeta+\eta\over1-\kappa}.
\tag{20}
\]

Proof: insert `F_h(q_computed)` and the sampled map into the difference from
the fixed point; move `kappa ||q_computed-q_h||` to the left. Add a consistent
time error and the Lipschitz output map to obtain (19) when `zeta=O(S^-1/2)`.
Local invertibility/stability can replace contraction. The cited TP/DMFT
papers do not provide this general solver error theorem on arbitrary compact
horizons for the present model.

The DMFT forward-prediction equation applies to passive test points. Numerical
evaluation needs the corresponding cross-covariances and test paths. There is
no universal constant-cost full-input function evaluator hidden in the
training-only kernel table. Equation (19) in `L^2(Q)` requires sampling and
stability estimates for those test observables as well.

## 7. The comparison in common computational units

The table counts training dynamics; input-layer `O(nd)` storage and `O(mnd)`
work are displayed here as common extra terms. `H` is fixed but retained to
show dependence. Activations require `O(Hmn)` workspace for dense/population
implementations. The closure retains W0 as a dense array.

| Implementation | Total resident state, up to constants | Work per RHS/grid step |
|---|---|---|
| Dense canonical width n | `H n^2 + Hmn + nd` | `Hmn^2 + mnd` |
| Old response memory | `H n^2 + HmnP + nd` | `Hmn^2 + Hm^2nP + HmnP + mnd` |
| Joint response memory | `H n^2 + HmnP + P^2 + nd` | old cost plus `HmnP^2 + P^3` |
| Direct NTH, order p | `sum_(r=2)^p m^r` fixed/evolving tensor entries, plus initialization/evaluator resources | `sum_(r=2)^p m^r` contractions, after initialization |
| Sampled TP/DMFT, streamed full-grid solver | `H m^2 K^2` kernels and streaming workspace | amortized `I H(S+1)m^3K^2` |

New-clock Gram solves apply to all `Hmn` history rows; factoring the shared
P-by-P Gram costs `P^3`. The clock's directional response differentiation
requires a constant number of forward/backward linearized passes. Fixed-depth
factors from those passes are included. Old triangular moment updates can use
prefix sums, hence linear rather than quadratic cost in P.

For the closures, the moving internal-layer state is `2(H-1)mnP`, compared to
`(H-1)n^2` trainable dense entries. That is a real reduction when `2mP<n`.
Total stored state nevertheless retains `W0`, and total per-step work retains
its dense forward and transpose actions. This implementation has not removed
the `n^2` term. Replacing W0 by a seed can trade storage for regeneration but
does not provide a fast Gaussian matrix multiplication; it is a different
implementation whose work must be counted.

An arbitrary test query after training costs `O(Hn^2+nd)` for dense training and
`O(H(n^2+nmP)+nd)` for a closure using its stored factors. NTH can use (17);
the number of coefficient terms is `O(m^(p-1))`, multiplied by the cost of
evaluating their initial mixed kernels. DMFT uses passive-path computations.
A numerical estimate of whole-circle RMSE adds quadrature/test-query error and
work for every method. This is separate from the analytical norm (1).

### Error versus memory under the expected square-root-width law

Assume the stable population-scale laws (6), with fixed m,H,d,T, and ignore
constants to compare powers. To achieve prediction RMSE epsilon,

| Method | Width/order allocation | Moving learned/history state | Total state retaining dense W0 | Per-step arithmetic |
|---|---|---|---|---|
| Dense | `n ~ epsilon^-2` | `epsilon^-4` | `epsilon^-4` | `epsilon^-4` |
| Old clock | `n ~ epsilon^-2`, `P ~ epsilon^-1` | `epsilon^-3` | `epsilon^-4` | `epsilon^-4` leading |
| Joint clock under the sharper normalized-variation bound | `n ~ epsilon^-2`, `P ~ epsilon^-1/2` | `epsilon^-5/2` | `epsilon^-4` | `epsilon^-4` leading |

Thus there is a meaningful moving-state trade-off without an improved leading
total-memory or total-arithmetic exponent in the present dense-W0 implementation.
Equivalently, balance sampling and order errors at `P~sqrt(n)` for the old clock
and `P~n^(1/4)` for the joint clock. Constants can make useful orders
much smaller in practice. These allocations are theoretical comparison laws,
not fits to the circle experiments or unconditional population guarantees.

Under the favorable NTH analytic regime (14), write its bound as `C_T q_T^p`
with `q_T<1`. Then `p~log(1/epsilon)/log(1/q_T)`, but the tensor cost is

\[
m^p\asymp\epsilon^{-\log m/\log(1/q_T)}.
\tag{21}
\]

Its efficiency depends strongly on m and on activity/analytic radius. It can
be attractive for a few samples and small q_T; there is no established q_T<1
for all desired rich-training horizons. The published `n^-p/2` theorem cannot
be used to replace q_T in this same-model table.

For the explicit streamed DMFT solver, assume (19) with Euler accuracy and
bounded I. Choosing `S~epsilon^-2`, `K~epsilon^-1` gives kernel memory
`O(Hm^2 epsilon^-2)` and the conservative Jacobian-based implementation's
amortized step work `O(IHm^3 epsilon^-4)`. Total work is `O(epsilon^-5)` at
fixed m,H,I. This illustrates a possible total-memory advantage for a solver
that analytically eliminates W0, at the cost of a growing time-history state.
It is a conditional numerical scaling, not a proven performance ranking.
Higher-order integration changes K's exponent; the same integration order
must be offered to dense and closure systems. All methods additionally need
a stable step size. Moment stiffness and Gram conditioning can make the
required number of steps depend on P; per-step counts alone do not certify
equal wall-clock cost at equal error.

## 8. What is firm and what the big picture predicts

The strongest current exact identity is (3): response memory inherits the
dense width error and adds its independently controlled temporal compression
error. The fixed-width rates are 1/P and 1/P^2. Ordinary population fluctuation
theory suggests adding 1/sqrt(n), but the present manuscript has not established
the width-uniform theorem needed to turn that outline into an unconditional
bound for the exact deep tanh model. The new estimate (7b) shows that the
existing joint clock's projection error is compatible with that comparison;
an RMS-normalized clock is another, optional implementation choice.

NTH legitimately learns features. Its matched version is (12), its same-target
conditional error certificate is (13), and it can describe a full fitted test
function through (17). Its central numerical obstacle is the growth of the
higher initial kernels and the number of sample-index tensors, not an absolute
inability to move features.

Numerical TP and DMFT should be compared as solvers for the same limiting
response process. They can eliminate explicit width and W0 storage, but must
pay for numerical expectations, two-time memory, and feedback stability. Their
sampler count is a different resource from finite-network width. Treating an
exact limit formula as a free exact solver would distort the comparison.

## Sources and verification scope

Full PDFs and layout-preserving extracted text are in
`data/generated/population_accuracy_complexity_20260927/full_texts/`; hashes
and retrieval URLs are in `sources.json`. All sources actually used above were
retrieved in full. A failed retrieval of a pi-limit paper is also recorded;
no conclusion here depends on that paper.

* Huang and Yau, *Dynamics of Deep Neural Networks and Neural Tangent
  Hierarchy*, 39 pages: https://arxiv.org/pdf/1909.08156 . Checked definitions,
  Assumptions 2.1--2.2, Theorem 2.6, passive-test equation (2.11), and its full
  Appendix C proof. The same-mobility hierarchy, conditional bound (13), and
  representation (17) above are derivations in this analysis.
* Yang and Hu, *Feature Learning in Infinite-Width Neural Networks*, full
  65-page version: https://arxiv.org/pdf/2011.14522 . Checked parametrization,
  Algorithm 1, Master Theorem 7.4, and computational discussion in Section 8.
* Bordelon and Pehlevan, *Self-Consistent Dynamical Field Theory of Kernel
  Evolution in Wide Neural Networks*, full 55-page version:
  https://arxiv.org/pdf/2205.09653 . Checked model/scaling, stochastic equations,
  complexity table, Appendix B Algorithm 1, and variable-initialization scope.
* Bordelon and Pehlevan, *Dynamics of Finite Width Kernel and Prediction
  Fluctuations in Mean Field Neural Networks*, 44 pages:
  https://arxiv.org/pdf/2304.03408 . Checked the expansion, propagator covariance,
  Appendix D, and discussion of its perturbative status.
* Nguyen and Pham, *A Rigorous Framework for the Mean Field Limit of Multilayer
  Neural Networks*, 125 pages: https://arxiv.org/pdf/2001.11443 . Checked network
  normalization, embeddings, Theorem 15, Remark 16, and Corollary 17. Not imported
  as a theorem for the different Gaussian-operator model here.
* Agazzi, Mosig Garcia, and Trevisan, *Quantitative Gaussian-Process Limits of
  Tensor Programs*, 37 pages: https://arxiv.org/pdf/2607.06290 . Checked program
  operations, execution rules, Theorem 1.2, and stated GP/feature-learning scope.
* Chen, Yang, Zhao, and Gu, *Global Convergence and Rich Feature Learning in
  L-Layer Infinite-Width Neural Networks under muP Parametrization*, 28 pages:
  https://arxiv.org/pdf/2503.09565 . Checked Theorem 4.5 and Corollary 4.6;
  neither is a finite-width error estimate.

Local inputs at inspection:

* `paper/main.tex`, SHA-256
  `e3046b2f47a3b7434122848cecfbb09d14ef17c88829bccf223155b1065b9124`.
* `docs/03-local-population.qmd`, SHA-256
  `3a6fc52191f815189337309f70e3fb822663b1532eedc54e4dea9402c3fdaebd`.
* `docs/04-continuing-flows.qmd`, SHA-256
  `78728dbbcc551392f7dd6cf7b91bad42324e5b540655d4242e830e9c38774a43`.

The displayed algebraic deductions were checked directly against the relevant
recurrences. There was no independent review, numerical solver implementation,
new experiment, or claimed formal verification of an external paper's entire
proof dependency tree. The source-dependent and conditional statements above
are deliberately kept separate.
