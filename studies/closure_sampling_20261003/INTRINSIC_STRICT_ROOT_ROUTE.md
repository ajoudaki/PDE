# Strict root-width folding from passive-query carrier moments

2026-10-04. Independent scoped candidate, frozen before exchanging its new
mathematical conclusions. This is an internal proof candidate requiring
reconstruction, not a promoted result. No experiment, Git mutation, book
change, or manuscript change was made.

The candidate closes the earlier root-width tightness gap by using a
one-half Hölder increment estimate. It needs only fixed-query moments of
ordinary backward carriers. It does **not** require higher angular jets,
a uniform exponential query budget, or a finite-moment bound for the
products of differentiated response fields in the earlier Sobolev route.
The new insertion extension and its asymmetric trace are proved below;
they are the principal points requiring independent checking.

Inputs read completely: INTRINSIC_INPUT_DIMENSION_ROUTE.md (including all
appendices), DIMENSION_FREE_REPRESENTATION_ROUTE.md,
ARCHITECTURE_CONSTANT_REFINEMENT.md, LABEL_DEPTH_RESCALING_ROUTE.md,
DEPTH_INDEPENDENT_EXPONENT.md, DEEP_COMPLEX_SOURCE.md, and
LABEL_SEPARATE_BUDGETS.md. The explicitly authorized prior files
DEPTH_CAVITY_ROUTE.md, DEPTH_INSERTION_CHECK.md, and
DEPTH_CAVITY_PROBABILITY_CHECK.md in dense_cutoff_population_rate_20261001
were read; their appended unbounded-activation claims are not used.
The canonical-notation and neural conventions, rigorous-proof skill, and
research-contract/evidence/adversarial references were applied. No other
study or new sibling-route result was read.

## 1. Contract and result

Use unit inputs v=x/sqrt(d), fixed hidden depth L>=2, and the canonical
width-n network

\[
z^{(1)}(t,v)=A(t)v,\qquad
z^{(\ell)}(t,v)=W^{(\ell)}(t)h^{(\ell-1)}(t,v),\qquad
h^{(\ell)}=\phi_\ell(z^{(\ell)}),\qquad
f_n(t,v)=w(t)^\top h^{(L)}(t,v)/n.
\tag{1}
\]

The initial entries of A are independent N(0,1), hidden entries are
independent N(0,1/n), initialized blocks are independent, and w(0)=0.
All activations are real on the real line and bounded and holomorphic
on the common fixed strip. Use the activation number beta>=10 from
ARCHITECTURE_CONSTANT_REFINEMENT.md. Put c_a=y_a-f_n(t,v_a),
Y=||y||_2/sqrt(m), and let gamma>0 be its limiting initialized top-feature
Gram gap. Assume

\[
Y\le (\gamma/m)\beta^{-62L},\qquad
\lambda=\min(1,\gamma/m),\qquad S=16Y/\lambda.
\tag{2}
\]

For Y=0 every output is exactly zero; suppose Y>0 below. The loss is
m^(-1)sum_a c_a^2, with mobilities (n,1,...,1,n). Define query carriers
at every unit v by

\[
k^{(L)}(t,v)=w(t),\quad
\delta^{(\ell)}(t,v)=\phi_\ell'(z^{(\ell)}(t,v))\odot k^{(\ell)}(t,v),
\quad k^{(\ell)}=W^{(\ell+1)\top}\delta^{(\ell+1)}.
\]

Training uses only the corresponding vectors at v_a:

\[
\dot A={2\over m}\sum_a c_a\delta_a^{(1)}v_a^\top,\quad
\dot W^{(\ell)}={2\over mn}\sum_a c_a
               \delta_a^{(\ell)}h_a^{(\ell-1)\top},\quad
\dot w={2\over m}\sum_a c_a h_a^{(L)}.
\tag{3}
\]

