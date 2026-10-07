# Orthogonal-data route: exact reduction and all-time small-label bounds

This scoped theoretical route uses only the supplied model and
`docs/notation.qmd`. The required canonical-notation skill was inaccessible at
its supplied path, including after an escalated read; no readable alternate
was found. The fallback follows the user's explicit notation requirements and
the maintained notation contract. The `investigate-conjectures` and
`solve-math-rigorously` skills and the former's research-contract and
adversarial-audit references were read. No experiment, other study, archived
book passage, or external scientific source was used.

The main fixed-label, all-time, all-sphere, polylogarithmic-storage target is
**open on this route**. Orthogonality reduces the input geometry and gives a
complete width-independent small-label stability theorem. It does not by
itself close the population dynamics in finitely many scalar variables. A
one-sample nonlinear scalar candidate below has computable coefficients and
the correct first nonlinear Taylor coefficient, but its prediction accuracy
at positive times is not proved.

## 1. Exact finite equations

Let the $m\le d$ training inputs satisfy $x_a^T x_b/d=\delta_{ab}$, and let
the labels $y_a\in\mathbb R$ have either sign. All test inputs satisfy
$\|x\|_2=\sqrt d$. Write

\[
u_a=A x_a/\sqrt d,\quad h_a=\tanh(u_a),\quad z_a=W h_a,
\quad g_a=\tanh(z_a),\quad f_a=w^Tg_a/n,
\quad r_a=f_a-y_a.
\]

Here $A\in\mathbb R^{n\times d}$, $W\in\mathbb R^{n\times n}$, and
$w\in\mathbb R^n$. The loss is $m^{-1}\sum_a r_a^2$, the block mobilities
are $(n,1,n)$, and $w(0)=0$. For vectors, activation and multiplication
by activation derivatives are coordinatewise. Define the two backpropagated
vectors, without including the residual, by

\[
b_a=w\odot\tanh'(z_a),\qquad
c_a=\tanh'(u_a)\odot W^T b_a.
\]

The exact physical-time flow is

\[
\dot w=-\frac2m\sum_a r_a g_a,\qquad
\dot W=-\frac2{mn}\sum_a r_a b_a h_a^T,\qquad
\dot A=-\frac2m\sum_a r_a c_a x_a^T/\sqrt d.
\tag{1}
\]

Consequently, orthogonality gives the exact training-coordinate equations

\[
\dot u_a=-\frac2m r_a c_a.
\tag{2}
\]

This removes the ambient input dimension from training after initialization,
but retains $nm+n^2+n$ real coordinates. In particular, (2) is not a
population closure.

For a test input, define $u_x,h_x,z_x,g_x,b_x,c_x$ by the same formulas and
put $\rho_a(x)=x_a^Tx/d$. The exact prediction equation is

\[
\dot f(t,x)=-\frac2m\sum_a K_t(x,x_a)r_a(t),
\tag{3}
\]

where

\[
K_t(x,x_a)=\frac{g_x^Tg_a}{n}
+\frac{b_x^Tb_a}{n}\frac{h_x^Th_a}{n}
+\rho_a(x)\frac{c_x^Tc_a}{n}.
\tag{4}
\]

The training matrix $K(t)=(K_t(x_a,x_b))_{a,b}$ is positive semidefinite.
Its first contribution is the readout Gram; its second contribution is a
Gram matrix of matrix gradients; and its third is the diagonal matrix
$\operatorname{diag}(\|c_a\|_2^2/n)$ because the inputs are orthogonal.
At initialization only the first contribution remains. Denote it by

\[
(K_0)_{ab}=g_a(0)^Tg_b(0)/n.
\]

There is also an exact reduction for evaluation. Since every increment of
$A$ has its input direction in the training span,

\[
u(t,x)=u(0,x)+\sum_a\rho_a(x)\bigl(u_a(t)-u_a(0)\bigr).
\tag{5}
\]

For any one fixed test input, the Gaussian initialization implies

\[
u(t,x)=\sum_a\rho_a(x)u_a(t)
+\sqrt{1-\|\rho(x)\|_2^2}\,\xi,
\tag{6}
\]

in conditional distribution given the entire training trajectory, where
$\xi\sim\mathcal N(0,I_n)$ is independent of that trajectory. This is
legitimate because the initial component of $A$ orthogonal to the training
span is independent of $(u_a(0))_a,W(0)$ and never changes. It does not
authorize fresh independent Gaussian replacements for $W$, $W^T$, or
their actions during training. A simultaneous finite-realization statement
over different test inputs must also preserve the joint Gaussian coupling
of their orthogonal components.

