# Sampling an unseen query within a dense-forward budget

2026-10-06. Scoped author derivation. The new runtime target is
\(O(Ln^2+dn)\), with fixed admissible data, depth and confidence. The
previous requirement of time polynomial in the compact description is no
longer imposed. All other physical, storage and query qualifications remain.

**Result:** there is a fully counted conditional dense-budget corollary.
Moreover, finite-seed cubature can use a centered sub-Gaussian scale instead
of a global range bound, including for unbounded row functions. If the same
residual perturbation geometry controls statistical substitution and
numerical integration, the sufficient statistical estimate already implies
query time \(n\) times an absolute power of \(\log n\), hence strictly
\(O(n^2)\). The actual neural circuit has not been proved to satisfy that
estimate. Its existing \(\exp[\operatorname{polylog}(n)]\) caps do not
close this gap.

This note preserves the dense-variability **upper-bound scale**. It does not
silently preserve the earlier literal coefficient \(2b_n+1/n\): an added
\(O(b_n)\) error changes that coefficient. The exact coefficient issue is
quantified below.

## 1. Contract and inputs

Keep arbitrary fixed \(L\ge2\), the original \(m\ge d\) spanning
sphere data, Gaussian initialization, zero readout, mean-square flow with
mobilities \((n,1,\ldots,1,n)\), analytic strip activations with bounded
slope and possibly unbounded values, and the full original label/gap
conditions. The target is one event controlling every sphere input and the
whole physical trajectory, including its fitted endpoint. Test inputs need
not be declared during acquisition; no test labels are used. Preprocessing
may be expensive. Queries cannot retrieve discarded dense state or replay
the scalar training evolution. Retained bits and peak scratch both count.

The scientific files read for this route were the complete files
`RESULT.md`, `EFFICIENT_QUERY_RANDOMIZED_INTEGRATION.md`,
`EFFICIENT_QUERY_INFORMATION.md`,
`EFFICIENT_QUERY_PHYSICAL_SYNTHESIS.md`, and
`FAST_SMALL_MATRIX_FUNCTIONS.md` in this study. Links in those inputs were
not followed. Their common notation is used below. In particular
\(b_n=b_n(\delta/32)\) denotes the displayed inherited certificate in
`RESULT.md`; for fixed nonzero labels it is
\(n^{-1/2}\exp[O(\sqrt{\log n})]\) times logarithmic factors, and
\(b_n^{-2}\le Cn\). Zero labels have the exact zero predictor separately.

The required rigorous-proof and research skills were read. The custom
canonical-notation file returned `Permission denied`; the supervisor's
explicitly authorized minimal-notation fallback was applied. No external
source, other study, experiment, or Git operation was used.
After this independent derivation was written, the supervisor supplied and
authorized use of a capped-density identity from a concurrent conditioning
route. Section 6 proves its sampling corollary from that supplied identity;
no other route file was read.

## 2. Finite-seed cubature for unbounded row functions

Here is an extension of Section 2 of the randomized-integration input.
Condition on a fixed complete training tape. Let
\(h_r(z;\theta)\), \(1\le r\le J\), be finitely many deterministic
families on \(z\in\mathbb R^D\), where \(\theta\) contains the sphere
input and bounded physical-patch coordinate. Let \(\mu=N(0,I_D)\).
Assume the centered moment-generating bound

\[
 \log\int \exp\{\lambda(h_r-\textstyle\int h_r\,d\mu)\}\,d\mu
                  \le \lambda^2 s_r^2/2
             \qquad(\lambda\in\mathbb R).
 \tag{1}
\]

Thus \(s_r\) is a supplied sub-Gaussian scale, not merely a standard
deviation. No boundedness of \(h_r\) is assumed. At requested tolerance
\(u_r>0\), take an even integer \(k\ge2\) and integers

\[
 Q_r=\max\{1,\lceil256k s_r^2/u_r^2\rceil\},\qquad
 Q_* =\max_r Q_r.
 \tag{2}
\]

Functions with zero scale and continuous Gaussian-row dependence are
constant in that row and can instead be evaluated once. Assume local row
and parameter Lipschitz bounds on the cube used below, and a Lipschitz bound
for \(\theta\mapsto\int h_r\,d\mu\). These bounds may be very large;
their logarithms, not their magnitudes, enter the numerical cost. Choose a
proof-only parameter net so that extending both its empirical and exact
averages to all \(\theta\) costs at most \(u_r/4\). Write \(M_r\)
for its size and choose

