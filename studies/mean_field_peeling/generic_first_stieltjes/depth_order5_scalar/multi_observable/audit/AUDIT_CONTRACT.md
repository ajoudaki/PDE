# Hostile audit contract: amortized multi-observable MFP DAG

**Frozen before inspection of any proposed `Gamma_04` transition.**

Date: 2026-08-19.  Route: independent hostile reconstruction (H).

## 1. Canonical target and authority

The target is the arbitrary-but-fixed-depth, one-input (`B=1`), equal-hidden-width
Gaussian network already used by the audited unit-Gram order-five feature-ascent
calculation.  The parameter flow is

\[
  \dot\theta=p(\theta):=n\nabla_\theta f(\theta),\qquad
  D=p\cdot\nabla_\theta .
\]

The new observable is the hidden activation Gram and RMS

\[
 Q_\ell(s)=n^{-1}\|x^\ell(s)\|^2,\qquad
 R_\ell(s)=\sqrt{Q_\ell(s)}.
\]

The large-width limit is taken first at fixed `H`, fixed layer `ell`, and fixed
Taylor order.  All displayed unit-Gram transition coefficients must be finite
deterministic expressions in rational numbers, `d`, `tau_ell`, prior scalar
states, and one-dimensional atoms

\[
 M_{\nu_0\ldots\nu_5}
 =\mathbb E\prod_{r=0}^5\phi^{(r)}(G)^{\nu_r},\qquad G\sim N(0,1).
\]

Authorized work includes new derivation, exact symbolic computation, finite-width
automatic differentiation, and independent comparison.  Forbidden substitutions
include Hermite truncation, polynomial replacement of a generic activation,
response-aware Gaussian recursions presented as moment-only formulas, or reuse of
the target trajectory as a hidden coefficient.

The intended claim is a finite-order coefficient compiler, not convergence of the
Taylor series at positive time, uniformity in growing depth, or an autonomous
finite-state model for all observables and all times.

## 2. Claim ladder and promotion gates

The following levels must remain distinct.

1. **Exact finite width:** ordinary differentiation identities for `Q_ell`,
   `R_ell`, and the MSE time change.
2. **Formal normal form:** equality-partition/width-counting and Wick--Stein
   calculations yielding a candidate `M`-only head.
3. **Algebraically audited normal form:** two independently canonicalized routes
   agree coefficient by coefficient, including every transpose-response branch.
4. **Empirical check:** finite-width nonpolynomial tests agree within the frozen
   statistical rule below.
5. **Annealed theorem:** the finite-width expectations converge under explicit
   regularity and uniform-integrability hypotheses.

No formula for `Gamma_04`, its state dimension, one-sweep status, or its complexity
may be promoted past level 2 until every algebraic gate in Sections 4--6 passes.
An empirical pass cannot replace an algebraic or theorem-level gate.

## 3. Independently fixed identities to audit

Let `X_ell^(r)=D^r x^ell|_{s=0}` and

\[
 \Gamma^\ell_{rs}=\lim_{n\to\infty}\mathbb E
 \left[n^{-1}\langle X_\ell^{(r)},X_\ell^{(s)}\rangle\right].
\]

The producer must reproduce, rather than assume,

\[
 Q_\ell^{(k)}(0)=\sum_{r=0}^k {k\choose r}\Gamma^\ell_{r,k-r},
\]

the symmetric dictionary

\[
 \Gamma_{11}=w_\ell,\quad \Gamma_{02}=q02_\ell,\quad
 \Gamma_{22}=q22_\ell,\quad \Gamma_{13}=q13_\ell,
\]

and, writing `gamma04_ell=Gamma^ell_04`,

\[
 Q_\ell''=2(w_\ell+q02_\ell),\qquad
 Q_\ell^{(4)}=2\gamma04_\ell+8q13_\ell+6q22_\ell.
\]

Under unit Gram (`Q_ell(0)=1`) and readout-reflection parity, it must reproduce

\[
 R_\ell''=w_\ell+q02_\ell,
\]

\[
 R_\ell^{(4)}=\gamma04_\ell+4q13_\ell+3q22_\ell
             -3(w_\ell+q02_\ell)^2.
\]

