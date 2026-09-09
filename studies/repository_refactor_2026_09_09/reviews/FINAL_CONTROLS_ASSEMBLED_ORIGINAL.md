# Additional finite controls and Gaussian comparison results

The fragments below are organized by destination. Equation labels have a local
letter prefix. They retain finite Euclidean and Frobenius norms with explicit
RMS factors; population spaces and norms are declared separately. Cross-fragment
references use these prefixes. Each convergence statement specifies its clock
and observable.

## Destination: finite_optimization_and_controls — S. Squared-logarithmic response

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
finite-width feature flow, and let \(E:\mathbb R^m\to\mathbb R^{N_h+n}\)
be any isometric linear embedding, \(E^TE=I_m\). If (S.1) holds throughout
\([s_0,s]\), then, for the \(m\) positive singular values of \(U(s,s_0)E\),

\[
\sum_{j=1}^m\bigl(\log\sigma_j(U(s,s_0)E)\bigr)^2
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



## Destination: finite_optimization_and_controls — I. Initial Gaussian middle curvature

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


## Destination: finite_optimization_and_controls — C. Positive middle curvature at small feature times

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


## Destination: finite_optimization_and_controls — E. Moderate-sine physical controls

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
      -h\|V\|_{raw}^2+	frac12(11000\sqrt n B^9)h^{(2)}\|V\|_{raw}^2
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


## Destination: finite_optimization_and_controls — Q1. Integrated initial-matrix queries

This fragment records the exact finite arctangent equations needed to define the
filtered comparison. The datum, loss and raw metric are those of fragment S;
all derivatives here use feature time. It also proves the deterministic
compression and states the derivative information it does not provide.

### 1. Finite setup and exact integral equations

Fix a positive integer width \(n\). Each
\(z^{(\ell)},h^{(\ell)},\delta^{(\ell)}\), for \(\ell=1,2,3\),
and the stored readout \(W^{(4)}\) is a real column vector of
length \(n\); \(W^{(2)},W^{(3)}\) are real \(n\)-by-\(n\)
matrices. A superscript \(T\) denotes the ordinary matrix transpose.
The activation is \(\phi(z)=\arctan z\), applied coordinatewise,
and \(\odot\) denotes coordinatewise multiplication. Define
\[
h^{(\ell)}=\phi(z^{(\ell)}),\qquad
z^{(2)}=W^{(2)}h^{(1)},\qquad z^{(3)}=W^{(3)}h^{(2)},
\]
\[
\delta^{(3)}=W^{(4)}\odot\phi'(z^{(3)}),\qquad
q^{(2)}=(W^{(3)})^T\delta^{(3)},\qquad
\delta^{(2)}=\phi'(z^{(2)})\odot q^{(2)},
\]
\[
\delta^{(1)}=\phi'(z^{(1)})\odot(W^{(2)})^T\delta^{(2)}.
\]
The canonical initialization has independent entries
\(z^{(1)}_{0,i}\sim N(0,1)\),
\(W^{(2)}_{0,ij},W^{(3)}_{0,ij}\sim N(0,1/n)\), and
\(W^{(4)}_{0,i}\sim N(0,n^{-2})\), with all blocks independent.
Every identity below also holds deterministically for any initial
values for which the indicated finite flow exists.

A prime denotes differentiation in feature time \(s\). The uncut
finite feature-time equations are
\[
(z^{(1)})'=\delta^{(1)},\qquad
(W^{(2)})'=\frac{\delta^{(2)}(h^{(1)})^T}{n},\qquad
(W^{(3)})'=\frac{\delta^{(3)}(h^{(2)})^T}{n},\qquad
(W^{(4)})'=h^{(3)}.
\]
This is the feature clock associated with the canonical physical
equations through \(ds/dt=-2(f_n-1)\); no clock convergence is
asserted here. Set
\(F(z)=z+z^3/3\) and \(x^{(1)}=F(z^{(1)})\), coordinatewise.
Since \(F'(z)=1/\phi'(z)\), the transformed first equation is
\((x^{(1)})'=(W^{(2)})^T\delta^{(2)}\).
Introduce the layer-two primitive
\[
a^{(2)}(s)=\int_0^s\delta^{(2)}(u)\,du.
\]
Write the trained increments as
\[
M^{(2)}(s)=\int_0^s
 \frac{(a^{(2)})'(u)(h^{(1)}(u))^T}{n}\,du,\qquad
M^{(3)}(s)=\int_0^s
 \frac{\delta^{(3)}(u)(h^{(2)}(u))^T}{n}\,du.
\tag{Q1.1}
\]
Thus \(W^{(\ell)}(s)=W^{(\ell)}_0+M^{(\ell)}(s)\), for
\(\ell=2,3\). All histories in (Q1.1) are retained exactly. Integrating
the first feature-time equation and interchanging the triangular
integrals gives
\[
\begin{split}
x^{(1)}(s)={}&x^{(1)}_0+(W^{(2)}_0)^T a^{(2)}(s)+R^{(1)}(s),\\
R^{(1)}(s)={}&\int_0^s h^{(1)}(u)
 \frac{((a^{(2)})'(u))^T[a^{(2)}(s)-a^{(2)}(u)]}{n}\,du.
\end{split}                                                    \tag{Q1.2}
\]
Indeed,
\[
\int_0^s (M^{(2)}(v))^T\delta^{(2)}(v)\,dv
=\int_0^s h^{(1)}(u)
  \frac{(\delta^{(2)}(u))^T\int_u^s\delta^{(2)}(v)dv}{n}\,du.
\]
The remaining exact equations are
\[
z^{(1)}=F^{-1}(x^{(1)}),\qquad h^{(1)}=\phi(z^{(1)}),
\]
\[
z^{(2)}(s)=W^{(2)}_0h^{(1)}(s)
 +\int_0^s (a^{(2)})'(u)
       \frac{(h^{(1)}(u))^T h^{(1)}(s)}{n}\,du,
\qquad h^{(2)}=\phi(z^{(2)}),                                \tag{Q1.3}
\]
\[
z^{(3)}(s)=W^{(3)}_0h^{(2)}(s)
 +\int_0^s\delta^{(3)}(u)
       \frac{(h^{(2)}(u))^T h^{(2)}(s)}{n}\,du,
\qquad h^{(3)}=\phi(z^{(3)}),                                \tag{Q1.4}
\]
\[
W^{(4)}(s)=W^{(4)}_0+\int_0^s h^{(3)}(u)du,
\qquad \delta^{(3)}=W^{(4)}\odot\phi'(z^{(3)}),              \tag{Q1.5}
\]
\[
q^{(2)}(s)=(W^{(3)}_0)^T\delta^{(3)}(s)
 +\int_0^s h^{(2)}(u)
       \frac{(\delta^{(3)}(u))^T\delta^{(3)}(s)}{n}\,du,
\qquad
(a^{(2)})'=\phi'(z^{(2)})\odot q^{(2)}.                    \tag{Q1.6}
\]
The output is exactly
\(f_n(s)=(W^{(4)}(s))^T h^{(3)}(s)/n\).
Only the following four paths are arguments of an initial-matrix
action in (Q1.1)--(Q1.6):
\[
\begin{array}{c|c}
\text{action}&\text{argument}\\ \hline
W^{(2)}_0&h^{(1)}\\
(W^{(2)}_0)^T&a^{(2)}\\
W^{(3)}_0&h^{(2)}\\
(W^{(3)}_0)^T&\delta^{(3)}.
\end{array}                                                    \tag{Q1.7}
\]
In particular, the rough lower backward argument \(\delta^{(2)}\)
has disappeared from the initial-matrix actions in these integral
state equations. It has not disappeared from the nonlinear equation
that generates \(a^{(2)}\).

### 2. What time regularity proves

On \(0\le s\le S\), impose the primal bounds
\(\|W^{(2)}(s)\|_{\rm op},\|W^{(3)}(s)\|_{\rm op},
\|W^{(4)}(s)\|_\infty\le B_S\), with \(B_S\) independent of
\(n\). These are the established actual-trajectory bounds on the
corresponding primal event. All four paths in (Q1.7) then have derivative
Euclidean norm divided by \(\sqrt n\) bounded by a constant \(C_S\)
independent of \(n\). For the new path, boundedness of \(\phi'\)
gives \(\|\delta^{(2)}\|_2/\sqrt n\le B_S^2\), so, for
\(0\le t\le s\le S\),
\[
\frac{\|a^{(2)}(s)-a^{(2)}(t)\|_2}{\sqrt n}
\le\int_t^s\frac{\|\delta^{(2)}(u)\|_2}{\sqrt n}\,du
\le C_S|s-t|.
\tag{Q1.8}
\]
The other three derivative bounds were established in
fragment Q2. Constants are uniform in width on
the stated primal event. These are statements about actual unperturbed
trajectories; they are not assumed for a perturbed comparison process.

Let \(\pi(s)\) be the last mesh point at or before \(s\), for a
deterministic mesh of spacing at most \(\varepsilon/C_S\). Each of
the four query paths changes by Euclidean norm at most
\(\sqrt n\varepsilon\) between \(\pi(s)\) and \(s\). In particular,
\[
\begin{split}
\sup_{s\le S}
 \frac{\|W^{(2)}_0[h^{(1)}(s)-h^{(1)}(\pi(s))]\|_2}{\sqrt n}
 &\le\|W^{(2)}_0\|_{\rm op}\varepsilon,\\
\sup_{s\le S}
 \frac{\|(W^{(2)}_0)^T[a^{(2)}(s)-a^{(2)}(\pi(s))]\|_2}{\sqrt n}
 &\le\|W^{(2)}_0\|_{\rm op}\varepsilon.
\end{split}                                                    \tag{Q1.9}
\]
The two corresponding bounds for \(W^{(3)}_0h^{(2)}\) and
\((W^{(3)}_0)^T\delta^{(3)}\) have right-hand side
\(\|W^{(3)}_0\|_{\rm op}\varepsilon\).
Consequently a specified actual path admits a time net of
\(1+\lceil C_SS/\varepsilon\rceil\) matrix arguments per
orientation, independently of width. This is an approximation of
matrix responses along a supplied trajectory.

The rank memories in (Q1.1)--(Q1.2) do not hide an extra continuity failure
on this uniformly Lipschitz path class. For example, compare two
paths with their corresponding tilded memories. Suppose both paths
obey
\[
\frac{\|h^{(1)}(s)\|_2}{\sqrt n}\le B_h,\qquad
\frac{\|(h^{(1)})'(s)\|_2}{\sqrt n}\le L_h,\qquad
\frac{\|(a^{(2)})'(s)\|_2}{\sqrt n}\le L_a,
\]
and the same bounds hold for the tilded quantities. Define the two
scalar errors
\[
e_a=\sup_{s\le S}
 \frac{\|a^{(2)}(s)-\widetilde a^{(2)}(s)\|_2}{\sqrt n},\qquad
e_h=\sup_{s\le S}
 \frac{\|h^{(1)}(s)-\widetilde h^{(1)}(s)\|_2}{\sqrt n}.
\]
With both primitives zero initially, integration by parts gives
\[
\begin{split}
M^{(2)}(s)-\widetilde M^{(2)}(s)
={}&\frac{[a^{(2)}(s)-\widetilde a^{(2)}(s)](h^{(1)}(s))^T}{n}\\
 &-\int_0^s
  \frac{[a^{(2)}-\widetilde a^{(2)}]((h^{(1)})')^T}{n}\,du\\
 &+\int_0^s
  \frac{(\widetilde a^{(2)})'[h^{(1)}-\widetilde h^{(1)}]^T}{n}\,du,
\end{split}
\]
where all integrand factors are evaluated at \(u\). Hence
\[
\sup_s\|M^{(2)}-\widetilde M^{(2)}\|_{\rm op}
\le(B_h+SL_h)e_a+SL_ae_h.                                   \tag{Q1.10}
\]
Similarly, since
\(R^{(1)}(s)=\int_0^s(M^{(2)}(u))^T(a^{(2)})'(u)du\),
\[
\sup_{s\le S}\frac{\|R^{(1)}(s)-\widetilde R^{(1)}(s)\|_2}{\sqrt n}
\le SL_a\sup_s\|M^{(2)}-\widetilde M^{(2)}\|_{
\rm op}+2SL_aB_h e_a.                                      \tag{Q1.11}
\]
For (Q1.11), integrate
\(\int_0^s(\widetilde M^{(2)})^T
 [(a^{(2)})'-(\widetilde a^{(2)})']du\) by parts, using
\(\|\widetilde M^{(2)}\|_{\rm op}\le SL_aB_h\) and
\(\|(\widetilde M^{(2)})'\|_{\rm op}\le L_aB_h\).
For completeness, if both top-layer paths satisfy
\(\|h^{(2)}\|_2/\sqrt n\le B_2\) and
\(\|\delta^{(3)}\|_2/\sqrt n\le D_3\), then the ordinary
integral for \(M^{(3)}\) gives
\[
\begin{split}
\sup_{s\le S}\|M^{(3)}(s)-\widetilde M^{(3)}(s)\|_{\rm op}
\le{}&SB_2\sup_{s\le S}
 \frac{\|\delta^{(3)}(s)-\widetilde\delta^{(3)}(s)\|_2}{\sqrt n}\\
 &+SD_3\sup_{s\le S}
 \frac{\|h^{(2)}(s)-\widetilde h^{(2)}(s)\|_2}{\sqrt n}.
\end{split}
\]

Thus (Q1.9) yields small equation residuals after replacing only the
initial-matrix responses along the actual trajectory. The exact
rank-update memory has not been dropped to obtain this statement.

### 3. Why this does not yet construct a finite-query approximation

At time \(s_k\), the value of an actual query such as \(a^{(2)}(s_k)\)
has been generated by the dynamics on the entire preceding interval.
Those dynamics used the initial matrices at unrecorded intermediate
arguments. Observing the actual query is causal in physical time,
but it is not thereby measurable from only the retained finite-query
transcript. Gaussian conditioning on the latter transcript cannot
treat that query as a legal next query without proving this
measurability. Sampling a true trajectory does not supply such a proof.

A finite-call algorithm can instead evolve its own state using frozen
or interpolated matrix responses and make new calls on its own
queries. That is an admissible proposed approximation. Equation (Q1.9)
on the true path proves consistency of the substitution, not closeness
between this algorithm and the true dynamics. In particular it does
not establish the rank premise for the actual perturbed histories in
fragment Q4; query perturbations may generate
new directions in subsequent nonlinear queries.

The uniform temporal bounds also do not by themselves give strong
compactness in a fixed infinite-dimensional Hilbert space. For example,
in \(\ell^2(\mathbb N)\), the paths \(s\mapsto s e_j\), where
\(e_j\) is the \(j\)-th standard unit vector, are uniformly bounded
and Lipschitz on \([0,S]\), but their values at any positive time
have no norm-convergent subsequence. This observation is not a claim
that such a family occurs in the canonical network, nor a construction
of a population space for it.

### 4. The retained stability term and derivative observables

For two state paths, the exact primitive difference obeys
\[
\begin{split}
a^{(2)}(s)-\widetilde a^{(2)}(s)=\int_0^s\bigl\{
 &\phi'(z^{(2)})\odot(q^{(2)}-\widetilde q^{(2)})\\
 &+[\phi'(z^{(2)})-\phi'(\widetilde z^{(2)})]
       \odot\widetilde q^{(2)}\bigr\}\,du.
\end{split}                                                    \tag{Q1.12}
\]
All factors inside the integral are evaluated at \(u\).
The first integrand has Euclidean norm divided by \(\sqrt n\)
at most \(\|q^{(2)}-\widetilde q^{(2)}\|_2/\sqrt n\).
In the second integrand, the available bound on
\(\|\widetilde q^{(2)}\|_2/\sqrt n\) does not provide a
width-uniform Lipschitz bound in
\(\|z^{(2)}-\widetilde z^{(2)}\|_2/\sqrt n\).
For \(Q>0\) the exact tail split gives
\[
\begin{split}
&\frac{\|[\phi'(z^{(2)})-\phi'(\widetilde z^{(2)})]
       \odot\widetilde q^{(2)}\|_2}{\sqrt n}\\
&\quad\le\|\phi''\|_\infty Q
  \frac{\|z^{(2)}-\widetilde z^{(2)}\|_2}{\sqrt n}
 +2\frac{\|\widetilde q^{(2)}\odot
   \mathbf1_{\{|\widetilde q^{(2)}|>Q\}}\|_2}{\sqrt n}.
\end{split}                                                    \tag{Q1.13}
\]
The total L2 bound alone neither makes the last term uniformly small
over the approximation family nor supplies the tail-versus-stability
rate needed to pass \(Q\to\infty\). Integrating the initial query
therefore retains the actual middle multiplier; it does not resolve
the continuation problem represented by that multiplier.

There is also a separate observable issue. The lower backward result
is
\[
(W^{(2)}(s))^T\delta^{(2)}(s)
=\frac{d}{ds}\big[(W^{(2)}_0)^T a^{(2)}(s)\big]
 +(M^{(2)}(s))^T(a^{(2)})'(s),                             \tag{Q1.14}
\]
and \(\delta^{(1)}=\phi'(z^{(1)})\odot
(W^{(2)})^T\delta^{(2)}\). Uniform approximation of the integrated
response in (Q1.9) does not imply strong convergence of its derivative.
For example, \(j^{-1}\sin(js)v\) tends uniformly to zero with
uniformly bounded derivative, while its derivatives do not tend to
zero in time L2 for a nonzero fixed \(v\). This is a limitation of
the inference, not a canonical counterexample. Hidden velocities and
the raw first kernel block require additional derivative or energy
control even if uniform state convergence were separately proved.



## Destination: gaussian_calculus — Q2. Euler perturbations and slow-history compression


Consider the following completely specified triangular Gaussian perturbations,
with no mixture or complex parameter.

**Exact frozen-history lemma.** Let \(n,m,K\) be positive integers,
\(\eta,\sigma>0\), and \(T=K\eta\). Fix deterministic columns
\(\theta_l\in\mathbb R^n,\omega_l\in\mathbb R^m\) for
\(1\le l\le K\), and let \(\Gamma\in\mathbb R^{K\times K}\)
have independent standard real Gaussian entries. Put
\(\Theta=[\theta_1,\ldots,\theta_K]\),
\(\Omega=[\omega_1,\ldots,\omega_K]\), and take upper Cholesky
factors with positive diagonal:
\[
A_\theta^TA_\theta=\Theta^T\Theta+\sigma^2I,\qquad
A_\omega^TA_\omega=\Omega^T\Omega/m+\sigma^2I.
\]
Set \(t_i=(\Theta A_\theta^{-1})_i\) and
\(s_i=(\Omega A_\omega^{-1})_i/\sqrt m\), for column index \(i\).
Define the two triangular covariance-matching terms by
\[
g_l=\frac1{\sqrt m}\sum_{i\le l}t_i(\Gamma A_\omega)_{il},\qquad
k_l=\frac1{\sqrt m}\sum_{i<l}s_i(\Gamma^TA_\theta)_{il},
\]
where \(k_l\) is the perturbation of \(p_l/\sqrt m\).

Then the following identities and estimates hold. They evaluate the added
forcing, not the difference between two adaptive solutions.
\[
\mathbb E\left\|\eta\sum_{l=1}^K g_l\right\|^2
=\frac{\eta^2}{m}\sum_{i=1}^K\|t_i\|^2
\left[\frac1m\left\|\sum_{l=i}^K\omega_l\right\|^2
+\sigma^2(K-i+1)\right],                                      \tag{Q2.A}
\]
\[
\mathbb E\left\|\eta\sum_{l=1}^K k_l\right\|^2
=\frac{\eta^2}{m}\sum_{i=1}^{K-1}\|s_i\|^2
\left[\left\|\sum_{l=i+1}^K\theta_l\right\|^2
+\sigma^2(K-i)\right].                                       \tag{Q2.B}
\]
**Proof of the identities.** Group each independent \(\Gamma_{ij}\) in (Q2.A):
its coefficient is \(\eta t_i\sum_{l\ge i}(A_\omega)_{jl}/\sqrt m\).
Summing over \(j\) produces the suffix quadratic form of
\(A_\omega^TA_\omega\). For (Q2.B), the coefficient of
\(\Gamma_{ji}\) is
\(\eta s_i\sum_{l>i}(A_\theta)_{jl}/\sqrt m\), giving the
strict suffix and (Q2.B). Cross terms between distinct Gaussian entries
have zero expectation. The strict inequality in (Q2.B) is essential.

For repeated queries \(\theta_l=\theta,\omega_l=\omega\), put
\(a=\|\theta\|>0,b=\|\omega\|/\sqrt m>0\). The regularized upper
Cholesky factor of \(a^2\mathbf1\mathbf1^T+\sigma^2I\) satisfies
\[
(A_a)_{ii}=\sigma\sqrt{\frac{\sigma^2+ia^2}{\sigma^2+(i-1)a^2}},
\quad
(A_a)_{ij}=\frac{a^2\sigma}
 {\sqrt{(\sigma^2+(i-1)a^2)(\sigma^2+ia^2)}}\quad(i<j).
\]
Consequently \(t_i=\theta d_i(a)\), where
\[
d_i(a)=\frac{\sigma}
 {\sqrt{(\sigma^2+(i-1)a^2)(\sigma^2+ia^2)}},\qquad
\sum_{i=1}^l d_i(a)^2=\frac{l}{\sigma^2+la^2}.
\]
Substitution gives
\[
\mathbb E\left\|\eta\sum_lg_l\right\|^2
=\frac{a^2\eta^2}{m}\sum_{i=1}^Kd_i(a)^2
 [b^2(K-i+1)^2+\sigma^2(K-i+1)]
\le\frac{b^2T^2+\sigma^2T\eta}{m}.                            \tag{Q2.C}
\]
The analogous bound for \(\eta\sum_lk_l\) is
\((a^2T^2+\sigma^2T\eta)/m\), using \(i<K\) and \(K-i\).
In the fixed-\(K\), \(\sigma\downarrow0\) limit,
\(g_l\to(\theta/a)(b/\sqrt m)\Gamma_{11}\) for every \(l\),
whereas \(k_1=0\) and
\(k_l\to(\omega/(b\sqrt m))(a/\sqrt m)\Gamma_{11}\) for \(l\ge2\).
The forcing is coherent in time: Euler integration yields \(T/\sqrt m\),
not a \(\sqrt K\) growth. Inequality (Q2.C) is already uniform in both
\(K\) and \(\sigma\), so this conclusion does not exchange limits.

More generally, with \(\|\omega_l\|/\sqrt m\le B\), (Q2.A) is bounded by
\[
\frac{T^2B^2+\sigma^2T\eta}{m}\,
r_{\rm eff}(\Theta,\sigma),\qquad
r_{\rm eff}=\operatorname{tr}\!\left[
\Theta^T\Theta(\Theta^T\Theta+\sigma^2I)^{-1}\right].           \tag{Q2.D}
\]
A deterministic finite-rank path has bounded effective rank, including
an affine slowly changing history. This follows because
\(\sum_i\|t_i\|^2=r_{\rm eff}\), by cyclicity of the trace and
\(A_\theta^{-1}A_\theta^{-T}=(\Theta^T\Theta+\sigma^2I)^{-1}\).
The reverse orientation has the analogous estimate with
\(r_{\rm eff}(\Omega/\sqrt m,\sigma)\) and
\(A=\max_l\|\theta_l\|\).

These estimates also give convergence in the supremum norm of the
integrated path, not merely convergence at its last time. Specifically,
\[
\mathbb E\max_{1\le j\le K}
 \left\|\eta\sum_{l=1}^j g_l\right\|^2
\le \frac{T^2(B^2+\sigma^2)}m\,r_{\rm eff}(\Theta,\sigma),      \tag{Q2.E}
\]
and the reverse orientation has bound
\(T^2(A^2+\sigma^2)r_{\rm eff}(\Omega/\sqrt m,\sigma)/m\).
Indeed, pathwise Cauchy–Schwarz bounds the maximum by
\(T\eta\sum_l\|g_l\|^2\), while Gaussian isometry gives
\(\mathbb E\|g_l\|^2=(\|\omega_l\|^2/m+\sigma^2)
 \sum_{i\le l}\|t_i\|^2/m\).

The unintegrated frozen queries also admit a uniform maximum bound:
\[
\mathbb E\max_{1\le l\le K}\|g_l\|^2
\le\frac{4(B^2+\sigma^2)}m\,
 r_{\rm eff}(\Theta,\sigma)\log(2K),                           \tag{Q2.F}
\]
with the analogous reverse-orientation estimate. To verify this without
any independence between times, let \(Z_l\) be centered Gaussian
vectors with \(\mathbb E\|Z_l\|^2\le v^2\). For \(v>0\), the
covariance eigenvalues \(\lambda_j\) are at most \(v^2\), and
\[
\log\mathbb E e^{\|Z_l\|^2/(4v^2)}
=-\tfrac12\sum_j\log(1-\lambda_j/(2v^2))\le\tfrac12.
\]
Here \(-\log(1-x)\le2x\) for \(0\le x\le1/2\) was used.
Jensen's inequality and \(\max_l e^{x_l}\le\sum_l e^{x_l}\)
give \(\mathbb E\max_l\|Z_l\|^2\le4v^2\log(2K)\).
The case \(v=0\) is immediate. Apply this with
\(v^2=(B^2+\sigma^2)r_{\rm eff}/m\), using the per-query identity
above. Thus (Q2.F) also includes arbitrarily correlated frozen query times.

**Slow-history bound, including integer choices.** Assume only the discrete
Lipschitz estimate
\(\|\theta_l-\theta_j\|\le M\eta|l-j|\). Then
\[
r_{\rm eff}\le r+\frac{KM^2T^2}{\sigma^2r^2}\quad(1\le r\le K).
\]
To prove this, partition the indices into the nonempty blocks
\(\lfloor(j-1)K/r\rfloor<l\le\lfloor jK/r\rfloor\),
\(1\le j\le r\), replacing each column by the first column of its
block. Each block spans at most \(\eta(\lceil K/r\rceil-1)\le T/r\)
in physical time. This rank-at-most-\(r\) matrix approximation therefore
has squared Frobenius error at most \(K(MT/r)^2\). The sum of squared
singular values after the first \(r\) is no larger than that error;
the first \(r\) terms of the effective rank are at most one each, and
the rest are at most their squared singular values divided by
\(\sigma^2\). This proves the estimate.

Set \(x=(KM^2T^2/\sigma^2)^{1/3}\) and choose
\(r=\min\{K,\max\{1,\lceil x\rceil\}\}\). If \(x\le K\),
the estimate is at most \(1+2x\); if \(x>K\), use
\(r_{\rm eff}\le K\) directly. Thus
\[
r_{\rm eff}\le\min\{K,1+2(KM^2T^2/\sigma^2)^{1/3}\}.
\]
For \(K=O(m^2)\), uniformly bounded \(M,T\), and
\(\sigma\gg m^{-1/2}\), this proves \(r_{\rm eff}/m\to0\).
Choosing additionally \(\sigma\to0\), for example
\(\sigma=m^{-\beta}\), \(0<\beta<1/2\), removes the added
regularization forcing below. The reverse orientation needs the same
Lipschitz control of \(\omega_l/\sqrt m\).

The additive \(\sigma U/\sqrt m\), \(\sigma V\) terms in the displayed triangular formulas have
Euler-integrated mean-square norms \(\sigma^2(n/m)T\eta\) and
\(\sigma^2T\eta\), respectively, in the same two normalized spaces.
For independent standard Gaussian \(U,V\), their partial sums are
square-integrable vector martingales; the expected squared maximum is at
most four times these quantities by the \(L^2\) maximal inequality.
The same Gaussian maximum argument bounds the expected squared maximum
of their unintegrated query values by
\(4\sigma^2(n/m)\log(2K)\) and \(4\sigma^2\log(2K)\).

Thus, for deterministic histories with uniformly bounded
\(A,B,T,n/m\) and both discrete Lipschitz constants,
\(K\asymp m^2\), and \(\sigma=m^{-1/4}\), each expected squared
supremum of the integrated covariance perturbation is \(O(m^{-1/6})\).
Each additive-noise bound is \(O(m^{-5/2})\). Both orientations of the
full frozen primitive consequently vanish in \(L^2\) of the supremum
norm. This is a consequence of (Q2.E), without a union bound or logarithmic
loss; it is not a statement about the unfrozen dynamics.
Furthermore, (Q2.F) gives expected squared raw-query maxima
\(O(m^{-1/6}\log m)\), and the additive terms contribute
\(O(m^{-1/2}\log m)\). Hence the unintegrated frozen perturbations
also vanish uniformly over the mesh.

The implication is scoped. Simple deterministic histories resolve the
raw Gaussian-matrix-size concern, even with \(K\asymp m^2\).
However, in the actual comparison dynamics the Cholesky factors and
queries depend on \(\Gamma\); conditioning on those histories does not
preserve the independent Gaussian law used in (Q2.A)–(Q2.B) or (Q2.F). The actual
preactivation/backprop perturbations enter nonlinear queries before their
effect reaches an Euler update. An actual causal covariance estimate and
propagation bound are still required. The canonical middle multiplier
\(\operatorname{diag}(\phi''(z)b)\) is one unresolved propagation term;
this calculation does not show it is the only remaining obligation.
Claim 1 is unused. No experiments were performed.

### Which actual network histories satisfy the temporal premise?

This section concerns the canonical finite three-hidden-layer flow in
feature time \(s\), not an extra claim about the perturbed comparison
process. All hidden vectors and the stored readout \(W^{(4)}\) have
length \(n\), and \(W^{(2)},W^{(3)}\) are \(n\) by \(n\). Write
\[
h^{(\ell)}=\phi(z^{(\ell)}),\quad
z^{(2)}=W^{(2)}h^{(1)},\quad z^{(3)}=W^{(3)}h^{(2)},\quad
\delta^{(3)}=W^{(4)}\odot\phi'(z^{(3)}),
\]
\[
q^{(2)}=(W^{(3)})^\top\delta^{(3)},\qquad
\delta^{(2)}=\phi'(z^{(2)})\odot q^{(2)},\qquad
\phi(z)=\arctan z.
\]
Here \(q^{(2)}\) names the repeatedly used ungated backward result.
One can instead use common \(C^1\) clipping
\(\delta^{(2)}=\phi'(z^{(2)})\odot\tau_R(q^{(2)})\), with
\(|\tau_R(a)|\le |a|\), \(|\tau_R(a)|\le2R\), and
\(|\tau_R'(a)|\le1\).
The feature-time equations, with or without this clipping, are
\[
(z^{(1)})'=\phi'(z^{(1)})\odot(W^{(2)})^\top\delta^{(2)},\quad
(W^{(2)})'=\frac{\delta^{(2)}(h^{(1)})^\top}{n},\quad
(W^{(3)})'=\frac{\delta^{(3)}(h^{(2)})^\top}{n},\quad
(W^{(4)})'=h^{(3)}.
\]
Assume on \(0\le s\le S\) that the two matrix operator norms and
\(\|W^{(4)}\|_\infty\) are at most \(B_S\), independently of \(n,R\).
These are the already available primal bounds; the following implication
can also be read simply as a deterministic statement on that event.
Throughout this section \(C_S\) depends only on \(S,B_S\) and arctangent.

Because \(h^{(\ell)},\phi'\), and \(\phi''\) are bounded,
\(\|\delta^{(3)}\|_2/\sqrt n\), \(\|q^{(2)}\|_2/\sqrt n\), and
\(\|\delta^{(2)}\|_2/\sqrt n\) are bounded by \(C_S\).
Differentiating the actual forward equations gives
\[
(h^{(1)})'=\phi'(z^{(1)})^2\odot(W^{(2)})^\top\delta^{(2)},
\]
\[
(z^{(2)})'
=\frac{\|h^{(1)}\|_2^2}{n}\delta^{(2)}
 +W^{(2)}\!\left[
   \phi'(z^{(1)})^2\odot(W^{(2)})^\top\delta^{(2)}
 \right],
\]
\[
(h^{(2)})'=\phi'(z^{(2)})\odot(z^{(2)})',\qquad
(z^{(3)})'=\frac{\|h^{(2)}\|_2^2}{n}\delta^{(3)}
 +W^{(3)}(h^{(2)})',
\]
\[
(\delta^{(3)})'
=h^{(3)}\odot\phi'(z^{(3)})
 +W^{(4)}\odot\phi''(z^{(3)})\odot(z^{(3)})'.
\]
Every derivative displayed has Euclidean norm divided by \(\sqrt n\)
at most \(C_S\). Therefore \(h^{(1)}/\sqrt n\),
\(h^{(2)}/\sqrt n\), and \(\delta^{(3)}/\sqrt n\) have the
uniform time-Lipschitz property used in the frozen-history lemma.

This also yields an exact distinction for the lower backward query:
\[
(q^{(2)})'
=h^{(2)}\frac{\|\delta^{(3)}\|_2^2}{n}
 +(W^{(3)})^\top(\delta^{(3)})',
\]
so \(\|(q^{(2)})'\|_2/\sqrt n\le C_S\). In the uncut flow,
\[
(\delta^{(2)})'
=\phi''(z^{(2)})\odot(z^{(2)})'\odot q^{(2)}
 +\phi'(z^{(2)})\odot(q^{(2)})'.
\]
Cauchy--Schwarz gives
\[
\frac1n\sum_i|(\delta_i^{(2)})'|
\le \|\phi''\|_\infty
 \frac{\|(z^{(2)})'\|_2\|q^{(2)}\|_2}{n}
 +\frac{\|(q^{(2)})'\|_2}{\sqrt n}\le C_S.
\]
It does not supply a uniform Euclidean derivative bound for the product
\((z^{(2)})'\odot q^{(2)}\). For the clipped flow the same product
contains \(\tau_R(q^{(2)})\), and direct differentiation instead gives
\(\|(\delta^{(2)})'\|_2/\sqrt n\le C_S(1+R)\).
Thus all required lower-matrix frozen histories are time-Lipschitz for
fixed \(R\), but this argument is not uniform as \(R\) grows.

The scaling into the comparison lemma is explicit. For the top matrix
use \(m=n\), \(G=\sqrt n\,W_0^{(3)}\),
\(\theta_l=\delta_l^{(3)}/\sqrt n\), and \(\omega_l=h_l^{(2)}\).
Then its initial-matrix responses are
\[
G\omega_l/n=W_0^{(3)}h_l^{(2)}/\sqrt n,\qquad
G^\top\theta_l=(W_0^{(3)})^\top\delta_l^{(3)}.
\]
The lower matrix uses \(G=\sqrt n\,W_0^{(2)}\),
\(\theta_l=\delta_l^{(2)}/\sqrt n\), and \(\omega_l=h_l^{(1)}\).
The trained-matrix corrections remain present in the histories; they
are not being identified with these initialization-only responses.

Freeze an unperturbed flow path and sample the auxiliary \(\Gamma,U,V\)
independently of its initialization. Conditional on that path, the
frozen-history lemma applies. The top-matrix temporal constants just
proved are uniform in \(R\), while the lower-matrix backward constant
above is not. On any fixed primal-bounded event the resulting conditional
estimates have uniform constants. This is a forcing estimate along the
frozen path, not along the solution after adding that forcing.
Nothing here permits conditioning on a \(\Gamma\)-dependent perturbed
trajectory, removing clipping, or concluding unique autonomous restart.


## Destination: gaussian_calculus — Q3. A contained rectangular martingale bound

Let \((Y_k)_{k=0}^J\) be a real \(d_1\)-by-\(d_2\) matrix
martingale, \(Y_0=0\), for a filtration \((\mathcal F_k)\). Write
\(X_k=Y_k-Y_{k-1}\). Suppose almost surely, for deterministic \(c,v\ge0\),
\[
 \|X_k\|_{op}\le c,\qquad
 \sum_{i\le k}\mathbb E_{i-1}X_iX_i^T\preceq vI_{d_1},\qquad
 \sum_{i\le k}\mathbb E_{i-1}X_i^TX_i\preceq vI_{d_2}
 \quad(0\le k\le J).
\]
Here \(\mathbb E_{i-1}\) denotes conditional expectation. Then for \(x>0\),
\[
 \mathbb P\{\max_{k\le J}\|Y_k\|_{op}\ge x\}
 \le(d_1+d_2)\exp\!\left(-\frac{x^2}{2(v+cx/3)}\right).
 \tag{Q3.1}
\]
If the denominator vanishes the probability is zero. This is the finite-horizon
rectangular Freedman inequality. The full proof, including the matrix
trace-concavity step, follows. The statement agrees with
[Tropp, Corollary 1.3](https://tropp.caltech.edu/papers/Tro11-Freedmans-Inequality.pdf).

**Inverse Jensen and logarithms.** For positive definite self-adjoint operators
\(T_i\) on a finite-dimensional Hilbert space and linear maps \(U_i\) satisfying
\(\sum_iU_i^*U_i=I\), the block matrix
\[
 \begin{pmatrix}T_i&I\\I&T_i^{-1}\end{pmatrix}\succeq0
\]
is positive by completing a square. Sandwich by
\(\operatorname{diag}(U_i,U_i)\), sum, and take the Schur complement to obtain
\[
 \left(\sum_iU_i^*T_iU_i\right)^{-1}
 \preceq\sum_iU_i^*T_i^{-1}U_i.
\]
Apply this to \(T_i+tI\) and integrate the scalar spectral identity
\[
 -\log T=\int_0^\infty[(T+tI)^{-1}-(1+t)^{-1}I],dt.
\]
It gives
\[
 -\log\left(\sum_iU_i^*T_iU_i\right)
 \preceq\sum_iU_i^*(-\log T_i)U_i.                 \tag{Q3.2}
\]
All integrals converge in operator norm in finite dimension. The same integral
and the inverse-order implication \(A\preceq B\Rightarrow B^{-1}\preceq A^{-1}\)
prove that the logarithm preserves positive-definite order. Inverse order
itself follows by congruence with \(A^{-1/2}\) and diagonalization.

**Joint convexity of matrix relative entropy.** For positive definite matrices,
put \(D_0(A,B)=\operatorname{tr}[A(\log A-\log B)]\). Given positive weights
\(p_i\) summing to one, set \(A=\sum_ip_iA_i\) and \(B=\sum_ip_iB_i\).
On the Hilbert space of matrices with inner product
\(\langle X,Y\rangle=\operatorname{tr}(X^*Y)\), define
\[
 T_iX=B_iXA_i^{-1},\qquad
 U_iX=\sqrt{p_i}\,XA^{-1/2}A_i^{1/2}.
\]
Left and right multiplication here commute; \(T_i\) is positive definite
and self-adjoint on this Hilbert space. Direct multiplication gives
\[
 \sum_iU_i^*U_i=I,\qquad
 \sum_iU_i^*T_iU_i:X\mapsto BXA^{-1},\qquad
 U_iA^{1/2}=\sqrt{p_i}A_i^{1/2}.
\]
The logarithm of the operator \(X\mapsto BXA^{-1}\) is
\(X\mapsto(\log B)X-X\log A\), as is verified on the rank-one basis formed
from eigenvectors of \(A\) and \(B\). Pairing (Q3.2) with \(A^{1/2}\) therefore
proves
\[
 D_0(A,B)\le\sum_ip_iD_0(A_i,B_i).                \tag{Q3.3}
\]
This contains the full joint-convexity argument needed here.

The modified entropy
\(D(A,B)=D_0(A,B)-\operatorname{tr}A+\operatorname{tr}B\) is nonnegative.
Indeed, diagonalize \(A\) and \(B\) with eigenvalues \(a_i,b_j>0\); the squared
overlaps \(w_{ij}\) of their orthonormal eigenvectors have all row and column
sums one. Then
\[
 D(A,B)=\sum_{i,j}w_{ij}
 [a_i\log(a_i/b_j)-a_i+b_j]\ge0,
\]
by \(u\log u-u+1\ge0\). Equality holds at \(A=B\).
Consequently for each self-adjoint \(H\),
\[
 \operatorname{tr}e^H
 =\max_{X\succ0}\operatorname{tr}(XH-X\log X+X),
\]
with maximizer \(X=e^H\). Replacing \(H\) by \(H+\log A\) expresses
\(\operatorname{tr}\exp(H+\log A)\) as the maximum over \(X\succ0\) of
\(\operatorname{tr}(XH)-D_0(X,A)+\operatorname{tr}X\). This expression is jointly
concave in \((X,A)\) by (Q3.3). To verify concavity after maximizing, take the
maximizers at two arguments and evaluate at their convex combination; joint
concavity supplies the required lower bound. Thus
\[
 A\longmapsto\operatorname{tr}\exp(H+\log A)
 \quad\hbox{is concave on }A\succ0.              \tag{Q3.4}
\]
This entropy-to-trace step follows the variational argument in
[Tropp, Theorem 1 and Lemma 6](https://tropp.caltech.edu/papers/Tro12-Joint-Convexity.pdf);
(Q3.2)–(Q3.3) provide its joint-convexity dependency explicitly.

**Conditional exponential estimate.** First consider self-adjoint increments
\(X_k\) of size \(d\), with \(\|X_k\|_{op}\le c\) and
\(\mathbb E_{k-1}X_k=0\). For \(0<\theta c<3\), put
\(g=\theta^2/[2(1-\theta c/3)]\). The power series and
\(j!\ge2\,3^{j-2}\) for \(j\ge2\) imply, for \(|u|\le c\),
\(e^{\theta u}\le1+\theta u+gu^2\). Spectral calculus and conditional
expectation give, with \(V_k=\mathbb E_{k-1}X_k^2\),
\[
 \log\mathbb E_{k-1}e^{\theta X_k}
 \preceq\log(I+gV_k)\preceq gV_k.                \tag{Q3.5}
\]
The first inequality uses the order preservation of log just proved; the
second uses \(\log(1+u)\le u\) on the eigenvalues of \(gV_k\).
For self-adjoint \(A\preceq B\), the min–max characterization orders every
eigenvalue, so \(\operatorname{tr}e^A\le\operatorname{tr}e^B\).

Set \(W_k=\sum_{i\le k}V_i\). Conditional Jensen using (Q3.4), with the
predictable matrix \(H=\theta Y_{k-1}-gW_k\), gives
\[
 \begin{split}
 \mathbb E_{k-1}\operatorname{tr}e^{\theta Y_k-gW_k}
 &\le\operatorname{tr}\exp\left(H+
              \log\mathbb E_{k-1}e^{\theta X_k}\right)\\
 &\le\operatorname{tr}e^{\theta Y_{k-1}-gW_{k-1}}.
 \end{split}                                                   \tag{Q3.6}
\]
Jensen is legitimate for these bounded positive definite random matrices;
approximate them by simple matrices in their compact spectral range and use
continuity. Hence the displayed nonnegative trace process is a supermartingale
starting at \(d\).

Stop at the first \(k\le J\) with \(\lambda_{max}(Y_k)\ge x\), or at \(J\)
if there is no such time. Conditional induction for this bounded stopping time
bounds its expected trace by \(d\). If \(W_k\preceq vI\), the trace on the
crossing event is at least \(\exp(\theta x-gv)\), because
\(\lambda_{max}(\theta Y_k-gW_k)\ge\theta x-gv\). Thus the crossing probability
is at most \(d\exp(-\theta x+gv)\). For \(v>0\) take
\(\theta=x/(v+cx/3)\), giving \(d\exp[-x^2/(2(v+cx/3))]\).
If \(v=0\), every increment has zero conditional squared norm and is zero
almost surely, so the assertion follows directly. The case \(c=0\) is the
same; otherwise the chosen \(\theta\) lies in the required range.

Finally replace each rectangular increment by its self-adjoint dilation
\[
 \mathscr D(X_k)=\begin{pmatrix}0&X_k\\X_k^T&0\end{pmatrix}.
\]
Its norm is \(\|X_k\|_{op}\), its squared conditional variation has exactly
the two stated rectangular variation blocks, and
\(\lambda_{max}(\mathscr D(Y_k))=\|Y_k\|_{op}\). Taking \(d=d_1+d_2\)
proves (Q3.1) with all dependencies contained.



## Destination: gaussian_calculus — Q4. Adaptive Gram martingale

The hypotheses here permit adaptive query vectors. Fragment Q5 checks them for
each of its two interacting initial matrices and proves the rank premise.

### 1. Causal setup and exact identities

Fix \(n,m,K\ge1\) and \(\sigma>0\). Let \(\Gamma\in
\mathbb R^{K\times K}\) have independent standard Gaussian entries.
Let \(\mathcal H\) contain all other random arrays and seeds, jointly
independent of \(\Gamma\). In the perturbed-original process these
include the original Gaussian matrix and its direct-noise arrays;
revealing their entire arrays initially does not
reveal any entry of \(\Gamma\).

Use finite-valued measurable causal query maps in the order
\(\theta_l\to p_l\to\omega_l\to q_l\). Define
\[
\mathcal F_l=\mathcal H\vee\sigma(\Gamma_{ij}:i,j\le l),\qquad
\mathcal F_{l-1/2}=\mathcal F_{l-1}\vee
 \sigma(\Gamma_{lj}:j<l).
\]
Here \(\theta_l\in\mathbb R^n\) is \(\mathcal F_{l-1}\)-measurable,
\(p_l,\omega_l\in\mathbb R^m\) are
\(\mathcal F_{l-1/2}\)-measurable, and \(q_l\) is
\(\mathcal F_l\)-measurable. The assertions are the causal hypothesis on the queries, satisfied by the
explicit oracle in fragment Q5: its reverse strict-triangular term uses the fresh row
\(\Gamma_{lj},j<l\); its forward triangular term subsequently uses
the fresh column \(\Gamma_{il},i\le l\). The other terms are already
measurable from the queries and \(\mathcal H\).

For each leading history take the positive-diagonal upper Cholesky
factors
\[
A_\theta^TA_\theta=\Theta^T\Theta+\sigma^2I,\qquad
A_\omega^TA_\omega=\Omega^T\Omega/m+\sigma^2I.
\]
The leading blocks of these factors and their inverses agree between
prefixes. Thus the columns
\[
t_i=(\Theta A_\theta^{-1})_i\in\mathbb R^n,\qquad
s_i=(\Omega A_\omega^{-1})_i/\sqrt m\in\mathbb R^m
\]
never change when later queries arrive. In particular \(t_l\) is
known before the fresh row and \(s_l\) before the fresh column.
An arbitrary horizon-dependent Cholesky sign convention is not allowed.

Put
\[
\mathsf T_l=\sum_{i\le l}t_it_i^T\preceq I_n,\qquad
\mathsf S_l=\sum_{i\le l}s_is_i^T\preceq I_m,
\quad \rho_{\theta,l}=\operatorname{tr}\mathsf T_l,
\quad \rho_{\omega,l}=\operatorname{tr}\mathsf S_l.              \tag{Q4.1}
\]
Indeed \(\mathsf T_l=\Theta_l(\Theta_l^T\Theta_l+
\sigma^2I)^{-1}\Theta_l^T\), and the singular-value decomposition
gives eigenvalues \(d_j^2/(d_j^2+\sigma^2)\le1\); the same
calculation applies to \(\Omega_l/\sqrt m\). These traces are the
regularized effective ranks. They increase with the prefix, and
\(\|t_i\|,\|s_i\|\le1\).

Define the rectangular matrices
\[
B_{l-1/2}=\sum_{i\le l,j<l}t_i\Gamma_{ij}s_j^T,\qquad
B_l=\sum_{i,j\le l}t_i\Gamma_{ij}s_j^T,\qquad B_0=0.
\]
Their half-step increments are
\[
B_{l-1/2}-B_{l-1}=t_l a_l^T,
\quad a_l=\sum_{j<l}s_j\Gamma_{lj},\qquad
B_l-B_{l-1/2}=b_l s_l^T,
\quad b_l=\sum_{i\le l}t_i\Gamma_{il}.                        \tag{Q4.2}
\]
The first fresh vector is conditionally \(N(0,\mathsf S_{l-1})\),
and the second is conditionally \(N(0,\mathsf T_l)\), at their
respective preceding half-steps. Hence \(B\) is a rectangular matrix
martingale. Its increments have finite moments at every fixed finite
\(n,m,K\), by (Q4.1) and the Gaussian moments. No bound on the raw
query norms is needed for this assertion.

At each prefix define the triangular perturbations
\[
 g_l=\frac1{\sqrt m}\sum_{i\le l}t_i(\Gamma A_\omega)_{il},\qquad
 k_l=\frac1{\sqrt m}\sum_{i<l}s_i(\Gamma^TA_\theta)_{il}.
\]
All products use the leading \(l\)-by-\(l\) matrices. These formulas are the
adaptive versions of Q2; \(k_l\) uses a strict reverse triangle.
The exact decompositions are
\[
g_l=\frac{B_l\omega_l}{m}
 +\frac{\sigma^2}{\sqrt m\,A_{\omega,ll}}b_l,\qquad
k_l=\frac{B_{l-1/2}^T\theta_l}{\sqrt m}
 +\frac{\sigma^2}{\sqrt m\,A_{\theta,ll}}a_l.                  \tag{Q4.3}
\]
For \(j\le l\), the Gram identity gives
\[
\frac{s_j^T\omega_l}{\sqrt m}
=\big[A_\omega-\sigma^2A_\omega^{-T}\big]_{jl},
\]
so \(A_{\omega,jl}=s_j^T\omega_l/\sqrt m\) for \(j<l\),
and the diagonal has the additional \(\sigma^2/A_{\omega,ll}\).
The same identity holds for \(A_\theta\). Substitution into the two
triangular terms just displayed proves (Q4.3), including the strict reverse sum.
Furthermore, each diagonal obeys \(A_{ll}\ge\sigma\): its squared
Schur complement is
\(\sigma^2+x_l^T[I-X_{l-1}(X_{l-1}^TX_{l-1}+
\sigma^2I)^{-1}X_{l-1}^T]x_l\ge\sigma^2\).
Thus both residual coefficients in (Q4.3), apart from \(m^{-1/2}\),
are at most \(\sigma\).

### 2. Quantitative adaptive bound

Take deterministic \(R_\theta,R_\omega\ge0\),
\(r=\max(R_\theta,R_\omega)>0\), and \(0<\alpha<1\). Set
\[
E_R=\{\rho_{\theta,K}\le R_\theta,
       \rho_{\omega,K}\le R_\omega\},\quad
u=\log(4K/\alpha),\quad c=\sqrt{2r+4u},
\quad v=\log(2(n+m)/\alpha),
\quad L=2\sqrt{rv}+\tfrac23cv.                               \tag{Q4.4}
\]
Then
\[
\mathbb P\left(E_R\cap
 \left\{\max_h\|B_h\|_{\rm op}>L
 \ \text{or}\ \max_l(\|a_l\|\vee\|b_l\|)>c\right\}\right)
\le\alpha,                                                  \tag{Q4.5}
\]
where \(h\) runs over all half and full steps through \(K\).
If additionally
\(\max_l\|\theta_l\|\le A\),
\(\max_l\|\omega_l\|/\sqrt m\le C\), then outside the same
exceptional event, on \(E_R\),
\[
\max_l\|g_l\|\le\frac{CL+\sigma c}{\sqrt m},\qquad
\max_l\|k_l\|\le\frac{AL+\sigma c}{\sqrt m}.                 \tag{Q4.6}
\]
These norm bounds may instead be imposed on an event and intersected
with \(E_R\). If \(r=0\), both Gram contractions are zero on
\(E_R\), and the claimed perturbations are zero there.

### Proof, including localization and truncation

First stop accepting increments permanently before a rank threshold
would be exceeded. Before row \(l\), both \(\rho_{\theta,l}\)
and \(\rho_{\omega,l-1}\) are known; accept the row only while they
are within their thresholds. Before column \(l\),
\(\rho_{\omega,l}\) is also known; accept the column only if its
threshold has not been exceeded. These acceptance indicators are
predictable at their respective half-steps. The accepted process agrees
with \(B\) on \(E_R\). Its coefficients still refer to the original
adaptive histories; this construction does not alter the query dynamics.

For an accepted untruncated row increment \(X=t_la_l^T\), its two
conditional second-moment matrices are
\[
\mathbb E[XX^T\mid\mathcal F_{l-1}]
 =\rho_{\omega,l-1}t_lt_l^T,\qquad
\mathbb E[X^TX\mid\mathcal F_{l-1}]
 =\|t_l\|^2\mathsf S_{l-1}.
\]
For an accepted column increment \(Y=b_ls_l^T\), they are
\[
\mathbb E[YY^T\mid\mathcal F_{l-1/2}]
 =\|s_l\|^2\mathsf T_l,\qquad
\mathbb E[Y^TY\mid\mathcal F_{l-1/2}]
 =\rho_{\theta,l}s_ls_l^T.
\]
Summing along each realized path, (Q4.1) and the threshold rule imply
\[
W_{\rm left}\preceq
 R_\omega\sum_{\rm accepted\ rows}t_lt_l^T
 +\sum_{\rm accepted\ columns}\|s_l\|^2I_n
 \preceq2R_\omega I_n,
\]
\[
W_{\rm right}\preceq
 \sum_{\rm accepted\ rows}\|t_l\|^2I_m
 +R_\theta\sum_{\rm accepted\ columns}s_ls_l^T
 \preceq2R_\theta I_m.                                      \tag{Q4.7}
\]
In particular both predictable quadratic variations have norm at most
\(2r\). The unequal left/right constants matter: no factor \(K\)
has been introduced.

To bound increments without an unjustified Gaussian boundedness
assumption, multiply each accepted row increment by
\(\mathbf1_{\{\|a_l\|\le c\}}\), and each accepted column
increment by \(\mathbf1_{\{\|b_l\|\le c\}}\). Conditional
Gaussian symmetry makes the truncated increments centered. Their
conditional second moments are bounded in positive-semidefinite order
by the untruncated ones, so (Q4.7) remains valid. Their operator norms are
at most \(c\), since \(\|t_l\|,\|s_l\|\le1\).

At every accepted half-step the fresh Gaussian vector \(Z\) has
covariance at most the identity and trace at most \(r\). Its covariance
eigenvalues \(\lambda_j\in[0,1]\) give
\[
\mathbb E[e^{\|Z\|^2/4}\mid\text{past}]
=\prod_j(1-\lambda_j/2)^{-1/2}\le e^{r/2},\qquad
\mathbb P(\|Z\|>c\mid\text{past})\le e^{-u}.
\]
The product estimate uses \(-\log(1-x)\le2x\) for \(x\le1/2\).
A union bound over at most \(2K\) accepted half-steps costs at most
\(2Ke^{-u}=\alpha/2\). On its complement and \(E_R\), no
truncation or stopping occurred, and the truncated martingale agrees
with \(B\) at every half-step; all residual vectors have norm at most
\(c\).

Apply the rectangular martingale bound proved in fragment Q3.
For an \(n\times m\) matrix martingale with increment norms at most
\(c\) and both predictable quadratic variations at most \(2r\),
that bound controls the probability its norm ever exceeds \(x\) by
\[
(n+m)\exp\left[-\frac{x^2}{2(2r+cx/3)}\right].
\]
The truncated process starts at zero, is adapted and centered, has bounded
increments and thus is integrable, and satisfies (Q4.7); these verify every
hypothesis. For \(x=L\),
\(L^2\ge2v(2r+cL/3)\), so the bound is at most \(\alpha/2\).
Combining it with the truncation failure probability proves (Q4.5).
Finally (Q4.3), \(A_{ll}\ge\sigma\), and the query norm bounds prove
(Q4.6). None of these steps conditions on adaptive histories as though
their Gaussian law were unchanged.



## Destination: gaussian_calculus — Q5. The causal filtered recursion and its own ranks

This is a finite auxiliary recursion, with canonical Gaussian non-matrix and
initial-matrix seeds plus independent oracle noise. Its slow histories are
produced by its own perturbed dynamics. The proof uses Q4 twice; no frozen-query
Gaussian estimate is applied to an adaptive history.

Fix a feature-time horizon \(S>0\), and, for integers \(n\ge2\), put
\[
 \eta=n^{-2},\qquad N=\lceil Sn^2\rceil,\qquad
 T=N\eta\le S+1,\qquad K=N+1,
 \qquad \sigma=n^{-1/4},\qquad \gamma=1/8,\qquad \epsilon=n^{-\gamma},
 \qquad \ell_n=\log(e+n).
 \tag{Q5.1}
\]
Here \(N\) counts updates and \(K\) counts query pairs **per matrix**, including
one warmup. \(T\) is a feature-time horizon, not an established physical-time
horizon. Fix one deterministic scalar map \(\tau:\mathbb R\to\mathbb R\)
satisfying
\[
 |\tau(u)|\le |u|,\qquad |\tau(u)-\tau(v)|\le |u-v|.
 \tag{Q5.2}
\]
Apply it coordinatewise. Identity and any fixed clipping map satisfying
(Q5.2) are allowed. The constants below depend only on \(S\), not on the
clipping level or on which such map was fixed. The probability assertion
is for each fixed map; it does not assert a single event valid
simultaneously for all maps. A deterministic choice of map at each width
also satisfies the same estimates.

All vector norms below are ordinary Euclidean norms, with each factor
\(1/\sqrt n\) displayed explicitly. For a history
matrix \(X\in\mathbb R^{n\times k}\), define
\[
 \rho(X)=\operatorname{tr}\!\left[
 XX^T(XX^T+\sigma^2I_n)^{-1}\right].
 \tag{Q5.3}
\]
This equals the effective-rank expression using \(X^TX\), including when
\(k>n\). The four histories will be the lower and upper reverse arguments
divided by \(\sqrt n\), and the lower and upper forward arguments divided
by \(\sqrt n\), including their warmups.

**Auxiliary theorem.** The recursion in Sections 1--2 is finite and
measurable almost surely for every finite \(n,N\). There are deterministic
constants \(C_S<\infty\) and events \(\mathcal E_n^\tau\) such that
\[
 \mathbb P(\mathcal E_n^\tau)
 \ge 1-4e^{-(8-2\log9)n}-2n e^{-n^2/2}-5n^{-2},
 \tag{Q5.4}
\]
and, on these events, every prefix of every one of the four actual
histories satisfies
\[
 \rho\le C_S n^{11/12}\ell_n^{4/3}.
 \tag{Q5.5}
\]
For both matrices and both orientations, including warmups, let \(e_l\)
be the raw perturbed output minus the exact initial-matrix action on
that same actual query argument. Then, on the same event,
\[
 \max_l \frac{\|e_l\|_2}{\sqrt n}
 \le C_S n^{-1/24}\ell_n^{8/3}+C_S n^{-1/4}.
 \tag{Q5.6}
\]
Both terms tend to zero. This comparison is on the auxiliary algorithm's
own arguments, not on arguments imported from an unperturbed trajectory.

The proof first uses the universal ceiling \(\rho\le n\) in the adaptive
theorem. This gives logarithmic state bounds without assuming slow
histories. Relaxation then bounds increments of the actual histories.
A deterministic column approximation proves (Q5.5), after which a second,
localized application of the adaptive theorem proves (Q5.6). Neither pass
conditions on the realized histories as if their Gaussian law were
unchanged.

### 1. Exact oracle, canonical seeds, and causal warmup

Let \(\phi(z)=\arctan z\), \(F(z)=z+z^3/3\), and
\(\psi=\phi\circ F^{-1}\). These act coordinatewise. \(F\) is a
bijection of \(\mathbb R\), since \(F'(z)=1+z^2\ge1\) and its limits
at the two ends of the line are infinite with opposite signs. In particular,
\[
 |\phi|\le c_\phi:=\pi/2,\quad 0<\phi'\le1,\quad
 \|\phi''\|_\infty\le2,\quad
 \psi'(x)=\frac{1}{(1+(F^{-1}x)^2)^2}\le1.
 \tag{Q5.7}
\]

Sample the independent canonical initial blocks
\[
 z^{(1)}_{0,i}\sim N(0,1),\quad
 W^{(2)}_{0,ij},W^{(3)}_{0,ij}\sim N(0,1/n),\quad
 W^{(4)}_{0,i}\sim N(0,n^{-2}).
 \tag{Q5.8}
\]
Set \(x^{(1)}_0=F(z^{(1)}_0)\) and \(h^{(1)}_0=\phi(z^{(1)}_0)\).
The notation \(W^{(4)}_0\) will also denote the initial readout register.
For each \(b\in\{2,3\}\), set \(G^{(b)}=\sqrt n W^{(b)}_0\) and
sample independent arrays
\[
 \Gamma^{(b)}\in\mathbb R^{K\times K},\qquad
 U^{(b)}_l,V^{(b)}_l\in\mathbb R^n\quad(1\le l\le K),
 \tag{Q5.9}
\]
all with independent standard Gaussian entries. These two collections
are mutually independent and independent of (Q5.8).

Here is the exact paired oracle for either matrix; suppress \(b\)
temporarily. At call \(l\), the raw reverse argument is \(v_l\in\mathbb R^n\)
and the raw forward argument is \(h_l\in\mathbb R^n\). Its normalized variables
are
\[
 \theta_l=v_l/\sqrt n,\qquad\omega_l=h_l,\qquad
 p_l^{\rm src}=G^T\theta_l=W_0^Tv_l,\qquad
 q_l^{\rm src}=G\omega_l/n=W_0h_l/\sqrt n.
 \tag{Q5.10}
\]
For each leading history \(\Theta_l=[\theta_1,\ldots,\theta_l]\),
\(\Omega_l=[\omega_1,\ldots,\omega_l]\), take the positive-diagonal
upper Cholesky factors
\[
 A_{\theta,l}^TA_{\theta,l}=\Theta_l^T\Theta_l+\sigma^2I_l,
 \qquad
 A_{\omega,l}^TA_{\omega,l}=\Omega_l^T\Omega_l/n+\sigma^2I_l.
 \tag{Q5.11}
\]
Their leading blocks, including inverse leading blocks, agree as calls
are appended. Define the permanent columns
\[
 t_i=(\Theta_l A_{\theta,l}^{-1})_i,\qquad
 s_i=(\Omega_l A_{\omega,l}^{-1})_i/\sqrt n\quad(i\le l).
 \tag{Q5.12}
\]
The exact Gamma perturbations are
\[
 \begin{split}
 g_l&=\frac1{\sqrt n}\sum_{i\le l}
 t_i(\Gamma_{[l]\times[l]}A_{\omega,l})_{il},\\
 k_l&=\frac1{\sqrt n}\sum_{i<l}
 s_i(\Gamma_{[l]\times[l]}^T A_{\theta,l})_{il}.
 \end{split}
 \tag{Q5.13}
\]
In particular, the reverse sum is strict. Define the raw outputs, which
are the quantities actually used by the recursion, by
\[
 \begin{split}
 \mathcal R_l&=W_0^Tv_l+\sqrt n\,k_l+\sigma U_l,\\
 \mathcal F_l&=W_0h_l+\sqrt n\,g_l+\sigma V_l.
 \end{split}
 \tag{Q5.14}
\]
Thus the perturbed reverse output is \(\widehat p_l=\mathcal R_l\),
while its perturbed normalized forward output is
\(\widehat q_l=\mathcal F_l/\sqrt n=q_l^{\rm src}+g_l+\sigma V_l/\sqrt n\).
The raw query errors and their normalized sizes are consequently
\[
 e_l^{\rm rev}=\sqrt n\,k_l+\sigma U_l,\qquad
 e_l^{\rm for}=\sqrt n\,g_l+\sigma V_l,
 \tag{Q5.15}
\]
\[
 \frac{\|e_l^{\rm rev}\|_2}{\sqrt n}\le\|k_l\|_2+\sigma\frac{\|U_l\|_2}{\sqrt n},
 \qquad
 \frac{\|e_l^{\rm for}\|_2}{\sqrt n}\le\|g_l\|_2+\sigma\frac{\|V_l\|_2}{\sqrt n}.
 \tag{Q5.16}
\]
Both raw direct noises in (Q5.14) have coordinate variance \(\sigma^2\).
Their contributions to RMS errors are \(\sigma U_l/\sqrt n\) and
\(\sigma V_l/\sqrt n\). The Gaussian maximum bound is derived in Section 4.

Initialize the auxiliary registers
\[
 a^{(2)}_0=R^{(1)}_0=0,\qquad
 M^{(2)}_0=M^{(3)}_0=0,\qquad
 x^{(1)}_0=F(z^{(1)}_0),\qquad W^{(4)}_0\text{ as in (Q5.8)}.
 \tag{Q5.17}
\]
Here \(a^{(2)},R^{(1)},x^{(1)},W^{(4)},z^{(2)},z^{(3)}\) are vectors of
length \(n\), and \(M^{(2)},M^{(3)}\) are \(n\)-by-\(n\) matrices. The
preactivation registers \(z^{(2)}_0,z^{(3)}_0\) are obtained only by these
two warmup calls:

1. Lower call \(l=1\): use \(v^{(2)}_1=0\),
   \(h^{(2),\mathrm{query}}_1=h^{(1)}_0\), and set
   \(z^{(2)}_0=\mathcal F^{(2)}_1\).
2. Upper call \(l=1\): use \(v^{(3)}_1=0\),
   \(h^{(3),\mathrm{query}}_1=\phi(z^{(2)}_0)\), and set
   \(z^{(3)}_0=\mathcal F^{(3)}_1\).

Discard both warmup reverse outputs. For either warmup, \(\theta_1=0\)
implies \(t_1=0\), so (Q5.13) gives \(g_1=k_1=0\). The forward direct noise
does not vanish. In particular, the exact identities for these declared
oracle outputs are
\[
 z^{(2)}_0=W^{(2)}_0h^{(1)}_0+\sigma V^{(2)}_1,
 \qquad
 z^{(3)}_0=W^{(3)}_0\phi(z^{(2)}_0)+\sigma V^{(3)}_1.
 \tag{Q5.18}
\]
There are no other initial-matrix calls in initialization. Formula (Q5.18)
describes the two noisy calls; it is not an instruction to evaluate their
exact parts separately. The seeds have the canonical distribution (Q5.8),
but these warmup registers are not canonical exact network initialization.

### 2. All actual updates and their causal measurability

At each mesh state \(j=0,\ldots,N-1\), first form, entirely from that
pre-step state,
\[
 h^{(1)}_j=\psi(x^{(1)}_j),\qquad
 h^{(2)}_j=\phi(z^{(2)}_j),\qquad
 h^{(3)}_j=\phi(z^{(3)}_j),\qquad
 \delta^{(3)}_j=W^{(4)}_j\odot\phi'(z^{(3)}_j).
 \tag{Q5.19}
\]
At call index \(l=j+2\), use
\[
 \begin{array}{c|cc}
   &\theta_l&\omega_l\\\hline
 \text{lower }(b=2)&a^{(2)}_j/\sqrt n&h^{(1)}_j\\
 \text{upper }(b=3)&\delta^{(3)}_j/\sqrt n&h^{(2)}_j.
 \end{array}
 \tag{Q5.20}
\]
Execute the lower reverse/forward pair and then the upper reverse/forward
pair. Both arguments of both pairs have already been selected before
these outputs arrive. From the current upper reverse output form
\[
 q^{(2)}_j=\mathcal R^{(3)}_{j+2}
             +(M^{(3)}_j)^T\delta^{(3)}_j,
 \qquad
 \delta^{(2)}_j=\phi'(z^{(2)}_j)\odot\tau(q^{(2)}_j).
 \tag{Q5.21}
\]
Now update all registers simultaneously, using exactly the old factors
displayed on the right:
\[
 \begin{split}
 a^{(2)}_{j+1}&=a^{(2)}_j+\eta\delta^{(2)}_j,\\
 M^{(2)}_{j+1}&=M^{(2)}_j+
       \frac\eta n\delta^{(2)}_j(h^{(1)}_j)^T,\\
 M^{(3)}_{j+1}&=M^{(3)}_j+
       \frac\eta n\delta^{(3)}_j(h^{(2)}_j)^T,\\
 R^{(1)}_{j+1}&=R^{(1)}_j+\eta(M^{(2)}_j)^T\delta^{(2)}_j,\\
 W^{(4)}_{j+1}&=W^{(4)}_j+\eta h^{(3)}_j,\\
 x^{(1)}_{j+1}&=x^{(1)}_j+
    \frac\eta\epsilon
      [x^{(1)}_0+\mathcal R^{(2)}_{j+2}+R^{(1)}_j-x^{(1)}_j],\\
 z^{(2)}_{j+1}&=z^{(2)}_j+
    \frac\eta\epsilon
      [\mathcal F^{(2)}_{j+2}+M^{(2)}_j h^{(1)}_j-z^{(2)}_j],\\
 z^{(3)}_{j+1}&=z^{(3)}_j+
    \frac\eta\epsilon
      [\mathcal F^{(3)}_{j+2}+M^{(3)}_j h^{(2)}_j-z^{(3)}_j].
 \end{split}
 \tag{Q5.22}
\]
The memories retain every earlier increment. In particular, \(R^{(1)}\)
uses pre-step \(M^{(2)}_j\), not \(M^{(2)}_{j+1}\). The histories in the
theorem are the matrices \(\Theta^{(2)}_l,\Omega^{(2)}_l/\sqrt n,
\Theta^{(3)}_l,\Omega^{(3)}_l/\sqrt n\) actually generated by (Q5.17)--(Q5.22).

More explicitly, the finite-step memory identities are
\[
 \begin{split}
 M^{(2)}_j&=\frac\eta n\sum_{i<j}
                    \delta^{(2)}_i(h^{(1)}_i)^T,\\
 M^{(3)}_j&=\frac\eta n\sum_{i<j}
                    \delta^{(3)}_i(h^{(2)}_i)^T,\\
 R^{(1)}_j&=\eta\sum_{i<j}(M^{(2)}_i)^T\delta^{(2)}_i
       =\frac{\eta^2}{n}\sum_{0\le u<i<j}
           h^{(1)}_u(\delta^{(2)}_u)^T\delta^{(2)}_i\\
       &=\frac\eta n\sum_{u<j}h^{(1)}_u(\delta^{(2)}_u)^T
                         [a^{(2)}_j-a^{(2)}_{u+1}].
 \end{split}
 \tag{Q5.22a}
\]
The last identity uses
\(a^{(2)}_j-a^{(2)}_{u+1}=\eta\sum_{u<i<j}\delta^{(2)}_i\).
Thus \(R^{(1)}\) is the Euler, pre-step accumulated full rank memory;
at finite \(\eta\) it is not literally the continuous integral in the
integrated equations in fragment Q1. The strict time triangle is part of the specified
Euler convention. No trained term or earlier memory update is dropped.

Finiteness and measurability do not require a probability estimate.
All Gaussian entries are finite almost surely. Every regularized Gram
matrix in (Q5.11) is positive definite with smallest eigenvalue at least
\(\sigma^2>0\). Positive-diagonal Cholesky factorization and inversion
are continuous on this domain: the recursive diagonal square roots have
positive arguments and their denominators do not vanish. Formula (Q5.13)
therefore gives finite measurable outputs at every finite prefix. The
inverse \(F^{-1}\), arctangent, and \(\tau\) are continuous; finite sums
and products in (Q5.22) preserve finiteness. Induction over the two warmups
and the \(N\) updates proves the claim. No uniform bound is needed to
perform this induction.

For completeness, the adaptive filtration applies separately to each
matrix despite their interaction. For matrix \(b\), let
\(\mathcal H^{(b)}\) contain all canonical initial blocks, all \(U,V\),
and the other matrix's whole Gamma array. These primitive arrays are
jointly independent of \(\Gamma^{(b)}\). Set
\[
 \mathscr F^{(b)}_l=\mathcal H^{(b)}\vee
  \sigma(\Gamma^{(b)}_{ij}:i,j\le l),\qquad
 \mathscr F^{(b)}_{l-1/2}=\mathscr F^{(b)}_{l-1}\vee
  \sigma(\Gamma^{(b)}_{lj}:j<l).
 \tag{Q5.23}
\]
In the warmup, the upper forward argument depends only on the lower
warmup output, which is \(\mathcal H^{(3)}\)-measurable. Its own reverse
argument is zero. At each later call \(l=j+2\), the state at \(j\) uses
only calls through \(l-1\) of both matrices. Inductively it is
\(\mathscr F^{(b)}_{l-1}\)-measurable for each \(b\); the other matrix's
past calculations are measurable functions of the own past prefix and
the arrays already in \(\mathcal H^{(b)}\).

Consequently \(\theta_l\) and \(\omega_l\) in (Q5.20) are known before
the own fresh row. The reverse formula (Q5.13) uses only that row and the
old prefix. The forward formula then uses the own fresh column,
including the diagonal. The lower current call, when viewed in the
upper filtration, is also measurable before the upper fresh row,
because its arguments were pre-step arguments and its Gamma array is
in \(\mathcal H^{(3)}\). Thus the prescribed
\(\theta\to\widehat p\to\omega\to\widehat q\) order is valid.

The algorithm's query maps themselves need only its initial \(z^{(1)}_0,
W^{(4)}_0\) and its finite transcript of declared outputs. The larger
\(\mathcal H^{(b)}\) is a device for proving the adaptive estimate; it
does not authorize unrecorded matrix calls or supply an external network
trajectory. Nor does it include the other matrix's realized adaptive
transcript as an independent random array: that transcript is generated
by the just-verified measurable recursion.

### 3. The adaptive estimate in the exact form used

Here is the specialization of fragment Q4 to \(m=n\). For
either matrix set
\[
 \begin{split}
 B_{l-1/2}&=\sum_{i\le l,\,j<l}t_i\Gamma_{ij}s_j^T,
 &B_l&=\sum_{i,j\le l}t_i\Gamma_{ij}s_j^T,\\
 \mathfrak a_l&=\sum_{j<l}s_j\Gamma_{lj},
 &\mathfrak b_l&=\sum_{i\le l}t_i\Gamma_{il}.
 \end{split}
 \tag{Q5.24}
\]
The different font distinguishes these fresh Gaussian residual vectors
from the primitive register \(a^{(2)}\). The exact identities are
\[
 \begin{split}
 g_l&=B_l\omega_l/n+
       \frac{\sigma^2}{\sqrt n A_{\omega,ll}}\mathfrak b_l,\\
 k_l&=B_{l-1/2}^T\theta_l/\sqrt n+
       \frac{\sigma^2}{\sqrt n A_{\theta,ll}}\mathfrak a_l.
 \end{split}
 \tag{Q5.25}
\]
For example, (Q5.11)--(Q5.12) give
\[
 s_i^T\omega_l/\sqrt n
   =(A_\omega-\sigma^2A_\omega^{-T})_{il}.
\]
For \(i<l\) this is \(A_{\omega,il}\); on the diagonal it is
\(A_{\omega,ll}-\sigma^2/A_{\omega,ll}\). Substitution into (Q5.13)
gives the forward identity in (Q5.25); the same identity for \(t_i^T\theta_l\)
gives the strict reverse identity. Each diagonal is at least \(\sigma\):
its squared Schur complement is
\[
 \sigma^2+y^T[I-X(X^TX+\sigma^2I)^{-1}X^T]y\ge\sigma^2,
\]
where \(X\) comprises the previous normalized query columns. The matrix
in brackets is positive semidefinite, since its eigenvalues are
\(\sigma^2/(d^2+\sigma^2)\) on singular directions and one on the
orthogonal complement.

For a deterministic ceiling \(r>0\) and \(0<\alpha<1\), define
\[
 u=\log(4K/\alpha),\quad v=\log(4n/\alpha),\quad
 c(r)=\sqrt{2r+4u},\quad
 L(r)=2\sqrt{rv}+\tfrac23c(r)v.
 \tag{Q5.26}
\]
Let \(E_r^{(b)}\) be the event that both final effective ranks for matrix
\(b\) are at most \(r\). The adaptive theorem states
\[
 \mathbb P\left(E_r^{(b)}\cap\left\{
    \max_h\|B^{(b)}_h\|_{\rm op}>L(r)
    \ \text{or}\ 
    \max_l(\|\mathfrak a^{(b)}_l\|_2\vee
           \|\mathfrak b^{(b)}_l\|_2)>c(r)
 \right\}\right)\le\alpha.
 \tag{Q5.27}
\]
Here \(h\) ranges over all half and full steps, so no additional union
over query times is necessary. On \(E_r^{(b)}\), outside that exceptional
event, (Q5.25) implies for every call
\[
 \begin{split}
 \|g_l\|_2&\le
       \frac{L(r)\|h_l\|_2}{n}+\frac{\sigma c(r)}{\sqrt n},\\
 \|k_l\|_2&\le
       \frac{L(r)\|v_l\|_2}{n}+\frac{\sigma c(r)}{\sqrt n}.
 \end{split}
 \tag{Q5.28}
\]
These are pointwise inequalities; the query norms can subsequently be
bounded on an intersected event.

All hypotheses are satisfied: dimensions and horizon are deterministic
and finite, \(\sigma>0\), (Q5.9) supplies independent standard Gamma
entries and an independent \(\mathcal H^{(b)}\), (Q5.23) supplies the
required causal order, and (Q5.11) uses the required consistent Cholesky
choice. In fragment Q4, localization uses the actual histories and
does not modify their dynamics. The fresh conditional covariances are
\(\sum_{j<l}s_js_j^T\) and \(\sum_{i\le l}t_it_i^T\), each bounded by
the identity, with traces the corresponding effective ranks. In
particular \(\rho\le n\) always, regardless of raw query magnitudes.
Thus the first application of (Q5.27) with \(r=n\) has an automatic rank
premise. The second application below has a deterministic smaller
ceiling proved for these very histories.

### 4. Initial and direct-noise events; first adaptive pass

Let
\[
 E_0=\{\|W^{(2)}_0\|_{\rm op},\|W^{(3)}_0\|_{\rm op}\le8,
                   \ \|W^{(4)}_0\|_\infty\le1\}.
 \tag{Q5.29}
\]
We record elementary bounds for its probability instead of assuming a
primal bound for the new recursion. For a standard scalar Gaussian \(Z\),
completion of the square gives \(\mathbb E e^{tZ}=e^{t^2/2}\). Markov's
inequality, with \(t=a\) and then \(t=-a\), gives
\(\mathbb P(|Z|>a)\le2e^{-a^2/2}\). Hence the readout part fails with
probability at most \(2n e^{-n^2/2}\).

The Euclidean unit sphere has a \(1/4\)-net of size at most \(9^n\): take
a maximal separated set, whose disjoint radius-\(1/8\) balls lie in the
radius-\(9/8\) ball, and compare volumes. Maximality gives the net
property. For unit \(x,y\), approximate both by net points \(x_0,y_0\).
The error in \(x^TWy-x_0^TWy_0\) is at most
\(\frac12\|W\|_{\rm op}\), so
\(\|W\|_{\rm op}\le2\max_{x_0,y_0}|x_0^TWy_0|\).
For fixed net points and a matrix from (Q5.8), this bilinear form is a
Gaussian of variance \(1/n\). A union bound gives
\[
 \mathbb P(\|W\|_{\rm op}>8)
 \le2\,9^{2n}e^{-8n}.
\]
Applying it to both initial hidden matrices proves
\[
 \mathbb P(E_0^c)\le
 p_0(n):=4e^{-(8-2\log9)n}+2n e^{-n^2/2}.
 \tag{Q5.30}
\]
The first-layer Gaussian vector is finite almost surely. No norm bound
on its polynomial transform \(x^{(1)}_0\) will be needed; we bound the
displacement \(x^{(1)}_j-x^{(1)}_0\).

From now on choose \(\alpha=n^{-2}\) in (Q5.26), so
\[
 u=\log(4Kn^2),\qquad v=\log(4n^3),\qquad
 D_n=\sqrt{2+4u/n}=c(n)/\sqrt n.
 \tag{Q5.31}
\]
For a standard Gaussian vector \(Z\in\mathbb R^n\), integrating its
Gaussian density gives \(\mathbb E e^{\|Z\|_2^2/4}=2^{n/2}\le e^{n/2}\).
Therefore
\[
 \mathbb P(\|Z\|_2^2>2n+4u)\le e^{-u}.
\]
There are exactly \(4K\) direct-noise vectors across two orientations
and two matrices. The event
\[
 E_D=\left\{\max_{b,l}
   \frac{\|U^{(b)}_l\|_2\vee\|V^{(b)}_l\|_2}{\sqrt n}\le D_n\right\}
 \tag{Q5.32}
\]
satisfies \(\mathbb P(E_D^c)\le4Ke^{-u}=\alpha\), without any assumption
on the histories those vectors generate.

For each matrix let \(E_C^{(b)}\) be the event that all the bounds inside
(Q5.27) hold with \(r=n\). Since the rank premise is automatic,
\(\mathbb P((E_C^{(b)})^c)\le\alpha\). Define
\[
 E_C=E_0\cap E_D\cap E_C^{(2)}\cap E_C^{(3)}.
 \tag{Q5.33}
\]
No independence between these events is asserted or needed. Equations
(Q5.30)--(Q5.33) give \(\mathbb P(E_C^c)\le p_0(n)+3\alpha\).

The deterministic inequalities \(K\le(S+2)n^2\) and \(n\ge2\) imply
\[
 u,v\le C_S\ell_n,\qquad
 D_n\le C_S,\qquad
 c(n)\le C_S\sqrt n,\qquad
 L(n)/\sqrt n\le C_S\ell_n.
 \tag{Q5.34}
\]
For example, \(\ell_n/n\) is bounded for \(n\ge2\), and the two terms
in \(L(n)/\sqrt n\) are \(2\sqrt v\) and
\((2/3)D_nv\). Thus (Q5.14), (Q5.16), (Q5.28), and \(E_0\) show, on \(E_C\),
for either oracle and every actual call,
\[
 \frac{\|\mathcal R_l\|_2}{\sqrt n}\le C_S\ell_n\frac{\|v_l\|_2}{\sqrt n}+C_S\sigma,
 \qquad
 \frac{\|\mathcal F_l\|_2}{\sqrt n}\le C_S\ell_n\frac{\|h_l\|_2}{\sqrt n}+C_S\sigma.
 \tag{Q5.35}
\]
This conclusion does not presuppose any bound on \(v_l\).

In particular, the warmup identities (Q5.18) and \(|\phi|\le c_\phi\)
give
\(\|z^{(2)}_0\|_2/\sqrt n,\|z^{(3)}_0\|_2/\sqrt n
  \le8c_\phi+\sigma D_n\le C_S\).
For orientation only, define the mathematical reference values
\(z^{(2),\mathrm{can}}_0=W^{(2)}_0h^{(1)}_0\) and
\(z^{(3),\mathrm{can}}_0=W^{(3)}_0\phi(z^{(2),\mathrm{can}}_0)\).
They are not evaluated by the algorithm. Their initial differences obey
\[
 \frac{\|z^{(2)}_0-z^{(2),\mathrm{can}}_0\|_2}{\sqrt n}\le\sigma D_n,
 \qquad
 \frac{\|z^{(3)}_0-z^{(3),\mathrm{can}}_0\|_2}{\sqrt n}\le9\sigma D_n,
 \tag{Q5.36}
\]
because the upper initial operator norm is at most eight and \(\phi\)
is 1-Lipschitz. This proves small initial discrepancies without hiding
any exact initialization calls.

### 5. Noncircular bounds for the actual states

All bounds in this section are deterministic on \(E_C\), uniform through
state \(N\), and uniform in the fixed choice of \(\tau\). Constants may
increase from line to line. For a rank-one increment,
\[
 \left\|uv^T/n\right\|_F=\frac{\|u\|_2\|v\|_2}{n},\qquad
 \frac{\|Av\|_2}{\sqrt n}\le\|A\|_{\rm op}\frac{\|v\|_2}{\sqrt n}\le\|A\|_F\frac{\|v\|_2}{\sqrt n}.
 \tag{Q5.37}
\]

First the readout update alone, independent of every other bound, gives
\[
 \|W^{(4)}_j\|_\infty\le1+j\eta c_\phi
        \le B_4:=1+(S+1)c_\phi,
 \qquad \frac{\|\delta^{(3)}_j\|_2}{\sqrt n}\le B_4.
 \tag{Q5.38}
\]
The upper matrix memory therefore satisfies
\[
 \|M^{(3)}_j\|_F
 \le\eta\sum_{i<j}\frac{\|\delta^{(3)}_i\|_2\|h^{(2)}_i\|_2}{n}
 \le T B_4c_\phi\le C_S.
 \tag{Q5.39}
\]
The upper reverse query in (Q5.20) has raw argument \(\delta^{(3)}_j\).
Using (Q5.35), (Q5.38), and (Q5.39) in (Q5.21) gives
\[
 \frac{\|q^{(2)}_j\|_2}{\sqrt n}
 \le C_S\ell_n B_4+C_S\sigma+
          \|M^{(3)}_j\|_F B_4
 \le C_S\ell_n,
 \qquad \frac{\|\delta^{(2)}_j\|_2}{\sqrt n}\le\frac{\|q^{(2)}_j\|_2}{\sqrt n}\le C_S\ell_n.
 \tag{Q5.40}
\]
The last inequality uses just (Q5.2) and \(\phi'\le1\). Summing the first
two updates in (Q5.22) yields
\[
 \frac{\|a^{(2)}_j\|_2}{\sqrt n}\le C_ST\ell_n\le C_S\ell_n,
 \qquad
 \|M^{(2)}_j\|_F\le C_STc_\phi\ell_n\le C_S\ell_n.
 \tag{Q5.41}
\]
The pre-step memory formula for \(R^{(1)}\) then yields
\[
 \frac{\|R^{(1)}_j\|_2}{\sqrt n}
 \le\eta\sum_{i<j}\|M^{(2)}_i\|_F\frac{\|\delta^{(2)}_i\|_2}{\sqrt n}
 \le C_S\ell_n^2.
 \tag{Q5.42}
\]
In particular, the lower reverse output and the two forward outputs
satisfy
\[
 \frac{\|\mathcal R^{(2)}_{j+2}\|_2}{\sqrt n}\le C_S\ell_n^2,
 \qquad
 \frac{\|\mathcal F^{(2)}_{j+2}\|_2}{\sqrt n},
 \frac{\|\mathcal F^{(3)}_{j+2}\|_2}{\sqrt n}\le C_S\ell_n,
 \tag{Q5.43}
\]
by (Q5.35), (Q5.41), and the uniform bound on every activation.

Set \(y_j=x^{(1)}_j-x^{(1)}_0\) and
\(\lambda=\eta/\epsilon=n^{-15/8}\in(0,1]\). The last three updates
in (Q5.22) are convex combinations of the current register and its target:
\[
 \begin{split}
 y_{j+1}&=(1-\lambda)y_j+
     \lambda[\mathcal R^{(2)}_{j+2}+R^{(1)}_j],\\
 z^{(2)}_{j+1}&=(1-\lambda)z^{(2)}_j+
     \lambda[\mathcal F^{(2)}_{j+2}+M^{(2)}_jh^{(1)}_j],\\
 z^{(3)}_{j+1}&=(1-\lambda)z^{(3)}_j+
     \lambda[\mathcal F^{(3)}_{j+2}+M^{(3)}_jh^{(2)}_j].
 \end{split}
 \tag{Q5.44}
\]
The targets have normalized norms at most \(C_S\ell_n^2,C_S\ell_n,
C_S\ell_n\), respectively, by (Q5.39)--(Q5.43). Since \(y_0=0\) and the
warmup preactivations are bounded, the triangle inequality and induction
in (Q5.44) give
\[
 \max_{j\le N}\frac{\|x^{(1)}_j-x^{(1)}_0\|_2}{\sqrt n}\le C_S\ell_n^2,
 \qquad
 \max_{j\le N}
 \frac{\|z^{(2)}_j\|_2\vee\|z^{(3)}_j\|_2}{\sqrt n}\le C_S\ell_n.
 \tag{Q5.45}
\]
There was no feedback bootstrap in this chain: bounded activations give
the readout and \(\delta^{(3)}\) bounds first, then the upper memory,
then \(\delta^{(2)}\), the lower memories, and finally the relaxed
registers. It uses neither a small effective-rank premise nor bounds
borrowed from an unperturbed network.

### 6. Actual slow histories and the warmup column

Taking differences in (Q5.44), and using both the target and state bounds,
gives
\[
 \begin{split}
 \frac{\|x^{(1)}_{j+1}-x^{(1)}_j\|_2}{\sqrt n}
      &\le C_S\eta\ell_n^2/\epsilon,\\
 \frac{\|z^{(2)}_{j+1}-z^{(2)}_j\|_2}{\sqrt n}
  \vee \frac{\|z^{(3)}_{j+1}-z^{(3)}_j\|_2}{\sqrt n}
      &\le C_S\eta\ell_n/\epsilon.
 \end{split}
 \tag{Q5.46}
\]
The Lipschitz bounds in (Q5.7) transfer these estimates to the first two
activation histories. For the upper reverse history, use the exact
difference identity
\[
 \begin{split}
 \delta^{(3)}_{j+1}-\delta^{(3)}_j
 ={}&(W^{(4)}_{j+1}-W^{(4)}_j)\odot\phi'(z^{(3)}_{j+1})\\
 &+W^{(4)}_j\odot
       [\phi'(z^{(3)}_{j+1})-\phi'(z^{(3)}_j)].
 \end{split}
\]
It and (Q5.38), (Q5.46) imply
\[
 \frac{\|\delta^{(3)}_{j+1}-\delta^{(3)}_j\|_2}{\sqrt n}
 \le\eta c_\phi+2B_4\frac{\|z^{(3)}_{j+1}-z^{(3)}_j\|_2}{\sqrt n}
 \le C_S\eta\ell_n/\epsilon.
\]
Finally \(\frac{\|a^{(2)}_{j+1}-a^{(2)}_j\|_2}{\sqrt n}\le C_S\eta\ell_n\) follows
directly from (Q5.40). Summing adjacent increments proves the discrete
Lipschitz bounds on mesh indices, with constants
\[
 \begin{array}{c|c}
 \text{normalized mesh history}&\text{Lipschitz constant in feature time}\\\hline
 h^{(1)}_j/\sqrt n&C_S\ell_n^2/\epsilon\\
 h^{(2)}_j/\sqrt n&C_S\ell_n/\epsilon\\
 \delta^{(3)}_j/\sqrt n&C_S\ell_n/\epsilon\\
 a^{(2)}_j/\sqrt n&C_S\ell_n.
 \end{array}
 \tag{Q5.47}
\]
Choose once a deterministic constant \(C_*(S)\ge1\) large enough that
\[
 M_*:=C_*(S)\ell_n^2/\epsilon
 \tag{Q5.48}
\]
dominates all four constants in (Q5.47), for all \(n\ge2\). Such a choice
is possible because every preceding constant was deterministic and
independent of \(\tau\).

The warmup needs separate treatment. For the lower reverse history its
warmup and first mesh column are both zero. For the two forward
histories the warmup repeats the first mesh argument. For the upper
reverse history, however, the warmup column is zero while the first
mesh column is \(\delta^{(3)}_0/\sqrt n\), generally nonzero, at the
same physical and feature time. We do **not** assert (Q5.47) across this
pair. We keep the warmup column exactly in a column approximation,
costing at most one additional rank direction for each history.

Here is the deterministic estimate, including integer and dimension
choices. Let \(X\) be any one of the \(n\)-by-\(K\) normalized full
histories, comprising one warmup and \(N\) mesh columns. For any integer
\(1\le d\le N\), partition the mesh-column indices \(1,\ldots,N\) into
the nonempty blocks
\[
 \lfloor (a-1)N/d\rfloor< i\le\lfloor aN/d\rfloor,
       \qquad a=1,\ldots,d.
\]
Replace each mesh column by its block's first column, and retain the
warmup exactly, to obtain \(Y\). Then
\[
 \operatorname{rank}Y\le d+1,\qquad
 \|X-Y\|_F^2\le N(M_*T/d)^2.
 \tag{Q5.49}
\]
Indeed, each block spans at most
\(\eta(\lceil N/d\rceil-1)\le\eta N/d=T/d\) in feature time,
and (Q5.47)--(Q5.48) bound each column error by \(M_*T/d\).

To verify the effective-rank implication without a spectral-tail
assumption, let \(P\) be the orthogonal projection onto the column space
of \(Y\), and let \(Q=XX^T(XX^T+\sigma^2I)^{-1}\). Eigenvalues give
\(0\preceq Q\preceq I\) and \(Q\preceq XX^T/\sigma^2\). Consequently
\[
 \begin{split}
 \rho(X)&=\operatorname{tr}(PQ)+\operatorname{tr}((I-P)Q)\\
 &\le d+1+\sigma^{-2}\|(I-P)X\|_F^2\\
 &\le d+1+\frac{NM_*^2T^2}{\sigma^2d^2}.
 \end{split}
 \tag{Q5.50}
\]
The last line uses \((I-P)Y=0\). Independently \(\rho(X)\le\min(n,K)\).

Put
\[
 x_*=(NM_*^2T^2/\sigma^2)^{1/3},\qquad
 d=\min\{N,\max\{1,\lceil x_*\rceil\}\}.
 \tag{Q5.51}
\]
If \(0<x_*\le N\), then \(d\le x_*+1\), \(d\ge x_*\), and (Q5.50) is
at most \(2+2x_*\). If \(x_*=0\), choose \(d=1\), and (Q5.50) is at most
two. If \(x_*>N\), take the exact \(K\)-column rank bound; in this case
\(K=N+1\le2+2x_*\). Thus, in every case,
\[
 \rho(X)\le r_n:=\min\{n,K,2+2x_*\}.
 \tag{Q5.52}
\]
The ceiling \(r_n>0\) is deterministic; the adaptive theorem permits real
ceilings. The integer \(d\) used to prove it has been specified in (Q5.51).
For the chosen parameters,
\[
 \begin{split}
 x_*&=C_*(S)^{2/3}
  (NT^2\epsilon^{-2}\sigma^{-2})^{1/3}\ell_n^{4/3}\\
 &\le C_S\big(n^2 n^{1/4}n^{1/2}\big)^{1/3}\ell_n^{4/3}
  =C_S n^{11/12}\ell_n^{4/3}.
 \end{split}
 \tag{Q5.53}
\]
This proves (Q5.5) for final histories on \(E_C\), with the extra two
absorbed in \(C_S\). Prefix effective ranks cannot exceed the final
rank: the consistent Cholesky columns express them as
\(\sum_{i\le l}\|t_i\|_2^2\) or \(\sum_{i\le l}\|s_i\|_2^2\).
This also proves (Q5.5) for every prefix. Every matrix in (Q5.49)--(Q5.53) is
the realized perturbed history; no frozen-history probabilistic
calculation was used.

### 7. Second adaptive pass and raw perturbation size

Apply (Q5.27) again to each matrix, now with the deterministic ceiling
\(r=r_n\), the same \(K,\sigma\), and failure allowance \(\alpha=n^{-2}\).
For \(b=2,3\), let
\[
 F_b=E_{r_n}^{(b)}\cap\left\{
    \max_h\|B^{(b)}_h\|_{\rm op}>L(r_n)
    \ \text{or}\ 
    \max_l(\|\mathfrak a^{(b)}_l\|_2\vee
           \|\mathfrak b^{(b)}_l\|_2)>c(r_n)
 \right\}.
 \tag{Q5.54}
\]
The theorem gives \(\mathbb P(F_b)\le\alpha\) unconditionally. Section 6
proved \(E_C\subseteq E_{r_n}^{(2)}\cap E_{r_n}^{(3)}\). Therefore on
\[
 \mathcal E_n^\tau=E_C\setminus(F_2\cup F_3)
 \tag{Q5.55}
\]
all the refined bounds hold for both matrices. The union bound gives
(Q5.4). In particular, we have not conditioned the second martingale
argument on the first pass, nor resampled any arrays, nor assumed
independence of the two matrices' resulting bad events.

From (Q5.26), (Q5.31), and (Q5.34),
\[
 \frac{L(r_n)}{\sqrt n}
 \le C_S\left(\sqrt{r_n/n}\,\ell_n+
                  n^{-1/2}\ell_n^{3/2}\right).
 \tag{Q5.56}
\]
Here \(\sqrt{r_nv}/\sqrt n\le C_S\sqrt{r_n/n}\ell_n\), and
\(c(r_n)\le\sqrt{2r_n}+2\sqrt u\) bounds the other term. Using (Q5.53)
in (Q5.56) yields
\[
 \frac{L(r_n)}{\sqrt n}
 \le C_S n^{-1/24}\ell_n^{5/3}
       +C_S n^{-1/2}\ell_n^{3/2}.
 \tag{Q5.57}
\]
Also \(r_n\le n\) implies
\[
 \sigma c(r_n)/\sqrt n\le\sigma c(n)/\sqrt n\le C_S\sigma.
 \tag{Q5.58}
\]
All forward raw arguments obey \(\frac{\|h_l\|_2}{\sqrt n}\le c_\phi\), including
warmups. All upper reverse raw arguments have normalized norm at most
\(B_4\), including the zero warmup. All lower reverse raw arguments have
normalized norm at most \(C_S\ell_n\) by (Q5.41), again including the zero
warmup. Thus a common upper bound for every query norm occurring in
(Q5.28) is \(C_S\ell_n\). Combining (Q5.16), (Q5.28), (Q5.32), and (Q5.57)--(Q5.58) gives
\[
 \max_{b,l}
 \frac{\|e_l^{(b),\rm rev}\|_2\vee\|e_l^{(b),\rm for}\|_2}{\sqrt n}
 \le C_S n^{-1/24}\ell_n^{8/3}
    +C_S n^{-1/2}\ell_n^{5/2}+C_S\sigma.
 \tag{Q5.59}
\]
For \(n\ge2\), the middle term is bounded by the first after enlarging
the constant, since their ratio is \(n^{-11/24}\ell_n^{-1/6}\le1\).
Substitution of \(\sigma=n^{-1/4}\) proves (Q5.6).

The rank bound also gives
\(r_n\ell_n^2/n\le C_S n^{-1/12}\ell_n^{10/3}\to0\), consistent
with the adaptive theorem's criterion. For any one of these errors,
its mesh primitive satisfies the purely deterministic bound
\[
 \max_{j\le N}\frac{\left\|\eta\sum_{i<j}e_{i+2}\right\|_2}{\sqrt n}
       \le T\max_{l\ge2}\frac{\|e_l\|_2}{\sqrt n}.
 \tag{Q5.60}
\]
Neither (Q5.59) nor (Q5.60) is a nonlinear trajectory comparison. The theorem
is proved for each prescribed \(\tau\). Its constants and failure
allowances are uniform in clipping level, but its adaptive events may
depend on \(\tau\). No union over all clipping maps has been taken.

For the degenerate horizon \(S=0\), there are no updates and \(K=1\):
the reverse histories are zero, each forward history has effective rank
at most one, the Gamma terms vanish, and the same asymptotic claims
follow directly from the Gaussian maximum for the four warmup noise
vectors. The main proof above treats the nonempty-update case \(S>0\).


## Destination: gaussian_calculus — Q6. Deterministic filtered/unfiltered clipped stability

Compare the exact auxiliary recursion in Q5 with the unfiltered, algebraically
constrained finite-width feature flow below. Both use the same initial bottom
vector, hidden matrices and stored readout, and the same bounded clipping map.
The query errors are evaluated at the actual perturbed arguments.

### Statement and exact comparison

Fix \(S,M\ge1\), \(R\ge1\), \(n\ge1\), and a scalar map \(\tau\) with
\[
 |\tau(v)|\le |v|,\qquad |\tau(v)|\le R,\qquad
 |\tau(v)-\tau(w)|\le |v-w|.
 \tag{Q6.1}
\]
Take \(0<\eta\le1\), an integer \(N\ge1\) with \(N\eta\le S+1\),
and \(\eta\le\varepsilon\le1\).
Every vector norm below is an ordinary Euclidean norm.
Suppose the two initial matrices have operator norm at most \(M\)
and \(\|W^{(4)}_0\|_\infty\le1\).
There is no bound needed on individual coordinates of \(z^{(1)}_0\).

The reference is the canonical finite-width feature flow with
\[
 h^{(\ell)}=\phi(z^{(\ell)}),\quad \phi(z)=\arctan z,\quad
 z^{(2)}=W^{(2)}h^{(1)},\quad z^{(3)}=W^{(3)}h^{(2)},
\]
\[
 \delta^{(3)}=W^{(4)}\odot\phi'(z^{(3)}),\quad
 q^{(2)}=(W^{(3)})^{\mathsf T}\delta^{(3)},\quad
 \delta^{(2)}=\phi'(z^{(2)})\odot\tau(q^{(2)}),
\]
\[
 (z^{(1)})'=\phi'(z^{(1)})\odot(W^{(2)})^{\mathsf T}\delta^{(2)},
 \quad (W^{(2)})'=\delta^{(2)}(h^{(1)})^{\mathsf T}/n,
 \quad (W^{(3)})'=\delta^{(3)}(h^{(2)})^{\mathsf T}/n,
 \quad (W^{(4)})'=h^{(3)}.
 \tag{Q6.2}
\]
All initial parameters equal the stated initial values. A prime in
this fragment means differentiation in feature time.
Put \(F(z)=z+z^3/3\), \(x^{(1)}=F(z^{(1)})\), and
\[
 a^{(2)}(s)=\int_0^s\delta^{(2)}(t)\,dt,\qquad
 M^{(\ell)}=W^{(\ell)}-W^{(\ell)}_0\quad(\ell=2,3),\qquad
 R^{(1)}(s)=\int_0^s (M^{(2)}(t))^{\mathsf T}\delta^{(2)}(t)\,dt.
 \tag{Q6.3}
\]
These identities retain every learned matrix term. Exactly,
\[
 x^{(1)}=x^{(1)}_0+(W^{(2)}_0)^{\mathsf T}a^{(2)}+R^{(1)}.
 \tag{Q6.4}
\]
Indeed \(F'=1/\phi'\) turns the first equation in (Q6.2) into
\((x^{(1)})'=(W^{(2)}_0+M^{(2)})^{\mathsf T}\delta^{(2)}\);
integrating proves (Q6.4).

Hats denote the filtered recursion at \(s_k=k\eta\).
At the start of each step set
\[
 \widehat h_k^{(1)}=\phi(F^{-1}(\widehat x_k^{(1)})),\quad
 \widehat h_k^{(2)}=\phi(\widehat z_k^{(2)}),\quad
 \widehat h_k^{(3)}=\phi(\widehat z_k^{(3)}),\quad
 \widehat\delta_k^{(3)}
   =\widehat W_k^{(4)}\odot\phi'(\widehat z_k^{(3)}).
\]
Let the four queried outputs be
\[
 \widehat T_k^{(2)}
  =(W^{(2)}_0)^{\mathsf T}\widehat a_k^{(2)}+e_{T,k}^{(2)},
 \qquad
 \widehat F_k^{(2)}
  =W^{(2)}_0\widehat h_k^{(1)}+e_{F,k}^{(2)},
\]
\[
 \widehat T_k^{(3)}
  =(W^{(3)}_0)^{\mathsf T}\widehat\delta_k^{(3)}+e_{T,k}^{(3)},
 \qquad
 \widehat F_k^{(3)}
  =W^{(3)}_0\widehat h_k^{(2)}+e_{F,k}^{(3)}.
 \tag{Q6.5}
\]
Here the query errors may depend arbitrarily on all previous states.
Assume only
\[
 \max_{\ell=2,3;\,0\le k<N}
 \frac{\|e_{T,k}^{(\ell)}\|_2+\|e_{F,k}^{(\ell)}\|_2}{\sqrt n}
 \le b,\qquad 0\le b\le1.
 \tag{Q6.6}
\]
Form \(\widehat q_k^{(2)}=\widehat T_k^{(3)}
       +(\widehat M_k^{(3)})^{\mathsf T}\widehat\delta_k^{(3)}\)
and \(\widehat\delta_k^{(2)}
       =\phi'(\widehat z_k^{(2)})\odot\tau(\widehat q_k^{(2)})\).
Every right side in the following simultaneous updates uses step \(k\):
\[
\begin{aligned}
 \widehat a_{k+1}^{(2)}
  &=\widehat a_k^{(2)}+\eta\widehat\delta_k^{(2)},\\
 \widehat M_{k+1}^{(2)}
  &=\widehat M_k^{(2)}
      +\eta\widehat\delta_k^{(2)}(\widehat h_k^{(1)})^{\mathsf T}/n,\\
 \widehat M_{k+1}^{(3)}
  &=\widehat M_k^{(3)}
      +\eta\widehat\delta_k^{(3)}(\widehat h_k^{(2)})^{\mathsf T}/n,\\
 \widehat R_{k+1}^{(1)}
  &=\widehat R_k^{(1)}
      +\eta(\widehat M_k^{(2)})^{\mathsf T}\widehat\delta_k^{(2)},\\
 \widehat W_{k+1}^{(4)}
  &=\widehat W_k^{(4)}+\eta\widehat h_k^{(3)},\\
 \widehat x_{k+1}^{(1)}
  &=(1-\eta/\varepsilon)\widehat x_k^{(1)}
       +(\eta/\varepsilon)
       [x_0^{(1)}+\widehat T_k^{(2)}+\widehat R_k^{(1)}],\\
 \widehat z_{k+1}^{(2)}
  &=(1-\eta/\varepsilon)\widehat z_k^{(2)}
       +(\eta/\varepsilon)
       [\widehat F_k^{(2)}+\widehat M_k^{(2)}\widehat h_k^{(1)}],\\
 \widehat z_{k+1}^{(3)}
  &=(1-\eta/\varepsilon)\widehat z_k^{(3)}
       +(\eta/\varepsilon)
       [\widehat F_k^{(3)}+\widehat M_k^{(3)}\widehat h_k^{(2)}].
\end{aligned}
 \tag{Q6.7}
\]
Initially \(\widehat a^{(2)},\widehat R^{(1)},\widehat M^{(2)},
\widehat M^{(3)}\) are zero,
\(\widehat x_0^{(1)}=x_0^{(1)}\), and
\(\widehat W_0^{(4)}=W_0^{(4)}\).
Allow warmup errors satisfying
\[
 d_0:=\frac{\|\widehat z_0^{(2)}-z_0^{(2)}\|_2+
                 \|\widehat z_0^{(3)}-z_0^{(3)}\|_2}{\sqrt n}\le1.
 \tag{Q6.8}
\]
Then a constant \(C_{S,M,R}\), independent of \(n,\eta,\varepsilon,b,d_0\)
and of the particular map in (Q6.1), satisfies
\[
\begin{split}
 \max_{0\le k\le N}\bigg\{
 &\frac{\|\widehat x_k^{(1)}-x^{(1)}(s_k)\|_2+
          \|\widehat z_k^{(2)}-z^{(2)}(s_k)\|_2+
          \|\widehat z_k^{(3)}-z^{(3)}(s_k)\|_2}{\sqrt n}\\
 &+\frac{\|\widehat a_k^{(2)}-a^{(2)}(s_k)\|_2+
          \|\widehat R_k^{(1)}-R^{(1)}(s_k)\|_2+
          \|\widehat W_k^{(4)}-W^{(4)}(s_k)\|_2}{\sqrt n}\\
 &+\|\widehat M_k^{(2)}-M^{(2)}(s_k)\|_{\rm F}
   +\|\widehat M_k^{(3)}-M^{(3)}(s_k)\|_{\rm F}\bigg\}
 \le C_{S,M,R}(\varepsilon+\eta+b+d_0).
\end{split}
 \tag{Q6.9}
\]
Thus there is no \(\exp(C/\varepsilon)\) stability loss here.
The constant is not claimed uniform as \(R\) increases.

### Uniform bounds and reference quadrature

Write \(c=\pi/2\) and \(T=S+1\). For either the reference or the
recursion, the readout coordinate bound is \(1+cT\), since each
readout derivative or increment is bounded by \(c\).
Consequently the normalized size of \(\delta^{(3)}\) is bounded
by \(1+cT\). The rank-one inequality
\(\|uv^{\mathsf T}/n\|_{\rm F}=\|u\|_2\|v\|_2/n\)
bounds \(\|M^{(3)}\|_{\rm F}\) and \(\|\widehat M^{(3)}\|_{\rm F}\)
by \(cT(1+cT)\).
Equation (Q6.5), (Q6.6), and the initial operator bound give
\(\|\widehat q_k^{(2)}\|_2/\sqrt n\le C_{S,M}\);
the same estimate, without query error, holds for the reference.
Domination in (Q6.1) gives the bound for both \(\delta^{(2)}\).
Their integrals and rank updates bound \(a^{(2)},M^{(2)},R^{(1)}\)
and their hatted versions, with vector norms divided by \(\sqrt n\)
and matrix Frobenius norms, by \(C_{S,M}\).
This reasoning is sequential: no state-error bound has been used.

The filter coefficient \(\eta/\varepsilon\) is in \([0,1]\).
Thus (Q6.7) bounds \(\|\widehat x^{(1)}-x_0^{(1)}\|_2/\sqrt n\)
by the maximum size of its bounded targets, and bounds the two
hatted preactivations similarly. Both their initial normalized sizes
are at most \(Mc+d_0\), by the initial operator bound and (Q6.8).
All these bounds are \(C_{S,M}\). The reference preactivations
are bounded by the two trained operator norms times \(c\).

The reference field is locally Lipschitz at each finite \(n\):
\(\tau\) is Lipschitz, the other coordinate functions are smooth,
and its products are locally Lipschitz in finitely many parameters.
The preceding polynomial readout and trained-matrix bounds prevent
escape. Its bottom derivative has normalized size at most
\(\|W^{(2)}\|_{\rm op}\|\delta^{(2)}\|_2/\sqrt n\),
which also prevents bottom escape. Hence its unique local solution
continues throughout \([0,T]\).

The reference velocities \(x^{(1)\prime},z^{(2)\prime},
z^{(3)\prime},h^{(1)\prime},h^{(2)\prime},h^{(3)\prime}\)
have normalized size bounded by \(C_{S,M}\).
For example,
\[
 x^{(1)\prime}=(W^{(2)})^{\mathsf T}\delta^{(2)},\qquad
 h^{(1)\prime}=\phi'(z^{(1)})^2\odot
                       (W^{(2)})^{\mathsf T}\delta^{(2)},
\]
\[
 z^{(2)\prime}
 =\frac{\|h^{(1)}\|_2^2}{n}\delta^{(2)}
       +W^{(2)}h^{(1)\prime},\qquad
 z^{(3)\prime}
 =\frac{\|h^{(2)}\|_2^2}{n}\delta^{(3)}
       +W^{(3)}h^{(2)\prime}.
 \tag{Q6.10}
\]
Use \(|\phi'|\le1\) and the established bounds.
Also
\[
 \delta^{(3)\prime}
 =h^{(3)}\odot\phi'(z^{(3)})
       +W^{(4)}\odot\phi''(z^{(3)})\odot z^{(3)\prime},
\]
\[
 q^{(2)\prime}
 =h^{(2)}\frac{\|\delta^{(3)}\|_2^2}{n}
       +(W^{(3)})^{\mathsf T}\delta^{(3)\prime}.
 \tag{Q6.11}
\]
These have the same normalized bounds because \(|\phi''|\le2\)
and the readout coordinates are bounded.
For the possibly nondifferentiable clipping, the difference quotient
bound from (Q6.1), followed by (Q6.10)--(Q6.11), gives
\[
 \frac{\|\delta^{(2)}(s)-\delta^{(2)}(t)\|_2}{\sqrt n}
 \le \frac{\|q^{(2)}(s)-q^{(2)}(t)\|_2}{\sqrt n}
       +2R\frac{\|z^{(2)}(s)-z^{(2)}(t)\|_2}{\sqrt n}
 \le C_{S,M,R}|s-t|.
 \tag{Q6.12}
\]
All five reference slow right sides
\[
 \delta^{(2)},\quad
 \delta^{(2)}(h^{(1)})^{\mathsf T}/n,\quad
 \delta^{(3)}(h^{(2)})^{\mathsf T}/n,\quad
 (M^{(2)})^{\mathsf T}\delta^{(2)},\quad h^{(3)}
 \tag{Q6.13}
\]
are therefore time-Lipschitz with constant \(C_{S,M,R}\) in their
respective norms. For a product, subtract one factor at a time and
use the uniform bounds above and the rank-one inequality.
Integrating its difference from the left endpoint over one step
gives a quadrature error at most \(C_{S,M,R}\eta^2/2\)
for each equation in (Q6.13).

### Filter contraction and the slow-state error

Let \(E_k\) be the sum of the last five errors in (Q6.9), namely
those in \(a^{(2)},M^{(2)},M^{(3)},R^{(1)},W^{(4)}\), and put
\(D_k=\max_{0\le j\le k}E_j\).
Let \(A_k,B_k,C_k\) be the normalized errors in
\(x^{(1)},z^{(2)},z^{(3)}\), respectively; these are nonnegative
scalars, not matrices. Initially \(E_0=A_0=0\) and \(B_0+C_0=d_0\).
The maps \(F^{-1}\) and \(\phi\circ F^{-1}\) are 1-Lipschitz,
because \(F'\ge1\) and
\((\phi\circ F^{-1})'=(\phi'\circ F^{-1})^2\le1\).

For \(p=\eta/\varepsilon\), (Q6.4)--(Q6.7) and the reference velocity
bound give
\[
 A_{k+1}\le(1-p)A_k+p(ME_k+E_k+b)+C_{S,M}\eta.
 \tag{Q6.14}
\]
The last term is the reference increment
\(x^{(1)}(s_{k+1})-x^{(1)}(s_k)\); its reference target at step
\(k\) equals \(x^{(1)}(s_k)\) exactly, not its next value.
Iterating (Q6.14) and using
\(\sum_{j=0}^{k-1}p(1-p)^j\le1\) gives
\[
 \max_{j\le k}A_j\le C_{S,M}(D_k+b+\varepsilon).
 \tag{Q6.15}
\]
Here \(\eta\sum_{j\ge0}(1-p)^j=\eta/p=\varepsilon\);
this is why there is no inverse-filter exponential.

Subtract the two layer-two targets. Their normalized difference is
at most
\[
 (M+\|\widehat M_k^{(2)}\|_{\rm op})A_k
       +c\|\widehat M_k^{(2)}-M^{(2)}(s_k)\|_{\rm F}+b.
\]
In this expression use the decomposition with the hatted matrix on
the activation difference and the reference activation on the matrix
difference. The same geometric-sum argument and (Q6.10) yield
\[
 \max_{j\le k}B_j
 \le B_0+C_{S,M}\big(\max_{j\le k}A_j+D_k+b+\varepsilon\big).
 \tag{Q6.16}
\]
For layer three replace \(A_k,M^{(2)}\) by \(B_k,M^{(3)}\):
\[
 \max_{j\le k}C_j
 \le C_0+C_{S,M}\big(\max_{j\le k}B_j+D_k+b+\varepsilon\big).
 \tag{Q6.17}
\]
The feedforward order of (Q6.15)--(Q6.17) gives, without a circular
instantaneous estimate,
\[
 \max_{j\le k}(A_j+B_j+C_j)
 \le C_{S,M}(D_k+b+\varepsilon+d_0).
 \tag{Q6.18}
\]

The ordinary top query difference is bounded by
\[
 \frac{\|\widehat q_k^{(2)}-q^{(2)}(s_k)\|_2}{\sqrt n}
 \le C_{S,M}(E_k+C_k)+b.
 \tag{Q6.19}
\]
Indeed the top backward difference is at most the readout error
plus \(2(1+cT)C_k\); expand the two factors in
\((W^{(3)}_0+\widehat M^{(3)})^{\mathsf T}\widehat\delta^{(3)}\)
and then add the reverse query error. The bounded clipping gives
\[
 \frac{\|\widehat\delta_k^{(2)}-\delta^{(2)}(s_k)\|_2}{\sqrt n}
 \le C_{S,M}(E_k+C_k)+b+2RB_k.
 \tag{Q6.20}
\]
Subtracting each slow right side in (Q6.13), one factor at a time,
therefore bounds its difference by
\(C_{S,M,R}(E_k+A_k+B_k+C_k+b)\).
For the memory right side specifically, use
\[
 \frac{\|(\widehat M_k^{(2)})^{\mathsf T}\widehat\delta_k^{(2)}
              -(M^{(2)}(s_k))^{\mathsf T}\delta^{(2)}(s_k)\|_2}{\sqrt n}
 \le
 \|\widehat M_k^{(2)}-M^{(2)}(s_k)\|_{\rm F}
       \frac{\|\widehat\delta_k^{(2)}\|_2}{\sqrt n}
 +\|M^{(2)}(s_k)\|_{\rm op}
       \frac{\|\widehat\delta_k^{(2)}-\delta^{(2)}(s_k)\|_2}{\sqrt n}.
 \tag{Q6.21}
\]
Thus the full returned memory is included.

The quadrature estimate after (Q6.13) and (Q6.18) imply
\[
 E_{k+1}\le E_k+
 C_{S,M,R}\eta(D_k+b+\varepsilon+d_0+\eta).
 \tag{Q6.22}
\]
Summing and maximizing,
\[
 D_k\le C_{S,M,R}(S+1)(b+\varepsilon+d_0+\eta)
       +C_{S,M,R}\eta\sum_{j<k}D_j.
 \tag{Q6.23}
\]
If \(H=C_{S,M,R}(S+1)(b+\varepsilon+d_0+\eta)\) and
\(L=C_{S,M,R}\), induction on (Q6.23) gives
\(D_k\le H(1+L\eta)^k\le H e^{L(S+1)}\).
This proves (Q6.9) together with (Q6.18).

### What this bridge does and does not remove

For a warmup of the form
\[
 \widehat z_0^{(2)}=W_0^{(2)}h_0^{(1)}+e_0^{(2)},\qquad
 \widehat z_0^{(3)}=W_0^{(3)}\phi(\widehat z_0^{(2)})+e_0^{(3)},
\]
one has \(d_0\le (1+M)\|e_0^{(2)}\|_2/\sqrt n+
\|e_0^{(3)}\|_2/\sqrt n\). Thus vanishing warmup errors are
covered, without pretending the noisy initial fields equal the
canonical fields. On any events where fragment Q5 establishes
\(b\to0\), its vanishing \(\varepsilon,\eta\) gives (Q6.9) for every
fixed clipping satisfying (Q6.1). The reference and the approximation
use the same original hidden matrices and the same prescribed tiny
readout; no comparison to a zero-readout evolved trajectory occurs.

One may reconstruct the forward fields from the approximate raw
parameters instead of from the registers. For example their layer-two
constraint discrepancy is bounded by
\[
 \frac{\|\widehat z_k^{(2)}
 -(W_0^{(2)}+\widehat M_k^{(2)})
      \phi(F^{-1}(\widehat x_k^{(1)}))\|_2}{\sqrt n}
 \le B_k+C_{S,M}(A_k+E_k).
 \tag{Q6.24}
\]
The layer-three discrepancy then follows using (Q6.24) and the bounded
trained operator norms. Hence the register constraint error also
vanishes under (Q6.9); it is not silently set to zero in (Q6.7).

For the uncut map \(\tau(v)=v\), (Q6.20) is not available with a fixed
constant \(R\). Its exact replacement retains
\[
 [\phi'(\widehat z_k^{(2)})-\phi'(z^{(2)}(s_k))]
       \odot q^{(2)}(s_k).
 \tag{Q6.25}
\]
The normalized Euclidean bound on \(q^{(2)}\) alone does not control
this term by \(B_k\), uniformly in width. Small query forcing,
vanishing filter scale, and causal low-rank histories do not discharge
that missing stability step. No uniformity as \(R\to\infty\), uncut
population existence, restartability, or exact raw-GD convergence is
proved here.

The estimate concerns states and the explicitly bounded clipped
queries in (Q6.19)--(Q6.20). Derivatives of the filter registers have a
factor \(1/\varepsilon\); (Q6.9) alone does not imply convergence of
those derivatives. All hidden velocity/kernel and physical-clock
convergence claims must still be justified separately.


## Destination: gaussian_calculus — Q7. Growing-cap filtered/unfiltered comparison

The reference in this statement remains clipped. Increasing the cap establishes
a comparison between two width-dependent clipped systems; it does not identify
an uncut or common population limit.

Fix \(S>0\). For each \(n\ge2\), choose a deterministic clipping bound
\(R_n\ge1\) and one deterministic scalar map \(\tau_n\) such that
\[
 |\tau_n(v)|\le\min\{|v|,R_n\},\qquad
 |\tau_n(v)-\tau_n(w)|\le|v-w|,\qquad R_n=o(\log n).
 \tag{Q7.1}
\]
In particular, \(R_n\to\infty\) is permitted. The identity map is
not covered by a finite \(R_n\); no assertion about it is hidden in (Q7.1).
Examples of admissible bounds include
\(R_n=\max\{1,\sqrt{\log(e+n)}\}\), with any common clipping satisfying
the displayed bounds. No condition of simultaneous Gaussian events
over all maps is imposed.

Let \(E_n(S)\) be exactly the maximum in equation (Q6.9) of fragment Q6 for the algorithm and its reference at all mesh states through
\(N=\lceil Sn^2\rceil\). Thus it sums the Euclidean errors, divided
by \(\sqrt n\), in \(x^{(1)},z^{(2)},z^{(3)},a^{(2)},R^{(1)},W^{(4)}\)
and the ordinary Frobenius errors in \(M^{(2)},M^{(3)}\).
The reference is clipped with \(\tau_n\), and its initial fields
are computed exactly from the original canonical Gaussian seeds;
the algorithm's noisy warmup is compared to them, not identified
with them.

There exist events with probability tending to one and a deterministic
sequence \(d_n(S)\to0\) such that
\[
 E_n(S)\le n^{-1/24+d_n(S)}.
 \tag{Q7.2}
\]
The events have the same lower probability bound as equation (Q5.4) of
fragment Q5, after ignoring finitely many widths. Consequently
\(E_n(S)\to0\) in probability for every fixed finite \(S\).

### The clipping dependence is explicit, not assumed uniform

We first extract a quantitative constant from the deterministic
stability proof. With \(S,M\) fixed, its preceding uniform state,
operator, readout-coordinate and filter bounds are independent of \(R\).
Call a common larger constant \(C_0(S,M)\ge1\).
Its reference middle-backward time difference in (Q6.12) is bounded by
\(C_0(1+R)|s-t|\). Each of its five reference slow right sides
therefore has time-Lipschitz constant at most \(C_1(1+R)\):
the only new \(R\) factor enters through \(\delta^{(2)}\), and in
each product one subtracts one factor at a time. All other factors
already have \(R\)-independent bounds. Thus the sum of one-step
quadrature errors is at most \(C_2(1+R)\eta^2\).

Likewise the difference of the two top backward fields is bounded
by the readout error and a constant times the layer-three state error,
independently of \(R\). The ordinary query difference has the same
property, together with its query error. The sole extra clipping
factor in the middle backward difference is
\[
 2R\,\frac{\|\widehat z_k^{(2)}-z^{(2)}(s_k)\|_2}{\sqrt n}.
 \tag{Q7.3}
\]
Each of the five slow right-side differences is thus bounded by
\(C_3(1+R)\) times the sum of current state and query errors.
There is no product of two middle backward differences.

In the notation of that proof, filter contraction gives
\[
 \max_{j\le k}(A_j+B_j+C_j)
 \le C_4(D_k+b+\varepsilon+d_0),
 \tag{Q7.4}
\]
with \(C_4\) independent of \(R\). Substitution into its slow-state
inequality therefore yields
\[
 E_{k+1}\le E_k+
 C_5(1+R)\eta(D_k+b+\varepsilon+d_0+\eta).
 \tag{Q7.5}
\]
Here \(E_k,D_k\) are respectively the slow-state error and its
running maximum; they are not \(E_n(S)\).
Summing and using the same elementary discrete Gronwall calculation
as in the fragment Q6 gives, after combining (Q7.4)--(Q7.5),
\[
 E_n(S)\le C_6(1+R)\exp(C_6(1+R))
                    (b+\varepsilon+d_0+\eta),
 \tag{Q7.6}
\]
whenever the hypotheses of that deterministic theorem hold.
All \(C_i\) depend only on \(S,M\), not on the map within its stated
bounds, width, mesh or filter scale. Increasing \(S\) to
\(\max\{1,S\}\) handles the fragment Q6's harmless \(S\ge1\)
normalization. This proves (Q7.6) with linear, not unspecified, clipping
dependence in the exponential.

### Apply the bound to the actual perturbed histories

The rank theorem applies to each prescribed \(\tau_n\), since its
constants and probability allowances are uniform in that deterministic
choice. It supplies a single event for this choice on which
\[
 \|W^{(2)}_0\|_{\rm op},\|W^{(3)}_0\|_{\rm op}\le8,\qquad
 \|W^{(4)}_0\|_\infty\le1,
\]
and every raw query error, divided by \(\sqrt n\), is at most
\[
 B_n=C_S n^{-1/24}\log(e+n)^{8/3}+C_S n^{-1/4}.
 \tag{Q7.7}
\]
The fragment Q6 uses a sum of two orientation errors at each
layer, so take \(b=2B_n\), not \(B_n\). Eventually \(b\le1\).
The direct-noise event in the rank theorem bounds the warmup errors
and gives \(d_0\le C_S n^{-1/4}\), by its equation (Q5.36) or direct
1-Lipschitzness of \(\phi\). Eventually \(d_0\le1\).
No conditional independence after selecting this event is used.

Its remaining parameters are
\(\varepsilon=n^{-1/8}\), \(\eta=n^{-2}\), and
\(N\eta\le S+1\), with \(0<\eta\le\varepsilon\le1\).
Thus all deterministic hypotheses are checked on the same event.
Apply (Q7.6) with \(M=8\) and \(R=R_n\). Since every other error is
bounded by a constant times the first term of (Q7.7), it follows that
\[
 E_n(S)\le
 C_S(1+R_n)\exp(C_S(1+R_n))
 n^{-1/24}\log(e+n)^{8/3}.
 \tag{Q7.8}
\]
The logarithm of the prefactor on the right, divided by \(\log n\),
tends to zero: \(R_n=o(\log n)\),
\(\log(1+R_n)=o(\log n)\), and
\(\log\log(e+n)=o(\log n)\). Enlarging a nonnegative deterministic
sequence \(d_n(S)\to0\) to absorb the constant in (Q7.8) proves (Q7.2).
The event probability tends to one by the rank theorem, which proves
the convergence in probability without any exchange of expectation,
clipping supremum or infinite-time limit.

### What remains after this diagonal transfer

Both processes in (Q7.2) still depend on the clipping \(\tau_n\).
The theorem says they are close to each other. It does not show that
either is close to the uncut canonical finite-width flow, nor that
their common asymptotic law exists. In particular, \(R_n\to\infty\)
alone does not prevent backward-field mass from reaching the cutoff.

The estimate has not proved a uniform clipped-tail envelope, uncut
uniqueness or autonomous restart, a limiting action-space construction,
or physical-clock/exact-GD convergence. The layer-register derivatives
and all required kernel/velocity observables still require their own
arguments. This diagonal bridge is stronger than holding the clipping
level fixed, but is not a substitute for any of these missing conclusions.


## Destination: gaussian_calculus — G. Exact coupled two-matrix Gaussian transcript law

Use the fully specified algorithm in Q5. All learned increments, query outputs,
filters and memories are retained, together with the non-matrix roots. The
original initialized matrices themselves are not part of the retained joint
transcript. The finite equality in distribution below follows from the complete
covariance and sequential conditioning proof; no asymptotic Gaussian comparison
theorem is assumed.

### 1. The two declared query rules

Fix \(n,K\ge1\) and \(\sigma>0\). For the moment consider a single
matrix. Its raw reverse and forward query vectors are \(v_l,h_l\)
at calls \(1\le l\le K\). Set
\[
 \theta_l=v_l/\sqrt n,\qquad \omega_l=h_l,\qquad
 \Theta_l=[\theta_1,\ldots,\theta_l],\quad
 \Omega_l=[\omega_1,\ldots,\omega_l].
\]
Use the positive-diagonal upper Cholesky factors
\[
 A_{\theta,l}^TA_{\theta,l}=\Theta_l^T\Theta_l+\sigma^2I_l,\qquad
 A_{\omega,l}^TA_{\omega,l}=\Omega_l^T\Omega_l/n+\sigma^2I_l.
 \tag{G.1}
\]
Leading blocks agree across prefixes. The columns
\[
 t_i=(\Theta_l A_{\theta,l}^{-1})_i,\qquad
 s_i=(\Omega_l A_{\omega,l}^{-1})_i/\sqrt n
 \quad(i\le l)
 \tag{G.2}
\]
therefore do not change with later calls. In particular
\[
 \sum_{i\le l}t_it_i^T\preceq I_n,\qquad
 \sum_{i\le l}s_is_i^T\preceq I_n.
 \tag{G.3}
\]
For example the first sum equals
\(\Theta_l(\Theta_l^T\Theta_l+\sigma^2I)^{-1}\Theta_l^T\);
its singular-direction eigenvalues are \(d^2/(d^2+\sigma^2)\).

For the original perturbed rule, let \(G_0\) be an \(n\)-by-\(n\)
standard Gaussian matrix, let \(\Gamma\) be \(K\)-by-\(K\) standard
Gaussian, and let \(U_l,V_l\in\mathbb R^n\) be standard Gaussian.
All entries and arrays are independent. With \(W_0=G_0/\sqrt n\),
the two raw outputs are
\[
 \begin{split}
 {\cal R}_l&=G_0^T\theta_l+
       \sum_{i<l}s_i(\Gamma^TA_\theta)_{il}+\sigma U_l,\\
 {\cal F}_l&=G_0\omega_l/\sqrt n+
       \sum_{i\le l}t_i(\Gamma A_\omega)_{il}+\sigma V_l.
 \end{split}
 \tag{G.4}
\]
Each product at call \(l\) uses its leading \(l\)-by-\(l\) blocks.
These are exactly the raw outputs of fragment Q5: in its notation
the two displayed Gamma sums are \(\sqrt n\,k_l,\sqrt n\,g_l\).
The reverse sum is strict.

For the replacement rule, sample mutually independent standard
Gaussian matrices \(Z^{\rm for},Z^{\rm rev}\in\mathbb R^{n\times K}\)
and \(\Lambda\in\mathbb R^{K\times K}\). Write \(Z_i^{\rm for}\) and
\(Z_i^{\rm rev}\) for their columns. With the same query maps and the
same factors (G.1)--(G.2), but evaluated on this rule's own transcript,
set
\[
 \begin{split}
 {\cal R}_l^{\rm alt}
 &=\sum_{i\le l}Z_i^{\rm rev}A_{\theta,il}
       +\sum_{i<l}s_i\big((Z_i^{\rm for})^T\theta_l+
                                      \sigma\Lambda_{li}\big),\\
 {\cal F}_l^{\rm alt}
 &=\sum_{i\le l}Z_i^{\rm for}A_{\omega,il}
       +\sum_{i\le l}t_i\big((Z_i^{\rm rev})^T\omega_l/\sqrt n+
                                      \sigma\Lambda_{il}\big).
 \end{split}
 \tag{G.5}
\]
All vector/matrix dimensions and raw width factors are explicit.
In particular both kinds of output are raw \(n\)-vectors, with the normalized forward quantity equal to \(\mathcal F_l/\sqrt n\).

Assume that \(\theta_l\) is a finite measurable function of past
outputs, and \(\omega_l\) is a finite measurable function of past
outputs and possibly the current reverse output. Thus the order is
\(\theta_l\), reverse output, \(\omega_l\), forward output.
Both (G.4) and (G.5) are explicit causal recursions.
The strict reverse triangle means its factors only require earlier
forward queries; a future forward query is not needed to define it.
Positive Gram regularization ensures finite Cholesky factors and
inverses at every finite history.

The claim is equality in law of the entire output transcript, and
hence every measurable state computed from that transcript. The claim
does not preserve \(G_0\) itself as a jointly observed variable.

### 2. Covariance at an arbitrary fixed history

In this section the query vectors are deterministic arbitrary vectors.
This is a calculation of Gaussian processes at a fixed argument, not
conditioning an adaptive transcript and assuming its primitives remain
independent.

For calls \(l,k\), write
\[
 V_\theta(l,k)=\theta_l^T\theta_k+\sigma^2{\bf1}_{\{l=k\}},
 \quad
 V_\omega(l,k)=\omega_l^T\omega_k/n+\sigma^2{\bf1}_{\{l=k\}},
\]
and \(T_m=\sum_{i\le m}t_it_i^T\),
\(S_m=\sum_{i\le m}s_is_i^T\), with \(T_0=S_0=0\).
The Cholesky identities give
\[
 \sum_{i\le \min(l,k)}A_{\theta,il}A_{\theta,ik}
       =V_\theta(l,k),
 \quad
 \sum_{i\le \min(l,k)}A_{\omega,il}A_{\omega,ik}
       =V_\omega(l,k).
 \tag{G.6}
\]

For (G.4), independence and equality of the two indices of a common
Gamma entry give
\[
 \operatorname{Cov}({\cal F}_l,{\cal F}_k)
       =V_\omega(l,k)(I_n+T_{\min(l,k)}),
 \tag{G.7}
\]
\[
 \operatorname{Cov}({\cal R}_l,{\cal R}_k)
       =V_\theta(l,k)(I_n+S_{\min(l,k)-1}).
 \tag{G.8}
\]
For (G.7), the \(G_0\) contribution plus the direct noise is
\(V_\omega(l,k)I_n\); the Gamma contribution is
\(\sum_{i\le\min(l,k)}t_it_i^T
  \sum_{j\le\min(l,k)}A_{\omega,jl}A_{\omega,jk}\).
For (G.8), the outer-product sum is over \(i<\min(l,k)\)
while the \(A_\theta\) sum includes the diagonal. This proves both
identities and their strict/inclusive endpoints.

Define the two vectors, only for the following cross-covariance,
\[
 a_{l,k}=\sum_{i\le\min(l,k)}t_iA_{\theta,ik},\qquad
 b_{l,k}=\sum_{j\le\min(l,k-1)}s_jA_{\omega,jl}.
\]
Then direct index matching in (G.4) gives
\[
 \operatorname{Cov}({\cal F}_l,{\cal R}_k)
       =\theta_k\omega_l^T/\sqrt n+a_{l,k}b_{l,k}^T.
 \tag{G.9}
\]
The first term comes from \(G_0\), and the second uses precisely the
common entries \(\Gamma_{ij}\) with
\(i\le\min(l,k)\), \(j\le\min(l,k-1)\).

For (G.5), the forward-forward covariance of the \(Z^{\rm for}\)
parts is \(V_\omega(l,k)I_n\). The \(Z^{\rm rev}\) parts give
\((\omega_l^T\omega_k/n)T_{\min(l,k)}\), and the Lambda parts give
\(\sigma^2{\bf1}_{\{l=k\}}T_l\). The three arrays are independent,
so their sum is (G.7). The same calculation in reverse, with its
strict sums, gives (G.8).

There are two nonzero cross-covariances in (G.5):
the first forward term against the second reverse term, and the
second forward term against the first reverse term. Their sum is
\[
 \operatorname{Cov}({\cal F}_l^{\rm alt},{\cal R}_k^{\rm alt})
       =\theta_k b_{l,k}^T+a_{l,k}\omega_l^T/\sqrt n.
 \tag{G.10}
\]
There is no Lambda cross term: matching \(\Lambda_{il}\) with
\(\Lambda_{kj}\) would require \(i=k\le l=j<k\), an impossibility.
For \(l<k\), (G.2) implies \(b_{l,k}=\omega_l/\sqrt n\).
For \(l\ge k\), it implies \(a_{l,k}=\theta_k\).
These two cases prove that (G.9) and (G.10) agree for every \(l,k\),
including \(l=k\).

Thus the full stacked raw output vectors of (G.4) and (G.5) have identical
centered Gaussian covariances at every deterministic query history.
That common covariance is strictly positive definite. Indeed the
stacked direct noises \(\sigma U_l,\sigma V_l\) in (G.4) are independent
of all other terms and give \(\sigma^2 I_{2nK}\) to its covariance.
This argument concerns fixed arguments; it does not assert that the
actual adaptive output vector is jointly Gaussian.

### 3. Sequential covariance matching implies equality in law

Here is the finite Gaussian-conditioning fact needed to pass from the
preceding computation to actual adaptive histories.

Let \(g\) be a finite-dimensional standard Gaussian vector. Suppose
successive vector observations have the form
\[
 y_j=L_j(y_1,\ldots,y_{j-1})g,\qquad 1\le j\le m,
 \tag{G.11}
\]
where all coefficient matrices are finite measurable functions.
For a prescribed prefix \(y_1,\ldots,y_{j-1}\), stack the
first \(j\) row blocks into \(L_{\le j}(y)\), and suppose
\(K_{\le j}(y)=L_{\le j}(y)L_{\le j}(y)^T\) is positive definite.
The last row block depends on the prefix but not on \(y_j\).
This convention is used in every entry of \(K_{\le j}\).

The conditional distribution of the next observation is Gaussian
with mean and covariance
\[
 K_{j,<j}(y)K_{<j,<j}(y)^{-1}y_{<j},
 \quad
 K_{j,j}(y)-K_{j,<j}(y)K_{<j,<j}(y)^{-1}K_{<j,j}(y).
 \tag{G.12}
\]
For \(j=1\), the mean is zero.

To prove this, for deterministic \(L\) of full row rank decompose
\[
 g=L^T(LL^T)^{-1}Lg+
       [I-L^T(LL^T)^{-1}L]g.
\]
The two Gaussian terms have zero cross covariance and hence are
independent; this follows, for example, by factorization of their
joint Gaussian characteristic function. Therefore conditioning on
\(Lg=y\) gives a Gaussian with mean
\(L^T(LL^T)^{-1}y\) and covariance
\(I-L^T(LL^T)^{-1}L\).

Apply this argument first to the first observation. Inductively,
given the previous observations, the next matrix \(L_j(y_{<j})\)
is fixed, so conditioning the current Gaussian posterior on this
next linear observation gives (G.12). The same update gives posterior
mean \(L_{\le j}^TK_{\le j}^{-1}y_{\le j}\) and covariance
\(I-L_{\le j}^TK_{\le j}^{-1}L_{\le j}\): these identities can be
checked using the block inverse of
\[
 K_{\le j}=
 \begin{pmatrix}K_{<j,<j}&K_{<j,j}\\K_{j,<j}&K_{j,j}\end{pmatrix}
\]
and its Schur complement appearing in (G.12).
All inverses are measurable, and the positive Schur complements give
ordinary Gaussian conditional densities. This constructs the
conditional kernels inductively, including outside any particular
realized prefix. No assumption of independence of \(g\) from past
observations was used at the inductive step.

Consequently two recursions of the form (G.11), possibly with Gaussian
vectors of different dimensions, have the same transcript law whenever
their fixed-argument covariance matrices \(K_{\le j}(y)\) agree for
every prefix. Their first conditional kernels agree; (G.12) makes every
subsequent kernel agree, so iterated integration gives the same joint
law. Independent non-Gaussian initialization can be retained jointly
by first fixing its value and then integrating this equality.

This lemma needs only measurable causal coefficient matrices. It does
not infer a frozen Gaussian isometry for an adaptive output norm.

### 4. Apply the lemma to both interacting matrices

Run the full filtered recursion of fragment Q5. Its independent
non-matrix seeds are \(z^{(1)}_0\) and \(W^{(4)}_0\), with exactly their
canonical laws. For each matrix label \(b=2,3\), supply an independent
copy of (G.4), or an independent copy of (G.5). The two collections of
primitive Gaussian arrays are independent of one another and of these
non-matrix seeds.

Order the output blocks as follows: lower reverse/forward warmup,
upper reverse/forward warmup, and then at each update the lower
reverse/forward pair followed by the upper reverse/forward pair.
The algorithm counts discarded reverse warmup outputs in this list
although its state does not use them.

For each fixed full hypothetical transcript and fixed non-matrix seeds,
the algorithm determines every query by its previous outputs. At
each update all four arguments are selected from the pre-step state.
The upper warmup forward argument is the activation of the earlier
lower warmup output, so it also obeys this ordering. Every learned
matrix and the returned memory is a finite sum of earlier factors.
There is no direct access to \(W^{(2)}_0,W^{(3)}_0\) outside the
declared calls. This is the measurability property already proved
in fragment Q5; it holds for every hypothetical finite transcript,
not only for realized outputs.

At a fixed transcript, every output block is a linear function of
the finite vector of all primitive Gaussian entries, with coefficients
depending only on preceding blocks. For (G.4), the extra direct noise
has coefficient \(\sigma I_n\); for (G.5), expand the displayed linear
sums. The two matrices' cross covariances are zero at that fixed
argument because their primitive arrays are independent.
Within either matrix, equations (G.7)--(G.10) give identical covariances.
These equalities persist for every leading chronological prefix.

The stacked covariance of the original perturbed rule is at least
\(\sigma^2 I\), also on every prefix. The sequential lemma therefore
applies in the combined output space, without pretending that one
matrix's adaptive transcript is an independent seed for the other.
It proves equality in law of the ENTIRE coupled output transcript
for the all-original and all-replacement algorithms, jointly with
\(z^{(1)}_0,W^{(4)}_0\).

Every state register, learned increment, forward activation and middle
backward query computed from this transcript has the same joint law.
In particular both learned matrices and the strict pre-step returned
memory are preserved as computed states. The INITIAL hidden matrices
themselves are not asserted to survive as observed coordinates in the
replacement law. Nor are cross-process pathwise equalities asserted.

The result holds for every finite \(n,K,\sigma>0\) and every fixed
allowed clipping map, even if \(K\) grows with width. No limit or
width-uniform differentiability constant enters this exact equality.
It includes fragment Q5's identity map at this distributional
level, without asserting its uncut stability.

### 5. The actual conditional innovation in the middle query

Now work in the all-replacement realization. Use matrix label three
in (G.1)--(G.5). At a mesh step \(j\), its call is \(l=j+2\), and
\(\theta_l=\delta_j^{(3)}/\sqrt n\),
\(\omega_l=h_j^{(2)}\), exactly as in fragment Q5.

Let the past immediately before this upper reverse call contain the
non-matrix seeds, both matrices' earlier revealed primitives, and
the already computed current lower pair. The current upper queries
were pre-step queries. Reveal upper primitives at each reverse call
by taking \(Z_l^{\rm rev}\) and the row entries \(\Lambda_{li},i<l\);
at each forward call reveal \(Z_l^{\rm for}\) and
\(\Lambda_{il},i\le l\). This is an acyclic reveal order.
The current lower pair depends on upper primitives only through
earlier upper outputs, so it reveals no fresh upper primitive.

Set
\[
 \begin{split}
 m_l^{(2)}
 &=\sum_{i<l}Z_i^{{\rm rev},(3)}A_{\theta,il}^{(3)}
       +\sum_{i<l}s_i^{(3)}
                  (Z_i^{{\rm for},(3)})^T\theta_l^{(3)},\\
 \nu_l^{(2)}
 &=A_{\theta,ll}^{(3)}Z_l^{{\rm rev},(3)}
                 +\sigma\sum_{i<l}s_i^{(3)}\Lambda_{li}^{(3)}.
 \end{split}
 \tag{G.13}
\]
All coefficients and the first vector in (G.13) are measurable from
this past. The second vector is conditionally centered Gaussian with
\[
 \operatorname{Cov}(\nu_l^{(2)}\mid\text{past})
 =(A_{\theta,ll}^{(3)})^2 I_n
             +\sigma^2\sum_{i<l}s_i^{(3)}(s_i^{(3)})^T.
 \tag{G.14}
\]
This is a statement about joint conditional covariance, not iid
coordinates: the second term need not be diagonal.

The raw reverse output is \(m_l^{(2)}+\nu_l^{(2)}\). Including all
learned upper memory, the middle query is exactly
\[
 q_j^{(2)}
 =m_{j+2}^{(2)}+(M_j^{(3)})^T\delta_j^{(3)}
                    +\nu_{j+2}^{(2)}.
 \tag{G.15}
\]
There is no omission of the trained part of \(W^{(3)}\).

For \(T=N\eta\le S+1\), on the non-matrix initial event
\(\|W^{(4)}_0\|_\infty\le1\), bounded activation alone gives
\[
 \|W^{(4)}_j\|_\infty\le B_4:=1+(S+1)\pi/2,\qquad
 \|\delta_j^{(3)}\|_2/\sqrt n\le B_4.
 \tag{G.16}
\]
The Schur-complement diagonal satisfies
\[
 (A_{\theta,ll}^{(3)})^2
 \le\|\theta_l^{(3)}\|_2^2+\sigma^2\le B_4^2+\sigma^2.
\]
Together with (G.3), this gives the actual innovation bound
\[
 \operatorname{Cov}(\nu_l^{(2)}\mid\text{past})
       \preceq(B_4^2+2\sigma^2)I_n.
 \tag{G.17}
\]
For every coordinate \(i\), every real \(\lambda\), and every such
past, the Gaussian characteristic/density calculation therefore yields
\[
 \mathbb E[e^{\lambda\nu_{l,i}^{(2)}}\mid\text{past}]
 \le\exp\!\big((B_4^2+2\sigma^2)\lambda^2/2\big),
 \tag{G.18}
\]
and Markov's inequality optimized in \(\lambda\) gives, for \(x\ge0\),
\[
 \mathbb P(|\nu_{l,i}^{(2)}|>x\mid\text{past})
 \le2\exp\!\left(-\frac{x^2}{2(B_4^2+2\sigma^2)}\right).
 \tag{G.19}
\]
The constants are independent of clipping, mesh, filter scale and
query count for a fixed feature horizon and bounded \(\sigma\).
The initial event has probability at least \(1-2ne^{-n^2/2}\).

The learned term in (G.15) also has a pointwise bound:
\[
 (M_j^{(3)})^T\delta_j^{(3)}
 =\frac{\eta}{n}\sum_{r<j}h_r^{(2)}
                         (\delta_r^{(3)})^T\delta_j^{(3)},
\]
so, for every coordinate,
\[
 \left|[(M_j^{(3)})^T\delta_j^{(3)}]_i\right|
 \le (S+1)(\pi/2)B_4^2.
 \tag{G.20}
\]
This uses the actual trained update and actual bounded top backward
fields; it is not a frozen-weight replacement.

Conditional on the enlarged primitive past used in (G.13), the complete query
(G.15) is Gaussian with the displayed mean, including its learned term, and
innovation covariance (G.14). After averaging over that past it need not be
Gaussian. The mean \(m_l^{(2)}\) has no bound here: its coefficients depend on
earlier Gaussian outputs. Therefore (G.17)–(G.20) give neither unconditional
Gaussianity nor coordinate independence nor a clipping-uniform tail bound for
the complete query.
A union bound over all calls would also introduce the growing call
count; a fixed-call innovation tail is not a uniform path-tail theorem.

### 6. Consequence for canonical clipped trajectories

Take now exactly the parameters of fragments Q5–Q7:
\(\eta=n^{-2}\), \(N=\lceil Sn^2\rceil\),
\(\sigma=n^{-1/4}\), \(\varepsilon=n^{-1/8}\), and a prescribed
deterministic common map with cap \(R_n\ge1\), \(R_n=o(\log n)\).
Let the reference be the canonical CLIPPED finite-width feature flow
with the original independent Gaussian matrices and tiny readout.

Fragment Q7 gives a coupling of this reference with the
all-original perturbed algorithm whose mesh-state distance tends to
zero in probability, with good-event error \(n^{-1/24+o(1)}\).
The deterministic stability proof also gives, at each \(0\le j<N\),
\[
 \frac{\|\widehat q_j^{(2)}-q^{(2)}(s_j)\|_2}{\sqrt n}
 \le C_S\big(E_j+C_j\big)+b,
 \tag{G.21}
\]
where \(E_j\) is its slow-state error, \(C_j\) its layer-three error,
and \(b\) its raw query-error bound. Its constant is independent of
\(R_n\): only the subsequent middle gate subtraction introduces the
clipping factor. Thus the same coupling controls the state distance
augmented by the maximum of (G.21), still at rate
\(n^{-1/24+o(1)}\) on the good event.

Define this augmented distance as the sum of the mesh-state distance
in fragment Q7 and the maximum middle-query error over
\(j<N\), with ordinary vector norms divided by \(\sqrt n\) and
ordinary Frobenius norms for learned matrices. The non-matrix seeds
may also be retained as jointly identical coordinates.

For every test of these augmented arrays that is bounded in absolute
value by one and 1-Lipschitz for this distance, the difference between
its canonical-clipped expectation and its all-replacement expectation
is at most
\[
 n^{-1/24+o(1)}
 +2\big(4e^{-(8-2\log9)n}+2ne^{-n^2/2}+5n^{-2}\big).
 \tag{G.22}
\]
Indeed compare reference and all-original paths on the proved coupling.
On its good event the test difference is bounded by the distance;
on the complement it is at most two. Section 4 identifies the
all-original expectation with the all-replacement expectation exactly.
Constants can be absorbed into the \(o(1)\) exponent.
No unbounded test, uniform integrability, or exchange of limits is
needed for this conclusion.

Thus the replacement process gives a rigorously connected
finite-width Gaussian-array representation of the canonical CLIPPED
state and middle query on the full growing training mesh.
This does not imply convergence to a fixed population law as \(n\)
changes. In particular (G.22) does not carry conditional law statements
or arbitrary discontinuous tail indicators to the canonical flow.

The identity map is allowed in the exact finite law and innovation
bounds, but not in the canonical-clipped comparison (G.22).
This identity supplies no bound on the predictable response
\(m_l^{(2)}\), no uncut clipping removal, no population uniqueness or
autonomous restart, and no physical-time/exact-GD/kernel/velocity
convergence. These are separate mathematical conclusions.