## 2. Complete deterministic all-time theorem

Assume

\[
\|W(0)\|_{\mathrm{op}}\le M,\qquad K_0\succeq\lambda I_m,
\qquad M\ge0,\quad\lambda>0.
\tag{7}
\]

Write $Y=\|y\|_2$, and define

\[
R=\frac{2\sqrt m\,Y}{\lambda},\qquad
B(s)=\frac{M s^2}{2}+\frac{s^4}{8},\qquad
C(s)=\frac{(1+M^2)s^2}{2}+\frac{M s^4}{8}.
\tag{8}
\]

Suppose the labels satisfy the explicit smallness condition

\[
2m C(2R)\le\lambda/2.
\tag{9}
\]

Then the flow exists for all $t\ge0$, all parameters have finite limits,
and

\[
\begin{aligned}
\|r(t)\|_2&\le Y e^{-\lambda t/m},\\
\|w(t)\|_2/\sqrt n&\le R,\\
\|W(t)-W(0)\|_{\mathrm{op}}&\le R^2/2,\\
\|A(t)-A(0)\|_{\mathrm{op}}/\sqrt n&\le B(R),\\
\sup_{\|x\|_2=\sqrt d}\|g(t,x)-g(0,x)\|_2/\sqrt n&\le C(R).
\end{aligned}
\tag{10}
\]

In particular the network interpolates at its endpoint. Define

\[
M_*=M+R^2/2,\qquad J_*=1+(1+M_*^2)R^2.
\]

The all-sphere endpoint tail is

\[
\sup_{\|x\|_2=\sqrt d}|f(\infty,x)-f(t,x)|
\le J_*R e^{-\lambda t/m}.
\tag{11}
\]

At every $t\in[0,\infty]$, the prediction has the sphere Lipschitz bound

