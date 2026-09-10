# Every fixed identity depth: uniform step doubling and local feature time

## 1. Scope, normalization, and the two limits

Fix an integer \(L\ge1\), independently of width and step count. There is
one input, \(d=m=1,x_1=1\), and every activation is the identity. All
blocks are trained. Write the stored endpoint vectors as \(U_n,A_n\in
\mathbb R^n\), and the stored connectors as \(B_{a,n}\in\mathbb
R^{n\times n}\), \(2\le a\le L\). Initially the endpoint entries are
independent \(N(0,1)\), the connector entries are independent
\(N(0,1/n)\), and all blocks are independent. The output is

\[
 f_n=\frac1n A_n^TB_{L,n}\cdots B_{2,n}U_n.
 \tag{IU1}
\]

An empty connector product is the identity. The raw parameter metric is

\[
 \frac{dA_n^Td\widetilde A_n}{n}
 +\frac{dU_n^Td\widetilde U_n}{n}
 +\sum_{a=2}^L\operatorname{Tr}
       (dB_{a,n}^Td\widetilde B_{a,n}).
 \tag{IU2}
\]

Thus its mobilities in stored coordinates are
\((n,1,\ldots,1,n)\). The updates below are simultaneous feature ascent
for \(f_n\). They contain no label, loss, or residual multiplier; their
step \(h\in\mathbb R\) is signed feature time.

For the finite proof representation put
\(u_n=U_n/\sqrt n, a_n=A_n/\sqrt n\). Define

\[
 x_{1,n}=u_n,\quad x_{a,n}=B_{a,n}x_{a-1,n},\qquad
 r_{L,n}=a_n,\quad r_{a-1,n}=B_{a,n}^Tr_{a,n}.
 \tag{IU3}
\]

All finite vector norms and pairings in this representation are ordinary
Euclidean ones. The exact Euler update is

\[
 \begin{split}
 a_n^+&=a_n+h x_{L,n},\\
 u_n^+&=u_n+h r_{1,n},\\
 B_{a,n}^+&=B_{a,n}+h r_{a,n}x_{a-1,n}^T,
                  \qquad 2\le a\le L.
 \end{split}
 \tag{IU4}
\]

All fields on the right are evaluated before any block is changed.
For example, the last line is the stored update
\(B_{a,n}^+=B_{a,n}+h\delta_{a,n}z_{a-1,n}^T/n\), with
\(\delta_{a,n}=\sqrt n\,r_{a,n}\) and
\(z_{a-1,n}=\sqrt n\,x_{a-1,n}\).

For each fixed integer \(N\ge0\) and fixed real \(h\), the width limit
of the output after \(N\) updates will be denoted \(F_{N,L}(h)\).
Section 3 proves its existence in probability and in every fixed finite
\(L^p\) over initialization. In particular it is also the limit of the
finite-width expected output. Only after taking this fixed-program
width limit do we let \(N\) increase and \(h\) decrease.

Here is the uniform estimate. Set \((d)_r=d(d-1)\cdots(d-r+1)\), with
\((d)_0=1\) and \((d)_r=0\) for \(r>d\), and define

\[
 K_L=\max\left\{1,\quad
  \max_{0\le r\le4}(L+1)(L)_r3^{L-r},\quad
  \max_{1\le r\le4}(L+1)_r3^{L+1-r}\right\}.
 \tag{IU5}
\]

Terms with zero falling factorial mean zero. In particular
\(K_1=6, K_2=27, K_3=108\). The explicit finite recurrence in
Section 5 defines \(C_K\) for every \(K\ge1\).

**Theorem IU.** For every integer \(t\ge1\) and
\(|h|\le1/(16K_Lt)\),

\[
 \left|F_{t,L}(2h)-F_{2t,L}(h)
 +\frac{t(2t-1)L(L+1)^2(L+2)}{3}h^3\right|
 \le C_{K_L}t^4|h|^5.
 \tag{IU6}
\]

The fixed-program limits are Euler iterates of the trace-class operator
state constructed below. On the signed interval
\(|T|\le T_L:=1/(8K_L)\) they converge, as the mesh decreases, to its
unique local feature-ascent flow, in the sum of the endpoint Hilbert
norms and connector trace norms. The convergence is uniform in feature
time on this interval. These statements hold for each separately fixed
\(L\); they assert neither a joint depth limit nor global feature-time
existence.

## 2. A fixed Hilbert source and a complete parameter space

The maintained dependency for the Gaussian identification is Section 9,
“A Gaussian source lemma with contained norm and Wick proofs,” of
`linear_dynamics.md`. Its hypotheses are exactly the independent
\(N(0,1/n)\) connectors and two independent \(N(0,I_n/n)\) endpoint
vectors in (IU3). It applies to any fixed finite number of labels and
to typed compatible words. We spell out the source it supplies.

Let \(\mathcal F\) be the real Hilbert space with orthonormal basis the
finite words on letters \(a,+\) and \(a,-\), \(2\le a\le L\), including
the empty word \(\Omega\). For \(L=1\), \(\mathcal F=\mathbb R\Omega\).
The creation map \(\ell_{a,\pm}\) prepends its letter. Its actual
Hilbert adjoint deletes that first letter when it matches, and otherwise
returns zero. On

\[
 \mathcal H=\mathcal F\oplus\mathcal F,
 \qquad U=(\Omega,0),\qquad A=(0,\Omega),
 \tag{IU7}
\]

put

