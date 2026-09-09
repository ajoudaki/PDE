# The compact depth--time cubic law

## 1. Theorem

Fix a hidden depth \(L\geq1\).  Assume

\[
 \phi\in C^{12}(\mathbb R),\qquad
 \mathbb E\phi(G)^2=1,qquad G\sim N(0,1),
\]

\[
 M_\phi=
 \max\left\{1,
 \sup_x\frac{|\phi(x)|}{1+|x|},
 \max_{1\leq r\leq12}\|\phi^{(r)}\|_\infty\right\}<\infty .
 \tag{1.1}
\]

Let \(F_{N,L}(h)\) be the output of the **already width-limited,
inverse-free Gaussian DAG** for \(N\) recomputed simultaneous gradient-ascent
steps of size \(h\).  Thus the width limit is taken at each fixed nonzero
\(h\) before any derivative at \(h=0\) is considered.  The fixed-\(h\)
identification of the actual network is not reproved in this note.

The unconditional singular-Price compiler defines

\[
 \boxed{
 \kappa^{\mathrm{PJ}}_{\phi,L,t}
 =\frac{8\mathcal J_3(F_{t,L})-\mathcal J_3(F_{2t,L})}{6},}
 \tag{1.2a}
\]

where every \(\mathcal J_3\) is a terminating finite recursion of Gaussian
activation integrals.  Singular Price differentiation, proved separately,
then identifies (1.2a) with the actual cubic coefficient of the width-first
DAG.  This is the rigorous coefficient used by the quantitative theorem.

The shorter finite Gaussian recursion in Section 6 defines two activation
numbers

\[
 \mathsf S_{\phi,L},\qquad \mathsf H_{\phi,L}\geq0,
 \qquad
 J_{\phi,L}:=\mathsf S_{\phi,L}+4\mathsf H_{\phi,L}.
 \tag{1.2}
\]

For every integer \(N\geq1\),

\[
 \boxed{
 F_{N,L}^{(3)}(0)
 =\mathcal A_N\mathsf S_{\phi,L}
  +\mathcal B_N\mathsf H_{\phi,L},}
 \tag{1.3}
\]

where

\[
 \mathcal A_N=\frac{N(4N^2-3N+1)}2,
 \qquad
 \mathcal B_N=2N(N-1)(2N-1).
 \tag{1.4}
\]

Also

\[
 F_{N,L}'(0)=N\Theta_L,
 \qquad
 \Theta_L=\sum_{r=0}^{L}d^r,
 \qquad d=\mathbb E\phi'(G)^2,
 \tag{1.5}
\]

and \(F_{N,L}\) is odd.  Consequently, for

\[
 D_{t,L}(\eta)=F_{t,L}(2\eta)-F_{2t,L}(\eta),
\]

the linear jet cancels, parity forces every even derivative that exists to
vanish, and the compact cubic coefficient is

\[
 \boxed{
 \kappa^{\mathrm{comp}}_{\phi,L,t}
 =\frac{8F_{t,L}^{(3)}(0)-F_{2t,L}^{(3)}(0)}6
 =-\frac{t(2t-1)}2J_{\phi,L}.}
 \tag{1.6}
\]

In particular, at three hidden layers,

\[
 \boxed{
 \kappa^{\mathrm{comp}}_{\phi,3,t}
 =-\frac{t(2t-1)}2J_{\phi,3},}
 \tag{1.7}
\]

and the concrete next rung is

\[
 \boxed{
 \frac1{6}\left.\frac{d^3}{d\eta^3}
 \{F_{2,3}(2\eta)-F_{4,3}(\eta)\}\right|_{\eta=0}
 =-3J_{\phi,3}.}
 \tag{1.8}
\]

Theorem 4.1 proves the common fixed-space gradient germ required for
(1.3)--(1.8).  The separate singular-Price compiler proves the fifth-order
remainder estimate.  Since both constructions compute the third derivative
of the same width-first DAG, uniqueness of the derivative gives the
intertwining identity

\[
 \kappa^{\mathrm{PJ}}_{\phi,L,t}
 =
 \kappa^{\mathrm{comp}}_{\phi,L,t}
 :=-\frac{t(2t-1)}2J_{\phi,L}.
 \tag{1.9}
\]

Thus the compact nine-moment recursion may replace the larger Price
recursion in the cubic coefficient, while the Price majorant still supplies
the quantitative fifth-order remainder.

## 2. Population parameter directions

This section records the algebraic finite-energy estimate.  Its moment
premise is proved independently by the fixed-operator core induction in
Section 4.1; the estimate is not used to construct those operators.

At initialization, let \(\mathcal H_a=L^2(\Omega_a)\) be the coordinate
space of layer \(a\).  A finite-energy perturbation direction has blocks

\[
 v=(v_A,K_L,\ldots,K_2,v_1)
 \in\mathcal P_L
 :=\mathcal H_L\oplus
 \bigoplus_{a=2}^L(\mathcal H_a\otimes\mathcal H_{a-1})
 \oplus\mathcal H_1.
 \tag{2.1}
\]

The initial dense Gaussian matrices are not elements of the tensor-product
summands in (2.1).  Their width-limit cylindrical laws are realized in
Section 4 by genuine bounded, non-Hilbert--Schmidt operators
\(W_{a,0}=I_a+J_a^*\).  Only the finite-energy perturbations \(K_a\) lie
in (2.1).

For a population state, write

\[
 X_a=\phi(Z_a),\qquad
 \Delta_a=R_a\phi'(Z_a).
\]

Reverse differentiation of one scalar output produces the finite-energy
gradient direction

\[
 \mathbf g=
 \bigl(X_L,\Delta_L\otimes X_{L-1},\ldots,
       \Delta_2\otimes X_1,\Delta_1\bigr)\in\mathcal P_L.
 \tag{2.2}
\]

The core induction in Section 4.1 shows that all its blocks have moments of
every finite order under (1.1).  The same is
true of the finitely many directions obtained by differentiating (2.2) at
most twice.  In particular,

\[
 \mathbf h:=D\mathbf g[\mathbf g],\qquad
 D\mathbf g[\mathbf h],\qquad
 D^2\mathbf g[\mathbf g,\mathbf g]
 \tag{2.3}
\]

are finite sums of \(L^2\) endpoint fields and Hilbert--Schmidt tensor
products.  These are the only directions required at cubic order.

Here is the promised finite-energy check, rather than an appeal to formal
differentiability.  If a superscript \([r]\) denotes a generated
directional derivative of total order \(r\leq2\), bounded derivatives of
\(\phi\) and its at-most-linear growth imply, inductively over the finite
forward/backward chronology,

\[
 Z_a^{[r]},X_a^{[r]},R_a^{[r]},\Delta_a^{[r]}
 \in\bigcap_{p<\infty}L^p.
 \tag{2.4}
\]

The induction starts from finitely many Gaussian source jets.  A sum or
product preserves all finite moments, and each differentiated activation is
a finite sum of products of a bounded \(\phi^{(q)}\) with earlier fields;
an undifferentiated \(\phi\) has only linear growth.  Thus every step is
covered by Holder's inequality.  The endpoint blocks of the generated
directions are among the fields in (2.4).  A matrix-gradient block and its
first two variations are exactly

\[
 \Delta_a\otimes X_{a-1},
\]

\[
 \Delta_a^{[1]}\otimes X_{a-1}
 +\Delta_a\otimes X_{a-1}^{[1]},
\]

