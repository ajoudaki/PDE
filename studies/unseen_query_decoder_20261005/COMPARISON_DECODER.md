# Training comparisons for an unseen-query decoder

2026-10-05. Scoped theoretical route by `/root/unseen_comparison_decoder`.
Frozen first attempt; no numerical experiments and no promotion claim.

The training-span argument does **not** extend the finite-panel theorem to
unseen inputs. There are two distinct issues. Input spanning determines a
query's first preactivation, but nonlinear features can leave the span of
training features. Even if exact current feature comparisons are supplied,
the trained readout need not lie in the span of the *current* training
features. The identities and counterexamples below prove these statements.
They do not disprove the existence of another compact decoder.

## 1. Inputs, scope, and conventions

Scientific inputs read completely were only the supervisor's self-contained
assignment, `studies/finite_panel_absolute_compression_20261005/RESULT.md`,
and `docs/notation.qmd`. Their SHA-256 hashes are respectively
`38ca06a2e812d8e2b45c6b7350c0437d710433b11a00b89aa66487a9229b028b`
and `78e11eb3dafc5321a8a3923742993c0bad78df53b0e80b6319f16e48f0131023`
for the two files. Linked studies were not opened. The finite-panel result
is an explicitly authorized inherited input, including its fitting and
variability assertions; its underlying dependencies are not independently
reproved here.

The proof and conjecture skills, their research-contract and adversarial-audit
references, and the shared workflow were read. Reading the required
`/home/amir/.codex/skills/explain-with-canonical-notation/SKILL.md` failed with
`Permission denied`; its neural-network reference was consequently unavailable.
The fallback is the supplied mathematical-communication instructions and the
complete maintained notation contract. No claim of applying that unread skill
is made.

Use the dense model and complete activation and label hypotheses of the
authorized result. In canonical notation, let

\[
v=x/\sqrt d,\qquad
z^{(1)}(t,x)=W^{(1)}(t)v,\qquad
z^{(\ell)}(t,x)=W^{(\ell)}(t)h^{(\ell-1)}(t,x),\qquad
h^{(\ell)}=\phi^{(\ell)}(z^{(\ell)}),
\]
\[
w(t)=W^{(L+1)}(t),\qquad
f_n(t,x)=w(t)^T h^{(L)}(t,x)/n,\qquad
r_a(t)=f_n(t,x_a)-y_a.
\]

Here the first matrix has independent standard Gaussian entries, hidden
matrices have independent Gaussian entries of variance $1/n$, and $w(0)=0$.
The loss is $m^{-1}\sum_a r_a^2$, with mobilities

\[
(n,1,\ldots,1,n).
\]

In particular,

\[
\dot w(t)=-\frac2m\sum_{a=1}^m r_a(t)h^{(L)}(t,x_a).
\tag{1}
\]

This sign agrees with the book's residual convention. It is the negative of
the source file's auxiliary residual $c=y-f$. Hidden matrices and nonlinear
features keep evolving throughout this report.

The intended guarantee has one initialization-only compiled state, followed
by arbitrary queries $x\in\sqrt d\,S^{d-1}$ not supplied to compilation,
uniformly over physical $t\in[0,\infty]$. All retained parameters, coefficients,
and query workspace must fit $O(C\log(en)^5)$. A bound tending to zero at the
dense variability scale and the stronger matched-reference

\[
n^{-1+o(1)}
\]

bound are distinct objectives. The results below isolate missing estimates
for either objective; neither is claimed proved. In the nondegenerate case

\[
m\ge2,\qquad Y=\|y\|_2/\sqrt m>0,
\]

the inherited dense lower bound supplies the benchmark

\[
b_n=c\,Y\sqrt\gamma\big/\big(\sqrt n\,\log(en)^{5/2}\big).
\tag{2}
\]

An error $o(b_n)$, on the appropriate intersected high-probability events,
would suffice for a vanishing error-to-actual-variability ratio. Merely proving
an $O(n^{-1/2})$ error would not establish that ratio through (2).

## 2. Exactly what input spanning gives

Write $V=[v_1\ \cdots\ v_m]\in\mathbb R^{d\times m}$, where

\[
v_a=x_a/\sqrt d,\qquad \|v_a\|_2=1.
\]

Spanning means $VV^T$ is invertible. For every unit $v$, define

\[
\alpha(v)=V^T(VV^T)^{-1}v.
\]

Then $V\alpha(v)=v$, so, at every time and every initialization,

\[
z^{(1)}(t,x)=\sum_a\alpha_a(v)z^{(1)}(t,x_a).
\tag{3}
\]

