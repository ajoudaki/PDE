# Both hidden representations move at a fixed nonvanishing scale

2026-10-03. Coordinator derivation for the one-input canonical dense
compression candidate. This is a feature-motion statement, not a test-label
generalization claim. It uses the exact dense activity equations and
elementary initialized Gaussian concentration. No population training
approximation or frozen-feature model is used.

## Statement

Train the canonical two-tanh-layer width-$n$ dense network on
$x_1=\sqrt2 e_1$ and one sufficiently small fixed $y>0$, with zero
initial readout. There are fixed $c,y_*,S>0$ such that, outside an
initialization event of probability $Ce^{-cn}$, both training feature
vectors satisfy

\[
 \frac{\|h(s)-h(0)\|_2}{\sqrt n}\ge cs^2,
 \qquad
 \frac{\|g(s)-g(0)\|_2}{\sqrt n}\ge cs^2,
 \qquad 0\le s\le S.
 \tag{1}
\]

Here $s$ is the exact activity variable, $ds/dt=2(y-f)$; $h$ and
$g$ are first- and second-layer features on the training input. The
small-label fitted endpoint lies in this interval and is at activity at
least $cy$, so both fitted feature displacements are at least $cy^2$.
These lower bounds do not shrink with width at any fixed nonzero label.

## Initialized event

Let
$a_0=A_0e_1$, $h_0=\tanh a_0$, $z_0=W_0h_0$,
$g_0=\tanh z_0$, $b_0=g_0\odot\operatorname{sech}^2z_0$,
and $k_0=W_0^\top b_0$. With probability $1-Ce^{-cn}$ there
are fixed positive $q_*,g_*,p_*,r_*$ and fixed $K$ such that

\[
 \|W_0\|_{\rm op}\le K,\quad
 \|h_0\|_2^2/n\ge q_*,\quad \|g_0\|_2^2/n\ge g_*,
\]

\[
 \frac1n\sum_j z_{0,j}\tanh z_{0,j}\operatorname{sech}^2z_{0,j}
 \ge p_*,\qquad
 \frac1n\sum_j\tanh^2z_{0,j}\operatorname{sech}^4z_{0,j}\ge r_*.
 \tag{2}
\]

For completeness, all three upper-layer summands are bounded functions of
conditionally independent $N(0,Q)$ variables, with
$Q=\|h_0\|_2^2/n\in[q_*,1]$. Their expectations are positive
and continuous in $Q$ on this compact interval, hence uniformly positive.
The elementary exponential moment bound for independent bounded variables
gives (2). The first-layer bound follows in the same way. The operator
event follows from Gaussian tails on finite sphere nets.

Choose a fixed large $R$ and a fixed small $\eta>0$ so that also

\[
 \frac1n\#\{i:|a_{0,i}|>R\}\le\eta,
 \qquad K\sqrt\eta\le p_*/4.
 \tag{3}
\]

A Gaussian tail and bounded-variable concentration give (3) with another
exponentially small failure probability. None of these events uses a
trained trajectory or a carrier tail theorem.

## Uniform activity estimates

The real activity equations and bounded tanh gates give, on a fixed short
interval independent of width,

\[
 \|w(s)\|_\infty\le s,\quad
 \|W(s)-W_0\|_F\le Cs^2,
\]

\[
 \frac{\|a(s)-a_0\|_2+\|h(s)-h_0\|_2
                   +\|z(s)-z_0\|_2+\|g(s)-g_0\|_2}{\sqrt n}
 \le Cs^2.
 \tag{4}
\]

Integrating $w'=g$ then gives
$\|w(s)-s g_0\|_2/\sqrt n\le Cs^3$. Consequently, with
$\delta(s)=w(s)\odot\operatorname{sech}^2 z(s)$,

\[
 \frac{\|\delta(s)-s b_0\|_2}{\sqrt n}\le Cs^3,
 \qquad
 \frac{\|W(s)^\top\delta(s)-s k_0\|_2}{\sqrt n}\le Cs^3.
 \tag{5}
\]

For the first inequality, separate the readout difference from the gate
difference and use $\|g_0\|_\infty\le1$. For the second, use
$\|W(s)-W_0\|_{\rm op}\le Cs^2$ and the response RMS bound
$\|\delta(s)\|_2/\sqrt n\le s$. These are complete remainders
on the fixed interval, not formal second-order expansions.

## First hidden layer

The identity

