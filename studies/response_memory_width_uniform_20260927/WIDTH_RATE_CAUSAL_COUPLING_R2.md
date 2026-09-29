# History transport, matrix reuse, and the noncausal coupling gap

28 September 2026. Scoped author proof search in the existing study. This
is not independent review or promotion. Only the four assigned study
sources and the complete assigned Reeves text were read; no experiment,
other study, maintained-source edit, Git mutation, or further agent was
used. The investigate-conjectures and solve-math-rigorously skills were
applied.

**Outcome.** There are two new complete positive results. First, for
source histories independent of a Gaussian matrix, its forward and
transpose actions have a joint, noncausal, root-width Gaussian coupling
under Sobolev bounds, with no query-Gram inverse and no time-node count.
The construction retains one matrix and its actual transpose. Second,
the same rate holds for an exact transpose-then-forward return whose
sources are arbitrary histories of the first query. Its response term
is retained exactly, and only the new history-covariance lemma and a
Hilbert-space sample average are needed.

Neither result proves the all-time trained-network width theorem.
Replacing the chronological step of Reeves by arbitrary history
transport is invalid in general: Section 5 gives a fixed bounded smooth
history law with ordinary squared Gaussian transport error O(1/n) but
order-one error for every common-filtration coupling. This is an
obstruction to that chronological argument, **not** to a noncausal
network coupling or to the intended theorem. Sections 6--7 examine the
noncausal fixed-point alternative. They identify its exact missing
matrix-marginal condition and show by a smooth small-response example
why contraction, small activity, and orthogonality alone do not satisfy
that condition.

**Continuation update.** Sections 10--12 go one query farther. They
prove a complete joint root-width coupling for
`g=W^T1, z=W psi(g), k=W^T chi(z)`, including both response terms;
allow an entire returned history when the forward query is scalar;
and prove inverse-free continuity of the continuum response vector
under Gaussian history transport. The full continuum third-query
joint innovation coupling remains open, for the specific reason in
Section 13. These additions strengthen the scope of the positive
results above without establishing the full trained-network theorem.

## 1. Contract and norms

The target remains the canonical fixed-depth, fixed-data network with
iid Gaussian initialization, zero readout, bounded activation slopes,
globally Lipschitz gates, a positive initial readout Gram margin, and the
proved small-label activity bound. No trained neurons are declared iid,
and no independent forward/backward matrices are substituted for a
reused matrix. The desired source accuracy is n^{-1/2+o(1)} in norms
strong enough for the all-time population prediction comparison and
integrated carrier-tail transfer in ACTIVATION_NEAR_QUADRATIC_ALLTIME.md.

The lemmas below use H=L2([0,1]) and E=H1([0,1]). A fixed finite tuple
of sample/layer indices changes constants only. Rescaling a fixed
activity interval to [0,1] changes constants in the same way. Put

\[
 \|u\|_{n,H}^2=\frac1n\sum_{i=1}^n\|u_i\|_H^2.
 \tag{1}
\]

The conclusions in this norm are complete history-source estimates;
they are not silently upgraded to a supremum norm. For an
activity-integrated forcing, Cauchy--Schwarz controls its L1 norm by
its L2 norm times the square root of the fixed activity length.

Use the cosine-basis operator D from
QUANTITATIVE_HISTORY_COVARIANCE.md, so that

\[
 \|Dx\|_H=\|x\|_E,\qquad
 \operatorname{Tr}(D^{-2})=\tau<\infty.
 \tag{2}
\]

## 2. Joint static coupling of a matrix and its transpose

Let f_1,...,f_n and b_1,...,b_n be deterministic E-valued histories.
Define their uncentered empirical covariance operators and Sobolev
energies by

\[
 Q_f=\frac1n\sum_jf_j\otimes f_j,\quad
 Q_b=\frac1n\sum_ib_i\otimes b_i,\qquad
 R_f^2=\frac1n\sum_j\|f_j\|_E^2,\quad
 R_b^2=\frac1n\sum_i\|b_i\|_E^2.
 \tag{3}
\]

**Lemma 1.** There is a coupling of an iid N(0,1/n) matrix W and two
mutually independent arrays of row histories G_f,G_b such that the rows
of G_f are iid N(0,Q_f), the rows of G_b are iid N(0,Q_b), and

\[
 \mathbb E\left[\|Wf-G_f\|_{n,H}^2
                 +\|W^Tb-G_b\|_{n,H}^2\right]
 \le\frac2n\operatorname{Tr}\sqrt{Q_f}
                \operatorname{Tr}\sqrt{Q_b}
 \le\frac{2\tau R_fR_b}{n}.
 \tag{4}
\]

Here Wf and W^Tb use the very same W. The lemma also holds conditionally
on a sigma-field containing the histories when W is independent of that
sigma-field. Independence of W from the histories is essential.

*Proof.* Let T_f:R^n->H have columns f_j/sqrt(n), so Q_f=T_fT_f^*.
Because T_f=D^{-1}(DT_f), the product inequality for Hilbert--Schmidt
operators gives

\[
 \operatorname{Tr}\sqrt{Q_f}
   =\|T_f\|_{\rm nuclear}
   \le\|D^{-1}\|_{\rm HS}\|DT_f\|_{\rm HS}
   =\sqrt\tau R_f.
 \tag{5}
\]

This product inequality follows, for example, by writing the nuclear
norm as the supremum of |Tr(AT_f)| over finite-rank contractions A and
applying Hilbert--Schmidt Cauchy--Schwarz to AD^{-1} and DT_f.
It does not require regularity of covariance eigenvectors. The same
argument applies to b.

Write the finite-rank singular decompositions as

\[
 f_j=\sqrt n\sum_k U_{jk}\sqrt{\lambda_k}\,e_k,
 \qquad
 b_i=\sqrt n\sum_l V_{il}\sqrt{\mu_l}\,d_l,
 \tag{6}
\]

