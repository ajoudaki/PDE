# Independent check of the finite-width/population rate note

2026-10-05. Independent internal mathematical check of
FINITE_WIDTH_RATE.md, current corrected SHA-256
dadea1977d33c38ccbb484d0fc6cdc21f30e2bcb541a7215411a7965496225af.
The audit began on frozen SHA-256
f2d03310b20297951dc66d479775e3a963ba50c7fc8311496b76e8cb7936f766.
During the check, the coordinator incorporated only the clarifications listed
below. The resulting changed passages and their interfaces were reread in
full. No experiment, simulation, Git-index mutation, maintained-book edit, or
checker edit of the primary input was performed.

## Verdict

**Pass.** Proposition 1 is a valid residual-damped reduction, including the
logarithmically growing fitting horizon and fitted endpoint. Theorem 2 has the
stated whole-sphere \(O_{\mathbb P}(n^{-1/2})\) centered fluctuation and
uniform \(O(n^{-1})\) bias. The model scaling, both empirical-process
arguments, the shared-\(\Xi_j\) contraction, Gaussian covariance
differentiation at singular covariances, and the probability quantifiers all
check.

The requested strict all-time finite-to-population theorem remains open. The
note correctly separates the centered dynamic source estimate from the
finite-width bias estimate and does not infer either from an
independent-dense comparison.

The initial snapshot required three clarifications. All three are incorporated
correctly in the current snapshot:

1. Section 5 now defines the scaled prediction gradient as

   \[
   \Theta=(W_n^{(1)},\sqrt n\,W_n^{(2)},W_n^{(3)}),\qquad
   \mathcal F_{n,v}=n f_n(v),\qquad
   g_{n,v}=\nabla_\Theta\mathcal F_{n,v},
   \]

   together with \(J_n(t,s)=D_{\Theta(s)}\Theta(t)\). This removes the former
   ambiguity with \(\nabla_\Theta f_n\), which would have put equations
   (31)--(33) off by a factor \(n\).

2. Proposition 1 now states the deterministic population tail explicitly as
   (8a). From the two displayed endpoint bounds, its literal continuation is

   \[
   \sup_{t\in[T_n,\infty]}\sup_v|f_n(t,v)-f(t,v)|
   \le \sup_v|f_n(T_n,v)-f(T_n,v)|
      +4C_{\rm tail}n^{-1/2}.
   \]

   The stated factor four correctly compares each value at \(t\) and \(T_n\)
   through its endpoint. The stronger integrated-velocity tail could reduce
   the constant to two, but is unnecessary.

3. The opening summary now calls (12) a sufficient prediction-level
   obligation rather than an equivalent reformulation of (33). Section 5 now
   also states that (33) alone is insufficient: the route still needs
   same-root trace estimates, quantitative query increments, and a smooth,
   globally valid stopped/extended Gaussian family whose stop can be removed.
   This correctly records the boundary contribution that prevents direct
   differentiation of an indicator-restricted good event. The separate
   dynamic bias estimate remains necessary afterward.

The source description is also corrected: maintained Section B.1 “provides no
quantitative finite-width rate,” rather than literally disclaiming one.

## 1. Normalization and initialized kernel

The note consistently defines the normalized input
\(v=x/\sqrt d\in S^{d-1}\). Thus for a row
\(A_i\sim N(0,I_d)\), the actual first preactivation is
\(A_i\cdot v\sim N(0,1)\); no further \(1/\sqrt d\) belongs in
\(H_n(v)\). This agrees with the global convention
\(W^{(1)}x/\sqrt d=W^{(1)}v\).

The maintained B.1 theorem uses unhalved sum loss and block multipliers
\(\kappa_1,\kappa_2,\kappa_3\). Taking every
\(\kappa_\ell=1/m\) gives squared mean loss with stored-weight mobilities
\((n,1,n)\). Deterministic zero readout satisfies its vanishing-readout
hypothesis.

In the mobility-Euclidean coordinates above,

\[
K_n(t;u,v)=\frac1n g_{n,u}(t)^Tg_{n,v}(t),\qquad
\partial_t f_n(t,v)=-\frac2m\sum_aK_n(t;v,v_a)r_{n,a}(t).
\]

