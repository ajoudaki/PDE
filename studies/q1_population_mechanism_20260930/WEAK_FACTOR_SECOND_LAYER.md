# Weak-factor second-layer acceleration: full q1 coefficient

Frozen candidate: 2026-09-30. Author: `simplex_mechanism_route`.
Scientific inputs: the supervisor's two self-contained assignments; no other
route file, study, book, external source, or trajectory was read. The frozen
triangle note was not changed. Required process/skill inputs are the same as
listed there. This note owns the second-layer weak-factor calculation only.

**Result conditional on a scalar sign certificate.** For all sufficiently
small positive fixed \(\varepsilon\), the actual population q1 startup
acceleration of either primitive-bit second-layer feature energy is positive,
although its labels have zero correlation with that bit. The context-feature
energy acceleration is negative. The derived coefficients include readin
drift, the full true-transpose covariance, and q1 memory. Their signs reduce
to explicit polynomials in one-dimensional Gaussian moments. An executed
ordinary quadrature gives large sign margins, but is not a rigorous sign
certificate. The root agent is independently certifying these scalar moments.

No claim of population-flow existence, a convergent time series, global
fitting, or persistence of these signs for a specified non-small
\(\varepsilon\) is made.

## 1. Exact setup and acceleration formula

The four inputs and labels are

\[
u_{\sigma\tau}=(\sqrt{1-2\varepsilon^2},\varepsilon\sigma,
\varepsilon\tau),\qquad y_{\sigma\tau}=\sigma\tau,
\qquad \sigma,\tau\in\{-1,1\},\quad 0<\varepsilon<1/\sqrt2.
\]

Use the assigned population q1 equations, tanh activation \(\phi\), standard
Gaussian readin \(A=(X,Y,Z)\), zero initial \(W,V\), initial \(K=H\),
and the fixed canonical Gaussian \(T\) with its true transpose. Let the
four Walsh characters be \(0,1,2,y\), representing
\(1,\sigma,\tau,\sigma\tau\), respectively. A Walsh coefficient always
means the normalized mean over the four samples:

\[
H_\chi=\tfrac14\sum_a\chi_a H_a,
\quad G_\chi=\tfrac14\sum_a\chi_aG_a,
\quad Q_\chi=\tfrac14\sum_a\chi_a\phi'(Z_a),
\quad R_\chi=\tfrac14\sum_a\chi_a\phi''(Z_a).
\]

