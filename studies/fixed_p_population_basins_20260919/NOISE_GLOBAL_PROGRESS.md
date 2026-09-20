# Accepted noise: fitting, norm escape, and a stricter acceptance theorem

2026-09-19. Continuation of this study's noise investigation. No simulation.

## 1. Exact model and conclusions

Use the exact fixed-order population state S=(w,c,M), on
H=L2(lambda1;R2) x L2(lambda2) x R^(d2 x d1), with its physical
L2/Frobenius metric. Keep the complete canonical initialization (g,0,D),
joint mark laws, dictionary normalization, actual transpose, and unhalved
probability-weighted square loss. Scientific inputs are established
global_nonlinear.md C.4.7.10.B/C.1/D.3 and this study's ESCAPE_AND_LIMITS.md.
With phi=tanh and x_i in sqrt(2) S1,

\[
a_i=E_1[b_1\phi(w\cdot x_i/\sqrt2)],\quad
H_i=\phi(b_2^TMa_i),\quad f_i=E_2[cH_i],\quad
L(S)=\sum_i\mu_i(f_i-y_i)^2.                                      \tag{1}
\]

Data are finite, have positive masses summing to one and compatible binary
labels: duplicate inputs have the same label and antipodal inputs have
opposite labels. No sample-count or linear-independence assumption is imposed.
The proofs here apply to p=1,2,3. They use these verified dictionary facts:
b1,b2 bounded; constants in the lower span; X=tanh(xi1) in the upper span
with positive density on (-1,1); nonatomic lower marks via Gaussian g1.
Consequently there exist fixed coefficient vectors l,e such that

\[
b_1^T l=1,\qquad b_2^T e=X.                                      \tag{2}
\]

The loss is continuous and exact physical gradient flow is globally
well posed and loss-decreasing on H, as proved in ESCAPE_AND_LIMITS.md.
Let nu be any centered full-support Gaussian on H with positive trace-class
covariance. Its fixed positive scale is included in nu. Proposals are
independent draws h from nu, added to the current state.

Results for the ORIGINAL rule, accepting every strict loss decrease:
a positive limiting loss forces ||S_k||_H to tend to infinity almost surely.
Hence bounded recurrence, without strong compactness, suffices for fitting.
Bounded recurrence from canonical initialization remains unproved.

A second theorem uses the SAME Gaussian proposal law with a CHANGED
acceptance rule: while holding the current state fixed, wait for a proposal
that reduces loss by a prescribed fraction. This gives unconditional
almost-sure fitting, with geometric loss decay per completed stage.
It does not give a uniform rate in proposal count or physical time.
The distinction between the two algorithms is essential.

## 2. Every compatible finite dataset has a finite zero-loss state

First merge identical and antipodal observations, adjusting signs of labels.
Oddness of (1) makes this reduction exactly loss-preserving. In the following
construction only, write u_i=x_i/sqrt(2) for the remaining representatives,
so u_i!=±u_j when i!=j.

For any unit direction v not orthogonal to the inputs, set
sigma_i(v)=sign(v dot u_i). Choose finitely many directions v_1,...,v_J
so that their sign columns R_i=(sigma_i(v_j))_j are different up to sign.
For each nonparallel, nonantiparallel pair, there are open directions with
equal signs and open directions with opposite signs. Select witnesses
avoiding all finitely many orthogonality directions. With one input,
one nonorthogonal direction suffices.

There are positive masses alpha_j summing to one such that

\[
s_i=\sum_j\alpha_j\sigma_i(v_j)\ne0,\qquad
s_i\ne\pm s_k\quad(i\ne k).                                     \tag{3}
\]

Indeed each forbidden equality is a proper affine hyperplane in the
probability simplex. A linear form vanishing on the whole simplex has
every coefficient zero, excluded by the sign-column construction.
A finite union of proper hyperplanes cannot contain the relative interior:
the product of their nonzero affine linear factors is a nonzero polynomial.
One can choose rational masses in the complement by density.

Partition the lower mark space into cells A_j of masses alpha_j using
successive quantiles of g1. Define v(omega)=v_j on A_j. The bounded upper
functions H_i^*(X)=phi(s_i X) are linearly independent. To check this
directly, a relation almost surely is an identity on (-1,1) by positive
density and continuity. Real analyticity extends it to R. Absorb signs
of s_i into coefficients and order the distinct positive slopes |s_i|.
The limit at +infinity says the coefficient sum is zero. Subtract this
constant relation and multiply by exp(2 min |s_i| X). The smallest-slope
term tends to minus twice its coefficient, since

\[
e^{2aX}(\tanh(aX)-1)\longrightarrow-2,
\]

and all larger-slope terms tend to zero. Induction removes every term.
Thus K_ij=E[H_i^*H_j^*] is positive definite.

Set w_T=T v and M_*=e l^T. Equation (2) gives

\[
b_2^TM_*a_i=X s_i(T),\qquad
s_i(T)=\sum_j\alpha_j\tanh(Tv_j\cdot u_i)\longrightarrow s_i.       \tag{4}
\]

