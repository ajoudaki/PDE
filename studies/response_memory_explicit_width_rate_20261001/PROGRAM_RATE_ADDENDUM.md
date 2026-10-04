# Quantitative program route: explicit proxy bridge

This addendum supplements the frozen `PROGRAM_RATE_ROUTE.md`. It does not
change the model or the original candidate proof's quantitative lemma.
Its purpose is to make the remaining proxy-consistency bridge explicit.
All statements remain candidate results pending the coordinated audit.

## 1. Clarifications and a fixed instruction budget

The empirical test assertion means **absolute errors of empirical second
moments**, not squares of empirical errors. For example, the controlled
quantity is

\[
 \left|\frac1n\sum_i (|p_i|-M)_+^2
             -E[(|P|-M)_+^2]\right|.
\]

An error `u` in this quantity gives an error at most `sqrt(u)` in its square
root. Pairings have their absolute empirical-mean error controlled directly.

Let `K` be the number of Euler intervals. Count every ordinary vector
instruction, elementary memory-sum addition or multiplication if expanded,
added Gaussian root, added noisy-query sum, and initialized matrix or
transpose call. With at most `K` passive probes (only one is needed below),
choose a fixed constant `C_0` large enough and set

\[
 N=\lceil C_0 K^3\rceil.
 \tag{A1}
\]

The program may be padded with zero instructions to make this exact. The
clipping cutoff is this `N` and the query-noise amplitude is `exp(-N^2)`.
The number of independent conditional innovations is also at most `N`.
The separate list of scalar empirical tests contains at most `C N^2` tests:
all required pairings and squared norms, plus each carrier at each Euler
node tested at thresholds `M/2`, `1<=M<=N`, and at the one additional
comparison threshold `R/2`. Fixed factors in this test count are absorbed
in the constants of the quantitative lemma. Tests are observations, not
new matrix queries.

The exact choice (A1), rather than merely an upper bound on `N`, ensures
that the clipping bias `exp(-cN^2)` is small as `K` grows. All counts include
the fresh noise roots before the quantitative lemma is applied.

## 2. Polynomial probability of the original initialization event

Choose the constants defining the paper's event `G_n` with fixed strict
slack above the relevant deterministic RMS limits. Then

\[
 \Pr(G_n^c)\le C/n+C e^{-cn}.
 \tag{A2}
\]

For the initialized hidden operator norms, this is the Gaussian net bound
already displayed in the paper, with `K_0` chosen sufficiently large.
For the first-layer preactivation and full first-layer Frobenius bounds,
the squared RMS quantities are averages of iid random variables with finite
variance. Chebyshev at their fixed positive slack gives `C/n`.

Here is a fixed-tolerance argument for the initial Gram, including singular
intermediate covariances. Write `Q_l` for the deterministic uncentered
feature covariance and `Q_{n,l}=H_l^T H_l/n`. Let `F_l` be its Gaussian
covariance recursion. It is continuous on positive semidefinite matrices,
including singular matrices, as proved in the paper. Choose a terminal
Frobenius tolerance `delta_L<=m lambda`. Recursively choose positive fixed
`delta_{l-1}` sufficiently small that

\[
 \|Q-Q_{l-1}\|_F\le\delta_{l-1}
 \quad\Longrightarrow\quad
 \|F_l(Q)-Q_l\|_F\le\delta_l/2.
\]

On this fixed covariance neighborhood, all conditional Gaussian activation
fourth moments are bounded by a fixed constant because activation growth
is linear. Conditional Chebyshev and a union bound over the fixed `m^2`
entries give

\[
 \Pr\{\|Q_{n,l}-F_l(Q_{n,l-1})\|_F>\delta_l/2
              \mid Q_{n,l-1}\text{ in its neighborhood}\}\le C_l/n.
\]

At the first layer, the same statement is an ordinary iid fourth-moment
calculation. Summing these finitely many conditional failure probabilities
shows `||Q_{n,L}-Q_L||_op<=m lambda` except on an event of probability
`C/n`. As `Q_L/m>=2 lambda I`, this gives `Q_{n,L}/m>=lambda I`, proving
(A2). A numerical modulus of covariance continuity is unnecessary here:
all tolerances are fixed independently of width and of the reference mesh.

## 3. Reference fields, empirical oracle fields, and proxy parameters

