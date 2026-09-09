# Two-time rank and the activation-only fifth-order remainder

This note closes the rank and remainder parts of the three-hidden-layer
comparison

\[
 \Delta_{21}(\eta)=F_2(\eta)-F_1(2\eta).
\]

It uses the exact Gaussian operator DAG in `WIDTH_DAG.md`.  In particular,
all derivatives below are derivatives of that already-defined width-first
operator program.  No finite-width Taylor expansion is used.

Throughout, $Z\sim N(0,1)$,

\[
 \mathbb E\phi(Z)^2=1,
 \qquad
 M_\phi=
 \max\left\{1,
 \sup_x\frac{|\phi(x)|}{1+|x|},
 \max_{1\le j\le12}\|\phi^{(j)}\|_\infty\right\}<\infty .       \tag{1}
\]

Thus $\phi\in C^{12}$, has at most linear growth, and its first twelve
derivatives are bounded.  Put, with
$\phi_j=\phi^{(j)}(Z)$,

\[
\begin{aligned}
 d&=\mathbb E\phi_1^2,& e&=\mathbb E\phi_1^4,
 &b&=\mathbb E[\phi_0\phi_2],\\
 m&=\mathbb E[\phi_0\phi_2\phi_1^2],
 &r&=\mathbb E[\phi_1\phi_3],
 &s&=\mathbb E[\phi_2^2\phi_1^2],\\
 \ell&=\mathbb E[\phi_0^2\phi_1^2],
 &t&=\mathbb E\phi_2^2.
\end{aligned}                                                   \tag{2}
\]

These are finite and are activation data only.

## 1. Result

Let $Q_H,Q_G,K_E,K_C$ be the two-time population Grams in
`WIDTH_DAG.md`: $H,G$ are the first and second hidden activations, while
$E,C$ are the middle and top cotangents.  If $d>0$, define

\[
 c_1=1+d,
 \qquad
 \nu_H=d^2e,                                                    \tag{3}
\]

\[
 \nu_G=d\nu_H+c_1^2de
       =de\bigl(d^2+c_1^2\bigr),
 \qquad
 c_2=1+c_1d=1+d+d^2,                                          \tag{4}
\]

\[
 \tau_C
 =\ell+2c_2m+3c_2^2s+\nu_Gt,                                 \tag{5}
\]

\[
 k_C=2d+b+c_2(r+t),                                            \tag{6}
\]

and

\[
 \tau_E
 =d\tau_C+k_C^2\ell+\nu_Hdt
   +3c_1^2d^2s+2k_Cc_1dm.                                    \tag{7}
\]

Then

\[
\begin{array}{c|c}
 \text{Gram}&\displaystyle\lim_{h\to0}\frac{\det\operatorname{Gram}(h)}{h^2}\\
 \hline
 Q_H&\nu_H\\
 Q_G&\nu_G\\
 K_C&d\tau_C\\
 K_E&d^2\tau_E.
\end{array}                                                    \tag{8}
\]

All four numbers in the right column are strictly positive.  Sections 2--4
prove (8), including positivity, directly from the operator DAG.

Section 5 gives a terminating activation-envelope compiler.  Denote its
fourth-derivative Gram bounds by

\[
 \bar Q_{H,rs,j},\quad \bar Q_{G,rs,j},\quad
 \bar K_{E,rs,j},\quad \bar K_{C,rs,j},                       \tag{9}
\]

and its output fifth-derivative bounds by

\[
 \overline{\mathcal J}_{1,5},\qquad
 \overline{\mathcal J}_{2,5}.                                \tag{10}
\]

Define

\[
\begin{aligned}
 D_{Q_H}
 &=\bar Q_{H,11,4}
   +\sum_{a=0}^4\binom4a
      \bar Q_{H,01,a}\bar Q_{H,01,4-a},\\
 D_{Q_G}
 &=\bar Q_{G,11,4}
   +\sum_{a=0}^4\binom4a
      \bar Q_{G,01,a}\bar Q_{G,01,4-a},\\
 D_{K_C}
 &=d\bar K_{C,11,4}
   +\sum_{a=0}^4\binom4a
      \bar K_{C,01,a}\bar K_{C,01,4-a},\\
 D_{K_E}
 &=d^2\bar K_{E,11,4}
   +\sum_{a=0}^4\binom4a
      \bar K_{E,01,a}\bar K_{E,01,4-a}.                     \tag{11}
\end{aligned}
\]

