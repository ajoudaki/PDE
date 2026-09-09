# Adversarial audit of ROUTE_CAUSAL_COMPOSITE.md

Date: 25 August 2026.

## Verdict

\[
\boxed{\text{FAIL for Lemma 3.1, Corollary 3.2, and their application to the actual differentiated OMFP DAG.}}
\]

The elementary schedule bound in Lemma 4.1, the power-series summation in
Theorem 5.1, and the Gaussian estimate in Lemma 6.1 are correct within
their explicit abstract hypotheses.  They do not repair the failed causal
grammar step.

There are two distinct defects.

1. Lemma 3.1 is false for the stated class “a scalar node of the exact
   \(L=2\) DAG.”  A barred response kernel used as the root supplies a
   concrete two-response, zero-step branch.
2. Even after restricting roots to actual state/output occurrences and
   charging the incoming edge of a barred kernel, Corollary 3.2 is not
   proved.  Differentiating moving pointers enlarges the Gaussian source
   list, and resolving an adjoint on a source-marked field raises source
   order without differentiating an explicit schedule factor.  The note
   assumes away precisely the all-source provenance theorem it needs.

Consequently (1.1) is at most a bound for a stripped, schedule-hit-only
formal skeleton.  It is not a bound for the response part of the actual
OMFP propagator or for its first three full \(h\)-derivatives.

## 1. Reconstruction of the exact \(L=2\) response grammar

Besides the state equations (2.1)--(2.5), the exact closed grammar contains
the source tangents