\[
             2\sum_r M_r4^{-k}\le\beta/2.
 \tag{3}
\]

For the sphere and a fixed number of interval coordinates,
\(\log M_r\) is bounded by a fixed-dimensional multiple of the logarithms
of the Lipschitz bounds, parameter ranges and \(u_r^{-1}\), as proved in
the input. Prefix and patch labels enter the finite index \(r\); there is
no net over all possible training tapes.

Choose a positive integer \(A\) with

\[
                  A^2\ge2\log(4Q_*D/\beta).
 \tag{4}
\]

Use exactly the input's binary-field polynomial generator to produce
\(k\)-wise independent row indices, each giving \(D\) independent
\(b\)-bit coordinate cells. For a coordinate cell with index \(V\), the
algorithm evaluates the Gaussian quantile at its midpoint
\((V+1/2)2^{-b}\), clipped to \([-A,A]\), to a prescribed error.
The seed is independent of the training tape and is retained.

The following coupling removes the need for a large bounded-function cap.
For the proof only, append independent uniforms \(U_{ia}\) on \([0,1]\)
inside all coordinate cells, \(1\le a\le D\), and define

\[
 Z_{ia}=\Phi^{-1}((V_{ia}+U_{ia})2^{-b}),
 \tag{5}
\]

where \(\Phi\) is the standard Gaussian distribution function. Any at
most \(k\) resulting rows are independent standard Gaussians: their cell
indices are independent uniform indices, and their within-cell uniforms
are independent. These extra uniforms are never generated or retained by
the algorithm.

At a fixed net point, the centered \(k\)-th moment of the average of the
first \(Q_r\) exact rows equals its fully independent counterpart. Indeed,
each term in the expanded moment uses at most \(k\) row indices. From
(1), independent averages have tails at most
\(2\exp[-Q_rt^2/(2s_r^2)]\); integrating this tail gives

\[
 \mathbb E\left|Q_r^{-1}\sum_{i\le Q_r}h_r(Z_i;\theta)
                         -\int h_r\,d\mu\right|^k
             \le2(k s_r^2/Q_r)^{k/2}.
 \tag{6}
\]

Markov's inequality and (2) give failure at most \(2\cdot4^{-k}\)
for error \(u_r/4\). Equation (3) controls all net tests. Separately,
the Gaussian tail and a union over \(Q_*D\) coordinates show that all
the exact rows in (5) lie in \([-A,A]^D\), except with probability at
most \(\beta/2\). This union does not depend on a query or parameter net.

On this latter event, the clipped quantile equals the exact quantile at
every coordinate in (5). The clipped quantile has global Lipschitz constant
\(\sqrt{2\pi}e^{A^2/2}\). Therefore the computed and exact row coordinates
differ by at most

\[
             \sqrt{2\pi}e^{A^2/2}2^{-b}+\zeta,
 \tag{7}
\]

where \(\zeta\) is the numerical quantile error. If \(K_z\) bounds
the local row Lipschitz constants, choose (7) at most
\(\min_r u_r/(8K_z)\), and at most one. Use the enlarged cube
\([-A-1,A+1]^D\) for the local bounds. Row rounding, function evaluation
and accumulation can then share \(u_r/2\); net extension costs
\(u_r/4\). Together with (6), the total error is at most \(u_r\).

This is a probability statement about the retained seed alone. If a seed
produces an inaccurate finite computed average, no value of the proof-only
uniforms can make all the preceding sufficient good events true. Hence its
failure probability is bounded by the joint seed/uniform failure probability.
Integrating out the auxiliary uniforms proves the claimed seed guarantee.
There is no population clipping bias in this argument: the exact Gaussian
samples in (6) concentrate around the original untruncated integral.

All actual prefixes, patches and sphere inputs are covered on this one
event. Averaging the conditional assertion over the independent training
tape produces one joint event. The finite seed gives a deterministic query
map after preprocessing; adaptive choices of later query inputs are covered.

The choices of \(k\), the cube and the net can be made without a circular
parameter definition in the dense-budget application. First use the desired
upper bound \(Q_r\le n^2\) in (4), choose local bounds and nets on that
cube, and then choose \(k\) by (3). The subsequent strict-budget estimates
below ensure (2) is eventually below this proposed bound. All net sizes and
local bounds used in this check must have the stated logarithmic estimates.

