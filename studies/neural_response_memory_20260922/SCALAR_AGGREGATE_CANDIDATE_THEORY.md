# Scalar aggregate directional hierarchy for dense nonlinear training

2026-09-25. Scoped theory construction for the user-authorized scalar-only
continuation. This file is an author derivation, not an independent review,
an experimental report, or promoted material. The scoped author ran no
research experiment. Numerical implementation and the frozen bounded test
protocol are owned by the supervisor.

## 1. Recommendation and precise target

Test the rank-four directional hierarchy below against the original dense
three-hidden-layer tanh gradient flow. Every retained coordinate and every
stored coefficient is a scalar indexed only by training samples. Once the
initial scalar tensors are computed, the reduced RHS contains no neuron
arrays, initialized matrices, parameter vectors, dense-network evaluator,
new neural gradients, or trajectory-derived coefficients. It is an autonomous
nonlinear observable closure with constant storage in width and elapsed steps.

This constructs a new aggregate approximation directly to the canonical dense
flow. It is not an exact aggregation of the study's fixed-history-order
Legendre population model. It therefore introduces no history-projection
order P and does not inherit that model's estimates for its physical defect.
Its sole new approximation is truncation of a directional-derivative
hierarchy. The resulting scalar closure defect is derived below.

The observables are the M training outputs and their mean squared residual.
The permitted initializer uses the same finite dense network as the reference,
and model derivatives at that initialized state only. Labels enter the reduced
RHS through its current residuals; no future dense trajectories are read or
fitted. A bounded experiment may assess one candidate on its specified finite
horizon. It cannot establish arbitrary-accuracy existence or width-uniform
convergence.

## 2. Exact directional hierarchy

Flatten the physical parameters as theta. Let B be the constant block
mobility matrix: n on the first matrix and readout blocks, and 1 on each
internal matrix block. Let f_a(theta) be the canonical normalized output,
r_a=f_a-y_a, and alpha=2/M. Define the model-derived vector field and its
scalar derivative operator

    g_a(theta)=B grad_theta f_a(theta),
    D_a H(theta)=grad_theta H(theta) dot g_a(theta).

The canonical dense flow is exactly

    theta'=-alpha sum_a r_a g_a(theta).

For each scalar parameter observable H, the chain rule gives

    H'=-alpha sum_a r_a D_a H.

Define, with the last index always the outermost derivative,

    Theta_ab = D_b f_a,
    C_abc    = D_c Theta_ab,
    Q_abcd   = D_d C_abc,
    R_abcde  = D_e Q_abcd.

All five types are scalar observables of the dense state. Since B is
symmetric positive definite,

    Theta_ab=(grad f_a)^T B grad f_b.

Thus Theta is symmetric positive semidefinite at every physical dense state.
For the three-hidden model and the notation of DEEP_CIRCLE_DERIVATION,

    H^(ell)_ab=h_(ell,a)^T h_(ell,b)/n,
    D^(ell)_ab=delta_(ell,a)^T delta_(ell,b)/n,
    G_ab=U_a^T U_b,

    Theta_ab=H^(3)_ab+H^(2)_ab D^(3)_ab
                        +H^(1)_ab D^(2)_ab+G_ab D^(1)_ab.

The scalar observables satisfy the exact, unclosed equations

    f'_a       = -alpha sum_b Theta_ab r_b,
    Theta'_ab  = -alpha sum_c C_abc r_c,
    C'_abc     = -alpha sum_d Q_abcd r_d,
    Q'_abcd    = -alpha sum_e R_abcde r_e.

The derivative direction itself depends on theta. Consequently D_d D_c
need not equal D_c D_d. Only the first two indices of C and Q are
necessarily symmetric. Do not symmetrize the derivative indices c,d.

## 3. Autonomous rank-four truncation and matched lower orders

Initialize f,Theta,C,Q at the exact common dense initialization. Evolve

    f'_a       = -alpha sum_b Theta_ab (f_b-y_b),
    Theta'_ab  = -alpha sum_c C_abc (f_c-y_c),
    C'_abc     = -alpha sum_d Q_abcd (f_d-y_d),
    Q'_abcd    = 0.

This polynomial vector field is locally Lipschitz and has a unique local
solution from every finite initial scalar state. Finite-time boundedness and
positive semidefiniteness of Theta are not guaranteed by this truncation.
Loss is computed directly as mean((f-y)^2), with exact reduced identity

    loss'=-(4/M^2) r^T Theta r.

