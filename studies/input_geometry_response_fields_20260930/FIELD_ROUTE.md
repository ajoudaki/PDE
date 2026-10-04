# Input-field route: exact label separation and finite spatial closure

This scoped theory note uses only the supervisor's supplied network and memory equations. It does not inspect other studies or assume that an empirical feature or response matrix has low rank. The investigation and rigorous-mathematics skills were applied. No computation or training was performed.

**Conclusion.** Every backward memory field is affine in the label, with two coefficient fields regular in the input. Arbitrary square-integrable label noise is therefore compatible with sample-count-independent spatial compression. A finite autonomous spatial approximation of every fixed temporal order follows from Lipschitz input regularity; analyticity improves its coefficient count. The spatial statement below includes finite coefficient provenance and a whole-trajectory bound. Identification of the temporal-order limit with the original network is a separate obligation.

## 1. Contract

Let \(x=X(\xi)\), with \(\xi\in K=[-1,1]^p\), and let \(P\) be any joint probability law of \((\xi,y)\) with \(Y^2=\mathbb E y^2<\infty\). Empirical measures are included. The parametrization is supplied, not inferred. For the basic theorem \(X\) is Lipschitz; for spectral rates it has a bounded holomorphic extension.

Width \(n\), ambient input dimension \(d\), depth \(L\ge2\), temporal order \(q\ge1\), initialization, and horizon \(T<\infty\) are fixed. Complexity may depend on these quantities, accuracy, geometry, activation, and regularity bounds, but not empirical sample count. This is not a width-independent theorem. Fixed \(W_l^0\) remain available, and the same reconstructed weights act in forward and transpose propagation.

Define
\[
 \mu(E)=P(\xi\in E),\quad
 \nu(E)=\mathbb E[y1_{\{\xi\in E\}}],\quad m_2=Y^2.
\]
Then \(\nu\) is signed with \(\|\nu\|_{\rm TV}\le Y\). No density or smoothness of \(\nu\), or of a conditional mean, is assumed. Set
\[
 (D_qV)_k=kV_k+\sum_{j<k}(2j+1)V_j,\qquad 0\le k<q.
\]
Use zero initial backward training memory: \(A_k(0)=C_k(0)=0\). Forward moments have the prescribed \(H_0(0)=h(0)\), \(H_{k>0}(0)=0\).

The error is uniform on \([0,T]\), in input supremum norm for smooth fields and predictions and in \(L^2(P)\) for backward memory. No future trajectory or runtime measure oracle is allowed.

## 2. Exact label separation

At every time \(h_l,\delta_l,f\) depend on \(\xi\), but not the label attached to it: weights and clock are common to all examples. The linear moment equations therefore preserve
\[
 B_{l,k}(t,\xi,y)=A_{l,k}(t,\xi)-yC_{l,k}(t,\xi),                 \tag{2.1}
\]
where
\[
 \dot A_{l,k}=f\delta_l-\frac\rho\tau(D_qA_l)_k,\qquad
 \dot C_{l,k}=\delta_l-\frac\rho\tau(D_qC_l)_k,                 \tag{2.2}
\]
and
\[
 \dot H_{l,k}=\rho h_l-\frac\rho\tau(D_qH_l)_k.                \tag{2.3}
\]
Subtracting \(y\) times the second equation from the first gives exactly the supplied \(B\) equation and its initial value; uniqueness proves (2.1). The identity holds for the infinite moment family as well, one index at a time.

Consequently the hidden reconstruction is
\[
 W_l=W_l^0-\frac2{n\tau}\sum_{k<q}(2k+1)
 \left\{\int A_{l,k}H_{l-1,k}^{\mathsf T}d\mu
             -\int C_{l,k}H_{l-1,k}^{\mathsf T}d\nu\right\}.   \tag{2.4}
\]
The other equations become
\[
\begin{aligned}
 \dot W_1&=-\frac2{\sqrt d}
 \left\{\int f\delta_1X^{\mathsf T}d\mu-\int\delta_1X^{\mathsf T}d\nu\right\},\\
 \dot w&=-2\left\{\int fh_Ld\mu-\int h_Ld\nu\right\},\\
 \dot\tau&=\rho,\qquad
 \rho=\left(\int f^2d\mu-2\int f\,d\nu+m_2\right)^{1/2}.
\end{aligned}                                                \tag{2.5}
\]
Together with the original nonlinear forward and backward network, this exactly reformulates the fixed-\(q\) closure. Features are not frozen or linearized.

