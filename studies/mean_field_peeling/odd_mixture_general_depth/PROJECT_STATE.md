# General-depth odd-mixture research state

Exact activation: phi_theta(z)=(1-theta)z+theta atan(z), 0<theta<=1. Three fixed inputs, strict absolute angular separation, original Gaussian initialization and raw GF/GD, separately fixed hidden depth L.

Requested global trained theorem: **UNRESOLVED**. No sufficient theta_*(delta,L) or depth-uniform theta_*(delta) has been proved or refuted. Do not mark this objective complete or promote the initialization result to a trained result.

Delivered report: REPORT.md. Its final SHA256 is `cd62425a6d8ae0ca7351bb6e71b31cd0b4eb7266263e53e377f976bab261e037`. The complete self-contained initialization proof gives sharp worst-case order delta^2 theta^2 L/(1+theta L)^2, uniformly in the stated small-delta range, every positive convex mixture and all finite depths. Part II proves an adaptive-cap continuation criterion conditional on uniform primal bounds and curvature-weighted exponential incoming reference tails. Those hypotheses remain unproved for canonical training.

Three preparatory independent routes were completed: general-depth source-response recurrence and nonlinear continuation; independent depth-uniform initialization/variance analysis; sharp joint-parameter initialization geometry. A separate isolated initialization audit validated the quantitative proof and identified contextual clarifications; the final report has a full explicit model and no outside-document endorsements.

Three fresh final reviewers (Orion, Larch, Flint) read only immutable copies of the whole report, with no inherited history or outside material. All three validated the partial/conditional results. Flint also explicitly returned FAIL on completion of the original global target. Every full review was author-read and saved; exact input and review hashes were verified. See REVIEW_SUMMARY.md and reviews/final/MANIFEST.json. No post-review change was made to REPORT.md.

The report supplies the specialized Gaussian/Hermite/secant proofs internally. A recent muP paper was screened but not invoked; LITERATURE_SCREEN.md records that limited scope check without claiming a full proof audit or an exhaustive literature result.

All source studies were preserved. No numerical experiments, publication, original-task resumption or Git commit was performed.
