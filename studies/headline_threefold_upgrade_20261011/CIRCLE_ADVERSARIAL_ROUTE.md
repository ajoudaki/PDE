# Circle endpoint: actual-flow structural obstructions

This bounded route does not prove the requested \(n^{-1/2}\) lower bound and does not produce a counterexample. It proves two narrower statements about the **actual fully trained endpoint**: a differential-rank obstruction to local independence from initialization, and finite-width nonconstancy outside a countable set of label scales. Neither statement permits replacing the trained network by frozen features. Frozen features appear below only as an exact derivative at zero labels.

Scientific inputs were restricted to `paper/compact.tex` and `paper/compact_fitting.tex`. No other study artifacts, experiments, or manuscript changes were used. The rigorous-mathematics, conjecture-audit, and canonical-notation instructions were applied.

## Fixed target and notation

Let \(v_a=x_a/\sqrt2\in S^1\), \(a=1,\ldots,m\), be fixed pairwise nonparallel directions. Use exactly the architecture, Gaussian hidden initialization, zero readout initialization, block mobilities, and gradient flow in `compact.tex`. In particular,

\[
 z^{(1)}(v)=W^{(1)}v,\qquad
 z^{(\ell)}(v)=W^{(\ell)}h^{(\ell-1)}(v),\qquad
 h^{(\ell)}(v)=\phi_\ell(z^{(\ell)}(v)),\qquad
 f_n(v)=\frac{w^\top h^{(L)}(v)}n.
\]

All \(L\ge2\) hidden layers train. Each activation is nonaffine, real analytic on the real axis, holomorphic on the specified strip, and has bounded derivative there. Labels obey the original cap, without any additional smallness assumption.

For a fixed nonzero label direction \(\bar y\in\mathbb R^m\), normalized by \(\|\bar y\|_2/\sqrt m=1\), write

\[
 y=\lambda\bar y,\qquad
 0<\lambda\le\lambda_{\max}
 :=\frac\gamma m\beta^{-30L}.
\]

This variation of \(\lambda\) is used to state a partial theorem; it does not change the requested conclusion, which must hold at every fixed admissible nonzero label vector. The requested probability bound concerns two independent ordinary dense runs and

\[
 \sup_{v\in A}|f_n(\infty,v)-\widetilde f_n(\infty,v)|
 \ge \frac{c_\delta}{\sqrt n},
\]

where \(A\) is the whole circle or a prescribed nonempty separated open arc. The constants may depend on every fixed problem parameter and on \(\delta\), but not on \(n\).

## 1. Local endpoint maps lose exactly the training-residual directions

Use mobility coordinates

\[
 \theta=(W^{(1)}/\sqrt n,W^{(2)},\ldots,W^{(L)},w/\sqrt n)
 \in\mathbb R^p,
 \qquad p=(L-1)n^2+3n.
\]

Let \(F(\theta)=(f_n(v_a))_{a=1}^m\) and let \(\pi(\theta_0)\) denote the parameter endpoint of gradient flow with fixed labels. Consider any trajectory supplied by the fitting lemma. Its endpoint \(\theta_\infty\) satisfies \(F(\theta_\infty)=y\), and \(DF(\theta_\infty)\) has rank \(m\): the readout contribution already has full row rank because the final training feature Gram is positive definite.

**Local endpoint lemma.** In a neighborhood of this initial condition, the endpoint map is real analytic, and

\[
 \operatorname{rank}D\pi=p-m,
 \qquad \dim\ker D\pi=m.
\]

Here the initial neighborhood allows perturbing all parameter blocks; the restriction to zero initialized readout is imposed afterward.

To verify the lemma, first work near the fitted endpoint. By the analytic inverse function theorem and the full row rank of \(DF\), analytic coordinates can be chosen as \((r,q)\), where \(r=F-y\in\mathbb R^m\) and \(q\in\mathbb R^{p-m}\). The gradient-flow equations have the form

\[
 \dot r=-A(r,q)r,\qquad \dot q=B(r,q)r,
 \qquad A=\frac2m DF\,DF^\top.
\]

The coordinate expression of \(B\) is analytic, and \(A(0,q_\infty)\) is positive definite. On a sufficiently small real or complex neighborhood, the Hermitian part of \(A\) remains uniformly positive. Hence \(\|r(t)\|\) decays exponentially, while \(q\) moves by at most a constant times the initial residual norm. Shrinking the neighborhood makes this estimate self-consistent for all positive time. The flows are holomorphic in their initial coordinates by locally convergent Picard iteration; exponential decay gives locally uniform convergence of \(q(t)\) and \(r(t)\) to \((0,q_\infty(r(0),q(0)))\). The limit is therefore holomorphic, and its real restriction is analytic.