Use the original population Euler program at times
`0=t_0<...<t_K=T`, with steps `h_k<=h`. Its deterministic residuals are
`r^o_{a,k}`. All its scalar contractions and residuals remain frozen in the
modified program. Write its scalar fields as
`H^o_{a,k}, Z^o_{a,k}, P^o_{a,k}, delta^o_{a,k}, w^o_k`.

Use lower-case sans hats `h^p,z^p,p^p,delta^p,w^p` for the vectors produced
by the **modified empirical oracle program** on the actual arrays. Thus its
gates are

\[
 \delta^{p,\ell}_{a,k}
    =g_\ell(z^{p,\ell}_{a,k})\odot
             \operatorname{clip}_N(p^{p,\ell}_{a,k}),
 \qquad p^{p,L}_{a,k}=w^p_k.
 \tag{A3}
\]

The fresh input noise occurs at every initialized matrix call. Its frozen
learned-memory coefficients use the original population expectations, not
empirical contractions and not the modified population expectations.

For a finite vector write `||v||_n=||v||_2/sqrt(n)`. Define the actual finite
proxy parameters by

\[
\begin{aligned}
 \widetilde w_k
   &=-\frac2m\sum_{r<k}h_r\sum_b r^o_{b,r}h^{p,L}_{b,r},\\
 \widetilde W^1_k
   &=W^1_0-\frac2m\sum_{r<k}h_r\sum_b
                   r^o_{b,r}\delta^{p,1}_{b,r}v_b^T,\\
 \widetilde W^\ell_k
   &=W^\ell_0-\frac2{mn}\sum_{r<k}h_r\sum_b
       r^o_{b,r}\delta^{p,\ell}_{b,r}(h^{p,\ell-1}_{b,r})^T,
       \qquad \ell\ge2.
\end{aligned}
\tag{A4}
\]

In particular `widetilde w_k=w^p_k`. For each interval, interpolate these
parameters affinely, with constant velocity `V^p_k` given by the corresponding
single Euler update in (A4) divided by `h_k`. This defines an actual finite
parameter path using the true initialized matrices.

The physical responses recomputed from (A4) will be denoted by tildes. They
use the original activation and the ordinary, **unclipped** backward pass.
They are not equated to the modified oracle fields.

## 4. The simultaneous quantitative oracle event

Apply the finite-program lemma with its pairing and tail tests. Enlarge
constants once and define

\[
 \xi=e^{C N^5}n^{-1/8}+C e^{-cN^2}.
 \tag{A5}
\]

Require `log n>=C N^5` and then increase the fixed width threshold so
`xi<=1`. Except on an event of probability

\[
 e^{C N^5}n^{-1/2}+C e^{-cn},
 \tag{A6}
\]

the following hold simultaneously.

1. Every required empirical pairing of modified oracle vectors differs from
   the corresponding **original** population expectation by at most `C xi`.
   This includes the forward `hh` contractions, reverse `delta delta`
   contractions, squared norms, and readout-feature prediction contractions.
2. Every training oracle response has normalized norm bounded by a fixed
   constant. More precisely, its norm differs from the corresponding
   original population norm by at most `C xi` when norms are among the
   tests. Hence feature norms are at most `C` and backward/readout norms at
   most `C Y+C xi`.
3. Every added Gaussian root has normalized norm at most two, and the
   initialized operator norms are at most `K_0`.
4. For every oracle training carrier and every selected threshold `M`,

\[
 \|(|p^{p,\ell}_{a,k}|-M/2)_+\|_n
      \le C e^{-cM^2}+C\xi.
 \tag{A7}
\]

To justify item 1, compare the empirical quantity first to the modified
population law by the quantitative lemma. Then compare its expectation
with the original law using the common-population `L^2` bias estimate and
Cauchy--Schwarz. The original scalar norms are uniformly bounded, and the
modified norms differ from them by at most `Ce^{-cN^2}`. No original finite
unclipped program concentration estimate is used.

For item 4, the empirical squared-tail test gives its norm with an error
bounded by the first term of (A5). The scalar positive-part norm changes by
at most the common-population `L^2` bias. The original population Gaussian
bound supplies the displayed exponential tail. In particular,

\[
 \|p^p1_{|p^p|>M}\|_n
 \le 2\|(|p^p|-M/2)_+\|_n
 \le C e^{-cM^2}+C\xi.
 \tag{A8}
\]

