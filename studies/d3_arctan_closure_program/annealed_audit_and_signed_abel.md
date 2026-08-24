# Annealed audit and the exact signed endpoint reduction

This note uses the normalized inner product
\[
  \langle v,w\rangle_n=n^{-1}v^{\mathsf T}w,
  \qquad (v\otimes w)y=v\langle w,y\rangle_n.
\]
Thus
\[
 P_2^{k+1}=P_2^k+h,B_3^k\otimes X_2^k,
 \qquad
 (P_2^k)_{:j}={h\over n}\sum_{s<k}B_3^sX_{2,j}^s.
\]
All assertions below are finite-dimensional identities unless a limiting statement is
explicitly labelled as such.

## 1. What the slow-tube construction does and does not prove

The local characteristic equations admit paths on which the dressed tangent grows
like \(\exp(c\sqrt L)\): choose, for a time interval of length comparable with
\(L^{-1/2}\),
\[
 R\simeq L,\qquad z\simeq-1,
 \qquad \beta\simeq- Ld(-1).
\]
The self term \(R d(z)\) is then cancelled in the state equation by the bath, while
the corresponding tangent transport remains expanding.  This proves that no
pathwise estimate of the form
\[
 \sup_{t\leq T}|D z(t)|\leq \Phi\bigl(\hbox{global energy of the state}\bigr)
\]
with a mesh-uniform, polynomially integrable \(\Phi\) can follow from global energy
alone.

It does **not** by itself disprove an annealed canonical estimate.  Full support in
the ambient Gaussian space only says that the tube event has positive probability
for each \(n\); it supplies no lower bound uniform in \(n\).  An open ball specifying
\(O(n)\) Gaussian coordinates can have probability \(\exp(-cn)\).

To turn the tube into an annealed counterexample one would need the following
finite-dimensional cavity statement.  For constants independent of \(n\), on an
event of probability at least \(c_0>0\), the conditional law of the three relevant
marks (one may use \(z(0),R(0),\beta(0)\), after subtracting their cavity means) must
have a density satisfying
\[
 \mathbb P\bigl(
   |z(0)+1|\leq cL^{-1/2},\ |R(0)-L|\leq c,
   \ |\beta(0)+Ld(-1)|\leq cL^{1/2}
   \mid \mathcal C_j\bigr)
 \geq c_1 e^{-C_1L^2}.                                      \tag{1.1}
\]
One also needs a conditional probability bounded below for the local continuity
bounds which keep the path in the tube for \(cL^{-1/2}\) time.  Under (1.1),
\[
 \|D F_j\|_p
 \gtrsim \exp\{c\sqrt L-C L^2/p\}.
\]
Taking \(L\asymp p^{2/3}\) gives \(\exp(cp^{1/3})\), contradicting a
\(C\sqrt p\) gradient estimate.

The available energy and Bessel estimates do not prove (1.1).  In particular,
nondegeneracy of the endpoint mark \(R(0)\) does not imply joint nondegeneracy with
the compensating bath \(\beta(0)\).  Consequently the rigorous conclusion is:

* the deterministic energy-to-gradient route is false;
* the annealed canonical Gaussian-Poincare route remains open.

## 2. Exact signed Abel identity for one hidden coordinate

Fix a hidden coordinate \(j\), and abbreviate
\[
 x_k=X_{2,j}^k,\quad b_k=B_3^k,\quad
 w_k=(\Gamma _2+P_2^k)_{:j},
\]
\[
 f_k=\Gamma _{2,:j}^{\mathsf T}b_k,\quad
 r_k=w_k^{\mathsf T}b_k,\quad
 \gamma_k=w_k^{\mathsf T}F_3^k,
 \quad \rho_k=\langle b_k,b_{k+1}\rangle_n.
\]
Since \(b_{k+1}=b_k+hF_3^k\) and
\(w_{k+1}=w_k+h b_kx_k/n\), direct multiplication gives
\[
 r_{k+1}-r_k=h\gamma_k+h x_k\rho_k.                \tag{2.1}
\]
Moreover
\[
 r_m-f_m=(P_2^m)_{:j}^{\mathsf T}b_m
       =h\sum_{s<m}x_s\langle b_s,b_m\rangle_n.     \tag{2.2}
\]
Combining (2.1) and (2.2), with \(P_2^0=0\), yields the exact signed formula
\[
 \boxed{
 f_m=f_0+h\sum_{k<m}\gamma_k+E_m,
 }
                                                               \tag{2.3}
\]
where
\[
 E_m=h\sum_{k<m}x_k
 \bigl(\langle b_k,b_{k+1}\rangle_n-
       \langle b_k,b_m\rangle_n\bigr).               \tag{2.4}
\]
There is no response norm in (2.4).  Since \(|x_k|\leq\pi/2\),
\(|b_{k,i}|\leq |A_i^k|\), and
\[
 |A_i^k|\leq |A_i^0|+{\pi T\over2},
\]
we have, pathwise,
\[
 |E_m|
 \leq C T\left(\|A^0\|_n+T\right)^2.                \tag{2.5}
\]
Indeed each of the two sums in (2.4) is bounded separately by Cauchy--Schwarz.
The right side of (2.5) has all fixed moments uniformly in the mesh (and uniformly
in \(n\), with the usual normalized Gaussian endpoint initialization).

Thus learned-column memory is not the obstruction.  Notice, however, that
splitting \(\gamma_k=\Gamma _{2,:j}^{\mathsf T}F_3^k+
(P_2^k)_{:j}^{\mathsf T}F_3^k\) in (2.3) makes the first sum telescope back to
\(f_m-f_0\).  Therefore (2.3) alone cannot estimate \(f_m\); its content is the
rigorous isolation and uniform control of every learned-memory boundary term.

## 3. Value-level first-chaos formula (no Malliavin tangent)

The remaining term has an exact signed covariance representation.  The elementary
lemma is as follows.

**Gaussian transfer lemma.**  Let \(Y=(Y_0,\ldots,Y_m)\) be centered Gaussian with
covariance \(C\), let \(b\in L^2(\sigma(Y),\mathcal E)\), and put
\[
 c=\mathbb E[Yb\mid\mathcal E].
\]
Then
\[
 \Pi_1 b=c^{\mathsf T}C^\dagger Y,
 \qquad
 \mathbb E[(\Pi_1b)^2\mid\mathcal E]
       =c^{\mathsf T}C^\dagger c
       \leq \mathbb E[b^2\mid\mathcal E].             \tag{3.1}
\]
If the isometric transfer sends \(Y_k\) to a feature coordinate \(x_k\), then
\[
 \boxed{\quad \mathcal P_m(x)=x^{\mathsf T}C^\dagger c.\quad}  \tag{3.2}
\]

To prove the lemma, diagonalize \(C\) on its range.  In whitened coordinates the
first-chaos coefficient of \(b\) is \(\mathbb E[\widehat Y b]\); Parseval gives
(3.1), and applying the specified isometry gives (3.2).  No differentiation of
\(b\) is used.

For the network, after deleting hidden neuron \(j\), the top-row Gaussian history is
\[
 Y_k=(\Gamma _2X_2^k)_i,
 \qquad C_{k\ell}=\langle X_2^k,X_2^\ell\rangle_n,
\]
and the transferred coordinate is
\(x_k=X_{2,j}^k\).  Formula (3.2) is exactly the invariant endpoint predictor
\(U\Pi_1b_m\).  The fixed-mesh row/column cavity expansion gives
\[
 f_m=\xi_m+\mathcal P_m(X_{2,j}^{0:m})+o_{L^p,n}(1),    \tag{3.3}
\]
where, at each fixed \((p,h)\), the remainder tends to zero and \(\xi_m\) is the
fresh Gaussian row-summed innovation.  The innovation obeys a \(C_T\sqrt p\)
(hence \(C_Tp\)) bound because \(|b_{m,i}|\leq|A_i^0|+C_T\).

Chronological extension consistency and \(hF_3^k=b_{k+1}-b_k\) give, exactly,
\[
 \mathcal P_{k+1}-\mathcal P_k=hT_{k+1}F_3^k,
 \qquad T_{k+1}b_k=T_kb_k,                              \tag{3.4}
\]
so the entire signed time sum collapses to the endpoint transfer.  Equations
(2.3)--(3.4) show that neither time accumulation nor learned memory requires a
total-variation estimate.

## 4. The precise surviving obligation

Let \(q=C^\dagger c\).  The sole leading estimate still needed is
\[
 \left\|q^{\mathsf T}X_{2,j}^{0:m}\right\|_p\leq C_Tp,
 \qquad C_T\ \hbox{independent of }h.                   \tag{4.1}
\]
The canonical law gives only
\[
 \mathbb E_j[(q^{\mathsf T}X_{2,j})^2]
   =q^{\mathsf T}Cq=c^{\mathsf T}C^\dagger c
   \leq \mathbb E[b_m^2].                               \tag{4.2}
\]
Gauge symmetry makes the left side of (3.2) odd under the simultaneous hidden-block
sign flip, but oddness plus (4.2) does not imply (4.1).

There is also an exact score representation
\[
 \mathcal P_m(x)=\mathbb E\!left[b_m(Y),
            Y^{\mathsf T}C^\dagger x\mid x,\mathcal E\right]. \tag{4.3}
\]
Cauchy--Schwarz bounds this by
\(\|b_m\|_2\sqrt{x^{\mathsf T}C^\dagger x}\), which is precisely the leverage
quantity whose expectation is controlled but whose exponential tail is not.
Thus replacing the tangent by the signed value removes the false pathwise-gradient
claim, but a crude absolute-value estimate in (4.3) merely recreates the old
leverage gap.

The useful rigorous status is therefore:

1. the Gaussian innovation in (3.3) is safe;
2. all learned and time-boundary terms are mesh-uniform by (2.5) and (3.4);
3. no annealed counterexample has been established;
4. the only unresolved leading term is the signed canonical endpoint value (3.2),
   not a block-gradient norm.

Any successful continuation must estimate (3.2) while retaining its sign (for
example through a causal signed martingale or a network-specific paraproduct
estimate).  Poincare followed by a pathwise tangent bound and Cauchy--Schwarz in
(4.3) are both too lossy.

## 5. Frozen-feature Volterra lemma: a mesh-uniform signed bound

There is a network-specific estimate which does prove (4.1) for the leading
row-cavity object.  Its important feature is that it estimates the **averaged signed
first-chaos coefficient**, not the norm of a full-network gauge tangent.

Fix an arbitrary feature history \(X^0,\ldots,X^m\), and set
\[
 C_{sk}=\langle X^s,X^k\rangle_n,
 \qquad |C_{sk}|\leq K:=(\pi/2)^2.
\]
After one top row has been removed from the lower network, its exact forward
recursion, conditional on this history, is the scalar Volterra system
\[
 \begin{aligned}
 z_k&=y_k+h\sum_{s<k}b_s C_{sk},\\
 A_k&=A_0+h\sum_{s<k}\arctan z_s,\\
 b_k&=A_k d(z_k).
 \end{aligned}                                             \tag{5.1}
\]
Here \(y_k=(\Gamma _2X^k)_i\) is a centered Gaussian history with covariance
\(C\).  Formula (5.1) is just the exact unrolling of
\(P_2^k=h\sum_{s<k}B_3^s\otimes X^s\); no approximation has been made inside the
frozen row.

**Volterra first-chaos lemma.**  Let \(b_m(y,A_0)\) be defined by (5.1), with
\(mh\leq T\).  Then
\[
 \sup_{y\in\mathbb R^{m+1}}
 \|\nabla_y b_m(y,A_0)\|_1
 \leq C(1+L)\exp\{C T(1+L)\},
 \qquad L=|A_0|+\pi T/2,                                  \tag{5.2}
\]
where \(C\) depends only on \(K\), not on \(h,m\), or \(C^{-1}\).

