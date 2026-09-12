# Promotion provenance addendum — attributable v2 review records

**Conclusion: the retrieved records corroborate three distinct completed v2 review tasks, each explicitly launched with `fork_turns="none"`, and tie their final messages to the unchanged frozen reports. Their recorded read requests cover the assigned scientific scopes. No launch, completion, report-hash, or requested-coverage discrepancy was found.**

Prepared by `/root/promotion_provenance` on 2026-09-12. This bounded metadata check supplements the existing preflight and does not constitute a new mathematical review.

## Scope and preserved preflight

The supervisor supplied two same-study metadata artifacts and authorized verification of exactly three named source-session lines. I read `promotion_review_events_v2.json` and `promotion_spawn_records_v2.json`. An aggregate tool output truncated part of the reviewer-B event record; I repaired it by separately reading that complete agent object. The remaining event records and all spawn-record fields were completely visible. I used the already-read frozen neutral packets, complete v2 reports, and resolution for comparison; I did not retrieve any assessment.

The original `promotion_preflight.md` remains unchanged at SHA256 `80d2fb8cf0433f2e981add2dfe8a9e2e3fc2687cd64dd67ccba61dda46ba5d53`. Its point-in-time findings and stated original-versus-final document handling remain intact. This addendum records the additional attributable metadata now available; it does not rewrite the earlier evidence boundary.

The only directly inspected session records were lines **958, 964 and 979** of:

`/home/codex-b/.codex/sessions/2026/09/11/rollout-2026-09-11T23-11-17-01a0924f-7b0b-7360-8f81-e593b5f2ca7b.jsonl`

Other lines were discarded while locating these line numbers; no other session record was parsed, displayed, or used. Only whitelisted launch metadata was displayed or retained. The encrypted initial-message field was not displayed, saved, decrypted or assessed. No other session file, study, Git history, assessment, or scientific proof body was read. No book/code/Git change or scientific test was performed.

## Inputs and retained machine record

| File in `studies/trained_prediction_sampling/` | Verified SHA256 |
|---|---|
| `promotion_review_events_v2.json` | `0a3cafa4c700d736cc42c83d9a37d49cbfe34fa08cdb0725964c6bc4ae46957f` |
| `promotion_spawn_records_v2.json` | `08cc2e51cf1c2e9d9cd6c3a2f150a308e40bf1d4b3b550f201d203237ad3fb6d` |
| `promotion_preflight.md` | `80d2fb8cf0433f2e981add2dfe8a9e2e3fc2687cd64dd67ccba61dda46ba5d53` |
| `review_packet_v2.md` | `4eb8fb821a7e87d6819afc1c2fd7e1716e09b7bd2333d83509ca5a02802fb996` |
| `integration_packet_v2.md` | `b6ede822df001807c55ac017c7986de4f541a8fcb1e1fb1f7292d601fa477a4c` |
| `review_v2_A.md` | `32371cdd2fa0e8b26c1d1ac3a7e9f23fca7cabbf0277152d6edc66d336e5fa8e` |
| `review_v2_B.md` | `f6f6f2c492ea25fd27115174f4174abc372e873afbb57a8ba210aea104a93a98` |
| `integration_v2.md` | `0dad4e3f95c1c1918083886227c5c3306ea43168fe263c6d6901aff910456511` |
| `review_resolution.md` | `96dff02189d74b67aa36d1ea680507470b556987fa321e3f260a51077221748f` |

All listed hashes were checked again immediately before this addendum was written and remained identical. The machine verification is retained in `data/generated/trained_prediction_sampling/promotion_preflight_20260912/review_launch_completion_check.json`; it records every identity comparison, each requested interval union and its command IDs, full-file read command IDs, exact timestamps and limitations.

## Launch, attribution and completion

For each source line, the SHA256 of the **raw line including its terminating newline** exactly matches `promotion_spawn_records_v2.json`. Each is a `response_item` / `function_call` for namespace `collaboration`, name `spawn_agent`. Timestamp, item ID, call ID, task name and `fork_turns="none"` all agree with the retained spawn metadata.

| Source line | Task name | Raw-line SHA256 including newline |
|---|---|---|
| 958 | `review_v2_a` | `60309adc419791ca219683489452ebd31e162fbfb8182b00f2bb60fd8fdd43d0` |
| 964 | `review_v2_b` | `ab328323d82083cb4b37fe541a07d8531c6425a5b13bf04bbc98c3afcb98156a` |
| 979 | `integration_v2` | `8895b0b40efa09f0db5608cbc8f77b3e0ff905c577a35e47b1d9818639fb8821` |

Each launch call ID matches exactly one app `started` event with the same agent path and subtask ID. All three subtask IDs are distinct and differ from the parent task ID `01a0924f-7b0b-7360-8f81-e593b5f2ca7b`. Each has one completed turn, a matching parent `completed` event, a completed status and a final answer. Spawn timestamps agree with app start times to the recorded whole-second precision, and completion times follow starts.

| Agent path | Spawn call ID | Distinct subtask ID | Completed turn ID |
|---|---|---|---|
| `/root/review_v2_a` | `call_YAKEO4ZMqU3QsNMKvMm4Ro72` | `01a0926b-c00d-7381-bb03-7bb3a52bd832` | `01a0926b-c055-7632-b321-a25603879f99` |
| `/root/review_v2_b` | `call_EV8AjZnPe73gRPlSk2XgXRG7` | `01a0926b-d85e-7463-a536-d86a4ea9945c` | `01a0926b-d89c-7bc1-80d5-2ac60a07a48f` |
| `/root/integration_v2` | `call_7X0sE41lU2hZFyBT8Cmb8U0J` | `01a0926c-36c5-7973-a375-ad1838ae023c` | `01a0926c-3707-7331-acfa-274cfd1347b0` |

