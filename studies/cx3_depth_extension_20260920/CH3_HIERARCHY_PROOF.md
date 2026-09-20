# C-X3: typed observable closure and numerical convergence

Frozen scoped author result, 2026-09-20. This is a proof candidate, not an
independent review or a promotion. No implementation or computation is claimed.
Scientific inputs used: CONTRACT sections 2, 3, 5; maintained
`docs/global_nonlinear.md` C-H1/C-H2/C-H3 (C.4.7.8--10), and its maintained
fixed-depth C.1/C.2 and Gaussian-program dependencies; `docs/NOTATION.md`;
`docs/special_data_limits.md` III.F.1--9. No other study or agent draft was used.

**Result.** The exact finite-feature construction, complete multi-edge Gaussian
initializer, all numerical limits at fixed feature order, and a conditional
order-convergence theorem extend to every separately fixed finite depth.
The condition for order convergence is a strong target with bounded raw norms,
bounded readout, and resolution-independent Gaussian tails for every backward
query. The maintained C.2 supplies the needed local Euler source bounds; the
completion argument below gives the corresponding mathematical onset target
for every circle law and each fixed finite dataset. Identification of that
target with actual finite GF/GD is a separate dependency. No extension through
a fitting horizon follows unless its source/tail and continuation hypotheses
are established there. Fixed-dimensional numerical convergence needs none of
those infinite-order tail hypotheses. Actual code and operational validation
remain obligations of the supervising task.

## 1. Types, target, and admissible observations

Fix L>=2 and d<infinity, |u|=1, |y|<=1, and a probability training law mu.
There are L probability spaces with H_ell=L2(Omega_ell). The row w is in
H_1^d, the readout c is in H_L, and

    A_ell=A_ell,0+K_ell : H_(ell-1) -> H_ell,  2<=ell<=L,

where only K_ell is Hilbert--Schmidt. The initialized actions are those of
the independent normalized Gaussian matrices, and each reverse is the actual
adjoint. It suffices to use the proved bound ||A_ell,0||<=10. No spectral-edge
constant 2 is needed. Let phi=tanh, G=phi'=1-phi^2, and define

    Z_1(u)=w.u, H_1(u)=phi(Z_1(u)),
    Z_ell(u)=A_ell H_(ell-1)(u), H_ell(u)=phi(Z_ell(u)),
    f(u)=E_L[c H_L(u)], r(u,y)=f(u)-y,
    q_L(u)=c, Delta_L(u)=G(Z_L(u))c,
    q_ell(u)=A_(ell+1)^* Delta_(ell+1)(u),
    Delta_ell(u)=G(Z_ell(u))q_ell(u),  ell=L-1,...,1.

The target equations are

    w'=-2 integral r Delta_1 u dmu,
    K_ell'=-2 integral r Delta_ell tensor H_(ell-1) dmu,
    c'=-2 integral r H_L dmu.                              (1)

Every expectation contracts one population; a tensor a tensor b means
v -> a E[bv]. The initial row is g~N(0,I_d), and c=0,K_ell=0.
This zero readout is only the population initialization.

Admitted observation graphs have a fixed finite number of typed instructions:
the current row/readout, frozen initial forward fields, affine combinations,
bounded Lipschitz scalar functions, products with a bounded continuous gate,
and either orientation of a named edge on a square-integrable preceding
field. Bounded products have their actual deterministic syntax envelopes.
There is no unrestricted product of two L2 fields. Output tuples lie within
one population. Their quadratic contractions, and tuples of initial/current
hidden fields at the same row and input, are included. Inputs can range over
the whole sphere. No cross-layer pairing is defined.

## 2. Determining language, complete initialization, and filters

Use the following initialized alphabet: constants on all L populations;
g_1,...,g_d on population 1; rational affine combinations; sin, cos and tanh;
products of two bounded words; and A_ell,0 or A_ell,0^* on bounded words of
the correct population. Constants and gate outputs have bounded sort; root
and action outputs have L2 sort. A bounded word is also L2. Each action stores
both its edge identity ell and its orientation. An interior population has
two incident edges, so its population type alone does not determine the edge.

Here is a literal countable finite-prefix convention. Encode trees as finite
strings over a fixed finite alphabet: constructors, parentheses, separators,
and binary integers for edge/coordinate indices and rational numerators and
positive denominators. Retain valid bounded expressions in increasing string
length, then lexicographic order, through length N. Include constants at
every order and a fixed finite pilot union if desired. Decode and check types
using syntax alone; combine literal duplicate expressions, never empirically
equal values. All dependencies of retained expressions are compiled. Every
finite rational word occurs, each prefix is finite, and retained raw lists
are nested. A pilot may include forward tanh chains from each g_i through
all layers, followed by tanh(A_ell,0^* H_ell^0(e_i)) for every edge. It exposes
both orientations at finite order without asserting that this core is dense.
One may, in particular, enrich each order by all total-degree-at-most-N
Chebyshev products in the forward anchor fields H_ell^0(e_i), and, when
ell<L, tanh(A_(ell+1),0^* H_(ell+1)^0(e_i)). These are bounded initialized
words; the Chebyshev recurrence and T_k(cos t)=cos(kt) give bound one on
their products. Their nested addition leaves every density/filter proof
below unchanged. Any fixed effective causal natural-number encoding with
an exhaustive bounded prefix is equivalent for these proofs to the literal
string encoding just specified; neither its counting rate nor a core-only
density assertion is used.

