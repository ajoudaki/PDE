# Generic first feature/Stieltjes correction

This directory is the staged extension program requested for a generic smooth
activation.  It begins with one sample and two hidden layers and does not use
a Hermite or polynomial approximation of the activation.

## Current result

For the frozen \(L=2,B=1\) model, the coefficient

\[
C=\lim_{n\to\infty}\mathbb E[D_n^3f_n]
\]

has been reduced to an executable Gaussian normal form containing exactly 17
one-dimensional Gaussian atoms and activation derivatives only through order
three.  Two independently grouped analytic derivations canonicalize to the
same expression.  Exact constant, linear, affine, and quadratic controls pass;
smooth sine and tanh quadrature values agree with an independent finite-width
Taylor-jet oracle.

The base coefficient is fully audited under the polynomially-smooth activation
envelope: `PEELING_AND_PROBABILITY_LEDGER.md` encodes the exact finite-width
observable as one Tensor Program, Tensor Programs III supplies the complete
joint Gaussian/Onsager limit, and Non-Gaussian Tensor Programs Theorem 3.7
gives almost-sure and \(L^p\) convergence for every finite \(p\).  Thus
covariance replacement, uniform integrability, and convergence of
initialization expectations are discharged.  If only derivatives through
\(\phi'''\) are polynomially controlled, the almost-sure result remains valid
under pseudo-Lipschitz assumptions but the annealed result needs the explicit
tail condition recorded in that ledger.

An important outcome is that the generic coefficient need not be positive.
For \(q_0=1\) and \(\phi(x)=\sin x\), the normal form gives

\[
A=1,\qquad C=-1.88699982730593\ldots.
\]

Thus \(C/(2A^2)\) is generically a first nonlinear feature coefficient, not
automatically a Stieltjes moment.

The same two-hidden-layer, one-sample model is now closed through route order
five.  The [`order5/`](order5/) calculation gives fully flattened formulas

\[
A=F'(0),\qquad B=F^{(3)}(0),\qquad C=F^{(5)}(0)
\]

with no Hermite approximation and no auxiliary Gaussian variables in the
terminal result.  In the unit-Gram quotient, the formula contains 3, 46, and
974 rational moment monomials respectively and uses activation derivatives
only through \(\phi^{(5)}\).  A canonical factored arithmetic DAG is embedded
in one self-contained report.  Two separately implemented eliminators agree
coefficient-for-coefficient, both in the unit quotient and in the complete
symbolic-\(Q^0\) layer-separated formula.  The exact linear and unnormalised
quadratic controls are

\[
(A,B,C)=(3,48,1464),
\qquad
(111,1\,685\,184,77\,400\,633\,120),
\]

and a preregistered normalized-sine finite-width regression passes.  The
calculation also supplies \(\mu_0,\mu_1\), the local kernel series, and the
one-pole Padé-induced loss curve.  As already seen at order three, a generic
smooth activation need not yield positive Stieltjes moments: normalized sine
has both \(\mu_0<0\) and \(\mu_1<0\).

The [`depth_order5/`](depth_order5/) route extends this same one-sample,
order-five calculation to three and four hidden layers.  At each depth it
emits both a layer-tagged arbitrary-forward-variance terminal formula and a
unit-Gram formula containing only deterministic arithmetic and declared
one-dimensional Gaussian activation moments.  The exact distributed term
counts for \((A,B,C)\) are

\[
\begin{array}{c|cc}
H&\text{layer tagged}&\text{unit Gram}\\ \hline
3&(4,342,27\,421)&(4,160,6\,519)\\
4&(5,1\,929,462\,776)&(5,350,17\,641).
\end{array}
\]

Two independently frozen compilers agree on every coefficient in all four
maps.  A separate exact interpolation-and-holdout audit, using the proved
explicit-\(Q^0\) degree bounds \((1,3,5)\), also certifies the complete
symbolic input-variance dependence.  The general layer-tagged proof IR uses,
per reused hidden matrix, 21 forward covariances, 15 reverse covariances, 15
forward responses, and 15 transpose responses: 66 entries and one outer
forward/reverse sweep.

In the shared-activation unit-Gram quotient, that IR has now been completely
Wick--Stein contracted into a literal \(M_\nu\)-only scalar recurrence at every
separately fixed \(H\).  It uses six chronological sweeps with dimensions

\[
7/8/4/4/3/3,
\]

or 29 deterministic coordinate types.  All 38 local transition polynomials
are displayed explicitly, and exact expansion gives 974, 6,519, and 17,641
terms in \(C_H\) at \(H=2,3,4\), with zero coefficient discrepancies.  A
post-freeze comparison of two separately written assemblers also agrees
atom-by-atom on every terminal sector.  This is a full flattened algebraic
closure, but it is not the stronger one-forward/one-backward architecture:
the moving feature jets depend chronologically on earlier reverse sweeps, and
two-sweep compression remains open.  The tagged fifth-derivative map still
grows from 1,045 terms at \(H=2\) to 462,776 at \(H=4\), so no depth-uniform
flat-polynomial-size claim is made.

The direct annealed theorem tier assumes a (C^\infty) activation whose every
derivative has polynomial growth, so that the fixed program falls under
Golikov--Yang, *Non-Gaussian Tensor Programs*, Theorem 3.7.  With only the
finite (C^5) envelope the Taylor identities remain exact, but expectation
convergence needs a separate probability limit and uniform-integrability
bound.  Exact constant, affine, deep-linear, and unnormalised quadratic
controls pass, and a preregistered 7,700-network normalized-sine regression
passes at both depths.  Normalized sine again has both
\(\mu_0<0\) and \(\mu_1<0\), so its rational correction is Padé rather than a
positive Stieltjes approximant.

The two-hidden-layer result now also closes for every separately fixed batch
size \(B\), arbitrary deterministic labels, and every deterministic PSD input
Gram, including singular Grams.  The terminal normal form contains only
\(B\)-dimensional expectations

\[
 \mathbb E_{G\sim N(0,Q)}\prod_j\phi^{(r_j)}(G_{i_j}),
 \qquad 0\le r_j\le3,
\]

and has a direct \(O(B^4)\) atom/DAG representation.  If \(\Theta\) is the
usual two-hidden-layer limiting NTK and \(C_c\) is the audited quartic
directional normal form, the coefficientwise limiting initialization Taylor
jet is

\[
\begin{aligned}
 J(t)={}&\frac{y^Ty}{B}
 -\frac{4\eta}{B^2}y^T\Theta y\,t
 +\frac{8\eta^2}{B^3}y^T\Theta^2y\,t^2\\
 &-\left[
   \frac{32\eta^3}{3B^4}y^T\Theta^3y
   +\frac{8\eta^3}{3}C_{y/B}
  \right]t^3\pmod{t^4}.
\end{aligned}
\]

The second term in the bracket is the first feature-learning correction to
the frozen-NTK loss.  The two extra finite-width response contractions needed
to obtain this formula were encoded explicitly and proved to vanish in the
limit by whole-program centered-readout parity; they were not discarded by
formal symmetry alone.  This is a local coefficient theorem, not a claim that
the width limit and a positive training-time interval can be interchanged.

The depth axis now closes as well.  For every separately fixed hidden depth
\(H\), fixed batch size \(B\), arbitrary deterministic channel \(c\), and
deterministic \(Q^0\succeq0\), the coefficient \(C_{H,c}\) is computed by an
explicit response-aware Gaussian recursion.  Each forward layer uses one
\(4B\)-dimensional Gaussian block, and the retained state is
\(O(B^2)\) per layer, hence \(O(HB^2)\) when all layers are stored.  The
compact form evaluates \(\phi\) through \(\phi'''\); inverse-free
Wick--Stein elimination produces literal \(B\)-dimensional activation atoms
using derivatives through at most \(\phi^{(5)}\).  An independent hostile
audit accepts the transpose chronology, parity closures, probability bridge,
and arbitrary-label loss map.

