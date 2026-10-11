# Independent audit of the zero-label extension

Checked 2026-10-11 by unconditional_direct.

Verdict: the corrected candidate passes this mathematical audit for every
fixed finite number of active orthogonal inputs, relative to the supplied
orthogonal strong-flow and Gaussian finite-width convergence theorem.
The extension gives a correlated family with sample count exceeding input
rank. The original shortcut for three or more active inputs was invalid;
Section 10 below supplies a separate conditional-moment proof that repairs
that step. The simpler proof in Section 6 already covers one or two active
inputs.

Scientific inputs were the supervisor's self-contained candidate and its
corrections and later strengthening, together with the complete same-study source
GAUSSIAN_POSITIVE_GEOMETRY.md, SHA-256
d220fba99906085e9770aceb33b939b5d0cfa2bb2bc005909f31fe2449afa574.
For the later strengthening the supervisor also supplied the conditional
sensitivity argument in GAUSSIAN_NONORTHOGONAL_EXTENSION.md; that file was
read completely at SHA-256
37a4f9fea1e64c2404c066358a82f2611f733c6496512d6179bef501424f9b11.
The source's orthogonal construction is the supplied dependency; this
audit checks its use and the new extension, not a fresh proof of the
underlying maintained Gaussian-program theorem. No other studies or
external sources were read. Required skills and shared process instructions
had already been read and were applied.

This audit was completed against the supplied mathematical candidate,
before reading the supervisor's separately written result file. It is an
internal check, not promotion or a review of a frozen integration packet.
No experiments, staging, commits, or shared-source edits were performed.
Only this assigned report was written.

## 1. Precise claim checked

Let \(k\ge1\) be fixed. Fix orthonormal unit inputs
\(x_1,\ldots,x_k\in\mathbb R^d\), and finitely many further unit inputs
\(v_1,\ldots,v_q\) orthogonal to their span. Assume the \(v_b\) are
pairwise distinct and no two are antipodal. Put \(m=k+q\). Let

\[
y_a=a_*\sigma_a\quad(1\le a\le k),\qquad
y_{k+b}=0\quad(1\le b\le q),
\qquad a_*>0,\quad \sigma_a\in\{-1,1\}.
\]

Use the exact two-tanh-layer model

\[
U=\tanh(AX),\quad H=\tanh(WU),\quad
f=H^\top w/n,\quad \mathcal L=\|f-y\|_2^2/m,
\]

where \(X=[x_1,\ldots,x_k,v_1,\ldots,v_q]\),
\(A\in\mathbb R^{n\times d}\), \(W\in\mathbb R^{n\times n}\),
and \(w\in\mathbb R^n\). Below
\(\|z\|_n=\|z\|_2/\sqrt n\) and
\(\langle z,z'\rangle_n=z^\top z'/n\).

with \(A_{ij}(0)\sim N(0,1)\), \(W_{ij}(0)\sim N(0,1/n)\),
independent, and \(w(0)=0\). All three layers train with mobilities
\((n,1,n)\).

The corrected conclusion is

\[
\Pr\left\{\lim_{t\to\infty}\mathcal L_n(t)=0\right\}\longrightarrow1.
\tag{1}
\]

On a probability tending to one event, the actual finite-width loss decays
exponentially after a deterministic finite time. All data, labels, and sample
counts are fixed before the width limit. The amplitude \(a_*\) is arbitrary
but fixed. The conclusion is not uniform in that amplitude or in all allowed
input configurations.

Oddness absorbs the active signs by replacing \(x_a\) with
\(\sigma_ax_a\). This preserves active orthonormality and orthogonality to
the zero-label inputs, and gives exactly the same loss and parameter
trajectory with positive active labels. The proof below uses this form.

Taking \(k=2\), \(q\ge3\), and arbitrarily many distinct nonantipodal inputs
in a fixed two-dimensional perpendicular plane gives intrinsic input
dimension at most four and \(m=2+q>4\). In particular, active labels
\((a_*,-a_*)\) are allowed. The correlated samples are part of the actual
training loss and their layer weights are not frozen in the actual flow.

## 2. Reference flow and the correct clock

Couple the actual network to a reference network with exactly the same
initial weights, but train the reference only on the \(k\) active inputs,
using loss normalization \(1/m\), not \(1/k\):

\[
\widehat{\mathcal L}
=\frac1m\sum_{a=1}^k(\widehat f_a-a_*)^2.
\tag{2}
\]

