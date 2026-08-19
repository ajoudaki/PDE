# Non-closure for the quadratic mean-field \(\mu\)P MLP

> **Historical synthesis; corrected claim status.** This document preserves
> the quadratic-nonclosure arguments, but its earlier headline classifications
> have been superseded.  In particular, the tagged-site Volterra/DMFT equation
> was postulated rather than derived from the finite network, and the step loss
> additionally uses a monotone, no-overshoot relaxed selection.  The resulting
> no-positive-delay argument is therefore an exact **conditional
> implication**, not an unconditional result about the network's mean-field
> dynamics.  Likewise, the special quadratic compiler now establishes an
> exact formal annealed fixed-order jet, but concentration of the random
> derivatives and identification with derivatives of an actual positive-time
> infinite-width trajectory remain separate.  For the current derivative
> calculus and exact fixed-order certificates, use the
> [mean-field-peeling report](../mean_field_peeling/CURRENT_RESEARCH_STATE.md).
> For the current output-kernel moment conjecture, use the
> [Stieltjes report](../stieltjes_conjecture/CURRENT_RESEARCH_STATE.md).

## Unified statements, proof chains, scope, and source provenance

### Executive conclusion

The repository does **not** currently contain an unconditional positive-time
non-closure theorem for the actual infinite-width quadratic network.  It
contains exact finite-width identities, an exact formal annealed derivative
compiler for the special quadratic model, several topology and restricted
hierarchy obstructions, and the following conditional DMFT implication:

> **If** the fully trained infinite-width network is represented by the
> asserted tagged-site Volterra equation with its independence, continuity,
> positive-response, and output identities, **and if** the monotone,
> no-overshoot relaxed selection is adopted, then its selected loss trace is
> \[
> \mathcal L_{\mathrm{rel}}(0)=1,
> \qquad
> \mathcal L_{\mathrm{rel}}(t)=0\quad(t>0).
> \]
> Consequently, every continuous finite-dimensional autonomous closure has
> uniform error at least \(1/2\); if it matches the correct initial loss, its
> uniform error is at least \(1\).

The Volterra comparison and the elementary continuity lower bound are exact
once those hypotheses are granted.  What is missing is not merely uniform
finite-width convergence: the report does not derive the asserted tagged-site
equation, prove its self-consistency for this network, construct a classical
positive-time solution, or show that the relaxed selection is forced.  The
conditional implication therefore cannot be used as evidence that the actual
network loss is discontinuous or that the broad finite-PDE question is
settled.

The strongest unconditional statement about the ordinary Taylor compiler is
instead a statement about its **formal annealed fixed-order jet**:

> The exact quadratic peeling/Wick coefficients have radius zero. Their
> positive degree-\(M\) source profiles diverge at every positive feature
> time, and their residual-clock loss curves form an initial boundary layer.
> Hence the precise iterated global-shadowing conjecture for that one-source
> Taylor family is internally inconsistent.  This does not construct or
> identify a positive-time mean-field loss curve; a claim about a typical
> limiting network jet additionally needs concentration and interchange of
> width limits with time differentiation.

No result in the repository proves that **every** signed, nonanalytic,
non-Taylor, accuracy-dependent real-axis finite compiler is impossible. The
reports explicitly preserve that distinction.

---

## 1. First list: every non-closure or no-go result found

The following list separates distinct mathematical statements instead of
combining them under the ambiguous phrase “no finite PDE.”

| ID | Result | Exact force |
|---|---|---|
| N1 | **No finite ordinary degree/rectangular monomial-moment cutoff is invariant in the displayed frozen reductions.** Their equations send \(M_{p,r}\) to moments with larger \(p\) or \(r\); the full model additionally generates ordered matrix-reuse messages. | Exact for the displayed cutoff grammars. Message proliferation alone does not exclude a nonlinear statistic, compressed operator state, or every finite representation. |
| N2 | **Conditional noncommutative continuation-capacity obstruction.** All \(2^r\) ordered reuse words occur, while a bounded-filtration commuting-source finite-jet algebra has subexponential capacity. | Exact implication only after assuming fixed-degree freeness/faithfulness and branch-separating continuation; those two model-specific lemmas remain unproved. It does not exclude operator, noncommuting, or integro-differential states. |
| N3 | **Zero radius of the formal annealed Wick jet.** Along odd \(k\), the exact fixed-order expectation coefficient \(c_k\) has a factorial lower bound, so \(\limsup c_k^{1/k}=+\infty\). | Exact theorem at the formal-annealed level. It does not prove concentration of the random derivatives or construct a positive-time limiting curve. |
| N4 | **Divergence of the ordinary positive Wick--Taylor source profiles.** For every \(s>0\), \(F_M(s)\to+\infty\). | Complete corollary for the formal compiler, from N3 and coefficient positivity. |
| N5 | **Failure of the associated formal one-source Taylor family in physical time.** Its residual-clock losses approach an initial step and are not uniformly Cauchy on any interval containing \(0\). | Complete disproof of the precise Wick--Taylor global-shadowing claim for this prescribed family; not a theorem about every finite compiler or the actual network loss. |
| N6 | **Real target fitting does not imply that the target lies inside the initial Taylor disk.** An invariant finite-width symmetric orbit has a backward complex/real singularity closer than its forward target time. | Complete counterexample to that proof route; not a typical-Gaussian mean-field theorem. |
| N7 | **No exact regular analytic realization of the formal jet on one Banach space.** Such a realization would force positive Taylor radius, contradicting N3. | Exact for a bounded analytic local generator and analytic readout reproducing every \(c_k\). Singular/nonanalytic equations, unbounded generators, scales of spaces, and approximation sequences remain outside the result. |
| N8 | **No positive classical semigroup completion preserving the formal local derivatives and a continuous Wick readout.** Positivity makes every Taylor partial sum a lower bound, which diverges. | Exact only under the displayed cone, domain, semigroup, and continuity hypotheses. |
| N9 | **No coefficientwise-positive, fixed-order-consistent polynomial compiler for the formal jet.** Recovering every \(c_k\) while keeping nonnegative coefficients forces divergence at every positive source value. | Exact for positive polynomial compilers; signed or independently validated real-axis schemes remain outside the result. |
| N10 | **Explicit symbolic Euler/Wick and positive-stage polynomial compilers for the formal jet diverge under mesh refinement.** A binomial selection of \(k\) first-order generator hits recovers the divergent \(c_k\) lower bound. | Exact for the stated Wick-positive consistent polynomial one-step class; signed, implicit, tamed, and scale-space schemes remain open. |
| N11 | **Initialization derivatives alone do not identify a positive-time real-axis function within unrestricted \(C^\infty\).** Flat functions can change positive-time values without changing any derivative at \(0\). | Exact non-identification of a function by its jet, not ambiguity of a fully specified well-posed dynamics. Summability or quasianalytic structure could restore uniqueness. |
| N12 | **Ambient Gaussian \(L^2\) control alone does not control the cubic readout.** Vanishing product-\(L^2\) perturbations can change the readout by order one. | Exact functional counterexample on a nonatomic space. It is not a reachable-state counterexample for this network and does not defeat \(L^2\) methods supplemented by higher-moment control. |
| N13 | **One Banach function space cannot simultaneously contain a Gaussian coordinate, embed continuously into \(L^1\), and have globally bounded ordinary multiplication.** Such a space embeds into \(L^\infty\). | Exact for that one-space algebra package; graded/scale spaces, restricted domains, and unbounded or renormalized products remain possible. |
| N14 | **Gaussian compact truncation can be dynamically singular in the frozen-first-layer subsystem.** Extreme positive particles drive target times to \(0\) as the cutoff grows. | Complete for the frozen subsystem; it is not automatically a full-model theorem because the additional matrix message is not coordinatewise positive. |
| N15 | **Conditional no-positive-delay implication in the asserted tagged-site DMFT.** Positive initial self-response plus the unbounded Gaussian readout tail prevents any classical solution from remaining below a subtarget on a positive interval. | Exact implication from the postulated tagged-site Volterra law and response hypotheses. If a hitting time is defined it is zero; the law and a classical flow are not constructed or identified with the network here. |
| N16 | **Conditional continuous-closure obstruction for the selected relaxed step loss.** Every continuous surrogate has error at least \(1/2\), or \(1\) with exact initialization. | Elementary corollary once N15 and the additional monotone/no-overshoot relaxed selection are assumed; not a model-level network theorem. |
| N17 | **The displayed frozen RMSNorm and global direction-only WN moment hierarchies have no invariant finite rectangular cutoff.** | Complete for those natural frozen reductions. Full trained-system hierarchy nonclosure is diagnostic rather than proved, and no theorem covers every nonlinear statistic or non-Taylor PDE. |
| N18 | **The raw positive-coefficient zero-radius proof does not transfer to RMSNorm or global readout WN.** Signed projection and reciprocal-normalization terms permit cancellations. | A proved limitation on transferring N3, not a positive closure theorem. Any hidden-row-only coefficient transfer requires its separately stated large-fan-in and fixed-order hypotheses. |

Three nearby statements are important but are not themselves non-closure
theorems:

1. An unrestricted “some finite one-source PDE exists” statement is vacuous:
   any continuous scalar curve can be approximated by an oracle Bernstein
   polynomial and packed into two states.
2. Squared loss gives a genuine residual-clock stability theorem: an already
   small feature-profile or tangent-kernel error produces a uniform-in-physical-
   time loss error. It does not make an unproved hierarchy tail small.
