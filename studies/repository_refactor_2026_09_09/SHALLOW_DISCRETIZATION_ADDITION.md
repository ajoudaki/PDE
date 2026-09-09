## 11. A sharp uniform shallow feature-step estimate

At one hidden layer the feature-ascent coordinates remain independent.
This permits a bound uniform in the update count that is stronger than
the fixed-program estimate of Section 8. The result concerns exact Euler
steps for feature ascent, with order-one stored readout. It does not
replace the residual by a constant in physical loss GD.

### 11.1. Model and quantitative statement

Take \(L=m=d=1,x_1=1\), and write the stored parameters as
\(a_i=W_i^{(2)},u_i=W_i^{(1)}\). All initial \(a_i,u_i\) are independent
standard Gaussians. Both block mobilities for feature ascent are \(n\).
For a real feature step \(h\), the simultaneous raw updates and output are

\[
 a_i^{j+1}=a_i^j+h\phi(u_i^j),\qquad
 u_i^{j+1}=u_i^j+ha_i^j\phi'(u_i^j),\qquad
 f_{n,1}^j=\frac1n\sum_{i=1}^na_i^j\phi(u_i^j).
 \tag{SD1}
\]

The index \(j\) counts steps. The scalar \(h\) is neither physical time
\(t\), the physical loss-GD step \(\eta_n\), nor a hidden feature vector.
There is no loss or residual multiplier in (SD1). Assume

\[
 \phi\in C^{12}(\mathbb R),\quad E\phi(G)^2=1,\quad
 M=\max\left\{1,\sup_z\frac{|\phi(z)|}{1+|z|},
                \max_{1\le q\le12}\|\phi^{(q)}\|_\infty\right\}<\infty,
 \qquad G\sim N(0,1).
 \tag{SD2}
\]

On the single mark space \(\Omega_1=(\mathbb R^2,\gamma_2)\), let
\(a_0,u_0\) be its independent standard Gaussian coordinates. Define
population coordinates \(A_j=W_j^{(2)},U_j=Z_j^{(1)}\) by the same
two-dimensional recursion, starting from \(A_0=a_0,U_0=u_0\), and set

