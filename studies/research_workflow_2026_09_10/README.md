# Study workflow maintenance

This study maintains the shared research workflow for PDE and PDE-2. It is
repository-process work, not a mathematical promotion. The user explicitly
requested the current simplification after clarifying the intended routine.

## Current result and scope

Root AGENTS.md introduces one RESEARCH_WORKFLOW.md with separate routine-study
and promotion parts. Each study's existing README is its only required
administrative record. Tasks and studies have a many-to-many relationship.
Internal verification includes persisted evidence and executed empirical
reproduction; it is separate from the stronger independent relevance/correctness
and editorial checks for promotion. The user must approve the concrete reviewed
addition before established book/code changes.

The optional shared helper retains compatibility with structured study/packet
records. It no longer generates or requires ordinary per-study AGENTS.md files;
existing such files are preserved. Its checks cannot grant internal verification
or user approval. The redundant live instruction file in this study was removed.
Other earlier records below are retained for their historical evidence, not
required for future studies.

The coordinator `/root` owns the shared edits and is the sole Git writer.
The bounded edit list is root AGENTS.md, RESEARCH_WORKFLOW.md and README.md;
studies/README.md and studies/_workflow.py; this study's README, redundant
AGENTS.md removal, tests and current review reports. Generated diagnostics go
under data/generated/research_workflow_2026_09_10/. No scientific campaign is opened.

## Checks and current disposition

This simplified edition passed internal tests and two fresh complete independent
process/code reviews. Both reviewers read all 1,277 selected lines; their original
reports are [A1](reviews/LIGHT_WORKFLOW_A1.md) and [B1](reviews/LIGHT_WORKFLOW_B1.md).
The coordinator read both reports completely and verified initial/final input
hashes and actual execution evidence. No required correction remains. These are
maintenance checks, not acceptance of a mathematical or empirical PDE result.
Baseline HEAD is `15042ed697eab69a4c3746cd490fa4dd2db37a3a`. All fourteen
inherited dirty paths match the earlier START.json preservation receipt (six
readable hashes; eight metadata-only), and the shared index was empty at startup.

The deterministic regression command is:

```sh
python -B -m unittest discover -s studies/research_workflow_2026_09_10/tests -p test_workflow.py -v
```

The coordinator and both reviewers passed all ten deterministic tests. Independent
checks covered tasks spanning studies, multiple contributors, no new ordinary
instruction files, preservation of existing records, rollback and missing evidence.
All 126 local guide links resolved, all 27 accepted scientific input hashes stayed
unchanged, and all fourteen inherited paths remained preserved. This result applies
to the exact [reviewed input manifest](reviews/LIGHT_INPUTS.json); it does not reuse
the earlier edition's favorable verdicts. No required implementation work remains.

Generated coordinator logs: `data/generated/research_workflow_2026_09_10/simplification_r1/`.
Python 3.10.12; test exit status 0. Test-log SHA256:
`5d7455fcab6650d62fa5ab531e142b823d26131eff2cf2128b0ac8523defede8`.
Integration-check receipt SHA256: `1826516e75b50ab8e874a4f0b122495ed6c2ad5e6bd9de7fb38a37a28381c9a9`.
Original report SHA256 values:

- A1: `8356e1212239bbcf4f4f97a9e109ce13fd7eee4a11e3ee64bc150a92e52d9f0d`
- B1: `4399fbc3bd6282e62a313b773cfc7e3e9e60c755cae3dc6a3b3231a7061fb203`

The complete independent diagnostic programs are embedded in the reports. To replay,
use the exact reviewed source version and fresh study-owned scratch directories;
change only each program's scratch assignment. The scripts expect the manifest at
`data/generated/research_workflow_2026_09_10/simplification_r1/inputs.json`:
restore it from `reviews/LIGHT_INPUTS.json` if absent, or verify existing bytes match;
never overwrite a different run. Thus no unique diagnostic source or manifest lives
only in ignored generated data. These checks do not test the other credential's
private configuration or claim OS enforcement of the workflow.

## Earlier edition, preserved as history

The larger initial workflow was committed in `2fe4a69` and sealed in `15042ed`.
[ACCEPTANCE.md](ACCEPTANCE.md), [COMMITS.json](COMMITS.json), STATE.md, CLAIMS.md,
EXPERIMENTS.md and the original review packets describe that earlier edition;
their favorable verdicts do not review the current changed files. This README
is now the current maintenance record. [AUTO_LOADING.md](AUTO_LOADING.md) records
an actual fresh-task discovery check of the earlier entry file; the same shared
file locations are used, without changing either credential's configuration.
[REPLAY_REVIEWS.md](REPLAY_REVIEWS.md) reproduces the original frozen diagnostic
edition, not a verification of later changed helper code.
