# Polynomial Gaussian state complexity at fixed block dimension

2026-09-27. Scoped theoretical audit of the supervisor's proposed monomial
construction. Inputs are the normalized exact lift and bounds in
`TRUE_AGGREGATE_CONSTRUCTIVE.md` and `NEXT_GAUSSIAN_ROUTE.md`. No experiment
was run for this route. This is an internal derivation, not an independent
promotion review of those inputs.

**Result.** Subject to the Gaussian stability and bounded-mark propagation
lemmas derived in `NEXT_GAUSSIAN_ROUTE.md`, the proposed route is sound as a
polynomial **state-count** theorem for each fixed k,m,H. Expand the exact
observable contractions into local-coordinate monomials, then retain only
constituents reachable by exact differentiation below the degree cutoff. Evolve a
logarithmic number of independent Gaussian-mark cutoffs, and use a continuous
clock-dependent decoder. One horizon-independent family then approximates the
actual Gaussian output uniformly on every compact time interval and the
entire circle, with algebraic error versus its scalar state count.

The count has the curse of the local block dimension. The construction is
not a practical low-order replacement. The subsequent
[analytic-initialization addendum](NEXT_POLYNOMIAL_INITIALIZATION.md) proves
polynomial fixed-parameter initialization work; polynomial numerical
integration work remains unproved. These limitations are explicit parts of
the result, not an effective-compression claim hidden in a fixed-parameter
asymptotic statement.

## 1. Fixed local coordinates and exact moment equations

Fix k,m,H and the training data. Use the same response-memory population,
Gaussian initialization, c(0)=A(0)=0, and normalization

    g=1/L,   zeta=cg/2,   alpha=A g^2/sqrt(m),   beta=B g.

For a radial mark cutoff R>=1, let G^[R] be the projection of G onto the
Frobenius ball of radius R. A local coordinate vector for all training inputs
and one passive input v consists of

    Z = (G^[R]/R, zeta, alpha, beta,
                         x_1,...,x_m,x_v, h_1,...,h_m,h_v).

Every component lies in [-1,1] at all times. The first weights w are absent
after the initial gates are computed. The number of real local coordinates is

    d = k^2 + k + 2kmH + 2k(m+1)
      = k^2 + k(2m+3+2mH).                         (1)

The training-only vector has d_c=d-2k coordinates. Both d and d_c are
independent of original network width and elapsed time, but they grow with
block size, sample count, and memory order.

The available candidate observables, indexed by a in N^d, are the aggregates

    q_a = E[Z^a],      |a|=sum_i a_i.

The expectation includes all joint correlations, including reuse of the same
G in forward and transpose operations. These are current moving-state
moments. No density, particles, quadrature labels, or reference trajectory
is evolved or reconstructed by the closure.

The local equations in `NEXT_GAUSSIAN_ROUTE.md` sections 1–2 are polynomials
in Z with coefficients depending on g and a fixed finite list of moments of
degree at most s=9. The static-mark derivatives are zero. Differentiating

    d/dt Z^a = sum_i a_i Z^(a-e_i) dot Z_i

therefore gives exact moment equations

    dot q_a = sum_b A_ab(q_low,g) q_b,
                         |b|<=|a|+r,    r=10.       (2)

