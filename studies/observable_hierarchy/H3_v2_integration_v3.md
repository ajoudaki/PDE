# Complete isolated integration review — packet v3, frozen edition v2

**Verdict: REQUIRED CORRECTION; this frozen edition is blocked for integration.**
The complete assigned review found one new Markdown rendering defect in a proof
inequality (R1 below). It is a small documentation correction, not a newly found
mathematical counterexample or solver failure. All remaining integration
components passed at their stated scope. No candidate file was changed.

## Identity, isolation and scope

Reviewer: `/root/h3v2_integration_v3`, fresh isolated integration reviewer.
The neutral assignment was the sole task-specific discussion inherited. The
manifest identifies authors/assemblers `/root`, `/root/h3v2_route_basis`,
`/root/h3v2_route_gaussian`, `/root/h3v2_scope` and
`/root/h3v2_scope/arithmetic_audit`; selector `/root/h3v2_relevance`; the evidence
manifest identifies reproducer `/root/h3v2_reproducer`. I am distinct from
these roles. I did not consult a scientific reviewer, prior verdict, human
reproduction report, author discussion/history, other study or external
scientific source. The only subsequent supervisor message requested progress
metadata and explicitly said to continue the complete review. No subreview
was substituted for my reading.

I read `AGENTS.md` and the complete `RESEARCH_WORKFLOW.md` under its independent
isolated review scope. I used the complete required instructions of
`/etc/codex/skills/solve-math-rigorously/SKILL.md` and
`/etc/codex/skills/investigate-conjectures/SKILL.md`, including the latter's
research-contract, adversarial-audit and decisive-experiments references.
This is a complete review of the assigned integration, not a fresh whole-book
proof audit or a replacement for the two scientific reviews.

All outputs are this report and fresh scratch under
`/home/amir/Codes/PDE/data/generated/observable_hierarchy/H3_v2_integration_v3/`.
I did not use Git, edit the frozen edition, run finite-network training or
generate an additional solver trajectory. In particular I did not rerun the
guide's trajectories: its complete auxiliary producer and immutable execution
evidence were inspected instead.

## Frozen identity and hash verification

The edition root is
`/home/amir/Codes/PDE/data/generated/observable_hierarchy/H3_v2_edition_v2/`.
The following SHA256 values matched at entry and exit:

| Input | SHA256 |
| --- | --- |
| Neutral integration assignment v3 | `08199ea87daa0b0217a953c5bcdbd08929485384262d4682353ba079edd67286` |
| Edition `review/manifest.json` | `13a21f2c652ac583243ae4f680bebfaca4576147a14ea557c0d6610336e38dc8` |
| Complete evidence manifest v3 | `a2673a062eac3f86559d6e811d877b4b1cd7c14bc99f61f7c9b31b9096919ea8` |
| Integration comparison manifest v3 | `d76088fdd6b430542388d08ad5b3e573da93af6196c2d0f1532ba550ac091126` |
| New section | `2a5743ff533492cadd406e3e0284aae174902b381a05a53773e017b21ea071f8` |
| Complete selected dependency packet | `452276358e23c958cf6a7140d8227188b11e5b8aba688ab5e8c4cfff3924ac84` |

All **126 assigned paths** were verified: four trusted assignment/manifests,
27 edition files, 92 complete-evidence files and three frozen base files.
Each path, expected/actual digest and byte length is recorded in
[entry_hashes.json](/home/amir/Codes/PDE/data/generated/observable_hierarchy/H3_v2_integration_v3/entry_hashes.json)
and
[exit_hashes.json](/home/amir/Codes/PDE/data/generated/observable_hierarchy/H3_v2_integration_v3/exit_hashes.json).
Every exit digest and byte length equals its entry value. Live paths listed
only as source provenance were not fetched. The assigned auxiliary reproduction
sources were read directly; their three executed copies have identical bytes.
The human report digest appearing as metadata in the reproducer's exit JSON
was not followed to its report.

## Complete reading coverage

All lines of the new section (1–1423), library guide (1–184) and notation
contract (1–98) were read. Every selected dependency line (1–5131) was read,
including proofs, calculations, qualification paragraphs and contained
certificate code. Truncated initial reads were repaired with bounded reads;
later machine-output truncations were repaired or resolved by exact equality
to fully read duplicate records.

The precise older scientific scope, using the packet's own source boundaries,
was:

| Source | Complete assigned bodies read |
| --- | --- |
| `special_data_limits.md` | III.F.1–10: finite programs, operator bound, conditioning, source response, singular queries, feedback, common carrier/adjoints, Hilbert–Schmidt state, multipliers and scalar gradient calculus |
| `global_nonlinear.md` | A.1–4; all C.4.1; all six parts of C.4.2; C.4.3 parts 1–3 |
| Same | All C.4.5.1 and C.4.5.2 parts 1–4 |
| Same | C.4.7 model/conclusions 1–3 and observation contract; complete C.4.7.2–5 |
| Same | Complete C.4.7.8 and C.4.7.9, including their initialization, comparison, identification, observations, restart and scope paragraphs |
| Adjacent placement | C.4.8 introduction/model and its explicit restoration of `T=40`, carrier, finite initialization, law neighborhood and output spaces, frozen chapter lines 13979–14042 |

The scientific complement of the copied full chapters was **not** audited:
all `special_data_limits.md` outside III.F, and all `global_nonlinear.md`
outside the selected bodies, new section and adjacent placement scope above.
The full frozen base chapter and proposed chapter were consumed for byte
correspondence only outside that scope. Reading a chapter synopsis or an
existing link in a guide did not authorize or trigger reading its target's
unassigned proof. No other chapters were fetched.

Complete code bodies read:

| Component | Full files and line counts |
| --- | --- |
| Six new modules | `observable_fixed.py` 223; `observable_arithmetic.py` 230; `observable_words.py` 217; `observable_compiler.py` 528; `observable_initialization.py` 397; `observable_solver.py` 350 |
| Unchanged import/dependency modules | `__init__.py` 26; `finite_network.py` 363; `gaussian_moments.py` 114; `observable_closure.py` 697 |
| All five tests | closure 312; compiler 157; initialization 243; solver 133; validation 223 |
| Three maintained scripts | validation worker 123; analyzer 293; supervisor 296 |
| Configuration | `observable_solver_plan.json` 187 |
| Auxiliary reproduction sources | Complete budget wrapper, guide example and read-only audit, plus byte-identity checks of their executed copies |

Both complete base guides and both complete proposed guides were covered:
base docs 717 lines and proposed docs 725; base code 748 and proposed code 934.
Common bodies were read completely once, all additions/replacements were read
completely, and byte correspondence established their exact occurrence in
each proposed guide. The complete appended library guide was also read as its
standalone frozen input. Both new Python examples were inspected and parsed.

The complete machine evidence was inspected: all twelve `record.json` bodies,
all supervisor entries, both full analysis products, every command/result,
test/example/worker/audit log, environment and hash inventory, and the complete
auxiliary read-only audit. Repeated summary fields were checked against the
fully read original record fields; every remaining summary field and all 16
comparisons were read. All 24 checkpoint files were decoded, and all twelve
NPZ archives were inspected and used in reconstruction. No unlisted human
interpretation was an input.

## Required correction

**R1 — format the integrated comparison inequality as mathematics.**
At
[proposed_section.md:839](/home/amir/Codes/PDE/data/generated/observable_hierarchy/H3_v2_edition_v2/review/proposed_section.md:839),
identically at
[global_nonlinear.md:13393](/home/amir/Codes/PDE/data/generated/observable_hierarchy/H3_v2_edition_v2/docs/global_nonlinear.md:13393),
the plain-text expression is:

```text
sup_t e_N<=CT exp[C(1+s)T]((1+s)epsilon_N+tau(s)).
```

Its brackets and parentheses form a Markdown link. The installed Markdown
renderer produces:

```html
sup_t e_N&lt;=CT exp<a href="(1+s)epsilon_N+tau(s)">C(1+s)T</a>.
```

Thus the entire factor `((1+s)epsilon_N+tau(s))` disappears from the displayed
inequality into a nonexistent link destination. This changes what the reader
sees at the step justifying the ordered limit. It is more than cosmetic line
wrapping. The raw argument has the needed factor; no mathematical repair is
requested. Replace the expression with a properly delimited formula, for
example:

```tex
\[
\sup_{0\le t\le T}e_N(t)
\le CT\,\exp\bigl(C(1+s)T\bigr)
       \bigl((1+s)\epsilon_N+\tau(s)\bigr).
\]
```

Preserve the following ordered-limit sentence. Apply the same corrected
section to the proposed chapter when creating a new edition. The exact input,
rendered output, source digest and line locations are saved in
[render_check.json](/home/amir/Codes/PDE/data/generated/observable_hierarchy/H3_v2_integration_v3/render_check.json).
The check used Python-Markdown 3.3.6. No frozen correction was made here.

