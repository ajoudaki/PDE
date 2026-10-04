# A positive aggregate kernel through the first feature-learning correction

2026-09-30. Scoped theoretical construction; no training experiments or code
experiments were run. This is an internally derived, unreviewed result, not
established book material. Inputs were the supervisor's exact P1 model and
Sections 1–2 of `AGGREGATE_SCALAR_CONSTRUCTION.md`. No other candidate route
notes were read.

**Conclusion.** There is a concrete autonomous aggregate ODE with
`m(m−1)/2 + 2m` evolving scalars for training, and at most a further `m^3`
scalars for decoding the whole test function. Its kernel changes during
training, is positive semidefinite, and all its states stop when the training
residual is zero. Under a positive initial training Gram matrix and
sufficiently small label amplitude `a`, it approximates the P1 output,
uniformly for all training times and all inputs in the unit disk, with error
`O(a^5)`. It therefore captures the cubic output correction caused by feature
learning. Its coefficients are initialization contractions, with `O(m^4)`
training coefficient storage. This is **not** a theorem for unit labels or
strong feature movement, and at fixed non-small amplitude it is not an
arbitrary-accuracy hierarchy.

The small-amplitude route was suggested by the supervisor after the exact
lag/Gram decomposition below had been derived independently. It replaces a
much larger generic Lie-response-jet candidate as this note's proposed
construction.

## 1. Contract and notation

There are `m` training inputs `u_a`, with `|u_a|≤1`, and tanh activation.
The labels are `y=a ybar`, where `ybar` is fixed and `a≥0` is the amplitude.
The population initial readout is zero. The middle initialization consists
of independent Gaussian `k × k` blocks, with fixed `k`, and their actual
transposes are always reused. The same formulas hold for a finite block
network, with empirical normalized contractions.

For finite width, put `<v,w>=v^T w/n`; in the block population this means
`E[v^T w/k]`. Products of such brackets in the formulas below remain
products of expectations. In particular they are not replaced by a single
same-block expectation. Let

\[
p_a=\tanh(w_0u_a),\quad q_a=1-p_a^2,\quad
H_a=\tanh(W_0p_a),\quad d_a=1-H_a^2.
\]

`W0` in a population local expression is the block `G`. Write
`K0_ab=<H_a,H_b>`. We assume

\[
K_0\succeq\lambda I_m,\qquad \lambda>0.                 \tag{1}
\]

The result is conditional on (1), which is directly checkable from the
initialization contractions. It does not silently cover singular Gram
matrices. Constants below can depend on `m,k,lambda,ybar`, and the eighth
moment of `1+||G||F`, but not on block count. Gaussian blocks satisfy this
moment hypothesis. The query domain is the whole input unit disk, not a
query mesh.

Allowed coefficients are finite contractions of initial features and their
derivatives, computed from the prescribed Gaussian law and the dataset.
No trained population, future trajectory, labels of individual evolving
blocks, fitted kernel history, or moving quadrature nodes are retained.
Static quadrature for initialization has its own accuracy and work cost;
its nodes can be discarded after the contractions have been computed.

## 2. Exact P1 output dynamics: where positivity fails

For this section all features are current features. Set

\[
N=B/L,\qquad C=A/L,\qquad E_b=h_{1,b}-N_b.
\]

The exact reconstructed matrix and its velocity are

\[
W=W_0-\frac2{mn}AN^T,
\qquad
\dot N_b=\frac\rho L(h_{1,b}-N_b),
\]

\[
\dot W=-\frac2{mn}\sum_b
\left[r_b\delta_{2,b}N_b^T+\rho C_bE_b^T\right].       \tag{2}
\]

Define the current scalar contractions

