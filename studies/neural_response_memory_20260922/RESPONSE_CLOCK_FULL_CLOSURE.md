# A fully specified response-clock closure

Explanation and algebraic continuation, 2026-09-25. This fixes one version of
the proposal: two hidden tanh layers, a finite uniformly weighted training
set, the unscaled Euclidean response monitor, a continuous matching prefix,
and weighted polynomial projection. It does not implement or experimentally
validate the solver. Root owns this file and its README pointer.

Inputs are RESPONSE_CLOCK_DESIGN.md, RESPONSE_CLOCK_WEIGHTED_CHECK.md and the
canonical conventions already read for this study. Two prompt-scoped agents,
complete_clock_bound and complete_clock_algorithm, checked respectively the
all-order reconstruction proof and the complete finite algorithm. They read
only their assigned current-study notes and prompt equations; neither wrote
files nor ran experiments. Their checks were collaborative internal checks,
not promotion reviews. Root checked both complete responses and the algebra
below. The prefix-correction bookkeeping is essential throughout.

## 1. Model, current responses, and the clock

There are M samples (x_a,y_a), x_a in R^d, and n neurons in each hidden layer.
The initialized middle matrix W0 is fixed and retained. For current outer
weights W1 in R^(n by d), W3 in R^n and reconstructed middle operator W_hat,

    h1_a=tanh(W1 x_a/sqrt(d)),
    h2_a=tanh(W_hat h1_a),
    f_a=W3^T h2_a/n, r_a=f_a-y_a,
    rho=sqrt(mean_a r_a^2),
    delta2_a=W3 odot (1-h2_a^2),
    delta1_a=(1-h1_a^2) odot W_hat^T delta2_a.

On rho>0 define u_a=r_a delta2_a/rho and the explicit observable map

    Psi=stack_a(h1_a,u_a) in R^(2nM).

The proposed clock is

    g=rho+||Psi_dot||_2
     =rho+sqrt(sum_a(||h1_a_dot||_2^2+||u_a_dot||_2^2)),
    L_dot=g, L(0)=1.

All dots are derivatives with respect to physical time t. The clock is an
extra scalar of the closure, not a new optimizer. Psi is computed from the
current state; it is not a separately trained or independently integrated
variable. Its velocity is computed explicitly in section 5.

For one sample, rho=|r| and u=sign(r)delta2. On a positive-residual-magnitude
interval the sign is constant, so

    g=|r|+sqrt(||h1_dot||_2^2+||delta2_dot||_2^2).

Let A=1+integral_0^t rho ds. Then

    L=A+integral_0^t ||Psi_dot||_2 ds,  A<=L.

Thus L combines accumulated residual activity with response-path length.
Each selected vector is 1-Lipschitz in the new coordinate because its physical
speed is at most g. Equivalently ||dPsi/dL||_2<=1. This statement uses the
unscaled Euclidean norm, not an implicit neuron/sample RMS normalization.

## 2. Coordinate placement and integration weight are different

At physical time s, place a history point at xi=L(s), but assign it integration
weight rho(s)ds. Precisely, for a scalar or vector integrand F,

    integral F(xi) dmu_t(xi)
      = integral_0^1 F(xi) dxi + integral_0^t F(L(s)) rho(s) ds.

The measure has mass A. Its density with respect to dxi on actual history is
rho/g; on the artificial prefix [0,1] it is one.

Define encoded histories hbar_a, ubar_a by hbar_a(L(s))=h1_a(s) and
ubar_a(L(s))=u_a(s). On the prefix they are the matching constants h1_a(0)
and u_a(0). Both extended histories are 1-Lipschitz on [0,L].

Let C_a=u_a(0)h1_a(0)^T, a fixed rank-one term stored by its vectors. Then

    J_a=integral ubar_a hbar_a^T dmu_t
       =C_a+I_a,
    I_a=integral_0^t r_a delta2_a h1_a^T ds.

The subtraction of C_a is necessary to remove the artificial learning
contribution. In particular, define the exact history integral along the
closure's own responses by

    W_int=W0-(2/(nM))sum_a I_a.

This is a mathematical comparison object; it is not supplied to the solver
and it is not the separately evolved dense network's weight.

## 3. Polynomial state, reconstruction, and initialization

For order P>=1, let p=(p_0,...,p_(P-1))^T be shifted Legendre polynomials on
[0,1], with p_k(1)=1. Everywhere in the following integrals evaluate p at
xi/L(t). Store

    H_a=integral hbar_a p^T dmu_t in R^(n by P),
    U_a=integral ubar_a p^T dmu_t in R^(n by P),
    G=integral p p^T dmu_t in R^(P by P).

G is shared by all samples because their coordinate and insertion measure
are shared. Since p_0=1, the mass A equals G_00 and needs no separate
evolving coordinate. For every nonzero c in R^P,

    c^T G c >= integral_0^1 |c^T p(xi/L)|^2 dxi >0.

A nonzero polynomial cannot vanish on the full prefix interval. Hence G is
positive definite for fixed finite P,L. This is not a conditioning bound.

