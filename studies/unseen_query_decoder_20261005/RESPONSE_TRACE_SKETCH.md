# Gaussian sketches of total initialization-response traces

2026-10-06. Scoped theoretical continuation. Internal partial results;
no experiments, promotion, maintained-source edits, or Git operations.

An independent Gaussian matrix probe estimates the **total derivative
trace with respect to one dense initialization block** with near-root
absolute error. Its variance is $O(B^2A^2/n)$ when the two vector
sources have RMS at most $B$ and root Jacobian operator norms at most
$A$. The same probes give a simultaneous analytic-patch bound with a
logarithm of the number of patches. Neither the number of original
matrix entries nor a history-covariance inverse appears in that error.

There are two distinct storage conclusions. A finite predeclared panel
admits a static time-coefficient certificate with $O(\log^5 n)$
retained real numbers, after dense preprocessing and probe disposal.
Separately, the inherited coordinate-selection construction can represent
the original and probe mixers on finite augmented tangent-source spaces
with an absolute polylogarithmic coordinate count. The first is explicitly
time-indexed playback; the second is a source representation, whose
accurate autonomous tangent runtime still needs a comparison theorem.
Neither is offered as the requested late-query decoder.

## 1. Exact trace and probe identity

Let $G$ be the complete real Gaussian initialization root, and let
$M\in\mathbb R^{n\times n}$ be one standard-Gaussian hidden block.
Its physical initialized mixer is $W_0=M/\sqrt n$. At a fixed root
where the sources are differentiable, let
$c,h\in\mathbb R^n$ satisfy

\[
 \|c\|_2,\|h\|_2\leq B\sqrt n,
 \qquad
 \|D_Mc\|_{\rm op},\|D_Mh\|_{\rm op}\leq A.
\tag{1}
\]

The derivative domain in (1) is the matrix space with Frobenius norm.
Bounds for the complete-root derivatives imply these restricted bounds.
Write

\[
 \tau(G)=\frac1{n^{3/2}}
              \sum_{i,j}\partial_{M_{ij}}(c_i h_j).
\tag{2}
\]

This is an aggregate total derivative of the actual source maps. In a
trained network it includes their complete dependence on all intervening
parameters, residuals, and reused matrix actions. It is not an individual
partial derivative with respect to a Gaussian-history coordinate, and
is not asserted to equal an Onsager or regression coefficient.

Let $Z$ be an independent standard-Gaussian $n\times n$ matrix, sampled
independently of $G$, and define the tangent vectors

\[
 c_Z=D_Mc[Z],\qquad h_Z=D_Mh[Z],\qquad P=Z/\sqrt n.
\]

Then the probe statistic is

\[
 Q_Z=\frac{c_Z^TZh+c^TZh_Z}{n^{3/2}}
     =\frac{c_Z^TPh+(P^Tc)^Th_Z}{n}.
\tag{3}
\]

It uses forward and reverse actions of the same fixed probe matrix,
together with the two directional source derivatives. Conditional on
$G$, both $c_Z,h_Z$ are linear in $Z$. Thus $Q_Z$ is a Gaussian
quadratic form; its factors are not independent and are not treated
as independent in the following calculation.

Put $U(M)=ch^T$, and view
$\mathcal T=D_MU$ as a square linear operator on matrix space. For an
increment $V$,

\[
 \mathcal T[V]=(D_Mc[V])h^T+c(D_Mh[V])^T.
\tag{4}
\]

Its range is contained in
$\{u h^T+c v^T:u,v\in\mathbb R^n\}$, of dimension at most $2n$.
Moreover

\[
 \|\mathcal T\|_{\rm op}\leq2B\sqrt n A,
 \qquad
 \|\mathcal T\|_{\rm HS}^2
 \leq2\|h\|_2^2\|D_Mc\|_{\rm HS}^2
       +2\|c\|_2^2\|D_Mh\|_{\rm HS}^2
 \leq4B^2n^2A^2.
\tag{5}
\]

The last step uses the rank-at-most-$n$ Jacobians of the two vector
maps. The Hilbert--Schmidt bound is not obtained by multiplying an
$n^2$ output count by an uncontrolled coordinate derivative.

