# Fixed finite depth: the original activity-clock closure

Scoped theory route, 2026-09-25. Author: `deep_old_clock`.

**Result.** At every fixed finite hidden depth, finite width/data, and for
componentwise activations in `C^{1,1}_{loc}(R)`, the original zero-backward-prefix
Legendre closure has physical-weight error `O_T(P^{-1})` on each fixed finite
time interval, for all sufficiently large orders `P`. The constants and order
threshold depend only on initial arrays, data, activation bounds on specified
compact intervals, depth, width, and horizon. Bounded activations are not
required. This covers tanh, logistic sigmoid, and exact GELU. Unconditional
ReLU/SELU coverage requires a separate nonsmooth argument.

This is a complete candidate proof, not an independent check or promotion.
No experiment, numerical computation, or maintained-source edit is used.

## 1. Contract and equations

Fix positive integers `n,d,M`, hidden depth `H>=2`, finite real data `(x_a,y_a)`,
and arbitrary finite initial arrays. Every hidden layer has width `n`; there
are no biases. Write `z_a=x_a/sqrt(d)` and

    v_1a=W_1 z_a,                  h_1a=phi_1(v_1a),
    v_la=W_l h_(l-1),a,            h_la=phi_l(v_la),       2<=l<=H,
    f_a=w^T h_Ha/n,                r_a=f_a-y_a,
    rho=(mean_a r_a^2)^(1/2),      L=mean_a r_a^2.

Each componentwise activation is continuously differentiable with locally
Lipschitz derivative. Define

    delta_Ha=w odot phi_H'(v_Ha),
    delta_la=phi_l'(v_la) odot W_(l+1)^T delta_(l+1),a.

With mobilities `n` for `W_1,w` and one for internal matrices, unhalved
mean-square-loss gradient flow has vector field

    F_1=-2 mean_a r_a delta_1a z_a^T,
    F_l=-(2/n) mean_a r_a delta_la h_(l-1),a^T,       2<=l<=H,
    F_w=-2 mean_a r_a h_Ha.                                  (1)

Use the physical norm

    ||theta||_* = ||W_1||_F+sum_(l=2)^H ||W_l||_F+||w||_2.

Independently for each internal layer retain `P` raw forward/backward moments:

    tau_dot=rho,                         tau(0)=1,
    H_lak_dot=rho h_(l-1),a
       -(rho/tau)[k H_lak+sum_(j<k)(2j+1)H_laj],
    U_lak_dot=r_a delta_la
       -(rho/tau)[k U_lak+sum_(j<k)(2j+1)U_laj],
    W_lhat=W_l0-(2/(nM tau))sum_(a,k<P)(2k+1)U_lak H_lak^T,
    W_1hat_dot=F_1(theta_hat),             what_dot=F_w(theta_hat). (2)

All responses use the current reconstructed network. Initially
`H_la0=h_(l-1),a(0)`, higher `H` moments and all `U` moments vanish. The
common activity clock may equivalently be duplicated with identical initial
value/equation. The construction is autonomous and finite-state; coefficients
and initialization use only data and initial arrays. Histories and dense
trajectories below are proof devices, not information supplied to the solver.
The limit is `P->infinity` at fixed `n,d,M,H,T` in exact continuous time.

The proof first bounds the dense solution using gradient-flow dissipation.
On a physical ball, an exact projection-energy identity controls backward
endpoint errors; a layer induction then controls every forward history in
activity `H^1`. Forward projection approximation supplies small accumulated
errors. Integral stability closes the physical-ball bootstrap.

## 2. Dense existence and a non-oracle physical ball

The canonical vector field is locally Lipschitz. Along its local solution,

    -Ldot=||W_1dot||_F^2/n
              +sum_(l=2)^H ||W_ldot||_F^2+||wdot||_2^2/n.     (3)

