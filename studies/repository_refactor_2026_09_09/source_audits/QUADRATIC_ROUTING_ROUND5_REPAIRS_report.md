# Quadratic migration worker report

Status: F1, F4, F5 and F6 implemented; 23 bounded routing tests PASS. This is an implementation handoff, not independent acceptance or scientific validation.

## Scope and repairs

Writes were confined to studies/mfp_quadratic_compiler, the supplied test_quadratic_routing.py, and this private directory. No ResNet, root metadata, core/theory, seals, historical evidence or commit edits were made.

- F1: Campaign 5 Stage A/B provenance and Stage C projection evidence now follow INPUT_ROOT/campaign5_b3. Protocols, live source hashes and the Stage C runner remain source-relative. Explicit missing evidence does not fall back. Existing authorization and hash assertions remain intact.
- F4: Graph JSON exports reject identical paths, symlink/parent aliases and hardlinks to the selected checkpoint before run/loading/computation. Normal checkpoint updates, resume, differentiation-only and evaluation-only remain available. The callable run/save_checkpoint implementations are unchanged.
- F5: Graded output is checked against both lower-result and the selected binary before any sector work. The original frozen lower hash, parent-source and regression gates remain unchanged. A distinct existing result can still be updated.
- F6: Native sparse-reuse output must be distinct from source values and optional target-prefix values before discovery, reads or append. Existing sparse checkpoints may still be resumed. The shared native helper checks resolved paths and existing file identity; filesystem identity errors fail closed.
- Sibling fixes: Campaign 6 benchmark reports cannot overwrite the selected executable; component_parallel.cpp and sector_parallel.cpp reject an aliased checkpoint.tmp before discovery. Ordinary checkpoint replacements remain unchanged. The five postprocessors retain their stricter new-output-only rule through the shared Python alias helper.
- Requested README note: the legacy export_evaluator_reference.cpp power filter is enabled only at argc == 3; extra term-limit/range arguments disable it. This is a static interface observation, explicitly outside this repair and not a numerical validation result. That C++ source is byte-unchanged.

Sibling inspection included the complete graph run/save/main and high_sector main; graded run_order/main; benchmark main; all three native checkpoint driver mains; Campaign 5 provenance tests, Stage C runner/sector gate, two-colour gate and lower-moment interfaces. Existing postprocessor routing tests were retained. No useful tool was retired and Stage C was not reauthorized.

## Reproduced evidence

Command (from this private directory):

```text
env PYTHONDONTWRITEBYTECODE=1 TMPDIR=/tmp/pde-quadratic-worker-7eUHn2 python3 -B /home/amir/Codes/PDE/studies/repository_refactor_2026_09_09/test_quadratic_routing.py -v
```

Exit 0; 23 tests in 0.350 seconds. Full output: [tests.log](tests.log).

Tests cover same-path, symbolic, hardlink and parent-directory aliases; missing/dangling identity; pre-computation rejection; separate existing outputs; mocked deliberate graph checkpoint updates and read-only evaluation; synthetic Campaign 5 evidence/live-source roles, missing evidence and retained mismatch refusal; frozen graded lower/parent hash failures; Stage C refusal before hashing/launch; mocked benchmark success/refusal; direct CLI help and graph package import without output creation. Native tests are static assertions on the complete helper and guard placement, not execution of C++.

Historical manifest testing used only the Campaign 4 sector path/hash mapping and 125 sector byte hashes. The six Campaign 5 moved evidence files were hashed, not scientifically reanalysed. Mocked success fixtures do not constitute fresh scientific evidence or renewed seals.

## Preservation and exact hashes

[Input hashes](input-hashes.tsv) gives the exact before/after SHA-256 and byte count for every one of the 306 paths in the union: 173 original current inputs, one new header, and 132 historical files. There are 11 edited existing files, one added file, no deletions, and 294 unchanged existing files. All 132 historical files are unchanged. No source __pycache__ or .pyc exists in either snapshot.

[before.json](before.json) and [after.json](after.json) also include per-function/class AST hashes. [preservation.json](preservation.json), reproduced by [preservation.py](preservation.py), establishes:

- The three complete native drivers recover their original byte hashes after removing only the new include and identity guard.
- Graph and graded main bodies recover their original AST hashes after removing only the identity statement; all their computational/callable functions remain unchanged.
- Campaign 5 provenance assertions recover their original AST hashes after mapping the evidence-root name back; no assertion or expected digest was weakened.
- Stage C runner, scientific native sources, CURRENT_SOURCE_SHA256.txt, HISTORICAL_SOURCE_HASHES.txt and frozen protocol hashes remain unchanged. No old seal mismatch was repaired to match.
- The README differs only by the requested current-limits paragraph.
- export_evaluator_reference.cpp remains SHA-256 f429865db14efa0623fc2a05e16d52f3328983218a9cea2135dc55baffd7644e.