\[
\begin{aligned}
K^c_{ab}&=\langle h_{2,a},h_{2,b}\rangle,\\
K^w_{ab}&=(u_a\cdot u_b)\langle\delta_{1,a},\delta_{1,b}\rangle,\\
D_{ab}&=\langle\delta_{2,a},\delta_{2,b}\rangle,\quad
H_{ab}=\langle h_{1,a},h_{1,b}\rangle,\\
E_{ab}&=\langle h_{1,a},E_b\rangle,\quad
V_{ab}=\langle\delta_{2,a},C_b\rangle.
\end{aligned}
\]

Differentiating `f_a=<c,h2_a>` and inserting (2) gives the exact identity

\[
\dot r=-\frac2mK_*r+\frac2m j,
\quad K_*=K^c+K^w+D\odot H,
\quad
j_a=\sum_bE_{ab}(D_{ab}r_b-\rho V_{ab}).              \tag{3}
\]

`K_*` is PSD, as a sum of Gram matrices, but the innovation `j` has no
general favorable sign. Thus replacing P1 by a canonical PSD tangent
kernel is not an exact identification.

There is a useful entirely scalar innovation certificate. Put

\[
Z_{bc}=\langle E_b,E_c\rangle,\quad
U_{bc}=\langle C_b,C_c\rangle,
\]

\[
T_{bc}=r_br_cD_{bc}-\rho r_bV_{bc}-\rho r_cV_{cb}
            +\rho^2U_{bc},\qquad
\tau=\sum_{bc}Z_{bc}T_{bc}.                           \tag{4}
\]

`Z` and `T` are PSD. More strongly, the following is a Gram matrix in a
tensor product of two normalized layer spaces:

\[
\begin{pmatrix}D\odot H&j\\j^T&\tau\end{pmatrix}
\succeq0.                                           \tag{5}
\]

Indeed its first `m` vectors are
`h1_a tensor delta2_a`, and its last vector is
`sum_b E_b tensor (r_b delta2_b−rho C_b)`.
Consequently

\[
|r^Tj|\le\sqrt{(r^T(D\odot H)r)\tau}.               \tag{6}
\]

This is a source-size certificate, not a closure theorem: differentiating
these Gram entries generates additional nonlinear contractions. Positivity
alone does not supply the missing evolution equations. The construction
below supplies those equations to the first nonzero feature-learning
order, with an explicit residual-relative defect.

## 3. One initial PSD tensor

For training indices `a,b,c,d`, define

\[
\begin{aligned}
S_{(a,b),(c,d)}={}&(u_a\cdot u_c)
\left\langle q_a\odot W_0^T(H_b\odot d_a),
q_c\odot W_0^T(H_d\odot d_c)\right\rangle\\
&+\langle p_a,p_c\rangle
\langle H_b\odot d_a,H_d\odot d_c\rangle .            \tag{7}
\end{aligned}
\]

Regarded as a matrix with the paired index `(a,b)`, `S` is PSD. The first
term is the Gram of
`[q_a ⊙ W0^T(H_b ⊙ d_a)] tensor u_a`. The second is the Gram of
`p_a tensor (H_b ⊙ d_a)`. Both normalized inner products have exactly the
scaling displayed in (7). This also proves symmetry under interchange of
the two paired indices.

The formula extends to a query `x` in either position of a paired index by
using `u_x=x` and its initial features. A query in the second position
means `H_x`; a query in the first position changes `p_x,q_x,d_x,u_x`.
These two roles are different and cannot be interchanged silently.

## 4. The autonomous aggregate ODE

Keep the residual `r` in `R^m`, cumulative residual `z` in `R^m`, and a
matrix `J` in `R^(m×m)`. Initialize

\[
r(0)=-y,\qquad z(0)=0,\qquad J(0)=0.
\]

From these states calculate

\[
M_{qa}=\frac4{m^2}\sum_{bc}J_{bc}S_{(a,q),(b,c)},
\qquad
N_{qa}=\frac4{m^2}\sum_{db}z_dz_bS_{(q,d),(a,b)}.     \tag{8}
\]

Here `N` is a kernel, unrelated to the normalized memory `N=B/L` in
Section 2; to avoid ambiguity in implementations it should be named
`K_tangent2`. It is PSD: for `v in R^m`,

