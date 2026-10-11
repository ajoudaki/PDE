# Correlated balance geometry and the missing variation bound

2026-10-11. Scoped theoretical attempt. Scientific inputs were the supervisor's
model and checked convergence-or-escape statement, `docs/notation.qmd`, and the
complete assigned `GAUSSIAN_RANK_ONE_COMPLETION.md`,
`TWO_SAMPLE_ESCAPE_ROUTE.md`, and, after explicit expansion of scope,
`BOUNDEDNESS_RENEWAL.md`. Required mathematical and research skills were read.
No experiment, external theorem, altered initialization, frozen layer, or Git
operation was used. These are internally derived partial results.

The requested unconditional result remains open. The new results here are an
explicit coercive integrating factor for the correlated balance, a reduction
of boundedness to cumulative variation of middle-column norms, and a stronger
obstruction to universal first integrals. In particular, for nonzero
correlation, **no nonconstant twice differentiable universal first integral
depending only on a first row's two preactivations and its middle-column
squared norm exists**. This extends the earlier obstruction, which concerned
only an additive potential. A closed-loop construction shows that finite
gradient-energy-type bounds do not repair that obstruction by themselves.
The construction is a test of the proposed estimates, not a nonfitting
trajectory of the neural network.

## 1. Exact model and the balance under investigation

Fix two unit inputs \(x_1,x_2\in\mathbb R^d\) with
\(\rho=x_1^\top x_2\in(-1,1)\), fixed labels
\(y=(y_1,y_2)^\top\ne0\), and finite width \(n\ge1\). The actual
parameters are \(A\in\mathbb R^{n\times d}\),
\(W\in\mathbb R^{n\times n}\), and \(w\in\mathbb R^n\). Set
\[
p_a=Ax_a,\qquad u_a=\tanh p_a,\qquad
z_a=Wu_a,\qquad h_a=\tanh z_a,
\qquad f_a=\frac1n w^\top h_a,
\]
\[
r_a=f_a-y_a,\qquad
\mathcal L=\frac12(r_1^2+r_2^2),\qquad
D_a=\operatorname{sech}^2p_a,\qquad
E_a=\operatorname{sech}^2z_a,\qquad
B_a=W^\top(w\odot E_a).
\]
The nonlinearities and products involving \(D_a,E_a\) act entrywise.
The mobilities are exactly \((n,1,n)\), so
\[
\begin{aligned}
\dot w&=-r_1h_1-r_2h_2,\\
\dot W&=-\frac1n\left[
r_1(w\odot E_1)u_1^\top+r_2(w\odot E_2)u_2^\top\right],\\
\dot A&=-r_1(D_1\odot B_1)x_1^\top
         -r_2(D_2\odot B_2)x_2^\top,\\
\dot p_1&=-r_1D_1\odot B_1-\rho r_2D_2\odot B_2,\\
\dot p_2&=-\rho r_1D_1\odot B_1-r_2D_2\odot B_2.
\end{aligned}                                                    \tag{1}
\]
Initialization remains independent \(A_{ij}(0)\sim N(0,1)\),
\(W_{ij}(0)\sim N(0,1/n)\), and exactly \(w(0)=0\). No statement
below changes the law or exchanges the finite-width and infinite-time limits.

For one first-layer neuron \(j\), suppress \(j\) in its two scalar
preactivations and define
\[
R=\|W_{:,j}\|_2^2,\qquad
v_a=-r_aB_{ja},\qquad
C=\begin{pmatrix}1&\rho\\\rho&1\end{pmatrix},\qquad
D=\operatorname{diag}(\operatorname{sech}^2p_1,
                      \operatorname{sech}^2p_2).
\]
Here \(C=X^\top X\), with \(X=(x_1,x_2)\), is the unnormalized
two-input Gram matrix; it is \(d\) times the book's normalized Gram.
Equation (1) implies the exact pair
\[
\dot p=CDv,\qquad
\frac n2\dot R=\tanh(p_1)v_1+\tanh(p_2)v_2.                  \tag{2}
\]
Since \(C,D\) are invertible at finite parameters, elimination of \(v\)
gives
\[
\frac n2\,dR=\alpha,
\qquad
\alpha=
\frac{q(p_1)-\rho q(p_2)}{1-\rho^2}\,dp_1
+\frac{q(p_2)-\rho q(p_1)}{1-\rho^2}\,dp_2,
\qquad q(p)=\sinh p\cosh p.                                 \tag{3}
\]
The differential notation in (3) means equality after evaluation on the
actual time derivative. It does not make \(\alpha\) an exact differential.

