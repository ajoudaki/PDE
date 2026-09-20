# Internal check of the order-rate and action-depth arguments

2026-09-20. Bounded independent internal mathematical check, not a promotion
review. No training, proof-file change, or Git operation was performed.
The solve-math-rigorously skill governed this check. Authors' confidence
statements and earlier reviews were not evidence.

**Verdict: PASS within the assigned scope and stated canonical dependencies.**
No mathematical objection was found to the gate improvement, its source-proof
propagation, the explicit H3 order-rate inversion, or the separate factorial
action-generation theorem. Dependency limits are recorded below.

## Inputs and coverage

SHA-256 hashes of the complete files (first six paths are study-relative):

| Input | SHA-256 |
| --- | --- |
| `TAME_GATE_RATE.md` | `b26b6974cade34a960b67336256c769708aaf0b8d082b7a0de8c2624a4a605e7` |
| `ORDER_RATE_INVERSION.md` | `f5a3815931965128f63b4c619d7579bfd5cb16fea34475b002722803fc959491` |
| `ORDER_TAIL_STRUCTURE.md` | `d52fa09837ff1db78cbf6eea5dc5a3ef6d45222835eab3ee710cdc084db584dd` |
| `ROUTE_DICTIONARY.md` | `c894744d37cd0e2eb5adcf2524dce26507748a23fed84b69ef8fd0645902ea1c` |
| `ROUTE_DYNAMICS.md` | `f84da8b5a840079a239ae8b2ffd4c12359f8abab08f27d831e0534f2ac2fa755` |
| `RESULT.md` | `0ec5197dc1a92d16226ffefc0c1df0bae00405a674b38f6db03a51b3810fa43a` |
| `docs/NOTATION.md` | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |
| `docs/global_nonlinear.md` | `81d969a531fc6daee26dbee2041fad8a3425a4b01580351387c5fc376cef412c` |
| `/etc/codex/skills/solve-math-rigorously/SKILL.md` | `9be5cb903f8957c5da9e2acfb1302eba4ba45e3ef9d45e30b9740ad7dbc8cff7` |

All six study files and the notation contract were read completely.
`ORDER_RATE_INVERSION.md` was initially read at hash
`4bd8759747f7f8b3458c2093b3adb89629cc576219b3be6332d65aa84a90db33`;
the author subsequently corrected three `{cal E}` tokens to `\mathcal E`.
Those three replacements and the final hash above were checked; all other
study input hashes remained unchanged.

Maintained lines 13161–13360 were read for C.4.7.10.B grammar, counts, source
conventions, ridge and lifted equations. An erroneous initial section range
also displayed lines 12600–12960 in part A; this out-of-scope exposure is
disclosed and was not used as an additional scientific input. No README,
other study, prior reviewer report, chat or Git history was read. The optional
`validate_order_rates.py` was not used; a short independent Fraction calculation
checked the scalar constants without constructing giant integers.

## Gate and source construction

For `a(v)=cosh²(F^{-1}(v))`, `a'=2 tanh(F^{-1}(v))` implies
`cosh²g<=cosh²J+2|V|`, hence `0<J_g<=1+2|V|` globally. On the clock box,
the clamped coordinate map gives Lipschitz constant `12R²`; the sum of three
binomial fluctuations gives Bernstein error `36R²/sqrt(n)`. The proposed
`n=2^84 lambda^-6` makes this `36 lambda/1024<lambda/16`. The exceptional-set
bound uses only individual second moments; rationalization and the global
output envelope follow from positive Bernstein weights summing to one.

The complete supplied dependency chain was checked: rational Euler witnesses,
field bounds, local defects, fourth-moment induction, saturation, literal
codes, retained-feature ridge estimate, and the three source defects. Later
steps use only the compiler error, envelope, node count and coefficient bound;
none separately needs its discarded exponential derivative estimate. Thus
`rho_N(6)<=13*2^(-k)` persists with the smaller compiler degree.

Within the stated initialized-source rule, the moment induction correctly
bounds at most `W` response terms using bounded operands and first frozen
source derivatives; the centered Gaussian contribution has L4 norm at most
twice the operand L2 norm. The saturation therefore uses a genuine fourth
moment, not an unsupported L2-tail rate. No trained-query independence,
future-trajectory coefficients, or replacement of the literal prefix is used.

