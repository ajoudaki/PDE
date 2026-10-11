# Arbitrary-amplitude fitting with many dependent inputs

Status: internally checked theorem, 2026-10-11; see
ZERO_LABEL_EXTENSION_CHECK.md (including arbitrary-\(k\) assembly) and
ZERO_LABEL_SECOND_CHECK.md (base \(k\le2\)).
This is a theorem about the canonical finite-width dynamics,
not a conditional population endpoint statement. It is not a promotion to
the maintained book and does not establish the compression theorems.

## 1. Headline and exact scope

There may be arbitrarily many distinct training inputs in a fixed
four-dimensional input span, with two arbitrarily large, oppositely signed
labels. The remaining labels are zero in the base theorem. The input
geometry inside the complementary two-dimensional plane is arbitrary,
apart from signed duplicates. At sufficiently large width, the actual
Gaussian-initialized, fully trained two-hidden-layer tanh network fits all
these samples with probability tending to one.

An open-neighborhood extension is recorded separately in
ZERO_LABEL_OPEN_EXTENSION.md. The base proof below does not assume that
extension.

Use unit inputs \(x_a\in\mathbb R^d\); these are the original sphere inputs
divided by \(\sqrt d\). Put \(X=[x_1,\ldots,x_m]\). The network, loss and
mobilities are
\[
 U=\tanh(AX),\qquad H=\tanh(WU),\qquad f=H^\top w/n,\qquad
 r=f-y,\qquad \mathcal L=\|r\|_2^2/m,
\]
\[
 \dot A=-n\nabla_A\mathcal L,\qquad
 \dot W=-\nabla_W\mathcal L,\qquad
 \dot w=-n\nabla_w\mathcal L.
\]
Initialization is exactly independent
\[
 A_{ij}(0)\sim N(0,1),\qquad W_{ij}(0)\sim N(0,1/n),
 \qquad w(0)=0.
\]
There are no biases, frozen trainable blocks, altered learning rates, or
non-Gaussian initialization choices.

Choose any fixed integer \(k\ge1\), \(m>k\), and \(a>0\). Assume:

1. \(x_1,\ldots,x_k\) are orthonormal.
2. Every \(x_b\), \(b>k\), lies in their orthogonal complement.
3. The inputs \(x_b\), \(b>k\), are unit vectors and satisfy
   \(x_b\ne\pm x_c\) for \(b\ne c\).
4. \(y_i=a\sigma_i\), \(i\le k\), for arbitrary
   \(\sigma_i\in\{-1,1\}\), and \(y_b=0\), \(b>k\).

All quantities in these assumptions are fixed independently of width and
of the initialization. There is no upper bound on \(a\), and no condition
\(m\le d\). For example, take \(k=2\), \(x_1=e_1,x_2=e_2\), and any number of
distinct, nonantipodal points in the \(e_3,e_4\) plane, with
\(y_1=a,y_2=-a\).

**Theorem.** There are deterministic \(T<\infty\) and \(c>0\), depending on
the fixed dataset and \(a\), such that
\[
 \Pr\left\{\mathcal L_n(t)\le
          \mathcal L_n(T)e^{-c(t-T)}
          \text{ for every }t\ge T,\quad
          \lim_{t\to\infty}\mathcal L_n(t)=0\right\}\longrightarrow1.
 \tag{1}
\]
Equivalently, for each \(\delta>0\), a sufficiently large deterministic
width threshold makes the displayed event have probability at least
\(1-\delta\). No quantitative width threshold or useful uniform rate in
the dataset is claimed. In particular, infinity is taken along the
actual finite-width gradient flow before sending width to infinity.

The proof uses the completed orthogonal canonical-Gaussian theorem and
its compact-time limit in GAUSSIAN_POSITIVE_GEOMETRY.md, Sections 11 and
13. For \(k=1\), the same proof is its scalar specialization: the
natural-coordinate construction, readout–residual argument and capture
proof do not require \(k\ge2\). The additional argument below is what
permits arbitrarily many dependent inputs. The additional fully proved
lemma ORTHOGONAL_FEATURE_GAP.md supplies its first-feature endpoint gap
for arbitrary \(k\).

