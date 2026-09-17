# User clarification: keep the continuation a mild sanity check

After launch, the user clarified that this is not a question worth hours and
that visually sufficient settling is enough. This instruction supersedes the
original plan's requirement to continue until every strict threshold passes
or the two-hour ceiling is reached.

Keep the same trajectories, equations, step sizes, controls and recorded
measurements. Inspect the completed longer curves and stop by the common
T=640 stage (16 times the original horizon), or sooner if the plots already
answer the qualitative question. Do not launch a new configuration or chase
the remaining tail. Keep all original strict settling checks as diagnostics;
do not relabel a failed strict check as a pass. Report observable flattening
and remaining drift separately, with the actual achieved common horizon.

An external stop watcher may interrupt the already-running frozen supervisor
after its complete T=640 analysis appears. Any just-launched next-stage work
is cancelled and excluded; completed stages and checkpoints remain intact.
This is a user-directed reduction of scope, not a numerical failure or an
outcome-driven retry. No simulation producer is edited during the campaign.
