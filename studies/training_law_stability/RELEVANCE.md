# Independent relevance and placement: training-law stability

Selector: `/root/selector`. Date: 2026-09-11.

**Recommendation: accept the R1 scientific scope for assembly as a new Section C.4
of `docs/global_nonlinear.md`, immediately after C.3. Consolidate repeated
arguments during assembly.** This is a relevance and placement decision under
Part 2, step 1 of the workflow. It does not certify the proofs, approve a live
book change, or replace the subsequent scientific and integration reviews.

## Independence and read scope

The neutral assignment and its continuation asked for an independent comparison
with current book coverage, with no desired verdict. I did not author or assemble
the proposed mathematics. The stated authors are `/root`, `/root/transport`,
`/root/population`, and `/root/nonlazy`; the assembler is `/root`. I read no study
README, study history, review report, or another selector's findings. No prior
verdict is evidence for this decision. I wrote only this report and performed no
Git writes or candidate edits.

The final decision uses these inputs:

- `R1_PROOF.md`, all 1,841 lines: the theorem and all four complete proof parts.
  I reread the frozen version, including the completed restart argument, after
  earlier reading of the four individual components.
- `R1_DEPENDENCIES.md`, all mathematical content: shared notation; III.F.1–9;
  A.1–A.2; C.2; finite dynamics sections 1–4. I read the newly encountered
  dependency bodies in the frozen packet. The notation and C.2 bodies had been
  read completely in the canonical sources; a literal comparison verified that
  the packet contains those same excerpts. Truncated tool output from III.F was
  repaired by targeted reads.
- `RESEARCH_WORKFLOW.md`, Part 2 completely.
- `docs/README.md` and `docs/NOTATION.md`, completely.
- `docs/global_nonlinear.md`, introductory section C and C.1–C.3 completely,
  including weighted-loss activity; A.1–A.2 through the frozen dependencies;
  the complete neighboring fragment introduction and index at lines 1799–1834.

The remaining chapters were compared through the complete chapter descriptions
in `docs/README.md`, not through a fresh whole-book proof audit. In particular,
the continuous-depth comparisons are based on that guide's stated architecture
and scope. No maintained code or empirical producer is proposed in this packet,
and I did not inspect unrelated code.

## Distinct value relative to current coverage

| Proposed contribution | Current coverage | Selection assessment |
|---|---|---|
| One strong autonomous flow for every training law on the stated compact observation space, with a common Gaussian action and full first-row field | C.1 fixes the training list and dimension, even though its local time and response constants are independent of cardinality and Gram conditioning | Substantive enlargement. Keeping the complete first row and proving completion in the training law address inputs outside a fixed active list. |
| Quantitative continuity in joint input-label Wasserstein distance, for the state and all forward inputs | C.1 compares states on one fixed-data construction; C.2 supplies weighted reference tails | Useful new estimate. The explicit changing-input factor in the first-row update and the integrated reference tails are the relevant additions. |
| Simultaneous growing-data, width and vanishing actual-GD-step limits, including passive predictions and paired representation displacement | C.1 supplies every vanishing step for a separately fixed dataset; it explicitly does not assert a growing-dataset theorem | Distinct approximation result. The fixed finite reference comparison is central and must remain explicit in the assembled proof. |
| Replacement stability and a bound on the absolute expected signed generalization gap | The guide identifies out-of-sample behavior as a further target and contains no corresponding bound for this local nonlinear law-driven algorithm | Worth retaining as a short consequence of the new algorithm theorem. The exchange argument alone would not justify a separate chapter or a standalone statistical promotion. |
| Positive averaged activation motion in both layers on an open set of laws, transferred to actual networks | C.3 already proves strict activity for fixed finite nondegenerate data, in a broader activation class and with stronger individual-input conclusions | The reference onset calculation overlaps existing theory. Its useful addition is persistence over an open set containing correlated and nonatomic laws, together with the joint finite-network displacement transfer. |

This package addresses the book's stated input-population question while
retaining an ordinary Gaussian middle matrix, its actual adjoint and learned
hidden representations. It does not change to the particle/residual architecture
described in the continuous-depth guide. Its scope therefore fits directly after
the local dense-network theorem. No priority claim over external literature is
needed for inclusion, and none was assessed here.

## Useful scope and assumptions

The useful theorem is local and model-specific: exactly two tanh hidden layers,
two-dimensional inputs on the normalized circle, bounded labels with fixed
`Y>0`, no biases, the stated independent Gaussian variances, mean squared loss,
and stored-weight mobilities `(n,1,n)`. The time is positive and common across
admissible laws, but no useful numerical time lower bound or global continuation
is claimed. These restrictions define a concrete intermediate result rather than
making the result vacuous.

The law class itself is broad within that model. Atom counts, atom weights,
coincident inputs, singular Grams and input-label dependence are unrestricted;
iid observations are independent of initialization. There is no imposed
orthogonality condition on the theorem's full class. Orthogonality is used only
to produce one reference witness whose open neighborhood permits other laws.