\[
\bar\rho_{si}=\mathbb E[\psi'(u_s)p_s^i],
\qquad
\bar\sigma_{si}=\mathbb E[q_s^i],
\qquad i<s,
\]

where

\[
\begin{aligned}
p_{s+1}^i
&=p_s^i+\varepsilon_s\widehat d_s^i,\\
\widehat r_s^i
&=\sigma_{ss}\psi'(u_s)p_s^i
 +\sum_{j<s}\varepsilon_j
   (K_{js}+\bar\sigma_{sj})\psi'(u_j)p_j^i,
\end{aligned}
\]

and

\[
\begin{aligned}
q_s^i
&=\alpha_s^i\psi'(z_s)
  +a_s\psi''(z_s)\zeta_s^i,\\
\zeta_s^i
&=(Q_{is}+\bar\rho_{si})q_i^i
  +\sum_{i<j<s}\varepsilon_j
    (Q_{js}+\bar\rho_{sj})q_j^i.
\end{aligned}
\]

These equations are indispensable: treating
\(\bar\rho,\bar\sigma,\sigma_{ss}\) as opaque “edge decorations” is not a
full unrolling of the response graph.

### A direct counterexample to Lemma 3.1 as stated

Choose \(i<s\) and use the scalar DAG node \(\bar\sigma_{si}\) as the root.
The branch

\[
\bar\sigma_{si}
\longrightarrow q_s^i
\longrightarrow \zeta_s^i
\longrightarrow \bar\rho_{si}
\]

contains the monomial

\[
\mathbb E\!\left[
 a_s\psi''(z_s)\,
 \bar\rho_{si}\,q_i^i
\right].
\]

It contains two response vertices,
\(\bar\sigma_{si}\) and \(\bar\rho_{si}\), both with terminal time \(s\),
and no displayed \(\varepsilon_j\).  Thus \(k=2\), whereas Lemma 3.1
requires at least \(k-1=1\) chronological factor.

The same branch appears inside the actual state equation as

\[
\varepsilon_i\bar\sigma_{si}x_i.
\]

In that context the incoming \(\varepsilon_i\) repairs the count.  This
shows exactly why a possible charging theorem must be **contextual**:
it must include the incoming edge by which a response kernel is reached.
It cannot be a theorem about an arbitrary scalar node.

This example also disproves line 129 of the proposed proof: a branch can
contain both a reverse historical response \(\bar\sigma_{si}\) and a
forward historical response \(\bar\rho_{si}\) at the same terminal time.
The proof considered only a forward historical response versus the reverse
*current* response and omitted this case.

### What remains plausible but unproved

A repaired value-level statement might hold for branches rooted at an
actual state or output occurrence, if:

- the incoming edge of every barred kernel is retained;
- \(\bar\rho,\bar\sigma,\sigma\), \(p\), and \(q\) are included in one
  simultaneous induction;
- the charge records both source time and terminal time; and
- no factor is charged twice.

No such induction appears in the note.  Therefore even the repaired
value-level claim is open here.

## 2. Moving pointers invalidate Corollary 3.2's proof

For a fixed operator,

\[
\partial_h(J\delta_s)=J(\partial_h\delta_s),
\qquad
\partial_h(Ix_s)=I(\partial_hx_s).
\]

The right sides are new Gaussian source coordinates with new pointers.
They are not merely old kernels with differentiated scalar decorations.
For a field already marked in a source direction \(\zeta\), the exact
aggregate identity is

\[
J^*D_\zeta V
=\mathbb E[D_JD_\zeta V].
\]

Thus applying a reused adjoint raises source order by one without
differentiating any displayed \(\varepsilon_i\).  Repetition raises it
again.  This is the all-source hierarchy; it is not counted by the number
\(q\) of common-step derivatives.

The issue is already visible in a first derivative of the current response:

\[
\partial_h\sigma_{ss}
=\mathbb E\!\left[
 a_s'\psi''(z_s)
 +a_s\psi'''(z_s)z_s'
\right],
\]

while \(z_s'\) contains the differentiated fixed actions
\(I x_s'\) and \(J^*x_s'\).  Resolving \(J^*x_s'\) introduces a response
shift inside the derivative of the kernel \(\sigma_{ss}\).  It is not
obtained by merely deleting one of the already displayed factors in the
undifferentiated branch.

Similarly,

\[
\partial_h\bar\rho_{si}
=\mathbb E\!\left[
 \psi''(u_s)u_s'p_s^i
 +\psi'(u_s)(p_s^i)'
\right],
\]

and \((p_s^i)'\) differentiates its moving raw actions and response
kernels.  The assertion at lines 160--169 that a kernel derivative only
changes an edge decoration is therefore not an established property of the
exact DAG.

A valid derivative theorem would need an induction over

\[
\{\text{time},\ \text{pointer provenance},\
  \text{Malliavin source order},\ h\text{-order}\}
\]

and must show that every new source shift receives a distinct contextual
chronological charge.  Corollary 3.2 supplies no such induction.  Hence the
bound “at most \(q+1\) unweighted shifts” is unproved and cannot be used.

## 3. Lemma 4.1

For \(r\) distinct indices,

\[
\prod_{\ell=1}^r\varepsilon_{i_\ell}
=h^r\prod_{\ell=1}^ra_{i_\ell}.
\]

Therefore, for \(0\le d\le r\),

\[
\left|
\partial_h^d\prod_{\ell=1}^r\varepsilon_{i_\ell}
\right|
=\frac{r!}{(r-d)!}|h|^{r-d}
 \prod_{\ell=1}^r|a_{i_\ell}|.
\]

Using

\[
e_r(|a|)\le\frac{A_N^r}{r!},
\qquad
\tau=|h|A_N,
\]

gives exactly

\[
\sum_{i_1<\cdots<i_r}
\left|\partial_h^d\prod_{\ell=1}^r
\varepsilon_{i_\ell}\right|
\le A_N^d\frac{\tau^{r-d}}{(r-d)!}.
\]

This includes \(h=0\): if \(r>d\), both sides vanish; if \(r=d\), the
elementary symmetric bound applies.

**Verdict on Lemma 4.1:** pass.

Its use requires the factors to have distinct indices.  That is exactly
the point not established for the differentiated all-source grammar.

## 4. Theorem 5.1 and its constants

The radius-shift estimate

\[
\|S^kb\|_{\rho'}
\le\frac{k!\rho}{(\rho-\rho')^{k+1}}\|b\|_\rho
\]

is valid, although not sharp.  For \(n=m+k\), the coefficient ratio is

\[
\rho^{-k}\frac{(m+k)!}{m!}
\left(\frac{\rho'}{\rho}\right)^m,
\]

whose supremum is bounded by the sum

\[
\rho^{-k}\sum_{m\ge0}\frac{(m+k)!}{m!}x^m
=\frac{k!\rho}{(\rho-\rho')^{k+1}},
\qquad x=\rho'/\rho.
\]

Assuming a branch with \(k=r+1\) shifts really has \(r\) distinct charged
factors and assuming its complete positive transition is bounded by
\(C^{r+1}S^{r+1}\), equations (5.2)--(5.3) are arithmetically correct:

\[
\sum_{\ell\ge0}
\frac{(\ell+d+1)!}{\ell!}x^\ell
=\frac{(d+1)!}{(1-x)^{d+2}}.
\]

This yields precisely the coefficient in (1.1).

There are nevertheless three application failures:

1. the required contextual charging theorem has not been proved;
2. \(\partial_h^{[d]}\) differentiates only displayed schedule factors,
   whereas full \(h\)-derivatives also differentiate moving kernels and
   pointers; and
3. no explicit, horizon-independent \(C\) is constructed for the complete
   decorated all-source transition.  Counting local branches alone does
   not bound products or pointer norms.

Accordingly Theorem 5.1 passes only as an abstract generating-function
lemma after its hypotheses are assumed.  It does not prove (1.1) for the
actual \(P_N^{\rm resp}\).  The statement in Section 7 that the causal
source-shift obstruction is resolved is false.

## 5. Lemma 6.1

Assume \(c\ge0\), as its use as a positive majorant requires.  Discrete
variation of constants gives

\[
X_N
\le
\left(X_0+\sum_sw_sB_s\right)
\exp\!\left(c\tau+c\sum_sw_s|G_s|\right).
\]

When \(\tau>0\), convexity gives

\[
\exp\!\left(\lambda\sum_sw_s|G_s|\right)
\le
\sum_s\frac{w_s}{\tau}
\exp(\lambda\tau|G_s|).
\]

For a centered Gaussian of variance at most \(V^2\),

\[
\mathbb E e^{t|G|}
=2e^{t^2\operatorname{Var}(G)/2}
 \Phi(t\sqrt{\operatorname{Var}(G)})
\le2e^{t^2V^2/2}.
\]

Hence

\[
\mathbb E\exp\!\left(\lambda\sum_sw_s|G_s|\right)
\le2e^{\lambda^2\tau^2V^2/2},
\]

without any independence assumption.  Hölder with exponents \(2,2\) and
\(\lambda=2pc\) gives

\[
\|X_N\|_p
\le
2^{1/(2p)}
e^{c\tau+pc^2\tau^2V^2}
\left\|X_0+\sum_sw_sB_s\right\|_{2p}.
\]

Thus every numerical constant in (6.2) is correct.  The only missing
minor hypothesis is \(c\ge0\); if the right side is infinite, the estimate
is still trivially valid.

**Verdict on Lemma 6.1:** pass after stating \(c\ge0\).

The sentence following it is properly conditional: the lemma applies only
after an actual coupled tangent block has been reduced to (6.1).  The note
does not perform that reduction for \(\bar\rho,\bar\sigma\).

## 6. Final claim-level audit

| Claim | Verdict |
|---|---|
| Lemma 3.1 as stated for any scalar DAG node | **Fail; explicit counterexample** |
| Corollary 3.2 for moving-pointer derivatives | **Fail; circular/unproved** |
| Lemma 4.1 | **Pass** |
| Theorem 5.1 as an abstract charged-skeleton sum | **Pass conditionally** |
| Theorem 5.1 for the actual OMFP response propagator | **Fail** |
| Lemma 6.1 and its constants | **Pass**, with \(c\ge0\) |
| “Causal source-shift obstruction is resolved” | **Fail** |
| Uniform scalar \(Ct^4h^5\) theorem | Correctly not claimed |

The productive next statement is a contextual, typed charging conjecture,
not Lemma 3.1: root the branch at an actual output/state occurrence, retain
every incoming response edge, and prove a simultaneous all-source
provenance induction.  Until that induction is supplied, no causal
propagator estimate for the actual OMFP DAG has been established.