Also $\|\alpha(v)\|_2\le\sigma_{\min}(V)^{-1}$; mere spanning provides no
uniform bound on that coefficient across data sets. Equation (3) does not
give the analogous identity after a nonlinear activation.

Here is an exact obstruction to the particular decoder

\[
D_{\rm lin}(t,x)=\sum_a\alpha_a(v)f_n(t,x_a).
\tag{4}
\]

Take $d=m=2$, $v_1=e_1,v_2=e_2$, arbitrary $L\ge2$, and

\[
\phi^{(\ell)}(z)=\cos z\quad(1\le\ell\le L).
\]

These activations satisfy the strip hypotheses: on every fixed horizontal
strip their first and second derivatives are bounded, and they are real on
the real axis. Set $y=(\varepsilon,0)^T$, with $\varepsilon>0$ small enough
to satisfy the source's displayed label condition.

The source's population covariance on the two training points has the form

\[
Q^{\ell}=\begin{pmatrix}q_\ell&c_\ell\\c_\ell&q_\ell\end{pmatrix},
\quad q_0=1,\quad c_0=0,
\]
\[
q_\ell=e^{-q_{\ell-1}}\cosh(q_{\ell-1}),\qquad
c_\ell=e^{-q_{\ell-1}}\cosh(c_{\ell-1}).
\tag{5}
\]

To verify (5), use

\[
\cos u\cos v=\tfrac12\{\cos(u-v)+\cos(u+v)\}
\]

and $\mathbb E\cos Z=e^{-\operatorname{Var}(Z)/2}$ for a centered Gaussian.
Inductively $q_\ell>c_\ell\ge0$, because $\cosh$ is strictly increasing
on $[0,\infty)$. Thus the training gap is

\[
\gamma=q_L-c_L>0.
\]

For example, $0<\varepsilon\le\gamma\beta^{-30L}/\sqrt2$ satisfies

\[
Y=\varepsilon/\sqrt2\le(\gamma/2)\beta^{-30L}.
\]

At the unseen point $x=-x_1$, equation (3) uses

\[
\alpha=-e_1.
\]

The first activation is even, so every realization of this fully trained
network satisfies

\[
f_n(t,-x_1)=f_n(t,x_1)
\]

at every time. Decoder (4) instead returns $-f_n(t,x_1)$. On the inherited
fitting event, its endpoint error is exactly

\[
|D_{\rm lin}(\infty,-x_1)-f_n(\infty,-x_1)|=2\varepsilon.
\tag{6}
\]

Using compact training outputs whose error tends to zero changes (6) by
at most that training-output error. This is a failure of input-linear
interpolation within the required spanning, nonlinear, arbitrary-depth
class. It is not a failure of nonlinear comparison decoders.

## 3. Exact current-feature comparison formula and its remainder

Let $H(t)\in\mathbb R^{n\times m}$ have columns $h^{(L)}(t,x_a)$, and put

\[
\mathcal G(t)=H(t)^TH(t)/n,\qquad
p(t)=H(t)^Tw(t)/n=y+r(t).
\]

On the inherited fitting event $\mathcal G(t)$ is invertible for all time. For a
query write $h(t,x)=h^{(L)}(t,x)$, and define the training comparisons

\[
k(t,x)=H(t)^Th(t,x)/n.
\]

Define the Euclidean orthogonal projections

\[
P(t)=\frac1nH(t)\mathcal G(t)^{-1}H(t)^T,\qquad Q(t)=I-P(t).
\]

Then the following decomposition is exact:

\[
f_n(t,x)=p(t)^T\mathcal G(t)^{-1}k(t,x)+R(t,x),
\tag{7}
\]
\[
R(t,x)=\frac{(Q(t)w(t))^TQ(t)h(t,x)}n.
\tag{8}
\]

Indeed $w=Pw+Qw$, $h=Ph+Qh$, and the two ranges are orthogonal.
Moreover

\[
Pw=H\mathcal G^{-1}p,
\]

which gives the first term in (7). The remainder vanishes on every training
point because $Qh(t,x_a)=0$. Training-output accuracy alone therefore
provides no estimate for it.

Equation (1) says $Q(t)\dot w(t)=0$, but differentiating the moving projection
gives

\[
\frac{d}{dt}\{Q(t)w(t)\}=-\dot P(t)w(t),\qquad Q(0)w(0)=0.
\tag{9}
\]

Thus the current training span need not contain the accumulated readout.
The exact bound

\[
|R(t,x)|\le
\frac{\|Q(t)h(t,x)\|_2}{\sqrt n}
\int_0^t\|\dot P(s)\|_{\rm op}\,
             \frac{\|w(s)\|_2}{\sqrt n}\,ds
\tag{10}
\]

