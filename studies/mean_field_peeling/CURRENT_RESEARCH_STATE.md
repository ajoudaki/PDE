# Mean-Field Peeling: Theory, Algorithm, and Theorem Program

**Status:** Canonical maintained theory document  
**Detailed execution:**
[`MUP_TRAINING_CASE_STUDY.md`](MUP_TRAINING_CASE_STUDY.md)  
**Exact quadratic specialization:**
[`quadratic_compiler/`](quadratic_compiler/)
**Historical source:**
[`archive/ORIGINAL_NOTES_AND_NTK_SAMPLE.md`](archive/ORIGINAL_NOTES_AND_NTK_SAMPLE.md)  
**Last consolidated:** 2026-08-13

## 1. Purpose and status

Mean-field peeling is a layer-by-layer method for reducing a
width-normalized scalar contraction of neural-network derivatives to explicit
Gaussian expectations. One exposes the highest active layer, conditions on
all lower layers, integrates the current Gaussian weights exactly by Wick and
Stein identities, passes every lower-layer factor created by that integration
to the next layer, and repeats.

This is not an independence argument. A matrix can create both a
preactivation and backward or differentiated fields. Their dependence is
exactly what generates Stein, or Onsager, response terms. Some response terms
vanish after complete width counting; others survive and encode feature
learning.

Four claim levels are used throughout.

1. **Exact finite-width identity.** Ordinary differentiation, conditioning,
   Gaussian integration by parts, or Taylor expansion proves the statement
   before taking a width limit.
2. **Mean-field result under explicit assumptions.** The displayed limit
   follows from the peel provided the stated smoothness, moment,
   leave-finitely-many-out, joint-CLT, concentration, and uniform-integrability
   assumptions hold. These assumptions are named rather than hidden.
3. **Formal mean-field closure.** The differentiated state and its local
   Gaussian operations have been specified, but a complete joint convergence
   theorem for every registered channel has not been supplied.
4. **Open theorem program.** The broad Gaussian-normal-form and
   depth-linear finite-state claims remain targets, not established theorems.

There is now one important exact specialization. For the one-sample,
two-hidden-layer quadratic model, derivative monomials close under a finite
decorated-forest grammar. The resulting compiler and its exact order-eleven
certificates are described in Section 11. This proves a substantial
special-case peeling calculus; it does not upgrade the general theorem target.

For a fixed batch of size $B$, a primitive preactivation row is a
$B$-dimensional Gaussian vector. Higher-order states may require $q$ jointly
generated base vectors and therefore a Gaussian integral of total dimension
$qB$. The number $q$ is finite for each fixed finite construction and is
independent of width. A bound on $q$ independent of depth is an additional
open finite-state-closure problem.

## 2. Network, raw parameters, and scaling ledger

Fix a batch

$$
\{(x_a,y_a):a=1,\ldots,B\}.
$$

For a fully connected network, write the effective forward weights as

$$
A^\ell_{ij}=s_{\ell,n}\theta^\ell_{ij},
$$

where $\theta^\ell$ is the raw parameter optimized during training and
$s_{\ell,n}$ is its forward multiplier. The forward pass is

$$
z_i^\ell(a)
=
\sum_j A^\ell_{ij}h_j^{\ell-1}(a)
+\sigma_{b,\ell}b_i^\ell,
\qquad
h_i^\ell(a)=\phi_\ell(z_i^\ell(a)),
$$

with $h^0(a)=x_a$. Under fan-in Gaussian initialization,

$$
A^\ell_{ij}
\sim
N\left(0,\frac{\sigma_{w,\ell}^2}{n_{\ell-1}}\right).
$$

Before any peeling calculation, record:

- every width and limiting width ratio;
- each raw parameter and the corresponding effective forward tensor;
- every weight and bias variance;
- output dimension and readout normalization;
- the layerwise optimizer or μP metric factor;
- the observable normalization and desired asymptotic width order;
- whether the target is an expectation, a deterministic probability limit,
  or a fluctuation law.

No width power counting is meaningful until this ledger is fixed.

## 3. Exact layerwise conditional Gaussian law

Let

$$
\mathcal F_{\ell-1}
=
\sigma(A^1,b^1,\ldots,A^{\ell-1},b^{\ell-1}).
$$

Conditional on $\mathcal F_{\ell-1}$, the row blocks

$$
\bigl(A^\ell_{i,:},b_i^\ell,Z_i^\ell\bigr),
\qquad
Z_i^\ell=(z_i^\ell(1),\ldots,z_i^\ell(B)),
$$

are independent centered jointly Gaussian vectors across $i$. Exactly at
finite width,

$$
Q^\ell_{n,ab}
:=
\operatorname{Cov}
\left(z_i^\ell(a),z_i^\ell(b)\mid\mathcal F_{\ell-1}\right)
=
\frac{\sigma_{w,\ell}^2}{n_{\ell-1}}
\sum_jh_j^{\ell-1}(a)h_j^{\ell-1}(b)
+\sigma_{b,\ell}^2,
\tag{3.1}
$$

$$
\operatorname{Cov}(A^\ell_{ij},A^\ell_{i'j'})
=
\delta_{ii'}\delta_{jj'}
\frac{\sigma_{w,\ell}^2}{n_{\ell-1}},
\tag{3.2}
$$

and

