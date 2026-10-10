# Operational calculus for finite Gaussian derivative programs

This is an operational companion to [the master proof](master_proof.md),
Sections 1, 2, 7 and 8. It reorganizes the proved calculus without enlarging its
language or making a new convergence claim. It remains a study artifact.
[Worked examples](worked_examples.md) derive matrix reuse, a normalized rank-one
update, singular duplicate queries, and a moving gradient-flow direction.

The order of operations is: differentiate the finite-width program exactly,
lower represented matrix actions into primitive operations, then evaluate the
resulting finite graph with Gaussian sources and response coefficients. Physical
derivatives and formal source partials have different inputs and different rules.

## 1. Input contract and compiler state

Fix the width $n$. A vector type labels one copy of $\mathbb R^n$; matching
dimensions alone do not identify two types. A named initialized matrix

\[
W:\mathbb R^n_{\rm lower}\longrightarrow\mathbb R^n_{\rm upper}
\]

has independent $N(0,1/n)$ entries. Its two endpoint types are distinct.
Different named matrices are independent. Each type has a fixed finite Gaussian
root tuple, independent across coordinate indices; its within-coordinate law
may be singular. Different types' roots and all initialized matrices are
independent. Root means and all deterministic constants are fixed.

An input graph is a finite acyclic list of the following instructions.

| Instruction | Inputs | Output |
| --- | --- | --- |
| Coordinate map | Same-type vectors $u^1,\ldots,u^k$, earlier scalars $s$ | $v_i=F(u_i^1,\ldots,u_i^k;s)$, of that vector type |
| Normalized average | Same-type vectors and earlier scalars | $a=n^{-1}\sum_i F(u_i^1,\ldots,u_i^k;s)$, a scalar |
| Scalar arithmetic | Earlier scalars | Their sum or product |
| Forward matrix call | Named $W$, lower-type $h$ | $y=Wh$, of upper type |
| Transpose call | The same named $W$, upper-type $u$ | $v=W^T u$, of lower type |

Every $F$ is a finite expression in constants, arguments, sums, products and
$\phi^{(r)}$, where $\phi\in C^\infty(\mathbb R)$ and every derivative has
polynomial growth. Deterministic constant vectors are also permitted. All
dimensions other than $n$, derivative orders, update counts, graph lengths
and coefficients are fixed as $n\to\infty$.

The finite compiler stores node identities, types, causal dependencies, named
matrix identities and their orientations. A represented current matrix also
stores an optional initialized matrix plus a finite list of normalized
rank-one terms. Equal-looking uses of one matrix share its identity; its
transpose never creates a new independent matrix.

The output of physical differentiation and lowering is another finite primitive
graph, exactly equal to the requested scalar or vector expression at each
finite $n$. The Gaussian evaluator in Sections 5–7 produces its limiting
scalar expression.

## 2. Lower every represented matrix action exactly

Let $A$ have lower-to-upper type and the stored representation

\[
A=W_0+\sum_{\nu=1}^M c_\nu u_\nu v_\nu^T/n,
\]

where $u_\nu$ has upper type, $v_\nu$ has lower type and $c_\nu$ is scalar.
The $W_0$ term may be absent. Emit

\[
\begin{aligned}
Ah&=W_0h+\sum_\nu c_\nu u_\nu\left(\frac{v_\nu^Th}{n}\right),\\
A^Tu&=W_0^Tu+\sum_\nu c_\nu v_\nu\left(\frac{u_\nu^Tu}{n}\right).
\end{aligned}
\]

Each pairing is one normalized average on its own type. These are finite-width
identities, including all correlations among the factors and matrix history.
Do not send $A$ to the Gaussian evaluator as if it were a newly initialized
Gaussian matrix. The limiting rank-one action is
$H\mapsto U\,\mathbb E[VH]$, with the expectation on the input type.

Admitted matrix-gradient contractions lower by

\[
\left\langle\frac{uv^T}{n},\frac{pq^T}{n}\right\rangle_F
=\left(\frac{u^Tp}{n}\right)\left(\frac{v^Tq}{n}\right),
\qquad \langle B,C\rangle_F=\operatorname{tr}(B^TC).
\]

Thus no unnormalized hidden-coordinate sum is introduced.

## 3. Exact physical automatic differentiation

Here $D$ differentiates the actual finite-dimensional program at fixed $n$.
Differentiate the realized function with respect to its parameter coordinates
or other declared inputs, then evaluate at the sampled parameter values.
No sampling law is varied.

For one directional derivative, first evaluate the direction at the base
state and hold it fixed in that derivative. If $\delta u=Du[\delta\theta]$
and $\delta s=Ds[\delta\theta]$, the local rules are