\[
 h_0^\top k_0/n=z_0^\top b_0/n\ge p_*,
 \qquad \|k_0\|_2/\sqrt n\le K
 \tag{6}
\]

forces a nonvanishing part of $k_0$ onto moderate initialized neurons.
Indeed choose fixed $M\ge4K^2/p_*$ and let
$E=\{i:|a_{0,i}|\le R,\ |k_{0,i}|\le M\}$.
The contribution to $n^{-1}\sum |h_{0,i}k_{0,i}|$ from
$|a_{0,i}|>R$ is at most $K\sqrt\eta\le p_*/4$.
The contribution from $|k_{0,i}|>M$ is at most
$n^{-1}\sum k_{0,i}^2/M\le K^2/M\le p_*/4$.
Thus $n^{-1}\sum_{i\in E}|k_{0,i}|\ge p_*/2$, and
Cauchy--Schwarz implies

\[
 \frac1n\sum_{i\in E}k_{0,i}^2\ge p_*^2/4.
 \tag{7}
\]

The function $\operatorname{sech}^4$ is globally Lipschitz and is
at least $\operatorname{sech}^4R$ initially on $E$. Equations
(4) and (7) give

\[
 \frac1n\sum_i k_{0,i}^2\operatorname{sech}^4a_i(s)
 \ge \operatorname{sech}^4R\,p_*^2/4-CM^2s^2\ge c_1>0
 \tag{8}
\]

after fixing a sufficiently small $S$. The second error uses
$n^{-1}\sum |a_i(s)-a_{0,i}|\le Cs^2$; no coordinatewise
trained carrier estimate is needed.

Since $h'=\operatorname{sech}^4a\odot W^\top\delta$,
(5) and (8) imply

\[
 k_0^\top h'(s)/n\ge c_1s-CKs^3\ge c_1s/2.
\]

Integration and Cauchy--Schwarz with (6) prove the first part of (1).

## Second hidden layer

Write $D_a=\operatorname{diag}(\operatorname{sech}^2a)$ and
$D_z=\operatorname{diag}(\operatorname{sech}^2z)$. The exact chain
rule, including the learned hidden matrix, gives

\[
 g'=T(s)w,\qquad
 T(s)=D_z\left[\frac{\|h\|_2^2}{n}I+WD_a^2W^\top\right]D_z.
 \tag{9}
\]

This real matrix is positive semidefinite and has operator norm at most
a fixed constant on (4). Moreover, for small fixed $S$,

\[
 \frac{g_0^\top T(s)g_0}{n}
 \ge\frac{\|h(s)\|_2^2}{n}
       \frac1n\sum_j g_{0,j}^2\operatorname{sech}^4 z_j(s)
 \ge q_*r_*/4=:c_2>0.
 \tag{10}
\]

The last step uses (2), (4), bounded $g_0$, and Lipschitz continuity
of the gate. In particular its perturbation is bounded by an RMS
displacement, not a maximum preactivation displacement.

Using $w=s g_0+O_{\mathrm{RMS}}(s^3)$ in (9) now gives
$g_0^\top g'(s)/n\ge c_2s-Cs^3\ge c_2s/2$.
Integration proves the second part of (1).

## Fitting and transfer to the compressed representations

The exact positive training slope is bounded above and below by fixed
constants on this interval. Taking $y_*$ small enough therefore puts
the fitted activity $s_*$ in $[cy,S]$. Equations (1) give the two
fitted lower bounds $cy^2$.

The source cubature in `CANONICAL_NEURON_COMPRESSION.md` preserves all
feature-history pairings up to $C\epsilon$, with
$\epsilon=O(n^{-1/2})$. Its weighted autonomous trajectory is within
$C\epsilon$ of the retained reference states at equal activity. Hence
the squared weighted feature displacement in either reduced layer differs
from the corresponding reference squared displacement by at most
$C\epsilon$. Its own fitted activity is also at least $cy$ and
differs from the reference's by $O(\epsilon)$. For any fixed nonzero
$y\le y_*$, sufficiently large $n$ therefore gives a positive
$cy^2$ lower bound on both reduced feature displacements as well.

This last transfer uses the compression theorem and inherits its check
status. Equations (1)--(10) for the canonical reference are independent
of that theorem. The result asserts actual movement of both nonlinear
representations; it does not assert that every such movement improves a
specified test truth, nor that fixed features could not fit the one label.
