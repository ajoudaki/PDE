# Gaussian trapping renewal: an exclusion theorem and a sign-adapted obstruction

2026-10-11. Scoped theoretical continuation; no experiment or Git operation.
Scientific inputs were the supervisor's assignment, `docs/notation.qmd`, and
the complete `GLOBAL_FAILURE_ALTERNATIVES.md`, `GAUSSIAN_NEGATIVE_MASS.md`,
`GAUSSIAN_CAPTURE_RENEWAL.md`, `TANH_LARGE_RESIDUAL_CAPTURE.md`, and
`FITTING_BOUNDARY_RESULT.md`. Required research, proof, and canonical-notation
skills were applied. No other study or concurrent route was consulted.

**Status.** The requested nonvanishing-probability Gaussian failure theorem
remains open. The main new result is a quantitative obstruction to the known
near-initial-loss traps: at every fixed label radius, canonical Gaussian
initialization gives a definite fractional loss decrease in a definite time,
simultaneously for all labels in that radius, except on an exponentially small
event. Consequently the known bad manifolds with sufficiently large residual
parameter have exponentially small Gaussian capture probability. A second
result shows why uncorrected Gaussian-noise Hessian arguments cannot establish
a broader positive theorem: adaptive hidden sign choices preserve Gaussian
middle-layer noise while making an existing bad profile a strict normal local
minimum with probability tending to one. Capture from Gaussian first weights
and exactly zero readout is not established for these minima.

## 1. Exact model and probability contract

Let \(X=[x_1,\ldots,x_m]\in\mathbb R^{d\times m}\) have fixed unit columns,
with no pair parallel or antiparallel. Let \(y\in\mathbb R^m\) be fixed
independently of width and initialization. Write

\[
U=\tanh(AX),\qquad H=\tanh(WU),\qquad
f=H^\top w/n,\qquad r=f-y,\qquad
\mathcal L=\|r\|_2^2/m.
\]

Here \(A\in\mathbb R^{n\times d}\), \(W\in\mathbb R^{n\times n}\), and
\(w\in\mathbb R^n\). The physical mobilities are \((n,1,n)\), and the
initialization is independent \(A_{jk}(0)\sim N(0,1)\),
\(W_{ij}(0)\sim N(0,1/n)\), with **exactly** \(w(0)=0\).
Put \(D=1-H\odot H\) and \(E=1-U\odot U\). The exact equations are

\[
\begin{aligned}
\dot w&=-\frac2mHr,\\
\dot W&=-\frac{2}{mn}\operatorname{diag}(w)D
                  \operatorname{diag}(r)U^\top,\\
\dot A&=-\frac2m
\{W^\top\operatorname{diag}(w)D\odot E\}
                  \operatorname{diag}(r)X^\top.
\end{aligned}                                                    \tag{1}
\]

Loss dissipation gives \(\|r(t)\|_2\le\|y\|_2\), global finite-time
existence, and

\[
\dot{\mathcal L}=-\frac4{m^2}r^\top Kr,
\qquad K\succeq H^\top H/n.                                    \tag{2}
\]

The unresolved negative target is a fixed compatible \(X,y\ne0\) and
\(c,p>0\) for which

\[
\liminf_{n\to\infty}
\Pr\{\lim_{t\to\infty}\mathcal L_n(t)\ge c\}\ge p.
\]

The time limit is inside the probability and precedes the width limit.
No result below interchanges those limits.

## 2. A uniform initial loss decrease under Gaussian initialization

Fix a Euclidean label radius \(B>0\), and put \(R=\|X\|_{\rm op}\).
Define the two deterministic covariance matrices

\[
C_{ab}=\mathbb E_{g\sim N(0,I_d)}
 [\tanh(g^\top x_a)\tanh(g^\top x_b)],\qquad
Q=\mathbb E_{Z\sim N(0,C)}[\tanh(Z)\tanh(Z)^\top].                 \tag{3}
\]

Both are positive definite. For \(C\), choose a direction \(v\) whose
projections onto the inputs are nonzero with distinct absolute values.
The functions \(t\mapsto\tanh(tv^\top x_a)\) are linearly independent:
in a vanishing linear combination, subtract its limiting constant at
\(t\to\infty\) and successively isolate the slowest exponential
\(e^{-2t|v^\top x_a|}\). A nonzero linear combination of the ridge features
therefore cannot vanish everywhere. Continuity and the positive Gaussian
density make its squared Gaussian expectation positive. For \(Q\), the
Gaussian \(Z\) has full support, and the coordinatewise tanh image contains
the open box \((-1,1)^m\). No nonzero linear form vanishes on that box.

