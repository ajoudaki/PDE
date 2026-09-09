# Incorporation acceptance and exact scope

This is a progressive record after checkpoint `a257e59`, not a blanket audit
of every historical source. The starting library inventory is preserved in
`reviews/INCORPORATION_BASE_LIBRARY_INPUTS.json`. The final integrated edition
and navigation will be checked after the remaining assemblies are reviewed.

## First accepted package: correlated-data partial results

The complete Part IV proof is identical to
`FIRST_LAYER_COMPACTNESS_ADDITION.md`, SHA-256
`02500ea3eee80f9dadd36790a5ccaea6258c06d0c6901564b54417624452ef93`.
The source was the fully read 1,623-line
`ALL_ANGLE_FIRST_LAYER_COMPACTNESS_COMPLETE_PROOF.md` in the recovered
`l2-two-sample-proof-0ywjpp` directory, source SHA-256
`910f4df8fdcaf79313858fd5a8bfe8f58dd5a655b7bb90181ef97233fa5ba8a9`.
The assembly translates its first weights to the shared normalization,
preserving the actual raw GF/GD and mean-versus-sum clock distinction.

The original assembly's two isolated reviews required eight Gram-symbol
repairs and one continuity-codomain repair. They remain preserved without
relabeling in `reviews/FIRST_LAYER_ROUND1_A.md` and
`reviews/FIRST_LAYER_ROUND1_B.md`. Two fresh reviewers, seeing only the
corrected complete proof and notation, returned CLEAN at the exact current
hash: `reviews/FIRST_LAYER_ROUND2_A.md` and
`reviews/FIRST_LAYER_ROUND2_B.md`.

The complete Sections 10–11 proof is identical to
`MIXED_FITTING_ADDITION.md`, SHA-256
`36a50c2aa599302db2b2942d0ddb21d5561488ac0eff5e4b34dd7e43e3717a78`.
Its fully read sources in the same recovered directory are:

| Source | SHA-256 |
|---|---|
| `COMPACT_FIRST_LINEAR_TAIL_TOP_CLOCK.md` | `cb0a9abb96ede054190b54cf883f9bd51081b39c3d7b36689eaa335268301e8b` |
| `COMPACT_LINEAR_TAIL_PERMANENT_FIRST_GATES.md` | `dcaaea01fe2f22b8848da127eed58fbcf29bc8fe9fba516ebcaa0dde70abac20` |

The historical permanent-gate review was also read fully, but not used as a
mathematical premise. The new assembly contains its proofs with the shared
first-weight normalization, explicit sufficient constants, all Gaussian
event estimates and the necessary extra strip event. Two fresh isolated
complete-proof reviewers returned CLEAN with no corrections:
`reviews/MIXED_FITTING_A.md`, `reviews/MIXED_FITTING_B.md`.

Both pairs read the exact proof and the complete notation contract only;
they did not see studies, prior verdicts or other agents. Their individual
reports give full read coverage and exact input hashes. The additions invoke
no unprovided specialized theorem. Ordinary finite-dimensional ODE facts,
elementary Gaussian identities and norm inequalities are used at the stated
hypotheses; the nontrivial compactness and clock arguments are contained.

The first result is strong first-layer compactness for actual arctangent
GF/GD, including kinetic and residual-weighted kernel conclusions along
strong subsequences. It is not a common full-sequence population flow.
The second is finite-GF fitting and finite parameter endpoints on explicit
events, plus gate mass on an augmented event; it is not a population/GD or
persistent-feature-velocity theorem. Introductory chapter and guide summaries
have been updated to keep these scopes distinct. The prior complete theorem
proofs are unchanged.

The remaining initialization, calculus/code, quantitative and exact-capture
drafts are not accepted by this package. `make check` currently passes 73
small deterministic tests, including draft-code tests; that test count is
not an independent proof/code verdict or promotion of those drafts.
