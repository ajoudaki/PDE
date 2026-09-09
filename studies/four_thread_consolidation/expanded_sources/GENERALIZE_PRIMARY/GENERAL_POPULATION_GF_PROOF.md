# A fixed positive-time population gradient-flow limit

Status: complete proof, independently reviewed by three fresh adversarial
reviewers, all PASS with no required mathematical repair. The detailed response
lemma is GENERAL_DEPTH_RESPONSE_PROOF.md; the review record is REVIEW_RECORD.md.

The time interval in this result is chosen before width and step size tend to
their limits. It is not a claim about every finite time interval. The population
state contains fields and bounded linear operators; it has infinitely many
scalar degrees of freedom.

## Statement and exact finite model

Fix integers d,m and L>=2. There are L hidden layers, each of width n. The m
inputs x_a in R^d are fixed, with ||x_a||_2/sqrt(d)<=X and
G_ab=x_a^top x_b/d. Their Gram matrix may be singular and inputs may coincide.
For squared loss assume |y_a|<=Y. Choose positive weights omega_a with
sum_a omega_a=1 and use

    L_n = sum_a omega_a (f_n,a-y_a)^2,       r_n,a=f_n,a-y_a.

This declares a change from summed loss. For summed loss on m examples, the
same statement applies after multiplying physical time by m.

Each activation phi^(ell):R->R is C^1, with bounded derivative and globally
Lipschitz derivative. Fix common finite bounds

    |phi^(ell)(0)|<=D0,
    |phi^(ell)'(s)|<=D1,
    |phi^(ell)'(s)-phi^(ell)'(t)|<=D2 |s-t|.

The activations themselves need not be bounded. In particular their growth is
at most linear. Nonaffinity is not required for existence.

Concrete examples include arctan, tanh, logistic sigmoid, softplus, exact GELU,
and SiLU, with different choices in different layers. For softplus,
phi'=s and phi''=s(1-s), where s is the logistic sigmoid evaluated at the
argument. For exact GELU phi(t)=t Phi(t),
phi'(t)=Phi(t)+t varphi(t) and phi''(t)=(2-t^2)varphi(t), where Phi and
varphi are the standard normal distribution function and density. For SiLU,
phi(t)=t s(t), phi'(t)=s(t)+t s(t)(1-s(t)) and
phi''(t)=2s(t)(1-s(t))+t s(t)(1-s(t))(1-2s(t)). These derivatives are bounded
because Gaussian and logistic tails dominate the displayed polynomial
factors. The C1,1 class also contains a quadratic smoothing of ReLU: zero for
t<=0, t^2/2 for 0<=t<=1, and t-1/2 for t>=1. Its derivative is bounded and
1-Lipschitz although its second derivative does not exist at both junctions.

For the principal initialization take independent Gaussian first weights
W^(1)_0,ij~N(0,sigma_1^2), independent middle matrices
W^(ell)_0,ji~N(0,sigma_ell^2/n), 2<=ell<=L, and independent readout entries
W^(L+1)_0,j distributed as a fixed random variable with

    sup_(p>=2) (E|W^(L+1)_0,j|^p)^(1/p)/sqrt(p) <= B_out < infinity.

Zero, bounded, and nonvanishing Gaussian readout are all allowed. The first
weights may more generally be iid centered subGaussian variables, with a fixed
subGaussian bound B_in. This extension is justified below; the strict-activity
corollary will use Gaussian first weights. All initialization groups are
independent. Sigma values may be zero in the existence theorem.

Define, with coordinatewise activation,

    z^(1)_a=W^(1)x_a/sqrt(d),       h^(1)_a=phi^(1)(z^(1)_a),
    z^(ell)_a=W^(ell)h^(ell-1)_a,  h^(ell)_a=phi^(ell)(z^(ell)_a), 2<=ell<=L,
    f_n,a=(W^(L+1))^top h^(L)_a/n.

W^(L+1) is always the stored rescaled readout. In particular, for L=2 it is
W^(3), and f_n,a=(W^(3))^top h^(2)_a/n.

