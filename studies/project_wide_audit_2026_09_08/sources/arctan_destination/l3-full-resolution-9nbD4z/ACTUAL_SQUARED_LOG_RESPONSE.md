# Squared logarithmic distortion of actual canonical responses

This note proves a deterministic finite-width estimate for the actual
uncut arctan network: a second logarithmic moment in raw canonical
coordinates, including every transported initial subspace and the actual
Gaussian column probe. LOGARITHMIC_NETWORK_COMPARISON.md uses a transformed
first-layer coordinate; no identification of the two response spectra is
asserted here. The new estimate does not supply a width-uniform normalized
response-trace bound, source-alignment control, or global population
continuation. No numerical experiment is used.

## Canonical coordinates and the bound

Let the width be \(n\ge1\), and let \(a=\pi/2\). All vector norms are
ordinary Euclidean norms, all matrix Frobenius norms are ordinary
Frobenius norms, and all transposes are finite transposes. The network is

\[
h^{(\ell)}=\phi(z^{(\ell)}),\quad \phi=\arctan,\quad
z^{(2)}=W^{(2)}h^{(1)},\quad z^{(3)}=W^{(3)}h^{(2)},\quad
f_n=(W^{(4)})^T h^{(3)}/n.
\]

Here \(W^{(4)}\) is the rescaled readout. The backward fields, without
the residual, are

\[
\delta^{(3)}=W^{(4)}\odot\phi'(z^{(3)}),\quad
q^{(2)}=(W^{(3)})^T\delta^{(3)},\quad
\delta^{(2)}=\phi'(z^{(2)})\odot q^{(2)},\quad
q^{(1)}=(W^{(2)})^T\delta^{(2)},\quad
\delta^{(1)}=\phi'(z^{(1)})\odot q^{(1)}.
\]

Use the Euclidean coordinates

\[
x=(z^{(1)},\sqrt n W^{(2)},\sqrt n W^{(3)})\in\mathbb R^d,
\qquad c=W^{(4)}\in\mathbb R^n,\qquad d=n+2n^2.
\]

These use the raw first preactivation, not \(F(z^{(1)})\). With

\[
\mathcal P(x,c)=c^T h^{(3)}(x),\qquad b=\nabla\mathcal P,
\]

