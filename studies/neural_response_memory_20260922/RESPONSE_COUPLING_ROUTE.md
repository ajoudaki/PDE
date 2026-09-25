# Response coupling: exact local construction and its limits

Scoped theory-only route, 2026-09-22. Scientific inputs: the supervisor's canonical network and, in the final section, the supervisor's proposed Legendre history construction. No other study or external scientific source was consulted. No experiment was run.

## 1. Strongest result

At a specified interpolating equilibrium of the canonical dense network, its complete **linearized** forward and backward neuron response admits an autonomous finite ODE with a positive semidefinite generator. It can be organized as two response blocks coupled by one small rectangular matrix. Each block has dimension at most the number of training samples. Its coefficients are derivatives of the actual dense equilibrium, not coefficients fitted to the future trajectory.

This gives a rigorous local response model with relaxation and plateau offsets. It is a frozen tangent model, however, and therefore does not satisfy a requirement excluding frozen representations of full nonlinear feature learning. It also requires an equilibrium supplied in advance. The theorem is a restricted construction and a diagnostic of what additional claims need proof, not a solution of general dense-training compression.

## 2. Canonical model and whitening

Use samples indexed by \(\mu=1,\ldots,m\), positive loss weights \(\rho_\mu\), and two width-\(n\) hidden layers:

\[
h^\mu=\tanh(W_1x^\mu/\sqrt d),\quad
z^\mu=W_2h^\mu,\quad H^\mu=\tanh z^\mu,
\]
\[
f^\mu=c^\top H^\mu/n,\quad
\delta^\mu=c\odot(1-(H^\mu)^2),\quad q^\mu=W_2^\top\delta^\mu,
\qquad L=\sum_\mu\rho_\mu(f^\mu-y^\mu)^2.
\]

Let \(\theta=(W_1,W_2,c)\), flattening matrices only for linear algebra, and let the constant gradient-flow mobility be
\[
D=\operatorname{diag}(nI_{W_1},I_{W_2},nI_c),\qquad
\dot\theta=-D\nabla L(\theta).
\]
Fix \(\theta_*\) satisfying \(f^\mu(\theta_*)=y^\mu\) for every sample. Every unmarked network factor below is evaluated at this equilibrium. Write \(J_{\mu,:}=D_\theta f^\mu(\theta_*)\), \(R=\operatorname{diag}(\rho_\mu)\), and
\[
B=\sqrt2 R^{1/2}JD^{1/2},\qquad A=B^\top B.
\]

For the whitened infinitesimal displacement \(\eta=D^{-1/2}\Delta\theta\), the exact variational equation at the equilibrium is
\[
\dot\eta=-A\eta.
\]
Indeed differentiating the loss twice gives
\[
\nabla^2L=2J^\top RJ+2\sum_\mu\rho_\mu(f^\mu-y^\mu)\nabla^2f^\mu,
\]
whose second term vanishes at interpolation. Whitening converts the linearized generator to the symmetric nonnegative matrix \(A\).

The gradient entries determining all coefficients are
\[
\partial_{c_j}f^\mu=H_j^\mu/n,\quad
\partial_{(W_2)_{ji}}f^\mu=\delta_j^\mu h_i^\mu/n,\quad
\partial_{(W_1)_{ia}}f^\mu=q_i^\mu(1-(h_i^\mu)^2)x_a^\mu/(n\sqrt d).
\]

## 3. A literal small coupling matrix between two response blocks

Partition whitened parameters into block 1, consisting of \(W_1\), and block 2, consisting of \((W_2,c)\). Thus \(B=[B_1\ B_2]\). Including the readout in the second block is necessary because it is trained in the canonical flow.

