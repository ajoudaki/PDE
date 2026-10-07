# Implicit Gaussian setup for the same Harmonic model

2026-10-06. End-to-end synthesis of this study's user-requested lower-cost
Harmonic initialization investigation. Complete component proofs, separate
reconstruction checks and the combined-interface audit have passed. This is
internally checked research, not a promoted result or a finite-precision
implementation.

## Contract and scope

The user expressly permits a fresh dense reference that is never
materialized. The target is to sample the same joint law as ordinary iid
Gaussian dense initialization followed by the checked finite Harmonic setup,
using only an implicit representation of the initialized hidden matrices.
An already supplied dense weight array or prescribed coordinatewise random
seed is not an input. The method must not replace the dense Gaussian law,
discard its unexplored component, freeze features, change the training metric,
or relax the original label, activation, whole-sphere/all-time error or
retained-storage scope.

The desired gain concerns setup arithmetic and peak setup memory. All
internal resolutions and their structural dependence must be displayed.
First-layer arrays, input data, Gaussian draws, scalar/activation evaluations,
source projection, coordinate selection, final metrics and mixer assembly
must be charged. The exact-real convention of the inherited result remains;
bit complexity, finite-precision rank decisions and practical conditioning
must not be silently claimed. No new small-label assumption is permitted.

This is the implementation/coupling continuation of the same investigated
setup algorithm, whose explicitly materialized execution is already checked
in LOCAL_SETUP_RESULT.md. It is not a new population approximation or a new
prediction theorem. The original RESULT.md remains unchanged until the
new result is fully checked and any integration is explicitly accounted for.

## Inputs, ownership and proof obligations

Scientific inputs are this study's RESULT.md, the complete relevant local
Taylor/activation/assembly and prior stability/quadrature notes, and the
maintained docs/ notation and Gaussian-reuse material. No other study,
archived book, prior unrelated task or unpromoted external study is an input.
The Gaussian sampling lemma will be proved directly in finite dimension;
no asymptotic state-evolution theorem is used to justify a finite transcript.

The original integrated result is bound to SHA-256
`c2cbd1bb0e6a39de87181df89be977eaf2e272fda4f1459ac934396d84e1b278`.
The explicit execution bridge is bound to
`dedba0b570d6a73b5c9eabbd414953d01fdc6d46056de023748eede621c64f2b`.
Their original scope and exact-real qualifications are inherited, not
replaced by a distributional similarity claim about separate predictors.

| Obligation | Assigned artifact | Status |
|---|---|---|
| Exact adaptive forward/transpose Gaussian sampler, interleaved layers, stopping and completion | IMPLICIT_GAUSSIAN_SAMPLER.md | Complete; reconstruction PASS |
| Same finite algorithm without dense materialization; all supplied-order costs | IMPLICIT_HARMONIC_EXECUTION.md | Complete; corrected convention checked, PASS |
| Explicit order recipe from structural/activation parameters and source accuracy | IMPLICIT_SETUP_ORDERS.md | Complete; reconstruction PASS |
| End-to-end joint-law coupling, error/storage inheritance, final cost synthesis | This document | Complete; combined audit PASS |

The root owns this result and README. The sampler and execution authors
started with fresh scoped contexts and separate files. The order-interface
author has disclosed prior authorship/checking of this study's assembly
arguments. Current candidates were not shared between them until frozen.
Separate reconstruction checks followed complete candidates. These are internal
research checks, not promotion reviews. No Git mutation, book/paper change or
neural-training experiment is authorized or planned in this round.

The additional canonical-notation skill remains inaccessible at its prescribed
path. The accessible proof/research skills, maintained notation contract and
user's explicit minimal-notation requirements are applied; access to unread
instructions is not claimed.

## Required success and failure criteria

Success requires one latent jointly iid dense initialization for which the
entire numerical setup transcript and final compressed arrays equal those of
the already checked explicit algorithm. This must hold under adaptive
queries, repeated/dependent directions, both transpose directions and
interleaved layers. It then transfers the existing prediction theorem under
the original event; no new approximation error or failure allowance should
be needed. Counts must include the information retained by the sampler and
the history of learned low-rank increments.