Changed-file digest index:

| Path | Before SHA-256 | After SHA-256 |
| --- | --- | --- |
| `studies/mfp_quadratic_compiler/README.md` | `4e9f167de013012b127038ca1100fa6a7aea0cbd09bad68c856757edf06341e3` | `65440716fc82d88bce06f9cb59e5c577bf5d37b6dbac2301bdced4f2c9b23683` |
| `studies/mfp_quadratic_compiler/campaign1/run_graded_campaign.py` | `6c1df2f53085c1d31853b4cb06a9733e2bc86a26f276015fbf17eb37725240c8` | `23b2c550a86f32d0e15860852ea85de9c0ebd83182b9ef0b63ad70e3b1ce26d8` |
| `studies/mfp_quadratic_compiler/campaign5_b3/test_stage_a_provenance.py` | `9a66d320788a2ce91013fbb98368eee2aa8d0f9a117d5ab13a6af739e8687c98` | `d9e49700d1e5512db70116770ac92c3bec6cb37e4903a4fea649ece0b8014cc9` |
| `studies/mfp_quadratic_compiler/campaign5_b3/test_stage_c_closed.py` | `63ed83ddddc8de4f9feed158372c9cd0f75c2cb99b6dcedb8280677c2e0c5a9f` | `fef0541e3e6183f1b0d2a03b1a08209e21bda90b021dc079e4af7613ccb88bcb` |
| `studies/mfp_quadratic_compiler/campaign6_f13_threshold/run_benchmark.py` | `f2b35ce19e7df38cb6228e91b8646475ad965cacb812a7b49786abf1642170e5` | `8b9cb48a1c0a6ef12b5af5493a288513eeefbd80af4df0b90fca5dc55caec50f` |
| `studies/mfp_quadratic_compiler/campaign_paths.py` | `9aa339812a929461c49e15c2566545f98b89230f39b48e93292d67c23b66e093` | `bbb7aecb3400bb695cd166fe761e8275eb0462775c37d77904809540a3e40289` |
| `studies/mfp_quadratic_compiler/checkpoint_paths.h` | `ABSENT` | `59b98a143721f1024a424ed7d6a7f2f152909ea6ce78329dffb14b6a816e2c40` |
| `studies/mfp_quadratic_compiler/component_parallel.cpp` | `d51486aaff893ae603acae3d084a0132d3864be0e0869401e74d44fa96681d5a` | `88ee7a84d38250b74fc2993d8cc0fb1a1ebfb572d3ff30e50849ca7b6cd5d376` |
| `studies/mfp_quadratic_compiler/exact_graph_wick.py` | `0678a45afd089a5e690296e2cc7f6f668b3635ca550ab0ee3013b396ac2ca77d` | `34ece0c40aa6f1fbb16a5fca7dc451142ffb3c2174a38062b7bcc5311bfa88fe` |
| `studies/mfp_quadratic_compiler/sector_parallel.cpp` | `9ea028a247f803f3b1beca6e927b74cd8d9717999a88beb09e3fe27a39204ceb` | `d15056b61a75350adb435e023c848722b595e8570aed131736910439d0904b11` |
| `studies/mfp_quadratic_compiler/sector_parallel_reuse.cpp` | `752c9f744e48cbc2ceecfd7800ae57aabbabd40b6fb6315ee22bc16246a4636c` | `65bf4c1e4be6c6394ace052e88025faccdd36b0f076cb33fc139fad69527f63d` |
| `studies/repository_refactor_2026_09_09/test_quadratic_routing.py` | `76c7d08785a8fafdf30dbb12e85e0e4f3fbb731cba6544e3095b68456e81f2be` | `3ac19e66207fbb89909b46f35e2c7eb523ebf2746196a43363b542148dcec412` |

## Limits / handoff

No native compiler, experiment, coefficient generation, science rerun, GPU, install or seal generation/reset was invoked. Optional scientific dependencies were neither loaded nor installed; their runtime availability and numerical correctness are unassessed. Guards address pre-existing aliases, not a concurrent malicious-filesystem guarantee. Opaque benchmark argument semantics are not inferred. Caller-selected arbitrary inappropriate outputs are not blanket-sandboxed.

The power-filter/extra-argument discrepancy remains outside this interface repair and is now discoverable in the current README. ResNet F2/F3 changes and the main worker's reported 15 passing tests were not inspected or rerun here. Independent acceptance is pending the separately planned fresh reviewer. No residual blocker was reproduced within these repaired quadratic interfaces under the stated bounded checks.