The comparison threshold `R` is selected in advance and included even if
it is not an integer. Take `1<=R<=N`; later `R` is of order `sqrt(log K)`.

The original population Euler program has total activity bounded by `CY`.
Consequently (A4), item 2, and the normalized outer-product identity give

\[
 \|\widetilde w_k\|_n\le C Y,
 \quad
 \|\widetilde W^1_k-W^1_0\|_F/\sqrt n
       +\sum_{\ell\ge2}\|\widetilde W^\ell_k-W^\ell_0\|_F
       \le C Y(Y+\xi).
 \tag{A9}
\]

These inequalities include harmless fixed data factors. For the theorem's
small fixed `Y`, and sufficiently small `xi`, all proxy nodes and their
affine interpolants remain inside a fixed physical tube. Their speeds obey

\[
 \|V^p_k\|_{\rm sum}\le C\rho^o_k\le C,
 \qquad
 d_n(\widetilde\theta(t),\widetilde\theta_k)\le C h.
 \tag{A10}
\]

If necessary use a slightly enlarged tube; its constants remain independent
of width, mesh, and time. The actual dense path is already controlled on
`G_n` by the existing all-time fitting proof.

## 5. Exact action discrepancies at mesh nodes

For a hidden forward action, let
`C^h_{br,ak}=E[H^{o,ell-1}_{b,r} H^{o,ell-1}_{a,k}]`.
The modified oracle instruction has the form

\[
 z^{p,\ell}_{a,k}
  =W^\ell_0(h^{p,\ell-1}_{a,k}+\epsilon\chi_{a,k})
    -\frac2m\sum_{r<k,b}h_r r^o_{b,r}
                \delta^{p,\ell}_{b,r}C^h_{br,ak}.
\]

Subtract this from the **true action of the proxy matrix on the oracle
feature**. The exact discrepancy is

\[
\begin{aligned}
 A^h_{a,k}
 &:=\widetilde W^\ell_k h^{p,\ell-1}_{a,k}
                                  -z^{p,\ell}_{a,k}\\
 &=-\epsilon W^\ell_0\chi_{a,k}
   -\frac2m\sum_{r<k,b}h_r r^o_{b,r}\delta^{p,\ell}_{b,r}
       \left\{\frac{(h^{p,\ell-1}_{b,r})^T
                       h^{p,\ell-1}_{a,k}}n-C^h_{br,ak}\right\}.
\end{aligned}
\tag{A11}
\]

Every brace is `O(xi)`, the time-weighted absolute residual sum is bounded
by `CY`, and the oracle vector norms are bounded. Therefore

\[
 \|A^h_{a,k}\|_n\le C\xi.
 \tag{A12}
\]

The first-layer oracle linear instruction agrees exactly with the proxy
first-layer action. A normalized passive query has precisely (A11), with
its features and its population contractions normalized by `s_x`; its
constants remain uniform in `x`.

For a hidden reverse action define
`C^delta_{br,ak}=E[delta^{o,ell}_{b,r}delta^{o,ell}_{a,k}]`.
The same subtraction gives

\[
\begin{aligned}
 A^p_{a,k}
 &:=(\widetilde W^\ell_k)^T\delta^{p,\ell}_{a,k}
                                  -p^{p,\ell-1}_{a,k}\\
 &=-\epsilon (W^\ell_0)^T\chi'_{a,k}
   -\frac2m\sum_{r<k,b}h_r r^o_{b,r}h^{p,\ell-1}_{b,r}
       \left\{\frac{(\delta^{p,\ell}_{b,r})^T
                       \delta^{p,\ell}_{a,k}}n-C^delta_{br,ak}\right\}.
\end{aligned}
\tag{A13}
\]

Hence `||A^p_{a,k}||_n<=C xi`. The fresh noisy inputs are explicitly
accounted for in (A11) and (A13); they are not discarded by a width limit.

## 6. Recomputed node responses and the node velocity defect

Subtract the ordinary proxy forward recursion from its oracle instruction:

\[
 \widetilde z^{\ell}_{a,k}-z^{p,\ell}_{a,k}
   =\widetilde W^\ell_k
          (\widetilde h^{\ell-1}_{a,k}-h^{p,\ell-1}_{a,k})
       +A^h_{a,k}.
\]

