# Frozen hostile-audit contract: order-five scalar depth recursion

Frozen before inspecting any producer recurrence or producer-generated coefficient
map.  This contract is deliberately stricter than checking a few numerical
activations.

## 1. Target claim

For the stated fully trained, equal-width, one-sample network at every fixed
hidden depth \(H\), with the width limit taken before any depth limit and with
unit forward Grams, there is one depth-independent finite tuple of ordinary
deterministic scalars whose explicitly printed layer maps produce

\[
A_H=F_H'(0),\qquad B_H=F_H^{(3)}(0),\qquad C_H=F_H^{(5)}(0).
\]

Every coefficient of every printed map must belong to

\[
 \mathbb Q[d,\tau_0,\tau_1,\ldots,
 \{M_{\nu_0\ldots\nu_5}\}],
 \qquad
 M_\nu=\mathbb E\!\left[\prod_{r=0}^5
 \phi^{(r)}(G)^{\nu_r}\right],
\]

with \(G\sim N(0,1)\), \(d=M_{020000}\), and
\(\tau_\ell=\sum_{j=0}^{\ell}d^j\).  A state coordinate is an ordinary
scalar polynomial/rational expression, not an encoded function, array with
depth-dependent extent, unevaluated expectation, or hidden compiler object.

The requested witness is a *flattened Wick--Stein contraction*: no Gaussian
innovation, tangent/backward random variable, covariance or response matrix,
implicit derivative, pseudoinverse, random empirical covariance, formal
integral, generating-function coefficient instruction, named-but-unprinted
operator, or 66-entry response-aware proof IR may remain in its public layer
maps.

## 2. Pass/fail gates

The audit returns `PASS` only if every gate below passes.  A failure of this
particular witness does not prove that no M-only scalar recursion exists.

### G1. Literal admissibility and state-size honesty

1. Every initialization, forward transition, top initialization, backward
   transition, and terminal contraction is printed as a finite expression.
2. An independent symbol scan finds only rational constants, the declared
   \(M_\nu\), \(d\), the relevant \(\tau_\ell\), layer/depth integers where
   explicitly allowed, and prior scalar states.
3. Forward and backward scalar dimensions are reported.  They are independent
   of \(H\); no coordinate hides a vector, matrix, polynomial table, symbolic
   expression DAG, history, or variable-length family.
4. “Smallest obtained” is acceptable.  “Minimal” is rejected without a lower
   bound proof.
5. The same transitions are used at every interior layer.  There is no
   H-specific lookup, interpolation in \(H\), or branch specialized to the
   three audited depths.

### G2. Independent exact expansion against frozen maps

After the producer freezes its text and machine-readable representation, the
auditor reconstructs the printed transitions independently and expands with
exact integer/rational arithmetic.  Canonical monomial keys are exponent
vectors of the terminal \(M_\nu\) atoms; zero coefficients are deleted.

The resulting \(C_H\) maps must agree coefficient by coefficient with the
pre-existing frozen unit-Gram maps:

| depth | required nonzero monomials in \(C_H\) | permitted discrepancy count |
|---:|---:|---:|
| 2 | 974 | 0 |
| 3 | 6,519 | 0 |
| 4 | 17,641 | 0 |

The audit records both source hashes, both monomial counts, missing keys,
extra keys, and unequal coefficients.  Merely evaluating selected activations
does not satisfy this gate.  A comparison in which both sides are emitted by
the same transition implementation is invalid.

Because three depths cannot by themselves prove the claimed arbitrary-depth
derivation, the accompanying mathematical derivation must also establish the
layer transition.  If affordable, an unused \(H=5\) comparison against the
response-aware compiler is a discriminator against depth interpolation, but it
is supplementary rather than a substitute for the derivation.

### G3. Lower-order projections

Without changing the state definition, the printed recurrence must project to

\[
A_H=\tau_H=1+d+\cdots+d^H
\]

and exactly to the accepted Section 7.1 scalar recursion for \(B_H\).  The
auditor compares the projected symbolic transitions, not only their H=2,3,4
terminal values.

### G4. Derivative ceiling

The finite-width fifth directional derivative is first checked to use no
activation derivative above \(\phi^{(5)}\).  The Wick--Stein contraction must
not silently increase that ceiling: every terminal atom name must have exactly
six exponent slots and largest derivative index at most five.  A proof must
explain why integration by parts is organized without introducing
\(\phi^{(6)}\) or higher.

