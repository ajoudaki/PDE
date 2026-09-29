# Direct closure: a quantitative initialized-branch result and its limit

28 September 2026. Scoped continuation of the direct finite-order closure
width proof. Inputs are `DIRECT_CLOSURE_WIDTH_ROUTE.md`,
`ACTIVATION_NEAR_QUADRATIC_ALLTIME.md`, the same-study
`WIDTH_RATE_CAUSAL_COUPLING_R2.md`, and the already-read complete Reeves
Gaussian-coupling paper in the study's generated source directory. No new
literature search, experiment, other study, agent, or maintained-book edit
was used.

**Status.** There is a quantitative, same-matrix joint coupling for a
precisely specified finite-step, capped, Gaussian-regularized
**population-oracle program**. Its normalized error is root width, with an
explicit dependence on the number of Gaussian queries and the
regularization. The local moment energy removes order dependence from
the oracle source Lipschitz estimate. This is not a theorem about the
uncapped continuous-time closure. In particular, quantitative removal of
the cap and control of coupled source velocities are not proved here.

## 1. The distinction between a finite local state and a finite program

Use the orthonormal moment coordinates of
`DIRECT_CLOSURE_WIDTH_ROUTE.md`. For each feature/backward source the
moment vector satisfies

\[
 \frac{da}{d\tau}=\frac{u}{\sqrt\tau}v-\frac{A}{\tau}a,
 \qquad A+A^T=uu^T,
\]
\[
 \frac d{d\tau}\|a\|^2
 =\|v\|^2-\left\|v-\frac{u^Ta}{\sqrt\tau}\right\|^2.
 \tag{1}
\]

All norms on moment indices are Euclidean norms of the entire moment
vector, rather than sums of coordinatewise bounds. In particular,

\[
 \|a(\tau)-\widetilde a(\tau)\|^2
 \le \|a(1)-\widetilde a(1)\|^2
       +\int_1^\tau\|v-\widetilde v\|^2ds
 \tag{2}
\]

when the clocks agree. The estimate holds at every order `q`.

The initialized actions in the exact closure remain
`W_{ell,0} h_{ell-1,a}(t)` and
`W_{ell,0}^T delta_{ell,a}(t)`. They are continuously many adaptive
queries even when `q=1`. The theorem below instead concerns a specified
finite program with `P` matrix calls. It does not identify `P` with `q`,
the number of moment coordinates, or the number of Picard passes.

## 2. A bounded finite-step oracle program

Fix a deterministic mesh and a finite activity budget `S`, with
`1 <= tau <= 1+S`. A macro step consists of finitely many forward and
backward passes, followed by updates of the local state. There are

\[
 P\le d+C_{L,m}K
 \tag{3}
\]

matrix calls for `K` such steps. Additional fixed factors in the number
of passes only change `C_{L,m}`.

The following modifications define the program for this result.

1. Residuals, clocks, and learned scalar/vector contractions are
   deterministic **oracle coefficients**. They may be prescribed, or
   generated causally from expectations in the matched finite-step
   comparison process. In the latter case a macro step uses coefficients
   determined by completed preceding passes. This is an explicit causal
   discretization, not an implicit equation for the current step.
2. Scalar source fields and the finitely many non-moment local state
   coordinates are clipped at a level `M >= 1`. Each full local moment
   vector is projected onto its Euclidean ball of radius `M`. The
   deterministic contraction vectors are bounded by `C M^2` in their
   complete moment norm. No coordinatewise moment cutoff is used.
3. Moment transport on each clock interval is solved exactly with the
   held input. Equivalently, use its exact homogeneous propagator and
   input integral, then the radial projection. This avoids the unstable
   order dependence of an explicit Euler step for `A`.
4. Each non-root initialized matrix call receives an additional
   independent Gaussian observation of variance `delta^2`, where
   `0 < delta <= 1`. The same original initialized matrix is still used
   at every one of its forward and transpose calls.

