# Execution note

Before the authoritative frozen manifest existed, a preliminary validation
manifest was created and then invalidated by the final analyzer/protocol
state. It is preserved as `ABORTED_PRE_FREEZE_MANIFEST.json` and excluded
from evidence.

During the PDE stage, concurrent orchestration correctly stopped when one
worker observed another worker's active `.partial` archive. All already
started jobs completed cleanly. The remaining frozen jobs were resumed
serially with identical commands and settings. No trajectory was selected,
edited, rerun under a changed configuration, or omitted. The final exact
11-file PDE inventory and exact 9-file dense inventory were independently
validated and cryptographically sealed before analysis.