All joint initialization laws and contractions are computed from ONE finite
typed union, including every retained word and A_ell,0 applied to every
retained raw word in population ell-1. Append reverse queries as diagnostics
if wanted; they use the same union. Write psi_ell,N for the bounded raw feature
column, with length r_ell. At each edge maintain two source families: xi^ell
on population ell for forward calls and zeta^ell on population ell-1 for
reverse calls. Different matrix/orientation families are independent centered
Gaussian families, independent of g. Within a family, covariance is the full
uncentered input Gram. At its next forward or reverse call the exact rule is

    A_ell,0 b = xi_b^ell
       + sum_(old reverse calls j on edge ell) d_j E_(ell-1)[partial_(zeta_j^ell)b],
    A_ell,0^* d = zeta_d^ell
       + sum_(old forward calls i on edge ell) b_i E_ell[partial_(xi_i^ell)d]. (2)

Derivatives act on the complete earlier coordinate expression, including
response paths through other edges. Freeze all covariances, contractions and
previous response coefficients. Each named source is a separate formal slot,
also at singular covariance. There is no derivative through an expectation or
through the opposite-population operand of a source call.

For an old covariance C and extension (b,v), positivity of the input Gram
implies b perpendicular to ker C and v-b^T C^dagger b>=0: test the quadratic
form on (tz,1), z in ker C, then complete its square on ran C. Thus the new
source can be b^T C^dagger xi+sqrt(v-b^T C^dagger b)G. Formula (2), with this
extension, defines every finite joint law including duplicate queries. The
initialization theorem used here is III.F.1--7: fixed programs of finitely
many independent Gaussian matrices, reused transposes, independent roots and
C1 coordinate maps with bounded derivatives have joint same-layer W2 limits;
their canonical actions are bounded and their reverse maps are adjoints.
Its hypotheses hold because each product of bounded parents can be smoothly
extended outside their fixed ranges with bounded derivatives. All our other
coordinate maps have bounded derivatives. At any fixed graph, values have
linear Gaussian growth and named derivatives have finite deterministic bounds.
Thus every expectation in (2) and every initialization contraction exists.

On population ell, retain JOINTLY all its roots and incident source families.
In particular, at 1<ell<L, xi^ell and zeta^(ell+1) are independent source
families but their resulting feature values must be evaluated in one joint
population cloud: nonlinear response expressions can depend on both. Independent
resampling of different feature columns, or of the two factors of a same-layer
contraction, gives a different law. Populations themselves have separate clouds.

Set eta_N=1/[1024(N+1)^2]>0 and define

    G_ell=E_ell[psi_ell psi_ell^T],
    L_ell L_ell^T=G_ell+eta_N I,  L_ell lower triangular with positive diagonal,
    b_ell=L_ell^{-1}psi_ell,
    C_ell=E_ell[psi_ell (A_ell,0 psi_(ell-1))^T],
    D_ell=L_ell^{-1} C_ell L_(ell-1)^{-T}.                (3)

The right transpose in D_ell is essential. Define, for proof only,
U_ell v=b_ell^T v and Q_ell=U_ell U_ell^*. Since

    U_ell^*U_ell=I-eta_N L_ell^{-1}L_ell^{-T}<=I,

these maps are contractions, D_ell=U_ell^* A_ell,0 U_(ell-1), and
||D_ell||op<=10. D_ell^T represents the actual reverse contraction.

Bounded rational words span a dense subspace of the L2 spaces generated by
the initialized language. Indeed finite-coordinate cylinders are dense by
the monotone-class approximation of indicators, then simple functions and
truncation. Sine/cosine tests of rational affine combinations of a finite
tuple are dense in its L2 law: an orthogonal L2 function defines a finite
signed measure with zero Fourier transform (first extend rational frequencies
by continuity); Gaussian convolution gives zero density, and shrinking the
convolution gives zero against bounded continuous tests, hence zero measure.
Real coefficients and directions are obtained by L2 approximation along each
fixed graph, using bounded actions, Lipschitz gates and product envelopes.
Thus the rational language has the same completion as the real language.

Writing S_N a=psi_N^T a, diagonalization of G_N gives, for a vector in an
earlier raw span padded by zeros,

    ||(I-Q_N)S_N a||2 <= sqrt(eta_N)|a|/2.                (4)

The inequality is eta sqrt(lambda)/(lambda+eta)<=sqrt(eta)/2. Density and
||I-Q_N||<=1 prove Q_ell,N -> I strongly. Both initialized action directions
preserve these spaces: apply an action first to bounded words, then use
density and boundedness. Adjunction makes them a reducing collection.