At some finite T the s_i(T) remain nonzero and distinct up to sign.
The Gram K(T) of H_i(T)=phi(s_i(T)X) is positive definite by the same
proof. The finite field

\[
c_T=\sum_j [K(T)^{-1}y]_jH_j(T)                                 \tag{5}
\]

satisfies E[c_T H_i(T)]=y_i. Hence (w_T,c_T,M_*) is a zero-loss state
of the exact full closure. This is an expressivity witness, not a changed
initialization, a prescribed trajectory, or a restriction of M during
training. Its constants may deteriorate with input geometry.

## 3. Uniform probability of fitting from a bounded population ball

For every R<infinity and a>0, there is q(R,a)>0 such that

\[
\inf_{\|S\|_H\le R}\nu\{h:L(S+h)<a\}\ge q(R,a).                  \tag{6}
\]

This is a closure-specific result. Gaussian full support alone does not
give a uniform hitting probability over an infinite-dimensional ball.

Proof. Keep the sign-pattern field v, ideal features H_i^*=phi(s_iX), and
their Gram K from Section 2. For the current readout c put

\[
h_c(c)=\sum_j[K^{-1}(y-f^*(c))]_jH_j^*,\qquad
f_i^*(c)=E[cH_i^*].                                             \tag{7}
\]

Then E[(c+h_c(c))H_i^*]=y_i. For ||c||2<=R there is C_R<infinity
bounding both ||h_c(c)||2 and ||c+h_c(c)||2, because K is fixed
positive definite and |H_i^*|<=1.

For a fixed large T use additive controls centered at

\[
h(S)=(T v,\ h_c(c),\ M_*-M).                                    \tag{8}
\]

As ||S||<=R varies, these centers lie in a compact subset of H:
the row component is fixed, the readout component belongs to a bounded
set in a fixed finite-dimensional span, and the matrix component is
finite-dimensional and bounded. Take the compact closure if necessary.
There is no attempt to approximate -w in infinitely many coordinates.

Let m=min_(i,j)|v_j dot u_i|>0. If ||w_tilde||2<=R+1, then outside
the set |w_tilde|>Tm/2, the sign of (w_tilde+Tv) dot u_i is the
prescribed sigma_i(v_j), with absolute value at least Tm/2.
The tanh tail estimate and Markov inequality imply uniformly in i that

\[
\left|E_1\phi((\widetilde w+Tv)\cdot u_i)-s_i\right|
\le 2e^{-Tm}+\frac{8(R+1)^2}{T^2m^2}=:d_T\longrightarrow0.       \tag{9}
\]

For an error h_err of H norm less than r<=1 around (8), absorb its
row component into w_tilde=w+(h_err)_w. The new matrix is
M_*+(h_err)_M. Write B_l=ess sup |b_l|. Its upper preactivation
differs from s_i X by at most d_T+B1 B2 r in L-infinity: the
M_* contribution is (9), using (2), and the matrix error is bounded
by B2 r |a_i|<=B1 B2 r. Since tanh is 1-Lipschitz, the resulting
feature has the same error bound. Thus

\[
|f_i(S+h(S)+h_{\rm err})-y_i|
\le C_R(d_T+B_1B_2r)+r.                                        \tag{10}
\]

Choose T finite so C_R d_T<sqrt(a)/4, then r>0 so the right side is
strictly below sqrt(a). Both choices are uniform over ||S||<=R.
The probability weights sum to one, so all these proposed states have
loss below a.

Cover the compact set of centers (8) by finitely many radius-r/2
balls with centers h_1,...,h_N. For every h(S), one such center is
within r/2, and its radius-r/2 ball lies in B(h(S),r). Each of the
finitely many balls has positive nu mass by full support. Their
positive minimum proves (6).

This proof also works for any fixed full-support additive proposal law.
It does not work for proposals conditioned to a fixed norm bound: (8)
may lie outside their support. The probability q(R,a) can be extremely
small and has no claimed bound uniform in R, target a, or data geometry.

## 4. The unchanged algorithm: fitting or escape to infinity

Let S_k be the state just before proposal k, accepting every strict
loss decrease and optionally running any finite nonnegative duration
of the exact gradient flow between proposals. Loss decreases to a
limit L_infinity.

Fix an integer R and a positive rational a. Whenever ||S_k||<=R and
L(S_k)>=a, (6) with target a/2 gives conditional probability at least
q(R,a/2)>0 of proposing a state below a/2. It is accepted, and
subsequent flow preserves that strict bound. Avoiding success through
N such visits has probability at most (1-q)^N, by successive
conditioning at the visit times. Thus infinitely many visits to the
radius-R ball are incompatible with L_infinity>=a almost surely.
A countable union over R and a yields

\[
P\{L_\infty>0,\ \liminf_{k\to\infty}\|S_k\|_H<\infty\}=0.         \tag{11}
\]

Equivalently, almost surely,

\[
L(S_k)\longrightarrow0\quad\text{or}\quad
\|S_k\|_H\longrightarrow\infty.                                 \tag{12}
\]