The first-layer difference is zero. Bounded proxy operator norms and the
activation slope bound yield, through the fixed depth,

\[
 \max_{\ell,a}
  (\|\widetilde z^\ell_{a,k}-z^{p,\ell}_{a,k}\|_n
   +\|\widetilde h^\ell_{a,k}-h^{p,\ell}_{a,k}\|_n)
       \le C\xi.
 \tag{A14}
\]

At a backward gate, write its subtraction in the following order:

\[
\begin{aligned}
 \widetilde\delta-\delta^p
 &=g(\widetilde z)(\widetilde p-p^p)
    +[g(\widetilde z)-g(z^p)]p^p
    +g(z^p)[p^p-\operatorname{clip}_N(p^p)].
\end{aligned}
\tag{A15}
\]

The middle term has normalized norm at most

\[
 jR\|\widetilde z-z^p\|_n
       +2s\|p^p1_{|p^p|>R}\|_n.
\]

The last term is at most `s ||p^p1_{|p^p|>N}||_n`, which is bounded by the
same tail at `R` because `N>=R`. For the first term at lower layers,

\[
 \widetilde p^{\ell-1}-p^{p,\ell-1}
   =(\widetilde W^\ell_k)^T
       (\widetilde\delta^\ell-\delta^{p,\ell})+A^p_{a,k}.
\]

At the top, `widetilde p=w^p=p^p`. Thus (A8), (A12)--(A15), and descending
induction give

\[
 \max_{\ell,a}
  (\|\widetilde p^\ell_{a,k}-p^{p,\ell}_{a,k}\|_n
    +\|\widetilde\delta^\ell_{a,k}-\delta^{p,\ell}_{a,k}\|_n)
 \le C\zeta,
 \qquad \zeta=(1+R)\xi+e^{-cR^2}.
 \tag{A16}
\]

The cutoff is added at each layer, not multiplied at every layer.

Predictions need only (A14), `widetilde w=w^p`, and the empirical
readout-feature pairing test. They satisfy

\[
 \|\widetilde r_k-r^o_k\|_m\le C\xi.
 \tag{A17}
\]

Subtracting the physical vector field at the proxy node from its affine
velocity now gives a concrete consistency estimate:

\[
 \|F(\widetilde\theta_k)-V^p_k\|_{\rm sum}\le C\zeta.
 \tag{A18}
\]

For clarity, the readout subtraction is
`(widetilde r-r^o)widetilde h+r^o(widetilde h-h^p)`.
The first-layer subtraction replaces `h` by `delta` and includes the fixed
input vector. A hidden block has the three terms from subtracting residual,
backward response, and forward response in `r delta h^T/n`.
Their norms are controlled by (A14), (A16), (A17), and the identity
`||uv^T/n||_F=||u||_n||v||_n`. These are all the terms in (A18).

## 7. Interpolation, current-state carrier tails, and comparison to dense flow

The following estimate packages the same calculation without needing to
postulate regularity of an empirical carrier path. Let `vartheta` be any
physical state in the common tube, at normalized parameter distance `d_*`
from the proxy mesh node `widetilde theta_k`. Ordinary forward subtraction,
followed by (A14), gives

\[
 \max_{\ell,a}(\|z^\ell(\vartheta)-z^{p,\ell}_{a,k}\|_n
             +\|h^\ell(\vartheta)-h^{p,\ell}_{a,k}\|_n)
       \le C(d_*+\xi).
 \tag{A19}
\]

In the reverse action, subtract as

\[
\begin{aligned}
 (W^\ell(\vartheta))^T\delta^\ell(\vartheta)-p^{p,\ell-1}_{a,k}
 &= (W^\ell(\vartheta))^T
                  (\delta^\ell(\vartheta)-\delta^{p,\ell}_{a,k})\\
 &\quad +(W^\ell(\vartheta)-\widetilde W^\ell_k)^T
                                      \delta^{p,\ell}_{a,k}
        +A^p_{a,k}.
\end{aligned}
\]

Its extra weight-change term has norm at most `C d_*`, by the Frobenius
block distance and the bounded oracle RMS. Apply the gate decomposition
(A15), now using (A19), against the same oracle carrier. The result is

\[
 \max_{\ell,a}(\|p^\ell(\vartheta)-p^{p,\ell}_{a,k}\|_n
          +\|\delta^\ell(\vartheta)-\delta^{p,\ell}_{a,k}\|_n)
 \le C[(1+R)(d_*+\xi)+e^{-cR^2}].
 \tag{A20}
\]

