# Gaussian response energy for growing causal programs

2026-10-06. Scoped theoretical continuation of the unseen-query study.
Internal results; no promotion and no experiments.

The new positive result is an exact root-width estimate for empirical
Gaussian integration-by-parts errors in the energy in which they act on
the response fields. It has no least-eigenvalue denominator. The estimate
continues to hold for functions depending on all coordinate samples, with
an explicit aggregate derivative-energy term. A radius-weighted analytic
jet estimate controls all Taylor orders together. A separate localization
argument works directly in the original dense Gaussian roots, and one
complete reverse/forward reuse is identified against smooth scalar tests
at root width. The first additional covariance loop is also controlled
using only first derivatives. These results remove specific inverse-Gram,
localization, and high-order losses. They do not yet identify the original
trained network with the growing population program.

## Scope and inputs

The target retains fixed hidden depth $L\ge2$, spanning unit inputs
$v_a=x_a/\sqrt d\in S^{d-1}$, $m\ge d$, correlated data, mean squared
loss, mobilities $(n,1,\ldots,1,n)$, independent Gaussian first weights
and hidden mixers, and exactly zero stored readout. The activation
functions are analytic on a common strip with bounded first derivative;
their values may be unbounded. The labels and positive initial training
feature-Gram gap retain the source allowance. The requested error is

\[
 n^{-1/2}\exp\{C\sqrt{\log(en)}\}\log(en)^C
\]

uniformly in physical time, including the fitted endpoint, and over the
whole input sphere. The query is supplied only after compilation. An
absolute power of $\log n$ must bound both retained state and peak live
decoding workspace. Dense oracles, free function-valued state, playback
of a future trajectory, and replacement by frozen-feature dynamics are
not allowed. The results below do not alter this contract.

Read completely: current-study `POPULATION_DECODER.md`; the explicitly
authorized `integrated_general_compression_20261004/GENERAL_DENSE_COMPARISON.md`
and `GENERAL_TRAJECTORY_LOWER_BRIDGE.md`; maintained `docs/notation.qmd`.
Read complete relevant maintained sections of `docs/02-gaussian-reuse.qmd`:
5.4--5.6, 5.9, Q4, Q6, and G.5. Their roles are stated where used below.
No other study artifact, linked source, archived book passage, source
history, or numerical experiment was consulted.

Process reads: `investigate-conjectures` and its research-contract,
evidence-ledger, and adversarial-audit references; `solve-math-rigorously`.
The required canonical-notation skill at
`/home/amir/.codex/skills/explain-with-canonical-notation/SKILL.md`
returned `Permission denied`; its linked neural-network reference was
therefore unavailable. The supplied notation instructions and maintained
notation contract were applied directly. The supervisor's selected input
scope replaces ordinary author startup.

## 1. The covariance error needed by a smooth scalar observable

Let $Q_0,Q_1$ be positive-semidefinite $r\times r$ matrices and let
$g:\mathbb R^r\to\mathbb R$ be $C^2$. Suppose its derivatives through
order two have polynomial growth. Set
$Q_s=(1-s)Q_0+sQ_1$ and $X_s\sim N(0,Q_s)$. Then

\[
 \mathbb E g(X_1)-\mathbb E g(X_0)
 =\frac12\int_0^1\sum_{a,b}(Q_1-Q_0)_{ab}
                    \mathbb E\partial_{ab}g(X_s)\,ds.       \tag{1}
\]

Here and below singular Gaussian laws are permitted. To prove (1), first
replace both endpoint covariances by $Q_j+\varepsilon I$. Differentiate
the Gaussian density along the covariance segment. Its derivative is
one half of the covariance increment contracted with the density's
second spatial derivative. Two integrations by parts give (1) for
$\varepsilon>0$. Gaussian moments are uniformly bounded on this compact
covariance segment. Polynomial domination and the representation
$X_{s,\varepsilon}=X_s+\sqrt\varepsilon Z$, with independent standard
Gaussian $Z$, permit dominated convergence as $\varepsilon\downarrow0$.

Thus, if all the displayed expected second derivatives have absolute
value at most $B$,

\[
 |\mathbb E g(X_1)-\mathbb E g(X_0)|
 \le\frac B2\sum_{a,b}|(Q_1-Q_0)_{ab}|.                    \tag{2}
\]

The scalar weak error is linear in the covariance error even at a zero
eigenvalue. The example $Q_0=0$, $Q_1=\varepsilon$ does force a
$\sqrt\varepsilon$ error for a Gaussian-coordinate $L^2$ coupling,
but it does not force that error for the smooth expectation in (2).
For unbounded activations the polynomial domination hypothesis, or
another explicitly proved integrable domination, remains necessary.

## 2. Exact Stein-error energy, including adaptive sample functions

Let $Z_1,\ldots,Z_n$ be independent standard Gaussian vectors in
$\mathbb R^r$. An independent auxiliary root is allowed. Let
$g_i=g_i(Z_1,\ldots,Z_n)$ be real smooth scalar functions. Initially
assume polynomial bounds on the functions and derivatives needed for
the following integrations by parts. The conclusions extend to the
corresponding Gaussian first-order Sobolev class by smooth
approximation whenever the right sides are finite.

Write $D_jg_i=\nabla_{Z_j}g_i\in\mathbb R^r$ and define

\[
 e=\frac1n\sum_{i=1}^n[Z_i g_i-D_i g_i]\in\mathbb R^r.       \tag{3}
\]

Then $\mathbb E e=0$ and the exact identity is

\[
 \mathbb E\|e\|_2^2
 =\frac1{n^2}\left[
      r\sum_i\mathbb E g_i^2
      +\sum_{i,j}\mathbb E\langle D_jg_i,D_i g_j\rangle
                  \right].                              \tag{4}
\]

In particular,

\[
 \mathbb E\|e\|_2^2
 \le\frac1{n^2}\left[
      r\sum_i\mathbb E g_i^2
      +\sum_{i,j}\mathbb E\|D_jg_i\|_2^2\right].           \tag{5}
\]

For completeness, index a Gaussian coordinate by $p=(i,a)$ and set
$\delta_p(u)=Z_{ia}u-\partial_{ia}u$. One-dimensional integration
by parts says $\mathbb E[\delta_p(u)v]=\mathbb E[u\partial_pv]$.
Differentiating $\delta_q(v)$ and applying the same identity a second
time gives