For label-one MSE time, set `c=2 eta`, `A=A_H`, `B=B_H`,
`q2=Q_ell''(0)`, and `q4=Q_ell^(4)(0)`.  The audited composition must give

\[
 Q_t''=c^2q2,
 \quad Q_t'''=-3c^3Aq2,
 \quad Q_t^{(4)}=c^4(q4+7A^2q2),
\]

\[
 Q_t^{(5)}=-5c^5\{(3A^3+B)q2+2Aq4\}.
\]

## 4. Semantic and structural gates

The final semantic guide must verify from the displayed graph that:

- each named sweep contains exactly `H` nearest-neighbour layer transitions;
- sharing a within-sweep template does not identify the six different jet-grade
  maps `F1,R1,F2,R2,F3,R3`;
- `(w,u,j;e11,c10)` is an autonomous order-three projection;
- `A_H`, `B_H`, and `C_H` are read from specified backbone nodes and terminal
  accumulators, with no implicit evaluator;
- every backbone coordinate has a stated derivative/covariance interpretation;
- at `d=1`, `b_ell=1` and `tau_ell=ell+1` in the current indexing, while local
  coefficients may retain `ell`-dependence through `tau_(ell-1)` and stored state;
- universal flow jets `p,Dp,D^2p,D^3p` are separated from an
  observable-specific contraction head.

The `Gamma_04` head counts as one post-`R3` forward sweep only if all its inputs are
already frozen backbone/source nodes and every output at layer `ell` depends solely
on its state at `ell-1`, layer-`ell` fixed moments, and stored universal nodes.  A
backward lookup, response recursion, or unevaluated covariance invalidates that
description.  Report the smallest *found* state, never a minimal state, absent a
lower-bound proof.

## 5. Algebraic audit gates

Promotion requires all of the following.

1. Derive the finite-width fourth feature jet by repeated product/chain rule, and
   verify `Q^(4)=2<X0,X4>/n+8<X1,X3>/n+6<X2,X2>/n` exactly.
2. Enumerate all equality partitions of free neuron indices in every candidate
   `Gamma_04` branch; attach its width exponent and discard a branch only after
   proving its exponent is negative.
3. Include both ordinary and transposed uses of every weight matrix.  Explicitly
   list transpose-response branches and their limiting contractions.
4. Perform Wick--Stein elimination until only declared one-dimensional `M` atoms
   remain.  No Gaussian innovation, response variable, empirical covariance,
   multivariate Gaussian atom, pseudoinverse, or unnamed operator may survive.
5. Freeze the producer expression.  A second implementation, written without
   importing producer transition tables, must canonicalize the same polynomial.
   Compare exact rational coefficients atom by atom for every audited depth and
   layer; discrepancy count must be zero.
6. Scan the recurrence and its expanded tests for activation derivatives beyond
   the asserted ceiling.  A ceiling claim requires both local-transition and
   expansion scans.
7. Verify exact constant, linear, and a nontrivial affine activation.  The affine
   control must retain its constant term and therefore tests response branches
   that a homogeneous linear control misses.

Failure of any gate leaves the head **open**, while preserving any exact identities
that did pass.

## 6. Preregistered smooth nonpolynomial regression

This section is frozen before seeing any `Gamma_04` numerical output.

### Decision question

Does the candidate population `M`-only head predict the independently differentiated
finite-width hidden-activation fourth jet for a genuinely nonpolynomial activation?

### Model and testbed

- activation: `phi(x)=sin(x)/sigma`,
  `sigma^2=(1-exp(-2))/2`, so the forward Gram is one;
- depth: `H=3`; observed hidden layers: `ell=2,3`;
- widths: `n in {64,128,256}` with equal hidden widths;
- independent Gaussian initialization and double precision;
- primary quantities: `gamma04_ell` and `Q_ell^(4)(0)` obtained by exact jet/AD
  differentiation, not finite differences;
- at least 1,024 independent networks per width and one fixed preregistered seed
  recorded in the result artifact.

The mechanism is preserved because nonlinear activation derivatives through order
four, forward and transpose weight responses, multiple hidden layers, and the
moving feature jet all remain present.  Normalization removes only a forward-scale
confounder.

### Exact/numerical validity gates

- enable 64-bit arithmetic;
- for each realization, the relative residual in the exact finite-width identity
  `Q4=2 gamma04+8 Gamma13+6 Gamma22` is at most `1e-9`, using denominator
  `max(1,|Q4|,|rhs|)`;
- no NaN or infinity; fewer than `0.1%` discarded samples, with every exclusion
  logged;
- the standard error of each fitted infinite-width intercept is at most
  `0.10*max(1,|target|)`;
- weighted least squares fits `mean(n)=alpha+beta/n`; the design and residuals must
  not show a statistically resolved monotone curvature large enough to move the
  intercept by more than two fitted standard errors when a `1/n^2` term is added.
  Otherwise the regression is inconclusive and requires larger widths, not a
  reinterpretation.

### Pass/fail/inconclusive rule

For all four primary comparisons (two quantities at two layers), let
`z=|alpha-target|/se(alpha)`.

- **Pass:** every validity gate holds and every `z<=4`.
- **Fail:** every validity gate holds and at least one `z>6` after the replication
  rule below.
- **Inconclusive:** any validity gate fails or some `4<z<=6` after the permitted
  replication.

If an initial comparison has `3<z<=6`, repeat the complete experiment once with an
independent recorded seed and pool only the two preregistered replications.  No
other branch, activation, layer, width search, or threshold change is allowed for
the confirmatory claim.  The hard budget is two replications of the stated grid.

An empirical pass upgrades only the finite-width-regression claim; it does not
prove the Wick algebra or the annealed limit.

## 7. Theorem boundary

An annealed large-width theorem requires either:

1. a cited tensor-program/mean-field limit theorem whose hypotheses are checked
   for every extended jet coordinate, together with polynomially bounded
   derivatives of `phi` through every derivative actually generated and a moment
   bound strong enough to pass expectations; or
2. a direct convergence-in-probability/almost-sure proof plus
   `sup_n E|Z_n|^(1+epsilon)<infinity` for every coefficient observable whose
   expectation is taken.

`phi in C^4` is sufficient for the finite-width fourth-jet identity but is not by
itself an annealed-limit theorem.  State separately the stronger smoothness and
uniform-integrability conditions used by the chosen limit argument.  No result is
uniform in `H` unless proved with constants controlled as `H` grows.

## 8. Integration and cleanup gates

The authoritative research state must explain, self-containedly, the reusable
feature-ascent backbone, output/kernel/loss heads, hidden-activation RMS heads,
preactivation-RMS heads, per-head versus all-layer cost, and the universal versus
observable-specific state split.  Low-level coefficient tables may be linked.

Cleanup must preserve reproducibility: raw/frozen manifests, independent
implementations, exact comparison outputs, and negative/inconclusive evidence may
not be deleted merely to simplify presentation.  Superseded prose must point to
the replacement rather than coexist as a contradictory current conclusion.

## 9. Separately quarantined order-seven roadmap

The order-seven section is exploratory only.  Independently check:

- grade-triangular embedding of the order-five graph;
- candidate `F4/R4` and `F5/R5` passes;
- possible terminal derivative ceiling `phi^(7)`;
- the proposed count of 23 free-tree contraction families in raw `D^7 f`;
- fixed-dimensional `M`-only closure and factored `O(H)` evaluation.

None of closure, dimension, sweep count, derivative ceiling, family count, or
`O(H)` complexity is a result until explicit construction and an independent audit
exist.  A combinatorial family count alone does not establish Wick closure.

## 10. Falsifiers

- Any surviving response/Gaussian state is witness-fatal to the requested
  moment-only head.
- Any nonzero exact atom discrepancy is witness-fatal at the tested depth/layer.
- A missing transpose branch is fatal to the claimed audit, even if controls pass.
- A valid nonpolynomial failure falsifies the tested formula, not the broad
  possibility of another observable head.
- Failure to establish uniform integrability blocks only the annealed expectation
  theorem; it does not invalidate exact finite-width algebra.
- A wrong order-seven family count changes only the roadmap.

