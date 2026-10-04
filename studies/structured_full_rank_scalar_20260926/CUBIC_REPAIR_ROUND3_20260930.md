# Round 3: actual feature overlap and one orthogonal response direction

Freeze the overlap candidates before their integration. Round2 bounded-Gram
feedback improves hard RMS to0.240264/0.252676 and smooth cluster to0.010079,
passing the mechanism gate but not practical repair. It overestimates hidden
feature norm and underestimates dense readout energy on both difficult cases.
The bounded Gram transport uses A=K K0^-1 to infer an initial/current feature
overlap; a Gram alone does not determine this overlap. Retaining it explicitly
is a compact additional feedback channel, not a new population representation.

## Frozen candidate O

Let initial readout basis have Gram G (initially just the m training features),
and let R's columns represent current training features in that basis. Keep
R in R^(p×m) and readout coefficients v in R^p, initially R=[I;0],v=0.
Initially p=m; the optional additional response mode below has p=m+1.
Use the initial response tensor S[(a,e),(c,f)] with e,f ranging over p
readout basis functions and a,c over the m training inputs. It is PSD as a
paired-index Gram, computed from initial hidden-parameter gradients only.

    K = R.T G R; f = R.T G v; r=f-y;
    g_a = (1-K_aa)/(1-K0_aa);
    T_ea = -alpha*g_a*sum_cf r_c*g_c*v_f*S[(a,e),(c,f)];
    R' = solve(G,T); v' = -alpha*R*r; alpha=2/m.

No Gram-to-overlap substitution is made. The exact internal identities are
f'=-alpha*(K+N)*r with N_ac=g_a*g_c*sum_ef v_e v_f S[(a,e),(c,f)] PSD,
and q'= -2alpha*r.f for q=v.T G v. Each K_aa derivative has factor1-K_aa.
These assertions require independent algebra checks before training.

For query x, initial kx contains its inner products with the p readout basis
functions. Set b0=solve(G,kx), d0=K0xx-kx.solve(G,kx). Evolve only b in R^p:

    kappa_x=d0+b.T G b;
    g_x=(1-kappa_x)/(1-K0xx);
    Tx_e=-alpha*g_x*sum_cf r_c*g_c*v_f*S[(x,e),(c,f)];
    b'=solve(G,Tx); f_x=b.T G v.

For common initial contractions d0>=0; the feature bound and Cauchy-Schwarz
give |f_x|²<=q. Training aliases coincide with R columns. Query state cost
is p scalars EACH, not a fixed-size full-function decoder. This projected
readout model omits orthogonal readout motion. The p=m ungated ablation
(allg=1) matches the direct bilinear model's projected feature dynamics.

Run O gated and ungated on the three focus tasks. The fixed denominator is
initial average tanh gate; it is not a fitted damping constant. The gate
factorization itself is an approximation and does not follow exactly from
the dense nonlinear moment hierarchy.

## Frozen candidate O+1 (conditional coefficient completion)

The independent minimal-mode route constructs one normalized response
direction orthogonal to the m initial training features, from the terminal
cubic readout under the known linearized initial-kernel residual dynamics.
Its exact formulas must be frozen in CUBIC_MINIMAL_MODE_ROUTE_20260930.md
and independently checked before running this branch. No dense trajectory
or fitted output chooses the mode. Use those extended initialization
contractions in O, with p=m+1. Run the same gated/ungated pair to distinguish
readout enrichment from saturation. Training state is then (m+1)².

These four candidates are the final predeclared development round. All
focus/transfer/numerical gates and per-run budgets remain unchanged. A
transfer branch is permitted for a method passing the original factor3
mechanism gate on both hard cases without smooth-case regression>.02;
passing that gate is not achieving the0.05 practical target. No parameter
sweep or selection of a mode from dense test errors is allowed. Distinguish
state savings, static initialization cost, and per-query evolving state.

Products: cubic_feedback_repair_20260930/round3/ and explicitly named
transfer/check subdirectories. Preserve all earlier adverse results.