where the positive eigenvalues are those of Q_f,Q_b, and complete U,V
to orthogonal n by n matrices. In these bases, Z=sqrt(n)V^TWU has
iid standard Gaussian entries. The forward coefficient at (l,k) is
sqrt(lambda_k)Z_lk; the transpose coefficient at (k,l) is
sqrt(mu_l)Z_lk. Only pairs with lambda_k>0 and mu_l>0 occur in both
outputs. This is the full dependence produced by the transpose.

For each such pair take independent standard Gaussians xi,eta and put

\[
 Z=\frac{\lambda\xi+\mu\eta}
          {\sqrt{\lambda^2+\mu^2}}.
 \tag{7}
\]

Then Z is standard Gaussian. Couple the actual coefficient pair
(sqrt(lambda)Z,sqrt(mu)Z) to the independent target pair
(sqrt(lambda)xi,sqrt(mu)eta). Its squared expected cost is exactly

\[
 2(\lambda+\mu)-2\sqrt{\lambda^2+\mu^2}
 =\frac{4\lambda\mu}
        {\lambda+\mu+\sqrt{\lambda^2+\mu^2}}
 \le2\sqrt{\lambda\mu}.
 \tag{8}
\]

Use independent Gaussian pairs for different matrix entries. Entries
appearing in only one output are coupled identically; unused entries
are filled independently. All entries of Z are therefore iid standard
normal, so W=VZU^T/sqrt(n) has exactly its required marginal. Orthogonal
row changes preserve the product Gaussian law of the target histories.
Summing (8) and dividing by n proves the first inequality in (4);
(5) proves the second. No eigenvalue is inverted. Zero eigenvalues
create no shared pair and need no regularization. This proves the lemma.

Consequently, the transpose algebra by itself does **not** obstruct a
root-width history coupling. The obstruction is the dependence of the
sources on the matrix being coupled.

## 3. Combining the static result with empirical covariance transport

Suppose the f_j are iid copies of an E-valued f, and the b_i are iid
copies of an E-valued b, independent of W. No cross-independence between
the two source arrays is needed for the following expectation bound.
Assume their Sobolev norms have the exponential moments required by
QUANTITATIVE_HISTORY_COVARIANCE.md, with exponent alpha_f and alpha_b.
Let Q_f^pop=E[f tensor f], Q_b^pop=E[b tensor b].

Apply Lemma 1 conditionally on both arrays. Conditional on the arrays,
its two Gaussian target arrays are independent product laws. Couple
each row from its empirical covariance law to its population covariance
law, with independent coupling kernels across all rows and both arrays.
The new target arrays have fixed product Gaussian laws even after
conditioning on the sources, hence are independent of those sources.
Conditional kernels can be composed with the coupling in Lemma 1 by
retaining its conditional law given the intermediate Gaussian arrays.
In finite projections this is ordinary disintegration; the same
construction applies to these separable Hilbert-space Gaussian laws.

The squared triangle inequality and the proved covariance lemma give

\[
 \mathbb E\left[\|Wf-G_f^{\rm pop}\|_{n,H}^2
             +\|W^Tb-G_b^{\rm pop}\|_{n,H}^2\right]
 \le\frac Cn\left[1+(\log(en))^{2/\alpha_f}
                       +(\log(en))^{2/\alpha_b}\right].
 \tag{9}
\]

For the static term use
E[R_fR_b]<=sqrt(E R_f^2 E R_b^2). Thus a singular empirical
covariance, an infinite history rank, and simultaneous transpose
observations can all be treated without a finite-query condition
number **when the matrix/source independence is valid**.

## 4. An exact same-matrix return with its response term

There is a nontrivial reused-matrix case in which the independence needed
above can be recovered exactly. Let v=(1,...,1)^T, W_ij iid N(0,1/n),
and

\[
 g=W^Tv,
 \qquad f_j=\psi(\cdot,g_j)\in E,
 \qquad z=Wf.
 \tag{10}
\]

The g_j are iid N(0,1). The map psi may specify a complete nonlinear
history; it need not have a finite time discretization. Assume the
Sobolev exponential moment in the covariance lemma and
E[g^2||psi(.,g)||_H^2]<infinity. The latter follows, for example,
from a fourth Sobolev moment by Cauchy--Schwarz.

Put

\[
 a=\mathbb E[g\psi(\cdot,g)],\quad
 Q=\mathbb E[\psi(\cdot,g)\otimes\psi(\cdot,g)].
 \tag{11}
\]

**Lemma 2.** There is a coupling preserving (10) exactly and an array
G with iid N(0,Q) rows, independent of the whole vector g, such that

\[
 \mathbb E\|z-(va+G)\|_{n,H}^2
 \le C\frac{1+(\log(en))^{2/\alpha}}n.
 \tag{12}
\]

*Proof.* Denote P_v=vv^T/n. Gaussian orthogonal decomposition gives
the exact joint representation

\[
 W=\frac{vg^T}{n}+(I-P_v)\widetilde W,
 \tag{13}
\]

where tilde W is iid N(0,1/n), independent of g. To check this directly,
for each column the two displayed terms are independent centered
Gaussian vectors with covariances P_v/n and (I-P_v)/n. Their sum
has covariance I/n, and columns remain independent. Its transpose
action on v is exactly g.

Writing a_n=n^{-1}sum_j g_j f_j and U=tilde W f gives

\[
 z=va_n+(I-P_v)U.
 \tag{14}
\]

Conditional on g, U has iid Gaussian rows with covariance
Q_n=n^{-1}sum_j f_j tensor f_j. Couple these rows to iid N(0,Q)
histories G with expected normalized cost equal, or arbitrarily close,
to E W2^2(N(0,Q_n),N(0,Q)). Their conditional target law is fixed,
so G is independent of g. This coupling can be lifted to tilde W
by retaining its Gaussian conditional law given U,g; its original
conditional marginal given g is unchanged.

The Hilbert-space iid variance identity gives

\[
 \mathbb E\|a_n-a\|_H^2
 =\frac1n\mathbb E\|g\psi(\cdot,g)-a\|_H^2.
 \tag{15}
\]

Moreover, conditional independence of U's rows yields