For each \(\ell=1,2\), let \(V_\ell\) be any orthonormal basis of \(\operatorname{range}B_\ell^\top\), with \(r_\ell=\operatorname{rank}B_\ell\le m\) columns. Decompose
\[
\eta_\ell=V_\ell a_\ell+\eta_\ell^0,\qquad
\eta_\ell^0\in\ker B_\ell.
\]
Define \(T_\ell=B_\ell V_\ell\), \(S_\ell=T_\ell^\top T_\ell\), and the small interblock matrix
\[
M=T_1^\top T_2\in\mathbb R^{r_1\times r_2}.
\]
Then the exact active response dynamics are
\[
\dot a_1=-S_1a_1-Ma_2,\qquad
\dot a_2=-M^\top a_1-S_2a_2,\qquad
\dot\eta_\ell^0=0.
\]
All rates and couplings are fixed by the equilibrium and dataset. Neither \(M\) alone nor a freely chosen pair \((S_1,S_2)\) determines a canonically valid model: their joint Gram structure matters.

**Exactness and stability.** The full linear equation gives
\(\dot\eta_\ell=-B_\ell^\top(B_1\eta_1+B_2\eta_2)\). Its right side lies in \(\operatorname{range}V_\ell\), so the orthogonal component \(\eta_\ell^0\) stays constant. Multiplying by \(V_\ell^\top\) yields the displayed equations. Their joint generator is
\[
\mathcal A=
\begin{pmatrix}S_1&M\\M^\top&S_2\end{pmatrix}
=[T_1\ T_2]^\top[T_1\ T_2]\succeq0.
\]
Consequently
\[
\frac{d}{dt}\frac{\|a_1\|^2+\|a_2\|^2}{2}
=-\|T_1a_1+T_2a_2\|^2\le0.
\]
Diagonalizing this real symmetric matrix yields constant modes at eigenvalue zero and exponential modes \(e^{-\lambda t}\) for positive \(\lambda\). This is an all-time result for the linearized equation. Its rates cannot be chosen independently to manufacture desired plateaus while retaining the original response.

## 4. Forward and backward states for every neuron

Let \(\mathcal O(\theta)\) concatenate, for every training sample and every neuron, \(h,z,H,c,\delta,q\). Set
\[
C=D_\theta\mathcal O(\theta_*)D^{1/2}=[C_1\ C_2],\qquad
E_\ell=C_\ell V_\ell.
\]
These loadings are obtained by differentiating the actual network, including both terms in each product:
\[
\Delta h=(1-h^2)\odot(\Delta W_1x/\sqrt d),
\]
\[
\Delta z=\Delta W_2h+W_2\Delta h,\qquad
\Delta H=(1-H^2)\odot\Delta z,
\]
\[
\Delta\delta=(1-H^2)\odot\Delta c
-2c\odot H\odot(1-H^2)\odot\Delta z,
\]
\[
\Delta q=\Delta W_2^\top\delta+W_2^\top\Delta\delta.
\]
Thus each neuron retains its own forward and backward observable entries; no term in the transpose product rule is discarded. With
\(o^0=C_1\eta_1^0+C_2\eta_2^0\), its entire linear response is
\[
o(t)=o^0+E_1a_1(t)+E_2a_2(t).
\]
Equivalently these per-neuron entries can be stored as explicit ODE states:
\[
\dot o=-E_1(S_1a_1+Ma_2)-E_2(M^\top a_1+S_2a_2),
\quad o(0)=C\eta(0).
\]
The equations are autonomous and restartable on this consistency manifold. The extra observable states are redundant readouts of the same global modes, not independent nonlinear degrees of freedom. A requirement for dynamically changing neuron-specific response functions is therefore stronger than this theorem.

Online one can discard \(V_\ell\) after forming \(E_\ell,S_\ell,M\) and initializing \(a_\ell,o^0\). For \(O(nm)\) per-sample neuronal observables this needs \(O(nm^2)\) loading storage, plus \(O(m^2)\) coupling storage, rather than a dynamic \(n\times n\) weight matrix. Offline coefficient construction still uses the dense equilibrium, may be expensive, and is not compression of the process that found it. Width independence requires fixed sample count and does not establish bounds uniform in width.

## 5. Minimal sample-space realization and plateau interpretation

