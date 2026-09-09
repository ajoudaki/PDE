# Superseded draft

The canonical completed remainder note is
../temporary_quantitative_width_first_rung3/REMAINDER.md. The material below
is retained only as an earlier construction draft and must not be cited as
the final rung-three statement.

# The three-versus-one rung

This note isolates the genuinely new part of the comparison

$$
\Delta_{31}(h)=F_3(h)-F_1(3h).
$$

It uses exactly the finite network, normalization, initialization, and
simultaneous ascent update in `PROOF.md`.  In particular, a subscript on
$F$ counts recomputed Euler steps and not a power of an operator.

## 1. Recursive fixed-step operator DAG

The following recursion is the convenient form of the width-first program.
It also makes clear which matrix actions have to be identified at finite
width.

Put $H_0=\phi(U)$, where $U\sim N(0,1)$.  Suppose that
$H_0,\ldots,H_s$ and $C_0,\ldots,C_{s-1}$ have already been constructed.
Write

$$
Q^{[s]}_{rt}=\mathbb E[H_rH_t],\qquad 0\le r,t\le s.
$$

Let $A\sim N(0,1)$ be independent of
$\xi^{[s]}=(\xi_0,\ldots,\xi_s)\sim N(0,Q^{[s]})$.  In this joint block,
recompute all earlier top variables and define

$$
z_s=\xi_s+\sum_{r<s}L_{sr}C_r,
\qquad
L_{sr}=\rho_{sr}+hQ^{[s]}_{rs},
$$

$$
a_s=A+h\sum_{r<s}\phi(z_r),
\qquad
C_s=a_s\phi'(z_s).
$$

For a nonterminal top stage define

$$
K^{[s]}_{rt}=\mathbb E[C_rC_t],
\qquad
\sigma_{sr}=\mathbb E[\partial_{\xi_r}C_s],
\qquad 0\le r,t\le s.
$$

Let $\chi^{[s]}=(\chi_0,\ldots,\chi_s)\sim N(0,K^{[s]})$ be independent
of $U$.  In this joint lower block, recompute the earlier lower variables and
put

$$
b_s
=\chi_s+\sum_{r\le s}\sigma_{sr}H_r
 +h\sum_{r<s}K^{[s]}_{rs}H_r,
$$

$$
u_{s+1}=u_s+hb_s\phi'(u_s),
\qquad
H_{s+1}=\phi(u_{s+1}),
$$

$$
\rho_{s+1,r}=\mathbb E[\partial_{\chi_r}H_{s+1}],
\qquad 0\le r\le s.
$$

The convention $\sigma_{00}=0$ follows directly from
$\mathbb E[A\phi''(\xi_0)]=0$.  Starting at $s=0$ and iterating through
$s=2$ constructs $H_1,C_1,H_2,C_2,H_3$.  The terminal value is

$$
F_3(h)=\mathbb E[a_3\phi(z_3)].
$$

At finite width, this is the seven-action reveal order

$$
Y^0,D^0,Y^1,D^1,Y^2,D^2,Y^3,
\qquad
Y^s=WH^s/\sqrt n,quad D^s=W^TC^s/\sqrt n.
$$

The exact learned-matrix identities are, for $0\le s\le3$ and
$0\le s\le2$, respectively,

$$
z^s=Y^s+h\sum_{r<s}Q^{(n)}_{rs}C^r,
$$

$$
b^s=D^s+h\sum_{r<s}K^{(n)}_{rs}H^r.
$$

Thus no rank-one term is lost in the recursion.

## 2. Reused-matrix response identity for all seven actions

The adaptive Gaussian-conditioning lemma in `PROOF.md` applies verbatim to
any finite number of predictable row and column queries.  What must be added
for the present rung is the following response calculation; it replaces six
separate appeals to an unspecified cavity induction.

Assume all actions before a new row query have already been identified, and
collect the old fields into vectors $H,C,Y,D$.  There are deterministic
strictly triangular response matrices $R,S$ such that, at a representative
coordinate,

$$
Y=\xi+RC,
\qquad
D=\chi+SH,
$$

where $\xi\sim N(0,Q)$ and $\chi\sim N(0,K)$.  Let $H_+$ be the new row
query, put

