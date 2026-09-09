# Executive orientation

## The idea in one sentence

Mean-field peeling is a layer-by-layer method for reducing a width-normalized
scalar contraction of neural-network derivatives to explicit Gaussian
expectations: expose the highest active layer, integrate its fresh Gaussian
weights exactly by Wick and Stein identities, pass every lower-layer factor
created by that integration to the next layer, and repeat.

This formulation is deliberately more precise than saying that weights and
activations become independent. They do not become independent in the way
needed by the calculation. The same matrix creates both a preactivation and
many backward or differentiated fields. The resulting correlations are the
source of Stein, or Onsager, response terms. Some vanish after complete width
counting; others are leading and encode feature learning.

## What is established, and what is not

Four levels of claim are used throughout.

1. **Exact finite-width identity.** This follows from ordinary differentiation,
   conditioning, Gaussian integration by parts, or Taylor expansion. No width
   limit has been taken.

2. **Audited mean-field result.** The displayed limit follows from the peel
   under the stated smoothness, moment, leave-one-out, joint-CLT, and
   concentration assumptions. The backward kernel and one-step coefficients
   are presented at this level.

3. **Formal mean-field closure.** The finite differentiated state and its local
   Gaussian operations are specified, but a complete joint convergence theorem
   for every registered channel has not yet been supplied. The general
   nonlinear two-step recursion has this status.

4. **Open theorem program.** The broad assertion that every admissible
   fixed-order derivative observable has a depth-linear finite-state Gaussian
   normal form remains to be proved.

The central mathematical correction made during the worked examples is this:
the network is not globally jointly Gaussian across layers. Gaussianity is
exact only **conditionally and one layer at a time**. This conditional law is
enough for peeling.

## Headline computational result

For a fixed batch of size \(B\), fixed depth, and fixed derivative order, every
worked coefficient below reduces to expectations of explicit scalar functions
of finitely many Gaussian base vectors. Each primitive preactivation vector is
only \(B\)-dimensional. At higher derivative order several jointly generated
base vectors may be needed, giving total Gaussian dimension \(qB\), where
\(q\) is finite and independent of width.

The hoped-for theorem would additionally prove that, at fixed derivative
order, the state size \(q\) can be chosen independently of depth. Only then
does the informal claim of an \(O(L)\) algorithm follow.

# 1. Baseline network and the mean-field state

## 1.1 General fully connected network

Take a fixed batch

$$
\{(x_a,y_a):a=1,\ldots,B\}.
$$

For a general fully connected network, write the effective forward weights as

$$
A^\ell_{ij}=s_{\ell,n}\theta^\ell_{ij},
$$

where \(\theta^\ell\) is the raw parameter optimized during training and
\(s_{\ell,n}\) records the forward normalization. The forward pass is

$$
z_i^\ell(a)
=
\sum_j A^\ell_{ij}h_j^{\ell-1}(a)
+\sigma_{b,\ell}b_i^\ell,
\qquad
h_i^\ell(a)=\phi_\ell(z_i^\ell(a)),
$$

with \(h^0(a)=x_a\).

For fan-in Gaussian initialization,

$$
A^\ell_{ij}
\sim
N\left(0,\frac{\sigma_{w,\ell}^2}{n_{\ell-1}}\right).
$$

Before any peeling calculation, one must record:

- every width and limiting width ratio;
- raw and effective parameter coordinates;
- weight and bias variances;
- output normalization;
- optimizer or \(\mu\)P metric factors;
- normalization of the observable;
- desired order in width;
- whether the target is an expectation, deterministic limit, or fluctuation.

A missing normalization in this ledger changes the diagram degree and can
change which contractions survive.

## 1.2 Exact conditional Gaussianity

Let

$$
\mathcal F_{\ell-1}
=
\sigma(A^1,b^1,\ldots,A^{\ell-1},b^{\ell-1})
$$

be the information in all lower layers. Conditional on
\(\mathcal F_{\ell-1}\), the row blocks

$$
\bigl(A^\ell_{i,:},b_i^\ell,
      z_i^\ell(1),\ldots,z_i^\ell(B)\bigr)
$$

are independent centered jointly Gaussian vectors across \(i\). Their exact
finite-width covariance is

$$
Q^\ell_{n,ab}
:=
\operatorname{Cov}
\left(z_i^\ell(a),z_i^\ell(b)\mid\mathcal F_{\ell-1}\right)
=
\frac{\sigma_{w,\ell}^2}{n_{\ell-1}}
\sum_jh_j^{\ell-1}(a)h_j^{\ell-1}(b)
+\sigma_{b,\ell}^2,
$$

$$
\operatorname{Cov}(A^\ell_{ij},A^\ell_{i'j'})
=
\delta_{ii'}\delta_{jj'}
\frac{\sigma_{w,\ell}^2}{n_{\ell-1}},
$$

and