### Counted cost

The field degree is
\(w=\max\{Db,\lceil\log_2(Q_*+1)\rceil\}\). The retained seed
and fixed field polynomial use at most \((k+1)w+1\) bits. Horner
evaluation costs \(O(kw^2)\) elementary bit operations using schoolbook
binary polynomial arithmetic. The Gaussian quantile procedure in the input
has polynomial time and space in \(A^2\) and its requested precision.
Equation (7) needs

\[
 b=O\bigl(A^2+\log(2+K_z)+\max_r\log(2+u_r^{-1})\bigr).
 \tag{8}
\]

If a row circuit has instruction count \(N\), its complete local
evaluation includes those \(N\) operations, every activation call,
Gaussian generation, and all small matrices. The fast-matrix input makes
the matrix cost polynomial in \(N\), dimension, precision and logarithms
of the amplitude and inverse-gap bounds. An accumulator with local error
\(u_r/(C Q_r)\) requires an additional
\(O(\log Q_r+\log(2+u_r^{-1}))\) bits. Large row values also require
their integer-bit length; local amplitude logarithms must be counted.

Consequently all these costs are absolute-polylogarithmic whenever their
listed dimensions, counts and logarithms are. This statement counts the
original activation primitives, as the dense-forward comparison does.
A bit-time version requires polynomial-time activation and data/input
precision interfaces. The earlier polynomial-space interface alone does
not imply that stronger time statement, and analyticity alone does not
imply computability. No activation assumption has been strengthened in
the primitive-time conclusion.

## 3. Full query cost, including every row instruction

At a fixed current prefix \(c\), write an identity-preserving query as

\[
 d_r=a_r(c,d_{<r};x,t)^Tc+
            \int R_r(z;c,d_{<r};x,t)\,\mu(dz),
                    \qquad 1\le r\le q.
 \tag{9}
\]

All retained training summaries are fixed coefficients here. Computing the
row functions at new Gaussian arguments is allowed; acquiring missing
training summaries is not. Suppose supplied pointwise perturbation bounds
give a nonnegative strictly lower-triangular matrix \(\Lambda\) such
that summary errors satisfy

\[
 e_r\le\sum_{s<r}\Lambda_{rs}e_s+u_r.
 \tag{10}
\]

Let the final output have coordinate Lipschitz weights
\(\ell_r\ge0\). Define the row-influence weights by

\[
 (w_1,\ldots,w_q)=\ell^T(I-\Lambda)^{-1},\qquad
 (I-\Lambda)^{-1}=I+\Lambda+\cdots+\Lambda^{q-1}.
 \tag{11}
\]

Every matrix entry is nonnegative, so (10) implies output error at most
\(\sum_r w_r u_r\). This also explains seed reuse: concentration is
applied only to row functions at the seed-independent exact arguments in
(9); the change to computed earlier summaries is handled pointwise by (10).
There is no independence assertion at the adaptively computed arguments.

Let \(W_r\) be a certified complete cost for **one** numerical evaluation
of row instruction \(r\), including the finite Gaussian generation and
precision costs just described. Put \(W=\sum_r W_r\). Computing the
coefficients and final output has additional absolute-polylogarithmic cost
\(T_0\). Use cost envelopes at a common prescribed precision sufficient
for the tolerances below; optimizing tolerances does not treat
precision-dependent work as constant. Given positive influence and scale, choose

\[
 E=\sum_r [W_r(w_rs_r)^2]^{1/3},\qquad
 u_r=\frac{\varepsilon}{E}
                   \left(\frac{W_rs_r^2}{w_r}\right)^{1/3}.
 \tag{12}
\]

Then \(\sum_r w_ru_r=\varepsilon\), and substituting (2) gives
the complete sampled-query bound

\[
 T_{\rm query}\le T_0+C W+
            \frac{Ck}{\varepsilon^2}
                      \left\{\sum_r[W_r(w_rs_r)^2]^{1/3}\right\}^3.
 \tag{13}
\]

Terms of zero row scale can be evaluated deterministically; zero-influence
terms can be omitted from the output's dependency graph. Formula (12)
minimizes the continuous sum \(\sum_rW_rs_r^2/u_r^2\) under the
error constraint: Lagrange differentiation gives
\(u_r^3\propto W_rs_r^2/w_r\), and the function is convex on the
positive orthant. Integer sample ceilings cost the displayed \(CW\).
Thus (13) counts all \(q\) integrals, not a single representative row.

