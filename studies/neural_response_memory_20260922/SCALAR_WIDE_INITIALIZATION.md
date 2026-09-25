# Exact cached initialization at width 2048

2026-09-25. This is an implementation derivation for the unchanged scalar
candidate, not a new approximation or a research-run result. The initializer
returns only the original sample-indexed f, Theta, C and ordered Q arrays.

## Preserved network and derivative convention

The stored matrices use exactly the existing normalization:

    H1 = tanh(W1 U^T),
    Hl = tanh(Wl H(l-1)), l=2,...,L,
    f = c^T HL/n.

There is no additional division by n inside a hidden-layer matrix action.
Write p_l=1-H_l^2 and B_L=c[:,None]. For l<L,

    B_l = W(l+1)^T delta(l+1),   delta_l = p_l B_l.

All products without matrix-multiplication notation are pointwise. Training
directions, and only training directions, determine the derivatives. For
direction i, the parameter direction G_l^i has factors

    G1^i = delta1[:,i] U_i^T,
    Gl^i = delta_l[:,i] H(l-1)[:,i]^T/n, l>1,
    g_c^i = HL[:,i].

The mixed parameter coefficient is A^{ij}=Dg_i[g_j], so Q[...,i,j]
means D_j(D_i Theta). Its internal-matrix blocks are rank at most two:

    Al^{ij} = (delta_l^j[:,i] H(l-1)[:,i]^T
                + delta_l[:,i] H(l-1)^j[:,i]^T)/n.

For the first matrix, A1^{ij}=delta1^j[:,i] U_i^T; for the readout,
A_c^{ij}=HL^j[:,i]. Neither these directions nor the initialized Gaussian
matrices are approximated. In particular, i,j are never symmetrized.

## Cached first and streamed mixed responses

For any rank-one factor uv^T, apply it to X as u(v^T X), and apply its
transpose as v(u^T X). Use the sum of two such actions for A^{ij}.
Consequently only the original W_l and W_l^T need dense matrix actions.

Cache the base fields and all M first-direction responses. With Z_l^i
the first preactivation response,

    Z1^i = G1^i U^T,
    Zl^i = Wl H(l-1)^i + Gl^i H(l-1),
    Hl^i = p_l Zl^i,
    B_L^i = g_c^i[:,None],
    B_l^i = W(l+1)^T delta(l+1)^i + G(l+1)^{i,T} delta(l+1),
    delta_l^i = p_l B_l^i - 2 H_l Hl^i B_l.

Process one ordered pair i,j at a time. The mixed preactivation and
activation coefficients are

    Z1^{ij} = A1^{ij} U^T,
    Zl^{ij} = Wl H(l-1)^{ij} + Gl^i H(l-1)^j
                + Gl^j H(l-1)^i + Al^{ij} H(l-1),
    Hl^{ij} = p_l Zl^{ij} - 2 H_l p_l Zl^i Zl^j.

Define p_l^i=-2H_l Hl^i and
p_l^{ij}=-2(Hl^i Hl^j+H_l Hl^{ij}). Then

    B_L^{ij} = A_c^{ij}[:,None],
    B_l^{ij} = W(l+1)^T delta(l+1)^{ij}
                 + G(l+1)^{i,T} delta(l+1)^j
                 + G(l+1)^{j,T} delta(l+1)^i
                 + A(l+1)^{ij,T} delta(l+1),
    delta_l^{ij} = p_l B_l^{ij} + p_l^i B_l^j
                    + p_l^j B_l^i + p_l^{ij} B_l.

These are precisely the coefficients of 1,s,t,st in the original bivariate
jet evaluated at theta+s g_i+t g_j+st Dg_i[g_j]. They do not divide by a
tanh derivative and remain defined when floating-point tanh saturates.
The two cross terms are both retained when i=j.

For a feature array V, the mixed rectangular Gram coefficient is

    K^{ij}(V) = ((V_probe^{ij})^T V_train
                  + (V_probe^i)^T V_train^j
                  + (V_probe^j)^T V_train^i
                  + V_probe^T V_train^{ij})/n.

The first Gram response has its two product-rule terms. Substitute these
Gram responses into the original cross-kernel formula, retaining all four
mixed product-rule terms in each product of activation and backward Grams.
This produces exactly the same Theta, C and Q as the original initializer.

## Work and storage estimates

For three hidden layers there are four large dense matrix actions per base,
first response or mixed response: two forward and two transpose actions.
For M=8 the count is therefore

    4(1+M+M^2) = 292

matrix products per combined training/probe batch. The old pairwise jet path
uses nine dense products per jet matrix action, giving 4*9*64=2304 products
for its 64 mixed pairs alone. The reduction in this dominant count is 7.89x
before batching overhead; it is not a measured speedup.

The implementation prepends the M training inputs to each batch. At n=2048,
1064 passive inputs, batch size128 and M=8, nine batches process a total of
1064+9*8=1136 columns. Counting a multiply-add as two operations gives about
2.78e12 floating-point operations for the large matrix products, compared
with approximately2.06e13 in the old passive mixed-jet path alone. Low-rank
actions, elementwise operations and Gram contractions add lower-order work.

Each n-by-136 float64 field is2.125MiB. The two dense internal matrices
occupy64MiB; the cached base and eight first responses occupy approximately
210MiB. Streamed mixed responses and temporary products add tens of MiB.
A working-memory estimate below450MiB is reasonable for this implementation,
excluding caller-retained duplicates and library workspaces; the first real
width2048 initialization must record actual RSS and elapsed time.

The returned training tensors occupy4680 float64 values at M=8. All1064
passive coefficient rows occupy622440 values, approximately4.75MiB. These
outputs are independent of width. Caller-owned initialized parameters are
never changed, and no parameter, feature cache or direction callback is
retained in the returned dictionary.

## Validation and execution boundary

`test_scalar_wide_initialization.py` passes five deterministic test methods:
complete old/new tensor comparisons over depths2/3, widths2/7 and all
orders2/3/4; zero, small and large readouts; width11 rectangular queries;
batch partition invariance; training-probe equivalence; explicit ordered-Q
asymmetry; saturated tanh; and input immutability/invalid-input rejection.
The comparison tolerance is4e-11 relative plus2e-12 absolute.

These checks establish numerical agreement on the stated fixtures. The
separately frozen width2048 protocol requires the first large configuration's
four-probe old/new comparison before its scientific use. No width2048
initializer, dense training or scalar research trajectory was run by this
implementation subtask. Initialization may use the protocol's four CPU BLAS
threads; scalar integration remains the existing single-threaded engine.
