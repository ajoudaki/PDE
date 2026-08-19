# Mean-field peeling

Mean-field peeling is a proposed general calculus for reducing fixed-order,
width-normalized neural-network derivative contractions to explicit Gaussian
normal form by layerwise conditional Wick--Stein elimination. Its local
Gaussian identities are exact, its detailed muP examples are audited under
named mean-field assumptions, and its one-sample quadratic specialization has
an exact decorated-forest compiler with accepted coefficients through
derivative order eleven.  Separate exact Gaussian-program recurrences extend
the canonical specialization through derivative order seventeen. The general
observable-grammar theorem and depth-linear finite-state closure remain open.

| Result | Status |
|---|---|
| Conditional Gaussian laws and Wick--Stein identities | Exact |
| Fixed-network backward and training calculations | Audited under stated assumptions; some higher nonlinear closures remain formal |
| Generic order-three feature correction at separately fixed depth and batch | Explicit audited Gaussian recursion under polynomial smoothness |
| Generic order-five route at two hidden layers and one sample | Fully flattened one-dimensional moment formula; independent symbolic-\(Q^0\) atom audit under polynomial smoothness |
| Generic order-five route at arbitrary fixed depth, one sample, unit Gram | Explicit 29-coordinate-type, six-sweep, one-dimensional-moment recursion; exact H=2,3,4 coefficient audits; strict one-forward/one-backward compression remains open |
| Quadratic decorated-forest reduction | Exact special-case reduction |
| Canonical quadratic derivatives through order seventeen | Accepted exact certificates; connected forest through eleven, polynomial Gaussian-program recurrence through thirteen, two scalar exact recurrences through seventeen |
| Canonical hidden preactivation norms | Two exact contractions through $Q_2^{(16)}$; nine first-hidden and eight second-hidden moment candidates; every accessible squared/literal-RMS Hankel principal minor passes strictly |
| Independent block-metric extension through order nine | Exact special-case continuum certificate |
| \(\beta=1\) block-metric family through order thirteen | Complete exact \(\alpha\)-polynomial jet; downstream strict-interior Hankel counterexamples |
| Three-input equicorrelation extension through order five | Exact special-case jets and two lower moment signs; no Hankel determinant |
| Bounded quadratic order-thirteen Campaign 6 | Protocol-inconclusive; no accepted new bound |
| General Gaussian-normal-form theorem | Open |
| Depth-independent finite-state closure and shared $O(L)$ DAG | Open |
| Full canonical quadratic coefficients through order seventeen | Exact finite-order certificates |

## Maintained sources

[`CURRENT_RESEARCH_STATE.md`](CURRENT_RESEARCH_STATE.md) is the
canonical theory document. It defines the admissible observable language,
conditional Wick--Stein elimination, equality partitions, global width
counting, deterministic covariance replacement, feature-learning jets, the
target theorem, the relation to Tensor Programs, and the open proof program.

[`MUP_TRAINING_CASE_STUDY.md`](MUP_TRAINING_CASE_STUDY.md) is the complete
calculation audit for one three-hidden-layer muP network. It contains the
backward-kernel peel, the one-step loss and hidden-Gram coefficients, the
two-step gradient correction, deep-linear checks, the general readout-scaled
backward template, and the explicit five-branch two-sample expansion.

[`generic_first_stieltjes/`](generic_first_stieltjes/) is the audited
fixed-observable specialization for the first feature-dependent MSE
coefficient with a generic activation.  It starts from two hidden layers and
one sample, then closes the Gaussian recursion for every separately fixed
hidden depth and batch size.  The compact recursion retains \(O(B^2)\) state
per layer, supports arbitrary deterministic PSD input Grams and labels, and
uses no Hermite approximation.  It does not assert growing depth/batch,
positive training time, or the general observable-grammar theorem.
For the two-hidden-layer, one-sample route it additionally contains a fully
flattened calculation through \(F^{(5)}(0)\), with literal moment-only
artifacts, an independent atomwise audit, and the induced one-pole Padé loss
approximation.
For the same order-five one-sample observable at three and four hidden layers,
[`generic_first_stieltjes/depth_order5/`](generic_first_stieltjes/depth_order5/)
contains four explicit terminal moment DAGs and fully distributed coefficient
maps, independently equal coefficient-by-coefficient, including the complete
symbolic input-variance dependence.  Its arbitrary-fixed-depth derivation
retains exactly 66 covariance/response states per reused hidden matrix at
order five.  In the shared-activation unit-Gram quotient, the adjacent
[`generic_first_stieltjes/depth_order5_scalar/`](generic_first_stieltjes/depth_order5_scalar/)
fully contracts that proof IR into 29 deterministic scalar coordinate types
and 38 explicit one-dimensional-moment transition polynomials.  Its six
chronological sweeps reproduce the frozen H=2,3,4 maps with zero exact
coefficient discrepancies at 974, 6,519, and 17,641 fifth-order monomials.
This establishes a fixed-type scalar closure for this observable, but not the
stronger single-forward/single-backward schedule, a growing-depth limit,
generic observable grammar, or positive-time dynamics.  The annealed
identification uses an all-orders polynomially-smooth activation theorem;
finite \(C^5\) regularity alone supplies only the exact finite-width Taylor
algebra unless a separate probability/UI bridge is proved.