The common Gaussian realization, integrated backward tails, existence,
uniqueness, and finite-network identification are presented as proved parts of
the packet, not supplied favorable trajectories or covariance assumptions. The
fixed reference oracle is a proof construction whose coefficients come from
earlier population Euler nodes. That is an appropriate candidate architecture
for selection; its validity remains an obligation of the fresh complete proof
reviews.

The assembled theorem and guide must retain the following limits:

- Restart concerns reached states on the remaining local interval and the
  stated bounded-state class.
- Quantitative sample replacement is for the deterministic infinite-width
  empirical-law learning map. The finite-width result is qualitative joint
  convergence, with no finite-width replacement rate.
- The statistical quantity is
  `sup_t |E_S[R_mu(f_S(t)) - Rhat_S(f_S(t))]|`. It is neither an expected
  absolute gap nor an expectation of a time supremum, and it gives no excess
  risk or useful risk reduction.
- Nonzero activation displacement holds on a specified open family at a fixed
  positive physical time. It does not hold for every law, and it does not show
  that the learned features improve prediction or persist for all later times.

These qualifications do not defeat relevance. They separate a meaningful
stability and approximation theorem from the stronger explanation of successful
generalization that the book still seeks.

## Duplication, maintenance cost and smallest addition

The new proof is substantial: 1,841 frozen proof lines, accompanied by 1,310
dependency lines. Most dependency material already has a canonical home. A new
standalone chapter reproducing those dependencies would add avoidable maintenance
cost. A Section C.4 can use the existing complete A.1–A.2, C.2 and III.F proof units
with precise links, while retaining complete proofs of every new step.

The raw components repeat the state definition, preliminary norm ball,
bounded-multiplier continuity, cutoff comparison, optimized modulus and
displacement-continuity estimate. Assembly should state each common argument
once, give the finite/population interpretations together where appropriate,
and reference it from the later corollaries. In particular, the proof of
displacement convergence in the algorithm part can support the final activity
transfer without a second full derivation. The existing C.3 theorem should stay
in place: this specialized averaged witness does not supersede its broader
activation and individual-input conclusions.

The chapter's shared fragment index already assigns D–J to results in the
special-data chapter. Calling this addition D would create an avoidable
collision with that existing scheme. C.4 is preferable: it extends the local
theory immediately after C.1–C.3, while its own statement declares the distinct
model and growing-data scope.

The smallest suitable maintained change is:

1. A clearly titled local Section C.4 containing the exact model and theorem,
   full-row transport comparison, common-law construction and restart,
   fixed-reference actual-GD comparison, the statistical consequence, and the
   open-family activation-displacement corollary.
2. Focused edits to the global-nonlinear chapter introduction and
   `docs/README.md` to expose this scope. Update the fragment index and its
   blanket fixed-dataset description to distinguish the C.4 exception. The
   guide's broad statement about the
   absence of an input-population/generalization theorem needs qualification
   to acknowledge this restricted local result while preserving the remaining
   global, general-architecture, excess-risk and explanatory gaps.
3. Canonical notation throughout: retain the layer-indexed population action
   and readout convention, distinguish the full first-row field as a typed
   auxiliary state, and remove study filenames, author-process commentary and
   references to the research contract from maintained mathematical prose.
   A separate notation-guide edit is needed only if the assembled addition
   introduces a reusable convention; no unrelated notation rewrite is called
   for.

No new code API, numerical experiment, dataset or maintained reproduction driver
is justified by this proof-only package. The assembly should be reviewable with
its complete dependencies outside the study and receive the workflow's new
scientific and integration reviews before a concrete user approval request.

I recommend no scientific narrowing beyond the frozen theorem's present scope,
and no new research to enlarge it. The consolidation above is an assembly
requirement for proportionate maintenance cost, not a request to remove the
proof obligations that make the result useful.

## Input fingerprints

SHA-256 hashes captured for this decision are below. Whole-file hashes identify
the context files; they do not imply that the unread chapter complement was
audited. The five frozen dependency excerpts were also compared literally with
their advertised current source slices; all five matched.

| File | SHA-256 |
|---|---|
| `R1_PROOF.md` | `b7f2a65252353d0e47af50da9895f7206d4e202dd591ac4342bf6a2696e036c1` |
| `R1_DEPENDENCIES.md` | `606fe87a97b91a8cad31a26d9e545c4b51ebefd582e55a7ba1b2311bfa2f9469` |
| `RESEARCH_WORKFLOW.md` | `4323e5ada1a4875af2c8121c742c50f07d8ff5b569c3aa71e11ef9a14605b442` |
| `docs/README.md` | `4d3cf63cf09e2effb3342f96272a754e8f8f127aada44179b893f6e1a36df453` |
| `docs/NOTATION.md` | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |
| `docs/global_nonlinear.md` | `8c575acb99ed713ef688cafb39fe9d8d8430e80815d2a69ac6686bac2cc19101` |

The recommendation is **accept for assembly in the existing chapter**, with
repetition consolidated and the exact local scientific scope preserved.
