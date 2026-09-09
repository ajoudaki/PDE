# Three-step width-first identification and rank audit

This note treats the same network and normalization as the quantitative
two-step proof, but applies the update for `s=0,1,2`.  It establishes the
fixed-step identification and the extra nonterminal ranks needed for
`F_3(h)`.  It does not calculate the third jet of `F_3`.

## 1. Exact seven-action chronology

Put

$$
Y^s=WH^s/\sqrt n,\qquad D^s=W^\top C^s/\sqrt n,
$$

where `W=W^0`.  Since

$$
W^s=W+\frac h{\sqrt n}\sum_{r<s}C^r(H^r)^\top,
$$

the exact finite-width identities are

$$
z^s=Y^s+h\sum_{r<s}Q_{rs}^{(n)}C^r,
\qquad
b^s=D^s+h\sum_{r<s}K_{rs}^{(n)}H^r.
$$

In particular,

$$
b^2=D^2+hK_{02}^{(n)}H^0+hK_{12}^{(n)}H^1,
$$

$$
z^3=Y^3+hQ_{03}^{(n)}C^0+hQ_{13}^{(n)}C^1
       +hQ_{23}^{(n)}C^2.
$$

The source matrix is exposed in the predictable order

$$
Y^0,D^0,Y^1,D^1,Y^2,D^2,Y^3.
$$

The query for each action is measurable before that action: `C^s` is made
after `Y^s`, and `H^{s+1}` is made after `D^s`.  Thus the adaptive Gaussian
conditioning lemma applies at all seven actions.  The nonterminal blocks that
must be invertible are precisely

$$
Q_{0:2}=\mathbb E[H_{0:2}H_{0:2}^\top],\qquad
K_{0:2}=\mathbb E[C_{0:2}C_{0:2}^\top].
$$

The innovation of `H_3` is terminal and can vanish.

## 2. Three-step Gaussian recursion

The recursion can be written without inverse Grams.  At time `s`, define

$$
\rho_{sr}=\mathbb E[\partial_{\chi_r}H_s],\quad r<s,
\qquad
\sigma_{sr}=\mathbb E[\partial_{\xi_r}C_s],\quad r\le s.
$$

Then

$$
z_s=\xi_s+\sum_{r<s}(\rho_{sr}+hQ_{rs})C_r,
$$

$$
a_s=A+h\sum_{r<s}\phi(z_r),\qquad C_s=a_s\phi'(z_s),
$$

and

$$
b_s=\chi_s+
\sum_{r\le s}\sigma_{sr}H_r
+h\sum_{r<s}K_{rs}H_r,
$$

$$
u_{s+1}=u_s+h b_s\phi'(u_s),\qquad H_{s+1}=\phi(u_{s+1}).
$$

Here `(\xi_0,\ldots,\xi_s)` has Gram `Q_{0:s}`, while
`(\chi_0,\ldots,\chi_s)` has Gram `K_{0:s}`; the two Gaussian blocks and
`A,U` are independent.  At `s=0`, `\sigma_{00}=0` by centering of `A`.
The terminal output is

$$
F_3(h)=\mathbb E[a_3\phi(z_3)].
$$

For `s=0,1` these formulas are exactly the four-stage recursion already
proved.  At `s=2` they add `C_2`, `D^2`, `H_3`, and `Y^3`.

## 3. The two new reused-matrix cancellations

The following calculation explicitly handles all dependencies at the two
new actions.  It is the population limit of the exact adaptive conditioning
formula, not an independence assertion.

For `D^2`, write

$$
h_*=(H_0,H_1,H_2)^\top,\quad c_*=(C_0,C_1)^\top,
$$

$$
y=(Y^0,Y^1,Y^2)^\top=\xi+Pc_*,
\quad
d=(D^0,D^1)^\top=\chi+Sh_*,
$$

with

$$
P=\begin{pmatrix}
0&0\\ \rho_{10}&0\\ \rho_{20}&\rho_{21}
\end{pmatrix},
\qquad
S=\begin{pmatrix}
0&0&0\\ \sigma_{10}&\sigma_{11}&0
\end{pmatrix}.
$$

Let `Q=Q_{0:2}`, `K=K_{0:1}`,

$$
k=\mathbb E[c_*C_2],\qquad
\sigma_2=(\sigma_{20},\sigma_{21},\sigma_{22})^\top.
$$

Gaussian integration by parts gives

$$
R:=\mathbb E[c_*y^\top]=SQ+KP^\top,
$$

$$
r:=\mathbb E[yC_2]=Q\sigma_2+Pk.
$$

Consequently, the `h_*` coefficient in the column-conditioning formula is