The reference is an auxiliary comparison flow. Its behavior on zero-label
queries is evaluated using its current full network.

The orthogonal source gives the constructed strong scalar-ascent path
for

\[
g=\frac1k\sum_{a=1}^k f_a.
\]

It has deterministic equal active predictions, a finite target feature
time \(s_*\) with \(g(s_*)=a_*\), and positive scalar feature energy.
The physical reference clock for the normalization (2) is

\[
\frac{ds}{dt}=\frac{2k}{m}(a_*-g(s)),
\qquad
\frac2m\int_0^T k(a_*-g(t))\,dt=s(T)\le s_*.
\tag{3}
\]

This factor \(k/m\) is necessary. It amounts to a constant physical-time
rescaling of the source's active-only mean-loss flow. The source's compact
time convergence applies after this rescaling to the active reference
predictions and all first-feature contractions used below.

For \(k=1\), the same scalar construction is the one-coordinate
specialization of the source's transformed Lipschitz system; the scalar
radial argument requires only positive initial feature energy. For \(k=2\),
the complete construction and both relevant feature differences are
explicitly available in Sections 11 and 13 of the supplied source.

## 3. Unused Gaussian roots remain independent of the reference

Write the input space as the orthogonal sum of the active span and its
orthogonal complement. Gaussian rotational invariance makes the corresponding
components of every row of \(A(0)\) independent. Across rows, all these
root pairs are independent.

The reference first-layer velocity belongs to the active span. Its
orthogonal component therefore stays equal to its initial value. The
entire reference trained state relevant to the active inputs, including
\(\widehat W(t)\) and \(\widehat w(t)\), is measurable in the active
Gaussian roots and \(W(0)\). It does not use the unused roots.

Conditional on those trained inputs to the reference, the rows
\[
(A_j(0)v_1,\ldots,A_j(0)v_q)
\]
remain independent centered Gaussian vectors with covariance
\((v_b^\top v_c)_{bc}\). Thus every reference first feature on a zero-label
query is exactly its frozen initial Gaussian feature.

This conditional independence does not assert that \(W(0)\) is independent
of an active trained query. It uses independent first-layer coordinates
which the reference flow never accesses.

## 4. Conditional prediction estimate for a zero-label query

Fix one \(v_b\), a time \(t\), and condition on all active roots and
\(W(0)\). Write its unused standard Gaussian coordinates as
\(G_1,\ldots,G_n\), so its first preactivations are independent \(N(0,1)\).
Its conditional prediction is

\[
F(G)=\frac1n\widehat w^\top
 \tanh\bigl(\widehat W\tanh G\bigr).
\]

The transformation \(G\mapsto-G\) changes the sign of \(F\), so
\(\mathbb E[F\mid\text{active roots},W(0)]=0\). Differentiation gives

\[
\nabla_GF
=\frac1n\operatorname{diag}(\operatorname{sech}^2G)
 \widehat W^\top
 \bigl[\widehat w\odot
 \operatorname{sech}^2(\widehat W\tanh G)\bigr].
\]

On any event where
\(\|\widehat W(t)\|_{\mathrm{op}}\le M\) and
\(\|\widehat w(t)\|_\infty\le S\),

\[
\|\nabla_GF\|_2^2\le\frac{M^2S^2}{n}.
\]

The Gaussian Poincare inequality therefore yields

\[
\mathbb E[\widehat f_{k+b}(t)^2
 \mid\text{active roots},W(0)]
\le\frac{M^2S^2}{n}.
\tag{4}
\]

