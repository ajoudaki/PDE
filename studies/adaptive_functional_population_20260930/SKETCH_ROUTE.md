# Fixed random sketches for compact-time nonlinear feature learning

Scoped derivation, 2026-09-30. This route used only the supervisor's prompt and the required research/proof skills. It did not inspect other studies, retrieve scientific sources, or run training. The complete architecture and activation assumptions were not supplied, so the normalized derivative bounds below are explicit hypotheses, not claims already verified for the canonical deep network.

The useful positive result is a compact-time sampling theorem with no covering of parameter space. It gives an original-sample-count-independent coreset size proportional to the inverse square of the desired error, provided normalized gradient and Hessian bounds hold. A separate, genuinely functional Galerkin theorem also has an inverse-square coefficient count, but requires a fixed-dictionary second-moment bound and a computable projected vector field. Bounded Hilbert norms alone do not supply that assumption. Neither theorem, by itself, settles the desired population-field encoding for the canonical deep network.

## 1. Contract and notation

The target is the same nonlinear network and squared-loss flow

\[
\dot\theta=-2D\,\mathbb E[(f_\theta(X)-Y)\nabla_\theta f_\theta(X)],
\qquad D=\operatorname{diag}(n,1,\ldots,1,n),
\]

with the same realized Gaussian initialization, including the exact matrices \(W_0\). No lazy-training, fixed-feature, low-degree, or low-rank replacement is made in the first theorem. The comparison is on a fixed finite physical-time interval \([0,T]\). The initialization is conditioned on throughout and is independent of the fresh sampling used by the approximation. More generally it is enough that the reference dynamics are deterministic conditional on all retained inputs and independent of the fresh sketch.

Write \(N\) for the original data count, if the target law is empirical, and \(s\) for the number of fresh quadrature samples. Thus \(P\) can be either a population law or the fixed empirical law \(P_N\). Sampling from \(P_N\) means sampling with replacement and retaining multiplicity weights. A bound independent of \(N\) is not automatically independent of width \(n\), input dimension \(d\), depth, or memory order \(q\).

Use the whitened parameter

\[
u=D^{-1/2}\theta,\qquad f(u,x)=f_{D^{1/2}u}(x),\qquad
g(u,x)=\nabla_u f(u,x)=D^{1/2}\nabla_\theta f_\theta(x).
\]

The parameter norm is therefore \(\|\theta\|_{D^{-1}}=\|D^{-1/2}\theta\|\). In this norm,

\[
\dot u=F(u)=P\,b(u,Z),\qquad
b(u,z)=-2(f(u,x)-y)g(u,x).
\]

The sketch flow uses the same initial parameter and the same architecture:

\[
\dot u_s=F_s(u_s)=\frac1s\sum_{i=1}^s b(u_s,Z_i),\qquad
u_s(0)=u(0),\qquad Z_i\overset{\rm iid}{\sim}P.
\]

This is an autonomous empirical gradient flow. Its coefficients and initialization use no future reference trajectory.

## 2. A fixed-reference source estimate replaces parameter-space covering

Assume the population trajectory exists on \([0,T]\), \(L_0=P(f(u(0),X)-Y)^2<\infty\), and the derivatives needed below exist. On the union of radius-\(R\) balls around the population trajectory suppose

\[
\|g(v,x)\|\le G,\qquad
\|\nabla_u^2 f(v,x)\|_{\rm op}\le H
\tag{2.1}
\]

for \(P_X\)-almost every \(x\), with deterministic bounds after conditioning on the retained inputs. These are normalized derivative bounds: an unnormalized Euclidean bound on \(\nabla_\theta f\) is not a substitute. For uniform prediction on an external test set, (2.1) must additionally hold there.

Let \(L(t)=P(f(u(t),X)-Y)^2\). The exact loss identity is

\[
\frac{dL}{dt}=-\|\dot u\|^2,
\qquad
\int_0^T\|\dot u\|^2dt\le L_0,
\qquad
\int_0^T\|\dot u\|dt\le\sqrt{T L_0}.
\tag{2.2}
\]

The last bound is Cauchy--Schwarz. Consequently the residual along the reference curve has the pointwise envelope

\[
|r_t(z)|\le |r_0(z)|+G\sqrt{T L_0}.
\tag{2.3}
\]

