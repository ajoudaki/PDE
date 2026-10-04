# Coordinator reconstruction of the neuron-reduction continuation

2026-10-03. Internal collaborative check, not a promotion review. The
coordinator read the complete two route notes, their complete cross-checks,
and the complete relevant initialized-projection and all-order-fitting
portion of the unchanged manuscript proof. The manuscript and study
dependencies previously read in full remain unchanged.

## Frozen source versions and status

| Source | SHA-256 | Checked scope |
|---|---|---|
| `NEURON_GLOBAL_NEGATIVE.md` | `ddfca55aaaddd6bb80d74d0664038539ed8d7d1ee5ea52240eeee3d97de47e1c` | Complete fixed-time, fitted-endpoint, and orthogonal-continuum lower bounds |
| `NEURON_GLOBAL_POSITIVE.md` | `00aefc9cbccee65a8d4ddaa603709395d1eace1a2e91d54aa4da7c85389e8819` | Complete finite-jet construction and its limitations; history consequence using the previously checked history proof |
| `paper/proof_alltime.tex` | `f3f0a0f5d0f553ced7c7334863bc04734033d00ecef48cd2031194dda374035d` | Initialization, projection estimates, fitting, and convergence dependency |

**PASS within the stated scopes.** No unconditional global neuron-sampling
theorem or universal incompressibility theorem follows. The two complete
cross-checks are [negative](NEURON_GLOBAL_NEGATIVE_CHECK.md) and
[positive](NEURON_GLOBAL_POSITIVE_CHECK.md). The former checked the negative
source before its subsequent continuum extension, at hash
`0eeba02726f8f3bec3dbe5026d857402ca091c69b5c382bf6b9ae55731e98e80`.
The additional extension is reconstructed below. The latter includes a
version follow-up to the final positive source.

## Negative theorem: independent reconstruction

The coordinator first reconstructed the whole fixed-time proof and then
derived the fitted-endpoint extension before asking the route author to
check it. The route author supplied the necessary training-only fitting
event and complete argument. The positive-route author then reconstructed
the complete result in its separate check. This was collaborative internal
checking, not three independent discoveries or isolated promotion reviews.

The crucial verified steps are:

1. With only $x_1=\sqrt d\,e_1$ trained, the entire closure path is
   measurable from $(A_0e_1,W_0)$. Each orthogonal query $A_0v$ remains
   Gaussian and independent of that training initialization. This does not
   assert Gaussianity of trained backward signals.
2. The small-label fitting proof needs only the training preactivation RMS,
   mixer operator norm, and training Gram gap. Its full first-matrix norm
   event is unnecessary here. Removing that part of the event preserves the
   untouched-query conditional Gaussian law.
3. The final speed bounds in the manuscript give $O(y^2)$ integrated mixer
   and feature displacement, despite an earlier coarse $O(y^{3/2})$ tube
   bound. The closure defect is included in these speeds. They are uniform
   in width and every positive memory order.
4. Scalar residual sign preservation and interpolation imply
   $w_\infty=(y/G_k)g_0(x_1)+e$, where
   $\|e\|_2/\sqrt k\le Cy^3$ and $\|w_\infty\|_\infty\le Cy$.
5. The nonlinear query remainder is odd in the untouched Gaussian vector.
   Subtracting its two gradients has readout, matrix, and gate terms. Each
   is at most $Cy^3/\sqrt k$. Gaussian Poincare therefore bounds its
   second moment by $Cy^6/k$, rather than a width-independent error.
6. Conditioning on the two initial lower-feature vectors makes upper rows
   independent Gaussian pairs. The variance of their tanh product is
   uniformly positive on a fixed covariance neighborhood. This proves the
   initial kernel second-moment lower bound $c/k$.
7. Restriction to both good training events is handled by monotonicity for
   upper moments and boundedness of the initial kernel for the lower
   moment. No invalid joint Gaussian conditioning or independence between
   the two widths is used. The reverse triangle inequality and fourth
   moments yield the positive-probability prediction lower bound.

The constants are uniform over deterministic choices of both orders. This
is not a claim that one lower-bound event occurs simultaneously for every
pair of orders. The smaller marginal must remain canonical. Initialization-
dependent noncanonical weights or a response-aware projected mixer are not
covered. The root-$n$ impossibility applies at sufficiently high fixed
confidence; a fixed failure-probability lower bound is not an almost-sure
statement.

### Continuum extension

