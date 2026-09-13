# H3 v2 rational primitive author audit

Date: 2026-09-13.

Author: scoped agent `/root/h3v2_scope/arithmetic_audit`, supervised by
`/root/h3v2_scope` in the `observable_hierarchy` study.

Status: candidate author audit by source inspection and mathematical argument.
This is not an independent promotion review, an executed numerical validation,
or an acceptance of the full solver or trajectory theorem. The conclusions below
apply to the exact audited source hashes, with the stated qualifications.

The assignment permitted only the two complete numerical sources below, shared
instructions, required skills and applicable skill references, with optional
installed primitive documentation. Actual scientific read coverage was all 223
lines of `H3_v2_fixed.py` and all 230 lines of `H3_v2_arithmetic.py`. Process inputs
were the complete `AGENTS.md`, `RESEARCH_WORKFLOW.md`,
`/etc/codex/skills/solve-math-rigorously/SKILL.md`,
`/etc/codex/skills/investigate-conjectures/SKILL.md`, and its
`references/adversarial-audit.md`. Truncated combined output was repaired by
further reads. No study README, other research routes, trajectories, external
scientific sources, or installed primitive documentation were read. No numerical
code was executed and no Git operation was performed. This file persists the
completed report after the supervisor authorized this one report path; the
implementation was not edited.

Audited SHA-256 hashes, obtained with `sha256sum` in `/home/amir/Codes/PDE`:

| Source | SHA-256 |
| --- | --- |
| `H3_v2_fixed.py` | `75c5b6a4478e5365d008bd7ad134cf1c2b6cd6942c68358e0a2d4137207c1225` |
| `H3_v2_arithmetic.py` | `2181b9e47e1c765e440feff582b34208651ff4687e19ce8a96db7752402a6edb` |

## Completed report

The rational path is locally uniformly consistent under the hypotheses below.
I found no mathematical error in its elementary-function formulas.

Let \(d\ge20\), \(\delta=10^{-d}\), and regard a `Fixed` value as its exact
rational `units/scale`.

- **Basic arithmetic, fixed lines 12–14, 50–125:** `nearest` correctly rounds
  both signs, including ties, with error at most \(\delta/2\). Addition,
  subtraction, negation and absolute value are exact on represented operands;
  multiplication and division each incur at most \(\delta/2\). Division requires
  a nonzero represented denominator. Fixed integer powers terminate by halving
  the exponent; negative powers are eventually defined when the exact base is
  nonzero. These operations are locally uniformly consistent on their continuous
  domains, with denominator margins for division.
- **Square root, 165–169:** integer square root gives
  \(0\le\sqrt{x}-\operatorname{sqrt}_d(x)<\delta\) for every represented
  \(x\ge0\), including zero. Conversion of varying exact inputs preserves uniform
  convergence on bounded nonnegative intervals using
  \(|\sqrt{x}-\sqrt{y}|\le\sqrt{|x-y|}\). An \(O(\delta)\) input-to-output bound
  at zero would be false: exact input \(x=\delta/2\) rounds to zero and has error
  \(\sqrt{\delta/2}\).
- **Pi, 17–30:** both alternating series terminate geometrically. Their combined
  error is at most \(20\,10^{-(d+5)}\). The identity follows directly from
  \(\tan(2\arctan(1/5))=5/12\) and
  \(\tan(4\arctan(1/5)-\arctan(1/239))=1\), with the angle in \((0,\pi/2)\).
- **Logarithm, 33–43 and 171–182:** every positive represented operand reaches
  \(x\in[1,2)\) after finitely many exact doublings/halvings. There
  \(z=(x-1)/(x+1)\in[0,1/3]\). After the last included term is at most
  \(\tau\), the omitted doubled tail is at most \(\tau/4\), since successive
  terms have ratio at most \(1/9\). Consequently the returned logarithm differs
  from the represented operand's exact logarithm by at most
  \[
  \delta/2+\delta/(4\cdot10^5).
  \]
  This includes \(x=1\), where the result is exactly zero, and gives local uniform
  consistency on compact subsets of \((0,\infty)\).
