# Residual-clock check for the symmetric two-layer tanh example

2026-10-07. Independent bounded analytic audit of the supervisor's supplied clock and cubic-coefficient formulas, using the canonical setup and this route's previously established initial-program identities. No additional scientific source, other agent's findings, experiment, or numerical quadrature was consulted.

**Verdict.** The population symmetry, clock normalization, Gaussian variance, and proposed cubic coefficient are correct under the qualifications below. In particular, the cubic coefficient is $2/3$ times the stated contraction, not that contraction itself. The exact clock belongs to a deterministic population flow with shared population residuals; symmetry of a finite-width ensemble mean is not sufficient to give each dense trajectory that clock. A local cubic truncation is not an all-time accuracy theorem.

## 1. Setup and the precise symmetry statement

There are two orthogonal training inputs $v_1=e_1,v_2=e_2$, two hidden tanh layers, and zero initial readout. Their labels are

\[
y=a(1,s),\qquad s\in\{+1,-1\},
\tag{1}
\]

where the amplitude $a$ is fixed, not width-dependent. Write $T(x)=\tanh x$ and $g(x)=T'(x)=\operatorname{sech}^2x$. The canonical physical factor $2/m$ is one because $m=2$.

At finite width, the source model is

\[
z_{1,j}=Av_j,\quad h_{1,j}=T(z_{1,j}),\quad
z_{2,j}=Wh_{1,j},\quad h_{2,j}=T(z_{2,j}),\quad
f_j=w^\top h_{2,j}/n,
\]

with $A(0)$ having iid $N(0,1)$ entries, $G=W(0)$ having iid $N(0,1/n)$ entries, and $w(0)=0$. The derivative-gated fields are

\[
\delta_{2,j}=g(z_{2,j})\odot w,\qquad
b_{1,j}=W^\top\delta_{2,j},\qquad
\delta_{1,j}=g(z_{1,j})\odot b_{1,j}.
\]

The physical velocities are

\[
\dot A=\sum_{j=1}^2c_j\delta_{1,j}v_j^\top,
\quad
\dot W=\frac1n\sum_{j=1}^2c_j\delta_{2,j}h_{1,j}^\top,
\quad
\dot w=\sum_{j=1}^2c_jh_{2,j},
\qquad c_j=y_j-f_j.
\tag{2}
\]

For a deterministic compatible population flow, replace normalized row pairings by their population expectations. Assume that this flow, or the local residual-free orbit used below, exists uniquely on the interval under discussion and respects the canonical coordinate equations. No global interval is asserted in this audit.

Let $O_s e_1=s e_2$ and $O_s e_2=s e_1$. This is an orthogonal input transformation. The transformation $A\mapsto AO_s$, with $W,w$ unchanged, sends

\[
(f_1,f_2)\mapsto(s f_2,s f_1).
\tag{3}
\]

Oddness of tanh and evenness of $g$ imply the corresponding equivariance of (2). The label vector (1) is invariant under the same output transformation, and the iid Gaussian law of $A(0)$ is invariant under right multiplication by $O_s$. Therefore the unique deterministic population law is invariant, giving

\[
f_2(t)=s f_1(t),\qquad c_2(t)=s c_1(t).
\tag{4}
\]

For a typical finite-width initialization, (4) is not an exact sample-path identity. The initialization law and ensemble statistics have the symmetry, but a realized empirical cross-Gram is not exactly zero. Averaging a finite-width equation with random residuals does not justify replacing those residuals by their average. Thus a clock inferred only from ensemble-mean symmetry would be an invalid extra step; the common population residual in (4) is essential.

## 2. The exact local clock and its parity

Define a residual-free sign orbit, parametrized by $u$, by

\[
\begin{aligned}
A'&=\delta_{1,1}v_1^\top+s\delta_{1,2}v_2^\top,\\
W'&=(\delta_{2,1}h_{1,1}^\top+s\delta_{2,2}h_{1,2}^\top)/n,\\
w'&=h_{2,1}+s h_{2,2},
\end{aligned}
\tag{5}
\]

where a prime denotes $d/du$. Use the same initialization and the corresponding population interpretation. Let $F_s(u)$ be its first population prediction. The orbit obeys the symmetry in (4), so its second prediction is $sF_s(u)$.

Since all three physical velocities in (2) contain the same scalar residual after (4), composition with

\[
\dot u=a-F_s(u),\qquad u(0)=0
\tag{6}
\]

gives exactly the physical population flow wherever both sides exist. The chain rule establishes this without assuming that $u$ is globally invertible or that the residual stays positive. Conversely, uniqueness identifies this composition with the physical solution on a common local interval.

The sign-orbit transformation $u\mapsto-u$, $w\mapsto-w$, with $A,W$ unchanged, preserves (5) and the initialization. Indeed the $A,W$ velocities are linear in $w$, while $w'$ is independent of $w$ at a fixed hidden state. Uniqueness therefore gives

\[
A(-u)=A(u),\quad W(-u)=W(u),\quad w(-u)=-w(u).
\tag{7}
\]

