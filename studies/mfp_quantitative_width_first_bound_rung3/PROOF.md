# Quantitative width-first third-rung theorem

## Theorem

Let both hidden layers have width \(n\).  For a deterministic input
\(x\in\mathbb R^p\), assume \(\|x\|^2/p=1\).  Initialize all coordinates of
\(w_j^0,W^0,a_i^0\) independently as standard Gaussians.  Assume

$$
\phi\in C^{12}(\mathbb R),\qquad
\mathbb E[\phi(G)^2]=1,
$$

and

$$
M_\phi=
\max\left\{
1,
\sup_x\frac{|\phi(x)|}{1+|x|},
\max_{1\le r\le12}\|\phi^{(r)}\|_\infty
\right\}<\infty,
\qquad G\sim N(0,1).
$$

Let \(F_{k,n}(h)\) be the annealed output after \(k\) recomputed simultaneous
gradient-ascent steps of size \(h\), with the exact normalization in Section
1.  On the interval constructed below, take \(n\to\infty\) separately at
each fixed \(h\), and denote the resulting operator output by \(F_k(h)\).
Define

$$
\Delta_{31}(\eta)=F_3(\eta)-F_1(3\eta).
$$

Sections 2--7 below give finite, terminating formulas, involving only
\(M_\phi\) and Gaussian activation integrals, for numbers

$$
\kappa_{31},\qquad B_{31}<\infty,\qquad h_{31}>0.
$$

They satisfy, for every \(|\eta|\le h_{31}\),

$$
\boxed{
|\Delta_{31}(\eta)-\kappa_{31}\eta^3|
\le B_{31}|\eta|^5.
}
$$

In particular, for every \(\varepsilon>0\),

$$
|\eta|
\le
\eta_{31}(\phi,\varepsilon)
:=
\min\left\{
h_{31},
\sqrt{\frac{\varepsilon}{1+B_{31}}}
\right\}
$$

implies

$$
|F_3(\eta)-F_1(3\eta)|
\le (|\kappa_{31}|+\varepsilon)|\eta|^3.
$$

To state the coefficient, write \(\phi_r=\phi^{(r)}(G)\) and set

$$
\begin{aligned}
d&=\mathbb E[\phi_1^2],&
e&=\mathbb E[\phi_1^4],&
m&=\mathbb E[\phi_0\phi_2\phi_1^2],\\
j&=\mathbb E[\phi_3\phi_1^3],&
s&=\mathbb E[\phi_2^2\phi_1^2],&
\ell&=\mathbb E[\phi_0^2\phi_1^2],\\
b&=\mathbb E[\phi_0\phi_2],&
r&=\mathbb E[\phi_1\phi_3],&
t&=\mathbb E[\phi_2^2].
\end{aligned}
$$

Put

$$
c=1+d,\qquad
\beta=b+cr,\qquad
\delta=d+ct,\qquad
k=d+\beta+\delta,
$$

$$
S_\phi
=3c^2m+3c^3j+3de\beta+3dkm+3d^2j,
$$

and

$$
H_\phi
=c^2e+c\ell+2c^2m+3c^3s+cedt
+2ed^2+3d^2s+k^2\ell+2dkm.
$$

Then

$$
\boxed{
\kappa_{31}
=\frac52S_\phi+10H_\phi
=\frac52(S_\phi+4H_\phi).
}
$$

No derivative of a finite-width network is used.  The proof identifies the
actual network at each fixed nonzero step first, proves regularity of that
width-first Gaussian DAG at its singular covariance, and only then
differentiates in \(h\).

## 1. Exact finite-width network

For \(1\le i,j\le n\), let

$$
w_j^0\sim N(0,I_p),\qquad W_{ij}^0\sim N(0,1),\qquad a_i^0\sim N(0,1)
$$

independently.  At time \(s\), define

$$
u_j^s=\frac{(w_j^s)^Tx}{\sqrt p},\qquad
H_j^s=\phi(u_j^s),
$$

$$
z_i^s=\frac1{\sqrt n}\sum_jW_{ij}^sH_j^s,
\qquad
f_n^s=\frac1n\sum_i a_i^s\phi(z_i^s),
$$

$$
C_i^s=a_i^s\phi'(z_i^s),
\qquad
b_j^s=\frac1{\sqrt n}\sum_iW_{ij}^sC_i^s.
$$

One ascent step is

$$
\theta^{s+1}=\theta^s+hn\nabla_\theta f_n^s.
$$

Equivalently, with every right-hand side evaluated at time \(s\),

$$
\begin{aligned}
a_i^{s+1}&=a_i^s+h\phi(z_i^s),\\
W_{ij}^{s+1}&=W_{ij}^s+\frac h{\sqrt n}C_i^sH_j^s,\\
u_j^{s+1}&=u_j^s+h b_j^s\phi'(u_j^s).
\end{aligned}
$$

These updates are used for \(s=0,1,2\), and

$$
F_{k,n}(h)=\mathbb E[f_n^k].
$$

Write \(W=W^0\) and

$$
Q_{rs}^{(n)}=\frac1n(H^r)^TH^s,
\qquad
K_{rs}^{(n)}=\frac1n(C^r)^TC^s.
$$

The learned rank-one pieces can be separated from the reused source matrix
exactly:

$$
z^s=\frac{WH^s}{\sqrt n}
+h\sum_{r<s}Q_{rs}^{(n)}C^r,
$$

$$
b^s=\frac{W^TC^s}{\sqrt n}
+h\sum_{r<s}K_{rs}^{(n)}H^r.
$$

The second sums contain only updates made before time \(s\); in particular,
no current-time term is present.

## 2. The three-step Gaussian operator DAG

For a positive-semidefinite matrix \(V\), including a singular one, write

$$
\Gamma_V[\Psi]=\mathbb E[\Psi(X)],\qquad X\sim N(0,V).
$$

Every lower Gaussian expectation below uses a fresh block
\((U,\chi_0,\ldots)\) in which \(U\) is independent of the \(\chi\)-block.
Every top expectation uses a fresh block \((A,\xi_0,\ldots)\) in which
\(A\) is independent of the \(\xi\)-block.  The lower and top expectation
spaces may be chosen mutually independent; they communicate only through
the deterministic Gram and response coefficients already computed.  Thus
the recursion specifies the full joint law at each node.

The following recursion contains no inverse Gram and therefore defines
\(F_3(h)\) for every \(|h|\le1\), including \(h=0\).

Start with \(u_0=U\sim N(0,1)\) and \(A\sim N(0,1)\), independent.  For
\(s\ge0\), put \(H_s=\phi(u_s)\).  Once \(C_0,\ldots,C_s\) have been
defined, let \((\chi_0,\ldots,\chi_s)\) be centered Gaussian, independent of
\(U\), with covariance

$$
K_{rt}=\mathbb E[C_rC_t].
$$

Define

$$
\sigma_{sr}=\mathbb E[\partial_{\xi_r}C_s],
$$