An independent Gaussian answer to each query, an uncharged full matrix or
Gram construction, a source-event test requiring unavailable matrix norms,
or a coupling that fails to include the final selected model is a failure.
Proving only individual product marginals or only a fixed finite number of
queries is insufficient. The bounded finite transcript theorem must apply
at the actual width-dependent query count.

Near-linear means n times explicitly qualified polylogarithmic factors at
separately fixed structural parameters. It is not strict O(n), uniformity in
growing dimension/data/depth, or a claim that a requested quadratic-size
output can be written in linear work. A sufficient explicit parameter
recipe with large factors must remain visible rather than being hidden in
fixed-parameter notation.

## 1. Main theorem: exact reference law, near-linear setup

Fix the training data, sample count \(m\), input dimension \(d\ge1\),
hidden depth \(L\ge2\), positive population feature-Gram gap \(\gamma\),
label RMS \(Y=\|y\|_2/\sqrt m>0\), and activations satisfying the original
strip-analytic assumptions. Activation values need not be bounded. Keep the
full original small-label interval, not just its smaller beta-power sufficient
subinterval. Fix a confidence \(0<\delta<1\). The exact label formulas and
all width qualifications are in Sections 1--4 of
[the complete order recipe](IMPLICIT_SETUP_ORDERS.md).

For each sufficiently large individual width \(n\), there is an algorithm
producing the same finite Harmonic model as the checked explicit setup, jointly
with an implicit dense Gaussian reference of width \(n\). Its output and
reference have exactly the ordinary joint law. Thus, with probability at least
\(1-\delta\), the unchanged whole-sphere/all-time prediction certificate
holds, including the fitted limit. No new approximation error or failure term
is incurred by implicit execution.

In particular, choose the original source horizon and tolerance

\[
T=32\frac m\gamma\log(en),\qquad \eta=\frac1n.
\tag{1}
\]

Let \(a\) be the activation strip half-width, \(b\) a bound on
\(|\phi_j(0)|\), and \(s,t_2\ge1\) the original valid half-strip first-
and second-derivative bounds. Define the same activation envelope

\[
\beta=\max\{10,1+b,16/a,s,t_2\}.
\]

A fully numerical, generally nonminimal error bound inherited from RESULT is

\[
\begin{split}
\sup_{t\in[0,\infty]}\sup_{\|x\|_2=\sqrt d}
 |f_H(t,x)-f_n(t,x)|
\le{}&\frac{Ym}{\gamma}\left(1+\sqrt{\frac m\gamma}\right)
\left[
\frac{2000e^{44}\beta^{42L}}n
 (1+\sqrt{\log(en)})e^{64\sqrt{\log(en)}}
+236\beta^{9L}(en)^{-8}
\right].
\end{split}
\tag{2}
\]

This uses the full-interval numerical prefactor and tail bounds, not the
optional smaller-label refinement. The exact recurrence certificate can be
smaller. For general supplied \(T,\eta\), it remains precisely the
Harmonic horizon-and-tolerance certificate in RESULT; this note does not
replace that certificate by a width-only bound.

At separately fixed admissible \(m,d,L,\gamma,Y\), activation envelopes
and confidence, the sufficient costs at (1) are

| Quantity | Bound |
|---|---|
| Setup work, bounded-cost scalar primitives | \(O(n\log(en)^{9d/2+3})\) |
| Peak setup memory, exact real words | \(O(n\log(en)^{3d/2+1})\) |
| All retained Harmonic storage | \(O(\log(en)^{3d+2})\) |
| Whole-sphere/all-time prediction error | The bound (2), hence \(n^{-1+o(1)}\) |

Only this asymptotic table fixes structural parameters. The finite counts in
Section 3 have absolute big-O constants and expose them through every supplied
order; their full deterministic recipe is linked in Section 4. For the circle
\(d=2\), the table gives work \(O(n\log(en)^{12})\), peak memory
\(O(n\log(en)^4)\), and retained storage \(O(\log(en)^8)\).
These are sufficient, conservative bounds, not claims that the log powers are
optimal or that the prescribed constants are practical at moderate widths.