3. The formal output-coordinate identity
   \(K(y)=F'(F^{-1}(y))\) is an orbit-specific reparameterization, not by
   itself a closure.  At the canonical point, the exact moments
   \(\mu_0,\ldots,\mu_7\) pass every currently accessible Hankel test, but the
   canonical all-order Stieltjes property remains open.  The stronger uniform
   block-metric extension is exactly false: for \(\beta=1\) and
   \(0<\alpha\le1/100\), a shifted \(3\times3\) Hankel determinant is
   negative.  Determinacy and equality with an actual positive-time network
   kernel also remain open.

---

## 2. Current headline classifications

The later audit separates one resolved formal-compiler question, one
conditional DMFT implication, and one exact frozen-hierarchy result.

### R1. The prescribed ordinary Wick--Taylor closure family is disproved

The formal annealed initial Wick series has radius zero; its positive partial sums
diverge at every \(s>0\); and the induced physical-time closures fail
uniformly. This resolves the **concrete formal Wick--Taylor one-source
compiler question**, but does not identify the actual positive-time
mean-field loss and does not cover every non-Taylor compiler.

Primary proof: `approximate_single_source_conjecture_resolution.md`, with the
current exact coefficient certificates in the mean-field-peeling report.

### R2. Conditional DMFT step-loss implication

Assuming the asserted tagged-site Volterra representation and response
hypotheses, the comparison forbids positive subtarget delay for any classical
solution.  Adding the monotone/no-overshoot relaxed selection gives a selected
step loss.  The \(1/2\)
continuity lower bound, sharpened to \(1\) under exact initialization, is then
exact for that selected target.

Primary proof:
`mean_field_single_source_conjecture_audited_resolution.md`.

This is not an unconditional resolution of the network closure conjecture.
The tagged equation, its self-consistency, a classical positive-time flow,
network-to-DMFT identification, and uniqueness of the relaxed selection are
not proved in the source corpus.

### R3. Exact frozen natural moment/message cutoffs remain non-invariant after the audited normalizations

The displayed frozen RMSNorm and direction-only WN recurrences do not make
any finite rectangular polynomial-moment cutoff invariant. This resolves
that narrower frozen-hierarchy question. It does not prove full trained-system
nonclosure or resolve the broader existence of a signed, non-Taylor,
accuracy-dependent real-axis PDE.

Primary proof: `normalized_mean_field_taylor_closure_audit.md`.

### Supporting results with individually stated scopes

N6, N11--N14 are self-contained counterexamples within their stated scopes.
N7--N10 are exact exclusions of constructions required to realize the same
formal zero-radius jet under the displayed analytic or positivity hypotheses.
They strengthen the explanation of why several proposed proof routes fail,
but they must not be promoted to a theorem against every admissible finite
PDE or against an unidentified actual loss curve.

For N2, the exponential word-generation lemma and the subexponential
commuting-source capacity count are proved, but the link between them is
conditional.  Fixed-degree freeness/faithfulness of the relevant operators
and a branch-separating continuation lemma for the actual Wick hierarchy are
still open.  Consequently N2 is not a theorem against the operator-valued or
integro-differential `operator_pde` proposal.

---

## 3. Which documents actually contain the proofs?

### Primary proof sources

| Source | Role |
|---|---|
| `approximate_single_source_conjecture_resolution.md` | Embedded positive scalar history, factorial lower bound for the formal annealed coefficients, zero radius, boundary layer of the prescribed Taylor closures, and the invariant-manifold Taylor-disk counterexample.  It does not prove concentration or identify an actual positive-time mean-field curve. |
| `approximate_single_source_stability.md` | Residual-clock, coercivity, clock-shadowing, and input-to-state stability implications; exact finite source-PDE algebra.  The stability results assume that a small profile defect has already been established. |
| `adversarial_audit_report.md` | Anti-oracle formulation and scoped analytic, semigroup, positive-compiler, Euler/Wick, \(L^2\), Banach-algebra, and frozen-tail obstructions.  Each excludes only the hypotheses stated there. |
| `mean_field_single_source_conjecture_audited_resolution.md` | Conditional tagged-site Volterra comparison.  The comparison is exact after assuming the representation and response properties; the step trace additionally assumes the relaxed selection. |
| `normalized_mean_field_taylor_closure_audit.md` | RMSNorm and direction-only WN vector fields, exact frozen-block moment recurrences, signed-cancellation analysis, and diagnostic full-system message proliferation. |

### Later synthesis and scope sources

The historical synthesis
`archive/earlier_documents/master_syntheses/MASTER_NEURAL_PDE_REPORT_2026-07-26.md`
promoted several of these claims to established model-level results.  That
classification is superseded by
`FINITE_CAUSAL_NEURAL_PDE_MASTER_MONOGRAPH_v2.2_2026-07-31.md` and by the
current mean-field-peeling and Stieltjes ledgers linked at the top of this
report.

The continuous-depth reports use a bounded residual-\(\tanh\) model. Their
Hermite phrase “complete quadratic” refers to basis degree, not quadratic
activation. Their continuation, rank, compactness, and topology
counterexamples are distinct results and are not additional proofs of R1--R3.

---

## 4. The research goal and the conjectures that must be kept distinct

### 4.1 Canonical target

The model is a two-hidden-layer, one-input, scalar-output MLP with

\[
\phi(u)=\frac{u^2}{2},
\qquad
\mathcal L_n=(1-f_n)^2,
\]

trained in the mean-field \(\mu\)P feature-learning scaling.

The research goal is to replace the infinite mean-field hierarchy by a
finite, autonomous, restartable PDE/ODE whose complexity is independent of
width and of the physical training horizon, while allowing the dimension to
depend on the requested accuracy.

For a non-vacuous result, the finite system must satisfy all of the following.

1. **Finite state:** for each \(\varepsilon>0\), its dimension
   \(D(\varepsilon)\) is finite.
2. **Width independence:** \(D(\varepsilon)\) does not grow with network
   width.
3. **Horizon independence:** one autonomous system predicts the whole
   requested physical-time interval; for the strongest conjecture this is
   \([0,\infty)\).
4. **Non-oracular provenance:** coefficients are derived from the
   architecture, initialization law, and declared local mean-field rules,
   not sampled from the already-solved future loss curve.
5. **Restartability:** the finite state at a positive time determines its own
   continuation.
6. **Correct observable:** the predicted loss obeys the stated uniform norm,
   usually, for an independently constructed and identified target,
   \[
   \sup_{t\ge0}
   |\widehat{\mathcal L}_\varepsilon(t)-\mathcal L_{\mathrm{target}}(t)|
   \le\varepsilon.
   \]
7. **Classical regularity:** in the continuous-closure conjecture the finite
   flow and its loss observable are continuous in time.

### 4.2 Four inequivalent closure questions

The reports sometimes use “finite closure” for four different statements.

1. **Exact natural hierarchy closure:** does a fixed finite list of ordinary
   moments, Grams, or messages form an invariant algebra?
2. **Exact continuation-faithful closure:** can one merge histories while
   preserving every possible tagged future continuation?
3. **Concrete Wick--Taylor approximation:** do the first \(M+1\) limiting
   initialization derivatives generate a uniformly accurate one-source PDE
   as \(M\to\infty\)?
4. **Broad accuracy-dependent finite approximation:** does some admissible
   non-oracular finite real-axis compiler achieve every requested accuracy?

Failure of question 1, 2, or 3 does not by itself answer question 4.  The
tagged-site comparison would answer question 4 for continuous closures of
the selected relaxed step trace only **if** the postulated Volterra
representation and the extra selection rule describe the intended network
target.

### 4.3 Why “one source” alone is not a mathematical restriction

Every \(D\)-state ODE \(\dot x=V(x)\) can be encoded in one source variable.
For example, with

\[
U(t,s)=\sum_{j=0}^{D-1}x_j(t)s^j,
\]

the source derivatives at \(s=0\) recover the coordinates and one can write
a PDE whose restriction to this polynomial ansatz is exactly the ODE.
Therefore “one field, one source” controls syntax only. Finiteness,
provenance, regularity, and the approximation norm carry the actual closure
content.

Conversely, if one is allowed to inspect the exact future target curve, a
two-state one-source construction can approximate any continuous fitting
curve by Bernstein polynomials. Such a construction is curve fitting, not a
mean-field closure.

For completeness, let \(f:[0,\infty)\to[f_0,1]\) be continuous with
\(f(t)\to1\), set

\[
q(t)=\frac{t}{1+t},
\qquad
g(q)=f\!\left(\frac{q}{1-q}\right),
\qquad
g(1)=1,
\]

and let \(p_M\) be a Bernstein polynomial of \(g\). Then

\[
\|p_M-g\|_{L^\infty([0,1])}\to0.
\]

The affine ansatz

\[
U_M(t,s)=u_M(t)+q_M(t)s
\]

is invariant under

\[
\partial_tU_M
=
\bigl(1-\partial_sU_M(t,0)\bigr)^2
\left[
p_M'\!\left(\partial_sU_M(t,0)\right)+s
\right],
\]

because it gives

\[
\dot q_M=(1-q_M)^2,
\qquad
\dot u_M=(1-q_M)^2p_M'(q_M).
\]

With zero initial source slope,

\[
q_M(t)=\frac{t}{1+t},
\qquad
u_M(t)=p_M(q_M(t)).
\]

Hence \(u_M\) uniformly approximates \(f\) on all physical time. The
construction is finite and one-source, but the coefficients of \(p_M\)
contain samples of the already-known target curve. It proves that
non-oracular provenance is mathematically indispensable.

---

## 5. Common model, scaling, and notation

### 5.1 Finite-width network

Suppress the single fixed input and write the hidden preactivations and
activations canonically as

\[
h_i^{(1)}=\frac{(z_i^{(1)})^2}{2},
\]

\[
z_j^{(2)}=\sum_{i=1}^n W_{ji}h_i^{(1)},
\qquad
h_j^{(2)}=\frac{(z_j^{(2)})^2}{2},
\qquad
f_n=\frac1n\sum_{j=1}^n a_jh_j^{(2)}.
\]

For compactness in the derivations below only, write
\(h=h^{(1)}\) and \(z=z^{(2)}\). The symbol \(x\) is reserved for the
external input, which is fixed and therefore suppressed.

Here \(a_j\) is the rescaled readout coordinate. In raw coordinates the
readout weight is \(W_j^{(3)}=a_j/n\), so
\(W_j^{(3)}(0)\sim N(0,n^{-2})\).

Initialization is independent:

\[
z_i^{(1)}\sim N(0,1),
\qquad
a_j\sim N(0,1),
\qquad
W_{ji}\sim N\!\left(0,\frac{\gamma}{n}\right),
\quad \gamma>0.
\]

In this historical report, \(\gamma\) denotes the **middle-layer variance
parameter** (with the earlier canonical choice \(\gamma=4/3\)).  The current
Stieltjes and peeling reports use a rescaled presentation in which \(\gamma\)
denotes an **activation coefficient** and the canonical point is written
\(\gamma=1\).  Numerical constants such as \(17/6\) and \(111\) must not be
mixed without the following rescaling dictionary.

Temporarily write \(\lambda=\gamma\) for the historical middle-layer
variance and set

\[
W^\circ=\sqrt{\frac n\lambda}\,W,
\qquad
z^\circ=\frac1{\sqrt n}W^\circ (z^{(1)})^{\odot2},
\qquad
f^\circ=\frac1n\sum_j a_j(z_j^\circ)^2.
\]

Then \(W^\circ_{ji}\sim N(0,1)\), and the historical variables satisfy

\[
z=\frac{\sqrt\lambda}{2}z^\circ,
\qquad
f_n=\frac\lambda8 f^\circ.
\tag{5.0a}
\]

Let \(D_a^\circ,D_{z^{(1)}}^\circ,D_W^\circ\) denote the three block contributions
to the unit-variance compiler derivation
\(n\nabla f^\circ\mathbin\cdot\nabla\).  Direct change of variables gives

\[
D_{+,n}
=\frac18\left(
\lambda D_a^\circ+
\lambda D_{z^{(1)}}^\circ+
D_W^\circ
\right).
\tag{5.0b}
\]

Consequently,

\[
\mathbb E[D_{+,n}^k f_n]
=\frac\lambda{8^{k+1}}
\mathbb E\!\left[
(\lambda D_a^\circ+\lambda D_{z^{(1)}}^\circ+D_W^\circ)^k f^\circ
\right].
\tag{5.0c}
\]

Thus the historical model is a block-weighted specialization of the same
decorated-forest grammar, not the literal unit-block-metric point.  Constant
block weights change coefficients but not the finite grammar or the
leading-width forest selection.  As a normalization check, (5.0c) gives
the unit-model first-order block contributions
\((27,48,36)\) from \((a,z^{(1)},W)\), and hence

\[
F'(0)=\frac{\lambda}{64}(75\lambda+36)
=\frac{17}{6}
\quad\text{at }\lambda=\frac43.
\]

At the unit-variance, unit-block point the same contributions sum to \(111\).

The label is \(1\) and

\[
\mathcal L_n=(1-f_n)^2.
\]

### 5.2 Feature-ascent derivation

Let \(D_{+,n}\) be the \(\mu\)P gradient-ascent derivation of the readout:

\[
D_{+,n}z_i^{(1)}=n\frac{\partial f_n}{\partial z_i^{(1)}},
\qquad
D_{+,n}W_{ji}=\frac{\partial f_n}{\partial W_{ji}},
\qquad
D_{+,n}a_j=n\frac{\partial f_n}{\partial a_j}.
\]

Direct differentiation gives

\[
D_{+,n}a_j=\frac12z_j^2,
\tag{5.1}
\]

\[
D_{+,n}W_{ji}=\frac1n a_jz_jh_i,
\tag{5.2}
\]

\[
D_{+,n}z_i^{(1)}=z_i^{(1)}\sum_jW_{ji}a_jz_j.
\tag{5.3}
\]

Define

\[
q_n=\frac1n\sum_i h_i^2,
\qquad
K_n=W\operatorname{diag}(h)W^\top,
\qquad
u=a\odot z.
\]

Differentiating \(z=Wh\), using
\(D h_i^{(1)}=z_i^{(1)}D z_i^{(1)}\), gives

\[
D_{+,n}z=q_nu+2K_nu.
\tag{5.4}
\]

The first term \(q_nu\) is the positive scalar branch used in the
zero-radius proof. The second term contains the reused dense-matrix message.
Although \(K_n\succeq0\), the vector \(K_nu\) is not coordinatewise
nonnegative.

### 5.3 Feature time and the residual clock

Let \(\Theta_n(\tau)\) solve feature ascent and set

\[
F_n(\tau)=f_n(\Theta_n(\tau)).
\]

Then

\[
F_n'(\tau)=\kappa_n(\Theta_n(\tau))\ge0,
\tag{5.5}
\]

where \(\kappa_n\) is the \(\mu\)P tangent kernel, a sum of squared metric
gradients.

Physical squared-loss gradient flow follows the same parameter orbit with

\[
\dot\tau_n(t)=2\bigl(1-F_n(\tau_n(t))\bigr),
\qquad
f_n(t)=F_n(\tau_n(t)).
\tag{5.6}
\]

Equivalently,

\[
\dot f_n=2(1-f_n)\kappa_n,
\qquad
\dot{\mathcal L}_n=-4\kappa_n\mathcal L_n.
\tag{5.7}
\]

These identities are exact. They are not scalar closure equations because
\(\kappa_n\) depends on the hidden message hierarchy.

### 5.4 Fixed-order mean-field coefficients

For every fixed \(k\), distinguish the random initialization derivative

\[
C_{n,k}=\frac{D_{+,n}^kf_n(0)}{k!}
\tag{5.8}
\]

from its annealed fixed-order coefficient

\[
c_k
=
\lim_{n\to\infty}\mathbb E[C_{n,k}].
\tag{5.9}
\]

The current exact quadratic decorated-forest compiler establishes (5.9) for
this special one-sample, two-hidden-layer polynomial model: it gives the
finite derivative grammar, leading-width Wick selection, factorization, and
an exact all-order positive subfamily.  This supersedes the older audit's
missing **expectation** bridge for this specialization.

It does **not** prove

\[
C_{n,k}\longrightarrow c_k
\quad\text{in probability or in }L^1,
\tag{5.10}
\]

and it does not justify interchanging the width limit with time
differentiation.  Thus \((c_k)\) is an exact formal annealed mean-field jet.
Calling it the derivative jet of a typical deterministic positive-time
trajectory requires the separate concentration and trajectory-identification
bridges in (5.10).

The order of limits remains crucial: \(k\) is held fixed before
\(n\to\infty\).  No uniform-in-\(k\) convergence or positive-time trajectory
follows from the compiler.

At initialization,

\[
q_n\longrightarrow q_0
=\mathbb E\!\left[\left(\frac{G^2}{2}\right)^2\right]
=\frac34.
\tag{5.11}
\]

---

## 6. Common positive result: residual-clock observable stability

This section is included because it identifies exactly what the negative
results do and do not destroy.

Let \(F\) and \(\widetilde F\) be increasing feature-time profiles with the
same initial output \(f_0<1\). Suppose both reach \(1\), and on a common
target-reaching interval

\[
0<\mu\le F'(\tau)\le K,
\qquad
\|F-\widetilde F\|_\infty\le\varepsilon.
\tag{6.1}
\]

Let their residual clocks solve

\[
\dot\tau=2(1-F(\tau)),
\qquad
\dot{\widetilde\tau}
=2(1-\widetilde F(\widetilde\tau)).
\]

Set \(e=\widetilde\tau-\tau\). If \(e>0\), monotonicity gives

\[
\dot e
=2\bigl(F(\tau)-\widetilde F(\widetilde\tau)\bigr)
\le -2\mu e+2\varepsilon.
\]

The same inequality holds for the upper Dini derivative of \(|e|\) when
\(e<0\). Scalar comparison yields

\[
\sup_{t\ge0}|\widetilde\tau(t)-\tau(t)|
\le\frac{\varepsilon}{\mu}.
\tag{6.2}
\]

Therefore

\[
\sup_{t\ge0}
|F(\tau(t))-\widetilde F(\widetilde\tau(t))|
\le
\left(1+\frac K\mu\right)\varepsilon.
\tag{6.3}
\]

Since both outputs lie in \([f_0,1]\),

\[
\sup_{t\ge0}
|\widetilde{\mathcal L}(t)-\mathcal L(t)|
\le
2(1-f_0)
\left(1+\frac K\mu\right)\varepsilon.
\tag{6.4}
\]

Thus squared loss propagates a **known** small feature-profile defect
uniformly for all physical time. The Wick--Taylor failure below occurs
because its profile defect does not become small.

### 6.1 Positive-entry coercivity and finite total feature time

Let

\[
C_n(t)=\frac1n\sum_{j=1}^n a_j(t)^2.
\]

The readout-layer contribution to the tangent kernel is

\[
\frac1{4n}\sum_j z_j^4.
\]

Cauchy--Schwarz gives

\[
f_n^2
=
\left(\frac1{2n}\sum_j a_jz_j^2\right)^2
\le
C_n\left(\frac1{4n}\sum_jz_j^4\right)
\le C_n\kappa_n.
\tag{6.5}
\]

The physical readout equation is

\[
\dot a_j=(1-f_n)z_j^2,
\]

so

\[
\dot C_n
=
\frac2n\sum_j a_j\dot a_j
=4f_n(1-f_n).
\tag{6.6}
\]

Assume \(f_n(t_*)=a_*\in(0,1)\). While \(0<f_n<1\),

\[
\begin{aligned}
\frac d{dt}\frac{C_n}{f_n^2}
&=
\frac{4(1-f_n)}{f_n}
\left(1-\frac{C_n\kappa_n}{f_n^2}\right)
\le0
\end{aligned}
\]

by (6.5). Therefore, for \(t\ge t_*\),

\[
\kappa_n(t)
\ge
\frac{f_n(t)^2}{C_n(t)}
\ge
\lambda_n
:=
\frac{a_*^2}{C_n(t_*)}>0.
\tag{6.7}
\]

It follows that

\[
1-f_n(t)
\le
(1-a_*)e^{-2\lambda_n(t-t_*)}.
\tag{6.8}
\]

Using the residual clock,

\[
\int_{t_*}^\infty2(1-f_n(t))\,dt
\le
\frac{1-a_*}{\lambda_n}<\infty.
\tag{6.9}
\]

Thus a target-fitting physical trajectory uses only a finite amount of
feature time. This is the mechanism behind the stability theorem, but it
still requires the feature-profile defect to be small on that finite
interval.  The estimate is finite-width and trajectorywise after a time
\(t_*\) at which \(f_n(t_*)=a_*\in(0,1)\).  Its rate
\(\lambda_n=a_*^2/C_n(t_*)\) is random and width-dependent, so it does not by
itself prove typical entry into this regime or uniform-in-width mean-field
contraction.

---

## 7. The zero-radius theorem

### 7.1 The embedded scalar branch

Freeze the first-layer variables only for the purpose of selecting one word
inside the full derivative expansion. Retain the readout and middle-feature
updates

\[
a'=\frac12z^2,
\qquad
z'=qaz.
\]

Define

\[
\mathscr D_0
=\frac{z^2}{2}\partial_a+qaz\,\partial_z,
\qquad
g(a,z)=\frac12az^2,
\]

and

\[
P_k(a,z;q)=\frac1{k!}\mathscr D_0^kg(a,z).
\tag{7.1}
\]

Both coefficients in \(\mathscr D_0\) and the coefficients of \(g\) are
nonnegative. Induction therefore shows that every coefficient of \(P_k\) is
nonnegative.

The total degree of \(P_k\) is \(k+3\). Each application of
\(\mathscr D_0\) flips the parity of the power of \(a\). Hence, for odd \(k\)
and

\[
m=\frac{k+3}{2},
\]

there are coefficients \(p_{uv}(q)\ge0\) such that

\[
P_k(a,z;q)
=
\sum_{u+v=m}p_{uv}(q)a^{2u}z^{2v}.
\tag{7.2}
\]

### 7.2 Exact coefficient identity on an invariant ray

The ray

\[
z=\sqrt{2q}\,a
\]

is invariant, because on it

\[
a'=\frac12(2qa^2)=qa^2
\]

and

\[
z'=qaz
=q a\sqrt{2q}\,a
=\sqrt{2q}\,a'.
\]

Starting from \(a(0)=1\),

\[
a(\tau)=\frac1{1-q\tau}.
\]

Along the ray,

\[
g(\tau)=\frac12a(\tau)z(\tau)^2
=qa(\tau)^3
=\frac{q}{(1-q\tau)^3}.
\]

Using

\[
(1-x)^{-3}
=\sum_{k=0}^\infty\binom{k+2}{2}x^k,
\]

comparison of the \(\tau^k\) coefficient gives

\[
P_k(1,\sqrt{2q};q)
=q^{k+1}\binom{k+2}{2}.
\tag{7.3}
\]

### 7.3 Why the full network cannot cancel this word

In the independent primitive variables,

\[
f_n
=
\frac1{8n}
\sum_{j,i,\ell}
a_jW_{ji}W_{j\ell}(z_i^{(1)})^2(z_\ell^{(1)})^2.
\tag{7.4}
\]

Every numerical coefficient in (7.4) is nonnegative. Each component of the
feature-ascent vector field is a positive learning-rate factor times a
partial derivative of \(f_n\), and therefore also has nonnegative polynomial
coefficients.

If \(p\) has nonnegative primitive coefficients, then

\[
D_{+,n}p
=\sum_\alpha
\frac{\partial p}{\partial\theta_\alpha}
D_{+,n}\theta_\alpha
\]

also has nonnegative primitive coefficients. Induction shows that every
product-rule history in \(D_{+,n}^kf_n\) is coefficientwise nonnegative.

For independent centered Gaussian primitive variables, a monomial has
expectation zero if any exponent is odd and strictly positive if every
exponent is even. Hence every surviving omitted history has nonnegative Wick
expectation. Selecting the \(q_n(a\odot z)\) term in (5.4) at every hit and
never differentiating \(q_n\) therefore gives a genuine lower bound for the
full fixed-order coefficient.

### 7.4 Gaussian factorial amplification

Let

\[
A\sim N(0,1),
\qquad
Z\sim N(0,\gamma q_0),
\]

independently, and define

\[
b_\gamma
=\frac12\min\left\{1,\frac\gamma2\right\}>0.
\tag{7.5}
\]

For \(u+v=m\),

\[
\mathbb E[A^{2u}Z^{2v}]
=(2u-1)!!(2v-1)!!(\gamma q_0)^v.
\]

Since

\[
(2u-1)!!\ge u!,
\qquad
(2v-1)!!\ge v!,
\]

and

\[
u!v!
=\frac{m!}{\binom mu}
\ge\frac{m!}{2^m},
\]

we obtain

\[
\mathbb E[A^{2u}Z^{2v}]
\ge
m!b_\gamma^m(2q_0)^v.
\tag{7.6}
\]

Indeed, the preceding double-factorial bounds first give

\[
\mathbb E[A^{2u}Z^{2v}]
\ge m!2^{-m}\gamma^vq_0^v.
\]

If \(d=\min\{1,\gamma/2\}\), then \(v\le m\) implies
\(d^m\le(\gamma/2)^v\). Hence
\(\gamma^v\ge d^m2^v\), which is exactly (7.6) because
\(b_\gamma=d/2\).

Using (7.2), (7.6), coefficient nonnegativity, and then (7.3),

\[
\begin{aligned}
\mathbb E[P_k(A,Z;q_0)]
&\ge
m!b_\gamma^m
\sum_{u+v=m}p_{uv}(q_0)(2q_0)^v\\
&=
m!b_\gamma^m
P_k(1,\sqrt{2q_0};q_0)\\
&=
m!b_\gamma^m q_0^{k+1}\binom{k+2}{2}.
\end{aligned}
\]

The no-cancellation comparison, followed by the exact annealed
leading-width evaluation in (5.9), therefore proves:

### Theorem 7.1 — Zero radius

For every odd \(k\), with \(m=(k+3)/2\),

\[
\boxed{
c_k
\ge
m!b_\gamma^m q_0^{k+1}\binom{k+2}{2}.
}
\tag{7.7}
\]

Since \(m\sim k/2\), Stirling’s formula gives

\[
(m!)^{1/k}\asymp\sqrt{k},
\]

and all other factors in (7.7) have at most exponential or polynomial
growth. Consequently,

\[
\boxed{
\limsup_{k\to\infty}c_k^{1/k}=+\infty.
}
\tag{7.8}
\]

Thus the formal series

\[
\sum_{k=0}^\infty c_ks^k
\]

has radius of convergence zero.

This conclusion concerns the formal annealed fixed-order mean-field series.
If a macroscopic profile \(F\) exists and satisfies
\(F^{(k)}(0)=k!c_k\), then \(F\) is not analytic at \(0\) and this Taylor
series cannot represent it. Without that extra identification, the exact
statement is the zero radius of the **formal annealed Wick series**.  In
particular, zero radius does not rule out a singular finite ODE/PDE or any
other nonanalytic continuation of an actual curve.

---

## 8. Failure of the one-source Wick--Taylor PDE

### 8.1 The exact formal-compiler conjecture

Define the degree-\(M\) source profile

\[
F_M(s)=\sum_{k=0}^M c_ks^k.
\tag{8.1}
\]

The proposed one-field, one-source closure is

\[
\partial_tU_M(t,s)
=
2\bigl(1-U_M(t,0)\bigr)\partial_sU_M(t,s),
\qquad
U_M(0,s)=F_M(s).
\tag{8.2}
\]

Its output and loss are

\[
f_M(t)=U_M(t,0),
\qquad
\mathcal L_M(t)=(1-f_M(t))^2.
\tag{8.3}
\]

The polynomial space of degree at most \(M\) is invariant. If

\[
u_k(t)=\partial_s^kU_M(t,0),
\]

then (8.2) is exactly

\[
\dot u_k=2(1-u_0)u_{k+1},
\quad 0\le k<M,
\qquad
\dot u_M=0,
\tag{8.4}
\]

with

\[
u_k(0)=k!c_k.
\]

The historical formula used an unqualified distance to the random curve
\(\mathcal L_n\), so it did not specify an almost-sure, in-probability, or
expected norm.  A precise weak version is enough for the no-go. For each
\(T>0\), define the bounded path metric

\[
d_T(g,h)=\min\!\left\{1,
\sup_{0\le t\le T}|g(t)-h(t)|\right\}.
\]

The audited shadowing conjecture is

\[
\boxed{
\lim_{M\to\infty}
\limsup_{n\to\infty}
\mathbb E\!\left[d_T(\mathcal L_M,\mathcal L_n)\right]
=0
\quad\text{for every }T>0.
}
\tag{8.5}
\]

The order of limits is part of the statement: first the fixed-order
annealed coefficients are taken, then the source order \(M\) is increased.
An expected untruncated uniform norm is stronger and is ruled out as well.
A deterministic mean-curve version is a different, generally weaker
condition, but its common-target formulation is also ruled out by the same
Cauchy triangle argument.

### 8.2 Divergence at every positive feature time

All \(c_k\ge0\), because the primitive derivative histories are
coefficientwise nonnegative and Gaussian Wick expectation is nonnegative on
that cone. Also \(c_0=0\).

Fix \(s>0\). By (7.8), along an odd subsequence

\[
c_ks^k
\]

does not tend to zero; indeed it is unbounded. Since the partial sums are
monotone in \(M\),

\[
\boxed{
F_M(s)\longrightarrow+\infty
\quad\text{for every }s>0.
}
\tag{8.6}
\]

For \(y\in(0,1)\), let \(r_M(y)\) be the first positive solution of

\[
F_M(r_M(y))=y.
\]

For every odd \(k\le M\),

\[
y=F_M(r_M(y))
\ge c_kr_M(y)^k,
\]

so

\[
r_M(y)
\le
\left(\frac{y}{c_k}\right)^{1/k}.
\]

Choose an increasing odd sequence for which \(c_k^{1/k}\to\infty\).
Then

\[
\boxed{
r_M(y)\longrightarrow0.
}
\tag{8.7}
\]

### 8.3 Collapse of physical target times

The characteristic through \(s=0\) has source clock \(s_M(t)\) satisfying

\[
\dot s_M(t)
=2\bigl(1-F_M(s_M(t))\bigr),
\qquad
s_M(0)=0,
\tag{8.8}
\]

and

\[
f_M(t)=F_M(s_M(t)).
\]

The physical time required to reach output \(y\in(0,1)\) is

\[
t_M(y)
=
\int_0^{r_M(y)}
\frac{ds}{2(1-F_M(s))}.
\tag{8.9}
\]

For \(0\le s\le r_M(y)\),

\[
0\le F_M(s)\le y,
\]

and therefore

\[
t_M(y)
\le
\frac{r_M(y)}{2(1-y)}
\longrightarrow0.
\tag{8.10}
\]

Fix \(t>0\). For every \(y<1\), (8.10) implies that \(f_M(t)\ge y\) for
all sufficiently large \(M\). The residual clock cannot cross the first
target root, so \(f_M(t)\le1\). Letting \(y\uparrow1\) gives

\[
\boxed{
f_M(t)\longrightarrow1,
\qquad
\mathcal L_M(t)\longrightarrow0
\quad(t>0).
}
\tag{8.11}
\]

At the initial time,

\[
\boxed{
\mathcal L_M(0)=1
\quad\text{for every }M.
}
\tag{8.12}
\]

Thus the pointwise limit is

\[
\mathcal L_\infty(t)
=
\begin{cases}
1,&t=0,\\
0,&t>0.
\end{cases}
\tag{8.13}
\]

Every \(\mathcal L_M\) is continuous. Hence uniform convergence on any
\([0,T]\), \(T>0\), is impossible.

### 8.4 Direct contradiction to probabilistic global shadowing

The conclusion does not require a regular limiting true loss curve.
Suppose (8.5) were true. Since \(d_T\) is a metric, for any \(M,M'\),

\[
d_T(\mathcal L_M,\mathcal L_{M'})
\le
d_T(\mathcal L_M,\mathcal L_n)
+d_T(\mathcal L_n,\mathcal L_{M'}).
\]

Taking expectations, then \(\limsup_{n\to\infty}\), and finally large
\(M,M'\), would force
\((\mathcal L_M)\) to be uniformly Cauchy. But (8.11)--(8.12) show that it
is not uniformly Cauchy on any interval containing zero. Therefore:

### Theorem 8.1 — Failure of the prescribed formal Wick--Taylor closure family

\[
\boxed{\text{The conjecture \((8.5)\) is false.}}
\]

The theorem does not address a diagonal limit \(M=M(n)\), a fixed-\(n\)
Taylor germ inside its random convergence disk, or a signed/non-Taylor
real-axis compiler.  The step in (8.13) is the pointwise limit of the
**constructed Taylor-closure losses** \(\mathcal L_M\); it is not the loss of
an independently constructed network mean-field trajectory.

---

## 9. Real fitting does not imply Taylor-disk coverage

The repository also gives a deterministic finite-width counterexample to the
argument “the real trajectory reaches the target stably, therefore its
initial Taylor series reaches that far.”

Consider the invariant symmetric manifold

\[
z_i^{(1)}=\zeta,
\qquad
a_j=a,
\qquad
W_{ji}=\frac wn.
\]

Equations (5.1)--(5.3) reduce to

\[
f=\frac18aw^2\zeta^4,
\]

\[
a'=\frac18w^2\zeta^4,
\qquad
w'=\frac14aw\zeta^4,
\qquad
\zeta'=\frac12aw^2\zeta^3.
\tag{9.1}
\]

Choose

\[
a(0)=-1,
\qquad
w(0)=2,
\qquad
\zeta(0)=\sqrt8.
\tag{9.2}
\]

Differentiate

\[
w^2-2a^2
\quad\text{and}\quad
\zeta^2-4a^2
\]

using (9.1). Both derivatives vanish. Their initial values are \(2\) and
\(4\), so

\[
w^2=2(1+a^2),
\qquad
\zeta^2=4(1+a^2).
\]

Substitution into (9.1) yields

\[
a'=4(1+a^2)^3,
\qquad
f=4a(1+a^2)^3.
\tag{9.3}
\]

Backward from \(a=-1\), the orbit blows up at feature-time distance

\[
B
=\int_1^\infty\frac{ds}{4(1+s^2)^3}.
\]

For \(s\ge1\), \(1+s^2\ge2s\). Hence

\[
B
\le
\int_1^\infty\frac{ds}{32s^3}
=\frac1{64}.
\tag{9.4}
\]

Forward, the target time exceeds the time needed just to move from \(a=-1\)
to \(a=0\):

\[
\tau_*
>
\int_0^1\frac{ds}{4(1+s^2)^3}.
\]

On \(0\le s\le1\), \(4(1+s^2)^3\le32\), so

\[
\tau_*>\frac1{32}.
\tag{9.5}
\]

Therefore

\[
B\le\frac1{64}<\frac1{32}<\tau_*.
\tag{9.6}
\]

The initial Taylor radius is bounded by a backward singularity strictly
closer than the forward target. Squared-loss physical dynamics can still be
stable because the residual clock follows the real forward branch; it does
not enlarge the analytic disk.

---

## 10. Structural corollaries of zero radius

The next results enlarge the class of constructions excluded by Theorem 7.1,
without claiming a no-go against every possible real-axis compiler.  They
are exact exclusions of systems required to reproduce the **formal annealed
jet** \((c_k)\).  Until that jet is identified with an actual positive-time
network trajectory, they are not no-go theorems for the trajectory itself.

### 10.1 No one-space bounded analytic realization

Assume there is a Banach space \(X\), an initial state \(Y_0\in X\), and an
exact realization

\[
Y'=V(Y),
\qquad
F'=K(Y),
\tag{10.1}
\]

where \(V\) and \(K\) are analytic near \(Y_0\). This includes a
representation in which all polynomial attachment and contraction rules are
bounded multilinear maps on one Banach space.

The analytic Banach-space ODE theorem makes \(Y(\tau)\) analytic for
\(|\tau|<R\) for some \(R>0\). Then \(K(Y(\tau))\), and after integration
\(F(\tau)\), are analytic on a possibly smaller disk. Cauchy estimates give

\[
\frac{|F^{(k)}(0)|}{k!}\le CR^{-k}.
\tag{10.2}
\]

Exactness identifies the left side with \(|c_k|\), contradicting (7.8).
Thus:

### Corollary 10.1

There is no exact one-Banach-space realization with a bounded analytic local
generator and analytic readout map that reproduces all fixed-order
quadratic/Gaussian Wick coefficients.

A scale of spaces with regularity loss, an unbounded generator, a mild
solution outside all generator domains, or a nonanalytic real-axis
construction is not covered.

### 10.2 No positive classical semigroup completion

Let \(\mathcal A_+\) be the cone of primitive polynomials with nonnegative
coefficients, and let \(\Lambda\) be centered Gaussian Wick expectation. The
primitive algebra satisfies

\[
f\in\mathcal A_+,
\qquad
D\mathcal A_+\subseteq\mathcal A_+,
\qquad
\Lambda(p)\ge0\quad(p\in\mathcal A_+).
\tag{10.3}
\]

Suppose an ordered Banach completion carries a positive strongly continuous
semigroup \(S(\tau)\), its generator extends \(D\) on every
\(D^kf\), and \(\Lambda\) extends to a continuous positive functional.

The semigroup Taylor formula gives, for every \(M\),

\[
S(\tau)f
=
\sum_{k=0}^M\frac{\tau^k}{k!}D^kf
+
\int_0^\tau
\frac{(\tau-r)^M}{M!}S(r)D^{M+1}f\,dr.
\tag{10.4}
\]

Every factor in the remainder is positive in the ordered space. Applying
\(\Lambda\) yields

\[
\Lambda(S(\tau)f)
\ge
\sum_{k=0}^M c_k\tau^k.
\tag{10.5}
\]

For every \(\tau>0\), the right-hand side tends to \(+\infty\). This
contradicts a finite-valued continuous readout \(\Lambda(S(\tau)f)\).

### Corollary 10.2

No finite-valued positive classical semigroup can simultaneously preserve
the primitive positive cone, realize every local derivative \(D^kf\), and
make Wick readout continuous.

The theorem deliberately leaves open constructions that lose at least one
of these properties, such as signed nonlocal cancellation or a mild state
outside the domains of high generator powers.

### 10.3 No positive fixed-order-consistent polynomial compiler

Let

\[
P_M(s)=\sum_{k\ge0}\beta_{M,k}s^k
\]

be finite polynomials such that

\[
\beta_{M,k}\ge0
\]

and, for every fixed \(k\),

\[
\beta_{M,k}\longrightarrow c_k.
\tag{10.6}
\]

Fix \(s>0\) and \(A>0\). By (7.8), choose a fixed \(k\) with

\[
c_ks^k>2A.
\]

By (10.6), for sufficiently large \(M\),

\[
\beta_{M,k}>\frac{c_k}{2}.
\]

Therefore

\[
P_M(s)\ge\beta_{M,k}s^k>A.
\]

Since \(A\) is arbitrary:

### Corollary 10.3

\[
\boxed{
P_M(s)\longrightarrow+\infty
\quad\text{for every }s>0.
}
\]

Hence no coefficientwise-positive polynomial compiler can both recover all
fixed Wick coefficients and converge at positive feature time.

### 10.4 Explicit Euler/Wick and positive-stage one-step compilers

Let \(X\) be the polynomial feature-ascent vector field and let \(E_h\) be
pullback by one explicit Euler update:

\[
E_hp=p\circ(I+hX).
\]

Because \(p=f\) and \(X\) have nonnegative primitive coefficients,
multinomial expansion gives

\[
E_h=I+hD+\sum_{\ell\ge2}h^\ell A_\ell,
\tag{10.7}
\]

where every \(A_\ell\) preserves the coefficientwise-positive cone.

In \(E_h^Nf\), choose \(hD\) from exactly \(k\) of the \(N\) factors and the
identity from the others. There are \(\binom Nk\) such choices, and their
combined contribution is

\[
\binom Nk h^kD^kf.
\]

Every omitted choice has nonnegative Wick expectation. With \(h=\tau/N\),

\[
\begin{aligned}
\Lambda(E_{\tau/N}^Nf)
&\ge
\binom Nk\left(\frac{\tau}{N}\right)^k\Lambda(D^kf)\\
&=
\tau^k\frac{(N)_k}{N^k}c_k,
\end{aligned}
\tag{10.8}
\]

where

\[
(N)_k=N(N-1)\cdots(N-k+1).
\]

Fix \(\tau>0\) and \(A>0\). Choose \(k\) with

\[
c_k\tau^k>2A,
\]

then choose \(N\) so large that

\[
\frac{(N)_k}{N^k}>\frac12.
\]

Equation (10.8) gives

\[
\Lambda(E_{\tau/N}^Nf)>A.
\]

Thus:

### Corollary 10.4

\[
\boxed{
\Lambda(E_{\tau/N}^Nf)\longrightarrow+\infty
\quad(\tau>0).
}
\]

The same combinatorics applies when the Euler kernel is integrated rather
than the Euler readout: selecting \(k-1\) generator hits at the \(m\)-th
checkpoint and using

\[
\sum_{m=k-1}^{N-1}\binom{m}{k-1}
=\binom Nk
\]

recovers (10.8). More generally, the proof covers a consistent polynomial
one-step compiler of the form (10.7) whenever all higher operators preserve
the positive Wick cone, including the stated positive-stage Picard/SSP
schemes.

It does not cover genuinely signed, implicit, tamed, nonpolynomial, or
independently certified scale-space integrators.

### 10.5 The complete jet does not identify a real-axis solution

Suppose every derivative at \(0\) were known. In \(C^\infty\), the function

\[
\psi(\tau)
=
\begin{cases}
e^{-1/\tau^2},&\tau>0,\\
0,&\tau\le0
\end{cases}
\]

is nonzero for \(\tau>0\) but satisfies

\[
\psi^{(k)}(0)=0
\quad\text{for every }k.
\]

Thus \(F\) and \(F+\psi\) have the same complete initialization jet and
different positive-time behavior. Once analyticity is unavailable, a jet
does not select its own continuation within unrestricted \(C^\infty\).  This
does not make a fully specified, independently well-posed network dynamics
ambiguous; it only shows that the jet alone is insufficient data.

Padé, Borel, or another resummation may still be correct, but it requires a
summability, quasianalyticity, or independent real-axis well-posedness theorem
identifying its continuation with the network’s trajectory.

---

## 11. Topology and Gaussian-tail obstructions

### 11.1 The cubic readout is discontinuous in ordinary \(L^2\)

Let the underlying probability space be nonatomic. For \(R>1\), choose an
event \(A_R\) of probability \(R^{-3}\) and define

\[
a_R=z_R=R\,\mathbf 1_{A_R}.
\]

Then

\[
\|a_R\|_2^2+\|z_R\|_2^2
=
2R^2R^{-3}
=\frac2R
\longrightarrow0.
\tag{11.1}
\]

But the cubic readout contribution is

\[
\mathbb E[a_Rz_R^2]
=R^3R^{-3}
=1.
\tag{11.2}
\]

Therefore the map

\[
(a,z)\longmapsto\mathbb E[az^2]
\]

is not continuous at \(0\) in the product \(L^2\) topology. Since the
tangent kernel contains still higher powers, ordinary \(L^2\) control is
even less sufficient for it.

This invalidates any argument that uses only ambient \(L^2\) energy bounds to infer
continuity of the loss, weak lower semicontinuity of the loss, or a small
observable Galerkin residual. It does not rule out a stronger higher-moment,
Orlicz, scale-of-spaces, or reachable-set topology.  The constructed
rare-event pair is a functional witness on a nonatomic probability space; it
is not shown to lie on the reachable state manifold of the canonical
network.

### 11.2 A single bounded-multiplication Banach algebra excludes Gaussians

Let \(X\) be a Banach space of random variables such that

\[
\|x\|_1\le C_1\|x\|_X
\tag{11.3}
\]

and ordinary multiplication is bounded:

\[
\|xy\|_X\le C_2\|x\|_X\|y\|_X.
\tag{11.4}
\]

Iterating (11.4) and then using (11.3),

\[
\|x^m\|_1
\le
C_1C_2^{m-1}\|x\|_X^m.
\]

Taking \(m\)-th roots,

\[
\|x\|_m
\le
C_1^{1/m}C_2^{1-1/m}\|x\|_X.
\]

On a probability space, \(\|x\|_m\uparrow\|x\|_\infty\) as
\(m\to\infty\). Hence

\[
\boxed{
\|x\|_\infty\le C_2\|x\|_X.
}
\tag{11.5}
\]

Thus \(X\subset L^\infty\), and \(X\) cannot contain a nondegenerate
Gaussian coordinate. A successful Gaussian theory cannot simply place all
polynomial rules in one Banach function algebra with **globally** bounded
ordinary pointwise multiplication and a continuous embedding into \(L^1\);
it may instead use a scale of spaces, a restricted nonlinear domain, an
unbounded generator, or a renormalized product.

### 11.3 Frozen-first-layer Gaussian cutoff can be dynamically singular

In the frozen-first-layer subsystem, after the rescaling used in the source,
a particle satisfies

\[
\dot u=qv^2,
\qquad
\dot v=quv,
\tag{11.6}
\]

and contributes \(quv^2\) to the readout. For \(u,v\ge0\), both coordinates
are nondecreasing. Moreover

\[
\frac d{d\tau}(v^2-u^2)=0.
\tag{11.7}
\]

On the invariant ray \(u=v=w\),

\[
\dot w=qw^2,
\qquad
w(\tau)=\frac{w_0}{1-qw_0\tau}.
\tag{11.8}
\]

Now condition the centered Gaussian initial law to the square
\([-R,R]^2\). Its density is bounded below by a positive constant on a
small neighborhood of the positive corner \((R,R)\). Put

\[
\tau_R=\frac1{qR}
\]

and let \(\tau=\tau_R-\epsilon\). Consider the corner square

\[
B_\epsilon=[R-C\epsilon,R]^2
\]

for a fixed \(C>0\) and sufficiently small \(\epsilon\). It has probability
at least \(c_R\epsilon^2\), where \(c_R>0\) may depend on the fixed cutoff
\(R\).

For a trajectory starting in \(B_\epsilon\), put
\(w=\min\{u,v\}\). If \(u\le v\), then

\[
\dot u=qv^2\ge qu^2=qw^2;
\]

if \(v\le u\), then

\[
\dot v=quv\ge qv^2=qw^2.
\]

Thus the lower right Dini derivative satisfies

\[
D_+w\ge qw^2.
\]

Scalar comparison with (11.8) gives

\[
w(\tau)
\ge
\frac{w_0}{1-qw_0\tau}.
\tag{11.9}
\]

Here \(w_0\ge R-C\epsilon\), and

\[
\begin{aligned}
1-qw_0\tau
&\le
1-q(R-C\epsilon)(\tau_R-\epsilon)\\
&=
qR\epsilon+\frac{C}{R}\epsilon-qC\epsilon^2
\le C_R'\epsilon.
\end{aligned}
\]

Therefore, on \(B_\epsilon\),

\[
u(\tau),v(\tau)\ge w(\tau)\ge\frac{c_R'}{\epsilon}.
\]

The contribution to the mean readout from this corner alone obeys

\[
\mathbb E[qu(\tau)v(\tau)^2]
\ge
\Pr(B_\epsilon)\,
q\left(\frac{c_R'}{\epsilon}\right)^3
\ge\frac{c_R''}{\epsilon}
\longrightarrow+\infty.
\tag{11.10}
\]

Hence the feature-time readout tends to \(+\infty\) as
\(\tau\uparrow\tau_R\), and every fixed subtarget \(y<1\) is reached at a
feature time strictly less than \(1/(qR)\).

Before the subtarget is reached, \(1-F_R(\tau)\ge1-y\). The physical-time
change therefore gives

\[
t_R(y)
=
\int_0^{\tau_R(y)}
\frac{d\tau}{2(1-F_R(\tau))}
\le
\frac{1}{2qR(1-y)}
\longrightarrow0.
\tag{11.11}
\]

Thus the cutoff losses equal \(1\) initially but tend to \(0\) at every
fixed positive physical time. Initial convergence of truncated Gaussian laws
in Wasserstein distance or in each fixed moment does not imply dynamic
uniform convergence.

The exact statement is confined to the frozen subsystem. In the fully
trained model the extra term \(K(a\odot z)\) has no coordinatewise sign, so
this particular particle comparison does not transfer automatically.

---

## 12. Conditional tagged-site comparison and no-positive-delay implication

This argument is logically independent of the Taylor-series proof, but it is
not an established model-level DMFT theorem.  It starts from a postulated
tagged-site Volterra representation.  The calculation below is exact **if**
that representation and its response/output properties hold.

### 12.1 Postulated tagged-site equations

For a tagged second-layer neuron, let

- \(a(t)\) be the rescaled readout weight;
- \(z(t)\) be its second-layer preactivation;
- \(\xi(t)\) be the cavity Gaussian field;
- \(M(t,s)\) be the deterministic causal self-response kernel;
- \(r(t)=1-f(t)\) be the residual.

Assume that the infinite-width network is represented by

\[
z(t)
=
\xi(t)
+
\int_0^t r(s)M(t,s)a(s)z(s)\,ds,
\tag{12.1}
\]

\[
\dot a(t)=r(t)z(t)^2.
\tag{12.2}
\]

Also assume all of the following causal and self-consistency properties:

1. \(\xi\) is a nondegenerate continuous Gaussian process;
2. \(a(0)\sim N(0,1)\) is independent of the entire cavity process \(\xi\);
3. \(M\) is deterministic, causal, and continuous on an initial triangle
   \(0\le s\le t\le\delta_0\);
4. wherever the classical flow exists,
   \[
   \dot f=2(1-f)\kappa,
   \qquad
   \kappa\ge\frac14\mathbb E[z^4].
   \tag{12.3}
   \]

The source corpus does not derive (12.1) from the finite network, prove
self-consistency or network-to-DMFT identification, establish uniqueness, or
construct a classical positive-time solution satisfying all four items.  The
comparison below is therefore an exact implication from these assumptions,
not evidence that this is the actual mean-field law of the canonical
network.

### 12.2 Positive initial self-response

Let

\[
h_0=\frac12G^2,
\qquad
G\sim N(0,1).
\]

Then

\[
\mathbb E[h_0]=\frac12,
\qquad
\mathbb E[h_0^2]=\frac34.
\tag{12.4}
\]

The diagonal middle-layer Gram coefficient at initialization is

\[
K_{\mathrm{diag}}(0)
=\gamma\mathbb E[h_0]
=\frac\gamma2.
\tag{12.5}
\]

The exact finite-width physical-time composite equation is

\[
\dot z
=2r\bigl(q(a\odot z)+2K(a\odot z)\bigr).
\]

Its instantaneous coefficient multiplying \(a_jz_j\) is

\[
2q_0+4K_{\mathrm{diag}}(0)
=
2\mathbb E[h_0^2]+4\gamma\mathbb E[h_0].
\]

This finite-width coefficient is a necessary local consistency check for a
correct tagged-site limit, but it does not derive the Volterra kernel.  In
the conditional argument we therefore **assume** that the postulated kernel
inherits, in the convention in which \(r(s)\) is outside it,

\[
\boxed{
M(0,0)
=\frac32+2\gamma>0.
}
\tag{12.6}
\]

Continuity of \(M\) gives constants \(m>0\) and \(\delta_0>0\) such that

\[
M(t,s)\ge m
\qquad
(0\le s\le t\le\delta_0).
\tag{12.7}
\]

No global coordinatewise sign of the finite matrix \(K\) is assumed.  What
is assumed instead is the representation claim that all remaining effects
are captured by \(\xi\) and a continuous response kernel satisfying
(12.6)--(12.7).

### 12.3 A positive-probability cavity event

Choose \(z_*>0\). By continuity and nondegeneracy of \(\xi(0)\), after
possibly reducing \(\delta_0\),

\[
p_\xi
:=
\Pr\!\left[
\inf_{0\le t\le\delta_0}\xi(t)\ge z_*
\right]
>0.
\tag{12.8}
\]

Indeed, the event

\[
\left\{\xi(0)\ge2z_*\right\}
\cap
\left\{
\sup_{t\le\delta_0}|\xi(t)-\xi(0)|\le z_*
\right\}
\]

has positive probability for sufficiently small \(\delta_0\).

Independence of \(a(0)\) and \(\xi\) gives, for every finite \(A\),

\[
p_A
:=
\Pr\!\left[
a(0)\ge A,\
\inf_{t\le\delta_0}\xi(t)\ge z_*
\right]
=p_\xi\Pr[a(0)\ge A]
>0.
\tag{12.9}
\]

The probability can be extremely small. Strict positivity is enough.

### 12.4 Cooperative Riccati comparison

Fix \(y\in(0,1)\) and suppose the output remains below \(y\) on a positive
interval. Then

\[
r(t)\ge c:=1-y>0.
\tag{12.10}
\]

On the event in (12.9), equations (12.1)--(12.2), (12.7), and
(12.10) imply

\[
a(t)
\ge
A+c\int_0^t z(s)^2\,ds,
\tag{12.11}
\]

\[
z(t)
\ge
z_*+cm\int_0^t a(s)z(s)\,ds.
\tag{12.12}
\]

Compare with

\[
\dot b=cv^2,
\qquad
\dot v=cm\,bv,
\qquad
b(0)=A,
\qquad
v(0)=z_*.
\tag{12.13}
\]

The right-hand sides are cooperative on \(b,v\ge0\), so monotone Volterra
comparison yields

\[
a(t)\ge b(t),
\qquad
z(t)\ge v(t)
\tag{12.14}
\]

until either the output reaches \(y\) or the comparison solution blows up.

The comparison has invariant

\[
v(t)^2-z_*^2
=
m\bigl(b(t)^2-A^2\bigr).
\tag{12.15}
\]

For \(A>z_*/\sqrt m\), let

\[
\alpha
=
\sqrt{A^2-\frac{z_*^2}{m}}.
\]

Then (12.15) gives

\[
\dot b
=cm(b^2-\alpha^2).
\tag{12.16}
\]

Separating variables,

\[
\int_A^{b(t)}
\frac{d\beta}{\beta^2-\alpha^2}
=cm\,t.
\]

Since

\[
\int
\frac{d\beta}{\beta^2-\alpha^2}
=
\frac1{2\alpha}
\log\!\left(\frac{\beta-\alpha}{\beta+\alpha}\right),
\]

the blow-up time is

\[
\boxed{
T_A
=
\frac1{2cm\alpha}
\log\!\left(\frac{A+\alpha}{A-\alpha}\right).
}
\tag{12.17}
\]

As \(A\to\infty\),

\[
\alpha
=A-\frac{z_*^2}{2mA}+O(A^{-3}),
\]

so

\[
\frac{A+\alpha}{A-\alpha}
=O(A^2)
\]

and therefore

\[
\boxed{
T_A=O\!\left(\frac{\log A}{A}\right)
\longrightarrow0.
}
\tag{12.18}
\]

### 12.5 No classical solution can have positive subtarget delay

Suppose a classical solution exists on a positive interval and remains below
some \(y\in(0,1)\) there.  Before \(f\) reaches \(y\), (12.3) and (12.10)
imply

\[
\dot f
=2r\kappa
\ge
\frac c2\mathbb E[z^4].
\tag{12.19}
\]

On the event of probability \(p_A\), (12.14) gives \(z\ge v\). Hence

\[
\dot f(t)
\ge
\frac{cp_A}{2}v(t)^4.
\tag{12.20}
\]

Near \(T_A\), equation (12.16) gives

\[
b(t)\asymp\frac1{cm(T_A-t)},
\]

and (12.15) gives the same order for \(v(t)\). Consequently

\[
\int_0^{T_A}v(t)^4\,dt=+\infty.
\tag{12.21}
\]

If \(f\) remained below \(y\) up to \(T_A\), integrating (12.20) would make
the finite output exceed every finite level, a contradiction. Thus the
first hitting time \(T_y\) satisfies

\[
T_y<T_A.
\]

Given any \(\delta>0\), choose \(A\) so large that

\[
T_A<\min\{\delta,\delta_0\}.
\]

Then \(T_y<\delta\). Since \(\delta\) is arbitrary:

### Conditional Theorem 12.1 — No positive subtarget delay under the asserted representation

\[
\boxed{
\text{No classical solution satisfying all assumptions can remain below}
\ y\in(0,1)\ \text{on a positive interval.}
}
\tag{12.22}
\]

Equivalently, if such a classical solution exists far enough for its first
hitting time \(T_y\) to be defined, then \(T_y=0\). If no positive-time
classical solution exists, (12.22) is a nonexistence/continuity obstruction,
not the assertion of a hitting time for a constructed flow.

The Gaussian tail probability \(p_A\) tends to zero with \(A\), but for each
fixed \(A\) it is strictly positive, while the comparison fourth-moment
integral is infinite.

### 12.6 The selected relaxed loss trace

For an ordinary squared-loss trajectory starting below the label,

\[
r(t)
=r(0)
\exp\!\left(-2\int_0^t\kappa(s)\,ds\right),
\]

so \(f\) is nondecreasing and does not overshoot \(1\). If one now imposes
the additional relaxed-selection rule that preserves these two properties,
(12.22) forces

\[
f(t)=1
\qquad(t>0).
\]

Since \(f(0)=0\),

\[
\boxed{
\mathcal L_{\mathrm{rel}}(t)
=
\begin{cases}
1,&t=0,\\
0,&t>0.
\end{cases}
}
\tag{12.23}
\]

More precisely, no classical output continuous at initialization can satisfy
all of the asserted equations and response hypotheses.  The displayed step
is a **stipulated selected trace**, not a constructed self-consistent DMFT
flow.  Monotonicity/no overshoot is an additional selection axiom; it is not
forced by a positive-time existence or uniqueness theorem in the corpus.

### 12.7 Continuity lower bound for the stipulated trace

Let \(\widehat{\mathcal L}\) be any continuous predicted loss and set

\[
E
=
\sup_{t\ge0}
|\widehat{\mathcal L}(t)-\mathcal L_{\mathrm{rel}}(t)|.
\]

At \(t=0\),

\[
|\widehat{\mathcal L}(0)-1|\le E.
\tag{12.24}
\]

For positive \(t\downarrow0\), the target is zero. Continuity gives

\[
|\widehat{\mathcal L}(0)|\le E.
\tag{12.25}
\]

The triangle inequality yields

\[
1
\le
|1-\widehat{\mathcal L}(0)|
+|\widehat{\mathcal L}(0)|
\le2E.
\]

Therefore

\[
\boxed{E\ge\frac12.}
\tag{12.26}
\]

If the closure matches the correct initialization,

\[
\widehat{\mathcal L}(0)=1,
\]

then for \(t\downarrow0\),

\[
|\widehat{\mathcal L}(t)-0|
\longrightarrow1,
\]

so

\[
\boxed{E\ge1.}
\tag{12.27}
\]

### Conditional Theorem 12.2 — Continuity no-go for the selected relaxed step trace

No family of continuous finite-dimensional autonomous closures can
approximate the selected relaxed loss (12.23) with arbitrarily small
uniform error on \([0,\infty)\).

The numerical dimension, autonomy, and one-source syntax are not used in the
lower bound; continuity alone suffices. Those extra conditions specify the
intended closure class and exclude an impulsive source that simply writes the
step by fiat.  Its relevance to the network is conditional on every upstream
representation, response, self-consistency, and selection assumption.

---

## 13. Normalized variants: what is and is not closed

The normalization report changes the architecture. Its results must not be
silently attributed to the raw model, and the raw positivity proof must not
be silently transferred to the normalized models.

### 13.1 RMSNorm after both hidden activations

For a vector \(x\), define true across-width RMS normalization

\[
N(x)
=
\frac{\phi(x)}
{\sqrt{\langle\phi(x)^2\rangle+\varepsilon}},
\tag{13.1}
\]

with the denominator recomputed throughout training. In the primary model
\(\varepsilon=0\), there is no learned gain and no centering.

Writing

\[
u^{(1)}=N_1(z^{(1)}),
\qquad
z^{(2)}=Wu^{(1)},
\qquad
u^{(2)}=N_2(z^{(2)}),
\qquad
f=\langle a,u^{(2)}\rangle,
\]

the normalized-activation Jacobian is

\[
J_\ell
=
\frac1{s_\ell}
\left(I-u^{(\ell)}\otimes u^{(\ell)}\right)
\operatorname{diag}\phi'(z^{(\ell)}).
\tag{13.2}
\]

The second-layer backpropagated message is

\[
\delta_2
=J_2^*a
=
\frac{\phi'(z^{(2)})}{s_2}
\odot\bigl(a-fu^{(2)}\bigr).
\tag{13.3}
\]

Already (13.2)--(13.3) show why the raw positive primitive cone is lost:
there are negative projection terms and derivatives of reciprocal
normalization factors.

The full feature vector field is

\[
D_+a=u^{(2)},
\]

\[
D_+W=\frac1n\delta_2(u^{(1)})^\top,
\]

\[
D_+z^{(1)}=\delta_1,
\qquad
D_+z^{(2)}=\delta_2+WJ_1\delta_1.
\tag{13.4}
\]

Differentiating \(J_\ell\) repeatedly creates:

1. derivatives of \(s_\ell^{-1}\), indexed by product and Bell partitions;
2. derivatives of
   \(I-u^{(\ell)}\otimes u^{(\ell)}\), producing new outer-product
   attachments;
3. new population contractions such as
   \(\langle h^{(p)},h^{(q)}\rangle\);
4. the raw ordered \(W/W^\top\) reuse words.

Thus RMSNorm fixes one second moment per layer but does not determine all
higher mixed moments or messages.  This establishes proliferation in the
displayed derivative grammar; by itself it is not a dimension lower bound
against a nonlinear or operator-valued compression of the fully trained
system.

### 13.2 Exact frozen-block recurrence for RMSNorm

The non-invariance can be seen without the full message grammar. Freeze the
lower hidden block, keep the quadratic activation, and train the top feature
and readout under final RMSNorm. Define

\[
M_{p,r}=\mathbb E[a^pz^r],
\qquad
R^2=M_{0,4},
\qquad
f=\frac{M_{1,2}}R.
\tag{13.5}
\]

The exact particle equations are

\[
\dot a=\frac{z^2}{R},
\qquad
\dot z
=
\frac{2z}{R}
\left(a-\frac{fz^2}{R}\right).
\tag{13.6}
\]

Differentiate \(a^pz^r\):

\[
\frac d{d\tau}(a^pz^r)
=
pa^{p-1}z^r\dot a
+
ra^pz^{r-1}\dot z.
\]

Substituting (13.6) and taking expectation gives

\[
\boxed{
\dot M_{p,r}
=
\frac pR M_{p-1,r+2}
+
\frac{2r}{R}M_{p+1,r}
-
\frac{2rf}{R^2}M_{p,r+2}.
}
\tag{13.7}
\]

For arbitrary large boundary indices, (13.7) creates
\(M_{p+1,r}\) or \(M_{p,r+2}\). Their coefficients are not algebraically
zero. Therefore no finite cutoff by polynomial degree, or any finite
rectangular cutoff in \((p,r)\), is invariant under this natural hierarchy.

This proves exact non-invariance of every finite degree or rectangular cutoff
in the displayed ordinary monomial-moment hierarchy. It does not prove that
no nonlinear finite statistic could approximate the observable.

### 13.3 Direction-only weight normalization

For direct projected gradient on a weight sphere,

\[
D_+w=P_wG,
\qquad
P_w
=I-\frac{ww^\top}{\|w\|^2}.
\tag{13.8}
\]

For the global rescaled readout vector, with

\[
C=\langle a^2\rangle,
\]

the projected equation is

\[
\boxed{
D_+a=h^{(2)}-\frac fC a.
}
\tag{13.9}
\]

The negative radial subtraction again destroys the raw coefficientwise
positive cone.

For a hidden row,

\[
D_+W_j
=
\frac{a_j\phi'(z_j)}{n}
\left(
h^{(1)}-\frac{z_j}{\|W_j\|^2}W_j
\right).
\tag{13.10}
\]

Under the large-fan-in convention, the hidden radial correction to the
preactivation derivative is \(O(n^{-1})\) at every fixed Wick order. The
global readout projection (13.9) remains \(O(1)\).

Repeated differentiation of \(P_w\) creates outer-product projector words:

\[
P_w^{(m)}
=
-\frac1{\|w\|^2}
\sum_{p=0}^m
\binom mp
w^{(p)}(w^{(m-p)})^\top.
\tag{13.11}
\]

Thus direction-only WN removes radial modes but not the tangential
noncommutative message hierarchy in this grammar.  As above, message
generation is diagnostic and does not alone prove a full-system
no-compression theorem.

### 13.4 Exact frozen-block recurrence for readout WN

Freeze the lower hidden block. With

\[
q=\mathbb E[(h^{(1)})^2],
\qquad
C=1,
\]

the top-block particle equations are

\[
\dot a=\frac12z^2-fa,
\qquad
\dot z=qaz,
\qquad
f=\frac12\mathbb E[az^2].
\tag{13.12}
\]

For \(M_{p,r}=\mathbb E[a^pz^r]\),

\[
\begin{aligned}
\dot M_{p,r}
&=
\mathbb E\!\left[
pa^{p-1}z^r\left(\frac12z^2-fa\right)
+
ra^pz^{r-1}(qaz)
\right]\\
&=
\boxed{
\frac p2M_{p-1,r+2}
-pfM_{p,r}
+rqM_{p+1,r}.
}
\tag{13.13}
\end{aligned}
\]

Again the derivative raises \(p\) or \(r\) at every boundary of a finite
degree set. Hence the natural monomial hierarchy has no finite invariant
degree cutoff.

### 13.5 Why the raw zero-radius theorem does not automatically transfer

For the raw quadratic network, every primitive coefficient was nonnegative.
RMSNorm contains

\[
a-fu
\]

and alternating derivatives of \(s^{-1}\). Readout WN contains

\[
-\frac fC a.
\]

Surviving Wick graphs can therefore cancel. The embedded raw scalar word is
no longer automatically a lower bound on the complete normalized
coefficient.

The low-order formal annealed calculation makes the change concrete. At
\(\gamma=4/3\), encode the jet by

\[
F(\tau)\equiv A\tau+\frac{B}{3!}\tau^3\pmod{\tau^5},
\]

the repository obtains

\[
\begin{array}{c|cc}
\text{model}&A&F'''(0)=B\\ \hline
\text{raw}&\dfrac{17}{6}&\dfrac{229957}{216}\\[2mm]
\text{global readout direction-WN}
&\dfrac{17}{6}&\dfrac{223939}{216}\\[2mm]
\text{RMSNorm after both hidden activations}
&\dfrac{34}{9}&-\dfrac{273712}{729}.
\end{array}
\tag{13.14}
\]

The RMS sign reversal proves that cancellation is substantive, not merely
formal.

Accordingly:

- zero radius is **not proved** for RMSNorm;
- zero radius is **not proved** for global readout WN;
- every possible non-Taylor finite PDE remains unruled-out for these
  normalized variants;
- if WN is applied only to large-fan-in hidden rows and not to the readout,
  the source reports that its fixed-order corrections vanish under its
  large-fan-in assumptions, so the raw **formal-jet** Taylor no-go transfers
  in that convention if the stated fixed-order reduction is valid.

The last item is a fixed-order reduction to Theorem 7.1, not a new
all-compilers theorem.

---

## 14. Claim ledger: proved, conditional, and open

### 14.1 Unconditional results at their stated scope

1. **The formal annealed Wick--Taylor compiler fails.**  The exact quadratic
   forest compiler and positive all-order subfamily give a zero-radius formal
   coefficient sequence.  Its prescribed positive Taylor profiles diverge,
   and the corresponding closure losses are not uniformly Cauchy.  This
   refutes (8.5), but does not identify an actual positive-time loss.

2. **The displayed frozen monomial cutoffs are non-invariant.**  Equations
   (13.7) and (13.13), and their raw counterparts, raise the boundary degree.
   This is not a theorem against nonlinear, operator-valued, or approximate
   compression of the fully trained hierarchy.

3. **Several realization classes cannot reproduce the formal jet.**  The
   regular analytic one-space realization, positive classical semigroup,
   coefficientwise-positive polynomial compiler, and positive-stage
   Euler/Wick classes are excluded under the exact hypotheses in Sections
   10.1--10.4.  Singular equations and signed real-axis constructions are not
   covered.

4. **Two ambient topology packages fail.**  Product \(L^2\) control alone
   does not control the cubic observable, and one Banach space with continuous
   \(X\to L^1\) embedding and globally bounded pointwise multiplication
   cannot contain a nondegenerate Gaussian coordinate.  Neither statement is
   a no-go for all stronger or structured Gaussian state spaces.

### 14.2 Exact implications under additional hypotheses

1. The residual-clock stability theorem proves
   \[
   \text{small profile/kernel defect}
   \Longrightarrow
   \text{small global loss defect}.
   \]
   It does not establish the small-defect premise.

2. The conditional DMFT implication proved in Section 12 is
   \[
   \begin{gathered}
   \text{asserted tagged-site Volterra representation and response laws}
   \\
   \Longrightarrow\ \text{no positive subtarget delay for a classical solution},
   \\
   \text{plus monotone/no-overshoot relaxed selection}
   \\
   \Longrightarrow\ \text{selected step trace and continuity lower bound}.
   \end{gathered}
   \]
   The representation, self-consistency, positive-time solution,
   network-to-DMFT identification, and selection are not established.

3. The noncommutative continuation-capacity argument becomes a no-go only
   under the freeness/faithfulness and branch-separation lemmas, as well as
   its bounded-filtration commuting-source grammar.  It does not cover the
   operator/integro-differential state class.

4. The hidden-row-only WN transfer additionally assumes the reported
   fixed-order large-fan-in reduction.  It is not an independent normalized
   positive-time theorem.

5. A generic Banach/Hilbert Galerkin convergence theorem is valid if one
   supplies a well-posed exact hierarchy, stable projections, continuity of
   the observable, and a vanishing outgoing residual.  Those model-specific
   premises remain open here.

### 14.3 Statements not proved

The repository does **not** prove any of the following.

- Concentration of every random initialization derivative \(C_{n,k}\), or
  identification of the formal annealed jet with derivatives of an actual
  width-first positive-time mean-field trajectory.
- Derivation, self-consistency, existence, or uniqueness of the asserted
  tagged-site DMFT for this network, or that the relaxed step selection is
  the network loss.
- The two missing continuation-capacity lemmas needed by N2.
- Every signed, nonanalytic, non-Taylor, certified real-axis finite compiler
  is impossible.
- A diagonal \(M=M(n)\) limit fails, or every fixed-\(n\) Taylor germ fails
  inside its own random convergence radius.
- The fully trained Gaussian network has the frozen subsystem's
  coordinatewise rare-particle comparison.
- The full raw or normalized trained system admits no finite nonlinear or
  operator-valued compressed state.
- RMSNorm or global readout WN has a zero-radius feature-time series.
- The quadratic no-go theorems transfer to the bounded residual-\(\tanh\),
  continuous-depth model.

---

## 15. How the headline results compare without conflating claim levels

### 15.1 Broadest surrogate exclusion after stipulating a target

Once the selected step trace \(\mathcal L_{\mathrm{rel}}\) is stipulated,
continuity alone excludes every continuous predicted loss with error below
\(1/2\), or below \(1\) under matched initialization.  This is broad in the
**surrogate class**, but weak as evidence about the network because the
target depends on the unproved DMFT representation and selection hypotheses.

### 15.2 Strongest unconditional formal-compiler result

The Wick--Taylor argument directly refutes the precise iterated shadowing
claim (8.5), requires no positive-time mean-field target, and has an internal
non-Cauchy contradiction.  Its subject is the formal annealed coefficient
sequence and its prescribed positive Taylor family.  Signed, non-Taylor, or
singular real-axis methods are not covered.

### 15.3 Exact restricted-hierarchy witnesses

The frozen raw, RMSNorm, and readout-WN recurrences prove non-invariance of
ordinary finite degree/rectangular monomial cutoffs.  This is stronger than a
low-order mismatch but weaker than either an approximation no-go or a
full-system dimension lower bound; a non-invariant hierarchy may still admit
accurate projections or compressed operator states.

---

## 16. Supersession and non-transfer

### 16.1 What the later resolution changed

The stability report originally reduced the positive PDE theorem to the tail
claim

\[
\varepsilon_M(T)\to0.
\]

The zero-radius report did not merely leave this lemma open: it proved that
the ordinary Wick--Taylor source sequence behaves in the opposite way. Thus:

\[
\boxed{
\text{residual-clock stability survives;}
\quad
\text{ordinary Wick--Taylor approximation does not.}
}
\]

The later causal-DMFT report proposed a stronger-looking real-time
**conditional implication** for continuous closures of a selected relaxed
step target.  The v2.2 audit superseded its promotion to a network theorem
because the tagged-site representation and relaxed selection were not
derived.

### 16.2 What was not superseded

The following remain valid with the scopes used in this report:

- the special quadratic compiler computes the formal annealed fixed-order
  coefficients, while concentration is separate;
- the residual-clock identity is exact;
- a known small profile/kernel error gives a global loss error bound;
- the analytic and positive-compiler no-gos remain valid for exact
  realizations of that formal jet;
- signed non-Taylor real-axis compilers lie outside the Wick-positive
  theorems.

### 16.3 Why the later continuous-depth reports are not additional quadratic proofs

The later principal model uses bounded residual \(\tanh\), residual depth,
and an operator--Hermite Liouville PDE. Its phrase “complete quadratic
\(P=15\)” denotes quadratic **Hermite basis degree**, not the activation
\(\phi(u)=u^2/2\).

The later master reports expressly state:

- the unbounded polynomial feedback and Gaussian readout tail are
  model-specific;
- the training-time zero-radius result does not obstruct the separate
  depth-Volterra/Dyson factorial mechanism;
- early adverse Hermite-order comparisons were later corrected by parity
  analysis and are not non-closure theorems;
- convergence of that bounded-model Hermite hierarchy remains open.

Therefore none of those experiments should be added to the list of proved
quadratic-activation non-closure theorems.

---

## 17. Compact theorem ledger

| Theorem | Target/model | Closure class excluded | Complete? | Main dependency |
|---|---|---|---|---|
| Factorial lower bound and zero radius | Raw quadratic/Gaussian formal annealed jet | Ordinary Taylor series for that jet | Yes at formal-jet level | Exact special-case forest compiler and positive all-order subfamily |
| Physical-time boundary layer | Prescribed formal Taylor family | Degree-\(M\) zero-flux source PDE | Yes for that family | Zero radius and positivity; not an actual network loss |
| Global-shadowing conjecture false | Iterated \(n\to\infty\), then \(M\to\infty\), as in (8.5) | Prescribed Wick--Taylor closures | Yes | Non-uniform-Cauchy argument |
| Regular analytic realization no-go | Formal annealed jet | One-space bounded analytic exact realization | Yes for stated class | Exact reproduction of the jet and zero radius |
| Positive semigroup no-go | Formal annealed jet | Positive classical semigroup with continuous Wick readout | Yes for stated class | Cone/domain/continuity hypotheses |
| Positive polynomial compiler no-go | Formal annealed jet | Nonnegative fixed-order-consistent source polynomials | Yes for stated class | Zero radius and positivity |
| Euler/positive-stage no-go | Formal annealed jet | Wick-positive consistent polynomial step methods | Yes for stated class | Binomial lower bound |
| \(L^2\) discontinuity | Ambient cubic readout | Product-\(L^2\) control alone | Yes as a functional witness | Explicit rare-set sequence; no reachability claim |
| Gaussian Banach-algebra obstruction | Gaussian coordinate | One space with \(X\to L^1\) and globally bounded multiplication | Yes for stated package | \(L^m\to L^\infty\) argument |
| Frozen Gaussian cutoff singularity | Frozen first-layer reduction | Naive compact-cutoff/particle route | Scoped subsystem argument | Cooperative Riccati growth; no full-model transfer |
| Noncommutative continuation capacity | Bounded-filtration commuting-source finite-jet encoder | Exact branchwise continuation | **Conditional** | Freeness/faithfulness and branch separation remain open |
| No positive subtarget delay | Postulated tagged-site Volterra system | Classical subtarget-delayed output satisfying all assumptions | **Conditional** | Asserted representation, response, continuity, output inequality; hitting time is zero only if defined |
| Step-vs-continuous lower bound | Selected relaxed step trace \(\mathcal L_{\mathrm{rel}}\) | Every continuous loss predictor | Yes for stipulated trace; network relevance conditional | Upstream DMFT assumptions plus extra selection rule |
| RMS frozen-cutoff nonclosure | Frozen RMSNorm top block | Finite rectangular monomial cutoff | Yes | Recurrence (13.7) |
| WN frozen-cutoff nonclosure | Frozen direction-WN top block | Finite rectangular monomial cutoff | Yes | Recurrence (13.13) |
| Broad signed real-axis no-go | Full raw or normalized model | Every admissible finite compiler | **No** | Quantitative residual/noncompactness lower bound still absent outside the step-target class |

---

## 18. Source concordance

For reproducibility, the source roles are:

1. **`approximate_single_source_conjecture_resolution.md`**
   Sections 1--5 give the raw model, selected scalar history, positivity, and
   factorial bound.  Read with the current exact quadratic compiler, these
   prove zero radius for the formal annealed jet.  Section 6 proves failure of
   the prescribed Taylor-closure family, not a step loss for the network.

2. **`approximate_single_source_stability.md`**
   Sections 1--4 give the residual clock and positive-entry coercivity.
   Sections 5--7 give the finite source PDE, clock-shadowing, and
   input-to-state stability. Section 9 explicitly isolates the tail lemma
   that the later zero-radius result disproves for this compiler.

3. **`adversarial_audit_report.md`**
   Sections 1--3 distinguish oracle existence from closure. Section 4 gives
   the \(L^2\), Banach-algebra, analytic, semigroup, positive compiler,
   Euler/Wick, and frozen-tail witnesses, each under its displayed scope.
   Sections 5--7 state the surviving open signed real-axis problem.

4. **`mean_field_single_source_conjecture_audited_resolution.md`**
   Sections 2--7 give a comparison conditional on an asserted tagged-site
   representation and response law. Sections 8--10 add a relaxed-selection
   axiom and derive the continuity lower bound for the resulting stipulated
   step trace.  This source is not a network-to-DMFT derivation.

5. **`normalized_mean_field_taylor_closure_audit.md`**
   Sections 3--5 derive the normalized vector fields and frozen reductions.
   The frozen recurrences prove non-invariance of ordinary monomial cutoffs;
   the full-system message grammar is diagnostic.  The source also explains
   why the raw positivity proof does not transfer.

6. **Current authority.**
   `studies/mean_field_peeling/CURRENT_RESEARCH_STATE.md` supplies the exact
   special quadratic annealed compiler while explicitly leaving
   concentration and positive-time identification open.
   `studies/stieltjes_conjecture/CURRENT_RESEARCH_STATE.md` preserves the same
   formal-jet distinction.  The v2.2 monograph classifies the tagged-site
   DMFT chain as exact only under its asserted representation and selection
   hypotheses.  Older master syntheses that promoted those claims are
   superseded.

---

## 19. Final answer in one paragraph

The strongest DMFT-related statement is conditional: if the asserted
tagged-site Volterra representation and response hypotheses hold, no
classical solution can have positive subtarget delay (equivalently, its
hitting time is zero if defined); if one additionally imposes the
monotone/no-overshoot relaxed selection, the stipulated step trace has
uniform distance at least \(1/2\) from every continuous surrogate, or \(1\)
under matched initialization.  This is not established for the canonical
network.  Independently, the exact quadratic compiler proves that the formal
annealed Wick jet has zero radius and that its prescribed positive Taylor
closures form an initial boundary layer and are not uniformly Cauchy.  This
does not construct an actual positive-time mean-field loss; concentration
and trajectory identification remain open.  The analytic, positive, \(L^2\),
Banach-algebra, noncommutative, and normalized-hierarchy arguments exclude
only their explicitly stated realization, topology, grammar, or frozen
cutoff classes.  No result here rules out every singular, signed,
nonanalytic, operator/integro-differential, or otherwise certified finite
real-axis description of the true network dynamics.