Let V=span{v_a}, r=dim(V), and k=d-r. Choose orthonormal coordinate
matrices U for V and E for its perpendicular. If k>0, choose a fixed
unit e in V perpendicular and put

\[
\widetilde v=P_Vv+\|P_{V^\perp}v\|_2 e.
\tag{4}
\]

The candidate conclusion is that for every fixed failure probability
xi>0, for all sufficiently large widths,

\[
\Pr\left\{\sup_{t\in[0,\infty],\ v\in S^{d-1}}
 |f_n(t,v)-f_n(t,\widetilde v)|
             \le C_{d,L,\phi,\mathrm{data},\xi}/\sqrt n\right\}
 \ge1-\xi.
\tag{5}
\]

The constant is independent of width and time. It is not claimed to have
the explicit error coefficient of the older theorem. This is a comparison
of two queries of the **same realized finite network**, with its original
physical time and original learned hidden matrices.

## 2. Training conditioning and the event used in concentration

Equation (3) gives A(t)E=A(0)E=:G. The entire training path depends only
on A(0)U, the hidden initialization, and the data. Denote their sigma-field
by F. Thus G is an n-by-k standard Gaussian matrix independent of F and

\[
z^{(1)}(t,v)=A_V(t)U^\top v+GE^\top v,\qquad A_V=A U.
\tag{6}
\]

Take an F-measurable event E_n with probability tending to one on which
the inherited real fitting tube and separate training budgets hold through
T_n=32lambda^(-1)log(en). Its initial first-weight norm restriction uses
only A(0)U; no restriction on G is included in E_n. The source proofs
remain valid after this choice: training never uses G, and the extra
Gaussian query-row events are kept separately below. The event supplies

\[
\rho(t):=\|c(t)\|_2/\sqrt m\le Ye^{-\kappa t},\quad
\kappa=\lambda/4,\quad
\sup_t\|w(t)\|_\infty\le BS,
\]
\[
\sup_t\|W^{(\ell)}(t)\|_{\rm op}\le9,\quad
\sup_t\|A_V(t)\|_{\rm op}/\sqrt n\le C,\quad
\sup_{t,v,\ell}\|k^{(\ell)}(t,v)\|_{2,n}\le CS.
\tag{7}
\]

Here ||u||_(p,n)=(n^(-1)sum_i|u_i|^p)^(1/p). The final bound in (7)
holds for every real G and unit query, because it uses only bounded gates,
bounded mixer operators, and the readout bound. Training budgets are

\[
{1\over n}\sum_{\ell<L,i}
 \exp\left({\eta\over S}\sup_{0\le t\le T_n}
                          |k_{a,i}^{(\ell)}(t)|\right)\le\mathcal B
\tag{8}
\]

separately for each a. The fixed eta and mathcal B are those of
LABEL_DEPTH_RESCALING_ROUTE.md. Their doubled versions apply to autonomous
cavities on common prefixes. In mobility coordinates
Theta=(A,sqrt(n)W^(2),...,sqrt(n)W^(L),w), all training Hessians and
external-response endpoints have the bounds

\[
\|H\|_{p,n}\le A_H+{SD_H\over\eta}\,p(2\mathcal B)^{1/p},\quad
\|H\|_{2,n}\le H_2,\qquad p\ge2.
\tag{9}
\]

For matrices ||M||_(p,n)=n^(-1/p)||M||_(S_p). These are bounds for the
actual augmented training Hessian blocks specified in the source, not
claims that every query Hessian has the higher-p bound (9).

## 3. The new query-endpoint trace

Delete a singleton neuron i at layer j<L. Let x_i be its initialized
outgoing column, and, for j>=2, let y_i be its initialized incoming row
transposed. Conditional on retained initialization they are independent
N(0,I/n) roots. The autonomous rectangular cavity keeps normalization n
and its own residual. Its retained training equation, state variation,
negative-Gram base propagator, and residual-Hessian insertions are precisely
those of the bounded prior insertion theorem.

