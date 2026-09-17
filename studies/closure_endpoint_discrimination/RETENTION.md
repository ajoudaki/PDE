# Network checkpoint retention

The six-GiB campaign cap includes network states, each of which retains its
complete middle matrix. To continue the same trajectories without multiplying
this storage at every common checkpoint, a superseded successful `state.pt`
may be retired after its direct continuation has been verified.

`RETIRE.py` is restricted to this study's `campaign_001` folder. Preparation
does not delete. It requires both successful records, current hashes of both
states and trajectory archives, matching frozen source/input/initialization and
trajectory settings, a strictly later direct child, and an exact copy of the
complete old history at the beginning of the child history. Both prior
`VERIFY.py` reports must bind those files and show independently performed
**exact** dense endpoint replay. The child report must also record the live
parent checkpoint hash observed during verification. Frozen `NETWORK.py`
checks the old output hash before loading a continuation, but it does not save
a separate consumed-byte digest; this lineage therefore also relies on the
supervisor preserving completed output files unchanged. Reports containing
only producer replay statements or deferred independent replay do not suffice.
The declared verifier version must be in the helper's explicit approved list.
Genuine report provenance is supplied by the supervised verification workflow;
these local JSON records are not cryptographically authenticated attestations.

Preparation writes a new, read-only `state.retirement.json` beside the old
checkpoint and persists it before returning. A separate explicit
`--execute descriptor` invocation revalidates all evidence and file identities,
then unlinks exactly that old `state.pt`. The latest child, every record,
configuration, trajectory, dense output, log, failure artifact, verification
report and descriptor remains. A read-only receipt records completion. A
failure before unlink leaves the old state intact; an interruption after unlink
can be recovered by re-executing the same descriptor and retaining the truthful
recovery status. A descriptor alone does not establish completed retirement.

```
python -B studies/closure_endpoint_discrimination/RETIRE.py \
  --old /absolute/campaign_001/old_run/state.pt \
  --new /absolute/campaign_001/continued_run/state.pt \
  --old-verification /absolute/campaign_001/old_verification.json \
  --new-verification /absolute/campaign_001/new_verification.json

python -B studies/closure_endpoint_discrimination/RETIRE.py \
  --execute /absolute/campaign_001/old_run/state.retirement.json
```

Only the campaign supervisor may schedule execution, after all readers of the
old checkpoint have finished. Helper invocations share an exclusive retirement
lock. Completed producer files and directory entries must remain unchanged
during preparation and execution; the helper pins the parent directory before
unlinking, while the supervisor excludes competing writers to that directory.
The helper rejects failed runs, non-network states, non-increasing
time, altered evidence, path traversal, symlink components and hard-linked
checkpoint files.

For a missing historical resume state, `VERIFY.py` checks the preserved records,
original verification reports, immutable descriptor and receipt, then follows
strictly increasing retirement links to an existing successor. It labels the
result **historical attestation** and explicitly sets
`checkpoint_replayable=false` and `observed_live_state_hash=false`. The deleted
checkpoint is no longer independently replayable; its former bytes are known
only through retained hash evidence. A current job whose own checkpoint is
missing still fails ordinary verification.

This changes storage only. Frozen network, closure, integration, input and
analysis implementations remain untouched. No retirement was executed while
implementing and auditing this helper.
