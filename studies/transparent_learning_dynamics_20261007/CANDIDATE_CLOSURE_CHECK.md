# Conceptual closure check: two hidden nonlinear layers

2026-10-07. Independent bounded audit of the candidate state consisting of full causal local laws and their first, frozen-coefficient tangent fields. Scientific inputs were the complete CAUSAL_KERNEL_DYNAMICS.md and RESPONSE_GAUSSIAN_CLOSURE.md, plus the assigned finite-program setup. No continuum derivation, other audit, external source, experiment, or new width-rate proof was used.

## Verdict

The finite chronological candidate is genuinely closed when its state includes the prescribed local circuits, the joint laws of their full histories, and the joint first tangent fields needed to evaluate the response coefficients. Its construction does not require a learned matrix, a future dense trajectory, or a second-order tangent hierarchy. This is stronger than an unclosed list of moments, but weaker than a finite-dimensional Markov closure.

The honest continuous-time candidate is a causal, history-dependent population path law together with its first response operator. The finite-program proof alone does not establish that this continuous-time object exists, is unique, or is the limit of the discrete response construction. Those qualifications cannot be removed merely by replacing sums with integrals.

## 1. An explicit finite two-layer test

Let $a=1,\ldots,p$ index a declared training/passive panel, with training indices $a\leq m$. Put $S_{ab}=v_a^\top v_b$ and $\alpha=2/m$. The Euler step is $\Delta t$, and $c_a^k=y_a-f_a^k$ for training indices only. There are two scalar neuron populations.

In the lower population, retain $z_{1,a}^k$, $h_{1,a}^k=\phi_1(z_{1,a}^k)$, $b_{1,a}^k$, and $\delta_{1,a}^k=\phi_1'(z_{1,a}^k)b_{1,a}^k$. In the upper population retain $z_{2,a}^k$, $h_{2,a}^k=\phi_2(z_{2,a}^k)$, the common readout $w^k$, and $\delta_{2,a}^k=w^k\phi_2'(z_{2,a}^k)$.

There is one initialized square interface. Its upper primitive family is $\eta_a^k$ and lower primitive family is $\xi_a^k$. Their covariance kernels are, respectively,

\[
\mathbb E[\eta_a^k\eta_b^j]=\mathbb E[h_{1,a}^k h_{1,b}^j],
\qquad
\mathbb E[\xi_a^k\xi_b^j]=\mathbb E[\delta_{2,a}^k\delta_{2,b}^j].
\tag{1}
\]

The two families and the initial lower Gaussian panel are mutually independent; coordinates within a family generally are not. In this section all expectations use the relevant local population.

Abbreviate the source kernels by $C_{1,ab}(k,j)$, $D_{2,ab}(k,j)$, $R^h_{ab}(k,j)$ and $R^\delta_{ab}(k,j)$. The complete primal circuit is

\[
\begin{aligned}
z_{1,a}^k
 &=z_{1,a}^0+\alpha\Delta t\sum_{j<k,b\leq m}
    c_b^j S_{ab}\delta_{1,b}^j,\\
w^k
 &=\alpha\Delta t\sum_{j<k,b\leq m}c_b^j h_{2,b}^j,\\
z_{2,a}^k
 &=\eta_a^k+\sum_{j<k,b\leq p}R^h_{ab}(k,j)\delta_{2,b}^j
   +\alpha\Delta t\sum_{j<k,b\leq m}
       c_b^j C_{1,ab}(k,j)\delta_{2,b}^j,\\
b_{1,a}^k
 &=\xi_a^k+\sum_{j\leq k,b\leq p}R^\delta_{ab}(k,j)h_{1,b}^j
   +\alpha\Delta t\sum_{j<k,b\leq m}
       c_b^j D_{2,ab}(k,j)h_{1,b}^j,\\
f_a^k&=\mathbb E[w^k h_{2,a}^k].
\end{aligned}
\tag{2}
\]

The covariance and response arrays in (2) are computed from these same laws, not supplied externally. The response definitions are

\[
R^h_{ab}(k,j)
=\mathbb E[\partial_{\xi_b^j}h_{1,a}^k],\qquad
R^\delta_{ab}(k,j)
=\mathbb E[\partial_{\eta_b^j}\delta_{2,a}^k].
\tag{3}
\]

Each derivative holds all deterministic population coefficients fixed. In particular it does not differentiate the quantities $c,C,D,R$ occurring in (2).

## 2. First tangents suffice: a direct check

Fix a lower primitive coordinate $q=(b,j)$ and define the random first tangent fields

