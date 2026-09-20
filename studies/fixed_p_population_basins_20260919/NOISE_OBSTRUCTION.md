# Accepted Gaussian noise does not by itself force zero loss

This is a scoped, prompt-only theoretical analysis. Its scientific inputs are the assumptions in the assignment: a separable Hilbert state space; a continuous, nonnegative, continuously differentiable loss with locally Lipschitz gradient; every local minimum has zero loss; independent fixed-scale Gaussian proposals accepted exactly when they strictly decrease loss; and optional full-gradient flow between proposals. No other research artifacts were read. No numerical experiment was performed.

**Conclusion.** Those assumptions do not imply almost-sure convergence of the loss to zero. The obstruction already occurs for a real-analytic scalar squared loss with a unique local minimum, which is a zero global minimum. With ordinary Gaussian proposals, there is positive probability of escape to infinity with loss converging to one. This remains true with any finite nonnegative gradient-flow intervals. With proposals conditioned to a fixed ball, a suitable initialization makes the positive loss limit occur almost surely.

This disproves an implication from the abstract assumptions. It does not assert that the particular population loss under investigation realizes this obstruction; ruling that out requires additional structure of that loss.

## 1. A real-analytic squared loss

On the Hilbert space \(H=\mathbb R\), define
\[
r(x)=1+(x-1)e^{-x},\qquad L(x)=r(x)^2.
\]
Both functions are real analytic, so \(L\) is nonnegative, continuously differentiable, and has locally Lipschitz gradient. Direct differentiation gives
\[
r'(x)=(2-x)e^{-x},\qquad
L'(x)=2r(x)(2-x)e^{-x}.
\]
The residual is strictly increasing on \(( -\infty,2)\), vanishes at zero, and satisfies
\[
r(2)=1+e^{-2},\qquad r(x)>1\quad(x>2),\qquad
\lim_{x\to+\infty}r(x)=1.
\]
Consequently \(r\) has exactly one zero. The loss is strictly decreasing on \(( -\infty,0)\), strictly increasing on \((0,2)\), and strictly decreasing on \((2,\infty)\). Its only stationary points are
\[
x=0\quad\text{(unique local and global minimum, }L=0\text{)},
\qquad
x=2\quad\text{(strict local maximum)}.
\]
In particular, there are no positive-loss local minima, but
\[
L(x)>1\quad(x>2),\qquad \lim_{x\to+\infty}L(x)=1.
\tag{1}
\]

## 2. Gradient flow preserves the escape branch

Let \(\phi_h(x)\) be the full-gradient flow after a finite time \(h\ge0\):
\[
\dot x=-L'(x).
\]
For \(x>2\), the vector field is strictly positive. The right branch is invariant and
\[
\phi_h(x)\ge x>2.
\tag{2}
\]
There is no finite-time explosion on this branch: the positive vector field is continuous and bounded on \([2,\infty)\), because it tends to zero at infinity. In fact, gradient flow is globally defined from every scalar initial state. On \(( -\infty,0)\) it points toward zero; on \((0,2)\) it points toward zero; and the stationary states and right branch account for the remaining cases.

The argument below applies to every sequence of finite nonnegative flow intervals \(h_k\), including \(h_k\equiv0\) and \(h_k\equiv h>0\). These intervals may depend on past states and observations. Only (2) is used.

## 3. Gaussian proposals: a positive-probability escape event

Fix \(\tau>0\). Let \(\xi_1,\xi_2,\ldots\) be independent \(N(0,\tau^2)\) increments. Starting at \(X_0=x_0>2\), define the accepted state
\[
A_k=\begin{cases}
X_k+\xi_{k+1},&L(X_k+\xi_{k+1})<L(X_k),\\
X_k,&\text{otherwise},
\end{cases}
\qquad X_{k+1}=\phi_{h_k}(A_k).
\tag{3}
\]
Using the opposite convention, with the flow immediately before each proposal, gives the same proof after relabeling proposal times.

Define from the same increments the monotone comparison process
\[
R_k=x_0+\sum_{j=1}^k\xi_j^+,
\qquad \xi_j^+=\max(\xi_j,0),
\]
and the event
\[
E=\bigcap_{k\ge0}\{\xi_{k+1}>2-R_k\}.
\tag{4}
\]
On \(E\), induction proves \(X_k\ge R_k>2\) at every proposal time. Indeed, the proposed state satisfies
\[
X_k+\xi_{k+1}\ge R_k+\xi_{k+1}>2.
\]
Strict decrease of \(L\) on that branch means exactly that positive increments are accepted and negative increments are rejected. Thus
\[
A_k=X_k+\xi_{k+1}^+,
\qquad
X_{k+1}\ge X_k+\xi_{k+1}^+\ge R_{k+1},
\]
where the first inequality uses (2).