\[
\begin{aligned}
\delta F(u;s)&=\sum_j F_{u^j}(u;s)\odot\delta u^j
                  +\sum_b F_{s_b}(u;s)\,\delta s_b,\\
\delta\left[\frac1n\sum_iF(u_i;s)\right]
 &=\frac1n\sum_i\left[\sum_jF_{u^j}(u_i;s)\delta u_i^j
                       +\sum_bF_{s_b}(u_i;s)\delta s_b\right],\\
\delta(Ah)&=(\delta A)h+A\delta h,\\
\delta(A^Tu)&=(\delta A)^Tu+A^T\delta u.
\end{aligned}
\]

Scalar arithmetic has its ordinary product and sum rules. In the first line,
$\odot$ denotes componentwise multiplication; scalar terms are broadcast.
Represented matrix directions are finite sums $cuv^T/n$. Their derivatives
remain represented sums because

\[
\delta(cuv^T/n)
=(\delta c)uv^T/n+c(\delta u)v^T/n+cu(\delta v)^T/n.
\]

### Reverse accumulation and ambient gradients

For a scalar output $O$, store normalized vector adjoints
$b_u=n\,\partial O/\partial u\in\mathbb R^n$ and scalar adjoints
$a_s=\partial O/\partial s\in\mathbb R$. Initialize $a_O=1$ and every
other adjoint to zero. Visit instructions in reverse order and **add** each
contribution, including every reuse of a node or matrix.

| Primal instruction | Contributions, one per argument |
| --- | --- |
| $v=F(u;s)$ | $b_{u^j}\mathrel{+}=b_v\odot F_{u^j}$; $a_{s_b}\mathrel{+}=n^{-1}\sum_i b_{v,i}F_{s_b}(u_i;s)$ |
| $t=n^{-1}\sum_iF(u_i;s)$ | $b_{u^j}\mathrel{+}=a_tF_{u^j}$; $a_{s_b}\mathrel{+}=a_t n^{-1}\sum_iF_{s_b}(u_i;s)$ |
| $v=Au$ | $b_u\mathrel{+}=A^Tb_v$; $\nabla_AO\mathrel{+}=b_vu^T/n$ |
| $v=A^Tu$ | $b_u\mathrel{+}=Ab_v$; $\nabla_AO\mathrel{+}=ub_v^T/n$ |

For example, the last two rows follow by matching
$dO=b_v^Tdv/n$ to $\langle\nabla_AO,dA\rangle_F+b_u^Tdu/n$.
Use the ordinary scalar reverse rules for scalar arithmetic.

Compute an ambient current-matrix gradient with $A$ treated as the current
parameter before substituting its stored representation. Differentiating the
representation with respect to historical update factors computes a different
pullback. When the requested derivative is through the training history,
differentiate that history explicitly; do not confuse the two requests.

With mobility $n\kappa$ on a vector parameter, its gradient-flow velocity is
$-\kappa b_u$. With mobility $\kappa$ on a matrix parameter, its velocity is
$-\kappa\nabla_A\mathcal L$, a represented sum. Here the $b$'s are computed
for the stated loss $\mathcal L$, and $\kappa$ is fixed. In particular,

\[
n\,\nabla_uO^T\nabla_uS=\frac{(b_u^O)^Tb_u^S}{n}.
\]

A fixed number of gradient updates preserves the representation. Its number
of terms can grow with that fixed update count.

### Higher jets and a moving gradient direction

Use factorial-normalized physical-time coefficients

\[
u_{[r]}=\frac1{r!}\left.\frac{d^ru(t)}{dt^r}\right|_{t=0}.
\]

For a fixed requested order $R$, work in truncated polynomials through
$t^R$. Emit convolution products and the finite Taylor rule

\[
\begin{aligned}
(uv)_{[r]}&=\sum_{a+b=r}u_{[a]}v_{[b]},&
(Au)_{[r]}&=\sum_{a+b=r}A_{[a]}u_{[b]},\\
\phi(u)_{[r]}&=[t^r]\sum_{k=0}^r\frac{\phi^{(k)}(u_{[0]})}{k!}
                   \left(\sum_{j=1}^ru_{[j]}t^j\right)^k.
\end{aligned}
\]

The $k=0$ term is interpreted as the constant $\phi(u_{[0]})$.
Finite Taylor's theorem justifies this rule for smooth $\phi$; analyticity
is unnecessary. Averages act coefficientwise. Mixed derivatives use a
multivariate truncated polynomial with declared truncation orders.

