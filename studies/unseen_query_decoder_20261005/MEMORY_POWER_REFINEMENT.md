# Exact storage refinements and a packet-encoding obstruction

2026-10-06. Scoped author analysis; no experiment, Git operation, independent
review, or promotion. The conclusions concern the current finite source and
metric witness. They do not establish a lower bound for every decoder with
the same scientific guarantee.

The full memory power remains six. A smaller exact representation of the
scalar noise marks is available, but it does not remove the selected packets,
metric, acquired pair history, or coefficient arrays. More sharply, lossless
compression of the selected packets themselves cannot provide the desired
power reduction: a counting argument below gives an explicit lower bound in
the number of independent packet coordinates. It allows the initialization
algorithm to inspect the complete source and choose its selected rows.

## 1. Fixed contract and the terms that must decrease

Keep the source, finite scalar summaries, original analytic activation class,
full label intersection, fixed depth \(L\ge2\), general spanning
\(m\ge d\) sphere data, and learning in every layer. The target remains the
independently initialized dense-run upper-certificate error, uniformly over
the complete sphere and physical time including the fitted endpoint. The
present analysis changes no physical model or label assumption. Every
retained random bit and peak training/query workspace is counted. Queries
do not reexecute the scalar training recursion.

Use \(R,p,Z,\beta\) exactly as in FAST_LOCAL_COMPOSITION.md. Its internal
memory bound is

\[
 C\{R^2p+(L+1)Rp^2\},\qquad
 R=O(Z^{5/2}),\quad p=O(Z)
 \tag{1}
\]

when the other stated parameters are fixed. The first term is present in
several separately stored objects: selected packet coordinates, the dense
metric, the scalar prefix, and protected coefficient arrays. In particular,
the prescribed complete-pair extension has \(P\) comparable to \(R^2\).
The query-seed and batched-median term alone has power \(9/2\).

Thus reducing only the metric or only the retained query seeds does not
lower the complete power six. Likewise, even deleting the first term of
(1) hypothetically would leave power \(9/2\) under the current seed and
median allowances. This is accounting for this implementation, not a
lower bound on seed length or statistical memory.

For clarity, without absorbing dimension factors into a common envelope,
the two terms in (1) have sufficient bounds

\[
 \begin{split}
 R^2p&\le C\beta^{512L}(m+d+2)^2(d+1)
                   (1+m/\gamma)^5Z^6,\\
 (L+1)Rp^2&\le C(L+1)\beta^{421L}(m+d+2)(d+1)^2
                   (1+m/\gamma)^4Z^{9/2}.
 \end{split}
 \tag{2}
\]

The coefficient 421 is \(201+2\cdot110\). The larger headline envelope
in FAST_LOCAL_EFFICIENCY_RESULT.md covers both terms.

## 2. Coarser retained scalar marks preserve the same rounded summaries

The finite source acquires a scalar on its predetermined grid \(h_a\) as

\[
 C_a=Q_{h_a}(A_a+\eta\widehat E_a),\qquad
 A_a=n^{-1}\sum_i u_a(i;C_{<a})v_a(i;C_{<a}).
 \tag{3}
\]

Here \(h_a\) is either the ordinary grid \(h\) or the innovation grid
\(h_t\), \(0<h_a\le\eta\), and \(Q_{h_a}\) rounds to the nearest
grid point with the prescribed tie rule. Both operands are existing
finite fields with immutable creation-time arguments. The scalar noise
marks have \(|\widehat E_a|\le T_G+1\).

Fix the acquisition failure allocation \(0<\delta_{\rm acq}<1\) and put

\[
 \zeta_a=\frac{\delta_{\rm acq}h_a}{64(P+1)}.
 \tag{4}
\]

Take the finite sampler and rounded metric at the already permitted
tolerances giving, outside sampler failure at most
\(\delta_{\rm acq}/2\),

\[
 \eta|\widehat E_a-E_a|\le\min_b\zeta_b,
 \qquad
 |u_a(I)^T(\widehat M-M)v_a(I)|\le\min_b\zeta_b.
 \tag{5}
\]

The first condition is the source's equation (21a); the second is the
local metric-rounding recipe. The \(E_a\) are the independent Gaussian
ancestors from the proof coupling. No ancestor is supplied to the algorithm.

After source construction, replace only the stored mark by

\[
 \widetilde E_a=Q_{\Delta_a}(\widehat E_a),\qquad
 \frac{\zeta_a}{2\eta}<\Delta_a\le\frac{\zeta_a}{\eta},
 \tag{6}
\]

where \(\Delta_a\) is dyadic. The replacement is computed from the actual
finite mark. It uses no future scalar answer. In compact acquisition use
\(\widetilde E_a\) in place of \(\widehat E_a\), and allow the existing
optional arithmetic error at most \(\min_b\zeta_b\) before rounding.

This modification preserves the complete realized scalar tape on an event
of probability at least \(1-\delta_{\rm acq}\). To prove it, along the
actual source put \(X_a=A_a+\eta E_a\). Conditional on the source array
and earlier marks, \(A_a\) is fixed and \(E_a\) is fresh. The Gaussian
boundary estimate in FAST_LOCAL_PRECISION_TEST.md gives