At \(W_n^{(3)}(0)=0\), both hidden-block prediction gradients vanish.
Consequently the whole initialized tangent kernel is

\[
K_n^0(u,v)=\frac1n h_n^{(2)}(0,u)^Th_n^{(2)}(0,v).
\]

For orthonormal \(v_a\), the first-layer Gaussian coordinates for distinct
samples are independent and centered after the odd tanh. Their covariance is
\(qI_m\), where \(q=\mathbb E\tanh^2(G)\). The initialized middle Gaussian
action gives independent \(N(0,q)\) sample coordinates, and the top-feature
covariance is \(\gamma I_m\), where

\[
\gamma=\mathbb E\tanh^2(\sqrt q\,G)>0.
\]

Thus \(\lambda=\gamma/m\) and the initialized population Gram are correct.

## 2. Proposition 1

Set

\[
e_a(t)=f_n(t,v_a)-f(t,v_a),\qquad r_n(t)=r(t)+e(t).
\]

Since \(A_n=K_n^{\rm train}/m\) and \(A=K^{\rm train}/m\), subtraction of
the two exact residual equations gives

\[
\dot e=-2A_ne-2(A_n-A)r,\qquad e(0)=0,
\]

with no missing \(m\), width, or sign. The finite tangent matrix is symmetric
positive semidefinite. Its readout block alone is the normalized top-feature
Gram, so the checked fitting event gives
\(A_n(t)\succeq(\lambda/4)I_m\); \(g=\lambda/4\) is valid.

Writing \(F(t)=\lVert(A_n-A)r\rVert_2\), the upper Dini derivative obeys

\[
D^+\lVert e(t)\rVert_2\le-2g\lVert e(t)\rVert_2+2F(t).
\]

Variation of constants and Tonelli give

\[
\lVert e(t)\rVert_2
\le2\int_0^te^{-2g(t-s)}F(s)\,ds,
\qquad
\int_0^T\lVert e(t)\rVert_2\,dt
\le g^{-1}\int_0^TF(t)\,dt.
\]

For a passive query, direct subtraction gives

\[
\dot d_v=-2a_n(t,v)^Te-2(a_n(t,v)-a(t,v))^Tr,\qquad d_v(0)=0.
\]

If the two terms in \(\mathfrak S_n(T)\) are
\(I_{\rm tr}\) and \(I_{\rm q}\), respectively, then

\[
\sup_{t\le T,v}|d_v(t)|
\le2\frac Bg I_{\rm tr}+2I_{\rm q}
\le2\left(1+\frac Bg\right)\mathfrak S_n(T).
\]

This proves (10). Damping is used on the training error and the passive
query is controlled by its time integral; no factor \(T\) appears.

The explicit fitting proof supplies time- and width-independent hidden
operator, feature, readout, Gram-gap, residual-decay, and whole-sphere tail
bounds on an event of prescribed probability for every sufficiently large
width. The same energy/path-length and first-exit argument works in the
canonical population Hilbert spaces because the rank-one updates and middle
action use their actual Hilbert adjoints. It gives a deterministic population
endpoint and the analogous whole-sphere tail. This is a direct argument, not
an interchange of \(n\to\infty\) with \(t\to\infty\).

At \(T_n=\lambda^{-1}\log n\), both tails are \(O(n^{-1/2})\).
Apply (12) at confidence \(\delta/2\) and the physical fitting event at
confidence \(\delta/2\). A union bound proves (4), after changing the fixed
coefficient. Both \(C_\delta\) and \(N_\delta\) may depend on the fixed task
and \(\delta\). The probability is separate at each width, not one common
event for an infinite sequence. The stated quantifiers are correct.

## 3. First-layer empirical covariance in Theorem 2

With

\[
H_n(v)=n^{-1/2}(\tanh(A_i\cdot v))_{i=1}^n,
\]

the entries of \(\Sigma_n(u,v)\) are averages of bounded iid variables.
For the off-diagonal class, symmetrization produces coordinate maps

\[
s\longmapsto \tanh(A_i\cdot u)\tanh(s).
\]

After the rows \(A_i\) are fixed, these maps vanish at zero and are
one-Lipschitz. Coordinatewise contraction therefore reduces the Rademacher
supremum to