the feature-time equations are exactly \((x,c)'=b(x,c)\). In particular,
the two hidden matrix blocks of \(b\) are

\[
\delta^{(2)}(h^{(1)})^T/\sqrt n,
\qquad \delta^{(3)}(h^{(2)})^T/\sqrt n.
\]

Let \(B=Db=D^2\mathcal P\). At any state obeying

\[
\|W^{(2)}\|_{\rm op},\|W^{(3)}\|_{\rm op}\le M,
\qquad \|c\|_2/\sqrt n\le R,
\tag{1}
\]

put \(K_2=a+M\), \(K_3=a+MK_2\), and

\[
C_B(M,R)=2R(M^2+MK_2^2+K_3^2+M+K_2)+\sqrt2 K_3.
\]

Then the full state-space Frobenius norm satisfies

\[
\|B\|_{\rm F}\le C_B(M,R)\sqrt n.
\tag{2}
\]

This needs neither a maximum-coordinate readout bound nor a spatial
tail bound on either backward query.

Let \(U(s,s_0)\) be the full derivative propagator along an actual
finite-width feature flow, and let \(E:\mathbb R^m\to\mathbb R^{d+n}\)
be any isometric linear embedding, \(E^TE=I_m\). If (1) holds throughout
\([s_0,s]\), then, for the \(m\) positive singular values of \(U(s,s_0)E\),

\[
\sum_{j=1}^m\bigl(\log\sigma_j(U(s,s_0)E)\bigr)^2
\le C_B(M,R)^2 n(s-s_0)^2.
\tag{3}
\]

The estimate holds for every embedding on the same pathwise event;
independence between the embedding and the trajectory is unnecessary.
In particular,

\[
\#\{j:|\log\sigma_j(U(s,s_0)E)|\ge r\}
\le C_B(M,R)^2 n(s-s_0)^2/r^2\qquad(r>0).
\tag{4}
\]

The analogous physical-time conclusions are given below.

## Complete Frobenius calculation

For a hidden variation \(u=(u_1,E_2,E_3)\), where \(E_2,E_3\) vary
the coordinates \(\sqrt n W^{(2)},\sqrt n W^{(3)}\), define

\[
T_1u=u_1,
\]
\[
T_2u=E_2h^{(1)}/\sqrt n+
 W^{(2)}[\phi'(z^{(1)})\odot u_1],
\]
\[
T_3u=E_3h^{(2)}/\sqrt n+
 W^{(3)}[\phi'(z^{(2)})\odot T_2u].
\]

Thus \(\|T_1\|_{\rm op}=1\), \(\|T_2\|_{\rm op}\le K_2\), and
\(\|T_3\|_{\rm op}\le K_3\). The derivative of the output feature
vector is \(J=\operatorname{diag}(\phi'(z^{(3)}))T_3\), so
\(\|J\|_{\rm op}\le K_3\) and \(\operatorname{rank}J\le n\).

Also define

\[
S_2u=E_2^T\delta^{(2)}/\sqrt n,
\qquad S_3u=E_3^T\delta^{(3)}/\sqrt n.
\]

The norm assumptions give

\[
\|q^{(2)}\|_2\le MR\sqrt n,\quad
\|q^{(1)}\|_2\le M^2R\sqrt n,\quad
\|S_2\|_{\rm op}\le MR,\quad \|S_3\|_{\rm op}\le R.
\tag{5}
\]

Twice differentiating \(c^Th^{(3)}\) along the straight hidden
parameter line gives, with \(A=D_x^2[c^Th^{(3)}]\),

\[
\begin{split}
u^TAu={}&(T_1u)^T\operatorname{diag}(\phi''(z^{(1)})\odot q^{(1)})T_1u\\
&+(T_2u)^T\operatorname{diag}(\phi''(z^{(2)})\odot q^{(2)})T_2u\\
&+(T_3u)^T\operatorname{diag}(\phi''(z^{(3)})\odot c)T_3u\\
&+2(S_2u)^T[\phi'(z^{(1)})\odot T_1u]\\
&+2(S_3u)^T[\phi'(z^{(2)})\odot T_2u].
\end{split}
\tag{6}
\]

For completeness, the second preactivation variations are

\[
d^2z^{(2)}[u,u]=2E_2[\phi'(z^{(1)})\odot u_1]/\sqrt n
 +W^{(2)}[\phi''(z^{(1)})\odot u_1^2],
\]
\[
d^2z^{(3)}[u,u]=2E_3[\phi'(z^{(2)})\odot T_2u]/\sqrt n
 +W^{(3)}[\phi''(z^{(2)})\odot(T_2u)^2
              +\phi'(z^{(2)})\odot d^2z^{(2)}[u,u]].
\]

The second derivative of the last activation and contraction with \(c\)
give (6), including both trained-matrix cross terms.

For any \(T\) and diagonal \(D\),
\(\|T^TDT\|_{\rm F}\le\|T\|_{\rm op}^2\|D\|_{\rm F}\).
Since \(|\phi''|\le2\), (5) bounds the three diagonal terms in (6)
respectively by

\[
2M^2R\sqrt n,\qquad 2K_2^2MR\sqrt n,
\qquad 2K_3^2R\sqrt n.
\]

Each map \(S_2^T\operatorname{diag}(\phi'(z^{(1)}))T_1\) has rank at
most \(n\), hence Frobenius norm at most \(MR\sqrt n\); adding its
transpose costs at most twice this. The corresponding \(S_3,T_2\)
pair costs at most \(2RK_2\sqrt n\). Finally,

\[
B=\begin{pmatrix}A&J^T\\J&0\end{pmatrix},\qquad
\left\|\begin{pmatrix}0&J^T\\J&0\end{pmatrix}\right\|_{\rm F}
=\sqrt2\|J\|_{\rm F}\le\sqrt{2n}K_3.
\]

The triangle inequality proves exactly (2). This calculation uses
the Euclidean coordinate metric specified above, not the unrescaled
matrix entries with a different gradient metric.

## Logarithms of all singular values, including repeated values

We prove the matrix implication without a singular-vector differentiability
assumption. Let \(D(t)\) be any continuous real square matrix, let
\(V'=DV\), and assume \(V(s_0)^TV(s_0)=I_m\). The fundamental square
solution is invertible, so the rectangular \(V(t)\) retains full column
rank. Put

\[
G=V^TV>0,\qquad Q=VG^{-1/2},\qquad Q^TQ=I_m,
\qquad \mathcal E=\tfrac14\operatorname{Tr}[(\log G)^2].
\]

Then \(\mathcal E=\sum_j(\log\sigma_j(V))^2\). For a differentiable
positive definite matrix \(G\) and a smooth scalar function \(g\),
\(d\operatorname{Tr}g(G)/dt=\operatorname{Tr}[g'(G)G']\): in an
orthonormal eigenbasis the trace of the differential keeps only its
diagonal entries \(g'(\lambda_j)G'_{jj}\). This remains true in a
repeated-eigenvalue block, where \(g'(\lambda_j)\) is constant.
Apply this to \(g(\lambda)=(\log\lambda)^2/4\). With
\(D_{\rm sym}=(D+D^T)/2\), one obtains

\[
\begin{split}
\mathcal E'
&=\tfrac12\operatorname{Tr}[(\log G)G^{-1}G']\\
&=\operatorname{Tr}[(\log G)Q^TD_{\rm sym}Q].
\end{split}
\]

Cauchy--Schwarz for Frobenius products, together with
\(\|Q^TD_{\rm sym}Q\|_{\rm F}\le\|D_{\rm sym}\|_{\rm F}\), gives

\[
|\mathcal E'|\le2\sqrt{\mathcal E}\,\|D_{\rm sym}\|_{\rm F}.
\]

To avoid division at zero, differentiate \(\sqrt{\mathcal E+\epsilon}\)
for \(\epsilon>0\), integrate from \(s_0\), and let \(\epsilon\downarrow0\).
Because \(\mathcal E(s_0)=0\),

\[
\left(\sum_j(\log\sigma_j(V(s)))^2\right)^{1/2}
\le\int_{s_0}^s\|D_{\rm sym}(u)\|_{\rm F}\,du.
\tag{7}
\]

No normality, commutation in time, or selected smooth eigenbasis is
required. Taking \(D=B\) and \(V=U(\cdot,s_0)E\) proves (3)--(4).

## Physical time and canonical Gaussian initialization

The exact physical field is \(2(1-f_n)b\). Since
\(\nabla f_n=b/n\), its Jacobian is

\[
B_{\rm phys}=2(1-f_n)B-(2/n)bb^T.
\tag{8}
\]

All clock derivatives are retained in the second term. The elementary
bound

\[
\|b\|_2^2/n\le M^4R^2+a^2M^2R^2+a^2R^2+a^2=:K_b^2
\]

follows by evaluating its four blocks. Also \(|f_n|\le aR\). Thus,
using \(n\ge1\),

\[
\|B_{\rm phys}\|_{\rm F}
\le[2(1+aR)C_B(M,R)+2K_b^2]\sqrt n=:C_{\rm phys}(M,R)\sqrt n.
\tag{9}
\]

Consequently (3)--(4) apply at fixed physical times with \(C_B\)
replaced by \(C_{\rm phys}\) and \(s-s_0\) by \(t-t_0\). These are
derivatives at fixed physical time, not derivatives obtained by
silently holding a state-dependent feature clock fixed.

The canonical independent initialization is
\(z^{(1)}_{0,i}\sim N(0,1)\),
\(W^{(2)}_{0,ij},W^{(3)}_{0,ij}\sim N(0,1/n)\),
and \(W^{(4)}_{0,i}\sim N(0,n^{-2})\).
The established finite-width primal theorem supplies bounds (1) on
every fixed physical horizon with probability tending to one and
constants independent of width. This is the sole dependency for this
probabilistic corollary: substitute those constants into (3)--(4)
and (9). The deterministic estimates above do not assume a Gaussian
draw and also allow exactly zero readout. They do not transfer a
zero-readout population limit to the tiny-readout population limit.

## Actual top-column probe and the unresolved amplitude

Fix a middle neuron \(i\). In the raw coordinates above the embedding

\[
E_i u=(0,0,ue_i^T,0)
\]

is isometric. It corresponds to perturbing the original top matrix
column by \(u/\sqrt n\). If \(g\sim N(0,I_n)\) is an independent
derivative probe and \(Y_i=U(s,0)E_i\), then \(Y_i g\) is the full
canonical column response, conditional on the trained trajectory.
Its conditional covariance is \(Y_iY_i^T\); its nonzero eigenvalues
are \(\sigma_j(Y_i)^2\). Hence (3) controls the squared logarithms
of that actual covariance spectrum. It is not a hypothesis on a
surrogate response.

For the trained-increment response \(Z_i=Y_i-E_i\),

\[
Z_i^TZ_i\preceq2Y_i^TY_i+2I_n.
\]

Writing the eigenvalues in decreasing order and using the variational
characterization of ordered eigenvalues gives

\[
\begin{split}
\sum_{j=1}^n[\log(1+\sigma_j(Z_i)^2)]^2
&\le\sum_{j=1}^n[\log(3+2\sigma_j(Y_i)^2)]^2\\
&\le2n(\log5)^2+8\sum_{j=1}^n(\log\sigma_j(Y_i))^2\\
&\le n[2(\log5)^2+8C_B(M,R)^2s^2].
\tag{10}
\end{split}
\]

The scalar inequality used is \(3+2u^2\le5\max(1,u^2)\).
The same conclusion holds with the physical propagator and its constant.

The estimates do not supply a width-uniform bound on the normalized
trace \(\operatorname{Tr}(Z_i^TZ_i)/n\), nor on the response energy required
by the global stability proof. For example,
the abstract matrix path generated by
\(D_n=\operatorname{diag}(\sqrt n,0,\ldots,0)\) has
\(\|D_n\|_{\rm F}=\sqrt n\) and satisfies (7) with equality, while
one singular value is \(e^{s\sqrt n}\). Its mean squared amplification
over \(n\) directions diverges at every fixed positive \(s\). This
abstract example is not claimed to be a canonical network trajectory.
It shows precisely why (2)--(10) alone do not close the amplitude bound.

The count \(O(n/r^2)\) in the stated raw metric is a new actual-response
constraint. No transfer to the nonlinear first-layer coordinate is claimed. It leaves the
canonical alignment and amplitude problem open. A complete global
proof still requires a further estimate controlling those quantities.

Explicit mathematical dependencies: the full Hessian identity is
rederived here and also appears in ACTUAL_HIDDEN_GRAPH_VOLUME.md;
the high-probability finite-horizon primal bounds are supplied by
READOUT_COERCIVITY.md. No external theorem is used for the new
Frobenius-to-logarithmic response implication.