Vectorizing $Z$ gives $Q_Z=Z^T\mathcal T Z/n^{3/2}$. Consequently

\[
 \mathbb E_Z Q_Z=\operatorname{tr}\mathcal T/n^{3/2}=\tau(G).
\tag{6}
\]

Only the symmetric part $H=(\mathcal T+\mathcal T^T)/2$ contributes
to this quadratic form. It has the same trace and satisfies
$\|H\|_{\rm op}\leq\|\mathcal T\|_{\rm op}$ and
$\|H\|_{\rm HS}\leq\|\mathcal T\|_{\rm HS}$. In particular

\[
 \operatorname{Var}_Z(Q_Z\mid G)
       =2\|H\|_{\rm HS}^2/n^3
       \leq8B^2A^2/n.
\tag{7}
\]

Although $\mathcal T$ has rank at most $2n$, its symmetric part can
have rank as large as $4n$. The proof uses the norm inequalities above,
so it does not incorrectly retain the smaller rank after symmetrization.

## 2. Explicit high-probability bound

For a real symmetric matrix $H$ with eigenvalues $\lambda_i$,
$Z^THZ-\operatorname{tr}H$ has the law
$\sum_i\lambda_i(g_i^2-1)$. For
$|t|<(2\|H\|_{\rm op})^{-1}$, independence and the one-dimensional
Gaussian integral give

\[
 \log\mathbb E e^{t(Z^THZ-\operatorname{tr}H)}
 =\sum_i\left[-t\lambda_i-\tfrac12\log(1-2t\lambda_i)\right]
 \leq\frac{t^2\|H\|_{\rm HS}^2}
                  {1-2|t|\|H\|_{\rm op}}.
\tag{8}
\]

The inequality follows by summing the logarithm's power series and
bounding its terms of order at least two in absolute value. Exponential
Markov with
$t=\sqrt x/(\|H\|_{\rm HS}+2\|H\|_{\rm op}\sqrt x)$, and then
with $-t$, yields

\[
 \mathbb P\{|Z^THZ-\operatorname{tr}H|
       >2\|H\|_{\rm HS}\sqrt x+2\|H\|_{\rm op}x\}
       \leq2e^{-x}.
\tag{9}
\]

Degenerate zero norms are handled by continuity or directly. For $R$
independent probes let $\widehat\tau_R=R^{-1}\sum_{b=1}^R Q_{Z_b}$.
Apply (9) to the block diagonal matrix with $R$ copies of $H/R$,
then use (5). For every $x>0$,

\[
 \mathbb P_Z\left\{
 |\widehat\tau_R-\tau(G)|
   >4BA\left[\sqrt{\frac{x}{nR}}+\frac{x}{nR}\right]
                       \,\middle|\,G\right\}
       \leq2e^{-x}.
\tag{10}
\]

Thus a single probe already has the requested near-root scale whenever
$A=n^{o(1)}$ and $B=O(1)$. More probes reduce sampling error but
are not needed merely to obtain that order. For a finite list of $J$
source pairs or normalized jets, choosing $x=\log(2J/\eta)$ gives
a simultaneous error with conditional failure at most $\eta$.

These formulas require probes independent of the baseline initialization
and sources. Subsequent deterministic selection or compression may depend
on the probes; the probabilistic argument is then applied to the original
probe statistics, before that deterministic approximation. The selected
probe matrix itself is not asserted to have fresh iid entries.

## 3. Uniform analytic-patch version with the same probes

The current `SOURCE_SUPREMUM_EXTENSION.md` supplies the following actual
good-set properties for its specified source pairs: training features,
training backward fields or readout on one side, and a forward query
feature on the other, including initialized matrix images. On the common
complex time/query domain they have RMS at most $B=O(1)$ and good-root
Lipschitz constant

\[
 A_n=C(1+\sqrt{\ell_n})e^{C\sqrt{\ell_n}},
 \qquad\ell_n=\log(en).
\tag{11}
\]