The response also has an exact realization with at most \(m\) active coordinates:
\[
w=B\eta,\quad K=BB^\top,\quad G=CB^\top,
\qquad \dot w=-Kw,\quad\dot o=-Gw.
\]
Its explicit kernel is
\[
K_{\mu\nu}=2\sqrt{\rho_\mu\rho_\nu}
\left[
\frac{x^\mu\cdot x^\nu}{nd}
\sum_i q_i^\mu q_i^\nu(1-(h_i^\mu)^2)(1-(h_i^\nu)^2)
+\frac{(\delta^\mu\cdot\delta^\nu)(h^\mu\cdot h^\nu)}{n^2}
+\frac{H^\mu\cdot H^\nu}{n}
\right].
\]
Here \(K\) couples sample responses; it is not a learned interlayer weight matrix. With \(K^\dagger\) denoting the pseudoinverse,
\[
o(t)=o(0)-GK^\dagger(I-e^{-Kt})w(0).
\]
There is no secular zero-mode term because \(w(0)=B\eta(0)\in\operatorname{range}K\). In particular the sample-space zero modes carry no compatible perturbation. The plateau is instead
\[
o(\infty)=C P_{\ker B}\eta(0),
\]
in addition to the equilibrium baseline \(\mathcal O(\theta_*)\). This identity follows by the orthogonal decomposition into \(\ker B\) and \(\operatorname{range}B^\top\); the latter components decay.

If an input \(u\) is added to the *linear response* equation as \(\dot\eta=-A\eta+B^\top u\), the transfer function to \(o=C\eta\) is
\[
C(sI+A)^{-1}B^\top=G(sI+K)^{-1}.
\]
This is a concrete rational response embedding with poles at nonpositive real rates. A collocated output \(B\eta\) has nonnegative spectral weights; arbitrary neuron forward/backward observables need not. Stable global modes therefore do not imply monotonicity or absence of overshoot in each neuron observable.

## 6. Validity for the nonlinear network

The preceding exactness concerns the variational equation, not the nonlinear training trajectory. Write the actual whitened displacement as \(\xi=D^{-1/2}(\theta-\theta_*)\). Smoothness of the finite tanh network gives, on a sufficiently small ball,
\[
\dot\xi=-A\xi+N(\xi),\qquad\|N(\xi)\|\le C_N\|\xi\|^2.
\]
For \(\|\xi(0)\|\le\varepsilon\), fix \(T\), require \(2\varepsilon\) to lie inside that ball and \(2C_N\varepsilon T\le1\). Duhamel's formula and \(\|e^{-At}\|\le1\) imply by a continuation argument
\[
\sup_{t\le T}\|\xi(t)\|\le2\varepsilon,
\qquad
\sup_{t\le T}\|\xi(t)-e^{-At}\xi(0)\|
\le4C_NT\varepsilon^2.
\]
A second-order Taylor bound for \(\mathcal O\) then gives observable error at most
\(4(\|C\|C_NT+C_{\mathcal O})\varepsilon^2\), where \(C_{\mathcal O}\) bounds its quadratic remainder in whitened coordinates. These constants can depend on width and on the dense equilibrium. This is a fixed-horizon local theorem, with no width-uniform or all-time nonlinear claim.

Away from interpolation the residual Hessian term need not be positive semidefinite. Along a nonstationary training trajectory the generator also changes with time and need not preserve a fixed finite response subspace. Replacing it by a constant stable matrix changes the dynamics unless a separate controlled approximation proves otherwise.

### Exact canonical counterexample to an all-time tangent plateau

Take \(n=d=m=1\), \(x=1,y=0,\rho=1\), denote \((W_1,W_2,c)=(w,a,c)\), and use the interpolating equilibrium \((0,1,0)\). Here
\(f=c\tanh(a\tanh w)\) and \(J_*=0\), so \(A=0\): every tangent perturbation is stationary.