Prediction subtraction gives `||r(vartheta)-r^o_k||_m<=C(d_*+xi)`.
Repeating the three-factor vector-field subtraction from (A18) therefore
gives

\[
 \|F(\vartheta)-V^p_k\|_{\rm sum}
   \le C[(1+R)(d_*+\xi)+e^{-cR^2}].
 \tag{A21}
\]

This estimate can be used both at the current proxy interpolation state
and at the current actual dense state. Define

\[
 D(t)=d_n(\theta_{n,D}(t),\widetilde\theta(t)).
\]

By (A10), the dense state's distance from the proxy mesh node is at most
`D(t)+C h`. The two parameter paths start at the same initialization, and
their derivative difference is `F(theta_{n,D}(t))-V^p_k`. Integrating
(A21) gives

\[
 D(t)\le C\int_0^t(1+R)D(s)\,ds
       +Ct[(1+R)(h+\xi)+e^{-cR^2}].
\]

The scalar integrating-factor inequality yields precisely

\[
 \sup_{t\le T}D(t)
  \le C T e^{C(1+R)T}
       [(1+R)(h+\xi)+e^{-cR^2}].
 \tag{A22}
\]

This is formula (17) of the route with a fully specified consistency
quantity. There is no unspecified `o_P(1)` term and no width-dependent
carrier estimate assumed of the actual dense path.

Current-state carrier tails follow directly from (A20). Define

\[
 \nu=C[(1+R)(\sup_{t\le T}D(t)+h+\xi)+e^{-cR^2}].
\]

The actual dense carrier at any time in interval `k` differs from its
oracle node carrier by at most `nu` in normalized RMS. The same statement
holds for the current proxy carrier, with `D` omitted. For each tested
integer `M<=N`, the 1-Lipschitz positive-part map and (A7) give

\[
 \|p_D(t)1_{|p_D(t)|>M}\|_n
 \le 2\|(|p_D(t)|-M/2)_+\|_n
 \le C e^{-cM^2}+C\xi+2\nu.
 \tag{A23}
\]

This bound is uniform over all physical times in `[0,T]`; a new empirical
time net or a continuity claim for the threshold indicator is unnecessary.
For `M>N`, monotonicity bounds the left side by its value at `N`. Enlarge
the `exp(-cN^2)` contribution in (A5), if needed, so that (A23) extends to
all integer `M` with error `C(xi+nu)`.

Summing over the fixed layers and samples, integrating against the actual
dense residual, and using its bounded total activity gives

\[
 \int_0^T\rho_D(t)H_n(M,t)\,dt
      \le C e^{-cM^2}+C(\xi+\nu).
 \tag{A24}
\]

After `T`, the already established finite-width RMS bounds give
`H_n(M,t)<=C`, and exponential fitting gives an additional
`C exp(-kappa T)`, uniformly in `M`. Consequently the exact excess-tail
definition used in the paper obeys

\[
 a_n\le C[\xi+\nu+e^{-\kappa T}]
 \tag{A25}
\]

on the intersection of the oracle event and `G_n`. If the constants in the
definition of `a_n` need increasing, choose them once uniformly; this is
already allowed by the original existence statement for that remainder.

## 8. Parameter substitution and remaining identification

With `K=(log(e^e+n))^(1/128)` rounded down, `N=ceil(C_0 K^3)`,
`T=a sqrt(log K)`, `h=T/K`, and `R=A sqrt(log K)`, choose `A` sufficiently
large and then `a` sufficiently small. The choices give

\[
 \xi\le n^{-1/16}+C e^{-cN^2},\qquad
 \sup_{t\le T}D(t)+\nu\le C K^{-c_0},
\]

after a fixed width threshold. The oracle failure probability is at most
`C n^{-1/4}`, and (A2) adds only `C/n+C exp(-cn)`. Substitution in (A25)
therefore yields the advertised candidate bound

\[
 \Pr\left\{a_n>C\exp[-c\sqrt{\log\log(e^e+n)}]\right\}
       \le C n^{-1/4}.
 \tag{A26}
\]