The backpropagated fields omit the loss derivative:

    delta^(L)_a=W^(L+1) phi^(L)'(z^(L)_a),
    delta^(ell)_a=phi^(ell)'(z^(ell)_a)
                       [(W^(ell+1))^top delta^(ell+1)_a], ell<L.

Thus delta^(ell)_a=n partial f_n,a/partial z^(ell)_a. Choose fixed finite
kappa_ell>=0. Stored-weight gradient-descent rates are

    eta_n (n kappa_1, kappa_2, ..., kappa_L, n kappa_(L+1)).

The exact updates are

    W^(1)_(k+1)=W^(1)_k
        -(2 eta_n kappa_1/sqrt(d)) sum_b omega_b r_n,b,k delta^(1)_b,k x_b^top,
    z^(1)_a,k+1=z^(1)_a,k
        -2 eta_n kappa_1 sum_b omega_b G_ab r_n,b,k delta^(1)_b,k,
    W^(ell)_(k+1)=W^(ell)_k
        -(2 eta_n kappa_ell/n) sum_b omega_b r_n,b,k
                             delta^(ell)_b,k (h^(ell-1)_b,k)^top, 2<=ell<=L,
    W^(L+1)_(k+1)=W^(L+1)_k
        -2 eta_n kappa_(L+1) sum_b omega_b r_n,b,k h^(L)_b,k.                 (1)

Use physical time t=k eta_n, interpolate these parameters linearly, and
recompute forward quantities between grid points.

There is T_*>0 depending only on L, X, Y, D0,D1,D2, the initialization bounds
and the kappa values, such that for EVERY eta_n>0 tending to zero the following
conclusions hold on [0,T_*]:

1. A unique strong population flow exists in the field/operator state described
   below. It is autonomous and retains each matrix together with its adjoint.
2. Predictions, loss, and all kernel entries converge in probability uniformly
   in time to their population values.
3. Separately for each neuron population, empirical laws of the joint m-input
   hidden paths converge in Wasserstein distance of order two for the uniform
   path norm. This applies to both preactivations and activations.
4. Integrated squared hidden speeds converge. Fixed finite, correctly typed
   forward/adjoint probes assembled from Lipschitz coordinate maps, linear
   combinations, and products of a bounded factor and an L2 field also have
   their joint continuous quadratic-growth measurements converge, provided
   the bounded factors are continuous functions of their arguments.

The constants do not depend on n, eta_n, m, d, or a smallest Gram eigenvalue
when the stated bounds remain fixed. Here m,d and the inputs are nevertheless
fixed in the convergence assertion: no uniform convergence rate for growing
datasets or dimension is claimed. Probe length is fixed; arbitrary products of
two unbounded factors are not part of the probe assertion.

## Population state, construction, and preliminary norm bounds

There is a separate probability space for coordinates in each hidden layer.
The field Z^(1)_a belongs to the first, W^(L+1) to the last. For 2<=ell<=L,
W^(ell) is a bounded linear map from the mean-square space at layer ell-1 to
the one at layer ell. Its adjoint is denoted (W^(ell))^*. Expectations pair
variables belonging to the same population. Define

    (u tensor v)V = u E[v V].

This is the population version of the finite map u v^top/n. The population
forward and backward formulas are those above with uppercase Z,H, expectation
in place of b^top c/n, and * in place of top. In particular

    f_a=E[W^(L+1) H^(L)_a],
    P^(L)_a=W^(L+1),
    P^(ell)_a=(W^(ell+1))^* delta^(ell+1)_a, ell<L,
    delta^(ell)_a=phi^(ell)'(Z^(ell)_a) P^(ell)_a.

The limiting equations are

    dot Z^(1)_a=-2 kappa_1 sum_b omega_b G_ab r_b delta^(1)_b,
    dot W^(ell)=-2 kappa_ell sum_b omega_b r_b
                                  delta^(ell)_b tensor H^(ell-1)_b, 2<=ell<=L,
    dot W^(L+1)=-2 kappa_(L+1) sum_b omega_b r_b H^(L)_b.                    (2)

