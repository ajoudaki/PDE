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

## Second accepted package: finite calculus and reusable implementation

The moving L2, one-sample, order-three physical-GF recurrence is fully contained
in `FINITE_JET_ADDITION.md`, SHA-256
`bb927e3f7a2dc75a222664a871b7caf247ebccd0fc1f31815434f6f2e3c26fb6`.
Two isolated reviewers read the entire proof, notation, numerical contract,
implementation, tests and complete local import dependencies. Both returned
CLEAN with no required corrections: `reviews/FINITE_JETS_A.md` and
`reviews/FINITE_JETS_B.md`. Their independent rational coordinate-differentiation
checks complement, rather than replace, the recurrence proof. The floating-point
range exclusions remain explicit, including intermediate overflow even when
an exact coefficient exists.

The forest factorization, key, reversion/determinant algorithms and quadratic
zero-first-mobility certificate are contained in `EXACT_CALCULUS_ADDITION.md`,
SHA-256 `1babf900769e75b6951d1579108e4e3159d1fd297589f5d580f7382d5f95b799`.
Both full isolated reviews are CLEAN with no required corrections:
`reviews/EXACT_CALCULUS_A.md` and `reviews/EXACT_CALCULUS_B.md`.
Their proof input also contained the complete Gaussian Section 4; all supplied
code, tests and import dependencies were fully read. Independent Riccati/formal
ODE coefficient derivations and independent inverse/determinant calculations
reproduced every displayed certificate coefficient. These checks do not supply
concentration or a positive-time identification claim, which are not asserted.

The book's Section 7 preserves both proof bodies except for heading levels and
the optional harmless superscript typo `^{,k}` changed to `^{k}` in (7.C3).
The original reviewed fragment is retained unchanged. This is an editorial
correction, not a new probability or arithmetic assertion. The code guide adds
API contracts, examples, limitations and the complete certificate command.

| Accepted implementation/test | SHA-256 |
|---|---|
| `code/pde/finite_jets.py` | `1d8e5bdf4ca056645c720fce69a4df9e82dbbdf840da7f9f4599efe5c401aca2` |
| `code/tests/test_finite_jets.py` | `991ae49dc65f1e0970c02ab57596560fabd79a1e71416879b43c52aa5e75c88a` |
| `code/pde/exact_calculus.py` | `482a45deb3e5fb721acdd0ae97654f9f5db57da145e0902d9ff1b24f01c8fc41` |
| `code/tests/test_exact_calculus.py` | `b4a7f5795def064e53b2e7a849637d29dcaa0bad403e8e8ff893863b8468a439` |

`make check` passes all 73 small deterministic tests and the structural boundary
check. No training experiment, high-order campaign, data or figure was generated.
Initialization, quantitative and exact-capture drafts still await their remaining
independent reviews; the final integrated-edition audit and inventory are pending.