The finite population recursion in item 1 is well defined: before each
new call the source map and all required oracle coefficients have
already been specified, so its Gaussian covariance and response mean
are computed from the preceding comparison law. Caps make all its
moments finite. It is a particular capped finite-step population
program; its identification with any continuous-time limiting law is
not being asserted.

### 2.1 Order-uniform Lipschitz bound with frozen oracle coefficients

Let `U_<t` denote arbitrary previous external answers to the matrix
calls. With the oracle coefficients frozen, the source for call `t` is
a deterministic map `f_t(U_<t)`. Apart from the matrix action itself,
the only operations needed to construct it are fixed-depth local
forward/backward algebra, integration of the first-layer/readout state,
the moment filter, and clipping/projection.

The learned action on a neuron is an inner product between its moment
vector and a deterministic contraction vector. Its Lipschitz constant
on the indicated balls is bounded by a polynomial in `M`, without a
factor `q`. All scalar products, multiplication operations, activation
evaluations and gate evaluations in a single pass have Lipschitz
constants bounded by another fixed polynomial in `M`; the depth and
the number of data points are fixed. The gate is Lipschitz by the
stated `C^{1,1}` assumption. No third activation derivative is used.

For completeness, radial projections do not spoil (2). On a clock
interval use (2) for the two exact filter evolutions; at its right
endpoint apply the nonexpansiveness of projection to the two terminal
states. Iterating gives the same integrated difference inequality.
The first-layer/readout integrals satisfy the analogous inequality by
Cauchy--Schwarz, with total measure at most `S`. Combining these facts
with the local algebra yields, for the squared local-state difference,

\[
 E(s)^2\le C E(0)^2+
 C_M\int_0^s\bigl(E(v)^2+|\Delta U(v)|^2\bigr)dv.
 \tag{4}
\]

Here `U(v)` is the held transcript on each interval; current-step
algebraic queries also contribute their current finite list of answer
differences. The constant `C_M <= C(1+M)^p` has a fixed exponent
depending only on the architecture and activation constants. Gronwall
and (2) prove

\[
 \operatorname{Lip}(f_t)\le L_M,
 \qquad
 L_M=C(1+M)^p\exp\{C(1+M)^p S\}.
 \tag{5}
\]

This is a bound in the Euclidean norm of the stacked external
transcript, after the matrix embedding below. The held-input squared
integral is bounded by `S` times that stacked squared norm; this changes
only the fixed constants. In particular (5) is independent of `q`,
`K`, and `n`. Initial constant-prefix moments occupy only the zeroth
coordinate and satisfy the same bound.

The qualification "frozen oracle coefficients" matters. For the actual
empirical closure, those coefficients and its clock are functions of
all neurons. This section alone does not give (5) for that map or prove
its comparison with the oracle program.

## 3. Exact same-matrix embedding and a nonsingular query covariance

Let

\[
 N=Ln+d+P
\]

and take one `N` by `N` GOE matrix `A`: its off-diagonal entries have
variance `1/N`, its diagonal entries variance `2/N`, and its upper
triangular entries are independent. Partition its coordinates into
`L` physical neuron blocks of size `n`, `d` root coordinates, and `P`
auxiliary coordinates. For adjacent physical blocks set

\[
 W_{\ell,0}=\sqrt{N/n}\,A_{\ell,\ell-1}.
 \tag{6}
\]

These are independent canonical matrices with entries `N(0,1/n)`.
Their transpose calls use the same off-diagonal blocks. The first-layer
Gaussian roots are obtained from

\[
 W_{1,ij}=\sqrt N A_{(1,i),\mathrm{root}(j)}.
 \tag{7}
\]

They are iid `N(0,1)` and independent of the hidden initialized blocks.
All unused GOE entries may be ignored by the local program.

A hidden call with source `v_t` on physical block `b_t` has padded
source

