# Smooth nonanalytic route: exact obstructions and the missing dense-network witness

Status: bounded theoretical search completed; the requested worst-case dense-network lower bound is **open on this route**. The propositions below are self-contained exact results, not an independently reviewed theorem for the canonical network. No experiments, Git writes, or shared-book changes were made.

Input scope: the supervisor's scoped assignment; `docs/index.qmd` and `docs/notation.qmd`; the official Huang–Yau paper, specifically its model and Assumption 2.1; required process and mathematical-presentation skills. No other study, other route, or archived-book material was read. Author: scoped agent `worst_smooth_witness`, 2026-10-10.

## Contract and admissible regularity

The target network has two hidden layers of width $n$,

$$
z_a^{(1)}=W^{(1)}x_a/\sqrt d,\quad
h_a^{(1)}=\phi_1(z_a^{(1)}),\quad
z_a^{(2)}=W^{(2)}h_a^{(1)},\quad
f_a=u^T\phi_2(z_a^{(2)})/n.
$$

Here $m$ training inputs and their labels are fixed, the loss is
$\mathcal L=(2m)^{-1}\sum_a(f_a-y_a)^2$, and the parameter mobility is
$M_n=\operatorname{diag}(nI,I,nI)$ on $(W^{(1)},W^{(2)},u)$. Initialization has independent entries $W^{(1)}_{ij}\sim N(0,1)$ and $W^{(2)}_{ij}\sim N(0,1/n)$, with $u=0$. A passive test input does not appear in the loss.

Write $r_a=f_a-y_a$ and define the original ordered hierarchy by

$$
K_1(a)=f_a,\qquad
K_{s+1}(a,b_2,\ldots,b_s,b)
=D K_s(a,b_2,\ldots,b_s)[M_n\nabla f_b].
$$

The first index may be a test input; all driving indices are training indices. The rank-$q$ closure copies $K_s(0)$ for $s\le q$, freezes $K_q$, and evolves

$$
\dot{\widehat K}_s(a,b_2,\ldots,b_s)
=-\frac1m\sum_b
\widehat K_{s+1}(a,b_2,\ldots,b_s,b)\widehat r_b,
\qquad s<q,
$$

using its own residual $\widehat r_b=\widehat K_1(b)-y_b$. No restarts or alternative closures are permitted. The desired conclusion concerns prediction error on a fixed physical interval, Gaussian high probability, one fixed activation and nondegenerate dataset, and literal ordered-tensor storage $\sum_{s\le q}m^s$ when $m\ge2$.

