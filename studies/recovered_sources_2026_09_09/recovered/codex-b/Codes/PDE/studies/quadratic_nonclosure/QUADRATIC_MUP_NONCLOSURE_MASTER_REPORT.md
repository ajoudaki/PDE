# Non-closure for the quadratic mean-field \(\mu\)P MLP

> **Historical synthesis with conditional claims.** This document preserves
> the strongest formulation assembled in the quadratic-nonclosure phase.  Its
> causal-DMFT and physical-time conclusions require the tagged-site/response
> and fixed-order expectation/covariance bridges named below; those bridges
> are not proved here.  For the current unconditional derivative calculus and
> exact fixed-order results, use the
> [mean-field-peeling report](../mean_field_peeling/CURRENT_RESEARCH_STATE.md).
> For the current output-kernel moment conjecture, use the
> [Stieltjes report](../stieltjes_conjecture/CURRENT_RESEARCH_STATE.md).

## Unified statements, proof chains, scope, and source provenance

### Executive conclusion

The repository contains one strongest model-level non-closure theorem and
several narrower but fully proved compiler, topology, and hierarchy
obstructions.

The strongest result is the causal mean-field result:

> For the canonical two-hidden-layer quadratic network with an unbounded
> Gaussian trainable readout, the natural monotone, no-overshoot causal-DMFT
> loss trace is
> \[
> \mathcal L_{\mathrm{MF}}(0)=1,
> \qquad
> \mathcal L_{\mathrm{MF}}(t)=0\quad(t>0).
> \]
> Consequently, every continuous finite-dimensional autonomous closure has
> uniform error at least \(1/2\); if it matches the correct initial loss, its
> uniform error is at least \(1\).

This is stronger than the earlier Wick--Taylor result because it is a
real-time obstruction and applies to every continuous finite-dimensional
closure of the stated pure-DMFT target, not only to a Taylor compiler. Its
scope is nevertheless exact and limited: it is a theorem about the canonical
tagged-site pure mean-field/DMFT model and its natural relaxed loss trace. It
is not a separate theorem that finite-width trajectories converge uniformly
to that discontinuous trace.

The strongest completely unconditional compiler result is:

> The formal fixed-order mean-field Wick--Taylor series has radius zero. Its
> positive degree-\(M\) source profiles diverge at every positive feature
> time, and their residual-clock loss curves form an initial boundary layer.
> Hence the precise iterated global-shadowing conjecture for that one-source
> Taylor PDE is false, without needing to assume that the true finite-width
> losses possess a regular large-width limit.

No result in the repository proves that **every** signed, nonanalytic,
non-Taylor, accuracy-dependent real-axis finite compiler is impossible. The
reports explicitly preserve that distinction.

---

## 1. First list: every non-closure or no-go result found

The following list separates distinct mathematical statements instead of
combining them under the ambiguous phrase “no finite PDE.”