For a positive number $a$ and a nonnegative number $D$, set

\[
 R(a,D)=\min\left\{1,\sqrt{\frac{12a}{1+D}}\right\}.          \tag{12}
\]

The explicit rank/remainder constants are

\[
\begin{aligned}
 h_\phi=\min\bigl\{&\tfrac12,
 R(\nu_H,D_{Q_H}),R(\nu_G,D_{Q_G}),\\
 &R(d\tau_C,D_{K_C}),R(d^2\tau_E,D_{K_E})\bigr\},            \tag{13}
\end{aligned}
\]

\[
 B_\phi
 =\frac{\overline{\mathcal J}_{2,5}
          +2^5\overline{\mathcal J}_{1,5}}{120}.             \tag{14}
\]

They are finite, strictly positive except that $B_\phi$ is allowed to be
zero, and are computed solely from (1), finitely many Gaussian activation
moments, integer arithmetic, and the explicit Gaussian moments in (39)
below.  For every $0<|h|\le h_\phi$, all four two-time Grams are positive
definite.  The exact seven-call Price-jet recursion in `PROOF.md`,
equations (5.12)--(5.24), first defines the activation-only number
$\kappa_\phi=\kappa_\phi^{\rm PJ}$ and then proves

\[
 \Delta_{21}'(0)=0,
 \qquad
 \kappa_\phi=\frac{\Delta_{21}^{(3)}(0)}6.                   \tag{15}
\]

Consequently the compiler proves, without an unspecified remainder,

\[
 \left|\Delta_{21}(\eta)-\kappa_\phi\eta^3\right|
 \le B_\phi|\eta|^5,
 \qquad |\eta|\le h_\phi.                                   \tag{16}
\]

The derivative quotient in (15) is not the definition of $\kappa_\phi$:
the finite Price recursion constructs it first from explicit Gaussian
activation integrals.  Formula (14) is the complete quantitative remainder
constant.

If $d=0$, continuity and full support of Gaussian measure give
$\phi'\equiv0$.  Normalization makes $\phi\equiv\pm1$; the exact network
has $F_k(h)=kh$.  Hence $\Delta_{21}\equiv0$, and one may set

\[
 h_\phi=\tfrac12,\qquad B_\phi=0,\qquad \kappa_\phi=0.         \tag{17}
\]

## 2. A Gram forward-difference lemma

Let $X_0\in L^2$ and suppose

\[
 X_1(h)=X_0+hP+o_{L^2}(h).                                   \tag{18}
\]

Writing ${\cal G}(h)=\operatorname{Gram}(X_0,X_1(h))$, direct
expansion of its determinant gives

\[
 \lim_{h\to0}\frac{\det {\cal G}(h)}{h^2}
 =\|X_0\|_2^2\|P\|_2^2-\langle X_0,P\rangle^2.              \tag{19}
\]

Indeed, write $X_1=X_0+hP+hR_h$, where
$\|R_h\|_2\to0$.  The determinant is unchanged after replacing its
second Gram vector by $X_1-X_0$.  It is therefore

\[
 h^2\left(
 \|X_0\|_2^2\|P+R_h\|_2^2
 -\langle X_0,P+R_h\rangle^2\right),
\]

which proves (19).

We will repeatedly use a signed Gaussian realization at a singular
two-time covariance.  If $X_1-X_0=hP+o_{L^2}(h)$, (19) and ordinary
Gaussian regression permit the corresponding centered Gaussian source to
be realized as

\[
 \xi_1(h)=\frac{\mathbb E[X_0X_1(h)]}{\mathbb E X_0^2}\xi_0
 +h\sqrt{v(h)}\,Z_*,                                        \tag{20}
\]

where $Z_*$ is fresh standard Gaussian and $v(h)\to v_0$, the Schur
coefficient in (19) divided by $\mathbb E X_0^2$.  For negative $h$,
the factor $h$, not $|h|$, is used.  This has exactly the prescribed
covariance and is differentiable at zero in $L^p$ for every finite $p$.
Thus all jets below are jets of Gaussian expectations at the singular
covariance, not derivatives of a Cholesky factor containing $|h|$.

