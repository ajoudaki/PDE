# A Gaussian backward-response cone preserved through the next hidden layer

Root candidate, 2026-09-06. This is an INITIALIZATION lemma, not
a trained-path sign invariant or a global stability theorem.
Explicit dependencies:
GAUSSIAN_INITIAL_SIGNED_RESPONSE.md for the elementary integral
lemmas restated below, and the finite initial Gaussian-conditioning
argument proved in Section 3 here. The former has a scoped audit PASS
on SHA256 05708450c2896f62e9ec39beeb67c9b9d1e804ba37a96fa8e342d6cd3692e1f1.
No numerical experiment or external theorem is used.

Use phi=1+epsilon atan, epsilon=1/10, y=(1,sigma), sigma=+1 or -1,
and Y=diag(1,sigma). All derivatives below keep deterministic
coefficients fixed. A Gaussian source independent of the displayed
forward Gaussian pair is held fixed when differentiating that pair.

## 1. The scalar Gaussian identities needed

For a centered Gaussian pair (Z_1,Z_2) with common variance q>0
and covariance c in [-q,q], put f=atan and f'=h=1/(1+z^2).
Define

  B_q(c)=E[h(Z_1)h(Z_2)],
  J_q(c)=-E[f(Z_2)f''(Z_1)],
  D_q=B_q(q)-J_q(q), T_q(c)=B_q(c)-J_q(c).

The explicit sine/cosine Laplace integrals in the dependency prove

  B_q even and strictly positive,
  J_q odd,
  D_q>0,
  T_q(q)=D_q, and T_q(t)>D_q for -q<=t<q.             (1)

For precision the last inequality follows from

  T_q'(t)=-(1/4) integral_(0,infinity)^2
       exp[-u-v-q(u^2+v^2)/2]
       [(u-v)^2 exp(tuv)+(u+v)^2 exp(-tuv)] du dv<0.

The bounds e^{-u-v} times polynomials justify the derivative
including one-sided limits at the endpoints. Also
D_q=q^-1 E[Z_1 atan(Z_1)/(1+Z_1^2)]>0 by one-dimensional Gaussian
integration by parts. These statements do not assume c positive.

## 2. Exact transfer and its invariant sign cone

Let M=[[m,b],[b,m]] be a deterministic symmetric matrix, and put
C=Y M. Let zeta be any centered Gaussian pair independent of
(Z_1,Z_2); its covariance need not be invertible. Set

  Q_a=zeta_a+sum_j C_aj phi(Z_j),
  D_a=phi'(Z_a) Q_a.

These have all finite moments, since phi and its derivatives are
bounded and zeta is Gaussian. Define the new label-left-weighted
expected derivative matrix

  N_ab=y_a E[partial D_a / partial Z_b].              (2)

Differentiating the displayed complete expression, before any
possible Gaussian-support identities, gives

  partial D_a / partial Z_b
       =1_{a=b}phi''(Z_a) Q_a
              +phi'(Z_a) C_ab phi'(Z_b).

The independent centered source contributes zero to the expectation
of the first term. For j=a and j not equal to a respectively,

  E[phi''(Z_a)phi(Z_j)]
       =-epsilon^2 J_q(q), -epsilon^2 J_q(c).

The constant part of phi vanishes against the odd phi'' under a
centered Gaussian marginal. Since y_a C_aj=M_aj, (2) is exactly

  N=epsilon^2 [
       [D_q m-J_q(c)b, B_q(c)b],
       [B_q(c)b, D_q m-J_q(c)b] ].                    (3)

Let lambda_y=m+sigma b and lambda_perp=m-sigma b be the eigenvalues
of M in directions (1,sigma) and (1,-sigma). The new eigenvalues are

  nu_y=(epsilon^2/2)[
      (D_q+T_q(sigma c)) lambda_y
           +(D_q-T_q(sigma c)) lambda_perp ],

  nu_perp=(epsilon^2/2)[
      (D_q-T_q(-sigma c)) lambda_y
           +(D_q+T_q(-sigma c)) lambda_perp ].        (4)

To check (4), substitute m=(lambda_y+lambda_perp)/2 and
b=sigma(lambda_y-lambda_perp)/2 into the two eigenvalues of (3);
evenness of B and oddness of J give the two stated T arguments.

