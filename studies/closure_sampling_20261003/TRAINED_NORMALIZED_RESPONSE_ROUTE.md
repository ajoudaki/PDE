# An actual trained mixed-response bound for two hidden layers

2026-10-04. Scoped research derivation in the existing study. This note proves
an all-time, whole-sphere bound for the first curvature product in a
trained two-hidden-layer network with one training input and a normalized
nonlinear activation. The bound is uniform in width and does not assume a
Gaussian trained law. It does not prove polynomial dependence on arbitrary
depth or a complete compression theorem. The upper-layer mixed response and
the general-data extension remain open. This is a candidate derivation,
awaiting a separate reconstruction; no experiment was run.

The mechanism is a surviving independence: input-weight columns orthogonal
to the single training input never change and are independent of the entire
training trajectory. A bounded-variation estimate for the actual backward
carrier upgrades this independence from a fixed-time expectation to a uniform
all-time bound. No neuron maximum or logarithmic width factor is used.

## 1. Model and normalized nonlinear activation

Take one unit training input, rotated to \(e_1\in\mathbb R^d\), and label
\(y\in\mathbb R\). There are two hidden layers, each of width \(n\):

\[
z^{(1)}(v)=Av,\quad h^{(1)}(v)=\phi(z^{(1)}(v)),\quad
z^{(2)}(v)=Wh^{(1)}(v),\quad
f(v)=n^{-1}w^\top\phi(z^{(2)}(v)).
\tag{1}
\]

Here \(A\in\mathbb R^{n\times d}\), \(W\in\mathbb R^{n\times n}\),
and \(w\in\mathbb R^n\). Initialize the entries of \(A\) independently
as \(N(0,1)\), those of \(W\) independently as \(N(0,1/n)\), and \(w=0\).
The blocks are independent. Use loss \(\mathcal L=(f(e_1)-y)^2\) and
mobilities \((n,1,n)\). For vectors write
\(\|q\|_{2,n}=\|q\|_2/\sqrt n\); matrix operator norms are Euclidean.