The current determining hierarchy uses the analogous finite current word
programs, current w,c, frozen initial forward words, all edge identities and
both orientations, with full same-layer joint laws. It is determined by
bounded sine/cosine tests of finite tuples, rather than by power moments.
Saturations T_R(v)=R tanh(v/R), at rational R->infinity, recover an L2 operand
and its action. This is relevant at depth three: Delta_2 is generally unbounded,
so A_2^*Delta_2 is NOT a single bounded-operand word. It is the L2 limit of
A_2^*T_R(Delta_2), with Delta_2 itself recovered from its gate and q_2.
Iterating this procedure recovers every field of (1), and all the admitted
observation graphs. No finite bounded-operand alphabet is falsely claimed
to contain an exact unbounded backward product followed by an action.

Equality of all current joint laws defines unital L2 isometries between the
generated spaces: send a bounded Borel function of a finite tuple to the
same function of the matching tuple, then complete. Joint laws make this
well-defined even for expressions equal almost surely. The isometries preserve
bounded multiplication, roots and all action directions by density. Hence
they determine the dynamically relevant state up to these isometries. If a
reached strong target has the tails of section 5, restarted Euler steps stay
in these spaces and converge to the continuation by the comparison proved
there. Its HS increments remain in the corresponding operator blocks.
Transport of that continuation by the isometries gives matching predictions
and joint observations, with uniqueness from the same one-reference estimate.
This establishes determining reached-state information, not well-posedness
of arbitrary formal characteristic-function arrays or arbitrary switched laws.

## 3. Exact finite-feature law state and equations

Save L complete populations and L-1 coefficient matrices:

    Gamma_1=Law(b_1,g,w),      g,w in R^d,
    Gamma_ell=Law(b_ell),      1<ell<L,
    Gamma_L=Law(b_L,c),        c in R,
    M_ell in R^(r_ell by r_(ell-1)), 2<=ell<=L.            (5)

Intermediate populations are STATIC JOINT MARK LAWS, not omitted populations.
The static D_ell and dictionary/arithmetic descriptions are fixed inputs.
Initially w=g,c=0,M_ell=D_ell. All b coordinates and g are frozen. Current
hidden fields are recomputed, not independent state coordinates.

For every u, compute the following contractions using the saved population
for each expectation:

    H_1=phi(w.u),                 a_1=E_1[b_1 H_1],
    Z_ell=b_ell^T M_ell a_(ell-1), H_ell=phi(Z_ell),
    a_ell=E_ell[b_ell H_ell],      ell=2,...,L,
    f_N=E_L[c H_L],               r_N=f_N-y,
    Delta_L=c G(Z_L),             d_L=E_L[b_L Delta_L],
    q_ell=b_ell^T M_(ell+1)^T d_(ell+1),
    Delta_ell=G(Z_ell)q_ell,       d_ell=E_ell[b_ell Delta_ell],
                                 ell=L-1,...,1.          (6)

Unused a_L,d_1 can be omitted. Set Z_1=w.u in the backward recursion. The
autonomous evolution is

    w'=-2 integral r_N Delta_1 u dmu,
    c'=-2 integral r_N H_L dmu,
    M_ell'=-2 integral r_N d_ell a_(ell-1)^T dmu.          (7)

Gamma_1 and Gamma_L are pushed forward along these endpoint characteristic
velocities; the other Gamma's remain fixed. This is a finite-feature closure
containing probability laws. It is explicitly NOT yet a finite scalar state.

At fixed N all feature envelopes k_ell=sup|b_ell| are finite. On bounded
sets of (w-g,c,M) in L-infinity x L-infinity x finite matrix spaces the
right side is locally Lipschitz. Every hidden/bwd field is obtained from
bounded marks, tanh/gates, finite matrix products, and probability integrals.
The unbounded g appears only inside tanh and fixed first-row coordinates.
Picard contraction on a sufficiently short interval constructs the unique
characteristic solution. The following bounds continue it for every finite T.

The state metric is the sum of endpoint L2 squares and coefficient Frobenius
squares. The loss gradients are exactly minus (7): variation of M_ell gives
delta f=d_ell^T delta M_ell a_(ell-1), by the reverse recursion, and the
endpoint variations give Delta_1 u and H_L. Therefore

    loss_N'=-||w'||2^2-||c'||2^2-sum_ell ||M_ell'||F^2,
    loss_N(0)=integral y^2 dmu<=1.                       (8)

The curve chain rule is justified by bounded-multiplier continuity, adjunction
and the rank identity; bounded input/readout and compact time intervals justify
the training integral. In particular, for 0<=t<=T,

    ||c(t)||infty<=2t,
    ||w(t)-g||2^2+||c(t)||2^2+sum ||M_ell(t)-D_ell||F^2<=t,
    ||M_ell(t)||op<=10+sqrt(t).                          (9)

The second inequality is Cauchy--Schwarz applied to the integrated full
velocity and (8). It avoids a depth-dependent polynomial differential
inequality for the matrix norms. At fixed N, (9), the feature envelopes and
the backward recursion bound w-g in L-infinity on each finite interval.
They also bound c,M in the local existence norms. Cauchy endpoints and another
Picard interval prevent finite-time escape.