At \(s=0\), centering of \(A\) gives
\(\sigma_{00}=0\) and \(K_{00}=d\), so the first lower update is available
before the remaining top block is compiled.

$$
b_s
=\chi_s+\sum_{r=0}^s\sigma_{sr}H_r
+h\sum_{r<s}K_{rs}H_r,
$$

and

$$
u_{s+1}=u_s+h b_s\phi'(u_s).
$$

Once \(H_0,\ldots,H_s\) have been defined, let
\((\xi_0,\ldots,\xi_s)\) be centered Gaussian, independent of \(A\), with
covariance

$$
Q_{rt}=\mathbb E[H_rH_t].
$$

Put

$$
\rho_{sr}=\mathbb E[\partial_{\chi_r}H_s],
\qquad
L_{sr}=\rho_{sr}+hQ_{rs}\quad(r<s),
$$

$$
z_s=\xi_s+\sum_{r<s}L_{sr}C_r,
$$

$$
a_s=A+h\sum_{r<s}\phi(z_r),
\qquad
C_s=a_s\phi'(z_s).
$$

The chronological evaluation is

$$
H_0;\ C_0;\ H_1;\ C_1;\ H_2;\ C_2;\ H_3;\ z_3,a_3,
$$

where at each semicolon the newly available Gram and response coefficients
are computed before they are used.  Explicitly, the two new stages beyond
the two-step program are

$$
\begin{aligned}
b_2&=\chi_2+\sigma_{20}H_0+\sigma_{21}H_1+\sigma_{22}H_2
      +h(K_{02}H_0+K_{12}H_1),\\
u_3&=u_2+h b_2\phi'(u_2),\qquad H_3=\phi(u_3),\\
z_3&=\xi_3+\sum_{r=0}^2(\rho_{3r}+hQ_{r3})C_r,\\
a_3&=A+h\sum_{r=0}^2\phi(z_r).
\end{aligned}
$$

Finally,

$$
F_3(h)=\mathbb E[a_3\phi(z_3)].
$$

The one-step quantity \(F_1(h)\) is the same recursion stopped at
\(a_1,z_1\).

## 3. Fixed-step identification of the actual network

The only randomness reused across the alternating matrix actions is the
initial \(W\).  We first record the exact conditioning identity that controls
it.

### 3.1 Adaptive row/column Gaussian conditioning

We use [Lemma 4.1 of the preceding proof](../mfp_quantitative_width_first_bound/PROOF.md),
whose full adaptive-filtration proof is part of this study.  It proves the
following result for an arbitrary finite predictable sequence, not merely
for five actions.  We restate its formulas here so that the present
instantiation is unambiguous.

Let \(H\in\mathbb R^{n\times p_0}\) and
\(C\in\mathbb R^{n\times q_0}\) collect all row and column queries already
revealed, and put

$$
Y=WH/\sqrt n,\qquad D=W^TC/\sqrt n,
$$

$$
Q=H^TH/n,\qquad K=C^TC/n,\qquad R=C^TY/n=D^TH/n.
$$

Every new query is measurable before its corresponding action is exposed.
Conditionally on the current filtration,

$$
W=P_CW+WP_H-P_CWP_H+P_C^\perp\widetilde W P_H^\perp,
$$

where \(\widetilde W\) is a fresh standard Gaussian matrix.  Consequently,
for a new column query \(c\),

$$
\frac{W^Tc}{\sqrt n}
=DK^{-1}k+HQ^{-1}(r-R^TK^{-1}k)
+\tau_cP_H^\perp g,
$$

$$
k=C^Tc/n,\qquad r=Y^Tc/n,\qquad
\tau_c^2=c^Tc/n-k^TK^{-1}k.
$$

For a new row query \(v\),

$$
\frac{Wv}{\sqrt n}
=YQ^{-1}q+CK^{-1}(s-RQ^{-1}q)
+\tau_vP_C^\perp g,
$$

$$
q=H^Tv/n,\qquad s=D^Tv/n,\qquad
\tau_v^2=v^Tv/n-q^TQ^{-1}q.
$$

This is an adaptive statement: after any finite history, the unrevealed
part of \(W\) is the double-orthogonal Gaussian block.  To prove it, decompose
the next predictable query into its old-span and orthogonal parts.  Revealing
the action fixes exactly one Gaussian projection of that block; Gaussian
orthogonality leaves a fresh block on the two new orthogonal complements.
Induction from the empty history yields the displayed conditional law.
Orthogonally projecting the new action onto the old \(H\)- and \(C\)-spans
then gives the two formulas.  This proof also covers a singular empirical
span with Moore--Penrose inverses; below we stop before a population-singular
nonterminal span is encountered.

### 3.2 Seven predictable actions and their empirical data

Put

$$
Y^s=WH^s/\sqrt n,\qquad D^s=W^TC^s/\sqrt n.
$$

Expose \(W\) in the order

$$
Y^0,D^0,Y^1,D^1,Y^2,D^2,Y^3.
$$

After \(Y^s\), the query \(C^s\) is known; after \(D^s\), the query
\(H^{s+1}\) is known.  Thus every query is predictable.  The complete ledger
is:

| action | new query | new empirical data, in addition to earlier Grams |
|---|---|---|
| \(Y^0\) | \(H^0\) | \(Q_{00}^{(n)}\) |
| \(D^0\) | \(C^0\) | \(K_{00}^{(n)},(Y^0)^TC^0/n\) |
| \(Y^1\) | \(H^1\) | \(Q_{01}^{(n)},Q_{11}^{(n)},(D^0)^TH^1/n\) and the old \(C^TY/n\) block |
| \(D^1\) | \(C^1\) | \(K_{01}^{(n)},K_{11}^{(n)},(Y^r)^TC^1/n,\ r\le1\) |
| \(Y^2\) | \(H^2\) | \(Q_{02}^{(n)},Q_{12}^{(n)},Q_{22}^{(n)},(D^r)^TH^2/n,\ r\le1\) |
| \(D^2\) | \(C^2\) | \(K_{02}^{(n)},K_{12}^{(n)},K_{22}^{(n)},(Y^r)^TC^2/n,\ r\le2\) |
| \(Y^3\) | \(H^3\) | \(Q_{03}^{(n)},Q_{13}^{(n)},Q_{23}^{(n)},Q_{33}^{(n)},(D^r)^TH^3/n,\ r\le2\) |

At each line, the previously accumulated \(C^TY/n=D^TH/n\) block is also
used by the conditioning formula; all of its entries appeared on an earlier
line.  Thus the table lists every new scalar empirical input and does not
hide a response coefficient.

The nonterminal population ranks required by these seven formulas are the
principal submatrices of

$$
Q^{[2]}=(Q_{rs})_{0\le r,s\le2},
\qquad
K^{[2]}=(K_{rs})_{0\le r,s\le2}.
$$

The new feature innovation at \(Y^3\) is terminal, so \(Q^{[3]}\) need not
be invertible.

### 3.3 The two new response cancellations

