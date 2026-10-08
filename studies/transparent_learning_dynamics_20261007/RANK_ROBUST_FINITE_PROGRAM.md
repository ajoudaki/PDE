# Rank-robust aggregate law for a finite clipped Gaussian-query program

Status: complete proof candidate, frozen for the supervisor's check on 2026-10-07. This establishes a qualitative finite-program result for the grammar below. It does not establish the unclipped neural flow, a quantitative width rate, a continuum-time limit, or an all-time approximation.

Notation clarification only: initial deterministic constant vector registers are broadcasts $c\mathbf1_n$, not coordinate-dependent deterministic arrays. The pre-clarification frozen SHA-256 was baf872d95919981848b0b0d7958b737426feffb6a29508d7ea1870365c815f62. This makes the coordinate symmetry already used in the proof explicit; no theorem qualification changed.

Scientific inputs: the supervisor's new self-contained assignment and this route's own frozen CAUSAL_GAUSSIAN_ROUTE.md. No other route, book, study history, code, literature, or experiment was consulted. In particular, I did not read the optionally permitted ADAPTIVE_SIGNAL_CONCENTRATION.md. Required skills and process instructions were already read and remain current.

The omission argument works without a stable-rank hypothesis. A necessary extra step is supplied here: normalized Euclidean comparison alone would not transfer arbitrary polynomial moments to the original program. Gaussian concentration, exchangeability and bounded query inputs provide uniform moments of every order for its raw matrix outputs; interpolation then completes that transfer.

## 1. Allowed finite program and theorem

Fix a finite collection of populations, each containing $n$ coordinates, a finite collection of directed matrix connections between those populations, and a finite deterministic list of instructions. None of those counts depends on $n$.

For connection $e$ from population $s(e)$ to population $t(e)$, let

\[
G_e=\frac1{\sqrt n}J_e,\qquad (J_e)_{ij}\overset{\mathrm{iid}}{\sim}N(0,1).
\]

All these matrices are independent. Each population may also have finitely many Gaussian seed registers: their coordinate rows are independent copies of a fixed finite centered Gaussian vector, independently across populations and independently of all matrices. Singular seed covariance is permitted. Fixed scalar constants and their broadcast vector registers $c\mathbf1_n$ are also permitted.

A vector register belongs to one population. A scalar register is common to the program. Its allowed instructions are:

1. **Coordinate operation.** From finitely many existing vector registers $v^1,\ldots,v^k$ in one population and finitely many scalar registers $s$, form
   \[
   u_i=F(v_i^1,\ldots,v_i^k,s),
   \]
   with one fixed globally Lipschitz function $F$ used at every coordinate. The output need not be bounded.
2. **Empirical scalar reduction.** Form
   \[
   a=\frac1n\sum_{i=1}^n \psi(v_i^1,\ldots,v_i^k,s),
   \]
   where $\psi$ is fixed, bounded and globally Lipschitz.
3. **Scalar operation.** Apply a fixed globally Lipschitz function to finitely many existing scalar registers.
4. **Gaussian query.** Form $u=G_e h$ or $u=G_e^\top d$, with the input in the appropriate population. Every query input is uniformly bounded coordinatewise by a deterministic constant attached to that instruction. This is an algebraic bound for arbitrary values of earlier registers, so it holds in the modified simulator too. A preceding componentwise clipping operation ensures this condition.

All scalar constants, seed covariances, functions, Lipschitz constants, clipping bounds and the instruction list are fixed independently of $n$. Functions may depend on the given finite dataset, labels and time mesh. Coordinate-index masks, dimension-dependent amplifications, discontinuous tests, arbitrary matrix-entry inspections and empirical Gram inverses are not instructions in this grammar. Adaptivity means that each query input can depend on all preceding allowed computations. Reuse of a matrix in both directions is allowed arbitrarily often within the finite list.

Because reductions are bounded, all scalar registers have deterministic finite bounds depending only on the finite program. Coordinate operations can have unbounded outputs; their global Lipschitz constants are essential. A product of clipped variables is allowed by writing it as a globally Lipschitz function on the full input space. This includes fixed finite Euler programs in which the queried features and backward signals are clipped and every coordinate product is expressed through bounded factors. It does not silently include an unclipped product such as $w\phi'(z)$.

