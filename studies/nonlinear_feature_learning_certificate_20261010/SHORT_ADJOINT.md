# Scalar adjoint replacement for the short-time proof

The proposed reduction is valid with the existing strong probability
quantifier and with unbounded activation values. It removes every propagated
preactivation/feature-acceleration row law, the second forward conditioning
pass, and the matrix-valued second-order kernel coefficient. The constants
are exactly $m^2/8$ in the partial adjoint increment, $m^2/2$ in the
label-projected kernel increment, and $m/3$ in the output gap.

This check uses only `paper/compact.tex`, `paper/compact_fitting.tex`,
`paper/feature_learning_theorem.tex`, `paper/feature_learning_proof.tex`, and
`paper/feature_learning_initialization.tex`. It does not certify portions of
the compression theorem outside these supplied inputs.

## Initialization facts that remain necessary

Use the paper's forward equations, residuals, loss, and physical gradient
flow. Put $k=2/m$, $W_0^{(\ell)}=W^{(\ell)}(0)$, and

\[
 \langle u,v\rangle_n=u^\top v/n,\qquad
 \|u\|_n=\|u\|_2/\sqrt n.
\]

For an individual hidden matrix define

\[
 \langle U,V\rangle_{\mathrm{mob},1}=\langle U,V\rangle_F/n,
 \qquad
 \langle U,V\rangle_{\mathrm{mob},\ell}=\langle U,V\rangle_F
 \quad(\ell\ge2).
\]

The squared tuple norm is the sum of the squared block norms. All
unmarked forward fields in the following definitions are evaluated at zero:

\[
 \begin{aligned}
 S&=\sum_b y_bh_b^{(L)}(0),&P_a^{(L)}&=S,\\
 B_a^{(\ell)}&=\phi_\ell'(z_a^{(\ell)}(0))\odot P_a^{(\ell)},&
 P_a^{(\ell-1)}&=W_0^{(\ell)\top}B_a^{(\ell)}\quad(\ell\ge2),\\
 V_1&=k^2\sum_a y_aB_a^{(1)}v_a^\top,&
 V_\ell&=\frac{k^2}{n}\sum_a y_aB_a^{(\ell)}h_a^{(\ell-1)}(0)^\top
 \quad(\ell\ge2).
 \end{aligned}
\]

These satisfy $V_\ell=\ddot W^{(\ell)}(0)$ and

\[
 E_{\ell,n}:=\|V_\ell\|_{\mathrm{mob},\ell}^2
   =k^4y^\top(Q_n^{(\ell-1)}\circ D_n^{(\ell)})y,
 \qquad
 D_{n,ab}^{(\ell)}=\langle B_a^{(\ell)},B_b^{(\ell)}\rangle_n,
\]

where $Q_n^{(0)}=[v_a^\top v_b]_{a,b}$ and

\[
 Q_{n,ab}^{(j)}=\langle h_a^{(j)}(0),h_b^{(j)}(0)\rangle_n
 \quad(j\ge1).
\]

The shortened initialization lemma needs only the following conclusions:

1. At each layer the initialized forward fields and $P,B$ have a
   deterministic joint empirical quadratic-Wasserstein limit.
2. At layer one this includes the full initial weight row and the row of
   $V_1$, the latter being the displayed linear combination of $B_a^{(1)}$.
3. $D_n^{(\ell)}\to D^{(\ell)}\succ0$, and therefore
   $E_{\ell,n}\to e_\ell>0$, in probability.

The first forward pass and first reverse pass in the supplied initialization
proof establish precisely these facts. No later forward call is needed.
The positivity argument for $D^{(\ell)}$ remains unchanged: at the top use
full Gaussian support, analyticity, and nonconstant activation derivatives;
below it use the independent Gaussian innovation in the first reverse call.
The Schur-product estimate already proved there gives

\[
 e_\ell
 =k^4y^\top(Q^{(\ell-1)}\circ D^{(\ell)})y
 \ge k^4\lambda_{\min}(D^{(\ell)})
       \sum_a y_a^2Q_{aa}^{(\ell-1)}>0.
\]