\[
 \Gamma_a=(\ell_{a,+}+\ell_{a,-}^*)
               \oplus(\ell_{a,+}+\ell_{a,-}^*).
 \tag{IU8}
\]

Both roots have norm one; \(\|\Gamma_a\|\le2\), because a creation
map is an isometry and its adjoint has norm one. Each hidden layer has
a typed copy \(\mathcal H_a\) of \(\mathcal H\). The connector
\(\Gamma_a:\mathcal H_{a-1}\to\mathcal H_a\) uses label \(a\);
transpose actions use its actual adjoint. The two entire rooted word
subspaces are orthogonal and are preserved by every source action.
In the word formulas below, a creation map also denotes its diagonal
action on \(\mathcal H\) and on the indicated typed copies.

Explicitly, the Gaussian lemma says that for every fixed finite list of
initial compatible words \(P,Q\) and root choices \(i,j\in\{1,2\}\),

\[
 (P(B_n)g_{i,n})^TQ(B_n)g_{j,n}
 \longrightarrow
 \langle P(\Gamma)g_i,Q(\Gamma)g_j\rangle
 \quad\hbox{in probability},
 \tag{IU9}
\]

where \(g_{1,n}=u_n(0),g_{2,n}=a_n(0)\) and \(g_1=U,g_2=A\).
The cited section proves this by finite Wick pairings, the connected
graph count for the trace variance, Gaussian conditioning on the roots,
and the creation/annihilation word rule. Consequently (IU9) uses neither
a claim about arbitrary coordinate nonlinearities nor an unproved
simultaneous Gaussian-operator realization.

Write a current connector as \(B_a=\Gamma_a+P_a\), with
\(P_a\in\mathfrak S_1(\mathcal H_{a-1},\mathcal H_a)\). Here
\(\mathfrak S_1\) is the trace-class space: the trace norm is the sum of
the singular values. Section 2.A, “Compact operators and the complete
trace-norm space,” of `linear_dynamics.md` supplies its complete-space
construction, the inequalities

\[
 \|P\|\le\|P\|_{\mathfrak S_2}\le\|P\|_{\mathfrak S_1},
 \qquad
 \|v\otimes w\|_{\mathfrak S_1}=\|v\|\|w\|,
 \tag{IU10}
\]

and the operator ideal inequalities. The tensor convention is
\((v\otimes w)z=v\langle w,z\rangle\). In particular rank-one
increments belong to this complete space even though the fixed
\(\Gamma_a\) need not be compact.

Use the Banach space

\[
 \mathcal X_L=\mathcal H_L\oplus\mathcal H_1\oplus
   \bigoplus_{a=2}^L
       \mathfrak S_1(\mathcal H_{a-1},\mathcal H_a),
 \quad
 \|\theta\|_{\mathcal X_L}
 =\|a\|+\|u\|+\sum_{a'=2}^L\|P_{a'}\|_{\mathfrak S_1}.
 \tag{IU11}
\]

Its initial state is \(\theta_0=(A,U,0,\ldots,0)\). Define

\[
 \begin{aligned}
 x_1&=u,&x_a&=B_ax_{a-1},\\
 r_L&=a,&r_{a-1}&=B_a^*r_a,\\
 f(\theta)&=\langle a,x_L\rangle,&
 g(\theta)&=(x_L,r_1,(r_a\otimes x_{a-1})_{a=2}^L).
 \end{aligned}
 \tag{IU12}
\]

The notation \(a\) for the endpoint in this formula is distinct from
an integer connector index. All population norms and pairings are the
displayed Hilbert and operator ones. These representatives describe
normalized rooted geometry, rather than individual neuron coordinates.

The maps \(f:\mathcal X_L\to\mathbb R\) and
\(g:\mathcal X_L\to\mathcal X_L\) are continuous polynomials. On
the unit ball about \(\theta_0\), endpoint norms are at most two and
connector operator norms at most three. Each of the \(L+1\) components
of \(g\) is a product with exactly \(L\) parameter factors; \(f\) has
\(L+1\). In each product a block occurs at most once. Differentiating
\(r\) times assigns the ordered differentiated factors in at most
\((L)_r\), respectively \((L+1)_r\), ways. Every direction component is
bounded by its \(\mathcal X_L\) norm; for a matrix output use (IU10).
It follows, in the multilinear operator norms induced by (IU11), that

\[
 \|D^rg(\theta)\|\le(L+1)(L)_r3^{L-r},\qquad
 \|D^rf(\theta)\|\le(L+1)_r3^{L+1-r}.
 \tag{IU13}
\]

The first bound is for \(0\le r\le4\), the second for \(1\le r\le4\).
This proves all the hypotheses represented by \(K_L\) in (IU5).

For gradient identities only, replace the trace-class factors by
Hilbert--Schmidt factors and the sum norm by the Hilbert direct-sum
norm; call the resulting Hilbert space \(\mathcal Y_L\). The same
products are continuous polynomials there because operator norm is
bounded by Hilbert--Schmidt norm. The reverse chain rule gives

\[
 Df(\theta)[v]=\langle g(\theta),v\rangle_{\mathcal Y_L}.
 \tag{IU14}
\]

For example, the connector derivative is
\(\langle r_a,\dot P_ax_{a-1}\rangle\), whose
Hilbert--Schmidt representative is \(r_a\otimes x_{a-1}\).
Thus (IU14) is a gradient identity on a Hilbert space; it is not an
identification of the Banach trace norm with a Hilbert metric.

## 3. Identification of every fixed Euler program

