# Case Study: Mean-Field Peeling for a μP Network at Initialization, After One Step, and After Two Steps

**Status:** Maintained worked execution  
**Date:** 2026-08-03  
**Consolidated:** 2026-08-05  
**Role:** A self-contained, low-level execution of the mean-field peeling program on one fixed network and three increasingly difficult observables.
**Canonical theory:**
[`CURRENT_RESEARCH_STATE.md`](CURRENT_RESEARCH_STATE.md)

This case study performs three calculations in one notation:

1. the initialization backward-sensitivity kernels;
2. the output and loss changes after one gradient-descent step through order
   $\eta$, and the hidden-Gram change through order $\eta^2$;
3. the hidden-Gram changes after two gradient-descent steps, through order $\eta^2$, including the correction caused by updating the gradient itself.

The purpose is not merely to quote the answers. Every calculation is organized in the order required by mean-field peeling:

1. fix the raw/effective parameter and optimizer scalings;
2. expand derivatives and training updates before taking a width limit;
3. scalarize the highest active group;
4. peel the readout first;
5. apply exact conditional Wick--Stein identities to the highest hidden group;
6. retain every lower-group factor created by Stein differentiation;
7. split equality patterns before width counting;
8. replace normalized empirical averages by deterministic Gaussian expectations only after all indices using them have been exposed;
9. repeat downward through the network;
10. audit the result by parity, scaling, and a solvable deep-linear specialization.

The finite-width Taylor and chain-rule identities below are exact. The mean-field limits require the regularity assumptions stated in Section 2.7.

## Document map