Extremely small positive scales need not force excessive precision. Replace
each tolerance in (12), if necessary, by
\(\max\{u_r/2,\varepsilon/[2q\max\{1,w_r\}]\}\).
The total weighted tolerance is still at most \(\varepsilon\), because
the maximum is bounded by the sum of its two arguments. The sample cost
increases by at most a factor four. Thus logarithmic required precision is
bounded using \(\log(\varepsilon^{-1})\), \(\log q\), and
\(\max_r\log(1+w_r)\), without an inverse-small-scale bit requirement.

For a simpler sufficient bound define
\(S=\sum_rw_rs_r\). Hölder's inequality gives

\[
 E\le W^{1/3}S^{2/3},\qquad
 T_{\rm query}\le T_0+CW+CkWS^2/\varepsilon^2.
 \tag{14}
\]

Equivalently, \(u_r=\varepsilon s_r/S\) uses a common sample count
\(O(1+kS^2/\varepsilon^2)\) for every row instruction and proves (14)
directly. No list of samples is stored: each loop regenerates the required
row from its index. The live storage comprises the seed, current row,
current small matrices, the \(q\) query summaries, counters and accumulators.
Their bound is an absolute power of \(\log n\), under the listed
logarithmic hypotheses. Neither \(Q_r\) nor a sphere net enters the
workspace count.

At error \(\varepsilon=c b_n\), the exact sufficient quadratic-budget
condition from (13) is

\[
 k\left\{\sum_r[W_r(w_rs_r)^2]^{1/3}\right\}^3
                         =O(n^2 b_n^2),
 \tag{15}
\]

with \(T_0+W=O(n^2)\). This is more specific than polynomial time in
\(n\). For example, if \(kW\le C\log^a(en)\) and
\(S\le C n^{1/2-\xi}\) for any fixed \(\xi>0\), then
(14) and \(b_n^{-2}\le Cn\) give
\(T_{\rm query}\le C n^{2-2\xi}\log^a(en)+T_0+CW=O(n^2)\).
The last implication follows from
\(a\log\log(en)-2\xi\log n\to-\infty\). In particular,
\(S=n^{o(1)}\) gives \(n^{1+o(1)}\) time and ample strict quadratic
slack. An unspecified polynomial \(S\), or
\(S=\exp[\log^2 n]\), does not satisfy this argument.

## 4. When the statistical estimate already pays for runtime

The training history is
\(C_r=n^{-1}\sum_iF_r(Z_i;C_{<r})+\eta E_r\), with information
budget \(H\) as in the inputs. On their all-prefix entropy event the
row-array posterior entropy is at most \(H/\alpha\).

Suppose the actual passive row test has the exact decomposition

\[
 G_r(z;c,u;x,t)=a_r(c,u;x,t)^TF(z;c)+R_r(z;c,u;x,t),
 \qquad \|a_r\|_1\le A_r.
 \tag{16}
\]

At the deterministic arguments of (9), assume (1) for \(R_r\) with
scale \(s_r\). The input's entropy-to-event proof applies without change
to the sub-Gaussian prior tail. For any fixed conditional failure budget
\(\rho>0\), put

\[
 h=\log(2q)+\frac{H/\alpha+\log2}{\rho}.
 \tag{17}
\]

With posterior probability at least \(1-\rho\), all \(q\) fixed row
residual discrepancies are bounded by
\(s_r\sqrt{2h/n}\). Indeed their union has prior probability at most
\(2q e^{-h}\), and binary relative entropy bounds its posterior
probability by \(\rho\). This is a pointwise consequence of one entropy
bound on a posterior measure. It introduces no additional training
exceptional set when the query input or physical time varies.

The historical-noise and fresh-query-noise events from the randomized
input give respective bounds \(T\) and \(T_q\), with explicitly
allocatable fixed failure budgets. The exact identity (16) then makes
the local empirical-versus-anchored errors at most

\[
 u_r^{\rm stat}=s_r\sqrt{2h/n}+\eta A_rT+\eta_qT_q.
 \tag{18}
\]

Here the original small noises multiply the reuse coefficients; there is
no replacement of a known empirical moment by an unrelated prior mean.