The reduced loss decreases whenever the current reduced Theta is positive
semidefinite. Indefiniteness, loss growth or finite-time failure are possible
candidate failures; silently clipping eigenvalues would define a different
closure. A consistent zero-residual state is stationary.

The rank-two control freezes Theta and evolves only f. The rank-three
closure additionally evolves Theta with frozen C. The rank-four candidate
is the smallest member of this list that can represent the leading kernel
acceleration when the readout starts at zero. Indeed, with c=0, g_a moves
only the readout; Theta has an even dependence on c, so D_c Theta=0 at that
point. Q need not vanish: it contains both readout-curvature terms and the
change of the g_c direction that starts moving hidden parameters. The actual
canonical readout is small but nonzero; this exact zero-readout observation
explains why an initially tiny C need not imply negligible feature learning.

Counting nonsymmetry-reduced tensors, the rank-four representation retains

    M + M^2 + M^3 + M^4

scalar values, including the constant Q coefficient tensor: 340 at M=4 and
4680 at M=8. Its moving state can omit Q and pass it as immutable coefficient
storage. Each RHS requires O(M^4) arithmetic and no width-dependent work.

The reduced system is nonlinear through the products of its current residuals
and evolving derivative tensors. It is not a Taylor polynomial in physical
time. It is restartable using its current scalar state. For example, with
z'_a=-alpha r_a and z(0)=0, it has the equivalent identities

    C_abc=C_abc(0)+sum_d Q_abcd(0) z_d,
    Theta_ab=Theta_ab(0)+sum_c C_abc(0) z_c
               +sum_cd Q_abcd(0) integral z_d dz_c.

These are integrals of its own current residual-controlled evolution. The
ordered integrals generally carry noncommuting directional information and
cannot all be replaced by one-half z_c z_d. No observed target path supplies
them. Maintaining the tensor equations directly is simpler than using these
alternative coordinates.

## 4. NumPy-feasible initialization by analytic bivariate differentiation

All width-dependent objects in this section are temporary initializer work.
They must not become coefficients or hidden state of the reduced RHS.

From a forward/backward pass at theta0, each g_c has blocks

    (g_c)_W1 = delta_(1,c) U_c^T,
    (g_c)_Well = delta_(ell,c) h_(ell-1,c)^T/n, ell=2,3,
    (g_c)_readout = h_(3,c).

The factors follow from grad f's factor 1/n and the stated B mobilities.
There is no residual or factor alpha in g_c.

To compute a_cd=Dg_c(theta0)[g_d(theta0)], differentiate one ordinary
forward/backward pass along the fixed parameter direction g_d. Denote its
directional responses by h^[d],delta^[d]. Then

    (a_cd)_W1 = delta_(1,c)^[d] U_c^T,
    (a_cd)_Well = (delta_(ell,c)^[d] h_(ell-1,c)^T
                     +delta_(ell,c) (h_(ell-1,c)^[d])^T)/n,
    (a_cd)_readout = h_(3,c)^[d].

The directional pass uses the full product rules. For example,

    z_ell^[d]=(g_d)_Well h_(ell-1)+Well h_(ell-1)^[d],
    h_ell^[d]=(1-h_ell^2) .* z_ell^[d],
    delta_3^[d]=(g_d)_readout .* (1-h_3^2)
                         -2 c .* h_3 .* h_3^[d],

with lower backward layers obtained by differentiating their actual matrix
transposes and gates. Independent random reverse maps are never introduced.

For each ordered pair c,d, form the formal parameter bi-jet

    theta(s,t)=theta0+s g_c+t g_d+st a_cd.

Evaluate the scalar kernel formula using coefficients of 1,s,t,st in all
forward and backward operations. Its s coefficient is C_abc. Its st
coefficient is exactly

    D^2 Theta_ab[g_c,g_d]+DTheta_ab[a_cd]
      = D_d(D_c Theta_ab)=Q_abcd.

This follows by differentiating D_c Theta=DTheta[g_c] in direction g_d.
It is the crucial direction-derivative term: omitting a_cd computes a
fixed-direction Hessian contraction instead of the requested Q.

There is no factor one-half in the mixed coefficient, even for c=d: s and
t remain distinct formal variables. If X=X0+s Xs+t Xt+st Xst and similarly
for Y, a bilinear product has mixed coefficient

    (XY)st=X0 Yst+Xs Yt+Xt Ys+Xst Y0.