\[
v^TNv=\frac4{m^2}\sum_{qd,ab}
(v_qz_d)S_{(q,d),(a,b)}(v_az_b)\ge0.                 \tag{9}
\]

Define

\[
\widehat K=(I+K_0^{-1}M)^TK_0(I+K_0^{-1}M)+N
=K_0+M+M^T+N+M^TK_0^{-1}M.                         \tag{10}
\]

The complete training ODE is

\[
\dot r=-\frac2m\widehat K r,\qquad
\dot z=r,\qquad \dot J=rz^T.                        \tag{11}
\]

The training output is `fhat_train=y+r`. If a clock is wanted, append
`Lhat'=||r||/sqrt(m)`, `Lhat(0)=1`; it is not needed to evaluate (11).

The symmetric part of `J` is redundant:

\[
J+J^T=zz^T.
\]

Thus retain only a skew matrix `Omega`, set `J=zz^T/2+Omega`, and evolve
`Omega'=(rz^T−zr^T)/2`. The independent training state count is

\[
D_{\rm train}=\frac{m(m-1)}2+2m                      \tag{12}
\]

or one more with the optional clock. The ODE has ordinary polynomial
right-hand sides once the constant inverse `K0^-1` is computed.

Two structural properties hold without a small-label assumption:

* `Khat` is PSD at every state, and
  `d(||r||^2/m)/dt=−4 r^T Khat r/m^2≤0`.
* At `r=0`, every state derivative in (11), including all optional query
  integrals below, is zero. Stopping is an exact property of the vector
  field, not a numerical clipping rule.

These properties also yield global existence. The residual stays bounded;
on every finite interval `z` grows at most linearly, `J` at most
quadratically, and hence no state can escape to infinity in finite time.
They do not by themselves imply convergence to zero for arbitrary labels.

## 5. Why this is the cubic feature-learning correction

First drive the exact P1 system with any residual path `r(t)`, setting
`rho=||r||/sqrt(m)`, and define its exact path integrals

\[
z_a=\int_0^t r_a(s)\,ds,\qquad
J_{ab}=\int_0^t r_a(s)z_b(s)\,ds.                    \tag{13}
\]

The leading readout and the quadratic parameter movements are

\[
c_1=-\frac2m\sum_bz_bH_b,
\]

\[
w_2=\frac4{m^2}\sum_{ab}J_{ab}
 [q_a\odot W_0^T(H_b\odot d_a)]u_a^T,
\]

\[
A_{2,a}=-\frac2m\sum_bJ_{ab}(H_b\odot d_a),
\qquad
W_2=\frac4{m^2n}\sum_{ab}J_{ab}(H_b\odot d_a)p_a^T.
                                                               \tag{14}
\]

For example, substituting `c1` into
`w'=−(2/m)sum_a r_a q_a ⊙ W0^T(c1 ⊙ d_a) u_a^T`
produces the second equation of (14), since `J_ab'=r_a z_b`.
The equations for `A2` and `W2` follow from `A_a'=r_a c1 ⊙ d_a`
and `W−W0=−2 A(B/L)^T/(mn)`, with `B/L=p` to the needed order.

The induced quadratic second-layer feature change at query `q` is

\[
h_{2,2,q}=d_q\odot[W_0(q_q\odot w_2u_q)+W_2p_q].    \tag{15}
\]

Moving `W0` to its actual transpose in the normalized bracket gives

\[
\langle H_d,h_{2,2,q}\rangle
=\frac4{m^2}\sum_{ab}J_{ab}S_{(q,d),(a,b)}.           \tag{16}
\]

In particular `M_qa=<H_q,h2,2,a>`. Therefore the readout-feature Gram is

\[
K^c=K_0+M+M^T+O(R^4),\qquad
R(t)=\int_0^t\|r(s)\|_2\,ds.                        \tag{17}
\]