Assume **the same influence weights** (11) dominate propagation of (18)
through the actual empirical query and propagation of cubature errors
through the anchored sampled query. This is a substantive common-stability
hypothesis. One may always take a common maximum of available local
Lipschitz bounds, but their existing large values need not be useful.
Under this hypothesis the statistical output error is at most

\[
 \Delta_{\rm stat}
  =S\sqrt{2h/n}
       +\eta T\sum_rw_rA_r+\eta_qT_q\sum_rw_r.
 \tag{19}
\]

Choose the conditional failure budgets to total less than \(5/8\).
The robust-center interval of posterior mass at least \(5/8\) from
the inputs must then intersect the posterior interval around (9). The
same interval-overlap proof gives, on the original source and new training
events, uniformly over every query and time,

\[
 |d(c,x,t)-f_n(t,x)|\le 2b_n+\varepsilon_{\rm bridge}
                                      +\Delta_{\rm stat}.
 \tag{20}
\]

The cubature event adds \(\varepsilon\). Rounding the acquired prefix
and other fixed coefficients adds \(\varepsilon_{\rm prefix}\),
provided the replacement query has a proved modulus for those perturbations.
For example a certified bound
\(|d(c)-d(\widetilde c)|\le K_c\|c-\widetilde c\|_\infty\)
costs \(O(\log(2+K_c)+\log(\varepsilon_{\rm prefix}^{-1}))\)
fractional bits, plus the counted local arithmetic. This modulus is a
required bridge; the information bound for ideal histories does not prove it.
The probability budgets for all source, prefix, noise and seed events must
sum to at most the requested \(\delta\).

Now suppose the sufficient statistical scale condition itself holds:

\[
 S\sqrt{h/n}=O(b_n),\qquad
 \eta T\sum_rw_rA_r+\eta_qT_q\sum_rw_r=O(b_n),
 \qquad \varepsilon_{\rm prefix}=O(b_n).
 \tag{21}
\]

With \(\varepsilon=c b_n\), equation (14) immediately becomes

\[
       T_{\rm query}\le T_0+CW+CknW/h.
 \tag{22}
\]

If the local descriptions and precision parameters have the existing
absolute-polylogarithmic sizes, \(kW\le C\log^a(en)\) for an
absolute \(a\). Since \(h\ge\log2\), (22) is at most
\(Cn\log^a(en)\), which is strictly \(O(n^2)\) at all sufficiently
large individual widths. Because \(L\ge2\) and \(d,L\) are fixed,
this is also \(O(Ln^2+dn)\), with the allowed fixed-parameter constants.
Thus **a valid statistical substitution with this shared perturbation
geometry already suffices for the relaxed computational target**. No
separate claim that the existing global caps are \(n^{o(1)}\) is needed.

There remain two cautions. First, a small statistical influence in one
geometry need not bound perturbations made by a numerical algorithm in
another; the common-stability hypothesis cannot be omitted. Second, if the
literal old bound \(2b_n+1/n\) is required without proved slack in its
\(2b_n\) term, new errors must fit an \(O(1/n)\) allowance. Setting
\(\varepsilon=1/n\) in (14) costs \(CkWS^2n^2\), so strict quadratic
time would require the additional bound \(kWS^2=O(1)\) for this witness.
The inputs do not establish it. Equations (20)--(22) assert the historical
dense-upper-bound scale with stated constant changes.

## 5. A gap-free residual mechanism, and its precise limitation

A ridge control variate illustrates how an inverse covariance gap can
disappear from the scale in (1). Fix one prefix and deterministic query
arguments. Center the retained tests and query test under \(\mu\):
\(X=F-\mathbb EF\), \(g=G-\mathbb EG\). Let
\(K=\mathbb E[XX^T]\), \(v=\mathbb Eg^2\), and
\(k_0=\mathbb E[Xg]\). For \(\tau>0\) set

\[
                a=(K+\tau I)^{-1}k_0,\qquad R=G-a^TF.
 \tag{23}
\]

No covariance gap is assumed. A zero-eigenvalue direction of \(K\)
has zero covariance with \(g\), by Cauchy--Schwarz. Diagonalizing \(K\)
on its positive range gives \(k_0=K^{1/2}b\), where
\(\|b\|^2\le v\): minimize
\(\mathbb E(g-c^TX)^2\ge0\) over that range to obtain this bound.
Since \(\lambda/(\lambda+\tau)^2\le1/(4\tau)\),