\[
 \mathbb E\|P_vU\|_{n,H}^2
 =\frac{\mathbb E\operatorname{Tr}Q_n}{n}
 =\frac{\mathbb E\|\psi(\cdot,g)\|_H^2}{n}.
 \tag{16}
\]

Use (14), z-(va+G)=v(a_n-a)+(U-G)-P_vU, and the squared
three-term triangle bound. Equations (15)--(16) and the covariance
lemma prove (12).

When psi has an integrable weak derivative in g, Gaussian integration
by parts identifies a(t)=E[partial_g psi(t,g)] for almost every t.
Thus the deterministic term va is exactly the familiar Gaussian
response, not an error or an independent-matrix replacement. For
psi(t,g)=g it is v, and discarding it gives order-one normalized bias.
The proof itself needs no derivative representation and no third
activation derivative.

This lemma covers one finite-rank initial query followed by an arbitrary
continuum of sources measurable from it. It does not cover histories
that subsequently inspect the residual matrix (I-P_v)tilde W. In a
trained deep network they do inspect it. That is the precise point at
which repeating this argument would require a further theorem.

## 5. A decisive obstruction to chronological covariance transport

The following result concerns the attempted *black-box* replacement of
Reeves's triangular-factor step. It is deliberately not asserted to be
a realizable network trajectory.

Choose a nonzero smooth compactly supported bump b_0 in (1/2,1), with
||b_0||_H=1. Choose disjoint open intervals I_k inside (0,1/4), ordered
from left to right and accumulating only at 1/4, of lengths comparable
to 2^{-k}. Let b_k be a fixed smooth bump rescaled to I_k and multiplied
by 2^{-k^2}. Write r_0,r_1,... for independent random signs and define

\[
 X(t)=r_0b_0(t)+\sum_{k\ge1}r_kb_k(t).
 \tag{17}
\]

Because the supports are disjoint,

\[
 \|X\|_E^2=\|b_0\|_E^2+\sum_{k\ge1}\|b_k\|_E^2=R^2<\infty.
 \tag{18}
\]

Indeed the summands are O(2^{-2k^2+k}). Every derivative of the early
bumps tends to zero at their accumulation point: the r-th derivative
is bounded by C_r 2^{-k^2+rk}. Hence every history is C-infinity,
with a deterministic uniform bound on every fixed derivative order.
This is much stronger than bounded Sobolev norm.

Take n iid copies X_i and condition on the entire sign array. The
empirical Gaussian history can be represented as

\[
 U_n(t)=\frac1{\sqrt n}\sum_{i=1}^n\gamma_iX_i(t),
 \qquad \gamma_i\stackrel{\rm iid}{\sim}N(0,1).
 \tag{19}
\]

For each k>=1, observing its nonzero bump coefficient before time 1/4
reveals n^{-1/2}sum_i gamma_i r_{i,k}. Almost surely the sequence of
sign columns (r_{1,k},...,r_{n,k}) visits every member of {+1,-1}^n:
each specified pattern has probability 2^{-n} on each independent
trial, so the probability it never occurs is
lim_K(1-2^{-n})^K=0; take a finite union over patterns. These patterns
span R^n. A finite random set of early observations therefore recovers
gamma completely. In particular the later coefficient

\[
 A_n=\frac1{\sqrt n}\sum_i\gamma_ir_{i,0}
 \tag{20}
\]

is measurable from U_n restricted to [0,1/4], given the source array.
It is conditionally centered Gaussian with variance one.

The population covariance is sum_{k>=0} b_k tensor b_k, so its
Gaussian law has the representation

\[
 V(t)=\sum_{k\ge0}Z_kb_k(t),\qquad
 Z_k\stackrel{\rm iid}{\sim}N(0,1).
 \tag{21}
\]

The late coefficient Z_0 is independent of the entire population past.
Require a chronological/common-filtration coupling in the following
explicit sense: conditional on the source array, the law of Z_0 given
the *joint* histories of U_n and V before 1/4 is still N(0,1). This is
the conditional-innovation property needed to reuse the Gaussian
conditioning construction after a coupling step. Then

\[
 \mathbb E[A_nZ_0\mid(X_i)_i]=0,
 \qquad
 \mathbb E[(A_n-Z_0)^2\mid(X_i)_i]=2.
 \tag{22}
\]

Because the late bump has H norm one, every such coupling has

\[
 \mathbb E\|U_n-V\|_H^2\ge2\quad\hbox{for every }n.
 \tag{23}
\]

Yet the newly proved bounded-Sobolev covariance result gives

\[
 \mathbb E\,\mathcal W_2^2
       (N(0,Q_n),N(0,Q))\le\frac{\tau R^2}{n}.
 \tag{24}
\]

Thus small ordinary transport cost does not imply any small transport
cost compatible with exact chronological innovations, even with uniform
smoothness of all orders and a single fixed source law. Small early
amplitudes carry little L2 cost but can carry arbitrarily much exact
information. One can discard them in an approximate construction, or
use a noncausal coupling; those are additional constructions and are
not consequences of (24).

Reeves's Definition 2 builds q_t from the past, then proves its new
Gaussian slot independent of that past. Its Section 4.3 couples
chronological QR/Cholesky factors R and Omega. Formula (24) gives an
ordinary transport between covariance laws; replacing those triangular
factors by a whole-history optimal rotation need not preserve the
conditional innovation property. Equations (17)--(24) show why a
uniform theorem making that replacement from Sobolev bounds alone is
false. They do not constrain unrestricted couplings of final network
observables.

## 6. The noncausal fixed-point proposal and its exact missing condition

The positive construction in Section 2 suggests sampling a full
population candidate, taking its source histories, constructing W from
the Gaussian pairs in (7), and then solving a small-activity fixed point
with the exact population response terms. Noncausality is permitted in
a proof of output accuracy. The difficulty is not that this proposal
uses the future; it is that it has not specified a coupling with the
right matrix marginal.

In Lemma 1 the bases U,V and pair weights lambda,mu are fixed before
sampling their Gaussian coefficients. If they become functions of
those same coefficients, the inference

\[
 W=VZU^T/\sqrt n\quad\Longrightarrow\quad
       (W_{ij})\hbox{ iid }N(0,1/n)
 \tag{25}
\]