The statement is near-linear \(n^{1+o(1)}\), not strictly \(O(n)\).
It is also not uniform linear scaling when dimension, depth, data size or
inverse gap grow with width. In particular the first matrix alone uses
\(nd\) words, and tensor-product spatial quadrature retains its dimension
dependence. The cases \(Y=0\) and full-width retention keep their original
separate definitions; the latter does not have a subquadratic output size.

## 2. Construction and proof of the joint-law theorem

The explicitly initialized first layer has \(nd\) independent standard
normal entries. Each of the \(L-1\) hidden mixers has independent
\(N(0,1/n)\) entries; their whole arrays are not generated. The readout is
exactly zero. These are the original dense initialization and normalizations.

**Exact Gaussian actions.** For each hidden mixer, retain orthonormal bases of
the already queried forward and transpose directions and their returned images.
For a new direction, its projection onto the observed span has a known image.
Only the orthogonal new component needs randomness. Sample that component in
the complementary output span, with the conditional mean forced by the opposite
direction observations. The complete finite-dimensional construction and
Gaussian independence proof are in
[IMPLICIT_GAUSSIAN_SAMPLER.md](IMPLICIT_GAUSSIAN_SAMPLER.md).
For \(k\) requests, its arithmetic is at most \(4nk^2+6nk+2\),
draws at most \(n\min(k,2n-1)\), and memory at most
\(2n\min(k,2n)+8n+5\min(k,2n)+64\) words. These are pathwise
counts, without nondegeneracy or conditioning hypotheses.

The proof conditions on the full global transcript, not only on one layer's
history. The unexplored remainders of different layers remain conditionally
independent. It handles either multiplication direction, adaptive interleaving,
dependent queries, exact zero queries and bounded adaptive stopping. Completing
the unobserved remainders at the end is a mathematical coupling only; those
entries are never generated as part of setup.

**Factored numerical training increments.** The original dense hidden update is

\[
\dot W^{(j)}=-\frac2{mn}\sum_{a=1}^m
 (f_n(x_a)-y_a)\,\delta_a^{(j)}h_a^{(j-1)T}.
\]

For a degree-\(K\) Taylor panel, group its finite endpoint increment into
at most \(mK\) outer products. At panel \(b\), its anchor therefore has
the exact representation

\[
W_b^{(j)}=W_0^{(j)}+A_b^{(j)}B_b^{(j)T},
\qquad A_b^{(j)},B_b^{(j)}\in\mathbb R^{n\times bmK}.
\tag{3}
\]

Here the two factors are local proof notation, not the first-layer matrix.
Both forward and transpose anchor actions use the Gaussian sampler for
\(W_0^{(j)}\) and ordinary contractions for the factors. The nonconstant
parameter jets also act by factored contractions. This is an identity for the
finite Taylor algorithm, not an assertion that the exact continuous trained
increment has rank \(mK\). No dense anchor update is materialized.

**Unchanged source and final model.** Compute the exact original-activation
initialized features, then the checked polynomial-activation local setup.
Stream passive spatial queries into the same global Chebyshev--harmonic modes.
Panels do not create extra retained source modes. Request initialized matrix
images of the completed coefficient vectors and of the final basis columns.
These preserve exact source/image pairing and the original small mixer formula.
The original coordinate selector, metrics, initialized weights, solve caches
and original runtime activations are unchanged. Every temporary sampler,
history, source and basis array is discarded afterwards.

**Finite-program coupling.** Fix the explicit algorithm's generator order,
scalar routines, rank conventions and selector tie-breaking. Complete any
undefined off-event inverse branch by a deterministic failure return. The
program has a deterministic query bound obtained from (4) below by replacing
the output-dependent \(r\) by \(\min(n,R)\). Apply the sampler theorem
at that deterministic bound. Under its joint completion, induction over all
scalar operations and queries identifies every computed jet, source coefficient,
basis, selected index, metric and final mixer with the explicit algorithm's.
The rank-factor identities justify regrouping; exact real arithmetic makes
these regroupings equal. An off-event failure branch is reproduced as well.

