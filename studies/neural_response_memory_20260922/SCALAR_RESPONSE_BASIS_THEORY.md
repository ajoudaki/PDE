# Response-basis scalar model: mechanism and finite-time scope

2026-09-25. Scoped theoretical audit of the frozen implementation. Inputs for
this audit were only `scalar_response_basis.py`, its own algebra checker,
`SCALAR_VARIANTS_PROTOCOL.md`, and the four
`data/generated/neural_response_memory_20260922/scalar_variants01/basis_r{4,8,12,16}/result.json`
files. No other route findings or dense result file were read. No fits were
run and the engine was not changed. Required process skills: conjecture
investigation and rigorous mathematics. This is an internal derivation, not
an independent promotion review.

The engine SHA256 is
`16ec712b0726f7c23d1e4759c12a6f725fede4e0dd2f81b8f9a4d1b797dd13b4`,
matching all four result files. The protocol SHA256 is
`a5d9373bc922e9a745db6188cd472a579b674c310a02320914cc71dc8299e219`.

**Conclusion.** The model retains a changing positive semidefinite training
operator and exactly dissipates its internal training loss at every rank.
Its projected response fields need not be activations of its decoded weights.
Increasing rank reduced the observed internal/decoder disagreement, but small
internal loss alone certifies neither a fitted decoded network nor accurate
passive predictions. A common-time residual/stability theorem is available;
small residuals and width-uniform approximation remain unproved.

## 1. What is retained and what is approximated

For layer l, let Q_l be the fixed initialized feature matrix, normalized by
Q_l^T Q_l/n=I, and let P_l=Q_l Q_l^T/n. Its features use active inputs only.
The frozen feature bank consists of centered/RMS-normalized initial responses,
backward fields and response velocities, c0 additionally on layer3, their
pairwise products, and their individual cubic powers. A single SVD yields
nested ranks. All four recorded fits used zero Gaussian completion directions.
The constant is retained exactly. Passive inputs cannot alter the bases or
training equations.

The fixed cubic tensor defines

    a star_l b = Q_l^T [(Q_l a) elementwise (Q_l b)]/n.

Each product in the response/backpropagation calculation is projected
separately. This product is commutative but generally nonassociative. For
example, projecting an intermediate square before multiplying by another
field discards a possible return from the omitted subspace. Consequently the
engine is not the Galerkin projection of an entire unprojected polynomial RHS.

Initialized actions use C_l=Q_l^T W_l0 Q_prev/n and the same C_l^T for reverse
actions. Correlations within these retained subspaces are preserved without
resampling. The discarded actions (I-P_l)W_l0 Q_prev and their adjoint-side
counterparts are genuine approximation errors. Learned matrices B_l and the
response fields evolve; this is not a frozen neural tangent kernel model and
uses no P-order history approximation.

The moving coefficient state consists of dw, B2, B3, c, and three response
matrices for J inputs. Its dimension is 2r^2+(3J+3)r. Here J=5, giving
104,272,504,800 scalars. Cubic coefficient storage is O(r^3); the initialized
arrays and Q matrices are detached from the solver and retained separately
only for validation decoding. Rank16 at width16 reconstructs the full state
and is solely a control. Even rank12 is only a modest moving-state reduction:
504 versus the dense network's 560 physical parameters, with 44,192 bytes of
fixed solver coefficients. This is not evidence of a total-storage advantage.

## 2. Exact internal loss dissipation at every rank

Write h_lq for the coefficient response, e_l for the constant, and

    D_lq=e_l-h_lq star_l h_lq,   S_lq v=D_lq star_l v,
    M_l=C_l+B_l.

The cubic tensor is symmetric in all indices. Thus S_lq is a symmetric matrix:
u^T S_lq v=v^T S_lq u. For every input q, define backward coefficients

    delta3q=S_3q c,
    delta2q=S_2q M3^T delta3q,
    delta1q=S_1q M2^T delta2q.

