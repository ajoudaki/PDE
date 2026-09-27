# Gaussian marks and a common full-circle aggregate decoder

2026-09-27. Scoped theory continuation; no experiment or existing-file edit.
Inputs: the stipulated model in sections 1–3 of
`AGGREGATE_SCALAR_CONSTRUCTION.md`, the complete
`TRUE_AGGREGATE_CONSTRUCTIVE.md` and its audit. Required
conjecture-investigation and rigorous-math skills were read. This is an
internal derivation, not an independent promotion review.

**Result.** The bounded-mark construction can be upgraded to an autonomous
scalar hierarchy converging to the actual Gaussian block population,
uniformly over every compact time interval and the entire input circle.
The construction is independent of the horizon and original network width.
It evolves aggregate tree moments, not particles, law cells, or a dictionary
of initial labels. Two additions suffice: Gaussian cutoff stability and a
union of independent passive-query moment families sharing their training
moments. The second addition also gives polynomial accuracy versus state
count for the bounded-mark full-circle problem.

**Unresolved requirement.** The resulting Gaussian error versus state count
is poor. This does not establish the requested useful polynomial Gaussian
rate or practical initialization. Gaussian convergence and useful Gaussian
complexity are distinct claims here.

**Subsequent same-study extension.** `NEXT_POLYNOMIAL_ROUTE.md` and
`NEXT_POLYNOMIAL_INITIALIZATION.md` use a different, observable-generated
labeled-monomial family to obtain formal polynomial scalar-state and
initialization bounds at fixed k,m,H (H is the stipulated memory order,
also denoted P elsewhere). Thus the poor state-count rate below remains a
limitation of this exponentially counted tree witness, not the strongest
current existence result. The extension still gives no useful practical
bound, no uniformity in the structural parameters, and no polynomial
numerical ODE integration-time theorem. All these results remain internal.

## 1. Exact target, normalization, and permitted approximation

Fix block size k, memory order H, training inputs u_b in the unit disk,
b=1,...,m, and labels with max |y_b|=Y. Initially the k-by-k entries of G
are independent N(0,1/k), the entries of the k-by-2 matrix w_0 are independent
N(0,1), independently of G. Initially c=A_j=0, B_0 has columns
tanh(w_0 u_b), B_j=0 for j>0, and L=1. The target is the population
response-memory closure at this fixed H, not the dense Gaussian model and
not a memory-order limit.

Let g=1/L, zeta=cg/2, alpha_j=A_j g^2/sqrt(m), beta_j=B_j g, and
nu_j=2j+1. For any training or passive input v_a, write

    x_a=tanh(w v_a),
    s_(j,a)=E[beta_j^T x_a/k],
    h_a=tanh(G x_a-K(g) sum_j nu_j alpha_j s_(j,a)),
    K(g)=2/(sqrt(m) g^2),
    F_a=E[zeta^T h_a/k],    f(v_a)=2F_a/g,
    R_b=2F_b-g y_b,         sigma=(sum_b R_b^2/m)^(1/2),
    t_(j,b)=E[alpha_j^T(zeta odot (1-h_b^2))/k].

Expectation is over the common block law, including the actual same G in
each forward and transpose use. Training indices b alone appear in sums
over b. The normalized local equations are

    g'=-sigma g,
    zeta'=-(1/m)sum_b R_b h_b-sigma zeta,
    beta_(j,b)'=sigma[x_b-(j+1)beta_(j,b)
                           -sum_(i<j)nu_i beta_(i,b)],
    alpha_(j,b)'=(2/sqrt(m))R_b zeta odot(1-h_b^2)
                  -sigma[(j+2)alpha_(j,b)
                            +sum_(i<j)nu_i alpha_(i,b)].        (1)

With C_ab=v_a dot u_b, the lifted gate equations are

    x_a'=-4/(m g^2)sum_b R_b C_ab
       (1-x_a^2) odot(1-x_b^2) odot {
          G^T[zeta odot(1-h_b^2)]
             -K(g)sum_j nu_j beta_j t_(j,b)},

    s_(j,a)'=E[((beta_j')^T x_a+beta_j^T x_a')/k],

    h_a'=(1-h_a^2) odot {G x_a'
       -K(g)sum_j nu_j[
          alpha_j' s_(j,a)+alpha_j s_(j,a)'
                              +2sigma alpha_j s_(j,a)]}.       (2)

