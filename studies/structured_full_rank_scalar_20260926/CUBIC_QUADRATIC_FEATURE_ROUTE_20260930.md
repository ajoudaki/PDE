# Exact hidden-feature Hessian in a finite scalar gradient flow

2026-09-30. Frozen round-four construction before any training in this
route. The supervisor explicitly requested this omitted term after the
previous finite models remained inaccurate. It is one theory-specified
change, not a parameter search. Scientific inputs are the same study's
`cubic_minimal_mode_repair.py`, its own initial-response construction,
and the canonical initial network and mobilities in `dense_compare.py`.
No other study or trained trajectory is used. This scoped author runs
coefficient and algebra checks only; any training belongs to the supervisor's
separate frozen protocol.

## Model and initial contractions

The initial two-hidden-layer tanh network has first and second features
`p_x=tanh(w0 x)`, `H_x=tanh(W0 p_x)`. Write
`q_x=1-p_x^2`, `d_x=1-H_x^2`, and `<a,b>=a.T b/n`.
The readout is initially zero. The loss is unhalved mean square,
`alpha=2/m`, with canonical mobilities `(n,1,n)` and hidden metric

    <(dw,dW),(ew,eW)> = trace(dw.T ew)/n+trace(dW.T eW).

Fix the initial readout basis C as either the m training features H_a,
or those features plus the single terminal cubic response mode E from
`CUBIC_MINIMAL_MODE_ROUTE_20260930.md`. There is no additional mode tuning.
Let `pdim` denote its size, and `G_ij=<C_i,C_j>`.
For the paired index j=(b,i), the initial hidden gradient is

    gamma_j = d_b*C_i,
    beta_j = q_b*(W0.T gamma_j),
    Phi_j = (beta_j u_b.T, gamma_j p_b.T/n).

Form the exact Gram S of these directions. Its `(b,i),(c,k)` entry is

    (u_b dot u_c)<beta_bi,beta_ck>
      +<p_b,p_c><gamma_bi,gamma_ck>.

Let S=V diag(lambda) V.T and keep every eigenvalue strictly above
`1e-12*lambda_max`. This is the one fixed numerical rank convention,
with retained/discarded rank and eigenvalues reported. No cutoff is
selected from output accuracy. Define

    U=V_kept diag(lambda_kept^(-1/2)),
    xi_l=sum_j U_jl Phi_j,     l=1,...,d.

These directions are orthonormal in the stated hidden metric, up to
floating-point error. Positive discarded eigenvalues are a numerical
projection approximation; statements about all original directions require
their absence. S=0 gives d=0. No matrix pseudoinverse is applied in the ODE.

The scalar coefficient arrays are

    A_ai=<C_i,H_a>,
    L_ail=<C_i,DH_a[xi_l]>=(S U)_(ai),l,
    H_ailk=<C_i,D^2H_a[xi_l,xi_k]>.

The letter H with four indices denotes a contracted Hessian; the initial
feature H_a remains a width vector only during construction.

## Exact Hessian construction

For any two fixed hidden directions X=(dw_X,dW_X) and Y, at input x put

    t_X=dw_X x,
    dp_X=q_x*t_X,
    d2p_XY=(-2 p_x*q_x)*t_X*t_Y,
    dz_X=W0 dp_X+dW_X p_x,
    d2z_XY=W0 d2p_XY+dW_X dp_Y+dW_Y dp_X.

The exact second derivative of the original hidden feature map is

    D2H_x[X,Y]=(-2 H_x*d_x)*dz_X*dz_Y+d_x*d2z_XY.

Both mixed middle/first-layer terms are required. There is no second
derivative of W itself: W is an affine parameter. The factors 1/n in
Phi's middle block already encode the mobility convention; they are not
inserted again in directional differentiation.

The implementation whitens before forming the quadratic matrices. Let
`t_l=sum_j U_jl beta_j (u_b dot x)`, `dp_l=q_x*t_l`, and

    dz_l=W0 dp_l+sum_(b,i) U_(bi),l gamma_bi <p_b,p_x>.

The contracted first term is the weighted Gram

    <C_i*(-2 H_x*d_x), dz_l*dz_k>.

