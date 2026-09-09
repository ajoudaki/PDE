# Joint middle-query energy: an exact top cancellation and its residual

Status: exact finite-width identities for the actual trained network,
including a finite full/pruned pair. The correction below cancels the
pure middle-input third derivative of the top query. It leaves a specified
mixed trained-top pairing and the actual mobility difference. Neither is
estimated sufficiently to close global comparison here.

No Gaussian tail estimate, frozen top operator, or replacement of the
actual trained mobility is used. The deterministic identities need only
the established finite-feature-time primal/operator bounds and a bound
on the initial readout infinity norm. Thus they apply on the corresponding
events for zero or prescribed tiny initial readout. This is not a
global transfer between those initializations.

## 1. Exact top decomposition

Use normalized vector norms \(\|u\|_n=\|u\|_2/\sqrt n\), normalized inner
products, ordinary matrix Frobenius norms, and \(u\otimes v=uv^\top/n\).
Write
\[
\begin{gathered}
 h=h^{(2)},\quad W=W^{(3)},\quad z=Wh,\quad \eta=\phi(z),\\
 D=\operatorname{diag}(\phi'(z)),\quad
 B=\operatorname{diag}(C\phi''(z)),\quad d=DC,\quad
 q=W^\top d,\quad m=\|h\|_n^2 .
\end{gathered}
\]
Here \(\phi=\arctan\), and \(C=W^{(4)}\). The actual trained equations are
\[
 W'=d\otimes h,\qquad C'=\eta,\qquad
 z'=md+Wh'.
\]
In particular \(d\) is bounded coordinatewise on any fixed feature
interval. Direct differentiation, retaining \(W'\), gives
\[
\begin{split}
 q'&=g+S h',\\
 S&=W^\top BW=S^\top,\\
 g&=h\|d\|_n^2+W^\top D\eta+mW^\top Bd .                \tag{1}
\end{split}
\]
The actual lower layers give
\[
 h'=M_2q,\qquad M_2=D_2A_2D_2,\qquad
 A_2=m_1I+W^{(2)}D_1^2(W^{(2)})^\top,\quad
 m_1=\|h^{(1)}\|_n^2 .                                  \tag{2}
\]
Thus \(M_2\) is positive semidefinite, while \(S\) is self-adjoint
but need not be positive. The primal bounds give
\[
 \|S\|_{\rm op}+\|M_2\|_{\rm op}+\|g\|_n+\|h'\|_n
                                                       \le C_S.
\]
The formula \(q'=g+SM_2q\) has a bounded \(L^2\) generator along the
actual path. This fact alone does not estimate differences of its
coefficients.

## 2. The corrected tangent query

Consider an actual initial-data variation, differentiating all trained
blocks. For its top variables write
\[
 e=\delta h,\qquad V=\delta W,\qquad c=\delta C,\qquad
 \zeta=Vh+We,\qquad \rho=Dc+B\zeta .
\]
The complete top tangent equations are
\[
 V'=\rho\otimes h+d\otimes e,\qquad
 c'=D\zeta,\qquad
 \delta q=V^\top d+W^\top\rho .                         \tag{3}
\]
Subtract the top Hessian response to the middle input:
\[
\begin{split}
 r&=\delta q-Se\\
  &=V^\top d+W^\top Dc+W^\top BVh .
                                                               \tag{4}
\end{split}
\]
This is already a bounded algebraic map:
\[
 \|r\|_n\le C_S(\|V\|_{\rm F}+\|c\|_n).                 \tag{5}
\]
The purpose of differentiating it is to test a joint dynamic energy,
not to supply a new bound for this algebraic quantity.

The exact derivative has a cancellation:
\[
 r'=L_t(e,V,c)
       +W^\top\big[
         (\phi''(z)c+C\phi'''(z)Vh)\odot Wh'\big],
                                                               \tag{6}
\]
where
\[
 \|L_t(e,V,c)\|_n\le C_S(\|e\|_n+\|V\|_{\rm F}+\|c\|_n).
                                                               \tag{7}
\]
In particular, the potentially large term
\[
 W^\top\big[C\phi'''(z)(We)\odot Wh'\big]
\]
has canceled. It occurs both in the variation of \(S h'\) and in
the time derivative of \(Se\). The remaining term in (6) instead
contains the trained top-parameter variations \(c,V\).

Here is a complete formula verifying (6)--(7). Put
\(\delta m=2\langle h,e\rangle_n\), and let
\[
\begin{split}
 \delta g={}&e\|d\|_n^2+2h\langle d,\rho\rangle_n
       +V^\top D\eta
       +W^\top[(\phi''(z)\eta+\phi'(z)^2)\odot\zeta]\\
 &+\delta m\,W^\top Bd+mV^\top Bd\\
 &+mW^\top[
          (\phi''(z)c+C\phi'''(z)\zeta)\odot d+B\rho].
\end{split}
\]
The part of \(S'\) produced by the trained top parameters alone,
with \(h\) held fixed, is
\[
\begin{split}
 \dot S_\theta={}&(d\otimes h)^\top BW+
                    W^\top B(d\otimes h)\\
 &+W^\top\operatorname{diag}
           (\eta\phi''(z)+mC\phi'''(z)d)W .
\end{split}
\]
It has bounded operator norm, because \(d,C,\eta\) are bounded
coordinatewise. Then exactly
\[
 L_t=\delta g+V^\top BWh'+W^\top BVh'-\dot S_\theta e .
                                                               \tag{8}
\]
Every displayed term in \(\delta g\) is bounded in \(L^2\) by the
right side of (7). For example the factor \(d\) in
\((\phi''c+C\phi'''\zeta)\odot d\) is bounded coordinatewise.
The last two matrix-action terms in (8) need only
\(\|h'\|_n\le C_S\), not a coordinate bound for \(h'\).

Consequently the corrected-query energy is exactly
\[
 \frac12(\|r\|_n^2)'
    =\langle r,L_t(e,V,c)\rangle_n
      +\left\langle Wr,\,
          (\phi''(z)c+C\phi'''(z)Vh)\odot Wh'
        \right\rangle_n .                              \tag{9}
\]
The ordinary top-parameter energy contributes
\[
 \frac12(\|V\|_{\rm F}^2+\|c\|_n^2)'
   =\langle Vh,\rho\rangle_n+\langle Ve,d\rangle_n
                              +\langle c,D\zeta\rangle_n.
                                                               \tag{10}
\]
It has no \(h'\)-term that cancels the last pairing in (9).
Separate \(L^2\) bounds on its three factors do not estimate that
pairing by the squared tangent norm.

This does not show instability: \(r\) has the bounded algebraic
estimate (5). The product in (9) is a cost introduced by treating
the corrected query as a dynamic energy variable.

## 3. Exact finite full/pruned version

The cancellation has a finite-pair form. Let hats denote a second actual
trained top trajectory; it may be the fully pruned reference. In the
pruned case use its actual input
\(\widehat h=Q_E\phi(\widehat z^{(2)})\), not the unused activation
on \(E\). Both top parameter blocks train through their respective
inputs. Set
\[
 e=h-\widehat h,\quad V=W-\widehat W,\quad c=C-\widehat C,
 \quad \Delta q=q-\widehat q,\quad
 d_{\rm top}=\|e\|_n+\|V\|_{\rm F}+\|c\|_n.
\]
For \(0\le\lambda\le1\), put
\[
\begin{gathered}
 h_\lambda=\widehat h+\lambda e,\quad
 W_\lambda=\widehat W+\lambda V,\quad
 C_\lambda=\widehat C+\lambda c,\quad z_\lambda=W_\lambda h_\lambda,\\
 D_\lambda=\operatorname{diag}\phi'(z_\lambda),\quad
 B_\lambda=\operatorname{diag}(C_\lambda\phi''(z_\lambda)),\quad
 d_\lambda=D_\lambda C_\lambda,\quad
 S_\lambda=W_\lambda^\top B_\lambda W_\lambda .
\end{gathered}
\]
These are recomputed segment quantities; they are not assumed to solve
the network equations. The secant formula gives
\[
\begin{split}
 \overline S&=\int_0^1S_\lambda\,d\lambda,\qquad
 r=\Delta q-\overline S e=\int_0^1 r_\lambda\,d\lambda,\\
 r_\lambda&=V^\top d_\lambda+
      W_\lambda^\top D_\lambda c+
      W_\lambda^\top B_\lambda Vh_\lambda .
                                                               \tag{11}
\end{split}
\]
Thus \(\|\overline S\|_{\rm op}\le C_S\) and
\(\|r\|_n\le C_S(\|V\|_{\rm F}+\|c\|_n)\).

There is a useful actual-training fact in differentiating (11).
Let
\[
 a_\lambda=W_\lambda' h_\lambda .
\]
The interpolated matrix derivative is
\[
 W_\lambda'=(1-\lambda)\widehat d\otimes\widehat h+
                                      \lambda d\otimes h.
\]
Hence \(\|a_\lambda\|_\infty\le C_S\); this is a consequence of the
trained rank-one formula and the bounded top backward coordinates,
not of an \(L^2\)-operator-to-\(L^\infty\) claim. Also
\[
 z_\lambda'=a_\lambda+W_\lambda h_\lambda',\qquad
 \|h_\lambda'\|_n+\|d_\lambda'\|_n\le C_S,\qquad
 \|C_\lambda'\|_\infty\le \pi/2 .
\]
The bounded top maps and their exact trained equations give
\[
 \|V'\|_{\rm F}+\|c'\|_n\le C_Sd_{\rm top}.             \tag{12}
\]

Differentiate (11). Exactly,
\[
\begin{split}
 r'&={\cal L}+{\cal G},\qquad
       \|{\cal L}\|_n\le C_Sd_{\rm top},\\
 {\cal G}
 &=\int_0^1 W_\lambda^\top
   \big[(\phi''(z_\lambda)c+
       C_\lambda\phi'''(z_\lambda)Vh_\lambda)
                         \odot W_\lambda h_\lambda'\big]
                                                    \,d\lambda .
                                                               \tag{13}
\end{split}
\]
For a fully explicit verification, set
\[
 B_{\lambda,\theta}'=
 \operatorname{diag}\big[
     C_\lambda'\phi''(z_\lambda)
          +C_\lambda\phi'''(z_\lambda)a_\lambda\big],
 \qquad \|B_{\lambda,\theta}'\|_{\rm op}\le C_S .
\]
The integrand of \({\cal L}\) is
\[
\begin{split}
 {\cal L}_\lambda={}&
       (V')^\top d_\lambda+V^\top d_\lambda'
       +(W_\lambda')^\top D_\lambda c
       +W_\lambda^\top D_\lambda c'\\
 &+W_\lambda^\top
               [\phi''(z_\lambda)a_\lambda\odot c]\\
 &+(W_\lambda')^\top B_\lambda Vh_\lambda
       +W_\lambda^\top B_{\lambda,\theta}'Vh_\lambda\\
 &+W_\lambda^\top B_\lambda V'h_\lambda
       +W_\lambda^\top B_\lambda Vh_\lambda' .
\end{split}
\]
Each term is bounded by \(C_Sd_{\rm top}\), using (12), the bounded
operator norms, and the coordinate bound for \(a_\lambda\).
This proves (13) without differentiating a guessed inequality.

For a full/pruned pair with the same initial top matrix, rank-one
memory additionally gives
\[
 \|V(t)h_\lambda(t)\|_\infty\le C_S.
\]
Indeed insert \(V(t)=\int_0^t
 (d\otimes h-\widehat d\otimes\widehat h)\,ds\) and use bounded
coordinates of \(d,\widehat d\) and bounded normalized norms of both
inputs. Therefore the vector inside each \(W_\lambda^\top\) in
\({\cal G}\) is uniformly bounded in \(L^2\) and has \(L^1\) norm at most
\(C_Sd_{\rm top}\). This is a genuine bounded/small-\(L^1\) structure,
but (13) is an uncompressed action on the whole middle layer.
The existing singly pruned Gaussian lemmas do not by themselves make
this uncompressed vector \(L^2\)-small: \(W_\lambda\) also contains
the actual, reused matrix, and depends on \(\lambda\) and both paths.

## 4. The joint energy retains the actual mobility difference

For the fully pruned reference, define
\[
 \widehat M_2
   =Q_E\widehat D_2\widehat A_2\widehat D_2Q_E .
\]
It is positive semidefinite and
\(\widehat h'=\widehat M_2\widehat q\), with the unused query
\(\widehat q\) kept in this formula. Thus the exact middle comparison is
\[
 e'=M_2(\overline S e+r)
                         +(M_2-\widehat M_2)\widehat q . \tag{14}
\]
All trained lower-layer factors remain in \(A_2,\widehat A_2\);
neither is replaced by an independent or fixed mobility.

For a fixed \(\kappa>0\), consider the positive joint component energy
\[
 {\cal E}_\kappa
   =\tfrac12\big(\|e\|_n^2+\kappa\|r\|_n^2+
                           \|V\|_{\rm F}^2+\|c\|_n^2\big).
\]
Since \(\overline S\) is bounded, its first two terms are uniformly
equivalent to the joint norm in \((e,\Delta q)\), with constants
depending on \(\kappa,S\). This is not a norm of all lower-layer
parameters.

Using (12)--(14) gives the exact residual decomposition
\[
 {\cal E}_\kappa'={\cal B}_\kappa
   +\langle e,(M_2-\widehat M_2)\widehat q\rangle_n
   +\kappa\langle r,{\cal G}\rangle_n,\qquad
 |{\cal B}_\kappa|\le C_{S,\kappa}{\cal E}_\kappa .       \tag{15}
\]
Here \({\cal B}_\kappa=
\langle e,M_2(\overline S e+r)\rangle_n+
\kappa\langle r,{\cal L}\rangle_n+
\langle V,V'\rangle_{\rm F}+\langle c,c'\rangle_n\).
The second residual is explicitly
\[
 \langle r,{\cal G}\rangle_n
 =\int_0^1
   \left\langle W_\lambda r,\,
      (\phi''(z_\lambda)c+
        C_\lambda\phi'''(z_\lambda)Vh_\lambda)
                 \odot W_\lambda h_\lambda'\right\rangle_n
                                                       \,d\lambda .
                                                               \tag{16}
\]
The positivity of each mobility does not give a sign to their difference
in (15). The exact top cancellation eliminates the pure middle-input
third derivative, but not (16). Ordinary top-parameter energies have no
velocity \(h_\lambda'\) term that cancels (16); their contribution has
already been bounded in (15).

Keeping \(r\) algebraic instead of differentiating it avoids (16), but
then its bound supplies no new estimate for the remaining mobility
feedback in (14). Thus this route has not improved the unresolved
signed covariance estimate in ACTUAL_BACKPROP_PRIMITIVE_RESPONSE.md.
The positive result is the exact tangent and finite-pair cancellation
(6), (13), including its actual rank-training bounds. The precise
remaining terms for this proposed joint energy are (15)--(16), not
a generic assertion about positive operators or gradient systems.