| ID | Result | Exact force |
|---|---|---|
| N1 | **No finite natural polynomial-moment cutoff is invariant.** Even frozen-block moment equations send \(M_{p,r}\) to moments with larger \(p\) or \(r\). The full model additionally generates ordered matrix-reuse messages. | Exact non-closure of the natural moment/message hierarchy; not impossibility of every finite representation. |
| N2 | **Exact continuation-faithful closure by current low-order moments/Grams is obstructed by noncommutative matrix reuse.** Future tagged continuations distinguish histories that an untagged scalar aggregate merges. | Reported as an earlier exact result, but the complete quadratic-model proof is not reproduced in the available source set. |
| N3 | **Zero radius of the limiting Wick jet.** Along odd \(k\), the coefficient \(c_k\) has a factorial lower bound, so \(\limsup c_k^{1/k}=+\infty\). | Complete theorem, using the repository’s previously established fixed-order Wick/concentration limit. |
| N4 | **Divergence of the ordinary positive Wick--Taylor source profiles.** For every \(s>0\), \(H_M(s)\to+\infty\). | Complete corollary of N3 and coefficient positivity. |
| N5 | **Failure of the associated one-source PDE in physical time.** Its losses converge pointwise to a step and are not uniformly Cauchy on any interval containing \(0\). | Complete disproof of the precise Wick--Taylor global-shadowing conjecture. |
| N6 | **Real target fitting does not imply that the target lies inside the initial Taylor disk.** An invariant finite-width symmetric orbit has a backward complex/real singularity closer than its forward target time. | Complete counterexample to that proof route; not a typical-Gaussian mean-field theorem. |
| N7 | **No exact one-Banach-space bounded analytic hierarchy realization.** Such a realization would force positive Taylor radius, contradicting N3. | Complete no-go for this analytic realization class. |
| N8 | **No positive classical semigroup completion preserving all local derivatives and a continuous Wick readout.** Positivity makes every Taylor partial sum a lower bound, which diverges. | Complete no-go under the displayed semigroup hypotheses. |
| N9 | **No coefficientwise-positive, fixed-order-consistent polynomial compiler.** Recovering every \(c_k\) while keeping nonnegative coefficients forces divergence at every positive source value. | Complete class-level compiler no-go. |
| N10 | **Explicit symbolic Euler/Wick and positive-stage polynomial compilers diverge under mesh refinement.** A binomial selection of \(k\) first-order generator hits recovers the divergent \(c_k\) lower bound. | Complete for the stated Wick-positive consistent polynomial one-step class. |
| N11 | **Initialization derivatives alone do not identify a positive-time real-axis profile.** Once analyticity fails, flat functions can change the positive-time curve without changing any derivative at \(0\). | Complete semantic obstruction to an uncertified jet-only continuation rule; not a no-go for independently justified resummation. |
| N12 | **Ordinary Gaussian \(L^2\) is not a closure topology for the cubic readout.** Vanishing \(L^2\) perturbations can change the readout by order one. | Complete topology counterexample; it invalidates unqualified \(L^2\) Galerkin/minimizing-movement arguments. |
| N13 | **No single Banach function algebra with bounded multiplication, continuous embedding into \(L^1\), and nondegenerate Gaussian coordinates.** Such an algebra embeds into \(L^\infty\). | Complete functional-analytic obstruction to the most direct one-space polynomial theory. |
| N14 | **Gaussian compact truncation can be dynamically singular in the frozen-first-layer subsystem.** Extreme positive particles drive target times to \(0\) as the cutoff grows. | Complete for the frozen subsystem; it is not automatically a full-model theorem because the additional matrix message is not coordinatewise positive. |
| N15 | **Instantaneous fitting in the canonical causal DMFT.** Positive initial self-response plus the unbounded Gaussian readout tail makes every subtarget hitting time zero. | Complete real-time comparison theorem within the tagged-site DMFT assumptions. |
| N16 | **No uniformly accurate continuous finite closure of the natural relaxed DMFT loss.** Every continuous surrogate has error at least \(1/2\), or \(1\) with exact initialization. | Strongest model-level result; an elementary corollary of N15 and the natural monotone/no-overshoot selection. |
| N17 | **RMSNorm and global direction-only WN do not create exact finite natural moment/message closure.** Their recurrences and differentiated projectors generate unbounded moment/message families. | Complete for natural finite-degree/message cutoffs; not a theorem against every non-Taylor finite PDE. |
| N18 | **The raw positive-coefficient zero-radius proof does not transfer to RMSNorm or global readout WN.** Signed projection and reciprocal-normalization terms permit cancellations. | A proved limitation on transferring N3, not a positive closure theorem. Hidden-row-only WN is a separate large-fan-in case in which fixed-order corrections vanish. |

Two nearby statements are important but are not themselves non-closure
theorems:

1. An unrestricted “some finite one-source PDE exists” statement is vacuous:
   any continuous scalar curve can be approximated by an oracle Bernstein
   polynomial and packed into two states.
2. Squared loss gives a genuine residual-clock stability theorem: an already
   small feature-profile or tangent-kernel error produces a uniform-in-physical-
   time loss error. It does not make an unproved hierarchy tail small.

---

## 2. Second list: the short list completely resolved in the repository

The later master reports preserve the following three headline conclusions as
the authoritative quadratic-model results.

### R1. Ordinary Wick--Taylor closure is disproved

The limiting initial Wick series has radius zero; its positive partial sums
diverge at every \(s>0\); and the induced physical-time closures fail
uniformly. This fully resolves the **concrete Wick--Taylor one-source
conjecture**, but not every non-Taylor compiler.

Primary proof: `approximate_single_source_conjecture_resolution(1).md`.

### R2. Continuous uniform finite closure of the natural pure-DMFT loss is impossible

The causal-DMFT comparison gives instantaneous fitting and hence a step loss.
The \(1/2\) continuity lower bound, sharpened to \(1\) under exact
initialization, completely resolves the **continuous, autonomous,
uniform-in-time finite-closure conjecture for that natural relaxed pure-DMFT
target**.

Primary proof:
`mean_field_single_source_conjecture_audited_resolution(2).md`.

This theorem is already posed after the mean-field reduction. It does not
claim a separate uniform finite-width-to-DMFT convergence theorem.

