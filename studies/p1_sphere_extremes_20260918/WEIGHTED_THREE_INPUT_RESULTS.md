# Weighted three-input slow onset and a descending positive plateau

Date: 2026-09-18. These are internally proved and independently reviewed
study results, not promoted book material. The complete proofs are in
`start_classification.md`, `start_hitting_classification.md`,
`architectural_loss_floor.md`, and `plateau_construction.md`. This synthesis
uses only those frozen proofs and the canonical established sources listed
in the README. No experiment is a premise.

The later terminal continuation is summarized in
`PLATEAU_CLASSIFICATION.md`. It adds finite-state saddle and upper-parameter
escape theorems, while leaving the compatible-data initialized plateau
question open. The slow-onset classification below is unchanged.

## 1. Exact scope and the meaning of slow start

Use the canonical full p=1 population closure in dimension three, with
phi=tanh, x_i in sqrt(3) S^2, labels y_i in {+1,-1}, positive probabilities
p_i summing to one, and

\[
 L(t)=\sum_{i=1}^3p_i(f_t(x_i)-y_i)^2.
\]

The fixed dictionaries, joint initialization correlations, ridge
eta=1/4096, and physical gradient metric are unchanged. The prescribed
initial state is w=g, c=0, M=D. The complete matrix evolves and its actual
transpose is used. The exact odd parity representation has b_1 in R^6,
b_2 in R^3, w in R^3, and M in R^(3x6). All three trainable blocks remain
active. Expectations below are population expectations.

In particular, with

\[
 a_t(x)=E_1[b_1\phi(w_t\cdot x/\sqrt3)],\qquad
 H_t(x)=\phi(b_2^TM_ta_t(x)),\qquad f_t(x)=E_2[c_tH_t(x)],
\]

the full flow is the gradient flow of the unhalved L in the population
L2/L2/Frobenius metric. It has L(0)=1 and the established full energy
identity. The results concern this closure, not a finite neural network.

An asymptotic assertion needs a family of datasets, indexed by n. Define
**slow onset** by

\[
 \sup_{0\le t\le T}|L_n(t)-1|\longrightarrow0
 \quad\text{for every fixed }T<\infty.                 \tag{1}
\]

This means every fixed amount of learning is postponed to arbitrarily
large physical time. It is stronger than delay to just one specified deep
loss threshold. Actual datasets can be required to have distinct or
linearly independent inputs. Coincidences, antipodes, and zero masses must
still be retained in their limits.

## 2. Complete necessary-and-sufficient classification

For the listed three slots define the explicit defect

\[
 \Delta(p,x,y)=\min_{k=1,2,3}\left\{
 |p_k-\tfrac12|+
 \frac13\sum_{j\ne k}p_j\|y_jx_j+y_kx_k\|^2\right\}.    \tag{2}
\]

It is a defect of the listed configuration, not an intrinsic distance on
probability laws after merging repeated slots. Its zero set and its
convergence-to-zero criterion are independent of that representation.

**Theorem.** For every sequence of weighted three-input configurations,
the following are equivalent:

1. Delta_n tends to zero.
2. -L_n'(0) tends to zero.
3. Slow onset (1) holds.
4. For every fixed delta in (0,1),
   inf{t:L_n(t)<=1-delta} tends to infinity.

An unattained threshold has hitting time infinity. There is no claim that
any threshold is eventually reached at each member of a slow family.

The exact zero set has a simple description: after removing zero-weight
slots and reindexing, one slot has weight 1/2, and every other active slot
has the opposite **label-adjusted** direction:

\[
 p_k=\tfrac12,\qquad y_jx_j=-y_kx_k
 \quad(j\ne k,\ p_j>0).                                \tag{3}
\]

With three positive weights, the other two add to 1/2. With only two
positive limiting weights, both are 1/2 and the inactive input is
unrestricted. A one-atom limit never gives slow onset. A sequence need
not have a single limiting direction or a single distinguished index;
formula (2) covers oscillation between cancellation configurations.

Equivalently, the probability law of y_i x_i becomes invariant under
sign reversal in the limit. For at most three atoms, that invariance can
only occur on one antipodal axis. Equation (3) is the complete limiting
class, rather than a selection of examples from it.

### Important special cases

If every weight stays a fixed positive distance from 1/2, geometry alone
cannot produce slow onset.
In particular, equal weights 1/3 have a uniformly positive initial slope
over all input arrangements and all binary labels. There is a uniformly
positive small loss reduction by a common short time. This is a local
progress result, not a uniform all-time fitting theorem.

With exactly balanced label mass, slow onset has an even simpler form:

\[
 \sum_{i<j}p_{i,n}p_{j,n}\|x_{i,n}-x_{j,n}\|^2
       \longrightarrow0.                                \tag{4}
\]

