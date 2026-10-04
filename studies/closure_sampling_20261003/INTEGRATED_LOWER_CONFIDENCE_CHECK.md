# Internal reconstruction of the fixed-confidence predictor lower bound

2026-10-04. Scoped mathematical check. This is an internal reconstruction,
not an independent promotion review.

**Verdict: PASS for the revised fixed-confidence lower-bound theorem,
its numerical constants, and its qualified width consequence.** The
width consequence is valid for an upper tolerance on
the independent-copy discrepancy; a tolerance relative to a common
deterministic reference uses twice that tolerance in the comparison. The
precise probability requirements and constants for both interpretations
are derived below.

The target input, read completely, is
INTEGRATED_LOWER_CONFIDENCE.md, SHA-256

    f0e6941471bf29c56e02e9a0997326e7526ecc27a495fe2723b3ac2b4b65a5c7

The initial revision with hash
e2c5e0269a3937ccb79ad8c671f5898b1a99ac991c9c85d3b9613ded943e2348
was also read completely. The coordinator revised the necessity paragraph
after this check distinguished the two error criteria; the complete final
revision was then reread and verified.

The explicitly assigned additional inputs are:

- INTEGRATED_DENSE_LOWER_ROUTE.md, sections 1, 3, and 5a read completely,
  plus the section 2 definition around (6) and the section 5 training-event
  tail proof through (25), with supervisor authorization;
  whole-file SHA-256
  8069187d94d4b90acfaa1406b1ccbd6961a24c2fc6d21de8d9a3a651c1e16200.
- INTEGRATED_COMPARISON_CHECK.md, read completely as the inherited
  reconstruction of the nonlinear remainder and training-good event;
  SHA-256
  e5c4281030648c0e25792a09e55227e943b7a2dd5a326978701880c16aacbd21.
- The initialized CLT in INTEGRATED_INITIAL_VARIABILITY.md was fully
  reconstructed in this checker's preceding assignment. Its SHA-256 is
  unchanged:
  97cdb707c082acf1579e3f73fea6d448e6941a0a06e98568fc4383b3f93a5c6d.

Required canonical-notation, neural-network, and rigorous-math skill
instructions were reused. No other scientific input or numerical
experiment was used. Only this report was written.

## Setup and inherited nonlinear estimate

Fix \(m\ge1\), \(d\ge m+1\), and deterministic labels
\(y\in\mathbb R^m\) with \(0<Y=\|y\|_2/\sqrt m\le1/m\). The network is

\[
h^{(1)}(x)=\tanh(Ax/\sqrt d),\qquad
h^{(2)}(x)=\tanh(Wh^{(1)}(x)),\qquad
f(x)=n^{-1}w^\top h^{(2)}(x).
\]

Both hidden layers have width \(n\). Initially the entries of \(A\) are
independent \(N(0,1)\), those of \(W\) are independent \(N(0,1/n)\), and
\(w=0\); the two matrices are independent. Training uses the mean squared
loss, residual \(r_a=f(x_a)-y_a\), and block mobilities \((n,1,n)\).
The inputs are \(x_a=\sqrt d\,e_a\), and the query is
\(x_*=\sqrt d\,e_{m+1}\).

The exact gradient equations in lower-source (3) show that only the first
\(m\) columns of \(A\) change during training. Thus
\(g=A_0e_{m+1}\sim N(0,I_n)\) remains independent of the complete training
path. With \(H_0^{(2)}\in\mathbb R^{n\times m}\) the initial training
feature matrix, define

\[
K_y(g)=\frac1{mn}(H_0^{(2)}y)^\top\tanh(W_0\tanh g),\qquad
R_n(t,g)=f_n(t,x_*)-2tK_y(g).
\tag{A}
\]

This is an exact decomposition of the actual trained prediction. It
does not replace the dynamics by frozen features. Given the training
initialization, the query map, \(K_y\), and \(R_n\) are odd in \(g\).
Their conditional means under the independent Gaussian \(g\) vanish.

The directly checked training-only event (6) is

\[
\mathcal T=\{\|W_0\|_{\rm op}\le10,\
 \|H_0^{(2)}\|_{\rm op}/\sqrt n\le2\}.
\]

It is determined by \(W_0\) and the trained first-layer columns, so is
independent of the unused query column. On it, the
lower source's stopped bounds hold for \(t=m\tau\),
\(0\le\tau\le1464^{-1/2}\), under \(mY\le1\). The three explicitly retained
query-gradient remainder terms in source (31c), after factoring out
\(\sqrt mY/\sqrt n\), are