### R3. Exact natural moment/message closure remains impossible after the audited normalizations

RMSNorm and direction-only WN do not make any finite polynomial-moment or
natural message cutoff invariant. This completely resolves that narrower
exact-hierarchy question. It does not resolve the broader existence of a
signed, non-Taylor, accuracy-dependent real-axis PDE.

Primary proof: `normalized_mean_field_taylor_closure_audit(1).md`.

### Supporting results that are also completely proved, but are not separate broad conjecture resolutions

N6--N14 are rigorous counterexamples or class-level corollaries within their
stated hypotheses. They strengthen the explanation of why several proposed
proof routes fail, but they should not be promoted to a theorem against every
admissible finite PDE.

The earlier exact noncommutative continuation result N2 is repeatedly cited,
but its complete quadratic-model theorem and proof are not present in the
available files. It therefore should not be silently reconstructed as a new
headline theorem here.

---

## 3. Which documents actually contain the proofs?

### Primary proof sources

| Source | Role |
|---|---|
| `approximate_single_source_conjecture_resolution(1).md` | Exact model; embedded positive scalar branch; no-cancellation argument; factorial lower bound; zero radius; physical-time boundary layer; invariant-manifold Taylor-disk counterexample. |
| `approximate_single_source_stability(1).md` | Surviving residual-clock, coercivity, clock-shadowing, and input-to-state stability theorems; exact finite source-PDE algebra; explicit statement of the missing tail lemma later disproved. |
| `adversarial_audit_report(1).md` | Anti-oracle formulation; analytic, semigroup, positive-compiler, Euler/Wick, \(L^2\), Banach-algebra, and frozen-tail obstructions; exact boundary between proved no-gos and open signed real-axis compilers. |
| `mean_field_single_source_conjecture_audited_resolution(2).md` | Tagged-site causal-DMFT setup; positive self-response; positive cavity event; cooperative Riccati comparison; zero hitting times; step loss; uniform-continuity lower bound. |
| `normalized_mean_field_taylor_closure_audit(1).md` | RMSNorm and direction-only WN vector fields, moment recurrences, signed-cancellation analysis, and exact natural-hierarchy non-closure. |

### Later synthesis and scope sources

`MASTER_NEURAL_PDE_REPORT_2026-07-26(1).md` and
`MASTER_NEURAL_PDE_REPORT_WITH_FIGURES.md` preserve R1--R3 as established,
model-specific results. They do not reproduce the complete proofs.

The continuous-depth reports use a bounded residual-\(\tanh\) model. Their
Hermite phrase “complete quadratic” refers to basis degree, not quadratic
activation. Their continuation, rank, compactness, and topology
counterexamples are distinct results and are not additional proofs of R1--R3.