It remains to prove that \(E\) has positive probability. For any \(\lambda>0\), the Gaussian exponential moment is
\[
\mathbb E e^{-\lambda\xi_1}=e^{\lambda^2\tau^2/2}.
\]
Since \(\xi_{k+1}\) is independent of \(R_k\), the exponential Markov inequality yields
\[
\begin{aligned}
\mathbb P(\xi_{k+1}\le2-R_k)
&\le e^{\lambda^2\tau^2/2}\,
\mathbb E e^{-\lambda(R_k-2)}\\
&=e^{-\lambda(x_0-2)+\lambda^2\tau^2/2}\,q^k,
\end{aligned}
\]
where
\[
q=\mathbb E e^{-\lambda\xi_1^+}\in(0,1).
\]
The strict upper bound holds because the integrand is at most one and is strictly less than one on the positive-probability event \(\xi_1>0\). The union bound and geometric series therefore give the explicit estimate
\[
\mathbb P(E)
\ge 1-
\frac{e^{-\lambda(x_0-2)+\lambda^2\tau^2/2}}{1-q}.
\tag{5}
\]
For example, choose any fixed \(\lambda>0\) and then choose
\[
x_0>2+\frac{\lambda\tau^2}{2}
       +\frac1\lambda\log\frac1{1-q}.
\tag{6}
\]
The lower bound in (5) is then strictly positive. All choices depend only on the fixed noise law, not on its future realization.

Finally, \(R_k\to\infty\) almost surely. To see this without an asymptotic estimate, choose \(a>0\). The independent events \(\{\xi_j\ge a\}\) have the same positive probability \(p\). For each \(N\), the probability that no such event occurs after \(N\) is \(\lim_{m\to\infty}(1-p)^m=0\). Taking a countable union over \(N\) proves that infinitely many increments are at least \(a\). Their positive parts force the sum defining \(R_k\) to diverge.

Intersecting that probability-one event with \(E\), we obtain
\[
\mathbb P\bigl(X_k\to+\infty\text{ and }L(X_k)\downarrow1\bigr)>0.
\tag{7}
\]
The accepted states \(A_k\) have the same loss limit. This is a statement about the actual stochastic trajectory, not just about existence of a deterministic escape valley.

Positive escape probability in fact holds from every \(x_0>2\). Choose \(B\) so large that (5), started at any point at least \(B\), is bounded below by some \(c>0\). The first Gaussian increment has positive probability to exceed \(B-x_0\); it is accepted and, after the optional flow, leaves the state at least \(B\). Independence of the subsequent increments then gives escape probability at least \(c\,\mathbb P(\xi_1\ge B-x_0)>0\).

## 4. Gaussian proposals conditioned to a fixed ball

Suppose instead that the independent increments have the Gaussian law conditioned on \(|\xi|<\varepsilon\), where \(\varepsilon>0\) is fixed. Initialize at
\[
x_0>2+\varepsilon.
\]
Every proposal remains above two as long as the current state is at least \(x_0\). On that branch the acceptance rule and optional gradient flow imply
\[
X_{k+1}\ge X_k+\xi_{k+1}^+\ge X_k.
\]
Induction therefore makes the branch invariant for every realization. The conditional Gaussian law has \(\mathbb P(\xi\ge a)>0\) for every \(a\in(0,\varepsilon)\). The preceding independent-event argument gives
\[
X_k\to+\infty,\qquad L(X_k)\downarrow1
\quad\text{almost surely}.
\tag{8}
\]
Thus the bounded-proposal variant has an even stronger obstruction.

## 5. Any nonzero separable Hilbert space

The scalar example already disproves a universal Hilbert-space theorem. If an infinite-dimensional state space is required, choose a unit vector \(e\in H\) and set
\[
\mathcal L(S)=\bigl[1+(\langle S,e\rangle-1)e^{-\langle S,e\rangle}\bigr]^2.
\]
This is a real-analytic squared loss on \(H\). Its local minima are exactly the hyperplane \(\langle S,e\rangle=0\), and all have loss zero: at every other scalar coordinate the scalar function admits arbitrarily close lower values. Its gradient is
\[
\nabla\mathcal L(S)=L'(\langle S,e\rangle)e,
\]
which is locally Lipschitz. The scalar coordinate obeys precisely the dynamics above.

For a centered full-support Gaussian \(Z\) with trace-class covariance \(Q\), the proposed scalar increment \(\sigma\langle Z,e\rangle\) is \(N(0,\tau^2)\), with
\[
\tau^2=\sigma^2\langle Qe,e\rangle>0.
\]
The strict positivity follows from full support: zero variance would confine \(Z\) to the proper closed hyperplane \(e^\perp\). The orthogonal components of a proposal do not affect loss acceptance, so the proof applies even if those components are correlated with the scalar component.

For the law conditioned on \(\|\sigma Z\|<\varepsilon\), the scalar increment is bounded in absolute value by \(\varepsilon\). It has positive probability to exceed some \(a>0\): full support gives positive Gaussian mass to a sufficiently small ball around \(be\), for any \(0<a<b<\varepsilon\). This small ball lies inside the conditioning event. Independent conditioned proposals therefore give (8) as well. In both cases \(\|S_k\|\ge|\langle S_k,e\rangle|\to\infty\) on the escape event.

## 6. Exact consequence for the proposed global argument

The already-known local conclusion, that a nonminimum cannot be an accumulation point, is compatible with this example: the escaping trajectory has no norm accumulation point at all. Neither fixed-scale full support of the proposals nor adding full-gradient flow supplies the missing recurrence or compactness.

The decisive mechanism is a summable total probability of proposals returning from progressively larger states to the other side of the loss barrier. The monotone accepted positive increments make this summability explicit. A global theorem for the particular population loss must use an additional property that excludes this geometry, or a mechanism ensuring recurrent access to uniformly effective descent sets. The abstract assumptions alone leave the desired zero-loss conclusion false.