\[
594\tau^2+5368(mY)^2\tau^3,\qquad
\frac{24(mY)^2\tau^3}{\sqrt m},\qquad
240(mY)^2\tau^3.
\]

Since \(m\ge1\), \(mY\le1\), and \(\tau\le1\), their sum is at most

\[
(594+5368+24+240)\tau^2=6226\tau^2<7000\tau^2.
\]

Consequently

\[
\sup_g\|\nabla_gR_n(m\tau,g)\|_2
\le7000\frac{\sqrt mY}{\sqrt n}\tau^2.
\tag{B}
\]

The conditional Gaussian Poincare inequality states that
\(\operatorname{Var}(U(g))\le\mathbb E\|\nabla_gU(g)\|_2^2\) for a
square-integrable Gaussian Sobolev function. Here the fixed-training
query function is smooth and bounded, its gradient is bounded by (B),
and its mean is zero by oddness. Thus its hypotheses hold, and

\[
\mathbb E_g R_n(m\tau,g)^2
\le7000^2\frac{mY^2}{n}\tau^4
\quad\hbox{on }\mathcal T.
\]

Integrating over the training initialization verifies target (3).
The proof of this Poincare inequality, by Gaussian Hermite expansion and
Sobolev approximation, is included in the assigned lower-source section 3.
The deterministic stopped-motion inputs and their constants are
inherited from the fully read coordinator reconstruction; no unassigned
part of that proof is silently presented here as independently reread.

## Centering and the two-copy event

Use a tilde for the fully independent, identically distributed second
network. Its training-good event is \(\widetilde{\mathcal T}\). Write
\(\mathcal G=\mathcal T\cap\widetilde{\mathcal T}\), and suppress the
common time and query arguments in this paragraph.

Because \(\mathcal T\) is measurable with respect to the training
initialization, conditional oddness implies

\[
\mathbb E[R_n\mathbf1_{\mathcal T}]=0.
\]

The integrability needed here follows from the second-moment estimate
on \(\mathcal T\). Independence of the two complete networks gives

\[
\begin{aligned}
\mathbb E[(R_n-\widetilde R_n)^2\mathbf1_{\mathcal G}]
&=2\Pr(\mathcal T)\mathbb E[R_n^2\mathbf1_{\mathcal T}]
 -2\bigl(\mathbb E[R_n\mathbf1_{\mathcal T}]\bigr)^2\\
&=2\Pr(\mathcal T)\mathbb E[R_n^2\mathbf1_{\mathcal T}]\\
&\le2\cdot7000^2\frac{mY^2}{n}\tau^4.
\end{aligned}
\tag{C}
\]

Thus target (4) is exact at its equality step and valid at its inequality
step. The factor is \(2\), rather than the factor \(4\) available from a
generic squared triangle inequality. No independence between the leading
term and remainder within one network is needed anywhere in the proof.

## The leading initialized Gaussian limit

Let \(Z\sim N(0,1)\), and define

\[
Q=\mathbb E\tanh^2 Z,\qquad
q=\mathbb E\tanh^2(\sqrt QZ),\qquad
a_2=\mathbb E\tanh'(\sqrt QZ).
\]

Both \(Q\) and \(q\) lie strictly between zero and one. Orthogonal inputs
and odd activations make the population first-layer Gram \(QI\) and the
top-layer Gram \(qI\), including the query. Hence the unnormalized
training gap is \(\gamma=q\).

For the initialized top Gram entries
\(K_{n,*a}=n^{-1}h_0^{(2)}(x_*)^\top h_0^{(2)}(x_a)\), the previously
checked fixed-depth CLT gives the query-row covariance

\[
\nu_2 I_m,\qquad \nu_2=q^2+a_2^4Q^2\ge q^2.
\]

Equation (A) is equivalently
\(K_y=m^{-1}\sum_a y_aK_{n,*a}\). Therefore the two independent copies
satisfy

\[
\sqrt n(K_y-\widetilde K_y)
\ \Longrightarrow\
N\!\left(0,\frac{2\nu_2}{m^2}\|y\|_2^2\right)
=N\!\left(0,\frac{2\nu_2Y^2}{m}\right).
\]

Multiplying by \(2m\tau/(\sqrt mY)\) proves target (5):

\[
\frac{\sqrt n}{\sqrt mY}\,2m\tau(K_y-\widetilde K_y)
\ \Longrightarrow\ N(0,8\nu_2\tau^2).
\tag{D}
\]

In particular, there is no lost \(m\) from the mean-loss factor in
\(K_y\). The normalization is legitimate because \(Y>0\).

## Confidence allocation and every displayed constant