Let \(E_h\theta=\theta+h g(\theta)\). We prove

\[
 F_{N,L}(h)=f(E_h^N\theta_0).
 \tag{IU15}
\]

At every fixed finite step, expand each learned connector into its
initial connector plus the finite sum of rank-one updates. Applying
such an increment to a vector replaces that action by a scalar inner
product times a previously generated vector. Induction over the finite
forward, backward, and update operations therefore expresses every
generated vector as a finite sum of initial rooted words. Its scalar
coefficients are polynomials in a finite list of initial rooted Gram
entries. The list and polynomial degrees can depend on \(L,N,h\), but
are finite and independent of \(n\). No Gram inverse is used. The same
expansion is valid with the fixed \(\Gamma_a,U,A\). Applying (IU9) and
continuity to these finite polynomials proves convergence in probability
of every scalar contraction in the program, including its terminal
output, to the value in (IU15).

For completeness this also gives convergence of expected outputs; no
unjustified passage from probability to expectation is needed. The
Gaussian net argument in Section 9 of `linear_dynamics.md`, with its
threshold left variable, gives

\[
 \mathbb P\{\|B_{a,n}(0)\|>y\}
 \le2\exp(n\log81-ny^2/8).
 \tag{IU16}
\]

Indeed the same \(1/4\)-net has at most \(9^n\) points, the norm is
at most twice the largest net bilinear form, and each such form is
\(N(0,1/n)\). For \(y^2\ge16\log81\), the right side is at most
\(2e^{-y^2/16}\), uniformly in \(n\ge1\). Integrating this tail gives
uniform bounds for every finite moment of the initial connector norms.
For a normalized Gaussian endpoint and integer \(p\ge1\), convexity
gives

\[
 \mathbb E\|u_n(0)\|^{2p}
 =\mathbb E\left(\frac1n\sum_{i=1}^n U_{n,i}^2\right)^p
 \le\mathbb E|G|^{2p}<\infty,
 \qquad G\sim N(0,1).
 \tag{IU17}
\]

The same holds for \(a_n(0)\). At a finite step put

\[
 M_k=1+\|u_{n,k}\|+\|a_{n,k}\|
            +\sum_{a=2}^L\|B_{a,n,k}\|.
\]

The rank-one norm formula and (IU4) imply

\[
 M_{k+1}\le M_k+|h|(L+1)M_k^L,
 \qquad |f_{n,k}|\le M_k^{L+1}.
 \tag{IU18}
\]

At fixed \(N,h\), iteration gives a finite polynomial bound in \(M_0\)
with nonnegative coefficients. Equations (IU16)--(IU18) consequently
bound every finite moment of the output uniformly in width. Convergence
in probability to (IU15), followed by truncation and a higher moment
bound for the tails, proves convergence in every finite \(L^p\), in
particular \(L^1\). The same reasoning applies to each fixed program
scalar or vector Gram entry.

There is also an operator-state interpretation of this identification.
Each learned connector after \(N\) steps is the sum of \(N\) outer
products \(h r_{a,k}\otimes x_{a-1,k}\). All Gram entries of this fixed
list converge. For a finite-rank map \(VCW^*\), its nonzero squared
singular values are those of
\(G_V^{1/2}CG_WC^*G_V^{1/2}\), where \(G_V=V^*V,G_W=W^*W\).
Continuity of the positive square root and of the eigenvalues of a
finite symmetric matrix proves convergence of each singular value and
of the trace norm. This statement does not compare vectors from
different widths in a common norm. It identifies their fixed finite
rooted geometry with the unique state \(E_h^N\theta_0\in\mathcal X_L\).

Finally, the finite program is odd in the common step after averaging.
Let \(S\) negate only the readout endpoint. Directly from (IU12),

\[
 f(S\theta)=-f(\theta),\qquad
 Sg(\theta)=-g(S\theta),\qquad
 SE_h=E_{-h}S.
 \tag{IU19}
\]

The law of the finite initial state is invariant under \(S\); its
expected output is therefore odd in \(h\). The \(L^1\) identification
just proved yields

\[
 F_{N,L}(-h)=-F_{N,L}(h).
 \tag{IU20}
\]

This argument uses symmetry of the initial law; it does not assert
that the deterministic representative \(\theta_0\) is fixed by \(S\).

## 4. The identity cubic coefficient from orthogonal words

All quantities in this section are evaluated at \(\theta_0\) unless an
argument is displayed. Write \(g_0=g(\theta_0)\),

\[
 H_0^{\rm vec}=Dg[g_0],\qquad
 K_0^{\rm vec}=Dg[H_0^{\rm vec}],\qquad
 R_0^{\rm vec}=D^2g[g_0,g_0],
 \quad
 S_0=D^3f[g_0,g_0,g_0],\quad
 H_0^{\rm sc}=\|H_0^{\rm vec}\|_{\mathcal Y_L}^2.
 \tag{IU21}
\]

These temporary scalar and vector names will not be used for the
majorants in the next section. Symmetry of the derivatives of the
Hilbert gradient (IU14) gives

\[
 Df[K_0^{\rm vec}]=H_0^{\rm sc},\qquad
 D^2f[H_0^{\rm vec},g_0]=H_0^{\rm sc},\qquad
 Df[R_0^{\rm vec}]=S_0.
 \tag{IU22}
\]

For example, the first equality is
\(\langle g_0,Dg[H_0^{\rm vec}]\rangle
=\langle Dg[g_0],H_0^{\rm vec}\rangle\), since \(Dg\) is
self-adjoint on \(\mathcal Y_L\). The third is the differentiated
gradient identity.

