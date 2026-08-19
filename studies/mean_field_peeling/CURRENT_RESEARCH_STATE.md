# Mean-Field Peeling: Theory, Algorithm, and Theorem Program

**Status:** Canonical maintained theory document  
**Detailed execution:**
[`MUP_TRAINING_CASE_STUDY.md`](MUP_TRAINING_CASE_STUDY.md)  
**Generic fixed-observable specializations:**
[`generic_first_stieltjes/`](generic_first_stieltjes/)<br>
**Amortized one-sample observable-head audit:**
[`generic_first_stieltjes/depth_order5_scalar/multi_observable/`](generic_first_stieltjes/depth_order5_scalar/multi_observable/)<br>
**Exact quadratic specialization:**
[`quadratic_compiler/`](quadratic_compiler/)
**Historical source:**
[`archive/ORIGINAL_NOTES_AND_NTK_SAMPLE.md`](archive/ORIGINAL_NOTES_AND_NTK_SAMPLE.md)  
**Last consolidated:** 2026-08-19

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

Several important exact specializations are now maintained. For the one-sample,
two-hidden-layer quadratic model, derivative monomials close under a finite
decorated-forest grammar; Section 11 records its certificates. For the single
order-three directional observable \(D_c^3g_c\), the
[`generic_first_stieltjes/`](generic_first_stieltjes/) study closes a
response-aware Gaussian recursion for generic polynomially-smooth activations
at every separately fixed hidden depth and batch size. These prove substantial
special-case peeling calculi; neither upgrades the general theorem target.

For a fixed batch of size $B$, a primitive preactivation row is a
$B$-dimensional Gaussian vector. Higher-order states may require $q$ jointly
generated base vectors and therefore a Gaussian integral of total dimension
$qB$. The number $q$ is finite for each fixed finite construction and is
independent of width. A bound on $q$ independent of depth is an additional
open finite-state-closure problem for the general grammar. The audited
order-three specialization above is a narrower exception: its compact forward
transition uses one \(4B\)-dimensional Gaussian block at every layer.

At two hidden layers and one sample, the same specialization is now carried
through \(F^{(5)}(0)\).  Complete Wick--Stein elimination gives a terminal
formula containing only products of one-dimensional activation moments, with
derivatives through order five.  Independent compilers agree on all 974
unit-Gram monomials of the fifth derivative and on the full symbolic input-
variance dependence.  This is an exact fixed-order exception, not a generic
order-five observable compiler or a depth-uniform closure theorem.