For a fixed probability measure $\mu$ on the orthogonal input sphere,
every pointwise marginal bound above holds with identical constants. Let
$D(x)$ be the fitted difference and $\mathcal T$ the two training-good
events' intersection. The reverse triangle inequality in the product
space $L^2(\mathbb P\times\mu)$ gives

\[
 \left(\mathbb E\int D(x)^2\mathbf1_{\mathcal T}\,d\mu\right)^{1/2}
 \ge \frac y{\sqrt N}(c-Cy^2-C\sqrt{N/n}).
\]

For $Z=\mathbf1_{\mathcal T}\int D^2\,d\mu$, Tonelli and
Cauchy--Schwarz give

\[
 \mathbb E Z^2
 \le\iint\sqrt{
  \mathbb E[D(x)^4\mathbf1_{\mathcal T}]
  \mathbb E[D(x')^4\mathbf1_{\mathcal T}]}
       \,d\mu(x)d\mu(x')\le Cy^4/N^2.
\]

The scalar second-moment lower-tail inequality applied to $Z$ proves the
same $c_y/\sqrt N$ lower bound in fitted $L^2(\mu)$ with fixed positive
probability. The all-time norm dominates this endpoint norm. This argument
requires no independence of query directions. For $d\ge3$, uniform
measure on the orthogonal sphere is nonatomic. It is not uniform measure
on the full input sphere. The same proof works for the fixed-time version.

## Positive theorem: independent reconstruction and corrections

The coordinator read the complete finite-jet construction before receiving
the other author's cross-check. The empirical-isometry normalization
$U^\top U/n=I$, $V^\top V/n=I$ gives the projected source coefficient
$B=U^\top W_0V/n$ without a missing width factor. The selected positive
Gram rules make both forward and reverse actions exact on the listed jet
vectors, and give the advertised operator bound. The raw moment equations
use exactly the weighted lower and upper contractions required by the
induction. Every retained memory derivative is a linear combination of
already included feature or backward-response derivatives, regardless of
the number of memory modes. Thus the node count has no hidden factor of
$q$, while the moving memory count correctly includes $q$.

The clock is the original residual-RMS clock, whose derivatives exist near
initialization because $Y>0$. Zero labels are stationary. The finite-jet
claim applies to every finite initialization. Fitting, in contrast,
requires a positive initial Gram gap, deterministic initialization bounds,
and sufficiently small labels; the source was corrected to state this
explicitly. The correction changes no cubature identity. A subsequent
dilation wording change to "each moment" also changes no equation.

The selected design can depend on $q,p$ and the fixed finite probe set;
the result does not give one design simultaneously matching every order or
every query. Its initialization-only computations may be expensive and
ill conditioned. It is an autonomous finite system once those computations
are complete, but no degree choice $p(n)$ has been proved to give the
requested global prediction accuracy.

The history follow-up uses the already checked same-study weighted
Legendre-domain estimate. Holder's inequality gives the stated amplitude
$\ell^p$ bound for $p>2/5$, with the original history-bound constant
retained. The actual fixed mixer preserves this bound by its operator
norm even though the coefficients are endogenous. The displayed
two-sided Gaussian conditioning formula requires predictable queries;
future history coefficients do not meet that premise automatically. The
one-sample quadratic-form calculation is an exact obstruction to that
particular Gaussian shortcut, not an impossibility theorem for cubature.

## Research conclusion and operations

The negative result certifies persistence of canonical sampling
fluctuations through learning and fitting. The positive result certifies
that any finite collection of initial nonlinear responses can be included
in a much smaller weighted population. Neither resolves the unrestricted
source-dependent all-time sampling target. No unproved global comparison
has been relabelled as a condition or promoted to a theorem.

No numerical experiment was run. No paper, maintained-code, prior-study,
Git-index, commit, or remote change was made. The existing modified PDF and
unrelated study README were preserved. Validation was mathematical
reconstruction, source hashing, and local artifact checks.

The final artifact check verified matching display-math delimiters, all
local Markdown-file links, and both frozen route hashes across the six new
notes and README. The first link-check pattern also matched a mathematical
matrix product; restricting it to Markdown-file targets removed that
checker false positive, and the complete check passed. `git diff --cached
--name-only` remained empty; HEAD remained
`4dfa5c1ef2c5b920eda2bbc84316b189b97da92e`; tracked status still contained
only the two pre-existing modifications recorded above.
