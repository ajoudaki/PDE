# Restricted structured theorem: diagonal plus fixed rank

Internal theoretical result, 2026-09-26. This result concerns the declared
restricted class below. It does **not** resolve the study's primary candidate
with independent central signs. No experiments or external research inputs are
used. All statements below concern the fixed response-memory order `P` system
in the study README, rather than an untruncated memory limit.

## Statement and exact construction

Fix input dimension `d`, sample count `m >= 1`, memory order `P >= 1`, rank
`r >= 0`, data `(u_a,y_a)` with `|u_a|_2 <= 1`, and finite constants
`C_0,S,M`. Let

\[
 W_0=\operatorname{diag}(s_i)+\frac1nUV^\top,
 \qquad |s_i|\le S,\quad |U_{i\ell}|,|V_{i\ell}|\le M.
\]

Assume `|c_i(0)| <= C_0`; impose no pointwise bound on `w_i(0)`. The initial
memory is the one in the README: `L(0)=1`, `A_k(0)=0`,
`B_{0a}(0)=tanh(w(0) dot u_a)`, and `B_k(0)=0` for `k>0`.
The initial seed law is

\[
 \lambda_n=\frac1n\sum_{i=1}^n
  \delta_{(w_i(0),c_i(0),s_i,U_i,V_i)}.
\]

The same construction applies to every probability seed law `lambda` with a
finite first moment in `w`, supported on these bounds for the other
coordinates. Empirical weights may be arbitrary nonnegative weights summing
to one. Write `mu_0` for its lift to the prescribed initial memory.

For every finite `T`, the construction below has a unique solution on `[0,T]`.
Its finite-time bounds and stability constants depend only on
`T,d,m,P,r,C_0,S,M` and the data; they do not depend on `n`, the maximum initial
first-layer weight, or future information. It has the following properties.

1. For `lambda_n`, its `n` characteristics reproduce exactly the README ODE.
2. For any two admissible seed laws, their evolved laws and common scalar
   `L` are Lipschitz in their initial Wasserstein distance, uniformly on
   `[0,T]`. This controls outputs uniformly on the entire unit ball, hence on
   the unit circle when `d=2`, and controls the training loss.
3. Quantizing the seed law gives a finite autonomous scalar ODE with
   `K` weighted characteristics and no retained width-sized array or matrix
   oracle. Its error tends to zero for every seed law with a finite first
   moment. A uniform `p`th moment bound, `p>1`, gives an explicit polynomial
   error versus retained scalar count.
4. The Gaussian initialization in the README satisfies the hypotheses and a
   width-independent second-moment quantization bound with any prescribed
   high probability. Gaussian first-layer tails are not an unresolved
   trajectory-compactness assumption.
5. Every sequence of admissible seed laws converging in `W_1` has the
   corresponding compact-time law, output, and loss limit.

Here and below `W_1` uses the sum of absolute differences in all scalar state
coordinates. In particular `w` uses its `ell^1` norm.

The local characteristic state and fixed marks are

\[
 x=(w,c,(A_{kb},B_{kb})_{0\le k<P,1\le b\le m},s,U,V),
 \qquad w\in\mathbb R^d.
\]

Let `mu` be its probability law; brackets mean integration against `mu`, and
put `alpha_k=2(2k+1)/(mL)`. For **every** test input `u` with `|u|_2<=1`, set

\[
 h_u(x)=\tanh(w\cdot u),\qquad
 z_u(x)=s h_u(x)+\sum_{\ell=1}^rU_\ell\langle V_\ell h_u\rangle
       -\sum_{k,b}\alpha_k A_{kb}\langle B_{kb}h_u\rangle,
 \qquad F_u(\mu,L)=\langle c\tanh z_u\rangle.
 \tag{1}
\]

For training input `u_a`, use subscripts `a` and define

\[
 r_a=F_{u_a}-y_a,\qquad
 \rho=\left(m^{-1}\sum_a r_a^2\right)^{1/2},\qquad
 d_a(x)=c(1-\tanh^2 z_a(x)),
\]

\[
 t_a(x)=s d_a(x)+\sum_{\ell=1}^r V_\ell\langle U_\ell d_a\rangle
             -\sum_{k,b}\alpha_k B_{kb}\langle A_{kb}d_a\rangle.
 \tag{2}
\]

