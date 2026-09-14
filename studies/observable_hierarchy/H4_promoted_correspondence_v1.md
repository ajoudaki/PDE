# H4 v3 promoted installation correspondence

**PASS — independent static installation check.** Checked 2026-09-14T08:39:47.426964+00:00.

All 11 approved installations and 20 inherited dependencies match the frozen edition byte for byte and match every declared SHA-256. No tests or training were run.

## Checks

- **PASS**: frozen manifest identities.
- **PASS**: approved scope partitions complete edition.
- **PASS**: approved and edition destination hashes agree.
- **PASS**: all 31 live destinations equal frozen edition and declared hashes.
- **PASS**: all 20 inherited dependencies preserved.
- **PASS**: exact D source and separator removal restores every old chapter byte.
- **PASS**: D is inside C.4.7.10 immediately before C.4.8.
- **PASS**: new runtime files parse and have no study imports or path dependence.
- **PASS**: affected guide recipe names installed plan scripts and supported CLI flags.
- **PASS**: guide-selected worker is resolved beside the supervisor and receives code import path.
- **PASS**: guide file and fragment references within the edition resolve.
- **PASS**: H4 guide and chapter cross-references identify the installed addition.

The D insertion occupies zero-based bytes [645675, 720786), starts at line 13982, and contains 75,110 source bytes plus one LF. Its source SHA-256 is `b755c3d05eacc0ef20df6d0499f73dcc6fbf46abdcf4a04084c346ce6b4ad432`; the inserted-byte SHA-256 is `2eefceea010ce2ca23940b39dd5aa78bfe9be5abcf9af51fcefa46796a90839d`. Removing these exact bytes restores `77e0f2b9a2ecd337c1a47b8f6c2025c72122e28512ca7481377418fe3f235932`, the approved original chapter SHA-256. C.4.8 begins immediately afterward at line 15737.

The guide check resolved 20 file/fragment links within the permitted edition, confirmed the 14-configuration plan and CLI argument names, and checked all four new/changed runtime files for study imports and path dependence. These checks parsed text only.

## Exact input identities

- Final mapping: `3aac433611215b6af76e4d699c85b79bcf322a9643c15520e5b072441dedb5dd`.
- Review manifest, identity only: `06132871ed70c3c13651a3fbb1f8e76d13582301237acb811f50756bdb223d02`.
- Edition manifest: `64bd43d30e11e1f591b12f9c07c76d192c5fa7dcd8f22c1c0e3fd313c27e8250`.

## All final destination hashes

