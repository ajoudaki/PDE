# Frozen successor 01: canonical pilot horizon repair

Status: **frozen before any successor trajectory**.  This is a separately
named successor to the closed Stage-2 run in `PROTOCOL.md`; it does not amend,
overwrite, or reclassify that run.

The predecessor stopped after 7.623125169426203 seconds because its first
physical point used `max_time=0.012`, which could not reach the frozen
$y=.99$ node.  No NPZ or quantitative trajectory value was written.  The only
exposed scientific bit was $T_n(.99)>.012$.

This failure was predictable without neural data.  From the accepted
one-moment upper kernel

$$
K_U(y)=111+\frac{280864}{4107}y^2,
$$

the conjectured hierarchy itself gives

$$
T(.99)\ge T_U(.99)=0.0149394803\ldots>0.012.
$$

The NTK lower kernel gives the pre-existing worst proxy hitting time

$$
T_{\rm NTK}(.99)=0.02074400985\ldots.
$$

Therefore this successor changes **only** every physical `max_time` from
`0.012` to `0.024`, a value frozen from the old proxy envelope with margin.
It retains the exact hypotheses, output nodes, seeds, widths, pair counts,
integrator, steps, metrics, validity gates, classifications, per-point wall
and memory caps, and all later branch rules in `PROTOCOL.md`.  Step-count caps
are raised only arithmetically to accommodate the longer declared horizon.

The predecessor's 7.623125169426203 seconds are charged to the frozen
one-GPU-device-hour Stage-2 budget.  This successor has a 2,400-second global
wall cap and the original 600-second cap per point, so the combined worst case
remains below one GPU-device-hour.  There is one attempt only.  Failure to
reach any node, any numerical/resource failure, or any validity-gate failure
closes all neural branches without another successor or repair.

The predecessor config, unlock, summary, and manifest remain immutable.  The
successor uses `configs/FROZEN_SUCCESSOR_01.json`, a distinct run directory,
and a hash-bound successor unlock.  The accepted exact-boundary result is
unchanged.
