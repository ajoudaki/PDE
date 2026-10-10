# Sample moment tensors: exact identities and a conditional autonomous construction

Scope: prompt-only independent mathematical route, 10 October 2026. Scientific
inputs were the supervisor's stated problem and activation-class clarification;
required repository/process and
canonical-notation skills were read. No other study, book passage, external source,
experiment, or prior route was used. These are derived candidates, not independently
checked or promoted results. The sample axis is treated separately from width and
temporal closure order; no claim about simultaneous limits is made.

## 1. Exact sample projection and its omitted term

For \(m\) examples, use \(\langle u,v\rangle_m=m^{-1}\sum_a u_av_a\).
For vector-valued sample fields, let \(\|u\|_m^2=m^{-1}\sum_a\|u_a\|_2^2\)
and apply sample projections componentwise. A bias-free scalar-output network is
\(h_a^{(0)}=x_a\), \(z_a^{(\ell)}=W^{(\ell)}h_a^{(\ell-1)}\),
\(h_a^{(\ell)}=\phi(z_a^{(\ell)})\), \(f_a=w^\top h_a^{(L)}\).
Its residual and loss are \(r_a=f_a-y_a\) and
\(\mathcal L=\tfrac12\langle r,r\rangle_m\). Define the unit-residual
backward response \(\delta_a^{(\ell)}=\nabla_{z_a^{(\ell)}}f_a\).
With constant positive mobility \(\gamma_\ell\), physical gradient flow obeys
\[
\dot W^{(\ell)}=-\gamma_\ell\langle b^{(\ell)}h^{(\ell-1)\top}\rangle_m,
\qquad b_a^{(\ell)}=r_a\delta_a^{(\ell)}.
\]
Here \(\langle b h^\top\rangle_m=m^{-1}\sum_a b_ah_a^\top\), a matrix.

Fix empirical orthonormal functions \(\psi_1,\ldots,\psi_R\), with
\(\psi_1=1\). Set \(u_i=\langle\psi_i,u\rangle_m\),
\(Pu=\sum_i\psi_i u_i\), and \(Q=I-P\). Orthogonality gives the exact identity
\[
\langle b h^\top\rangle_m
=\sum_{i=1}^R b_i h_i^\top+\langle Qb\,(Qh)^\top\rangle_m,
\qquad
\left\|\langle Qb\,(Qh)^\top\rangle_m\right\|_F
\le\|Qb\|_m\|Qh\|_m.
\]
The mixed terms vanish componentwise; the bound follows by the triangle inequality
and scalar Cauchy--Schwarz. Thus jointly small *exact* projection tails give a
quadratic instantaneous gradient error. Computing \(b_i\) from full samples at
every time is not an autonomous compression. Replacing the full trajectory by a
reduced one introduces a separate dynamical error.

If residuals, backward responses and activations are projected separately, the
fixed third moment tensor is
\[
M_{ijk}=\langle\psi_i\psi_j\psi_k\rangle_m,
\qquad
\langle (Pr)(P\delta)(Ph)^\top\rangle_m
=\sum_{i,j,k=1}^R M_{ijk}\,r_i\delta_jh_k^\top.
\]
This differs from projecting \(b=r\delta\) directly. Its exact error is
\[
\langle (Qr)\delta h^\top\rangle_m
+\langle (Pr)(Q\delta)h^\top\rangle_m
+\langle (Pr)(P\delta)(Qh)^\top\rangle_m.
\]
For example, the first term has Frobenius norm at most
\(\|Qr\|_m\|\delta\|_\infty\|h\|_m\), where
\(\|\delta\|_\infty=\max_a\|\delta_a\|_2\). The other two are bounded by
\(\|Pr\|_\infty\|Q\delta\|_m\|h\|_m\) and
\(\|Pr\|_\infty\|P\delta\|_m\|Qh\|_m\). Projection is not generally an
\(L^\infty\) contraction. Separate low-rank approximations therefore do not
automatically inherit the preceding quadratic-tail estimate.

## 2. Nonlinear sample algebra and storage

The coefficient vector of \(P[(Pu)(Pv)]\) is
\((u\star v)_i=\sum_{j,k}M_{ijk}u_jv_k\). Multiplication by a fixed field
\(u\) is an \(R\)-by-\(R\) matrix with entries
\(\sum_kM_{ijk}u_k\). Dense storage is \(R^2\) for that matrix and \(R^3\)
for the reusable tensor; symmetry reduces constants, not these worst-case orders.