At one passive query v define, in the zero-source cavity,

\[
d_v=\delta^{(j+1)}(t,v),\qquad B_v=D_\Theta d_v,
\qquad E_v=D_{e_v}d_v,
\tag{10}
\]

where e_v is an external preactivation at layer j+1. Query fields produce
no training force. The Hessian identity in prior equation (11), with the
sample replaced by v and one argument restricted to e_v, proves

\[
\|B_v\|_{2,n}\le C,\qquad
|\operatorname{tr}E_v|/n\le CS.
\tag{11}
\]

For the first bound, every curvature term is a bounded-map contraction
of diag(phi'' k^(ell)(v)); its normalized Hilbert--Schmidt norm uses
only the query carrier RMS in (7). Mixed weight terms have rank O(n)
and bounded operator norm, again using feature and carrier RMS. The
readout mixed term is bounded independently of S. For the trace bound,
E_v is the sum of T_ell^T diag(phi''k^(ell)(v))T_ell with
||T_ell||_op<=C; hence its normalized trace is bounded by
Csum_ell||k^(ell)(v)||_(1,n)<=CS. Neither statement uses a query
carrier maximum or query higher moment.

Let J(t,s) be the cavity variational propagator. The same-root state
insertion for the passive endpoint contains

\[
{1\over n}\operatorname{tr}\{B_v(t)J(t,s)B_a(s)^\top\},
\tag{12}
\]

where B_a=D_Theta delta_a^(j+1) is a **training** endpoint. A Dyson term
with h>=1 training Hessians uses Schatten exponent 2 for B_v and exponent
2(h+1) for each of the h Hessians and B_a. The reciprocal exponents sum
to one. The normalized trace is consequently bounded, after time-simplex
integration, by

\[
{C S^h\over h!}
\left[A_H+{2SD_H\over\eta}(h+1)
                  (2\mathcal B)^{1/[2(h+1)]}\right]^{h+1}.
\tag{13}
\]

At h=0 use both endpoints in normalized Schatten-2. To sum (13), split
the (h+1)st power by (u+v)^(h+1)<=2^h(u^(h+1)+v^(h+1)). Its constant
part sums to at most C A_H exp(2SA_H). Its budget part is bounded by

\[
C{SD_H\over\eta}\sqrt{2\mathcal B}
\sum_{h\ge1}(4eS^2D_H/\eta)^h(h+1).
\tag{14}
\]

We used (h+1)^(h+1)/h!<=e^(h+1)(h+1), which follows from
h!>=(h/e)^h and (1+1/h)^h<=e. The series converges under the existing
source condition
16eS^2(D_H/eta)sqrt(2mathcal B)<=1. The harmless factor two in the
complex proof is unnecessary here. Thus (12) has a width-independent
bound C depending on the already fixed source constants. No extra
small-label condition depending on a query moment degree is introduced.

This is the asymmetric improvement needed here. Assigning the same
Schatten exponent to both endpoints would incorrectly ask for a query
carrier budget that has not been proved.

## 4. Passive backward insertion and fixed-query moments

The inherited local insertion proof did not explicitly include passive
backward observables. The following extension verifies what is added.
Impose, solely for its proof, a simultaneous real-query carrier stop

\[
\max_{v\in S^{d-1},\,j<L,\,i,\,t\le T_n}
 |k_i^{(j)}(t,v)|\le M_n=C_* S\sqrt{\log(en)},
\tag{15}
\]

and doubled caps for each cavity. All query RMS bounds (7) hold before,
after, and independently of this stop. The already inherited training
budget cap is O(log n).

At a deletion, the passive forward computation has the exact external
source e_v=x_i h_i^(j)(v), plus the learned-column remainder. Its lower
backward computation has source q_v=y_i delta_i^(j)(v), plus the
learned-row remainder. These are observable sources only: they do not
enter the training vector field. Their amplitudes and time Lipschitz
constants are respectively polylogarithmic and sqrt(n) times a
polylogarithm on (15). Learned source remainders have norm
n^(-1/2)polylog(n), by the same actual rank-one weight updates.

