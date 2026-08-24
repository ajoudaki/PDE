# Audit: leverage entropy and full-tangent spectral control

## Verdict

Neither row entropy, a fixed Rényi/IPR functional, nor an ambient
full-tangent Schatten bound closes the column-response estimate required by
the frozen contract.  The failures are structural:

1. the target response \(J=D_gB_3\) is not a restartable state;
2. empirical exponential moments valid for a fresh Gaussian row fail for an
   adapted arctan query;
3. the full tangent contains exact unstable saddle directions invisible to
   \(J\).

These results reject the proposed invariants.  They do **not** refute the
desired probabilistic bound for the canonical iid initialization.  The
surviving object would have to be a target-specific covariant or quotient
response which retains both differentiated memories while removing tangent
directions that cannot reach \(B_3\).

## Exact coupled column response

Put

\[
 D_r=\operatorname{diag}d(Z_r),\qquad
 E_r=\operatorname{diag}d'(Z_r),\qquad d(z)=(1+z^2)^{-1}.
\]

For the standard-Gaussian coordinates
\(g=\sqrt n\,\Gamma_{2,:,j}\), write, column by column,

\[
 P=D_gA,\quad W=D_gr,\quad U=D_gu=D_1W,\quad H_r=D_gG_r,\quad
 V_r=D_gZ_r,\quad Y_r=D_gX_r,
 \quad J=D_gB_3,\quad K_2=D_gB_2.
\]

Direct differentiation gives