Let `Lambda=2n+H-1` and `L_0=L(theta_0)`. Cauchy--Schwarz across blocks
with their mobility weights, then in time, gives

    ||theta(t)-theta_0||_*
       <=sqrt(Lambda t)[integral_0^t (-Ldot) ds]^(1/2)
       <=sqrt(Lambda t L_0).                                (4)

Thus parameters stay bounded at finite times. On a bounded physical set the
field is bounded and locally Lipschitz, so the solution has a limit at any
putative finite endpoint and extends by local existence there. This proves
unique global dense existence, without globally bounded activations.

Fix `0<=T<infinity`, set `R=1+sqrt(Lambda T L_0)`, and let
`K={theta:||theta-theta_0||_*<=R}`. The dense solution stays at least unit
distance from its boundary. Explicit constants on `K` are obtained recursively:

    X=max_a||z_a||,                  Y=(mean_a y_a^2)^(1/2),
    D_l=||W_l0||_F+R,               B_w=||w_0||+R,
    Z_1=D_1 X,
    A_l=sqrt(n) max_(|u|<=Z_l)|phi_l(u)|,
    G_l=max_(|u|<=Z_l)|phi_l'(u)|,
    Z_l=D_l A_(l-1)                  (2<=l<=H),
    B_H=B_w G_H,
    B_l=G_l D_(l+1)B_(l+1)          (l=H-1,...,1),
    q=B_w A_H/n+Y,                  S=Tq,          ell=1+S.    (5)

The forward definitions are evaluated in layer order. On `K` they bound
`||h_la||<=A_l`, `||delta_la||<=B_l`, `||W_l||_op<=D_l`, and `rho<=q`.
On an existing closure segment in `K` with `t<=T`, consequently
`tau<=ell` and `tau-1<=S`.

The raw field (2) is locally Lipschitz on `tau>0`; the residual norm is
locally Lipschitz, and (2) never divides by `rho`. A zero residual vector
makes every raw right-hand side zero. Local uniqueness, also in reversed
local time, prevents a solution with `rho(0)>0` from reaching that equilibrium
at a finite time of existence. Hence its activity is strictly increasing.
If `rho(0)=0`, both systems are the same stationary physical state and the
theorem is immediate. Below assume `rho(0)>0`.

## 3. Online projection energy and cross-energy

In activity `xi=tau(t)`, define the histories for each internal layer by

    a_la(xi)=h_(l-1),a(t(xi)),
    b_la(xi)=r_a(t(xi))delta_la(t(xi))/rho(t(xi)),       xi>1,

with constant prefix `a_la=h_(l-1),a(0)` and zero prefix `b_la=0` on `[0,1]`.
Write `Pi_s` for componentwise `L^2(0,s)` projection on polynomials of degree
less than `P`. Shifted Legendre orthogonality and the dilation identity
`x p_k'=k p_k+sum_(j<k)(2j+1)p_j` give, exactly,

    H_lak=integral_0^tau a_la(xi)p_k(xi/tau) dxi,
    U_lak=integral_0^tau b_la(xi)p_k(xi/tau) dxi,
    W_lhat=W_l0-(2/n)mean_a
                 integral_0^tau (Pi_tau b_la)(Pi_tau a_la)^T dxi. (6)

Indeed differentiation gives precisely (2) and its initial data; uniqueness
of those linear moment equations proves the first two identities. The
normalization `integral_0^1 p_jp_k=1_(j=k)/(2k+1)` proves the third.

For an arbitrary locally square-integrable vector history `g`, define

    e_g(s)=g(s)-(Pi_s g)(s),
    D_g(s)=integral_0^s ||g-Pi_s g||^2.

The exact endpoint energy identity is

    D_g'(s)=||e_g(s)||^2                 for almost every s>0. (7)

For vector histories `g,h` the cross-energy version is

    d/ds [integral_0^s gh^T
            -integral_0^s(Pi_s g)(Pi_s h)^T]=e_g(s)e_h(s)^T.   (8)

