## 8. Quantitative step doubling for the exact fixed-program limit

This section uses the fixed-program width theorem in Section 5 at its
stated scope and supplies the additional finite-order calculus. Its
conclusion concerns separately fixed integers \(L,N\), with width sent
to infinity at each fixed nonzero feature-ascent step before the two
population outputs are compared. It supplies an exact Gaussian-integral
formula for the cubic coefficient and a fully explicit fifth-order
remainder. The number of steps does not grow in any limit here.

### 8.1. Model, coefficient, and quantitative statement

Use exactly the one-input, one-sample network, independent initialization,
and simultaneous stored-parameter updates (5.2.1)--(5.2.8). In particular,
\(m=d=1\), \(x_1=1\), the stored readout has independent \(N(0,1)\)
coordinates, and the mobility matrix in stored coordinates is
\(D_n=\operatorname{diag}(nI,I,\ldots,I,nI)\). There is no residual or
loss in these feature-ascent updates. The scalar \(h\) below is the
feature-ascent step of Section 5. It is not physical training time \(t\),
a loss-GD step \(\eta_n\), or the proof mesh \(\Delta\). The index
\(k\) always counts updates; the hidden features retain their layer
superscripts \(h^{(\ell)}\) and \(H^{(\ell)}\).

Strengthen the activation hypothesis to
\[
 \phi\in C^{12}(\mathbb R),\qquad E\phi(G)^2=1,
 \qquad G\sim N(0,1),                                      \tag{8.1.1}
\]
\[
 M_\phi=\max\left\{1,\sup_x\frac{|\phi(x)|}{1+|x|},
       \max_{1\le j\le12}\|\phi^{(j)}\|_\infty\right\}<\infty,
 \qquad B_\phi=\max\{4,M_\phi\}.                           \tag{8.1.2}
\]
The expectation \(E\) in a one-dimensional activation integral is over
the displayed standard Gaussian. All population contractions elsewhere
are \(E_\ell\) on the physical layer \(\Omega_\ell\), as in Section 5.5.

Let \(F_{N,L}(h)\) be the inverse-free population output (5.5.12).
Sections 8.2--8.4 define its finite exact compiler, including at zero
step. Write \(\mathcal J^{\mathrm{cmp}}_{j,N,L}\) for the number returned
by the order-\(j\) terminal compiler, defined by (8.4.8) below before any
identification with an output derivative. Set
\[
 \mathcal C^{\mathrm{cmp}}_{\phi,L,N}
   =\frac{8\mathcal J^{\mathrm{cmp}}_{3,N,L}
                 -\mathcal J^{\mathrm{cmp}}_{3,2N,L}}6.      \tag{8.1.3}
\]
This notation leaves \(\kappa_\ell\) reserved for mobility multipliers.
The integer \(E_{L,N}\) is explicitly defined in (8.5.1)--(8.5.4),
(8.5.13); it depends only on \(L,N\).

**Theorem 8.1 (fixed-depth, fixed-step-count quantitative doubling).**
Under (8.1.1)--(8.1.2), for every fixed \(L,N\ge1\),
\[
 F_{N,L}\in C^5([-1,1]),\qquad
 \sup_{|h|\le1}|F_{N,L}^{(5)}(h)|\le B_\phi^{E_{L,N}},    \tag{8.1.4}
\]
and
\[
 \left|F_{N,L}(2h)-F_{2N,L}(h)
                  -\mathcal C^{\mathrm{cmp}}_{\phi,L,N}h^3\right|
       \le B_\phi^{E_{L,2N}}|h|^5,
       \qquad |h|\le\tfrac12.                            \tag{8.1.5}
\]
For each fixed \(h\ne0\) in this interval, both outputs in (8.1.5)
are the actual width-first expectations:
\[
 F_{N,L}(2h)=\lim_{n\to\infty}E f_{n,L}^{N}(2h),\qquad
 F_{2N,L}(h)=\lim_{n\to\infty}E f_{n,L}^{2N}(h).          \tag{8.1.6}
\]
The argument in parentheses specifies the common step of that finite
program. At \(h=0\), the finite-width expectation and the population
output are both zero, by the separate argument in Section 8.7.