Repeated projected multiplication is generally not full-product projection:
\[
P\{P[(Pu)(Pv)](Pw)\}
-P[(Pu)(Pv)(Pw)]
=-P\{Q[(Pu)(Pv)](Pw)\}.
\]
This is an explicit high-to-low interaction. In particular, \(\star\) need not
be associative. For a polynomial activation of degree \(p\), exact evaluation of
\(P\phi(Pz)\) needs fixed moments through order \(p+1\); third moments alone
suffice for a quadratic activation. Dense worst-case storage is \(O(R^{p+1})\).
For a polynomial coordinate basis, unprojected degree is multiplied by \(p\)
per hidden layer, hence can grow as \(p^L\). A nonpolynomial activation generally
creates arbitrarily high degrees. Fixed rank therefore needs truncation,
special algebraic structure, or a further controlled nonlinear approximation.

If a sample subspace contains constants and is closed under every pointwise
product, it is exactly the functions constant on the classes of a partition of
the finite sample set. To see this, identify samples on which every subspace
function agrees. A generic linear combination of a finite basis has distinct
values on the finitely many classes: avoid the finitely many hyperplanes where
two class values agree. Polynomial interpolation in that one function gives
each class indicator, so all class-constant functions lie in the subspace.
Thus global exact algebra closure has a grouping interpretation. This does not
rule out smaller invariant families for a particular reachable trajectory.

## 3. A concrete autonomous Galerkin network with an energy identity

The first approximation is to replace each activation by its sample projection.
The non-affine polynomial activation below is a toy specialization outside the
stated class of activations with bounded derivatives on a strip. Its extension
to that class requires the separate value-and-derivative approximation below.
For \(\phi(s)=c_0+c_1s+c_2s^2\), define the map on one neuron's
coefficient vector \(z\in\mathbb R^R\) by
\[
A_i(z)=c_0\mathbf1_{i=1}+c_1z_i+c_2\sum_{j,k}M_{ijk}z_jz_k,
\qquad
\frac{\partial A_i}{\partial z_j}
=c_1\mathbf1_{i=j}+2c_2\sum_kM_{ijk}z_k.
\]
The tensor is symmetric, so this Jacobian is symmetric. This is exactly
\(P\phi(\sum_i z_i\psi_i)\), represented by its coefficients. It defines
a changed network, with nonlinear moving features; it is not an exact rewrite
of the original network unless the required projection tails vanish.

Retain the fixed input coefficients \(X_i=\langle\psi_i,x\rangle_m\) and
label coefficients \(Y_i=\langle\psi_i,y\rangle_m\). The reduced forward pass is
\[
\widehat h_i^{(0)}=X_i,\qquad
\widehat z_i^{(\ell)}=W^{(\ell)}\widehat h_i^{(\ell-1)},\qquad
(\widehat h_{\nu i}^{(\ell)})_{i=1}^R
=A((\widehat z_{\nu i}^{(\ell)})_{i=1}^R),\qquad
\widehat f_i=w^\top\widehat h_i^{(L)}.
\]
Here \(\nu\) indexes neurons. Define \(\widehat r_i=\widehat f_i-Y_i\) and
\(\mathcal L_R=\tfrac12\sum_i\widehat r_i^2\).
The reconstructed empirical loss equals
\(\mathcal L_R+\tfrac12\|Qy\|_m^2\), because its output belongs to the
sample subspace. The optional constant \(\|Qy\|_m^2\) can be retained as one scalar.

For explicit reverse evaluation, let
\(E_{\nu i}^{(\ell)}=\partial\mathcal L_R/\partial\widehat z_{\nu i}^{(\ell)}\)
and \(S_{\nu i}^{(\ell)}=\partial\mathcal L_R/\partial\widehat h_{\nu i}^{(\ell)}\).
Initialize \(S_{\nu i}^{(L)}=w_\nu\widehat r_i\), then compute
\[
E_{\nu,:}^{(\ell)}=DA(\widehat z_{\nu,:}^{(\ell)})^\top S_{\nu,:}^{(\ell)},
\qquad S_i^{(\ell-1)}=W^{(\ell)\top}E_i^{(\ell)},
\]
where each colon denotes a column vector across sample modes. Therefore
\[
\dot W^{(\ell)}=-\gamma_\ell\sum_i E_i^{(\ell)}\widehat h_i^{(\ell-1)\top},
\qquad
\dot w=-\gamma_{L+1}\sum_i\widehat r_i\widehat h_i^{(L)},
\qquad
\frac{d\mathcal L_R}{dt}
=-\sum_\ell\gamma_\ell\|\nabla_{W^{(\ell)}}\mathcal L_R\|_F^2
-\gamma_{L+1}\|\nabla_w\mathcal L_R\|_2^2\le0.
\]
The identities follow by differentiating the displayed finite computation graph
and the loss. In fact this polynomial gradient flow exists globally: for the
vector \(\theta\) of all parameters and \(\gamma_{\max}=\max_\ell\gamma_\ell\),
\(\int_0^t\|\dot\theta\|_2^2\,ds\le\gamma_{\max}\mathcal L_R(0)\), whence
\(\|\theta(t)-\theta(0)\|_2\le\sqrt{t\gamma_{\max}\mathcal L_R(0)}\).
This excludes escape from every bounded parameter set in finite time, allowing
the locally smooth ODE to continue. It proves neither boundedness for all time
nor zero limiting loss.