Neither formula differentiates `g` or `h`. To prove them, use the monomial
vector `v(x)=(1,x,...,x^(P-1))^T`, its Gram matrix `G(s)=integral_0^s vv^T`,
and `m_g(s)=integral_0^s gv^T`. The Gram matrix is positive definite for
`s>0`, since a nonzero polynomial does not vanish almost everywhere on an
interval. The projected history is `m_gG^(-1)v`; its cross-energy is
`m_gG^(-1)m_h^T`. The identities

    G'=v(s)v(s)^T,   m_g'=g(s)v(s)^T,
    (G^(-1))'=-G^(-1)G'G^(-1)

hold almost everywhere. Differentiating
`integral_0^s gh^T-m_gG^(-1)m_h^T` leaves the product
`[g(s)-m_gG^(-1)v(s)][h(s)-m_hG^(-1)v(s)]^T`, proving (8). Trace its
case `h=g` to obtain (7). In physical time this proves the requested identity

    D_gdot(t)=rho(t)||g(tau(t))-(Pi_tau g)(tau(t))||^2.         (9)

The ordinary polynomial space does not change algebraically as `s` grows;
only its basis coordinates and inner product change. Past history values
are fixed, including when future values are generated by closure feedback.
These facts justify the online use of (7)--(9).

On the physical ball, `mean_a||b_la||^2<=B_l^2`, since
`mean_a(r_a/rho)^2=1`. The zero backward prefix has zero projection error.
Consequently (7) and projection contraction imply

    integral_1^tau mean_a||e_b_la(s)||^2 ds
       =mean_a D_b_la(tau)
       <=mean_a integral_0^tau||b_la||^2
       <=B_l^2(tau-1)<=B_l^2S.                              (10)

In particular backward endpoint errors have a uniform activity `L^2`
bound without backward-history variation or derivative assumptions. The
backward prefix jump is allowed.

## 4. Forward endpoint control and finite-depth induction

For `g in H^1(0,s)`, its endpoint projection kernel is
`K_P(s,x)=s^(-1)sum_(k<P)(2k+1)p_k(x/s)`. Its integral is one. Telescoping
`p_(k+1)'-p_(k-1)'=2(2k+1)p_k` (with the `k=0` term separately) shows

    integral_0^x K_P(s,y)dy=Q_P(x/s),
    Q_P(u)=[p_P(u)+p_(P-1)(u)]/2.

The boundary values are `Q_P(0)=0` and `Q_P(1)=1`. Integration by parts and
Legendre orthogonality therefore give

    e_g(s)=integral_0^s Q_P(x/s)g'(x)dx,
    integral_0^s |Q_P(x/s)|^2dx
       =(s/4)[1/(2P+1)+1/(2P-1)]=sP/(4P^2-1)<=s/3,
    ||e_g(s)||<=sqrt(sP/(4P^2-1))||g'||_L2(0,s)
              <=sqrt(ell)||g'||_L2(0,s),       1<=s<=ell.      (11)

This bound is uniform for every `P>=1`. The exact factor even decays with
order, but the uniform bound suffices. Bounding endpoint evaluation from
arbitrary `L^2` histories instead would introduce growing powers of `P`.

Differentiate (6) with (8). With a prime now denoting activity differentiation,

    W_lhat'(s)=-(2/n)mean_a
                    [b_la(s)a_la(s)^T-e_b_la(s)e_a_la(s)^T].   (12)

This is exact and includes all compression feedback. Define constants

    J_1=2G_1B_1X^2 sqrt(S),
    V_l=(2B_l sqrt(S)/n)[A_(l-1)+sqrt(ell)J_(l-1)],
    J_l=G_l[A_(l-1)V_l+D_lJ_(l-1)],                 2<=l<=H.  (13)

We prove that `max_a||h_la'||_L2(0,tau)<=J_l`, with each forward history
extended constantly on `[0,1]`. Only the constants through `J_(H-1)` are
needed for matrix errors.