\[
 \Delta_a^{[2]}\otimes X_{a-1}
 +2\Delta_a^{[1]}\otimes X_{a-1}^{[1]}
 +\Delta_a\otimes X_{a-1}^{[2]}.
 \tag{2.5}
\]

For a simple tensor, its Hilbert--Schmidt norm is the product of the two
\(L^2\) norms.  Equations (2.4)--(2.5), followed by the triangle inequality,
prove that \(\mathbf g\), \(\mathbf h\),
\(D\mathbf g[\mathbf h]\), and
\(D^2\mathbf g[\mathbf g,\mathbf g]\) are genuine elements of
\(\mathcal P_L\).  No cylindrical initialization matrix is asserted to
belong to \(\mathcal P_L\).

## 3. The reused-matrix adjoint identity

The following lemma is the local reason that the limiting response terms
retain the gradient structure.

**Lemma 3.1 (finite-history cylindrical adjoint).**  Consider one reused
matrix.  Let \(x_0,\ldots,x_p\in L^2(\Omega_-)\) be its exposed row-query
history and \(c_0,\ldots,c_q\in L^2(\Omega_+)\) its exposed column-query
history.  Let

\[
 \xi=(\xi_i)_{i\leq p},\qquad
 \chi=(\chi_j)_{j\leq q}
\]

be independent centered Gaussian blocks with

\[
 \mathbb E\xi_i\xi_k=\mathbb E x_ix_k,
 \qquad
 \mathbb E\chi_j\chi_m=\mathbb E c_jc_m.
 \tag{3.1}
\]

For an additional query variation \(\dot x\in L^2(\Omega_-)\), define its
raw forward source \(I(\dot x)\) jointly with \(\xi\) by

\[
 \mathbb E[I(\dot x)\xi_i]=\mathbb E[\dot x x_i],
 \qquad
 \mathbb E I(\dot x)^2=\mathbb E\dot x^2.
\]

If \(c\) is a smooth polynomially bounded function of the forward sources,
and \(\dot x\) is a smooth polynomially bounded function of the transpose
sources, put

\[
 \sigma_i(c)=\mathbb E[\partial_{\xi_i}c],
 \qquad
 \rho_j(\dot x)=\mathbb E[\partial_{\chi_j}\dot x].
\]

Let \(J(c)\) be the raw transpose source with

\[
 \mathbb E[J(c)\chi_j]=\mathbb E[c c_j],
 \qquad
 \mathbb EJ(c)^2=\mathbb Ec^2.
\]

Define

\[
 \boxed{
 \mathbb E\!\left[c\left\{I(\dot x)
             +\sum_{j=0}^q\rho_j(\dot x)c_j\right\}\right]
 =\mathbb E\!\left[\dot x\left\{J(c)
             +\sum_{i=0}^p\sigma_i(c)x_i\right\}\right].}
 \tag{3.2}
\]

The identity remains valid when either Gram in (3.1) is singular.

**Proof.**  Gaussian integration by parts in the forward block gives

\[
 \mathbb E[cI(\dot x)]
 =\sum_{i=0}^p
   \mathbb E[\partial_{\xi_i}c]\,
   \mathbb E[\dot x x_i]
 =\mathbb E\left[\dot x\sum_{i=0}^p\sigma_i(c)x_i\right].
 \tag{3.3}
\]

Gaussian integration by parts in the transpose block gives

\[
 \mathbb E[\dot xJ(c)]
 =\sum_{j=0}^q
   \mathbb E[\partial_{\chi_j}\dot x]\,
   \mathbb E[c c_j]
 =\mathbb E\left[c\sum_{j=0}^q\rho_j(\dot x)c_j\right].
 \tag{3.4}
\]

Adding (3.3) and (3.4) proves (3.2).  Neither calculation uses a covariance
inverse.  For a singular Gram, add \(\varepsilon I\), use (3.3)--(3.4),
couple by the positive-semidefinite square root, and let
\(\varepsilon\downarrow0\).  The polynomial envelopes and Gaussian moments
give domination.  \(\square\)

For a finite history, (3.2) applies to every linear combination of the
queries and cotangents.  The learned Hilbert--Schmidt part of a matrix has
the ordinary adjoint identity

\[
 \langle c,Kx\rangle_{\mathcal H_+}
 =\langle c\otimes x,K\rangle_{\mathcal H_+\otimes\mathcal H_-}.
 \tag{3.5}
\]

Thus (3.2)--(3.5) include both the cylindrical initialization and every
accumulated rank-one update.

## 4. A fixed bounded Gaussian operator and the intertwining theorem

The fixed-list identity in Section 3 does not itself give a compatible
action on moving queries.  The following construction does: it realizes
each initialization matrix by one genuine bounded operator on fixed
Gaussian \(L^2\) spaces.  No covariance square root varies with the step
size.

**Theorem 4.1 (common singular cubic gradient germ).**  For every fixed
finite \((L,N)\), there is one finite-dimensional scalar perturbation DAG
containing the temporal step variables and the generated directions

\[
 \mathbf g,\quad D\mathbf g[\mathbf g],\quad
 D\mathbf g[D\mathbf g[\mathbf g]],\quad
 D^2\mathbf g[\mathbf g,\mathbf g],
\]

such that:

1. all forward and transpose source variables are restrictions of one
   compatible common Gaussian family under every history enlargement;
2. the family is \(C^3\) at the coalesced singular covariance, with
   commuting mixed derivatives and common polynomial domination;
3. every nonlinear moving query is in the domain of the same cylindrical
   action germ through order three, not merely represented by a list of its
   origin jets;
4. node by node, the three-jet of this germ equals the three-jet of the
   inverse-free temporal DAG, including every differentiated response term;
5. reverse differentiation gives (4.2) for all generated directions.

The proof occupies Sections 4.1--4.3.

### 4.1 Fixed Gaussian spaces and creation--annihilation connectors

There is a concrete common scalar perturbation before any abstract
direction is introduced.  For a fixed horizon \(m\), replace the common
step size by independent step variables
\(\varepsilon_0,\ldots,\varepsilon_{m-1}\).  The temporal DAG becomes

\[
 A_s=A+\sum_{r<s}\varepsilon_rX_{L,r},
 \qquad
 Z_{1,s}=U+\sum_{r<s}\varepsilon_r\Delta_{1,r},
 \tag{4.1a}
\]

\[
 Z_{a,s}=\xi_{a,s}
 +\sum_{r<s}(\rho^a_{sr}+\varepsilon_rQ^{a-1}_{rs})
   \Delta_{a,r},
 \qquad 2\leq a\leq L,
 \tag{4.1b}
\]

\[
 R_{a-1,s}=\chi_{a,s}
 +\sum_{r\leq s}\sigma^a_{sr}X_{a-1,r}
 +\sum_{r<s}\varepsilon_rK^a_{rs}X_{a-1,r}.
 \tag{4.1c}
\]

The source covariances are the feature and cotangent Grams, and \(\rho\)
and \(\sigma\) are the same source derivatives as in Lemma 3.1.  Equations
(4.1a)--(4.1c), evaluated in forward/backward chronological order, are an
explicit finite Gaussian DAG in the scalar vector \(\varepsilon\).

For each hidden layer choose, once and for all, a standard Gaussian
probability space \(\Omega_a\) with infinite-dimensional first chaos
\(\mathcal G_a\), and put \(\mathcal H_a=L^2(\Omega_a)\).  Split each
\(\mathcal G_a\) into mutually orthogonal infinite-dimensional closed
subspaces, one for each incident connector and one for an endpoint seed
when needed.  Orthogonal Gaussian chaoses are independent.  Choose unit
Gaussians \(U\in\mathcal H_1\) and \(A\in\mathcal H_L\) in the endpoint
seed subspaces.