Fixed sample-dependent storage is \(dR+R+R^3\), plus a compact description
of the basis if evaluation on new inputs is required. Moving parameters are the
network weights; activation/adjoint workspace is \(O(R\sum_\ell n_\ell)\).
Thus this route compresses sample dependence, while not itself compressing
neurons. All moments can be obtained from pretraining data passes and the
full \(m\)-by-\(R\) evaluation matrix can then be discarded. This requires an
explicit, compactly evaluable basis; arbitrary stored singular vectors fail it.
Generic dense third moments have \(O(mR^3)\) preprocessing cost. Small empirical
Gram eigenvalues can make orthonormalization ill-conditioned.

For degree \(p\), use
\(A_i(z)=\sum_{s=0}^p c_s\sum_{j_1,\ldots,j_s}
\langle\psi_i\psi_{j_1}\cdots\psi_{j_s}\rangle_m
z_{j_1}\cdots z_{j_s}\); the empty product at \(s=0\) is \(1\).
Its exact Jacobian uses the same moments through order \(p+1\), and the same
energy argument applies. Polynomial approximation of a general activation needs
both value and derivative accuracy on a controlled reachable preactivation range.

## 4. What sample rank and temporal order do, and do not, prove

An elementary sample-rank estimate is available under explicit geometric
regularity. Suppose \(x_a=g(\zeta_a)\), \(\zeta_a\in[0,1]^k\),
\(g\) is \(L_g\)-Lipschitz, and every required sample field extends to a
function on the observed image with ambient Lipschitz constant at most \(L_F\).
Greedily choose observed centers more than \(\rho>0\) from all earlier centers.
The final centers cover the dataset within \(\rho\). A grid on the latent cube
of side at most \(\rho/(L_g\sqrt{k})\) puts at most one center in each cell,
since two image points in one cell have distance at most \(\rho\). Hence
\[
R\le\min\{m,\max(1,\lceil L_g\sqrt{k}/\rho\rceil^k)\}.
\]
For \(L_g=0\), one center suffices. Assign samples to nearest centers and use
the normalized cell indicators as orthonormal coordinates; an orthogonal rotation
recovers the constant-first convention above. Denote the projection by \(P\).
Center evaluation gives a cell-constant approximant with pointwise
error at most \(L_F\rho\); least-squares optimality of \(P\) gives
\(\sup_F\|(I-P)F\|_m\le L_F\rho\). The same partition works uniformly
over time if the Lipschitz constant does. Thus \(R=O((L_gL_F/\varepsilon)^k)\)
suffices for tail \(\varepsilon\), independently of \(m\).

The greedy algorithm uses observed distances, not latent coordinates. If the
fields are only Lipschitz in an unknown latent coordinate, with no ambient
Lipschitz or inverse-modulus control, this algorithmic conclusion does not follow.
Deriving this regularity for residuals also needs label regularity; arbitrary
labels need not satisfy the hypothesis.
Width independence would separately require appropriately scaled uniform response
norms. In indicator coordinates the tensor is diagonal, with
\(M_{jjj}=p_j^{-1/2}\) for cell mass
\(p_j\), so this construction reduces to weighted grouping. Its rank theorem
does not alone establish a richer tensor closure with overlapping sample modes.

For a fixed temporal expansion with \(q\) modes, a samplewise stored history
\(\bar h_{a,j}\) becomes coefficients
\(\langle\psi_i,\bar h_{\cdot,j}\rangle_m\), with \(qR\) entries per
neuron coordinate. Fixed sample projection commutes with time integration and
differentiation. Nonlinear evaluation still needs the tensors and tail controls
above. An independent temporal truncation need not preserve the Galerkin network's
energy identity. Increasing \(q\) cannot remove sample projection error.

Finally, a trajectory comparison requires error production *and* stability.
If the full and reduced parameter vector fields differ by at most \(\eta\)
on a common tube, the full field is \(K\)-Lipschitz there, and their initial
parameters agree, their distance \(e(t)\) satisfies \(e'\le Ke+\eta\).
Multiplying by \(e^{-Kt}\) and integrating yields
\(e(t)\le\eta(e^{Kt}-1)/K\), interpreted as \(\eta t\) when \(K=0\).
Obtaining \(\eta\to0\) needs uniform forward/backward projection defects,
nonlinear derivative control and a shared reachable tube. Sample rank by itself
supplies none of these bridges; proving them is the remaining central gap.
