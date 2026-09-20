# Quantitative anchored refresh and noisy auxiliary search

2026-09-19. Independent bounded theoretical route, frozen before comparison
with other routes. No experiments; not promoted. Scientific inputs read in
full: this study's `NOISE_GLOBAL_PROGRESS.md`, `NOISE_RECURRENCE.md`, and
`ESCAPE_AND_LIMITS.md`. The research-contract, adversarial-audit, and rigorous
mathematics skills were applied. No other studies or routes were read.

The answer is affirmative for explicitly changed optimizers. Absolute
Gaussian refreshes on a constructive, finite-dimensional population family
give an explicit polynomial accuracy bound. An auxiliary accepted Gaussian
search on the family's readout coefficients gives an explicit logarithmic
accuracy bound, with a geometry-dependent condition number. The latter
does not compute a fitted readout, does not use a fitted state as an input,
and uses labels only in loss evaluations. It does build a data-dependent
feature family and runs a separate search in that family. These guarantees
do not establish a rate for the original centered additive Gaussian rule,
or a globally convergent genuinely local perturbation of its incumbent.

## 1. Exact object and admissible information

Use the exact fixed-order population state and physical metric

\[
S=(w,c,M)\in\mathcal H
=L^2(\lambda_1;\mathbb R^2)\oplus L^2(\lambda_2)
 \oplus\mathbb R^{d_2\times d_1}.
\]

The bounded, correctly normalized dictionaries and their full joint mark
laws remain those of canonical order p=1,2,3. Write B_l=ess sup |b_l|,
u_i=x_i/sqrt(2), and

\[
a_i=E_1[b_1\tanh(w\cdot u_i)],\quad
H_i=\tanh(b_2^TMa_i),\quad f_i=E_2[cH_i],\quad
L=\sum_i\mu_i(f_i-y_i)^2.                                      \tag{1}
\]

Merge repeated and antipodal observations, changing label signs when a
representative is reversed and adding masses. Compatibility and oddness
make this exactly loss-preserving. Let n>=1 be the remaining number of
representatives, with u_i!=+/-u_j, mu_i>0, sum mu_i=1, and y_i in {-1,1}.
Canonical initialization is still (g,0,D), with L_0=1.

All constructions below use only inputs, masses, known dictionary/mark
laws, and subsequently actual losses. Geometry preprocessing is permitted
and explicitly charged as preprocessing, outside the proposal clock.
The mathematical bounds assume exact population expectations and exact
loss comparisons. They do not assert finite-precision computational cost.
Exact full population gradient flow may run between incumbent proposals;
its global existence and decreasing loss are established in the allowed
inputs. No fixed-feature identity is asserted for this full flow.

## 2. A label-independent finite family containing an interpolant

Choose unit directions v_1,...,v_J avoiding all input orthogonality
directions and such that the rows (sign(v_j dot u_i))_j are different up
to sign. For each pair choose one direction giving equal signs and one
giving opposite signs; their open direction sets are nonempty because
the pair is not parallel. A finite union of forbidden orthogonality
directions cannot fill either open set. Thus J<=n(n-1) for n>=2; for n=1
one direction suffices. This is a construction from inputs alone.

For a completely specified choice of positive masses, put

\[
A_J=\sum_{j=1}^J3^{j-1}=(3^J-1)/2,\qquad
\alpha_j=3^{j-1}/A_J,\qquad
s_i=\sum_j\alpha_j\operatorname{sign}(v_j\cdot u_i).
\]

These sums are nonzero and pairwise different up to sign. Indeed, in a
nonzero signed sum of powers of three, the largest nonzero term has
absolute value larger than the sum of all smaller possible terms.
For differences or sums of two sign rows, divide the coefficients by
two and use the same argument. Therefore the finite positive constants

\[
m=\min_{i,j}|v_j\cdot u_i|,\qquad
\eta=\min\bigl(\{|s_i|\}_i\cup
 \{|s_i-s_k|,|s_i+s_k|\}_{i<k}\bigr)                            \tag{2}
\]

