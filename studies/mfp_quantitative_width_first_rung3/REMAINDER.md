# Activation-only remainder for \(F_3(h)-F_1(3h)\)

This note supplies the regularity, envelope, domain, parity, and Taylor
remainder components of the three-versus-one comparison. It uses the exact
finite network and the proved singular-Price and envelope lemmas in
../temporary_quantitative_width_first_bound/PROOF.md. No finite-width
learning-rate expansion is used.

Assume throughout

\[
\phi\in C^{12}(\mathbb R),\qquad
\mathbb E[\phi(G)^2]=1,
\]

and

\[
M_\phi
=\max\left\{
1,\sup_x\frac{|\phi(x)|}{1+|x|},
\max_{1\le r\le12}\|\phi^{(r)}\|_\infty
\right\}<\infty.
\]

## 1. Exact three-step operator recursion

The recursion below is the object that must first be identified as the
width limit at each fixed \(h\ne0\).

Let \(U,A\) be independent standard Gaussians and set

\[
u_0=U,\qquad H_0=\phi(U).
\]

At a top stage \(s\), let

\[
\xi^{[s]}=(\xi_0,\ldots,\xi_s)\sim N(0,Q^{[s]}),
\qquad
Q^{[s]}_{rt}=\mathbb E[H_rH_t],
\]

independently of \(A\). Recompute all preceding top variables in this joint
Gaussian block, then set

\[
z_s=\xi_s+\sum_{r<s}L_{sr}C_r,
\qquad
L_{sr}=\rho_{sr}+hQ^{[s]}_{rs},
\]

\[
a_s=A+h\sum_{r<s}\phi(z_r),
\qquad
C_s=a_s\phi'(z_s).
\]

If the stage is nonterminal, define

\[
K^{[s]}_{rt}=\mathbb E[C_rC_t],
\qquad
\sigma_{sr}=\mathbb E[\partial_{\xi_r}C_s],
\qquad 0\le r,t\le s.
\]

At the following lower stage take

\[
\chi^{[s]}=(\chi_0,\ldots,\chi_s)\sim N(0,K^{[s]})
\]

independently of \(U\), recompute all preceding lower variables in this
block, and set

\[
b_s
=\chi_s+\sum_{r\le s}\sigma_{sr}H_r
 +h\sum_{r<s}K^{[s]}_{rs}H_r,
\]

\[
u_{s+1}=u_s+hb_s\phi'(u_s),
\qquad
H_{s+1}=\phi(u_{s+1}),
\]

\[
\rho_{s+1,r}
=\mathbb E[\partial_{\chi_r}H_{s+1}],
\qquad 0\le r\le s.
\]

Here \(\sigma_{00}=0\), since
\(\mathbb E[A\phi''(\xi_0)]=0\). Run the nonterminal top/lower stages for
\(s=0,1,2\). The terminal top stage is

\[
z_3=\xi_3+\sum_{r=0}^2L_{3r}C_r,
\qquad
a_3=A+h\sum_{r=0}^2\phi(z_r),
\]

\[
F_3(h)=\mathbb E[a_3\phi(z_3)].
\]

At finite width the required source-matrix reveal order is exactly

\[
Y^0,D^0,Y^1,D^1,Y^2,D^2,Y^3,
\qquad
Y^s=\frac{WH^s}{\sqrt n},
\quad
D^s=\frac{W^\top C^s}{\sqrt n}.
\]

The learned-matrix terms are exactly

\[
z^s=Y^s+h\sum_{r<s}Q_{rs}^{(n)}C^r,
\qquad 0\le s\le3,
\]

and

\[
b^s=D^s+h\sum_{r<s}K_{rs}^{(n)}H^r,
\qquad 0\le s\le2.
\]

Thus the displayed Gaussian recursion retains every reused-\(W\) response
and every learned rank-one term.

### Fixed-\(h\) identification of the two added actions

The complete good-event, concentration, response, and uniform-integrability
proof is given in
../temporary_quantitative_width_first_bound_rung3/WIDTH_IDENTIFICATION.md.
The calculation below records how its two added actions attach to the
operator recursion. In particular, this section invokes the full
stage-by-stage proof there, not an unnamed state-evolution induction.