is false. Conditioning on the candidate histories does not repair it:
their conditional law already constrains the coefficients from which
W is being reconstructed. Lemma 2 succeeds precisely because exact
Gaussian regression exposes a residual matrix independent of the
entire chosen family of sources.

A contraction proves existence and uniqueness for the equations of the
proposed coupled variables. It does not prove the probability law of
the resulting W. To apply the existing stopped comparison, the source
identity needed is, schematically,

\[
 \begin{split}
 W\,h^{\rm ref}&=\xi+\hbox{exact forward response}+e_f,\\
 W^T\delta^{\rm ref}&=\eta+\hbox{exact transpose response}+e_b,
 \end{split}
 \tag{26}
\]

**on a coupling where W has its canonical iid Gaussian marginal**, and
where the reference program has its specified population marginal.
The exact deterministic response terms are those in Section 3 of
ACTIVATION_GAUSSIAN_ALLTIME.md. Inserting them by definition of a
candidate path does not verify the emphasized marginal condition.

This is a separate source error from covariance fluctuations. A map
that solves (26) with small apparent e_f,e_b but changes the law of W
has approximated a different initialized ensemble. Its error cannot
be propagated by the canonical stability theorem until that ensemble
change has itself been coupled or otherwise controlled.

For a smooth invertible realization T of a transformation of a
standard Gaussian vector G, its exact marginal test is