## 2. A coercive integrating factor and an exact history correction

Define the sum and difference of these two preactivations and a scalar
potential by
\[
s=p_1+p_2,\qquad d_-=p_1-p_2,\qquad
F_\rho(p_1,p_2)=\frac12\left[
\frac{\log\cosh s}{1+\rho}
+\frac{\log\cosh d_-}{1-\rho}\right].                       \tag{4}
\]
The subscript on \(d_-\) distinguishes this scalar from the input dimension.
Put
\[
K=\cosh s\cosh d_-
  =1+\sinh^2p_1+\sinh^2p_2\ge1.
\]
Then (3) has the exact integrating-factor form
\[
\alpha=K\,dF_\rho,
\qquad
\frac n2\dot R=K\dot F_\rho.                                \tag{5}
\]
To verify it, use
\(q(p_1)+q(p_2)=\sinh s\cosh d_-\) and
\(q(p_1)-q(p_2)=\cosh s\sinh d_-\) in (3). The resulting
coefficients of \(ds,dd_-\) are
\[
\alpha=
\frac{\sinh s\cosh d_-}{2(1+\rho)}\,ds
+\frac{\cosh s\sinh d_-}{2(1-\rho)}\,dd_-,
\]
which are precisely \(K\) times the two derivatives of (4).

This is a coercive potential: since
\(\log\cosh z\ge |z|-\log2\) and
\(|p_1+p_2|+|p_1-p_2|=2\max\{|p_1|,|p_2|\}\),
\[
F_\rho\ge
\frac{\max\{|p_1|,|p_2|\}-\log2}{1+|\rho|}.                 \tag{6}
\]
It also controls the integrating factor quantitatively:
\[
e^{2(1-|\rho|)F_\rho}
\le K\le e^{2(1+|\rho|)F_\rho}.                             \tag{7}
\]
Indeed, write \(a=\log\cosh s\ge0\),
\(b=\log\cosh d_-\ge0\). Then \(\log K=a+b\), whereas
\(2F_\rho=a/(1+\rho)+b/(1-\rho)\), giving both inequalities.

Equation (5) says that \(R\) and \(F_\rho\) always have the same
sign of derivative. It does not assert that \(R\) is a function of
\(F_\rho\): \(K\) varies along a level set of \(F_\rho\) when
\(\rho\ne0\).

An exact history correction makes the missing term explicit. Let
\(\xi=\cosh s\), \(\eta=\cosh d_-\), so \(K=\xi\eta\), and
define the signed integral
\[
\mathcal A(t)=\int_0^t
\bigl[\xi(\tau)\dot\eta(\tau)
      -\eta(\tau)\dot\xi(\tau)\bigr]\,d\tau.
\]
Straight expansion of (3) gives
\[
\alpha=\frac{dK+\rho(\xi\,d\eta-\eta\,d\xi)}
                 {2(1-\rho^2)},
\]
hence the exact identity
\[
n(1-\rho^2)R(t)-K(t)-\rho\mathcal A(t)
=n(1-\rho^2)R(0)-K(0).                                     \tag{8}
\]
At \(\rho=0\), this is the existing orthogonal invariant. For
\(\rho\ne0\), the signed history term has neither a proved sign nor
a proved finite bound along the actual neural-network flow. Calling (8)
a conserved augmented quantity does not supply a coercive bound, because
\(\mathcal A\) records the unresolved trajectory integral.

## 3. A precise sufficient condition, and the necessary variation mechanism