follows from integrating (9) and applying Cauchy--Schwarz. None of the
factors in (10) carries an automatic negative power of $n$. A small-label
estimate alone cannot be substituted for width-dependent vanishing when
the admissible label vector is fixed as $n\to\infty$.

For completeness, a useful projection derivative estimate can be checked
without differentiating an inverse explicitly. Differentiating $PH=H$
gives $\dot P H=Q\dot H$. Differentiating $P^2=P$ gives

\[
P\dot P P=0,\qquad Q\dot P Q=0.
\]

Since $P$ and $\dot P$ are symmetric, their off-diagonal blocks are
transposes. Hence

\[
\dot P=Q\dot H(H^TH)^{-1}H^T
       +H(H^TH)^{-1}\dot H^TQ,
\]
\[
\|\dot P\|_{\rm op}
\le\frac{2\|\dot H\|_{\rm op}}{\sqrt{n\lambda_{\min}(\mathcal G)}}.
\tag{11}
\]

These are exact finite-network statements, not a frozen-feature replacement.

### A concrete nonzero nonlinear remainder

This illustration proves that setting $R=0$ is not an exact identity. It
does not by itself refute a high-probability width-asymptotic approximation.

At zero readout, all hidden velocities vanish, so $\dot H(0)=0$. Write

\[
H_0=H(0),\qquad H_2=\ddot H(0),\qquad Q_0=Q(0).
\]

Differentiating (1) and $PH=H$, or multiplying their Taylor expansions,
gives

\[
Q(t)w(t)=-\frac{2}{3m}t^3Q_0H_2y+O(t^4).
\tag{12}
\]