The feature paths and their Gram functions are even in $u$, while $F_s$ is odd. This parity is an orbit statement, not an even/odd statement in physical time $t$ after the nonlinear clock (6).

There is also an orthogonal transformation that flips only the second input coordinate. Combined with changing $s$ from $+1$ to $-1$, it shows that the deterministic first-prediction orbit is the same for the two signs. We may therefore write $F(u)$ without $s$ for this symmetric training panel. Off-diagonal feature Grams change sign. A fixed asymmetric passive input is not invariant under this transformation, so its output is not determined by the training symmetry alone.

## 3. Initialization constants and the complete first return

Take independent lower roots $X_1,X_2\sim N(0,1)$ and write $H_j=T(X_j)$. Set

\[
\sigma^2=\mathbb E[T(X)^2],\qquad
q_X=\mathbb E[g(X)^2],\qquad
\tau_X=\mathbb E[T(X)^2g(X)^2].
\tag{8}
\]

The initialized upper training roots $Z_1,Z_2$ are independent $N(0,\sigma^2)$. Write $K_j=T(Z_j)$ and define

\[
\begin{aligned}
\nu&=\mathbb E[T(Z)^2],&
\alpha&=\mathbb E[g(Z)],&
\beta&=\mathbb E[g(Z)^2],\\
\tau&=\mathbb E[T(Z)^2g(Z)^2],&
r_0&=\mathbb E[g(Z)^2+T(Z)T''(Z)]
     =3\beta-2\alpha.
\end{aligned}
\tag{9}
\]

Here $X\sim N(0,1)$ and $Z\sim N(0,\sigma^2)$ in the respective expectations. The identity for $r_0$ uses $T''=-2Tg$ and $T^2=1-g$.

At $u=0$, all hidden velocities vanish and

\[
Q:=w'(0)=K_1+sK_2,\qquad
d_1=g(Z_1)Q.
\tag{10}
\]

The initial transpose return has lower row law

\[
B_1:=b_{1,1}'(0)
=\zeta_1+r_0H_1+s\alpha^2H_2,
\tag{11}
\]

where $\zeta_1$ is centered Gaussian independent of the lower roots. Its variance is the full uncentered second moment of the reverse input:

\[
\begin{aligned}
\mathbb E\zeta_1^2
&=\mathbb E[g(Z_1)^2(K_1+sK_2)^2]\\
&=\mathbb E[g(Z)^2T(Z)^2]
  +\mathbb E[g(Z)^2]\mathbb E[T(Z)^2]\\
&=\tau+\nu\beta.
\end{aligned}
\tag{12}
\]

The mixed term vanishes by oddness and independence, and $s^2=1$. The reaction variance is not subtracted from (12). In particular $B_1$ itself has the larger variance

\[
\mathbb E B_1^2=\tau+\nu\beta+\sigma^2(r_0^2+\alpha^4).
\tag{13}
\]

Nor should the first and second Gaussian returns be assumed independent: their joint covariance is the uncentered pairing of their reverse inputs. The one-coordinate contraction below requires only (11)–(12) and the Gaussian return's independence from the lower roots.

The derivative coefficients in (11) can be checked directly:

\[
\mathbb E\partial_{Z_1}d_1=r_0,
\qquad
\mathbb E\partial_{Z_2}d_1=s\alpha^2.
\]

Thus both the variance and the signs in the supplied return law are correct.

## 4. Compute the cubic contraction by exact adjointness

Let $J_{1,1}=h_{1,1}''(0)$ and $J_{2,1}=h_{2,1}''(0)$ along (5). Orthogonality of the two training inputs gives

\[
J_{1,1}=g(X_1)^2B_1.
\tag{14}
\]

At finite width, before taking initial-program limits, the product rule is exactly

\[
z_{2,1}''(0)=W''(0)h_{1,1}(0)+G h_{1,1}''(0),
\tag{15}
\]

because both $W'(0)$ and $h_{1,1}'(0)$ vanish. The initial lower training Gram tends to $\sigma^2I_2$, so the middle-learning contribution to the upper feature acceleration is

\[
J_{2,1}^{\mathrm{middle}}=\sigma^2 g(Z_1)^2Q.
\]

It follows from (12) that

\[
\mathbb E[QJ_{2,1}^{\mathrm{middle}}]
=\sigma^2(\tau+\nu\beta).
\tag{16}
\]

For the remaining term, do not assume that $G$ acts independently on the adapted lower acceleration. At finite width, exact adjointness instead gives

\[
\frac1n\langle Q\odot g(z_{2,1}),G h_{1,1}''(0)\rangle
=\frac1n\langle G^\top d_1,h_{1,1}''(0)\rangle.
\tag{17}
\]

The established joint first-return law then identifies the limiting contraction as

\[
\mathbb E[B_1J_{1,1}]=\mathbb E[g(X_1)^2B_1^2].
\]

Substitute (11). Gaussian centering removes its cross terms with lower features, and independence/oddness removes the $H_1H_2$ term. Therefore

\[
\mathbb E[g(X_1)^2B_1^2]
=q_X(\tau+\nu\beta)+r_0^2\tau_X
 +\alpha^4q_X\sigma^2.
\tag{18}
\]

