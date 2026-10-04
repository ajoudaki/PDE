# Initial information, response widths, and stable scalar loss dynamics

Status: independent information route; frozen before comparison, 2026-09-30.
Scope: the study README's exact q=1 finite-data equations, the current manuscript's
setting and response-memory construction, and maintained observable-closure
sections on finite moments and autonomous initialized dictionaries. No other
study or route was read. No training experiment was run. This is an internally
proved route, not established book material or a proof of the requested q=1
scalar compression.

The main conclusion is that terminal stabilization is useful only after one
has controlled the finite evaluator's response error. Arbitrarily many initial
loss derivatives, even together with strong and matching terminal stability,
do not supply that control. Conversely, an explicitly evaluable initialized
response expansion of algebraic order better than one half would suffice for
an all-time scalar saving in the monotone scalar setting below. Its existence
for the actual q=1 flow is the unresolved bridge. There is also a q=1-specific
reason not to turn generic moment nonclosure into an information lower bound:
for fixed finite data, the data Gram and labels already determine the entire
random training-curve law.

## 1. Exact q=1 reduction: the data Gram is a complete source parameter

Write X for the d-by-m matrix whose columns are x_a/sqrt(d), and G=X^T X.
Let Z=AX, with column z_a, and use the study's variables w,v_a,k_a,tau and
its actual fixed W0. Then the exact closed finite-width training equations are

    h_a=tanh(z_a), B=W0+(mn)^(-1) sum_b v_b k_b^T,
    g_a=tanh(B h_a), f_a=n^(-1) w^T g_a, r_a=f_a-y_a,
    d_a=w odot (1-g_a^2), ell_a=(1-h_a^2) odot B^T d_a,
    zdot_a=-(2/m) sum_b r_b G_ab ell_b,
    wdot=-(2/m) sum_b r_b g_b,
    vdot_a=-2 r_a d_a, kdot_a=(rho/tau)(h_a-k_a), taudot=rho.

The moving training state has n(3m+1)+1 entries. Its frozen mixer still has
n^2 entries; this reduction does not solve the desired scalar problem.

**Proposition 1.** For any fixed width n, Gaussian A and Gaussian W0 as in the
study, the law of the complete q=1 training trajectory depends on the dataset
only through (G,y), with n fixed. Consequently, if that trajectory's loss
converges to a deterministic population loss, the limit is a function of
(G,y,t). This assertion requires neither independent inputs nor nonsingular G.

**Proof.** Multiplying the exact Adot equation on the right by x_a/sqrt(d)
gives the displayed zdot equation, so components of A outside the input span
never enter training predictions or their evolution. Each initial row of Z is
Gaussian with mean zero and covariance G; the rows are independent, and Z is
independent of W0. This remains valid for singular G. The other initial values
are w=v=0, k_a=tanh(z_a), tau=1. Equal G and y therefore give the same initial
law for the same autonomous finite-dimensional vector field. Local uniqueness
holds because tanh is smooth, the residual norm is Lipschitz, and tau>=1.
The manuscript's bounded-activation fixed-q continuation gives the trajectory
on every compact physical interval. Equal initial laws hence yield equal path
laws. If two such laws converge to deterministic losses, their limits agree.
Every occurrence of B^T uses the transpose of the same B; W0 is never resampled.
QED.

This proposition identifies source information, not an algorithm for evaluating
its consequence. Computing G costs O(dm^2) operations and O(m^2) storage; labels
add m entries. A square root of G can generate the initial row law in O(m^3)
preprocessing, including singular G. None of these operations computes a
population training curve. In particular, a lower bound over arbitrary initial
neuron laws cannot be transferred to this fixed Gaussian class without a
separate embedding theorem. For a realized finite-width path, the random Z and
W0 realization remains additional information; the proposition is about its
law, and the deterministic-limit statement is conditional.

## 2. Sharp initialized-linear-information theorem

