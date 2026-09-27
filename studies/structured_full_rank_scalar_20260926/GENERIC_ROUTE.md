# Independent-sign route: exact bounds and a conditional scalar theorem

Scope: the complete model in this study's README, required proof/research
skills, and the primary external source identified below. No other study,
route artifact, archived book, experiment, or target trajectory is an input.

Status: the requested independent-sign theorem is **not proved**. This route
proves global finite-width well-posedness and dimension-independent bounds,
then reduces general-data scalar existence to a precise reachable-field
tail estimate. Section 6 gives a complete unconditional scalar-existence
theorem for one training sample, retaining the original independent
central signs. Neither construction proves a polynomial size/error
relation. The general-data tail estimate cannot be replaced by
orthogonality alone.

## 1. Exact sign gauge and convolution structure

Write n=2^b and index neurons by G=(Z/2Z)^b, with
H_{xs}=n^{-1/2}(-1)^{x dot s}. Set K=H D2 H. Define

    w'=D3 w, c'=D1 c, A'_k=D1 A_k, B'_k=D3 B_k.

Since tanh is odd and its derivative is even, the primed equations have
exactly the same form with

    W'=D1 W D3=K-2/(m n L) sum_k (2k+1) A'_k B'_k^T.

Every output, residual, loss and L is unchanged. Conditional on the signs,
the primed initial w and c still have their original independent centered
Gaussian laws. Thus the outer signs can be eliminated without weakening the
central independent-sign model. Below primes are omitted.

If epsilon_s are the central signs, then

    K_{xy}=kappa_{x+y},
    kappa_z=(1/n) sum_s epsilon_s (-1)^{z dot s},
    K^T=K, K^2=I, K 1=epsilon_0 1.

For a multiplication operator M_v=diag(v),

    (H M_v H)_{st}=(H v)_{s+t}/sqrt(n).

Consequently a word K M_v K retains the spectral signs on both sides of a
nontrivial convolution. The identity K^2=I cancels adjacent K's only; it
does not collapse arbitrary nonlinear forward/backward reuse.

## 2. Deterministic bounds uniform in n

Use ||v||_{2,n}=(n^{-1} sum_i v_i^2)^{1/2}; use the corresponding normalized
Frobenius norm for w. Let Y=(m^{-1} sum_a y_a^2)^{1/2}, C0=||c(0)||_infty,
and assume P>=1. The input dimension is d_in; it is independent of the
Walsh bit count b, and d_in=2 for the unit-circle assertion. For a fixed
horizon T define

    C_T=(C0+Y)e^{2T}-Y,
    R_T=C_T+Y,
    L_T=1+(C0+Y)(e^{2T}-1)/2,
    D=P(P-1),
    a_T=sqrt(m) L_T^D C_T (L_T-1),
    b_T=L_T^{D+1},
    K_T=1+2P^2 a_T b_T.

The evident limiting interpretation applies when C0+Y=0. For every
t<=T, every column a and memory index k,

    ||c(t)||_infty <= C_T,     rho(t)<=R_T,
    1<=L(t)<=L_T,
    ||A_{k,a}(t)||_infty<=a_T,
    ||B_{k,a}(t)||_infty<=b_T,
    ||W(t)||_{2->2}<=K_T,
    ||W(t)^T delta2_a(t)||_{2,n}<=K_T C_T,
    ||w(t)||_{2,n}<=||w(0)||_{2,n}+2T R_T K_T C_T.

Proof. The readout gives |f_a|<=||c||_infty and rho<=||c||_infty+Y.
The equation for c gives the upper Dini derivative
C'(t)<=2(C(t)+Y), proving the first two bounds and the bound on L.
The triangular memory drift has absolute row sum at most
k+sum_{j<k}(2j+1)=k+k^2<=D. Gronwall with
integral rho/L=log L and |r_a|<=sqrt(m) rho yield

    max_k ||A_k||_infty <=sqrt(m) L_T^D integral_0^T rho C
                            <=sqrt(m) L_T^D C_T(L_T-1),
    max_k ||B_k||_infty <=L_T^D(1+integral_0^T rho)
                            <=L_T^{D+1}.

For normalized rank-one contractions,
||A_a B_a^T/n||_{2->2}=||A_a||_{2,n}||B_a||_{2,n}. Summing m columns and
sum_{k<P}(2k+1)=P^2 proves the W bound. The gate1 multiplier has norm at
most one and ||u_a||=1, so
||wdot||_{2,n}<=2 rho K_T C_T. Integration proves the final estimate.