Let \(\theta_N(h)=E_h^N\theta_0\). At zero step all its intermediate
states equal \(\theta_0\). Differentiating its recurrence successively
and summing gives

\[
 \begin{split}
 \theta_N'(0)&=Ng_0,\\
 \theta_N''(0)&=N(N-1)H_0^{\rm vec},\\
 \theta_N'''(0)&=6\binom N3K_0^{\rm vec}
       +\frac{N(N-1)(2N-1)}2R_0^{\rm vec}.
 \end{split}
 \tag{IU23}
\]

To check the last sum, its increment at step \(k\) is
\(3k(k-1)K_0^{\rm vec}+3k^2R_0^{\rm vec}\); sum over
\(0\le k<N\). The third scalar chain rule and (IU22) now give

\[
 F_{N,L}'''(0)
 =\frac{N(4N^2-3N+1)}2S_0
     +2N(N-1)(2N-1)H_0^{\rm sc}.
 \tag{IU24}
\]

It remains to calculate just \(S_0,H_0^{\rm sc}\) for the explicit
source. At initialization the forward and reverse vectors are unit
words

\[
 X_a=\ell_{a,+}\cdots\ell_{2,+}U,\qquad
 R_a=\ell_{a+1,-}\cdots\ell_{L,-}A.
 \tag{IU25}
\]

The factors absent at an endpoint are identities. The equality with
the forward and backward recursion follows because distinct labels
cannot annihilate the first letter in these words. They lie in the
orthogonal \(U\)- and \(A\)-rooted sectors, respectively.

Consider the straight parameter line \(\theta_0+s g_0\). Its connector
increment is \(s(R_a\otimes X_{a-1})\), which maps the \(U\)-sector
into the \(A\)-sector and annihilates the \(A\)-sector. Source connectors
preserve both sectors. Thus two such increments in a forward product
give zero; an increment applied after the endpoint variation \(sR_1\)
also gives zero. The forward state on this line is exactly

\[
 x_a(s)=X_a+sV_a,\qquad
 V_1=R_1,\quad V_a=\Gamma_aV_{a-1}+R_a,
 \tag{IU26}
\]

where \(V_a\) belongs to the \(A\)-sector. The readout is \(A+sX_L\).
Orthogonality implies that
\(\langle A+sX_L,X_L+sV_L\rangle\) is linear in \(s\).
Consequently

\[
 S_0=0.
 \tag{IU27}
\]

We next evaluate the norms in (IU26), retaining the returns created
by reuse of the same connector. For \(1\le k\le a\), set

\[
 e_{a,k}=\ell_{a,+}\cdots\ell_{k+1,+}R_k.
 \tag{IU28}
\]

When \(k=a\), this is \(R_a\). These are distinct unit words in the
\(A\)-sector, hence orthonormal. For \(k<a-1\), applying \(\Gamma_a\)
to \(e_{a-1,k}\) merely creates its first \(a,+\) letter and yields
\(e_{a,k}\). For the last word,

\[
 \Gamma_aR_{a-1}=e_{a,a-1}+R_a,
 \tag{IU29}
\]

because the annihilator deletes its initial \(a,-\). Induction in
(IU26) proves

\[
 V_a=\sum_{k=1}^a k e_{a,k},\qquad
 \|V_a\|^2=\sum_{k=1}^a k^2.
 \tag{IU30}
\]

The reverse variation on the same straight line obeys

\[
 T_L=X_L,\qquad T_{a-1}=\Gamma_a^*T_a+X_{a-1}.
 \tag{IU31}
\]

Indeed the derivative of \(B_a^*r_a\) adds
\((X_{a-1}\otimes R_a)R_a=X_{a-1}\). For an explicit orthogonal
expansion, define

\[
 \widetilde e_{a,j}=\ell_{a+1,-}\cdots\ell_{j,-}X_j,
                         \qquad a\le j\le L.
\]

These are distinct \(U\)-sector unit words. The creation term of
\(\Gamma_a^*\) prepends \(a,-\), while its annihilation term deletes
the initial \(a,+\) of \(X_a\). Exactly as in (IU29), the last return
adds to the direct \(X_{a-1}\) term. Backward induction in (IU31)
therefore gives

\[
 T_a=\sum_{j=a}^L(L-j+1)\widetilde e_{a,j},\qquad
 \|T_a\|^2=\sum_{q=1}^{L-a+1}q^2.
 \tag{IU32}
\]

The endpoint components of \(Dg[g_0]\) are \(V_L,T_1\); its connector
component is

\[
 T_a\otimes X_{a-1}+R_a\otimes V_{a-1}.
 \tag{IU33}
\]

The two terms are Hilbert--Schmidt orthogonal, since their range
vectors belong to orthogonal root sectors. Their squared norms are
\(\|T_a\|^2\) and \(\|V_{a-1}\|^2\), since \(X_{a-1},R_a\)
are unit vectors. Equations (IU30)--(IU33) yield

\[
 \begin{split}
 H_0^{\rm sc}
 &=\|V_L\|^2+\|T_1\|^2
      +\sum_{a=2}^L(\|T_a\|^2+\|V_{a-1}\|^2)\\
 &=2\sum_{q=1}^L(L-q+1)q^2
   =\frac{L(L+1)^2(L+2)}6.
 \end{split}
 \tag{IU34}
\]

