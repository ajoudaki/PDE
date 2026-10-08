# A quantitative rate for each fixed actual neural query program

2026-10-07. Proof candidate for a bounded continuation of the causal-Gaussian route.

Notation-only correction: the retained-history gap is now denoted by $\lambda_{\mathrm{hist}}$, distinct from the established initial feature-Gram gap $\gamma$. The pre-correction frozen SHA-256 was 9dbafab203759e85a42f442802f3e9a650d6b57f5ea456e5d3f92d0fd41995e8. No theorem hypothesis or qualification changed.

Scientific inputs: the complete 248-line UNCLIPPED_FINITE_HISTORY.md, SHA-256 814a72f722b26ab2a8d360b8c03bb9e4781fe4ba4733948c14a731605da86595, the supervisor's quantitative assignment, and this route's own conditioning and finite-program proofs. No external source, other study, experiment or additional agent result was used.

The result below strengthens the unclipped fixed-history law to an explicit high-probability $n^{-1/2}$ rate multiplied by a fixed power of $\log n$. It applies to each fixed finite canonical Euler computation. It does not allow its program length, mesh or retained conditioning gaps to vary with width.

The abstract source class permits merely continuous shared-coefficient maps. Such maps do not in general preserve a specified rate. The quantitative statement uses locally Lipschitz coefficient maps near the finitely many limiting arguments. This is satisfied by the actual Euler program's polynomial scalar operations and does not impose a new condition on its labels.

## 1. Fixed-program statement

Use the source's finite collection of width-$n$ populations, independent initialized Gaussian matrices with entry variance $1/n$, and independent Gaussian row roots. Within a population each root row has the same fixed finite covariance, possibly singular. There are $Q\geq1$ prescribed instructions, independent of $n$, built from:

* initialized matrix or transpose queries;
* globally Lipschitz coordinate functions, including at-most-linear growth activations;
* gated products $u_i a(v_i)$ with $a$ bounded and globally Lipschitz;
* finite linear combinations of row fields with shared scalar coefficients;
* normalized empirical inner products and scalar coefficient maps.

Every shared scalar coefficient map is locally Lipschitz on a neighborhood of its deterministic limiting argument. The finite program is defined on its finite-width inputs; only its behavior in these neighborhoods enters the high-probability estimate. No row is selected by its index. No empirical history inverse occurs in the original program.

Construct the deterministic scalar law and retain/omit schedule as in the source: retain a query precisely when its population $L^2$ innovation relative to the retained same-direction query history is positive. Return the corresponding linear combination of past answers for a zero innovation.

Let $V_j$ be any scalar row field in that construction, and let $v_j^{(n)}$ be its actual finite-program field. Expectations of products below are taken within the appropriate population's scalar law. Let $s_k$ and $s_k^{(n)}$ denote limiting and actual shared scalar registers.

**Theorem.** For every fixed program and every $r>0$, there are constants $C_r<\infty$ and $n_r<\infty$, independent of width, such that for all $n\geq n_r$,

\[
\mathbb P\left\{
\max_{j,k\text{ in the same population}}
\left|\frac1n(v_j^{(n)})^\top v_k^{(n)}-\mathbb E[V_jV_k]\right|
\ \vee\ \max_k|s_k^{(n)}-s_k|
>
C_r n^{-1/2}[\log(en)]^{2Q+2}
\right\}
\leq C_r n^{-r}.
\tag{1}
\]

One can include a constant-one field to obtain means as well. Outputs and the finitely sampled feature/backward kernels of a fixed canonical Euler computation are included among these scalar registers and pairings.

There is also a coupling with iid reference rows $V_{j,i}$ of the scalar law, using the same Gaussian row roots and fresh scalar-law innovations, for which

\[
\max_j\left(\frac1n\sum_i|v_{j,i}^{(n)}-V_{j,i}|^2\right)^{1/2}
\leq C_r n^{-1/2}[\log(en)]^{2Q+2}
\tag{2}
\]

on an event of probability at least $1-C_r n^{-r}$. Independence is across reference rows within each population, not between the actual interacting neurons. The exponent in (1)–(2) is deliberately coarse; it makes its dependence on fixed program length explicit.

The constants may depend on:

1. $Q$, the number of populations and matrices, root dimensions and covariance operators;
2. fixed data, labels, Euler steps and all deterministic scalar-law coefficients;
3. coordinate-function Lipschitz constants and intercepts, and each gate's uniform bound and Lipschitz constant;
4. the local Lipschitz constants and neighborhood radii of all shared coefficient maps;
5. the smallest eigenvalue $\lambda_{\mathrm{hist}}>0$ among nonempty retained limiting history Grams, and the smallest positive retained innovation variance $\nu>0$;
6. the probability exponent $r$.

Empty minima in item 5 can be assigned the value one. For each fixed program the nonempty minima are positive by the retention rule and finiteness. They are not additional lower-bound assumptions on an admissible label class. Their values may deteriorate along a sequence of programs or labels.

## 2. The scalar fields have a Gaussian linear envelope

For each population, collect all its initial standardized Gaussian roots and all scalar innovations used in retained queries into one finite-dimensional standard Gaussian vector $\zeta$. Each scalar field is a deterministic function of this vector. The coefficients in this scalar construction are deterministic.

In fact, every field admits an envelope

\[
|V_j(\zeta)|\leq A_j(1+\|\zeta\|_1)
\tag{3}
\]

with a finite program-dependent $A_j$. This is stronger than arbitrary polynomial growth:

* A globally Lipschitz coordinate function has at most linear growth in its arguments.
* The gate product obeys $|u\,a(v)|\leq\|a\|_\infty|u|$.
* A fixed linear combination adds the corresponding envelope constants.
* Each retained Gaussian query is a fixed linear combination of existing fields plus a fixed multiple of one new Gaussian coordinate.

These observations prove (3) by induction. They also show that every same-population product $V_jV_k$ has a quadratic Gaussian envelope. Singular root covariance is handled by a fixed linear map of standardized roots.

Put

\[
\lambda_n=\sqrt{\log(en)},\qquad
\epsilon_n=n^{-1/2}\lambda_n^3.
\tag{4}
\]

For every $r>0$, iid reference rows can be chosen so that, with probability at least $1-C_r n^{-r}$, simultaneously for the finitely many fields, roots, innovations and pairings,

\[
\begin{aligned}
\max_{j,i}|V_{j,i}|+\max_{\text{primitive }Z_i}|Z_i|
&\leq B_r\lambda_n,\\
\max_{j,k}\left|
\frac1n\sum_i V_{j,i}V_{k,i}-\mathbb E[V_jV_k]
\right|&\leq B_r\epsilon_n .
\end{aligned}
\tag{5}
\]

In particular all empirical reference second moments are bounded by a fixed constant on this event for sufficiently large $n$.

Here is an elementary concentration proof. Gaussian tails and a union bound over the fixed number of primitive columns and their $n$ rows bound their largest coordinate by a constant times $\lambda_n$ with arbitrary prescribed inverse-polynomial failure probability. Truncate a row product when any primitive root in that row exceeds this threshold. By (3), its truncated value is bounded by $C_r\lambda_n^2$. These truncated row products are independent across rows. If independent centered variables satisfy $|X_i|\leq M$, symmetrization with an independent copy and $\cosh t\leq e^{t^2/2}$ give