For the actual trajectory of column \(j\), define its cumulative increase
after time \(T\) by
\[
V_j^+(T,t)=\int_T^t\max\{\dot R_j(\tau),0\}\,d\tau,
\qquad R_j=\|W_{:,j}\|_2^2.
\]
Equations (5)--(6), using \(K\ge1\), prove
\[
\begin{aligned}
F_\rho(p_{j1}(t),p_{j2}(t))
&\le F_\rho(p_{j1}(T),p_{j2}(T))
   +\frac n2 V_j^+(T,t),\\
\max_a|p_{ja}(t)|
&\le (1+|\rho|)\left[
F_\rho(p_{j1}(T),p_{j2}(T))
+\frac n2 V_j^+(T,t)\right]+\log2.
\end{aligned}                                               \tag{9}
\]
For the first inequality, integrate
\(\dot F_\rho=n\dot R_j/(2K)\); its negative part can be discarded
in an upper bound, and its positive part is at most
\(n\max\{\dot R_j,0\}/2\).

Consequently, if
\[
\sup_{t\ge0}\|w(t)\|_2<\infty,
\qquad
V_j^+(0,\infty)<\infty\quad\text{for every }j,                \tag{10}
\]
then every parameter remains bounded. Indeed, (9) bounds \(P=AX\),
and
\(R_j(t)\le R_j(0)+V_j^+(0,\infty)\) bounds every column of
\(W\). Finally, the part of \(A\) orthogonal to the data span is
constant by (1), and the exact reconstruction is
\[
A(t)=A(0)(I-XC^{-1}X^\top)+P(t)C^{-1}X^\top.                \tag{11}
\]
Thus \(A\) is bounded too. This proof is deterministic, applies to
arbitrary labels, and imposes no sign condition on \(A,W,w\).

Combining this implication with the supervisor's internally checked
Gaussian convergence-or-escape statement gives fitting on the event (10).
For two inputs its width condition is simply \(n\ge1\). More precisely,
outside the null set in that checked statement,
\[
\text{(10)}\quad\Longrightarrow\quad\mathcal L(t)\longrightarrow0.
                                                                    \tag{12}
\]
This is a conditional corollary, not proof that event (10) has probability
one. The present note does not independently reprove the supplied
convergence-or-escape theorem.

There is also a necessary condition that sharpens the bounded-middle escape
case. Outside the same Gaussian null set, if \(W,w\) are bounded and
\(\mathcal L_\infty>0\), then at least one \(R_j\) has infinite
cumulative positive variation. Since that \(R_j\) itself is bounded,
its cumulative negative variation must be infinite as well: their difference
is exactly \(R_j(t)-R_j(0)\). In particular, no eventual monotonicity
of every middle-column squared norm is compatible with this kind of bad
escape. The required obstruction is repeated variation, even though each
column norm can stay inside a finite interval.

## 4. No universal scalar first integral of the full three-variable balance

The earlier nonintegrability calculation rules out a potential of the form
\(R-F(p_1,p_2)\). The following statement allows an arbitrary nonlinear
dependence on all three variables.

**Proposition.** Fix \(0<|\rho|<1\). On a connected open subset of
\(\mathbb R^2\times(0,\infty)\), suppose a \(C^2\) function
\(I(p_1,p_2,R)\) is conserved by (2) for every instantaneous driving
vector \(v\in\mathbb R^2\). Then \(I\) is constant.

Write \(\alpha=\alpha_1dp_1+\alpha_2dp_2\) as in (3).
Since \(CD\) is invertible, arbitrary \(v\) gives arbitrary
\(\dot p\). Thus the two differential operators
\[
V_1=\partial_{p_1}+\frac2n\alpha_1\partial_R,
\qquad
V_2=\partial_{p_2}+\frac2n\alpha_2\partial_R
\]
both annihilate \(I\). Their commutator must annihilate \(I\) too.
Because the coefficients \(\alpha_a\) do not depend on \(R\),
\[
[V_1,V_2]
=\frac{2\rho}{n(1-\rho^2)}
\bigl[\cosh(2p_2)-\cosh(2p_1)\bigr]\partial_R.              \tag{13}
\]
At every point with \(|p_1|\ne|p_2|\), this coefficient is nonzero,
so \(\partial_R I=0\). The equations \(V_aI=0\) then give
\(\partial_{p_a}I=0\) as well. These points are dense in any open
set, and the derivatives of \(I\) are continuous. Its full gradient
therefore vanishes throughout the connected open domain, so \(I\) is
constant.