\[
 f_t=\sqrt{N/n}\,\iota_{b_t}v_t
        +\delta\sqrt N\,e_{\mathrm{aux}(t)}.
 \tag{8}
\]

Its answer is `x_t=A f_t`; only the requested physical output block is
passed to the local computation. A root query has source
`sqrt(N) e_root(j)`. The physical part of (8) is exactly the original
forward or transpose action, and its auxiliary part is exactly an
independent Gaussian noise vector of variance `delta^2`. Distinct calls
use distinct auxiliary coordinates. The original matrix blocks in
(6)--(7) have not been resampled or conditioned on adaptive histories.

Although each fresh noise vector affects future sources, its column
was independent of all previously used physical output entries before
its own call. Auxiliary outputs are never fed to the local program.
Thus this is also the usual operational construction with fresh
independent observation noise at each call.

Let `Y` be the matched state-evolution process for these deterministic
source maps, and let

\[
 \Sigma_{st}=\frac1N\mathbb E\langle f_s(Y_{<s}),f_t(Y_{<t})\rangle.
 \tag{9}
\]

Unique auxiliary coordinates in (8) give, exactly,

\[
 \Sigma\succeq\delta^2 I_P.
 \tag{10}
\]

Indeed its non-root block is a positive semidefinite physical-source
Gram matrix plus `delta^2 I`; the root block is the identity and is
orthogonal to all non-root sources. The argument is algebraic and
does not need the adaptive physical histories to be linearly
independent.

Clipping gives a deterministic bound

\[
 \|f_t\|\le B_M\sqrt N,
 \quad B_M=C(1+M),
 \quad \lambda_{\max}(\Sigma)\le P B_M^2,
 \quad \kappa(\Sigma)\le P B_M^2/\delta^2.
 \tag{11}
\]

Assume `n >= d+P` so that `N/n <= L+2`; this also makes all embeddings
in (5) uniformly bounded. Source roots and auxiliary coordinates
can be padded with unused coordinates if necessary.

The joint law of all initialized blocks and all their reused actions
is preserved by this construction. Independence of distinct forward
and backward matrices has not been introduced.

## 4. Quantitative coupling of the finite oracle program

Write the padded finite program as

\[
 x_t=A f_t(x_{<t}),\qquad
 y_t=m_t(y_{<t})+w_t,
 \quad \operatorname{Cov}(w_s,w_t)=\Sigma_{st}I_N.
 \tag{12}
\]

Use the matched response mean from Definition 1 of the Reeves paper.
It has the form `m_t=sum_{s<t} b_{st} f_s`. Thus this comparison retains
the response from matrix reuse; it does not replace it by a centered
independent Gaussian action.

A bound on the response coefficients follows directly from that
definition. Every entry of

\[
 h_r=N^{-1}\mathbb E\langle w_r,f_t\rangle
\]

has absolute value at most `B_M^2`, by Cauchy--Schwarz and (11).
Every relevant inverse covariance has operator norm at most
`delta^{-2}`. The full or restricted row contraction appearing in the
definition therefore gives

\[
 |b_{st}|\le \sqrt P B_M^2\delta^{-2},
 \qquad
 \operatorname{Lip}(m_t)\le
 \Lambda_m:=P^2 B_M^2 L_M\delta^{-2}.
 \tag{13}
\]

The slightly looser power `P^2` avoids any need to optimize the
triangular indexing of the regression formula. In particular this
bound does not require differentiating the activation gate.

Let `Sigma=Omega^T Omega` be its Cholesky decomposition. Each column
of `Omega` has norm at most `B_M`, so

\[
 \|\Omega\|_{2,1}\le P B_M.
 \tag{14}
\]

All hypotheses of Reeves Theorem 5 now hold: deterministic Lipschitz
source maps, zero `g_t`, Lipschitz matched means, positive definite
matched covariance, and `P <= N`. Its two mismatch terms vanish by
the matched state-evolution construction. Consequently there exists
a coupling of the complete finite transcripts with