\[
|f(t,x)-f(t,x')|
\le R M_*\left(\frac{\|A(0)\|_{\mathrm{op}}}{\sqrt n}+B(R)\right)
\frac{\|x-x'\|_2}{\sqrt d}.
\tag{12}
\]

All constants in (8)--(12) are independent of width when $M,\lambda,m$,
and $\|A(0)\|_{\mathrm{op}}/\sqrt n$ are bounded uniformly in width.
One sufficient explicit label threshold is as follows. Set

\[
c_M=\frac{1+M^2}{2}+\frac M8,\qquad
S=\min\left\{1,\sqrt{\frac{\lambda}{4m c_M}}\right\}.
\]

Then $Y\le\lambda S/(4\sqrt m)$ implies (9).

### Proof

For $Y=0$, the flow is stationary, so assume $Y>0$. Introduce the
accumulated residual length

\[
\ell(t)=\frac2{\sqrt m}\int_0^t\|r(s)\|_2\,ds.
\]

Since $|\tanh|,|\tanh'|\le1$, (1) and Cauchy--Schwarz imply, as
inequalities against the nonnegative measure $d\ell$,

\[
d\bigl(\|w\|_2/\sqrt n\bigr)\le d\ell,\qquad
d\|W-W(0)\|_{\mathrm{op}}
\le(\|w\|_2/\sqrt n)d\ell.
\]

Thus $\|w\|_2/\sqrt n\le\ell$ and
$\|W\|_{\mathrm{op}}\le M+\ell^2/2$. Similarly,

\[
d\bigl(\|A-A(0)\|_{\mathrm{op}}/\sqrt n\bigr)
\le\|W\|_{\mathrm{op}}(\|w\|_2/\sqrt n)d\ell,
\]

whose integral is at most $B(\ell)$. For every sphere input, the
first-layer activation changes by at most $B(\ell)$ in RMS. Writing

\[
z(t,x)-z(0,x)
=(W(t)-W(0))h(t,x)+W(0)(h(t,x)-h(0,x))
\]

and using the 1-Lipschitz property of tanh gives the last estimate in (10)
with $R$ replaced by $\ell$.

The $n\times m$ matrix with columns $g_a/\sqrt n$ has operator norm
at most $\sqrt m$. Its difference from the initial matrix has operator
norm at most $\sqrt m C(\ell)$. Factoring a difference of Grams shows
that the current readout Gram differs from $K_0$ in operator norm by at
most $2mC(\ell)$. On any interval with $\ell\le2R$, condition (9)
therefore gives $K(t)\succeq(\lambda/2)I_m$. Equation (3) on training
inputs yields

\[
\frac{d}{dt}\|r\|_2^2=-\frac4m r^TK(t)r
\le-\frac{2\lambda}{m}\|r\|_2^2.
\]

Integration gives $\|r(t)\|_2\le Ye^{-\lambda t/m}$, hence
$\ell(t)\le R$. Because $R<2R$, a first hitting time of $2R$
cannot occur. The parameter bounds exclude escape on finite physical-time
intervals, so the finite-dimensional smooth ODE extends globally. Integrable
bounds on each parameter derivative give finite parameter limits, proving
(10) and endpoint interpolation.

For any test point, $\|b_x\|_2/\sqrt n\le R$,
$\|c_x\|_2/\sqrt n\le M_*R$, and $|\rho_a(x)|\le1$.
Thus (4) has absolute value at most $J_*$. Integrating (3) from $t$
to infinity proves (11). Finally,

\[
|f(t,x)-f(t,x')|
\le\frac{\|w(t)\|_2}{\sqrt n}\|W(t)\|_{\mathrm{op}}
\frac{\|A(t)\|_{\mathrm{op}}}{\sqrt n}
\frac{\|x-x'\|_2}{\sqrt d},
\]

which proves (12), including its limit at infinity. For the displayed
label threshold, $2R\le S\le1$, so
$2mC(2R)\le2m c_M S^2\le\lambda/2$. This completes the proof.

### A useful consequence for promoting a convergence theorem

Suppose a sequence satisfying common constants in (7), (9), and (12)
converges, uniformly on compact time intervals, at every point of each
finite sphere net. Then it converges uniformly on the whole sphere and on
$[0,\infty]$: choose the common tail cutoff using (11), choose a sphere
net using (12), and use finite-net compact-time convergence for the remaining
part. If convergence is instead known at every finite panel drawn from
a dense time set, (3) gives the uniform time Lipschitz constant
$2J_*Y/\sqrt m$, allowing a finite time net. A single fixed time panel
does not suffice. This is a qualitative extension mechanism; no quantitative
$n^{-1/2}$ rate is created by it.

## 3. Explicit initialization event

For the prescribed independent Gaussian initialization, let

\[
q_1=\mathbb E\tanh^2(Z),\qquad
q_2=\mathbb E\tanh^2(\sqrt{q_1}Z),\qquad Z\sim\mathcal N(0,1).
\]

Both constants are strictly positive. Set

\[
\epsilon=\frac{q_2\sqrt{q_1}}{8m^{3/2}},\qquad
\eta=\frac{q_2}{4m}.
\]

With probability at least $1-p_n$, the three simultaneous bounds

\[
K_0\succeq(q_2/2)I_m,\qquad
\|W(0)\|_{\mathrm{op}}\le8,\qquad
\|A(0)\|_{\mathrm{op}}/\sqrt n\le8\sqrt{1+d/n}
\tag{13}
\]

hold, where the completely explicit union bound is

\[
\begin{aligned}
p_n={}&2m^2 e^{-n\epsilon^2/2}
+2m^2 e^{-n\eta^2/2}\\
&+2e^{-(8-2\log9)n}
+2e^{-(8-\log9)(n+d)}.
\end{aligned}
\tag{14}
\]

The bound is useful once its right side is below one; $m,d$ are fixed in
the width limit. In particular (13), (9) provide a fully specified
initialization event and a fixed positive label threshold, independent of
$n\ge d$, for the all-time theorem.

### Proof

Orthogonality makes the $u_{ja}(0)$ independent standard Gaussians. Let
$H$ be the $n\times m$ matrix with columns $h_a(0)$, and put
$C_0=H^TH/n$. Its summands lie in $[-1,1]$, have mean
$q_1\delta_{ab}$, and are independent across rows. The elementary
bounded-sum tail inequality
$\mathbb P(|n^{-1}\sum_i(X_i-\mathbb EX_i)|>s)
\le2e^{-ns^2/2}$ for $X_i\in[-1,1]$ gives, by a union bound,

\[
\max_{a,b}|(C_0)_{ab}-q_1\delta_{ab}|\le\epsilon
\]

except on an event of probability $2m^2e^{-n\epsilon^2/2}$. This
bounded-sum inequality follows by applying the exponential Markov inequality
to the centered variables, bounding their moment generating functions by
$e^{t^2/2}$, and optimizing at $t=s$; the moment generating function
bound follows from convexity on the interval of length two.

Conditioned on $H$, the rows of $WH$ are independent centered Gaussian
vectors with covariance $C_0$. Couple such a row to a vector with
covariance $q_1I_m$ using a common standard Gaussian vector. Since tanh
is 1-Lipschitz and both activation vectors have norm at most $\sqrt m$,
their second-moment matrices differ in operator norm by at most

\[
2\sqrt m\,\|C_0^{1/2}-\sqrt{q_1}I_m\|_F
\le\frac{2\sqrt m}{\sqrt{q_1}}\|C_0-q_1I_m\|_F
\le\frac{2m^{3/2}\epsilon}{\sqrt{q_1}}=q_2/4.
\]

The middle inequality follows on each eigenvalue from
$|\sqrt s-\sqrt{q_1}|=|s-q_1|/(\sqrt s+\sqrt{q_1})$.
The comparison second-moment matrix is $q_2I_m$. A second conditional
bounded-sum inequality, now for $g_{ia}g_{ib}$, gives entrywise error at
most $\eta$ and hence operator error at most $m\eta=q_2/4$,
with failure probability at most $2m^2e^{-n\eta^2/2}$. This proves the
first bound of (13).

For completeness, a Euclidean unit sphere in dimension $k$ admits a
$1/4$-net with at most $9^k$ points: take a maximal separated set and
compare volumes of its disjoint radius-$1/8$ balls inside the radius-$9/8$
ball. For a rectangular matrix, approximating both unit vectors in a
maximizing bilinear pairing by net points loses at most half its operator
norm. Each net pairing of $W$ is $\mathcal N(0,1/n)$, so the Gaussian
tail bound gives
$\mathbb P(\|W\|_{\mathrm{op}}>8)
\le2\cdot9^{2n}e^{-8n}$.
The same argument for $A/\sqrt n$, with net sizes $9^n,9^d$, yields
$2\cdot9^{n+d}e^{-8(n+d)}$ at threshold
$8\sqrt{1+d/n}$. Gaussian tails here follow directly by applying the
exponential Markov inequality to the Gaussian moment generating function.
Combining the four failure events proves (14).

## 4. Complete uniform cubic comparison with frozen initial features

Under the deterministic theorem's assumptions, let $v(0)=0$ solve the
actual frozen-initial-feature training problem

\[
\dot v=-\frac2m\sum_a(f^{\mathrm{fr}}_a-y_a)g_a(0),
\qquad f^{\mathrm{fr}}(t,x)=v(t)^Tg(0,x)/n.
\]

This is an auxiliary reference, not an admissible direct compact model: it
uses the realized dense initialization. Its training residual is
$r^{\mathrm{fr}}(t)=-e^{-2K_0t/m}y$. Put

\[
D_*=2mC(R)+(m+M_*^2)R^2.
\]

Then

\[
\sup_{t\in[0,\infty]}\sup_{\|x\|_2=\sqrt d}
|f(t,x)-f^{\mathrm{fr}}(t,x)|
\le R\left(2C(R)+D_*/\lambda\right).
\tag{15}
\]

For $M,\lambda,m$ fixed and labels satisfying the stated threshold, the
right side is at most a fixed constant times $\|y\|_2^3$.

To prove this, the training kernel's readout contribution changes by at
most $2mC(R)$. Its $W$-contribution has trace at most $mR^2$ and is
positive semidefinite, while its $A$-contribution is diagonal and bounded
by $M_*^2R^2 I_m$. Therefore
$\|K(t)-K_0\|_{\mathrm{op}}\le D_*$. The difference
$e=r-r^{\mathrm{fr}}$ satisfies

\[
\dot e=-\frac2m K_0e-\frac2m(K(t)-K_0)r,\qquad e(0)=0.
\]

Variation of constants and nonnegative integration give

\[
\int_0^\infty\|e(t)\|_2dt
\le\frac{D_*}{\lambda}\int_0^\infty\|r(t)\|_2dt
\le\frac{mD_*Y}{\lambda^2}.
\]

Subtracting the two readout equations and integrating yields

\[
\|w(t)-v(t)\|_2/\sqrt n
\le\frac2{\sqrt m}\int_0^t
\bigl(C(R)\|r(s)\|_2+\|e(s)\|_2\bigr)ds
\le R\left(C(R)+D_*/\lambda\right).
\]

Write $f-f^{\mathrm{fr}}=(w-v)^Tg(0,x)/n+
w^T(g(t,x)-g(0,x))/n$. The parameter and feature bounds prove (15),
including its endpoint by continuity.

The distinction in label scaling is essential. If
$\|y_n\|_2=O(n^{-1/6})$, this nonlinear-to-frozen discrepancy is
$O(n^{-1/2})$. For any fixed nonzero label vector, (15) provides a
fixed cubic error bound, not the requested vanishing error. No population
kernel approximation or all-sphere random-kernel concentration theorem
is asserted by (15).

## 5. A proved nonlinear coefficient and a computable scalar candidate

The one-sample case already shows why zero initial readout does not remove
nonlinear feature learning. Set $m=1$, write the sole label as $y$, and
evaluate all of the following vectors at initialization:

\[
h=\tanh(u),\quad z=Wh,\quad g=\tanh(z),\quad
v=g\odot\tanh'(z),\quad D=\operatorname{diag}(\tanh'(u)^2),
\quad q_{1,n}=\|h\|_2^2/n.
\]

Define the nonnegative scalar

\[
Q_n=\frac1n v^T\bigl(q_{1,n}I_n+W D W^T\bigr)v.
\tag{16}
\]

Direct differentiation of (1), with $w(0)=0$, gives

\[
w'(0)=2yg,\quad W''(0)=4y^2 v h^T/n,\quad
u''(0)=4y^2\tanh'(u)\odot W^Tv,
\]

and hence

\[
z''(0)=4y^2(q_{1,n}I_n+WDW^T)v.
\]

For the scalar training kernel $K(t)$, differentiating its three terms
in (4) gives $K'(0)=0$. The readout term contributes $8y^2Q_n$ to
$K''(0)$; the $W$ and $A$ terms together contribute another
$8y^2Q_n$. Consequently,

\[
f'''(0)-(f^{\mathrm{fr}})'''(0)=32y^3Q_n.
\tag{17}
\]

If $q_{1,n}>0$ and $v\ne0$, then $Q_n>0$. These hold almost surely
under the Gaussian initialization. Thus the nonlinear effect already
survives at the third physical-time derivative for every nonzero label;
the sign of the correction is the sign of $y$.

This coefficient has an explicit deterministic population limit that
preserves reuse of the same $W$. Let $U,Z$ be independent standard
Gaussians, and put

\[
\begin{aligned}
V&=\mathbb E\left[\tanh^2(\sqrt{q_1}Z)
                  \tanh'(\sqrt{q_1}Z)^2\right],\\
b&=\mathbb E\left[\sqrt{q_1}Z\,
          \tanh(\sqrt{q_1}Z)\tanh'(\sqrt{q_1}Z)\right],\\
d_0&=\mathbb E\tanh'(U)^2,\qquad
d_2=\mathbb E\left[\tanh^2(U)\tanh'(U)^2\right].
\end{aligned}
\]

Then, in probability,

\[
Q_n\longrightarrow Q=q_1V+d_0V+\frac{b^2}{q_1^2}d_2>0.
\tag{18}
\]

To verify (18), condition on $h$ and on $z=Wh$. The Gaussian row
decomposition is

\[
W_i=\frac{z_i}{\|h\|_2^2}h^T+\zeta_i^T,
\qquad
\zeta_i\sim\mathcal N(0,P/n),\quad
P=I_n-hh^T/\|h\|_2^2,
\]

with independent $\zeta_i$, independent of $z$. If
$b_n=n^{-1}\sum_i z_i v_i$ and $V_n=\|v\|_2^2/n$, then

\[
W^Tv=(b_n/q_{1,n})h+\zeta,
\qquad \zeta\mid(h,z)\sim\mathcal N(0,V_nP).
\tag{19}
\]

Conditional bounded-sum laws give $V_n\to V$, $b_n\to b$, while
ordinary independent-coordinate laws give $q_{1,n}\to q_1$,
$n^{-1}\operatorname{tr}D\to d_0$, and
$n^{-1}h^TDh\to d_2$. The conditional variance of
$n^{-1}\zeta^TD\zeta$ is at most $2V_n^2/n$, and its conditional
mean is
$V_n(\operatorname{tr}D/n-h^TDh/(n^2q_{1,n}))$.
The cross term in $n^{-1}(W^Tv)^TD(W^Tv)$ has conditional variance at
most $4b_n^2V_n/(nq_{1,n})$, which tends to zero in probability.
Substitution into (16) proves (18). These variance identities follow by
expanding products of centered independent Gaussian coordinates; the fourth
moment is three times the squared variance. The term
$b^2d_2/q_1^2$ is specifically the contribution of reusing $W^T$
after $W$; a naive independent transpose substitution omits it.

For one sample there is an exact local feature-time parametrization
$ds/dt=2(y-f)$. In that parametrization the full finite trajectory,
initialized from the same weights, is independent of $y$. Its prediction
has the local expansion

\[
F_n(s)=\frac{\|g\|_2^2}{n}s+\frac23Q_n s^3+O(s^4)
\quad\text{as }s\to0.
\tag{20}
\]

Indeed the feature-time second derivative of $g$ at zero is
$\tanh'(z)\odot(q_{1,n}I+WDW^T)v$; integrating $dw/ds=g(s)$
and multiplying by $g(s)$ gives the cubic coefficient $2Q_n/3$.
Only a local, finite-width remainder is asserted in (20).

This produces a concrete directly initialized autonomous scalar candidate:

\[
\dot s=2\bigl(y-P(s)\bigr),\qquad s(0)=0,
\qquad \widehat f(t,x_1)=P(s(t)),\qquad
P(s)=q_2s+\frac23Q s^3.
\tag{21}
\]

Its coefficients are one-dimensional Gaussian integrals, its dynamic state
is one scalar, and it requires no width-$n$ initialization. It is globally
well posed: $P'(s)=q_2+2Qs^2\ge q_2>0$, so $P(s)=y$ has exactly one
root; the scalar flow stays between zero and this root. Its prediction
converges to $y$, with residual at most
$|y|e^{-2q_2t}$. Its first three physical-time prediction derivatives
equal the limits of those of the dense network:

\[
\widehat f'(0)=2yq_2,\qquad
\widehat f''(0)=-4yq_2^2,\qquad
\widehat f'''(0)=8yq_2^3+32y^3Q.
\]

Thus (21) has a genuine leading feature-learning correction and uses no
independent replacement under matrix reuse. However, derivative matching
does not prove prediction convergence on any positive time interval.
Neither its fixed-label approximation error nor an all-sphere decoder is
established here. It addresses only the one-sample training output, not
the main $m$-sample target.

## 6. What symmetry does and does not establish

The initialization law is invariant under input rotations fixing every
training point. If a deterministic population prediction limit exists, its
test-input dependence must therefore be a function of the $m$ correlations
$\rho_a(x)$. This reduces the input domain to the unit ball in
$\mathbb R^m$ (or the sphere when $m=d$); it does not imply a finite
state description of the evolving function on that domain. Biasless tanh
networks are odd in their input at every time. Their global label-sign
symmetry is also exact: replacing $y$ by $-y$ replaces $w,f$ by
$-w,-f$, while $A,W$ remain the same.

Finite-rank instantaneous updates do not establish finite-rank cumulative
updates. Equation (1) integrates rank-at-most-$m$ matrices along a changing
trajectory; the span of their factors can grow. For $m>1$, defining
$\dot s_a=-2r_a/m$ gives several controls, not automatically a
closed state $s\in\mathbb R^m$. Their feature vector fields generally
do not commute: already at $w=0$, the two orders of readout updates give
different $W$-derivatives proportional to
$(g_a\odot\tanh'(z_b))h_b^T/n$ and
$(g_b\odot\tanh'(z_a))h_a^T/n$. Orthogonality does not cancel these
terms. Their cumulative history cannot be discarded without a separate
closure argument.

The useful proved bridge is now explicit. Any compact model identified with
the true population dynamics on finite time/input panels can use (11),
(12), and their population limits to handle all physical times and the
whole sphere for sufficiently small fixed labels. The unresolved bridge is
the direct, computable, polylogarithmic scalar approximation of the reused
Gaussian population dynamics, with a quantitative error small enough for
the $C_{\mathrm{data},\delta}/\sqrt n$ target. Neither the geometric
reduction, the all-time stability theorem, the frozen-feature cubic bound,
nor the single nonlinear Taylor coefficient supplies that bridge.