Here are the coefficients: $w'(0)=2H_0y/m$, $w''(0)$ lies in
$\operatorname{ran}(H_0)$, $Q_0w'''(0)=2Q_0H_2y/m$,
$\dot P(0)=0$, and $\ddot P(0)H_0=Q_0H_2$. Thus the cubic coefficient
is $Q_0H_2y/(3m)-Q_0H_2y/m$, as claimed.

Take $L=2,d=m=1,n=2,x_1=1$, first activation the identity and second
activation $1+\sin z$. At the particular initialization

\[
W^{(1)}(0)=(1,1)^T,\qquad
W^{(2)}(0)=\operatorname{diag}(0,\pi/2),\qquad w(0)=0,
\]

put $u=(1,0)^T$. The training top feature is $H_0=(1,2)^T$, and the
unseen top feature at $x=-1$ is $u$. With a nonzero sufficiently small
label $y$, direct differentiation of the actual mobility-scaled gradient
flow gives

\[
H_2=4y^2u.
\tag{13}
\]

To verify the scaling in (13), set $a=W^{(1)}(0)$, $B=W^{(2)}(0)$, and
$D=\operatorname{diag}(\cos(Ba))$. Then

\[
w'(0)=2yH_0,\quad
(W^{(1)})''(0)=4y^2B^TDH_0,\quad
(W^{(2)})''(0)=\frac{4y^2}{n}DH_0a^T,
\]
\[
H_2=4y^2D\left[\frac{\|a\|_2^2}{n}I+BB^T\right]DH_0=4y^2u.
\]

Also $\|Q_0u\|_2^2=4/5$. Combining (8), (12), and (13) gives

\[
R(t,-1)=-\frac{16}{15}y^3t^3+O(t^4).
\tag{14}
\]

The activations satisfy the required strip bounds, and the one-point
population gap is positive. The coefficient in (14) is continuous in the
initial weights and nonzero at the displayed choice. Gaussian initialization
has positive density on a neighborhood of that finite-dimensional choice,
so nonzero remainders are compatible with the actual initialization law.
No lower bound on the probability of such neighborhoods as $n\to\infty$
is claimed. In particular, this $m=d=1$ example is not used as a dense
variability lower bound; (2) has a separate $m\ge2$ hypothesis.

## 4. Where nonlinear training-feature comparisons lose information

The obstruction is visible before training. Continue with $d=m=2$,
$v_1=e_1,v_2=e_2$, first activation cosine, and the unseen
$v=(e_1+e_2)/\sqrt2$. A first-layer row has independent standard normal
coordinates $g_1,g_2$. Its training features and unseen feature are

\[
\cos g_1,\qquad\cos g_2,\qquad
\cos((g_1+g_2)/\sqrt2).
\]

The third random variable is not in the $L^2$ span of the first two. If
it were, continuity and the positive Gaussian density would give the
identity

\[
\cos((s+t)/\sqrt2)=a\cos s+b\cos t
\]

for every real $s,t$. At $t=0$, the second derivative at $s=0$
requires $a=1/2$, whereas the fourth derivative requires $a=1/4$, a
contradiction. The finite-dimensional span is closed, so its squared
projection residual is a strictly positive number $\rho^2$.

Explicitly, if

\[
q=(1+e^{-2})/2,\qquad c=e^{-1},\qquad
b=e^{-1}\cosh(1/\sqrt2),
\]

then

\[
\rho^2=q-\frac{2b^2}{q+c}>0.
\tag{15}
\]

For the empirical first-layer training matrix $H^{(1)}$, its column
projection $P^{(1)}$, and the unseen feature $u^{(1)}$, bounded iid
averaging gives

\[
\frac1n\|(I-P^{(1)})u^{(1)}\|_2^2
\ \longrightarrow\ \rho^2
\quad\text{in probability}.
\tag{16}
\]

For precision, each empirical second moment has variance $O(1/n)$, so
Chebyshev's inequality gives convergence of all the finitely many moments.
The limiting training Gram has smallest eigenvalue

\[
q-c=(1-e^{-1})^2/2>0.
\]

The inverse and the residual formula are continuous near that matrix,
which proves (16).

Condition on the entire first layer. Decompose a Gaussian second-layer
matrix row into its projections onto the range of $H^{(1)}$ and its
orthogonal complement. These jointly Gaussian projections have covariance
zero and are independent. Consequently, conditional also on
$W^{(2)}H^{(1)}$,

\[
W^{(2)}u^{(1)}
=W^{(2)}H^{(1)}
 [(H^{(1)})^TH^{(1)}]^{-1}(H^{(1)})^Tu^{(1)}+\xi,
\tag{17}
\]

where the $n$ coordinates of $\xi$ are conditionally independent
centered Gaussians with variance

\[
\frac1n\|(I-P^{(1)})u^{(1)}\|_2^2.
\]

The variance tends to the positive constant in (15). Thus knowledge of the
training preactivations and training feature comparisons does not determine
the exact unseen second-layer preactivation. Equation (17) is a precise
unclosed term, not just a dimension count.

Three qualifications matter. First, a compiler may retain more information
than these particular training actions. Second, an output average may be
far easier to approximate than all its hidden preactivations. Third, a
decoder could integrate the conditional Gaussian innovation at initialization.
Equation (17) therefore does not show an order-one prediction error for all
comparison decoders. Extending a Gaussian conditional calculation through
feature learning would require a new joint-law argument; holding that
initial law fixed would change the model.

## 5. A precise sufficient estimate for a repaired decoder

Suppose a compact runtime returns training predictions \(\widehat p(t)\), a
training Gram \(\widehat{\mathcal G}(t)\), query comparisons \(\widehat k(t,x)\), and a
query remainder approximation \(\widehat R(t,x)\), all from its counted
current state and the newly supplied query. Define

\[
D(t,x)=\widehat p(t)^T\widehat{\mathcal G}(t)^{-1}\widehat k(t,x)
       +\widehat R(t,x).
\tag{18}
\]

For all times and sphere inputs assume

\[
\lambda_{\min}(\mathcal G),\lambda_{\min}(\widehat{\mathcal G})\ge g>0,
\quad \|p\|_2\le P_*,\quad\|\widehat k\|_2\le K_*,
\]
\[
\|p-\widehat p\|_2\le e_p,\quad
\|\mathcal G-\widehat{\mathcal G}\|_{\rm op}\le e_G,\quad
\|k-\widehat k\|_2\le e_k,\quad
|R-\widehat R|\le e_R.
\]

Then, uniformly on that same time/query set,

\[
|f_n-D|\le
\frac{K_*}{g}e_p+rac{P_*}{g}e_k
 +\frac{P_*K_*}{g^2}e_G+e_R.
\tag{19}
\]

To prove it, subtract (18) from (7), split the difference into the prediction,
query-comparison, inverse-Gram, and remainder terms, and use

\[
\mathcal G^{-1}-\widehat{\mathcal G}^{-1}
=\mathcal G^{-1}(\widehat{\mathcal G}-\mathcal G)\widehat{\mathcal G}^{-1}.
\]

For the dense flow, loss decay gives $\|p\|_2\le2\|y\|_2$, so one can take
\(P_*=2\sqrt mY\). Formula (19) makes the missing claim explicit: for the
variability-ratio objective its right side must be $o(b_n)$; for the
stronger matched-reference objective it must be $n^{-1+o(1)}$. Uniform
training-output accuracy supplies only the first error in this formula.

The supplied compact corrected-readout network already has an algebraic
version of (7), using its metric and its own current feature projection.
Thus a full compact forward pass retains a compact analogue of the remainder
automatically. It is unnecessary and potentially harmful to drop that term.
The issue then becomes proving that the compact query comparisons and
remainder match the dense ones uniformly. The finite-panel theorem explicitly
does not assert this at queries omitted from compilation.

The cost of evaluating such a decoder from width

\[
q=O(m\log(en)^{5/2})
\]

is compatible with the required exponent: the inherited runtime costs
\(O((L+1)m^2\log(en)^5)\); its current nonlinear query forward pass and
\(m\) comparisons use $O(Lq+mq+m^2+d)$ further real coordinates, or less
with sequential layer buffers. This is a storage audit, not a proof of the
missing uniform accuracy estimates. Dense feature vectors or dense matrices
cannot be used to evaluate $\widehat k$ or $\widehat R$.

## 6. Cross-time comparison identity and the remaining bridge

Integrating (1) from zero gives a second exact representation:

\[
f_n(t,x)=-\frac2m\int_0^t\sum_{a=1}^m r_a(s)
  \frac{h^{(L)}(s,x_a)^Th^{(L)}(t,x)}n\,ds.
\tag{20}
\]

This includes the moving-span remainder because it compares a query with
training features at every earlier time, not just their current values.
It does not justify retaining a history oracle. The temporal source space
in the inherited construction compresses training curves, so (20) identifies
the natural next query-estimation problem: uniformly evaluate pairings of
the current unseen feature with the retained training temporal sources.

To quantify the required accuracy independently of a representation, assume
\(\lambda_{\min}(\mathcal G(t))\ge g>0\). The dense tangent Gram is the sum of the
readout Gram and positive semidefinite hidden-block Grams, so

\[
\|r(t)\|_2\le e^{-2gt/m}\|y\|_2.
\]

Replacing every normalized feature pairing in (20) by an approximation
with uniform scalar error at most \(\eta\), while keeping the exact residual,
changes the answer by at most

\[
\frac2m\eta\int_0^\infty\|r(s)\|_1ds
\le\frac{mY}{g}\eta.
\tag{21}
\]

This follows from \(\|r\|_1\le\sqrt m\|r\|_2\) and integrating the
exponential. It is an error-propagation estimate only. It does not produce
the required uniformly accurate comparisons or make the integral a finite
autonomous runtime. Using compact residuals also requires controlling their
integrated difference; a uniform-in-time output error alone is not an
integrable bound on an infinite time interval.

The most focused missing estimate is therefore:

> From the same initialization and training-only compilation, construct a
> counted autonomous query evaluator for the needed pairings between
> training temporal source vectors and current unseen nonlinear features,
> uniformly over the sphere and physical time, at the error scale required
> by (19) or (21).

No supplied result bounds the complexity of these query functions by the
absolute exponent five. Input spanning, exact training Gram preservation,
temporal holomorphy at finitely many declared points, and all-time training
fitting do not by themselves provide this estimate.

## 7. Status and adversarial checks

- **Proved exact identities:** input preactivation reconstruction (3),
  current-feature decomposition (7)--(9), the cubic expansion (12), and
  cross-time comparison formula (20).
- **Proved scoped witness failures:** input-linear interpolation has the
  nonvanishing endpoint error (6) in an admissible $m=d=2,L\ge2$ example;
  dropping the current-feature remainder is not an exact identity, as (14)
  shows. These are not general decoder impossibility results.
- **Proved missing feature information:** the Gaussian conditional
  innovation (17) has nonvanishing variance in the displayed example.
  This concerns a specified training-action representation, not every
  possible retained compact state or its final scalar prediction.
- **Conditional sufficient bounds:** (19) and (21) transfer the stated
  query-comparison errors to output error. Their uniform source estimates
  remain unproved.
- **Open:** an admissible $O(C\log(en)^5)$ unseen-query decoder at the dense
  variability scale, and the separate stronger $n^{-1+o(1)}$ result.

The all-time endpoint in (6) uses the inherited fitting theorem, while the
exact identities hold wherever the actual dense flow and the stated inverse
exist; their endpoint versions follow from its convergent parameters and
positive Gram gap. The Taylor illustration is only local in time and is not
promoted to an all-time or width-asymptotic lower bound. No compact source
is assumed to contain an unseen point; no dense query oracle, frozen kernel,
or encoded arbitrary information is introduced. These arguments were
self-audited algebraically, with no independent review yet. Their frozen
status is a completed scoped route with an explicit open uniform-comparison
bridge, not an internally reviewed proof of the requested decoder.