The two files named `PDE_GENERALIZATION_FINAL_REPORT(2).md` and
`PDE_GENERALIZATION_FINAL_REPORT(3).md` are byte-identical. Neither supplies a
new non-closure theorem.

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
   usually
   \[
   \sup_{t\ge0}
   |\widehat{\mathcal L}_\varepsilon(t)-\mathcal L_{\mathrm{MF}}(t)|
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

Failure of question 1, 2, or 3 does not by itself answer question 4. The
causal-DMFT step theorem answers question 4 only for continuous closures of
the specified natural relaxed pure-DMFT loss.

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

Suppress the single fixed input and write

\[
x_i=z_i^{(1)},
\qquad
h_i=\frac{x_i^2}{2},
\]

\[
z_j=\sum_{i=1}^n W_{ji}h_i,
\qquad
f_n=\frac1{2n}\sum_{j=1}^n a_jz_j^2.
\]

Here \(a_j\) is the rescaled readout coordinate. In raw coordinates the
readout weight is \(W_j^{(3)}=a_j/n\), so
\(W_j^{(3)}(0)\sim N(0,n^{-2})\).

Initialization is independent:

\[
x_i\sim N(0,1),
\qquad
a_j\sim N(0,1),
\qquad
W_{ji}\sim N\!\left(0,\frac{\gamma}{n}\right),
\quad \gamma>0.
\]

The label is \(1\) and

\[
\mathcal L_n=(1-f_n)^2.
\]

### 5.2 Feature-ascent derivation

Let \(D_{+,n}\) be the \(\mu\)P gradient-ascent derivation of the readout:

\[
D_{+,n}x_i=n\frac{\partial f_n}{\partial x_i},
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
D_{+,n}x_i=x_i\sum_jW_{ji}a_jz_j.
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

Differentiating \(z=Wh\), using \(D h_i=x_iD x_i\), gives

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
H_n(\tau)=f_n(\Theta_n(\tau)).
\]

Then

\[
H_n'(\tau)=\kappa_n(\Theta_n(\tau))\ge0,
\tag{5.5}
\]

where \(\kappa_n\) is the \(\mu\)P tangent kernel, a sum of squared metric
gradients.

Physical squared-loss gradient flow follows the same parameter orbit with

\[
\dot\tau_n(t)=2\bigl(1-H_n(\tau_n(t))\bigr),
\qquad
f_n(t)=H_n(\tau_n(t)).
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

The repository’s fixed-order Wick/concentration calculus establishes, for
every fixed \(k\), a deterministic limit

\[
c_k
=
\lim_{n\to\infty}
\frac{D_{+,n}^kf_n(0)}{k!},
\tag{5.8}
\]

in probability and in \(L^1\). The proof uses a finite derivative-diagram
expansion at fixed \(k\), Gaussian Wick contraction, second-moment power
counting, and fixed-degree hypercontractivity for uniform integrability.

This fixed-order theorem is an input to the zero-radius result. It is crucial
that it holds **for each fixed \(k\)**; it does not supply a bound uniform in
\(k\).

At initialization,

\[
q_n\longrightarrow q_0
=\mathbb E\!\left[\left(\frac{G^2}{2}\right)^2\right]
=\frac34.
\tag{5.9}
\]

---

## 6. Common positive result: residual-clock observable stability

This section is included because it identifies exactly what the negative
results do and do not destroy.

Let \(H\) and \(\widetilde H\) be increasing feature-time profiles with the
same initial output \(f_0<1\). Suppose both reach \(1\), and on a common
target-reaching interval

\[
0<\mu\le H'(\tau)\le K,
\qquad
\|H-\widetilde H\|_\infty\le\varepsilon.
\tag{6.1}
\]

Let their residual clocks solve

\[
\dot\tau=2(1-H(\tau)),
\qquad
\dot{\widetilde\tau}
=2(1-\widetilde H(\widetilde\tau)).
\]

Set \(e=\widetilde\tau-\tau\). If \(e>0\), monotonicity gives

\[
\dot e
=2\bigl(H(\tau)-\widetilde H(\widetilde\tau)\bigr)
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
|H(\tau(t))-\widetilde H(\widetilde\tau(t))|
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
interval.

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
a_jW_{ji}W_{j\ell}x_i^2x_\ell^2.
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

The no-cancellation comparison and the fixed-order \(L^1\) limit (5.8)
therefore prove:

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

This conclusion concerns the deterministic iterated fixed-order
mean-field series. If a macroscopic profile \(H\) exists and satisfies
\(H^{(k)}(0)=k!c_k\), then \(H\) is not analytic at \(0\) and this Taylor
series cannot represent it. Without that extra identification, the exact
statement is the zero radius of the **formal limiting Wick series**.

---

## 8. Failure of the one-source Wick--Taylor PDE

### 8.1 The exact conjecture

Define the degree-\(M\) source profile

\[
H_M(s)=\sum_{k=0}^M c_ks^k.
\tag{8.1}
\]

The proposed one-field, one-source closure is

\[
\partial_tU_M(t,s)
=
2\bigl(1-U_M(t,0)\bigr)\partial_sU_M(t,s),
\qquad
U_M(0,s)=H_M(s).
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

The sharpened conjecture was

\[
\boxed{
\lim_{M\to\infty}
\limsup_{n\to\infty}
\sup_{t\ge0}
|\mathcal L_M(t)-\mathcal L_n(t)|
=0.
}
\tag{8.5}
\]

The order of limits is part of the statement: first the fixed-order
mean-field coefficients are taken, then the source order \(M\) is increased.

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
H_M(s)\longrightarrow+\infty
\quad\text{for every }s>0.
}
\tag{8.6}
\]

For \(y\in(0,1)\), let \(r_M(y)\) be the first positive solution of

\[
H_M(r_M(y))=y.
\]

For every odd \(k\le M\),

\[
y=H_M(r_M(y))
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
=2\bigl(1-H_M(s_M(t))\bigr),
\qquad
s_M(0)=0,
\tag{8.8}
\]

and

\[
f_M(t)=H_M(s_M(t)).
\]

The physical time required to reach output \(y\in(0,1)\) is

\[
t_M(y)
=
\int_0^{r_M(y)}
\frac{ds}{2(1-H_M(s))}.
\tag{8.9}
\]

For \(0\le s\le r_M(y)\),

\[
0\le H_M(s)\le y,
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

### 8.4 Direct contradiction to the global-shadowing conjecture

The conclusion does not require a regular limiting true loss curve.
Suppose (8.5) were true. Then, for any \(M,M'\),

\[
\begin{aligned}
\|\mathcal L_M-\mathcal L_{M'}\|_\infty
&\le
\|\mathcal L_M-\mathcal L_n\|_\infty
+\|\mathcal L_n-\mathcal L_{M'}\|_\infty.
\end{aligned}
\]

Taking \(\limsup_{n\to\infty}\) and then large \(M,M'\) would force
\((\mathcal L_M)\) to be uniformly Cauchy. But (8.11)--(8.12) show that it
is not uniformly Cauchy on any interval containing zero. Therefore:

### Theorem 8.1 — Failure of the Wick--Taylor closure conjecture

\[
\boxed{\text{The conjecture \((8.5)\) is false.}}
\]

The theorem does not address a diagonal limit \(M=M(n)\), a fixed-\(n\)
Taylor germ inside its random convergence disk, or a signed/non-Taylor
real-axis compiler.

---

## 9. Real fitting does not imply Taylor-disk coverage

The repository also gives a deterministic finite-width counterexample to the
argument “the real trajectory reaches the target stably, therefore its
initial Taylor series reaches that far.”

Consider the invariant symmetric manifold

\[
x_i=x,
\qquad
a_j=a,
\qquad
W_{ji}=\frac wn.
\]

Equations (5.1)--(5.3) reduce to

\[
f=\frac18aw^2x^4,
\]

\[
a'=\frac18w^2x^4,
\qquad
w'=\frac14awx^4,
\qquad
x'=\frac12aw^2x^3.
\tag{9.1}
\]

Choose

\[
a(0)=-1,
\qquad
w(0)=2,
\qquad
x(0)=\sqrt8.
\tag{9.2}
\]

Differentiate

\[
w^2-2a^2
\quad\text{and}\quad
x^2-4a^2
\]

using (9.1). Both derivatives vanish. Their initial values are \(2\) and
\(4\), so

\[
w^2=2(1+a^2),
\qquad
x^2=4(1+a^2).
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
without claiming a no-go against every possible real-axis compiler.

### 10.1 No one-space bounded analytic realization

Assume there is a Banach space \(X\), an initial state \(Y_0\in X\), and an
exact realization

\[
Y'=F(Y),
\qquad
H'=K(Y),
\tag{10.1}
\]

where \(F\) and \(K\) are analytic near \(Y_0\). This includes a
representation in which all polynomial attachment and contraction rules are
bounded multilinear maps on one Banach space.

The analytic Banach-space ODE theorem makes \(Y(\tau)\) analytic for
\(|\tau|<R\) for some \(R>0\). Then \(K(Y(\tau))\), and after integration
\(H(\tau)\), are analytic on a possibly smaller disk. Cauchy estimates give

\[
\frac{|H^{(k)}(0)|}{k!}\le CR^{-k}.
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

Thus \(H\) and \(H+\psi\) have the same complete initialization jet and
different positive-time behavior. Once analyticity is unavailable, a jet
does not select its own continuation.

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

This invalidates any argument that uses only \(L^2\) energy bounds to infer
continuity of the loss, weak lower semicontinuity of the loss, or a small
observable Galerkin residual. It does not rule out a stronger higher-moment,
Orlicz, scale-of-spaces, or reachable-set topology.

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
polynomial rules in one Banach function algebra with bounded multiplication;
it must use a scale of spaces, a restricted nonlinear domain, an unbounded
generator, or a renormalized product.

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

Before the subtarget is reached, \(1-H_R(\tau)\ge1-y\). The physical-time
change therefore gives

\[
t_R(y)
=
\int_0^{\tau_R(y)}
\frac{d\tau}{2(1-H_R(\tau))}
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

## 12. The causal-DMFT instantaneous-fitting theorem

This is the repository’s strongest model-level result. It is logically
independent of the Taylor-series proof.

### 12.1 Canonical tagged-site equation

For a tagged second-layer neuron, let

- \(a(t)\) be the rescaled readout weight;
- \(z(t)\) be its second-layer preactivation;
- \(\xi(t)\) be the cavity Gaussian field;
- \(M(t,s)\) be the deterministic causal self-response kernel;
- \(r(t)=1-f(t)\) be the residual.

The canonical causal-DMFT representation used in the repository is

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

The stated causal properties are:

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

The proof below is complete from these tagged-DMFT properties. The source
poses the closure question directly at this pure mean-field level; it does
not supply a separate theorem deriving (12.1) as a uniform positive-time
limit of finite-width networks.

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

The exact physical-time composite equation is

\[
\dot z
=2r\bigl(q(a\odot z)+2K(a\odot z)\bigr).
\]

Therefore the instantaneous tagged coefficient multiplying \(a_jz_j\) is

\[
2q_0+4K_{\mathrm{diag}}(0)
=
2\mathbb E[h_0^2]+4\gamma\mathbb E[h_0].
\]

In the convention in which the residual \(r(s)\) is outside the memory
kernel,

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

No global coordinatewise sign of the finite matrix \(K\) is assumed.

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

### 12.5 Every subtarget has hitting time zero

Before \(f\) reaches \(y\), (12.3) and (12.10) imply

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

### Theorem 12.1 — Instantaneous subtarget hitting

\[
\boxed{
T_y=0
\quad\text{for every }y\in(0,1).
}
\tag{12.22}
\]

The Gaussian tail probability \(p_A\) tends to zero with \(A\), but for each
fixed \(A\) it is strictly positive, while the comparison fourth-moment
integral is infinite.

### 12.6 The natural relaxed loss trace

For an ordinary squared-loss trajectory starting below the label,

\[
r(t)
=r(0)
\exp\!\left(-2\int_0^t\kappa(s)\,ds\right),
\]

so \(f\) is nondecreasing and does not overshoot \(1\). Within the natural
relaxed class preserving these two properties, (12.22) forces

\[
f(t)=1
\qquad(t>0).
\]

Since \(f(0)=0\),

\[
\boxed{
\mathcal L_{\mathrm{MF}}(t)
=
\begin{cases}
1,&t=0,\\
0,&t>0.
\end{cases}
}
\tag{12.23}
\]

Equivalently, there is no classical tagged-DMFT output continuous at
initialization. Without choosing the monotone, no-overshoot relaxed
continuation, the conclusion is this nonexistence statement rather than an
independently constructed classical step-valued flow.

### 12.7 Uniform continuous closure is impossible

Let \(\widehat{\mathcal L}\) be any continuous predicted loss and set

\[
E
=
\sup_{t\ge0}
|\widehat{\mathcal L}(t)-\mathcal L_{\mathrm{MF}}(t)|.
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

### Theorem 12.2 — Continuous uniform finite-closure no-go

No family of continuous finite-dimensional autonomous closures can
approximate the natural relaxed loss (12.23) with arbitrarily small
uniform error on \([0,\infty)\).

The numerical dimension, autonomy, and one-source syntax are not used in the
lower bound; continuity alone suffices. Those extra conditions specify the
intended closure class and exclude an impulsive source that simply writes the
step by fiat.

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
higher mixed moments or messages.

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

This proves exact non-closure of the ordinary monomial-moment hierarchy. It
does not prove that no nonlinear finite statistic could approximate the
observable.

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
noncommutative message hierarchy.

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

The low-order calculation makes the change concrete. At \(\gamma=4/3\),
writing

\[
H(\tau)=A\tau+\frac{B}{3!}\tau^3+O(\tau^5),
\]

the repository obtains

\[
\begin{array}{c|cc}
\text{model}&A&H'''(0)=B\\ \hline
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
  the source reports that its fixed-order corrections vanish, so the raw
  fixed-order Taylor no-go transfers in that convention.

The last item is a fixed-order reduction to Theorem 7.1, not a new
all-compilers theorem.

---

## 14. Exact status: full resolutions, reductions, and open statements

### 14.1 Results that fully resolve their own stated conjectures

1. **The precise ordinary Wick--Taylor global-shadowing conjecture (8.5) is
   false.**  
   The proof supplies the missing asymptotic estimate with the opposite sign:
   the coefficients grow factorially and the proposed PDEs are not uniformly
   Cauchy.

2. **Within the canonical tagged-site DMFT and its natural monotone,
   no-overshoot relaxed selection, continuous uniform finite closure is
   impossible.**  
   The real-time comparison proves the step target, and continuity gives the
   sharp elementary error lower bounds.

3. **The natural finite-degree moment/message closure question for the
   audited normalized variants has a negative answer.**  
   Equations (13.7) and (13.13), together with the full differentiated
   projector grammar, show that no finite natural cutoff is invariant.

4. **The stated analytic, positive-semigroup, positive-polynomial, and
   positive one-step compiler classes are impossible.**  
   These are complete corollaries of the zero-radius theorem, with the
   hypotheses stated explicitly in Sections 10.1--10.4.

5. **Ordinary \(L^2\) and a single bounded-multiplication Gaussian Banach
   algebra cannot supply the required closure topology.**  
   The counterexamples in Sections 11.1--11.2 are self-contained.

### 14.2 Results that are reductions or conditional propagation theorems

1. The residual-clock stability theorem proves
   \[
   \text{small profile/kernel defect}
   \Longrightarrow
   \text{small global loss defect}.
   \]
   It does not prove the premise for a proposed hierarchy truncation.

2. The tagged-DMFT comparison is a complete theorem from the causal
   properties in Section 12.1. A separate derivation/identification of that
   tagged equation as the finite-width limit is outside the pure-DMFT
   theorem and is not supplied in these files.

3. The hidden-row-only WN statement reduces its fixed-order coefficients to
   the raw model under the declared large-fan-in convention. It does not
   prove an independent normalized real-axis theorem.

4. A generic Banach/Hilbert Galerkin theorem is correct if one supplies a
   well-posed exact hierarchy, stable projections, a continuous kernel
   observable, and an outgoing residual tending to zero. Those
   model-specific hypotheses are not established for every signed
   nonanalytic full-model compiler.

5. The earlier exact noncommutative continuation theorem is cited as prior
   work. Because its complete quadratic-model proof is absent from the
   available source bundle, this report records its conclusion but does not
   present an invented proof.

### 14.3 Statements not proved

The repository does **not** prove any of the following.

- Every signed, nonanalytic, non-Taylor, certified real-axis finite compiler
  is impossible.
- A diagonal \(M=M(n)\) limit fails.
- Every fixed-\(n\) Taylor germ fails inside its own random convergence
  radius.
- The fully trained finite-width Gaussian network has the same
  coordinatewise rare-particle comparison as the frozen subsystem.
- RMSNorm or global readout WN has a zero-radius feature-time series.
- The quadratic no-go theorems transfer to the later bounded
  residual-\(\tanh\), continuous-depth model.

---

## 15. Why the three headline results are ordered by strength

“Stronger” is used here in the logical sense: a stronger theorem excludes a
larger closure class under no stronger target assumptions.

### 15.1 Strongest model-level result

The causal-DMFT step/no-continuous-closure theorem is strongest because:

1. it is a real-time argument, not an initialization Taylor argument;
2. it does not require coefficientwise positivity of a compiler;
3. once the step target is fixed, it excludes **every continuous**
   finite-dimensional predicted loss, regardless of its internal basis or
   source syntax;
4. its lower bound is quantitative: \(1/2\), or \(1\) with exact
   initialization.

Its price is that its target is the stated pure-DMFT model and natural
relaxed selection.

### 15.2 Strongest compiler theorem independent of a regular mean-field target

The Wick--Taylor PDE failure is strongest in a different sense:

1. it directly refutes a precise iterated finite-width shadowing conjecture;
2. it does not assume existence of a continuous large-width target loss;
3. its non-Cauchy contradiction is internal to the finite closure sequence.

It is narrower in compiler class: a signed or non-Taylor real-axis method is
not covered.

### 15.3 Strongest exact-hierarchy result

The normalized moment/message recurrences show exact non-invariance of the
natural finite hierarchy even after architectural normalization. This is
stronger than a low-order numerical mismatch, but weaker than an
approximation no-go because a non-invariant hierarchy may still admit
accurate finite projections.

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

The later causal-DMFT report then supplied a stronger real-time obstruction
for continuous closures of the natural relaxed pure-DMFT target.

### 16.2 What was not superseded

The following remain valid:

- fixed-order derivative/Wick coefficients are computable;
- the residual-clock identity is exact;
- a known small profile/kernel error gives a global loss error bound;
- the analytic and positive-compiler no-gos remain valid;
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
| Factorial lower bound and zero radius | Raw quadratic/Gaussian, fixed-order mean-field jet | Ordinary analytic Wick series | Yes, at repository level | Previously established fixed-order \(L^1\) Wick limit |
| Physical-time boundary layer | Same | Degree-\(M\) zero-flux source PDE | Yes | Zero radius and positivity |
| Global-shadowing conjecture false | Same, iterated \(n\to\infty\), then \(M\to\infty\) | Prescribed Wick--Taylor closures | Yes | Non-uniform-Cauchy argument |
| Analytic Banach realization no-go | Same | One-space bounded analytic exact hierarchy | Yes | Zero radius |
| Positive semigroup no-go | Same | Positive classical semigroup with continuous Wick readout | Yes | Zero radius and positive remainder |
| Positive polynomial compiler no-go | Same | Nonnegative fixed-order-consistent source polynomials | Yes | Zero radius |
| Euler/positive-stage no-go | Same | Wick-positive consistent polynomial step methods | Yes | Binomial lower bound and zero radius |
| \(L^2\) discontinuity | Cubic readout | Ordinary \(L^2\) closure topology | Yes | Explicit rare-set sequence |
| Gaussian Banach-algebra obstruction | Gaussian coordinates | One bounded-multiplication Banach function algebra | Yes | \(L^m\to L^\infty\) argument |
| Frozen Gaussian cutoff singularity | Frozen first layer | Naive Gaussian cutoff/particle proof | Yes in subsystem | Cooperative Riccati growth |
| Instantaneous subtarget hitting | Canonical causal tagged DMFT | Regular positive-time pure-DMFT output | Yes from stated DMFT properties | Positive self-response and Gaussian tail |
| Step-vs-continuous lower bound | Natural relaxed pure-DMFT loss | Every continuous finite loss predictor | Yes once target is accepted | Continuity |
| RMS natural hierarchy nonclosure | True RMSNorm quadratic model | Finite ordinary moment/message cutoff | Yes | Recurrence (13.7) and projector grammar |
| WN natural hierarchy nonclosure | Direction-only WN quadratic model | Finite ordinary moment/message cutoff | Yes | Recurrence (13.13) and projector grammar |
| Broad signed real-axis no-go | Full raw or normalized model | Every admissible finite compiler | **No** | Quantitative residual/noncompactness lower bound still absent outside the step-target class |

---

## 18. Source concordance

For reproducibility, the source roles are:

1. **`approximate_single_source_conjecture_resolution(1).md`**  
   Sections 1--5 give the exact raw model, scalar branch, positivity, Gaussian
   factorial bound, and zero radius. Section 6 proves physical-time failure.
   Section 7 gives the invariant-manifold counterexample. Sections 8--9
   preserve stability and delimit scope.

2. **`approximate_single_source_stability(1).md`**  
   Sections 1--4 give the residual clock and positive-entry coercivity.
   Sections 5--7 give the finite source PDE, clock-shadowing, and
   input-to-state stability. Section 9 explicitly isolates the tail lemma
   that the later zero-radius result disproves for this compiler.

3. **`adversarial_audit_report(1).md`**  
   Sections 1--3 distinguish oracle existence from closure. Section 4 gives
   the \(L^2\), Banach-algebra, analytic, semigroup, positive compiler,
   Euler/Wick, and frozen-tail results. Sections 5--7 state the surviving
   open signed real-axis problem.

4. **`mean_field_single_source_conjecture_audited_resolution(2).md`**  
   Sections 2--7 give the tagged-DMFT assumptions, initial response, cavity
   event, comparison, and zero hitting times. Sections 8--10 give the natural
   step trace and continuous-closure lower bound.

5. **`normalized_mean_field_taylor_closure_audit(1).md`**  
   Sections 3--5 derive the normalized vector fields and frozen reductions.
   Section 6 proves natural hierarchy proliferation and explains the loss of
   positivity. Section 7 states the exact PDE classification.

6. **`MASTER_NEURAL_PDE_REPORT_2026-07-26(1).md`** and
   **`MASTER_NEURAL_PDE_REPORT_WITH_FIGURES.md`**  
   These are the later supersession-aware summaries. They treat the
   quadratic zero-radius, physical-time failure, causal-DMFT step, and
   normalized natural-hierarchy results as established and expressly forbid
   transferring them to the bounded residual-\(\tanh\) model.

---

## 19. Final answer in one paragraph

The repository’s strongest non-closure theorem is that the unbounded
quadratic/Gaussian tagged mean-field dynamics fit instantaneously in the
natural monotone, no-overshoot relaxed class, producing a step loss that no
continuous finite-dimensional closure can uniformly approximate below
\(1/2\) error, or below \(1\) when initialization is matched. Independently,
the ordinary limiting Wick--Taylor compiler is rigorously disproved by a
factorial positive scalar branch: the formal series has radius zero, its
positive source profiles diverge at every positive feature time, and its
physical-time closures are not uniformly Cauchy. Analytic one-space,
positive-semigroup, positive-polynomial, and positive Euler/Wick
constructions consequently fail, while ordinary \(L^2\) and a single
Gaussian Banach algebra are invalid closure topologies. RMSNorm and
direction-only WN still have no exact finite natural moment/message closure,
but their signed terms prevent automatic transfer of the raw zero-radius
proof. What remains unproved is a blanket impossibility theorem for every
signed, nonanalytic, non-Taylor, certified real-axis finite compiler outside
the continuous step-target class.