It follows that the full dense initialization and compressed output have the
same joint law as in explicit setup. The original event is a property of that
latent initialization. It need not be computable from the transcript: equality
of joint laws transfers its probability and deterministic comparison conclusion.
In particular no source-event rejection, matrix-norm test, new union-bound loss,
or observed-trajectory oracle is needed. This proves the theorem, including
the same whole-sphere/all-time error rather than merely agreement at setup nodes.

## 3. Full supplied-order cost interface

The following symbols are local to this cost interface. They are kept separate
because their roles and costs differ.

| Symbol | Supplied or computed quantity |
|---|---|
| \(J,K,D\) | Number of local panels, Taylor degree, temporary activation-polynomial degree |
| \(p,\ell_*\) | Largest temporal Chebyshev and spherical degrees |
| \(N_t,N_x\) | Time and spatial quadrature node counts |
| \(H_{\rm sph},N\) | Spatial basis count and retained joint-mode count |
| \(R=2m+d+1+4N\) | Sufficient per-layer source generator count |
| \(r\le\min(n,R)\) | Largest actual source rank |
| \(q\le9r\) | Largest actual selected support, without padding an unused budget |

For \(d=1\), there are two spatial points, \(H_{\rm sph}=N_x=2\),
\(N=2(p+1)\), and no spherical degree. Use \(n\ge\max(m,d)\),
as in the common cost interface. Define the single query-count abbreviation

\[
k_*=m+2J(m+N_x)(K+1)+2N+r.
\tag{4}
\]

Its four terms are exact initialized training actions, all local training and
passive forward/transpose actions, completed coefficient images, and final
basis images. A rigorous deterministic upper budget replaces \(r\) by
\(\min(n,R)\). A posteriori costs can use (4) by the pathwise sampler count.

The exact arithmetic envelope is

\[
\begin{split}
O\bigl(&nd(1+m)+m^2d+nm^2+m^3+L+d+m+1+L(D+1)^2\\
&+(L-1)nk_*^2
 +(L-1)nm(m+N_x)J(J-1)K(K+1)\\
&+J[nd(m+N_x)+dmN_x]
 +JLm(m+N_x)(K+1)^2(n+K+1)\\
&+JLn(m+N_x)(D+1)(K+1)^2\\
&+(N_t+J)(p+1)(K+1)
 +LnJ(K+1)(N_xH_{\rm sph}+N)\\
&+LnRr+Lnr^3+(L-1)nr^2
 +L(qr^2+r^3+q^2r)+qd\\
&+G_{\rm time}+N_t\log(2+N_t)\bigr).
\end{split}
\tag{5}
\]

The matching peak resident real-word bound is

\[
\begin{split}
O\bigl(&nd+(L-1)n[k_*+JmK]+Lmn(D+1)(K+1)\\
&+Lm^2(K+1)^2+LnR+Ln(K+1)H_{\rm sph}\\
&+Lq^2+q(d+Lm+1)+m^2+m(d+1)\\
&+L(D+1)+(p+1)(K+1)+N_t+J
 +G_{\rm memory}+L+d+m+1\bigr).
\end{split}
\tag{6}
\]

There is no structural factor hidden in the big-O constants of (5)--(6).
For the quadrature with azimuthal order \(N_\varphi\), polar order
\(N_\theta\), and \(N_x=N_\varphi N_\theta^{d-2}\) when
\(d\ge3\), the geometric terms are explicitly

\[
G_{\rm time}=
\begin{cases}
N_t+J,&d=1,\\
N_t+N_x+JN_x(\ell_*+1),&d=2,\\
N_\theta^2+dN_\theta+N_t+N_\varphi+d+d(\ell_*+1)^2
+JdN_x[1+(\ell_*+1)^2+H_{\rm sph}],&d\ge3,
\end{cases}
\]
\[
G_{\rm memory}=
\begin{cases}
N_t+1,&d=1,\\
N_t+N_x+\ell_*+1,&d=2,\\
dN_\theta+N_t+N_\varphi+d[1+(\ell_*+1)^2+H_{\rm sph}],&d\ge3.
\end{cases}
\]

