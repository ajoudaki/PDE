# A genuine finite-time remainder bridge for an orthogonal two-tanh witness

Status: new bounded author derivation with an internal check, 2026-10-10.
This proves an initialized
jet and actual-trajectory remainder sub-bridge for two tanh layers. It does
**not** prove a stronger NTH order or storage lower bound. The complete
coefficient noncancellation and probability-scale issues remain open.

The averaged-upper author checked Sections 2--4 at SHA256
`d484836a408a31d96a04b5f2ff55f95f2f51dbdb56e92b63f2efcdf1dee5c4c8`;
the check record is in FINITE_TIME_REMAINDER.md, Section 4. Root also read
and reconstructed the complete argument. This is a same-study check, not
an independent promotion review. This status paragraph changes no formulas.

Scientific inputs: the complete same-study `GAUSSIAN_TAIL_LOWER.md`,
`INITIAL_JET_MOMENTS.md`, and `NONLINEAR_RESULT.md`. Required proof,
conjecture-audit, and canonical-notation instructions were applied. No
experiments, other-study inputs, Git operations, or closure changes were used.

## 1. Scope and new result

Take two training inputs \(v_a=x_a/\sqrt2=e_a\), \(a=1,2\), labels
\(y=(\eta,0)\), and fixed \(0<\eta\le1\). The first and second
activations are both tanh. With \(z_a=W^{(1)}e_a\), \(W=W^{(2)}\),

\[
h_a=\tanh z_a,\qquad Z_a=Wh_a,\qquad
f_a=n^{-1}u^\top\tanh Z_a.
\]

Initialization and mobilities are the canonical ones:
\(z_{a,j}\sim N(0,1)\), \(W_{ij}\sim N(0,1/n)\), independently,
\(u_0=0\), and mobility \((n,1,n)\). The loss is
\(\sum_a(f_a-y_a)^2/4\). The original frozen-top NTH copies initialized
tensors, freezes its top rank, and uses its own residual at every lower
rank, exactly as in `NONLINEAR_RESULT.md`.

**Finite-remainder theorem.** Fix \(A>0\). There are constants \(C_A\)
and \(C\), independent of width and order, such that with probability
at least \(1-Cn^{-A}\), simultaneously for integers
\(2\le q\le R\le\lfloor\log(en)\rfloor\), both the actual dense
prediction and the order-\(q\) original NTH prediction have their actual
degree-\(R\) physical-time Taylor remainders bounded by

\[
C(B_{R,n}t)^{R+1},\qquad
0\le t\le B_{R,n}^{-1},\qquad
B_{R,n}=[C_A(R+1)\log(en)]^{C_A}.
\tag{1}
\]

Increasing the fixed exponent or the constant is allowed in this formula.
The dense-minus-NTH discrepancy obeys the same estimate with twice the
constant. No holomorphic neighborhood of the true dense trajectory is
assumed. The prediction and state jets in this theorem are the actual
ones, not a frozen-carrier approximation.

Orthogonality is essential to the coordinate calculation below. For
correlated training inputs the transformed first-layer equations retain
ratios of first-activation derivatives, and this proof does not apply.

## 2. Exact real coordinates and width-independent stability

Define

\[
F(x)=x/2+\sinh(2x)/4,\qquad H=\tanh\circ F^{-1}.
\]

