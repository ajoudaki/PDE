# Identity activation: exact jets through order eleven

> **Endpoint update:** the order-eleven values below remain valid, but the
> accepted jet now extends through order thirteen.  See `ORDER13_RESULTS.md`.
>
> **Positive-time/depth update:** the fixed-order values also remain valid,
> but the identity model now has a rooted-path autonomous mean-field closure
> at every fixed hidden depth.  See
> `arbitrary_depth_autonomous_mse_closure/CANONICAL_NOTE.md` for its corrected
> claim boundary.  At exactly three hidden layers, a separate cyclic
> construction proves compact-time finite-width identification; see
> `depth3_unfrozen_readout_closure/THEOREM_AND_PROOF.md`.

For the frozen one-input, equal-width feature-ascent models in `PROTOCOL.md`,
the exact width-first derivatives are

| derivative order \(r\) | two hidden layers \(F_2^{(r)}(0)\) | three hidden layers \(F_3^{(r)}(0)\) |
|---:|---:|---:|
| 0 | 0 | 0 |
| 1 | 3 | 4 |
| 2 | 0 | 0 |
| 3 | 48 | 160 |
| 4 | 0 | 0 |
| 5 | 1,464 | 13,888 |
| 6 | 0 | 0 |
| 7 | 76,800 | 2,222,592 |
| 8 | 0 | 0 |
| 9 | 6,193,152 | 571,082,752 |
| 10 | 0 | 0 |
| 11 | 708,341,760 | 214,935,699,456 |

## Validation

- Ordinary-Taylor and derivative-normalized exact assemblers agree at all
  orders through eleven for both depths.
- The pre-existing independent path/Wick enumerator was replayed and exactly
  reproduced `(3,48,1464)` at depth two and `(4,160,13888)` at depth three.
- The exploratory independent depth-two order-seven value `76800` is also
  reproduced.
- Every even derivative is zero by centered-Gaussian parity, and every
  nonzero output is an integer.
- In the decisive run, each exact route took under `0.06` seconds.  The
  identity-specific linear-Gaussian recurrence therefore stayed far inside
  the frozen two-minute and 1-GiB bound.

These tables are fixed-order, width-first coefficient calculations and do
not by themselves assert a positive-time trajectory, an all-order sign law,
or a convergence radius.  A separate rooted-path construction supplies an
exact autonomous deterministic equation at every fixed depth.  Its
positive-time finite-width identification is proved at hidden depths one and
two and remains conditional at depth three and beyond; see the corrected
claim boundary in `arbitrary_depth_autonomous_mse_closure/CANONICAL_NOTE.md`.
The separate cyclic construction closes that bridge at exactly depth three;
it does not prove the rooted-path bridge at every greater depth.