\[
 \|a\|^2\le\frac{v}{4\tau},\qquad
 \operatorname{Var}(R)
  =v-k_0^T(K+\tau I)^{-1}k_0-\tau\|a\|^2\le v.
 \tag{24}
\]

Suppose, in addition, the centered joint vector \((X,g)\) is
sub-Gaussian relative to its covariance: every linear functional \(Z\)
of that vector satisfies
\(\log\mathbb E e^{\lambda Z}\le
\kappa^2\lambda^2\mathbb EZ^2/2\). Apply this to \(g-a^TX\).
Then (1) holds with

\[
       s_R\le\kappa\sqrt v,\qquad
       \eta T\|a\|_2\le\frac{\eta T\sqrt v}{2\sqrt\tau}.
 \tag{25}
\]

Both statistical residual concentration and Section 2's unbounded cubature
use this same gap-independent \(s_R\). Choosing \(\tau=\eta\), for
example, makes the historical-noise term at most
\(T\sqrt{v\eta}/2\). Computing a supplied small ridge system uses
only logarithmic inverse-gap precision by the fast-matrix result. The
large coefficients can therefore be harmless **if** their centered residual
has the asserted relative sub-Gaussian control and the physical query
propagates it with useful weights.

This is not yet an algorithm for the neural query. The population
covariances and query cross-covariances in (23) must themselves be obtained,
the numerical effects of their errors must be bounded, and multistep
coefficient dependence must satisfy the common stability and rounding
conditions above. Retaining the training moments alone does not provide
these unseen-query quantities.

Nor does analytic bounded slope imply the relative sub-Gaussian premise.
For a direct diagnostic take \(Z\sim N(0,1)\) and
\(G_t(Z)=\log(1+e^{Z-t})\), with \(t\to\infty\). These are real
analytic on a common strip \(|\operatorname{Im}z|<\pi/2\), and their
derivatives have modulus at most one there. For real \(Z\), dominated
convergence gives \(\operatorname{Var}(G_t)\to0\), since
\(G_t(Z)\le\log(1+e^Z)\le\log2+|Z|\) when \(t\ge0\).
However any centered sub-Gaussian scale \(s_t\) for \(G_t\) must
satisfy \(s_t^2\ge1\). Indeed, for \(\lambda\ge t+1\),

\[
 \mathbb E e^{\lambda(G_t-\mathbb EG_t)}
 \ge \tfrac12
      \exp\{\lambda^2/2-\lambda(t+\mathbb EG_t)\}.
 \tag{26}
\]

To verify this, restrict to \(Z\ge t+1\), use
\(G_t(Z)\ge Z-t\), and complete the Gaussian square; the remaining
probability for \(N(\lambda,1)\) to exceed \(t+1\) is at least
one half. Divide the logarithm of (26) by \(\lambda^2/2\) and let
\(\lambda\to\infty\). Hence a covariance-relative constant would
obey \(\kappa_t^2\ge1/\operatorname{Var}(G_t)\to\infty\).
This is a diagnostic about a proposed implication from activation
regularity, not a counterexample to the original physical neural theorem.

## 6. A bounded-density tilt variant supplied by the supervisor

Here is a separate conditional application of the same counted sampler.
Suppose the present prefix provides a row law \(\nu\) with density
\(r=d\nu/d\mu\) and relative entropy \(D(\nu\Vert\mu)\le h_0\),
where \(h_0=H/(\alpha n)\). Set

\[
 \omega(z)=\min\{r(z),4\},\qquad Z=\int\omega\,d\mu,\qquad
                         d\bar\nu=(\omega/Z)d\mu.
 \tag{27}
\]

Put \(e=\int(r-4)_+d\mu=1-Z\). The nonnegative entropy integrand satisfies
\(r\log r-r+1\ge(\log4-1)r\) on \(r>4\). Thus

\[
 e\le h_0/(\log4-1),\qquad Z\ge1-Ch_0,\qquad
                         \|\nu-\bar\nu\|_{\rm TV}\le e.
 \tag{28}
\]

For the last bound, removing mass \(e\) changes the unnormalized density
by \(L^1\) distance \(e\), and normalizing the remaining mass changes
it by another \(e\); total variation is half the \(L^1\) distance.
Eventually \(Z\ge1/2\) because \(H\) is absolute-polylogarithmic.
If \(|G|\le B_G\), then