Let $V_i^{(r,n)}$ be the finite row vector collecting every vector register produced in population $r$ by the original program. Its empirical law is

\[
\mu_{r,n}=\frac1n\sum_{i=1}^n\delta_{V_i^{(r,n)}}.
\]

**Theorem.** For every fixed program in this grammar, there are deterministic probability laws $\mu_r$ and deterministic limits of all scalar registers, defined by the causal scalar construction in Section 2, such that, for every population $r$ and every continuous function $\Psi$ with at most polynomial growth,

\[
\frac1n\sum_{i=1}^n\Psi(V_i^{(r,n)})
\ \longrightarrow\
\int\Psi\,d\mu_r
\qquad\text{in probability}.
\tag{1}
\]

The laws have moments of every finite order. No assumption is made on the ranks of the matrix-query histories or their limiting Gram matrices. Zero query innovations, zero labels, repeated queries and singular seed covariances are included.

This is a pointwise theorem for each fixed finite program and its fixed coefficients. It asserts no uniform convergence rate as labels or coefficients approach degeneracy. The aggregate construction contains finitely many scalar Gaussian innovations and moment coefficients, with counts independent of $n$; it contains no dense initialization or realized dense trajectory.

## 2. The deterministic causal scalar construction

Keep the joint law of all scalar coordinate registers separately in each population. Initial laws are their specified Gaussian seed laws. Coordinate operations act on the appropriate law. An empirical scalar reduction is replaced by its expectation, and scalar operations act on already computed deterministic scalars.

For each matrix $G$, retain selected forward queries and selected backward queries. The retained scalar histories are denoted by

\[
H=(H_1,\ldots,H_r)^\top,\quad Y=(Y_1,\ldots,Y_r)^\top,\qquad
D=(D_1,\ldots,D_s)^\top,\quad X=(X_1,\ldots,X_s)^\top.
\]

Here $H$ and $X$ belong to the input population of $G$, while $Y$ and $D$ belong to its output population. The histories correspond to the identities $GH_j=Y_j$ and $G^\top D_j=X_j$ at finite width. Expectations involving variables from one population use that population's joint law. No coordinatewise pairing between distinct populations is used.

For a new forward input $h$, define

\[
\Gamma_H=\mathbb E[HH^\top],\qquad
a=\Gamma_H^{-1}\mathbb E[Hh],\qquad
e=h-H^\top a,\qquad \sigma^2=\mathbb E[e^2].
\tag{2}
\]

With no retained forward history, the linear combination is zero and $e=h$. Empty inverses and products below have their zero-dimensional meaning.

* If $\sigma^2=0$, define the new output by $y=Y^\top a$ and do not add a retained query.
* If $\sigma^2>0$, set
  \[
  q=\Gamma_D^{-1}\mathbb E[Xe],\qquad
  y=Y^\top a+D^\top q+\sigma Z,
  \tag{3}
  \]
  where $Z\sim N(0,1)$ is independent of all existing scalar registers in the output population. Append $h,y$ to the retained forward histories.

For a new backward input $d$, define

\[
\Gamma_D=\mathbb E[DD^\top],\qquad
b=\Gamma_D^{-1}\mathbb E[Dd],\qquad
e'=d-D^\top b,\qquad \tau^2=\mathbb E[(e')^2].
\tag{4}
\]

If $\tau^2=0$, define $x=X^\top b$ and retain nothing. Otherwise define