Under the common-carrier interpretation,

    B_ell,N=Q_ell,N A_ell,0 Q_(ell-1),N,
    K_ell,N=U_ell,N(M_ell-D_ell)U_(ell-1),N^*,
    A_ell,N=B_ell,N+K_ell,N.                             (10)

Thus ||K_ell,N||HS<=||M_ell-D_ell||F and
||A_ell,N||op<=10+sqrt(T), uniformly in N. The learned increment equation
is precisely the corresponding rank equation with Q_ell on its output
and Q_(ell-1) on its input. Bounds (9)--(10), including the sum of squared
increment norms, are resolution-independent; feature supremum bounds are not.

At a restart retain every population's complete current joint law, all frozen
marks and M,D. The same vector field is locally Lipschitz on the reached
bounded characteristic class. Couple identical current coordinates and apply
uniqueness to identify its continuation with the original restriction. No
new initialization, past velocity, clock forcing, or target state is needed.

## 4. Actual finite arrays and their metric

Replace each Gamma_ell's initial joint mark law by a positive weighted rule
{(b_ell,i,g_i if ell=1),pi_ell,i}_{i=1}^{P_ell}, sum pi_ell,i=1. Retain a
single joint vector b_ell,i at each node. Save w_i on layer 1, c_i on layer L,
all matrices M_ell,D_ell, weights, and data. Equations (6)--(7) now mean
ordinary finite sums E_ell X=sum_i pi_ell,i X_i. For represented atomic
training data, the outer integral is its exact finite weighted sum.

Both orientations of edge ell use M_ell and M_ell^T, with the SOURCE
population weights in each contraction. No extra 1/P is inserted when the
weights already sum to one. The exact finite ODE is gradient flow in metric

    sum_i pi_1,i |delta w_i|^2
      +sum_i pi_L,i |delta c_i|^2+sum_ell ||delta M_ell||F^2. (11)

Hence node-coordinate Euclidean mobilities are 1/pi_1,i and 1/pi_L,i,
and matrix mobilities are one. The ODE is smooth and globally exists by
(8) and finite-dimensional continuation. This is a numerical population
rule for the closure, not an original width-n neural network.

For unequal population counts, retained scalar storage (including weights,
both g and w, and both M and D) is exactly

    S=sum_ell P_ell(r_ell+1)+2d P_1+P_L
                       +2 sum_(ell=2)^L r_ell r_(ell-1).  (12)

Finite represented data and exact syntax/metadata add their own storage.
There is no width n. Intermediate populations contribute their full mark
tables and weights even though they have no moving node variables.

## 5. Order convergence: source production and propagation

Here is a precise reusable theorem. Suppose (1) has a strong C1 solution
on [0,T], lying in the initialized generated spaces, with continuous HS
increments, bounded raw/action norms and bounded readout. Assume, for every
ell<L, uniformly in t and passive u,

    ||q_ell(t,u) 1_(|q_ell(t,u)|>R)||2 <= C0 exp(-a0 R^2), R>=1, (13)

where C0,a0>0 do not depend on N or any numerical resolution. A law-averaged
version suffices for one fixed data law and the trajectory comparison; uniform
passive tails also support comparisons between different data laws. Then the
finite-feature laws (5)--(7) converge on [0,T] to this target in sum endpoint
L2 and learned-increment HS norms. Predictions converge in
C([0,T] x S^(d-1)); every fixed admitted same-layer observation tuple converges
uniformly in time in Euclidean W2, with second moments. Initial/current pair
laws under population x training-law averaging, paired RMS and risks converge
uniformly in time. No hierarchy-order rate is asserted.

Proof. Strong convergence of Q and the initialized action bound imply strong
convergence B_ell,N -> A_ell,0 and B_ell,N^* -> A_ell,0^*. Uniform boundedness
makes this uniform on any compact L2 set: approximate the set by a finite net
and bound the distance to that net by the common operator norm. All exact
fields above are continuous in (t,u), by finite forward/backward induction
and bounded-multiplier continuity; their images are compact. Define

    eps_N=sum_ell [sup_(t,u)||(B_ell,N-A_ell,0)H_(ell-1)(t,u)||2
               + sup_(t,u)||(B_ell,N^*-A_ell,0^*)Delta_ell(t,u)||2
               + sup_t||Q_ell,N K_ell'(t)Q_(ell-1),N-K_ell'(t)||HS]. (14)

Each term tends to zero. For the HS term, approximate a fixed HS operator
by finitely many rank-one tensors; strong Q convergence controls their
factors, contraction controls the remainder, and a finite net handles the
compact K_ell' curve. These are errors evaluated on the target solely for
proof. They are never used to initialize, choose N, or evolve the closure.
This proves small omitted sources; density and bounded norms alone would
not prove trajectory convergence.

Let e_N be the sum of row/readout L2 and all increment HS errors. Uniform
action bounds give, by forward induction,

    sup_u (||Z_ell,N-Z_ell||2+||H_ell,N-H_ell||2+|f_N-f|)
                                        <=C(e_N+eps_N). (15)

