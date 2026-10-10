# Notation migration: scope and inventory

Status: refactor implemented, author-checked and independently post-audited.
The fresh notation reviewer confirmed 29 persistent semantic objects by reading
all 3,958 lines and tracing statement-only dependencies. The paper itself prints
the 29-object inventory below.
The subsequent statement-shortening pass retains this inventory. The source
proposition's pregated response and finite-query radius are local to that
statement/proof, and consumers continue to redeclare their own auxiliary
quantities. No new persistent symbol was introduced.
The user requests independent fresh audits before and after migration, and an
absolute ceiling of 30 paper-specific objects that a reader must remember across
arguments. The pre-migration sources are frozen in PREAUDIT_INPUTS.tar.gz.

## Counting rule

Count meanings, not merely distinct printed letters. Unrelated meanings sharing
a letter are different objects; decorating an auxiliary constant does not evade
the count. A layer-indexed canonical object is one family, but a family name may
not conceal unrelated coefficient tables. A proof-local object must be defined
in that proof, or as a bound variable of its immediately preceding statement.
No later proof may silently use it. Reusing the same convenient letter later
requires a fresh local definition. Summation/integration indices and conventional
mathematical operations (addition, transpose, derivative, probability, expectation,
Euclidean norm, identity, Gaussian distribution) are not newly introduced
paper-specific objects. They will be listed as conventions, not hidden constants.

The decisive test is a statement-only read: after reading a lemma's statement,
the reader must be able to forget its proof's private symbols. Later arguments
must invoke the statement, not reach into its proof's coefficient definitions.

## Persistent inventory for the migration (29)

| Count | Object | Meaning |
|---:|---|---|
| 1 | n | Dense width |
| 2 | m | Training sample count |
| 3 | d | Input dimension |
| 4 | L | Hidden depth |
| 5 | p | Declared passive-input count |
| 6 | x | Input vectors, with sample index when needed |
| 7 | y | Training labels, individually or as a vector |
| 8 | t | Physical training time |
| 9 | W | Layer-indexed weight matrices |
| 10 | w | Readout vector |
| 11 | z | Layer-indexed preactivations |
| 12 | h | Layer-indexed activations |
| 13 | r | Training residual vector and entries |
| 14 | delta with layer/sample indices | Residual-free backward responses |
| 15 | phi | Layer-indexed activation functions |
| 16 | a | Activation strip half-width |
| 17 | beta | Fixed activation envelope |
| 18 | Q | Population feature-Gram matrices |
| 19 | gamma | Smallest eigenvalue of the final population Gram |
| 20 | Y | Label RMS |
| 21 | script L | Mean squared training loss |
| 22 | script X | Promised query domain |
| 23 | trajectory norm with subscript script X | Physical-time/query supremum, including fitted endpoint |
| 24 | delta without layer/sample indices | Failure probability (counted separately from backward responses) |
| 25 | C | An explicitly qualified activation/depth constant |
| 26 | f_n | Dense predictor |
| 27 | tilde f_n | Independent dense predictor |
| 28 | f_model | Compressed predictor, tagged by method when needed |
| 29 | v=x/sqrt(d) | Normalized input, with sample index when needed |

Normalized gap lambda, activity allowance S, log-width ell,
residual RMS rho, time horizon T, approximation tolerance, orders, source spaces,
selected metrics/mixers/deficits, and every coefficient ledger are NOT persistent.
They must be explicit at a statement boundary or locally defined in the relevant
statement/proof. This includes actual algorithm state: it is introduced inside
the construction using it, not silently exported to another construction.

## Required structural migrations

1. Move fitting coefficients into the fitting proof; export physical bounds in
   canonical quantities. Subsequent fitting/comparison proofs redeclare any
   convenient local coefficient they need.
2. Make analytic-source results export bounds in beta, n, m, gamma, Y, d and L.
   Keep the stopped-cavity coefficient ledger private to the source argument.
   Later methods must not import H_j, tau_j, U, V, K_src or other ledger entries.
3. State the selected-runtime transfer with an explicit portable error and state
   bound. Keep metric construction, corrected readout, local deficit and stability
   ledger inside its construction/proof. Harmonic and panel proofs call this
   interface with freshly defined source spaces.
4. Keep Legendre's order, clock and moments inside its construction and associated
   statement/proof block, with local definitions at every proof boundary that
   consumes them. Do not import a coefficient defined inside the fitting proof.
5. Keep innovation moments and conditional-fluctuation constants private to the
   lower-bound proof. The exported lower bound uses only canonical parameters
   and a locally qualified positive confidence-dependent constant.
6. Re-read the result as a statement-only document and as complete proofs. Audit
   all external coefficient imports, repeated overloaded names, implicit norms,
   model tags and qualifiers. Then freeze the migrated sources for fresh reviewers.

## Implemented checks before the fresh post-audit

- Fitting coefficients now live in the fitting proof. The statement exports
  canonical decay, parameter length, output tail and empirical Gram convergence.
- A single shared-source statement exports explicit beta bounds, radii, source
  families and adaptive-panel counts. The full stronger working estimates and
  their coefficient recurrences stay in its structured proof, with local claims.
- The selected-runtime statement exports its source contract, error, sufficient
  tolerance and full retained inventory. Harmonic and panel proofs instantiate
  that statement instead of importing its optimizer's private coefficient ledger.
- Legendre's clock, moment state, local fitting bounds and comparison ledger
  stay within its construction proof. Dense innovation moments and fluctuation
  variables stay within the lower-bound proof.
- The lead read all mathematical before/after diffs and all new public statement
  interfaces. Authors also read their resulting modules completely. An additional
  reference-scope check found balanced proof environments and no cross-file
  references to proof-private labels. The review is semantic as well as lexical:
  shared spellings for differently defined local coefficients do not make them
  persistent objects.
- Three genuinely new isolated reviewers received the full frozen manuscript,
  not this inventory or earlier verdicts. All completed their reviews with
  matching before/after source hashes. No necessary proof or interface repair
  was identified; the independent notation count was 29. See POSTAUDIT_A.md,
  POSTAUDIT_B.md and POSTAUDIT_NOTATION.md for evidence and review limitations.
