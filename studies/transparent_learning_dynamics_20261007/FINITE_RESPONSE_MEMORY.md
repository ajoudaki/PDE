# Finite-width response memory: what can replace the matrices exactly?

2026-10-07. Lead derivation. This note separates a genuine matrix-free causal
construction from two additional claims that do not follow from it: a
population closure, and a transparent compressed autonomous flow. It uses the
exact conditioning lemma in `CAUSAL_GAUSSIAN_ROUTE.md`, rederived below in the
form needed here, and the user-authorized current integrated construction.
There is no literature input. The interpretation and its limitations are new
analysis, not an independent audit of the integrated numerical certificate.

## 1. A useful distinction

A deterministic population limit is not necessary to remove the learned
matrices. An alternative is to retain the realized finite network's response
memory, including its fluctuations. This avoids an unnecessary change of
reference from one particular dense run to its average. It also avoids the
incorrect assumption that an initialized matrix, reused in forward and
backward passes, supplies independent fresh Gaussian fields each time.

The exact construction below is a causal stochastic discrete dynamical
system. Its nonlinearity acts on scalar response histories, its reductions
are named inner products, and its driving inputs are training residuals.
It has no moving dense weight matrix. However, before a separate compression
step it retains width-sized random response records. Their cost must be
counted. Matrix-free is not the same as low-dimensional.

## 2. Setup and the exact force-memory equations

There are \(p\ge m\) declared inputs \(v_a=x_a/\sqrt d\), each of norm one;
only \(a\le m\) has a training label \(y_a\). Their fixed input Gram is

\[
S_{ab}=v_a^\top v_b.
\]

At width \(n\) and hidden depth \(L\), the dense reference is

\[
z_{1,a}=Av_a,\qquad h_{\ell,a}=\phi_\ell(z_{\ell,a}),\qquad
z_{\ell,a}=W_\ell h_{\ell-1,a}\quad(\ell\ge2),\qquad
f_a=\frac1n w^\top h_{L,a},\qquad c_a=y_a-f_a\quad(a\le m).
\]

The loss is \(m^{-1}\sum_{a\le m}c_a^2\). Initially \(A\) has iid
\(N(0,1)\) entries, \(W_\ell\) have independent iid \(N(0,1/n)\) entries,
and \(w=0\). The activation and label qualifications are those of the
reference; none is needed merely for the finite algebra below, except that
the evaluated activations and derivatives exist.

For an Euler step of size \(h>0\), put superscript \(k\) on the quantities
at its start. Define the backward field before its activation gate by

\[
b_{L,a}^k=w^k,\qquad
\delta_{\ell,a}^k=\phi'_\ell(z_{\ell,a}^k)\odot b_{\ell,a}^k,
\qquad b_{\ell-1,a}^k=(W_\ell^k)^\top\delta_{\ell,a}^k.
\]

The physical updates are

\[
\begin{aligned}
A^{k+1}&=A^k+\frac{2h}{m}\sum_{a\le m}c_a^k\delta_{1,a}^k v_a^\top,\\
W_\ell^{k+1}&=W_\ell^k+\frac{2h}{mn}
\sum_{a\le m}c_a^k\delta_{\ell,a}^k(h_{\ell-1,a}^k)^\top,\\
w^{k+1}&=w^k+\frac{2h}{m}\sum_{a\le m}c_a^k h_{L,a}^k.
\end{aligned}
\tag{1}
\]

Define the two-time feature and backward Grams by

\[
C_{\ell;ab}^{s,k}=\frac1n(h_{\ell,a}^{s})^\top h_{\ell,b}^{k},\qquad
D_{\ell;ab}^{s,k}=\frac1n(\delta_{\ell,a}^{s})^\top\delta_{\ell,b}^{k}.
\tag{2}
\]

Write \(G_\ell=W_\ell^0\), and use \(g_{\ell,a}^k\) and
\(\widetilde g_{\ell-1,a}^k\) for the initialized actions
\(G_\ell h_{\ell-1,a}^k\) and \(G_\ell^\top\delta_{\ell,a}^k\).
Summing (1), then applying its matrices to current vectors, gives exactly

\[
\begin{aligned}
z_{1,a}^k&=A^0v_a+\frac{2h}{m}
\sum_{s<k}\sum_{b\le m}c_b^sS_{ba}\delta_{1,b}^s,\\
z_{\ell,a}^k&=g_{\ell,a}^k+\frac{2h}{m}
\sum_{s<k}\sum_{b\le m}c_b^sC_{\ell-1;ba}^{s,k}\delta_{\ell,b}^s,
\quad \ell\ge2,\\
b_{\ell-1,a}^k&=\widetilde g_{\ell-1,a}^k+\frac{2h}{m}
\sum_{s<k}\sum_{b\le m}c_b^sD_{\ell;ba}^{s,k}h_{\ell-1,b}^s,
\quad \ell\ge2,\\
w^k&=\frac{2h}{m}\sum_{s<k}\sum_{b\le m}c_b^s h_{L,b}^s,\\
f_a^k&=\frac{2h}{m}\sum_{s<k}\sum_{b\le m}
c_b^s C_{L;ba}^{s,k}.
\end{aligned}
\tag{3}
\]

