# General nondegeneracy of the last Gaussian innovation

2026-10-04. New internally derived component of the integrated study.
This note removes the onset-nondegeneracy assumption for general positive
definite training covariance when there are at least two training samples.
It also classifies the one-sample exceptions. It concerns the actual
canonical gradient flow through its initialized derivative and the
already-proved derivative-to-trajectory inequality; it is not an endpoint
lower theorem.

Complete scientific inputs read: EARLY_VARIABILITY_AND_STORAGE.md
(SHA-256 54744f6e58fe0f03f0349041100664dbd55c1335e5edc80d574979b128d960ea)
and ONSET_TO_TRAJECTORY_LOWER.md
(SHA-256 34db6bf196433afd1c042832063f9fcc5c578a8aa389ec891ba3312dd345b5cd).
The quantitative covariance argument was
developed in parallel in this task and independently checked here; its
companion is GENERAL_INNOVATION_LOWER.md. No earlier-study source,
experiment, or unproved trained-response estimate is used.

## 1. Setup and main innovation bound

Fix arbitrary depth \(L\ge2\), finitely many unit training inputs
\(v_a=x_a/\sqrt d\), and a deterministic nonzero label vector
\(y\in\mathbb R^m\). Use the canonical independent Gaussian read-in and
mixers, zero readout, mean squared loss, and mobilities
\((n,1,\ldots,1,n)\). Activations can depend on the layer, need not be odd
or centered, and may have unbounded values. For the probabilistic lemma,
linear growth suffices; the trajectory conclusion uses the inherited
strip-holomorphic bounded-derivative assumptions.

Define the population covariance recursion on the training set by
\[
 Q^{(0)}_{ab}=v_a^\top v_b,\qquad
 Q^{(j)}_{ab}=\mathbb E[\phi_j(Z_a)\phi_j(Z_b)],
 \qquad Z\sim N(0,Q^{(j-1)}).
\]
Write \(Q=Q^{(L)}\) and assume
\(\gamma=\lambda_{\min}(Q)>0\). All diagonal entries of \(Q^{(j)}\)
equal the scalar moment
\[
 q_0=1,\qquad q_j=\mathbb E\phi_j(\sqrt{q_{j-1}}G)^2,
 \qquad G\sim N(0,1).
\]
For the final Gaussian layer set
\[
 Z\sim N(0,Q^{(L-1)}),\qquad H_a=\phi_L(Z_a),\qquad S=y^\top H,
 \qquad
 \mu_4=\mathbb E\phi_L(\sqrt{q_{L-1}}G)^4.
\]
The vector \(Z\) may have singular covariance. The fourth moment is
finite, and \(\mu_4>0\) because \(Q\succ0\).

For \(m\ge2\),
\[
 \operatorname{tr}\operatorname{Cov}(HS)
 \ge
 \frac{(m-1)^2}{4m^2}
 \frac{\gamma^3q_L}{\mu_4}\,\|y\|^2
 \ge
 \frac{\gamma^3q_L}{16\mu_4}\,\|y\|^2.
 \tag{1}
\]
Consequently at least one deterministic training index \(a_*\) satisfies
\[
 \operatorname{Var}(H_{a_*}S)
 \ge\frac{\gamma^3q_L}{16m\mu_4}\,\|y\|^2>0.
 \tag{2}
\]
The index can depend on the data, activations, and label direction, but
does not depend on width or on the random network initialization.
The constants use only two one-dimensional final-layer Gaussian moments,
which depend on the fixed activation functions and depth. No positive
gap for the centered feature covariance is assumed.

## 2. Qualitative nondegeneracy needs no Gaussian assumption