The documents distinguish exact finite-width identities, mean-field results
under named probabilistic assumptions, formal nonlinear closures, restricted
audits, and open theorem targets.

[`quadratic_compiler/`](quadratic_compiler/) contains the exact canonical
special-case graph rewrites, connected recurrence, Wick-sector engines,
checked arithmetic, certificates, provenance, and rejected acceleration
attempts. Its completed bounded parameter portfolio covers a relative metric
and hidden observable, two symmetry-reduced inputs, a shifted quadratic first
activation, the full independent two-block metric quadrant, and three
equicorrelated equal-label inputs.  The first four campaigns reached exact
finite Hankel endpoints.  The three-input grammar is accepted through order
five and proves $\mu_0,\mu_1>0$, but its order-seven resource gate failed, so
it supplies no Hankel determinant.  The adjacent Campaign-6 D13 threshold
probe is a stopped protocol-inconclusive diagnostic and supplies no accepted
new bound at its own claim level.  A later finite Gaussian-program recurrence
on the \(\beta=1\) family independently computes the complete canonical
order-thirteen coefficient.  Its bounded canonical scalar successor was then
implemented along two isolated exact routes through orders fifteen and
seventeen.  These remain model-specific fixed-order extensions; they do not
turn the implementation into a generic MLP compiler or establish a
positive-time trajectory.

The exact Stieltjes claim levels, all five campaign outcomes, and the
conditional-stop decision are consolidated in the sole downstream master,
[`../stieltjes_conjecture/CURRENT_RESEARCH_STATE.md`](../stieltjes_conjecture/CURRENT_RESEARCH_STATE.md).

The downstream
[`../stieltjes_conjecture/`](../stieltjes_conjecture/) study consumes the
quadratic feature derivatives but owns the series inversion, moment problem,
Hankel certificates, rational reconstruction, and numerical conjecture tests.
Its [resolution program](../stieltjes_conjecture/resolution_program/) extends
the exact \((0,1)\) reduction to the full \(\beta=1\) order-thirteen jet and
proves a negative shifted determinant for every
\(0<\alpha\leq1/100\).  Its
[canonical high-order successor](../stieltjes_conjecture/resolution_program/canonical_high_order/)
computes $F^{(15)}(0)$ and $F^{(17)}(0)$ exactly and finds both newly
available $4\times4$ Hankel matrices positive definite.  This extends
canonical compatibility to eight moments while leaving the all-order claim
open; no order-nineteen computation was attempted.  Its
[hidden-norm successor](../stieltjes_conjecture/resolution_program/canonical_hidden_high_order/)
also contracts the first- and second-hidden squared-RMS jets through the
available orders.  The resulting nine- and eight-moment prefixes, including
their normalized literal-RMS readouts, pass every accessible Hankel principal
minor exactly.  This remains fixed-order evidence, not an all-order hidden
measure or positive-time theorem.

## Historical source

[`archive/ORIGINAL_NOTES_AND_NTK_SAMPLE.md`](archive/ORIGINAL_NOTES_AND_NTK_SAMPLE.md)
preserves the original proposal and supplied NTK derivation. It is intentionally
not maintained as current mathematics; superseding corrections are stated in
the canonical theory and case study.

## Generated reading edition

[`report/MEAN_FIELD_PEELING_REPORT.pdf`](report/MEAN_FIELD_PEELING_REPORT.pdf) is the
offline reading edition.  The maintained Markdown sources above are
authoritative when they differ from an older generated PDF.  The PDF is generated from the general theory,
detailed training case, and frozen historical source using
[`report/MEAN_FIELD_PEELING_REPORT.tex`](report/MEAN_FIELD_PEELING_REPORT.tex), which owns
only typography, front matter, and inclusion order.

Build it with:

```bash
python3 report/build_report.py
```

The builder protects dollar-delimited mathematics for the workspace's legacy
LaTeX Markdown package, compiles with XeLaTeX in the ignored `build/`
directory, checks the PDF, and copies the final artifact to `report/`.
Generated LaTeX, Markdown, cache, and auxiliary files are not maintained
sources.

## Source-of-truth rule

- Mathematical prose and formulas are edited only in the Markdown sources.
- Presentation is edited only in `report/MEAN_FIELD_PEELING_REPORT.tex`.
- `report/MEAN_FIELD_PEELING_REPORT.pdf` is regenerated; it is not edited directly.
- Historical claims are not silently rewritten in the archive.
- Compiler outputs are accepted only at the claim level recorded by their
  adjacent audit; passing regressions do not upgrade a restricted algorithm
  into the general theorem.

The complete pre-restructure filesystem snapshot, including every earlier
report and build artifact from both document trees, is stored outside this
active directory at
`../../.backups/mean_field_peeling_pre_restructure_20260805T154408Z/` and is
protected by a SHA-256 manifest.