The initial gates come from the stated initial law. These equations are an
exact chain-rule lift of the target. They preserve moving features. In
particular the derivative of the shared field s is present in h'.

The Legendre memory identities in the source construction give, at all
times where the solution exists,

    |c_i|<=2(L-1),    |B_(j,ib)|<=L,
    |A_(j,alpha b)|<=sqrt(m)(L-1)^2,
    L<=Lambda_T:=1+(Y/2)(exp(2T)-1),     0<=t<=T.              (3)

For completeness, A is the time integral of r_b delta_(2,b) times
P_j(2L(s)/L(t)-1), and B is its analogous initial and time integral with
rho x_b. The polynomial has magnitude at most one on these arguments.
Use |c_i|<=2 integral rho=2(L-1), |r_b|<=sqrt(m)rho, and integrate
2sqrt(m)rho(L-1) to obtain (3). Thus |zeta|,|alpha|,|beta|,|x|,|h|<=1
and exp[-(2+Y)t]<=g<=1. These bounds are independent of G and w_0.

At each approximation degree D, replace G for purposes of the approximating
population by its radial projection G^[R] onto the Frobenius ball of radius
R. The actual target remains uncut Gaussian. This intermediate replacement
must be removed by an estimate; it is not called a Gaussian theorem by
itself. All dynamical coordinates of the final algorithm are expectations
of normalized decorated trees. Quadrature labels may be used to initialize
these expectations and are then discarded.

## 2. An explicit mark-cutoff dependence in the existing tree theorem

For R>=1, normalize every G edge by R. For each bipartite tree T, with
unrestricted numerical labels at its formal vertices, put

    q_T=E[k^(-|V(T)|) sum_labels
              product_edges (G^[R]_(alpha i)/R)
              product_decorations z_v].                      (4)

Decorations z_v are the normalized gates and variables in (1). Degree
counts decorations and edges. Every exact coordinate lies in [-1,1].
Numerical label collisions are included, so these are not independent-edge
or independent-G-transpose approximations.

Differentiating a decoration grafts a rooted tree with at most two new G
edges. Coefficient fields use moments of degree at most s=9, and degree
increases by at most r=10. The exact hierarchy is

    q_T'=sum_U a_(T,U)(q_low,g) q_U,
    deg U<=deg T+10.                                         (5)