The projections onto degree<P polynomials in L2(mu_t) are

    hbar_(P,a)(xi)=H_a G^(-1) p(xi/L),
    ubar_(P,a)(xi)=U_a G^(-1) p(xi/L).

Indeed their residual moments against every component of p vanish, which is
the finite-dimensional orthogonality condition. Their product integral is

    S_a=integral ubar_(P,a) hbar_(P,a)^T dmu_t
       =U_a G^(-1) H_a^T.

Reconstruct

    W_hat=W0-(2/(nM))sum_a(S_a-C_a).

The complete evolving state is W1,W3,(H_a,U_a)_a,G,L. Initialize W1,W3,W0
from the same network initialization as the original method; compute its
responses, rho0 and u_a0, then set

    H_a(0)=[h1_a(0),0,...,0],
    U_a(0)=[u_a(0),0,...,0],
G(0)=diag_k(1/(2k+1)), L(0)=1.

Thus S_a(0)=C_a and W_hat(0)=W0. If rho0=0, the original network is stationary
and can be returned without constructing an undefined normalized source.

This matching prefix differs from the old zero-backward prefix and changes
the finite-order closure. It is the specified version used for the clean
bound below. No old empirical result automatically applies to this version.

At P=1 the basis consists only of the constant polynomial. Then G=A is a
scalar, S_a=U_a H_a^T/A, and the moment derivatives have no coordinate-dilation
terms. With the prefix held fixed, changing the clock alone does not change
the physical P=1 closure. Coordinate adaptation affects higher modes P>=2.

## 4. Full proof of the same-history bound for every P>=1

Fix any finite time at which the construction is defined. Write L=L(t),
A=mu_t([0,L]), and d_P=max(1,P-1). All norms inside the weighted L2 spaces
are ordinary Euclidean vector norms.

Take either encoded history f=hbar_a or f=ubar_a. It is 1-Lipschitz, so
F(x)=f(Lx), x in [0,1], is L-Lipschitz.

For P>=2 set N=P-1 and construct the degree-N Bernstein polynomial

    B_N F(x)=sum_(j=0)^N F(j/N) binom(N,j) x^j(1-x)^(N-j).

This comparator is only a proof device; the solver uses the moment projection
and does not access these historical values or sample random variables.
Equivalently B_N F(x)=E[F(Z/N)] for Z binomial(N,x). Therefore

    ||F(x)-B_N F(x)||_2
      <= L E|x-Z/N|
      <= L sqrt(E|x-Z/N|^2)
       = L sqrt(x(1-x)/N)
      <= L/(2sqrt(N)).

The equality uses E[Z/N]=x and variance x(1-x)/N. Squaring the uniform bound
and integrating against a measure of mass A gives an L2(mu_t) bound
L sqrt(A)/(2sqrt(N)). Orthogonal projection is at least as accurate as this
particular degree-N comparator: its residual is orthogonal to the polynomial
space, so the Pythagorean identity proves that it minimizes the L2 error.

For P=1, the constant f(L/2) is an admissible comparator with uniform error
at most L/2. The same argument then proves, for every P>=1,

    E_(h,a)=||hbar_a-hbar_(P,a)||_(L2(mu_t))
             <= L sqrt(A)/(2sqrt(d_P)),
    E_(u,a)=||ubar_a-ubar_(P,a)||_(L2(mu_t))
             <= L sqrt(A)/(2sqrt(d_P)).

Expanding each history into its projection and residual gives

    J_a-S_a=integral(ubar_a-ubar_(P,a))
                      (hbar_a-hbar_(P,a))^T dmu_t.

The two mixed terms vanish because each projected component is a polynomial
and each residual component is orthogonal to all such polynomials. Using
||v w^T||_F=||v||_2||w||_2, the integral triangle inequality and Cauchy–Schwarz,

    ||J_a-S_a||_F <= E_(u,a)E_(h,a)
                  <= A L^2/(4d_P).

Since J_a=C_a+I_a, this is equivalently the error of S_a-C_a in reconstructing
the physical integral I_a. Summing and retaining the canonical sample/width
normalization gives

    ||W_hat-W_int||_F
      <= (2/(nM))sum_a ||J_a-S_a||_F
      <= A L^2/(2n d_P).

For P>=2 this is exactly A L^2/[2n(P-1)], including one sample. M cancels
in the averaging, but A and L still depend on the task, width, sample count,
clock convention and evolved path. This is a conservative bound, not a sharp
spectral rate. At t=0 the actual error is zero even though this upper bound
is positive.

For one fixed supplied history the bound tends to zero with order. Different
closures generate different histories and L_P,A_P; the statement alone does
not bound them uniformly over P. Moreover W_int is built from those same
histories. Comparison to a separately evolved dense trajectory needs a
stability argument for the difference of the two history integrals. Numerical
errors, endpoint defects and Gram conditioning are not covered by this bound.

## 5. Explicit multi-input derivative evaluation

Let e=(1,...,1)^T and define the fixed lower-triangular matrix T by

    T_kk=k, T_kj=2j+1 for j<k, T_kj=0 for j>k.