Add these query forward and backward linear variations to the prior
conditional event. For each deterministic training and query control,
they are linear maps of the omitted roots. The parameter-state variation
is unchanged. Bounded gates, bounded operators, and the stopped training
and query diagonals give operator norms n^(1/1000)polylog(n), at most
n^(1/200) eventually. Thus their coordinate tails at n^(-1/10) have
exponent n^(0.79), and their Euclidean images have radius n^(1/100).
The additional finite set of scalar query controls has the same
n^(5/8)polylog(n) control-net logarithm. A polynomial sphere/time grid
adds only O(log n). Its off-grid moduli are polynomial because the first
input derivative has norm O(sqrt(n)) and all stopped network derivative
operators have polynomial bounds. No function class indexed by a
continuum of query control histories is inserted without this grid/net.

For nonlinear observables, the exact downward recursion is

\[
\Delta\delta^{(\ell)}
 =\phi_\ell'(z_0^{(\ell)})\odot\Delta k^{(\ell)}
  +\phi_\ell''(z_0^{(\ell)})\odot k_0^{(\ell)}
                                      \odot\Delta z^{(\ell)}
  +\text{remainder},
\]
\[
\Delta k^{(\ell)}
 =W_0^{(\ell+1)\top}\Delta\delta^{(\ell+1)}
  +(\Delta W^{(\ell+1)})^\top\delta_0^{(\ell+1)}
  +(\Delta W^{(\ell+1)})^\top\Delta\delta^{(\ell+1)},
\tag{16}
\]

with the explicit q_v source added at the deleted layer. Here the subscript
0 means the cavity reference, not initialization. Split every change into
its Gaussian linear part and nonlinear remainder u. With the prior
exponents a=1/100 and b=1/10, products of changed scalar gates have
Euclidean remainder at most C[n^(a-b)+n^(-b)u+u^2]; reference query
carriers multiply this only by M_n. Mixed weight products retain 1/sqrt(n).
The independent incoming-row probe estimate is unchanged, since the
passive query only adds another lower bounded forward derivative map.
Its leading power remains n^(2a-b). There is no new residual Taylor
term because the query supplies no loss. Consequently the exact prior
bootstrap, with u<=n^(-1/25) and variational cost n^(1/1000), closes
with the same strict margins. It gives coordinate error o(1) and ordinary
Euclidean query-response error at most n^(1/100), uniformly on common
prefixes. This also transfers the doubled query cap to each cavity.

For the upper passive response d_v in (10), which has no direct reverse
observable source, the linearized identity is

\[
d_v^{\rm full}-d_v^0=B_v V+E_v x_i h_i^{(j)}(v)
                                      +o_{\ell^2}(1).
\tag{17}
\]

Pair with x_i. The training forward forcing in V contributes (12),
multiplied by a bounded deleted training activation and integrated against
residual activity. The incoming-root term is a centered x-y bilinear form,
including its actual training carrier control. The rank-one adaptive
residual term has normalized trace n^(-1+1/1000)polylog(n). The direct
query source contributes h_i^(j)(v)tr(E_v)/n. Uniformity of the Gaussian
quadratic-form event permits substituting all actual root-dependent
controls only after the event has been constructed. Equations (11)--(14)
therefore bound every nonvanishing same-root mean by CS. The learned
outgoing-column correction is at most CS^3, since its norm is CS^2/sqrt(n)
and ||d_v||_2<=CSsqrt(n). We obtain

\[
|k_i^{(j)}(t,v)-x_i^\top d_v^{-i}(t)|\le CS+o(1)
\tag{18}
\]

on common prefixes. Constants are independent of C_* in (15).