The time range is $[0,T]$, $T=32(m/\gamma)\ell_n$, and the number
of half-radius product patches can be taken as
$N_n\leq C\ell_n^{3+d/2}$. Each patch has $k=d+1$ complex variables.
The source theorem excludes passive-query backward fields and
fitted-endpoint derivative traces. Those exclusions remain here.

Expand $c,h$ on one patch and multiply their coefficients by the outer
multi-radius powers. Denote the weighted coefficients by
$C_\alpha,H_\beta$. Cauchy's formula gives the same bounds $B\sqrt n$
and $A_n$ for every order. Coefficientwise derivative locality on the
common good set implies that, outside one null set, their actual root
Jacobians satisfy those operator bounds. This conclusion holds for every
coefficient, since there are only countably many coefficients and
finitely many patches at each width. Coefficient extraction commutes
with root differentiation by local smooth dependence on the safe compact
complex domain.

For complex coefficients, apply (9) separately to the real and imaginary
parts of their quadratic-form errors. Their real Jacobians have rank
at most $2n$; this changes only a numerical factor in (5). Consequently
there is a universal $C$ such that each coefficient-pair error obeys

\[
 |\widehat\tau_{R,\alpha\beta}-\tau_{\alpha\beta}|
 \leq CBA_n\left[\sqrt{\frac{x_{\alpha\beta}}{nR}}
                    +\frac{x_{\alpha\beta}}{nR}\right]
\tag{12}
\]

except with conditional probability $4e^{-x_{\alpha\beta}}$.
No independence between different coefficient errors is needed.

Use

\[
 x_{\alpha\beta}
 =x+\log(4N_n)+2k\log(4/3)
                  +(\log4)(|\alpha|+|\beta|).
\tag{13}
\]

Since $\sum_\alpha4^{-|\alpha|}=(4/3)^k$, a union over all
patches and the countable coefficient pairs has probability at most
$e^{-x}$. On that event, sum (12) with the half-radius weights
$2^{-|\alpha|-|\beta|}$. Their sum is $2^{2k}$; after normalization
their mean value of $|\alpha|+|\beta|$ is $2k$. Cauchy--Schwarz
for the square-root term and direct summation for the linear term give

\[
 \sup_{s,t\leq T,\,v\in S^{d-1}}
 |\widehat\tau_R(G;s,t,v)-\tau(G;s,t,v)|
 \leq C_d BA_n
   \left[\sqrt{\frac{x+\log(4N_n)+C_d}{nR}}
             +\frac{x+\log(4N_n)+C_d}{nR}\right]
\tag{14}
\]

with conditional probe probability at least $1-e^{-x}$ for almost every
good baseline root. The summable majorant proves uniform convergence of
the centered coefficient series, so the bound is genuinely simultaneous
on the continuum. The resulting series agrees with (3) minus (2) on
the common good set.

Setting $x=\log(1/\eta)$ and using $\log N_n=O_d(\log\ell_n)$
gives a whole-sphere sketch error of order

\[
 \frac{e^{C\sqrt{\ell_n}}\sqrt{\ell_n}}{\sqrt{nR}}
          \sqrt{1+\log\ell_n+\log(1/\eta)}
\tag{15}
\]

plus the smaller linear term in (14), with success at least
$1-\eta-o(1)$ after restoring the inherited good-root event. All
fixed-problem constants and the source's original label conditions
remain. The logarithm of the analytic patch count replaces the
square-root patch loss that would arise from a second-moment-only
argument. This remains an error theorem, not a probe storage theorem.

## 4. Probe tangents have controlled temporal source complexity

Fix a predeclared finite panel, including the training inputs. For
each probe, the directional derivatives of its required sources are
holomorphic on the original safe complex time domain: they are
derivatives of the analytic finite-dimensional ODE and analytic forward
or backward maps with respect to initial conditions.

Their size also follows from the available root Jacobian bounds, without
postulating a new trained tangent moment law. For a real coefficient map
$u$ with $\|D_Mu\|_{\rm op}\leq A_n$, conditional on the baseline root,
$u_Z=D_Mu[Z]$ is a centered Gaussian vector with covariance operator at
most $A_n^2I$ and covariance trace at most $nA_n^2$. Applying the
quadratic-form calculation to its squared norm gives, for instance,

