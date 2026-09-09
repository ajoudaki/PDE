# Independent audit of the geometry and excursion claims

2026-09-08. Reviewed `/tmp/three_geometry_sharpness_20260908.md`, SHA-256 `08768e8c190e0e428efe978fa751b35b7444d327364c7bd393a2e9af9eee2fa9`. This audit concerns the explicitly limited mathematical claims in that note. It is not an audit certificate for a complete three-input GF/population theorem.

**Verdict: PASS for the new necessary near-collinear excursion/time bounds and the raw-L2-ball Taylor counterexample. No substantive correction required.**

1. The proposed triple is admissible for `0<delta<=1/4`: `c=1-delta` lies in `[3/4,1)`, and the outer correlation `2c^2-1` lies in `[1/8,1)` and is at most c because `(2c+1)(c-1)<=0`. The vector `v=(1,-2c,1)` is exactly Gram-null. For labels `(1,-1,1)`, its target pairing is `2+2c`.

2. `phi` and `atan` have Lipschitz constant one in the relevant L2 spaces. The sample distances are exactly `sqrt(2delta)`. The three preactivation-difference bounds follow sequentially by the actual bounded action norms. Adding and subtracting `2 atan(z_0)` yields
   `||T_l||_2<=2sqrt(2delta)P_l+pi delta`.
   This step uses only L2 differences and the bounded arctangent value and is valid at an arbitrary raw state.

3. The exact Gram-null telescoping identity has coefficients `a^2BA`, `aB`, and identity. Applying its three operator bounds gives the factor `2(a^2+a+1)<=6` in front of `sqrt(2delta)BAN` and the stated bounded-value remainder. The raw distance inequalities `N<=1+R`, `||A||,||B||<=10+R`, `||C||<=R` are valid in the canonical population metric. For `U=11+R`, the resulting coefficient is at most
   `6sqrt(2)+3pi/11<10`.

4. Loss at most `3/8` means `||r||<=sqrt(3)/2`. Since `||v||<=sqrt(6)` and `c>=3/4`,
   `v^T f>=7/2-sqrt(18)/2>1`.
   Combining this strict lower bound with the upper bound proves
   `R>(10 e sqrt(delta))^(-1/4)-11`.
   The energy-based fitting-time lower bound is correctly conditional on an existing true strong GF and its energy identity. The strict-separation variant with actual angle parameter `2delta` changes only the stated factor `sqrt(2)` in the constant and has a valid range `delta<=1/8`.

5. The rare-event first-layer modification is a legitimate L2 raw parameter increment on the canonical first neuron space. Its squared raw norm is bounded by
   `delta[4+(1+1/s)^2]`, which remains finite because `s^2=delta(2-delta)`. On the modified event the arctangent combination converges to `atan(2)-pi/2`, a nonzero number. It therefore has an L2 lower bound proportional to `sqrt(delta)`. This is incompatible with a uniform `O(delta)` estimate on that bounded raw neighborhood.

6. The comparison with the initialized `O(delta)` scale is sound. Writing the initialized combination as
   `[atan(cG_1+sG_2)+atan(cG_1-sG_2)-2atan(cG_1)] + 2[atan(cG_1)-c atan(G_1)]`,
   the first bracket is bounded by `||atan''||_infty s^2 G_2^2`, whose L2 norm is `O(delta)` by the Gaussian fourth moment. The second bracket has L2 norm at most `2delta(||G_1||_2+pi/2)`. Thus the claimed initialization rate and raw-ball failure are distinguished correctly.

An optional strengthening of the last example, unnecessary for its claim, is to use an event of probability `eta delta` with a fixed arbitrarily small eta. Its raw displacement then has limiting squared norm of order eta, while the arctangent-combination lower bound remains `c sqrt(eta delta)`. Hence the failure can be placed inside every prescribed positive-radius raw neighborhood by choosing eta sufficiently small.

The note correctly keeps these necessary/algorithm-independent results separate from sufficient amplitude bounds and source/continuation statements. It does not present either example as a bad actual gradient trajectory or as a counterexample to the positive-e theorem.
