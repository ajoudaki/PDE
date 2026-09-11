# P1 standalone validation evidence

Coordinator `/root`, 2026-09-11. This records deterministic assembly and exact
arithmetic checks, not a mathematical review verdict. The maintained edition
was not modified. No training experiment, parameter sweep or finite-width
simulation was run.

The exact frozen manifest is `P1_MANIFEST.json`, SHA256
`3dc31cc04695cb3fd48741cbfcea8575a746f3182132e93c0ac609cd5ec6e089`.
Every file in its inputs mapping was copied, without author components or
study history, to `data/generated/robust_learning_horizon/promotion_validation_02/frozen_inputs/`.
Only these copied inputs were used for the standalone check. Working directory
was `/home/amir/Codes/PDE`; runtime was Python 3.10.12, using its standard
library only. All numerical certificate inequalities use exact integers and
rational numbers; displayed decimal Gaussian enclosures are outward rounded.

Executed command, exit status 0:

```text
python data/generated/robust_learning_horizon/promotion_validation_02/frozen_inputs/validate_candidate.py --inputs data/generated/robust_learning_horizon/promotion_validation_02/frozen_inputs --output data/generated/robust_learning_horizon/promotion_validation_02/edition
```

The validator reconstructed the proposed global chapter from the full baseline,
five exact scope replacements and the complete 1,633-line addition. It checked
the two guide replacements, preservation of the old complement, all declared
input hashes, all eight complete dependency excerpt hashes, simple mathematical
markup balance, absence of study/history path dependencies in the addition,
and byte correspondence of the embedded rational Gaussian certificate. It
assembled the edition and dependencies in the new output directory, then ran
both certificate scripts there. Both exited 0 with empty stderr.

Observed reference certificate output:

```text
[0.392108947877, 0.396376711612, 0.233120735618, 0.339792209687, 0.631761866359]
```

These are the outward lower/upper bounds for q and the three lower bounds
used in the activity proof. The script also asserts the fitting, tail and
endpoint inequalities. The transfer certificate reported PASS, with transport
coefficient before rounding `661180`, loss Lipschitz bound `44928`, raw speed
`4082`, response exponent `2880`, response prefactor `225400`, `T=40`,
`t_act=1/200`, cutoff `exp(2900)`, radius `exp(-exp(3000))`, state tolerance
`1e-18`, and squared activity margin `1e-13`.

Output record and stdout hashes (paths relative to the edition output):

| File | SHA256 |
|---|---|
| validation.json | 654b725eaa8ab9c96472fe5178298de51f708f5c5ea3361ecac24315bc44b16f |
| P1_CERTIFY_REFERENCE.py.stdout | ad40e8d8f73fed6d22cc9b68a19f7f9e6c3f2f59383d581e372ce0c976786900 |
| P1_CERTIFY_TRANSFER.py.stdout | 97089ac3bf0eebb7a3b7058c4bc1e2e64c6f6af6321af84ff86569d9d0806df5 |
| Both stderr files (empty) | e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 |

The assembled chapter hash is
`d473d95ee27bc39d484185cea2689b5d3ceed448567a1527488f1003e24f1fa1`;
the assembled guide hash is
`7824df11fe7fa2d89cf2c75dc32716438b20c815a18d1c3809a84a0785d9d34e`.
The record also contains every assembled dependency-file hash and executed
certificate command. `promotion_validation_01/` retains a successful earlier
run made before the assignment and validator were included in the manifest;
it is not the final-manifest validation evidence. `author_validation_01/`
retains the independent author rerun of both component scripts.

Limitations: simple markup balance is not a rendering test or complete link
checker. Exact arithmetic certifies the programmed inequalities, not all
proof implications. This is not a formal proof-assistant check, a whole-book
audit, an empirical reproduction, or a quantitative finite-width estimate.
The complete new scientific argument and its notation/interfaces are assigned
to separate fresh scientific and integration reviewers. Their reports and
completion evidence must be read before acceptance.