The first five actions, including the critical dependence of \(H^1_j\) on
the reused column through \(\chi_{0j}\), are the proved five-query lemma in
[the preceding two-step proof](../mfp_quantitative_width_first_bound/PROOF.md).
That lemma proves the same stopped \(L^p\) coupling, all empirical overlaps,
and the \(D^1,Y^2\) response cancellations.  We now calculate the two
additional reused-matrix actions explicitly.

For \(D^2\), let

$$
h_*=(H_0,H_1,H_2)^T,\qquad c_*=(C_0,C_1)^T,
$$

$$
y=(Y^0,Y^1,Y^2)^T=\xi+Pc_*,
\qquad
d_*=(D^0,D^1)^T=\chi+Sh_*,
$$

with

$$
P=
\begin{pmatrix}
0&0\\
\rho_{10}&0\\
\rho_{20}&\rho_{21}
\end{pmatrix},
\qquad
S=
\begin{pmatrix}
0&0&0\\
\sigma_{10}&\sigma_{11}&0
\end{pmatrix}.
$$

Let \(Q=Q^{[2]}\), \(K=(K_{rs})_{r,s\le1}\),

$$
k_c=\mathbb E[c_*C_2],
\qquad
\sigma_2=(\sigma_{20},\sigma_{21},\sigma_{22})^T.
$$

Gaussian integration by parts, justified by the bounded derivative envelope,
gives

$$
R:=\mathbb E[c_*y^T]=SQ+KP^T,
\qquad
r:=\mathbb E[yC_2]=Q\sigma_2+Pk_c.
$$

The \(h_*\)-coefficient in the second term of the column-conditioning
formula is

$$
Q^{-1}(r-R^TK^{-1}k_c)
=\sigma_2-S^TK^{-1}k_c.
$$

The first conditioning term \(d_*^TK^{-1}k_c\) contributes
\(h_*^TS^TK^{-1}k_c\), so the unwanted term cancels exactly.  The remaining
Gaussian regression and its fresh orthogonal innovation form \(\chi_2\) with
the extended covariance \(K^{[2]}\).  Therefore

$$
D^2\ \Longrightarrow\
\chi_2+\sigma_{20}H_0+\sigma_{21}H_1+\sigma_{22}H_2.
$$

Adding the exact learned-\(W\) terms produces the \(b_2\) in Section 2.

For \(Y^3\), enlarge \(c_*\) to \((C_0,C_1,C_2)^T\), and use the square
matrices

$$
P=
\begin{pmatrix}
0&0&0\\
\rho_{10}&0&0\\
\rho_{20}&\rho_{21}&0
\end{pmatrix},
\qquad
S=
\begin{pmatrix}
0&0&0\\
\sigma_{10}&\sigma_{11}&0\\
\sigma_{20}&\sigma_{21}&\sigma_{22}
\end{pmatrix}.
$$

Now \(y=\xi+Pc_*\), \(d_*=\chi+Sh_*\), and

$$
R=SQ+KP^T.
$$

For

$$
q=\mathbb E[h_*H_3],
\qquad
\rho_3=(\rho_{30},\rho_{31},\rho_{32})^T,
$$

Gaussian integration by parts gives

$$
v:=\mathbb E[d_*H_3]=K\rho_3+Sq.
$$

The direct \(c_*\)-coefficient in row conditioning is

$$
K^{-1}(v-RQ^{-1}q)=\rho_3-P^TQ^{-1}q.
$$

The row-projection term \(y^TQ^{-1}q\) contributes the opposite
\(c_*^TP^TQ^{-1}q\).  Hence

$$
Y^3\ \Longrightarrow\
\xi_3+\rho_{30}C_0+\rho_{31}C_1+\rho_{32}C_2,
$$

and the exact learned terms turn this into \(z_3\).  These calculations also
show explicitly how the dependence of every \(H_j^s\), including the
dependence of \(H_j^1\) on the reused column through \(\chi_{0j}\), is retained
inside the joint \(\chi\)-block and its responses.

### 3.4 Concentration, regression coefficients, and uniform integrability

The complete seven-stage induction, including separate \(D^2\) and \(Y^3\)
error estimates, is proved in
[the seven-action identification lemma](WIDTH_IDENTIFICATION.md).  The
argument and all its quantitative invariants are reproduced below in
condensed form; the cited lemma is the non-abbreviated proof, not an appeal
to a standard state-evolution theorem.

For a vector \(x\in\mathbb R^n\), write

$$
\|x\|_{n,p}
=\left(\frac1n\sum_{i=1}^n|x_i|^p\right)^{1/p}.
$$

Fix \(h\ne0\) for which \(Q^{[2]}(h)\) and \(K^{[2]}(h)\) are positive
definite.  Let \(\gamma(h)>0\) be smaller than all eigenvalues and
nonterminal Schur complements used in the seven actions.  Couple each
orthogonal residual in Section 3.1 to one fresh iid Gaussian vector and use
the same vector in the population Gram--Schmidt program.  Use column marks

$$
(U,g_0,g_1,g_2)
$$

and row marks

$$
(A,e_0,e_1,e_2,e_3).
$$

The vectors \(\chi_2\) and \(\xi_3\) are obtained by ordinary Gaussian
regression on their earlier blocks plus \(g_2\) and \(e_3\), respectively.
The \(\xi_3\) innovation is allowed to have zero population variance because
it is terminal.

Here is the finite convergence argument.  Set \(\mathcal G_{-1}=\Omega\).
Before action \(r\), define \(\mathcal G_r\subseteq\mathcal G_{r-1}\) by
requiring every empirical Gram inverted at that action and every nonterminal
empirical Schur complement to be at least \(\gamma(h)/2\).  Stop the coupled
representation, but not the actual network, at the first failure.  On
\(\mathcal G_r\),

$$
\|A^{-1}-B^{-1}\|
\le\|A^{-1}\|\,\|A-B\|\,\|B^{-1}\|,
$$

and the square root is Lipschitz above \(\gamma(h)/2\).  Therefore every
conditional-mean coefficient and every nonterminal innovation scale is a
Lipschitz function of the finite empirical list in Section 3.2.

For an old query block \(V\in\mathbb R^{n\times r}\), conditional on \(V\),

$$
P_Vg=V(V^TV/n)^{-1}V^Tg/n,
$$

so, on the same good event and for all fixed finite \(p,s\),

$$
\left\|\|P_Vg\|_{n,p}\right\|_{L^s(g\mid V)}
\le C_{p,s,r,\gamma(h)}n^{-1/2}
\sum_{a=1}^r\|V_a\|_{n,p}.
$$

Thus replacing \(P_V^\perp g\) by \(g\) costs \(O(n^{-1/2})\) in normalized
\(L^p\).  Every ideal empirical average in the ledger is an average of iid
polynomial-growth coordinate functions.  Rosenthal's inequality gives

$$
\left\|
\frac1n\sum_{i=1}^n\Psi(X_i)-\mathbb E\Psi(X)
\right\|_{L^p}
\le C_{p,\Psi}n^{-1/2}.
$$

