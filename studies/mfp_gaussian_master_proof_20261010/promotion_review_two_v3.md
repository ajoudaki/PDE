# Complete scientific promotion review TWO — candidate v3

**Verdict: PASS for the frozen scientific candidate.** I found no required
correction, missing scientific dependency, failed reproduction, or unresolved
correctness objection within the assigned scope. Theory, implementation, and
worked examples each pass this review. This is not the separate integration
review, full-book rendering gate, or user approval to promote.

Reviewer identity: `/root/promotion_review_two_v3`. Review completed on
2026-10-10. The neutral assignment is
`studies/mfp_gaussian_master_proof_20261010/promotion_review_assignment_v3.md`.
The frozen run is
`data/generated/mfp_gaussian_master_proof_20261010/promotion_candidate_v3/`.
All paths below are relative to that run unless explicitly identified otherwise.

## Independence and input integrity

I am distinct from all nine authors/assemblers and the selector listed in
`review_packet/manifest.json`. I received the neutral assignment and process
instructions, with no author discussion or inherited scientific history. I did
not read the study README, selection report, author reports, prior reviews,
other reviewer findings, another study, archived book, or Git history. I did not
communicate with the other reviewer, delegate this audit, perform Git mutations,
modify frozen inputs, or edit maintained files. The only writes were this report
and the assigned `reviewer_two/` scratch directory. No accidental scientific
exposure outside the allowed inputs occurred.

The initial check verified every entry of the 116-file candidate manifest,
15-file changed manifest, and 18-file packet manifest. The final check verified
all entries again, with no mismatch. The following manifest hashes are identical
at the initial and final checks:

| Manifest | Initial and final SHA-256 |
| --- | --- |
| `candidate_manifest.json` | `541b0e75982342c181a99801cdb36269b4a1cc2a40c6e792799a3cce5da6f653` |
| `changed_manifest.json` | `ff6d10776f3add6a276f39be80e23a3517cf2b6d007a20c1eb40fa62299a69d8` |
| `review_packet/manifest.json` | `7c23c3faae35fb0a1ae4fb292d603145e54896260f3eedd3cfd71966d1f13fd9` |

Exact per-file input hashes are retained in
[`verified_frozen_inputs.json`](../../data/generated/mfp_gaussian_master_proof_20261010/promotion_candidate_v3/reviewer_two/verified_frozen_inputs.json),
including all edition files, every packet file, and the manifests/mapping.
The initial and final manifest snapshots are
[`initial_manifest_hashes.json`](../../data/generated/mfp_gaussian_master_proof_20261010/promotion_candidate_v3/reviewer_two/initial_manifest_hashes.json)
and
[`final_manifest_hashes.json`](../../data/generated/mfp_gaussian_master_proof_20261010/promotion_candidate_v3/reviewer_two/final_manifest_hashes.json).
The exact theory hash is
`c0517bd8b00fe9f3ea6856b7b26587980a38c4ae4e9550f40de4833e9efe4c72`.

I independently removed the one exact theory insertion and reversed the three
declared Chapter 2 replacements in memory. The reconstructed chapter has the
recorded original SHA-256
`c79a204fbf7fbb36d9886b94cb5f7f046e5a589be689f9d1d8156ba8f75aa723`.
Every dependency excerpt equals its declared complete source-line range, and
the Chapter 13 dependency's source hash also matches. The candidate mapping
equals the packet mapping. The 50 new native identifiers occur exactly once in
the assembled Chapter 2. This establishes byte correspondence; it does not
constitute a scientific rereview of the original chapter's unread complement.

## Complete read coverage and unread complement

I read the neutral assignment, root `AGENTS.md`, the complete
`RESEARCH_WORKFLOW.md`, the complete canonical-notation skill and its linked
neural-network reference, and the complete `solve-math-rigorously` skill. An
initial combined tool output was truncated in the process-instruction portion;
I repaired that read with a separate complete reading of the skills and the
remaining workflow section before proceeding. Subsequent scientific reads were
bounded, contiguous, and untruncated.

Every line of the following packet files was read, including all proof bodies,
metadata, attribution text, and exact patches:

| Packet file | Read lines |
| --- | --- |
| `promotion_theory.qmd` | 1–1010 |
| `dependency_chapter2_opening.qmd` | 1–251 |
| `dependency_chapter2_finite_jets.qmd` | 1–153 |
| `dependency_chapter2_specialization.qmd` | 1–76 |
| `dependency_finite_gaussian_law.qmd` | 1–369 |
| All four dependency `.origin.json` files | 1–8 each |
| `promotion_assemble.py` | 1–96 |
| `promotion_bibliography.bib` | 1–8 |
| `promotion_book_patches.json` | 1–14 |
| `promotion_code_mapping.json` | 1–13 |
| `promotion_code_readme_patches.json` | 1–10 |
| `promotion_quarto_patches.json` | 1–7 |
| `provenance_non_gaussian_tp_main.txt` | 1–786 |
| `provenance_appendices_H_I_J.txt` | 1–927 |
| `provenance_sources.json` | 1–16 |
| `manifest.json` | 1–56 |

Every `required_edition_reads` file was read in full:

| Edition file | Read lines |
| --- | --- |
| `code/MFP_CALCULUS.md` | 1–416 |
| `code/README.md` | 1–1266 |
| `code/pde/__init__.py` | 1–26 |
| `code/pde/gaussian_moments.py` | 1–114 |
| `code/pde/mfp_compiler.py` | 1–791 |
| `code/pde/mfp_expr.py` | 1–426 |
| `code/pde/mfp_finite.py` | 1–140 |
| `code/scripts/example_mfp_calculus.py` | 1–103 |
| `code/scripts/example_mfp_kernel_jets.py` | 1–112 |
| `code/scripts/example_mfp_mlp_derivative.py` | 1–69 |
| `code/tests/test_mfp_compiler.py` | 1–637 |
| `code/tests/test_mfp_expr.py` | 1–189 |
| `code/tests/test_mfp_kernel_jets.py` | 1–304 |
| `code/tests/test_mfp_mlp_example.py` | 1–65 |
| `docs/_quarto.yml` | 1–68 |
| `docs/index.qmd` | 1–260 |
| `docs/notation.qmd` | 1–98 |
| `docs/references.bib` | 1–74 |

I also read all three run-level manifests and the complete
`candidate_mapping.json`, checked the assembled insertion boundary at Chapter 2
line 252 and its following original section, and inspected the context of all
three book replacements, both README replacements, and the Quarto replacement.
The new theory occupies assembled Chapter 2 lines 252–1261. The scientific
content of the original opening, finite-jet section and contained A.1–A.4 scope
was read through the exact excerpts, with the applicable replacements read
separately. The original source ranges are 1–251, 1035–1187 and 3335–3410.
The bounded-law source range is `docs/12-three-sample-learning.qmd:316–684`.

The unread scientific complement comprises the rest of the 7807-line assembled
Chapter 2, the rest of the bounded-law source chapter, the other theory chapters,
and existing implementation files not enumerated above. `finite_network.py`
was imported by the parent package during the standalone executions; its
numerical implementation is unchanged and was not scientifically rereviewed.
Whole-file hashing and in-memory patch reversal accessed bytes of the book
complement solely to verify integrity. No broader scientific conclusion about
that complement is implied. I did not consult the original external PDF/ZIP
beyond the supplied complete attribution extracts and provenance metadata;
the external master theorem is not a proof dependency here.

## Theory audit

**Theory verdict: PASS.** The theorem has a precise fixed-program scope:
finitely many equal-width vector types; independent named Gaussian matrices
between distinct types; Gaussian iid root tuples with fixed means and possibly
singular covariances; scalar constants, averages, sums and products; and smooth
coordinate expressions whose derivatives have polynomial growth. The allowed
directions, normalized gradients, represented updates and jets are expanded
before invoking the probability theorem. No coordinate selection, inverse,
width-dependent coefficient, unrestricted tensor contraction or increasing
program length enters this assertion.

I checked the following substantive steps rather than treating the bounded-law
reference or the supplied tests as a substitute for a proof.