To prove (5.2), take an arbitrary perturbation \(\dot y\) with
\(\|\dot y\|_\infty\leq1\), and differentiate (5.1):
\[
 \begin{aligned}
 \dot z_k&=\dot y_k+h\sum_{s<k}C_{sk}\dot b_s,\\
 \dot A_k&=h\sum_{s<k}d(z_s)\dot z_s,\\
 \dot b_k&=d(z_k)\dot A_k+A_kd'(z_k)\dot z_k.
 \end{aligned}                                             \tag{5.3}
\]
Since \(|A_k|\leq L\), \(|d|\leq1\), and \(|d'|\leq1\), putting
\(u_k=|\dot z_k|+|\dot A_k|\) gives
\[
 u_k\leq1+hC(1+L)\sum_{s<k}u_s.                           \tag{5.4}
\]
The discrete Gronwall lemma yields
\(u_k\leq\exp\{CT(1+L)\}\), and the last line of (5.3) gives (5.2), by the duality
\(\|\nabla b_m\|_1=\sup_{\|\dot y\|_\infty\leq1}|D b_m[\dot y]|\).

Now average over the Gaussian row variables and the endpoint mark.  Gaussian
integration by parts, valid also for singular \(C\) by writing
\(y=C^{1/2}g\), gives
\[
 c=\mathbb E[y b_m]=C v,
 \qquad v=\mathbb E[\nabla_y b_m].                         \tag{5.5}
\]
If \(x\in\operatorname{Ran}C\), (3.2) and (5.5) imply
\[
 \mathcal P_m(x)=x^{\mathsf T}C^\dagger Cv=x^{\mathsf T}v. \tag{5.6}
\]
Consequently, for every \(x\) with \(\|x\|_\infty\leq\pi/2\),
\[
 |\mathcal P_m(x)|
 \leq {\pi\over2}\,\mathbb E\|\nabla_yb_m\|_1
 \leq C_T.                                                \tag{5.7}
\]
The last constant is finite and mesh-uniform because a Gaussian \(A_0\) has
\(\mathbb E\exp(\lambda|A_0|)<\infty\) for every fixed \(\lambda\).

The range condition is harmless.  For an empirical Gram matrix it follows from
\(\operatorname{Ran}(X^{\mathsf T}X)=\operatorname{Ran}(X^{\mathsf T})\), so every
feature-coordinate history is in the range.  For a population covariance, if
\(a\in\ker C\), then \(\mathbb E(a^{\mathsf T}X)^2=0\), hence
\(a^{\mathsf T}X=0\) almost surely.

### Consequence for the ordered limit

Suppose the previously established fixed-mesh row/column cavity expansion has the
form
\[
 f_{j,m}=\xi_{j,m}+\mathcal P_m(X_{2,j}^{0:m})
          +R_{n,h,p},
 \qquad \|R_{n,h,p}\|_p\longrightarrow0                 \tag{5.8}
\]
for every fixed \((h,p)\).  Then (5.7) and the Gaussian innovation estimate give
\[
 \limsup_{n\to\infty}\|f_{j,m}\|_p
 \leq C_T\sqrt p+C_T\leq C_Tp,                           \tag{5.9}
\]
uniformly in the mesh.  This is sufficient for the ordered limit
\(n\to\infty\) first and \(h\to0\) second.

At finite \(n\), conditioning on the endpoint marks leaves an empirical average of
the right side of (5.2), whose high-\(p\) norm is not uniform.  This is not a defect
for (5.9): at each fixed \((p,h)\), the row law of large numbers is taken before the
mesh limit.  The only fact that must still be checked against the exact conditioning
recursion is that every dependence of the removed top row on the lower feature
history is indeed contained in the fixed-mesh remainder in (5.8).  If the ordered
row/column cavity audit has already established that statement, then no
gauge-gradient estimate is needed for the leading term.

## 6. Audit of feature freezing: the order-one transpose return

The last proviso in Section 5 is substantive.  Deleting one top row changes every
coordinate of \(R_2\) in the direction of that same Gaussian row.  When the changed
hidden feature is fed back through the static row, a normalized quadratic form
survives.  Thus the frozen recursion (5.1) needs an Onsager-response kernel.

Write the deleted top row as
\[
 \Gamma_{2,i:}=g^{\mathsf T}/\sqrt n,
 \qquad g\sim N(0,I_n),
\]
and let superscript \(c\) denote the row-deleted cavity flow.  At time zero the
hidden feature \(X_2^0\) is independent of this row.  Put
\(b_0=A_i^0d(z_{3,i}^0)\).  Since \(P_2^0=0\),
\[
 \delta R_2^0={b_0\over\sqrt n}g,
 \qquad
 \delta B_2^0={b_0\over\sqrt n}D_0g,
 \quad D_0=\operatorname{diag}d(Z_2^0).                   \tag{6.1}
\]
Let \(E_0\) be the exact diagonal divided derivative of
\(r\mapsto\arctan(\iota(r))\) between the cavity and full first Euler states, and
let \(\widehat D_1\) be the corresponding divided derivative of \(\arctan\) at
the second hidden preactivation.  Directly differentiating one Euler step (using
divided differences, so this is an exact finite difference) gives
\[
 \delta X_1^1={h b_0\over\sqrt n}
       E_0(W_1^0)^*D_0g,                                  \tag{6.2}
\]
\[
 \delta Z_2^1={h b_0\over\sqrt n}
 \left[W_1^{1,c}E_0(W_1^0)^*D_0+\rho_{1,0}D_0\right]g,    \tag{6.3}
\]
and hence
\[
 \delta X_2^1={h b_0\over\sqrt n}L_{10}^{(n)}g,
 \quad
 L_{10}^{(n)}:=\widehat D_1
 \left[W_1^{1,c}E_0(W_1^0)^*D_0+\rho_{1,0}D_0\right].     \tag{6.4}
\]
The second summand in (6.3) is exactly the contribution of
\(\delta P_1^1=h\delta B_2^0\otimes X_1^0\).

Now evaluate the reinserted top-row preactivation at time one.  Its learned-row
part is the frozen Gram contribution
\(h b_0\langle X_2^0,X_2^{1,c}\rangle_n+o_{L^p,n}(1)\), but its static part contains
\[
 \Gamma_{2,i:}\delta X_2^1
   =h b_0,{1\over n}g^{\mathsf T}L_{10}^{(n)}g.           \tag{6.5}
\]
After the usual entry/two-row cavity replacement in the coefficients of
\(L_{10}^{(n)}\), conditional Hanson--Wright gives
\[
 {1\over n}g^{\mathsf T}L_{10}^{(n)}g
   ={1\over n}\operatorname{tr}L_{10}+o_{L^p,n}(1)
   =:\tau_{10}+o_{L^p,n}(1).                              \tag{6.6}
\]
Therefore the correct leading scalar equation is already, at \(k=1\),
\[
 z_{3,i}^1=y_1^c+h b_0\bigl(C_{01}+\tau_{10}\bigr)
             +o_{L^p,n}(1).                              \tag{6.7}
\]
The term \(\tau_{10}\) is genuinely extra; it is not part of the feature Gram
\(C_{01}\).  At this first step it is bounded because (6.4) is a product of bounded
diagonal gates and bounded one-step operators.  Its Ginibre-sandwich part has the
expected positive trace structure (when \(\iota'\geq0\)); learned \(O(h)\) pieces
need not have a sign.

### The first two-step trace word

At time one, removal of row \(i\) changes \(R_2^1\) in two leading ways.  The direct
row contribution is \(b_1g/\sqrt n\).  The response of all the other top rows to
\(\delta X_2^1\) is
\[
 K_1\delta X_2^1,
 \qquad
 K_1=(W_2^{1,c})^*
       \operatorname{diag}\!\bigl(A^{1,c}d'(Z_3^{1,c})\bigr)
       W_2^{1,c}.                                         \tag{6.8}
\]
At this step (6.8) is exact for the cavity rows: \(A^1\) and \(W_2^1\) depend only
on time-zero features, which were not changed.  Contributions from the learned
part of the removed row are smaller by \(n^{-1/2}\).  Thus
\[
 \sqrt n\,\delta R_2^1
   =b_1g+h b_0K_1L_{10}g+o_{L^p,n}(1).                    \tag{6.9}
\]

Let \(L_{21}\) be the one-step lower response from a time-one perturbation of
\(R_2\) to \(X_2^2\), and let \(L_{20}^{\rm prop}\) contain propagation of the
already stored time-zero lower-state perturbation, excluding (6.8).  Then
\[
 \sqrt n\,\delta X_2^2
 =h b_1L_{21}g+h b_0L_{20}^{\rm prop}g
   +h^2b_0L_{21}K_1L_{10}g+o_{L^p,n}(1).                 \tag{6.10}
\]
Consequently the two augmented kernels are
\[
 \begin{aligned}
 \Theta_{12}&={1\over n}\operatorname{tr}L_{21},\\
 \Theta_{02}&={1\over n}\operatorname{tr}L_{20}^{\rm prop}
  +h\,{1\over n}\operatorname{tr}(L_{21}K_1L_{10}).
 \end{aligned}                                            \tag{6.11}
\]
The last normalized trace is the first genuinely new feedback word.  It is not
positive in general because \(A^1d'(Z_3^1)\) changes sign.

### Correct augmented scalar Volterra equation

Iterating the same calculation gives, at each fixed mesh and after the ordered
cavity replacements,
\[
 \boxed{
 z_{3,i}^k=y_k^c+h\sum_{s<k}b_s
             \bigl(C_{sk}+\Theta_{sk}\bigr)
             +o_{L^p,n}(1).
 }                                                         \tag{6.12}
\]
Here \(\Theta_{sk}\) is the normalized trace of the full causal cavity response
from an isotropic perturbation of \(R_2^s\) to \(X_2^k\).  It includes alternating
lower and top response blocks; every additional return carries an additional
Euler factor \(h\).  The off-column fluctuations around these traces are precisely
the centered quadratic/bilinear forms handled by the ordered-limit cavity
remainder.  The trace itself is leading.

The proof of the Volterra lemma in Section 5 is unchanged with
\(C_{sk}\) replaced by \(C_{sk}+\Theta_{sk}\), provided
\[
 \sup_{s<k\leq T/h}|\Theta_{sk}|\leq C_T.                 \tag{6.13}
\]
Thus feature freezing does not destroy the signed endpoint strategy; it moves its
make-or-break estimate from a gauge-gradient norm to the normalized causal trace
(6.13).

### Why the trace structure is potentially sufficient

The endpoint factor in (6.8) must not be bounded by its operator norm.  Cyclicity
of trace gives, for bounded response blocks \(L,L'\),
\[
 \left|{1\over n}\operatorname{tr}
   \bigl(L(W_2)^*\operatorname{diag}(A d')W_2L'\bigr)\right|
 \leq C\,{1\over n}\sum_i|A_i|,                          \tag{6.14}
\]
where \(C\) uses the operator norms of \(W_2,L,L'\) and \(|d'|\leq1\).
For a word with \(r\) endpoint diagonal insertions, normalized noncommutative
Holder gives
\[
 |\operatorname{tr}_n(M_0D(A^{t_1})M_1\cdots
             D(A^{t_r})M_r)|
 \leq C^r\,{1\over n}\sum_i
       \bigl(|A_i^0|+C_T\bigr)^r.                         \tag{6.15}
\]
The sum over ordered insertion times contributes at most \(T^r/r!\).  Since
\(\mathbb E(|A_0|+C_T)^r\leq C_T^r r^{r/2}\),
\[
 \sum_{r\geq0}{(C_TT)^r r^{r/2}\over r!}<\infty.         \tag{6.16}
\]
Hence endpoint Gaussian marks are compatible with an arbitrary-time trace-Dyson
bound, even though the corresponding pathwise operator norm uses
\(\max_i|A_i^0|\) and is useless.

For the lower propagators, the raw linearization contains
\(R_2d'(Z_2)\).  The exact arctan characteristic replaces its principal part by
the dressed bath multiplier \(-(d'/d)\beta\), plus the already identified Euler
defect.  Therefore (6.13) follows from the trace-Dyson argument if the dressed bath
diagonals have Gaussian moment growth under the simultaneous row/column cavity and
all remaining response blocks have bounded operator norm.  If an undressed
predictor-amplitude diagonal survives that reduction, (6.15)--(6.16) do not apply;
that is now the precise obstruction to check.  In particular, the off-diagonal
bath is not itself a leading random matrix after the two-row cavities: its centered
part is in \(o_{L^p,n}(1)\), while its normalized trace/Stein compensator is retained
inside \(\Theta\).

## 7. Characteristic-dressed lower generator and the exact remaining leaf

This section performs the hostile check left open above.  The conclusion is mixed:
the instantaneous factor \(R_2d'(Z_2)\) cancels exactly, and all endpoint/static
Gaussian diagonal insertions admit the proposed Schatten--Dyson summation.  A
learned-bath insertion \(P_1V_1\), however, survives the dressing and is not
controlled by the endpoint envelope.  Thus (6.13) is reduced to one explicit
lower-layer Abel problem, not proved outright.

### 7.1 Exact dressed Euler tangent

The exact state increments at the second hidden layer are
\[
 Z^{k+1}-Z^k=h\{\beta_k+\rho_{1,k}d(Z^k)R^k\},
 \qquad \beta_k=W_1^kV_1^k,                               \tag{7.1}
\]
\[
 R^{k+1}-R^k=h\{\gamma_k+\rho_{3,k}\arctan Z^k\},
 \qquad \gamma_k=(W_2^k)^*F_3^k.                         \tag{7.2}
\]
Consider the leading cavity tangent; variations of the normalized scalar
correlations are lower-order trace/cavity terms and are put in the source.  Write
\(\zeta_k=\delta Z^k\), \(S_k=\delta R^k\), and
\(d_k=d(Z^k)\).  Then
\[
 \begin{aligned}
 \zeta_{k+1}&=\zeta_k+h\rho_{1,k}
   \{d_kS_k+R^kd'_k\zeta_k\}+h\,\delta\beta_k,\\
 S_{k+1}&=S_k+h\rho_{3,k}d_k\zeta_k+h\,\delta\gamma_k.
 \end{aligned}                                           \tag{7.3}
\]
Set \(\eta_k=\zeta_k/d_k\).  A direct subtraction, with no Taylor expansion,
gives
\[
 \begin{aligned}
 \eta_{k+1}={}&\eta_k
 +h\rho_{1,k}{d_k\over d_{k+1}}S_k
 +{h\over d_{k+1}}\delta\beta_k\\
 &-h{d'_k\over d_{k+1}}\beta_k\eta_k
 +e_k\eta_k,                                             \tag{7.4}\\
 S_{k+1}={}&S_k+h\rho_{3,k}d_k^2\eta_k+h\delta\gamma_k,
                                                               \tag{7.5}
\end{aligned}
\]
where
\[
 e_k={d'_k\Delta Z_k-(d_{k+1}-d_k)\over d_{k+1}}.         \tag{7.6}
\]
Indeed, the coefficient of \(\eta_k\) before the last rewrite is
\[
 {h\rho_{1,k}R^kd_k(d'_k-Dd_k)-hDd_k\beta_k\over d_{k+1}};
\]
using \(\Delta Z_k=h(\rho_{1,k}d_kR^k+\beta_k)\) reduces it
exactly to the last two terms in (7.4).  Thus no factor \(R^kd'_k\) remains.

For \(d(z)=(1+z^2)^{-1}\), (7.6) has the explicit form
\[
 e_k={ (\Delta Z_k)^2
   \{1-3(Z^k)^2-2Z^k\Delta Z_k\}
   \over (1+(Z^k)^2)^2}.                                 \tag{7.7}
\]
On paths whose Euler increments tend uniformly to zero, this has total variation
controlled by \(\sum_k|\Delta Z_k|^2\).  More explicitly, if
\(\Delta Z_k=h\dot Z_k\) and the normalized velocity energy satisfies
\(h\sum_k\mathbb E\|\dot Z_k\|_n^2\leq C_T\), exchangeability gives, for a fixed
coordinate \(j\),
\[
 \mathbb E\sum_k|\Delta Z_{k,j}|^2\leq C_Th,
 \qquad
 \mathbb P\{\max_k|\Delta Z_{k,j}|>\varepsilon\}
 \leq C_Th/\varepsilon^2.                                \tag{7.7a}
\]
On the complementary good event, (7.7) is at most
\(C(1+\varepsilon)\sum_k|\Delta Z_{k,j}|^2\).  Its total contribution therefore
tends to zero in probability as \(h\downarrow0\).  It may be discarded before
applying lower semicontinuity to a subsequential limiting law.  In particular,
(7.7) is an Euler defect, not a principal diagonal mark.

Passing formally to the limiting generator (or retaining (7.4) on the good-increment
set), the homogeneous dressed block is
\[
 \mathcal G_k=
 \begin{pmatrix}
  -a(Z^k)\beta_k&\rho_{1,k}I\\
  \rho_{3,k}d(Z^k)^2&0
 \end{pmatrix},
 \qquad a={d'\over d}={-2z\over1+z^2},\quad |a|\leq1.    \tag{7.8}
\]
This is the promised exact disappearance of \(R_2\) from the principal generator.

### 7.2 Every safe diagonal insertion and its empirical moments

There are two safe unbounded diagonal marks.

First, every top feedback Hessian has the form
\[
 (W_2)^*D(A^kd'(Z_3^k))W_2,
 \qquad A_i^k=A_i^0+s_i^k,quad |s_i^k|\leq \pi T/2.      \tag{7.9}
\]
For every \(r\geq2\), Minkowski and the Gaussian moment formula give
\[
 \begin{aligned}
 \|A^k\|_{S_r,n}
 &=\left({1\over n}\sum_i|A_i^k|^r\right)^{1/r}\\
 &\leq\left({1\over n}\sum_i|A_i^0|^r\right)^{1/r}
       +\pi T/2
 \longrightarrow (\mathbb E|G|^r)^{1/r}+\pi T/2
 \leq C_T\sqrt r.                                       \tag{7.10}
\end{aligned}
\]
This uses only the Gaussian endpoint and its bounded shift.

Second, split the lower bath as
\[
 \beta_k=\Gamma_1V_1^k+P_1^kV_1^k=:g_k+p_k.              \tag{7.11}
\]
After deleting a row of \(\Gamma_1\), the leading static part is conditionally
Gaussian.  If \(\sigma_k=\|V_1^k\|_n\), then for any fixed collection of times,
rowwise Gaussian Holder and the row law of large numbers yield
\[
 \|g_k\|_{S_r,n}\longrightarrow
   \sigma_k(\mathbb E|G|^r)^{1/r}leq C\sigma_k\sqrt r.   \tag{7.12}
\]
The time envelope is integrable using only the velocity energy:
\[
 h\sum_{k<T/h}\sigma_k
 \leq \sqrt T\left(h\sum_k\|V_1^k\|_n^2\right)^{1/2}
 \leq C_T.                                                \tag{7.13}
\]
All gates \(a,d^2\), correlations \(\rho\), and the characteristic source/end maps
on the good-increment set are bounded operators.  These are the complete safe
insertions after the row/entry cavity removes centered off-diagonal pieces.

### 7.3 Normalized Schatten--Dyson summation for the safe generator

Expand a causal response kernel in time-ordered insertions of (7.9) and the static
part (7.12); bounded maps between insertions are denoted by \(M_q\).  For a word
with \(r\) diagonal marks \(D(m_q)\), normalized noncommutative Holder gives
\[
 \left|\operatorname{tr}_n
  (M_0D(m_1)M_1\cdots D(m_r)M_r)\right|
 \leq C^r\prod_{q=1}^r\|m_q\|_{S_r,n}.                  \tag{7.14}
\]
Equations (7.10)--(7.13), followed by ordinary Holder for the joint Gaussian row
marks, bound the right side by
\[
 (C_T\sqrt r)^r\prod_{q=1}^r\kappa(t_q),
 \qquad \int_0^T\kappa(t)\,dt\leq C_T.                  \tag{7.15}
\]
There are at most \(C^r\) choices of insertion type.  The ordered time simplex has
mass at most \((\int\kappa)^r/r!\).  Hence the full safe series is bounded by
\[
 \sum_{r\geq0}{(C_T)^r r^{r/2}\over r!}<\infty,          \tag{7.16}
\]
because Stirling gives an \(r\)-th root asymptotic \(C_Te/\sqrt r\).
It follows, for the generator with \(p_k\) deleted, that
\[
 \sup_{m,s\leq T/h}|\Theta^{\rm safe}_{ms}|\leq C_T,
 \qquad
 \sup_m h\sum_{s<m}|\Theta^{\rm safe}_{ms}|\leq TC_T.  \tag{7.17}
\]
Endpoint/source maps add only finitely many bounded factors and do not alter the
series.

### 7.4 The smallest undressed factor

The learned part in (7.11) is exactly
\[
 p_{k,j}=(P_1^kV_1^k)_j
   =h\sum_{u<k}B_{2,j}^u\,
      \langle X_1^u,V_1^k\rangle_n.                      \tag{7.18}
\]
It is multiplied in (7.8) by the bounded diagonal \(a(Z_2^k)\), but (7.18) has no
endpoint-Gaussian envelope.  Cauchy--Schwarz gives only
\[
 |p_{k,j}|
 \leq C_T\|V_1^k\|_n
       \left(h\sum_{u<k}|B_{2,j}^u|^2\right)^{1/2}.       \tag{7.19}
\]
Energy controls the empirical \(L^2\) norm of the last factor, not its empirical
\(L^r\) norm.  Since
\[
 B_{2,j}^u=d(Z_{2,j}^u)
  \left\{\Gamma_{2,:j}^{\mathsf T}B_3^u
         +(P_2^u)_{:j}^{\mathsf T}B_3^u\right\},          \tag{7.20}
\]
and the learned term in braces is bounded while the first term is the predictor
under study, (7.19) is circular for \(r>2\).

This factor occurs at the first possible mesh time.  Since
\(P_1^1=hB_2^0\otimes X_1^0\),
\[
 p_{1,j}=hB_{2,j}^0\langle X_1^0,V_1^1\rangle_n.          \tag{7.21}
\]
The time-one dressed step therefore contains the diagonal word
\[
 -h^2\langle X_1^0,V_1^1\rangle_n\,
   D\!\left(a(Z_2^1)B_2^0\right),                        \tag{7.22}
\]
between the incoming and outgoing lower response maps.  It is gauge invariant and
has a nonzero normalized trace in general; row centering does not remove it.

Using \(hV_1^k=X_1^{k+1}-X_1^k\), an Abel transform of a single insertion gives
boundary terms involving
\[
 h\sum_u B_2^u\langle X_1^u,X_1^m-X_1^{u+1}\rangle_n,    \tag{7.23}
\]
plus coefficient-difference terms.  Unlike the corresponding top-layer boundary,
where \(|B_3|\leq|A_0|+C_T\), (7.23) still contains \(B_2\).  Applying Abel again
to the coefficient differences regenerates (7.18); it does not terminate from the
present identities.

Accordingly, (7.22) is the smallest exact open leaf.  The hostile check has shown
that \(\phi''(Z_2)R_2\) does **not** survive as an instantaneous curvature factor;
it is replaced by the static Gaussian bath, which is safe, the Euler defect (7.7),
and the learned causal bath (7.18).  The claimed arbitrary-time trace closure is
proved for all other insertions, but proving (6.13) still requires a signed estimate
for (7.18)/(7.23), or an additional identity which cancels it.

## 8. Candidate signed trace expansion of the learned bath (superseded by Section 9)

**Status warning.**  The one-petal identity below is correct, but the claimed
one-open-spine closure in Sections 8.2--8.4 is not established.  The hostile audit
in Section 9 exhibits a leading same-block second-variation graph which is not
covered by the distinct-block cavity remainder.  Sections 8.2--8.4 should therefore
be read only as the closure that would follow if that graph admitted an additional
factorization/cancellation.

The obstruction in Section 7 results from estimating the learned bath before using
the Gaussian sign in \(B_2\).  At the level of a normalized trace, the static part
of \(B_2\) has a useful one-edge Stein recurrence.  Under the ordered-limit cavity
statement (all non-cactus mixed row/entry remainders are \(o_n(1)\) at fixed mesh),
this recurrence closes the remaining trace kernel.

### 8.1 One-petal recurrence

Consider one learned-bath insertion inside a cyclic response word.  By cyclicity it
has the form
\[
 \operatorname{tr}_n\{Q D(a_kP_1^kV_1^k)\}
 =h\sum_{u<k}c_{uk}\,
   \operatorname{tr}_n\{Q D(a_kB_2^u)\},
 \quad c_{uk}=\langle X_1^u,V_1^k\rangle_n.              \tag{8.1}
\]
Put \(q_j=Q_{jj}\).  The learned part of \(R_2^u\) is safe:
\[
 ((P_2^u)_{:j})^{\mathsf T}B_3^u
 =h\sum_{v<u}X_{2,j}^v\langle B_3^v,B_3^u\rangle_n,
 \qquad \sup_j|\cdot|\leq C_T(\|A^0\|_n+C_T)^2.         \tag{8.2}
\]
For the static part define
\[
 w_j=q_j a(Z_{2,j}^k)d(Z_{2,j}^u),
 \qquad
 \mathcal J_u(w)=\operatorname{tr}_nD(w)D(\Gamma_2^*B_3^u)
                 =\langle \Gamma_2w,B_3^u\rangle_n.     \tag{8.3}
\]

Delete top row \(i\) and hidden column \(j\) from the coefficients of \(w\), as in
the fixed-mesh two-row/entry cavity.  Gaussian integration by parts in
\(\Gamma_{2,ij}\), whose variance is \(1/n\), gives the exact leading recurrence
\[
 \begin{aligned}
 \mathbb E\mathcal J_u(w)
 ={}&{1\over n^2}\sum_{i,j}
       \mathbb E\{(\partial_{ij}B_{3,i}^u)w_j\}\\
 &+{1\over n^2}\sum_{i,j}
       \mathbb E\{B_{3,i}^u\partial_{ij}w_j\}+o_n(1).    \tag{8.4}
\end{aligned}
\]
Let \(Y_i^\ell=(\Gamma_2X_2^\ell)_i\), and let
\(\bar q_{u\ell}=n^{-1}\sum_i
\mathbb E[\partial_{Y_i^\ell}B_{3,i}^u]\) be the signed top-row response
coefficient.  The direct part of the first line of (8.4) is
\[
 \sum_{\ell\leq u}\bar q_{u\ell}
       \langle w,X_2^\ell\rangle_n.                     \tag{8.5}
\]
All derivatives of the scalar top-row learned history are included in
\(\bar q\); the exact scalar Volterra recursion from Section 5 derives (8.5), with
\(C\) replaced by the augmented kernel \(C+\Theta\).

The second line of (8.4), together with the pieces of
\(\partial_{ij}B_{3,i}^u\) which differentiate the lower feature history, has a
different role: \(\partial_{ij}\) lands on one gate or one propagator in \(Q\).
The product rule gives a sum over possible landing sites, but each summand contains
exactly one marked derivative.  Causality forces this marked derivative to a time
strictly earlier than the feature it differentiates (\(X_2^0\) is independent of
\(\Gamma_2\)); hence it carries an Euler factor \(h\).  This is the return term
\[
 \mathcal R_u(w)={1\over n^2}\sum_{i,j}
       \mathbb E\{B_{3,i}^u\partial_{ij}w_j\},            \tag{8.6}
\]
which is the same open causal susceptibility at an earlier time, decorated by
bounded gates and a closed \(B_3\)-correlation.  Equations (8.4)--(8.6) are the
leading Gaussian-pairing/Stein recurrence requested for one petal.

There are therefore exactly three outcomes when (8.4) is iterated:

1. two fresh outgoing Gaussian edges are paired; their two \(B_3\) marks enter only
   through \(\langle B_3^v,B_3^u\rangle_n\), bounded by the endpoint \(L^2\)
   envelope;
2. an edge differentiates a top-row value, producing (8.5), ultimately exposing
   \(A_i^0\) plus its bounded shift;
3. an edge differentiates the core, producing (8.6), one extra causal \(h\), and
   one earlier copy of the same open susceptibility.

Stopping after replacing \(\Gamma_2^*B_3\) by its predictable value would obscure
this trichotomy and create the uncontrolled diagonal norm in (7.19).

### 8.2 Why only one open spine is produced

Mark the source and endpoint indices of the response trace.  In (8.4), a derivative
can land at many sites, but in each product-rule summand it lands at only one site.
If a Gaussian contraction cuts the cyclic index word, precisely one resulting
component contains the two marked response endpoints; every other component is a
closed normalized trace.  Inductively, every leading graph is therefore a collection
of closed cactus petals attached to one open spine.  A graph with two marked open
components requires a second mixed row/entry difference and belongs to the
\(o_n(1)\) fixed-mesh remainder.

This statement can also be checked directly by index counting: a leading covariance
identification removes one Gaussian factor \(n^{-1/2}\), one free index sum, and
adds its variance \(n^{-1}\), preserving the Euler characteristic of a cactus.
A crossing or a second independently open path loses at least one free index and is
\(O(n^{-1})\) before the fixed-mesh sensitivity constants.  The ordered limit sends
it to zero.

Consequently the return term is linear in the open susceptibility.  It never yields
a product of two unresolved open responses.  Closed side components may be summed
first.

### 8.3 The surviving backtracking cacti are summable

An \(r\)-petal learned-bath cactus has \(r\) ordered generator times \(k_a\) and
one history time \(u_a<k_a\) for each petal.  Each petal contributes
\(h^2c_{u_ak_a}\).  Ignoring harmless velocity envelopes, the total time volume is
bounded by
\[
 {1\over r!}\left({T^2\over2}\right)^r.                 \tag{8.7}
\]
The history times need not be mutually ordered; (8.7), rather than a fictitious
\((2r)!^{-1}\), is the correct worst case.

Gauge parity does not kill these cacti: both \(a(Z_{2,j}^{k_a})\) and
\(B_{2,j}^{u_a}\) change sign, so each petal is invariant.  Their size is nevertheless
safe after the full recurrence (8.4).  For each original outgoing Gaussian edge,
one either uses a Gaussian pairing or exposes one endpoint mark; it cannot do both.
Thus a cactus with \(r\) petals has at most \(r\) Gaussian/endpoint carriers in
total.  Joint Gaussian Holder and (7.10) give the carrier factor
\[
 (C_T\sqrt r)^r.                                         \tag{8.8}
\]
Leading rooted plane cacti are counted by at most \(C^r\) (the Catalan bound).  The
sum of all closed \(r\)-petal decorations is consequently bounded by
\[
 C_r(T)\leq { (C_TT^2)^r r^{r/2}\over r!}.               \tag{8.9}
\]
The series \(\sum_rC_r(T)\) converges for every \(T\), since its \(r\)-th root is
\(O(C_Te/\sqrt r)\).

The apparently dangerous all-predictable star is included in this count.  If one
first writes \(F_j^u=\xi_j^u+\mathcal P_u(X_{2,j})\), it appears as
\(n^{-1}\sum_j\prod_a\mathcal P_{u_a}(X_{2,j})\).  In the complete Stein expansion,
each factor is instead resolved by (8.4): a local top response gives (8.5), while a
feature derivative moves the unique open mark backward.  Hence no power of an
unestimated predictor remains as an atomic diagram.

### 8.4 Linear Volterra closure of the open spine

Let \(K_{m\ell}\) denote the sum of all closed cactus decorations before the next
return of the marked derivative to the open spine.  Equations (8.7)--(8.9), with
the velocity envelope controlled by (7.13), give
\[
 \sup_{m,\ell\leq T/h}|K_{m\ell}|\leq C_T,
 \qquad
 \sup_mh\sum_{\ell<m}|K_{m\ell}|\leq C_T.                \tag{8.10}
\]
The exact causal recurrence for the open trace has the form
\[
 |\Theta_{ms}|
 \leq C_T+h\sum_{s\leq\ell<m}|K_{m\ell}|\,|\Theta_{\ell s}|
      +o_n(1)+o_h(1),                                    \tag{8.11}
\]
where the first term includes the safe generator of Section 7, (8.2), and endpoint
maps; \(o_h(1)\) is the Euler defect (7.7).  Subdivide \([0,T]\) if necessary so
that the row sum in (8.10) is less than \(1/2\) on each slab, or apply the standard
discrete Volterra resolvent.  This gives
\[
 \sup_{m,s\leq T/h}|\Theta_{ms}|\leq C_T,
 \qquad
 \sup_mh\sum_{s<m}|\Theta_{ms}|\leq C_T,                 \tag{8.12}
\]
uniformly in the mesh after \(n\to\infty\).

Combining (8.12) with the augmented scalar Volterra lemma gives the bounded signed
endpoint predictor (5.7), and therefore the coordinatewise \(C_Tp\) bound in the
ordered limit.

The only structural hypothesis used beyond the displayed Euler identities is the
fixed-mesh ordered-cavity fact already isolated earlier: graphs requiring a second
independently open row/entry difference are \(o_n(1)\).  Without that fact, the
first nonabsorbable object would be a two-open-spine (theta) graph arising from a
third mixed row/entry derivative; with it, no such leading diagram remains.

## 9. Hostile audit of the cactus claim: a leading theta susceptibility

This section corrects the last sentence of Section 8.  The first theta graph uses
the **same** row/column block as the learned-bath petal.  It is a second variation
of the flow, not a mixed derivative across two independent cavity blocks, and its
normalized index sum is leading.

### 9.1 Differentiating a propagator creates two response factors

Let \(\mathsf S_k\) denote the full characteristic-dressed cavity state, let
\(L_k=D\Phi_k(\mathsf S_k)\) be its one-step tangent, and write
\[
 U_{m,s}=L_{m-1}\cdots L_s.
\]
For a static entry \(\Gamma_{2,ij}\), set
\(H_v^{ij}=\partial_{ij}\mathsf S_v\).  The exact product rule is
\[
 \partial_{ij}U_{m,s}
 =\sum_{v=s}^{m-1}U_{m,v+1}
    \left\{h(D_{\mathsf S}\mathcal G_v)[H_v^{ij}]
           +h\partial_{ij}^{\rm exp}\mathcal G_v\right\}
       U_{v,s},                                           \tag{9.1}
\]
where \(L_v=I+h\mathcal G_v\); the same formula with exact divided derivatives
holds for the Euler map.

Insert (9.1) into the second line of the one-petal Stein recurrence (8.4).  A
representative state-derivative contribution is
\[
 \boxed{
 \mathfrak T=
 {h^3c_{uk}\over n^2}\sum_{i,j}\sum_{v}
 \mathbb E\!\left[
 B_{3,i}^u,e_j^{\mathsf T}U_{m,v+1}
 (D_{\mathsf S}\mathcal G_v)[H_v^{ij}]
 U_{v,s}e_j\right].
 }                                                         \tag{9.2}
\]
Two of the displayed powers of \(h\) are the generator/history factors of the
learned-bath petal; the third is from (9.1).  Formula (9.2) contains the original
response \(U_{v,s}\) and the disorder-to-state response \(H_v^{ij}\), coupled by a
Hessian.  It is therefore a second-order, two-response trace, even though there is
only one Gaussian integration-by-parts derivative.

### 9.2 Exact index scaling: (9.2) is not an \(o_n(1)\) graph

At initialization, before learned terms are present,
\[
 R_{2,\ell}^0=\sum_r\Gamma_{2,r\ell}B_{3,r}^0,
 \qquad B_{3,i}^0=A_i^0d(Z_{3,i}^0).
\]
Since \(X_2^0\) is independent of \(\Gamma_2\), direct differentiation gives
\[
 \partial_{ij}R_{2,\ell}^0
 =\delta_{\ell j}B_{3,i}^0
  +\Gamma_{2,i\ell}A_i^0d'(Z_{3,i}^0)X_{2,j}^0.          \tag{9.3}
\]
The first term is localized: its normalized vector norm is \(O(n^{-1/2})\), but
its \(j\)-th coordinate is order one.  After one lower Euler response,
\(H_v^{ij}\) still has a \(j\)-coordinate of size \(hB_{3,i}^0\) times a bounded
one-step susceptibility.  Therefore a summand in (9.2), after removal of its
explicit Euler factors, is order one for each \((i,j)\).  The normalization
\(n^{-2}\) is exactly canceled by the \(n^2\) choices of \((i,j)\):
\[
 {1\over n^2}\sum_{i,j}
 (B_{3,i}^0)^2\,[\hbox{localized lower response at }j]
 \longrightarrow
 \mathbb E(B_3^0)^2\,\Xi,                                \tag{9.4}
\]
where \(\Xi\) is a normalized second-order response trace.  There is no residual
negative power of \(n\).

Thus (9.2) is not a graph with two independent open cavity blocks.  Both response
factors use the same \((i,j)\) source, and the leverage atom \(e_j\) defeats the
Hilbert--Schmidt scaling which would hold for an independent second block.

### 9.3 The exact new unknown

After the safe top-index average in (9.4), the remaining object has the schematic
form
\[
 \Xi_{m,v,s}
 ={1\over n}\sum_j e_j^{\mathsf T}U_{m,v+1}
  (D_{\mathsf S}\mathcal G_v)
       [\,U_{v,u}e_j\,]
  U_{v,s}e_j.                                             \tag{9.5}
\]
All arctan curvature amplitudes in \(D_{\mathsf S}\mathcal G\) are dressed: for
example, differentiating the principal lower diagonal gives
\[
 D\{-a(Z_2)\beta\}[H]
 =-a'(Z_2)H_Z\,\beta-a(Z_2)H_\beta,                       \tag{9.6}
\]
and differentiating the off-diagonal gate gives
\(2d(Z_2)d'(Z_2)H_Z\).  No naked \(R_2d'(Z_2)\) reappears.  Nevertheless (9.5)
is bilinear in two response factors and is not determined by the first normalized
trace \(\Theta=n^{-1}\operatorname{tr}U\).  Bounding it by absolute values asks for
a squared-gradient/Frobenius response energy, precisely the estimate which was not
available in the gauge-gradient route.

Differentiating (9.5) generates third variations, so simply adjoining \(\Xi\) to
the state starts an all-orders response hierarchy.  No identity in Sections 2--7
turns (9.5) into a linear Volterra convolution of \(\Theta\).

### 9.4 Direct hits on explicit disorder are safe but have no extra time gain

If the derivative in (8.4) hits an explicit \(W_2\) in
\(K=(W_2)^*D(A d')W_2\), then
\[
 \partial_{ij}^{\rm exp}K
 =e_je_i^{\mathsf T}D(A d')W_2
  +(W_2)^*D(A d')e_ie_j^{\mathsf T}.                      \tag{9.7}
\]
This is a Gaussian pairing/rank-one trace term and exposes the safe endpoint mark
\(A^0+\)bounded.  It carries no additional causal \(h\) beyond the two factors
already present in the learned-bath petal.  Thus it is safe, but it cannot be used
to improve the worst-case time volume from \(T^{2r}/r!\) to \(T^{2r}/(2r)!\).

### 9.5 The top-row coefficient is only locally controlled

Let \(V_I\) be the signed top-row response total variation on a slab \(I\) of
length \(\delta\), and put
\[
 M_I=\sup_{t\in I}h\sum_{s\in I,s<t}|\Theta_{ts}|.
\]
Differentiating the augmented scalar Volterra equation gives the local inequality
\[
 V_I\leq C_T(1+V_{<I})+C_T(\delta+M_I)V_I.                \tag{9.8}
\]
Thus \(\bar q_{u\ell}\) in (8.5) is bounded once \(M_I\) is small, but not before.
The one-spine proposal would have supplied
\(M_I\leq C_T\delta(1+V_I)+C_T\delta M_I\).  The actual recurrence contains the
additional term
\[
 M_I\leq C_T\delta(1+V_I)+C_T\delta M_I+C_T\delta\Xi_I.  \tag{9.9}
\]
Consequently (9.8)--(9.9) do not close without a bound for (9.5).  This is the
precise circularity hidden by treating \(\bar q\) as an a priori \(C_T\) coefficient
in Section 8.

### 9.6 Carrier counting must use all generator vertices

The statement “at most \(r\) carriers for \(r\) learned petals” is also too narrow:
safe response words already contain endpoint \(A\) diagonals and static Gaussian
bath diagonals.  If \(N\) denotes the total number of generator/Stein vertices,
then the safe one-spine words have at most \(N\) unbounded carriers and are bounded
by \((C_T\sqrt N)^N/N!\).  Explicit Ginibre matrices are controlled in operator norm
unless consumed by a pairing such as (9.7).  This revised count remains summable for
the safe class.

It does not count the hierarchy generated by (9.5).  The Catalan bound applies to
closed plane cacti after the one-spine property has been proved; it cannot be used
to prove that property.  General second-variation attachments have not been shown
to be Catalan or to possess the same time factorial.

### 9.7 What the fixed-mesh cavity estimate actually removes

The usable ordered-limit statement is the following restricted one.  For each
fixed program length \(m\) and moment order \(p\), a centered graph containing a
mixed finite difference across two **distinct independent** fresh row/entry blocks
has, after row aggregation, an additional \(n^{-1/2}\) factor (with a constant
\(C_{p,m}\)); higher distinct-block differences gain further fixed-mesh powers of
\(n^{-1/2}\).  Hence such graphs vanish when \(n\to\infty\) at fixed \((p,h)\), even
though \(C_{p,m}\) may grow with \(m\).

The source in (9.3) uses the same row \(i\) and column \(j\) in both response
factors.  It is a repeated-block second variation and receives no distinct-cavity
gain.  Therefore the ordered-limit theorem does not cover (9.2).

The corrected verdict is:

* the one-edge Stein recurrence (8.4) and all explicit-disorder pairings are safe;
* closed cacti not involving a state derivative of a propagator have the proposed
  summability;
* the first explicit diagram that is neither an endpoint/pairing nor a proved
  linear Volterra return is the same-block theta susceptibility (9.2)/(9.5).

Closing it would require either an exact second-variation characteristic identity
which reduces (9.5) to first-order traces, or a normalized nuclear/Frobenius estimate
for (9.5) based on signs rather than the failed pathwise bracket bound.

## 10. Exact value-level divided-difference resummation

The all-orders derivative hierarchy in Section 9 is not intrinsic to the top
endpoint.  It is produced by differentiating a bounded nonlinear value instead of
retaining its exact finite difference.  This section gives the corresponding exact
Euler identity.  It is a genuine reduction, but not yet a stability theorem.

Write
\[
 \psi(r)=\arctan(\Theta^{-1}(r)),\qquad
 f[x,y]=\begin{cases}{f(x)-f(y)\over x-y},&x\ne y,\\
 f'(x),&x=y,\end{cases}
\]
and put \(d(z)=(1+z^2)^{-1}\).  For the step \(k\to k+1\), define the diagonal
divided-difference multipliers
\[
 \bar H_1^k=D\psi[r^{k+1},r^k],\qquad
 \bar D_2^k=D\arctan[Z_2^{k+1},Z_2^k],                  \tag{10.1}
\]
\[
 \bar C_3^k=D\!\left(A^k d[Z_3^{k+1},Z_3^k]\right),
 \qquad D_3^{k+1}=D(d(Z_3^{k+1})).                       \tag{10.2}
\]
Here and below \(D(v)\) denotes coordinatewise multiplication by \(v\).  Since
\(\psi\) and arctangent are \(1\)-Lipschitz and \(d'\) is bounded,
\[
 \|\bar H_1^k\|_{\rm op},\|\bar D_2^k\|_{\rm op}\leq1,
 \qquad |\bar C_{3,i}^k|\leq\|d'\|_\infty |A_i^k|.       \tag{10.3}
\]

Set
\[
 c_1^k=\langle X_1^k,X_1^{k+1}\rangle_n,qquad
 c_2^k=\langle X_2^k,X_2^{k+1}\rangle_n,                \tag{10.4}
\]
\[
 \bar L_1^k=c_1^kI+G_1^k\bar H_1^k(G_1^k)^*.            \tag{10.5}
\]
The state updates and the identity \(B_2^k=D_2^kR_2^k\) give, without a
remainder,
\[
 \begin{aligned}
 Z_2^{k+1}-Z_2^k
 &=G_1^k(X_1^{k+1}-X_1^k)
   +(G_1^{k+1}-G_1^k)X_1^{k+1}\\
 &=h\bar L_1^kD_2^kR_2^k,
 \end{aligned}                                           \tag{10.6}
\]
and hence
\[
 X_2^{k+1}-X_2^k
 =h\bar D_2^k\bar L_1^kD_2^kR_2^k.                      \tag{10.7}
\]
The same product-rule ordering at the top layer yields
\[
 Z_3^{k+1}-Z_3^k
 =h\left[c_2^kB_3^k+G_2^k\bar D_2^k\bar L_1^kD_2^kR_2^k\right],             \tag{10.8}
\]
and, because \(A^{k+1}=A^k+hX_3^k\),
\[
 B_3^{k+1}-B_3^k
 =h\left[D_3^{k+1}X_3^k+
 \bar C_3^k\left(c_2^kB_3^k+
 G_2^k\bar D_2^k\bar L_1^kD_2^kR_2^k\right)\right].      \tag{10.9}
\]

Finally use \(G_2^{k+1}=G_2^k+h(B_3^k\otimes X_2^k)\) in
\(R_2^{k+1}=(G_2^{k+1})^*B_3^{k+1}\).  The result is the exact value recursion
\[
 \boxed{R_2^{k+1}=(I+hK_k)R_2^k+hF_k,}                  \tag{10.10}
\]
where
\[
 K_k=(G_2^k)^*\bar C_3^kG_2^k\bar D_2^k
       \bar L_1^kD_2^k,                                  \tag{10.11}
\]
\[
 F_k=X_2^k\langle B_3^k,B_3^{k+1}\rangle_n
 +(G_2^k)^*\left[D_3^{k+1}X_3^k+c_2^k\bar C_3^kB_3^k\right].               \tag{10.12}
\]
Every equality in (10.6)--(10.12) is finite-dimensional and exact.  In
particular, the coefficient \(K_k\) contains no middle curvature factor
\[
 C_2^k=D(R_2^k d'(Z_2^k)).                                \tag{10.13}
\]
Thus (10.10) simultaneously resums all repeated top-endpoint stars whose Taylor
expansion produced the \(d^{(r)}\) factorial in C-85.

There are two important limitations.  First, \(K_k\) and \(F_k\) are adapted
coefficients evaluated on the same trajectory; (10.10) is affine in the displayed
copy of \(R_2^k\), not an independence statement.  Second, (10.3) gives normalized
fixed-order control of the endpoint carrier,
\[
 \|\bar C_3^k\|_{L^p(\|\cdot\|_{p,n})}\leq C_T\sqrt p,
 \qquad A_i^k=A_i^0+O_T(1),                              \tag{10.14}
\]
but not a width-independent coordinate maximum.  A legitimate moment or graph
argument must retain normalized row sums and Gaussian signs rather than estimate
\(\|\bar C_3^k\|_\infty\).

The upper learned history remains harmless at the value level:
\[
 P_2^k=h\sum_{s<k}B_3^s\otimes X_2^s,
 \qquad
 (P_2^k)^*v=h\sum_{s<k}X_2^s\langle B_3^s,v\rangle_n.    \tag{10.15}
\]
It produces bounded feature coordinates and normalized covariances of endpoint
marks.  A word with \(r\) internal \(A^0\)-carriers costs at most
\(C^rr^{r/2}\), whose time-ordered series
\(
 \sum_r C_T^rr^{r/2}/r!
\)
converges.  Consequently the top \(d^{(r)}\) hierarchy is closed by (10.10); it
must not be cited again as the unresolved leaf.

## 11. The first surviving value-level cavity leaf

The learned lower history is
\[
 P_1^k=h\sum_{s<k}B_2^s\otimes X_1^s.                   \tag{11.1}
\]
Compare a full trajectory and a paired-block cavity trajectory and write
\(\delta V=V-V^{\rm cav}\).  Coordinatewise subtraction of
\(B_2=d(Z_2)R_2\) gives the exact identity
\[
 \boxed{
 \delta B_2
 =D_2\,\delta R_2+
 D\!\left(R_2^{\rm cav}d[Z_2,Z_2^{\rm cav}]\right)\delta Z_2.
 }                                                        \tag{11.2}
\]
The second summand contains an uncompensated \(R_2^{\rm cav}\).  Boundedness of
the divided difference only yields
\[
 |R_{2,i}^{\rm cav}d[Z_{2,i},Z_{2,i}^{\rm cav}]\delta Z_{2,i}|
 \leq\|d'\|_\infty|R_{2,i}^{\rm cav}\delta Z_{2,i}|.    \tag{11.3}
\]
The smallest missing estimate is therefore, for every fixed \(q,T\),
\[
 \boxed{
 \mathbb E\,{1\over n}\sum_i
 |R_{2,i}^{\rm cav}\delta Z_{2,i}|^q
 \leq C_{T,q}n^{-q/2}.
 }                                                        \tag{11.4}
\]
An ordered-limit variant is sufficient if it disposes of every nonleading cavity
remainder at fixed \((q,h)\) and leaves a leading recurrence with constants uniform
as \(h\downarrow0\).

Marginal \(L^q\) estimates do not prove (11.4).  Hölder gives
\[
 \|R_2^{\rm cav}\delta Z_2\|_{L^q}
 \leq\|R_2^{\rm cav}\|_{L^{2q}}
       \|\delta Z_2\|_{L^{2q}},                          \tag{11.5}
\]
so an induction at order \(q\) asks for order \(2q\).  This is a real
concentration loss, not a notational defect: with
\[
 R=\sqrt{n}\,e_1,qquad \delta Z=e_1,
\]
one has
\[
 \|R\|_n=1,qquad \|\delta Z\|_n=n^{-1/2},qquad
 \|R\odot\delta Z\|_n=1.                               \tag{11.6}
\]
Thus separate normalized \(L^2\) bounds allow exactly the localization that
destroys the cavity gain.

Nor can the loss be hidden in the chronological factorial.  Repeating the lower
branch \(r\) times requires schematically \(\|R_2\|_{L^{rq}}^r\).  Even granting
the target estimate \(\|R_2\|_{L^p}\leq Cp\), the absolute time-ordered bound is
\[
 { (CrqT)^r\over r!}\asymp(CeqT)^r,                     \tag{11.7}
\]
which is not summable for arbitrary fixed \(qT\).  Replacing the response by the
bounded finite difference \(|\delta X_2|\leq\pi\) avoids high moments but also
throws away the required \(n^{-1/2}\) smallness.

The exact status after (10.10) is therefore:

1. repeated top-layer endpoint derivatives and their factorial Taylor weights are
   completely resummed;
2. upper learned memory is value-level tail-safe;
3. generic marginal moment control is provably insufficient for the remaining
   lower learned-memory comparison;
4. the open theorem is a **joint nonconcentration** statement such as (11.4), or
   an exact signed conditional-value identity that bypasses it.

A Gaussian Poincare estimate on the full derivative, a direct \(q\mapsto2q\)
bootstrap, and a coordinatewise maximum bound would each reintroduce a previously
falsified obligation.  The live continuation is paired-block value resampling (or
an equivalent signed martingale/decoupling argument) that proves (11.4) from
order-\(q\), not order-\(2q\), information.

## 12. Paired-block Doob audit: centering survives, closure does not

The exact gauge symmetry does give the correct centering.  For a fixed middle
neuron \(j\), let
\[
 \mathcal B_j=
 \left(\sqrt n\,\Gamma_{1,j:},\sqrt n\,\Gamma_{2,:j}\right)
                                                               \tag{12.1}
\]
and condition on the complementary initialization.  Simultaneously changing the
sign of both parts of \(\mathcal B_j\) makes
\(Z_{2,j},X_{2,j},R_{2,j},B_{2,j}\) odd while leaving all physical upper fields
even.  Hence
\[
 F_j=(\Gamma_2^*B_3)_j
 \quad\hbox{is conditionally odd and conditionally centered}. \tag{12.2}
\]
Setting the whole block to zero defines the paired cavity and gives
\(R_{2,j}^{\rm cav}=0\).  The distinguished coordinate may have an order-one
finite difference, but it is therefore absent from the weighted average in
(11.4).

Reveal the \(2n\) standard-normal scalar entries of \(\mathcal B_j\).  Direct
resampling has the exact initial scales
\[
 \delta_{\Gamma_{2,ij}}R_{2,j}
 =n^{-1/2}\delta g\,B_{3,i}+\cdots,\qquad
 \delta_{\Gamma_{1,jk}}Z_{2,j}
 =n^{-1/2}\delta g\,X_{1,k}+\cdots .                    \tag{12.3}
\]
After the direct coordinate is removed, an individual off-diagonal martingale
increment has the expected \(n^{-1}\) scale; summing \(O(n)\) conditional
variances gives an \(O(n^{-1})\) square function and hence an
\(O(n^{-1/2})\) value difference.  Thus neither the initial normalization nor the
paired cavity is the problem.

The failure occurs when (11.2) is propagated.  If
\[
 S_i=\sum_{a=1}^{2n}\mathbb E_{a-1}|D_aZ_{2,i}|^2        \tag{12.4}
\]
is the scalar-reveal Doob square function, the lower self branch generates
schematically
\[
 S_i^{+}\ \ni\
 h^2\left|R_{2,i}^{\rm cav}
 d[Z_{2,i},Z_{2,i}^{(a)}]\right|^2S_i.                  \tag{12.5}
\]
This is the same-block theta of Section 9 inside a positive square-function
estimate.  The square is gauge-even, both response copies carry the same lower
index \(i\), and no independent free-index gain remains.

For every off-diagonal scalar reveal,
\[
 Z_{2,i}-Z_{2,i}^{(a)}=O(n^{-1/2}),
 \qquad
 d[Z_{2,i},Z_{2,i}^{(a)}]\longrightarrow d'(Z_{2,i}),  \tag{12.6}
\]
so bounded-value saturation is inactive in the leading tangent regime.  A direct
Burkholder/absolute propagation of (12.5), followed by the extra target weight
\(|R_{2,i}^{\rm cav}|^q\) in (11.4), asks for a
\(|R_{2,i}^{\rm cav}|^{2q}\) moment after the first return and approximately an
\((r+1)q\) moment after \(r\) returns.  Whole-block resampling does not alter this:
the only order-one coordinate has zero cavity weight, whereas every nonzero
weighted coordinate remains in the infinitesimal regime (12.6).

This calculation does **not** falsify (11.4).  It falsifies the proposed inference
from conditional oddness plus an ordinary Doob/Burkholder square-function bound.
Such a proof would need an additional self-normalized estimate of the form
\[
 S_i\lesssim {1\over n(1+|R_{2,i}^{\rm cav}|)^2},        \tag{12.7}
\]
or a signed cancellation before squaring.  The raw difference recursion points in
the opposite direction by multiplying \(S_i\) by \(R_{2,i}^2\), so (12.7) is not a
consequence of gauge symmetry, saturation, and the known marginal energy bounds.
The surviving route must therefore resum the lower same-block return in a signed
or noncommutative characteristic coordinate, or prove a genuinely joint
nonconcentration theorem by additional canonical-Gaussian structure.

## 13. Exact middle state characteristic for a genuine rerun cavity

Section 12 propagated the raw difference and therefore retained a local
\(R_2d'\) square-function branch.  At the state level this branch can be removed
before squaring.  Let
\[
 C_1=D\!\left((1+u^2)^{-2}\right),\qquad
 a_1=\langle X_1,X_1\rangle_n,\qquad D=D(d(Z_2)).
\]
The continuous feature-flow identities give
\[
 \dot Z_2=(a_1I+G_1C_1G_1^*)DR_2.                       \tag{13.1}
\]
Apply the same cubic \(\Theta(z)=z+z^3/3\) to the middle preactivation and set
\[
 Y_2=\Theta(Z_2),\qquad
 \mathcal L=D^{-1}G_1C_1G_1^*D .
\]
Then
\[
 \dot Y_2=a_1R_2+\mathcal LR_2.                          \tag{13.2}
\]

For a full orbit and a **genuinely rerun** paired cavity, define
\[
 \eta=Y_2-Y_2^{\rm cav},\qquad
 \bar d_i=
 \left(1+{Z_{2,i}^2+Z_{2,i}Z_{2,i}^{\rm cav}
 +(Z_{2,i}^{\rm cav})^2\over3}\right)^{-1}.             \tag{13.3}
\]
Thus \(\delta Z_{2,i}=\bar d_i\eta_i\) and \(0<\bar d_i\leq1\).  Subtracting
(13.2) gives exactly
\[
 \boxed{
 \dot\eta
 =a_1\delta R_2+\delta a_1R_2^{\rm cav}
  +\mathcal L\delta R_2+\delta\mathcal L\,R_2^{\rm cav}.
 }                                                       \tag{13.4}
\]
In particular,
\[
 |R_{2,i}^{\rm cav}\delta Z_{2,i}|
 \leq |R_{2,i}^{\rm cav}\eta_i|,                         \tag{13.5}
\]
and the direct local factor
\(R_{2,i}^{\rm cav}d[Z_{2,i},Z_{2,i}^{\rm cav}]
\delta Z_{2,i}\) is absent from (13.4).  This strictly improves the raw Doob
audit: the immediate same-time theta was a coordinate artifact.

There is also an exact Euler version.  Put
\[
 E_1^k=D\!\left({X_1^{k+1}-X_1^k\over r^{k+1}-r^k}\right),
 \qquad 0\leq E_1^k\leq I,                               \tag{13.6}
\]
using the derivative on a zero denominator.  Simultaneous expansion of the
\(r\)- and \(G_1\)-updates gives
\[
 Z_2^{k+1}-Z_2^k=hH_kD_kR_2^k,                          \tag{13.7}
\]
\[
 H_k=G_1^kE_1^k(G_1^k)^*
 \left\{\langle X_1^k,X_1^k\rangle_n
 +h\langle X_1^k,E_1^k(G_1^k)^*B_2^k\rangle_n\right\}I. \tag{13.8}
\]
If
\[
 \widehat d_i^k=
 {Z_{2,i}^{k+1}-Z_{2,i}^k\over
  \Theta(Z_{2,i}^{k+1})-\Theta(Z_{2,i}^k)},
\]
then the residual local ratio is
\[
 {d_i^k\over\widehat d_i^k}
 =1+{d_i^k\over3}(Z_{2,i}^{k+1}-Z_{2,i}^k)
                    (Z_{2,i}^{k+1}+2Z_{2,i}^k).         \tag{13.9}
\]
It is an \(O(h^2)\) local defect after (13.7), hence has \(O(h)\) accumulated
mass under the available fixed higher-moment velocity bounds.  This is adequate
for the contract's ordered \(n\to\infty\), then \(h\downarrow0\), passage.  No
mesh-uniform raw \(R_2d'\) tangent estimate should be required.

The genuine cavity convention is essential.  At initialization it sets
\[
 \Gamma_{1,j:}=0,\qquad\Gamma_{2,:j}=0
\]
and reruns every learned update.  Inductively,
\[
 Z_{2,j}^{\rm cav}=R_{2,j}^{\rm cav}=B_{2,j}^{\rm cav}=0,
\quad
 (P_1^{\rm cav})_{j:}=0,\quad(P_2^{\rm cav})_{:j}=0.    \tag{13.10}
\]
If one instead deletes only the raw blocks but reuses the full learned
\(P_\ell\), (11.4) is false for \(q>2\): after one update the exceptional
\(j\)-summand is order \(h^q/n\), not \(n^{-q/2}\).  That algebraic cavity is
therefore inadmissible for the proposed estimate.

## 14. The genuine learned-history two-time leaf

The characteristic cancellation does not eliminate every occurrence of the
learned \(P_1\) history inside \(\delta\mathcal L\).  Expand
\[
 P_1^k=h\sum_{s<k}B_2^s\otimes X_1^s.                   \tag{14.1}
\]
The term with \(\delta P_1^k\) on the left of the cross bath has the exact
coordinate form
\[
 \left(\delta P_1^kE_1^k(\Gamma_1^{\rm cav})^*
 B_2^{{\rm cav},k}\right)_i
 =h\sum_{s<k}\delta B_{2,i}^s\,\alpha_{s,k}
   +\hbox{the corresponding }\delta X_1\hbox{ terms},   \tag{14.2}
\]
where
\[
 \alpha_{s,k}=
 \left\langle X_1^s,E_1^k(\Gamma_1^{\rm cav})^*
 B_2^{{\rm cav},k}\right\rangle_n.                     \tag{14.3}
\]
In the state characteristic,
\[
 \delta B_{2,i}^s
 =d_i^s\delta R_{2,i}^s
 +\kappa_i^sR_{2,i}^{{\rm cav},s}\eta_i^s,\qquad
 |\kappa_i^s|\leq\|d'\|_\infty .                        \tag{14.4}
\]
For arctangent the coefficient has a substantially sharper exact form.  If
the two middle preactivations are (z,w), then
\[
 \kappa(z,w)={d(z)-d(w)\over\Theta(z)-\Theta(w)}
 =-{z+w\over
 (1+z^2)(1+w^2)\{1+(z^2+zw+w^2)/3\}} .                \tag{14.4a}
\]
Since
\[
 z^2+zw+w^2={3\over4}(z+w)^2+{1\over4}(z-w)^2
\]
and (1+s^2/4\geq |s|), this proves the endpoint-sensitive gate estimate
\[
 \boxed{|\kappa(z,w)|\leq d(z)d(w).}                    \tag{14.4b}
\]
In particular,
\[
 |\kappa_i^sR_{2,i}^{{\rm cav},s}|
 \leq d_i^s|B_{2,i}^{{\rm cav},s}|.                    \tag{14.4c}
\]
Thus the genuine history leaf contains only one *ungated* two-time query,
not two.  This improvement does not by itself close the estimate:
normalized action controls (B_2) only in empirical (L^2), while the
remaining factor (R_{2,i}^{{\rm cav},t}\eta_i^s) is coordinatewise and
adapted.  Treating (B_2) as bounded here would merely hide the original
no-condensation obligation.
Multiplying (14.2) by the target weight \(R_{2,i}^{{\rm cav},t}\) therefore
produces the first genuine nonlocal leaf
\[
 \boxed{
 h\sum_{s<k}\alpha_{s,k}\kappa_i^s
 R_{2,i}^{{\rm cav},t}R_{2,i}^{{\rm cav},s}\eta_i^s .
 }                                                       \tag{14.5}
\]
It appears only after a regular cavity defect propagates, is learned by
\(\delta P_1\), and returns through the cross \(P_1\Gamma_1^*\) bath.  It is not
the same-time scalar self-return canceled in Section 13.

The nuclear bound
\[
 \|P_1^k\|_1\leq
 h\sum_{s<k}\|B_2^s\|_n\|X_1^s\|_n\leq C_T             \tag{14.6}
\]
does scalarize terms in which \(P_1\) is fixed, but it does not scalarize
\(\delta P_1\) on the left in (14.2).  An absolute \(L^q\) estimate of (14.5)
asks for a two-time \(2q\) moment of the cavity query.  The Volterra expansion
prevents this loss from being repeated at every Euler step; nevertheless one
fixed higher-moment/two-time obligation remains.  Compact normalized energy and
same-\(q\) marginal control alone cannot discharge it.

For the purely static \(\Gamma_1\) cross bath there is a same-order regression
tool.  If \(g\sim N(0,I_n)\), \(a\) is independent of \(g\), and \(H\) is smooth,
one-dimensional Gaussian integration by parts after rotating \(a\) gives
\[
 \|(a\cdot g)H\|_p
 \leq C_p\left\||a|
 \left(|H|+|D_{a/|a|}H|\right)\right\|_p.               \tag{14.7}
\]
Consequently an off-diagonal factor
\(\Gamma_{1,i}C_1\Gamma_{1,j}^*\) carries its true
\(n^{-1/2}\) scale without first applying marginal Hölder to the cavity query.
Thus (14.5), rather than the pure static bath, is the sharp current leaf.

The preregistered GPU experiment in
GPU_PAIRED_CAVITY_PRODUCT_RESULTS_2026-08-23.md supports (11.4) through
\(q=8\), \(T=4\), and \(n=2048\), with all numerical audits passing.  That
evidence rules out neither a rare-tail failure nor the need for a new signed
two-time estimate and has no proof status.

## 15. Same-order Gaussian multiplier reduction for the two-time leaf

The \(q\mapsto2q\) loss in (14.5) is not unavoidable.  A second paired
cavity and one-dimensional Gaussian integration by parts replace it by a
directional response at the *same* moment order.  This is an exact reduction;
the response estimate needed to close it is not proved here.

For \(i\ne j\), start with the genuine \(j\)-cavity and then also remove the
paired middle block \((\Gamma_{1,i:},\Gamma_{2,:i})\).  Denote the resulting
orbit by a superscript \({\rm cav}(ij)\), and put
\[
 \xi_i=\sqrt n\,\Gamma_{2,:i}\sim N(0,I_n),\qquad
 u_{ij,t}=n^{-1/2}B_3^{{\rm cav}(ij)}(t).              \tag{15.1}
\]
Conditionally on the double-cavity environment, \(u_{ij,t}\) is independent
of \(\xi_i\), and the normalization is exactly
\[
 \|u_{ij,t}\|_2=\|B_3^{{\rm cav}(ij)}(t)\|_n,qquad
 u_{ij,t}^{\mathsf T}u_{ij,s}
 =\langle B_3^{{\rm cav}(ij)}(t),B_3^{{\rm cav}(ij)}(s)\rangle_n.       \tag{15.2}
\]

The elementary multiplier lemma used below is worth recording separately.
If \(z\sim N(0,1)\), \(f\) is smooth, and \(q\ge2\), then
\[
 \boxed{\ \|zf\|_q\le \sqrt{q-1}\,\|f\|_q+q\,\|\partial_zf\|_q.\ }  \tag{15.3}
\]
Indeed, integration by parts followed by Holder gives, with
\(a=\|zf\|_q,b=\|f\|_q,c=\|f'\|_q\),
\[
 a^q\le(q-1)a^{q-2}b^2+qa^{q-1}c,
\]
and hence \(a^2\le(q-1)b^2+qac\), which implies (15.3).

Let
\[
 F_{ij}(s)=R_{2,i}^{{\rm cav}(j)}(s)\eta_i^{(j)}(s).
\]
Rotating the conditional Gaussian law so that its first coordinate is
\(\xi_i^{\mathsf T}u_{ij,t}/\|u_{ij,t}\|_2\), (15.3) yields
\[
 \boxed{
 \| (\xi_i^{\mathsf T}u_{ij,t})F_{ij}(s)\|_q
 \le \sqrt{q-1}\,
 \|\|B_3^{{\rm cav}(ij)}(t)\|_nF_{ij}(s)\|_q
 +q\|D_{u_{ij,t}}F_{ij}(s)\|_q .}                    \tag{15.4}
\]
No independence of \(F_{ij}\) and \(\xi_i\) is assumed.  In particular,
(15.4) keeps moment order \(q\); its exact price is the mixed directional
response
\[
 D_{u_{ij,t}}F_{ij}
 =(D_{u_{ij,t}}R_{2,i}^{{\rm cav}(j)}(s))\eta_i^{(j)}(s)
 +R_{2,i}^{{\rm cav}(j)}(s)D_{u_{ij,t}}\eta_i^{(j)}(s).                 \tag{15.5}
\]
For the frozen Gaussian projection the direct derivative is only the
normalized two-time Gram scalar,
\[
 D_{u_{ij,t}}(\xi_i^{\mathsf T}u_{ij,s})
 =\langle B_3^{{\rm cav}(ij)}(t),B_3^{{\rm cav}(ij)}(s)\rangle_n.       \tag{15.6}
\]
The difference between the actual \(i\)-query in the \(j\)-cavity and this
projection is exactly a mixed \((i,j)\)-cavity response of \(B_3\), plus the
bounded learned term
\[
 \int_0^s X_{2,i}^{\rm cav(j)}(v)
 \langle B_3^{\rm cav(j)}(v),B_3^{\rm cav(j)}(s)\rangle_n\,dv.          \tag{15.7}
\]
Thus (15.4) replaces the old \(2q\)-moment leaf by a finite same-order
candidate hierarchy: the base weighted difference, the directional
\(D_u\eta\) response, and the mixed double-cavity response of \(B_3\).

There is no free gain merely from averaging the two labels.  For an
exchangeable off-diagonal family,
\[
 {1\over n^2}\sum_j\sum_{i\ne j}\mathbb E|Y_{ij}|^q
 =\left(1-{1\over n}\right)\mathbb E|Y_{12}|^q,        \tag{15.8}
\]
and a Frobenius estimate controls only \(q=2\).  A smooth tail-localized
Gaussian example can have
\(\|R_i\eta_{ij}\|_q\asymp n^{-1/2}\) but
\(\|R_i^2\eta_{ij}\|_q\asymp \sqrt{q\log n}\,n^{-1/2}\).  The derivative
term in (15.4) detects exactly this localization.

Time ordering and paired gauge parity are also insufficient by themselves.
The retarded scalar equation
\[
 y(t)=\varepsilon+\int_0^t(t-s)G^2y(s)\,ds
\]
is gauge even and has no instantaneous self-return, but
\(y(t)=\varepsilon\cosh(tG)\), whose \(L^q\) norm grows exponentially in
\(q\).  Therefore the surviving network lemma must control the *actual*
directional characteristic in (15.5); it cannot be inferred from marginal
moments, symmetry, or a Hilbert--Schmidt bound alone.

The precise new leaf is consequently a row-wise, same-order estimate for the
triple consisting of (i) \(F_{ij}\), (ii) \(D_{u_{ij,t}}F_{ij}\), and
(iii) the mixed \((i,j)\)-cavity response of \(B_3\), with scale
\(C_{T,q}n^{-1/2}\).  If its constants have factorial growth
\(C_T^qq!\), then (15.4), applied twice to the two query factors in (14.5),
has exactly the required \(C_Tq\) root growth.  Establishing that directional
characteristic, rather than a \(2q\)-moment bootstrap, is the current proof
obligation.

## 16. Coupled forward-query budget and the safe learned part

The top characteristic identifies which part of the directional response can
still amplify a row.  Write
\[
 z=Z_3,\quad d=d(z),\quad b=Ad,\quad
 a_2=\|X_2\|_n^2,\quad w=G_2\dot X_2,
\]
so that \(\dot z=a_2b+w\).  For a variation put
\(U=\delta A\) and \(V=\delta z/d\).  The exact calculation in (2.4), now
with the lower-path sources retained, gives
\[
 \dot U=d^2V,
 \qquad
 \dot V=a_2U+A\,\delta a_2+d^{-1}\delta w
          -{d'(z)\over d(z)}wV .                       \tag{16.1}
\]
Since
\[
 \left|{d'(z)\over d(z)}\right|={2|z|\over1+z^2}\le1,                 \tag{16.2}
\]
the homogeneous row propagator costs at most
\[
 \exp\left\{C_T(t-s)+\int_s^t|w_i(v)|\,dv\right\}.    \tag{16.3}
\]
No exponential of the endpoint mark \(A_{0,i}\) appears.  Notice that
(16.1), rather than a positive-part estimate on \(A d'\), is the safe exact
identity: restricting a logarithmic derivative to the random set
\(\{A z<0\}\) would leave an uncontrolled variation term.

The learned part of the budget in (16.3) is already harmless.  Indeed,
\[
 P_2(t)=\int_0^tB_3(s)\otimes X_2(s)\,ds
\]
and hence
\[
 |(P_2(t)\dot X_2(t))_i|
 \le C_T(1+|A_{0,i}|)\|\dot X_2(t)\|_n.               \tag{16.4}
\]
Moreover
\[
 \dot X_2=D_2\{\|X_1\|_n^2B_2+G_1D_1^2Q_1\},        \tag{16.5}
\]
so the spectral and trace-norm state bounds imply
\[
 \int_0^T\|\dot X_2(t)\|_n^2dt
 \le C_T\int_0^TK(t)\,dt\le C_T.                     \tag{16.6}
\]
Consequently
\[
 \boxed{
 \int_0^T|(P_2(t)\dot X_2(t))_i|dt
 \le C_T(1+|A_{0,i}|).}                               \tag{16.7}
\]
The empirical law of the right side has a width-uniform Gaussian exponential
moment on the usual initialization good event.

Thus the only new exponential budget is the static forward adaptive query
\[
 W_i^\Gamma(T)=\int_0^T|(\Gamma_2\dot X_2(t))_i|dt.    \tag{16.8}
\]
It is the forward partner of the transpose query \(R_2=G_2^*B_3\).
Operator norm and action give only the averaged square bound
\[
 {1\over n}\sum_i(W_i^\Gamma(T))^2
 \le T\int_0^T\|\Gamma_2\dot X_2(t)\|_n^2dt\le C_T,  \tag{16.9}
\]
which does not imply an empirical exponential moment.  A complete proof must
therefore couple the same-order multiplier hierarchy of Section 15 to a
row-cavity estimate for (16.8).  The preregistered computation
`FORWARD_QUERY_EXPONENTIAL_PREREGISTRATION_2026-08-23.md` tests this precise
quantity, without assigning it theorem status.

## 17. Product-rule audit of the learned lower history

There is a tempting identity which must be used with care.  Since

\[
 P_1(t)=\int_0^t B_2(s)\otimes X_1(s)\,ds,
 \qquad X_1'=C_1Q_1,
\]

one has exactly

\[
 P_1(t)X_1'(t)
 =\int_0^tB_2(s)\langle X_1(s),X_1'(t)\rangle_n\,ds,                 \tag{17.1}
\]

and hence

\[
 {d\over dt}\{P_1(t)X_1(t)\}
 =\|X_1(t)\|_n^2B_2(t)+P_1(t)X_1'(t).                              \tag{17.2}
\]

Thus the scalar coefficient in the learned-history leaf is the derivative
of a feature Gram.  Equation (17.2) does collect all of the boundary terms
created by Abel summation.  It does **not** make the full vector response an
endpoint quantity.

The exact obstruction can already be seen at width two.  In normalized
\(\mathbb R^2\), put

\[
 a=(1,1),\qquad h=(1,-1),\qquad
 \langle a,h\rangle_n=0,\quad \|a\|_n=\|h\|_n=1,                    \tag{17.3}
\]

and consider the symmetric state

\[
 u=u_0a,\qquad G_1=g\,a\otimes a,\qquad
 G_2=\lambda\,a\otimes a,\qquad A=A_0a.                            \tag{17.4}
\]

Write

\[
 x=\arctan u_0,\quad z=gx,\quad d=(1+z^2)^{-1},\quad
 w=\arctan z,\quad e=(1+(\lambda w)^2)^{-1},
\]
\[
 b=eA_0,\qquad R=\lambda b.                                        \tag{17.5}
\]

The antisymmetric variational subspace

\[
 \delta u=\delta A=0,\qquad
 \delta G_1=\gamma\,h\otimes a,\qquad
 \delta G_2=\beta\,a\otimes h                                    \tag{17.6}
\]

is invariant.  Direct differentiation of the complete equations, with all
left/right and feature companions retained, gives

\[
 \delta r=\delta X_1=\delta C_1=0,
 \qquad \delta R_2=b\beta h,                                      \tag{17.7}
\]

and

\[
 {d\over dt}\binom\gamma\beta
 =\begin{pmatrix}\alpha&k\\ k&0\end{pmatrix}\binom\gamma\beta,
 \qquad
 \alpha=d'(z)x^2R,\qquad k=bdx.                                   \tag{17.8}
\]

The term \(\alpha\gamma\) is precisely the linearization of the learned
\(P_1\) curvature:

\[
 \delta B_{2,\mathrm{learn}}
 =d'(z)\,\delta Z_2\,R
 =d'(z)xR\gamma h.                                                  \tag{17.9}
\]

At an instant with \((\gamma,\beta)=(1,0)\), every proposed companion
involving \(\delta R_2\), \(\delta X_1\), or \(\delta C_1\) vanishes, but
\(\gamma'=\alpha\ne0\) whenever \(zR\ne0\).  Moreover the determinant in
(17.8) is \(-k^2<0\), so the transverse generator has two real eigenvalues
of opposite sign and cannot be made skew-adjoint in any fixed positive
Hilbert metric.  This rules out an exact Hamiltonian or positive quadratic
cancellation of the learned term.

The differential-form version shows why the scalar case is misleading.  If
\(g_j=G_1e_j\), then

\[
 g_j'=X_{1,j}B_2,\qquad r_j'=\langle g_j,B_2\rangle_n,
 \qquad
 {d\over dt}\langle g_j,g_k\rangle_n
 =X_{1,j}r_k'+X_{1,k}r_j'.                                        \tag{17.10}
\]

Varying and integrating by parts leaves the curvature two-form

\[
 d\{X_{1,j}\,dr_k+X_{1,k}\,dr_j\}
 =(C_{1,j}-C_{1,k})\,dr_j\wedge dr_k.                              \tag{17.11}
\]

It vanishes in width one but is generically nonzero as soon as two feature
coordinates have different gates.  Therefore (17.1)--(17.2) may be used to
collect boundary terms, but they cannot eliminate (14.5), replace it by a
current scalar endpoint, or close the response without an annealed
same-block estimate.  The product-rule route is consequently closed as a
standalone resolution.

## 18. Audit of a bounded-cotangent reparametrization

Replacing (R_2) by (B_2=D_2R_2) removes the inverse middle gate from the
displayed value, but it does not turn the lower dynamics into a uniformly
Lipschitz (L^2) system.  The exact equations make the obstruction explicit.
Put

\[
 K_1=\|X_1\|_n^2I+G_1D_1^2G_1^*,qquad
 K_2=\|X_2\|_n^2I+G_2D_2K_1D_2G_2^*.                              \tag{18.1}
\]

Then

\[
 Z_2'=K_1B_2,qquad X_2'=D_2K_1B_2,qquad
 Z_3'=K_2B_3,                                                       \tag{18.2}
\]

and, with (a(z)=d'(z)/d(z)), (|a|le1),

\[
 B_3'=D_3X_3+a(Z_3)B_3\odot K_2B_3,                               \tag{18.3}
\]

\[
 R_2'=\|B_3\|_n^2X_2+G_2^*D_3X_3
       +G_2^*\{a(Z_3)B_3\odot K_2B_3\},                            \tag{18.4}
\]

\[
 B_2'=D_2R_2'+a(Z_2)B_2\odot K_1B_2.                              \tag{18.5}
\]

The logarithmic gate derivatives are bounded, but (18.3) and (18.5) still
contain pointwise products of two merely (L^2) fields.  Thus the change of
variables has moved, rather than removed, the concentration problem.

Clipping the endpoint (A) does give a dimension-free Lipschitz estimate for
the isolated top pair ((A,Z_3)), because (B_3=D_3A) is then bounded
coordinatewise.  There is no corresponding consequence for the lower pair.
The sharp deterministic example is

\[
 u=0,qquad G_1=I,qquad G_2=ve_1^{\mathsf T},qquad
 A={\bf1},qquad v=n^{-1/2}{\bf1}.                                  \tag{18.6}
\]

It has

\[
 X_1=Z_2=X_2=Z_3=0,qquad B_3={\bf1},qquad
 R_2=\sqrt n,e_1,qquad B_2=R_2,                                  \tag{18.7}
\]

while

\[
 \|A\|_\infty=\|A\|_n=\|G_1\|_{\rm op}
 =\|G_2\|_{\rm op}=\|R_2\|_n=1.                                  \tag{18.8}
\]

Consequently, for every fixed (K) and all (n>K^2),

\[
 {1\over n}\sum_jR_{2,j}^2{\bf1}_{\{|R_{2,j}|>K\}}=1,             \tag{18.9}
\]

and every fixed empirical exponential moment diverges.  This is not a
canonical iid-Gaussian counterexample; it is a decisive falsifier of any
deterministic inference from endpoint clipping, normalized energy, and bulk
operator norms.

The same example gives a failure of width-uniform continuity on that cutoff
set.  Perturb only the first input coordinate so that

\[
 X_1=\varepsilon e_1,qquad Z_2=\varepsilon e_1,qquad
 A=(1+q^2/n){\bf1},qquad q=\arctan\varepsilon.                       \tag{18.10}
\]

Then (B_3={\bf1}) and (R_2=\sqrt n e_1) remain unchanged.  The two
states are (O(n^{-1/2}))-close in the normalized state metric, whereas

\[
 \|Q_1-\widetilde Q_1\|_n
 =1-d(\varepsilon)>0                                                \tag{18.11}
\]

independently of (n).  Hence neither ((Z_2,B_2)) nor a bounded transform
such as (operatorname{arsinh}B_2) supplies the missing uniform modulus;
the latter maps (sqrt n e_1) to a vector whose normalized norm tends to
zero and therefore hides exactly the forbidden square defect.

The useful residue of this audit is the exact isolation

\[
 R_{2,j}(t)=(\Gamma_2^*B_3(t))_j
 +\int_0^tX_{2,j}(s)\langle B_3(s),B_3(t)\rangle_n,ds.             \tag{18.12}
\]

After endpoint clipping the second term is uniformly bounded.  Any proof
must therefore add genuinely Gaussian, columnwise information about the
first term.  No cotangent coordinate change can replace that annealed
no-condensation estimate.

## 19. Signed top commutator and the corrected row-leverage audit

The positive-curvature identity also isolates a tempting row-leverage
argument, but its normalization is decisive.  Define

\[
 \mathsf H_2=D_2K_1D_2,\qquad
 \mathcal E=\langle R_2,\mathsf H_2R_2\rangle_n,
 \qquad H=G_2\mathsf H_2R_2.                           \tag{19.1}
\]

Then the exact top equations are

\[
 Z_3'=\{\|X_2\|_n^2I+G_2\mathsf H_2G_2^*\}B_3,
 \qquad A'=X_3.                                        \tag{19.2}
\]

For (F=\langle A,X_3\rangle_n),

\[
 F'=\|X_3\|_n^2+|X_2\|_n^2\|B_3\|_n^2+\mathcal E,
 \qquad
 \mathcal E=\|X_1\|_n^2\|B_2\|_n^2+|D_1Q_1\|_n^2.  \tag{19.3}
\]

This is the raw-kernel identity in a useful PSD factorization.  With
(a=\pi/2), it gives

\[
 J_T:=\int_0^T\mathcal E(t)dt
 \leq2a\|A_0\|_n+a^2T.                                \tag{19.4}
\]

The residual coefficient in the top natural-coordinate response is

\[
 \mathcal C_i=2Z_{3,i}D_{3,i}H_i,qquad |\mathcal C_i|\leq|H_i|.       \tag{19.5}
\]

If (g_i^{\mathsf T}) is the ordinary (i)-th row of (G_2), then

\[
 H_i^2\leq
 (g_i^{\mathsf T}\mathsf H_2g_i)
 (R_2^{\mathsf T}\mathsf H_2R_2)
 =n(g_i^{\mathsf T}\mathsf H_2g_i)\mathcal E.          \tag{19.6}
\]

The factor (n) cannot be omitted.  Thus a pathwise leverage estimate based
only on (mathcal E) loses (sqrt n).

There is nevertheless an exact learned/static split.  Write

\[
 g_i(t)=\gamma_i+u_i(t),\qquad
 u_i(t)={1\over n}\int_0^tB_{3,i}(s)X_2(s)^{\mathsf T}ds,
 \qquad v=\mathsf H_2R_2.                              \tag{19.7}
\]

Put (S_T=\sup_{t\leq T}\|\mathsf H_2(t)\|_{\rm op}) and

\[
 U_{i,T}=\int_0^T|B_{3,i}(s)|\|X_2(s)\|_n ds.
\]

Then

\[
 \int_0^T|u_i(t)^{\mathsf T}v(t)|dt
 \leq U_{i,T}\sqrt{TS_TJ_T},
 \qquad
 U_{i,T}\leq aT|A_{0,i}|+{a^2T^2\over2}.              \tag{19.8}
\]

Moreover the normalized rank-one identities imply

\[
 S_T^{1/2}\leq a+\|\Gamma_1\|_{\rm op}+\sqrt{TJ_T},qquad
 \sup_{t\leq T}\|G_2(t)\|_{\rm op}
 \leq\|\Gamma_2\|_{\rm op}+\sqrt{TJ_T}.              \tag{19.9}
\]

Thus the learned row is tail-safe.  The sole row-leverage obstruction is

\[
 N_i(T)=\int_0^T|\gamma_i^{\mathsf T}\mathsf H_2R_2|dt.              \tag{19.10}
\]

At order two, exchangeability and the global action do close.  Indeed,

\[
 \mathbb E\int_0^TH_i^2dt
 =\mathbb E\int_0^T\|H\|_n^2dt
 \leq\mathbb E\!\left[
 \sup_{t\leq T}(\|G_2\|_{\rm op}^2S_T)J_T\right],                  \tag{19.11}
\]

and hence

\[
 \boxed{
 \left\|\int_0^T|\mathcal C_i(t)|dt\right\|_{L^2}^2
 \leq T\,\mathbb E\!\left[
 \sup_{t\leq T}(\|G_2\|_{\rm op}^2S_T)J_T\right].}               \tag{19.12}
\]

All factors on the right have dimension-free Gaussian moments.  This does
not extend to (q>2) from exchangeability: the generic loss
(n^{1/2-1/q}) is sharp.

To state the precise probabilistic residue, let
(\widehat v_i(t)) be independent of the static row (gamma_i), and set

\[
 L_i=\left(\int_0^T\|v(t)-\widehat v_i(t)\|_2^2dt\right)^{1/2},
 \qquad
 \widehat V_i^2={1\over n}\int_0^T\|\widehat v_i(t)\|_2^2dt.       \tag{19.13}
\]

Conditional Gaussian quadratic-form bounds and Cauchy--Schwarz give, for
(q\geq2),

\[
 \boxed{
 \|N_i(T)\|_q
 \leq C\sqrt{Tq}\,\|\widehat V_i\|_q
 +\sqrt T\,\|\|\gamma_i\|_2L_i\|_q.}                \tag{19.14}
\]

For the genuine row-deleted flow,
(\widehat V_i^2\leq\widehat S_T\widehat J_T).  Therefore the only
new input in (19.14) is a normalized (n^{-1/2}) cavity-stability estimate
for (mathsf H_2R_2).

This input cannot follow from Gaussian row marginals, exchangeability,
operator bounds, and action alone.  Let (Gamma) have iid
(N(0,n^{-1})) entries, choose (I) uniformly and independently, let
(gamma_I) be row (I), and zero that row to form (Gamma_{-I}).  Put

\[
 B=\sqrt n\,\Gamma_{-I}\gamma_I,qquad
 R=\Gamma^*B,qquad \mathsf H_2=I.                    \tag{19.15}
\]

Writing (W=\Gamma_{-I}^*\Gamma_{-I}),

\[
 R=\sqrt nW\gamma_I,qquad
 (\Gamma R)_I=\sqrt n\,\gamma_I^*W\gamma_I.           \tag{19.16}
\]

With probability (1-e^{-cn}), the last value is at least (c\sqrt n),
while (|B|_n), (|R|_n), and (|\Gamma|_{\rm op}) are (O(1)).
The construction is row-exchangeable, and for every fixed (i) and (q>2),

\[
 \|(\Gamma R)_i\|_q\geq c n^{1/2-1/q}.                \tag{19.17}
\]

This is not a reachable-flow counterexample.  It proves that (19.14) must
use a dynamical influence/reachability property and cannot be replaced by a
generic annealed leverage lemma.

Finally, the commutator coefficient has a signed Abel identity:

\[
 \mathcal C_i
 ={d\over dt}\log(1+Z_{3,i}^2)
 -2\|X_2\|_n^2Z_{3,i}D_{3,i}^2A_i.                    \tag{19.18}
\]

The second term has Gaussian exponential moments because
(|A_i(t)|\leq|A_{0,i}|+at).  Hence signed interval integrals telescope.
Absolute response estimates still require the total variation of
(log(1+Z_{3,i}^2)), which is another form of the same high-moment
anti-localization problem.

## 20. The exact divided gate does not control the terminal transported query

Write \(d(z)=(1+z^2)^{-1}\) and

\[
 \kappa(z,w)={d(z)-d(w)\over\Theta(z)-\Theta(w)}.
\]

Section 14 proved the sharp arctangent identity

\[
 |\kappa(z,w)|\leq d(z)d(w).                         \tag{20.1}
\]

Consequently the learned two-time leaf has the deterministic estimate

\[
 |L_i(t)|
 \leq |R_i^c(t)|\int_0^t d(Z_i(s))|B_i^c(s)|
                    |\eta_i(s)|\,ds.                 \tag{20.2}
\]

The gain in (20.1) is real, but it occurs only at the source time \(s\).  It
does not gate the terminal factor \(R_i^c(t)\).  The following exchangeable
path construction proves that empirical energy, bounded cotangents, and an
exact \(n^{-1/2}\) cavity displacement do not repair this endpoint trace.

Let \(T=1\), \(\varepsilon=n^{-1/2}\), \(M=n^{1/4}\), and let \(J\) be
uniform on \(\{1,\ldots,n\}\).  Choose a continuous nondecreasing \(u\), zero
on \([0,1/2]\), with \(u(1)=1\).  For \(i\ne J\), put \(w_i=r_i=1\); for
\(i=J\), put

\[
 w_J=1+(M-1)u,
 \qquad r_J=1+u w_J^2,
 \qquad z_i=\Theta^{-1}(\Theta(w_i)+\varepsilon).
                                                               \tag{20.3}
\]

Set \(R_i^c=r_i\), \(B_i^c=d(w_i)r_i\), and \(B_i=d(z_i)r_i\).  Then

\[
 \eta_i=\Theta(z_i)-\Theta(w_i)=n^{-1/2},
 \qquad |B_i|\leq |B_i^c|\leq1,                    \tag{20.4}
\]

and the empirical \(L^2\) norms of \(R^c,Z,Z^c\) are bounded uniformly in
\(n\) and time.  On the first half interval \(w_J=r_J=1\).  The Cauchy
mean-value theorem gives, for
\(z_\varepsilon=\Theta^{-1}(\Theta(1)+\varepsilon)\in(1,2)\),

\[
 \kappa(z_\varepsilon,1)
 =-{2\xi\over(1+\xi^2)^3}\leq-{4\over125}
 \quad\text{for some }\xi\in(1,2).                 \tag{20.5}
\]

At later times the divided difference remains negative.  Since
\(r_J(1)=1+\sqrt n\), the signed terms cannot cancel and

\[
 |L_J(1)|\geq {2\over125}.                           \tag{20.6}
\]

For each fixed \(i\), therefore,

\[
 \|L_i(1)\|_{L^q}\geq {2\over125}n^{-1/q}.          \tag{20.7}
\]

At \(q=(c/2)\log n\), (20.7) stays bounded below while
\(Cq/\sqrt n\to0\).  This is a proof-route counterexample, not a reachable
trajectory of the frozen feature flow.  It rigorously excludes deriving the
needed logarithmic-moment estimate from (20.1), exchangeability, normalized
energy, and bounded \(B,B^c\) alone.

The exact remaining quantity is

\[
 G_i(t)=|R_i^c(t)|
 \left(\int_0^t d(Z_i(s))^2|B_i^c(s)|^2ds\right)^{1/2},
 \qquad U_i(T)=\sup_{s\leq T}|\eta_i(s)|.            \tag{20.8}
\]

Time Cauchy--Schwarz gives

\[
 \sup_{t\leq T}|L_i(t)|
 \leq\sqrt T\,\sup_{t\leq T}G_i(t)\,U_i(T).        \tag{20.9}
\]

Thus the divided-gate route closes only after a genuinely dynamical
anti-localization statement: either a pathwise bound on \(G_i\), or a
leave-two-out sigma-field on which \(G_i\) is controlled and \(U_i\) has a
conditional \(C_Tq/\sqrt n\) bound.  An integrated \(L^2\) estimate is not
enough because it has no endpoint trace.  This is the same reachability leaf
identified independently by the row-leverage and slow-tube audits.

## 21. Continuum state-evolution response reaches the same same-label leaf

A clean-room continuum-response derivation gives a useful consistency check
on Sections 14--16.  This subsection records a route audit, not an invocation
of a DMFT theorem: passing the growing Euler program to these response
equations is itself part of the open mesh-uniform problem.

Let (C_\ell^X(t,s)=\mathbb E[X_\ell(t)X_\ell(s)]) and
(C_{\ell+1}^B(t,s)=\mathbb E[B_{\ell+1}(t)B_{\ell+1}(s)]).  In the formal
continuum causal regression, the middle backward field has the form

\[
 R_2(t)=\eta_2(t)+\alpha_3(t)X_2(t)
       +\int_0^tK_3(t,s)X_2(s),ds,                  \tag{21.1}
\]

where (eta_2) is centered Gaussian with covariance (C_3^B), (K_3)
contains covariance plus the regular top response, and
(alpha_3(t)=\mathbb E[A(t)d'(Z_3(t))]).  Thus a uniform bound on the
deterministic response contribution in (21.1) would immediately give the
desired exponential tail: the only unbounded innovation is Gaussian and
(X_2) is bounded.

The middle response does not close by an (L^2) argument.  If

\[
 J_2(t,s)={\delta Z_2(t)\over\delta\eta_2(s)},
\]

then elimination of the companion tangents produces a causal Volterra
equation whose local atom contains

\[
 p_2(v)=R_2(v)d_2'(v)+\alpha_3(v)d_2(v)^2.            \tag{21.2}
\]

Taking the response expectation therefore exposes

\[
 \mathbb E\!\left[d_2(t)R_2(v)d_2'(v)J_2(v,s)\right]. \tag{21.3}
\]

The arctangent identity gives the exact improvement

\[
 |R_2d_2'|\leq |B_2|,                                 \tag{21.4}
\]

but squaring a tangent estimate now requires

\[
 \mathbb E[B_2(v)^2J_2(v,s)^2],                       \tag{21.5}
\]

which is not controlled by the separate action bound and response (L^2)
norm.  Hölder recreates the (q\mapsto2q) hierarchy.  Iterating the causal
equation gives ordered products of the same-label (B_2(v_k)); time-simplex
factors do not control them without an exponential occupation estimate.

This failure is sharp for the proposed *abstract* estimate.  With a frozen
scalar (Z_2=-1), (d_2=d_2'=1/2), (B_2=Y), (R_2=2Y), and unit Volterra
kernel, the response is

\[
 J_2(t,s)=\tfrac12e^{Y(t-s)}.                          \tag{21.6}
\]

A lognormal (Y) has a finite quadratic action but makes the response
exponential moment infinite.  This is not a reachable-flow counterexample.
It proves only that the continuum-response route needs exactly the same
canonical same-label multiplier or anti-localization lemma as the finite
two-cavity route; expectation-level causality does not supply it for free.

## 22. Exact gauge, balance, and radial-freezing identities

The rank-one factor flow supplies additional reachability information which
is invisible to generic exchangeability counterexamples.  Let

\[
 h(z)=\arctan z-{z\over1+z^2}.
\]

Then (h) has the sign of (z), (|h|\leq\pi/2), and
(|z|/(1+z^2)\leq|\arctan z|).

For a middle neuron (i), write (r_i=G_{1,i:}) and (c_i=G_{2,:i}).
The exact normalized rank-one equations give

\[
 {d\over dt}\|c_i\|_2^2={2\over n}X_{2,i}R_{2,i},
 \qquad
 {d\over dt}\|r_i\|_2^2={2\over n}Z_{2,i}D_{2,i}R_{2,i},           \tag{22.1}
\]

and hence

\[
 {d\over dt}{\|c_i\|_2^2-\|r_i\|_2^2\over2}
 ={1\over n}R_{2,i}h(Z_{2,i}).                         \tag{22.2}
\]

Since (R_{2,i}=c_i^{\mathsf T}B_3), the compact-time (L^2) bound on
(B_3) implies

\[
 \operatorname{TV}_{[0,T]}\|r_i\|_2^2
 \leq\operatorname{TV}_{[0,T]}\|c_i\|_2^2
 \leq {C_T\over\sqrt n}
 \left(\|c_i(0)\|_2+{C_T\over\sqrt n}\right).          \tag{22.3}
\]

Thus a canonical middle row or column cannot acquire a large radial norm on
a compact interval.  Likewise, for each input coordinate (j), defining

\[
 V(s)=\int_0^s{\arctan r\over d(r)},dr
 =\Theta(s)\arctan s-{s^2\over6}-{1\over3}\log(1+s^2),             \tag{22.4}
\]

one has the exact balance law

\[
 {1\over2}\|G_{1,:j}(t)\|_2^2-{1\over n}V(u_j(t))
 ={1\over2}\|G_{1,:j}(0)\|_2^2-{1\over n}V(u_j(0)).    \tag{22.5}
\]

There is also an exact paired gauge.  Simultaneously flipping the sign of
row (i) of (Gamma_1) and column (i) of (Gamma_2) flips
(Z_{2,i},X_{2,i},R_{2,i},B_{2,i}) and leaves the top path and every other
middle coordinate unchanged.  Since the paired Gaussian block is symmetric,

\[
 \mathbb E[R_{2,i}(t)\mid\hbox{all other initial blocks}]=0.        \tag{22.6}
\]

Gaussian (L^q)-Poincare therefore gives the exact sufficient reduction

\[
 \|R_{2,i}(t)\|_q
 \leq C\sqrt q\,
 \big\|\|\nabla_{P_i}R_{2,i}(t)\|_2\big\|_q,            \tag{22.7}
\]

where (P_i=(\sqrt n\,\Gamma_{1,i:},\sqrt n\,\Gamma_{2,:i})).
A (C_T\sqrt q) bound on this paired tangent would prove the desired
(C_Tq) query envelope without a separate centering argument.

The factor identities do not prove (22.7)'s premise.  In the genuine
paired-zero cavity, the first unresolved forcing of the bottom state is

\[
 S_i(t)=B_{2,i}(t)D_1(t)r_i(t)^{\mathsf T},
 \qquad
 \|S_i(t)\|_n={|B_{2,i}(t)|\over\sqrt n}
               \|D_1(t)r_i(t)\|_2.                   \tag{22.8}
\]

Radial freezing controls the row factor but not the coordinate (B_{2,i}).
From exchangeability and global energy alone the sharp logarithmic-moment
bound is only (n^{-1/q}), which is order one at (q\asymp\log n).  At
(Z_{2,i}=0), both balance derivatives in (22.1) vanish even if
(B_{2,i}=\sqrt n), while (22.8) is order one.  This is a route falsifier,
not a reachable Gaussian trajectory.  It proves that balance and radial
freezing remove radial blow-up but cannot replace the open-gate
anti-localization theorem.

## 23. Transported gates, a proposed support spike, and its hostile audit

The lower forward equation has a simpler exact vector form than a diagonal
self/bath split suggests.  With

\[
 M_2=\|X_1\|_n^2I+G_1D_1^2G_1^{\mathsf T}\succeq0,
\]

one has

\[
 \dot Z_2=M_2B_2,
 \qquad
 \langle B_2,\dot Z_2\rangle_n
 =\|X_1\|_n^2\|B_2\|_n^2+\|D_1Q_1\|_n^2.             \tag{23.1}
\]

For \(L_{2,j}=\log(1+Z_{2,j}^2)\), exact differentiation gives

\[
 \dot L_{2,j}=2Z_{2,j}D_{2,j}(M_2B_2)_j,
 \qquad
 \dot B_{2,j}=D_{2,j}\dot R_{2,j}-\dot L_{2,j}B_{2,j}. \tag{23.2}
\]

Thus the integrating factor only recovers the tautology

\[
 e^{L_{2,j}(t)}B_{2,j}(t)=R_{2,j}(t);                  \tag{23.3}
\]

the terminal inverse gate is not removed.  Integrating the top learned
column gives the other exact reduction

\[
 R_{2,j}(t)=\Gamma_{2,:j}^{\mathsf T}B_3(t)
 +\int_0^tX_{2,j}(s)\langle B_3(s),B_3(t)\rangle_n\,ds. \tag{23.4}
\]

The second term is coordinatewise bounded on compact time from the known
\(L^2\) bounds.  The first is the genuinely adaptive Gaussian-column
projection.

A clean-room construction proposed a fixed-time support trajectory on which
that projection becomes \(\sqrt n\) while the middle gate closes and all
normalized actions remain bounded.  Its finite-dimensional scalings and
symmetry reduction survive audit.  In particular, for two lower row types
\(J,K\) and two input types \(+,-\), it produces an initially positive cross
coefficient

\[
 K_{JK}(0)=d_0^2\left({1\over nx_0^2}+\kappa n^{-3/4}\right),       \tag{23.5}
\]

and an exact local acceleration \(Z_{2,J}''(0)>0\).  The claimed
fixed-time conclusion does **not** survive the audit.  The favorable margin
in (23.5) is only \(O(n^{-3/4})\), whereas a crude compact-time change of the
distinguished row is \(O(t^2n^{-1/2})\).  Positivity of the full Gram matrix
does not imply positivity of its \((J,K)\) entry, and no uniform sign
bootstrap was supplied.  What is rigorous is only an \(n\)-dependent local
amplification interval.

Nor would topological support prove a canonical moment obstruction.  A
strict finite-\(n\) trajectory has a positive-probability Gaussian
neighborhood, but the probability can vanish super-exponentially with
\(n\).  Randomizing the special coordinate, signs, and partition leaves a
low-rank repeated-entry law, not the iid Gaussian initialization.  The
construction is therefore retained only as a route-level warning: no
support-uniform deterministic estimate may be assumed, while the canonical
annealed tail statement remains untouched.

## 24. Exact Gaussian moment flow and the weighted-response leaf

The most direct annealed moment calculation also isolates, rather than
removes, the same missing estimate.  Write

\[
 b=B_3,\qquad Y=\Gamma_2^{\mathsf T}b,
\]

so that (23.4) says \(R_2-Y\) is coordinatewise bounded.  For the raw column
\(c_j=\Gamma_{2,:j}\), define the full response

\[
 (H_j)_{ki}={\partial b_k\over\partial\Gamma_{2,ij}},
 \qquad \tau_j={1\over n}\operatorname{tr}H_j.          \tag{24.1}
\]

Gaussian integration by parts in the entries of \(\Gamma_2\) gives, for a
smooth \(\Phi\), the exact identity

\[
\begin{aligned}
 {d\over dt}\mathbb E\langle\Phi(Y)\rangle_n
={}&\mathbb E\!\left[
 \langle b,\dot b\rangle_n\langle\Phi''(Y)\rangle_n\right]\\
&+{1\over n^2}\sum_j\mathbb E\!\left[
 \Phi''(Y_j)\dot b^{\mathsf T}H_j^{\mathsf T}c_j\right]
 +\mathbb E\langle\Phi'(Y),\dot\tau\rangle_n .        \tag{24.2}
\end{aligned}
\]

For \(\Phi(y)=|y|^q\), normalized Hilbert--Schmidt control of the responses
only yields factors

\[
 \langle|Y|^{2q-4}\rangle_n^{1/2},\qquad
 \langle|Y|^{2q-2}\rangle_n^{1/2}.                    \tag{24.3}
\]

For \(\Phi(y)=\cosh(\lambda y)\), the same loss is
\(F_{2\lambda}^{1/2}\).  Adding the natural cross functional
\(\mathbb E\langle\Phi'(Y),\tau\rangle_n\) moves the last term but creates
\(\Phi''(Y)\dot Y\tau\).  A second Gaussian integration by parts
differentiates \(H_j\), creating a second response; repeating generates the
full response hierarchy because arctangent has nonzero derivatives at every
order.

This failure cannot be repaired from aggregate response energy.  Fix
\(q>2\), let \(J\) be uniform, \(\varepsilon\) an independent sign,
\(c=\Gamma_2e_J\), \(s=\|c\|_2^2\), and \(a=n^{1/q}\).  The smooth curve

\[
 b_0=\varepsilon{ac\over s},\qquad
 \dot b_0=\varepsilon{\sqrt n\,c\over\sqrt s}          \tag{24.4}
\]

is column-exchangeable and sign-symmetric and has bounded normalized state,
velocity, and first-response energies.  Nevertheless

\[
 Y_J(0)=\varepsilon n^{1/q},\qquad
 {d\over dt}\mathbb E\langle|Y(t)|^q\rangle_n\bigg|_{t=0}
 \ge c_q q n^{1/2-1/q}.                                \tag{24.5}
\]

Here \(\|\dot\tau\|_n=O(1)\), but its sole large coordinate is exactly
aligned with the rare \(Y_J\) spike.  This is not a reachable neural-flow
counterexample.  It proves sharply that Gaussianity, exchangeability, gauge
symmetry, operator bounds, and unweighted Hilbert--Schmidt response estimates
cannot close (24.2).

One sufficient reachable-state replacement is the weighted pair

\[
 \mathbb E\langle |Y|^{q-2}a^2\rangle_n
 \le C_T^2\mathbb E\langle|Y|^{q-2}\rangle_n,
 \qquad a_j=\|H_j^{\mathsf T}c_j\|_n,                  \tag{24.6}
\]

\[
 \mathbb E\langle |Y|^{q-2}|\dot\tau|^2\rangle_n
 \le C_T^2\mathbb E\langle|Y|^{q-2}\rangle_n.        \tag{24.7}
\]

Uniformly for \(q\lesssim\log n\), (24.2), (24.6), and (24.7) give
\(M_q'\le C_TM_q+C_Tq^2M_{q-2}\), hence
\(M_q^{1/q}\lesssim_Tq\).  The content of (24.6)--(24.7) is exactly a
reachable weighted response anti-alignment theorem.  It is a useful precise
target, not a consequence of the current estimates.

## 25. Exact action and the failure of continuous-history innovation control

There is a sharper exact form of the compact-time energy estimate.  Put
\(\alpha_\ell=\|X_\ell\|_n^2\) and
\(\Phi=\langle A,X_3\rangle_n\).  Directly from the feature flow,

\[
\boxed{
\dot\Phi
=\|X_3\|_n^2+\alpha_2\|B_3\|_n^2
 \alpha_1\|B_2\|_n^2+\|D_1Q_1\|_n^2 .}               \tag{25.1}
\]

The right side is exactly

\[
\|A'\|_n^2+\|G_2'\|_{\mathrm F}^2
+\|G_1'\|_{\mathrm F}^2+\|u'\|_n^2.                  \tag{25.2}
\]

Thus the full parameter action is bounded on compact feature intervals.
Moreover,

\[
|A d'(Z_3)|\le |B_3|,\qquad
|R_2d'(Z_2)|\le |B_2|,\qquad
|Q_1d'(u)|\le |D_1Q_1|,                              \tag{25.3}
\]

because \(2|z|d(z)\le1\).  Every raw Hessian multiplier is therefore a
gated backpropagation velocity at its natural layer.

This action does **not** justify a projection-BV argument for continuous
Gaussian conditioning.  Let \(\gamma=g/\sqrt n\) and first query the
deterministic path

\[
b(s)=(1,s,\ldots,s^{n-1}),\qquad 0<s<r<1.
\]

Noiseless knowledge of \(\gamma^{\mathsf T}b(s)\) on any interval determines
all coordinates of \(\gamma\) by the Vandermonde identity, although

\[
\|b'(s)\|_n^2\le {C_r\over n},\qquad
\sum_k\|(I-P_{k-1})\Delta b_k\|_n^2
\le h\int\|b'(s)\|_n^2ds=O(h).                       \tag{25.4}
\]

After the probing interval one may causally interpolate to
\(b_i=\tanh(Kg_i)\), keeping bounded coordinates and bounded normalized
speed, while

\[
\mathbb E[\gamma^{\mathsf T}b]
=\sqrt n\,\mathbb E[g\tanh(Kg)]\asymp\sqrt n.         \tag{25.5}
\]

The false inference is that a residual direction of amplitude
\(\varepsilon\) reveals only \(O(\varepsilon^2)\) information.  A noiseless
observation reveals the standardized coordinate after division by
\(\varepsilon\); information gain is rank, not quadratic mass.

The same failure persists abstractly after the arctan characteristic.
For iid \(g_i,a_i\), solve

\[
a_i'=\arctan z_i,\qquad
\Theta(z_i)'=\varepsilon a_i,\qquad z_i(0)=g_i,
\qquad b_i=d(z_i)a_i .
\]

For small fixed \(\varepsilon>0\),

\[
{d\over dt}\mathbb E[g\,b(t)]\bigg|_{t=0}
=\mathbb E[g\,d(g)\arctan g]
-2\varepsilon\mathbb E[g^2d(g)^3]>0,                 \tag{25.6}
\]

so \(\mathbb E[\gamma^{\mathsf T}b(t)]\asymp\sqrt n\) at a fixed small
time even though the mesh innovation mass is \(O(h)\).  This is not a
reachable-flow counterexample: the construction gives the tagged Gaussian
carrier order-one initial leverage instead of the canonical
\(n^{-1/2}\) leverage.  It proves that low influence, not (25.1), (25.4), or
the characteristic alone, is indispensable.

## 26. Column Jacobian and the exact characteristic tangent

Fix a middle column \(j\), put \(g=\sqrt n\,\Gamma_{2,:j}\), condition on all
other initial randomness, and define

\[
b(g,t)=B_3(t),\qquad J(t)=D_gb(g,t),\qquad
F(t)={1\over\sqrt n}g^{\mathsf T}b(g,t).
\]

Conditional Stein and Gaussian \(L^q\)-Poincare give

\[
\mathbb E_gF={1\over\sqrt n}\mathbb E_g\operatorname{tr}J,
\]

\[
\|F-\mathbb E_gF\|_q
\le {C\sqrt q\over\sqrt n}
\left(\|b\|_{L^q(\ell_2)}
+\|J^{\mathsf T}g\|_{L^q(\ell_2)}\right).             \tag{26.1}
\]

Consequently

\[
\|F(t)\|_q\le C_T\sqrt q
\left(1+\big\|\|J(t)\|_{\rm HS}\big\|_{2q}\right),    \tag{26.2}
\]

and the model-specific estimate

\[
\boxed{
\big\|\|D_gB_3(t)\|_{\rm HS}\big\|_{2q}
\le C_T\sqrt q,\qquad q\le c_T\log n}                 \tag{26.3}
\]

would imply the required \(C_Tq\) middle-query moments.  It initializes at
the correct scale:

\[
J(0)={X_{2,j}(0)\over\sqrt n}
\operatorname{diag}\!\big(A_0d'(Z_3(0))\big).         \tag{26.4}
\]

A diagonal weak-carrier benchmark proves that this scaling is enough when
off-diagonal transport is absent.  Take
\(z_i(0)=w_i+\beta_i g_i/\sqrt n\), put
\(\psi(\theta)=\arctan(\Theta^{-1}\theta)\), and note
\(\psi'=d^2\le1\).  The initial-data tangent has the two-scalar form
\(p'=\psi'r,\ r'=\lambda p\), whence

\[
|\partial_{g_i}b_i|
\le {C_T\over\sqrt n}(1+z_i(0)^2)(1+|a_i(0)|).
\]

Stein gives an \(O(n^{-1})\) mean per row, while
\(|g_ib_i|\le|g_i|(|a_i|+C_T)\).  Bernstein therefore yields

\[
\left\|{1\over\sqrt n}\sum_i g_ib_i\right\|_q
\le C_T\left(1+\sqrt q+{q\over\sqrt n}\right).        \tag{26.4a}
\]

Thus the characteristic plus canonical \(n^{-1/2}\) leverage closes the
diagonal model.  Preservation of that low influence under the mean-field
off-diagonal transport is precisely what is open.

Differentiating the full ODE gives a finite closed first-response system; no
second response is needed merely to write it.  For a directional derivative
\(\delta\), set

\[
a=\delta A,\quad v=\delta u,\quad W_\ell=\delta G_\ell,
\quad W_2(0)={q e_j^{\mathsf T}\over\sqrt n},
\]

and define

\[
\begin{aligned}
\chi_1&=D_1v,\\
\zeta_2&=W_1X_1+G_1\chi_1,&\chi_2&=D_2\zeta_2,\\
\zeta_3&=W_2X_2+G_2\chi_2,&\chi_3&=D_3\zeta_3,\\
\beta_3&=D_3a+E_3(A\odot\zeta_3),\\
\rho_2&=W_2^{\mathsf T}B_3+G_2^{\mathsf T}\beta_3,\\
\beta_2&=D_2\rho_2+E_2(R_2\odot\zeta_2),\\
\eta_1&=W_1^{\mathsf T}B_2+G_1^{\mathsf T}\beta_2 .
\end{aligned}                                         \tag{26.4b}
\]

Here \(E_\ell=\operatorname{diag}(d'(Z_\ell))\).  The exact tangent ODE is

\[
\begin{aligned}
\dot a&=\chi_3,\\
\dot v&=D_1\eta_1+E_1(Q_1\odot v),\\
\dot W_1&={1\over n}(\beta_2X_1^{\mathsf T}
                    +B_2\chi_1^{\mathsf T}),\\
\dot W_2&={1\over n}(\beta_3X_2^{\mathsf T}
                    +B_3\chi_2^{\mathsf T}).
\end{aligned}                                         \tag{26.4c}
\]

Thus \(J_j(t)q=\beta_3(t)\).  In the characteristic
variables \(V_\ell=\delta Z_\ell/d(Z_\ell)\), every diagonal self-curvature
cancels.  If

\[
P_2=G_1D_1^2G_1^{\mathsf T},\quad
K_2=\|X_1\|_n^2I+P_2,\quad
P_3=G_2D_2K_2D_2G_2^{\mathsf T},
\]

then the surviving signed off-diagonal transport at layer \(\ell=2,3\) is

\[
(\mathcal L_\ell V)_i
={1\over d_{\ell,i}}\sum_{k\ne i}(P_\ell)_{ik}B_{\ell,k}
\big(e_{\ell,k}V_k-e_{\ell,i}V_i\big),                \tag{26.5}
\]

where \(e=d'\).  Coefficient variations and the two differentiated learned
memories remain, but only at first response order.

No positive diagonal symmetrizer exists in general: on each nonzero edge it
would require \(B_ie_i\) to have one sign throughout the connected
component.  A deterministic Gram counterexample makes this obstruction
sharp.  For

\[
P=\begin{pmatrix}I_m&W\\W^{\mathsf T}&I_{n-m}\end{pmatrix},
\qquad WW^{\mathsf T}=r^2I_m,
\]

take \(B_D=L{\bf1}\) and
\(B_{D^c}=-(2L/r^2)W^{\mathsf T}{\bf1}\).  Then
\(((I+P)B)_D=0\), the normalized \(B\)-energy stays bounded for
\(m\asymp n/L^2\), yet at \(Z_D=-1\)

\[
\langle V,\mathcal LV\rangle=2L\|V_D\|^2.             \tag{26.6}
\]

This construction has the exact PSD Gram form and may be exchangeabilized,
but it is not a likely canonical Gaussian orbit.  It falsifies deterministic
closures from PSD, operator/Frobenius energy, exchangeability, or a local
positive tangent Lyapunov.

At initialization the off-diagonal field is better: deleting top row \(i\)
makes it conditionally centered Gaussian, with

\[
\|c_i\|_{L^q(\cdot\mid\mathcal F_{-i})}
\le C\sqrt q\,\|\Sigma_2\|_{\rm op}
\|\Gamma_{2,-i}\|_{\rm op}\|B_3\|_n.                 \tag{26.7}
\]

Training destroys this exact independence.  Gaussian integration by parts
then differentiates the first response and starts the already identified
higher-response tower.

## 27. Two-scalar crossing reduction and the exact failure of naive cavity

Fix \(i\), let

\[
M=\|X_1\|_n^2I+G_1D_1^2G_1^{\mathsf T},\quad
c=\Gamma_{2,:i},\quad y=c^{\mathsf T}B_3,\quad z=Z_{2,i}.
\]

The learned part \(\ell_i=R_{2,i}-y\) is the bounded integral in (23.4).
Writing

\[
S=\operatorname{diag}(A d'(Z_3)),\qquad v=G_2^{\mathsf T}Sc,
\]

the exact equations reduce to

\[
\boxed{
z'=m b+h,\qquad y'=k b+\eta,\qquad
b=d(z)(y+\ell_i),}                                    \tag{27.1}
\]

where

\[
\begin{aligned}
m&=M_{ii},&
h&=\sum_{j\ne i}M_{ij}B_{2,j},\\
k&=(MD_2v)_i,&
\eta&=c^{\mathsf T}(D_3X_3+\|X_2\|_n^2SB_3)
      +\sum_{j\ne i}(MD_2v)_jB_{2,j}.
\end{aligned}                                         \tag{27.2}
\]

Thus the same open-gate scalar \(b\) drives both coordinates.

There is a complete deterministic consequence.  Suppose on \([0,T]\)
\(0<m_0\le m\le m_1\), \(|\ell|\le C_0\), \(L\ge4C_0\), and \(y\) first
crosses from \(L/2\) to \(L\).  Put

\[
K=\sup|k|,\qquad H=\int|h|,\qquad E=\int|\eta|.
\]

On the crossing interval \(b\) has fixed sign.  Comparing the \(z\)-equation
with the cubic characteristic yields

\[
\boxed{
L\le C_TK\big(1+|z(0)|+H+L^{1/3}\big)+4E.}            \tag{27.3}
\]

Hence sub-Gaussian tails for \(K\) and \(1+|z(0)|+H\), together with a
subexponential tail for \(E\), imply an \(e^{-c_TL}\) crossing bound.
Independence between these three quantities is not required.

They are not presently known to have those tails.  In particular, full
\(k\) and \(h\) are not conditionally independent.  The learned exceptional
row gives the exact term

\[
h_i(t)
=a^{\mathsf T}v(t)
+\int_0^tB_{2,i}(s)
\langle X_1(s),v(t)\rangle_n\,ds,                    \tag{27.4}
\]

where \(a=\Gamma_{1,i:}\) and
\(v=D_1^2\sum_{j\ne i}G_{1,j:}^{\mathsf T}B_{2,j}\).
The integral may be \(O(L)\).  It is an order-one causal self-memory, not an
\(O(L/\sqrt n)\) cavity error.  Equation (27.4) is the first exact failure of
the naive paired leave-out argument.

## 28. Audited pause frontier: joint dynamic cavity, not a completed lemma

Two equivalent-looking sufficient targets survive.

The value-level version is a Schur--Volterra paired cavity expansion:
remove \((\Gamma_{1,i:},\Gamma_{2,:i})\), retain every order-one return of
that pair as a bounded causal kernel in (27.1), and prove that the remaining
row- and column-side carriers have the sub-Gaussian/subexponential bounds
needed in (27.3), uniformly through \(q\lesssim\log n\).  A useful stopped
form would take \(L_*=n^{1/16}\) and prove a remainder

\[
\left\|\int_0^{T\wedge\tau_*}
(|\varepsilon_z|+|\varepsilon_y|)\,dt\right\|_q
\le C_Tq^4{L_*^2\over\sqrt n},                        \tag{28.1}
\]

together with uniformly bounded Volterra resolvents and a positive lower
bound for \(m\).

The response-level version is a joint multi-row cavity estimate for

\[
Y_r=n\|J_je_r\|_2^2.
\]

It is enough to prove, for distinct \(i_a\) and
\(\sum_am_a=M\le c_T\log n\),

\[
\mathbb E\prod_aY_{i_a}^{m_a}
\le K_T^M\exp\!\left(C_T\sum_am_a^2\right).           \tag{28.2}
\]

Expanding \(\mathbb E(n^{-1}\sum_rY_r)^q\) by collision pattern then gives
(26.3).  This explains why separate row moments are insufficient: a common
lognormal factor can make every row individually lognormal while the
empirical Hilbert--Schmidt response has exponentially growing moments.

Neither (28.1) nor (28.2) has been proved.  The proposed power count that a
second unresolved excursion costs \(L_*^2/n\), the boundedness of every
renormalized causal kernel, the uniform lower bound for \(m\) after the
full/cavity comparison, and the \(q\)-uniform conditional carrier bounds are
all substantive missing steps.  They cannot be entered as a finite
enumeration already completed.

The exact action (25.1), characteristic cancellation (26.5), diagonal
weak-carrier benchmark, and crossing lemma (27.3) show why such a theorem is
dimensionally plausible.  The counterexamples in (25.4)--(25.6) and (26.6)
show why innovation mass, PSD, global action, marginal row moments, or
full-history conditioning cannot prove it.  No canonical-flow
counterexample was found, and no proof of C-13 was obtained.