## Artifact map

- `PROOF_CONTRACT.md`: frozen model, limit order, normal-form grammar, and
  acceptance gates.
- `L2_B1_GAUSSIAN_NORMAL_FORM.md`: compact 17-atom formula and primary
  tangent/Hessian derivation.
- `INDEPENDENT_ANALYTIC_DERIVATION.md`: separately grouped derivation and
  affine control.
- `AUDIT_REPORT.md`: hostile normalization, loss-jet, response-term, sign, and
  exact-control audit.
- `PEELING_AND_PROBABILITY_LEDGER.md`: exact Tensor Program, complete response
  and negative-width ledger, and the almost-sure/\(L^p\) theorem bridge.
- `PROBABILISTIC_BRIDGE_AUDIT.md`: independent hostile audit of theorem
  applicability and the weaker finite-order regularity tier.
- `EVIDENCE_LEDGER.md`: claim levels and unresolved dependencies.
- `compiler/`: typed GNF DAG, exact polynomial Wick evaluator, deterministic
  Gaussian quadrature, and independent finite-width order-three oracle.
- `b2/`: the explicit two-input and arbitrary-fixed-batch Gaussian normal
  form, independent derivation, exact finite-width programs, hostile response
  audit, and arbitrary-label local MSE theorem.
- `depth/`: the exact order-three finite-width compiler and the audited
  Gaussian recursions for arbitrary separately fixed hidden depth and batch,
  including independent raw-coordinate, exact polynomial, and hostile
  response/probability audits.
