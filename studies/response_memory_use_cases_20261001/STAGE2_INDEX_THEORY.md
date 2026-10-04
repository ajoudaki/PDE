# Shared indices are a choice of spacetime projection

Authored by the indexing route; frozen before experimental outcomes. Claims
below are finite-width algebra or stated Hilbert-space facts with proofs,
not consequences of the manuscript's all-time theorem. Scope: square-integrable
histories on a fixed input probability space, finite-dimensional orthonormal
input dictionaries, and the manuscript's residual clock. The proof needs no
external approximation theorem.

## Setup and the instantaneous identity

Use two tanh hidden layers,

\[
h^{(1)}(x)=\tanh(W^{(1)}x/\sqrt d),\quad
h^{(2)}(x)=\tanh(W^{(2)}h^{(1)}(x)),\quad
f(x)=w^Th^{(2)}(x)/n,
\]

with residual r=f-y, loss E[r²], rho=sqrt(E[r²]), and backward response
delta=w elementwise-times(1-h^(2)²). The input law mu is fixed. The canonical
hidden velocity is G=-2E[r delta h^(1)T]/n. First weights and readout have
mobilities n; the hidden matrix has mobility one. The base initialization is
retained; changing its representation does not remove its n² storage.

Write h=h^(1), let C_h=E[h h^T], and let V be an n by C matrix of orthonormal
eigenvectors of C_h with positive eigenvalues collected in diagonal Lambda.
Define psi(x)=Lambda^(-1/2)V^T h(x), a C-vector of input functions. Then

\[
E[\psi\psi^T]=I_C,\qquad
E[r\delta\psi^T]E[h\psi^T]^T
=E[r\delta h^T]V\Lambda^{-1}V^TC_h
=E[r\delta h^T]VV^T.
\]

The last equality uses C_h V=V Lambda and symmetry of C_h. Consequently the
instantaneously indexed velocity is GVV^T. If only this hidden block evolves,
its exact loss derivative is -||GV||_F², since G is minus that block's
Euclidean gradient. Canonical evolving outer blocks add nonpositive terms.
This construction is right-projected gradient descent, not a distinct
optimization mechanism merely because the index is a function of inputs.
The conclusion requires positive selected eigenvalues; pseudoinverse with a
zero mode deletes that mode rather than normalizing it.

For fixed V, implementing W^(2)=W0+A V^T and dot A=GV preserves this geometry
with nC moving coordinates. Recomputing V as h evolves still gives the
instantaneous identity, but integrating these velocities can accumulate a
full-rank matrix. Maintaining a fixed-rank correction is a separate change.

## Retrospective adaptive indices need discarded history

Let the clock tau(t) satisfy dot tau=rho and tau(0)=1. On the unit prefix set
h(x,xi)=h(x,0) and b(x,xi)=0; afterward b=r delta/rho where rho>0. No algorithm
below divides by rho. For a differentiable orthonormal dictionary
psi_c(x,t), consider *retrospectively reindexed* moments

\[
\bar h_{c,j}(t)=\int_0^{\tau(t)} E[h(x,\xi)\psi_c(x,t)]
p_j(\xi/\tau(t))\,d\xi.
\]

The same definition with b gives bar delta. Assume differentiability under
the integral is justified by integrable dominating functions; on a finite
empirical input law, continuously differentiable bounded histories suffice.
Leibniz' rule and xi p_j'(xi)=j p_j+sum_(k<j)(2k+1)p_k give

\[
\dot{\bar h}_{c,j}=\rho E[h(t)\psi_c(t)]
-\frac\rho\tau\left(j\bar h_{c,j}+\sum_{k<j}(2k+1)\bar h_{c,k}\right)
+\int_0^\tau E[h(x,\xi)\partial_t\psi_c(x,t)]p_j(\xi/\tau)d\xi.
\]

The backward source is E[r delta psi_c]; its connection term is the same
integral with b. Decompose
partial_t psi_c=sum_d Omega_dc psi_d+chi_c, where
Omega_dc=E[psi_d partial_t psi_c] and chi_c is perpendicular to the current
dictionary span. Differentiated orthonormality makes Omega skew-symmetric.
The represented part of the connection is sum_d Omega_dc bar h_dj; the chi
part requires unretained history. Thus rotations within the span can be
transported exactly, while motion of the span generally cannot.

More precisely, fix old and new C-dimensional spans S and T in L²(mu).
Old coefficients E[g psi_c] determine new coefficients E[g eta_d] for every
g in L²(mu) **if and only if T is contained in S** (hence equal when dimensions
match). Sufficiency follows by expanding eta_d in the old basis. For
necessity choose eta_d with v=(I-P_S)eta_d nonzero. Histories g=0 and g=v
have identical old coefficients, whereas E[v eta_d]=||v||²>0. Multiplying
these spatial fields by any retained Legendre polynomial gives the same
counterexample for finite temporal moments. No nonlinear decoder of the old
coefficients can distinguish the two inputs. This is an information
obstruction for arbitrary histories, not a theorem ruling out all adaptive
architectures or special reachable neural histories.