On \(r=0\), the flow is stationary, so the endpoint map is the identity on the interpolation manifold. Its differential consequently has rank \(p-m\) at the endpoint, and the same rank in a sufficiently small neighborhood: one corresponding minor stays nonzero, while the image remains in the \((p-m)\)-dimensional interpolation manifold. A sufficiently late finite-time flow takes the original trajectory into this neighborhood. That finite-time flow is a local analytic diffeomorphism, with inverse given by the reversed ODE on the finite trajectory segment. Composing it with the local endpoint map proves the lemma at the original initial condition. The same argument includes the label vector as an analytic parameter.

Define the function map on an open arc \(A\) by

\[
 \Phi_A(\theta)=f_n(\theta,\cdot)|_A,
 \qquad
 r_A=\dim\operatorname{span}
 \left\{\partial_{\theta_j}f_n(\theta_\infty,\cdot)|_A:
               1\le j\le p\right\}.
\]

The notation \(r_A\) here denotes a differential rank, not a training residual. Equivalently, it is the maximal Jacobian rank over finite passive panels contained in \(A\).

The zero-readout initialization manifold has tangent space \(S\) of dimension \(p-n\). Since \(\ker D\pi\) has dimension \(m\),

\[
 \dim D\pi(S)\ge p-n-m.
\]

Because \(\ker D\Phi_A\) has dimension \(p-r_A\), restriction to this image gives

\[
 \operatorname{rank}D(\Phi_A\circ\pi)|_S
 \ge r_A-n-m.
\]

Thus local independence of the fitted function from all hidden initialization variables forces

\[
 r_A\le n+m.
\]

This is an exact statement about the trained endpoint. It identifies a concrete structural obstruction that a putative locally deterministic endpoint must satisfy.

For fixed parameters, the network and its parameter derivatives are real analytic in the circle angle. A linear combination of these derivatives vanishing on a nonempty open arc vanishes on the entire circle by the one-variable identity theorem. Consequently \(r_A\) is the same for every nonempty open arc and for the whole circle. A rank argument of this kind therefore addresses the requested supremum domain and is not an antipodal single-query argument.

**Unresolved hypothesis.** The present assumptions do not, by the preceding reasoning alone, establish \(r_A>n+m\) at the randomly attained endpoint. Generic identifiability of arbitrary deep networks with arbitrary strip-analytic nonaffine activations cannot be silently inserted here. Even proving this rank inequality would establish local nonconstancy, not the requested fluctuation scale.

## 2. Actual endpoint nonconstancy for all but countably many label scales

**Partial theorem.** Fix the data, activations, depth, nonzero label direction \(\bar y\), and a nonempty open arc \(A\). There is a finite \(n_0\) such that, for every \(n\ge n_0\), one can find a finite set \(E_n\subset(0,\lambda_{\max}]\) with the following property: for every \(\lambda\notin E_n\), the actual fitted prediction at a query in \(A\) is nonconstant on an open set of hidden initializations satisfying the fitting event. Its conditional law on that open set under ordinary Gaussian initialization is non-atomic. In particular, outside the countable set \(\bigcup_{n\ge n_0}E_n\), this finite-width nonconstancy holds at every such width.

The exceptional sets are an upper bound on possible failures of this proof, not evidence of any genuinely deterministic label scale.

Choose \(v_*\in A\) nonparallel to every training direction. Such a point exists because the excluded directions are finite. For all sufficiently large \(n\), there is a strict initialization-fitting event on which

\[
 [h_0^{(L-1)}(v_1),\ldots,h_0^{(L-1)}(v_m),
           h_0^{(L-1)}(v_*)]
\]

has full column rank. The needed population Gram positivity follows directly from the hypotheses. At the first layer, a dependence among the ridge functions \(\phi_1(u^\top v_a)\) would, at any nonzero Taylor degree \(k\ge m\), imply a dependence among \(v_a^{\otimes k}\). Choose a coordinate axis not orthogonal to any direction and write their distinct slopes as \(t_a\). The first \(m+1\) tensor coordinates give a Vandermonde matrix in these slopes, so the coefficients vanish. Such a Taylor degree exists: otherwise analyticity would make \(\phi_1\) a polynomial, and bounded derivative would make it affine. Positivity propagates through subsequent layers because a positive definite Gaussian covariance has full support and a nonconstant coordinatewise activation cannot have a nontrivial linear dependence on that support. The empirical Gram convergence in the fitting lemma, applied also to this fixed augmented panel, gives the asserted finite-width event with positive probability, jointly with strict fitting margins.

Fix an initialization \(\xi_0\) in that event; \(\xi\) denotes its hidden blocks, with readout zero. Put

\[
 H=[h_0^{(L)}(v_1),\ldots,h_0^{(L)}(v_m)]\in\mathbb R^{n\times m},
 \qquad a=H(H^\top H)^{-1}\bar y\in\mathbb R^n.
\]