Only \(Y\in L^2(P)\), together with \(f(u(0),\cdot)\in L^2(P_X)\), is needed for the residual moments in this argument.

For \(v\) in the radius-\(R\) ball around \(u(t)\), subtract the two sample vector fields using

\[
r(v)g(v)-r_tg(u(t))
=[r(v)-r_t]g(v)+r_t[g(v)-g(u(t))].
\]

Integrating the gradient or Hessian on the line segment in that ball gives

\[
\|b(v,z)-b(u(t),z)\|
\le[2G^2+2H|r_t(z)|]\,\|v-u(t)\|.
\tag{2.4}
\]

Thus, on the event \(P_s|r_0|\le2\sqrt{L_0}\), the empirical drift has the needed comparison bound against the reference curve with constant

\[
\Lambda_*=2G^2+2HG\sqrt{T L_0}+4H\sqrt{L_0}.
\tag{2.5}
\]

This is a one-sided comparison against the reference trajectory; a uniform approximation theorem for all parameter values is unnecessary. Since \(P|r_0|\le\sqrt{L_0}\) and \(\operatorname{Var}(|r_0|)\le L_0\), Chebyshev's inequality gives

\[
\Pr\{P_s|r_0|>2\sqrt{L_0}\}\le 1/s.
\tag{2.6}
\]

The case \(L_0=0\) is separate and exact: the population residual and all sampled residuals are zero almost surely, so both flows remain at the same initial parameter.

Define the source error solely on the population trajectory,

\[
\eta_s(t)=(P_s-P)b(u(t),Z).
\]

Conditionally on the retained inputs, this is the average of independent, centered vectors. Expanding its squared norm cancels all cross terms, hence

\[
\begin{aligned}
\mathbb E_{\rm sketch}\|\eta_s(t)\|^2
&=\frac1s\left(P\|b(u(t),Z)\|^2-\|F(u(t))\|^2\right)\\
&\le\frac{4G^2}{s}L(t).
\end{aligned}
\tag{2.7}
\]

Tonelli's theorem applies to the nonnegative squared integrand. If \(Q_s=\int_0^T\|\eta_s(t)\|dt\), another Cauchy--Schwarz inequality yields

\[
\mathbb E_{\rm sketch}Q_s^2
\le \frac{4G^2T}{s}\int_0^T L(t)dt.
\tag{2.8}
\]

For \(0<\delta<1\), with probability at least \(1-\delta/2\),

\[
Q_s\le
\sqrt{\frac{8G^2T}{s\delta}\int_0^T L(t)dt}.
\tag{2.9}
\]

No time grid, entropy of a parameter ball, or union bound over trajectories appears here. The empirical trajectory is random, but the source is evaluated on the independent reference trajectory.

Before the first exit from its radius-\(R\) tube, subtracting the two ODEs gives

\[
\|u_s(t)-u(t)\|
\le\int_0^t\Lambda_*\|u_s(a)-u(a)\|da
+\int_0^t\|\eta_s(a)\|da.
\]

The integral Gronwall inequality used here says: if a continuous nonnegative function satisfies \(e(t)\le q(t)+\Lambda\int_0^t e(a)da\) with nondecreasing \(q\), then \(e(t)\le e^{\Lambda t}q(t)\). To check it, insert \(q(t)\) as a constant upper bound for \(q(a)\), iterate the integral inequality, and sum the exponential series. Therefore

\[
\sup_{t\le T}\|u_s(t)-u(t)\|
\le e^{\Lambda_* T}
\sqrt{\frac{8G^2T}{s\delta}\int_0^T L(t)dt}
\tag{2.10}
\]

with probability at least \(1-\delta\), provided \(s\ge2/\delta\) and the displayed bound is strictly below \(R\). Indeed, the event in (2.6) fails with probability at most \(\delta/2\), and (2.9) supplies the other half. On their intersection, a first exit would contradict the strict bound; local well-posedness then continues the empirical solution through \([0,T]\). In the finite-dimensional parameter setting a bounded tube also prevents finite-time escape of the solution.

In particular, for \(0<\varepsilon<R\), it is sufficient to take

\[
s\ge\max\left\{\frac2\delta,
\frac{8G^2T\left(\int_0^T L(t)dt\right)e^{2\Lambda_*T}}
{\delta\varepsilon^2}\right\},
\tag{2.11}
\]