For a discrete refresh let R_cd=E[psi_c eta_d]. The natural transported
coefficients bar h R are exact for P_S h, with error

\[
\int_0^\tau E[((I-P_S)h)(x,\xi)\eta_d(x)]p_j(\xi/\tau)d\xi.
\]

This explicitly identifies the discarded information. Orthogonal Procrustes
alignment can choose coordinates for T; it cannot eliminate its component
outside S.

## Write-time adaptive indices preserve a different exact projection

There is another viable construction. Choose measurable functions
psi_c(x,xi), orthonormal in L²(mu) for almost every historical clock xi.
Define memories with the dictionary present *when the observation is written*:

\[
\bar h_{c,j}(t)=\int_0^{\tau(t)}E[h(x,\xi)\psi_c(x,\xi)]
p_j(\xi/\tau(t))d\xi,
\quad
\bar\delta_{c,j}(t)=\int_0^{\tau(t)}E[b(x,\xi)\psi_c(x,\xi)]
p_j(\xi/\tau(t))d\xi.
\]

There is no partial_t psi term: xi is the fixed integration coordinate.
The standard source-plus-Legendre-dilation ODE is exact even when the
dictionary changes at finitely many clock points (interpret the ODE almost
everywhere). Initialize zeroth forward moments with the prefix dictionary,
all other modes zero. Reconstruct

\[
\widehat W^{(2)}=W_0^{(2)}-
\frac2{n\tau}\sum_{c,j}(2j+1)\bar\delta_{c,j}\bar h_{c,j}^T.
\]

To identify the projection, define u_cj(x,xi)=psi_c(x,xi)p_j(xi/tau) on the
joint space L²(mu(dx)dxi), xi in[0,tau]. Pointwise input orthonormality gives

\[
\langle u_{c,j},u_{d,k}\rangle
=\int_0^\tau\delta_{cd}p_j(\xi/\tau)p_k(\xi/\tau)d\xi
=\frac\tau{2j+1}\delta_{cd}\delta_{jk}.
\]

Let Q project onto these Cq orthogonal functions, coordinatewise for vector
fields. Expanding b=Qb+(I-Q)b and h=Qh+(I-Q)h, both cross terms vanish.
Therefore the exact same-history identity is

\[
\int_0^\tau E[bh^T]d\xi
=\frac1\tau\sum_{c,j}(2j+1)\bar\delta_{c,j}\bar h_{c,j}^T
+\int_0^\tau E[((I-Q)b)((I-Q)h)^T]d\xi.
\]

The omitted interaction's Frobenius norm is at most
|| (I-Q)b ||_(L²) || (I-Q)h ||_(L²): apply the triangle inequality to rank-one
matrices, then Cauchy-Schwarz. This proves orthogonality and the product-tail
identity for a learned write-time dictionary, even though its modes no longer
factor into a fixed input function times a time polynomial. It does not prove
small tails, a closed-loop tracking estimate, or loss monotonicity.

Orientation now matters. Take a constant 2D input span with orthonormal basis
e1,e2 and rotate its coordinates by angle2pi xi/tau. For constant histories
h=b=e1 and q=1, both vector coefficient integrals vanish although the exact
interaction integral is tau. The input span never changed. An aligned constant
basis gives the exact integral with q=1. Thus adapting coordinates can make
perfect spatial information temporally incompressible at fixed order.
Procrustes alignment limits a discrete coordinate jump but does not guarantee
smooth coefficients or small projection tails. This gauge sensitivity is a
specific cost of write-time indexing, distinct from missing-history transport.

## Numerical algorithm and limits

The frozen experiment starts from PCA of initialized features under the
empirical training law. Fixed fields retain that dictionary. If the predefined
drift trigger fires, two variants refresh at physical time64: Procrustes align
the current-feature PCA functions to the old functions, then either (a)
multiply old memories by overlap R, or (b) leave all moments unchanged and
write subsequent sources in the new functions. Variant(a) approximates
retrospective moments; variant(b) computes exact write-time moment equations.
The clock and outer parameters are unchanged. Neither is canonical dense GD,
and neither inherits the manuscript theorem. Both are implementable without
growing per-observation memory, although the empirical PCA setup uses the
training set and costs additional fixed dictionary storage and computations.

Root separately supplied a general descent criterion for fixed sample
projectors after this route's initial proposal. That criterion is not claimed
as an independent finding here; no other route's experimental results were
read. All arguments above were completed without reading its proof.

## Primary-literature boundary

Low-rank correction factors are established by
[LoRA](https://arxiv.org/abs/2106.09685); projected-gradient optimizer storage
is studied by [GaLore](https://arxiv.org/abs/2403.03507). Dynamically evolving
low-rank subspaces and tangent-space integration predate this construction,
including [Koch and Lubich](https://doi.org/10.1137/050639703) and
[Lubich and Oseledets](https://arxiv.org/abs/1301.1058). No priority is claimed
for PCA, learned subspaces, projection, low rank, or changing bases. The
specific result is the distinction between retrospective and write-time
indexing of paired response histories, with their respective discarded-history
and temporal-coordinate costs. This is limited positioning, not an exhaustive
novelty review or a transferred theorem from those sources.