For \(0<|h|\le h_{31,\phi}\), Section 4 below proves that
\(Q^{[2]}\) and \(K^{[2]}\) are positive definite. Rerun the stopped
normalized-\(L^p\) coupling in Section 4.2 of the two-step proof, now treating
\(Y^2\) as nonterminal. Its innovation Schur complement is positive because
\(Q^{[2]}\succ0\), so the square-root coefficient is locally Lipschitz and
the existing one-action estimate gives the \(O(n^{-1/2})\) coupling rate
needed by the next query.

After \(Y^2\), the exact coordinate updates make \(C^2\) measurable before
the next matrix action. The sixth action is

\[
D^2=\frac{W^\top C^2}{\sqrt n}.
\]

Its old row-query block is \((H^0,H^1,H^2)\), its old column-query block is
\((C^0,C^1)\), and its new empirical data are

\[
K_{02}^{(n)},K_{12}^{(n)},K_{22}^{(n)},
\qquad
\frac{(Y^r)^\top C^2}{n}\quad(0\le r\le2).
\]

The exact conditional innovation variance is the Schur complement of
\(K^{[1]}\) in \(K^{[2]}\), which is strictly positive. The one-action
coupling proof therefore applies with inverse norms bounded by the fixed
population eigenvalues of \(Q^{[2]}(h)\) and \(K^{[1]}(h)\).

To identify its conditional mean without losing reused-matrix dependence,
write all preceding raw actions as

\[
y=\xi+A_f^\top c,\qquad
d_{\rm raw}=\chi+\Sigma^\top H.
\]

At \(D^2\), the shapes are
\(A_f\in\mathbb R^{2\times3}\) and
\(\Sigma\in\mathbb R^{3\times2}\); at \(Y^3\), both response blocks are
\(3\times3\). Thus every product below has the orientation shown.

Gaussian integration by parts gives

\[
R:=\mathbb E[cy^\top]=\Sigma^\top Q+KA_f.
\]

For the new cotangent \(C_2\), put

\[
k_C=\mathbb E[cC_2],
\qquad
r_C=\mathbb E[yC_2]
=Q\sigma_2+A_f^\top k_C.
\]

Substitution into the exact adaptive column-conditioning formula shows that
the total \(H\)-coefficient is

\[
\Sigma K^{-1}k_C+
Q^{-1}\{r_C-R^\top K^{-1}k_C\}
=\sigma_2.
\]

Thus

\[
D^2
\longrightarrow
\chi_2+\sum_{r=0}^2\sigma_{2r}H_r.
\]

Adding the two exact learned-matrix terms gives the displayed \(b_2\), after
which \(H^3\) is measurable.

The seventh and terminal action is

\[
Y^3=\frac{WH^3}{\sqrt n}.
\]

Both old query blocks now have three columns. Its new empirical data are

\[
Q_{03}^{(n)},Q_{13}^{(n)},Q_{23}^{(n)},Q_{33}^{(n)},
\qquad
\frac{(D^r)^\top H^3}{n}\quad(0\le r\le2).
\]

Let

\[
q_H=\mathbb E[HH_3],
\qquad
\rho_3=\mathbb E[\nabla_\chi H_3].
\]

The two Gaussian integration-by-parts identities needed by the row
conditioning formula are

\[
\mathbb E[d_{\rm raw}H_3]
=K\rho_3+\Sigma^\top q_H,
\qquad
\mathbb E[cy^\top]=\Sigma^\top Q+KA_f.
\]

The direct \(c\)-coefficient is

\[
\rho_3-A_fQ^{-1}q_H,
\]

while projection on the previous \(y\)-block contributes
\(A_fQ^{-1}q_H\). Hence

\[
Y^3
\longrightarrow
\xi_3+\sum_{r=0}^2\rho_{3r}C_r.
\]

The new feature innovation is terminal, so its Schur complement may vanish;
the inequality

\[
|\sqrt x-\sqrt y|\le\sqrt{|x-y|}
\]

