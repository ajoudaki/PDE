# Quartic-flat gate: polynomial response for the pure tangent channel

This note proves a response theorem for an isolated equation on
\(\mathbb R^2\), globally in signed driver time. It also gives an exact
counterexample to extending its uniformity to arbitrary common forcing.
It does not prove a coupled-network theorem or change the activation in
the angle-specific arctangent theorem under review. No existing proof
file is modified. No agents or experiments are used.
The polynomial theorem is for the tangent system only; section 9 verifies
that an angle-uniform polynomial extension fails already on \(M_0=0\).

The proof uses the inverse-square invariant to control orbit derivatives,
then differentiates the clock to obtain derivatives at fixed driver time.
The exceptional orbit \(M_0=0\) is treated directly. The last sections
identify the actual common forcing and distinguish initial-state response
from response to a late injection.

## 1. Activation and theorem

Fix one constant \(e>0\), for example \(e=1/10\), throughout. Define
\[
 A(z)=\int_0^z\frac{du}{1+u^4},\qquad
 \phi(z)=1+z+eA(z),\qquad L=1+e,
\]
\[
 a(z)=\phi'(z)=1+\frac e{1+z^4},\qquad
 b(z)=\phi''(z)=-\frac{4ez^3}{(1+z^4)^2},\qquad
 F(s)=(1+s)(1+s+e)\quad(s\ge0).
\]
Thus expressions below use \(F(M^4)\), with the argument convention
fixed by this definition.