\[
\mathbb E e^{tX_i}
\leq\mathbb E e^{t(X_i-X_i')}
=\mathbb E\cosh(t(X_i-X_i'))
\leq e^{2t^2M^2}.
\]

Exponential Markov inequality, optimized in $t$, bounds their average deviation by a constant times $M\sqrt{\log(en)/n}$ at failure probability $C_r n^{-r}$. This is $C_r\epsilon_n$. Centering a bounded uncentered variable only changes the bound $M$ by a factor of two. The truncation bias is smaller: Cauchy–Schwarz, the fixed fourth Gaussian envelope moment and a sufficiently large Gaussian threshold bound it by any required negative power of $n$. A finite union over all same-population register pairs proves (5).

## 3. Coupling the retained simulator to iid scalar rows

Let the finite-width simulator retain only the population-positive innovations. At a retained query it obtains the actual matrix action; at an omitted query it returns the deterministic limiting linear combination of retained answers. Its nonmatrix operations are the original ones.

There is a joint construction in which the simulator's exact conditional Gaussian innovations are the same primitive Gaussian columns used to form the iid reference rows in Section 2. Generate its retained answers sequentially using the exact Gaussian posterior and independent full standard-normal innovation columns. After its final retained query, complete each initialized matrix from its Gaussian posterior. This completion gives the original independent Gaussian-matrix marginal law, and all simulator answers agree with actions of those completed matrices. Run the original program on those same matrices and roots afterward. This is only a coupling construction; the original program's additional answers never enter the simulator's conditioning transcript.

At one interface write $H,F$ for retained forward inputs and answers, and $D,B$ for retained backward inputs and answers. A finite retained forward query has exact conditional form

\[
g_n=F_n a_n+D_n b_n+\sigma_n(I-P_{D_n})\xi,
\tag{6}
\]

where

\[
\begin{aligned}
a_n&=(H_n^\top H_n/n)^{-1}(H_n^\top u_n/n),\\
u_{\perp,n}&=u_n-H_n a_n,\\
b_n&=(D_n^\top D_n/n)^{-1}(B_n^\top u_{\perp,n}/n),\\
\sigma_n^2&=\|u_{\perp,n}\|_{2,n}^2.
\end{aligned}
\tag{7}
\]

On a finite singular-Gram event the exact formula uses pseudoinverses. The quantitative induction below excludes that event for all sufficiently large widths on its good event. The reference row generated by the same $\xi_i$ is

\[
g_i=F_i^\top a+D_i^\top b+\sigma\xi_i.
\tag{8}
\]

For each retained opposite history, write

\[
P_{D_n}\xi=D_n\beta_n,\qquad
\beta_n=(D_n^\top D_n)^{-1}D_n^\top\xi.
\]

When its normalized Gram has smallest eigenvalue at least $\lambda_{\mathrm{hist}}/2$,

\[
\operatorname{Cov}(\beta_n\mid\text{past})
=(D_n^\top D_n)^{-1}
\preceq\frac{2}{n\lambda_{\mathrm{hist}}}I.
\]

Conditional Gaussian tails therefore imply, simultaneously for all finitely many calls,

\[
\|\beta_n\|\leq C_r n^{-1/2}\lambda_n
\tag{9}
\]

except on an event of probability at most $C_rn^{-r}$. To avoid a circular assumption, impose this bound only up to the first failure of a required Gram neighborhood. At each pre-failure call its conditional bound applies, so a union bound controls the probability of any failed projection bound before that stopping time. The deterministic estimates below prevent a Gram-neighborhood failure for sufficiently large $n$.

### Quantitative continuity of the retained coefficients

All coefficients in (7) are functions of finitely many empirical pairings of existing fields. Near their limiting values these functions are locally Lipschitz. Useful explicit bounds are

\[
\begin{aligned}
\|\Gamma_n^{-1}\|&\leq2/\lambda_{\mathrm{hist}},\\
\|\Gamma_n^{-1}-\Gamma^{-1}\|
&\leq2\lambda_{\mathrm{hist}}^{-2}\|\Gamma_n-\Gamma\|,\\
\|\Gamma_n^{-1}b_n-\Gamma^{-1}b\|
&\leq2\lambda_{\mathrm{hist}}^{-1}\|b_n-b\|
+2\lambda_{\mathrm{hist}}^{-2}\|b\|\,\|\Gamma_n-\Gamma\|.
\end{aligned}
\tag{10}
\]

They hold if $\|\Gamma_n-\Gamma\|\leq\lambda_{\mathrm{hist}}/2$. At a retained call $\sigma^2\geq\nu$, and

\[
|\sigma_n-\sigma|
=\frac{|\sigma_n^2-\sigma^2|}{\sigma_n+\sigma}
\leq\nu^{-1/2}|\sigma_n^2-\sigma^2|.
\tag{11}
\]

Thus no square-root loss occurs at a retained innovation. Zero limiting variance is handled by omission instead of applying a square root to a noisy empirical estimate.

### Entrywise simulator error induction

Let $E_j$ be the largest coordinate error between simulator and iid-reference fields created through instruction $j$, together with the largest error of their shared scalar registers. Initially $E_0=0$. Work on the reference event (5), the projection event (9), and the relevant coefficient neighborhoods.

If every prior coordinate error is at most $E\leq1$, the deviation of a simulator pairing from its population value is bounded by

\[
C_r\lambda_n E+C_r\epsilon_n.
\tag{12}
\]

Indeed, subtract the two factors against their reference rows and use (5), then add the iid empirical-pair fluctuation. Equation (12), local Lipschitz continuity and (10)–(11) bound all new coefficients. In (6)–(8), a coefficient error multiplies a reference coordinate or innovation of size at most $B_r\lambda_n$; an old field error is multiplied by a bounded coefficient. The projection term has coordinate bound

\[
C_r\max_i\|D_{n,i}\|\,\|\beta_n\|
\leq C_rn^{-1/2}\lambda_n^2.
\]

Consequently a retained query satisfies the safe bound

\[
E_j\leq K_j\lambda_n^2(E_{j-1}+\epsilon_n).
\tag{13}
\]

The same bound covers every nonmatrix instruction. A gated product costs at most one factor of $\lambda_n$, since

\[
|u_n a(v_n)-u a(v)|
\leq \|a\|_\infty|u_n-u|
+\operatorname{Lip}(a)|u|\,|v_n-v|.
\]

A linear combination costs a factor of $\lambda_n$ for a scalar coefficient error; empirical pairings obey (12). Fixed Lipschitz maps and locally Lipschitz scalar maps have smaller bounds.

At an omitted query the simulator and reference both take the same fixed linear combination of earlier retained answers. Thus (13) holds there too, without fresh error.

For example, choose $A_0=0$ and recursively

\[
A_j=K_j(A_{j-1}+1).
\]

Since $\lambda_n\geq1$, (13) gives

\[
E_j\leq A_j\epsilon_n\lambda_n^{2j},
\qquad 0\leq j\leq Q.
\tag{14}
\]

For each fixed program the right-hand side tends to zero. For sufficiently large $n$, it remains below one and (12) keeps every retained history Gram and shared-coefficient argument in its chosen neighborhood. This closes the stopping-time argument. It also proves the simulator field bounds

\[
\max_{j,i}|\widehat v_{j,i}^{(n)}|\leq C_r\lambda_n,\qquad
\max_j\|\widehat v_j^{(n)}\|_{2,n}\leq C_r.
\tag{15}
\]

The second bound follows from the reference empirical second moments and (14), not from its larger coordinate maximum.

## 4. Zero innovations have a rate without estimating a square root

At an omitted forward query, the scalar-law condition is

\[
\mathbb E[(u-H^\top a)^2]=0.
\]

It gives the exact rowwise identity

\[
u_i-H_i^\top a=0
\tag{16}
\]

almost surely for every iid reference row. There are only finitely many instructions and countably many possible rows, so all these identities may be imposed on one probability-one event.

Hence the corresponding finite simulator residual satisfies

\[
\|\widehat u_n-\widehat H_n a\|_\infty
\leq (1+\|a\|_1)E_{j-1}.
\tag{17}
\]

The same rate therefore holds in normalized Euclidean norm. Estimating its squared norm only by an empirical variance error and then taking a square root would lose the rate. The rowwise coupling avoids that step entirely.

The argument applies unchanged to omitted reverse queries and to an empty same-direction history whose limiting query is identically zero. In particular, zero-readout and zero-label degeneracies cause no exception.

## 5. Comparing the original program with the simulator

For a sufficiently large fixed $R$, the original Gaussian matrices satisfy

\[
\max_G\|G\|_{\mathrm{op}}\leq R
\tag{18}
\]

except with probability at most $Ce^{-cn}$. The direct quarter-net proof from the source gives this bound and remains valid in the coupling because the completed matrices have the original Gaussian marginal law.

Let $\Delta_j$ be the largest normalized Euclidean error between original and simulator fields through instruction $j$, together with the largest difference of their scalar registers. The two programs have identical initial roots, so $\Delta_0=0$.

For a gate, use the simulator as the large multiplier:

\[
\begin{aligned}
\|u_n a(v_n)-\widehat u_n a(\widehat v_n)\|_{2,n}
&\leq \|a\|_\infty\|u_n-\widehat u_n\|_{2,n}\\
&\quad+\operatorname{Lip}(a)\|\widehat u_n\|_\infty
\|v_n-\widehat v_n\|_{2,n}.
\end{aligned}
\tag{19}
\]

Equation (15) makes this at most $C_r\lambda_n\Delta_{j-1}$. No maximum or higher empirical moment of an original field is assumed.

As long as $\Delta_{j-1}\leq1$, original and simulator empirical norms are bounded by (15). Their pairings differ by at most $C_r\Delta_{j-1}$, by subtracting the two factors and applying Cauchy–Schwarz. The locally Lipschitz scalar maps then preserve this rate while their arguments remain in their fixed neighborhoods. Linear combinations and globally Lipschitz coordinate functions preserve it as well.

Retained queries cost at most $R\Delta_{j-1}$ by (18). At an omitted forward call, the exact retained identities give

\[
Gu_n-\widehat F_n a
=G(u_n-\widehat u_n)
+G(\widehat u_n-\widehat H_n a).
\]

Equations (17)–(18) bound its normalized Euclidean norm by

\[
R\Delta_{j-1}+C_rE_{j-1}.
\tag{20}
\]

Reverse queries are identical. Thus, with new finite program constants $K_j'$,

\[
\Delta_j\leq K_j'\lambda_n(\Delta_{j-1}+E_Q).
\tag{21}
\]

One can take $B_0=0$ and $B_j=K_j'(B_{j-1}+1)$ to obtain

\[
\Delta_j\leq B_jE_Q\lambda_n^j.
\]

Together with (14),

\[
\Delta_Q+E_Q
\leq C_r n^{-1/2}\lambda_n^{3Q+3}.
\tag{22}
\]

For sufficiently large $n$ this also stays below one and keeps the original scalar arguments in their prescribed neighborhoods, closing the comparison bootstrap. All constants in these recursions depend only on the list in Section 1 and the finitely many population moments defining the scalar law.

## 6. Outputs, pairings and the probability bound

For each same-population pair, split its error into original-versus-simulator, simulator-versus-reference, and iid reference-versus-expectation. The first two terms are at most $C_r(\Delta_Q+E_Q)$ because all normalized Euclidean norms are bounded on the good event. The last term is at most $B_r\epsilon_n$ by (5). Shared scalar registers obey the same local Lipschitz estimates already included in the induction.

The total error is therefore bounded by the right-hand side of (22), enlarged by a program constant. Since

\[
\lambda_n^{3Q+3}
\leq[\log(en)]^{2Q+2},
\]

this proves the advertised bounds (1)–(2). The union of the finitely many Gaussian-root, iid-pair and conditional-projection failures has probability at most $C_rn^{-r}$, and the matrix-norm failure is exponentially smaller.

For specificity, the finite threshold $n_r$ may be chosen large enough that the recursive bounds (14), (22) and the pairing bound (12) are below all of:

* one, for the field-error bootstraps;
* half the chosen local coefficient-neighborhood radii;
* the retained Gram tolerance needed for eigenvalues at least $\lambda_{\mathrm{hist}}/2$;
* the fixed moment neighborhoods used to bound the regression coefficient functions.

The inverse and square-root bounds (10)–(11), plus local Lipschitz constants on these neighborhoods, specify how to choose the finite $K_j,K_j'$ recursively. This makes the dependence on small retained gaps explicit; there is no width-dependent coefficient hidden in the constants.

## 7. Meaning for the actual neural model

The canonical fixed-mesh Euler history program has the required operations. Analyticity with bounded derivative in the assigned strip supplies a globally Lipschitz activation and a bounded globally Lipschitz derivative gate. Its residuals and memory coefficients are polynomial scalar operations on previously computed pairings and fixed labels. Thus the theorem covers its actual unbounded activation values without replacing them by clipped values and without adding a nonzero-label or history-gap hypothesis.

The bound is $n^{-1/2+o(1)}$ for each fixed program. It controls deterministic aggregate outputs and the realized finite outputs at the dense fluctuation scale up to logarithmic factors. It is not an $o_p(n^{-1/2})$ reconstruction of the realized fluctuation, and it does not establish a central limit theorem.

No conclusion here is uniform in the number of steps, depth, number of samples, retained gaps or local Lipschitz constants. Decreasing the step size at a fixed positive horizon increases the program and requires new uniform estimates. Continuous time, all-time stability, finite autonomous memory, and approximation over the full original small-label class with uniform constants remain separate obligations.