Interpret the last square root as \(\rho(f)=\|f-y\|_{L^2(P)}\). Thus
\[
 |\rho(f)-\rho(g)|\le\|f-g\|_{L^2(\mu)}\le\|f-g\|_\infty,      \tag{2.6}
\]
including at zero loss. Differentiating the square root and dividing by \(\rho\) is unnecessary.

Only \((\mu,\nu,m_2)\) affect the closure. The original weight flow uses \((\mu,\nu)\); label variance additionally affects its clock, and at finite temporal order it may affect the approximant through that clock. Replacing noisy labels by their conditional mean changes nothing only if the original \(m_2\) is retained separately for the clock.

If \(\|A-A_*\|_\infty\le a\) and \(\|C-C_*\|_\infty\le c\), then
\[
 \|B-B_*\|_{L^2(P)}\le a+Yc.                                 \tag{2.7}
\]
The rough label factor is retained exactly, rather than smoothed in the input.

At zero loss, \(A\) and \(C\) can still drift separately: their sources are \(f\delta\) and \(\delta\). Their combination \(A-yC\) cancels on the training law. Thus physical stationarity does not imply stationarity or an all-time bound for these separate coordinates. All field estimates below use a finite physical horizon.

## 3. Compact-horizon bounds and regularity

### Original flow

For the supplied scaling and loss \(\mathcal L=\mathbb E(f-y)^2\),
\[
 \dot{\mathcal L}
 =-\frac1n\|\dot W_1\|_F^2-\sum_{l=2}^L\|\dot W_l\|_F^2
                         -\frac1n\|\dot w\|^2.               \tag{3.1}
\]
Indeed, \(\nabla_{W_1}\mathcal L=(2/n)\mathbb E[r\delta_1x^{\mathsf T}/\sqrt d]\), so its mobility is \(n\); hidden weights have mobility one and the readout has mobility \(n\). Integration and Cauchy--Schwarz give
\[
 \|W_1(t)-W_1^0\|_F,\ \|w(t)-w^0\|\le\sqrt{nT\mathcal L(0)},
 \qquad \|W_l(t)-W_l^0\|_F\le\sqrt{T\mathcal L(0)}\quad(l\ge2).
                                                               \tag{3.2}
\]
For \(\phi\in C^{1,1}_{\rm loc}\), bounded inputs and integrable labels make the finite-dimensional vector field locally Lipschitz. These bounds prevent finite-time escape, yielding global continuation. Constants are sample-count independent if initialization and initial loss are uniformly bounded.