\[
 \frac{\|X-Y\|_F}{\sqrt n}
 \le \frac{C(1+4L_M)^{P-1}}{\sqrt n}
      \mathcal L^3(\sqrt P+\sqrt r)P B_M
 \tag{15}
\]

with probability at least `1-5 exp(-r)`, for `0 <= r <= N`, where

\[
 \mathcal L=\log_2(2P)+
  \sqrt P\,(L_M+\Lambda_m)(1+\Lambda_m)^{P-1}
       \frac{\sqrt P B_M}{\delta}.
 \tag{16}
\]

In (16) the actual condition number was replaced by its upper bound;
doing so only enlarges the estimate. One convenient coarser form is

\[
 \boxed{\quad
 \frac{\|X-Y\|_F}{\sqrt n}
 \le \frac{C P B_M(\sqrt P+\sqrt r)}{\sqrt n}
 \exp\!\left\{C P\log\left[
  2+\frac{P^2B_M^2(1+L_M)}{\delta^2}\right]\right\}.
 \quad}
 \tag{17}
\]

Constants here depend on the fixed architecture and activation
constants. This is an actual joint coupling statement for the program
defined in Section 2, not a statement conditional on an unverified
history Gram gap. In particular all physical forward/backward
transcript errors are bounded by the left side of (17).

For a target normalized error `epsilon` and failure probability
`5 exp(-r)`, a sufficient explicit width condition is

\[
 n\ge\max\{d+P,r\},
\]
\[
 n\ge C\epsilon^{-2}P^2B_M^2(P+r)
 \exp\!\left\{C P\log\left[
  2+\frac{P^2B_M^2(1+L_M)}{\delta^2}\right]\right\}.
 \tag{18}
\]

Local capped state/readout comparisons with the same deterministic
oracle coefficients follow by (4)--(5), at the cost of another factor
controlled by `L_M`. The finite-width oracle program itself continues
to use all original Gaussian matrices; its neurons were never assumed
independent. The row independence of the comparison process comes
from (12) and row-local deterministic source maps, after the oracle
coefficients have been fixed.

**Source use.** Equations (15)--(16) are the specialized bound in
Theorem 5 of the already-read local source
`data/generated/response_memory_width_uniform_20260927/quantitative_width_01/reeves_gaussian_coupling.txt`,
Definition 1 and Section 3.2. The embedding, regularizer, covariance
lower bound, and explicit substitutions (5), (11), (13), (14) are
supplied here. The reference theorem is used only in its finite-query
form.

## 5. What the suggested slow mesh achieves

For example, take fixed `0<a<1` and `b>0` and formally select

\[
 T_n\asymp\log\log n,\quad
 h_n=(\log n)^{-a},\quad
 P_n\asymp (\log n)^a\log\log n,
\]
\[
 M_n\asymp\sqrt{\log\log n},\qquad
 \delta_n=(\log n)^{-b}.
 \tag{19}
\]

The finite activity budget `S` remains fixed. Then

\[
 \log L_{M_n}=O((\log\log n)^{p/2}),
\]
\[
 P_n\log\left[
 2+P_n^2B_{M_n}^2(1+L_{M_n})/\delta_n^2\right]
 =o(\log n).
 \tag{20}
\]

Thus (17) is `n^{-1/2+o(1)}` for the **regularized finite oracle
programs** on this schedule, also for failure exponents `r=O(log n)`.
No factor `q` is present in this initialized-branch estimate. This
fact is useful even though it does not establish removal of the
approximations in (19).

In particular, (20) is not a rate for the continuous-time population
predictor or the empirical closure. Such a conclusion would need
quantitative bounds for all of the following: the empirical-to-oracle
feedback comparison, the mesh and observation-noise removal, the cap
removal, and the terminal-time tail. A bound in the current-query norm
also does not supply the source-velocity or total-variation estimate
needed by the all-time Gram-source resolvent.

