# Recovered sources — 9 September 2026

**ARCHIVAL: acceptance/status unknown.** These are byte-exact historical sources, not newly established results. Original claims, corrections, rejected drafts and review verdicts remain unchanged.

The initial recovery contains **269 payload files, 6,078,707 bytes**, all verified against the source SHA-256 and size before copying and against the destination afterwards:

| Selection | Files | Bytes |
|---|---:|---:|
| Original approved recovery plan | 247 | 5,904,672 |
| Stieltjes pre-cleanup tar supplement | 22 | 174,035 |

The original plan includes 176 external files, 49 unique ZIP members and 22 distinct existing-backup documents/sources. The three historical backup PDFs are document editions, not numerical figures. No raw arrays, coefficient tables, compiled binaries, caches or archive containers were imported. No recovered code was executed.

Payload lives under `recovered/`. Exact source → destination mappings and hashes are in [COPY_PLAN.jsonl](manifests/COPY_PLAN.jsonl) and [TAR_SUPPLEMENT.jsonl](manifests/TAR_SUPPLEMENT.jsonl). Verification records are [VERIFIED_ORIGINAL.jsonl](manifests/VERIFIED_ORIGINAL.jsonl) and [VERIFIED_TAR_SUPPLEMENT.jsonl](manifests/VERIFIED_TAR_SUPPLEMENT.jsonl). Every JSONL manifest has at most 250 rows.

[RECOVERY_IMPLEMENTATION.json](RECOVERY_IMPLEMENTATION.json) records completed copying, checks and limitations. The 11 original inventory/supplement manifests in `manifests/` were themselves copied byte-for-byte. Their pre-copy report/index remain historical; the implementation record supersedes their “nothing copied” and uninspected-Stieltjes-tar statements.

The Stieltjes archive's 187 members were safely listed. Of 60 source candidates, 37 match repository sources, 22 distinct campaign implementations/protocols/audits were recovered, and one unreferenced scratch script was excluded. Full classification is in [TAR_INVENTORY.jsonl](manifests/TAR_INVENTORY.jsonl).

Coverage remains bounded to the documented temporary-source patterns, 21 selected temporary directories, accessible codex-b checkout and seven report-listed proof attachments, plus the inspected repository ZIPs and Stieltjes tar. Raw sessions were not copied; old tasks and other agents were not contacted. The historically reconstructible `ROUTE_CAUSAL_COMPOSITE.md` is still not a materialized file; its locator is retained in [KEY_CHECKS.json](manifests/KEY_CHECKS.json).

Original files, Git and the main repository layout were not changed. Existing-repository duplicates were not recopied; source paths/import names and references to excluded data remain untouched. This is a recovery component for the non-data rollback snapshot, not a runnable reconstruction of every historical package.

The coordinator subsequently preserved three additional Markdown checkpoint
editions (102,143 bytes) before relocating cache directories. These are explicitly
separate from the initial 269-file record: [checkpoint supplement](manifests/CHECKPOINT_SUPPLEMENT.json).
The complete recovery payload is now 272 files, 6,180,850 bytes. No checkpoint
edition is promoted as current theory.