\[
 \mathbb E[\delta_p(u)\delta_q(v)]
 =\mathbf1_{p=q}\mathbb E[uv]
   +\mathbb E[(\partial_q u)(\partial_p v)].               \tag{6}
\]

Apply (6) with $u=g_i$, $v=g_j$, and sum over $i,j$ and the common
output coordinate $a$. This proves (4). The inequality
$2\langle a,b\rangle\le\|a\|_2^2+\|b\|_2^2$, with the
indices exchanged in one sum, proves (5). No conditional independence
of the $g_i$ has been used.

For iid coordinate functions $g_i=g(Z_i,U_i)$, with iid independent
auxiliary roots $U_i$, all off-diagonal derivatives vanish. Hence

\[
 \mathbb E\|e\|_2^2
 =\frac1n\left[r\mathbb E g^2+
                         \mathbb E\|\nabla_Zg\|_2^2\right].\tag{7}
\]

More generally, the adaptive functions have the same root-width scale
whenever

\[
 \frac1n\sum_i\mathbb E g_i^2\le M_0^2,
 \qquad
 \frac1n\sum_{i,j}\mathbb E\|D_jg_i\|_2^2\le M_1^2.       \tag{8}
\]

The bound is then $(rM_0^2+M_1^2)/n$. This replaces the repeated
high-moment induction for this particular source error by one aggregate
first-derivative energy. It is not a bound on arbitrary matrix-call
errors without the representation (3).

## 3. Correlated sources and why the inverse disappears in output energy

Let $Q\succeq0$ have rank $r$, and factor
$Q=BB^T$ with $B$ having $r$ linearly independent columns. Put
$X_i=BZ_i$. If $g_i$ is written in the $X$ coordinates, its total
gradient obeys $D_i g_i=B^T\nabla_{X_i}g_i$. The correlated defect is

\[
 e_Q=\frac1n\sum_i[X_i g_i-Q\nabla_{X_i}g_i]=Be.           \tag{9}
\]

The identity $B^TQ^\dagger B=I_r$ gives

\[
 e_Q^TQ^\dagger e_Q=\|e\|_2^2.                           \tag{10}
\]

In the iid case, (7) therefore becomes

\[
 \mathbb E[e_Q^TQ^\dagger e_Q]
 =\frac1n\left[
   \operatorname{rank}(Q)\mathbb E g^2+
   \mathbb E(\nabla_Xg)^TQ\nabla_Xg\right].                \tag{11}
\]

This identity has no hidden dependence on the positive eigenvalues of
$Q$. The zero-rank case has identically zero defect.

Its relevance to the maintained inverse-free DAG is direct. Section 5.6
of `docs/02-gaussian-reuse.qmd` cancels response terms by exact
Gaussian integration by parts. Before cancellation, a response
coefficient error has the form $Q^\dagger e_Q$. If the response fields
$C_1,\ldots,C_q$ have second-moment Gram $Q$, then their resulting
population-field error has squared norm

\[
 \left\|\sum_j (Q^\dagger e_Q)_j C_j\right\|_{L^2}^2
 =e_Q^TQ^\dagger e_Q.                                    \tag{12}
\]

Equation (11) bounds precisely (12). Bounding the coefficient vector
alone would discard this compensation and introduce a false
least-eigenvalue cost. This proves a source estimate for the ideal
Gaussian marks, including the adaptive extension in (5); it does not
declare the raw network's conditional history to be such a Gaussian
array.

## 4. Ridge reconstruction in the same energy

Let $\mathcal C:\mathbb R^q\to\mathcal H$ be a linear map into a
real Hilbert space with $\mathcal C^*\mathcal C=Q\succeq0$. Let
$\rho\in\mathbb R^q$, $e_Q\in\operatorname{range}(Q)$, and
$\tau>0$. Reconstruct from the perturbed response moment by

\[
 \widehat U=\mathcal C(Q+\tau I)^{-1}(Q\rho+e_Q),
 \qquad U=\mathcal C\rho.
\]

Then, pathwise,

\[
 \|\widehat U-U\|_{\mathcal H}
 \le\frac{\sqrt\tau}{2}\|\rho\|_2+
                         \sqrt{e_Q^TQ^\dagger e_Q}.       \tag{13}
\]

Indeed the bias is $-\tau\mathcal C(Q+\tau I)^{-1}\rho$.
Diagonalize $Q$. In an eigendirection of eigenvalue $\mu\ge0$ its
squared multiplier is
$\mu\tau^2/(\mu+\tau)^2\le\tau/4$. For the noise term the squared
multiplier is $\mu/(\mu+\tau)^2\le1/\mu$ when $\mu>0$;
the zero eigenspace contributes zero. The triangle inequality proves
(13). If $Q$ is the empirical Gram of finite columns, the same
algebra holds with their output norm written explicitly as Euclidean
norm divided by $\sqrt n$.

Consequently, for the defect in (9), decreasing the ridge below
$n^{-1}$ need not amplify the stochastic output error. With a
polylogarithmic response-coefficient bound, $\tau=n^{-A}$ for a fixed
$A>1$ makes the ridge bias smaller than root width. The storage needed
for the scalar ridge value does not depend on $\tau^{-1}$, under the
ordinary counted-scalar convention; this does not authorize packing
unrelated information into that scalar.

There is a specific limitation: (11) uses the deterministic source
covariance $Q$, whereas the raw conditioning identity uses the random
empirical Gram. Substituting one for the other in (12) is an additional
step. The algebraic estimate (13) does not prove that substitution.

## 5. Empirical feedback and the frozen-coefficient derivative

The population DAG differentiates its coordinate functions while
holding covariance and response coefficients fixed. The following
identity quantifies the correction when these coefficients are empirical.

Let $c=c(Z_1,\ldots,Z_n)\in\mathbb R^p$ be smooth and put
$g_i=\psi(Z_i,c)$. Write

\[
 a_i=\nabla_z\psi(Z_i,c),\quad
 b_i=\nabla_c\psi(Z_i,c),\quad
 S=\sum_j\|D_jc\|_F^2,\quad
 T=\frac1n\sum_i\|b_i\|_2^2.
\]

All these quantities are evaluated on the same sample. The own-row
derivative is $D_i g_i=a_i+(D_i c)^Tb_i$. Therefore the error obtained
using the frozen-coefficient derivative is

