

## Further finite response and physical controls

The following fragments S, I, C and E have separate model and clock
contracts, and locally prefixed equation numbers. Their associated integrated
query and adaptive Gaussian results Q2–Q7 and G are in
[Gaussian calculus](gaussian_calculus.md), under “Integrated queries and
adaptive Gaussian comparison”. Section 13 above supplies the exact query
memory identities used by that comparison.

## S. Squared-logarithmic response

The datum is one normalized scalar input, label one, three arctangent hidden
layers, unit block mobilities, and loss \(\mathcal L=(f_n-1)^2\).
The raw parameter metric is
\[
 n^{-1}\|dz^{(1)}\|_2^2+\|dW^{(2)}\|_F^2+
 \|dW^{(3)}\|_F^2+n^{-1}\|dW^{(4)}\|_2^2.
\]
The Euclidean coordinates used below multiply this metric by the common factor
\(n\); the readout is the stored readout, without Gaussian whitening.
The result controls squared logarithms of singular values of the actual full
response and of every transported initial subspace.

### Canonical coordinates and the bound

Let the width be \(n\ge1\), and let \(a=\pi/2\). All vector norms are
ordinary Euclidean norms, all matrix Frobenius norms are ordinary
Frobenius norms, and all transposes are finite transposes. The network is

\[
h^{(\ell)}=\phi(z^{(\ell)}),\quad \phi=\arctan,\quad
z^{(2)}=W^{(2)}h^{(1)},\quad z^{(3)}=W^{(3)}h^{(2)},\quad
f_n=(W^{(4)})^T h^{(3)}/n.
\]

Here \(W^{(4)}\) is the stored readout. The backward fields, without
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
x=(z^{(1)},\sqrt n W^{(2)},\sqrt n W^{(3)})\in\mathbb R^{N_h},
\qquad c=W^{(4)}\in\mathbb R^n,\qquad N_h=n+2n^2.
\]

These use the raw first preactivation, without replacing it by the nonlinear primitive \(F(z)=z+z^3/3\). With

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
\tag{S.1}
\]

put \(K_2=a+M\), \(K_3=a+MK_2\), and

\[
C_B(M,R)=2R(M^2+MK_2^2+K_3^2+M+K_2)+\sqrt2 K_3.
\]

Then the full state-space Frobenius norm satisfies

\[
\|B\|_{\rm F}\le C_B(M,R)\sqrt n.
\tag{S.2}
\]

This needs neither a maximum-coordinate readout bound nor a spatial
tail bound on either backward query.

Let \(U(s,s_0)\) be the full derivative propagator along an actual
finite-width feature flow, and let \(E:\mathbb R^k\to\mathbb R^{N_h+n}\)
be any isometric linear embedding, \(E^TE=I_k\). If (S.1) holds throughout
\([s_0,s]\), then, for the \(k\) positive singular values of \(U(s,s_0)E\),

\[
\sum_{j=1}^k\bigl(\log\sigma_j(U(s,s_0)E)\bigr)^2
\le C_B(M,R)^2 n(s-s_0)^2.
\tag{S.3}
\]

The estimate holds for every embedding on the same pathwise event;
independence between the embedding and the trajectory is unnecessary.
In particular,

\[
\#\{j:|\log\sigma_j(U(s,s_0)E)|\ge r\}
\le C_B(M,R)^2 n(s-s_0)^2/r^2\qquad(r>0).
\tag{S.4}
\]

The analogous physical-time conclusions are given below.

### Complete Frobenius calculation

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
\tag{S.5}
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
\tag{S.6}
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
give (S.6), including both trained-matrix cross terms.

For any \(T\) and diagonal \(D\),
\(\|T^TDT\|_{\rm F}\le\|T\|_{\rm op}^2\|D\|_{\rm F}\).
Since \(|\phi''|\le2\), (S.5) bounds the three diagonal terms in (S.6)
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

The triangle inequality proves exactly (S.2). This calculation uses
the Euclidean coordinate metric specified above, not the unrescaled
matrix entries with a different gradient metric.

### Logarithms of all singular values, including repeated values

We prove the matrix implication without a singular-vector differentiability
assumption. Let \(D(t)\) be any continuous real square matrix, let
\(V'=DV\), and assume \(V(s_0)^TV(s_0)=I_m\). The fundamental square
solution is invertible, so the rectangular \(V(t)\) retains full column
rank. Put

\[
G=V^TV>0,\qquad Q=VG^{-1/2},\qquad Q^TQ=I_m,
\qquad \mathcal E=\tfrac14\operatorname{Tr}[(\log G)^2].
\]

Then \(\mathcal E=\sum_j(\log\sigma_j(V))^2\). To differentiate without
any assumption of simple singular values, use the convergent resolvent formula
\[
 \log G=\int_0^\infty[(1+t)^{-1}I-(G+tI)^{-1}],dt,
 \quad
 D\log G[G']=\int_0^\infty(G+tI)^{-1}G'(G+tI)^{-1}\,dt.
\]
On a compact time interval the eigenvalues of \(G\) stay in a compact subset
of \((0,\infty)\), so differentiating under this integral is justified by a
constant bound near zero and an integrable \(O(t^{-2})\) bound at infinity.
The product rule and cyclicity of trace give
\(\mathcal E'=\tfrac12\operatorname{Tr}[(\log G)D\log G[G']]\).
Since \(\log G\) commutes with its resolvents and
\(\int_0^\infty(G+tI)^{-2}dt=G^{-1}\), this proves the first equality below,
including repeated eigenvalues. With \(D_{\rm sym}=(D+D^T)/2\),

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
\tag{S.7}
\]

No normality, commutation in time, or selected smooth eigenbasis is
required. Taking \(D=B\) and \(V=U(\cdot,s_0)E\) proves (S.3)--(S.4).

### Physical time and canonical Gaussian initialization

The exact physical field is \(2(1-f_n)b\). Since
\(\nabla f_n=b/n\), its Jacobian is

\[
B_{\rm phys}=2(1-f_n)B-(2/n)bb^T.
\tag{S.8}
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
\tag{S.9}
\]

Consequently (S.3)--(S.4) apply at fixed physical times with \(C_B\)
replaced by \(C_{\rm phys}\) and \(s-s_0\) by \(t-t_0\). These are
derivatives at fixed physical time, not derivatives obtained by
silently holding a state-dependent feature clock fixed.

The canonical independent initialization is
\(z^{(1)}_{0,i}\sim N(0,1)\),
\(W^{(2)}_{0,ij},W^{(3)}_{0,ij}\sim N(0,1/n)\),
and \(W^{(4)}_{0,i}\sim N(0,n^{-2})\).
Here is a direct proof of the needed probability and primal bounds. Put
\(\beta=1/(2a)\). A maximal \(1/4\)-separated sphere net has at most
\(9^n\) points (disjoint radius-\(1/8\) balls fit inside the ball of
radius \(9/8\)); two such nets give
\(\|W\|_{op}\le2\max_{u,v}|u^TWv|\). Each bilinear form is
\(N(0,1/n)\), so the probability either hidden norm exceeds 10 is at
most \(4\exp((2\log9-100/8)n)\). Markov's inequality gives
\(\mathbb P(\|c_0\|_2/\sqrt n>\beta)\le4a^2/n^2\).
On the complementary event define, for \(u\ge0\),
\[
 P_3(u)=10+a\beta u+a^2u^2/2,\qquad
 P_2(u)=10+a\int_0^uP_3(v)(\beta+av)\,dv.
\]
The four feature equations imply successively
\[
 \|c(u)\|_2/\sqrt n\le\beta+au,\quad
 \|W^{(3)}(u)\|_{op}\le P_3(u),\quad
 \|W^{(2)}(u)\|_{op}\le P_2(u),\quad
 \|(z^{(1)})'(u)\|_2/\sqrt n\le P_2(u)P_3(u)(\beta+au).
\]
The same rank-one estimates bound both learned Frobenius increments. These
finite polynomials prevent finite feature-time escape; the smooth ODE therefore
exists on every nonnegative finite feature interval. Moreover
\(f_n'=\|b\|_2^2/n\ge0\). Along the physical flow the residual obeys
\(\dot r=-2(\|b\|_2^2/n)r\). Since \(|f_n(0)|\le1/2\), the clock is
nonnegative and \(0\le s(t)\le3t\). Solving this scalar clock over the
complete feature solution proves physical existence on every fixed \([0,T]\)
and the asserted bounds with constants obtained at \(u=3T\). Their event
has probability at least
\(1-4e^{(2\log9-100/8)n}-4a^2/n^2\). Substitution into (S.3)--(S.4) and (S.9)
proves the Gaussian finite-horizon corollary. The deterministic estimates above do not assume a Gaussian
draw and also allow exactly zero readout. They do not transfer a
zero-readout population limit to the tiny-readout population limit.

### Actual top-column probe and the unresolved amplitude

Fix a middle neuron \(i\). In the raw coordinates above the embedding

\[
E_i u=(0,0,ue_i^T,0)
\]

is isometric. It corresponds to perturbing the original top matrix
column by \(u/\sqrt n\). If \(g\sim N(0,I_n)\) is an independent
derivative probe and \(Y_i=U(s,0)E_i\), then \(Y_i g\) is the full
canonical column response, conditional on the trained trajectory.
Its conditional covariance is \(Y_iY_i^T\); its nonzero eigenvalues
are \(\sigma_j(Y_i)^2\). Hence (S.3) gives explicitly \(\sum_j(\log\lambda_j)^2\le4C_B(M,R)^2ns^2\) for that actual covariance spectrum. It is not a hypothesis on a
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
\tag{S.10}
\end{split}
\]

The scalar inequality used is \(3+2u^2\le5\max(1,u^2)\).
The same conclusion holds with the physical propagator and its constant.

The estimates do not supply a width-uniform bound on the normalized
trace \(\operatorname{Tr}(Z_i^TZ_i)/n\), nor on the response energy required
by the global stability proof. For example,
the abstract matrix path generated by
\(D_n=\operatorname{diag}(\sqrt n,0,\ldots,0)\) has
\(\|D_n\|_{\rm F}=\sqrt n\) and satisfies (S.7) with equality, while
one singular value is \(e^{s\sqrt n}\). Its mean squared amplification
over \(n\) directions diverges at every fixed positive \(s\). This
abstract example is not claimed to be a canonical network trajectory.
It shows precisely why (S.2)--(S.10) alone do not close the amplitude bound.

