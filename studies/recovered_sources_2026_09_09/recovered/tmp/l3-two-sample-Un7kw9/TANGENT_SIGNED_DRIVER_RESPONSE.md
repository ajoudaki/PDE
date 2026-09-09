# Tangent contrast with a signed driver: complete local response candidate

Status: **complete candidate proof of a local two-dimensional flow and
response theorem; fresh independent audit required**. This is not a
universal-activation theorem for the coupled three-hidden-layer network.
Section 8 derives the additional network forcing and identifies its
canonical backward source channel without claiming to control it.

This file is separate from the frozen `UNIVERSAL_ANGLE_ROUTE.md`, whose
SHA-256 is
`20dbd9164881bf475ec5d684c43b4d122708338a145ae2934b70b3629ca46cdf`.
That file is not modified. The requested skills and required research
references were read during the preceding work. No experiment or agent
is used here. The result below is derived directly; no external
population-limit or response-continuation theorem is invoked.

## 1. Statement, conventions, and exact scope

Fix one number \(e>0\), and write
\[
 \phi(z)=1+z+e\arctan z,\qquad L=1+e,
 \qquad a(z)=\phi'(z)=1+\frac e{1+z^2},
 \qquad b(z)=\phi''(z)=-\frac{2ez}{(1+z^2)^2}.
                                                               \tag{1}
\]
The constant offset does not enter the local equation, but is retained
for consistency with the network candidate. For a real driver
\(q\in L^1_{\mathrm{loc}}([0,\infty))\), consider
\[
 \dot M(t)=q(t)V(t)b(M(t)),\qquad
 \dot V(t)=q(t)a(M(t)),\qquad (M(0),V(0))=(M_0,V_0).
                                                               \tag{2}
\]
The driver may have either sign, change sign arbitrarily, and be
selected using an external trajectory or randomness. For each such
selected driver the theorem is pathwise. In all initial-state
derivatives below the driver is held fixed. Derivatives of its selection
rule are excluded and are included only in the explicit chain rule in
section 7.

Let \(\Psi_r(M_0,V_0)\) be the flow of
\[
 \frac{dM}{dr}=Vb(M),\qquad \frac{dV}{dr}=a(M),
 \qquad \Psi_0(M_0,V_0)=(M_0,V_0).                    \tag{3}
\]
Here \(r\in\mathbb R\) is signed driver time, not physical or feature
time in the full network. Matrix norms below are Euclidean operator
norms; vector norms are Euclidean norms. Put
\[
 B=1+|M_0|+\sqrt e\,|V_0|,\qquad \gamma=\frac e{1+e}.
\]

**Local theorem.** The flow (3) is defined and continuously
differentiable in \((r,M_0,V_0)\) on all of \(\mathbb R^3\). Equation
(2) has exactly one locally absolutely continuous solution, given by
\[
 (M(t),V(t))=\Psi_{r(t)}(M_0,V_0),\qquad
 r(t)=\int_0^tq(s)ds.                                  \tag{4}
\]
It obeys
\[
 \sup_{r\in\mathbb R}|M(r)|^2\le M_0^2+(e/2)V_0^2,     \tag{5}
\]
and, for an explicit finite constant \(C_e\) defined in section 5,
\[
 \sup_{r\in\mathbb R}
 \left(\|D_{(M_0,V_0)}\Psi_r\|+\|\partial_r\Psi_r\|\right)
 \le C_e B^{10}\exp(\gamma V_0^2).                     \tag{6}
\]
Every entry of \(D\Psi_r\) in (6) is evaluated at fixed driver time
\(r\). The constant is independent of initial coordinates, elapsed
time, the terminal contrast, and the driver.

If \((M_0,V_0)\) is a centered jointly Gaussian pair with finite
variances and \(v=\operatorname{Var}(V_0)>0\), then the left side
of (6) has a finite \(p\)-th moment for every \(p>0\) satisfying
\[
 p\gamma v<\frac12.                                    \tag{7}
\]
Singular Gaussian covariances are permitted. If \(v=0\), all positive
moments are finite. For \(e=1/10\), \(v=1\), and \(p=4\), the strict
condition is \(4/11<1/2\), so it holds. Section 6 shows why equality
cannot be admitted in general.

The proof first constructs the global signed flow and its invariant,
then controls orbit derivatives at fixed contrast, and finally
differentiates the exact clock relation to obtain all four derivatives
at fixed driver. The last step is essential: an orbit derivative alone
is not the claimed response.

## 2. Global signed flow and locally integrable drivers