still gives normalized-\(L^p\) convergence and no later inverse uses it.
The two newly required positive Schur complements are the \(H^2\) Schur
used when \(Y^2\) becomes nonterminal and the \(C^2\) Schur used at
\(D^2\); the \(H^3\) Schur at \(Y^3\) is terminal.

For completeness, the concentration and uniform-integrability argument has
no new unverified class of variables. The polynomial-Lipschitz transfer
estimate first maps the coupled \(Y^2\)-fields to \(C^2\), then the coupled
\(D^2\)-fields to \(H^3\). Rosenthal's inequality applies to every empirical
average listed above. The good event appends the two positive Schur
complements just displayed; high-moment Markov bounds make its complement
\(O(n^{-M})\) for every prescribed \(M\). Run the explicit raw-energy
recursion for one additional update \(s=2\); it remains a fixed polynomial
in the initial Gaussian energy and therefore removes stopping by Hölder.
Finally,

\[
|f_n^3|
\le
\|a^3\|_{n,2}\|\phi(z^3)\|_{n,2}
\]

has a uniform \(L^{1+\delta}\) bound for every fixed \(\delta>0\). Thus the
terminal empirical convergence passes to annealed expectations:

\[
\lim_{n\to\infty}F_{3,n}(h)=F_3(h)
\]

at every fixed \(0<|h|\le h_{31,\phi}\). The one-step identification at
step size \(3h\) only needs \(d>0\) and is valid because \(|3h|\le1\).
At \(h=0\), both identifications follow directly from the initialized
network. This preserves the required width-first order of limits.

## 2. Exact chronological compiler

Let \(\mathcal P_5(N;C)\) denote the finite Price-envelope constructor proved
in Section 6 of ../temporary_quantitative_width_first_bound/PROOF.md. Its
inputs are:

- an exact syntactic Gaussian integrand for
  \(N(h)=\Gamma_{C(h)}[\psi_h]\);
- previously constructed numerical bounds for all scalar coefficient jets;
- numerical entry-sum bounds
  \(\bar c_j\ge\|C^{(j)}(h)\|_\Sigma\), \(0\le j\le5\).

It returns numbers

\[
\overline{\mathcal J}_j(N)
\ge |N^{(j)}(h)|,
\qquad |h|\le1,\quad 0\le j\le5,
\]

by the explicit envelope-pair and Price recursion. The returned numbers use
only \(M_\phi\), integer arithmetic, and

\[
\mu_{m,p}(v)
=\sum_{\ell=0}^p
\binom p\ell
v^{\ell/2}2^{\ell/2}
\frac{\Gamma((m+\ell)/2)}{\Gamma(m/2)}.
\]

The following six passes completely specify the \(F_3\) compilation.
Their logical use is split to preserve the limit order. First execute only
the internal Gram and response constructors in Passes 1--5; these define and
certify the rank of the proposed Gaussian program without asserting that an
output is a width limit. Use that certificate in the fixed-\(h\)
seven-action proof. Only after this identification apply the output calls in
Passes 2 and 6 and the singular-Price lemma to the now identified
\(F_1,F_3\). Listing the constructors in one chronological table does not
interchange these two logical operations.

### Pass 1: first lower node

Use covariance