$$
Q^{-1}(r-R^\top K^{-1}k)
=\sigma_2-S^\top K^{-1}k.
$$

The old-action term `d^\top K^{-1}k` contributes
`h_*^\top S^\top K^{-1}k`, cancelling the second summand.  Its Gaussian
part and the new orthogonal innovation form `\chi_2` with the prescribed
extended Gram.  Hence

$$
D^2=\chi_2+\sigma_{20}H_0+\sigma_{21}H_1+\sigma_{22}H_2
$$

in the limit, and adding the learned-matrix terms gives the displayed
formula for `b_2`.

For `Y^3`, enlarge the preceding matrices to

$$
P=\begin{pmatrix}
0&0&0\\ \rho_{10}&0&0\\ \rho_{20}&\rho_{21}&0
\end{pmatrix},
\qquad
S=\begin{pmatrix}
0&0&0\\ \sigma_{10}&\sigma_{11}&0\\
\sigma_{20}&\sigma_{21}&\sigma_{22}
\end{pmatrix}.
$$

Now `h_*=(H_0,H_1,H_2)^\top`, `c_*=(C_0,C_1,C_2)^\top`, and

$$
y=\xi+Pc_*,\qquad d=\chi+Sh_*.
$$

For

$$
q=\mathbb E[h_*H_3],\qquad
\rho_3=(\rho_{30},\rho_{31},\rho_{32})^\top,
$$

integration by parts gives

$$
R=SQ+KP^\top,qquad
v:=\mathbb E[dH_3]=K\rho_3+Sq.
$$

The direct `c_*` coefficient from row conditioning is therefore

$$
K^{-1}(v-RQ^{-1}q)=\rho_3-P^\top Q^{-1}q.
$$

The row projection `y^\top Q^{-1}q` contributes
`c_*^\top P^\top Q^{-1}q`, cancelling the second term.  Thus

$$
Y^3=\xi_3+\rho_{30}C_0+\rho_{31}C_1+\rho_{32}C_2,
$$

and the exact learned-matrix terms turn this into `z_3`.

## 4. The seven-query convergence statement

Fix a nonzero `h` for which `Q_{0:2}` and `K_{0:2}` are positive definite.
The five-query coupling proof extends with the following completely finite
changes:

1. use iid column marks `(U,g_0,g_1,g_2)` and row marks
   `(A,e_0,e_1,e_2,e_3)`;
2. after constructing `K_{0:2}`, generate `\chi_2` by its Gaussian
   regression on `(\chi_0,\chi_1)` plus one fresh `g_2` innovation;
3. after constructing `Q_{0:3}`, generate the terminal `\xi_3` by its
   regression on `(\xi_0,\xi_1,\xi_2)` plus one fresh `e_3` innovation;
4. insert the two ideal actions proved in Section 3 of this note;
5. run the stopped coupling for seven, rather than five, actions; the good
   event now also requires the empirical third feature and cotangent Schur
   complements to be at least half their population values;
6. run the raw-energy recursion through `s=2` and form the terminal fields at
   `s=3`.

At each of the two new actions, every coefficient is a rational function of
the finitely many empirical Gram and cross-moment entries displayed in
Section 3.  On the good event its inverse is Lipschitz.  Rosenthal bounds the
new ideal empirical averages, the projector estimate bounds each new
orthogonal innovation, and the polynomial-Lipschitz coordinate estimate
transfers the coupling through `C_2,H_3`.  High-moment Markov bounds make the
probability of either new good-event failure `O(n^{-M})` for arbitrary fixed
`M`.  The raw-energy polynomials and Holder's inequality remove stopping.
They also give uniform integrability of

$$
\frac1n\sum_i a_i^3\phi(z_i^3).
$$

Since this is a seven-element list, the recursion terminates after the
terminal `Y^3` action.  It follows that

$$
\lim_{n\to\infty}\mathbb E[f_n^3]=F_3(h)
$$

at every such fixed `h`.  No small-step limit has entered this argument.

## 5. Desingularized feature rank

Write, for `G\sim N(0,1)`,