For a state $\theta$ satisfying $\dot\theta=V(\theta)$, initialize
$\theta_{[0]}$ and recursively emit

\[
(r+1)\theta_{[r+1]}=[t^r]V\left(\sum_{j=0}^{r}\theta_{[j]}t^j\right).
\]

Every state-dependent coefficient in $V$ participates. At second order,

\[
\left.\frac{d^2}{dt^2}O(\theta(t))\right|_0
=D^2O(\theta_0)[V(\theta_0),V(\theta_0)]
 +DO(\theta_0)[DV(\theta_0)[V(\theta_0)]].
\]

The Hessian term alone is the second derivative along the straight line
$\theta_0+tV(\theta_0)$. The second term records motion of the vector field.
For any observable jet, multiply coefficient $O_{[r]}$ by $r!$ to recover
the ordinary derivative.

## 4. Two derivative operations with distinct meanings

| Operation | Differentiated object | Held fixed | Role |
| --- | --- | --- | --- |
| Physical $D$, or $d/dt$ | Actual finite-width parameter/input program | The sampling law and width $n$; a direction only when a single Fréchet derivative specifies it as fixed | Produces the exact differentiated primitive graph |
| Formal $\partial_{\xi_r}$, $\partial_{\zeta_s}$ | Explicit scalar representative as a function of named Gaussian source coordinates | Every already-computed expectation, covariance entry and scalar coefficient | Produces response coefficients during Gaussian evaluation |

Physical differentiation propagates through finite-width averages and their
scalar feedback. Formal source differentiation holds their already-computed
limiting scalar values fixed. The latter is a local rule in a symbolic
expression, not the derivative of the Gaussian measure or of its covariance.

For example, if an earlier scalar value is $c$ and a field is
$H=c\phi(\zeta_1+\zeta_2)$, then

\[
\partial_{\zeta_1}H=c\phi'(\zeta_1+\zeta_2)
\]

even if $c$ was obtained from an expectation involving those sources.
Differentiate through any explicit source dependence in earlier matrix
outputs and coordinate nodes. Do not differentiate $c$, a covariance square
root, or an expectation node in this operation.

## 5. State of the Gaussian evaluator

For each type maintain its declared root tuple and scalar representatives of
all emitted vector nodes. For each **oriented** named matrix group, maintain
an ordered list of source names and their covariance entries. For each named
matrix maintain both lists of past inputs and outputs. Also maintain an
ordered table of deterministic expectation nodes.

Coordinate maps act on scalar representatives using earlier scalar values.
A normalized average on type $\tau$ emits

\[
s=\mathbb E_\tau F(U^1,\ldots,U^k;t),
\]

where $U^j$ are representatives of the inputs and $t$ consists of earlier
deterministic scalar values. Scalar addition and multiplication remain those
operations. Roots retain their declared laws.

Within an oriented source group, covariances are computed by the next rules.
Different oriented groups—including the two orientations of one $W$—and
the original roots are independent Gaussian groups. This is a statement about
the **sources**. The actual output fields generally depend on other groups
through their response terms and need not be independent.

## 6. Emit a matrix call and its response

Write earlier forward calls to $W$ as $y_r=Wh_r$ and earlier reverse calls
as $v_s=W^Tu_s$. Their scalar inputs are $H_r,U_s$, their scalar outputs
are $Y_r,V_s$, and their named sources are $\xi_r,\zeta_s$.

**New forward input $h$, representative $H$.** Append a new centered
upper-type Gaussian source $\xi$ with

\[
\operatorname{Var}(\xi)=\mathbb E_{\rm lower}H^2,
\qquad
\operatorname{Cov}(\xi,\xi_r)=\mathbb E_{\rm lower}[HH_r].
\]

For every earlier reverse call compute its formal source derivative and emit
the coefficient $\mathbb E_{\rm lower}[\partial_{\zeta_s}H]$. Return

\[
Y=\xi+\sum_{s\text{ earlier reverse}}U_s\,
                       \mathbb E_{\rm lower}[\partial_{\zeta_s}H].
\]

**New reverse input $u$, representative $U$.** Append a new centered
lower-type Gaussian source $\zeta$ with

\[
\operatorname{Var}(\zeta)=\mathbb E_{\rm upper}U^2,
\qquad
\operatorname{Cov}(\zeta,\zeta_s)=\mathbb E_{\rm upper}[UU_s].
\]

For every earlier forward call compute
$\mathbb E_{\rm upper}[\partial_{\xi_r}U]$. Return