All occurrences of G in (1)–(2) are: one transpose in x', two matrix factors
in G x', and at most one matrix factor in s'. Consequently, after edge
normalization, both the coefficient row sum and its Lipschitz constant on
g>=exp[-(2+Y)T] satisfy

    sum_U |a_(T,U)|<=A_T(R) deg T,
    sum_U |a_(T,U)(z)-a_(T,U)(z')|
        <=A_T(R) deg T ||z-z'||_infinity,
    A_T(R)<=C_T(1+R)^2.                                      (6)

The constants include powers of k for new vertex sums, the finite training
and memory colors, and inverse powers of g up to seven in the Lipschitz
bound. They do not include the number of passive queries below. To verify
the R dependence, expand (1)–(2): no term contains more than two G factors,
and products of coefficient moments are evaluated on a fixed cube. Their
derivatives on that cube are bounded. The norm defining sigma is Lipschitz;
no derivative of sigma or inverse residual norm is required.

The finite ODE retains degree <=D, omits higher children, clips each used
moment to [-1,1], and adds the outward penalty

    -a(ghat,R) deg T [qhat_T-pi(qhat_T)],

where pi is scalar projection to [-1,1] and
a(g,R)=C(1+R)^2(1+g^(-6)) bounds the coefficient row sum. It evolves the
single clock ghat'=-sigma(pi(qhat_low),ghat) ghat. The box |qhat_T|<=2 is
invariant, and exp[-(2+Y)t]<=ghat<=1. Thus this is a globally defined
autonomous finite ODE independent of a design horizon. The penalty has
nonpositive contribution to error relative to an exact moment in [-1,1].

The source construction's finite-degree argument can now be quantified in
R. With E_d the maximum error through degree d, including the shared clock,

    E_d(t)<=E_d(t0)+A d integral E_(d+10)
                              +A d integral E_9,             (7)

where A=A_T(R), and all omitted moments are bounded by one. Choose slabs
of length 1/(80A). After the change of variable s=A(t-t0), every constant
in the one-slab argument is independent of A. In particular there exist
C_1,C_2,c_*>0 and alpha in (0,1/4], depending only on the fixed low grade
and grade increment, with c_*<=log(2)/20<1, such that one slab maps control through degree M to
control through degree alpha M with error

    C_1 exp(C_2 d)[delta+exp(-c_* M)],
    C_2 alpha<=c_*/4.                                       (8)

This follows by iterating (7): the j-th coefficient is
(A t)^j product_(ell<j)(d+10ell)/j!, whose sum is
(1-10At)^(-d/10); the unestimated boundary at degree M is exponentially
small when d<=M/4. The term involving E_9 is then handled by scalar
Gronwall on that same slab. No exact moments are inserted between slabs.

There are J<=1+80TA_T(R) slabs. Repeated application of (8) shrinks the
proved degree range by alpha^J and multiplies constants by at most C_1^J.
Increasing C_T gives the following convenient version of the existing
bound, including the output decoder and initialization error <=exp(-D):

    max_queries sup_(t<=T)|f^[R](v)-fhat_(D,R)(v)|
      <=exp[C_T(1+R)^2]
           exp{-D exp[-C_T(1+R)^2]},                          (9)

provided D>=exp[C_T(1+R)^2]. Constant prefactors are absorbed by increasing
C_T. The initialization term is also covered: the total exponent from
successive amplifications is at most C_2 D alpha/(1-alpha)<=c_*D/3, so
exp(-D) remains exponentially small.

Equation (9) is a sufficient bound, not a lower bound on actual error.
Its dependence on R is precisely why cutoff removal does not automatically
give a useful polynomial cost.

## 3. Passive queries need separate families, not mixed query colors

Fix a passive input v. Starting from its output moment E[zeta^T h_v/k],
the exact generator creates only training colors and that one passive
color pair (x_v,h_v). Equation (2) sums over training b; it never inserts a
different passive query. The shared fields s_(j,v) and s_(j,v)' belong to
the same v. Products of those fields likewise introduce no new query.
The training hierarchy is independent of all passive queries.

Therefore for M prescribed passive inputs v_1,...,v_M, retain the union of
M tree families, each having training colors and its own single passive
color. Identify their common training-only coordinates and evolve one
clock. Trees containing two distinct passive-query labels are unnecessary.
This union is closed under (5) before degree truncation.

With

    B_0=64(m+mH+5)^2,

a conservative scalar state bound is

    N(D,M)<=1+(M+1) B_0^(D+1).                               (10)

This uses the source's decorated-plane-tree count with m+1 queries within
each family. For any individual coordinate, its RHS sees only its own
family and the shared training family. Consequently the row sums,
Lipschitz estimates, clock estimate, and comparison (7), taken in the
maximum over all families, have no factor M. The constants in (9) are
uniform over all passive points in the unit disk because |v dot u_b|<=1.

This is one saved scalar state with an arbitrary-query decoder after
training. The passive points label observables, not representative neurons
or cells of an evolving law. Their initial values are expectations over
the entire initial population. No query family is rerun from time zero
when the decoder is evaluated. The ODE is autonomous and restartable from
its saved moments and clock.

## 4. Gaussian cutoff stability, including its effect on all other blocks

Here the cutoff error is proved independently of a claim that Gaussian
tail mass alone controls trained output.

Couple all capped populations by the same original (G,w_0). Write
Q=||G||_F, and compare cutoffs R' >= R >=1. The normalized local dynamic
state is X=(w,zeta,alpha,beta); do not include the static mark in this
state metric. Define

    d(X,X')=min(1,||w-w'||_F)
              +||zeta-zeta'||_infinity
              +||alpha-alpha'||_infinity
              +||beta-beta'||_infinity,
    e(t)=E d(X^[R](t),X^[R'](t))+|g^[R](t)-g^[R'](t)|.        (11)

All normalized terms are bounded. Initially e(0)=0, since the projected
mark changes no initial w,zeta,alpha,beta or clock. The initial second
gates need not agree on bad marks; they enter the source estimate below.

For every 1<=s<=R, direct subtraction gives, almost everywhere,

    e'<=C_T[(1+s^2)e+M exp(-a s^2)].                          (12)

Here a>0 and M<infinity depend only on the Gaussian mark law and the fixed
structural parameters, not on either cutoff or original network width.
The detailed dependency chain establishing (12) is as follows.

* On Q<=s the two static marks agree. The first gates differ by at most a
  fixed constant times min(1,||Delta w||_F), uniformly for all unit inputs.
  Since beta and gates are bounded, differences of the shared s fields
  are bounded by C e, with a bad-label tail contribution when needed.
* The second preactivation difference on good marks is bounded by
  C_T[(1+s)d+e+|Delta g|]. The tanh map is 1-Lipschitz on the real line.
  Splitting the expectation at Q=s therefore bounds differences of f and
  the t fields by C_T[(1+s)e+P(Q>s)]. Differences of the residual norm are
  bounded by the maximum training output difference.
* The local w velocity contains one transpose G. Subtracting it introduces
  at most another factor s through the second gate difference. Products
  with residual differences cost at most another factor (1+s), yielding
  C_T[(1+s^2)d+(1+s^2)e] on good marks. Equations (1) require no larger
  power. This explicitly includes feedback of the changed law onto every
  good block through the shared fields.
* On Q>s, the two w velocities have magnitude at most C_T(1+Q), since
  radial projection never increases Q. The other normalized velocities
  are bounded by C_T. For the clipped distance in w, its upper derivative
  is bounded by the velocity difference when ||Delta w||<1 and is zero
  away from the clipping boundary when ||Delta w||>1. At the boundary the
  same upper bound holds. The other norm terms obey their ordinary upper
  derivative bounds.
* The Gaussian integral gives E exp(a_0 Q^2)<infinity for 0<a_0<k/2.
  Thus E[(1+Q^2)1_(Q>s)]<=M exp(-a s^2) for a smaller a>0. Polynomial
  factors multiplying the bad-label terms above are absorbed in this
  bound by reducing a once more.

These statements are uniform over the unit disk, although only training
queries are required in the dynamical comparison. Norm changes in the
finite arrays only modify C_T. They establish (12).

Set delta=M exp(-a R^2), d_*=e+delta, and enlarge M to exceed a fixed bound
for d_* on [0,T]. Choose s^2=a^(-1)log(M/d_*) when it belongs to [1,R^2],
and use the closest endpoint otherwise. Equation (12) implies

    d_*'<=C_T d_*[1+log(M/d_*)].                             (13)

The endpoint cases obey the same inequality after enlarging C_T. If
z=log(M/d_*), then z'>=-C_T(1+z). Integrating this scalar inequality, and
using d_*(0)=delta, gives

    sup_(t<=T)e(t)<=C_T exp(-a R^2 exp(-C_T T)).              (14)

All constants can be written as C_T,c_T>0 without hiding cutoff dependence:
neither depends on R. To pass to outputs, the local second-gate subtraction
contains E[(1+Q)min(1,||Delta w||)]. By Cauchy–Schwarz, this is at most
[E(1+Q)^2]^(1/2) e^(1/2). All other terms are bounded by C_T e or Gaussian
mark tails. It follows that

    sup_(t<=T, |v|<=1)|f^[R](t,v)-f^[R'](t,v)|
                         <=C_T exp(-c_T R^2).               (15)

This is a propagated Gaussian-tail estimate, not an unpropagated tail-mass
assertion. Its constants can deteriorate sharply with T and H.

The same argument constructs the uncapped Gaussian flow. For each capped
population the local equations have bounded dynamic coordinates and
|w'|<=C_T(1+Q), so the mean-field integral equations have a unique global
solution by contraction on successive finite intervals. Equation (14)
makes the capped states Cauchy in the bounded metric. Their w differences
are uniformly integrable because the common w_0 cancels and
||w^[R](t)-w_0||<=C_T(1+Q). The velocities have the same integrable
domination. Hence the states converge in L1, uniformly in time after using
their common L1 modulus of continuity. Weighted uniform integrability and
the velocity domination C_T(1+Q) then give convergence of the shared fields
and local velocities in time-integrated L1. The integral equations pass in
C([0,T];L1). Equality at rational times followed by continuity of each
characteristic supplies a common-seed version of the limiting equations.
The resulting solution has the actual unprojected G. Applying (12)
for arbitrary s, then (13) with an initial positive regularization tending
to zero, gives uniqueness among these solutions with the stated bounds.
Taking R' to infinity in (15) proves

    sup_(t<=T, |v|<=1)|f^[R](t,v)-f(t,v)|
                         <=C_T exp(-c_T R^2).               (16)

The Gaussian initial w_0 never needs to be cut off in this dynamical proof.

## 5. A full-circle Lipschitz estimate requiring only Gaussian moments

An explicit bound avoids assumptions about a common analytic strip for
unbounded w_0. This calculation was also supplied by the parallel scoped
obstruction reassessment and was checked directly here.

Let d_T=Lambda_T-1, let Q=||G||op, and set

    Q1=E Q<=sqrt(k),       Q2=E Q^2<=k,
    W1=E||w_0||_F<=sqrt(2k),
    U_T=W1+2sqrt(k)d_T^2 Q1+2sqrt(km)H^2 d_T^4,
    V_T=W1 Q1+2sqrt(k)d_T^2 Q2
                       +2sqrt(km)H^2 d_T^4 Q1.               (17)

The same bounds hold uniformly for radial cutoffs. To prove them, the
transpose contribution to ||delta_1||_2 is at most 2sqrt(k)(L-1)Q.
For the memory contribution, ||B_j||F<=sqrt(km)L and each component of
V_j is at most 2sqrt(m)(L-1)^3. Hence

    ||w'||F<=4sqrt(k)rho(L-1)Q
                         +8sqrt(km)H^2 rho(L-1)^3.

Integrating with dL/dt=rho gives the pathwise estimate

    ||w(t)||F<=||w_0||F+2sqrt(k)d_T^2 Q
                                  +2sqrt(km)H^2 d_T^4.       (18)

Independence of G and w_0 then yields E||w(t)||F<=U_T and
E[Q||w(t)||F]<=V_T.

For two unit inputs u,v,
||h_1(u)-h_1(v)||_2<=||w||F |u-v|. Also

    ||S_j(u)-S_j(v)||_2
                    <=sqrt(m/k)L U_T |u-v|,
    ||A_j||op<=m sqrt(k)(L-1)^2.

Substitution into the second preactivation and then the readout gives

    |f(t,u)-f(t,v)|<=K_T |u-v|,
    K_T=(2d_T/sqrt(k))
                 [V_T+2sqrt(m)H^2 d_T^2 U_T].                (19)

Thus the full Gaussian output, and every capped output, have one common
finite Lipschitz constant on the unit disk for each T. When Y=0 all outputs
vanish and the statement is immediate.

Choose M equispaced circle points u(theta_j). Store their predictions from
the union in section 3, and decode by periodic piecewise linear
interpolation in theta. Since |u(theta)-u(phi)|<=|theta-phi|, the exact
interpolation error on an arc of length 2pi/M is at most pi K_T/M. Indeed
with local fraction lambda it is at most
2K_T lambda(1-lambda)(2pi/M), whose maximum is pi K_T/M. Interpolating
approximate node values adds at most their maximum error. Therefore

    sup_(t<=T, theta)|f^[R](t,u(theta))-fhat_(D,R,M)(t,theta)|
       <=exp[C_T(1+R)^2] exp{-D exp[-C_T(1+R)^2]}
                                               +pi K_T/M.  (20)

No new query-specific evolution is required at readout time.

For fixed bounded R, choose D=O_(T,R)(log(1/epsilon)) and
M=O_T(1/epsilon). Equations (10) and (20) give
N<=C_(T,R) epsilon^(-p_(T,R)) for a finite exponent. This establishes
the bounded-mark full-circle extension without the unfinished Fourier
argument. The exponent and prefactor may still be impractical.

## 6. One actual Gaussian hierarchy for every finite horizon

Combine (16) and (20). For all sufficiently large D relative to R and T,

    sup_(t<=T, theta)|f(t,u(theta))-fhat_(D,R,M)(t,theta)|
      <=C_T exp(-c_T R^2)+pi K_T/M
            +exp[C_T(1+R)^2]
                       exp{-D exp[-C_T(1+R)^2]}.             (21)

The constants are independent of R,D,M and original width. They depend on
the fixed k,m,H,Y,T and dataset. This is an actual Gaussian comparison,
with each approximation axis and its error explicit.

For example, prescribe, without using a design horizon,

    R_D=max(1,[log(D+e)]^(1/4)),
    M_D=D,       initialization error per moment <=exp(-D).  (22)

Then R_D^2 grows as sqrt(log D), whereas the effective propagation degree
is at least D exp[-C_T sqrt(log D)]. For every fixed T this tends to
infinity faster than D^(1/2). The cutoff error tends to zero, as does the
circle interpolation error. Thus this single autonomous sequence satisfies

    for every T<infinity,
    sup_(0<=t<=T, theta in [0,2pi])
       |fhat_D(t,theta)-f(t,u(theta))| -> 0.                  (23)

It uses at most 1+(D+1)B_0^(D+1) evolving real scalar coordinates. At fixed
D its size is unchanged for all elapsed times. The statement is convergence
on each compact interval, not a uniform-in-all-time error claim. H is fixed
throughout; setting H=D would require tracking all H dependencies afresh.

The prescribed initial moments are computable solely from the known
Gaussian initialization and dataset. Compute (4) with radial G projection;
for deterministic quadrature, truncate the original Gaussian seed domain
only during integration and assign an error budget to the omitted mass.
The integrands are bounded by one, radial projection is Lipschitz, and
initial gates are Lipschitz on the finite seed domain. A sufficiently fine
finite tensor quadrature therefore achieves exp(-D) simultaneous error.
Each tree contraction is evaluated by leaf-to-root matrix-vector messages.
Discard all quadrature labels after initialization. This proves finite
computability and coefficient provenance; it does not remove the curse of
the k^2+2k dimensional seed integral.

At fixed T the displayed schedule has a certificate no better than a form
such as exp[-c_T sqrt(log D)] from the Gaussian cutoff term. Since the
retained tree count is exponential in D, this is extremely slow in state
count. Alternatively, after fixing T in the analysis, choosing R^2 as a
small T-dependent multiple of log D yields an algebraic bound in D, hence
still only a logarithmic-type bound in exponential state count. Neither
option proves the requested useful polynomial Gaussian accuracy cost.

### Uniformity for finite empirical block laws

The proof also has a deterministic conditional version for empirical
block laws, with c_0=0 as above. Assume their initial seed laws obey

    E exp[a(||G||F^2+||w_0||F^2)]<=M_seed                 (24a)

for fixed a>0 and M_seed<infinity. In this paragraph E may be a finite
empirical average. Gaussian independence is unnecessary: (24a) supplies
the Gaussian-type mark tail in (12), bounds all second moments, and gives
E[||G||op ||w_0||F] by Cauchy–Schwarz. In (17), replace W1 Q1 in V_T by
sqrt(E||G||op^2 E||w_0||F^2). Every other estimate applies unchanged.
Consequently (21)–(23) hold uniformly over all such empirical laws, with
constants depending on a,M_seed but not their number of original blocks.

For b Gaussian-initialized blocks, the empirical exponential moment in
(24a) has expectation

    M_0=(1-2a/k)^(-k^2/2)(1-2a)^(-k),
    0<a<min(k/2,1/2).

Markov's inequality gives probability at least 1-delta that (24a) holds
with M_seed=M_0/delta, for each b, with the same bound independent of b.
This is not a simultaneous event over every possible b and is not a
deterministic guarantee for arbitrarily bad Gaussian realizations.

For an empirical target, initialize each retained moment by its empirical
average of the clipped-mark tree expression, computed in one pass through
the initial blocks, then discard those blocks. This initialization costs
work proportional to the available data size, while the evolving state
has the same bound (10). Using population Gaussian initial moments instead
would compare to the population target and requires a separate sampling
error estimate to compare with that particular finite realization. This
extension does not silently equate those initializations. Finite-width
nonzero initial readout requires a further initial-perturbation argument;
the present theorem retains the explicitly stated c_0=0 target.

## 7. Why naive Gaussian Lp normalization does not close the rate gap

One tempting alternative retains uncut G and normalizes a tree with e
edges by a Gaussian mark moment. Since gates and normalized dynamic
coordinates have magnitude at most one, a safe bound is

    |q_T|<=mu_e:=E||G||F^e.

For Q=||G||F, k Q^2 has the chi-square density with k^2 degrees of freedom.
Its elementary radial Gaussian integral gives the exact ratio

    mu_(e+2)/mu_e=(k^2+e)/k.                                 (24)

Replacing a differentiated decoration can append two G edges. Therefore
the straightforward absolute coefficient estimate after normalization by
mu_e contains a factor

    (number of differentiated factors) (k^2+e)/k.

When e is proportional to total grade d, this grows quadratically in d,
rather than linearly. The finite-propagation proof used above then loses
its positive time slab: repeated coupling produces roughly product j^2
divided by j!, which does not give an exponentially small distant-degree
boundary. Using an Lp bound of the same Gaussian growth only relocates
this factor. It does not remove it.

This is a failure of an absolute-moment proof route, not an impossibility
theorem for the Gaussian dynamics. Boundedness alone really is insufficient
for a generic quadratically coupled hierarchy. For illustration, let E_j be
independent exponentials of rate j^2 and define

    q_d(t)=P(sum_(j=d)^infinity E_j <=t).

The sum is finite almost surely because its expectation is sum j^(-2).
Convolving the first exponential shows

    q_d'=d^2(q_(d+1)-q_d),    q_d(0)=0,    0<=q_d<=1.

This is a nonzero bounded solution, while the all-zero sequence is another
bounded solution with the same initial data. Thus an abstract replacement
of linear grade rates by quadratic rates would need a further boundary or
structural condition; bounds on moments alone are insufficient. This toy
hierarchy is not asserted to arise from the neural model.

Likewise, splitting marks into shells only within a proof does not by itself
repair the rate. The present shell estimate has the schematic form
exp[-D exp(-C R^2)], while the shell probability is exp(-c R^2).
The crossover R^2 of order log D can leave only algebraic accuracy in D.
A shellwise argument based on these same estimates therefore supplies no
fixed polynomial certificate in an exponentially large tree state count.
This is not a proposal to store a shell histogram, and not a lower bound
on all aggregate algorithms.

## 8. Exact remaining obligations and claim status

| Claim | Status in this note |
| --- | --- |
| Actual Gaussian cutoff stability with shared-field feedback | Derived in section 4 |
| Common full-circle decoder using only aggregate dynamics | Derived in sections 3 and 5 |
| One horizon-independent Gaussian hierarchy converging on every compact interval | Derived in section 6 |
| Width-independent dynamical scalar state count | Explicit in (10), (22) |
| Polynomial bounded-mark full-circle state count versus inverse error | Derived, with cutoff-dependent exponent |
| Useful polynomial Gaussian state count versus inverse error | Open |
| Polynomial/practical initialization in structural parameters | Open |
| Uniformity in k, H, or all elapsed times | Not claimed |
| Dense Gaussian identification or memory-order convergence | Outside this result |

The highest-leverage missing estimate is a Gaussian-averaged control of
high-degree feedback that avoids the exp(C_T R^2) deterioration and is
compatible with actual G/G-transpose correlations. Gaussian cancellation
cannot be inserted by treating those reused marks as independent. A useful
alternative would need either a different finite aggregate basis with a
subexponential count at the required grade, or a structural stability bound
that produces exponential low-observable accuracy in the current grade
without a growing mark cutoff in its exponent. The present Lp calculation
does not establish either statement.

This note supersedes only two prior open points: existence of a convergent
Gaussian aggregate sequence, and a common full-circle aggregate decoder.
It does not supersede the prior warnings about useful Gaussian complexity,
initialization, or the absence of promotion review.
