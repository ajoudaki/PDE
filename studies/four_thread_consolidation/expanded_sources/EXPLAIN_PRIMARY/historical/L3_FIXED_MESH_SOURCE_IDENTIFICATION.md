# Fixed-mesh source identification for clipped three-hidden-layer arctangent flow

This is a fixed finite-program result. Its constants may depend on the number of steps, the step size, and the clipping level. It proves neither mesh-uniform response bounds nor a continuous-time limit.

## Statement and conventions

Fix an integer N, a feature step Delta > 0, and a smooth clipping function tau_R with bounded derivative, |tau_R(q)| <= |q|, |tau_R'(q)| <= 1, and |tau_R(q)| <= 2R. Let phi(z)=arctan(z), d=phi', F(z)=z+z^3/3. Let A_0,B_0 be independent n by n matrices with independent N(0,1/n) entries, independent of iid standard Gaussian Z^(1)_0. Initially C_0=0.

Consider the exact finite-width discrete calculation

\[
X^{(1)}_0=F(Z^{(1)}_0),\quad
H^{(1)}_k=\phi(F^{-1}(X^{(1)}_k)),\quad
Z^{(2)}_k=A_kH^{(1)}_k,\quad H^{(2)}_k=\phi(Z^{(2)}_k),
\]
\[
Z^{(3)}_k=B_kH^{(2)}_k,\quad H^{(3)}_k=\phi(Z^{(3)}_k),\quad
\delta^{(3)}_k=C_k\odot d(Z^{(3)}_k),\quad
q^{(2)}_k=B_k^\top\delta^{(3)}_k,
\]
\[
\delta^{(2)}_k=d(Z^{(2)}_k)\odot\tau_R(q^{(2)}_k),\quad
q^{(1)}_k=A_k^\top\delta^{(2)}_k,
\]
\[
X^{(1)}_{k+1}=X^{(1)}_k+\Delta q^{(1)}_k,\quad
A_{k+1}=A_k+\frac\Delta n\delta^{(2)}_k(H^{(1)}_k)^\top,
\]
\[
B_{k+1}=B_k+\frac\Delta n\delta^{(3)}_k(H^{(2)}_k)^\top,
\qquad C_{k+1}=C_k+\Delta H^{(3)}_k.
\]

For every fixed same-layer tuple of its nodes through step N, its empirical law converges in probability in W_2 to the scalar construction below. In particular, all the pairwise contractions used below converge. Covariance matrices may be singular.

There are four mutually independent centered Gaussian groups

\[
(\xi^{(2)}_k)_k,\quad(\xi^{(3)}_k)_k,\quad
(\zeta^{(1)}_k)_k,\quad(\zeta^{(2)}_k)_k,
\]

also independent of Z^(1)_0, with covariances

\[
\mathbb E\xi^{(\ell)}_k\xi^{(\ell)}_s
=\mathbb E H^{(\ell-1)}_kH^{(\ell-1)}_s,\qquad
\mathbb E\zeta^{(\ell-1)}_k\zeta^{(\ell-1)}_s
=\mathbb E\delta^{(\ell)}_k\delta^{(\ell)}_s,
\quad\ell=2,3.
\]

The scalar equations are

\[
X^{(1)}_k=F(Z^{(1)}_0)+\Delta\sum_{r<k}q^{(1)}_r,
\quad H^{(1)}_k=\phi(F^{-1}(X^{(1)}_k)),
\]
\[
Z^{(2)}_k=\xi^{(2)}_k+\sum_{s<k}a^{(2)}_{ks}\delta^{(2)}_s,
\quad q^{(1)}_k=\zeta^{(1)}_k+\sum_{s\le k}b^{(2)}_{ks}H^{(1)}_s,
\]
\[
Z^{(3)}_k=\xi^{(3)}_k+\sum_{s<k}a^{(3)}_{ks}\delta^{(3)}_s,
\quad q^{(2)}_k=\zeta^{(2)}_k+\sum_{s\le k}b^{(3)}_{ks}H^{(2)}_s,
\]

with H^(ell)=phi(Z^(ell)), C_k=Delta sum_{r<k} H^(3)_r, delta^(3)_k=C_k d(Z^(3)_k), delta^(2)_k=d(Z^(2)_k)tau_R(q^(2)_k), and

\[
a^{(\ell)}_{ks}
=\mathbb E\frac{\partial H^{(\ell-1)}_k}
                    {\partial\zeta^{(\ell-1)}_s}
 +\Delta\mathbb E H^{(\ell-1)}_kH^{(\ell-1)}_s,
\qquad s<k,
\]
\[
b^{(\ell)}_{ks}
=\mathbb E\frac{\partial\delta^{(\ell)}_k}
                    {\partial\xi^{(\ell)}_s}
 +\Delta\mathbf1_{s<k}\mathbb E\delta^{(\ell)}_k\delta^{(\ell)}_s,
\qquad s\le k.
\]