Consequently

  lambda_y>0 and lambda_perp<0
       imply nu_y>0 and nu_perp<0                    (5)

for every -q<=c<=q. The coefficient D+T in either expression
is strictly positive. Every coefficient D-T is nonpositive by
(1). Thus in the first line its second term is nonnegative and
its first strictly positive; in the second line its first term is
nonpositive and its second strictly negative. This proof includes
both singular endpoints and uses no division by q-c or q+c.

This is not positive-semidefinite preservation. It preserves an
INDEFINITE two-mode cone, with the positive direction selected by
the labels. The covariance of zeta drops out of (3) only because
the calculation is an expected first derivative with independent,
centered zeta. It does not drop out of E[D_a D_b] or of the actual
backward query law.

## 3. Its actual meaning at the two transposes at initialization

At zero population readout let

  V_0=(H^(3)_{0,1}+sigma H^(3)_{0,2})/2,
  U^(3)_a=V_0 phi'(Z^(3)_{0,a}).

Here U^(3) is the INITIAL READOUT-VELOCITY backpropagated at fixed
hidden initialization. It is not the ordinary initial delta, which
vanishes at zero readout. All three hidden initial forward layers
have their usual Gaussian laws and the separate neuron populations
are retained.

Write Q^(2)_a for the joint initial-law limit of
(W^(3)_0)^T U^(3)_a. The initial Gaussian matrix conditioning gives

  Q^(2)_a=zeta^(2)_a+sum_b C^(3)_ab H^(2)_{0,b},
  C^(3)_ab=E_3[partial U^(3)_a/partial Z^(3)_{0,b}],
  Cov(zeta^(2))_ab=E_3[U^(3)_a U^(3)_b],              (6)

with the Gaussian source independent of the layer-two forward pair.
For clarity, this independence is a property of the limiting source
representation, not an iid assertion about finite reused-matrix
coordinates.

Here and below a law assertion means joint empirical convergence in
probability within each neuron population, together with the second
and mixed moments explicitly proved below. The finite model and all
normalizations are specified in the following proof. The two samples
stay in one same-neuron tuple. Different populations are not identified
by their neuron indices, and no finite-coordinate iid conclusion
after matrix reuse is asserted.

The preceding signed-initial note proves that M^(3)=Y C^(3) has
strictly positive label eigenvalue and strictly negative orthogonal
eigenvalue at every admissible actual input configuration. Its
current and historical source slots are distinct in a time-mesh
program; (6) is the direct static initial query and contracts only
their attained initial values, not their formal future dependence.

Set U^(2)_a=phi'(Z^(2)_{0,a}) Q^(2)_a. Apply Section 2 with
(Z_1,Z_2)=(Z^(2)_{0,1},Z^(2)_{0,2}) and M=M^(3). Then

  C^(2)_ab=E_2[partial U^(2)_a/partial Z^(2)_{0,b}],
  M^(2)=Y C^(2)

is exactly (3), and (5) proves that it too has positive label-mode
and negative orthogonal-mode eigenvalues.

Conditioning the initial second matrix on its two initial forward
queries gives the next actual transpose law

  Q^(1)_a=zeta^(1)_a+sum_b C^(2)_ab H^(1)_{0,b},
  Cov(zeta^(1))_ab=E_2[U^(2)_a U^(2)_b].              (7)

The new Gaussian source is independent of the first-layer root.
We now prove (6) and (7), including the unbounded-input moments
needed for the second transpose. No convergence of finite-network
derivatives is claimed or used.

Equation (7) therefore concerns the second reused transpose, not
an independently resampled matrix. The sign statement applies
to its deterministic expected-derivative coefficient, not to its
Gaussian source or to each finite coordinate.

### 3.1 Finite arrays and forward averages