Initialize the actual nonlinear model at \((\varepsilon,1,\varepsilon)\), with \(0<\sinh\varepsilon<1\). All three coordinates stay positive at finite times and decrease. Writing \(h=\tanh w\), \(H=\tanh(ah)\), their exact equations are
\[
\dot w=-2c^2Ha(1-H^2)(1-h^2),\quad
\dot a=-2c^2H(1-H^2)h,\quad
\dot c=-2cH^2.
\]
Direct differentiation shows
\[
a^2-\sinh^2w=1-\sinh^2\varepsilon>0.
\]
Thus \(a\) stays bounded away from zero. Monotonic bounded coordinates have limits. If both \(w\) and \(c\) had positive limits, \(\dot c=-2cH^2\) would approach a strictly negative number, a contradiction. Hence \(w\to0\) or \(c\to0\). At least one of the forward state \(h\) and the readout state \(c\) changes by order \(\varepsilon\), whereas the tangent model predicts it constant. The initial nonzero \(\delta=c(1-H^2)\) also need not retain its tangent plateau. Stable zero linear modes therefore cannot establish all-time nonlinear plateaus, even in this canonical architecture.

## 7. Audit of the supervisor-supplied Legendre history construction

This section audits a new construction supplied directly by the supervisor during this route; it is not an independent discovery or a source imported from another study.

Let \(F(s)\) and \(G(s)\) be square-integrable histories taking values in real Hilbert neuron spaces, with their normalization fixed. Let \(\ell_k(u)=\sqrt{2k+1}P_k(2u-1)\) be the orthonormal shifted Legendre functions on \([0,1]\), and set
\[
F_k(t)=\int_0^1\ell_k(u)F(tu)\,du,\qquad
G_k(t)=\int_0^1\ell_k(u)G(tu)\,du.
\]
For a kernel whose increment is \(-2\int_0^tF(s)\otimes G(s)\,ds\), completeness and continuity of the tensor integral give
\[
\Delta W(t)=-2t\sum_{k\ge0}F_k(t)\otimes G_k(t).
\]
The series converges in Hilbert--Schmidt norm because
\(\sum_k\|F_k\|\|G_k\|\le\|F(t\cdot)\|_{L^2}\|G(t\cdot)\|_{L^2}\).

Retain \(k=0,\ldots,P-1\), \(P\ge1\), and denote their orthogonal projection by \(P_P\). Cross terms vanish by orthogonality, leaving exactly
\[
\Delta W-\Delta W_P
=-2t\int_0^1[(I-P_P)F(t\cdot)](u)\otimes[(I-P_P)G(t\cdot)](u)\,du.
\]
The norm of a rank-one tensor is the product of the vector norms. The triangle inequality and scalar Cauchy--Schwarz therefore give
\[
\|\Delta W-\Delta W_P\|_{\rm HS}
\le2t\|(I-P_P)F(t\cdot)\|_{L^2}\|(I-P_P)G(t\cdot)\|_{L^2}.
\]