The alternatives need not be exclusive. Fitting can accompany diverging
neutral coordinates. This replaces the earlier precompactness premise
by bounded recurrence, using the actual architecture.

Uniform tightness of ||S_k|| along a deterministic infinite subsequence
also suffices. Suppose P(L_infinity>=a)=s>0. Choose R so on that
subsequence P(||S_k||>R)<s/2. Then
P(L(S_k)>=a,||S_k||<=R)>=s/2. At each such time the event that loss
crosses from at least a to below a/2 has probability at least
q(R,a/2)s/2. These events are disjoint over time, since loss never
increases. Infinitely many events with the same positive lower
probability contradict total probability at most one. Therefore s=0.

Neither bounded recurrence nor norm tightness is proved for the original
noisy closure from canonical initialization. Loss does not control all
population norms; noise can also accumulate in neutral directions.
The theorem is the event-level dichotomy (12), not unconditional fitting
for this algorithm.

## 5. Unconditional fitting with a fractional-progress acceptance test

Fix theta in (0,1), for example 1/2. Keep the same fixed Gaussian law nu.
At a stage beginning at S with loss ell>0:

1. Optionally run exact gradient flow for a fixed finite duration h,
   obtaining T. If L(T)<=theta ell, complete the stage.
2. Otherwise HOLD T FIXED while drawing independent h_j from nu.
   Accept the first candidate satisfying L(T+h_j)<=theta ell.
   Reject all others, including smaller improvements.
3. Begin the next stage at the accepted state. Stop if loss is zero.

There is no flow during the unsuccessful trial loop. This pause and
the stronger acceptance threshold are explicit algorithm changes.
All tests use current states, data and loss; no future endpoint is
an algorithmic input.

**Theorem.** From any finite-loss state, including canonical (g,0,D),
each positive-loss stage completes in finitely many proposals almost
surely. If J counts completed stages,

\[
L_J\le\theta^J L_0,\qquad L\longrightarrow0
\quad\text{almost surely as training stages and trials proceed}. \tag{13}
\]

Proof. Conditional on the fixed T and ell>0, Section 2 supplies a
finite zero-loss state S^*. By continuity a ball about S^* has
loss strictly less than theta ell. Its translate by -T has positive
nu mass. Hence

\[
p(T,\ell)=\nu\{h:L(T+h)\le\theta\ell\}>0.
\]

As T stays fixed during the trial loop, the waiting time N is geometric:

\[
P(N>n\mid T,\ell)=(1-p(T,\ell))^n,\qquad
E[N\mid T,\ell]=1/p(T,\ell)<\infty.                              \tag{14}
\]

A stage completed by gradient flow needs no trials. Induction proves
that each finite number of stages finishes almost surely; taking their
countable intersection proves completion of every stage unless exact
zero was reached earlier. The loss reduction at each completed stage
proves (13). For every positive epsilon, finitely many stages suffice,
and their finitely many almost-surely finite trial counts sum to a
finite trial count almost surely. If one wants a wall-clock convention,
give every trial one unit of time and every deterministic stage its
stated finite duration; every positive accuracy is reached in finite
such time almost surely. No uniform rate is implied.

The zero-loss witness is used only to prove positive success probability.
The algorithm never computes it or receives it as an oracle. More
abstractly the same argument applies to any continuous loss with infimum
zero, even if it is not attained, by using an approximate minimizer.

## 6. Interpretation, counterchecks, and exact limits

The strengthened acceptance rule prevents infinitely many negligible
improvements from moving the state away before a substantial proposal
gets repeated chances. NOISE_OBSTRUCTION.md proves that the original
rule can have this failure mode, even with an analytic square loss and
a unique zero local minimum. That auxiliary example is not the closure.

The following distinctions are part of the conclusions:

* Equation (13) is geometric in COMPLETED STAGES, not physical GF time
  or total proposals. The waiting probabilities (14) have no uniform
  positive lower bound here, and unconditional expected waiting times
  are not bounded.
* Any fixed positive Gaussian scale is allowed. Its unbounded support
  can be essential: rare large jumps may carry the guarantee. There
  is no equivalent theorem here for norm-bounded infinitesimal noise.
* Rejected high-loss candidates are evaluated but never become the
  accepted state. All accepted-state losses remain nonincreasing.
* This is neither ordinary additive SDE noise nor minibatch SGD noise.
* All hidden layers remain trainable in the actual model. The special
  interpolation/control constructions prove existence and support;
  they do not replace its trajectory by a frozen-feature flow.
* No no-spurious-local-minima theorem is needed for Sections 3--5.
  Full-support proposals can cross loss barriers. Consequently (13)
  is an eventual global-search guarantee, not a mechanism-specific
  explanation or an efficient convergence result for gradient descent.

For the exact old rule, the remaining obligation is to exclude
positive-loss norm escape in (12), or otherwise prove that the total
conditional probability of effective descent remains divergent along
such escapes. The new acceptance variant resolves eventual fitting,
with the algorithmic changes and rate limitations stated above.