A strong solution means these integral equations hold in L2 for the fields
and in operator norm for the matrices, continuously in time. The initial first
roots have the law of (W^(1)_0 x_a/sqrt(d))_a for a single row. For Gaussian
weights this is N(0,sigma_1^2 G). The initial operators are constructed from
the joint matrix/transpose limits, not replaced by independent backward maps.

We need only the following fixed-computation result from Tensor Programs III,
Setup 2.2, Theorem 2.10, Box 1 and Remarks 2.11--2.12:

For a fixed finite list of operations on iid jointly Gaussian coordinate
roots and independent iid Gaussian matrices of variance sigma^2/n, using
polynomially bounded measurable coordinate maps, every polynomially bounded
same-population empirical measurement has the deterministic expectation limit
specified by Gaussian innovations and opposite-direction response terms. For
smooth dependence on a matrix's innovation slots, those response coefficients
are sigma^2 times the expectations of the formal partial derivatives. The
coefficients and covariance laws are held fixed in those derivatives. Singular
covariances are permitted. This theorem is only used for a fixed computation.

Source: https://arxiv.org/pdf/2009.10685 .

For C2 activations, all fixed Euler programs here and their innovation
derivatives are polynomially bounded: activations have linear growth, their
first two derivatives are bounded, and the program uses finitely many sums
and products. Scalars in that program are deterministic population residuals
and contractions. General subGaussian scalar roots are also permitted by the
following explicit encoding. If F is their distribution function and Phi is
the standard Gaussian distribution function, set U=F^{-1}(Phi(g)). A
subGaussian tail bound and Gaussian tail estimates give
|F^{-1}(Phi(s))|<=C(1+|s|) for finite s; redefining isolated quantile endpoints
does not affect the law. This is a polynomially bounded measurable coordinate
map. Innovation derivatives hold g fixed and never differentiate this map.
Apply it to each of the d first-weight entries and to the readout. Centered
independent subGaussian first entries have uniformly subGaussian projections:
their moment bounds give E exp(t W_ij)<=exp(C B_in^2 t^2); independence then
gives E exp(t sum_j u_j W_ij)<=exp(C B_in^2 t^2 sum_j u_j^2).
Thus each initial Z^(1)_a has a marginal subGaussian bound depending only on
B_in X. No assumption of iid neuron coordinates after matrix reuse is made.

To obtain common spaces for different meshes, take the countable union of the
programs for rational meshes, their finite unions, rational linear
combinations and the coordinate operations needed here (including clipped
products). Their laws are consistent under deletion of instructions. Realize
these countably many laws jointly on each population and take the L2 closure
of the resulting fields. Operator inequalities pass from finite width to each
finite collection. Indeed a 1/4-net in each unit sphere gives

    P(||W^(ell)_0||_op>M)
       <=2*9^(2n)*exp[-n M^2/(8 sigma_ell^2)] -> 0                       (3)

for a sufficiently large fixed M (zero variance needs no bound). Since
||W^(ell)_0 v||_2/sqrt(n)<=M ||v||_2/sqrt(n), second-moment convergence gives
||W^(ell)_0 V||_L2<=M||V||_L2 on the generated span, hence on its closure.
The same argument gives the transpose map. The exact finite adjunction
identity passes to the limit and identifies it with the adjoint. Coordinate
operations extend wherever needed by clipping and L2 limits. This construction
is also consistent with the existing operator semantics of Tensor Programs
IVb, Definition 2.6.7 and Propositions 2.6.8--2.6.9:
https://arxiv.org/pdf/2308.01814 .

For two states on these same spaces use the distance

    d(theta,theta_tilde)=max_a ||Z^(1)_a-Ztilde^(1)_a||_L2
       +sum_(ell=2)^L ||W^(ell)-Wtilde^(ell)||_op
       +||W^(L+1)-Wtilde^(L+1)||_L2.                                    (4)

At finite width replace every field L2 norm by ||b||_2/sqrt(n). No operator
distance between a finite matrix and a population operator is asserted.

