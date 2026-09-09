# Quantitative three-time Gram rank

Throughout, `G\sim N(0,1)`, `\mathbb E[\phi(G)^2]=1`, and

$$
\phi\in C^{12}(\mathbb R),\qquad
M_\phi=
\max\left\{1,\sup_x\frac{|\phi(x)|}{1+|x|},
\max_{1\le j\le12}\|\phi^{(j)}\|_\infty\right\}<\infty.
$$

Set

$$
d=\mathbb E[\phi'(G)^2]>0,\qquad
e=\mathbb E[\phi'(G)^4],\qquad
t=\mathbb E[\phi''(G)^2].
$$

Use the activation moments of the two-time proof

$$
c=1+d,\qquad
k=d+\beta+\delta,
$$

where

$$
\beta=\mathbb E[\phi(G)\phi''(G)]
+c\mathbb E[\phi'(G)\phi'''(G)],
$$

$$
\delta=d+c\mathbb E[\phi''(G)^2],
$$

and

$$
\tau
=\ell+2cm+3c^2s+edt>0,
$$

where

$$
\ell=\mathbb E[\phi(G)^2\phi'(G)^2],\qquad
m=\mathbb E[\phi(G)\phi''(G)\phi'(G)^2],\qquad
s=\mathbb E[\phi''(G)^2\phi'(G)^2].
$$

For completeness, \(\tau\) is strictly positive under \(d>0\).  If
\(A,Z,G\) are independent standard Gaussians, then

$$
V=\phi(G)\phi'(G)+\sqrt{de}\,AZ\phi''(G)
+cA^2\phi'(G)\phi''(G)
$$

satisfies \(\mathbb E[V^2]=\tau\).  If \(t>0\), its \(Z\)-dependent
component has squared norm \(edt>0\).  If \(t=0\), continuity makes
\(\phi\) affine and then \(\tau=\ell=d>0\).

The definitions of `\beta,\delta` are not needed below except through the
explicit activation number `k`.

## Lemma

Let `Q^{[2]}(h)=(\mathbb E[H_rH_s])_{0\le r,s\le2}` and
`K^{[2]}(h)=(\mathbb E[C_rC_s])_{0\le r,s\le2}` be the population Grams in
the width-first three-step Gaussian operator recursion.  There are explicit,
finite, activation-defined numbers

$$
r_{Q,3}>0,\qquad r_{K,3}>0
$$

such that, for every

$$
0<|h|\le r_3:=\min\{r_{Q,3},r_{K,3}\},
$$

both `Q^{[2]}(h)` and `K^{[2]}(h)` are positive definite.  No
nondegeneracy assumption beyond `d>0` is required.

The radii use only:

1. explicit Gaussian integrals of `\phi,\ldots,\phi'''`;
2. derivative bounds through order five for the entries of `Q^{[2]}` and
   `K^{[2]}` returned by the activation-envelope compiler;
3. integer arithmetic, factorials, and eigenvalue bounds for explicit
   three-by-three matrices.

In particular, `C^{12}` is sufficient.

## Proof

### 1. Lower forward-difference jets

Let `U,B,T` be independent centered Gaussians with variances

$$
\mathbb E[U^2]=1,\qquad \mathbb E[B^2]=d,\qquad
\mathbb E[T^2]=\tau.
$$

With `p=\phi'(U)` and `q=\phi''(U)`, define

$$
P_0=\phi(U),\qquad P_1=Bp^2,
$$

$$
P_2=Tp^2+k\phi(U)p^2+2B^2p^2q.
$$

We first derive these variables directly.  The two-time cotangent Gram has

$$
K_{01}(h)=d+O(h^2),\qquad
K_{11}(h)-\frac{K_{01}(h)^2}{d}=\tau h^2+O(h^4).
$$

On the already certified two-time punctured interval it therefore has the
Gaussian realization

$$
\chi_0=B,\qquad
\chi_1=\frac{K_{01}(h)}dB
+h\sqrt{\frac{K_{11}(h)-K_{01}(h)^2/d}{h^2}}\,Z,
$$

where `Z` is independent standard Gaussian.  Hence

$$
\chi_1=B+hT+o_{L^p}(h)
$$

for every finite `p`; changing the sign of `Z` for negative `h` gives the
same covariance and the same two-sided conclusion.

The first lower update is exact:

$$
u_1=U+hBp.
$$

The first derivatives of the top response coefficients, obtained directly
from their Gaussian integrals, are

$$
\sigma_{10}(h)=\delta h+O(h^3),\qquad
\sigma_{11}(h)=\beta h+O(h^3),\qquad
K_{01}(h)=d+O(h^2).
$$

Consequently the second lower preactivation direction obeys

$$
b_1=B+h\{T+k\phi(U)\}+o_{L^p}(h).
$$

Since

$$
u_2=u_1+h b_1\phi'(u_1),
$$

Taylor's formula with integral remainder gives

$$
u_2
=U+2hBp
+h^2\{(T+k\phi(U))p+B^2pq\}
+o_{L^p}(h^2).
$$

The bounded third derivative of `\phi`, together with the Gaussian moment
bounds, makes each displayed remainder `o_{L^p}`.  Applying `\phi` once
more yields

$$
H_0=P_0,
$$

$$
\frac{H_1-H_0}{h}\longrightarrow P_1,
$$

and

$$
\frac{H_2-2H_1+H_0}{h^2}\longrightarrow P_2
$$

in every finite `L^p`.

Independence and the centered Gaussian moments give

$$
\mathbb E[P_0P_1]=0,\qquad
\mathbb E[P_1P_2]=0,\qquad
\mathbb E[P_1^2]=de.
$$

Indeed, every term in `P_0P_1` contains `B`; the three terms in
`P_1P_2` contain respectively `BT`, `B`, and `B^3`.

Put

$$
a_Q=\mathbb E[P_0P_2]
=k\ell+2dm,
$$

$$
\lambda_Q=\mathbb E[P_2^2]-a_Q^2.
$$

The summand `Tp^2` is orthogonal to `P_0,P_1` and to the other two summands
of `P_2`.  Therefore

$$
\lambda_Q\ge\mathbb E[T^2p^4]=\tau e>0.
$$

Thus the explicit lower jet Gram is

$$
G_Q:=\operatorname{Gram}(P_0,P_1,P_2)
=\begin{pmatrix}
1&0&a_Q\\
0&de&0\\
a_Q&0&\mathbb E[P_2^2]
\end{pmatrix},
$$

and

$$
\det G_Q=de\lambda_Q>0.
$$

### 2. Top forward-difference jets

Let `Z_0,Z_1,Z_2,A` be independent standard Gaussians and define

$$
X=Z_0,\qquad S=\sqrt{de}\,Z_1,\qquad
R=a_QZ_0+\sqrt{\lambda_Q}\,Z_2.
$$

Then `(X,S,R)` has Gram `G_Q`.  Evaluate

$$
g=\phi(X),\qquad p=\phi'(X),\qquad
q=\phi''(X),\qquad r=\phi'''(X),
$$

and set

$$
R_1=S+cAp,
$$

$$
T_0=Ap,\qquad T_1=gp+AqR_1,
$$

$$
R_2=R+cT_1,
$$

$$
T_2=p^2R_1+AqR_2+2gqR_1+ArR_1^2.
$$

We derive these variables from the top operator.  In the lower Newton basis,
the raw Gaussian coordinates can be coupled so that

$$
\xi_0\longrightarrow X,\qquad
\frac{\xi_1-\xi_0}{h}\longrightarrow S,\qquad
\frac{\xi_2-2\xi_1+\xi_0}{h^2}\longrightarrow R
$$

in every finite `L^p`.  The first response jets are

$$
\frac{L_{10}}h\longrightarrow c,\qquad
\frac{L_{20}}h\longrightarrow c,\qquad
\frac{L_{21}}h\longrightarrow c.
$$

All three response functions are odd, so their errors after the displayed
linear term are `O(h^3)`.  It follows that

$$
\frac{z_1-z_0}{h}\longrightarrow R_1.
$$

Moreover, from

$$
z_2-2z_1+z_0
=(\xi_2-2\xi_1+\xi_0)
+(L_{20}-2L_{10})C_0+L_{21}C_1,
$$

we obtain

$$
\frac{z_2-2z_1+z_0}{h^2}\longrightarrow R+cT_1=R_2.
$$

Now

$$
a_1=A+hg,\qquad
a_2=A+h\{g+\phi(z_1)\}.
$$

Write, temporarily,

$$
z_1=X+hR_1+h^2V+o_{L^p}(h^2).
$$

The preceding second-difference limit gives

$$
z_2=X+2hR_1+h^2(2V+R_2)+o_{L^p}(h^2).
$$

Taylor-expanding `a_s\phi'(z_s)` gives

$$
C_1
=Ap+h(gp+AqR_1)
+h^2\left(AqV+\frac12ArR_1^2+gqR_1\right)
+o_{L^p}(h^2),
$$

and

$$
\begin{aligned}
C_2
={}&Ap+2h(gp+AqR_1)\\
&+h^2\{p^2R_1+4gqR_1+Aq(2V+R_2)+2ArR_1^2\}
+o_{L^p}(h^2).
\end{aligned}
$$

The unknown second-order variable `V` cancels in the second difference.
Therefore

$$
C_0\longrightarrow T_0,\qquad
\frac{C_1-C_0}{h}\longrightarrow T_1,
$$

$$
\frac{C_2-2C_1+C_0}{h^2}\longrightarrow T_2
$$

in every finite `L^p`.

Direct Gaussian expansion gives

$$
\mathbb E[T_0T_1]=0,\qquad
\mathbb E[T_0^2]=d,\qquad
\mathbb E[T_1^2]=\tau.
$$

For the last identity, the three square contributions and the only
nonzero cross term are

$$
\ell,\qquad edt,\qquad 3c^2s,\qquad 2cm.
$$

Define

$$
\lambda_K
=\mathbb E[T_2^2]
-\frac{\mathbb E[T_0T_2]^2}{d}
-\frac{\mathbb E[T_1T_2]^2}{\tau}.
$$

This is the squared norm of the residual of `T_2` after projection onto the
orthogonal pair `(T_0,T_1)`.

Suppose first that `t>0`.  The only dependence of `T_2` on `Z_2` is

$$
Aq\sqrt{\lambda_Q}\,Z_2.
$$

It is orthogonal to `T_0,T_1` and to the remainder of `T_2`, all of which
are measurable with respect to `(A,Z_0,Z_1)`.  Hence

$$
\lambda_K\ge\lambda_Q\mathbb E[A^2q^2]
=t\lambda_Q>0.
$$

If `t=0`, continuity implies `\phi''\equiv0`; write

$$
\phi(x)=\alpha x+\beta,\qquad d=\alpha^2>0.
$$

Then

$$
T_0=\alpha A,\qquad
T_1=\alpha(\alpha Z_0+\beta),
$$

and

$$
T_2=\alpha^2\{\sqrt{de}\,Z_1+c\alpha A\}.
$$

Projection removes the `A` component, while the `Z_1` component is
orthogonal to `T_1`.  Thus

$$
\lambda_K=\alpha^4de=\alpha^{10}=d^5>0.
$$

The explicit upper jet Gram

$$
G_K:=\operatorname{Gram}(T_0,T_1,T_2)
$$

therefore satisfies

$$
\det G_K=d\tau\lambda_K>0.
$$

This proves universal positivity, including the affine case.

### 3. Quantitative radius from only fifth derivatives

For either `G=Q^{[2]}` or `G=K^{[2]}`, let

$$
c_{ar}=(-1)^{a-r}\binom ar,\qquad 0\le r\le a\le2,
$$

and define

$$
N_{ab}(h)
=\sum_{r=0}^a\sum_{s=0}^b c_{ar}c_{bs}G_{rs}(h).
$$

For `h\ne0`, set

$$
\widehat G_{ab}(h)=\frac{N_{ab}(h)}{h^{a+b}}.
$$

This is exactly the Gram of the three forward-difference fields

$$
X_0,\qquad \frac{X_1-X_0}{h},\qquad
\frac{X_2-2X_1+X_0}{h^2}.
$$

Equivalently, if

$$
D_h=\begin{pmatrix}
1&0&0\\
-h^{-1}&h^{-1}&0\\
h^{-2}&-2h^{-2}&h^{-2}
\end{pmatrix},
$$

then

$$
\widehat G(h)=D_hG(h)D_h^\top,\qquad
\det G(h)=h^6\det\widehat G(h).
$$

The `L^2` jet limits just proved imply

$$
N_{ab}(h)=O(|h|^{a+b}).
$$

The operator Price lemma makes every `N_{ab}` five-times continuously
differentiable.  Taylor's theorem then forces

$$
N_{ab}^{(j)}(0)=0,\qquad j<a+b,
$$

and gives

$$
\widehat G_{ab}(0)
:=\frac{N_{ab}^{(a+b)}(0)}{(a+b)!}.
$$

The matrices so obtained at zero are exactly `G_Q` and `G_K`, respectively.

Let the activation-envelope compiler return numerical bounds

$$
\overline G_{rs,j}
\ge\sup_{|h|\le1}|G_{rs}^{(j)}(h)|,
\qquad 0\le r,s\le2,\quad 0\le j\le5.
$$

These numbers are not defined using the unknown output.  They are obtained
chronologically from the Gaussian activation nodes for the entries of
`Q^{[2]}` and `K^{[2]}` by the finite rules

$$
\Psi_0=\psi,\qquad
\Psi_{j+1}=\partial_h\Psi_j+\frac12C'(h):D_x^2\Psi_j,
$$

together with the weighted envelope arithmetic

$$
(A,p)\oplus(B,q)=(A+B,\max\{p,q\}),
$$

$$
(A,p)\odot(B,q)=(AB,p+q),
$$

and the explicit Gaussian moment

$$
\mu_{m,p}(v)
=\sum_{j=0}^p\binom pjv^{j/2}2^{j/2}
\frac{\Gamma((m+j)/2)}{\Gamma(m/2)}.
$$

Every covariance or response coefficient needed by a node is compiled
before that node.  The chronological list is

$$
(Q_{0:1},\rho_1),\quad
(K_{0:1},\sigma_1),\quad
(Q_{r2},\rho_2),\quad
(K_{r2}).
$$

Thus the compiler is finite and acyclic.

For `0\le a,b\le2`, put

$$
E^G_{ab}
=\frac1{(a+b+1)!}
\sum_{r=0}^a\sum_{s=0}^b
\binom ar\binom bs\,
\overline G_{rs,a+b+1},
$$

and

$$
E_G=\left(\sum_{a,b=0}^2(E^G_{ab})^2\right)^{1/2}.
$$

Taylor's formula with integral remainder, using the preceding vanishing
derivatives, gives explicitly

$$
|\widehat G_{ab}(h)-\widehat G_{ab}(0)|
\le E^G_{ab}|h|,
$$

and therefore

$$
\|\widehat G(h)-\widehat G(0)\|_{\mathrm{op}}
\le E_G|h|.
$$

The largest derivative index in this formula is

$$
a+b+1\le5.
$$

This is why an eighth derivative of the determinant is neither used nor
needed.

For a positive three-by-three matrix `A`,

$$
\lambda_{\min}(A)
\ge\frac{\det A}{(\operatorname{tr}A)^2},
$$

because the product of the two larger eigenvalues is at most
`(\operatorname{tr}A)^2`.  Define the explicit activation numbers

$$
\underline\lambda_Q
=\frac{de\lambda_Q}{(\operatorname{tr}G_Q)^2},
$$

$$
\underline\lambda_K
=\frac{d\tau\lambda_K}{(\operatorname{tr}G_K)^2}.
$$

Let `r_2>0` be the already explicit two-time rank radius and set

$$
r_{Q,3}
=\min\left\{r_2,1,
\frac{\underline\lambda_Q}{2(1+E_Q)}\right\},
$$

$$
r_{K,3}
=\min\left\{r_{Q,3},1,
\frac{\underline\lambda_K}{2(1+E_K)}\right\}.
$$

Weyl's inequality now yields, for `0<|h|\le r_{Q,3}`,

$$
\lambda_{\min}(\widehat Q(h))
\ge\underline\lambda_Q-E_Q|h|
\ge\frac12\underline\lambda_Q>0,
$$

and, for `0<|h|\le r_{K,3}`,

$$
\lambda_{\min}(\widehat K(h))
\ge\frac12\underline\lambda_K>0.
$$

The forward-difference matrix `D_h` is invertible whenever `h\ne0`, so the
original Grams are positive definite on the same punctured interval.

If the finite-query coupling needs an explicit population inverse bound,
let

$$
T_Q=\sum_{r=0}^2\overline Q_{rr,0},\qquad
T_K=\sum_{r=0}^2\overline K_{rr,0}.
$$

Since `\det G=h^6\det\widehat G` and all three eigenvalues of
`\widehat G` are at least the displayed lower bound,

$$
\lambda_{\min}(Q^{[2]}(h))
\ge
\frac{|h|^6(\underline\lambda_Q/2)^3}{T_Q^2},
$$

$$
\lambda_{\min}(K^{[2]}(h))
\ge
\frac{|h|^6(\underline\lambda_K/2)^3}{T_K^2}.
$$

Every principal submatrix has smallest eigenvalue at least that of the full
positive matrix.  Moreover, if \(S\) is the scalar Schur complement of the
last coordinate, then

$$
S^{-1}=(G^{-1})_{33}\le\|G^{-1}\|_{\mathrm{op}}
=\lambda_{\min}(G)^{-1},
$$

so \(S\ge\lambda_{\min}(G)\).  Hence the same displayed
activation-defined numbers lower-bound every nonterminal population
innovation required by the seven-query conditioning proof.  Empirical
Schur-complement convergence then uses only the inverse identity on the event
where the empirical Gram differs from its population value by less than half
this fixed-step bound.

These are positive at each fixed nonzero `h`; their deterioration as
`h\to0` does not exchange the width and learning-rate limits.

### 4. Why `C^{12}` suffices

The rank radius requests only fifth derivatives of Gaussian Gram entries.
At derivative order five, repeated Price differentiation introduces at most
ten Gaussian-coordinate derivatives.  A response integrand begins with at
most two activation derivatives already present.  Hence no derivative above
`\phi^{(12)}` occurs.  All undifferentiated activations have at most linear
growth, and every differentiated activation is bounded, so the weighted
envelope and the explicit Gaussian moments dominate every term.

Thus the compiler bounds used above are finite under precisely the stated
`C^{12}` activation class.  The proof requires neither analyticity nor any
additional activation nondegeneracy.  This completes the lemma.
