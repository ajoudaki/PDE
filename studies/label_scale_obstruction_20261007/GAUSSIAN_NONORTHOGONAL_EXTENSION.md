# Gaussian nonorthogonal perturbations of the orthogonal fitting theorem

Status: complete candidate extension proof, awaiting independent review. The frozen orthogonal proof in GAUSSIAN_POSITIVE_GEOMETRY.md is unchanged. No experiments were used.

## 1. Claim and dependencies

Fix \(m\ge2\), \(a>0\), and \(\sigma\in\{-1,1\}^m\). There is a deterministic \(\varepsilon>0\), depending on \(m,a\), such that the following holds. Let \(X\in\mathbb R^{d\times m}\) have unit columns and
\[
\|X^\top X-I_m\|_{\rm op}<\varepsilon,\qquad
\|y-a\sigma\|_2<\varepsilon.
\]
Use the exact network and flow
\[
U=\tanh(AX),\quad H=\tanh(WU),\quad
f=H^\top w/n,\quad r=f-y,\quad
\mathcal L=\|r\|_2^2/m,
\]
\[
\dot A=-n\nabla_A\mathcal L,\qquad
\dot W=-\nabla_W\mathcal L,\qquad
\dot w=-n\nabla_w\mathcal L,
\]
with independent \(A_{ij}\sim N(0,1)\), \(W_{ij}\sim N(0,1/n)\), and exactly \(w(0)=0\). Then a deterministic \(c>0\), independent of width, satisfies
\[
\Pr\{\mathcal L_n(t)\le \mathcal L_n(0)e^{-ct}
                 \text{ for every }t\ge0\}\longrightarrow1.
\tag{1}
\]
In particular the actual finite-width limiting loss is exactly zero on this event.

The proof uses the orthogonal theorem and its compact-time Gaussian-program bridge in Sections 11 and 13 of the frozen note, with its stated dependence on maintained book III.F. It does not assume a population flow for the perturbed geometry. Instead it compares the actual finite perturbed flow with the actual finite orthogonal reference over one deterministic time interval, and then applies deterministic finite-width capture.

This is an open neighborhood of orthogonal geometries and equal-magnitude labels. It does not cover arbitrary fixed input Grams or arbitrary label ratios. The neighborhood is not asserted to have a useful explicit radius.

The two new ingredients are:

1. uniform Gaussian tails for the reverse fields of the **orthogonal reference**, proved by Gaussian sensitivity and integration by parts;
2. a tail-splitting stability estimate in the bounded first features \(U\), which avoids unbounded natural-coordinate ratios.

Signs may be absorbed into input columns exactly as in the frozen proof. This conjugates the input Gram by a diagonal sign matrix and preserves its distance to \(I_m\). We therefore prove the statement near \(y_0=a\mathbf1_m\).

## 2. Exact equations and finite-horizon bounds

Write
\[
\Gamma=X^\top X,\quad
z_a=Wu_a,\quad h_a=\tanh z_a,\quad
D_a=1-u_a^2,\quad
b_a=w\odot(1-h_a^2),\quad B_a=W^\top b_a.
\]
Products and powers of neuron fields are pointwise. For any \(v\in\mathbb R^n\), set \(\|v\|_{2,n}=\|v\|_2/\sqrt n\); for a tuple of sample fields use the corresponding normalized Frobenius norm.

The first-feature dynamics close exactly:
\[
\dot u_a=-\frac2m D_a\odot
       \sum_b\Gamma_{ab}r_b D_b\odot B_b.
\tag{2}
\]
The other equations are
\[
\dot W=-\frac2{mn}\sum_a r_a b_a u_a^\top,\qquad
\dot w=-\frac2m\sum_a r_a h_a.
\tag{3}
\]
These are identities for the original fully trained network, not a different feature-space optimizer.