Combining (16) and (18) proves the proposed formula

\[
\mathcal B:=\mathbb E[QJ_{2,1}]
=(\sigma^2+q_X)(\tau+\nu\beta)
 +r_0^2\tau_X+\alpha^4q_X\sigma^2.
\tag{19}
\]

The terms have separate origins: explicit middle learning; propagated centered Gaussian return variance; self-feature reaction alignment; and cross-feature reaction alignment. Every term is nonnegative, and $\mathcal B>0$.

## 5. The factor four and the cubic coefficient

The prediction along the orbit is $F(u)=\mathbb E[w(u)h_{2,1}(u)]$. At zero, $w=0$, $h_{2,1}'=0$, $w'=Q$, and

\[
w'''(0)=J_{2,1}+sJ_{2,2}.
\]

Hence the product rule gives

\[
F'''(0)
=\mathbb E[(J_{2,1}+sJ_{2,2})K_1]
 +3\mathbb E[QJ_{2,1}].
\tag{20}
\]

The signed-exchange symmetry from Section 1 implies
$\mathbb E[K_1J_{2,2}]=\mathbb E[K_2J_{2,1}]$:
both factors acquire a sign $s$, whose product is one. The first expectation in (20) is therefore exactly $\mathcal B$. Consequently

\[
F'''(0)=4\mathcal B,
\qquad \kappa=\frac{F'''(0)}{6}=\frac23\mathcal B.
\tag{21}
\]

Also $F'(0)=\mathbb E[QK_1]=\nu$. Orbit parity removes the even coefficients. Under local $C^5$ regularity of this population orbit with bounded fifth derivative on a neighborhood, Taylor's theorem gives

\[
F(u)=\nu u+\kappa u^3+O(u^5),\qquad
\kappa=\frac23\left[
(\sigma^2+q_X)(\tau+\nu\beta)
+r_0^2\tau_X+\alpha^4q_X\sigma^2\right].
\tag{22}
\]

Without that local population regularity assertion, the calculation still establishes the indicated initialized finite-program derivative coefficients and their parity; it should not manufacture a uniform remainder bound merely from the formal series. This distinction does not affect the coefficient audit.

An independent bookkeeping check follows from symmetry:
$2F=\mathbb E[w(h_{2,1}+sh_{2,2})]=\mathbb E[ww']$.
Thus $F=(\mathbb E w^2)'/4$. Expanding $w=uQ+u^3(J_{2,1}+sJ_{2,2})/6+\cdots$ again gives $\nu$ and $2\mathcal B/3$. This catches either a missing readout-acceleration contribution or an erroneous Taylor factorial.

The decimal values supplied in the assignment, approximately $\nu=0.2364504$ and $\kappa=0.1811526$, were not independently recomputed here. Formula (22), including its normalization, is the analytically verified result; decimal certification is a separate quadrature check.

## 6. Feature coefficients, physical time, and the reduced approximation

The previously checked cross-feature jets have the orbit form

\[
\begin{aligned}
C^1_{12}(u)&=s b_1u^2+O(u^4),
&b_1&=\sigma^2q_X\alpha^2,\\
C^2_{12}(u)&=s b_2u^2+O(u^4),
&b_2&=(\sigma^2+q_X)\nu\beta+\sigma^2q_X\alpha^4.
\end{aligned}
\tag{23}
\]

The stated remainders require the corresponding local $C^4$ regularity. Since $u'(0)=a$, their physical initial accelerations are $2sa^2b_1$ and $2sa^2b_2$, matching $2y_1y_2b_\ell$ in the canonical source clock. There is no extra factor of $2/m$ to insert for this two-sample example.

The even-in-$u$ expansions need not be even in physical time. For example $u''(0)=-\nu a$. Consequently a feature term proportional to $u^2$ also creates a physical $t^3$ term. As another normalization check, (6) and (22) give

\[
f_1'(0)=a\nu,\qquad
f_1''(0)=-a\nu^2,\qquad
f_1'''(0)=a\nu^3+6\kappa a^3.
\tag{24}
\]

These physical derivatives are different objects from $F'''(0)$ along the residual-free orbit.

The proposed explicit one-state approximation is therefore correctly normalized:

\[
\dot u=a-\nu u-\kappa u^3,\qquad u(0)=0.
\tag{25}
\]

Its training outputs are approximated by $(\nu u+\kappa u^3)(1,s)$, and (23) gives optional leading cross-feature observables. The coefficients come solely from initialization Gaussian expectations. They are not fitted trajectory coefficients, and the same coefficients apply to both signs in this orthogonal symmetric population example.

This is a genuine reduced model of that restricted example. Its exact antecedent (6) still needs the whole orbit function $F$, while (25) replaces that function by a local cubic. Positivity of $\nu,\kappa$ makes the cubic scalar equation well behaved, but does not establish its error relative to the exact orbit for arbitrary amplitude, long time, finite width, nonsymmetric data, or passive outputs. A passive observable requires its own orbit function or separately justified expansion. Numerical agreement in selected regimes cannot supply those missing error bounds.