The leading trained first-layer and middle tangent Gram is precisely
`N` from (8), because substituting `c1` into the two tangent features gives
the contraction in (9). It follows that the canonical part of (3) is

\[
K_*=K_0+M+M^T+N+O(R^4).                            \tag{18}
\]

This is feature learning: both `M` and `N` evolve, and are generally
nonzero. It is not a frozen-kernel fit. The construction does not claim
that their change is large; it is quadratic in label amplitude in the
proved regime.

The extra term in (10) has size `O(R^4)`. It is the positive completion of
the moving readout Gram from its cross-Gram `M`, and changes the output
only at fifth order. No future trajectory is used in this completion.

## 6. A residual-relative source estimate

The following estimate provides the bridge beyond a formal Taylor series.
For any controlled path with `R(t)≤1`, the exact P1 output satisfies

\[
\left\|\dot f(t)+\frac2m
\widehat K(z(t),J(t))r(t)\right\|_2
\le C R(t)^4\|r(t)\|_2.                             \tag{19}
\]

The same statement holds for a bounded query, using the cubic query
kernel in Section 8 and omitting the order-four completion. The constant
is uniform over the query unit disk.

Here are explicit ingredients for proving (19). Let
`g=1+||G||F`. The constants in the following componentwise block estimates
are independent of block count; `m,k` factors are absorbed into `C`.
For `R≤1`, direct integration and `|tanh|,|tanh'|≤1` give

\[
\begin{aligned}
|c|&\le CR,& |A|&\le CR^2,& |B/L|&\le1,\\
|w-w_0|&\le CR^2g,&
|h_1-p|&\le CR^2g,&
|B/L-p|&\le CR^3g,\\
|h_2-H|&\le CR^2g^2,&
|c-c_1|&\le CR^3g^2.
\end{aligned}                                                    \tag{20}
\]

For the memory estimate, use the exact positive average

\[
\frac{B_a(t)}{L(t)}=
\frac{p_a+\int_0^t\rho(s)h_{1,a}(s)\,ds}
 {1+\int_0^t\rho(s)\,ds}.
\]

Subtracting `p_a`, the numerator is an integral of
`rho(h1_a−p_a)`. Since `int rho≤R/sqrt(m)` and
`|h1_a−p_a|≤CR^2g`, this is `O(R^3g)`.
Subtracting the equations in (14) from the exact equations, and using
the bounded first and second derivatives of tanh, next gives

\[
|A-A_2|\le CR^4g^2,\quad
|w-w_0-w_2|\le CR^4g^3,\quad
|h_2-H-h_{2,2}|\le CR^4g^4.                          \tag{21}
\]

For clarity, the forcing of `w−w0−w2` is the product of `r` with
one of: `c−c1=O(R^3g^2)` followed by `G^T`; the change of a tanh
derivative `O(R^2g^2)` times `c1=O(R)` and at most one `G^T`;
or the learned middle matrix acting on a readout of size `O(R)`.
Its size is at most `C||r|| R^3g^3`, whose integral is
`O(R^4g^3)`. The argument for `A−A2` removes the extra transpose.
Applying the bounded second derivative to the forward maps gives the
last estimate of (21), with one further `G`.

Using (20)–(21) in normalized brackets proves (17)–(18), as well as
`K^w+D odot H−N=O(R^4)`. The eighth moment hypothesis controls all
displayed squared weighted remainders; it is more than sufficient for
the unsquared output bounds.

Finally `E_ab=O(R^2)`, `D_ab=O(R^2)`, and `V_ab=O(R^3)` in (3).
Since `rho≤||r||/sqrt(m)`, its innovation obeys

\[
\|j\|_2\le C(R^4+R^5)\|r\|_2.                       \tag{22}
\]

Equations (18), (22), and `M^T K0^-1 M=O(R^4)` prove (19).
This is an actual error-production estimate, not an assumption that an
uncomputed closure residual is small.

