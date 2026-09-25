# Fixed-depth response-memory convergence for smooth activations

Theory continuation, 2026-09-25. Root owns this synthesis and the corresponding
README entry. The user requests extension of the old and new clock theorems
to fixed finite depth and the activations considered in this study. This
continues the same closure investigation; no experiment or code change is
part of this work. The original two-layer proofs remain unchanged.

The conclusions below are finite-width, finite-data, exact gradient-flow
statements on every prescribed finite physical-time interval. Internal check
status and hashes are recorded in the README and scoped check reports.

## 1. The theorem and its boundary

Fix finite positive n,d,M, a fixed number H>=2 of hidden layers, arbitrary
finite data and initial arrays. Here H denotes depth and L the new clock;
this distinguishes the two uses of L in earlier notes. Activations may differ
between layers. Use no biases, scalar output, unhalved mean MSE, and canonical
mobilities (n,1,...,1,n). Compress every internal matrix W_l, 2<=l<=H, while
retaining every initialized matrix and its actual transpose exactly.

Let theta be the dense physical parameter vector. Use its ordinary Euclidean
norm, with Frobenius norms for the matrix blocks:

    ||theta||^2 = sum_(l=1)^H ||W_l||_F^2 + ||w||_2^2.       (1)

For every fixed finite T there are finite constants independent of P such
that the following statements hold.

* OLD CLOCK: If each phi_l is C^{1,1}_loc on R (continuously differentiable,
  with locally Lipschitz first derivative), the original zero-backward-prefix
  closure exists uniquely through T for every sufficiently large P and

      sup_(t<=T)||theta_hat_P(t)-theta(t)||
         <= C_old(T)/sqrt(P(P+1)).                         (2)

* NEW CLOCK: If phi_1 is C^{1,1}_loc and each phi_l, l>=2, is C^{2,1}_loc
  (twice continuously differentiable with locally Lipschitz second derivative),
  the matching-prefix, weighted-Gram response-clock closure exists uniquely
  and regularly through T for every sufficiently large P, has a P-independent
  clock bound L_P<=Lambda_T, and

      sup_(t<=T)||theta_hat_P(t)-theta(t)||
         <= C_new(T)/[P(P+1)].                            (3)

No global boundedness or global Lipschitz bound on the activations or their
derivatives is required. All constants depend only on the finite dimensions,
depth, dataset, initial arrays, T and activation bounds on explicitly bounded
preactivation intervals. Successful fitting, special input geometry, Gaussian
initialization and task compatibility are unnecessary. Any finite Gaussian
realization is included. Layer-dependent smooth activations are included.

If the initial residual RMS is zero, both constructions use stationary
evolution; the new normalized backward sources need not be evaluated.
If H=1, there is no compressed internal matrix and the closure is exactly
the dense system. T=0 is immediate.

The general theorems assert eventual-in-P existence on each fixed horizon.
They do not extend the earlier two-hidden-tanh theorem's all-P global
existence claim to this entire class. For bounded activations with bounded
first derivatives, however, the old clock retains all-P global existence
and the bound (2) for every P>=1; see the corollary in section 5.
Neither theorem asserts uniformity
as T, H, n or M grow, monotonic actual error in P, numerical accuracy or
useful practical constants. Smoothness here is a sufficient hypothesis,
not a claim that every excluded activation fails to admit any closure theorem.

## 2. Common deep network and histories

Put v_a=x_a/sqrt(d). The network and backward recurrence are

    z_1a=W_1 v_a, h_1a=phi_1(z_1a),
    z_la=W_l h_(l-1),a, h_la=phi_l(z_la), 2<=l<=H,
    f_a=w^T h_Ha/n, r_a=f_a-y_a, rho=sqrt(mean_a r_a^2),
    delta_Ha=w odot phi_H'(z_Ha),
    delta_la=phi_l'(z_la) odot W_(l+1)^T delta_(l+1),a.

The canonical field F has blocks

    F_1=-2 mean_a r_a delta_1a v_a^T,
    F_l=-(2/n) mean_a r_a delta_la h_(l-1),a^T, 2<=l<=H,
    F_w=-2 mean_a r_a h_Ha.                               (4)

For each internal link define its encoded forward and backward responses

    a_la=h_(l-1),a,  b_la=(r_a/rho)delta_la.              (5)