with a harmless strict increase if needed for the tube bootstrap. Replacing \(\int_0^T L\) by \(TL_0\) makes this bound available from the initial loss and the derivative bounds, without observing the future curve.

This proves an inverse-square sample rate at fixed confidence. The \(\delta^{-1}\) factor is a second-moment guarantee, appropriate when only a label \(L^2\) assumption is available. A logarithmic confidence dependence needs stronger tail assumptions or a different robust estimator; it is not proved here.

## 3. What the sampling theorem does and does not buy

For predictions under the same gradient bound,

\[
\sup_{t\le T}\|f(u_s(t),\cdot)-f(u(t),\cdot)\|_{L^2(P_X)}
\le G\sup_{t\le T}\|u_s(t)-u(t)\|.
\tag{3.1}
\]

The same right side bounds the supremum over a test set if (2.1)'s gradient bound holds uniformly on that set. It does not follow from a gradient bound only in \(L^2(P_X)\). Population loss is controlled because the triangle inequality gives

\[
|\sqrt{L(u_s(t))}-\sqrt{L(u(t))}|
\le\|f(u_s(t),\cdot)-f(u(t),\cdot)\|_{L^2(P_X)}.
\]

Analogous hidden-feature or response-field conclusions require their own normalized parameter-to-field Lipschitz bounds. Output accuracy alone is not a proof of internal feature accuracy.

The theorem has no explicit \(d\) or \(N\) in its sample rate. That is a useful absence of a covering-number curse, conditional on \(G,H,L_0\) being controlled independently of those quantities. It is not a proof that those constants are dimension-free for an unspecified deep architecture. In particular:

* Products of normalized layer operator norms and activation derivative bounds can grow rapidly with depth. The exponential \(e^{2\Lambda_*T}\) can also be large.
* A Gaussian initialization does not automatically establish the required uniform Hessian bound on an entire finite-time tube.
* For unbounded inputs, a uniform \(G\) need not exist. Replacing it by an \(L^2\) bound alone is invalid: (2.7) needs \(P[r_t^2\|g_t\|^2]<\infty\), which does not follow from separate second moments of \(r_t\) and \(g_t\).
* A nonsmooth activation requires a separate well-posedness and stability argument. The twice differentiable argument above cannot simply be asserted for ReLU.

The state in this theorem remains the full trainable parameter \(\theta_s\). It compresses the measure used to evaluate the drift. It does not yet compress the trained parameter state into a width-independent set of functional coefficients. Sampling \(s\) actual data points also retains \(sd\) input coordinates and \(s\) labels. Consequently this is a coreset result, not by itself a functional population encoding.

For a finite target dataset, the conclusion compares training on a random weighted coreset to training on that particular dataset. For a population target, it compares empirical training to population training. These are distinct targets, although the same conditional proof applies.

## 4. A conditional theorem for an actual functional basis

Here is the additional theorem that would be relevant to a population-field code. Let \(\mathcal H\) be the Hilbert space of all retained functional fields, with a norm specified to control the required observables. Let \(U_0\) be the exactly retained base state, which may depend on \(W_0\), and suppose

\[
\dot U=\mathcal F(U),\qquad U(0)=U_0.
\]

Assume local well-posedness and a Lipschitz bound \(\Lambda\) for \(\mathcal F\) in the needed tube. Let \(\mu\) be a probability distribution chosen from the permitted initial inputs, without the future trajectory, and let \(\phi_\omega\in\mathcal H\) be evaluable dictionary atoms. Suppose that along the reference curve

\[
\mathcal F(U(t))=
\mathbb E_{\omega\sim\mu}[a(U(t),\omega)\phi_\omega],
\qquad
\mathbb E_\mu\|a(U(t),\omega)\phi_\omega\|_{\mathcal H}^2
\le M(t)^2.
\tag{4.1}
\]

For a uniform constructive theorem, \(\mu\), the atoms, and an upper bound on \(\int_0^T M^2\) must be available a priori for the claimed problem class. A posteriori existence of some trajectory-specific \(\mu\) does not meet this requirement.

Draw \(K\) atoms once, independently of the reference solution, and let \(P_K\) be the orthogonal projection onto their span. Define the autonomous approximation