| Destination | Role | SHA-256, frozen = live = expected |
|---|---|---|
| `code/pde/__init__.py` | inherited dependency | `65eb96a5dd455041d2ad1f32652e3e26e8c15192eb41bdffba27980f0f69e8c3` |
| `code/pde/finite_network.py` | inherited dependency | `efe694b200b8af2603cbf1bb9d0249f49636e874088c2bafd98f402b5bfbe551` |
| `code/pde/gaussian_moments.py` | inherited dependency | `6c2a21a9f3d101c433b5f06cb3f6e1dcdeca23a814891ea7bd81e73960e854ae` |
| `code/pde/observable_closure.py` | inherited dependency | `f8dc5d16e5de1737444c44aae737ee1c9b4d664188d72f59acd0bb92f457c137` |
| `code/pde/observable_words.py` | inherited dependency | `b12ed6021dfa8b8409b56793c88334d303f4c2cffeb7aa0a2d460311ba3e41b5` |
| `code/pde/observable_fixed.py` | inherited dependency | `75c5b6a4478e5365d008bd7ad134cf1c2b6cd6942c68358e0a2d4137207c1225` |
| `code/pde/observable_arithmetic.py` | inherited dependency | `2181b9e47e1c765e440feff582b34208651ff4687e19ce8a96db7752402a6edb` |
| `code/pde/observable_compiler.py` | inherited dependency | `1add30410ee2e8de05fffca225643dbbbeab7ab8d6420382014bb8c9cceca7ac` |
| `code/pde/observable_initialization.py` | inherited dependency | `6dafe3b5906c8762c7b6e0782c535b0031bbcf206359d384ef0911853ce131d2` |
| `code/pde/observable_solver.py` | inherited dependency | `711a648df33e587591d35bd709e3b1c052b1a6f7dc6513afe636b2acf7031605` |
| `code/scripts/validate_observable_solver.py` | inherited dependency | `54a8c5dbe8ffa0c105a54a2bc2b6969b83fe56f6f78ef9bdbc19c4b689e7f265` |
| `code/scripts/analyze_observable_solver.py` | inherited dependency | `6c0ae411f567a94ff51e286a09c8f2fec2b90c5d73055ee083c6699f65e75347` |
| `code/validation/observable_solver_plan.json` | inherited dependency | `92bf0cdd9cc5dc0147881ffc07c8235ed8e0480fd91631e7276c3e2e0b856e92` |
| `code/tests/test_observable_compiler.py` | inherited dependency | `8a5955ad47df01a6110e8b5f3b64264b414e8ee70696e7f93250dcdf9dbb17cb` |
| `code/tests/test_observable_initialization.py` | inherited dependency | `9e36f4c120013d58bb082bd521ea683a574bdf5a3652058fc0479a0e665e6e68` |
| `code/tests/test_observable_solver.py` | inherited dependency | `9bb806d59a0d3c0261261d342d83ce97dddb2eb41645894e6a2f2393ecced7f1` |
| `code/tests/test_observable_validation.py` | inherited dependency | `e1ee08c217ce6f39e64801f1c2b64f71482fe6efe5ee8924fe36c6bacc0201c1` |
| `code/pde/observable_laws.py` | approved installation | `6fb38416ce02ca77aae0392201927eb9aeba5c672ebe774181822dfb805d0503` |
| `code/tests/test_observable_laws.py` | approved installation | `96c3b788a11f721a95daa8f4e86088ee2974be93795c2b910fe58b47936f872b` |
| `code/scripts/validate_observable_horizon.py` | approved installation | `3e1704a460a87e6e9f221ecfb73c15c05627f0a864fd4df01337f65a88ce5cb2` |
| `code/scripts/run_observable_validation.py` | approved installation | `d8a66b9a7c16802acc80602f233d76095ed32fcfcdc8a28df321faf9f3d3e0e5` |
| `code/tests/test_observable_horizon_validation.py` | approved installation | `5e49bb2b17ff8225287179714ba855f0b901cc246f389795afb965ea75837ca7` |
| `code/scripts/analyze_observable_horizon.py` | approved installation | `742ea5a7f46d0f7afb279195d33631a350984280ad7c9a86e70f550657499e14` |
| `code/tests/test_observable_horizon_analysis.py` | approved installation | `13419bb449f03bfb6db540156602e49b20719ff852778d031c45202af22a0314` |
| `code/validation/observable_horizon_plan.json` | approved installation | `b89c4a1ff7b8ed335e551f1ff553e7d3aefbe1acdfa914e19444901f080f08e7` |
| `docs/NOTATION.md` | inherited dependency | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |
| `docs/finite_dynamics.md` | inherited dependency | `a57d832a0ce0ad2bf40fa1ec574af787d05bade3264b619a8faca5545bc0012a` |
| `docs/special_data_limits.md` | inherited dependency | `5b7b48aa5deab320042217a6f284002366a683bf0f7f0b63c05d8167c526a489` |
| `docs/global_nonlinear.md` | approved installation | `cbcf00fd705a9a938a6a3fd0d2bbc2f1c2dd3ab4303d848740a549dbb169f629` |
| `code/README.md` | approved installation | `b25c0ad7be0a770881c7ae75446a1718d4217ceec5576bdc14864790daffc91e` |
| `docs/README.md` | approved installation | `0a27a6bc697c65b290bbe6d16c9992575c6221115b992efaef1a78ad983ae13e` |

## Coverage, method and limits

Checker: `python -B studies/observable_hierarchy/H4_promoted_correspondence_v1_check.py`, working directory `/home/amir/Codes/PDE`. CPU use 0.243782 seconds; peak RSS 28,401,664 bytes; enforced limits 60 CPU seconds and 4 GiB address space.

Only shared instructions, the permitted mapping/manifests, frozen edition files and corresponding live destinations were used. All file-byte identities and detailed static evidence are in `H4_promoted_correspondence_v1_checks.json`; the reusable checker is `H4_promoted_correspondence_v1_check.py`.

- No tests, imports of candidate code, numerical experiments, training, Git commands or established-file edits.
- Full bytes hashed for all 31 frozen/live pairs; scientific bodies were not rereviewed.
- No prior reviewer report was opened; verdict labels embedded in permitted mapping were visible but unused.
- Review manifest was accessed for identity metadata only; its named non-edition sources were not opened.
- Static CLI and path checks do not establish runtime behavior or independently reproduce reported empirical results.
- Guide links outside the 31 assigned edition destinations were not checked.
- Pre-install state was not independently captured: original chapter and dependency identity use the approved frozen hashes.
- No commit correspondence is claimed; the supervisor owns Git integration.

The supervisor should retain this report with the exact installation mapping and final commit record. This report does not replace the earlier promotion review or reproduction gates.
