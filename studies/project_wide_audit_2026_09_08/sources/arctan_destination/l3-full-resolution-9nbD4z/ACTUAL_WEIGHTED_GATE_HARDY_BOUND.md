# Actual uncompressed gate control and its Hardy history

## Scope

This note gives a new bound on the UNCOMPRESSED active gate difference,
using the actual rare-path estimate from RARE_BACKWARD_ENERGY.md.
No nested-pruned Gaussian events are needed. Its remaining term is
an explicit average of distance histories over larger deleted sets.
The resulting hierarchy is not claimed to close global continuation.

All networks are the canonical ZERO-initial-readout finite proxies.
The full and pruned network are both uncut or use the same prescribed
coordinatewise clipping \(\tau\), with \(|\tau(x)|\le|x|\) and
Lipschitz constant at most one. Constants are uniform in that
prescribed clipping, not on a single event over all clipping levels.
There is no global transfer to the tiny-random-readout finite target.

Use normalized vector norms and inner products, and ordinary
Frobenius norms for matrix differences. Fix a finite feature horizon
\(S\). All statements below hold on the already proved common event
of ACTUAL_RARE_BACKWARD_DERIVATIVE.md, together with the initial
operator-bound event. There is no further probability allocation.
Let \(\epsilon_n\) be its vanishing width error.

## 1. State envelopes and the prefix-time query bound

For each deleted set \(E\), define the squared full-state distance
\[
 \begin{split}
 y_E(t)={}&\|X^{(1)}-\widehat X^{(1)}\|_n^2
       +\|W^{(2)}-\widehat W^{(2)}\|_{\rm F}^2\\
     &+\|W^{(3)}-\widehat W^{(3)}\|_{\rm F}^2
       +\|W^{(4)}-\widehat W^{(4)}\|_n^2 .
 \end{split}
 \tag{1}
\]
Hats in each term refer to the single fully pruned network for \(E\).
The earlier sum distance satisfies \(d_E\le2\sqrt{y_E}\).
All \(y_E(0)=0\), and the primal estimates bound \(y_E\) uniformly
in \(E,n,t\le S\).

Define, for \(0\le r\le1\),
\[
 Y_r(t)=\max_{|F|\le\lfloor nr\rfloor}y_F(t).
 \tag{2}
\]
In particular \(Y_r(t)=0\) for \(r<1/n\), because only the empty
deletion is allowed there. The envelopes are nondecreasing in \(r\);
no time supremum is included in (2).
Set
\[
 \Phi(x)=\mu(\sqrt x)^2
       =x[1+\tfrac12\log_+(1/x)],\qquad \Phi(0)=0.
 \tag{3}
\]
This function is nondecreasing, and
\(\mu(d_E)^2\le4\Phi(y_E)\).

Let the actual, uncut top-transpose query be
\[
 q(t)=(W^{(3)}(t))^*\delta^{(3)}(t),\qquad
 q_{*,i}(t)=\sup_{0\le u\le t}|q_i(u)|.
 \]