\[
 F_{N,1}(h)=E_1[A_N\phi(U_N)],\qquad
 J_\phi=E\left[3\phi'(G)^3\phi'''(G)
       +11\phi(G)\phi'(G)^2\phi''(G)
       +4\phi'(G)^4+4\phi(G)^2\phi'(G)^2
       +12\phi'(G)^2\phi''(G)^2\right].
 \tag{SD3}
\]

The one-dimensional expectation in \(J_\phi\) uses the displayed \(G\);
\(E_1\) contracts the mark population. Set \(c_\phi=(16M)^{-1}\).
Section 11.2 defines a finite, explicit constant \(B_\phi^{\rm sh}\)
using only \(M\) and two Gaussian integrals.

**Theorem SD.** For every integer \(k\ge1\) and every
\(|h|\le c_\phi/k\),

\[
 \left|F_{k,1}(2h)-F_{2k,1}(h)
        +\frac{k(2k-1)}2J_\phi h^3\right|
 \le B_\phi^{\rm sh}k^4|h|^5.
 \tag{SD4}
\]

For each fixed finite \(N,h\), \(E f_{n,1}^N(h)=F_{N,1}(h)\) at
every width \(n\); thus these are also the width-first expected outputs.
The constant and the radius do not use a trained trajectory, an output
derivative, or a continuity modulus. The power \(k^4\) is sharp within
the activation class (SD2).

The proof first factors each coarse/fine Euler defect by \(h^2\).
Three step derivatives of each transported defect cost at most \(k^3\),
and there are \(k\) defects. A Gaussian-integrable envelope justifies
averaging those derivatives. Readout-sign symmetry then removes the
even terms, and a direct Gaussian calculation identifies the cubic term.

### 11.2. The explicit activation-only constant

All quantities in this subsection are nonnegative scalar envelopes, not
network coordinates or kernels. For a real \(R\ge1\), set

\[
 c=c_\phi,\qquad \Lambda=12MR,\qquad
 P=\exp(4c\Lambda)=e^{3R}.
 \tag{SD5}
\]

In the following order define

\[
 \begin{aligned}
 X_1&=4P\Lambda,\\
 X_2&=P(8\Lambda X_1+4c\Lambda X_1^2),\\
 X_3&=P\{12\Lambda(X_1^2+X_2)
                  +4c\Lambda(X_1^3+3X_1X_2)\},
 \end{aligned}
 \tag{SD6}
\]

\[
 \begin{aligned}
 \mathcal G_0&=\Lambda,&\mathcal G_1&=\Lambda X_1,\\
 \mathcal G_2&=\Lambda(X_2+X_1^2),&
 \mathcal G_3&=\Lambda(X_3+3X_1X_2+X_1^3),\\
 \mathcal B_q&=\sum_{v=0}^q\binom qv\mathcal G_v\mathcal G_{q-v}
       &&(0\le q\le3).
 \end{aligned}
 \tag{SD7}
\]

With \(\mathcal B_{-1}=\mathcal B_{-2}=0\), put

\[
 \mathcal Z_q=X_q+c^2\mathcal B_q+2qc\mathcal B_{q-1}
                         +q(q-1)\mathcal B_{q-2}\quad(1\le q\le3),
 \tag{SD8}
\]

\[
 \begin{aligned}
 T_1&=P(\mathcal Z_1+2\Lambda),\\
 T_2&=P(\mathcal Z_2+4\Lambda T_1+2c\Lambda T_1^2),\\
 T_3&=P\{\mathcal Z_3+6\Lambda(T_1^2+T_2)
                         +2c\Lambda(T_1^3+3T_1T_2)\}.
 \end{aligned}
 \tag{SD9}
\]

Next define

\[
 \begin{aligned}
 \mathcal H_0&=\Lambda,&\mathcal H_1&=\Lambda T_1,\\
 \mathcal H_2&=\Lambda(T_2+T_1^2),&
 \mathcal H_3&=\Lambda(T_3+3T_1T_2+T_1^3).
 \end{aligned}
 \tag{SD10}
\]

Finally, starting at \(V_0=P\mathcal B_0\), define successively for
\(q=1,2,3\)

\[
 V_q=P\left\{\mathcal B_q
      +2c\sum_{v=1}^q\binom qv\mathcal H_vV_{q-v}
      +2q\sum_{v=0}^{q-1}\binom{q-1}v\mathcal H_vV_{q-1-v}\right\},
 \qquad
 \mathcal C_M(R)=\frac16\sum_{v=0}^3\binom3v\mathcal H_vV_{3-v}.
 \tag{SD11}
\]

The claimed constant is

\[
 B_\phi^{\rm sh}=E_1\mathcal C_M(1+|a_0|+|u_0|).
 \tag{SD12}
\]

Every sum has at most four terms, and all right sides use previously
defined quantities. Finiteness of this fully specified integral is
proved below; no numerical quadrature or stored array is a premise.

### 11.3. Exact width identification and transported defect

For \(z=(a,u)\in\mathbb R^2\), define

\[
 \psi(z)=a\phi(u),\quad
 g(z)=(\phi(u),a\phi'(u))=\nabla\psi(z),\quad
 E_hz=z+hg(z),\quad R(z)=1+|a|+|u|.
 \tag{SD13}
\]

All derivative operator norms below are induced by ordinary Euclidean
norms. \(R(z)\) is a scalar growth envelope. Direct substitution gives

\[
 R(E_{\alpha h}z)\le(1+\alpha M|h|)R(z),\qquad 0\le\alpha\le2.
 \tag{SD14}
\]

For fixed \(N,h\), this bounds the terminal summand in (SD1) by
\(M(1+M|h|)^{2N}(1+|a_0|+|u_0|)^2\), which is integrable.
Each neuron is a function only of its own independent initial pair, so
the neurons remain iid and expectation of their average is exactly
\(F_{N,1}(h)\). This proves width identification before any step
derivative is taken.

Write \(C_h=E_{2h},B_h=E_h\circ E_h\). The fundamental theorem of
calculus gives

\[
 B_hz=C_hz+h^2b_h(z),\qquad
 b_h(z)=\int_0^1Dg(z+\tau hg(z))[g(z)]\,d\tau.
 \tag{SD15}
\]

For \(q=0,\ldots,k-1\), put \(x_q=C_h^{k-1-q}z\) and
\(v_q=\psi\circ B_h^q\). Consecutive hybrids
\(\psi(B_h^q(C_h^{k-q}z))\) differ by
\(v_q(C_hx_q)-v_q(B_hx_q)\). Summation and a segment integral give
the exact, signed identity

\[
 \psi(C_h^kz)-\psi(B_h^kz)=h^2Q_k(h,z),
 \qquad
 Q_k(h,z)=-\sum_{q=0}^{k-1}\int_0^1
 Dv_q(C_hx_q+\tau h^2b_h(x_q))[b_h(x_q)]\,d\tau.
 \tag{SD16}
\]

This uses no commutation of the two Euler maps.

### 11.4. Uniform derivative envelopes

Fix an initial \(z_0\), put \(R=R(z_0)\), and assume \(|h|k\le c\).
Every pre-defect Euler path in (SD16), including
\(x+\tau hg(x)\) in (SD15), has total Euler coefficient at most \(4k\).
The interpolation point is

\[
 C_hx+\tau h^2b_h(x)=(1-\tau)C_hx+\tau B_hx.
 \tag{SD17}
\]

Both endpoints obey (SD14). Convexity of \(R(z)\) bounds their
interpolation by \(e^{4M|h|k}R\). Starting at that point, at most
\(2k\) further fine steps remain. Thus every relevant point obeys

\[
 R(z)\le e^{6M|h|k}R\le e^{3/8}R<2R.
 \tag{SD18}
\]

The interpolation has not been treated as an Euler step. The larger
coefficient allowance \(4k+2k\) avoids any need to identify its path
with a single unbroken Euler trajectory.

For \(0\le q\le4\) and \(1\le j\le4\), respectively,

\[
 \|D^qg(z)\|\le6MR(z),\qquad
 \|D^j\psi(z)\|\le5MR(z).
 \tag{SD19}
\]

For \(q\ge1\), the second coordinate of \(D^qg\) consists of
\(a\phi^{(q+1)}(u)\) times all \(u\)-directions and \(q\) terms
with one \(a\)-direction and \(\phi^{(q)}(u)\). Unit Euclidean
directions have coordinate magnitudes at most one; summing these terms
and the first coordinate gives the first bound. The same count, with
one fewer activation derivative, gives the second; its first derivative
uses the linear-growth bound on \(\phi\). The case \(q=0\) follows
directly from (SD13). By (SD18), all these derivative bounds are at
most \(\Lambda=12MR\).

Consider a pre-defect path \(y_{j+1}=y_j+\alpha_jhg(y_j)\) starting
at \(z_0\), where \(0\le\alpha_j\le2\) and
\(\sum_j\alpha_j\le4k\). Its homogeneous tangent products have norm
at most

\[
 \prod_j(1+\alpha_j|h|\Lambda)
 \le e^{\Lambda|h|\sum_j\alpha_j}\le P.
 \tag{SD20}
\]

A prime denotes \(d/dh\). Differentiating one step gives

\[
 \begin{aligned}
 y_{j+1}'&=(I+\alpha_jhDg)y_j'+\alpha_jg,\\
 y_{j+1}''&=(I+\alpha_jhDg)y_j''+2\alpha_jDg[y_j']
                             +\alpha_jhD^2g[y_j',y_j'],\\
 y_{j+1}'''&=(I+\alpha_jhDg)y_j'''
       +3\alpha_j\{D^2g[y_j',y_j']+Dg[y_j'']\}\\
       &\quad+\alpha_jh\{D^3g[y_j',y_j',y_j']
                                  +3D^2g[y_j',y_j'']\}.
 \end{aligned}
 \tag{SD21}
\]

Iterating in \(j\) and summing the inhomogeneous terms gives

\[
 \|y_j^{(q)}\|_2\le X_qk^q,\qquad q=1,2,3.
 \tag{SD22}
\]

In detail, the first recurrence gives \(4P\Lambda k=X_1k\).
After division by \(k^2\), the second's source sum is bounded by
\(8\Lambda X_1+4c\Lambda X_1^2\), then multiplied by \(P\).
After division by \(k^3\), the third's source sum is bounded by
\(12\Lambda(X_1^2+X_2)+4c\Lambda(X_1^3+3X_1X_2)\),
then multiplied by \(P\). These are exactly (SD6). The initial
derivatives vanish because \(z_0\) is independent of \(h\).

The curve \(x_q+\tau hg(x_q)\) in (SD15) is the path to \(x_q\)
with one coefficient \(\tau\le1\) appended; its total is still below
\(4k\). The chain rule, (SD19), and (SD22) bound the derivatives
of \(g(x_q)\) and \(Dg(x_q+\tau hg(x_q))\) through order three by
\(\mathcal G_jk^j\). For example the third derivative of a composition
is the sum of the terms with \(y'''\), \(3y'y''\), and \((y')^3\),
which explains \(\mathcal G_3\). Leibniz's rule inside (SD15) yields

\[
 \|\partial_h^jb_h(x_q)\|_2\le\mathcal B_jk^j,
 \qquad 0\le j\le3.
 \tag{SD23}
\]

Since

\[
 \partial_h^j(h^2b_h)
 =h^2\partial_h^jb_h+2jh\partial_h^{j-1}b_h
                         +j(j-1)\partial_h^{j-2}b_h,
 \tag{SD24}
\]

Terms with negative derivative order are omitted. For \(j=1,2,3\),
the derivatives of the point (SD17) are bounded by
\(\mathcal Z_jk^j\). Here \(C_hx_q\) itself is a pre-defect path
covered by (SD22); use \(k\ge1,|h|k\le c\) in (SD24).
Starting from this interpolation point and repeating (SD21) for the
remaining at most \(2k\) fine steps proves bounds \(T_jk^j\).
The corresponding normalized source sums now have coefficients
\(2,4,6\) and \(2c\), and their initial contributions are
\(\mathcal Z_j\). This gives exactly (SD9), with the same upper
bound \(P\) for homogeneous amplification. Derivatives through order
three of \(Dg\) and \(D\psi\) along this last path are consequently
bounded by \(\mathcal H_jk^j\), as in (SD10).

It remains to transport the initial direction \(b_h(x_q)\) through
these fine steps. If that direction is denoted by \(\omega\), then

\[
 \omega^+=\omega+hDg(z)\omega,
 \quad
 (\omega^+)^{(j)}=\omega^{(j)}
  +h\sum_{v=0}^j\binom jv(Dg(z))^{(v)}\omega^{(j-v)}
  +j\sum_{v=0}^{j-1}\binom{j-1}v(Dg(z))^{(v)}\omega^{(j-1-v)}.
 \tag{SD25}
\]

The \(v=0\) term in the first sum is the homogeneous tangent factor.
The other terms are summed over at most \(2k\) fine steps. Starting
from (SD23), induction on \(j=0,1,2,3\) proves
\(\|\omega^{(j)}\|_2\le V_jk^j\): after dividing by \(k^j\),
the two source sums are bounded by the \(2c\) and \(2j\) sums in
(SD11), respectively, followed by amplification \(P\).

The transported integrand in (SD16) is now \(D\psi(z)[\omega]\).
For every \(0\le j\le3\), its \(j\)-th derivative has magnitude at
most

\[
 k^j\sum_{v=0}^j\binom jv\mathcal H_vV_{j-v}.
 \tag{SD26}
\]

Integration in \(\tau\) has mass one and there are \(k\) summands.
In particular,

\[
 \sup_{|h|\le c/k}|\partial_h^3Q_k(h,z_0)|
 \le6\mathcal C_M(R)k^4.
 \tag{SD27}
\]

All envelopes (SD6)--(SD11) are finite polynomials with nonnegative
coefficients in \(c,\Lambda,P\). Since \(c\le1,\Lambda=12MR\),
\(P=e^{3R}\), each is bounded by a polynomial in \(R\) times
\(e^{C R}\), with finite constants depending only on the displayed
finite recursion and \(M\). Such functions are integrable at
\(R=1+|a_0|+|u_0|\): for any finite \(p,\lambda\ge0\),

\[
 E[(1+|G|)^pe^{\lambda|G|}]<\infty,
 \tag{SD28}
\]

because \(\lambda|x|-x^2/2\le -x^2/4\) outside a finite interval.
Apply this one-dimensional integral estimate to both independent marks.
It proves finiteness of (SD12) and, using (SD26) for all four derivative
orders, an integrable envelope for \(Q_k\) and its first three
derivatives at each fixed \(k\). Integrating the fundamental theorem of
calculus and applying dominated convergence successively therefore
justifies all three differentiations under \(E_1\).

### 11.5. Parity, cubic coefficient, and sharpness

Set \(\overline Q_k(h)=E_1Q_k(h,(a_0,u_0))\). The preceding proof gives

\[
 D_k(h):=F_{k,1}(2h)-F_{2k,1}(h)=h^2\overline Q_k(h),
 \qquad
 \sup_{|h|\le c/k}|\overline Q_k'''(h)|
 \le6B_\phi^{\rm sh}k^4.
 \tag{SD29}
\]

Replacing \((h,a_0,u_0)\) by \((-h,-a_0,u_0)\) preserves the law,
negates each \(A_j\), and leaves each \(U_j\) unchanged. Thus each
\(F_{N,1}\), and hence \(D_k\), is odd. The factorization shows that
\(\overline Q_k\) is odd away from zero; continuity extends this to
zero, so \(\overline Q_k(0)=\overline Q_k''(0)=0\). Repeated
integration of its third derivative gives

\[
 \overline Q_k(h)-h\overline Q_k'(0)
   =\frac12\int_0^h(h-v)^2\overline Q_k'''(v)\,dv.
 \tag{SD30}
\]

The same estimate applies to negative \(h\) by reversing orientation.
Multiplication by \(h^2\) proves a remainder at most
\(B_\phi^{\rm sh}k^4|h|^5\).

To identify its coefficient without any Gaussian compiler input, evaluate
all derivatives at the initial \(z\) and write
\(b=Dg[g],c_1=Dg[b],c_2=D^2g[g,g]\). Direct differentiation of
\(z_{j+1}=z_j+hg(z_j)\) at \(h=0\) and summation give

\[
 z_N'(0)=Ng,\quad z_N''(0)=N(N-1)b,\quad
 z_N'''(0)=6\binom N3c_1+\frac{N(N-1)(2N-1)}2c_2.
 \tag{SD31}
\]

Indeed the third-derivative increment is
\(3j(j-1)c_1+3j^2c_2\); the finite sums of \(j(j-1)\) and \(j^2\)
are \(2\binom N3\) and \(N(N-1)(2N-1)/6\). Since \(g=\nabla\psi\),
symmetry of the Hessian gives

\[
 D\psi[c_1]=D^2\psi[g,b]=\|b\|_2^2,\qquad
 D\psi[c_2]=D^3\psi[g,g,g].
 \tag{SD32}
\]

Define \(\mathsf S=E_1D^3\psi[g,g,g]\) and
\(\mathsf H=E_1\|Dg[g]\|_2^2\). The third derivative of the
observable in (SD31) has the three terms
\(D\psi[z_N''']+3D^2\psi[z_N',z_N'']+
D^3\psi[z_N',z_N',z_N']\), and consequently

\[
 F_{N,1}^{(3)}(0)=\frac{N(4N^2-3N+1)}2\mathsf S
                  +2N(N-1)(2N-1)\mathsf H.
 \tag{SD33}
\]

These derivatives may be averaged: for fixed \(N\), (SD18)--(SD22)
apply in a neighborhood of zero, and the chain rule for \(\psi\)
gives the same polynomial-times-linear-exponential Gaussian envelope.

At \(z=(a_0,u_0)\), put \(p=\phi'(u_0),q=\phi''(u_0)\). Then

\[
 g=(\phi(u_0),a_0p),\qquad
 Dg[g]=(a_0p^2,\phi(u_0)p+a_0^2pq),
 \tag{SD34}
\]

and
\(D^3\psi[g,g,g]=3a_0^2\phi(u_0)p^2q+
a_0^4p^3\phi'''(u_0)\).
Independence and \(E a_0^2=1,E a_0^4=3\) give

\[
 \begin{aligned}
 \mathsf S&=3E[\phi\phi'^2\phi''+\phi'^3\phi'''],\\
 \mathsf H&=E[\phi'^4+\phi^2\phi'^2
                          +2\phi\phi'^2\phi''+3\phi'^2\phi''^2],
 \end{aligned}
 \tag{SD35}
\]

where all activation factors are evaluated at \(G\sim N(0,1)\).
Thus \(\mathsf S+4\mathsf H=J_\phi\). Substitution of \(N=k,2k\)
in (SD33) yields

\[
 \overline Q_k'(0)
 =\frac{8F_{k,1}^{(3)}(0)-F_{2k,1}^{(3)}(0)}6
 =-\frac{k(2k-1)}2J_\phi.
 \tag{SD36}
\]

Together with (SD29)--(SD30), this proves (SD4).

For the constant branch \(\phi\equiv\pm1\), one has
\(F_{N,1}(h)=Nh,J_\phi=0\), and the discrepancy vanishes exactly.
For \(\phi(z)=z\), diagonalize one step using
\((a+u)/\sqrt2,(a-u)/\sqrt2\), whose multipliers are \(1+h,1-h\).
Both initial coordinates have variance one, so

\[
 F_{N,1}(h)=\frac{(1+h)^{2N}-(1-h)^{2N}}2,\qquad J_\phi=8.
 \tag{SD37}
\]

Its discrepancy has cubic coefficient \(-4k(2k-1)\) and fifth
coefficient

\[
 32\binom{2k}5-\binom{4k}5
 =-\frac43k(k-1)(2k-1)(8k-9).
 \tag{SD38}
\]

If (SD4) held with \(Ck^p|h|^5\) for some fixed \(p<4\) and
positive radius proportional to \(1/k\), divide by \(|h|^5\) and
take \(h\to0\) at each fixed \(k\). Equation (SD38) would be bounded
in magnitude by \(Ck^p\), which is impossible as \(k\to\infty\).
This proves sharpness. \(\square\)

### 11.6. A restricted dyadic terminal-output consequence

For a real accumulated feature time \(s\), set
\(G_N(s)=F_{N,1}(s/N)\). Fix \(0<S\le2c_\phi\). Substituting
\(h=s/(2k)\) in (SD4) gives

\[
 \sup_{|s|\le S}|G_{2k}(s)-G_k(s)|
 \le\frac{|J_\phi|S^3}{8k}
                   +\frac{B_\phi^{\rm sh}S^5}{32k}.
 \tag{SD39}
\]

For \(k=2^j\), the right side is summable in \(j\). Telescoping,
completeness of \(\mathbb R\), and
\(\sum_{j=p}^\infty2^{-j}=2^{1-p}\) give a uniform limit
\(G_\infty\) on \([-S,S]\), with

\[
 \sup_{|s|\le S}|G_\infty(s)-G_{2^p}(s)|
 \le2^{-p}\left(\frac{|J_\phi|S^3}{4}
                         +\frac{B_\phi^{\rm sh}S^5}{16}\right).
 \tag{SD40}
\]

Each fixed \(G_N\) is continuous by its finite smooth recursion and
the Gaussian envelope (SD14); uniform convergence preserves continuity.
The consequence is only about the terminal expected output on this
explicit short feature-time interval. It supplies no restart state,
partition independence, hidden-state convergence, or growing-program
width theorem. Physical loss GD includes a moving residual in every
raw step, so it is a different discretization. Neither (SD4) nor
(SD40) establishes its continuous-time limit or any corresponding result
with reused inter-hidden-layer matrices.
