# Finite-depth response-speed closure for locally smooth activations

Frozen independent route, 2026-09-25. Author: scoped agent
`deep_new_clock`. This is a complete candidate proof, not a promotion review.
Its independent input scope was the three response-clock files listed at the
end and the supervisor's finite-depth model. No other route, study source,
experiment, external scientific source, or Git action was used. The supervisor
handled shared-checkout safety metadata. Only this file is owned by this route.

## 1. Claim and regularity

Fix finite integers H>=2, n,d,M>=1, finite training data (x_i,y_i), and finite
initial parameters theta0=(W1_0,...,WH_0,w0). Let z_i=x_i/sqrt(d), and define

    v1_i=W1 z_i, h1_i=phi1(v1_i),
    vl_i=Wl h(l-1)_i, hl_i=phil(vl_i), 2<=l<=H,
    f_i=w^T hH_i/n, r_i=f_i-y_i, rho=(M^-1 sum_i r_i^2)^(1/2).

Activations act componentwise, are defined on all of R, and satisfy

    phi1 in C^{1,1}_loc(R),
    phil in C^{2,1}_loc(R), 2<=l<=H.                 (1)

Here C^{k,1}_loc means k continuous derivatives with the kth derivative
locally Lipschitz. Requiring C^{2,1}_loc at every layer is a simpler sufficient
condition. No activation or derivative is assumed globally bounded. In
particular, all globally defined C^3 activations qualify, including polynomial
and exponential activations. Condition (1) is sufficient, not asserted necessary.
Ordinary ReLU is outside this classical theorem; specifying dynamics at its
kinks would be a separate issue.

Use unhalved mean squared loss rho^2 and stored-weight mobilities n for W1,w
and 1 for W2,...,WH. Compress each internal matrix Wl separately using its
forward/backward pair

    a_(l,i)=h(l-1)_i, b_(l,i)=r_i delta_(l,i)/rho,

the continuous matching prefix, one shared weighted Gram matrix, and the shared
clock

    L_dot=rho+||Psi_dot||_2, L(0)=1,
    Psi=stack_(l=2,...,H;i=1,...,M)(a_(l,i),b_(l,i)). (2)

The Euclidean norm in (2) is unscaled across all coordinates, layers and samples.
All responses are computed from the current reconstructed network.

Let ||theta||_* be the sum of Frobenius norms of its matrix blocks and the
Euclidean norm of w. For rho0>0 and every finite T>0, there are finite constants
P0(T), Lambda_T, C_T, K_T, depending only on the stated dimensions, activations,
data, initialization and T, such that for all integers P>=P0(T), the closure
has a unique regular solution on [0,T], its clock obeys L_P<=Lambda_T, and

    integral_0^T sum_(l=2)^H ||E_(l,P)(t)||_F dt
        <= C_T/[P(P+1)],
    sup_(0<=t<=T)||theta_hat_P(t)-theta_dense(t)||_*
        <= C_T exp(K_T T)/[P(P+1)].                 (3)

Here E_l is the exact velocity defect derived below. Thus this is unconditional
O_T(P^-2) tracking at fixed finite depth, width and data. If rho0=0, return the
stationary initialized network exactly without evaluating b. No future dense
trajectory is supplied to the closure or needed to define the constants.

The proof first obtains an initial-data compact ball for the dense flow from
gradient energy. On a stopped closure interval in a slightly larger ball,
endpoint projection energies bound total physical variation and then the clock.
The joint polynomial approximation estimate makes the defect small. Stability
then excludes both the physical-ball and residual exits, while the prefix Gram
bound excludes breakdown of the finite moment system.

## 2. Physical vector field and dense compactness

Define backward responses without the final factor 1/n:

    delta_(H,i)=w odot phiH'(vH_i),
    delta_(l,i)=phil'(vl_i) odot W(l+1)^T delta_(l+1,i), l=H-1,...,1.

The physical gradient field F is

    F1=-2 mean_i r_i delta_(1,i) z_i^T,
    Fl=-(2/n) mean_i r_i delta_(l,i) a_(l,i)^T, 2<=l<=H,
    Fw=-2 mean_i r_i hH_i.                          (4)

Let D be the diagonal block mobility operator (n,1,...,1,n). The metric norm

    ||v||_D^2=||v1||_F^2/n+sum_(l=2)^H||vl||_F^2+||vw||_2^2/n

satisfies ||v||_*<=kappa||v||_D, where kappa=sqrt(2n+H-1).
Since F=-D grad(rho^2), differentiation along the dense solution gives

    d(rho^2)/dt=-||F||_D^2,
    integral_0^t||F||_* ds <= kappa sqrt(t) rho0.    (5)

