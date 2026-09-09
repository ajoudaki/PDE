# Adversarial audit of the proposed uniform bounds at depths two and three

## 1. Verdict

Let

\[
 R_{t,L}(h):=F_{t,L}(2h)-F_{2t,L}(h)
 +\frac{t(2t-1)}2J_{\phi,L}h^3 .
 \tag{1.1}
\]

Under the stated assumptions

\[
 \phi\in C^{12},\qquad
 \sup_x\frac{|\phi(x)|}{1+|x|}<\infty,qquad
 \max_{1\le j\le12}\|\phi^{(j)}\|_\infty<\infty,
 \tag{1.2}
\]

the claim to be audited is the existence of activation-defined constants
\(c_{\phi,L}>0\) and \(C_{\phi,L}<\infty\) such that

\[
 |R_{t,L}(h)|\le C_{\phi,L}t^4|h|^5,
 \qquad t\ge1,\quad |h|\le c_{\phi,L}/t.             \tag{1.3}
\]

The independent verdict is:

| depth | verdict | reason |
|---|---|---|
| \(L=1\) | **proved** | the width-first dynamics is an iid two-dimensional Euler recursion; a pathwise weighted \(C^4\) envelope is Gaussian-integrable and yields (1.3) |
| \(L=2\) | **open** | the first reused connector creates adjoint responses for which only an \(L^2\) energy bound and fixed-horizon all-moment membership have been proved; the required horizon-uniform high-moment/source-sensitivity estimate is absent |
| \(L=3\) | **open** | it contains the unresolved depth-two connector problem twice; the proposed layer-transfer estimate is stated but not proved |

Accordingly, `UNIFORM_L2.md` and `UNIFORM_L3.md` are correct only because
they explicitly decline to claim (1.3).  They are not proofs of the
requested depth-two or depth-three theorem.  No explicit
\(C_{\phi,2},c_{\phi,2},C_{\phi,3},c_{\phi,3}\) satisfying (1.3) has
been constructed.

## 2. What is already rigorous and common to all three depths

For the width-first population Euler map

\[
 E_h\theta=\theta+h g(\theta),\qquad C_h=E_{2h},
 \qquad B_h=E_h^2,
\]

the local coarse/fine defect factors exactly:

\[
 B_h\theta-C_h\theta
 =h^2\int_0^1Dg(\theta+shg(\theta))[g(\theta)]\,ds. \tag{2.1}
\]

Pullback telescoping through \(t\) macro-steps therefore gives

\[
 F(C_h^t\theta_0)-F(B_h^t\theta_0)=h^2Q_{t,L}(h),  \tag{2.2}
\]

where \(Q_{t,L}\) is a sum of exactly \(t\) transported local defects.
The Gaussian sign involution makes the left side odd.  If, and only if,
\(Q_{t,L}\in C^3\) with the quantitative estimate