\[
 \left|\int G\,d\nu-
                 \frac{\int\omega G\,d\mu}{\int\omega\,d\mu}\right|
                              \le2 B_G e.
 \tag{29}
\]

The numerator integrand is bounded by \(4B_G\), and the denominator by
four. If their numerical errors are \(u_N\) and \(u_Z\le1/4\),
the computed denominator is at least \(1/4\), and the ratio error is
at most \(4u_N+4B_Gu_Z\). This follows by adding and subtracting the
exact numerator divided by the computed denominator and using
\(|\int\omega G\,d\mu|\le B_G Z\). Apply the bounded version of
Section 2 with \(u_N\) of order \(\varepsilon\) and \(u_Z\) of
order \(\varepsilon/\max\{1,B_G\}\). The resulting sample count is

\[
                  O\bigl(k[1+B_G^2]/\varepsilon^2\bigr),
 \tag{30}
\]

with the already counted per-row costs and finite seed. The small entropy
therefore removes a large-density-ratio obstruction for **bounded tests**,
at a proved clipping bias \(O(B_G H/n)\). It does not prove that this
bias is small for the existing enormous global test caps or after a large
output amplification.

For an exponential tilt \(r=\exp(\lambda^TF-\psi)\), capped-density
evaluation is also numerically well conditioned in its log density:
the scalar function \(v\mapsto\min\{e^v,4\}\) is globally
four-Lipschitz. It can be evaluated to any absolute tolerance by clipping
large positive log densities and treating sufficiently negative ones as
zero. Large \(\lambda\), \(F\), and \(\psi\) need their full
integer-bit lengths and sufficient absolute precision in their difference;
if their logarithmic magnitudes and evaluation sensitivities are
absolute-polylogarithmic, these are counted polynomial costs. This claim
presumes that the present prefix makes \(\lambda\), \(\psi\), and
their certified precisions available, or supplies a counted algorithm to
obtain them. It supplies neither an optimization oracle nor future training
summaries.

This variant bypasses uncontrolled importance-weight variance in this
bounded-test setting. It still needs a comparison between the true
posterior physical query and the selected calibrated row law, plus useful
multistep propagation, prefix-rounding and test-scale bounds. It is not a
proof of that physical comparison.

## 7. Exact remaining physical obligations

The new cubature lemma removes bounded activation values and inefficient
Gaussian integration as automatic obstructions, under its explicit row
scale and local precision hypotheses. The complete neural application
still requires all of the following quantitative bridges:

1. Construct usable identities (16) for the actual passive-query circuit,
   with computable coefficients and centered residual scales satisfying
   (1), or an equally strong counted concentration mechanism. Generic
   range caps are insufficient and variance alone is insufficient.
2. Prove influence bounds that apply both to physical empirical
   substitution and to the implemented sampled recursion, with (21).
   An inverse-noise gain cannot be canceled by merely calling it an
   artifact; its cancellation must hold in these perturbation directions.
3. Count coefficient construction, query cross-covariances, all row calls,
   activation primitives and precision within \(W\), and establish the
   rounded-prefix modulus. Access to dense roots or training replay cannot
   be used to provide these ingredients.
4. Preserve the source's whole-trajectory and endpoint bridge and allocate
   the source, information, noise, numerical and seed failures on one
   event. The uniform cubature and entropy arguments above show how to
   combine such supplied bridges without a separate event per test input.

The physical-forcing lemma in the synthesis input does not by itself
establish item 2. It requires an explicit lift of the moment perturbations
to parameter displacement and integrable forcing, and residual-curvature
control along every intervening forced path. Its actual-trajectory action
bound \(CY(1+Y\sqrt{\log(en)})\) supplies neither condition. Even after
a lift, the necessary comparison is its size times that physical
amplification against the fixed \(b_n\), not a comparison of two
unspecified \(n^{-1/2+o(1)}\) expressions.

Status: (2)--(15), the conditional implication (21)--(22), and the ridge
and diagnostic calculations (23)--(26) are new proved conditional author
results. The application to the full original network remains open. The
relaxed dense-pass budget removes the earlier sample-count objection once
the correct statistical and numerical geometry is established; it does
not establish that geometry. Only this assigned note was written.