Bounded derivatives and linear growth make each network coordinate update
polynomial-Lipschitz.  Hence, if the already constructed fields converge in
normalized \(L^{2p}\), the mean-value theorem and Hölder's inequality transfer
the convergence through the next scalar update.  Applying these three
estimates successively to the seven rows of the ledger proves normalized
\(L^p\) convergence of every value field and \(L^p\) convergence of every
Gram and cross-moment there.  At the terminal zero innovation use

$$
|\sqrt x-\sqrt y|\le\sqrt{|x-y|};
$$

convergence still holds and that innovation is never inverted later.

This finite recursion also proves concentration of its own stopping events.
At any prescribed moment order, Markov and Weyl give a failure probability
\(O(n^{-M})\), for arbitrary fixed \(M\), at each of the seven stages.  The
union contains only seven events.

If \(\Theta_{r,n}\) denotes the finite vector of empirical regression
coefficients and innovation scales at action \(r\), and \(\Theta_r\) is the
corresponding population vector, use

$$
\widetilde\Theta_{r,n}
=\Theta_{r,n}\mathbf1_{\mathcal G_r}
+\Theta_r\mathbf1_{\mathcal G_r^c}.
$$

The preceding Lipschitz estimates give
\(\widetilde\Theta_{r,n}\to\Theta_r\) in every finite \(L^p\); hence every
coefficient actually used by the stopped identification is uniformly
integrable.  The untruncated rational inverse-Gram expression on
\(\mathcal G_r^c\) is neither needed nor an actual network parameter.

For completeness, stopping can be removed without any moment of an inverse
Gram.  Define

$$
R_n=1+\|W\|_{\rm op}/\sqrt n+\|A\|_2/\sqrt n+\|U\|_2/\sqrt n.
$$

It has moments of every order uniformly in \(n\).  Starting with
\(\mathsf u_0=\|U\|_{n,2}\), \(\mathsf a_0=\|A\|_{n,2}\), and
\(\mathsf w_0=\|W\|_{\rm op}/\sqrt n\), recursively for \(s=0,1,2\) set

$$
\begin{aligned}
\mathsf h_s&=M_\phi(1+\mathsf u_s),&
\mathsf z_s&=\mathsf w_s\mathsf h_s,&
\mathsf c_s&=M_\phi\mathsf a_s,\\
\mathsf b_s&=\mathsf w_s\mathsf c_s,&
\mathsf a_{s+1}&=\mathsf a_s+M_\phi(1+\mathsf z_s),&
\mathsf u_{s+1}&=\mathsf u_s+M_\phi\mathsf b_s,\\
\mathsf w_{s+1}&=\mathsf w_s+\mathsf c_s\mathsf h_s.
\end{aligned}
$$

After the \(s=2\) update, set

$$
\mathsf h_3=M_\phi(1+\mathsf u_3),
\qquad
\mathsf z_3=\mathsf w_3\mathsf h_3.
$$

The exact update and Cauchy--Schwarz show that these majorize all Euclidean
field norms through time three.  Each is a fixed polynomial in \(R_n\).
Choosing \(M\) larger than the finitely many polynomial degrees and applying
Hölder makes the contribution of the stopped complement tend to zero.
Therefore every actual empirical Gram, raw cross-moment, and terminal output
is uniformly integrable; the stopped regression coefficients were handled
separately above.  In particular,

$$
\lim_{n\to\infty}\mathbb E[f_n^3]=F_3(h).
$$

The same argument stopped after \(Y^1\) gives
\(\lim_nF_{1,n}(h)=F_1(h)\).  At \(h=0\), all updates are identities and both
expected outputs are zero.  No small-\(h\) limit has been used anywhere in
this section.

## 4. Explicit punctured rank interval

Assume first that \(d>0\).  Then \(e>0\).  Define the activation number

$$
\tau=\ell+2cm+3c^2s+edt.
$$

It is strictly positive.  Indeed, for independent standard Gaussians
\(A,Z,G\), the variable

$$
V=\phi(G)\phi'(G)+\sqrt{de}\,AZ\phi''(G)
  +cA^2\phi'(G)\phi''(G)
$$

satisfies \(\mathbb E[V^2]=\tau\).  If \(t>0\), the term containing \(Z\)
has positive squared norm \(edt\).  If \(t=0\), continuity gives
\(\phi''\equiv0\); then \(\phi\) is affine and \(\tau=\ell=d>0\).

### 4.1 Feature forward jets

Let \(U\sim N(0,1)\), \(X\sim N(0,d)\), and \(T\sim N(0,\tau)\) be
independent.  At \(U\), write

$$
g=\phi(U),\qquad p=\phi'(U),\qquad q=\phi''(U),
$$

and define

$$
P_0=g,\qquad P_1=Xp^2,
$$

$$
P_2=Tp^2+kgp^2+2X^2p^2q.
$$

These are the first three Newton jets of the lower operator:

$$
H_0\longrightarrow P_0,\qquad
\frac{H_1-H_0}{h}\longrightarrow P_1,\qquad
\frac{H_2-2H_1+H_0}{h^2}\longrightarrow P_2
$$

in every finite \(L^p\).  Here is the direct calculation.  The two-time
cotangent Gram has

$$
K_{01}=d+O(h^2),\qquad
K_{11}-K_{01}^2/d=\tau h^2+O(h^4).
$$

Choose the signed Gaussian realization

$$
\chi_0=X,\qquad
\chi_1=\frac{K_{01}}dX+
h\sqrt{\frac{K_{11}-K_{01}^2/d}{\tau h^2}}\,T,
$$

using the signed factor \(h\sqrt{\cdot}\) for both signs of \(h\).  Thus
\(\chi_1=X+hT+o_{L^p}(h)\).  Direct differentiation of the top response
integrals gives

$$
\sigma_{10}=\delta h+O(h^3),\qquad
\sigma_{11}=\beta h+O(h^3),\qquad K_{01}=d+O(h^2).
$$

Consequently

$$
b_1=X+h(T+kg)+o_{L^p}(h).
$$