## 2. Exact equations and a disposable reference

Write \(u_a,h_a\) for the sample columns and
\[
 b_a=w\odot(1-h_a^2),\qquad B_a=W^\top b_a,\qquad
 \|v\|_{2,n}=\|v\|_2/\sqrt n.
\]
Then
\[
 \dot A=-\frac2m\sum_a r_a
       [(1-u_a^2)\odot B_a]x_a^\top,\quad
 \dot W=-\frac2{mn}\sum_a r_a b_a u_a^\top,\quad
 \dot w=-\frac2m\sum_a r_a h_a.                         \tag{2}
\]
All finite trajectories exist on every finite time interval by loss
dissipation and the standard finite-dimensional continuation argument.

Absorb each active sign into its input. Oddness of the whole bias-free
network gives the exact identity
\((f(x_i)-a\sigma_i)^2=(f(\sigma_i x_i)-a)^2\), as functions of
all parameters. This leaves orthogonality unchanged. It is enough to
consider \(y_i=a\) for \(i\le k\).

Let bars denote the network with the **same sampled initial arrays**,
trained on the active samples only, using the loss
\[
 \overline{\mathcal L}=\frac1m\sum_{i\le k}(\bar f_i-a)^2.
 \tag{3}
\]
Thus its time is the active \(k\)-sample theorem's time multiplied by
\(m/k\). This reference is a proof device; the network in (1) trains on
all \(m\) samples by (2).

Let \(P\) be the orthogonal projection onto the active input span.
The reference gradient \(\dot{\bar A}\) has its rows in that span, so
\[
 \bar A(t)(I-P)=A(0)(I-P),\qquad
 \bar u_b(t)=\tanh(A(0)x_b)\quad(b>k).                  \tag{4}
\]
Moreover, its evolving active coordinates \(\bar A(t)P,\bar W(t),\bar w(t)\)
are measurable with respect to \(A(0)P,W(0)\). Gaussian orthogonal
projections make the unused roots \(A(0)(I-P)\) independent of these
quantities; the full matrix \(\bar A\) of course still contains those roots.

## 3. The reference predicts zero on the extra samples

Condition on \(A(0)P,W(0)\). At a fixed time and extra input, put
\(g=A(0)x_b\). Its coordinates are iid standard Gaussians, independent
of \(\bar W,\bar w\), and
\[
 \bar f_b=\frac1n\bar w^\top
            \tanh\bigl(\bar W\tanh g\bigr).
 \tag{5}
\]
This is an odd function of \(g\), so its conditional mean is zero.
Its Euclidean Lipschitz constant is at most
\[
 \frac{\|\bar W\|_{\rm op}\|\bar w\|_2}{n}
 \le \frac{\|\bar W\|_{\rm op}\|\bar w\|_\infty}{\sqrt n}.
 \tag{6}
\]
The Gaussian Poincare inequality therefore gives
\[
 \mathbb E\!\left[\bar f_b(t)^2\mid A(0)P,W(0)\right]
 \le \frac{\|\bar W(t)\|_{\rm op}^2\|\bar w(t)\|_\infty^2}{n}.
 \tag{7}
\]
This inequality can also be obtained by integrating the Gaussian
concentration bound proved in Section 3.3 of
GAUSSIAN_NONORTHOGONAL_EXTENSION.md. Poincare with constant one follows
directly by integrating the squared-gradient contraction of the
Ornstein–Uhlenbeck semigroup; it applies to (5), a smooth globally
Lipschitz function of finitely many standard Gaussians.

On \(\{\|W(0)\|_{\rm op}\le10\}\), loss dissipation gives deterministic
bounds on \(\|\bar w\|_\infty,\|\bar W\|_{\rm op}\) on every fixed
\([0,T]\). Consequently, conditional Cauchy–Schwarz and integration give
\[
 \int_0^T\|(\bar f_b(t))_{b>k}\|_2\,dt
       =O_{\mathbb P}(n^{-1/2}),\qquad
 \|(\bar f_b(T))_{b>k}\|_2=O_{\mathbb P}(n^{-1/2}).
 \tag{8}
\]
The constants here may depend on \(T,m,a\); the matrix-norm event has
probability tending to one. No independence between different extra
queries is required. In particular no time-grid concentration theorem
for the full correlated training problem has been assumed.

