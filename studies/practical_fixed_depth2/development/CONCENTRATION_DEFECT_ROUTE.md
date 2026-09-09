# Concentration defects, exact Gaussian actions, and physical forcing

2026-09-08. This note studies the smooth energy-dissipating approximations in
ENERGY_ROUTE.md for the fixed activation and raw metric in ../CONTRACT.md.
No experiment or external theorem is used. The Gaussian calculation below is
one fixed forward/reverse/forward query, not a new general source projection
theory.

**Result.** The learned rank updates and bounded multipliers admit a useful
concentration-defect estimate. The unresolved step is the initialized action:
the actual canonical Gaussian action can turn uniformly subGaussian input
paths into concentrating outputs, even when the paths start at the exact
initialization and all gate paths are uniformly \(L^2\)-Lipschitz in time.
An auxiliary family can additionally satisfy the exact raw energy identity.
It does not satisfy the true gradient equations or the cap equations.

There is also a positive physical statement: the caps' first nonzero
first-layer forcing belongs to a strongly compact family, and has uniformly
vanishing projection on the concentrating modes in the example. This is only
an initialization statement. No positive-time cap removal is established.

## 1. Concentration amplitude and the exact affine remainder

For a family \(\mathscr F\subset L^2(\Omega;\mathbb R^m)\) bounded in \(L^2\),
define

\[
d_\eta(\mathscr F)
=\sup_{X\in\mathscr F}\sup_{\mu(B)\le\eta}\|\mathbf1_BX\|_2,
\qquad
d(\mathscr F)=\lim_{\eta\downarrow0}d_\eta(\mathscr F).
\tag{1}
\]

The limit exists by monotonicity. The equality \(d(\mathscr F)=0\) is uniform
integrability of the squared amplitudes. It is weaker than strong
precompactness: an orthogonal Rademacher family has defect zero.

Three elementary facts will be used.

1. If \(\sup_X\|b_X\|_\infty\le K\), then
   \(d(\{b_XX:X\in\mathscr F\})\le Kd(\mathscr F)\).
2. A strongly compact \(L^2\) family has defect zero. Cover it by a finite
   \(L^2\) net and use absolute continuity of each net point's squared
   integral.
3. If \(\phi(x)=a x+b+\psi(x)\) with \(\psi\) uniformly bounded, then
   \[
   d(\{\phi(X):X\in\mathscr F\})=|a|d(\mathscr F).
   \tag{2}
   \]
   Indeed the two restricted norms differ by at most
   \((|b|+\|\psi\|_\infty)\sqrt\eta\), by both triangle inequalities.