Huang–Yau Assumption 2.1 requires smoothness and a separate finite bound on each derivative through order $2p^*+1$, for each fixed order cutoff. It does not impose analyticity or a common analytic derivative-growth estimate. Smooth periodic functions and smooth compact bumps with bounded derivatives of every fixed order satisfy this activation requirement. The paper uses a different normalization and Gaussian readout initialization, so its quantitative theorem cannot simply be transferred to the model above. Source: [Huang and Yau, *Dynamics of Deep Neural Networks and Neural Tangent Hierarchy*, Assumption 2.1, PDF p. 4](https://proceedings.mlr.press/v119/huang20l/huang20l.pdf).

## 1. Exact all-order blindness is sufficient, even with the closure's own residual

**Proposition 1.** Fix an initialized smooth finite-parameter model and a passive test index $*$. If

$$
K_s(*,b_2,\ldots,b_s;0)=0
\quad\text{for every }s\ge1\text{ and every training-index tuple},
$$

then every finite frozen-top hierarchy predicts $\widehat f_*(t)=0$ throughout its interval of existence. This conclusion does not require the training residuals to be frozen, small, or externally prescribed.

**Proof.** For a fixed $q$, the frozen top tensors with first index $*$ are zero. The derivative of each level-$q-1$ test tensor is a contraction of these zero tensors against the closure's own residual, hence vanishes. Its copied initial value is zero. Descending induction gives zero test tensors at every lower level, including $\widehat f_*$. This works for every finite $q$. $\square$

Thus a canonical-network construction satisfying these zero-jet identities with high probability, while $|f_*(T)|$ exceeds the actual dense variability, would give a stronger conclusion than exponential storage: no finite rank would suffice. The unproved part is constructing that event under the required iid Gaussian initialization without suppressing learning.

There is a complete smooth counterexample for general parametric observables, demonstrating that the obstruction is mathematically real but not realizing the required architecture. Let $\theta=(v,w)$, $M=I$, two training outputs $f_1=v,f_2=w$, labels $(1,2)$, and $\theta(0)=(0,0)$. The half-MSE is

$$
\mathcal L=\frac14[(v-1)^2+(w-2)^2],\qquad
v(t)=1-e^{-t/2},\quad w(t)=2(1-e^{-t/2}).
$$

The training Jacobian is the identity and both coordinates learn. Set

$$
\chi(z)=\begin{cases}e^{-1/z^2},&z>0,\\0,&z\le0,\end{cases}
\qquad f_*(v,w)=\chi(v-1/4).
$$

Every derivative of $\chi$ is bounded: on $z>0$ its derivatives are a finite sum of powers of $1/z$ times $e^{-1/z^2}$; these tend to zero as $z\downarrow0$, and derivatives are bounded at infinity. The test function is identically zero near the initial parameters. Since the training vector fields are $\partial_v$ and $\partial_w$, every initial test hierarchy entry is zero. Rank $q\ge2$ reproduces the training predictions exactly, but Proposition 1 gives $\widehat f_*(t)=0$ for every $q$. At $T=2\log2$, the actual prediction is $f_*(T)=e^{-16}>0$.

This example has active, independently fitted training coordinates and no residual forcing from outside the closure. Its fatal mismatch with the target is the observable architecture and deterministic hidden initialization: a nonlinear function is applied directly to the evolving coordinate $v$. In the prescribed network the zero-initialized readout is followed by no activation, while hidden preactivations start Gaussian. The toy is not a proof about the requested network or its width fluctuations.

## 2. A fixed unseen bump does not occur with Gaussian high probability

**Proposition 2.** Fix a nonzero input $x$, a continuous nonzero first-layer activation $\phi_1$ with bounded first derivative, and a nonempty open interval $B\subset\mathbb R$. Under the canonical initialization there exist fixed $c,C>0$, depending on these choices but not on $n$, such that

$$
\mathbb P\{z_i^{(2)}(x)\notin B\text{ for all }1\le i\le n\}
\le Ce^{-cn}.
$$

For first-layer preactivations the corresponding assertion holds directly whenever $x\ne0$.

**Proof.** Put $\sigma_x^2=\|x\|^2/d>0$. The first-layer preactivations are iid $G_j\sim N(0,\sigma_x^2)$. Conditional on them, the independent second-layer rows give iid

$$
z_i^{(2)}(x)\mid (G_j)_{j\le n}\sim N(0,v_n),
\qquad v_n=\frac1n\sum_j\phi_1(G_j)^2.
$$

Continuity, nonzero $\phi_1$, and the positive Gaussian density imply
$v=\mathbb E\phi_1(G)^2>0$. The bounded derivative gives
$|\phi_1(z)|\le |\phi_1(0)|+L|z|$, so $\phi_1(G)^2$ has a finite exponential moment near the origin. For completeness, this moment yields exponential concentration of $v_n$ between fixed constants: for the upper tail, choose $v_+>v$ and sufficiently small $\lambda>0$ such that
$\log\mathbb E e^{\lambda\phi_1(G)^2}<\lambda v_+$; exponential Markov gives $\mathbb P(v_n>v_+)\le e^{-c_+n}$. For the lower tail choose $0<v_-<v$ and sufficiently small $\lambda>0$ such that
$\log\mathbb E e^{-\lambda\phi_1(G)^2}<-\lambda v_-$; the same argument gives $\mathbb P(v_n<v_-)\le e^{-c_-n}$. These choices follow by differentiating each log moment at zero, whose derivative is $\pm v$.

For $v'\in[v_-,v_+]$, the probability $p(v')=\mathbb P\{N(0,v')\in B\}$ is continuous and strictly positive. Thus its minimum $p_0$ on this compact interval is positive. Conditional independence gives an avoidance probability at most $(1-p_0)^n\le e^{-p_0n}$ on the good variance event. Adding the two variance-tail probabilities proves the assertion. The first-layer version is simply $(1-\mathbb P\{G\in B\})^n$. $\square$

Consequences are limited but decisive for the simplest construction:

- If a fixed nonzero bump is added to an activation, it differs from the baseline on an open interval. The event that all scalar preactivations avoid that interval has exponentially small probability, not probability tending to one.
- Taking a very remote but fixed bump changes the constant $c$ and the onset width; it does not change the asymptotic conclusion.
- Width-dependent bump locations, shrinking bumps, growing input thresholds, or order-dependent activation choices would violate the fixed-instance target.
- This does **not** prove that NTH tensors determine the activation, nor that all smooth nonanalytic lower-bound routes fail. Exact tensor cancellations or a quantitatively small but initially visible component are not addressed by Proposition 2.

The special test input $x=0$ does not give the obvious escape. Its first-layer vector is the fixed constant $\phi_1(0)\mathbf1$. If $\phi_1(0)\ne0$, the second-layer preactivations are iid nondegenerate Gaussians, so the same avoidance argument applies. If $\phi_1(0)=0$, then $h^{(1)}(0)=0$ and $z^{(2)}(0)=0$ for all training times. Choosing $\phi_2$ flat and zero at zero makes the actual test output zero forever; no missed activation event occurs. If $\phi_2(0)\ne0$, the test prediction is $\phi_2(0)n^{-1}\sum_i u_i$, so it is not an initially invisible flat test feature.

## 3. A fixed admissible activation with severe derivative growth

An explicit activation worth retaining for a different attack is

$$
\phi(z)=\sum_{k=1}^{\infty}e^{-\sqrt k}\cos(kz).
$$

For each fixed derivative order $r$, the series of derivative suprema is bounded by $\sum_k k^r e^{-\sqrt k}<\infty$. To verify convergence, group $j^2\le k<(j+1)^2$: the group is bounded by $(2j+1)(j+1)^{2r}e^{-j}$, whose series converges by the ratio test. Uniform convergence of all derivative series permits termwise differentiation, so $\phi\in C^\infty$ and every fixed-order derivative is bounded. The activation and its bounds are independent of width.

Nevertheless, for every integer $r\ge1$, all summands of the even derivative at zero have the same sign, and selecting $k=16r^2$ gives

$$
\frac{|\phi^{(2r)}(0)|}{(2r)!}
\ge \frac{(16r^2)^{2r}e^{-4r}}{(2r)!}
\ge (8r)^{2r}e^{-4r}.
$$

Thus its Taylor series at zero has radius zero. Adding a fixed constant, or multiplying by a fixed nonzero small constant, preserves the conclusion and can make the activation positive if useful.

There is a quantitative empirical-derivative obstruction in a translation benchmark. It is stated only as a benchmark, because translation of independent scalar coordinates has not been derived from the canonical trained network. For $Z\sim N(0,1)$, fixed $T>0$, and Taylor degree $q$, set

$$
P_q(Z,T)=\sum_{j=0}^q\frac{T^j}{j!}\phi^{(j)}(Z),
\qquad R_q(Z,T)=P_q(Z,T)-\phi(Z+T).
$$

For all sufficiently large $q$,

$$
\operatorname{Var}R_q(Z,T)\ge c\left(\frac{Tq}{e}\right)^{2q},
$$

where $c>0$ is independent of $q$. To prove this, use the frequency $k=q^2$ and write $A=kT$. For $q$ large enough that $A\ge3q$, the leading term of $E_q(iA)=\sum_{j=0}^q(iA)^j/j!$ dominates the others:

$$
\sum_{j=0}^{q-1}\frac{A^j}{j!}
\le \frac{A^q}{q!}\sum_{r=1}^q(q/A)^r
\le\frac12\frac{A^q}{q!}.
$$

Hence $|E_q(iA)|\ge A^q/(2q!)$ and, for sufficiently large $q$,
$|E_q(iA)-e^{iA}|\ge A^q/(4q!)$. The corresponding complex Fourier multiplier of $R_q$ has magnitude at least
$e^{-q}(q^2T)^q/(4q!)$. Under uniform measure on $[-\pi,\pi]$, distinct Fourier frequencies are orthogonal and $R_q$ has mean zero. Under the Gaussian, reduce modulo $2\pi$: its wrapped density is bounded below by $(2\pi)^{-1/2}e^{-\pi^2/2}>0$ on that interval. For every constant $a$,

$$
\mathbb E(R_q(Z,T)-a)^2
\ge c_0\int_{-\pi}^{\pi}(R_q(z,T)-a)^2\,dz.
$$

Minimizing in $a$, Fourier orthogonality bounds the Gaussian variance below by a constant times the squared multiplier just obtained. Finally $q!\le q^q$ gives the displayed inequality after changing $c$.

For iid $Z_1,\ldots,Z_n$, the empirical Taylor-error variance is exactly $\operatorname{Var}R_q(Z,T)/n$, while the actual empirical translated prediction $n^{-1}\sum_i\phi(Z_i+T)$ has variance at most $\|\phi\|_\infty^2/n$. This identifies a concrete mechanism: increasingly high derivatives of a fixed admissible activation can amplify empirical noise far above the true prediction's sampling variability.

This variance statement is **not** a high-probability lower bound, and large variance alone cannot supply one; rare outcomes might dominate it. It also does not identify the frozen-top NTH with a Taylor polynomial in physical time. These are substantive missing implications, not presentational details.

## 4. Exact remaining obligations and stopping decision

The all-order flat-jet route needs a canonical-network realization of Proposition 1 with a fixed admissible activation, Gaussian high probability, active feature learning, and a nonzero later test prediction. The simple open-bump invisibility construction is ruled out by Proposition 2. The general realization question remains open.

The derivative-noise route needs all of the following before it answers the user's question:

1. Derive an actual canonical-network prediction contribution with the required derivative growth, including all parameter blocks, contractions, correlations, and zero-readout parity effects. The scalar translation benchmark is not this derivation.
2. Control the closure's own evolving residual and prove that the contribution survives its feedback. Supplying the exact dense residual would change the algorithm.
3. Convert growth of coefficients or variance into prediction-error lower bounds with the requested probability, allowing cancellation between levels and paths and covering every candidate rank in the alleged accuracy regime.
4. Establish the actual dense prediction fluctuation scale for the same fixed activation, data, test observable, and interval. A generic $n^{-1/2}$ comparison cannot be assumed after an adversarial activation is chosen.
5. Deduce a necessary rank $q(n)\gg\log n$ (superpolynomial literal storage), $q(n)\gtrsim n^\alpha$ (exponential-in-a-power storage), or failure of every finite rank. Failure of one fixed rank, failure of Taylor convergence for a scalar function, or failure of one upper-bound proof proves none of these conclusions.

Registry recommendation: stop this bounded route as **open with exact partial results**. Reopen only with a new dense-network realization or a direct high-probability NTH error estimate that bypasses it. The admissibility check widens the candidate activation class, but it does not currently establish the requested worst-case lower bound.