First consider any random vector \(H\) with finite fourth moment and
\(\mathbb E HH^\top=Q\succ0\). If all the coordinates of \(HS\) had
variance zero, then
\[
 HS=c\quad\text{almost surely},\qquad c=\mathbb E HS=Qy.
\]
Taking the scalar product with \(y\) gives
\[
 S^2=y^\top Qy>0
\]
almost surely. Thus \(H=c/S\) lies in the fixed one-dimensional span of
\(c\), forcing \(\operatorname{rank}Q\le1\). This contradicts \(Q\succ0\)
when \(m\ge2\). This proof does not use oddness, independent coordinates,
Gaussian support, or continuity. Positive definiteness of the uncentered
second moment is exactly the required hypothesis.

## 3. Quantitative proof with fourth moments

The following derivation also holds for an arbitrary random vector with
equal second and fourth marginal moments. Put
\[
 c=Qy,\qquad
 V=\mathbb E\|HS-c\|^2,\qquad
 K=\mathbb E\|H\|^4,\qquad T=\operatorname{tr}Q=mq_L.
\]
Here \(c\ne0\), and Cauchy--Schwarz gives
\[
 K=\sum_{a,b}\mathbb E H_a^2H_b^2\le m^2\mu_4.
 \tag{3}
\]
The squared area of the pair \(c,H\) obeys
\[
 \|c\|^2\|H\|^2-(c^\top H)^2
 \le\|HS-c\|^2\|H\|^2.
 \tag{4}
\]
Indeed the left side is the squared norm of the component of \(c\)
orthogonal to \(H\), multiplied by \(\|H\|^2\); replacing \(c\) by
\(c-HS\) leaves that orthogonal component unchanged. Formula (4) also
holds when \(H=0\).

The expectation of the left side is
\[
 N=c^\top(TI-Q)c
   =y^\top Q^2(TI-Q)y>0.
 \tag{5}
\]
For any \(R>0\), split the expectation into \(\{\|H\|\le R\}\) and
its complement. Equation (4) controls the first part, while the
left side of (4) is at most \(\|c\|^2\|H\|^2\) on the second part.
Markov's pointwise estimate gives
\[
 N\le R^2 V+\|c\|^2
       \mathbb E[\|H\|^2\,1_{\{\|H\|>R\}}]
 \le R^2V+\frac{\|c\|^2K}{R^2}.
\]
Choose \(R^2=2\|c\|^2K/N\). Every denominator is positive. Rearranging,
\[
 V\ge\frac{N^2}{4\|c\|^2K}.
 \tag{6}
\]

All eigenvalues of \(Q\) lie in
\([\gamma,T-(m-1)\gamma]\). Hence
\[
 N\ge(m-1)\gamma\|c\|^2.
 \tag{7}
\]
There is a second lower bound that retains the fixed marginal scale.
For any eigenvalue \(x\) of \(Q\), \(x\in[\gamma,T-\gamma]\), and
\[
 x(T-x)-\gamma(T-\gamma)
 =(x-\gamma)(T-\gamma-x)\ge0.
\]
Multiplying by \(x\ge\gamma\) gives
\(x^2(T-x)\ge\gamma^2(T-\gamma)\). Applying this scalar inequality
in an eigenbasis of \(Q\) proves
\[
 N\ge\gamma^2(T-\gamma)\|y\|^2.
 \tag{8}
\]
Multiplication of (7) and (8), followed by (6) and (3), yields
\[
 V\ge
 \frac{(m-1)\gamma^3(T-\gamma)}{4m^2\mu_4}\,\|y\|^2.
\]
Since \(\gamma\le q_L\), we have
\(T-\gamma=mq_L-\gamma\ge(m-1)q_L\).
This proves (1). Dividing the sum of coordinate variances by \(m\)
proves (2).

A simpler bound, avoiding the second spectral estimate, follows directly
from (7), (6), and \(\|Qy\|\ge\gamma\|y\|\):
\[
 V\ge\frac{(m-1)^2\gamma^4}{4m^2\mu_4}\|y\|^2.
 \tag{9}
\]
Thus even the simpler fourth-moment argument gives a polynomial gap
dependence. The sharper estimate (1) improves \(\gamma^4\) to
\(\gamma^3q_L\); no optimality claim is made.