Index summations over k coordinates are finite sums in their coefficients.
There is no tree restriction and no assumption of independence between local
coordinates. On 0<=t<=T, their row sums and coefficient Lipschitz constants
obey

    sum_b |A_ab| <= C_T(1+R)^2 |a|,
    sum_b |A_ab(z)-A_ab(z')|
          <= C_T(1+R)^2 |a| ||z-z'||_infinity.       (3)

To verify (3), each local velocity has at most two G factors, replaced by R
times a bounded normalized coordinate. Its finitely many scalar feedback
fields and their derivatives have bounded coefficients on the clipped low
moment cube and g>=exp[-(2+Y)T]. Differentiating the product contributes
sum_i a_i=|a|. This gives the same degree growth and R dependence as the tree
proof, with different finite constants depending on k,m,H. No factor
depending on the total number of retained moments occurs in the row sum.

For D>=9, start with every monomial constituent of the output and the F,s,t,
and exact dot-s coefficient fields. Repeatedly differentiate every selected
monomial by (2), combine identical monomials exactly, and add every resulting
child of degree at most D. Stop when this finite set is closed. This procedure
enumerates only the observable-reachable family, not the entire ambient
joint-state monomial basis. The fixed numeric coordinate indices combine
graph terms that evaluate to the same monomial.

Every omitted derivative child of a retained row has degree above D; no
feedback path is left at a fixed unrefined depth as D increases. Clip used
moments to [-1,1], set missing children to zero, and apply the degree-majorant
outward penalty from the source construction.
Keep q_0=1 fixed and evolve the cutoff's own g. This is a finite autonomous
ODE with |qhat_a|<=2 and ghat>=exp[-(2+Y)t]. Consequently it is well posed
for all finite times. The normalized coefficient/penalty formulas do not use
a design horizon.

## 2. The bounded-mark estimate survives with polynomial state count

The ambient number of monomials of degree at most D in d coordinates is

    B_d(D) = binomial(D+d,d).                         (4)

This is an upper bound, not an equality, for the generated reachable state.
For fixed d it is O_d(D^d). Counting ambient monomials follows by adjoining the
slack coordinate a_(d+1)=D-|a| and counting weak compositions of D into
d+1 parts. This is a different count from the exponential tree enumeration.
Its price is explicit dependence on the full block-coordinate dimension.

The degree propagation proof uses only the bounded exact coordinates, the
fixed low grade s, the degree jump r, (3), and the clipping/penalty comparison.
It applies to the generated family: below the final boundary, every child
needed by its retained rows is present, all seed moments are present, and
the proof takes maxima only over selected moments in each degree band.
Moments outside that reachable family do not occur in any retained equation.
In particular a computable nondecreasing
function C(t)>=1 can be chosen so that initialization errors at most exp(-D)
in every retained moment give

    sup_(0<=s<=t) |f^[R](s,v)-fhat_(D,R)(s,v)|
       <= exp[C(t)(1+R)^2]
                  exp{-D exp[-C(t)(1+R)^2]},         (5)

provided D>=exp[C(t)(1+R)^2]. The constants are uniform over |v|<=1.

Computable here means computable from the supplied data and the fixed local
polynomial formulas, not fitted from target trajectories. One way to choose
C is to bound both coefficient norms in (3) by a common finite sum of absolute
coefficients, replace every inverse g power by exp[(2+Y)t] to the required
power, use the explicit short-slab comparison constants, and count the
slabs. Increasing a fixed B then permits a smooth nondecreasing majorant of
the form B(1+t)exp(Bt). A nonsharp algorithmic majorant is enough. Merely
naming a noncomputable unknown stability constant would not define the
decoder below.

For M passive circle nodes, retain the union of M generated monomial families, each
with the training variables and one passive gate pair. Share every
training-only moment within this one cutoff population. There is no need to
retain monomials containing two distinct passive inputs: the exact derivative
of one family's moment uses only that family and training fields. The total
moment count is at most

    B_(d_c)(D) + M [B_d(D)-B_(d_c)(D)].              (6)

The sup-norm error estimate (5) gains no factor M. Periodic linear
interpolation between M equispaced circle-node predictions adds at most
pi K_T/M, using the uniform output Lipschitz constant K_T derived in the
Gaussian note. This interpolation is a decoder of current learned aggregate
outputs; it is not reference playback or a fixed activation dictionary.

## 3. A fixed family of independent cutoffs

For every integer D>=9 prescribe

    J_D=floor(log D),   R_j=sqrt(j),  1<=j<=J_D,
    M_D=D.

Evolve all J_D cutoff hierarchies in parallel. They approximate different
self-consistent populations; their training moments and clocks must not be
identified across j. In particular this is not a decomposition into Gaussian
shell populations whose means are combined inside one law. Each hierarchy
has its own residuals, feedback, and clock g_j. Only the final prediction
decoder combines them. All initial moments are computed from the same
prescribed Gaussian seed law after the respective radial projection.

Add one physical-time clock tau with dot tau=1 and tau(0)=0. The full system
is autonomous and restartable from its saved moments, g_j, and tau. Its
dimension does not change when training runs longer. The extra clock is used
only by a prescribed decoder; it does not supply target-trajectory forcing.

Let

    a_D(tau) = min(J_D, max(1, log D / [8 C(tau)])).

At an integer value a_D=j, decode using cutoff j. Between j and j+1, use the
convex linear interpolation of their two circle decoders, with weights
1-(a_D-j) and a_D-j. This is continuous in tau, including at the integer
boundaries. At J_D use that endpoint alone. It involves at most two current
cutoff predictions but all cutoffs have been evolving continuously since
initialization. No cutoff is initialized or restarted at a switching time.

## 4. Algebraic Gaussian error on every compact interval

The Gaussian cutoff result of the source note supplies, for every fixed T,
constants A_T,c_T>0 independent of R and D such that

    sup_(t<=T,theta) |f^[R](t,theta)-f(t,theta)|
                              <= A_T exp(-c_T R^2).  (7)

Write C_T=C(T). For sufficiently large D depending on T, the unclamped value
log D/[8C(t)] lies between one and J_D throughout 0<=t<=T. Every cutoff
index j receiving nonzero decoder weight then satisfies

    log D/(8 C_T)-1 <= j <= log D/(8 C(t))+1.         (8)

The lower bound gives the Gaussian error

    A_T exp(-c_T j)
                    <= A_T exp(c_T) D^(-c_T/(8C_T)). (9)

For the truncation error at time t, apply (5) with its own horizon t and
cutoff sqrt(j), rather than unnecessarily applying C_T to the selected
index at every earlier time. Since j>=1,

    H_j(t):=C(t)(1+sqrt(j))^2 <=4 C(t)j
                                  <=(log D)/2+4C_T. (10)

For log D>=8C_T, this also verifies the applicability requirement D>=exp H_j.
Equations (5) and (10) yield

    truncation error <= exp(4C_T) sqrt(D)
                              exp[-exp(-4C_T)sqrt(D)]. (11)

The bound is uniform over t<=T and is smaller than every fixed inverse
power of D for large D. Each circle decoder adds at most pi K_T/D. A convex
combination cannot increase the maximum of these error bounds. Thus, setting

    eta_T = min(1,c_T/(8C_T)) > 0,

there is a finite A'_T such that the single horizon-independent family obeys

    sup_(0<=t<=T,theta) |fhat_D(t,theta)-f(t,theta)|
                                <= A'_T D^(-eta_T). (12)

The finitely many smaller D can be absorbed in A'_T because both exact and
approximate predictions are bounded on [0,T]. The output normalization
g_j>=exp[-(2+Y)T] supplies the latter bound independently of j and D.

The complete scalar state count, including all cutoff clocks and tau, obeys

    N_D <= 1+J_D {1+B_(d_c)(D)
                    +D[B_d(D)-B_(d_c)(D)]}
         = O_d(D^(d+1) log D).                       (13)

In particular N_D<=C_d D^(d+2) for D>=9, so (12) implies the conservative
algebraic state-count guarantee

    error on [0,T] <= A''_T N_D^(-eta_T/(d+2)).       (14)

This establishes a polynomial inverse-accuracy scalar-state bound at fixed
k,m,H,T. The ODE family, cutoff list, query grid, and initialization schedule
are fixed by D alone; T occurs only in the guarantee. It is not a uniform
all-time guarantee, uniformity in k or H, or identification with the canonical
dense-Gaussian network. The memory-order limit remains separate.

## 5. Initialization, precision, and practical limitations

The normalization and coefficient provenance need only the modifications
already stated: use G^[R_j]/R_j as local coordinates and allow each cutoff its
own self-consistent fields and clock. The exp(-D) initial-moment accuracy
schedule used in (5) suffices for every cutoff, and the source short-slab
argument shows it remains sufficient when the useful cutoff grows like
sqrt(log D). No future information or target trajectory is used.

At time zero these are finite Gaussian seed integrals in k^2+2k variables.
The integrands are bounded by one. Truncate the original seed tails only
for quadrature, allocate their total probability to the initialization error,
and use finite quadrature for the remaining Lipschitz integrands. Radial
projection is Lipschitz and the initial gates are smooth; a simultaneous
exp(-D) guarantee is therefore computable. Discard the quadrature labels.
Known exact initial zeros from zeta, alpha, and higher beta orders can be
used without approximation.

The elementary Lipschitz tensor-grid initialization currently available has
mesh size proportional to exp(-D) divided by a degree-dependent Lipschitz
bound. Its node count is exponential in D at fixed seed dimension. Thus
polynomial state count alone therefore does not imply polynomial
initialization work. The separate
[analytic-initialization addendum](NEXT_POLYNOMIAL_INITIALIZATION.md)
subsequently supplies the missing regularity/complexity proof: split the
radial integral at the cutoff and use analytic quadrature on each piece.
It gives polynomial fixed-parameter work, still with a severe dimension
exponent. The Lipschitz-grid estimate here is retained as the weaker bound
which that addendum supersedes.

Exp(-D) storage precision itself costs only O(D) bits per normalized initial
moment, so the theorem does not hide an arbitrary-precision real-number
encoding. Total bit storage is still polynomial in D. That observation
does not certify the cost of obtaining those bits. Nor is a polynomial
floating-point integration-time bound proved: large degree and small clocks
can cause stiffness and severe conditioning. An exact-ODE state-count theorem
must not be reported as a solver-work theorem.

The dimension dependence is already severe in the smallest tested two-input
case: k=4,m=2,H=1 gives d=60 and d_c=52. The ambient degree-nine bound for one
template is binomial(69,9)=56,672,074,888. This is a bound, not a measured
reachable count, and no claim is made that every such moment is retained.
The theoretical O(D^61 log D) whole-circle upper bound has a large exponent
even there. By contrast, the separately implemented
complete-feedback depth-one model has thousands of training moments. This
monomial theorem supplies no claim that the affordable depth-one model
inherits (14).

## 6. Admissibility and the earlier full-law-basis exclusion

`TRUE_AGGREGATE_GAUSSIAN.md` section 5 excluded enumeration of all monomials
of the joint block state and required a substantially smaller,
observable-relevant family. The later `TRUE_AGGREGATE_ASSESSMENT.md` section 1
clarified that possible law determination by an infinite moment sequence is
not itself disqualifying; the operational questions concern the finite
evolving statistics, observable error, and total computation. Both points
matter here.

The present revised construction directly generates only the observable and
feedback dependencies. It stores no law masses or density coefficients and
does not reconstruct a law at runtime. Its monomials are not an invertible
recoding of a particle or histogram array. The ambient monomial family is
used only to count a containing set. These facts justify studying it as an
aggregate-moment candidate under the later operational criterion.

They do not prove that its reachable set is substantially smaller than the
ambient basis on difficult instances, or that the user-requested practical
effectiveness has been achieved. If the earlier requirement is interpreted
as a mandatory quantitative reduction relative to all joint moments, that
additional requirement remains unproved. Polynomial state complexity at
fixed block dimension must not be substituted for that practical claim.

## 7. Audit outcome

| Assertion | Status |
| --- | --- |
| Observable-generated local monomial hierarchy uses current aggregate moments | Exact construction |
| Degree jump and linear-degree coefficient envelope persist | Derived in (2)–(3) |
| State count polynomial in degree at fixed block dimension | Ambient combinatorial upper bound |
| Parallel-cutoff decoder is continuous, causal, autonomous, restartable | Explicit construction |
| Actual Gaussian full-circle algebraic error versus scalar state count | Derived from the cited internal Gaussian and propagation lemmas |
| Polynomial fixed-parameter initialization work | Proved in the subsequent analytic-initialization addendum |
| Polynomial numerical solve work at the promised output accuracy | Not proved |
| Useful low-order accuracy or uniformity in structural parameters | Not claimed |

The proposal closes the earlier *state-count rate* gap for fixed k,m,H if the
internal Gaussian cutoff proof is accepted. It does not close the requested
practical-compression gap. Fresh independent proof review would still be
needed before promotion of this theorem or the supporting Gaussian lemmas.