Then \(F'(x)=\cosh^2x>0\), so the inverse exists on the real line, and

\[
H'(s)=(1-H(s)^2)^2,\qquad |H(s)|<1,\qquad 0<H'(s)\le1.
\tag{2}
\]

Use normalized variables

\[
\zeta_a=F(z_a)/\sqrt n,\qquad U=u/\sqrt n,\qquad D=W-W_0,
\]

and define the normalized coordinatewise maps

\[
\mathcal A_n(\zeta)=H(\sqrt n\zeta)/\sqrt n,
\qquad \mathcal T_n(V)=\tanh(\sqrt n V)/\sqrt n.
\]

Put \(A_a=\mathcal A_n(\zeta_a)\), \(V_a=WA_a\),
\(d_a=\operatorname{sech}^2(\sqrt nV_a)\),
\(C_a=d_a\odot U\), and \(\rho_a=(y_a-f_a)/2\).
The exact physical equations in the original state are

\[
\begin{aligned}
f_a&=U^\top\mathcal T_n(V_a),\\
\dot\zeta_a&=\rho_aW^\top C_a,\\
\dot U&=\sum_b\rho_b\mathcal T_n(V_b),\\
\dot W&=\sum_b\rho_b C_b A_b^\top.
\end{aligned}
\tag{3}
\]

The cancellation in the first equation for \(\dot\zeta_a\) uses the
orthogonal input directions. No activation or parameter mobility changed.

Let \(Y=\|y\|_2/\sqrt2\). Loss monotonicity gives
\(\sum_a|\rho_a|\le Y\). Since raw second-layer features have modulus
at most one,

\[
\|u(t)\|_\infty\le Yt,\qquad
\|U(t)\|_2\le Yt,\qquad
\|W(t)\|_{\rm op}\le\|W_0\|_{\rm op}+Y^2t^2/2.
\tag{4}
\]

Also

\[
\sum_a\|\zeta_a(t)-\zeta_a(0)\|_2
\le \tfrac12\|W_0\|_{\rm op}Y^2t^2+Y^4t^4/8.
\tag{5}
\]

These follow by integrating (3), using \(\|A_a\|_2\le1\),
\(\|C_a\|_2\le\|U\|_2\), and \(\|\dot W\|_F\le Y\|U\|_2\).
They prevent finite-time blowup of the finite-dimensional real system.
They do not assert an eventual Gram gap or fitting rate.

For stability, equip state differences with

\[
\|\Delta S\|=\sum_a\|\Delta\zeta_a\|_2+
\|\Delta U\|_2+\|\Delta W\|_F.
\]

Both \(\mathcal A_n\) and \(\mathcal T_n\) are 1-Lipschitz on real
vectors. If two states satisfy
\(\|W\|_{\rm op},\|U\|_2,\|u\|_\infty\le M\), then

\[
\|\Delta V_a\|_2\le M\|\Delta\zeta_a\|_2+\|\Delta W\|_F,
\quad
\|\Delta C_a\|_2\le
\|\Delta U\|_2+2M\|\Delta V_a\|_2.
\tag{6}
\]

The second estimate uses \(|(\operatorname{sech}^2)'|\le2\) and
\(\sqrt n\|U\|_\infty=\|u\|_\infty\); this is where a raw readout
bound, not merely its Euclidean norm, matters. Subtracting the products
in (3) now proves that the original vector field and the predictions are
Lipschitz with constants depending only on \(M,y\), not on \(n\).
Together with (4), this gives width-independent real stability on every
fixed finite time interval for bounded initial matrix operator norm.
No bound on the absolute transformed coordinates is needed.

## 3. Complete initialized jets under conditional Gaussian projection

Here raw transformed coordinates are denoted by
\(\xi_a=F(z_a)=\sqrt n\zeta_a\); the symbol \(\xi_a\) is not a
Gaussian contrast. Let \(D_b= D[\,M\nabla f_b\,]\). Exact source rules
are

\[
\begin{aligned}
D_b\xi_a&=\delta_{ab}W^\top(u\odot d_b),\\
D_bu&=\tanh Z_b,\\
D_bW&=(u\odot d_b)h_b^\top/n,\\
D_bZ_a&=W\{H'(\xi_a)\odot D_b\xi_a\}
 +(u\odot d_b)\langle h_b,h_a\rangle_n,
\end{aligned}
\tag{7}
\]

where \(\langle v,w\rangle_n=v^\top w/n\). Gate derivatives use
Leibniz and chain rules. In physical derivatives use
\(D=\sum_b\rho_bD_b\) and expand
\(\rho_b=(y_b-\langle u,\tanh Z_b\rangle_n)/2\) before
differentiating. Thus differentiated residuals are included exactly.

Condition on the initialized first layer and \(Z=[Z_1,Z_2]\). Set
\(H_0=[h_1,h_2]\), \(Q_n=H_0^\top H_0/n\). The conditional Gaussian
decomposition is

\[
W_0=R+ZQ_n^{-1}H_0^\top/n-RH_0Q_n^{-1}H_0^\top/n,
\qquad R_{ij}\stackrel{\rm iid}{\sim}N(0,1/n).
\tag{8}
\]

Here \(R\) is independent of the conditioning variables; only the
displayed projection of it matters. Every action of \(W_0\) or
\(W_0^\top\) is therefore a fixed finite sum of actions of \(R\) or
\(R^\top\), deterministic vector leaves, and normalized pairings.
For example,

\[
W_0v=Rv+\sum_{a,b}(Q_n^{-1})_{ab}
(Z_a-Rh_a)\langle h_b,v\rangle_n.
\tag{9}
\]

Assume \(\|Q_n^{-1}\|_{\rm op}\le C_0\) and
\(\max_{a,i}|Z_{ia}|\le R_Z\). The grammar proof in
`INITIAL_JET_MOMENTS.md` then applies to (7) after (8), with the same
matrix reused at every occurrence. For clarity, the relevant counting
does not require independence of the initialized gates:

- Each monomial is a forest with Gaussian edges, deterministic gates,
  and normalized scalar components. If it has \(E\) Gaussian edges
  and \(S\) normalized scalar components, its factor is
  \(n^{-E/2-S}\).
- In an even \(p\)-th moment, each Wick pairing leaves at most
  \(pE/2+pS\) free summed indices. A connected quotient graph has at
  most its edge count plus one vertices; one vertex is fixed in the
  rooted coordinate component. Identifications cannot increase the
  number of unrooted components. Width powers therefore cancel.
- There are at most \((pE)^{pE/2}\) pairings. Local rules (7), including
  derivatives of a matrix action, add only bounded expression size at
  one Leibniz site. After \(r\) derivatives, size and total gate order
  are \(O(r+1)\), with at most \((Cr)^{Cr}\) monomials. Expansion (8)
  increases this by only a fixed factor per matrix occurrence.

The required gate bounds are uniform. For \(H\), solve
\(H'=(1-H^2)^2\) on a complex disk around any real center. On the
supremum ball \(|H-H_0|\le1/2\), \(|H_0|\le1\), the vector field
has modulus at most 11 and derivative at most 20. The integral equation
is a contraction for disk radius \(1/64\), with image increment below
\(1/2\). Cauchy's formula on a smaller disk gives
\(|H^{(s)}|\le C^s s!\) uniformly on the real line. The same bound
for tanh follows on uniform disks inside its strip. Products of these
factorials are bounded by the factorial of their total order.

Consequently, for every \(r\ge1\) and even \(p\ge2\), each raw
coordinate of an initialized order-\(r\) jet of \(\xi_a,Z_a,u\),
each initialized scalar prediction jet, and every corresponding
sample-word jet has conditional moment bound

\[
\|\text{jet}\|_{L^p(R)}
\le [C(r+1)p(1+R_Z)]^{C(r+1)}.
\tag{10}
\]

Matrix-increment jets obey the same bound in Frobenius norm. Indeed
their terms remain rank-one matrices \(vw^\top/n\), and
\(\|vw^\top/n\|_F=(\|v\|_2/\sqrt n)(\|w\|_2/\sqrt n)\);
Minkowski and Hölder reduce this to the coordinate bounds. No
Frobenius bound on \(W_0\) itself is needed. No bound (10) on the raw
zeroth-order \(\xi_a\) is asserted: it can be large, but the equations
contain it only through uniformly bounded gates.

For these orthogonal inputs, rows of \(H_0\) are independent bounded
vectors with population Gram
\(\mathbb E\tanh^2(G)\,I_2\succ0\). Entrywise bounded-variable
concentration implies the required inverse-Gram bound except on an
exponentially small event. Conditionally on the first layer, each entry
of \(Z\) is Gaussian with variance at most one, so a union bound gives
\(R_Z=C_A\sqrt{\log(en)}\) except with probability \(O(n^{-A-2})\).
Also \(\|W_0\|_{\rm op}\le8\) except with exponentially small
probability, directly from a fixed-radius sphere net and Gaussian tails.

Choose a common even \(p=C_A\log(en)\). There are at most
\(Cn(R+1)2^{R+2}\) coordinates, scalar words, and matrix norms through
order \(R\le\log(en)\). Conditional Markov and a union bound using
each order's own threshold in (10) show that, on one event of
probability at least \(1-Cn^{-A}\), every positive-order raw vector
Taylor coefficient through any such final order \(R\) is bounded
coordinatewise by \(B^r\), and each normalized state coefficient or
matrix-increment coefficient is bounded in norm by \(B^r\), where

\[
B=[C_A(R+1)\log(en)]^{C_A}.
\tag{11}
\]

All initialized NTH entries through rank \(R\) are bounded by
\(B^s\) at rank \(s\). This is a complete conditional-Gaussian
estimate, not an assertion about one response sector.

## 4. Auxiliary preactivation jets, not auxiliary dynamics

A direct complex estimate on
\(\sqrt nW\mathcal A_n(\zeta)\) using only operator norms would
lose a factor \(\sqrt n\). To avoid that loss, form a finite Taylor
polynomial also for \(V_a=Z_a/\sqrt n\). This variable is used only
inside the proof. Its exact derivative is

\[
\dot V_a=W\{H'(\sqrt n\zeta_a)\odot\dot\zeta_a\}
 +\sum_b\rho_b C_b(A_b^\top A_a).
\tag{12}
\]

Regard (3), with \(V_a\) temporarily an independent argument, together
with (12), as an extended analytic vector field. It preserves
\(V_a=W\mathcal A_n(\zeta_a)\) for the exact initialized solution.
No stability claim for this extended vector field is needed.

Let \(P_R\) be the extended state's degree-\(R\) Taylor polynomial
with its exact initialized jets. Set \(\rho=(DB)^{-1}\), where \(D\)
is a sufficiently large fixed constant. By (11), on \(|t|\le\rho\),
every raw transformed-coordinate increment and raw second-preactivation
increment is at most
\(\sum_{r\ge1}(B\rho)^r=1/(D-1)\). Choose \(D\ge256\).
The first scalar gate then remains within its uniform complex disk,
and the second tanh remains within a fixed pole-free strip. The raw
readout polynomial has the same increment bound, since \(u_0=0\).

All normalized features, \(U\), \(W\) in operator norm, and the
extended vector field evaluated on \(P_R\) are bounded by constants
independent of width and order on this disk. In particular (12) uses
only bounded diagonal gates and normalized matrix/vector products.
Taylor matching and Cauchy's formula give the equation defect bound

\[
\|P_R'(t)-\mathcal V_{\rm ext}(P_R(t))\|
\le C\rho^{-R}t^R,\qquad 0\le t\le\rho/2.
\tag{13}
\]

Use Euclidean norms for normalized vectors and Frobenius norm for the
matrix increment. The algebraic defect

\[
E_a(t)=P_{V_a}(t)-P_W(t)\mathcal A_n(P_{\zeta_a}(t))
\]

is likewise bounded and holomorphic on the disk, and its coefficients
through degree \(R\) vanish. Thus

\[
\|E_a(t)\|_2\le C\rho^{-(R+1)}t^{R+1}.
\tag{14}
\]

For real \(t\), compare only the original-state portion
\(Q_R=(P_{\zeta_1},P_{\zeta_2},P_U,P_W)\) to the true original
state. Replacing \(P_{V_a}\) by its defining network value changes
\(\mathcal T_n\) by at most \(\|E_a\|_2\), and changes
\(d_a\odot P_U\) by at most
\(2\|\sqrt nP_U\|_\infty\|E_a\|_2\). The latter raw readout
bound is at most one after increasing \(D\). Therefore (13)–(14)
bound the defect of \(Q_R\) in the actual original vector field.
Applying the real stability estimate (6) from the common initial state
gives

\[
\|S(t)-Q_R(t)\|\le C\rho^{-R}t^{R+1}.
\tag{15}
\]

The additional integral of (14) is absorbed because \(t\le\rho/2\).
The polynomial-path observable
\(P_U^\top\mathcal T_n(P_{V_a})\) is bounded and holomorphic,
has the true prediction coefficients through degree \(R\), and has
Cauchy tail \(C\rho^{-(R+1)}t^{R+1}\). Its difference from the true
output is controlled by (14)–(15). This proves the dense part of (1)
after a fixed enlargement of \(B\).

For the original NTH put \(X_s=K_s/B^s\). Its initialized max norm
is at most one, and the exact own-residual equations are majorized
coefficientwise by \(Z'=2B^2Z^2\), \(Z(0)=1\). Consequently the
finite NTH ODE is holomorphic on \(|t|\le(4B^2)^{-1}\), with
prediction bounded by \(2B\); Cauchy's formula gives tail
\(4B(4B^2t)^{R+1}\) on \(0\le t\le(8B^2)^{-1}\).
Enlarging the fixed polynomial power in (11) puts this and the dense
bound into (1). These rank weights and polynomial paths are proof
devices, not changes to top freezing or to either residual.

## 5. What the new bridge does and does not transfer

There is a useful exact transfer with Taylor degree \(R\) left free.
Suppose an actual discrepancy has coefficient magnitude at least
\(L>0\) at degree \(j\le R\), and the remainder in (1), with
\(C_+=\max(1,C)\). Set \(X=LB^{-j}\le1\),
\(d=R+1-j\), and

\[
\tau=B^{-1}\left(\frac{X}{6C_+7^R}\right)^{1/d}.
\tag{16}
\]

The shifted-Chebyshev inequality from `NONLINEAR_RESULT.md` bounds
the supremum of its entire degree-\(R\) Taylor polynomial below by
\(L\tau^j/(3\cdot7^R)\). At this time the remainder is at most
half that bound. Hence, for the actual trajectories,

\[
\sup_{0\le t\le\tau}|f_a(t)-f_a^{(q)}(t)|
\ge
\frac{X^{(R+1)/(R+1-j)}}{6\,7^R}
(6C_+7^R)^{-j/(R+1-j)}.
\tag{17}
\]

The same formula applies to a fixed scalar contraction of predictions
after adjusting constants. It controls cancellation among all Taylor
coefficients up to degree \(R\); it does not assume positivity. For
fixed positive observation horizon \(T\), the time (16) is in
\([0,T]\) for all sufficiently large widths.

Equation (17) also quantifies the remaining fluctuation-scale difficulty.
Even if a **complete** first-missed coefficient were known with adequate
probability to satisfy \(L=n^{-1/2}A_j\), taking \(R=2j\) makes the
power of \(n^{-1/2}\) nearly two. Taking larger \(R\) reduces that
loss but introduces the polynomial coefficient factor \(7^R\).
For \(R\ge2j\), the additional logarithmic losses relative to
\(\log L\) are bounded above, up to constants, by

\[
R+\frac{j}{R}\log n+j\log B,
\tag{18}
\]

when \(A_j\ge1\) and \(L\le1\). Balancing the first two terms
suggests \(R\) of order \(\sqrt{j\log n}\), when this lies in the
proved range. This is better than forcing \(R=2j\), but still has a
substantial cost. Formula (18) is an analysis of the guaranteed bound
(17), not an impossibility theorem for sharper remainder arguments.

In particular the available scalar-star factorial \(L^2\) lower bound
does not meet the hypotheses of (17): it is neither the complete neural
coefficient nor an adequate-probability lower bound for that coefficient.
The full second-layer contraction sectors may cancel a selected chaos,
and large growing-order second moments need not imply fixed-confidence
fluctuations. To exploit a coefficient merely at the dense fluctuation
scale, a sharper same-scale remainder or a direct probabilistic analysis
of the complete discrepancy may additionally be needed.

The existing sine-witness theorem already uses a shrinking positive
early time. Replacing an endpoint norm by a worst early-time norm does
not by itself strengthen its order exponent. The substantive advance
here is (1) for the orthogonal two-tanh network: a genuine missing
trajectory-remainder sub-bridge is available, while the coefficient
noncancellation and small-ball steps remain unresolved. No stronger
storage conclusion is claimed.