Here is an explicit preliminary interval on which these norms stay bounded.
Let S be the maximum of the individual norms entering the state (not the
distance). Choose S0 so the initial norms are <=S0 with probability tending to
one, uniformly in the bound parameters, and are <=S0 in the population.
First-weight concentration is needed only over fixed m. Set B=2S0+2 and

    h_1=D0+D1 B,       h_ell=D0+D1 B h_(ell-1),
    d_ell=D1^(L-ell+1) B^(L-ell+1),
    R0=B h_L+Y.

On S<=B, all ||H^(ell)_a||_L2<=h_ell, ||delta^(ell)_a||_L2<=d_ell,
and |r_a|<=R0. The same inequalities hold at finite width. The norm of each
state velocity is therefore bounded by the corresponding member of

    2 kappa_1 X^2 R0 d_1,
    2 kappa_ell R0 d_ell h_(ell-1) (2<=ell<=L),
    2 kappa_(L+1) R0 h_L.

Let V0>=1 bound their sum. On

    T_ball=min(1,(B-S0)/(4 V0)),                                       (5)

Euler trajectories with mesh <=T_ball remain in S<=B through time 2 T_ball:
up to the first possible exit the cumulative increment is at most 2T_ball V0,
strictly less than B-S0. The same first-exit argument works for integral
solutions. It also bounds interpolation speeds, with a constant depending on
L. This requires only operator and RMS bounds, including for the readout.

## The additional estimate uniform in the time mesh

The fixed-depth response lemma in GENERAL_DEPTH_RESPONSE_PROOF.md derives,
on a further interval T_response>0, for every population Euler mesh Delta,

    sup_(k Delta<=T_response) max_(a,ell)
          E exp(c |P^(ell)_a,k|^2) <= C.                                (6)

It proves this for unbounded activations as well as nonvanishing subGaussian
readout. Its precise recurrences and noncircular choice of constants are part
of this proof, not an additional hypothesis of the theorem.

The important bounds in that derivation are entrywise response coefficients
|C^(ell)_(ak,bs)|<=c_ell Delta omega_b and bounded row sums of A^(ell).
SubGaussian norms of the forward fields and backward fields are bootstrapped
together. A derivative in a single backward slot starts with a pulse carrying
Delta omega_b. Every later random growth coefficient appears in a weighted
time sum Delta sum_(s,b) omega_b |P^(ell)_b,s|. Jensen's inequality bounds its
exponential using marginal subGaussian estimates; independence over time is
not assumed and no maximum of Gaussian fields over the mesh is taken.

Set T_*<=min(T_ball,T_response), with any additional reductions specified in
the lemma. The constants are functions of the displayed bounds only. In
particular they do not contain Delta or m.

## Localization, existence, and uniqueness

Forward fields and predictions are Lipschitz in (4) on the ball S<=B, with
a constant depending on fixed depth and bound parameters. This follows by
expanding W H-Wtilde Htilde=(W-Wtilde)H+Wtilde(H-Htilde), and using
||phi(Z)-phi(Ztilde)||_L2<=D1||Z-Ztilde||_L2.

Backward fields require a cutoff. For any reference field Ptilde,

    ||[phi'(Z)-phi'(Ztilde)] Ptilde||_L2
       <=D2 R ||Z-Ztilde||_L2
           +2D1 ||Ptilde 1_(|Ptilde|>R)||_L2.                            (7)

Write a delta difference as

    phi'(Z)(P-Ptilde)+[phi'(Z)-phi'(Ztilde)]Ptilde.

For ell<L the difference P^(ell)-Ptilde^(ell) is bounded by
B||delta^(ell+1)-deltatilde^(ell+1)||_L2+C d; at ell=L it is a readout
difference. Downward substitution yields

    max_(a,ell)||delta^(ell)_a-deltatilde^(ell)_a||_L2
       <=C(1+R)d+C sum_(ell=1)^L max_a
                  ||Ptilde^(ell)_a 1_(|Ptilde^(ell)_a|>R)||_L2.

Each backward step multiplies the previous difference only by bounded
activation derivatives and bounded operators. The new cutoff term is added;
there is no power R^L. Outer-product differences satisfy
||u tensor v-utilde tensor vtilde||_op
 <=||u-utilde||_L2 ||v||_L2+||utilde||_L2 ||v-vtilde||_L2.