\[
u_a^k(q)=\partial_{\xi_b^j}z_{1,a}^k,\qquad
v_a^k(q)=\partial_{\xi_b^j}b_{1,a}^k,\qquad
t_{1,a}^k(q)=\partial_{\xi_b^j}\delta_{1,a}^k.
\]

All are zero before their probe coordinate is introduced. Differentiating (2) with the stipulated convention gives

\[
\begin{aligned}
u_a^k(q)
 &=\alpha\Delta t\sum_{r<k,d\leq m}c_d^r S_{ad}t_{1,d}^r(q),\\
v_a^k(q)
 &=\mathbf1_{\{q=(a,k)\}}
   +\sum_{r\leq k,d\leq p}R^\delta_{ad}(k,r)
       \phi_1'(z_{1,d}^r)u_d^r(q)\\
 &\quad+\alpha\Delta t\sum_{r<k,d\leq m}
       c_d^rD_{2,ad}(k,r)\phi_1'(z_{1,d}^r)u_d^r(q),\\
t_{1,a}^k(q)
 &=\phi_1''(z_{1,a}^k)b_{1,a}^k u_a^k(q)
   +\phi_1'(z_{1,a}^k)v_a^k(q),\\
\partial_{\xi_b^j}h_{1,a}^k
 &=\phi_1'(z_{1,a}^k)u_a^k(q).
\end{aligned}
\tag{4}
\]

Now fix an upper primitive coordinate $q=(b,j)$ and put

\[
s_a^k(q)=\partial_{\eta_b^j}z_{2,a}^k,\qquad
\omega^k(q)=\partial_{\eta_b^j}w^k,\qquad
t_{2,a}^k(q)=\partial_{\eta_b^j}\delta_{2,a}^k.
\]

Then

\[
\begin{aligned}
s_a^k(q)
 &=\mathbf1_{\{q=(a,k)\}}
   +\sum_{r<k,d\leq p}R^h_{ad}(k,r)t_{2,d}^r(q)\\
 &\quad+\alpha\Delta t\sum_{r<k,d\leq m}
       c_d^rC_{1,ad}(k,r)t_{2,d}^r(q),\\
\omega^k(q)
 &=\alpha\Delta t\sum_{r<k,d\leq m}
       c_d^r\phi_2'(z_{2,d}^r)s_d^r(q),\\
t_{2,a}^k(q)
 &=w^k\phi_2''(z_{2,a}^k)s_a^k(q)
   +\phi_2'(z_{2,a}^k)\omega^k(q).
\end{aligned}
\tag{5}
\]

Averaging the last line of (4) and the last line of (5) gives (3). Equations (4)–(5) retain correlations between the primal fields and their tangents; replacing their expectations by products of expectations would not be valid.

These are linear equations in the random tangent fields along the already constructed random primal path. Their coefficients contain $\phi'$ and $\phi''$, but no second derivative of a random field with respect to primitive coordinates. There is no need to differentiate a tangent equation in a second primitive direction. Thus no hierarchy of second, third, and higher stochastic tangents is introduced by this construction.

This is not an assertion that the evolving expectations $R^h,R^\delta$ obey a closed ODE by themselves. If one instead differentiated these expectations with respect to a population-wide perturbation, or insisted on eliminating the full local law in favor of finitely many moments, additional responses or higher moments could appear. That is a different closure problem.

## 3. Why the finite construction is causal, including its current-time term

At Euler step $k$, lower $z_1^k,h_1^k$ and their tangents are obtained from completed strict-past backward fields. They determine the new forward covariance row and $R^h(k,j)$ for $j<k$. Appending the upper Gaussian coordinate then gives $z_2^k,h_2^k$, with $w^k$ already determined by the strict past. Consequently the output, deficits, upper backward inputs, and their tangents are known before the new reverse Gaussian coordinate is appended.

Only then is $b_1^k$ formed. Its current-step coefficient is already known from the upper population. In particular,

\[
R^\delta_{ab}(k,k)
=\mathbf1_{a=b}\,\mathbb E[w^k\phi_2''(z_{2,a}^k)].
\tag{6}
\]

There is therefore no same-time fixed-point problem in the finite program: the apparent current-time feedback in $b_1^k$ is triangular across layers. The newly formed $\delta_1^k$ influences $z_1^{k+1}$, not $z_1^k$.

The Gaussian covariance extensions exist at every event because their entries are uncentered second moments of already defined query fields. Such a matrix is positive semidefinite. The extension can be singular; a dependent new coordinate is introduced as its corresponding linear combination instead of requiring a fresh innovation. Smooth canonical circuit differentiation remains defined with formal primitive coordinates. Only the response-weighted fields, not every individual coefficient in a singular representation, are invariant under admissible off-support changes.

