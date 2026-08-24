# Evidence ledger: depth-three arctangent operator IDE

> Historical 21 August snapshot.  Superseded by the authoritative
> [CORE_EVIDENCE_LEDGER_2026-08-23.md](CORE_EVIDENCE_LEDGER_2026-08-23.md).

Status: contract frozen; all isolated proof-search and hostile-audit rounds
reconciled, 21 August 2026.

| ID | Claim | Rung | Status | Decisive dependency or falsifier |
|---|---|---|---|---|
| E1 | The displayed forward/backward equations are the exact mixed-metric feature gradient | C0 | proved independently and checked numerically at widths 3, 7, 19 | Block differentiation plus `test_finite_identities.py` |
| E2 | The feature derivative is the sum of the four squared block-gradient norms | C0 | proved and central-difference checked | Same finite check |
| E3 | Two static Gaussian actions plus two current trace-class perturbations algebraically retain all weight memory | C1--C2 | proved at the exact algebraic level | Joint two-matrix pointed-action source construction must be written cleanly |
| E4 | The obvious bare \(L^2\) vector field is locally Lipschitz | C3 | falsified | Multiplication by the unbounded middle adjoint is not locally Lipschitz on \(L^2\) balls |
| E5 | A fixed stronger or lifted state makes the IDE well posed without adding history | C3 | conditional | \(\psi_1\) control of the middle static-adjoint query gives an Osgood modulus; invariance is open |
| E6 | Fixed Euler meshes are finite two-matrix transpose programs | C4 | proved | Eliminate both trained matrices into finite sums of normalized rank-one actions |
| E7 | Continuous \(B_2,Q_1\) have square-tail tightness uniformly in width | C5 | open, sharply reduced | Prove a signed leave-one-column response bound, or moderate moments through \(p\asymp\log n\) |
| E8 | Canonical finite predictors, raw kernels, residuals, and losses converge on compact physical time | C6 | open | C0--C5 and scalar-clock stability |
| E9 | Dimension-free state bounds alone imply kernel equicontinuity | C5 | falsified | A bounded-norm Householder state has \(K'_n(0)\asymp-\sqrt n\) and an \(O(1)\) drop in \(O(n^{-1/2})\) time |
| E10 | The Householder instability refutes the iid-Gaussian theorem | C5 | not established | Its alignment is non-generic; canonical initial Hessian contractions are \(O_{\mathbb P}(1)\) |
| E11 | One Gaussian integration by parts closes annealed stability | C5 | falsified for the direct first-order route | The directional Malliavin equation regenerates the same diagonal multiplier without a small width factor |
| E12 | The learned part of the middle adjoint is tail-safe | C3--C5 | proved | \(q_2^*b=\int X_2(s)\langle B_3(s),b\rangle ds\) is pointwise controlled; only \(\Gamma_2^*b\) is hard |
| E13 | A finite cotangent, log-momentum, or present-Jacobian lift restores bare-\(L^2\) local Lipschitzness | C3 | falsified for these lift classes | The exact lift contains \(\kappa(s)c^2\), while \(\dot J=M_aJ+JM_b+\cdots\); finite graph norms regenerate the multiplication hierarchy |
| E14 | Ordinary weak/action or intrinsic \(L^1\) convergence is enough for the raw kernel | C5 | falsified | An action-null one-coordinate spike is invisible to bounded probes but has an order-one adjoint square; static \(G_1^*\) does not propagate \(L^1\) control |
| E15 | Fixed-mesh all-moment bounds and a compact-time \(L^2\) bound automatically yield some continuous-time \(L^{2+\varepsilon}\) bound | C3--C5 | falsified as an abstract inference | \(Y'=Z^2Y/4,\ Y(0)=(1+Z^2)^{-1}\) has every fixed-mesh moment and a finite \(L^2\) endpoint, but no \(L^{2+\varepsilon}\) endpoint moment |
| E16 | A componentwise natural/moving coordinate removes the middle multiplier while leaving uniformly bounded operators | C3--C5 | falsified for uniformly equivalent local-coordinate contracts | The unique cancellation coordinate is \(h'=C/d\); it creates \(D_2^{-1}G_1D_1^2G_1^*D_2\), whose canonical norm is \(\Omega_{\mathbb P}(\log n)\) |
| E17 | A first-response Gaussian/ZDot or absolute Malliavin/Fock norm proves the needed moderate tails | C5 | falsified for these norm classes | First response creates mixed responses of all orders; absolute derivative radius stays \(O_T(1)\), whereas \(p\asymp\log n\) needs radius \(\asymp\sqrt{\log n}\) |
| E18 | The completed route failures disprove canonical iid-Gaussian convergence | C6 | not established | Every counterexample attacks a topology or proof inference; none is a reachable canonical trajectory with nonvanishing probability |
| E19 | A moving Hilbert bundle or a scalar energy-defect formulation removes the tail obligation | C3--C5 | falsified as an unconditional inference | Parallel transport is isometric gauge trivialization back to ((z,G,b)); weak--strong defect elimination assumes the same Osgood tail class for the reference solution |

No empirical observation, route failure, or formal finite-state identity will
promote E8.  Conversely, no route-level counterexample will demote the
canonical conjecture to false without a reachable iid-Gaussian construction.
