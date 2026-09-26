# User-directed comparison by nearest archived dictionary size

After the base training grid completed, the user requested live comparisons
against the old result with the most similar number of vectors, rather than
the same order label. This changes reporting, not tasks, training, numerical
gates or selection of attempted trajectories. Preserve the frozen protocol,
manifest and all raw runs. The first provisional updates compared equal p;
the following mapping supersedes that framing for updates and main summaries.

Use nearest available absolute difference in total vectors K1+K2, among the
common archived orders p1,p3,p5:

| New order | New vectors | Archived order | Archived vectors |
|---|---:|---|---:|
| p1 | 6 | p1 | 8 |
| p3 | 18 | p1 | 8 |
| p5 | 38 | p3 | 45 |

Apply this same mapping separately to old closure, Gaussian and orthogonal.
Do not choose whichever random family or order gives a favorable score.
The n2048 suite has no old p2 (21-vector) trajectories. Thus the 18-vector
comparison has a substantial residual size difference, which must be visible.
Plots continue to show all actual archived sizes8,45,149 and new6,18,38,
so users can also inspect the other endpoints directly. Retain each point's
own numerical-validity flag. Main38-vector table now uses archived45-vector
models, not149-vector models. Equal-p results remain reproducible from the
complete metric table but are not described as equal-size comparisons.

The first3-case analysis produced before this reporting change retains its
original comparisons.json. Its metric/audit results remain valid; final
report comparisons are regenerated from those same metrics with this mapping.
No asymptotic rate or parameter-exact matching claim follows.