These are also meaningful for passive q, although the engine only needs
training backward coefficients. The implemented forward velocity chain is

    h1q'=S_1q dw' U_q,
    h2q'=S_2q (B2' h1q+M2 h1q'),
    h3q'=S_3q (B3' h2q+M3 h2q').

Differentiating f_q=c^T h3q and repeatedly moving each symmetric S and each
M to the other side of the scalar pairing gives exactly

    f_q'=h3q^T c' + delta3q^T B3' h2q
                       + delta2q^T B2' h1q + delta1q^T dw' U_q.       (1)

Let p=(dw,B2,B3,c), with Frobenius inner products for matrix blocks. Let g_q
be the four blocks

    (delta1q U_q^T, delta2q h1q^T, delta3q h2q^T, h3q).

Equation (1) is f_q'=g_q dot p'. With residual r_a=f_a-y_a and M active
inputs, the engine sets p'=-(2/M) sum_a r_a g_a. Therefore, if J has active
rows g_a, its internal outputs satisfy

    f_train'=-(2/M) J J^T r,
    loss' = -(4/M^2) r^T J J^T r = -||p'||^2 <= 0,                 (2)

where loss=M^{-1}sum_a r_a^2. Neither associativity of star nor decoder
consistency is needed for this proof. J depends on changing responses and
weights, so its positive semidefinite kernel changes during training.

Equation (2) explains why fitting can remain robust while passive predictions
are inaccurate: loss decreases along the model's own response dynamics. It
does not prove that g_q is a gradient of one decoded-network potential.
It also gives ||p(t)-p(0)||<=sqrt(t*loss(0)), by integrating (2) and applying
Cauchy--Schwarz. This bounds parameter coefficients on finite intervals but
does not bound every independent response coordinate or prove global
existence of the polynomial response ODE. The vector field is locally
Lipschitz, so a unique solution exists until possible finite-time escape.

## 3. Why the validation decoder can disagree

Decoding reconstructs

    w_hat=w0+Q1 dw,
    W_hat_l=W_l0+Q_l B_l Q_prev^T/n,
    c_hat=Q3 c.

Let H_lq^dec be the ordinary tanh activations of these physical weights, and
let H_hat_lq=Q_l h_lq be the lifted internal responses. Define the consistency
defect C_lq=H_hat_lq-H_lq^dec. Its output consequence is the exact identity

    f_q^internal-f_q^decoded = <c_hat,C_3q>_n,
    |f_q^internal-f_q^decoded| <= ||c||_2 ||C_3q||_n,                (3)

