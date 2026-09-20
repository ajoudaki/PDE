# Internal check of rate composition

Verdict: PASS for the requested component composition and final index shift.
This is an internal check, not a promotion review. The reviewer authored the
dynamics component; the separate dictionary component received the complete
independent check recorded in `DICTIONARY_INTERNAL_CHECK.md`.

Final checked assembly: `RESULT.md`, SHA256
`0ec5197dc1a92d16226ffefc0c1df0bae00405a674b38f6db03a51b3810fa43a`.
The full initial assembly was read; subsequent changes to the heading,
auxiliary-symbol names, and integer wording were checked against the same
composition. The final order recipe and composition were reread at this hash.

Component hashes used:

- `ROUTE_DICTIONARY.md`:
  `c894744d37cd0e2eb5adcf2524dce26507748a23fed84b69ef8fd0645902ea1c`.
- `ROUTE_DYNAMICS.md`:
  `f84da8b5a840079a239ae8b2ffd4c12359f8abab08f27d831e0534f2ac2fa755`.

The two components use identical H3 filters, ridge, and source norm: the
forward source covers the whole circle, the reverse source is at the sole
training input, and the rank source is in feature time on `[0,6]`.
The dictionary's raw threshold gives
`N>=N_k => rho_N<=13*2^(-k)`. Therefore
`N>=N_(k+4) => rho_N<=2^(-k)` since `13/16<1`.

For the dynamics constant, `121*255/5093<7` and `exp(30558)>=1` give

    C_* < 72186*13*exp(30558)
        < 2^20 * 4^30558
        = 2^61136 < 2^62000.

Thus `P_j=N_(j+62004)` implies
`rho_N<=2^(-(j+62000))<1/100` for every `N>=P_j`, activating the endpoint
and all-physical-time comparison. Its error is at most
`C_*rho_N<2^(-j)`, uniformly on the circle at identical physical times.
Both endpoint predictions obey the same bound. Larger-order validity uses
retained-word inclusion and the ridge bound, not monotonicity of actual errors.

The assembly explicitly treats Gaussian-moment roundings as existential
finite proof-witness choices. Their uniform bounds determine `N_k`, so neither
their values nor a certified quadrature algorithm is required for order
selection. This matches the qualified PASS in the dictionary check and does
not assert a numerical coefficient-integration rate.

One literal objection was raised to assembly hash
`bd3b2e20eef29fc771e8ad8d9913215081f936e28d91d5b524f7dc0b9fbd1e10`:
the sentence “All numbers in this recipe are integers” incorrectly included
`lambda=2^(-(k+400000))`. The final checked version states that lambda is a
positive dyadic rational and all remaining displayed quantities are integers.
The correction changes neither the recipe nor any estimate. No outstanding
composition correction remains.