This was initially suspected to be an overbroad link-check match. Four short
checks retained in scratch tested exclusions for delimited math and examples;
the expression is actually unformatted prose, and direct rendering confirmed
the defect. Those original logs and script versions are preserved. The final
audit continued through all other checks and records R1 explicitly.

## Component assessments

| Component | Verdict | Evidence and limits |
| --- | --- | --- |
| Scientific interfaces and notation | PASS within integration scope | Same bias-free two-hidden tanh Gaussian model, normalized directions, mobilities `(n,1,n)`, unhalved loss and physical clock; actual finite Gaussian readout retained in the finite bridge |
| Law family and horizon | PASS | Fixed rational two-arc family, degenerate atomic members, nonorthogonal correlations and nonatomic laws; convergence stops at `1/200`, independent of every resolution parameter |
| Numerical/outer limit interfaces | PASS | Arithmetic, time, input, population and initialization refinements followed by source regularization removal where used; outer dictionary order last; qualitative iterated convergence rather than an arbitrary simultaneous limit |
| Placement and preservation | PASS | Exactly one new section inserted before C.4.8; all old chapter bytes preserved, with one extra newline separator; entire base code guide preserved with the exact heading-shifted library-guide append |
| Roadmap and guide summaries | PASS | Accurately separate short-time H3 from time-40 H4; precision, quadrature, feature conditioning, resource limits and exploratory usage are explicit |
| New links/rendering | REQUIRED CORRECTION | Intended C.4.7.10 roadmap fragment resolves; R1 is the sole additional link-like expression found and fails rendering |
| Package/import interfaces | PASS | All 18 Python files parse; all ten package modules import from the frozen edition; six new modules depend only on package peers, NumPy and the standard library |
| State, actions and restart | PASS | Full joint marks retained; one evolving feature action `M` and its transpose; frozen `D`; current `w,c`; exact scalar checkpoint encodings; no trajectory history or initializer replay required by restart |
| Deterministic verification | PASS | All 54 tests passed, including independent gradient/energy and transpose checks, singular sources, named partials, exact syntax, arithmetic, resource failures and restart |
| Maintained reproduction/analysis | PASS | Full immutable twelve-run evidence has exact producer/configuration/output provenance; regenerated analysis matches every field except its own elapsed CPU time; Markdown summary byte-identical |
| Hashes/isolation/resources | PASS | All 126 assigned paths unchanged; no extra trajectories, outside-study inputs, frozen edits or Git operation |

The new closure is a justified compatible variant, rather than a claim that
the older prototype's finite numerical defaults inherit the new theorem.
The raw-state comparison, common Gaussian source construction, persistent
formal named derivatives, joint law contract and reached-state restart agree
with the complete older dependencies. The inverse lower-Cholesky orientation
and positive ridge match the implemented filter. The polynomial core keeps
both covariance and reverse-to-forward response contractions. The general
compiler preserves the full joint source program and its regularization;
no hidden rank deletion or independent marginal resampling replaces it.

Order 5 deliberately retains two redundant constant tail words. Its large
finite P-mark Gram condition number is therefore not evidence of a silently
pruned dictionary, nor is it a certificate for the Q-rule raw initialization
Gram. The guide and analysis distinguish those objects. Their limitations
also distinguish scalar-slot/state accounting from complete process peak RSS
and from a cost-to-accuracy theorem.

The new material supplies local arguments for the broader short-time family;
it does not assume that every represented arc law belongs to the old fitted
reference neighborhood. The adjacent C.4.8 introduction explicitly resets its
own law neighborhood and `T=40`; the insertion does not widen that theorem.
Whole-circle prediction is a mathematical claim and a direct evaluation API;
the saved 128-direction panel remains a diagnostic. Paired initial/current
observations share their own population marks, and their RMS uses population
and training-rule weights. No empirical signal threshold is required by this
review or inferred from the small recorded motions.

## Predeclared and actual checks

The checks and success criteria were recorded before execution in
[predeclared.md](/home/amir/Codes/PDE/data/generated/observable_hierarchy/H3_v2_integration_v3/predeclared.md).
The predeclared allowance was 600 CPU seconds, 4 GiB and one numerical thread,
with no new trajectory configuration. Numerical commands used the retained
budget wrapper copied byte-for-byte into this review's scratch. It set the
thread variables to one, `PYTHONPATH` to the frozen package, no bytecode,
temporary directories to scratch, and CPU/address-space limits. The old
prototype override environment variable was removed.

Actual successful commands, all with the frozen edition as working directory,
were the following. The wrapper's absolute path is
`/home/amir/Codes/PDE/data/generated/observable_hierarchy/H3_v2_integration_v3/bounded_command.py`.