For the base layer, the first canonical equation divided by `rho` gives
`||W_1hat'||<=2B_1X`, using sample Cauchy--Schwarz. Therefore
`||h_1a'||<=G_1X||W_1hat'||<=2G_1B_1X^2`. Its active interval has length
at most `S` and its prefix derivative is zero, proving the bound `J_1`.

Suppose `J_(l-1)` has been proved on every existing history segment. Equation
(11) gives `max_a||e_a_la(s)||<=sqrt(ell)J_(l-1)`. Applying sample
Cauchy--Schwarz to (12),

    ||W_lhat'(s)||_F
      <=(2/n)[B_l A_(l-1)
            +sqrt(ell)J_(l-1)(mean_a||e_b_la(s)||^2)^(1/2)].

Taking the activity `L^2` norm and using (10) gives
`||W_lhat'||_L2(1,tau)<=V_l`. The forward chain rule is

    h_la'=diag(phi_l'(v_la))
             [W_lhat' h_(l-1),a+W_lhat h_(l-1),a'].

Its `L^2` norm is at most `G_l[A_(l-1)V_l+D_lJ_(l-1)]=J_l`, completing
the induction. There is no circularity: the derivative bound for `W_lhat`
uses only the preceding forward layer's derivative, and all backward sources
use physical bounds and (10). For fixed `P` the needed differentiations hold
on compact existing positive-activity segments. The estimates just derived
are independent of `P` and of the chosen segment, rather than assuming
uniform regularity in advance.

## 5. Projection error and accumulated physical defects

For every vector `g in H^1(0,s)`, shifted Legendre approximation satisfies

    ||g-Pi_s g||_L2(0,s)
       <=s||g'||_L2(0,s)/(2sqrt(P(P+1))).                    (14)

Here is the needed proof. The equation
`-[u(1-u)p_k']'=k(k+1)p_k` and integration by parts identify the weighted
derivative coefficient with `k(k+1)` times the ordinary coefficient.
Weighted Bessel then bounds the sum of coefficient energies multiplied by
`k(k+1)` by `integral_0^1 u(1-u)||g'||^2`. On the tail `k>=P`, divide by
`P(P+1)`, use polynomial completeness for Parseval and `u(1-u)<=1/4`, and
rescale the interval. Componentwise summation proves (14).

Define the proof-only accumulator along the closure's own trajectory,

    W_lacc(t)=W_l0+integral_0^t F_l(theta_hat(s))ds,
    R_lP=W_lhat-W_lacc.

The zero backward prefix contributes no unprojected product. Orthogonality
in (6) thus yields exactly

    R_lP=(2/n)mean_a integral_0^tau
                         b_la(a_la-Pi_tau a_la)^T dxi.        (15)

The source has sample-averaged `L^2` norm at most `B_l sqrt(S)`. By (13)--(14)
the forward error has norm at most `ell J_(l-1)/(2sqrt(P(P+1)))` for every
sample. Cauchy--Schwarz in sample and history gives

    ||R_lP||_F<=ell B_l sqrt(S)J_(l-1)/(n sqrt(P(P+1))),
    sum_(l=2)^H ||R_lP||_F<=C/sqrt(P(P+1)),
    C=(ell sqrt(S)/n)sum_(l=2)^H B_lJ_(l-1).                 (16)

This bounds signed accumulated error, not the instantaneous derivative
defect or the integral of its norm.

## 6. Explicit stability constant and continuation

