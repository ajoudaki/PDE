# Actual network logarithmic comparison and singular-value distortion

Status: exact finite-width identities and a width-normalized logarithmic
distortion bound. The coordinatewise logarithmic estimates below do not close
the full/pruned comparison. The determinant bound does not imply a trace,
Frobenius response moment, or all-finite-time population theorem.

The probabilistic full/pruned application below uses the ZERO-initial-readout
Gaussian hidden-weight proxy and its genuinely fully pruned reference.
It does not remove the canonical tiny Gaussian readout globally. The
deterministic Jacobian statements hold on any finite interval on which the
stated primal bounds hold. We prove them for the uncut flow. A fixed smooth
middle clipping with \(|\tau(q)|\le |q|\), \(|\tau'(q)|\le1\) has the same
Jacobian estimates, as explained below; no event uniform over all clippings
is asserted.

## 1. Normalization and the exact finite-dimensional field

Write
\[
 \langle u,v\rangle_n=\frac{u^\top v}{n},\qquad
 \|u\|_n=\frac{\|u\|_2}{\sqrt n},\qquad
 u\otimes v=\frac{uv^\top}{n}.
\]
Matrix norms \(\|\cdot\|_{\rm F}\) and \(\|\cdot\|_{\rm op}\) are the ordinary
Frobenius and Euclidean operator norms. In particular
\(\|u\otimes v\|_{\rm F}=\|u\|_n\|v\|_n\).

Let \(\phi(z)=\arctan z\), \(a=\pi/2\), \(F(z)=z+z^3/3\), and
\(\chi(X)=\phi(F^{-1}(X))\). The transformed state and its Hilbert norm are
\[
 \Theta=(X,W^{(2)},W^{(3)},C),\qquad
 \|\Theta\|_{\mathcal H_n}^2
 =\|X\|_n^2+\|W^{(2)}\|_{\rm F}^2+
                  \|W^{(3)}\|_{\rm F}^2+\|C\|_n^2.
\]
Its dimension is \(N=2n^2+2n\). Adjoint, nuclear norm, singular value, and
determinant for state-space operators below refer to this Hilbert metric,
or equivalently to an orthonormal basis for it.

Put
\[
\begin{gathered}
 h^{(1)}=\chi(X),\quad z^{(1)}=F^{-1}(X),\quad
 z^{(2)}=W^{(2)}h^{(1)},\quad h^{(2)}=\phi(z^{(2)}),\\
 z^{(3)}=W^{(3)}h^{(2)},\quad h^{(3)}=\phi(z^{(3)}),\quad
 D_\ell=\operatorname{diag}\big((1+(z^{(\ell)})^2)^{-1}\big),\\
 \delta^{(3)}=D_3C,\qquad q=(W^{(3)})^\top\delta^{(3)},\qquad
 \delta^{(2)}=D_2q .
\end{gathered}
\]
The autonomous feature-time field \(\mathcal F\) is
\[
\begin{split}
 X'&=(W^{(2)})^\top\delta^{(2)},\\
 (W^{(2)})'&=\delta^{(2)}\otimes h^{(1)},\\
 (W^{(3)})'&=\delta^{(3)}\otimes h^{(2)},\\
 C'&=h^{(3)}.                                             \tag{1}
\end{split}
\]
Here \(\chi'(X)=D_1^2\) coordinatewise. Fix a finite feature horizon \(S\)
and a bound \(M\) for the two initial hidden operator norms. For zero
initial readout, (1) directly gives, at feature time \(s\),
\[
\begin{gathered}
 \|C(s)\|_\infty\le as,\qquad
 \|W^{(3)}(s)\|_{\rm op}\le M+a^2s^2/2,\\
 \|q(s)\|_n\le as(M+a^2s^2/2),\\
 \|W^{(2)}(s)\|_{\rm op}
       \le M+a^2Ms^2/2+a^4s^4/8 .
\end{gathered}
\]
For example \(\|(W^{(3)})'\|_{\rm op}
\le\|\delta^{(3)}\|_n\|h^{(2)}\|_n\le a^2s\); the other bounds follow
successively. The same bounds hold for the fully pruned network.
Every constant below can be taken to depend only on these bounds. Neither
\(\|q\|_\infty\) nor a backward-query tail bound is assumed.

## 2. The coordinatewise logarithmic identity retains a nonlocal term

Fix a pruned middle set \(E\), \(P=P_E\), \(Q=I-P\). Hats denote the
fully pruned network. Its middle activation and backward vector vanish
on \(E\); the unused preactivation \(\widehat z^{(2)}\) and unused query
\(\widehat q=(\widehat W^{(3)})^\top\widehat\delta^{(3)}\) are still defined.
Write \(U=W^{(2)}\), \(V=\widehat W^{(2)}\), \(h=h^{(1)}\), and define
\[
\begin{gathered}
 e=Q(z^{(2)}-\widehat z^{(2)}),\quad A=Q(U-V),\quad
 \Delta h=h-\widehat h^{(1)},\\
 m=\|h\|_n^2,\quad K=UD_1^2U^\top,\quad A_2=mI+K,\\
 \widehat A_2=\|\widehat h^{(1)}\|_n^2I+
                         V\widehat D_1^2V^\top,\\
 v=Q(D_2-\widehat D_2)\widehat q,\qquad
 w=QD_2(q-\widehat q),\qquad r=P\delta^{(2)},\\
 g=Q(A_2-\widehat A_2)\widehat\delta^{(2)}.
\end{gathered}
\]
The exact active equations, including the row training, are
\[
\begin{split}
 e'&=m(v+w)+QK(v+w+r)+g,\\
 A'&=(v+w)\otimes h+\widehat\delta^{(2)}\otimes\Delta h.
                                                               \tag{2}
\end{split}
\]
Indeed \(\delta^{(2)}-\widehat\delta^{(2)}=r+w+v\), and
\((z^{(2)})'=A_2\delta^{(2)}\) holds for the actual network; the analogous
formula holds for the unused pruned preactivation.

For \(\varepsilon>0\), put
\[
 s_i=n\sum_jA_{ij}^2,\quad R_i=e_i^2+s_i,\quad
 \beta_i=\frac{\mathbf1_{i\notin E}}{\varepsilon^2+R_i},\qquad
 {\cal L}_\varepsilon=\frac1n\sum_{i\notin E}
                         \log(1+R_i/\varepsilon^2).
\]
Differentiating (2) gives exactly
\[
\begin{split}
 {\cal L}_\varepsilon'
  ={}&2\langle\beta(me+Ah),v+w\rangle_n\\
    &+2\langle\beta e,K(v+w+r)+g\rangle_n
      +2\langle\beta A\Delta h,\widehat\delta^{(2)}\rangle_n .
                                                               \tag{3}
\end{split}
\]
Multiplication by a vector such as \(\beta\) is coordinatewise. The
rank-one normalization in (1) is essential in this formula:
\(s_i'=2(v_i+w_i)(Ah)_i+
2\widehat\delta_i^{(2)}(A\Delta h)_i\).

The local middle-gate part really is controlled without tails.
Since \(|\phi''|\le2\), \(|v_i|\le2|e_i||\widehat q_i|\), while
\[
 |(Ah)_i|\le a\sqrt{s_i},\qquad
 |e_i(me_i+(Ah)_i)|\le(a^2+a/2)R_i .
\]
Consequently
\[
 \left|2\langle\beta(me+Ah),v\rangle_n\right|
 \le(4a^2+2a)\|\widehat q\|_{1,n},\qquad
 \|\widehat q\|_{1,n}=\frac1n\sum_i|\widehat q_i|.          \tag{4}
\]
This bound is independent of \(\varepsilon\).

The other middle-gate contribution is the exact weighted transpose pair
\[
 2\langle\beta e,Kv\rangle_n
   =2\langle D_1U^\top(\beta e),D_1U^\top v\rangle_n.       \tag{5}
\]
There is no negative copy of (5) in the row update in (3).
Adding the first-layer coordinate log of \(x=X-\widehat X\) contributes
\(2\langle U[x/(\varepsilon^2+x^2)],v\rangle_n\), not such a negative copy.
The top parameter velocities have no instantaneous \(v\)-term: they depend
on \(h^{(2)}\), \(h^{(3)}\), and \(\delta^{(3)}\), not on
\(\delta^{(2)}\). Thus their coordinate log derivatives do not cancel (5)
algebraically either.

There are also logarithmically weighted top-query and mobility terms
in (3). In particular the exact top identity is
\[
\begin{split}
 q-\widehat q={}&(W^{(3)}-\widehat W^{(3)})^\top\delta^{(3)}\\
 &+(\widehat W^{(3)})^\top
 \left[D_3(C-\widehat C)+(D_3-\widehat D_3)\widehat C\right].
                                                               \tag{6}
\end{split}
\]
Define
\[
 d_E=\|X-\widehat X\|_n+\|W^{(2)}-\widehat W^{(2)}\|_{\rm op}
        +\|W^{(3)}-\widehat W^{(3)}\|_{\rm op}+\|C-\widehat C\|_n.
\]
The established top Lipschitz estimate gives
\(\|q-\widehat q\|_n\le C_{S,M}(d_E+\sqrt{|E|/n})\), but an
unweighted \(L^2\) estimate inserted into (3) can cost
\(\|\beta e\|_n\le1/(2\varepsilon)\).

The existing Gaussian compression estimates control specified compressed
output norms, not the adaptive weighted pair (5). Pairing such an output
estimate with \(\beta e\) retains this inverse-\(\varepsilon\) factor.
The weights may be large on a set of order-one size where the error is
of order \(\varepsilon\); this set is not automatically a rare deleted
set. This identifies the precise missing estimate for this metric.
It is not a counterexample to canonical stability, nor a proof that
every logarithmic metric must fail.

## 3. A nuclear-norm bound for the actual Jacobian

Let \(J=D\mathcal F(\Theta)\). For a state variation
\(y=(x,A,B,c)\), define
\[
\begin{gathered}
 u_1=D_1^2x,\qquad
 \zeta_2=Ah^{(1)}+W^{(2)}u_1,\qquad u_2=D_2\zeta_2,\\
 \zeta_3=Bh^{(2)}+W^{(3)}u_2,\qquad
 v_3=D_3c+\operatorname{diag}(C\phi''(z^{(3)}))\zeta_3,\\
 v_q=B^\top\delta^{(3)}+(W^{(3)})^\top v_3,\qquad
 b=\phi''(z^{(2)})q.
\end{gathered}
\]
Differentiating every trained factor in (1) yields
\[
 J=L_0+R\,\operatorname{diag}(b)\,T,                       \tag{7}
\]
where
\[
\begin{split}
 Ty&=\zeta_2,\qquad
 Rv=((W^{(2)})^\top v,\ v\otimes h^{(1)},\ 0,\ 0),\\
 L_0y={}&\big(
 A^\top\delta^{(2)}+(W^{(2)})^\top D_2v_q,\ 
 (D_2v_q)\otimes h^{(1)}+\delta^{(2)}\otimes u_1,\\
 &\hspace{31mm}v_3\otimes h^{(2)}+\delta^{(3)}\otimes u_2,\
 D_3\zeta_3\big).
\end{split}
\]
All maps in \(L_0,R,T\) have operator norms bounded by \(C_{S,M}\):
the only potentially large diagonal multiplier was separated into
\(\operatorname{diag}(b)\); factors \(\delta^{(2)}\) that remain in \(L_0\)
occur as rank-one factors or in \(A^\top\delta^{(2)}\), and require only
their normalized \(L^2\) norms.

There is an additional rank fact. The image of \(L_0\) lies in
\[
\begin{split}
 {\mathbb R}^n\ \oplus\
 &\{u\otimes h^{(1)}+\delta^{(2)}\otimes w:u,w\in{\mathbb R}^n\}\\
 {}\oplus\
 &\{u\otimes h^{(2)}+\delta^{(3)}\otimes w:u,w\in{\mathbb R}^n\}
 \ \oplus\ {\mathbb R}^n .
                                                               \tag{8}
\end{split}
\]
This is an instantaneous subspace of dimension at most \(6n\);
it need not be fixed in time. Thus
\(\|L_0\|_*\le6n\|L_0\|_{\rm op}\). The nuclear ideal inequality and
the diagonal singular values now give
\[
\begin{split}
 \|J\|_*
 &\le6n\|L_0\|_{\rm op}
        +\|R\|_{\rm op}\|T\|_{\rm op}\sum_{i=1}^n|b_i|\\
 &\le C_{S,M}n\big(1+\|q\|_{1,n}\big)
 \le C_{S,M}n .                                           \tag{9}
\end{split}
\]
All these are Hilbert-space nuclear norms in the normalization specified
in Section 1. In particular no extra \(n\) is hidden in the rank-one
blocks, or in the middle diagonal operator.

For a fixed smooth middle clipping, replace
\(\delta^{(2)}\) by \(D_2\tau(q)\), \(b\) by
\(\phi''(z^{(2)})\tau(q)\), and \(D_2v_q\) by
\(D_2\operatorname{diag}(\tau'(q))v_q\).
Equations (7)--(9) and the rank bound remain valid with the same type
of constants. We do not need differentiability of an arbitrary
Lipschitz clipping for the uncut theorem.

## 4. Both stretching and contraction have bounded logarithmic distortion

The following finite-dimensional implication applies to the actual
Jacobian path and, more generally, any continuous state-space operator
\(J(s)\) satisfying \(\|J(s)\|_*\le Cn\).
Let
\[
 U'(s)=J(s)U(s),\qquad U(0)=I_N.
\]
The matrix \(U\) is invertible and \(\det U>0\). Define
\[
\begin{split}
 \Xi(s)
 &=\frac1n\left[
       \log\det(I_N+U(s)^*U(s))-N\log2-\log\det U(s)\right]\\
 &=\frac1n\sum_{j=1}^N
                      \log\cosh\big(\log\sigma_j(U(s))\big).
                                                               \tag{10}
\end{split}
\]
The second equality follows from
\(\log(1+\sigma^2)-\log2-\log\sigma
=\log\cosh(\log\sigma)\). In particular \(\Xi\ge0\) and \(\Xi(0)=0\).

Put
\[
 P_U=U(I_N+U^*U)^{-1}U^*.
\]
It is self-adjoint with spectrum strictly between zero and one.
The derivative of a log determinant and cyclicity of trace give
\[
 \Xi'=\frac1n\operatorname{Tr}\big[J(2P_U-I_N)\big],
 \qquad |\Xi'|\le\frac{\|J\|_*}{n}\le C .                  \tag{11}
\]
Indeed the derivative of the first determinant in (10) is
\(\operatorname{Tr}[(J+J^*)P_U]=2\operatorname{Tr}(JP_U)\);
the derivative of \(\log\det U\) is \(\operatorname{Tr}J\).
Since \(\|2P_U-I_N\|_{\rm op}\le1\), the last inequality in (11)
follows without a sign or normality assumption on \(J\).

Consequently, for the actual network,
\[
 \frac1n\sum_{j=1}^N
       \log\cosh\big(\log\sigma_j(U(t))\big)\le C_{S,M}t.
                                                               \tag{12}
\]
For every \(R>0\), both expanding and contracting singular directions
are counted in
\[
 \#\{j:|\log\sigma_j(U(t))|\ge R\}
       \le\frac{C_{S,M}nt}{\log\cosh R}.                  \tag{13}
\]
The same statements hold for the propagator \(U(t,s)\), with \(t\)
replaced by \(t-s\). Equations (12)--(13) are pathwise consequences
of the primal bounds; no Gaussian independence is used in their proof.

## 5. Exact link to the actual Gaussian column-probe covariance

The determinant calculation also applies to a rectangular homogeneous
response \(Y'=JY\), where \(Y:\mathbb R^m\longrightarrow\mathcal H_n\).
For \(\varepsilon>0\), let
\[
 P_\varepsilon=Y(\varepsilon^2I_m+Y^*Y)^{-1}Y^*.
\]
Then \(0\le P_\varepsilon\le I_N\), and exactly
\[
 \frac d{dt}\frac1n\log\det(I_m+Y^*Y/\varepsilon^2)
       =\frac2n\operatorname{Tr}(JP_\varepsilon).
                                                               \tag{14}
\]
Thus the absolute value of this derivative is at most \(2C_{S,M}\).

For the actual top-column response from
ACTUAL_BULK_GAUSSIAN_TANGENT_ENERGY.md, fix a middle index \(i\) and
define the seed map
\[
 I_i u=(0,0,(u/\sqrt n)e_i^\top,0),\qquad
                 I_i^*I_i=I_n/n .
\]
Including the original seed in the top-matrix variation produces the
homogeneous full-flow tangent
\[
 Y_i(t)=U(t)I_i .
\]
If \(\xi\) is an independent standard Gaussian vector in \(\mathbb R^n\),
then \(Y_i(t)\xi\) is exactly this seeded tangent, and conditional on
the entire actual trajectory its covariance is \(Y_iY_i^*\).
Equation (14) proves the pathwise covariance-determinant bound
\[
 \frac1n\log\det(I_n+Y_i(t)^*Y_i(t)/\varepsilon^2)
 \le \log(1+1/(n\varepsilon^2))+2C_{S,M}t.                \tag{15}
\]
By the determinant identity for rectangular products, the determinant
equals \(\det(I_N+Y_iY_i^*/\varepsilon^2)\). Thus (15) can also be
read as a bound on twice the conditional Gaussian entropy excess,
divided by \(n\), after adding independent isotropic noise of covariance
\(\varepsilon^2I_N\). This is an exact determinant interpretation,
not a trace-covariance estimate.

For clarity, the zero-initial trained-increment response has map
\(Z_i=Y_i-I_i\), not \(Y_i\). At \(\varepsilon^2=1/n\),
\[
 I_n+nZ_i^*Z_i\le3(I_n+nY_i^*Y_i).
\]
Therefore it too obeys
\[
 \frac1n\log\det(I_n+nZ_i^*Z_i)
              \le\log6+2C_{S,M}t.                      \tag{16}
\]
Here the positive-matrix inequality follows from
\((Y_i-I_i)^*(Y_i-I_i)\le2Y_i^*Y_i+2I_n/n\);
monotonicity of the log determinant then gives (16).
Neither (15) nor (16) bounds
\(n\mathbb E_\xi\|Z_i\xi\|_{\mathcal H_n}^2
=n\operatorname{Tr}(Z_i^*Z_i)\).
One or a few singular directions can carry a large trace while
contributing only their logarithms to these estimates.

## 6. The actual full/pruned mean-value equation and what is still missing

There is an exact finite-pair application, not just a tangent statement.
Let \(\mathcal F_E\) be the fully pruned field on the same parameter
space. For the actual and reference parameter states, put
\[
 \Delta=\Theta-\widehat\Theta,\qquad
 \overline J_E(t)=\int_0^1
 D\mathcal F(\widehat\Theta(t)+\lambda\Delta(t))\,d\lambda .
\]
The mean-value identity gives
\[
 \Delta'=\overline J_E\Delta+f_E,\qquad
 f_E=\mathcal F(\widehat\Theta)-\mathcal F_E(\widehat\Theta),
 \qquad \Delta(0)=0.                                    \tag{17}
\]
Every segment state in this integral has bounded hidden operator norms
and bounded readout \(\ell^\infty\) norm: these are convex bounds on
the parameter states. Its recomputed activations are bounded by \(a\),
and its recomputed backward vectors have bounded normalized \(L^2\)
norms. The proof of (9) applies to every segment state, even though it
need not lie on a network trajectory. Convexity of the nuclear norm
therefore gives
\[
 \|\overline J_E(t)\|_*\le C_{S,M}n.                     \tag{18}
\]
We do not assert that the averaged bounded part has rank \(6n\);
its instantaneous ranges may change with \(\lambda\).
Equations (10)--(13) consequently apply to the propagator of (17).

The source in (17) is also quantitatively controlled without assuming
that the two trajectories are already close. Evaluate the FULL field at
the pruned parameter state, denoting its recomputed quantities by tildes.
Only the formerly deleted middle activations are restored:
\[
 \widetilde h^{(2)}-\widehat h^{(2)}
       =P\phi(\widehat z^{(2)}),\qquad
 \|\widetilde h^{(2)}-\widehat h^{(2)}\|_n\le a\sqrt p,
 \quad p=|E|/n .
\]
The bounded top maps imply
\[
 \|\widetilde z^{(3)}-\widehat z^{(3)}\|_n+
 \|\widetilde\delta^{(3)}-\widehat\delta^{(3)}\|_n+
 \|\widetilde q-\widehat q\|_n\le C_{S,M}\sqrt p .
\]
For the lower backward vector,
\[
 \widetilde\delta^{(2)}-\widehat\delta^{(2)}
   =P\widehat D_2\widehat q+
                         \widehat D_2(\widetilde q-\widehat q).
                                                               \tag{19}
\]
On the previously established simultaneous pruned-query event,
\[
 \|P\widehat q(t)\|_n
       \le C_{S,M}\big[\sqrt{h(p)}+\varepsilon_n\big],
 \qquad h(p)=p\log(e/p).                                 \tag{20}
\]
This event and its width error are precisely the allocated
pruned-query event in SHARP_RARE_ACCUMULATED_FORCING.md, equation (4).
It uses the fully pruned trajectory's independence of the deleted
initial top columns. No such independence is asserted for
\(\overline J_E\).

The \(X\) source is
\((\widehat W^{(2)})^\top
(\widetilde\delta^{(2)}-\widehat\delta^{(2)})\);
the \(W^{(2)}\) source is this backward-vector difference tensored
with \(\widehat h^{(1)}\). The \(W^{(3)}\) source is
\[
 (\widetilde\delta^{(3)}-\widehat\delta^{(3)})
             \otimes\widetilde h^{(2)}
       +\widehat\delta^{(3)}
             \otimes(\widetilde h^{(2)}-\widehat h^{(2)}),
\]
and the readout source is
\(\widetilde h^{(3)}-\widehat h^{(3)}\).
Using the rank-one norm identity from Section 1 proves
\[
 \|f_E(t)\|_{\mathcal H_n}
       \le C_{S,M}\big[\sqrt{h(p)}+\varepsilon_n\big].     \tag{21}
\]
Thus all four trained blocks occur in this finite-pair reduction.
For a fixed smooth common clipping, (19) is replaced by
\[
 P\widehat D_2\tau(\widehat q)
    +\widehat D_2[\tau(\widetilde q)-\tau(\widehat q)],
\]
so the same source bound holds on its corresponding prescribed-clipping
pruned event.

The remaining step is specific and not supplied by (18):
\[
 \Delta(t)=\int_0^t U_E(t,s)f_E(s)\,ds.                  \tag{22}
\]
The logarithmic distortion bound counts expanding singular directions,
but does not control the size of (22) when the actual pruning source
has a component in one of those directions. The Gaussian independence
used in (20) does not make \(f_E(s)\) independent of \(U_E(t,s)\);
the latter is computed from the coupled actual/reference histories.
Likewise (15)--(16) do not control the signed response covariance
or its trace moment in the existing actual probe-energy identity.

For comparison, a genuinely inhomogeneous response \(Y'=JY+G\) has the
additional exact determinant derivative
\[
 \frac2n\operatorname{Tr}
   [(\varepsilon^2I+Y^*Y)^{-1}Y^*G] .
                                                               \tag{23}
\]
Its general nuclear-norm bound is
\(\|G\|_*/(n\varepsilon)\), because
\(\|(\varepsilon^2I+Y^*Y)^{-1}Y^*\|_{\rm op}
\le1/(2\varepsilon)\). This identifies the source-direction issue
directly in a regularized determinant calculation as well.

The new established conclusion is therefore the actual normalized
nuclear-Jacobian estimate (9), its two-sided singular distortion
consequence (12), and the exact actual-probe covariance determinant
bound (15). The coordinate metric retains (5), and the full/pruned
mean-value equation retains the source propagation in (22).
Neither remaining term has been closed here.