All closure responses are evaluated at its own current reconstructed network.
In particular no dense trajectory is an input to these definitions.

OLD: tau=1+integral rho dt, histories inserted at xi=tau(t) with dxi=rho dt;
prefix 0<=xi<=1 has a_la=a_la(0) and b_la=0. With shifted Legendre p_k,
retain H_lak=integral a_la p_k(xi/tau)dxi and U_lak=integral b_la p_k(xi/tau)dxi.
Their equations and reconstruction are

    H_lak_dot=rho a_la-(rho/tau)[kH_lak+sum_(j<k)(2j+1)H_laj],
    U_lak_dot=r_a delta_la-(rho/tau)[kU_lak+sum_(j<k)(2j+1)U_laj],
    W_lhat=W_l0-(2/(nM tau))sum_(a,k<P)(2k+1)U_lak H_lak^T. (6)

Initially H_la0=a_la(0), higher H moments and every U moment vanish.
Equations (6) do not divide by rho and are locally Lipschitz for tau>0
under the old theorem's activation assumptions. Outer blocks obey (4).

NEW: On rho>0 concatenate all encoded responses using ordinary, unscaled
Euclidean coordinates:

    Psi(theta)=stack_(l=2..H,a=1..M)(a_la,b_la),
    g=rho+||D Psi(theta_hat)[theta_hat_dot]||_2,
    L_dot=g, L(0)=1.                                     (7)

Place each actual history point at xi=L(t), but insert mass rho dt. Give
the prefix [0,1] Lebesgue mass and matching constants a_la(0),b_la(0).
Write dmu for the resulting measure, A=1+integral rho dt for its mass.
Then dmu<=dxi and A<=L. Put C_la=b_la(0)a_la(0)^T, retained by its vectors.

Let p=(p_0,...,p_(P-1))^T, e=(1,...,1)^T, and let the triangular matrix
mathsfT have entries T_kk=k, T_kj=2j+1 for j<k, zero above the diagonal.
Store H_la=integral a_la p^T dmu, U_la=integral b_la p^T dmu and the ONE
shared G=integral pp^T dmu, all with p evaluated at xi/L. Then

    W_lhat=W_l0-(2/(nM))sum_a(U_la G^-1 H_la^T-C_la),
    H_la_dot=rho a_la e^T-(g/L)H_la mathsfT^T,
    U_la_dot=r_a delta_la e^T-(g/L)U_la mathsfT^T,
    G_dot=rho ee^T-(g/L)(mathsfT G+G mathsfT^T).          (8)

Initialize H_la=[a_la(0),0,...], U_la=[b_la(0),0,...] and
G=diag_k(1/(2k+1)). The prefix subtraction gives W_lhat(0)=W_l0.

## 3. Exact energy identity at every link

Let Pi_t be the appropriate history projection and fstar its value at the
current endpoint. For any one encoded vector history f define

    D_f(t)=||f-Pi_t f||_L2(history measure)^2.

Every prefix is constant, hence D_f(0)=0. In the new construction, if B_f
is its moment matrix, its fitted energy is tr(B_f G^-1 B_f^T). The inverse
Gram derivative from (8), followed by the product rule, gives

    d/dt tr(B_f G^-1 B_f^T)
       =rho[2<f,fstar>-||fstar||^2].

All terms proportional to g/L cancel. The raw energy derivative is
rho||f||^2 because previously inserted history is fixed. Therefore

    D_f_dot=rho||f-fstar||^2,
    integral_0^t rho||f-fstar||^2 ds=D_f(t).            (9)

For the old construction take G=tau diag_k(1/(2k+1)); the same calculation
applies. Its backward prefix jump does not affect (9): the formulas only
require square-integrable history and differentiation of growing integrals,
not differentiation of the history values.

Differentiating each reconstructed product also cancels dilation and yields

    theta_hat_dot=F(theta_hat)+E,
    E_1=E_w=0,
    E_l=(2rho/(nM))sum_a(b_la-bstar_la)(a_la-astar_la)^T. (10)

Consequently, for both clocks,

    integral_0^t ||E_l||_F ds
       <= (2/(nM))sum_a sqrt(D_b,la(t)D_a,la(t)).       (11)