The complete term-by-term implementation is equations (23)--(28) of
[IMPLICIT_HARMONIC_EXECUTION.md](IMPLICIT_HARMONIC_EXECUTION.md).
Those geometric counts include quadrature-weight construction, repeated spatial
point generation and separated harmonic evaluation; they are not a free oracle.
In particular spatial values are regenerated each panel, a time/memory choice
consistently charged in both bounds. The \(nm^2+m^3\) terms allow formation
and factorization of the exact initialized training Gram/readout cache.

Separately charge the following primitive calls:

\[
\begin{aligned}
\text{standard Gaussian draws}&\le nd+(L-1)nk_*,\\
\text{original real activation values}&\le Lnm+4L(D+1),
\end{aligned}
\tag{7}
\]

with at most \(L\) extra activation values if the supplied envelope does
not already contain \(\phi_j(0)\). For the elementary-function count,
define the local angular table size as zero for \(d=1\), \(N_x\) for
\(d=2\), and \(N_\theta+N_\varphi+d(\ell_*+1)^2\) for
\(d\ge3\). The number of elementary evaluations is at most a numerical
constant times

\[
L+d+m+1+L(D+1)+N_t+\text{angular table size}
+(L-1)k_*+Lr.
\]

These include scalar parameter preparation, angular normalizations,
trigonometric nodes and sampler/source-basis square roots. Multiply each
primitive class by its actual per-call cost, or sum the nonuniform call costs,
and add its peak scratch to (6); execution equation (32) makes this convention
explicit. Analyticity
does not imply a constant-time activation evaluator. Population moments and
the positive gap are theorem inputs/certificates, not silently computed for free
from arbitrary function descriptions.

All retained storage is unchanged, and in particular is at most

\[
1020(L+1)R^2+10m(d+1)
\tag{8}
\]

real coordinates in the established sufficient inventory. The learned-state
inventory is at most \((L-1)q^2+q(d+1)+m\). These are runtime inventories,
not the peak setup memory in (6). No unobserved Gaussian completion or query
oracle is retained in the final model. Its later training/query cost interface
is exactly RESULT's existing Harmonic interface.

## 4. Every order's structural dependence

[IMPLICIT_SETUP_ORDERS.md](IMPLICIT_SETUP_ORDERS.md) supplies the complete
rounded finite recipe, in this order:

1. Activation envelopes, original source/fitting recurrences and full label
   interval; no smaller label cap is substituted.
2. Explicit initialization gates, original analytic gates and the separately
   disclosed existential stochastic source-width threshold.
3. Time/input analytic radii, weighted-simplex source modes, exact harmonic
   multiplicities, source rank bound and sufficient selected budget.
4. Positive temporal, azimuthal and polar quadrature, including their tensor
   product and the separate \(d=1\) case.
5. Numerical restart/stability constants, source nodal tolerance, real-value
   activation polynomial, local Taylor degree and panel count.

The formulas depend only on \(n,m,d,L,\gamma,Y,T,\eta\), the original
activation bounds/certificates, and ordinary explicit scalar operations. The
confidence \(\delta\) enters the width qualification, not a new sampling
failure allowance. Bounds involving \(\beta\) are supplied as conservative
envelopes; beta alone does not recover an arbitrary activation's exact Gaussian
moments, evaluator cost or the unquantified stochastic width onset. All these
qualifications are visible in the recipe rather than absorbed into (5).

At (1) and separately fixed admissible parameters, that recipe yields

\[
J=O(\log(en)^{3/2}),\quad K=O(\log(en)),\quad
D=O(\log(en)^{3/2}),
\]
\[
p+1,N_t=O(\log(en)^{5/2}),\quad
\ell_*=O(\log(en)^{3/2})\quad(d\ge2),
\]
\[
N_x,H_{\rm sph}=O(\log(en)^{3(d-1)/2}),\qquad
N,R,r,q,k_*=O(\log(en)^{3d/2+1}).
\tag{9}
\]