Substitution in \(u_1=U+hXp\) and
\(u_2=u_1+h b_1\phi'(u_1)\), followed by Taylor's formula with integral
remainder, gives exactly the three displayed \(P\)-limits.

Independence and centered Gaussian moments yield

$$
\mathbb E[P_0P_1]=\mathbb E[P_1P_2]=0,
\qquad
\mathbb E[P_1^2]=de.
$$

Put

$$
a_Q=\mathbb E[P_0P_2]=k\ell+2dm,
$$

$$
\lambda_Q=\mathbb E[P_2^2]-a_Q^2.
$$

The \(Tp^2\) component is orthogonal to \(P_0,P_1\) and to the other
components of \(P_2\), so

$$
\lambda_Q\ge\tau e>0.
$$

Therefore

$$
G_Q:=\operatorname{Gram}(P_0,P_1,P_2)
=
\begin{pmatrix}
1&0&a_Q\\
0&de&0\\
a_Q&0&\mathbb E[P_2^2]
\end{pmatrix}
$$

is positive definite and

$$
\det G_Q=de\lambda_Q.
$$

### 4.2 Cotangent forward jets

Let \(Z_0,Z_1,Z_2,A\) be independent standard Gaussians, and set

$$
X_0=Z_0,\qquad
S_1=\sqrt{de}\,Z_1,\qquad
R=a_QZ_0+\sqrt{\lambda_Q}\,Z_2.
$$

At \(X_0\), write

$$
g=\phi(X_0),\quad p=\phi'(X_0),\quad
q=\phi''(X_0),\quad r_3=\phi'''(X_0).
$$

Define

$$
R_1=S_1+cAp,\qquad T_0=Ap,
$$

$$
T_1=gp+AqR_1,\qquad R_2=R+cT_1,
$$

$$
T_2=p^2R_1+AqR_2+2gqR_1+Ar_3R_1^2.
$$

The Gaussian source block with covariance \(Q^{[2]}\) can be realized in
the Newton basis so that

$$
\xi_0\to X_0,\qquad
\frac{\xi_1-\xi_0}{h}\to S_1,\qquad
\frac{\xi_2-2\xi_1+\xi_0}{h^2}\to R.
$$

Since every \(L_{sr}=ch+O(h^3)\),

$$
\frac{z_1-z_0}{h}\to R_1,\qquad
\frac{z_2-2z_1+z_0}{h^2}\to R_2.
$$

For \(C(a,z)=a\phi'(z)\), the first Newton increment is
\(DC[(g,R_1)]=T_1\).  Its second Newton increment is

$$
DC[(pR_1,R_2)]+D^2C[(g,R_1),(g,R_1)]=T_2.
$$

Thus

$$
C_0\to T_0,\qquad
\frac{C_1-C_0}{h}\to T_1,\qquad
\frac{C_2-2C_1+C_0}{h^2}\to T_2
$$

in every finite \(L^p\).

Direct expansion gives

$$
\mathbb E[T_0T_1]=0,\qquad
\mathbb E[T_0^2]=d,\qquad
\mathbb E[T_1^2]=\tau.
$$

Define the Gaussian activation integral

$$
\lambda_K
=\mathbb E[T_2^2]
-\frac{\mathbb E[T_0T_2]^2}{d}
-\frac{\mathbb E[T_1T_2]^2}{\tau}.
$$

If \(t>0\), the component \(Aq\sqrt{\lambda_Q}Z_2\) is orthogonal to
\(T_0,T_1\) and every other component of \(T_2\), hence

$$
\lambda_K\ge t\lambda_Q>0.
$$

If \(t=0\), write \(\phi(x)=\alpha x+\beta_0\).  Then the residual component
\(\alpha^2\sqrt{de}\,Z_1\) has squared norm
\(\alpha^4de=\alpha^{10}=d^5>0\).  Hence, in every nonconstant case,

$$
G_K:=\operatorname{Gram}(T_0,T_1,T_2)\succ0,
\qquad
\det G_K=d\tau\lambda_K.
$$

### 4.3 A radius using only activation-envelope data

For a three-time Gram \(G(h)=(G_{rs}(h))_{0\le r,s\le2}\), define

$$
N_{ab}(h)
=\sum_{r=0}^a\sum_{s=0}^b
(-1)^{a-r+b-s}\binom ar\binom bsG_{rs}(h),
$$

and, for \(h\ne0\),

$$
\widehat G_{ab}(h)=\frac{N_{ab}(h)}{h^{a+b}},
\qquad 0\le a,b\le2.
$$

This is the Gram after the invertible zeroth/first/second forward-difference
change of basis.  Sections 4.1--4.2 prove

$$
\widehat Q(0):=\lim_{h\to0}\widehat Q(h)=G_Q,
\qquad
\widehat K(0):=\lim_{h\to0}\widehat K(h)=G_K.
$$

Let the compiler of Section 5 return numbers

$$
\bar G_{rs,j}\ge
\sup_{|h|\le1}|G_{rs}^{(j)}(h)|,\qquad 0\le j\le5.
$$

Define

$$
E_{ab}(G)
=\frac1{(a+b+1)!}
\sum_{r=0}^a\sum_{s=0}^b
\binom ar\binom bs\bar G_{rs,a+b+1},
$$

$$
E_G=\sum_{a,b=0}^2E_{ab}(G),
$$

and the explicit lower eigenvalue

$$
\underline\gamma_G
=\frac{\det\widehat G(0)}
       {\operatorname{tr}(\widehat G(0))^2}.
$$

The numerator \(N_{ab}\) vanishes through order \(a+b-1\).  Taylor's
integral formula therefore gives

$$
\|\widehat G(h)-\widehat G(0)\|_{\rm op}
\le E_G|h|.
$$

Only original Gram derivatives through
\(a+b+1\le5\) occur.  Weyl's inequality and
\(\lambda_{\min}(\widehat G(0))\ge\underline\gamma_G\) show that

$$
r_G
=\min\left\{
1,\frac{\underline\gamma_G}{2(1+E_G)}
\right\}
$$

ensures \(\widehat G(h)\succ0\), and hence \(G(h)\succ0\), for every
\(0<|h|\le r_G\).

Apply this construction to \(Q^{[2]}\) and \(K^{[2]}\), using \(G_Q,G_K\)
at zero, and call the resulting radii \(r_Q,r_K\).  They are positive and
are computed solely from the displayed Gaussian activation integrals and
the finite envelope compiler.  Set

$$
h_{31}=\min\left\{\frac13,r_Q,r_K\right\}.
$$

For an explicit fixed-\(h\) conditioning lower bound, put

$$
T_G=\sum_{r=0}^2\bar G_{rr,0}.
$$

On the certified punctured interval,

$$
\det G(h)=h^6\det\widehat G(h)
\ge |h|^6\left(\frac{\underline\gamma_G}{2}\right)^3,
$$

and hence

$$
\lambda_{\min}(G(h))
\ge
\frac{|h|^6(\underline\gamma_G/2)^3}{T_G^2}.
$$

Every earlier principal Gram has at least this minimum eigenvalue.  If
\(\mathfrak s\) is a scalar new-query Schur complement, then
\(\mathfrak s^{-1}\) is a diagonal entry of \(G^{-1}\), so
\(\mathfrak s\ge\lambda_{\min}(G)\).  Taking the minimum of these explicit
\(Q,K\) bounds with \(1\) and \(d\) supplies the \(\gamma(h)\) used in
Section 3.

For every fixed \(0<|h|\le h_{31}\), all population Grams and Schur
complements needed in Section 3 are positive.  Thus Section 3 proves the
pointwise width-first identification on the entire punctured interval.  The
factor \(1/3\) keeps the comparison argument \(3\eta\) inside the compiler
interval \([-1,1]\).

## 5. Singular-covariance regularity and the finite envelope compiler

This section defines the derivative majorants used in Section 4 and the
remainder constant used below.  None is defined through a supremum of an
output.

### 5.1 Price differentiation at a singular covariance

We invoke [the singular-covariance Price lemma proved in Section 5 of the
preceding proof](../mfp_quantitative_width_first_bound/PROOF.md).
That proof uses compact cutoffs, the Gaussian Fourier identity, uniform
polynomial domination, and the fundamental theorem of calculus to pass from
\(C+\epsilon I\) to \(C\), including the derivatives.  Thus it does not
infer derivative convergence from pointwise convergence.  Its statement in
the notation needed here is as follows.

Let \(C(h)\) be a \(C^5\) positive-semidefinite covariance curve and

$$
N(h)=\Gamma_{C(h)}[\psi_h].
$$

If all mixed derivatives requested below have a common polynomial envelope,
then

$$
N'(h)=
\Gamma_{C(h)}
\left[
\partial_h\psi_h+\frac12C'(h):D_x^2\psi_h
\right],
$$

even when \(C(h)\) is singular.  To prove this, replace \(C\) by
\(C+\epsilon I\).  Differentiation of the nonsingular Gaussian density and
two integrations by parts give the formula.  The polynomial envelope and a
uniform Gaussian moment bound permit dominated convergence as
\(\epsilon\downarrow0\).  Repeating the argument with the newly produced
integrand proves the formula through order five.  This is performed
chronologically: every covariance entry is regular before a later node uses
it.

### 5.2 Exact envelope arithmetic

An envelope pair \((A,p)\) represents

$$
|g(x)|\le A(1+\|x\|)^p.
$$

Define

$$
(A,p)\oplus(B,q)=(A+B,\max\{p,q\}),
$$

$$
(A,p)\odot(B,q)=(AB,p+q).
$$

For a scalar \(\lambda\), define

$$
\lambda\odot(A,p)=(|\lambda|A,p).
$$

On \(|h|\le1\), initialize

$$
\mathcal E(1)=\mathcal E(h)=(1,0),\qquad
\mathcal E(x_i)=(1,1).
$$

Use \(\oplus,\odot\) on the exact syntactic sum/product tree.  If
\(\mathcal E(g)=(A,p)\), set

$$
\mathcal E(\phi(g))=(M_\phi(1+A),p),
$$

$$
\mathcal E(\phi^{(r)}(g))=(M_\phi,0),
\qquad 1\le r\le12.
$$

Generate every mixed derivative by the finite rules

$$
\partial(uv)=(\partial u)v+u(\partial v),
\qquad
\partial(\phi^{(r)}(u))=\phi^{(r+1)}(u)\partial u,
$$

$$
\partial_hh=1,\qquad
\partial_{x_i}x_j=\mathbf1_{\{i=j\}}.
$$

An earlier scalar coefficient \(S(h)\) is represented by tokens \(S^{[j]}\)
with

$$
\mathcal E(S^{[j]})=(\bar S_j,0),\qquad
\partial_hS^{[j]}=S^{[j+1]}.
$$

Write

$$
E_{j,\alpha}(\psi)
=\mathcal E(\partial_h^j\partial_x^\alpha\psi).
$$

### 5.3 Finite Price recursion

For integers \(m\ge1\), \(p\in\mathbb N_0\), and \(v\ge0\), define the
explicit moment

$$
\mu_{m,p}(v)
=\mathbb E(1+\sqrt v\|G_m\|)^p
=\sum_{r=0}^p\binom pr
v^{r/2}2^{r/2}
\frac{\Gamma((m+r)/2)}{\Gamma(m/2)}.
$$

Here \(G_m\sim N(0,I_m)\).  For a matrix \(A\), write
\(\|A\|_\Sigma=\sum_{i,j}|A_{ij}|\).

Suppose numerical covariance bounds

$$
\bar c_j\ge
\sup_{|h|\le1}\|C^{(j)}(h)\|_\Sigma,
\qquad 0\le j\le5,
$$

have already been constructed from earlier nodes.  For
\(j+\lceil s/2\rceil\le5\), initialize

$$
R^{(0)}_{j,s}
=\bigoplus_{|\alpha|=s}E_{j,\alpha}(\psi).
$$

For
\(r+j+\lceil s/2\rceil<5\), recurse by

$$
\begin{aligned}
R^{(r+1)}_{j,s}
={}&R^{(r)}_{j+1,s}\\
&\oplus
\bigoplus_{\ell=0}^j
\left[
\frac12\binom j\ell\bar c_{\ell+1}
\odot R^{(r)}_{j-\ell,s+2}
\right].
\end{aligned}
$$

If \(R^{(r)}_{0,0}=(A_r,p_r)\), define

$$
\overline{\mathcal J}_r(N)
=A_r\mu_{m,p_r}(\bar c_0).
$$

This is a proved majorant.  Indeed, set

$$
\Psi_0=\psi,\qquad
\Psi_{r+1}=\partial_h\Psi_r+\frac12C':D_x^2\Psi_r.
$$

Induction on the displayed finite index set shows that
\(R^{(r)}_{j,s}\) envelopes every
\(\partial_h^j\partial_x^\alpha\Psi_r\), \(|\alpha|=s\).  The entry-sum
norm absorbs the complete covariance contraction.  Section 5.1 gives

$$
N^{(r)}(h)=\Gamma_{C(h)}[\Psi_r],
$$

and the Gaussian moment formula therefore proves

$$
|N^{(r)}(h)|\le\overline{\mathcal J}_r(N),
\qquad |h|\le1.
$$

If new covariance entries are nodes \(C_{ab}=N_{ab}\), set

$$
\bar c_j^{\rm new}
=\sum_{a,b}\overline{\mathcal J}_j(N_{ab}).
$$

For a response node \(S\), set
\(\bar S_j=\overline{\mathcal J}_j(S)\).  Finally, for
\(L=S+hQ\), use the explicit rule

$$
\bar L_j=\bar S_j+\bar Q_j+j\bar Q_{j-1},
\qquad \bar Q_{-1}=0.
$$

### 5.4 Six chronological passes

The following list completely specifies the finite computation.
Its logical order preserves the width-first limit: first execute only the
internal Gram and response calls in passes 1--5 to certify the rank of the
proposed operator DAG; then apply Section 3 at each fixed nonzero \(h\);
only after that identification use the output calls for \(F_1,F_3\) and
differentiate them at zero.  Internal operator regularity used to certify a
query Gram is not a finite-width output derivative or a limit exchange.

1. With covariance \(\operatorname{diag}(1,d)\), compile
   \(Q_{00},Q_{01},Q_{11},\rho_{10}\), and \(L_{10}\).
   Initialize its covariance bounds by

   $$
   \bar c_0=1+d,\qquad \bar c_j=0\quad(1\le j\le5).
   $$

2. With covariance \(\operatorname{diag}(1,Q^{[1]})\), compile
   \(F_1\), every \(K_{rs}\) for \(r,s\le1\), and every
   \(\sigma_{1r}\).  Its covariance bounds are

   $$
   \bar c_j=\mathbf1_{\{j=0\}}
   +\sum_{r,s\le1}\bar Q_{rs,j}.
   $$

3. With covariance \(\operatorname{diag}(1,K^{[1]})\), construct
   \(b_1,u_2,H_2\); compile \(Q_{r2}\) for \(r\le2\), and compile
   \(\rho_{2r},L_{2r}\) for \(r\le1\).

4. With covariance \(\operatorname{diag}(1,Q^{[2]})\), construct
   \(z_2,a_2,C_2\); compile every \(K_{rs}\), \(r,s\le2\), and every
   \(\sigma_{2r}\), \(r\le2\).

5. With covariance \(\operatorname{diag}(1,K^{[2]})\), construct
   \(b_2,u_3,H_3\); compile \(Q_{r3}\) for \(0\le r\le3\), and compile
   \(\rho_{3r},L_{3r}\) for \(0\le r\le2\).

6. With covariance \(\operatorname{diag}(1,Q^{[3]})\), construct
   \(z_3,a_3\), compile \(F_3=\mathbb E[a_3\phi(z_3)]\), and set

   $$
   \overline{\mathcal J}_{3,5}
   =\overline{\mathcal J}_5(F_3).
   $$

At passes 3--6 the covariance bound is always

$$
\bar c_j=\mathbf1_{\{j=0\}}+
\sum_{r,s}\bar G_{rs,j}
$$

over the displayed current Gram.  Retain

$$
\overline{\mathcal J}_{1,5}
=\overline{\mathcal J}_5(F_1)
$$

from pass 2.

This recursion terminates.  There are six passes, finitely many integrands
per pass, and the Price index set

$$
\{(r,j,s):r+j+\lceil s/2\rceil\le5\}
$$

is finite.  On it \(j+s\le10\).  A response integrand begins with activation
derivative order at most two, so no factor above \(\phi^{(12)}\) occurs.
The largest Gaussian block has dimension five.  Thus every compiler output
is a finite formula in \(M_\phi\), integer arithmetic, and the displayed
Gaussian moments; in particular,

$$
F_1,F_3\in C^5([-1,1])
$$

at the singular covariance \(h=0\), with the stated fifth-derivative
majorants.

## 6. Direct cubic jet of the width-first DAG

This section reproduces the calculation in
[the dedicated nodewise jet ledger](../mfp_quantitative_width_first_bound/RUNG3_CUBIC_JET.md).
That ledger differentiates the lower responses, feature Grams, terminal top
node, and every singular Price term in chronological order; it does not use
a symbolic script or a finite-width initialization derivative.

The sign change

$$
h\mapsto-h,\qquad A\mapsto-A,\qquad
(\chi_0,\chi_1,\chi_2)\mapsto-(\chi_0,\chi_1,\chi_2)
$$

leaves every \(u_s,H_s,z_s,Q,K\) unchanged and changes the sign of every
\(b_s,a_s,C_s,\rho,\sigma,L\).  This follows successively from the two
recursions in Section 2; both Gaussian laws are invariant under the displayed
sign changes.  Hence every \(F_N\) constructed by the same DAG is odd.

For the calculation only, extend the finite recursion of Section 2 to an
arbitrary fixed terminal index \(N\); this defines \(F_N\) by the same
chronological Gaussian nodes and requires no new limiting assertion.  We now
differentiate only that DAG.  At \(h=0\), all lower Gaussian coordinates
coalesce to \(X\sim N(0,d)\), and every activation argument within a given
layerwise expectation coalesces to a standard Gaussian.  Distinct lower and
top expectations use fresh independent Gaussian copies.  Because all copies
have the same law, we write \(G\) for the representative copy at the node
currently being differentiated, and set

$$
g=\phi(G),\qquad p=\phi'(G),\qquad q=\phi''(G).
$$

For a time index \(v\), direct differentiation of the lower recursion gives

$$
u_v'=vXp,
$$

$$
u_v''=v(v-1)(kgp+X^2pq).
$$

Indeed, direct differentiation of the top response integrand gives

$$
\sigma_{vr}'(0)=\delta\quad(r<v),
\qquad
\sigma_{vv}'(0)=v\beta.
$$

The historical derivatives follow from
\(d+ct=\delta\), the terminal derivative from \(v(b+cr)=v\beta\), and
\(Q'(0)=0\) eliminates a first-order Price term.  Together with the \(v\)
learned-matrix terms, this gives \(b_v'(0)=vkg\), proving the preceding
recursion.  Therefore

$$
H_v'=vXp^2,
$$

$$
H_v''
=v(2v-1)X^2p^2q+v(v-1)kgp^2.
$$

The only possible \(K''\)-Price term here differentiates the zeroth
integrand \(g^2\) in the \(\chi\)-coordinates and is zero.  It follows that

$$
\boxed{
Q_{rv}''(0)
=dm\{r(2r-1)+v(2v-1)\}
+k\ell\{r(r-1)+v(v-1)\}
+2rvde.
}
$$

To calculate the response contribution to the terminal top node, put

$$
R_N=\sum_{r<N}\rho_{Nr},
$$

$$
T_2(N)=\frac{N(N-1)(2N-1)}6,\qquad
C_2(N)=\frac{N(N-1)}2,\qquad
C_3(N)=\frac{N(N-1)(N-2)}6.
$$

Before coalescence, let \(S_v=\sum_{r<v}\chi_r\) and
\(D=\sum_{r<N}\partial_{\chi_r}\).  The already displayed lower recursion
gives

$$
u_v'=pS_v,
$$

$$
u_v''=v(v-1)kgp+2pq\sum_{r<v}\chi_rS_r.
$$

Differentiating this finite sum once more and applying \(D\) gives

$$
\begin{aligned}
Du_N'''={}&
6p^3\{(\delta+d)C_3(N)+\beta T_2(N)\}\\
&+3kgpq\{3T_2(N)-C_2(N)\}\\
&+9X^2p^2\phi'''(G)T_2(N)
 +18X^2pq^2C_3(N).
\end{aligned}
$$

Using

$$
DH_N'''
=3\phi'''(G)(u_N')^2Du_N'
+3q\{Du_N'\,u_N''+u_N'Du_N''\}
+pDu_N'''
$$

and taking the Gaussian expectation yields

$$
\boxed{
\begin{aligned}
R_N'''(0)={}&
\frac32N(4N^2-3N+1)dj\\
&+6N(N-1)(2N-1)ds\\
&+3N(N-1)(2N-1)km\\
&+N(N-1)e\{(\delta+d)(N-2)+\beta(2N-1)\}.
\end{aligned}
}
$$

The possible covariance-source correction is

$$
\frac32K''(0):D_\chi^2\partial_h(DH_N)|_{h=0}.
$$

But \(\partial_h(DH_N)|_{h=0}=Np^2\) is independent of \(\chi\), so this
term is exactly zero.

Since \(L_{Nr}=\rho_{Nr}+hQ_{rN}\),

$$
\sum_{r<N}L_{Nr}'''(0)
=R_N'''(0)+3\sum_{r<N}Q_{rN}''(0),
$$

where direct summation of the boxed \(Q''\)-formula gives

$$
\boxed{
\begin{aligned}
\sum_{r<N}Q_{rN}''(0)={}&
\frac{N(16N^2-15N+5)}6dm\\
&+\frac{2N(N-1)(2N-1)}3k\ell
+N^2(N-1)de.
\end{aligned}
}
$$

It remains to differentiate the terminal top integrand.  At coalescence,

$$
a_N'=Ng,\qquad
a_N''=N(N-1)cAp^2,
$$

$$
a_N'''
=cN(N-1)(N-2)gp^2
+\frac12c^2N(N-1)(4N-5)A^2p^2q,
$$

$$
z_N'=NcAp,
$$

$$
z_N''=cN(N-1)(gp+cA^2pq).
$$

Writing \(L_N^{(3)}=\sum_{r<N}L_{Nr}'''(0)\), one also obtains

$$
\begin{aligned}
z_N'''={}&ApL_N^{(3)}
+c^2N(N-1)(N-2)Ap^3\\
&+3c^2N(N-1)^2Agpq\\
&+\frac12c^3N(N-1)(2N-1)A^3p^2\phi'''(G)\\
&+c^3N(N-1)(N-2)A^3pq^2.
\end{aligned}
$$

Substitution into the six product/chain-rule terms of
\((a_N\phi(z_N))'''\) gives the full fixed-coordinate part

$$
\boxed{
\begin{aligned}
E_{3,N}={}&
2cN(N-1)(2N-1)\ell\\
&+2c^2N(N-1)(2N-1)e\\
&+\frac12c^2N(28N^2-33N+11)m\\
&+\frac32c^3N(4N^2-3N+1)j\\
&+6c^3N(N-1)(2N-1)s+dL_N^{(3)}.
\end{aligned}
}
$$

Let \(x_0,\ldots,x_N\) denote the formal coordinates of the top Gaussian
source block before coalescence.  The first terminal integrand derivative is

$$
\psi_1
=\left(\sum_{r<N}\phi(x_r)\right)\phi(x_N)
+cA^2\left(\sum_{r<N}\phi'(x_r)\right)\phi'(x_N).
$$

Its historical diagonal Hessians have expectation \(\beta\), its terminal
diagonal Hessian \(N\beta\), its historical-terminal Hessians \(\delta\),
and its distinct historical Hessians zero.  Since \(Q\) is even, the entire
source-law contribution in the third Price formula is therefore

$$
\boxed{
P_N
=\frac32\beta
\left\{\sum_{r<N}Q_{rr}''(0)+NQ_{NN}''(0)\right\}
+3\delta\sum_{r<N}Q_{rN}''(0).
}
$$

The remaining sum is

$$
\begin{aligned}
\sum_{r<N}Q_{rr}''(0)+NQ_{NN}''(0)
={}&\frac{N(16N^2-15N+5)}3dm\\
&+\frac{4N(N-1)(2N-1)}3k\ell\\
&+\frac{N(8N^2-3N+1)}3de.
\end{aligned}
$$

Adding \(E_{3,N}+P_N\), inserting the two response sums, and using
\(k=d+\beta+\delta\) gives, by direct collection of the nine displayed
activation moments,

$$
\boxed{
F_N'''(0)
=\frac{N(4N^2-3N+1)}2S_\phi
+2N(N-1)(2N-1)H_\phi.
}
$$

At first order the covariance derivative is zero and the terminal integrand
gives

$$
F_N'(0)=N(1+d+d^2).
$$

Thus

$$
F_1'''(0)=S_\phi,\qquad
F_3'''(0)=42S_\phi+60H_\phi,
$$

and

$$
\Delta_{31}'(0)=0,
\qquad
\frac{\Delta_{31}'''(0)}6
=\frac52S_\phi+10H_\phi
=\kappa_{31}.
$$

Every derivative in this section is a derivative of the already defined
Gaussian operator nodes.  The source-covariance terms were evaluated
explicitly; no initialization jet of the finite-width network was imported.

## 7. Explicit remainder and conclusion

Define the activation-only compiler output

$$
\boxed{
B_{31}
=\frac{\overline{\mathcal J}_{3,5}
+3^5\overline{\mathcal J}_{1,5}}{120}.
}
$$

This is not shorthand for an output supremum: Section 5 is its complete,
terminating numerical recursion.

For \(|t|\le h_{31}\), one has \(|t|\le1\) and \(|3t|\le1\), so

$$
\begin{aligned}
|\Delta_{31}^{(5)}(t)|
&\le |F_3^{(5)}(t)|+3^5|F_1^{(5)}(3t)|\\
&\le
\overline{\mathcal J}_{3,5}
+3^5\overline{\mathcal J}_{1,5}.
\end{aligned}
$$

Oddness, the linear cancellation, and Section 6 give

$$
\Delta_{31}(0)=\Delta_{31}'(0)=\Delta_{31}''(0)
=\Delta_{31}^{(4)}(0)=0,
$$

$$
\Delta_{31}'''(0)=6\kappa_{31}.
$$

Taylor's formula with integral remainder through order four therefore yields

$$
\Delta_{31}(\eta)-\kappa_{31}\eta^3
=\frac1{24}\int_0^\eta
(\eta-t)^4\Delta_{31}^{(5)}(t)\,dt.
$$

Since

$$
\frac1{24}\int_0^{|\eta|}(|\eta|-t)^4\,dt
=\frac{|\eta|^5}{120},
$$

we obtain

$$
\boxed{
|F_3(\eta)-F_1(3\eta)-\kappa_{31}\eta^3|
\le B_{31}|\eta|^5,
\qquad |\eta|\le h_{31}.
}
$$

If

$$
|\eta|
\le
\min\left\{
h_{31},
\sqrt{\frac{\varepsilon}{1+B_{31}}}
\right\},
$$

then

$$
B_{31}|\eta|^2
\le\frac{B_{31}}{1+B_{31}}\varepsilon
\le\varepsilon.
$$

Consequently,

$$
|F_3(\eta)-F_1(3\eta)|
\le(|\kappa_{31}|+\varepsilon)|\eta|^3.
$$

When \(\kappa_{31}\ne0\), this leading constant is sharp:
the fifth-order estimate implies
\(\Delta_{31}(\eta)/\eta^3\to\kappa_{31}\), so no bound with a coefficient
strictly below \(|\kappa_{31}|\) can hold on every punctured neighborhood of
zero.

Finally, if \(d=0\), continuity and Gaussian full support imply
\(\phi'\equiv0\).  RMS normalization gives \(\phi\equiv1\) or
\(\phi\equiv-1\).  The hidden parameters do not move, while the readout
changes by \(h\phi\) at every step, so, exactly at every finite width,

$$
F_{k,n}(h)=kh.
$$

Thus \(F_3(\eta)-F_1(3\eta)=0\).  In this case take

$$
\kappa_{31}=B_{31}=0,\qquad h_{31}=\frac13.
$$

This completes the fixed-step width identification, singular-covariance
regularity proof, activation-only rank radius, direct cubic calculation, and
quantitative fifth-order remainder without exchanging the width and
learning-rate limits.