## 3. Forward jets

Take mutually independent variables

\[
 U,Z,Y,A,E_H,E_G\sim N(0,1),
 \qquad X\sim N(0,d^2),\qquad \Omega\sim N(0,d).              \tag{21}
\]

Here $X=\chi_0$ is the initial raw $W^T$-source and
$\Omega=\omega_0$ is the initial raw $V^T$-source in the notation of
the Gaussian DAG.

At the first hidden layer,

\[
 u_1=U+hX\phi'(U),
\]

so the first activation forward difference is

\[
 P_H=X\phi'(U)^2,
 \qquad
 \mathbb E[\phi(U)P_H]=0,
 \qquad
 \mathbb EP_H^2=d^2e=\nu_H.                                 \tag{22}
\]

The first raw $W$-source difference therefore has derivative
$\sqrt{\nu_H}E_H$.  Also

\[
 (\rho^W_{10})'(0)
 =\mathbb E\phi'(U)^2=d,
\]

while the learned-$W$ term contributes $Q_{H,00}=1$.  Hence the first
variation of the second-layer preactivation is

\[
 R_z=\sqrt{\nu_H}E_H+c_1\Omega\phi'(Z).                     \tag{23}
\]

Consequently the second-hidden activation difference has derivative

\[
 P_G=\phi'(Z)R_z.                                            \tag{24}
\]

Independence and centering give

\[
 \mathbb E[\phi(Z)P_G]=0,
\]

and

\[
 \mathbb EP_G^2
 =\nu_Hd+c_1^2de=\nu_G.                                     \tag{25}
\]

The first raw $V$-source difference therefore has derivative
$\sqrt{\nu_G}E_G$.  Differentiating $G_1$ with respect to the initial
raw $V^T$-source $\Omega$ gives

\[
 (\rho^V_{10})'(0)=c_1\mathbb E\phi'(Z)^2=c_1d.
\]

Adding the learned-$V$ coefficient $Q_{G,00}=1$ gives $c_2$.  Thus
the top preactivation variation is

\[
 R_y=\sqrt{\nu_G}E_G+c_2A\phi'(Y).                           \tag{26}
\]

Equations (19), (22), and (25) prove the first two rows of (8).

## 4. Cotangent jets and universal positivity

At initialization the top cotangent is

\[
 C_0=A\phi'(Y),\qquad \mathbb EC_0^2=d.                     \tag{27}
\]

Since $a_1=A+h\phi(Y)$, its forward difference is

\[
 T_C=\phi(Y)\phi'(Y)+A\phi''(Y)R_y.                          \tag{28}
\]

Every term in $\mathbb E[C_0T_C]$ contains either an odd power of $A$
or the independent centered $E_G$, so

\[
 \mathbb E[C_0T_C]=0.                                       \tag{29}
\]

Expanding the square in (28) gives

\[
 \mathbb ET_C^2
 =\ell+2c_2m+3c_2^2s+\nu_Gt=\tau_C.                         \tag{30}
\]

This proves the $K_C$ row of (8).

For completeness, we now derive the response entering the middle
cotangent; it cannot be discarded.  The signed two-source realization (20)
and (29) show that the raw $V^T$-source difference is
$\sqrt{\tau_C}B_C$, with $B_C\sim N(0,1)$ fresh.  The sum of the two
first-order transpose-response coefficients is

\[
 \mathbb E[\partial_YT_C]
 =d+b+c_2(r+t).                                               \tag{31}
\]