For each finite n the vector field is locally Lipschitz on L>0: rho is a
norm of a smooth finite-dimensional map and hence locally Lipschitz, even
at rho=0. The bounds exclude escape on finite intervals and L never
approaches zero. They therefore prove a unique global solution for each
finite n. No loss-decrease assertion is used.

These constants are high-probability dimension-independent constants at
the stated random initialization. For example, c_i=Z_i/n gives
P(C0>R)<=2n exp(-n^2 R^2/2)<=2 exp(-R^2/2) for R>=sqrt(2), n>=1.
Also E||w(0)||_{2,n}^2=d_in, so Markov's inequality bounds its normalized
norm uniformly in n at any chosen failure probability. A union bound
supplies an event of probability at least 1-delta with all the constants
above depending only on delta,T,P and the fixed data.

For any unit-circle inputs u,v, at every t<=T,

    |f(t,u)-f(t,v)|
      <= C_T K_T ||w(t)||_{2,n} ||u-v||.

This follows by applying Cauchy--Schwarz, the 1-Lipschitz property of tanh,
the W operator bound, and the normalized Frobenius bound on w. Thus a
finite angular net controls the entire circle, once its output values are
controlled. Direct differentiation of W using the bounded memory
equations also gives a dimension-independent bound on ||Wdot||_{2->2},
and hence on the time derivative of every output. These compactness
bounds do not themselves give a permitted autonomous closure.

## 3. Orthogonality does not give the missing adaptive tail bound

Let v_j=sign(K_{0j}), choosing either sign at zero. Then ||v||_infty=1 and

    (Kv)_0=sum_j |K_{0j}|=:J.

Every K_{0j} has the distribution n^{-1} S_n, where S_n is a sum of n
independent signs. E S_n^2=n and E S_n^4<=3n^2. Applying the elementary
Paley--Zygmund inequality to S_n^2 gives
P(|S_n|>=sqrt(n/2))>=1/12. Therefore

    E J=E|S_n|>=c sqrt(n),     c=1/(12 sqrt(2)).

The row norm gives J<=sqrt(n). It follows that
P(J>c sqrt(n)/2)>=c/2: otherwise the expectation bound would fail
(the exact lower bound c/(2-c) is stronger). On this event,

    (1/n) sum_i |(Kv)_i|^2 1_{|(Kv)_i|>M} >= c^2/4

whenever c sqrt(n)/2>M. Thus there is no vanishing uniform L2 tail
estimate over all bounded vectors allowed to depend on K. There is also
no uniform Lp bound for such vectors for any p>2, since the displayed
single coordinate gives ||Kv||_{p,n}>= (c/2)n^{1/2-1/p}.

This is not a counterexample to the desired theorem: the constructed v
has not been shown reachable as delta2. Its exact consequence is that a
proof must exploit the evolution and initialization, rather than treating
delta2 merely as an arbitrary bounded vector.

Similarly, a finite-rank replacement of K does not approximate its full
first forward field. Conditional on K, for h_i=tanh(w_i dot u) the h_i
are independent with mean zero and variance q>0. If Q=Q(K) has rank r,

    E_w ||(K-Q)h||_{2,n}^2
       =(q/n)||K-Q||_F^2 >=q(1-r/n).

This rules out that particular field approximation at fixed r as n grows.
It is not a lower bound on the complexity of observable approximation.

## 4. An exact sufficient tail lemma

Set z_a(t)=W(t)^T delta2_a(t). A sufficient unproved statement is:

> For every T<infinity and delta>0 there exist a>0 and B<infinity,
> independent of n, such that, simultaneously with the initial bounds
> above and with probability at least 1-delta, the same realized solution
> satisfies
>
>     sup_{t<=T} max_{a<=m} (1/n) sum_i exp(a |z_{a,i}(t)|^2)<=B.

This statement is stronger than necessary. It makes the required
uniformity and the exact adaptive field explicit. It is not established
by the present derivations or by the external finite-step theorem below.

Here is its consequence, including the finite-scalar step. Clip each z_a
coordinate to [-M,M] in the w equation. Extend the vector field globally
by coordinate clipping c,A,B to sufficiently generous deterministic bounds
from Section 2 and by clipping L to an interval contained in (0,infinity).
Leave w unclipped. The extensions equal the original maps at the exact
trajectory. In the Hilbert norm consisting of normalized neuron block
L2 norms and the ordinary scalar L norm, this extended vector field F_M
is globally Lipschitz with a constant

    Lip(F_M)<=Gamma_T(1+M),

