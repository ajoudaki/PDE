# Independent audit of the moderate-sine physical-energy route

2026-09-08. Audited Sections 2--6 of `/tmp/sine_physical_route.md` directly from the exact raw model and displayed bounds. No previous or sibling review verdict was used as a premise. No source file was edited and no experiment was run.

**Verdict: PASS for the stated finite-width energy/stability, weak path-law tightness, gradient-continuity and strong-endpoint results. No blocking mathematical defect found.** These results do not prove continuation from the population endpoint or the unconditional global population/GF/GD limit.

## 1. Primal and raw vector-field estimates

The field table is correct under `|Phi(z)|<=2|z|` and `|Phi'|<=2`. In particular,

`||h1||<=2B`, `||h2||<=4B^2`, `||h3||<=8B^3`,

and the backward sequence is `2B, 2B^2, 4B^2, 4B^3, 8B^3`.

The prediction magnitude is at most `8B^4`, so the sum of the two residual magnitudes is at most `16B^4+2<=18B^4`. Each raw parameter block has norm at most `144B^7`. The stated total bound `576B^7` is conservative because the raw product norm is at most the sum of its four block norms.

The first-layer normalization was checked explicitly:

`sqrt(d/n) ||d^{-1} u x^T||_F = ||u||_n`

when `||x||^2=d`. The middle rank-one normalization is also correct:

`||u h^T/n||_F=||u||_n ||h||_n`.

No width or dimension factor has been lost in these estimates.

## 2. The explicit finite-width Lipschitz constant

The forward differences in (5) follow by placing one parameter difference in each exact product. The sample prediction difference is at most `32B^3 d0`, giving the stated two-residual sum `64B^3 d0`.

The backward differences in (6) were checked independently:

- Top gate: `2 d0 +24 sqrt(n)B^3 d0 <=26 sqrt(n)B^3 d0`.
- Middle incoming: `2B d0+26 sqrt(n)B^4 d0 <=28 sqrt(n)B^4 d0`.
- Middle gate: `56 sqrt(n)B^4 d0+16 sqrt(n)B^3 d0 <=72 sqrt(n)B^4 d0`.
- Bottom incoming: `4B^2 d0+72 sqrt(n)B^5 d0 <=76 sqrt(n)B^5 d0`.
- Bottom gate: `152 sqrt(n)B^5 d0+8 sqrt(n)B^3 d0 <=160 sqrt(n)B^5 d0`.

These retain the necessary `sqrt(n)` from the coordinate maximum. Expanding residuals and rank-one factors gives the displayed block constants:

- first block: `512+2880=3392`;
- second block: `512+2592+144=3248`;
- third block: `512+1872+288=2672`;
- readout block: `512+432=944`.

Their sum is `10256`, below the claimed conservative coefficient `11000`. Every omitted smaller power is dominated by `sqrt(n) B^9`, since n>=1 and B>=1. The primal set is convex, being the intersection of operator-norm balls and norms of linear parameter images. Thus the same bound is valid throughout each Euler segment contained in that set.

This is a finite-dimensional estimate. The note correctly does not infer a population Lipschitz bound from it.

## 3. Raw GD at the prescribed step

The stopping argument is valid with the stated slack. Before raw displacement R, all primal quantities are at most `b0+R=B-1`. The condition `576B^7 n^{-2}<=1` puts the next candidate Euler segment inside the larger primal ball B even before proving that its endpoint remains inside the raw stopping radius.

The gradient Lipschitz condition needed by the descent lemma is

`h L_n <=1`, where `h=n^{-2}` and `L_n=11000 sqrt(n)B^9`.

This is exactly the first inequality of (8). The resulting one-step decrease is at least `h||V||_raw^2/2`. Summing and applying Cauchy--Schwarz to the raw increments gives

`sum_{j<k} h||V_j||_raw^2 <=2E0`

and

`||Theta_k-Theta_0||_raw <=sqrt(2kh E0)`.

For the endpoints needed to cover the fixed observation interval, `kh<=T+1`, and this is strictly below R. The argument therefore closes its own stopping condition. It does not need a population path or an uncut finite-width GF comparison.

The random-initialization specialization is also valid: a deterministic choice `b0=10`, `E0<=2` holds on events whose probability tends to one, and it makes the two width conditions eventually deterministic for each fixed T. The theorem is finite-horizon eventual-in-width stability of raw GD, not a fixed-step all-time convergence assertion.

## 4. Finite GF and weak path tightness

At fixed width, the true gradient energy bound prevents escape in the finite-dimensional raw norm. Norm equivalence at that fixed width and ordinary local ODE existence give global finite GF.