are explicitly determined by this construction. For n=1 the pair terms
are absent. Numerical computation of these constants and the integrals
below requires effective input data and certified integration/spectral
bounds; the exact-oracle theorem does not assert computability for an
arbitrary unspecified real-number or operator presentation.
Partition lower marks into cells A_j of masses alpha_j, using Gaussian
g_1 quantiles. Set v=v_j on A_j and

\[
T=\frac{\log(8/\eta)}{2m},\quad w_*=Tv,\quad
M_*=e\ell^T,\qquad b_1^T\ell=1,\quad b_2^Te=X=\tanh(\xi_1).
                                                                    \tag{3}
\]

These dictionary identities and the positive density of X on (-1,1)
hold for each of p=1,2,3 by the allowed source. Since
|tanh(Tt)-sign(t)|<=2 exp(-2T|t|), the numbers

\[
t_i=\sum_j\alpha_j\tanh(Tv_j\cdot u_i)
\]

satisfy |t_i-s_i|<=eta/4. Hence |t_i|>=3eta/4 and
|t_i+/-t_k|>=eta/2. The actual population features at (w_*,M_*) are

\[
H_i^*(X)=\tanh(t_iX),\qquad K_{ik}=E_2[H_i^*H_k^*].             \tag{4}
\]

For completeness, K is positive definite. A linear dependence among
these continuous functions almost surely is an identity on (-1,1)
because X has positive density there. Analyticity extends it to R.
Absorb signs of the nonzero t_i into coefficients and order their
distinct absolute values. The limit at +infinity makes the coefficient
sum zero. Subtract that constant identity and multiply by exp(2aX),
where a is the smallest absolute slope. The smallest-slope term tends
to minus twice its coefficient, and the others vanish. Successively
removing coefficients proves independence and positive definiteness.

Write lambda=lambda_min(K)>0 and C=sqrt(n/lambda). The following state
exists, but none of the algorithms below is given or computes it:

\[
c_*=\sum_i(K^{-1}y)_iH_i^*,\quad
f_i(w_*,c_*,M_*)=y_i,\quad
\|c_*\|_2^2=y^TK^{-1}y\le n/\lambda=C^2.                       \tag{5}
\]

K and lambda depend on inputs and mark laws, not labels. A fully explicit,
possibly very weak lower bound is

\[
\lambda\ge\det K/n^{n-1},                                    \tag{6}
\]

since every other eigenvalue is at most tr K<=n. K consists of the
specified bounded one-variable integrals in (4); the determinant is a
defined data constant, not an unspecified full-support probability.
No uniform lower bound over all finite compatible datasets is claimed.

## 3. Independent all-block Gaussian refresh: an explicit polynomial rate

Take the finite-dimensional population subspace with rows constant on
the cells A_j, readouts in span{H_i^*}, and arbitrary middle matrices.
Use the orthonormal row fields 1_{A_j}/sqrt(alpha_j) times the two
Cartesian directions, an orthonormal readout basis, and Frobenius matrix
coordinates. Its dimension is

\[
d=2J+n+d_1d_2.                                                 \tag{7}
\]

The coefficient map from R^d to H is an isometry. The zero-loss witness
(5) has coefficient norm bounded by

\[
R_*=(T^2+\|M_*\|_F^2+C^2)^{1/2}.                              \tag{8}
\]

An explicit global bound relative to this witness is useful. For any
S=(w,c,M), set delta_w=||w-w_*||_2, delta_c=||c-c_*||_2, and
delta_M=||M-M_*||_F. Boundedness and the Lipschitz constant one of tanh
give

\[
|a_i-a_i^*|\le B_1\delta_w,\quad |a_i|\le B_1,
\]

and, using Ma_i-M_*a_i^*=(M-M_*)a_i+M_*(a_i-a_i^*),

\[
\|H_i-H_i^*\|_\infty
\le B_1B_2(\delta_M+\|M_*\|_F\delta_w).
\]

Decompose cH_i-c_*H_i^*=(c-c_*)H_i+c_*(H_i-H_i^*). Then

\[
|f_i-y_i|\le\delta_c+CB_1B_2
 (\delta_M+\|M_*\|_F\delta_w)
\le A_*\|S-S_*\|_{\mathcal H},
\quad
A_*^2=1+C^2B_1^2B_2^2(1+\|M_*\|_F^2).                        \tag{9}
\]