where Gamma_T is a finite function of the fixed data and the Section 2
bounds, independent of n. To verify this, coordinate clipping and tanh are
1-Lipschitz in normalized L2; clipped neuron blocks have uniform infinity
bounds; rank-one operators depend Lipschitz-continuously on their factors
in normalized L2; and the only previously unbounded multiplier in wdot,
namely z_a, now has infinity norm at most M. All scalar contractions are
normalized inner products of uniformly bounded L2 blocks. The residual
norm rho is Lipschitz. These facts prove the bound term by term.

For M>=a^{-1/2}, the tail hypothesis implies

    sup_t max_a ||z_a 1_{|z_a|>M}||_{2,n}
       <= C(a,B) exp(-a M^2/4).

Indeed x^2 1_{x>M} <= C(a)e^{-aM^2/2}e^{a x^2}; average and take a square
root. The exact solution is an approximate solution of F_M with defect
bounded by a finite fixed-data constant times this tail. Gronwall,
comparing the same initialized
exact and clipped flows, therefore gives

    sup_{t<=T} ||X(t)-X_M(t)||
       <= Gamma'_T exp(Gamma_T(1+M)T-aM^2/4) -> 0.

The quadratic tail exponent dominates the linear stability exponent for
every fixed finite T. A finite moment bound alone would not justify this
argument. The output map is Lipschitz on the bounded blocks, and the
angular estimate from Section 2 transfers the result to every unit-circle
input. Squared-loss error follows from bounded outputs and fixed labels.

## 5. Generic finite-scalar reduction for a Lipschitz flow

The following elementary construction closes the scalar-existence step
under the sufficient tail lemma. It is extremely large and gives no useful
polynomial storage rate. Its coefficient construction may use temporary
full-width vectors while processing the initial data; the final ODE,
stored coefficients and readout retain none of them. If preprocessing
cost itself is required to be independent of n, this construction does
not meet that stronger requirement.

Let F_n be an autonomous vector field on a finite-dimensional Hilbert
space, with Lip(F_n)<=L and ||F_n(x0)||<=M0 independent of n. Shift x0 to
zero. Set R=M0 T e^{LT}. Starting with V0={0}, choose a finite eta-net
N_k of the radius-R ball of V_k, using deterministic coefficient grids in
an orthonormal basis, and set

    V_{k+1}=span(V_k union {F_n(v): v in N_k}).

An eta-net in dimension d has size bounded by a function of d,R,eta.
Thus dim(V_k) obeys a recursion independent of n. Basis vectors and their
Gram products come from evaluations at these predetermined artificial
states, not from the target trajectory or its future values.

Define only for the proof the projected Picard functions

    q0(t)=0,
    q_{k+1}(t)=integral_0^t P_{V_{k+1}} F_n(q_k(s)) ds.

They satisfy q_k(t) in V_k and ||q_k(t)||<=R. Every F_n(q_k(t)) is within
L eta of V_{k+1}. Comparing with ordinary Picard iterates and summing the
integrated recurrence gives

    sup_t dist(x(t),V_K)
       <= a_K:=M0 e^{LT} L^K T^{K+1}/(K+1)!
                   + eta(e^{LT}-1).

The formula at L=0 is interpreted directly; that case is a constant
vector field and trivial. The first term is the usual Picard factorial
remainder, obtained by repeatedly integrating the Lipschitz inequality.
The second is bounded by solving
d_{k+1}(t)<=integral_0^t (L d_k(s)+L eta)ds with d0=0.

Let v solve the autonomous Galerkin equation
vdot=P_{V_K}F_n(v), v(0)=0. Writing e=P_{V_K}x-v gives
||edot||<=L(a_K+||e||), hence

    sup_t ||x(t)-v(t)||<=a_K e^{LT}.