The quantifier over arbitrary backward forcing is essential. The proposition
does not rule out an invariant involving more network variables, an inequality
valid only on states reachable from zero readout, or a probabilistic argument.
It does rule out repairing the row/column balance by merely choosing a more
complicated scalar function of the same three variables.

## 5. Why finite energy alone does not control the signed history

For \(\rho\ne0\), choose a smooth closed loop in the \((s,d_-)\)
plane contained in \(s>d_->0\). By the formula preceding (5),
\[
d\alpha=
\frac{\rho}{1-\rho^2}\sinh s\sinh d_-\,ds\wedge dd_-.
                                                                    \tag{14}
\]
Thus one orientation of the loop has strictly positive circulation
\(J=\oint\alpha>0\). For example, on an oriented rectangle with
\(0<d_0<d_1<s_0<s_1\), the circulation is
\[
\frac{\rho}{1-\rho^2}
(\cosh s_1-\cosh s_0)(\cosh d_1-\cosh d_0),                \tag{15}
\]
with sign reversed when the orientation is reversed. A smooth loop enclosing
a small positive area in the same region has the same strict sign by (14).

Parametrize such a smooth loop periodically as \(p(\tau)\), with
period \(T_0\), choosing the orientation for which \(J>0\). Traverse
it with the slow clock \(\tau=\log(1+t)\), and set
\[
R(t)=R_0+\frac2n\int_0^{\log(1+t)}
\alpha(p(\tau))[p'(\tau)]\,d\tau.                          \tag{16}
\]
The integral equals \((J/T_0)\log(1+t)\) plus a bounded periodic
remainder. Choose \(R_0\) large enough that \(R(t)\ge1\).
Then (16) satisfies the exact balance (3), has bounded preactivations, and
obeys
\[
R(t)=\frac{2J}{nT_0}\log(1+t)+O(1)\longrightarrow\infty.
\]
If a column vector is assigned length \(\sqrt{R(t)}\) in a fixed
direction, its squared velocity and the squared preactivation velocity are
integrable:
\[
\|\dot p(t)\|_2=O((1+t)^{-1}),\qquad
\left|\frac d{dt}\sqrt{R(t)}\right|=O((1+t)^{-1}).           \tag{17}
\]
The first bound uses the bounded periodic derivative of \(p\), and
the second follows from bounded periodic circulation density, \(R\ge1\),
and the chain rule. Both squared bounds integrate over \([0,\infty)\).
The column displacement is only \(O(\sqrt{\log(1+t)})=o(\sqrt t)\).

This construction is not asserted to satisfy the network's \(W,w,A\)
equations or its loss identity. It proves the narrower, useful obstruction:
the exact row/column balance together with finite squared speed and the
sub-\(\sqrt t\) displacement estimate cannot alone force boundedness.
They permit repeated signed circulation. An actual fitting proof must use
additional coupling from the neural-network equations to exclude it.

## 6. Exact remaining obligations

The positive target would follow from (10), but neither ingredient of (10)
is established here under the canonical Gaussian initialization. In particular,
finite gradient energy gives \(L^2\) control of velocities, while
\(V_j^+\) requires an \(L^1\) bound on
\(\max\{2\langle W_{:,j},\dot W_{:,j}\rangle,0\}\).
Even bounded \(W\) does not bridge that difference on an infinite interval.
Equations (14)--(17) expose why the formal balance does not bridge it either.

The no-first-integral proposition concerns only a universal function of
\((p_{j1},p_{j2},R_j)\). It leaves open a coercive estimate using the
full trained state and the exact residual feedback. No Gaussian event of
positive-loss escape, let alone one with probability bounded away from zero
as width grows, is constructed. No boundedness or fitting theorem for
arbitrary fixed labels is claimed beyond the explicit conditional corollary
(12).