Because the masses sum to one, L(S)<=A_*^2||S-S_*||^2. There is no
unwritten radius restriction in (9).

At each proposal, independently with probability rho in (0,1], generate
an ABSOLUTE candidate by drawing all d coefficients from N(0,s^2I_d),
where

\[
s=(R_*+1)/\sqrt d.                                             \tag{10}
\]

Accept it only if it strictly improves the actual incumbent loss.
Other proposals, if rho<1, may be the original centered additive
population Gaussian, with the same strict acceptance test. Full exact
flow may run between trials. The incumbent need never lie in the
finite-dimensional refresh family.

For 0<epsilon<=1, let r=sqrt(epsilon)/A_*<=1. Every coefficient in
B(theta_*,r) has loss at most epsilon. Its volume and a density lower
bound give

\[
\begin{split}
P\{L(S_{\rm refresh})\le\epsilon\}
&\ge\frac{\pi^{d/2}r^d}{\Gamma(d/2+1)}
 (2\pi s^2)^{-d/2}
 \exp[-(R_*+r)^2/(2s^2)]\\
&\ge Q_d\epsilon^{d/2},\\
Q_d&=\frac{(d/(2e))^{d/2}}{\Gamma(d/2+1)}
       [A_*(R_*+1)]^{-d}>0.                                  \tag{11}
\end{split}
\]

This derives both the volume and the loss-to-radius constant; no
unknown Gaussian small-ball mass remains. Before the loss reaches
epsilon, such a candidate is accepted. Successive conditioning, even
with arbitrary intervening decreasing flow and other proposals, gives
for the first proposal time tau_epsilon with loss<=epsilon,

\[
P\{\tau_\epsilon>N\}\le(1-\rho Q_d\epsilon^{d/2})^N
\le e^{-\rho Q_dN\epsilon^{d/2}},\qquad
E\tau_\epsilon\le\frac{\epsilon^{-d/2}}{\rho Q_d}.              \tag{12}
\]

Thus N>=epsilon^{-d/2} log(1/delta)/(rho Q_d) suffices with probability
at least 1-delta. For N>=1 the expected loss also obeys

\[
E L_N\le\min\{1,\,
 \Gamma(1+2/d)(\rho Q_dN)^{-2/d}\}.                            \tag{13}
\]

Indeed integrate P(L_N>t)<=exp(-rho Q_dNt^{d/2}) over 0<t<1 and
then enlarge the integral to (0,infinity). Substitution
u=rho Q_dNt^{d/2} gives the displayed gamma factor.

This is polynomial in inverse accuracy for each fixed instance and d.
Its exponent grows with n and the dictionary dimension, and its
constant may be extremely bad. It is global random search.

### A smaller refresh family

Keeping w_*,M_* fixed only when forming candidates and drawing isotropic
Gaussian coefficients in an orthonormal basis of span{H_i^*} reduces
the proposal dimension to n. For these candidates
L(c)<=||c-c_*||_2^2, because |H_i^*|<=1 and sum mu_i=1.
Using s=(C+1)/sqrt(n) gives (11)--(13) with

\[
d=n,\qquad Q_n=
 \frac{(n/(2e))^{n/2}}{\Gamma(n/2+1)}(C+1)^{-n}.                \tag{14}
\]

This family is independent of labels. Its covariance and lower-field
anchor are data-dependent. All hidden variables remain trainable in
the incumbent's subsequent full flow; that does not turn the candidate
generator into full-feature training.

## 4. Adaptive Gaussian coefficient search: an explicit logarithmic rate

The polynomial bound can be strengthened by letting the proposal
generator keep its own improving readout coefficients. This is an
additional optimizer change and requires an auxiliary state in R^n.
It uses the RAW features H_i^* in (4), so no matrix inverse or fitted
readout is needed by the algorithm.

For coefficients a in R^n define the actual population candidate

\[
S(a)=(w_*,\,\sum_j a_jH_j^*,\,M_*),\qquad
V(a)=L(S(a))=(Ka-y)^TW(Ka-y),\quad W=\operatorname{diag}(\mu_i).
                                                                    \tag{15}
\]

Let