$$
d=\mathbb E[\phi'(G)^2],\quad
e=\mathbb E[\phi'(G)^4],\quad
t=\mathbb E[\phi''(G)^2],
$$

and retain the activation moments `c,k,\tau` from the two-step proof.  Thus
`c=1+d` and `\tau>0` whenever `d>0`.

Let `U\sim N(0,1)`, `B\sim N(0,d)`, and `T\sim N(0,\tau)` be independent.
Put, with all activation factors evaluated at `U`,

$$
P_0=\phi(U),\qquad
P_1=B\phi'(U)^2,
$$

$$
P_2=T\phi'(U)^2
    +k\phi(U)\phi'(U)^2
    +2B^2\phi'(U)^2\phi''(U).
$$

The two-step Gram expansion and its explicit rank radius permit the smooth
realization

$$
\chi_1=\frac{K_{01}(h)}dB
+h\sqrt{\frac{\det K_{0:1}(h)}{d h^2}}\,Z,
$$

where `Z` is independent standard Gaussian.  The square-root factor tends
to `\sqrt\tau`.  Taylor expansion of the exact lower recursion, with an
`L^2` integral remainder, gives

$$
\frac{H_1-H_0}{h}\longrightarrow P_1,
$$

$$
\frac{H_2-2H_1+H_0}{h^2}\longrightarrow P_2.
$$

The three limits are pairwise orthogonal except possibly `P_0,P_2`:

$$
\mathbb E[P_0P_1]=0,\qquad
\mathbb E[P_1P_2]=0,qquad
\mathbb E[P_1^2]=de.
$$

The second equality follows term by term from independence and the odd
Gaussian moments `E[B]=E[B^3]=E[BT]=0`.  Define the explicit activation
integrals

$$
a_Q=\mathbb E[P_0P_2],
\qquad
\lambda_Q=\mathbb E[P_2^2]-a_Q^2.
$$

Equivalently,

$$
a_Q=k\,\mathbb E[\phi(G)^2\phi'(G)^2]
    +2d\,\mathbb E[\phi(G)\phi''(G)\phi'(G)^2].
$$

The term `T\phi'(U)^2` is orthogonal to both preceding directions and to
the rest of `P_2`; hence

$$
\lambda_Q\ge\tau e>0.
$$

If `\widehat Q(h)` denotes the Gram of

$$
H_0,\quad (H_1-H_0)/h,\quad
(H_2-2H_1+H_0)/h^2,
$$

then

$$
\widehat Q(h)\longrightarrow
G_Q:=\operatorname{Gram}(P_0,P_1,P_2),
$$

and

$$
\det G_Q=de\lambda_Q>0,
\qquad
\det Q_{0:2}(h)=h^6\det\widehat Q(h).
$$

## 6. Desingularized cotangent rank

Let `(X,S,R)` be centered Gaussian with covariance `G_Q`.  It can be written

$$
X=Z_0,\qquad S=\sqrt{de}\,Z_1,
\qquad R=a_QZ_0+\sqrt{\lambda_Q}\,Z_2,
$$

with independent standard `Z_0,Z_1,Z_2`.  Let `A` be another independent
standard Gaussian.  In the formulas below, put

$$
g=\phi(X),\quad p=\phi'(X),\quad q=\phi''(X),
\quad r=\phi'''(X).
$$

Define

$$
R_1=S+cAp,
$$

$$
T_0=Ap,qquad T_1=gp+AqR_1,
$$

$$
R_2=R+cT_1,
$$

$$
T_2=p^2R_1+AqR_2+2gqR_1+ArR_1^2.
$$

Taylor expansion of the exact top recursion in the Newton Gaussian
coordinates gives

$$
\frac{C_1-C_0}{h}\longrightarrow T_1,
$$

$$
\frac{C_2-2C_1+C_0}{h^2}\longrightarrow T_2
$$

in `L^2`.  For the second formula, the raw Gaussian second difference tends
to `R`; the response second difference is `cT_1`, which explains `R_2`.

One has

$$
\mathbb E[T_0T_1]=0,qquad
\mathbb E[T_0^2]=d,qquad
\mathbb E[T_1^2]=\tau.
$$

Define the explicit Gaussian activation integral

$$
\lambda_K
=\mathbb E[T_2^2]
-\frac{\mathbb E[T_0T_2]^2}{d}
-\frac{\mathbb E[T_1T_2]^2}{\tau}.
$$

If `t>0`, the component

$$
Aq\sqrt{\lambda_Q}\,Z_2
$$

of `T_2` is orthogonal to every function of `(A,Z_0,Z_1)`, including
`T_0,T_1` and every other component of `T_2`.  Therefore

$$
\lambda_K\ge t\lambda_Q>0.
$$

If `t=0`, continuity gives `\phi''\equiv0`, so
`\phi(x)=\alpha x+\beta` with `d=\alpha^2>0`.  In this case the component of
`T_2` orthogonal to `T_0,T_1` is

$$
\alpha^2\sqrt{de}\,Z_1,
$$

whose variance is

$$
\alpha^4de=\alpha^{10}=d^5>0.
$$

Thus no nondegeneracy assumption beyond `d>0` is required.

If `\widehat K(h)` is the Gram of

$$
C_0,\quad (C_1-C_0)/h,\quad
(C_2-2C_1+C_0)/h^2,
$$

then

$$
\widehat K(h)\longrightarrow
G_K:=\operatorname{Gram}(T_0,T_1,T_2),
$$

$$
\det G_K=d\tau\lambda_K>0,
\qquad
\det K_{0:2}(h)=h^6\det\widehat K(h).
$$

## 7. An explicit activation-defined rank radius

The preceding convergence can be made quantitative without differentiating
an output.  Apply the envelope arithmetic from the two-step proof to the
fixed Gaussian realizations above, adding the rules

$$
\mathcal E\!\left(\int_0^1g(s)\,ds\right)=\mathcal E(g),
$$

$$
\mathcal E(x^{-1})=(m^{-1},0),\qquad
\mathcal E((x^{-1})')=(m^{-2},0)\odot\mathcal E(x'),
$$

$$
\mathcal E(\sqrt x)=(\sqrt M,0),\qquad
\mathcal E((\sqrt x)')=(2\sqrt m)^{-1}\odot\mathcal E(x'),
$$

whenever the already-certified scalar input obeys `m\le x\le M`.
Use the integral identities

$$
\frac{N(h)}h=\int_0^1N'(sh)\,ds
\quad(N(0)=0),
$$

$$
\frac{N(h)}{h^2}=\int_0^1(1-s)N''(sh)\,ds
\quad(N(0)=N'(0)=0)
$$

for every Newton difference.  First use the old explicit two-time rank
radius to bound the conditional square root defining `\chi_1`.  The
resulting finite differentiation tree returns numbers `A_{Q,i}` such that

$$
\|\widehat H_i(h)-P_i\|_2\le A_{Q,i}|h|,
\qquad i=0,1,2.
$$

After the feature rank below has been certified, apply the ordinary
three-by-three Cholesky recursion

$$
L_{jj}=\sqrt{G_{jj}-\sum_{r<j}L_{jr}^2},
\qquad
L_{ij}=\frac{G_{ij}-\sum_{r<j}L_{ir}L_{jr}}{L_{jj}}
$$

to `\widehat Q(h)`.  The just-certified eigenvalue bound supplies all
positive lower inputs for the reciprocal and square-root rules.  The same
finite tree returns `A_{K,i}` with

$$
\|\widehat C_i(h)-T_i\|_2\le A_{K,i}|h|.
$$

Only three coordinate updates and derivatives through third order occur;
the `C^{12}` envelope is more than sufficient.  The tree is acyclic: lower
two-time data, lower three-time data, its Cholesky factor, and top
three-time data are processed in that order.  Every integral rule removes
one displayed difference quotient, so the recursion terminates after a
finite number of syntactic nodes.

For `X_i=P_i` or `T_i`, define

$$
E_{ij}=A_i\|X_j\|_2+A_j\|X_i\|_2+A_iA_j.
$$

Then Cauchy--Schwarz gives, for `|h|\le1`,

$$
|\widehat G_{ij}(h)-G_{ij}|\le E_{ij}|h|.
$$

Let

$$
E_Q=\max_{i,j}E^Q_{ij},\quad
L_Q=1+\max_{i,j}|(G_Q)_{ij}|+E_Q,
$$

and define `E_K,L_K` analogously.  Since a three-by-three determinant is a
sum of six triple products,

$$
|\det A-\det B|
\le18L^2\max_{i,j}|A_{ij}-B_{ij}|
$$

whenever all entries of `A,B` are bounded by `L`.  Therefore the fully
activation-defined radius

$$
r_{Q,3}
=\min\left\{r_2,
\frac{de\lambda_Q}{36L_Q^2(1+E_Q)}\right\},
$$

$$
r_{K,3}
=\min\left\{r_{Q,3},
\frac{d\tau\lambda_K}{36L_K^2(1+E_K)}\right\},
$$

where `r_2` is the explicit two-time rank radius, satisfies, for every
`0<|h|\le r_{K,3}`,

$$
\det Q_{0:2}(h)\ge\frac12de\lambda_Q|h|^6>0,
$$

$$
\det K_{0:2}(h)\ge\frac12d\tau\lambda_K|h|^6>0.
$$

All inputs to this radius are finite Gaussian activation integrals or
numbers returned by the displayed finite envelope recursion.  No network
output, trained-trajectory supremum, or continuity modulus is used.

Consequently the seven-action identification in Sections 1--4 holds at
every fixed nonzero `h` in this interval, before any limit `h\to0` is taken.
