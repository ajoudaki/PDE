# Independent assessment of milestone 1

Assessment date: 2026-09-11. Coordinator: `/root`. Starting checkout:
`93337c968f352f1b94697213810d6f3232bbcd2a`; study closing commit: `c45f54e`.
This records verification and strategic advice requested by the user. It neither
approves nor applies promotion, and opens no research or training campaign.

## Decision against the original task

**Milestone 1 is accomplished for its original A–C contract.** I found no
surviving substantive proof gap after reading the complete proposed theorem,
its complete mathematical dependencies, both existing canonical scientific
reviews and the original/corrected integration reviews, and obtaining two new
complete isolated scientific audits. This is an acceptance of the precise
infinitesimal-response theorem, not of nonlinear law continuation.

The original assignment in the originating “Study trained-data response” task
(`01a090b5-1a52-7072-a829-cd2aad518558`) specified this sequence: trained-data
response; finite nonlinear changes of training law; selected unseen predictions
and sampling effects. Its actual milestone-1 requirements were:

| Original requirement | What the final proof supplies | Decision |
|---|---|---|
| A: a well-defined forced response retaining the full first row, actual Gaussian action/adjoint, appropriate norms, off-support forcing and passive observations | Strong evolution on clock-row L2, middle HS and readout L2; zero initial tangent; a continuous bounded signed-law forcing map with the inverse gate justified; controlled hidden/prediction observations | Met |
| B: differentiate actual finite GF first, then identify its width limit on each fixed physical horizon, including 40, and the whole circle | Exact finite right differentiation, actual finite weighted moments, fixed-program proxies and a separate integrated finite-tangent defect estimate; convergence in probability uniformly on each fixed time/circle domain | Met |
| C: bound the population homogeneous propagator over all physical times, with explicit conditioning dependence and the corresponding forced bound | A singular-Gram-compatible endpoint semigroup, integrable deviation of the actual generator, and a finite uniform propagator constant; forced response at most proportional to horizon times total-variation mass | Met |

The assignment did not require a nonlinear population flow for fixed nonzero
contamination, a width-uniform finite-contamination remainder, endpoint law
continuity, GD derivatives, or a numerically evaluated conditioning constant.
Their absence is not a retreat from the original milestone.

The model remains two equal-width bias-free tanh hidden layers, input
`x in sqrt(2) S1`, stored Gaussian variances `(1,1/n,1/n²)`, stored mobilities
`(n,1,n)`, output `c^T H2/n`, and physical GF for the unhalved square loss.
The reference law is
`nu_* = (delta_(sqrt(2)e1,+1) + delta_(sqrt(2)e2,-1))/2`.
The actual finite random initial readout is retained. A perturbing probability
law is any fixed deterministic Borel law on the circle with labels in `[-Y,Y]`,
`Y>=1`; it enters as `sigma=nu-nu_*`. Constants do not require positive minimum
atom weights, a fixed support count, or Gram invertibility. The probability
statement is for each fixed law, not one failure bound uniform over all laws.

## Why the central proof bridges survive scrutiny

1. **Forcing is justified on the actual finite trajectory.** The row source
   contains `u_a phi'(w.u) Q(u)/phi'(w_a)`. RMS control of Q alone would not
   make it square-integrable. The proof deletes one initialized matrix column,
   retains the complete learned cavity dynamics and its own residuals, and
   compares both action orientations. Gaussian conditioning is performed on
   the event independent of the removed column. Conditional query-process
   estimates then bound actual finite coordinate moments. The exact inequality
   `cosh² j(X,g) <= cosh² g + 2|X|` supplies the weight. This proves the source
   tails before the width limit; it is not an assumed population tail bound.

2. **Propagation handles the endpoint's neutral directions.** In the clock
   norm the actual homogeneous generator is `L=-2SE+C(t)`, with
   `E=S*D`, `D=R*R` injective but not coercive, and `Gamma=S*DS`.
   The identity `ker Gamma=ker S=ker E*` rules out a nilpotent zero mode and
   justifies the pseudoinverse semigroup formula even at singular Gram rank.
   Exponential reference convergence and the supplied endpoint Q fourth
   moment make `L(t)+2S_infty E_infty` integrable in operator norm. This
   controls the actual time-dependent evolution, not only its frozen endpoint.

3. **Finite derivative capture has its own approximation argument.** Fixed
   Gaussian programs identify tangent proxies only after source clips,
   quadrature and mesh are fixed. A separate same-width comparison controls
   the integrated defect against the actual finite linear ODE. Changing
   multipliers are tested on compact L2 families, rather than declared small
   in operator norm. Width precedes mesh removal at a fixed test cutoff;
   cutoff removal follows. The observation proof supplies the extra `|w|Q`
   control and time/input moduli needed for the whole-circle assertion.

