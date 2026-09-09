## 14. Exact tangent geometry and a reached signed-Hessian obstruction

Sections 14.1–14.5 give a deterministic finite-width counterexample to a specific
pointwise matrix estimate. It uses the original three-hidden-layer arctangent
network with all blocks trained, one sample `d=m=1`, `x_1=y_1=1`, the full
loss \(\mathcal L_n=(f_n-1)^2\), and stored block mobilities \((n,1,1,n)\).
The constructed hidden initialization is correlated and deterministic. It is
not an independent Gaussian initialization or a typical-Gaussian obstruction.

The result separates two kinds of control. The first preactivation and
readout RMS and both hidden-matrix operator norms stay bounded on the whole
constructed trajectory segment. The complete Hessian is bounded in operator
norm at its terminal state. Its material derivative nevertheless has a
positive Rayleigh quotient growing linearly with width, even after subtracting
any fixed real multiple of the Hessian square. No bound on the Hessian along
the whole segment is assumed or established.

Sections 14.6–14.7 also prove a positive full tangent-volume bound, including
its expectation under the prescribed independent Gaussian initialization.
The exact hidden-projection formula identifies an additional angle factor;
the full-volume estimate alone does not bound that factor from below.

### 14.1 The metric, potential and exact statement

Let \(\phi(z)=\arctan z\), and retain the forward equations

\[
 h^{(\ell)}=\phi(z^{(\ell)}),\qquad
 z^{(2)}=W^{(2)}h^{(1)},\qquad z^{(3)}=W^{(3)}h^{(2)},\qquad
 f_n=\frac{c^Th^{(3)}}n,\quad c=W^{(4)}.
\]

The parameter coordinate used for all Hessians in this section is

\[
 \vartheta=(z^{(1)},\sqrt n W^{(2)},\sqrt nW^{(3)})
       \in\mathbb R^{N_h},\qquad N_h=n+2n^2,\qquad
 \Theta=(\vartheta,c)\in\mathbb R^{N_h+n}.             \tag{14.1}
\]

Matrix coordinates have their ordinary Frobenius metric; vector coordinates
have their ordinary Euclidean metric. Define the scalar potential
\(\mathscr F(\vartheta,c)=c^Th^{(3)}(\vartheta)=nf_n\),
\(J=D_\vartheta h^{(3)}\), and its Euclidean gradient and Hessian

\[
 b=\nabla_\Theta\mathscr F=(J^Tc,h^{(3)}),\qquad
 \mathsf B=Db=\begin{pmatrix}A&J^T\\J&0\end{pmatrix},
 \qquad A=D_\vartheta^2\mathscr F.                    \tag{14.2}
\]