Substituting (9) into (5), the conservative selector term \(Lnr^3\)
dominates every other width-proportional term. The latter have exponents at
most \(3d+2\), \(3d/2+7/2\), or \(3d-1/2\), all no larger
than \(9d/2+3\) for \(d\ge1\). The remaining terms are fixed powers
of \(\log(en)\), hence eventually smaller than the displayed width term.
In (6), sampler and source arrays have exponent \(3d/2+1\); history and
online activation arrays have exponent \(5/2\), which is no larger for
\(d\ge1\). This proves the main cost table without omitting temporary
history or projection buffers. For \(d=1\), the two-point convention gives
the same conclusion directly.

## 5. What has closed, and what has not been claimed

The implicit-reference question is closed at the original theorem's exact-real
level: there is one ordinary latent dense initialization, a finite executable
matrix-action program with all accesses charged, a joint-law proof for the final
Harmonic model, explicit deterministic orders/costs at admissible width, and
unchanged accuracy/storage/label qualifications. No original trained reference
or hidden \(n^2\) array is supplied for free.

The following are not consequences and are not described as proved:

- A linear-time conversion of an already supplied dense matrix or prescribed
  entrywise random seed; the user authorized a freshly sampled implicit reference.
- Strict \(O(n)\) setup, optimal log powers, dimension-free spatial quadrature,
  or uniformly polynomial dependence in every structural parameter.
- A numerical confidence-to-width bound beyond the inherited source theorem.
- A finite-bit implementation, stable approximate rank decisions, or finite-
  precision Gaussian conditioning. Exact original initialization values and
  exact-real Gaussian draws remain the original primitive conventions.
- A speedup over every possible implicit dense solver. The same Gaussian action
  device can accelerate other algorithms. The distinct Harmonic benefit is
  that the final model discards all width-dependent transcripts and history.

The accessible proof-search and rigorous-math workflows determined the separate
coupling, execution and parameter audits; they do not promote this study into
the maintained book. No commit or book/paper change is made in this round.

## 6. Version-bound checks and closure record

The root read the complete sampler, execution, order recipe and all three
check reports, reconstructed the central posterior/low-rank identities and
checked the copied error/cost formulas. Separate component checks and the
combined synthesis check are recorded here:

| Scope | Check | Frozen scientific input |
|---|---|---|
| Sampler and finite execution | [Reconstruction](IMPLICIT_GAUSSIAN_EXECUTION_CHECK.md) | Sampler `24eb0ab622156cd073bfdf457c3746bc02523bfac551e03f47bb8265206efd57`; execution `fe3e6dbcde65c050f63d58a6b8995c423d9fd1e2c87eddac8ad2fb391dc6ccf5` |
| Every deterministic order and full original qualification | [Orders check](IMPLICIT_SETUP_ORDERS_CHECK.md) | `3f5ff8a63c97ea76dda4890b0f464f05e8bb8576760cde93ff1f4c18d00a6009` |
| Complete joint-law/error/cost synthesis | [Integration check](IMPLICIT_SETUP_RESULT_CHECK.md) | This document before status-only changes and this closure record: `62aa72aa090e86439f075e218765ea2b97c833b6e523dfbb3ebb87653f368839` |

The execution audit found and corrected an omitted raw-Taylor-to-affine-panel
coefficient rescaling. It also made the deterministic query cap explicit when
the actual source rank is random. Neither correction changes the prescribed
orders, cost bounds or approximation guarantee. The order audit requested an
explicit restatement of the original full-strip derivative hypothesis; no
scope or order was tightened. The final integration audit required no scientific
correction. No issue remains open inside the stated conditional exact-real
setup theorem; the limitations in Section 5 remain outside that theorem.

Root mechanical checks cover paired mathematical delimiters, unique equation
tags, control characters, local-link existence and scoped whitespace. The
original RESULT.md still has hash
`c2cbd1bb0e6a39de87181df89be977eaf2e272fda4f1459ac934396d84e1b278`.
No timing benchmark, training experiment, empirical success-rate claim, full
Markdown/TeX rendering or finite-precision implementation was performed.
All new setup work remains uncommitted in this study.