These arguments retain trained features and matrix reuse. This is a response
along a substantially trained nonlinear trajectory, not a time Taylor series
at initialization. It says nothing about convergence of such a time series.

## Audit scope, provenance and reproduction

My scientific reading covered all 2,062 section lines and the complete 3,238-line
dependency packet, including the full proofs of the Gaussian-program/action
construction, transformed reference flow, fitted endpoint and required source
moments. I read the complete 300-line ancillary package and both verification
programs. The original book guide and canonical notation were read completely.
For strategic comparison I also read the relevant current C.4 construction and
C.4.5 statement/limitations through their supplied integration excerpts, and
the complete scoped obstructions in `docs/special_data_limits.md` J.1
(lines 23557–23754) and its Gaussian-norm gate subsection (25638–25708).
This was not a fresh whole-book proof audit. No other study's research was read.

The new reviewers started with `fork_turns="none"` and only the neutral
assignment, the complete frozen P1 section/dependencies/ancillary files, the
two check programs, the manifest and required skills. They had no author
discussion, previous verdicts or one another's findings. Both read all inputs
completely, repaired truncated reads, reconstructed the substantive bridges,
ran the prescribed checks and added separate adversarial algebra checks.
I read their complete final reports:

- [Fresh audit A](ASSESSMENT_FRESH_A.md): ACCEPT, no required correction.
- [Fresh audit B](ASSESSMENT_FRESH_B.md): ACCEPT, no required correction.
- [Separate strategic challenge](ASSESSMENT_STRATEGY.md): narrower source-bounded
  strategic analysis, not a third scientific acceptance or promotion review.
  Its extra deductions and proposed next theorem are not additions to P1.

| Item | SHA-256 |
|---|---|
| P1 section | `33c819282d83f7f4704cbd3a90e87b445d17ce161cc922c1ad786b5eb0d9de38` |
| P1 dependencies | `ca696bc4ed14ea337028eb1e6ef9c7f729ed2a0153bc210de8e16dea18f5ee79` |
| P1 ancillary | `649f0ee17af3c0a2f4b995e971929f8e7a62d9d420614baee418af62d6cdd420` |
| Fresh audit A | `7f4868e1ec8a9f6781374b55ebfd54847fd7ccf3e8bcff437a0214d8eb487e8e` |
| Fresh audit B | `7fcdb6ed0f27f22306fcb7126013c55a800782e355013b20799a6eb7179e4da2` |

All frozen manifest input hashes and declared dependency excerpts match the
current files. The two existing P1 scientific reports and original/corrected
integration reports match their recorded hashes and completed process
identities/exits. I read all four reports. The initial adverse integration
report identified undeclared structural inputs and an out-of-scope manifest
entry; the corrected P1I2 package resolves them without changing the scientific
section or either proposed destination. The completed scientific reviews are
valid evidence for these unchanged inputs. R1 manifest hashes were also
checked; this assessment does not claim a fresh reading of the older R1 reports.

I reran, from the repository root:

```text
python studies/trained_data_response/P1_CHECK_IDENTITIES.py --output data/generated/trained_data_response/assessment_root_20260911/identities
python studies/trained_data_response/P1_REFERENCE_CERTIFICATE.py
python studies/trained_data_response/P1I2_BUILD.py --section studies/trained_data_response/P1_SECTION.md --output data/generated/trained_data_response/assessment_root_20260911/edition
python studies/trained_data_response/P1I2_VALIDATE.py --edition data/generated/trained_data_response/assessment_root_20260911/edition --output data/generated/trained_data_response/assessment_root_20260911/validation
```

All completed successfully. Central derivative errors decreased by factors
of approximately four; the loss/metric discrepancy was `7.90e-12` and the
singular-semigroup discrepancy at most `1.53e-14`. The five exact rational
certificate assertions passed. Standalone checks confirmed links, structure,
exact correspondence and preservation of prior content. Environment:
Python 3.10.12, NumPy 1.26.4, SciPy 1.13.0. Algebra checks support the algebra;
the asymptotic conclusions rely on the proofs. No training experiment was run.

Root evidence is in `data/generated/trained_data_response/assessment_root_20260911/`,
including `provenance.json`, `review_processes.json`, `final_verification.json`
and `validation/validation.json`. Reviewer evidence is in the separately assigned
`assessment_fresh_a_20260911/` and `assessment_fresh_b_20260911/` namespaces.

## Strategic judgment and next target