\[
 \Pr\{\operatorname{dist}(X_a,h_a(\mathbb Z+1/2))
                                      \le4\zeta_a\}
 \le16\zeta_a/h_a=\frac{\delta_{\rm acq}}{4(P+1)}.
 \tag{7}
\]

Union over the \(P\) acquisitions and intersect with (5). If the prefixes
agree, the selected operand values are exactly the source values. The
compact pre-rounding value differs from \(X_a\) by at most

\[
 \zeta_a+\zeta_a+\zeta_a/2+\zeta_a
                 =\tfrac72\zeta_a<4\zeta_a.
 \tag{8}
\]

These four terms are metric error, finite-sampler error, mark compression,
and arithmetic error. The source value differs by at most \(\zeta_a\).
Both values therefore lie in the same rounding cell. Induction proves
literal equality of every scalar summary. Deterministic row evaluation,
coefficient preparation, and the passive algorithm consequently receive
the original scalar prefixes. The passive theorem and its scientific
error are unchanged. The probability allocation can be fitted into the
existing acquisition share by fixed numerical constants.

An exact representation of the coarsened mark uses at most

\[
 C+\log_2(\eta/h_a)+\log_2((P+1)/\delta_{\rm acq})
                    +\log_2(T_G+2)
 \tag{9}
\]

bits, including its range. This is a bit saving, not a word-count change.
In the ordinary-grid choice \(h=\eta/4\), it is
\(O(\log(P/\delta_{\rm acq})+\log(T_G+2))\) per ordinary mark.
For fixed problem parameters this is \(O(\log Z)\). Innovation marks
retain the extra \(\log_2(\eta/h_t)\), which can be \(O(Z)\).
The statement also applies to any finer actual ordinary grid, with its
actual ratio charged in (9); changing that grid after construction would
change the tape and is not proposed.

Even reducing all ordinary scalar-mark storage from \(O(R^2p)\) to
\(O(R^2\log Z)\) would leave the other terms in Section 1. This is an
exact component refinement, not a proof of a smaller full-model power.

## 3. Finite packet coordinates have small atoms

Let \(D\) now denote the actual number of independent first-layer and
innovation Gaussian coordinates in one finite source packet. This is the
packet dimension, not a new substitute for \(R\). Distinct coordinates
and rows are independent under the actual source prior. The finite sampler
couples one coordinate \(\widehat g\) to a standard Gaussian \(g\) with

\[
 |\widehat g-g|\le\epsilon_G\quad\text{on }|g|\le T_G.
\]

For every real \(x\), the event \(\widehat g=x\) is then contained in
\(\{|g-x|\le\epsilon_G\}\cup\{|g|>T_G\}\). Since the standard
Gaussian density is at most \(1/\sqrt{2\pi}\),

\[
 \sup_x\Pr(\widehat g=x)
 \le\frac{2\epsilon_G}{\sqrt{2\pi}}+2e^{-T_G^2/2}.
 \tag{10}
\]

This uses only the sampler coupling, so no injectivity assumption about
its inverse-CDF implementation is needed.

The explicit source choices give a convenient sufficient bound

\[
 \sup_x\Pr(\widehat g=x)\le\vartheta:=\frac1{8n}.
 \tag{11}
\]

Here is the numerical check. Equation (6) of the source bridge has
\(T_G\ge\sqrt{2\log(1024N_G/\rho)}\) and \(N_G\ge n\),
so its contribution to (10) is at most \(\rho/(512n)\).
Equations (17), (20), and (21) there imply
\(\epsilon_G\le\eta/(64\mathcal M)\),
\(\eta\le\xi_0/[64(T_G+1)]\),
\(\xi_0\le\rho/[2^{20}(n+1)]\), and
\(\mathcal M\ge n+1\). Thus
\(\epsilon_G\le\rho/[2^{32}(n+1)^2]\).
With \(\rho<1/4\), (10) is strictly smaller than (11).
Further passive precision requirements only decrease this bound.

## 4. Exact rank cannot remove these coordinates

Let \(G\in\mathbb R^{n\times D}\) be the finite root-coordinate
subtable and suppose \(n>D\). Then

\[
 \Pr\{\operatorname{rank}[\mathbf1,G]<D+1\}
                      \le D\vartheta^{\,n-D}.
 \tag{12}
\]

To verify it, reveal the columns in order, beginning with the constant
column. Before revealing column \(j\), the preceding span has dimension
at most \(j\). For any fixed subspace of dimension \(r\le j\), choose
\(r\) coordinate positions on which restriction is injective. Conditional
on those positions of the new column, each of the remaining \(n-r\)
positions is specified if the column belongs to the subspace. Independence
and (11) bound that conditional probability by
\(\vartheta^{n-r}\le\vartheta^{n-j}\). Sum over \(1\le j\le D\).