\[
 \|u_Z\|_2\leq A_n(\sqrt n+\sqrt{2x})
\tag{16}
\]

except with probability $e^{-x}$. Complex coefficients have real output
dimension $2n$ and satisfy the same assertion with a numerical factor.

Apply (16) to normalized temporal coefficients, allocate exponentially
decreasing failure probabilities in their order, and sum on half-radius
disks. A finite time-patch cover supplies a slightly smaller rectangle
around $[0,T]$. For fixed confidence and a fixed number of probes, all
needed tangent feature, training backward, and readout curves therefore
have RMS at most $C A_n$ on that rectangle. The statement also permits
polylogarithmically many probes by including their count in the
logarithmic failure allocation. Since each coordinate is bounded by
the Euclidean norm, the coordinate envelope is at most

\[
 C\sqrt n\,(1+\sqrt{\ell_n})e^{C\sqrt{\ell_n}}.
\tag{17}
\]

The normalized Gaussian probe $P=Z/\sqrt n$ has a fixed operator-norm
cap with failure $e^{-cn}$. A direct proof uses fixed $1/4$-nets of
the two unit spheres, with at most $9^{2n}$ pairs, and the Gaussian
tail for $u^TPv$ of variance $1/n$. Choosing a sufficiently large
numerical cap absorbs that net count. Thus probe images and initialized
original-matrix images of these curves have the same type of envelope.

The finite-panel temporal approximation argument applies to any finite
list of holomorphic vector curves with this envelope; it does not require
them to solve the original nonlinear optimizer. If $r=c\ell_n^{-1/2}$
is the smaller time radius and $T=C\ell_n$, put
$\alpha=r/(4T)=c'\ell_n^{-3/2}$. The cosine substitution and contour
translation give a degree-$K$ coordinate tail at most
$4M_n\alpha^{-1}e^{-\alpha K}$, where $M_n$ is (17). For any
fixed $a>0$, accuracy $n^{-a}$ therefore needs only

\[
 K=O(\ell_n^{5/2}),
\tag{18}
\]

because $\log M_n=O(\ell_n)$. A subpolynomial factor in the tangent
amplitude changes the coefficient-accuracy requirement but not the
absolute exponent in (18). This proves a temporal source-rank count
for the probe tangents; it is not a tangent-runtime comparison.

## 5. A fully counted finite-panel static trace certificate

There is a concrete way to discard all dense probes for a predeclared
finite list of source pairs. It is useful to state it exactly, including
why it is not the desired autonomous decoder.

For each probe, approximate the curves $c,c_Z,h,h_Z$ on $[0,T]$ by
the degree-$K$ Chebyshev expansions above. Include the physical probe
images $Ph$ and $P^Tc$ or form them exactly from the computed source
coefficients. Choose their coordinate tolerance small enough that the
bilinear error in (3) is at most $n^{-a}$; for example
$\varepsilon=n^{-a}/[C(1+A_n)^2]$ suffices when all required RMS
and probe operator norms have the preceding bounds. Its logarithm is
still $O(\ell_n)$, so (18) is unchanged.

Writing $\mathsf T_j(2t/T-1)$ for the scalar Chebyshev polynomial,
precompute for each source pair the scalar table

\[
 B_{ij}=\frac1R\sum_{b=1}^R\frac1n
  \left[(c_{Z_b})_i^TP_bh_j
                   +c_i^TP_b(h_{Z_b})_j\right],
 \qquad 0\leq i,j\leq K.
\tag{19}
\]

Subscripts in (19) label time-polynomial coefficient vectors, not neuron
coordinates. Its evaluation is

\[
 \sum_{i,j=0}^K B_{ij}
       \mathsf T_i(2s/T-1)\mathsf T_j(2t/T-1).
\tag{20}
\]

After forming (19), discard every original-width source vector, tangent
array, initialized dense matrix, probe matrix, and quadrature/jet workspace.
The retained table has $(K+1)^2=O(\ell_n^5)$ scalar entries per
predeclared pair. The average over probes has already been taken, so
the number of retained table entries does not increase with $R$.
Sequential polynomial evaluation uses $O(K)$ live scalar workspace,
or less with recomputation, along with a time input and accumulators.
Its approximation error is at most $n^{-a}$ in addition to (10) or
the finite-panel specialization of (14).