Character products are denoted by concatenation. All quantities in the
calculations below are evaluated at initialization, unless time is displayed.
Equivariance and uniqueness, when available, give \(F_a=y_af\). In the
local feature clock \(s=2\int_0^t(1-f)\,dt\),
\(W'=G_y\), \(V_a'=y_aD_a\), and
\(A'=\frac14\sum_a y_aL_a u_a\). Consequently

\[
A'(0)=V'(0)=K'(0)=G'(0)=0,
\qquad V_a''(0)=U_a:=y_aG_y\phi'(Z_a),
\]

\[
A''(0)=A_U:=\tfrac14\sum_a\phi'(A\cdot u_a)u_a T^*U_a.
\]

For a measured character \(k\), define
\(Y_a^k=k_aG_k\phi'(Z_a)\) and
\(A_{Y^k}=\frac14\sum_a\phi'(A\cdot u_a)u_aT^*Y_a^k\).
Then the exact initial acceleration of
\(\mathcal E_k(s)=\mathbb E_2G_k(s)^2\) is

\[
\mathcal E_k''(0)
=2\mathbb E_1 A_U\cdot A_{Y^k}
+\frac2{16}\sum_{a,b}C_{ab}\mathbb E_2U_bY_a^k,
\qquad C_{ab}=\mathbb E_1H_aH_b. \tag{1.1}
\]

To verify all factors: \(G'=0\), so the energy derivative is
\(2\mathbb E G_kG_k''\). The readin part of \(Z_a''\) is
\(T[\phi'(A\cdot u_a)u_a\cdot A_U]\). Transposition gives exactly the
first term. The memory part is
\(\frac14\sum_b V_b''\mathbb E_1K_bH_a
=\frac14\sum_bU_b C_{ab}\); another sample average in the energy gives
the second term. Neither key motion nor a derivative of \(K_bH_a\)
contributes: \(V=V'=0\) initially. Thus (1.1) includes the entire initial
memory effect.

This is a conditional startup theorem: it requires the supplied regular
flow, differentiability at zero, the expectation interchanges, and the
specified first-transpose source law. It does not establish any of them.

## 2. Walsh parity reduces all reverse calls exactly

Initial readin parity gives
\(\mathbb E_1H_\chi H_\psi=0\) for \(\chi\ne\psi\). Put
\(v_\chi=\mathbb E_1H_\chi^2\). The four Gaussian calls
\(Z_\chi=TH_\chi\) are therefore independent centered Gaussians of
variances \(v_\chi\), and \(Z_a=\sum_\chi\chi_aZ_\chi\).

Walsh-transform the sources in (1.1):

\[
U_\chi=G_yQ_{y\chi},\qquad Y_\chi^k=G_kQ_{k\chi}.
\]

The true-transpose formula supplied in the assignment gives

\[
T^*U_\chi=\beta_\chi H_\chi+\xi_\chi,
\qquad T^*Y_\chi^k=\gamma_\chi^kH_\chi+\eta_\chi^k, \tag{2.1}
\]

where all reverse residuals are jointly centered Gaussian, independent of
the initial readin, with

\[
\mathbb E\xi_\chi\eta_\psi^k
=\mathbf1_{\chi=\psi}\mathbb E_2U_\chi Y_\chi^k. \tag{2.2}
\]

Here and below this is the full source Gram, without subtracting a projected
or centered covariance. To justify the diagonal structure, under either
latent-bit flip the source \(U_\chi\), as well as \(Y_\chi^k\), transforms
by the character \(\chi\). Consequently
\(\mathbb E\partial_{Z_\psi}U_\chi=0\) and
\(\mathbb E U_\chi Y_\psi^k=0\) when \(\chi\ne\psi\). Applying the
given transpose rule in Walsh coordinates has no extra factor of four:
\(\sum_b\mathbb E\partial_{Z_b}U_\chi H_b
=\sum_\psi\mathbb E\partial_{Z_\psi}U_\chi H_\psi\).

For the remaining diagonal coefficients, differentiation gives the exact
identities

\[
\beta_\chi=\mathbb E_2Q_{y\chi}^2+\mathbb E_2G_yR_y,
\qquad
\gamma_\chi^k=\mathbb E_2Q_{k\chi}^2+\mathbb E_2G_kR_k. \tag{2.3}
\]

Indeed, \(\partial_{Z_\chi}G_y=Q_{y\chi}\) and
\(\partial_{Z_\chi}Q_{y\chi}=R_y\), and likewise for \(k\).

Let \(D_U=\sum_\chi\beta_\chi H_\chi\nabla H_\chi\) and
\(D_{Y^k}=\sum_\chi\gamma_\chi^kH_\chi\nabla H_\chi\), where
\(\nabla\) differentiates the initial readin vector. Equations (2.1)--(2.2)
give the exact decomposition

\[
\mathbb E_1A_U\cdot A_{Y^k}
=\mathbb E_1D_U\cdot D_{Y^k}
+\sum_\chi\mathbb E_1|\nabla H_\chi|^2\,
\mathbb E_2U_\chi Y_\chi^k. \tag{2.4}
\]

Similarly Walsh orthogonality turns the memory term in (1.1) into

\[
2\sum_\chi v_\chi\mathbb E_2U_\chi Y_\chi^k. \tag{2.5}
\]

Thus there are precisely three contributions: the drift in (2.4), its full
reverse covariance, and (2.5).

## 3. Small-factor expansion and scalar constants

For the inner scalar Gaussian \(X\sim N(0,1)\), write

\[
h=\phi(X),\quad p=\phi'(X),\quad k=\phi''(X),\quad
\ell=\phi'''(X),\qquad
\kappa=\mathbb E h^2,\quad a=\mathbb E p^2,\quad b=\mathbb E k^2.
\]

Expansion in the fixed geometric parameter \(\varepsilon\) gives, in every
finite Gaussian \(L^r\),

\[
\begin{array}{ll}
H_0=h+O(\varepsilon^2),&\nabla H_0=(p,0,0)+O(\varepsilon^2),\\
H_1=\varepsilon Yp+O(\varepsilon^3),&
\nabla H_1=\varepsilon(Yk,p,0)+O(\varepsilon^3),\\
H_2=\varepsilon Zp+O(\varepsilon^3),&
\nabla H_2=\varepsilon(Zk,0,p)+O(\varepsilon^3),\\
H_y=\varepsilon^2YZk+O(\varepsilon^4),&
\nabla H_y=\varepsilon^2(YZ\ell,Zk,Yk)+O(\varepsilon^4).
\end{array} \tag{3.1}
\]

In particular, \(v_0=\kappa+O(\varepsilon^2)\),
\(v_1=v_2=\varepsilon^2a+O(\varepsilon^4)\), and
\(v_y=\varepsilon^4b+O(\varepsilon^6)\).

Introduce independent Gaussians
\(R\sim N(0,\kappa)\), \(B,C\sim N(0,a)\), and \(D\sim N(0,b)\),
and use uppercase derivatives at the outer context Gaussian:

\[
g=\phi(R),\quad J=\phi'(R),\quad K=\phi''(R),\quad
L=\phi'''(R),\quad M=\phi''''(R),
\quad \Lambda=JD+KBC,\quad \mathcal M=KD+LBC.
\]

Taylor expansion of the Gaussian forward calls yields

\[
G_0=g+O(\varepsilon^2),\quad G_1=\varepsilon JB+O(\varepsilon^3),
\quad G_y=\varepsilon^2\Lambda+O(\varepsilon^4),
\]

\[
Q_0=J+O(\varepsilon^2),\quad Q_1=\varepsilon KB+O(\varepsilon^3),
\quad Q_2=\varepsilon KC+O(\varepsilon^3),
\quad Q_y=\varepsilon^2\mathcal M+O(\varepsilon^4),
\]

\[
R_y=\varepsilon^2(LD+MBC)+O(\varepsilon^4). \tag{3.2}
\]

Define outer constants

\[
T=\mathbb E J^2,\quad U=\mathbb E K^2,\quad
S=\mathbb E(K^2+JL),\quad V=\mathbb E(L^2+KM),
\]

\[
B_0=bS+a^2V,\quad B_1=aU,\quad C_0=aS. \tag{3.3}
\]

Equations (2.3) and (3.2) give

\[
(\beta_0,\beta_1,\beta_2,\beta_y)
=(\varepsilon^4B_0,\varepsilon^2B_1,
\varepsilon^2B_1,T)
+(O(\varepsilon^6),O(\varepsilon^4),O(\varepsilon^4),O(\varepsilon^2)).
\tag{3.4}
\]

For the measured bit \(k=1\),

\[
(\gamma_0^1,\gamma_1^1,\gamma_2^1,\gamma_y^1)
=(\varepsilon^2C_0,T,\varepsilon^2a\mathbb E JL,
\varepsilon^2C_0)
+(O(\varepsilon^4),O(\varepsilon^2),O(\varepsilon^4),O(\varepsilon^4)).
\tag{3.5}
\]

It matters to use (2.3), rather than differentiate only a leading source
truncation. For example, the leading displayed \(Y_y^1\) below has no
\(D\) dependence, but the next source term contributes to
\(\gamma_y^1\) at order \(\varepsilon^2\).

The expansions and remainders need no flow expansion in \(\varepsilon\):
they are calculations of its exact initial acceleration. For justification,
all tanh derivatives of any fixed order are bounded. Taylor remainders are
therefore controlled by Gaussian polynomials. The normalized variances
\(v_1/\varepsilon^2\), \(v_y/\varepsilon^4\) have positive limits
\(a,b\); their square roots extend smoothly near zero. Coupling each Walsh
call to a fixed independent standard Gaussian gives the displayed
\(L^r\) bounds. Parity under simultaneous reversal of the two input bits
ensures the scalar energy accelerations are even in \(\varepsilon\), so
the successive remainder orders below are two powers apart.

## 4. Primitive-bit energy: all three order-six coefficients

Using (3.1), (3.4), and (3.5), write
\(D_U=\varepsilon^4d_U+O_{L^r}(\varepsilon^6)\) and
\(D_{Y^1}=\varepsilon^2d_1+O_{L^r}(\varepsilon^4)\), where

\[
\begin{split}
(d_U)_x&=B_0hp+B_1(Y^2+Z^2)pk+T Y^2Z^2k\ell,\\
(d_U)_y&=B_1Yp^2+T YZ^2k^2,\\
(d_U)_z&=B_1Zp^2+T Y^2Zk^2,
\end{split}
\]

\[
d_1=(C_0hp+TY^2pk,\ TYp^2,\ 0). \tag{4.1}
\]

Define six inner moments

\[
A_0=\mathbb E h^2p^2,\quad A_1=\mathbb E hp^2k,\quad
A_2=\mathbb E p^2k^2,\quad A_3=\mathbb E hpk\ell,\quad
A_4=\mathbb E pk^2\ell,\quad A_5=\mathbb E p^4.
\]

Since \(Y,Z\) are independent standard Gaussians,
\(\mathbb EY^2=1\), \(\mathbb EY^4=3\), and
\(\mathbb E(Y^2+Z^2)Y^2=4\). Taking the dot product in (4.1) gives the
readin-drift coefficient

\[
\boxed{\begin{split}
\mathfrak D_1={}&B_0C_0A_0+(B_0T+2B_1C_0)A_1
+(4B_1T+T^2)A_2\\
&+TC_0A_3+3T^2A_4+B_1TA_5.
\end{split}} \tag{4.2}
\]

For the other terms, the source expansions are

\[
\begin{array}{c|c|c}
\chi&U_\chi&Y_\chi^1\\ \hline
0&\varepsilon^4\Lambda\mathcal M+O(\varepsilon^6)
 &\varepsilon^2JKB^2+O(\varepsilon^4)\\
1&\varepsilon^3KC\Lambda+O(\varepsilon^5)
 &\varepsilon J^2B+O(\varepsilon^3)\\
2&\varepsilon^3KB\Lambda+O(\varepsilon^5)
 &\varepsilon^3JB\mathcal M+O(\varepsilon^5)\\
y&\varepsilon^2J\Lambda+O(\varepsilon^4)
 &\varepsilon^2JKBC+O(\varepsilon^4).
\end{array} \tag{4.3}
\]

Put \(P=\mathbb E J^2K^2\) and \(Q=\mathbb E JK^2L\). Gaussian
independence and the fourth moment of \(B\) give

\[
\mathbb E U_0Y_0^1
=\varepsilon^6(abP+3a^3Q)+O(\varepsilon^8),
\quad
\mathbb E U_1Y_1^1=\varepsilon^4a^2P+O(\varepsilon^6). \tag{4.4}
\]

For example, the first expectation equals at leading order
\(\mathbb E(JD+KBC)(KD+LBC)JKB^2\).
Its two surviving terms are
\(\mathbb E D^2\mathbb EB^2\mathbb EJ^2K^2=abP\) and
\(\mathbb EB^4\mathbb EC^2\mathbb EJK^2L=3a^3Q\).
All mixed terms contain an odd independent Gaussian. The channels \(2,y\)
give products of orders six and four, respectively; their gradient norms
are orders two and four, so both contribute only at order eight or above.

As \(\mathbb E|\nabla H_0|^2=a+O(\varepsilon^2)\) and
\(\mathbb E|\nabla H_1|^2=\varepsilon^2(a+b)+O(\varepsilon^4)\),
the full reverse-covariance contribution is

\[
\boxed{\mathfrak N_1=a^2(a+2b)P+3a^4Q.} \tag{4.5}
\]

The memory coefficient from (2.5), using
\(v_0=\kappa+O(\varepsilon^2)\) and
\(v_1=\varepsilon^2a+O(\varepsilon^4)\), is

\[
\boxed{\mathfrak M_1=(\kappa ab+a^3)P+3\kappa a^3Q.} \tag{4.6}
\]

Combining (1.1)--(2.5),

\[
\boxed{\mathcal E_1''(0)
=2\varepsilon^6(\mathfrak D_1+\mathfrak N_1+\mathfrak M_1)
+O(\varepsilon^8).} \tag{4.7}
\]

The same formula holds for bit \(2\) by exchanging \(Y,Z\). All constants
are fixed, independent of \(\varepsilon\). In particular, positivity of
the parenthesized scalar implies positivity for every sufficiently small
positive fixed \(\varepsilon\), rather than merely a sign at the
degenerate limiting dataset.

## 5. Context energy: all three order-four coefficients

For the context character \(k=0\), (2.3) gives
\(\gamma_0^0=J_0+O(\varepsilon^2)\), where

\[
J_0=\mathbb E(J^2+gK).
\]

All other \(\gamma_\chi^0\) are bounded, so
\(D_{Y^0}=J_0(hp,0,0)+O_{L^r}(\varepsilon^2)\). Consequently

\[
\boxed{\mathfrak D_0=J_0(B_0A_0+2B_1A_1+TA_3).} \tag{5.1}
\]

Let \(P_0=\mathbb E gJ^2K\), \(Q_0=\mathbb E gJKL\). The context
source \(Y_0^0=gJ+O(\varepsilon^2)\), so

\[
\mathbb E U_0Y_0^0
=\varepsilon^4(bP_0+a^2Q_0)+O(\varepsilon^6). \tag{5.2}
\]

Every other Walsh channel gives a reverse-covariance or memory contribution
of order at least six: the source-product orders for channels \(1,2,y\)
are four, four, and four, while their gradient-norm and variance orders
are two, two, and four. Hence

\[
\boxed{\mathfrak N_0=a(bP_0+a^2Q_0),\qquad
\mathfrak M_0=\kappa(bP_0+a^2Q_0),} \tag{5.3}
\]

\[
\boxed{\mathcal E_0''(0)
=2\varepsilon^4(\mathfrak D_0+\mathfrak N_0+\mathfrak M_0)
+O(\varepsilon^6).} \tag{5.4}
\]

## 6. Exact polynomial recipe for scalar certification

Define only the following twelve scalar moments:

\[
I_j=\mathbb E_{X\sim N(0,1)}\operatorname{sech}^{2j}X,
\qquad
J_j=\mathbb E_{R\sim N(0,\kappa)}\operatorname{sech}^{2j}R,
\quad j=1,\ldots,6,
\quad \kappa=1-I_1.
\]

The coefficient polynomials are obtained by the following finite recipe;
there are no further expectations or trajectory-dependent quantities:

\[
\begin{gathered}
a=I_2,\quad b=4(I_2-I_3),\quad
T=J_2,\quad U=4(J_2-J_3),\\
S=8J_2-10J_3,\quad V=32J_2-112J_3+84J_4,\\
B_0=bS+a^2V,\quad B_1=aU,\quad C_0=aS,\\
A_0=I_2-I_3,\quad A_1=-2(I_3-I_4),\quad
A_2=4(I_4-I_5),\\
A_3=-8I_3+20I_4-12I_5,\quad
A_4=16I_4-40I_5+24I_6,\quad A_5=I_4,\\
P=4(J_4-J_5),\quad Q=16J_4-40J_5+24J_6,\\
J_0=3J_2-2J_1,\quad P_0=-2(J_3-J_4),\quad
Q_0=-8J_3+20J_4-12J_5.
\end{gathered} \tag{6.1}
\]

Substitute these polynomials into (4.2), (4.5), (4.6), and (5.1), (5.3).
These expressions follow directly from
\(\phi'=p\), \(\phi''=-2hp\),
\(\phi'''=4p-6p^2\), and
\(\phi''''=(-8+24p)hp\), with \(h^2=1-p\).
For example,
\((\phi''')^2+\phi''\phi''''=32p^2-112p^3+84p^4\),
which verifies the less immediate polynomial \(V\).

There is a typographical distinction between \(J_0\) (the explicitly
defined context drift constant) and \(J_j\), \(j\ge1\), the Gaussian
moments; no moment with exponent zero is being used.

## 7. Executed diagnostic and exact reproduction source

One deterministic one-dimensional quadrature was executed with Python
3.10.12, NumPy 1.26.4, and SciPy 1.13.0 in `/home/amir/Codes/PDE`.
It evaluates the explicit scalar
integrals above; it is not a training experiment, trajectory approximation,
or rigorous numerical sign enclosure. Exit status was zero. The source below
is the exact executed heredoc body; it used `python - <<'PY'` and the closing
delimiter `PY`.

```python
import numpy as np
from scipy.integrate import quad
from math import sqrt, pi, exp, tanh

def moments(v):
    return {j: 2*quad(lambda x: (1-tanh(x)**2)**j*exp(-x*x/(2*v))/sqrt(2*pi*v),0,12,epsabs=2e-13,epsrel=2e-13)[0] for j in range(1,7)}
i=moments(1.0)
kappa=1-i[1]
a=i[2]; b=4*(i[2]-i[3]); o=moments(kappa)
T=o[2]; u=4*(o[2]-o[3]); S=8*o[2]-10*o[3]; D=32*o[2]-112*o[3]+84*o[4]
B0=b*S+a*a*D; B1=a*u; C0=a*S
I0=b/4; I1=-2*(i[3]-i[4]); I2=4*(i[4]-i[5]); I3=-8*i[3]+20*i[4]-12*i[5]; I4=16*i[4]-40*i[5]+24*i[6]; I5=i[4]
J2=4*(o[4]-o[5]); J4=16*o[4]-40*o[5]+24*o[6]
Dr=B0*C0*I0+(B0*T+2*B1*C0)*I1+(4*B1*T+T*T)*I2+T*C0*I3+3*T*T*I4+B1*T*I5
No=a*a*(a+2*b)*J2+3*a**4*J4
Me=(kappa*a*b+a**3)*J2+3*kappa*a**3*J4
ctxDr=(3*o[2]-2*o[1])*(B0*I0+2*B1*I1+T*I3)
ctxNo=a*(b*(-2*(o[3]-o[4]))+a*a*(-8*o[3]+20*o[4]-12*o[5]))
ctxMe=kappa/a*ctxNo
for name, value in [('kappa',kappa),('a',a),('b',b),('T',T),('S',S),('D',D),('B0',B0),('bit_drift',Dr),('bit_noise',No),('bit_memory',Me),('bit_total',Dr+No+Me),('context_drift',ctxDr),('context_noise',ctxNo),('context_memory',ctxMe),('context_total',ctxDr+ctxNo+ctxMe)]: print(name,repr(value))
print('inner_moments',i)
print('outer_moments',o)
```

Observed output:

```text
kappa 0.39429449039784104
a 0.4644029024482682
b 0.300203812004187
T 0.6365445624738773
S -0.46647593302905754
D 0.048505627020709596
B0 -0.12957664201724725
bit_drift 0.06644492877718391
bit_noise 0.02228613542900998
bit_memory 0.012159152962622993
bit_total 0.10089021716881688
context_drift -0.009172270491556986
context_noise -0.010166441105147318
context_memory -0.008631668091609864
context_total -0.02797037968831417
inner_moments {1: 0.605705509602159, 2: 0.4644029024482682, 3: 0.38935194944722146, 4: 0.3415092073166637, 5: 0.3077260201223371, 6: 0.2822723630638548}
outer_moments {1: 0.7635495895007041, 2: 0.6365445624738773, 3: 0.5558832432820076, 4: 0.499261938993351, 5: 0.45683733634031665, 6: 0.4235722328699151}
```

## 8. Claim status and remaining checks

The exact formulas (1.1)--(2.5) and the coefficient derivation are
author-derived, with every term included. The polynomial reduction and the
executed scalar quadrature agree on the stated signs. This is not yet an
independent mathematical audit of the derivation and not a rigorous sign
certificate. No further integral run was performed after the supervisor
reserved certification for the root agent.

If rigorous enclosures make
\(\mathfrak D_1+\mathfrak N_1+\mathfrak M_1>0\) and
\(\mathfrak D_0+\mathfrak N_0+\mathfrak M_0<0\), (4.7) and (5.4)
prove the signs for all sufficiently small positive fixed
\(\varepsilon\). Under twice-continuous differentiability of the actual
population feature energies in \(s\), their first derivatives vanish at
zero, so the bit energies strictly increase and the context energy strictly
decreases on some nonempty initial interval. This final time implication
uses continuity of the second derivative; it is not an identification of a
formal series with a trajectory.

The first layer and readout coefficient are outside this note's assignment.
The bit-label correlations vanish exactly:
\(\frac14\sum_{\sigma,\tau}(\sigma\tau)\sigma
=\frac14\sum_{\sigma,\tau}(\sigma\tau)\tau=0\).
Thus the potential positive bit acceleration is a nonlinear learned-feature
effect rather than a direct nonzero primitive-bit label correlation. No
comparison with optimal frozen-feature prediction or global generalization
performance is inferred from it.
