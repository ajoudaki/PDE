# Claim ledger

## C1: requested global odd-mixture extension

- Statement: a sufficient positive mixture cutoff \(\theta_*(\delta,L)\) for the full canonical global three-input trained limit with all required GF/GD/path/velocity/kernel, uniqueness and nonaffinity claims.
- Status: **Open** in this work.
- Scope: exact odd mixture, all strictly separated realizable triples, Gaussian initialization and raw training, separately fixed depth.
- Missing bridge: a canonical trained-law regularity/continuation estimate; initialization does not provide it.
- Stronger version: one positive \(\theta_*(\delta)\) for every finite depth is also open. Neither is refuted by initialization collapse.

## C2: sharp initialized smallest eigenvalue

- Statement: for \(0<\delta\le1/4\), \(0<\theta\le1\), \(L\ge1\), \(d\ge2\), the infimum over strictly admissible triples is comparable, with universal constants, to \(\delta^2\theta^2L/(1+\theta L)^2\).
- Status: proved by the complete argument in REPORT.md; all three final reviewers validated this scope without mathematical correction.
- Dependencies: scalar Gaussian variance recursion, Hermite identities proved in the report, cubic tensor lifting, accumulated nonlinear injection and a strictly admissible clustered upper example.
- Sharpness scope: joint initialization geometry, not a sufficient trained cutoff.

## C3: depth-dependent signal scale

- Statement: \(q_L\sim1/(2\theta L)\) for fixed positive \(\theta\), and the initialized scalar nonaffinity margin in layer \(L\) is asymptotic to \(1/(12\theta L^3)\).
- Status: proved in REPORT.md.
- Consequence: a common positive absolute kernel or nonaffinity lower constant across every depth is impossible.
- Does not imply: that the admissible mixture itself must shrink with depth.

## C4: normalized initialized conditioning

- Statement: the worst normalized eigenvalue has joint order \(\delta^2\theta^2L/(1+\theta L)\), so for fixed \(\delta,\theta>0\) it remains bounded below over all finite depths.
- Status: proved in REPORT.md.
- Does not imply: trained-time preservation of that lower bound.

## C5: conditional continuation with adaptive caps

- Statement: on every fixed-depth compact horizon, common primal bounds and the displayed curvature-weighted exponential reference-tail condition imply uniform raw state/direction convergence of the caps, strong uncut existence, uniqueness against bounded-primal competitors and uniqueness from reached states.
- Status: **Exact under the additional stated assumptions**, complete proof in REPORT.md.
- New mechanism: the reference-only global gate secant has one power of the cap, independent of depth, and depends on incoming/preactivation ratios.
- Missing bridge: prove the hypotheses for the canonical references. They are not asserted to follow from raw energy, pairwise separation, or a positive initialized Gram.
- Separate missing results: finite-width trained observation/velocity limits and all-time trained nonaffinity.

## C6: affine-reference obstruction

- Statement: the equilateral triple with equal unit labels is admissible for \(\delta<1/2\), has zero feature sum for every bias-free affine network, and the zero-readout affine population is stationary at every depth.
- Status: proved in REPORT.md.
- Consequence: invalidates the uniform bounded-clock affine-reference route for all separated triples.
- Does not imply: falsity of the positive-mixture theorem, whose initialized Gram is strictly positive.

## C7: external literature screen

- Status: no advanced external theorem invoked.
- A recent arbitrary-depth μP paper was screened and not applied because its stated scope does not supply the requested all-triple raw GF/vanishing-step path-and-velocity theorem. See LITERATURE_SCREEN.md. This is not a complete audit of that paper or an exhaustive literature no-go claim.
