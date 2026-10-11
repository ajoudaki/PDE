# Setup proof shortening candidate

The complete replacement is `SHORT_SETUP.tex`. It is an author candidate,
not an independent review or an integration approval. Only the assigned
candidate and these notes were written; paper, book and Git were untouched.

Frozen inputs and candidate:

- Baseline HEAD: `aa28e4693eecb93e6770db404878e959f5161fdf`.
- Original `paper/compact_initialization.tex` SHA256:
  `f2f801a714205d28930c9887ded1d4028350c5a11379ba6440f6f9747f8366c5`.
- Candidate SHA256:
  `eccbf4cad4e215fbcfc18263850165b0fd7dc6d8934de7c189a5e12ec89edd22`.
- Original: 1,510 lines, 6,868 whitespace-separated words, 62,137 bytes.
- Candidate: 1,218 lines, 5,112 words, 49,765 bytes: 25.6% fewer words,
  19.9% fewer bytes. These are source counts, not a rendered-page claim.

## Structural reductions and correspondence

| Original component | Candidate treatment | Preservation argument |
| --- | --- | --- |
| Signed parameter-error subtraction | Uses the exact signed identity proved in `cp:signed`, then retains the negative square and the sharper cubic inequality | The endpoint bounds, all real constants, coefficient `A_n`, defect hypotheses and conclusion are unchanged. The final estimate of `cp:signed` is not substituted, since doing that would change constants. |
| Three numerical-envelope ledgers | Retained, with shared endpoint-subtraction explanation | Real, complex and activation-substitution constants, restart radius, all inverse tolerances, activation degree and numerical orders remain unchanged. |
| Fourier contour coefficient argument | Reuses the argument already proved in `cp:harmonic-approximation` for the scalar activation polynomial and the periodic trapezoid | Aliasing, ellipse containment, Cauchy derivative error, positive Fejer weights, angular tube containment and product quadrature error remain proved in the candidate. |
| Taylor input reduction | Uses the complete exact span-reduction proof in `cp:panel` | The reduced matrix, unit inputs, preserved Gaussian law/Gram/trajectories, and `Md` map cost are explicit. |
| Taylor capped-panel count | Uses `cp:poly:eq:panel-count` | The exact substitution is `X=beta^L`, `ell_n=ell`, `r_n=r_cap`, `b_n=b_cap`, `B_n=B_cap`. The bound is identical; the numerical disk containment and `h(0)>=r_cap/2` check remain. |
| Taylor source degree | Retained independently | Real interpolation has a different degree from the earlier initialized-jet construction. The full `B_0`, active/inactive tolerance-branch check and `K_s+1<=8 ell` proof remain. |
| Gaussian forward/transpose sampler | Uses the explicit involution exchanging `(V,Y,p)` with `(U,R,q)` | Both innovation equations and both conditional-mean updates remain. Conditional product kernels, adaptive query choice, bounded stopping, singular cases, completion coupling, exact zero tests, operation/draw/memory counts all remain. |
| Explicit/implicit numerical execution | Shares the causal coefficient/factored-anchor routine and coupling induction | The full four-category initialized-matrix request list and both query budgets remain, including final basis images that need not have been queried earlier. |
| Eight finite work/memory ledgers | Four explicit shared sums plus the eight separately labelled method-specific sums | Expanding the shared sums reproduces every original term exactly; see below. No parameter or finite order is hidden in the numerical big-O constants. |
| Final asymptotic substitution and access qualifications | Consolidated | All four setup orders, retained-state/error guarantees, scalar calls, Gaussian calls, complete physical horizon and exact-real limitations remain. |

All 58 original labels are retained, with no added or duplicate labels.
The two subsection anchors `cp:init:sec:explicit-costs` and
`cp:init:sec:implicit-costs` now both point to the shared finite-cost
subsection. Each of the eight equation labels still identifies its own
corresponding work or memory sum. No other label relocation changes an
interface. No original finite coefficient has been removed or renamed;
the four new cost functions and their argument names are local to the
cost subsection. The transpose query's disposable scalar variables are
specified by the stated involution instead of a second algorithm paragraph.