\[
\begin{aligned}
Y_1&=D_1U=D_1^2W,\\
V_2&=H_1X_1+G_1Y_1,&Y_2&=D_2V_2,\\
V_3&=H_2X_2+G_2Y_2,&Y_3&=D_3V_3,\\
J&=D_3P+\operatorname{diag}(A d'(Z_3))V_3,\\
D_gR_2&=H_2^*B_3+G_2^*J,\\
K_2&=D_2D_gR_2+\operatorname{diag}(R_2d'(Z_2))V_2,\\
D_gQ_1&=H_1^*B_2+G_1^*K_2.
\end{aligned}
\]

The differentiated flow is

\[
\begin{aligned}
P'&=Y_3,&W'&=D_gQ_1,\\
(H_1^{(k)})'&=n^{-1}
  \{K_{2,:k}X_1^\top+B_2Y_{1,:k}^\top\},\\
(H_2^{(k)})'&=n^{-1}
  \{J_{:k}X_2^\top+B_3Y_{2,:k}^\top\}.
\end{aligned}
\]

At time zero,

\[
 H_2^{(k)}(0)=n^{-1/2}e_ke_j^\top,\qquad
 P(0)=W(0)=U(0)=H_1(0)=0,
\]

and hence

\[
 V_3(0)=n^{-1/2}X_{2,j}I,\qquad
 J(0)=n^{-1/2}X_{2,j}
       \operatorname{diag}(A_i d'(Z_{3,i})).
\]

Thus the prescribed source has the favorable diffuse Frobenius scale

\[
 \|J(0)\|_{\rm HS}
 \le \frac\pi2\|d'\|_\infty\|A\|_n.
\]

The two differentiated rank-one memories in the displayed ODE are
unavoidable.  Present row energies of \(J\) alone do not determine their
future contribution.

## Exact entropy identities and failure of closure

Let

\[
 e_i=\|J_{i,:}\|_2^2,\quad S=\sum_ie_i,\quad
 w_i=e_i/S,
\]

and, for \(e_i>0\),

\[
 \gamma_i=\frac{\langle J_{i,:},J'_{i,:}\rangle}{e_i},
 \qquad \bar\gamma=\sum_iw_i\gamma_i.
\]

Then

\[
 w_i'=2w_i(\gamma_i-\bar\gamma)
\]

and the relative entropy and Rényi masses obey the exact identities

\[
 \left(\sum_iw_i\log(nw_i)\right)'
 =2\sum_iw_i(\gamma_i-\bar\gamma)\log(nw_i),
\]

\[
 \left(\sum_iw_i^q\right)'
 =2q\sum_iw_i^q(\gamma_i-\bar\gamma).
\]

There is no sign.  Entropy duality only replaces the problem by empirical
exponential moments of the adapted growth rates:

\[
 \sum_iw_i a_i\le\lambda^{-1}\left\{
 \sum_iw_i\log(nw_i)+
 \log\left(n^{-1}\sum_ie^{\lambda a_i}\right)\right\}.
\]

Moreover bounded entropy is too weak to exclude leverage spikes.  Taking

\[
 w_1=(\log n)^{-1},\qquad
 w_i=\frac{1-(\log n)^{-1}}{n-1}\quad(i>1)
\]

keeps the relative entropy \(O(1)\), while its average against
\(a_1=\sqrt n,a_i=0\) equals \(\sqrt n/\log n\).  Fixed Rényi functionals have
the analogous nonclosure because a row with weight \(n^{-1/2}\) and local
growth \(\sqrt n\) has bounded IPR but order-\(\sqrt n\) relative IPR growth.

## Fresh versus adapted Gaussian exponential moments

If \(G_{ik}\sim N(0,1/n)\) and \(x\) is independent of the rows of \(G\), with
\(\|x\|_n\le L\), a direct multiplicity expansion proves, for fixed
\(\lambda,L\) and \(p\le c\log n\),

\[
 \left\|n^{-1}\sum_i e^{\lambda|(Gx)_i|}\right\|_p\le C.
\]

Independence is essential.  If \(r\) is the first row of \(G\), put
\(\xi_k=\sqrt n\,r_k\) and choose the bounded adapted arctan vector
\(x_k=\arctan\xi_k\).  Then

\[
 (Gx)_1=\sqrt n\,n^{-1}\sum_k\xi_k\arctan\xi_k.
\]

Since \(\mu=\mathbb E[\xi\arctan\xi]>0\), this is at least
\(\mu\sqrt n/2\) with probability \(1-O(n^{-1})\).  Consequently its
empirical exponential moment grows at least as
\(n^{-1}e^{\lambda\mu\sqrt n/2}\).  Bounded arctan features therefore do not
turn an adapted transpose query into a fresh Gaussian one.

## Two restartability counterexamples

First take a canonical equilibrium with \(A=0,G_2=0,X_2\ne0\).  Then the
base flow is stationary and, for tangent data,

\[
 J=P,\qquad J'=H_2X_2.
\]

For any nonzero \(P\), the two choices

\[
 H_2^{\pm,(k)}=
 \pm c P_{:k}\frac{X_2^\top}{\|X_2\|_2^2}
\]

have identical \(J\), row entropy, all row Rényi masses, IPR,
\(JJ^\top\), and every trace-exponential functional of \(JJ^\top\), but
\(J'_{\pm}=\pm cJ\).  Thus no \(J\)-only functional gives a restartable
autonomous differential inequality for the full tangent.  This statement
does not claim that both artificial tangent states arise from the prescribed
initial column injection.

Second, for \(n=1\), take the exact equilibrium

\[
 u=u_*,\quad c=\arctan u_*\ne0,\quad G_1=G_2=0,\quad A=M.
\]

The weight tangent contains

\[
 \delta G_1'=Mc\,\delta G_2,\qquad
 \delta G_2'=Mc\,\delta G_1,
\]

and therefore grows as \(\cosh(Mct)\).  Yet \(Z_3\) is quadratic in these two
directions at that equilibrium, so \(J=D_gB_3\equiv0\) to first order.  If
\(M\) is Gaussian, the ambient tangent has \(L^p\) growth of order
\(e^{c^2t^2p/2}\) while the target is identically zero.  Bounding the target
by the complete tangent therefore destroys a real cancellation.

## Surviving obligation

A successful spectral argument must construct a response operator
\(\mathcal V\) that is closed under both differentiated memories and projects
exactly onto \(D_gB_3\), while quotienting the invisible saddle.  Its source
must retain the diffuse singular-value scale
\(n^{1/(2q)-1/2}\) in \(S_{2q}\), and its generator must be controlled without
replacing empirical \(A,B_2,B_3\) moments by coordinate maxima.  No such
covariant response has yet been constructed.