\[
 \log\frac{d(T_\#\gamma)}{d\gamma}(Tg)
  =\frac{\|Tg\|^2-\|g\|^2}{2}-\log|\det DT(g)|.
 \tag{27}
\]

Thus a random orthogonal transformation preserving norms still needs
its Jacobian determinant to equal one almost everywhere to preserve
Gaussian measure. A bound on DT-I is not this identity. Singular
bases and covariance factors would additionally require a valid
regularization or a nonsmooth measure argument; none is supplied by
the Sobolev covariance estimate.

The exact response terms may well permit such a construction by a
different argument. No impossibility theorem for that network-specific
construction has been obtained here. The next section rules out the
claim that small feedback alone already supplies it.

## 7. Smooth small adaptive rotations need not preserve Gaussian law

Let G=(X,Y) be standard two-dimensional Gaussian, 0<epsilon<1/6,
rho(g)=sqrt(1+||g||^2), and define

\[
 \theta(g)=\epsilon X/\rho(g),\qquad
 T(g)=R_{\theta(g)}g,
 \tag{28}
\]

where R is the ordinary planar rotation. This is smooth and preserves
||g|| exactly. Furthermore

\[
 \|DT(g)-I\|_{\rm op}\le3\epsilon\quad\hbox{for every }g.
 \tag{29}
\]

Indeed ||R_theta-I||<=|theta|<=epsilon and
||grad theta||<=2epsilon/rho, so differentiating R_theta g adds at
most 2epsilon. Therefore T-I is a global contraction, and for each y
the fixed point g=y-(T(g)-g) gives a unique preimage. The derivative is
invertible by (29), so T is a smooth global diffeomorphism.

Nevertheless its second coordinate has a positive mean of order
epsilon. Symmetry in Y cancels E[Y cos(theta)], while
X sin(epsilon X/rho)>=epsilon sin(1) X^2/rho. Hence

\[
 \mathbb E[T(G)_2]\ge c_0\epsilon,\qquad
 c_0=\sin(1)\mathbb E[X^2/\rho(G)]>0.
 \tag{30}
\]

The Gaussian law has zero mean, so every coupling has squared Euclidean
cost at least c_0^2 epsilon^2. Taking n independent copies makes this
a constant lower bound on the averaged squared error, not O(1/n).

The matrix determinant lemma gives an exact version of the marginal
defect. With Jg=(-Y,X),

\[
 \det DT(g)=1+\nabla\theta(g)\cdot Jg
            =1-\epsilon Y/\rho(g).
 \tag{31}
\]

By (27), its relative entropy with respect to a standard Gaussian is

\[
 D(T_\#\gamma\|\gamma)
 =\mathbb E[-\log(1-\epsilon Y/\rho(G))]
 =\sum_{k\ge1}\frac{\epsilon^{2k}}{2k}
         \mathbb E[(Y/\rho(G))^{2k}]
 =\Theta(\epsilon^2).
 \tag{32}
\]

Absolute convergence of the logarithm series is uniform since
|epsilon Y/rho|<1/6; symmetry removes odd terms. In n independent
copies this entropy is Theta(n epsilon^2). Thus even a globally
contractive perturbation of the identity with exactly orthogonal point
values can produce an extensive density change. A fixed small label
does not make such a change a width error.

Subtracting only the mean does not fully repair the law. Since T
preserves the original squared norm,

\[
 \mathbb E\|T(G)-\mathbb ET(G)\|^2
       =2-\|\mathbb ET(G)\|^2<2.
 \tag{33}
\]

The reverse triangle inequality in the L2 norm of any coupling then
gives distance at least
sqrt(2)-sqrt(2-||E T(G)||^2), which is at least c epsilon^2.
This is still a width-independent discrepancy. The example does not
identify the neural Onsager correction with a mere mean subtraction;
it demonstrates why exact marginal control cannot be inferred from
smallness plus a first-order response correction without proving the
remaining identities.

## 8. What the existing stability estimate can and cannot finish

QUANTITATIVE_WIDTH_CAVITY.md proves an activity-based stopped response
factor C(1+M)exp(C(1+M)S), with S=O(Y), and the near-quadratic synthesis
uses the corresponding all-time cutoff comparison. At
M=C sqrt(log n), this factor is n^{o(1)}. Therefore the node-free
root-width source costs in Sections 2--4 have the right size for that
stability mechanism. They do not contain an extra physical-time or
query-count loss.

But those exact source results cover source-independent actions or
the single finite-rank regression return. Actual deep learned
histories require a simultaneous version of (26), together with
its correct Gaussian matrix and population marginals and the necessary
carrier stop/tail control. The static construction does not supply
this version, and a noncausal fixed point justified only by small
activity does not supply its marginal condition. No quantitative
all-time dense/population bias or dense-tail floor is established by
this report.

Accordingly, this report does not upgrade the epsilon^{-5/2+o(1)}
moving-state calculation to a theorem. It isolates the source of the
remaining issue more narrowly than a covariance condition number:
ordinary history covariance transport and transpose compatibility can
be root-width simultaneously; the unproved step is the joint adaptive
response coupling with the exact initialized Gaussian matrix law.

## 9. Input provenance

All four assigned study inputs were read completely:

- ACTIVATION_NEAR_QUADRATIC_ALLTIME.md:
  `0801cb31acd77d8fbd157833090de3f88e5484a23cb471349b6e9c1b7e413bb7`.
- ACTIVATION_GAUSSIAN_ALLTIME.md:
  `6385264a060893eb226e94b4302ff86a095e00bf34e9fa364f4e7759486139d0`.
- QUANTITATIVE_HISTORY_COVARIANCE.md:
  `cda11855e9f55a69d6d1a738faa1a157c792b342819deb1d759497bbbc96451d`.
- QUANTITATIVE_WIDTH_CAVITY.md:
  `716bdfcb75500e220332386e1dea19e7770c91fc40f6603e4879754460b87eff`.

The complete local text of Galen Reeves, *Dimension-Free Bounds for
Generalized First-Order Methods via Gaussian Coupling*, arXiv:2508.10782v1,
was read at
`data/generated/response_memory_width_uniform_20260927/quantitative_width_01/reeves_gaussian_coupling.txt`,
SHA-256
`860ba43a1a53630295a1ff9b1bf61122c98c76ca32600c0f1a10265fde33c4b2`.
Only its explicit coupling construction and error decomposition are
used here; no unverified generalization of its finite-query theorem is
invoked. Sections 2, 4, 5, and 7 above are self-contained derivations.

## 10. Complete joint coupling through the third scalar query

This continuation uses the same Gaussian matrix three times. Put
v=(1,...,1)^T and

\[
 g=W^Tv,\quad f_j=\psi(g_j),\quad z=Wf,\quad
 c_i=\chi(z_i,\zeta_i),\quad k=W^Tc,
 \tag{34}
\]

where the zeta_i are iid auxiliary roots independent of W. Assume
psi is globally Lipschitz, |psi(0)| finite, and chi is bounded by B
and globally L-Lipschitz in its scalar first argument, uniformly in
its root. A classical second derivative of either map is unnecessary.
Define, for independent standard normal G,X and a root zeta,

\[
 a=\mathbb E[G\psi(G)],\quad \sigma^2=\mathbb E\psi(G)^2,
 \quad Z_*=a+\sigma X,
 \tag{35}
\]
\[
 \mu=\mathbb E\chi(Z_*,\zeta),\qquad
 \nu^2=\operatorname{Var}\chi(Z_*,\zeta),\qquad
 \beta=\mathbb E\,\partial_z\chi(Z_*,\zeta).
 \tag{36}
\]

For sigma>0 the derivative in (36) is the almost-everywhere derivative
of a Lipschitz function; Gaussian integration by parts gives
sigma beta=E[X chi(a+sigma X,zeta)]. At sigma=0, continuity and the
full support of the Gaussian law imply psi=0 everywhere; choose beta=0.

**Lemma 3.** There is a coupling preserving (34) exactly with arrays
g,xi,eta of independent standard normal coordinates, mutually
independent and independent of the iid roots, such that, with

\[
 z_i^*=a+\sigma\xi_i,\qquad
 k_j^*=\mu g_j+\beta\psi(g_j)+\nu\eta_j,
 \tag{37}
\]

one has

\[
 \mathbb E\bigl[\|z-z^*\|_2^2/n+\|k-k^*\|_2^2/n\bigr]
 \le C/n.
 \tag{38}
\]

The constant depends on the displayed bounds for psi, chi. There is no
history-Gram inverse and no assumption of positive sigma or nu. In
particular eta is independent of the **whole** reference forward
array xi, not merely of one selected forward coordinate.

*Exact regression.* Let

\[
 a_n=\frac1n\sum_jg_jf_j,\quad \sigma_n^2=\|f\|_2^2/n,
 \quad P_f=ff^T/\|f\|_2^2\quad(f\ne0),
 \tag{39}
\]

and set P_f=0 when f=0. Starting from (13), regress tilde W onto its
action on f. Conditional on g, this gives

\[
 z=a_nv+\sigma_n(\xi-\bar\xi v),\qquad
 \bar\xi=n^{-1}\sum_i\xi_i,
 \tag{40}
\]

with xi independent standard normal and independent of g. The remaining
matrix has the form A(I-P_f), with A iid Gaussian independent of
g,xi. Consequently the third query has the **exact** representation

\[
 k=g\bar c+\frac f{\sigma_n}B_n
       +\nu_n(I-P_f)\eta,
 \tag{41}
\]
\[
 \bar c=\frac1n\sum_i c_i,\quad
 B_n=\frac1n\sum_i(\xi_i-\bar\xi)c_i,\quad
 \nu_n^2=\frac1n\sum_i(c_i-\bar c)^2.
 \tag{42}
\]

The middle term is zero when f=0. To verify it for f!=0, the regression
part is f U^T(I-P_v)c/||f||^2 with U=sigma_n xi; this is
f B_n/sigma_n. Conditional on g,xi,roots, A^T(I-P_v)c has covariance
nu_n^2 I_n, which gives the last term with eta independent of the
whole conditioning field. Completing its unused f-direction with an
independent normal makes eta a full iid normal vector. This is a
Gaussian conditional decomposition of the same W, not a replacement
of one matrix call by a new matrix.

*Width estimates.* For every fixed p>=2,

\[
 \|a_n-a\|_{L^p}\le C_p/\sqrt n,\qquad
 \|\sigma_n-\sigma\|_{L^p}\le C_p/\sqrt n.
 \tag{43}
\]

The first follows from iid moments of G psi(G), which has moments of
all orders by linear growth: expand an even centered moment 2k>=p;
terms with a singleton index vanish, leaving at most k distinct
indices and hence at most C_k n^k terms before division by n^{2k}.
For the second, sigma_n as a function of
the Gaussian vector g is Lip(psi)/sqrt(n)-Lipschitz by the reverse
Euclidean triangle inequality. The Gaussian Lipschitz concentration
inequality stated in QUANTITATIVE_WIDTH_CAVITY.md gives its centered
Lp bound and Var(sigma_n)<=Lip(psi)^2/n. Since E sigma_n^2=sigma^2,
|E sigma_n-sigma|<=sqrt(Var(sigma_n)). This proves (43) without
division by sigma. Equation (40), Gaussian moments of bar xi, and
independence of g,xi now give

\[
 \left\|\|z-z^*\|_2/\sqrt n\right\|_{L^p}
 \le C_p/\sqrt n.
 \tag{44}
\]

Write c_i^*=chi(z_i^*,zeta_i). Lipschitz continuity and (44) control
the RMS difference c-c^* at the same rate. Bounded iid averaging of
c_i^* and xi_i c_i^* gives

\[
 \|\bar c-\mu\|_{L^4}\le C/\sqrt n,\qquad
 \|B_n-\sigma_n\beta\|_{L^2}\le C/\sqrt n.
 \tag{45}
\]

For the second estimate, subtract n^{-1}sum_i xi_i c_i^*: the difference
has absolute value at most

\[
 \frac{\|\xi\|_2}{\sqrt n}
       \frac{\|c-c^*\|_2}{\sqrt n}
       +B|\bar\xi|.
 \tag{46}
\]

Its L2 norm is O(n^{-1/2}) by (44) in L4. The iid average has mean
sigma beta and L2 fluctuation O(n^{-1/2}); finally use (43) and
|beta|<=L. Although (41) contains f/sigma_n, its normalized norm is
exactly one, and therefore

\[
 \left\|\frac f{\sigma_n}B_n-\beta f\right\|_2/\sqrt n
 =|B_n-\sigma_n\beta|\quad(f\ne0).
 \tag{47}
\]

Both vector terms vanish when f=0. This cancellation is the reason no
small-variance inverse occurs in the result.

The empirical standard deviation is 1-Lipschitz in normalized Euclidean
distance. For the iid c_i^*, put D_i=c_i^*-mu. Then |D_i|<=2B and
E D_i^2=nu^2. If nu>0,

\[
 \mathbb E\left(\sqrt{n^{-1}\sum_iD_i^2}-\nu\right)^2
 \le\frac{\operatorname{Var}(D_1^2)}{n\nu^2}
 \le\frac{4B^2}{n}.
 \tag{48}
\]

If nu=0 the left side is zero. Removing the empirical mean changes
this square-root second moment by at most |n^{-1}sum_iD_i|, whose
second moment is nu^2/n. Together with (44) this proves
E(nu_n-nu)^2<=C/n. Since eta is independent of all coefficients,

\[
 \mathbb E\|\nu_n(I-P_f)\eta-\nu\eta\|_2^2/n
 \le2\mathbb E(\nu_n-\nu)^2+2\mathbb E\nu_n^2/n
 \le C/n.
 \tag{49}
\]

Finally, the first term of k-k^* is g(bar c-mu); its normalized
squared expectation is O(1/n) by Cauchy--Schwarz, (45), and the bounded
fourth moment of ||g||/sqrt(n). Combining (44), (47), and (49) proves
(38), including the zero-variance cases. The two response terms in
(37) are essential: mu g is the return through the initial constant
query, while beta psi(g) is the return through the nonlinear forward
query.

## 11. A continuum of returned histories after one scalar forward query

The scalar rank of the *forward source* can be retained while allowing
the returned query to be a whole history. Keep g,f,z as in (34), and
let

\[
 c_i=\mathcal C(z_i,\zeta_i)\in H,\qquad k=W^Tc.
 \tag{50}
\]

Assume C:R x root-space->H is L-Lipschitz in its scalar argument,
uniformly in the root; its H-valued derivative is bounded by L when
used below. Assume the ideal history
C_*=C(a+sigma X,zeta) has the exponential H1 moment in the history
covariance lemma and has the necessary fourth H moment. No H1 bound
for a perturbed history is inferred from its H distance.

Define H-valued mu=E C_*, beta=E partial_z C(a+sigma X,zeta), and

\[
 V=\mathbb E[(C_*-\mu)\otimes(C_*-\mu)].
 \tag{51}
\]

**Lemma 4.** There is a joint coupling with g,xi as above and rows
G_j iid N(0,V), independent of the entire g,xi,root array, such that

\[
 k_j^*=g_j\mu+\psi(g_j)\beta+G_j
 \tag{52}
\]

obeys

\[
 \mathbb E\left[\|z-z^*\|_2^2/n+
                 \|k-k^*\|_{n,H}^2\right]
 \le C\{1+(\log(en))^{2/\alpha}\}/n.
 \tag{53}
\]

Here beta=0 is admissible at sigma=0, as before. If a derivative
representation is unwanted, use sigma beta=E[X C_*] at sigma>0;
the expectation exists in H.

*Proof.* The exact decomposition (41) remains valid with H-valued
bar c,B_n and with its Gaussian last term replaced by
(I-P_f)U, where, conditionally on g,xi,roots, U has iid rows of
covariance

\[
 V_n=\frac1n\sum_i(c_i-\bar c)\otimes(c_i-\bar c).
 \tag{54}
\]

The original residual matrix is independent of the scalar forward
observations, so this Gaussian conditional statement concerns the
complete returned history, not separate incompatible time marginals.
The Hilbert-space versions of (45)--(47) use Lipschitz C, Hilbert
Cauchy--Schwarz, and the iid variance identity. In (46) the last term
becomes |bar xi| ||bar c||_H; its L2 bound uses the bounded fourth
moment of ||bar c||_H, supplied by C_* and the Lipschitz perturbation.
Fourth moment bounds for empirical Hilbert-space means follow by
expanding the square of their squared norm: only paired and repeated indices survive,
giving C n^{-2} E||Y-EY||^4. They provide the stated O(1/n)
squared costs for both response terms.

It remains to couple V_n to V. Let c_i^*=C(z_i^*,zeta_i), with empirical
mean bar c^*. Shared independent scalar Gaussian coefficients show

\[
 \mathcal W_2^2(N(0,V_n),N(0,V_n^*))
 \le\frac1n\sum_i
    \|(c_i-c_i^*)-(\bar c-\bar c^*)\|_H^2
 \le\frac1n\sum_i\|c_i-c_i^*\|_H^2.
 \tag{55}
\]

Here V_n^* is the empirically centered covariance of c_i^*.
For D_i=c_i^*-mu, put Q_n^D=n^{-1}sum_i D_i tensor D_i. Then

\[
 Q_n^D=V_n^*+(\bar c^*-\mu)\otimes(\bar c^*-\mu).
 \tag{56}
\]

Adding an independent Gaussian multiple of bar c^*-mu couples these
last two covariances with squared cost ||bar c^*-mu||_H^2, whose
expectation is O(1/n). The iid centered histories D_i inherit the
required Sobolev exponential moment from C_* (with changed constants),
so the covariance lemma couples Q_n^D to V at squared cost
O(log^{2/alpha}(en)/n). Equations (44)--(56) and the squared triangle
inequality give the same rate for E W2^2(N(0,V_n),N(0,V)).

Apply this coupling independently across the Gaussian rows U, given
the complete g,xi,root array. The target Gaussian array G has a fixed
product conditional law and is therefore independent of that array.
The rank-one projection loss costs

\[
 \mathbb E\|P_fU\|_{n,H}^2
 \le\mathbb E\operatorname{Tr}V_n/n\le C/n.
 \tag{57}
\]

Combining the estimates proves (53). This proves a continuum of
returned histories, but the forward source f remains one scalar query.
It does not replace an arbitrary continuum of forward sources by rank
one.

## 12. Inverse-free continuity of the full continuum response vector

The mean response extends to arbitrary forward histories without a
finite-rank restriction. This statement isolates a complete part of
the next iteration, rather than assuming continuity of gate derivatives.

Let T:R^n->H have columns f_j/sqrt(n), X~N(0,I_n), and U_n=TX.
Let U be a centered H-valued Gaussian and couple U_n,U **jointly
Gaussian**, with

\[
 \delta^2=\mathbb E\|U_n-U\|_H^2.
 \tag{58}
\]

The joint coupling can be extended to X by retaining its Gaussian
conditional law given TX, so its originally specified marginal is
unchanged. Let C:H->R be L-Lipschitz, with a bounded measurable
Fréchet derivative of norm at most L, and let a_n,a be elements of H.
No Lipschitz modulus of this derivative is assumed. Let u_n,u in H
represent the bounded averaged derivative functionals

\[
 \langle u_n,h\rangle=\mathbb E DC(a_n+U_n)[h],\qquad
 \langle u,h\rangle=\mathbb E DC(a+U)[h].
 \tag{59}
\]

Independent auxiliary roots can be included in C and the expectations.

**Lemma 5.** Under these assumptions,

\[
 \|T^*(u_n-u)\|_2
 \le L\|a_n-a\|_H+2L\delta.
 \tag{60}
\]

*Proof.* Gaussian integration by parts gives
T^*u_n=E[X C(a_n+U_n)]. Define the operator A:R^n->H by
A v=E[(U-U_n) <X,v>]. Bessel's inequality for the orthonormal
random variables X_1,...,X_n gives ||A||op<=delta. Another Gaussian
integration by parts gives

\[
 \mathbb E[X C(a+U)]=T^*u+A^*u.
 \tag{61}
\]

For any scalar square-integrable random variable F, the same Bessel
inequality gives ||E[XF]||_2<=||F||_{L2}. Subtracting (61) from
the first identity therefore yields

\[
 \begin{split}
 \|T^*(u_n-u)\|_2
 &\le\|C(a_n+U_n)-C(a+U)\|_{L2}+\|A^*u\|_2\\
 &\le L\|a_n-a\|_H+L\delta+L\delta.
 \end{split}
 \tag{62}
\]

This proves (60). For completeness, the Hilbert-valued joint Gaussian
U can be written Cov(U,X)X+V, where V is independent of X. Condition
on V (and any auxiliary root), and apply ordinary finite-dimensional
Gaussian integration by parts in X. The bounded derivative makes all
the integrals finite. This proves the displayed identities directly,
without passing derivatives through a finite-projection limit or
assuming continuity of DC.

For the empirical-history application, take iid
f_j=psi(.,g_j), a_n=n^{-1}sum_j g_jf_j, and a=E[g psi(.,g)].
The exact averaged response in coordinate j is
R_{n,j}=<f_j,u_n>; its population counterpart on the same initialized
root is R_j^*=<f_j,u>. Thus

\[
 \|R_n-R^*\|_2/\sqrt n=\|T^*(u_n-u)\|_2.
 \tag{63}
\]

Assume the Sobolev exponential moment for psi(.,G), together with
E[G^2||psi(.,G)||_H^2]<infinity. The joint Gaussian coupling underlying
the covariance lemma supplies E delta^2<=C log^{2/alpha}(en)/n.
The iid Hilbert variance identity supplies E||a_n-a||_H^2<=C/n.
Consequently

\[
 \mathbb E\|R_n-R^*\|_2^2/n
 \le C\{1+(\log(en))^{2/\alpha}\}/n.
 \tag{64}
\]

This is a complete quantitative continuum **mean-response** result.
It remains valid for singular covariances. It uses neither their
pseudoinverses nor continuity of DC; only the value difference of C is
estimated. It does not assert a joint innovation law for W^TC(z).

One can also include the rank-one centering in the **actual** third
query mean. For n>=2 put q_n=1-1/n, and define

\[
 \mu_{n,c}=\mathbb E C(a_n+\sqrt{q_n}U_n),\qquad
 u_{n,c}=\mathbb E DC(a_n+\sqrt{q_n}U_n),\qquad
 \mu=\mathbb E C(a+U).
 \tag{64a}
\]

These expectations condition on the initialized vector g. For the
actual continuum network
z_i=a_n+U_i-bar U and k=W^T(C(z_i))_i, Gaussian integration by parts
in the entries of tilde W gives the exact conditional mean

\[
 \mathbb E[k_j\mid g]
 =g_j\mu_{n,c}+q_n\langle f_j,u_{n,c}\rangle.
 \tag{64b}
\]

Indeed Cov(tilde W_ij,z_l)=P_v^perp(li) f_j/n. Summing the diagonal
terms gives q_n<f_j,u_{n,c}>; the mean-subtraction terms vanish
because every column sum of P_v^perp is zero. Each row z_l has law
a_n+sqrt(q_n)U_n, which gives the displayed coefficients. This proof
also works after averaging independent row roots.

Couple sqrt(q_n)U_n to U using (58). Its L2 error is at most
delta+(1-sqrt(q_n))sqrt(Tr Q_n). Apply (60) with sqrt(q_n)T and
divide by sqrt(q_n)>=1/sqrt(2); the extra q_n factor in (64b) costs
at most L sqrt(Tr Q_n)/n in normalized norm. Lipschitz C similarly
bounds |mu_{n,c}-mu| by L times the mean and Gaussian-history
coupling errors. It follows that

\[
 \mathbb E\left[\frac1n\sum_j
  \left|\mathbb E[k_j\mid g]
       -\mu g_j-\langle f_j,u\rangle\right|^2\right]
 \le C\{1+(\log(en))^{2/\alpha}\}/n.
 \tag{64c}
\]

For precision, multiplication of the scalar mean error by ||g||/sqrt(n)
does not require a higher-moment covariance rate. On
{||g||/sqrt(n)<=2} that factor is bounded. The complementary event has
probability exp(-c n), by the Gaussian norm bound. The crude coupling
cost delta^2<=2(Tr Q_n+Tr Q), the Sobolev exponential moment, and
Gaussian moments give bounded higher moments for every remaining
factor, so Hölder bounds this complement exponentially. Thus (64c)
uses only the expectation covariance estimate already proved. The
finitely many cases n<2 are absorbed in its constant whenever needed.

Formula (64c) is a width bound for the complete conditional mean of
the actual third query. It still leaves its centered fluctuation and
joint independence requirement to be proved.

The response comparison also extends to a Hilbert-valued returned
history. Let K be another separable Hilbert space and C:H->K be
L-Lipschitz with a bounded measurable directional derivative that is
a linear operator H->K of norm at most L. A bounded Fréchet derivative
is sufficient; it is enough that the derivative and chain rule hold
along the finite Gaussian directions used in the integration by parts.
Write A_n=E DC(a_n+U_n) and A=E DC(a+U), interpreted weakly as bounded
operators. Then

\[
 \|(A_n-A)T\|_{\rm HS(R^n,K)}
 \le L\|a_n-a\|_H+2L\delta.
 \tag{64d}
\]

To verify this, the K-valued first-chaos projection satisfies
sum_j ||E[X_j F]||_K^2<=E||F||_K^2. Also the cross-covariance
B v=E[(U-U_n)<X,v>] satisfies ||B||HS<=delta by the same
vector-valued Bessel inequality. Gaussian integration by parts gives
(A_n-A)T=E[(C(a_n+U_n)-C(a+U)) tensor X]+AB. The Hilbert--Schmidt
norm of the first term is at most L(||a_n-a||+delta); the second
is at most ||A||op ||B||HS<=L delta. This proves (64d).

Consequently (64b)--(64c) hold in normalized K-valued history norm as
well, with response rows A f_j. This includes a pointwise map with a
bounded, everywhere-defined scalar derivative, acting from one L2
history space to itself: its directional derivative is multiplication
by that derivative, and dominated convergence verifies the directional
chain rule. No claim that point evaluation is Lipschitz on L2 is needed.

## 13. Remaining joint issue for an arbitrary continuum forward query

For general f_j in H, conditional regression of the entire row history
TX reveals every row direction in range(T^*). Even histories with
bounded Sobolev norm can have rank n. Discarding this active subspace
and replacing it by an independent Gaussian costs its rank divided
by n in squared normalized return norm. This is precisely the loss
that Lemma 3 avoids because its active subspace has rank one.

There is a useful distinction between marginal return approximation
and a joint coupling suitable for another matrix call. A row-wise
Gaussian Stein/CLT argument can try to approximate the active-coordinate
sum by a Gaussian. Such a Gaussian is in general coupled to the
forward row histories used in that sum. Its Gaussian marginal alone
does not make it independent of the full reference forward array.
Lemmas 3--4 establish that independence explicitly; Lemma 5 only
addresses the response mean.

A weighted joint transport could potentially overcome this. In white
latent coordinates, write each forward history as T x_i. The
observable joint cost is the squared norm of

\[
 (T x_1/\sqrt n,\ldots,T x_n/\sqrt n,S/\sqrt n),
 \qquad S=n^{-1/2}\sum_i x_i\{C(Tx_i)-\mathbb EC(Tx_i)\}.
 \tag{65}
\]

For a linear sample statistic, removing its dependence on the old
Gaussian sample is a Gaussian bridge operation and the old-history
cost is governed by Tr(TT^*)/n rather than rank(T)/n. The covariance
part of a Gaussian transport likewise uses sums with denominators
lambda_i+lambda_j, as in the proved history-covariance lemma.

For the nonlinear statistic in (65), direct Gaussian differentiation
has the additional term x_i (T^* DC)^T. An unweighted Stein discrepancy
bound applied to that term counts the active rank. I have not proved
an anisotropic joint transport inequality or a Gaussian bridge
construction that retains only the Sobolev trace cost while preserving
both required marginal laws. In particular, no such bound is inserted
into (64) as though it were already a fluctuation estimate.

The complete new results of this continuation are therefore the joint
scalar third-query theorem, its full returned-history extension after
one scalar forward query, and the continuum response-mean comparison.
The arbitrary-forward-history joint innovation coupling, and hence
the full all-time dense width theorem, remain unproved.