This also works at the possibly rank-deficient first input Gram, whose
diagonal entries equal one. Positivity of feature-acceleration limits is no
longer a premise or a required conclusion of the initialization lemma.

## A replacement proof of strong early-time activity

Use the real bootstrap already proved in the paper. On an event of
probability tending to one, with deterministic width-independent constants,
the hidden matrix increments in mobility norm and all forward increments
in neuron RMS are $O(t^2)$, $\|w(t)\|_n=O(t)$, the hidden operator
norms and forward RMS norms are bounded, and $f_n(t)=O(t)$. The estimates
hold simultaneously for $0\le t\le T$.

Retain exactly the paper's definition of $o_*(t^q)$: for every

\[
 \varepsilon>0\quad\text{there exists a deterministic }T_\varepsilon>0
 \quad\text{such that}\quad
 \Pr\!\left\{\sup_{0<t\le T_\varepsilon}
       \frac{\|R_n(t)\|}{t^q}>\varepsilon\right\}\longrightarrow0.
\]

Here the norm is the scalar absolute value or the explicitly indicated
array norm. Constants below may depend on the fixed problem.

For any of the finitely many initialized vectors $u=P_a^{(\ell)}$ or

$B_a^{(\ell)}$, quadratic-Wasserstein convergence gives, for every

\[
 \eta>0,\quad\text{some finite }D\text{ with}\quad
 \Pr\{\|u\mathbf1_{|u|>D}\|_n^2>\eta\}\longrightarrow0.
\]

Choose a continuity threshold with limiting tail second moment less than

$\eta/2$. The finite collection of these events can be intersected.
For bounded Lipschitz $g$, coordinate splitting gives

\[
 \|[g(z)-g(z_0)]\odot u\|_n^2
 \le\operatorname{Lip}(g)^2D^2\|z-z_0\|_n^2
       +4\|g\|_\infty^2\|u\mathbf1_{|u|>D}\|_n^2.
 \tag{1}
\]

Choose the tail tolerance, then $D$, then time. With $g=\phi_\ell'$,
the bootstrap makes (1) $o_*(1)$, uniformly also when

$z-z_0=\theta\Delta z(t)$, $0\le\theta\le1$.

The readout equation gives

\[
 \|w(t)/t-kS\|_n\le Ct.
\]

Subtract the backward recursion from $ktB_a^{(\ell)}$. At the top, the
two errors are the bounded gate times $w(t)/t-kS$ and a gate difference
times $kS$. At a lower layer the three errors, after division by time,
are the upper backward error propagated through bounded operators, the
matrix increment applied to $kB_a^{(\ell+1)}$, and the gate difference
applied to $kP_a^{(\ell)}$. Equation (1) controls the last term. Thus

\[
 \delta_a^{(\ell)}(t)=ktB_a^{(\ell)}+o_{*,\|\cdot\|_n}(t).
 \tag{2}
\]

In the weight equations, $r_a=-y_a+O(t)$ and the forward increments
are $O_{\|\cdot\|_n}(t^2)$. The exact outer-product norm identities

\[
 \|uv^\top\|_F/\sqrt n=\|u\|_n\|v\|_2,
 \qquad \|uh^\top\|_F/n=\|u\|_n\|h\|_n
\]

therefore give $\dot W^{(\ell)}(t)=tV_\ell+o_*(t)$ in the block
mobility norm. Integration preserves the uniform remainder quantifier:

\[
 \Delta W^{(\ell)}(t)=\frac{t^2}{2}V_\ell
             +o_{*,\|\cdot\|_{\mathrm{mob},\ell}}(t^2).
 \tag{3}
\]

It remains to test forward increments against the initialized adjoints.
Define the scalar

\[
 J_\ell(t)=\sum_a y_a
       \langle P_a^{(\ell)},\Delta h_a^{(\ell)}(t)\rangle_n,
 \qquad J_0(t)=0.
\]

The exact integral formula for an activation increment and (1) give