\[
Q=KWK,\quad \kappa=\lambda_{\min}(Q)>0,\quad
\Lambda=\lambda_{\max}(Q),\quad
q_0=\frac{e^{-2}}{2\sqrt{2\pi}},\quad
\gamma=\frac{q_0\kappa}{4n\Lambda}.                            \tag{16}
\]

These constants and the feature construction use inputs, masses and
mark laws only. Conservative certified bounds may replace the exact
eigenvalues: kappa_lower=mu_min(det K/n^{n-1})^2 and
Lambda_upper=n^2 are valid. Using those instead throughout simply
weakens gamma. No label preprocessing is used.

Initialize auxiliary a_0=0, whose loss is one. On an auxiliary trial
with ell=V(a)>0 draw an independent G~N(0,I_n), set

\[
a'=a+\frac{\sqrt{\kappa\ell}}{4n\Lambda}G,                    \tag{17}
\]

and replace a by a' exactly when V(a')<V(a). The scale uses the actual
current loss, not its unknown difference from an unspecified infimum:
the zero infimum was proved in (5). Stop the auxiliary chain at ell=0.
The algorithm needs only loss values, features, and spectral constants;
it never uses a_*=K^{-1}y, whose role below is exclusively in the proof.

Independently at each main trial, with probability rho, do ONE such
auxiliary trial and offer its resulting population state to the
incumbent, accepting only a strict incumbent improvement. Otherwise
one may use the original Gaussian proposal. Exact full flow may run
between any trials. Maintain the auxiliary chain even when the
incumbent already has smaller loss and rejects its proposed state.
At initialization and after every trial,

\[
L(S_{\rm incumbent})\le V(a),                                 \tag{18}
\]

because the two initial losses equal one, flow/other accepted proposals
only decrease incumbent loss, and an improving auxiliary state either
replaces the incumbent or already has no smaller loss than it.

**One-step contraction proof.** Put e=a-a_*, ell=e^TQe, g=Qe, and
sigma=sqrt(kappa ell)/(4n Lambda). Spectral bounds imply

\[
\|g\|^2=e^TQ^2e\ge\kappa\ell,\qquad
V(a+\sigma G)-\ell=2\sigma g\cdot G+\sigma^2G^TQG.            \tag{19}
\]

Resolve G into Z along g/||g|| and its independent orthogonal component
G_perp. For n>=2, Markov's inequality gives
P(||G_perp||^2<=2(n-1))>=1/2. For n=1 this component is zero. Also

\[
P(-2\le Z\le-1)=\int_1^2\frac{e^{-z^2/2}}{\sqrt{2\pi}}dz
\ge\frac{e^{-2}}{\sqrt{2\pi}}.
\]

Thus an event of conditional probability at least q_0 has
g dot G<=-||g|| and ||G||^2<=4+2(n-1)<=4n. On that event (19) is at most

\[
-2\sigma\sqrt{\kappa\ell}+4n\Lambda\sigma^2
=-\frac{\kappa}{4n\Lambda}\ell.                              \tag{20}
\]

This proposal is accepted; on the complement acceptance keeps loss
from increasing. Therefore

\[
E[V(a_{k+1})\mid a_k]\le(1-\gamma)V(a_k).                     \tag{21}
\]

Independent Bernoulli selection of the auxiliary trials changes this
factor to 1-rho gamma per MAIN proposal. Equations (18) and (21) yield
the actual proposal-clock guarantees

\[
E L_N\le(1-\rho\gamma)^N\le e^{-\rho\gamma N},\qquad
P(L_N>\epsilon)\le\epsilon^{-1}e^{-\rho\gamma N}.              \tag{22}
\]

In particular, for 0<epsilon<1,

\[
N\ge\frac{4n\Lambda}{\rho q_0\kappa}
          \log\frac1{\epsilon\delta}                          \tag{23}
\]

suffices for loss<=epsilon with probability at least 1-delta. Monotonicity
identifies {tau_epsilon>N} with {L_N>epsilon}. Summing the bound
min(1,epsilon^{-1}(1-rho gamma)^N), starting its geometric tail at
ceil(log(1/epsilon)/[-log(1-rho gamma)]), gives

