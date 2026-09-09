# Independent audit of `temporary_linear_growth_uniform_counterexample/FINAL_AUDITED_STATUS.md`

## Verdict

The main claim boundary is correct: the literal fifth jet is quartic in the
horizon, the scalar finite-output instability is not an `L=2` theorem, and
the fixed-schedule-integrable width-first `L=2` question remains open.
The following scope repairs should be made before calling the note final.

## 1. Section 2: actual output versus operator admissibility

The displayed exp-phase calculation proves

\[
 \mathbb E|\phi'(U+hB\phi'(U))|^2=\infty.
\]

This decisively proves failure of the square-integrable second OMFP
gradient state.  By itself it does **not** prove that the raw width-first
network output `F_2(h)` is `+infinity`; a signed reused-matrix cancellation
or a non-Gaussian scaling would have to be excluded.  Therefore the sentence

> “The literal assertion ... is therefore false”

should read either

> “The assertion is not well posed on the linear-growth-only class”

or explicitly define a non-finite operator state as failure of the claimed
finite bound.  It should not be described as an actual-output theorem.

There is now a stronger exact finite-width fact: for every fixed width
`N`, `E(f_(2,N))_+=infinity`; see
`EXACT_FINITE_WIDTH_OUTPUT_FAILURE.md`.  Thus the second expected output is
not a finite real number at any width, although its negative part was not
proved finite.  For sufficiently small `c`, the width-one preceding output
also satisfies `E|f_1|<infinity`, locating the earliest failure there.
Consequently the usual width-first limit of finite expected outputs cannot
be formed for this activation.  This refutes the literal linear-growth-only
statement, but does not close Section 4's **finite-output** width-first
question.

## 2. Section 3: missing quantifier on `rho`

The scalar estimates were proved for fixed

\[
 0<\rho\le1/2.
\]

The constants depend on `rho` and the activation.  The phrase “for
`h=rho/t`” should include this range.  Apart from that omission, both growth
scales are correct:

\[
 \log F_{2t}^{sc}(\rho/t)\gtrsim4^t-O(t^2),
 \qquad
 \log(1+|F_t^{sc}(2\rho/t)|)\lesssim t3^t.
\]

The negative part was genuinely bounded by `O(t)`, so there is no
`|E X|<=E|X|` reversal.  “Counterexample” should retain the adjective
“scalar” every time it is used.

## 3. Section 1: domain of the universal wording

The sentence “Thus no activation can have ...” is broader than the proved
quantifier.  The exact statement is:

> Every activation for which the width-first fifth jet and the temporal
> intertwining identity exist has a degree-at-most-four paired fifth
> coefficient; the displayed numerical envelope additionally assumes the
> stated weighted `C^12` class.

This matters for nonsmooth activations such as the triangular-phase scalar
witness, for which the classical fifth jet was not established in the
note.

## 4. Section 4: notation is exact but potentially misleading

The identity

\[
 z_i^+=G_i^++ha_i\phi'(z_i)Q_n
\]

is correct, but `G_i^+` is not Gaussian or fresh at finite width.  The text
says this immediately afterward, so there is no mathematical error.  A
symbol such as `R_i^+` would reduce the risk of reading a Gaussian
independence assumption into the formula.

## 5. Affine boundary

The affine constants and radius agree with the audited theorem:

\[
 C=10^9 22^{10},\qquad
 (64\,22^2t)^{-1}=(30976t)^{-1}.
\]

Readout reflection still gives oddness when the affine activation has a
nonzero constant term: if `S` flips only the readout, then
`grad f(S theta)=-S grad f(theta)`, whence
`E_h(S theta)=S E_{-h}(theta)`.  No correction is needed there.