Set
\[
b_0=\sqrt{1-\frac{\pi}{2\sqrt3}},\qquad
\phi(x)=b_0+\sqrt{\frac{\pi\sqrt3}{2}}
                  \operatorname{erf}(x/\sqrt2).
\tag{2}
\]
Its useful bounds are
\[
B=b_0+\sqrt{\frac{\pi\sqrt3}{2}},\quad S=3^{1/4},\quad
T=H=S e^{-1/2},
\tag{3}
\]
where \(|\phi|\le B\), \(|\phi'|\le S\), \(|\phi''|\le T\),
and \(|x\phi'(x)|\le H\) on the real line. Indeed
\(\phi'(x)=S e^{-x^2/2}\) and \(\phi''(x)=-Sxe^{-x^2/2}\).
For \(Z\sim N(0,1)\), the uniformity of the Gaussian distribution
function at \(Z\) and the elementary Gaussian integral give
\[
\mathbb E\phi(Z)^2=1,\qquad \mathbb E\phi'(Z)^2=1.
\tag{4}
\]
Thus the limiting initialized training covariance is the one-by-one matrix
\((1)\), and the requested label condition is precisely \(Y=|y|\le c\),
since \(m=\gamma=1\). This is an order-one nonlinear activation.

## 2. An explicit all-time fitting and operator tube

Let \(a=Ae_1\), and write the remaining columns of \(A\) as
\(G\in\mathbb R^{n\times(d-1)}\). All unlabelled features in this
section are evaluated at the training input. Define
\[
\delta=\phi'(z^{(2)})\odot w,\qquad b=W^\top\delta.
\tag{5}
\]
The symbol \(b\) denotes this actual trained backward carrier; \(b_0\) in
(2) is the fixed activation offset. Exact physical-time equations are
\[
\dot w=-2r h^{(2)},\quad
\dot W=-2r\delta h^{(1)\top}/n,\quad
\dot a=-2r\phi'(a)\odot b,\quad \dot G=0,
\qquad r=f(e_1)-y.
\tag{6}
\]
In particular the complete training trajectory is a function of
\((a(0),W(0),y)\) and is independent of \(G\).

The case \(Y=0\) is stationary. By changing \(y,w\) to \(-y,-w\), it
suffices to take \(y=Y>0\). Direct differentiation gives
\[
\dot r=-2\mathcal K r,\qquad
\mathcal K=\|h^{(2)}\|_{2,n}^2
 +\|h^{(1)}\|_{2,n}^2\|\delta\|_{2,n}^2
 +\|\phi'(a)\odot b\|_{2,n}^2.
\tag{7}
\]
Hence \(r<0\) at every finite time. Introduce the increasing residual
clock \(\tau(t)=2\int_0^t|r(s)|\,ds\). A prime below denotes
differentiation with respect to this clock, not physical time. Equation
(6) becomes
\[
w'=h^{(2)},\quad W'=\delta h^{(1)\top}/n,\quad
a'=\phi'(a)\odot b.
\tag{8}
\]

Work on the initialized event
\[
\|W(0)\|_{\mathrm{op}}\le8,\qquad
\|h^{(2)}(0)\|_{2,n}\ge1/\sqrt2.
\tag{9}
\]
Put \(K=9\), \(C_2=B^2+K^2S^2\), and choose
\[
c=\min\left\{1,(16SB^2)^{-1/2},
                    (64S^2BC_2)^{-1/2}\right\}.
\tag{10}
\]
If \(0<Y\le c\), then for all physical times, including the limit,
\[
\|W\|_{\mathrm{op}}\le K,\qquad
\|h^{(2)}\|_{2,n}>1/2,\qquad
|r(t)|\le Y e^{-t/2},\qquad \tau(\infty)\le4Y.
\tag{11}
\]

Here is a complete bootstrap. As long as the first two tube inequalities
hold, (7) gives \(\mathcal K\ge1/4\), and hence the last two bounds
in (11). On this interval, for \(0\le\tau\le4Y\),
\[
\begin{split}
\|w\|_\infty&\le B\tau,&
\|\delta\|_{2,n}&\le SB\tau,&
\|b\|_{2,n}&\le KSB\tau,\\
\|W'\|_{\mathrm{op}}&\le SB^2\tau,&
\|(z^{(2)})'\|_{2,n}&\le SBC_2\tau.
\end{split}
\tag{12}
\]
For the last bound, differentiate the training forward pass exactly:
\[
(z^{(2)})'=\delta\|h^{(1)}\|_{2,n}^2
                    +W[\phi'(a)^2\odot b].
\tag{13}
\]
Integration yields
\[
\|W-W(0)\|_{\mathrm{op}}\le\tfrac12 SB^2\tau^2\le1/2,
\quad
\|h^{(2)}-h^{(2)}(0)\|_{2,n}
                 \le\tfrac12 S^2BC_2\tau^2\le1/8.
\tag{14}
\]
Both bounds are strictly inside their tubes:
\(8+1/2<9\) and \(1/\sqrt2-1/8>1/2\).
Local existence and the bounded derivatives in (8) prevent a finite-time
escape. First-exit continuation proves (11). Finite residual clock and
the displayed derivative bounds give limits of \(a,W,w\); therefore the
limit time is included. No supplied source or insertion theorem is used.

Event (9) has probability tending to one. The first-layer empirical
second moment converges to one by bounded-variable variance estimates.
Conditionally on that layer, the second-layer training preactivations are
independent \(N(0,q_1)\), where \(q_1=\|h^{(1)}(0)\|_{2,n}^2\).
Another bounded-variable variance estimate, and continuity of
\(q\mapsto\mathbb E\phi(\sqrt q Z)^2\), give the second event in (9).
For the operator event, two \(1/4\)-nets of the unit sphere with at most
\(9^n\) points each give
\(\|W\|_{\mathrm{op}}\le2\max_{u,v\text{ in nets}}|u^\top Wv|\).
Each pairing has variance \(1/n\), so its failure probability at the cap
eight is at most \(2\exp[-(8-2\log9)n]\).

## 3. The adaptive carrier has bounded total variation in RMS

Differentiating the actual carrier uses no distributional approximation:
\[
b'=W'^\top\delta+W^\top\delta',\qquad
\delta'=\phi'(z^{(2)})\odot h^{(2)}
       +\phi''(z^{(2)})\odot(z^{(2)})'\odot w.
\tag{15}
\]
The coordinate bound on \(w\), not on \(b\), is sufficient. From (12),
\[
\|\delta'\|_{2,n}\le SB+TSB^2C_2\tau^2,
\quad
\|b'\|_{2,n}\le KSB+D\tau^2,
\quad D=S^2B^3+KTSB^2C_2.
\tag{16}
\]
Consequently, writing \(\tau_*=4Y\),
\[
\sup_\tau\|b(\tau)\|_{2,n}\le KSB\tau_*=:B_1,
\qquad
\int_0^{\tau(\infty)}\|b'(\tau)\|_{2,n}\,d\tau
          \le KSB\tau_*+D\tau_*^3/3=:V_b.
\tag{17}
\]
These bounds hold for the finite network after reuse of \(W\) in both
forward and backward propagation. They have not replaced that matrix by
an independent copy.

## 4. All-time mixed product without a neuron maximum

The mobility coordinates are \(\Theta=(A,\sqrt n W,w)\). For a query
\(v\in S^{d-1}\), a unit direction \(u\in\mathbb R^d\), and the
training input \(e_1\), define the actual quantities
\[
J^{(1)}(v,u)=D_vz^{(1)}(v)[u]=Au,
\qquad
R^{(1)}(v)=D_\Theta z^{(1)}(v)\nabla_\Theta(nf(e_1)).
\tag{18}
\]
Writing \(u=(u_1,u_\perp)\), exact differentiation gives
\[
J^{(1)}=a u_1+G u_\perp,\qquad
R^{(1)}(v)=v_1\phi'(a)\odot b.
\tag{19}
\]
It is enough to bound a matrix Frobenius norm; no query net is required:
\[
\begin{split}
\sup_{v,u}\|\phi''(z^{(1)}(v))\odot R^{(1)}(v)
                                      \odot J^{(1)}(v,u)\|_{2,n}
&\le T\left[H\|b\|_{2,n}
             +S\|\operatorname{diag}(b)G\|_F/\sqrt n\right].
\end{split}
\tag{20}
\]
The first term uses \(|a_i\phi'(a_i)|\le H\); this is where the
chosen nonlinear activation controls the training-aligned tangent.

Condition on \((a(0),W(0),y)\). The entire curve \(b(\tau)\) is then
fixed and \(G\) still has independent standard Gaussian entries.
Since \(b(0)=0\), the fundamental theorem of calculus and Minkowski give
\[
\sup_\tau\|\operatorname{diag}(b(\tau))G\|_F/\sqrt n
\le\int_0^{\tau(\infty)}
          \|\operatorname{diag}(b'(\tau))G\|_F/\sqrt n\,d\tau.
\tag{21}
\]
For every fixed vector \(q\), direct Gaussian integration gives
\[
\left(\mathbb E_G\frac{\|\operatorname{diag}(q)G\|_F^2}{n}\right)^{1/2}
=\left(\frac{d-1}{n}\sum_iq_i^2\right)^{1/2}
=\sqrt{d-1}\|q\|_{2,n}.
\tag{22}
\]
Minkowski in conditional \(L^2(G)\) and (17) therefore bound the square
root of the conditional second moment of the left side of (21)
by \(\sqrt{d-1}V_b\). Equivalently, square its right side, use Tonelli,
and apply Cauchy--Schwarz to the two Gaussian factors. Markov's inequality
for that square proves: for every
\(0<\eta<1\), conditional on any training initialization satisfying (9),
with conditional probability at least \(1-\eta\),
\[
\sup_{t\in[0,\infty],\,v\in S^{d-1},\,\|u\|=1}
\|\phi''(z^{(1)}(t,v))\odot R^{(1)}(t,v)
                                    \odot J^{(1)}(t,v,u)\|_{2,n}
\le T\left[HB_1+\frac{S\sqrt{d-1}}{\sqrt\eta}V_b\right].
\tag{23}
\]
At \(d=1\), the Gaussian term is identically zero and the statement is
deterministic on (9). For fixed \(d,\eta\), the right side is at most

\[
C_\eta Y,\qquad
C_\eta=4THKSB+
\frac{TS\sqrt{d-1}}{\sqrt\eta}
             \left(4KSB+\frac{64}{3}Dc^2\right),
\tag{24}
\]
independently of width. Overall probability is at least
\(1-\eta-o_n(1)\). The same proof without the outer factor \(T\)
bounds \(R^{(1)}\odot J^{(1)}\). In particular the actual physical
curvature forcing is integrable:
\[
\int_0^\infty\sup_{v,u}
\|\phi''(z^{(1)})\odot\dot z^{(1)}\odot J^{(1)}\|_{2,n}\,dt
\le4C_\eta Y^2,
\tag{25}
\]
because \(\dot z^{(1)}=-2rR^{(1)}\) and \(\tau(\infty)\le4Y\).
This is a loss-weighted trained estimate, not an initialization result.

## 5. What remains unclosed, even in this restricted model

Equation (23) controls the curvature term in the time derivative of the
second preactivation tangent,
\[
\dot J^{(2)}=\dot W[\phi'(z^{(1)})\odot J^{(1)}]
 +W[\phi''(z^{(1)})\odot\dot z^{(1)}\odot J^{(1)}]
 +W[\phi'(z^{(1)})\odot\dot J^{(1)}].
\tag{26}
\]
It does not control every source Hessian or the top feature-tangent
curvature. The next residual-free response is exactly
\[
R^{(2)}(v)=\delta\langle h^{(1)},h^{(1)}(v)\rangle_n
       +v_1W[\phi'(z^{(1)}(v))\odot\phi'(a)\odot b],
\quad
J^{(2)}(v,u)=W[\phi'(z^{(1)}(v))\odot Au].
\tag{27}
\]
Here \(\langle p,q\rangle_n=p^\top q/n\). The product
\[
\phi''(z^{(2)}(v))\odot R^{(2)}(v)\odot J^{(2)}(v,u)
\tag{28}
\]
contains two adaptively correlated images under the same \(W\). A bound
on its operator norm and separate RMS norms does not bound their
coordinatewise product. Conditional independence of \(G\) alone does
not remove the nonzero, trained, conditional means of those images.
No width-uniform estimate for (28) is asserted here.

At three hidden layers, differentiating the corresponding carrier
already produces an internal term
\(\phi''(z^{(2)})\odot(z^{(2)})'\odot k^{(2)}\), where the
backward carrier is
\(k^{(2)}=W^{(3)\top}[\phi'(z^{(3)})\odot w]\);
the bounded-coordinate argument for \(w\) in (15) no longer applies.
Thus (16) is not a recursion proving polynomial depth growth. For
multiple training inputs, the frozen columns orthogonal to their span
remain available, but the tangent inside that span and the vector
residual-clock cancellation need new estimates.

## 6. The favorable Gaussian gate identity does not close training

For completeness, the proposed normalized erf has an especially favorable
joint Gaussian tangent identity. If \((Z,J)\) is centered jointly Gaussian,
\(\mathbb EZ^2=q>0\), \(\mathbb EJ^2=v_J\), and
\(\mathbb EZJ=c_J\), Gaussian regression followed by the elementary
integrals for \(e^{-Z^2}\) gives
\[
\mathbb E[\phi'(Z)^2J^2]
=\frac{\sqrt3}{\sqrt{1+2q}}v_J
 -\frac{2\sqrt3}{(1+2q)^{3/2}}c_J^2.
\tag{29}
\]
Indeed write \(J=(c_J/q)Z+U\), with \(U\) independent of \(Z\) and
variance \(v_J-c_J^2/q\), then use
\(\mathbb E e^{-Z^2}=(1+2q)^{-1/2}\) and
\(\mathbb E Z^2e^{-Z^2}=q(1+2q)^{-3/2}\).
At unit variance (29) is \(v_J-2c_J^2/3\le v_J\). Correlation
therefore helps in this exactly Gaussian calculation.

The actual trained empirical tangent energy
\(M=n^{-1}\sum_i\phi'(z_i)^2J_i^2\) instead has the exact derivative
\[
\dot M=2\langle\phi'(z)^2\odot J,\dot J\rangle_n
       +2\langle\phi'(z)\phi''(z)\odot J^2,\dot z\rangle_n.
\tag{30}
\]
For general data, \(\dot z=-(2/m)\sum_a r_aR_a\), so the second
term is \(-(4/m)\sum_a r_a\langle\phi'\phi''J^2,R_a\rangle_n\).
It has no established sign and requires the trained mixed response.
Loss energy controls the parameter velocity; it does not identify this
query-dependent multiplier with a dissipative quadratic form. Replacing
the empirical law in (30) by the law in (29) would be an unproved
approximation. The two scalar normalizations in (4) do not bound that
replacement error or preserve Gaussian regression after matrix reuse.

## 7. Inputs, check status, and consequence

Complete scientific inputs were `BETA_ENVELOPE_AUDIT.md`,
`NONEXPANSIVE_INITIAL_QUERY_ROUTE.md`, `NORMALIZED_ERF_COMPLEX_GAIN_ROUTE.md`,
`RUNTIME_SMALL_ACTIVITY_CONSTANT_ROUTE.md`, and
`ERROR_PREFACTOR_GEOMETRIC_ROUTE.md`, all within this study. No linked
scientific dependency was imported. Required shared instructions,
canonical notation and neural conventions, rigorous proof instructions,
and research contract/audit instructions were read. The supervisor
requested prioritizing two hidden layers and suggested the Gaussian
conditional gate identity; the bounded-variation construction above was
derived here. This was a collaborative route, not an isolated review.

Established by the displayed argument, pending independent reconstruction:
the finite trained two-hidden-layer, one-input first-gate bound (23) and
its loss-weighted form (25), with an explicit fitting bootstrap and no
width logarithm. Exact but insufficient for the full target: the Gaussian
identity (29) and the trained energy equation (30). Open: (28), general
training data, higher layers, polynomial depth constants, and the full
all-time whole-sphere root-width autonomous compression theorem. No
existing all-time compression claim is superseded.

Input hashes at completion:

| Input | SHA-256 |
| --- | --- |
| `BETA_ENVELOPE_AUDIT.md` | `42461b5f2381b337c2646ab7c5387921abf8b3e1f255df7160d5757025940d28` |
| `NONEXPANSIVE_INITIAL_QUERY_ROUTE.md` | `0f705c36cf297f086ee6eedecfcf4e99f467bf73fdc5ccad79ea7e6f476a3da9` |
| `NORMALIZED_ERF_COMPLEX_GAIN_ROUTE.md` | `8368603ca1a6bd449dc478810befce7aa62dc8cc1dc05869c9a68114a19599ef` |
| `RUNTIME_SMALL_ACTIVITY_CONSTANT_ROUTE.md` | `061d46972a7b026bd6b6b5176fc411214e82bd1e9d9e18ec5bd8e119fedbeaa2` |
| `ERROR_PREFACTOR_GEOMETRIC_ROUTE.md` | `2cf92bcfb35729374b607c348b69ab80ae8e741878155012980ed3ffa580879c` |

Author checks: reconstructed mobility factors in (6)--(8), residual signs,
the strict bootstrap margins, the zero-label and one-dimensional cases,
the response definition in (18)--(19), and conditional independence in
(21)--(22). A delimiter audit found matching inline and display math
delimiters with no inline delimiters inside displays. These author checks
are not an independent review. Only this assigned artifact was written;
no Git mutation or maintained-source edit was made.