There is a direct interpretation of every trained contribution. Sample \(b\)
at time \(s\) writes its backward response into the forward field of a later
sample \(a\), weighted by their earlier/current feature overlap. The reverse
pass has the dual rule: it retrieves the earlier feature, weighted by the
backward-response overlap. The sign and strength of both writes are the
training deficit \(c_b^s\). Passive inputs can receive these writes but never
appear as their training sources.

Equations (3) are not closed until the initialized actions are generated.
In particular, replacing either of them by unrelated Gaussian noise would
change the model even for a linear activation.

## 3. Generating the initialized actions using only response history

At one hidden interface let \(H\) be the columns previously sent forward
through \(G\), with answers \(F=GH\). Let \(D\) be the columns sent in the
reverse direction, with answers \(B=G^\top D\). Here \(H,B\) live in the
lower-layer neuron population, and \(F,D\) in the upper population. These
local capital letters refer to query/answer stacks, not the two-time arrays
in (2). Define \(\langle u,v\rangle_n=u^\top v/n\), including its
matrix-valued extension, and let \(P_H,P_D\) be the Euclidean orthogonal
projections onto the two query spans. All inverses in this section are
Moore--Penrose inverses; no positive history gap is assumed.

For a new forward query \(u\), set

\[
\begin{aligned}
a&=\langle H,H\rangle_n^\dagger\langle H,u\rangle_n,
&u_\perp&=u-Ha,\\
b&=\langle D,D\rangle_n^\dagger\langle B,u_\perp\rangle_n,
&\sigma^2&=\langle u_\perp,u_\perp\rangle_n.
\end{aligned}
\]

Then its exact conditional distribution is

\[
Gu=Fa+Db+\sigma(I-P_D)\xi,
\qquad \xi\sim N(0,I_n)
\tag{4}
\]

with \(\xi\) independent of the prior transcript. The reverse formula
is obtained by exchanging \(H,F\) with \(D,B\). Empty stacks give zero
terms. A zero innovation variance gives no fresh contribution. Projection
of the fresh vector can itself be evaluated using its overlaps with \(D\).

For clarity, (4) follows from the Gaussian posterior

\[
G=FH^++D(D^\top D)^\dagger B^\top(I-P_H)
 +(I-P_D)\widehat G(I-P_H),
\tag{5}
\]

where \(H^+=(H^\top H)^\dagger H^\top\) and \(\widehat G\) is an
independent iid Gaussian matrix with entry variance \(1/n\). The affine
mean satisfies both observed constraints because \(D^\top F=B^\top H\).
It is orthogonal to the homogeneous constraint space
\(\{(I-P_D)M(I-P_H):M\}\). Isotropy of the Gaussian matrix therefore
gives (5), and applying it to \(u\) gives (4). The algorithm uses (4), not
the unmaterialized matrix in (5).

This remains exact for adaptive queries. Conditional on past observations,
the next query is fixed and its answer is one more linear observation of the
Gaussian remainder. Induction also preserves the conditional independence
of the remainders of distinct initialized matrices. Auxiliary randomness
must be independent of those remainders, and unrevealed matrix entries may
not be used to choose a query.

The three terms of (4) have different meanings:

1. \(Fa\) repeats the already known response to the part of the input
   lying in its previous forward span.
2. \(Db\) is the cross-direction correction imposed by previous backward
   observations. It is not an optional small perturbation.
3. The projected innovation supplies only the still-unobserved part of the
   initialized operator, respecting every earlier reverse observation.

Thus the initialized operator is a source of **reciprocal response memory**,
not a sequence of independent random kernels. Equations (3) describe newly
learned associations; (4) describes reuse of the initial associations.
These two mechanisms must not be merged.

## 4. Exact finite-step realization and its information cost

**Finite-step theorem.** Fix any finite number \(N\) of Euler steps and a
fixed chronological order for the forward and backward calls. Initialize
the first-layer fields by independent Gaussian rows of covariance \(S\).
Evaluate (3) forward in layer order, then compute the output, residual, and
backward fields in reverse layer order, generating every initialized action
by (4). The resulting joint law of all fields, pairings, and predictions is
exactly the joint law of the dense Euler computation (1).

The proof is induction over the calls. The first-layer Gaussian law equals
that of \(A^0[v_1,\ldots,v_p]\). Given an identical transcript, (4) is the
correct conditional law for its next initialized-matrix action. All other
operations are the identical deterministic nonlinear evaluations, contractions
and rank updates in (1)--(3). Induction identifies the complete joint law.
Equivalently the two computations admit a coupling with identical transcripts.
This statement concerns Euler iterates, not yet continuous gradient flow.

At fixed \(N,p,L\), a call adds one Gaussian response vector and scalar
coefficients computed from named pairings. Every neuron coordinate is a
scalar program applied to that coordinate's independent Gaussian roots and
innovations. Globally acquired coefficients are shared between coordinates;
they can depend on all coordinates through the earlier pairings. This
adaptivity does not invalidate the exact posterior induction.