An explicit Lipschitz constant for `F` on `K` follows from product splitting.
Let `L_l` be any finite Lipschitz constant for `phi_l'` on `[-Z_l,Z_l]` and set

    c_v1=X,                 c_h1=G_1 c_v1,
    c_vl=D_l c_h(l-1)+A_(l-1),    c_hl=G_l c_vl,    2<=l<=H,
    c_f=(B_w c_hH+A_H)/n,
    c_deltaH=G_H+B_w L_H c_vH,
    c_deltal=L_l c_vl D_(l+1)B_(l+1)
           +G_l[B_(l+1)+D_(l+1)c_delta(l+1)],       l=H-1,...,1,
    K_F=2X[B_1c_f+q c_delta1]
       +(2/n)sum_(l=2)^H[B_l A_(l-1)c_f
                      +q(A_(l-1)c_deltal+B_l c_h(l-1))]
       +2[A_Hc_f+q c_hH].                                  (17)

To check every contribution, for two states in `K` at distance `e`, forward
product splitting gives `||Delta v_la||<=c_vl e`, `||Delta h_la||<=c_hl e`,
and `|Delta f_a|<=c_f e`. Splitting the top gate and `w` gives `c_deltaH`.
At lower layers split the gate, matrix, and next backward response: their
bounds are the three terms in `c_deltal`. Splitting the residual and the
remaining response factors in (1), and using `mean|r_a|<=q`, gives exactly
the three block contributions in `K_F`. Hence

    ||F(theta')-F(theta)||_*<=K_F||theta'-theta||_*,  theta,theta' in K.

The physical weights obey the exact integral identity

    theta_hat(t)=theta_0+integral_0^t F(theta_hat(s))ds
                        +(0,R_2P(t),...,R_HP(t),0).           (18)

As long as the closure remains in `K`, subtract the dense equation and use
(16)--(17) to get `e(t)<=C/sqrt(P(P+1))+K_F integral_0^t e(s)ds`.
Iteration and the exponential series imply

    e(t)<=C exp(K_F T)/sqrt(P(P+1)).                          (19)

Choose any integer `P_0>=1` such that this last bound is at most `1/2` for
`P=P_0`. The explicit choice `P_0=max(1,ceil(2C exp(K_F T)))` suffices;
if `C=0`, choose one. For `P>=P_0`, a first exit from `K` before `T` would
give distance at least one from the dense state by (4), contradicting (19).

Premature termination of the raw solution while its physical state stays
in `K` is also impossible. Bessel in (6) gives, for each layer,

    sum_(a,k<P)(2k+1)||H_lak||^2<=M ell^2 A_(l-1)^2,
    sum_(a,k<P)(2k+1)||U_lak||^2<=M ell B_l^2S.               (20)

Together with the physical bounds on `W_1hat,what` and `tau in [1,ell]`,
these bound every coordinate of the finite raw state in a compact subset
of `tau>0`. The locally Lipschitz field is bounded there, so the state has a
limit at a putative finite endpoint and extends by local existence. This
justifies the first-exit argument even if a maximal interval initially ends
before `T`. Thus the closure exists uniquely on `[0,T]` for all `P>=P_0`,
and (19) holds throughout that interval.

For `T=0` the comparison is exact. For `H=1` no matrices are compressed and
the physical closure equals the dense system identically.

## 7. Scope and activation consequences

The resulting quantifiers are: for every finite `T` and every fixed finite
instance with `C^{1,1}_loc` activations, there are finite `P_0,C,K_F` independent
of `P` such that, for every `P>=P_0`, the closure exists uniquely on `[0,T]`
and

    sup_(t<=T)||theta_hat_P(t)-theta_dense(t)||_*
       <=C exp(K_F T)/sqrt(P(P+1)).                          (21)

Training-prediction error is at most `c_f` times this bound, and layer-`l`
hidden-response error at most `c_hl` times it. The same forward splitting
with a bounded passive-input norm gives uniform prediction/hidden-response
convergence on any fixed bounded set of passive inputs.

All constants and the threshold use initial loss, initial arrays, data, and
activation bounds on compact intervals determined by (5). No future dense
trajectory is used. The theorem asserts neither useful computational orders
nor width/depth-uniform constants, all-time tracking, numerical conditioning,
or a finite-step solver guarantee.

Tanh, logistic sigmoid, and exact GELU `u Phi(u)` are smooth on all of `R`.
GELU is unbounded, which does not obstruct this proof. The same argument
allows values and derivatives unbounded at infinity for any activation in
`C^{1,1}_loc`, since only compact-interval bounds enter.

ReLU and usual SELU fail to be `C^1` at zero. Their discontinuous gate maps
at crossings invalidate the local-Lipschitz and classical uniqueness/stability
steps above. Forward `H^1` histories alone do not repair this. Identities
(7)--(16) remain available along a suitably defined bounded trajectory with
the forward chain rule, but comparison to a selected dense nonsmooth flow
needs an additional crossing/solution argument.

A conditional special case is a dense trajectory whose every training
preactivation stays a positive distance from zero. Choose smooth activation
extensions agreeing with the original activation on its compact attained
preactivation intervals. Apply this theorem to the extensions. Physical
convergence then keeps sufficiently high-order closures in the same branches,
where both dense and closure equations agree with the original ReLU/SELU
equations. This argument does not cover crossing or touching a kink.

Unlike the two-hidden-layer tanh input theorem, this route proves finite-time
closure existence only for sufficiently large `P`; it does not prove global
existence at every fixed order. This limitation is not a demonstrated
finite-order blowup. The deeper-history obstruction itself is resolved:
backward endpoint energy (10), forward endpoint control (11), and the layer
induction (13) bound earlier compressed-matrix feedback without closure loss
decay or backward differentiability.

## 8. Provenance and check status

Scientific inputs were the supervisor's canonical extension prompt and the
following two complete files, read in full:

- `ORACLE_FINITE_HORIZON_BOUND.md`, SHA256
  `bfe32ba200b980f088846f5c9e902f08e6e740219368b6cbbfc19616029f16c1`.
- `ORACLE_FINITE_HORIZON_CHECK.md`, SHA256
  `7dd393cb2c7ab117c60d6cd0fad15a02840e762ff48f0e4481b96b3f4cbbd009`.

No other study artifact, established scientific chapter, code, external
scientific reference, or another route's findings was read before sections
1--8 were completed. Shared workflow
instructions and the required `solve-math-rigorously` and
`investigate-conjectures` skills were read and applied, including the latter's
research-contract and adversarial-audit references. The scoped assignment
replaced ordinary author startup reading under the shared workflow.

The endpoint energy identities, finite-depth induction, compact-region
constants, and continuation argument are new derivations here. The permitted
old source supplies the original two-layer construction and its forward-only
projection method. This candidate has undergone author mathematical checks
but awaits supervisor reconciliation and a separate check before designation
as internally checked. No experiments or Git mutations were performed.

## 9. All orders for bounded activations and bounded slopes

This corollary was added after the original candidate froze at SHA256
`3d247c5051a35665c897cdd133ef43ecde166bd49ceffd6c0cde7b364cc78194`.
Its downward physical-bound idea was supplied by the supervisor after that
freeze and verified below. It is a collaborative addition, not an independent
discovery by this route. The supervisor also described a different endpoint
proof after the candidate was completed; that argument is not used here.

Assume additionally, for every layer, that both `phi_l` and `phi_l'` are
globally bounded. Retain `C^{1,1}_loc` regularity. Then both dense flow and
every closure order `P>=1` exist uniquely at every finite physical time, and
the bound (21) holds for every `P>=1`, with the constants specified below.
In particular this all-order result covers arbitrary fixed hidden depth with
tanh or logistic sigmoid activations. It does not require the slope itself
to be globally Lipschitz, only locally Lipschitz and globally bounded.

Fix a horizon `T` and put

    A_l=sqrt(n) sup_(u in R)|phi_l(u)|,
    G_l=sup_(u in R)|phi_l'(u)|,
    B=sqrt(||w_0||^2+nY^2 T),
    q=B A_H/n+Y,                 S=Tq,             ell=1+S.   (22)

Both systems have the same canonical readout equation. Regardless of closure
loss descent, it gives

    d||w||^2/dt=-4n mean_a(f_a-y_a)f_a
      =nY^2-4n mean_a(f_a-y_a/2)^2<=nY^2.                   (23)

Consequently `||w||<=B`, `rho<=q`, and `tau<=ell` on every local interval
under consideration. The next bounds are defined in downward layer order:

    B_H=B G_H,
    D_l=||W_l0||_F+(2/n)B_l A_(l-1)sqrt(ell S),    l=H,...,2,
    B_(l-1)=G_(l-1) D_l B_l,                      after each D_l,
    D_1=||W_10||_F+2B_1 X S.                               (24)

There is no circularity: `B_H` is already known from the readout, so `D_H`
is known before computing `B_(H-1)`, and so on.

For each internal layer, suppose the bounds on its later matrices have
already been established. They imply `||delta_la||<=B_l` pointwise and
`mean||b_la||^2<=B_l^2`. Its forward history obeys `||a_la||<=A_(l-1)`
without any bound on its earlier matrices. Projection contraction in (6)
therefore gives the closure bound

    ||W_lhat-W_l0||_F
       <=(2/n)[mean||b_la||_L2^2]^(1/2)
                [mean||a_la||_L2^2]^(1/2)
       <=(2/n)B_l A_(l-1)sqrt(tau(tau-1))
       <=(2/n)B_l A_(l-1)sqrt(ell S).                       (25)

For the dense flow direct integration of (1) gives the smaller bound
`(2/n)B_l A_(l-1)S`, since `integral_0^T rho<=S` and
`S<=sqrt(ell S)`. Thus `D_l` bounds both matrices. The backward recursion
then establishes `B_(l-1)`. Induction gives all internal bounds in (24),
and the first-layer equation yields

    ||W_1dot||_F<=2rho B_1X,
    ||W_1(t)||_F<=||W_10||_F+2B_1XS=D_1.                    (26)

These bounds hold on each existing segment, for every `P`. The moment bounds
(20), together with (22)--(26), bound the whole finite raw state with
`tau>=1`. The same continuation argument as before excludes a finite maximal
existence time. Since `T` was arbitrary, every finite order exists globally.

Now use (13) and (16) with the constants `A_l,G_l,B_l,D_l,S,ell` in
(22)--(24), and use `B_w=B` in (17). For the local slope Lipschitz constants
in (17), take the compact intervals `[-Z_l,Z_l]` with `Z_1=D_1X` and
`Z_l=D_lA_(l-1)` for `l>=2`. Both solutions lie in the common compact
convex product of these physical block balls. Hence (17)--(19) apply
directly on `[0,T]`, with no first-exit threshold. This proves

    sup_(t<=T)||theta_hat_P(t)-theta_dense(t)||_*
       <=C exp(K_F T)/sqrt(P(P+1)),           every P>=1.     (27)

As before this is a compact-horizon estimate at fixed finite depth/width,
not uniform all-time accuracy. The all-order global existence in this
corollary is separate from the eventual-order theorem for unbounded
activations proved in sections 1--8.

## 10. Complete synthesis check and stronger integrated-defect consequence

After section 9 was frozen, the supervisor explicitly expanded this route's
allowed input scope to the complete `DEEP_ACTIVATION_ERROR_THEOREM.md`.
The route then read all 565 lines, sections 1--9, at SHA256
`57e6e16b9af6ea32dd3cbc266f1c5b9054ae63219ce8e191bffdb3b87f44d8dd`.
The pre-check version of this route, including section 9, had SHA256
`1c5ec6d148de4d131269f635da34f93ee917ab99e44d10f6061f549be1ad8e69`.
No other new scientific file was read. This is a collaborative mathematical
check by a contributing route author, not an isolated promotion review.

**Outcome: no required mathematical correction found in the complete
synthesis.** The principal requested coverage was its sections 1--5, including
the supervisor's distinct old-clock proof and the all-order corollary.
The following checks were performed by direct algebra and proof reconstruction:

- Canonical deep normalization and dense energy: the mobility operator's
  largest eigenvalue is `n`, giving the synthesis's Euclidean displacement
  `sqrt(nt)rho0` and its explicit containing ball. Forward/backward bounds,
  field and residual Lipschitz constants, and dense residual lower bound
  have the claimed dependencies.
- Old projection-energy identity: prefix jumps do not invalidate it; only
  square-integrable history is required. The synthesis's pointwise backward
  endpoint bound follows from evaluation norm `P/sqrt(tau)` and raw-history
  energy at most `tau B_l^2` in sample mean.
- In synthesis (18), sample Cauchy bounds `||E_l/rho||^2` by
  `4(P+1)^2 B_l^2 mean||e_a||^2/n^2`. Activity integration equals forward
  projection error energy, which is at most `A^2Z_(l-1)/(4P(P+1))`.
  The remaining ratio `(P+1)/P<=2` gives exactly its constant
  `2B_l^2A^2Z_(l-1)/n^2`. The layer induction (19) includes each factor
  of the incoming activation bound and matrix norm correctly.
- The stronger integrated-defect estimate (20), integral stability, and
  first-exit/continuation proof are valid. The bounded-activation/slope
  corollary's downward physical induction and all-order continuation agree
  with section 9 above; its looser `2A B_l a_(l-1)/n` increment bound is valid.
- New-clock regularity: the encoded backward responses start at layer two,
  so only those layers need the stated second-derivative regularity.
  The endpoint-product velocity cancels the dilation term before computing
  the response derivative, making the clock explicit. The positive dense
  residual lower bound and stopped compact set supply the derivative bound
  used for clock length.
- New-clock estimates: summed raw source energies include the matching
  prefix. They give the stated coarse total-variation bound and derived
  clock cap. Joint response `H^1` regularity, weighted best approximation,
  and `dmu<=dxi` give precisely its `L^2(L-1)/(4P(P+1))` energy bound and
  `1/(4nM)` integrated-defect factor. The fixed-order prefix Gram lower
  bound suffices for continuation and makes no order-uniform conditioning
  claim.
- Activation limitations: the ReLU delayed-departure example gives
  different absolutely continuous selected-field solutions, with a mismatch
  only at the departure instant. The SELU example's two one-sided velocities
  have the displayed strict inward signs, while its selected velocity at
  zero is nonzero. Applying the chain rule to `W_1^2` proves the claimed
  selected-field nonexistence. The conditional kink-free statements remain
  distinguished from an unconditional nonsmooth theorem.
- The implementation recurrences, ranks, storage, and stated per-action
  operation counts have the displayed dimensions and do not introduce
  future history or a dense trained correction.

The synthesis's stronger old integrated-velocity bound also follows directly
from this route's identities. Let `E_l=W_lhat_dot-F_l(theta_hat)`. Equations
(8), (12), and Cauchy--Schwarz over activity and samples give

    integral_0^t ||E_l||_F ds
      <=(2/n)[mean_a D_b_la(tau)]^(1/2)
               [mean_a D_a_la(tau)]^(1/2)
      <=ell B_l sqrt(S)J_(l-1)/(n sqrt(P(P+1))).              (28)

Summing gives `integral_0^T||E||_*<=C/sqrt(P(P+1))` with this route's
constant (16). Thus its earlier signed-accumulator estimate admits this
additional conclusion once endpoint energy is used a second time. This
does not assert a small pointwise velocity defect. The original permitted
two-layer source did not claim this stronger conclusion; it is justified
here by the newly derived online energy identity.

No experiments, software execution tests, or independent empirical checks
are part of this mathematical check. The synthesis's complete statements
are verified at the recorded hash; changing a statement or proof would
require a new check of the affected material.