where <u,v>_n=u^T v/n. At initialization C_lq=(P_l-I)H_lq(0), generally
nonzero. Subsequent projected multiplication and operator leakage create
additional defects. For example,

    C_1q'=Q1 h1q' - [1-(H_1q^dec)^2] elementwise (Q1 dw' U_q).

The first term uses projected products and its internal h1q; the second uses
the actual decoded tanh derivative. There is no identity forcing equality
at reduced rank. The higher layers additionally have initialized-operator
leakage. At full rank the projections are identities, exact consistent
initialization is retained, and the ordinary activation chain rule preserves
C_lq=0. The full-rank method is then exactly the dense response lift in changed
coordinates, before numerical integration error.

The supplied result files report the following RMS gap over all five outputs:

| Rank | Internal/decoded RMS | Decoded training RMS | Internal target time |
|---|---:|---:|---:|
| 4 | 0.114464 | 0.117150 | 8.72770 |
| 8 | 0.027084 | 0.030857 | 8.17323 |
| 12 | 0.010471 | 0.041847 | 4.35412 |
| 16 | 1.06e-9 | 0.031623 | 4.04441 |

All internal training RMS values reached sqrt(.001). Rank12's decoded network
did not reach that threshold, despite its much smaller consistency gap.
At rank4, the 90-degree internal output is -0.425966 while its decoded output
is -0.229322; changing readouts would materially change the reported outcome.
The protocol correctly requires these to remain distinct.

The rank12 internal passive outputs are closer to the full-rank control than
rank4's in the recorded terminal panel. This is consistent with improved
retention of nonlinear response directions, not a proof identifying one
error mechanism: source defects were not recorded, and the stopping times
differ. The root's dense comparisons and prescribed refinement determine
the campaign verdict. These four unrefined files alone do not establish
common-time accuracy or width generalization.

Nested spaces make initial orthogonal projection errors nonincreasing for a
fixed field. They do not make nonlinear trajectory errors monotone. Reported
operator-leakage Frobenius norms are also not monotone by necessity: enlarging
the rank enlarges the input space being tested. The relevant dynamic error
uses the leakage acting on the actual coefficient vectors, not its unweighted
Frobenius norm alone.

## 4. The finite-time theorem that is justified

Fix n, the initialization, data, query list and finite T. Let X be the exact
dense polynomial response lift, including first-weight changes, internal
weight changes, c and the response fields. Its initial responses are the
actual tanh forward pass, which ensures it stays on the activation manifold.
Let F be its exact vector field, G_r the implemented coefficient field, and
Psi_r the linear reconstruction of the corresponding fields and weight
changes. Use the state norm with empirical squared norms for neuron vectors
and first-weight changes, and Frobenius squared norms for internal weight
changes. Q_l^T Q_l/n=I makes Psi_r an isometry for the coefficient block norm.

Suppose both trajectories exist through T and their connecting segments lie
in a bounded region where ||F(x)-F(y)||<=Lambda||x-y||. Such a finite Lambda
exists on every bounded ball because F is a finite polynomial. Define

    R_r(t)=Psi_r G_r(z_r(t))-F(Psi_r z_r(t)).

Subtracting the two integral equations gives

    e(t)<=e(0)+integral_0^t [Lambda e(s)+||R_r(s)||] ds,

where e(t)=||Psi_r z_r(t)-X(t)||. Solving the scalar majorant by multiplying
its derivative by exp(-Lambda*t) yields

    e(t)<=exp(Lambda*t)e(0)
                 +integral_0^t exp(Lambda*(t-s))||R_r(s)|| ds.       (4)

The initial discrepancy is explicitly the projected c/response errors;
initial weight changes are zero. Output errors are controlled by

    |<c,H3>_n-<c_hat,H_hat3>_n|
      <=||c-c_hat||_n ||H3||_n + ||c_hat||_n ||H3-H_hat3||_n.        (5)

Equations (4)--(5) prove a conditional common-time statement. They do not
estimate the omitted error by rank alone. Numerical integration defects are
an additional term; the protocol's tolerance refinement is an empirical
numerical check, not a computed bound on R_r.

For a possible initial-data-only residual certificate, store fourth-order
feature Grams H_ijkl=<Q_i Q_j Q_k Q_l>_n. Each elementary multiplication has
the exact squared projection defect

    ||(Qa) elementwise (Qb)-Q(a star b)||_n^2
       =sum_ijkl a_i b_j a_k b_l H_ijkl - ||a star b||_2^2.

Operator defects likewise follow from quadratic forms of the stored Gram
of W0 Q_prev-Q C and its reverse counterpart. Bounds on intermediate product
and operator norms propagate these local defects through the finite RHS
calculation and produce a bound for ||R_r|| without retaining neuron arrays.
These optional Grams and propagated bounds were not implemented or measured
in the frozen experiment, and could be conservative.

Decoder prediction versus dense prediction can alternatively be bounded in
physical parameter space, or by adding (3) to (5). Distinct loss-stopping
times require another estimate: a bound on output time variation and on
the stopping-time difference, typically requiring transversality of the
loss crossing. Common-time control does not supply that estimate implicitly.

The surviving obligations are thus a small accumulated residual, controlled
amplification, decoder consistency for the intended readout, and independently
validated width dependence. Full-rank recovery settles the implementation
identity, not these reduced-rank approximation questions.