This theorem quantifies the gap that exact finite-moment nonclosure leaves
open. It is applicable to a declared initialized kernel interface. It is not
a theorem that q=1 loss is linear in its neuron initialization law.

Let K be compact, let psi_1,...,psi_J and phi be continuous real functions on K,
and put V=span{1,psi_1,...,psi_J}. An initializer retains only
I(mu)=(integral psi_j dmu)_j from an arbitrary probability law mu on K.
An arbitrary deterministic decoder D estimates integral phi dmu from I(mu).
Then

    inf_D sup_mu |integral phi dmu-D(I(mu))|
        = dist_infinity(phi,V).                                      (1)

The supremum can already be witnessed by two finitely supported laws. For a
family phi_z with the query z supplied to the decoder, the same minimax error
is sup_z dist_infinity(phi_z,V). This is an exact information radius, not merely
a sufficient linear-decoder error estimate.

**Proof.** A best uniform approximant v in V exists: a minimizing sequence is
bounded in the finite-dimensional normed space V, so it has a convergent
subsequence. Write delta=||phi-v||_infinity. Integrating v gives an affine
function of I(mu), proving the upper bound. If delta=0 the lower bound is
immediate. Suppose delta>0, and choose a basis b=(1,b_1,...,b_s) of V. On the
compact extremal set E={x:|phi(x)-v(x)|=delta}, put
s(x)=sign(phi(x)-v(x)).

Zero lies in the convex hull of {s(x)b(x):x in E}. To see this, otherwise the
point of that compact convex hull nearest zero gives a separating vector c
with c dot s(x)b(x)>0 uniformly on E. Continuity preserves the sign and a
positive lower bound on a neighborhood of E. On its compact complement the
approximation error has a strict gap below delta. Thus adding a sufficiently
small positive multiple of c dot b to v decreases the uniform error, a
contradiction. Compactness of the convex hull follows in finite dimension;
explicitly an affine dependence removes points from any convex combination
until at most s+2 remain, so it is the continuous image of a compact collection
of coefficients and at most s+2 points.

Consequently there are finitely many x_i in E and alpha_i>=0 with sum alpha_i=1
and sum alpha_i s(x_i)b(x_i)=0. The constant coordinate gives equal total
positive and negative weights, each 1/2. Define

    mu_+=2 sum_{s(x_i)=+1} alpha_i delta_{x_i},
    mu_-=2 sum_{s(x_i)=-1} alpha_i delta_{x_i}.

Their I values agree. Their phi integrals differ by 2 delta, since the v
contribution vanishes and s(x_i)(phi(x_i)-v(x_i))=delta. Any decoder at the
common input has error at least delta for one law. This proves (1). For the
family, apply this lower bound at each fixed z, and the individual best
approximants give the matching upper bound. QED.

The family version alone does not produce an acceptable finite ODE: its
best-approximant coefficients could still require an infinite evaluator as
z changes. The operational condition is a supplied finite formula

    phi_z(xi) approximately c_0(z)+sum_{j=1}^J c_j(z) psi_j(xi),        (2)

with a certified uniform remainder, a finite program for c_j, and a declared
cost and provenance for the initialized psi_j integrals. Pointwise existence
of best approximants is weaker than (2).

## 3. Terminal stability and any finite jet order leave a fixed error

The following is a sharp counterexample to a proposed proof principle, not a
counterexample inside the q=1 network class. It survives the objection that a
smooth compactly supported bump is not analytic.

**Proposition 2.** For every integer J>=0 and fixed eta>0, there are two scalar
autonomous real-analytic vector fields on a neighborhood of [0,1], with common
initial loss 1, such that:

* both losses are positive, strictly decrease, and obey L(t)<=exp(-t);
* their initial physical-time derivatives agree through order J;
* their vector fields have the same derivatives at the terminal equilibrium
  zero through order J, including stable derivative -1;
