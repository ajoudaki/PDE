# Exact archived discovery-producer source

The four selected width-2048 discovery dense references are backed by an
exact recovered producer file matching their recorded SHA256. The current
`scaling_benchmark.py` has later wrapper changes; it is not silently substituted
for the archived producer. No old source, archive, or frozen suite manifest
was modified, and no GPU work or simulation was performed.

This narrow reconciliation concerns only `quadrant_pairs_full` and
`two_outliers_alternating_full`, each at its selected primary and refined
level, and only the source path
`studies/random_dictionary_learned_circle_20260920/scaling_benchmark.py`.
All other source checks remain separate requirements.

## Exact retrieval and digest

The two primary producer configurations record Git HEAD
`acfbedf78aaf104ba2a54053ac354404ebe66e40`; the two refined configurations
record `22d2ed040258f5927de5367e815e80527f097743`. Read-only retrieval of
the one authorized original-study source path at each recorded commit
succeeded. Both retrieved files have identical bytes and SHA256

```
fce49cb577e89e1bed1a043277fd786af52b37ddac5b55a2ccfd861f9f637a9a
```

This is exactly the digest recorded by all four producer configurations.
The recovered files are retained in
`data/generated/gradient_flow_probe_dictionary_20260921/suite_inventory01/sourceproofs/`:

- `acfbedf7_scaling_benchmark.py`: exact primary-commit source; usable frozen
  source for all four digest checks.
- `22d2ed04_scaling_benchmark.py`: identical source recovered independently
  from the refined configurations' recorded commit.
- `git_retrieval.json`: exact commit/path, retrieval exit status, retained
  paths and digests.
- `acfbedf7_versus_current.diff` and `22d2ed04_versus_current.diff`: complete
  source differences.
- `reconciliation.json`: exact four endpoint/configuration identities,
  configuration hashes, commands, frozen/current source digests and scope.

The current wrapper SHA256 is
`8f1fb614fba6bf1a895a78adf778069e43ddfde8854814955e1d64a881eaa7f1`.
Git was used only to read the specified source file at the two recorded
commits. No other study file or its history was inspected.

## What changed after the archived runs

Every affected command uses `--group discovery --stage A`, width 2048,
network seed 20260920, dictionary seed 7319, and orders 6/7 with the full
reference included. Primary rtol/atol are 6.25e-5/6.25e-7; refined values
are 1.5625e-5/1.5625e-7.

The complete current-versus-archived differences are:

1. Add the `user_width4096` allowed stage and a `--protocol` option whose
   default is the previously hard-coded `SCALING_PROTOCOL.md`.
2. Broaden the multiple-case guard only for `group=width` and the newer
   `user_width4096`/`extra` branches. All four affected commands have
   `group=discovery`, so this guard does not execute.
3. Add a validation guard only for `stage=user_width4096`. All four affected
   commands have `stage=A`, so this guard does not execute.
4. Record `protocol_path` in provenance and hash the protocol argument.
   These archived commands contain no `--protocol` flag; the default refers
   to the same old file. The added provenance field changes metadata output.

The complete main-function body from the worker timer through network
initialization, dictionary construction, trajectory execution and completion
record has identical syntax trees after removing source-position attributes.
The diff additionally shows unchanged width, seed, tolerance and case selection
for the executed discovery branch. Thus these wrapper changes do not change
the mathematical or numerical path of the four archived dense trajectories.
This statement is a source comparison, not a new numerical replay or a claim
that arbitrary future changes to the wrapper are harmless.

## Audit use

For the four enumerated configurations, authenticate the critical recorded
producer against the recovered exact file and its expected digest. Retain
the current-file mismatch and this reconciliation as provenance. Do not
remove `scaling_benchmark.py` from the critical dependency graph, and do not
waive any unrelated source mismatch. Other maintained and study dependency
digests must still pass the analyzer's independent source checks.

`SUITE_MANIFEST.json` remains unchanged at SHA256
`d34ea135c3a2d60dcccce94f23114d92a3692ac3475d13fc3d20dd68387b3670`.
This report and the machine-readable mapping supplement that frozen manifest.