Fix \(0<\delta<1\), before taking \(n\to\infty\), and set

\[
\tau=\frac{q\delta^{3/2}}{56000},\qquad
t_\delta=m\tau,\qquad
b_n=\delta q\tau\frac{\sqrt mY}{\sqrt n}.
\tag{E}
\]

These are strictly positive. Since \(q<1\) and \(\delta<1\),
\(\tau<1/56000<1464^{-1/2}\), so the nonlinear estimate applies.

Let \(L_n=2m\tau(K_y-\widetilde K_y)\). In (D), the two boundary points
\(\pm\delta q\tau\) have probability zero under the limiting Gaussian.
Consequently

\[
\Pr\{|L_n|<b_n\}\longrightarrow
\Pr\!\left\{|N(0,1)|<
\frac{\delta q}{\sqrt{8\nu_2}}\right\}.
\]

The standard Gaussian density is at most \(1/\sqrt{2\pi}\), so

\[
\Pr\{|N(0,1)|\le u\}\le\sqrt{2/\pi}\,u
\quad (u\ge0).
\]

Applying this and \(\nu_2\ge q^2\) bounds the limiting probability by

\[
\sqrt{2/\pi}\frac{\delta q}{\sqrt{8\nu_2}}
\le\frac{\delta}{2\sqrt\pi}<\frac\delta2.
\tag{F}
\]

The strict margin in (F) is important: convergence in distribution then
gives a finite width threshold after which
\(\Pr\{|L_n|<b_n\}\le\delta/2\). No convergence rate or uniformity in
\(\delta,m,y\) has been used.

The training-good tail in source (24), checked directly in its assigned
section 5, is

\[
\Pr(\mathcal T^c)\le
2e^{-c_Wn}+4m^2e^{-n/(32m^2)},\qquad
c_W=100/8-2\log9>0.
\tag{F1}
\]