The function \(A\) is odd, smooth, bounded, and nonaffine. In fact
\[
 |A(z)|\le\int_0^1du+\int_1^\infty u^{-4}du=\frac43.
\]
All its derivatives of positive order are bounded: if
\(g(z)=(1+z^4)^{-1}\), induction gives
\(g^{(k)}(z)=P_k(z)/(1+z^4)^{k+1}\), where \(P_k\) is a polynomial
of degree at most \(3k\). Differentiating this expression proves the
induction, and the degree bound implies decay at infinity. Continuity
then gives boundedness. Nonaffinity follows from the nonconstant
derivative \(A'(z)=(1+z^4)^{-1}\). Consequently \(\phi\) is a smooth
nonaffine function with bounded derivatives of every positive order and
a bounded perturbation of \(1+z\); \(\phi\) itself is unbounded. Also
\[
 1\le a\le L,\qquad |b(z)|\le4e,\qquad
 b'(z)=\frac{4ez^2(5z^4-3)}{(1+z^4)^3},
 \qquad b(0)=b'(0)=0.
\]
The bound on \(b\) follows by considering \(|z|\le1\) and
\(|z|\ge1\) separately.

Write \(\Psi_r(M_0,V_0)=(M(r),V(r))\) for the flow
\[
 M_r=Vb(M),\qquad V_r=a(M),\qquad
 \Psi_0(M_0,V_0)=(M_0,V_0),\qquad r\in\mathbb R.
 \tag{1}
\]
Let \(B=1+|M_0|+\sqrt e\,|V_0|\). Vector and operator norms are
Euclidean norms.

**Theorem.** The flow (1) is globally defined and \(C^1\) jointly in
\((r,M_0,V_0)\). There is a finite constant \(C_e\), depending only
on the fixed \(e>0\), such that
\[
 \sup_{r\in\mathbb R}|M(r)|^2\le M_0^2+eV_0^2,
 \tag{2}
\]
\[
 \sup_{r\in\mathbb R}
 \left(\|D_{(M_0,V_0)}\Psi_r\|+\|\partial_r\Psi_r\|\right)
 \le C_e B^{20}.
 \tag{3}
\]
In particular the proposed looser exponents 26 or 30 also work.
Initial-state derivatives in (3) hold the signed driver time fixed.

For every real \(q\in L^1_{\rm loc}([0,\infty))\), the system
\[
 \dot M=q(t)Vb(M),\qquad \dot V=q(t)a(M)
 \tag{4}
\]
has exactly one locally absolutely continuous solution, namely
\[
 X(t)=\Psi_{r(t)}(M_0,V_0),\qquad r(t)=\int_0^tq(s)\,ds.
 \tag{5}
\]
No sign or monotonicity condition on \(q\) is imposed.

For any jointly Gaussian initial pair with finite means and variances,
including singular covariance, the supremum in (3) has a finite
\(p\)-th moment for every finite \(p>0\). There is no condition
involving \(pe\), a contrast variance, or an arctangent exponent.
There is no uniform-in-driver bound on \(V(r)\) itself.

## 2. Global signed flow and the zero common coordinate

The vector field \(G(M,V)=(Vb(M),a(M))\) is smooth. Local existence
and uniqueness follow from the integral-map contraction on continuous
paths in a closed ball: choose the interval length so that the field
bound times this length is smaller than the radius, and its Lipschitz
constant times this length is smaller than one. For either sign of \(r\),
every local solution satisfies
\[
 |V(r)|\le |V_0|+L|r|,
 \qquad
 |M(r)|\le |M_0|+4e|V_0||r|+2eLr^2.
 \tag{6}
\]
These follow by integrating the bounds on \(a,b\); the second uses
\(\int_0^{|r|}(|V_0|+Ls)ds\). Thus no solution can escape a bounded
set in finite driver time. At a hypothetical finite endpoint, the
bounded field makes the solution have a limit, and local existence
from that limit extends it. This proves global existence.

For completeness, the smooth-dependence result needed here is: a
\(C^1\) vector field has a \(C^1\) local flow, and the derivative in
initial state solves \(J_r=DG(X(r))J\), \(J(0)=I_2\), as long as
the solution exists. Here (6) supplies a common compact containing set
for nearby initial states on any bounded driver interval. On this set,
Taylor's formula for \(G\) has a remainder uniform in the base point.
Subtracting the integral equations for a difference quotient and the
linear variational equation, the remainder tends uniformly to zero;
the integral inequality with the finite bound on \(DG\) then gives
convergence of the difference quotients and continuity of the
derivative. This verifies the hypotheses and yields the stated global
\(C^1\) dependence by covering bounded intervals. It does not assume
the uniform estimate (3).

Since \(V_r\ge1\), \(r\mapsto V(r)\) is strictly increasing and
onto \(\mathbb R\): \(V(r)\ge V_0+r\) for \(r\ge0\), and
\(V(r)\le V_0+r\) for \(r\le0\). Each orbit therefore passes
through \(V=0\) exactly once.

At \(M_0=0\), uniqueness gives the exact flow
\[
 \Psi_r(0,V_0)=(0,V_0+Lr).
\]
Its full initial-state Jacobian, including transverse perturbations,
is obtained from
\[
 DG(M,V)=\begin{pmatrix}Vb'(M)&b(M)\\ b(M)&0\end{pmatrix}.
\]
This matrix is zero along \(M=0\), so
\[
 D\Psi_r(0,V_0)=I_2,\qquad
 \partial_r\Psi_r(0,V_0)=(0,L)
 \quad\hbox{for every }r,V_0\in\mathbb R.
 \tag{7}
\]
In particular there is no exponential common-coordinate entry on this
orbit. We will not assign a value to the singular invariant at zero.

## 3. Invariant, excursion, and orbit envelope

Suppose \(M_0\ne0\). Along a solution,
\[
 M_r=\left[-\frac{4eVM^2}{(1+M^4)^2}\right]M.
\]
The bracket is continuous on compact driver intervals, so the
exponential formula for this scalar linear equation shows that \(M\)
never vanishes in finite driver time and keeps the sign of \(M_0\).

On either open half-line define
\[
 \Lambda(M)=-\frac{L}{4eM^2}
       +\frac{2+e}{4e}M^2+\frac{M^6}{12e}.
\]
Direct differentiation and multiplication give
\[
 \Lambda'(M)=\frac{L+(2+e)M^4+M^8}{2eM^3}
            =\frac{F(M^4)}{2eM^3}=-\frac{2a(M)}{b(M)},
\]
\[
 \frac d{dr}\{V^2+\Lambda(M)\}
 =2Va(M)+\Lambda'(M)Vb(M)=0.
\]
Hence the exact invariant is
\[
 V^2+\Lambda(M)=V_0^2+\Lambda(M_0).
 \tag{8}
\]
The function \(\Lambda\) is even, strictly increasing on
\((0,\infty)\), and has limits \(-\infty\) at zero and
\(+\infty\) at infinity. Consequently (8) uniquely specifies the
common coordinate \(m(v;M_0,V_0)\) of the sign of \(M_0\) for
every real contrast \(v\). This is the actual orbit coordinate,
since the flow traverses every contrast. Its dependence on \(v\)
is through \(Y=v^2\). Put \(Y_0=V_0^2\).

Differentiation of (8) in \(Y\) gives
\[
 m_Y=f(m):=-\frac{2em^3}{F(m^4)},\qquad m(Y_0)=M_0.
 \tag{9}
\]
For \(X=m^2>0\),
\[
 X_Y=-\frac{4eX^2}{(1+X^2)(1+X^2+e)}\in[-e,0].
 \tag{10}
\]
Indeed the denominator is at least \((1+X^2)^2\ge4X^2\).
Let \(m_c=m(0;M_0,V_0)\) and \(c=|m_c|>0\). Integrating (10)
from 0 to \(Y_0\) proves
\[
 |m(v)|\le c,\qquad c^2\le M_0^2+eV_0^2\le B^2.
 \tag{11}
\]
This proves (2), including negative common coordinates; the zero case
was already treated directly.

The invariant between contrasts zero and \(V_0\) gives
\[
 V_0^2=\Lambda(m_c)-\Lambda(M_0)
 =\frac L{4e}\left(\frac1{M_0^2}-\frac1{c^2}\right)
 +\frac{2+e}{4e}(c^2-M_0^2)
 +\frac{c^6-M_0^6}{12e}.
\]
All three terms are nonnegative by (11). Multiplying the inequality
obtained by retaining the first term by \(4ec^2/L\) yields
\[
 \left(\frac c{|M_0|}\right)^2
 \le1+\frac{4eV_0^2c^2}{L}\le1+\frac4L B^4.
 \tag{12}
\]
This is the polynomial replacement for the logarithmic-invariant
estimate of the arctangent gate.

Since \(F\) is increasing on \([0,\infty)\), (9) also implies
\[
 \frac d{dY}\frac1{m^2}=\frac{4e}{F(m^4)}
       \ge\frac{4e}{F(c^4)}.
\]
Integrating from zero and taking square roots gives the envelope
\[
 |m(v)|\le\frac{c}{\sqrt{1+\kappa v^2}},\qquad
 \kappa=\frac{4ec^2}{F(c^4)}>0.
 \tag{13}
\]
There is no integrable \(|m|\) envelope on a nonzero orbit. More
precisely, put \(H=V_0^2+\Lambda(M_0)\). As \(|v|\to\infty\),
\(\Lambda(m)=H-v^2\to-\infty\), so \(m\to0\), and (8) gives
\[
 v^2m^2=Hm^2+\frac L{4e}
       -\frac{2+e}{4e}m^4-\frac{m^8}{12e}\longrightarrow\frac L{4e}.
 \tag{14}
\]
Thus \(|m(v)|\sim\sqrt L/(2\sqrt e\,|v|)\), and
\(\int_{\mathbb R}|m(v)|dv=\infty\) for \(M_0\ne0\).
Only integrable higher powers will be used.

## 4. Orbit derivatives at fixed terminal contrast

In this section derivatives of \(m\) hold terminal contrast \(v\)
fixed. The implicit function theorem applies on each sign branch since
\(\Lambda'(m)\ne0\). Differentiating (8) gives the exact identities
\[
 J:=m_{M_0}=\frac{\Lambda'(M_0)}{\Lambda'(m)}
   =\frac{f(m)}{f(M_0)}
   =\left(\frac m{M_0}\right)^3\frac{F(M_0^4)}{F(m^4)}>0,
 \tag{15}
\]
\[
 m_{V_0}=-2V_0f(m),\qquad m_v=2vf(m).
 \tag{16}
\]
For example, \(\Lambda'(m)m_{V_0}=2V_0\) and
\(1/\Lambda'(m)=-f(m)\); this checks the sign in the first formula
of (16). These formulas require no division by \(v\) or \(V_0\).

Introduce constants depending only on \(e\):
\[
 K=2(2+e),\qquad \rho=\sqrt{1+4/L},\qquad
 j=K/L+\rho^3,\qquad I=\sqrt{K/e}.
 \tag{17}
\]
Because \(B\ge1\) and \(c\le B\),
\[
 F(c^4)\le K B^8,\qquad
 F(M_0^4)\le K B^8,\qquad c/|M_0|\le\rho B^2.
\]
For \(Y\ge Y_0\), \(|m|\le|M_0|\), so (15) gives
\[
 0<J\le F(M_0^4)/L\le (K/L)B^8.
\]
For \(0\le Y\le Y_0\), \(|M_0|\le|m|\le c\). In this direction
\(F(M_0^4)/F(m^4)\le1\), so
\[
 0<J\le(c/|M_0|)^3\le\rho^3 B^6.
\]
Therefore
\[
 \sup_{v\in\mathbb R}|m_{M_0}(v)|\le jB^8=:J_*.
 \tag{18}
\]
If one bounds the denominator in (15) merely by \(L\), the backward
estimate is instead \((K\rho^3/L)B^{14}\), as proposed. That estimate
is valid; the monotonicity observation above improves it to \(B^6\).

We next record every orbit integral needed by the clock. From (13),
the substitution \(t=\sqrt\kappa v\), and
\(\int_{\mathbb R}(1+t^2)^{-3/2}dt=2\) (the antiderivative is
\(t/\sqrt{1+t^2}\)),
\[
 \int_{\mathbb R}|m(v)|^3dv
 \le\frac{2c^3}{\sqrt\kappa}
 =\frac{c^2\sqrt{F(c^4)}}{\sqrt e}\le I B^6.
 \tag{19}
\]
Using \(|m|^6\le c^3|m|^3\), and using
\(t/(1+t^2)^{3/2}\le1\) for \(t\ge0\), respectively, gives
\[
 \int_{\mathbb R}|m(v)|^6dv
 \le\frac{c^5\sqrt{F(c^4)}}{\sqrt e}\le I B^9,
\]
\[
 \sup_v |v|\,|m(v)|^3
 \le\frac{c^3}{\sqrt\kappa}
 =\frac{c^2\sqrt{F(c^4)}}{2\sqrt e}\le I B^6.
 \tag{20}
\]
These upper bounds have no negative power of \(c\), despite the
intermediate occurrence of \(\sqrt\kappa\) in denominators.

Since \(F\ge L\), \(|f(m)|\le(2e/L)|m|^3\). Define
\[
 d=\frac{4\sqrt e}{L},\qquad h=\frac{4eI}{L}.
\]
Equations (11), (16), (20), and \(|V_0|\le B/\sqrt e\) imply
\[
 \sup_v|m_{V_0}|\le dB^4,\qquad
 \sup_v|m_v|\le hB^6.
 \tag{21}
\]

## 5. The clock and all four fixed-driver derivatives

Since \(V_r=a(M)>0\), the exact signed clock is
\[
 r=\int_{V_0}^{V(r)}\frac{dv}{a(m(v;M_0,V_0))}.
 \tag{22}
\]
Its derivative in terminal \(V\) is \(1/a(m(V))\in[1/L,1]\), so
it has an everywhere nonzero derivative. For finite \(r\), this is a
finite integral of a continuously differentiable integrand when
\(M_0\ne0\). Differentiation in parameters is therefore legitimate.
No improper integral is differentiated: (19)--(20) are only subsequent
upper bounds on the resulting finite signed integrals.

Subscripts on \(M(r),V(r)\) now denote derivatives at fixed \(r\).
Differentiating (22), including the moving lower endpoint for \(V_0\),
gives
\[
 V_{M_0}=a(m(V))\int_{V_0}^V
       \frac{b(m(v))m_{M_0}(v)}{a(m(v))^2}\,dv,
 \tag{23}
\]
\[
 V_{V_0}=\frac{a(m(V))}{a(M_0)}
       +a(m(V))\int_{V_0}^V
       \frac{b(m(v))m_{V_0}(v)}{a(m(v))^2}\,dv.
 \tag{24}
\]
In (24), \(m(V_0;M_0,V_0)=M_0\) supplies the endpoint term.
Both formulas remain valid for \(V<V_0\) with the indicated oriented
integrals.

Define two further constants
\[
 k=4eLI,\qquad \ell=L+16e^{3/2}I.
\]
Using \(|b(m)|\le4e|m|^3\), \(1\le a\le L\), (18), and (19)
in (23) gives
\[
 |V_{M_0}|\le4eLJ_*\int_{\mathbb R}|m|^3dv
       \le kB^6J_*=kjB^{14}.
 \tag{25}
\]
For (24), the sharper pointwise version of (16) gives
\[
 |b(m)m_{V_0}|\le\frac{16e^2}{L}|V_0|\,|m|^6.
\]
After multiplication by the terminal factor at most \(L\), (20)
and \(|V_0|\le B/\sqrt e\) show that the integral contribution is
at most \(16e^{3/2}I B^{10}\). The endpoint term is at most \(L\).
Thus
\[
 |V_{V_0}|\le \ell B^{10}.
 \tag{26}
\]

The common-coordinate derivatives require the terminal-contrast chain
rule; an orbit derivative alone would not suffice:
\[
 M_{M_0}=m_{M_0}(V)+m_v(V)V_{M_0},\qquad
 M_{V_0}=m_{V_0}(V)+m_v(V)V_{V_0}.
 \tag{27}
\]
Combining (18), (21), (25), and (26), and using \(B\ge1\), yields
\[
 |M_{M_0}|\le J_*+hB^6 kB^6J_*
       \le(1+hk)jB^{20},
\]
\[
 |M_{V_0}|\le dB^4+hB^6\ell B^{10}
       \le(d+h\ell)B^{16}.
 \tag{28}
\]
These estimates bound all four initial-state entries at fixed signed
driver time, uniformly over every terminal contrast.

Finally, the driver derivative is the vector field itself. Equations
(20) and \(a\le L\) give
\[
 \|\partial_r\Psi_r\|
 \le |Vb(M)|+a(M)
 \le4eI B^6+L\le(L+4eI)B^6.
 \tag{29}
\]
One explicit admissible constant in (3) is
\[
 C_e=(1+hk)j+kj+(d+h\ell)+\ell+L+4eI.
 \tag{30}
\]
Indeed the operator norm is at most the sum of the absolute values of
the four entries, and every exponent in (25)--(29) is at most 20.
All constants are finite for every fixed \(e>0\); uniformity as
\(e\downarrow0\) is not asserted. Formula (7) gives a sum of norms
\(1+L\) at \(M_0=0\), which is smaller than (30). This completes
the deterministic bound (3) on the whole plane.

## 6. Signed L1 composition, driver differentiation, and Gaussian moments

For \(q\in L^1_{\rm loc}\), \(r(t)=\int_0^tq\) is locally
absolutely continuous and has compact image on every finite interval.
The chain rule for an absolutely continuous scalar function composed
with a \(C^1\) function applies on this compact image and proves
(4)--(5) almost everywhere. For uniqueness on a compact physical-time
interval, two candidate continuous paths lie in a common ball. A
Lipschitz constant \(K_0\) for \(G\) there gives
\[
 |X(t)-\widetilde X(t)|
 \le K_0\int_0^t|q(s)|\,|X(s)-\widetilde X(s)|\,ds.
\]
Partition the interval into finitely many pieces with
\(K_0\int|q|<1\) on each piece. Taking a supremum on the first
piece forces equality, and induction does so on every piece. This
proves uniqueness without requiring a monotone \(r(t)\).

On each finite interval \([0,T]\), the solution map
\[
 (x_0,q)\longmapsto\big[t\mapsto\Psi_{\int_0^tq}(x_0)\big]
 \quad\text{from }\mathbb R^2\times L^1[0,T]
 \text{ to }C([0,T];\mathbb R^2)
\]
is continuously differentiable. To justify this assertion, integration
is a bounded linear map from \(L^1\) to \(C\), with norm at most
one. The arguments of \(\Psi\) for a fixed base point and its small
perturbations lie in a compact subset of \(\mathbb R^3\). Uniform
continuity of the derivative of \(\Psi\) on that compact set gives
a Taylor remainder that is uniformly small relative to the increment,
which proves differentiability into \(C\) and continuity of the
derivative. Its exact value is
\[
 \delta X(t)=D\Psi_{r(t)}(x_0)\,\delta x_0
    +\partial_r\Psi_{r(t)}(x_0)\int_0^t\delta q(s)\,ds,
\]
\[
 \sup_{t\le T}|\delta X(t)|
 \le C_e B^{20}\big(|\delta x_0|+\|\delta q\|_{L^1[0,T]}\big).
 \tag{31}
\]
The bound is independent of the realized driver and of \(T\).
If \(q\) is selected from another trajectory or randomness, the
fixed-driver derivatives remain pathwise valid. Differentiating the
selection rule requires its differentiability into \(L^1\); when that
holds, (31) is the chain rule and still leaves \(\delta q\) to be
estimated. It does not control the selection rule itself.

Let \(S(x_0)\) denote the supremum in (3). It is measurable because
continuity in \(r\) allows the same supremum over rational \(r\).
For any \(p>0\),
\[
 S(M_0,V_0)^p\le C_e^p(1+|M_0|+\sqrt e|V_0|)^{20p}.
\]
For \(s>0\), a power of a sum of three nonnegative numbers is at
most \(3^{\max(s-1,0)}\) times the sum of their \(s\)-th powers.
Every scalar Gaussian with finite variance has every positive absolute
moment: for positive variance this follows by integrating a polynomial
power against its Gaussian density; zero variance is a constant.
Apply the sum inequality with \(s=20p\) to the two Gaussian marginals.
This proves \(\mathbb E S^p<\infty\) without independence,
nondegeneracy, or a restriction on \(p\). It also bounds the random
operator norm in (31) in every finite moment. Uniform moments of the
state \(V\), or of uncontrolled input derivatives, are not implied.

## 7. The actual common forcing and its invariant defect

The local tangent pair with both incoming adjoints has equations
\[
 \dot M=a(M)p+Vb(M)q,\qquad \dot V=a(M)q.
 \tag{32}
\]
Here \(p\) is the incoming adjoint to the common activation
\(h=\phi(M)\), and \(q\) is the incoming adjoint to the contrast
activation \(k=a(M)V\). Indeed
\[
 dh=a(M)dM,\qquad dk=b(M)VdM+a(M)dV,
\]
so their preactivation adjoints are
\[
 P=a(M)p+b(M)Vq,\qquad Q=a(M)q.
 \tag{33}
\]

The additional \(p\) is generated by the actual upper-layer
derivatives. To make this precise without population regularity
assumptions, consider finite-dimensional coordinatewise activations,
operators \(U,W\), readout \(C\), and the tangent objective
\[
 h_\ell=\phi(M_\ell),\quad k_\ell=a(M_\ell)V_\ell,
 \quad (M_2,V_2)=(Uh_1,Uk_1),
 \quad (M_3,V_3)=(Wh_2,Wk_2),
 \quad G=\langle C,k_3\rangle.
\]
Products of fields below are coordinatewise. The chain rule (33) and
the definition of transpose give
\[
 p_3=0,\ q_3=C,\quad
 p_2=W^*[Cb(M_3)V_3],\quad q_2=W^*[Ca(M_3)],
\]
\[
 p_1=U^*\left[
    a(M_2)W^*[Cb(M_3)V_3]
   +b(M_2)V_2W^*[Ca(M_3)]\right],
\]
\[
 q_1=U^*\left[a(M_2)W^*[Ca(M_3)]\right].
 \tag{34}
\]
Under Euclidean gradient ascent of \(G\), the bottom pair is exactly
(32) with \(p=p_1,q=q_1\); any common scalar loss factor can be
absorbed in these drivers. These identities follow by differentiating
the displayed maps and do not assume an angle limit of dynamics.
For population fields their use additionally requires the displayed
products and adjoint actions to be defined in the chosen spaces.

There is no algebraic factorization forcing \(p_1\) to vanish with
\(M_1\). For a scalar example, take \(U=W=C=1\), \(M_1=0\),
and \(V_1=1\). Then \(M_2=1\), \(V_2=L\),
\(M_3=\phi(1)>0\), and \(V_3=a(1)L>0\). Since \(b(z)<0\)
for \(z>0\), both terms in the formula for \(p_1\) in (34) are
strictly negative. Thus \(p_1<0\) although \(M_1=0\).

On an interval where \(M\ne0\), differentiating the invariant under
(32) cancels the two \(q\) terms and leaves the exact defect
\[
 \frac d{dt}\{V^2+\Lambda(M)\}
 =\Lambda'(M)a(M)p
 =\frac{(1+M^4+e)^2}{2eM^3}\,p.
 \tag{35}
\]
Its coefficient behaves as \(L^2/(2eM^3)\) near zero. No bound or
vanishing of \(p\) sufficient to absorb this singularity follows
from (34). A nonzero \(p\) can move \(M\) through zero, and (35)
is not an identity across such a crossing. This is a defect of this
invariant method, not a singularity of the smooth equation (32).

For example, prescribed \(p,q\in L^1_{\rm loc}\) still give global
finite-horizon existence and uniqueness for (32). With
\(P_t=\int_0^t|p|\) and \(Q_t=\int_0^t|q|\), integration yields
\[
 |V(t)|\le|V_0|+LQ_t,
 \qquad
 |M(t)|\le|M_0|+LP_t+4e|V_0|Q_t+2eLQ_t^2.
\]
Here \(\int_0^tQ_s|q(s)|ds=Q_t^2/2\). Local integral-map
contraction uses the integrable Lipschitz majorant
\(K_0(|p|+|q|)\) on a containing ball, and the displayed bounds
allow continuation. Such existence does not give a uniform response
estimate for the coupled forcing.

Trained operators also produce additional terms at upper layers, for
example
\[
 \dot M_2=\dot U h_1+U[a(M_1)\dot M_1],
 \qquad
 \dot V_2=\dot U k_1+
 U[b(M_1)V_1\dot M_1+a(M_1)\dot V_1],
\]
and the corresponding formulas with \(W\) at layer 3. Thus even
\(p_3=0\) does not identify the moving top preactivation with an
isolated copy of (1).

## 8. Late common injections: identity at zero, cubic growth off zero

Consider the first variation of (32) about \(p=0\), with fixed \(q\)
and initial state, in a prescribed direction \(\eta\in L^1[0,T]\)
for \(p\). The variational equation is
\[
 \dot{\delta X}=q(t)DG(X(t))\delta X
                   +(a(M(t))\eta(t),0),\qquad \delta X(0)=0.
\]
The flow property implies that its homogeneous propagator from \(s\)
to \(t\) is
\[
 K(t,s)=D\Psi_{r(t)-r(s)}(X(s)).
\]
Indeed differentiating in \(t\) gives
\(\partial_tK=q(t)DG(X(t))K\) almost everywhere and \(K(s,s)=I_2\).
The coefficients are integrable on finite intervals. Differentiating
the following integral therefore verifies variation of constants:
\[
 \delta X(t)=\int_0^t
 D\Psi_{r(t)-r(s)}(X(s))\,(a(M(s))\eta(s),0)\,ds.
 \tag{36}
\]
The theorem bounds this propagator polynomially in the reached state,
\[
 \|K(t,s)\|\le
 C_e\big(1+|M(s)|+\sqrt e\,|V(s)|\big)^{20}.
 \tag{37}
\]
It does not replace the reached contrast in (37) by the original \(B\).

If \(M_0=0\), the base orbit has \(M(t)=0\), and (7) gives
\(K(t,s)=I_2\) for all \(s,t\), regardless of \(q\). Consequently
\[
 \delta X(t)=\left(L\int_0^t\eta(s)ds,\,0\right).
 \tag{38}
\]
This is the exact linear common-forcing response at the zero orbit.
There is no arctangent-type exponential amplification there.

For nonzero common initial state, however, a propagator uniform over
all drivers cannot be bounded by the original \(B\). Fix \(c>0\)
and start at \(x_*=(c,0)\). For \(R>0\), let
\(x_R=(m_R,R)\) be the reached state on this orbit, and let
\(r_R>0\) be its driver time. Equations (8) and (22) give
\[
 R^2+\Lambda(m_R)=\Lambda(c),\qquad
 R/L\le r_R\le R,\qquad 0<m_R\le c.
\]
Freeze \(r_R\) at this nominal value when differentiating the return
map \(\Psi_{-r_R}\) at \(x_R\). Its terminal contrast is zero.
The terminal chain term in (27) vanishes because \(m_v=2vf(m)=0\)
there. Thus its common-to-common entry is exactly
\[
 \left.\partial_{M_{\rm in}}
 [\Psi_{-r_R}(M_{\rm in},V_{\rm in})]_M\right|_{x_R}
 =\frac{f(c)}{f(m_R)}
 =\left(\frac c{m_R}\right)^3\frac{F(m_R^4)}{F(c^4)}.
 \tag{39}
\]
Equation (14) on this orbit gives
\(Rm_R\to\sqrt L/(2\sqrt e)\). Since \(F(m_R^4)\to L\),
\[
 \frac{f(c)}{f(m_R)}
 \sim \frac{8e^{3/2}c^3}{\sqrt L\,F(c^4)}\,R^3
 \longrightarrow\infty.
 \tag{40}
\]
This is polynomial, rather than the exponential zero-orbit return
response of the arctangent gate, but it is still unbounded with fixed
original \(B=1+c\).

The example can be realized by an ordinary unit-\(L^1\) common
forcing, without an impulsive distribution. On the fixed physical
interval \([0,3]\), set
\[
 q_R(t)=
 \begin{cases}
 r_R,&0\le t<1,\\
 0,&1\le t<2,\\
 -r_R,&2\le t\le3,
 \end{cases}
 \qquad p_\varepsilon(t)=\varepsilon\,\mathbf1_{[1,2]}(t).
\]
At \(\varepsilon=0\), the path reaches \(x_R\), pauses for one
unit of time, and returns to \(x_*\). During the pause its first
variation is exactly \((a(m_R),0)\). Applying the return map gives
\[
 \left.\frac d{d\varepsilon}M_\varepsilon(3)
                  \right|_{\varepsilon=0}
 =a(m_R)\frac{f(c)}{f(m_R)}
 \sim\frac{8e^{3/2}c^3\sqrt L}{F(c^4)}R^3.
 \tag{41}
\]
The forcing direction has \(L^1\) norm one for every \(R\), whereas
the response diverges. Therefore no estimate depending only on the
original initial state can bound the derivative with respect to an
arbitrary common \(L^1\) forcing uniformly over signed \(q\), even
at \(p=0\) and on this fixed physical interval. This does not exclude
an estimate with explicit dependence on the driver size or one using
additional structure of the actual network forcing.

There is no contradiction with (3): for the original initial-state
derivative, the outward and return derivatives multiply to
\(D\Psi_0(x_*)=I_2\). A perturbation introduced during the pause has
not undergone the outward response. A driver perturbation also has a
different direction: differentiating the autonomous flow identity gives
\(D\Psi_{r(t)-r(s)}(X(s))G(X(s))=G(X(t))\), which is precisely the
cancellation behind (31), and does not hold with \((a(M(s)),0)\)
in place of \(G(X(s))\).

## 9. Finite-angle caveat: an exact loss of angle-uniform polynomial control

Fix \(0<\delta<1\) and \(\mu^2=1-\delta^2\). The pure contrast
equation at finite angle has
\[
 a_\delta(M,V)=\frac{a(M+\delta V)+a(M-\delta V)}2,
 \qquad
 b_\delta(M,V)=\frac{a(M+\delta V)-a(M-\delta V)}{2\delta},
\]
\[
 M_r=\mu^2 b_\delta(M,V),\qquad V_r=a_\delta(M,V).
 \tag{42}
\]
Taking the difference of the two rational functions in \(b_\delta\)
and using
\((M-\delta V)^4-(M+\delta V)^4
 =-8M\delta V(M^2+\delta^2V^2)\) gives exactly
\[
 b_\delta(M,V)=
 -\frac{4eMV(M^2+\delta^2V^2)}
 {[1+(M+\delta V)^4][1+(M-\delta V)^4]}.
 \tag{43}
\]
For each fixed \(\delta>0\), the vector field in (42) is smooth and
bounded, since \(1\le a_\delta\le L\) and
\(|b_\delta|\le e/(2\delta)\). Thus it has a global \(C^1\) flow
\(\Psi_r^\delta\), by the same local construction and continuation
argument as above.

At \(M_0=0\), the orbit stays on zero and
\[
 V_r=\alpha_\delta(V):=1+\frac e{1+\delta^4V^4},\qquad
 \partial_M b_\delta(0,V)
 =-\frac{4e\delta^2V^3}{(1+\delta^4V^4)^2}
 =\frac{\alpha_\delta'(V)}{\delta^2}.
\]
Also \(\partial_V b_\delta(0,V)=0\) and
\(\partial_M a_\delta(0,V)=0\). Hence the linearized system is
diagonal. The common entry \(J_\delta\), at fixed driver time,
satisfies
\[
 \frac d{dr}\log J_\delta
 =\frac{\mu^2}{\delta^2}\alpha_\delta'(V),\qquad
 J_\delta(0)=1.
\]
Dividing by \(V_r=\alpha_\delta(V)>0\) and integrating yields
\[
 D\Psi_r^\delta(0,V_0)=
 \begin{pmatrix}
 [\alpha_\delta(V(r))/\alpha_\delta(V_0)]^{\mu^2/\delta^2}&0\\
 0&\alpha_\delta(V(r))/\alpha_\delta(V_0)
 \end{pmatrix}.
 \tag{44}
\]
Since \(V\) traverses all real values and \(\alpha_\delta\) is
maximized at zero, the exact maximum common response is attained on
return to terminal contrast zero:
\[
 J_{\delta,\max}(V_0)
 :=\sup_r J_\delta(r;V_0)
 =\left[\frac{L}{\alpha_\delta(V_0)}\right]^{\mu^2/\delta^2}.
 \tag{45}
\]
For \(|V_0|>1\), choose \(\delta=1/|V_0|\). Then
\[
 \log J_{\delta,\max}(V_0)
 =(V_0^2-1)\log\frac{2L}{L+1}
 =:(V_0^2-1)\lambda_e,\qquad \lambda_e>0.
 \tag{46}
\]
With \(M_0=0\), \(B=1+\sqrt e|V_0|\); the exponential in (46)
eventually exceeds every constant times every fixed power of \(B\).
Thus (3) cannot hold with an angle-independent polynomial constant
and exponent for (42), even on the zero common orbit. This conclusion
uses fixed-driver Jacobians; it does not differentiate the choice
\(\delta=1/|V_0|\).

There is nevertheless the proposed angle-uniform exponential upper
bound for this zero-orbit response. If \(V_0\ne0\), put
\(u=\delta^2V_0^2>0\). Since \(\log(1+x)\le x\) for \(x\ge0\)
(integrate \((1+x)^{-1}\le1\)),
\[
 \log\frac{L(1+u^2)}{L+u^2}
 =\log\left(1+\frac{eu^2}{L+u^2}\right)
 \le\frac{eu^2}{L+u^2}.
\]
Using \(\mu^2\le1\), \(1/\delta^2=V_0^2/u\), and
\(L+u^2\ge2\sqrt L\,u\), (45) gives
\[
 0\le\log J_{\delta,\max}(V_0)
 \le\frac{eV_0^2u}{L+u^2}
 \le\frac{eV_0^2}{2\sqrt L}.
 \tag{47}
\]
For \(V_0=0\) the same bound holds since \(J_{\delta,\max}=1\).

In particular, for Gaussian \(V_0\) with variance \(\sigma^2>0\),
\[
 \mathbb E\left[\left(\sup_{0<\delta<1}
                J_{\delta,\max}(V_0)\right)^p\right]
 <\infty\qquad\text{if }pe\sigma^2<\sqrt{1+e}.
 \tag{48}
\]
Here the expectation is of the \(p\)-th power of the supremum.
To verify the threshold, raise (47) to an exponential and multiply by
the Gaussian density. The coefficient of \(v^2\) in the exponent is
\(pe/(2\sqrt L)-1/(2\sigma^2)<0\); a nonzero finite Gaussian mean
adds only a linear term. Measurability of the supremum follows by
continuity in \(\delta\) and restriction to rational \(\delta\).
The other diagonal entry in (44) and the driver derivative on this
orbit are bounded by \(L\), so the same sufficient threshold also
controls the complete zero-orbit response. For example, \(e=1/10\),
\(\sigma^2=1\), and \(p=4\) satisfy it.

This is a sufficient threshold, not an optimal one. Conversely, for
centered Gaussian \(V_0\) of positive variance, (46) implies that
the angle supremum has infinite \(p\)-th moment whenever
\(p\lambda_e\ge1/(2\sigma^2)\), including equality. This follows
by integrating its lower bound
\(\exp[p\lambda_e(V_0^2-1)]\) on \(|V_0|>1\) against the Gaussian
density. Thus angle-uniform moments of every order are false.

For each fixed positive \(\delta\), in contrast,
\(J_{\delta,\max}\le L^{\mu^2/\delta^2}\), so this particular
zero-orbit response does have all moments at that fixed angle. What
fails is the polynomial estimate and all-order moment control
uniformly over angles. At fixed \(V_0\), (47)'s preceding bound
\(eV_0^2u/(L+u^2)\) tends to zero as \(\delta\to0\), consistently
with the exact tangent identity (7). None of these finite-angle
zero-orbit calculations proves response bounds for arbitrary nonzero
common states or for the coupled common forcing.

The established result is the tangent pure-channel, fixed-driver initial-state
and driver response theorem with a polynomial \(B^{20}\) bound and
all finite Gaussian moments for one fixed \(e>0\). The unresolved
network work is to control the actual \(p\), its source derivatives,
the driver-selection derivatives, and the trained-operator transport
terms. Equations (35) and (41) show why the local theorem alone does
not supply those bounds. No full-network closure, angle-limit transfer,
cutoff removal, or modification of the original arctangent theorem is
claimed.