1. **Named matrix reuse on a typed graph.** The extension of the bounded
   theorem beyond an adjacent-layer chain is justified matrix by matrix.
   Conditioning on the complete past fixes the next query; it conditions only
   the queried independent residual matrix factor. Parallel edges and type
   cycles therefore preserve the product conditional law. Each query still
   involves two distinct population types. The finite-rank Gaussian projection
   error depends on the fixed query-list rank, not graph adjacency. Chronology
   remains acyclic even when the type graph has cycles.

2. **Source identity and singular slots.** For a new forward input $H$, the
   least-squares component in old forward inputs cancels the corresponding
   part of the old reverse-response corrections. Gaussian integration by parts
   leaves exactly the sum of old reverse inputs multiplied by
   $\mathbb E[\partial_{\zeta_s}H]$. Covariances are uncentered input second
   moments. Formal partials retain distinct source names, freeze already
   computed deterministic coefficients, and follow expression paths through
   other matrix calls. The supplied bounded theorem proves singular-query
   removal by independent query perturbations and continuous positive
   semidefinite square roots; it does not take a limit of inverse Grams.

3. **Uniform raw-entry moments.** The simultaneous induction over all fixed
   derivative orders is legitimate because each node depends only on earlier
   nodes. Let $\alpha$ be a raw-entry differentiation list and $p$ an even
   moment order. For $\partial^\alpha(Wv)$, differentiating the explicit linear
   matrix factor contributes at most $|\alpha|$ earlier derivatives; the
   remaining sum is handled by the moment expansion. In a product with $b$
   distinct row entries and $s$ singleton entries, the commuting zero-entry
   differences are exact. Terms missing one singleton difference vanish by
   independence and centering. Repeated fundamental-theorem integration
   inserts precisely one extra copy of each singleton. Cauchy–Schwarz gives
   $C n^{-(p+s)/2}$; the multiplicity inequality $p+s\ge2b$ offsets at
   most $n^b$ index assignments. The case $s=0$ is included. The derivative
   factor is evaluated after shrinking raw entries, so the variance-upper-bound
   induction applies without extra differentiation factors or division by the
   shrinkage parameter. This also covers zero variances and repeated raw
   derivative indices. Scalar feedback is controlled by the same earlier-node
   product estimates and Jensen's inequality.

4. **Uniform clipping and correlated errors.** Each clipped map has a common
   polynomial derivative profile, even though its global Lipschitz constant
   can depend on the clipping radius. Thus the moment estimates are uniform
   in both width and radius. Input errors vanish in every fixed finite
   $L^p$ by interpolation from $L^2$, with higher moments available from
   the moment lemma. Polynomial difference bounds and high-moment tail bounds
   control coordinate, scalar and average steps. For a matrix input error
   correlated with the matrix, the fourth operator moment and fourth input
   moment give the displayed Hölder estimate; no false independence assumption
   is made. All named initialized matrices have the required uniform operator
   moments by the fully supplied net proof.

5. **Identification and expectation limits.** At a fixed clip radius, the
   bounded typed lemma covers scalar broadcasts and causal scalar feedback.
   The unclipped source construction is obtained by a finite induction over
   expectation coefficients. Positive semidefinite square-root coupling and
   common polynomial envelopes justify convergence of input Grams and response
   expectations even at rank loss. The finite-width clipping error, then the
   fixed-radius width limit, then removal of clipping yield convergence in
   probability. A strictly higher moment gives uniform integrability and the
   claimed scalar $L^p$ convergence. The same-array coupling gives empirical
   $\mathcal W_2$ convergence of every fixed same-type tuple.

6. **Actual finite derivatives and physical normalization.** The vector
   adjoint is $b_u=n\,\partial O/\partial u$. Its scalar-feedback adjoint
   therefore includes a normalized average; its matrix adjoint is
   $b_vu^T/n$, with the factor order reversed at a transpose call. These
   formulas match the finite differential. Root mobility $n\kappa$ and
   matrix mobility $\kappa$ give the claimed normalized velocities and
   contractions. The ambient gradient must be formed before substituting a
   represented current state; differentiating the resulting training-history
   graph is a different pullback. The derivative rules, outer-product
   lowering and finite coefficient algebra close exactly. Moving jets include
   $DO[DV[V]]$ in the second derivative; local finite-dimensional existence
   supplies jets without a common width-independent horizon. Frozen seeds
   have the declared enlarged-space partial-derivative semantics and retain
   their statistical source dependence.