If \(E\phi'(G)^2=0\), then \(\phi\equiv1\) or \(-1\),
\(F_{N,L}(h)=Nh\), and the difference in (8.1.5) is identically zero.
Its coefficient and remainder can both be taken to be zero for all real
\(h\). The other branch includes nonconstant affine activations.

To prove the theorem, first express every population expectation as a
chronological Gaussian call on a single layer. A density calculation and
regularization prove the needed Price formula even at singular
covariance. Exact differentiation and polynomial envelopes then provide
both the coefficient and its explicit error bound. Finally, parity and
a direct first-order calculation cancel the lower-order terms. The
only width-limit input is the theorem already proved in Section 5.

### 8.2. Layerwise calls and their exact chronology

Keep \(Z^{(\ell)}_k,H^{(\ell)}_k,\Delta^{(\ell)}_k,
q^{(\ell)}_k,W^{(L+1)}_k,Q_{\ell,jk},K_{\ell,jk},
\rho_{\ell,kj},\sigma_{\ell,kj},\xi_{\ell,k},\chi_{\ell,k}\)
with precisely the types and definitions in (5.5.1)--(5.5.13).
In particular, \(q^{(\ell)}_k\) is the incoming population backsignal,
\(H^{(\ell)}_k=\phi(Z^{(\ell)}_k)\) is the feature, and source
derivatives hold every deterministic covariance and response coefficient
fixed. Neither a transpose nor a response is an independent replacement
for a reused initialization matrix.

For the finite compiler introduce only the deterministic full response
coefficients
\[
 R_{\ell,kj}=\rho_{\ell,kj}+hQ_{\ell-1,jk}\quad(j<k),
                                                               \tag{8.2.1}
\]
\[
 T_{\ell,kj}=\sigma_{\ell,kj}+hK_{\ell,jk}\quad(j<k),
 \qquad T_{\ell,kk}=\sigma_{\ell,kk}.                      \tag{8.2.2}
\]
These are scalar history coefficients, not operators, times, or kernels.
Thus the relevant assignments from Section 5.5 read
\[
 Z^{(\ell)}_k=\xi_{\ell,k}
       +\sum_{j<k}R_{\ell,kj}\Delta^{(\ell)}_j\quad(\ell\ge2),
 \qquad H^{(\ell)}_k=\phi(Z^{(\ell)}_k),                  \tag{8.2.3}
\]
\[
 q^{(\ell-1)}_k=\chi_{\ell,k}
             +\sum_{j\le k}T_{\ell,kj}H^{(\ell-1)}_j,
 \qquad
 \Delta^{(\ell-1)}_k=q^{(\ell-1)}_k\phi'(Z^{(\ell-1)}_k). \tag{8.2.4}
\]
The bottom update and readout are still (5.5.7), (5.5.11)--(5.5.12).
Every sum proportional to an update uses strictly earlier steps.

Write \(Q_\ell^{[k]}=(Q_{\ell,ij})_{0\le i,j\le k}\) and similarly
for \(K_\ell^{[k]}\); a history with upper index \(-1\) is empty.
For \(L\ge2\), start with \(Q_{1,00}=1\). At each
\(k=0,\ldots,N-1\), make the following calls in the displayed order.
Each call reconstructs the local history with already known scalar
coefficients, then integrates all its new scalar outputs against the
indicated finite Gaussian law.

1. For \(\ell=2,\ldots,L-1\) in increasing order, use the layer-\(\ell\)
   source vector
   \((\xi_{\ell,0:k},\chi_{\ell+1,0:k-1})\), with covariance
   \(Q_{\ell-1}^{[k]}\oplus K_{\ell+1}^{[k-1]}\).
   Reconstruct old cotangents and the current forward field. Return the
   new row of \(Q_\ell^{[k]}\), the responses
   \(\rho_{\ell+1,kj}\), \(j<k\), and their full coefficients.
2. On layer \(L\), use \((A,\xi_{L,0:k})\), with covariance
   \([1]\oplus Q_{L-1}^{[k]}\). Form the current feature, readout,
   and cotangent. Return the new row of \(K_L^{[k]}\),
   \(\sigma_{L,kj}\), \(j\le k\), their full coefficients, and
   \(E_L[W^{(L+1)}_kH^{(L)}_k]\) if wanted.
3. For \(\ell=L-1,\ldots,2\) in decreasing order, use
   \((\xi_{\ell,0:k},\chi_{\ell+1,0:k})\), with covariance
   \(Q_{\ell-1}^{[k]}\oplus K_{\ell+1}^{[k]}\).
   Reconstruct the local history and current cotangent. Return the new
   row of \(K_\ell^{[k]}\), \(\sigma_{\ell,kj}\), \(j\le k\),
   and their full coefficients.
4. On layer 1 use \((U,\chi_{2,0:k})\), with covariance
   \([1]\oplus K_2^{[k]}\). Form the current cotangent and
   \(Z^{(1)}_{k+1}=Z^{(1)}_k+h\Delta^{(1)}_k\). Return the new row
   of \(Q_1^{[k+1]}\), \(\rho_{2,k+1,j}\), \(j\le k\), and
   their full coefficients.

At \(k=N\), perform only the ascending interior calls and the top call;
the latter stops after the terminal readout-times-feature expectation.
No terminal cotangent is needed. Empty layer ranges are omitted. Every
input covariance and response used inside a call has therefore been
constructed before that call. New Gram entries and responses computed
in the same call are parallel outputs; none is an input to its own
integrand or covariance.

The call dimensions are
\[
 \begin{array}{c|c}
 \text{call}&\text{source dimension}\\ \hline
 \text{interior forward at }k&2k+1\\
 \text{top at }k&k+2\\
 \text{interior backward at }k&2k+2\\
 \text{bottom at }k&k+2\\
 \text{terminal interior}&2N+1\\
 \text{terminal top}&N+2.
 \end{array}                                                \tag{8.2.5}
\]
They are all at most \(D_N=2N+2\). There are
\(2(L-1)\) nonterminal calls per update and \(L-1\) terminal calls,
hence exactly \((2N+1)(L-1)\) calls. This equals the number of raw
initialization-matrix actions in Section 5.3; a call here is a
layerwise expectation bundle, not an additional matrix observation.

For \(L=1\), there is instead one expectation on independent
\((A,U)\sim N(0,I_2)\). In that one call unroll
\[
 Z^{(1)}_0=U,\quad W^{(2)}_0=A,\qquad
 \begin{aligned}
 W^{(2)}_{k+1}&=W^{(2)}_k+h\phi(Z^{(1)}_k),\\
 Z^{(1)}_{k+1}&=Z^{(1)}_k+hW^{(2)}_k\phi'(Z^{(1)}_k),
 \end{aligned}                                             \tag{8.2.6}
\]
and integrate \(W^{(2)}_N\phi(Z^{(1)}_N)\). Both updates use the old
state. No fictitious connector or history inverse is introduced.

All these calls are also defined at \(h=0\). Indeed a matrix of
second moments is positive semidefinite: its quadratic form at \(b\)
is the expectation of the square of the corresponding linear
combination. Chronological construction therefore supplies a Gaussian
law for each covariance, using the finite square-root construction in
Section 4. No strict-rank assertion is needed to define these calls.

### 8.3. Price differentiation, with the singular case proved

**Lemma 8.2.** Let \(I=[-1,1]\), and let
\(C\in C^5(I;\mathbb S_+^{b})\), where \(b\) is a source dimension
and is unrelated to the network input dimension \(d=1\). Suppose
\(\psi(h,x)\) has jointly continuous mixed derivatives
\[
 \partial_h^j D_x^\alpha\psi,
       \qquad j+\left\lceil|\alpha|/2\right\rceil\le5,       \tag{8.3.1}
\]
all bounded in absolute value by \(A_*(1+\|x\|_2)^{p_*}\), uniformly
on \(I\). If \(Y_h\sim N(0,C(h))\), then
\(\mathcal T(h)=E\psi(h,Y_h)\) belongs to \(C^5(I)\), and
\[
 \mathcal T^{(r)}(h)=E\Psi_r(h,Y_h),\qquad
 \Psi_0=\psi,\qquad
 \Psi_{r+1}=\partial_h\Psi_r+\tfrac12 C'(h):D_x^2\Psi_r,
       \quad 0\le r<5.                                    \tag{8.3.2}
\]
The contraction is \(C':D_x^2=\sum_{a,c=1}^{b}C'_{ac}\partial_a\partial_c\);
off-diagonal ordered pairs are both included. On a closed interval
\(C^5\) means that the derivatives through order five extend
continuously to the endpoints.

**Proof.** First suppose \(C(h)>0\). Its Gaussian density \(p_h\)
satisfies, by differentiating its determinant and quadratic exponent,
\[
 \partial_h p_h(x)=\tfrac12
  \left(x^TC^{-1}C'C^{-1}x-\operatorname{tr}(C^{-1}C')\right)p_h(x).
                                                               \tag{8.3.3}
\]
On the other hand,
\[
 \partial_a\partial_c p_h(x)
  =\left((C^{-1}x)_a(C^{-1}x)_c-(C^{-1})_{ac}\right)p_h(x).
\]
Contracting this identity with \(C'_{ac}/2\) gives (8.3.3).
Differentiation under the integral and two integrations by parts now
give
\[
 \frac{d}{dh}\int\psi(h,x)p_h(x)\,dx
 =\int\left(\partial_h\psi+\tfrac12 C':D_x^2\psi\right)p_h\,dx.
                                                               \tag{8.3.4}
\]
On a compact parameter interval with positive minimum covariance
eigenvalue, the density and its differentiated factors have polynomial
times Gaussian bounds. Together with (8.3.1), these bounds justify the
differentiation and make the boundary terms vanish, for instance by
first inserting compact cutoffs and then sending their radius to infinity.

Each iteration either applies one \(h\)-derivative to an integrand
or covariance coefficient, or adds two spatial derivatives with one
factor of \(C'\). After \(r\) iterations, only covariance derivatives
through order \(r\) and integrand derivatives with
\(j+\lceil|\alpha|/2\rceil\le r\) occur. Thus (8.3.4) iterates
through order five using exactly (8.3.1).

For a possibly singular \(C\), put \(C_\epsilon=C+\epsilon I_b\),
\(0<\epsilon\le1\). Its positive definiteness permits the preceding
argument. Its derivatives of positive order equal those of \(C\),
so the derived expressions \(\Psi_r\) are unchanged. Couple
\(Y_{\epsilon,h}=C_\epsilon(h)^{1/2}G_b\) and
\(Y_h=C(h)^{1/2}G_b\) with a standard Gaussian \(G_b\).
Diagonalize \(C(h)\). The two square roots have the same eigenvectors,
and, for every eigenvalue \(\lambda\ge0\),
\[
 0\le\sqrt{\lambda+\epsilon}-\sqrt\lambda\le\sqrt\epsilon.
\]
Consequently
\[
 \sup_{h\in I}\|C_\epsilon(h)^{1/2}-C(h)^{1/2}\|_{\rm op}
       \le\sqrt\epsilon.                                  \tag{8.3.5}
\]
Let \(v=\sup_{h\in I}\sum_{a,c}|C_{ac}(h)|<\infty\).
Both coupled vectors have norm at most \(\sqrt{v+1}\|G_b\|_2\).
Every \(\Psi_r\) is a finite sum of the mixed derivatives in (8.3.1)
times bounded covariance-derivative coefficients, so it has a common
polynomial envelope. On \(\{\|G_b\|_2\le R\}\), (8.3.5) and
uniform continuity on compact sets give uniform convergence in \(h\)
of its coupled values. Outside that event, a fixed polynomial in
\(\|G_b\|_2\) dominates their difference and has a tail expectation
tending to zero as \(R\to\infty\). Hence
\[
 E\Psi_r(h,Y_{\epsilon,h})\longrightarrow E\Psi_r(h,Y_h)
 \quad\text{uniformly on }I,\quad 0\le r\le5.             \tag{8.3.6}
\]
The limiting expectations are continuous by the same compact-and-tail
argument. For each \(r<5\), pass to the limit in
\[
 \mathcal T_\epsilon^{(r)}(v_1)
 -\mathcal T_\epsilon^{(r)}(u_1)
       =\int_{u_1}^{v_1}\mathcal T_\epsilon^{(r+1)}(s)\,ds.
\]
Uniform convergence shows successively that each limiting function has
the next as its derivative. This proves (8.3.2), including at changes
of rank. No derivative of a singular covariance square root, and no
inverse of the original covariance, has been used. \(\square\)

### 8.4. Exact compiler, envelope compiler, and derivative budget

An envelope \((A,p)\), with \(A\ge0\) and integer \(p\ge0\), means
\(|g(x)|\le A(1+\|x\|_2)^p\), uniformly for \(|h|\le1\).
Use the two operations
\[
 (A,p)\oplus(B,q)=(A+B,\max\{p,q\}),\qquad
 (A,p)\odot(B,q)=(AB,p+q).                                 \tag{8.4.1}
\]
The leaves \(1,h,x_a\) have envelopes \((1,0),(1,0),(1,1)\).
A real constant has envelope \((|c|,0)\). If \(g\) has envelope
\((A,p)\), assign
\[
 \mathcal E(\phi(g))=(M_\phi(1+A),p),\qquad
 \mathcal E(\phi^{(j)}(g))=(M_\phi,0),\quad1\le j\le12.   \tag{8.4.2}
\]
Sums, products, and derivatives are expanded by their exact rules.
An earlier scalar node \(S(h)\), with bounds \(\bar S_j\) through
order five, supplies formal tokens
\[
 \partial_h S^{[j]}=S^{[j+1]},\qquad
 \partial_{x_a}S^{[j]}=0,
 \qquad\mathcal E(S^{[j]})=(\bar S_j,0).                  \tag{8.4.3}
\]
All ambient source derivatives in a response also hold these tokens
fixed. Only total \(h\)-differentiation advances their order.

Consider a call \(\mathcal T(h)=E_{N(0,C(h))}\psi(h,Y)\) in dimension
\(b\le D_N\). Available covariance bounds are
\(\bar c_j\ge\sup_{|h|\le1}\sum_{a,c}|C^{(j)}_{ac}(h)|\),
\(0\le j\le5\). For ordered spatial index lists \(\mathbf i\) of
length \(q\), initialize
\[
 P^{(0)}_{j,q}
   =\bigoplus_{\mathbf i\in\{1,\ldots,b\}^{q}}
       \mathcal E(\partial_h^j\partial_{Y_{\mathbf i}}\psi),
       \qquad j+\lceil q/2\rceil\le5.                     \tag{8.4.4}
\]
There is one empty list when \(q=0\). Whenever
\(r+j+\lceil q/2\rceil<5\), recurse by
\[
 P^{(r+1)}_{j,q}=P^{(r)}_{j+1,q}
    \oplus\bigoplus_{a=0}^{j}
      \left[(\tfrac12\tbinom ja\bar c_{a+1},0)
                          \odot P^{(r)}_{j-a,q+2}\right].  \tag{8.4.5}
\]
This follows by applying \(\partial_h^jD_Y^q\) to (8.3.2): Leibniz's
rule differentiates \(C'\) exactly \(a\) times. Aggregating absolute
values over all ordered indices, then multiplying by the entrywise
covariance bound, can only increase the bound. In particular it includes
both off-diagonal covariance entries. The strict guard ensures that
every child is available, that \(a+1\le5\), and that no
\(S^{[5]}\) is differentiated.

If \(P^{(r)}_{0,0}=(A_r,p_r)\), return
\[
 \overline{\mathcal J}_r(\mathcal T)
       =A_r\mu_{b,p_r}(\bar c_0),\qquad
 \mu_{b,p}(v)=\sum_{q=0}^{p}\binom pq v^{q/2}2^{q/2}
              \frac{\Gamma((b+q)/2)}{\Gamma(b/2)}.          \tag{8.4.6}
\]
Indeed, \(\|C^{1/2}G_b\|_2\le\sqrt{\bar c_0}\|G_b\|_2\).
Polar coordinates in the Gaussian integral give
\(E\|G_b\|_2^q=2^{q/2}\Gamma((b+q)/2)/\Gamma(b/2)\):
the angular factor cancels in the ratio of the radial integrals
\(\int_0^\infty r^{b+q-1}e^{-r^2/2}dr\) and
\(\int_0^\infty r^{b-1}e^{-r^2/2}dr\), and the substitution
\(u=r^2/2\) gives the stated ratio. Expansion of
\((1+\sqrt v\|G_b\|_2)^p\) proves (8.4.6). At \(v=0\), its
\(q=0\) term is one and its positive-order terms are zero.

Assemble each covariance by summing the bounds on its entries. For the
full coefficients (8.2.1)--(8.2.2), use
\[
 \bar R_j=\bar\rho_j+\bar Q_j+j\bar Q_{j-1},\qquad
 \bar T_j=\bar\sigma_j+\bar K_j+j\bar K_{j-1},             \tag{8.4.7}
\]
with negative-index terms zero and the diagonal \(\bar T_j=\bar\sigma_j\).
These formulas use the exact identity
\((hQ)^{(j)}=hQ^{(j)}+jQ^{(j-1)}\), including \(j=0\).

For the exact compiler use the same chronological calls and the exact
expressions \(\Psi_r\) in (8.3.2). Initialize jets of genuinely constant
scalar nodes by their values at order zero and zero at higher orders.
In each subsequent call, substitute the already computed jets for
earlier scalar tokens and define
\[
 \mathcal J_r(\mathcal T)
   =E_{Y\sim N(0,C(0))}\Psi_r(0,Y),\qquad0\le r\le5,
 \qquad
 S^{[j]}\big|_{h=0}=\mathcal J_j(S).                      \tag{8.4.8}
\]
Exact coefficient assembly uses
\(\mathcal J_j(R)=\mathcal J_j(\rho)+j\mathcal J_{j-1}(Q)\)
at zero, and the corresponding formula for \(T\), with zero
negative-index jets. Equations (8.2.1)--(8.2.6), (8.3.2), and (8.4.8)
therefore determine the terminal numbers
\(\mathcal J^{\mathrm{cmp}}_{r,N,L}\) without referring to an unknown
output derivative.

Here is the full regularity check that justifies both compilers. An
undifferentiated local state, Gram product, or output integrand contains
activation atoms of order at most one. A response first applies one
ambient source derivative, so its maximum atom order is at most two.
Within the guarded array at Price level \(r\), the additional number
of ordinary formal derivatives falling on an integrand is at most
\[
 2r+j+q\le10
       \quad\text{if }r+j+\lceil q/2\rceil\le5.           \tag{8.4.9}
\]
The response's one preliminary derivative is already included in its
atom order two. Thus \(\phi^{(12)}\) is sufficient, and
\(\phi^{(13)}\) is never requested. A scalar token needs at most five
\(h\)-derivatives; a covariance needs at most five as well. Higher
spatial derivatives do not differentiate scalar tokens.

At the first call, all coefficient and covariance inputs are constant
functions of \(h\). Suppose all earlier scalar outputs have continuous
derivatives and bounds through order five. Finite local syntax, the
chain and product rules, and (8.4.1)--(8.4.3) then supply jointly
continuous mixed derivatives (8.3.1) with one common polynomial
envelope. Its covariance is \(C^5\), by the earlier scalar outputs,
and is positive semidefinite by its Gram construction. Lemma 8.2 applies
and supplies the next scalar outputs and bounds. This is a finite
induction in Section 8.2's chronology, including the single call when
\(L=1\). It proves
\[
 |\mathcal T^{(r)}(h)|\le\overline{\mathcal J}_r(\mathcal T),
 \qquad \mathcal J_r(\mathcal T)=\mathcal T^{(r)}(0),
 \quad |h|\le1,\quad0\le r\le5.                          \tag{8.4.10}
\]

To make the activation-integral content of (8.4.8) explicit, put
\(\mu_{\phi'}=E\phi'(G)^2\). At zero step all responses vanish,
all time copies of a forward source on a layer coincide, and
\[
 Q_{\ell,jk}(0)=1,\qquad
 K_{\ell,jk}(0)=\mu_{\phi'}^{L-\ell+1}.                   \tag{8.4.11}
\]
These facts also follow from the zero-step calculation in Section 8.6.
One joint representation uses independent standard Gaussians
\(A,G_1,\ldots,G_L,B_1,\ldots,B_{L-1}\), with \(U=G_1\),
\(\xi_{\ell,k}=G_\ell\), and
\(\chi_{\ell,k}=\mu_{\phi'}^{(L-\ell+1)/2}B_{\ell-1}\).
Different physical layers retain their own independent marks.

Differentiate in the ambient source coordinates before making these
identifications. After substitution, every expanded term in (8.4.8)
is a product of ordinary Gaussian monomials and activation atoms at
individual standard Gaussians. Independence reduces its expectation to
finite products of ordinary Gaussian moments and integrals
\[
 I_{a,\boldsymbol\beta}(\phi)
   =E\left[G^a\prod_{j=0}^{12}
                    \phi^{(j)}(G)^{\beta_j}\right],
 \quad a,\beta_j\in\{0,1,2,\ldots\},\quad\phi^{(0)}=\phi.\tag{8.4.12}
\]
All are finite by (8.1.2). Carrier powers with odd Gaussian expectation
vanish; even powers of their standard deviations are integer powers of
\(\mu_{\phi'}\). Thus the coefficient (8.1.3) is an explicitly
terminating activation-integral expression. No reduction to a prescribed
small list of moments is asserted.

### 8.5. The explicit exponent and all its majorant obligations

The following constants are specified independently of any trajectory or
output supremum. For \(D=D_N=2N+2\), set
\[
 R_{N,0}=1,\qquad
 R_{N,k+1}=16(N+2)(R_{N,k}+1),
                  \quad0\le k<8(N+1),                    \tag{8.5.1}
\]
\[
 c_{N,0}=4(R_{N,8(N+1)}+1),\qquad
 c_{N,j+1}=64(D+1)^{10}(c_{N,j}+1)^2,
                  \quad0\le j<24,\qquad C_N=c_{N,24},    \tag{8.5.2}
\]
\[
 \nu_N=\mu_{D,C_N}((D+1)^2),\qquad
 \alpha_N=\left\lceil\log_2(2^{C_N}\nu_N)\right\rceil,
 \qquad p_N=2C_N,\quad r_N=C_N+\alpha_N.                  \tag{8.5.3}
\]
Here \(\mu_{b,p}\) is the explicit Gaussian moment expression
(8.4.6). Every recurrence has a finite displayed terminal index;
\(\nu_N\) is a positive finite number given by a finite sum,
\(\alpha_N\) is a specified nonnegative integer, and \(p_N>1\).
Finally the number of calls is
\[
 M_{L,N}=\begin{cases}(2N+1)(L-1),&L\ge2,\\1,&L=1.
                    \end{cases}                         \tag{8.5.4}
\]

**Lemma 8.3 (one-call bound).** Suppose every incoming scalar token and
its derivatives through order five have magnitude at most \(S\ge2\)
on \([-1,1]\), and every covariance entry has the same derivative
bounds. Every new scalar bound returned by one call, including full
coefficient assembly and covariance entrywise-bound assembly, is at most
\[
 B_\phi^{r_N}S^{p_N}.                                    \tag{8.5.5}
\]

**Proof.** Give a leaf size one, a unary activation node size one plus
its child size, and a binary sum or product size one plus its two child
sizes. Before counting, expand integer coefficients into signed unit
summands, expand every binomial multiplicity, and expand every covariance
contraction and ordered spatial-index sum. Factors of magnitude at most
one, such as \(1/2\), may be retained with their exact values and
bounded by one. Thus no large combinatorial constant is treated as a
unit-size bounded scalar token.

If the available expressions have size at most \(R\), a product of
at most three has size at most \(3R+2\). A sum of \(J\le2N+3\)
such products has size at most \(J(3R+3)-1\), which is bounded by
\(16(N+2)(R+1)\). This also dominates a single activation
assignment and the affine source-plus-history assignments. In a local
interior history there are at most the four assignments
\(Z^{(\ell)}_k,H^{(\ell)}_k,q^{(\ell)}_k,\Delta^{(\ell)}_k\)
per time slice. At the top replace \(q\) by \(W^{(L+1)}\);
at the bottom use the bottom state update. Thus \(4(N+1)\)
assignments suffice for every \(L\ge2\) call. The scalar unrolling
(8.2.6), including its terminal activation, uses fewer than
\(4(N+1)+2\le8(N+1)\) assignments. Equation (8.5.1) covers them
all. A terminal or Gram product has size at most twice the terminal
raw size plus one; a pre-response expression has no larger bound.
Both are below \(c_{N,0}\).

For a formal derivative in any one source coordinate or in \(h\),
structural induction gives
\[
 |\partial e|\le2(|e|+1)^2.                               \tag{8.5.6}
\]
For a sum use the sum of its two differentiated children and one sum
node. For a product use two product nodes and one sum node, containing
one differentiated and one unchanged child in each term. For an
activation use \(\phi^{(j+1)}(g)\partial g\), with the unchanged
child \(g\) and its differentiated copy. Substitution of the child
bounds in these three cases proves (8.5.6); leaves differentiate to a
leaf or zero. Token advancement changes no tree size.

There are at most ten mixed-derivative levels, one extra ambient
derivative for a response, one aggregation of at most \(D^{10}\)
ordered spatial lists, and five levels of (8.4.5). At one Price level
the expanded expression has at most
\[
 1+D^2\sum_{a=0}^{j}\binom ja\le1+32D^2                 \tag{8.5.7}
\]
summands, since \(j\le5\). Multiplication by a covariance token
and addition of these terms, or addition of \(D^{10}\) expressions,
are each bounded by one application of
\(c\mapsto64(D+1)^{10}(c+1)^2\). Equation (8.5.6) is bounded
by that map as well. The guard (8.4.9) limits the actual derivative
order; counting ten base derivative levels and five combination levels
is only a conservative size count, not a request for extra derivatives.

Two more applications cover full coefficient and covariance-bound
assembly: the former adds at most seven signed-unit terms at derivative
order at most five, and the latter adds at most \(D^2\) entry bounds.
Old entries in such an assembly are incoming tokens. The maximum size
along any branch therefore needs at most
\[
 10+1+1+5+2=19<24
\]
applications. In particular, \(C_N\) bounds syntax size, the number
of incoming-token occurrences, and polynomial-envelope degree, including
all integer and dimension multiplicities. For the degree assertion,
spatial leaves contribute degree one, sums take a maximum, products
add, and a zeroth activation preserves degree by (8.4.2); a positive
activation derivative has degree zero. Induction bounds degree by
the number of nodes.

The envelope coefficient of a tree of size at most \(C_N\) is at most
\[
 (2B_\phi)^{C_N}S^{C_N}.                                 \tag{8.5.8}
\]
Here each scalar leaf costs at most \(S\), each activation costs at
most \(B_\phi\), and the factor two per node absorbs the
\(1+A\) in (8.4.2) and sums. A formal structural induction can take
the common leaf/node base \(2B_\phi S\): for a sum of children the
extra node bounds their sum by the product of their bases times
\(2B_\phi S\); products multiply the child bounds; and
\(B_\phi(1+A)\le2B_\phi\max\{1,A\}\) handles an activation.

There is only one Gaussian-moment cost per returned bound. To see this
also for assembly after integration, regard an incoming scalar as a
constant integrand in the current call. A sum of bounds
\(A_i\mu_{b,p_i}(v)\) is at most
\((\sum_i A_i)\mu_{b,\max_i p_i}(v)\). Thus sums for (8.4.7)
and for entrywise covariance bounds can be assembled before applying
one common Gaussian-moment majorant. They do not cause a second
independent factor of \(\nu_N\).

The covariance used by the call has entrywise norm at most
\((D+1)^2S\). For \(b\le D\), couple \(G_b\) to the first
\(b\) coordinates of \(G_D\). Since \(S\ge1\),
\[
 \begin{aligned}
 \mu_{b,C_N}((D+1)^2S)
 &=E[1+(D+1)\sqrt S\|G_b\|_2]^{C_N}\\
 &\le S^{C_N/2}E[1+(D+1)\|G_D\|_2]^{C_N}
  =S^{C_N/2}\nu_N.\end{aligned}                          \tag{8.5.9}
\]
Combining (8.5.8)--(8.5.9), enlarging
\(S^{3C_N/2}\) to \(S^{2C_N}\), and using
\[
 2^{C_N}\nu_N\le2^{\alpha_N}\le B_\phi^{\alpha_N}
\]
gives (8.5.5). \(\square\)

Initialization supplies only genuinely constant functions of \(h\)
as free scalar inputs: units, zeros, the normalized initial forward
variance, and, if precomputed, the initial cotangent variances
\(\mu_{\phi'}^j\), \(0\le j\le L\). Their derivatives of positive
order are zero and their values are at most \(B_\phi^{2L}\), since
\(\mu_{\phi'}\le M_\phi^2\). This initialization bound is not applied
to derivatives of a nonconstant history node merely because its value
at zero step equals an initial variance. Every such node must first
pass through its chronological compiler call.

Starting at \(S_0=B_\phi^{2L}\), write \(S_j=B_\phi^{a_j}\) and use
Lemma 8.3 to obtain
\[
 a_0=2L,\qquad a_{j+1}=r_N+p_Na_j,
               \quad0\le j<M_{L,N}.                      \tag{8.5.10}
\]
The map increases positive inputs, so the new bound also bounds every
retained older token. Induction solves this scalar recurrence as
\[
 a_j=2L p_N^j+r_N\sum_{i=0}^{j-1}p_N^i.                  \tag{8.5.11}
\]
The terminal order-five bound is consequently
\[
 \overline{\mathcal J}_5(F_{N,L})\le B_\phi^{E_{L,N}},     \tag{8.5.12}
\]
where the promised explicit exponent is
\[
 E_{L,N}=2L p_N^{M_{L,N}}
           +r_N\frac{p_N^{M_{L,N}}-1}{p_N-1}.             \tag{8.5.13}
\]
The quotient is the finite integer geometric sum in (8.5.11).
There is no unspecified multiplicative constant in (8.5.12).

For later use, \(E_{L,N}\) is nondecreasing in \(N\). Increasing
\(N\) increases the multiplier and the number of iterations in
(8.5.1), and then the initial value and multiplier in (8.5.2).
Thus \(D_N,C_N\) are nondecreasing. Couple standard Gaussians by
initial coordinates as above; because \(1+(D+1)\|G_D\|_2\ge1\),
\(\nu_N\) is nondecreasing in both \(D_N\) and \(C_N\).
So are \(\alpha_N,p_N,r_N\). The number \(M_{L,N}\) increases
for \(L\ge2\) and stays one for \(L=1\). Finally (8.5.10)
iterates an increasing map that increases positive inputs. Increasing
its parameters and applying it no fewer times proves the assertion.

### 8.6. Parity and an explicit first-order cancellation calculation

The following symmetry holds without any parity assumption on \(\phi\).
Change \(h\) to \(-h\), change the top root \(A\) and every
backward source \(\chi_{\ell,k}\) to their negatives, and leave
\(U\) and every \(\xi_{\ell,k}\) fixed. Chronological induction
in (5.5.4)--(5.5.12) gives even transformation for
\(Z^{(\ell)},H^{(\ell)},Q_\ell,K_\ell\), and odd transformation
for \(W^{(L+1)},q^{(\ell)},\Delta^{(\ell)},\rho,\sigma,R,T\).
For a response, differentiating an even transformed feature with
respect to the sign-reversed backward coordinate supplies a minus sign;
differentiating an odd transformed cotangent with respect to an unchanged
forward coordinate retains its minus sign. Thus the response definitions
respect the induction. Gram entries are unchanged, so at the next call
the Gaussian covariance is unchanged; simultaneous negation of its
backward block preserves its centered Gaussian law. This proves the
law-level induction and, for all \(h\in[-1,1]\),
\[
 F_{N,L}(-h)=-F_{N,L}(h),\quad
 Q_\ell(-h)=Q_\ell(h),\quad K_\ell(-h)=K_\ell(h).         \tag{8.6.1}
\]
For \(L=1\), the same assertion follows immediately from (8.2.6)
under \((h,A)\mapsto(-h,-A)\).

In particular all responses vanish at zero, and all covariance matrices
in the calls have \(C'(0)=0\). At \(h=0\), the bottom state is
\(U\), all higher states equal their current forward sources, and
all forward variances equal one by normalization. A backward source
has the initialization cotangent variance of its upper layer. Descending
from \(\Delta^{(L)}=A\phi'(G_L)\) gives exactly (8.4.11).
In the coalesced representation, define the initial upper carrier on
layer \(\ell\) by
\[
 V_L=A,\qquad
 V_\ell=\mu_{\phi'}^{(L-\ell)/2}B_\ell\quad(\ell<L).
                                                               \tag{8.6.2}
\]
It is independent of \(G_\ell\), has second moment
\(\mu_{\phi'}^{L-\ell}\), and
\(\Delta^{(\ell)}_k(0)=V_\ell\phi'(G_\ell)\) for every
applicable \(k\).

Here is a direct computation of the first terminal jet, which also
checks that no covariance term is missing. A dot in the next calculation
means the explicit \(h\)-derivative of a local integrand at zero,
including earlier scalar-token derivatives and holding its ambient
Gaussian coordinates fixed. At first order, Lemma 8.2 reduces to
expectation of this dot, since \(C'(0)=0\).

For \(j<k\), define the deterministic numbers
\(b_{\ell,kj}=\rho_{\ell,kj}'(0)\), \(2\le\ell\le L\).
From the exact bottom identity
\(Z^{(1)}_k=U+h\sum_{j<k}\Delta^{(1)}_j\), differentiation
before collapsing the backward source coordinates gives
\[
 \partial_{\chi_{2,j}}\dot H^{(1)}_k=\phi'(U)^2,
 \qquad b_{2,kj}=\mu_{\phi'}.                            \tag{8.6.3}
\]
Indeed at zero the ambient bottom cotangent at time \(j\) is
\(\chi_{2,j}\phi'(U)\); other times use their own ambient coordinates.

For \(2\le\ell<L\), the analogous ambient calculation from
(8.2.3) gives
\[
 \dot H^{(\ell)}_k
   =\phi'(\xi_{\ell,k})
       \sum_{j<k}(1+b_{\ell,kj})
                      \chi_{\ell+1,j}\phi'(\xi_{\ell,j}).\tag{8.6.4}
\]
The factor one is \(Q_{\ell-1,jk}(0)\). Terms differentiating an
old cotangent are multiplied by \(R(0)=0\) and vanish. The
numbers \(b_{\ell,kj}\) are scalar tokens, hence are held fixed
by the ambient derivative. Take \(\partial_{\chi_{\ell+1,j}}\)
of (8.6.4), and only then set
\(\xi_{\ell,k}=\xi_{\ell,j}=G_\ell\). The first-jet Price formula
for the response gives
\[
 b_{\ell+1,kj}=\mu_{\phi'}(1+b_{\ell,kj}).                \tag{8.6.5}
\]
Together with (8.6.3), this finite layer induction yields
\[
 b_{\ell,kj}=\sum_{a=1}^{\ell-1}\mu_{\phi'}^a.
                                                               \tag{8.6.6}
\]
The result is independent of \(j,k\); no derivative of a backward
response was needed for this forward first-order calculation.

At the top, (8.2.3), (8.6.6), and the coalesced source law give
\[
 \dot H^{(L)}_N
    =N\left(\sum_{a=0}^{L-1}\mu_{\phi'}^a\right)
                       A\phi'(G_L)^2,
 \qquad
 \dot W^{(L+1)}_N=N\phi(G_L).                            \tag{8.6.7}
\]
For \(L=1\), these two equations follow directly from (8.2.6), with
the sum reduced to one and \(G_L=U\). Apply the first-jet Price
formula to the terminal product and use \(EA^2=1\),
\(E\phi(G_L)^2=1\). It gives
\[
 \mathcal J^{\mathrm{cmp}}_{1,N,L}
 =F_{N,L}'(0)
 =N+N\mu_{\phi'}\sum_{a=0}^{L-1}\mu_{\phi'}^a
 =N\sum_{a=0}^{L}\mu_{\phi'}^a.                          \tag{8.6.8}
\]
Thus every first-order contribution, including the effect of forward
reuse responses, has been evaluated inside the population compiler.
There was no differentiation of a finite-width limit. By oddness and
\(C^5\) regularity,
\[
 F_{N,L}(0)=F_{N,L}^{(2)}(0)=F_{N,L}^{(4)}(0)=0.          \tag{8.6.9}
\]

### 8.7. Taylor remainder, width identification, and scope

The elementary integral Taylor formula follows by repeated integration
of the fifth derivative:
\[
 F_{N,L}(u)=u\mathcal J^{\mathrm{cmp}}_{1,N,L}
        +\frac{u^3}{6}\mathcal J^{\mathrm{cmp}}_{3,N,L}
        +\frac1{4!}\int_0^u(u-v)^4F_{N,L}^{(5)}(v)\,dv,
        \qquad |u|\le1.                                 \tag{8.7.1}
\]
For negative \(u\), reverse the integration orientation to bound its
absolute value. In either direction the integral has magnitude at most
\(\overline{\mathcal J}_5(F_{N,L})|u|^5/120\).
Apply (8.7.1) at \(u=2h\) for \(N\) updates and at \(u=h\)
for \(2N\) updates. Equation (8.6.8) cancels the two linear terms,
and (8.1.3) is exactly the remaining cubic coefficient. Therefore
\[
 \begin{aligned}
 &|F_{N,L}(2h)-F_{2N,L}(h)
                      -\mathcal C^{\mathrm{cmp}}_{\phi,L,N}h^3|\\
 &\qquad\le
   \frac{32\overline{\mathcal J}_5(F_{N,L})
                   +\overline{\mathcal J}_5(F_{2N,L})}{120}|h|^5,
       \qquad |h|\le\tfrac12.\end{aligned}                \tag{8.7.2}
\]
Monotonicity of \(E_{L,N}\), (8.5.12), and \(33/120<1\) prove
(8.1.5). Equations (8.4.10) and (8.5.12) prove (8.1.4).

It remains to verify the network interpretation at exactly the scope
available internally. Conditions (8.1.1)--(8.1.2) imply (5.1.1)--(5.1.2),
for example with \(M=2M_\phi\). For each separately fixed
\(h\ne0\), apply the fixed-program theorem of Section 5.1 once to
\((L,N,2h)\) and once to \((L,2N,h)\). Its initialization and
stored-coordinate mobilities are precisely those in Section 8.1, and
its output program is the one reorganized in Section 8.2. For a
nonconstant activation its strict-rank proof includes the affine case;
its joint coupling and terminal uniform integrability establish the
convergence of expectations in (8.1.6). No new uniform-in-\(h\)
conditioning gap is inferred from that theorem. For \(L=1\), its
separate iid coordinate argument applies directly.

At \(h=0\) every finite update is the identity. The initialized hidden
features are independent of the centered stored readout, so conditioning
on those features gives \(E f_{n,L}^{N}(0)=0\) for every finite
\(n,L,N\). These expectations exist by the Gaussian initialization
and finite linear-growth network. The population program has the
zero-step law in (8.4.11), with terminal product
\(A\phi(G_L)\) (or \(A\phi(U)\) if \(L=1\)); its expectation
is zero as well. This separate calculation establishes agreement at
zero without applying Section 5's punctured-step rank theorem there.

If \(\mu_{\phi'}=0\), continuity of \(\phi'\) and the strictly
positive standard Gaussian density imply \(\phi'\equiv0\): any
nonzero derivative value would have a neighborhood with positive
integral of its square. Normalization then gives \(\phi\equiv c\)
with \(c\in\{-1,1\}\). Every cotangent is zero and the stored
readout is \(W^{(L+1)}_N=W^{(L+1)}_0+Nhc\,\mathbf1\).
Its prediction expectation is \(Nh\), at every width and in the
population program. This proves the constant branch of Theorem 8.1.
\(\square\)

An optional shared activation-only radius base is
\(h_\phi=(2B_\phi)^{-1}\). Since \(B_\phi\ge4\) and
\(E_{L,2N}\ge1\), the smaller explicit domain
\(|h|\le h_\phi^{E_{L,2N}}\) is contained in \(|h|\le1/2\)
and satisfies the same bound (8.1.5). For \(L=3\), substitution gives
\[
 M_{3,2N}=8N+2,\qquad
 E_{3,2N}=6p_{2N}^{8N+2}
       +r_{2N}\frac{p_{2N}^{8N+2}-1}{p_{2N}-1}.           \tag{8.7.3}
\]
For every \(\varepsilon>0\), a fully explicit cubic comparison is
\[
 |F_{N,L}(2h)-F_{2N,L}(h)|
       \le (|\mathcal C^{\mathrm{cmp}}_{\phi,L,N}|+\varepsilon)|h|^3
                                                               \tag{8.7.4}
\]
whenever
\[
 |h|\le\min\left\{\tfrac12,
           \sqrt{\frac{\varepsilon}{1+B_\phi^{E_{L,2N}}}}\right\}.
                                                               \tag{8.7.5}
\]
Indeed the fifth-order error divided by \(|h|^3\), for \(h\ne0\),
is then at most
\(\varepsilon B_\phi^{E_{L,2N}}/(1+B_\phi^{E_{L,2N}})\le\varepsilon\);
the zero-step case is already established.

All conclusions are for fixed finite \(L,N\), the specified order-one
stored readout, and exact feature-ascent updates. The equality of the
two accumulated feature-step lengths, \(N(2h)=(2N)h\), is the
comparison used here; it does not identify either scheme with an exact
physical-time loss-gradient flow. The coefficient is the full finite
compiler (8.4.8), with no compact nine-moment identity substituted for
it. The exponent is allowed to grow with \(N\). Nothing here proves
a growing-step-count width limit, a bound proportional to \(N^4|h|^5\)
on a domain proportional to \(1/N\), convergence of an infinite Taylor
series, or a continuous-time limit.