For the last equality expand the sum as
\(2[(L+1)\sum q^2-\sum q^3]\), and use
\(\sum_{q=1}^Lq^2=L(L+1)(2L+1)/6\) and
\(\sum_{q=1}^Lq^3=L^2(L+1)^2/4\); both identities follow by
induction on \(L\).

Subtracting the two cubic coefficients in (IU24), including the
factor \(2^3\) for the coarse step, proves

\[
 \begin{split}
 \frac{8F_{t,L}'''(0)-F_{2t,L}'''(0)}6
 &=-\frac{t(2t-1)}2(S_0+4H_0^{\rm sc})\\
 &=-\frac{t(2t-1)L(L+1)^2(L+2)}3.
 \end{split}
 \tag{IU35}
\]

This derivation is specific to the identity activation and the stated
independent Gaussian initialization.

## 5. The explicit uniform transported-defect theorem

We prove the numerical estimate on a Banach space, so that its dependence
on the step count is visible. Let \(f\in C^4(\mathcal X;\mathbb R)\),
\(g\in C^4(\mathcal X;\mathcal X)\), and suppose on the unit ball about
\(\theta_0\) that

\[
 \|D^rg\|\le K\quad(0\le r\le4),\qquad
 \|D^rf\|\le K\quad(1\le r\le4),\qquad K\ge1.
 \tag{IU36}
\]

It suffices that the maps be defined on a neighborhood of the ball.
Put \(E_hx=x+hg(x)\), \(C_h=E_{2h}\), and \(B_h=E_h^2\). Suppose
\(d_t(h)=f(C_h^t\theta_0)-f(B_h^t\theta_0)\) is odd in \(h\).
For \(c=1/(16K)\), the following finite recurrence defines the constant.
The letters in this recurrence are numerical majorants only:

\[
 \begin{split}
 X_1&=8K,\\
 X_2&=2\{8KX_1+4cKX_1^2\},\\
 X_3&=2\{12K(X_1^2+X_2)+4cK(X_1^3+3X_1X_2)\},\\
 G_0&=K,\quad G_1=KX_1,\quad G_2=K(X_2+X_1^2),\\
 G_3&=K(X_3+3X_1X_2+X_1^3),\\
 A_r&=\sum_{q=0}^r\binom rqG_qG_{r-q}\quad(0\le r\le3),\\
 A_{-1}&=A_{-2}=0,\\
 Z_r&=X_r+c^2A_r+2rcA_{r-1}+r(r-1)A_{r-2}
                                      \quad(1\le r\le3),\\
 T_1&=2(Z_1+2K),\\
 T_2&=2\{Z_2+4KT_1+2cKT_1^2\},\\
 T_3&=2\{Z_3+6K(T_1^2+T_2)+2cK(T_1^3+3T_1T_2)\},\\
 H_0&=K,\quad H_1=KT_1,\quad H_2=K(T_2+T_1^2),\\
 H_3&=K(T_3+3T_1T_2+T_1^3).
 \end{split}
 \tag{IU37}
\]

Starting with \(W_0=2A_0\), define successively for \(r=1,2,3\),

\[
 W_r=2\left\{A_r
 +2c\sum_{q=1}^r\binom rqH_qW_{r-q}
 +2r\sum_{q=0}^{r-1}\binom{r-1}qH_qW_{r-1-q}\right\},
 \qquad
 C_K=\frac16\sum_{q=0}^3\binom3qH_qW_{3-q}.
 \tag{IU38}
\]

All indices are fixed finite ranges; these formulas terminate and
produce a number depending only on \(K\).

**Transported-defect estimate.** Under (IU36) and the oddness assumption,
for \(t\ge1, |h|\le c/t\),