For an action subtraction use
A_ell,N(V_N-V)+(K_ell,N-K_ell)V+(B_ell,N-A_ell,0)V.
The top backward difference has the same bound since the reference c is
bounded. At each lower layer split

    Delta_ell,N-Delta_ell
      =G(Z_ell,N)(q_ell,N-q_ell)
         +[G(Z_ell,N)-G(Z_ell)]q_ell.

The second term has norm at most
2R||Z_ell,N-Z_ell||2+2 tau_R(q_ell), because Lip(G)<=2 and |G|<=1.
The first is bounded by the next-layer backward error times the bounded
action norm, plus the two corresponding operator/increment sources. Therefore
backward induction yields

    sup_u ||Delta_ell,N-Delta_ell||2
       <=C[(1+R)(e_N+eps_N)+sum_(j=ell)^(L-1)tau_R(q_j)]. (16)

**The cutoff factor is linear in R at every fixed depth.** It is not
(1+R)^(L-1): each gate difference uses the already controlled forward error,
while propagated backward differences are multiplied only by action norms.

For each learned increment subtract its filtered rank equation from (1).
The rank-difference identity
||a tensor b-a0 tensor b0||HS<=||a-a0||2||b||2+||a0||2||b-b0||2
and contraction by Q bound the dynamic term using (15)--(16); the remaining
projection source is in (14). Subtraction of residuals is controlled by (15)
and the common raw ball. Consequently

    D^+ e_N <=C(1+R)(e_N+eps_N)+C C0 exp(-a0 R^2), e_N(0)=0. (17)

C depends on L,T and the target/common bounds, not on N,R. Scalar integration
(or multiplying by exp[-C(1+R)t]) gives

    sup_(t<=T)e_N(t)
      <=CT exp(C(1+R)T)[(1+R)eps_N+C0 exp(-a0 R^2)].       (18)

First let N tend to infinity at a fixed R, then R tend to infinity. The
negative quadratic exponent dominates the positive linear exponent. This
proves convergence. The same estimate with zero initial source gives uniqueness
against any strong competitor on a common bounded ball: only the reference
needs tails. It also proves convergence of its restarted Euler schemes.

For observation graphs, seeds converge by the raw estimate. Frozen initial
fields use w=g and all M=D, so forward induction and strong compact
convergence handle them. Bounded Lipschitz maps and bounded products preserve
L2 convergence. For a bounded continuous gate times an L2 field, subtract
the field difference, truncate the fixed reference field and use uniform
continuity on bounded coordinate sets; tails are uniform along a compact
L2 curve by a finite-net argument. Each action uses the same three-term
subtraction as above, including its actual adjoint. This proves graph
convergence uniformly in time. Couple all nodes of each fixed tuple on their
own common population; then

    W2(Law(V_N),Law(V))^2<=sum_j ||V_N,j-V_j||2^2.         (19)

Quadratic contractions converge by Cauchy--Schwarz. In a paired activation
tuple the initial and current entries are evaluated at the SAME mark and
input. Couple u identically and integrate (19); both activations are bounded
by one. Paired RMS is the L2 norm of their difference and converges by the
reverse triangle inequality. Risks converge from the uniform prediction
bound and bounded labels/readouts. Nothing couples neuron indices across
different populations. This proves the theorem.

## 6. Where the onset source hypothesis comes from, and its limit

The maintained C.2 is a theorem for every fixed depth. Its conclusions
(15)--(16),(36) bound all Euler backward fields by uniform subGaussian norms,
independently of mesh length, atom count/masses, or covariance rank. Its
assumptions are: normalized input Gram bounded by one; tanh with bounded
first two derivatives; independent Gaussian roots/actions; bounded residuals;
and a preliminary common RMS ball. These hold here on an explicitly positive
preliminary interval. Put a=11 and T_ball=min(1/4,1/[8 a^(L-1)]). At every
Euler prefix of total duration <=T_ball,

    ||c||infty<=exp(2T_ball)-1<1, |r|<2,
    ||A_ell||op<=11, ||H_ell||2<=1,
    ||Delta_ell||2<=11^(L-ell), ||w-g||2<=1/2.            (20)

Indeed c's recurrence is C_next+1<=(1+2h)(C+1). While ||A_ell||<=11,
the total HS change in block ell is <=4T_ball 11^(L-ell)<=1/2,
and the total row change is <=4T_ball 11^(L-1)<=1/2. First exit therefore
cannot occur. This verifies an RMS cap S=11^(L-1) and residual cap 2 for C.2.
Choose the smaller positive time T_L supplied by its explicit finite cap
selection (33)--(35). All those constants precede mesh, data and numerical
limits. They depend on L and the fixed initialization/gate bounds only.

The full row update is the vector equation in (1); taking its pairing with
u_a recovers the first-preactivation recurrence used in C.2. Orthogonal
components of g not generated by the training span remain frozen, so this
does not discard the full row or require an inverse input Gram. To obtain a
passive query u, add it with zero training weight to a fixed finite program.
This can be justified by assigning a positive weight delta, renormalizing
the existing weights, then sending delta to zero at this fixed program.
All formulas are continuous in the finitely many coefficients, and C.2's
bounds are independent of delta. Its bounds therefore hold for every passive
query, without a maximum over inputs or source slots. Affine interpolants
are Euler prefixes with one shortened final step, as in C.2.