\[
 e_{\rm frozen}:=\frac1n\sum_i[Z_i g_i-a_i]
 =e+\frac1n\sum_i(D_i c)^Tb_i.                            \tag{14}
\]

Cauchy--Schwarz gives

\[
 \left\|e_{\rm frozen}-e\right\|_2^2\le\frac{ST}{n}.       \tag{15}
\]

Moreover, $D_jg_i=\mathbf1_{i=j}a_i+(D_jc)^Tb_i$ implies

\[
 \sum_{i,j}\|D_jg_i\|_2^2
 \le2\sum_i\|a_i\|_2^2+2nST.                             \tag{16}
\]

If $n^{-1}\sum_i\mathbb E g_i^2\le M_0^2$,
$n^{-1}\sum_i\mathbb E\|a_i\|_2^2\le M_1^2$, and
$\mathbb E[ST]\le A^2/n$, then (5), (15), and (16) prove

\[
 \|e_{\rm frozen}\|_{L^2}
 \le\sqrt{\frac{rM_0^2+2M_1^2}{n}+\frac{2A^2}{n^2}}
                   +\frac A n.                          \tag{17}
\]

Thus a normally scaled empirical coefficient response contributes an
order-$n^{-1}$ correction to the frozen-coefficient Stein identity.
Neither independence of $c$ from the rows nor an inverse-Gram bound was
used. The displayed derivative-energy hypotheses must still be verified
for the actual coefficient construction.

They cannot be omitted merely because the functions are bounded and
analytic. For $r=1$, set $S_n=\sum_i Z_i$ and
$g_i=\sin S_n$ for every $i$. Then

\[
 e=\frac{S_n\sin S_n}{n}-\cos S_n,
 \qquad
 \mathbb E e^2=\frac{1-e^{-2n}}{2n}+\frac{1+e^{-2n}}2.
                                                               \tag{18}
\]

This follows from (4), since every $D_jg_i=\cos S_n$ and
$S_n\sim N(0,n)$. The variance tends to $1/2$. The example refutes
root-width Stein-error control for unrestricted adaptive coordinate
rules with only value and local activation bounds. It is not asserted
to be a trajectory of the original network.

## 6. One analytic energy bound controls all temporal jet orders

The high-order estimate can be stated directly in a Hilbert space,
which avoids repeated derivative moment estimates. Suppose
$g_i(t,Z)$ is holomorphic in $|t|<r_0$ as a function with values in
Gaussian first-order Sobolev space. Choose $0<r<r_0$. To distinguish
source dimension from the time radius, let $q$ denote the Gaussian root
dimension in this paragraph. Assume the finite boundary energy

\[
 B_r^2=\frac1{2\pi}\int_0^{2\pi}
 \left[
  \frac qn\sum_i\mathbb E|g_i(re^{i\theta})|^2
  +\frac1n\sum_{i,j}\mathbb E\|D_jg_i(re^{i\theta})\|_2^2
 \right]d\theta<\infty.                                  \tag{19}
\]

Write $g_i(t)=\sum_{k\ge0}g_i[k]t^k$, and let $e[k]$ be (3)
formed from the coefficient functions $g_i[k]$. For complex-valued
functions, the proof of (5) applies with conjugates and real parts and
has the same upper bound. Hilbert-space Parseval and (5) give

\[
 \sum_{k\ge0}r^{2k}\mathbb E\|e[k]\|_2^2\le\frac{B_r^2}{n}.
                                                               \tag{20}
\]

To verify Parseval here, on any smaller circle first use the uniformly
convergent Hilbert-valued power series. Orthogonality of
$e^{ik\theta}$ eliminates all different-order cross terms in the
integrated squared norm. Increase the smaller radius to $r$ and use
monotone convergence of the nonnegative coefficient series, or use
the assumed Hilbert-space continuity on the circle at $r<r_0$.

For $0<h<r$, let $\vartheta=h/r$. At every degree $K$,

\[
 \left\|\sup_{|t|\le h}
       \left\|\sum_{k=0}^Ke[k]t^k\right\|_2\right\|_{L^2}
 \le\sum_{k=0}^Kh^k\|e[k]\|_{L^2}
 \le\frac{B_r}{\sqrt{n(1-\vartheta^2)}}.                  \tag{21}
\]

The first inequality is the pointwise triangle inequality followed by
Minkowski. The second is Cauchy--Schwarz against the geometric weights
$\vartheta^k$, followed by (20). The tail after degree $K$ has the
same bound multiplied by $\vartheta^{K+1}$. Thus growing Taylor degree
does not itself cause an exponential constant in this source estimate.

For $H$ patches, one may combine their squared boundary energies and
use $\mathbb E\max_j X_j^2\le\sum_j\mathbb E X_j^2$.
If their boundary energies are bounded by $B$, the patch-uniform
bound costs at most $\sqrt H B/\sqrt{n(1-\vartheta^2)}$.
Any polylogarithmic number of patches remains compatible with the
requested root-width scale. Gaussian tail estimates or a sphere net
are not supplied by this $L^2$ statement alone.

The current source proves complex-time bounds for values of selected
network curves. It does not, in the authorized inputs, prove (19) for
all the coordinate and response functions of a growing population DAG.
Equation (19) is a sharply identified new sufficient estimate, not an
extra hypothesis appended to the requested theorem.

## 7. Adaptive finite-rank projection errors already have the right scale

For a fresh $g\sim N(0,I_n)$ and any past-measurable orthogonal
projector $P$ of rank at most $R$,

\[
 \mathbb E[\|Pg\|_2^2/n\mid\text{past}]
 =\operatorname{tr}(P)/n\le R/n.                          \tag{22}
\]

This elementary estimate never uses the conditioning of a chosen basis
for the range of $P$. Section 5.9 of the maintained chapter uses stronger
coordinate moments and coefficientwise inverse estimates for its fixed
program proof; (22) shows why those inverse constants should not be
treated as intrinsic to RMS projection error.

The maintained adaptive Gram result Q4 goes further. It bounds the
original/replacement triangular perturbations using regularized
effective ranks, and its constants do not contain an inverse ridge.
For a transcript with at most $R$ calls, both effective ranks are at
most $R$ without a temporal-rank theorem. Its displayed martingale
bound is therefore a root-width bound multiplied by powers of $R$ and
logarithms when the physical input and output query norms are bounded.
That result is genuinely adaptive: its predictable half-step reveal
order is part of the proof. It does not assert iid coordinate laws for
the resulting full transcript. G.5 explicitly separates a conditionally
Gaussian innovation from its history-dependent mean.