## 4. General onset and actual-trajectory conclusions

Let \(Y=\|y\|/\sqrt m\). At training query \(v_a\), the last-layer
innovation in the initialized covariance central limit theorem contributes
\[
 \frac8{m^2}\operatorname{Var}(H_aS)
 \tag{10}
\]
to the asymptotic variance of the difference of the two independent
initial physical-time derivatives. The covariance recursion in
EARLY_VARIABILITY_AND_STORAGE.md is a sum of positive semidefinite
covariances. Earlier layers therefore cannot cancel (10).

Choose \(a_*\) as above, and let \(\sigma_{a_*}^2\) denote that full
onset variance. Equations (1) and (10) imply the more precise estimate
and its convenient consequence
\[
 \sigma_{a_*}^2
 \ge\frac{2(m-1)^2}{m^4}
           \frac{\gamma^3q_LY^2}{\mu_4}
 \ge\frac{\gamma^3q_LY^2}{2m^2\mu_4}.
 \tag{11}
\]
Taking the query to be a training input is legitimate: the initialized
theorem permits a duplicated query coordinate and singular augmented
Gaussian covariances.

For the actual-trajectory conclusion, assume the activations are real
on the real axis, holomorphic on \(|\operatorname{Im}z|<a\), and have
bounded first derivative there. Use the inherited constants
\[
 \beta=\max\left\{10,\ 1+\max_j|\phi_j(0)|,\ 16/a,\
   \max_{j,\,k=1,2}\sup_{|\operatorname{Im}z|\le a/2}
                  |\phi_j^{(k)}(z)|\right\},
 \qquad
 0<Y\le\frac{\gamma}{m}\beta^{-30L},
\]
\[
 \vartheta=\min\left\{1,\
   \frac{a(\gamma/m)}
        {1024Y^2\beta^{26L}\sqrt{d+3}}\right\}.
 \tag{12}
\]
Let \(\Phi\) be the standard normal distribution function. Applying
the proved onset-to-trajectory theorem at \(v_{a_*}\) gives, for every
fixed \(u>0\),
\[
 \liminf_{n\to\infty}\Pr\!\left\{
 \sup_{\substack{t\ge0\\\|v\|=1}}
 |f_n(t,v)-\widetilde f_n(t,v)|
 \ge
 \frac{\vartheta u\,\gamma^{3/2}Y}
      {128m\sqrt n\,\log(en)^{5/2}}
          \sqrt{\frac{q_L}{\mu_4}}
 \right\}
 \ge2[1-\Phi(u)].
 \tag{13}
\]
The only weakening is \(1/(64\sqrt2)\ge1/128\).
The same bound is witnessed at the single training query and some
physical time in
\([0,\vartheta/\sqrt{\log(en)}]\).

One can remove the extra scalar moments from a conservative displayed
coefficient. Linear growth and \(\beta\ge10\) give
\[
 \max(1,q_j)\le4\beta^2\max(1,q_{j-1})\le\beta^{3j},
\]
where the final expression follows by induction. In particular,
\[
 \mu_4\le8\beta^4+24\beta^4q_{L-1}^2
 \le32\beta^{6L-2}\le\beta^{6L},\qquad q_L\ge\gamma.
 \tag{14}
\]
Thus (13) remains valid with its lower threshold replaced by
\[
 \frac{\vartheta u\,\gamma^2Y}
      {128m\beta^{3L}\sqrt n\,\log(en)^{5/2}}.
 \tag{15}
\]
Equations (13)–(15) apply to arbitrary fixed depth and general finite
training inputs with \(Q\succ0\), for every nonzero label direction,
when \(m\ge2\). They add no activation symmetry, bounded-value, data
orthogonality, or centered-covariance hypothesis.

All problem parameters are fixed in this limit. The inherited initialized
central limit theorem and source event do not yet provide an effective
confidence-dependent width threshold. Taking
\(u=\Phi^{-1}(1/2+\delta/4)\) gives a lower bound with probability at least
\(1-\delta\) at every sufficiently large individual width. No simultaneous
claim over infinitely many independently sampled widths is made.