The autonomous characteristic equations are

\[
 \begin{aligned}
 \dot w&=-\frac2m\sum_a r_a(1-h_a^2)t_a u_a,\\
 \dot c&=-\frac2m\sum_a r_a\tanh z_a,\\
 \dot A_{ka}&=r_a d_a-\frac\rho L
       \left[kA_{ka}+\sum_{j<k}(2j+1)A_{ja}\right],\\
 \dot B_{ka}&=\rho h_a-\frac\rho L
       \left[kB_{ka}+\sum_{j<k}(2j+1)B_{ja}\right],\\
 \dot s&=\dot U=\dot V=0,\qquad \dot L=\rho.
 \end{aligned}
 \tag{3}
\]

The law `mu_t` is the pushforward of `mu_0` by these characteristics; `L` is
one shared scalar, not a coordinate independently averaged over particles.
For a weighted atomic law, every bracket in (1)--(3) is the corresponding
finite weighted sum.

**Exactness, including transpose.** For an empirical law with weights `1/n`,
(1) is coordinate `i` of `W h_u` after substituting

\[
 W=W_0-\frac2{mnL}\sum_k(2k+1)A_kB_k^\top.
\]

Equation (2) is coordinate `i` of `W^T d_a`. In particular its marks `U,V`
and memory coordinates `A,B` are interchanged. Multiplication by
`1-h_a^2` and substitution into the README equations give (3), including
all factors of `m,n,L`. Thus this is a representation of the same realized
system, not a new evolution inferred from entrywise distributional matching.

## Finite-time bounds without a bound on initial `w`

The following bounds also hold when the initial memory has arbitrary uniform
bounds `|A_{ka}(0)|<=A_0`, `|B_{ka}(0)|<=B_0`. This slightly larger class is
useful for stability and restartability. Set

\[
 \begin{aligned}
 Y&=\max_a|y_a|,& C&=(C_0+Y)e^{2T}-Y,& R&=C+Y,\\
 Q&=P^2,& E&=e^{RQ T},&
 A&=(A_0+RC T)E,\\
 B&=(B_0+R T)E,& \Lambda&=1+RT,&
 H&=S+rM^2+2P^2AB.
 \end{aligned}
 \tag{4}
\]

For `0<=t<=T`,

\[
 |c|\le C,\quad |A_{ka}|\le A,\quad |B_{ka}|\le B,
 \quad 1\le L\le\Lambda,
 \quad \|w(t)-w(0)\|_1\le2\sqrt d\,TRCH.
 \tag{5}
\]

These are support bounds for a law, not bounds holding only on average.
For the prescribed initial memory take `A_0=0,B_0=1`.

To prove them, first `|F_{u_a}|<=||c||_infinity`, so
`|r_a|,rho <= ||c||_infinity+Y`. The equation for `c` gives

\[
 \|c(t)\|_\infty\le C_0+
  2\int_0^t(\|c(s)\|_\infty+Y)\,ds.
\]

Iteration of this integral inequality gives
`||c(t)||_infinity <= (C_0+Y)e^{2t}-Y`. This argument applies to the essential
supremum over characteristics by taking suprema after the pointwise integral
bound. The initial local solutions have bounded `c`; the bound prevents exit.
Integrating `dot L=rho` gives the bound on `L`, including its lower bound.
For every `k<P`,

\[
 k+\sum_{j<k}(2j+1)=k+k^2\le P^2.
\]

Since `|d_a|<=C`, the integral inequalities for the largest absolute memory
coordinate have forcing at most `RC` and `R`, respectively, and linear
coefficient at most `RQ`. Iterating them, or multiplying their scalar upper
comparison ODEs by `e^{-RQt}`, yields the (slightly loose) bounds `A,B` in
(4), also when `R=0`. Finally (2) gives

\[
 |t_a|\le C\left(S+rM^2+
       \frac2{mL}\sum_{k,b}(2k+1)AB\right)\le CH.
\]

Because `||u_a||_1<=sqrt(d)`, the first equation of (3) gives the last bound
in (5). No step bounded `|w(0)|` or `|w(t)|`. In particular a finite first
moment remains finite, and a finite `p`th moment remains finite, by bounded
displacement. These estimates apply on each finite `T`; no uniform-in-time
claim is being made.