\[
 \sup_{|v|\le c_{\phi,L}/t}|Q_{t,L}'''(v)|
 \le6C_{\phi,L}t^4,                                \tag{2.3}
\]

Taylor's integral formula gives

\[
 \left|F_{t,L}(2h)-F_{2t,L}(h)-Q_{t,L}'(0)h^3\right|
 \le C_{\phi,L}t^4|h|^5.                           \tag{2.4}
\]

The independent cubic calculation identifies

\[
 Q_{t,L}'(0)=-\frac{t(2t-1)}2J_{\phi,L}.           \tag{2.5}
\]

Thus all time combinatorics, the coefficient, and the power \(t^4\) have
been settled.  The only substantive question is whether (2.3) has been
proved on the actual reused-matrix population dynamics.  It has at
\(L=1\), and it has not at \(L=2,3\).

## 3. Depth one really closes

At \(L=1\), each neuron is an independent copy of

\[
 a^+=a+h\phi(u),\qquad
 u^+=u+ha\phi'(u),qquad f(a,u)=a\phi(u).           \tag{3.1}
\]

There is no reused matrix and no response coefficient.  With
\(r=1+|A|+|U|\) and \(|h|t\le(16M_\phi)^{-1}\), the pathwise state obeys

\[
 1+|a_s|+|u_s|\le e^{M_\phi\sum_j|h_j|}r<2r.       \tag{3.2}
\]

The derivatives through order four of the vector field and observable
are bounded by a constant linear in \(r\).  Differentiating the exact
transported defect three times gives a finite expression bounded by a
polynomial in \(r\) times \(e^{Cr}\).  This is integrable under the two
Gaussian seeds.  Hence differentiation through the expectation is
justified uniformly in \(t\), and (2.3) follows with the explicit
constant in `UNIFORM_L1.md`.

The identity activation is a hostile sharpness test:

\[
 F_{N,1}(h)=\frac{(1+h)^{2N}-(1-h)^{2N}}2,
\]

and the fifth coefficient of the discrepancy is

\[
 32{2t\choose5}-{4t\choose5}
 =-\frac43t(t-1)(2t-1)(8t-9).                     \tag{3.3}
\]

It has exact order \(t^4\).  Thus the claimed time power is both achieved
and sharp at depth one.

## 4. The precise failure at depth two

### 4.1 The valid \(L^2\) estimate is insufficient

Write the learned connector as \(K_s\) and set

\[
 \mathcal E_s=\|a_s\|_2+\|K_s\|_{\rm HS}+\|u_s\|_2.
\]

The fixed connector has \(L^2\)-operator norm at most two.  The calculation
in `UNIFORM_L2.md` proves

\[
 \mathcal E_{s+1}
 \le \mathcal E_s+6M_\phi^2|\varepsilon_s|
                  (1+\mathcal E_s)^2,              \tag{4.1}
\]

and hence

\[
 \sum_s|\varepsilon_s|\le(216M_\phi^2)^{-1}
 \quad\Longrightarrow\quad
 \sup_s\mathcal E_s\le3.                          \tag{4.2}
\]

This part is horizon independent and correct.  It controls the state only
in \(L^2\).  The first normalized top-source tangent already contains

\[
 a_s\phi''(z_s)\zeta_s^i,                          \tag{4.3}
\]

and the bottom-source tangent contains

\[
 r_s\phi''(u_s)p_s^i.                              \tag{4.4}
\]

Controlling either term in \(L^2\) requires, for example,

\[
 \|a_s\zeta_s^i\|_2
 \le\|a_s\|_4\|\zeta_s^i\|_4.                   \tag{4.5}
\]

Equation (4.2) supplies neither factor on the right.  Repeating the same
entrywise Holder argument at \(L^4\) asks for \(L^8\), and repeating it
through a history of unrestricted length does not close at a fixed moment
order.  Fixed-horizon membership in every \(L^p\) does not give a bound
uniform in the horizon.

### 4.2 Causal step factors do not supply the missing norm

The chronological DAG does show that a strictly past response must cross
the update at its source time.  In a fixed chronological coordinate
presentation one can therefore factor

\[
 \rho_{si}=\varepsilon_i\bar\rho_{si},\qquad
 \sigma_{si}=\varepsilon_i\bar\sigma_{si},
 \qquad i<s.                                      \tag{4.6}
\]

This converts the response histories to Volterra sums.  It solves the
counting problem, but not the analytic one: (4.6) bounds a sum by total
variation only after a horizon-independent bound for
\(\bar\rho_{si},\bar\sigma_{si}\) and their required mixed derivatives
has been proved.  Equations (4.3)--(4.5) are exactly where that proposed
bound fails to follow from the current energy estimate.

There is also a singular-coordinate qualification.  When a source Gram is
singular, individual formal coefficients in a redundant Gaussian history
are not intrinsic: two smooth extensions off the Gaussian support can
have different individual coordinate derivatives.  What is intrinsic is
the aggregate adjoint response

\[
 J^*x=\sum_i\mathbb E[\partial_{\chi_i}x]c_i        \tag{4.7}
\]

and its forward analogue.  Thus (4.6) is rigorous for a specified
chronological formal presentation, or after being stated for the
aggregate response.  It should not be advertised as a representation-free
identity for each coefficient at a singular Gram.

### 4.3 The connector shortcut is false

No ambient \(L^p\) connector estimate repairs (4.5).  For \(p>2\), take
\(c_m\in\bigcap_{q<\infty}L^q\) with

\[
 \|c_m\|_2=1,\qquad \|c_m\|_p\to\infty,
\]

and set \(x_m=Jc_m\).  Each \(x_m\) is exactly standard Gaussian, but

\[
 J^*x_m=c_m.                                       \tag{4.8}
\]

Consequently even identical all-moment input laws do not control the
target \(L^p\) norm of a reused connector.  The necessary estimate must
use the special dynamically reachable response class; it cannot follow
from Gaussian input moments plus the \(L^2\)-operator norm.

The Nemytskii shortcut is also unavailable.  For non-affine \(\phi\), the
second formal derivative contains pointwise multiplication, which is not
a bounded map \(L^2\times L^2\to L^2\).  Hence the abstract Banach-space
\(C^4\) theorem cannot simply be applied on the population Hilbert space.

These are not cosmetic omissions.  They leave (2.3) unproved already at
\(L=2\).

## 5. Depth three adds no closure

At \(L=3\) there are two fixed connectors

\[
 W_2=I_2+J_2^*,\qquad W_3=I_3+J_3^*.
\]

The causal graph argument gives one Volterra response pair for each
connector.  It does not prove a uniform norm for either pair.  Since the
lower connector already contains the complete depth-two obstruction,
adding the upper connector cannot make (4.5) available.

`UNIFORM_L3.md` proposes bounds over the finite moment list
\(\{2,4,8,16,32\}\).  The list is only part of a sufficient-lemma
proposal: no node-by-node Holder ledger proves that it closes all mixed
state, response, interpolation, and transported-tangent derivatives.
Therefore even the sufficiency of that exact five-element list should
not be promoted to a proved statement.  What is certainly sufficient is
a finite, explicitly derived mixed Gaussian-Sobolev ledger that closes
all products through the required derivative order; such a ledger has not
been constructed.

One further distinction is essential.  A cylindrical partial derivative
with respect to an old formal raw source holds later raw coordinates fixed.
An ordinary Euler parameter tangent differentiates future fixed-operator
actions as well:

\[
 \frac d{d\lambda}I_ax_s(\lambda)=I_ax_s'(\lambda),
 \qquad
 \frac d{d\lambda}J_a\delta_s(\lambda)=J_a\delta_s'(\lambda). \tag{5.1}
\]

Therefore a normalized old-source partial cannot be identified with the
ordinary transported recursion

\[
 P_{s+1}=P_s+\varepsilon_sDg(\theta_s)[P_s]         \tag{5.2}
\]

unless the derivatives in (5.1), the moving query directions, and the
aggregate adjoint responses are explicitly included.  Section 5 of
`UNIFORM_L3.md` should be read as motivation for the desired tangent
system, not as a proof that its displayed old-source partials already
satisfy (5.2).

The spiky example (4.8) is not a counterexample to the network inequality,
because those vectors have not been shown reachable from the Gaussian
initialization.  It is, however, a decisive counterexample to the ambient
connector estimate on which a short depth-three proof might otherwise be
based.

## 6. What the low-depth analysis says about general depth

The low-depth cases identify the correct prospective induction, but do
not execute it.  A valid induction must start by proving, at one reused
connector, an intrinsic **causal Gaussian-Sobolev transfer lemma** with
the following features:

1. its norm includes the aggregate adjoint responses rather than relying
   on nonintrinsic singular-history coefficients;
2. it controls the finitely many state, step, source, interpolation, and
   transported-direction derivatives required by (2.3);
3. every historical contribution is integrated against its source-time
   step, so the bound depends on \(\sum_s|\varepsilon_s|\), not on the
   number of history slots;
4. its Holder/Malliavin exponents form a finite, explicitly verified
   ledger;
5. its constants depend only on the activation envelope, Gaussian moments,
   and the incoming layer ledger.

If this lemma supplied an explicit map

\[
 \mathfrak R_a=\Gamma_{\phi,a}(\mathfrak R_{a-1}), \tag{6.1}
\]

then applying it forward and backward through the \(L-1\) connectors
would terminate at every fixed depth.  Its final constant could be inserted
into the already proved transported-defect recursion, giving the explicit
\(t^4\) factor for general \(L\).

The key lesson is that depth three does not reveal a new time
combinatoric obstruction: causal divisibility persists layer by layer.
The unresolved analytic base case is depth two.  Until the transfer lemma
is actually proved there, neither the \(L=2\), \(L=3\), nor general-depth
version of (1.3) is established.

## 7. Final audit statement

The strongest fully rigorous conclusion presently supported is:

\[
 \boxed{\text{the uniform }t^4|h|^5\text{ remainder is proved at }L=1
 \text{ and remains open at }L=2,3.}
\]

The fixed-finite-\((L,t)\) compiler bounds remain unconditional at depths
two and three, but their constants grow with the exposed horizon and do
not imply (1.3).  The low-depth work informs a plausible general-depth
route—an intrinsic causal Gaussian-Sobolev layer transfer—but supplies
neither its depth-two proof nor the activation-only constants required by
the requested theorem.