For clarity, the necessary completion is also available from these bounds.
Take finite laws mu_j tending to a fixed circle Borel mu in W1 and meshes
h_j->0, and construct their common-carrier full-row/HS Euler paths. On their
common bounded ball, the subtraction proving (15)--(17), now without projection
sources and with different data laws, gives

    ||F_mu(theta)-F_nu(theta_bar)||sum
       <=C(1+R)(||theta-theta_bar||sum+W1(mu,nu))+C exp(-aR^2). (21)

For coupled directions u,v, the first forward difference is bounded by
||w-w_bar||2+||w_bar||2 |u-v|. Subsequent forward differences have the same
form with a fixed larger constant. Each backward gate uses its reference
q at v and the preceding cutoff estimate. Residuals also add |y-z|. After
integration over the coupling this proves (21), with no rank or atom-mass
constant. Finite d enters the full-row bound sqrt(d)+1/2 and is fixed.

The preceding-node/interpolant error is at most C h_j in the sum raw metric,
since the raw velocities are uniformly bounded by (20). Integrating (21)
between two Euler paths shows they are Cauchy: first send j,k->infinity at
fixed R, then R->infinity. Continuity of the vector field follows from the
bounded-multiplier lemma, bounded actions, and the HS rank identity. For a
fixed continuous Banach-valued integrand on compact data space, coupling laws
at distance q bounds the integral difference by omega(b)+2||F||infty q/b;
this proves continuity in the law. Thus the Euler integral identities pass
to a strong C1 solution, with continuous HS derivatives. Every Euler step
stays in the initialized generated spaces; closedness passes this to the
limit. Uniform Gaussian tails pass by an almost-sure subsequence from L2
convergence and Fatou's lemma (decrease the tail exponent if needed).
This proves (13), the mathematical all-Borel circle target, its law continuity
and same-law reached-state uniqueness/restart on [0,T_L]. For each fixed
finite d and dataset the identical construction applies. Its restriction
to the training preactivations is the maintained C.1 local population target
by that theorem's uniqueness; the full row is reconstructed as above.

Consequently the hierarchy/order part applies on this mathematical onset
interval to the whole original rational two-arc family and all represented
finite datasets, including singular Grams. The finite-width/GD capture of
the full-row and Borel completion is still a separate theorem; this document
does not replace that capture proof by the closure's numerical convergence.

On a proposed longer horizon T_fit, (20) and C.2's local cap do not prove
(13) through T_fit. Energy bounds alone give L2 bounds and no such tail
control. The exact bridge (17)--(18) shows what must be established: a bounded
strong continuation and a source-tail majorant whose decay defeats
exp(C R T_fit). Gaussian tails suffice. This is a major open dependency for
that branch, not a reason to reset the approximation at intermediate times.

## 7. Complete fixed-order numerical limits

Use distinct parameters: N feature order; epsilon>0 source covariance
regularization; Q initializer cubature; P population replay cubature; m input
quadrature; h time step; p arithmetic precision. None is width n or raw GD
step eta_n. At every fixed N all below are finite constructions.

### 7.1 Initializer and population rules

Compile the complete typed finite union of section 2. For each edge/orientation
append source covariances from the empirical uncentered operand Gram plus
epsilon I, preserving all older operand tables and Cholesky rows. A family
prefix is therefore positive definite even when exact operands are duplicate
or zero. Derive response coefficients by (2), using a formal derivative walk
through coordinate and frozen response edges only. Each population uses one
joint Gaussian rule including ALL incident source groups and its roots.

A concrete rule is the maintained Halton--Box--Muller construction. Its
needed proved fact is: in any fixed Gaussian dimension its empirical measures
converge weakly and have uniformly vanishing tails of every finite polynomial
moment. The proof is the one in C-H3 C.2: radical-inverse digit blocks and
the Chinese remainder rule give box equidistribution; endpoint discrepancy
D_Q=O(log Q/Q) and |log U|<=log(bQ) give, by layer cake, tails bounded by
integrals of t^r exp(-t) plus a uniform decaying boundary term; Box--Muller
turns these into Gaussian polynomial-tail bounds. Splitting into a compact
box and its tail then proves that for converging finite coefficient vectors
theta_Q and continuous F with a common polynomial envelope,

    Q^{-1}sum_i F(theta_Q,z_i) -> E F(theta,Z).            (22)

This includes coefficients computed adaptively on the same cloud.

At fixed epsilon>0, causal induction using (22) and continuity of positive
Cholesky factors proves convergence of every response coefficient, covariance,
joint output, Gram and edge contraction as Q->infinity. Finite expressions
and their formal derivatives have common polynomial envelopes on compact
coefficient sets. One does not refit or resample individual feature columns.
With Q,epsilon fixed, replay the ENTIRE joint mark program on P points using
its frozen factors and coefficients. It refits nothing. Equation (22) gives
W2 convergence of each complete mark law, including g, as P->infinity.