\[
r=\Gamma_H^{-1}\mathbb E[Ye'],\qquad
x=X^\top b+H^\top r+\tau Z',
\tag{5}
\]

with a fresh scalar standard normal in the input population, and append $d,x$ to the retained backward histories.

These are causal definitions: every expectation uses previously constructed registers, including the currently available query input. The selection of retained queries is deterministic because the population laws are deterministic.

Every retained Gram matrix is positive definite by construction. Indeed, when a new $h$ has positive innovation variance, $\mathbb E[He]=0$ and, for any coefficient vector $u$ and scalar $v$,

\[
\mathbb E[(u^\top H+vh)^2]
=(u+va)^\top\Gamma_H(u+va)+v^2\sigma^2.
\]

This is strictly positive unless $u=v=0$. The backward argument is identical. Thus the displayed inverses exist wherever they are used. No positive lower bound uniform in the program's coefficients is asserted.

All scalar laws have moments of every order, inductively: Gaussian seeds do; globally Lipschitz operations have at most linear growth; and (3) and (5) are finite linear combinations of earlier registers and a Gaussian variable with finite deterministic coefficients. The exact rank decision is part of a mathematical definition. An effective uniform numerical method for deciding zero variance of an arbitrary Gaussian integral is a separate issue.

## 3. Two elementary convergence facts

Use the normalized empirical norms

\[
\|v\|_{p,n}
=\left(\frac1n\sum_i|v_i|^p\right)^{1/p},\qquad 1\leq p<\infty.
\]

The notation extends to rows of finitely many registers by using Euclidean norm within each row.

First, suppose arrays $U_n$ have convergence against all continuous polynomial-growth tests and bounded empirical moments of every order. Suppose also

\[
\|U_n-\widetilde U_n\|_{p,n}\longrightarrow0
\quad\text{in probability for every finite }p.
\tag{6}
\]

Then $\widetilde U_n$ has the same test limits. To see this, restrict both row vectors to a fixed compact ball. On this ball the test is uniformly continuous, and the fraction of rows on which their distance exceeds any fixed positive number tends to zero by (6). Outside the ball, a moment of order strictly greater than the test's polynomial growth bounds the empirical contribution by a negative power of the ball radius. All requisite empirical moments are bounded in probability, using the triangle inequality and (6). Let the width tend to infinity, then the radius tend to infinity and the continuity threshold tend to zero. This proves the assertion.

Second, if $U_n$ has the above test convergence, and $\xi_i$ are conditionally independent standard normals independent of the existing array, then $(U_{n,i},\xi_i)$ converges against every continuous polynomial-growth test to $(U,Z)$ with independent $Z\sim N(0,1)$. Conditional expectation gives the existing empirical average of

\[
\overline\Psi(u)=\mathbb E_Z[\Psi(u,Z)].
\]

This is continuous with polynomial growth by dominated convergence on compact sets and Gaussian moments. Its empirical average has the required limit. The conditional variance of the original average is bounded by

\[
\frac Cn\left(1+\frac1n\sum_i\|U_{n,i}\|^{2k}\right)
\tag{7}
\]

for some finite $C,k$ determined by the test. The factor in parentheses is bounded in probability. Conditional Chebyshev, first restricted to a bounded-moment event, proves the claim. These arguments also prove joint convergence for any finite list of tests and populations.

## 4. A modified finite-width simulator

Run a simulator on the same initial Gaussian matrices and seeds as the original program. It executes every ordinary coordinate and scalar instruction unchanged. Its matrix-query instructions use the deterministic retention decisions from Section 2.

For a retained forward query it computes the actual product $G\widehat h$ and stores the pair $\widehat h,\widehat y$. For a skipped forward query it returns

\[
\widehat y=\widehat Y a,
\tag{8}
\]

where $\widehat Y$ contains its earlier retained forward responses and $a$ is the deterministic population coefficient from (2). In particular, it does not inspect or reveal $G\widehat h$ on a skipped query. The backward rule is the same, with $\widehat Xb$.

It follows exactly that its retained histories satisfy

\[
G\widehat H=\widehat Y,\qquad G^\top\widehat D=\widehat X.
\tag{9}
\]

Skipped outputs and retention decisions reveal no additional constraints on any matrix: they are functions of the existing transcript and deterministic constants. All actual query vectors are predictable from that transcript. This fact is essential to the conditioning argument.

We prove by induction over the instruction list that all simulator population arrays converge against every continuous polynomial-growth test to the laws in Section 2, and all its scalar registers converge to the specified deterministic values.

The initialization follows from the ordinary variance estimate for an empirical average of independent Gaussian rows; every polynomial-growth test has finite variance. Coordinate and scalar operations preserve the claim using their Lipschitz continuity and the first fact in Section 3. For reductions, bounded Lipschitz convergence is already sufficient. A skipped query is a fixed linear combination of existing retained responses, so it also preserves the claim.

It remains to prove the assertion for a retained query.

## 5. Conditioning proves every retained-query induction step

Suppress hats temporarily. Given retained forward constraints $GH=Y$ and backward constraints $G^\top D=X$, let

\[
P_H=H(H^\top H)^\dagger H^\top,\qquad
P_D=D(D^\top D)^\dagger D^\top.
\]

The exact adaptive Gaussian conditional law is

\[
G=M+(I-P_D)\widetilde G(I-P_H),\qquad
M=Y(H^\top H)^\dagger H^\top
  +D(D^\top D)^\dagger X^\top(I-P_H),
\tag{10}
\]

where $\widetilde G$ is conditionally independent with the original independent $N(0,1/n)$ entries.

For completeness, the homogeneous constraint space is precisely the range of the orthogonal projection $B\mapsto(I-P_D)B(I-P_H)$. Compatibility $D^\top Y=X^\top H$ shows that $M$ satisfies both constraints; each term of $M$ is orthogonal to that homogeneous space in the Frobenius inner product. Resolving an isotropic Gaussian vector into these orthogonal subspaces proves (10). Predictability extends this to adaptive queries by induction: each next observation is a fixed linear functional conditional on the past. For multiple independent matrices their unrevealed Gaussian remainders stay conditionally independent; a query observes only its chosen remainder.

The scalar retained histories have positive definite Gram matrices by Section 2. By the empirical moment induction hypothesis, the finite-width retained history Grams are invertible with probability tending to one, and their normalized inverses converge to the deterministic scalar inverses. We work on that event; its complement has probability tending to zero and is immaterial for convergence in probability. The exact formula (10) itself remains valid on the complement with its pseudoinverses.

For a new retained forward input $h$, put

\[
\begin{aligned}
a_n&=(H^\top H/n)^{-1}(H^\top h/n),&
e_n&=h-Ha_n,\\
q_n&=(D^\top D/n)^{-1}(X^\top e_n/n),&
\sigma_n^2&=\|e_n\|_{2,n}^2.
\end{aligned}
\]

The conditioning formula gives

\[
Gh=Ya_n+Dq_n+\sigma_n(I-P_D)\xi,
\tag{11}
\]

where $\xi$ is a conditionally independent standard Gaussian vector. By the induction hypothesis,

\[
a_n\to a,\qquad q_n\to q,\qquad \sigma_n\to\sigma
\quad\text{in probability}.
\tag{12}
\]

The convergence follows from the required input-population and output-population second moments, not from any neuron matching across the two populations.

To remove the noise projection in every finite empirical norm, write

\[
P_D\xi=D\beta_n,\qquad
\beta_n=(D^\top D/n)^{-1}\frac{D^\top\xi}{n}.
\]

Conditional on the past,

\[
\operatorname{Cov}\!\left(\frac{D^\top\xi}{n}\right)
=\frac1n\frac{D^\top D}{n}.
\]

The inverse Gram converges to a finite deterministic matrix, so $\beta_n=O_{\mathbb P}(n^{-1/2})$. Every column of $D$ is a bounded query input; alternatively the induction's empirical moment bounds suffice. Hence, for every finite $p$,

\[
\|P_D\xi\|_{p,n}
\leq\sum_{j=1}^s|\beta_{n,j}|\,\|D_j\|_{p,n}
\longrightarrow0
\quad\text{in probability}.
\tag{13}
\]

The coefficient replacements in (12) also change (11) by $o_{\mathbb P}(1)$ in every such norm, because every prior raw response has bounded empirical moments by induction, and $\|\xi\|_{p,n}=O_{\mathbb P}(1)$. Thus the new register differs, in every finite empirical norm, from

\[
Ya+Dq+\sigma\xi.
\]

The conditional Gaussian averaging fact in Section 3 and its perturbation fact now prove the joint polynomial-test limit of all existing output-population registers and this new register. It is exactly (3).

The backward case uses

\[
G^\top d
=Xb_n+Hr_n+\tau_n(I-P_H)\xi'
\]

and the identical argument. This proves the entire simulator induction, including moments of every order and all singular-history cases removed by deterministic omission.

## 6. The original program is close in normalized Euclidean norm

For all initial matrices let

\[
\Omega_{n,R}=\{\max_e\|G_e\|_{\mathrm{op}}\leq R\}.
\]

For a sufficiently large fixed $R$, its probability tends to one exponentially fast; an elementary proof is given in Section 7.

Couple the original program and simulator through the same matrices and seeds. We claim, by induction, that corresponding vector registers differ by $o_{\mathbb P}(1)$ in $\|\cdot\|_{2,n}$ and corresponding scalar registers differ by $o_{\mathbb P}(1)$. Coordinate and scalar operations and empirical reductions preserve this assertion by their global Lipschitz constants and Cauchy–Schwarz. For a retained query,

\[
\|Gh-G\widehat h\|_{2,n}
\leq R\|h-\widehat h\|_{2,n}
\quad\text{on }\Omega_{n,R}.
\]

For a skipped forward query, the simulator's moment theorem and the vanishing scalar innovation give

\[
\|\widehat h-\widehat H a\|_{2,n}^2
\longrightarrow
\mathbb E[(h-H^\top a)^2]=0.
\tag{14}
\]

Using the exact retained identities (9), the query-output difference is

\[
Gh-\widehat Ya
=G(h-\widehat h)+G(\widehat h-\widehat H a).
\]

Its normalized Euclidean norm is at most

\[
R\|h-\widehat h\|_{2,n}
+R\|\widehat h-\widehat H a\|_{2,n}
=o_{\mathbb P}(1)
\tag{15}
\]

on $\Omega_{n,R}$. The backward skipped-query proof is identical. There are finitely many instructions, so the induction proves the claim for the full original program.

The original program never uses inverse empirical Gram matrices. Their occurrence in (10)–(12) is conditional-law analysis only. Thus a nearly zero history direction cannot be divided by its small norm by an allowed program instruction. This is precisely where the globally Lipschitz grammar makes the omission comparison valid.

## 7. Uniform polynomial moments for the original raw query outputs

This section closes the moment-transfer gap. It uses only bounded query inputs, the specified Gaussian randomness, coordinate symmetry, and the globally Lipschitz finite program.

### 7.1 Gaussian operator norms

An $\varepsilon$-net of the Euclidean unit sphere with $\varepsilon=1/4$ has at most $9^n$ points: choose a maximal separated subset and compare the volumes of disjoint radius-$\varepsilon/2$ balls inside the radius-$(1+\varepsilon/2)$ ball. Approximating both unit vectors in the bilinear variational expression for the operator norm gives

\[
\|G\|_{\mathrm{op}}
\leq2\max_{u,v\text{ in the net}}|u^\top Gv|.
\]

For fixed unit $u,v$, the variable $u^\top Gv$ is $N(0,1/n)$. Its exponential moment gives the two-sided tail bound $2e^{-nt^2/2}$. Taking a union bound therefore yields

\[
\mathbb P(\|G\|_{\mathrm{op}}>R)
\leq 2\exp\left(2n\log9-\frac{nR^2}{8}\right).
\tag{16}
\]

For finitely many matrices, choose one fixed $R$ sufficiently large. Then

\[
\mathbb P(\Omega_{n,R}^c)\leq C e^{-cn},
\tag{17}
\]

and integration of (16) above a fixed sufficiently large threshold proves

\[
\sup_n\mathbb E\|G_e\|_{\mathrm{op}}^q<\infty
\qquad\text{for every finite }q.
\tag{18}
\]

The fixed $R$ may be chosen so that the probability in (17) is at most $1/16$ for every $n$.

### 7.2 A self-contained Gaussian Lipschitz bound

If $Z$ is any finite-dimensional standard Gaussian vector and $f$ is $K$-Lipschitz in Euclidean norm, with $K>0$, then

\[
\mathbb E e^{\lambda(f(Z)-\mathbb Ef(Z))}
\leq e^{\lambda^2K^2/2},
\qquad
\mathbb P(|f-\mathbb Ef|>t)\leq2e^{-t^2/(2K^2)}.
\tag{19}
\]

Here is a derivation to make the dimension-free input explicit. For a smooth positive function $F$ bounded above and below, use the Gaussian averaging operator

\[
P_tF(x)=\mathbb E\left[F(e^{-t}x+\sqrt{1-e^{-2t}}\,Z)\right].
\]

Gaussian integration by parts gives its generator $\Delta-x\cdot\nabla$, preserves Gaussian expectation, and gives

\[
\operatorname{Ent}(F)
:=
\mathbb E[F\log F]-\mathbb EF\log\mathbb EF
=\int_0^\infty
\mathbb E\frac{\|\nabla P_tF\|^2}{P_tF}\,dt.
\]

This follows by differentiating $\mathbb E[P_tF\log P_tF]$, whose derivative is the negative displayed integrand, and letting $t$ tend to infinity. Initially one may assume bounded derivatives as well, so that all differentiations are dominated. Gradient commutation and weighted Cauchy–Schwarz give

\[
\nabla P_tF=e^{-t}P_t\nabla F,\qquad
\frac{\|\nabla P_tF\|^2}{P_tF}
\leq e^{-2t}P_t\!\left(\frac{\|\nabla F\|^2}{F}\right).
\]

Consequently,

\[
\operatorname{Ent}(F)\leq\frac12\mathbb E\frac{\|\nabla F\|^2}{F}.
\]

Apply this to $F=e^{\lambda f}$ for smooth bounded $K$-Lipschitz $f$. If $H(\lambda)=\log\mathbb E e^{\lambda f}$, the inequality reads

\[
\lambda H'(\lambda)-H(\lambda)\leq\lambda^2K^2/2.
\]

Integrating $(H(\lambda)/\lambda)'$ from zero proves the moment-generating bound in (19); negative $\lambda$ follows by replacing $f$ with $-f$. Exponential Markov inequality and optimization give the tails. A general Lipschitz $f$ follows by clipping its values and smoothing, without increasing its Lipschitz bound, and passing to the limit. The bound $|f(x)|\leq|f(0)|+K\|x\|$ supplies the needed Gaussian integrability in each finite dimension. The resulting constants depend on $K$, not that dimension.

### 7.3 Original outputs are Lipschitz on the operator-norm event

Collect all entries of all $J_e$ and all standardized Gaussian seeds into one standard Gaussian vector $Z_n$. On the set $\Omega_{n,R}$, each original-program vector register $v$ satisfies

\[
\|v(Z)-v(\widetilde Z)\|_2\leq K_v\|Z-\widetilde Z\|_2,
\tag{20}
\]

and each scalar register satisfies

\[
|a(Z)-a(\widetilde Z)|
\leq\frac{K_a}{\sqrt n}\|Z-\widetilde Z\|_2,
\tag{21}
\]

with constants independent of $n$, for any two primitive arrays in this set.

These estimates follow inductively. Initial Gaussian registers are fixed linear images of their seed blocks. A coordinate operation contributes at most its Lipschitz constant times the input vector differences plus $\sqrt n$ times scalar differences. A normalized empirical reduction contributes at most its Lipschitz constant times input vector differences divided by $\sqrt n$, together with the scalar differences. Scalar operations preserve (21).

For a forward query whose input bound is $B$, write $G=J/\sqrt n$ and $\widetilde G=\widetilde J/\sqrt n$. Then

\[
\begin{aligned}
\|Gh-\widetilde G\widetilde h\|_2
&\leq R\|h-\widetilde h\|_2
 +\frac{\|J-\widetilde J\|_F}{\sqrt n}\|\widetilde h\|_2\\
&\leq R\|h-\widetilde h\|_2+B\|J-\widetilde J\|_F.
\end{aligned}
\tag{22}
\]

The transpose estimate is identical. This proves (20)–(21) through the entire finite original program. In particular, every coordinate of a raw query output is $K$-Lipschitz on $\Omega_{n,R}$, with $K$ independent of $n$ and of the coordinate.

### 7.4 Symmetry fixes the location of the concentration bound

The original program is equivariant under an independent permutation of coordinates in each population, accompanied by the matching row and column permutations of all incident matrices and the matching permutations of seed rows. These transformed primitive arrays have the same distribution. Thus all coordinates of an output register have the same distribution.

For a raw forward output $y=Gh$ with $|h_i|\leq B$, this implies

\[
\mathbb E|y_i|^2
=\mathbb E\|y\|_{2,n}^2
\leq B^2\mathbb E\|G\|_{\mathrm{op}}^2
\leq C_2.
\tag{23}
\]

This estimate does not require independence between $h$ and $G$. It also holds for a transpose query.

Extend the scalar function $y_i(Z)$ from $\Omega_{n,R}$ to a $K$-Lipschitz function on all primitive arrays by

\[
\widetilde y_i(z)=
\inf_{x\in\Omega_{n,R}}\{y_i(x)+K\|z-x\|_2\}.
\]

The triangle inequality proves that this extension equals $y_i$ on the set, is finite everywhere, and is $K$-Lipschitz. Choose a fixed $A$ such that (23) gives $\mathbb P(|y_i|>A)\leq1/16$. By the choice of $R$,

\[
\mathbb P(|\widetilde y_i|\leq A)\geq7/8.
\]

The concentration bound (19) now bounds $|\mathbb E\widetilde y_i|$ by a constant depending only on $A,K$: if its absolute mean were larger than $A+K\sqrt{2\log8}$, the one-sided tail bound would contradict the preceding probability. Integrating (19) gives

\[
\sup_{n,i}\mathbb E|\widetilde y_i|^q<\infty
\quad\text{for every finite }q.
\tag{24}
\]

On the complement of the norm event, the original raw output still satisfies the deterministic estimate

\[
|y_i|\leq B\sqrt n\,\|G\|_{\mathrm{op}}.
\]

Cauchy–Schwarz, (17) and (18) consequently give

\[
\mathbb E[|y_i|^q\mathbf1_{\Omega_{n,R}^c}]
\leq B^q n^{q/2}
\bigl(\mathbb E\|G\|_{\mathrm{op}}^{2q}\bigr)^{1/2}
\mathbb P(\Omega_{n,R}^c)^{1/2}
\leq C_q n^{q/2}e^{-cn/2}.
\tag{25}
\]

Together (24)–(25) prove uniform moments of every order for every original raw query output. Initial seeds already have such moments. Global Lipschitz coordinate operations, finitely many inputs, and bounded scalar registers then give uniform moments of every order for every original vector register. In particular, every original empirical moment is bounded in probability, by Markov inequality.

## 8. Completing polynomial-moment convergence of the original program

Fix any finite $p>2$ and choose $q>p$. For the difference $v-\widehat v$ of corresponding original and simulator registers, Sections 5 and 7 give

\[
\|v-\widehat v\|_{q,n}=O_{\mathbb P}(1),
\]

whereas Section 6 gives $\|v-\widehat v\|_{2,n}=o_{\mathbb P}(1)$. Interpolation yields

\[
\|v-\widehat v\|_{p,n}
\leq
\|v-\widehat v\|_{2,n}^{\theta}
\|v-\widehat v\|_{q,n}^{1-\theta}
\longrightarrow0,\qquad
\frac1p=\frac{\theta}{2}+\frac{1-\theta}{q}.
\tag{26}
\]

For $p\leq2$, the conclusion follows directly from the normalized Euclidean bound. Thus original and simulator arrays differ by a vanishing amount in every finite empirical norm. Section 3 transfers all continuous polynomial-growth test limits from the simulator to the original program. Scalar convergence was already proved in Section 6. This proves the theorem.

## 9. What the theorem does and does not settle

The finite aggregate law is identified for the stated clipped Gaussian program with no history-rank assumption. The retained-history Gram inverses are legitimate because positive innovation selects an independent scalar direction; omitted directions never become observed finite-width constraints. Zero innovations are included through exact scalar-law dependence and the operator-norm estimate (15).

The construction uses one fresh scalar normal for each retained query. For a program with $J$ queries, it stores at most $J$ such innovations and at most order $J^2$ moment coefficients, distributed among the populations. Initial Gaussian scalar seeds add their fixed dimensions. All coefficients come from the prescribed finite program and already constructed scalar laws. This is an aggregate law, not a re-encoding of $n^2$ matrix entries.

The result supplies a genuine width-identification bridge for a fixed finite clipped neural program. It does not finish the original neural-flow task:

* Removing clipping requires a comparison to the original analytic-activation program. Its local products need not be globally Lipschitz, and its query vectors need not be bounded. The preceding proof does not silently supply that comparison.
* The finite-step law has no uniform error rate. Near a changing rank, its analysis coefficients can be arbitrarily large even though each fixed instance converges.
* A time-mesh limit needs estimates uniform in the number of instructions and a uniqueness theorem for the limiting causal law.
* A response-measure representation of that continuum law still needs its own identification and regularity argument.
* All-time approximation and a finite autonomous approximation require additional residual-tail, stability, approximation and restartability estimates on the original admitted small-label class. The theorem imposes no replacement class and makes none of those claims.

The only extra mathematical structure needed for polynomial-moment transfer beyond the omission argument is explicit in the grammar: Gaussian seed representation, coordinate permutation symmetry, uniformly bounded query inputs and a finite globally Lipschitz computation. Without a suitable uniform-moment argument, normalized Euclidean agreement alone would justify bounded observables but would not justify all polynomial tests.