All three widths equal n. Let the rows of the n-by-2 matrix z^(1)_0
be independent centered Gaussian pairs of variance one and fixed
correlation rho in [-1,1). Independently, W^(2)_0 and W^(3)_0 have
independent N(0,1/n) entries and are independent of one another.
Set, entrywise and by ordinary matrix multiplication,

  h^(1)_0=phi(z^(1)_0), z^(2)_0=W^(2)_0 h^(1)_0,
  h^(2)_0=phi(z^(2)_0), z^(3)_0=W^(3)_0 h^(2)_0,
  h^(3)_0=phi(z^(3)_0),
  u^(3)_(i,a)=[h^(3)_(0,i,1)+sigma h^(3)_(0,i,2)]
                            phi'(z^(3)_(0,i,a))/2,
  q^(2)=(W^(3)_0)^T u^(3),
  u^(2)_(i,a)=phi'(z^(2)_(0,i,a))q^(2)_(i,a),
  q^(1)=(W^(2)_0)^T u^(2).

These are static queries; u^(ell) denotes the initial hidden
backward VELOCITY defined above, not the zero initial delta.
The vanishing population readout suffices to interpret them as
initial feature-ascent velocities; no finite physical-clock
identification is required for this static assertion.

For ell=1,2, let K_(ell,n)=(h^(ell)_0)^T h^(ell)_0/n.
Let K_ell=E[H^(ell)_0(H^(ell)_0)^T], using column two-vectors
in population expectations. The root law and conditional Gaussian
row laws give K_(ell,n)->K_ell in probability. More generally, at
each initial forward layer every continuous test of at most fixed
polynomial growth has its empirical average converge in probability
to its stated Gaussian expectation. To see this directly, conditional
on the preceding features, the new rows are independent Gaussians
with covariance K_(ell-1,n). Since |phi|<7/6, their covariance entries
are uniformly bounded. A polynomial-growth test has uniformly
bounded conditional second moment by the elementary Gaussian moment
integrals, so its empirical conditional variance is O(1/n).
Its conditional expectation is continuous in the covariance: couple
as K^(1/2)N for a fixed standard Gaussian two-vector N, use continuity
of the positive semidefinite square root and dominated convergence.
The root stage is the same independent-row argument. Inducting
proves the assertion, including ||z^(2)_0||_F/sqrt(n)=O_p(1).
Here O_p(1) means bounded in probability, and o_p(1) means tending
to zero in probability.

For completeness, square-root continuity for positive semidefinite
two-by-two matrices follows without a choice of eigenvectors: every
bounded sequence of their positive square roots has a convergent
subsequence, whose limit is positive semidefinite and squares to
the limiting matrix; the positive square root is unique by diagonalizing
that matrix and commuting a root with its square. This also handles
singular reverse-source covariance matrices below.

K_1 and K_2 are positive definite for every allowed rho. At rho=-1,
the first features are 1+epsilon atan(G),1-epsilon atan(G), whose
constant and nonconstant odd parts are linearly independent. At
-1<rho<1, the root has a strictly positive two-dimensional Gaussian
density; a linear relation between its two strictly monotone
feature coordinates would force both coefficients to vanish. A
positive definite feature second moment makes the next forward
Gaussian pair nondegenerate, so the same reasoning applies to K_2.
Therefore inverses of K_(1,n),K_(2,n) exist and are bounded on events
whose probabilities tend to one. All subsequent arguments are on
these events; their complements have vanishing probability. No bound
uniform in rho is needed.

### 3.2 Exact finite transpose exposure

In this paragraph h,z,u are n-by-2 finite arrays and W has independent
N(0,1/n) entries. Expose h, z=Wh, and a reverse input u determined by
this exposure and other variables independent of the unexplored
part of W. Suppose h^T h is invertible. Orthogonal projection of
each Gaussian row onto span(h) and its perpendicular space gives

  W=z(h^T h)^-1 h^T + W_tilde(I-Pi_h),
  Pi_h=h(h^T h)^-1 h^T,

where W_tilde can be chosen independent of the exposure with the
original Gaussian entry variance. The two row projections have
zero cross covariance and are jointly Gaussian, hence independent
(their joint Gaussian characteristic function factors).
Writing K_n=h^T h/n, T_n=z^T u/n, S_n=u^T u/n, it follows exactly
in this conditional representation that

  W^T u=h K_n^-1 T_n+(I-Pi_h)b,                       (8)