There are \(O(LpN)\) call fields and \(O(Lp^2N^2)\) scalar pairings and
coefficient entries. The initial first-layer panel can be represented with
at most \(\operatorname{rank}S\le\min(d,p)\) independent roots per neuron.
The uncompressed primitive random record consequently has size

\[
O\bigl(n[\min(d,p)+LpN]\bigr)
\]

real numbers. Storing the response vectors has the same width dependence.
If the random record is supplied by a restartable external random oracle,
that oracle is part of the fixed information cost; it is not free compressed
storage. A short finite-bit seed cannot be asserted to generate these exact
independent real Gaussian vectors. Any short-seed replacement needs its own
finite-precision approximation theorem.

No \(n\times n\) learned or initialized matrix is explicitly retained.
When the query histories leave a nonzero Gaussian remainder, that unobserved
component is not encoded. If sufficiently many queries span the input space,
the transcript can determine the whole matrix; no information reduction is
claimed in that case. At fixed query count and growing width, the construction
is a substantive response reduction, but not logarithmic compression by itself.

## 5. What the integrated logarithmic construction can supply

The authorized integrated document's finite-source construction, specifically
(FC.28)--(FC.53), uses a noisy regularized version of (4), finite scalar
arithmetic, and selection of a small set of row packets with a bilinear
metric. Its initialized-matrix posterior is a Sylvester solve on the history
Grams. The positive observation-noise floor removes singular-inverse problems.
The induced physical perturbation and chronological coupling are separately
charged in that source proof. Removing the noise while retaining its finite
precision claims would not be justified.

Here is the elementary part of that reduction, stated without importing its
error theorem. For a completed finite field table \(V\in\mathbb R^{n\times R}\)
of rank \(q\le R\), choose independent columns and \(q\) rows whose square
intersection is invertible. There is a matrix \(C\in\mathbb R^{n\times q}\)
with

\[
V=C V_I,\qquad C_I=I_q,\qquad
M=C^\top C/n,\qquad V^\top V/n=V_I^\top M V_I.
\tag{6}
\]

This follows by expressing every column in the chosen column basis and
recovering its coordinates from the selected rows. It preserves every
pairing in the table, including mixed response pairings. The selected row
packets and \(M\) cost \(O(R^2)\) scalars when each packet has \(O(R)\)
entries. Future scalar answers need not be stored: they can be recomputed
from the selected packets and \(M\) if the same scalar prefixes are reproduced.
Finite rounding with independently smoothed acquisition boundaries is how
the integrated source obtains literal prefix replay at a finite precision.

There are three important qualifications.

- The selection and metric in (6) depend on the completed source field
  table. The metric is not an oblivious input-geometry quadrature rule.
- Exactness for this table does not imply exactness for counterfactual labels,
  a different control history, or new row functions. Such fields need separate
  span or approximation arguments.
- In the probability proof, the private selected metric must not be included
  in the conditioning history used to derive the Gaussian posterior. It
  contains future-table information. The source posterior is proved first;
  deterministic replay of its finite scalar prefixes is proved afterward.

Consequently, using that existing construction could transfer its dense
accuracy certificate to a Gram-program implementation. It would not by itself
prove a universal autonomous law on arbitrary Gram states, or establish that
all its data-dependent fixed information has an immediate mechanistic meaning.
Its coefficient provenance is computed setup, not a freely supplied dense
trajectory oracle, but it remains trajectory-specific setup. Whether that
constitutes the explanatory formulation sought by the user cannot be decided
merely by observing that no future scalar answers are stored.

## 6. All-time accuracy and the remaining scientific distinction

The finite-step theorem does not provide an Euler step size or an all-time
error estimate. An accurate source integrator can replace Euler: its matrix
calls remain predictable, and the same posterior argument applies when its
Taylor-coefficient or stage fields are added to the named-field program.
If a specified finite implementation has a proved coupling error at most
\(\varepsilon\) to the dense flow on the declared panel, its exactly replayed
implementation has that same error. This is a conditional transfer theorem,
not a proof of the numerical premise.

The integrated source supplies a particular analytic finite program and
claims all-time dense comparison, including its final frozen tail. This note
has inspected the local posterior and replay interfaces cited above, not
audited every analytic, finite-word, short-seed, or whole-sphere premise of
that result. No headline exponents or unconditional inherited PASS are being
declared here.

The most useful new explanatory statement is the distinction between two
forms of memory: training writes rank-one forward/backward associations (3),
while Gaussian reciprocity carries the cross-direction response correction
(4). A population approximation that retains the first and discards the
second is already wrong at the first nonzero backward sweep. A compressed
realized-history model must retain both, plus the nonlinear coactivation
information in its scalar response law.

This is a promising non-neural dynamical description, but not yet a completed
solution of the broad research contract. The next decisive question is whether
its data-dependent response law admits an autonomous, directly observable
closure with controlled error on the original all-time scope, without using
trajectory-specific table replay as the reason it works.

The finite-step algebra, conditional law and counts passed the scoped internal
check in CAUSAL_FINITE_AND_OBSTRUCTION_AUDIT.md. This version incorporates its
training-index and spanning-history qualifications. That check did not audit
the inherited integrated numerical/replay certificate.