The loss clock has a particularly high-order effect here. It gives
`L−1=O(a)` but `B/L−p=O(a^3)`. Multiplication by `A=O(a^2)` first
puts this particular clock-dependent change into `W` at order `a^5`,
and into output at order `a^6`. P1 can already differ from canonical
gradient dynamics at order `a^5` in output because replacing the current
`h1` by `B/L` creates the order-four kernel lag in (22). These are two
different comparisons.

## 7. Uniform-in-time small-label theorem

**Theorem.** Under (1), zero initial readout, and the stated eighth moment
bound, there exist `a0>0` and `C<infinity`, depending only on the data,
fixed block size, initial contraction/moment bounds, and `ybar`, such that
for `0≤a≤a0` both the exact P1 residual and the aggregate residual in
(11) decay exponentially to zero. Moreover

\[
\sup_{t\ge0}\|f_{\rm P1}(t,\mathrm{train})-(y+r(t))\|_2
+\int_0^\infty\|r_{\rm P1}(t)-r(t)\|_2\,dt
\le Ca^5.                                          \tag{23}
\]

The query decoder in Section 8 also satisfies

\[
\sup_{t\ge0,\ |x|\le1}
|f_{\rm P1}(t,x)-\widehat f(t,x)|\le Ca^5.           \tag{24}
\]

Both sides of (24) have terminal limits, and the bound holds for those
limits. With loss defined as mean squared residual, its trajectory error
is `O(a^6)` by (23) and the `O(a)` residual bounds.

**Proof.** The estimates above first give, for either residual flow,

\[
\dot r=-\frac2mK_0r+e_0,
\qquad \|e_0\|\le CR(t)^2\|r\|,
\]

whenever `R≤1`. Choose `R0>0` such that `CR0^2≤lambda/m`, and then
choose `a0` such that `m a0||ybar||/lambda<R0/2`.
Until a possible first crossing of `R0`,

\[
\|r(t)\|\le a\|\bar y\|e^{-\lambda t/m},\qquad
R(t)\le ma\|\bar y\|/\lambda<R_0/2.
\]

This contradicts such a first crossing and proves the bound for all
time. The constants can be reduced further below as needed. It also
gives `z=O(a)`, `J=O(a^2)`, `M,N=O(a^2)`, and coercivity
`Khat≥lambda I/4` on both relevant paths.

Now form `z*,J*` from the exact P1 residual by (13). Equation (19) says
that `(r*,z*,J*)` satisfies (11) with a residual-equation forcing `d(t)`
bounded by `C a^4 ||r*(t)||`. Let

\[
E_1(t)=\int_0^t\|r^*(s)-r(s)\|\,ds.
\]

Then `||z*−z||≤E1` and, subtracting the two integrals defining `J`,
`||J*−J||≤Ca E1`. Since `M` is linear in `J` and `N` quadratic in `z`,

\[
\|\widehat K(z^*,J^*)-\widehat K(z,J)\|
\le Ca E_1(t).
\]

The error equation has a coercive homogeneous matrix. Taking its norm,
integrating its exponential variation bound, and then integrating over
time gives, with constants independent of the upper time endpoint,

\[
E_1(t)\le C a^2E_1(t)+Ca^5.
\]

Reducing `a0` until the first coefficient is at most `1/2` proves the
integrated part of (23). The same variation bound gives its supremum
part. This proves (23) without an exponentially growing time-horizon
constant. Applying the query version of (19) and integrating its source
costs at most `C a^4 int||r*||=Ca^5`; changes of path integrals cost
`O(E1)=O(a^5)`. The explicit query completion below costs another
`O(a^5)`, proving (24). All derivative integrals are absolutely
convergent because residuals decay exponentially, proving the terminal
claims. ∎

This proof establishes a small-amplitude theorem; it does not give a
useful numerical amplitude threshold without evaluating the data- and
moment-dependent constants. A tiny `lambda` makes the admissible
amplitude correspondingly restrictive.

## 8. Decoding every query without query states