SANE_METRIC_PACKETS.md explicitly includes the original Gaussian roots and
fresh innovations in the named field table. Consequently its exact table
rank \(q\) is at least \(D+1\) on the event in (12). This remains true
regardless of the nonlinear training fields added to the table. A low-rank
factorization of its exact full metric therefore cannot discard this
independent root subspace. The result is about the finite table's exact
rank; it asserts no spectral lower bound for every history-field Gram.

## 5. A selection-aware lower bound for lossless packet encodings

Fix the deterministic problem data and finite interpreter. Consider any
representation of at most \(B_{\rm enc}\) retained bits from which a
deterministic decoder can recover \(k\) distinct selected original packets,
including all \(D\) finite coordinates in each. Initialization may inspect
every source packet, every scalar noise mark, and the completed source
tape. It may choose its packets by any rule. All retained advice and
randomness used for recovery are included in \(B_{\rm enc}\); the decoder
has no access to the discarded source array.

For any such representation,

\[
 \Pr\{\text{the selected packets are recovered exactly}
                 \text{ using at most }B_{\rm enc}\text{ bits}\}
 \le 2^{B_{\rm enc}+1}n^k\vartheta^{kD}.
 \tag{13}
\]

Indeed there are fewer than \(2^{B_{\rm enc}+1}\) strings of length at
most \(B_{\rm enc}\), and hence at most that many decoded ordered
packet tuples. For a fixed ordered tuple of distinct row indices, the
probability of any one decoded tuple is at most \(\vartheta^{kD}\),
by independence of its \(kD\) coordinates. Union over decoded tuples
and at most \(n^k\) ordered index choices proves (13). Additional
source randomness or private selection criteria cannot enlarge the event
beyond this union. The count also covers a compact packet generator that
reconstructs the exact finite coordinates on demand.

In particular, recovery with probability at least \(1/2\) requires

\[
 \begin{split}
 B_{\rm enc}
 &\ge kD\log_2(1/\vartheta)-k\log_2 n-2\\
 &\ge k(D-1)\log_2 n+3kD-2.
 \end{split}
 \tag{14}
\]

On the full-rank event, the current metric witness selects at least
\(k=D+1\) rows. Recover just the first \(D+1\) of them to apply (13),
even if its full selected size \(q\) is larger and random. If a proposed
encoding and the full-rank event intersect with probability at least
\(1/2\), it therefore requires

\[
 B_{\rm enc}\ge(D^2-1)\log_2 n+3D(D+1)-2.
 \tag{15}
\]

The failure in (12) tends to zero rapidly in the regime \(D<n\), so
this covers the high-probability exact-packet recovery relevant here.
It does not assume that the selected packets remain independent after
selection; that incorrect assumption is precisely what the factor \(n^k\)
avoids.

The exact statement is in the actual independent-coordinate count \(D\).
When \(D\) is comparable to the actual action/field count \(R\), as in a
schedule with one fresh innovation coordinate per matrix action and only
a constant number of named fields per action, (15) is
\(\Omega(R^2\log n)\). If that actual count has order
\(\log^{5/2}n\), this is order \(\log^6n\). An upper envelope
\(R=O(Z^{5/2})\) alone is not a lower bound on an unspecified actual
schedule; the conditional nature of this last substitution is deliberate.

## 6. What the obstruction leaves open

Equation (15) excludes a power improvement obtained solely by losslessly
encoding the selected original packets in the present exact-table witness.
Changing dense-metric storage to Cholesky factors also retains quadratic
entry count at full rank. These are bounded failures of specific routes.

The bound does not exclude a new representation that produces the same
scalar summaries without recovering selected original packets. Such a
representation must supply the next pair contraction from its current
state, preserve completed-call chronology and the passive finite-history
law, and avoid recomputing earlier scalar training. It must also account
for the pair history and query coefficient workspace. The supplied sources
do not give that alternative construction or a lower bound against it.

No late-time enlargement of the complex radius is used. The missing
variational and conditional-law controls identified in SANE_ADAPTIVE_TIME.md,
Section 5, therefore remain untouched. Temporal analyticity also does not
itself identify the independent finite innovations across calls, which are
the source of the exact-packet obstruction above.

The smallest surviving target for a power reduction is consequently an
aggregate representation that dispenses with exact selected-packet recovery
while preserving the existing summaries, or a newly justified source
schedule with fewer independent innovations. Neither is established here.
The positive refinement (6)--(9) preserves the original tape but does not
change the leading complete memory power.

Complete scoped scientific inputs read: FAST_LOCAL_EFFICIENCY_RESULT.md,
FAST_LOCAL_COMPOSITION.md, SANE_METRIC_PACKETS.md,
FAST_LOCAL_PRECISION_TEST.md, FAST_FINITE_SOURCE_BRIDGE.md,
FAST_FINITE_PASSIVE.md, FAST_TAYLOR_NOISE.md, and SANE_ADAPTIVE_TIME.md.
No linked reports, other studies, or archived book material were read.
The research, rigorous-proof, canonical-notation, and neural-network
instructions were applied. Only this assigned artifact was written.