This is a valid retained-coordinate and decoder-workspace count for
the specified scalar certificates. It permits substantial dense
preprocessing and requires the same finite activation/jet evaluation
interface as the inherited construction. The tables have explicit
finite-computation provenance and do not encode a dense array inside
one arbitrary real. The inherited source result counts real coordinates,
but these scalar tables also admit a direct bit count. On the real time
interval, a Chebyshev coefficient has Euclidean norm at most twice the
curve's supremum norm. Hence every entry in (19) has magnitude at most
$CBA_n$ on the preceding tangent and probe-norm event. Rounding each
entry to absolute accuracy
$n^{-a}/[4(K+1)^2]$ changes (20) by at most $n^{-a}/4$, since
$|\mathsf T_i|\leq1$ on $[-1,1]$. Each entry therefore requires
$O(\ell_n)$ bits, and the retained quantized table requires

\[
 O_{L,m,p}(\ell_n^6)\quad\hbox{bits}.
\tag{20a}
\]

The same $O(\ell_n)$ working precision suffices for evaluation after
increasing its constant. Indeed the recurrence for $\mathsf T_i$ has
rounding-error amplification at most $O(K^2)$ on $[-1,1]$: an error
inserted at one step propagates by a second-kind Chebyshev polynomial
of magnitude at most $K+1$, and there are at most $K$ insertion steps.
The $O(K^2)$ final terms and their magnitudes $O(BA_n)$ cost only
additional polynomial factors in $K$ and the subpolynomial $A_n$.
Input precision of the same order suffices because
$|\mathsf T_i'|\leq i^2$ there. Thus the evaluation uses
$O(K\ell_n)$ working bits, in addition to the retained table and the
stated-precision time input. This argument does not assert a bit-cost
bound for compiling the table from activation evaluations; a finite
precision implementation of those evaluations remains the preprocessing
interface. It does show that the retained scalar certificate itself
requires neither infinite precision nor a repeatable dense random tape.

However, (20) is a time-indexed compiled trace function. It is not an
autonomous evolving model, and it only covers the queries declared
before compilation. It therefore cannot be substituted for a decoder
contract that excludes trajectory playback or must answer later sphere
queries without a query-dependent source table. If preprocessing peak
memory is also counted, this construction has not reduced that peak.

## 6. Exact tangent equations and the augmented source list

Here is the dynamical alternative that would be needed to avoid the
static tables. Use a dot for physical-time derivative and a prime for
the directional derivative $D_M[Z]$. Primes in this section apply to
network quantities; activation derivatives remain explicit
$\phi_j',\phi_j''$.

For the baseline flow, $r_a=f_n(v_a)-y_a$. The forward and backward
tangent recursions are

\[
 (z_a^{(1)})'=A'v_a,\qquad
 (z_a^{(j)})'=(W^{(j)})'h_a^{(j-1)}
                     +W^{(j)}(h_a^{(j-1)})',\qquad
 (h_a^{(j)})'=\phi_j'(z_a^{(j)})\odot(z_a^{(j)})',
\tag{21}
\]

\[
 r_a'=\frac{(w')^Th_a^{(L)}+w^T(h_a^{(L)})'}n,
\]
\[
 (\delta_a^{(L)})'
   =\phi_L'(z_a^{(L)})\odot w'
       +\phi_L''(z_a^{(L)})\odot w\odot(z_a^{(L)})',
\]
\[
 (k_a^{(j)})'=((W^{(j+1)})')^T\delta_a^{(j+1)}
                         +(W^{(j+1)})^T(\delta_a^{(j+1)})',
\]
\[
 (\delta_a^{(j)})'
   =\phi_j'(z_a^{(j)})\odot(k_a^{(j)})'
       +\phi_j''(z_a^{(j)})\odot k_a^{(j)}\odot(z_a^{(j)})'.
\tag{22}
\]

Differentiating the actual mean-loss equations gives

