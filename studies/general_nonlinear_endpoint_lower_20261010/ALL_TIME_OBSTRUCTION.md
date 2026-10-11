# A positive root-width lower bound cannot hold throughout training

## Superseded time contract

The user subsequently clarified that only the final fitted model is required.
This obstruction is therefore not an answer to the current endpoint-only
question. It is retained solely to distinguish the two quantifiers.

The user's final qualification requires a positive constant independent of
width and time such that the dense-copy discrepancy is at least that constant
times $n^{-1/2}$ **throughout training, including the fitted endpoint**.
This statement is false for the paper's canonical zero-readout initialization,
regardless of nonaffinity, data compatibility, or separation of the query set.
Excluding time zero alone does not repair it.

This is distinct from the earlier endpoint-only question. A general root-width
endpoint lower bound for all the specified nonlinear activations and data has
not been proved or disproved by this investigation.

## Precise obstruction and proof

Fix any finite width $n$ and two initializations from the paper, and let
$\mathcal X$ be any nonempty subset of the input sphere. The user-specified
set of queries separated from both signs of every training input is one such
set. The two networks are initialized with $w(0)=\widetilde w(0)=0$, hence

\[
f_n(0,x)=\widetilde f_n(0,x)=0\quad\text{for every }x.
\]

The finite parameter ODE has a locally Lipschitz vector field because the
activations are analytic on the real line. Thus it has a continuous solution
on some initial time interval for every finite initialized parameter tuple.
The finite network is jointly continuous in its parameters and its input.
The image of a compact initial time interval under the two parameter paths
is compact; the input sphere is compact. Uniform continuity therefore gives

\[
\lim_{t\downarrow0}
\sup_{\|x\|=\sqrt d}|f_n(t,x)-\widetilde f_n(t,x)|=0.
\]

Restricting the supremum to $\mathcal X$ preserves the limit. In particular,
for every $C>0$ independent of $t$,

\[
\inf_{t>0}\sup_{x\in\mathcal X}
 |f_n(t,x)-\widetilde f_n(t,x)|=0<C/\sqrt n. \tag{1}
\]

If the flows have not yet been shown global, the infimum can instead be taken
over any common initial existence interval; the same contradiction holds.
Thus the event of a positive simultaneous lower bound for all training times
is empty for each width. Gaussian initialization makes finite parameters
almost sure, so its probability is zero. No sufficiently-large-width
threshold changes this conclusion.

Even the weaker probability formulation with a common positive $C$, a common
width threshold, and a lower success probability at **each** deterministic
$t>0$ fails. Fix one width above that threshold. The indicators of
$\sup_{x\in\mathcal X}|f_n(t,x)-\widetilde f_n(t,x)|\ge C/\sqrt n$
converge to zero as $t\downarrow0$ almost surely on the locally defined
flows. Their probabilities converge to zero by bounded convergence, with
nonexistence before $t$ counted as failure. There can be no fixed positive
success probability valid for every such $t$.

## An explicit small-time upper bound on the paper's fitting event

For this paragraph only let
$H=\max_{0\le j\le L}\sqrt{Q^{(j)}_{11}}$. The real fitting lemma gives
$\sup_x\|h^{(L)}(t,x)\|/\sqrt n\le2H$ and
$\|r(t)\|/\sqrt m\le Y$. The exact readout equation gives

\[
\frac{\|\dot w(t)\|}{\sqrt n}
\le\frac2m\sum_a|r_a(t)|\frac{\|h_a^{(L)}(t)\|}{\sqrt n}
\le4HY.
\]

Since $w(0)=0$, each predictor obeys
$\sup_x|f_n(t,x)|\le8H^2Yt$. On both fitting events,

\[
\sup_{x\in\mathcal X}|f_n(t,x)-\widetilde f_n(t,x)|
\le16H^2Yt. \tag{2}
\]

For every finite $n$, choosing $0<t<C/(16H^2Y\sqrt n)$ contradicts the
requested lower bound directly. No label-shrinking limit is taken.

## What remains distinct

1. A lower bound on $\sup_t\sup_x|f_n-\widetilde f_n|$ requires one witnessing
   time, and does not assert a bound at each time or at the endpoint.
2. An endpoint-only bound concerns $\sup_x|f_n(\infty,x)-\widetilde
   f_n(\infty,x)|$ and is not refuted by (1).
3. A uniform lower bound after a fixed positive, problem-dependent start time
   would avoid (1), but it is an additional unproved problem, not a conclusion
   supplied by the endpoint-only results.
4. A proposed time profile that vanishes at initialization, for example a
   bound proportional to $\min\{t,1\}/\sqrt n$, is not contradicted by
   continuity. It is also not proved here.

## Retained partial analysis of the earlier endpoint question

- `ENDPOINT_IDENTITY.md` gives an exact decomposition of the actual nonlinear
  endpoint into initial-feature interpolation and a training correction,
  together with a fully explicit deterministic cubic-in-label correction
  bound. That absolute bound cannot control root-width fluctuations at fixed
  nonzero label size.
- The separately assigned route notes retain initialization nondegeneracy,
  carefully distinguished random-feature results, and possible covariance
  lemmas. None establishes the requested fully trained endpoint theorem.

These are study results only. The paper, the established book, the old study,
and the Git index are unchanged. No numerical experiment was run.