## 8. What has changed and the remaining transfer

| Statement | Status |
|---|---|
| Smooth Gaussian scalar weak error is linear in covariance perturbation at singular covariance | Proved in (1)--(2) |
| Gaussian response-cancellation defect has inverse-free output energy | Proved in (3)--(12), including adaptive coordinate functions |
| Ridge bias can be reduced without amplifying that output-energy noise | Proved in (13) |
| Empirical coefficient feedback has an explicit own-row correction | Proved in (14)--(17) |
| Bounded analytic values alone control arbitrary adaptive Stein defects | Falsified by (18); no original-network counterexample claimed |
| One analytic aggregate response-energy bound controls all jet orders | Proved conditionally on the explicit analytic Sobolev premise (19) |
| Good-event scalar matrix-divergence and all-degree temporal-jet errors | Proved in Sections 10--11 under explicit amplitude and pairwise Lipschitz premises |
| One reverse/forward reuse has the response-corrected smooth-test Gaussian law | Proved in Section 12 with an explicit high-probability event |
| The first centered matrix-square covariance loop is root-width small | Proved in Section 14 under explicit coordinate bounds |
| The actual growing Gaussian transcript satisfies that premise and the same covariance-energy comparison | Open |
| Accurate autonomous late-query decoder with absolute-polylogarithmic peak workspace | Open; neither proved nor refuted |

The needed transfer is now more specific than a generic
small-eigenvalue lemma. The actual adaptive conditional law must be
compared in the response-field energy, while retaining both orientations
of each initial matrix. Its empirical covariance and coefficient
dependence must yield the aggregate derivative budget in (8)/(19), or
an equivalent causal martingale budget. A valid proof must also control
the difference between the actual empirical Gram and the source
covariance in that same energy. The fixed-program spectral stopping
argument does not provide these growing-program estimates.

The new formulas do not increase the retained matrix list: a program
with $R$ scalar Gaussian-source coordinates stores $O(R^2)$ covariances
and responses. Computing a first derivative or a Hessian contraction of
a scalar evaluator can retain its $O(R)$ directional array, or an
$O(R^2)$ full derivative array, and stream the Gaussian quadrature.
This is a conditional workspace observation, not a claim that all the
needed integrals, error tolerances, dynamics, and autonomous continuation
have already been constructed. In particular no Gaussian source has
been allowed to retain a dense initialization for free.

These results refine the missing width bridge recorded in
`POPULATION_DECODER.md`. They do not supersede its open status. The
supervisor requested a focus on scalar weak error rather than
coordinatewise square-root coupling; the proofs above were then
developed in this scoped continuation. Subsequent supervisory feedback
emphasized cumulative adaptive error and peak workspace; Sections 5--6
and the preceding workspace statement address that feedback. A further
supervisory proposal to use dense-root flow sensitivities motivated the
additional exact obstruction and localization result below.

The supervisor subsequently relayed the user's explicit clarification:
full training forward/backward histories may not be retained; compressed
temporal summaries are permitted, and peak decoding workspace remains
counted. All memory observations in this note refer to scalar covariance,
response, and radius-weighted jet summaries, not stored width-$n$ fields
or full function-valued histories.

## 9. Dense-root energy is not automatically innovation-root energy

The Gaussian roots in (3) must be the roots used by the corresponding
coordinate program. A bound on derivatives with respect to the original
dense entries cannot be transferred to adaptively chosen innovation
coordinates solely from their common standard Gaussian law.

Here is an exact causal example. Let $X,Y_1,Y_2$ be independent standard
Gaussians. After revealing $X$, choose an angle $\alpha=MX$ and set

\[
 U=\cos\alpha\,Y_1+\sin\alpha\,Y_2,
 \qquad V=-\sin\alpha\,Y_1+\cos\alpha\,Y_2.
                                                               \tag{23}
\]

Conditioned on $X$, this is an orthogonal rotation, so $(X,U,V)$ is
again a triple of independent standard Gaussians. The physical scalar
$Y_1$ has squared gradient norm one in its original roots. In the new
roots it is $g(X,U,V)=\cos(MX)U-\sin(MX)V$, and

\[
 \mathbb E\|\nabla_{X,U,V}g\|_2^2=1+M^2.                 \tag{24}
\]

The two derivatives in $U,V$ contribute one; the derivative in $X$
has variance $M^2$. Thus even a causal Gaussian reparametrization can
have an arbitrarily large Sobolev-energy cost.

Nearly dependent raw directions expose the same mechanism while their
unscaled derivatives remain bounded. For deterministic orthonormal
$e_1,e_2,e_3$, take

\[
 q_1=e_1,\qquad
 q_2=e_1+\varepsilon[
       \cos(X/\varepsilon)e_2+\sin(X/\varepsilon)e_3].     \tag{25}
\]

The derivative of $q_2$ has norm one, but its normalized residual after
projecting out $q_1$ has derivative norm $\varepsilon^{-1}$. The raw
two-column Gram has a small eigenvalue of order $\varepsilon^2$.
Equations (23)--(25) refute an unrestricted argument that transfers
dense-root gradient bounds through adaptive Gram normalization without
a cost. They do not refute a covariance-invariant proof or show that
this configuration is generated by the requested network flow.

## 10. A localized scalar Stein estimate in the original dense roots

The preceding coordinate problem can be avoided for scalar matrix
contractions. Let $M\in\mathbb R^{n\times n}$ have independent standard
Gaussian entries, independent of all other initialization roots. Let
$c,h\in\mathbb R^n$ be smooth functions of all these roots, with the
integrability needed below. They may depend arbitrarily on $M$. Define

\[
 \mathcal E(c,h)=\frac1{n^{3/2}}\sum_{i,j}
     [M_{ij}c_i h_j-\partial_{M_{ij}}(c_i h_j)].           \tag{26}
\]

The first term is exactly $c^T(W_0h)/n$, where $W_0=M/\sqrt n$.
The derivative term retains both orientations:

\[
 \partial_{M_{ij}}(c_i h_j)
 =h_j\partial_{M_{ij}}c_i+c_i\partial_{M_{ij}}h_j.         \tag{27}
\]