**Keep the second milestone, with greater confidence in its linear foundation
and a sharper nonlinear completion criterion.** The response equation now has
both justified source production and a bounded homogeneous evolution, and it
is identified from actual finite training. Those were substantive unresolved
dependencies. The next missing bridge is the nonlinear law map, not another
formal response coefficient or a better constant for this one reference.

At finite width one has a first-order contamination expansion, but its
remainder can depend on width. Convergence of its derivatives alone does not
construct the changed-law population flow or justify exchanging width and
differentiation. For example, `a_n(epsilon)=epsilon/(1+n epsilon)` has derivative
one at zero for every n and a zero pointwise limiting function. This illustrates
the logical gap, not a counterexample for these networks.

The next target should construct the autonomous, uniquely restartable nonlinear
population GF through **one fixed trained interval `[0,40]`**, on a nonzero
Wasserstein-open neighborhood of `nu_*` whose radius is independent of width
and sample count. It should identify actual finite GF for approximating
empirical laws, retain the whole-circle predictions and hidden fields, and
give continuity between laws in that neighborhood. For contamination paths
`mu_epsilon=(1-epsilon)nu_*+epsilon nu`, it should also justify the P1 response
by a controlled superlinear remainder, for example

\[
 \sup_{t\le40,\,x\in\sqrt2S^1}
 |f_{\mu_\epsilon}(t,x)-f_{\nu_*}(t,x)
       -\epsilon\mathscr D_{\nu-\nu_*}f(t,x)|
 \le\epsilon\omega_{40}(\epsilon),
 \qquad\omega_{40}(\epsilon)\longrightarrow0.
\]

The corresponding finite remainder/limit bridge must be proved, not assumed;
the theorem must specify its law-uniformity and state topology. A quadratic
remainder or an ambient clock-L2 differentiability theorem is not required.
The goal is actual nonlinear prediction and state capture with an adequate
response remainder on reached states. Fixing `[0,40]` avoids claiming a
growing-horizon width limit or a fixed law's global continuation by shrinking
the admissible law radius with time.

A transport-open domain matters: small input movements need not be small in
total variation, and empirical laws of a nonatomic distribution do not
converge to it in total variation. Mixtures that retain the reference atoms
alone would be a useful intermediate construction but would not complete
this trained-interval population/sampling bridge. P1 already proves continuity
of its *linear forcing integrand* in the data; the strategic report explains
the resulting linear transport modulus. That is not nonlinear two-law stability.

This target is technically difficult for specific reasons. General nonlinear
increments create products not controlled by arbitrary L2 norms; even the
tanh substitution map need not be Frechet differentiable from L2 to L2, as
fixed-height increments on shrinking sets show. The initialized action's L2
bound supplies no generic Lp bound. P1's exact clock cancellation uses the
orthogonal base inputs. The established nonzero Lie-bracket obstruction for
correlated inputs prevents simply extending that simultaneous scalar
straightening to general training controls. A proof must control the actual
reached nonlinear deviations and their weighted remainder terms. Failure of
an ambient norm estimate alone would not falsify the neural theorem.

The existing C.4 local nonlinear law construction and its tail-based comparison
provide the appropriate existence/uniqueness template. P1 adds trained-reference
moments, response identification and propagation. C.4.5's positive fixed-accuracy
transfer supplies a trained-time benchmark, but its fixed positive comparison
distance from the reference does not make two approximations to a changed
law Cauchy. This is why the proposed next theorem is not already proved there.
These dependencies give a concrete research route; they do not prove that
the needed nonlinear remainder estimate will close.

Uniform homogeneous propagation is also not uniform forced response. The
present bound is proportional to `T`, and new data may keep forcing parameter
directions that preserve the two fitted training predictions. Thus a universal
endpoint O(epsilon) comparison should not be the next target. A nonzero secular
direction has not been proved by P1; the strategic report's conditional drift
criterion remains strategic analysis, not an accepted new result.

Success at the proposed second milestone would yield actual selected prediction
functions for nonzero correlated/nonatomic law changes at a time of substantial
learning. It would connect the local input-population theorem, the trained
reference and the new response calculus in one object. The following scientific
task would then be to use that law map for sampling effects and prediction
selection across a substantive admissible family. Recentring beyond the special
reference, stronger risk statements and long-time selection would still require
new estimates. Neither stability nor moving hidden features alone proves that
feature learning improves generalization. My confidence has increased in this
specific next bridge, not in an automatic route to the full general-data goal.

## Authorized status

The scientific candidate remains unchanged. This assessment supports promotion
of its exact reviewed scope; it does not constitute the user's approval.
Established-file edits remain pending that approval. Concurrent exporter,
maintenance and independent continuation files were preserved. Only these
assessment reports and a link in the study README are assigned to this task.