\[
\dot U_K=P_K\mathcal F(U_K),\qquad U_K(0)=U_0,
\qquad U_K-U_0\in\operatorname{span}\{\phi_{\omega_i}\}_{i=1}^K.
\tag{4.2}
\]

For each fixed reference time, the Monte Carlo average in (4.1) belongs to the sampled span. Orthogonal projection is the best approximation in a Hilbert subspace, so

\[
\begin{aligned}
\mathbb E\|(I-P_K)\mathcal F(U(t))\|^2
&\le\mathbb E\left\|\mathcal F(U(t))-
\frac1K\sum_{i=1}^K a(U(t),\omega_i)\phi_{\omega_i}\right\|^2\\
&\le\frac{M(t)^2}{K}.
\end{aligned}
\tag{4.3}
\]

The coefficients in this Monte Carlo expression are only a proof witness for the projection residual. They are not inserted into the surrogate dynamics and therefore do not constitute future-trajectory playback.

Subtracting (4.2) from the reference ODE, using the contraction property of \(P_K\), integrating the source estimate as in Section 2, and bootstrapping the tube yields

\[
\Pr\left\{\sup_{t\le T}\|U_K(t)-U(t)\|_{\mathcal H}
\le e^{\Lambda T}
\sqrt{\frac{T}{K\delta}\int_0^T M(t)^2dt}\right\}
\ge1-\delta,
\tag{4.4}
\]

provided the right side is below the tube radius. This is a genuine \(K=O(\varepsilon^{-2})\) scalar-coefficient theorem under (4.1). It uses neither low polynomial degree nor a covering of the ambient parameter space. It allows strong nonlinear motion.

To see precisely what is stored, write \(U_K=U_0+\sum_i c_i\phi_{\omega_i}\). With Gram matrix \(\Gamma_{ij}=\langle\phi_{\omega_i},\phi_{\omega_j}\rangle\), a coordinate equation is

\[
\dot c=\Gamma^\dagger b(c),\qquad
b_i(c)=\left\langle\phi_{\omega_i},
\mathcal F\left(U_0+\sum_j c_j\phi_{\omega_j}\right)\right\rangle,
\qquad c(0)=0.
\tag{4.5}
\]

The pseudoinverse removes any redundancy in the sampled dictionary. The forcing vector belongs to the range of \(\Gamma\), since every linear relation among the atoms is orthogonal to every element of \(\mathcal H\). Thus (4.5) realizes the unique projected derivative. An orthonormal basis for the same span gives an equivalent equation.

The positive theorem has two decisive conditions that are not automatic:

1. The fixed-dictionary representation (4.1) must hold with an acceptable, width- and dimension-controlled bound in a norm that controls the intended fields. A bound on \(\|\mathcal F(U)\|_{\mathcal H}\) alone is insufficient.
2. Every atom, Gram entry, and right side in (4.5) must have a permitted finite description and be computable from the finite state and fixed retained inputs. If (4.5) merely invokes unrestricted integration against an unencoded population law, it is a finite-state equation with a population oracle, not a fully encoded executable system. Approximating those integrals introduces another sampling or representation error that must be proved separately.

The retained atom descriptors and any Gram matrix count toward storage. Even if there are only \(K\) evolving coefficients, a dense Gram matrix has \(K^2\) entries unless structure or recomputation removes that storage. A dictionary atom that is itself an arbitrary inaccessible function is not a compact coefficient.

## 5. Why a norm or changing variation measure is not enough

A familiar favorable atomic situation is \(\|\phi_\omega\|\le1\) and a fixed known measure for which the coefficient density has bounded second moment. Then (4.1) has a dimension-free bound directly. This is a genuine structural approximation class.

It is weaker to say that each source separately has atomic variation at most \(V\): the optimal sampling distribution can change with the source. For example, take an orthonormal dictionary \(\phi_j=e_j\). Every source \(e_j\) has atomic variation one. For any single fixed probability distribution \(p_j\) on infinitely many atoms, representing \(e_j\) by unbiased sampling has second moment at least \(1/p_j\); these moments are unbounded as \(j\) varies. Thus a uniform variation bound with state-dependent optimal measures does not establish (4.1) for a single preselected sketch. A priori domination of the evolving coefficient measures, or a proved adaptive atom-selection mechanism, is needed.

