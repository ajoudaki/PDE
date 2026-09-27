# A bounded-moment tree closure: proved bounded-mark result and remaining Gaussian gap

2026-09-27. Scoped independent theoretical route. Inputs: the block model in
sections 1–3 of `AGGREGATE_SCALAR_CONSTRUCTION.md`; the histogram construction
is not used. Required rigorous-math and conjecture-investigation skills were
read. No training experiment, other study, or external result is used.

**Conclusion.** There is a genuine, autonomous moment hierarchy for the
block system with bounded G and fully Gaussian initial first-layer weights:
retain decorated tree contractions, and bound their approximate values by
a projection and penalty. The same hierarchy is independent of a chosen end
time. For any fixed time interval and any fixed finite set of queries, its error is
exponentially small in the retained tree degree. The scalar state count is
exponential in that degree with a base depending polynomially on the memory
order and number of queries, but not on block size. Consequently this gives an
algebraic error-versus-state-count bound for the bounded-mark problem. The
exponent and constants depend on block size and the mark bound; the result
does **not** give the requested effective polynomial bound for the actual
Gaussian population. Initialization cost is another unresolved efficiency
issue. A Fourier version can plausibly address the entire circle for bounded
marks, but its complete proof is not claimed here. Section 11 gives the
strongest form of the construction; sections 2–6 first prove its convergence
mechanism with a simpler normalization. The independent same-study audit
checked both forms and the extension in section 11.

## 1. Contract and notation

Write H for the given block-memory order and D for the degree of the additional
aggregate approximation. These are different approximation axes. The target
has k first and k second neurons in each block, m training inputs, and the
population law of blocks. Width has already disappeared. The initial marks
are the k-by-k matrix G and k-by-2 matrix w(0), with the Gaussian laws stated
in the input. The model uses the actual G and G transpose from the same block.

The preliminary proof first replaces the initial law by its conditioning
on a permutation-invariant bounded box

    |G_{alpha i}| <= R_G,  |w_{i ell}(0)| <= R_w.

This replacement is explicit and is not identified with the Gaussian model.
The initial gates and memory states are still initialized exactly as in that
model. Fix T and a finite query list v_1,...,v_M containing the m training
inputs. The closure approximates every f(v_a) and the training loss uniformly
on [0,T]. It retains expectations of functions of current block state, not
particles, cell masses, an initial-label population, or future trajectories.

The result proves state-count efficiency at fixed R_G,k,m,H,M,T. It does
not prove polynomial initialization work in these parameters, a polynomial
bound with an exponent uniform in the mark cutoff, or the full-circle version.
The preliminary normalization in sections 3–6 uses a prescribed horizon T.
Section 11 replaces it with one fixed clock normalization, yielding a single
hierarchy indexed by D that converges on every fixed compact interval with
the same coefficients. It also removes the cutoff on w(0) from the target.
Restarting uses the current aggregate state and the same coefficients; it
does not require fresh target-law information.

## 2. An exact polynomial gate lift

Let g=1/L. For every query a, add the current gates

    x_a = tanh(w v_a),    h_a = tanh(z_2(v_a)).

They are redundant functions of current state and current aggregate fields;
they are not frozen features. Training gates are among these queries. Put

    d_b = c odot (1-h_b^2),
    S_{j,a} = E[B_j^T x_a/k],
    V_{j,b} = E[A_j^T d_b/k],
    f_a = E[c^T h_a/k],
    r_b = f_b-y_b,    rho = (sum_b r_b^2/m)^(1/2),
    nu_j = 2j+1,    kappa = 2g/m.

Here b is a training index; a may be an arbitrary query. Define

    J_b = G^T d_b - kappa sum_j nu_j B_j V_{j,b},
    C_{ab} = v_a dot u_b.

The original w equation and the chain rule give the exact formula

    dot x_a = -(2/m) sum_b r_b C_{ab}
              (1-x_a^2) odot (1-x_b^2) odot J_b.                 (4)

The remaining local equations are

    dot c = -(2/m) sum_b r_b h_b,
    dot A_{j,b} = r_b d_b - rho g [j A_{j,b}
                              + sum_{i<j} nu_i A_{i,b}],
    dot B_{j,b} = rho x_b - rho g [j B_{j,b}
                              + sum_{i<j} nu_i B_{i,b}],
    dot g = -rho g^2,    dot G = 0.                              (5)