\[
\frac1n\sup_{\lVert v\rVert_2=1}
\left|\sum_i\varepsilon_iA_i\cdot v\right|
=\frac1n\left\lVert\sum_i\varepsilon_iA_i\right\rVert_2,
\]

whose expectation is at most \(\sqrt{d/n}\).
The class \(s\mapsto\tanh^2(s)\) is bounded, vanishes at zero, and is
two-Lipschitz, so the varying diagonal has the same bound; the fixed
\(u\)-diagonal is simpler. Replacing one row changes each empirical
supremum by at most \(2/n\). Bounded differences and a constant union over
the covariance entries give (26). No independence among those entries is
needed.

## 4. Conditional second-layer empirical process

Conditional on the first layer,

\[
K_n^0(u,v)=\frac1n\sum_jF_v(\Xi_j),\qquad
F_v(\xi)=\tanh(\xi\cdot H_n(u))\tanh(\xi\cdot H_n(v)),
\]

where the rows \(\Xi_j\sim N(0,I_n)\) are iid. The shared use of
\(\Xi_j\) in the two factors causes no independence gap. After the rows are
fixed, put \(c_j=\tanh(\Xi_j\cdot H_n(u))\). Each coordinate map
\(s\mapsto c_j\tanh s\) vanishes at zero and has Lipschitz constant at most
one. Coordinatewise Rademacher contraction is therefore legitimate even
though the multiplier and score use the same \(\Xi_j\). It leaves

\[
Z=\frac1n\sum_j\varepsilon_j\Xi_j\sim N(0,I_n/n)
\]

exactly.