The vector field \((Vb(M),a(M))\) is smooth and locally Lipschitz on
\(\mathbb R^2\). Local existence and uniqueness can be obtained
directly by the integral-map contraction: on a closed ball around an
initial state, choose a time interval so that the vector-field bound
times its length is less than the ball radius, and its Lipschitz
constant times the length is less than one. The integral map is then
a contraction on continuous paths in that ball.

Since \(1\le a\le L\) and \(|b|\le2e\), every local solution satisfies
for either sign of \(r\)
\[
 |V(r)|\le |V_0|+L|r|,
 \qquad
 |M(r)|\le |M_0|+2e|V_0||r|+eLr^2.                    \tag{8}
\]
Thus its state stays in a bounded set on every bounded driver interval.
If a finite endpoint of a maximal interval existed, the vector field
would be bounded there, the path would have a limit at the endpoint,
and the same local construction at that limit would extend it. This
proves existence for every real \(r\).

On any fixed bounded driver interval, nearby initial states have a
common bounded containing set by (8). Taylor expansion of the smooth
vector field on that set, followed by the integral difference estimate,
shows that the initial-state difference quotients converge to the
solution of
\(J'=D(Vb(M),a(M))J\), \(J(0)=I\). The Taylor remainder is uniform
on the containing set and tends to zero with the initial increment;
the integral inequality for the remainder gives convergence after
multiplication by the finite factor \(\exp(K|r|)\), where \(K\) is a
bound on the field derivative on that set. The same argument gives
continuity of these derivatives. Consequently the global flow is
\(C^1\) in initial state and driver time. This local justification does
not supply, or assume, the uniform bound (6).

The strictly positive velocity \(V_r=a(M)\) implies that \(V(r)\) is
strictly increasing. For \(r\ge0\), \(V(r)\ge V_0+r\); for \(r\le0\),
\(V(r)\le V_0+r\). Therefore \(r\mapsto V(r)\) maps \(\mathbb R\)
onto \(\mathbb R\), and there is exactly one point on each orbit with
contrast zero.

For locally integrable \(q\), the function \(r(t)\) in (4) is locally
absolutely continuous and has bounded image on each compact time
interval. The chain rule for a \(C^1\) map composed with an absolutely
continuous scalar function proves (2) almost everywhere and its
integral equation. For uniqueness, two candidate paths are bounded on
a compact interval by continuity. A Lipschitz constant \(K\) for the
vector field on a common containing ball gives
\[
 |X(t)-\widetilde X(t)|
 \le K\int_0^t |q(s)|\,|X(s)-\widetilde X(s)|ds.
\]
An integrating factor, or iteration on subintervals with
\(K\int|q|<1\), makes this difference zero. This argument requires
neither a positive driver nor a monotone clock \(r(t)\).

## 3. Invariant, zero common coordinate, and orbit bounds

First suppose \(M_0\ne0\). On every compact driver interval,
\[
 M_r=-\frac{2eV}{(1+M^2)^2}M
\]
is a linear equation in \(M\) with a continuous coefficient evaluated
along the path. Its exponential integral formula shows that \(M\)
never vanishes at finite driver time and retains the sign of \(M_0\).

Define, on the two open half-lines,
\[
 \Lambda(M)=\frac{1+e}{e}\log|M|
       +\frac{2+e}{2e}M^2+\frac{M^4}{4e},\qquad
 F(X)=(1+X)(1+X+e).                                    \tag{9}
\]
Its derivative is
\[
 \Lambda'(M)=\frac{F(M^2)}{eM}
             =-\frac{2a(M)}{b(M)}.
\]
Multiplying (3) by these derivatives gives the exact invariant
\[
 V^2+\Lambda(M)=V_0^2+\Lambda(M_0).                    \tag{10}
\]
This involves no assumption on the sign of \(VM\) or of \(qV\).

On the positive half-line, \(\Lambda\) is strictly increasing, with
limits \(-\infty\) at zero and \(+\infty\) at infinity. Therefore,
for each real \(v\), (10) uniquely determines a common coordinate
\(m(v;M_0,V_0)\) of the sign of \(M_0\). This is the common
coordinate on the actual orbit at contrast \(v\), since that orbit
passes through every real contrast and satisfies (10). Its dependence
on \(v\) is through \(Y=v^2\). With \(Y_0=V_0^2\), differentiation
of (10) gives
\[
 \frac{dm}{dY}=f(m):=-\frac{em}{F(m^2)},\qquad m(Y_0)=M_0,
 \qquad
 \frac{d(m^2)}{dY}=-\frac{2e m^2}{F(m^2)}.             \tag{11}
\]
Since \(F(X)\ge(1+X)^2\ge4X\) for \(X\ge0\),
\[
 -e/2\le\frac{d(m^2)}{dY}\le0.
\]
Writing \(m_c=m(0;M_0,V_0)\), integration from \(0\) to \(V_0^2\)
yields
\[
 |m(v)|\le|m_c|,\qquad m_c^2\le M_0^2+(e/2)V_0^2.      \tag{12}
\]
This proves (5) for \(M_0\ne0\).

Because \(F\) is increasing on \([0,\infty)\), (11) also gives
\[
 \frac d{dY}\log|m|=-\frac e{F(m^2)}
                      \le-\frac e{F(m_c^2)}.
\]
Integrating from \(Y=0\) proves the deterministic orbit envelope
\[
 |m(v)|\le |m_c|\exp[-ev^2/F(m_c^2)].                  \tag{13}
\]

For \(M_0=0\), the exact flow and its initial-state derivatives are
\[
 \Psi_r(0,V_0)=(0,V_0+Lr),
\]
\[
 D\Psi_r(0,V_0)=
 \begin{pmatrix}
 \exp[-2eV_0r-eLr^2]&0\\0&1
 \end{pmatrix},\qquad \partial_r\Psi_r(0,V_0)=(0,L).   \tag{14}
\]
To verify the nontrivial entry, linearize the common equation along
this flow: \(J_r=-2e(V_0+Lr)J\), \(J(0)=1\). The other entries
follow because \(a'(0)=0\) and the common coordinate is identically
zero for every \(V_0\). Equivalently that entry equals
\[
 \exp\{\gamma[V_0^2-(V_0+Lr)^2]\}\le e^{\gamma V_0^2}.
                                                               \tag{15}
\]
This proves the zero-common-coordinate part directly, without assigning
a value to the logarithmic invariant at zero. Formula (5) is immediate
in this case.

## 4. Orbit derivatives at fixed terminal contrast

In this section assume \(M_0\ne0\). All derivatives of \(m(v;M_0,V_0)\)
with respect to initial coordinates hold the terminal contrast \(v\)
fixed. They will be converted to fixed-driver derivatives in section 5.

Let \(J(Y)=\partial_{M_0}m\) with \(Y_0\) fixed. The scalar variational
equation is \(J_Y=f'(m)J\), \(J(Y_0)=1\). Both \(J\) and
\(f(m)/f(M_0)\) solve this equation with the same initial value, since
\(f(M_0)\ne0\). For \(Y\ge Y_0\), (12) gives \(|m/M_0|\le1\), so
\[
 0<J(Y)=\frac{f(m)}{f(M_0)}
       =\frac m{M_0}\frac{F(M_0^2)}{F(m^2)}
       \le\frac{F(M_0^2)}L.                          \tag{16}
\]
For \(0\le Y\le Y_0\), differentiate the explicit expression for
\(f\). The derivative \(F'\) here is with respect to its nonnegative
argument:
\[
 f'(m)=-\frac e{F(m^2)}
       +\frac{2em^2F'(m^2)}{F(m^2)^2}\ge-\frac eL=-\gamma.
\]
Thus
\(\log J(Y)=-\int_Y^{Y_0}f'(m(u))du\le\gamma Y_0\). Combining both
directions,
\[
 \sup_{v\in\mathbb R}|m_{M_0}(v;M_0,V_0)|
 \le J_*:=\frac{F(M_0^2)}L+e^{\gamma V_0^2}.            \tag{17}
\]
This controls the complete signed integrated self-curvature in (11);
it has no dependence on the terminal \(Y\).

The other two derivatives follow directly by differentiating
\(v^2+\Lambda(m)=V_0^2+\Lambda(M_0)\):
\[
 m_{V_0}=-2V_0f(m),\qquad m_v=2vf(m).                 \tag{18}
\]
For example \(\Lambda'(m)m_{V_0}=2V_0\) and
\(1/\Lambda'(m)=-f(m)\). These identities also hold at \(v=0\) and
at \(V_0=0\). No division by either contrast coordinate is used.

## 5. All four Jacobian entries at fixed driver, with explicit constants

The following constants depend only on the fixed positive \(e\):
\[
 K=2(e+2),\qquad I=\sqrt{\pi K/e},\qquad
 j=1+K/L,\qquad h=2\gamma I,\qquad k=2eLI,
\]
\[
 d_*=2\sqrt e/L,\qquad \ell_*=L+4e^{3/2}I.
                                                               \tag{19}
\]
The symbol \(d_*\) is a numerical constant and is unrelated to the
input dimension in the network contract. From \(B\ge1\) and (12),
\[
 |m_c|\le B,\qquad F(m_c^2)\le K B^4,
 \qquad J_*\le jB^4e^{\gamma V_0^2}.                  \tag{20}
\]
Integration of (13), and maximization of \(|v|e^{-\alpha v^2}\), give
the following three explicit bounds:
\[
 \int_{\mathbb R}|m(v)|dv
 \le |m_c|\sqrt{\pi F(m_c^2)/e}\le I B^3,
\]
\[
 \int_{\mathbb R}m(v)^2dv
 \le m_c^2\sqrt{\pi F(m_c^2)/(2e)}\le I B^4,
\]
\[
 \sup_v|vm(v)|
 \le |m_c|\sqrt{F(m_c^2)/(2e\exp(1))}\le I B^3.        \tag{21}
\]
In particular (18), \(|f(m)|\le\gamma|m|\), and
\(|V_0|\le B/\sqrt e\) imply
\[
 \sup_v|m_{V_0}|\le d_*B^2,\qquad
 \sup_v|m_v|\le hB^3.                                \tag{22}
\]

Because \(V_r=a(M)\), the exact clock along the orbit is
\[
 r=\int_{V_0}^{V}\frac{dv}{a(m(v;M_0,V_0))}.           \tag{23}
\]
The integral is signed if \(V<V_0\). Its derivative with respect to
the terminal \(V\) is \(1/a(m(V))\in[1/L,1]\), so it has a
nonvanishing derivative everywhere. For every finite \(r\), ordinary
differentiation of this finite integral is legitimate because the
integrand and its parameter derivatives are continuous when
\(M_0\ne0\). The bounds (21) subsequently control these derivatives
uniformly over all terminal contrasts; no differentiation of an
improper integral is needed.

Let subscripts on \(M(r),V(r)\) now mean derivatives at fixed driver
\(r\). Differentiation of (23) yields both exact formulas
\[
 V_{M_0}=a(m(V))\int_{V_0}^{V}
             \frac{a'(m(v))m_{M_0}(v)}{a(m(v))^2}dv,
                                                               \tag{24}
\]
\[
 V_{V_0}=\frac{a(m(V))}{a(M_0)}
       +a(m(V))\int_{V_0}^{V}
             \frac{a'(m(v))m_{V_0}(v)}{a(m(v))^2}dv.
                                                               \tag{25}
\]
The lower endpoint term in (25) is required. The factors
\(m_{M_0},m_{V_0}\) inside these integrals are precisely the
fixed-terminal-contrast derivatives from section 4.

Using \(|a'(m)|\le2e|m|\), \(1\le a\le L\), and (17), (21),
the first formula gives
\[
 |V_{M_0}|\le2eLJ_*\int_{\mathbb R}|m(v)|dv
             \le kB^3J_*\le kjB^7e^{\gamma V_0^2}.    \tag{26}
\]
For the second, (18) gives the integrand estimate
\[
 |a'(m)m_{V_0}|\le4e\gamma |V_0|m^2.
\]
Including the factor \(a(m(V))\le L\), its integral is at most
\[
 4e\gamma L |V_0|\int_{\mathbb R}m(v)^2dv
 \le4e^{3/2}I B^5.
\]
The endpoint term is at most \(L\). Therefore
\[
 |V_{V_0}|\le\ell_*B^5.                              \tag{27}
\]

The two remaining total derivatives require the terminal-contrast
chain rule:
\[
 M_{M_0}=m_{M_0}(V)+m_v(V)V_{M_0},\qquad
 M_{V_0}=m_{V_0}(V)+m_v(V)V_{V_0}.                    \tag{28}
\]
Equations (17), (22), (26), (27) give
\[
 |M_{M_0}|\le(1+hk)B^6J_*
              \le(1+hk)jB^{10}e^{\gamma V_0^2},
\]
\[
 |M_{V_0}|\le d_*B^2+h\ell_*B^8
              \le(d_*+h\ell_*)B^8.                  \tag{29}
\]
Together (26), (27), and (29) bound all four Jacobian entries at fixed
driver. They do not hold the terminal \(V\) fixed.

Finally the derivative with respect to driver is the actual vector
field. Equations (1) and (21) yield
\[
 \|\partial_r\Psi_r\|
 \le |Vb(M)|+|a(M)|
 \le2e I B^3+L\le(L+2eI)B^3.                         \tag{30}
\]
Since a matrix's Euclidean operator norm is at most the sum of the
absolute values of its entries, one explicit admissible constant in
(6) is
\[
 C_e=(1+hk)j+kj+(d_*+h\ell_*)+\ell_*+L+2eI.          \tag{31}
\]
Indeed \(B\ge1\) and \(e^{\gamma V_0^2}\ge1\), so every term in
(26)--(30) is bounded by its coefficient times
\(B^{10}e^{\gamma V_0^2}\). All constants in (19), (31) are positive
and finite for every fixed \(e>0\). They are not optimized, and no
uniform limit as \(e\downarrow0\) is asserted.

For \(M_0=0\), (14)--(15) give a sum of norms at most
\(e^{\gamma V_0^2}+1+L\). The constant (31) is larger than \(2+L\),
so the same (6) holds. This completes the deterministic theorem,
including the exceptional coordinate and every sign of driver time.

## 6. Gaussian integrability and the strict threshold

Let \((M_0,V_0)\) be a centered jointly Gaussian pair with finite
variances. Suppose first \(v=\operatorname{Var}(V_0)>0\). It can be
written as \(M_0=\alpha V_0+Z\), with \(Z\) an independent centered
Gaussian, possibly of zero variance: choose
\(\alpha=\operatorname{Cov}(M_0,V_0)/v\); the resulting jointly
Gaussian residual is uncorrelated with, hence independent of, \(V_0\).

For each \(p>0\), the finite Gaussian moments of \(Z\) imply
\[
 \mathbb E[B^{10p}\mid V_0]
 \le C_{e,p,\mathrm{law}}(1+|V_0|)^{10p}.
\]
For powers below one use subadditivity; for powers at least one use
the inequality bounding a power of a finite sum by the sum of powers
times a fixed constant. Taking the \(p\)-th power of (6) therefore
reduces integrability to
\[
 \int_{\mathbb R}(1+|x|)^{10p}
    \exp\left[\left(p\gamma-\frac1{2v}\right)x^2\right]dx<\infty,
\]
which holds under the strict inequality (7). If \(v=0\), centeredness
gives \(V_0=0\) almost surely, and the bound is polynomial in a
Gaussian \(M_0\), so all positive moments exist. Suprema over \(r\)
are measurable: continuity permits taking the same supremum over the
countable set of rational driver times.

For \(e=1/10\), \(\gamma=1/11\). With standard Gaussian contrast,
\(p=4\) gives \(p\gamma v=4/11<1/2\). Thus
\[
 \mathbb E\left[
  \sup_{r\in\mathbb R}
     (\|D\Psi_r\|+\|\partial_r\Psi_r\|)^4\right]<\infty.
                                                               \tag{32}
\]
This does not assert moments of every order for that fixed activation.

The strictness is substantive. Take the admissible degenerate Gaussian
pair \(M_0=0\), \(V_0\sim N(0,v)\). By (14)--(15), choosing the
driver time \(r=-V_0/L\) realizes
\[
 \sup_r|M_{M_0}(r)|=\exp(\gamma V_0^2).
\]
Its \(p\)-th moment is infinite whenever \(p\gamma v\ge1/2\),
including equality. Therefore the moment claim cannot be extended to
that boundary uniformly over all Gaussian covariances allowed here.

The common coordinate itself has Gaussian-tail control through (5).
The contrast coordinate traverses all real values as \(r\) varies.
No uniform-in-driver bound on the state \(V\), or on its distribution
under an uncontrolled random driver, follows from the response theorem.

## 7. Differentiating a source-dependent driver

Let a parameter \(\xi\) affect both the initial state and a selected
driver. Assume the initial state is differentiable in \(\xi\), and
on the finite interval under consideration assume
\(\xi\mapsto q_\xi\) is differentiable as a map into \(L^1\).
This hypothesis ensures
\(\partial_\xi r_\xi(t)=\int_0^t\partial_\xi q_\xi(s)ds\).
The exact chain rule is then
\[
 \partial_\xi\Psi_{r_\xi(t)}(M_0(\xi),V_0(\xi))
 =D\Psi_{r_\xi(t)}\,\partial_\xi(M_0,V_0)
   +\partial_r\Psi_{r_\xi(t)}
                     \int_0^t\partial_\xi q_\xi(s)ds. \tag{33}
\]
The local gain multiplying either input is bounded by (6), irrespective
of the realized signed driver. Thus this local step needs no exponential
in \(\int|q|\). Equation (33) does not bound the derivative of the
driver itself, or justify exchanging its derivative with an integral
without the stated hypothesis. In particular it is not a closed
response estimate when \(q\) is generated by the other network layers.

## 8. Exact additional forcing in the tangent network

### Tangent objective and its two backward channels

Use three separate population spaces, bounded initial/current actions
\(A,B\), and a readout field \(C\), as in the contract. Absorb the
overall opposite-label sign into \(C\). The near-coincident tangent
forward equations are
\[
 h_\ell=\phi(M_\ell),\qquad k_\ell=a(M_\ell)V_\ell,
\]
\[
 M_2=Ah_1,\quad V_2=Ak_1,\qquad
 M_3=Bh_2,\quad V_3=Bk_2,\qquad G=\langle C,k_3\rangle.
                                                               \tag{34}
\]
Here \(M_1,V_1\) are the orthonormal common and contrast input
coordinates in the limiting metric. This is the tangent objective
obtained by normalizing contrast and letting the input separation
vanish. It is not the original coincident-input interpolation problem.
No claim of convergence of gradients or dynamics as the angle vanishes
is needed or established by the algebra below.

The following derivatives are exact in finite-dimensional versions.
For population fields they hold on a constructed differentiable path
where the displayed products belong to their indicated \(L^2\) spaces
and the chain rules hold. They do not assert that the tangent gradient
is defined on every \(L^2\) ball: products such as \(CV_3\) would make
that assertion false without extra hypotheses.

Define \(p_\ell,q_\ell\) as the incoming adjoints to the forward
activation slots \(h_\ell,k_\ell\), respectively. Define
\(P_\ell,Q_\ell\) as the resulting adjoints to the preactivation slots
\(M_\ell,V_\ell\). Differentiating the two coordinate maps gives
\[
 P_\ell=a(M_\ell)p_\ell+b(M_\ell)V_\ell q_\ell,
 \qquad Q_\ell=a(M_\ell)q_\ell.                       \tag{35}
\]
The boundary conditions and transpose recursions are
\[
 p_3=0,\quad q_3=C,\qquad
 p_2=B^*P_3,\quad q_2=B^*Q_3,\qquad
 p_1=A^*P_2,\quad q_1=A^*Q_2.                         \tag{36}
\]
For example, varying \(M_3,V_3,C\) in \(G\) first gives
\(P_3=C b(M_3)V_3\), \(Q_3=C a(M_3)\), and \(G_C=k_3\).
Substituting \(dM_3=(dB)h_2+B\,dh_2\) and
\(dV_3=(dB)k_2+B\,dk_2\) gives (36) and the block gradient for
\(B\). Repeating that argument at layer 2 and then at layer 1 proves
all remaining formulas, including the raw-metric gradient equations
\[
 \dot M_1=P_1,\quad \dot V_1=Q_1,\qquad
 \dot A=P_2\otimes h_1+Q_2\otimes k_1,
\]
\[
 \dot B=P_3\otimes h_2+Q_3\otimes k_2,
 \qquad \dot C=k_3.                                  \tag{37}
\]
Thus even the bottom local equation is
\[
 \dot M_1=a(M_1)p_1+V_1b(M_1)q_1,\qquad
 \dot V_1=a(M_1)q_1.                                 \tag{38}
\]
The extra common forcing is not an unspecified residual. Explicitly,
\[
 p_2=B^*[C b(M_3)V_3],\qquad q_2=B^*[C a(M_3)],
\]
\[
 p_1=A^*\left[
    a(M_2)B^*[C b(M_3)V_3]
   +b(M_2)V_2 B^*[C a(M_3)]\right],
\]
\[
 q_1=A^*\left[a(M_2)B^*[C a(M_3)]\right].              \tag{39}
\]
It is generated by curvature in the upper layers and retains their
actual adjoint actions. At the top incoming slot \(p_3=0\), but this
does not make the top preactivation dynamics an isolated copy of (2).
The preactivations also change through the trained operators:
\[
 \dot M_2=\dot A h_1+A[a(M_1)\dot M_1],
\]
\[
 \dot V_2=\dot A k_1+
           A[a(M_1)\dot V_1+b(M_1)V_1\dot M_1],
\]
\[
 \dot M_3=\dot B h_2+B[a(M_2)\dot M_2],
\]
\[
 \dot V_3=\dot B k_2+
           B[a(M_2)\dot V_2+b(M_2)V_2\dot M_2].        \tag{40}
\]
These identities display the additional transport terms that a
network-level extension would have to handle.

### Identification with normalized original backward inputs

Let \(\delta=\sqrt{(1-\rho)/2}>0\), \(\mu=\sqrt{1-\delta^2}\),
and use the exact normalized forward maps
\[
 h_\delta(M,V)=\frac{\phi(M+\delta V)+\phi(M-\delta V)}2,
 \quad k_\delta(M,V)=
          \frac{\phi(M+\delta V)-\phi(M-\delta V)}{2\delta}.
\]
Put
\[
 a_\delta=\tfrac12[\phi'(M+\delta V)+\phi'(M-\delta V)],
 \quad b_\delta=
       \frac{\phi'(M+\delta V)-\phi'(M-\delta V)}{2\delta}.
\]
Their exact coordinate Jacobian is
\[
 D(h_\delta,k_\delta)=
 \begin{pmatrix}a_\delta&\delta^2b_\delta\\
                 b_\delta&a_\delta\end{pmatrix}.
                                                               \tag{41}
\]
Consequently the normalized adjoint recursions at every positive
\(\delta\) have
\[
 P_\ell^\delta=a_\delta p_\ell^\delta+b_\delta q_\ell^\delta,
 \qquad Q_\ell^\delta=\delta^2b_\delta p_\ell^\delta
                                      +a_\delta q_\ell^\delta.
                                                               \tag{42}
\]
Let \(\widehat q_{a,\ell}\) be the original, unnormalized sample
backward input before applying the gate; at the top both inputs are
\(C\). If \(\widehat\delta_{a,\ell}
=\phi'(z_a^{(\ell)})\widehat q_{a,\ell}\), then exact substitution
in (42) gives
\[
 q_\ell^\delta=\frac{\widehat q_{1,\ell}+\widehat q_{2,\ell}}2,
 \qquad
 p_\ell^\delta=\frac{\widehat q_{1,\ell}-\widehat q_{2,\ell}}{2\delta},
\]
\[
 Q_\ell^\delta=\frac{\widehat\delta_{1,\ell}
                         +\widehat\delta_{2,\ell}}2,
 \qquad
 P_\ell^\delta=\frac{\widehat\delta_{1,\ell}
                         -\widehat\delta_{2,\ell}}{2\delta}.
                                                               \tag{43}
\]
These identities are preserved by both matrix transposes. In the
normalized feature clock \(u=\delta s\), the bottom metric gives
\(dM_1/du=\mu^2P_1^\delta\), \(dV_1/du=Q_1^\delta\).
As formal coordinate maps, \(a_\delta\to a(M)\),
\(b_\delta\to b(M)V\), and \(\mu^2\to1\), yielding (35), (38).
This explains the metric coefficient and both powers of \(\delta\)
without postulating a dynamical angle limit.

In particular the forcing \(p\) is the normalized *difference* of
the original sample backward inputs. For opposite-label exchange
symmetry it is even under the exchange involution; the average input
\(q\) is odd. Its being even does not force it to vanish when the
common preactivation is zero.

### Canonical Gaussian-program source channel

This source identification is an algebraic statement at a fixed
finite Gaussian program. It assumes only the usual representation
already used in `NEAR_AFFINE_RESPONSE_ROUTE.md`: a backward input is
its oriented Gaussian source plus its causal response/learned-action
terms. It proves no mesh-uniform response estimate.

For either lower layer, write a sample-vector row at time index \(k\)
as
\[
 \widehat q_k=\zeta_k+\sum_{j\le k}\mathcal R_{kj}\widehat h_j,
\]
where \(\zeta_k=(\zeta_{1,k},\zeta_{2,k})^T\),
\(\mathcal R_{kj}\) are the canonical two-by-two coefficient blocks,
and \(\widehat h_j=(h_j+\delta k_j,h_j-\delta k_j)^T\).
Use the channel order \((q,p)\) and matrices
\[
 T_\delta=\begin{pmatrix}1/2&1/2\\
                   1/(2\delta)&-1/(2\delta)\end{pmatrix},
 \qquad J_\delta=\begin{pmatrix}1&\delta\\1&-\delta\end{pmatrix}.
\]
Multiplication of the preceding exact row by \(T_\delta\) gives
\[
 \binom{q_k^\delta}{p_k^\delta}
 =\binom{(\zeta_{1,k}+\zeta_{2,k})/2}
             {(\zeta_{1,k}-\zeta_{2,k})/(2\delta)}
   +\sum_{j\le k}T_\delta\mathcal R_{kj}J_\delta
                      \binom{h_j}{k_j}.              \tag{44}
\]
Thus the canonical source for the additional forcing is the
normalized difference of the backward oriented Gaussian sources:
\(\zeta_p=(\zeta_1-\zeta_2)/(2\delta)\). This is the difference
channel of \(\zeta^{(1)}\) at the bottom and of \(\zeta^{(2)}\) in
the middle, in the notation of the existing response route. It is
not a new independent scalar driver that can be set to zero.

Where the canonical backward Gaussian-source covariance is the
second-moment Gram of the transpose query inputs, the same linear
transformation gives, exactly at fixed program length,
\[
 \operatorname{Var}(\zeta_{p,\ell,k})
   =\mathbb E[(P_{\ell+1,k}^\delta)^2],\qquad
 \operatorname{Var}(\zeta_{q,\ell,k})
   =\mathbb E[(Q_{\ell+1,k}^\delta)^2],
\]
\[
 \operatorname{Cov}(\zeta_{p,\ell,k},\zeta_{q,\ell,k})
   =\mathbb E[P_{\ell+1,k}^\delta Q_{\ell+1,k}^\delta].
                                                               \tag{45}
\]
Here \(\ell=1,2\); the corresponding cross-time identities have the
two time indices in the two factors. These equations are simply
bilinearity of that source covariance, together with (43), and use
uncentered second moments. They neither assume nonsingular covariance
nor discard the causal terms in (44).

For example, if a controlled tangent limit of this fixed-program
description were available, the middle \(p\)-source would have
variance \(\mathbb E[C^2b(M_3)^2V_3^2]\), the square norm of the
first field in (39) before applying \(B^*\). Bounds for this product,
and for the transformed causal coefficients in (44), remain needed.
Equations (44)--(45) do not themselves establish that the normalized
sources or their responses have a controlled limit as \(\delta\to0\).

## 9. Invariant defect under the additional forcing and research status

For the forced bottom channel, write generally
\[
 \dot M=a(M)p+Vb(M)q,\qquad \dot V=a(M)q.             \tag{46}
\]
On any interval on which \(M\ne0\), cancellation of the two \(q\)
terms in the derivative of (10) leaves the exact defect
\[
 \frac d{dt}[V^2+\Lambda(M)]
 =\Lambda'(M)a(M)p
 =\frac{(1+M^2+e)^2}{eM}\,p.                         \tag{47}
\]
The coefficient behaves as \(L^2/(eM)\) near zero. A nonzero \(p\)
can also drive \(M\) through zero, so (47) is not an invariant formula
valid across such a crossing. No pointwise factorization
\(p=M\widetilde p\) follows from (39): transpose actions mix neuron
coordinates. Exchange parity alone supplies no such factorization.

This is an obstruction to using this invariant unchanged, not to
finite-dimensional existence for prescribed forcings. If both \(p,q\)
are locally integrable, \(|\dot V|\le L|q|\) and
\(|\dot M|\le L|p|+2e|V||q|\) still give finite-horizon bounds for
the two-dimensional forced equation. What has not been established is
a counterpart of the uniform response bound (6) that controls the
actual network forcing, its source derivatives, and the operator
transport terms (40).

Even the unforced local theorem does not bound arbitrary perturbations
injected at late times by the original-initial-state constant. For
example, start (3) at \((0,0)\), advance to driver time \(R>0\), and
then reverse to driver time zero. The reached state is \((0,LR)\).
By (14), the derivative of the return map with respect to a common
perturbation at that reached state is \(\exp(eLR^2)\), which diverges
with \(R\). The full map from the original initial state back to
itself has derivative one in that coordinate: it includes the preceding
contraction. Thus (6) and the drive derivative in (33) cannot be used
as a bound on the propagator for an arbitrary late common-channel
forcing. This is a precise remaining obstruction for a variation-of-
constants treatment of \(p\); it does not invalidate the theorem.

| Claim | Status and scope |
|---|---|
| Global signed driver flow and composition with any locally integrable driver | Complete candidate proof, sections 2--3 |
| Exact invariant and common-field excursion bound without a sign condition | Complete candidate proof, section 3 |
| All four initial-state Jacobian entries at fixed driver and driver derivative, with \(B^{10}\) bound | Complete candidate proof, sections 4--5 |
| Gaussian moment bound under the strict variance condition, including \(e=.1,p=4,v=1\) | Complete candidate proof, section 6 |
| Source-dependent driver chain rule | Exact under the differentiability assumptions in section 7 |
| Tangent network common forcing and its normalized backward-source identification | Exact algebra under the regularity/program assumptions stated in section 8 |
| Uniform coupled-network response with one activation for all angles | Open; (39)--(40), (44), and (47) expose the missing inputs |
| Cutoff removal, original joint MF/GF/exact-GD theorem, and transfer from the tangent model | Not proved or asserted in this note |

The local theorem removes a driver-size or elapsed-time exponential
from the self-curvature response of one complete tangent contrast
channel. It preserves the additional network channels as explicit
uncontrolled inputs. It is offered for fresh independent proof audit;
no finite-width primal endpoint, numerical experiment, or agent output
is used as a substitute for response control.