$$
q=\mathbb E[HH_+],
\qquad
\rho=\mathbb E[\nabla_\chi H_+].
$$

Gaussian integration by parts gives, entry by entry,

$$
\mathbb E[CY^T]=S^TQ+KR^T,
\qquad
\mathbb E[DH_+]=K\rho+S^Tq.
$$

Substitution in the exact row-conditioning formula gives the direct
$C$-coefficient

$$
\rho-R^TQ^{-1}q.
$$

The separate projection of the new action on $Y$ contributes
$R^TQ^{-1}q$.  These two terms cancel, leaving exactly $\rho$.  Hence

$$
Y_+=\xi_++\rho^TC.
$$

Transposing the argument gives the column identity

$$
D_+=\chi_++\sigma^TH,
\qquad
\sigma=\mathbb E[\nabla_\xi C_+].
$$

This calculation includes the dependence of every later $H_j$ on every
reused column action; it does not treat a query as independent of the column
that generated it.

For a fixed nonzero $h$, once the nonterminal population query Grams are
positive definite, the stopped normalized-$L^p$ coupling from `PROOF.md`
extends from five to seven actions as follows.  Use the same good-event
invariant at each of the seven displayed actions, append the new empirical
Gram entries and cross-moments to the invariant, and append one independent
Gaussian residual to the joint Gram--Schmidt block.  Rosenthal's inequality
controls each newly appended empirical average; the inverse identity and
the positive population eigenvalue control its regression coefficients; the
projection estimate controls the residual; and the polynomial-Lipschitz
transfer estimate controls the following coordinate update.  There are
exactly seven repetitions.  The raw-energy recursion in `PROOF.md` is run
for $s=0,1,2$ and the terminal bounds are formed at $s=3$.  It is a finite
polynomial in the same Gaussian energy variable, so the arbitrary-moment
bad-event estimate removes stopping and supplies uniform integrability of
$n^{-1}\sum_i a_i^3\phi(z_i^3)$.  Consequently the seven-action recursion,
not an independently postulated Gaussian program, is the pointwise
fixed-$h$ limit whenever the rank condition in Section 4 below holds.

## 3. Finite activation-only fifth-derivative compiler

Use the envelope-pair arithmetic, formal product/chain differentiation,
singular Price recursion, Gaussian moment function $\mu_{m,p}$, covariance
constructor, response constructor, and $L=\rho+hQ$ constructor of Section 6
of `PROOF.md`, unchanged.  Extend its chronological list by precisely two
passes:

1. after the existing second top pass has constructed
   $C_0,C_1,C_2$, all $K^{[2]}_{rs}$, and all $\sigma_{2r}$, form the lower
   covariance $\operatorname{diag}(1,K^{[2]})$ and compile
   $H_3,Q^{[3]}_{r3},\rho_{3r},L_{3r}$ for $0\le r\le2$;
2. form the top covariance $\operatorname{diag}(1,Q^{[3]})$, construct
   $z_3,a_3$, and compile $F_3=\mathbb E[a_3\phi(z_3)]$.

For every covariance node $G$ set, as before,

$$
\bar c_j(G)=\sum_{r,t}\overline{\mathcal J}_j(G_{rt}),
\qquad 0\le j\le5.
$$

Every earlier scalar derivative is a coefficient token and receives its
already compiled numerical bound.  The reachable Price indices remain

$$
r+j+\left\lceil\frac{s}{2}\right\rceil\le5.
$$

There are six chronological Gaussian nodes and a finite number of response
nodes, so this recursion terminates.  A response integrand initially contains
at most $\phi''$; the reachable set takes at most ten spatial derivatives.
Thus no derivative above $\phi^{(12)}$ occurs.  The largest Gaussian block
has dimension five, so the only change in the explicit moment formula is
that $\mu_{m,p}$ is used for $m\le5$ instead of $m\le4$.

Denote the returned numerical output bounds by

$$
\overline{\mathcal J}_{3,j}
\ge \sup_{|h|\le1}|F_3^{(j)}(h)|,
\qquad 0\le j\le5,
$$

and retain $\overline{\mathcal J}_{1,j}$ from the first top node.  These
numbers are syntactic functions of $M_\phi$ and the explicit Gaussian moment
formula; they are not defined from an output supremum.  The singular Price
lemma therefore proves $F_1,F_3\in C^5([-1,1])$.