Since \(\bar y\ne0\), at least one \(a_i\ne0\). Choose that row \(i\). The augmented penultimate feature rank gives a vector \(b\in\mathbb R^n\) satisfying

\[
 b^\top h_0^{(L-1)}(v_a)=0\quad(1\le a\le m),
 \qquad b^\top h_0^{(L-1)}(v_*)\ne0.
\]

Perturb only the \(i\)-th row of \(W_0^{(L)}\) by \(\tau b^\top\). The initialized training matrix \(H\), and hence \(a\), remain exactly unchanged. The passive feature changes only in coordinate \(i\), by

\[
 \phi_L\!\left(z_{0,i}^{(L)}(v_*)
       +\tau b^\top h_0^{(L-1)}(v_*)\right)
       -\phi_L\!\left(z_{0,i}^{(L)}(v_*)\right).
\]

This analytic function of \(\tau\) is nonconstant because \(\phi_L\) is nonconstant and the displayed slope is nonzero. Choose an arbitrarily small \(\tau\) for which it is nonzero. Strict fitting margins persist; write \(\xi_1\) for the resulting initialization. Both initializations can be placed in one connected open ball \(U\) of strict fitting initializations.

Now consider the **fully trained** predictor

\[
 g_n(\lambda)=f_n(\infty,v_*;\xi_1,\lambda\bar y)
             -f_n(\infty,v_*;\xi_0,\lambda\bar y).
\]

The local endpoint lemma shows that it is real analytic on a neighborhood of every point of \([0,\lambda_{\max}]\). The fitting lemma supplies all these endpoints, and the local analytic descriptions agree by uniqueness of the flow.

At \(\lambda=0\), the exact flow is stationary. Differentiating the actual flow at zero labels gives zero first-order hidden-weight motion because every hidden update contains both a residual and the readout. If \(u=\partial_\lambda w|_{\lambda=0}\), its exact linearized dynamics are

\[
 \dot u=-\frac2mH\left(\frac{H^\top u}{n}-\bar y\right),
 \qquad u(0)=0.
\]

Since \(H\) has full column rank,

\[
 u(\infty)=nH(H^\top H)^{-1}\bar y,
 \qquad
 \left.\partial_\lambda f_n(\infty,v_*;\xi,\lambda\bar y)
 \right|_{\lambda=0}=h_0^{(L)}(v_*)^\top a.
\]

The construction of \(\xi_1\) therefore gives \(g_n'(0)\ne0\). In particular, \(g_n\) is not identically zero. Its zeros in the compact interval \((0,\lambda_{\max}]\) form a finite set: zeros cannot accumulate in an analytic neighborhood, including at the two endpoints, and \(g_n'(0)\ne0\) excludes an accumulation at zero. Take these zeros as \(E_n\).

For \(\lambda\notin E_n\), the actual scalar endpoint map on \(U\) is analytic and nonconstant, since it takes different values at \(\xi_0\) and \(\xi_1\). Every level set of a nonconstant real analytic function on a connected open set has Lebesgue measure zero. One proof uses local power series, applies the one-variable isolated-zero property on coordinate lines, and inducts on dimension to treat lines on which the series vanishes identically; Fubini then gives the conclusion. Ordinary Gaussian initialization has a positive smooth density in all hidden coordinates, so conditioning on \(U\) yields a non-atomic scalar endpoint law. This proves the partial theorem.

The argument uses the original label interval. It does not require shrinking the label cap. Its conclusion is weaker because it excludes a countable collection of possible label scales and supplies no width-uniform anti-concentration.

## 3. What remains unresolved

The exact target is still open under this route. Three gaps must not be conflated:

1. **All fixed labels.** The analytic argument cannot exclude a special nonzero \(\lambda\) where the selected initialization difference vanishes. Proving every such zero harmless would require another witness or a structural theorem about the whole endpoint function map.
2. **The fluctuation scale.** The open set \(U\), its Gaussian probability, and the difference witnessed there can all deteriorate with \(n\). Analytic nonconstancy does not imply \(n\operatorname{Var}(f_n(\infty,v_*))\) stays positive, and a positive variance would not by itself prove the requested lower-tail probability.
3. **Every fixed confidence.** The desired result needs the scaled circle difference to stay away from zero in probability at each prescribed confidence. A positive-probability finite-width witness is insufficient. A nondegenerate endpoint fluctuation limit, or a direct quantitative anti-concentration argument with comparable force, is still needed.

No exact conservation law, finite label symmetry, or admissible activation identity was found that makes the actual fitted function deterministic on an open circle arc. The rank criterion explains one obstruction such a mechanism must overcome. The strongest established result of this route is the generic-label finite-width nonconstancy theorem above; it is not a proof of the requested root-n claim.