* their loss curves have a separation at a fixed physical time bounded below
  by a positive constant depending only on eta, independently of J.

**Construction and proof.** Put p=J+1, and for 0<=u<=1 define

    U_p(u)=[2(1-u)]^p / ([2(1-u)]^p+u^p),
    D_p(u)=(2u)^p / ((2u)^p+(1-u)^p),
    b_p(u)=U_p(u)D_p(u).

The denominators are positive on [0,1], so each b_p is real analytic on an open
neighborhood of that interval. It satisfies 0<=b_p<=1, vanishes to order p at
both endpoints, and satisfies b_p>=1/4 on [2/5,3/5]. The last claim holds because
both numerator-to-other-term ratios are at least one on [1/3,2/3]. Consider

    Ldot_0=-L_0,                    L_0(0)=1,
    Ldot_1=-L_1[1+eta b_p(L_1)],     L_1(0)=1.                       (3)

The coefficient lies between 1 and 1+eta. The interval (0,1] is forward
invariant, and integration of the logarithmic derivative gives
exp(-(1+eta)t)<=L_1(t)<=exp(-t). Thus the solution is global and zero is stable.
At u=1 the vector fields differ by a function with a zero of order p. Successive
time differentiation of Ldot=F(L) shows that the kth time derivative at zero
uses only F,...,F^(k-1) at L=1. Hence initial time derivatives agree through
order p, more than required. At u=0 the vector fields differ by O(u^(p+1)), so
their terminal derivatives agree through order p.

Let t_*=log(5/2), the time at which L_0 reaches 2/5. The time at which L_1
reaches the same level is

    t_1=integral_(2/5)^1 du/[u(1+eta b_p(u))].

The advance Delta=t_*-t_1 obeys

    Delta=integral_(2/5)^1 eta b_p(u)/[u(1+eta b_p(u))] du
          >= [eta/(4+eta)] log(3/2) =: Delta_* >0.

After t_1, L_1 decays at rate at least one, giving

    L_0(t_*)-L_1(t_*) >= (2/5)[1-exp(-Delta_*)] =: c_eta >0.         (4)

This proves every claim. QED.

Any decoder using only the first J initial loss derivatives and the first J
terminal vector-field derivatives receives the same data on this pair. Its
worst-case uniform loss error is at least c_eta/2. Thus there is no rate at all
uniformly over this analytic stable class from that information alone. The
complex neighborhoods on which b_p remains controlled can shrink with p;
real analyticity without a uniform analytic norm or radius does not fix this.
The result does not exclude richer initialized observables, a fixed specific
analytic equation, or a q=1-specific uniform regularity theorem.

## 4. A finite initialized response expansion does give an all-time result

This constructive theorem isolates precisely the quantitative bridge needed
by an initialized-scalar strategy. It does not suppose that (3), or any other
scalar coefficient equation, is already a closure of q=1.

Let mu be an initialized probability measure on K and consider

    Ldot=-L a_mu(L), L(0)=L_0>0,
    a_mu(u)=integral phi_u(xi) mu(dxi), 0<=u<=L_0.                   (5)

Assume phi_u(xi) is continuous and Lipschitz in u uniformly in xi, and
kappa<=phi_u(xi)<=Lambda for known 0<kappa<=Lambda. Suppose (2) is supplied
with Lipschitz finite-program c_j, and uniform error at most delta<kappa.
Save M_j=integral psi_j dmu, and define

    a_J(u)=clip_[kappa,Lambda](c_0(u)+sum_j c_j(u)M_j),
    Ldot_J=-L_J a_J(L_J), L_J(0)=L_0.                              (6)

These are one moving scalar and J frozen initialized coefficients, with a
restartable finite evaluator. The clipping is Lipschitz, preserves the
coefficient bounds, and cannot increase its error against a_mu. Both flows
exist globally and preserve (0,L_0]. Their all-time physical-loss error obeys

    sup_(t>=0) |L_J(t)-L(t)|
       <= [Lambda L_0/(e kappa)] delta/(kappa-delta).               (7)