Critically, the derivative of the global S field is retained:

    D_{j,a} := dot S_{j,a}
       = E[((dot B_j)^T x_a + B_j^T dot x_a)/k].                (6)

Using dot kappa = -(2/m) rho g^2, the second gate equation is

    dot h_a = (1-h_a^2) odot {
       G dot x_a
       + (2/m) rho g^2 sum_j nu_j A_j S_{j,a}
       - (2/m) g sum_j nu_j [(dot A_j) S_{j,a}+A_j D_{j,a}]
    }.                                                        (7)

Equations (4)–(7), with (6) substituted, are polynomial in the local scalar
coordinates x,h,c,A,B,G. Coefficients are locally Lipschitz functions of g
and finitely many expectations. The sole square root is rho, which is a
Euclidean norm of the finite residual vector and is Lipschitz at zero.
There is no derivative of rho in these equations.

Counting every local scalar factor, including each G entry, gives:

| expression | maximum local degree |
| --- | ---: |
| dot x | 8 |
| dot A | 3 |
| dot B, dot c | 1 |
| integrands defining D | 9 |
| dot h | 11 |

S,V,f have degree at most 2,4,2 respectively. Thus all coefficient fields
are determined by a fixed list of moments of degree at most s=9; local
Lie differentiation raises degree by at most r=10. The coefficients in this
count may be products of low moments. This is a local-degree count, not a
claim that the full ODE is a polynomial of degree eleven in the aggregate
state.

The lift is exact. Initially set x,h from their definitions. If (4)–(7) are
solved together with w, then differentiation of

    x_a-tanh(w v_a),
    h_a-tanh(G x_a-kappa sum_j nu_j A_j S_{j,a})

shows that zero discrepancies remain zero by uniqueness. Alternatively w is
unnecessary for the finite-query lifted dynamics after its initial gates are
computed. No low-rank assumption about G has been introduced.

## 3. Bounded local coordinates on a fixed interval

For the bounded-mark target, all local coordinates in the lift have explicit
finite deterministic bounds on [0,T]. In fact the needed memory bounds do
not grow with H. Let P_j be the ordinary Legendre polynomial and set
p_j(x)=P_j(2x-1). The identities

    p_j(1)=1,
    x p_j'(x)=j p_j(x)+sum_(i<j)(2i+1)p_i(x),
    |p_j(x)|<=1 for 0<=x<=1

give the exact representations, coordinate by coordinate,

    A_{j,a}(t) = integral_0^t r_a(s) d_a(s)
                                p_j(L(s)/L(t)) ds,

    B_{j,a}(t) = integral_0^1 x_a(0) p_j(xi/L(t)) dxi
                 + integral_0^t rho(s) x_a(s)
                                p_j(L(s)/L(t)) ds.             (8a)

Differentiation reproduces (5), including every lower-order memory term;
orthogonality to constants gives the stated B initialization. The bound on
P_j can also be checked from its elementary integral representation

    P_j(cos theta) = pi^(-1) integral_0^pi
              (cos theta+i sin theta cos phi)^j dphi,

whose integrand has magnitude at most one. These are identities for
polynomials, so endpoint and zero-speed intervals of L introduce no inverse
change-of-time assumption in (8a).

Since |dot c_alpha|<=2rho and c(0)=0, |c_alpha|<=2(L-1). Also
|r_a|<=sqrt(m)rho. Applying |p_j|<=1 in (8a) therefore gives

    |B_{j,ia}| <= L,
    |A_{j,alpha a}| <= integral_0^t 2sqrt(m)rho(s)(L(s)-1)ds
                       = sqrt(m)(L-1)^2.                      (8b)

Write Y=max_b |y_b|. Minkowski's inequality gives
rho<=max|c|+Y<=2(L-1)+Y, whence

    L-1 <= (Y/2)(exp(2t)-1).                                  (8c)

These establish the finite deterministic normalization bounds without an
artificial exponential in H. The coefficient sums in the ODE still depend
on H, since j+sum_(i<j)(2i+1)=j+j^2<=H^2. For Y=0, c,A,w,L
are stationary and the assertion follows directly; normalization constants
are chosen at least one to avoid zero denominators.