\[
E\tau_\epsilon\le
1+\frac{\log(1/\epsilon)+1}{\rho\gamma}.                       \tag{24}
\]

The chain therefore converges almost surely to zero loss as well:
for every rational epsilon>0, its nonincreasing loss has probability
zero of staying above epsilon by (22). Unlike a rate per completed
successful stage, (22)--(24) count every unsuccessful proposal.

### What preconditioning can and cannot remove

If one is willing to compute a label-independent inverse, define
c(z)=sum_j[K^{-1}W^{-1/2}z]_jH_j^*. Its predictor is W^{-1/2}z,
and its loss is ||z-W^{1/2}y||^2. The SAME accepted rule with
z'=z+sqrt(ell)G/(4n) has kappa=Lambda=1 in the proof above.
It gives gamma=q_0/(4n), with no data condition number in the proposal
clock. It still starts at z=0 and does not solve for W^{1/2}y.

This apparent improvement pays for the inverse interpolation operator
in advance. In physical readout norm,

\[
\|c(z)\|_2^2=z^T(W^{1/2}KW^{1/2})^{-1}z,
\]

so poor geometry can make typical physical steps enormous. If
kappa_w=lambda_min(W^{1/2}KW^{1/2}), then an update has
E||delta c||_2^2<=ell/(16n kappa_w). This is not a geometry-free
physical-time or finite-precision theorem. The raw-coefficient theorem
(23) avoids giving the algorithm that inverse and exposes the condition
number directly.

## 5. Mechanism, limits, and hostile checks

* **Original problem versus variant.** The incumbent always lives in
  the exact full population closure and begins at canonical initialization.
  Absolute replacement proposals and the auxiliary search change the
  optimizer. Neither result is a theorem for the original iid centered
  additive Gaussian perturbations alone.
* **No supplied fitted state.** All proposal support, partition, slopes,
  Gram entries and spectral constants are determined without label
  values. The raw-coefficient algorithm never inverts K and uses labels
  only through losses. Its proof uses the interpolant (5); the algorithm
  does not. The optional preconditioned version explicitly computes an
  inverse from geometry and must be reported separately.
* **Fixed-feature explanation survives.** The logarithmic guarantee
  comes entirely from a strongly convex readout problem in an auxiliary
  family. Full hidden-layer flow is allowed in the incumbent, but this
  proof gives it no credit. Calling the guarantee a convergence rate for
  full population gradient flow would be false.
* **Local versus global.** Independent refresh relies on global search
  and can be extraordinarily rare. In the auxiliary chain, effective
  relative decreases have uniformly positive probability q_0 and use
  ||G||<=2sqrt(n); they are not rare-tail successes. Their physical
  readout increments tend to zero with sqrt(ell), for each fixed geometry.
  However a candidate resets the incumbent's hidden fields to (w_*,M_*).
  That incumbent jump need not be local even when auxiliary steps are
  small. These results do not resolve global fitting under norm-bounded
  small perturbations of the current full state.
* **All dependencies exposed.** n, input separation through m and eta,
  Gram conditioning, dictionary bounds, matrix norm and refresh fraction
  enter the constants displayed above. No uniform efficient bound over
  sample count or collapsing data geometries follows. For (23),
  compatibility, finite data and p=1,2,3 suffice for positivity of kappa;
  good numerical conditioning is not automatic.
* **Clock.** Every rejected candidate counts. One proposal costs an exact
  population loss evaluation, and setup requires the specified integrals
  and spectral information. To turn a proposal count into elapsed time,
  one needs a bound on these costs and on intervening flow durations.
  Unbounded discretionary flow duration defeats any such translation.
* **No compactness repair smuggled in.** The rates are independent of
  incumbent norm or recurrence because the successful proposal mechanism
  is external to its current location. This removes a recurrence premise
  by changing proposals, rather than proving recurrence of the old chain.

The strongest non-oracle quantitative conclusion in this route is (23):
accepted isotropic Gaussian coefficient perturbations, with loss-dependent
scale, find useful candidates in logarithmically many total trials for
each fixed dataset, with an explicit condition-number cost. The independent
refresh result (12) is closer to the existing restart idea but weaker in
accuracy. Both use global candidate replacement at the incumbent level.