That one-sample order-five axis is now explicitly closed and independently
audited at three and four hidden layers as well.  For \((A,B,C)=
(F'(0),F^{(3)}(0),F^{(5)}(0))\), the layer-tagged distributed maps contain
\((4,342,27\,421)\) and \((5,1\,929,462\,776)\) terms, while the unit-Gram maps
contain \((4,160,6\,519)\) and \((5,350,17\,641)\).  Two frozen compilers agree
on every coefficient, including the full symbolic \(Q^0\) dependence.  The
underlying arbitrary-fixed-depth construction keeps 21 forward covariances,
15 reverse covariances, and 30 response coefficients per reused hidden
matrix: 66 states and one forward/reverse outer sweep per layer.  This is a
finite-state construction for this particular order-five observable.  It is
not a theorem that arbitrary observables admit the same registry, that fully
distributed formulas stay small, or that a regime with \(H=H(n)\) converges.
In the shared-activation unit-Gram quotient, the
[`depth_order5_scalar` report](generic_first_stieltjes/depth_order5_scalar/ARBITRARY_DEPTH_B1_ORDER5_SCALAR_RECURRENCE.md)
now replaces those 66 response-aware entries by six alternating deterministic
scalar sweeps of dimensions \(7/8/4/4/3/3\), or 29 propagated coordinate
types.  All 38 local maps use only one-dimensional \(M_\nu\) atoms and their
exact H=2,3,4 expansions have zero coefficient discrepancies.  The dependency
chain is F1/R1/F2/R2/F3/R3; no compression to a single forward and single
backward sweep has been proved.
The annealed identification is direct under an all-orders polynomially-smooth
activation envelope; a finite \(C^5\) envelope alone still requires a separate
probability and uniform-integrability bridge.

The same unit-Gram graph also exposes an amortized multi-observable
architecture.  The parameter-flow jets are universal; observable derivative
tensors attach as separate heads.  For the hidden-activation squared RMS, two
independently frozen Wick--Stein producers reduce the missing moving
\(\Gamma_{04}\) contraction to one additional \(H\)-cell forward sweep with
two dynamic scalars and literal \(M_\nu\)-only transitions.  All algebraic,
finite-width, parity, exact-control, and smooth-nonpolynomial gates pass, so
this named head is promoted at arbitrary separately fixed \(H\), \(B=1\), and
unit forward Gram.  The original three-hidden-layer, three-width panel remains
permanently **inconclusive** because its frozen curvature fit was saturated;
a separately frozen fourth-width extension resolved that design defect and
passed without relabelling the original experiment.  Section 13 gives the
complete derivation, exact outputs, architecture, and claim boundary.

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

There is now one audited narrower exception at derivative order five.  For
the one-sample output jet \((F'(0),F^{(3)}(0),F^{(5)}(0))\), the response-aware
compiler uses exactly 66 covariance/response entries per reused hidden
matrix, so its outer chronological program has \(66(H-1)\) registry entries
and one forward/reverse sweep at every separately fixed hidden depth.  The
terminal H=3 and H=4 maps have been emitted and independently compared
atom-by-atom.  In the unit-Gram quotient, a second representation eliminates
the response objects completely and closes on 29 deterministic scalar types
across six alternating sweeps.  Its local grammar is independent of depth and
its H=2,3,4 expansions are exactly audited.  This does not close the general
state family \(\mathcal S\) in (10.1): the result is for one observable, its
strict two-sweep compression remains open, and assigning distinct layer tags
and fully distributing the fifth-order formula grows from 1,045 terms at H=2
to 462,776 at H=4.

For the hidden-activation squared-RMS observable, the same universal cache
supports an algebraically audited two-scalar \(\Gamma_{04}\) head.  It adds
one nearest-neighbour forward sweep: one target layer costs \(\ell\) cells,
while the same \(H\)-cell sweep emits all layer heads, so it is not \(H\)
separate computations.  Its independent algebraic, exact finite-width, and
smooth-nonpolynomial promotion gates pass.  This named construction supplies
no small-head theorem for a generic observable.

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
F^{(11)}(0)&=291\,982\,832\,387\,585\,872\,335\,470\,592,\\
F^{(13)}(0)&=102\,853\,512\,279\,246\,664\,353\,620\,526\,022\,656,\\
F^{(15)}(0)&=49\,079\,184\,579\,077\,107\,476\,764\,629\,402\,991\,788\,032,\\
F^{(17)}(0)&=30\,555\,969\,894\,096\,099\,495\,444\,855\,650\,521\,777\,374\,167\,040.
\end{aligned}
$$

The order-eleven number is the exact sum of all twelve Wick-pair sectors. The audit combines a transparent Python prototype, direct pairings at low order, exhaustive differentiated-forest expansion, compressed connected recursion, and a second equality-partition evaluator. Every accepted higher-order route first reproduced all ten order-nine sectors exactly. Order-eleven sectors $P=1,\ldots,9$ were evaluated from exhaustive exports with checked 512-bit arithmetic; $P=10,11,12$ were separately certified by the high-sector machinery. A conservative bound needs only 275 bits through order thirteen, so overflow would throw rather than wrap.

The order-thirteen value comes from a separate exact finite Gaussian-program
recurrence on the \(\beta=1\) block-metric family.  It reproduces every
Campaign-4 coefficient through order nine, the accepted canonical value
through order eleven, and the complete solvable \(\alpha=0\) axis through
order thirteen.  A direct \(\mathbb Q[\alpha]\) implementation independently
recomputes every coefficient, while the connected-tree compiler reproduces
substantial new order-eleven and order-thirteen sectors.

The order-fifteen and order-seventeen values come from a bounded canonical
scalar successor of that recurrence.  A production implementation and an
isolated implementation with a separate sparse Gaussian-monomial and Wick
engine each reproduced the entire accepted prefix through order thirteen,
all parity zeros through order sixteen, and both new integers exactly.  The
retained production order-seventeen run used 230.318 seconds and 189.4375 MiB
peak RSS.  The independent route used 43.59 seconds at standalone order
fifteen and 163.08 seconds with 94,060 KiB peak RSS at order seventeen.  Full
results and retained route records are in the
[canonical high-order successor](../stieltjes_conjecture/resolution_program/canonical_high_order/).
Its frozen protocol ended at order seventeen; no order-nineteen computation
was attempted.

The same two scalar recurrences were subsequently contracted against the
hidden observables

$$
Q_1=\mathbb E[u^2],\qquad Q_2=\mathbb E[z^2].
$$

They agree exactly through $Q_1^{(16)}(0)$ and $Q_2^{(16)}(0)$ after
reproducing the Campaign-1 jets through order eight.  The Ward identity
$Q_1'=8F$ additionally fixes $Q_1^{(18)}(0)$ from the already accepted
$F^{(17)}(0)$, with no order-nineteen feature computation.  Downstream exact
inversion supplies nine first-hidden and eight second-hidden Stieltjes
moment candidates; every accessible squared- and literal-RMS Hankel principal
minor is strictly positive.  Sources, route records, and certificates are in
the [canonical hidden-norm successor](../stieltjes_conjecture/resolution_program/canonical_hidden_high_order/).
These are model-specific fixed-order contractions, not an all-order hidden
measure or positive-time trajectory theorem.

These are exact integer outputs of audited computer algebra under proved
special-case reductions, not hand enumerations or formally verified software.
In particular, the order-eleven \(P=9\) sector has one complete checked route
but has not been redundantly recomputed by the newer connected-sector engine.
Full forest provenance is in [the D11 audit](quadratic_compiler/D11_LOWER_SECTOR_AUDIT.md)
and [sector-engine audit](quadratic_compiler/SECTOR_ENGINE.md); the
order-thirteen through order-seventeen recurrences and independent checks are
in the downstream
[resolution program](../stieltjes_conjecture/resolution_program/).

### 11.5 Historical order-thirteen and acceleration audits

The complete \(F^{(13)}(0)\) is now the exact value in Section 11.4.  Before
the Gaussian-program recurrence was found, exact positive-subsum calculations
gave monotone lower bounds, culminating at

$$
50\,393\,647\,763\,255\,899\,049\,472\,742\,772\,736
$$

for component-edge cap fourteen. This remains only a historical lower bound.
In the maximal \(P=14\) sector, discovery found 465,075 recurrence states and
325,190 base trees; only the first 704 base contractions completed, so no
sector subtotal was certified by that route. See
[the D13 audit](quadratic_compiler/D13_ATTEMPT.md).

Several accelerations were audited:

- approximate first-pair and adjacent-pair modes retain positive sub-sums but are not exact checkpoints;
- the GF(2) matroid shortcut is valid only in the no-weight-hit, even-row, tight-nullity case; an explicit decorated-tree counterexample invalidates its unrestricted rank gate;
- a singleton-row shortcut omitted even-$a$ parity, so its reported subtotal and timing are retracted;
- prefixwise factor-nine two-hit bounds are exactly false, and an all-order version would contradict the factorial lower bound; no special order-eleven upper bound was proved;
- finite-width formal-jet simulation is a numerical pilot, not an exact mean-field certificate.

The restricted proofs, counterexamples, and retractions live next to the compiler. They illustrate a central MFP rule: a shortcut earns only the scope of its proof, even after passing extensive low-order regression gates.

### 11.6 Model-specific parameter extensions

Six bounded compiler campaigns tested how much of the same exact grammar
survives beyond the canonical point.

1. A relative block-metric ray jointly computed the output through order nine
   and the second-hidden squared-RMS response through order eight.  The later
   canonical-only Gaussian-program successor extends that hidden response
   through order sixteen without extending the full parameter ray.
2. Two symmetry-reduced inputs with equal and opposite labels were computed
   through order seven while retaining the input Gram matrix in both the
   initialization law and the first-layer gradient metric.
3. A centered-to-overcentered first-hidden quadratic activation was computed
   through order seven using an exact centered-Gaussian moment grammar.
4. Independent first-hidden and middle-weight metric parameters were graded
   into 125 atomic sectors through order nine on the full nonnegative
   quadrant.
5. Three equicorrelated equal-label inputs were compiled through order five,
   including a genuine signed three-color cycle invariant; the order-seven
   resource gate failed closed.
6. A bounded canonical order-thirteen threshold probe tested coarse and
   hybrid envelopes but failed its fresh-regression/provenance gate and
   produced no accepted new bound.

Campaigns 1--4 reached exact finite Hankel endpoints in the downstream
Stieltjes study.  Campaign 5 proves only exact lower jets and two necessary
moment signs, not a Hankel determinant.  Campaign 6 is a stopped diagnostic,
not a coefficient or bound.  These extensions enlarge the audited
special-case compiler but do not establish the general MFP theorem.  Their
consolidated claim levels are in the downstream
[Stieltjes master](../stieltjes_conjecture/CURRENT_RESEARCH_STATE.md).

### 11.7 What this does and does not establish

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

### 13.2 Audited one-sample order-five backbone

There is now one fixed-observable construction in which the depth recursion
has been completely Wick--Stein contracted. Its scope is one sample,
arbitrary but separately fixed hidden depth \(H\), shared activation, equal
hidden widths, and unit forward Grams. Define

$$
M_{\nu_0\ldots\nu_5}
:=\mathbb E_{G\sim N(0,1)}
\prod_{r=0}^{5}\phi^{(r)}(G)^{\nu_r},\qquad
d=M_{020000},\qquad
b_\ell=d^{H-\ell},\qquad
\tau_\ell=\sum_{r=0}^{\ell}d^r.
\tag{13.3}
$$

The exact factored graph is

$$
F1\longrightarrow R1\longrightarrow F2\longrightarrow R2
\longrightarrow F3\longrightarrow R3.
\tag{13.4}
$$

Every named sweep contains exactly \(H\) nearest-neighbour layer cells. The
printed first-layer initialization of a forward sweep is its \(0\to1\)
boundary cell with the fixed boundary substituted; a reverse top
initialization is the output-to-\(H\) boundary cell. A single polynomial
template is reused from layer to layer *within* each sweep, but the six
templates are different jet-grade maps and alternate direction. Their
propagated dimensions are \(7/8/4/4/3/3\), hence 29 scalar coordinate types.
At \(d=1\),

$$
b_\ell=1,\qquad \tau_\ell=\ell+1,
\tag{13.5}
$$

but the layer-\(\ell\) cell can still depend numerically on
\(\tau_{\ell-1}=\ell\) and on the stored states.

To distinguish the two jet geometries, put hats on derivatives along the
frozen straight line through initialization and use unhatted symbols for
derivatives along the moving feature-ascent flow. Normalized inner products
and all response coefficients below mean their deterministic annealed
large-width limits. The 29 coordinates have the following meanings.

| sweep | coordinates | derivative/covariance meaning |
|---|---|---|
| \(F1\) | \(u,v,w,x,y\) | \(u=\langle\widehat X_0,\widehat X_2\rangle_n\), \(v=\langle\widehat X_0,\widehat X_4\rangle_n\), \(w=\langle X_1,X_1\rangle_n\), \(x=\langle\widehat X_1,\widehat X_3\rangle_n\), \(y=\langle\widehat X_2,\widehat X_2\rangle_n\) |
| \(F1\) | \(j,k\) | Stein responses of \(\widehat X_3,\widehat X_5\) to the base reverse innovation |
| \(R1\) | \(e02,e11,e13,e22\) | frozen reverse covariances \(\langle\widehat\Delta_0,\widehat\Delta_2\rangle_n\), \(\|\widehat\Delta_1\|_n^2\), \(\langle\widehat\Delta_1,\widehat\Delta_3\rangle_n\), \(\|\widehat\Delta_2\|_n^2\) |
| \(R1\) | \(c10,c21,c30,c32\) | coefficients in \(\widehat\Delta_1=E_1+c10\,\widehat X_0\), \(\widehat\Delta_2=E_2+c21\,\widehat X_1\), and \(\widehat\Delta_3=E_3+c30\,\widehat X_0+c32\,\widehat X_2\) |
| \(F2\) | \(q02,q22,qfm,a2\) | \(q02=\langle X_0,X_2\rangle_n\), \(q22=\|X_2\|_n^2\), \(qfm=\langle\widehat X_2,X_2\rangle_n\), and the reverse-grade-one response of \(X_2\) |
| \(R2\) | \(r02,r22,rfm,d21\) | \(r02=\langle\widehat\Delta_0,\Delta_2\rangle_n\), \(r22=\|\Delta_2\|_n^2\), \(rfm=\langle\widehat\Delta_2,\Delta_2\rangle_n\), and the coefficient in \(\Delta_2=J_2+d21\,X_1\) |
| \(F3\) | \(q13,a30,a32\) | \(q13=\langle X_1,X_3\rangle_n\), plus responses of \(X_3\) to reverse grades zero and two |
| \(R3\) | \(r13,d30,d32\) | \(r13=\langle\widehat\Delta_1,\Delta_3\rangle_n\), plus responses in \(\Delta_3=J_3+d30\,X_0+d32\,X_2\) |

In particular, \(v\) is the frozen-line \(G_{04}\); it is not the moving-flow
\(\Gamma_{04}\) introduced below. The order-three graph is the autonomous
projection

$$
(w,u,j;\ e11,c10)\subset(F1,R1),
\tag{13.6}
$$

with no feedback from higher grades.

For the exact finite-width tensor identities, let
\(\widetilde\nabla=\sqrt n\nabla_\theta\),
\(p=\widetilde\nabla f_n\), and
\(D_n=p\mathbin\cdot\widetilde\nabla\). This rescaled \(p\) is not the raw
parameter vector field \(P=n\nabla_\theta f_n\) used in Section 13.3. Write
\(\mathsf H_f=\widetilde\nabla^2f_n\), \(T=\widetilde\nabla^3f_n\),
\(U=\widetilde\nabla^4f_n\), \(V=\widetilde\nabla^5f_n\), and
\(A_f=\mathsf H_fp\). Then

$$
D_n^3f_n=2T[p,p,p]+4\lVert A_f\rVert^2,
\tag{13.7}
$$

and, with \(m_2=D_n^2p\), \(m_3=D_n^3p\),

$$
D_n^5f_n
=2V[p^5]+10U[A_f,p^3]+10\langle T[p,p],m_2\rangle
+4\lVert m_2\rVert^2+12\langle A_f,m_3\rangle.
\tag{13.8}
$$

The backbone endpoints are

$$
S_{3,H}=j_H+3u_H,\qquad S_{5,H}=k_H+5v_H.
\tag{13.9}
$$

Let the five deterministic terminal folds be

$$
\mathcal H_2=\lVert A_f\rVert^2,\quad
\mathcal U_1=U[A_f,p,p,p],\quad
\mathcal T_2=\langle T[p,p],m_2\rangle,\quad
\mathcal N_2=\lVert m_2\rVert^2,\quad
\mathcal H_3=\langle A_f,m_3\rangle.
\tag{13.10}
$$

Their layerwise definitions are the explicit folds in the
[scalar recurrence](generic_first_stieltjes/depth_order5_scalar/ARBITRARY_DEPTH_B1_ORDER5_SCALAR_RECURRENCE.md).
No Gaussian evaluation remains at the terminal. The output head is

$$
\boxed{
A_H=\tau_H,\qquad
B_H=2S_{3,H}+4\mathcal H_2,\qquad
C_H=2S_{5,H}+10\mathcal U_1+10\mathcal T_2
+4\mathcal N_2+12\mathcal H_3.}
\tag{13.11}
$$

Exact expansion of the 38 local scalar maps agrees coefficient by coefficient
with frozen independent Gaussian normal forms at \(H=2,3,4\). The respective
\(C_H\) maps contain \(974\), \(6\,519\), and \(17\,641\) unit-Gram monomials,
with zero discrepancies. The combined graph uses activation derivatives
only through \(\phi^{(5)}\).

### 13.3 Universal parameter jets and observable heads

Return now to raw parameter coordinates and put

$$
P(\theta)=n\nabla_\theta f(\theta),\qquad
D=P\mathbin\cdot\nabla_\theta,\qquad
\dot\theta=P(\theta).
\tag{13.12}
$$

Ordinary flow differentiation gives the **universal parameter jets**

$$
\theta'=P,\qquad \theta''=DP,\qquad
\theta'''=D^2P,\qquad \theta^{(4)}=D^3P.
\tag{13.13}
$$

They depend on the feature flow but not on a subsequently chosen observable.
For every \(C^4\) scalar observable \(O\), the exact finite-width readout head
is

$$
\begin{aligned}
O'={}&O_1[P],\\
O''={}&O_2[P,P]+O_1[DP],\\
O'''={}&O_3[P,P,P]+3O_2[P,DP]+O_1[D^2P],\\
O^{(4)}={}&O_4[P,P,P,P]+6O_3[P,P,DP]+3O_2[DP,DP]\\
&\quad+4O_2[P,D^2P]+O_1[D^3P].
\end{aligned}
\tag{13.14}
$$

This is the universal-observable principle: compile the parameter-flow jets
once, then attach observable derivative tensors as small readout heads when
their contractions close. It does **not** say that every observable admits
a fixed small scalar head. Each new head still requires its own equality-
partition, width, transpose-response, Wick--Stein, and probability audit.

### 13.4 Hidden-activation squared-RMS head

For the moving activation jet

$$
X_\ell^{(r)}
=\left.\frac{d^r}{ds^r}x^\ell(\theta(s))\right|_{s=0},
$$

define the finite-width empirical contraction

$$
\Gamma_{rs,n}^\ell
:=\frac1n\langle X_\ell^{(r)},X_\ell^{(s)}\rangle
$$

and its annealed limit \(\Gamma_{rs}^\ell\) when the limit and expectation
interchange are justified. The exact finite-width product rule for

$$
Q_\ell(s)=\frac1n\lVert x^\ell(s)\rVert^2
$$

is

$$
Q_{\ell,n}^{(k)}(0)
=\sum_{r=0}^{k}\binom{k}{r}\Gamma_{r,k-r,n}^\ell.
\tag{13.15}
$$

After the probability bridge, the same identity holds for the deterministic
limits. The audited backbone dictionary is

$$
\Gamma_{11}^\ell=w_\ell,\qquad
\Gamma_{02}^\ell=q02_\ell,\qquad
\Gamma_{22}^\ell=q22_\ell,\qquad
\Gamma_{13}^\ell=q13_\ell.
\tag{13.16}
$$

It follows that

$$
Q_\ell''(0)=2(w_\ell+q02_\ell),
\tag{13.17}
$$

while order four additionally needs

$$
\gamma04_\ell:=\Gamma_{04}^\ell,\qquad
Q_\ell^{(4)}(0)=2\gamma04_\ell+8q13_\ell+6q22_\ell.
\tag{13.18}
$$

The missing contraction is not the frozen state \(v_\ell\). At every internal
equal-width matrix layer, its local peel starts from the exact finite-width
identities

$$
W^{\ell,(r+1)}
=\frac1{\sqrt n}\sum_{a=0}^{r}\binom ra
\Delta_{\ell,a}X_{\ell-1,r-a}^{\mathsf T},
\tag{13.19}
$$

$$
Z_{\ell,4}
=\frac1{\sqrt n}\sum_{a=0}^{4}\binom4a
W^{\ell,(a)}X_{\ell-1,4-a}.
\tag{13.20}
$$

The first hidden layer is the corresponding fixed-input boundary cell: its
input-Gram factors are substituted before applying the same contraction.  It
is not represented by falsely treating the input as another random
equal-width hidden vector.

Regrouping all ten rank-one matrix-flow terms gives

$$
\begin{aligned}
Z_{\ell,4}={}&F_{\ell,4}
+(5\Gamma^{\ell-1}_{03,n}+10\Gamma^{\ell-1}_{12,n})\Delta_{\ell,0}\\
&+(9\Gamma^{\ell-1}_{02,n}+8\Gamma^{\ell-1}_{11,n})\Delta_{\ell,1}
+7\Gamma^{\ell-1}_{01,n}\Delta_{\ell,2}
+\Gamma^{\ell-1}_{00,n}\Delta_{\ell,3}.
\end{aligned}
\tag{13.21}
$$

The order-four activation Bell polynomial is exactly

$$
X_{\ell,4}
=\phi^{(4)}Z_1^4+6\phi^{(3)}Z_1^2Z_2
+3\phi''Z_2^2+4\phi''Z_1Z_3+\phi'Z_4.
\tag{13.22}
$$

Readout-reflection parity kills the deterministic grade-zero and grade-two
branches after expectation, but not seedwise. The two surviving transpose
responses give

$$
Z_{\ell,4}=F_{\ell,4}+l41\,\Delta_{\ell,1}
+l43\,\Delta_{\ell,3},
\tag{13.23}
$$

$$
l41=9q02_{\ell-1}+8w_{\ell-1}+a41_{\ell-1},\qquad
l43=1+a43_{\ell-1}.
\tag{13.24}
$$

The raw local state is
\((\gamma04,a41,a43)\), initialized at zero. Complete Wick--Stein
elimination gives

$$
a43_\ell=d(1+a43_{\ell-1}),
\qquad 1+a43_\ell=\tau_\ell.
\tag{13.25}
$$

Thus \(a43\) is deterministic depth data, \(l43=\tau_{\ell-1}\), and the
smallest state found is the two-vector

$$
h_\ell=(\gamma04_\ell,a41_\ell),\qquad h_0=(0,0).
\tag{13.26}
$$

No minimality theorem is claimed. With \(b=b_\ell\),
\(l1=\tau_{\ell-1}\), \(l2=1+a2_{\ell-1}\),

$$
l30=4q02_{\ell-1}+3w_{\ell-1}+a30_{\ell-1},\qquad
l32=1+a32_{\ell-1},\qquad
l41=9q02_{\ell-1}+8w_{\ell-1}+a41_{\ell-1},
\tag{13.27}
$$

the transition is

$$
(\gamma04_\ell,a41_\ell)
=\bigl(\mathcal P_\gamma,\mathcal P_a\bigr)
(h_{\ell-1};\text{stored backbone states},M).
\tag{13.28}
$$

The literal, fully contracted polynomials
\(\mathcal P_\gamma\) and \(\mathcal P_a\) contain 64 and 17 canonical
monomials and are displayed in the
[frozen two-state transition table](generic_first_stieltjes/depth_order5_observables/independent/FROZEN_GAMMA04_REDUCED_TRANSITIONS.md).
They contain no Gaussian innovation, random covariance, response operation,
matrix inverse, or multivariate integral. Every token on the right of that
table is either an \(M_\nu\) atom, rational arithmetic, deterministic depth
data, a previous head state, or a stored backbone state. The head itself
uses derivatives only through \(\phi^{(4)}\), so it does not raise the full
backbone ceiling \(\phi^{(5)}\). It is one post-\(R3\) bottom-up sweep of
exactly \(H\) nearest-neighbour cells.

The local audit includes all five set partitions of derivative grade four,
all four transpose-response grades, and every equality partition of at most
five neuron labels. After forced same-matrix transpose contractions are
peeled, a partition \(\pi\) of \(m\) remaining labels has relative width
degree

$$
n^{|\pi|-m}.
\tag{13.29}
$$

Every accidental collision is therefore negative width; reverse innovations
are Wick-paired and forward innovations are Wick-paired or Stein-attached to
the base Gaussian. Two independently frozen producers agree on every raw
\(83/20/1\) monomial and every reduced \(64/17\) monomial. A corrected third
five-slot canonicalizer agrees as well. Its preserved predecessor, which
emitted 82 terms, is falsified: it aliased the new fifth forward innovation
with an existing slot. Exact population expansions at every layer through
\(H=4\) have zero discrepancies, and two finite-width differentiators agree
in 30 layer cases to maximum scaled error \(1.38\times10^{-15}\). Constant,
linear, and nontrivial unit-affine controls pass exactly.

### 13.5 RMS and readout-reflection parity

Let \(T\) flip only the Gaussian readout. The initialization law is
\(T\)-invariant and

$$
f(T\theta)=-f(\theta),\qquad P(T\theta)=-T P(\theta).
\tag{13.30}
$$

Uniqueness of the finite-dimensional feature-flow ODE gives

$$
\theta(s;T\theta_0)=T\theta(-s;\theta_0),\qquad
X_\ell^{(r)}(T\theta_0)=(-1)^rX_\ell^{(r)}(\theta_0).
\tag{13.31}
$$

The output curve also obeys

$$
F(s;T\theta_0)=-F(-s;\theta_0).
$$

Consequently the annealed output curve is odd,
\(F(-s)=-F(s)\), and
\(F(0)=F''(0)=F^{(4)}(0)=0\).  Hidden-Gram and hidden-RMS
observables are even after annealed expectation, so every odd derivative of
those observables vanishes. These are not the false seedwise claims that one
unpaired initialization has zero output at the origin or zero odd hidden
derivative.

Under unit Gram, \(Q_\ell(0)=1\). For
\(R_\ell=\sqrt{Q_\ell}\), (13.17)--(13.18) give

$$
\boxed{R_\ell''(0)=w_\ell+q02_\ell,}
\tag{13.32}
$$

$$
\boxed{
R_\ell^{(4)}(0)
=\gamma04_\ell+4q13_\ell+3q22_\ell
-3(w_\ell+q02_\ell)^2.}
\tag{13.33}
$$

### 13.6 Label-one MSE coefficient head

At finite width, one-sample label-one MSE is exactly a scalar time change of
the corresponding feature-ascent curve.  After taking separately fixed-depth
annealed limits coefficient by coefficient, the deterministic Taylor germs
obey the formal time-change algebra

$$
\frac{ds}{dt}=c(1-F(s)),\qquad c=2\eta.
\tag{13.34}
$$

Let \(q_2=Q_\ell''(0)\), \(q_4=Q_\ell^{(4)}(0)\). Exact formal series
composition of these deterministic coefficient germs, using
\(F'(0)=A_H\), \(F'''(0)=B_H\), yields

$$
\boxed{
\begin{aligned}
Q_t''(0)&=c^2q_2,\\
Q_t'''(0)&=-3c^3A_Hq_2,\\
Q_t^{(4)}(0)&=c^4(q_4+7A_H^2q_2),\\
Q_t^{(5)}(0)&=-5c^5\bigl[(3A_H^3+B_H)q_2+2A_Hq_4\bigr].
\end{aligned}}
\tag{13.35}
$$

The fifth feature coefficient \(C_H\) first enters \(s^{(6)}(0)\); its
absence from (13.35) is required.  Equation (13.35) is not a seedwise
finite-width identity: before the limit, \(F_n(0)\) and the odd hidden-
observable jets need not vanish, and expectations contain products such as
\(\mathbb E[A_nq_{2,n}]\), not a priori \(A_Hq_2\).

### 13.7 Amortized DAG architecture and cost

The audited architecture should be read as

$$
\begin{array}{c}
\text{universal feature-ascent backbone: }F1/R1/F2/R2/F3/R3\\[2mm]
\swarrow\hspace{28mm}\searrow\\[-1mm]
\text{output fold }(A_H,B_H,C_H)
\hspace{10mm}
\text{audited }\Gamma_{04}\text{ sweep}\\
\downarrow\hspace{38mm}\downarrow\\
\text{kernel/loss algebra}
\hspace{15mm}
\text{layerwise }Q_\ell,R_\ell\text{ and MSE-time head}.
\end{array}
\tag{13.36}
$$

In the factored representation the backbone costs \(6H\) nearest-neighbour
cells. One chosen hidden layer adds \(\ell\) head cells; the same \(H\)-cell
head sweep emits results for *all* hidden layers, rather than requiring \(H\)
independent sweeps. The dynamic head state streams in \(O(1)\) memory once
the backbone cache exists; retaining all layer outputs costs \(O(H)\). The
output, kernel, and scalar loss algebra is terminal \(O(1)\) work. In
particular, with the local output-clock kernel defined by the formal Taylor
inverse
\(K_H(y):=F_H'(F_H^{-1}(y))\).  This inverse exists locally as a formal series
because \(A_H=\tau_H>0\):

$$
\mu_{0,H}=\frac{B_H}{2A_H^2},\qquad
\mu_{1,H}=\frac{4B_H^2-A_HC_H}{24A_H^5},\qquad
K_H(y)=A_H+\mu_{0,H}y^2-\mu_{1,H}y^4+O(y^6).
\tag{13.37}
$$

When \(\mu_{0,H}\ne0\), the first one-pole Padé head is

$$
K_{H,[0/1]}(y)
=A_H+\frac{\mu_{0,H}y^2}
{1+(\mu_{1,H}/\mu_{0,H})y^2}.
\tag{13.38}
$$

Its induced label-one MSE curve is defined by

$$
\dot y=2\eta(1-y)K_{H,[0/1]}(y),\qquad y(0)=0,\qquad
L_{H,[0/1]}=(1-y)^2,\qquad L_{H,[0/1]}(0)=1.
\tag{13.39}
$$

This is a rational approximation to \(K_H\) and the loss curve induced by
that approximation, not a proof of Stieltjes positivity or of the exact
positive-time neural trajectory.

The analogous preactivation observables
\(n^{-1}\|Z_\ell(s)\|^2\) reuse the universal parameter jets, but their
moment-only observable head has not been constructed. Its state and cost
remain open. More generally, this example does not prove a small-head
theorem for arbitrary observables.

### 13.8 Claim level, probability boundary, and order-seven roadmap

The status is deliberately split.

1. Equations (13.13)--(13.15), (13.19)--(13.22), and (13.30)--(13.31)
   are exact finite-width identities.  The finite-width counterpart of
   (13.34) is the exact scalar time-change law, while (13.34)--(13.35) display
   its exact formal algebra after the deterministic annealed coefficient
   limits and parity identities have been established.
2. The \(M_\nu\)-only two-state transition is an algebraically audited
   Gaussian normal form: independent producers, atom maps, finite-width
   differentiators, and exact controls agree.
3. Two separately preregistered normalized-sine panels at \(H=2\) pass. The
   original hostile \(H=3\) panel is retained as **inconclusive**, because its
   three widths saturate the preregistered quadratic-in-\(1/n\) curvature
   diagnostic. It is not silently relabelled a pass.  A separately frozen
   extension added \(n=512\), regenerated all old samples, and passed the
   unchanged validity and curvature thresholds over 4,096 networks: the
   largest absolute intercept z-score is \(0.493\), the largest exact identity
   residual is \(6.01\times 10^{-14}\), and no nonfinite sample or resolved
   material curvature occurs.  This follow-up discharges the empirical gate
   while preserving the original outcome.  The frozen design, raw hashes,
   exact atom comparisons, and claim-level decision are recorded in the
   [hostile audit](generic_first_stieltjes/depth_order5_scalar/multi_observable/audit/HOSTILE_REPORT.md)
   and its [evidence ledger](generic_first_stieltjes/depth_order5_scalar/multi_observable/audit/EVIDENCE_LEDGER.md).
4. At every separately fixed \(H\), a sufficient annealed theorem envelope
   is polynomial smoothness—\(\phi\in C^\infty\), with every derivative
   polynomially bounded—together with the applicable finite tensor-program
   convergence in every finite \(L^p\). A weaker route must prove convergence
   in probability and a uniform \(L^{1+\epsilon}\) bound for every retained
   transition monomial and Gram. \(C^4\) regularity suffices only for the
   finite-width order-four hidden head; the combined output backbone uses
   derivatives through order five.

Accordingly, the two-state \(\Gamma_{04}\) head is promoted as a fixed-\(H\),
\(B=1\), unit-Gram Gaussian normal form, with an annealed theorem under the
stated probability hypotheses. Nothing here is uniform in \(H=H(n)\), covers
\(B>1\), proves a positive-time expansion, or establishes a grammar-wide
compiler theorem.

There is a separately quarantined order-seven roadmap. Grade triangularity
suggests that the order-five graph may embed unchanged, with possible new
\(F4/R4\) and \(F5/R5\) passes. Two independent abstract free-tree
enumerations find 23 unlabeled shapes on eight vertices, the proposed raw
\(D^7f\) family count. But no rank-labelled 23-family tensor identity,
complete coefficients, equality/transpose audit, fixed-dimensional
\(M\)-only recurrence, or complexity proof has been constructed. Therefore
the order-seven closure, state count, sweep count, derivative ceiling
\(\phi^{(7)}\), family interpretation, and \(O(H)\) factored-DAG claim remain
roadmap hypotheses, not results.

### 13.9 Discrete gradient descent

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

### 13.10 What a jet does not prove

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
- For the particular one-sample order-five output jet, such a compiler and a
  66-state-per-hidden-matrix response registry are explicit.  In the unit-Gram
  quotient, an explicit 29-coordinate-type, six-sweep scalar recurrence
  eliminates that response registry into one-dimensional moments.  Frozen
  terminal maps have been audited at hidden depths two, three, and four.  This
  is evidence for, not a proof of, the preceding grammar-wide target.
- The exact observable chain rule factors finite-order work into universal
  parameter-flow jets and observable-specific readout tensors.  For the
  hidden-activation squared RMS, the named extra head is fully
  Wick--Stein contracted to two scalar states and independently equal
  atom-by-atom across three implementations.  Its finite-width identities,
  algebraic normal form, and smooth-nonpolynomial gate pass.  The original
  three-width \(H=3\) panel remains inconclusive, while a separately frozen
  fourth-width extension resolves its identifiability defect and passes.
- Polynomial-smooth finite-\(L^p\) tensor-program convergence supplies a
  sufficient annealed bridge at separately fixed \(H\).  It does not replace
  the empirical claim level, prove a finite-\(C^5\) bridge, or make the result
  uniform in depth.
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
21. A constant response-registry size and an \(O(L)\) outer sweep do not imply
    a small fully distributed normal form.  The order-five one-sample depth
    compiler provides an explicit counterexample to that inference even
    though its compact factored DAG remains executable.

## 17. Required nonclaims

The current program does not prove:

- convergence of a learning-rate or time Taylor series;
- complete positive-time training dynamics;
- arbitrary or width-dependent training times;
- a uniform-in-depth probability limit;
- a depth-uniform bound on the size of a fully distributed order-five normal
  form merely from the existence of a fixed per-layer response registry;
- that every observable attaches through a fixed small scalar head;
- a contracted preactivation-RMS head;
- minimality of the promoted two-state hidden-activation \(\Gamma_{04}\)
  head, or an analogous small-head result for every observable;
- any order-seven scalar closure, state count, sweep count, derivative
  ceiling, or \(O(H)\) factored-DAG theorem;
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
15. **Replicate and broaden the observable-head empirical audit.** The
    original three-width \(H=3\) design remains inconclusive and the separately
    frozen fourth-width extension discharges the promotion gate.  Replicate
    that extension and test further depths and activations without changing
    either frozen decision.
16. **Finite-regularity observable bridge.** Prove convergence and uniform
    integrability for the order-five backbone plus hidden-RMS head under a
    direct finite-\(C^5\) envelope, rather than all-orders polynomial
    smoothness.
17. **Additional observable heads.** Derive and audit the preactivation-RMS
    head and identify which observable classes share the same cached
    parameter-flow jets without new reverse sweeps.
18. **Order-seven construction.** Write the rank-labelled raw tensor
    identity, perform equality/transpose peeling, and independently audit any
    proposed \(M_\nu\)-only recurrence before promoting the 23-tree roadmap.

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

There are two complementary core laboratories, five bounded parameter-
extension campaigns, and one stopped threshold diagnostic. The fixed
three-hidden-layer backward and
training calculations expose conditional Stein corrections and lower-layer
boundary transport. The canonical one-sample quadratic compiler proves an
exact decorated-forest specialization and supplies accepted integer
coefficients through derivative order eleven.  A separate finite
Gaussian-program recurrence on the \(\beta=1\) block-metric family supplies
the complete exact \(\alpha\)-polynomial jet through order thirteen,
including the canonical coefficient at \((1,1)\).  Two bounded exact scalar
implementations then extend the canonical jet through order seventeen,
reproducing one another and the full accepted lower prefix.  Its campaigns retain the
same basic grammar while varying a relative block metric and hidden
observable, two- and three-input symmetry channels, a shifted first-hidden
activation, and two independent hidden-block metric weights.  Four reached
their frozen finite Hankel endpoints downstream; the three-input route stops
at lower moments, and the threshold diagnostic contributes no new bound at
its own claim level.  The order-thirteen \(\beta=1\) jet yields a negative
shifted \(3\times3\) output-kernel Hankel determinant throughout
\(0<\alpha\leq1/100\).  It therefore disproves the uniform block-metric
Stieltjes extension without freezing a layer, while leaving the canonical
\((1,1)\) all-order claim open.  Exact inversion of the canonical successor
gives eight output moments and positive-definite ordinary and shifted
$4\times4$ Hankel matrices.  Hidden contractions of the same recurrence give
nine first-hidden and eight second-hidden moments, with every accessible
squared- and literal-RMS Hankel principal minor strictly positive.  These are
finite-order passes, not all-order theorems.  No
order-nineteen run was attempted.  These results remain model-specific and
do not prove a generic compiler theorem.

For one specific order-three directional observable, the generic-activation
program has now been closed beyond the earlier formal examples.  The
[`generic_first_stieltjes/`](generic_first_stieltjes/) specialization gives an
explicit response-aware Gaussian recursion for
\(C_{H,c}=\lim_n\mathbb E[D_c^3g_c]\) at every separately fixed hidden depth
\(H\), batch size \(B\), channel \(c\), and deterministic PSD input Gram,
under an all-orders polynomially-smooth activation envelope.  Its compact DAG
uses \(O(B^2)\) retained state per layer, and an independent hostile audit
checks the transpose chronology, parity cancellations, tensor-program
probability bridge, exact reductions, and arbitrary-label cubic MSE
coefficient.  This proves closure for that fixed observable, not for the
general admissible grammar, growing \(H\) or \(B\), or positive training time.
Here \(C_{H,c}\) is the historical notation of the order-three program; in
the order-five convention of Section 13 it is the cubic coefficient \(B_H\)
along the scalar feature-ascent channel, not the fifth-order coefficient
\(C_H\).

For the narrower one-sample order-five route, the same study gives
algebraically flattened and independently audited expressions for
\(F^{(5)}(0)\) at two, three, and four hidden layers.  The respective unit-Gram
fifth-derivative maps have 974, 6,519, and 17,641 moment monomials and no
auxiliary Gaussian state.  At three and four layers, separately frozen
compilers also agree on all 27,421 and 462,776 layer-tagged fifth-derivative
terms, and an exact degree/interpolation/holdout audit certifies the complete
symbolic-\(Q^0\) dependence.  The accompanying arbitrary-fixed-depth
chronology has 66 covariance/response states per hidden matrix for general
forward Grams.  Its unit-Gram contraction instead has 29 deterministic scalar
coordinate types in six alternating sweeps, with every transition written in
one-dimensional \(M_\nu\) moments and H=2,3,4 literal comparisons all exact.
This is not yet the stronger one-forward/one-backward representation.  Under
the all-orders polynomially-smooth fixed-program envelope these are annealed
width-limit theorems; finite \(C^5\) regularity alone does not supply
expectation convergence.  The formulas provide the first two local
kernel/Padé coefficients, while normalized sine has both coefficients
negative.  Thus neither positivity of a generic Stieltjes sequence nor a
depth-uniform small flattened representation follows.

The new amortized-observable audit makes the architecture of that unit-Gram
graph explicit.  It separates universal parameter-flow jets from
observable-specific heads, identifies every one of the 29 backbone
coordinates, and derives a two-dynamic-scalar, one-forward-sweep
\(\Gamma_{04}\) head for hidden-activation RMS derivatives.  The exact
finite-width identities, all equality and transpose branches, independent
Wick--Stein maps, H=2--4 population maps, parity, and exact controls pass.
Two \(H=2\) sine panels pass.  The original mandatory three-width \(H=3\)
curvature panel remains inconclusive, while a separately frozen \(n=512\)
extension passes and discharges the gate.  The two-state head is therefore
promoted in its fixed-depth unit-Gram scope.  Preactivation RMS, a universal
small-head theorem, and every proposed order-seven closure remain open.

The general nonlinear two-step closure remains formal, its
deep-linear specialization is audited, and the finite-state theorem for the
full proposed admissible grammar remains open. None of the exact
specializations should be mistaken for that general theorem.