To verify (31), differentiate (28), holding $A,E_G$ fixed.  The
derivative of $\phi\phi'$ has expectation $d+b$.  The term containing
$E_G$ remains centered.  The two remaining expectations are
$c_2\mathbb E[\phi'\phi_3]=c_2r$ and
$c_2\mathbb E\phi_2^2=c_2t$.  The learned-$V$ transpose term contributes
$K_{C,00}=d$.  Therefore the variation of the full back-propagated field
$d_1$ in `WIDTH_DAG.md` is

\[
 \dot d_1=\sqrt{\tau_C}B_C+k_C\phi(Z),                       \tag{32}
\]

with $k_C$ given by (6).  This calculation is also obtained directly by
differentiating the displayed responses
$\sigma^V_{10},\sigma^V_{11}$: at zero their values vanish, and the
derivative of their sum is (31).  Thus (32) includes both reused-$V$
response terms and the learned rank-one term.

The middle cotangent is $E_s=d_s\phi'(z_s)$.  Combining (23) and (32)
gives

\[
\begin{aligned}
 T_E
 :={}&\left.\frac{d}{dh}E_1(h)\right|_{h=0}\\
 ={}&\sqrt{\tau_C}B_C\phi'(Z)
 +k_C\phi(Z)\phi'(Z)\\
 &+\sqrt{\nu_H}\,\Omega E_H\phi''(Z)
 +c_1\Omega^2\phi'(Z)\phi''(Z).                             \tag{33}
\end{aligned}
\]

Again, every term in $\mathbb E[E_0T_E]$, where
$E_0=\Omega\phi'(Z)$, contains a centered independent factor or an odd
power of $\Omega$.  Hence

\[
 \mathbb E[E_0T_E]=0.                                       \tag{34}
\]

The first summand in (33) is orthogonal to the other three.  Expanding the
square of the remaining terms yields

\[
\begin{aligned}
 \mathbb ET_E^2
 ={}&d\tau_C+k_C^2\ell+\nu_Hdt
 +3c_1^2d^2s+2k_Cc_1dm\\
 ={}&\tau_E.                                                 \tag{35}
\end{aligned}
\]

Equations (19), (34), and $\mathbb EE_0^2=d^2$ prove the $K_E$ row of
(8).

It remains to verify strict positivity without assuming a generic
activation.  Since $d>0$, $e>0$, so $\nu_H,\nu_G>0$.  If $t>0$, the
$A E_G\phi''(Y)$ component of $T_C$ has squared norm
$\nu_Gt>0$ and is orthogonal to all components not containing $E_G$.
Thus $\tau_C>0$.  If $t=0$, continuity and full Gaussian support give
$\phi''\equiv0$; hence $\phi$ is a nonconstant affine function.  Then
$T_C=\phi(Y)\phi'(Y)$ and

\[
 \tau_C=\mathbb E[\phi(Y)^2\phi'(Y)^2]=d>0.                 \tag{36}
\]

Finally, the $B_C$-component in (33) is orthogonal to the other terms, so

\[
 \tau_E=d\tau_C+
 \left\|k_C\phi_0\phi_1+\sqrt{\nu_H}\Omega E_H\phi_2
       +c_1\Omega^2\phi_1\phi_2\right\|_2^2
 \ge d\tau_C>0.                                             \tag{37}
\]

This proves universal positivity of every coefficient in (8) for every
nonconstant activation in (1).

There is also a formal consistency check against the conditional compact
recursion in `CUBIC.md`.  In its notation, our moments satisfy

\[
 e_{\rm here}=u_{\rm cubic},\qquad
 b_{\rm here}=v_{\rm cubic},\qquad
 s_{\rm here}=e_{\rm cubic},\qquad
 t_{\rm here}=s_{\rm cubic}.
\]

Substitution into equations (5.2)--(5.11) there gives

\[
 V_1=\nu_H,\qquad V_2=\nu_G,\qquad
 \Theta_1=c_1,\qquad \Theta_2=c_2,
\]

and, in the reverse pass,

\[
 \beta_3=\tau_C,\qquad \gamma_3=k_C,\qquad \beta_2=\tau_E.  \tag{37a}
\]

Thus the unconditional forward-difference Gram computation agrees term for
term with that compact recursion where their formulas overlap.  This check
does not invoke, or prove, the population-intertwining hypothesis isolated
in `CUBIC.md`.

## 5. Explicit activation-envelope compiler

This section gives all rules that produce the bars in (9)--(10).  It also
proves $C^5$ regularity at the singular covariance $h=0$.

### 5.1 Envelope syntax

An envelope is a pair $(A,p)\in[0,\infty)\times\mathbb N$, meaning

\[
 |g(x)|\le A(1+\|x\|)^p.
\]

Define

\[
 (A,p)\oplus(B,q)=(A+B,\max\{p,q\}),
 \qquad
 (A,p)\odot(B,q)=(AB,p+q).                                  \tag{38}
\]

Scalar multiplication by $\lambda$ replaces $A$ by $|\lambda|A$.
Initialize

\[
 \mathcal E(1)=\mathcal E(h)=(1,0),\qquad
 \mathcal E(x_i)=(1,1),
\]

and propagate exact sums and products using (38).  If
$\mathcal E(g)=(A,p)$, set

\[
 \mathcal E(\phi(g))=(M_\phi(1+A),p),\qquad
 \mathcal E(\phi^{(j)}(g))=(M_\phi,0),\quad1\le j\le12.
\]

Formal derivatives are generated, term by term including multiplicities,
by

\[
 \partial(uv)=(\partial u)v+u(\partial v),\qquad
 \partial\phi^{(j)}(u)=\phi^{(j+1)}(u)\partial u,
\]

and the usual derivatives of $h,x_i$.  If $S(h)$ is a scalar node
already compiled, introduce tokens $S^{[j]}$, put

\[
 \mathcal E(S^{[j]})=(\bar S_j,0),\qquad
 \partial_hS^{[j]}=S^{[j+1]},\qquad \partial_{x_i}S^{[j]}=0.
\]

Only $0\le j\le5$ is ever requested.

For a Gaussian dimension $D\in\mathbb N$, $p\in\mathbb N$, and $v\ge0$,
define the explicit moment

\[
 \mu_{D,p}(v)
 =\mathbb E(1+\sqrt v\|G_D\|)^p
 =\sum_{q=0}^p\binom pqv^{q/2}2^{q/2}
   \frac{\Gamma((D+q)/2)}{\Gamma(D/2)}.                      \tag{39}
\]

### 5.2 Price constructor, including singular covariances

For a $C^5$ positive-semidefinite $D\times D$ covariance $\Sigma(h)$,
possibly singular, and a polynomially dominated integrand $\psi(h,x)$,
put

\[
 N(h)=\mathbb E_{X\sim N(0,\Sigma(h))}\psi(h,X).
\]

For every real matrix $B$, write

\[
 \|B\|_\Sigma:=\sum_{r,s}|B_{rs}|.
\]

This entrywise norm dominates the operator norm; for a covariance it
therefore supplies the Gaussian moment majorant used below.

If all mixed derivatives with
$j+\lceil|\alpha|/2\rceil\le5$ have a common polynomial envelope, then

\[
 N'(h)=\mathbb E\left[
 \partial_h\psi+\tfrac12\Sigma'(h):D_x^2\psi\right].         \tag{40}
\]

This formula remains valid when $\Sigma(h)$ changes rank.  To prove it,
first take a Schwartz integrand.  Fourier inversion writes the Gaussian
expectation with multiplier
$e^{-\zeta^T\Sigma(h)\zeta/2}$; differentiating this multiplier produces
$-\zeta^T\Sigma'\zeta/2$, the Fourier multiplier of the second term in
(40).  No covariance inverse occurs.  For a polynomial-growth integrand,
multiply by a smooth cutoff supported in $\|x\|\le2R$, mollify, and apply
the Schwartz identity.  All differentiated cutoffs are bounded by the same
polynomial envelope uniformly in $R$.  Since

\[
 \sup_{|h|\le1}\mathbb E(1+\|X_h\|)^p
 \le\mu_{D,p}\left(\sup_{|h|\le1}\|\Sigma(h)\|_\Sigma\right)<\infty,
\]

Gaussian tail uniform integrability permits first removing the mollifier
and then the cutoff.  Iterating this argument five times proves $C^5$
regularity and repeated Price differentiation.

The following finite recursion turns that proof into numerical bounds.  If

\[
 \bar c_j\ge\|\Sigma^{(j)}(h)\|_\Sigma,\qquad 0\le j\le5,\quad |h|\le1,
\]

where the numbers $\bar c_j$ have already been constructed, let
$\mathcal I_{D,s}=\{1,\ldots,D\}^s$ be the ordered derivative-index
strings and set

\[
 R^{(0)}_{j,s}
 =\bigoplus_{(i_1,\ldots,i_s)\in\mathcal I_{D,s}}
   \mathcal E(\partial_h^j\partial_{x_{i_1}}\cdots
   \partial_{x_{i_s}}\psi),
 \qquad j+\lceil s/2\rceil\le5.                              \tag{41}
\]

Recursively, whenever
$q+j+\lceil s/2\rceil<5$, set

\[
 R^{(q+1)}_{j,s}
 =R^{(q)}_{j+1,s}
 \oplus
 \bigoplus_{a=0}^j
 \left[
  \left(\frac12\binom ja\bar c_{a+1},0\right)
  \odot R^{(q)}_{j-a,s+2}
 \right].                                                    \tag{42}
\]

If $R^{(q)}_{0,0}=(A_q,p_q)$, define

\[
 \overline{\mathcal J}_q(N)
 =A_q\mu_{D,p_q}(\bar c_0).                                  \tag{43}
\]

Leibniz's rule applied to (40) gives exactly (42); induction therefore
proves

\[
 |N^{(q)}(h)|\le\overline{\mathcal J}_q(N),\qquad |h|\le1.    \tag{44}
\]

If a covariance entry is the previously compiled node $N_{ab}$, define

\[
 \bar c_j^{\rm new}=
 \sum_{a,b}\overline{\mathcal J}_j(N_{ab}).                 \tag{45}
\]

If a response is a previously compiled node $S$, put
$\bar S_j=\overline{\mathcal J}_j(S)$.  Finally, for
$L=S+hQ$, use the explicit rule

\[
 \bar L_j=\bar S_j+\bar Q_j+j\bar Q_{j-1},\qquad
 \bar Q_{-1}=0.                                             \tag{46}
\]

### 5.3 The seven chronological compiler calls

The following calls completely specify every number in (9)--(10).  In each
call, generate the scalar expressions exactly from equations (5.3)--(5.7)
of `WIDTH_DAG.md`, replace earlier scalar nodes by the tokens above, and
apply (41)--(46).

1. **First lower call.**  Use the Gaussian block
   $(U,\chi_0)$ with covariance
   $\operatorname{diag}(1,d^2)$.  Compile
   $H_0,H_1$, all $Q_{H,rs}$ for $r,s\le1$, and
   $\rho^W_{10}=\mathbb E\partial_{\chi_0}H_1$.  Construct
   $L^W_{10}=\rho^W_{10}+hQ_{H,01}$.

2. **First middle-forward call.**  Use
   $(\xi_0,\xi_1,\omega_0)$ with covariance
   $Q_H^{[1]}\oplus[d]$.  Recompute $z_0,z_1,G_0,G_1$, and compile
   all $Q_{G,rs}$, $r,s\le1$, together with
   $\rho^V_{10}=\mathbb E\partial_{\omega_0}G_1$.  Construct
   $L^V_{10}=\rho^V_{10}+hQ_{G,01}$.

3. **First top call.**  Use
   $(A,\zeta_0,\zeta_1)$ with covariance
   $[1]\oplus Q_G^{[1]}$.  Recompute $y_0,y_1,a_1,C_0,C_1$.  Compile
   $F_1=\mathbb E[a_1\phi(y_1)]$, all entries of $K_C^{[1]}$, and
   $\sigma^V_{1r}=\mathbb E\partial_{\zeta_r}C_1$, $r=0,1$.
   The time-zero response is identically zero.  Before the next call,
   define the full transpose coefficients
   $T^V_{10}=\sigma^V_{10}+hK_{C,01}$ and
   $T^V_{11}=\sigma^V_{11}$, compiling their derivative bounds with
   rule (46).

4. **First middle-backward call.**  Use
   $(\xi_0,\xi_1,\omega_0,\omega_1)$ with covariance
   $Q_H^{[1]}\oplus K_C^{[1]}$.  Recompute
   $z_0,z_1,G_0,G_1,d_0,d_1,E_0,E_1$.  Compile all entries of
   $K_E^{[1]}$ and
   $\sigma^W_{1r}=\mathbb E\partial_{\xi_r}E_1$, $r=0,1$.
   Before the next call, define
   $T^W_{10}=\sigma^W_{10}+hK_{E,01}$ and
   $T^W_{11}=\sigma^W_{11}$, again using rule (46).

5. **Second lower call.**  Use
   $(U,\chi_0,\chi_1)$ with covariance
   $[1]\oplus K_E^{[1]}$.  Recompute $u_0,u_1,u_2,H_0,H_1,H_2$.
   Compile $Q_{H,r2}$, $0\le r\le2$, and
   $\rho^W_{2r}=\mathbb E\partial_{\chi_r}H_2$, $r=0,1$.
   Construct $L^W_{2r}=\rho^W_{2r}+hQ_{H,r2}$.

6. **Second middle-forward call.**  Use
   $(\xi_0,\xi_1,\xi_2,\omega_0,\omega_1)$ with covariance
   $Q_H^{[2]}\oplus K_C^{[1]}$.  Recompute all fields through
   $G_2$.  Compile $Q_{G,r2}$, $0\le r\le2$, and
   $\rho^V_{2r}=\mathbb E\partial_{\omega_r}G_2$, $r=0,1$.
   Construct $L^V_{2r}=\rho^V_{2r}+hQ_{G,r2}$.

7. **Final top call.**  Use
   $(A,\zeta_0,\zeta_1,\zeta_2)$ with covariance
   $[1]\oplus Q_G^{[2]}$.  Recompute $y_0,y_1,y_2,a_2$ and compile
   $F_2=\mathbb E[a_2\phi(y_2)]$.

For clarity, the covariance derivative majorant supplied to each successive
call is, entry by entry,

\[
\begin{array}{c|c}
 \text{call}&\bar c_j\\ \hline
1&\mathbf1_{j=0}(1+d^2)\\
2&\displaystyle\sum_{r,s\le1}\bar Q_{H,rs,j}
       +\mathbf1_{j=0}d\\
3&\displaystyle\mathbf1_{j=0}
       +\sum_{r,s\le1}\bar Q_{G,rs,j}\\
4&\displaystyle\sum_{r,s\le1}
       (\bar Q_{H,rs,j}+\bar K_{C,rs,j})\\
5&\displaystyle\mathbf1_{j=0}
       +\sum_{r,s\le1}\bar K_{E,rs,j}\\
6&\displaystyle\sum_{r,s\le2}\bar Q_{H,rs,j}
       +\sum_{r,s\le1}\bar K_{C,rs,j}\\
7&\displaystyle\mathbf1_{j=0}
       +\sum_{r,s\le2}\bar Q_{G,rs,j}.
\end{array}                                                   \tag{47}
\]

This recursion is acyclic in the displayed order.  It has seven calls, each
uses a Gaussian dimension at most five, and the index set in (41)--(42) is
finite.  On that index set $j+s\le10$.  A response integrand begins with
an activation derivative of order at most two, and each formal derivative
raises the order of any one activation factor by at most one.  Consequently
no derivative above $\phi^{(12)}$ occurs.  Equations (38)--(47) therefore
terminate after finitely many sums and products and return finite numbers
depending only on $M_\phi$ and explicit Gaussian moments (39).  In
particular, neither (10) nor (14) contains a supremum of an output, a
trained trajectory, or an unspecified continuity modulus.

The domination produced by the same recursion verifies the hypotheses of
the singular Price constructor at every call.  Induction over the seven
calls proves that every Gram, response, $F_1$, and $F_2$ is $C^5$ on
$[-1,1]$, including at $h=0$.

## 6. Quantitative rank radius

There is an exact sign symmetry of the operator DAG.  Send

\[
 h\mapsto-h,\qquad A\mapsto-A,\qquad
 (\chi_0,\chi_1)\mapsto-(\chi_0,\chi_1),\qquad
 (\omega_0,\omega_1)\mapsto-(\omega_0,\omega_1).             \tag{48}
\]

The Gaussian laws are invariant.  Chronologically, $u_s,z_s,y_s$ and
$H_s,G_s$ remain unchanged, $C_s,E_s,b_s,d_s,a_s$ change sign,
all four Grams are unchanged, every response and every $L$-coefficient
changes sign, and each output changes sign.  This is checked first at time
zero and then in equations (5.3)--(5.6), one displayed line at a time.
Thus

\[
 Q_H,Q_G,K_C,K_E\ \text{are even in }h,\qquad
 F_1,F_2\ \text{are odd in }h.                              \tag{49}
\]

The determinants are therefore even.  Equations (8) and (49) imply

\[
\begin{aligned}
 (\det Q_H)''(0)&=2\nu_H,&
 (\det Q_G)''(0)&=2\nu_G,\\
 (\det K_C)''(0)&=2d\tau_C,&
 (\det K_E)''(0)&=2d^2\tau_E.                              \tag{50}
\end{aligned}
\]

Since the time-zero diagonal entries are constant,

\[
 \det Q_H=Q_{H,11}-Q_{H,01}^2,\quad
 \det Q_G=Q_{G,11}-Q_{G,01}^2,
\]

\[
 \det K_C=dK_{C,11}-K_{C,01}^2,\quad
 \det K_E=d^2K_{E,11}-K_{E,01}^2.                           \tag{51}
\]

Four differentiations and Leibniz's rule show that the respective absolute
fourth derivatives are bounded by the four quantities in (11).  Taylor's
formula through degree three, (49), and (50) therefore give, for a Gram
with leading coefficient $a$ and fourth-derivative bound $D$,

\[
 |\det\operatorname{Gram}(h)-ah^2|
 \le\frac D{24}|h|^4.                                      \tag{52}
\]

If $0<|h|\le R(a,D)$, the right side is at most
$ah^2/2$, because $D/(1+D)\le1$.  Hence

\[
 \det\operatorname{Gram}(h)\ge\frac12ah^2>0.               \tag{53}
\]

Applying (53) four times proves the rank assertion following (14).  If an
explicit inverse bound is wanted, define

\[
\begin{aligned}
 T_{Q_H}&=1+\bar Q_{H,11,0},&
 T_{Q_G}&=1+\bar Q_{G,11,0},\\
 T_{K_C}&=d+\bar K_{C,11,0},&
 T_{K_E}&=d^2+\bar K_{E,11,0}.
\end{aligned}
\]

A positive-semidefinite $2\times2$ matrix satisfies
$\lambda_{\min}\ge\det/\operatorname{tr}$.  Thus, at every fixed
nonzero $h$ in (13), each inverse used by the ten-action conditioning
argument has a strictly positive activation-defined bound, for example

\[
 \lambda_{\min}(Q_H(h))\ge\frac{\nu_Hh^2}{2T_{Q_H}},
 \qquad
 \lambda_{\min}(K_E(h))\ge\frac{d^2\tau_Eh^2}{2T_{K_E}},    \tag{54}
\]

with the analogous two bounds for $Q_G,K_C$.  These bounds may vanish as
$h\to0$, which is harmless: the finite-width identification is applied at
each fixed nonzero $h$ before the operator DAG is differentiated.

## 7. Fifth-order remainder

From (44) and the last two compiler calls,

\[
 |F_2^{(5)}(h)|\le\overline{\mathcal J}_{2,5},\qquad
 |F_1^{(5)}(h)|\le\overline{\mathcal J}_{1,5},\qquad |h|\le1.
\]

Therefore, for $|\eta|\le1/2$,

\[
 |\Delta_{21}^{(5)}(\eta)|
 \le\overline{\mathcal J}_{2,5}
    +2^5\overline{\mathcal J}_{1,5}=120B_\phi.              \tag{55}
\]

By (49), $\Delta_{21}$ is odd, so its zeroth, second, and fourth
derivatives vanish at zero.  The exact first- and third-order Price
calculations in `PROOF.md`, equations (5.25)--(5.26), supply (15).
Taylor's theorem with the continuous fifth derivative and (55) then gives
exactly (16).

Finally, (16) implies, for every $\varepsilon>0$,

\[
 |\Delta_{21}(\eta)|
 \le(|\kappa_\phi|+\varepsilon)|\eta|^3                    \tag{56}
\]

whenever

\[
 |\eta|\le
 \min\left\{h_\phi,
 \sqrt{\frac{\varepsilon}{1+B_\phi}}\right\}.              \tag{57}
\]

Indeed, (57) gives
$B_\phi|\eta|^2\le B_\phi\varepsilon/(1+B_\phi)\le
\varepsilon$, and (16) gives (56).