Fix \(T<\infty\) and an upper bound \(Y\) on \(\|y\|_2\). Exact loss dissipation and zero initial prediction give
\[
\|r(t)\|_2\le Y,\qquad
\|w(t)\|_\infty\le P:=2TY/\sqrt m,
\qquad 0\le t\le T.
\tag{4}
\]
Writing \(V=W-W_0\), the accumulated-residual bound gives
\[
\|V(t)\|_F\le P^2/2,\qquad
\|W(t)\|_{\rm op}\le L+P^2/2,\quad L=\|W_0\|_{\rm op}.
\tag{5}
\]
Consequently all finite-dimensional trajectories exist through every finite time: the first-layer, middle-weight, and readout velocities are bounded on each finite horizon by these estimates. The first-layer bound also uses fixed \(\|X\|_{\rm op}\). No tail estimate is needed for this finite-width continuation.

## 3. Orthogonal-reference sensitivity to its initialized Gaussian matrix

In this section only, \(\Gamma=I_m\) and \(y=y_0\). Condition on arbitrary initialized first-layer rows. Let
\[
\zeta(z)=z/2+\sinh(2z)/4,\qquad
\psi(\xi)=\tanh(\zeta^{-1}(\xi)),\qquad
\xi_a=\zeta(Ax_a).
\]
Then \(|\psi|\le1\), \(|\psi'|\le1\), and the reference dynamics are exactly
\[
\dot\xi_a=-\frac2m r_a B_a,\qquad
\dot V=-\frac2{mn}\sum_a r_a b_a u_a^\top,\qquad
\dot w=-\frac2m\sum_a r_a h_a.
\tag{6}
\]
The first-layer initial conditions are held fixed when differentiating below. Write \(W_0=Q/\sqrt n\), where the entries of \(Q\) are independent standard Gaussians.

All constants in this section may depend on \(T,m,Y\), but not on \(n\), the conditioned first-layer roots, or \(Q\), unless an explicit dependence on \(L=\|Q/\sqrt n\|_{\rm op}\) is displayed.

### 3.1 The variational estimate

For a deterministic perturbation \(\Delta Q\), denote the directional derivatives of \((\xi,w,V)\) by \((\eta,v,E)\), and put
\[
\mathcal R=\|\eta\|_F+\|v\|_2+\sqrt n\|E\|_F.
\]
All three derivatives start at zero. Set
\[
F_U=\|(\Delta Q/\sqrt n)U\|_F,\qquad
F_b=\|(\Delta Q^\top/\sqrt n)[b_1,\ldots,b_m]\|_F.
\]
For \(M=L+P^2/2\), differentiating the forward pass gives
\[
\|\delta U\|_F\le\|\eta\|_F,\qquad
\|\delta H\|_F\le F_U+\sqrt m\,\mathcal R+M\mathcal R,
\]
\[
\|\delta b\|_F\le\sqrt m\|v\|_2+2P\|\delta H\|_F,
\qquad
\sqrt n\|\delta r\|_2
\le\sqrt m\|v\|_2+P\|\delta H\|_F.
\tag{7}
\]
For the reverse fields,
\[
\|\delta B\|_F
\le F_b+P\sqrt m\,\mathcal R+M\|\delta b\|_F.
\tag{8}
\]
Here, for example,
\(\|EU\|_F\le\sqrt{mn}\|E\|_F\) and
\(\|E^\top b\|_F\le P\sqrt{mn}\|E\|_F\).

In the derivative of the first equation in (6), the residual-variation term is bounded by
\[
\|[B_a\,\delta r_a]_a\|_F
\le MP\sqrt n\,\|\delta r\|_2.
\]
For the middle equation, multiply its differentiated Frobenius norm by \(\sqrt n\); the three terms are bounded by constants times
\(\sqrt n\|\delta r\|_2,\|\delta b\|_F,\|\delta U\|_F\).
The readout equation has the same first and third bounds. Combining these with (7)–(8) yields the upper Dini derivative estimate
\[
D^+\mathcal R\le C(1+L^2)\mathcal R
       +C(1+L)(F_U+F_b).
\tag{9}
\]
This estimate does not involve the size of the natural-coordinate roots.

For arbitrary \(\Delta Q\),
\[
F_U+F_b\le C\|\Delta Q\|_F.
\]
For a single-entry perturbation \(\Delta Q=e_i e_j^\top\), only one row or column is forced directly, so instead
\[
F_U+F_b\le C/\sqrt n.
\tag{10}
\]
Gronwall, (7), and (8) imply, uniformly on \(0\le t\le T\),
\[
\|\delta B\|_F+\|\delta b\|_F
\le C_T(L)\|\Delta Q\|_F,\qquad
C_T(L)\le C\exp(C L^2),
\tag{11}
\]
and, for a single-entry perturbation,
\[
\|\partial b/\partial Q_{ij}\|_F\le C_T(L)/\sqrt n.
\tag{12}
\]
Polynomial factors in \(L\) have been absorbed by increasing the displayed exponential constant. Finite-dimensional smooth dependence justifies the differentiation; the estimates then extend to finite differences along segments on which \(L\) is bounded.

### 3.2 A bounded conditional mean

A \(1/4\)-net on each unit sphere has cardinality at most \(9^n\), and the norm is at most twice the largest bilinear form on the two nets. The scalar Gaussian tail and a union bound give
\[
\Pr\{L>x\}\le2\exp(2n\log9-nx^2/8)
\le2e^{-nx^2/16}\qquad(x\ge10).
\tag{13}
\]
Thus, for every fixed \(C\), \(\mathbb E e^{CL^2}\) is bounded uniformly over all sufficiently large \(n\). This follows by integrating the tail in (13), splitting at 10, and choosing \(n>32C\).

For a fixed sample \(a\) and first-layer neuron \(j\), Gaussian integration by parts gives
\[
\mathbb E_Q B_{a,j}
=\frac1{\sqrt n}\sum_i
  \mathbb E_Q\!\left[Q_{ij}b_{a,i}\right]
  +\mathbb E_Q(V^\top b_a)_j
=\frac1{\sqrt n}\sum_i
  \mathbb E_Q\frac{\partial b_{a,i}}{\partial Q_{ij}}
  +\mathbb E_Q(V^\top b_a)_j.
\tag{14}
\]
The first term is uniformly bounded by (12)–(13).
The learned-weight term also has a coordinatewise bound independent of width. Indeed, (3) gives
\[
(V^\top b_a(t))_j
=-\frac2m\int_0^t\sum_c r_c(v)\,u_{c,j}(v)
             \langle b_c(v),b_a(t)\rangle_n\,dv,
\]
where \(\langle x,z\rangle_n=x^\top z/n\). Its absolute value is at most \(C(T,m,Y)\), since \(|u_{c,j}|\le1\), \(|r_c|\le Y\), and \(\|b_c\|_{2,n}\le P\). Consequently
\[
\sup_{a,j,t\le T}
\left|\mathbb E_Q B_{a,j}(t)\right|\le C.
\tag{15}
\]
All bounds are conditional on arbitrary first-layer roots, with constants independent of those roots. The exponential derivative bound and (13) justify integration by parts by cutoff and dominated convergence for sufficiently large \(n\).

### 3.3 Gaussian concentration, with the needed theorem proved

We use the following elementary Gaussian concentration fact. If \(F:\mathbb R^N\to\mathbb R\) is \(K\)-Lipschitz and \(G\) is standard Gaussian, then
\[
\Pr\{|F(G)-\mathbb EF(G)|>x\}
\le2e^{-x^2/(2K^2)}.
\tag{16}
\]
For completeness, let \(P_tq(x)=\mathbb E q(e^{-t}x+\sqrt{1-e^{-2t}}G)\). Gaussian integration by parts, invariance, and differentiation of \(P_t\) give, first for positive smooth bounded \(q\),
\[
\operatorname{Ent}_\gamma(q)
=\int_0^\infty
 \mathbb E_\gamma\frac{|\nabla P_tq|^2}{P_tq}\,dt.
\]
The identity follows by differentiating
\(\mathbb E(P_tq)\log(P_tq)\), whose derivative is the negative integrand, and using its limit \((\mathbb Eq)\log(\mathbb Eq)\). Since
\(\nabla P_tq=e^{-t}P_t\nabla q\), Cauchy–Schwarz under the averaging measure gives
\[
\frac{|\nabla P_tq|^2}{P_tq}
\le e^{-2t}P_t\!\left(\frac{|\nabla q|^2}{q}\right).
\]
Integration and invariance yield
\(\operatorname{Ent}_\gamma(q)\le\frac12\mathbb E_\gamma|\nabla q|^2/q\).
Apply this to \(q=e^{\lambda F}\). For
\(\Lambda(\lambda)=\log\mathbb E e^{\lambda F}\),
\[
\lambda\Lambda'(\lambda)-\Lambda(\lambda)
\le\lambda^2K^2/2.
\]
Integrating the derivative of \(\Lambda(\lambda)/\lambda\) from zero proves
\(\log\mathbb E e^{\lambda(F-\mathbb EF)}\le\lambda^2K^2/2\).
Chernoff's bound at \(\lambda=x/K^2\), and the same bound for \(-F\), give (16). Smooth truncation and convolution extend the argument to all Lipschitz \(F\); domination follows from Gaussian integrability of \(\exp(c|G|)\). Thus no unverified concentration hypothesis is being inserted.

By (11), each map \(Q\mapsto B_{a,j}(t)\) is \(C_T(10)\)-Lipschitz on the convex set \(\{L\le10\}\). Extend it to the entire Euclidean matrix space with this same Lipschitz constant. At \(Q=0\), the zero-readout reference stays at \(w=V=0\), so \(B=0\); the extension can therefore be chosen to vanish there and obey \(|F(Q)|\le C\|Q\|_F\).

The mean of the extension differs from (15) by \(o(1)\), uniformly in the conditioned roots, \(a,j,t\). In fact
\[
|B_{a,j}(t)|\le P\sqrt n(L+P^2/2),\qquad
|F(Q)|\le C\|Q\|_F,
\]
and Cauchy–Schwarz with (13) makes the expectation of their sum on \(\{L>10\}\) tend to zero exponentially, up to a polynomial prefactor.

Equation (16) now supplies bounded-mean sub-Gaussian tails on \(\{L\le10\}\). The same exceptional-event estimates imply the useful consequence
\[
\limsup_{n\to\infty}\ 
\sup_{\text{first-layer roots},\,a,j,t\le T}
\mathbb E_Q\bigl[(|B_{a,j}(t)|-R)_+^2\bigr]
\le C e^{-cR^2}\qquad(R\ge1).
\tag{17}
\]
For the good-event contribution, integrate (16) beyond \(R\); enlarge \(C\) for \(R\) below the bounded mean. For the bad-event contribution, use the displayed deterministic bound and (13). The constants \(C,c>0\) may depend on \(T,m,Y\), never on \(R\) or width.

The learned-weight term in (14) is essential. Omitting it would incorrectly identify the full reverse field with the initialized Gaussian action.

## 4. Reference tails hold with probability tending to one

The compact-time orthogonal Gaussian-program argument in the frozen note also applies to \(B_a=W^\top b_a\): this is an allowed reused-transpose observation, and the transformed-state Euler estimates control it in normalized \(L^2\). In particular its empirical coordinate law converges in \(W_2\), for each fixed time, to the deterministic reference population law.

For fixed \(R\), \(x\mapsto(|x|-R)_+\) is globally Lipschitz. Therefore
\[
\|(|B_{a,n}(t)|-R)_+\|_{2,n}
\longrightarrow
\|(|B_{a,\infty}(t)|-R)_+\|_2
\]
in probability. From (17) and Fatou's inequality along an almost surely convergent subsequence, the limiting squared norm is at most \(Ce^{-cR^2}\). This step requires no independence of the trained query and \(W_0\).

The convergence is uniform on \(0\le t\le T\). On \(\{L\le10\}\), equations (4)–(6), bounded \(\psi'\), and bounded top-activation derivatives give a width-independent bound on
\[
\|\dot B_a(t)\|_{2,n}
\le\|\dot W\|_{\rm op}\|b_a\|_{2,n}
       +\|W\|_{\rm op}\|\dot b_a\|_{2,n}.
\]
Every term on the right is bounded by the preceding finite-horizon estimates; in particular
\(\dot b_a=\dot w(1-h_a^2)-2wh_a\dot h_a\), with \(w\) pointwise bounded. A finite time net therefore upgrades pointwise convergence of the tail norms to uniform convergence.

After adjusting \(C,c\), we have for each fixed \(R\ge1\)
\[
\Pr\!\left\{
 \max_a\sup_{t\le T}
 \|(|B_{a,n}(t)|-R)_+\|_{2,n}
 \le C e^{-cR^2}
 \right\}\longrightarrow1.
\tag{18}
\]
Only the orthogonal reference has been passed to a population limit.

## 5. Stability in bounded first features

Let bars denote this orthogonal reference, with labels \(y_0\), and compare it with the exact finite-width system (2)–(3) with Gram \(\Gamma\), labels \(y\), and the same \(W_0\). Write
\[
\delta=\|\Gamma-I_m\|_{\rm op}+\|y-y_0\|_2,\qquad
E(t)=\|U-\bar U\|_{F,n}^2
    +\|W-\bar W\|_F^2+\|w-\bar w\|_{2,n}^2.
\]
Assume \(\|\Gamma\|_{\rm op}\le2\), bounded \(\|y\|_2\), and \(L\le10\). On the fixed interval, (4)–(5) hold for both systems with common constants. The forward and upper-backward differences obey
\[
\|H-\bar H\|_{F,n}
+\|b-\bar b\|_{F,n}
+\|B-\bar B\|_{F,n}
\le C\sqrt E,
\qquad
\|r-\bar r\|_2\le C\sqrt E+\delta.
\tag{19}
\]
These inequalities follow by adding and subtracting one factor at a time, using the pointwise readout bound, \(|u_a|\le1\), and the middle operator bounds. Equations (3) consequently contribute at most \(C(E+\delta^2)\) to \(E'\).

In (2), separate \(\Gamma=I_m+(\Gamma-I_m)\). The second part has normalized norm at most \(C\delta\); its energy pairing contributes at most \(C(E+\delta^2)\). In the diagonal part, add and subtract \(\bar D_a^2\bar B_a\bar r_a\). All terms are controlled by (19) except
\[
(D_a^2-\bar D_a^2)\bar B_a\bar r_a.
\]
Because \(D_a=1-u_a^2\) and \(|u_a|,|\bar u_a|\le1\),
\(|D_a^2-\bar D_a^2|\le4|u_a-\bar u_a|\).
Its pairing with the first-feature difference is therefore at most
\[
C\sum_a\frac1n\sum_j
 |u_{a,j}-\bar u_{a,j}|^2\,|\bar B_{a,j}|.
\]
On \(\{|\bar B_a|\le2R\}\) this is at most \(CR E\). On the complement use \(|u_a-\bar u_a|\le2\) and
\[
|\bar B_a|\mathbf1_{\{|\bar B_a|>2R\}}
\le2(|\bar B_a|-R)_+.
\]
Cauchy–Schwarz then gives the exact differential inequality
\[
E'\le C(1+R)E+C\delta^2
  +C\sum_a\|(|\bar B_a|-R)_+\|_{2,n}.
\tag{20}
\]
This is where bounded first features, rather than raw preactivations, remove the need for fourth moments or exponential moments of the perturbed trajectory.

Couple the first-layer initializations using an \(n\times m\) iid standard Gaussian matrix \(Z_0\):
\[
\bar U(0)=\tanh Z_0,\qquad
U(0)=\tanh(Z_0\Gamma^{1/2}).
\]
The latter is exactly the initialized feature law for input Gram \(\Gamma\), independent of \(W_0\). When \(\|\Gamma-I_m\|_{\rm op}\le1/2\), spectral calculus gives
\(\|\Gamma^{1/2}-I_m\|_{\rm op}\le C\|\Gamma-I_m\|_{\rm op}\).
Since tanh is 1-Lipschitz,
\[
E(0)\le C\delta^2\|Z_0\|_{F,n}^2\le C_m\delta^2
\tag{21}
\]
with probability tending to one by the iid law of large numbers. The initial \(W,w\) agree.

Combining (18), (20), and (21), for every fixed \(R\ge1\),
\[
\Pr\!\left\{
\sup_{t\le T}E(t)
\le C_T e^{C_T R}\bigl(\delta^2+e^{-c_T R^2}\bigr)
\right\}\longrightarrow1.
\tag{22}
\]
The required limit order is explicit: given an error tolerance, first choose a finite \(R\) so that \(e^{C_TR-c_TR^2}\) is small; then choose a fixed \(\delta>0\) so that \(e^{C_TR}\delta^2\) is small; only then send width to infinity. Thus the allowable geometry perturbation does not shrink with width.

## 6. Transfer to all-time exact fitting

The readout-plus-middle tangent features are, for each sample,
\[
h_a,\qquad b_a\otimes u_a,
\]
where the neuron and Hilbert–Schmidt norms have the normalizations of the frozen note. On the bounded finite horizon, (19) and the rank-one difference identity show that these tangent features, their Gram matrix \(K_{\rm R+W}\), and the predictions differ from the reference by at most \(C_T\sqrt E\).

The reference orthogonal proof gives a positive minimum eigenvalue \(\kappa\) on its full finite-feature-time path, and a finite feature endpoint \(s_*\). Set \(p=s_*+1\) and \(b=10+p^2/2\). For a general input Gram with \(\|\Gamma\|_{\rm op}\le2\), the deterministic capture proof remains valid after replacing its first-feature displacement bound by
\[
\alpha(s)=\frac2{\sqrt m}
 \left[bM_p(s)+\frac{M_p(s)^2}{2}\right],
\qquad M_p(s)=ps+s^2/2.
\tag{23}
\]
Indeed the original first-layer velocity and the conversion from \(A\) to \(AX\) together contribute \(\|X\|_{\rm op}^2=\|\Gamma\|_{\rm op}\le2\). All other capture estimates are unchanged.

Choose a deterministic sufficiently late reference time \(T\) so that the snapshot has a strict capture margin using (23), a fixed positive kernel lower bound, and residual as small as needed. Such a time exists because the reference residual tends to zero while its endpoint kernel stays positive definite.

The exact accumulated-residual bounds give, for either finite system,
\[
\|w(T)\|_\infty\le S_n(T),\qquad
\|W(T)\|_{\rm op}\le\|W_0\|_{\rm op}+S_n(T)^2/2,\qquad
S_n(T)=2\int_0^T\sqrt{\mathcal L_n(t)}\,dt.
\]
Reference convergence gives \(\bar S_n(T)\to S_\infty(T)\le s_*\). Equation (19) and the reverse triangle inequality for \(\|r\|_2\) show
\[
|S_n(T)-\bar S_n(T)|
\le C_T\left(\sup_{t\le T}\sqrt{E(t)}+\delta\right).
\]
Thus sufficiently small error in (22) places the perturbed finite snapshot inside the same strict capture region, with the bounds \(p,b\), probability tending to one.

The same small-error choice preserves \(K_{\rm R+W}\succeq(\kappa/2)I_m\) throughout \([0,T]\), using uniform reference kernel convergence. Deterministic capture controls the entire later interval. The full tangent kernel is at least its readout-plus-middle part, so its exact loss dissipation gives a deterministic positive exponential rate on both intervals. Taking the smaller rate proves (1).

This argument establishes an actual open neighborhood of input geometries and labels. It does not infer that neighborhood from finite-\(n\) continuity, does not use an unproved population model for correlated inputs, and does not interchange width with infinite training time.

## 7. Review boundary

The candidate relies on the separately audited orthogonal theorem. Its new critical checks are the scaled variational inequalities (9)–(12), the learned-weight correction in (14), and the bounded-feature stability inequality (20). All three are displayed with their dimension-dependent factors.

If those checks pass, the nonorthogonal-neighborhood result is unconditional for the canonical initialization, not a conditional future-Gram hypothesis. Outside this neighborhood, arbitrary correlated data and arbitrary mixed-label ratios remain unresolved. The proof supplies no strong negative alternative.