## 4. Explicit three-time rank radius using only five derivatives

The new nonterminal Grams are

$$
Q^{[2]}=(Q_{rs})_{0\le r,s\le2},
\qquad
K^{[2]}=(K_{rs})_{0\le r,s\le2}.
$$

For either $G=Q^{[2]}$ or $G=K^{[2]}$, and $a,b\in\{0,1,2\}$, define the
forward-difference numerator

$$
N^G_{ab}(h)
=\sum_{r=0}^a\sum_{s=0}^b
(-1)^{a-r+b-s}\binom ar\binom bsG_{rs}(h).
$$

Nodewise differentiation of the recursive DAG gives

$$
(N^G_{ab})^{(j)}(0)=0,
\qquad 0\le j<a+b.
$$

This is also a finite compiler check: construct the exact Price derivative
expression for each of the $18$ pairs $(G,a,b)$ and reduce it by the product
and chain rules.  No limiting output occurs in this calculation.

Define the explicit desingularized jet Gram

$$
\widehat G_{ab}(0)
=\frac{(N^G_{ab})^{(a+b)}(0)}{(a+b)!}.
$$

Each entry is a finite Gaussian integral of $\phi$ and its derivatives.
Equivalently, for $h\ne0$, let

$$
T_h=
\begin{pmatrix}
1&0&0\\
-h^{-1}&h^{-1}&0\\
h^{-2}&-2h^{-2}&h^{-2}
\end{pmatrix}.
$$

Then

$$
\widehat G(h)=T_hG(h)T_h^T,
\qquad
\widehat G_{ab}(h)=\frac{N^G_{ab}(h)}{h^{a+b}},
$$

and the displayed formula defines its continuous value at zero.

Let the compiler's entrywise derivative majorants be
$\bar G_{rs,j}$.  Put

$$
e^G_{ab}
=\frac1{(a+b+1)!}
\sum_{r=0}^a\sum_{s=0}^b
\binom ar\binom bs\bar G_{rs,a+b+1},
$$

$$
E_G=\left(\sum_{a,b=0}^2(e^G_{ab})^2\right)^{1/2},
\qquad
\lambda_G=\lambda_{\min}(\widehat G(0)).
$$

Taylor's integral formula, divided by $h^{a+b}$, gives for every
$0<|h|\le1$,

$$
\left|
\widehat G_{ab}(h)-\widehat G_{ab}(0)
\right|
\le e^G_{ab}|h|.
$$

Therefore

$$
\|\widehat G(h)-\widehat G(0)\|_{\mathrm{op}}
\le E_G|h|.
$$

Assume the explicit activation nondegeneracy condition

$$
\lambda_Q>0,
\qquad
\lambda_K>0.
$$

Define

$$
r_G=min\left\{1,\frac{\lambda_G}{2(1+E_G)}\right\},
\qquad G\in\{Q,K\},
$$

and

$$
h_{31}=\min\{1/3,r_Q,r_K\}.
$$

Weyl's inequality yields

$$
\lambda_{\min}(\widehat G(h))\ge\lambda_G/2>0
$$

for $0<|h|\le h_{31}$.  Since $T_h$ is invertible, $G(h)$ is positive
definite.  Its earlier one- and two-time principal Grams are consequently
positive definite as well.  This proves every nonterminal rank hypothesis
needed by the seven-action conditioning argument.  Notice that only fifth
derivatives were used: the apparent sixth-order zero of $\det G$ was removed
before estimating the remainder.

The restriction $h_{31}\le1/3$ ensures both $|h|\le1$ for the $F_3$
compiler and $|3h|\le1$ for the $F_1$ compiler.  All estimates use $|h|$,
so the same radius covers negative step sizes.

## 5. Cubic coefficient

Direct differentiation of the Gaussian DAG, with the covariance derivatives
handled by Price's formula, gives for every fixed integer $k$ the third-jet
identity