These energies and exact accumulators are proof devices; the algorithm
does not store them. The Euclidean norm of E is at most the sum of its
internal-block Frobenius norms.

## 4. Dense existence and an initial-data compact region

Let mathcalL=rho^2 and let mathcalD be the fixed mobility operator in (4).
It has largest eigenvalue n. Since F=-mathcalD grad mathcalL,

    mathcalL_dot=-||mathcalD^(-1/2)theta_dot||^2,
    integral_0^t ||theta_dot||^2 ds <= n rho0^2,
    ||theta(t)-theta0|| <= sqrt(nt)rho0.                (12)

For locally Lipschitz F, local solutions exist uniquely by contraction of
the integral equation. If a maximal endpoint were finite, the same energy
bound between any two times makes theta(t) Cauchy at that endpoint. Its
finite limit admits a new local solution. This proves global dense existence,
without global activation bounds. The argument also works for C^{1,1}_loc
activations because the differentiable loss has locally Lipschitz gradient.

Fix T>0 and the closed physical ball

    R=||theta0||+sqrt(nT)rho0+1,  B={theta:||theta||<=R}. (13)

Dense dynamics remain at least distance one from its boundary. All estimates
for a closure are first used only until its first exit from this ball.
For explicit finite bounds, set X=max_a||v_a|| and A_0=X. Recursively choose

    s_l=sup_(|z|<=R A_(l-1)) |phi_l'(z)|,
    A_l=sqrt(n) sup_(|z|<=R A_(l-1)) |phi_l(z)|,
    B_H=R s_H, B_l=s_l R B_(l+1), l=H-1,...,1.         (14)

Thus ||h_la||<=A_l, ||delta_la||<=B_l throughout B. Define

    Y=sqrt(mean y_a^2), q=R A_H/n+Y, S=Tq, A=1+S,
    v_1=2B_1 X, v_l=2B_l A_(l-1)/n (2<=l<=H), v_w=2A_H,
    V=sqrt(v_1^2+sum_(l=2)^H v_l^2+v_w^2),
    a=(1/n)sqrt((B_1 X)^2+sum_(l=2)^H(B_l A_(l-1))^2+A_H^2).
                                                               (15)