\[
 \left|d_t(h)-\frac{d_t'''(0)}6h^3\right|
 \le C_Kt^4|h|^5.
 \tag{IU39}
\]

**Proof.** The exact local defect, with no Taylor truncation, is

\[
 B_hx=C_hx+h^2a_h(x),\qquad
 a_h(x)=\int_0^1Dg(x+s h g(x))[g(x)]\,ds.
 \tag{IU40}
\]

For a scalar map \(v\), write \(P_Mv=v\circ M\), and set

\[
 R_hv(x)=-\int_0^1
 Dv(C_hx+s h^2a_h(x))[a_h(x)]\,ds.
 \tag{IU41}
\]

Then \(P_{C_h}-P_{B_h}=h^2R_h\). The noncommutative telescoping
identity \(A^t-B^t=\sum_{j=0}^{t-1}A^{t-1-j}(A-B)B^j\) gives

\[
 d_t(h)=h^2Q_t(h),\qquad
 Q_t(h)=\sum_{j=0}^{t-1}
   (P_{C_h}^{t-1-j}R_hP_{B_h}^jf)(\theta_0).
 \tag{IU42}
\]

For each summand this means: first take \(t-1-j\) coarse steps,
then one coarse step and interpolate across its local defect, then
take \(2j\) fine steps, transporting the tangent direction
\(a_h(x)\) through these last fine steps. The order in (IU42) is
essential and follows from the displayed operator identity.

We give bounds for all its parameter derivatives through order three.
Consider any variable-step path from \(\theta_0\) of the form

\[
 x_{m+1}=x_m+\alpha_mh g(x_m),\qquad
 0\le\alpha_m\le2,\qquad \sum_m\alpha_m\le4t.
 \tag{IU43}
\]

As long as it lies in the unit ball its displacement is at most
\(K|h|\sum_m\alpha_m\le4cK=1/4\). The same bound at the first
putative exit rules out that exit. All interpolation points in (IU40)
are further variable-step points. In (IU41), the extra displacement is
at most \(|h|^2K^2\le c^2K^2=1/256\). The trajectory before that
point uses at most \(2t\) Euler weight and the trajectory after it uses
at most \(2t\); their total displacement is bounded by
\(1/4+1/256<1\). A first-exit argument again justifies using (IU36)
everywhere in (IU40)--(IU42), also for negative \(h\).

Primes now denote differentiation in \(h\). With all \(g\)-derivatives
evaluated at \(x_m\), differentiating one step of (IU43) gives

\[
 \begin{split}
 x_{m+1}'&=(I+\alpha_mhDg)x_m'+\alpha_mg,\\
 x_{m+1}''&=(I+\alpha_mhDg)x_m''
       +2\alpha_mDg[x_m']+\alpha_mhD^2g[x_m',x_m'],\\
 x_{m+1}'''&=(I+\alpha_mhDg)x_m'''
       +3\alpha_m\{D^2g[x_m',x_m']+Dg[x_m'']\}\\
 &\hspace{18mm}+\alpha_mh\{D^3g[x_m',x_m',x_m']
                                      +3D^2g[x_m',x_m'']\}.
 \end{split}
 \tag{IU44}
\]

The product of any consecutive homogeneous factors has norm at most

\[
 \prod_m(1+\alpha_m|h|K)
 \le\exp(K|h|\sum_m\alpha_m)\le e^{4cK}<2.
 \tag{IU45}
\]

Iterating each affine recurrence in (IU44) bounds it by twice the sum
of its inhomogeneous terms. Divide the derivative of order \(r\) by
\(t^r\) and use \(\sum\alpha_m/t\le4, |h|t\le c\).
The first derivative is at most \(8K t=X_1t\). The second derivative
is at most twice
\((8KX_1+4cKX_1^2)t^2\). The third derivative is at most twice
\(\{12K(X_1^2+X_2)+4cK(X_1^3+3X_1X_2)\}t^3\).
These are exactly the first three recurrences in (IU37); hence

\[
 \sup_m\|x_m^{(r)}\|\le X_rt^r\quad(1\le r\le3).
 \tag{IU46}
\]

For \(a_h(x(h))\) in (IU40), both \(x(h)\) and
\(x(h)+s h g(x(h))\) are paths covered by (IU46). In the actual
telescoping expression their total Euler weights, including this extra
coefficient \(s\in[0,1]\), are less than \(4t\). The chain rule for
\(g(x(h))\) and \(Dg(x(h)+s h g(x(h)))\), through order three,
gives respectively the four bounds \(G_rt^r\) in (IU37). For the
second function this uses \(D^{r+1}g\), so \(D^4g\) is indeed needed.
Leibniz's rule, followed by integration over a unit interval, gives

\[
 \left\|\frac{d^r}{dh^r}a_h(x(h))\right\|
 \le A_rt^r\quad(0\le r\le3).
 \tag{IU47}
\]

For the interpolation in (IU41), its base \(C_hx(h)\) is also a
path covered by (IU46). Since

\[
 (h^2a_h)^{(r)}=h^2a_h^{(r)}+2rh a_h^{(r-1)}
                              +r(r-1)a_h^{(r-2)},
\]

the interpolated initial point of the remaining fine path has derivative
norm at most \(Z_rt^r\), using \(|h|t\le c\) and \(t\ge1\) to enlarge
the bounds. Apply (IU44) to at most \(2t\) fine microsteps, now with
these nonzero initial derivatives. The homogeneous product is still
less than two. At first order this gives \(T_1=2(Z_1+2K)\).
At second and third order the inhomogeneous sums give precisely the
\(T_2,T_3\) in (IU37). Thus the final and intermediate post-interpolation
states \(z(h)\) satisfy

\[
 \|z^{(r)}(h)\|\le T_rt^r\quad(1\le r\le3).
 \tag{IU48}
\]

By the chain rule, derivatives through order three of \(Dg(z(h))\)
and \(Df(z(h))\) have norms at most \(H_rt^r\) with \(H_r\) from
(IU37). The latter bound uses \(D^4f\).

It remains to bound the transported tangent \(w(h)\), initially
\(a_h(x(h))\). A fine step has tangent recurrence

\[
 w^+=w+hDg(z)w.
 \tag{IU49}
\]

Writing \(Dg(z)^{(q)}\) for its total derivative in \(h\), the exact
Leibniz formula is

\[
 \begin{split}
 (w^+)^{(r)}=w^{(r)}
 &+h\sum_{q=0}^r\binom rqDg(z)^{(q)}w^{(r-q)}\\
 &+r\sum_{q=0}^{r-1}\binom{r-1}q
                         Dg(z)^{(q)}w^{(r-1-q)}.
 \end{split}
 \tag{IU50}
\]

The \(q=0\) term in the first sum is the homogeneous factor.
Its product is bounded by (IU45). For \(r=0\), (IU47) therefore
gives \(\|w\|\le2A_0=W_0\). Inductively suppose the lower
derivatives satisfy \(\|w^{(q)}\|\le W_qt^q\). Sum the other
terms of (IU50) over at most \(2t\) fine steps, divide by \(t^r\),
and use \(|h|t\le c\). The first sum contributes at most
\(2c\sum_{q=1}^r\binom rqH_qW_{r-q}\); the second contributes
\(2r\sum_{q=0}^{r-1}\binom{r-1}qH_qW_{r-1-q}\).
The initial derivative is bounded by \(A_rt^r\). Multiplication by
the homogeneous bound two is exactly (IU38), so

\[
 \|w^{(r)}\|\le W_rt^r\quad(0\le r\le3).
 \tag{IU51}
\]

The scalar integrand of each transported defect is \(Df(z)[w]\).
A final Leibniz rule gives

\[
 \left|\frac{d^3}{dh^3}\bigl(Df(z(h))[w(h)]\bigr)\right|
 \le t^3\sum_{q=0}^3\binom3qH_qW_{3-q}=6C_Kt^3.
 \tag{IU52}
\]

Differentiation under the interpolation integral is justified by these
continuous, uniformly bounded derivatives on its compact interval.
There are exactly \(t\) defects, so

\[
 \sup_{|h|\le c/t}|Q_t'''(h)|\le6C_Kt^4.
 \tag{IU53}
\]

The expression (IU42) defines \(Q_t\in C^3\) also at zero. Because
\(d_t=h^2Q_t\) is odd, \(Q_t\) is odd, and consequently
\(Q_t(0)=Q_t''(0)=0\). The integrated third-order Taylor identity is

\[
 Q_t(h)-Q_t'(0)h
 =\frac12\int_0^h(h-s)^2Q_t'''(s)\,ds.
 \tag{IU54}
\]

Also \(Q_t'(0)=d_t'''(0)/6\), directly from \(d_t=h^2Q_t\).
Taking absolute values in (IU54), including negative \(h\), and
multiplying by \(h^2\) proves (IU39). This argument removes the exact
factor \(h^2\) before differentiating: three derivatives of each of
\(t\) local defects give \(t^4\). It uses no fifth derivative of an
unknown limiting output. \(\square\)

Apply (IU39) to the complete space (IU11), using (IU13), the parity
(IU20), and the explicit coefficient (IU35). This proves (IU6).

## 6. The unique local operator-state flow

Let \(K=K_L, T_L=1/(8K)\). We construct the solution of

\[
 \dot\theta(T)=g(\theta(T)),\qquad \theta(0)=\theta_0,
 \quad |T|\le T_L,
 \tag{IU55}
\]

in the Banach space (IU11). On continuous paths with
\(\sup_{|T|\le T_L}\|\theta(T)-\theta_0\|_{\mathcal X_L}\le1/2\),
the map

\[
 (\mathcal P\theta)(T)=\theta_0+\int_0^Tg(\theta(s))\,ds
 \tag{IU56}
\]

maps into the radius-\(1/8\) path ball. The integral is the Banach
integral of a continuous function, obtained by limits of Riemann sums
in the complete space. The mean-value integral and (IU13) bound the
Lipschitz constant of \(g\) on the convex unit ball by \(K\).
Consequently \(\mathcal P\) contracts the supremum path distance by
at most \(KT_L=1/8\). Iteration is a geometric Cauchy sequence in
the closed complete path ball, its limit is a fixed point, and the
same contraction proves uniqueness there. The fundamental theorem for
the continuous integral makes the limit \(C^1\) and proves (IU55).
Any other solution starting at \(\theta_0\) cannot leave the radius
\(1/2\) ball on this interval: before a first exit its displacement is
at most \(K|T|\le1/8\). Thus uniqueness has no extra path-ball
hypothesis for solutions on the stated interval.

In components this is the autonomous operator system

\[
 \dot a=x_L,\qquad \dot u=r_1,\qquad
 \dot P_a=r_a\otimes x_{a-1}\quad(2\le a\le L),
 \tag{IU57}
\]

with fields recomputed by (IU12). In particular its readout satisfies

\[
 \frac{d}{dT}f(\theta(T))
 =\|x_L\|^2+\|r_1\|^2
     +\sum_{a=2}^L\|r_a\|^2\|x_{a-1}\|^2.
 \tag{IU58}
\]

This is feature time for the metric (IU2); no physical-loss clock is
part of this construction.

For an explicit convergence argument, first take the positive uniform
grid \(h=T_L/m\). All Euler iterates through step \(m\) lie within
distance \(Kmh\le1/8\) of \(\theta_0\), by the same first-exit
argument. The local integral defect of the exact flow is bounded by

\[
 \left\|\theta(T+h)-\theta(T)-h g(\theta(T))\right\|
 \le\int_0^h K\|\theta(T+s)-\theta(T)\|\,ds
 \le K^2h^2/2.
 \tag{IU59}
\]

If \(e_k=\|E_h^k\theta_0-\theta(kh)\|\), then

\[
 e_{k+1}\le(1+Kh)e_k+K^2h^2/2,
 \qquad
 e_k\le\frac{Kh}{2}\{(1+Kh)^k-1\}
       \le\frac{Kh}{2}(e^{KT_L}-1).
 \tag{IU60}
\]

For negative time apply the same argument to the field \(-g\), or
replace \(h\) by \(|h|\) in the error recurrence. Linear interpolation
between Euler states changes the comparison by at most \(2K|h|\):
both the Euler segment and the exact flow move by at most \(K|h|\).
Thus the piecewise linear Euler paths on the positive and negative
grids converge uniformly on \([-T_L,T_L]\) in \(\mathcal X_L\).
The same estimate with \(h=T/m\) proves

\[
 E_{T/m}^m\theta_0\longrightarrow\theta(T)
                  \quad\hbox{in }\mathcal X_L,
             \qquad |T|\le T_L.
 \tag{IU61}
\]

By (IU15), these are precisely the operator representatives obtained
after the width limit for each fixed \(m,T/m\). The output and every
fixed polynomial contraction of the fields converge along this mesh
limit by continuity. The connector convergence in (IU61) is trace-norm
convergence in the fixed population spaces. No uniform-in-width bound
with a growing number of finite-width steps is asserted.

## 7. The scalar dyadic consequence

There is a useful summability statement directly from the sharper
step-doubling estimate. For \(|T|\le T_L\), put
\(G_t(T)=F_{t,L}(T/t)\), and abbreviate
\(D_L=L(L+1)^2(L+2)\). In (IU6) take \(h=T/(2t)\), which meets
its radius condition. Since \(t(2t-1)\le2t^2\),

\[
 |G_{2t}(T)-G_t(T)|
 \le\frac1t\left\{\frac{D_L|T|^3}{12}
                      +\frac{C_{K_L}|T|^5}{32}\right\}.
 \tag{IU62}
\]

The sum over \(t,2t,4t,\ldots\) is finite, uniformly for \(T\) on the
stated compact interval. Hence the scalar dyadic approximations are
uniformly Cauchy, with the explicit tail estimate

\[
 \left|f(\theta(T))-G_t(T)\right|
 \le\frac2t\left\{\frac{D_L|T|^3}{12}
                      +\frac{C_{K_L}|T|^5}{32}\right\}.
 \tag{IU63}
\]

The identification of the limit in (IU63) uses the already proved
operator-state convergence (IU61). Scalar summability by itself would
not supply existence or uniqueness of that state flow.

## 8. Boundary: bounded slopes do not give energy-ball activation stability

The positive theorem above uses the identity activation. A distinct
finite-dimensional obstruction explains why bounded activation slopes
alone cannot replace its polynomial Banach estimates.

Consider two hidden layers, one input \(x_1=1\), stored endpoint vectors
\(u,a\in\mathbb R^n\), and stored connector \(M\). For a common
activation \(\psi\), let

\[
 H=\psi(u),\qquad z=MH,\qquad
 f_\psi=\frac1n a^T\psi(z).
 \tag{IU64}
\]

Use the same raw metric as (IU2), so all blocks undergo simultaneous
feature ascent. Its first bottom Euler update, evaluated at the old
state, is exactly

\[
 u^+=u+h\,\psi'(u)\odot
             M^T\bigl(a\odot\psi'(M\psi(u))\bigr).
 \tag{IU65}
\]

Here \(\odot\) is coordinatewise multiplication. Define a distance
between activations by

\[
 d_1(\psi,\widetilde\psi)
 =\sup_{x\in\mathbb R}
       \frac{|\psi(x)-\widetilde\psi(x)|}{1+|x|}
       +\|\psi'-\widetilde\psi'\|_\infty.
 \tag{IU66}
\]

Take

\[
 \psi(x)=x+\arctan x,\qquad
 \widetilde\psi_n(x)=\psi(x)+n^{-1/2},\qquad
 u=0,\quad a=\sqrt n\,e_1,\quad
 M=\frac{e_1\mathbf1^T}{\sqrt n}.
 \tag{IU67}
\]

Both activations are smooth with the same positive slope
\(\psi'(x)=1+(1+x^2)^{-1}\in(1,2]\), and uniform linear-growth
and derivative bounds. Their distance is exactly \(n^{-1/2}\).
The initial energy quantities are fixed:

\[
 \frac{\|u\|_2}{\sqrt n}=0,\qquad
 \frac{\|a\|_2}{\sqrt n}=1,\qquad
 \|M\|_{\mathrm{op}}=1,\qquad
 1+\frac{\|u\|_2+\|a\|_2}{\sqrt n}+\|M\|_{\mathrm{op}}=3.
 \tag{IU68}
\]

For \(\psi\), \(H=z=0\); hence
\(M^T(a\odot\psi'(z))=2\mathbf1\) and
\(u^+=4h\mathbf1\). For \(\widetilde\psi_n\),
\(\widetilde H=n^{-1/2}\mathbf1\) and
\(\widetilde z=e_1\). The only coordinate selected by \(a\) has
\(\psi'(1)=3/2\), so

\[
 M^T(a\odot\widetilde\psi_n'(\widetilde z))
       =\tfrac32\mathbf1,\qquad
 \widetilde u^+=3h\mathbf1,\qquad
 \frac{\|\widetilde u^+-u^+\|_2}{\sqrt n}=|h|.
 \tag{IU69}
\]

Consequently, for any fixed nonzero feature step \(h\), no finite
constant depending only on the displayed energy bound, that step, and
the common activation bounds can control this first state difference
by \(d_1(\psi,\widetilde\psi_n)\), uniformly over widths and all states
in that energy ball. In particular a bound of the form
\(d_1 P(3)\), with a width-independent polynomial \(P\), tends to zero
and contradicts (IU69).

The failure occurs in the product of the readout and a slope difference.
The latter has Euclidean norm divided by \(\sqrt n\) of order
\(n^{-1/2}\), while multiplication by the concentrated readout makes
that norm order one. The connector operator-norm bound does not
remove this product.

This is a deterministic statement on an energy ball with a
width-dependent activation perturbation. It supplies no assertion
about Gaussian-typical initial states, expected-output continuity, or
a single final bounded-slope activation's uniform time remainder.
An averaged stability statement needs its own probabilistic argument.