The forward velocity inequalities (11) have the same constants as their difference counterparts. They remain valid almost everywhere for the raw piecewise-linear GD interpolation when hidden fields are recomputed, as required by the original contract. Combining them with the GF or GD energy bound supplies a deterministic bound, on the stated high-probability events, on the empirical mean squared H1 norm of the joint same-layer four-coordinate paths. The time-L2 part of the H1 norm follows from the initialized second moment and the integrated derivative bound.

Bounded H1 balls have compact images in C on the finite interval: their members have uniformly bounded pointwise values and the common square-root time modulus. Closedness of the image can be checked by weak H1 compactness after taking a uniformly convergent subsequence. Markov's inequality then bounds the empirical mass outside these compact path sets. This establishes the claimed weak tightness.

The distinction from Wasserstein compactness is essential and correct. A bounded empirical second moment of the H1 norm does not imply uniform integrability of squared path norms; the same argument does not identify limiting kernels, adjoints, or velocity laws.

## 5. Raw gradient continuity and scalar Frechet differentiability

For strongly convergent L2 pairs `(z_j,q_j)`, the product decomposition in (12) is valid. The fixed-q term tends to zero because bounded continuous functions of `z_j` converge in measure, and their products with the fixed integrable `q^2` are uniformly dominated. Passing to almost-everywhere subsubsequences proves convergence of the whole sequence. Recursing backward and using continuity of rank-one L2 products gives continuity of the complete raw gradient.

The scalar Frechet derivative proof also checks. The Taylor remainder bound

`|Phi(z+u)-Phi(z)-Phi'(z)u|<=min(|u|^2,4|u|)`

follows from the first two derivative bounds. Splitting its pairing with any fixed L2 adjoint q at `|q|>K` gives a quadratic bounded-part term and an arbitrarily small linear tail term.

To spell out why this scalar argument survives the composition: expand the top prediction first. Its activation remainder is paired with the fixed current readout. The top preactivation difference is

`Delta W3 h2 + W3 Delta h2 + Delta W3 Delta h2`.

The last term contributes only a quadratic remainder. Move the fixed top adjoint through W3 and apply the same scalar activation remainder argument at the middle layer; then repeat at the bottom. Forward differences are O(raw distance), so each scalar remainder is o(raw distance). Perturbations of the readout paired with feature differences are quadratic. This yields the claimed Frechet derivative without asserting that the activation Nemytskii map is Frechet differentiable from L2 to L2. Its gradient is continuous by the previously established product argument.

## 6. Strong endpoint, and precisely what it does not provide

For any already constructed strong physical population solution before a finite endpoint, the true energy identity follows from the scalar C1 chain rule. Equation (14) makes the full raw state Cauchy as the endpoint is approached. Completeness of the first-field/HS-increment/readout Hilbert product supplies an actual raw endpoint.

Gradient continuity then gives convergence of the raw velocity. Forward and backward continuity give all the claimed field limits. HS convergence controls operator norm, so both orientations of the actions converge on every converging L2 probe. Integrating the convergent velocities proves the stated left derivative at the endpoint.

Each extended incoming-field path has compact image in L2. The finite-net tail proof in (15) is valid: for `||q-f||_2<=eta`, split the q-tail according to `|f|>R/2` to obtain the displayed bound by `2eta` plus a fixed-reference tail. Thus the result gives qualitative uniform square-tail integrability of that single already-constructed path, including its endpoint.

It does not give a quantitative tail rate uniform over the cap approximants. It also does not prove existence beyond the endpoint. A continuous vector field on an infinite-dimensional Hilbert space does not acquire an applicable local existence or uniqueness theorem from this argument. The note correctly distinguishes a strong endpoint from a continuation theorem and retains the requirement that Gaussian source histories not be reset.

## 7. Exact accepted scope

The independently checked conclusions are:

1. The displayed finite-width raw Lipschitz bound with constant `11000 sqrt(n)B^9`.
2. Unconditional finite-horizon loss descent, displacement and raw-energy bounds for simultaneous raw GD with step `n^{-2}`, for sufficiently large width under the explicit conditions.
3. Global finite-width GF and weak same-layer path-law tightness for both finite algorithms.
4. Continuity of the population raw gradient, scalar C1 loss regularity, and a strong endpoint with convergent velocity for any population physical solution already constructed up to a finite time.

No unconditional global strong population construction, reached-state continuation existence, full-sequence population identification, path-W2 convergence, or joint observable theorem is established by these results alone.