- `order5/H2_B1_ORDER5_SELF_CONTAINED.md`: the complete two-hidden-layer,
  one-sample order-five result, including the literal unit and arbitrary-
  variance moment DAGs, six-family finite-width identity, peeling ledger,
  independent atom audit, controls, theorem hypotheses, Padé kernel, and
  induced loss equation.
- `depth_order5/primary/H3_H4_ORDER5_SELF_CONTAINED.md`: the self-contained
  three- and four-hidden-layer, one-sample order-five result.  It embeds all
  four frozen terminal CSE formulas byte-for-byte and records the
  arbitrary-fixed-depth 66-state recursion, exact symbolic-\(Q^0\) audit,
  controls, probability boundary, and finite-width nonpolynomial regression.
- `depth_order5/independent/` and `depth_order5/audit/`: the separately frozen
  compiler, literal coefficient comparisons, equality/transpose census,
  theorem audit, exact controls, and preregistered numerical gates for the
  depth-order-five result.
- `depth_order5_scalar/ARBITRARY_DEPTH_B1_ORDER5_SCALAR_RECURRENCE.md`: the
  self-contained, fully contracted arbitrary-fixed-depth unit-Gram recurrence
  through order five.  It embeds every one-dimensional-\(M_\nu\) transition,
  records the 7/8/4/4/3/3 sweep chronology, exact map and control audits,
  probability boundary, and the still-open two-sweep compression obligation.

The maintained project-wide MFP theory remains
`../CURRENT_RESEARCH_STATE.md`; this directory is a new fixed-observable
specialization and does not supersede it.

## Reproduce the current checks

From the repository root, run

```bash
python -m studies.mean_field_peeling.generic_first_stieltjes.compiler.run_checks
python -m studies.mean_field_peeling.generic_first_stieltjes.b2.run_checks
python -m studies.mean_field_peeling.generic_first_stieltjes.b2.raw_coordinate_jet_audit
python -m studies.mean_field_peeling.generic_first_stieltjes.depth.run_checks
python -m studies.mean_field_peeling.generic_first_stieltjes.depth.run_fixed_batch_gates
python -m studies.mean_field_peeling.generic_first_stieltjes.order5.run_checks
python -m studies.mean_field_peeling.generic_first_stieltjes.depth_order5.primary.run_lightweight_checks
python -m studies.mean_field_peeling.generic_first_stieltjes.depth_order5_scalar.run_checks
```

For the independent accepted quadratic pairing gate, run

```bash
cd studies/mean_field_peeling/quadratic_compiler
python independent_checks.py --max-order 3 --direct-wick-through 3
```

The required outputs at derivative orders one and three are `111` and
`1685184`, respectively.

## Extension order

The frozen order is

\[
(L=2,B=1)\to(L=2,B=2)\to(L=2,B\text{ fixed})
\to(L\text{ fixed},B\text{ fixed}).
\]

All four stages are complete for this one fixed order-three observable.  The
fixed-batch and joint fixed-depth/fixed-batch formulas, response registries,
probability bridges, and physical arbitrary-label local loss coefficient are
explicit and independently audited.  This does not prove the general MFP
observable-grammar theorem, a regime with \(H=H(n)\) or \(B=B(n)\), a
polynomial bound for flattened atoms or Gaussian quadrature, or convergence at
fixed positive training time.  For arbitrary labels the primary object
remains the first non-NTK loss coefficient; a scalar Stieltjes coordinate is
not presumed.

At order five, explicit frozen terminal maps are complete for \(B=1\) and
\(H=2,3,4\).  The 66-entry response-aware transition applies at arbitrary
separately fixed depth and general forward Grams.  In the shared unit-Gram
case, the new 29-coordinate-type scalar recurrence gives the arbitrary-\(H\)
coefficient using three alternating forward/reverse pairs; its layer maps are
proved locally and its \(H=2,3,4\) expansions are exactly audited.  Maps beyond
\(H=4\) have not received an additional independent terminal-map freeze, and
compressing the six sweeps to one forward and one backward pass remains open.
No order-five fixed-batch extension, simultaneous growing-depth theorem,
depth-uniform flattened-size bound, or positive-time reconstruction is
claimed.  The finite-difference deep-linear closed form recorded in the depth
report also remains conjectural until its symbolic depth-degree bound is
proved.