Together with (6), this proves for the vector field in (2)

    ||F(theta)-F(theta_reference)||
       <=C(1+R)d(theta,theta_reference)+C exp(-c R^2),                    (8)

when the reference is a population Euler grid state. Only the reference needs
the tail estimate.

Compare two piecewise linear population Euler interpolants. At time t their
assigned velocities are F evaluated at their respective preceding grid
states. These states differ by at most their interpolant distance plus
C(Delta+Delta'). Apply (8) directly to these grid states and integrate:

    sup_(t<=T_*) d(theta^Delta(t),theta^Delta'(t))
       <=C exp[C(1+R)T_*]
           ((1+R)(Delta+Delta')+exp(-cR^2)).                             (9)

First fix R and send both meshes to zero; then send R to infinity. Since
exp(CRT_*-cR^2)->0, the paths are Cauchy in the complete field/operator spaces.

All coordinate products occurring in F are continuous on these spaces.
For the only subtle product, if Z_j->Z and P_j->P in L2, split
phi'(Z_j)P_j-phi'(Z)P into the bounded multiplier times P_j-P and
[phi'(Z_j)-phi'(Z)]P. The latter converges in L2 by convergence in probability,
boundedness of phi', and uniform integrability against the single integrable
variable P^2. Thus F is continuous; on the compact range of a convergent
sequence of continuous paths this continuity is uniform. The Euler integral
equations pass to (2), giving a strong solution. All P fields converge at
fixed times; Fatou transfers (6) to the solution uniformly in time.

For any other strong solution with the same initial state, (5) bounds its
norms on this interval. Apply (8) with the constructed solution as reference.
Their distance is <=C exp(CRT_*-cR^2) for every R, hence zero. This proves
uniqueness without assuming tails of the competing solution.

Equations (2) use only the current fields, operators, and adjoints. More
precisely, the closed spaces generated by a current state under these
operations and clipped products contain all its subsequent Euler
approximations and their limits. Equal current joint action laws identify
these spaces by an L2 isometry intertwining the operators and coordinate
operations. Uniqueness identifies their subsequent laws. This is autonomy
and restartability on the constructed interval, not a finite scalar closure.

## From the population flow to every vanishing-step finite GD sequence

Fix a rational coarse mesh Delta, independently of eta_n. Expand

    W^(ell)_k=W^(ell)_0-2 kappa_ell Delta
          sum_(s<k,b) omega_b r_b,s delta^(ell)_b,s tensor H^(ell-1)_b,s.   (10)

Build a finite oracle computation using the same sampled initial arrays as
actual GD. In its expanded matrix actions replace all scalar contractions
and residuals by their deterministic population Euler values. This is a
fixed finite program, so the stated theorem gives joint empirical convergence
of every needed node, contraction, second moment, and continuous quadratic
tail cutoff. Its coefficients are a proof device determined by the population
Euler equations; they are not the coefficients of the final autonomous flow.

Construct proxy parameters from the oracle's first-layer/readout nodes and
the finite rank expansion corresponding to (10), with u v^top/n. Applying a
proxy matrix to an oracle node differs from its prescribed oracle action by
finitely many terms of the form

    -2 kappa_ell Delta omega_b r_b,s delta^(ell)_b,s,oracle
       ((h^(ell-1)_b,s,oracle)^top h^(ell-1)_a,k,oracle/n
                         -E[H^(ell-1)_b,s H^(ell-1)_a,k]),               (11)

and transpose actions have the corresponding delta contractions. At fixed
Delta, their scalar errors vanish and their vector RMS norms are bounded.
Consequently all proxy forward quantities are consistent in RMS. To transfer
backpropagation with an unbounded readout, use (7) against oracle P nodes and
proceed downward through layers. At any fixed cutoff the errors vanish, and
the empirical oracle tails converge to the tails in (6); sending that cutoff
to infinity proves the recomputed proxy delta fields are consistent in RMS.
This also proves consistency of its vector field and residuals.

The proxy grid fields therefore have reference tails with limiting upper
bound C exp(-cR^2), after harmless changes in constants. For example if
||v-u||_2/sqrt(n)=e_n then

    ||v 1_(|v|>2R)||_2/sqrt(n)
       <=2 e_n+2||u 1_(|u|>R)||_2/sqrt(n).

Its grid and interpolated norm/speed bounds have limiting upper bounds
independent of Delta, by (5), (10), and the fixed-mesh consistency. Enlarge
the comparison ball by a fixed amount if necessary.

Compare actual GD and the proxy interpolant using their assigned grid
velocities. The actual preceding fine-grid state and reference preceding
coarse-grid state are at distance at most the interpolant distance plus
C(eta_n+Delta). The actual-to-proxy vector-field difference obeys (8), now
with empirical reference tails and fixed-mesh errors. Thus

    sup_(t<=T_*) d_n(theta_n^GD(t),theta_n^proxy,Delta(t))
       <=C exp[C(1+R)T_*]
          ((1+R)(eta_n+Delta)+exp(-cR^2)+o_P(1)).                         (12)

Here o_P(1) is at fixed R,Delta. Initial distance is zero because the oracle
uses the same roots. A vanishing initialization perturbation contributes its
distance to the right side. The actual GD requires only its RMS/operator
ball, not a maximum coordinate bound or an empirical tail theorem for a
growing number of steps.

The limit order is: n->infinity with R,Delta fixed, then Delta->0, then
R->infinity. Equation (12), (9), and fixed-mesh empirical convergence prove
the joint width/step limit. There is no condition such as eta_n sqrt(n)->0.

Predictions follow by the forward Lipschitz bound. Define the kernel blocks

    K^(1)_ab=G_ab E[delta^(1)_a delta^(1)_b],
    K^(ell)_ab=E[H^(ell-1)_a H^(ell-1)_b]
                      E[delta^(ell)_a delta^(ell)_b], 2<=ell<=L,
    K^(L+1)_ab=E[H^(L)_a H^(L)_b],
    K=sum_(ell=1)^(L+1) kappa_ell K^(ell).

Their finite counterparts use b^top c/n in every contraction. Backward RMS
consistency and Cauchy--Schwarz give uniform convergence of these entries.
For Omega=diag(omega_1,...,omega_m), direct differentiation gives

    dot f=-2 K Omega r,        dot L=-4 (Omega r)^top K (Omega r).         (13)

Each block is positive semidefinite, being a parameter-gradient Gram matrix.

For completeness, the extra observable steps do not demand higher moments
of actual GD. The population parameter velocities converge uniformly in L2
and operator norm by (8). Recursively,

    dot Z^(ell)_a=dot W^(ell) H^(ell-1)_a
                    +W^(ell)[phi^(ell-1)'(Z^(ell-1)_a) dot Z^(ell-1)_a]   (14)

is continuous in the state and parameter velocity in the stated norms.
The bounded-multiplier product is justified by the same fixed-reference
uniform-integrability argument used after (9). On the compact population
time path these velocities form a compact L2 family, hence have uniformly
vanishing L2 tails. For each fixed Delta, oracle evaluations of these
velocities are fixed finite programs and have convergent empirical cutoff
moments. Localizing their bounded-multiplier products, first using (12),
then passing Delta to zero, proves convergence of the integrated squared
hidden speeds. No exponential estimate for these derived velocities is
needed; cutoffs here occur after state stability, outside Gronwall.

At any grid with cell length at most epsilon, each absolutely continuous
coordinate path obeys

    sup_(s,t in one cell)|z(t)-z(s)|^2
         <=epsilon integral_cell |dot z(u)|^2 du.

After averaging over neurons and summing over cells, the error of grid
reconstruction in squared uniform path norm is <=C epsilon, uniformly in n
on the ball. Fixed-time empirical joint laws converge in Wasserstein distance
of order two by fixed-program convergence and their second moments. Combining
this with grid reconstruction proves assertion 3. Activations follow from
their Lipschitz bounds. The same cutoff induction proves assertion 4: an
operator amplifies L2 errors by at most B, Lipschitz functions preserve them,
and bounded-factor products use the compact reference L2 family's uniform
integrability. This explains the stated restriction on products.

## Removing second differentiability; losses and initialization perturbations

First the proof above is for C2 activations with bounded first two
derivatives. For a C1 activation whose derivative is globally Lipschitz,
convolve with a smooth compactly supported probability density of scale
epsilon. Then

    ||phi_epsilon-phi||_infinity<=C D1 epsilon,
    ||phi_epsilon'-phi'||_infinity<=C D2 epsilon,
    ||phi_epsilon'||_infinity<=D1,    ||phi_epsilon''||_infinity<=D2.

The response lemma and T_* depend only on these bounds, uniformly in
epsilon. Include rational smoothing scales in the common program family.
The comparison (8) between different smoothings has an additional
C(1+R)(epsilon+epsilon') term: forward differences gain O(epsilon), and
backward differences use (7) plus the uniform difference of derivatives.
The same ordered limits construct a strong flow for the original activation,
inherit (6), and prove uniqueness. Compare finite GD for the original
activation with the fixed smooth oracle by the identical estimate, adding
C(1+R)epsilon inside (12). Taking n,Delta,epsilon,R in that order proves the
same joint limit for C1,1 activations. ReLU's discontinuous derivative does
not satisfy this argument.

More general separable losses are allowed: use sum_a omega_a ell_a(f_a),
where every ell_a is C1 and its derivative is locally Lipschitz, with common
finite bounds and Lipschitz constants on bounded prediction intervals.
Replace every 2r_b in (1),(2),(10)--(12) by ell_b'(f_b). The preliminary ball
uses sup_(a,|f|<=B h_L)|ell_a'(f)| in place of 2R0; prediction stability uses
the corresponding local Lipschitz constant. In response differentiation these
oracle coefficients are frozen, so every response estimate uses only their
bound and the pulse still carries Delta omega_b. The proof is unchanged
with exactly these replacements. No convexity or global growth assumption
on the loss is required on this short interval. For this loss,
dot f_a=-sum_b K_ab omega_b ell_b'(f_b), and
dot L=-sum_ab omega_a ell_a'(f_a) K_ab omega_b ell_b'(f_b).

Finally (12) also allows perturbing the sampled initial arrays by an amount
tending to zero in probability in (4), and changing the kappa constants by
vanishing amounts. The actual initial arrays need only the resulting RMS
and operator bounds. In particular zero population readout covers finite
Gaussian readout sigma_out n^(-beta) g for EVERY beta>0, and indeed any
readout perturbation with ||W^(L+1)_0||_2/sqrt(n)->0 in probability. This
does not assert universality for different O(1) non-Gaussian middle matrices:
such a replacement need not be small in operator norm.

## Strict feature activity is a separate two-hidden-layer corollary

For L=2, squared loss, Gaussian first weights, zero limiting readout, positive sigma_1,sigma_2 and
kappa_1,kappa_2,kappa_3, assume normalized pairwise nonparallel inputs,
nonzero labels, and both activations nonaffine. Within the theorem's C1,1
class, the strict-activity proof in the companion activity note applies.
It does not require monotonicity, oddness, analyticity, or derivatives
nonzero everywhere. On a possibly smaller fixed positive interval, every
input's hidden preactivation AND activation displacements have strictly
positive order-t^2 RMS coefficients, and speeds have order-t coefficients.
The middle matrix changes on every initial feature, all three kernel blocks
are positive definite and nonconstant, the total kernel is nonconstant,
the loss has strictly negative slope, and every hidden activation has
positive best-affine-fit error. The activity interval can depend on the
fixed geometry and labels. These strict claims have not been proved here
at arbitrary depth or for a nonzero limiting readout.

The weighted activity calculation uses omega_a y_a wherever the unweighted
proof uses a label. It keeps the physical kernel in (13). A detailed
independent audit is recorded in ACTIVITY_SOURCE_AUDIT.md.

This proof establishes neither an all-time theorem nor publication priority.
The stored learning-rate powers, feature-learning regime, fixed-step
population limits, and operator formulation have prior literature. The
specific additional proof obligation addressed here is mesh-uniform control
and the joint eta_n->0, n->infinity passage on a fixed positive interval.