## 6. The concrete cap-removal obstruction in the present proof

There is a Gaussian innovation in (12), with standard deviation at
most `B_M` per coordinate. That alone does not control the full
carrier `y_t=m_t(Y_<t)+w_t` at level `M`. For a physical coordinate,
(13) and the capped physical source bound give only

\[
 |m_{t,i}|\le C P^{3/2}B_M^3\delta^{-2}.
 \tag{21}
\]

This is much larger than `M` along (19). Moreover the variance upper
bound `B_M^2` itself grows with the cap. Gaussian innovation tails at
threshold `M` therefore do not imply that the cap activates rarely.
The full response is a nonlinear function of prior Gaussian slots;
repeatedly applying the finite-program Lipschitz estimate only gives
a concentration scale growing with `(1+Lambda_m)^P`, which also does
not close this removal argument.

Equation (21) is a limitation of the available estimate, not proof
that actual response means are large. A sharper first-chaos/response
energy estimate could improve it. To remove the caps one needs, for
example, a uniform direct-population bound on carrier tails and their
velocity-weighted tails, stable under this discretization and
regularization. Such a bound has not been derived from (1) here.
Moment energy controls second moments of stored histories. It does
not by itself control Gaussian tails of instantaneous nonlinear
response means.

The existing dense all-time bridge with a qualitative width remainder
cannot justify this missing statement: it concerns a different
training flow and gives no quantitative cap-exit probability for the
direct finite-order population program. Thus even an actual slow
logarithmic rate for the original closure cannot presently be
concluded by choosing (19).

## 7. Finite activity and Picard iteration do not yet remove the gap

For a Volterra equation with a bounded Lipschitz constant on activity
length `S`, the usual Picard error bound has a factorial denominator,
of the form `C(CS)^k/k!`. This suggests taking
`k` of order `log n / log log n`. The suggestion only helps the matrix
coupling if a whole Picard pass can be counted as a single query.

Reeves Theorem 5 does not do that. A pass evaluating
`W_0 h^{(k)}(t)` and `W_0^T delta^{(k)}(t)` for all `t` contains a
continuum of scalar-source columns. A discretized pass with `J`
sampling times contributes order `J` calls, so `k` passes contribute
order `kJ`, not `k`. Fixed `q` and finite local state do not change
this counting.

The static inverse-free history coupling and the inverse-free mean
response theorem in `WIDTH_RATE_CAUSAL_COUPLING_R2.md` do not supply
the missing Hilbert-valued adaptive block theorem: the former assumes
source histories independent of the reused matrix, and the latter
controls a conditional mean, rather than a joint innovation with all
previous histories. The positive scalar third-query theorem there
also does not establish arbitrary-depth continuum iteration.

Finite activity and stable local dynamics may allow a better theorem
in the actual observable-state metric than for arbitrary histories.
Nevertheless, projecting the past onto a nonlinear finite local state
does not preserve Gaussian conditional laws. A proof would still have
to construct a coupling preserving the original matrix marginal and
bound the joint innovation in that state metric. Neither a small
input-output Lipschitz constant nor the factorial Picard estimate
alone constructs that coupling.

## 8. Exact current claim level

The proved addition is (17)--(18) for the explicitly defined capped,
noisy, finite-step oracle program, including the order-uniform local
source bound (5) and exact preservation of all canonical initialized
matrix blocks and their transpose reuse. It supplies a concrete
initialized-branch estimate without an assumed finite-query Gram gap.

The missing step for the requested all-time direct closure theorem is
still a quantitative joint initialized-source comparison, together
with its velocity control, that survives cap/noise/mesh removal. The
finite learned contractions and order-uniform moment energy simplify
the feedback branch but do not prove that remaining statement. No
numerical width rate for the actual continuous-time closure, and no
`epsilon^{-5/2+o(1)}` moving-state corollary, is claimed by this note.