Scale each local coordinate by its corresponding bound, or by one if that
bound is smaller than one. The exact normalized local coordinates lie in
[-1,1]. Scale G by max(1,R_G). Gates need no scaling. Each coordinate's
velocity is a finite sum of products of normalized local coordinates and
coefficient fields. On the cube of physically bounded low moments and
0<=g<=1, the sum of absolute values of the normalized coefficients and its
Lipschitz constant are finite and computable from (4)–(8).

These constants are **not** uniform in k or the mark cutoff. An unnormalized
edge contraction sum_i G_{alpha i} z_i has coefficient bound k R_G under
entrywise normalization. A two-edge term can contribute (k R_G)^2. The fact
that Gaussian entries normally have size k^(-1/2) does not turn either
absolute coefficient bound into a constant. Using operator bounds may improve
constants but is not used in the theorem.

## 4. Decorated tree observables and their count

There are two types of vertices, first-layer i and second-layer alpha.
First-vertex decorations are the scalar colors x_a and B_{j,b};
second-vertex decorations are h_a,c,A_{j,b}. An edge carries normalized
G_{alpha i}. A decoration may occur with any nonnegative integer power.
For a finite bipartite tree T, define

    psi_T(z) = k^(-|V(T)|) sum_{all vertex labels in {1,...,k}}
               product_edges normalized_G
               product_vertex_decorations normalized_coordinate.   (9)

Every sum is over all labels, with repeated numerical labels permitted.
Thus |psi_T|<=1. A repeated value of two formal labels is not discarded.
The contractions retain the correlations between G and its own transpose.
The expectation q_T=E psi_T is one ordinary real aggregate.

Degree counts edge factors plus scalar decoration factors. The constant and
single-vertex decorated trees are included. Redundant trees may be retained;
one does not need a costly minimal invariant basis.

Lie differentiation preserves this class. Differentiate one decoration at
one existing vertex. Equations (4)–(7) replace it by a finite sum of local
decorations and newly summed neighbors. A G-transpose factor attaches a fresh
second vertex to a first vertex; G dot x attaches a fresh first vertex, with
at most one further new second vertex. Every formal index introduced by a
matrix-vector multiplication is fresh. The operation grafts a rooted tree
at the differentiated vertex and never joins two existing formal vertices.
Scalar aggregate factors remain coefficients. In particular D in (6) is a
finite list of expectations of single-vertex or one-edge trees. Numerical
index collisions are already present in (9), so no distinct-index assumption
is being made.

Normalization produces explicit powers of k. Attaching v fresh formal
vertices introduces k^v when the new average (9) replaces the original sum.
These factors belong in the coefficient constants of section 3. They do not
create extra coordinates.

Let C= M+mH+3 be an upper bound on the number of decoration colors at one
vertex. The number N_D of plane decorated trees of degree at most D admits
the conservative bound

    N_D <= [64(C+1)^2]^(D+1).                                  (10)

Indeed a rooted plane tree with e edges has at most 4^e shapes; the root
type contributes a factor two. It has e+1 vertices. Distributing at most D
decorations over these vertices and ordering their colors can be bounded by
2^(D+e+1) C^D. Sum over e<=D and the number of decorations, absorbing the
polynomial factors into the displayed exponential. Invalid empty or
redundant trees may simply be kept, so this is an upper bound. Taking a
canonical ordering of branches only reduces the count.

This count is independent of k. The coefficients, accuracy exponent, and
work needed to initialize a tree expectation are not claimed independent
of k. The tree restriction is stronger than simply keeping all monomials
in a k^2+O(kmH)-dimensional block state.

## 5. The autonomous bounded-moment closure

The exact hierarchy has the form

    dot q_T = sum_U a_{T,U}(q_low,g) q_U,                       (11)