Let $D_M$ denote the Jacobian with respect to all entries of this one
matrix. The Gaussian divergence identity (6), now summing over all
matrix entries, proves that $\mathbb E\mathcal E=0$ and

\[
 \mathbb E|\mathcal E(c,h)|^2
 \le\frac1{n^3}\mathbb E\left[
       \|c\|_2^2\|h\|_2^2
             +\|D_M(c\otimes h)\|_{\rm HS}^2\right]
\]
\[
 \le\frac1{n^3}\mathbb E\left[
       \|c\|_2^2\|h\|_2^2
       +2\|h\|_2^2\|D_Mc\|_F^2
       +2\|c\|_2^2\|D_Mh\|_F^2\right].                 \tag{28}
\]

In this display $c\otimes h$ means the finite array with entries
$c_i h_j$; it is an ordinary Euclidean outer product, not a normalized
population weight operator. To check the first inequality, regard this
array as a vector field $u$ on the $n^2$ Gaussian entries. Formula (6)
gives
$\mathbb E|\sum_p\delta_p(u_p)|^2
=\mathbb E\|u\|_2^2+\mathbb E\sum_{p,q}(\partial_q u_p)(\partial_p u_q)$.
The final sum is at most $\mathbb E\|Du\|_F^2$ by the same
index-exchange inequality as in (5). For the second inequality apply
$\|a+b\|_2^2\le2\|a\|_2^2+2\|b\|_2^2$ to
$\partial_p(c\otimes h)=(\partial_pc)\otimes h+
c\otimes(\partial_ph)$ and sum over $p$.

The estimates hold with arbitrary independent external roots by first
conditioning on them. They extend to Gaussian first-order Sobolev
vector fields by smooth approximation: (28) applied to differences
makes the Gaussian divergences converge in $L^2$ whenever the vector
fields converge in Gaussian $H^1$.

Now let $E$ be a measurable set of full initialization roots. Suppose
the original coordinates are locally $C^1$ on an open neighborhood of
$E$, and for every two roots $G,G'\in E$,

\[
 |c_i(G)|,|h_i(G)|\le B,
 \quad
 |c_i(G)-c_i(G')|,|h_i(G)-h_i(G')|
                       \le A\|G-G'\|_2.                 \tag{29}
\]

The full root vector $G$ may have order $n^2$ coordinates. The constants
$A,B$ may depend on width. Extend each scalar coordinate by

\[
 \widetilde c_i(G)=\operatorname{clip}_{[-B,B]}
  \inf_{G'\in E}\{c_i(G')+A\|G-G'\|_2\},                \tag{30}
\]

and use the same formula for $h_i$. If $E$ is empty the desired
good-event assertion is vacuous. Otherwise the infima in (30) are
finite. The triangle inequality proves that each extension is
$A$-Lipschitz; the good-set Lipschitz property proves equality to the
original coordinate on $E$. Clipping preserves the Lipschitz constant
and equality on $E$.

Almost everywhere the extensions satisfy

\[
 \|\widetilde c\|_2^2,\|\widetilde h\|_2^2\le nB^2,
 \qquad
 \|D_M\widetilde c\|_F^2,
 \|D_M\widetilde h\|_F^2\le nA^2.                       \tag{31}
\]

The derivative of an extension agrees with the original derivative
almost everywhere on $E$. One elementary justification is to restrict
their difference to almost every coordinate line. It is locally
absolutely continuous and zero on that line's section of $E$.
At almost every density point of its zero set at which it is
differentiable, its derivative is zero, by taking difference quotients
through zero-set points. Fubini gives equality of all weak derivatives
on $E$ up to a Lebesgue-null, and hence Gaussian-null, set.

Consequently $\mathcal E(\widetilde c,\widetilde h)
=\mathcal E(c,h)$ almost everywhere on $E$. Applying (28), (31),
and Markov's inequality proves, for every $0<\delta<1$,

\[
 \Pr\left(E\cap\left\{
 |\mathcal E(c,h)|>
       \sqrt{\frac{B^4+4B^2A^2}{n\delta}}
                              \right\}\right)\le\delta.\tag{32}
\]

There is no derivative of a sharp good-event indicator in this proof,
and no quantitative bound on $\Pr(E^c)$ is needed for (32). If the
source only gives $\Pr(E^c)=o(1)$, the corresponding full probability
bound is $\delta+o(1)$. The extensions are proof auxiliaries; (32)
concerns the original scalar contraction and its original response
traces on $E$. It does not place an extension oracle in the decoder.

For the proposed application, $A\le\exp(C\sqrt{\log n})\log(n)^C$
and $B\le\log(n)^C$ make (32) exactly a permitted source scale.
A pointwise Jacobian bound on $E$ alone does not prove (29), because
the straight segment joining two points of $E$ need not lie in $E$.
The existing good-pair comparison, or another explicit pairwise
argument, is needed. A global operator-norm bound for a derivative is
not silently substituted for this premise.

## 11. Localizing every time jet without a holomorphic global extension

There is a useful version of (32) for the complete temporal polynomial.
Suppose on the same set $E$ the vector functions $c(t,G),h(t,G)$ are
holomorphic in a neighborhood of $|t|\le r$ and, uniformly on
$|t|=r$, each scalar coordinate has amplitude at most $B$ and
good-pair Lipschitz constant at most $A$ in $G$. Cauchy's coefficient
formula proves that the radius-weighted coefficients

\[
 C_a(G)=r^a c[a](G),\qquad H_b(G)=r^b h[b](G)
\]

have the same amplitude and good-pair Lipschitz bounds. Apply (30)
separately to their real and imaginary parts. Their complex extensions
then have amplitude at most $\sqrt2 B$ and squared gradient norm
at most $2A^2$ per coordinate. These coefficient extensions need not
arise from a single globally holomorphic time function.

Let $\mathcal E_K(t)$ be the degree-$K$ Taylor polynomial of the raw
scalar defect (26). Bilinearity and commutation of root differentiation
with the finite Taylor coefficient extraction give, on $E$,

\[
 \mathcal E_K(t)
   =\sum_{a+b\le K}(t/r)^{a+b}\mathcal E(C_a,H_b).         \tag{33}
\]

Sobolev locality identifies every term with its extended version on
$E$, outside a null set common to the countable coefficient family.
Equation (28), applied to complex vector fields with the Hermitian
norm, gives the conservative bound