\[
C_{\mathcal L_1}=\operatorname{diag}(1,d),
\qquad
d=\mathbb E[\phi'(G)^2].
\]

Initialize its covariance bounds by

\[
\bar c_{\mathcal L_1,0}=1+M_\phi^2,
\qquad
\bar c_{\mathcal L_1,j}=0\quad(1\le j\le5).
\]

Compile \(Q_{00},Q_{01},Q_{11}\), \(\rho_{10}\), and

\[
L_{10}=\rho_{10}+hQ_{01}.
\]

For every compiled covariance or response entry retain all numerical
derivative bounds through order five.

### Pass 2: first top node

Use covariance

\[
C_{\mathcal T_1}=\operatorname{diag}(1,Q^{[1]}),
\]

with the entry-sum majorants

\[
\bar c_{\mathcal T_1,j}
=\mathbf 1_{\{j=0\}}
 +\sum_{r,t=0}^1\overline{\mathcal J}_j(Q_{rt}).
\]

Construct \(z_0,C_0,a_1,z_1,C_1\). Compile

\[
F_1=\mathbb E[a_1\phi(z_1)],
\qquad
K^{[1]}_{rt}=\mathbb E[C_rC_t],
\qquad
\sigma_{1r}=\mathbb E[\partial_{\xi_r}C_1].
\]

### Pass 3: second lower node

Use

\[
C_{\mathcal L_2}=\operatorname{diag}(1,K^{[1]}),
\]

\[
\bar c_{\mathcal L_2,j}
=\mathbf 1_{\{j=0\}}
 +\sum_{r,t=0}^1\overline{\mathcal J}_j(K_{rt}).
\]

Construct

\[
b_1
=\chi_1+(\sigma_{10}+hK_{01})H_0+\sigma_{11}H_1,
\]

\[
u_2=u_1+hb_1\phi'(u_1),
\qquad H_2=\phi(u_2).
\]

Compile \(Q^{[2]}_{r2}\) for \(r=0,1,2\), \(\rho_{2r}\) for
\(r=0,1\), and

\[
L_{2r}=\rho_{2r}+hQ_{r2},
\qquad r=0,1.
\]

### Pass 4: second top node, now nonterminal

Use

\[
C_{\mathcal T_2}=\operatorname{diag}(1,Q^{[2]}),
\]

\[
\bar c_{\mathcal T_2,j}
=\mathbf 1_{\{j=0\}}
 +\sum_{r,t=0}^2\overline{\mathcal J}_j(Q_{rt}).
\]

Recompute the first top stage and construct

\[
z_2=\xi_2+L_{20}C_0+L_{21}C_1,
\]

\[
a_2=A+h\{\phi(z_0)+\phi(z_1)\},
\qquad
C_2=a_2\phi'(z_2).
\]

Compile all entries of

\[
K^{[2]}_{rt}=\mathbb E[C_rC_t],
\qquad 0\le r,t\le2,
\]

and all responses

\[
\sigma_{2r}=\mathbb E[\partial_{\xi_r}C_2],
\qquad r=0,1,2.
\]

The old entries of \(K^{[1]}\) are reused, not independently recomputed.

### Pass 5: third lower node

Use

\[
C_{\mathcal L_3}=\operatorname{diag}(1,K^{[2]}),
\]

\[
\bar c_{\mathcal L_3,j}
=\mathbf 1_{\{j=0\}}
 +\sum_{r,t=0}^2\overline{\mathcal J}_j(K_{rt}).
\]

Recompute \(u_0,u_1,u_2,H_0,H_1,H_2\), then construct

\[
b_2
=\chi_2
 +\sum_{r=0}^2\sigma_{2r}H_r
 +h(K_{02}H_0+K_{12}H_1),
\]

\[
u_3=u_2+hb_2\phi'(u_2),
\qquad
H_3=\phi(u_3).
\]

Compile all new entries \(Q^{[3]}_{r3}\), \(r=0,1,2,3\), and all
responses

\[
\rho_{3r}=\mathbb E[\partial_{\chi_r}H_3],
\qquad r=0,1,2,
\]

and

\[
L_{3r}=\rho_{3r}+hQ_{r3}.
\]

### Pass 6: terminal third top node

Use

\[
C_{\mathcal T_3}=\operatorname{diag}(1,Q^{[3]}),
\]

\[
\bar c_{\mathcal T_3,j}
=\mathbf 1_{\{j=0\}}
 +\sum_{r,t=0}^3\overline{\mathcal J}_j(Q_{rt}).
\]

Recompute \(z_0,z_1,z_2,C_0,C_1,C_2\), then construct

\[
z_3=\xi_3+L_{30}C_0+L_{31}C_1+L_{32}C_2,
\]

\[
a_3=A+h\{\phi(z_0)+\phi(z_1)+\phi(z_2)\}.
\]

Apply \(\mathcal P_5\) to

\[
F_3(h)=\mathbb E[a_3\phi(z_3)]
\]

and define

\[
\overline{\mathcal J}_{3,5}
:=\overline{\mathcal J}_5(F_3).
\]

The coefficient rule used at every pass is explicit:

\[
\bar L_{sr,j}
=\bar\rho_{sr,j}+\bar Q_{rs,j}
 +j\bar Q_{rs,j-1},
\qquad
\bar Q_{rs,-1}=0.
\]

This follows from
\((hQ)^{(j)}=hQ^{(j)}+jQ^{(j-1)}\) and \(|h|\le1\).

## 3. Termination and the \(C^{12}\) budget

The compiler is finite for four separate reasons.

1. There are exactly six Gaussian passes.
2. Each pass contains finitely many covariance, response, and output
   integrands.
3. The Price index set is

   \[
   \left\{(r,j,s):
   r+j+\left\lceil s/2\right\rceil\le5\right\},
   \]

   hence finite.
4. Every formal product or chain derivative creates a finite expression.

On the reachable index set, \(j+s\le10\). An undifferentiated response
integrand begins with activation order at most two. Therefore no generated
factor exceeds \(\phi^{(12)}\). Adding the third step increases the number
of factors and Gaussian coordinates but does not increase the maximum
derivative order on one factor. The largest block is
\((A,\xi_0,\xi_1,\xi_2,\xi_3)\), of dimension five, so the explicit
Gaussian moment constructor only needs \(m\le5\).

It follows from the singular-covariance Price lemma, chronologically through
the six passes, that

\[
F_1,F_3\in C^5([-1,1])
\]

and that their fifth derivatives are bounded by the numerical compiler
outputs. This regularity is proved after the fixed-\(h\) operator has been
identified; it is not imported from a finite-width Taylor expansion.

## 4. Explicit admissible interval

Three steps require positive definiteness of the nonterminal three-time
feature and cotangent Grams

\[
Q^{[2]}=(Q_{rs})_{0\le r,s\le2},
\qquad
K^{[2]}=(K_{rs})_{0\le r,s\le2}.
\]

Here is an activation-only radius constructor requiring no derivative above
order five. For \(G=Q^{[2]}\) or \(K^{[2]}\), define

\[
N^G_{ab}(h)
=\sum_{r=0}^a\sum_{s=0}^b
(-1)^{a-r+b-s}\binom ar\binom bsG_{rs}(h),
\qquad a,b\in\{0,1,2\}.
\]

The exact nodewise derivative compiler verifies

\[
(N^G_{ab})^{(j)}(0)=0,
\qquad j<a+b.
\]

Define the desingularized activation jet Gram

\[
\widehat G_{ab}(0)
=\frac{(N^G_{ab})^{(a+b)}(0)}{(a+b)!}.
\]

Every entry is an explicit Gaussian activation integral. Let

\[
\lambda_G=\lambda_{\min}(\widehat G(0)).
\]

If \(\bar G_{rs,j}\) denotes the entrywise numerical derivative bound
returned by the compiler, set

\[
e^G_{ab}
=\frac{1}{(a+b+1)!}
\sum_{r=0}^a\sum_{s=0}^b
\binom ar\binom bs\bar G_{rs,a+b+1},
\]

\[
E_G=\left(\sum_{a,b=0}^2(e^G_{ab})^2\right)^{1/2}.
\]

Let \(r_{2,\phi}>0\) be the explicit two-time rank radius constructed in
Section 7 of the two-step proof. The activation calculation below proves

\[
\lambda_Q>0,\qquad \lambda_K>0,
\]

for every nonconstant activation in the stated class. Define

\[
r_Q=\min\left\{
r_{2,\phi},1,\frac{\lambda_Q}{2(1+E_Q)}
\right\},
\]

\[
r_K=\min\left\{
r_Q,1,\frac{\lambda_K}{2(1+E_K)}
\right\},
\qquad
h_{31,\phi}=\min\{1/3,r_K\}.
\]

For \(h\ne0\), let

\[
T_h=
\begin{pmatrix}
1&0&0\\
-h^{-1}&h^{-1}&0\\
h^{-2}&-2h^{-2}&h^{-2}
\end{pmatrix}.
\]

Then

\[
\widehat G(h)=T_hG(h)T_h^\top,
\qquad
\widehat G_{ab}(h)=\frac{N^G_{ab}(h)}{h^{a+b}}.
\]

Taylor's integral remainder and the compiled derivative bounds give

\[
\|\widehat G(h)-\widehat G(0)\|_{\mathrm{op}}
\le E_G|h|.
\]

Consequently, for \(0<|h|\le h_{31,\phi}\),

\[
\lambda_{\min}(\widehat G(h))
\ge\lambda_G-E_G|h|
\ge\lambda_G/2>0.
\]

Congruence by the invertible \(T_h\) proves that \(Q^{[2]}(h)\) and
\(K^{[2]}(h)\) are positive definite. Their earlier principal Grams are
then positive definite as well. This is exactly the rank input required by
the seven-action fixed-\(h\) conditioning proof.

If an explicit lower bound on every inverse and nonterminal Schur complement
is desired, put

\[
T_G=\sum_{r=0}^2\bar G_{rr,0}.
\]

Since

\[
\det G(h)=h^6\det\widehat G(h)
\ge |h|^6(\lambda_G/2)^3,
\]

the three-dimensional determinant/trace inequality gives

\[
\lambda_{\min}(G(h))
\ge
\frac{|h|^6(\lambda_G/2)^3}{T_G^2}.
\]

Every principal submatrix has at least this minimum eigenvalue. If \(S\) is
a scalar Schur complement, then
\(S^{-1}=(G^{-1})_{33}\le\lambda_{\min}(G)^{-1}\), hence
\(S\ge\lambda_{\min}(G)\). Thus the same fully activation-defined formula
controls all nonterminal inverses and innovation variances at each fixed
nonzero \(h\).

The factor \(1/3\) has a separate purpose: it ensures both
\(|h|\le1\), for the \(F_3\) compiler, and \(|3h|\le1\), for the
\(F_1(3h)\) compiler. Every estimate depends on \(|h|\), so this interval
also covers negative learning rates.

The required positivity is in fact activation-explicit. Put

\[
\begin{aligned}
e&=\mathbb E[\phi'(G)^4],&
m&=\mathbb E[\phi(G)\phi''(G)\phi'(G)^2],\\
s&=\mathbb E[\phi''(G)^2\phi'(G)^2],&
\ell&=\mathbb E[\phi(G)^2\phi'(G)^2],\\
t&=\mathbb E[\phi''(G)^2],&
c&=1+d,
\end{aligned}
\]

and use the already explicit first-order response quantity

\[
k=2d+\mathbb E[\phi(G)\phi''(G)]
 +c\left\{
\mathbb E[\phi'(G)\phi'''(G)]+t
\right\}.
\]

Define

\[
\tau=\ell+2cm+3c^2s+edt.
\]

For \(d>0\), one has \(e>0\) and \(\tau>0\), as proved by the
sum-of-squares representation in Section 7 of the two-step proof.

Let \(U,B,T\) be independent with

\[
U\sim N(0,1),\qquad B\sim N(0,d),\qquad T\sim N(0,\tau),
\]

and write \(g=\phi(U)\), \(p=\phi'(U)\), \(q=\phi''(U)\). The three
feature forward jets are

\[
P_0=g,\qquad P_1=Bp^2,
\]

\[
P_2=Tp^2+kgp^2+2B^2p^2q.
\]

They satisfy

\[
\langle P_0,P_1\rangle
=\langle P_1,P_2\rangle=0,
\qquad
\|P_1\|_2^2=de,
\]

\[
a_Q:=\langle P_0,P_2\rangle=k\ell+2dm.
\]

Consequently, with

\[
\Lambda_Q=\|P_2-a_QP_0\|_2^2,
\]

the independent \(T\)-component gives

\[
\Lambda_Q\ge\tau e>0,
\qquad
\det\widehat Q(0)=de\Lambda_Q>0.
\]

For the cotangent forward jets, let \(X,Z_1,Z_2,A\) be independent
standard Gaussians and, now evaluating \(g,p,q,r_3\) at \(X\), put

\[
S_1=\sqrt{de}\,Z_1,\qquad
R=a_QX+\sqrt{\Lambda_Q}\,Z_2,
\]

\[
R_1=S_1+cAp,\qquad T_0=Ap,
\]

\[
T_1=gp+AqR_1,\qquad R_2=R+cT_1,
\]

\[
T_2=p^2R_1+AqR_2+2gqR_1+Ar_3R_1^2.
\]

Exact differentiation of the Gaussian operator gives these three fields as
the cotangent forward jets. Direct Gaussian integration gives

\[
\langle T_0,T_1\rangle=0,\qquad
\|T_0\|_2^2=d,\qquad
\|T_1\|_2^2=\tau.
\]

Let

\[
\Lambda_K
=\left\|
T_2-\operatorname{Proj}_{\operatorname{span}(T_0,T_1)}T_2
\right\|_2^2.
\]

If \(t>0\), the centered independent \(Z_2\)-component of \(T_2\) is
\(\sqrt{\Lambda_Q}AqZ_2\), which is orthogonal to
\(\operatorname{span}(T_0,T_1)\). Therefore

\[
\Lambda_K\ge t\Lambda_Q>0.
\]

If \(t=0\), continuity gives \(\phi''\equiv0\), so \(\phi\) is affine.
Then the independent \(Z_1\)-component of \(T_2\) has squared norm \(d^5\),
and again \(\Lambda_K>0\). Hence

\[
\det\widehat K(0)=d\tau\Lambda_K>0.
\]

Thus the previously displayed \(\lambda_Q,\lambda_K\) are strictly
positive for every nonconstant activation in the stated class. The rank
radius is unconditional when \(d>0\); no existential continuity radius is
being hidden.

## 5. Parity

The operator recursion is invariant in law under

\[
h\mapsto-h,\qquad
A\mapsto-A,\qquad
\chi^{[s]}\mapsto-\chi^{[s]}
\]

at every lower stage; the \(\xi\)-blocks are unchanged. Inductively:

- every \(H_s,u_s,z_s\) is unchanged;
- every \(Q^{[s]},K^{[s]}\) is even in \(h\);
- every \(\rho,\sigma,L\) is odd;
- every \(b_s,a_s,C_s\) changes sign.

For the lower induction, each term of \(b_s\) changes sign:
\(\chi_s\) changes sign, \(\sigma_{sr}H_r\) is odd, and
\(hK_{rs}H_r\) is odd. Hence \(hb_s\), and therefore \(u_{s+1}\), is
unchanged. For the top induction, each \(L_{sr}C_r\) is unchanged, so
\(z_s\) is unchanged, whereas both \(A\) and
\(h\sum_{r<s}\phi(z_r)\) change sign. This proves the four assertions.

In particular,

\[
F_s(-h)=-F_s(h)
\]

for every constructed step count. Therefore

\[
\Delta_{31}(h)=F_3(h)-F_1(3h)
\]

is odd and

\[
\Delta_{31}(0)=\Delta_{31}''(0)
=\Delta_{31}^{(4)}(0)=0.
\]

## 6. Activation-only fifth-order bound

In addition to the moments in Section 4, put

\[
j=\mathbb E[\phi'''(G)\phi'(G)^3],
\qquad
b=\mathbb E[\phi(G)\phi''(G)],
\qquad
r=\mathbb E[\phi'(G)\phi'''(G)],
\]

\[
\beta=b+cr,\qquad
\delta=d+ct,\qquad
k=d+\beta+\delta.
\]

The two activation polynomials are

\[
S_\phi
=3c^2m+3c^3j+3de\beta+3dkm+3d^2j,
\]

\[
H_\phi
=c^2e+c\ell+2c^2m+3c^3s+cedt
 +2ed^2+3d^2s+k^2\ell+2dkm.
\]

The complete direct, nodewise operator-jet calculation is in
../temporary_quantitative_width_first_bound/RUNG3_CUBIC_JET.md. It gives

\[
F_3'(0)=3(1+d+d^2),\qquad
F_1'(0)=1+d+d^2,
\]

and

\[
F_3'''(0)=42S_\phi+60H_\phi,
\qquad
F_1'''(0)=S_\phi,
\]

where \(S_\phi,H_\phi\) are the explicit Gaussian activation polynomials
in Section 8 of the two-step proof. Therefore the activation-defined cubic
coefficient is

\[
\kappa_{31,\phi}
=\frac52S_\phi+10H_\phi
=\frac52(S_\phi+4H_\phi).
\]

It is not used in the remainder constant. Define

\[
\boxed{
B_{31,\phi}
=\frac{
\overline{\mathcal J}_{3,5}
+3^5\overline{\mathcal J}_{1,5}}
{120}.
}
\]

This is a finite number returned solely by the activation-envelope compiler.
For \(|t|\le h_{31,\phi}\),

\[
\begin{aligned}
|\Delta_{31}^{(5)}(t)|
&\le |F_3^{(5)}(t)|
 +3^5|F_1^{(5)}(3t)|\\
&\le
\overline{\mathcal J}_{3,5}
 +3^5\overline{\mathcal J}_{1,5}.
\end{aligned}
\]

The displayed first derivatives prove the necessary linear cancellation.
Taylor's formula with integral remainder through order four gives

\[
\Delta_{31}(h)-\kappa_{31,\phi}h^3
=\frac1{24}\int_0^h(h-t)^4\Delta_{31}^{(5)}(t)\,dt.
\]

Hence

\[
\boxed{
\left|
F_3(h)-F_1(3h)-\kappa_{31,\phi}h^3
\right|
\le B_{31,\phi}|h|^5,
\qquad |h|\le h_{31,\phi}.
}
\]

For every \(\varepsilon>0\), this implies

\[
|F_3(h)-F_1(3h)|
\le
(|\kappa_{31,\phi}|+\varepsilon)|h|^3
\]

whenever

\[
|h|
\le
\min\left\{
h_{31,\phi},
\sqrt{\frac{\varepsilon}{1+B_{31,\phi}}}
\right\}.
\]

Indeed,

\[
B_{31,\phi}|h|^2
\le
\frac{B_{31,\phi}}{1+B_{31,\phi}}\varepsilon
\le\varepsilon.
\]

For the constant activation case \(d=0\), continuity and Gaussian full
support give \(\phi\equiv\pm1\). Then \(F_k(h)=kh\), so the discrepancy is
zero. One may take

\[
\kappa_{31,\phi}=B_{31,\phi}=0,
\qquad h_{31,\phi}=1/3.
\]

## 7. Noncircularity audit

The quantities used above have the following provenance.

- \(\overline{\mathcal J}_{1,5}\) and
  \(\overline{\mathcal J}_{3,5}\) are outputs of the finite syntactic
  activation-envelope recursion. They are not defined as
  \(\sup|F_s^{(5)}|\).
- \(E_Q,E_K\) are finite arithmetic combinations of compiler outputs for
  Gram-entry derivatives.
- \(\widehat Q(0),\widehat K(0)\), and their smallest eigenvalues are finite
  Gaussian activation integrals produced by exact nodewise differentiation;
  they do not refer to an unknown trained output or a trajectory modulus.
- \(h_{31,\phi}\) is an explicit formula in those quantities, not a radius
  selected by continuity of \(F_1,F_3\), or \(\Delta_{31}\).
- The fixed-width limit is taken at each fixed nonzero \(h\) before the
  terminal-output singular-Price calculation at \(h=0\). The auxiliary
  internal Gram regularity used to certify query rank does not differentiate
  a finite-width output or assert a limit exchange.

The seven-action adaptive-conditioning identification is performed at fixed
\(h\) before the singular learning-rate calculation. The rank formula
supplies its quantitative domain, while direct operator differentiation
supplies the cubic coefficient and linear cancellation. Neither calculation
uses a finite-width Taylor expansion followed by a limit exchange.