A finite-dimensional linear sketch cannot recover every bounded field in an infinite-dimensional Hilbert space. For any rank-\(K\) map \(S:\mathcal H\to\mathbb R^K\), choose a unit vector \(v\in\ker S\). Both \(v\) and \(-v\) have code zero. For any decoder value \(w\) at zero,

\[
2=\|v-(-v)\|\le\|v-w\|+\|-v-w\|,
\]

so one of the reconstruction errors is at least one. The same argument applies to a fixed \(K\)-dimensional basis. It does not rule out compressibility of a smaller reachable class.

There is also no distribution-free guarantee for a random rank-\(K\) projection on the entire unit ball. In any \(D\)-dimensional orthonormal family,

\[
\sum_{j=1}^D\mathbb E\|P_K e_j\|^2\le K.
\]

Hence some \(e_j\) has expected squared residual at least \(1-K/D\). Sending \(D\) large defeats a uniform mean-square error bound strictly below one. This directly addresses a generic fixed random functional basis.

These are witness-class obstructions, not a no-go theorem for every nonlinear encoding of the canonical reachable fields. Proving such a no-go statement would require a sufficiently rich reachable family plus a stated continuity, finite-precision, or computability model for the encoder. In particular, a bare assertion that the unit ball of \(L^2\) is noncompact is not a lower bound on the much smaller set generated by one specified nonlinear flow.

The distinction is material here: under the normalized gradient bound, the initial label-to-parameter force is a Hilbert--Schmidt integral operator. For

\[
Ay=P[y(X)g(u_0,X)],
\]

and an orthonormal family \(v_j\) in parameter space, Parseval or Bessel gives

\[
\sum_j\|A^*v_j\|_{L^2(P_X)}^2
=P\sum_j|\langle g(u_0,X),v_j\rangle|^2
\le P\|g(u_0,X)\|^2\le G^2.
\]

Thus force generation already has an integral smoothing structure absent from an arbitrary Hilbert-ball recovery problem. Whether that structure admits an autonomous fixed population dictionary through the whole nonlinear trajectory is the actual open bridge. The elementary nullspace objection alone does not decide it.

## 6. Relation to the supplied memory hierarchy

The prompt supplied the retained-history equations

\[
\dot H_k=\rho h-\frac\rho\tau\mathsf T H_k,
\qquad
\dot B_k=r\delta-\frac\rho\tau\mathsf T B_k,
\qquad \dot\tau=\rho,
\qquad \rho=\sqrt{P r^2},
\]

and reconstruction

\[
W^\ell=W_0^\ell-
\frac{2}{n\tau}P\sum_k(2k+1)B_k^\ell(H_k^{\ell-1})^\top.
\tag{6.1}
\]

Here \(\mathsf T\) is the supplied temporal coefficient operator, not the physical-time horizon \(T\). No claim about the hierarchy's truncation error is supplied or assumed by the sampling theorem. The supplied clock starts at \(\tau(0)=1\), so division by \(\tau\) is nonsingular. At \(\rho=0\), the displayed moment equations have their direct zero-source interpretation almost surely under the data law; no division by \(\rho\) is needed in these equations.

Replacing \(P\) in a fixed-\(q\) version of (6.1) by \(s\) equal-weight samples gives

\[
W^\ell-W_0^\ell=-\frac{2}{n\tau s}
\sum_{i=1}^s\sum_{k=0}^{q-1}(2k+1)
B_k^\ell(Z_i)(H_k^{\ell-1}(Z_i))^\top.
\tag{6.2}
\]

Consequently the learned increment in this particular representation has rank at most \(sq\). The exact base \(W_0^\ell\) remains full rank. Therefore combining sampling with finite temporal memory does introduce a finite-rank learned increment, even though it is not a spectral low-rank truncation. This should not be sold as avoiding all low-rank representations.

Sampling alone does not imply a rank-\(s\) learned increment: although its instantaneous hidden-weight derivative has rank at most \(s\), the directions evolve and their time integral can have full rank. It is the additional finite history factorization in (6.2) that gives the rank bound.