Freeze cavity references at their own stops and set them to zero on their
own failed physical initialization events. Each frozen reference remains
independent of x_i and has RMS at most CS. At a fixed time and query,
its pairing with x_i is therefore a centered Gaussian with standard
deviation at most CS. A polynomial time/query grid and its polynomial
moduli give maximum CSsqrt(log n) with failure at most n^(-M), for any
fixed desired M, by increasing the fixed Gaussian multiplier. Equation
(18) strictly improves (15) when C_* is chosen with a margin. Cavity
caps cannot fail earlier by the coordinate-small comparison. Thus the
query caps disappear. All local insertion exceptional events are
superpolynomially small; initial query Gaussian-row and Gaussian-maximum
events can have any prescribed polynomial failure rate. The training
budget event remains E_n and is never conditioned on in a Gaussian law.

In particular, for every fixed p>=2, there is C_p independent of t,v,n
such that

\[
\sup_{t\le T_n,\,v\in S^{d-1},\,\ell}
\mathbb E\left[\mathbf1_{E_n}
                     \|k^{(\ell)}(t,v)\|_{p,n}^p\right]
 \le C_p S^p.
\tag{19}
\]

To verify the probability passage, on the local good event raise (18)
to p and remove full-event indicators only from the nonnegative Gaussian
upper bound. Conditional Gaussian moments give C_p S^p. On its complement
use the deterministic pointwise bound |k_i|<=CSsqrt(n) from (7), and
choose M>p/2+2 above. Its contribution is at most C_p S^p n^(p/2-M).
Average over i. No common-cavity moment expansion, independence between
neurons, or growing deletion count is needed for (19).

The all-time deterministic tail gives
max_(v,i,ell,t>=T_n)|k_i^(ell)(t,v)-k_i^(ell)(T_n,v)|
<=CS n exp(-kappa T_n)=O(n^(-7)). Indeed physical query forward speed
has RMS C rho S, all query carriers have RMS CS, and their crude coordinate
cap CSsqrt(n) gives the same backward-derivative bound as prior equation
(37), uniformly over unit v. Thus (19) holds for all t including infinity,
with a changed fixed constant. This tail uses no query moments.

## 5. Finite moments yield a one-half Hölder increment

Let tau(t)=1-exp(-kappa t), with tau(infinity)=1. This is a deterministic
clock used only in the proof. It avoids root-dependent inverse activity
times. From (3), (7), and residual decay, for t>=s,

\[
\|w(t)-w(s)\|_{2,n}\le CS|\tau(t)-\tau(s)|,
\]
\[
\|W^{(\ell)}(t)-W^{(\ell)}(s)\|_{\rm op}
 +\|A_V(t)-A_V(s)\|_{\rm op}/\sqrt n
 \le CS^2|\tau(t)-\tau(s)|.
\tag{20}
\]

For unit v,v', the real forward pass therefore satisfies, layer by layer,