## Recurrences, constants and actual order

With `e_r=log2 E_r`, `log2 Acoef=3n+3L+26<=W`, `e_0<=W`, and `W>=8`,

```
2e_r <= e_(r+1) <= 2e_r+2W+6,
2^W <= e_W <= 4W 2^W.
```

Since `E_W>=Acoef`, `Afinal=Rb` and `log2 Rb<=9W2^W`. For `m_r=log2 M_r`,

```
4e_W <= m_0 <= 18W2^W+6,   2m_r <= m_(r+1) <= 2m_r+8.
```

There are exactly `4W` code updates and `N_k=M_(4W)`, giving
`4*2^(5W)<=log2 N_k<=20W2^(5W)` and
`5W+2<=log2 log2 N_k<=5W+log2(20W)<=8W`.
The Cantor pairing and rational-index bounds agree with the maintained grammar;
DAG sharing does not eliminate numeric code growth.

Independent arithmetic verifies
`100*49*4*1616=31673600<2^25`,
`25+336+40+26*400000=10400401`, and
`10400401+3+28*62004=12136516=28*433447`.
Thus `W<=2^(28k+10400401)` and the stated floor inversion proves
`E(N)<=2^433448 (log2 log2 N)^(-1/28)` at the stated triple-log threshold.
The `62004` shift gives both the small-source premise and the required error
under the supplied all-time constant. No monotonicity of actual error is used.

Also checked: `W~360000*2^10400376*2^(28k)`, `log2 log2 N~5W`, the original
compiler's `log2 n=2^(L+19)+4L+48` and four-level accuracy-index asymptotic,
the raw counts `r_1+r_2~N^4/24`, `r_1 r_2~N^6/48`, and the selected-DAG
bit estimates. Raw count need not equal functional rank or runtime cost.

## Factorial depth, metric and physical clocks

Picard iterates preserve the claimed readout-supremum, HS and displacement
bounds on the full interval. The summed vector-field coefficients are
`2SB²+2SB+S+B`, `2SB+3S+1`, `B+1`, all below the stated `L`.
Since `E_0(s)<=Ms`, integral induction gives
`E_k(s)<=ML^k s^(k+1)/(k+1)!` with no smallness condition on `LS`.

The sigma-field induction has the correct forward-then-reverse order:
`H_k` is bounded in `G1^k`, its forward query and bounded `delta_k` lie in
`G2^(k+1)`, and its reverse query lies in `G1^(k+1)`. Bochner integration
preserves the closed population and HS blocks. At `k=r-1`, all three exact
cancellations hold. Operator-defect norm four and HS-complement norm one give
exactly `(9+10SB+S)E_(r-1)`, proving the omitted-source rate itself.

The auxiliary flow uses the ordinary HS metric on its supported block;
its row/readout gradients stay in the respective subspaces. Initial training
features are preserved, so its fitting constant is exactly `m_*` at every
`r`. This differs appropriately from finite H3's coefficient Frobenius metric.
Both endpoints lie below five using the cited `m_*>1/5`. Strong monotonicity
of the exact feature prediction gives the all-time contracting clock estimate,
including clocks on opposite sides of its fitting endpoint. The passive
derivative bound then compares the systems at identical physical times.
At `S=5`, independent arithmetic gives `B=29/2`, `L=4575/2`, `M=193/8`,
`V²=21129/4`. The displayed constant contains the needed factor `S`, since
`L^(r-1)S^r=S(LS)^(r-1)`. Endpoint limits and factorial inversion are valid.

## Objections and limits

No blocking mathematical objection was found. Every auxiliary generation
retains entire sigma-fields and infinite scalar resolution; the candidates
correctly forbid substituting finite H3 order `p` for depth `r`. The finite
order rate instead uses the separate compiler-and-code argument.

The canonical Gaussian source theorem and maintained `m_*>1/5` certificate
are inherited, specifically stated dependencies; they were not reconstructed
outside the assigned boundary. This check does not certify numerical error,
practical small-order accuracy, sharpness, or all-time finite-width convergence,
and supplies no promotion approval.