7. **Restricted activation moments.** The original centered feedforward
   preactivations have the stated covariance recursion because no reverse
   call precedes that original forward pass. Later fields in the restricted
   subclass are polynomial expressions in joint Gaussian coordinates and
   activation derivatives at those designated original preactivations.
   Gaussian integration by parts removes one explicit polynomial factor at
   each reduction, whether the derivative hits the remaining polynomial or
   an activation. Thus the reduction terminates without invertibility or an
   assumption of analyticity. Nonlinear functions of derivative fields and
   updated preactivations are expressly excluded from this normal form, while
   remaining eligible for the general expectation graph when admitted by the
   primitive language.

The theorem does not silently extend to the width-dependent small-readout law.
Its neural application instead declares readout variance $\tau^2$ fixed in
width. Shared first-matrix columns preserve input geometry and physical input
derivatives. The older finite-second-moment-root, lower-regularity bounded
theorem and contained specializations remain separate; the exact reconstructed
chapter confirms that the proposed explanatory replacements do not delete them.

## Implementation and independent attacks

**Implementation verdict: PASS.** I read the complete expression kernel,
typed builder/compiler, finite interpreter, tests and producer, and checked
their contracts against the theory.

The expression kernel uses exact rational constants, with finite symbolic
floats converted through their decimal string. Its formal derivative never
identifies singular Gaussian coordinates. The Gaussian reducer separates
fixed factors and uses a terminating Stein/Wick reduction only for flat
activation products; nested activations remain integrals. The lower-level
symbolic covariance PSD obligation is documented. The frontend separately
validates numeric root covariance by exact Schur complements, including zero
pivots. The expectation DAG records source identities and covariances, keeps
distinct matrix names, and lowers represented actions before physical AD.

Reverse accumulation, scalar broadcasts, normalized averages, shared matrix
occurrences, finite curve coefficients and simultaneous substitution agree
with the written calculus. In particular, substitution preserves existing
frozen seed expressions; it does not refresh them from the substituted current
state. The finite interpreter uses the actual supplied stored matrix entries
and introduces $1/n$ only at the documented averages/lowered rank terms.
Integer/Fraction computations are exact; float state arithmetic has the stated
finite-precision limitations. There is no numerical Gaussian quadrature hidden
inside compilation.

In addition to the supplied 72 tests, I wrote and ran
[`adversarial_checks.py`](../../data/generated/mfp_gaussian_master_proof_20261010/promotion_candidate_v3/reviewer_two/adversarial_checks.py).
Its independent degree-three polynomial ring and dense array formula do not
call the candidate's derivative rules to form their oracle. The mixed program
uses three types, a cycle $W:a\to b,V:b\to c,T:c\to a$, a separate parallel
matrix $Q:a\to b$, both orientations of $W$, three vector roots, one scalar
parameter, and nonlinear scalar feedback. At widths 1, 2 and 3:

- finite primal values and frozen derivatives of orders 1–3 equal the exact
  coefficients from direct dense polynomial arithmetic;
- the sum of all normalized vector-gradient contractions, ordinary matrix
  Frobenius contractions, and the scalar-gradient contraction equals that
  same independently computed first differential.

Additional source-law attacks check a three-independent-matrix cyclic action
whose squared norm has expectation one by successive conditioning, a parallel
independent matrix cross-pairing with limit zero, Wishart-chain leading moments
1, 2, 5, 14 and 42, a singular duplicate-query cancellation, rank-zero shifted
Gaussian roots, and the scalar-feedback gradient energy of

\[
O_n=\left(\frac1n\sum_i x_i^2\right)^2,
\qquad b_{x,i}=4\left(\frac1n\sum_jx_j^2\right)x_i,
\qquad \lim\mathbb E\frac1n\sum_i b_{x,i}^2=16.
\]