$$
F_k'''(0)
=\frac{k(4k^2-3k+1)}2S_\phi
 +2k(k-1)(2k-1)H_\phi.
$$

Here $S_\phi$ and $H_\phi$ are the explicit nine-moment activation
polynomials in Section 8 of `PROOF.md`.  The identity is obtained node by
node as follows.  At order three, repeated Euler substitution produces four
chain-rule tree shapes.  Their Gaussian Price evaluations are, in order,

$$
H_\phi,qquad S_\phi,qquad H_\phi,qquad S_\phi.
$$

The numbers of occurrences after $k$ recomputed steps are respectively

$$
6\binom{k}{3},qquad
\frac{k(k-1)(2k-1)}2,qquad
6k\binom{k}{2},qquad
k^3.
$$

Summing the two $H_\phi$ counts and the two $S_\phi$ counts gives the
displayed formula.  This calculation is internal to the already identified
operator DAG; it does not Taylor expand a finite-width network or exchange
the width and learning-rate limits.

In particular,

$$
F_1'''(0)=S_\phi,
\qquad
F_3'''(0)=42S_\phi+60H_\phi.
$$

The same first-order node calculation gives

$$
F_k'(0)=k(1+d+d^2).
$$

Consequently the linear term of $F_3(h)-F_1(3h)$ vanishes and

$$
\kappa_{31,\phi}
=\frac{F_3'''(0)-27F_1'''(0)}6
=\frac52S_\phi+10H_\phi
=\frac52(S_\phi+4H_\phi).
$$

## 6. Quantitative remainder

The same sign transformation used for one and two steps extends
inductively through the recursive DAG: under $h\mapsto-h$, change the signs
of $A$ and the complete lower Gaussian block $\chi$.  Every $Q,K$ remains
even, every response and $L$ remains odd, every preactivation remains
unchanged, and every $a_s,C_s$ changes sign.  Hence every $F_s$ is odd on
$[-1,1]$.  Thus $\Delta_{31}$ is odd and

$$
\Delta_{31}(0)=\Delta_{31}''(0)=\Delta_{31}^{(4)}(0)=0.
$$

Define the activation-only number

$$
B_{31,\phi}
=\frac{
\overline{\mathcal J}_{3,5}
+3^5\overline{\mathcal J}_{1,5}}
{120}.
$$

For $|t|\le h_{31}$,

$$
|\Delta_{31}^{(5)}(t)|
\le
\overline{\mathcal J}_{3,5}
+3^5\overline{\mathcal J}_{1,5}.
$$

Taylor's integral formula through order four therefore proves

$$
\left|
F_3(h)-F_1(3h)-\kappa_{31,\phi}h^3
\right|
\le B_{31,\phi}|h|^5,
\qquad |h|\le h_{31}.
$$

For every $\varepsilon>0$, it follows that

$$
|F_3(h)-F_1(3h)|
\le (|\kappa_{31,\phi}|+\varepsilon)|h|^3
$$

whenever

$$
|h|
\le
\min\left\{
h_{31},
\sqrt{\frac{\varepsilon}{1+B_{31,\phi}}}
\right\}.
$$

If $d=0$, then $\phi\equiv\pm1$, $F_k(h)=kh$, and the discrepancy is
identically zero.  One may take
$\kappa_{31,\phi}=B_{31,\phi}=0$ and $h_{31}=1/3$.

## 7. Exact status and the four-versus-two alternative

Everything above is activation-explicit once
$\lambda_Q,\lambda_K>0$ is assumed.  A universal theorem over every
nonconstant activation in the stated $C^{12}$ class additionally requires a
proof that the two explicit desingularized $3\times3$ jet Grams are always
positive definite, or a separate fixed-step conditioning proof on their
lower-rank strata.  The two-step proof in `PROOF.md` does not establish this
new fact.  Until one of those alternatives is supplied, removing the stated
activation nondegeneracy is open; it must not be hidden inside an existential
radius.

For comparison, the formal four-versus-two constants are

$$
\kappa_{42,\phi}=3(S_\phi+4H_\phi),
$$

$$
B_{42,\phi}
=\frac{
\overline{\mathcal J}_{4,5}
+2^5\overline{\mathcal J}_{2,5}}
{120}.
$$

That rung needs positive four-time query Grams.  Forward-difference
desingularization then has indices $0,1,2,3$ and denominators as large as
$h^6$; an explicit perturbation radius requires seventh covariance
derivative bounds.  The same envelope compiler at order seven uses activation
derivatives through $\phi^{(16)}$.  Thus the three-versus-one comparison is
the rung that remains within the original $C^{12}$ envelope.