| Agent | UTC start | UTC completion | Recorded completed commands |
|---|---|---|---|
| `/root/review_v2_a` | 2026-09-11T21:42:10+00:00 | 2026-09-11T21:47:22+00:00 | 39 |
| `/root/review_v2_b` | 2026-09-11T21:42:16+00:00 | 2026-09-11T21:49:50+00:00 | 52 |
| `/root/integration_v2` | 2026-09-11T21:42:40+00:00 | 2026-09-11T21:47:25+00:00 | 27 |

The 118 retained command entries all have `status="completed"` and `exitCode=0`. This concerns the entries supplied by the app export; it is not a claim that the export includes every tool event or full command output.

Each final answer names the corresponding report and includes exactly its current SHA256, which also matches the frozen resolution record:

| Completed task report | Final-message/current/frozen SHA256 |
|---|---|
| `review_v2_A.md` | `32371cdd2fa0e8b26c1d1ac3a7e9f23fca7cabbf0277152d6edc66d336e5fa8e` |
| `review_v2_B.md` | `f6f6f2c492ea25fd27115174f4174abc372e873afbb57a8ba210aea104a93a98` |
| `integration_v2.md` | `0dad4e3f95c1c1918083886227c5c3306ea43168fe263c6d6901aff910456511` |

## Requested-read coverage consistency

I extracted only explicit line-range read requests and full-file `cat` requests from the saved command metadata. I did not execute those commands or reread their proof contents. The interval unions have no missing requested line and no extra requested line relative to the scopes below.

| Task(s) | File | Recorded required coverage |
|---|---|---|
| Both proof reviewers, separately | Candidate `proposal_C4_8_v2.md` | Entire 1–1552 |
| Both proof reviewers, separately | Original `docs/global_nonlinear.md` | 1840–2453; 2924–3440; 3836–4946; 5268–11436, totaling 8,411 lines |
| Both proof reviewers, separately | `docs/special_data_limits.md` | 3785–4286 |
| Both proof reviewers, separately | `docs/finite_dynamics.md` | 1–227 |
| Integration reviewer | Candidate `proposal_C4_8_v2.md` | Entire 1–1552 |
| Integration reviewer | `standalone_v2/docs/global_nonlinear.md` | Entire new addition, 11440–12991 |
| Integration reviewer | Original `docs/global_nonlinear.md` | 1–32; 1803–1835; 3836–3980; 5268–5472; 6902–7167; 8976–9293; 9294–9605; 10300–10608 |
| Integration reviewer | `docs/finite_dynamics.md` | 1–227 |

All three records also contain completed full-file read requests for the summary edits, both deterministic check sources, `AGENTS.md`, `RESEARCH_WORKFLOW.md`, `docs/README.md`, and `docs/NOTATION.md`. The integration record additionally requests the complete validator and both assembled guide/notation files. The records include each assigned neutral packet and required skills/references.

The recorded repeat reads agree with the reports' stated truncation repairs: A repeats the guide/notation/summary read and Gaussian-dependency lines 4020–4090; B rereads the guide/notation pair, candidate lines 132–292, finite-dynamics lines 1–227 and the workflow; integration repeats its three sources and the live/assembled guide pairs. Candidate and assembled-addition requests cover the full consecutive blocks reported. Out-of-order execution of independent B chunks does not create a gap in their union.

The metadata also records each proof reviewer executing both prescribed deterministic programs, B executing its contained reference certificate, and the integration reviewer executing the fresh-edition validator and independent integration checker, all with zero exit status. The original reports and previously verified output hashes retain the stated results; this addendum does not recover omitted stdout or independently repeat the checks.

## What this establishes and what remains outside scope

The direct session-line matches now verify the retained no-inherited-turn launch requests and their call IDs. The supplied app event records connect those launches to three distinct task identities, their completed turns, executed command requests and exact frozen report digests. Together with the full original reports and unchanged scientific inputs already checked in the preflight, this supplies concrete launch/completion attribution beyond the reports' own identity declarations. It supports reuse of those completed reviews for the identical approved v2 package under Part 2.

Four limits remain explicit:

1. The app export was retrieved and supplied by the coordinator. I checked its internal attribution and independently matched its launch IDs to the three allowed raw source records; I did not perform a new app retrieval or authenticate unrelated historical records.
2. `fork_turns="none"` verifies the explicit launch setting preventing inherited conversation through that mechanism. The encrypted initial-message contents were not inspected. The app export also contains `interacted` events whose message bodies are absent. Neutral scope and freedom from later scientific contamination therefore still rely on the preserved neutral packets, complete reviewers' isolation statements and coordinator provenance; they are not independently established by these metadata alone.
3. Read commands establish requested ranges and successful command completion. Because the export omits outputs and aggregate truncation details, they do not alone prove that every line reached a reviewer, was personally read, or was correctly understood. The complete reports retain the substantive reading, truncation-repair and adversarial-audit evidence. This check adds no new mathematical verdict.
4. This addendum does not rehash or validate the live post-integration book. The approved append and three summary replacements have the expected final hashes already recorded in the frozen preflight; final live correspondence, affected checks, approval retention, README update and commit remain with the coordinator.

**Administrative finding: the newly inspected evidence resolves the launch/completion attribution gap within this assigned scope. No additional provenance blocker was found for the unchanged approved package.** The original reports and preflight remain frozen.