Every derivative is a derivative of the explicit finite coordinate expression with respect to the named Gaussian source coordinate. Previously calculated deterministic coefficients and covariance parameters are held fixed. Distinct source coordinates remain distinct formal arguments even if their joint Gaussian law is singular. Coefficients themselves need not be invariant under a different off-support extension; their contracted correction is invariant.

## Finite Gaussian conditioning, with two matrices

We first prove the needed source rule for a fixed finite calculation with deterministic scalar coefficients, globally Lipschitz C^1 coordinate instructions having bounded first derivatives, and finitely many independent Gaussian matrices, each reusable in both directions. The root coordinate tuples are iid with finite second moments and independent of the matrices. The initial tuple may contain both Z and F(Z); no Lipschitz assertion about F as a root-generating function is needed.

Condition on the complete adaptive transcript. For one selected matrix W, write its previous observations as

\[
WV=Y,\qquad W^\top U=Q.
\]

The other matrices cause no change to the following formula. Conditional residuals of the independent matrices remain independent: inductively, a query is measurable from the current transcript, and its newly observed answer imposes a linear constraint only on the queried matrix. Coordinate calculations reveal no further randomness.

When the two input Gram matrices are invertible, Gaussian orthogonal projection gives

\[
W\mid\mathcal H\ \overset d=
Y(V^\top V)^{-1}V^\top
+U(U^\top U)^{-1}Q^\top P_{V^\perp}
+P_{U^\perp}\widetilde W P_{V^\perp}.
\tag{1}
\]

For a new input h, put alpha_n=(V^T V)^(-1)V^T h and h_perp=h-V alpha_n. Then

\[
Wh=Y\alpha_n+U\beta_n+
\frac{\|h_\perp\|_2}{\sqrt n}P_{U^\perp}g,
\quad
\beta_n=(U^\top U/n)^{-1}(Q^\top h_\perp/n),
\tag{2}
\]

in conditional law, with fresh standard Gaussian g. The transpose formula is identical with the two sides interchanged.

Assume for the moment that all limiting input Gram matrices are positive definite. Induction on the finite transcript proves joint W_2 empirical convergence: all coefficients in (2) converge by the previous induction hypothesis; the removed projection has conditional mean squared normalized norm rank(U)/n; after removing it, conditional averaging of independent Gaussian coordinates gives joint weak convergence and second-moment convergence. Globally Lipschitz coordinate instructions preserve W_2 convergence. This works unchanged with two interleaved matrices.

## Why the response coefficient is the source derivative

Here is the identification step, rather than an invocation of a general tensor-program theorem. Use lowercase letters for the limiting scalar variables. Let the previous forward inputs be v_r, and the previous transpose inputs be u_s. Let Gamma_U=(E u_s u_t)_{st}. By induction write

\[
y_r=\xi_r+\sum_s D_{rs}u_s,
\qquad D_{rs}=\mathbb E\partial_{\zeta_s}v_r,
\]
\[
q_s=\zeta_s+\text{a linear combination of previous forward inputs}.
\]

Unavailable/future-source derivatives are zero. Let alpha be the limiting least-squares coefficients and h_perp=h-sum_r alpha_r v_r. Orthogonality gives E[v_r h_perp]=0 for every old forward input. Therefore the non-Gaussian correction in every q_s drops out of its pairing with h_perp:

\[
\mathbb E[q_s h_\perp]=\mathbb E[\zeta_s h_\perp].
\]

The Gaussian group zeta is independent of the roots and all other Gaussian groups and has covariance Gamma_U. Gaussian integration by parts yields

\[
\mathbb E[\zeta h_\perp]
=\Gamma_U\,\mathbb E\nabla_\zeta h_\perp.
\]

Thus (2)'s limiting coefficient is

\[
\beta=\mathbb E\nabla_\zeta h
       -\sum_r\alpha_r\mathbb E\nabla_\zeta v_r.
\]

After substituting the decompositions of y_r into (2), their old responses cancel the second term. The resulting rule is exactly

\[
\boxed{\quad
(Wh)_{\mathrm{lim}}
=\xi_h+\sum_s u_s\,\mathbb E\partial_{\zeta_s}h.
\quad}
\tag{3}
\]

The new Gaussian source is xi_h=sum_r alpha_r xi_r+sigma g_scalar, where sigma^2=E h_perp^2. Hence Cov(xi_h,xi_r)=E[h v_r] and Var(xi_h)=E h^2. The fresh scalar innovation is independent of every old source. As a result, source groups belonging to distinct oriented matrices W, W^T remain mutually independent, even though W and W^T themselves are dependent. The same argument applies separately to A_0 and B_0 at every interleaved call.

This proof uses the complete derivative of h as its finite coordinate expression. It does not discard derivative paths passing through calls to the other matrix.

## Removing singular-Gram difficulties

For each matrix call, temporarily replace its input h by h+epsilon chi, where chi is a new independent standard Gaussian input vector, revealed immediately before that call. At fixed epsilon>0, the limiting squared distance of a new input from its previous same-direction input span is at least epsilon^2: project the new independent chi off that fixed-dimensional span and use conditional second-moment calculations. Consequently all limiting query Gram matrices are positive definite, and the preceding proof applies. The chi variables are additional independent roots; the source rule (3) applies to the perturbed query inputs.