The last inequality is Cauchy--Schwarz in time and uses nonnegativity of the
loss. The field F is locally Lipschitz under (1). On every existing interval
of length at most T, (5) keeps the parameters in a fixed compact ball. F is
bounded there, so a solution approaching a finite maximal time has a limit
in parameter space; local existence from that limit extends it. Therefore
the dense solution exists uniquely on every finite horizon, even for unbounded
activations.

For the remainder fix T and put

    R0=kappa rho0 sqrt(T), R=R0+1,
    B={theta: ||theta-theta0||_*<=R}.

This convex compact set is specified entirely from initial data. Choose finite
constants on B as follows:

    alpha=sup_B ||D_theta(f_1,...,f_M)||_(* -> RMS),
    K=a Lipschitz constant of F from ||.||_* to ||.||_* on B,
    V=2 sup_B [mean_i ||D grad_theta f_i||_*^2]^(1/2),
    q=rho0+alpha R,
    mu=rho0 exp(-alpha V T)>0.                      (6)

RMS means Euclidean norm divided by sqrt(M), whereas D inside V is the
mobility operator. F is locally Lipschitz and B is convex compact, so a finite
K exists: cover B by finitely many local Lipschitz neighborhoods and subdivide
each line segment in B into pieces lying in those neighborhoods. All other
suprema in (6) are finite by continuity. Product estimates through the finite
network give such bounds using only local activation bounds on the finite
preactivation ranges induced by B.