Bounded weights, Lipschitz \(X\), and locally Lipschitz \(\phi,\phi'\) give input Lipschitz bounds for \(h,\delta,f\) by finite composition and multiplication. The moment ODEs preserve these bounds for fixed \(q,T\).

For analytic \(X,\phi\), bounded weights give a common complex input neighborhood on each compact horizon. All real preactivations lie in compact intervals. Choose a complex neighborhood of each interval on which \(\phi\) is holomorphic and bounded. Uniform continuity and the bounded matrix norms permit a small complex neighborhood of \(K\) to map successively into those neighborhoods. Products with \(\phi'\) preserve response holomorphy, and integrating bounded holomorphic sources preserves moment holomorphy. This produces both a uniform radius and an envelope bound, not merely pointwise analyticity.

### Fixed-\(q\) closure with bounded activation and derivative

For general activation, the spatial theorem below assumes a bounded fixed-\(q\) reference on \([0,T]\). If \(M=\sup|\phi|<\infty\) and \(D=\sup|\phi'|<\infty\), as for tanh, this condition follows without assuming a hidden-weight energy law for the closure.

Its readout equation retains
\[
 \frac d{dt}\|w\|^2=-4n\mathbb E[f(f-y)]
      =nm_2-4n\mathbb E(f-y/2)^2\le nm_2.                     \tag{3.3}
\]
Hence \(B_w=(\|w^0\|^2+nTY^2)^{1/2}\) bounds \(\|w\|\), while
\[
 \|h_l\|\le M\sqrt n,\quad |f|\le F:=MB_w/\sqrt n,\quad
 \rho\le F+Y,\quad 1\le\tau\le1+T(F+Y).
\]
The moment integral formulas, with the usual Legendre polynomial \(P_k(1)=1\), are
\[
\begin{aligned}
 H_k(t)&=\int_0^1P_k(2s/\tau(t)-1)h(0)\,ds\\
       &\quad+\int_0^tP_k(2\tau(u)/\tau(t)-1)\rho(u)h(u)\,du,\\
 A_k(t)&=\int_0^tP_k(2\tau(u)/\tau(t)-1)f(u)\delta(u)\,du,\\
 C_k(t)&=\int_0^tP_k(2\tau(u)/\tau(t)-1)\delta(u)\,du.
\end{aligned}                                                 \tag{3.4}
\]
Differentiation verifies them by the polynomial identity defining \(D_q\), even if \(\rho=0\). Since \(|P_k|\le1\) on \([-1,1]\), a bound \(\|\delta_l\|\le\beta_l\) implies
\[
 \|H_{l,k}\|\le M\sqrt n\,\tau,\quad
 \|A_{l,k}\|\le TF\beta_l,\quad \|C_{l,k}\|\le T\beta_l.
\]
Using (2.4), \(\|\nu\|_{\rm TV}\le Y\), and \(\sum_{k<q}(2k+1)=q^2\),
\[
 \|W_l\|_F\le\|W_l^0\|_F+
            \frac{2q^2TM(F+Y)}{\sqrt n}\beta_l.               \tag{3.5}
\]
Start with \(\beta_L=DB_w\), bound \(W_L\), and then set \(\beta_{L-1}=D\|W_L\|_F\beta_L\); continue downward. Each bound uses already bounded deeper-layer quantities. Equation (2.5) finally bounds \(\dot W_1\) by \(2(F+Y)\beta_1\|X\|_\infty/\sqrt d\). All parameters and moments remain bounded, proving continuation on every finite horizon. This elementary estimate is \(q\)-dependent and proves no temporal convergence.

## 4. Finite autonomous spatial construction

Take a tensor grid of spacing at most \(a\) with \(S\) vertices and continuous piecewise multilinear nodal basis \(\psi_i\). Then \(\psi_i\ge0\), \(\sum_i\psi_i=1\), the interpolation operator \(I_a\) has supremum norm one, and
\[
 \|I_ag-g\|_\infty\le\sqrt p\,a\,\operatorname{Lip}(g).        \tag{4.1}
\]
The estimate follows by expressing \(I_ag(\xi)-g(\xi)\) as a convex combination of differences to vertices of the cell containing \(\xi\).

Store nodal values of \(H_{l,k},A_{l,k},C_{l,k}\), together with \(W_1,w,\tau\). Precompute just
\[
\begin{array}{ll}
 M_{ij}=\int\psi_i\psi_jd\mu,&N_{ij}=\int\psi_i\psi_jd\nu,\\
 v_i=\int\psi_i d\nu,&m_2=\mathbb E y^2,\\
 M^{X,b}_{ij}=\int X_b\psi_i\psi_jd\mu,&
 v^{X,b}_i=\int X_b\psi_i d\nu\quad(1\le b\le d).
\end{array}                                                   \tag{4.2}
\]
These finite arrays are all data-dependent coefficients. Computing them from empirical data can cost the sample count; the claim concerns subsequent state and evolution, not free data ingestion.

At every ODE evaluation:

1. Reconstruct hidden weights by (2.4), using the \(M,N\) contractions of stored nodal coefficients.
2. Evaluate the original nonlinear network and its exact transpose backpropagation at the grid inputs \(X(\xi_i)\), obtaining \(h_{l,i},\delta_{l,i},f_i\). Interpolate these to \(h_{l,a},\delta_{l,a},f_a\).
3. Compute \(\rho_a^2=f^{\mathsf T}Mf-2v^{\mathsf T}f+m_2=\|f_a-y\|_{L^2(P)}^2\), taking the nonnegative root.
4. Advance moments by the nodal forms of (2.2)--(2.3), for example \(\dot A_{l,k,i}=f_i\delta_{l,i}-(\rho_a/\tau)(D_qA_l)_{k,i}\).
5. Advance \(w\) by the finite contractions for \(-2\int(f_a-y)h_{L,a}dP\). Advance column \(b\) of \(W_1\) by
   \[
   -\frac2{\sqrt d}\left\{\sum_{i,j}M^{X,b}_{ij}f_i\delta_{1,j}
                               -\sum_jv^{X,b}_j\delta_{1,j}\right\},
   \]
   and set \(\dot\tau=\rho_a\).

No nonlinear function is integrated at runtime. Linear interpolation gives \(f_a=w^{\mathsf T}h_{L,a}/n\), so the readout bound (3.3) remains valid. Static arrays come from one actual data law; this ensures positivity of the loss expression.

There are at most
\[
             3q(L-1)nS+nd+n+1                                \tag{4.3}
\]
dynamic real coordinates. Static moments use at most \(O((d+1)S^2)\) entries, with sparsity for local basis functions. Immutable initialization matrices remain available. Reconstructed matrices and transposes can be applied directly through their coefficient factors rather than stored dynamically. Current finite state and static arrays determine future evolution, so the system is autonomous and restartable.

The finite representation imposes a finite factorization on the *approximate* update. No low-rank assumption on the exact update appears in its justification.

## 5. Whole-trajectory spatial theorem

**Theorem.** Suppose \(X\) is Lipschitz and \(\phi\in C^{1,1}_{\rm loc}\). Fix \(q,T\), and suppose the fixed-\(q\) field system has a bounded trajectory on \([0,T]\). The algorithm in Section 4, initialized by nodal samples of the prescribed initial fields, exists through \(T\) for all sufficiently small \(a\) and obeys
\[
 \sup_{0\le t\le T}\left[
 \|U_a-U\|_\infty+\|W_{1,a}-W_1\|_F+\|w_a-w\|+|\tau_a-\tau|
 \right]\le C_Ta,\qquad U=(H,A,C).                            \tag{5.1}
\]
Use any fixed finite product norm on \(U\). Reconstructed weights, predictions, and responses have \(O(a)\) error, and backward memory has \(O(a)\) error in \(L^2(P)\). Constants are uniform over laws with common \(Y\), geometry, initialization, and reference-trajectory bounds. They are independent of sample count. For bounded \(\phi,\phi'\), Section 3 establishes the required bounded trajectory.

**Proof.** On a bounded neighborhood of the reference, each bilinear contraction in (2.4) is locally Lipschitz in field supremum norm: split a product difference into two terms and bound its integral by \(\mu(K)=1\) or \(\|\nu\|_{\rm TV}\le Y\). The clock denominator stays at least one along solutions; one may use the open neighborhood \(\tau>1/2\) for local existence. Finite compositions of locally Lipschitz \(\phi,\phi'\) and bounded matrix products make the forward and backward maps locally Lipschitz. Equation (2.6) controls the clock without loss division.

The finite equations have a local Lipschitz constant independent of \(a\): evaluation and interpolation have norm one, and (4.2) represents exact bounded integration. The reference fields \(U,h,\delta,f\) have a common finite input Lipschitz bound \(K_T\).

Let \(\Pi_a\) interpolate reference fields and leave its finite parameters unchanged. By (4.1), its field error is at most \(\sqrt pK_Ta\). Substitution of \(\Pi_aU\) in reconstruction changes hidden weights by \(O(a)\), hence network values at nodes by \(O(a)\). Interpolation changes reference \(h,\delta,f\) by \(O(a)\). Every moment source, parameter update, and clock update therefore differs by \(O(a)\) from the corresponding interpolated reference vector field. Denote this consistency bound by \(C_0a\) and the local Lipschitz constant by \(C_1\).

For the difference \(e(t)\) between the finite state and interpolated reference, \(e(0)=0\) and
\[
 e(t)\le C_0at+C_1\int_0^te(s)\,ds
       \le C_0at\,e^{C_1t}.
\]
The last estimate follows from the integrating-factor solution of the scalar majorant \(z'=C_0a+C_1z\), \(z(0)=0\). For small enough \(a\) it stays inside the chosen neighborhood, ensuring continuation through \(T\). Adding the interpolation error proves (5.1). Locally Lipschitz observation maps and (2.7) prove the remaining conclusions.

Since \(S=O(a^{-p})\), accuracy \(\epsilon\) needs \(S=O((C_T/\epsilon)^p)\). This exposes the geometric advantage and dimensional cost. Constants may grow rapidly with \(T,q,L\); the proof does not assert otherwise.

## 6. Analytic improvement

Suppose all relevant reference fields have a common holomorphic extension bounded by \(B\) on a product of Bernstein ellipses with parameter \(R>1\). Use tensor Chebyshev interpolation of degree \(m\) in each input coordinate, with norm \(\Lambda_m\le C_p(1+\log(m+1))^p\).

Here are the approximation facts needed. Under \(\xi_j=(z_j+z_j^{-1})/2\), the Cauchy integral formula bounds the Chebyshev coefficient of multi-index \(\alpha\) by \(C_pBR^{-|\alpha|_1}\). Summing the tensor tail bounds best polynomial approximation by \(C_{p,R}BR^{-m}\). The interpolation error is at most \(1+\Lambda_m\) times this bound, by writing \(g-I_mg=(g-v)-I_m(g-v)\) for any represented polynomial \(v\). The univariate logarithmic interpolation bound follows by summing cardinal trigonometric-kernel magnitudes: the sine denominator is bounded below by a constant times distance to its nearest node, so the sum is at most a constant times \(1+\sum_{j=1}^m1/j\). Tensorization multiplies these bounds.

The finite arrays (4.2) are used unchanged with the polynomial cardinal basis. On a fixed state neighborhood, interpolation enlarges network fields by at most \(\Lambda_m\). Each integrated parameter update contains at most two interpolated network fields, so the local Lipschitz constant is bounded by \(C(1+\Lambda_m)^2\). Nodal moment sources have no larger bound. Reconstruction itself is a bounded bilinear map of the stored field functions, independently of basis. The consistency defect is at most a fixed polynomial in \(1+\Lambda_m\) times \(R^{-m}\). The previous ODE comparison therefore gives, for some fixed integer \(b\),
\[
 E_m(T)\le C(1+\Lambda_m)^bR^{-m}
                    \exp\{CT(1+\Lambda_m)^2\}.               \tag{6.1}
\]
Since every fixed power of \(\log m\) is \(o(m)\), this tends to zero for fixed \(p,q,T,R,B\). For sufficiently large \(m\), it is at most \(CR^{-m/2}\). Thus asymptotically \(m=O(\log(1/\epsilon))\) and \(S=O((\log(1/\epsilon))^p)\), with potentially large thresholds. The same bootstrap establishes existence through \(T\).

Both radius and envelope are needed. Pointwise analyticity or a real \(L^2\) norm bound alone does not justify coefficient truncation.

## 7. Obstructions and scope limits

**Geometry plus norm does not force a cutoff.** On the one-dimensional input interval \(X(\xi)=\xi\), the fixed activation \(\phi(z)=\sin z\) and a one-unit first-layer weight \(j\) give \(h_j(\xi)=\sin(j\xi)\). These features are entire and bounded by one on the real interval. For uniform input measure, projection onto any fixed polynomial space tends to zero: integrating each fixed polynomial against \(\sin(j\xi)\) by parts gives \(O(1/j)\). Yet \(\|h_j\|_{L^2(\mu)}^2\to1/2\). A degree cutoff depending only on intrinsic dimension and real norm therefore fails. Uniform weight/derivative bounds or a common complex envelope supply the missing information. This is a uniformity counterexample, not a failure of the stated theorem.

**Direct smoothing of arbitrary labels fails.** If one instead requires \(B(\xi,y(\xi))\) itself to lie near a fixed smooth-input space, \(-y(\xi)C(\xi)\) retains arbitrary \(L^2\) oscillations. The exact affine representation avoids this obstruction. It does not reconstruct an unknown pointwise label function from finitely many moments; labels remain the explicit argument in (2.1).

**No all-time cutoff is proved.** The regularity and stability bounds depend on \(T\). One fixed resolution valid for all times would require additional uniform derivative control, dissipativity, or a weaker observable topology.

**Spatial and temporal limits are separate.** This proves spatial convergence at every fixed \(q\). The \(q\)-dependent bound (3.5) is neither a temporal-tail estimate nor uniform-in-\(q\) stability. To approximate the original network, first select \(q\) by a valid temporal theorem on the desired horizon, then select the spatial resolution for that \(q\). Spatial convergence cannot identify the temporal limit.

**No width-uniform rank conclusion.** Finite coefficients imply a finite factorization of the approximate update, but the coefficient count may grow with width-dependent regularity, depth, and accuracy. No uniform low rank of exact feature matrices is claimed.

## 8. Claim ledger

| Claim | Status | Condition or remaining issue |
|---|---|---|
| \(B=A-yC\); dependence only on \((\mu,\nu,m_2)\) | Exact | Common weights/clock and zero initial backward memory |
| Rough \(L^2\) labels admit smooth coefficient fields | Proved | Smoothness is in \(A,C,H\), not the labels |
| Finite autonomous algorithm with static coefficients | Constructed | Initial data moment arrays are provided/computed |
| Whole-trajectory spatial convergence at fixed \(q,T\) | Proved | \(C^{1,1}_{\rm loc}\) activation; bounded reference |
| Bounded fixed-\(q\) reference for bounded \(\phi,\phi'\) | Proved | Bounds can grow with \(q,T\) |
| Spectral spatial compression | Conditional theorem | Common complex radius and envelope |
| Cutoff from geometry and real norm alone | Falsified | Fixed sine-activation family |
| Original-network limit as \(q\to\infty\) | Separate obligation | Temporal error and stability |
| One finite closure uniformly for all time | Open here | No uniform regularity/stability bound |

The established bridge is from a sample-indexed response-memory table to finitely many input-field coefficients, with nonlinear dynamics and noisy labels preserved. The independent temporal approximation controls the remaining identification with the original network.