Here \(a=3/4\), \(b=3/4\), and \(\psi=\tfrac14\tanh\). Thus the nonlinear
remainder contributes zero concentration defect; it does not eliminate a
defect in its argument. The gate families have defect zero automatically,
since \(3/4\le\phi'\le1\).

If \(X_R(t)=\int_0^t Y_R(s)\,ds\), then for each \(\eta\),

\[
\sup_R\sup_{\mu(B)\le\eta}\|\mathbf1_BX_R(t)\|_2
\le\int_0^t\sup_R\sup_{\mu(B)\le\eta}
                   \|\mathbf1_BY_R(s)\|_2\,ds.
\tag{3}
\]

Minkowski proves this without a common maximizing event. Uniform \(L^2\)
bounds and dominated convergence then pass \(\eta\downarrow0\).
Finite sums obey the corresponding triangle inequality.

## 2. What the actual energy-cap equations control

Use \(A_R=A_0+U_R\) and the true fields

\[
z_{R,i}=w_R\cdot u_i,\quad h_{R,i}=\phi(z_{R,i}),\quad
v_{R,i}=A_Rh_{R,i},\quad k_{R,i}=\phi(v_{R,i}),
\]
\[
b_{R,i}=C_R\phi'(v_{R,i}),\qquad q_{R,i}=A_R^*b_{R,i}.
\]

The caps retain the true adjacent update, cap the entire readout velocity,
and multiply the entire first-layer direction by a scalar in \([0,1]\).
All statements below apply to both the unweighted and residual-weighted
first-layer cap from ENERGY_ROUTE.md.

Fix \(T\). Their exact dissipation gives a common raw ball and hence common
bounds on residuals, actions, fields, and raw speeds. The true rank formulas
are

\[
U_R(t)=-\int_0^t\sum_j r_{R,j}(s)b_{R,j}(s)\otimes h_{R,j}(s)\,ds.
\tag{4}
\]

Therefore, for a fixed observation time \(t\),

\[
\begin{split}
U_R(t)h_{R,i}(t)
&=-\int_0^t\sum_j r_{R,j}(s)b_{R,j}(s)
             \langle h_{R,j}(s),h_{R,i}(t)\rangle\,ds,\\
U_R(t)^*b_{R,i}(t)
&=-\int_0^t\sum_j r_{R,j}(s)h_{R,j}(s)
             \langle b_{R,j}(s),b_{R,i}(t)\rangle\,ds.
\end{split}
\tag{5}
\]

All scalar coefficients in these expressions are bounded by a common
\(K_T\). This retains genuine adjoints; it uses no compactness of an
Hilbert--Schmidt ball.

Write \(d_X(t)\) for the maximum over the three samples of (1), with the
family over integer caps at time \(t\); omit that maximum for \(C\).
An integer cap sequence suffices for the attempted cap-removal construction.
Equations (2)--(5), bounded multipliers, and the capped velocities give

\[
\begin{split}
d_h(t)&=\tfrac34 d_z(t),&
d_k(t)&=\tfrac34 d_v(t),&
d_b(t)&\le d_C(t),\\
d_z(t)&\le K_T\int_0^t d_q(s)\,ds,&
d_C(t)&\le K_T\int_0^t d_k(s)\,ds,\\
d_v(t)&\le d_{A_0h}(t)+K_T\int_0^t d_C(s)\,ds,&
d_q(t)&\le d_{A_0^*b}(t)+K_T\int_0^t d_h(s)\,ds.
\end{split}
\tag{6}
\]

For the first-layer estimate, \(|\phi'|\le1\), the first common cap is at most
one, and residuals and \(\Gamma\) are bounded. For the readout estimate,
\(|\tau_R(g_C)|\le|g_C|\le\sum_i|r_i||k_i|\). The Gaussian initial
preactivations have defect zero, as do \(C(0)=U(0)=0\).

Thus the learned part and the scalar activation admit a *linear*
defect estimate with two unresolved terms, \(A_0h\) and \(A_0^*b\).
Replacing their defects by operator norm times input defect would close a
zero-defect Gronwall argument, but that replacement is false even for the
actual canonical Gaussian action, as Section 4 shows.

For measurability in (3)--(6), at each fixed \(\eta\) the restricted-norm
supremum is a 1-Lipschitz function of \(X\in L^2\). Each fixed cap path is
strongly continuous, so the supremum over integer caps is measurable in
time. Taking the decreasing limit through \(\eta=1/n\) preserves
measurability. No uncountable cap supremum is used in the time integrals.

## 3. Time-regular gates do not give an operator-norm time modulus

On the raw ball, \(z_{R,i}\) and \(h_{R,i}\) have a common \(L^2\)-Lipschitz
constant. The actual product rule

\[
\dot v_{R,i}=\dot U_R h_{R,i}+A_R\dot h_{R,i}
\tag{7}
\]

and bounded actions and raw speeds give the same property for \(v_{R,i}\).
Consequently

\[
\|\phi'(z_{R,i}(t))-\phi'(z_{R,i}(s))\|_2
+\|\phi'(v_{R,i}(t))-\phi'(v_{R,i}(s))\|_2
\le K_T|t-s|.
\tag{8}
\]

This useful uniform statement does not control multiplication in operator
norm. For example, let \(\mu(B_n)=\varepsilon_n\downarrow0\),
\(e_n=\mathbf1_{B_n}/\sqrt{\varepsilon_n}\), and
\(g_n(t)=\phi'(t e_n)\). Its \(L^2\) time-Lipschitz constant is at most \(1/2\).
Yet

\[
\|M_{g_n(\sqrt{\varepsilon_n})}-M_{g_n(0)}\|_{\rm op}
=|\phi'(1)-\phi'(0)|>0.
\tag{9}
\]

Here \(M_g\) denotes multiplication by \(g\). Testing on a normalized
function supported in \(B_n\) proves the equality. Thus an argument for
nonautonomous linear equations with an operator-norm modulus cannot simply
insert (8). The next obstruction concerns even a fixed initialized action.

## 4. An exact three-query concentration mechanism for the genuine action

Select one initialized first-layer feature

\[
h_0=\phi(Z),\qquad Z=w_0\cdot u_i\sim N(0,1),\qquad
V=A_0h_0.
\]

Then \(V\) is centered Gaussian with variance \(H=\mathbb E h_0^2>0\).
Choose a nonzero smooth even function \(\rho\), supported in \((-1,1)\), and
for a sequence \(\delta\downarrow0\) set

\[
e_\delta=
\frac{\rho(V/\delta)}{\|\rho(V/\delta)\|_2},\qquad
B_\delta=\{|V|<\delta\},\qquad q_\delta=A_0^*e_\delta.
\tag{10}
\]

The bump is a smooth globally Lipschitz coordinate instruction for every
fixed \(\delta\), although its constants depend on \(\delta\).
We have \(\|e_\delta\|_2=1\), support in \(B_\delta\), and
\(\mu(B_\delta)\to0\).

The actual forward/reverse Gaussian query rule gives

\[
q_\delta=\zeta_\delta,\qquad
\zeta_\delta\sim N(0,1),
\tag{11}
\]

independent of the first-layer root \(w_0\). The return coefficient vanishes:
the derivative of the even bump is odd, so its Gaussian expectation is
zero. Equivalently \(\mathbb E[V e_\delta]=0\). For any smooth bounded-slope
function \(F(Z,q_\delta)\) of at most linear growth, the next forward query is

\[
A_0F(Z,q_\delta)
=\xi_\delta+
 \mathbb E[\partial_{\zeta}F(Z,\zeta)]\,e_\delta.
\tag{12}
\]

The primitive \(\xi_\delta\) is centered Gaussian of variance
\(\mathbb E F(Z,\zeta)^2\). It can be correlated with \(V\); no independence
between \(e_\delta\) and \(\xi_\delta\) is claimed or needed.

Here is a direct check of this particular rule against the finite Gaussian
matrix, so no arbitrary bounded-operator identity is being used. Condition
an iid \(N(0,1/n)\) matrix \(A_n\) on its first answer \(V_n=A_n h_{0,n}\).
Its conditional mean is
\(V_n h_{0,n}^T/\|h_{0,n}\|_{\ell^2}^2\), and its residual is a fresh Gaussian
matrix restricted to the orthogonal complement of \(h_{0,n}\).
The reverse answer on \(e_{\delta,n}\) therefore has mean proportional to
\(\langle V_n,e_{\delta,n}\rangle_n h_{0,n}\), which vanishes in the fixed
\(\delta\) limit by evenness. Its residual covariance is the norm of
\(e_{\delta,n}\) times a rank-one projection of the identity, yielding (11).
Conditioning the residual matrix on this reverse answer decomposes its next
forward answer into a Gaussian residual and the rank-one term

\[
e_{\delta,n}
 \frac{\langle q_{\delta,n},F_n\rangle_n}
      {\|e_{\delta,n}\|_n^2}.
\]

The normalized contraction converges to
\(\mathbb E[\zeta F(Z,\zeta)]
=\mathbb E[\partial_\zeta F(Z,\zeta)]\), by Gaussian integration by parts.
The remaining first-forward conditional mean and Gaussian residual combine
into the primitive \(\xi_\delta\), with its full covariance with \(V\).
The finite-rank projected noise terms vanish in normalized \(L^2\).
This is the fixed finite-query calculation behind (11)--(12).
All derivatives used here are bounded for a fixed \(\delta\), and the
functions have at most linear growth, so the Gaussian integrations have
integrable dominating functions and vanishing boundary terms. There is no
growing-transcript or cap-removal assertion in this calculation.

Now define genuine first-weight paths on the same canonical spaces,

\[
w_\delta(s)=w_0+\varepsilon s(1+q_\delta)u_i,\qquad
U_\delta(s)=0,\qquad \varepsilon>0.
\tag{13}
\]

They start at the exact first-weight initialization. Their first-sample
preactivation is \(Z+\varepsilon s+\varepsilon s q_\delta\), and all other
sample preactivations have the corresponding fixed Gram factor. Their
first-weight speed squared is exactly \(2\varepsilon^2\).
All these preactivations are Gaussian with means and variances uniformly
bounded on each fixed \(s\)-interval. Thus their actual features \(h_{\delta,j}\)
have uniformly subGaussian amplitudes and zero concentration defect.

Applying (12) to their actual first-sample feature gives

\[
v_{\delta,i}(s)=A_0h_{\delta,i}(s)
=\xi_\delta(s)+\kappa(s)e_\delta,
\]
\[
\kappa(s)=\varepsilon s\,
 \mathbb E\phi'(Z+\varepsilon s+\varepsilon s G)
\ge\frac34\varepsilon s,\qquad s>0,
\tag{14}
\]

where \(Z,G\) are independent standard Gaussians. The primitive Gaussian
variance is uniformly bounded on fixed intervals.

On the shrinking set \(B_\delta\), Cauchy--Schwarz gives

\[
\|\mathbf1_{B_\delta}\xi_\delta(s)\|_2
\le\|\xi_\delta(s)\|_4\,\mu(B_\delta)^{1/4}\longrightarrow0
\]

uniformly over a compact \(s\)-interval. Therefore

\[
\liminf_{\delta\downarrow0}
\|\mathbf1_{B_\delta}v_{\delta,i}(s)\|_2
\ge\kappa(s)>0.
\tag{15}
\]

The output of the *actual* initialized action has positive concentration
defect despite zero defect and Gaussian tails for its inputs. By (2), the
next feature \(k_{\delta,i}(s)=\phi(v_{\delta,i}(s))\) has a corresponding
positive defect, at least \(\tfrac34\kappa(s)\).

These paths have uniform \(L^2\)-Lipschitz gate paths at both hidden layers:
the first layer follows (13), and the second follows the bounded action
applied to a first-layer \(L^2\)-Lipschitz feature. One can also query
\(F=\phi'(Z+\varepsilon s+\varepsilon sG)\) in (12). Its return coefficient
is \(\varepsilon s\,\mathbb E\phi''(N)\), where \(N\) has positive mean
\(\varepsilon s\) and variance \(1+(\varepsilon s)^2\). It is strictly
negative: \(\phi''\) is odd and strictly negative on \((0,\infty)\), and a
Gaussian with positive mean has larger density at \(x\) than at \(-x\)
for every \(x>0\). Pairing the two half-line integrals proves the sign.
Thus bounded gate functions themselves need not be mapped into a family of
zero defect. The actual-feature calculation (14) already suffices.

This is oscillation-to-concentration transfer. The reverse inputs
\(e_\delta\) concentrate, their reverse answers \(q_\delta\) have ordinary
Gaussian amplitudes, and a return through the same matrix reinstates the
concentrating input. Suppressing that return would remove the mechanism
and change the actual action.

## 5. Adding the exact raw energy identity does not remove this generic example

The paths (13) with zero readout have constant loss and moving weights, so
they do not satisfy physical dissipation. The following extension separates
what an energy identity proves from what the actual gradient equations prove.

Assume the label vector is nonzero, as for the contract's usual \(\pm1\)
labels. Let the actual initialized top features be \(k_j^0\) and set

\[
D=\sum_j y_j k_j^0\ne0.
\tag{16}
\]

To check nonvanishing, the initialized lower feature Gram is positive
definite by the constant and first-Gaussian-chaos argument in
VARIATIONAL_ROUTE.md, Section 2. Thus the initialized top preactivation tuple
has a nondegenerate Gaussian law. If \(\sum_j y_j\phi(v_j)=0\) almost surely,
continuity and full Gaussian support make this identity valid on all of
\(\mathbb R^3\); differentiating coordinate \(j\) and using \(\phi'>0\) gives
\(y_j=0\), a contradiction. If all labels were zero, nontrivial motion with
nonincreasing nonnegative loss cannot start from loss zero; the present
energy-extension example is not asserted for that case.

Along (13), set \(C_\delta(s)=\beta s D\), \(\beta>0\), and keep \(U=0\).
Call the full path \(\gamma_\delta(s)\). Its squared raw speed is the constant

\[
N^2=2\varepsilon^2+\beta^2\|D\|_2^2,
\tag{17}
\]

independent of \(\delta\). Let \(E_\delta(s)=E(\gamma_\delta(s))\).
At \(s=0\),

\[
E_\delta'(0)=-\beta\|D\|_2^2.
\tag{18}
\]

Moreover \(E_\delta'(s)=-\beta\|D\|_2^2+O(s)\), uniformly in \(\delta\).
Indeed every \(k_{\delta,j}(s)\) has a common \(L^2\)-Lipschitz constant and
bounded \(L^2\) norm, by (13) and the bounded action. Writing
\(F_{\delta,j}(s)=\langle D,k_{\delta,j}(s)\rangle\), both \(F_{\delta,j}\)
and its derivative are uniformly bounded, and
\(F_{\delta,j}(s)-F_{\delta,j}(0)=O(s)\). The exact formulas
\(f_{\delta,j}=\beta sF_{\delta,j}\) and
\(f'_{\delta,j}=\beta F_{\delta,j}+\beta sF'_{\delta,j}\) prove the claim.

Choose \(s_0>0\) so that, uniformly in \(\delta\),

\[
\frac12\beta\|D\|_2^2
\le -E_\delta'(s)
\le\frac32\beta\|D\|_2^2,\qquad 0\le s\le s_0.
\tag{19}
\]

Reparametrize each path by the increasing deterministic clock

\[
t_\delta(s)=\int_0^s\frac{N^2}{-E_\delta'(a)}\,da.
\tag{20}
\]

Its inverse exists on a common positive physical interval \([0,T_*]\), and
(19) makes both clock derivatives uniformly bounded above and below.
For \(\Theta_\delta(t)=\gamma_\delta(s_\delta(t))\),

\[
\frac d{dt}E(\Theta_\delta(t))
=-\|\dot\Theta_\delta(t)\|_{\rm raw}^2.
\tag{21}
\]

This follows by substituting
\(s_\delta'(t)=-E_\delta'(s_\delta(t))/N^2\) into both sides.
Thus all paths have the exact initial state, the exact nonnegative raw loss,
the exact raw energy identity and its length bound, and uniformly
\(L^2\)-Lipschitz hidden gate paths.

Nevertheless concentration persists at every fixed \(t>0\): (19) gives
\(s_\delta(t)\ge c t>0\), so the same restricted-norm argument as (15) yields
a lower bound \(c'\varepsilon t\). The primitive Gaussian variance remains
uniformly bounded over \(s\in[0,s_0]\).

These are not true GF or energy-cap solutions. In particular their initial
first-weight velocity is nonzero, and their readout velocity differs from
the true readout gradient. The construction only shows that the listed
energy and time-regularity properties, even simultaneously and on the true
canonical network, do not by themselves prevent concentration.

## 6. The exact physical forcing forbids the inserted initial mode

There is a useful elementary distinction. If a path satisfies both true
equations \(\dot U=-g_U\), \(\dot C=-g_C\), and satisfies the raw dissipation
inequality, then the chain rule gives

\[
\langle g_w,\dot w\rangle\le-\|\dot w\|_2^2.
\tag{22}
\]

At \(C=0\), \(g_w=0\), so a strong path obeying this inequality must have
\(\dot w(0)=0\). The artificial family in Section 5 therefore cannot satisfy
all these requirements. Away from initialization, (22) alone still does not
specify the first gradient equation: global negative alignment allows
orthogonal components. No concentration theorem is deduced merely from it.

For the actual smooth caps, their complete first equation gives a sharper
initial fact. Put

\[
D_R=\tau_R(D),\qquad
a_R=\sum_j y_j\phi'(z_j^0)
       A_0^*[\phi'(v_j^0)D_R]\,u_j.
\tag{23}
\]

Their true initial values satisfy
\(\dot C_R(0)=D_R\), \(\dot U_R(0)=\dot w_R(0)=0\), and

\[
\lim_{t\downarrow0}\frac{\dot w_R(t)}t=a_R
\quad\hbox{in }L^2,\qquad
w_R(t)=w_0+\frac12t^2a_R+o(t^2)
\tag{24}
\]

for each fixed cap \(R\). To prove it, \(C_R(t)/t\to D_R\) and bounded
multiplier continuity give

\[
\frac{b_{R,j}(t)}t\to\phi'(v_j^0)D_R,\qquad
\frac{q_{R,j}(t)}t\to A_0^*[\phi'(v_j^0)D_R].
\]

The first cap equals the identity near zero. Its rescaled error tends to
zero in \(L^2\), because \(q_R(t)/t\) converges strongly and its relevant
tail threshold is \(R/t\to\infty\). The same argument works for the
residual-weighted cap. Substituting \(r(0)=-y\) proves (24).
This proof uses neither a full Frechet Hessian nor a trained Gaussian law.

The family \(\{a_R:R\ge1\}\) is strongly precompact. Indeed
\(\tau_R(D)\to D\) strongly in \(L^2\) as \(R\to\infty\), and depends
continuously on \(R\) for finite \(R\), by dominated convergence.
Equation (23) is a fixed bounded linear map of \(D_R\). The compactification
\(1/R\in[0,1]\) thus makes its image compact.

Meanwhile \(e_\delta\rightharpoonup0\), since it has unit norm and shrinking
support: \(|\langle e_\delta,X\rangle|\le
\|\mathbf1_{B_\delta}X\|_2\to0\) for each fixed \(X\in H_2\).
Hence \(q_\delta=A_0^*e_\delta\rightharpoonup0\), with uniformly bounded
norms (indeed norm one by (11)). A finite-net argument on the compact family
of \(a_R\) now proves

\[
\sup_{R\ge1}
|\langle a_R,q_\delta u_i\rangle|
\longrightarrow0.
\tag{25}
\]

This is genuine uniform suppression of the example's rare mode in the first
nonzero physical first-layer forcing. The artificial path inserts that mode
directly at first order.

No uniform-in-\(R\) remainder in (24), and no analogous positive-time
compactness of the reached forcing family, is proved here. Therefore (25)
must not be promoted to a continuation estimate.

## 7. Exact remaining issue

The asymptotically affine activation gives the exact defect identity (2).
The learned rank updates give the linear inequalities (6), and physical
energy gives the time-regular gate estimate (8). Those are valid pieces of
a concentration argument.

The initialized action has a same-matrix return that can convert
nonconcentrating, Gaussian-amplitude inputs into concentrating outputs.
Sections 4--5 demonstrate that this is compatible with the actual canonical
action, common initialization, smooth time gates, and even a raw energy
identity. Thus arbitrary bounded-operator counterexamples are not needed
to expose this obstacle.

The complete physical equations contain more information. In particular
they cannot freely insert the concentrating reverse input, and their first
nonzero forcing satisfies (25). Extending that restriction to every reached
time, while retaining the response chronology, is the unresolved
no-spontaneous-concentration step. This note proves neither a failure of
that step for physical caps nor the required strong canonical limit.
