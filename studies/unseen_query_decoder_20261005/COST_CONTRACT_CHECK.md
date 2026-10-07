# Bounded internal check of the cost contract

2026-10-06. Scope: the three frozen cost-interface candidates, their
arithmetic substitutions, computational interfaces, and stated claim
boundaries. This is not an independent review of the complete stochastic
decoder, a promotion review, or an implementation benchmark. Only the
assigned candidates, three authorized supporting notes, the expressly
authorized finite-panel result, and required instructions were read.
Links to other scientific inputs were not followed.

**Conclusion after the correction check:** no incorrect resource exponent, missing quadratic
collocation workspace, or normalization arithmetic error was found in
this bounded check. The stated distinction between exact-real panel
costs and the new conditional bit costs is maintained. The four small
specifications identified below were corrected by the author, and the
changed passages were rechecked. No unresolved finding remains within
this bounded accounting scope. The resource exponents did not change.

## Frozen inputs

All three initial candidate digests matched the assignment and remained
unchanged through the initial scientific check. They were then revised
by the author in response to the findings below.

| Candidate | SHA-256 |
|---|---|
| `COST_CONTRACT.md` | `d9f8b88cd8e960298c8d46974bd64d5b3e4d148531593ff9beca7b13d7bc5377` |
| `COST_INTERFACE_PANEL.md` | `7c888eb653a0ea3688dc9fc060c50c2d97c5875495b6d524f1b6a8f7b191bb3b` |
| `COST_INTERFACE_EVALUATORS.md` | `fff11a365914856e8348921cdb5f1b077458988642491ded20be4bd3c4eb3cdb` |

The complete supporting inputs read for this check were:

| Supporting input | SHA-256 |
|---|---|
| `PARAMETER_EXPLICIT_RESOURCES.md` | `45edabb3f3684e22a52545763fed299b43b6c8c9c37f83ba03fcdd9ad07f548e` |
| `PHYSICAL_PARAMETER_ACCOUNTING.md` | `395301fcca55af8937281f22b56c3ffe366d8e46fe7b4b12aeec35e5ca462279` |
| `COMPILER_PARAMETER_ACCOUNTING.md` | `00c017e1b39e96de79ca062b207514cef5cb045507f7cef4ed4975b69fa07c6e` |
| Authorized `../finite_panel_absolute_compression_20261005/RESULT.md` | `38ca06a2e812d8e2b45c6b7350c0437d710433b11a00b89aa66487a9229b028b` |

Corrected candidate digests, verified against the author's supplied
values when rereading the changed passages:

| Corrected candidate | SHA-256 |
|---|---|
| `COST_CONTRACT.md` | `1fcc293c4a726cad64b120c6cf2bc0e5d612789431d01a886c5d77d2c39d32f6` |
| `COST_INTERFACE_PANEL.md` | `36eeedf00b30800e8dc8bf45dc60ac653570127dcc4e685eec59d5cec69a6ba8` |
| `COST_INTERFACE_EVALUATORS.md` | `51f5260e5c06ca556c63095391443426c1785b6446a15d7971e60dbe98fdd284` |

## Initial findings and their resolution

The following comments and line references concern the initial frozen
candidates. They are preserved as the check record, rather than remaining
requests for changes.

1. **Fix the numerical accuracy exponent.** Evaluator-interface line 50
   says to fix the original exponent \(a_0\), and the next sentence
   permits a numerical factor depending on its choice. The headline
   contract does not choose it. For the intended fixed accuracy task,
   state one universal choice, for example \(a_0=10\), and apply it
   throughout this reporting interface. Then the factor comparing its
   \(Z\) with compiler (34) is numerical, as claimed. If instead
   \(a_0\) were user-variable, its dependence would have to remain
   explicit. No displayed exponent needs changing for the fixed choice.
   **Resolved:** the corrected contract and evaluator interface both fix
   \(a_0=10\) universally. The logarithm comparison can now use an
   absolute numerical factor without a free accuracy parameter.

2. **Name exact comparison as part of the panel machine model.**
   Panel-interface lines 126 onward say that activation, first-derivative,
   and square-root calls are the only non-arithmetic primitives. Exact
   source-rank extraction, pivot selection, and spectral selection also
   need sign/equality tests. State that the exact-real arithmetic model
   includes unit-cost exact comparisons. Their number fits the described
   loop bounds. This is a model clarification, not a finite-bit rank
   algorithm or a conditioning theorem; arbitrary precision oracles do
   not provide exact zero tests for free.
   **Resolved:** both the contract and panel interface explicitly state
   unit-cost exact sign/equality comparisons, and distinguish them from
   a finite-bit zero test.

3. **Place requested-time acquisition in the additive query formula.**
   The main contract explicitly charges acquisition of a requested time.
   Evaluator-interface (11) includes \(T_x\), but its definition at
   line 279 explicitly describes the \(d\) spatial coordinates only.
   If time is separately supplied, include its acquisition and scratch
   in that interface or name a separate term, including in (12). If the
   operation queries the already selected current state and has no new
   time input, say that this charge is absent for that reason. This
   closes a presentation gap in the claim of fully charged work; it
   leaves the internal arithmetic table unchanged.
   **Resolved:** the definition of \(T_x,S_x\) now includes an external
   requested time and its encoding/precision access. The already
   represented internal-clock case is stated separately. These terms
   already appear in both the work and memory formulas.