\[
 \begin{aligned}
 &\left|\langle P_a^{(\ell)},\Delta h_a^{(\ell)}\rangle_n
       -\langle B_a^{(\ell)},\Delta z_a^{(\ell)}\rangle_n\right|\\
 &\quad\le\|\Delta z_a^{(\ell)}\|_n
     \sup_{0\le\theta\le1}
       \|[\phi_\ell'(z_a^{(\ell)}(0)+\theta\Delta z_a^{(\ell)})
                 -\phi_\ell'(z_a^{(\ell)}(0))]
                   \odot P_a^{(\ell)}\|_n
   =o_*(t^2).
 \end{aligned}
 \tag{4}
\]

For $\ell\ge2$, substitute the exact forward subtraction

\[
 \Delta z_a^{(\ell)}
 =\Delta W^{(\ell)}h_a^{(\ell-1)}(0)
       +W_0^{(\ell)}\Delta h_a^{(\ell-1)}
       +\Delta W^{(\ell)}\Delta h_a^{(\ell-1)}.
\]

The propagated term pairs to $J_{\ell-1}$ by the defining transpose
relation for $P_a^{(\ell-1)}$. The final term has pairing $O(t^4)$
by the bootstrap and bounded initialized $B$-norms. The learned-link
term is exactly

\[
 \sum_a y_a\langle B_a^{(\ell)},
            \Delta W^{(\ell)}h_a^{(\ell-1)}(0)\rangle_n
   =k^{-2}\langle V_\ell,\Delta W^{(\ell)}
                       \rangle_{\mathrm{mob},\ell}.
\]

At layer one the same identity uses $v_a$ in place of the previous
feature, with no propagated or product term. Combining (3) and (4) gives

\[
 J_\ell(t)=J_{\ell-1}(t)+\frac{t^2}{2k^2}E_{\ell,n}+o_*(t^2)
   =\frac{m^2t^2}{8}\sum_{j\le\ell}E_{j,n}+o_*(t^2).
 \tag{5}
\]

The left side satisfies the sample-and-neuron Cauchy inequality

\[
 |J_\ell(t)|\le
 \left(\sum_a y_a^2\|P_a^{(\ell)}\|_n^2\right)^{1/2}
 \left(\sum_a\|\Delta h_a^{(\ell)}(t)\|_n^2\right)^{1/2}.
\]

The first factor is bounded by a deterministic constant on an event of
probability tending to one, because its square converges to a deterministic
finite limit. The coefficient in (5) converges to a strictly positive
constant. Choose one remainder tolerance below half the smallest leading
coefficient and then a common deterministic time. This proves every
layer's asserted $ct^2$ feature motion, simultaneously on that interval
with probability tending to one. No feature-acceleration limit has been used.

For the output gap, retain the exact tangent-kernel formula in the paper,
and write $E_n=\sum_\ell E_{\ell,n}$, $\Delta K(t)=K(t)-K(0)$.
Its readout contribution, paired with $y$, is exactly

\[
 \left\|\sum_a y_ah_a^{(L)}(t)\right\|_n^2-\|S\|_n^2
   =2J_L(t)+\left\|\sum_a y_a\Delta h_a^{(L)}(t)\right\|_n^2
   =\frac{t^2}{k^2}E_n+o_*(t^2).
\]

Its hidden contribution follows from (2) and the initialized feature
Grams:

\[
 k^2t^2\sum_\ell y^\top(Q_n^{(\ell-1)}\circ D_n^{(\ell)})y
      +o_*(t^2)
   =\frac{t^2}{k^2}E_n+o_*(t^2).
\]

Consequently

\[
 y^\top\Delta K(t)y=\frac{2t^2}{k^2}E_n+o_*(t^2)
                  =\frac{m^2t^2}{2}E_n+o_*(t^2).
 \tag{6}
\]

The real bootstrap alone also gives the full matrix bound
$\|\Delta K(t)\|_{\mathrm{op}}\le Ct^2$: subtract the readout
feature Grams using bounded feature norms and $O(t^2)$ feature increments;
each hidden term has two $O(t)$ backward factors. The number of samples
is fixed. A matrix-valued coefficient $K_2$ is unnecessary.

For $e(t)=f_n(t)-f_{\mathrm{NTK},n}(t)$, exact Duhamel integration gives

\[
 e(t)=k\int_0^t e^{-kK(0)(t-s)}\Delta K(s)[y-f_n(s)]\,ds.
\]

Because $K(0)\succeq0$ has deterministically bounded norm with
probability tending to one,
$\|e^{-kK(0)(t-s)}-I\|\le C(t-s)$. Together with
$\|\Delta K(s)\|\le Cs^2$ and $f_n(s)=O(s)$, this gives

\[
 y^\top e(t)=k\int_0^t y^\top\Delta K(s)y\,ds+O(t^4)
   =\frac{2}{3k}E_nt^3+o_*(t^3)
   =\frac m3E_nt^3+o_*(t^3).
 \tag{7}
\]

In particular, scalar control in (6), together with an $O(t^2)$ bound
on the full kernel increment, proves the paper's exact claimed cubic
identity and its width-independent positive-time conclusion.

## The nonlinear first-layer increment remains a separate argument

Let $V=\operatorname{span}\{x_a\}$, let $\Pi_V$ project onto this
space, and let $\Pi_{\mathrm{aff}}$ be orthogonal projection onto affine
functions in $L^2(S(V),\sigma_V)$. The nonparallel-input assumption gives
$\dim V\ge2$. Write

\[
 g_i=\Pi_V W_{0,i:}^{(1)\top},\qquad q_i=V_{1,i:}^{\top}\in V.
\]

The retained first-layer row law gives a deterministic joint empirical
quadratic-Wasserstein limit $(g,q)$, with $g$ nondegenerate Gaussian
on $V$ and $\mathbb E\|q\|^2=e_1>0$.
For nonzero $g,q\in V$,
$v\mapsto\phi_1'(g^\top v)(q^\top v)$ is not affine on $S(V)$:
an affine equality on the equator $q^\perp$ and its antipodes first
forces zero constant part and linear coefficient parallel to $q$; off
the equator it then forces $\phi_1'(g^\top v)$ to be constant.
Continuity and analyticity would make $\phi_1$ affine, a contradiction.
Hence the continuous, at-most-quadratic-growth function

\[
 (g,q)\longmapsto
 \|(I-\Pi_{\mathrm{aff}})
       [\phi_1'(g^\top v)(q^\top v)]\|_{L^2(\sigma_V)}^2
 \le\|\phi_1'\|_\infty^2\|q\|^2
\]

has a strictly positive deterministic limiting empirical average.

Equation (3) and the Lipschitz activation first replace the actual
first-layer weight increment by $t^2q_i/2$, with an $o_*(t^2)$ error
in the product of neuron RMS and $L^2(\sigma_V)$. Expand only this fixed
direction. On $\|q_i\|\le D$, the Taylor remainder divided by $t^2$
is at most $\|\phi_1''\|_\infty t^2D^2/8$. On the complement it is
at most $\|\phi_1'\|_\infty\|q_i\|$. The initialized row-law tails,
followed by a deterministic time choice, again give $o_*(t^2)$.
Applying the contractive projection $I-\Pi_{\mathrm{aff}}$ proves the
claimed positive $ct^4$ squared increment. This requires only the joint
law of the first weight and acceleration rows, not a propagated forward
acceleration law.

## Scope of the simplification

The proof may delete the initialization notation $R,A$, the second
forward conditional formula, the forward-acceleration induction, the
partial-acceleration adjoint identity, and the claimed convergence or
positivity of all feature-acceleration norms. Replace those conclusions by
the backward initialization facts above and (5). The first forward
conditioning pass, reverse conditioning, pre-gated $P$-tails, and first
weight/acceleration joint row law must remain.

No bounded activation-value assumption is needed. Linear activation growth
provides initialized second moments and bootstrap feature bounds; every
nonlinear remainder uses bounded first and second derivatives and initial
second-moment tails. No fourth-moment bound for moving increments and no
Fréchet differentiability of an activation map on $L^2$ is assumed.

For the strong probability convention, use deterministic bounds holding
with probability tending to one, as supplied by the bootstrap and the
deterministic initialized norm limits. Merely writing a tight
$O_{\mathbb P}(1)$ coefficient would leave a quantifier gap unless this
stronger bound is restored. The deterministic tail and time choices above
provide the required stronger conclusion.