- [Section 1](#1-headline-results) states the consolidated answers.
- [Section 2](#2-fixed-network-batch-initialization-and-μp-update) fixes one raw-coordinate μP convention.
- [Section 3](#3-the-two-exact-gaussian-identities-used-in-every-peel) derives the Gaussian identities.
- [Section 4](#4-execution-i-backward-sensitivity-kernels) executes the backward-kernel peel.
- [Section 5](#5-execution-ii-one-gradient-descent-step) computes the one-step coefficients.
- [Section 6](#6-execution-iii-two-gradient-descent-steps) computes the two-step gradient correction.
- [Section 7](#7-what-this-case-study-changes-in-the-peeling-program) records amendments to the general program.
- [Appendix A](#appendix-a-general-fixed-depth-backward-kernel-template) records the arbitrary-fixed-depth readout-scaled backward template.
- [Appendix B](#appendix-b-complete-two-sample-five-branch-backward-audit) gives the complete five-branch structural formula omitted from the earlier branch-order summary.

## Claim-status convention

- **Exact finite-width identity** means no width limit or independence approximation has been used.
- **Mean-field result** means the coefficient follows from the displayed peel under the smoothness, moment, leave-one-out, and concentration assumptions in Section 2.7.
- **Formal mean-field closure** means the finite state and every required Wick--Stein operation have been specified, but a joint convergence theorem for the complete state has not yet been supplied. The general nonlinear two-step recursion has this status; its deep-linear specialization is explicitly audited.

---

# 1. Headline results

For the network defined below, let

$$
G^\ell_{n,ab}
=
\frac1n\sum_i h_i^\ell(a)h_i^\ell(b),
\qquad \ell=1,2,3,
$$

be the hidden activation Gram between batch samples $a$ and $b$.

At initialization, the executed one-copy peel proves that the expectations of
the normalized backward kernels converge to

$$
\Pi^3_{ab}=D^3_{ab},
$$

$$
\Pi^2_{ab}=D^2_{ab}D^3_{ab},
$$

$$
\Pi^1_{ab}=D^1_{ab}D^2_{ab}D^3_{ab}.
$$

Conditional on the separate concentration obligation in Section 4.4, the
random empirical kernels themselves converge to these limits in $L^2$.

For one gradient-descent step, the expected sample loss has the linear expansion

$$
\mathbb E[(f_a^+-y_a)^2]
=
y_a^2
-
\frac{4\eta}{B}y_a\sum_bK_{ab}y_b
+o(\eta)+o_n(1),
$$

where

$$
\begin{aligned}
K_{ab}
={}&G^3_{ab}
+G^2_{ab}D^3_{ab}
+G^1_{ab}D^2_{ab}D^3_{ab}
\\
&+G^0_{ab}D^1_{ab}D^2_{ab}D^3_{ab}.
\end{aligned}
$$

The expected hidden-Gram linear coefficient vanishes at infinite width:

$$
\lim_{n\to\infty}
\left.
\frac{d}{d\eta}
\mathbb E[G^{\ell,+}_{n,ab}]
\right|_{\eta=0}
=0.
$$

Its first generic deterministic coefficient is quadratic:

$$
\mathbb E[G^{\ell,+}_{n,ab}]
=
G^\ell_{ab}
+\eta\,O(n^{-1})
+\eta^2C^\ell_{ab}
+o(\eta^2)+o_n(1).
$$

After two Euler gradient-descent steps,

$$
\mathbb E[G^{\ell,(2)}_{n,ab}]
=
G^\ell_{ab}
+\eta\,O(n^{-1})
+\eta^2\bigl(4C^\ell_{ab}+R^\ell_{ab}\bigr)
+o(\eta^2)+o_n(1),
$$

where $R^\ell$ is the new gradient-correction term. The change produced by the second update alone is

$$
\mathbb E[G^{\ell,(2)}_{n,ab}-G^{\ell,(1)}_{n,ab}]
=
\eta\,O(n^{-1})
+\eta^2\bigl(3C^\ell_{ab}+R^\ell_{ab}\bigr)
+o(\eta^2)+o_n(1).
$$

Neither two-step quantity has a deterministic $O(\eta)$ hidden-Gram term.

---

# 2. Fixed network, batch, initialization, and μP update

## 2.1 Indices

- Batch indices are $a,b,c,d\in\{1,\ldots,B\}$.
- First-hidden-layer neuron indices are $i,j$.
- Second-hidden-layer neuron indices are $p,q$.
- Third-hidden-layer neuron indices are $r,t$.
- The input dimension $d_0$ and batch size $B$ are fixed while $n\to\infty$.
- Every hidden layer has width $n$.

## 2.2 Forward pass

There are three hidden layers and one scalar output. Biases are omitted.

$$
z_i^1(a)
=
\frac1{\sqrt{d_0}}
\sum_{j=1}^{d_0}W^1_{ij}x_{aj},
\qquad
h_i^1(a)=\phi(z_i^1(a)),
$$

$$
z_p^2(a)
=
\frac1{\sqrt n}
\sum_iW^2_{pi}h_i^1(a),
\qquad
h_p^2(a)=\phi(z_p^2(a)),
$$

$$
z_r^3(a)
=
\frac1{\sqrt n}
\sum_pW^3_{rp}h_p^2(a),
\qquad
h_r^3(a)=\phi(z_r^3(a)),
$$

and

$$
f_a
=
\frac1n\sum_rv_rh_r^3(a).
$$

The raw parameters are independent standard Gaussians:

$$
W^1_{ij},W^2_{pi},W^3_{rp},v_r
\overset{\mathrm{iid}}\sim N(0,1).
$$

## 2.3 Effective parameter variances and learning rates

The effective tensors appearing without explicit normalization would be

$$
\frac{W^1}{\sqrt{d_0}},
\qquad
\frac{W^2}{\sqrt n},
\qquad
\frac{W^3}{\sqrt n},
\qquad
\frac vn.
$$

Their initialization variances and equivalent gradient learning rates are

| Effective tensor | Entry variance | Learning rate multiplying its gradient |
|---|---:|---:|
| $W^1/\sqrt{d_0}$ | $1/d_0$ | $n\eta/d_0$ |
| $W^2/\sqrt n$ | $1/n$ | $\eta$ |
| $W^3/\sqrt n$ | $1/n$ | $\eta$ |
| $v/n$ | $1/n^2$ | $\eta/n$ |

Equivalently, in the raw coordinates used throughout this case study, every block is updated by

$$
\theta^+
=
\theta-n\eta\nabla_\theta\mathcal J,
\qquad
\theta\in\{W^1,W^2,W^3,v\}.
$$

The fixed $d_0$ factors are a convention. The displayed width powers are the μP/maximal-update powers.

## 2.4 Loss and residuals

Use the average squared batch loss

$$
\mathcal J
=
\frac1B\sum_{c=1}^B(f_c-y_c)^2.
$$

Write

$$
e_c=f_c-y_c.
$$

No factor $1/2$ is placed in the squared loss, so every gradient contains the factor $2/B$.

## 2.5 Forward activation Grams

Define

$$
G^0_{ab}
=
\frac{x_a^\top x_b}{d_0},
$$

and, at finite width,

$$
G^\ell_{n,ab}
=
\frac1n\sum_i h_i^\ell(a)h_i^\ell(b),
\qquad \ell=1,2,3.
$$

The deterministic forward recursion is as follows. Let

$$
Z^1\sim N(0,G^0),
$$

and define

$$
G^1_{ab}
=
\mathbb E[\phi(Z^1_a)\phi(Z^1_b)].
$$

Next let

$$
Z^2\sim N(0,G^1),
$$

and define

$$
G^2_{ab}
=
\mathbb E[\phi(Z^2_a)\phi(Z^2_b)].
$$

Finally let

$$
Z^3\sim N(0,G^2),
$$

and define

$$
G^3_{ab}
=
\mathbb E[\phi(Z^3_a)\phi(Z^3_b)].
$$

For each layer define the derivative kernel

$$
D^\ell_{ab}
=
\mathbb E[\phi'(Z^\ell_a)\phi'(Z^\ell_b)].
$$

Every expectation in these definitions is over one $B$-dimensional centered Gaussian vector with the displayed covariance.

## 2.6 Normalized backward variables

Define

$$
\delta_i^\ell(a)
:=
n\frac{\partial f_a}{\partial z_i^\ell(a)}.
$$

The chain rule gives

$$
\delta_r^3(a)
=
v_r\phi'(z_r^3(a)),
$$

$$
\delta_p^2(a)
=
\phi'(z_p^2(a))
\frac1{\sqrt n}\sum_rW^3_{rp}\delta_r^3(a),
$$

and

$$
\delta_i^1(a)
=
\phi'(z_i^1(a))
\frac1{\sqrt n}\sum_pW^2_{pi}\delta_p^2(a).
$$

The normalization makes every $\delta_i^\ell(a)$ an $O(1)$ random variable at fixed depth.

## 2.7 Assumptions and order of limits

The calculations below assume:

1. fixed $B,d_0$, and depth;
2. $n\to\infty$ through equal hidden widths;
3. enough smoothness of $\phi$ for every displayed Taylor and Stein derivative;
4. polynomial or otherwise controlled growth of the required activation derivatives;
5. uniform moment bounds for every retained contraction state;
6. leave-finitely-many-out control when a singled-out neuron also enters an empirical covariance;
7. uniform integrability when convergence in probability is converted into convergence of expectations;
8. joint conditional multivariate CLTs, including convergence of every mixed covariance state, for the finite collection of forward, backward, tangent, and fresh Gaussian base fields retained by each peel.

The Taylor coefficient is first defined at finite $n$. The width limit is then taken. Every later display using shorthand such as $o(\eta^2)+o_n(1)$ is to be read in this ordered, coefficientwise sense; no uniform two-parameter remainder estimate is claimed. Claims about a whole finite-$\eta$ trajectory require additional uniform remainder estimates and are not implied merely by the coefficient calculations.

For ReLU, ordinary pointwise $C^2$ Taylor formulas are unavailable. A weak-derivative or Gaussian-boundary calculation is required.

---

# 3. The two exact Gaussian identities used in every peel

Let $w=(w_1,\ldots,w_n)$ have independent $N(0,1)$ coordinates and let

$$
Z(a)
=
\frac1{\sqrt n}\sum_jw_jh_j(a).
$$

Conditional on the lower-layer numbers $h_j(a)$, the vector $(w,Z)$ is jointly Gaussian.

For a smooth function $F$ of the fixed-batch vector $Z$, one-weight Stein gives

$$
\boxed{
\mathbb E[w_pF(Z)]
=
\frac1{\sqrt n}\sum_a
h_p(a)\mathbb E[\partial_aF(Z)].
}
\tag{3.1}
$$

Applying Gaussian integration by parts twice gives

$$
\boxed{
\mathbb E[w_pw_qF(Z)]
=
\delta_{pq}\mathbb E[F(Z)]
+
\frac1n\sum_{a,b}
h_p(a)h_q(b)
\mathbb E[\partial_a\partial_bF(Z)].
}
\tag{3.2}
$$

The first term of (3.2) is the weight--weight Wick branch. The second is the Stein/Onsager branch. No independence between $w$ and $Z$ has been asserted.

For a top-row sum, equality patterns must be separated. For example, $p=q$ and $p\ne q$ have different numbers of free indices and different Gaussian contractions. A branch is discarded only after its complete index multiplicity and every lower-layer sum created by Stein differentiation have been counted.

---

# 4. Execution I: backward sensitivity kernels

Define

$$
\Pi^\ell_{n,ab}
=
\frac1n\sum_i
\delta_i^\ell(a)\delta_i^\ell(b).
$$

We peel from the readout downward.

## 4.1 Readout and group 3

At the third hidden layer,

$$
\Pi^3_{n,ab}
=
\frac1n\sum_r
v_r^2
\phi'(z_r^3(a))\phi'(z_r^3(b)).
$$

The readout weights are independent of all hidden preactivations, so

$$
\mathbb E[v_r^2]=1.
$$

Conditional on the second hidden layer, the rows $z_r^3$ are iid Gaussian with covariance $G^2_n$. A weighted law of large numbers followed by $G^2_n\to G^2$ gives

$$
\boxed{
\Pi^3_{n,ab}\longrightarrow D^3_{ab}.
}
$$

## 4.2 Full scalarization of the group-3 peel for $\Pi^2$

Substitute the recursion for $\delta^2$:

$$
\begin{aligned}
\Pi^2_{n,ab}
=
\frac1{n^2}
\sum_{p,r,t}
&\phi'(z_p^2(a))\phi'(z_p^2(b))
W^3_{rp}W^3_{tp}
\\
&\times
v_rv_t
\phi'(z_r^3(a))\phi'(z_t^3(b)).
\end{aligned}
\tag{4.1}
$$

The readout is the highest group. Peel it first:

$$
\mathbb E_v[v_rv_t]=\delta_{rt}.
$$

Thus

$$
\begin{aligned}
\mathbb E_v[\Pi^2_{n,ab}]
=
\frac1{n^2}
\sum_{p,r}
&\phi'(z_p^2(a))\phi'(z_p^2(b))
(W^3_{rp})^2
\\
&\times
\phi'(z_r^3(a))\phi'(z_r^3(b)).
\end{aligned}
\tag{4.2}
$$

The factor $(W^3_{rp})^2$ is not independent of $z_r^3$. Apply (3.2) with $p=q$ and

$$
F(Z)=\phi'(Z_a)\phi'(Z_b).
$$

Because

$$
\frac{\partial z_r^3(c)}{\partial W^3_{rp}}
=
\frac{h_p^2(c)}{\sqrt n},
$$

the exact second derivative is

$$
\begin{aligned}
&\frac{\partial^2}{\partial(W^3_{rp})^2}
\left[
\phi'(z_r^3(a))\phi'(z_r^3(b))
\right]
\\
&=\frac1n\Big[
h_p^2(a)^2\phi'''(z_r^3(a))\phi'(z_r^3(b))
\\
&\qquad
+2h_p^2(a)h_p^2(b)
\phi''(z_r^3(a))\phi''(z_r^3(b))
\\
&\qquad
+h_p^2(b)^2
\phi'(z_r^3(a))\phi'''(z_r^3(b))
\Big].
\end{aligned}
\tag{4.3}
$$

Let

$$
\mathcal C^3_{n,ab}(c,d)
=
\mathbb E_{Z\sim N(0,G^2_n)}
\left[
\partial_c\partial_d
\{\phi'(Z_a)\phi'(Z_b)\}
\right].
$$

After applying (3.2) and summing the group-3-only index $r$, the exact conditional expression is

$$
\begin{aligned}
&\mathbb E_{v,W^3}
[\Pi^2_{n,ab}\mid W^1,W^2]
\\
&=
\frac1n\sum_p
\phi'(z_p^2(a))\phi'(z_p^2(b))
\Bigg[
D^3_{n,ab}
+
\frac1n\sum_{c,d}
h_p^2(c)h_p^2(d)\mathcal C^3_{n,ab}(c,d)
\Bigg],
\end{aligned}
\tag{4.3a}
$$

where

$$
D^3_{n,ab}
=
\mathbb E_{Z\sim N(0,G^2_n)}
[\phi'(Z_a)\phi'(Z_b)].
$$

Only now is the empirical covariance replaced by its deterministic limit. The first branch of (4.3a) converges to $D^2_{ab}D^3_{ab}$. The second branch has the form $n^{-2}\sum_p$ of bounded-moment row terms and is $O(n^{-1})$. Therefore

$$
\boxed{
\mathbb E[\Pi^2_{n,ab}]
\longrightarrow D^2_{ab}D^3_{ab}.
}
$$

## 4.3 Full path scalarization for $\Pi^1$

Expanding both backward paths gives

$$
\begin{aligned}
\Pi^1_{n,ab}
=
\frac1{n^3}
\sum_{i,p,q,r,t}
&v_rv_t
W^3_{rp}W^3_{tq}
W^2_{pi}W^2_{qi}
\\
&\times
\phi'(z_i^1(a))\phi'(z_i^1(b))
\\
&\times
\phi'(z_p^2(a))\phi'(z_q^2(b))
\\
&\times
\phi'(z_r^3(a))\phi'(z_t^3(b)).
\end{aligned}
\tag{4.4}
$$

The index ownership is essential:

- after the readout peel, $r$ is group-3-only;
- $p,q$ occur in groups 3 and 2 and cannot be summed out during the group-3 peel;
- $i$ occurs in groups 2 and 1 and cannot be summed out during the group-2 peel.

### 4.3.1 Peel the readout

Using

$$
\mathbb E[v_rv_t]=\delta_{rt},
$$

we obtain

$$
\begin{aligned}
\mathbb E_v[\Pi^1_{n,ab}]
=
\frac1{n^3}
\sum_{i,p,q,r}
&W^3_{rp}W^3_{rq}
W^2_{pi}W^2_{qi}
\\
&\times
\phi'(z_i^1(a))\phi'(z_i^1(b))
\\
&\times
\phi'(z_p^2(a))\phi'(z_q^2(b))
\\
&\times
\phi'(z_r^3(a))\phi'(z_r^3(b)).
\end{aligned}
\tag{4.5}
$$

### 4.3.2 Peel group 3

Condition on groups 1 and 2. Applying (3.2) to row $r$ gives

$$
\begin{aligned}
&\mathbb E_{W^3}
\left[
W^3_{rp}W^3_{rq}
\phi'(z_r^3(a))\phi'(z_r^3(b))
\right]
\\
&=
\delta_{pq}D^3_{n,ab}
+
\frac1n\sum_{c,d}
h_p^2(c)h_q^2(d)
\mathcal C^3_{n,ab}(c,d),
\end{aligned}
\tag{4.6}
$$

where

$$
D^3_{n,ab}
=
\mathbb E_{Z\sim N(0,G^2_n)}
[\phi'(Z_a)\phi'(Z_b)],
$$

and

$$
\mathcal C^3_{n,ab}(c,d)
=
\mathbb E_{Z\sim N(0,G^2_n)}
[\partial_c\partial_d\{\phi'(Z_a)\phi'(Z_b)\}].
$$

The Stein-created factors $h_p^2(c)h_q^2(d)$ belong to group 2. They remain inside the lower boundary state.

The first branch of (4.6) enforces $p=q$. The second leaves both patterns $p=q$ and $p\ne q$ to be counted at group 2.

Before applying a group-2 Stein identity, remove the dependence of the coefficients in (4.6) on the distinguished group-2 rows. Using a leave-two-out version of $G^2_n$ and then its deterministic limit gives

$$
D^3_{n,ab}=D^3_{ab}+o_{L^1}(1),
$$

$$
\mathcal C^3_{n,ab}(c,d)
=
\mathcal C^3_{ab}(c,d)+o_{L^1}(1),
\tag{4.6a}
$$

where

$$
\mathcal C^3_{ab}(c,d)
=
\mathbb E_{Z\sim N(0,G^2)}
[\partial_c\partial_d\{\phi'(Z_a)\phi'(Z_b)\}].
$$

The $o(1)$ error is carried through the remaining normalized sums by uniform integrability. Equivalently, one could retain derivatives of $D^3_n$ and $\mathcal C^3_n$ with respect to the distinguished rows; the leave-two-out replacement is the cleaner leading-order implementation used here.

### 4.3.3 Peel group 2: Wick branch

The group-3 Wick branch becomes

$$
\frac{D^3_{ab}}{n^2}
\sum_{i,p}
(W^2_{pi})^2
\phi'(z_i^1(a))\phi'(z_i^1(b))
\phi'(z_p^2(a))\phi'(z_p^2(b)).
\tag{4.7}
$$

Applying (3.2) to $(W^2_{pi})^2$ gives a leading Wick term

$$
\frac{D^3_{ab}D^2_{n,ab}}n
\sum_i
\phi'(z_i^1(a))\phi'(z_i^1(b)),
\tag{4.8}
$$

up to the already recorded $o(1)$ covariance-replacement error.

More explicitly, if

$$
\mathcal C^2_{n,ab}(c,d)
=
\mathbb E_{Z\sim N(0,G^1_n)}
[\partial_c\partial_d\{\phi'(Z_a)\phi'(Z_b)\}],
$$

then

$$
\begin{aligned}
&\mathbb E_{W^2}
[(W^2_{pi})^2\phi'(z_p^2(a))\phi'(z_p^2(b))]
\\
&=
D^2_{n,ab}
+
\frac1n\sum_{c,d}
h_i^1(c)h_i^1(d)\mathcal C^2_{n,ab}(c,d).
\end{aligned}
\tag{4.8a}
$$

After the $p$- and $i$-sums, the second line contributes $O(n^{-1})$ and leaves only group-1 activations.

### 4.3.4 Peel group 2: branch created by group-3 Stein differentiation

After the group-3-only index $r$ has been summed, the full branch created by the second term of (4.6) is

$$
\begin{aligned}
\mathcal S_n
=
\frac1{n^3}\sum_{i,p,q}
W^2_{pi}W^2_{qi}
&\phi'(z_i^1(a))\phi'(z_i^1(b))
\\
\times
\sum_{c,d}\mathcal C^3_{ab}(c,d)
&\phi'(z_p^2(a))\phi(z_p^2(c))
\\
\times
&\phi'(z_q^2(b))\phi(z_q^2(d)).
\end{aligned}
\tag{4.9}
$$

For $p=q$, define

$$
P_{cd}(Z)
=
\phi'(Z_a)\phi'(Z_b)\phi(Z_c)\phi(Z_d).
$$

Conditional on group 1, let $Z\sim N(0,G^1_n)$. The exact group-2 row peel of the row-dependent factor is

$$
\begin{aligned}
&\mathbb E[
(W^2_{pi})^2P_{cd}(z_p^2)
]
\\
&=
\mathbb E[P_{cd}(Z)]
+
\frac1n\sum_{u,w}
h_i^1(u)h_i^1(w)
\mathbb E[\partial_u\partial_wP_{cd}(Z)].
\end{aligned}
\tag{4.10}
$$

The diagonal family contains only $n^2$ choices for $(i,p)$. With the $n^{-3}$ normalization in (4.9), its Wick and Stein terms are respectively $O(n^{-1})$ and $O(n^{-2})$.

For $p\ne q$, the two group-2 rows are conditionally independent. Each single weight must be removed using the one-weight identity (3.1). The two Stein covariances contribute $n^{-1}$ together. There are $n^3(1+o(1))$ choices for $(i,p,q)$, but the original normalization is $n^{-3}$, so this branch is again $O(n^{-1})$.

In full notation, put

$$
F_{a,c}(Z)=\phi'(Z_a)\phi(Z_c),
\qquad
F_{b,d}(Z)=\phi'(Z_b)\phi(Z_d).
$$

For $p\ne q$,

$$
\mathbb E[W^2_{pi}F_{a,c}(z_p^2)]
=
\frac1{\sqrt n}\sum_u
h_i^1(u)\mathbb E[\partial_uF_{a,c}(Z)],
$$

$$
\mathbb E[W^2_{qi}F_{b,d}(z_q^2)]
=
\frac1{\sqrt n}\sum_w
h_i^1(w)\mathbb E[\partial_wF_{b,d}(Z)].
\tag{4.11}
$$

Their product supplies the stated $n^{-1}$ Stein cost. Thus the five branch orders—leading ladder, group-2 Stein correction, group-3-Stein diagonal Wick, group-3-Stein diagonal Stein, and group-3-Stein off-diagonal—are

$$
1,\qquad n^{-1},\qquad n^{-1},\qquad n^{-2},\qquad n^{-1}.
\tag{4.12}
$$

Thus every branch created by the group-3 Stein term vanishes at leading order, but only after the $p=q$ and $p\ne q$ families have been separated and counted.

Before the final group-1 law of large numbers, use a leave-one-out covariance to replace

$$
D^2_{n,ab}=D^2_{ab}+o_{L^1}(1),
\qquad
\mathcal C^2_{n,ab}(c,d)
=
\mathcal C^2_{ab}(c,d)+o_{L^1}(1).
\tag{4.12a}
$$

This prevents the distinguished group-1 row from being hidden inside a coefficient that is incorrectly treated as constant.

### 4.3.5 Peel group 1

After group 2 is removed, the leading remaining expression is (4.8). The index $i$ now belongs only to group 1, so the law of large numbers gives

$$
\frac1n\sum_i
\phi'(z_i^1(a))\phi'(z_i^1(b))
\longrightarrow D^1_{ab}.
$$

Therefore

$$
\boxed{
\mathbb E[\Pi^1_{n,ab}]
\longrightarrow
D^1_{ab}D^2_{ab}D^3_{ab}.
}
$$

## 4.4 Result and concentration obligation

The limiting backward recursion is

$$
\boxed{
\Pi^3=D^3,
\qquad
\Pi^2=D^2\odot\Pi^3,
\qquad
\Pi^1=D^1\odot\Pi^2.
}
$$

Here $\odot$ denotes entrywise multiplication.

The calculation above establishes the expectation limits. To obtain convergence of the random empirical kernel itself, one must peel the square. Four backward paths appear. The expected mechanism is that the disconnected pair of ladders reproduces the square of the expectation, while every connected equality pattern loses at least one free neuron index. A sufficient estimate is

$$
\operatorname{Var}(\Pi^\ell_{n,ab})=O(n^{-1}).
$$

The complete four-path Wick--Stein enumeration is not reproduced in this case study. Accordingly, the variance estimate is recorded as an additional concentration hypothesis/proof obligation under the fixed-depth moment assumptions. When it holds,

$$
\Pi^\ell_{n,ab}\to\Pi^\ell_{ab}
$$

in $L^2$. Every later replacement of a product involving $\Pi^\ell_n$ invokes this concentration estimate together with uniform integrability; it does not follow from the one-copy expectation calculation alone.

## 4.5 Exact conditional integration versus mean-field replacement

At group 3 the Gaussian covariance used in (4.3a) and (4.6) is initially

$$
G^2_{n,cd}
=
\frac1n\sum_p h_p^2(c)h_p^2(d),
$$

not the deterministic matrix $G^2$. Likewise, the group-2 row peel initially uses

$$
G^1_{n,cd}
=
\frac1n\sum_i h_i^1(c)h_i^1(d).
$$

The correct order is:

1. condition on the lower groups and apply the exact Gaussian integration-by-parts identity with $G_n^{\ell-1}$;
2. retain every lower-group factor created by differentiation;
3. expose the equality patterns of the distinguished rows;
4. then replace $G_n^{\ell-1}$ by $G^{\ell-1}$.

When a distinguished row $p$ or pair $(p,q)$ also occurs inside $G^2_n$, a quantitative proof replaces $G^2_n$ temporarily by its leave-one-out or leave-two-out version. Removing finitely many rows changes the covariance by $O(n^{-1})$; the remaining covariance is independent of the distinguished rows and converges to $G^2$. Uniform integrability then permits passage to expectations.

This procedure proves the leading $o(1)$ limit. It does not, without a sharper fluctuation expansion, identify an exact finite-width $1/n$ bias.

---

# 5. Execution II: one gradient-descent step

The output and sample losses are computed through linear order in $\eta$. The hidden Grams are computed through quadratic order, because their deterministic linear coefficient vanishes. All Taylor coefficients are formed at finite width before taking $n\to\infty$.

## 5.1 Exact parameter and preactivation velocities

Put a dot over a quantity to mean its derivative with respect to the one-step learning-rate parameter at $\eta=0$. From

$$
\theta^+=\theta-n\eta\nabla_\theta\mathcal J
$$

and the definition of $\delta$, the exact raw-parameter velocities are

$$
\dot v_r
=
-\frac2B\sum_c e_c h_r^3(c),
\tag{5.1}
$$

$$
\dot W^3_{rp}
=
-\frac{2}{B\sqrt n}\sum_c
e_c\delta_r^3(c)h_p^2(c),
\tag{5.2}
$$

$$
\dot W^2_{pi}
=
-\frac{2}{B\sqrt n}\sum_c
e_c\delta_p^2(c)h_i^1(c),
\tag{5.3}
$$

and

$$
\dot W^1_{ij}
=
-\frac{2}{B\sqrt{d_0}}\sum_c
e_c\delta_i^1(c)x_{cj}.
\tag{5.4}
$$

Define the first preactivation velocities

$$
u_i^\ell(a)
:=
\left.\frac{d z_i^{\ell,+}(a)}{d\eta}\right|_{\eta=0}.
$$

Substitution of (5.2)--(5.4) into the forward equations gives, still exactly at finite width,

$$
u_i^1(a)
=
-\frac2B\sum_c e_cG^0_{ac}\delta_i^1(c),
\tag{5.5}
$$

$$
\begin{aligned}
u_p^2(a)
={}&
-\frac2B\sum_c e_cG^1_{n,ac}\delta_p^2(c)
\\
&+
\frac1{\sqrt n}\sum_i
W^2_{pi}\phi'(z_i^1(a))u_i^1(a),
\end{aligned}
\tag{5.6}
$$

and

$$
\begin{aligned}
u_r^3(a)
={}&
-\frac2B\sum_c e_cG^2_{n,ac}\delta_r^3(c)
\\
&+
\frac1{\sqrt n}\sum_p
W^3_{rp}\phi'(z_p^2(a))u_p^2(a).
\end{aligned}
\tag{5.7}
$$

These equations already exhibit the two branches that peeling must track: the direct change of the current matrix and the propagated change of the preceding representation.

## 5.2 Exact tangent kernel and the linear loss coefficient

Define the optimizer-metric tangent kernel

$$
K_{n,ab}
=
n\sum_{k=1}^3
\left\langle
\nabla_{W^k}f_a,\nabla_{W^k}f_b
\right\rangle
+n\left\langle\nabla_vf_a,\nabla_vf_b\right\rangle.
\tag{5.8}
$$

The finite-width output velocity is therefore

$$
\dot f_a
=
-\frac2B\sum_cK_{n,ac}e_c.
\tag{5.9}
$$

Every parameter gradient is rank one. For example,

$$
\frac{\partial f_a}{\partial W^3_{rp}}
=
\frac{\delta_r^3(a)h_p^2(a)}{n\sqrt n},
$$

so

$$
\begin{aligned}
n\sum_{r,p}
\frac{\partial f_a}{\partial W^3_{rp}}
\frac{\partial f_b}{\partial W^3_{rp}}
&=
\left(\frac1n\sum_r\delta_r^3(a)\delta_r^3(b)\right)
\left(\frac1n\sum_ph_p^2(a)h_p^2(b)\right)
\\
&=
\Pi^3_{n,ab}G^2_{n,ab}.
\end{aligned}
$$

Doing the same for every block gives the exact factorization

$$
\boxed{
K_{n,ab}
=
G^3_{n,ab}
+G^2_{n,ab}\Pi^3_{n,ab}
+G^1_{n,ab}\Pi^2_{n,ab}
+G^0_{ab}\Pi^1_{n,ab}.
}
\tag{5.10}
$$

The backward expectation calculation in Section 4, together with the joint concentration obligation stated in Section 4.4, gives

$$
\boxed{
\begin{aligned}
K_{ab}
={}&G^3_{ab}
+G^2_{ab}D^3_{ab}
+G^1_{ab}D^2_{ab}D^3_{ab}
\\
&+G^0_{ab}D^1_{ab}D^2_{ab}D^3_{ab}.
\end{aligned}
}
\tag{5.11}
$$

Because $f_a\to0$, the residual satisfies $e_a\to-y_a$. Weighted convergence, rather than a finite-width independence claim, yields

$$
\boxed{
\lim_{n\to\infty}\mathbb E[\dot f_a]
=
\frac2B\sum_cK_{ac}y_c.
}
\tag{5.12}
$$

For the individual loss $\ell_a=e_a^2$,

$$
\dot\ell_a
=
2e_a\dot f_a
=
-\frac4B e_a\sum_cK_{n,ac}e_c.
$$

Consequently,

$$
\boxed{
\mathbb E[\ell_a^+]
=
y_a^2
-\frac{4\eta}{B}y_a\sum_cK_{ac}y_c
+o(\eta)+o_n(1).
}
\tag{5.13}
$$

For the average loss this becomes

$$
\boxed{
\mathbb E[\mathcal J^+]
=
\frac1B\sum_a y_a^2
-\frac{4\eta}{B^2}y^\top Ky
+o(\eta)+o_n(1).
}
\tag{5.14}
$$

The batch-average coefficient is nonpositive because $K$ is positive semidefinite. A particular sample loss need not decrease.

## 5.3 Exact hidden-Gram linear coefficient

Define the activation velocity

$$
g_i^\ell(a)
:=
\left.\frac{d h_i^{\ell,+}(a)}{d\eta}\right|_0
=
\phi'(z_i^\ell(a))u_i^\ell(a).
\tag{5.15}
$$

The coefficient of $\eta$ in the hidden Gram is exactly

$$
\boxed{
L^\ell_{n,ab}
:=
\left.\frac{dG^{\ell,+}_{n,ab}}{d\eta}\right|_0
=
\frac1n\sum_i
\left[
g_i^\ell(a)h_i^\ell(b)
+h_i^\ell(a)g_i^\ell(b)
\right].
}
\tag{5.16}
$$

Equivalently, before any width limit,

$$
L^\ell_{n,ab}
=
-\frac{2n}{B}\sum_c e_c
\sum_{k\leq\ell}
\left\langle
\nabla_{W^k}G^\ell_{n,ab},
\nabla_{W^k}f_c
\right\rangle.
\tag{5.17}
$$

The readout must be peeled before any hidden group. For a coordinate $z_j^k(c)$ with $k\leq3$,

$$
\delta_j^k(c)
=
\sum_r
v_r\phi'(z_r^3(c))
\frac{\partial z_r^3(c)}{\partial z_j^k(c)}
$$

is linear in $v$. Hence the label branch is odd and vanishes:

$$
\mathbb E_v[-y_c\delta_j^k(c)]=0.
\tag{5.18}
$$

The output branch contains two readout factors. Its contraction is

$$
\begin{aligned}
\mathbb E_v[f_c\delta_j^k(c)]
&=
\frac1n\sum_{r,t}
\mathbb E[v_tv_r]
h_t^3(c)\phi'(z_r^3(c))
\frac{\partial z_r^3(c)}{\partial z_j^k(c)}
\\
&=
\frac1n\sum_r
h_r^3(c)\phi'(z_r^3(c))
\frac{\partial z_r^3(c)}{\partial z_j^k(c)}
\\
&=
\frac12
\frac{\partial G^3_{n,cc}}{\partial z_j^k(c)}.
\end{aligned}
\tag{5.19}
$$

Substituting this exact top-group peel into (5.17) gives

$$
\boxed{
\mathbb E_v[L^\ell_{n,ab}\mid W^1,W^2,W^3]
=
-\frac1B\sum_c\sum_{k\leq\ell}
\left\langle
\nabla_{W^k}G^\ell_{n,ab},
\nabla_{W^k}G^3_{n,cc}
\right\rangle.
}
\tag{5.20}
$$

This formula makes the remaining width loss visible. For example, the direct $k=\ell=3$ term is

$$
\begin{aligned}
-\frac{2}{Bn}\sum_c
\Bigg[&
G^2_{n,ac}
\frac1n\sum_r
h_r^3(b)\phi'(z_r^3(a))
h_r^3(c)\phi'(z_r^3(c))
\\
&+
G^2_{n,bc}
\frac1n\sum_r
h_r^3(a)\phi'(z_r^3(b))
h_r^3(c)\phi'(z_r^3(c))
\Bigg].
\end{aligned}
\tag{5.21}
$$

The two inner averages have finite Gaussian limits, while the outer $1/n$ remains. For $k<\ell$, expanding the two derivatives in (5.20) creates two forward paths. Peeling from group 3 downward gives either a Wick pairing or a Stein attachment at each shared matrix. Those operations change the limiting Gaussian moment but do not restore the one free neuron index already lost in (5.20). Thus every such path family is also $O(n^{-1})$.

Therefore

$$
\mathbb E[L^\ell_{n,ab}]=O(n^{-1}),
$$

and

$$
\boxed{
\lim_{n\to\infty}
[\eta]\,\mathbb E[G^{\ell,+}_{n,ab}]
=0.
}
\tag{5.22}
$$

The cancellation is an annealed statement caused by the centered readout. It does not say that an individual finite-width network has zero first-order feature motion.

## 5.4 Exact quadratic hidden-Gram expansion

At finite width write

$$
z_i^{\ell,+}(a)
=
z_i^\ell(a)+\eta u_i^\ell(a)+\eta^2q_i^\ell(a)+o(\eta^2),
\tag{5.23}
$$

and

$$
h_i^{\ell,+}(a)
=
h_i^\ell(a)+\eta g_i^\ell(a)+\eta^2s_i^\ell(a)+o(\eta^2).
\tag{5.24}
$$

Taylor's formula gives

$$
g_i^\ell(a)=\phi'(z_i^\ell(a))u_i^\ell(a),
\tag{5.25}
$$

$$
s_i^\ell(a)
=
\phi'(z_i^\ell(a))q_i^\ell(a)
+\frac12\phi''(z_i^\ell(a))u_i^\ell(a)^2.
\tag{5.26}
$$

The first preactivation is linear in $W^1$, so

$$
q^1=0.
$$

For $\ell=2,3$, expanding the product of the updated matrix and the updated preceding activation gives

$$
\boxed{
q_i^\ell(a)
=
\frac1{\sqrt n}\sum_j
\left[
W^\ell_{ij}s_j^{\ell-1}(a)
+\dot W^\ell_{ij}g_j^{\ell-1}(a)
\right].
}
\tag{5.27}
$$

Therefore the exact coefficient of $\eta^2$ in the hidden Gram is

$$
\boxed{
C^\ell_{n,ab}
=
\frac1n\sum_i
\left[
g_i^\ell(a)g_i^\ell(b)
+s_i^\ell(a)h_i^\ell(b)
+h_i^\ell(a)s_i^\ell(b)
\right].
}
\tag{5.28}
$$

## 5.5 Peel the residual and readout factors in the quadratic coefficient

Every first velocity is linear in the residuals. Its leading quadratic products therefore contain

$$
e_ce_d
=
y_cy_d-y_cf_d-y_df_c+f_cf_d.
\tag{5.29}
$$

Each normalized backward signal $\delta$ is odd under $v\mapsto-v$. A quadratic velocity term has two such signals and is even. The two mixed terms in (5.29) add one further readout factor and are odd, so their conditional readout expectation is zero. The $f_cf_d$ branch is even but is $O(n^{-1})$ in every fixed moment because $f_c=O_{L^p}(n^{-1/2})$. Thus only the label--label term survives at leading order.

Set

$$
\lambda_c:=\frac{2y_c}{B}.
\tag{5.30}
$$

From this point through the end of the one-step quadratic calculation, all velocities mean their leading label-driven branch.

## 5.6 Separate the local activation gate from the incoming backward signal

At finite width define the incoming backward signals by

$$
\xi_r^3(a)=v_r,
$$

$$
\xi_p^2(a)
=
\frac1{\sqrt n}\sum_rW^3_{rp}\delta_r^3(a),
$$

$$
\xi_i^1(a)
=
\frac1{\sqrt n}\sum_pW^2_{pi}\delta_p^2(a).
\tag{5.31a}
$$

Then the exact identity is

$$
\delta_i^\ell(a)
=
\phi'(z_i^\ell(a))\xi_i^\ell(a).
$$

For a limiting representative neuron, write

$$
\delta^\ell(a)
=
\phi'(Z^\ell_a)\xi^\ell(a).
\tag{5.31}
$$

The multichannel extension of the Section 4 peel gives, under the joint-CLT and leave-one-out assumptions in Section 2.7, Gaussian base fields satisfying

$$
Z^\ell\ \perp\ \xi^\ell,
$$

with

$$
\mathbb E[\xi^\ell(a)\xi^\ell(b)]
=P^\ell_{ab},
$$

where

$$
P^3_{ab}=1,
\qquad
P^2_{ab}=D^3_{ab},
\qquad
P^1_{ab}=D^2_{ab}D^3_{ab}.
\tag{5.32}
$$

Accordingly,

$$
\Pi^\ell_{ab}=D^\ell_{ab}P^\ell_{ab}.
$$

The displayed independence is an additional leading joint-state conclusion, not a consequence of the backward second moment alone. It follows by conditioning on the forward network, peeling the mixed moments and conditional covariance of $\xi^\ell$, removing finitely many distinguished rows, and applying the conditional multivariate CLT. It is not a finite-width claim that a backward signal is independent of the weights and preactivations that define it.

Define three partial tangent factors, entrywise in the pair $(a,b)$:

$$
T^0=G^0,
$$

$$
T^1=G^1+D^1\odot T^0,
$$

$$
T^2=G^2+D^2\odot T^1.
\tag{5.33}
$$

Thus $T^{\ell-1}$ records the parameters at and below layer $\ell$ that can move $z^\ell$.

## 5.7 Execute the first-velocity peel

At layer 1, (5.5) immediately becomes

$$
u_i^1(a)
=
\sum_c\lambda_cT^0_{ac}\delta_i^1(c).
\tag{5.34}
$$

At layer 2, substitute (5.34) and the explicit transpose channel

$$
\xi_i^1(c)
=
\frac1{\sqrt n}\sum_{p'}W^2_{p'i}\delta_{p'}^2(c)
$$

into the propagated term of (5.6). This exposes all indices:

$$
\begin{aligned}
&\frac1{\sqrt n}\sum_i
W^2_{pi}\phi'(z_i^1(a))u_i^1(a)
\\
&\quad=
\frac1n\sum_{i,p'}W^2_{pi}W^2_{p'i}
\phi'(z_i^1(a))
\sum_c\lambda_cG^0_{ac}
\phi'(z_i^1(c))\delta_{p'}^2(c).
\end{aligned}
\tag{5.35}
$$

The equality patterns $p'=p$ and $p'\ne p$ must be treated separately.

For $p'=p$, the Wick branch of the two-weight identity forces the two paths to use the same target row. After the group-1 average is exposed, it gives

$$
\sum_c
\lambda_cG^0_{ac}D^1_{ac}\delta_p^2(c).
\tag{5.36}
$$

Adding the direct matrix-update term in (5.6),

$$
\sum_c\lambda_cG^1_{ac}\delta_p^2(c),
$$

produces

$$
\sum_c\lambda_cT^1_{ac}\delta_p^2(c).
\tag{5.37}
$$

For $p'\ne p$, an individual term has zero centered conditional mean, but the whole family cannot be discarded: it contains $n^2(1+o(1))$ pairs $(i,p')$. Scalarizing two copies of (5.35), pairing the row-distinct weights, and then applying the group-1 law of large numbers leaves a centered Gaussian field. Call it $\Gamma^2$. Its covariance is exactly the preceding activation-velocity covariance,

$$
\mathbb E[\Gamma^2(a)\Gamma^2(b)]
=
\mathbb E[g^1(a)g^1(b)].
\tag{5.38}
$$

The same diagonal-response/off-diagonal-fluctuation split at layer 3 yields the following equality in the limiting representative-neuron law:

$$
\boxed{
u^\ell(a)
=
\Gamma^\ell(a)
+\sum_c\lambda_cT^{\ell-1}_{ac}\delta^\ell(c),
\qquad \ell=1,2,3,
}
\tag{5.39}
$$

where $\Gamma^1=0$. For $\ell=2,3$, the fresh field is centered Gaussian and

$$
\mathbb E[\Gamma^\ell(a)\Gamma^\ell(b)]
=
V^{\ell-1}_{ab},
\tag{5.40}
$$

where

$$
V^\ell_{ab}:=\mathbb E[g^\ell(a)g^\ell(b)].
\tag{5.41}
$$

The remaining cross-covariance with the current preactivation is

$$
\mathbb E[\Gamma^\ell(a)Z^\ell_b]
=
\mathbb E[g^{\ell-1}(a)h^{\ell-1}(b)].
$$

The right-hand side is odd in the centered readout and is zero at this order. The recursion below additionally uses the corresponding mixed two-copy conclusion

$$
\lim_{n\to\infty}
\mathbb E\!\left[
\left(
\frac1{\sqrt n}\sum_jW^\ell_{ij}g_j^{\ell-1}(a)
-\text{its complete Stein response}
\right)
\xi_i^\ell(b)
\right]
=0.
\tag{5.40a}
$$

Its disconnected branch vanishes by readout parity; every connected branch must reconnect the two copies through a shared row or a Stein attachment and loses one width power. A complete joint-state theorem must include this mixed contraction explicitly. Under that joint-CLT obligation, zero cross-covariance of the Gaussian base fields makes $\Gamma^\ell$ independent of $(Z^\ell,\xi^\ell)$ at this one-step order.

## 5.8 Recursion for the velocity covariance

Insert (5.31) and (5.39) into

$$
g^\ell(a)=\phi'(Z^\ell_a)u^\ell(a).
$$

The fresh-field/response cross terms vanish. The fresh-field square gives $D^\ell_{ab}V^{\ell-1}_{ab}$. The response square gives one backward covariance $P^\ell_{cd}$ and a four-gate Gaussian moment. Therefore

$$
\boxed{
\begin{aligned}
V^\ell_{ab}
={}&
D^\ell_{ab}V^{\ell-1}_{ab}
\\
&+
\sum_{c,d}\lambda_c\lambda_d
T^{\ell-1}_{ac}T^{\ell-1}_{bd}P^\ell_{cd}
\\
&\qquad\times
\mathbb E\!\left[
\phi'(Z^\ell_a)\phi'(Z^\ell_b)
\phi'(Z^\ell_c)\phi'(Z^\ell_d)
\right],
\end{aligned}
}
\tag{5.42}
$$

with $V^0=0$ and $Z^\ell\sim N(0,G^{\ell-1})$.

The first line of (5.42) is the off-diagonal Wick/CLT branch just derived from $p'\ne p$. Replacing the empirical random operator in (5.35) by its mean before squaring would delete this term and give a wrong quadratic coefficient.

## 5.9 Execute the second-displacement peel

Define the cross moment

$$
S^\ell_{ab}
:=
\mathbb E[s^\ell(a)h^\ell(b)],
\qquad S^0=0.
\tag{5.43}
$$

There are two terms in (5.27). The mixed matrix/feature term is, on the label branch,

$$
\frac1{\sqrt n}\sum_j
\dot W^\ell_{ij}g_j^{\ell-1}(a)
=
\sum_c\lambda_c\delta_i^\ell(c)
X^{\ell-1}_{n,ca},
\tag{5.44}
$$

where

$$
X^{\ell-1}_{n,ca}
=
\frac1n\sum_j
h_j^{\ell-1}(c)g_j^{\ell-1}(a).
\tag{5.45}
$$

Its one-copy expectation is zero by readout parity, but that is not sufficient to discard it. Scalarizing two copies gives

$$
\mathbb E[(X^{\ell-1}_{n,ca})^2]
=
\frac1{n^2}\sum_{j,k}
\mathbb E[
h_j(c)g_j(a)h_k(c)g_k(a)
].
\tag{5.46}
$$

The $j=k$ family has $n$ assignments against the $n^2$ normalization and is $O(n^{-1})$. In the $j\ne k$ family, the disconnected readout contraction factorizes into two zero odd first moments. A connected contraction must either identify a current-layer row or attach one copy to the other by a Stein covariance carrying an extra $n^{-1}$. The lower-group boundary sums created by that attachment cannot restore the lost width: both copies must reconnect to the same current-layer backward field. Thus the connected family is also $O(n^{-1})$. Hence

$$
X^{\ell-1}_{n,ca}=O_{L^2}(n^{-1/2}),
$$

and (5.44) is negligible in the leading annealed coefficient after bounded-moment control.

It remains to peel

$$
\frac1{\sqrt n}\sum_jW^\ell_{ij}s_j^{\ell-1}(a).
\tag{5.47}
$$

The target-row Stein response coefficient is

$$
\mathbb E\!\left[
\frac{\partial s^{\ell-1}(a)}
{\partial\xi^{\ell-1}(c)}
\right].
$$

At this order $s^{\ell-1}$ is even under $v\mapsto-v$, whereas $\xi^{\ell-1}$ is odd. The differentiated random quantity is therefore odd, so its annealed response coefficient—not the random derivative itself—is zero. In the limiting representative-neuron law, the row-distinct Wick patterns leave a centered Gaussian base field $\Omega^\ell$ with the covariance needed below:

$$
\mathbb E[\Omega^\ell(a)Z^\ell_b]
=
S^{\ell-1}_{ab}.
\tag{5.48}
$$

Now use (5.26). Gaussian integration by parts in the jointly Gaussian pair $(\Omega^\ell,Z^\ell)$ gives

$$
\begin{aligned}
&\mathbb E[
\phi(Z^\ell_b)\phi'(Z^\ell_a)\Omega^\ell(a)
]
\\
&\quad=
D^\ell_{ab}S^{\ell-1}_{ab}
+
\mathbb E[
\phi(Z^\ell_b)\phi''(Z^\ell_a)
]S^{\ell-1}_{aa}.
\end{aligned}
\tag{5.49}
$$

The term $\tfrac12\phi''(Z_a^\ell)u^\ell(a)^2$ has a fresh-field square and a response square. Combining them with (5.49) yields

$$
\boxed{
\begin{aligned}
S^\ell_{ab}
={}&
D^\ell_{ab}S^{\ell-1}_{ab}
\\
&+
\mathbb E[
\phi(Z^\ell_b)\phi''(Z^\ell_a)
]
\left(S^{\ell-1}_{aa}+\frac12V^{\ell-1}_{aa}\right)
\\
&+
\frac12\sum_{c,d}\lambda_c\lambda_d
T^{\ell-1}_{ac}T^{\ell-1}_{ad}P^\ell_{cd}
\\
&\qquad\times
\mathbb E\!\left[
\phi(Z^\ell_b)\phi''(Z^\ell_a)
\phi'(Z^\ell_c)\phi'(Z^\ell_d)
\right].
\end{aligned}
}
\tag{5.50}
$$

Every expectation in (5.42) and (5.50) is over the single $B$-dimensional vector

$$
Z^\ell\sim N(0,G^{\ell-1}).
$$

Finally, (5.28) becomes

$$
\boxed{
C^\ell_{ab}
=
V^\ell_{ab}+S^\ell_{ab}+S^\ell_{ba}.
}
\tag{5.51}
$$

Thus the one-step hidden-Gram expansion is

$$
\boxed{
\mathbb E[G^{\ell,+}_{n,ab}]
=
G^\ell_{ab}
+\eta\,O(n^{-1})
+\eta^2C^\ell_{ab}
+o(\eta^2)+o_n(1).
}
\tag{5.52}
$$

## 5.10 Fully explicit first-layer coefficient

At layer 1, $V^0=S^0=0$, $T^0=G^0$, and $P^1_{cd}=D^2_{cd}D^3_{cd}$. Writing, only in the next display,

$$
\phi_a=\phi(Z^1_a),
\qquad
\phi'_a=\phi'(Z^1_a),
\qquad
\phi''_a=\phi''(Z^1_a),
$$

with $Z^1\sim N(0,G^0)$, gives

$$
\boxed{
\begin{aligned}
C^1_{ab}
=
\frac4{B^2}\sum_{c,d}y_cy_dP^1_{cd}
\Bigg[&
G^0_{ac}G^0_{bd}
\mathbb E[\phi'_a\phi'_b\phi'_c\phi'_d]
\\
&+
\frac12G^0_{ac}G^0_{ad}
\mathbb E[\phi_b\phi''_a\phi'_c\phi'_d]
\\
&+
\frac12G^0_{bc}G^0_{bd}
\mathbb E[\phi_a\phi''_b\phi'_c\phi'_d]
\Bigg].
\end{aligned}
}
\tag{5.53}
$$

This is already a completely explicit fixed-dimensional Gaussian integral. Layers 2 and 3 are obtained by evaluating (5.42), (5.50), and (5.51) in order.

## 5.11 Deep-linear audit of the one-step coefficient

Set $\phi(z)=z$. Then $D^\ell=P^\ell=1$, $S^\ell=0$, and every $G^\ell=G^0$. Define

$$
\kappa=\frac2B,
\qquad
\sigma_a=\sum_cG^0_{ac}y_c.
$$

The partial tangents are

$$
T^0=G^0,
\qquad
T^1=2G^0,
\qquad
T^2=3G^0.
$$

The velocity recursion gives

$$
\boxed{
C^1_{ab}=\kappa^2\sigma_a\sigma_b,
\qquad
C^2_{ab}=5\kappa^2\sigma_a\sigma_b,
\qquad
C^3_{ab}=14\kappa^2\sigma_a\sigma_b.
}
\tag{5.54}
$$

The nontrivial coefficient $5$ can be checked directly. Put

$$
M=\frac1nW^2W^{2\top}.
$$

The layer-2 velocity contains $I+M$, so

$$
\frac1n\operatorname{tr}(I+M)^2
\longrightarrow
1+2\cdot1+2=5,
$$

because

$$
\frac1n\operatorname{tr}M\to1,
\qquad
\frac1n\operatorname{tr}M^2\to2.
$$

Replacing $M$ by its entrywise mean $I$ before forming the square would give $4$, not $5$. This solvable case directly verifies that the row-distinct fluctuation branch in (5.42) is essential.

---

# 6. Execution III: two gradient-descent steps

The second Euler step differs from simply doubling the first displacement because the gradient is recomputed at the parameters reached after step one. This section isolates that correction exactly, peels its readout, and gives the layer-by-layer state recursion needed to peel the hidden groups.

## 6.1 Exact two-step Taylor identity

Let the raw-coordinate μP vector field be

$$
F(\theta):=-n\nabla\mathcal J(\theta).
\tag{6.1}
$$

Two Euler steps are

$$
\theta^{(1)}=\theta+\eta F(\theta),
$$

$$
\theta^{(2)}
=
\theta^{(1)}+\eta F(\theta^{(1)}).
$$

Taylor-expanding the second vector-field evaluation at finite width gives

$$
\boxed{
\theta^{(2)}
=
\theta+2\eta F
+\eta^2DF[F]
+O(\eta^3).
}
\tag{6.2}
$$

For the observable

$$
O(\theta)=G^\ell_{n,ab}(\theta),
$$

define

$$
L^\ell_{n,ab}=DO[F],
\qquad
C^\ell_{n,ab}=\frac12D^2O[F,F],
\qquad
R^\ell_{n,ab}=DO[DF[F]].
\tag{6.3}
$$

Then

$$
\boxed{
G^{\ell,(2)}_{n,ab}
=
G^\ell_{n,ab}
+2\eta L^\ell_{n,ab}
+\eta^2(4C^\ell_{n,ab}+R^\ell_{n,ab})
+O(\eta^3).
}
\tag{6.4}
$$

Subtracting the one-step expansion gives the change caused by the second update alone:

$$
\boxed{
G^{\ell,(2)}_{n,ab}-G^{\ell,(1)}_{n,ab}
=
\eta L^\ell_{n,ab}
+\eta^2(3C^\ell_{n,ab}+R^\ell_{n,ab})
+O(\eta^3).
}
\tag{6.5}
$$

The factors $4$ and $3$ are purely Taylor-combinatorial. The identity

$$
D_FL^\ell_{n,ab}=2C^\ell_{n,ab}+R^\ell_{n,ab}
\tag{6.6}
$$

is an independent check.

Section 5 proved $\mathbb E[L^\ell_{n,ab}]=O(n^{-1})$. Hence neither (6.4) nor (6.5) has a deterministic linear term after the sequential Taylor-then-width limit. Crucially, one may not set $L^\ell_n$ equal to its limiting value zero before differentiating it: (6.6) generally has a nonzero limit.

## 6.2 Isolate the new gradient correction

For squared loss,

$$
\nabla^2\mathcal J
=
\frac2B\sum_c
\left(
\nabla f_c\nabla f_c^\top
+e_c\nabla^2f_c
\right).
\tag{6.7}
$$

Since $DF[F]=n^2\nabla^2\mathcal J\,\nabla\mathcal J$, substitution into (6.3) yields the exact finite-width identity

$$
\boxed{
\begin{aligned}
R^\ell_{n,ab}
=
\frac4{B^2}\sum_{c,d}e_d
\Big[&
\left(n\nabla G^\ell_{n,ab}\right)^{\!\top}\nabla f_c\,K_{n,cd}
\\
&+
e_c n^2
\left(\nabla G^\ell_{n,ab}\right)^{\!\top}
\nabla^2f_c\nabla f_d
\Big].
\end{aligned}
}
\tag{6.8}
$$

The first line is the residual-change, or Gauss--Newton, branch. Its label part is odd in the centered readout and vanishes. Its surviving initialization-output branch is the same connected one-free-index-deficient family encountered in the linear Gram calculation, so it is $O(n^{-1})$.

In the second line, the label--label branch is even and survives, while mixed label/output branches are odd and the output--output branch is width-suppressed. Thus the leading correction is

$$
\boxed{
R^\ell_{ab}
=
\frac4{B^2}\sum_{c,d}y_cy_d
\lim_{n\to\infty}
\mathbb E\!\left[
n^2\left(\nabla G^\ell_{n,ab}\right)^{\!\top}
\nabla^2f_c\nabla f_d
\right].
}
\tag{6.9}
$$

## 6.3 Execute the top readout peel exactly

Let $\theta$ and $\psi$ denote individual raw parameter coordinates. Because a hidden Gram has no direct dependence on $v$, the contraction inside (6.9) is

$$
n^2\sum_{\theta\,\mathrm{hidden}}
\sum_\psi
\partial_\theta G^\ell_{n,ab}
\,\partial_{\theta\psi}f_c
\,\partial_\psi f_d.
\tag{6.10}
$$

There are two equality types for $\psi$.

If $\psi=v_s$, then

$$
\partial_{\theta v_s}f_c
=
\frac1n\partial_\theta h_s^3(c),
\qquad
\partial_{v_s}f_d
=
\frac1nh_s^3(d),
$$

and the prefactor $n^2$ cancels the two readout normalizations.

If $\psi$ is hidden, then

$$
\partial_{\theta\psi}f_c
=
\frac1n\sum_rv_r\partial_{\theta\psi}h_r^3(c),
$$

$$
\partial_\psi f_d
=
\frac1n\sum_tv_t\partial_\psi h_t^3(d).
$$

The exact readout Wick contraction $\mathbb E[v_rv_t]=\delta_{rt}$ again cancels the two factors $1/n$. Therefore

$$
\boxed{
\begin{aligned}
&\mathbb E_v\!\left[
n^2\left(\nabla G^\ell_{n,ab}\right)^{\!\top}
\nabla^2f_c\nabla f_d
\,\middle|\,W^1,W^2,W^3
\right]
\\
&=
\sum_{\theta\,\mathrm{hidden}}
\partial_\theta G^\ell_{n,ab}
\Bigg[
\sum_rh_r^3(d)\partial_\theta h_r^3(c)
\\
&\hspace{42mm}+
\sum_{\psi\,\mathrm{hidden}}\sum_r
\partial_{\theta\psi}h_r^3(c)
\partial_\psi h_r^3(d)
\Bigg].
\end{aligned}
}
\tag{6.11}
$$

Equation (6.11) is the completely explicit boundary state handed from the readout group to group 3. No independence between a hidden matrix and the preactivations it creates has been used.

## 6.4 Exact differentiated forward and backward states

The Hessian contraction can be evaluated without writing a third-order parameter tensor. Differentiate the ordinary forward/backward program in the direction $F$.

Keep

$$
u^\ell=D_Fz^\ell,
\qquad
g^\ell=D_Fh^\ell=\phi'(z^\ell)u^\ell,
$$

and define

$$
\dot\delta^\ell:=D_F\delta^\ell.
\tag{6.12}
$$

At the top hidden layer the exact readout velocity and exact directional boundary are

$$
\dot v_r
=
-\frac2B\sum_ce_ch_r^3(c),
$$

$$
\boxed{
\dot\delta_r^3(a)
=
\dot v_r\phi'(z_r^3(a))
+v_r\phi''(z_r^3(a))u_r^3(a).
}
\tag{6.13}
$$

Write a superscript $(y)$ for the leading label-driven component of a directional state. Then

$$
\dot v_r^{(y)}
=
\sum_c\lambda_ch_r^3(c),
$$

$$
\boxed{
\dot\delta_r^{3,(y)}(a)
=
\left(\sum_c\lambda_ch_r^3(c)\right)
\phi'(z_r^3(a))
+v_r\phi''(z_r^3(a))u_r^{3,(y)}(a).
}
\tag{6.13y}
$$

For $\ell=1,2$, recall $\delta^\ell=\phi'(z^\ell)\xi^\ell$. Hence

$$
\boxed{
\dot\delta^\ell(a)
=
\phi''(z^\ell(a))u^\ell(a)\xi^\ell(a)
+\phi'(z^\ell(a))\dot\xi^\ell(a).
}
\tag{6.14}
$$

Its label-driven component satisfies

$$
\boxed{
\dot\delta^{\ell,(y)}(a)
=
\phi''(z^\ell(a))u^{\ell,(y)}(a)\xi^\ell(a)
+\phi'(z^\ell(a))\dot\xi^{\ell,(y)}(a).
}
\tag{6.14y}
$$

The incoming signal is a transpose multiplication, so its exact finite-width directional derivative is

$$
\boxed{
\dot\xi_j^\ell(a)
=
\frac1{\sqrt n}\sum_i
\left[
\dot W^{\ell+1}_{ij}\delta_i^{\ell+1}(a)
+W^{\ell+1}_{ij}\dot\delta_i^{\ell+1}(a)
\right].
}
\tag{6.15}
$$

For the label-driven component,

$$
\dot W^{\ell+1,(y)}_{ij}
=
\frac1{\sqrt n}\sum_c
\lambda_c\delta_i^{\ell+1}(c)h_j^\ell(c).
$$

Peeling its contribution to the first term of (6.15) uses the already-computed backward Gram:

$$
\begin{aligned}
\frac1{\sqrt n}\sum_i
\dot W^{\ell+1,(y)}_{ij}\delta_i^{\ell+1}(a)
&=
\sum_c\lambda_ch_j^\ell(c)
\frac1n\sum_i
\delta_i^{\ell+1}(c)\delta_i^{\ell+1}(a)
\\
&\longrightarrow
\sum_c\lambda_ch_j^\ell(c)\Pi^{\ell+1}_{ca}.
\end{aligned}
\tag{6.16}
$$

The second term of (6.15) is a new backward transpose sum and must be peeled against every forward channel through the same matrix. Section 6.6 makes that operation explicit.

Now set

$$
A:=DF[F],
$$

and define the correction-forward states

$$
\bar z^\ell:=D_Az^\ell,
\qquad
\bar h^\ell:=D_Ah^\ell=\phi'(z^\ell)\bar z^\ell.
\tag{6.17}
$$

For concise denominators, let

$$
\rho_1=\sqrt{d_0},
\qquad
\rho_2=\rho_3=\sqrt n.
$$

The exact differentiated vector field for a hidden matrix is

$$
\boxed{
\begin{aligned}
A_{W^\ell}
=
-\frac{2}{B\rho_\ell}\sum_c
\Big[&
\dot f_c\,\delta^\ell(c)h^{\ell-1}(c)^\top
\\
&+e_c\dot\delta^\ell(c)h^{\ell-1}(c)^\top
\\
&+e_c\delta^\ell(c)g^{\ell-1}(c)^\top
\Big].
\end{aligned}
}
\tag{6.18}
$$

Here $h^0(c)=x_c$ and $g^0=0$. In the first line of (6.18), the label-driven part of $\dot f_c\,\delta^\ell$ is odd in the readout and vanishes. Its initialization-output-driven part is even but belongs to the width-suppressed residual-change family identified below (6.8). Replacing $e_c$ by $-y_c$ in the other two lines gives the leading even part

$$
\boxed{
A_{W^\ell}^{\mathrm{lead}}
=
\frac1{\rho_\ell}\sum_c\lambda_c
\left[
\dot\delta^{\ell,(y)}(c)h^{\ell-1}(c)^\top
+\delta^\ell(c)g^{\ell-1,(y)}(c)^\top
\right].
}
\tag{6.19}
$$

The exact correction-forward recursion is

$$
\bar z^1(a)
=
A_{W^1}\frac{x_a}{\sqrt{d_0}},
\tag{6.20}
$$

and, for $\ell=2,3$,

$$
\boxed{
\bar z^\ell(a)
=
\frac1{\sqrt n}W^\ell\bar h^{\ell-1}(a)
+\frac1{\sqrt n}A_{W^\ell}h^{\ell-1}(a).
}
\tag{6.21}
$$

Finally, the correction to the hidden Gram is

$$
\boxed{
R^\ell_{n,ab}
=
\frac1n\sum_i
\left[
\bar h_i^\ell(a)h_i^\ell(b)
+h_i^\ell(a)\bar h_i^\ell(b)
\right],
}
\tag{6.22a}
$$

When $\bar h^{\ell,\mathrm{lead}}$ is built from $A^{\mathrm{lead}}$, the formal leading mean-field replacement is

$$
\boxed{
R^\ell_{ab}
=
\mathbb E\!\left[
\bar h^{\ell,\mathrm{lead}}(a)h^\ell(b)
+h^\ell(a)\bar h^{\ell,\mathrm{lead}}(b)
\right].
}
\tag{6.22}
$$

Equations (6.13), (6.14), (6.15), (6.18), and (6.20)--(6.22a) are exact when they are built from the full directional states. Equations (6.13y), (6.16), (6.19), and the later mean-field recursions (6.29)--(6.35) describe only the leading label--label branch. Equation (6.22) additionally requires joint row convergence and uniform integrability. Together these identities turn the Hessian contraction into ordinary products of explicit forward, backward, and differentiated states.

## 6.5 The multichannel Wick--Stein rule required at step two

At one step, a matrix was coupled mainly to one forward and one backward channel. Differentiation creates several channels through the same matrix, so the single-channel shorthand (3.1) must be generalized without dropping any covariance.

Let $W$ be an iid standard Gaussian $n\times n$ matrix. Suppose the same matrix creates transpose channels

$$
b_j^\alpha
=
\frac1{\sqrt n}\sum_iW_{ij}y_i^\alpha,
\qquad \alpha=1,\ldots,q.
\tag{6.23}
$$

If the source vectors $y^\alpha$ and the remaining lower-group variables are frozen with respect to the current matrix $W$, and $\Psi_j$ is a smooth function of all $b_j^1,\ldots,b_j^q$, then the exact one-weight identity gives

$$
\mathbb E[W_{ij}\Psi_j]
=
\frac1{\sqrt n}\sum_{\alpha=1}^q
y_i^\alpha\,
\mathbb E[\partial_{b^\alpha}\Psi_j].
\tag{6.24}
$$

After summing $j$ and exposing equality patterns, the mean-field forward multiplication has the form

$$
\boxed{
\frac1{\sqrt n}\sum_jW_{ij}\Psi_j
\quad\Longrightarrow\quad
\Gamma_\Psi
+\sum_{\alpha=1}^q
y_i^\alpha\mathbb E[\partial_{b^\alpha}\Psi].
}
\tag{6.25}
$$

The row-distinct patterns form the centered Gaussian field $\Gamma_\Psi$. It is generated jointly with every other forward sum through $W$; for two integrands $\Psi$ and $\widetilde\Psi$,

$$
\mathbb E[\Gamma_\Psi(a)\Gamma_{\widetilde\Psi}(b)]
=
\mathbb E[\Psi(a)\widetilde\Psi(b)].
\tag{6.26}
$$

All cross-covariances with previously created fields using the same matrix must also be retained.

The transpose version is symmetric. If

$$
z_i^\alpha
=
\frac1{\sqrt n}\sum_jW_{ij}x_j^\alpha,
$$

and $\Upsilon_i$ depends on every $z_i^\alpha$, then

$$
\boxed{
\frac1{\sqrt n}\sum_iW_{ij}\Upsilon_i
\quad\Longrightarrow\quad
\Xi_\Upsilon
+\sum_{\alpha=1}^q
x_j^\alpha\mathbb E[\partial_{z^\alpha}\Upsilon],
}
\tag{6.27}
$$

with joint fresh-field covariance

$$
\mathbb E[\Xi_\Upsilon(a)\Xi_\Omega(b)]
=
\mathbb E[\Upsilon(a)\Omega(b)].
\tag{6.28}
$$

Equations (6.25) and (6.27) are not independence substitutions. Their response terms are precisely the accumulated Stein/Onsager corrections; their fresh Gaussian terms are the surviving off-diagonal Wick families.

Equations (6.24)--(6.27) apply directly only when their channel sources are frozen with respect to the current matrix. If a source such as $y^\alpha$ or $x^\alpha$ itself depends on $W$, that dependence must first be exposed as additional forward or transpose channels, and the full integration-by-parts derivative must include it.

For a rigorous use of these rules, the list of channels must therefore be complete. A derivative such as $\partial_{z^\alpha}\Upsilon$ is a total derivative through all deterministic response pieces already built from that channel. If a fresh field made earlier with the same matrix reappears, it must be registered as another jointly generated Gaussian base channel rather than declared independent.

## 6.6 Peel the differentiated backward pass

Apply (6.27) to the label-driven component of the second term of (6.15). The visible forward channels through $W^{\ell+1}$ are the ordinary preactivation $z^{\ell+1}$, sourced by $h^\ell$, and its first label tangent $u^{\ell+1,(y)}$, sourced by $g^{\ell,(y)}$. Thus the first two response terms are

$$
\sum_c h_j^\ell(c)
\mathbb E\!\left[
\frac{\partial\dot\delta^{\ell+1,(y)}(a)}
{\partial Z^{\ell+1}_c}
\right]
$$

and

$$
\sum_c g_j^{\ell,(y)}(c)
\mathbb E\!\left[
\frac{\partial\dot\delta^{\ell+1,(y)}(a)}
{\partial u^{\ell+1,(y)}(c)}
\right].
$$

Together with the direct term (6.16), the peeled form is

$$
\boxed{
\begin{aligned}
\dot\xi^{\ell,(y)}(a)
={}&
\sum_c\lambda_ch^\ell(c)\Pi^{\ell+1}_{ca}
+\Xi^{\ell,(y)}(a)
\\
&+
\sum_c h^\ell(c)
\mathbb E\!\left[
\partial_{Z^{\ell+1}_c}\dot\delta^{\ell+1,(y)}(a)
\right]
\\
&+
\sum_c g^{\ell,(y)}(c)
\mathbb E\!\left[
\partial_{u^{\ell+1,(y)}(c)}\dot\delta^{\ell+1,(y)}(a)
\right]
+\text{responses of any additional registered channel}.
\end{aligned}
}
\tag{6.29}
$$

The Gaussian base field $\Xi^{\ell,(y)}$ is centered. It is generated jointly with the ordinary incoming field $\xi^\ell$ and all other transpose sums through the same matrix. In particular,

$$
\mathbb E[\Xi^{\ell,(y)}(a)\Xi^{\ell,(y)}(b)]
=
\mathbb E[
\dot\delta^{\ell+1,(y)}(a)
\dot\delta^{\ell+1,(y)}(b)
],
$$

$$
\mathbb E[\Xi^{\ell,(y)}(a)\xi^\ell(b)]
=
\mathbb E[
\dot\delta^{\ell+1,(y)}(a)
\delta^{\ell+1}(b)
].
\tag{6.30}
$$

Equations (6.13y), (6.14y), and (6.29), evaluated in the order $3\to2\to1$, define the formal multichannel peel of the label-driven differentiated backward pass once a complete channel registry and covariance block are supplied. The placeholder in (6.29) makes this a schema, not a fully enumerated nonlinear closed recursion.

## 6.7 Peel the correction-forward pass

In the leading branch of (6.21), the term $W^\ell\bar h^{\ell-1,\mathrm{lead}}/\sqrt n$ is a forward multiplication. The current matrix also generates the transpose channels $\xi^{\ell-1}$ and $\dot\xi^{\ell-1,(y)}$, sourced respectively by $\delta^\ell$ and $\dot\delta^{\ell,(y)}$. Applying (6.25) gives

$$
\begin{aligned}
\frac1{\sqrt n}W^\ell\bar h^{\ell-1,\mathrm{lead}}(a)
\Longrightarrow{}&
\bar\Gamma^{\ell,\mathrm{lead}}(a)
\\
&+
\sum_c\delta^\ell(c)
\mathbb E[
\partial_{\xi^{\ell-1}(c)}\bar h^{\ell-1,\mathrm{lead}}(a)
]
\\
&+
\sum_c\dot\delta^{\ell,(y)}(c)
\mathbb E[
\partial_{\dot\xi^{\ell-1,(y)}(c)}
\bar h^{\ell-1,\mathrm{lead}}(a)
]
\\
&+
\text{responses of any additional registered channel}.
\end{aligned}
\tag{6.31}
$$

The fresh Gaussian base field $\bar\Gamma^{\ell,\mathrm{lead}}$ must be generated jointly with $Z^\ell,u^{\ell,(y)}$, and every other forward sum through $W^\ell$; its covariance and all cross-covariances follow from (6.26).

The direct $A_{W^\ell}h^{\ell-1}$ term in (6.21) gives

$$
\sum_c\lambda_c\dot\delta^{\ell,(y)}(c)G^{\ell-1}_{ac}
+
\sum_c\lambda_c\delta^\ell(c)
\frac1n\sum_jg_j^{\ell-1,(y)}(c)h_j^{\ell-1}(a).
\tag{6.32}
$$

The second empirical average is odd in the readout. Its disconnected limit is zero, and a connected two-copy peel is width-suppressed. Therefore the leading correction-forward recursion is

$$
\boxed{
\bar z^{\ell,\mathrm{lead}}(a)
=
\operatorname{ForwardPeel}_\ell[\bar h^{\ell-1,\mathrm{lead}}(a)]
+\sum_c\lambda_cG^{\ell-1}_{ac}\dot\delta^{\ell,(y)}(c),
}
\tag{6.33}
$$

where $\operatorname{ForwardPeel}$ means the right-hand side of (6.31) after a complete channel registry has been supplied, including every response and joint covariance. Since that registry is not fully enumerated here, (6.33) is a formal schema. For layer 1 there is no propagated term, so

$$
\boxed{
\bar z^{1,\mathrm{lead}}(a)
=
\sum_c\lambda_cG^0_{ac}\dot\delta^{1,(y)}(c).
}
\tag{6.34}
$$

With $\bar h^{\ell,\mathrm{lead}}=\phi'(z^\ell)\bar z^{\ell,\mathrm{lead}}$, substitution into (6.22) represents $R^\ell$ as fixed-dimensional Gaussian expectations. For example, once the differentiated-backward channel law has been supplied, the layer-1 endpoint is

$$
\boxed{
\begin{aligned}
R^1_{ab}
=
\sum_c\lambda_c\Big[&
G^0_{ac}
\mathbb E[
\phi(Z^1_b)\phi'(Z^1_a)\dot\delta^{1,(y)}(c)
]
\\
&+
G^0_{bc}
\mathbb E[
\phi(Z^1_a)\phi'(Z^1_b)\dot\delta^{1,(y)}(c)
]
\Big].
\end{aligned}
}
\tag{6.35}
$$

The nonlinear variables inside (6.35) are explicit functions of the Gaussian base channels produced by the preceding forward, backward, first-tangent, and differentiated-backward peels. At fixed derivative order the Gaussian base-channel count is finite, so each layer requires an expectation over a fixed multiple $qB$ of batch coordinates, independent of width. It need not be only one $B$-dimensional vector.

## 6.8 Execution schema for the general nonlinear correction

For clarity, the reusable two-step computation is the following finite-state program schema.

1. **Forward pass:** compute $G^0,G^1,G^2,G^3$ and retain representative Gaussian preactivations $Z^1,Z^2,Z^3$.

2. **Ordinary backward peel:** compute $\xi^3,\delta^3$, then $\xi^2,\delta^2$, then $\xi^1,\delta^1$, retaining their complete joint covariances. This gives $P^\ell$ and $\Pi^\ell$.

3. **First-tangent peel:** compute $u^{1,(y)},g^{1,(y)}$, then $u^{2,(y)},g^{2,(y)}$, then $u^{3,(y)},g^{3,(y)}$ using the diagonal Stein responses and fresh off-diagonal Gaussian base fields in (5.39).

4. **Differentiated-backward peel:** start with the label-leading top boundary (6.13y). Then use (6.14y), (6.16), and the multichannel schema (6.29) for groups $3\to2\to1$.

5. **Correction-forward peel:** compute $\bar z^{1,\mathrm{lead}},\bar h^{1,\mathrm{lead}}$ from (6.34), followed by layers 2 and 3 using (6.31)--(6.33). At each matrix, generate all fresh Gaussian base fields jointly with fields previously made from that matrix.

6. **Observable readout:** evaluate (6.22). Each entry is the expectation of an explicit function of the finite Gaussian base channels accumulated above.

The finite-width directional equations and the underlying multichannel one-weight integration-by-parts identity (6.24), under its frozen-source condition, are exact. The Gaussian-limit arrows (6.25) and (6.27) are formal mean-field conclusions under the assumptions in Section 2.7. The claim is that the Gaussian base channels converge jointly and every retained forward, backward, and differentiated state is an explicit nonlinear function of them—not that the entire state is jointly Gaussian. A theorem must additionally prove the leave-one-out estimates, uniform moment bounds, source-channel completeness, and joint convergence for the registered Gaussian base channels. The finite count $q$ may depend on derivative order and on the chosen depth/state construction, but not on width. This qualification matters more at two steps than at one because differentiated fresh fields can be correlated with several earlier channels through the same matrix.

## 6.9 Two-step result

Subject to completion and convergence of the nonlinear channel registry in Section 6.8, the formal mean-field closure is, coefficient by coefficient,

$$
\boxed{
\mathbb E[G^{\ell,(2)}_{n,ab}]
=
G^\ell_{ab}
+\eta\,O(n^{-1})
+\eta^2(4C^\ell_{ab}+R^\ell_{ab})
+o(\eta^2)+o_n(1).
}
\tag{6.36}
$$

For the second update alone,

$$
\boxed{
\mathbb E[G^{\ell,(2)}_{n,ab}-G^{\ell,(1)}_{n,ab}]
=
\eta\,O(n^{-1})
+\eta^2(3C^\ell_{ab}+R^\ell_{ab})
+o(\eta^2)+o_n(1).
}
\tag{6.37}
$$

The expectations of both linear coefficients are $O(n^{-1})$ before the width limit; the random coefficients themselves need not be. The term $C^\ell$ is the one-step quadratic coefficient from Section 5, and $R^\ell$ is due entirely to recomputing the gradient. Equations (6.36)--(6.37) are formal for a general nonlinear activation and verified explicitly in the deep-linear specialization below.

## 6.10 Deep-linear audit of the two-step correction

Again set $\phi(z)=z$, let

$$
\kappa=\frac2B,
\qquad
\sigma=G^0y,
$$

and write

$$
\tau(A)=\frac1n\operatorname{tr}A.
$$

The one-step coefficients are

$$
C^\ell_{ab}
=
(1,5,14)_\ell\,\kappa^2\sigma_a\sigma_b.
$$

For the correction term define

$$
M_2=\frac1nW^{2\top}W^2,
\qquad
M_3=\frac1nW^{3\top}W^3,
\qquad
M_{23}=\frac1nW^{2\top}M_3W^2.
\tag{6.38}
$$

Gaussian Wick contraction gives

$$
\tau(M_2)=\tau(M_3)=\tau(M_{23})=1,
$$

$$
\tau(M_2^2)=\tau(M_3^2)=2,
$$

$$
\tau(M_{23}M_2)=2,
\qquad
\tau(M_{23}^2)=3.
\tag{6.39}
$$

For example, expanding

$$
\tau(M_2^2)
=
\frac1{n^3}\sum_{a,b,i,j}
W^2_{ia}W^2_{ib}W^2_{jb}W^2_{ja}
$$

produces three Wick pairings. Two retain three free indices and contribute $1$ each; the crossing pairing retains only two and is $O(n^{-1})$. Hence $\tau(M_2^2)\to2$.

Because $M_{23}$ contains the independent Wishart matrix $M_3$ only once in $\tau(M_{23}M_2)$, conditioning on $W^2$ and using $\mathbb E[M_3]=I$ reduces it to $\tau(M_2^2)$, giving $2$.

For $\tau(M_{23}^2)$, put $\widetilde M_2=W^2W^{2\top}/n$. Cyclicity gives

$$
\tau(M_{23}^2)
=
\tau(M_3\widetilde M_2M_3\widetilde M_2).
$$

For fixed symmetric $\widetilde M_2$, the exact second moment of the Wishart entries is

$$
\mathbb E[(M_3)_{ij}(M_3)_{kl}]
=
\delta_{ij}\delta_{kl}
+\frac1n(\delta_{ik}\delta_{jl}+\delta_{il}\delta_{jk}).
$$

Substitution into the normalized trace yields, at leading order,

$$
\mathbb E_{M_3}[
\tau(M_3\widetilde M_2M_3\widetilde M_2)
]
=
\tau(\widetilde M_2^2)+\tau(\widetilde M_2)^2+o(1)
\longrightarrow2+1=3.
$$

To connect these traces to the differentiated-state program, define the label-aggregated forward vectors

$$
a^\ell:=\sum_c\lambda_ch^\ell(c),
$$

and the ordinary linear backward vectors

$$
b^3=v,
\qquad
b^2=\frac1{\sqrt n}W^{3\top}b^3,
\qquad
b^1=\frac1{\sqrt n}W^{2\top}b^2.
$$

Because

$$
a^2=\frac1{\sqrt n}W^2a^1,
\qquad
a^3=\frac1{\sqrt n}W^3a^2,
$$

differentiating the backward pass along the label-driven first update gives

$$
\dot b^3=a^3,
$$

$$
\dot b^2
=
\frac{\lVert b^3\rVert^2}{n}a^2
+\frac1{\sqrt n}W^{3\top}a^3
\ \Longrightarrow\ (I+M_3)a^2,
$$

and

$$
\dot b^1
=
\frac{\lVert b^2\rVert^2}{n}a^1
+\frac1{\sqrt n}W^{2\top}\dot b^2
\ \Longrightarrow\ (I+M_2+M_{23})a^1.
\tag{6.39a}
$$

The first term in each line comes from differentiating the corresponding weight matrix; the remaining terms propagate the differentiated backward vector. Inserting (6.39a) into the correction-forward recursion (6.19)--(6.21) gives the following one-sided Gram contractions.

The one-sided correction contractions at layers 1, 2, and 3 are respectively

$$
3=\tau(I+M_2+M_{23}),
$$

$$
7
=
\tau[M_2(I+M_2+M_{23})]+\tau(I+M_3)
=
(1+2+2)+(1+1),
$$

and

$$
\begin{aligned}
10
&=
\tau[M_{23}(I+M_2+M_{23})]
+\tau[M_3(I+M_3)]+1
\\
&=
(1+2+3)+(1+2)+1.
\end{aligned}
$$

The Gram has two endpoints, so symmetrization doubles these values:

$$
\boxed{
R^1_{ab}=6\kappa^2\sigma_a\sigma_b,
\qquad
R^2_{ab}=14\kappa^2\sigma_a\sigma_b,
\qquad
R^3_{ab}=20\kappa^2\sigma_a\sigma_b.
}
\tag{6.40}
$$

Therefore the cumulative two-step coefficients are

$$
\boxed{
(4C^\ell+R^\ell)_{ab}
=
(10,34,76)_\ell\,\kappa^2\sigma_a\sigma_b,
}
\tag{6.41}
$$

and the second-step increment coefficients are

$$
\boxed{
(3C^\ell+R^\ell)_{ab}
=
(9,29,62)_\ell\,\kappa^2\sigma_a\sigma_b.
}
\tag{6.42}
$$

This audit checks the factors $4$ and $3$, the gradient-correction sign, and the off-diagonal width patterns. It also distinguishes two Euler steps from gradient flow evaluated at time $2\eta$: the latter would have quadratic coefficient $4C^\ell+2R^\ell$.

---

# 7. What this case study changes in the peeling program

The three executions support the core peeling architecture, but they sharpen several statements that should be part of any theorem-level formulation.

1. **The raw/effective coordinate convention must be fixed before peeling.** In the raw convention used here,

   $$
   \operatorname{Cov}(W^3_{rp},z_r^3(c)\mid h^2)
   =\frac{h_p^2(c)}{\sqrt n}.
   $$

   Writing $h_p^2(c)/n$ would correspond to a different effective-weight convention and would corrupt width counting.

2. **Exact conditional Gaussian integration precedes deterministic Gram replacement.** A singled-out row may also occur in the empirical covariance of its layer. The safe proof uses leave-one-out or leave-two-out covariances, performs Wick--Stein first, and only then sends the empirical covariance to its deterministic limit.

3. **Stein-created lower-group factors remain boundary data.** For example, $h_p^2(c)h_q^2(d)$ created while peeling group 3 belongs to group 2. It cannot be averaged or summed out during the group-3 peel.

4. **An off-diagonal family cannot be removed from its one-copy mean.** In the backward kernel it is subleading after complete counting; in the quadratic feature coefficient it survives as the fresh field $\Gamma^\ell$. The observable and the number of copies determine the answer.

5. **Expectation and concentration are separate proof obligations.** One-copy peeling identifies an annealed limit. Replacing empirical kernels inside later products requires a two-copy or higher-copy concentration argument plus uniform integrability.

6. **A limiting zero cannot be differentiated as zero.** Although $L_n^\ell\to0$, its directional derivative contains the nonzero terms $2C^\ell+R^\ell$.

7. **Higher training steps require derivative-state augmentation.** At step two, the state must include $u,g,\dot\delta,\dot\xi,\bar z,\bar h$ in addition to the ordinary forward and backward variables. At higher Taylor order this becomes a finite jet of differentiated states.

8. **The Gaussian integration dimension is a fixed multiple of batch size.** A primitive forward kernel uses one $B$-dimensional Gaussian vector. A higher-order calculation uses a finite collection of jointly Gaussian base vectors, and the retained nonlinear states are explicit functions of them. Their total Gaussian dimension is $qB$. The number $q$ may depend on derivative order and on the chosen depth/state construction, but not on width.

9. **An $O(L)$ recursion still requires depth-uniform finite-state closure.** The intended algorithm traverses depth a constant number of times at fixed jet order, but the nonlinear registry is still schematic and its base-channel count may depend on depth. Linear complexity in $L$ is therefore a target conclusion, not yet an established result. It requires proving that the registered state size is bounded independently of depth at fixed derivative order.

10. **The nonlinear two-step closure still carries theorem obligations.** The exact finite-width directional identities are complete, but the displayed nonlinear mean-field channel registry is schematic. A rigorous theorem must enumerate the registry and prove joint convergence of its Gaussian base channels while tracking every cross-covariance; the deep-linear audit alone does not prove the general nonlinear closure.

# 8. Final consolidated statement

For this three-hidden-layer μP network, the mean-field peeling calculation gives the following coefficientwise results, subject to the concentration and joint-state obligations stated above:

$$
\Pi^\ell
=
D^\ell\odot D^{\ell+1}\odot\cdots\odot D^3,
$$

$$
\lim_{n\to\infty}
[\eta]\,\mathbb E[\ell_a^+]
=
-\frac4B y_a\sum_cK_{ac}y_c,
$$

$$
\lim_{n\to\infty}
[\eta]\,\mathbb E[G^{\ell,+}_{n,ab}]
=0,
$$

$$
\lim_{n\to\infty}
[\eta^2]\,\mathbb E[G^{\ell,+}_{n,ab}]
=
C^\ell_{ab},
$$

and

$$
\lim_{n\to\infty}
[\eta^2]\,\mathbb E[G^{\ell,(2)}_{n,ab}]
=
4C^\ell_{ab}+R^\ell_{ab}.
$$

The backward kernels and one-step coefficient $C^\ell$ close through explicit fixed-batch Gaussian expectations under the stated joint-CLT assumptions. The two-step correction $R^\ell$ is represented by the exact differentiated-state identities and formally reduced through the multichannel Gaussian-peeling schema in Section 6. Its general nonlinear registry and convergence remain proof obligations, while its full deep-linear specialization is explicitly verified in (6.40)--(6.42).

---

# Appendix A. General fixed-depth backward-kernel template

The main text uses the raw-coordinate specialization with three hidden layers,
unit hidden variances, and a centered $1/n$ readout. This appendix preserves
the more general normalization that motivated that execution. It is a
fixed-depth template supported by the explicit three-layer audit; a complete
all-depth diagram induction and concentration theorem remain proof
obligations.

Let hidden layers be $1,\ldots,H$, all of width $n$, and set $L:=H+1$ for
the scalar readout group. Use effective hidden weights

$$
A^\ell_{ij}
\sim
N\left(0,\frac{s_\ell^2}{n}\right),
$$

and the scalar readout

$$
f_a
=
s_Ln^{-\alpha}
\sum_{i=1}^na_i h_i^H(a),
\qquad
a_i\overset{\mathrm{iid}}\sim N(0,1).
\tag{A.1}
$$

The choices $\alpha=1/2$ and $\alpha=1$ give, respectively, a standard
random-output/NTK-size readout and the centered mean-field/μP-size readout used
in the main calculation.

Define

$$
g_i^{\ell,a}
:=
\frac{\partial f_a}{\partial z_i^\ell(a)},
\qquad
\beta_i^{\ell,a}:=n^\alpha g_i^{\ell,a}.
$$

Then

$$
\beta_i^{H,a}
=
s_La_i\phi'(z_i^{H,a}),
\tag{A.2}
$$

and, for $\ell<H$,

$$
\beta_i^{\ell,a}
=
\phi'(z_i^{\ell,a})
\sum_{r=1}^nA^{\ell+1}_{ri}\beta_r^{\ell+1,a}.
\tag{A.3}
$$

The normalized backward kernel is

$$
\widehat\Pi^\ell_{n,ab}
:=
\frac1n\sum_i\beta_i^{\ell,a}\beta_i^{\ell,b}
=
n^{2\alpha-1}
\sum_i g_i^{\ell,a}g_i^{\ell,b}.
\tag{A.4}
$$

Thus (A.4) is the ordinary backward inner product for $\alpha=1/2$;
for $\alpha=1$, the ordinary inner product is
$n^{-1}\widehat\Pi^\ell_{n,ab}$.

Let $Z^\ell\sim N(0,Q^\ell)$ and set

$$
D^\ell_{ab}
:=
\mathbb E[
\phi'(Z_a^\ell)\phi'(Z_b^\ell)].
\tag{A.5}
$$

For a hidden transition, the corresponding derivative-transport coefficient
is

$$
\dot Q^\ell_{ab}
:=
s_{\ell+1}^2D^\ell_{ab}.
\tag{A.5a}
$$

The readout contraction gives the boundary

$$
\widehat\Pi^H_{n,ab}
=
\frac{s_L^2}{n}\sum_i
a_i^2\phi'(z_i^{H,a})\phi'(z_i^{H,b})
\longrightarrow
s_L^2D^H_{ab}.
\tag{A.6}
$$

For a lower transition, put

$$
u_i^{\ell,ab}
=
\phi'(z_i^{\ell,a})\phi'(z_i^{\ell,b}).
$$

Recursive scalarization gives the exact expression

$$
\widehat\Pi^\ell_{n,ab}
=
\frac1n\sum_{i,r,s}
u_i^{\ell,ab}
A^{\ell+1}_{ri}A^{\ell+1}_{si}
\beta_r^{\ell+1,a}\beta_s^{\ell+1,b}.
\tag{A.7}
$$

If $v_{\ell+1}=s_{\ell+1}^2/n$, Gaussian integration by parts gives, for a
smooth $F$ of the current matrix,

$$
\mathbb E[A^{\ell+1}_{ri}A^{\ell+1}_{si}F]
=
v_{\ell+1}\delta_{rs}\mathbb E[F]
+v_{\ell+1}^2
\mathbb E[
\partial_{A^{\ell+1}_{ri}}
\partial_{A^{\ell+1}_{si}}F].
\tag{A.8}
$$

Because the effective coordinate satisfies

$$
\partial_{A^{\ell+1}_{ri}}
=
\sum_{c=1}^B
h_i^{\ell,c}\partial_{z_r^{\ell+1,c}},
$$

(A.8), applied to
$F=\beta_r^{\ell+1,a}\beta_s^{\ell+1,b}$, yields

$$
\mathbb E_{A^{\ell+1}}
[\widehat\Pi^\ell_{n,ab}]
=
s_{\ell+1}^2
\widehat D^\ell_{n,ab}
\mathbb E_{A^{\ell+1}}
[\widehat\Pi^{\ell+1}_{n,ab}]
+R^\ell_{n,ab},
\tag{A.9}
$$

where

$$
\widehat D^\ell_{n,ab}
=
\frac1n\sum_i u_i^{\ell,ab}
$$

and

$$
\begin{aligned}
R^\ell_{n,ab}
&=
\frac{s_{\ell+1}^4}{n^3}
\sum_{i,r,s}\sum_{c,d=1}^B
u_i^{\ell,ab}h_i^{\ell,c}h_i^{\ell,d}
\\
&\qquad\times
\mathbb E\left[
\partial_{z_r^{\ell+1,c}}
\partial_{z_s^{\ell+1,d}}
(\beta_r^{\ell+1,a}\beta_s^{\ell+1,b})
\right].
\end{aligned}
\tag{A.10}
$$

Equations (A.9)--(A.10) are exact after the stated conditional expectation.
They display the Wick branch and the complete Onsager remainder without an
independence substitution. In the top transition the explicit same-coordinate
identity is

$$
\begin{aligned}
&\mathbb E[(A^H_{ri})^2
\phi'(Z_r^H(a))\phi'(Z_r^H(b))
\mid\mathcal F_{H-1}]
\\
&\quad=
\frac{s_H^2}{n}
\mathbb E[\phi'(Z_a)\phi'(Z_b)]
\\
&\qquad+
\frac{s_H^4}{n^2}\sum_{c,d}
h_i^{H-1,c}h_i^{H-1,d}
\mathbb E[
\partial_{cd}\{\phi'(Z_a)\phi'(Z_b)\}],
\end{aligned}
\tag{A.11}
$$

where $Z\sim N(0,Q_n^H)$. The second line after the leading term contains
the $\phi'''\phi'$, $\phi''\phi''$, and $\phi'\phi'''$ integrands and is
$O(n^{-1})$ after the normalized row sum under the stated bounded-moment
assumptions.

Substitution of (A.11) gives the explicit top-transition decomposition

$$
\begin{aligned}
\mathbb E[
\widehat\Pi^{H-1}_{n,ab}\mid\mathcal F_{H-1}]
&=
s_H^2\widehat D^{H-1}_{n,ab}
\left[
s_L^2\mathbb E_{Z\sim N(0,Q_n^H)}
[\phi'(Z_a)\phi'(Z_b)]
\right]
\\
&\quad+
\frac{s_L^2s_H^4}{n^2}\sum_i
u_i^{H-1,ab}
\sum_{c,d}h_i^{H-1,c}h_i^{H-1,d}
\\
&\hspace{36mm}\times
\mathbb E[
\partial_{cd}\{\phi'(Z_a)\phi'(Z_b)\}].
\end{aligned}
\tag{A.11a}
$$

The second term is an explicit, nonzero Onsager correction before the width
limit. It is subleading for this normalized backward expectation under the
stated assumptions.

Unrolling (A.3) gives the two-path representation used for the general ladder
picture:

$$
\beta_{i_\ell}^{\ell,a}
=
s_L\sum_{i_{\ell+1},\ldots,i_H}
a_{i_H}
\left(
\prod_{t=\ell}^H\phi'(z_{i_t}^{t,a})
\right)
\left(
\prod_{t=\ell+1}^H
A^t_{i_ti_{t-1}}
\right).
\tag{A.11b}
$$

In the leading ladder, the readout contraction identifies the terminal path
indices and each hidden weight pairing identifies the two path indices at the
next level. Every shared hidden index supplies one factor $n$, while every
paired effective hidden weight supplies one factor $n^{-1}$; these powers
cancel layer by layer and leave the derivative moments (A.5). A Stein
attachment can release a Wick equality but carries an additional inverse
width and changes the lower boundary signature, so its final order must be
decided only after the paths reconnect or all lower sums are exposed.

For a centered readout, a nominally leading disconnected split also vanishes
because each isolated backward branch has zero first moment. This suppression
is specific to this normalized backward second-moment observable; it is not a
universal pseudo-independence statement for backward or higher-derivative
objects.

The formal arbitrary-fixed-depth ladder recursion is

$$
\Pi^H=s_L^2D^H,
\qquad
\Pi^\ell
=
s_{\ell+1}^2D^\ell\odot\Pi^{\ell+1},
\quad 1\le\ell<H,
\tag{A.12}
$$

or entrywise

$$
\Pi^\ell_{ab}
=
\left(\prod_{r=\ell+1}^{L}s_r^2\right)
\left(\prod_{t=\ell}^{H}D^t_{ab}\right).
\tag{A.13}
$$

The main text explicitly verifies the required suppression of all Stein
branches for $H=3$ at expectation level. Equations (A.12)--(A.13) are the
general ladder template; a complete induction over every arbitrary-depth
boundary pattern has not been supplied here.

Likewise, the expected concentration mechanism is a four-path expansion. The
disconnected pair of ladders reproduces

$$
(\mathbb E\widehat\Pi^\ell_{n,ab})^2,
$$

whereas each connected cross-copy pattern is expected to lose at least one
free neuron block. Establishing

$$
\operatorname{Var}(\widehat\Pi^\ell_{n,ab})=O(n^{-1})
$$

requires that complete enumeration and is not supplied by the two-path
calculation. Under such a theorem, the deterministic Stein bias is typically
$O(n^{-1})$, while finite-width random fluctuations are typically
$O_p(n^{-1/2})$.

For the sample loss

$$
\mathcal L_a=(f_a-y_a)^2,
$$

the normalized loss adjoint obeys the exact identity

$$
n^\alpha\frac{\partial\mathcal L_a}{\partial z_i^\ell(a)}
=
2(f_a-y_a)\beta_i^{\ell,a},
$$

and therefore

$$
\widehat\Pi^{\ell,\mathrm{loss}}_{n,ab}
=
4(f_a-y_a)(f_b-y_b)
\widehat\Pi^\ell_{n,ab}.
\tag{A.14}
$$

For the centered $\alpha=1$ readout, $f_a\to0$ and the limiting loss-adjoint
kernel is $4y_ay_b\Pi^\ell_{ab}$. For $\alpha=1/2$, the output has a
nondegenerate Gaussian-process limit $F$, so the loss-adjoint kernel generally
retains the random multiplier

$$
4(F_a-y_a)(F_b-y_b)\Pi^\ell_{ab}.
$$

If $F$ is centered with covariance $K^f$, its annealed expectation is

$$
4(K^f_{ab}+y_ay_b)\Pi^\ell_{ab}.
\tag{A.15}
$$

The backward kernel here is a second-moment object. It is not the mixed first
moment $M_{k,\ell}$ from the historical NTK sample. With a declared parameter
coordinate and optimizer metric, a layerwise tangent-kernel contribution is a
forward activation Gram multiplied entrywise by the corresponding backward
kernel, together with the appropriate scaling factor.

# Appendix B. Complete two-sample five-branch backward audit

Section 4 gives the full fixed-batch derivation and branch-order count. This
appendix records the explicit two-sample branch formula that is useful for
checking a symbolic implementation. It adds no new independence assumption.

Fix two samples $a,b$. For $\ell=1,2,3$, let $\mathbb E_\ell$ denote
expectation under $Z^\ell\sim N(0,G^{\ell-1})$ and define

$$
D_\ell
=
\mathbb E_\ell[
\phi'(Z_a)\phi'(Z_b)],
$$

$$
C_\ell(c,d)
=
\mathbb E_\ell\left[
\partial_c\partial_d
\{\phi'(Z_a)\phi'(Z_b)\}
\right].
\tag{B.1}
$$

The only nonzero second derivatives in (B.1) are generated by occurrences of
$a$ and $b$. When $a\ne b$, they are explicitly

$$
\begin{array}{c|c}
(c,d)&\partial_c\partial_d
\{\phi'(Z_a)\phi'(Z_b)\}\\ \hline
(a,a)&\phi'''(Z_a)\phi'(Z_b)\\
(a,b)&\phi''(Z_a)\phi''(Z_b)\\
(b,a)&\phi''(Z_a)\phi''(Z_b)\\
(b,b)&\phi'(Z_a)\phi'''(Z_b).
\end{array}
\tag{B.2}
$$

If $a=b$, coincident factor occurrences must be summed. For example,

$$
\partial_{aa}[\phi'(Z_a)^2]
=
2\phi'''(Z_a)\phi'(Z_a)
+2\phi''(Z_a)^2.
\tag{B.2a}
$$

The occurrence formula (B.5) below handles both distinct and coincident sample
labels without a separate case convention.

For auxiliary sample labels $c,d$, set

$$
P_{cd}(Z)
=
\phi'(Z_a)\phi'(Z_b)\phi(Z_c)\phi(Z_d),
$$

$$
L_c(Z)=\phi'(Z_a)\phi(Z_c),
\qquad
R_d(Z)=\phi'(Z_b)\phi(Z_d).
\tag{B.3}
$$

The one-row first derivatives are fully explicit. For example,

$$
\partial_uL_c(Z)
=
\mathbf 1_{u=a}\phi''(Z_a)\phi(Z_c)
+\mathbf 1_{u=c}\phi'(Z_a)\phi'(Z_c),
\tag{B.4}
$$

with the analogous formula for $R_d$ after replacing $a$ by $b$.

To expand the second derivative of $P_{cd}$ without hiding product-rule
terms, regard its four factor occurrences as

$$
(a,1),\quad(b,1),\quad(c,0),\quad(d,0),
$$

where the second coordinate is the derivative order and
$\phi^{(0)}=\phi$. If these pairs are denoted locally by $(r_j,m_j)$, then

$$
\begin{aligned}
\partial_u\partial_wP_{cd}(Z)
&=
\sum_{j=1}^4
\mathbf 1_{r_j=u}\mathbf 1_{r_j=w}
\phi^{(m_j+2)}(Z_{r_j})
\prod_{k\ne j}\phi^{(m_k)}(Z_{r_k})
\\
&\quad+
\sum_{j\ne k}
\mathbf 1_{r_j=u}\mathbf 1_{r_k=w}
\phi^{(m_j+1)}(Z_{r_j})
\phi^{(m_k+1)}(Z_{r_k})
\prod_{l\ne j,k}\phi^{(m_l)}(Z_{r_l}).
\end{aligned}
\tag{B.5}
$$

The occurrence notation handles repeated labels such as $c=a$ correctly.

After the readout peel, exact group-3 and group-2 Wick--Stein eliminations,
the $p=q$ versus $p\ne q$ split, and deterministic replacement of the two
empirical covariances, the complete structural expansion is

$$
\begin{aligned}
\mathbb E[\Pi^1_{n,ab}]
&=D_1D_2D_3
\\
&\quad+
\frac{D_3}{n}\sum_{u,w}C_2(u,w)
\mathbb E_1[
\phi'(Z_a)\phi'(Z_b)\phi(Z_u)\phi(Z_w)]
\\
&\quad+
\frac{D_1}{n}\sum_{c,d}C_3(c,d)
\mathbb E_2[P_{cd}(Z)]
\\
&\quad+
\frac1{n^2}\sum_{c,d,u,w}C_3(c,d)
\mathbb E_2[\partial_u\partial_wP_{cd}(Z)]
\\
&\hspace{29mm}\times
\mathbb E_1[
\phi'(Z_a)\phi'(Z_b)\phi(Z_u)\phi(Z_w)]
\\
&\quad+
\frac{n-1}{n^2}\sum_{c,d,u,w}C_3(c,d)
\mathbb E_2[\partial_uL_c(Z)]
\mathbb E_2[\partial_wR_d(Z)]
\\
&\hspace{29mm}\times
\mathbb E_1[
\phi'(Z_a)\phi'(Z_b)\phi(Z_u)\phi(Z_w)]
+o(1).
\end{aligned}
\tag{B.6}
$$

The five displayed branches have orders

$$
1,\qquad n^{-1},\qquad n^{-1},\qquad n^{-2},\qquad n^{-1},
\tag{B.7}
$$

respectively. Thus the leading expectation is

$$
\boxed{
\lim_{n\to\infty}\mathbb E[\Pi^1_{n,ab}]
=D_1D_2D_3.
}
\tag{B.8}
$$

The $o(1)$ in (B.6) records deterministic replacement of the empirical
group-2 and group-3 covariances. Consequently (B.6) is a complete structural
branch expansion after the leading mean-field reduction, not an exact
finite-width $1/n$ asymptotic expansion. Fluctuations of those empirical
covariances can alter the displayed $1/n$ coefficient even though they cannot
alter (B.8).

The final group contains no explicit $W^1$ factor because the observable is a
kernel of derivatives with respect to $z^1$. It is peeled by the row law of
large numbers

$$
\frac1n\sum_i
F(z_i^1(1),\ldots,z_i^1(B))
\longrightarrow
\mathbb E_{Z\sim N(0,G^0)}[F(Z)].
\tag{B.9}
$$

Upgrading (B.8) from an expectation limit to convergence of the random kernel
requires the separate four-path calculation stated as an obligation in
Section 4.4.