Population Euler-to-flow approximation is still required to identify the
prediction target; it is the deterministic estimate already provided in
the current paper and has the same `T,R,h` budget. It is not needed for
(A25), which uses finite population Euler nodes only to transfer uniform
carrier tails. Prediction transfer additionally uses its readout-feature
tests and the normalized passive-input argument stated in the route.

The potentially delicate distinctions are now explicit: oracle fields are
modified and noisy; physical recomputed fields are unmodified; their
discrepancy is controlled through (A11)--(A21); and empirical tail bounds
are used only for the fixed oracle nodes before being transferred to
arbitrary current physical states.

## 9. Activity-damped upgrade: a logarithmic power rate

This section sharpens the conservative physical-time argument (A22). The
earlier sections remain valid. This refinement was requested by the
supervisor after the fixed-program result and (A11)--(A25) were frozen.

First, clarify the probe count in (A1): `N=ceil(C_0 K^3)` accommodates
`P<=K` passive probes, or a single probe, since the elementary count is
`C K^2(1+P)`. It does not accommodate an arbitrary fixed power of `K` without
changing the exponent of the budget. A larger bounded-domain input net can
instead be handled by separate normalized single-probe estimates and a
union bound. Those estimates have constants uniform in the input and need
no enlarged simultaneous program. Dependence between their events does not
affect the union bound.

### 9.1 Retain the residual in the local interpolation defect

For `t` in interval `k`, define

\[
 \alpha(t)=(t-t_k)\rho^o_k\le h\rho^o_k,
 \qquad q_R=e^{-cR^2}.
\]

The stronger form of (A10) is
`d_n(widetilde theta(t),widetilde theta_k)<=C alpha(t)`.
Apply (A19)--(A20) with this distance. The proxy interpolation fields obey

\[
\begin{aligned}
 \|\widetilde r(t)-r^o_k\|_m
    +\max_{\ell,a}\|\widetilde h^\ell_a(t)-h^{p,\ell}_{a,k}\|_n
       &\le C(\alpha(t)+\xi),\\
 \max_{\ell,a}
  (\|\widetilde p^\ell_a(t)-p^{p,\ell}_{a,k}\|_n
   +\|\widetilde\delta^\ell_a(t)-\delta^{p,\ell}_{a,k}\|_n)
       &\le C[(1+R)(\alpha(t)+\xi)+q_R].
\end{aligned}
\tag{A27}
\]

Put `E_p(t)=dot(widetilde theta)(t)-F(widetilde theta(t))` and
`e_p(t)=||E_p(t)||_sum`. In subtracting each gradient block, put the residual
difference first, and leave the original node residual in all remaining
terms. In the readout, for example, the subtraction is

\[
 (\widetilde r-r^o_k)\widetilde h
                  +r^o_k(\widetilde h-h^p_k).
\]

For a hidden block, write the three differences as

\[
 (\widetilde r-r^o_k)\widetilde\delta\widetilde h^T/n
 +r^o_k(\widetilde\delta-\delta^p_k)\widetilde h^T/n
 +r^o_k\delta^p_k(\widetilde h-h^p_k)^T/n.
\]

The fixed sample count converts the coefficients `r^o_{a,k}` into a factor
bounded by `C rho^o_k`. Using (A27) and the uniform physical RMS bounds gives

\[
 e_p(t)\le C(\alpha(t)+\xi)
       +C\rho^o_k[(1+R)(\alpha(t)+\xi)+q_R].
 \tag{A28}
\]

This displays the only unweighted error, the residual discrepancy
`C(alpha+xi)`. The clipping tail is multiplied by `rho^o_k`.

The original Euler residuals satisfy
`sum_k h_k rho^o_k<=C` and `sup_k rho^o_k<=C`. Consequently

\[
 \int_0^T\alpha(t)\,dt
       \le h\sum_k h_k\rho^o_k\le Ch,
 \qquad
 \int_0^T\rho^o_k\alpha(t)\,dt\le Ch.
\]

Integration of (A28) proves

\[
 \varepsilon_p:=\int_0^T e_p(t)\,dt
 \le C[(1+R)h+q_R+(T+1+R)\xi].
 \tag{A29}
\]

No term `T q_R` occurs. Also, (A27) gives

\[
 \widetilde\rho(t)\le(1+Ch)\rho^o_k+C\xi,
 \qquad
 \int_0^T\widetilde\rho(t)\,dt\le C+C T\xi.
 \tag{A30}
\]