Passive indices can be observed without becoming training forces. Every learned-write sum in (2), (4), and (5) has $d\leq m$. The reciprocal sums over the full panel track observations of the same initialized map. In the canonical circuit, active queries do not depend on passive formal primitives, so the associated active-to-passive derivative entries vanish; adding passive observations does not change the active law.

## 4. What the state actually is

For a fixed number $K$ of Euler steps and fixed panel size $p$, the state admits a finite symbolic representation: a finite Gaussian root/primitive vector, its covariance arrays, a prescribed local scalar computation graph, and its first-derivative graph. The graph and coefficient arrays are independent of network width. With two populations, the number of primitive coordinates is $O(pK)$; full sample/time tangent and covariance tables require $O(p^2K^2)$ scalar slots, up to fixed field-type factors. Exact evaluation of the nonlinear Gaussian expectations is not thereby reduced to a fixed-cost calculation.

As a probability measure the full joint law is a population object, not a finite vector of covariances. Its finite-horizon circuit representation is legitimate and useful, but the retained history and Gaussian integration dimension grow with $K$. The continuum analogue carries paths and probe-time-indexed response fields, hence is naturally an infinite-dimensional, memory-dependent law. One can call it Markov only after retaining the whole history as state, which does not produce the finite-dimensional restartable ODE the stronger target would require.

The phrase “full local-path laws plus first tangent kernels” must also be made precise:

- If “tangent kernels” means the joint random tangent fields, or the explicit tangent computation rule together with the full primitive-to-field circuit, this supplies (4)–(5) and is sufficient at finite horizon.
- If it means only the averaged arrays $R^h,R^\delta$, with unspecified local response rules, it is not enough. Future terms need averages such as $\mathbb E[\phi''(z)b u]$, including their joint dependence.
- Primal path marginals alone do not prescribe an off-support derivative on a singular Gaussian support. A canonical causal circuit or an equivalent probe-response rule is part of the specification, even though observable response sums are invariant under the allowed choice.

These are specification distinctions, not evidence of a missing higher-tangent hierarchy in the correctly augmented finite program.

## 5. Is this just weights renamed?

Not in the literal or computational sense relevant here. The state contains no learned $n\times n$ matrix, no coordinate pairing between individual neurons in adjacent populations, and no access to a realized dense initialized operator. The two populations communicate through population expectations, colored Gaussian covariances, and causal response coefficients. At any fixed query count the law has a width-independent circuit description and forgets individual-neuron labels and weight-matrix orientation. Many dense microscopic realizations have the same limiting state.

The candidate nevertheless retains rich nonlinear information: complete local histories and how those histories respond to primitive probes. It is a statistical single-neuron process with self-consistent colored forcing and memory, not a small macroscopic kernel ODE. Describing it as “only a few kernels” would hide the state responsible for its closure. Describing it as “the same dense weights under another name” would hide the genuine removal of inter-neuron matrices and the causal Gaussian reduction.

Mechanistically, it separates feature agreement, agreement of backward loss responses, actual learned rank-one writes, and reciprocal corrections caused by reusing one initialized map in both directions. Those distinctions remain meaningful even if exact integration over the local path law is expensive.

## 6. Critical holes that remain for a continuous candidate

The finite-program result supports a precise candidate, but not an unconditional continuous-law theorem. The remaining obligations are:

1. Specify the path and response spaces, including how a local probe at a time enters the primitive path. A derivative with respect to a point coordinate in a finite Gaussian vector does not automatically become a well-defined derivative kernel on a Gaussian path space.
2. Give a consistent limit of the growing discrete covariance/response laws. Bounds on field paths alone do not bound the first-response operator or establish convergence of its expectation.
3. Treat diagonal response terms explicitly. The current-time term (6) is order one, whereas strict-past response coefficients may converge through a time-integrated kernel. An endpoint atom cannot be silently absorbed into an ordinary integral density.
4. Establish causal well-posedness of the proposed self-consistent continuum law, including any regularity and integrability used to exchange derivatives, expectations, and time limits. Finite-step triangularity is supporting structure, not a proof of all these analytic limits.
5. Distinguish the population law from a width-dependent realization at the network's fluctuation scale. No quantitative accuracy claim follows from conceptual closure alone.

None of these holes says that a first-tangent formulation necessarily fails. They delimit the proved finite chronological object from the proposed continuous, history-dependent closure. A transparent presentation should name that object first and use a concrete two-hidden-layer interacting-sample/passive example to explain its mechanism before asking for stronger approximation theorems.