Its factors can be reconstructed explicitly. Two \(1/4\)-nets with at
most \(9^n\) vectors each give
\(\|W_0\|_{\rm op}\le2\max|u^\top W_0v|\). Each bilinear form has variance
\(1/n\), so the threshold \(5\) and the union bound give
\(2\exp[-n(25/2-2\log9)]\). For the feature cap, each lower off-diagonal
Gram entry is an average of independent centered variables in
\([-1,1]\). Hoeffding at tolerance \(1/(4m)\) gives
\(2e^{-n/(32m^2)}\) for each entry. With those lower entries controlled,
Gaussian covariance differentiation and
\(|\tanh'|\le1\) bound the conditional upper off-diagonal moments by
\(1/(4m)\); the diagonal moments are at most one. Their population
operator norm is at most \(5/4\). A second conditional Hoeffding bound
controls all upper empirical entries to within \(1/(4m)\), adding at
most \(1/4\) to that operator norm. The result is at most \(3/2<4\),
which implies the event's feature cap. Bounding each of the two entry
union losses by \(2m^2e^{-n/(32m^2)}\) proves (F1).

In particular, it suffices for each individual failure probability to
be at most \(\delta/16\), which follows from

\[
n\ge \max\!\left\{c_W^{-1}\log(64/\delta),\
32m^2\log(128m^2/\delta)\right\}.
\tag{F2}
\]

Then the union bound gives \(\Pr(\mathcal G^c)\le\delta/8\).
This is unconditional and is not subtracted again from the leading
Gaussian approximation. The additional variance-comparison width
conditions in source (25) are unnecessary for this CLT-based argument;
they would also hold eventually for fixed \(m\). The only unquantified
width threshold here is the one required by the Gaussian approximation.

On the joint good event, Markov's inequality and (C) give

\[
\begin{aligned}
\Pr\{|R_n-\widetilde R_n|\ge b_n/2,\ \mathcal G\}
&\le\frac4{b_n^2}
 \mathbb E[(R_n-\widetilde R_n)^2\mathbf1_{\mathcal G}]\\
&\le\frac{8\cdot7000^2\tau^2}{\delta^2q^2}\\
&=\frac\delta8,
\end{aligned}
\tag{G}
\]

because \(56000=8\cdot7000\). All \(m,Y,n\) factors cancel in this
ratio; no conditioning changes the denominator.

Outside the union of the three failure events in (F), \(\mathcal G^c\),
and (G), the triangle inequality applied to the exact decomposition (A)
gives

\[
|f_n(t_\delta,x_*)-\widetilde f_n(t_\delta,x_*)|
>b_n/2.
\]

Their total probability is at most
\(\delta/2+\delta/8+\delta/8=3\delta/4\). Thus the proof actually gives
success probability at least \(1-3\delta/4\), which implies the stated
\(1-\delta\). Finally,

\[
\frac{b_n}{2}
=\frac{q^2\delta^{5/2}}{112000}
 \frac{\sqrt mY}{\sqrt n},
\qquad
t_\delta=\frac{mq\delta^{3/2}}{56000}.
\]

This checks every constant in target (1).

The query lies on the specified sphere, and \(t_\delta\) is the same
physical time for both runs. The all-time sphere supremum is therefore
at least this pointwise discrepancy. The dense flows exist for every
finite physical time: for the finite-dimensional positive mobility
matrix \(M\), gradient flow obeys

\[
\int_0^T\|\dot\theta(t)\|_2^2\,dt
\le\|M\|_{\rm op}\mathcal L(0).
\]

Cauchy--Schwarz bounds the displacement on every finite interval, which
precludes escape to infinity in finite time for the locally Lipschitz
vector field. This observation supplies the domain for the all-time
supremum without asserting fitting or endpoint convergence.

## Quantifiers and the dense-width consequence

For each fixed \(m,d,y,\delta\) satisfying the hypotheses, the argument
chooses a finite \(n_0\) large enough for both the initialized CLT
approximation and the training-good tail. The remainder estimate itself
already holds at every width on its good event. The theorem then holds
for every \(n\ge n_0\). The proof does not exchange \(n\to\infty\) with
\(\delta\downarrow0\), \(m\to\infty\), or any time limit. Nor does it give
a quantified \(n_0\). The label restriction \(mY\le1\) controls the
nonlinear motion through time proportional to \(m\), and is used before
the asymptotic argument.

Set \(\delta=1/4\), and write

\[
c_0=\frac{q^2}{3584000},\qquad
D_n=\sup_{t\ge0}\sup_{\|x\|_2=\sqrt d}
 |f_n(t,x)-\widetilde f_n(t,x)|.
\]

The denominator is correct because
\((1/4)^{5/2}=1/32\) and \(112000\cdot32=3584000\). The theorem gives

\[
\Pr\!\left\{D_n\ge c_0\frac{\sqrt mY}{\sqrt n}\right\}\ge\frac34
\quad(n\ge n_0).
\tag{H}
\]

If an upper tolerance for the dense-copy discrepancy means
\(\Pr\{D_n\le\varepsilon\}\ge p\) for any fixed \(p>1/4\), then necessarily

\[
n\ge c_0^2\frac{mY^2}{\varepsilon^2},
\qquad n\ge n_0.
\tag{I}
\]

Indeed, violating (I) makes the threshold in (H) strictly larger than
\(\varepsilon\), so these two events are disjoint despite having
probabilities summing to more than one. The usual success level
\(p=3/4\), for example, satisfies this condition.

If instead the intended tolerance is relative to one common
deterministic function \(f_{\rm ref}(t,x)\), suppose a single dense run
satisfies

\[
\Pr\!\left\{\sup_{t,x}|f_n(t,x)-f_{\rm ref}(t,x)|
 \le\varepsilon\right\}\ge p,\qquad p>1/2.
\]

Independence of the two runs gives joint success probability at least
\(p^2>1/4\), and on this joint event \(D_n\le2\varepsilon\). Applying (I)
with tolerance \(2\varepsilon\) yields

\[
n\ge\frac{c_0^2}{4}\frac{mY^2}{\varepsilon^2},
\qquad n\ge n_0.
\tag{J}
\]

Thus an error to a common deterministic reference has the same width
power but a factor \(1/4\) in this particular necessary constant. No
assertion about the value or bias of that reference follows.

For ordinary dense storage in this two-hidden-layer family, the hidden
matrix alone contains \(n^2\) stored trainable coordinates. In the
sufficiently-wide asymptotic regime of (I), this gives

\[
\operatorname{storage}\ge n^2
\ge c_0^4m^2Y^4\varepsilon^{-4}.
\]

The corresponding constant from (J) is \(c_0^4/16\). For each fixed
task with \(mY>0\), this proves the stated necessary
\(\varepsilon^{-4}\) power for conventional dense storage. It is a
statement about this canonical independent dense family and these
probabilistic error criteria. It is not a lower bound on alternative
representations, coordinated compressors, or all possible training
algorithms. The qualification \(n\ge n_0\) remains part of the
consequence; no separate finite-width optimality assertion is proved.

The confidence improvement is therefore a valid use of the initialized
CLT together with a fluctuation-scale estimate on the complete actual
nonlinear remainder. It does not extrapolate an initial slope to a fitted
endpoint, and it does not assume convergence of finite-width variances.