We will impose `T xi<=1`, which holds by a large margin in the eventual
width/mesh choice. Thus the proxy has uniformly bounded total activity;
successful fitting of the proxy itself is not being assumed.

### 9.2 Weighted tails of the current proxy carriers

Let `H_p(R,t)` be the paper's sum of normalized carrier tail norms, now for
the **unclipped physical backward pass of the proxy interpolation state**.
The positive-part inequality and the second line of (A27) give

\[
 H_p(R,t)\le C[q_R+(1+R)(\alpha(t)+\xi)].
 \tag{A31}
\]

One may decrease the fixed Gaussian exponent in `q_R` to account for the
halved positive-part thresholds. Define

\[
 Z_p(R)=\int_0^T\widetilde\rho(t)H_p(R,t)\,dt.
\]

By (A30), `integral rho_p<=C`. Furthermore

\[
\begin{aligned}
 \int_0^T\widetilde\rho(t)\alpha(t)\,dt
 &\le C h\sum_k h_k(\rho^o_k)^2
                  +C\xi h\sum_k h_k\rho^o_k\le Ch,\\
 \int_0^T\widetilde\rho(t)\xi\,dt&\le C\xi.
\end{aligned}
\]

Hence

\[
 Z_p(R)\le C[q_R+(1+R)(h+\xi)].
 \tag{A32}
\]

This is the tail source used in damping. It concerns current proxy states,
and has been deduced from fixed oracle-node empirical tests.

### 9.3 One-reference damping with a perturbed proxy

Let `u=r_D-r_p`, where `r_p` is the recomputed proxy residual, and retain
`D(t)=d_n(theta_D(t),theta_p(t))`. Both paths start at the same parameters.
The dense path satisfies the preserved Gram gap `Gamma_D>=lambda I/2`.
The proxy residual equation is exact almost everywhere:

\[
 \dot r_p=-2\Gamma_p r_p+J_p E_p.
\]

Therefore

\[
 \dot u=-2\Gamma_D u
            -2(\Gamma_D-\Gamma_p)r_p-J_pE_p.
 \tag{A33}
\]

The one-reference backward subtraction from the paper applies with the
proxy as reference: bounded gates and operators, plus its current carrier
tails, give

\[
 \|\Gamma_D-\Gamma_p\|_{\rm op}
   \le C[(1+R)D(t)+H_p(R,t)].
\]

Physical RMS bounds give `||J_p E_p||_m<=C e_p`. Taking the upper derivative
of `||u||_m`, then integrating the damped inequality, yields for every
terminal time `t<=T`

\[
 \int_0^t\|u(s)\|_m\,ds
 \le C\left[(1+R)\int_0^t\widetilde\rho(s)D(s)\,ds
                   +Z_p(R;t)+\varepsilon_p(t)\right].
 \tag{A34}
\]

At zeros of `u`, use the usual regularization of its Euclidean norm, as in
the paper. No proxy Gram lower bound is needed here, because the damped
matrix in (A33) is the actual dense Gram.

Subtract parameter updates with the same residual ordering. Terms with
`u` are controlled by uniform physical RMS bounds; all response-change
terms retain the factor `rho_p`. Integrating and using the normalized
outer-product identity gives

\[
 D(t)\le C\varepsilon_p(t)+C\int_0^t\|u(s)\|_m\,ds
       +C\int_0^t\widetilde\rho(s)
                       [(1+R)D(s)+H_p(R,s)]\,ds.
\]

Insert (A34), replace the nondecreasing source by its terminal value, and
apply the integrating factor. By (A30),

\[
 \sup_{t\le T}D(t)
  \le C e^{C(1+R)\int_0^T\widetilde\rho}
                [\varepsilon_p+Z_p(R)]
  \le C e^{CR}[\varepsilon_p+Z_p(R)].
\]

Combining (A29) and (A32) proves the improved comparison

\[
 \sup_{t\le T}D(t)
 \le C e^{CR}[(1+R)h+e^{-cR^2}+(T+1+R)\xi].
 \tag{A35}
\]

The amplification depends on total activity, not on physical duration.
Its proof uses only the existing fitting theorem for the actual dense flow,
the explicitly controlled proxy defect, and the proxy activity and tail
bounds (A30)--(A32).

### 9.4 Deterministic population Euler comparison has the same upgrade