This is a transient prediction lower bound in the common trajectory norm.
At the selected training input, both fitted endpoints equal the same
label. Therefore this argument provides no endpoint separation. It also
does not remove the factor \(\log(en)^{-5/2}\) or establish a necessary
storage lower bound.

## 5. Exact one-sample exception

For \(m=1\), the last innovation has variance
\[
 \operatorname{Var}(H_1S)
 =Y^2\eta,\qquad
 \eta=\mu_4-q_L^2=\operatorname{Var}
       \big(\phi_L(\sqrt{q_{L-1}}G)^2\big).
 \tag{16}
\]
Under continuity of the real activation and \(Q=q_L>0\),
\(\eta=0\) holds exactly when either \(q_{L-1}=0\) or
\(\phi_L\) is constant on the real axis.

If \(q_{L-1}>0\), the Gaussian has full support on the real line.
Variance zero would make \(\phi_L(t)^2\) one fixed positive number for
every real \(t\), by continuity. A continuous map from the connected
real line into the two-point set of its possible square roots must be
constant. Conversely a constant activation, or a zero preactivation
variance, makes the final feature deterministic.

These effective-constant cases give actual deterministic predictor
dynamics, not merely a vanishing last-layer innovation. For a constant
last activation \(c\ne0\), every hidden gradient vanishes. If instead
\(q_{L-1}=0\), start with \(q_0=1\) and choose the last index \(j<L\)
where a positive \(q_{j-1}\) becomes zero. Continuity and Gaussian full
support force \(\phi_j\equiv0\). Every subsequent moment up to
\(q_{L-1}\) is zero, and hence each subsequent activation vanishes at
zero; otherwise a later return to zero would contradict the chosen
last index. These layers therefore output zero for every parameter
choice, and the top layer outputs the constant \(c=\phi_L(0)\ne0\).
The hidden flow is stationary in both cases. With zero readout,
\[
 f_n(t,v)=y(1-e^{-2c^2t})
 \tag{17}
\]
for every width, initialization, and query.

Outside these exceptions \(\eta>0\), and the full onset variance is at
least \(8Y^2\eta\). The inherited general theorem therefore gives the
same trajectory conclusion with lower threshold, for example,
\[
 \frac{\vartheta uY\sqrt\eta}
      {32\sqrt n\,\log(en)^{5/2}}.
 \tag{18}
\]
Here \(\eta\) is an explicit positive activation/depth constant.

There is no positive one-sample onset coefficient uniform in
\(\beta,\gamma\) alone, even after excluding exactly constant
activations. Take identity activations in the first \(L-1\) layers and
\[
 \phi_L(t)=\sqrt{1-\varepsilon^2}+\varepsilon t,
 \qquad 0<\varepsilon<1.
 \tag{19}
\]
Then \(q_{L-1}=q_L=\gamma=1\), all the strip envelopes can use the
same \(\beta=10\), and
\[
 \eta=4\varepsilon^2-2\varepsilon^4\longrightarrow0.
 \tag{20}
\]
In fact the entire scalar initialized covariance recursion gives
\[
 C_L=4\varepsilon^2+2(L-2)\varepsilon^4\longrightarrow0:
\]
the first \(L-1\) identity layers contribute \(C_{L-1}=2(L-1)\),
the last derivative map is multiplication by \(\varepsilon^2\),
and its new innovation is (20). Thus the full onset variance, not only
its final innovation contribution, tends to zero at fixed gap and
uniform strip bounds.

The \(m\ge2\) result has no such exception because a deterministic
rank-one feature family cannot have \(Q\succ0\). The earlier source
qualification that positive training gap does not always force onset
nondegeneracy remains correct for one sample and for a prescribed
arbitrary query, but it is unnecessary for the maximum over training
queries when \(m\ge2\).