Feature time \(s\) is defined by \(\Theta'=b\), where a prime denotes
\(d/ds\). In stored variables this is exactly

\[
 (z^{(1)})'=\delta^{(1)},\qquad
 (W^{(\ell)})'=\frac1n\delta^{(\ell)}(h^{(\ell-1)})^T
       \quad(\ell=2,3),\qquad c'=h^{(3)}.             \tag{14.3}
\]

Indeed the derivatives of \(\mathscr F\) with respect to
\(\sqrt nW^{(\ell)}\) are
\(\delta^{(\ell)}(h^{(\ell-1)})^T/\sqrt n\).
Thus (14.2) retains every trained block and the actual transpose.
It also gives

\[
 f_n'=\frac{\|b\|_2^2}{n}\ge0.                       \tag{14.4}
\]

Physical full-loss GF on a segment where \(f_n<1\) is the same curve
with \(ds/dt=\alpha=2(1-f_n)=-2r_n\). The counterexample below constructs
such a segment; feature time is not a change to the optimizer.

**Reachable signed-Hessian obstruction.** Fix any \(\beta,\gamma>0\).
There is \(\varepsilon_0>0\), depending only on these two constants, such
that for every fixed \(0<\varepsilon\le\varepsilon_0\) and every even
\(n\ge4\) there is a deterministic initial state with \(c(0)=0\) and a
feature time \(\tau_n\) satisfying

\[
 \frac{\varepsilon}{\pi/2}\le\tau_n\le
       \frac{\varepsilon}{h_*},\qquad h_*>0,           \tag{14.5}
\]

where \(h_*\) is independent of width. All four primal norms specified
above stay bounded independently of width on \([0,\tau_n]\). At its
terminal state \(\|\mathsf B\|_{\mathrm{op}}\le C\), and there is a
unit vector \(U_n\in\mathbb R^{N_h+n}\) such that, for every fixed
\(\kappa\in\mathbb R\),

\[
 U_n^T(\mathsf B'-\kappa\mathsf B^2)U_n
      \ge c_0\varepsilon^2 n-C_\kappa,\qquad c_0>0.   \tag{14.6}
\]

Here \(\mathsf B'=D\mathsf B[b]\) is the material derivative along the
full feature field, not a coordinatewise activation derivative. Constants
in (14.5)–(14.6) do not depend on width. The analogous conclusion holds for
the Jacobian of the full physical vector field and its physical material
derivative, as proved in Section 14.5.

The proof first gives the complete trained-block Hessian identities. It
then constructs a terminal state with a positive bulk feature and a
concentrated two-coordinate middle response, and integrates backward a
uniformly controlled short distance until the common readout is zero.

### 14.2 Complete Hessian and material derivative

Write \(D_\ell=\operatorname{diag}(\phi'(z^{(\ell)}))\), and define

\[
 \delta^{(3)}=D_3c,\quad q^{(2)}=(W^{(3)})^T\delta^{(3)},\quad
 \delta^{(2)}=D_2q^{(2)},\quad q^{(1)}=(W^{(2)})^T\delta^{(2)},\quad
 \delta^{(1)}=D_1q^{(1)}.
\]

For a fixed hidden tangent \(u=(u_1,E_2,E_3)\), where the matrices vary the
scaled coordinates in (14.1), let

\[
 \begin{aligned}
 T_1u&=u_1,\\
 T_2u&=E_2h^{(1)}/\sqrt n+W^{(2)}D_1u_1,\\
 T_3u&=E_3h^{(2)}/\sqrt n+W^{(3)}D_2T_2u,\\
 S_2u&=E_2^T\delta^{(2)}/\sqrt n,\qquad
 S_3u=E_3^T\delta^{(3)}/\sqrt n.
 \end{aligned}                                        \tag{14.7}
\]

These are linear maps from \(\mathbb R^{N_h}\) to \(\mathbb R^n\), and
\(J=D_3T_3\). Set

\[
 M_1=\operatorname{diag}(\phi''(z^{(1)})q^{(1)}),\quad
 M_2=\operatorname{diag}(\phi''(z^{(2)})q^{(2)}),\quad
 M_3=\operatorname{diag}(\phi''(z^{(3)})c),
\]

where the products inside the diagonals are coordinatewise. The full hidden
Hessian is determined by the quadratic form

\[
 u^TAu=\sum_{\ell=1}^3(T_\ell u)^TM_\ell T_\ell u
       +2(S_2u)^TD_1T_1u+2(S_3u)^TD_2T_2u.            \tag{14.8}
\]

For verification, the first variation of \(z^{(\ell)}\) is \(T_\ell u\).
Along the straight parameter line \(\vartheta+\lambda u\), the second variations
of the two upper preactivations at \(\lambda=0\) are

\[
 \begin{aligned}
 \partial_\lambda^2 z^{(2)}
  &=2E_2D_1u_1/\sqrt n
      +W^{(2)}\{\phi''(z^{(1)})\odot u_1^{\odot2}\},\\
 \partial_\lambda^2 z^{(3)}
  &=2E_3D_2T_2u/\sqrt n
      +W^{(3)}\{\phi''(z^{(2)})\odot(T_2u)^{\odot2}
                     +D_2\partial_\lambda^2z^{(2)}\}.
 \end{aligned}
\]

Differentiating the final activation twice and pairing with \(c\) gives
(14.8), including both mixed matrix terms. Polarization determines the
symmetric operator \(A\) from this quadratic form.

For its material derivative put \(\nu_\ell=(z^{(\ell)})'\). Equations
(14.3) give the exact identities

\[
 \begin{aligned}
 \nu_1&=\delta^{(1)},\\
 \nu_2&=\frac{\|h^{(1)}\|_2^2}{n}\delta^{(2)}
                            +W^{(2)}D_1\nu_1,\\
 \nu_3&=\frac{\|h^{(2)}\|_2^2}{n}\delta^{(3)}
                            +W^{(3)}D_2\nu_2,\\
 D_\ell'&=\operatorname{diag}(\phi''(z^{(\ell)})\nu_\ell),\\
 (\delta^{(3)})'&=D_3'c+D_3h^{(3)},\\
 (q^{(2)})'&=((W^{(3)})')^T\delta^{(3)}
                              +(W^{(3)})^T(\delta^{(3)})',\\
 (\delta^{(2)})'&=D_2'q^{(2)}+D_2(q^{(2)})',\\
 (q^{(1)})'&=((W^{(2)})')^T\delta^{(2)}
                              +(W^{(2)})^T(\delta^{(2)})'.
 \end{aligned}                                        \tag{14.9}
\]

For the same fixed tangent \(u\), differentiating (14.7) gives

\[
 \begin{aligned}
 T_1'&=0,\\
 T_2'u&=E_2D_1\nu_1/\sqrt n
           +(W^{(2)})'D_1u_1+W^{(2)}D_1'u_1,\\
 T_3'u&=E_3D_2\nu_2/\sqrt n+(W^{(3)})'D_2T_2u
           +W^{(3)}D_2'T_2u+W^{(3)}D_2T_2'u,\\
 S_2'u&=E_2^T(\delta^{(2)})'/\sqrt n,\qquad
 S_3'u=E_3^T(\delta^{(3)})'/\sqrt n,\\
 J'&=D_3'T_3+D_3T_3'.
 \end{aligned}                                        \tag{14.10}
\]

The diagonal derivatives are

\[
 \begin{aligned}
 M_1'&=\operatorname{diag}\{
       \phi'''(z^{(1)})\nu_1q^{(1)}+\phi''(z^{(1)})(q^{(1)})'\},\\
 M_2'&=\operatorname{diag}\{
       \phi'''(z^{(2)})\nu_2q^{(2)}+\phi''(z^{(2)})(q^{(2)})'\},\\
 M_3'&=\operatorname{diag}\{
       \phi'''(z^{(3)})\nu_3c+\phi''(z^{(3)})h^{(3)}\}.
 \end{aligned}                                        \tag{14.11}
\]

Products in (14.11) are again coordinatewise. Differentiating (14.8),
with \(u\) fixed, is consequently the complete formula

\[
 \begin{aligned}
 u^TA'u={}&\sum_{\ell=1}^3\left\{
       2(T_\ell'u)^TM_\ell T_\ell u+(T_\ell u)^TM_\ell'T_\ell u\right\}\\
 &+2(S_2'u)^TD_1T_1u+2(S_2u)^TD_1'T_1u\\
 &+2(S_3'u)^TD_2T_2u+2(S_3u)^TD_2'T_2u
                              +2(S_3u)^TD_2T_2'u.
 \end{aligned}                                        \tag{14.12}
\]

There is no omitted derivative of a trained transpose or readout. In
particular \(\mathsf B'=\left(\begin{smallmatrix}A'&(J')^T\\J'&0\end{smallmatrix}\right)\),
and for a full tangent \(U=(u,\xi)\), with \(\xi\in\mathbb R^n\),

\[
 \begin{aligned}
 U^T(\mathsf B'-\kappa\mathsf B^2)U
  =u^TA'u+2\xi^TJ'u
       -\kappa\left(\|Au+J^T\xi\|_2^2+\|Ju\|_2^2\right).
 \end{aligned}                                        \tag{14.13}
\]

### 14.3 The terminal state and its positive Rayleigh quotient

Let \(\mathbf1\in\mathbb R^n\) be the all-ones vector, and choose a
balanced unit vector \(e\) with entries \(\pm1/\sqrt n\), so that
\(e^T\mathbf1=0\). Let \(e_1,e_2\) be the first two coordinate vectors.
Define

\[
 a_0=\pi/4,\quad \mu=a_0^2<1,\quad \rho=(n-2)/n,\quad
 w=e_1+e_2,\quad v=e_1-2e_2,\quad g=\mathbf1-e_1-e_2.
\]

For fixed \(\beta,\gamma,\varepsilon>0\), prescribe the terminal state

\[
 \begin{aligned}
 z^{(1)}&=\mathbf1,\qquad c=\varepsilon\mathbf1,\\
 W^{(2)}&=2we^T+\frac{\beta}{a_0n}g\mathbf1^T,\\
 W^{(3)}&=\frac{\mathbf1v^T}{\sqrt n}
                               +\frac\gamma n\mathbf1g^T.
 \end{aligned}                                        \tag{14.14}
\]

The ranges and domains of the two summands of \(W^{(2)}\) are orthogonal.
Also \(v^Tg=0\), \(\|v\|_2^2=5\), and \(\|g\|_2^2=n\rho\). Hence

\[
 \|W^{(2)}\|_{\mathrm{op}}
       =\max\{2\sqrt2,\beta\sqrt\rho/a_0\},\qquad
 \|W^{(3)}\|_{\mathrm{op}}=\sqrt{5+\gamma^2\rho},
\]

while \(\|z^{(1)}\|_2/\sqrt n=1\) and \(\|c\|_2/\sqrt n=\varepsilon\).
Introduce the following scalars, used only in this construction:

\[
 \begin{aligned}
 t_\beta&=\phi(\beta),\quad d_\beta=\phi'(\beta),\quad
 Z=\gamma\rho t_\beta,\quad H=\phi(Z),\quad D=\phi'(Z),
       \quad k=\varepsilon D,\\
 \Lambda&=\beta\gamma d_\beta\rho/a_0,\\
 R_\beta&=\gamma d_\beta\left(\mu+
                                  \frac{\beta^2\rho}{4a_0^2}\right),\\
 Q_\beta&=\rho t_\beta^2+5\mu+1+\gamma\rho d_\beta R_\beta.
 \end{aligned}
\]

The complete forward and backward quantities at (14.14) are

\[
 \begin{aligned}
 h^{(1)}&=a_0\mathbf1,\quad z^{(2)}=\beta g,\quad
 h^{(2)}=t_\beta g,\quad z^{(3)}=Z\mathbf1,\quad h^{(3)}=H\mathbf1,\\
 f_n&=\varepsilon H,\qquad \delta^{(3)}=k\mathbf1,\\
 q^{(2)}&=\sqrt n k v+\gamma k g,\qquad
 \delta^{(2)}=\sqrt n k v+\gamma d_\beta k g,\\
 q^{(1)}&=-2\sqrt n k e+\Lambda k\mathbf1,\\
 \nu_1&=-\sqrt n k e+(\Lambda k/2)\mathbf1,\\
 \nu_2&=\sqrt n k(\mu v-w)+kR_\beta g,\qquad
 \nu_3=kQ_\beta\mathbf1.
 \end{aligned}                                        \tag{14.15}
\]

These identities follow by matrix multiplication and (14.9). In particular
\(D_1=I/2\), and

\[
 \nu_2=\left\{\mu I+W^{(2)}D_1^2(W^{(2)})^T\right\}\delta^{(2)}.
\]

Its first two coordinates see the block \(\mu I+ww^T\); the bulk cross
terms vanish by the orthogonalities just stated. This gives its rare part
\(\sqrt n k(\mu v-w)\). The bulk term is
\(k(\mu\gamma d_\beta+\beta\Lambda/(4a_0))g=kR_\beta g\).
Substituting into \(\nu_3\) gives \(Q_\beta\), because
\(v^T(\mu v-w)=5\mu+1\).

The Hessian itself is uniformly bounded at this state. Indeed,
\(\phi''(1)=-1/2\), \(\phi''(0)=0\), and (14.15) give

\[
 \|M_1\|_{\mathrm{op}}\le |k|(1+\Lambda/2),\quad
 \|M_2\|_{\mathrm{op}}\le |\phi''(\beta)|\gamma|k|,\quad
 \|M_3\|_{\mathrm{op}}\le\varepsilon|\phi''(Z)|.       \tag{14.16}
\]

For \(P=\pi/2\), the bounds \(|\phi|\le P\), \(|\phi'|\le1\) imply
from (14.7) that

\[
 \|T_1\|_{\mathrm{op}}\le1,\quad
 \|T_2\|_{\mathrm{op}}\le P+\|W^{(2)}\|_{\mathrm{op}},\quad
 \|T_3\|_{\mathrm{op}}
        \le P+\|W^{(3)}\|_{\mathrm{op}}\|T_2\|_{\mathrm{op}},
 \quad\|J\|_{\mathrm{op}}\le\|T_3\|_{\mathrm{op}}.
\]

Also
\(\|S_2\|_{\mathrm{op}}\le\|\delta^{(2)}\|_2/\sqrt n
\le\|W^{(3)}\|_{\mathrm{op}}\varepsilon\) and
\(\|S_3\|_{\mathrm{op}}\le\varepsilon\).
For a symmetric matrix \(A\), its operator norm is the supremum of
\(|u^TAu|\) over unit \(u\). Thus (14.8) and (14.16) bound \(A\), and
(14.2) bounds \(\mathsf B\), independently of width. Furthermore,

\[
 \frac{\|b\|_2^2}{n}\le
       \|J\|_{\mathrm{op}}^2\varepsilon^2+P^2.         \tag{14.17}
\]

Now take the unit hidden tangent and full tangent

\[
 u_1=0,\qquad E_2=e_1\mathbf1^T/\sqrt n,\qquad E_3=0,
 \qquad U_n=(u,0).
\]

Its matrix Frobenius norm is one. Equations (14.7), (14.10), and balance
of \(e\) give

\[
 T_1u=0,\quad T_2u=a_0e_1,\quad T_2'u=(\Lambda k/4)e_1,
 \quad T_3u=\frac{a_0}{\sqrt n}\mathbf1,
 \quad T_3'u=\frac{\Lambda k}{4\sqrt n}\mathbf1.       \tag{14.18}
\]

For the last derivative, the trained term \((W^{(3)})'D_2T_2u\) vanishes
because \(h^{(2)}=t_\beta g\) has first coordinate zero. The term
\(W^{(3)}D_2'T_2u\) vanishes because \(\phi''(z_1^{(2)})=\phi''(0)=0\).
The remaining \(W^{(3)}D_2T_2'u\) gives the displayed value. Thus the
third matrix has been differentiated, not frozen.

In (14.12), the bottom terms and every \(S_2\) term contain \(T_1u=0\).
Both \(S_3u\) and \(S_3'u\) vanish since \(E_3=0\). The cross term with
\(T_2'\) and \(M_2\) vanishes since \(M_2e_1=0\). Finally,
\(\phi'''(0)=-2\) and (14.11), (14.15) give

\[
 (M_2')_{11}=2(1-\mu)n k^2,\qquad
 M_3'=\{\phi'''(Z)\varepsilon kQ_\beta+\phi''(Z)H\}I.
\]

Substitution of all remaining terms yields the exact full-field identity

\[
 \begin{aligned}
 U_n^T\mathsf B'U_n
   ={}&2\mu(1-\mu)n k^2
      +\mu\{\phi'''(Z)\varepsilon kQ_\beta+\phi''(Z)H\}\\
      &+(a_0\Lambda/2)\varepsilon k\phi''(Z).
 \end{aligned}                                        \tag{14.19}
\]

All terms after the first are bounded independently of width, since
\(\rho\in[1/2,1)\) and \(\beta,\gamma,\varepsilon\) are fixed. Moreover

\[
 D\ge D_*:=\frac1{1+\{\gamma\phi(\beta)\}^2}>0.
\]

The Hessian bound gives
\(U_n^T\mathsf B^2U_n=\|\mathsf BU_n\|_2^2\le C^2\).
Equation (14.6) follows from (14.19) with
\(c_0=2\mu(1-\mu)D_*^2>0\), for every fixed real \(\kappa\).

This also explains why a scalar arctangent sign is insufficient. Direct
substitution of
\(\phi'=1/(1+z^2)\), \(\phi''=-2z/(1+z^2)^2\), and
\(\phi'''=(6z^2-2)/(1+z^2)^3\) gives the negative scalar identity
\(\phi'''\phi'-(3/2)(\phi'')^2=-2(\phi')^4\).
But the positive-semidefinite middle mobility in (14.15) has off-diagonal
entries. Here \(\nu_{2,1}q_1^{(2)}=(\mu-1)nk^2<0\). At the same
coordinate \(M_2\) vanishes, while \(M_2'\) is positive of order \(n\).
The complete calculation (14.19) shows that the other trained blocks and
\(\mathsf B^2\) do not supply a compensating order-\(n\) term.

### 14.4 Uniform backward passage to exactly zero readout

It remains to make (14.14) a reached state. Its third-matrix rows are
identical and its readout coordinates are equal. The subspace

\[
 W^{(3)}=\mathbf1p^T,\qquad c=\chi\mathbf1
\]

is invariant in both feature-time directions: with
\(y=p^Th^{(2)}\), equations (14.3) become

\[
 z^{(3)}=y\mathbf1,\qquad
 (W^{(3)})'=\frac{\chi\phi'(y)}n\mathbf1(h^{(2)})^T,
 \qquad \chi'=\phi(y).                                \tag{14.20}
\]

The full finite vector field is smooth. Local uniqueness ensures that its
solutions starting in this invariant subspace agree with the restricted
solutions in either time direction.

Choose constants independent of width:

\[
 \begin{aligned}
 K_{2,0}&=\max\{2\sqrt2,\beta/a_0\},\quad
 K_{3,0}=\sqrt{5+\gamma^2},\quad
 N_2=K_{2,0}+1,\quad N_3=K_{3,0}+1,\\
 K&=P^2+N_3^2(P^2+N_2^2),\quad
 y_*=\gamma\phi(\beta)/2,\quad h_*=\phi(y_*/2)>0,\\
 \varepsilon_0&=\min\left\{1,\frac1{4P},
       \sqrt{\frac{h_*}{4PN_3}},
       \sqrt{\frac{y_*h_*}{4K}}\right\},\qquad P=\pi/2.
 \end{aligned}                                        \tag{14.21}
\]

On an interval where \(\|W^{(2)}\|_{\mathrm{op}}\le N_2\),
\(\|W^{(3)}\|_{\mathrm{op}}\le N_3\), and \(0\le\chi\le\varepsilon\),
the exact forward/backward formulas give

\[
 \begin{aligned}
 \|\delta^{(3)}\|_2/\sqrt n&\le\chi,&
 \|\delta^{(2)}\|_2/\sqrt n&\le N_3\chi,&
 \|\delta^{(1)}\|_2/\sqrt n&\le N_2N_3\chi,\\
 \|(W^{(3)})'\|_{\mathrm{op}}&\le P\chi,&
 \|(W^{(2)})'\|_{\mathrm{op}}&\le PN_3\chi,\\
 \|\nu_2\|_2/\sqrt n&\le(P^2+N_2^2)N_3\chi,&
 |y'|=\|\nu_3\|_2/\sqrt n&\le K\chi.
 \end{aligned}                                        \tag{14.22}
\]

The matrix inequalities follow by the rank-one norm formula. For \(\nu_2\)
and \(\nu_3\), substitute the first line and \(\|h^{(\ell)}\|_2/\sqrt n\le P\)
into (14.9). The last equality holds since all coordinates of \(z^{(3)}\)
are the same. No Hessian bound is used in (14.22).

Start at (14.14), assign it feature time zero temporarily, and integrate
backward with elapsed time \(\sigma\ge0\). Before the first zero of \(\chi\),
consider the conditions

\[
 0<\chi\le\varepsilon,\quad y\ge y_*/2,\quad
 \|W^{(2)}\|_{\mathrm{op}}<N_2,\quad
 \|W^{(3)}\|_{\mathrm{op}}<N_3,\quad \sigma\le\varepsilon/h_*.
\]

Initially \(y=Z\ge y_*\), since \(\rho\ge1/2\), and both matrix bounds
have margin at least one. While these conditions hold, (14.20) gives
\(d\chi/d\sigma=-\phi(y)\le-h_*\), so \(\chi\) cannot cross its upper
boundary. Integrating (14.22) and using (14.21) gives

\[
 \begin{aligned}
 \|W^{(3)}(\sigma)-W^{(3)}(0)\|_{\mathrm{op}}
       &\le P\varepsilon^2/h_*\le1/4,\\
 \|W^{(2)}(\sigma)-W^{(2)}(0)\|_{\mathrm{op}}
       &\le PN_3\varepsilon^2/h_*\le1/4,\\
 |y(\sigma)-y(0)|&\le K\varepsilon^2/h_*\le y_*/4,\\
 \|z^{(1)}(\sigma)-z^{(1)}(0)\|_2/\sqrt n
       &\le N_2N_3\varepsilon^2/h_*.
 \end{aligned}                                        \tag{14.23}
\]

Thus neither a matrix boundary nor the lower \(y\) boundary can be reached.
For each fixed width the same bounds preclude finite-time escape in all
parameter coordinates: the vector Euclidean norms are bounded, and a matrix
operator bound implies a Frobenius bound at most \(\sqrt n\) times as
large. A smooth finite-dimensional ODE extends while its state remains in
a bounded set, because on a slightly larger closed ball its field is bounded
and Lipschitz, so the integral equation has a local continuation at any
finite limiting endpoint. Hence the backward solution extends until
\(\chi=0\) or \(\sigma=\varepsilon/h_*\). The latter cannot occur first with
\(\chi>0\), since integration of \(d\chi/d\sigma\le-h_*\) would give
\(\chi\le0\) there. The first zero occurs at some
\(\tau_n\le\varepsilon/h_*\). Since \(|d\chi/d\sigma|\le P\), it also
satisfies \(\tau_n\ge\varepsilon/P\).

Declare this zero-readout endpoint to be feature time zero and run the
same smooth solution forward. It reaches (14.14) at \(\tau_n\).
Equations (14.22)–(14.23) prove the claimed whole-segment primal bounds.
The initial hidden weights are obtained by this deterministic inverse
flow; no distributional identification with independent Gaussian weights
is made.

### 14.5 Physical time and the exact scope of the obstruction

By (14.4), the predictor increases from zero to \(\varepsilon H\) along
the constructed segment. The choice (14.21) gives

\[
 0\le f_n\le\varepsilon H\le\varepsilon P\le1/4.
\]

Therefore \(\alpha=2(1-f_n)\in[3/2,2]\), and the same curve is a full
physical-loss GF trajectory with terminal time \(t_n\) satisfying
\(\tau_n/2\le t_n\le2\tau_n/3\). Both feature and physical terminal
times lie in fixed positive compact intervals when \(\varepsilon\) is
fixed, but need not be identical at different widths.

The physical vector field in coordinates (14.1) is \(\mathcal V=\alpha b\).
Since \(\nabla_\Theta f_n=b/n\), its complete Jacobian is the symmetric
matrix

\[
 \mathsf C=D\mathcal V=\alpha\mathsf B-\frac2n bb^T.
\]

A dot now denotes the physical material derivative. Using
\(\dot\alpha=-2\alpha\|b\|_2^2/n\),
\(\dot b=\alpha\mathsf Bb\), and \(\dot{\mathsf B}=\alpha\mathsf B'\),
exact differentiation gives

\[
 \dot{\mathsf C}=\alpha^2\mathsf B'
   -\frac{2\alpha}{n}\|b\|_2^2\mathsf B
   -\frac{2\alpha}{n}\{(\mathsf Bb)b^T+b(\mathsf Bb)^T\}. \tag{14.24}
\]

At the terminal state, \(\|\mathsf B\|_{\mathrm{op}}\) and
\(\|b\|_2/\sqrt n\) are bounded by (14.16)–(14.17). The two correction
terms in (14.24) thus have bounded operator norm. The same holds for
\(\mathsf C\) and \(\mathsf C^2\). Applying (14.19) to the same unit
vector and using \(\alpha\ge3/2\) gives, for every fixed real \(\kappa\),

\[
 U_n^T(\dot{\mathsf C}-\kappa\mathsf C^2)U_n
    \ge\frac94c_0\varepsilon^2 n-C_\kappa'
      \longrightarrow+\infty.                         \tag{14.25}
\]

This disproves a width-independent upper bound for either signed matrix
in (14.6) or (14.25) inferred only from the stated primal bounds, even
on trajectories begun at exactly zero readout. The residual-clock terms
are fully included. It does not disprove a bound that assumes additional
Hessian-history or response information, a Gaussian-typical estimate, or
an integrated-in-time signed estimate. No probability lower bound under
the prescribed independent Gaussian initialization, no fixed-time
convergence failure, and no failure of the nonlinear population limit
are consequences of this deterministic construction.

### 14.6 Positive intrinsic-volume bounds for the full trained flow

There is also a positive uniform statement for transported tangent volumes.
It concerns the full Hessian \(\mathsf B\), rather than its signed material
derivative. The same arctangent architecture, coordinates (14.1), potential
and full-loss clock are used throughout. The deterministic bounds first allow
arbitrary finite initial parameters. The expectation conclusions then use the
specified independent Gaussian initialization

\[
 z_j^{(1)}(0)\sim N(0,1),\quad
 W_{ij}^{(2)}(0),W_{ij}^{(3)}(0)\sim N(0,1/n),\quad
 c_i(0)\sim N(0,n^{-2}).                              \tag{14.26}
\]

Here the stored readout is small, unlike the deterministic terminal witness
in Section 14.3. No Gaussian hypothesis is imposed on the evolved state.

We prove global existence in both feature-time directions and give an
explicit polynomial bound

\[
 \sup_{|s|\le S}\|\mathsf B(s)\|_*
      \le n\,\mathcal P_S(M,R_0),\qquad
 M=\max_{\ell=2,3}\|W^{(\ell)}(0)\|_{\mathrm{op}},\quad
 R_0=\|c(0)\|_2/\sqrt n,                              \tag{14.27}
\]

where \(\|\cdot\|_*\) is the nuclear norm, the sum of singular values.
For every full-column-rank tangent response
\(\mathcal T(s)\in\mathbb R^{(N_h+n)\times q}\),
\(1\le q\le N_h+n\), satisfying \(\mathcal T'=\mathsf B\mathcal T\),
let

\[
 V_{\mathcal T}(s)=\sqrt{\det(\mathcal T(s)^T\mathcal T(s))}.
\]

It remains positive, and simultaneously for every such initial tangent plane
and every \(|s|\le S\),

\[
 \left|\log\frac{V_{\mathcal T}(s)}{V_{\mathcal T}(0)}\right|
       \le n|s|\mathcal P_S(M,R_0).                   \tag{14.28}
\]

Under (14.26), this implies
\(\mathbb E\sup_{|s|\le S}|\log(V_{\mathcal T}(s)/V_{\mathcal T}(0))|
\le C_S n\). The analogous full physical tangent response has expected
absolute log-volume change at most \(C_Tn\), uniformly over \([0,T]\).
The constants are independent of width and tangent dimension. Initial
tangent planes may depend measurably on the initial parameters, since the
underlying bounds are pathwise and simultaneous.

**Primal bounds and complete finite flow.** Put \(P=\pi/2\). For
\(u\ge0\), define the nonnegative polynomials

\[
 \begin{aligned}
 R(u)&=R_0+Pu,\\
 K_3(u)&=M+PR_0u+P^2u^2/2,\\
 K_2(u)&=M+P\int_0^u K_3(v)R(v)\,dv.
 \end{aligned}                                        \tag{14.29}
\]

The integral in the last line is a polynomial in \(u,M,R_0\), since its
integrand is a product of the two displayed polynomials. For either sign
of feature time, integrating (14.3) with absolute values gives

\[
 \|c(s)\|_2/\sqrt n\le R(|s|),\qquad
 \|W^{(3)}(s)\|_{\mathrm{op}}\le K_3(|s|),\qquad
 \|W^{(2)}(s)\|_{\mathrm{op}}\le K_2(|s|).             \tag{14.30}
\]

Indeed \(\|c'\|_2/\sqrt n\le P\),
\(\|(W^{(3)})'\|_{\mathrm{op}}\le P\|c\|_2/\sqrt n\), and
\(\|(W^{(2)})'\|_{\mathrm{op}}
\le P\|W^{(3)}\|_{\mathrm{op}}\|c\|_2/\sqrt n\).
These follow from \(|\phi'|\le1\) and the rank-one norm formula. Likewise,

\[
 \frac{\|z^{(1)}(s)\|_2}{\sqrt n}
 \le\frac{\|z^{(1)}(0)\|_2}{\sqrt n}
       +\int_0^{|s|}K_2(v)K_3(v)R(v)\,dv.             \tag{14.31}
\]

At each fixed width these estimates bound every Euclidean parameter
coordinate on every bounded feature-time interval. The smooth vector field
therefore continues in both directions by the bounded-state argument used
in Section 14.4. Denote its complete flow by \(\Phi_s\). Uniqueness gives
\(\Phi_{-s}\Phi_s=I\).

Smooth dependence on initial data follows by differentiating the integral
equation on bounded parameter sets: difference quotients satisfy the linear
variational integral equation plus a remainder tending to zero uniformly,
because the field has a continuous derivative on the relevant compact set.
The integral inequality \(e(t)\le a+L\int_0^t e(v)\,dv\) gives
\(e(t)\le ae^{Lt}\), by iteration of its integral operator, and removes
that remainder. Higher derivatives follow by differentiating the same
finite-dimensional equation repeatedly. Thus \(\Phi_s\) is smooth, with
invertible full derivative. One may check the latter directly: if
\(Y'=\mathsf BY\), \(Y(0)=I\), and \(Z'=-Z\mathsf B\), \(Z(0)=I\),
then \((ZY)'=0\), so \(ZY=I\). All these linear equations have continuous
coefficients on the bounded trajectory interval.

**Elementary nuclear inequalities.** For a finite matrix
\(H=\sum_i\sigma_i u_iv_i^T\) in a singular-value decomposition,

\[
 |\operatorname{Tr}(Q^TH)|\le\|Q\|_{\mathrm{op}}\sum_i\sigma_i.
\]

Taking \(Q=\sum_i u_iv_i^T\) shows that the supremum over
\(\|Q\|_{\mathrm{op}}\le1\) equals \(\|H\|_*\). This dual formula
proves the nuclear triangle inequality. It also gives
\(\|H\|_*\le\operatorname{rank}(H)\|H\|_{\mathrm{op}}\).
A rank-one matrix \(uv^T\) has nuclear norm \(\|u\|_2\|v\|_2\), so
decomposing a diagonal matrix into coordinate rank-one matrices gives

\[
 \|T^T\operatorname{diag}(d)T\|_*
     \le\|T\|_{\mathrm{op}}^2\sum_i|d_i|.             \tag{14.32}
\]

For any orthogonal projector \(\Pi\), the trace inequality also gives
\(|\operatorname{Tr}(\Pi H)|\le\|H\|_*\).

To apply these facts to the complete Hessian (14.8), fix \(S\ge0\) and
write \(R=R(S)\), \(K_2=K_2(S)\), \(K_3=K_3(S)\). Let

\[
 t_2=P+K_2,\qquad t_3=P+K_3t_2.
\]

On \(|s|\le S\), (14.7) gives
\(\|T_1\|_{\mathrm{op}}\le1\),
\(\|T_2\|_{\mathrm{op}}\le t_2\),
\(\|T_3\|_{\mathrm{op}},\|J\|_{\mathrm{op}}\le t_3\),
\(\|S_2\|_{\mathrm{op}}\le K_3R\), and
\(\|S_3\|_{\mathrm{op}}\le R\).
The backward fields satisfy

\[
 \|q^{(1)}\|_2/\sqrt n\le K_2K_3R,\qquad
 \|q^{(2)}\|_2/\sqrt n\le K_3R.
\]

Since \(|\phi''|\le2\), the sums of absolute diagonal entries of
\(M_1,M_2,M_3\) are bounded by
\(2nK_2K_3R,2nK_3R,2nR\), respectively. This uses only
\(\sum_i|v_i|\le\sqrt n\|v\|_2\), not a maximum coordinate bound.
Each symmetric mixed operator in (14.8) has rank at most \(2n\) and
operator norm at most twice the product of its two map norms. Thus

\[
 \|A\|_*\le2nR(K_2K_3+t_2^2K_3+t_3^2)
                       +4nR(K_3+t_2).
\]

The off-diagonal block
\(\left(\begin{smallmatrix}0&J^T\\J&0\end{smallmatrix}\right)\)
has rank at most \(2n\) and operator norm at most \(t_3\). Adding its
nuclear norm to that of \(\operatorname{diag}(A,0)\) proves (14.27) with

\[
 \mathcal P_S(M,R_0)
 =2R(K_2K_3+t_2^2K_3+t_3^2)+4R(K_3+t_2)+2t_3.        \tag{14.33}
\]

This is an explicit polynomial with nonnegative coefficients in \(S,M,R_0\).
In particular \(|\operatorname{Tr}\mathsf B|\le n\mathcal P_S\), while
no width-independent operator bound on \(\mathsf B\) is inferred.
The same estimates yield the additional useful bound

\[
 \frac{\|b\|_2^2}{n}\le\mathcal Q_S(M,R_0)
           :=t_3^2R^2+P^2.                            \tag{14.34}
\]

**Tangent volumes.** Write \(\mathcal T(s)=Y(s)\mathcal T(0)\), using
the invertible full derivative just proved. Thus its Gram matrix is positive
definite for all finite times. For any differentiable invertible matrix
\(G(s)\), multilinearity of the determinant gives
\(\det(I+hH)=1+h\operatorname{Tr}H+O(h^2)\), and consequently
\((\log\det G)'=\operatorname{Tr}(G^{-1}G')\) when \(G\) is positive
definite. Applying this identity to \(\mathcal T^T\mathcal T\), using
symmetry of \(\mathsf B\), gives

\[
 \frac{d}{ds}\log V_{\mathcal T}
   =\operatorname{Tr}(\Pi_{\mathcal T}\mathsf B),\qquad
 \Pi_{\mathcal T}=\mathcal T(\mathcal T^T\mathcal T)^{-1}\mathcal T^T.
                                                               \tag{14.35}
\]

The displayed \(\Pi_{\mathcal T}\) is the orthogonal projector onto the
current tangent range: it is symmetric, squares to itself, and fixes that
range. The nuclear trace bound therefore implies
\(|(\log V_{\mathcal T})'|\le n\mathcal P_S\). Integration in either
time direction proves (14.28).

**Gaussian expectations.** We supply the moment estimates needed to take
expectations of the polynomial in (14.33). A maximal \(1/4\)-separated
set on the unit sphere of \(\mathbb R^n\) is a \(1/4\)-net of at most
\(9^n\) points: disjoint radius-\(1/8\) balls about its points lie in the
radius-\(9/8\) ball, and comparison of volumes gives the cardinality.
For a matrix \(W\) with independent \(N(0,1/n)\) entries, each fixed
bilinear form \(y^TWx\) at unit vectors has law \(N(0,1/n)\). Completing
the square gives \(\mathbb E e^{t y^TWx}=e^{t^2/(2n)}\); exponential
Markov with \(t=na\) for each sign gives
\(\Pr\{|y^TWx|>a\}\le2e^{-na^2/2}\). Approximating a maximizing pair
of vectors by the two nets gives
\(\|W\|_{\mathrm{op}}\le2\max_{x,y\text{ in the net}}|y^TWx|\).
The union bound therefore yields

\[
 \Pr\{\|W\|_{\mathrm{op}}>u\}
     \le2\,81^n e^{-nu^2/8}\le2e^{-u^2/16}
       \qquad(u\ge10).                               \tag{14.36}
\]

For the last inequality, \(\log81<5\le u^2/16\) and \(n\ge1\).
Integrating this tail gives, for every fixed \(p>0\),

\[
 \mathbb E\|W\|_{\mathrm{op}}^p
    \le10^p+2p\int_{10}^\infty u^{p-1}e^{-u^2/16}\,du<\infty,
\]

uniformly in width. A union bound treats the maximum of the two initial
hidden norms \(M\).

For independent standard Gaussians \(g_i\), put
\(R_n^{\mathrm{std}}=(n^{-1}\sum_i g_i^2)^{1/2}\). If \(p\ge2\), convexity gives
\(\mathbb E(R_n^{\mathrm{std}})^p\le\mathbb E|g_1|^p\); if \(0<p<2\), concavity gives
\(\mathbb E(R_n^{\mathrm{std}})^p\le\{\mathbb E(R_n^{\mathrm{std}})^2\}^{p/2}=1\).
These Gaussian moments
are finite by their density integral. Under (14.26),
\(R_0\) has law \(R_n^{\mathrm{std}}/n\), so

\[
 \mathbb ER_0^p\le C_pn^{-p},\qquad
 \mathbb E(\|z^{(1)}(0)\|_2/\sqrt n)^p\le C_p.       \tag{14.37}
\]

Hölder's inequality bounds every mixed monomial in \(M,R_0\) by their
higher moments; hence \(\mathbb E\mathcal P_S(M,R_0)\le C_S\).
Equations (14.28) and (14.33) prove the stated expected intrinsic-volume
bound, also with the supremum over \(|s|\le S\).

**Forward physical time.** The argument must retain the residual clock even
when the initial residual has either sign. A local physical trajectory has
\(\dot\Theta=\alpha b\), \(\alpha=2(1-f_n)\), and

\[
 \dot r_n=-2r_n\frac{\|b\|_2^2}{n}.
\]

Solving this scalar linear equation along the existing trajectory gives
\(|r_n(t)|\le|r_n(0)|\le1+PR_0\). The physical path therefore equals
\(\Phi_{s(t)}(\Theta(0))\), where its signed feature clock satisfies

\[
 |\alpha(t)|\le2(1+PR_0),\qquad
 \int_0^T|\alpha(t)|\,dt\le S_T:=2T(1+PR_0).         \tag{14.38}
\]

The equality of paths follows first locally by the chain rule and uniqueness.
The complete feature flow and (14.30)–(14.31) keep the physical state bounded
on each finite forward interval, extending the physical solution and this
identity to all \(t\ge0\). If \(r_n(0)=0\), it is the stationary solution.
Backward physical completeness is not needed.

For a derivative taken at fixed physical time, the full Jacobian is
\(\mathsf C=\alpha\mathsf B-2bb^T/n\), as in Section 14.5. The rank-one
nuclear norm is exactly \(2\|b\|_2^2/n\), so (14.27), (14.34) and
(14.38) give

\[
 \sup_{0\le t\le T}\|\mathsf C(t)\|_*
    \le n\widetilde{\mathcal P}_T(M,R_0),\quad
 \widetilde{\mathcal P}_T
    =2(1+PR_0)\mathcal P_{S_T}+2\mathcal Q_{S_T}.      \tag{14.39}
\]

We used \(n\ge1\) for the last term. Since \(S_T\) is itself polynomial
in \(T,R_0\), the right side is a polynomial envelope of the same type.
The full physical variational equation is
\(\dot{\mathcal T}=\mathsf C\mathcal T\); its fundamental matrix is
invertible by the same inverse linear equation used above. Repeating
(14.35) with \(\mathsf C\) yields

\[
 \sup_{0\le t\le T}
 \left|\log\frac{V_{\mathcal T}(t)}{V_{\mathcal T}(0)}\right|
    \le nT\widetilde{\mathcal P}_T(M,R_0),\qquad
 \mathbb E\sup_{0\le t\le T}
 \left|\log\frac{V_{\mathcal T}(t)}{V_{\mathcal T}(0)}\right|
    \le C_Tn.                                         \tag{14.40}
\]

The expectation uses the original full Gaussian law (14.26), without
conditioning on a norm event. These are intrinsic volumes of full transported
tangent subspaces. They control neither the largest response singular value
by a width-independent constant nor the volume of a specified projection.

### 14.7 Exact hidden projection and its additional angle factor

Fix the initial readout \(c_0\), and differentiate the feature flow with
respect to its hidden initial coordinate \(\vartheta_0\). Let

\[
 \mathsf P=D_{\vartheta_0}\vartheta_s\in\mathbb R^{N_h\times N_h},
 \qquad \mathsf R=D_{\vartheta_0}c_s\in\mathbb R^{n\times N_h},
 \qquad
 \mathcal T=\begin{pmatrix}\mathsf P\\\mathsf R\end{pmatrix},
 \qquad \mathcal T(0)=\begin{pmatrix}I_{N_h}\\0\end{pmatrix}.
\]

The full derivative is invertible, so \(\mathcal T\) has full column rank
and \(V_{\mathcal T}>0\), with \(V_{\mathcal T}(0)=1\).
The positive-definite Gram matrix has a unique positive-definite square root,
obtained by diagonalizing it. The matrix

\[
 Q=\mathcal T(\mathcal T^T\mathcal T)^{-1/2}
       =\begin{pmatrix}Q_H\\Q_C\end{pmatrix}
\]

has orthonormal columns. In particular,
\(Q_H^TQ_H=I_{N_h}-Q_C^TQ_C\). Let \(a_1,\ldots,a_n\in[0,1]\) be
the singular values of the \(n\)-by-\(N_h\) matrix \(Q_C\), including
zeros. The upper bound one follows from \(Q_C^TQ_C\le I_{N_h}\).
Since
\(\mathsf P=Q_H(\mathcal T^T\mathcal T)^{1/2}\), taking determinants
of the Gram matrices gives exactly

\[
 |\det\mathsf P|
   =V_{\mathcal T}\sqrt{\det(I_n-Q_CQ_C^T)}
   =V_{\mathcal T}\prod_{j=1}^n\sqrt{1-a_j^2}.         \tag{14.41}
\]

This identity includes singular \(\mathsf P\): both sides then vanish.
To justify changing determinant dimension, a singular-value decomposition
of \(Q_C\) shows that \(Q_C^TQ_C\) and \(Q_CQ_C^T\) have the same
nonzero eigenvalues, with only extra zeros in the larger matrix. Thus the
determinants of their identity-minus forms agree.

Equation (14.41) places all loss of projected volume in at most \(n\)
directions, even though the hidden parameter dimension is \(N_h=n+2n^2\).
It gives \(|\det\mathsf P|\le V_{\mathcal T}\). The intrinsic bound
(14.28) supplies no estimate on how close the \(a_j\) are to one, and
therefore supplies no lower bound for the projected determinant.

On any interval where \(\mathsf P\) is invertible, define its readout
slope \(\mathsf K=\mathsf R\mathsf P^{-1}\). Factoring
\(\mathcal T=\left(\begin{smallmatrix}I\\\mathsf K\end{smallmatrix}\right)\mathsf P\)
and using the same singular-value argument gives

\[
 \log|\det\mathsf P|
     =\log V_{\mathcal T}
       -\frac12\log\det(I_n+\mathsf K\mathsf K^T).    \tag{14.42}
\]

The subtracted quantity is nonnegative. The full block variational equation
from (14.2) is

\[
 \mathsf P'=A\mathsf P+J^T\mathsf R,\qquad
 \mathsf R'=J\mathsf P.
\]

Differentiating \(\mathsf K=\mathsf R\mathsf P^{-1}\), with
\((\mathsf P^{-1})'=-\mathsf P^{-1}\mathsf P'\mathsf P^{-1}\), proves
its exact Riccati equation

\[
 \mathsf K'=J-\mathsf K A-\mathsf KJ^T\mathsf K.       \tag{14.43}
\]

This is a derivative at one fixed initial readout. It is not a conditional
covariance or the derivative of a conditional mean after averaging over
initial readouts.

The determinant identities (14.41)–(14.42) apply as well at fixed physical
time to its full derivative and the same hidden initial plane. The feature
Riccati equation (14.43) must then be replaced by its physical block equation.
Writing \(\mathsf C\) in hidden/readout blocks, it is

\[
 \dot{\mathsf K}=\mathsf C_{CH}+\mathsf C_{CC}\mathsf K
      -\mathsf K\mathsf C_{HH}-\mathsf K\mathsf C_{HC}\mathsf K,
\]

on each interval where \(\mathsf P\) is invertible. The full expression
\(\mathsf C=\alpha\mathsf B-2bb^T/n\) specifies every block, including
the clock terms. No feature-time derivative is substituted at fixed physical
time.

These exact identities and the positive intrinsic-volume bounds do not
establish hidden-projection nonsingularity, a projected lower-volume or
entropy bound, a response covariance estimate, or control of an adaptive
Gaussian query. Those require estimates beyond the full tangent-volume
bound proved here.