$$
\operatorname{Cov}
\left(A^\ell_{ij},z_{i'}^\ell(a)\mid\mathcal F_{\ell-1}\right)
=
\delta_{ii'}
\frac{\sigma_{w,\ell}^2}{n_{\ell-1}}
h_j^{\ell-1}(a).
\tag{3.3}
$$

Equation (3.3) is the source of the Stein response. It contains a
lower-layer activation, so eliminating group $\ell$ creates boundary data for
group $\ell-1$.

Unconditionally, the covariance in (3.1) is random. Deep variables across
several layers therefore form a Gaussian mixture in general, not one global
joint Gaussian vector. Peeling relies on exact conditional Gaussianity one
layer at a time.

## 4. Deterministic forward state

Under the required law-of-large-numbers and moment assumptions,

$$
Q_n^\ell\longrightarrow Q^\ell.
$$

The deterministic recursion is

$$
Q^1_{ab}
=
\sigma_{w,1}^2\frac{x_a^\top x_b}{n_0}
+\sigma_{b,1}^2,
$$

and

$$
Q^{\ell+1}_{ab}
=
\sigma_{w,\ell+1}^2
\mathbb E_{Z\sim N(0,Q^\ell)}
[\phi_\ell(Z_a)\phi_\ell(Z_b)]
+\sigma_{b,\ell+1}^2.
\tag{4.1}
$$

Labels do not enter these initialization covariances. They enter through loss
derivatives and training-time vector fields.

## 5. Groups, explicit atoms, and admissible observables

Group $\ell$ contains:

- raw or effective layer-$\ell$ parameter coordinates and biases;
- preactivation coordinates $z_i^\ell(a)$;
- scalar functions of those coordinates, including
  $\phi_\ell,\phi_\ell',\phi_\ell'',\ldots$.

A backward error, Hessian-vector product, or training-time derivative is not
initially explicit. Chain rule, product rule, and Faà di Bruno expansion turn
each fixed-order derivative into a finite sum of products of explicit atoms.

The proposed admissible input language consists of scalar expressions
generated from:

- outputs and losses on the fixed batch;
- preactivations, activations, and hidden-Gram entries;
- parameter, input, or training-time derivatives of total order at most a
  fixed $R$;
- finite sums, products, and tensor contractions;

subject to the following structural conditions:

1. all width-growing neuron and parameter indices are eventually contracted;
2. every width normalization is declared;
3. the local expression schema is independent of width;
4. depth dependence is generated by repeated layer-local templates;
5. the expression is width-balanced under the declared scaling.

This definition is intentionally syntactic. “Any observable having a
mean-field limit” would be circular and too broad. A width-growing uncontracted
Hessian is not one scalar peeling state. Ratios, inverses, maxima, spectral
edges, and similar global nonlinear functions require additional
nondegeneracy or regularity arguments.

## 6. Scalar contraction normal form

After derivative expansion and scalarization, one term has the form

$$
T_n
=
c_n
\sum_{\boldsymbol\iota}
\mathbf 1\{\mathcal C(\boldsymbol\iota)\}
\prod_{r=1}^{R_W}A^{\ell_r}_{i_rj_r}
\prod_{s=1}^{R_Z}
\psi_s(z^{k_s}_{u_s}(a_s)).
\tag{6.1}
$$

The contraction state records:

- every neuron index and its layer;
- all fixed batch labels;
- exact equality and inequality constraints;
- the derivative order of every scalar function;
- all explicit width powers;
- every open lower-layer index passed to the next peel.

Once indices are exposed, every factor is scalar and may be reordered by
group. Recursive scalarization exposes only the current highest group rather
than expanding the whole depth at once.

The desired final output is a finite Gaussian-normal-form directed acyclic
graph. A Gaussian atom has the form

$$
\mathcal I_{\ell,F}
=
\int_{\mathbb R^d}F(g)\,N(0,K^\ell)(dg),
\tag{6.2}
$$

with the layer $\ell$, covariance $K^\ell$, dimension $d$, integrand $F$,
all activation derivatives, deterministic coefficients, and surviving
batch-index/equality contractions explicitly specified. The final output
contains no random weights, neuron-index sums, implicit backward vectors,
recursively named limit variables, or unevaluated Onsager terms.

## 7. Exact Wick--Stein elimination

### 7.1 One weight

If $(X,Z)$ is centered jointly Gaussian and $F$ is differentiable with
integrable derivative, then

$$
\mathbb E[XF(Z)]
=
\sum_\alpha
\operatorname{Cov}(X,Z_\alpha)
\mathbb E[\partial_\alpha F(Z)].
\tag{7.1}
$$

For a current-layer weight, conditional on the lower filtration,

$$
\mathbb E[A^\ell_{ij}F(Z_i^\ell)\mid\mathcal F_{\ell-1}]
=
\frac{\sigma_{w,\ell}^2}{n_{\ell-1}}
\sum_{a=1}^B h_j^{\ell-1}(a)
\mathbb E[\partial_{z_i^\ell(a)}F(Z_i^\ell)
\mid\mathcal F_{\ell-1}].
\tag{7.2}
$$

The explicit weight disappears, a derivative is added to the nonlinear
factor, and the covariance inserts a lower-layer activation. The latter must
remain explicit until its own group is peeled.

### 7.2 Two weights

For centered jointly Gaussian $X,Y,Z$,

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
\tag{7.3}
$$

The first line is the weight--weight Wick branch. The second is the double
Stein, or Onsager, branch. Neither may be discarded before global counting.

### 7.3 General partial matchings

Let $X_1,\ldots,X_r$ be explicit Gaussian parameter coordinates in the
current group and let $F(Z)$ contain all current preactivation functions.
Conditional on lower groups,

$$
\begin{aligned}
\mathbb E\left[\prod_{q=1}^rX_qF(Z)\right]
={}&
\sum_\pi
\left(
\prod_{\{q,t\}\in\pi}\operatorname{Cov}(X_q,X_t)
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
\tag{7.4}
$$

Here $\pi$ ranges over partial matchings of the weight occurrences and
$U(\pi)$ is the unmatched set. A matched pair is a weight--weight Wick
contraction. An unmatched occurrence attaches to a preactivation through
Stein's identity. Every attachment differentiates the top nonlinear factor
and inserts the corresponding lower-layer activation.

Complete matchings are sometimes called pseudo-independent branches; partial
matchings are Onsager branches. The phrase “independent copy plus correction”
is only a mnemonic. Equation (7.4) is the actual identity, and branch names do
not determine asymptotic size.

## 8. Equality partitions and global width degree

For top-row indices $i_1,\ldots,i_q$, split the sum by exact equality
partition:

$$
\sum_{i_1,\ldots,i_q}
=
\sum_{\pi\in\mathcal P_q}
\sum_{\ker(\boldsymbol i)=\pi}.
\tag{8.1}
$$

A partition with $|\pi|$ distinct blocks has

$$
n_\ell^{|\pi|}(1+O(n_\ell^{-1}))
$$

assignments before other constraints are imposed. For one row block, define

$$
\Gamma_\ell
[(a_1,\psi_1),\ldots,(a_s,\psi_s);Q]
:=
\mathbb E_{Z\sim N(0,Q)}
\left[\prod_{r=1}^s\psi_r(Z_{a_r})\right].
\tag{8.2}
$$

Different row blocks yield products of such moments, subject to any joint
base-channel structure retained by the state.

For iid rows $Z_i$, the elementary two-index example is

$$
\frac1{n^2}\sum_{i,j}F(Z_i)G(Z_j)
=
\frac1{n^2}\sum_{i\ne j}F(Z_i)G(Z_j)
+\frac1{n^2}\sum_iF(Z_i)G(Z_i).
\tag{8.3}
$$

The off-diagonal partition has two free row blocks and converges to
$\mathbb E[F(Z)]\mathbb E[G(Z)]$. The diagonal partition has one free row
block and is lower by $n^{-1}$ under this normalization. If the observable
instead contains $n^{-1}\sum_iF(Z_i)G(Z_i)$, that diagonal joint moment is
leading. This is the smallest example of why equality patterns and
normalization must be considered together.

The global width degree includes:

- one positive width power for each free neuron-index block;
- negative powers from weight covariances and weight--preactivation
  attachments;
- the observable normalization;
- raw-to-effective parameter multipliers;
- optimizer or μP metric factors;
- every lower-layer sum created by a Stein attachment.

A branch may be dropped only after its full lower-layer boundary signature is
known. A locally subleading branch can create another lower-layer sum and
recover its order. A locally comparable branch can later be forced onto a
diagonal and lose an order. Likewise, an off-diagonal family with zero
one-copy mean can survive in a two-copy calculation as a fresh Gaussian
fluctuation field.

## 9. Deterministic covariance replacement

Exact conditional integration initially produces Gaussian moments at the
lower-random empirical covariance $Q_n^\ell$. Only after distinguished rows
and equality patterns have been exposed may one use

$$
Q_n^\ell\longrightarrow Q^\ell
$$

and conclude, under continuity and uniform integrability,

$$
\Gamma_\ell[\cdots;Q_n^\ell]
\longrightarrow
\Gamma_\ell[\cdots;Q^\ell].
\tag{9.1}
$$

If a distinguished row also enters $Q_n^\ell$, a quantitative proof first
uses a leave-one-out or leave-finitely-many-out covariance. Removing finitely
many rows changes the covariance by the relevant small width order and makes
the remaining covariance independent of those distinguished rows.

For a centered or fluctuation-amplified target, the zeroth-order replacement
can erase the leading term. One must then expand in $Q_n^\ell-Q^\ell$.
Price's identity keeps this expansion inside the same Gaussian derivative
algebra:

$$
D\,\mathbb E_{Z\sim N(0,Q)}[F(Z)][H]
=
\frac12\sum_{a,b}H_{ab}
\mathbb E[\partial_{ab}F(Z)],
\tag{9.2}
$$

with the usual symmetric-covariance convention.

## 10. The peeling algorithm

### 10.1 Inputs

Specify the architecture, widths, activations, raw/effective parameter
scalings, output and bias normalization, optimizer metric, fixed batch,
scalar observable, maximum derivative order, requested width order, and
convergence mode.

### 10.2 One maximal-layer elimination

1. Expand derivative rules only far enough to expose the highest active
   group.
2. Scalarize all contractions involving that group.
3. Record exact width powers, equality constraints, and open lower-layer
   indices.
4. Reorder scalar atoms by group and select the highest active group $p$.
5. Condition on $\mathcal F_{p-1}$.
6. Split top-row indices into compatible exact equality partitions.
7. Apply (7.4) until no explicit group-$p$ Gaussian parameter remains.
8. Expand every derivative created on a nonlinear factor.
9. Substitute the exact conditional covariances.
10. Resolve Kronecker deltas and update the lower-layer boundary state.
11. Count widths globally, including every downstream sum.
12. Convert surviving top-row functions to Gaussian row moments at the
    empirical covariance $Q_n^p$.
13. Replace $Q_n^p$ by $Q^p$, or retain the covariance fluctuation required by
    the target.
14. Canonicalize and merge algebraically identical lower states.
15. Repeat at group $p-1$.
16. At layer zero, evaluate deterministic input and label contractions.

Exact conditional elimination and deterministic mean-field replacement are
separate steps. An index may be summed during group $p$ only when none of its
remaining occurrences belongs to a lower group.

### 10.3 Convergence pass

If a deterministic limit for a typical initialization is claimed, repeat the
calculus on the square, covariance, or relevant cumulants. A one-copy
expectation calculation does not prove concentration.

### 10.4 Recursive-state form

If the boundary signatures close on a finite state family $\mathcal S$, one
peel has the form

$$
V_p(s)
=
\sum_{s'\in\mathcal S}
T_p(s,s';Q^p)V_{p-1}(s'),
\tag{10.1}
$$

and hence

$$
V_L=T_L(Q^L)\cdots T_1(Q^1)V_0.
\tag{10.2}
$$

The conservative statement is that maximal-layer elimination terminates
after at most $L$ layer stages. An $O(L)$-size shared DAG additionally
requires a state-space bound independent of depth at fixed batch size,
derivative order, step count, and observable schema. That finite-state
strengthening remains open in general.

## 11. Exact quadratic decorated-forest specialization

### 11.1 Model and scope

At activation scale $\gamma=1$, the one-sample, two-hidden-layer quadratic model collapses to

$$
z_i=\frac1{\sqrt n}\sum_{j=1}^nW_{ij}u_j^2,
\qquad
f_n=\frac1n\sum_{i=1}^na_i z_i^2
=\frac1{n^2}\sum_{i,j,k}a_iW_{ij}W_{ik}u_j^2u_k^2,
$$

with all $a_i,W_{ij},u_j$ independent standard Gaussians. Feature-ascent differentiation of an observable $A$ is

$$
D_nA=n\langle\nabla f_n,\nabla A\rangle,
$$

where the gradient includes every $a,W,u$ coordinate. For fixed $k$,

$$
J_k=\lim_{n\to\infty}\mathbb E[D_n^kf_n].
$$

If $F$ denotes the formal feature jet, then $F^{(k)}(0)=J_k$. The derivative order is fixed before $n\to\infty$; no uniform-in-$k$ bound, positive-time trajectory, or convergence of the formal series follows. The readout flip and time reversal give $J_{2r}=0$.

### 11.2 Exact scalar graph grammar

Every scalar monomial generated by repeated differentiation is a decorated bipartite forest:

- a row vertex stores a row index and the exponent of $a_i$;
- a column vertex stores a column index and half the exponent of $u_j$;
- an edge is one occurrence of $W_{ij}$.

The derivation has exactly three local rewrites.

1. An $a$-hit adds the two weight edges contributed by $z_i^2$, with the current $a$-multiplicity.
2. A hit on $u_j^{2p}$ adds the new row/column gadget with coefficient $8p$.
3. A $W_{ij}$-hit has coefficient $2$, deletes that bridge, changes its endpoint decorations, and adds the fresh edge prescribed by the vector field.

The first two preserve connectedness. A weight hit splits a tree into two trees. If $k-1$ derivatives remain, the exact Leibniz contribution is

$$
2\sum_{q=0}^{k-1}\binom{k-1}{q}A_q(T_1)A_{k-1-q}(T_2).
$$

The sector-graded recurrence also records the number $w$ of weight hits. At total derivative order $k$, the number of Wick covariance pairs is

$$
P=k+1-w.
$$

### 11.3 Leading-width factorization theorem

Take a generated normalized forest with $r$ original components and $2P$ weight edges. A Wick pairing gives a quotient covariance graph with $P$ edges. If it has $V$ vertices, $c$ components, and cycle rank $\beta$, then

$$
V=P+c-\beta.
$$

The state normalization makes the contraction leading exactly when $V=P+r$. Pairing can only merge original components, so $c\le r$, and $\beta\ge0$. Therefore survival requires

$$
c=r,\qquad\beta=0.
$$

No leading covariance pair joins two original components, every quotient component is a tree, and the leading expectation factors across the original components. This exact result is scoped to the generated quadratic forest grammar and its normalization; it is not a general independence principle.

### 11.4 Accepted exact coefficients

The accepted computational certificates are

$$
\begin{aligned}
F'(0)&=111,\\
F^{(3)}(0)&=1\,685\,184,\\
F^{(5)}(0)&=77\,400\,633\,120,\\
F^{(7)}(0)&=7\,315\,868\,433\,079\,296,\\
F^{(9)}(0)&=1\,181\,161\,141\,825\,400\,561\,664,\\
F^{(11)}(0)&=291\,982\,832\,387\,585\,872\,335\,470\,592.
\end{aligned}
$$

The order-eleven number is the exact sum of all twelve Wick-pair sectors. The audit combines a transparent Python prototype, direct pairings at low order, exhaustive differentiated-forest expansion, compressed connected recursion, and a second equality-partition evaluator. Every accepted higher-order route first reproduced all ten order-nine sectors exactly. Order-eleven sectors $P=1,\ldots,9$ were evaluated from exhaustive exports with checked 512-bit arithmetic; $P=10,11,12$ were separately certified by the high-sector machinery. A conservative bound needs only 275 bits through order thirteen, so overflow would throw rather than wrap.

These are exact integer outputs of audited computer algebra under the proved special-case reduction, not hand enumerations or formally verified software. In particular, the order-eleven $P=9$ sector has one complete checked route but has not been redundantly recomputed by the newer connected-sector engine. Full provenance is in [the D11 audit](quadratic_compiler/D11_LOWER_SECTOR_AUDIT.md) and [sector-engine audit](quadratic_compiler/SECTOR_ENGINE.md).

### 11.5 Order-thirteen and acceleration audits

The complete $F^{(13)}(0)$ is unknown. Exact positive-subsum calculations give monotone lower bounds, culminating at

$$
50\,393\,647\,763\,255\,899\,049\,472\,742\,772\,736
$$

for component-edge cap fourteen. This is only a lower bound. In the maximal $P=14$ sector, discovery found 465,075 recurrence states and 325,190 base trees; only the first 704 base contractions completed, so no sector subtotal was certified. See [the D13 audit](quadratic_compiler/D13_ATTEMPT.md).

Several accelerations were audited:

- approximate first-pair and adjacent-pair modes retain positive sub-sums but are not exact checkpoints;
- the GF(2) matroid shortcut is valid only in the no-weight-hit, even-row, tight-nullity case; an explicit decorated-tree counterexample invalidates its unrestricted rank gate;
- a singleton-row shortcut omitted even-$a$ parity, so its reported subtotal and timing are retracted;
- prefixwise factor-nine two-hit bounds are exactly false, and an all-order version would contradict the factorial lower bound; no special order-eleven upper bound was proved;
- finite-width formal-jet simulation is a numerical pilot, not an exact mean-field certificate.

The restricted proofs, counterexamples, and retractions live next to the compiler. They illustrate a central MFP rule: a shortcut earns only the scope of its proof, even after passing extensive low-order regression gates.

### 11.6 What this does and does not establish

The compiler establishes full scalarization, exact derivative rewrites, leading-width Wick selection, equality-identification bookkeeping, component factorization, canonical-state memoization, and exact integer evaluation for this special model.

It does not cover arbitrary depth or batch size, general smooth activations, conditional weight--activation Stein attachments, random empirical-covariance replacement, arbitrary biases or readouts, general muP optimizer metrics, concentration, fluctuation laws, or depth-independent state closure. It is an exact special-case realization and regression laboratory, not a proof of the full Mean-Field Derivative Peeling Theorem.

## 12. Backward-kernel laboratory: what the first execution establishes

The complete fixed-network calculation is in the
[case study](MUP_TRAINING_CASE_STUDY.md). Its role in the theory is to expose
the simplest nontrivial state transition.

For a centered $1/n$ readout and three hidden layers, define normalized
backward variables $\delta_i^\ell(a)$ and empirical kernels

$$
\Pi^\ell_{n,ab}
=
\frac1n\sum_i\delta_i^\ell(a)\delta_i^\ell(b).
$$

If

$$
D^\ell_{ab}
=
\mathbb E[
\phi'(Z_a^\ell)\phi'(Z_b^\ell)],
\qquad
Z^\ell\sim N(0,G^{\ell-1}),
$$

the fully enumerated expectation peel gives

$$
\Pi^3=D^3,
\qquad
\Pi^2=D^2\odot D^3,
\qquad
\Pi^1=D^1\odot D^2\odot D^3.
\tag{11.1}
$$

The direct Wick contractions form one ladder through the two backward paths.
All fixed-three-layer Stein branches are retained until their equality
patterns and downstream sums are counted; their orders are explicitly shown
to be lower than the ladder in this expectation. This is an executed
expectation calculation, not a universal rule that Onsager branches vanish.

The arbitrary-fixed-depth product recursion is a natural one-state extension
of this ladder and is recorded in the case-study appendix with the general
readout scaling. A complete all-depth diagram induction and the four-path
concentration enumeration remain proof obligations. In particular, the
statement

$$
\operatorname{Var}(\Pi^\ell_{n,ab})=O(n^{-1})
$$

is the expected concentration conclusion under standard fixed-depth moment
conditions, but it is not proved by the displayed one-copy calculation.

The subsequent training execution demonstrates a different outcome. A
row-distinct family with zero one-copy mean survives after two copies are
formed and becomes a leading fresh Gaussian field in the quadratic
hidden-Gram coefficient. Thus “off diagonal” and “Onsager” are structural
labels, not asymptotic verdicts.

## 13. Feature-learning jets

### 13.1 Gradient-flow derivatives

Let the scaled gradient flow be

$$
\dot\theta_n(\tau)
=
-P_n\nabla\mathcal R_n(\theta_n(\tau)),
$$

and define the differential operator

$$
\mathcal V_n
:=
-\bigl(P_n\nabla\mathcal R_n\bigr)\cdot\nabla.
$$

For a smooth scalar observable $A_n$,

$$
\left.
\frac{d^r}{d\tau^r}A_n(\theta_n(\tau))
\right|_{\tau=0}
=
\mathcal V_n^rA_n(\theta_n(0)).
\tag{13.1}
$$

At fixed $r$, repeated application of $\mathcal V_n$ creates a finite sum of
scalar contractions of initialization derivatives of the observable, network,
and loss. Those contractions are peeling inputs.

For a hidden activation Gram,

$$
G^\ell_{n,ab}(\tau)
=
\frac1{n_\ell}\sum_i
h_i^\ell(x_a;\theta_\tau)
h_i^\ell(x_b;\theta_\tau),
$$

the intended chain is

$$
\text{training derivative}
\longrightarrow
\text{initialization contraction}
\longrightarrow
\text{peeling state}
\longrightarrow
\text{explicit Gaussian normal form}.
\tag{13.2}
$$

### 13.2 Discrete gradient descent

Fix a number $s$ of gradient-descent steps and a Taylor order $p$. For sample
$a$, let $\mathcal L_a^{(s)}(\eta)$ be the loss after $s$ steps, and define

$$
G_{ab}^{\ell,(s)}(\eta)
=
\frac1n
\left\langle
h_a^{\ell,(s)}(\eta),
h_b^{\ell,(s)}(\eta)
\right\rangle.
$$

For fixed $k\le p$, the coefficients

$$
[\eta^k]\,\mathbb E[\mathcal L_a^{(s)}(\eta)]
$$

and

$$
[\eta^k]\,\mathbb E[G_{ab}^{\ell,(s)}(\eta)]
$$

are fixed-order initialization derivative observables once their
admissibility and scaling are verified. The finite collection through order
$p$ is the **order-$p$ feature-learning jet**.

The case study computes the one-step loss coefficient, the first nontrivial
hidden-Gram coefficient, and the exact two-Euler-step decomposition in one
fixed μP convention. It also shows why a limiting cancellation may not be
differentiated as an identity: although the expected finite-width linear Gram
coefficient tends to zero, its directional derivative contributes at the next
order.

### 13.3 What a jet does not prove

Fixed-order initialization coefficients do not by themselves establish:

- interchange of width limits with time differentiation;
- concentration of every coefficient;
- a nonzero Taylor radius uniform in width;
- reconstruction of positive-time training from the local jet;
- validity for a number of steps growing like $1/\eta$;
- arbitrary or width-dependent training times.

These are separate analytic questions.

## 14. Target theorem and its strengthenings

### 14.1 Conservative target

The first theorem should be formulated for equal-width fully connected MLPs,
fixed batch size $B$, fixed depth $L$, fixed derivative order, and a fixed
number of training steps when updates are included. Fixed positive width
ratios and other architectures are planned extensions. Assume enough
polynomially controlled activation derivatives for every state actually
generated by the peel.

> **Target Mean-Field Derivative Peeling Theorem.** For every admissible
> scalar derivative observable $O_n$, there is a deterministic syntactic
> transformation $\operatorname{Peel}$ that recursively eliminates the
> maximal remaining layer group. Each elimination replaces that group by a
> finite sum of explicitly specified Gaussian-integral coefficients
> multiplying admissible lower-group states. The transformation terminates
> after at most $L$ maximal-layer eliminations and emits a finite Gaussian
> normal-form DAG. Under the stated regularity, moment, leave-out, and
> uniform-integrability hypotheses,
> $$
> \lim_{n\to\infty}\mathbb E_{\theta_0}[O_n]
> =
> \operatorname{Eval}(\operatorname{Peel}(O_n)).
> $$
> Every integrand, covariance, dimension, coefficient, activation derivative,
> and equality pattern in the output is constructed from the network, fixed
> data, and observable syntax.

This is a target statement. Its hypotheses and closure claims have not yet
been proved for the entire proposed grammar.

### 14.2 Finite-state strengthening

The strongest useful extension would show that, for fixed $B$, derivative
order $R$, training-step count, and observable schema $O$, the boundary
signatures close on state types whose number is independent of width and
depth. After common-state sharing, the normal-form DAG would then have at most

$$
C_{B,R,O}L
$$

nodes, and every Gaussian atom would have dimension at most

$$
d_{B,R,O},
$$

where both effective constants are independent of width and depth. They may
grow combinatorially or exponentially with derivative order and step count;
no polynomial bound is currently claimed.

### 14.3 Possible batch-dimensional factorization

A stronger corollary would reduce each connected Gaussian atom to one
$B$-dimensional layer-preactivation integral, with multiple row components
factoring into products. The current examples motivate this in simple states,
but no general equality-partition factorization theorem has been proved. The
safe target therefore uses $d_{B,R,O}$ rather than asserting dimension $B$.

## 15. Claim ladder and relation to Tensor Programs

The proposed contribution must be separated from established prior work.

- Deterministic limits of normalized wide-network averages are broadly
  established and are not the novelty claim.
- Tensor Programs gives recursive limiting coordinate semantics and moment
  expectations for broad finite tensor computations, including μP
  feature-learning limits.
- Recursive first- and higher-derivative kernel analyses also have prior art.
- A mechanical compiler from a specified contracted derivative grammar to a
  completely eliminated Gaussian normal form is an open target claim.
- Termination after maximal-layer eliminations, depth-independent finite-state
  closure, and a linear-size shared DAG are progressively stronger open
  targets.
- Exactly $B$-dimensional atoms and finite-time dynamics are not established.

### 15.1 What recursive Tensor Program semantics already provides

For a coordinatewise operation

$$
x_i=\phi(y_i^1,\ldots,y_i^k),
$$

the limiting coordinate variable is recursively represented as

$$
Z^x=\phi(Z^{y^1},\ldots,Z^{y^k}).
$$

For a normalized average

$$
q_n=\frac1n\sum_i\psi(x_i^1,\ldots,x_i^k),
$$

the limiting scalar is

$$
q_n\longrightarrow
\mathbb E[\psi(Z^{x^1},\ldots,Z^{x^k})].
$$

When a Gaussian matrix $W$ is reused, Tensor Programs decomposes the limiting
coordinate schematically as

$$
Z^{Wx}=\widehat Z^{Wx}+\dot Z^{Wx},
\tag{15.1}
$$

where the fresh variables generated by the same matrix are jointly Gaussian,

$$
\operatorname{Cov}
(\widehat Z^{Wx},\widehat Z^{Wy})
=
\sigma_W^2\mathbb E[Z^xZ^y],
\tag{15.2}
$$

and a transpose reuse creates an Onsager response of the schematic form

$$
\dot Z^{Wx}
=
\sigma_W^2\sum_a Z^{y_a}
\mathbb E\left[
\frac{\partial Z^x}
{\partial\widehat Z^{W^\top y_a}}
\right].
\tag{15.3}
$$

These are constructive semantics, not an existence-only theorem.

### 15.2 Intended distinction

Tensor Programs begins with a straight-line tensor computation. A contracted
higher derivative must first be differentiated, normalized, compiled into
that program language, and checked against the master-theorem hypotheses.
Its final answer may retain recursively named nonlinear limit variables and
symbolic Onsager responses.

For any particular finite program, one may in principle continue unwinding
those recursive variables. If all fresh Gaussian innovations required by the
program are collected into a finite vector

$$
G\sim\mathcal N(0,\Sigma_G),
$$

then the recursively defined limit variables can be represented as a
deterministic measurable transformation

$$
(Z^1,\ldots,Z^m)=F(G).
$$

Consequently, whenever the required integrability holds,

$$
\mathbb E\,\Psi(Z^1,\ldots,Z^m)
=
\int \Psi(F(g))\,\mathcal N(0,\Sigma_G)(dg).
$$

This observation does not by itself provide the proposed peeling normal form.
The map $F$ may still contain a recursively nested history of nonlinear and
Onsager operations, and mechanically unwinding all symbolic responses can
cause a large expression-size blowup. Thus *recursive Gaussian semantics* and
an *explicit, normalized Gaussian-integral representation with a controlled
finite state* are different output contracts.

Mean-field derivative peeling seeks a narrower source-to-source result. It
begins with contracted derivative syntax, executes every Wick and Stein
branch, enumerates equality partitions, performs width counting, and emits a
normal form containing only deterministic algebra and fully specified
Gaussian integrals. On their common domain, the intended validation identity
is

$$
\operatorname{Peel}(O)
=
\operatorname{UnrollTP}
\bigl(\operatorname{CompileDerivative}(O)\bigr).
\tag{15.4}
$$

Equation (15.4) is itself a proposed equivalence theorem, not an assumption.
The defensible positioning is therefore a specialized explicit normal-form
compiler, not a replacement for Tensor Programs and not the first recursive
Gaussian semantics for wide networks.

## 16. Amendments forced by the executions

The audited examples require the following maintained form of the program.

1. Use layerwise conditional Gaussianity, never an unconditional global
   Gaussian law across layers.
2. Replace pseudo-independence language by exact Wick--Stein partial
   matchings. Any limiting independence must follow from a joint law and
   vanishing mixed covariances.
3. Peel the readout before hidden groups; it fixes parity, scale, and the
   hidden boundary state.
4. Retain every lower-group factor created by Stein differentiation.
5. Split exact equality patterns before rowwise averaging or independence is
   used.
6. Count widths globally, including optimizer factors and downstream sums.
7. Do not discard an off-diagonal family merely because its one-copy mean is
   zero; it may survive in a square as a fresh field.
8. Perform exact conditional integration before deterministic Gram
   replacement; use leave-finitely-many-out when distinguished rows enter the
   empirical Gram.
9. Treat an exact subleading expansion separately from a leading mean-field
   replacement. Gram fluctuations can modify a displayed $1/n$ coefficient.
10. Separate expectation calculations from concentration or fluctuation
    theorems.
11. Register all channels generated through the same matrix and retain their
    complete covariance block.
12. Do not differentiate a limiting cancellation as though it were an exact
    finite-width identity.
13. Permit a finite Gaussian dimension $qB$ or $d_{B,R,O}$ at higher order;
    a single $B$-vector is not automatic.
14. Treat $O(L)$ formula size as a theorem conclusion requiring
    depth-uniform state closure.
15. Fix depth, batch size, derivative order, and step count before the width
    limit; growing-depth regimes require new uniform estimates.
16. Handle a scalar output separately because it has no neuron-row
    law-of-large-numbers factor.
17. Allow the activation derivative order generated by the peel to exceed the
    nominal derivative order of the input observable.
18. Track readout conventions explicitly. A noncentered readout may require
    backward first-moment/off-diagonal states; a zero readout may make the
    initialization backward kernel vanish; an $n^{-1/2}$ readout retains a
    random Gaussian-process output whereas an $n^{-1}$ centered readout tends
    to zero.
19. Biases require their own Stein branches; their bias--preactivation
    covariance can be order one.
20. ReLU requires weak derivatives, smoothing, or Gaussian boundary terms;
    pointwise $C^r$ formulas do not apply directly.

## 17. Required nonclaims

The current program does not prove:

- convergence of a learning-rate or time Taylor series;
- complete positive-time training dynamics;
- arbitrary or width-dependent training times;
- a uniform-in-depth probability limit;
- elementary closed forms for general activations;
- polynomial complexity in derivative order or training-step count;
- self-averaging of every admissible observable;
- general architectural universality;
- exactly $B$-dimensional integration without a factorization theorem.

Expectation-level exactness and sample-level determinism are separate claims.

## 18. Proof obligations

A complete theorem should be divided into the following modules.

1. **Observable grammar and algebraic compilation.** Define the contracted
   derivative language noncircularly and prove that chain, product, and Faà di
   Bruno expansion produce finitely many scalar states.
2. **Derivative closure and Stein termination.** Prove that every local
   elimination remains inside a declared state language and terminates without
   uncontrolled activation derivative order.
3. **Exact layer elimination.** Establish (7.4) for the chosen regularity
   class, including weights, biases, rows, and batch coordinates.
4. **Equality-partition completeness.** Enumerate every compatible pattern
   and prove that no locally subleading branch can recover order through an
   omitted lower contraction.
5. **Invariant global width degree.** Formalize width valuation under every
   transition, including optimizer and raw/effective multipliers.
6. **Uniform moments and leave-out estimates.** Bound all retained states and
   justify removal of finitely many distinguished rows.
7. **Joint conditional CLT.** Prove joint convergence of every registered
   fresh Gaussian base field and its entire covariance block. Nonlinear states
   are explicit functions of those bases; they need not themselves be jointly
   Gaussian.
8. **Covariance replacement and fluctuations.** Justify leading replacement
   and Price expansions at subleading orders.
9. **Multi-copy concentration.** Show that connected cross-copy diagrams are
   subleading whenever a deterministic limit is claimed.
10. **Finite-state and depth-uniform closure.** Classify boundary signatures
    and prove the state-size bound needed for a linear-depth DAG.
11. **Complexity and Gaussian dimension.** State effective dependence on
    $B,R$, step count, and observable schema, and determine whether the
    single-$B$-vector factorization is valid.
12. **Nonsmooth activations and architectural extensions.** Treat weak
    derivatives, residual connections, unequal widths, and biases separately.
13. **Tensor Programs equivalence.** Prove (15.4) on the overlap class as a
    validation theorem.
14. **Generalize the forest factorization.** Determine which parts of the
    quadratic quotient-forest theorem survive for the full conditional
    Wick--Stein boundary language, including nonlinear response attachments.

The decisive unresolved step is depth-uniform finite-state closure. Without
it, peeling is an explicit layerwise elimination recipe but not yet the
claimed $O(L)$ dynamic program.

## 19. Practical worksheet

### 19.1 Specify

- What is the raw parameter and what effective tensor enters the forward pass?
- What are the initialization variances and optimizer factors?
- What scalar observable and normalization are used?
- Is the target an expectation, deterministic limit, or fluctuation?
- What width order is requested?
- Which readout, bias, smoothness, and order-of-limits assumptions apply?

### 19.2 Compile

- Expand only the highest active group.
- Write every current tensor product with explicit indices.
- Record width powers, equality constraints, and the group of every factor.
- Retain all open lower-layer boundary indices.

### 19.3 Peel

- Condition on lower groups.
- Split exact equality partitions.
- Execute every Wick and Stein branch.
- Differentiate nonlinear factors explicitly.
- Insert exact conditional covariances.
- Carry newly created lower activations downward.
- Count the complete diagram before discarding it.

### 19.4 Close

- Convert row averages into Gaussian moments.
- Justify empirical-to-deterministic covariance replacement.
- Register fresh Gaussian channels and all cross-covariances.
- Repeat on the next group.
- If the result enters another random product, prove the required multi-copy
  convergence separately.

### 19.5 Audit

- Check centered-readout parity.
- Check a linear-activation specialization.
- Check a one-sample or batch-diagonal case.
- Compare width degree with a direct indexed calculation.
- Verify that no limiting zero was differentiated away.
- Verify whether each claim concerns expectation, convergence in probability,
  $L^2$, or a fluctuation law.

## 20. Terminology, framing, and literature anchors

Recommended vocabulary is:

- **method:** mean-field derivative peeling, shortened to mean-field peeling;
- **target theorem:** Mean-Field Derivative Peeling Theorem;
- **output:** Gaussian normal form;
- **local training data:** feature-learning jet;
- **algorithmic representation:** peeling-state DAG.

The acronym “MFP” is avoided because it is naturally read as mean-field
parameterization. A suitable paper title is:

> **Mean-Field Peeling: Explicit Gaussian Normal Forms for Feature-Learning
> Jets**

If “jet” is undesirable, “Taylor coefficients” is the direct replacement.
Other retained editorial alternatives are:

1. **Mean-Field Derivative Peeling: An Explicit Gaussian Calculus for Local
   Feature Learning**;
2. **Peeling Wide Neural Networks: Explicit Gaussian Recursions for
   Feature-Learning Derivatives**;
3. **From Derivatives to Gaussian Integrals: Mean-Field Peeling in
   Feature-Learning Networks**;
4. **Feature-Learning Jets at Infinite Width: A Mean-Field Peeling
   Calculus**.

“Gaussian Normal-Form Peeling Theorem” and “Layerwise Gaussian Elimination
Theorem for Derivative Observables” are descriptive alternatives for the core
theorem. “Feature-Learning Jet Representation Theorem” is better reserved for
the training corollary.

The literature comparison is an evidence-based positioning assessment, not a
certification of novelty. Primary anchors are:

- Greg Yang and Edward J. Hu,
  [Tensor Programs IV: Feature Learning in Infinite-Width Neural Networks](https://proceedings.mlr.press/v139/yang21c.html),
  ICML 2021, together with its
  [supplementary material](https://proceedings.mlr.press/v139/yang21c/yang21c-supp.pdf),
  especially the Master Theorem and Algorithm 1;
- Greg Yang,
  [Tensor Programs II: Neural Tangent Kernel for Any Architecture](https://arxiv.org/abs/2006.14548),
  2020;
- Greg Yang,
  [Tensor Programs III: Neural Matrix Laws](https://arxiv.org/abs/2009.10685),
  2020;
- Jiaoyang Huang and Horng-Tzer Yau,
  [Dynamics of Deep Neural Networks and Neural Tangent Hierarchy](https://proceedings.mlr.press/v119/huang20l.html),
  ICML 2020;
- Ethan Dyer and Guy Gur-Ari,
  [Asymptotics of Wide Networks from Feynman Diagrams](https://arxiv.org/abs/1909.11304),
  2019;
- Max Guillen, Philipp Misof, and Jan E. Gerken,
  [Finite-Width Neural Tangent Kernels from Feynman Diagrams](https://arxiv.org/abs/2508.11522),
  ICML 2026.

## 21. Current authoritative positioning

Mean-field peeling is a proposed explicit normal-form calculus for fixed-order
contracted derivative observables in wide mean-field MLPs. Tensor Programs
already supplies constructive recursive semantics for broad finite neural
computations, including μP feature-learning limits. The prospective
distinction is that peeling begins from derivative syntax and performs all
layerwise Gaussian elimination, Stein correction, Wick contraction,
equality-pattern enumeration, and width power counting explicitly, with the
goal of a finite Gaussian-integral DAG and a finite-state depth recursion.

There are two complementary core laboratories and three bounded
parameter-extension campaigns. The fixed three-hidden-layer backward and
training calculations expose conditional Stein corrections and lower-layer
boundary transport. The canonical one-sample quadratic compiler proves an
exact decorated-forest specialization and supplies accepted integer
coefficients through derivative order eleven. Its isolated campaigns retain
the same basic grammar while varying a relative block metric and hidden
observable, a two-input symmetry channel, and a shifted first-hidden
activation. They provide exact finite-order continuum tests, not a generic
compiler theorem. The general nonlinear two-step closure remains formal, its
deep-linear specialization is audited, and the finite-state theorem for the
full proposed admissible grammar remains open. None of the exact
specializations should be mistaken for that general theorem.