## A complete Lipschitz certificate and existence argument

On the domain specified by (5) and the fixed mark bounds, use the distance

\[
 D((x,\mu,L),(x',\nu,L'))
   =\|x-x'\|_1+W_1(\mu,\nu)+|L-L'|.
\]

There is a finite, explicitly computable constant `K_T`, independent of all
initial first-layer weight magnitudes, such that the local vector field `v`
in (3) and scalar vector field `rho` satisfy

\[
 \|v(x,\mu,L)-v(x',\nu,L')\|_1
       \le K_T D((x,\mu,L),(x',\nu,L')),
 \qquad
 |\rho(\mu,L)-\rho(\nu,L')|
       \le K_T\{W_1(\mu,\nu)+|L-L'|\}.
 \tag{6}
\]

Here is a finite arithmetic prescription for such a constant; it also
justifies its existence without a hidden compactness argument. Assign every
scalar expression a pair `(bound,Lipschitz constant)` under `D`. Constants
have pair `(|a|,0)`; the coordinates `c,A,B,s,U,V` have their bounds from
(4) and Lipschitz constant `1`. The function `h_u=tanh(w dot u)` has pair
`(1,1)` uniformly for `|u|_2<=1`, although `w` is unbounded. The reciprocal
`1/L` has pair `(1,1)`. Use the rules

\[
 \begin{array}{c|c}
 \text{expression}&\text{pair}\\ \hline
 g+h&(M_g+M_h,K_g+K_h)\\
 gh&(M_gM_h,M_gK_h+M_hK_g)\\
 \tanh g&(1,K_g)\\
 1-\tanh^2 g&(1,2K_g)\\
 \langle g\rangle&(M_g,2K_g).
 \end{array}
 \tag{7}
\]

For the last rule, couple `mu,nu`, apply the pointwise Lipschitz inequality,
and integrate: the local displacement costs at most `K_g W_1`, and the
explicit law and `L` dependence costs at most
`K_g(W_1+|L-L'|)`. This proves the stated rule, including for expressions
with nested moments. The norm map
`(r_a) -> (m^{-1}sum r_a^2)^{1/2}` is `1`-Lipschitz from the maximum norm:
this is the triangle inequality for the Euclidean norm divided by `sqrt(m)`.
Thus a common residual Lipschitz constant is valid for `rho`, including at
`rho=0`, where differentiability is unnecessary. Apply (7) to (1)--(3),
taking the sum of coordinate constants for the vector field and its maximum
with the constant for `rho`. This gives `K_T`. For coordinates of `dot w`,
`u_a` is a fixed coefficient of absolute value at most `1`; the unbounded
expression `w dot u` never occurs outside its displayed bounded tanh.
The same calculation supplies a finite `O_T` with

\[
 |F_u(\mu,L)-F_u(\nu,L')|
 \le O_T\{W_1(\mu,\nu)+|L-L'|\},\qquad |u|_2\le1.
 \tag{8}
\]

The arithmetic prescription is part of the certificate: it depends on a
fixed finite expression tree of size determined by `d,m,P,r` and never on
`n` or a trajectory oracle.

For completeness, existence for arbitrary laws can be constructed directly.
Fix `T` and temporarily clip all bounded state arguments to a box strictly
larger than (5), clip marks to their allowed intervals, and replace `1/L` by
the reciprocal of `L` clipped to `[1,Lambda+1]`. Do not clip `w`. In the
clipped formula, `v` and `rho` are globally bounded and Lipschitz in the
metrics in (6); clipping is `1`-Lipschitz and (7) applies. Starting from an
initial random variable `X_0` of law `mu_0`, use the iterations

\[
 X^{j+1}_t=X_0+\int_0^t v(X^j_s,\mathop{\rm Law}(X^j_s),L^j_s)\,ds,
 \qquad L^{j+1}_t=1+\int_0^t\rho(\mathop{\rm Law}(X^j_s),L^j_s)\,ds.
\]

Take `X^0_t=X_0,L^0_t=1`. Boundedness gives a finite first difference.
Inequality (6), and the coupling provided by the same `X_0`, bound each
successive difference in `sup_{s<=t} E||X_s-X'_s||_1+sup_{s<=t}|L_s-L'_s|`
by a constant times the integral of the preceding difference. Iteration
gives a bound of the form `M(3K)^j T^{j+1}/(j+1)!`; its sum is finite. Hence
the iterates converge in this complete space, and Lipschitz continuity
allows passage through the time integrals. They define a solution. Applied
to two solutions, the same integral estimate and its iteration force their
difference to vanish if they have the same initial data.

The clipping is inactive: until any first exit from the larger box, the
solution solves the original equations, so (4)--(5) keep every bounded
coordinate strictly inside that box. The lower edge `L=1` cannot be crossed
because `rho>=0`. Taking the essential supremum in the integral estimates
also rules out exit by a subset of characteristics before a common exit
time. Thus the constructed solution solves (1)--(3) on `[0,T]`. Repeating
for arbitrary `T` and using uniqueness gives the asserted global solution.
The characteristic construction also makes the pushforward definition
precise. It uses only finite first moments, not compact support in `w`.

## Width-independent stability and observables

Consider two such solutions with the same data and the same uniform bounds.
Couple their initial laws, and evolve each member of the pair by its own
characteristic equation. Write

\[
 e(t)=\mathbb E\|X_t-X'_t\|_1,\qquad \ell(t)=|L_t-L'_t|.
\]

The evolved pair is a coupling, so `W_1(mu_t,nu_t)<=e(t)`. Integral (6)
gives

\[
 e(t)+\ell(t)\le e(0)+\ell(0)
       +3K_T\int_0^t(e(s)+\ell(s))\,ds.
\]

Iteration yields

\[
 \sup_{0\le t\le T}\{W_1(\mu_t,\nu_t)+|L_t-L'_t|\}
 \le e^{3K_TT}\{W_1(\mu_0,\nu_0)+|L_0-L'_0|\}.
 \tag{9}
\]

One can first use a coupling within any positive tolerance of the infimum
and then let that tolerance decrease; no existence theorem for an optimal
coupling is needed. In the seed-law construction both initial `L`s equal
`1`. The lifting map is `(1+m)`-Lipschitz: the only new nonconstant
coordinates are the `m` entries `B_{0a}=tanh(w dot u_a)`, whose total
variation is at most `m||w-w'||_1`. Consequently the right side of (9) is
at most `(1+m)e^{3K_TT}W_1(lambda,lambda')`.

The unhalved training loss is `mathcal L=mean_a(F_{u_a}-y_a)^2`. Equations
(8)--(9), and `|r_a|<=R`, give

\[
 \sup_{t\le T,\ |u|_2\le1}|F_u(\mu_t,L_t)-F_u(\nu_t,L'_t)|
 \le O_Te^{3K_TT}W_1(\mu_0,\nu_0),
 \tag{10}
\]

\[
 \sup_{t\le T}|\mathcal L(t)-\mathcal L'(t)|
 \le 2R O_Te^{3K_TT}W_1(\mu_0,\nu_0).
 \tag{11}
\]

These are simultaneous bounds over the uncountable test-input ball; no
finite input net or bound on `max_i|w_i|` is required. The derivative of the
output with respect to the input is not the observable being controlled.

## Quantization, retained storage, and provenance

The seed dimension is

\[
 q=d+2+2r.
\]

The memory coordinates do not enter this dimension because they are
initialized by the displayed Lipschitz lifting map. Let
`R_0=max(1,C_0,S,M)` and take a clipping radius `R_w>=R_0` and an integer
`J>=1`. Clip each coordinate of `w` to `[-R_w,R_w]`. Round every seed
coordinate to a nearest node of the uniform `J`-interval grid in
`[-R_w,R_w]`; project the rounded bounded coordinates back to their allowed
intervals. Projection cannot increase their rounding error. The resulting
map `Q` has at most `(J+1)^q` values and satisfies

\[
 W_1(\lambda,Q_\#\lambda)
 \le \frac{qR_w}{J}
    +\int\|w\|_1\mathbf1_{\{\|w\|_1>R_w\}}\,d\lambda.
 \tag{12}
\]

Indeed the rounding error per coordinate is at most `R_w/J`, and coordinate
clipping costs at most the displayed tail integrand. For a finite first
moment this tail tends to zero by its definition as the tail of an
integrable nonnegative function. Taking `R_w` large and then `J` large
proves arbitrary accuracy, with no moment stronger than the first. For a
uniform rate suppose

\[
 \int\|w\|_1^p\,d\lambda\le M_p,\qquad p>1.
\]

The tail in (12) is at most `M_p R_w^{1-p}`. Set
`R_w=R_0 J^{1/p}` to obtain

\[
 W_1(\lambda,Q_\#\lambda)
 \le \left(qR_0+M_pR_0^{1-p}\right)J^{-(p-1)/p}.
 \tag{13}
\]

Lift the quantized seeds to their own initial memory and solve the weighted
atomic equations (1)--(3). Equations (9)--(11) hold with initial state error
at most `(1+m)` times (12) or (13). This is the complete deterministic error
certificate, with no future reference forcing or unproved truncation
residual. All approximation error is produced by the initial quantization;
the autonomous dynamics propagate that error by (9).

For `K<= (J+1)^q` occupied grid cells, retain only:

- `K` weights summing to one;
- `K(d+1+2Pm)` evolving scalar coordinates `w,c,A,B`;
- `K(1+2r)` fixed scalar marks `s,U,V`;
- the common scalar `L`;
- the fixed training data, `P,r`, and numerical coefficients in (1)--(3).

Thus the retained scalar count, including all fixed marks and weights, is

\[
 N_{\rm store}=1+K(d+3+2Pm+2r)+m(d+1)+O(1).
 \tag{14}
\]

Temporary sums in evaluating the vector field have size depending on
`K,m,P,r`, not `n`; they can be recomputed from the retained state. Evaluation
of an arbitrary test input uses (1) on this same state. No array of the
original `n` neurons, initialized matrix, Walsh operator, or input-indexed
future trajectory is retained. A one-pass initial histogram computes the
weights from realized initial seeds; original seeds may then be discarded.
Representatives, including their marks, are grid values, not encodings of
omitted neurons. Exact empirical histogram weights have denominator `n`. Even this dependence
of their bit representation on width can be removed: for any integer `D`,
round down each of the first `K-1` weights to a multiple of `1/D`, and assign
the remaining mass to the last weight. The new weights are nonnegative,
sum to one, and have total variation distance at most `K/D` from the old
ones. Since the quantized seed support has diameter at most `2qR_w`, coupling
common masses and then the remaining masses gives the additional initial
seed error

\[
 W_1(Q_\#\lambda,\widehat\lambda)\le 2qR_wK/D.
 \tag{15a}
\]

Taking `D=ceil(2qR_w K J^{(p-1)/p})` makes this at most
`J^{-(p-1)/p}`. Under the choice in (13), this denominator is at most a
constant times `(J+1)^{q+1}`. Thus stored weight precision can be chosen
independently of `n`, with only `O(log J)` bits per weight at fixed problem
parameters, and the same convergence exponent. Intermediate initial
histogram counters may use `log n` bits and are discarded. Grid
representatives are prescribed functions of `J,R_w` and the fixed bounds;
they do not encode the omitted initial array. The theorem remains a
real-arithmetic ODE and does not claim a discretized-time solver or a full
floating-point complexity bound. All finite-precision weight error is
explicitly included by (15a).

For fixed structural parameters, (13)--(14) give error
`O(N_store^{-(p-1)/(pq)})` along the prescribed grid hierarchy (or using its
worst-case scalar budget). The output/loss constants are precisely the
factors in (10)--(11) and the lifting factor. This polynomial exponent is
not claimed optimal. The grid ODE can be restarted from any current finite
state: weights and marks remain fixed, and `w,c,A,B,L` are its complete
current dynamical state. If restarted at a time with `L_0>1`, the same proof
uses `Lambda=L_0+RT`; the lower bound `L>=1` and every other estimate remain
valid.

## Gaussian initialization: explicit probability statement

For any width `n>=1`, let the `d` entries of each `w_i(0)` be independent
standard Gaussians, and let `c_i(0)=g_i/n`, with each `g_i` standard Gaussian.
The static marks may be any realization within their deterministic bounds;
the estimates below do not require independence between marks and initial
weights. Fix `0<eta<1`, and define

\[
 C_\eta=\max\left(1,\sqrt{2\log(4/\eta)}\right),
 \qquad M_{2,\eta}=\frac{2d^2}{\eta}.
 \tag{15}
\]

The Gaussian tail bound `P(|g|>a)<=2e^{-a^2/2}` follows by applying Markov's
inequality to `e^{tg}` with `E e^{tg}=e^{t^2/2}`, choosing `t=a`, and treating
the two signs. Hence

\[
 \Pr\{\max_i|c_i(0)|>C_\eta\}
 \le2n e^{-n^2C_\eta^2/2}\le2e^{-C_\eta^2/2}\le\eta/2.
 \tag{16}
\]

The middle inequality uses `log n <= (n^2-1)/2` for `n>=1` and
`C_eta>=1`; this inequality follows by differentiating its two sides as
functions of real `n>=1`. Also
`||w||_1^2 <= d||w||_2^2`, so `E||w||_1^2<=d^2`. Applying Markov to the
empirical average gives

\[
 \Pr\left\{\frac1n\sum_i\|w_i(0)\|_1^2>M_{2,\eta}\right\}
 \le\eta/2.
 \tag{17}
\]

With probability at least `1-eta`, simultaneously (16)--(17) fail to occur.
On this event all preceding conclusions hold with
`C_0=C_eta,p=2,M_p=M_{2,eta}`. In particular a single grid resolution chosen
from `T,eta,d,m,P,r,S,M`, the data, and the desired accuracy works with the
stated probability at **every fixed width**, with complexity independent
of width and uniform error for all `t<=T` and all `|u|_2<=1`.
This quantifier does not claim that one event has probability `1-eta`
simultaneously over an unspecified coupling of infinitely many widths.
The actual finite realization can also be certified deterministically by
using its computed initial `max|c_i|` and empirical moment in (4), (13).
No Gaussian maximum bound for `w_i` is used anywhere.

## Arbitrary empirical laws and their limit

Let `lambda_j` be any sequence of empirical seed laws (widths and weights
arbitrary), with the same deterministic bounds on `c` and static marks,
and suppose `W_1(lambda_j,lambda_infinity)->0`, where the limiting law has
a finite first moment. The lifting inequality and (9) show

\[
 \sup_{t\le T}\left[W_1(\mu^j_t,\mu^\infty_t)
          +|L^j_t-L^\infty_t|\right]\longrightarrow0.
\]

Equations (10)--(11) give uniform convergence of the entire input-ball
output and of the loss. This identifies the limit with the unique law
solution (1)--(3), rather than merely with some subsequential observable.
Quantization and width limits commute whenever their initial `W_1` errors
tend to zero, by the same estimate. No convergence of empirical marks is
assumed without saying so: if initial empirical seed laws have different
limits, the theorem supplies their corresponding different law solutions.

## The Walsh special case and the boundary of the result

Let `n=2^b` and let `H` be the normalized symmetric Walsh matrix, so
`H_ij=epsilon_ij/sqrt(n)` with `epsilon_ij` a sign and `H^2=I`. Let `D_1,D_3`
be arbitrary sign diagonals. If the central sign diagonal has exactly the
fixed `r` exceptional negative signs at indices `j_1,...,j_r`, then

\[
 D_2=I-2\sum_{\ell=1}^r e_{j_\ell}e_{j_\ell}^\top,
\]

\[
 D_1HD_2HD_3
 =D_1D_3-\frac2n\sum_{\ell=1}^r
       (D_1\epsilon_{\cdot j_\ell})
       (D_3\epsilon_{\cdot j_\ell})^\top.
 \tag{18}
\]

Thus take `s_i=(D_1)_ii(D_3)_ii`,
`U_iell=-2(D_1)_ii epsilon_i,jell`, and
`V_iell=(D_3)_ii epsilon_i,jell`; the theorem applies with `S=1,M=2`.
The initialized matrix remains orthogonal and full rank, since every factor
in (18) is orthogonal. The construction has a diagonal local action and a
fixed number of nonlocal modes; full rank alone does not prevent this
compression. For this Walsh subclass one may preserve the finite mark
alphabet exactly in quantization, improving constants and the grid
exponent, but (13) already proves a width-independent polynomial rate.

With genuinely independent central signs, the number of negative signs is
not a fixed parameter as width increases. Substitution in (18) then makes
`r`, the seed dimension, and retained storage scale with width. The proof
above therefore supplies neither the desired primary independent-sign
theorem nor a no-go result for it. Its complete conclusion is the explicit
restricted full-rank theorem stated at the beginning.