\[
 \|\mathcal E(\widetilde C_a,\widetilde H_b)\|_{L^2}
 \le\frac{2\sqrt{B^4+4B^2A^2}}{\sqrt n}.                 \tag{34}
\]

For $0<\vartheta<1$, the pointwise triangle inequality and Minkowski
give

\[
 \left\|\sup_{|t|\le\vartheta r}
  \left|\sum_{a+b\le K}(t/r)^{a+b}
       \mathcal E(\widetilde C_a,\widetilde H_b)\right|
                                                 \right\|_{L^2}
 \le\frac{2\sqrt{B^4+4B^2A^2}}
              {\sqrt n(1-\vartheta)^2}.                 \tag{35}
\]

The only summation is
$\sum_{a,b\ge0}\vartheta^{a+b}=(1-\vartheta)^{-2}$.
Thus (35), and its Markov good-event probability version, are uniform
in $K$. There is no need to take a Gaussian expectation of a source
curve defined only on $E$, no globally holomorphic extension, and no
Taylor-order moment tower for this scalar defect.

For a finite list of patches and matrix contractions, their common
good event can be retained and their squared bounds summed. A
polylogarithmic list only adds a polylogarithmic factor. A sphere net
and a modulus for the relevant raw scalar defects remain separate
requirements for a whole-sphere conclusion.

This establishes a local-to-global source-error lemma in the original
dense Gaussian coordinates. The exact surviving causal gap is the
response trace in (27): the authorized sources do not yet identify
all its growing-order values with the covariance and response
coefficients of the compact scalar DAG, with the same quantitative
error and counted evaluator. Dense-root sensitivities can justify
(29) after the appropriate good-pair and complex-time proof, but
they do not themselves perform that trace-to-DAG identification.
That distinction remains necessary after this new localization result.

## 12. A complete smooth-test closure for one reverse/forward reuse

This example goes beyond a single contraction estimate: it identifies
the empirical law against every separately fixed smooth scalar test.
It also shows exactly which dependency becomes new in a longer program.

Let $a\in\mathbb R^n$ be deterministic, with
$\|a\|_2/\sqrt n\le A$ and $\|a\|_\infty\le A$. Let $M$ be the
standard Gaussian matrix from Section 10 and define the causal calls

\[
 b=M^Ta/\sqrt n,\qquad h_j=\phi(b_j),\qquad y=Mh/\sqrt n.
                                                               \tag{36}
\]

Assume $\phi$ is $C^2$ with $|\phi'|\le a_1$,
$|\phi''|\le a_2$, and at most linear growth. Put

\[
 \rho=\frac1n\sum_j\phi'(b_j),\qquad
 Q=\frac1n\sum_jh_j^2,\qquad \mu_i=a_i\rho.               \tag{37}
\]

Fix functions $F_i:\mathbb R\to\mathbb R$ whose derivatives through
order three are continuous and have the common bounds
$\|F_i^{(k)}\|_\infty\le K_k$, $1\le k\le3$.
The index $i$ may record a deterministic row mark such as $a_i$.
No supremum over all tests is asserted by the probability conclusion.

For deterministic $\mu\in\mathbb R$ and $Q\ge0$, define

\[
 u_i(x;\mu,Q)=-\int_0^\infty\left[
  \mathbb E F_i\big(e^{-s}x+(1-e^{-s})\mu+
                    \sqrt{1-e^{-2s}}\sqrt Q Z\big)
  -\mathbb E F_i(\mu+\sqrt Q Z)\right]ds,
                                                               \tag{38}
\]

where $Z\sim N(0,1)$. The integrand is bounded in absolute value by
$K_1 e^{-s}(|x-\mu|+\mathbb E|\sqrt QZ|)$, by coupling to the
stationary Gaussian with the same $Z$ and using
$1-\sqrt{1-e^{-2s}}\le e^{-s}$. Thus the integral converges.
Differentiation of the Gaussian semigroup, or one integration by parts
in $Z$, gives its generator
$Q\partial_x^2-(x-\mu)\partial_x$. Integrating the derivative in
$s$ of the bracket proves

\[
 Q\psi_{i,x}(x;\mu,Q)-(x-\mu)\psi_i(x;\mu,Q)
 =F_i(x)-\mathbb E F_i(\mu+\sqrt Q Z),\qquad
 \psi_i=\partial_xu_i.                                   \tag{39}
\]

All covariance derivatives below are right derivatives at $Q=0$;
the formulas remain valid there by Gaussian interpolation (1).
Differentiating (38) and integrating the exponential weights gives

\[
 |\psi_i|\le K_1,\quad
 |\psi_{i,x}|\le K_2/2,\quad
 |\psi_{i,\mu}|\le K_2/2,\quad
 |\psi_{i,Q}|\le K_3/3.                                  \tag{40}
\]

