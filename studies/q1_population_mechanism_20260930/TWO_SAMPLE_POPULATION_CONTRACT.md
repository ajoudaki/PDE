# Two-sample population continuation: contract and route record

2026-09-30. The user explicitly continues the learning investigation with two
samples and now requires the infinite-width q=1 population object itself.
Finite-width examples and the original dense trained model are not substitutes.
The earlier finite-width endpoint theorem is context, not a proof dependency
of the present population claims. No further compression objective is active.

## Target

Two normalized inputs u_a=x_a/sqrt(d), labels y_a in {-1,1}, equal sample
weights, two tanh hidden populations, zero readout and value initialization,
the residual-speed q=1 key memory, and the canonical fixed Gaussian source
with its true adjoint. Seek the hidden-population evolution, fitting or its
failure, and the entire selected query function through a fitted endpoint.
The main nondegenerate geometry is -1<c<1, where
c=(y_1u_1)^T(y_2u_2). No orthogonality, frozen feature map, independent fresh
backward mixer, or finite-neuron construction may be silently substituted.

The population form of the initialized mixer is denoted T. The state has a
first-population read-in field A and keys K_1,K_2, and a second-population
readout W and values V_1,V_2. Expectations contract fields only in their own
population. T and T* are fixed actions on the common generated source spaces;
the rank-two learned action is reconstructed from V and K. It is not an
independently evolving fully connected layer. Joint laws, rather than separate
one-dimensional marginal densities, are required unless a further closure is
proved. These joint laws may be singular, so existence of Lebesgue densities
is not presupposed.

The current manuscript explicitly labels its fixed-order population limit a
conjecture. Thus three claims must remain distinct:

1. Canonical initialized Gaussian population calculations (finite source calls).
2. Intrinsic identities/theorems for a regular, unique, equivariant population
   q=1 flow on those source spaces.
3. Construction, uniqueness and all-time fitting of that flow, or identification
   as the limit of the finite q=1 systems.

Naming population fields does not establish claim 3. Conversely, studying an
intrinsically specified population system need not compare its trajectory with
dense training. The research seeks additional bridges rather than concealing
these distinctions.

## Scope and reading

The paper, its included appendices, docs/index.qmd and docs/notation.qmd were
read completely earlier in this same continuation and their SHA256 hashes
remain unchanged. AGENTS.md and Part 1 of RESEARCH_WORKFLOW.md were reread.
The current study README was read. Newly relevant maintained material is the
Gaussian reuse/conditioning definitions and generated population-space
construction, and the precise scope of input-exchange symmetry. Selected
complete sections read by root:

- docs/02-gaussian-reuse.qmd, lines 1--170: both initial conditioning sections.
- docs/03-local-population.qmd, lines 174--305: population-space construction
  and the additional response estimate required by its dense-flow theorem.
- docs/10-correlated-pairs.qmd, lines 310--435: exchange symmetry and dense
  label-mode gradient geometry. Its dense-gradient monotonicity is explicitly
  not transferred to q=1.

No other study or old_docs source is permitted. No new numerical experiment,
external literature audit, manuscript edit, commit or push is initiated.

## Bounded initial proof round

Three scoped routes run alongside root's normalization, source audit and
population channel analysis. They must freeze before findings are integrated.

| Route | Scientific inputs | Owned output | Question |
|---|---|---|---|
| pair_symmetry_route | Self-contained model prompt only | TWO_SAMPLE_SYMMETRY_ROUTE.md | Entire query-function geometry and exact sample symmetry |
| pair_fitting_route | Self-contained model prompt only | TWO_SAMPLE_FITTING_ROUTE.md | Sustained interaction, energy, and sufficient fitting mechanism |
| population_mixing_route | Prompt and explicitly assigned manuscript/book sections | TWO_SAMPLE_MIXING_ROUTE.md | First canonical Gaussian return and information required by population laws |
| root | Current manuscript, permitted study and selected maintained sources | TWO_SAMPLE_POPULATION_ANALYSIS.md plus README updates | Reconcile routes, derive common/contrast memory effects, audit claims |

The symmetry worker reported accidental exposure to completed agents' summaries
through a metadata tool. Its result will be treated as a scoped derivation,
not a blind independent attempt. No output from those earlier agents is a
scientific premise. A later fresh check must see only the complete candidate.

Initial round stop: each route returns a complete concrete lemma/reduction or
the exact failed implication. Root then chooses at most one strengthened
follow-up bottleneck and obtains an adversarial check of any accepted new
theorem. No assertion of successful fitting or novelty priority is authorized
merely by the user's request for a strong result.

## Completed theoretical round

All three scoped routes froze and were read completely by root. The one
targeted follow-up was the fitting route's initialized contrast-lag sign;
its addendum proves that the proposed nonnegative lag condition fails locally.
Root then integrated the routes and derived the full second-layer contrast
contraction using four jointly conditioned reverse sources. This additional
proof retains both the moving read-in and the learned memories.

Frozen route hashes:

- TWO_SAMPLE_MIXING_ROUTE.md:
  `10b415ed1249ee9f8f89b4dc58aa05c23810dcf1cd8ef2b7e7bc3a273619f622`.
- TWO_SAMPLE_SYMMETRY_ROUTE.md:
  `9e78832f5788f25574924216d8ff4b116feca66f328eaad38f81ac555f9b8393`.
- TWO_SAMPLE_FITTING_ROUTE.md, including targeted addendum:
  `4b0e8200d0431fefda5774b0749caf4c6e47249bbeee47913aa17f73efbb52f1`.

The fresh startup check covers the first two routes and their initialized
Gaussian dependencies. The separate assembled-candidate check covers the
complete new theorem, exact q=1 attribution, lag, symmetry and conditional
endpoint statements. Its one required correction explicitly bounds first
derivatives in the general Gaussian source class; every actual tanh source
already satisfies that condition. Optional continuation/covariance precision
edits were also adopted. Original findings and the correction verification
are retained in the complete reports. README.md is the current check-status
record, including final hashes.

No numerical experiment, manuscript edit, trained finite-width substitution,
or Git write occurred. This round proves conditional local learning and exact
query restrictions, and exposes the actual lag obstruction. It leaves global
population construction, fitting, and the complete fitted function open. A
further research round would need a new compensation argument, not repetition
of the disproved termwise-sign route.