- **Exponential, 184–207:** range reduction terminates with \(0<y\le1/2\).
  Taylor terms decrease geometrically, so stopping occurs and its omitted tail
  is at most the tolerance. Writing \(q=2^s\), exact squaring amplifies this error
  by at most \(q e^{2|x|}\). The implemented guard dominates that factor, leaving
  error at most \(10^{-5}\delta\) before final rounding. Negative inputs are safe
  because both the truncated positive exponential and exact exponential are at
  least one; reciprocation cannot increase their absolute discrepancy. Zero
  returns exactly one.
- **Sine/cosine, 209–223:** the computed rational \(P\) lies in \((3,16/5)\).
  Modulo and the subsequent subtraction give \(r=x-2mP\in(-P,P]\), for positive
  and negative inputs alike. After the first generated Taylor term, subsequent
  absolute terms decrease because \(P^2<12\); the alternating remainder at
  stopping is therefore at most \(10^{-(d+5)}\). Zero terminates immediately and
  returns the correct value. For \(|x|\le M\),
  \[
  |f_d(x)-f(x)|
  \le \delta/2+10^{-(d+5)}
      +2(M/6+1)\,20\,10^{-(d+10)}.
  \]
  This uses periodicity and Lipschitz continuity, so it also covers
  discontinuities of the reduction quotient \(m\).
- **Tanh, arithmetic 87–92:** the exponential argument is nonpositive, and its
  rounded output remains nonnegative. Thus \(1+e\ge1\); division is safe. Both
  sign branches agree continuously at zero, yielding local uniform consistency.

**Cholesky and cubature.** Arithmetic lines 145–168 eventually succeed for
same-precision `Fixed` matrices converging to a fixed matrix whose symmetric part
is positive definite. Induct along the finite Cholesky calculation: each exact
pivot is positive, preceding computed entries converge, so the corresponding
computed pivot becomes positive and its square root converges. Positive
represented pivots also have strictly positive returned square roots. The same
argument proves inverse-lower consistency when diagonal entries have a nonzero
margin.

For fixed finite Gaussian count/dimension, prime enumeration terminates by
Euclid's argument; each radical-inverse loop terminates by integer division. Its
uniform lies strictly between zero and one, hence eventually rounds above zero.
Rounded uniforms never exceed one. For a rounded uniform below one, it is at most
\(1-\delta\); the logarithm error bound above ensures its computed logarithm
remains negative. A uniform equal to one produces exactly zero radius. Thus
Box–Muller becomes defined and converges for all sufficiently large precision.

**Necessary qualifications / counterexamples:**

1. Arithmetic line 13 imports `pde.observable_fixed`, not this frozen
   `H3_v2_fixed.py`. Explicitly bind/stage the audited implementation before
   attributing its guarantees to that import.
2. Arithmetic line 146 does not convert matrix entries. For example,
   `Arithmetic(20, backend="rational").cholesky([[1]])` reaches a Python floating
   value at line 165 and attempts its nonexistent `.sqrt()`. Require
   `ar.array(...)` or otherwise same-precision `Fixed` inputs.
3. Keep matrix/refinement fixed during precision refinement, or impose a uniform
   positive pivot margin. The SPD sequence
   \(A_d=\operatorname{diag}(10^{-(d+1)},1)\) rounds to a zero first pivot at every
   precision \(d\).
4. Do not include comparisons, Boolean conversion, or `__float__` in an
   unrestricted “every primitive is locally uniformly consistent” statement.
   Comparisons are discontinuous at equality; for instance
   `Fixed(0,d) == Fraction(1,10**(d+1))` is true. `__float__` remains a fixed
   floating-point projection.

**Resources.** Every adaptive loop above terminates for each valid represented
operand. With \(R\) retained `Fixed` scalars bounded by \(M\), retained storage is
\[
O\!\left(R[d+\log(1+M)]\right)\text{ bits}.
\]
It is not bounded solely by \(d\): `Fixed(10**K,d)` retains \(\Theta(K+d)\) bits.
Temporary exact `Fraction` storage must also be counted. On fixed bounded operand
sets, and away from zero for logarithm/division, a conservative
elementary-function bound is \(O(d^2\log(d+2))\) bits per temporary rational, with
\(O(d)\) series iterations. Constants depend on the operand bounds; exponential
range reduction/squaring can be very expensive for large magnitudes. Any
whole-solver resource claim therefore needs bounds on retained magnitudes and
array counts, plus the fixed input-description size.