Thus every input carrying nonvanishing weight must coalesce with the
others. If all weights stay bounded below, all three pairwise distances
must tend to zero. An input whose weight vanishes may stay elsewhere.
The same characterization holds under asymptotically vanishing label
imbalance. Without balance, use (2), since same-label antipodes can also
cancel. Opposite-label antipodes reinforce the initialized signal.

### Why the classification concerns the full nonlinear features

The canonical Gaussian calculation gives

\[
 Da_0(x)=
 \bigl(T(x^{(1)}/\sqrt3),T(x^{(2)}/\sqrt3),
       T(x^{(3)}/\sqrt3)\bigr),                           \tag{5}
\]

where superscripts denote spatial coordinates. The initialization proof,
including its reverse correlation and ridge terms, shows that T is odd
and strictly increasing on [-1,1]. It follows that the initialized
coefficient is nonzero on the sphere and distinguishes all inputs,
including modulo sign.

Here is the additional independence argument. The upper mark law has
positive density on an open cube about zero. For q<=3 distinct inputs
modulo sign, choose a vector whose inner products t_i with the q
initialized coefficients are nonzero and have distinct squares. An
identity sum_i A_i phi(b_2 dot Da_0(x_i))=0 would restrict on a short
line to sum_i A_i phi(s t_i)=0. The nonzero linear, cubic, and quintic
coefficients of tanh give

\[
 \sum_i A_i t_i^{2m+1}=0,\qquad 0\le m<q.
\]

This Vandermonde system is invertible. Therefore the only initialized
feature dependencies are those forced by coincident or antipodal inputs.
Since c_0=0, the exact full initialization gives

\[
 -L'(0)=4\left\|\sum_i p_i y_iH_0(x_i)\right\|_2^2.      \tag{6}
\]

At initialization, the lower and matrix velocities vanish. Their
subsequent evolution remains part of the full flow. Equation (6), feature
independence, and positivity of the weights prove (3).
Continuity on the compact simplex times three spheres gives the
equivalence of (2) and vanishing slope for arbitrary sequences.

To extend beyond the initial derivative, the complete vector field is
uniformly Lipschitz in the population Hilbert metric on every common
finite-time state region. This follows from bounded dictionaries, bounded
derivatives of phi, c_infinity<=2T, and ||M||<=||D||+2T^2. The unbounded
Gaussian g stays inside bounded gates; no supremum-norm continuity in
the input direction is assumed. If C_T is a common Lipschitz constant,
the full energy identity and the integral speed estimate give