```text
python <wrapper> --name tests --cpu 180 --memory 4294967296 python -B -m unittest discover -s code/tests -p 'test_observable*.py' -v

python <wrapper> --name analysis --cpu 180 --memory 4294967296 python -B code/scripts/analyze_observable_solver.py --plan code/validation/observable_solver_plan.json --runs data/established/independent_v2_runs --output /home/amir/Codes/PDE/data/generated/observable_hierarchy/H3_v2_integration_v3/analysis --recount-state

python <wrapper> --name static_complete --cpu 60 --memory 4294967296 python -B /home/amir/Codes/PDE/data/generated/observable_hierarchy/H3_v2_integration_v3/static_evidence_audit.py

python <wrapper> --name render_check --cpu 10 --memory 4294967296 python -B /home/amir/Codes/PDE/data/generated/observable_hierarchy/H3_v2_integration_v3/render_check.py
```

Exact argument arrays, working directory, environment, exit status, CPU and
memory for **every** bounded command are retained in its `_command.json` and
`_result.json`. The four earlier static executions, with names
`static_evidence`, `static_evidence_corrected`, `static_evidence_final` and
`static_evidence_pass`, exited at the same new-link assertion before the rest
of the audit. They are not candidate test failures; their final explanation
is R1. No test-suite rerun or replacement trajectory followed them.

| Successful check | Result | Reaped child CPU seconds | OS peak RSS bytes |
| --- | --- | ---: | ---: |
| Frozen deterministic suite | 54 tests, OK; test runner elapsed 4.546 seconds | 4.431123 | 57057280 |
| Maintained analysis | 12 records, 16 comparisons, no problems | 0.482037 | 70639616 |
| Complete static/evidence audit | Complete, records R1 and passes remaining checks | 0.931385 | 77266944 |
| Exact rendering witness | Confirms the unintended link and hidden factor | 0.091297 | 20746240 |

Including all four failed preliminary link assertions, measured bounded child
CPU was **6.586117 seconds**, with maximum measured OS peak RSS **77266944
bytes**. Entry and exit hashing each took less than 0.1 CPU second. Plain-text
reading and small metadata/format comparisons were additional short processes;
they were not accumulated into that child-CPU figure. The review remained
well within the total 600-second allowance. No numerical computation was run
outside the bounded one-thread environment.

The maintained analyzer was rerun without evolving anything. Its fresh JSON
differs from the frozen summary only at `postprocessing_cpu_seconds`; its
Markdown summary is byte-identical. Independently written formulas reconstructed
both saved layer-pair arrays and circle predictions from all final checkpoints,
with maximum float64 discrepancy `2.7755575615628914e-16`. Midpoint and final
frozen marks and data laws agree exactly. All source/configuration/output
hashes, full state schemas and repeated record/summary fields matched.
The guide's recorded own-state continuation matches uninterrupted and in-memory
continuation in all nine state arrays and all three data arrays. Those are
operational consistency findings, not canonical-error estimates.

The original immutable evidence reports twelve successful configurations,
19.481271854 seconds of worker body CPU (21.083589 seconds charged by the
supervisor), and maximum worker RSS 76480512 bytes. Its plan and maintained
scripts regenerate initialization and evolution from inputs into fresh output
directories. No retained experiment, study loader, target trajectory or external
Gaussian-action service is needed by the maintained solver. The ancillary
read-only audit naturally reads the frozen outputs; it is not an evolution
dependency.

## Optional suggestions and completion limits

No additional optional change is needed for this review. Broader conversion
of plain ASCII formulas into mathematical notation could be scheduled as
editorial work, but R1 is the only required correction identified here.
Rates, true-error certificates, an automatic tolerance selector, efficient
arbitrary-order generic compilation, an all-observation runtime compiler,
numerical hidden-motion thresholds and time-40 computation are not imposed as
completion requirements.

All assigned integration checks and reading are complete; no scientific input
was missing. Completion evidence is retained in
[static_evidence_audit.json](/home/amir/Codes/PDE/data/generated/observable_hierarchy/H3_v2_integration_v3/static_evidence_audit.json),
[completion_checks.json](/home/amir/Codes/PDE/data/generated/observable_hierarchy/H3_v2_integration_v3/completion_checks.json),
the exact rendering witness, the regenerated analysis and the entry/exit hash
inventories. The unchanged frozen edition remains blocked solely by R1.
This report grants neither promotion approval nor a substitute scientific
verdict for any unassigned part of the book.