The Wishart oracle uses the noncrossing Gaussian-pairing recurrence

\[
C_0=1,\qquad C_k=\sum_{j=0}^{k-1}C_jC_{k-1-j};
\]

it does not derive the target numbers from the candidate compiler. Seven
additional rejection attacks cover negative variance, a zero covariance pivot
with a nonzero row, asymmetry, infinite covariance, same-type named matrices,
an inadmissible declared preactivation, and a random optimizer step size.
All these attacks passed. The supplied suite adds independent dense moving-ODE
checks and detailed frozen-seed/current-gradient/history-pullback tests; those
were read and executed in full.

## Worked formulas, geometry, clock and producer

**Examples and producer verdict: PASS.** The reuse example has conditional
squared norm

\[
\left(\frac{y^T\phi(y)}n\right)^2
+\left(1-\frac1n\right)\frac{\|\phi(y)\|^2}{n}.
\]

Taking expectations gives exactly the stated $1/n$ correction. In particular
the identity activation has finite expectation $2+1/n$, while compilation
returns 2. The displayed physical matrix gradient includes both the explicit
transpose occurrence and the derivative of the preceding forward occurrence.

For the saved-vector update, exact lowering gives the response shift

\[
c\longmapsto c-\eta q,
\quad q=\mathbb E[\phi'(\gamma)^2],
\quad c=\mathbb E[\phi''(\gamma)],
\]

and hence $q+(c-\eta q)^2$, yielding

\[
15+(3-15\eta)^2=24-90\eta+225\eta^2
\]

for the quartic loss. Duplicate singular queries have two formal partials;
their response sum gives the factor four in the squared response, and
opposite contributions cancel. For $\dot x=-x^3$, the exact coordinate
solution confirms frozen second derivative 30, moving second derivative 120,
and factorial-normalized second coefficient 60 after Gaussian averaging.

For the two-hidden-layer MLP, centered independent order-one readout makes the
transpose response expectation zero. Its first-layer gradient energy is

\[
s_1s_2,\qquad
s_1=\mathbb E[\phi'(\gamma)^2],\quad
s_2=\mathbb E[\phi'(Z)^2],\quad
Z\sim N(0,\mathbb E[\phi(\gamma)^2]).
\]

Writing $q_1=\mathbb E[\phi(\gamma)^2]$ and
$q_2=\mathbb E[\phi(Z)^2]$, the remaining metric blocks give $q_1s_2+q_2$.
Identity activation gives
first-layer energy 1 and full metric energy 3. Cubic activation gives
first-layer energy 164025 and full metric energy 305775.

The kernel example trains the actual shared first-weight columns $U,V$, with

\[
G_{11}=\alpha^2,\quad G_{12}=\alpha\beta,
\quad G_{22}=\beta^2+\gamma^2.
\]

This preserves correlated and singular input geometry; it does not mistake
supplied sample covariance for independent trainable preactivations. The
stored readout law, all four trained blocks, half-mean loss, negative physical
gradient field and $1/r!$ coefficient convention are explicit. The feature
kernel is only the readout block of the tangent kernel.

I checked the independent identity-activation derivation: with
$\lambda_b=\sum_cG_{bc}y_c/m$, the first-feature-velocity pairing has limit
$5\lambda_a\lambda_b$, each acceleration pairing has limit
$4\lambda_a\lambda_b$, and the second kernel derivative has expectation
$18\lambda_a\lambda_b$. Dividing by two and setting $m=2$ gives

\[
J_2=\frac94(G_{11}y_1+G_{12}y_2)
                 (G_{12}y_1+G_{22}y_2).
\]

Terms containing initial predictions vanish by the proved higher moments and
scalar $L^p$ convergence. Terms involving residual derivatives have a
deterministic limiting coefficient multiplying the appropriate odd-readout
pairing; their expectation vanishes. This is a physical-time calculation,
with the half-loss clock retained.

For the quadratic activation, the initial kernel follows independently from
two Gaussian fourth-moment identities. The long second-coefficient polynomial
is a produced formula. I regenerated it; the stated compact polynomial equals
the expanded output, and the generic expectation graph specializes to the same
quadratic result. These two routes share the Gaussian compiler, as the guide
expressly discloses. I do not claim they are independent derivations of all
its coefficients. Acceptance rests on the audited source-rule algorithm and
the proved finite-program theorem, together with independent rational dense
backpropagation and coefficient-convolution checks of all moving blocks at
widths two and three. There is no empirical training or positive-time claim
being inferred from this polynomial.

The standalone producer regenerated symbolic, identity and quadratic variants.
Their expectation counts at orders 0, 1 and 2 were respectively
`(4,14,132)`, `(0,0,0)` and `(0,0,0)`. Every regenerated integral references only
earlier expectation symbols; each final output references defined expectations.
The producer manifest's source hashes match the frozen producer/compiler/kernel,
and all saved output hashes verify. The default scripts and all five Python
blocks in the API guide execute from the standalone edition with its own code.

## Commands and observed results

All algorithmic checks ran with working directory

```text
/home/amir/Codes/PDE/data/generated/mfp_gaussian_master_proof_20261010/promotion_candidate_v3/edition
```

and with this environment prefix, followed by the listed command:

```sh
env PYTHONPATH=code PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1
```

| Actual command after that prefix | Result and retained log |
| --- | --- |
| `python -B -m unittest discover -s code/tests -p 'test_mfp_*.py' -v > ../reviewer_two/unit_tests.log 2>&1` | Exit 0; 72 tests, 20.183 seconds; all pass |
| `python -B code/scripts/example_mfp_calculus.py > ../reviewer_two/example_calculus.log` | Exit 0; all eight examples regenerate |
| `python -B code/scripts/example_mfp_mlp_derivative.py > ../reviewer_two/example_mlp.log` | Exit 0; all three generic observables regenerate |
| `python -B code/scripts/example_mfp_kernel_jets.py --activation identity > ../reviewer_two/example_identity.log` | Exit 0; orders 0–2 match the independent identity formula |
| `python -B code/scripts/example_mfp_kernel_jets.py --activation all --output-dir ../reviewer_two/produced_kernel_jets > ../reviewer_two/producer.log 2>&1` | Exit 0; three complete variants, formulas, JSON and manifest regenerated in a fresh directory |
| `python -B ../reviewer_two/adversarial_checks.py > ../reviewer_two/adversarial_checks.log 2>&1` | Exit 0; every independent rational/source/boundary attack passes |
| `python -B ../reviewer_two/guide_blocks.py > ../reviewer_two/guide_blocks.log 2>&1` | Exit 0; all five Python-fenced guide blocks pass |

The metadata-only correspondence check ran as

```sh
python -B ../reviewer_two/check_integrity.py > ../reviewer_two/integrity.log 2>&1
```

and exited 0. It verifies all frozen input hashes, exact excerpt origins,
Chapter 2 patch correspondence, mapping equality, new identifier uniqueness,
regenerated expectation-graph chronology, and producer source/output hashes.
Its scripts and logs remain in the assigned scratch directory. Python was
3.10.12 on Linux x86_64. The independent attack log retains `sys.path`: the
only candidate-library entry is this standalone edition's `code/`; the live
checkout's maintained code is absent. Bytecode was disabled. No stochastic
training experiment or numerical width-limit extrapolation was run.

## Attribution, limitations and completion

The attribution is supported by the supplied primary-source text. Appendix J
of Golikov–Yang establishes uniform raw-entry derivative moments with a
variance-upper-bound setup and a common smoothness profile. Its singleton
cancellation/moment-counting mechanism is the one adapted here, while this
candidate supplies its own proof using commuting differences. The citation
does not substitute an inaccessible external theorem for the present proof,
and the candidate makes no priority claim requiring a separate literature
exclusion argument.

No unresolved objection remains. I completed every assigned scientific and
implementation read, inspected the full producer, ran the relevant standalone
suite and recipes, added independent adversarial checks, and reverified the
unchanged frozen inputs. The scientific review is therefore complete and
**PASS**. Full HTML/PDF/LaTeX rendering, broader interface/placement integration
review, and the concrete user approval gate remain outside this assigned
scientific review.