**Proof.** Both coefficients are positive, so L is strictly decreasing from
L_0 onto zero. There is a unique increasing time change s(t) with
L_J(t)=L(s(t)). Differentiation gives

    s'(t)=a_J(L_J(t))/a_mu(L_J(t)),
    1-delta/kappa<=s'(t)<=1+delta/kappa.

Put q=delta/kappa<1. Then |s(t)-t|<=qt and min{s(t),t}>=(1-q)t. Since
|L'(v)|<=Lambda L_0 exp(-kappa v), the fundamental theorem of calculus gives

    |L(s(t))-L(t)|
       <=Lambda L_0 qt exp[-kappa(1-q)t].

The maximum of t exp(-bt) for b>0 is 1/(eb), proving (7). The comparison is
at equal physical t; the time change is only a proof device. QED.

If a constructible expansion has delta_J<=C J^(-s), with fixed
kappa,Lambda,L_0 and s>1/2, choosing J=O(epsilon^(-1/s)) gives total scalar
storage O(J)=o(epsilon^(-2)). Exponential decay of delta_J gives logarithmic
storage. The moving state of (6) alone is one scalar; the stated stronger
storage bound includes its J coefficients and assumes O(J) program storage.
For delta<=kappa/2, the constant in (7) is at most
2 Lambda L_0 delta/(e kappa^2).

There is no population integral in the moving vector field (6). If initial
moments are computed only approximately, and sum_j sup_u|c_j(u)| |M_j-Mtilde_j|
plus coefficient-program error is eta_init, replace delta by delta+eta_init.
This displays conditioning rather than hiding it. Initialization must supply
a certified algorithm for the J moments. For a known finite law with N atoms,
direct evaluation costs O(NJ) kernel evaluations, after which that law can be
discarded; for Gaussian initialization, Gaussian cubature cost depends on the
finite initialized-program dimension and regularity and is not bounded here.
The full coefficient-generation program and its integration work are additional
costs. An oracle specification of moments is not an implementation.

## 5. The exact unresolved q=1 bridge

Equations (5)-(6) are a mechanism test, not a replacement network. To apply them
to the study target one would need all the following, none supplied by the
scalar theorem:

1. A deterministic population q=1 target, or a stated finite-width comparison
   target with the relevant probability and width rate.
2. A reachable scalar coefficient representation with a uniformly positive
   decay coefficient. The q=1 response-memory system is not the exact gradient
   flow in its full saved coordinates, so monotone loss and fitting may not be
   imported from dense gradient flow. Defining a(u) retrospectively along one
   monotone loss curve would use future trajectory information and is forbidden.
3. A finite initialized response interface such as (2), constructed from G,y
   and finite joint Gaussian initialization programs. It must retain every use
   of W0 and its true adjoint and allow hidden features to move nonlinearly.
4. A quantitative uniform response-approximation rate, with coefficient
   conditioning and initialization cost. Density of an initialized dictionary
   gives no such rate. The maintained autonomous-observable construction keeps
   entire evolving laws and establishes no scalar cubature rate, and its proved
   canonical-GF scope is not this general-data q=1 flow.

A higher-dimensional residual/response system could replace scalar (5); then
one must prove its stability and response-source bound rather than assume the
one-dimensional order argument. Failure to scalarize monotonically would kill
this particular witness, not the existence of any finite scalar-state ODE.

The useful new boundary is precise. Propositions 1-2 and (1) are exact, and (7)
is an all-time theorem under its stated coefficient hypotheses. No all-time
q=1 approximation or o(epsilon^(-2)) q=1 cost is established. The highest-value
next proof obligation is a constructible response-family width bound with a
finite evaluator; terminal stability can then propagate it, while initial jets
and exact density arguments cannot substitute for it.