## 4. Direct finite-width comparison on a fixed interval

Use the established natural coordinate
\[
 \zeta(z)=z/2+\sinh(2z)/4,\qquad
 \psi(\xi)=\tanh(\zeta^{-1}(\xi)),\qquad |\psi'|\le1.
\]
For active samples set \(\xi_i=\zeta(Ax_i)\). For extra samples retain
the raw preactivation \(z_b=Ax_b\).
Active orthogonality and the zero cross-Gram give the exact equations
\[
 \dot\xi_i=-2r_i B_i/m,\qquad
 \dot z_b=-\frac2m\sum_{c>k}(x_b^\top x_c)
                r_c(1-u_c^2)\odot B_c.                \tag{9}
\]
The reference satisfies the first equation with bars and
\(\dot{\bar z}_b=0\).

Measure the difference by
\[
 E=\|(\xi_i-\bar\xi_i)_{i\le k}\|_{F}/\sqrt n
  +\|(z_b-\bar z_b)_{b>k}\|_{F}/\sqrt n
  +\|W-\bar W\|_F+\|w-\bar w\|_{2,n}.
 \tag{10}
\]
On a fixed horizon, (2), loss dissipation and \(w(0)=0\) bound both
readouts pointwise and both middle matrices in operator norm, uniformly
in width on the preceding matrix-norm event. Adding and subtracting
factors, using the Lipschitz bounds for \(\psi,\tanh,\tanh'\), gives
\[
 \|U-\bar U\|_{F}/\sqrt n+
 \|H-\bar H\|_{F}/\sqrt n+
 \|b-\bar b\|_{F}/\sqrt n+
 \|B-\bar B\|_{F}/\sqrt n+
 \|f-\bar f\|_2\le C_T E.                              \tag{11}
\]
For example the only readout multiplier in the top backward difference
can be taken to be a pointwise-bounded reference readout. Middle
operator differences are bounded by their Frobenius differences.
The extra raw-coordinate velocity in (9) obeys
\[
 \|(\dot z_b)_{b>k}\|_{F}/\sqrt n
       \le C_T\|(r_b)_{b>k}\|_2
       \le C_T\left(E+\|(\bar f_b)_{b>k}\|_2\right).
 \tag{12}
\]
This step is crucial: it estimates the whole extra-sample force, rather
than differentiating a gate times an unbounded backward field.
For active coordinates, subtract the first equation of (9) and use
(11). For \(W,w\), subtract (2), separate active and extra sums, and
use the rank-one difference identity and (11)–(12). The upper Dini
derivative therefore satisfies
\[
 D^+E\le C_T E+C_T\|(\bar f_b)_{b>k}\|_2,\qquad E(0)=0.
 \tag{13}
\]
Equations (8) and (13) prove
\[
 \sup_{t\le T}E(t)=O_{\mathbb P}(n^{-1/2}).             \tag{14}
\]
Thus this comparison requires neither a population flow for the
correlated dataset nor backward-field tail control for its extra samples.

## 5. Positive first-feature gap at the reference endpoint

The active orthogonal theorem constructs a finite feature-time endpoint
\(s_*\), with common prediction \(g(s_*)=a\), finite readout and middle
operator norms, and convergence of the finite reference through every
fixed physical time. It also gives convergence of the active fields to
that endpoint as physical time tends to infinity.

Permutation symmetry gives a first-feature Gram with common
and contrast eigenvectors. For \(k\ge2\), the contrast eigenvalue is positive by the
natural-coordinate noncollapse estimate in the active orthogonal proof:
on every finite feature interval,
\[
 \|(\xi_1-\xi_2)'(s)\|_2
   \le C\|\xi_1(s)-\xi_2(s)\|_2.
 \tag{15}
\]
Its initially nonzero norm cannot reach zero. Injectivity of \(\psi\)
then excludes \(u_1=u_2\) almost surely.
For the common eigenvalue, ORTHOGONAL_FEATURE_GAP.md proves a uniform
root-conditional second-moment bound on each row's natural-coordinate
displacement on every finite scalar-ascent interval. Rows whose initial
active Gaussian projections are all sufficiently positive consequently
retain positive common feature with positive conditional probability.
Passing the bounded common-feature second moment to the deterministic
population limit proves its strictly positive common eigenvalue.
That proof includes \(k=1\), and has no amplitude smallness assumption.
Thus the active endpoint first-feature Gram is positive definite for
every fixed \(k\).

For \(k=2\) there is also a simpler common-mode argument:
\(u_1=-u_2\) would imply \(h_1=-h_2\), contradicting \(g=a>0\).
For three or more columns this shortcut is invalid; the separately
checked conditional-moment argument, not that shortcut, is used.

The extra-feature covariance is
\[
 Q_{bc}=\mathbb E[\tanh(G^\top x_b)\tanh(G^\top x_c)],
       \qquad b,c>k,\quad G\sim N(0,I_d).              \tag{16}
\]
It is positive definite for distinct nonantipodal unit inputs, even
when their input Gram is singular. One elementary proof is the
linear independence of these ridge functions. Choose a direction \(v\)
such that all \(v^\top x_b\) are nonzero with pairwise distinct absolute
values; excluded directions form finitely many proper hyperplanes.
After absorbing projection signs, a linear relation restricted to
\(G=tv\) is a relation among \(\tanh(\alpha_b t)\) for distinct
positive \(\alpha_b\). Taking \(t\to\infty\) first removes its constant
term; the slowest nonzero exponential term
\(-2e^{-2\alpha_b t}\) then forces its coefficient to vanish.
Induction removes every coefficient. A zero Gaussian \(L^2\) norm
would, by continuity and full Gaussian support, give such an everywhere
zero relation. This proves (16) is positive definite.

By (4), the empirical extra Gram converges to (16). Conditional on the
entire active reference, each active–extra inner product has mean zero
and variance at most \(1/n\), because the extra first-layer rows are
independent centered bounded variables and each active coefficient has
absolute value at most one. Hence at every fixed time
\[
 \bar U(T)^\top\bar U(T)/n
 \ \longrightarrow\
 \begin{pmatrix}Q_{\rm active}(T)&0\\0&Q\end{pmatrix}
 \quad\hbox{in probability}.                         \tag{17}
\]
For all sufficiently late fixed \(T\), the limiting matrix has a fixed
positive lower bound independent of \(T\).

## 6. The full middle-layer tangent gap

The exact readout and middle-layer blocks of the tangent kernel are
\[
 K_{\rm R}=H^\top H/n,\qquad
 K_{\rm W}=(U^\top U/n)\odot(b^\top b/n).
 \tag{18}
\]
The full kernel is at least their sum. If \(U^\top U/n\succeq\lambda I\),
the Schur product theorem gives
\[
 K_{\rm W}\succeq
       \lambda\,\operatorname{diag}(\|b_a\|_{2,n}^2).
 \tag{19}
\]
To bound these diagonal entries uniformly at a late reference snapshot,
suppose \(\|\bar w\|_{2,n}\ge a/3\),
\(\|\bar w\|_\infty\le S\), and \(\|\bar W\|_{\rm op}\le M\).
The first inequality follows from the mean active prediction being
at least \(a/3\), since all activations have absolute value at most one.
For each sample \(\|\bar W\bar u_a\|_{2,n}\le M\). With
\(R=3\sqrt2 SM/a\), the readout mass on
\(\{|\bar W\bar u_a|>R\}\) is at most
\(S^2M^2/R^2=a^2/18\). Therefore
\[
 \|\bar b_a\|_{2,n}^2
 \ge (a^2/18)\operatorname{sech}^4(3\sqrt2 SM/a)>0.
 \tag{20}
\]
Equations (17)–(20) provide a positive deterministic middle-kernel gap
at late fixed reference snapshots, with probability tending to one.
This includes the extra samples, not just the active training direction.

The needed \(S,M\) do not deteriorate when the snapshot time is chosen
late. For the actual full flow define its accumulated residual clock
\[
 S_n(T)=\frac2m\int_0^T\|r_n(t)\|_1\,dt.
 \tag{21}
\]
Directly from (2),
\[
 \|w_n(T)\|_\infty\le S_n(T),\qquad
 \|W_n(T)-W(0)\|_F\le S_n(T)^2/2.
 \tag{22}
\]
The latter follows by integrating \(S_n S_n'\).
The active population reference clock is exactly \(s(T)\le s_*\).
Active compact-time convergence, (8) and (14) give
\[
 S_n(T)\le s_*+o_{\mathbb P}(1)
 \tag{23}
\]
for each fixed \(T\). Thus \(S=s_*+1\) and \(M=10+S^2/2\) work at
all the late fixed snapshots used in the argument. RMS closeness of
the readout alone would not imply the pointwise bound in (22);
the residual clock is the reason it is valid.

## 7. Deterministic capture and order of choices

For completeness, use the parameter metric
\[
 \|\Delta\theta\|^2
 =\|\Delta A\|_F^2/n+\|\Delta W\|_F^2+\|\Delta w\|_2^2/n.
 \tag{24}
\]
Its exact squared speed is \(-\dot{\mathcal L}\).
At any snapshot with a gap \(K_{\rm R}+K_{\rm W}\succeq\kappa I\)
and bounds \(S,M\) as above, there is a deterministic accumulated-clock
increment \(\eta>0\) for which that gap remains at least \(\kappa/2\).
Here is a direct justification that does not assume pointwise readout
control for arbitrary metric perturbations.

Until the future clock increment reaches \(\eta\), (2) gives
\(\|w\|_\infty\le S+\eta\),
\(\|W-W(T)\|_F\le S\eta+\eta^2/2\), and
\[
 \|A-A(T)\|_F/\sqrt n
 \le \int_0^\eta (S+v)(M+Sv+v^2/2)\,dv.
 \tag{25}
\]
The unit-input assumption and the triangle inequality suffice for (25).
The first features, upper features and the tangent features
\(h_a,\ b_a\otimes u_a\) consequently change by quantities tending to
zero with \(\eta\), uniformly in width. Their Gram changes tend to
zero as well. Choose \(\eta\) small enough to preserve the stated gap.

While it is preserved,
\[
 \frac{d}{dt}\|r\|_2\le-\kappa\|r\|_2/m,\qquad
 \frac2m\|r\|_1\le\frac{2}{\sqrt m}\|r\|_2.
 \tag{26}
\]
The total future clock increment is therefore at most
\[
 2\sqrt m\,\|r(T)\|_2/\kappa.                         \tag{27}
\]
If this is strictly below \(\eta\), a first-exit argument proves
capture forever and exponential loss decay. This is a finite-width
deterministic argument.

Choose endpoint bounds and the resulting \(\kappa,\eta\) first.
Then choose a deterministic \(T\) sufficiently late that the active
population residual is smaller than the strict threshold in (27).
The limiting active first-feature gap is positive, so the same endpoint
bounds hold at this time. Finally send \(n\to\infty\).
Equations (8), (14), (17) and (23) imply that the actual full snapshot
has the required gap, bounds and residual with probability tending to
one. Capture proves (1). There is no exchange of the limits \(n\to\infty\)
and \(t\to\infty\).

## 8. What is and is not proved

This construction removes any global small-label-amplitude condition
on this class, permits \(m\) arbitrarily larger than input rank, and
retains the exact canonical Gaussian initialization and full training.
It is not the general arbitrary-label theorem: in the base result the
extra labels are exactly zero, and the active labels have a common
arbitrary magnitude with arbitrary signs. The separate open-neighborhood argument is needed
to replace those equalities by robust nonzero-label neighborhoods.

No uniform width bound, sharp rate, efficient simulation theorem,
compression theorem, or incompressibility lower bound follows merely
from (1). Those claims require their own estimates.