where deg(U)<=deg(T)+10, q_low comprises a fixed list of trees of degree
at most 9, and g obeys (5). Products of low moments are evaluated in the
coefficient function. Duplicated representations of the same low moment
can be fixed once in advance. On the physical low-moment cube, coefficient
bounds have the form

    sum_U |a_{T,U}| <= a deg(T),
    sum_U |a_{T,U}(z)-a_{T,U}(z')|
                    <= b deg(T) ||z-z'||_infinity,             (12)

for finite a>=1,b>=1 depending on the fixed parameters. A direct finite
algorithm obtains a,b by expanding the displayed formulas, summing absolute
coefficients, and using a Lipschitz bound for rho. This need not be a sharp
algorithm. The factor deg(T) counts the possible differentiated factors;
each replacement has bounded size and finitely many colors.

Let pi(x)=min(1,max(-1,x)). Keep all tree coordinates of degree at most D,
and set missing children to zero in (11). The proposed scalar ODE is

    dot qhat_T = sum_{deg(U)<=D}
       a_{T,U}(pi(qhat_low),ghat) pi(qhat_U)
       - a deg(T) [qhat_T-pi(qhat_T)],

    dot ghat = -rho(pi(qhat_low)) ghat^2,    ghat(0)=1.          (13)

The degree-zero constant is fixed to one. Initialize every retained
coordinate with its exact initial expectation for the bounded-mark law.
Approximate initialization is covered in section 6.

This is a finite, autonomous, locally Lipschitz ODE. Its coefficients use
only the data, H,k, normalizing constants, and the current scalar state.
There is no target trajectory in the coefficients. Its state at an
intermediate time suffices to continue it, so it is restartable.

The box |qhat_T|<=2 is invariant: at qhat_T=2, the first term has absolute
value at most a deg(T) and the penalty is -a deg(T); the lower face is
analogous. Also 0<ghat<=1. Thus the solution exists for all positive time.
The qhat need not be realizable as moments of one probability law, and the
algorithm does not reconstruct such a law. Exact physical moments lie in
[-1,1], so neither pi nor the penalty changes their untruncated evolution.

## 6. Finite propagation through the moment degrees

Here is the convergence argument, including the source of the omitted error.
Let E_d(t) be the largest error among trees of degree at most d, together
with |g-ghat| when d>=s. Take s=9, enlarged to include any chosen output
observable, and r=10. The g equation only changes the constants below.
All moment errors are bounded by three. Projection is nonexpansive.
Moreover for a true q in [-1,1], the outward penalty has a nonpositive
contribution to the upper derivative of |qhat-q|. Therefore (11)–(13) imply
the integral comparison

    E_d(t) <= E_d(t0)
           + a d integral_(t0)^t E_(d+r)(v) dv
           + b d integral_(t0)^t E_s(v) dv.                    (14)

For degrees above the truncation, the fictitious approximate child is zero;
the missing true child has magnitude at most one. This is the actual source
term. Bounding all higher errors by three makes (14) valid as a finite
iteration up to the truncation boundary. Constants can be enlarged once
to cover low degrees, the g equation, and the finite low-moment list.

Choose a slab length tau with ar tau<=1/8. Suppose all initial errors of
degree at most M are at most delta, with M<=D. Iterate (14) n+1 times, where
n=floor((M-d)/r). The coefficient of an initial error at degree d+jr is

    (a t)^j [d(d+r)...(d+(j-1)r)]/j! .                         (15)

The remainder is bounded by three times (15) with j=n+1. For d<=M/4,
the rising-factorial identity and the elementary binomial bound yield

    sum_(j>=0) (a tau)^j (d)_(r,j)/j!
       = (1-ar tau)^(-d/r) <= exp(c_0 d),

    (a tau)^(n+1) (d)_(r,n+1)/(n+1)!
       <= C exp(-c_2 M),                                     (16)

where one may take c_0=log(8/7)/r and c_2=log(2)/(2r), after a fixed
enlargement of C. To verify the second bound, put h=ceil(d/r). The
factorial ratio is at most 2^(h+n), while n+1 >= (M-d)/r >=3M/(4r).
Multiplication by 8^(-(n+1)) gives an exponential stronger than the stated
one. Floors and small M are absorbed in C.

The kernel multiplying the low-degree error after this iteration is bounded
by

    d (1-ar tau)^(-d/r-1).

First apply the estimate at d=s and use the scalar integral Gronwall
inequality. This bounds E_s throughout the slab by

    C_s [delta + exp(-c_2 M)].

Insert that estimate into the bound for general d. For constants C_1,C_2
independent of D,M,d, one obtains

    sup_(0<=t<=tau) E_d(t0+t)
       <= C_1 exp(C_2 d) [delta+exp(-c_2 M)],
       s <= d <= M/4.                                       (17)

This derivation uses boundedness to control the truncation boundary. An
ordinary unsaturated Carleman system does not supply that bound.

To cover T, use J=ceil(T/tau) slabs. Choose

    0<alpha<=min(1/4,c_2/(4C_2)).

At each slab retain the estimate only through degree alpha times the
previous estimated degree; the actual ODE still retains all D coordinates.
Starting with zero initial error, (17) inductively gives constants C_J and
c_J>0 such that

    sup_(0<=t<=T) E_s(t) <= C_J exp(-c_J D),                  (18)

provided D is large enough that alpha^J D>=2s. One may take c_J to be a
fixed multiple of c_2 alpha^(J-1), with a further fixed reduction to absorb
integer floors. For the induction, if the old error is at most
C exp[-(c_2/2) M/alpha], the amplification exp(C_2 alpha M) and the new
tail exp(-c_2 M) are both bounded by a constant times
exp[-(c_2/2) M]. Constants multiply finitely many times. The same estimate
inside each slab gives the supremum in (18).

This is finite-horizon convergence, not merely a small-time Taylor series.
Its exponent can be extremely small: J grows with aT and alpha depends on
the normalized coefficient bounds. No favorable uniform-in-T exponent is
asserted.

For initialization error at most delta_0 in every retained coordinate,
the same proof applies with the initial delta_0 term. Choosing delta_0
exponentially small in D, with a sufficiently large exponent determined by
the finite number of slabs, preserves (18). Thus exact integration is not
an essential mathematical oracle, but the required integration accuracy
has a computational cost.

Since f_a is a scaled degree-two moment, (18) proves uniform finite-query
output accuracy. The training residuals are uniformly bounded by section 3
and the clipped prediction bounds, so

    |m^(-1)sum_b r_b^2 - m^(-1)sum_b rhat_b^2|
       <= [max_b(|r_b|+|rhat_b|)] max_b |f_b-fhat_b|

proves the same rate for training loss. Combining (10) and (18), with a
fixed padding convention for the tree list if necessary, gives an
algebraic bound C N^(-eta) for the prescribed sequence of state sizes,
with eta>0 depending on all the fixed bounded-mark parameters. This does
not assert that eta is numerically useful.

## 7. Initialization and equation-generation costs

An initial coordinate is the expectation of the explicitly known expression
(9), with x=tanh(w(0)v_a), h=tanh(Gx), c=A=0 and the specified B. These are
finite bounded integrals over k^2+2k initial Gaussian variables restricted
to a known box. Deterministic quadrature with a verified error bound computes
them to the accuracy required in section 6; quadrature nodes are discarded
and are never dynamical states. This establishes computability from the
allowed initial law, not cheap initialization.

Direct tensor quadrature has the curse of dimension. The tree state count
does not solve this cost. Gaussian conditioning and symmetry may reduce
some integrals, but no polynomial-in-k,m,H algorithm for all required initial
coordinates has been proved here. The quadrature cost can nevertheless be
made explicit. Let d_0=k^2+2k. On the seed box every normalized initial local
factor has a computable Lipschitz bound K_0 independent of D. A product of
at most D factors in [-1,1] is D K_0-Lipschitz; averaging labels preserves
this bound. Product Gaussian cell probabilities and midpoint quadrature
therefore achieve simultaneous error eta in all coordinates with seed-cell
diameter at most eta/(D K_0). This needs at most

    [1+O(max(R_G,R_w) sqrt(d_0) D K_0 / eta)]^d_0

cells. Since eta may be chosen exponentially small in D, this is exponential
in D with an exponent depending on d_0; at fixed k it is polynomial in the
requested inverse accuracy, but it is not a practical dimension-free bound.

Evaluation of one tree on one quadrature block does **not** require
k^(D+1) direct index enumeration. Root the tree and pass k-component messages
from leaves to root. Each edge contracts one k-by-k matrix G or its
transpose with the child message; local decorations multiply the message
componentwise. Including one factor 1/k per eliminated vertex and the final
root average evaluates (9) exactly. This costs O(k^2(D+1)) arithmetic
operations, plus computing the initial gates once per quadrature block.
Repeated numerical labels are still included because every matrix-vector
sum is unrestricted. No random sampling is needed or used in this argument.

By contrast, generating the ODE by grafting local formulas onto listed tree
decorations requires finitely many local operations per vertex and per
coefficient term. A redundant plane-tree enumeration avoids a hard graph
isomorphism problem. This does not settle floating-point conditioning or
precision requirements for a practical solver.

## 8. Why this is not yet the actual Gaussian result

There are three distinct gaps.

1. **Cutoff removal with a fixed algebraic complexity exponent.** Gaussian
   tails permit bounded-mark approximation in principle, but R_G must
   increase as the requested error decreases. In this proof a,b grow
   with those bounds, and c_J in (18) decreases at least as fast as the
   conservative propagation argument prescribes. Therefore substituting
   R_G approximately sqrt(log(1/epsilon)) into (18) does not yield
   D=O(log(1/epsilon)) with a fixed constant. N_D exponential in D can then
   exceed every fixed polynomial in 1/epsilon. This is a defect of the
   present bound, not a lower bound against every closure.

2. **All circle inputs at once.** The proved theorem treats fixed M. A
   Lipschitz circle net needs M of order 1/epsilon under a generic first
   derivative bound. Inserting that M into (10) can give
   exp[O(log(1/epsilon)^2)] state count even with D logarithmic. Analytic
   interpolation improves M but does not by itself restore a fixed
   algebraic exponent in this construction.

3. **Aggregate initialization.** Section 7 proves finite computability, not
   the requested practical or polynomial parameter dependence.

The actual Gaussian population is not replaced by bounded marks in the
claim. Nor does failure to close these estimates prove a no-go theorem for
the desired Gaussian aggregate closure.

## 9. A concrete route for the circle, not counted as proved

There is a way to avoid a growing number of query colors. Use one symbolic
circle variable theta and gate colors x(theta),h(theta), in addition to the
fixed training colors. For each decorated tree retain Fourier coefficients

    q_(T,ell) = E[(2pi)^(-1) integral psi_T(z,theta)
                                      exp(-i ell theta) dtheta].

Products in theta become convolutions, so these are still scalar current-state
aggregates. Their real and imaginary parts are ordinary real ODE coordinates.
Grafting (4)–(7) uses only two extra query colors. A Fourier cutoff Q gives
O(Q N_D) coordinates rather than changing the exponential base to depend on
the number of sampled queries.

For bounded initial marks and fixed T, the exact gates extend to a common
complex strip in theta: bounded w controls the imaginary part of w u(theta),
and then bounded G,A,B control the second preactivation. A sufficiently
small strip stays a positive distance from tanh's poles. Consequently exact
tree functions have norms bounded by K^degree in a periodic analytic Sobolev
algebra. After that normalization, one can try to replace scalar clipping
in (13) by projection of each finite Fourier vector onto its Hilbert norm
unit ball. Projection is nonexpansive and the same outward-penalty argument
is available. Fourier tails in a slightly narrower strip are exponentially
small in Q; taking Q proportional to D should preserve exponential degree
accuracy and O(D N_D) state count.

To promote this paragraph to a theorem, one must specify one Hilbert algebra,
verify all global field product bounds and the strip gap uniformly in tree
degree, and run the coupled Fourier/tree source estimate without losing
the coefficient bound O(degree). Those details have not been completed in
this bounded route. Even their completion would leave Gaussian cutoff
removal and initialization cost open.

## 10. Claim status and adversarial audit

| claim | status |
| --- | --- |
| exact polynomial training/query gate lift, including dot S | proved |
| tree grafting closure, including index collisions | proved |
| state count independent of k at fixed degree | proved; constants are not uniform in k |
| bounded-moment autonomous ODE is globally well posed | proved |
| fixed finite-query bounded-mark compact-horizon convergence | proved above |
| same hierarchy for every fixed horizon, with Gaussian w(0) | proved in section 11; bounded G still required |
| algebraic error versus state count for those fixed parameters | proved; exponent may be tiny |
| cheap initial expectation computation | open |
| bounded-mark full-circle theorem | concrete incomplete route |
| actual Gaussian closure with fixed polynomial error/size rate | open |

The method retains moving features and the full G/G-transpose correlation.
Its coefficients and initial values use no future trajectory. It is
restartable and stores finitely many genuine aggregate observables. The
principal structural objection is the uncontrolled dependence of the useful
accuracy exponent on Gaussian-tail cutoffs. The principal computational
objection is the cost of producing the initial aggregates. Neither is
resolved by the favorable tree count alone.

## 11. Extension: one bounded-mark hierarchy for all finite horizons

The target-horizon normalization in sections 3–6 can be replaced by the
following normalization using the existing clock. This extension uses the
exact history bounds (8b), rather than a new hypothesis. Write

    zeta = c g/2,
    alpha_j = A_j g^2/sqrt(m),
    beta_j = B_j g.

Every entry of zeta,alpha,beta has absolute value at most one for all time:
(8b) gives bounds 1-g, (1-g)^2, and 1, respectively. Gates x,h remain bounded
by one, and normalize the static G entries by max(1,R_G), as before. These
coordinate bounds and the normalization are independent of a chosen T.

Define the current aggregate fields

    F_a = E[zeta^T h_a/k],
    R_b = 2 F_b-g y_b,
    sigma = (m^(-1)sum_b R_b^2)^(1/2),
    s_{j,a} = E[beta_j^T x_a/k],
    t_{j,b} = E[alpha_j^T(zeta odot(1-h_b^2))/k].

Indices b are training indices; a may be any query. Then

    f_a=2F_a/g,    r_b=R_b/g,    rho=sigma/g,
    S_{j,a}=s_{j,a}/g,    V_{j,b}=2sqrt(m)t_{j,b}/g^3.

Direct differentiation gives the exact lifted equations

    dot g = -sigma g,
    dot zeta = -(1/m)sum_b R_b h_b - sigma zeta,

    dot beta_{j,b} = sigma [x_b-(j+1)beta_{j,b}
                                   -sum_{i<j}nu_i beta_{i,b}],

    dot alpha_{j,b} = (2/sqrt(m)) R_b zeta odot(1-h_b^2)
                -sigma [(j+2)alpha_{j,b}
                                   +sum_{i<j}nu_i alpha_{i,b}].     (19)

The first gate equation is

    dot x_a = -4/(m g^2) sum_b R_b C_{ab}
       (1-x_a^2) odot (1-x_b^2) odot {
         G^T[zeta odot(1-h_b^2)]
         -2/(sqrt(m)g^2) sum_j nu_j beta_j t_{j,b}
       }.                                                        (20)

For each query let K(g)=2/(sqrt(m)g^2). Its preactivation and the second
gate derivative are

    z_{2,a}=G x_a-K(g)sum_j nu_j alpha_j s_{j,a},

    dot s_{j,a}=E[((dot beta_j)^T x_a+beta_j^T dot x_a)/k],

    dot h_a=(1-h_a^2) odot {
       G dot x_a-K(g)sum_j nu_j[
           (dot alpha_j)s_{j,a}+alpha_j dot s_{j,a}
                                  +2sigma alpha_j s_{j,a}]
       }.                                                        (21)

The sign and coefficient of the last term follow from dot K=2sigma K.
For example, the G part of (20) has prefactor g^(-2), while its memory
part has prefactor g^(-4). Substitution of dot s into (21) adds at most a
further g^(-2), so the largest inverse-clock power in the expanded local
velocity is g^(-6). The local degrees remain 8 for dot x, 9 in the
dot-s integrands, and 11 for dot h; the low-moment grade remains s=9.
The scalar norm sigma is again Lipschitz in its finite residual vector.

Use precisely the same decorated trees, replacing c,A,B colors by
zeta,alpha,beta. The normalization of their contractions is fixed once R_G
is fixed and does not use T. All exact moment coordinates remain in [-1,1].
Expanding (19)–(21) yields coefficient envelopes, for a computable C>=1,

    sum_U |a_{T,U}(q_low,g)|
                         <= C(1+g^(-6)) deg(T),

    coefficient Lipschitz bound on g>=g_0
                         <= C'(1+g_0^(-7)) deg(T).              (22)

The constants depend on k,m,H,M,R_G and Y. They include the same k-per-new-
vertex and G scaling factors discussed in section 4. To check (22), expand
the finite formulas; all dependence on g is through powers g^(-j), j<=6,
and R=2F-g y. On the clipped low-moment cube, F,s,t and each constituent
moment of dot s are bounded. Products have bounded derivatives there,
sigma has a uniform Lipschitz constant, and differentiating g^(-j) adds
at most one inverse power. Increasing C,C' covers all sums and products.

In (13), replace the fixed penalty coefficient a by the fixed function

    a(g)=C(1+g^(-6)),

and replace the clock equation by

    dot ghat=-sigma(pi(qhat_low),ghat) ghat.                     (23)

All coefficients of this new D-th closure are now independent of T. Since
every clipped F_b has magnitude at most one and 0<ghat<=1,

    0<=sigma<=2+Y,
    exp[-(2+Y)t]<=ghat(t)<=1.                                  (24)

The same bound holds for the exact g. The invariant moment box |qhat|<=2
still follows at each time from the matching coefficient envelope and
penalty. Equations (22)–(24) imply bounded locally Lipschitz coefficients
on every finite time interval; therefore this one autonomous closure is
globally well posed for every D.

Fix T only for the convergence analysis. On [0,T], take the constants in
(14)–(18) from (22) with g_0=exp[-(2+Y)T]. The outward penalty still has a
nonpositive contribution to the moment error even though its coefficient
depends on ghat. The clock error satisfies a finite Lipschitz inequality
in the low moments and clock itself. Hence the complete proof of section 6
applies without changing the ODE: for this same hierarchy,

    for every fixed T,   sup_(0<=t<=T) E_9(t)
                              <= C_T exp(-c_T D),  c_T>0.        (25)

Read the prediction as fhat_a=2pi(qhat_(zeta h_a))/ghat. By (24), on [0,T]
its error is at most

    2 exp[(2+Y)T] |F_a-pi(qhat_(zeta h_a))|
      +2 exp[2(2+Y)T] |g-ghat|,

so outputs and training loss retain the rate (25). The tree count and
deterministic initialization arguments are unchanged: at time zero g=1,
zeta=alpha=0, beta=B and the gates are those already used.

A single finite-precision initialization schedule also suffices for every
fixed T. Set the maximum initial moment error to eta_D=exp(-D), projecting
the computed initial moments into [-1,1] if necessary. In the slab proof,
the old error is amplified by at most C_1 exp(C_2 d_j), where
d_j<=alpha^j D and alpha<=min(1/4,c_2/(4C_2)). Hence the total contribution
of initial error after J slabs is at most

    C_1^J eta_D exp[C_2 D sum_(j>=1) alpha^j]
       <= C_T eta_D exp(c_2 D/3),

because alpha<=1/4. Here c_2=log(2)/(2r), r=10, is independent of T.
Thus eta_D=exp(-D) leaves an exponentially small initialization term for
every fixed T. The analysis parameters alpha,J may depend on T, but this
initialization rule and the ODE do not. The tensor quadrature of section 7
then has cost exponential in D with an exponent depending on the seed
dimension, rather than requiring superexponential precision in D. It still
has the stated curse in k and does not establish practical initialization.

This removes the target-horizon dependence of the bounded-mark family.
It does not remove dependence of the accuracy exponent on T, k, or R_G,
and it does not settle Gaussian cutoff removal or the whole-circle decoder.

There is also no need to truncate w(0) in the target of this finite-query
theorem. Once x_a(0),h_a(0) are initialized, w is absent from (19)–(21).
For bounded G, these gates and all normalized local coordinates are bounded
even when w(0) has its full Gaussian law. Thus the same theorem applies to
bounded G and untruncated Gaussian w(0), with the same evolution constants.
Only the initial integrals use w(0). To compute them deterministically, cut
off the Gaussian w tail for quadrature alone and allocate its probability
to the initialization error: because every integrand has magnitude at most
one, replacing a tail of probability p by a fixed in-box seed changes each
moment by at most 2p. For bounded G, initial gates have a global Lipschitz
bound in w(0), so the cell quadrature estimate from section 7 still applies.
This is an approximation to initial aggregate values, not a change to the
target dynamics. The remaining Gaussian evolution gap is therefore the
unbounded matrix G. This corollary does not assert a uniform circle decoder.