For continuously differentiable histories, integration by parts in
\(-[u(1-u)\ell_k']'=k(k+1)\ell_k\), followed by orthogonal projection in the weighted derivative norm, gives
\[
\sum_{k\ge1}k(k+1)\|F_k(t)\|^2
\le\int_0^1u(1-u)\|\partial_uF(tu)\|^2\,du=:C_F(t)^2.
\]
The boundary term vanishes because \(u(1-u)=0\) at both ends; the finite partial-sum identity and nonnegativity of the remaining derivative norm suffice, so equality of the full Sobolev expansion is unnecessary. It follows that
\[
\|(I-P_P)F(t\cdot)\|_{L^2}\le\frac{C_F(t)}{\sqrt{P(P+1)}},\qquad
\|\Delta W-\Delta W_P\|_{\rm HS}
\le\frac{2t C_F(t)C_G(t)}{P(P+1)}.
\]
The derivative is with respect to \(u\): \(\partial_uF(tu)=t\dot F(tu)\). Thus a time-uniform bound on \(\dot F\) alone gives \(C_F(t)\le t\sup_{s\le t}\|\dot F(s)\|/\sqrt6\); the displayed estimate is not automatically uniform at long times.

These moments satisfy exact finite triangular driven ODEs. Put \(\beta_k=\sqrt{2k+1}\). Differentiating and integrating by parts yields
\[
t\dot F_k=\beta_k F(t)-(k+1)F_k-\beta_k\sum_{j<k}\beta_jF_j,
\]
and the identical equation with \(F\) replaced by \(G\). The coefficient identity used here is
\(\ell_k+u\ell_k'=(k+1)\ell_k+\beta_k\sum_{j<k}\beta_j\ell_j\).
The compatible initial values are \(F_0(0)=F(0)\), \(F_k(0)=0\) for \(k>0\); the integral definition resolves the regular-singular equation at zero. In log-time \(\tau=\log t\), the homogeneous matrix is triangular with strictly negative rates \(-1,\ldots,-P\). Under constant forcing its equilibrium is \((F,0,\ldots,0)\). Hence these are concrete per-neuron relaxation filters, with algebraic relaxation in physical time, not time-Taylor coefficients.

With the supervisor's normalized rank-one convention \(v\otimes_n w=vw^\top/n\), the canonical equation is directly \(\dot W_2=-2\rho r\delta\otimes_n h\); for unit sample weight the coefficient \(-2\) in the history identity is correct without rescaling the matrix. The Hilbert--Schmidt norm of this rank-one operator is \(\|v\|_n\|w\|_n\), where \(\|v\|_n^2=\sum_i v_i^2/n\). All the displayed tail arguments therefore apply with normalized neuron norms and this operator convention.

The proven error evaluates moments on the exact dense history. A self-consistent closed surrogate changes the driving \(F,G\), and requires an additional stability and consistency argument. The initial operator \(W_2(0)\) and its transpose remain present in forward and backward actions. Moment-filter stability by itself proves neither a plateau of physical neuron states nor width-independent compression of those initial dense actions.

The supervisor subsequently supplied an activity-clock refinement: \(a(t)=a_0+\int_0^t2R(s)ds\), \(a_0>0\), \(F=(r/R)\delta\), and \(G=h\), with constant dummy history on \([0,a_0]\). For a single sample with unit weight, \(R\ge0\) and \(R=0\Rightarrow r=0\), change of variables gives exactly
\[
W_2(t)-W_2(0)
=-\left[a(t)\sum_{k\ge0}F_k(a(t))\otimes_nG_k(a(t))
-a_0F_{\rm init}\otimes_nG_{\rm init}\right].
\]
The physical-time encoder equations follow by multiplying the moment equation by \(\dot a/a=2R/a\). In the \(F\) source this gives \(2RF=2r\delta\), so the implemented equation need not divide by \(R\). When \(R=0\), every encoder derivative is zero. This avoids continued history aging after zero residual. It provides an exact encoder plateau when the drive stops; it does not prove that the coupled network reaches zero residual or that a finite self-consistent truncation tracks dense training. The same tail proof applies in the normalized activity coordinate, with the appropriate derivative norm and prefactor \(a\), and dummy-history regularity must be included in its assumptions.

## 8. Claim status

- Proved: exact local linear response; the two-block Gram coupling; positive semidefinite generator; fixed-horizon second-order nonlinear accuracy for sufficiently small perturbations; the stated Legendre tail estimate and exact moment ODE.
- Disproved for this witness: inferring all-time nonlinear plateaus from zero eigenvalues of the equilibrium Hessian.
- Not established: a coefficient construction from ordinary random initialization giving a small autonomous model of full nonlinear training; a width-uniform number of necessary modes; closed stable finite dynamics retaining the actions of an arbitrary dense initial matrix.
- Highest-leverage unresolved bridge: for the history construction, control the error generated by self-consistent approximate histories and the omitted initial-operator action, in norms that control both forward and backward neuron states.