The count \(O(n/r^2)\) in the stated raw metric is an actual-response
constraint. No transfer to the nonlinear first-layer coordinate is claimed. It leaves the
canonical alignment and amplitude problem open. A complete global
proof still requires a further estimate controlling those quantities.



## I. Initial Gaussian middle curvature

The following initialization lemma supplies the joint empirical law used in
fragment C. It is an initialization result for the same one-input arctangent
model, with all displayed hidden matrices independent. It does not require a
readout draw.
### Statement

For each integer \(n\geq1\), let
\[
z_{0,i}^{(1)}\overset{\mathrm{iid}}{\sim}N(0,1),\qquad
(W_0^{(2)})_{ij},(W_0^{(3)})_{ij}
\overset{\mathrm{iid}}{\sim}N(0,1/n),
\qquad 1\leq i,j\leq n,
\]
with all these variables independent. Define, coordinatewise,
\[
\phi(x)=\arctan x,\qquad
h_0^{(\ell)}=\phi(z_0^{(\ell)}),\qquad
z_0^{(2)}=W_0^{(2)}h_0^{(1)},\qquad
z_0^{(3)}=W_0^{(3)}h_0^{(2)}.
\]
All vectors here belong to \(\mathbb R^n\); \(\|\cdot\|\) is the ordinary Euclidean norm, and \(T\) denotes transpose. Set
\[
g(x)=\phi'(x)\phi(x)=\frac{\arctan x}{1+x^2},
\qquad
u_n^{(2)}=(W_0^{(3)})^T
\bigl[\phi'(z_0^{(3)})\odot\phi(z_0^{(3)})\bigr]
=(W_0^{(3)})^T g(z_0^{(3)}).
\]
Thus \(u_n^{(2)}\) is determined by the displayed canonical initialization.

Let \(G_1,G_2,G_3,G\) be independent \(N(0,1)\) population variables, and define
\[
\begin{aligned}
m_1&=\mathbb E[\phi(G_1)^2],
&Z^{(2)}&=\sqrt{m_1}\,G_2,\\
m_2&=\mathbb E[\phi(Z^{(2)})^2],
&Z^{(3)}&=\sqrt{m_2}\,G_3,\\
\beta&=\frac{\mathbb E[Z^{(3)}g(Z^{(3)})]}{m_2},
&\sigma^2&=\mathbb E[g(Z^{(3)})^2],\qquad
U^{(2)}=\beta\phi(Z^{(2)})+\sigma G,
\end{aligned}
\]
where \(\sigma\) is the positive square root. Then
\(m_1,m_2,\sigma^2>0\) and \(0<\beta\leq1\).

For every continuous \(F:\mathbb R^2\to\mathbb R\) satisfying
\[
|F(z,v)|\leq C_F(1+z^2+v^2)
\quad\text{for some finite }C_F,
\]
the joint empirical-average law is
\[
\frac1n\sum_{i=1}^n F(z_{0,i}^{(2)},u_{n,i}^{(2)})
\longrightarrow \mathbb E[F(Z^{(2)},U^{(2)})]
\quad\text{in probability and in }L^1.
\tag{I.1}
\]
In particular, with \([a]_+=\max(a,0)\),
\[
c_n=\frac1n\sum_{i=1}^n
\bigl[u_{n,i}^{(2)}\phi''(z_{0,i}^{(2)})\bigr]_+
\longrightarrow
c_*=\mathbb E\!\left[\bigl[U^{(2)}\phi''(Z^{(2)})\bigr]_+\right]>0
\quad\text{in probability and in }L^1.
\tag{I.2}
\]
Consequently \(\mathbb E c_n\to c_*\).

The proof first derives the exact conditional law after reuse of
\(W_0^{(3)}\), then removes its projection term in root mean square.
A coupling with independent population pairs gives empirical convergence.
Uniform fourth moments justify the unbounded tests and convergence of
expectations; an explicit conditional Gaussian event gives strict positivity.

### Proof

Write \(H=\pi/2\). The elementary bounds used below are
\[
|\phi(x)|\leq H,\quad |\phi(x)|\leq|x|,\quad
0<\phi'(x)=\frac1{1+x^2}\leq1,\quad
\phi''(x)=-\frac{2x}{(1+x^2)^2},\quad |\phi''(x)|\leq2,
\tag{I.3}
\]
and
\[
|g(x)|\leq H,\qquad |g(x)|\leq|x|,\qquad
0\leq xg(x)\leq x^2,\qquad |xg(x)|\leq H/2.
\tag{I.4}
\]
For the last bound use \(|x|/(1+x^2)\leq1/2\).
The function \(g\) vanishes exactly at zero, and \(xg(x)>0\) for \(x\ne0\).
Since a nondegenerate Gaussian has probability zero of being zero,
these facts successively give \(m_1>0\), \(m_2>0\),
\(\sigma^2>0\), and \(\mathbb E[Z^{(3)}g(Z^{(3)})]>0\).
All expectations are finite by (I.3)--(I.4).
Also \(\mathbb E[Z^{(3)}g(Z^{(3)})]\leq\mathbb E (Z^{(3)})^2=m_2\), proving
\(0<\beta\leq1\).

### Exact finite-dimensional conditioning

Define the empirical second moments
\[
m_{1,n}=\frac{\|h_0^{(1)}\|^2}{n},\qquad
m_{2,n}=\frac{\|h_0^{(2)}\|^2}{n}.
\]
Almost surely \(m_{1,n}>0\): its vanishing would require all
\(z_{0,i}^{(1)}=0\). Given the first layer, the rows of \(W_0^{(2)}\)
give independent coordinates \(z_{0,i}^{(2)}\sim N(0,m_{1,n})\).
Thus, conditionally on \(m_{1,n}>0\), the probability that \(h_0^{(2)}=0\)
is zero. In particular \(m_{2,n}>0\) almost surely.
Given the variables in the first two layers, the \(z_{0,j}^{(3)}\) are independent
\(N(0,m_{2,n})\). Hence \(z_0^{(3)}\ne0\) and \(\|g(z_0^{(3)})\|>0\) almost surely.
Both random variances lie in \([0,H^2]\).

For a fixed nonzero \(h_0^{(2)}\), define the orthogonal projection
\[
P_n^{(2)}=\frac{h_0^{(2)}(h_0^{(2)})^T}{\|h_0^{(2)}\|^2}.
\]
Writing \((W_0^{(3)})_{j,:}\) for row \(j\), the exact decomposition is
\[
(W_0^{(3)})_{j,:}^T
=\frac{h_0^{(2)}\,z_{0,j}^{(3)}}{\|h_0^{(2)}\|^2}
+(I-P_n^{(2)})(W_0^{(3)})_{j,:}^T,\qquad
z_{0,j}^{(3)}=(W_0^{(3)})_{j,:}h_0^{(2)}.
\]
Conditionally on \(h_0^{(2)}\), the scalar \(z_{0,j}^{(3)}\) and vector
\((I-P_n^{(2)})(W_0^{(3)})_{j,:}^T\) are jointly Gaussian,
and their cross covariance is
\[
\mathbb E\!\left[
(I-P_n^{(2)})(W_0^{(3)})_{j,:}^T z_{0,j}^{(3)}
\mid h_0^{(2)}\right]
=\frac1n(I-P_n^{(2)})h_0^{(2)}=0.
\]
They are therefore independent: the characteristic function of a centered
joint Gaussian with zero cross covariance factors into its two marginal
characteristic functions. The residual vectors for distinct rows are
independent, have covariance \((I-P_n^{(2)})/n\), and are independent of the
entire vector \(z_0^{(3)}\). Since \(W_0^{(3)}\) is independent of all lower-layer
variables, the same statements hold after additionally conditioning on
those variables.

Multiplying row \(j\) by \(g(z_{0,j}^{(3)})\) and summing proves that, conditionally
on the lower layers and \(z_0^{(3)}\),
\[
u_n^{(2)}\ \overset{\mathrm{law}}{=}
\beta_n h_0^{(2)}+\sigma_n(I-P_n^{(2)})\xi,\qquad
\beta_n=\frac{(z_0^{(3)})^Tg(z_0^{(3)})}{\|h_0^{(2)}\|^2},\qquad
\sigma_n^2=\frac{\|g(z_0^{(3)})\|^2}{n},
\tag{I.5}
\]
where \(\xi\sim N(0,I_n)\) can be chosen independent of the lower layers
and \(z_0^{(3)}\). Indeed, the conditional mean is \(\beta_n h_0^{(2)}\), and the
conditional covariance is
\[
\sum_{j=1}^n g(z_{0,j}^{(3)})^2\,\frac{I-P_n^{(2)}}{n}
=\sigma_n^2(I-P_n^{(2)}).
\]
The square root \(\sigma_n\) is nonnegative and is positive almost surely.
If \(h_0^{(2)}=0\), then \(z_0^{(3)}=0\), \(g(z_0^{(3)})=0\), and the original \(u_n^{(2)}=0\).
On this null event set \(\beta_n=0\) and \(P_n^{(2)}=0\);
then \(\sigma_n=0\) and (I.5) remains valid. These conventions resolve
every zero denominator in (I.5).

Equation (I.5) is a conditional-law representation of the original
matrix-derived vector. It does not change the initialization or introduce
an independent network output. In particular, it retains the correlation
created by using the same matrix in \(z_0^{(3)}=W_0^{(3)}h_0^{(2)}\) and
\(u_n^{(2)}=(W_0^{(3)})^Tg(z_0^{(3)})\).

### Random variances and coefficients

For independent identically distributed variables of finite variance \(v\),
their sample average has variance \(v/n\); Chebyshev's inequality therefore
gives convergence in probability to their mean. We use this fact also
conditionally, integrating the conditional variance bound.

Applied to the bounded first-layer variables it gives
\[
m_{1,n}\longrightarrow m_1
\quad\text{in }L^2\text{ and in probability}.
\tag{I.6}
\]
Let \(G'\sim N(0,1)\) be a dummy variable in expectations and define on
\([0,H^2]\)
\[
f(q)=\mathbb E[\phi(\sqrt q\,G')^2],\qquad
a(q)=\mathbb E[\sqrt q\,G' g(\sqrt q\,G')],\qquad
b(q)=\mathbb E[g(\sqrt q\,G')^2].
\]
Each function is continuous, including at zero: its integrand is
pointwise continuous in \(q\), and (I.3)--(I.4) bound the integrands
respectively by \(H^2,H/2,H^2\), so dominated convergence applies.
Conditionally on the first layer,
\[
\mathbb E[m_{2,n}\mid z_0^{(1)}]=f(m_{1,n}),\qquad
\mathbb E[(m_{2,n}-f(m_{1,n}))^2\mid z_0^{(1)}]\leq H^4/n.
\]
Continuity of \(f\), (I.6), and this variance bound give
\[
m_{2,n}\longrightarrow f(m_1)=m_2
\quad\text{in probability}.
\tag{I.7}
\]
For example, continuity at \(m_1\) says that sufficiently small
\(|m_{1,n}-m_1|\) makes \(|f(m_{1,n})-f(m_1)|\) arbitrarily small;
the complementary event has probability tending to zero by (I.6).

Set \(A_n=(z_0^{(3)})^Tg(z_0^{(3)})/n\). Conditionally on the lower layers, (I.4) gives
\[
\begin{aligned}
\mathbb E[A_n\mid z_0^{(1)},W_0^{(2)}]&=a(m_{2,n}),&
\mathbb E[(A_n-a(m_{2,n}))^2\mid z_0^{(1)},W_0^{(2)}]
&\leq H^2/(4n),\\
\mathbb E[\sigma_n^2\mid z_0^{(1)},W_0^{(2)}]&=b(m_{2,n}),&
\mathbb E[(\sigma_n^2-b(m_{2,n}))^2\mid z_0^{(1)},W_0^{(2)}]
&\leq H^4/n.
\end{aligned}
\]
Using (I.7) and continuity of \(a,b\), we obtain
\[
A_n\longrightarrow a(m_2)=\mathbb E[Z^{(3)}g(Z^{(3)})],\qquad
\sigma_n^2\longrightarrow b(m_2)=\sigma^2
\quad\text{in probability}.
\]
Since \(m_2>0\), the event \(m_{2,n}\geq m_2/2\) has probability tending
to one. Division on this event and continuity of the square root yield
\[
\beta_n=A_n/m_{2,n}\longrightarrow\beta,\qquad
\sigma_n\longrightarrow\sigma
\quad\text{in probability}.
\tag{I.8}
\]
The ratio at zero uses the convention in (I.5). No deterministic lower
bound on the finite random variances was assumed.

### Projection correction and joint empirical convergence

The successive forward conditional Gaussian laws and (I.5) permit the
following exact construction in distribution. Draw the first layer and
three mutually independent standard Gaussian vectors
\(\eta,\zeta,\xi\), independent also of the first layer, and set
\[
z_{0,i}^{(2)}=\sqrt{m_{1,n}}\,\eta_i,\qquad
h_0^{(2)}=\phi(z_0^{(2)}),\qquad
z_0^{(3)}=\sqrt{m_{2,n}}\,\zeta,\qquad
u_n^{(2)}=\beta_n h_0^{(2)}+\sigma_n(I-P_n^{(2)})\xi.
\tag{I.9}
\]
The coefficients and variances in (I.9) are computed from the vectors
already drawn, exactly as above. Successively conditioning on the first
layer, on \(z_0^{(2)}\), and on \(z_0^{(3)}\) shows that (I.9) has the original
joint law of \((z_0^{(1)},z_0^{(2)},z_0^{(3)},u_n^{(2)})\). This equality includes
all dependencies needed below; it does not assert independence of the
original coordinate pairs.

For the projection correction, independence of \(\xi\) and \((h_0^{(2)},z_0^{(3)})\) gives,
on \(h_0^{(2)}\ne0\),
\[
\mathbb E\left[\left.
\frac{\|\sigma_nP_n^{(2)}\xi\|^2}{n}\right|h_0^{(2)},z_0^{(3)}\right]
=\frac{\sigma_n^2}{n}
\mathbb E\left[\left.\frac{((h_0^{(2)})^T\xi)^2}{\|h_0^{(2)}\|^2}\right|h_0^{(2)},z_0^{(3)}\right]
=\frac{\sigma_n^2}{n}\leq\frac{H^2}{n}.
\tag{I.10}
\]
On \(h_0^{(2)}=0\) the left side is zero by the stated conventions.
Thus \(\|\sigma_nP_n^{(2)}\xi\|/\sqrt n\) tends to zero in \(L^2\) and in
probability. This also covers \(n=1\), when \(P_n^{(2)}=I\) for \(h_0^{(2)}\ne0\).

On the representation space define the comparison coordinates
\[
\bar z_i^{(2)}=\sqrt{m_1}\,\eta_i,\qquad
\bar u_i^{(2)}=\beta\phi(\bar z_i^{(2)})+\sigma\xi_i.
\]
These comparison pairs are independent and identically distributed with
law \((Z^{(2)},U^{(2)})\). Since
\[
\frac1n\sum_i|z_{0,i}^{(2)}-\bar z_i^{(2)}|^2
=(\sqrt{m_{1,n}}-\sqrt{m_1})^2\,\frac1n\sum_i\eta_i^2,
\tag{I.11}
\]
the left side tends to zero in probability by (I.6) and
\(n^{-1}\sum_i\eta_i^2\to1\). The latter convergence follows from
\(\mathbb E\eta_i^2=1\), \(\operatorname{Var}(\eta_i^2)=2\) and
the sample-average variance bound. The same reasoning gives
\(\|\xi\|/\sqrt n\to1\) in probability.

The bound \(\phi'\leq1\) makes \(\phi\) Lipschitz with constant one.
Subtracting the comparison vector from (I.9) and using the triangle
inequality consequently gives
\[
\begin{split}
\frac{\|u_n^{(2)}-\bar u^{(2)}\|}{\sqrt n}
&\leq |\beta_n-\beta|\sqrt{m_{2,n}}
+|\beta|\frac{\|z_0^{(2)}-\bar z^{(2)}\|}{\sqrt n}\\
&\quad+|\sigma_n-\sigma|\frac{\|\xi\|}{\sqrt n}
+\frac{\|\sigma_nP_n^{(2)}\xi\|}{\sqrt n}
\longrightarrow0
\quad\text{in probability},
\end{split}
\tag{I.12}
\]
by (I.8)--(I.11) and \(m_{2,n}\leq H^2\).
In particular,
\[
D_n^2:=\frac1n\sum_i
\left(|z_{0,i}^{(2)}-\bar z_i^{(2)}|^2+|u_{n,i}^{(2)}-\bar u_i^{(2)}|^2\right)
\longrightarrow0
\quad\text{in probability}.
\tag{I.13}
\]

If \(F\) is bounded and uniformly continuous, let
\(\omega_F(\delta)=\sup_{\|x-x'\|\leq\delta}|F(x)-F(x')|\),
using the ordinary Euclidean norm on \(\mathbb R^2\).
At most a fraction \(D_n^2/\delta^2\) of the paired points have
distance exceeding \(\delta>0\), so
\[
\left|\frac1n\sum_i F(z_{0,i}^{(2)},u_{n,i}^{(2)})
-\frac1n\sum_i F(\bar z_i^{(2)},\bar u_i^{(2)})\right|
\leq\omega_F(\delta)+2\|F\|_\infty D_n^2/\delta^2.
\tag{I.14}
\]
First choosing \(\delta\) so that \(\omega_F(\delta)\) is small and then
using (I.13) proves that this difference tends to zero in probability.
The comparison average converges to \(\mathbb E F(Z^{(2)},U^{(2)})\) by
the sample-average variance bound, since its summands are bounded and
independent. We next justify the larger test class in (I.1).

### Uniform moments, unbounded tests, and \(L^1\)

The following moment bounds are uniform over every \(n\geq1\).
Gaussian integration by parts gives
\(\mathbb E(G')^{2k}=(2k-1)\mathbb E(G')^{2k-2}\):
integrate \(x^{2k-1}x e^{-x^2/2}\), whose boundary term vanishes.
Thus \(\mathbb E(G')^4=3\) and \(\mathbb E(G')^8=105\).
The forward conditional law gives
\[
\mathbb E|z_{0,i}^{(2)}|^4=3\mathbb E m_{1,n}^2\leq3H^4.
\tag{I.15}
\]
On \(m_{2,n}>0\), (I.4) and (I.9) give
\[
0\leq\beta_n
\leq\frac{\|z_0^{(3)}\|^2}{nm_{2,n}}
=\frac1n\sum_j\zeta_j^2.
\]
Convexity of \(t\mapsto t^4\) on \([0,\infty)\) therefore yields
\[
\mathbb E\beta_n^4
\leq\mathbb E\left(\frac1n\sum_j\zeta_j^2\right)^4
\leq\frac1n\sum_j\mathbb E\zeta_j^8=105.
\tag{I.16}
\]
The null-event convention satisfies the same moment bound.
Conditionally on \(h_0^{(2)},z_0^{(3)}\), each coordinate
\(\sigma_n((I-P_n^{(2)})\xi)_i\) is a centered Gaussian of variance at most
\(\sigma_n^2\leq H^2\), and hence of fourth moment at most \(3H^4\).
Using \(|r+s|^4\leq8(|r|^4+|s|^4)\) in (I.5), together with
\(|h_{0,i}^{(2)}|\leq H\) and (I.16), proves
\[
\mathbb E|u_{n,i}^{(2)}|^4\leq8H^4\mathbb E\beta_n^4+24H^4
\leq864H^4.
\tag{I.17}
\]
This is a direct moment estimate for the reused Gaussian matrix;
it requires no independence between its original output coordinates.
The population variables likewise have finite fourth moments because
\(Z^{(2)}\) is Gaussian and
\(|U^{(2)}|\leq|\beta|H+\sigma|G|\).
Since \((z^2+v^2)^2\leq2(z^4+v^4)\), (I.15)--(I.17) in particular imply
\[
\sup_n\mathbb E\left[\frac1n\sum_i
\bigl((z_{0,i}^{(2)})^2+(u_{n,i}^{(2)})^2\bigr)^2\right]<\infty.
\tag{I.18}
\]

Now let \(F\) have the continuous, at most quadratic growth in (I.1).
For \(R\geq1\), choose a continuous function
\(\chi_R:\mathbb R^2\to[0,1]\) equal to one on the ball of radius \(R\)
and zero outside the ball of radius \(R+1\); for example
\(\chi_R(x)=\max(0,\min(1,R+1-\|x\|))\).
Then \(F_R=\chi_RF\) is continuous with compact support and is bounded
and uniformly continuous, so (I.14) applies. For \(r=(z^2+v^2)^{1/2}\),
\[
|F(z,v)-F_R(z,v)|
\leq C_F(1+r^2)\mathbf1_{\{r>R\}}
\leq \frac{2C_F}{R^2}r^4.
\tag{I.19}
\]
By (I.18), the expectation of the empirical average of (I.19) is bounded
by a constant times \(R^{-2}\), uniformly in \(n\).
The analogous population expectation has the same bound, because the
population fourth moment is finite. Markov's inequality therefore
makes the empirical truncation error small in probability uniformly
in \(n\). First taking \(n\to\infty\) for \(F_R\), and then
\(R\to\infty\) in these bounds, proves the probability convergence
in (I.1).

For completeness, write
\(X_n=n^{-1}\sum_iF(z_{0,i}^{(2)},u_{n,i}^{(2)})\) and
\(\mu=\mathbb E F(Z^{(2)},U^{(2)})\), which is finite by the population
moment bound. Jensen's inequality and (I.18) give
\[
\sup_n\mathbb E|X_n|^2
\leq C_F^2\sup_n\mathbb E\left[\frac1n\sum_i
\bigl(1+(z_{0,i}^{(2)})^2+(u_{n,i}^{(2)})^2\bigr)^2\right]<\infty.
\tag{I.20}
\]
Here \((1+r^2)^2\leq2(1+r^4)\). In particular the averages are
uniformly integrable, since
\(\mathbb E[|X_n|\mathbf1_{\{|X_n|>K\}}]\leq\mathbb E|X_n|^2/K\).
More explicitly, for every \(\varepsilon>0\), Cauchy--Schwarz gives
\[
\mathbb E|X_n-\mu|
\leq\varepsilon+
\bigl(\mathbb E|X_n-\mu|^2\bigr)^{1/2}
\mathbb P(|X_n-\mu|>\varepsilon)^{1/2}.
\]
The second moments are bounded by (I.20), and the probabilities tend
to zero. Taking a limit superior and then \(\varepsilon\downarrow0\)
proves \(L^1\) convergence in (I.1). All probability and expectation
statements transfer from (I.9) to the canonical network by equality
of the joint laws for each \(n\).

### The curvature average and strict positivity

The test
\[
F(z,v)=[v\phi''(z)]_+
\]
is continuous. By (I.3),
\(0\leq F(z,v)\leq2|v|\leq1+v^2\), so it is in the class of (I.1).
This proves both convergences in (I.2) and finiteness of \(c_*\).

To prove strict positivity explicitly, on \(1\leq z\leq2\) we have
\[
-\phi''(z)=\frac{2z}{(1+z^2)^2}\geq\frac{2}{25}.
\]
Consider the event
\[
1\leq Z^{(2)}\leq2,\qquad
G\leq-\frac{|\beta|H+1}{\sigma}.
\tag{I.21}
\]
On (I.21), \(U^{(2)}=\beta\phi(Z^{(2)})+\sigma G\leq-1\), so
\([U^{(2)}\phi''(Z^{(2)})]_+\geq2/25\).
Conditionally on any \(Z^{(2)}=z\in[1,2]\), the second event in (I.21)
has the same strictly positive probability, since \(G\) is independent
of \(Z^{(2)}\) and \(\sigma>0\).
Writing \(\Phi\) for the standard Gaussian distribution function gives
\[
c_*\geq\frac{2}{25}
\left[\Phi\!\left(\frac2{\sqrt{m_1}}\right)
-\Phi\!\left(\frac1{\sqrt{m_1}}\right)\right]
\Phi\!\left(-\frac{|\beta|H+1}{\sigma}\right)>0.
\tag{I.22}
\]
The bracket is positive because \(m_1>0\) and the Gaussian density
is strictly positive on every finite interval; the last factor is
positive because its argument is finite.

This proves the claimed initial hidden-layer empirical law and curvature
limit. The Gaussian representation was exact at finite \(n\); only the
explicit projection correction and empirical averages were passed to
their limits. No central limit approximation or independence assertion
for the original finite coordinate pairs is involved. \(\square\)


## C. Positive middle curvature at small feature times

For the canonical tiny-readout initialization, the actual middle coefficient
\(q_i^{(2)}\phi''(z_i^{(2)})\) has a positive-part mean of linear size at small
fixed feature times. A positive fraction of the coefficients have that size.
The proof differentiates the actual trained query and controls its remainder;
it does not replace the trajectory by an evolved zero-readout solution.
The datum, raw metric and loss are those in S; clipped variants are expressly
defined below and are not asserted to be loss gradients.

### 1. Exact dynamics and deterministic path bounds

Let \(\phi=\arctan\), \(c=\pi/2\), and fix a feature horizon \(S>0\).
The first layer is the vector \(z^{(1)}=W^{(1)}\); the hidden matrices
are \(W^{(2)},W^{(3)}\); \(W^{(4)}\) is the stored readout vector.
Use ordinary Euclidean vector norms, ordinary matrix operator and
Frobenius norms, and finite transpose \(T\). Define
\[
h^{(\ell)}=\phi(z^{(\ell)}),\quad
z^{(2)}=W^{(2)}h^{(1)},\quad z^{(3)}=W^{(3)}h^{(2)},
\]
\[
\delta^{(3)}=W^{(4)}\odot\phi'(z^{(3)}),\quad
q^{(2)}=(W^{(3)})^T\delta^{(3)},\quad
\delta^{(2)}=\phi'(z^{(2)})\odot\tau(q^{(2)}).
\]
Here \(\tau\) is any fixed prescribed map with
\(|\tau(v)|\le|v|\) and \(|\tau(v)-\tau(w)|\le|v-w|\).
The identity gives the exact uncut model. There is no pruning mask.
Every trained block obeys its actual feature equation:
\[
\begin{gathered}
(z^{(1)})'=\phi'(z^{(1)})\odot(W^{(2)})^T\delta^{(2)},\\
(W^{(2)})'=\delta^{(2)}(h^{(1)})^T/n,\quad
(W^{(3)})'=\delta^{(3)}(h^{(2)})^T/n,\quad
(W^{(4)})'=h^{(3)}.
\end{gathered}
\tag{C.1}
\]
The estimates are in feature time \(s\), not physical time. The canonical
uncut physical flow is (C.1) times \(2(1-f)\), for
\(f=(W^{(4)})^Th^{(3)}/n\) and loss \((f-1)^2\).
No physical-clock or exact-GD convergence assertion is made here.

For arbitrary finite initial data put
\[
M=\max_{\ell=2,3}\|W^{(\ell)}(0)\|_{\rm op},\qquad
\varepsilon=\frac{\|W^{(4)}(0)\|_2}{\sqrt n},\qquad
\alpha=\|W^{(4)}(0)\|_\infty.
\]
These definitions impose no upper bound on \(\varepsilon,\alpha\).
In particular \(\varepsilon\le\alpha\le\sqrt n\,\varepsilon\).
Define the finite nonnegative constants
\[
\begin{gathered}
K_3=M+c(\varepsilon S+cS^2/2),\\
K_2=M+cK_3(\varepsilon S+cS^2/2),\\
J=K_3(c^2+K_2^2),\qquad K=c^2+K_3J.
\end{gathered}
\tag{C.2}
\]
They are polynomials in \(M,\varepsilon\), with coefficients depending
only on \(S\). The readout equation and \(|\phi|\le c\), \(|\phi'|\le1\)
give
\[
\frac{\|\delta^{(3)}(s)\|_2}{\sqrt n}
\le\frac{\|W^{(4)}(s)\|_2}{\sqrt n}\le\varepsilon+cs,\qquad
\|W^{(4)}(s)\|_\infty\le\alpha+cs.
\tag{C.3}
\]
Using \(\|uv^T/n\|_{\rm F}=\|u\|_2\|v\|_2/n\) in (C.1) yields
\[
\|W^{(3)}(s)-W^{(3)}(0)\|_{\rm F}
\le c(\varepsilon s+cs^2/2),\quad
\|W^{(3)}(s)\|_{\rm op}\le K_3,
\]
\[
\frac{\|\delta^{(2)}(s)\|_2}{\sqrt n}\le K_3(\varepsilon+cs),
\quad
\|W^{(2)}(s)-W^{(2)}(0)\|_{\rm F}
\le cK_3(\varepsilon s+cs^2/2),\quad
\|W^{(2)}(s)\|_{\rm op}\le K_2.
\tag{C.4}
\]
The first-layer velocity divided by \(\sqrt n\) is at most
\(K_2K_3(\varepsilon+cs)\).
At each fixed width, the vector field is locally Lipschitz, including
the Lipschitz clipping. Local existence and uniqueness follow from the
contraction of its integral equation on a sufficiently short interval
in a finite-dimensional ball. The displayed bounds keep every parameter
entry in a bounded set on a prescribed finite horizon. A hypothetical
finite endpoint then has a state limit, since the vector field is
bounded on that compact set, and local existence extends it.
Thus (C.1) has a unique trajectory through \([0,S]\).

Differentiating only the forward factors gives the exact identities
\[
(z^{(2)})'=
\left[\frac{\|h^{(1)}\|_2^2}{n}I+
W^{(2)}\operatorname{diag}(\phi'(z^{(1)})^2)(W^{(2)})^T\right]\delta^{(2)},
\]
\[
(z^{(3)})'=\frac{\|h^{(2)}\|_2^2}{n}\delta^{(3)}
+W^{(3)}\operatorname{diag}(\phi'(z^{(2)}))(z^{(2)})'.
\tag{C.5}
\]
No derivative of \(\tau\) is used. Consequently
\[
\frac{\|(z^{(2)})'(s)\|_2}{\sqrt n}\le J(\varepsilon+cs),\qquad
\frac{\|(z^{(3)})'(s)\|_2}{\sqrt n}\le K(\varepsilon+cs).
\tag{C.6}
\]
Integration bounds the corresponding displacements by
\(J(\varepsilon s+cs^2/2)\) and \(K(\varepsilon s+cs^2/2)\).

### 2. A direct Duhamel remainder for the actual middle query

Let \(g(v)=\phi'(v)\phi(v)\) and define the initial hidden-block query
\[
u_n^{(2)}=(W^{(3)}(0))^T g(z^{(3)}(0)).
\tag{C.7}
\]
This is a function only of the original hidden initialization, not an
extra random readout seed. We use
\[
|g|\le c,\quad |g'|=|(\phi')^2+\phi\phi''|\le1+2c,\quad
|\phi''|\le2,\quad
|\phi'''(v)|=\frac{|-2+6v^2|}{(1+v^2)^3}\le8.
\tag{C.8}
\]
In particular \(\|u_n^{(2)}\|_2/\sqrt n\le Mc\).

Differentiate the actual query, retaining the trained \(W^{(3)}\):
\[
\begin{split}
(q^{(2)})'
={}&h^{(2)}\frac{\|\delta^{(3)}\|_2^2}{n}
+(W^{(3)})^Tg(z^{(3)})\\
&+(W^{(3)})^T
\bigl[W^{(4)}\odot\phi''(z^{(3)})\odot(z^{(3)})'\bigr].
\end{split}
\tag{C.9}
\]
The first term is exactly \(((W^{(3)})')^T\delta^{(3)}\); the other
terms come from
\((\delta^{(3)})'=g(z^{(3)})+
W^{(4)}\odot\phi''(z^{(3)})\odot(z^{(3)})'\).
Thus (C.9) also holds for merely Lipschitz clipping.

For \(A=c^2+M(1+2c)K\), (C.4), (C.6), and (C.8) give
\[
\frac{\|(W^{(3)}(s))^Tg(z^{(3)}(s))-u_n^{(2)}\|_2}{\sqrt n}
\le A(\varepsilon s+cs^2/2).
\tag{C.10}
\]
Indeed the trained-matrix increment contributes at most
\(c^2(\varepsilon s+cs^2/2)\); the change of \(g\) contributes at most
\(M(1+2c)K(\varepsilon s+cs^2/2)\).
The other two terms of (C.9) have norms divided by \(\sqrt n\) bounded by
\[
c(\varepsilon+cs)^2,\qquad
2K_3K(\alpha+cs)(\varepsilon+cs).
\]
Also \(\|q^{(2)}(0)\|_2/\sqrt n\le M\varepsilon\).
Integrating (C.9)--(C.10) therefore proves, for every \(0\le s\le S\),
\[
\frac{\|q^{(2)}(s)-s u_n^{(2)}\|_2}{\sqrt n}\le R(s),
\tag{C.11}
\]
where the explicit nonnegative remainder is
\[
\begin{split}
R(s)={}&M\varepsilon+
c\left(\varepsilon^2s+\varepsilon c s^2+\frac{c^2s^3}{3}\right)\\
&+A\left(\frac{\varepsilon s^2}{2}+\frac{cs^3}{6}\right)\\
&+2K_3K\left(\alpha\varepsilon s+
\frac{c(\alpha+\varepsilon)s^2}{2}+\frac{c^2s^3}{3}\right).
\end{split}
\tag{C.12}
\]
The initial readout has not been set to zero or hidden in a
width-dependent Taylor remainder.

Define the empirical positive parts
\[
B_n(s)=\frac1n\sum_i[q_i^{(2)}(s)\phi''(z_i^{(2)}(s))]_+,\qquad
c_n=\frac1n\sum_i[(u_n^{(2)})_i\phi''(z_i^{(2)}(0))]_+.
\tag{C.13}
\]
The map \(x\mapsto[x]_+\) is 1-Lipschitz. Separate the query change
from the change of \(\phi''\), then use Cauchy--Schwarz and (C.6), (C.8):
\[
\begin{split}
|B_n(s)-s c_n|
&\le 2\frac{\|q^{(2)}(s)-s u_n^{(2)}\|_2}{\sqrt n}\\
&\quad+8s\frac{\|u_n^{(2)}\|_2}{\sqrt n}
\frac{\|z^{(2)}(s)-z^{(2)}(0)\|_2}{\sqrt n}\\
&\le 2R(s)+8McJ\,s(\varepsilon s+cs^2/2).
\end{split}
\tag{C.14}
\]
These inequalities are pathwise, simultaneous in \(s\), and use
constants independent of the choice of allowed fixed clipping.
For \(M\le M_*,\varepsilon\le1,\alpha\le1\), collecting the explicit
terms in (C.12)--(C.14) yields
\[
|B_n(s)-s c_n|\le C_{S,M_*}
(\varepsilon+\alpha s^2+s^3),\qquad 0\le s\le S.
\tag{C.15}
\]
For example, \(\alpha\varepsilon s\le S\varepsilon\),
\(\varepsilon^2s\le S\varepsilon\), and
\(\varepsilon s^2\le S^2\varepsilon\); every remaining term has one
of the two displayed time powers. Equations (C.2) bound all coefficients
uniformly under these restrictions.

### 3. Canonical initialization and the required initial law

The canonical initial blocks are mutually independent:
\[
z_i^{(1)}(0)\sim N(0,1),\quad
W_{ij}^{(\ell)}(0)\sim N(0,1/n)\ (\ell=2,3),\quad
W_i^{(4)}(0)=G_i^{(4)}/n,\quad G_i^{(4)}\sim N(0,1).
\tag{C.16}
\]
Independence and identical distribution here concern initialization
only, not trained or reused-matrix coordinate outputs.

Fragment I proves the following initialization law. For independent standard
Gaussians \(G_1,G_2,G_3,G\), put
\[
m_1=\mathbb E\phi(G_1)^2,\quad
Z^{(2)}=\sqrt{m_1}G_2,\quad m_2=\mathbb E\phi(Z^{(2)})^2,\quad
Z^{(3)}=\sqrt{m_2}G_3,
\]
\[
\beta=\frac{\mathbb E[Z^{(3)}g(Z^{(3)})]}{m_2},\qquad
\sigma^2=\mathbb E[g(Z^{(3)})^2],\qquad
c_*=\mathbb E\left[
\left[\phi''(Z^{(2)})(\beta\phi(Z^{(2)})+\sigma G)\right]_+\right].
\tag{C.17}
\]
Then \(m_1,m_2,\sigma,c_*>0\) and \(c_n\to c_*\) in probability
and in \(L^1\). The expectation in the last definition means expectation
of the positive part. The independent \(G\) describes unexplored
conditional Gaussian randomness in the reused hidden matrix, not a
change of the readout initialization.
The full proof, including its moment and positivity arguments, is in fragment I.

Here are the probability and integrability details for applying (C.14)
directly to (C.16). On the initial event
\[
\Omega_n=\{M\le10,\ \|G^{(4)}\|_2/\sqrt n\le2\},
\tag{C.18}
\]
one has \(\varepsilon\le2/n\), \(\alpha\le2/\sqrt n\).
For \(n\ge4\), (C.15) therefore gives
\[
|B_n(s)-s c_n|\le C_S
(n^{-1}+n^{-1/2}s^2+s^3),\quad 0\le s\le S,
\tag{C.19}
\]
on the same event for every allowed fixed clipping.
Moreover
\[
\mathbb P(\Omega_n^c)\le
4e^{-(25/2-2\log9)n}+e^{-(1-\frac12\log2)n}.
\tag{C.20}
\]
To check this directly, a maximal \(1/4\)-separated
spherical set is a \(1/4\)-net with at most \(9^n\) points by disjoint
radius-\(1/8\) ball packing. Approximate both arguments of a bilinear
form using this net; the two errors are at most half the operator norm,
so that norm is at most twice the net maximum. For a fixed pair of unit
vectors a canonical Gaussian matrix bilinear form has variance \(1/n\),
and its two-sided tail at \(r/2\) is at most \(2e^{-nr^2/8}\), by its
Gaussian exponential moment and Markov's inequality. Union over both
matrices and both nets gives
\[
\mathbb P(M>r)\le4e^{2n\log9-nr^2/8}.
\]
Use \(r=10\) for (C.20). For the readout,
\(\mathbb E e^{\|G^{(4)}\|_2^2/4}=2^{n/2}\);
Markov's inequality at squared norm \(4n\) gives its stated error.

For \(r\ge10\), the same matrix bound is at most \(4e^{-r^2/16}\);
tail integration thus bounds every fixed moment of \(M\) uniformly in
width. Differentiating the Gaussian squared-norm exponential moment
at zero gives, for integers \(k\ge1\),
\[
\mathbb E\varepsilon^{2k}
=n^{-3k}\prod_{j=0}^{k-1}(n+2j)\le C_k n^{-2k},\qquad
\mathbb E\alpha^{2k}\le n^k\mathbb E\varepsilon^{2k}
\le C_k n^{-k}.
\tag{C.21}
\]
Differentiation is justified by domination with a squared-norm
exponential moment at a fixed positive parameter less than \(1/2\).
All fixed moments of the polynomial constants in (C.2), (C.10) and (C.14)
are consequently uniformly bounded, using Cauchy--Schwarz for their
mixed moments.

For any such polynomial factor \(P\), Cauchy--Schwarz gives
\[
\mathbb E[|P|\varepsilon]\le C_S/n,\quad
\mathbb E[|P|\varepsilon^2]\le C_S/n^2,\quad
\mathbb E[|P|\alpha]\le C_S/\sqrt n.
\]
Also \(\alpha\varepsilon\le\sqrt n\,\varepsilon^2\) gives
\(\mathbb E[|P|\alpha\varepsilon]\le C_S n^{-3/2}\).
Apply these estimates to the unrestricted (C.12)--(C.14), not just on
\(\Omega_n\), to obtain
\[
\mathbb E|B_n(s)-s c_n|\le
C_S(n^{-1}+n^{-1/2}s^2+s^3),\qquad 0\le s\le S.
\tag{C.22}
\]
This holds uniformly over prescribed clippings, including any
measurably selected fixed clipping, because the same measurable
initial-data polynomial dominates (C.14). No uncountable supremum is
interchanged with expectation.

### 4. Actual positive-time consequences and their limits

Take \(S=1\), and let \(C_1\) be the deterministic constant in (C.19).
The initialization law’s \(c_*>0\) permits a fixed \(s_0\in(0,1]\) with
\(C_1s_0^2\le c_*/8\). For any fixed \(a\in(0,s_0]\), on the measurable
initial event \(\Omega_n\cap\{c_n\ge3c_*/4\}\), equation (C.19) gives
\[
\frac{B_n(s)}s\ge\frac{3c_*}{4}
-C_1(n^{-1}/a+n^{-1/2}s_0+s_0^2),
\qquad a\le s\le s_0.
\]
For all sufficiently large \(n\), depending on \(a\), the two
width-dependent terms times \(C_1\) sum to at most \(c_*/8\).
The event has probability tending to one. On it, simultaneously for
every allowed fixed clipping and every \(s\in[a,s_0]\),
\[
B_n(s)\ge\frac{c_*}{2}s.
\tag{C.23}
\]
This is an actual common positive interval after the width limit,
not a width-dependent Taylor neighborhood. It does not assert (C.23)
down to arbitrarily small \(s\) uniformly in \(n\).

The positive part is not carried by a vanishing fraction of middle
coordinates on these events. For \(S=1\), set
\[
D=2(1+c)[10+c(1+c/2)].
\]
Increasing the deterministic width threshold so that \(2/n\le a\),
(C.3)--(C.4) give for \(a\le s\le s_0\)
\[
\left(\frac1n\sum_i
|q_i^{(2)}(s)\phi''(z_i^{(2)}(s))|^2\right)^{1/2}
\le 2K_3(\varepsilon+cs)\le Ds.
\]
Let \(p_n(s)\) be the fraction of indices with
\(q_i^{(2)}(s)\phi''(z_i^{(2)}(s))\ge c_*s/4\).
The positive-part mean on its complementary indices is at most
\(c_*s/4\). Cauchy--Schwarz on the selected indices, together with
(C.23), therefore yields
\[
\frac{c_*s}{2}\le B_n(s)\le\frac{c_*s}{4}
+Ds\sqrt{p_n(s)},\qquad
p_n(s)\ge\left(\frac{c_*}{4D}\right)^2>0.
\tag{C.23a}
\]
This is simultaneous in the same time prefixes and allowed fixed
clippings. It is a positive fraction of scalar curvature coefficients,
not a claim about eigenvalues of a full parameter Hessian.

The expectation version follows with the explicit error:
\[
\mathbb E|B_n(s)-s c_*|
\le C_S(n^{-1}+n^{-1/2}s^2+s^3)+s\,\mathbb E|c_n-c_*|.
\tag{C.24}
\]
In particular, for each fixed \(s>0\),
\[
c_*s-C_Ss^3\le\liminf_{n\to\infty}\mathbb E B_n(s)
\le\limsup_{n\to\infty}\mathbb E B_n(s)\le c_*s+C_Ss^3.
\tag{C.25}
\]
The constants are uniform over allowed fixed clippings; (C.25) also
allows a prescribed width-dependent sequence of such maps.
Taking \(n\to\infty\) first and then \(s\downarrow0\) proves
\[
\lim_{s\downarrow0}\liminf_{n\to\infty}\frac{\mathbb E B_n(s)}s
=\lim_{s\downarrow0}\limsup_{n\to\infty}\frac{\mathbb E B_n(s)}s
=c_*>0.
\tag{C.26}
\]
Equation (C.25) alone does not assert convergence in \(n\) at fixed
positive time; its nonzero \(s^3\) error must not be discarded.

Consequently neither coordinatewise nonpositivity of the middle
coefficient nor a canonical mean positive-part bound of fifth order
can be obtained by transplanting the top-layer sign-lag argument.
For any fixed finite proposed coefficient of \(s^5\), choose a small
fixed \(s\le s_0\) where it is less than \(c_*s/2\); (C.23) contradicts
that bound with probability tending to one. The expectation version
is likewise contradicted by (C.25) for sufficiently small fixed \(s\).

This does not rule out a positive Gronwall constant, cancellation with
other signed work, or stronger actual response estimates. The coefficient's
positive part is not the Hessian quadratic form of an actual response.
No transported covariance bound, uniform tail envelope, population
restartability, full joint limit, or negative canonical resolution
is established here.

The clause concerning a measurably selected fixed clipping has a precise
interpretation. Give the set of 1-Lipschitz maps dominated by the identity the
compact-open metric \(\sum_{j\ge1}2^{-j}(1\wedge\sup_{|x|\le j}|\tau(x)-\nu(x)|)\).
At fixed width, finite initial data and finite horizon, the polynomial primal
bounds confine all solutions with nearby data to a common finite-dimensional
compact set. Their vector fields have a common local Lipschitz constant in
state and converge uniformly there when the maps converge compact-open.
Subtracting their integral equations and applying scalar Gronwall proves
continuous dependence on the data and map. Evaluations of all fields, and hence
the errors above, are measurable under a measurable selection of a map that is
then held fixed in time. The initial-data polynomial bounds already dominate
all those paths, so no supremum over random Gaussian events is required.


## E. Moderate-sine physical controls

#### E.1. Activation and exact finite model

Put

\[
 v=(1-e^{-8})/2-4e^{-4},\qquad N=\sqrt{1+4v/25},
\qquad \Phi(z)=az+b\sin(2z),
\]
\[
 a=(1-4e^{-2}/5)/N,\qquad b=2/(5N).
\]

For \(G\sim N(0,1)\), the Gaussian Fourier integral and its derivative give
\(\mathbb E\sin^2(2G)=(1-e^{-8})/2\) and
\(\mathbb E[G\sin(2G)]=2e^{-2}\). Hence \(v\) is the squared \(L^2\) norm
of \(\sin(2G)-2e^{-2}G\), which is orthogonal to \(G\) and is not zero.
Thus \(v>0\), \(N>1\), and writing
\(\Phi(G)=[G+(2/5)(\sin(2G)-2e^{-2}G)]/N\) also shows
\(\mathbb E\Phi(G)^2=1\). The exact derivatives are

\[
 \Phi'(z)=a+2b\cos(2z),\qquad
 \Phi''(z)=-4b\sin(2z).
\]

Since `e^2>4`,

\[
 0<m:=(1/5-4e^{-2}/5)/N\le\Phi'(z)<2,
 \qquad |\Phi''(z)|<2,
 \qquad \Phi(0)=0,\quad |\Phi(z)|\le2|z|.       \tag{E.1}
\]

No small coefficient or condition on the observation horizon is used in (E.1). The lemmas below in fact apply to any C2 activation with `phi(0)=0`, `||phi'||_infinity<=2` and `||phi''||_infinity<=2`; the lower slope is not needed for them. They hold for any input correlation in `[-1,1]`, so in particular for any fixed separated pair.

### 2. Raw norm and estimates on a primal ball

Use two fixed samples \((x_a,y_a)\), \(a=1,2\), with
\(x_a\in\mathbb R^d\), \(\|x_a\|_2^2=d\), \(y_a\in\{-1,1\}\), and any
\(\rho=x_1^Tx_2/d\in[-1,1]\). The activation above is used in all three hidden
layers. Write \(C=W^{(4)}\) for the stored finite readout and define
\[
 z_a^{(1)}=W^{(1)}x_a/\sqrt d,\quad
 z_a^{(2)}=W^{(2)}h_a^{(1)},\quad z_a^{(3)}=W^{(3)}h_a^{(2)},\quad
 h_a^{(\ell)}=\Phi(z_a^{(\ell)}),\quad f_a=C^Th_a^{(3)}/n,
 \quad r_a=f_a-y_a,
 \quad\mathcal L=(r_1^2+r_2^2)/2.
\]
The backward fields have no residual factor:
\[
 \delta_a^{(3)}=C\odot\Phi'(z_a^{(3)}),\quad
 q_a^{(2)}=(W^{(3)})^T\delta_a^{(3)},\quad
 \delta_a^{(2)}=\Phi'(z_a^{(2)})\odot q_a^{(2)},\quad
 q_a^{(1)}=(W^{(2)})^T\delta_a^{(2)},\quad
 \delta_a^{(1)}=\Phi'(z_a^{(1)})\odot q_a^{(1)}.
\]
All blocks train in physical time with unit multipliers and raw metric
\[
 \|d\Theta\|_{raw}^2=n^{-1}\|dW^{(1)}\|_F^2+
 \|dW^{(2)}\|_F^2+\|dW^{(3)}\|_F^2+n^{-1}\|dC\|_2^2.
\]
Thus the exact vector field \(V=-\nabla_{raw}\mathcal L\) is
\[
 \dot W^{(1)}=-\sum_{a=1}^2r_a\delta_a^{(1)}x_a^T/\sqrt d,\qquad
 \dot W^{(\ell)}=-\sum_{a=1}^2r_a\delta_a^{(\ell)}(h_a^{(\ell-1)})^T/n
 \quad(\ell=2,3),\qquad
 \dot C=-\sum_{a=1}^2r_ah_a^{(3)}.
\]
Raw GD means \(\Theta_{k+1}=\Theta_k+\eta_nV(\Theta_k)\),
\(\eta_n=n^{-2}\), simultaneously in these weights; weights are linearly
interpolated and all hidden fields are recomputed. No feature clock is used.
The canonical initialization has independent entries
\(W^{(1)}_{ij}\sim N(0,1)\), \(W^{(2)}_{ij},W^{(3)}_{ij}\sim N(0,1/n)\),
\(C_i\sim N(0,n^{-2})\), with independence between all blocks. Initial sample
preactivations are correlated according to \(\rho\), not independently
redrawn for the two samples.

All vector estimates below use the displayed Euclidean RMS factors. Suppose

\[
 \max_i\frac{\|z_i^{(1)}\|_2}{\sqrt n},\quad \|W^{(2)}\|_{op},\quad
 \|W^{(3)}\|_{op},\quad\frac{\|C\|_2}{\sqrt n}\le B,\qquad B\ge1.      \tag{E.2}
\]

The following bounds follow successively from (E.1):

| Field | Norm bound |
|---|---:|
| `h^{(1)}` | `2B` |
| `z^{(2)},h^{(2)}` | `2B^2,4B^2` |
| `z^{(3)},h^{(3)}` | `4B^3,8B^3` |
| `delta^{(3)},q^{(2)}` | `2B,2B^2` |
| `delta^{(2)},q^{(1)},delta^{(1)}` | `4B^2,4B^3,8B^3` |

Each table entry bounds the displayed field’s Euclidean norm divided by \(\sqrt n\), maximized over the two samples. Since the labels have modulus one,

\[
 \sum_i|r_i|\le16B^4+2\le18B^4.                  \tag{E.3}
\]

Let `V=-grad_raw L` be the actual physical vector field. Each of its four parameter blocks has raw norm at most `144B^7`, and hence

\[
 \|V\|_{raw}\le576B^7.                           \tag{E.4}
\]

For a middle block this uses

\[
 \|uh^T/n\|_F=\frac{\|u\|_2}{\sqrt n}\frac{\|h\|_2}{\sqrt n}.
\]

For the first block,

\[
 n^{-1/2}\|u x_i^T/\sqrt d\|_F=\|u\|_2/\sqrt n
\]

because `||x_i||^2=d`. Thus no dimension or width factor enters (E.4). The same argument applies to population fields, with Hilbert--Schmidt norms of the learned increments.

### 3. A dimension-explicit raw Lipschitz estimate

At width n, let two states both satisfy (E.2), and let `d_0` be their raw distance. Forward differences satisfy

\[
 \frac{\|\Delta z^{(1)}\|_2}{\sqrt n}\le d_0,\quad
 \frac{\|\Delta h^{(1)}\|_2}{\sqrt n}\le2d_0,\quad
 \frac{\|\Delta z^{(2)}\|_2}{\sqrt n}\le4Bd_0,\quad
 \frac{\|\Delta h^{(2)}\|_2}{\sqrt n}\le8Bd_0,
\]
\[
 \frac{\|\Delta z^{(3)}\|_2}{\sqrt n}\le12B^2d_0,\quad
 \frac{\|\Delta h^{(3)}\|_2}{\sqrt n}\le24B^2d_0,\quad
 \sum_i|\Delta r_i|\le64B^3d_0.                    \tag{E.5}
\]

For example,

`Delta z^{(2)}=W^{(2)} Delta h^{(1)}+Delta W^{(2)} h_tilde^1`,

and `||Delta W^{(2)}||op<=||Delta W^{(2)}||F<=d_0`. The last inequality in (E.5) uses

`|Delta f_i| <= (||Delta C||_2 ||h_i^{(3)}||_2 + ||C_tilde||_2 ||Delta h_i^{(3)}||_2)/n <=32B^3 d_0`.

For the backward gates, use

\[
 \frac{\|\Phi'(z)q-\Phi'(\widetilde z)\widetilde q\|_2}{\sqrt n}
 \le2\frac{\|q-\widetilde q\|_2}{\sqrt n}
       +2\frac{\|\widetilde q\|_\infty\|z-\widetilde z\|_2}{\sqrt n},
 \quad \|u\|_\infty\le\|u\|_2.
\]

Substitution of (E.5) and the field bounds gives, in causal order,

\[
 \frac{\|\Delta\delta^{(3)}\|_2}{\sqrt n}\le26\sqrt n B^3d_0,\quad
 \frac{\|\Delta q^{(2)}\|_2}{\sqrt n}\le28\sqrt n B^4d_0,\quad
 \frac{\|\Delta\delta^{(2)}\|_2}{\sqrt n}\le72\sqrt n B^4d_0,
\]
\[
 \frac{\|\Delta q^{(1)}\|_2}{\sqrt n}\le76\sqrt n B^5d_0,\quad
 \frac{\|\Delta\delta^{(1)}\|_2}{\sqrt n}\le160\sqrt n B^5d_0.         \tag{E.6}
\]

For instance the middle gate difference is at most

`2(28 sqrt(n) B^4)d_0 + 2(sqrt(n) 2B^2)(4B)d_0 <=72 sqrt(n) B^4 d_0`.

Expanding each rank-one update and its residual then gives respective raw block Lipschitz bounds

\[
 3392\sqrt n B^9,\quad3248\sqrt n B^9,\quad
 2672\sqrt n B^9,\quad944\sqrt n B^9.
\]

These four coefficients come respectively from
\(512+2880\), \(512+2592+144\), \(512+1872+288\), and \(512+432\):
the first summand in each case differentiates the residual, the second the
backward field (or the readout update's feature), and the third, when present,
the rank-one feature factor. For example the first-block bound is
\((64B^3)(8B^3)+(18B^4)(160\sqrt n B^5)
 \le3392\sqrt n B^9\).
Their sum is 10256. Consequently the conservative bound

\[
 \|V(\Theta)-V(\widetilde\Theta)\|_{raw}
 \le11000\sqrt n B^9\|\Theta-\widetilde\Theta\|_{raw}        \tag{E.7}
\]

holds whenever the two states satisfy (E.2). The primal set (E.2) is convex in the raw parameters, so the same bound controls the entire segment joining them. This is a finite-width estimate; its `sqrt(n)` factor is not dropped in a population argument.

### 4. Unconditional finite-time raw-GD energy

Fix an observation horizon T and an initialization with primal bounds at most `b_0>=1` and loss `E_0`. Put

\[
 R=\sqrt{2(T+1)E_0}+2,\qquad B=b_0+R+1,
 \qquad h=n^{-2}.
\]

Assume n is sufficiently large that

\[
 11000B^9n^{-3/2}\le1,\qquad576B^7n^{-2}\le1.      \tag{E.8}
\]

Then the actual simultaneous raw GD iterates through time T, and one additional endpoint if necessary, satisfy

\[
 \mathcal L(\Theta_k)\le E_0,\qquad
 \sum_{j<k}h\|V(\Theta_j)\|_{raw}^2\le2E_0,
\]
\[
 \|\Theta_k-\Theta_0\|_{raw}
 \le\sqrt{2khE_0}\le\sqrt{2(T+1)E_0}.             \tag{E.9}
\]

Proof. Stop provisionally before raw distance R from initialization. A raw displacement of size R changes either initial operator norm, the readout norm, or a first-layer sample norm by at most R, so (E.2) holds with room to spare. The second inequality in (E.8) and (E.4) keep the next Euler segment inside the larger primal ball B. Taylor's formula for the scalar loss and (E.7) give

\[
 \mathcal L(\Theta+hV)\le\mathcal L(\Theta)
      -h\|V\|_{raw}^2+\tfrac12(11000\sqrt n B^9)h^2\|V\|_{raw}^2
 \le\mathcal L(\Theta)-\tfrac12h\|V\|_{raw}^2.
\]

Summing proves the first two claims in (E.9). Cauchy--Schwarz for the sum of raw increments proves the third, which is strictly below R. This closes the induction and removes the stop. No population flow, tail bound, convergence theorem, or fixed-width comparison with continuous GF was assumed.

For the stated initialization one may take \(b_0=10\) and \(E_0\le2\)
on events with probability tending to one. For each sample, the first
preactivations are iid \(N(0,1)\) over neurons, so Chebyshev's inequality
applied to their squares proves RMS convergence to one; union over the two
samples suffices even when they are correlated. The sphere-net argument in
fragment S bounds both hidden operator norms by 10 with probability tending
to one. Also \(\mathbb E\|C_0\|_2^2/n=n^{-2}\), so its RMS vanishes in
probability. On the hidden-operator/first-field event, the field table bounds
\(\|h_a^{(3)}(0)\|_2/\sqrt n\) by a deterministic constant. Conditional on
these hidden fields, independence of \(C_0\) gives
\(\mathbb E[f_a(0)^2\mid h_a^{(3)}(0)]=\|h_a^{(3)}(0)\|_2^2/n^4=O(n^{-3})\).
Thus both predictions converge to zero in probability and \(E_0\to1\).
The initial hidden RMS bounds used below follow from the same field table.
For each fixed \(T\), (E.8)–(E.9) consequently hold with constants uniform in
width on events of probability tending to one.

This proves stable finite-horizon raw GD at the prescribed step; it does not identify its strong population limit.

### 5. Finite GF and weak path-law tightness

At every fixed width the finite-dimensional smooth vector field is locally Lipschitz. Its true gradient-flow energy identity is

\[
 \mathcal L(t)+\int_0^t\|\dot\Theta(s)\|_{raw}^2ds=E_0,
 \quad
 \|\Theta(t)-\Theta(0)\|_{raw}\le\sqrt{tE_0}.       \tag{E.10}
\]

It therefore cannot escape in finite time and is global. This is finite-dimensional existence only.

On any primal ball B, for a differentiable raw path write `s(t)=||dot Theta(t)||raw`. Successive forward differentiation gives

\[
 \frac{\|\dot z^{(1)}\|_2}{\sqrt n}\le s,\quad\frac{\|\dot h^{(1)}\|_2}{\sqrt n}\le2s,
 \quad\frac{\|\dot z^{(2)}\|_2}{\sqrt n}\le4Bs,\quad\frac{\|\dot h^{(2)}\|_2}{\sqrt n}\le8Bs,
\]
\[
 \frac{\|\dot z^{(3)}\|_2}{\sqrt n}\le12B^2s,\qquad
 \frac{\|\dot h^{(3)}\|_2}{\sqrt n}\le24B^2s.                        \tag{E.11}
\]

These inequalities hold almost everywhere also for linearly interpolated raw GD, with hidden fields recomputed from the interpolated parameters from the interpolated weights. Equations (E.9)-(E.11), together with initialized second-moment bounds, uniformly bound the average squared H1([0,T]) norm of the joint same-layer neuron paths \((z_{1,j}^{(\ell)},h_{1,j}^{(\ell)},z_{2,j}^{(\ell)},h_{2,j}^{(\ell)})\), \(j=1,\ldots,n\), for each \(\ell=1,2,3\).

Closed bounded H1 balls on a finite one-dimensional time interval have compact images in C([0,T]); this follows directly from the pointwise bound and the modulus `|x(t)-x(s)|<=sqrt(|t-s|)||x'||_L2`, and a diagonal subsequence on rational time points: the common modulus
upgrades convergence on that dense set to uniform convergence. The weak
lower-semicontinuity of the \(H^1\) norm keeps the limit inside the same ball. Markov's inequality for the empirical average H1 norm therefore gives tightness of the empirical path measures on \(C([0,T];\mathbb R^4)\) in
probability: on the same high-probability events, for every \(\varepsilon>0\)
a common compact set carries at least \(1-\varepsilon\) of each empirical
measure.

This is not W2 compactness: a bounded mean squared H1 norm does not by itself make squared path norms uniformly integrable. It does not identify a deterministic subsequential law, kernels, adjoints, or velocity laws.

### E.6. Strong endpoints on specified population action spaces

For this statement, suppose probability spaces \((\Omega_\ell,\mathcal A_\ell,
\mathbb P_\ell)\), \(\ell=1,2,3\), with separable real
\(\mathcal H_\ell=L^2(\Omega_\ell)\), and bounded initial operators
\(W_0^{(2)}:\mathcal H_1\to\mathcal H_2\),
\(W_0^{(3)}:\mathcal H_2\to\mathcal H_3\), are already specified.
They and their adjoints are fixed throughout. This conditional analytic result
does not construct Gaussian action spaces or identify them from finite width.
The complete affine raw state space is
\[
 \mathfrak X=L^2(\Omega_1;\mathbb R^d)\times
 HS(\mathcal H_1,\mathcal H_2)\times
 HS(\mathcal H_2,\mathcal H_3)\times\mathcal H_3,
\]
with state \(\Theta=(W^{(1)},M^{(2)},M^{(3)},W^{(4)})\),
\(W^{(\ell)}=W_0^{(\ell)}+M^{(\ell)}\) for \(\ell=2,3\), and product norm
using \(\mathbb E_1\|dW^{(1)}\|_{\mathbb R^d}^2\), the two squared HS norms,
and \(\mathbb E_3|dW^{(4)}|^2\). Population fields are
\[
 Z_a^{(1)}=W^{(1)}x_a/\sqrt d,\quad
 Z_a^{(\ell)}=W^{(\ell)}H_a^{(\ell-1)},\quad H_a^{(\ell)}=\Phi(Z_a^{(\ell)}),
 \quad f_a=\mathbb E_3[W^{(4)}H_a^{(3)}],
\]
\[
 \Delta_a^{(3)}=W^{(4)}\Phi'(Z_a^{(3)}),\quad
 Q_a^{(\ell)}=(W^{(\ell+1)})^*\Delta_a^{(\ell+1)},\quad
 \Delta_a^{(\ell)}=\Phi'(Z_a^{(\ell)})Q_a^{(\ell)}
 \quad(\ell=1,2).
\]
Products of fields are pointwise within the indicated layer. The physical
field is the negative raw gradient of \(\mathcal L=(r_1^2+r_2^2)/2\):
\[
 \dot W^{(1)}=-\sum_ar_a\Delta_a^{(1)}x_a^T/\sqrt d,\quad
 \dot M^{(\ell)}=-\sum_ar_a\Delta_a^{(\ell)}\otimes H_a^{(\ell-1)},\quad
 \dot W^{(4)}=-\sum_ar_aH_a^{(3)}.
\]
Here \((U\otimes H)g=U\mathbb E_{\ell-1}[Hg]\). Its HS norm is
\(\|U\|_{L^2(\Omega_\ell)}\|H\|_{L^2(\Omega_{\ell-1})}\).
The theorem permits any initial state in this affine space. In particular it
applies to an existing canonical strong flow with Gaussian first mark and zero
limiting readout, if its action spaces have been constructed; it does not replace
the finite tiny Gaussian readout by zero in a convergence theorem.

**Continuity and the scalar chain rule.** The fields just displayed and their
raw vector field are continuous in the raw norm and are polynomially bounded
on every bounded raw set. Forward continuity follows from the global
Lipschitz bound for \(\Phi\), operator continuity, and
\(\|M\|_{op}\le\|M\|_{HS}\). For the only nontrivial backward step,
if \((Z_j,Q_j)\to(Z,Q)\) in \(L^2\times L^2\),
\[
 \|\Phi'(Z_j)Q_j-\Phi'(Z)Q\|_{L^2}
 \le2\|Q_j-Q\|_{L^2}
   +\|[\Phi'(Z_j)-\Phi'(Z)]Q\|_{L^2}\longrightarrow0.       \tag{E.12}
\]
The second term converges by convergence in measure, continuity and boundedness
of \(\Phi'\), and integrability of \(16Q^2\): every subsequence admits an
a.e. convergent subsubsequence to which dominated convergence applies. Backward
induction and continuity of rank-one maps into HS prove the assertion.

The scalar prediction is continuously Fréchet differentiable with the displayed
backpropagation formula even though the full activation map need not be
Fréchet differentiable \(L^2\to L^2\). For fixed \(Q\in L^2\), Taylor's formula
and the two derivative bounds give
\[
 |\Phi(Z+U)-\Phi(Z)-\Phi'(Z)U|\le\min(|U|^2,4|U|).
\]
Pair the remainder with \(Q\). On \(|Q|\le K\) its integral is at most
\(K\|U\|_{L^2}^2\), and on the complement it is at most
\(4\|Q\mathbf1_{|Q|>K}\|_{L^2}\|U\|_{L^2}\). Divide by \(\|U\|_{L^2}\),
first send \(U\to0\) with \(K\) fixed, then send \(K\to\infty\).
To telescope layers explicitly, replace the top activation increment by its
linear term paired with the fixed current readout; pass the fixed linear term
through \((W^{(3)})^*\), repeat at layer two, then at layer one.
Each preactivation increment is \(O(\|d\Theta\|_{raw})\). Terms involving a
perturbed operator times a perturbed field are \(O(\|d\Theta\|_{raw}^2)\),
as is the perturbed-readout/perturbed-feature pairing. This accounts for every
remainder and gives the stated derivative; (E.12) makes it continuous.
The scalar loss is therefore \(C^1\) with gradient \(-V\).

**Strong endpoint theorem.** Let \(\Theta\) be an already existing strong
physical solution \(\dot\Theta=V(\Theta)\) on \([0,T_*)\), \(T_*<\infty\),
in the stated complete affine Hilbert space. Here a strong solution is a
norm-continuous, locally absolutely continuous path satisfying the equation
a.e.; continuity of \(V\) then makes it \(C^1\). The scalar chain rule gives
\[
 \mathcal L(\Theta(t))+\int_0^t\|V(\Theta(u))\|_{raw}^2du
 =\mathcal L(\Theta(0)).
\]
Thus for \(s<t<T_*\),
\[
 \|\Theta(t)-\Theta(s)\|_{raw}
 \le\sqrt{(t-s)[\mathcal L(\Theta(s))-\mathcal L(\Theta(t))]}.
                                                               \tag{E.13}
\]
The nonnegative decreasing loss has a limit; this inequality makes the path
Cauchy at \(T_*\). Completeness gives \(\Theta_*\in\mathfrak X\).
Continuity of \(V\) and of all field maps proves
\[
 \Theta(t)\to\Theta_*\text{ in raw norm},\qquad
 V(\Theta(t))\to V(\Theta_*)\text{ in raw norm}.                 \tag{E.14}
\]
Every \(Z,H,Q,\Delta\) converges strongly in its indicated \(L^2\) space.
For any converging probe \(g_t\to g_*\) in the domain of an action,
\[
 \|W(t)g_t-W_*g_*\|\le\|W(t)\|_{op}\|g_t-g_*\|
                  +\|M(t)-M_*\|_{HS}\|g_*\|\to0,
\]
and the identical inequality for adjoints gives both orientations. Integrating
the convergent velocity proves that the extension at \(T_*\) is differentiable
from the left with derivative \(V(\Theta_*)\).

Each extended incoming-field path has compact image in \(L^2\). Hence, for
every one of the finitely many sample/layer incoming fields,
\[
 \lim_{R\to\infty}\sup_{0\le t\le T_*}
 \|Q(t)\mathbf1_{|Q(t)|>R}\|_{L^2}=0.                         \tag{E.15}
\]
Indeed cover the compact image by finitely many balls of radius \(\varepsilon\)
centered at fields \(F\). The inequality
\(\|Q\mathbf1_{|Q|>R}\|_{L^2}
 \le2\|Q-F\|_{L^2}+2\|F\mathbf1_{|F|>R/2}\|_{L^2}\)
follows by splitting at \(|F|>R/2\). Send \(R\to\infty\) for the finitely
many centers and then \(\varepsilon\to0\). This is a qualitative tail bound
for this one existing path, with no uniform rate over widths or restarts.

### E.7. Exact limitation of the endpoint theorem

Bounded positive slope does not make the ambient backward multiplication map
locally Lipschitz. On a standard Gaussian probability space take \(Z=Q=G\)
and \(\mathcal B(Z,Q)=\Phi'(Z)Q\). Choose disjoint fixed-length intervals
\(I_j\) tending to positive infinity, inside regions where \(\sin(2z)\ge3/4\).
A fixed sufficiently small \(u>0\) keeps every segment \([z,z+u]\),
\(z\in I_j\), inside a region where \(\sin(2z)\ge1/2\).
Set \(E_j=\{G\in I_j\}\) and \(Z_j=G+u\mathbf1_{E_j}\). The mean-value theorem
and \(\Phi''=-4b\sin(2z)\) give
\[
 \|\mathcal B(Z_j,G)-\mathcal B(G,G)\|_{L^2}
 \ge2b(\inf I_j)u\mathbb P(E_j)^{1/2},\qquad
 \|Z_j-G\|_{L^2}=u\mathbb P(E_j)^{1/2}\to0.
\]
Their ratio diverges. This is an ambient continuity-versus-Lipschitz example;
it makes no claim that the perturbations are generated network trajectories.

The endpoint theorem establishes neither local existence nor uniqueness from
\(\Theta_*\) in the infinite-dimensional space. A continuation and finite-width
identification theorem still needs a quantitative response/tail estimate at
reached states with the same retained Gaussian histories. Neither (E.15), the
finite GD energy inequality, nor weak path-law tightness supplies that estimate.
