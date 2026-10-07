# Robust posterior centers at every retained training prefix

2026-10-06. Conditional transfer theorem for a current-state decoder.
The result does not construct a posterior expectation evaluator, replace
the initialization, or authorize training replay during decoding.

A whole-trajectory dense concentration bound supplies a deterministic
proof center. If retained training prefixes form a nested information
sequence, one maximal inequality controls the posterior probability of a
bad training tape at every prefix. Uniform conditional control of fresh
passive-query noise then gives posterior medians close to the actual
dense reference at every admissible query and physical time. A jointly
realized query-noise process is unnecessary.

## 1. A deterministic center used only in the proof

Let $\mathcal Z$ index the desired outputs, including physical time,
sphere input and the fitted endpoint. For random initialization $G$, let
$f_G:\mathcal Z\to\mathbb R$ be the dense trajectory. All displayed
suprema and events are assumed measurable. An arbitrary measurable
extension may be used off the physical good event, with that complement
included in the failure probability.

Suppose independent dense copies satisfy

\[
 \Pr_{G,G'}\left\{\sup_{z\in\mathcal Z}
                     |f_G(z)-f_{G'}(z)|>b\right\}\le\eta.
 \tag{1}
\]

Put $q(g)=\Pr_{G'}(\|f_g-f_{G'}\|_*>b)$. Its expectation is at
most $\eta$, so some fixed $g_0$ satisfies $q(g_0)\le\eta$.
Otherwise $q>\eta$ almost surely would force its expectation above
$\eta$. Define the deterministic function $f_0=f_{g_0}$. Then

\[
 \Pr_G\{\|f_G-f_0\|_*\le b\}\ge1-\eta.
 \tag{2}
\]

The same $f_0$ is used for every time, query and prefix. It is an
existential witness, not a stored trajectory, decoder input, or computable
object required by the algorithm. If (1) comes from a good-pair event
that also bounds both trajectories by a fixed $B$, choose $g_0$ from
that event's nonzero conditional success set; then $\|f_0\|_*\le B$.
Alternatively, an actual-reference bound on the good event below bounds
$f_0$ by $B+b$ whenever that event has positive probability.

## 2. Training tape, retained prefixes and a common good event

Let $W$ denote the full training tape: dense initialization, all training
matrix noise, and all scalar smoothing noise used during training.
Take its probability space and all finite-dimensional summary spaces to
be standard Borel, so regular conditional distributions exist. The
initialization $G$ is a component of $W$.

Let $C_j=C_j(W)$ be the retained compressed history after prefix $j$,
$0\le j\le R$. Require

\[
 \mathcal F_j:=\sigma(C_j),\qquad
 \mathcal F_0\subseteq\mathcal F_1\subseteq\cdots
                    \subseteq\mathcal F_R.
 \tag{3}
\]

For example $C_j$ may contain all retained coefficients from prefixes
$0,\ldots,j$, with old entries recoverable from the current summary.
They still have to satisfy the intended compressed information count.
No future tape is supplied at runtime. A summary that discards old
information does not automatically satisfy (3); Section 6 gives an
explicit obstruction.

Let $A$ be one measurable event of complete training tapes on which:

- $\|f_G-f_0\|_*\le b$;
- the original physical good bounds and all required training-noise
  budgets hold;
- the noiseless passive predictor determined by the current trained state
  has the stipulated uniform error $\varepsilon_{\rm tr}$ from $f_G$,
  at each prefix's admissible times and inputs.

The last item is a fidelity certificate that must be proved for the
actual training program; small noise values alone do not imply it without
a stability argument. Suppose

\[
 p:=\Pr(A^c)\le\eta+\delta_{\rm tr},                 \tag{4}
\]

where $\delta_{\rm tr}$ accounts for any additional training failures.
The event may depend on the entire future training tape. It is used for
proof only and need not be recognizable from a current prefix.

Choose one regular posterior kernel $\pi_j(c,dw)$ for $W$ given $C_j$,
and define

\[
 q_j(c)=\pi_j(c,A^c),\qquad Q_j=q_j(C_j)
                          =\mathbb E[\mathbf1_{A^c}\mid\mathcal F_j].
 \tag{5}
\]

These nonnegative bounded random variables form a martingale. The finite
number of prefixes permits one common probability-one set on which all
posterior identities hold. The same kernels below define all query laws;
separate query-dependent versions of conditional expectation are not used.

## 3. Maximal posterior control, including the actual good event

For $0<\alpha<1$, there is an event of probability at least
$1-p/\alpha$ on which

\[
 A\text{ holds and }q_j(C_j)\le\alpha
                    \text{ for every }0\le j\le R.
 \tag{6}
\]

Here is a finite elementary proof that also avoids an unnecessary
additional $p$ failure term. Append one proof-only information step
$\mathcal F_{R+1}=\sigma(\mathcal F_R,A)$. Then
$Q_{R+1}=\mathbf1_{A^c}$ and $(Q_j)_{j=0}^{R+1}$ is still a
nonnegative martingale with expectation $p$. Let $\tau$ be the first
index at which $Q_j>\alpha$, if such an index exists. The events
$\{\tau=j\}$ are disjoint and belong to $\mathcal F_j$; therefore

\[
 \begin{aligned}
 \alpha\Pr\{\tau\text{ exists}\}
 &\le\sum_j\mathbb E[Q_j\mathbf1_{\{\tau=j\}}]\\
 &=\sum_j\mathbb E[Q_{R+1}\mathbf1_{\{\tau=j\}}]
 \le\mathbb E Q_{R+1}=p.
 \end{aligned}
 \tag{7}
\]

On the complementary event every actual prefix posterior is at most
$\alpha$, and $Q_{R+1}\le\alpha<1$ forces $A$ itself. This proves
(6). The appended step is only a proof device; the decoder is not given
$A$ or its truth value. It is equally possible to obtain the weaker
bound by applying the maximal inequality and then a union bound, but
(7) proves the sharper statement directly.

## 4. Uniform conditional query laws and posterior medians

For a prefix $j$, let $\mathcal Z_j$ be its admissible passive queries.
It may contain an entire physical-time patch and the whole input sphere.
The terminal prefix may include the frozen tail and infinity. These
domains must cover all outputs the claimed current-state decoder serves;
no ability to predict an uncomputed future state is inferred.

For each tape $w$, prefix $j$ and query $z\in\mathcal Z_j$, let
$K_j(w,z,dx)$ be the law of a real noisy passive-query output. Assume
these are measurable kernels and, on the same event $A$, satisfy

\[
 K_j\bigl(w,z,[f_G(z)-\varepsilon,f_G(z)+\varepsilon]\bigr)
      \ge1-\rho
 \quad\text{for every }w\in A,\ j,\ z\in\mathcal Z_j.
 \tag{8}
\]

Here $\varepsilon=\varepsilon_{\rm tr}+\varepsilon_{\rm qry}$
may separate training and query errors. The query randomness is fresh
conditional on the complete training tape. It need not be jointly sampled
over $z$. What is essential is that (8) is a uniform conditional bound
on a common set of tapes, not merely an unconditional bound for each
fixed query. Section 5 supplies a sufficient forward-only noise estimate.

The posterior law to be evaluated from the current summary is

\[
 \mu_{j,c,z}(D)=\int K_j(w,z,D)\,\pi_j(c,dw).
 \tag{9}
\]

No conditioning on the event $A$ occurs in this definition. Bad tapes
remain part of the posterior and their contribution is controlled by (5).
Since $\|f_G-f_0\|_*\le b$ on $A$, equations (8)–(9) give

\[
 \begin{aligned}
 \mu_{j,c,z}([f_0(z)-b-\varepsilon,f_0(z)+b+\varepsilon])
 &\ge(1-\rho)\pi_j(c,A)\\
 &\ge1-q_j(c)-\rho.
 \end{aligned}
 \tag{10}
\]

This inequality holds for all admissible queries using the same posterior
kernel and the pointwise-on-$A$ hypothesis (8). There is no union over
queries and no conditional event involving a jointly realized noisy
function.

Choose $\alpha+\rho<1/2$. On the event (6), every law in (9) has
strictly more than half its mass in the interval in (10). Every median
of that law therefore lies in that interval: below or above it one of
the two defining median half-probabilities would be at most
$\alpha+\rho<1/2$. For any fixed deterministic choice of median
$D_j(c,z)$, this proves simultaneously

\[
 \boxed{\quad
 \sup_{0\le j\le R}\ \sup_{z\in\mathcal Z_j}
      |D_j(C_j,z)-f_G(z)|\le2b+\varepsilon
 \quad}                                                       \tag{11}
\]

with probability at least $1-p/\alpha$. The second $b$ is the
distance of the actual reference to $f_0$ on $A$. At $\alpha=1/4$
and $\rho\le1/8$, the posterior mass is at least $5/8$, and the
success probability is at least $1-4p$.

If an admissible query domain depends measurably on the retained state,
the same proof applies to $z\in\mathcal Z_j(c)$: the posterior is
concentrated on tapes with that state, and (8) must hold for all such
admissible queries on $A$. A finite prefix schedule covering continuous
physical-time patches is enough for (11); no continuum-time martingale
theorem is required.

### Deterministic smooth-test implementation, conditional on an evaluator

Let $\psi$ be a nondecreasing smooth function with values in $[0,1]$,
equal to zero on $(-\infty,-1]$ and one on $[1,\infty)$. A posterior
expectation evaluator would return

\[
 H_{j,c,z}(s)=\int\psi((s-x)/\tau)\,\mu_{j,c,z}(dx)
 \tag{12}
\]

to deterministic error at most $\nu<1/2-\alpha-\rho$. Assume a
counted rational bracket $[-M,M]$ containing
$[f_0(z)-b-\varepsilon-\tau,f_0(z)+b+\varepsilon+\tau]$ for
every admissible query. Such an $M$ follows from a supplied physical
output bound; it is not a bound on bad-tape outputs.

Bisect at threshold value $1/2$, updating the lower endpoint when the
computed value is below $1/2$ and the upper endpoint otherwise. Stop at
bracket length at most $\delta$. The same bounded-test proof as in
`ROBUST_CENTER_TRANSFER.md` is short enough to repeat: the center mass
in (10) gives $H(s)\le\alpha+\rho$ below
$f_0(z)-b-\varepsilon-\tau$, and $H(s)\ge1-\alpha-\rho$
above its upper counterpart. Every bisection preserves
$H(l)\le1/2+\nu$ and $H(u)\ge1/2-\nu$. Thus $l$ is below
the upper counterpart and $u$ is above the lower one. Their final
midpoint has error at most $b+\varepsilon+\tau+\delta/2$ from
$f_0(z)$. Consequently the implemented version of (11) has error

\[
 2b+\varepsilon+\tau+\delta/2.                       \tag{13}
\]

Atoms and flat CDF regions cause no problem. For the fixed choices
$\alpha=1/4$, $\rho\le1/8$, one may take $\nu=1/16$.
The tests are bounded, so no moment of bad-tape outputs is needed.
The expectation is under the unconditional posterior (9), not a
good-event-conditioned or limiting-population substitute.

Given $C_j$, a deterministic repeatable evaluator and fixed bisection
rule define one consistent decoder function on all its queries. Its
extra workspace is only the bracket, counter and smoothing parameters,
as in the preceding robust-center note. A per-query randomized numerical
guarantee would not establish the simultaneous claim.

## 5. A sufficient forward-only conditional Gaussian-noise estimate

Here is a concrete way to verify the query part of (8), without a net.
Fix a complete training tape on its good event and a current parameter
state. Suppose its hidden matrix operator bounds are $B_\ell$, its
activation slopes are at most $s_\ell$, and its readout RMS is at most
$B_w$, uniformly over all prefixes and their admissible times. Let the
passive query computation add errors $e_\ell$ to its layer
preactivations and a scalar error $e_0$ to its final output. Assume

\[
 \mathbb E[\|e_\ell\|_{2,n}^2\mid W]\le\sigma_\ell^2,
 \qquad \mathbb E[|e_0|^2\mid W]\le\sigma_0^2,
 \tag{14}
\]

uniformly over queries. It suffices that these bounds hold conditional
also on earlier query noises. For an additive centered Gaussian vector
with covariance operator at most $\sigma_\ell^2 I_n$, (14) follows
from its trace divided by $n$. Independence across layers is not needed
for the bound below.

Subtract the noisy and noiseless forward passes. The first-layer feature
error is at most $s_1\|e_1\|_{2,n}$, and subsequent errors obey

\[
 d_\ell\le s_\ell(B_\ell d_{\ell-1}
                                      +\|e_\ell\|_{2,n}).
\]

Thus the output difference has absolute value at most
$\sum_{\ell=1}^L a_\ell\|e_\ell\|_{2,n}+|e_0|$, where

\[
 a_\ell=B_w s_\ell
                  \prod_{r=\ell+1}^L(s_r B_r).
\]

Minkowski's inequality in conditional $L^2$ and then Markov's inequality
give the width-independent bound

\[
 \Pr\{|g_{\rm noisy}-g_{\rm noiseless}|>
                 \varepsilon_{\rm qry}\mid W\}
 \le \frac{(\sum_{\ell=1}^L a_\ell\sigma_\ell+\sigma_0)^2}
              {\varepsilon_{\rm qry}^2}.
 \tag{15}
\]

All coefficients are deterministic good-event bounds independent of the
particular sphere input or time. Therefore (15) holds for every query
on the same set of training tapes. Combined with the uniform training
fidelity on $A$, it proves (8), with the right side of (15) at most
$\rho$. No query backpropagation or coordinate maximum is used.

This lemma applies only when the actual query law has been coupled to
that fixed trained forward pass with the stated additive errors.
An arbitrary Gaussian regression approximation does not acquire that
coupling from its name or covariance formula. Query-dependent coefficient
rounding or smoothing errors require their own forward perturbation
bounds; they are not automatically covered by (14).

### Standardized innovations need larger caps after fixing the full tape

A conditional-Gaussian innovation used by a row program is not generally
Gaussian after conditioning on the complete dense initialization and
training-noise tape. Only the fresh raw query noise has that law under
this stronger conditioning. The distinction is important when proving
that scalar caps preserve the query program.

Consider a raw initialized-matrix answer
$y=M_0v+\sigma\xi$, where $\|M_0\|_{\rm op}\le C$,
$\|v\|_{2,n}\le B$ and $\xi$ is a fresh standard Gaussian vector
conditional on the full training tape and earlier query answers.
Suppose its posterior mean and covariance, under the appropriate revealed
prefix, satisfy the supplied bounds

\[
 \|\mu\|_{2,n}\le M_\mu,
 \qquad \Gamma\succeq\sigma^2I.
\]

These bounds must hold uniformly for the actual capped oracle inputs.
For the standardized innovation $g=\Gamma^{-1/2}(y-\mu)$, deterministic
norm inequalities give, on $\|\xi\|_{2,n}\le2$,

\[
 \|g\|_{2,n}
       \le\sigma^{-1}(CB+M_\mu)+2,
 \qquad
 \max_i|g_i|\le\sqrt n\,[\sigma^{-1}(CB+M_\mu)+2].
 \tag{16}
\]

Thus a coordinate cap of this latter size is justified, unlike a
$C\sqrt{\log n}$ cap inferred from an inapplicable conditional
Gaussian law. If a separately proved closed posterior formula bounds
$M_\mu$ by a polynomial in $R$, $\sigma^{-1}$ and the declared
input/tape bounds, (16) has the proposed $\sqrt n$ times polynomial
size. Its logarithmic description length remains polynomial in
$\log n$, $\log(\sigma^{-1})$ and the other counted quantities.
Equation (16) proves this cap consequence, not the missing posterior
mean formula or Gaussian identification itself.

For clarity, the relevant raw-noise tail is elementary. With
$\xi\sim N(0,I_n)$,

\[
 \Pr(\|\xi\|_{2,n}>2)
 \le e^{-n}\mathbb E e^{\|\xi\|_2^2/4}
 =e^{-(1-\frac12\log2)n}\le e^{-n/2}.
 \tag{17}
\]

The same bound holds conditional on any fixed good training tape and
earlier query noise. Hence $q$ fresh query matrix calls cost at most
$q e^{-n/2}$ failure for each query, uniformly over all admissible input
and time choices. There is still no union over queries. On their common
success event the forward recurrence bounds the query error by
$2\sum_\ell a_\ell\sigma_\ell$, before additional scalar errors.
If $N_s$ fresh scalar standard Gaussians are capped at magnitude $n$,
their extra failure probability is at most $2N_s e^{-n^2/2}$.
Their contribution to output error requires the separately certified
scalar perturbation coefficients, as stated above.

RMS projections on oracle feature or carrier inputs are nonexpansive and
can enforce the required input bound $B$. Their identity on the intended
good computation must be checked; the present transfer does not presume
it. Their role here is to justify a uniform conditional estimate for
fresh raw query noise, not to claim that standardized innovations remain
Gaussian after the full tape is fixed.

## 6. Two conditions that cannot be dropped

**Current summaries must carry nested information for this argument.**
Let a tape be uniform on $\{0,1,\ldots,R\}$, let $A^c=\{0\}$,
and define the current one-bit summary
$C_j=\mathbf1_{\{0,j\}}$ for $1\le j\le R$. Whenever $C_j=1$,
the bad-event posterior is $1/2$. For every tape there is some prefix
with this posterior, so
$\Pr(\max_j\Pr(A^c\mid C_j)>1/4)=1$, whereas
$4\Pr(A^c)=4/(R+1)$ tends to zero. These summaries discard earlier
information and their sigma-fields are not nested. Conditioning instead
on the retained full prefix $(C_1,\ldots,C_j)$ restores (3), but that
history's information must actually be counted and available to the
decoder. Merely introducing it in the proof would change the decoder law.

**Unconditional pointwise query couplings are not enough after conditioning.**
Let $W$ be uniform on $\{1,\ldots,N\}$, the target be identically
zero, the query set be this same finite set, and the noiseless program
output be $g(z;W)=\mathbf1_{\{z=W\}}$. Each fixed query has
unconditional failure probability $1/N$. But if the retained summary is
$C=W$, the posterior program output at $z=C$ is certainly one.
Thus every realized state fails somewhere. This violates the common-tape
conditional hypothesis (8), while satisfying arbitrarily small
unconditional pointwise errors. The uniform conditional RMS estimate
(15), not an unconditional querywise union argument, is the relevant
repair for the specified fresh-noise forward program.

## 7. What is, and is not, a current-state decoder theorem

The posterior expectation interface in (12) is to be implemented from
the retained current prefix and the passive query alone. This note does
not prescribe regenerating the training path or conditioning a dense
initialization by uncounted computation. Its probability proof uses the
full tape $W$, posterior kernels and $f_0$ only as mathematical objects.
They are not additional runtime inputs.

To turn the transfer into the requested current compressed-history model,
the separate construction must prove that the retained state determines
the exact relevant posterior query law; that its information is nested
as in (3); that (8) follows from the actual finite-width coupling; and
that bounded tests of that posterior are deterministically evaluable with
all coefficients, precision and peak workspace counted, without replaying
training. None of those representation or computational conclusions is
implied merely by writing the conditional probability in (9).

What is established here is the accuracy transfer once those interfaces
hold: with $p\le\eta+\delta_{\rm tr}$ and fixed
$\alpha=1/4$, $\rho\le1/8$, success is at least $1-4p$ and the
simultaneous error is (11), or (13) for smooth-test bisection. There is
no extra factor $R$ in the failure probability and no query net.
An opaque eventual bound on $p$ remains an opaque eventual bound; the
argument does not make the success width effective.

## 8. Provenance

This bounded continuation uses the supervisor's conditional-prefix task,
its specified global training-good event and fresh passive-query-noise
mechanism, plus the author's own `ROBUST_CENTER_TRANSFER.md`.
The center selection, finite maximal proof, posterior-kernel argument,
forward noise bound and counterexamples were derived here. No new
scientific source, other agent's note, experiment or other study was read.
The existing notation and rigorous-proof instructions were applied, with
the previously directed fallback for the inaccessible custom notation
skill. Only this assigned file was created; no Git index or maintained
source was changed.