On B: rho<=q, ||F||<=Vrho and |rho(theta')-rho(theta)|<=a||theta'-theta||.
The last estimate follows by differentiating each f_a: its gradient blocks
are delta_1a v_a^T/n, delta_la h_(l-1),a^T/n and h_Ha/n, respectively.
Their squared norms sum to at most a^2, so the prediction RMS map is
a-Lipschitz on the convex ball. Taking a norm preserves this bound for rho.
Let K be any Lipschitz constant of F on B. F is locally Lipschitz under
the stated assumptions, so such a finite K follows from (14) and local
Lipschitz constants of phi_l'. All these constants concern an explicit ball,
not an unknown dense trajectory or a P-dependent closure trajectory.

For rho0>0, dense dynamics obey rho_dot>=-aVrho while rho>0, hence

    rho_dense(t)>=mu:=rho0 exp(-aVT)>0, t<=T.            (16)

A first zero would contradict this inequality and continuity.

## 5. Old clock: controlling deeper forward histories

On a regular closure segment inside B, its activity length tau<=A. A solution
with initially positive rho cannot reach rho=0 at a finite regular state:
every raw-state velocity vanishes there, and local uniqueness backward from
that equilibrium rules out a first arrival. We may therefore use xi=tau(t).
Primes in this section denote derivatives in xi. Forward histories have
constant prefixes. Define their mean derivative energies

    Z_l(t)=mean_a integral_0^tau ||h_la'(xi)||^2 dxi.

They are finite on every compact regular segment. The Legendre estimate is

    mean_a D_h,la(t)<=A^2 Z_l(t)/[4P(P+1)].             (17)

To recall its proof, on [0,1] the equation
-(x(1-x)p_k')'=k(k+1)p_k and integration by parts give orthogonal weighted
derivatives with norm squared k(k+1)/(2k+1). Bessel applied to f' bounds
the coefficient tail by [P(P+1)]^-1 integral x(1-x)||f'||^2. Parseval,
polynomial density and rescaling give (17), using x(1-x)<=1/4.

The crucial extra estimate controls the velocity of earlier compressed
matrices without differentiating their backward histories. Endpoint
evaluation of a polynomial of degree<P has L2(0,tau) norm P/sqrt(tau),
because sum_(k<P)(2k+1)=P^2. Projection contraction and
mean_a||b_la||^2<=B_l^2 therefore give

    (mean_a||bstar_la||^2)^(1/2)<=P B_l,
    (mean_a||b_la-bstar_la||^2)^(1/2)<=(P+1)B_l.

Put e_l=E_l/rho. By (10), Cauchy--Schwarz over samples, then (9),(17),

    integral_0^t rho||e_l||_F^2 ds
    <= [4(P+1)^2 B_l^2/n^2] mean_a D_a,la(t)
    <= 2B_l^2 A^2 Z_(l-1)(t)/n^2.                    (18)

Here (P+1)/P<=2 cancels the potentially growing endpoint factor. This is
why merely copying the two-layer forward-Lipschitz argument is insufficient,
and why no loss of rate with depth is necessary.

For layer one, ||h_1a'||<=s_1 v_1 X. For l>=2 the forward chain rule is

    h_la'=phi_l'(z_la) odot[(F_l/rho+e_l)h_(l-1),a
                                      +W_lhat h_(l-1),a'].

Using ||x+y+z||^2<=3(||x||^2+||y||^2+||z||^2), define the finite recursion

    Zbar_1=S(s_1 v_1 X)^2,
    Zbar_l=3s_l^2[ S v_l^2 A_(l-1)^2
       +(R^2+2B_l^2 A^2 A_(l-1)^2/n^2)Zbar_(l-1) ].   (19)

Equations (18) and the chain rule prove Z_l(t)<=Zbar_l by induction, starting
at l=1. The induction is triangular in forward depth: only derivative
energy from the preceding layer enters. The constants can grow rapidly
with H, but contain no P.

The old backward prefix is zero, so mean_a D_b,la<=S B_l^2. Equations
(11),(17),(19) now yield the stronger integrated-velocity estimate

    integral_0^t ||E|| ds <= B_old/sqrt(P(P+1)),
    B_old=(A/n)sum_(l=2)^H B_l sqrt(S Zbar_(l-1)).      (20)

In particular this bounds each signed accumulated matrix reconstruction
error. Subtracting the dense equation and iterating
e(t)<=B_old/sqrt(P(P+1))+K integral_0^t e(s)ds gives

    ||theta_hat_P(t)-theta(t)||
      <=B_old exp(KT)/sqrt(P(P+1)).                    (21)

Choose P large enough that this is <=1/2. It excludes the physical-ball
exit, since dense stays distance one from its boundary. For each fixed P,
the moment representations, bounded histories and tau in [1,A] bound all
raw state entries. The locally Lipschitz field remains in a compact subset
of tau>0, so a finite maximal endpoint has a limit and extends. This also
excludes loss of existence before T and proves (2). No residual stop or
closure loss-monotonicity hypothesis was used.

### All-P corollary for bounded activations with bounded slopes

Suppose additionally that every phi_l and phi_l' is bounded on R. Keep
the C^{1,1}_loc assumption. Then the old closure exists uniquely for every
finite time at every order P>=1, and (2) holds for every P>=1. This includes
tanh, sigmoid, arctan and bounded smooth periodic activations such as sine.

Here are the order-independent bounds that replace the physical-ball stop.
Write a_l=sqrt(n)||phi_l||_infinity, s_l=||phi_l'||_infinity,
Y=sqrt(mean y_a^2), and

    B_w=sqrt(||w0||^2+nY^2T), q=B_w a_H/n+Y,
    S=Tq, A=1+S, B_H=B_w s_H.

For both the dense and old closure, the unchanged readout equation gives

    d||w||^2/dt=nY^2-4n mean_a(f_a-y_a/2)^2<=nY^2.

Thus ||w||<=B_w, rho<=q and tau<=A on each existing segment through T.
Starting at l=H and proceeding DOWNWARD to l=2, set

    D_l=||W_l0||_F+2A B_l a_(l-1)/n,
    B_(l-1)=s_(l-1)D_l B_l.                            (21a)

Indeed projection contraction in (6), followed by sample and history
Cauchy--Schwarz, bounds the old increment by
2B_l a_(l-1)sqrt(tau(tau-1))/n<=2A B_l a_(l-1)/n. For dense dynamics
integrating (4) gives the smaller bound 2S B_l a_(l-1)/n. The backward
recursion then proves the next B_(l-1). There is no loop: the bound on
delta_l uses only already bounded upper matrices and the readout, and the
incoming activation has a global bound. Finally

    ||W_1||_F<=||W_10||_F+2SX B_1.

These bounds and the moment representations give compact continuation at
each fixed P, without an order threshold. On this common compact region
F has a finite Lipschitz constant independent of P. Repeat (17)--(20) with
global a_l,s_l, backward bounds B_l, and D_l in place of the earlier R
in the layer-l chain rule. The derivative-energy recursion and comparison
then yield (2) at every order. Constants still depend on T and depth.
No corresponding all-small-P assertion for the new clock is proved here.

## 6. New clock: bounded length and the quadratic rate

Stop the new closure while it lies in B and rho_hat>mu/2. Under the stated
activation assumptions, Psi is C^1 with locally Lipschitz derivative on
rho>0. Only phi_l'', l>=2, occur when differentiating the encoded backward
responses; phi_1'' is not needed. Thus there is a finite bound

    ||D Psi(theta)||_op<=J on B intersect {rho>=mu/2}.   (22)

This follows directly from compactness or from differentiating (5):
if qvec=r/rho, Dqvec=(I-qvec qvec^T/M)Dr/rho and ||qvec||=sqrt(M).
The remaining factors are bounded by (14) and local bounds on the first
two activation derivatives. The residual denominator is at least mu/2.

For a coarse estimate, set

    B_resp=M sum_(l=2)^H [A_(l-1)^2+B_l^2].

The sum of raw energies of all encoded histories is at most A B_resp,
including their matching prefixes: mean_a||b_la||^2<=B_l^2. By (11)
and 2sqrt(xy)<=x+y,

    integral_0^t ||E|| ds <= A B_resp/(nM)=:C0,
    integral_0^t ||theta_hat_dot|| ds <=VS+C0.

Therefore, on this stopped interval,

    L_P(t)<=Lambda:=A+J(VS+C0).                        (23)

This does not assume a clock cap. It derives one from the exact projection
energy identity and a compact physical region.

The entire concatenated history is 1-Lipschitz in xi, since
||dPsi/dxi||=||Psi_dot||/(rho+||Psi_dot||)<=1, and its prefix derivative
vanishes. Weighted best approximation, dmu<=dxi, and the unweighted
Legendre bound give the JOINT estimate

    sum_(l,a)(D_a,la+D_b,la)
       <= L^2 integral_0^L ||Psi_bar'(xi)||^2 dxi/[4P(P+1)]
       <= L^2(L-1)/[4P(P+1)].                         (24)

The ordinary Legendre projection is only a comparison polynomial; no
orthogonality under the weighted measure is assumed. Combining (11),(24),

    integral_0^t ||E|| ds
       <= L_P(t)^2(L_P(t)-1)/[4nM P(P+1)]
       <= B_new/[P(P+1)],
    B_new=Lambda^2(Lambda-1)/(4nM).                    (25)

Using the joint monitor saves a factor relative to separately bounding
every history by one. The displayed absence of an explicit depth multiplier
does not mean depth-independent constants: Lambda and J depend on H, M, n.

Comparison with the dense field gives

    ||theta_hat_P(t)-theta(t)||<=B_new exp(KT)/[P(P+1)]. (26)

Choose P so that its right side is at most 1/2 and its product with a is
at most mu/4. The first bound rules out the physical-ball exit. The second
gives rho_hat>=3mu/4, ruling out the residual exit. If a=0 the latter
inequality is automatic; no division by a is necessary.

For fixed P and L<=Lambda, the prefix bounds the Gram away from singularity:

    G >= integral_0^1 p(xi/L)p(xi/L)^T dxi,
    min_(1<=l<=Lambda)lambda_min integral_0^1 p(xi/l)p(xi/l)^T dxi >0.

Each matrix is positive definite because a nonzero polynomial cannot vanish
on an interval; continuity in l and compactness give the positive minimum.
All moment entries are bounded by their raw-history integrals and |p_k|<=1.
Together with the physical, residual and clock bounds, this places the
full state in a compact subset of its locally Lipschitz domain. The same
continuation argument as before excludes a finite maximal endpoint through T.
This proves (3) and the uniform clock bound, for all sufficiently large P.
The Gram lower bound may deteriorate with P; it is an existence argument,
not a numerical conditioning guarantee.

## 7. Implementability at depth H

The new clock is explicit, despite containing response derivatives. Solve
Gq=e once and form astar_la=H_la q, bstar_la=U_la q. Then

    V_l=W_lhat_dot=-(2rho/(nM))sum_a
                 [b_la astar_la^T+bstar_la(a_la-astar_la)^T].

These velocities contain no g. Compute V_1=F_1 and V_w=F_w, then the
directional forward pass

    z_1a_dot=V_1 v_a,
    z_la_dot=V_l h_(l-1),a+W_lhat h_(l-1),a_dot,
    h_la_dot=phi_l'(z_la) odot z_la_dot,
    r_a_dot=(V_w^T h_Ha+w^T h_Ha_dot)/n,
    rho_dot=mean_a r_a r_a_dot/rho.

Differentiate backpropagation in reverse layer order, for l>=2:

    delta_Ha_dot=V_w odot phi_H'(z_Ha)
                  +w odot phi_H''(z_Ha) odot z_Ha_dot,
    delta_la_dot=phi_l''(z_la) odot z_la_dot odot W_(l+1)^T delta_(l+1),a
       +phi_l'(z_la) odot [V_(l+1)^T delta_(l+1),a
                               +W_(l+1)^T delta_(l+1),a_dot],
    b_la_dot=(r_a_dot delta_la+r_a delta_la_dot)/rho-b_la rho_dot/rho.

Now evaluate g from the stack of a_dot,b_dot and return (8). Every matrix
and its transpose refer to the same current reconstruction. No implicit
solve for g, full Jacobian, loss Hessian or dense correction is required.

Both clocks use 2MnP(H-1) moving history entries and retain (H-1)n^2 fixed
initialized entries. The outer blocks add nd+n moving entries. Old adds
one clock; new adds one clock and P(P+1)/2 shared Gram entries, plus fixed
matching-prefix vectors. Each old learned correction has rank <=MP; each
new correction has rank <=M(P+1), including the prefix subtraction, capped
by n. New operator velocities have rank <=2M per link.

One shared Gram factorization costs O(P^3) per RHS, with factor solves
O((H-1)MnP^2). After these solves, a matrix or transpose action costs
O(n^2+MnP) per link per vector, including the initialized dense action.
Moment dilation uses prefix sums in O((H-1)MnP), and Gram dilation O(P^2).
Derivative passes add applications at each layer. Storage is independent
of elapsed steps. These are operation counts, not experimental performance
or finite-precision guarantees. The new deep solver has not been implemented.

## 8. Which activations are covered, and which are not

Tanh, logistic sigmoid and exact GELU from this study satisfy both smooth
hypotheses. GELU is unbounded, which is allowed. Arctan and its shifted/scaled
variants, softplus, SiLU, sine, affine and polynomial activations also satisfy
them as functions on R. Different admitted activations can be mixed by layer.
No temporal analyticity or convergent time-Taylor series is used.

Literal ReLU and standard SELU from the activation campaign are different:
their selected first derivatives jump at zero. ReLU has slopes 0 and 1;
SELU has one-sided slopes lambda*alpha and lambda, with lambda>0 and alpha>1. The study
selects ReLU'(0)=0 and SELU'(0)=lambda*alpha. Thus they
do not satisfy the smooth theorem. This is a substantive boundary:

1. The old history and defect algebra, including (9), remains meaningful
   for absolutely continuous selected-field trajectories with bounded
   backward histories. Indeed the forward-energy induction can be used
   on bounded existing segments with bounded selected slopes. The missing
   general step is uniqueness and stable comparison for the discontinuous
   physical field, not the backward-prefix jump or matrix reconstruction.

2. At a switch, delta_l and b_la can have a nonzero jump. A continuous clock
   xi=L(t) cannot turn that into a continuous history. The a.e. derivative
   integral in (7) ignores the jump; a derivative bound a.e. alone does not
   make a discontinuous history Lipschitz or H1. For example a step function
   has zero classical derivative a.e. and nonzero polynomial projection
   error. Thus the new argument (24) cannot be asserted across such switches.

3. Even the dense selected ReLU ODE can be nonunique at a kink. Take n=d=M=1,
   H=2, x=y=1 and initial W1=1,W2=0,w=1, with phi'(0)=0. All selected
   velocities vanish, so the constant state solves the ODE. In the all-positive
   region write a=W1,v=W2,c=w. Its smooth equations are

       (a_dot,v_dot,c_dot)=2(1-avc)(vc,ac,av).

   The solution of this polynomial field starting at (1,0,1) has v_dot(0)=2
   and remains all-positive for sufficiently small positive time. It also
   solves the selected ReLU ODE almost everywhere, with a possible mismatch
   only at its departure time. Delaying departure gives further absolutely
   continuous solutions from the same initial state. Hence an arbitrary-
   initialization theorem about a unique selected dense trajectory would
   already be false, before compression is considered. This example does
   not assert nonuniqueness almost surely under Gaussian initialization.

4. For the selected SELU equation even existence can fail. Take n=d=1,
   M=2, inputs +1,-1, targets 1,q with 1<q<alpha^H, W1=0 and all upper
   weights and readout equal to one. Write a=lambda*alpha and b=lambda for
   its left and right slopes. The selected W1 velocity at zero is
   a^H(1-q)<0. Its limits from W1>0 and W1<0 are respectively
   b^H-q a^H<0 and a^H-q b^H>0. These strict signs persist in a neighborhood
   of the full initial state. Any purported absolutely continuous solution
   there would have (W1^2)_dot<=0 a.e., hence W1=0 throughout a short interval.
   All upper weights then stay constant since their incoming activations
   are zero. This contradicts the selected nonzero W1 velocity. Thus no
   selected absolutely continuous solution starts there. Starting with W1
   sufficiently small and positive reaches such an obstruction in finite
   time; the other blocks remain close to one over that short interval.
   This checks the literal selected-field convention, not a differential
   inclusion which might allow sliding at the kink.

If a specified dense trajectory stays uniformly away from activation kinks
through T, its compact neighborhood has smooth fixed branches; applying
the same proof there gives both rates for sufficiently large P. The proof
uses a small tube, with the margin replacing the unit ball margin in the
stopping argument. The dense reference and closure then remain in the same
branches. This is a conditional kink-avoidance result, not general ReLU/SELU
coverage. More generally smoothness of the actual response maps on such a
neighborhood suffices even if a harmless inactive preactivation is zero.

Smoothing the activation gives a different, smooth target covered by the
theorem, with constants potentially diverging as smoothing vanishes. A
jump-aware clock or a selected differential-inclusion/event convention
would also change or supplement the present formulation. None is silently
substituted for the tested literal activation or proved here across all
switches. A broad nonsmooth tracking theorem remains open.

## 9. Sources, checks and scope of the continuation

Root read the complete old finite-horizon proof, complete new construction
and quadratic/unconditional proofs, complete three-layer derivation and
complete activation-general derivation in this study. Established inputs:
docs/NOTATION.md and finite_dynamics.md sections 1--3, including their full
gradient-energy and global-existence arguments. The proof above contains
the needed arguments, with the C^{1,1}_loc extension stated explicitly.
No other study's scientific contents or generated experiments were used.

Fresh scoped routes: deep_old_clock owns DEEP_OLD_CLOCK_ROUTE.md;
deep_new_clock owns DEEP_NEW_CLOCK_ROUTE.md; activation_scope owns
DEEP_ACTIVATION_SCOPE.md. Their allowed inputs and later check coverage are
retained in their reports. They initially saw only their selected older
source files and assignments, not one another's developments. Root derived
the endpoint-evaluation cancellation (18) separately while the old route
developed a different endpoint estimate. The new route also identified the
joint-monitor improvement in (24)--(25).

After the first complete candidates froze, root proposed the bounded-
activation/slope all-P corollary to the old route for an additional check.
This later exchange is collaborative and is recorded separately from the
independent initial derivations. Root read all three complete route reports.

This is theory internal to the study, not promotion into established docs.
No training, solver implementation, maintained-source edit or Git-index
mutation is part of the continuation. Results concern closure order at
fixed width and depth; no population or infinite-depth limit is implied.