$$
\operatorname{Cov}
\left(A^\ell_{ij},z_{i'}^\ell(a)
\mid\mathcal F_{\ell-1}\right)
=
\delta_{ii'}
\frac{\sigma_{w,\ell}^2}{n_{\ell-1}}
h_j^{\ell-1}(a).
$$

This last covariance is the source of every Stein response. Notice that it
contains a lower-layer activation. Peeling the current layer therefore creates
boundary data for the next layer.

Unconditionally, these covariances are random. The joint distribution across
several layers is generally a Gaussian mixture, not one multivariate Gaussian.

## 1.3 Deterministic forward Gram recursion

Under standard law-of-large-numbers and moment assumptions,
\(Q^\ell_n\) converges to a deterministic \(B\times B\) matrix \(Q^\ell\).
Starting from

$$
Q^1_{ab}
=
\sigma_{w,1}^2\frac{x_a^\top x_b}{n_0}
+\sigma_{b,1}^2,
$$

the recursion is

$$
Q^{\ell+1}_{ab}
=
\sigma_{w,\ell+1}^2
\mathbb E_{Z\sim N(0,Q^\ell)}
\left[\phi_\ell(Z_a)\phi_\ell(Z_b)\right]
+\sigma_{b,\ell+1}^2.
$$

This recursion supplies the deterministic covariance at which the explicit
Gaussian moments produced by peeling are evaluated. Labels do not enter these
initialization covariances; they enter through the loss and training vector
field.

# 2. What may be peeled

## 2.1 Groups and explicit atoms

Group \(\ell\) contains:

- layer-\(\ell\) weights and biases;
- coordinates \(z_i^\ell(a)\);
- scalar functions of those coordinates, including
  \(\phi,\phi',\phi'',\ldots\).

A backward error, Hessian-vector product, or training-time derivative is not
initially explicit. Chain rule, product rule, and, when necessary,
Faà di Bruno expansion express it as a finite sum of products of explicit
atoms.

The natural first domain of the theory is:

> width-normalized scalar contractions of finitely many parameter, input, or
> training-time derivatives of the network, loss, or a smooth
> permutation-invariant observable, evaluated on a fixed batch at
> initialization.

The word scalar matters. An uncontracted Hessian with a growing number of free
indices is not one finite peeling state. Ratios, matrix inverses, maxima, and
spectral edges require extra regularity and nondegeneracy arguments.

## 2.2 Scalar contraction normal form

After expansion and scalarization, one term has the form

$$
T_n
=
c_n
\sum_{\boldsymbol\iota}
\mathbf 1\{\mathcal C(\boldsymbol\iota)\}
\prod_{r=1}^{R_W}A^{\ell_r}_{i_rj_r}
\prod_{s=1}^{R_Z}
\psi_s(z^{k_s}_{u_s}(a_s)).
$$

The state must retain:

- neuron indices and their layers;
- fixed batch labels;
- exact equality and inequality constraints;
- derivative order of each scalar function;
- all explicit powers of width;
- open lower-layer indices created by the current peel.

Because every factor is now scalar, factors may be reordered by group. The
highest active group is placed on the right and integrated first.

# 3. The exact Gaussian calculus

## 3.1 One-weight Stein identity

If \((X,Z)\) is jointly centered Gaussian and \(F\) is differentiable with
integrable derivative, then

$$
\mathbb E[X F(Z)]
=
\sum_\alpha
\operatorname{Cov}(X,Z_\alpha)
\mathbb E[\partial_\alpha F(Z)].
$$

This identity does not say that \(X\) may be declared independent of \(Z\).
It exactly transfers the dependence into a derivative of \(F\).

For a current-layer weight,

$$
\mathbb E
\left[
A^\ell_{ij}F(Z_i^\ell)
\mid\mathcal F_{\ell-1}
\right]
=
\frac{\sigma_{w,\ell}^2}{n_{\ell-1}}
\sum_{a=1}^B
h_j^{\ell-1}(a)
\mathbb E
\left[
\partial_{z_i^\ell(a)}F(Z_i^\ell)
\mid\mathcal F_{\ell-1}
\right].
$$

The lower-layer factor \(h_j^{\ell-1}(a)\) must remain explicit until group
\(\ell-1\) is peeled.

## 3.2 Two-weight identity

For centered jointly Gaussian \(X,Y,Z\),

$$
\begin{aligned}
\mathbb E[XYF(Z)]
={}&
\operatorname{Cov}(X,Y)\mathbb E[F(Z)]
\\
&+
\sum_{\alpha,\beta}
\operatorname{Cov}(X,Z_\alpha)
\operatorname{Cov}(Y,Z_\beta)
\mathbb E[\partial_{\alpha\beta}F(Z)].
\end{aligned}
$$

The first line is the direct Wick pairing. The second line is the double Stein
attachment. Neither branch may be dropped before global width counting.

## 3.3 General partial-matching identity

Let \(X_1,\ldots,X_r\) be current-group Gaussian parameter coordinates and
let \(F(Z)\) contain all current-group preactivation functions. Conditional on
the lower layers,

$$
\begin{aligned}
\mathbb E\left[\prod_{q=1}^rX_qF(Z)\right]
={}&
\sum_{\pi}
\left(
\prod_{\{q,t\}\in\pi}
\operatorname{Cov}(X_q,X_t)
\right)
\\
&\times
\sum_{\alpha:U(\pi)\to\mathcal I_Z}
\left(
\prod_{q\in U(\pi)}
\operatorname{Cov}(X_q,Z_{\alpha(q)})
\right)
\mathbb E[
\partial_{\alpha(U(\pi))}F(Z)].
\end{aligned}
$$

Here \(\pi\) ranges over partial matchings of the weight occurrences and
\(U(\pi)\) is the unmatched set.

- Each matched pair is a weight-weight Wick contraction.
- Each unmatched weight attaches to one preactivation by Stein's identity.
- Each attachment differentiates the top nonlinear factor.
- Each attachment inserts a lower-layer activation through its covariance.

Complete matchings are sometimes called pseudo-independent terms. Partial
matchings are Onsager branches. These names do not decide asymptotic size.

## 3.4 Equality partitions

For top-row indices \(i_1,\ldots,i_q\), split the sum by exact equality
partition:

$$
\sum_{i_1,\ldots,i_q}
=
\sum_{\pi\in\mathcal P_q}
\sum_{\ker(\boldsymbol i)=\pi}.
$$

If a partition has \(|\pi|\) distinct blocks, it has

$$
n_\ell^{|\pi|}(1+O(n_\ell^{-1}))
$$

assignments before other constraints are imposed.

For one row block define the primitive moment

$$
\Gamma_\ell
[(a_1,\psi_1),\ldots,(a_s,\psi_s);Q]
:=
\mathbb E_{Z\sim N(0,Q)}
\left[\prod_{r=1}^s\psi_r(Z_{a_r})\right].
$$

Different row blocks become products of such moments. Each primitive
expectation is at most \(B\)-dimensional.

## 3.5 Global width counting

The width degree of a diagram includes:

- one positive power for every free neuron-index block;
- negative powers from weight covariances;
- negative powers from weight-preactivation attachments;
- observable normalization;
- raw-to-effective parameter multipliers;
- optimizer or \(\mu\)P metric factors;
- lower-layer sums created by Stein attachments.

The last item is essential. A branch that looks subleading in the current
layer can create a lower-layer free sum and recover its order. Conversely, a
locally leading branch may later be forced onto a diagonal and lose a width.
Only the complete boundary signature permits a valid decision.

The distinction between one-copy and two-copy calculations is equally
important. An off-diagonal family may have zero one-copy mean yet survive in a
second moment as a fresh Gaussian fluctuation field.

## 3.6 Replacing random Grams

Exact conditional integration produces moments evaluated at the empirical
covariance \(Q_n^\ell\). Only after distinguished indices have been exposed
and removed by a leave-finitely-many-out argument may one use

$$
Q_n^\ell\longrightarrow Q^\ell
$$

and replace

$$
\Gamma_\ell[\cdots;Q_n^\ell]
\longrightarrow
\Gamma_\ell[\cdots;Q^\ell].
$$

Uniform integrability is needed to pass from convergence in probability to
expectation.

If the zeroth-order term vanishes or a fluctuation is deliberately magnified,
one may need to expand in \(Q_n^\ell-Q^\ell\). Price's identity keeps this
expansion inside Gaussian derivative calculus:

$$
D\,\mathbb E_{Z\sim N(0,Q)}[F(Z)][H]
=
\frac12\sum_{a,b}
H_{ab}\mathbb E[\partial_{ab}F(Z)].
$$

# 4. The peeling algorithm

Given an admissible scalar contraction, perform the following pass.

1. Fix the scaling ledger and the desired asymptotic order.
2. Expand derivatives only far enough to expose the highest active group.
3. Scalarize every contraction involving that group.
4. Record exact width factors and all lower-layer boundary indices.
5. Condition on all lower groups.
6. Split top-row indices into compatible equality partitions.
7. Apply the generalized Wick-Stein identity until no explicit top-group
   Gaussian parameter remains.
8. Expand all derivatives created on nonlinear factors.
9. Substitute exact conditional covariances.
10. Resolve Kronecker deltas and update the lower-layer boundary state.
11. Perform global width counting, including all downstream sums.
12. Convert surviving top-row functions to Gaussian row moments.
13. Replace the empirical covariance by its deterministic limit, or retain
    the covariance fluctuation required by the target.
14. Merge algebraically identical lower-layer states.
15. Repeat on the next lower group.
16. At layer zero, evaluate the remaining deterministic input and label
    contractions.

If convergence for a typical initialization is claimed, repeat the procedure
on the square, covariance, or relevant cumulants. Computing an expectation and
proving concentration are separate jobs.

## 4.1 Recursive-state form

If the active boundary signatures form a finite family \(\mathcal S\), one
peel can be written

$$
V_p(s)
=
\sum_{s'\in\mathcal S}
T_p(s,s';Q^p)V_{p-1}(s').
$$

Thus

$$
V_L
=
T_L(Q^L)\cdots T_1(Q^1)V_0.
$$

This expression explains the hoped-for dynamic program. There are \(L\)
layer transitions. But an \(O(L)\) theorem needs more: the state dimension
must be bounded independently of depth at fixed derivative order and
observable type. That closure remains an open proof obligation.

# 5. Worked execution I: the backward kernel

## 5.1 Fixed three-hidden-layer network

For the concrete audit, all hidden widths are \(n\), the input dimension
\(d_0\) and batch size \(B\) are fixed, and

$$
z_i^1(a)=\frac1{\sqrt{d_0}}\sum_jW^1_{ij}x_{a,j},
\qquad
h_i^1(a)=\phi(z_i^1(a)),
$$

$$
z_p^2(a)=\frac1{\sqrt n}\sum_iW^2_{pi}h_i^1(a),
\qquad
h_p^2(a)=\phi(z_p^2(a)),
$$

$$
z_r^3(a)=\frac1{\sqrt n}\sum_pW^3_{rp}h_p^2(a),
\qquad
h_r^3(a)=\phi(z_r^3(a)),
$$

$$
f_a=\frac1n\sum_rv_rh_r^3(a).
$$

All entries of \(W^1,W^2,W^3,v\) are independent \(N(0,1)\).

Define the activation Grams

$$
G^0_{ab}=\frac{x_a^\top x_b}{d_0},
\qquad
G^\ell_{n,ab}
=
\frac1n\sum_i h_i^\ell(a)h_i^\ell(b),
$$

and their deterministic limits recursively by

$$
Z^\ell\sim N(0,G^{\ell-1}),
\qquad
G^\ell_{ab}
=
\mathbb E[\phi(Z^\ell_a)\phi(Z^\ell_b)].
$$

Also define

$$
D^\ell_{ab}
=
\mathbb E[
\phi'(Z^\ell_a)\phi'(Z^\ell_b)].
$$

## 5.2 Normalized backward variables

Define

$$
\delta_i^\ell(a)
:=
n\frac{\partial f_a}{\partial z_i^\ell(a)}.
$$

The exact chain rule gives

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

$$
\delta_i^1(a)
=
\phi'(z_i^1(a))
\frac1{\sqrt n}\sum_pW^2_{pi}\delta_p^2(a).
$$

The backward empirical kernels are

$$
\Pi^\ell_{n,ab}
=
\frac1n\sum_i
\delta_i^\ell(a)\delta_i^\ell(b).
$$

The target is first their expectation and then, separately, their
concentration.

## 5.3 Peel the readout and group 3

At the top hidden layer,

$$
\begin{aligned}
\mathbb E[\Pi^3_{n,ab}]
&=
\frac1n\sum_r
\mathbb E[
v_r^2\phi'(z_r^3(a))\phi'(z_r^3(b))]
\\
&=
\frac1n\sum_r
\mathbb E[
\phi'(z_r^3(a))\phi'(z_r^3(b))],
\end{aligned}
$$

because \(v\) is independent of the hidden weights and
\(\mathbb E[v_r^2]=1\). Conditional on the first two groups, the rows
\(z_r^3\) are iid Gaussian with empirical covariance \(G^2_n\). Therefore

$$
\mathbb E[\Pi^3_{n,ab}\mid\mathcal F_2]
=
\mathbb E_{Z\sim N(0,G^2_n)}
[\phi'(Z_a)\phi'(Z_b)].
$$

After the leave-one-out and covariance-replacement step,

$$
\Pi^3_{ab}=D^3_{ab}.
$$

## 5.4 Full group-3 scalarization for the layer-2 kernel

Substitute the group-3 recursion twice:

$$
\begin{aligned}
\Pi^2_{n,ab}
=
\frac1{n^2}
\sum_{p,r,s}
&\phi'(z_p^2(a))\phi'(z_p^2(b))
W^3_{rp}W^3_{sp}
\\
&\times
v_rv_s
\phi'(z_r^3(a))\phi'(z_s^3(b)).
\end{aligned}
$$

The readout Wick contraction forces \(r=s\):

$$
\mathbb E_v[v_rv_s]=\delta_{rs}.
$$

Hence

$$
\mathbb E_v[\Pi^2_{n,ab}\mid W^1,W^2,W^3]
=
\frac1{n^2}\sum_{p,r}
\phi'(z_p^2(a))\phi'(z_p^2(b))
(W^3_{rp})^2
\phi'(z_r^3(a))\phi'(z_r^3(b)).
$$

Now condition on groups 1 and 2. For fixed \(r,p\),
\(W^3_{rp}\) and \(Z_r^3=(z_r^3(1),\ldots,z_r^3(B))\) are jointly
Gaussian with

$$
\operatorname{Cov}(W^3_{rp},z_r^3(c)\mid\mathcal F_2)
=
\frac{h_p^2(c)}{\sqrt n}.
$$

Let

$$
F_r
=
\phi'(z_r^3(a))\phi'(z_r^3(b)).
$$

The exact two-weight identity gives

$$
\mathbb E[(W^3_{rp})^2F_r\mid\mathcal F_2]
=
\mathbb E[F_r\mid\mathcal F_2]
+
\frac1n
\sum_{c,d}
h_p^2(c)h_p^2(d)
\mathbb E[\partial_{cd}F_r\mid\mathcal F_2].
$$

The first term is the Wick branch. The second is the complete double-Stein
branch. It is not zero and has not been hidden by an independence claim.

Substitution yields two families. The Wick family is

$$
\frac1{n^2}\sum_{p,r}
\phi'(z_p^2(a))\phi'(z_p^2(b))
\mathbb E[F_r\mid\mathcal F_2].
$$

It has \(n^2\) assignments and an \(n^{-2}\) normalization, so it survives.
The row average over \(r\) gives \(D^3_{ab}\); the row average over \(p\)
belongs to group 2 and is retained until group 2 is peeled.

The double-Stein family is

$$
\frac1{n^3}
\sum_{p,r}\sum_{c,d}
\phi'(z_p^2(a))\phi'(z_p^2(b))
h_p^2(c)h_p^2(d)
\mathbb E[\partial_{cd}F_r\mid\mathcal F_2].
$$

The batch sums are fixed, and only \(p,r\) are free, so this family is
\(O(n^{-1})\), assuming bounded Gaussian derivative moments. It vanishes for
the leading expectation.

The important procedural point is that
\(h_p^2(c)h_p^2(d)\) belongs to group 2. It is not averaged during the
group-3 peel. It is carried as lower-boundary data until its global order has
been decided.

Therefore the surviving group-3 reduction is

$$
\mathbb E[\Pi^2_{n,ab}]
=
D^3_{ab}
\mathbb E\left[
\frac1n\sum_p
\phi'(z_p^2(a))\phi'(z_p^2(b))
\right]
+o(1).
$$

Peeling group 2 now gives

$$
\boxed{\Pi^2_{ab}=D^2_{ab}D^3_{ab}.}
$$

## 5.5 Continue through group 2 and group 1

Fully expanding \(\Pi^1_n\) produces two copies of every path:

$$
\begin{aligned}
\Pi^1_{n,ab}
=
\frac1{n^3}
\sum_{i,p,q,r,s}
&\phi'(z_i^1(a))\phi'(z_i^1(b))
W^2_{pi}W^2_{qi}
\\
&\times
\phi'(z_p^2(a))\phi'(z_q^2(b))
W^3_{rp}W^3_{sq}
\\
&\times
v_rv_s
\phi'(z_r^3(a))\phi'(z_s^3(b)).
\end{aligned}
$$

The correct order is:

1. peel the readout, forcing \(r=s\);
2. condition on groups 1 and 2 and peel group 3;
3. retain both the direct \(W^3\)-pairing branch and every Stein branch;
4. resolve the induced equalities among \(p,q,r\);
5. pass any group-2 activations created by group-3 Stein derivatives downward;
6. peel group 2;
7. finally average the remaining group-1 gate product.

The leading ladder diagram is obtained by the direct pairings

$$
v_r\leftrightarrow v_s,
\qquad
W^3_{rp}\leftrightarrow W^3_{sq},
\qquad
W^2_{pi}\leftrightarrow W^2_{qi}.
$$

They impose

$$
r=s,
\qquad
p=q,
$$

and leave one free row index at each hidden group. Their covariance powers are
exactly balanced by the three normalized row sums. The surviving gate
averages are

$$
D^3_{ab},\qquad D^2_{ab},\qquad D^1_{ab}.
$$

Every group-3 Stein attachment differentiates a group-3 gate and inserts one
or more group-2 activations. Those factors are carried into the group-2
scalarization. In this two-copy backward observable, complete equality
partitioning shows that each such connected correction either contains an
extra \(n^{-1}\) covariance without a compensating free sum or forces an
additional row equality. The same is true of the group-2 Stein branches.
Thus they are \(o(1)\) for this leading expectation.

Consequently,

$$
\boxed{
\Pi^1_{ab}=D^1_{ab}D^2_{ab}D^3_{ab}.
}
$$

Together,

$$
\boxed{
\Pi^3=D^3,\qquad
\Pi^2=D^2\odot D^3,\qquad
\Pi^1=D^1\odot D^2\odot D^3,
}
$$

where \(\odot\) means entrywise multiplication.

## 5.6 Expectation is not concentration

The preceding calculation identifies the annealed limits. To substitute
\(\Pi_n^\ell\) inside another random product, one also needs

$$
\operatorname{Var}(\Pi^\ell_{n,ab})\longrightarrow0.
$$

That is a four-copy peeling problem. One scalarizes
\(\Pi^\ell_{n,ab}\Pi^\ell_{n,ab}\), classifies equality partitions shared
between the two copies, and shows that every connected cross-copy diagram
loses at least one width. Uniform integrability then upgrades convergence in
probability to convergence of the relevant expectations.

This separate obligation is easy to suppress in informal NTK arguments and
must be explicit in a theorem.

# 6. Worked execution II: one muP gradient step

## 6.1 Parameterization and update

Use the same three-hidden-layer network. The effective forward tensors are

$$
\frac{W^1}{\sqrt{d_0}},
\qquad
\frac{W^2}{\sqrt n},
\qquad
\frac{W^3}{\sqrt n},
\qquad
\frac vn.
$$

Their entry variances are respectively

$$
\frac1{d_0},\qquad \frac1n,\qquad \frac1n,\qquad\frac1{n^2}.
$$

In the raw coordinates used here, the \(\mu\)P maximal-update rule is

$$
\theta^+
=
\theta-n\eta\nabla_\theta\mathcal J,
\qquad
\theta\in\{W^1,W^2,W^3,v\},
$$

with average squared loss

$$
\mathcal J
=
\frac1B\sum_{c=1}^B(f_c-y_c)^2.
$$

Write \(e_c=f_c-y_c\). There is no factor \(1/2\) in the loss, so the
gradient carries \(2/B\).

The width limit is always taken coefficientwise: first form the finite-width
Taylor coefficient in \(\eta\), then send \(n\) to infinity. No joint
finite-\(\eta\), infinite-width limit is implied by the coefficient
calculation alone.

## 6.2 Exact optimizer-metric tangent kernel

Define

$$
K_{n,ab}
=
n\sum_{k=1}^3
\left\langle
\nabla_{W^k}f_a,\nabla_{W^k}f_b
\right\rangle
+n\langle\nabla_vf_a,\nabla_vf_b\rangle.
$$

The exact output velocity is

$$
\dot f_a
:=
\left.\frac{df_a^+}{d\eta}\right|_{\eta=0}
=
-\frac2B\sum_cK_{n,ac}e_c.
$$

Every parameter gradient factorizes. For example,

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
\left(\frac1n\sum_r
\delta_r^3(a)\delta_r^3(b)\right)
\left(\frac1n\sum_p
h_p^2(a)h_p^2(b)\right)
\\
&=
\Pi^3_{n,ab}G^2_{n,ab}.
\end{aligned}
$$

Doing this for every block gives the exact identity

$$
\boxed{
K_{n,ab}
=
G^3_{n,ab}
+G^2_{n,ab}\Pi^3_{n,ab}
+G^1_{n,ab}\Pi^2_{n,ab}
+G^0_{ab}\Pi^1_{n,ab}.
}
$$

Backward peeling and concentration give the deterministic limit

$$
\boxed{
\begin{aligned}
K_{ab}
={}&
G^3_{ab}
+G^2_{ab}D^3_{ab}
+G^1_{ab}D^2_{ab}D^3_{ab}
\\
&+
G^0_{ab}D^1_{ab}D^2_{ab}D^3_{ab}.
\end{aligned}
}
$$

This is the usual layerwise tangent recursion written in the fixed raw
coordinate convention.

## 6.3 Linear change in output and loss

At initialization, the centered \(1/n\) readout makes

$$
f_a=O_{L^p}(n^{-1/2})
\longrightarrow0,
\qquad
e_a\longrightarrow-y_a.
$$

Weighted convergence, not finite-width independence, then gives

$$
\lim_{n\to\infty}\mathbb E[\dot f_a]
=
\frac2B\sum_cK_{ac}y_c.
$$

For the individual loss \(\ell_a=e_a^2\),

$$
\dot\ell_a
=
2e_a\dot f_a
=
-\frac4B e_a\sum_cK_{n,ac}e_c.
$$

Therefore

$$
\boxed{
\mathbb E[\ell_a^+]
=
y_a^2
-\frac{4\eta}{B}
y_a\sum_cK_{ac}y_c
+o(\eta)+o_n(1).
}
$$

For the average loss,

$$
\boxed{
\mathbb E[\mathcal J^+]
=
\frac1B\sum_a y_a^2
-\frac{4\eta}{B^2}y^\top Ky
+o(\eta)+o_n(1).
}
$$

The average coefficient is nonpositive because \(K\) is positive
semidefinite. An individual sample loss need not decrease.

## 6.4 Exact hidden-Gram linear coefficient

Let

$$
u_i^\ell(a)
:=
\left.\frac{dz_i^{\ell,+}(a)}{d\eta}\right|_0,
\qquad
g_i^\ell(a)
:=
\phi'(z_i^\ell(a))u_i^\ell(a).
$$

The coefficient of \(\eta\) in the layer-\(\ell\) activation Gram is exactly

$$
L^\ell_{n,ab}
=
\frac1n\sum_i
\left[
g_i^\ell(a)h_i^\ell(b)
+h_i^\ell(a)g_i^\ell(b)
\right].
$$

Equivalently,

$$
L^\ell_{n,ab}
=
-\frac{2n}{B}\sum_c e_c
\sum_{k\leq\ell}
\left\langle
\nabla_{W^k}G^\ell_{n,ab},
\nabla_{W^k}f_c
\right\rangle.
$$

The readout is the highest active group, so it must be peeled first. Every
backward variable is linear in \(v\). The label branch
\(-y_c\delta_j^k(c)\) is odd in \(v\), hence its conditional readout
expectation is zero. The output branch contains two readout factors. Its exact
contraction is

$$
\begin{aligned}
\mathbb E_v[f_c\delta_j^k(c)]
&=
\frac1n\sum_r
h_r^3(c)\phi'(z_r^3(c))
\frac{\partial z_r^3(c)}{\partial z_j^k(c)}
\\
&=
\frac12
\frac{\partial G^3_{n,cc}}{\partial z_j^k(c)}.
\end{aligned}
$$

Substitution gives the exact conditional identity

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
$$

The top contraction has already lost one free neuron index. Peeling the
remaining groups changes its Gaussian moment but cannot restore that index.
Every path family is therefore \(O(n^{-1})\). Hence

$$
\mathbb E[L^\ell_{n,ab}]=O(n^{-1})
$$

and

$$
\boxed{
\lim_{n\to\infty}
[\eta]\,\mathbb E[G^{\ell,+}_{n,ab}]
=
0.
}
$$

This is an annealed cancellation caused by the centered readout. It does not
say that one finite-width realization has no first-order feature motion.

## 6.5 Exact quadratic Gram expansion

At finite width write

$$
z_i^{\ell,+}(a)
=
z_i^\ell(a)+\eta u_i^\ell(a)+\eta^2q_i^\ell(a)+o(\eta^2),
$$

$$
h_i^{\ell,+}(a)
=
h_i^\ell(a)+\eta g_i^\ell(a)+\eta^2s_i^\ell(a)+o(\eta^2).
$$

Taylor expansion gives

$$
g_i^\ell(a)
=
\phi'(z_i^\ell(a))u_i^\ell(a),
$$

$$
s_i^\ell(a)
=
\phi'(z_i^\ell(a))q_i^\ell(a)
+\frac12\phi''(z_i^\ell(a))u_i^\ell(a)^2.
$$

Because the first preactivation is linear in \(W^1\), \(q^1=0\). For
\(\ell=2,3\),

$$
q_i^\ell(a)
=
\frac1{\sqrt n}\sum_j
\left[
W^\ell_{ij}s_j^{\ell-1}(a)
+\dot W^\ell_{ij}g_j^{\ell-1}(a)
\right].
$$

The exact quadratic Gram coefficient is

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
$$

The residual product in a quadratic velocity is

$$
e_ce_d
=
y_cy_d-y_cf_d-y_df_c+f_cf_d.
$$

The mixed branches are odd in the readout and vanish. The output-output
branch is \(O(n^{-1})\). Thus the label-label branch is leading. Define

$$
\lambda_c:=\frac{2y_c}{B}.
$$

## 6.6 Backward and tangent states used by the quadratic peel

Separate the local gate from the incoming backward signal:

$$
\delta^\ell(a)
=
\phi'(Z^\ell_a)\xi^\ell(a).
$$

Under the required joint conditional CLT and leave-one-out estimates, the
representative Gaussian base fields satisfy

$$
Z^\ell\perp\xi^\ell,
\qquad
\mathbb E[\xi^\ell(a)\xi^\ell(b)]
=
P^\ell_{ab},
$$

where

$$
P^3_{ab}=1,
\qquad
P^2_{ab}=D^3_{ab},
\qquad
P^1_{ab}=D^2_{ab}D^3_{ab}.
$$

This is a limiting statement proved by peeling mixed moments; it is not a
finite-width independence assumption.

Define the partial tangent states

$$
T^0=G^0,
$$

$$
T^1=G^1+D^1\odot T^0,
$$

$$
T^2=G^2+D^2\odot T^1.
$$

Here and below \(\odot\) is entrywise multiplication.

## 6.7 Why the off-diagonal branch survives

At layer 2, the propagated part of the velocity contains

$$
\frac1n\sum_{i,p'}
W^2_{pi}W^2_{p'i}
\phi'(z_i^1(a))
\sum_c\lambda_cG^0_{ac}
\phi'(z_i^1(c))\delta_{p'}^2(c).
$$

The pattern \(p'=p\) gives the diagonal Stein response

$$
\sum_c\lambda_c
G^0_{ac}D^1_{ac}\delta_p^2(c).
$$

Together with the direct weight-update contribution, this produces

$$
\sum_c\lambda_cT^1_{ac}\delta_p^2(c).
$$

The pattern \(p'\ne p\) has zero one-copy conditional mean, but there are
\(n^2(1+o(1))\) such pairs. In two copies, its row-distinct Wick contractions
have order one and converge to a centered fresh Gaussian field. Denote that
field by \(\Gamma^2\). Repeating the same split at each layer yields

$$
\boxed{
u^\ell(a)
=
\Gamma^\ell(a)
+\sum_c\lambda_cT^{\ell-1}_{ac}\delta^\ell(c),
\qquad \ell=1,2,3,
}
$$

where \(\Gamma^1=0\) and

$$
\mathbb E[\Gamma^\ell(a)\Gamma^\ell(b)]
=
V^{\ell-1}_{ab},
\qquad
V^\ell_{ab}
:=
\mathbb E[g^\ell(a)g^\ell(b)].
$$

The mixed covariances required to declare the fresh Gaussian base independent
of the response variables must also be peeled. They vanish at this order by a
combination of readout parity and one-width loss. This is a joint-state
obligation, not a shortcut.

## 6.8 Closed one-step Gaussian recursions

Set \(V^0=0\). Squaring the preceding velocity law gives

$$
\boxed{
\begin{aligned}
V^\ell_{ab}
={}&
D^\ell_{ab}V^{\ell-1}_{ab}
\\
&+
\sum_{c,d}
\lambda_c\lambda_d
T^{\ell-1}_{ac}T^{\ell-1}_{bd}P^\ell_{cd}
\\
&\qquad\times
\mathbb E\left[
\phi'(Z^\ell_a)\phi'(Z^\ell_b)
\phi'(Z^\ell_c)\phi'(Z^\ell_d)
\right].
\end{aligned}
}
$$

The first line is exactly the row-distinct fresh-field branch. Replacing the
random empirical operator by its mean before squaring would delete this term
and give the wrong coefficient.

Define

$$
S^\ell_{ab}
:=
\mathbb E[s^\ell(a)h^\ell(b)],
\qquad
S^0=0.
$$

Peeling the second displacement gives

$$
\boxed{
\begin{aligned}
S^\ell_{ab}
={}&
D^\ell_{ab}S^{\ell-1}_{ab}
\\
&+
\mathbb E[
\phi(Z^\ell_b)\phi''(Z^\ell_a)]
\left(S^{\ell-1}_{aa}+\frac12V^{\ell-1}_{aa}\right)
\\
&+
\frac12\sum_{c,d}
\lambda_c\lambda_d
T^{\ell-1}_{ac}T^{\ell-1}_{ad}P^\ell_{cd}
\\
&\qquad\times
\mathbb E\left[
\phi(Z^\ell_b)\phi''(Z^\ell_a)
\phi'(Z^\ell_c)\phi'(Z^\ell_d)
\right].
\end{aligned}
}
$$

Every expectation here and in the \(V^\ell\) recursion is over the single
batch Gaussian vector

$$
Z^\ell\sim N(0,G^{\ell-1}).
$$

Finally,

$$
\boxed{
C^\ell_{ab}
=
V^\ell_{ab}+S^\ell_{ab}+S^\ell_{ba}.
}
$$

Thus

$$
\boxed{
\mathbb E[G^{\ell,+}_{n,ab}]
=
G^\ell_{ab}
+\eta\,O(n^{-1})
+\eta^2C^\ell_{ab}
+o(\eta^2)+o_n(1).
}
$$

## 6.9 Fully explicit first-layer answer

At layer 1, \(V^0=S^0=0\), \(T^0=G^0\), and
\(P^1_{cd}=D^2_{cd}D^3_{cd}\). With
\(Z^1\sim N(0,G^0)\), write only in this formula

$$
\phi_a=\phi(Z^1_a),
\qquad
\phi'_a=\phi'(Z^1_a),
\qquad
\phi''_a=\phi''(Z^1_a).
$$

Then

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
$$

This is already a fixed-dimensional explicit Gaussian integral. Layers 2 and
3 follow by evaluating the displayed recursions in order.

## 6.10 Deep-linear audit

Set \(\phi(z)=z\). Then \(D^\ell=P^\ell=1\),
\(S^\ell=0\), and every \(G^\ell=G^0\). Define

$$
\kappa=\frac2B,
\qquad
\sigma_a=\sum_cG^0_{ac}y_c.
$$

The partial tangents are

$$
T^0=G^0,\qquad T^1=2G^0,\qquad T^2=3G^0.
$$

The recursion gives

$$
\boxed{
C^1_{ab}=\kappa^2\sigma_a\sigma_b,\qquad
C^2_{ab}=5\kappa^2\sigma_a\sigma_b,\qquad
C^3_{ab}=14\kappa^2\sigma_a\sigma_b.
}
$$

The coefficient \(5\) is a decisive audit. Let

$$
M=\frac1nW^2W^{2\top}.
$$

The layer-2 velocity contains \(I+M\), so

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

Replacing \(M\) by its entrywise mean \(I\) before taking the square gives
\(4\), not \(5\). The missing unit is precisely the off-diagonal
Wick-fluctuation branch represented by \(\Gamma^2\).

# 7. Worked execution III: two Euler steps

## 7.1 Exact Taylor identity

Let the raw-coordinate \(\mu\)P vector field be

$$
F(\theta):=-n\nabla\mathcal J(\theta).
$$

Two Euler steps satisfy

$$
\theta^{(1)}=\theta+\eta F(\theta),
$$

$$
\theta^{(2)}
=
\theta^{(1)}+\eta F(\theta^{(1)})
=
\theta+2\eta F+\eta^2DF[F]+O(\eta^3).
$$

For an observable \(O(\theta)=G^\ell_{n,ab}(\theta)\), define

$$
L^\ell_{n,ab}=DO[F],
\qquad
C^\ell_{n,ab}=\frac12D^2O[F,F],
\qquad
R^\ell_{n,ab}=DO[DF[F]].
$$

Then the exact finite-width expansions are

$$
\boxed{
G^{\ell,(2)}_{n,ab}
=
G^\ell_{n,ab}
+2\eta L^\ell_{n,ab}
+\eta^2(4C^\ell_{n,ab}+R^\ell_{n,ab})
+O(\eta^3),
}
$$

and, for the second update alone,

$$
\boxed{
G^{\ell,(2)}_{n,ab}-G^{\ell,(1)}_{n,ab}
=
\eta L^\ell_{n,ab}
+\eta^2(3C^\ell_{n,ab}+R^\ell_{n,ab})
+O(\eta^3).
}
$$

The factors \(4\) and \(3\) are Taylor-combinatorial. A useful check is

$$
D_FL^\ell_{n,ab}
=
2C^\ell_{n,ab}+R^\ell_{n,ab}.
$$

Although \(L^\ell_n\to0\) in expectation, its directional derivative need
not vanish. A limiting zero may not be differentiated as though it were
identically zero.

## 7.2 Isolating the gradient correction

For squared loss,

$$
\nabla^2\mathcal J
=
\frac2B\sum_c
\left(
\nabla f_c\nabla f_c^\top
+e_c\nabla^2f_c
\right).
$$

Substitution gives the exact finite-width identity

$$
\begin{aligned}
R^\ell_{n,ab}
=
\frac4{B^2}\sum_{c,d}e_d
\Big[&
\left(n(\nabla G^\ell_{n,ab})^{\top}\nabla f_c\right)K_{n,cd}
\\
&+
e_c n^2
(\nabla G^\ell_{n,ab})^{\top}
\nabla^2f_c\nabla f_d
\Big].
\end{aligned}
$$

Readout parity and complete width counting suppress the leading
Gauss-Newton branch. In the Hessian branch, the label-label term survives,
while mixed label-output terms are odd and the output-output branch is
width-suppressed. Thus the leading correction is

$$
\boxed{
R^\ell_{ab}
=
\frac4{B^2}\sum_{c,d}y_cy_d
\lim_{n\to\infty}
\mathbb E\left[
n^2(\nabla G^\ell_{n,ab})^{\top}
\nabla^2f_c\nabla f_d
\right].
}
$$

## 7.3 Exact readout peel

The hidden Gram has no direct dependence on \(v\). If \(\theta\) is a hidden
parameter coordinate and \(\psi\) any parameter coordinate, the Hessian
contraction contains

$$
n^2\sum_{\theta\ {\rm hidden}}\sum_\psi
\partial_\theta G^\ell_{n,ab}
\partial_{\theta\psi}f_c
\partial_\psi f_d.
$$

If \(\psi=v_s\), the two factors \(1/n\) from the readout cancel \(n^2\).
If \(\psi\) is hidden, the exact readout Wick contraction
\(\mathbb E[v_rv_t]=\delta_{rt}\) again cancels those factors. Therefore

$$
\begin{aligned}
&\mathbb E_v\left[
n^2(\nabla G^\ell_{n,ab})^{\top}
\nabla^2f_c\nabla f_d
\mid W^1,W^2,W^3
\right]
\\
&=
\sum_{\theta\ {\rm hidden}}
\partial_\theta G^\ell_{n,ab}
\Bigg[
\sum_rh_r^3(d)\partial_\theta h_r^3(c)
\\
&\hspace{28mm}
+
\sum_{\psi\ {\rm hidden}}\sum_r
\partial_{\theta\psi}h_r^3(c)
\partial_\psi h_r^3(d)
\Bigg].
\end{aligned}
$$

This is the exact boundary state delivered from the readout to hidden group
3. No hidden weight has been declared independent of the preactivation it
creates.

## 7.4 Differentiated-state program

The Hessian contraction is computed without constructing a third-order
parameter tensor. Differentiate the ordinary forward and backward programs
in direction \(F\).

Keep

$$
u^\ell=D_Fz^\ell,
\qquad
g^\ell=D_Fh^\ell=\phi'(z^\ell)u^\ell,
$$

and define

$$
\dot\delta^\ell:=D_F\delta^\ell.
$$

At the top hidden layer,

$$
\dot\delta_r^3(a)
=
\dot v_r\phi'(z_r^3(a))
+v_r\phi''(z_r^3(a))u_r^3(a).
$$

For lower layers, because
\(\delta^\ell=\phi'(z^\ell)\xi^\ell\),

$$
\dot\delta^\ell(a)
=
\phi''(z^\ell(a))u^\ell(a)\xi^\ell(a)
+\phi'(z^\ell(a))\dot\xi^\ell(a),
$$

and the incoming differentiated signal obeys the exact recursion

$$
\dot\xi_j^\ell(a)
=
\frac1{\sqrt n}\sum_i
\left[
\dot W^{\ell+1}_{ij}\delta_i^{\ell+1}(a)
+W^{\ell+1}_{ij}\dot\delta_i^{\ell+1}(a)
\right].
$$

Now let

$$
A:=DF[F],
\qquad
\bar z^\ell:=D_Az^\ell,
\qquad
\bar h^\ell:=D_Ah^\ell
=
\phi'(z^\ell)\bar z^\ell.
$$

The leading label-label part of the differentiated matrix vector field is

$$
A_{W^\ell}^{\rm lead}
=
\frac1{\rho_\ell}\sum_c\lambda_c
\left[
\dot\delta^{\ell,(y)}(c)h^{\ell-1}(c)^\top
+\delta^\ell(c)g^{\ell-1,(y)}(c)^\top
\right],
$$

where

$$
\rho_1=\sqrt{d_0},
\qquad
\rho_2=\rho_3=\sqrt n.
$$

The correction-forward recursion is

$$
\bar z^1(a)=A_{W^1}\frac{x_a}{\sqrt{d_0}},
$$

$$
\bar z^\ell(a)
=
\frac1{\sqrt n}W^\ell\bar h^{\ell-1}(a)
+\frac1{\sqrt n}A_{W^\ell}h^{\ell-1}(a),
\qquad \ell=2,3.
$$

Finally,

$$
\boxed{
R^\ell_{n,ab}
=
\frac1n\sum_i
\left[
\bar h_i^\ell(a)h_i^\ell(b)
+h_i^\ell(a)\bar h_i^\ell(b)
\right].
}
$$

These directional equations are exact when the full states are retained.

## 7.5 Multichannel Wick-Stein rule

At two steps the same matrix creates several forward and transpose channels.
Suppose

$$
b_j^\alpha
=
\frac1{\sqrt n}\sum_iW_{ij}y_i^\alpha,
\qquad
\alpha=1,\ldots,q,
$$

and the source vectors are frozen with respect to \(W\). For a smooth
\(\Psi_j\) of all channels,

$$
\mathbb E[W_{ij}\Psi_j]
=
\frac1{\sqrt n}\sum_{\alpha=1}^q
y_i^\alpha
\mathbb E[\partial_{b^\alpha}\Psi_j].
$$

After the row sum and equality decomposition, the mean-field form is

$$
\boxed{
\frac1{\sqrt n}\sum_jW_{ij}\Psi_j
\Longrightarrow
\Gamma_\Psi
+\sum_{\alpha=1}^q
y_i^\alpha\mathbb E[\partial_{b^\alpha}\Psi].
}
$$

For two integrands,

$$
\mathbb E[\Gamma_\Psi(a)\Gamma_{\widetilde\Psi}(b)]
=
\mathbb E[\Psi(a)\widetilde\Psi(b)].
$$

The fresh Gaussian fields generated through the same matrix must be produced
jointly, with every cross-covariance retained. The transpose rule is
symmetric:

$$
\frac1{\sqrt n}\sum_iW_{ij}\Upsilon_i
\Longrightarrow
\Xi_\Upsilon
+\sum_\alpha
x_j^\alpha\mathbb E[\partial_{z^\alpha}\Upsilon].
$$

If a source itself depends on \(W\), that dependence must first be exposed as
an additional channel. The derivative in the response term is a total
derivative through all already registered deterministic responses.

This multichannel registry is the essential new object at the second step.

## 7.6 Status of the nonlinear two-step closure

A reusable formal program is now clear:

1. compute the forward Gaussian state;
2. peel the ordinary backward state;
3. peel the first tangent \(u,g\);
4. start \(\dot\delta\) at the readout and peel the differentiated backward
   pass from group 3 to group 1;
5. peel the correction-forward states \(\bar z,\bar h\) from group 1 to
   group 3;
6. evaluate the final Gram contraction.

At fixed derivative order, this uses finitely many Gaussian base channels and
fixed-dimensional Gaussian expectations. However, the maintained derivation
does not yet enumerate a provably complete nonlinear channel registry for
arbitrary depth, nor prove its joint convergence. Consequently,

$$
\boxed{
\mathbb E[G^{\ell,(2)}_{n,ab}]
=
G^\ell_{ab}
+\eta\,O(n^{-1})
+\eta^2(4C^\ell_{ab}+R^\ell_{ab})
+o(\eta^2)+o_n(1)
}
$$

is a **formal general nonlinear closure**, not yet a fully proved general
theorem. The second-step increment is

$$
\boxed{
\mathbb E[G^{\ell,(2)}_{n,ab}-G^{\ell,(1)}_{n,ab}]
=
\eta\,O(n^{-1})
+\eta^2(3C^\ell_{ab}+R^\ell_{ab})
+o(\eta^2)+o_n(1).
}
$$

Neither expression has a deterministic linear hidden-Gram term.

## 7.7 Deep-linear two-step audit

For \(\phi(z)=z\), the registry closes explicitly. Retain

$$
\kappa=\frac2B,
\qquad
\sigma=G^0y.
$$

The one-step coefficients are

$$
C^\ell_{ab}
=
(1,5,14)_\ell\,
\kappa^2\sigma_a\sigma_b.
$$

Gaussian Wick contractions of the relevant Wishart words give the correction

$$
\boxed{
R^1_{ab}=6\kappa^2\sigma_a\sigma_b,\qquad
R^2_{ab}=14\kappa^2\sigma_a\sigma_b,\qquad
R^3_{ab}=20\kappa^2\sigma_a\sigma_b.
}
$$

Therefore the cumulative two-step coefficients are

$$
\boxed{
(4C^\ell+R^\ell)_{ab}
=
(10,34,76)_\ell\,
\kappa^2\sigma_a\sigma_b,
}
$$

and the second-step increment coefficients are

$$
\boxed{
(3C^\ell+R^\ell)_{ab}
=
(9,29,62)_\ell\,
\kappa^2\sigma_a\sigma_b.
}
$$

This verifies the signs, the factors \(4\) and \(3\), and the retained
off-diagonal width patterns. It also separates two Euler steps from gradient
flow at time \(2\eta\), whose quadratic coefficient would be
\(4C^\ell+2R^\ell\).

# 8. Feature-learning interpretation

## 8.1 Initialization jets

For scaled gradient flow

$$
\dot\theta_n(\tau)
=
-P_n\nabla\mathcal R_n(\theta_n(\tau)),
$$

define

$$
\mathcal V_n
:=
-\bigl(P_n\nabla\mathcal R_n\bigr)\cdot\nabla.
$$

For a smooth scalar observable \(A_n\),

$$
\left.
\frac{d^r}{d\tau^r}
A_n(\theta_n(\tau))
\right|_{\tau=0}
=
\mathcal V_n^rA_n(\theta_n(0)).
$$

At fixed \(r\), repeated application of \(\mathcal V_n\) creates a finite sum
of scalar contractions of initialization derivatives of the network, loss,
and observable. Those contractions are precisely peeling inputs.

For a hidden feature kernel

$$
G^\ell_{n,ab}(\tau)
=
\frac1{n_\ell}\sum_i
h_i^\ell(x_a;\theta_\tau)
h_i^\ell(x_b;\theta_\tau),
$$

the intended chain is

$$
\begin{aligned}
\text{training derivative}
&\longrightarrow
\text{initialization contraction}
\\
&\longrightarrow
\text{peeling state}
\longrightarrow
\text{explicit Gaussian moments}.
\end{aligned}
$$

This is the main connection to feature learning: the local training trajectory
can, coefficient by coefficient, be expressed through deterministic Gaussian
calculations rather than width-sized random tensors.

## 8.2 What initialization jets do not prove

Fixed-order coefficients do not by themselves establish:

- interchange of time differentiation and the width limit;
- concentration of every coefficient;
- a nonzero Taylor radius uniform in width;
- recovery of finite-time training from the entire local jet;
- validity for a number of discrete steps growing as \(1/\eta\).

Those are analytic questions beyond the algebraic peeling calculus.

# 9. A precise theorem target

The strongest defensible present statement is a theorem schema.

> Fix batch size \(B\), derivative order \(R\), depth \(L\), and a Gaussian
> fully connected architecture whose hidden widths tend to infinity with
> fixed positive ratios. Let \(O_n\) be an \(O(1)\)-normalized admissible
> scalar contraction of the initialization jet of order at most \(R\).
> Assume sufficient activation smoothness and moments, deterministic
> convergence of forward empirical Grams, uniform integrability of retained
> states, and finite-state closure of the layerwise contraction rules. Then
> the leading large-width expectation of \(O_n\) is computable through
> \(L\) layer-local peeling transitions. Every transition coefficient is a
> finite linear combination of explicit batch-dimensional Gaussian
> expectations of scalar activations and their derivatives, evaluated at
> deterministic layerwise covariances. If a separate multi-copy peel proves
> vanishing variance, the same expression is the limit in probability.

This statement is conditional on finite-state closure and convergence. It is
not yet the finished mean-field peeling theorem.

## 9.1 The plausible novelty

Existing tensor-program methods already provide recursive semantics and
Gaussian limits for broad classes of wide-network programs. The plausible
distinct contribution of peeling is narrower and more syntactic:

- accept a contracted fixed-order derivative observable;
- compile it into a finite equality-partition and boundary-signature state;
- eliminate each layer by explicit conditional Wick-Stein rules;
- output a human-readable Gaussian normal form;
- expose the exact leading diagrams and every Onsager correction.

Thus the credible claim is not the first recursive Gaussian computation for
wide networks. It is a source-to-source calculus for explicit derivative
observables, with transparent power counting and potentially automatable
normal-form output.

# 10. Amendments learned from the executions

The case studies force the following changes to the original informal
program.

1. **Replace global Gaussianity by layerwise conditional Gaussianity.**
   Across layers, the unconditional law is generally a Gaussian mixture.

2. **Do not replace weight-activation dependence by pseudo-independence.**
   Use exact Wick-Stein partial matchings. Independence, when it appears in a
   limiting representative state, must be established through vanishing
   mixed covariances and a joint CLT.

3. **Peel the readout before hidden layers.** It controls parity, width, and
   the correct boundary state.

4. **Keep Stein-created lower-group factors.** A factor created in the
   current peel belongs to the layer where its activation was produced and
   must be delegated downward.

5. **Separate equality patterns before averaging.** Diagonal and
   row-distinct families can have different limits.

6. **Count widths globally.** Current-layer covariance powers, lower-layer
   free sums, optimizer factors, and observable normalization all enter the
   same degree.

7. **Do not infer irrelevance from zero one-copy mean.** Row-distinct fields
   can survive in a square and become leading Gaussian fluctuation channels.

8. **Perform exact conditional integration before deterministic Gram
   replacement.** Distinguished rows require leave-one-out control.

9. **Separate expectation from concentration.** A deterministic replacement
   inside later products needs a multi-copy proof.

10. **Register all channels sharing a matrix.** At higher training order,
    fresh fields are generally correlated. Their entire covariance block is
    part of the state.

11. **Do not differentiate a limiting cancellation.** A sequence whose mean
    tends to zero can have a directional derivative with a nonzero limit.

12. **Allow Gaussian dimension \(qB\), not always just \(B\).** Each primitive
    row moment uses a \(B\)-vector, but higher-order states can require several
    jointly generated vectors.

13. **Treat \(O(L)\) complexity as a theorem conclusion.** It requires a
    depth-uniform state bound, not merely a layerwise recipe.

14. **State regularity caveats.** ReLU needs weak derivatives, smoothing, or
    Gaussian boundary terms. Biases can have order-one Stein covariances and
    cannot be ignored.

# 11. Proof obligations for a complete theorem

A full proof should be divided into modules.

## 11.1 Algebraic compilation

Prove that every admissible fixed-order contracted jet expands into finitely
many scalar states with bounded derivative order, explicit equality
constraints, and a finite lower-boundary signature.

## 11.2 Exact layer elimination

Prove the generalized conditional Wick-Stein identity for the selected
regularity class and show that every current-group parameter can be removed
without leaving the state language.

## 11.3 Uniform moments and leave-one-out

Control all activation derivatives and retained contraction states uniformly
in width. Show that removing finitely many distinguished rows changes each
empirical covariance by a negligible amount at the requested order.

## 11.4 Joint conditional CLT

For every channel registry created by one peel, prove joint convergence of the
fresh Gaussian base fields and convergence of the full covariance block.
Nonlinear states are then explicit functions of those Gaussian bases; the
nonlinear states themselves need not be jointly Gaussian.

## 11.5 Global diagram degree

Prove a bookkeeping lemma that assigns each equality-partition diagram a
width degree preserved under local transitions, including all downstream
free-index effects.

## 11.6 Concentration

Repeat the calculus on two or more copies and show that every connected
cross-copy diagram is subleading whenever a deterministic limit is claimed.

## 11.7 Finite-state closure

At fixed \(B,R\), observable type, and asymptotic order, prove that the
boundary and channel state space is finite. To obtain a truly \(O(L)\)
algorithm, strengthen this to a state-size bound independent of depth.

# 12. Practical worksheet

For a new problem, the following worksheet prevents most mistakes.

## 12.1 Specify

- What is the raw parameter?
- What effective tensor enters the forward pass?
- What are the initialization variances?
- What optimizer factor multiplies each raw gradient?
- What scalar observable is being computed?
- Is the target its expectation, deterministic limit, or fluctuation?
- What width order is required?

## 12.2 Compile

- Expand only the highest active group.
- Write every matrix product with explicit indices.
- Record all width powers.
- Record every equality and inequality constraint.
- Mark the group of every remaining factor.

## 12.3 Peel

- Condition on lower groups.
- Split exact equality partitions.
- Apply every Wick and Stein branch.
- Differentiate the nonlinear factor explicitly.
- Insert the exact conditional covariance.
- Carry newly created lower activations downward.
- Count the complete diagram before discarding it.

## 12.4 Close

- Convert row averages into Gaussian moments.
- Justify empirical-to-deterministic covariance replacement.
- Register fresh Gaussian channels and all cross-covariances.
- Repeat for the next group.
- If using the result inside a product, prove concentration separately.

## 12.5 Audit

- Check parity in centered readouts.
- Check a linear activation specialization.
- Check a one-sample or diagonal batch case.
- Compare width degree against a direct tensor calculation.
- Verify that a zero limiting term was not differentiated away.

# 13. Consolidated formula sheet

For the audited three-hidden-layer network:

$$
\Pi^3=D^3,\qquad
\Pi^2=D^2D^3,\qquad
\Pi^1=D^1D^2D^3.
$$

The deterministic tangent kernel is

$$
K
=
G^3+G^2D^3+G^1D^2D^3+G^0D^1D^2D^3,
$$

with all products entrywise.

The one-step sample-loss coefficient is

$$
[\eta]\,\mathbb E[(f_a^+-y_a)^2]
=
-\frac4B y_a\sum_cK_{ac}y_c.
$$

The expected hidden-Gram linear coefficient is zero in the width limit:

$$
\lim_{n\to\infty}
[\eta]\,\mathbb E[G^{\ell,+}_{n,ab}]
=
0.
$$

Its first generic deterministic coefficient is

$$
C^\ell=V^\ell+S^\ell+(S^\ell)^\top,
$$

where \(V^\ell\) and \(S^\ell\) obey the explicit Gaussian recursions in
Section 6.

After two Euler steps,

$$
[\eta^2]\,\mathbb E[G^{\ell,(2)}_{n,ab}]
=
4C^\ell_{ab}+R^\ell_{ab},
$$

and for the second update alone,

$$
[\eta^2]\,
\mathbb E[G^{\ell,(2)}_{n,ab}-G^{\ell,(1)}_{n,ab}]
=
3C^\ell_{ab}+R^\ell_{ab}.
$$

In the deep-linear audit,

$$
C^\ell=(1,5,14)_\ell\,
\kappa^2\sigma\sigma^\top,
$$

$$
R^\ell=(6,14,20)_\ell\,
\kappa^2\sigma\sigma^\top,
$$

$$
4C^\ell+R^\ell
=(10,34,76)_\ell\,
\kappa^2\sigma\sigma^\top,
$$

and

$$
3C^\ell+R^\ell
=(9,29,62)_\ell\,
\kappa^2\sigma\sigma^\top.
$$

# 14. Source and status ledger

This report synthesizes three maintained sources in the local research
folder:

- the living mean-field peeling program, which contains the original raw
  proposal, the corrected conditional-Gaussian formulation, and the complete
  backward-kernel audit;
- the consolidated \(\mu\)P training case study, which contains the
  initialization, one-step, and two-step executions in one convention;
- the theorem-framing and Tensor Programs contrast report, which sharpens the
  admissible input class, output normal form, novelty claim, and open proof
  obligations.

The formulas labelled exact above are finite-width identities. The backward
kernel and one-step Gaussian recursions are audited mean-field conclusions
under the explicit assumptions stated in the maintained case study. The
general nonlinear two-step recursion is a formal finite-state schema; its
deep-linear specialization is explicitly verified. The all-observables
finite-state, depth-linear peeling theorem remains open.

# 15. Closing perspective

The peeling program is most useful when viewed neither as an informal
independence trick nor as a claim that all network states become Gaussian.
It is an exact conditional Gaussian elimination calculus followed by a
carefully ordered mean-field limit.

The backward kernel shows the simplest successful ladder structure. The
one-step hidden Gram shows why zero-mean off-diagonal families can survive as
fresh Gaussian fields. The two-step calculation shows why derivative order
forces state augmentation and a multichannel covariance registry. Together,
these examples locate both the strength of the method and the remaining
theorem gap.

The practical research objective is now crisp: define the admissible
contraction language, prove local Wick-Stein closure and global width-degree
control, construct a complete joint channel registry, and establish
depth-uniform finite-state closure. Achieving those pieces would turn the
working method into a reusable mean-field peeling theorem and an explicit
Gaussian compiler for initialization jets of feature-learning observables.