Move W0 to its actual transpose in the first part of d2z. Its contribution
is the weighted Gram of t_l,t_k with weight
`[W0.T(C_i*d_x)]*(-2 p_x*q_x)`. The mixed part is

    M_ilk=sum_(b,s) U_(bs),l <C_i*d_x,gamma_bs> <p_b,dp_k>.

Add `M_ilk+M_ikl`. This procedure retains every exact Hessian term and
never forms a separate width-by-width dW matrix for each direction.

## Frozen autonomous equations and passive decoder

Keep `v in R^pdim` and `eta in R^d`, initially zero. For degree two set

    F_ai(eta)=A_ai+sum_l L_ail eta_l
                       +.5 sum_lk H_ailk eta_l eta_k,
    B_al=sum_i v_i (L_ail+sum_k H_ailk eta_k),
    f=Fv,    r=f-y.

The frozen equations are

    v'=-alpha G^{-1} F.T r,
    eta'=-alpha B.T r.

This is the exact gradient flow of the displayed finite quadratic-feature
model, with readout metric G and orthonormal hidden coordinates. For the
controlled degree-one baseline use precisely the same C,U,A,L, and omit
H everywhere. A degree-one comparison therefore isolates curvature from
whitening or mode selection.

Its training kernel and energy identities are

    r'=-alpha (F G^{-1} F.T+B B.T)r,
    loss'=-||v'||_G^2-||eta'||^2 <=0,
    d(v.T G v)/dt=-2 alpha r.T f.

All derivatives vanish when r=0. The kernel is positive semidefinite.
Every finite solution exists globally, despite the polynomial feature
map: integration of the loss identity gives a finite integral of squared
state speed, and Cauchy--Schwarz bounds its travel on [0,T] by
`sqrt(T*loss(0))` in the fixed positive state metric. A bounded finite
state cannot terminate a solution of this smooth polynomial ODE. Neither
this argument nor kernel positivity proves that arbitrary labels fit.

At every passive query x, form the same A_x,L_x,H_x contractions once.
Decode with the identical formula `f(x)=F_x(eta)v`; no query states or
interpolation repair are needed. Training aliases agree exactly in
arithmetic. No queries enter basis selection or the training equations.

## Claim boundary and cost

For fixed readout/hidden subspaces and small labels, v starts at order a
and eta at order a^2. The Hessian first affects eta at order a^4 and
output at order a^5. It does not change cubic coefficients. This is the
exact initial hidden-feature curvature, unlike an empirical activation
gate. It remains a finite Taylor model: it does not enforce tanh bounds,
contain all later hidden directions, or provide general fifth-order
agreement with the unconstrained original network. Cubic readout motion
outside C can feed later hidden motion. A single added terminal mode does
not eliminate that general obstruction.

The evolving state has `pdim+d<=pdim+mpdim=O(m^2)` scalars. G,A,L,H
require O(m^6) static training coefficients in the worst case, versus
O(m^4) for the bilinear response tensor. Each query requires
`pdim*(1+d+d^2)=O(m^5)` scalars, with no evolving query coordinates.
The direct RHS cost is O(m*pdim*d^2)=O(m^6). This trades static coefficients
and contraction work for dynamic compression; it is not a universal
arbitrary-accuracy construction or an end-to-end speedup claim.

For q queries, dense one-time construction costs, conservatively,
O(n^2 m pdim+n(m pdim)^2+(m pdim)^3)
for the basis and whitening, followed by
O((m+q)[(d+pdim)n^2+pdim*d^2*n+d*m*pdim*n])
for the derivative contractions. Workspace stores the given W0 once,
initial response arrays, and O(n*d+n*pdim) query temporaries. The returned
model and coefficients retain no width vectors or weight matrices.

The supervisor's hard initialization limits are 30 seconds per task and
2 GiB resident memory; constructor timing and coefficient bytes must be
reported. The prototype adds no internal wall-time truncation that could
silently return incomplete coefficients. A caller enforces the hard
budget and records a failure if exceeded. No training result is claimed
by this note. Deterministic checks and any limitations are appended below.

## API and explicit lifted-network diagnostic

`cubic_quadratic_feature_repair.py` exposes

    initialize_with_queries(w,W,inputs,labels,queries,extra_mode=False,degree=2)