Cauchy--Schwarz in the sample index, applied to
F=-(2/M)sum_i r_i D grad f_i, gives ||F||_*<=V rho. The output derivative
bound gives rho<=q on B and |rho(theta')-rho(theta)|<=alpha||theta'-theta||_*.
On the dense path,

    rho_dot >= -||r_dot||_RMS >= -alpha V rho.

Integrating up to any putative first zero and using continuity proves

    rho_dense(t)>=mu, 0<=t<=T.                     (7)

In particular the lower bound is valid without compatibility of the data or
eventual successful fitting.

## 3. Exact autonomous finite-depth equations

Let p=(p_0,...,p_(P-1))^T be shifted Legendre polynomials, e=(1,...,1)^T,
and let mathsfT have entries mathsfT_kk=k, mathsfT_kj=2j+1 for j<k and zero
for j>k. Then x p'(x)=mathsfT p(x).

At historical physical time s place the sample at xi=L(s) with mass rho(s)ds.
On [0,1] give mass dxi and constant histories equal to their initial values.
Write mu_t for this measure, A(t)=1+integral_0^t rho(s)ds for its mass, and
abar_(l,i), bbar_(l,i) for the extended histories. Store

    A_(l,i)=integral abar_(l,i)(xi) p(xi/L)^T dmu_t,
    B_(l,i)=integral bbar_(l,i)(xi) p(xi/L)^T dmu_t,
    G=integral p(xi/L)p(xi/L)^T dmu_t,
    C_(l,i)=b_(l,i)(0)a_(l,i)(0)^T.

The scalar A(t) and moment matrix A_(l,i) are distinguished by their indices.
The reconstruction is

    Wl_hat=Wl_0-(2/(nM))sum_i(B_(l,i)G^-1 A_(l,i)^T-C_(l,i)). (8)

Initialize A_(l,i)=[a_(l,i)(0),0,...], B_(l,i)=[b_(l,i)(0),0,...],
G=diag_k(1/(2k+1)), L=1, W1=W1_0,w=w0. Thus (8) equals Wl_0 initially.
The ODE is

    A_(l,i)_dot=rho a_(l,i)e^T-(g/L)A_(l,i)mathsfT^T,
    B_(l,i)_dot=rho b_(l,i)e^T-(g/L)B_(l,i)mathsfT^T,
    G_dot=rho ee^T-(g/L)(mathsfT G+G mathsfT^T),
    W1_dot=F1, w_dot=Fw, L_dot=g.                   (9)

Set a*_(l,i)=A_(l,i)G^-1e and b*_(l,i)=B_(l,i)G^-1e. Product
differentiation, using

    (G^-1)_dot=-rho G^-1ee^T G^-1
                  +(g/L)(G^-1mathsfT+mathsfT^T G^-1),

cancels all dilation terms separately for every layer. Consequently

    Vl:=Wl_hat_dot=-(2rho/(nM))sum_i
          [b_(l,i)a*_(l,i)^T+b*_(l,i)(a_(l,i)-a*_(l,i))^T],
    E_l=Vl-Fl=(2rho/(nM))sum_i
          (b_(l,i)-b*_(l,i))(a_(l,i)-a*_(l,i))^T.  (10)

Let Vphys=(F1,V2,...,VH,Fw). The explicit clock evaluation is

    g=rho+||D_theta Psi(theta_hat)Vphys||_2.         (11)

Thus no implicit velocity or clock solve is involved. Under (1), Psi is
C^{1,1}_loc on rho>0: forward maps have this regularity, and each delta_l
appearing in Psi uses activation derivatives only at layers l,...,H with
l>=2. Division by rho is smooth away from zero. The other factors in (9)--(11)
are locally Lipschitz when L>0 and G is symmetric positive definite. Hence
the full finite ODE is locally Lipschitz on this open domain and has a unique
local solution, by contraction of its integral equation on a sufficiently
short interval. In particular, merely assuming continuous second derivatives
would not by itself justify this local Lipschitz argument for the clock field.

On each regular interval the history integrals obey (9) with the same initial
conditions, so uniqueness for the resulting linear moment equations proves
their integral representations. The prefix gives G>0 because a nonzero
polynomial cannot vanish throughout [0,1]. Since g>=rho>0, the histories are
well defined in xi and

    dmu_t<=dxi, ||d(bar Psi)/dxi||_2<=1,
    d(bar Psi)/dxi=0 on (0,1).                     (12)

The two pieces match continuously at xi=1. In particular, the complete stacked
history is 1-Lipschitz; this is stronger than separate 1-Lipschitz bounds.

## 4. Endpoint energies and the clock bound before exits

For each vector history fbar=abar_(l,i) or bbar_(l,i), write M_f for its
moment matrix and Pi_t for weighted degree-<P polynomial projection. Put

    D_f=integral||fbar||_2^2 dmu_t-tr(M_f G^-1 M_f^T)
       =||fbar-Pi_t fbar||_L2(mu_t)^2.

The polynomial subspace in xi does not change with L, although its coordinates
do. With f*=M_f G^-1e, the product rule in (9) gives

    d/dt tr(M_f G^-1 M_f^T)=rho(2<f,f*>-||f*||_2^2).

Old history is fixed, so the first integral in D_f has derivative rho||f||².
The constant prefix has zero initial projection error. Therefore

    D_f(t)=integral_0^t rho(s)||f(s)-f*(s)||_2^2 ds. (13)

Using (10), the outer-product Frobenius norm, and Cauchy--Schwarz in time,

    integral_0^t sum_l||E_l||_F ds
      <=(2/(nM))sum_(l,i) sqrt(D_(a,l,i)(t)D_(b,l,i)(t)). (14)

This bounds the integral of the defect norm, not only its signed integral.

Temporarily stop at the first physical exit from B, residual crossing below
mu/2, maximal regular existence endpoint, or T. The following bounds hold
throughout the preceding interval without assuming a clock bound. Define

    A*=1+Tq,
    A_l=sup_(theta in B,i)||a_(l,i)||_2,
    D_l=sup_(theta in B,i)||delta_(l,i)||_2,
    eta_l=sup_(theta in B,i)||D_theta a_(l,i)||_(* -> 2),
    zeta_l=sup_(theta in B,i)||D_theta delta_(l,i)||_(* -> 2).

All are finite; the symbol A_l without a sample index is a scalar bound,
whereas A_(l,i) in (8)--(9) is a moment matrix. Since sum_i(r_i/rho)^2=M,
raw history energies satisfy

    sum_i D_(a,l,i)<=M A* A_l^2,
    sum_i D_(b,l,i)<=M A* D_l^2.

The matching prefix obeys the same bounds. Applying sample Cauchy--Schwarz
to (14) yields the coarse, order-independent bound

    integral_0^t sum_l||E_l||_F ds <= C0,
    C0=(2A*/n)sum_(l=2)^H A_l D_l.                (15)

Since theta_hat_dot=F(theta_hat)+(0,E2,...,EH,0),

    integral_0^t||theta_hat_dot||_* ds <= VTq+C0.   (16)

To bound normalized-response derivatives, put qvec=r/rho, so ||qvec||_2=sqrt(M)
and

    Dqvec[v]=(I-qvec qvec^T/M)Dr[v]/rho,
    ||Dqvec[v]||_2<=sqrt(M)alpha||v||_*/rho.

For each layer the product b_(l,i)=qvec_i delta_(l,i) then gives

    ||stack_i Db_(l,i)[v]||_2
        <=sqrt(M)(zeta_l+2D_l alpha/mu)||v||_*,
    ||stack_i Da_(l,i)[v]||_2<=sqrt(M)eta_l||v||_*.

Thus the following constants are independent of P:

    J={M sum_(l=2)^H[eta_l^2+(zeta_l+2D_l alpha/mu)^2]}^(1/2),
    Lambda=1+Tq+J(VTq+C0).                         (17)

Equations (2), (16) and (17) prove L(t)<=Lambda on the stopped interval.
The physical stop is the only device replacing globally bounded activations;
it will be removed, not retained as a theorem assumption.

## 5. The sharp joint projection estimate

For completeness, if F is a finite-dimensional vector H^1 function on [0,1],
write e_k=sqrt(2k+1)p_k and c_k=integral_0^1 F e_k. The differential identity

    -(x(1-x)e_k')'=k(k+1)e_k

and integration by parts give integral x(1-x)F'e_k'=k(k+1)c_k.
The functions e_k'/sqrt(k(k+1)), k>=1, are orthonormal in the weighted
derivative space. Bessel's inequality, applied componentwise and summed,
therefore yields

    sum_(k>=1)k(k+1)||c_k||_2^2
         <= integral_0^1 x(1-x)||F'(x)||_2^2 dx.

Polynomial completeness gives the ordinary projection error as the coefficient
tail. For the present Lipschitz functions, completeness also follows directly
from uniform Bernstein-polynomial approximation followed by L2 approximation.
For P>=1 the tail indices have k(k+1)>=P(P+1). Rescaling to [0,L] gives

    ||f-Q_P f||_L2(dxi)^2
        <= [P(P+1)]^-1 integral_0^L xi(L-xi)||f'(xi)||_2^2 dxi. (18)

Apply this to the entire stacked history bar Psi. Weighted best approximation
and dmu<=dxi allow the unweighted polynomial Q_P bar Psi as a comparator.
Because projection acts componentwise with the same G, its squared error is
the sum of all D_(a,l,i) and D_(b,l,i). Using (12) in (18),

    sum_(l,i)(D_(a,l,i)+D_(b,l,i))
         <= L^2(L-1)/[4P(P+1)].                    (19)

Since 2sqrt(xy)<=x+y, (14) and (19) give the slightly stronger constant
available from the shared unscaled clock:

    integral_0^t sum_l||E_l(s)||_F ds
        <= L(t)^2(L(t)-1)/[4nM P(P+1)]
        <= b/[P(P+1)],
    b=Lambda^2(Lambda-1)/(4nM).                    (20)

There is no missing layer factor: all layer/sample derivatives are charged
jointly in (12). Depth and sample count still affect Lambda, so (20) is not a
dimension-uniform assertion. Applying separate history bounds instead would
give the weaker but also valid numerator (H-1)L²(L-1)/(2n).

## 6. Closing the bootstrap and continuing the full state

Subtract the dense equation from the exact reconstructed physical equation.
The initial discrepancy is zero. On the stopped interval both states lie in B,
so (6) and (20) yield

    e(t):=||theta_hat_P(t)-theta_dense(t)||_*
        <= b/[P(P+1)]+K integral_0^t e(s)ds
        <= b exp(KT)/[P(P+1)].                     (21)

The final inequality follows by iterating the scalar integral inequality and
summing the exponential series. Choose P0>=1 so that

    P0(P0+1)>=b exp(KT) max(2,4alpha/mu).           (22)

For all P>=P0, (21) gives e<=1/2 and alpha e<=mu/4, including alpha=0.
Consequently

    ||theta_hat_P-theta0||_*<=R0+1/2<R,
    rho_hat_P>=rho_dense-alpha e>=3mu/4>mu/2.       (23)

Thus neither physical nor residual exit can occur first.

To exclude a finite regular-existence endpoint, fix P and use

    G(t)>=G_prefix(L(t)),
    G_prefix(ell)=integral_0^1 p(xi/ell)p(xi/ell)^T dxi,
    gamma_(P,Lambda)=min_(1<=ell<=Lambda)lambda_min G_prefix(ell)>0. (24)

Each prefix Gram is positive definite because its quadratic form is the integral
of a nonzero polynomial squared on an interval. Its entries are continuous in
ell; compactness gives strict positivity of the minimum in (24). This auxiliary
continuation constant may depend on P. It does not enter the error constants.

For fixed P, let B_P=max_(k<P,0<=x<=1)|p_k(x)|<infinity. Integral representations
and the stopped bounds give, for every column k,

    ||A_(l,i),k||_2<=A* A_l B_P,
    ||B_(l,i),k||_2<=A* sqrt(M)D_l B_P,
    |G_jk|<=A* B_P^2.

Together with (23), (24), 1<=L<=Lambda, and the physical bounds for W1,w,
these put the full finite state in a compact subset of its locally Lipschitz
domain. The vector field is bounded on a containing compact neighborhood.
Any finite maximal endpoint therefore has a limiting state in the domain and
extends by local existence. It cannot be the first stopping event.

The initial state is strictly inside both stops. Equations (23)--(24) exclude
every endpoint before T. This proves (3) with C_T=b, K_T=K and Lambda_T=Lambda.
All convergence constants and the order threshold are independent of P;
only the auxiliary fixed-order Gram continuation bound is allowed to depend
on P. The proof does not assume global existence for every small P.

## 7. Derivative evaluation, storage and autonomy

The directional derivative in (11) can be computed with finite forward and
backward passes, not a full Jacobian. With V1=F1, Vw=Fw and Vl from (10),

    v1_i_dot=V1 z_i, h1_i_dot=phi1'(v1_i) odot v1_i_dot,
    vl_i_dot=Vl h(l-1)_i+Wl_hat h(l-1)_i_dot,
    hl_i_dot=phil'(vl_i) odot vl_i_dot,
    r_i_dot=(Vw^T hH_i+w^T hH_i_dot)/n,
    rho_dot=(sum_i r_i r_i_dot)/(M rho).

The backward derivative pass, needed only down to layer 2, is

    delta_(H,i)_dot=Vw odot phiH'(vH_i)
                     +w odot phiH''(vH_i) odot vH_i_dot,
    delta_(l,i)_dot=[phil''(vl_i) odot vl_i_dot]
                      odot [W(l+1)_hat^T delta_(l+1,i)]
                   +phil'(vl_i) odot
                      [V(l+1)^T delta_(l+1,i)
                        +W(l+1)_hat^T delta_(l+1,i)_dot],
    b_(l,i)_dot=(r_i_dot delta_(l,i)+r_i delta_(l,i)_dot)/rho
                    -b_(l,i)rho_dot/rho.

Concatenate a_(l,i)_dot=h(l-1)_i_dot and b_(l,i)_dot, obtain g, then return
(9). No phi1'' is used; this explains the asymmetric regularity in (1).
No derivative of g, loss Hessian, saved trajectory, or dense target state is
an input. The derivative of each learned internal matrix has rank at most 2M.

Both orientations of every reconstructed matrix are available directly:

    Wl_hat v=Wl_0 v-(2/(nM))sum_i
       [B_(l,i) solve(G,A_(l,i)^T v)-b_(l,i)(0)(a_(l,i)(0)^T v)],
    Wl_hat^T v=Wl_0^T v-(2/(nM))sum_i
       [A_(l,i) solve(G,B_(l,i)^T v)-a_(l,i)(0)(b_(l,i)(0)^T v)].

The evolving scalar-state count is

    nd+n+2(H-1)MnP+P(P+1)/2+1.

Fixed storage includes the data, (H-1)n² initial internal-matrix entries,
and 2(H-1)Mn prefix-vector entries. Per internal layer the learned correction
has rank at most min(n,M(P+1)). After one shared O(P³) Gram factorization,
pretransforming moment factors costs O((H-1)MnP²); one internal-matrix action
then costs O(n²+MnP). A full batch of M vectors at all internal layers costs
O((H-1)(Mn²+nM²P)), apart from forward-first-layer/outer operations and the
moment updates. Clock derivative passes add a bounded number of such passes
at each fixed depth. These are direct operation counts, not measured speedups.

The finite state, current data and fixed initialization determine the future
ODE, including its clock. Hence it is autonomous and restartable from that
state. Retaining only reconstructed weights and discarding moments would not
be the same restartable solver. No storage scales with elapsed time, but the
theorem does not assert width-independent memory or favorable Gram conditioning.

## 8. Scope, checks and provenance

This route establishes exact closure identities, local uniqueness under (1),
dense global finite-time existence, and sufficiently-large-P compact-time
tracking for the stated finite-depth construction. It does not establish
ordinary-ReLU dynamics, every-small-P global continuation, depth/width-uniform
constants, uniform all-time convergence, floating-point stability, or practical
acceleration. H=1 has no compressed internal matrix and reduces to the exact
dense flow. Prediction and finite-layer response discrepancies on any fixed
bounded input set follow from their local Lipschitz maps on B; they introduce
their own input-set-dependent constants.

The potentially circular points were checked directly: the clock cancels out
of every reconstructed matrix velocity; endpoint energy controls absolute
defect variation; dense energy supplies compactness without bounded activations;
both closure stops are removed; and bounded physical weights are supplemented
by a fixed-P Gram lower bound for continuation. The improved constant in (20)
uses the joint Euclidean monitor explicitly. These are author algebraic checks,
not an independent review of this finished candidate.

Scientific source files read completely, with frozen input hashes:

- RESPONSE_CLOCK_FULL_CLOSURE.md:
  `06560b5a53bbff5d0de7640ca2162f56d36ae25e7e57eb5b565505a951e8fa67`
- RESPONSE_CLOCK_QUADRATIC_ORDER_BOUND.md:
  `1744008b022c5a2f17cbdcd8e3575201e54b5e94178dd1c6bc27730c2a7c7661`
- RESPONSE_CLOCK_UNCONDITIONAL_BOUND.md:
  `dda4d7b386b13129f30a64e6012b553b6ba783c41ed932874d98a93788ca7027`

Required process inputs were RESEARCH_WORKFLOW.md Part 1, the
solve-math-rigorously and investigate-conjectures skills, and the latter's
research-contract, adversarial-audit and evidence-ledger references. The source
files' mentions of other artifacts were not followed. This candidate was frozen
before any other route findings were received.

## 9. Full adversarial check of the synthesis, original frozen version

After freezing the independent route above, the supervisor assigned a full
mathematical audit of DEEP_ACTIVATION_ERROR_THEOREM.md. This explicitly expanded
the input scope to that complete file. I read all 514 lines, including both
clock proofs, the activation boundary/counterexamples, implementability, and
provenance statements. The audited source hash was

    f580a58d90e2e107226d311f934af00b9556e8ef7634f0f23be254c35e568e2d

No other route report or additional scientific source was read. The check was
direct algebra, inequality, regularity, counterexample and continuation analysis;
no numerical experiment was run. This is a collaborative internal check, not
an isolated promotion review.

Verdict for the mathematical theorems: PASS. The entire original packet needs
one minor specification in its SELU counterexample before an unconditional
full-packet PASS: declare lambda>0, alpha>1 and the selected derivative
phi'(0)=lambda*alpha. Its displayed zero-velocity value assumes this selection.
This does not affect either smooth theorem or the SELU obstruction mechanism.

### 9.1 Coverage and attacks that did not reveal a defect

- Equations (1)--(4), conventions and edge cases: independently recomputed all
  loss/mobility factors, including the first/readout n mobilities and the 1/n
  factors at internal links. Euclidean block aggregation, rho0=0 stationary
  evolution, H=1, T=0 and P>=1 cases are consistent.
- Equations (5)--(8), finite representations: checked the old zero-backward
  prefix and new matching-prefix subtraction separately. Initial physical
  weights match. The one shared Gram matrix is valid because all layers and
  samples have the same coordinate and insertion measure. Old raw equations
  contain no inverse rho and remain locally Lipschitz at rho=0.
- Equations (9)--(11), endpoint identities: recomputed the inverse-Gram product
  cancellation and both projection-energy and matrix-velocity derivatives.
  In the old case G=tau diag(1/(2k+1)) has precisely the required derivative.
  The old backward prefix jump affects neither growing-integral derivatives
  nor the squared L2 error identity; it is never assigned an H1 estimate.
  The defect estimate controls the integral of its norm, not just its signed
  accumulated matrix. Summing internal-block norms safely bounds the ordinary
  Euclidean physical norm.
- Equations (12)--(16), compactness and constants: checked that the mobility
  operator's largest eigenvalue is n, giving the stated dense displacement
  sqrt(nT)rho0. Local C^{1,1} regularity of activations gives a locally Lipschitz
  loss gradient. The energy bound prevents finite escape without coercivity
  or bounded activations. The ranges R A_(l-1), forward bounds A_l, backward
  bounds B_l, residual bound q, velocity bound V and prediction-gradient bound
  a are all valid. The ball is convex, so the output derivative bound gives
  the asserted pairwise residual Lipschitz estimate. The dense residual bound
  mu=rho0 exp(-aVT) uses only the declared initial-data ball and excludes a
  first finite zero.
- Equation (17): checked the Legendre derivative Bessel argument, the
  P(P+1) tail index, scaling from [0,1] to [0,tau], and the factor 1/4. It is
  applied only to continuous forward histories with constant matching prefixes.
- Equation (18), the main old-clock attack: endpoint evaluation on degree-<P
  polynomials has norm P/sqrt(tau). Mean raw backward energy is at most
  (tau-1)B_l^2, so mean endpoint norm is at most P B_l. Cauchy--Schwarz in
  samples yields

      ||E_l/rho||_F^2
        <=4(P+1)^2 B_l^2 mean_a||a_la-astar_la||^2/n^2.

  Integrating with rho dt and using the endpoint-energy identity followed by
  (17) gives B_l² A² (P+1) Z_(l-1)/(n² P), bounded by the displayed
  2B_l² A² Z_(l-1)/n². The growth in the endpoint factor really cancels;
  there is no lost P, M or depth factor.
- Equations (19)--(21), old depth propagation: the first-layer derivative
  bound uses F1/rho only. At a deeper layer, the three terms are exactly the
  canonical internal velocity, its defect and the propagated previous-layer
  derivative. Squaring with factor three gives the stated recursion. It is
  triangular in depth, with no unresolved derivative energy at the current
  layer on the right. Combining forward derivative energy with the raw
  backward energy S B_l² gives the stated B_old. Gronwall then excludes the
  physical-ball exit. No uniform residual floor is needed: at rho=0 every
  old raw-state velocity is zero, and local uniqueness excludes first arrival
  at such an equilibrium from a positive-residual state. Bounded moments and
  tau>=1 suffice for continuation even at the raw-field zero-residual boundary.
- Equations (22)--(26), new depth propagation: Psi is C^{1,1}_loc on rho>0
  under precisely the asymmetric assumptions given. Its derivative never
  calls phi1''. The coarse energy bound and resulting physical variation
  bound precede and establish the clock bound; there is no assumed clock cap.
  The full stacked history has joint derivative norm at most one, so the
  sum of all squared projection errors has the constant in (24). Applying
  2sqrt(xy)<=x+y to (11) gives exactly 1/(4nM) in (25). The two smallness
  requirements in (26) exclude both stops; a=0 is handled without division.
  For each fixed P, prefix positivity uniformly over 1<=L<=Lambda plus bounded
  moments places the full raw state in a compact subset of the locally
  Lipschitz domain. A P-dependent Gram lower bound is sufficient and does not
  contaminate the P-independent tracking constants.
- Section 7, computational closure: checked every forward and backward
  directional derivative, including transpose placement, the residual/RMS
  derivative and the normalized source quotient rule. Each internal velocity
  can be computed before the clock because dilation cancels separately in
  every layer. Rank and state counts, the one shared O(P³) factorization,
  moment-factor solves, O(n²+MnP) actions and prefix-sum dilation costs are
  consistent. The claims are operation counts rather than speedup or numerical
  stability assertions, and the retained initialized dense matrices are not
  hidden from the storage discussion.
- Section 8, smooth activation scope: the listed globally smooth scalar
  activations satisfy the sufficient hypotheses; no boundedness or temporal
  analyticity is used. Different activations at different layers are allowed.
  The general theorem is explicitly not claimed for literal ReLU/SELU.
- Section 8, nonsmooth history attack: bounded selected slopes and absolutely
  continuous existing trajectories suffice for the old forward chain rule
  almost everywhere. On a level set of a preactivation at its kink, that
  preactivation's derivative is zero almost everywhere, so the selected
  bounded slope does not invalidate this use of the chain rule. This does not
  restore unique physical dynamics or stable comparison. For the new clock,
  response jumps really defeat the asserted H1/Lipschitz history premise;
  the derivative integral does not charge such jumps.
- Section 8, ReLU counterexample: directly recomputed the zero selected
  velocities at (W1,W2,w)=(1,0,1). The positive-region polynomial field has
  initial middle-weight derivative 2 and its solution enters the positive
  region immediately. It satisfies the selected ODE almost everywhere after
  departure. Arbitrary waiting before departure produces distinct absolutely
  continuous solutions. The text properly distinguishes this from a classical
  derivative-at-every-time claim and from almost-sure Gaussian initialization.
- Section 8, SELU counterexample: with positive lambda, alpha>1 and left-slope
  selection at zero, directly recomputed the three limiting velocities as
  a^H(1-q), b^H-q a^H and a^H-q b^H. Their strict signs hold for all nearby
  positive upper weights/readout. An absolutely continuous candidate would
  obey d(W1²)/dt<=0 almost everywhere and therefore remain at W1=0, forcing
  all other weights to remain fixed and contradicting the nonzero selected
  W1 velocity. From a sufficiently small positive W1, the velocity is bounded
  strictly negatively while the other coordinates remain in the same small
  neighborhood, so the obstruction is reached in finite time. This is not a
  differential-inclusion claim.
- Section 8, conditional fixed-branch statement: a compact dense path with
  positive kink margin has a small neighborhood in which every sample/neuron
  branch is fixed. A smaller uniform tube allows pairwise derivative/Lipschitz
  estimates on the straight segment from the dense state to the nearby closure
  state, even though the whole tube need not be convex. Replacing the unit
  distance margin by this tube radius closes the same stop. The result remains
  conditional and does not supply a general crossing theorem.
- Section 9 and scope statements: reviewed their consistency with the
  self-contained argument. No claim about another route's actual provenance,
  past experiment, or earlier artifact was independently verified outside the
  assigned scientific input scope. These metadata limitations do not leave a
  mathematical dependency of the displayed proof unexamined.

### 9.2 Required minor clarification of the original source

At original lines 460--464, explicitly specify the SELU parameters and the
selected derivative at zero, for example:

    Take standard SELU with lambda>0, alpha>1 and selected phi'(0)=lambda*alpha.

The displayed value a^H(1-q) then has an explicit standalone hypothesis.
Without the selection, the exact boundary value is not fixed by the two
one-sided slopes. A zero derivative selection would remove this particular
existence obstruction at the zero state; a positive right-slope selection
would preserve the obstruction but change the displayed boundary value.
The issue is therefore a minor missing specification of the example, not an
algebraic error and not a defect in either smooth-activation theorem. A
final-hash check after this edit is needed to attach full-packet PASS to the
revised source.

### 9.3 Complete reread and final-hash outcome

The supervisor then explicitly authorized the revised synthesis, including a
new old-clock all-P corollary. I reread the complete 565-line file, not only the
edited passages. Its final reviewed SHA256 is

    57e6e16b9af6ea32dd3cbc266f1c5b9054ae63219ce8e191bffdb3b87f44d8dd

Verdict: full mathematical PASS, with no unresolved required correction.
The original finding and its original hash above are preserved. The revised
activation discussion now explicitly states lambda>0, alpha>1,
ReLU'(0)=0 and SELU'(0)=lambda*alpha, resolving the missing specification.
The unchanged old/new main arguments retain the checks recorded in section 9.1.

The added bounded-activation/bounded-slope corollary was checked separately:

1. From the unchanged readout equation,

       d||w||²/dt=-4n mean_a (f_a-y_a)f_a
                 =nY²-4n mean_a(f_a-y_a/2)².

   Thus B_w, q, S and A bound both dense and old-closure trajectories on every
   existing segment, independently of all internal weights and P. Only the
   global bound on the final activation is needed at this first step.
2. For link l, projection contraction and Cauchy--Schwarz over both history
   and samples give an old learned-increment bound

       (2/(nM)) sqrt([M(tau-1)B_l²][M tau a_(l-1)²])
          =2B_l a_(l-1)sqrt(tau(tau-1))/n
          <=2A B_l a_(l-1)/n.

   The backward prefix is zero, while the forward prefix contributes its
   unit length. This exactly matches the corollary's D_l. Integrating the
   dense gradient component gives the stated smaller 2S bound.
3. The descending induction starts with delta_H bounded by B_w s_H.
   Bounding W_l uses this already available B_l and the globally bounded
   incoming activation, not an unbounded lower matrix. Then
   ||delta_(l-1)||<=s_(l-1)D_l B_l provides the next backward bound.
   The dependency is strictly downward and contains no circular bootstrap.
   Finally the uncompressed first-layer equation gives
   ||W1||<=||W1_0||+2SXB_1.
4. The resulting parameter region can be taken to be the product of these
   closed block norm balls, hence compact and convex. Every moment is bounded
   by its raw history on tau in [1,A]. For each fixed P this places the old
   raw state in a compact subset of tau>0. The field is locally Lipschitz even
   at rho=0, so continuation gives all finite times for every P>=1.
5. In the forward derivative-energy recursion, replace A_l by the global
   a_l, keep the newly obtained B_l, and replace the propagated-weight factor
   R² by D_l² at layer l. The endpoint estimate still cancels (P+1)/P<=2.
   The resulting Zbar_l and defect constant are finite and independent of P.
   A uniform Lipschitz constant for F on the common convex parameter region
   then yields (2) for every P>=1 without an exit threshold.

The corollary still requires the old theorem's C^{1,1}_loc regularity in
addition to global boundedness of phi and phi'. It does not assert all-small-P
regularity for the new clock. The final candidate states both restrictions.
No numerical performance, nonsmooth-crossing, population, or depth-uniform
conclusion was used to obtain this PASS. No experiment, code implementation,
external source retrieval, modification of the synthesis, or Git action was
performed by this reviewer.