The polynomial identity is x p'(x)=T p(x). At fixed historical xi,
the derivative of p(xi/L) is -(g/L)T p. Exact moment differentiation gives

    H_a_dot=rho h1_a e^T-(g/L)H_a T^T,
    U_a_dot=r_a delta2_a e^T-(g/L)U_a T^T,
    G_dot=rho ee^T-(g/L)(TG+GT^T), L_dot=g.

The source coefficients are rho, not g, because the insertion measure remains
rho dt. The clock changes the placement and dilation of the polynomial basis.

To evaluate g one needs response derivatives. There is no circular solve:
differentiate S_a=U_a G^(-1)H_a^T and use

    (G^(-1))_dot=-rho G^(-1)e e^T G^(-1)
                  +(g/L)(G^(-1)T+T^T G^(-1)).

All g/L terms cancel. Solve G q=e, set hstar_a=H_a q, ustar_a=U_a q, and get

    S_a_dot=(r_a delta2_a) hstar_a^T
               +rho ustar_a(h1_a-hstar_a)^T,
    V2=W_hat_dot=-(2/(nM))sum_a S_a_dot.

The constant prefix correction has zero derivative. V2 can be applied as a
sum of at most 2M rank-one terms. The matrix itself need not be assembled.

Compute the outer velocities at the reconstructed network:

    V1=W1_dot=-(2/(M sqrt(d)))sum_a r_a delta1_a x_a^T,
    V3=W3_dot=-(2/M)sum_a r_a h2_a.

Then evaluate sequentially

    h1_a_dot=(1-h1_a^2) odot (V1 x_a/sqrt(d)),
    h2_a_dot=(1-h2_a^2) odot (V2 h1_a+W_hat h1_a_dot),
    f_a_dot=(V3^T h2_a+W3^T h2_a_dot)/n,
    r_a_dot=f_a_dot,
    rho_dot=(sum_a r_a r_a_dot)/(M rho),
    delta2_a_dot=V3 odot(1-h2_a^2)
                    -2 W3 odot h2_a odot h2_a_dot,
    u_a_dot=(r_a_dot delta2_a+r_a delta2_a_dot)/rho
                    -u_a rho_dot/rho.

Finally evaluate Psi_dot by concatenation, evaluate g, and return the moment,
Gram and length velocities above together with V1,V3. No delta1 derivative,
g derivative, full Jacobian matrix, full loss Hessian or exact target
trajectory is an input to this calculation. rho is recomputed algebraically;
rho_dot is used only for the directional derivative of u.

The middle velocity differs from its canonical gradient component by exactly

    E=(2rho/(nM))sum_a(u_a-ustar_a)(h1_a-hstar_a)^T.

This is the closure defect. The history discrepancy bound in section 4 does
not by itself bound this endpoint-based velocity defect.

## 6. Matrix-free actions, cost, and implementation status

With c=2/(nM), evaluate both orientations using the same symmetric G:

    W_hat v=W0 v-c sum_a[U_a solve(G,H_a^T v)
                           -u_a0(h_a0^T v)],
    W_hat^T v=W0^T v-c sum_a[H_a solve(G,U_a^T v)
                           -h_a0(u_a0^T v)].

Use linear solves rather than constructing G^(-1). The learned correction
has rank at most min(n,M(P+1)), including the fixed prefix terms. The state
has nd+n+2MnP+P(P+1)/2+1 scalar entries if G symmetry is used. Fixed storage
additionally includes W0 (n^2), the data, and 2Mn prefix-vector entries.
Responses and Psi can be recomputed in O(nM) working arrays. State size is
independent of the number of elapsed time steps.

A dense factorization of G costs O(P^3) per right-hand-side evaluation.
Precomputing U_a G^(-1) via solves costs O(MnP^2); subsequent forward and
transpose actions cost O(n^2+MnP) per vector, including the retained W0.
Batching M sample vectors can therefore cost O(nM^2P) for the learned part.
Without precomputing factors, one action costs O(n^2+MnP+MP^2), using a shared
factorization. Prefix sums exploit T to evaluate moment dilation in O(MnP)
and Gram dilation in O(P^2). Extra response-derivative passes still apply W0.
These are direct-operation counts, not measured performance claims.

On rho>0, G positive definite, and finite L, all equations form an explicit
locally Lipschitz finite ODE, so local existence and uniqueness follow from
the finite-dimensional integral-equation contraction argument. There is no
global continuation or finite-total-clock theorem here. If rho=0 initially,
the original network is stationary. At a later exact zero residual one may
prescribe frozen evolution; the stated derivative formulas do not themselves
prove a unique regular extension through that boundary. Near-zero normalized
residual derivatives need numerical treatment and validation.

Analytic positivity of G does not imply good conditioning or positivity under
a finite-step solver. A real implementation must validate solves, integration
accuracy, reconstruction consistency, and near-zero handling. No numerical
implementation, experiment, practical speedup, or advantage over the previous
clock is claimed by this explanation.