Append only the third-order scalar integrals

\[
\dot P_{a;bc}=r_aJ_{bc},\qquad P(0)=0.                \tag{25}
\]

For any query `x`, let `k_x=(<H_x,H_a>)_a`. Define the cubic decoder

\[
\begin{aligned}
f_{\rm cub}(x)=-\frac2m\Bigg[&k_xz\\
&+\frac4{m^2}\sum_{abc}P_{a;bc}
 \{S_{(a,x),(b,c)}+S_{(x,a),(b,c)}\}\\
&+\frac4{m^2}\sum_{adb}
 (P_{a;db}+P_{a;bd})S_{(x,d),(a,b)}\Bigg].           \tag{26}
\end{aligned}
\]

To verify (26), differentiate it. The first line gives `k_x r`.
The next gives the two cross-Gram contributions `M(x,a)+M(a,x)`.
The last gives the tangent contribution because
`J_db+J_bd=z_dz_b`. Thus its derivative is exactly the cubic kernel
`K0+M+M^T+N` applied to the current residual, including at training
aliases.

Let `f_cub(train)` denote the vector of (26) at the training inputs.
The final decoder is

\[
\widehat f(x)=f_{\rm cub}(x)
 +k_xK_0^{-1}\{y+r-f_{\rm cub}(\mathrm{train})\}.      \tag{27}
\]

At `x=u_a`, `k_x K0^-1=e_a^T`, so (27) agrees **exactly** with the
training output `y_a+r_a`; there is no training/query inconsistency.
The quantity in braces is the accumulated difference between the
completed kernel (10) and its cubic part. Its derivative is

\[
-\frac2mM^TK_0^{-1}Mr,
\]

so it is `O(a^5)` uniformly in time in the theorem's regime. This proves
the completion claim used in (24).

For the Gaussian block population, `k_x` and the tensor entries involving
`x` are integrals over the known initial Gaussian seed distribution.
They are coefficient functions of the input, not an evolving distribution
or a stored initialization-label dictionary. Their seed dimension is
fixed by `k` and the input dimension. They can be evaluated for a newly
requested query after training without adding a state coordinate.

For an arbitrary *finite realized* network, exact evaluation of these
functions at previously unspecified inputs would require access to its
initial realization or a separate approximation of those coefficient
functions. The finite-network training formula does not remove that
information requirement. Thus the unrestricted-query claim above is
specifically for the prescribed block population, or for a separately
declared finite coefficient-function representation.

The full-function dynamic state count is at most

\[
D_{\rm query}=m^3+\frac{m(m-1)}2+2m,                 \tag{28}
\]

plus one if the clock is retained. Shuffle identities can reduce the
third-order coordinates, but are unnecessary for the stated count.

## 9. Matched-accuracy cost and the limits of this result

The training coefficients require `m(m+1)/2` entries of `K0` and
`m^2(m^2+1)/2` entries of the symmetric matrix `S`. All-time state counts
are (12) and (28). A naive right-hand-side evaluation contracts `S` in
`O(m^4)` work; no claim of cheap large-`m` computation is made. Static
quadrature must compute these contractions accurately and preserve PSD
(positive-weight Gram quadrature is one option). Such quadrature is an
initialization procedure; its nodes are not trained or retained as a
population surrogate.

A P1 block-population Monte Carlo surrogate with `b` blocks retains
approximately

\[
b\,[k^2+k(3+2m)]+1
\]

scalars if static block matrices are included. Under the same stable
small-amplitude regime its leading output sampling scale is
`O(a/sqrt(b))`, so the usual RMS Monte Carlo budget for output tolerance
`epsilon` is `b=O(a^2/epsilon^2)`, up to variance/confidence constants.
This comparison presumes nonzero sampling variance and comparable
initial-contraction accuracy; it is not a deterministic lower bound on
every sampling method.