This already yields arbitrary accuracy by finite K and eta, uniformly
in n. To remove the remaining full-vector evaluations at run time, fix
an orthonormal basis of V_K, tabulate the scalar coordinates of
P_{V_K}F_n at vertices of a sufficiently fine finite triangulation of a
coefficient box containing the radius-(R+2) ball, and use piecewise affine
interpolation. Coordinate clipping outside the box gives a globally
Lipschitz finite scalar vector field. Inside the box its uniform error
is at most L times the mesh diameter. Comparing its trajectory with v
using the Lipschitz constant of the exact projected field gives the
usual bound epsilon_mesh T e^{LT}. Choose this bound below one; a
first-exit argument then keeps the approximate trajectory inside the box.

Uniformly Lipschitz scalar observables can be tabulated and interpolated
on the same coefficient grid. For all-circle outputs, additionally use
the finite angular grid from Section 2. Finite scalar values at artificial
states are the complete retained data. The result is autonomous and
restartable from its coefficient state; it does not store a time series,
use future reference forcing, or call the original matrix at run time.
The construction is regular finite tabulation, not encoding an arbitrary
vector in the digits of a real number.

Applying this construction to F_M and then taking M large proves a
width-uniform finite-scalar existence statement **conditional on the
reachable-tail lemma**. All coefficient evaluations are functions of the
realized initialization, fixed data and algebraically chosen artificial
states. No change to the independent central signs is made.

## 6. Complete one-training-sample theorem

**Statement.** Fix one training input u in R^2 with ||u||_2=1, its label y,
P>=1, T<infinity, epsilon>0 and delta in (0,1). For every dyadic width n,
use exactly the initialized matrix and Gaussian variables specified in
the README. There is one construction rule, depending only on
P,T,epsilon,delta,u,y, which maps that realized initialization to a finite
autonomous scalar ODE and scalar readout. Its state dimension and number
of stored scalar coefficients are bounded independently of n. For each n,
with probability at least 1-delta,

    sup_{0<=t<=T} sup_{v in S^1} |fhat(t,v)-f(t,v)| <= epsilon,
    sup_{0<=t<=T} |(fhat(t,u)-y)^2-(f(t,u)-y)^2| <= epsilon.

The probability is for each width with the same constants; no simultaneous
probability assertion over an infinite sequence of widths is needed.
The coefficients are computed at initialization using prescribed
artificial states and no target-trajectory data. During evolution, there
are no neuron arrays or calls to W0. The ODE is restartable from its finite
current state. Preprocessing uses full-width temporary vectors, and its
arithmetic cost may depend on n. There is no uniform bit-complexity claim.
This is an existence theorem with immense static tabulation, not an
efficient dictionary result or a polynomial stored-size guarantee.

The same argument works for any fixed input dimension and its unit
sphere, using a finite sphere net. The explicit angular construction below
specializes to R^2. In fact the proof only uses ||W0||_{2->2}<=1 and does
not average over the central signs; it thus retains all their independent
randomness without requiring a universality theorem.

### 6.1 Exact monotone transform

For m=1 write s_i=w_i dot u and p_i=w_i(0)-s_i(0)u. The training equation
has wdot parallel to u, so p_i is constant. Define

    phi(s)=s/2+sinh(2s)/4,    phi'(s)=cosh^2(s),
    a_i=phi(s_i),            psi(a)=tanh(phi^{-1}(a)).

The map phi is a smooth increasing bijection R->R. Its inverse is
1-Lipschitz, and

    adot=-2r W^T delta2,
    psi'(a)=(1-tanh^2(phi^{-1}(a)))^2 in (0,1].

These identities follow by multiplying
sdot=-2r(1-tanh^2(s)) W^T delta2 by phi'(s). The complete transformed
state is X=(a,c,L,A_0,...,A_{P-1},B_0,...,B_{P-1}). Training h1=psi(a).
For any unit query v, recover its first hidden activation as

    h1_v=tanh((u dot v) phi^{-1}(a)+p dot v).

For fixed p and v this map is 1-Lipschitz in a in normalized L2.
The p_i are used only during preprocessing of scalar readout tables and
are discarded before the scalar ODE is run.

### 6.2 Uniform event and an explicit globally Lipschitz extension

Set

    Rc=max(sqrt(2),sqrt(2 log(4/delta))),
    Rw=sqrt(2 d_in/delta),       d_in=2.

The event E={||c(0)||_infty<=Rc, ||w(0)||_{2,n}<=Rw} has probability
at least 1-delta, by the Gaussian union estimate in Section 2 and Markov's
inequality E||w(0)||_{2,n}^2=d_in. Compute the bounds of Section 2 with
m=1, C0=Rc and Y=|y|, denoting them by Cbar,Rbar,Lbar,abar,bbar,Kbar.
All bounds then hold on E. In particular the true output has angular
Lipschitz constant at most

    Jcircle=Cbar Kbar (Rw+2T Rbar Kbar Cbar).