For width \(n\) and depth of order \(L\), retaining nodewise \(B,H\) arrays costs order \(Lnsq\) evolving scalar entries, plus node descriptors, other trainable boundary variables, and the exactly retained initialization. The initialized hidden matrices themselves cost order \(Ln^2\) if stored explicitly. A permitted exact random-operator primitive for \(W_0\) changes how that base is accessed, but does not make it newly trained coefficient storage.

The direct parameter sampling theorem avoids \(q\). To combine it with a \(q\)-memory approximation, one needs a separate compact-time memory error estimate and stability theorem, and then allocates the total error between sampling and temporal truncation. Applying the abstract functional theorem directly to the \(q\)-field system instead yields constants \(\Lambda_q,M_q\); it does not remove their dependence on \(q\).

The weights \(2k+1\) and the \(\tau^{-1}\) reconstruction matter. A small unweighted average error over coefficient fields need not give a small matrix or prediction error. A weighted direct-sum norm, possibly using a Parseval identity from the exact temporal basis, can prevent artificial factors of \(q\), but the corresponding reconstruction and multiplication bounds must actually be proved. A shared random atom count \(K\) does not by itself establish a \(q\)-independent total coefficient count: independently parameterized \(q\) fields typically need order \(qK\) coefficients, while shared scalar coefficients require an additional joint dictionary representation.

## 7. Norms and observables cannot be interchanged

For a population field \(v\in L^2(P_X;\mathbb R^a)\), its \(L^2\) error equals the supremum of its pairing against all vector-valued \(L^2\) tests of norm at most one. This follows from Cauchy--Schwarz and choosing the test proportional to the error. Thus a claim uniform over that entire unit test ball is a full \(L^2\) reconstruction claim; preserving a finite random collection of pairings is weaker.

By contrast, \(L^2(P_X)\) error does not imply uniform pointwise error over inputs. A field of fixed \(L^2\) norm can concentrate on a set of arbitrarily small mass. For example, \(v=\varepsilon p^{-1/2}\mathbf1_A\), where \(P_X(A)=p\), has \(L^2\) norm \(\varepsilon\) and supremum \(\varepsilon/\sqrt p\). To obtain uniform-input error one needs a uniform derivative bound as in Section 3, a reproducing-kernel bound, or another explicit regularity-to-supremum estimate. Such an estimate may reintroduce dimension dependence.

A Johnson--Lindenstrauss-type preservation statement for distances or finitely many observables is also not a decoder theorem for complete hidden and response fields. The two claims require different hypotheses.

## 8. Claim status and the highest-leverage next obligation

| Claim | Status | Decisive condition or gap |
|---|---|---|
| Same-initialization population/coreset compact-time comparison, with inverse-square sample count and no parameter covering | Proved above under (2.1) and well-posedness | Verify normalized derivative bounds for the exact architecture and allowed inputs |
| Uniformity in original sample count \(N\) | Proved under the same conditional bounds | Retained coreset still contains input nodes and labels |
| Width- and input-dimension-independent constants for the canonical deep network | Open in this scoped route | Complete architecture, activation and norm hypotheses were not supplied |
| Autonomous \(K\)-coefficient Hilbert Galerkin approximation with inverse-square rate | Proved under (4.1), Lipschitz stability and a valid observation norm | Fixed dictionary bound and finite computability of (4.5) are substantive |
| Mere Hilbert norm bounds imply a generic fixed random basis with that rate | False | Nullspace and trace arguments in Section 5 |
| State-dependent bounded atomic variation implies one fixed preselected sketch | Not established; false as an implication for a generic fixed measure | A domination or adaptive-selection theorem is missing |
| Coreset plus finite \(q\) is free of rank restrictions | False for reconstruction (6.2) | Learned increment has rank at most \(sq\) |
| Total population code size \(O(\varepsilon^{-2})\), independent of width, \(q\), and population integration | Not established | Three separate complexity bridges remain |

The highest-leverage next theoretical task is to identify an explicit, initially selectable nonlinear dictionary for the canonical *joint* forward, backward, and history fields, then prove a bound of the form (4.1) in a weighted norm that controls reconstruction. If this can be done with constants independent of \(d\) and width and with computable projected expectations, the fixed-reference proof already supplies compact-time propagation. If the only available atoms are data nodes with neuronwise response arrays, the construction remains the coreset route and inherits its storage and finite-history rank properties.