The present construction meets a requested tolerance when
`C a^5` plus the coefficient-integration error is at most `epsilon`.
At `epsilon` proportional to `a^5`, a Monte Carlo budget scales like
`a^-8`, whereas the number of evolving aggregate coordinates is fixed
for fixed `m`. It can therefore give a real state advantage in this
regime. Including static coefficient storage requires comparing
`O(m^4)` against the Monte Carlo storage, rather than counting only
the dynamic state.

There is no unconditional sub-width statement when `m` itself is large.
For example `m^3` query states can exceed an actual network width. The
state is sub-width only when the displayed counts are smaller than the
intended width-dependent baseline. Nor does decreasing coefficient
quadrature error drive the intrinsic `O(a^5)` truncation error to zero
at fixed amplitude. Higher feature-learning orders would need a new
construction and new source bounds.

## 10. Claim audit

* **Exact:** the P1 lag decomposition (2)–(3), innovation Gram certificate
  (5), PSD tensor (7), positivity and zero-residual stopping of (11),
  state counts, and the query alias identity (27).
* **Proved here, conditional:** all-time fifth-order output accuracy and
  sixth-order loss accuracy under (1) and sufficiently small labels,
  using the residual-relative source (19) and the small-gain argument.
  This derivation has not received an independent mathematical review.
* **Genuine but weak feature learning:** the order-two moving kernel and
  order-three output correction. The construction does not make that
  feature motion large in the regime covered by the theorem.
* **Open:** usefulness for the study's unit-label strong-learning tasks,
  informative numerical constants, large-`m` compression, singular
  initial Grams, and a practical arbitrary-accuracy extension at fixed
  amplitude.
* **Rejected inference:** PSD completion or bounded Gram state alone
  proves accurate P1 closure. The source estimate is indispensable.
* **No broad impossibility claim:** failure of this perturbative regime
  to cover a desired task would not rule out another compact aggregate
  construction.

The decisive applicability check is whether the actual target has a
useful initial coercivity constant and genuinely small cumulative
residual motion. If it does not, this result remains a rigorous limited
construction and must not be presented as the requested strong-learning
solution.

## 11. One training example: a single scalar ODE

The supervisor identified this reduction after the main derivation was
frozen. It is also obtained directly from (8)–(11). For `m=1`, write
`K0=kappa>0` and `S=s≥0`. Then

\[
J=z^2/2,\qquad M=2sz^2,\qquad N=4sz^2,
\qquad
\widehat K=\kappa+8sz^2+\frac{4s^2}{\kappa}z^4.
\]

Since `z'=r`, the residual equation can be integrated exactly with
respect to `z`, including by continuity at stationary points. The entire
training dynamics is the single scalar autonomous equation

\[
\dot z=-y-2\kappa z-\frac{16}{3}sz^3
             -\frac85\frac{s^2}{\kappa}z^5,
\qquad z(0)=0.                                      \tag{29}
\]

The training output is `fhat=y+z'`, equivalently the polynomial in (29)
without its `−y` term. The right-hand side has derivative
`−2 Khat≤−2 kappa`; it has one zero, and the solution tends to this zero
for every label `y`. Thus this one-scalar model has global terminal
fitting for any label. Its approximation theorem for the original P1
system still requires small `|y|`.

For any query, put

\[
k_x=\langle H_x,H_1\rangle,\qquad
A_x=S_{(1,x),(1,1)},\qquad B_x=S_{(x,1),(1,1)}.
\]

The third-order state also collapses: `P=z^3/6`. Equation (27) becomes
the explicit readout of this one scalar

\[
\widehat f(x)=
-2k_xz-\frac43z^3(A_x+3B_x)
-\frac{8k_xs^2}{5\kappa^2}z^5.                      \tag{30}
\]

At the training input, `kx=kappa` and `Ax=Bx=s`, so (30) equals the
training output exactly. At terminal time the root of (29) satisfies

\[
z_\infty=-\frac{y}{2\kappa}
             +\frac{s}{3\kappa^4}y^3+O(y^5),
\]

and hence