After Q->infinity, send epsilon down to zero. At each induction stage couple
the complete named source vector as C_epsilon^(1/2)Z. Positive semidefinite
square roots are continuous: a subsequential limit is positive and squares
to the limiting covariance, whose positive square root is unique. Continuous
expressions and their polynomial envelopes then give convergence of all next
covariances and formal derivative expectations. This induction retains named
slots and yields exactly (2), even at singular covariance. It assumes neither
singular Cholesky continuity nor pseudoinverse continuity nor rank deletion.

Raw feature envelopes B_ell,i are deterministic syntax bounds. Let
B_ell^2=sum_i B_ell,i^2. Exact AND empirical ridge whitening obeys

    |b_ell|<= B_ell/sqrt(eta_N)=:k_ell.                  (23)

This is uniform in Q,P,epsilon at fixed N; source regularization does not
change the bounded-word envelopes. Ridge linear algebra is continuous.
Hence all successive complete mark laws converge in W2 and all D_ell
converge in Frobenius norm. Empirical marks need not be contraction frames.

### 7.2 Stability at fixed order

For any mark laws satisfying (23), finite E|g|^2 and finite D_ell, equations
(6)--(7) have the characteristic solution proved in section 3. Energy (8)
holds even when the marks do not give contractions. It bounds
||M_ell-D_ell||F<=sqrt(T) and ||c||infty<=2T. At fixed feature envelopes,
recursive pointwise bounds on q_ell,Delta_ell and the row drift depend only
on L,T,k_ell and the common D bounds. Consequently all these finite-feature
backward multipliers are bounded uniformly along every inner numerical
convergence. No target Gaussian tail is required here.

Couple each pair of COMPLETE mark laws on its own population, retaining the
joint (b_1,g). Let rho=sum_ell ||b_ell-b_ell_tilde||2 and let e be the sum
of endpoint L2 errors and all coefficient Frobenius errors. Forward and
backward induction on (6), splitting each matrix/mark/product factor once,
gives field differences <=C(e+rho). Every product contains a bounded
reference factor by the preceding bounds. Direction changes cost C|u-v|;
at the first layer use ||w||2 |u-v|. Training-law coupling therefore adds
C W1(mu,mu_tilde). Integrating the velocity difference yields

    sup_(t<=T)e(t) <= exp(CT)[||g-g_tilde||2
         +sum_ell ||D_ell-D_ell_tilde||F
         +CT(rho+W1(mu,mu_tilde))].                      (24)

C is uniform along each fixed-order convergent inner sequence, but may
depend on N and grow with it. This is the required stability distinction
from the order-uniform estimate (17).

Finite data require exact finite representations or convergent computable
evaluators for coordinates/weights/labels. For rational two-arc laws use the
unchanged C-H3 rational parametrization U(s)=((1-s^2)/(1+s^2),2s/(1+s^2))
and R_*=[[3/5,-4/5],[4/5,3/5]]. Midpoints of rational parameter cells stay
inside their intervals and normalized input domain. Since |U'|<=2,
their W1 error is at most 1/(20m) on the original intervals. Degenerate
intervals remain atoms. Equation (24) removes input quadrature, then
population replay, initializer cubature, and regularization in that order.
Mathematical all-Borel existence does not provide a computable Borel integrator.

### 7.3 Time and arithmetic

At fixed N,epsilon,Q,P,m the exact finite ODE is smooth and has its global
finite-dimensional solution. Apply explicit Heun with intended step h=T/J
and recompute fields on linearly interpolated states. A compact tube about
the exact solution has finite velocity and derivative bounds. On that tube,
the exact Euler defect is O(h^2), and Heun differs from Euler by O(h^2).
Thus while the numerical path stays in the tube,

    e_(k+1)<=(1+Ch)e_k+Ch^2,

so e_k<=C_T h. For sufficiently small h this prevents first exit and also
keeps the stage points in the tube. Interpolation costs O(h). This proves
convergence on the whole horizon. At depth greater than two, no uniform
all-step-size Heun energy bound is asserted or needed.

For each FIXED finite parameter tuple including J, the exact computation is
a finite composition of arithmetic, positive square roots/divisions, and
elementary functions. Use the maintained unbounded integer/rational grid
backend or a backend with the same primitive guarantees: rounded products
and quotients have vanishing local error away from zero denominators;
sqrt is continuous including zero; log on positive arguments, exp, sin,
cos, tanh have terminating range-reduced rational series with uniformly
vanishing errors on compact subsets of their domains. The maintained
C-H3 C.4 supplies explicit algorithms and bounds. In our multiedge algorithm
every source pivot is positive at epsilon>0 and every feature pivot positive
at eta_N>0. A finite list of positive margins ensures eventual success and
coefficient convergence as p->infinity. Exact Halton uniforms lie in (0,1)
and eventually have admissible rounded arguments. At fixed J all exact
Heun values are finite, even if that J is too small for useful accuracy;
sufficient finite resource allowances admit their computation. Normalization
or data validators must use verified rounding tolerances, rather than demand
impossible exact unit norms of rounded circle coordinates.