### G5. Exact algebraic controls

The exact expanded recurrence must pass:

* readout parity: \(F_H(0)=F_H^{(2)}(0)=F_H^{(4)}(0)=0\);
* constant activation (including the distinction between a unit-Gram constant
  and a merely formal nonunit substitution);
* an affine activation, with any normalization/forward-consistency caveat
  stated explicitly;
* deep linear:
  \((A_3,B_3,C_3)=(4,160,13888)\) and
  \((A_4,B_4,C_4)=(5,400,73240)\);
* canonical unnormalized quadratic controls, including
  \((A_2,B_2,C_2)=(111,1685184,77400633120)\), and the accepted H=3 and H=4
  values from the frozen reference ledger.

Controls are secondary to G2 and cannot repair an atomwise mismatch.

### G6. Smooth nonpolynomial finite-width regression

At least one preregistered smooth nonpolynomial activation must compare the
recurrence's \(A_H,B_H,C_H\) predictions to an exact finite-width jet oracle at
multiple widths and seeds, with the stated extrapolation, uncertainty, and
validity gates.  A pre-existing experiment may be reused only if its contract,
code hash, raw output, and no-post-selection rule are auditable.  The outcome
may be pass/fail/inconclusive, but `PASS` for the whole deliverable requires the
regression gate requested by the user to pass rather than merely run.

### G7. Annealed-limit theorem scope

The report must distinguish:

1. exact finite-width identities (requiring only the derivatives and moments
   actually used);
2. formal population/Wick contractions;
3. exact rational atomwise audits at H=2,3,4;
4. a theorem-level fixed-H annealed limit.

For rung 4 it must state a sufficient activation class and the exact
uniform-integrability bridge permitting
\(\mathbb E[D_n^k f_n]\to\mathbb E[D_\infty^k f_\infty]\), \(k\le5\).
A safe sufficient statement is allowed to be stronger than necessary (for
example smooth derivatives of polynomial growth), but finite moments alone do
not establish UI.  No claim may cover \(H=H(n)\), growing batch, positive
training time, or an all-orders series unless separately proved.

### G8. Stieltjes coefficients

Only after G1--G7, define

\[
\mu_{0,H}=\frac{B_H}{2A_H^2},\qquad
\mu_{1,H}=\frac{4B_H^2-A_HC_H}{24A_H^5}.
\]

These algebraic coefficients do not by themselves imply positivity or a
Stieltjes representation.  Any Padé/Stieltjes terminology must preserve that
distinction.

## 3. Strongest pre-registered obstructions

1. **Moment-state nonclosure.**  Eliminating a response derivative can create a
   new mixed local Wick contraction not determined by the proposed state.
   Failure signature: two partial layer histories agree on every advertised
   scalar but yield different next-layer \(C\) contributions.
2. **Depth-growing type set.**  Fifth-order marked paths can retain their
   relative layer order, forcing a number of deterministic summaries that
   grows with depth.  Failure signature: a transition needs an indexed family
   whose live index range grows with \(\ell\).
3. **Hidden 66-state repackaging.**  Renaming response/covariance entries as
   scalars technically removes matrices but does not perform the requested
   Wick--Stein contraction.  Failure signature: a coordinate's definition
   still contains a Gaussian derivative, covariance, or response semantic.
4. **Finite-depth interpolation.**  A formula can reproduce H=2,3,4 by an
   H-dependent correction while having no valid layer derivation.  Failure
   signature: explicit depth branches, lookup constants, or disagreement at an
   unused depth.
5. **Stein derivative leak.**  Naive integration by parts can introduce
   derivatives above five.  Failure signature: an atom containing slot
   \(r>5\) or an unexpanded derivative operator.
6. **Forward-consistency confusion.**  Formal substitution of moments from an
   activation whose output variance is not one can be mislabeled as a control
   of the unit-Gram network.  Such substitutions are useful algebra checks but
   are not model-level controls unless normalization restores the Grams.

## 4. Decision rule and evidence discipline

* `PASS`: every gate G1--G8 passes and the exact artifacts are hashed.
* `FAIL (witness)`: a literal admissibility, derivation, or exact-map gate
  fails; the M-only scalar-recursion existence claim remains open.
* `INCONCLUSIVE`: required frozen artifacts, independent reconstruction, or a
  numerical validity gate is missing.

The final audit names every surviving branch rather than substituting the
response-aware compiler for the requested witness.
