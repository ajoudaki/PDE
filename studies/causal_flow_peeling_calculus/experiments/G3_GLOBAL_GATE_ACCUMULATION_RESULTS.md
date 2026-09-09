# G3: Compact-Time Gate-Block Accumulation

## Claim level

Empirical support for stable accumulation on sampled Gaussian-reachable
states.  Iterating the same autonomous frozen-input peeling block converts
the approximately quadratic local defect from G2 into an approximately
first-order global error through time `T=0.5`, uniformly over the tested
widths.  This is not a convergence or stability theorem.

## Runs

- widths `128,256,512,1024`, four seeds each;
- pure arctangent and `0.2*z+atan(z)`;
- meshes `0.02,0.01,0.005`;
- checkpoints `0.25,0.5`;
- coupled dense RK4 reference with step `2^-11`;
- selected width-512 pure-arctangent reference repeated at `2^-12`.

All steps preserve the original persistent matrices and their transposes.
No clipping is used.  A shorter final block hits each checkpoint exactly.
Artifacts are in:

- `outputs/g3_global_gate_accumulation_low/`;
- `outputs/g3_global_gate_accumulation_high/`;
- `outputs/g3_global_gate_accumulation_refined/`.

## Results

For pure arctangent, the median log--log slopes across all widths were:

| quantity | slope range |
|---|---:|
| bottom coordinate `u` | `0.987--0.990` |
| hidden response `r_2` | `0.983--0.985` |
| raw kernel | `0.980--0.981` |
| learned `G_1` Frobenius error | `0.956--0.987` in float32 |

The slight learned-matrix slope loss grows with width and reference
refinement while the physical fields and observables are unchanged; it is
consistent with accumulated float32 dense-matrix roundoff already diagnosed
by the G2 float64 control.

The error constants were also stable.  At `T=0.5`, the median pure-arctangent
`u_error/h` ranged from about `0.058` to `0.064` across widths, while
`kernel_error/h` ranged from about `0.206` to `0.234`.  No monotone width
inflation appeared.  The positive-slope activation had larger constants but
the same approximately first-order convergence.

The doubled-reference-resolution run reproduced the state, response, and
kernel slopes and constants.

## Interpretation

G3 passes its preregistered empirical compatibility gate.  Together, G2 and
G3 say:

1. the exact paired-edge block has an `O(h^2)`-compatible local defect on the
   sampled reachable ensemble;
2. those defects accumulate like `O(h)` rather than being visibly amplified
   by rare transverse directions through width `1024`;
3. pure arctangent does not require a leaky component for this numerical
   behavior.

This evidence directly rejects neither deterministic no-go.  The adversarial
states in those constructions choose rare coordinates and transverse
directions coherently; the numerical defects are causal functions of diffuse
Gaussian sources.  The proof obligation is therefore a uniform **annealed
reachable-cone** estimate, not operator-norm stability over arbitrary energy
balls.

The experiment does not establish width convergence, an adaptive tail,
forest summability, or autonomy of a limiting character.  Its strategic role
is to justify investing in a chronological cavity/tangent calculus rather
than modifying the activation or architecture solely to repair deterministic
Lipschitz bounds.