4. **Qualify the tiny-label nonabsorption statement.** Evaluator-interface
   lines 245–247 say that the floating exponent length \(E_Y\) does not
   fit a bound independent of arbitrarily small positive \(Y\) and must
   be added. This is correct before applying width restrictions. On a
   domain where the inherited gate \(n^{-1}\le Y\) holds,
   \(\log^+(1/Y)\le\log n\), and the displayed core envelope can
   already dominate that length. Keeping the actual input/output charge
   explicit is conservative and useful; describe its nonuniformity before
   imposing those gates, rather than implying an error in the original
   table on its admissible domain.
   **Resolved:** the corrected text makes precisely that qualification
   and preserves the explicit conservative charge.

## Checks supporting the conclusion

For the unseen model, put \(A=m+d+2\) and \(r=m/\gamma\).
The allowed compiler bounds give

\[
M^u\Theta^v\le C\beta^{(301u+200v)L}
 A^u(1+r)^{3u+v}Z^{6u+2v}.
\]

All resource substitutions were recomputed with integer arithmetic:

| Resource | \((u,v)\) | Activation exponent divided by \(L\) | Gap power | \(Z\) power |
|---|---:|---:|---:|---:|
| Retained bits | \((23,3)\) | 7523 | 72 | 144 |
| Runtime peak bits | \((66,6)\) | 21066 | 204 | 408 |
| Initialization work | \((146,16)\) | 47146 | 454 | 908 |
| Initialization memory, first term | \((10,1)\) | 3210 | 31 | 62 |
| Initialization memory, second term | \((54,6)\) | 17454 | 168 | 336 |
| All update work | \((148,16)\) | 47748 | 460 | 920 |
| Query work | \((189,17)\) | 60289 | 584 | 1168 |

Thus the shared \(\beta^{65000L}\) factor covers every row without
trading scientific parameters against a larger width. Primitive counts
use \((u,v)=(9,0),(11,0),(20,1)\), yielding activation exponents
2709, 3311, and 6220. The two precision choices use \((9,1),(11,1)\),
yielding 2909 and 3511. Their other displayed powers also agree. The
extra coefficient-preparation count is dominated by the query count.
External evaluator programs, their actual costs, original encodings,
certificate work, and single-call scratch remain explicit additions.

For the panel collocation schedule, the discrete-cosine coefficients are
the Chebyshev interpolant at the \(k\) root nodes. Integrating each
basis element from zero gives the displayed antiderivative, including
the separate constant and linear cases. Evaluating that polynomial at
the same nodes therefore applies the integrated Lagrange Picard map
exactly. The old derivatives can remain intact while all new states are
written, after which the field is evaluated. With
\(D=Ln^2+dn\), a Picard sweep costs \(O(Dk^2)\) operations and uses
\(O(Dk)\) stage storage plus \(O(k)\) reused scalar scratch. Summing
over patches and iterations gives the stated
\(CN_FD(m+k)\) work. No \(k^2\) table or condition \(k\le n^2\)
is needed. The half-angle construction also produces the power-of-two
root nodes with the stated arithmetic and square-root counts.

Substituting the supplied bounds on \(N_F,k,Q\), and source rank
into the panel producer preserves the displayed \(\beta^{400L}\)
work and \(\beta^{100L}\) memory envelopes. The runtime counts
retain all declared panel dependence, while a cached single query and
an entire panel evaluation remain distinct. Numerical integrator stage
counts are explicit choices; no certified number of steps is inferred.

The deterministic gate calculation was checked against finite-panel
RESULT (9) and (20). The recurrences yield
\(H_j\le\beta^{3j}\), \(M_0\le\beta^{7L}\),
\(\mathcal K\le\beta^{20L}\), and \(D_W\le\beta^{9L}\).
With \(S=16Yr\le1\), the fourth strip term uses
\(32rYS=2S^2\), so the displayed
\(\ell\ge\beta^{50L}(1+r)^2\) gate dominates every term and the
degree gate. This remains an exponential-width sufficient condition,
not an effective stochastic-success threshold.

For label normalization, absolute raw error \(\varepsilon\) changes
the RMS by at most \(\varepsilon\). Allowing another
\(\varepsilon\) for its numerical evaluation gives
\(\widehat Y\ge Y/2\) when \(\varepsilon\le Y/4\), and

\[
\left|\frac{\widetilde y_i}{\widehat Y}-\frac{y_i}{Y}\right|
\le\frac{6\sqrt m\,\varepsilon}{Y}.
\]

The displayed raw precision makes this less than half the requested
error. Exact dyadic squared sums and rational bisection use integers of
\(O(v)\) bits and at most \(O(v)\) iterations, supporting the
\(C(m+1)v^3\) batch bound. The two-pass alternative stores the
normalized cache plus scalar scratch; it does not require the provider
to return identical approximations in both passes. The nonzero-scale
certificate, its search cost, raw-provider workspace, floating exponent,
and chosen output representation are all charged explicitly.

The candidates preserve the full inherited label allowance and distinguish
the finite-panel matched-reference guarantee from the unseen model's
independent-reference upper-certificate guarantee. They neither turn
bare analyticity into a computable activation nor identify numerical
precision certificates with stochastic error estimates. Inherited source
and statistical comparison thresholds remain unquantified. This check
accepts the supplied compiler/source interfaces as inputs and does not
reprove their full theorems.

Process limitation: `AGENTS.md` and `solve-math-rigorously/SKILL.md`
were read. The required canonical-notation skill at
`/home/amir/.codex/skills/explain-with-canonical-notation/SKILL.md`
returned permission denied; its neural-network reference was consequently
unavailable. The explicit repository notation requirements and the
assigned sources' notation were followed. No candidate, maintained book,
code, other study, or Git state was modified by this check.