For the last bound, the derivative is one half times the integral of
$e^{-s}(1-e^{-2s})\mathbb E F_i'''$, whose weight integrates to
$2/3$. No covariance inverse occurs in (38)--(40).

Set $c_i=\psi_i(y_i;\mu_i,Q)$, using the actual empirical values
in (37). The direct derivatives are

\[
 \partial_{M_{ij}}h_j=\phi'(b_j)a_i/\sqrt n,
 \quad
 \partial_{M_{ij}}y_i=h_j/\sqrt n+
                         a_iM_{ij}\phi'(b_j)/n,
\]
\[
 \partial_{M_{ij}}\rho= a_i\phi''(b_j)/n^{3/2},
 \qquad
 \partial_{M_{ij}}Q=2a_i h_j\phi'(b_j)/n^{3/2}.           \tag{41}
\]

Insert (41) and the chain rule for $c_i$ into (26). The result is the
exact identity

\[
 \frac1n\sum_i\left[
 F_i(y_i)-\mathbb E_ZF_i(\mu_i+\sqrt Q Z)\right]
 =-\mathcal E(c,h)-R_1-R_2-R_3,                           \tag{42}
\]

where all derivatives of $\psi_i$ below are evaluated at
$(y_i;\mu_i,Q)$ and

\[
 R_1=\frac1{n^2}(a\odot\psi_x)^T
                 (M/\sqrt n)(h\odot\phi'(b)),
\]
\[
 R_2=\frac1{n^3}
           \left(\sum_i a_i^2\psi_{i,\mu}\right)
           \left(\sum_j h_j\phi''(b_j)\right),
\quad
 R_3=\frac2{n^3}
           \left(\sum_i a_i\psi_{i,Q}\right)
           \left(\sum_j h_j^2\phi'(b_j)\right).          \tag{43}
\]

To check the leading terms, the derivative of $h_j$ in (27) gives
$n^{-1}\sum_i\mu_i c_i$. The direct $h_j/\sqrt n$ term in
$\partial y_i$ gives $Qn^{-1}\sum_i\psi_{i,x}$. The remaining
part of $\partial y_i$ is $R_1$. Differentiating the empirical mean
and covariance gives $R_2,R_3$. Substituting (39) produces the sign in
(42).

On any event with $\|M/\sqrt n\|_{\rm op}\le M_0$ and
$\|h\|_2/\sqrt n\le H$, (40) gives

\[
 |R_1|+|R_2|+|R_3|
 \le\frac1n\left[
  \frac{K_2 A M_0 a_1H}{2}
  +\frac{K_2 A^2a_2H}{2}
  +\frac{2K_3 A a_1H^2}{3}\right].                       \tag{44}
\]

Every term has an explicit factor $n^{-1}$. No claim of independence
between $y$ and its empirical response coefficients was made.

The random contraction $\mathcal E(c,h)$ has the localized root-width
bound (32). Its premises follow on the same good set if also
$\max_j|h_j|\le B$. Indeed, for two matrices in this set,

\[
 \|b-b'\|_2\le A\|M-M'\|_F,\quad
 \|h-h'\|_2\le a_1A\|M-M'\|_F,
\]
\[
 \|y-y'\|_2\le(H+M_0a_1A)\|M-M'\|_F,
\]
\[
 |\rho-\rho'|\le\frac{a_2A}{\sqrt n}\|M-M'\|_F,
 \quad
 |Q-Q'|\le\frac{2Ha_1A}{\sqrt n}\|M-M'\|_F.             \tag{45}
\]

For the second line subtract $Mh-M'h'$ using $M'$ on the activation
difference and $h$ on the matrix difference. For the last covariance
bound use $|\|h\|_2^2-\|h'\|_2^2|
\le(\|h\|_2+\|h'\|_2)\|h-h'\|_2$.
The derivative bounds (40), the convexity of $Q\ge0$, and (45) give
a scalar Lipschitz bound for every $c_i$ with constant

\[
 A_c=\frac{K_2}{2}(H+M_0a_1A)
       +\frac{K_2a_2 A^2}{2\sqrt n}
       +\frac{2K_3Ha_1A}{3\sqrt n}.                     \tag{46}
\]

Thus (32) applies with common coordinate cap
$\max(B,K_1)$ and Lipschitz constant $\max(a_1A,A_c)$.

Finally, the entries of $b$ are independent $N(0,s^2)$, where
$s^2=\|a\|_2^2/n$. Define

\[
 \rho_* =\mathbb E\phi'(sZ),\qquad
 Q_* =\mathbb E\phi(sZ)^2.
\]

Their empirical errors obey
$\mathbb E|\rho-\rho_*|^2\le a_1^2/n$ and
$\mathbb E|Q-Q_*|^2=\operatorname{Var}(\phi(sZ)^2)/n$.
The latter variance is finite by the linear growth of $\phi$.
The averaged target in (42) changes by at most

\[
 K_1 A|\rho-\rho_*|+\frac{K_2}{2}|Q-Q_*|                 \tag{47}
\]

when replaced by
$n^{-1}\sum_i\mathbb E_ZF_i(a_i\rho_*+\sqrt{Q_*}Z)$.
The mean term follows from the test's Lipschitz bound; the variance
term follows from (1), including when $Q_*=0$. Combining
(32), (44), and (47), with Markov's inequality for the two independent-
column sample errors, proves the root-width smooth-test law on any
such high-probability good set.

Such a set is available here without an additional dynamical
assumption. Take $M_0=8$,
$H^2=1+2|\phi(0)|^2+2a_1^2A^2$, and
$B=|\phi(0)|+a_1A\sqrt{8\log(en)}$. Gaussian tails give
$\Pr(\max_j|b_j|>A\sqrt{8\log(en)})=O(n^{-3})$; the
case $A=0$ is deterministic. The independent-column fourth-moment
bound and Chebyshev give $\Pr(Q>H^2)=O(n^{-1})$ uniformly in
$s\le A$. For the matrix norm, unit-sphere $1/4$-nets with at most
$9^n$ elements follow by disjoint-ball volume comparison. The
bilinear net approximation gives
$\|M/\sqrt n\|_{\rm op}\le2\max_{u,v\ {m in\ the\ nets}}
|u^TMv|/\sqrt n$. Each fixed pairing has tail
$2e^{-nx^2/2}$. A union bound at $x=4$ therefore gives
$\Pr(\|M/\sqrt n\|_{\rm op}>8)
\le2\exp((2\log9-8)n)=o(1)$.
Thus the good set has probability $1-O(n^{-1})$, and the smooth-test
law error in this worked example is $O_\delta(n^{-1/2}\log(en))$.

The result is a causal response-corrected Gaussian law: its mean
$a_i\rho_*$ is the transpose response and its variance $Q_*$ is the
new Gaussian source variance. The physical derivative traces have
been identified with those scalar quantities in this complete
one-reuse case. They were not merely renamed as unknown coefficients.

For the requested growing training program, the earlier reverse query
$a$ depends on the same matrix through earlier forward calls.
Then (41) acquires the derivatives of $a$, and the additional terms
are not all $O(n^{-1})$: some are the nonzero causal responses that
the inverse-free DAG must retain. One must separate these leading
responses from the finite-width feedback remainder across the entire
chronology. Equations (42)--(47) do not perform that separation for a
growing number of mutually dependent calls. This is the precise
remaining law-identification issue exposed by the worked example.

## 13. Whole-sphere extension of the source lemma

The $L^2$ source estimate alone does not permit a union over a
polynomial-in-$n$ sphere net without losing the requested rate.
One sufficient alternative is a complex-query source bound, stated
here conditionally rather than imported from a linked source.

Suppose local real charts of the input sphere extend to complex
polydisks of radius $\rho_n\ge\log(en)^{-C}$ in their $d-1$ chart
coordinates. Suppose the amplitude and good-pair root-Lipschitz
bounds used in Section 11 hold on the distinguished boundaries of
these polydisks, with uniform constants. Multivariable Cauchy
coefficient estimates give the same bounds on every radius-weighted
coefficient. Applying the coefficientwise scalar extensions and
geometric summation to both factors in (26) costs at most
$(1-\vartheta)^{-2(d-1)}$ per spatial patch, in addition to the
temporal factor in (35).

A compact sphere admits $O_d(\rho_n^{-(d-1)})$ such smaller real
patches. Summing the squared bounds across patches costs only
$O_d(\rho_n^{-(d-1)/2})$, which is polylogarithmic at fixed $d$.
The spatial coefficients in this paragraph are proof devices; this
argument does not store them in the decoder. Its use therefore does
not change an absolute exponent in the retained scalar-state count.

The required complex-query good-pair Lipschitz bound is stronger than
the existing real prediction modulus and has not been established
here. Without it, a suitable input-Sobolev estimate or quantitative
high-moment divergence bound is still required for a whole-sphere
source event. This obligation is separate from the temporal uniformity
already established conditionally in Section 11.

## 14. The first covariance loop needs only first-derivative energy

The next reuse introduces a centered matrix-square trace. It too admits
a bound using first derivatives rather than a growing derivative tower.
Let $\alpha,\nu\in\mathbb R^n$ be globally Lipschitz functions of the
full Gaussian root, with each coordinate bounded in absolute value by
$B$ and each scalar coordinate Lipschitz constant at most $A$. Set

\[
 T=\frac1{n^2}\sum_{i,j}(M_{ij}^2-1)\alpha_i\nu_j.        \tag{48}
\]

There is an absolute constant $C$ such that

\[
 \|T\|_{L^2}\le
       \frac{C(B^2+BA)}n+\frac{2BA}{\sqrt n}.             \tag{49}
\]

To prove this, index a matrix entry by $p=(i,j)$ and write
$u_p=\alpha_i\nu_j$. The product rule for Gaussian divergence gives

\[
 (M_p^2-1)u_p=\delta_p(M_pu_p)+M_p\partial_pu_p.           \tag{50}
\]

The explicit derivative remainder in (50) has pointwise absolute value
at most

\[
 \frac{\|M\|_F}{n^2}
       \left(\sum_{i,j}|\partial_{M_{ij}}u_{ij}|^2\right)^{1/2}
 \le\frac{2BA\sqrt n}{n^2}\|M\|_F.                     \tag{51}
\]

Indeed the selected derivatives of $\alpha_i$ and $\nu_j$ are bounded
in squared sum by their full gradient energies, each at most $nA^2$.
Since $\mathbb E\|M\|_F^2=n^2$, (51) has $L^2$ norm at most
$2BA/\sqrt n$.

For the divergence part put $v_p=M_pu_p$. Then
$\mathbb E\|v\|_2^2\le B^4n^2$. The product rule and the elementary
three-term squared-norm inequality bound

\[
 \|Dv\|_F^2\le
  3n^2B^4
  +3B^2\sum_i\left(\sum_jM_{ij}^2\right)\|D\alpha_i\|_2^2
  +3B^2\sum_j\left(\sum_iM_{ij}^2\right)\|D\nu_j\|_2^2.
                                                               \tag{52}
\]

Here the full-root gradients may be used as upper bounds for the
matrix-block gradients. The expected maximum row and column squared
norms are at most $Cn$. One direct verification is
$\mathbb E\exp(\|M_{i,:}\|_2^2/4)=2^{n/2}$; Markov and a
union over the $2n$ rows and columns give an exponential upper tail
beyond a fixed multiple of $n$, whose integral is at most $Cn$.
Using $\sum_i\|D\alpha_i\|_2^2\le nA^2$ and the analogous
bound for $\nu$, (52) therefore has expectation at most
$Cn^2(B^4+B^2A^2)$.
The scalar divergence inequality from (28), applied to $v$, gives
$\|n^{-2}\sum_p\delta_p(v_p)\|_{L^2}
\le C(B^2+BA)/n$. Together with (51), this proves (49).

The same good-set version follows by the scalar extensions (30) and
Sobolev locality. No second derivative of $\alpha$ or $\nu$ was used.

For its causal role, take the next simple chronology with deterministic
$u\in\mathbb R^n$:

\[
 z=Mu/\sqrt n,\quad a=\psi(z),\quad
 b=M^Ta/\sqrt n,\quad h=\phi(b),\quad y=Mh/\sqrt n,
 \qquad \rho=\frac1n\sum_k\phi'(b_k).
                                                               \tag{53}
\]

Writing the response-corrected output as $s_i=y_i-\rho a_i$, exact
differentiation gives

\[
 \partial_{M_{ij}}s_i
 =\frac{h_j}{\sqrt n}
  +\frac{a_iM_{ij}\phi'(b_j)}n
  +\frac{\psi'(z_i)u_j}{\sqrt n}
       \left[\frac1n\sum_k(M_{ik}^2-1)\phi'(b_k)\right]
  -a_i\partial_{M_{ij}}\rho.                              \tag{54}
\]

To check the centered bracket, differentiate
$b_k=n^{-1/2}\sum_lM_{lk}\psi(z_l)$:

\[
 \partial_{M_{ij}}b_k
 =\mathbf1_{k=j}a_i/\sqrt n+
                    M_{ik}\psi'(z_i)u_j/n.
\]

Substitute this into $y_i=n^{-1/2}\sum_kM_{ik}\phi(b_k)$.
The resulting term
$\psi'(z_i)u_j n^{-3/2}\sum_kM_{ik}^2\phi'(b_k)$ loses
$\rho\psi'(z_i)u_j/\sqrt n$ upon differentiating $\rho a_i$,
which gives exactly (54).

In the averaged two-dimensional Stein identity for $(z_i,s_i)$,
the bracket in (54) is paired with a scalar row test weight. Its
normalized contribution is of form (48), with
$\nu_k=\phi'(b_k)$ and the row weight absorbing the test derivative
and $\psi'(z_i)$. Thus (49) controls this first covariance loop at
root width whenever those coordinate fields satisfy the indicated
good-pair bounds. The other terms in (54) retain the direct covariance,
the rank-one feedback term already present in Section 12, and the
empirical coefficient derivative. This identifies a real cancellation
and a bounded remainder for the next reuse; a complete quantitative
induction for arbitrary growing chronology is not asserted.