\[
V=\zeta+\sum_{r\text{ earlier forward}}H_r\,
                          \mathbb E_{\rm upper}[\partial_{\xi_r}U].
\]

The input Gram, not the centered input covariance, determines each source
covariance. Thus a constant input $H=1$ gives variance one. Only earlier
opposite-orientation calls contribute to the response; an absent source
has formal derivative zero. Paths through other matrices remain in the
explicit input expression and are differentiated.

All required integrands use existing fields and already computed coefficients.
The newly appended covariance is a positive semidefinite Gram extension.
These two facts make the construction causal.

## 7. Singular laws and preservation of exact identities

Keep a distinct formal source argument for each emitted call, even when the
joint Gaussian law is supported on a proper subspace. Compute source partials
in these named arguments **before** evaluating an expectation on that support.

For example, duplicate inputs $H_1=H_2=1$ give

\[
\operatorname{Cov}\begin{pmatrix}\xi_1\\\xi_2\end{pmatrix}=
\begin{pmatrix}1&1\\1&1\end{pmatrix},\qquad \xi_1=\xi_2\quad\text{almost surely}.
\]

For $F=\phi(\xi_1+\xi_2)$, the two formal
partials are each $\phi'(\xi_1+\xi_2)$. One may evaluate their expectations
as $\mathbb E\phi'(2G)$, $G\sim N(0,1)$, after computing them. Replacing
both source slots by $G$ before differentiation loses their separate roles.

Likewise, $F=\phi(\xi_1)-\phi(\xi_2)$ is zero almost surely on this support,
but its two formal partials are $\phi'(\xi_1)$ and $-\phi'(\xi_2)$.
For a subsequent reverse call the two response contributions cancel because
the original forward inputs agree; its source variance is also zero. The
output therefore remains exactly zero in the Gaussian evaluator.

No covariance inverse, pseudoinverse or artificial diagonal noise is an
evaluation rule. A Gaussian integral with singular covariance is legitimate.
For a centered Gaussian vector $G$ of covariance $K$, one may use $G=BZ$
with $BB^T=K$ and a standard Gaussian vector $Z$ to evaluate it.
The matrix $B$ is an integration device and is not differentiated by the
formal source rule. Deterministic linear identities, including duplicate and
zero calls, are preserved by the source Gram and matching response sums.

## 8. Output as an expectation DAG and the optional moment normal form

Collect every emitted expectation into an acyclic list

\[
I_j=\int F_j(g;I_1,\ldots,I_{j-1})\,
 N(0,K_j(I_1,\ldots,I_{j-1}))(dg),
\qquad O_*=P(I_1,\ldots,I_N).
\]

Root means are deterministic shifts inside $F_j$. Every dimension,
integrand and covariance entry is fixed by the graph. $P$ is polynomial
because the scalar language uses averages, sums and products. The master
theorem yields $\mathbb E|O_n-O_*|^p\to0$ for every finite $p\ge1$,
including the expectation limit. This is an asymptotic conclusion following
exact finite-width compilation; the Gaussian evaluator is not an exact
finite-$n$ replacement.

For the initialization subclass in master-proof Section 8, all nonlinear
arguments are literal original feedforward preactivations. Its optional
normal form reduces Gaussian polynomial factors using

\[
\mathbb E[G_iF(G)]=\sum_jK_{ij}\mathbb E[\partial_jF(G)],
\qquad G\sim N(0,K).
\]

This identity also holds for singular $K$: substitute $G=BZ$ and apply
one-dimensional Gaussian integration by parts to each independent coordinate
of $Z$. Polynomial growth gives integrable terms and vanishing boundary
terms. Each reduction removes one explicit Gaussian factor, so it terminates
in activation-derivative moments with recursively computed covariances.
Do not apply this restricted normal-form claim to arbitrary nonlinearities
of derivative fields or trained fields. The general expectation DAG still
applies whenever the primitive-language contract holds.

## 9. Scope checks before applying the theorem

Reject a graph that requires cross-type coordinate products, unidentified
matrix reuse, arbitrary dense matrix directions, unrestricted tensor-index
contractions, coordinate selection, inverse operations, width-dependent
coefficients, or growing graph length/order/update count. Do not treat a
derivative of an unspecified sampling law as an admitted primitive.

For an admitted graph, record the scalar observable, root and matrix laws,
all normalizations, physical mobilities, derivative convention and requested
fixed order. If vectors are retained, state convergence through their joint
empirical laws or normalized observables; a vector's individual coordinates
are not asserted to converge to a deterministic constant. Finite flow jets
do not assert convergence of an infinite Taylor series, a uniform existence
horizon, or reconstruction at positive time.