This definition of \(q\) is unchanged if the middle update uses
clipping. The zero readout gives \(q(0)=0\).
Retaining the time factors in the rare-energy proof, one has for
every fixed \(F\), with \(f=|F|/n\),
\[
 \int_0^t\|P_F\delta^{(2)}(u)\|_n^2du
 \le C_{S,M}\left[
 t(h(f)+\epsilon_n^2)+
                   \int_0^t\mu(d_F(u))^2du\right].
 \tag{4}
\]
Squaring the actual rare derivative estimate and using (4) gives
the same right side for \(\int_0^t\|P_Fq'(u)\|_n^2du\).
Coordinatewise Cauchy--Schwarz then gives
\[
 \|P_Fq_*(t)\|_n^2
 \le C_{S,M}\left[
 t^2(h(f)+\epsilon_n^2)
                 +t\int_0^t\mu(d_F(u))^2du\right].
 \tag{5}
\]
There is no interchange of a coordinatewise time supremum with
an empirical norm.

Consequently, writing
\[
 M_r(t)=\max_{|F|\le\lfloor nr\rfloor}\|P_Fq_*(t)\|_n^2,
 \]
one has \(M_r=0\) for \(r<1/n\), and for \(r\ge1/n\),
\[
 M_r(t)\le C_{S,M}\left[
 t^2(h(r)+\epsilon_n^2)
                  +t\int_0^t\Phi(Y_r(u))du\right].
 \tag{6}
\]
Taking the maximum inside the time integral only enlarges the
bound. Equation (6) concerns a single actual path, simultaneously
over every subset; a subset may therefore be chosen from the
gate difference at a later stage.

## 2. The actual query eliminates the need for nested references

Fix \(E\), put \(Q_E=I-P_E\), and abbreviate
\[
 D_2=\operatorname{diag}(\phi'(z^{(2)})),\qquad
 \widehat D_2=\operatorname{diag}(\phi'(\widehat z^{(2)})).
 \]
The problematic active vector is
\[
 v_E=Q_E(D_2-\widehat D_2)\tau(\widehat q).
 \tag{7}
\]
The identity map is understood in the uncut case. Add and subtract
\(\tau(q)\) in (7). Since clipping is contractive and dominated
by absolute value,
\[
 |v_{E,i}(t)|
 \le \sqrt{w_i(t)}\,|q_i(t)|+|q_i(t)-\widehat q_i(t)|,
 \]
where
\[
 w_i(t)=\mathbf 1_{\{i\notin E\}}
           |\phi'(z_i^{(2)}(t))
                   -\phi'(\widehat z_i^{(2)}(t))|^2\in[0,1].
 \]
Let
\[
 a_E(t)=\frac1n\sum_iw_i(t).
 \tag{8}
\]
The already checked primal comparison bounds imply
\[
 a_E(t)\le\min\{1,C_0y_E(t)\},\qquad
 \|q(t)-\widehat q(t)\|_n^2\le C_{S,M}[y_E(t)+p],
 \quad p=|E|/n.
 \tag{9}
\]
Here \(C_0\ge1\) is deterministic and depends only on the primal
bounds. For the first estimate use \(|\phi''|\le2\) and
\(\|Q_E(z^{(2)}-\widehat z^{(2)})\|_n
\le C_{S,M}\sqrt{y_E}\).

Therefore
\[
 \|v_E(t)\|_n^2
 \le2\langle w(t),q_*(t)^2\rangle_n
                         +C_{S,M}[y_E(t)+p].
 \tag{10}
\]
Only the ACTUAL maximal path enters (10). No estimate on a
second-pruned query, and no replacement by an independent copy,
is being made.

## 3. Exact layer cake and the discrete width floor

For \(0<a\le1\) and a nonnegative nondecreasing function \(J(r)\)
which vanishes for \(r<1/n\), define
\[
 \mathcal H_{a,n}J
    =aJ(1)+a\int_{\max\{a,1/n\}}^1\frac{J(r)}{r^2}\,dr,
 \qquad \mathcal H_{0,n}J=0.
 \tag{11}
\]
This is exactly
\(\int_0^1J(\min\{1,a/u\})du\), with the convention at \(a=0\).
The lower limit in (11) records the finite-width floor; it is not
silently replaced by a continuum of nonempty subsets below \(1/n\).

At fixed time, let \(F_u(t)=\{i:w_i(t)>u\}\). Its mass is at
most \(\min\{1,a_E(t)/u\}\), even though this set can depend on
both complete trajectories. Since (6) is uniform over all sets,
layer cake and Tonelli give
\[
 \langle w(t),q_*(t)^2\rangle_n
 \le\int_0^1M_{\min\{1,a_E(t)/u\}}(t)\,du.
 \tag{12}
\]
When \(a_E=0\), the left side is zero exactly.

Put
\[
 \Psi(a)=a[1+\log(1/a)+\tfrac12\log^2(1/a)]
 \quad(0<a\le1),\qquad \Psi(0)=0.
 \tag{13}
\]
An explicit integration yields
\[
 \int_0^1 h(\min\{1,a/u\})\,du=\Psi(a).
 \]
Indeed the part \(u\le a\) contributes \(a\), and on \(u>a\)
integrate \((a/u)[1+\log(u/a)]\).
For the width error, nonempty sets can occur only for
\(u\le na\), so its contribution has the additional factor
\(\kappa_n(a)=\min\{1,na\}\).

Combining (6), (10), and (12), with \(a=a_E(t)\), proves the
actual uncompressed bound
\[
 \begin{split}
 \|v_E(t)\|_n^2\le C_{S,M}\bigg[
 &y_E(t)+p+t^2\Psi(a)
                  +t^2\epsilon_n^2\kappa_n(a)\\
 &+t\int_0^t
       \mathcal H_{a,n}\big[r\mapsto\Phi(Y_r(u))\big]\,du
 \bigg].
 \end{split}
 \tag{14}
\]
Every term is defined for all distances, including \(a=0\).
This is a bound on \(v_E\) itself, not on a Gaussian compressed
image or on a rearrangement of the unknown parameter difference.

For a monotone \(J\), \(\mathcal H_{a,n}J\) is nondecreasing in
\(a\), as is immediate from its integral representation.
Thus \(a_E(t)\) in (14) may be replaced by
\[
 A(y_E(t)):=\min\{1,C_0y_E(t)\}.
 \tag{15}
\]
The width factor may then be bounded by one.

## 4. State comparison while preserving the square-root history

The finite pair equations give a direct norm estimate
\[
 \|(\Delta X^{(1)},\Delta W^{(2)},\Delta W^{(3)},
                                  \Delta W^{(4)})'\|
 \le C_{S,M}\left[
 \sqrt{y_E}+\sqrt p+\|P_E\delta^{(2)}\|_n+\|v_E\|_n
 \right].
 \tag{16}
\]
The norm here is the product Hilbert norm in (1). To verify (16),
use
\[
 \delta^{(2)}-\widehat\delta^{(2)}
 =P_E\delta^{(2)}
   +Q_ED_2[\tau(q)-\tau(\widehat q)]+v_E
 \]
in the two lower updates. Matrix-times-vector differences and
rank-one norms control all remaining terms. The two top updates
are Lipschitz in the state on the primal bounds, with the
\(\sqrt p\) input-activation deletion term. No maximum backward
coordinate occurs in (16).

Take the derivative of \(y_E\), use Young's inequality on the rare
action term, but KEEP \(\sqrt{y_E}\|v_E\|_n\) rather than
replacing it by \(\|v_E\|_n^2\). After integration, (4) gives
\[
 y_E(t)\le C_{S,M}\left[
 t(h(p)+\epsilon_n^2)
       +\int_0^t\Phi(y_E(s))ds
       +\int_0^t\sqrt{y_E(s)}\,\|v_E(s)\|_n\,ds
 \right].
 \tag{17}
\]
Uniformly over bounded \(y\),
\[
 \sqrt y\,\sqrt{\Psi(A(y))}\le C_{S,M}\Phi(y).
 \tag{18}
\]
For small \(y\), both sides have order
\(y\log(e/y)\); for \(A(y)=1\), boundedness of the range and
\(y\ge1/C_0\) prove the inequality. Thus the pure entropy term
in (14) gives a first-order Osgood modulus in (17), not a
\(y\log^2(e/y)\) term.

The time/history factor must remain intact. Combining
(14)--(18), then taking the maximum over \(|E|\le\lfloor np\rfloor\),
gives the hierarchy
\[
 \begin{split}
 Y_p(t)\le C_{S,M}\bigg[
 &t(h(p)+\epsilon_n^2)+\int_0^t\Phi(Y_p(s))ds\\
 &+\int_0^t\bigg(
 Y_p(s)\,s\int_0^s
 \mathcal H_{A(Y_p(s)),n}
       [r\mapsto\Phi(Y_r(u))]\,du
                    \bigg)^{1/2}ds
 \bigg].
 \end{split}
 \tag{19}
\]
Monotonicity of \(\Phi\), \(A\), and the Hardy map justifies
moving each finite-set maximum inside its nonnegative integrals.
The bounds \(s\le S\) are used only in constants for the terms
already absorbed into \(\Phi\) and the width error.
The displayed factor \(s\) and the inner integration over \(u\)
have NOT been discarded.

For \(p<1/n\), \(Y_p=0\) by definition. Formula (19) concerns the
whole finite-width family, not an assumed positive continuum
value at \(p=0\).

## Exact remaining limitation

Equation (14) is genuine control of the uncompressed active gate
vector. Its leading entropy contribution has the Osgood-sized
square root \(O(\sqrt a\log(e/a))\).
However the last term is
\[
 a\,\Phi(Y_1(u))
       +a\int_{\max\{a,1/n\}}^1
                     \frac{\Phi(Y_r(u))}{r^2}\,dr,
 \]
averaged over prior times. It cannot be replaced by its value at
\(r=a\), nor bounded using \(Y_p\) alone without a further estimate
on the larger-deletion envelopes.

The coupled inequality (19) preserves this size average, the
square root, and the additional time integration. No scalar
Osgood theorem is invoked to assert that it forces
\(\lim_{p\downarrow0}\limsup_nY_p=0\).
Independent scalar testing of this hierarchy is separate from the
canonical network proof. Any failure of the majorizing hierarchy
to force continuity is not a counterexample to the actual network.