For the fixed finite program, couple perturbed and unperturbed calculations using the same original matrices and roots. On the event that all the finitely many matrix operator norms and input-noise normalized norms are bounded, induction through the instructions gives

\[
\max_v\|v^\epsilon-v\|_n\le C\epsilon,
\tag{4}
\]

where C depends on the fixed program but not on n or epsilon<=1. The event has probability tending to one. The matrix bound follows, for example, by a fixed-net Gaussian tail bound and a union bound over the two matrices.

The scalar source constructions converge as epsilon decreases to zero as well. A detailed finite induction suffices: source covariance entries are second moments of previously constructed inputs; Gaussian covariance square roots are continuous even at singular positive-semidefinite matrices; all previously constructed scalar coordinate functions and their source derivatives are continuous in the finite deterministic coefficient list. Their first derivatives have deterministic bounds at each fixed instruction because the coordinate instructions have bounded first derivatives. Therefore Gaussian coupling, W_2 convergence, and dominated convergence pass both second moments and expected source derivatives to the epsilon=0 recursion. No inverse or pseudoinverse is used in this last continuity step. Combining this fact with (4) identifies the unperturbed empirical limit with (3).

For completeness, degenerate Gaussian Stein also directly explains the absence of ambiguity. If zeta has covariance Gamma and u has second-moment matrix Gamma, then

\[
\mathbb E[\zeta f]=\Gamma\mathbb E\nabla f,
\qquad
u^\top(I-\Gamma^+\Gamma)v=0\quad\text{a.s.}
\]

for every deterministic v. Thus replacing E grad f by Gamma^+ E[zeta f] may change its entries, but cannot change the response sum u^T E grad f. One must not assert convergence of finite pseudoinverses at a rank drop.

## Application and the empirical training coefficients

Unroll A_k and B_k into their initial matrices plus their finite learned rank-one sums. Each forward trained call has the extra term

\[
\Delta\sum_{s<k}\delta^{(\ell)}_s
                \langle H^{(\ell-1)}_s,H^{(\ell-1)}_k\rangle_n,
\]

and each transpose trained call has the extra term

\[
\Delta\sum_{s<k}H^{(\ell-1)}_s
                \langle\delta^{(\ell)}_s,\delta^{(\ell)}_k\rangle_n.
\]

Freeze these finitely many contractions at the population values constructed causally. This produces an oracle with deterministic coefficients, to which the proved finite conditioning/source lemma applies. At each stage the population contraction involves only already constructed variables, so this definition is not circular.

The oracle and actual finite Euler calculation agree asymptotically. Indeed, fixed clipping gives |delta^(2)|<=2R; bounded arctangent gives |C_k|<=N Delta pi/2 and bounded delta^(3). The product defining delta^(3) can therefore be extended to a globally Lipschitz C^1 map by smoothly clipping C outside a slightly larger interval. Every other required coordinate map is already globally Lipschitz. Root tuples have finite second moments. All oracle norms and all initial matrix operator norms are bounded with probability tending to one. On that event,

\[
|\langle u,v\rangle_n-\langle\bar u,\bar v\rangle_n|
\le \|u-\bar u\|_n\|v\|_n+
    \|\bar u\|_n\|v-\bar v\|_n.
\]

Finite induction through the unrolled calculation bounds actual/oracle error by a constant times the largest oracle contraction error. Every such error converges to zero by the lemma. No growing-mesh estimate is used. Adding the learned terms to (3) gives exactly the stated a and b formulas.

The causal call order at step k is A_0 H1_k, B_0 H2_k, B_0^T delta3_k, A_0^T delta2_k. Thus forward response sums use s<k, while transpose response sums use s<=k. This order also proves that every covariance extension and every derivative coefficient is known when needed.

As explicit checks on the current-source terms,

\[
b^{(3)}_{kk}=\mathbb E[C_k\phi''(Z^{(3)}_k)],
\]
\[
b^{(2)}_{kk}
=\mathbb E[\phi''(Z^{(2)}_k)\tau_R(q^{(2)}_k)]
 +b^{(3)}_{kk}\mathbb E[d(Z^{(2)}_k)^2\tau_R'(q^{(2)}_k)].
\]

The second term on the last line is a current-step return through the other matrix; omitting it would be incorrect. Earlier-source derivatives also retain every such path.

Finally, replacing C_0=0 by iid N(0,n^-2) changes no fixed-mesh limit. Couple the two finite calculations; the initial normalized C difference is O_P(n^-1), its initial coordinate supremum is bounded with probability tending to one, and the same fixed-step Lipschitz comparison applies. This last statement is only for fixed N, Delta, R.

## Scope of the result

The displayed scalar representation, the four independent Gaussian source groups, all current/previous response terms, and singular covariance cases are justified at each fixed clipped finite mesh. Individual off-support derivative coefficients require the stated formal-expression convention. This proof supplies no bound uniform in N, Delta tending to zero, or R tending to infinity.