Set

\[
\lambda=\tfrac12\lambda_{\min}(Q)>0,\qquad
b=\frac{2B}{\sqrt m},\qquad
z=\min\left\{1,\frac{\sqrt\lambda}
 {2(\sqrt m+81R^2)}\right\},\qquad
\tau=\frac{\sqrt{2z}}b,\qquad
\rho=\exp(-\lambda\tau/m)<1.                                  \tag{4}
\]

**Theorem 1.** There are constants \(C_X,c_X>0\), independent of \(n\)
and of labels in the ball \(\|y\|_2\le B\), such that with probability
at least \(1-C_Xe^{-c_Xn}\), all these label flows satisfy

\[
\mathcal L_n(\tau)\le\rho\mathcal L_n(0),\qquad
\mathcal L_n(\infty)\le\rho\mathcal L_n(0).                     \tag{5}
\]

The exceptional event depends only on the hidden initialization and \(X\).
The case \(y=0\) is the stationary zero-loss case. This theorem proves a
definite amount of learning, not fitting.

### Initial Gaussian event

Let \(C_n=U(0)^\top U(0)/n\). Each entry is an average of independent
bounded variables, so Hoeffding's inequality and a union bound give
exponential concentration of \(C_n\) around \(C\). Given \(A(0)\), the
rows of \(W(0)U(0)\) are independent \(N(0,C_n)\) vectors. Consequently
the conditional expected top-feature covariance is \(Q(C_n)\), where
\(Q(C')=\mathbb E[\tanh(Z)\tanh(Z)^\top]\) for \(Z\sim N(0,C')\).
The map \(Q(C')\) is continuous near the positive definite \(C\): use
\(Z=C'^{1/2}\xi\), continuity of the square root, and bounded dominated
convergence. Choose a fixed covariance neighborhood on which
\(\|Q(C')-Q\|_{\rm op}<\lambda_{\min}(Q)/4\).
Conditional Hoeffding concentration of the bounded top-feature products
then proves

\[
\Pr\{\lambda_{\min}(H(0)^\top H(0)/n)<\lambda\}
\le C_Xe^{-c_Xn}.                                               \tag{6}
\]

Here the form of Hoeffding used is
\(\Pr(|N^{-1}\sum_i V_i-\mathbb EV_i|>a)
\le2\exp(-Na^2/2)\) for independent \(V_i\in[-1,1]\), and finite
\(m\) permits conversion of entrywise errors to operator norm.

An elementary sphere-net bound also gives

\[
\Pr\{\|W(0)\|_{\rm op}>8\}
\le2\exp[-(8-\log81)n].                                        \tag{7}
\]

Indeed take a \(1/4\)-net of the unit sphere of size at most \(9^n\).
The bilinear supremum is at most twice its supremum on a pair of such
nets, and for each fixed pair \(u,v\), \(u^\top W(0)v\sim N(0,1/n)\).
A union bound at level (4) proves (7). Intersect (6) and (7).

### Deterministic short-time bound

On this initial event, (1), bounded tanh and (2) give, simultaneously
for \(\|y\|_2\le B\),

\[
\begin{aligned}
\|w(t)\|_\infty&\le bt,\\
\|\dot W(t)\|_F&\le b\|w(t)\|_\infty\le b^2t,\\
\|W(t)\|_{\rm op}&\le8+b^2t^2/2,\\
\frac{\|\dot A(t)\|_F}{\sqrt n}
&\le bR\|W(t)\|_{\rm op}\|w(t)\|_\infty,\\
\frac{\|\dot U(t)\|_F}{\sqrt n}
&\le b^2R^2\|W(t)\|_{\rm op}t.
\end{aligned}                                                   \tag{8}
\]

For example, the middle-weight bound follows by writing its derivative
as the sum over samples of rank-one matrices and using
\(\|U_{:a}\|_2\le\sqrt n\),
\(\|w\odot D_{:a}\|_2\le\sqrt n\|w\|_\infty\), and
\(\|r\|_1\le\sqrt m B\). In the first-weight bound, use
\(\|D\|_F\le\sqrt{nm}\) and \(\|\operatorname{diag}(r)\|_{\rm op}\le B\).

Since \(\dot H=D\odot(\dot WU+W\dot U)\) and
\(\|U\|_{\rm op}\le\sqrt{nm}\), integrating (8) yields

\[
\frac{\|H(t)-H(0)\|_F}{\sqrt n}
\le\frac{b^2t^2}{2}
 \left[\sqrt m+R^2(8+b^2t^2/2)^2\right].                         \tag{9}
\]

For \(0\le t\le\tau\), the right side is at most
\(z(\sqrt m+81R^2)\le\sqrt\lambda/2\). The singular-value perturbation
bound therefore gives

\[
H(t)^\top H(t)/n\succeq(\lambda/4)I_m.
\]

Substituting in (2) gives
\(\dot{\mathcal L}\le-(\lambda/m)\mathcal L\) through time \(\tau\).
Integration and monotonicity prove (5). The horizon is fixed before
taking width to infinity.

## 3. Exponentially small capture of the high-retained-loss manifolds

Let \(h_*\perp r_0\), with \(h_*\ne0\), \(r_0\ne0\), be any of the
existing tanh profile constructions in `TANH_LARGE_RESIDUAL_CAPTURE.md`.
Fix \(B>0\) and normalize the labels by

\[
y_M=s_M(h_*-Mr_0),\qquad
s_M=\frac{B}{\sqrt{\|h_*\|_2^2+M^2\|r_0\|_2^2}}.                \tag{10}
\]

These labels have norm exactly \(B\) and are fixed independently of width
when \(M\) is fixed. The existing bad critical manifold predicts
\(s_Mh_*\), so its loss fraction is

\[
R_M=\frac{M^2\|r_0\|_2^2}
 {\|h_*\|_2^2+M^2\|r_0\|_2^2}.                                 \tag{11}
\]

Choose \(M\) above the existing capture threshold and also so that

\[
M^2>\frac{\rho}{1-\rho}
 \frac{\|h_*\|_2^2}{\|r_0\|_2^2}.                              \tag{12}
\]

Then \(R_M>\rho\). By Theorem 1,

\[
\Pr\{\mathcal L_n(\infty)\ge R_M\mathcal L_n(0)\}
\le C_Xe^{-c_Xn}.                                               \tag{13}
\]

In particular, the probability of convergence to any part of that bad
manifold is bounded by (13). The same exclusion applies to an entire
neighborhood whose loss is strictly above \(\rho\mathcal L_n(0)\) after
time \(\tau\). It concerns actual eventual capture, not just the Gaussian
mass of a chosen small starting neighborhood.

This does not contradict the existing nonempty open basin at each fixed
width. It quantitatively resolves the probability gap for sufficiently
high-retained-loss instances of that family. It does not exclude another
bad attractor with lower loss, or the same construction at smaller \(M\).
The proof keeps \(M\), the labels, and \(\tau\) fixed as \(n\to\infty\).

## 4. Gaussian noise at a bad profile: instability and its sign loophole

The explicit existing profile has \(p_*\in\mathbb R^d\), \(q_*=1\),
\(u_a=\tanh(p_*^\top x_a)\), and \(h_a=\tanh(u_a)\). Put
\(\chi_a=\tanh'(p_*^\top x_a)\), \(D_a=\tanh'(u_a)\), and
\(\sigma_a=\tanh''(u_a)\). Its residual moments include

\[
\begin{gathered}
\sum_a r_{0,a}h_a=0,\qquad
\sum_a r_{0,a}D_au_a=0,\qquad
\sum_a r_{0,a}D_a\chi_ax_a=0,\\
\sum_a r_{0,a}\sigma_au_a^2=1,\qquad
\sum_a r_{0,a}\sigma_au_a\chi_ax_a=0,\\
\sum_a r_{0,a}\sigma_a\chi_a^2x_ax_a^\top=0,\qquad
\sum_a r_{0,a}D_a\tanh''(p_*^\top x_a)x_ax_a^\top=I_d.
\end{gathered}                                                   \tag{14}
\]

These are precisely the separate zero and identity terms displayed in
the existing capture note, including its equation (29) verification.
Take \(y=s(h-Mr_0)\), \(s,M>0\). Every state

\[
A_{j:}=p_*^\top,\qquad W\mathbf1=\mathbf1,\qquad
\mathbf1^\top w/n=s                                             \tag{15}
\]

is critical, with residual \(sMr_0\). Let \(c=W^\top w\). For a
parameter perturbation \((\delta A,\delta W,\delta w)\), put
\(v=\delta W\mathbf1\) and let \(\delta f\) be its first prediction
variation. Direct second differentiation and (14) give

\[
D^2\mathcal L[\delta\theta,\delta\theta]
=\frac2m\|\delta f\|_2^2
 +\frac{2sM}{mn}
  \left[\sum_i w_i v_i^2+\sum_j c_j\|\delta A_{j:}\|_2^2\right]. \tag{16}
\]

To verify that nothing is omitted, write
\(\delta z_{ia}=u_av_i+\chi_a\sum_jW_{ij}x_a^\top\delta A_{j:}\).
The residual contraction of \(\sigma_a\delta z_{ia}^2\) retains only
\(v_i^2\) by the fourth, fifth and sixth moments in (14). The bottom
second derivative gives the last moment, weighted by \(c_j\).
The mixed readout and mixed \(W,A\) terms vanish by the second and
third moments. The remaining squared-Jacobian term is the first term
of (16).

If \(k\ge2\) coordinates of \(c\) are negative, restrict to perturbations
of their \(A\) rows with \(\sum_j c_j\delta A_{j:}=0\), and set the
other perturbations to zero. Then \(\delta f=0\), while (16) is strictly
negative on a subspace of dimension \(d(k-1)\). Thus the Hessian has at
least \(d(k-1)\) negative eigenvalues.

For \(G_{ij}\sim N(0,1/n)\), let \(P=\mathbf1\mathbf1^\top/n\), and
consider the Gaussian lift \(W=G(I-P)+P\), \(w=s\mathbf1\).
It satisfies (15), and

\[
c_j=s(1+Z_j-\bar Z),\qquad
Z_j=(G^\top\mathbf1)_j\overset{\rm iid}{\sim}N(0,1).
\]

Hence \(k/n\to\Phi(-1)>0\) in probability, and this particular lift is
a saddle with a linear number of negative directions. More generally
the number (1) can be replaced by a fixed row sum \(q\), giving
\(\Phi(-q)\) when compatible moments are available. This calculation
does **not** describe the law of a dynamically selected endpoint.

There is a decisive sign loophole. Define instead

\[
\varepsilon_j=\operatorname{sign}(Z_j),\qquad
A_{j:}=\varepsilon_jp_*^\top,\qquad
W=G+(\mathbf1-G\varepsilon)\varepsilon^\top/n,\qquad
w=s\mathbf1.                                                   \tag{17}
\]

Now \(W\varepsilon=\mathbf1\), so this is the same critical profile
after the exact first-neuron sign symmetry. In the sign-adjusted
coordinates, the coefficients in (16) are

\[
\varepsilon_j(W^\top w)_j
=s\left(|Z_j|+1-\frac1n\sum_l|Z_l|\right).                      \tag{18}
\]

Since \(\mathbb E|Z|=\sqrt{2/\pi}<1\), with probability at least
\(1-e^{-cn}\) all coefficients in (18) are strictly positive. For
example choose \(a\in(\sqrt{2/\pi},1)\); the moment-generating function
of \(|Z|\) is finite, and a sufficiently small \(t>0\) satisfies
\(\log\mathbb Ee^{t|Z|}<ta\), giving
\(\Pr(n^{-1}\sum|Z_l|\ge a)\le e^{-n(ta-\log\mathbb Ee^{t|Z|})}\).

As \(w_i=s>0\), (16) is then nonnegative. Its kernel consists exactly
of tangents to the affine critical manifold: \(\delta A=0\),
\(\delta W\varepsilon=0\), and \(\mathbf1^\top\delta w=0\).
Indeed the positive terms first force the first two conditions;
the remaining prediction variation is \(h\mathbf1^\top\delta w/n\),
and \(h\ne0\). This is a strict normal local minimum. Taylor expansion
in affine normal/tangent coordinates gives a full-parameter attracting
neighborhood at each fixed width, by the same elementary local trapping
argument in the existing capture note.

The middle-matrix change in (17) has Frobenius norm

\[
\|W-G\|_F=\frac{\|\mathbf1-G\varepsilon\|_2}{\sqrt n}
\le1+\|G\|_{\rm op},                                           \tag{19}
\]

which is bounded with exponentially high probability. Thus the full
Gaussian matrix need not be close to a rank-one matrix in Frobenius norm
for the bad profile to be locally stable. Sign adaptation defeats a
claim that Gaussian bulk noise alone destabilizes every replicated bad
endpoint. Nevertheless, (17) engineers the first-layer collapse and
nonzero readout; neither has the requested initialization law.
Its attracting neighborhood has not been shown to meet the exact
zero-readout slice at appreciable Gaussian mass. For labels satisfying
(12), Theorem 1 already excludes appreciable Gaussian capture of it.

## 5. Exact transverse test for a saturated replicated escape

The supervisor additionally proposed a full-column-rank, three-input escape
geometry

\[
x_1=(c,s,0),\qquad x_2=(c,-s,0),\qquad x_3=(k,0,\epsilon),
\quad c^2+s^2=k^2+\epsilon^2=1,\quad k>c>0,
\]

with labels \((a,a,b)\), \(a>b>0\). A first weight along the first
coordinate gives the lower-label sample the larger positive margin. This
is compatible with the existing ordering-based escape mechanism, but the
top-neuron splitting directions require separate control.

For any inputs and labels, the family

\[
A_{j:}=p^\top,\qquad W_{ij}=q_i/n,\qquad w_i=v_i
\]

is invariant. Indeed all first-row velocities agree, and each middle-row
velocity is constant across its columns. Its prediction is
\(n^{-1}\sum_i v_i\tanh(q_i u_a)\), where
\(u_a=\tanh(p^\top x_a)\). Its top-coordinate equations are exactly

\[
\dot v_i=-\frac2m\sum_a r_a\tanh(q_i u_a),\qquad
\dot q_i=-\frac{2v_i}{m}\sum_a r_a u_a\tanh'(q_i u_a).           \tag{21}
\]

Along a symmetric solution \(q_i=q\), \(v_i=v>0\), take a nonzero
vector \(\eta\in\mathbb R^n\) with \(\sum_i\eta_i=0\), and perturb
\(q_i\) by \(\eta_i\xi\) and \(v_i\) by \(\eta_i\zeta\).
The first variations of the prediction and of the common first-weight
velocity vanish. Hence the exact variational system closes as

\[
\frac d{dt}\begin{pmatrix}\xi\\\zeta\end{pmatrix}
=-\frac2m
\begin{pmatrix}v a_r&b_r\\b_r&0\end{pmatrix}
\begin{pmatrix}\xi\\\zeta\end{pmatrix},\qquad
\begin{aligned}
b_r&=\sum_a r_a u_a\tanh'(q u_a),\\
a_r&=\sum_a r_a u_a^2\tanh''(q u_a).
\end{aligned}                                                  \tag{22}
\]

The instantaneous matrix has determinant \(-4b_r^2/m^2<0\) whenever
\(\dot q\ne0\). Indefiniteness of a time-varying matrix alone does
not prove accumulated instability. The following sufficient condition
does: suppose on a tail that \(\dot q>0\), \(q\to\infty\),
\(0<v\le V<\infty\), and \(a_r/b_r\ge-C\) for some \(C\ge0\).
Reparametrizing (22) by \(q\) gives

\[
\frac{d\xi}{dq}=\frac{a_r}{b_r}\xi+\frac\zeta v,\qquad
\frac{d\zeta}{dq}=\frac\xi v.                                  \tag{23}
\]

Start with \(\xi,\zeta>0\). The positive quadrant is invariant.
Componentwise its velocity is bounded below by that of the constant
cooperative matrix
\(M_0=\bigl(\begin{smallmatrix}-C&1/V\\1/V&0\end{smallmatrix}\bigr)\).
Let \(l\) be a positive left eigenvector for its positive eigenvalue

\[
\lambda_+=\frac{\sqrt{C^2+4/V^2}-C}{2}>0.
\]

Then \(d[l^\top(\xi,\zeta)]/dq\ge
\lambda_+l^\top(\xi,\zeta)\), which proves exponential growth in
\(q\). Thus these explicit tail hypotheses prevent uniformly bounded
transverse linear response about the symmetric escape.

For orientation only, at exact readout equilibrium for two distinct
effective margins, the ratio \(a_r/b_r\) is a divided difference.
Writing \(h=\tanh q\), as both margins approach one at fixed \(q\)
it tends to

\[
\frac{4h(qh-1)}{1-q(h+1/h)},
\]

which subsequently tends to \(-2\) as \(q\to\infty\). This follows
by dividing the moment functions by \(\tanh(qu)\): their relevant
derivatives at \(u=1\) are those of
\(u\tanh'(qu)/\tanh(qu)\) and \(-2u^2\tanh'(qu)\).
This iterated asymptotic is **not** a proof of the required ratio bound
along an actual joint escape; readout tracking and the joint rates remain
to be proved. Even a verified transverse instability would not exclude
nearby trajectories escaping in a different, nonsymmetric configuration.
It does block treating the scalar escape's open full-network basin as
automatic.

## 6. Initial motion and the remaining bottleneck

For completeness, the requested initial activity is automatic almost
surely when \(y\ne0\), \(n\ge m\). The initial top-feature matrix has
full column rank, so \(\dot{\mathcal L}(0)<0\). Both hidden velocities
vanish at time zero, as exact zero readout requires, but both hidden
feature matrices have nonzero second derivative almost surely.

Here is a direct verification of the latter point. Regard

\[
F(A,W)=\frac1{2n}\|H(A,W)y\|_2^2
\]

as a function of hidden parameters. Differentiating (1) at zero readout
gives

\[
\ddot A(0)=\frac{4n}{m^2}\nabla_AF(A_0,W_0),\qquad
\ddot W(0)=\frac4{m^2}\nabla_WF(A_0,W_0).                        \tag{24}
\]

The analytic function \(F\) is not constant in \(A\): it vanishes at
\(A=0\) but is positive at hidden parameters with \(H\) full column
rank. Thus at least one component of \(\nabla_AF\) is a nonzero
analytic function of \((A,W)\), whose zero set has Lebesgue measure
zero. Consequently \(\ddot A(0)\ne0\) almost surely. Each row of
\(\ddot A(0)\) lies in the span of the input columns; multiplication
by \(X\) is injective on that row subspace. Strict positivity of tanh'
therefore gives \(\ddot U(0)\ne0\).

Finally, the derivative of \(F\) in the hidden acceleration direction
equals

\[
\frac1n(Hy)^\top\ddot H(0)y
=\frac4{m^2}
 \left[n\|\nabla_AF\|_F^2+\|\nabla_WF\|_F^2\right]>0,
\]

so \(\ddot H(0)\ne0\). This proves actual immediate feature learning;
it does not control late-time loss.

The remaining negative obligation is to prove that typical Gaussian
trajectories reach and remain in a bad region whose loss is below the
uniform threshold (5), allowing readout/hidden sign selection and all
trained-layer feedback. The sign-adapted critical construction makes
such a geometric endpoint plausible but supplies no capture argument.
The explicit escape trajectory in the supplied source still has a
Gaussian-null symmetric initialization and no established basin mass.
Finite-time corrective cohorts from the alternate-activation source
do not transfer to tanh/tanh or to an infinite-time assertion.

| Claim | Status and limit |
|---|---|
| Definite fractional loss decrease for all labels in a fixed ball | Proved by (3)–(9), with exponentially high Gaussian probability at a fixed horizon. |
| Capture of sufficiently high-retained-loss existing bad manifolds | Exponentially small probability by (10)–(13), for fixed labels and time limit first. |
| Unadapted Gaussian lift of the explicit bad manifold | A saddle with order-\(n\) negative index, by (16). |
| Sign-adapted Gaussian lift | A strict normal local minimum with exponentially high probability; this is an engineered endpoint law. |
| Canonical Gaussian capture of any lower-loss finite trap | Open. |
| Canonical Gaussian positive-loss escape | Open. |
| Stability of the proposed replicated saturated escape | Exact splitting equation (22); conditional amplification criterion (23), with its tail hypotheses unverified. |
| Arbitrary-label high-probability fitting | Open; (5) alone cannot be iterated without new control of the evolved state. |

No known all-width open-basin theorem is superseded. What is superseded is
the unresolved probability status of its sufficiently high-retained-loss
instances: those particular manifolds cannot provide the requested
macroscopic Gaussian failure event. The broader fitting/failure question
remains unresolved.
