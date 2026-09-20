# Explicit fitting regions for arbitrary finite data under actual minibatch SGD

2026-09-19. Lead proof from the complete established
`docs/observable_p1.md` and `docs/NOTATION.md`. No other study is an input.
This concerns exact p=1 population SGD, not a diffusion or a finite-width
network. The theorem constructs its starting region from the data; it does
not assume a future Gram bound or an unknown trained endpoint.

## 1. The positive statement and its limitation

Let d>=2, let x_i in sqrt(d) S^(d-1) be finitely many inputs, let p_i>0
sum to one, and let y_i be fixed finite labels (in particular, arbitrary
mixtures of +1 and -1). Assume the architectural compatibility conditions:
equal inputs have equal labels, and antipodal inputs have opposite labels.
Keep the canonical p=1 correlated Gaussian-derived features and their
normalization, the complete trainable matrix and its actual transpose,
phi=tanh, the odd invariant sector, and the physical L2/L2/Frobenius norm.

For every such dataset, there is an explicitly defined finite-norm fitting
state theta_*, and for every delta in (0,1) an explicit positive radius
r_delta and step bound eta_* with the following property. From **every**
initial state in the physical ball ||theta_0-theta_*||<r_delta, fresh iid
minibatch SGD of **any fixed batch size B>=1**, including B=3, with any
constant step 0<eta<=eta_* converges to a zero-loss finite state with
probability at least 1-delta. On the stated successful event the total
state travel is finite, and its conditional expected loss decays
geometrically, with explicit constants below.

This is a local training theorem for a data-defined open region. It does
not prove that SGD from the canonical initial state (w,c,M)=(g,0,D)
enters that region, or fits globally. It preserves the canonical marks
and trains all blocks, but its guaranteed starting states differ from
canonical initialization. It is not a replacement answer for the missing
canonical entry theorem.

## 2. Constructing theta_* without a trained endpoint

Duplicate inputs and compatible antipodes can first be merged. Their
sample loss functions, and hence their sample gradients at every state,
are identical, since f(-x)=-f(x). The merged probability is the sum of
their probabilities. Drawing original samples or these merged
representatives therefore gives exactly the same law of SGD updates.
After merging, write u_i=x_i/sqrt(d); all u_i are distinct modulo sign.

Choose r in R^d outside the finite union of hyperplanes

\[
 r\cdot u_i=0,\qquad r\cdot(u_i-u_j)=0,
                         \qquad r\cdot(u_i+u_j)=0.     \tag{1}
\]

Each displayed normal is nonzero, so the union has Lebesgue measure zero
by iterated integration. Its open complement is nonempty. A deterministic
construction is to enumerate rational vectors until one violates all
equalities. Thus t_i=r dot u_i are nonzero with pairwise distinct squares.

Let e=sign G_1 and let q select the first normalized h-coordinate of the
nonconstant b_1. Set

\[
 \kappa=E_1[(q\cdot b_1)e]=E_1|q\cdot b_1|>0,
 \qquad w_*=er,\quad M_*=e_1q^T.
\]

These fields are in the canonical odd sector. With A=E_1[b_1e], all
lower moments are a_i=phi(t_i)A, so v_i=M_*a_i=z_i e_1 with
z_i=kappa phi(t_i). The z_i are nonzero with distinct squares. The
functions H_i=phi(z_i b_{2,1}) are linearly independent in upper L2.

Here is a proof for arbitrary finite sample count. The upper coordinate
has positive density on an interval containing zero. A vanishing L2
linear combination of the H_i therefore vanishes everywhere on that
interval by continuity. Its analytic power series is zero. All odd
Taylor coefficients of tanh are nonzero: write
phi(t)=sum_{n>=0} (-1)^n b_n t^(2n+1). From phi'=1-phi^2,

\[
 b_0=1,\qquad
 b_n=\frac1{2n+1}\sum_{j+k=n-1}b_jb_k>0\quad(n>=1).
\]