Choose generous clipping bounds

    C=Cbar+1, alpha=abar+1, beta=bbar+1, ell=Lbar+1,
    Rr=C+|y|, D=P(P-1), kappa=1+2P^2 alpha beta.

In the transformed vector field clip c,A_k,B_k coordinatewise to
[-C,C],[-alpha,alpha],[-beta,beta], and clip L to [1,ell]. Leave a
unclipped. Denote clipped quantities by a tilde. Define

    Wtilde=W0-(2/Ltilde) sum_{k<P}(2k+1)
                                     Atilde_k Btilde_k^T/n,
    h=psi(a), v=tanh(Wtilde h),
    d=ctilde*(1-v^2), r=<ctilde,v>_n-y, rho=|r|.

The globally defined extension is

    adot=-2r Wtilde^T d,   cdot=-2r v,   Ldot=rho,
    Adot_k=r d-(rho/Ltilde)[k Atilde_k+sum_{j<k}(2j+1) Atilde_j],
    Bdot_k=rho h-(rho/Ltilde)[k Btilde_k+sum_{j<k}(2j+1) Btilde_j].

On E this extension agrees with the transformed original vector field
along its entire exact trajectory through T. Its unique solution from
that initialization therefore is the exact transformed trajectory.

Here are explicit dimension-independent norm and Lipschitz bounds. Use
the Hilbert norm formed from the normalized L2 norms of all neuron
blocks and the ordinary absolute value of L. There are Q=2P+3 blocks.
The extended vector field, denoted F_n, obeys

    ||F_n(X)|| <= M,
    M=2Rr kappa C+3Rr
                  +P Rr(C+D alpha+1+D beta).

For a completely explicit Lipschitz constant put

    wL=2P^2(beta+alpha+alpha beta),
    vL=kappa+wL,
    fL=1+C vL,
    dL=1+2C vL,
    zL=kappa dL+C wL,
    La=2(Rr zL+kappa C fL),
    Lc=2(Rr vL+fL),
    LA=Rr dL+C fL+Rr D+D alpha(fL+Rr),
    LB=Rr+fL+Rr D+D beta(fL+Rr),
    Lambda=max(1,sqrt(Q)[La+Lc+fL+P(LA+LB)]),
    LO=sqrt(Q) fL.

Then Lip(F_n)<=Lambda, and every query output, computed with clipped
blocks and the recovered h1_v, is bounded by C and is LO-Lipschitz in
X, uniformly in the query v.

For verification, let E_sum be the sum of block differences. Clipping is
1-Lipschitz, so ||Delta Wtilde||_{op}<=wL E_sum,
||Delta h||_{2,n}<=E_sum, and ||Delta v||_{2,n}<=vL E_sum.
Consequently |Delta r|,|Delta rho|<=fL E_sum,
||Delta d||_{2,n}<=dL E_sum and
||Delta(Wtilde^T d)||_{2,n}<=zL E_sum. Also
|Delta(rho/Ltilde)|<=(fL+Rr)E_sum. These estimates give, respectively,
the displayed La,Lc,fL,LA,LB bounds for each derivative block. Finally
E_sum<=sqrt(Q)||Delta X|| converts the sum bound into the stated Hilbert
Lipschitz bound. Replacing h by any query's h1_v proves the output bound
by exactly the same calculation. The norm bound M follows from
|r|,rho<=Rr, ||d||<=C, ||Wtilde||<=kappa, and the triangular row-sum
bound D. Thus no tail estimate for W^T delta2 is used.

### 6.3 Explicit finite construction and its error certificate

Assume T>0; T=0 only requires a finite initial-output angular table.
Use Section 5 with initial state X0, global Lipschitz bound Lambda,
M0=M, and radius

    Rspace=M T e^{Lambda T}.

Shift X0 to zero before building the spaces. This does not require a
bound on the transformed initial a_i: all nonlinear maps of a used in
F_n and in its fixed-query readouts are globally Lipschitz, and F_n is
globally bounded by M. The scalar initial state is the zero coefficient
vector in the final basis.

Choose

    zeta=epsilon/max(1,2Rr),
    e0=min(1/2,zeta/(4LO)).