\[
\|z^{(\ell)}(t,v)-z^{(\ell)}(s,v')\|_{2,n}
 \le C\big[(1+\|G\|_{\rm op}/\sqrt n)\|v-v'\|_2
                       +S^2|\tau(t)-\tau(s)|\big].
\tag{21}
\]

The first layer uses (6) and (20); subsequent layers use bounded features,
slopes, and mixer operators. Write the bracket on the right as D.
Both phi' and phi'' are bounded on the real axis, so

\[
\|\phi_\ell'(z)-\phi_\ell'(z')\|_{4,n}
 \le C\|z-z'\|_{2,n}^{1/2}.
\tag{22}
\]

Indeed |phi'(z)-phi'(z')|^4 <= (2s)^2 t_phi^2 |z-z'|^2.
Subtract the two backward recursions, always multiplying a changed gate
by the reference carrier at (s,v'). Normalized counting Hölder gives

\[
\|(\phi'(z)-\phi'(z'))\odot k'\|_{2,n}
 \le C D^{1/2}\|k'\|_{4,n}.
\]

The changed mixer term is bounded by CS^3|tau(t)-tau(s)| using (7)
and (20). Downward induction from the readout proves

\[
\|\delta^{(1)}(t,v)-\delta^{(1)}(s,v')\|_{2,n}
 \le CS|\tau(t)-\tau(s)|
   +C D^{1/2}\sum_{\ell=1}^L\|k^{(\ell)}(s,v')\|_{4,n}.
\tag{23}
\]

For each fixed p>=2, (19), counting-norm monotonicity, and ordinary
probability Hölder bound the L^p norm of (23), with indicator E_n, by

\[
C_p S\big(|\tau(t)-\tau(s)|+\|v-v'\|_2\big)^{1/2}.
\tag{24}
\]

All required moments of ||G||_op/sqrt(n) are uniformly finite for fixed
k: its Frobenius norm bound is already sufficient. For example the
product in (23) is controlled by the 2p-th probability moments of the
carrier counting-four norm and of (1+||G||_op/sqrt(n))^(1/2).
When 2p>=4, Jensen gives
E[1_E||k||_(4,n)^(2p)] <= E[1_E||k||_(2p,n)^(2p)] <= C_p S^(2p).
The same argument with moment order 4 covers the smaller exponents.
Neither a coordinate maximum nor an independence of these two factors
has been used.

## 6. Gaussian increments and chaining, with no log(n) loss

Define

\[
\bar f_n(t,v)=\mathbb E_G[f_n(t,v)\mid F],\qquad
Z_n(t,v)=\sqrt n\,[f_n(t,v)-\bar f_n(t,v)].
\tag{25}
\]

For any fixed F in E_n, conditional differentiation gives exactly

\[
\nabla_G f_n(t,v)=n^{-1}\delta^{(1)}(t,v)(E^\top v)^\top.
\tag{26}
\]

For a smooth scalar H of a standard Gaussian vector, Gaussian rotation
between independent copies gives

\[
\|H-\mathbb EH\|_{L^p}\le C\sqrt p\,
                \|\|\nabla H\|_2\|_{L^p},\qquad p\ge2.
\tag{27}
\]

In detail, rotate (G,G') through a quarter-circle; the rotated derivative
matrix is standard Gaussian independent of the current rotated matrix.
Conditioning on the latter bounds its scalar product with grad H by
C sqrt(p)||grad H||_2. Integrate and apply Jensen to subtract the independent
copy. This proof also allows integration over F with the indicator E_n,
since E_n is independent of G and G'. Finite-width integrability follows
from bounded real activation derivatives and Gaussian first weights.

Apply (27) conditionally to H=f_n(t,v)-f_n(s,v'). Equations (23)--(26)
and ||delta||_(2,n)<=CS give

\[
\left\|\mathbf1_{E_n}
 [Z_n(t,v)-Z_n(s,v')]\right\|_{L^p(F,G)}
 \le C_p S\big(|\tau(t)-\tau(s)|+\|v-v'\|_2\big)^{1/2}.
\tag{28}
\]

The term from E^T(v-v') in (26) costs at most CS||v-v'||; this is
absorbed into the displayed one-half power on the compact index set.
Centering is conditional on F throughout; it has not been replaced by an
unconditional population mean.

Here is the elementary chaining step. The index space [0,1] times
S^(d-1), in the metric |tau-tau'|+||v-v'||, has 2^(-j) nets with
at most C_d 2^(j(d+1)) points. Fix one p>2(d+1). Connect each net point
to a nearest parent in the preceding net. Equation (28) and
||max_i |X_i|||_p <= (sum_i||X_i||_p^p)^(1/p) bound the scale-j maximum
increment by

\[
C_p S\,2^{-j/2}2^{j(d+1)/p}.
\]

Its sum is finite, independent of n. At time zero Z_n is identically
zero; a finite coarse net and (28) bound the base values. The actual
sample paths are continuous through t=infinity, by parameter convergence
and bounded gates; conditional means are continuous by dominated
convergence using |f_n|<=CBS. Thus telescoping extends from the countable
nets to the full domain and proves

\[
\left\|\mathbf1_{E_n}\sup_{t\in[0,\infty],\,v\in S^{d-1}}
                  |Z_n(t,v)|\right\|_{L^p}\le C_p S.
\tag{29}
\]

Markov and Pr(E_n^c)=o(1) give strict C_(data,xi)/sqrt(n) uniform
conditional-mean replacement. By (6), the conditional mean depends on
v only through U^T v and ||E^T v||. It is the same for v and its folded
query (4). The triangle inequality proves (5).

## 7. Counted compression consequence

Set D=min(d,r+1). If r+1<d, restrict the actual initialized dense model
to the orthonormal subspace [U,e]. The restricted first matrix
A(0)[U,e] has exactly the canonical D-dimensional Gaussian law, on the
same realization; all hidden matrices, readout, residuals, training data
inner products, gamma, and physical training paths are unchanged.
Apply the existing compression theorem in that D-dimensional subspace.
At runtime use the fixed query map

\[
v\longmapsto\left(U^\top v,
                \sqrt{\|v\|_2^2-\|U^\top v\|_2^2}\right).
\tag{30}
\]

The radicand is nonnegative. The user-authorized representation change
allows this explicit norm operation. Store U in dr coordinates, plus
O(d+r) work coordinates. The construction retains no original-width
matrix or trajectory. Combining (5) and the restricted compression error
by a union bound preserves strict root-width whole-sphere accuracy at
all physical times, including the fitted endpoint.

In particular its retained size is bounded by

\[
\beta^{84LD}(D+3)^D(m/\gamma)^2[\log(en)]^{3D+2}
       +10m(D+1)+Cdr+C(d+r).
\tag{31}
\]

If original training inputs are retained too, the harmless data term can
instead be 10m(d+1). The sharper factorial coefficient from the inherited
theorem can be substituted with D in place of d. If r+1>=d, use its
original d-dimensional construction and omit the projection. When r=d
there are no passive directions. This gives a strict-root-width result
with D in place of the ambient d in the costly source coefficient and
logarithmic exponent; it gives no improvement when the training span is
already full-dimensional.

The additional folding error constant in (5) is not explicitly optimized.
In particular (31) is not a claim that every other dependence on ambient
d disappears. It changes the source representation dimension without
weakening the width rate, query domain, time interval, or same-realization
comparison.

## 8. Claim status and audit targets

The exact training restriction and Gaussian conditioning were already
proved in the earlier route. The new mathematical chain is:

1. One Hilbert--Schmidt query endpoint and h+1 training factors give the
   summable trace (13), under the existing label restriction.
2. Adding passive backward observables to the stopped insertion graph
   gives (18) and the fixed-query empirical moments (19).
3. Bounded changed gates plus carrier fourth moments give the one-half
   Hölder increment (28); no differentiated query jets are required.
4. Finite-dimensional chaining at any fixed p>2(d+1) gives (29), then
   strict root-width folding and the counted construction (31).

The candidate's most consequential audit target is Step 2, specifically
all direct query observable sources in (16)--(17), the query-cap survival
argument, and separation of the F-measurable training event from the
arbitrarily small polynomial local exceptional probabilities. Step 1's
Hölder exponents differ from both previous symmetric and forward-endpoint
choices. Steps 3--4 explicitly avoid the old incorrect deterministic
Lipschitz-family lemma: the finite query carrier moments are new neural
information, and a one-half power is enough with a large fixed p.

No generic lower bound is contradicted. The old whole-feature source
obstruction still applies to approximating every first-layer feature.
Here one compares scalar outputs first and compresses only the restricted
realization. No population limit, Gaussian average of each nonlinear
layer, supplied trained snapshot, or hidden retained dense state is used.