Induction through the fixed finite computation proves convergence of every
state and observation at its finitely many times. Primitive local uniformity
and compact input/interpolation domains make it uniform in input and between
those times. Thus the precision limit precedes h->0. No diagonal with rapidly
shrinking Cholesky pivots is covered.

### 7.4 Targets, observation topology, and restart

The successive targets, from inner to outer, are:

1. p->infinity: the exact finite arithmetic initializer and exact finite Heun
   computation at the declared N,epsilon,Q,P,m,J.
2. h->0: the exact finite-array ODE at N,epsilon,Q,P,m.
3. m->infinity: that ODE for the fixed represented law, with other parameters
   fixed; omit this limit for exactly represented finite data.
4. P->infinity: the finite-feature characteristic ODE for the complete mark
   laws replayed with Q,epsilon coefficients held fixed.
5. Q->infinity: the finite-feature ODE for the exact regularized initializer.
6. epsilon->0: equations (3),(5)--(7) with their canonical singular-allowed
   Gaussian initialization at fixed N.
7. N->infinity: the target of section 5 on any horizon satisfying its hypotheses.

Accordingly the outermost-first order is exactly

    lim_N lim_(epsilon down to 0) lim_Q lim_P lim_m lim_(h down to 0) lim_p. (25)

At every inner step, (24), finite graph induction and the coupling argument
(19) give predictions uniformly in (t,u), same-layer fixed tuples in W2
with second moments, initial/current hidden pairs under population x data,
uniform-time paired RMS, and risks. A data coupling contributes a vanishing
paired cost since bounded inputs satisfy E|u-v|^2<=2 E|u-v|. The outer step
is section 5. This is an iterated convergence theorem, not a rate, arbitrary
diagonal, automatic resolution chooser or per-run accuracy certificate.

Discard every initialization transcript after extracting finite mark tables,
weights and D. Checkpoints retain (12), represented data and arithmetic
metadata exactly. Identical saved values, arithmetic and future steps produce
identical later finite computations at step endpoints. No previous velocity
or elapsed transcript is queried. At the limiting characteristic level,
uniqueness gives own-state restart; (24) with a nonzero initial-state error
gives convergence of approximate restarts. Over a longer horizon one evolves
the same approximate state throughout. Restarting from the target's exact
intermediate state would be a different, unauthorized convergence argument.

## 8. Finite work, storage, and remaining implementation obligations

Let A be the data quadrature count. Coefficient-first products in (6) give
RHS work bounded by

    O(A[sum_ell P_ell(r_ell+1)+dP_1
                  +sum_(ell=2)^L r_ell r_(ell-1)]+S+A(d+2)). (26)

Two-stage Heun multiplies work by O(J). With data blocks of size B, stage
workspace is bounded by

    O(S+A(d+2)+B sum_ell(P_ell+r_ell)
                               +sum_ell r_ell r_(ell-1)). (27)

A fixed number of state/stage copies changes constants only. Streaming
paired RMS uses this workspace; retaining every pair at every input adds
2A sum_ell P_ell scalars, and saving the whole trajectory would add an
unnecessary factor J. The required solver need not do that.

For a full initialization DAG with K nodes, s named sources and E<=2K+s^2
coordinate/response edges, a conservative equal-cloud-size bound is

    O(QsE+Qs^2+s^3+(Q+P)E
                  +(Q+P)sum_ell r_ell^2+sum_ell r_ell^3) (28)

scalar work, plus Gaussian-rule generation and exact syntax work. All
required edge-contraction calls are counted in K,s. Workspace is bounded
by O((Q+P)(K+s+sum r_ell)+s^2+sum r_ell^2). Count root dimension d as
additional Gaussian-rule coordinates and its tables. Unequal P_ell rules
replace P by their maximum for this conservative bound. These costs can
be enormous but are finite at each fixed resolution and independent of
neural width and elapsed step count.

At p decimal digits and retained magnitudes <=M_*, integer unit storage is
O(p+log(1+M_*)) bits per scalar; exact rational syntax, law descriptions,
weights and metadata have separate finite bit costs. Arithmetic work must
be weighted by integer-operation cost, and elementary-function temporary
fractions need their own storage (the maintained series backend has a
conservative O(p^2 log(p+2)) temporary-bit bound on fixed compact domains).
Bounds on Gaussian-rule endpoints and fixed causal coefficient induction
give finite M_* at each parameter tuple. Resource allowances must increase
when refinements or precision require it. No universal feasible cost-to-
accuracy bound follows from (25).

The mathematical result specifies the multi-edge compiler and equations,
but it does not certify an unexamined implementation. Completion requires
study-owned reusable code, independent deterministic algebraic oracles,
several genuinely enriched bounded validation runs under a prior budget,
own-state restart checks, and timing/memory/conditioning records. These
must exercise both orientations of both edges at L=3 and complete joint
interior marks. The substantive unresolved long-horizon dependency is the
strong target/source control described after (21); numerical Heun convergence
does not prove actual raw-GD capture or substantial fitting.
