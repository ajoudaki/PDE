# Evidence ledger

| ID | Claim | Status | Exact scope / failure mode |
|---|---|---|---|
| E1 | The exact coefficient `[h^5] Delta_t` has degree at most four in `t`. | Proved | Universal autonomous Euler-word identity, provided the fifth width-first jet exists. Therefore no fixed activation can have a literal fifth Taylor coefficient growing faster than `t^5`. |
| E2 | Quadratic activation can violate a uniform shrinking-window remainder bound violently. | Proved in earlier study | It has superlinear growth and so does not decide the present conjecture. |
| E3 | Bounded output activations are natural counterexamples. | Refuted as a mechanism | On a fixed total-time window the readout increments and terminal feature are bounded; a large endpoint output cannot be generated solely by hidden-gradient blow-up. This does not itself prove the full remainder estimate near zero. |
| E4 | Globally Lipschitz, linearly growing activations obey the desired uniform bound. | Under investigation | Expected from local Euler stability, but the reused-matrix width-first OMFP norm bridge must be proved. |
| E5 | `x+lambda sin(x^3)` is a valid natural candidate. | Under investigation | Smooth, linearly growing, all fixed Gaussian derivative moments finite; its gradient map has a rare-tail squaring mechanism. Oscillatory signs and actual full-network coupling are the main lower-bound obstacles. |
| E6 | A tailored slope-ladder activation can refute the conjecture. | Under investigation | Must retain linear growth, fixed-step finiteness, and a lower bound after Gaussian averaging in the actual `L=2` dynamics. |

## Decisive outcomes

1. **Universal positive result:** an activation-defined local radius and an
   all-step OMFP stability estimate imply `C_phi(t,rho)<=C_phi t^5`.
2. **Meaningful negative result:** one fixed smooth, linearly growing,
   fixed-step-finite activation has `limsup_t C_phi(t,rho)/t^5=infty` for
   every required local radius.
3. **Boundary theorem:** prove (1) under a sharp condition such as bounded
   derivative, and prove (2) outside it.