where the rows of b=W_tilde^T u are conditionally independent
centered Gaussian pairs with covariance S_n. This is an uncentered
second moment of u; no regression covariance is subtracted. In
particular,

  E[||Pi_h b||_F^2/n | exposure]
                       =rank(Pi_h) tr(S_n)/n.         (9)

Thus bounded rank is useful only together with tightness of S_n.
If tr(S_n)=O_p(1), (9) and conditional Markov first on tr(S_n)<=L,
then L->infinity, show ||Pi_h b||_F/sqrt(n)=o_p(1).

### 3.3 First transpose and joint layer-two averaging

Expose the complete lower data and z^(3)_0=W^(3)_0 h^(2)_0.
The reverse input u^(3) is now known and uniformly bounded.
The forward conditional averaging from 3.1 gives

  T_(3,n)=(z^(3)_0)^T u^(3)/n -> T_3=E[Z^(3)_0(U^(3))^T],
  S_(3,n)=(u^(3))^T u^(3)/n -> S_3=E[U^(3)(U^(3))^T].

For the first limit, its summands are continuous with linear
Gaussian growth; for the second they are bounded. Gaussian
integration by parts in the nondegenerate top pair gives

  (T_3)_(b,a)=sum_j (K_2)_(b,j) E[partial_j U^(3)_a],
  T_3=K_2 (C^(3))^T.

This identity follows by differentiating its Gaussian density;
boundedness of U^(3) and its derivatives makes the boundary term
zero. Hence K_(2,n)^-1 T_(3,n)->(C^(3))^T. Applying (8)-(9),

  ||q^(2)-[h^(2)_0(C^(3))^T+b_3]||_F/sqrt(n)=o_p(1), (10)

where, conditionally on this exposure, b_3 has independent Gaussian
rows of covariance S_(3,n). The matrix S_(3,n) is uniformly bounded
because u^(3) is bounded. The coefficient error in (10) vanishes
by boundedness of h^(2)_0; the projection error follows from (9).

For a bounded Lipschitz test of the layer-two tuple
(z^(2)_(0,i,:),h^(2)_(0,i,:),q^(2)_(i,:),u^(2)_(i,:)),
replace q^(2) by the approximation in (10) and u^(2) by its product
with the bounded gate. The average test error tends to zero by
Cauchy--Schwarz. Conditional on the exposure the resulting test
values have independent Gaussian randomness across rows, so their
conditional-average variance is O(1/n). Its mean is an average of
a continuous bounded function of z^(2)_0. Dependence on S_(3,n)
can be replaced uniformly by S_3, by the common Gaussian coupling
and the Lipschitz test bound; the gates are bounded. The forward
empirical law then identifies its limit. This proves the joint law
(6), including independence of its limiting Gaussian source from
the layer-two forward pair, not independence of finite reused
coordinates. All finite collections of such tests converge jointly
by a union bound.

### 3.4 The finite unbounded-input moments, before the next exposure

Set mu_(i,a)=sum_b C^(3)_(a,b)h^(2)_(0,i,b),
d_(i,a)=phi'(z^(2)_(0,i,a)), and
u_hat^(2)_(i,a)=d_(i,a)[mu_(i,a)+(b_3)_(i,a)].
Both mu and d are uniformly bounded. By (10),
||u^(2)-u_hat^(2)||_F/sqrt(n)=o_p(1).
Conditionally on the first exposure, exactly

  E[u_hat^(2)_(i,a)u_hat^(2)_(i,b) | exposure]
    =d_(i,a)d_(i,b)[mu_(i,a)mu_(i,b)+(S_(3,n))_(a,b)]. (11)

The conditional fourth Gaussian moments are bounded uniformly, so
the empirical average on the left differs from the empirical
average on the right by o_p(1). The right average converges by the
forward law and S_(3,n)->S_3. Its limit is
S_2=E[U^(2)(U^(2))^T] for the scalar law already identified.
In particular ||u_hat^(2)||_F/sqrt(n)=O_p(1).