Select K large enough and positive eta,h small enough that

    M e^{2Lambda T} Lambda^K T^{K+1}/(K+1)! <= e0/3,
    eta e^{Lambda T}(e^{Lambda T}-1) <= e0/3,
    Lambda h T e^{Lambda T} <= e0/3,
    LO h <= zeta/4.

All choices depend only on the stated data and accuracy parameters, and
exist because of the factorial in the first inequality. Here h is the
maximum simplex diameter of the final coefficient triangulation. The
space approximation plus interpolated Galerkin equation then gives

    sup_{t<=T} ||X(t)-X0-Qbasis q(t)|| <= e0.

The matrix Qbasis is only proof notation: its columns are the constructed
orthonormal full-state vectors. They are discarded after tabulation.
At run time q solves the autonomous piecewise affine scalar field whose
vertex values are the scalar coordinates of Qbasis^T F_n at artificial
states X0+Qbasis q. The field is extended outside its finite box by
coordinate clipping. The first-exit argument in Section 5 applies
because e0<=1/2.

At the same coefficient vertices tabulate outputs for a circle net with
maximum angular gap

    gamma <= min(1,zeta/(2 max(1,Jcircle))).

Interpolate in the coefficient simplices and periodically between angle
knots. This defines fhat from q and the requested angle alone. For each
angle knot, state error contributes at most LO e0<=zeta/4 and coefficient
interpolation contributes at most LO h<=zeta/4. For any angle, convex
interpolation between its neighboring knots contributes at most
Jcircle gamma<=zeta/2, by the true output's angular Lipschitz bound.
Thus the uniform output error is at most zeta<=epsilon. Both exact and
interpolated outputs lie in [-C,C], so

    |(fhat-y)^2-(f-y)^2| <= 2(C+|y|)|fhat-f|
                           <=2Rr zeta<=epsilon.

This proves the statement on E and hence with probability at least
1-delta. It approximates the same realization at every stage: no width
limit, Gaussian replacement, refreshed randomness or future reference
forcing occurs.

For a storage bound, the coefficient nets can be formed by projecting a
cubic lattice to the radius-Rspace ball. Let d_k=dim(V_k), d_0=0. One
valid bound, with the zero-dimensional power interpreted as one, is

    d_{k+1} <= d_k+(3+2 Rspace sqrt(d_k)/eta)^{d_k}.

Set Dstar=d_K. For Dstar>0, a cubic coefficient grid in
[-Rspace-2,Rspace+2]^{Dstar}, split into simplices of diameter at most h,
needs at most

    Vstar=(2+2(Rspace+2)sqrt(Dstar)/h)^{Dstar}

vertices. At most Jstar=ceil(2pi/gamma)+1 angle values are needed. Apart
from fixed grid rules, at most (Dstar+Jstar)Vstar scalar field/readout
values are retained, together with O(Dstar+Jstar+K) metadata. If Dstar=0
the exact solution is stationary and only its initial angular readout
table is needed. These bounds are independent of n but enormous; the
recursive dimension growth and final high-dimensional table yield no
polynomial error-versus-stored-size result. Temporary basis construction
and table evaluation still process the n-neuron initialization.

For several noncollinear training inputs the original w equation sums
the different vector fields (1-tanh^2(w dot u_a))u_a. The scalar transform
above does not simultaneously remove their gates. This completed
one-sample theorem therefore does not resolve the general fixed-data
target or provide an efficient reusable feature dictionary.

## 7. Source check and conclusion

The primary paper [Gorini, Jones, Kunisky and Pesenti, *Universality of
first-order methods on random and deterministic matrices*, April 13,
2026](https://lucaspesenti.github.io/universality.pdf), Introduction
Sections 1.1--1.2, treats fixed-length polynomial general first-order
methods through traffic distributions. Its discussion explicitly leaves
general nonlinearities to a possible approximation extension. This
supports looking at static contraction families, but does not supply the
adaptive tanh tail estimate, continuous-time limit, or a quantitative
width-uniform scalar approximation here. No theorem from that source is
used in the proved bounds above.

The exact remaining bridge for this route is a reachable backward-field
tail estimate strong enough to survive clipping stability, such as
Section 4, for the independent-sign convolution and general fixed data.
The bounded adaptive-vector construction shows why replacing that lemma
by an operator-norm assertion is invalid. Failure to prove this lemma is
a failure of the present route, not a proof that finite observable
compression is impossible.