\[
 0\le1-L(t)\le[-L'(0)]\frac{e^{2C_Tt}-1}{2C_T}
       \quad(0\le t\le T).                              \tag{7}
\]

Conversely, for a common small t_0>0,

\[
 1-L(t_0)\ge\tfrac14t_0[-L'(0)].                         \tag{8}
\]

These estimates prove the finite-horizon equivalence using all moving
blocks. The full raw state displacement also tends to zero on each fixed
horizon, by path energy. The hitting-time equivalence then follows from
loss monotonicity. Complete regularity details and an additional inverse
distance lower bound on the delay are in `start_hitting_classification.md`.

## 3. Why one chosen threshold has a different classification

Fix any desired drop delta in (0,1). Choose
0<kappa<min(1/2,delta/(1+delta)) and the limiting law

\[
 (p_1,p_2,p_3)=(1/2,1/2-\kappa,\kappa),\quad
 (y_1,y_2,y_3)=(+1,-1,-1),\quad
 (x_1,x_2,x_3)=\sqrt3(e_1,e_1,e_2).
\]

It is balanced. Completing the square gives the unavoidable floor

\[
 L\ge1-\frac{\kappa}{1-\kappa}>1-\delta,
\]

whereas its initial slope has strictly positive magnitude
4 kappa^2 ||H_0(sqrt(3)e_1)-H_0(sqrt(3)e_2)||_2^2.
Replace x_2 by sqrt(3)(e_1+epsilon e_3)/sqrt(1+epsilon^2).
For epsilon>0 the three inputs are independent and architecturally
realizable. Finite-time data continuity shows that the time to reach
1-delta tends to infinity as epsilon tends to zero, although the initial
slope tends to that strictly positive number. No eventual attainment
claim is needed. This prevents treating delay to one deeper target as
equivalent to delayed onset of all learning.

## 4. A balanced three-distinct-input trajectory with a positive plateau

Choose

\[
 \begin{array}{c|c|c}
 x_i&y_i&p_i\\\hline
 \sqrt3e_1&+1&1/4\\
 -\sqrt3e_1&+1&1/4\\
 \sqrt3e_2&-1&1/2
 \end{array}                                           \tag{9}
\]

The canonical initialized full flow satisfies

\[
 L(0)=1,\quad L'(0)=-k<0,\quad
 0<L(t)-\tfrac12\le\tfrac12e^{-2kt},\quad
 \lim_{t\to\infty}L(t)=\tfrac12,                        \tag{10}
\]

where k=E_2[H_0(sqrt(3)e_2)^2]>0 is a fixed exact initialization
expectation. Loss decreases strictly at every finite time. Both w and M
move at every positive finite time, and the complete state has a bounded
endpoint. More precisely, for some A,kappa_*>0,

\[
 L(t)=\tfrac12+A e^{-2\kappa_*t}(1+o(1)).                \tag{11}
\]

The inputs are distinct, and their directions span a plane. The positive
floor is architectural: every predictor is odd, so equally labelled
antipodes cannot both be fitted. This is a descending positive plateau,
not optimization failure on realizable data. Its excess above the floor
actually decays exponentially.

### Proof of the actual limit, beyond an architectural lower bound

Oddness yields, with F=-f(sqrt(3)e_2),

\[
 L=\tfrac12+\tfrac12 f(\sqrt3e_1)^2+\tfrac12(1-F)^2.
\]

Reflection in coordinate one preserves the canonical initialization and
data law. Equivariance and uniqueness force f(sqrt(3)e_1)=0 throughout
the trajectory. The complete physical flow is therefore
theta_t=(1-F) grad F, where theta=(w,c,M) with the original metric.

For the full ascent equation theta_s=grad F, put C=E_2[c^2]. Direct
differentiation and Cauchy--Schwarz give

\[
 F_s=\|\nabla F\|^2\ge F^2/C,\qquad C_s=2F,
 \qquad (F^2/C)_s\ge0,\qquad
 \lim_{s\downarrow0}F^2/C=k.
\]

Finite-clock polynomial bounds on c, M, and w-g ensure existence until
F reaches one, which occurs at a finite s_*<=1/k. The physical clock
s'=1-F approaches s_* as t tends to infinity. Consequently

\[
 (L-\tfrac12)'=-2\|\nabla F\|^2(L-\tfrac12)
              \le-2k(L-\tfrac12).
\]

This proves the endpoint value and strict descent in (10). Smoothness at
the bounded endpoint gives (11). `plateau_construction.md` also verifies
nonzero velocities of both hidden blocks and every continuation and
clock obligation. No evolved-feature lower bound is left as a premise.

## 5. All architectural obstructions, and what remains unresolved

There is an exact formula for the best possible loss of every weighted
three-input dataset. Group the active inputs modulo sign; choose one
representative v_G per group and write x_i=sigma_i v_G. Put

\[
 W_G=\sum_{i\in G}p_i,\qquad
 m_G=W_G^{-1}\sum_{i\in G}p_i\sigma_i y_i.
\]

Then for every state

\[
 L(S)=L_{\rm odd}+\sum_G W_G(f_S(v_G)-m_G)^2,\qquad
 L_{\rm odd}=\sum_G W_G(1-m_G^2).                        \tag{12}
\]

The initialized feature independence used above proves that all m_G
can be attained simultaneously by a bounded readout, already with
w=g and M=D. Thus L_odd is the exact attained architectural minimum,
not merely a lower bound. Coincident inputs need equal labels and
antipodal inputs need opposite labels for L_odd=0. With no coincidences
or antipodes, every three-input law is realizable, even if the input
vectors are linearly dependent.

Moreover L'(0)=0 iff L_odd=1. Hence a stationary initialization has no
available improvement anywhere in this odd architecture. Every dataset
whose architectural minimum is below one begins learning strictly.
Equation (9) instead has L_odd=1/2 and reaches it dynamically.

These results completely classify asymptotically delayed onset and the
architectural obstruction, and establish a strictly descending initialized
positive plateau. They do not classify every eventual hitting time or
prove that every initialized trajectory reaches L_odd. A positive limiting
loss above L_odd on compatible three-input data has neither been
constructed nor ruled out. The missing dynamical estimate is global
protection of residual-relevant prediction gradients, or another argument
excluding degeneration and escape along the prescribed trajectory. Static
expressivity and strict initial descent alone do not provide that estimate.

## Verification

`review_weighted_start.md` independently audits both complete onset
proofs, their full-flow extensions, degeneracies, and threshold
counterexamples. `review_weighted_plateau.md` independently audits the
complete plateau proof and architectural minimum, including the exact
Gaussian initialization and all trained blocks. These are internal
mathematical reviews; no promotion, numerical evidence, or external
trajectory assumption is part of the result.