with optional arguments keyword-only. It returns `(model,coefficients)`.
The model has `initial_state()`, `rhs(t,state)`, `residual(state)`,
`predict(state,coefficients)`, `blocks`, `size`, `training_size`,
`kernel(state)`, `readout_energy(state)`, and constructor metadata.
Separate initialize/query functions are supplied for callers that need
them; combined construction avoids regenerating the initial response
basis. Degree one and degree two select the same initial basis and hidden
whitening for a fixed input dataset and label direction.

The supervisor separately authorized this posthoc mechanism diagnostic:

    lifted_endpoint_diagnostic(w,W,inputs,labels,queries,state,extra_mode=False)

It regenerates the identical initial C,U and explicitly constructs

    c=sum_i v_i C_i,
    dw=sum_l eta_l xi_l.w,
    dW=sum_l eta_l xi_l.W.

It then evaluates the **exact tanh network** at `(w0+dw,W0+dW,c)` on
the specified queries. Its returned dictionary contains `prediction`
and serializable displacement/feature-motion norms. Compare its
`basis_whitening_sha256` with the model metadata to certify that the
lift used the same basis and whitening orientation. This diagnostic
explicitly accesses width arrays after the scalar solve. It is separate
from the scalar RHS and decoder and must not be represented as scalar
runtime, a deployable decoder, or a new training method. It takes no
dense target/reference output and performs no fitting or integration.

## Deterministic pre-training verification

The scoped author ran

    OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 timeout 40s python studies/structured_full_rank_scalar_20260926/check_cubic_quadratic_feature_repair.py

The script includes no training solve. It checks both basis choices on
a finite width-40,m=3 network, constructing physical hidden directions
independently and differentiating the original tanh network by central
differences. For steps `0.002,0.001,0.0005`, mixed-Hessian errors were
respectively `(3.27e-6,8.17e-7,2.04e-7)` without E and
`(6.47e-6,1.62e-6,4.04e-7)` with E, exhibiting the expected second-order
finite-difference convergence. The final errors satisfy the pre-check
`2e-6` threshold. Hessian symmetry and training-query alias errors were
exactly zero in both cases.

Whitened physical Gram errors were at most `6.50e-14`. The scalar
kernel derivative, loss dissipation and readout-energy identities held
within `1.39e-17`; an independent loss-gradient finite difference agreed
within `4.25e-11`. The degree-one model matched a direct width-space
linear-feature calculation within `6.94e-18`. The explicit lifted
diagnostic matched a separate direct tanh evaluation within `6.94e-18`,
with matching basis fingerprints and hidden-metric norm within `2.23e-16`.

A constructor-only check at width 1024, m=6, extra mode enabled, and 262
queries took `1.856` seconds with peak resident memory `89,944,064`
bytes. It retained all 42 hidden directions, used 49 evolving scalars,
and returned `607,984` training coefficient bytes plus `26,512,304`
query coefficient bytes. Its whitening Frobenius error was `1.67e-11`,
and training linear coefficients agreed with S U within `1.64e-14`.
This checks the requested resource envelope at one representative largest
m; it is not a universal timing or conditioning guarantee.

The frozen model source SHA256 is
`eeeef4226dcfa2aa097e1b8ac3fc495b8a3c51a185fd63c18cdbf164ec7706f6`;
the check source SHA256 is
`0835ca44451845fc71bd90401a3bd5491e93040c9910f36b28a6224dafd953a7`.
Raw results are preserved at
`data/generated/structured_full_rank_scalar_20260926/cubic_quadratic_feature_20260930/check_1790797271288475055/check.json`.
Each reproduction creates its own output directory.

A fresh prompt-only algebra auditor independently checked the supplied
Hessian, metric scaling, gradient/kernel/energy identities, and global
existence argument. The auditor did not inspect source or data. Its
main qualification is incorporated above: Hessian inclusion alone does
not recover readout directions missing from C, and dropped positive
Gram eigenvalues would be a real projection approximation. This is a
scoped algebra check, not an independent complete review or promotion.

Status at freeze: finite construction and implementation checked as
recorded; strong-label accuracy and mechanism identification remain open.
No training integration was run by this scoped author.