All infinite-dimensional separable real Hilbert spaces are isometrically
isomorphic.  Hence, for every \(2\leq a\leq L\), there are onto isometries

\[
 I_a:\mathcal H_{a-1}\longrightarrow\mathcal G_a^{\to},
 \qquad
 J_a:\mathcal H_a\longrightarrow\mathcal G_{a-1}^{\leftarrow},
 \tag{4.1d}
\]

where the displayed image chaoses are two of the fixed orthogonal blocks.
Define the initialization connector and its adjoint by

\[
 W_{a,0}:=I_a+J_a^*:\mathcal H_{a-1}\to\mathcal H_a,
 \qquad
 W_{a,0}^*=I_a^*+J_a.
 \tag{4.1e}
\]

These are genuine bounded operators, with norm at most \(2\); they are not
Hilbert--Schmidt and are not being treated as parameter directions.  For
deterministic \(x,y\in\mathcal H_{a-1}\) and
\(c,d\in\mathcal H_a\),

\[
 \mathbb E[I_a(x)I_a(y)]=\langle x,y\rangle,
 \qquad
 \mathbb E[J_a(c)J_a(d)]=\langle c,d\rangle.
 \tag{4.1f}
\]

Thus \(I_a\) and \(J_a\) are the forward and transpose raw Gaussian
source maps, and the two source blocks are independent.

The adjoint pieces give every response, including for singular histories.
Indeed, suppose

\[
 x=\Psi(J_ac_1,\ldots,J_ac_m,\zeta),
 \tag{4.1g}
\]

where \(\zeta\) is independent of
\(\mathcal G_{a-1}^{\leftarrow}\), and \(\Psi\) is \(C^1\) with a
polynomial envelope.  For arbitrary \(c\in\mathcal H_a\), Gaussian
integration by parts on the fixed first chaos gives

\[
\begin{aligned}
 \langle c,J_a^*x\rangle
 &=\mathbb E[(J_ac)x]\\
 &=\sum_{r=1}^m\langle c,c_r\rangle
       \mathbb E[\partial_r\Psi].
\end{aligned}
\]

Since this holds for every \(c\),

\[
 \boxed{J_a^*x=\sum_{r=1}^m
       \mathbb E[\partial_r\Psi]\,c_r.}
 \tag{4.1h}
\]

No linear independence of the \(c_r\)'s was used.  Consequently (4.1h)
holds when their Gram is singular; it is also invariant under adding
redundant or new history coordinates.  Symmetrically, if

