# Frozen Stage-C projection rule

This rule was frozen before any final-source order-seven pilot completed and
before any order-seven coefficient was inspected.  It supplements, and does
not weaken, `PROTOCOL.md`.

## Immutable implementation

- Sector source: `stage_c_sector.cpp`
- Source SHA-256:
  `f1912e81b2f25bdef04bcef9c490a0975757a64deda4cb55f74c7c50abfe64ce`
- Reproducible compile command:
  `g++ -std=c++20 -O3 -DNDEBUG stage_c_sector.cpp -o stage_c_sector`
- Binary SHA-256:
  `59d949b0808d92b946ec55a856764f43ed4ccbcc922c5849561c9ba73e175fbf`

The accepted Stage-A/B source remains the separate immutable
`b3_connected.cpp` with SHA-256
`5dd93cbc8fb97479e6c54dbc2202bfec42d0156014f5d34b4d40e77da9d6621f`.
No Stage-C change is permitted in that file.

## Mandatory lower-order gate

Before authorization, the sum of order-five W-hit sectors $0,\ldots,5$ from
the sector compiler must agree coefficient-for-coefficient with the frozen
dense order-five polynomial.  The independent dense raw artifact is
`frozen/stage_b_connected_order5.json`.  The internal two-colour
specialization must also reproduce the Campaign-2 equal-label polynomial
through order five after division by $2^{k+1}$.

## Pilot sample and caps

The fresh pilot sample is fixed to W-hit sectors $0$, $3$, and $7$:

- sector $0$ probes the no-splitting, terminal-contraction-heavy extreme;
- sector $7$ probes the maximal bridge-splitting/convolution extreme;
- sector $3$ probes the interior branching regime expected to have the
  largest mixture of rewrite types.

Each pilot uses the immutable hashes above and the command

```text
/usr/bin/time -v prlimit --as=4294967296 -- stage_c_sector 7 --w-hits S
```

for $S\in\{0,3,7\}$.  A pilot that reaches 1,800 seconds of wall time is
terminated; since its CPU time cannot exceed wall time, this also enforces a
conservative 1,800 CPU-second pilot cutoff.  Any failed, killed, or timed-out
pilot debits its measured CPU consumption and makes Stage C unauthorized.

## Projection and authorization rule

Let $c_S$ and $m_S$ be the measured CPU seconds and peak resident bytes for
pilot sector $S$.  Define

$$
C_{\rm pilot}=c_0+c_3+c_7,
\qquad
C_{\rm projected}=8\max(c_0,c_3,c_7).
$$

Stage C is authorized only if all of the following hold:

1. all three pilots exit successfully under the final hashes;
2. the order-five sector-sum and two-colour gates pass exactly;
3. $m_S<4$ GiB for every pilot;
4. $C_{\rm pilot}+C_{\rm projected}\le 21{,}600$ CPU seconds.

The three pilots are projection work, not reusable production checkpoints.
Their entire CPU cost is permanently debited from the six-CPU-hour campaign
budget.  Thus the production runner receives only

$$
21{,}600-C_{\rm pilot}
$$

CPU seconds for all eight fresh sectors, and must stop before launching a
sector once that remaining budget is exhausted.  The maximum-of-sample
projection is only a preregistered engineering estimate; the hard cumulative
runner cap remains the actual protection against an unexpectedly expensive
unsampled sector.

No order-seven production may begin until a hash-bound projection provenance
record supplies the three completed measurements and evaluates this rule.