For the mixed moment (z^(2)_0)^T u_hat^(2)/n, its conditional mean
has entries n^-1 sum_i z^(2)_(0,i,b)d_(i,a)mu_(i,a), converging by
the polynomial-growth forward law to E[Z^(2)_(0,b)U^(2)_a]. The
conditional variance of its centered Gaussian part is

  (S_(3,n))_(a,a) n^-2 sum_i[z^(2)_(0,i,b)d_(i,a)]^2
             <=(C/n)[n^-1 sum_i(z^(2)_(0,i,b))^2]
             =O_p(1/n).

Conditional Chebyshev and a tightness restriction make this o_p(1).
Both moments transfer to the actual u^(2), since

  ||[(u^(2))^T u^(2)-(u_hat^(2))^T u_hat^(2)]/n||_F
    <=[||u^(2)-u_hat^(2)||_F/sqrt(n)]
      [ (||u^(2)||_F+||u_hat^(2)||_F)/sqrt(n) ]=o_p(1),

  ||(z^(2)_0)^T[u^(2)-u_hat^(2)]/n||_F
    <=[||z^(2)_0||_F/sqrt(n)]
       [||u^(2)-u_hat^(2)||_F/sqrt(n)]=o_p(1).

Consequently the REQUIRED empirical limits, not just weak-law
assertions, have been proved:

  S_(2,n)=(u^(2))^T u^(2)/n -> S_2,
  T_(2,n)=(z^(2)_0)^T u^(2)/n
                     -> T_2=E[Z^(2)_0(U^(2))^T].      (12)

### 3.5 Second transpose with the same initial second matrix

Now expose (z^(1)_0,h^(1)_0,z^(2)_0,W^(3)_0). The entire finite
u^(2) is measurable in this exposure: it is obtained from z^(2)_0
and W^(3)_0 by the displayed forward/top/reverse operations. Its
dependence on W^(2)_0 is ONLY through z^(2)_0=W^(2)_0 h^(1)_0.
Since W^(3)_0 was initially independent of the first two layers,
including it in the exposure reveals no perpendicular residual of
W^(2)_0. Thus (8) legitimately gives

  q^(1)=h^(1)_0 K_(1,n)^-1 T_(2,n)+(I-Pi_h1)b_2,

with conditionally independent Gaussian rows b_2 of covariance
S_(2,n). Its tightness is now proved by (12), so (9) removes the
projection in RMS in probability. Gaussian integration by parts
in the limiting layer-two pair, conditional on its independent
zeta^(2), gives T_2=K_1(C^(2))^T. Its integrand derivative is
bounded by C(1+|zeta^(2)|), which is integrable; the Gaussian
boundary term vanishes, and deterministic response coefficients
and covariance parameters are held fixed. This uses no convergence
of finite-array derivatives.

Therefore K_(1,n)^-1 T_(2,n)->(C^(2))^T. The same conditional
bounded-Lipschitz averaging as in 3.3, now including z^(1)_0 and
h^(1)_0, proves (7). The conditional Gaussian covariance converges
to S_2, even if S_2 is singular. Quadratic moments of q^(1) and
mixed moments with the first root also converge: after discarding
the RMS error, expand the square of its bounded mean plus b_2;
conditional second/fourth Gaussian moments are bounded on
tr(S_(2,n))<=L, the empirical root second moment is tight, and
then let L increase. This is precisely the calculation (11)-(12)
with no middle gate. The analogous moments of q^(2) follow from
3.4 with d=1. These arguments establish second-moment control of
the complete local tuples as well as their bounded-Lipschitz laws.
All these assertions for the separate populations hold jointly in
probability, by taking a union bound over finitely many tests and
moments. They do not identify unrelated layer indices or assert
almost-sure convergence.

## 4. Scope and next use

The calculation establishes a concrete initial response property
at BOTH trained hidden matrices: the two-mode indefinite sign
pattern propagates through the next Gaussian hidden gate.
It does not imply that the full causal time-indexed response
operator has this cone property. At positive time the forward
fields are not centered Gaussian pairs, the reverse source need
not be independent of the current forward field as used here,
and response terms carry full time histories. The scalar
identities (1) and transfer (3) cannot be substituted for those
missing hypotheses.

In particular, (5) proves neither operator contraction nor
monotonicity of a kernel along training, and it does not settle
global continuation. It is a sharper initial-state discriminator
than the sign of diagonal curvature alone.