\[
 c=\Phi(I_ax_1,\ldots,I_ax_m,\zeta'),
\]

with \(\zeta'\) independent of \(\mathcal G_a^{\to}\), then

\[
 \boxed{I_a^*c=\sum_{r=1}^m
       \mathbb E[\partial_r\Phi]\,x_r.}
 \tag{4.1i}
\]

Equations (4.1h)--(4.1i) follow from one fixed pair of adjoint operators,
so they satisfy the history-enlargement cocycle automatically.  They also
act on nonlinear moving queries, rather than merely on their origin jets.
If \(x(\lambda)\) is a \(C^r\) curve in \(\mathcal H_{a-1}\), bounded
linearity gives

\[
 \partial_\lambda^qJ_a^*x(\lambda)
 =J_a^*\partial_\lambda^qx(\lambda),
 \qquad 0\leq q\leq r,
 \tag{4.1j}
\]

and the same statement holds for \(I_a,I_a^*,J_a\).  This identity is
valid at a coalesced singular history because no parameter-dependent
covariance factorization is present.

This also handles the new raw directions created by differentiating a
moving history.  If
\(J_a^*x(\lambda)=\sum_r\rho_r(\lambda)c_r(\lambda)\), then

\[
 J_a^*x'(\lambda)
 =\frac{d}{d\lambda}J_a^*x(\lambda)
 =\sum_r\{\rho_r'(\lambda)c_r(\lambda)
          +\rho_r(\lambda)c_r'(\lambda)\}.
 \tag{4.1k}
\]

The differentiated query may now involve \(J_ac_r'(\lambda)\); applying
(4.1h) to the enlarged finite jet list gives exactly the left side of
(4.1k), because both representations are the same intrinsic vector
\(J_a^*x'(\lambda)\).  Iterating this argument through order three, and
symmetrically for \(I_a^*\), proves jet-by-jet compatibility under every
history enlargement.

At each fixed scalar-parameter value, a finite chronology exposes only
finitely many first-chaos coordinates.  For local regularity one does not
claim that the whole parameterized curve lies in their finite span.
Instead, the fixed bounded maps in (4.1d)--(4.1e) put the curve in one
common \(L^2\) space, and induction shows that every mixed jet of total
order at most three lies in the finite smooth core at the base point.  A raw
derivative \(I_ax^{[\alpha]}\) or \(J_ac^{[\alpha]}\) is one Gaussian
coordinate.  Equations (4.1h)--(4.1i), applied to the differentiated
finite-cylindrical field at that base point, put each adjoint derivative in
the finite span of exposed opposite-field jets.  A learned rank-one
derivative is a finite sum of scalar inner products times such jets.

More explicitly, fix a finite scalar slice whose frozen directions belong
to the reachable all-moment smooth core generated in (2.2)--(2.3).  Its
complete history has a fixed finite number of slots and every forward query
has the form

\[
 x(\lambda)=\Psi\bigl(\lambda;
   J_ac_1(\lambda),\ldots,J_ac_m(\lambda),\zeta(\lambda)\bigr),
\]

where the \(J_a\)-orthogonal field \(\zeta(\lambda)\) is independent of
that source block.  Applying (4.1h) at each \(\lambda\) expresses
\(J_a^*x(\lambda)\) as a finite sum of the moving
\(c_r(\lambda)\)'s with scalar expectation coefficients.  The reverse
query has the symmetric representation and (4.1i).  Differentiating these
finite sums proves \(L^p\) regularity of the adjoint actions; it does not
infer \(L^p\) boundedness of \(J_a^*\) or \(I_a^*\) from their \(L^2\)
operator norms.

Under (1.1), all core jets have moments of every finite order.  Sums and
products preserve this property, bounded activation derivatives control
every differentiated activation, and the undifferentiated activation has
at most linear growth.  Taylor's formula with integral remainder, followed
by Holder's inequality, supplies an \(L^p\) dominator for each scalar
difference quotient.

For completeness, the induction is lexicographic in temporal node and
derivative order.  Its invariant is: every already constructed mixed
derivative of order at most three is in every \(L^p\).  The four operations
at the next node preserve it:

1. \(I_a\) and \(J_a\) commute with scalar derivatives, and
   \[
    \|I_ay\|_p=\|J_ay\|_p
      =(\mathbb E|G|^p)^{1/p}\|y\|_2.
   \]
2. For an adjoint action, differentiate the finite identity (4.1h) or
   (4.1i).  Multivariate Leibniz and chain rules give finite sums of
   derivatives of history fields times scalar expectations of products of
   earlier jets and bounded derivatives of \(\phi\).  Holder's inequality
   bounds every term.  Intrinsic equality to \(J_a^*\) or \(I_a^*\) makes
   the result independent of a redundant singular history description.
3. A learned connector is a finite sum of rank-one actions, so every
   derivative is a finite sum of deterministic inner products times
   earlier jets.
4. Pointwise activation derivatives are the finite Faà di Bruno sums;
   bounded \(\phi^{(r)}\) and the all-moment invariant bound them.

The base seeds are Gaussian, so the invariant starts.  The finite
chronology and the three derivative orders make the induction terminate.
Taylor's integral remainder at each of the four operations proves the
claimed derivatives rather than merely producing formal jets.  It follows
that every reachable finite scalar slice is \(C^3\) in all \(L^p\), with
commuting mixed derivatives.  No claim is made for an arbitrary
\(L^2\)-only direction.  This proves items 1--3 of Theorem 4.1 without
invoking Price differentiation or global Fréchet smoothness of the
Nemytskii map on \(L^2\).

### 4.2 Generated-core gradient identities

For

\[
 \theta=(a,K_L,\ldots,K_2,u)\in\mathcal P_L,
\]

put \(W_a(\theta)=W_{a,0}+K_a\) and define the population forward pass by

\[
 Z_1=u,\quad X_1=\phi(Z_1),\qquad
 Z_a=W_a(\theta)X_{a-1},\quad X_a=\phi(Z_a),
 \tag{4.2a}
\]

for \(2\leq a\leq L\), with scalar output

\[
 \mathcal F(\theta)=\langle a,X_L\rangle_{\mathcal H_L}.
 \tag{4.2b}
\]

Its initialization is

\[
 \theta_0=(A,0,\ldots,0,U).
 \tag{4.2c}
\]

Define reverse fields by

\[
 R_L=a,qquad \Delta_a=R_a\phi'(Z_a),
 \qquad R_{a-1}=W_a(\theta)^*\Delta_a
 \quad(2\leq a\leq L).
 \tag{4.2d}
\]

The regularity proved in Section 4.1 justifies all directional derivatives
below on the finite generated family.  For a frozen smooth-core perturbation
\(v=(v_A,V_L,\ldots,V_2,v_1)\), terminal differentiation first gives the
readout term.  At layer \(a\), the connector variation is
\(V_aX_{a-1}\), and

\[
 \langle\Delta_a,V_aX_{a-1}\rangle
 =\langle\Delta_a\otimes X_{a-1},V_a\rangle_{\rm HS}.
\]

The remaining term is moved downward by the genuine adjoint
\(W_a(\theta)^*\) in (4.2d).  Multiplication by
\(\phi'(Z_{a-1})\) gives \(\Delta_{a-1}\).  Descending through all layers
leaves \(\langle\Delta_1,v_1\rangle\).  Hence, with no omitted block,

\[
 D\mathcal F[v]=\langle\mathbf g,v\rangle_{\mathcal P_L}.
 \tag{4.2}
\]

On every reachable scalar slice, Section 4.1 makes \(X_a\) and
\(\Delta_a\) \(C^3\) as \(L^2\)-valued maps.  The rank-one map

\[
 (y,x)\longmapsto y\otimes x
\]

is continuous bilinear from
\(\mathcal H_a\times\mathcal H_{a-1}\) to the Hilbert--Schmidt class, with
\(\|y\otimes x\|_{\rm HS}=\|y\|_2\|x\|_2\).  Consequently the vector
\(\mathbf g\) in (2.2) is \(C^2\) as a
\(\mathcal P_L\)-valued map on every generated finite scalar slice.  This
is the precise local statement needed below; no global \(C^2\) vector
field on an open \(L^2\) ball is asserted.

Differentiate (4.2) inside the common scalar DAG, always keeping the second
direction frozen.  For every cubic-order generated direction,

\[
 D^2\mathcal F[u,v]
 =\langle D\mathbf g[u],v\rangle,
 \tag{4.3}
\]

\[
 D^3\mathcal F[u,w,v]
 =\langle D^2\mathbf g[u,w],v\rangle.
 \tag{4.4}
\]

Because mixed scalar derivatives commute, (4.3) also proves the required
self-adjointness on this finite set:

\[
 \langle D\mathbf g[u],v\rangle
 =\langle u,D\mathbf g[v]\rangle.
 \tag{4.5}
\]

Define

\[
 \mathsf S_{\phi,L}
 :=D^3\mathcal F[\mathbf g,\mathbf g,\mathbf g],
 \qquad
 \mathsf H_{\phi,L}
 :=\|D\mathbf g[\mathbf g]\|_{\mathcal P_L}^2.
 \tag{4.6}
\]

Writing \(\mathbf h=D\mathbf g[\mathbf g]\), equations
(4.2)--(4.5) give the four identities used later:

\[
 D^3\mathcal F[\mathbf g^3]=\mathsf S_{\phi,L},
 \qquad
 D^2\mathcal F[\mathbf h,\mathbf g]=\mathsf H_{\phi,L},
 \tag{4.7}
\]

\[
 D\mathcal F[D\mathbf g[\mathbf h]]=\mathsf H_{\phi,L},
 \qquad
 D\mathcal F[D^2\mathbf g[\mathbf g,\mathbf g]]
 =\mathsf S_{\phi,L}.
 \tag{4.8}
\]

The first identity in (4.8) follows from (4.2), (4.5), and the definition
of \(\mathbf h\).  The second follows from (4.4) with its last direction
equal to the frozen initialization field \(\mathbf g\).

There is no circularity in forming the generated directions.  First use
the affine curve \(\theta_0+\lambda\mathbf g\) to define
\(\mathbf h=D\mathbf g[\mathbf g]\).  Then freeze \(\mathbf h\) and use
the two-coordinate affine family to define
\(D\mathbf g[\mathbf h]\) and
\(D^2\mathbf g[\mathbf g,\mathbf g]\).  Section 2 places all four
directions in \(\mathcal P_L\), and the same fixed operators (4.1e) act on
every one of these families.  Taking all frozen directions as coordinates
in one final affine family gives the common scalar perturbation DAG in
Theorem 4.1.  The finite exposed jet list may grow by coordinates such as
\(I_ax'\) and \(J_ac'\), but the underlying Gaussian family, bounded
operators, and covariance factorization are never enlarged or changed.

### 4.3 Temporal DAG equals population Euler

For connector \(a\), (4.1e), (4.1h), and (4.1i) give, on every current
finite-cylindrical query,

\[
 W_{a,0}x
 =I_a(x)+\sum_r\mathbb E[\partial_{\chi_{a,r}}x]\,\Delta_{a,r},
 \tag{4.9a}
\]

and

\[
 W_{a,0}^*c
 =J_a(c)+\sum_r\mathbb E[\partial_{\xi_{a,r}}c]\,X_{a-1,r}.
 \tag{4.9b}
\]

The sums run over the complete exposed opposite history appropriate to the
call.  The operator on the left is fixed before training and is defined on
all of \(\mathcal H_{a-1}\); the sums on the right are its exact response
representation for the displayed nonlinear query.  Thus this is not an
application of a cylindrical object outside a finite list.

At time \(s\), accumulate the finite-energy parameter increments

\[
 A_s=A+\sum_{r<s}\varepsilon_rX_{L,r},
 \qquad
 u_s=U+\sum_{r<s}\varepsilon_r\Delta_{1,r},
\]

\[
 \mathcal K_{a,s}=\sum_{r<s}\varepsilon_r
 \Delta_{a,r}\otimes X_{a-1,r},
 \qquad 2\leq a\leq L.
 \tag{4.9}
\]

Every \(\mathcal K_{a,s}\) is Hilbert--Schmidt by Section 2.  The forward
action of the genuine bounded-plus-Hilbert--Schmidt connector
\(W_{a,0}+\mathcal K_{a,s}\) on its current query is

\[
 W_{a,0}X_{a-1,s}+\mathcal K_{a,s}X_{a-1,s}
 =W_{a,0}X_{a-1,s}
  +\sum_{r<s}\varepsilon_rQ^{a-1}_{rs}\Delta_{a,r}.
 \tag{4.10}
\]

We now prove equality with (4.1a)--(4.1c) at every fixed value of the step
variables.  Suppose all nodes before the forward call \((a,s)\) agree.
The dependence of \(X_{a-1,s}\) on the outgoing source block
\(\mathcal G_{a-1}^{\leftarrow}\) has arisen only through the already
exposed variables

\[
 \chi_{a,r}=J_a\Delta_{a,r},\qquad r<s.
\]

Equation (4.1h) therefore gives

\[
 W_{a,0}X_{a-1,s}
 =\xi_{a,s}+\sum_{r<s}\rho^a_{sr}\Delta_{a,r},
 \qquad \xi_{a,s}:=I_aX_{a-1,s}.
 \tag{4.10a}
\]

By (4.1f), the joint covariance of the \(\xi_{a,s}\)'s is exactly the
feature Gram \(Q^{a-1}\).  Combining (4.10a) with (4.10) gives (4.1b)
node by node.

The transpose action on the current cotangent is

\[
 W_{a,0}^*\Delta_{a,s}
 +\mathcal K_{a,s}^{*}\Delta_{a,s}
 =W_{a,0}^*\Delta_{a,s}
  +\sum_{r<s}\varepsilon_rK^a_{rs}X_{a-1,r},
 \tag{4.11}
\]

For the reverse call \((a,s)\), the dependence of \(\Delta_{a,s}\) on
\(\mathcal G_a^{\to}\) has arisen only through

\[
 \xi_{a,r}=I_aX_{a-1,r},\qquad r\leq s.
\]

Equation (4.1i) gives

\[
 W_{a,0}^*\Delta_{a,s}
 =\chi_{a,s}+\sum_{r\leq s}\sigma^a_{sr}X_{a-1,r},
 \qquad \chi_{a,s}:=J_a\Delta_{a,s}.
 \tag{4.11a}
\]

The \(\chi\)-covariance is exactly the cotangent Gram \(K^a\).  Combining
(4.11a) with (4.11) gives (4.1c).

At \(s=0\), the endpoint seeds and all connector source blocks are
independent, so the initialization forward and reverse passes agree.
Equations (4.10a) and (4.11a), first upward in \(a\) and then downward in
\(a\), close the induction at time \(s\).  The parameter assignments (4.9)
then close the induction from \(s\) to \(s+1\).  This proves equality of
all temporal nodes as functions of
\((\varepsilon_0,\ldots,\varepsilon_{N-1})\), not merely equality of
origin jets.  Singular feature or cotangent Grams cause no exception,
because (4.1h)--(4.1i) used neither an inverse nor a covariance square
root.

By (4.2), the assignments (4.9) are exactly simultaneous gradient-ascent
updates of the population functional.  Thus the multivariate update is

\[
 \theta_{s+1}=\theta_s+\varepsilon_s\mathbf g(\theta_s).
\]

On the diagonal \(\varepsilon_0=\cdots=\varepsilon_{N-1}=h\), it obeys

\[
 \theta_{s+1}=\theta_s+h\mathbf g(\theta_s),
 \qquad 0\leq s<N,
 \tag{4.12}
\]

as an identity of the fixed-space population construction.  The
\(C^3\) result of Section 4.1 therefore gives equality of the temporal and
Euler three-jets.  Together with Section 4.2, this proves items 4--5 and
completes Theorem 4.1.  No finite-width Taylor expansion or exchange of
\(n\to\infty\) with \(h\to0\) is used.

## 5. Universal time combinatorics

The calculation is an abstract lemma for a \(C^3\) scalar gradient germ.
Theorem 4.1 verifies its hypotheses for the inverse-free Gaussian DAG.

Differentiate (4.12) at \(h=0\), where every \(\theta_s\) equals the
initial state.  Put

\[
 \mathbf h=D\mathbf g[\mathbf g],
 \quad
 \mathbf k=D\mathbf g[\mathbf h],
 \quad
 \mathbf r=D^2\mathbf g[\mathbf g,\mathbf g].
\]

A direct induction gives

\[
 \theta_N'(0)=N\mathbf g,
 \qquad
 \theta_N''(0)=N(N-1)\mathbf h,
 \tag{5.1}
\]

\[
 \theta_N'''(0)
 =6\binom N3\mathbf k
  +3\frac{N(N-1)(2N-1)}6\mathbf r.
 \tag{5.2}
\]

Indeed, the third-derivative increment at step \(s\) is

\[
 3\{s(s-1)\mathbf k+s^2\mathbf r\},
\]

and

\[
 \sum_{s<N}s(s-1)=2\binom N3,
 \qquad
 \sum_{s<N}s^2=\frac{N(N-1)(2N-1)}6.
\]

Apply the third-order chain rule to
\(F_{N,L}(h)=\mathcal F(\theta_N(h))\).  Equations (4.7)--(4.8) and
(5.1)--(5.2) give

\[
\begin{aligned}
 F_{N,L}^{(3)}(0)
 ={}&N^3\mathsf S_{\phi,L}
 +3N^2(N-1)\mathsf H_{\phi,L}\\
 &+6\binom N3\mathsf H_{\phi,L}
 +\frac{N(N-1)(2N-1)}2\mathsf S_{\phi,L}.
\end{aligned}
 \tag{5.3}
\]

The two coefficients reduce to

\[
 N^3+\frac{N(N-1)(2N-1)}2
 =\frac{N(4N^2-3N+1)}2,
\]

\[
 3N^2(N-1)+6\binom N3
 =2N(N-1)(2N-1).
\]

This proves (1.3)--(1.4).

The initialization squared gradient norm is the sum of the readout,
hidden-matrix, and input-layer block energies:

\[
 \|\mathbf g\|^2
 =1+\sum_{a=1}^L d^{L-a+1}
 =\sum_{r=0}^Ld^r=\Theta_L.
 \tag{5.4}
\]

Each of the \(N\) coalesced Euler increments contributes (5.4), giving
(1.5).  Finally,

\[
 8\mathcal A_t-\mathcal A_{2t}=-3t(2t-1),
 \qquad
 8\mathcal B_t-\mathcal B_{2t}=-12t(2t-1),
 \tag{5.5}
\]

which gives the compact identity (1.6).

For parity, send

\[
 h\mapsto-h,qquad A\mapsto-A,qquad
 \chi_{a,s}\mapsto-\chi_{a,s}\quad(2\leq a\leq L),
 \tag{5.6}
\]

and leave every forward Gaussian source fixed.  Induction through the DAG
leaves all \(Z,X,Q,K\) fixed and negates every reverse carrier, cotangent,
response coefficient, learned-plus-response coefficient, and output.
The Gaussian source law is invariant, hence \(F_{N,L}(-h)=-F_{N,L}(h)\).

## 6. Terminating activation-integral recursion

This section gives the terminating recursion for the two invariants in
(1.2).  Theorem 4.1 and the response identities (4.1h)--(4.1i) justify the
straight-path calculation in Section 7.

At one standard Gaussian \(G\), write

\[
 g=\phi(G),\qquad p=\phi'(G),\qquad
 q=\phi''(G),\qquad r_3=\phi'''(G),
\]

and define the nine activation moments

\[
\begin{array}{lll}
 d=\mathbb Ep^2,&u=\mathbb Ep^4,&v=\mathbb E[gq],\\
 m=\mathbb E[gp^2q],&r=\mathbb E[pr_3],&s=\mathbb Eq^2,\\
 j=\mathbb E[p^3r_3],&e=\mathbb E[p^2q^2],
 &\ell=\mathbb E[g^2p^2].
\end{array}
 \tag{6.1}
\]

Assume first \(d>0\).  Define

\[
 \Theta_0=1,qquad
 \Theta_a=1+d\Theta_{a-1}=\sum_{r=0}^ad^r,
 \qquad
 b_a=d^{L-a},\qquad \pi_a=db_a.
 \tag{6.2}
\]

Initialize

\[
 V_0=M_0=T_0=0.
\]

For \(a=1,\ldots,L\), in increasing order, set

\[
 V_a=dV_{a-1}+\Theta_{a-1}^2b_au,
 \tag{6.3}
\]

\[
 M_a=vV_{a-1}+\Theta_{a-1}^2b_am+(d+v)M_{a-1},
 \tag{6.4}
\]

\[
\begin{aligned}
 T_a={}&3\Theta_{a-1}V_{a-1}r
 +3\Theta_{a-1}^3b_aj\\
 &+3\Theta_{a-1}M_{a-1}(r+s)
 +d(T_{a-1}+3M_{a-1}).
\end{aligned}
 \tag{6.5}
\]

Initialize the reverse recursion by

\[
 \beta_{L+1}=0,\qquad \gamma_{L+1}=1,
\]

and, for \(a=L,L-1,\ldots,1\), set

\[
\begin{aligned}
 \beta_a={}&b_aV_{a-1}s
 +3\Theta_{a-1}^2b_a^2e+d\beta_{a+1}
 +\gamma_{a+1}^2\ell\\
 &+2\Theta_{a-1}\gamma_{a+1}b_am,
\end{aligned}
 \tag{6.6}
\]

\[
 \gamma_a
 =\pi_a+\Theta_{a-1}b_a(r+s)
  +\gamma_{a+1}(v+d).
 \tag{6.7}
\]

Then

\[
 \boxed{\mathsf S_{\phi,L}=T_L+3M_L,}
 \tag{6.8}
\]

\[
 \boxed{
 \mathsf H_{\phi,L}
 =V_L+\beta_1
  +\sum_{a=2}^L\bigl(\beta_a+\pi_aV_{a-1}\bigr).}
 \tag{6.9}
\]

Equations (6.1)--(6.9) require exactly nine one-dimensional Gaussian
integrals, \(L\) forward assignments, and \(L\) reverse assignments.  They
therefore terminate for every finite \(L\).  They are a literal Gaussian
activation-integral formula for the invariants, not a definition
through an unknown output.

If \(d=0\), continuity and the full support of Gaussian measure imply
\(\phi'\equiv0\).  RMS normalization gives \(\phi\equiv1\) or
\(\phi\equiv-1\).  Every hidden gradient vanishes,
\(F_{N,L}(h)=Nh\), and

\[
 \mathsf S_{\phi,L}=\mathsf H_{\phi,L}=J_{\phi,L}=0.
 \tag{6.10}
\]

## 7. Derivation of the activation recursion

Theorem 4.1 supplies one common \(C^3\) action germ.  In particular,
(4.1h)--(4.1j) make the straight-path response formula (7.1a) and every
differentiated response below legitimate.

At initialization, one layer has an independent local representative

\[
 Z_a\sim N(0,1),\qquad R_a\sim N(0,b_a),
 \qquad \Delta_a=R_ap(Z_a).
 \tag{7.1}
\]

Here is the independence check.  At the top, \(R_L=A\) lies in the seed
block orthogonal to the forward source block.  If \(R_a\) is centered and
independent of \(Z_a\), then (4.1i) gives

\[
 I_a^*\Delta_a
 =\mathbb E[R_aq(Z_a)]X_{a-1}=0.
\]

Hence \(R_{a-1}=J_a\Delta_a\) is a raw Gaussian in the outgoing block,
independent of the lower forward sources.  Downward induction proves
(7.1).  Its variance relation is \(b_L=1\),
\(b_{a-1}=db_a\), proving (6.2).

Differentiate the common perturbation germ on the straight path
in the frozen direction \(\mathbf g\).  At connector \(a\geq2\), its
forward action on that path is

\[
 Z_a(t)=I_a(X_{a-1}(t))
 +\mathbb E[\partial_{R_{a-1}}X_{a-1}(t)]\,\Delta_a
 +t\,\mathbb E[X_{a-1}(0)X_{a-1}(t)]\,\Delta_a.
 \tag{7.1a}
\]

The three terms are respectively the cylindrical source, its complete
transpose-history response, and the learned Hilbert--Schmidt action.  Put

\[
 G_{rs}^{a-1}=\mathbb E[X_{a-1}^{[r]}X_{a-1}^{[s]}],
 \qquad
 q_r^{a-1}=\mathbb E[\partial_{R_{a-1}}X_{a-1}^{[r]}].
\]

Differentiating (7.1a) inside the common isonormal realization gives

\[
\begin{aligned}
 Z_a^{[1]}&=I_a(X_{a-1}^{[1]})
 +(q_1^{a-1}+G_{00}^{a-1})\Delta_a,\\
 Z_a^{[2]}&=I_a(X_{a-1}^{[2]})
 +(q_2^{a-1}+2G_{01}^{a-1})\Delta_a,\\
 Z_a^{[3]}&=I_a(X_{a-1}^{[3]})
 +(q_3^{a-1}+3G_{02}^{a-1})\Delta_a.
\end{aligned}
 \tag{7.1b}
\]

Reverse-sign parity gives \(q_2^{a-1}=G_{01}^{a-1}=0\).  The induction
below gives

\[
 q_1^{a-1}=d\Theta_{a-2},qquad
 q_3^{a-1}=T_{a-1},qquad
 G_{02}^{a-1}=M_{a-1}.
 \tag{7.1c}
\]

Since RMS normalization gives \(G_{00}^{a-1}=1\), (7.1b)--(7.1c) show
that the response and learned terms combine to
\(1+d\Theta_{a-2}=\Theta_{a-1}\), and that the third response is exactly
\(T_{a-1}+3M_{a-1}\).  This proves, rather than assumes, every response
coefficient used below.  At \(a=1\), the input-weight path is simply
\(Z_1(t)=Z_1+t\Delta_1\).

The first preactivation variation at layer \(a\) is therefore

\[
 Z_a^{[1]}=E_{a1}+\Theta_{a-1}R_ap(Z_a),
 \qquad
 \mathbb E E_{a1}^2=V_{a-1},
 \tag{7.2}
\]

where \(E_{a1}\) is independent of \((Z_a,R_a)\).  Since
\(X_a^{[1]}=p(Z_a)Z_a^{[1]}\), squaring (7.2) gives (6.3).

Parity makes the second preactivation variation a centered Gaussian
\(E_{a2}\), with

\[
 \mathbb E[E_{a2}Z_a]=M_{a-1}.
 \tag{7.3}
\]

The scalar chain rule gives

\[
 X_a^{[2]}=q(Z_a)(Z_a^{[1]})^2+p(Z_a)E_{a2}.
 \tag{7.4}
\]

Multiplying by \(g(Z_a)\), taking expectation, and using one-dimensional
Gaussian integration by parts on the second term gives

\[
 \mathbb E[g p E_{a2}]
 =M_{a-1}\mathbb E[(gp)'(G)]
 =(d+v)M_{a-1}.
\]

The two pieces of the first term are \(vV_{a-1}\) and
\(\Theta_{a-1}^2b_am\).  This proves (6.4), with
\(M_a=\mathbb E[X_aX_a^{[2]}]\).

Let

\[
 T_a=\mathbb E[\partial_{R_a}X_a^{[3]}].
\]

The third scalar chain derivative is

\[
 X_a^{[3]}
 =r_3(Z_a)(Z_a^{[1]})^3
 +3q(Z_a)Z_a^{[1]}E_{a2}
 +p(Z_a)Z_a^{[3]}.
 \tag{7.5}
\]

The exact forward response formula gives

\[
 \partial_{R_a}Z_a^{[1]}=\Theta_{a-1}p(Z_a),
 \qquad
 \partial_{R_a}Z_a^{[3]}
 =(T_{a-1}+3M_{a-1})p(Z_a).
 \tag{7.6}
\]

Differentiate the three terms in (7.5) with respect to \(R_a\).  Their
four nonzero contractions are, respectively,

\[
 3\Theta_{a-1}V_{a-1}r,qquad
 3\Theta_{a-1}^3b_aj,qquad
 3\Theta_{a-1}M_{a-1}(r+s),
\]

\[
 d(T_{a-1}+3M_{a-1}).
\]

This is (6.5).  At the top layer, Gaussian integration by parts in the
readout carrier \(R_L=A\), together with the derivative of the readout
itself, gives

\[
 D^3\mathcal F[\mathbf g^3]=T_L+3M_L,
\]

which proves (6.8).

For (6.6)--(6.9), differentiate the reverse carrier and cotangent along
\(\mathbf g\).  For \(a<L\), before simplifying responses, the derivative
of the transpose oracle at connector \(a+1\) has the finite jet-basis form

\[
 \widetilde R_a
 =B_a+\pi_{a+1}X_a
  +\sum_{r=0}^3\varrho_{a+1,r}X_a^{[r]},
 \qquad
 \varrho_{a+1,r}
 =\mathbb E[\partial_{E_{a+1,r}}\widetilde\Delta_{a+1}].
 \tag{7.7a}
\]

Here \(B_a\) is the isonormal derivative of the raw transpose source and
\(E_{a+1,r}=I_{a+1}(X_a^{[r]})\).  This list contains every possible
response through cubic order.

We now eliminate the spurious-looking terms in (7.7a).  Under the
reverse-sign involution, base reverse carriers and odd source jets change
sign while even source jets do not.  Induction through (7.1b) gives

\[
 X_a^{[r]}\longmapsto(-1)^rX_a^{[r]}.
\]

Starting at the readout and descending, \(\widetilde\Delta_{a+1}\) uses
only the zeroth and first forward source jets.  Hence
\(\varrho_{a+1,2}=\varrho_{a+1,3}=0\).  Directly,

\[
 \partial_{E_{a+1,1}}\widetilde\Delta_{a+1}
 =q(Z_{a+1})R_{a+1},
\]

whose expectation is zero because \(R_{a+1}\) is centered and independent
of \(Z_{a+1}\).  Thus \(\varrho_{a+1,1}=0\).  The base cotangent is odd
and its derivative is even, so

\[
 \mathbb E[\Delta_{a+1}\widetilde\Delta_{a+1}]=0.
\]

The jointly Gaussian raw-source derivative \(B_a\) is consequently
uncorrelated with, hence independent of, the local base reverse carrier.
Only \(\varrho_{a+1,0}\) remains.  Combining it with the learned coefficient
\(\pi_{a+1}\) defines \(\gamma_{a+1}\) and reduces (7.7a) to the exact
local forms below.  At the top,
\(\widetilde R_L=X_L\), which is the same formula with
\((\beta_{L+1},\gamma_{L+1})=(0,1)\):

\[
 \widetilde R_a=B_a+\gamma_{a+1}g(Z_a),
 \qquad \mathbb EB_a^2=\beta_{a+1},
 \tag{7.7}
\]

\[
 \widetilde\Delta_a
 =q(Z_a)Z_a^{[1]}R_a+p(Z_a)\widetilde R_a,
 \tag{7.8}
\]

where \(B_a\) is independent of the local forward and reverse variables.
The five nonzero terms in the square of (7.8) are

\[
 b_aV_{a-1}s,\quad
 3\Theta_{a-1}^2b_a^2e,\quad
 d\beta_{a+1},\quad
 \gamma_{a+1}^2\ell,\quad
 2\Theta_{a-1}\gamma_{a+1}b_am.
\]

Their sum is (6.6).  Differentiating (7.8) in the base forward innovation
gives the response

\[
 \Theta_{a-1}b_a(r+s)+\gamma_{a+1}(v+d).
\]

The learned transpose term contributes \(\pi_a\), proving (6.7).

Finally, \(D\mathbf g[\mathbf g]\) has orthogonal parameter blocks.  The
readout block contributes \(V_L\), the first-layer block contributes
\(\beta_1\), and matrix block \(a\) contributes

\[
 \beta_a+\pi_aV_{a-1}.
\]

Its possible cross term vanishes because
\(\mathbb E[X_{a-1}X_{a-1}^{[1]}]=0\) by the same reverse-sign parity.
Summing the blocks proves (6.9), and also proves
\(\mathsf H_{\phi,L}\geq0\) directly.

## 8. The explicit depth-three specialization

For \(L=3\), use the nine moments (6.1) and set

\[
 \Theta_0=1,\quad \Theta_1=1+d,\quad
 \Theta_2=1+d+d^2,\quad \Theta_3=1+d+d^2+d^3,
\]

\[
 b_1=d^2,\qquad b_2=d,\qquad b_3=1.
\]

Run (6.3)--(6.5) for \(a=1,2,3\), then run (6.6)--(6.7) for
\(a=3,2,1\), starting from \((\beta_4,\gamma_4)=(0,1)\).  The two
invariants are

\[
 \boxed{\mathsf S_{\phi,3}=T_3+3M_3,}
\]

\[
 \boxed{
 \mathsf H_{\phi,3}
 =V_3+\beta_1+(\beta_2+d^2V_1)+(\beta_3+dV_2).}
 \tag{8.1}
\]

Thus

\[
 \boxed{
 J_{\phi,3}
 =T_3+3M_3
 +4\{V_3+\beta_1+\beta_2+d^2V_1+\beta_3+dV_2\}.}
 \tag{8.2}
\]

This is a fixed, terminating formula involving only nine scalar Gaussian
activation integrals.

## 9. Audits and exact checks

### 9.1 Reduction to the audited depth-two polynomial

At \(L=2\), put

\[
 c=1+d,qquad \beta=v+cr,qquad
 \delta=d+cs,qquad k=d+\beta+\delta.
\]

Expanding (6.3)--(6.9) gives

\[
 \mathsf S_{\phi,2}
 =3c^2m+3c^3j+3du\beta+3dkm+3d^2j,
 \tag{9.1}
\]

\[
\begin{aligned}
 \mathsf H_{\phi,2}={}&c^2u+c\ell+2c^2m+3c^3e+cuds
 +2ud^2+3d^2e\\
 &+k^2\ell+2dkm.
\end{aligned}
 \tag{9.2}
\]

After the harmless renaming
\((u,v,s,e)=(e_{\rm old},b_{\rm old},v_{\rm old},s_{\rm old})\),
these are exactly the independently derived two-hidden-layer invariants.
This checks every coefficient in the general recursion against the known
depth-two result.

### 9.2 Constant activation

For \(\phi\equiv\pm1\), all nine derivative moments vanish.  Equations
(6.10), (1.3), and (1.6) agree with the exact output
\(F_{N,L}(h)=Nh\).

### 9.3 Identity activation at every depth

For \(\phi(x)=x\),

\[
 d=u=\ell=1,qquad v=m=r=s=j=e=0.
\]

The recursion gives

\[
 \Theta_a=a+1,qquad
 V_a=\sum_{q=1}^a q^2,qquad
 \beta_a=\sum_{q=1}^{L-a+1}q^2,qquad
 \mathsf S_{x,L}=0,
\]

and hence

\[
 \boxed{
 \mathsf H_{x,L}
 =2\sum_{q=1}^L(L-q+1)q^2
 =\frac{L(L+1)^2(L+2)}6.}
 \tag{9.3}
\]

Therefore

\[
 J_{x,L}=\frac{2L(L+1)^2(L+2)}3,
\]

\[
 \boxed{
 \kappa^{\mathrm{comp}}_{x,L,t}
 =-\frac{t(2t-1)L(L+1)^2(L+2)}3.}
 \tag{9.4}
\]

At \(L=3\), this gives

\[
 (V_1,V_2,V_3)=(1,5,14),qquad
 (\beta_3,\beta_2,\beta_1)=(1,5,14),
\]

\[
 \mathsf H_{x,3}=40,qquad J_{x,3}=160,qquad
 \kappa^{\mathrm{comp}}_{x,3,t}=-80t(2t-1).
 \tag{9.5}
\]

This agrees with the independent bounded cyclic-operator closure of the
fully trained depth-three linear model: its exact continuous feature-flow
output has \(F^{(3)}(0)=160\); see
`../identity_compiler/linear_gaussian_program/depth3_unfrozen_readout_closure/THEOREM_AND_PROOF.md`,
equation (7.6).  For an exact gradient flow the third
derivative is \(2\mathsf S+4\mathsf H\), which here equals \(160\).
Thus the depth-three value \(\mathsf H=40\) is checked by a representation
that does not use the discrete-time recursion above.

### 9.4 General affine activation

Let

\[
 \phi(x)=\alpha x+\beta,qquad \alpha^2+\beta^2=1,
 \qquad d=\alpha^2>0.
\]

Then

\[
 u=d^2,qquad \ell=d,qquad
 v=m=r=s=j=e=0.
\]

Equations (6.4)--(6.5) give \(M_a=T_a=0\) at every layer, hence

\[
 \boxed{\mathsf S_{\phi,L}=0.}
\]

The remaining recursion reduces, without a signed cancellation, to

\[
 V_a=dV_{a-1}+\Theta_{a-1}^2d^{L-a+2},
 \qquad V_0=0,
\]

\[
 \gamma_a=d^{L-a+1}+d\gamma_{a+1}
 =(L-a+2)d^{L-a+1},
\]

\[
 \beta_a=d\beta_{a+1}+d\gamma_{a+1}^2,
 \qquad (\beta_{L+1},\gamma_{L+1})=(0,1).
\]

Thus \(\mathsf H_{\phi,L}\) is the sum of the explicitly nonnegative
terms in (6.9), and

\[
 \kappa^{\mathrm{comp}}_{\phi,L,t}
 =-2t(2t-1)\mathsf H_{\phi,L}.
\]

At \(d=1\) these equations reduce to the identity-activation audit above;
at \(d=0\) they reduce to the separately treated constant branch.

## 10. A shared activation base and explicit depth majorant

For later quantitative use, define the single activation-only base

\[
 A_\phi=\max\{4,4M_\phi^4\}.
 \tag{10.1}
\]

The elementary bounds

\[
 \mathbb E(1+|G|)\leq2,qquad
 \mathbb E(1+|G|)^2\leq4
\]

show that the absolute value of every moment in (6.1) is at most
\(A_\phi\).  The following completely numerical recursion therefore
majorizes \(|J_{\phi,L}|\).  Put

\[
 A=A_\phi,qquad \overline\Theta=A^{2L},qquad
 \overline b=A^L,qquad \overline\pi=A^{L+1},
\]

initialize \(\overline V_0=\overline M_0=\overline T_0=0\), and for
\(a=1,\ldots,L\) set

\[
 \overline V_a=A\overline V_{a-1}
 +\overline\Theta^2\overline b A,
\]

\[
 \overline M_a=A\overline V_{a-1}
 +\overline\Theta^2\overline b A
 +2A\overline M_{a-1},
\]

\[
\begin{aligned}
 \overline T_a={}&3\overline\Theta\overline V_{a-1}A
 +3\overline\Theta^3\overline bA
 +6\overline\Theta\overline M_{a-1}A\\
 &+A(\overline T_{a-1}+3\overline M_{a-1}).
\end{aligned}
 \tag{10.2}
\]

Put \((\overline\beta_{L+1},\overline\gamma_{L+1})=(0,1)\), and for
\(a=L,\ldots,1\) set

\[
\begin{aligned}
 \overline\beta_a={}&
 \overline b\,\overline V_{a-1}A
 +3\overline\Theta^2\overline b^2A
 +A\overline\beta_{a+1}
 +A\overline\gamma_{a+1}^2\\
 &+2\overline\Theta\overline\gamma_{a+1}\overline bA,
\end{aligned}
\]

\[
 \overline\gamma_a
 =\overline\pi+2A\overline\Theta\overline b
  +2A\overline\gamma_{a+1}.
 \tag{10.3}
\]

Finally define

\[
 \overline S_L=\overline T_L+3\overline M_L,
\]

\[
 \overline H_L=\overline V_L+\overline\beta_1
 +\sum_{a=2}^L
   (\overline\beta_a+\overline\pi\,\overline V_{a-1}),
\]

\[
 \overline J_L=\overline S_L+4\overline H_L.
 \tag{10.4}
\]

Termwise induction in (6.3)--(6.9) proves

\[
 |J_{\phi,L}|\leq\overline J_L,
 \qquad
 |\kappa^{\mathrm{comp}}_{\phi,L,t}|
 \leq\frac{t(2t-1)}2\overline J_L.
 \tag{10.5}
\]

The only activation-dependent quantity in (10.2)--(10.5) is the shared
base \(A_\phi\); the number of assignments and every exponent involving
depth are explicit.  The construction terminates after two passes of length
\(L\) (three scalar assignments per forward layer and two per reverse
layer).

## 11. Exact scope

Proved here:

1. the finite-query cylindrical adjoint identity at singular Grams;
2. a common \(C^3\) perturbation DAG for exactly the directions needed at
   cubic order;
3. the order-three intertwining of the inverse-free temporal DAG with
   explicit Euler gradient ascent;
4. the universal two-invariant time polynomial (1.3);
5. the one-invariant discrepancy law (1.6);
6. the terminating nine-integral recursion at arbitrary fixed depth;
7. the depth-three and affine/constant consistency checks.

Not proved here:

1. pointwise finite-width identification at arbitrary fixed \(h\) and
   arbitrary time horizon;
2. nonterminal history-Gram rank on a punctured \(h\)-interval;
3. a fifth-order activation-envelope remainder;
4. a uniform-in-time \(t^4|h|^5\) remainder.

Those are logically separate from the cubic law.  In particular, this note
does not use a finite-width Taylor expansion or any interchange of the
width and learning-rate limits.

The original finite-list bridge failed the hostile audit in
`AUDIT_CUBIC.md`.  The fixed bounded-operator replacement above was then
audited from scratch in `AUDIT_CUBIC_REAUDIT.md`; that re-audit passes the
simultaneous construction, singular response identities, generated-core
regularity, temporal-DAG equality, and cubic coefficient.