The hypotheses are satisfied: the finite-dimensional function is smooth,
bounded, and has bounded gradient. To make the invoked inequality explicit,
if \(G\) is a standard Gaussian vector and \(F,\nabla F\in L^2\), it states
\(\operatorname{Var}F(G)\le\mathbb E\|\nabla F(G)\|^2\).
For the present smooth functions it follows directly from the Gaussian
Ornstein--Uhlenbeck averaging operator
\[
P_sF(x)=\mathbb E F(e^{-s}x+\sqrt{1-e^{-2s}}G').
\]
Gaussian integration by parts gives
\[
\operatorname{Var}F(G)
=2\int_0^\infty\mathbb E\|\nabla P_sF(G)\|^2\,ds.
\]
Differentiation under the bounded integrand gives
\(\nabla P_sF=e^{-s}P_s\nabla F\); Jensen's inequality, Gaussian
invariance, and \(2\int_0^\infty e^{-2s}\,ds=1\) prove the asserted bound.

For each fixed physical horizon \(T\), both flows have deterministic
width-independent bounds \(M_T,S_T\) on the event
\(\|W(0)\|_{\mathrm{op}}\le10\). For example loss dissipation gives
\[
\|r(t)\|_2,\ \|\widehat r_{\mathrm{active}}(t)\|_2
\le a_*\sqrt k,\qquad
\|w(t)\|_\infty,\ \|\widehat w(t)\|_\infty
\le2a_*\sqrt{k/m}\,T,
\]
where the displayed readout bound is a permissible loose bound for both
flows. The middle operator norm follows from the loss-energy path bound.
The event on \(W(0)\) has probability tending to one by the supplied
Gaussian initialization theorem.

Writing \(\widehat f_Q=(\widehat f_{k+1},\ldots,\widehat f_m)\),
equation (4), integration, and Cauchy--Schwarz imply conditionally

\[
\mathbb E\int_0^T\|\widehat f_Q(t)\|_2\,dt
\le\frac{T\sqrt q\,M_TS_T}{\sqrt n}.
\tag{5}
\]

Hence this integral tends to zero in probability. Also
\(\widehat f_Q(T)\to0\) in probability at any fixed time. Uniform-in-time
query concentration is not needed for the comparison below.

## 5. Actual versus reference dynamics: no hidden multiplier estimate

Define
\[
\zeta(p)=p/2+\sinh(2p)/4,\qquad
\psi(\xi)=\tanh(\zeta^{-1}(\xi)).
\]
Both \(\psi\) and \(\zeta^{-1}\) are 1-Lipschitz. For active samples use
\(\xi_a=\zeta(Ax_a)\). For zero-label samples retain raw first
preactivations \(p_b=Av_b\). The reference has constant
\(\widehat p_b=A(0)v_b\).

Let
\[
b_a=w\odot(1-h_a^2),\qquad
G_{bc}=v_b^\top v_c.
\]
The exact actual equations are
\[
\dot\xi_a=-\frac2m r_aW^\top b_a
\quad(1\le a\le k),
\tag{6}
\]
\[
\dot p_b=-\frac2m\sum_{c=1}^q
 G_{bc}\,r_{k+c}\,
 (1-u_{k+c}^2)\odot W^\top b_{k+c}.
\tag{7}
\]
Orthogonality to the active span removes every active contribution from
(7) and every inactive contribution from (6). This is the essential
geometric separation. No ratio of tanh derivatives occurs.

Use the comparison distance
\[
D(t)=
\left(\frac1n\sum_{a=1}^k\|\xi_a-\widehat\xi_a\|_2^2\right)^{1/2}
+\left(\frac1n\sum_{b=1}^q\|p_b-\widehat p_b\|_2^2\right)^{1/2}
+\|W-\widehat W\|_F
+\frac{\|w-\widehat w\|_2}{\sqrt n}.
\]
It starts at zero. On \([0,T]\), all forward and upper-backward differences
are bounded by \(C_TD\) in normalized \(L^2\). In detail,
\[
\|u_a-\widehat u_a\|/\sqrt n\le D,
\]
\[
\|h_a-\widehat h_a\|/\sqrt n
\le\|W-\widehat W\|_F+M_T\|u_a-\widehat u_a\|/\sqrt n,
\]
\[
\|b_a-\widehat b_a\|/\sqrt n
\le\|w-\widehat w\|/\sqrt n
 +2S_T\|h_a-\widehat h_a\|/\sqrt n.
\]
The last inequality uses
\(|(1-h^2)-(1-\widehat h^2)|\le2|h-\widehat h|\).
Similarly \(|f_a-\widehat f_a|\le C_TD\).

Subtracting the two active equations (6) is now Lipschitz in this distance:
split the difference of \(r_aW^\top b_a\) into its three factors and
use the normalized backward norm bound \(M_TS_T\).
The active terms in the \(W,w\) equations have the same property by
the rank-one difference identity. Their extra inactive terms have norm
at most \(C_T\|r_Q\|_2\).

Finally (7) has the direct bound
\[
\left(\frac1n\sum_b\|\dot p_b\|_2^2\right)^{1/2}
\le\frac{2M_TS_T}{m}\,
 \||G|\|_{\mathrm{op}}\|r_Q\|_2,
\tag{8}
\]
where \(|G|\) means entrywise absolute value.
This bound uses the backward field only in normalized \(L^2\).
There is no difference of products involving an unbounded backward
multiplier, because the reference inactive velocity is zero.
Since \(\|r_Q\|_2\le C_TD+\|\widehat f_Q\|_2\), integration gives
\[
D(t)\le C_T\int_0^t
 [D(s)+\|\widehat f_Q(s)\|_2]\,ds.
\]
Gronwall's inequality and (5) prove
\[
\sup_{0\le t\le T}D(t)\longrightarrow0
\quad\text{in probability}.
\tag{9}
\]
All constants depend on fixed data, labels, and \(T\), not width.
This directly compares the actual jointly trained flow with the reference;
no population construction for the correlated actual system is assumed.

## 6. First-feature Gram at the reference endpoint

The zero-label Gaussian first-feature covariance is
\[
Q_{Q,bc}=\mathbb E[
 \tanh(g^\top v_b)\tanh(g^\top v_c)],
\]
where \(g\) is standard Gaussian on the span of the \(v_b\).
It is strictly positive definite for the stated distinct, nonantipodal
inputs.

Indeed, a null vector \(c\) would make
\(\sum_b c_b\tanh(g^\top v_b)=0\) almost everywhere. Continuity and
Gaussian full support extend this equality to every \(g\). For every
direction avoiding the input hyperplanes, scale \(g\) to infinity to get
\(\sum_b c_b\operatorname{sgn}(g^\top v_b)=0\). These sign vectors span
\(\mathbb R^q\): crossing the hyperplane \(v_b^\perp\) at a point on no
other input hyperplane changes only sign \(b\). Such a crossing exists
because distinct nonantipodal inputs have distinct hyperplanes. Subtracting
the two sign identities gives \(c_b=0\). The one-dimensional admissible
case has at most one input and is immediate.

For every fixed time, conditional independence and boundedness imply that
the empirical zero-label Gram converges to \(Q_Q\). Each active/passive
cross entry has conditional mean zero and variance at most \(1/n\):
\[
\mathbb E\left[
\left|\frac1n\widehat u_a^\top u_{k+b}(0)\right|^2
\mathrel{\big|}\text{active roots},W(0)\right]\le\frac1n.
\tag{10}
\]

For \(k=1\), positive endpoint \(g=a_*\) implies \(u_1\ne0\), so its
one-by-one Gram is positive.
For \(k=2\), permutation symmetry of the established reference limit gives
common and contrast eigenspaces. The contrast first-feature mode is
nonzero by the source's natural-coordinate noncollapse estimate for
\(\xi_1-\xi_2\). If the common mode vanished, \(u_2=-u_1\), whence
\(h_2=-h_1\) by oddness and \(g=0\), a contradiction.
Thus the active endpoint first-feature Gram is positive definite.

The source gives strong continuity through the finite scalar endpoint
and convergence of all active first-feature contractions at fixed physical
times. Consequently, for sufficiently late fixed \(T\), the reference
full first-feature Gram
\[
\widehat Q_U(T)=\widehat U(T)^\top\widehat U(T)/n
\]
has a deterministic positive lower bound with probability tending to one.
It converges to the block-diagonal matrix consisting of the positive active
Gram at time \(T\) and \(Q_Q\). Equation (9), bounded first features, and
the matrix product difference identity transfer the same conclusion,
with a smaller fixed margin, to the actual \(Q_U(T)\).

The simple argument above is restricted to \(k\le2\). For \(k\ge3\),
\(\sum_a u_a=0\) does not imply \(\sum_a\tanh(Wu_a)=0\).
Thus positive mean prediction alone does not prove the common active
first-feature mode is nonzero. The additional proof in Section 10 is needed
for the arbitrary-\(k\) statement; no other step of the extension changes.

## 7. Snapshot bounds must use the residual clock

A late-time capture argument cannot use only crude bounds
\(\|w(T)\|_\infty=O(T)\), \(\|W(T)\|_{\mathrm{op}}=O(\sqrt T)\).
Those can make the resulting kernel certificate shrink faster than the
reference residual. The supplied correction removes this circularity.

For the actual network define
\[
C_n(T)=\frac2m\int_0^T\|r_n(t)\|_1\,dt.
\]
The exact equations give
\[
\|w_n(T)\|_\infty\le C_n(T),\qquad
\|W_n(T)-W_n(0)\|_F\le\frac12C_n(T)^2.
\tag{11}
\]
To see the second bound, the middle velocity is at most
\((2/m)\sum_a|r_a|\|b_a\|_n\|u_a\|_n
\le C_n'(t)C_n(t)\), and integration gives (11).

For fixed \(T\), (9), (5), and compact-time convergence of the active
reference imply
\[
C_n(T)\longrightarrow
\frac2m\int_0^T k(a_*-g(t))\,dt=s(T)\le s_*.
\tag{12}
\]
Therefore, with probability tending to one, every chosen fixed reference
time has the snapshot bounds
\[
\|w_n(T)\|_\infty\le S:=s_*+1,\qquad
\|W_n(T)\|_{\mathrm{op}}\le M:=10+S^2/2.
\tag{13}
\]
These constants are fixed before making \(T\) late. Endpoint positivity
also gives \(\|w_n(T)\|_n\ge c>0\), for example by choosing \(T\) with
active mean prediction close enough to \(a_*\), since each top feature
has normalized norm at most one.

## 8. Full endpoint kernel and capture

Suppose at the actual snapshot
\[
Q_U\succeq\lambda I_m,\qquad
\|w\|_n\ge c,\qquad \|w\|_\infty\le S,\qquad
\|W\|_{\mathrm{op}}\le M.
\]
Every top preactivation has \(\|z_a\|_n\le M\). At threshold
\(R_*=\sqrt2SM/c\),
\[
\frac1n\sum_{|z_{ia}|>R_*}w_i^2
\le\frac{S^2M^2}{R_*^2}=\frac{c^2}{2}.
\]
It follows that
\[
\|b_a\|_n^2
\ge\frac{c^2}{2}\operatorname{sech}^4R_*=:\beta>0
\quad\text{for every sample }a.
\tag{14}
\]

The middle kernel is the Hadamard product
\[
K_W=Q_B\odot Q_U,\qquad Q_{B,ab}=\langle b_a,b_b\rangle_n.
\]
Since \(Q_B\) and \(Q_U-\lambda I\) are positive semidefinite, their
Hadamard product is positive semidefinite: it is a Gram matrix of tensor
products of any Gram realizations of these matrices. Thus
\[
K_W\succeq\lambda\operatorname{diag}(\|b_a\|_n^2)
\succeq\lambda\beta I_m.
\tag{15}
\]
This verifies the proposed full-sample kernel bound with its normalization.

The readout-plus-middle Jacobian has a dimension-independent local
continuity bound around this snapshot in the physical parameter norm
\[
\|\Delta\theta\|_{\mathrm{par}}^2
=\|\Delta A\|_F^2/n+\|\Delta W\|_F^2+\|\Delta w\|_2^2/n.
\]
For completeness, on a ball of radius at most one,
\(\|\Delta u_a\|_n\le\|\Delta A\|_F/\sqrt n\),
\(\|\Delta h_a\|_n\le
\|\Delta W\|_F+(M+1)\|\Delta A\|_F/\sqrt n\).
Split the upper-backward difference as
\[
\Delta b_a=\Delta w(1-h_a^2)
+w_*[(1-h_a^2)-(1-h_{*,a}^2)].
\]
It is bounded in normalized \(L^2\) by
\(\|\Delta w\|_n+2S\|\Delta h_a\|_n\).
The tensor difference identity then bounds the middle Jacobian difference.
Summing over the fixed \(m\) samples gives a Lipschitz constant depending
only on \(m,S,M\). No bound on the new state's readout maximum or on a
first-layer backward maximum is needed.

Consequently there is a fixed radius \(\rho>0\) on which the full kernel
is bounded below by one quarter of the snapshot gap in (15).
The gradient identity gives a remaining path length at most the initial
residual norm divided by the square root of that lower bound. A sufficiently
small residual at the snapshot therefore prevents a first exit and implies
exponential fitting, exactly as in the deterministic capture argument of
the supplied source.

To select the snapshot without circularity, first fix the positive
limiting endpoint active Gram, the fixed \(Q_Q\), the positive readout
lower bound, and the constants (13). These give fixed positive
\(\lambda,\beta,\rho\) and a fixed residual capture radius. Then choose
one sufficiently late deterministic physical time \(T\), so the reference
active residual is below that radius and its active Gram is sufficiently
near its endpoint. Finally let width tend to infinity. Equations (4)--(15)
put the actual flow in the capture basin with probability tending to one.
All later times are controlled by exact finite-width inequalities. This
proves (1) relative to the stated orthogonal dependency.

## 9. Audit outcome and boundaries

The candidate's decisive new mechanism survives the checks: unused
Gaussian first-layer coordinates provide centered predictions on arbitrary
correlated zero-label queries, and the actual training perturbation is
controlled in an \(L^1\)-in-time forcing estimate. Orthogonality is needed
between the active span and the zero-label span; the geometry within the
zero-label span can be nonorthogonal and rank deficient.

The following qualifications are required in the final theorem:

- Use Section 10 for \(k\ge3\); positive mean prediction alone does not
  prove the common first-feature mode is nonzero.
- Keep the full normalization \(1/m\), hence clock (3).
- Use the residual clock for late snapshot bounds, as in (11)--(13).
- Preserve distinct/nonantipodal zero-label inputs for the stated
  positive-definite first-feature covariance argument.
- Treat the auxiliary inactive features as frozen only in the reference;
  the actual flow trains every layer on every sample.
- State dependence on the established orthogonal construction and feature
  convergence, not merely on an abstract assertion of orthogonal fitting.

The present check does not prove open perturbations of input geometry or
labels. Such extensions may follow from an additional actual-flow comparison
and strict capture margins, but require their own derivation. It also does
not cover arbitrary nonzero label ratios across a broadly correlated
dataset. No adverse actual Gaussian event was found.

## 10. Additional checked lemma: the common active mode for arbitrary \(k\)

This strengthening was supplied after the base audit. It uses only the
orthogonal scalar-ascent reference, not the correlated actual flow.
Its conditional bounds are uniform over the entire first-layer root array;
that uniformity is what makes a rare-root argument legitimate.

Fix a finite feature horizon \(S\), and condition on arbitrary first-layer
roots. Write \(W_0=Q/\sqrt n\), with independent standard Gaussian entries
in \(Q\), and \(V=W-W_0\). The exact scalar equations are

\[
\xi_a'=\frac1kW^\top b_a,\qquad
V'=\frac1{kn}\sum_{a=1}^k b_au_a^\top,\qquad
w'=\frac1k\sum_{a=1}^k h_a.
\tag{16}
\]

They have \(\|w(s)\|_\infty\le s\) and
\(\|V(s)\|_F\le s^2/2\). Hence
\(\|W(s)\|_{\mathrm{op}}\le L+S^2/2\), where
\(L=\|Q/\sqrt n\|_{\mathrm{op}}\).

For a perturbation \(\Delta Q\), let \((\eta,v,E)\) be the resulting
variations of \((\xi,w,V)\), and put
\[
\mathcal R=\|\eta\|_F+\|v\|_2+\sqrt n\|E\|_F,
\quad
F_U=\|(\Delta Q/\sqrt n)U\|_F,
\quad
F_b=\|(\Delta Q^\top/\sqrt n)[b_1,\ldots,b_k]\|_F.
\]
Every variation starts at zero. With \(M=L+S^2/2\), differentiation gives
\[
\|\delta U\|_F\le\|\eta\|_F,\qquad
\|\delta H\|_F\le F_U+M\|\eta\|_F+\sqrt{kn}\|E\|_F,
\]
\[
\|\delta b\|_F\le\sqrt k\|v\|_2+2S\|\delta H\|_F,
\]
\[
\|\delta B\|_F
\le F_b+S\sqrt{kn}\|E\|_F+M\|\delta b\|_F.
\]
The derivative of the middle equation in (16), multiplied by \(\sqrt n\),
is bounded by \(k^{-1/2}(\|\delta b\|_F+S\|\delta U\|_F)\).
The other two equations yield respectively
\(k^{-1}\|\delta B\|_F\) and \(k^{-1/2}\|\delta H\|_F\).
Combining them proves
\[
D^+\mathcal R
\le C_{S,k}(1+L^2)\mathcal R
 +C_{S,k}(1+L)(F_U+F_b).
\tag{17}
\]
The coefficients depend on no conditioned root values.

For arbitrary \(\Delta Q\), \(F_U+F_b\le C_{S,k}\|\Delta Q\|_F\).
For \(\Delta Q=e_i e_j^\top\), the bound improves to
\(C_{S,k}/\sqrt n\), because the directly forced row or column contains
only bounded \(u\) and \(b\). Gronwall and the preceding differential
formulas imply
\[
\|\delta B\|_F+\|\delta b\|_F
\le C e^{CL^2}\|\Delta Q\|_F,\qquad
\left\|\frac{\partial b}{\partial Q_{ij}}\right\|_F
\le\frac{Ce^{CL^2}}{\sqrt n}.
\tag{18}
\]
This reconstructs the needed part of the supplied sensitivity argument;
constant scalar coefficients remove its residual-variation terms.

For completeness, the Gaussian matrix norm has
\[
\Pr\{L>x\}\le2e^{-nx^2/16}\quad(x\ge10).
\]
One obtains this by taking \(1/4\)-nets of cardinality at most \(9^n\)
on both unit spheres, bounding the norm by twice the largest net bilinear
form, and applying the scalar Gaussian tail and a union bound.
Consequently \(\mathbb E_Q e^{CL^2}\) is uniformly bounded for every
fixed \(C\), once \(n\) is sufficiently large.

For a fixed coordinate \(B_{a,j}=(W^\top b_a)_j\), Gaussian integration
by parts gives
\[
\mathbb E_Q B_{a,j}
=\frac1{\sqrt n}\sum_i
 \mathbb E_Q\frac{\partial b_{a,i}}{\partial Q_{ij}}
 +\mathbb E_Q(V^\top b_a)_j.
\tag{19}
\]
The first term is bounded uniformly by (18). For the second, unroll (16):
\[
(V(s)^\top b_a(s))_j
=\frac1k\int_0^s\sum_c
 u_{c,j}(v)\langle b_c(v),b_a(s)\rangle_n\,dv.
\]
Its absolute value is at most \(s^3/2\), using
\(|u_{c,j}|\le1\), \(\|b_c(v)\|_n\le v\), and
\(\|b_a(s)\|_n\le s\). Thus \(|\mathbb E_Q B_{a,j}|\le C_{S,k}\).
The derivative integrability following (18) and the matrix norm tail
justify (19) by smooth cutoff and dominated convergence.

The first inequality of (18) bounds the Euclidean \(Q\)-gradient of
each scalar \(B_{a,j}\) by \(Ce^{CL^2}\). Applying the Gaussian Poincare
inequality proved in Section 4 gives a uniformly bounded conditional
variance. Together with (19),
\[
\sup_{\text{first-layer roots},\,a,j,\,s\le S}
\mathbb E_Q |B_{a,j}(s)|^2\le C_{S,k}
\tag{20}
\]
for all sufficiently large widths.
This argument needs only a second moment, not a conditional exponential
tail estimate.

Integrating the first equation of (16) and using Cauchy--Schwarz proves
\[
\sup_{\text{first-layer roots},\,j}
\mathbb E_Q\|\xi_j(S)-\xi_j(0)\|_{\mathbb R^k}^2
\le C'_{S,k}.
\tag{21}
\]
Choose a fixed \(R>0\) with \(\zeta(R)^2\ge8C'_{S,k}\).
For a first-layer row whose \(k\) initial preactivations are all at least
\(R\), conditional Markov inequality gives probability at least \(1/2\)
that its displacement in (21) is at most \(\zeta(R)/2\).
On this protected event,
\[
u_{j,a}(S)\ge\psi(\zeta(R)/2)>0
\quad\text{for every active sample }a.
\]
The initial orthogonal projections are independent standard Gaussians,
so the root event has probability \(p_R^k>0\), where
\(p_R=\Pr\{G\ge R\}\). Averaging over roots and \(Q\) yields
\[
\mathbb E\left[\frac1n
 \left\|\sum_{a=1}^k u_a(S)\right\|_2^2\right]
\ge\frac{k^2p_R^k}{2}\,
 \psi(\zeta(R)/2)^2>0.
\tag{22}
\]

The observable on the left is bounded by \(k^2\) and converges in
probability to a deterministic population contraction by the already
constructed orthogonal scalar flow. Boundedness therefore also gives
convergence of its expectation. Passing to the limit in (22) proves that
the population common first-feature mode is nonzero at every finite \(S\),
including the deterministic target feature time \(S=s_*\).
No convergence of indicators and no independence of protected-row events
is required.

For \(k\ge2\), the already established natural-coordinate estimate
\[
\|(\xi_a-\xi_b)'(s)\|_2
\le\frac{2SM^2}{k}\|\xi_a-\xi_b\|_2
\]
prevents a zero pair difference at finite \(S\), starting from independent
Gaussian roots. Injectivity of \(\psi\) then gives a nonzero first-feature
contrast. Sample-permutation symmetry makes the common and contrast
subspaces the eigenspaces of the active first-feature Gram. Both
eigenvalues are now strictly positive. For \(k=1\), (22) already suffices.

Thus the active endpoint Gram required in Section 6 is positive definite
for every fixed finite \(k\). Equations (4)--(15) then establish the same
zero-label extension for arbitrary finite \(k\), with unchanged limit
order and parameter dependencies.

## 11. Checks of the subsequent frozen source files

After completing the derivations above, the reviewer read both complete
candidate source files:

- ORTHOGONAL_FEATURE_GAP.md at SHA-256
  bbd82c9651672bd1ea5523c31b17b79f71575cfc8ee08b10aa7b70ebc1ef6f59.
- ZERO_LABEL_EXTENSION_RESULT.md at SHA-256
  bbe7b734cd060dda8c0ddb993cfb478a2bd293f6c972e324f2c5c3efeab3e523.

The first file passes the mathematical check. Its single-row conditional
second-moment bound is uniform over all first-layer roots. Its threshold
\(\zeta(R)-\zeta(1)\ge2S\sqrt{C_S/k}\) and Markov inequality give the
stated protected probability \(3/4\); the common feature is at least
\(\tanh(1)\) on that event. The bounded empirical observable permits passage
from a positive expectation bound to the deterministic population common
mode. The contrast argument and every width normalization agree with
Section 10 of this report.

The second file's mathematical chain agrees with Sections 1--8 of this
report and passes for its stated \(k\in\{1,2\}\) scope. Its alternative
proof of passive-feature covariance positivity by distinct ridge-function
slopes is valid. Its future residual-clock capture estimate has the correct
factors \(2\sqrt m\|r(T)\|_2/\kappa\).

One minor literal wording correction was requested in Section 2 of that
source. The sentence saying that the reference's "entire trained state"
is measurable in \(A(0)P,W(0)\) must refer instead to its evolving
coordinates \(\bar A(t)P,\bar W(t),\bar w(t)\). The full first-layer matrix
also contains the unused roots \(A(0)(I-P)\), so the literal broad wording
is false. The source's actual conditional calculations use
\(A(0)P,W(0)\) correctly, and all proofs above use the corrected restricted
statement. This is a source wording correction, not a mathematical gap in
the proposed mechanism.

The complete corrected base source was then reread at SHA-256
018a21bce9967a55ceb9a7f1c442d6a3e4e60c9c4e64184b4ba8e9ca5bf51b1e.
It explicitly restricts measurability and independence to
\(\bar A(t)P,\bar W(t),\bar w(t)\) and notes that the full matrix retains
the unused roots. The correction resolves the sole source wording
objection. This corrected base source passes the internal check for its
stated \(k\in\{1,2\}\) theorem.

Substituting the separately checked arbitrary-\(k\) first-feature lemma
for the second file's Section 5 argument removes its \(k\le2\) restriction.
No other step of that complete source uses the restriction. The resulting
assembly should be identified by its own final hash.

## 12. Final arbitrary-\(k\) assembly check

The complete assembled ZERO_LABEL_EXTENSION_RESULT.md was read at SHA-256
3e1f7e0668f68da1d247400b9db1d9e75d1cbce9850fe00b97ccb754db555d97.
The referenced ORTHOGONAL_FEATURE_GAP.md remained at its previously
checked SHA-256
bbd82c9651672bd1ea5523c31b17b79f71575cfc8ee08b10aa7b70ebc1ef6f59.

Verdict: PASS for the assembled theorem with every fixed finite \(k\ge1\).
The statement now permits arbitrary fixed \(k\); Section 5 uses the
checked root-conditional common-mode argument, with the existing
pair-difference argument providing all contrast modes. The former
two-sample shortcut is retained only as a valid special-case explanation.
The final scope paragraph correctly restricts active labels to a common
arbitrary magnitude with arbitrary signs and keeps the extra labels zero.
No other proof step depends on \(k\le2\), and the reference-clock
normalization, conditional Gaussian comparisons, endpoint Gram transfer,
late-time parameter bounds, and deterministic capture remain valid.
The example with two active inputs and a perpendicular two-dimensional
family remains a special case, not a restriction on the theorem.

With the supervisor's explicit authorization, the reviewer changed only
the result file's status paragraph to record this internal check and the
earlier second check of the base theorem. The final source SHA-256 is
b985f0d31cf02e4ffd327fce88618b0fd12ced173ae5f9de1ce7fd073a5c9b35.
No mathematical text was altered by the reviewer. This final hash is the
checked assembled theorem. The check retains the dependency boundary
stated at the beginning of this report and is not promotion to the book.