## Exact finite-cost decomposition

Write `Wex`, `Mex`, `Wim`, `Mim` for the four explicitly defined sums in
the candidate. This is only a map for checking that file; the manuscript
defines the sums completely before use.

- Explicit Harmonic work uses `Wex(P_d,m+N_x)`. Its residual terms are
  the original input-array cost, scalar setup, Harmonic time table and
  projection, both initialized image terms, geometry and node sorting.
  The two image terms become exactly `L n^2 (N+r)`.
- Explicit Taylor work uses `Wex(P_k,M+m)`. The residual terms are
  `P_d`, input reduction/projection, scalar setup, node evaluation,
  initialized source/basis images and node sorting/scheduling.
- `Mex` is exactly the intersection of the two explicit memory sums:
  `P_d + LmnDK + LnR + Lq^2 + LD + J + m^2 + L`.
  The displayed residual memory terms reproduce the corresponding
  Harmonic/Taylor buffers, with no added common `d`, `k`, `m` or `1` term.
- Implicit Harmonic work is `Wim(d,N_x,Q_H)` plus the original Harmonic
  projection, time table, geometry and sorting terms.
- Implicit Taylor work is `Wim(k,M,Q_T)` plus `dM^2`, node evaluation,
  sorting and scheduling. The original standalone `J` remains in this
  residual sum; it has not been silently absorbed into another term.
- Implicit Harmonic memory is `Mim(d,Q_H)` plus its original training
  contractions, harmonic coefficients, data, time table and geometry.
- Implicit Taylor memory is `Mim(k,Q_T)` plus `Md+dk`, passive jets,
  contractions, transformed data and source scheduling.

For the shared work routine the substitutions are literal: `e=d,F=N_x`
or `e=k,F=M`. The latter includes all Taylor forward inputs, while the
separate `m` pays its backward inputs. The factor-history term preserves
`J(J-1)K(K+1)` exactly. Explicit routines retain `K`, implicit routines
retain `K+1`; these were not identified asymptotically. The selector
`Lnr^3`, basis-image contraction `(L-1)nr^2`, exact initial Gram cost,
all metric solves and retained/evaluator descriptions remain charged.

## Checks, reading scope and remaining work

The author read the complete original initialization module, the main
manuscript setup/statements and assembly, and the notation contract. New
proof reuse was checked against complete bodies of `cp:signed`,
`cp:selection`, `cp:harmonic-approximation`, `cp:harmonic`, `cp:panel`,
and `cp:poly:source`; the relevant selected construction and endpoint-tail
proof were also read. The shared workflow and both required mathematical
skills, including the neural-network reference, were read. Other studies,
their histories and scientific contents were not inputs.

Executed checks:

- A Node script compared label multisets: original 58, candidate 58,
  missing/additional/duplicate lists all empty.
- The same script checked matching LaTeX environment stacks in both
  files: no mismatches or unclosed environments.
- A search for comma-separated `eqref` labels found and corrected one
  draft reference; the frozen version uses `cref` there.
- `wc -l -w -c` and `sha256sum` produced the counts and hashes above.
- All eight finite ledgers were manually expanded against the original
  equations, including terms independent of width. An attempted symbolic
  cross-check could not run because the default Python lacks SymPy; no
  package was installed and no symbolic-test pass is claimed.

The author has no identified mathematical gap introduced by the rewrite.
The coordinator still needs the assembled build, rendered size/layout
comparison, full cross-module preservation check and independent audit.
This subtask did not write build outputs because its write scope was the
two assigned artifacts only. Public theorem/proposition text and older
manuscript modules were not edited.

A further possible reduction would replace the real, complex and
activation recurrences by a single coarse power-of-beta envelope. That
would require a new quantitative lemma and would enlarge exposed
activation/depth powers in the finite numerical prescription. It was
rejected here to preserve the exact setup orders and constants. The
current reduction instead uses existing mathematical results, symmetry,
shared arithmetic routines and removal of repeated explanations.