The first m odd coefficients of a relation sum_i alpha_i H_i=0 thus
give sum_i alpha_i z_i (z_i^2)^n=0 for n=0,...,m-1. The Vandermonde
matrix has determinant product_{i<j}(z_j^2-z_i^2), nonzero, so all
alpha_i=0. Consequently the Gram K_ij=E_2[H_iH_j] is positive definite.
Define the bounded odd readout

\[
                         c_*=\sum_i(K^{-1}y)_i H_i.  \tag{2}
\]

It gives f_i=y_i exactly. The fixed Gaussian carriers, including the
joint correlations of g and b_1, are unchanged. The displacement w_*-g
is square integrable. Equations (1)--(2) completely specify a fitting
state from the given data and fixed canonical expectations.

## 3. Explicit local constants

Write theta=(w-g,c,M), and retain the physical norm. Let
B_l=ess sup |b_l|, C=||c_*||_2+1, and R_M=||M_*||_F+1. On the unit
ball about theta_*, write J_i=grad f_i. Directly from the physical
gradient formula,

\[
 J_i=(\phi'(w\cdot u_i)(b_1^TM^Td_i)u_i,
                   H_i,\ d_i a_i^T),\quad
 d_i=E_2[b_2c\phi'(b_2\cdot Ma_i)],
\]

we have ||J_i||<=G, where

\[
 G^2=1+B_1^2B_2^2C^2(R_M^2+1).                    \tag{3}
\]

The following explicitly computable bounds suffice for Lipschitz
constants on this ball:

\[
 D=B_2+2B_2^2CB_1(1+R_M),\qquad h=B_1B_2(1+R_M),
\]
\[
 J=2B_1R_MB_2C+B_1B_2C+B_1R_MD
                          +h+B_1D+B_1B_2C,
 \qquad K_L=2(G^2+GJ).                              \tag{4}
\]

Specifically ||d_i-d_i'||<=D||theta-theta'|| and
||H_i-H_i'||_2<=h||theta-theta'||. These follow from
|a_i-a_i'|<=B_1||w-w'||_2,
|Ma_i-M'a_i'|<=B_1(1+R_M)||theta-theta'||,
and |phi''|<=2. Subtracting the three blocks of J_i gives successively
the first three terms, the fourth term, and the last two terms of J
in (4); using the sum of block norms bounds the Hilbert norm. Hence
||J_i-J_i'||<=J||theta-theta'||.

Because f_i(theta_*)=y_i, integration along a segment gives
|f_i(theta)-y_i|<=G||theta-theta_*||. Subtracting
grad ell_i=2(f_i-y_i)J_i now gives the Lipschitz constant K_L in (4)
for each sample gradient and their weighted mean on the unit ball.
These estimates require only first derivatives and locally Lipschitz
gradients, not a generally Frechet-C2 lower gate map on L2.

Let lambda_* be the smallest eigenvalue of the positive definite
weighted readout Gram (sqrt(p_i p_j) K_ij). Set

\[
 R=\min\{1,\lambda_*/(4h)\},\qquad
 \lambda=\lambda_*/2,\qquad
 \eta_*=\min\{1/(4G^2),\lambda/(K_LG^2)\}.          \tag{5}
\]

On the radius-R ball the current weighted readout Gram has smallest
eigenvalue at least lambda. To verify it, regard its feature map as
T z=sum_i sqrt(p_i)z_i H_i. Both current and reference maps have
operator norm at most one, while their difference has norm at most
h||theta-theta_*||. Their Grams consequently differ in operator norm
by at most 2h||theta-theta_*||<=lambda_*/2. The variational
characterization of the smallest eigenvalue proves the bound.
In particular the full gradient satisfies, on this fixed ball,

\[
              \|\nabla L(\theta)\|^2\ge4\lambda L(\theta),
 \qquad E[\|\widehat g\|^2\mid\theta]\le4G^2 L(\theta). \tag{6}
\]

The first estimate uses its readout component alone. The second uses
Jensen for a batch average and ||g_i||<=2G|f_i-y_i|. The actual update
still trains every block; neither estimate freezes a block.

## 4. Actual SGD stays and fits with a quantified probability

Fix B>=1, 0<eta<=eta_*, and delta in (0,1). Define

\[
 r_\delta=\min\{R/4,\delta\lambda R/(8G^2)\},
 \qquad q=1-2\eta\lambda\in[1/2,1).                \tag{7}
\]

Start at any theta_0 with ||theta_0-theta_*||<r_delta. Let tau be the
first integer k with ||theta_k-theta_*||>=R/2, or infinity. While
k<tau, every possible update has length at most
2 eta G max_i|f_i-y_i|<=eta G^2 R<=R/4. Its endpoint and segment
therefore stay inside the radius-R ball. The Lipschitz-gradient
inequality, obtained by integrating grad L along that segment, and (6)
give

\[
 E[L(\theta_{k+1})\mid\theta_k]
 \le L-\eta\|\nabla L\|^2+\tfrac12K_L\eta^2 E\|\widehat g\|^2
 \le (1-4\eta\lambda+2K_L\eta^2G^2)L
 \le q L,\qquad k<\tau.                             \tag{8}
\]

Define the killed loss V_k=1_{tau>k}L(theta_k). Nonnegativity and (8)
give E V_k<=q^k L(theta_0). The expected total length of all updates
made before the exit, including the exiting update if there is one, is

\[
 \begin{split}
 E\sum_{k\ge0}1_{\{k<\tau\}}\|\theta_{k+1}-\theta_k\|
 &\le2\eta G\sum_{k\ge0}\sqrt{E V_k}\\
 &\le\frac{2\eta G\sqrt{L(\theta_0)}}{1-\sqrt q}
 \le\frac{2G}{\lambda}\sqrt{L(\theta_0)}.           \tag{9}
 \end{split}
\]

Exit requires length at least R/4 from the stated initial ball. Markov's
inequality, (9), and sqrt(L(theta_0))<=G||theta_0-theta_*|| imply

\[
 \mathbb P(\tau<\infty)
 \le\frac{8G\sqrt{L(\theta_0)}}{\lambda R}
 \le\frac{8G^2\|\theta_0-\theta_*\|}{\lambda R}<\delta. \tag{10}
\]

The nonnegative path length in (9) is finite almost surely because its
expectation is finite. Also sum_k E V_k<infinity, so sum_k V_k is finite
almost surely. On the event tau=infinity the actual state thus has
finite total length, converges in the complete Hilbert space, and has
L(theta_k)=V_k ->0. Continuity of L makes its finite endpoint an exact
fit. On the same event the quantitative conditional estimate is

\[
 E[L(\theta_k)\mid\tau=\infty]
                    \le\frac{q^k L(\theta_0)}{1-\delta}. \tag{11}
\]

No claim is made about the unconditional loss after an exit, and (8)
is not a pathwise monotonicity assertion. All probabilities concern the
specified iid sampling with replacement. The constants may be very
small or large as data geometry becomes poorly conditioned. Every
constant is defined from the data, fixed marks, and explicit theta_*.

## 5. Relation to the requested global result

This supplies an actual noisy-training convergence theorem for general
finite compatible configurations, including arbitrary sample count in
low dimension. It also proves zero-loss representability under exactly
the obvious odd-architecture compatibility restrictions. Those are
useful positive conclusions; neither requires independent input vectors.

The theorem leaves the main global obligation intact: from canonical
(g,0,D), prove entry into a successful fitting region (or another global
progress principle), excluding collapsed sample-stationary sets and
unbounded/nonconvergent trajectories. Local stochastic exit from a
non-common bad point does not give that entry. The proof makes no
implicit use of the canonical starting state being random in field
space: its Gaussian marks are already integrated into a fixed state.

Status: complete lead candidate, awaiting independent check.
