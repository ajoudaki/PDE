# Generated data and figures

Generated outputs belong here, not beside implementation files or manuscripts.
Everything except this README is ignored by Git. Do not place the only copy of
a proof, source program, hand-authored configuration or essential dependency here.

`historical/` retains the numerical arrays, generated coefficient tables,
figures, mixed binary release bundles and build products moved during the
9 September 2026 cleanup. `original_backups/` retains the old working-copy
backups. No numerical bytes were deliberately deleted. Existing Git history
still contains previously tracked data; the cleanup does not rewrite history.

The source-controlled migration and recovery manifests live in the refactor
study. They record the original paths, new paths, sizes and hashes. Some old
study commands still describe their historical output locations: consult that
study's migration notes before executing a historical campaign.

New established reproductions use `data/established/<run-name>/`, with explicit
commands, parameters and seeds documented by the corresponding source module.
New study outputs use `data/generated/<study-name>/<run-name>/`. A replay must
read retained historical inputs separately from its fresh output directory;
never overwrite the historical archive or silently regenerate an old seal.
No figure or empirical numerical conclusion is accepted into the established
documentation without its complete reproduction recipe. Historical retained
data are evidence archives, not a claim that all old campaigns can currently
be regenerated in the minimal supported environment.

The permanent [study workflow](../RESEARCH_WORKFLOW.md) requires each study's
arrays, figures, logs, caches and temporary review/test workspaces to remain in
its own `generated/<study-name>/` namespace. Keep source, hand-written
configuration and durable run/hash receipts in the study. Use a fresh run ID;
never overwrite prior runs or consumed inputs. Record the exact command, source
and input hashes, configuration, seed, environment, exit status and analysis
chain. An interrupted or failed run is not a successful reproduction.

Empirical promotion requires independent end-to-end reproduction using maintained
code into a fresh `established/<run-id>/`; archived arrays or downstream table
checks alone are insufficient. The general workflow is not new authorization to
run training or historical campaigns. No proof or unique source dependency may
exist only in ignored generated data.