\[
 \dot A'=-\frac2m\sum_a
       [r_a'\delta_a^{(1)}+r_a(\delta_a^{(1)})']v_a^T,
\]
\[
 \dot{(W^{(j)})'}=-\frac2{mn}\sum_a
  [r_a'\delta_a^{(j)}h_a^{(j-1)T}
       +r_a(\delta_a^{(j)})'h_a^{(j-1)T}
       +r_a\delta_a^{(j)}((h_a^{(j-1)})')^T],
\]
\[
 \dot w'=-\frac2m\sum_a
                   [r_a'h_a^{(L)}+r_a(h_a^{(L)})'].
\tag{23}
\]

Initially $A'=w'=0$, the targeted hidden block has
$(W^{(j_0)}(0))'=P$, and all other hidden tangent blocks are zero.
Thus a tangent matrix is its fixed probe initialization plus three
families of rank-one time integrals. It need not be retained as an
$n\times n$ array if its actions on the necessary vector-source spaces
can be represented and their approximate dynamics justified.

For a fixed panel and fixed probes, a sufficient finite list of vector
curves consists of baseline forward features and training backward
fields; their tangent versions; readout and tangent readout where needed;
the original initialized-matrix forward and reverse images of all these
applicable fields; and probe forward/reverse images of the baseline
fields needed in (21)–(23) and (3). For (3), using $P^Tc$ avoids
requiring $P h_Z$ as an additional source. Probe images of other probes'
tangents are not required for first directional derivatives.

The number of curves is $O_{L,m,p}(1+R)$, with $p$ the predeclared
panel size. Their time degree is (18). Include the original exact
initial additions and any required fixed probe-source image pairs.
The resulting per-layer source dimension is bounded by

\[
 D_{\rm src}=O_{L,m,p}((1+R)\ell_n^{5/2}).
\tag{24}
\]

All these statements concern vector sources, their linear initialized
images, and their time approximation. They do not claim that a
flattened tangent weight matrix is itself a source vector of small
dimension.

## 7. What coordinate selection supplies, and what it does not

The inherited finite-panel selection interface applies to arbitrary
finite source spaces: it gives restrictions $\mathcal R_j$, metrics
$M_j$, and $q_j\leq9D_{\rm src}$ such that restriction is an exact
isometry for the normalized dense pairing on each source space.
The same selected spaces can represent several fixed linear operators.

For any such operator $K$, including $W_0$ or a physical probe $P_b$,
let $P_{E_j}$ be the dense orthogonal projection onto the output
source space and $\Pi_{j-1}$ the selected metric projection onto the
restricted input source space. The selected operator is

\[
 K_C=\mathcal R_jP_{E_j}K
       (\mathcal R_{j-1}|_{E_{j-1}})^{-1}\Pi_{j-1}.
\tag{25}
\]

It has norm at most $\|K\|_{\rm op}$. When an input coefficient and its
$K$-image both belong to the source spaces, its forward image is exact.
Separately, when an output coefficient and its $K^T$-image both belong
to the corresponding source spaces, the metric adjoint gives the exact
reverse image. The proof
is the same finite-dimensional isometry/projection algebra as for the
original initialized mixer. Multiple fixed operators require more
retained selected matrices, not a new random-matrix theorem. A fixed
finite collection of cross-layer contractions can be included by using
its corresponding input and output source spaces.

Consequently one can discard all dense probes after constructing their
selected operators. A source representation retaining selected
coefficient vectors and the selected original/probe matrices has count
at most

\[
 O_{L,m,p}((1+R)D_{\rm src}^2)
    =O_{L,m,p}((1+R)^3\ell_n^5)
\tag{26}
\]

real coordinates, including metrics, selected coefficient arrays,
matrix copies, and vector/solve workspace of those dimensions. For
fixed $R$, the exponent is five. This does not hide an $n^2$ tangent
array: the retained matrices have dimensions $q_j\times q_{j-1}$.
Dense matrices and full-width coefficients may be used only during
preprocessing. Exact source-image pairing is preserved by computing
a coefficient and its image with identical scalar operations.

A candidate autonomous augmentation would retain the base compact
arrays and, for each probe, their first tangent arrays and tangent
residuals. Its moving-array count is
$O((1+R)[Lq^2+qd+m])$, within (26). Forward and backward tangent
evaluation needs $O((1+R)Lpq)$ buffers, also within that count.
This is a state inventory, not an accuracy theorem for that augmentation.

Three separate facts are not supplied by the selection argument:

1. The existing runtime is the corrected-readout optimizer. A uniform
   prediction comparison does not imply comparison of its directional
   derivatives with the dense gradient-flow derivatives. Differentiating
   an approximation error is not a valid substitute.
2. A direct comparison of the augmented equations must handle the terms
   with $r_a'$, tangent backward fields, changed gates times tangent
   carriers, and the differentiated readout correction. It needs stable
   propagation and a quantified source error. The original fitting and
   prediction comparison do not state that result.
3. The selected spaces and metrics can depend on the baseline root and
   probes. Holding them fixed defines one proposed tangent runtime;
   differentiating the full compiler would additionally differentiate
   that selection. Neither derivative is automatically the desired
   dense-root derivative. The target and construction must be specified
   before an identification claim.

The tangent sources' analytic rank count in Section 4 does not resolve
these dynamical issues. Nor does a training-only selection promise
accurate actions on a future query's new nonlinear feature vectors.
Extending the source spaces to all sphere queries through spatial
coefficients would reintroduce the dimension-dependent count that this
study is trying to avoid.

## 8. Retained-information accounting and precise outcome

| Construction | Retained information and live evaluation memory | Established scope |
|---|---|---|
| Original Gaussian probe estimator | A repeatable $n\times n$ probe plus dense source/tangent evaluator | Exact unbiasedness and bounds (10), (14) |
| Finite-panel scalar tables | $O_{L,m,p}(\log^5 n)$ real coefficients, or $O_{L,m,p}(\log^6 n)$ quantized bits; $O(K\log n)$ working bits; probes discarded | Static time-indexed trace approximation on the predeclared panel |
| Selected augmented source representation | $O_{L,m,p}((1+R)^3\log^5 n)$ real coordinates; only selected probe matrices retained | Finite source/action/pairing representation |
| Autonomous augmented tangent runtime | A candidate state fits the same count | Dense-tangent accuracy and late-query extension remain open |

A short seed is not silently substituted for an iid dense probe. The
two small retained representations instead compute only the needed
probe functionals during preprocessing and discard the unused directions.
Re-evaluating the original Gaussian quadratic form at arbitrary later
vectors would require those directions again; the finite-panel and
source-space guarantees do not permit that extra operation.

The trace estimate addresses (2), including both product-rule endpoint
responses. Extracting individual chronological response coefficients
from it would require a separate mathematical identity. If Gram
regression is proposed for that extraction, its conditioning and
prediction-energy stability require their own proof. The sketch lemma
does not close those obligations, and it does not identify the
unseen-query decoder.

## 9. Provenance

New authorized inputs read completely: the finite-panel study's
`RESULT.md`, `PANEL_SOURCE.md`, and `PANEL_RUNTIME.md`. Their SHA-256
hashes are respectively

`38ca06a2e812d8e2b45c6b7350c0437d710433b11a00b89aa66487a9229b028b`,

`ca1066cf168829bea642db013a4fbc24166b224df0731783a51b4c85e4fdbaed`,

`514d9e06cfd1cf23c496df0ece976812a39ea33f70112334c84326cfa0f0cd9f`.

The current-study source-supremum theorem and its full inputs were
already read in the preceding assigned audit. The integrated
`UNBOUNDED_COMPRESSOR_BRIDGE.md`, `ANALYTIC_TAIL_EXTENSION.md`, and
`GENERAL_DENSE_COMPARISON.md` remain the authorized source and fitting
interfaces. No linked other study or archived book was opened. The
Gaussian quadratic-form tail proof is included here; no unverified
external trace-estimation theorem is invoked.

Previously read rigorous-math and conjecture-audit instructions were
applied. The canonical-notation skill remained permission-inaccessible;
the maintained notation contract and supplied presentation rules were
used directly.