For h=tanh(z), the coefficients are

    h0=tanh(z0),
    hs=(1-h0^2) zs,
    ht=(1-h0^2) zt,
    hst=(1-h0^2) zst-2 h0(1-h0^2) zs zt.

The gate 1-h^2 is then evaluated by these same algebraic product rules.
They apply componentwise for gates and through the actual matrix product
for layer actions. Gram matrices are formed using the same rules and their
explicit factors 1/n. The resulting tensors are computed from model
identities without automatic differentiation libraries or dense training.

There are M^2 ordered pairs. Each pair needs a constant number of ordinary
three-layer forward/backward matrix operations over M samples. This gives
O(M^3 n^2) leading initializer arithmetic for fixed depth, with a moderate
constant from four bi-jet components. Pairwise streaming keeps temporary
memory O(n^2+nM), in addition to the stored scalar tensors; optionally
caching M directions adds O(M n^2). Widths 128--512 and M=4--8 are
computationally plausible for a bounded CPU initializer, but wall time must
be measured rather than promised. The reduced evolution itself remains
O(M^4) at every width.

## 5. Exact new defect and validity scope

Let A(theta)=(f,Theta,C,Q) and G be the truncated scalar vector field. Along
the dense flow,

    DA(theta) theta'-G(A(theta))
        =(0,0,0,-alpha sum_e R_abcde(theta) r_e).

This is the aggregate closure defect. It is not the history covariance E2
or E3 of the Legendre model. Initial f,Theta,C,Q are exact, but the omitted
next derivative can immediately change Q. For a compact region containing
the exact aggregate path and reduced path, assume G is Lambda-Lipschitz and
both solutions exist through T. Subtracting their integral equations and
using the integrating factor yields

    |q_reduced(t)-A(theta_dense(t))|
       <= integral_0^t exp(Lambda(t-s)) |defect(theta_dense(s))| ds.

The displayed source is exact; no small-source or width-uniform bound is
established here. If Q is treated as a fixed coefficient rather than a state,
the equivalent defect in C' is

    -alpha sum_d (Q_abcd(theta_dense(t))-Q_abcd(theta0)) r_d.

For smooth finite-width dynamics, the rank-four closure matches the first
three physical-time derivatives of f at initialization. The fourth output
derivative can involve R and is generally unmatched. This local consistency
does not make the entire reduced solution a cubic time polynomial, and it
does not give a useful long-horizon error bound.

## 6. Implementation audits and claim limits

A bounded test should distinguish the following:

- Initializer correctness: the explicit kernel matches the original dense
  output velocity; first-order and mixed bi-jet coefficients agree with
  finite differences at small diagnostic widths; the direction acceleration
  a_cd is included; first two tensor indices have the expected symmetry.
- Scalar-only contract: serialized reduced coefficients contain only f0,
  Theta0,C0,Q0 and labels/configuration. A reduced RHS call after initializer
  arrays are discarded performs only sample-indexed scalar contractions.
- Nonlinearity: the rank-four candidate is compared with the same initialized
  frozen kernel. Accuracy on a reference interval where the frozen kernel
  also succeeds does not isolate nonlinear feature learning.
- Numerical validity: dense and reduced integrators are separately refined;
  failures or instability are preserved as results. Track the smallest
  symmetric-kernel eigenvalue and any loss increase instead of suppressing
  them by an unannounced projection.
- Restartability: splitting a reduced integration and restarting from the
  saved scalar state must reproduce the unsplit integration up to solver
  tolerance. Reinitializing the hierarchy from a dense reached state is a
  distinct experiment and requires a new authorized initializer call.

Exact items are the directional identities, the specified finite closure,
its width-independent retained storage and RHS, its causal initialization,
and the explicit defect formula. Accuracy, global existence, positive
semidefiniteness after truncation, compact-horizon convergence as order grows,
and width-uniform approximation remain open until separately supported.
Failure of this rank-four closure would reject this witness on that test;
it would not exclude all finite scalar aggregate approximations.

## Scientific input scope

Complete assigned inputs read: AGGREGATE_OBSERVABLE_CLOSURE.md,
MOMENT_CONSTRUCTION.md, RATIONAL_ORTHOGONAL_MOMENT_ROUTE.md,
DEEP_CIRCLE_DERIVATION.md, deep_circle_cases.json, and docs/NOTATION.md.
Required process skills read: investigate-conjectures with its research
contract and adversarial-audit references, and solve-math-rigorously.
No other study, experiment output, or external scientific source was read.
Only this assigned theory file was written; no Git mutation was performed.