The population Euler affine interpolant has no finite-program or clipping
consistency error: set `xi=0` and replace modified empirical node fields by
the exact original population Euler fields. It has node-to-interpolant
distance `C alpha(t)`, and its node carriers have the uniform Gaussian tail.
The same gate cutoff gives its interpolant backward discrepancy at most
`C[(1+R)alpha(t)+q_R]`.

Consequently its total vector-field defect is at most
`C[(1+R)h+q_R]`, its residual activity is bounded by `C`, and its weighted
carrier-tail source is at most `C[q_R+(1+R)h]`. Compare to the already
constructed strong population flow on their common Hilbert spaces. The
strong flow supplies the preserved Gram gap in (A33), and all rank-one
norm identities used above remain valid in Hilbert--Schmidt norm.
Therefore

\[
 \sup_{t\le T}d(\theta_\infty(t),\theta^h(t))
      \le C e^{CR}[(1+R)h+e^{-cR^2}].
 \tag{A36}
\]

This is a new quantitative sharpening of the current paper's physical-time
Euler comparison; it does not invoke a stronger preexisting theorem.

### 9.5 Logarithmic-power consequence

Now take

\[
\begin{gathered}
 K=\left\lfloor(\log(e^e+n))^{1/128}\right\rfloor,
 \quad N=\lceil C_0K^3\rceil,\\
 T=(2/\kappa)\log K,\qquad h=T/K,
 \qquad R=A\sqrt{\log K},
\end{gathered}
\tag{A37}
\]

for sufficiently large `K`, with `A` chosen so the fixed tail exponent
`c A^2` is larger than two. Since `N^5<=C (log n)^(15/128)`, the term `xi`
in (A5) is smaller than every fixed power of `K` for large width. The
factor `exp(CR)` is `K^{o(1)}`. Equations (A35)--(A36) thus give

\[
 \sup_{t\le T}D(t)
       +\sup_{t\le T}d(\theta_\infty(t),\theta^h(t))
           \le K^{-1+o(1)}.
 \tag{A38}
\]

In (A20), the actual dense state is at distance at most
`D(t)+C alpha(t)` from the proxy mesh node, so all-time-on-`[0,T]` carrier
transfer costs at most `C(1+R)(sup D+h+xi)+C q_R`. Repeat (A23)--(A25)
and add the remaining dense residual activity `C exp(-kappa T)=C K^{-2}`.
This gives the stronger conclusion

\[
 a_n\le K^{-1+o(1)},
 \qquad\text{hence eventually }a_n\le C K^{-1/2},
 \tag{A39}
\]

with failure probability at most `C n^{-1/4}` after intersecting with the
original initialization event. The paper's exact remainder relation gives

\[
 b_n=C\Phi(a_n)\le C K^{-1/3}
             =C(\log(e^e+n))^{-1/384},
 \tag{A40}
\]

for sufficiently large width, since
`exp(C sqrt(log K))=K^{o(1)}`. One may weaken these fixed exponents further
to simplify the common parameter and prediction statement.

For a normalized fixed passive input, the node pairing estimate, (A38),
the deterministic population Euler bound, and the exponential terminal
variation give all-time prediction error at most `C K^{-1/2}` on an event
with failure `C n^{-1/4}`, with constants uniform in that input. On `G_n`,
the normalized prediction error is always bounded by a fixed constant.
Thus its squared expectation restricted to `G_n` is at most
`C(K^{-1}+n^{-1/4})`. For a fixed test law with finite second moment,
multiply by `s_x^2`, integrate by Tonelli, and apply Markov. It follows that

\[
 d_{n,\mu}=O_{\Pr}(K^{-1/4}),
 \qquad
 b_{n,\mu}=C_\mu b_n+d_{n,\mu}
       =O_{\Pr}((\log(e^e+n))^{-1/512}).
 \tag{A41}
\]

For instance, the probability that `d_{n,mu}` exceeds a fixed multiple of
`K^{-1/4}` is `O_mu(K^{-1/2})+O(n^{-1})`, which tends to zero. This argument
uses the fixed test law's second moment, with no quantitative tail
assumption. It controls the supremum over time inside the test integral,
because the single-input estimate already holds over all time.

The stronger logarithmic-power result supersedes the conservative
`exp(-c sqrt(log log n))` consequence, while preserving its valid
finite-program lemma and physical-time comparison as intermediate results.