On \(\lVert W_n^{(1)}(0)\rVert_{\rm op}/\sqrt n\le2\), the map
\(H_n:S^{d-1}\to\mathbb R^n\) is two-Lipschitz and takes values in the unit
ball. The centered Gaussian process \(Z^TH_n(v)\) therefore has increment
metric at most \(2\lVert v-v'\rVert_2/\sqrt n\). Anchoring at one point and
comparing with \(2g\cdot v/\sqrt n\) gives expectation
\(C(1+\sqrt d)/\sqrt n\). Conditional bounded differences adds
\(C\sqrt{\log(1/\delta)/n}\). The first-layer operator event has
exponentially small failure at fixed \(d\), which is absorbed into
\(\delta\) for \(n\ge N(d,\delta)\). This matches the target's
\(\delta\)-dependent width threshold.

## 5. Covariance regularity and the \(O(n^{-1})\) bias

Let

\[
F(z_1,z_2)=\tanh(z_1)\tanh(z_2),\qquad
\Psi(\Sigma)=\mathbb E_\Sigma F(Z).
\]

For a positive-definite covariance path, Gaussian integration by parts gives

\[
D\Psi(\Sigma)[E]
=\frac12\sum_{i,j}E_{ij}\,\mathbb E_\Sigma[\partial_{ij}F(Z)],
\]

and another differentiation gives

\[
D^2\Psi(\Sigma)[E,G]
=\frac14\sum_{i,j,k,l}E_{ij}G_{kl}\,
  \mathbb E_\Sigma[\partial_{ijkl}F(Z)].
\]

All derivatives of tanh are bounded, so these formulas give uniform
covariance Lipschitz and Hessian bounds. They remain valid at singular
covariances: add \(\varepsilon I\) to the whole positive-semidefinite
segment, use the same derivative bounds, and let
\(\varepsilon\downarrow0\) by dominated convergence. This includes the
rank-one case \(u=v\); no inverse covariance appears.

Taylor's formula yields

\[
|\Psi(\Sigma_n)-\Psi(\Sigma)
 -D\Psi(\Sigma)[\Sigma_n-\Sigma]|
\le C\lVert\Sigma_n-\Sigma\rVert_F^2.
\]

Every entry of \(\Sigma_n-\Sigma\) is a centered average of bounded iid
variables, so

\[
\mathbb E(\Sigma_n-\Sigma)=0,\qquad
\mathbb E\lVert\Sigma_n-\Sigma\rVert_F^2\le C/n.
\]

Expectation cancels the linear term and proves (20), uniformly in \(v\).
The upper-layer average is conditionally unbiased, so it adds no bias.
Combining the \(O(n^{-1})\) bound with the strict-root bound for
\(K_n^0-K^0\) proves (21).

At zero readout, \(r_{n,a}(0)=r_a(0)=-y_a\), so (30) follows from the exact
kernel equation. Since

\[
\frac1m\sum_a|y_a|\le\frac{\lVert y\rVert_2}{\sqrt m}=Y,
\]

(22) follows directly. Apply (21) at confidence \(\delta/m\) for each fixed
training input and take a union bound to obtain (23); no independence across
training inputs is required.

The final variance lower-bound remark also checks. Conditional on the first
layer, the diagonal upper-layer summands are iid. Their conditional variance
converges to
\(\operatorname{Var}[\tanh^2(\sqrt q\,G)]>0\), and the law of total variance
gives \(\operatorname{Var}K_n^0(u,u)\ge c/n\) eventually.

## 6. The dynamic boundary

Maintained Section B.1 identifies the width limit at each fixed proof mesh and
only afterward sends the mesh to zero. Its fixed-program input is qualitative
and concerns a finite transcript. It supplies no rate uniform in a refining
mesh or on \(T_n\asymp\log n\), so it cannot imply (12).

The authorized corrected dense-comparison proof distinguishes:

- instantaneous fields \(D_\Theta z[g_{n,b}]\), for which fixed-order
  counting moments and Hessian-gradient RMS estimates are available under
  its source hypotheses;
- transported fields
  \(D_\Theta z[J_n(T,s)^Tg_{n,v}(T)]\), for which those estimates do not
  apply.

Differentiating the transported terminal field creates a propagated Hessian
endpoint and an integral containing third derivatives of the prediction.
The latter contains
\(k_{n,a}^{(\ell)}\odot R_{n,a}^{(\ell)}\). Available carrier moments control
the first factor, but neither a physical RMS stop nor the instantaneous
response theorem controls the transported second factor in counting \(L^4\).
Thus (33), with clarification 3, is an accurate first missing response
estimate in this particular route.

The dynamic bias is separate. Fixed-program convergence says that the reused
Gaussian-action bias vanishes for each fixed finite transcript; it does not
give an \(O(n^{-1})\), or even \(O(n^{-1/2})\), expansion uniformly on a
growing transcript or residual-weighted interval. The authorized whole-query
source theorem constructs initialization-computable source spaces for one
realized dense trajectory, and its \(C\sqrt n\) passive-query magnitude enters
only an analytic approximation degree. It supplies neither centered
concentration nor a bias expansion relative to the deterministic population
action. Finally, the orthogonal-tanh onset formulas contain cross-label terms
after differentiating the hidden dynamics, so initialized orthogonality does
not close the transported-response hierarchy.

The two dynamic entries and the requested theorem must therefore remain
**open**.

## 7. Scope and limitations

The complete initial and corrected primary snapshots and all five
user-authorized notes named in the study README were read. Directly relevant
corrections/proofs inspected
were the complete explicit fitting proof and check, the complete corrected
dense-comparison proof, the complete whole-query response source and check,
and the orthogonal-tanh time/prediction route and check. Maintained scope was
`docs/index.qmd`, `docs/notation.qmd`, B.1 of
`docs/04-continuing-flows.qmd`, and the fixed-program specialization in
`docs/02-gaussian-reuse.qmd`. No `RESULT.md`, other route in the present
new study, unrelated study, Git history, or `old_docs/` passage was read.

The rigorous-math and conjecture-audit instructions were applied. The
repository-required canonical-notation skill at
`/home/amir/.codex/skills/explain-with-canonical-notation/SKILL.md` was
inaccessible: ordinary and escalated reads both returned operating-system
`Permission denied`, so its linked neural-network reference could not be
discovered. `docs/notation.qmd` and the explicit repository notation rules
were used as the fallback.

This check reconstructs every new argument in Proposition 1 and Theorem 2 and
checks the claimed dynamic boundary against the authorized corrected sources.
It does not independently re-prove every ancestral stochastic insertion
theorem cited inside those sources. That limitation does not affect the pass
for the two new results or the conclusion that the strict dynamic theorem is
still open.