\[
\widehat f_\infty(x)=\frac{k_x}{\kappa}y
 +\frac{y^3}{6\kappa^3}
 \left(A_x+3B_x-\frac{4k_xs}{\kappa}\right)+O(y^5).   \tag{31}
\]

The cubic term is an explicit feature-learning change to terminal test
prediction. It vanishes at the training input, as it must. Formula (31)
does not assert that it is nonzero for every query or dataset.

## 12. Quantitative qualifications and checkable surrogate stability

Let `s_op=||S||op`. Reshaping indices gives the exact identity
`vec(M^T)=(4/m^2) S vec(J)`. Thus, with
`R(t)=int_0^t ||r||`,

\[
\|J\|_F\le R^2/2,\qquad
\|M\|\le\frac{2s_{\rm op}}{m^2}R^2,\qquad
\|N\|\le\frac{4s_{\rm op}}{m^2}R^2.                 \tag{32}
\]

If `R^2≤m^2 lambda/(4 s_op)`, then `||K0^-1 M||≤1/2` and
`Khat≥lambda I/4`. A first-crossing bootstrap therefore proves
exponential fitting of the surrogate whenever

\[
\|y\|_2<\frac{\lambda^{3/2}}{4\sqrt{s_{\rm op}}}.     \tag{33}
\]

Indeed coercivity gives `R≤2m||y||/lambda`, strictly below the proposed
crossing radius under (33). If `S=0`, the kernel is the constant `K0`
and the amplitude restriction in (33) is unnecessary. This explicit
surrogate threshold does not replace the additional moment-dependent
smallness needed to compare with exact P1.

Two limitations are especially relevant when judging practicality.

First, at output tolerance `O(a^5)`, leading initialization Gram errors
generally need to be `O(a^4)`, because an error `eta` in `K0` can produce
an `O(a eta)` output error. If all initialization contractions are
computed using ordinary Monte Carlo, their one-time sample requirement
can again scale like `a^-8`. Nodes are subsequently discarded, so the
dynamic-state saving remains, but an end-to-end work advantage has not
been proved. Fixed-dimensional deterministic Gaussian quadrature is a
possible way to compute the initial contractions; this note does not
give a sharp complexity theorem for that step.

Second, the query decoder belongs to a finite span of explicitly
specified *initial response coefficient functions*. These are not
individual initial-label characteristic maps and do not constitute an
evolving population dictionary. Nevertheless this is a finite response
expansion around initialization. Its validity comes from the proved
small-motion remainder, and it is not a general escape from the need
for richer functions when feature movement is large.

The supervisor subsequently reported separate finite algebra checks of
the tangent Gram, positive completion, and query derivative, without
running training experiments. Those checks are supporting algebraic
diagnostics only; the theorem above rests on the displayed derivation
and has not been promoted to established material.

## 13. Other controlled observables

Appending `Lhat'=||r||/sqrt(m)` controls the actual P1 loss clock:

\[
\sup_{t\ge0}|L_{\rm P1}(t)-\widehat L(t)|
\le\frac1{\sqrt m}\int_0^\infty
\|r_{\rm P1}(t)-r(t)\|\,dt=O(a^5).                  \tag{34}
\]

The same derivation controls genuine feature-learning aggregates, not
only output. Uniformly in time, the current P1 second-hidden feature
Gram differs from `K0+M+M^T` by `O(a^4)`. Adding its positive completion
`M^T K0^-1 M` retains the same order of accuracy. Its combined first-layer
and middle backward tangent Gram differs from `N` by `O(a^4)`.
Equations (17)–(18) give these errors on the exact residual path;
the proved path-integral comparison transfers them to the aggregate
path, with smaller additional errors.

The first-hidden feature Gram can likewise be decoded to this order by
contracting `p_a` with `q_b ⊙ (w2 u_b)` and its transpose, using (14).
This requires additional initialization contractions but no additional
dynamic states. It is not needed for (11) or the whole-query decoder.
