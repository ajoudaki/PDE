# Response subtraction and small Gaussian-root Hessians

2026-10-06. Scoped continuation in the unseen-query decoder study.
Internal theoretical results; no experiments or promotion.

The complete alternating program

\[
 z=Mu/\sqrt n,\quad a=\psi(z),\quad
 b=M^Ta/\sqrt n,\quad h=\phi(b),\quad y=Mh/\sqrt n
\]

has a response-corrected last source
$s=y-\rho a$, where $\rho=n^{-1}\sum_j\phi'(b_j)$.
For bounded activation derivatives through order three and bounded
deterministic input RMS, the maximum over coordinates of the Hessian
operator norm of $s_i$, with respect to the original standard Gaussian
matrix entries, is $O_{L^4}(\log(en)/\sqrt n)$. Its first gradients
have bounded $L^4$ norms. This is an explicit cancellation result for
two alternating reuses. The corresponding low-Hessian Gaussian test
identity is proved below without a covariance inverse.

This does not establish the growing-program decoder. The structural
information required to continue the Hessian induction is identified
at the end; a coordinatewise small-Hessian bound by itself is
insufficient to continue through another matrix call.

## Scope and provenance

The supervisor assigned a bounded test of the Hessian route within the
same study and scientific source scope. The current shared `AGENTS.md`
was reread. The complete process skills and required references read in
the preceding scoped task remain current: `investigate-conjectures`,
its research-contract, evidence-ledger, and adversarial-audit references,
and `solve-math-rigorously`. The required custom canonical-notation
skill was previously permission-denied, so the supplied instructions
and the maintained `docs/notation.qmd` contract continue to apply.

Scientific inputs are the sources recorded in the frozen
`GROWING_PROGRAM_STABILITY.md`, whose Section 12 was reread here, and
the supervisor's explicit prompt. Gaussian Lipschitz concentration is
the primitive used in the already authorized and completely read
`integrated_general_compression_20261004/GENERAL_DENSE_COMPARISON.md`.
No new external scientific source or specialized Stein theorem is used.
The needed smooth-test Gaussian identity is derived in Section 5.
The earlier file is not modified by this continuation.

The overall study contract still concerns the fully trained nonlinear
network, original label/gap allowance, all physical times and queries,
late query arrival, and absolute-polylogarithmic retained and peak live
workspace. The finite program below is a proof test for that contract,
not a substituted network theorem.

## 1. Objects and norms

Let $M\in\mathbb R^{n\times n}$ have independent $N(0,1)$ entries,
and write $W=M/\sqrt n$. Let $u\in\mathbb R^n$ be deterministic with
$\|u\|_2/\sqrt n\le U$, for a constant $U$ independent of $n$.
The extra bound $\|u\|_\infty\le U$ is not needed for the Hessian
statement. Let $\psi,\phi:\mathbb R\to\mathbb R$ be $C^3$, with

\[
 |\psi^{(j)}|\le p_j,\qquad |\phi^{(j)}|\le q_j,
 \qquad 1\le j\le3.                                      \tag{1}
\]

Values may grow linearly. Constants below may depend on
$U,|\psi(0)|,|\phi(0)|$, and these six derivative bounds, but not
on $n$. Coordinatewise application of scalar functions is understood.
Define

\[
 z=Wu,\quad a=\psi(z),\quad b=W^Ta,\quad h=\phi(b),
 \quad y=Wh,\quad \rho=\frac1n\sum_j\phi'(b_j),
 \quad s=y-\rho a.                                       \tag{2}
\]

All derivatives in this note are with respect to the $n^2$ entries of
$M$, equipped with ordinary Frobenius norm. Thus $Dg$ for a vector
field is a linear map from $\mathbb R^{n\times n}$ to
$\mathbb R^n$, and $D^2s_i$ is a scalar bilinear form on the matrix
space. Its operator norm is the supremum of
$|D^2s_i[E,F]|$ over $\|E\|_F,\|F\|_F\le1$.

Put $K=\|W\|_{\rm op}$ and define the polynomial bounds

\[
 A_0=|\psi(0)|+p_1KU,\qquad
 B_1=A_0+Kp_1U,\qquad
 H_0=|\phi(0)|+q_1KA_0.                                  \tag{3}
\]

The basic deterministic estimates are

\[
 \|a\|_2/\sqrt n\le A_0,\quad
 \|h\|_2/\sqrt n\le H_0,\quad
 \|Dz\|_{\rm op}\le U,\quad
 \|Da\|_{\rm op}\le p_1U,\quad
 \|Db\|_{\rm op}\le B_1.                                \tag{4}
\]

For example,
$Db[E]=E^Ta/\sqrt n+W^TDa[E]$, which proves the last bound.
The first two follow from the linear value-growth bounds and the
ordinary operator norm of $W$.

## 2. Warmup: one reverse/forward reuse

For deterministic $a$ consider only
$b=M^Ta/\sqrt n$, $h=\phi(b)$, $y=Mh/\sqrt n$.
Write $A=\|a\|_2/\sqrt n$ and fix coordinate $i$.
Different columns of $M$ enter separate summands of $y_i$.
The Hessian block corresponding to column $j$ is exactly

\[
 \frac{\phi'(b_j)}n(e_i a^T+a e_i^T)
 +\frac{M_{ij}\phi''(b_j)}{n\sqrt n}aa^T.                 \tag{5}
\]

Hence

\[
 \|D^2y_i\|_{\rm op}
 \le\frac{2q_1A+q_2A^2\max_j|M_{ij}|}{\sqrt n}.           \tag{6}
\]

The response subtraction $a_i\rho$ changes the column-$j$ block by
$a_i\phi'''(b_j)aa^T/n^2$, whose operator norm is at most
$|a_i|q_3A^2/n$. In this first reuse the uncorrected Hessian was
already small: a nonlinear response mean has not yet entered the
output population. The nontrivial cancellation begins in the full
program (2), where $a_i=\psi(z_i)$ has an order-one Hessian.

## 3. The exact Hessian cancellation in the full sandwich

Define the weighted row Gram

\[
 B_{ik}=\sum_j W_{ij}W_{kj}\phi'(b_j)
       =\frac1n\sum_jM_{ij}M_{kj}\phi'(b_j),\qquad
 R_{ik}=B_{ik}-\rho\mathbf1_{i=k}.                         \tag{7}
\]

For each fixed $i$, let
$v_i=(W_{ij}\phi'(b_j))_{j=1}^n$.
Direct differentiation gives the exact decomposition

\[
\begin{aligned}
 D^2s_i[E,F]={}&
 \frac{E_{i,:}\,Dh[F]+F_{i,:}\,Dh[E]}{\sqrt n}\\
 &+\sum_j W_{ij}\phi''(b_j)\,Db_j[E]Db_j[F]\\
 &+\frac{(Ev_i)^TDa[F]+(Fv_i)^TDa[E]}{\sqrt n}\\
 &+\sum_k\psi''(z_k)R_{ik}\,Dz_k[E]Dz_k[F]\\
 &-Da_i[E]D\rho[F]-Da_i[F]D\rho[E]
                         -a_iD^2\rho[E,F].
\end{aligned}                                             \tag{8}
\]

Every term in (8) can be checked without probabilistic assumptions.
First differentiate $y_i=n^{-1/2}M_{i,:}h$ twice. The two direct
derivatives of $M$ give the first line. The part of $D^2h_j$ containing
$\phi''(b_j)$ gives the second line. Next,

\[
 D^2b_j[E,F]
 =\frac{E_{:,j}^TDa[F]+F_{:,j}^TDa[E]}{\sqrt n}
       +\sum_kW_{kj}\psi''(z_k)Dz_k[E]Dz_k[F].             \tag{9}
\]

Weight (9) by $W_{ij}\phi'(b_j)$ and sum over $j$.
This produces the third line of (8) and its fourth line with $B_{ik}$
in place of $R_{ik}$. Finally, the term
$\rho D^2a_i=\rho\psi''(z_i)Dz_i\otimes Dz_i$ in
$D^2(\rho a_i)$ subtracts precisely the diagonal mean in (7).
The other product derivatives give the final line of (8).

The derivative of the empirical coefficient satisfies

\[
 \|D\rho\|_2\le\frac{q_2B_1}{\sqrt n},
\]
\[
 \|D^2\rho\|_{\rm op}
 \le\frac{q_3B_1^2+2q_2p_1U}{n}
             +\frac{U^2p_2Kq_2}{\sqrt n}.                \tag{10}
\]

For the second estimate, differentiate
$\rho=n^{-1}\sum_j\phi'(b_j)$ twice. Its first term is
$n^{-1}(Db)^T\operatorname{diag}(\phi'''(b))Db$.
For the remaining sum, use (9) with weights
$w_j=\phi''(b_j)/n$, so $\|w\|_2\le q_2/\sqrt n$.
The direct terms cost $2\|w\|_2p_1U/\sqrt n$;
the last term has coefficient $Ww$ and costs
$U^2p_2\|Ww\|_\infty\le U^2p_2Kq_2/\sqrt n$.
This proves (10).

Let $m_* =\max_{i,j}|M_{ij}|$ and
$a_* =\max_i|a_i|$. Combining (4), (8), and (10) yields

\[
 \max_i\|D^2s_i\|_{\rm op}
 \le C(K)\left[
       \frac{1+m_*+a_*}{\sqrt n}
                    +\max_{i,k}|R_{ik}|\right],           \tag{11}
\]

where $C(K)$ is a fixed polynomial in $1+K$ with nonnegative
coefficients depending only on the constants in (1)--(3).
For clarity, the first three lines of (8) cost respectively
$2q_1B_1/\sqrt n$,
$q_2B_1^2m_*/\sqrt n$, and
$2q_1Kp_1U/\sqrt n$.
The fourth line costs $U^2p_2\max_k|R_{ik}|$.
The product terms are bounded by (10) and
$\|Da_i\|_2\le p_1U$.

The first-gradient bound is

\[
 \max_i\|Ds_i\|_2
 \le H_0+Kq_1B_1+q_1p_1U
                 +\frac{a_*q_2B_1}{\sqrt n}.             \tag{12}
\]

Both (11) and (12) also have global polynomial bounds in $1+K$ alone:
$m_*/\sqrt n\le K$,
$a_*/\sqrt n\le|\psi(0)|+p_1KU$,
and $\max|R_{ik}|\le q_1(K^2+1)$.
This global control will make the exceptional-event contribution
quantitative; it is not enough by itself to prove the small bound.

## 4. The weighted row-Gram fluctuation, with centering justified

The mean of (7) is already root-width small. Gaussian integration by
parts in $M_{ij}$ gives

\[
 \mathbb E R_{ik}
 =\frac1n\sum_j\mathbb E\left[
       M_{kj}\phi''(b_j)\partial_{M_{ij}}b_j\right],
\]
\[
 \partial_{M_{ij}}b_j
 =\frac{a_i}{\sqrt n}
       +\frac{M_{ij}\psi'(z_i)u_j}{n}.                   \tag{13}
\]

The first identity subtracts
$\mathbf1_{i=k}\mathbb E\rho$ exactly. Since
$z_i\sim N(0,\|u\|_2^2/n)$,
$\|a_i\|_{L^2}\le|\psi(0)|+p_1U$.
Cauchy--Schwarz gives
$\mathbb E|a_iM_{kj}|\le|\psi(0)|+p_1U$, irrespective of
whether $i=k$. Also
$\mathbb E|M_{ij}M_{kj}|\le1$ and
$\sum_j|u_j|\le nU$. Thus

\[
 |\mathbb E R_{ik}|
 \le\frac{q_2(|\psi(0)|+p_1U)}{\sqrt n}
                       +\frac{q_2p_1U}{n}.              \tag{14}
\]

The Gaussian integration by parts is legitimate: (13), the bounded
derivatives, and the linear value-growth bound give integrable
polynomial Gaussian envelopes for the integrands and derivatives.

Fix a sufficiently large numerical $D$ and define

\[
 E_n=\left\{K\le8,\quad
 m_*\le D\sqrt{\log(en)},\quad
 \max_i|z_i|\le DU\sqrt{\log(en)}\right\}.               \tag{15}
\]

If $U=0$, the last condition is identically satisfied. For any chosen
fixed $A>0$, increasing $D$ makes
$\Pr(E_n^c)\le C_A n^{-A}$ for all $n$.
The entry and $z$ bounds follow directly from Gaussian tails and a
union over $n^2+n$ variables. For $K$, sphere $1/4$-nets of size
at most $9^n$, the bilinear net inequality, and the scalar Gaussian
tail give $\Pr(K>8)\le2e^{(2\log9-8)n}$.
The same net argument, with a variable threshold, shows
$\sup_n\mathbb E K^p<\infty$ for every fixed finite $p$.

On this set, each $R_{ik}$ has the following pairwise Lipschitz bound
in the original Gaussian matrix:

\[
 |R_{ik}(M)-R_{ik}(\widetilde M)|
 \le\frac{C_D\sqrt{\log(en)}}{\sqrt n}
                              \|M-\widetilde M\|_F
 \qquad(M,\widetilde M\in E_n).                          \tag{16}
\]

To prove it, first observe from direct subtraction that
$\|b(M)-b(\widetilde M)\|_2\le C\|M-\widetilde M\|_F$
whenever both normalized matrix norms are at most eight. The two
row differences in $B_{ik}$ cost at most
$16q_1\|M-\widetilde M\|_F/\sqrt n$.
For the gate difference, use

\[
 \|(\widetilde M_{ij}\widetilde M_{kj})_{j=1}^n\|_2
 \le \max_j|\widetilde M_{ij}|\,
                             \|\widetilde M_{k,:}\|_2
 \le8D\sqrt{n\log(en)}.
\]

Multiplying this by
$q_2\|b(M)-b(\widetilde M)\|_2/n$ proves the required bound
for that term. The mean coefficient obeys
$|\rho(M)-\rho(\widetilde M)|
\le q_2\|b(M)-b(\widetilde M)\|_2/\sqrt n$.
Combining the three terms proves (16) without assuming that the line
segment between the two matrices remains in $E_n$.

Moreover $|R_{ik}|\le65q_1$ on $E_n$. Extend $R_{ik}$ from $E_n$
by its scalar McShane formula with the constant in (16), then clip to
$[-65q_1,65q_1]$. Denote the resulting globally Lipschitz extension by
$\widetilde R_{ik}$. It agrees with $R_{ik}$ on $E_n$.
Its expectation differs from the raw expectation by at most

\[
 |\mathbb E\widetilde R_{ik}-\mathbb E R_{ik}|
 \le65q_1\Pr(E_n^c)+
             \|R_{ik}\|_{L^2}\Pr(E_n^c)^{1/2}
 \le C_A n^{-A/2}.                                       \tag{17}
\]

Here $|R_{ik}|\le q_1(K^2+1)$ gives a uniform $L^2$ bound.
This is the required centering correction; an eventual good event
with no quantitative failure rate would not suffice for this step.

The inherited Gaussian Lipschitz concentration inequality gives
$\Pr(|\widetilde R_{ik}-\mathbb E\widetilde R_{ik}|>t)
\le2\exp[-t^2/(2L_n^2)]$, with
$L_n=C_D\sqrt{\log(en)/n}$.
A union over $n^2$ pairs and (14), (17) prove

\[
 \Pr\left(E_n\cap\left\{
 \max_{i,k}|R_{ik}|>
 \frac C{\sqrt n}+C_A n^{-A/2}
       +C_D\sqrt{\frac{\log(en)\log(2n^2/\delta)}n}
                       \right\}\right)\le\delta.        \tag{18}
\]

Integrating the corresponding union tail yields
$\|\max_{i,k}|\widetilde R_{ik}|\|_{L^4}
\le C\log(en)/\sqrt n$.
For the part outside $E_n$, use the global bound
$\max|R_{ik}|\le q_1(K^2+1)$ and Hölder with its uniform
$L^8$ moment. Choosing, for example, $A=12$ in (15), (17)
therefore gives

\[
 \left\|\max_{i,k}|R_{ik}|\right\|_{L^4}
                  \le\frac{C\log(en)}{\sqrt n}.          \tag{19}
\]

On $E_n$, (11) and the coordinate caps now yield the same rate for
the Hessian. On $E_n^c$, its global polynomial bound in $K$ and the
same Hölder argument give a smaller contribution. Equation (12)
has a global polynomial bound in $K$. Consequently

\[
 \left\|\max_i\|D^2s_i\|_{\rm op}\right\|_{L^4}
                  \le\frac{C\log(en)}{\sqrt n},\qquad
 \left\|\max_i\|Ds_i\|_2\right\|_{L^4}\le C.            \tag{20}
\]

This proves the claimed Hessian cancellation for the full chronology
(2), with quantitative localization and no covariance-gap premise.

## 5. A derived smooth Gaussian identity with no covariance inverse

Let $G$ be a standard Gaussian vector in a finite Euclidean space,
and let $F=(F_1,\ldots,F_q)$ be a smooth function of $G$ with
$\mathbb EF=0$. Suppose its gradients and Hessian operator norms
have finite fourth moments. Set

\[
 g_a=\|\|DF_a\|_2\|_{L^4},\qquad
 h_a=\|\|D^2F_a\|_{\rm op}\|_{L^4},\qquad
 \Sigma=\mathbb E[FF^T].                                 \tag{21}
\]

For every $C^2$ test $T:\mathbb R^q\to\mathbb R$ with bounded
first derivatives and
$\sup_x\max_{a,b}|\partial_{ab}T(x)|\le B_T$, and for
$Z_\Sigma\sim N(0,\Sigma)$, including singular $\Sigma$,

\[
 |\mathbb ET(F)-\mathbb ET(Z_\Sigma)|
 \le\frac{3B_T}{4}
                     \left(\sum_a h_a\right)
                     \left(\sum_b g_b\right).            \tag{22}
\]

Here is a proof of the identity and estimates used in (22). Define the
Gaussian semigroup
$P_t f(x)=\mathbb E f(e^{-t}x+\sqrt{1-e^{-2t}}G')$,
with independent standard $G'$. Gaussian integration by parts gives
its generator $\mathcal L=\Delta-x\cdot\nabla$ and
$\mathbb E[(\mathcal Lf)g]=-\mathbb E\langle Df,Dg\rangle$.
Integrating the semigroup derivative, and using
$DP_t f=e^{-t}P_tDf$, gives

\[
 \mathbb E[F_a\Psi(F)]
 =\sum_b\mathbb E[\Gamma_{ab}\partial_b\Psi(F)],
 \qquad
 \Gamma_{ab}=\int_0^\infty e^{-t}
             \langle P_tDF_a,DF_b\rangle\,dt.             \tag{23}
\]

The centering makes the semigroup limit zero. For polynomially growing
smooth functions, all operations follow by Gaussian domination and
integration by parts. Smooth truncation gives the stated integrability
version. Taking $\Psi(F)=F_b$ shows
$\mathbb E\Gamma_{ab}=\Sigma_{ab}$.

The Gaussian Poincare inequality needed here also follows from the
same semigroup. Differentiate $\mathbb E(P_tf)^2$, integrate from
zero to infinity, and commute the derivative through $P_t$:

\[
 \operatorname{Var}(f)
 =2\int_0^\infty\mathbb E\|DP_tf\|_2^2\,dt
 \le2\int_0^\infty e^{-2t}\mathbb E\|Df\|_2^2,dt
 =\mathbb E\|Df\|_2^2.                                  \tag{24}
\]

The semigroup limit and integration are immediate first for smooth
compactly supported functions; Gaussian $H^1$ approximation then
gives (24) in the needed class.

Differentiating (23), using the product rule and
$D(P_tDF_a)=e^{-t}P_tD^2F_a$, gives

\[
 \|D\Gamma_{ab}\|_{L^2}
 \le\int_0^\infty
      [e^{-t}h_b g_a+e^{-2t}h_a g_b],dt
 =h_b g_a+\frac12h_a g_b.                                \tag{25}
\]

Holder's inequality supplies each product bound. Conditional Jensen
and invariance of Gaussian measure imply that $P_t$ contracts $L^4$,
including the operator norm of the Hessian. Thus (24) and (25) prove
$\|\Gamma_{ab}-\Sigma_{ab}\|_{L^2}
\le h_bg_a+h_ag_b/2$.

Finally solve the Gaussian test equation using the covariance-$\Sigma$
semigroup:

\[
 v(x)=-\int_0^\infty
 [\mathbb ET(e^{-t}x+\sqrt{1-e^{-2t}}Z_\Sigma)
                         -\mathbb ET(Z_\Sigma)],dt.
\]

It obeys
$\Sigma:D^2v-x\cdot Dv=T-\mathbb ET(Z_\Sigma)$ and
$\sup|\partial_{ab}v|\le B_T/2$, by integrating $e^{-2t}$.
The first-derivative bound on $T$ makes the defining integral converge.
No density or inverse of $\Sigma$ is required. Apply (23) to
$\Psi=\partial_av$ and sum over $a$. The resulting error is at most

\[
 \frac{B_T}{2}\sum_{a,b}
       \mathbb E|\Gamma_{ab}-\Sigma_{ab}|
 \le\frac{3B_T}{4}(\sum_a h_a)(\sum_b g_b),
\]

which proves (22). The finite programs in this note have polynomial
Gaussian envelopes for the required derivatives, so they satisfy the
integrability assumptions directly.

Applying (22) to any $q$ selected coordinates among the variables
$z_i$ and $s_i$ gives error $C B_T q^2\log(en)/\sqrt n$,
after centering. The $z_i$ have zero Hessians and gradient norm at
most $U$; (20) handles all the $s_i$. A polylogarithmic coordinate
panel is therefore allowed in this finite-sweep statement.
The next section identifies its covariance instead of treating the
actual covariance as an unspecified evaluator input.

## 6. Mean and covariance of the corrected source pair

Define the actual empirical contractions

\[
 q_u=\frac{\|u\|_2^2}{n},\qquad
 P_n=\frac{u^Th}{n},\qquad Q_n=\frac{\|h\|_2^2}{n}.       \tag{26}
\]

Uniformly over row indices $i,k$,

\[
 |\mathbb Es_i|\le C/\sqrt n,\qquad
 \operatorname{Cov}(z_i,z_k)=q_u\mathbf1_{i=k},
\]
\[
 \left|\operatorname{Cov}(z_i,s_k)
            -\mathbf1_{i=k}\mathbb EP_n\right|
 +\left|\operatorname{Cov}(s_i,s_k)
            -\mathbf1_{i=k}\mathbb EQ_n\right|
 \le\frac{C\log(en)}{\sqrt n}.                           \tag{27}
\]

We give the exact identities behind these bounds. Differentiating in
row $i$ rather than only at its matching output gives

\[
 \partial_{M_{ij}}s_k
 =\mathbf1_{i=k}\frac{h_j}{\sqrt n}
  +\frac{a_iM_{kj}\phi'(b_j)}n
  +\frac{\psi'(z_i)u_j}{\sqrt n}R_{ki}
                         -a_k\partial_{M_{ij}}\rho.      \tag{28}
\]

The cancellation in the third term is exactly the first-order version
of (8). Gaussian integration by parts in $y_i$ also gives

\[
 \mathbb Es_i=
  \frac1{n\sqrt n}\sum_j
              u_j\mathbb E[M_{ij}\psi'(z_i)\phi'(b_j)],   \tag{29}
\]

which is at most $p_1q_1U/\sqrt n$ in absolute value.

Since $z_i=n^{-1/2}\sum_jM_{ij}u_j$, its covariance with $s_k$
is $n^{-1/2}\sum_j u_j\mathbb E\partial_{M_{ij}}s_k$.
The four terms of (28) contribute respectively
$\mathbf1_{i=k}\mathbb EP_n$,
a term bounded by $C/\sqrt n$ using
$\|u\|_2\le U\sqrt n$ and $\|M_{k,:}\|_2/\sqrt n\le K$,
$q_u\mathbb E[\psi'(z_i)R_{ki}]$, and a term bounded by
$\mathbb E[|a_k|U\|D\rho\|_2]\le C/\sqrt n$.
Equation (19) bounds the third contribution and proves the cross
covariance assertion.

For the final covariance, integration by parts in
$\mathbb E[y_i s_k]$ gives an $\mathbb E[\rho a_i s_k]$
term that cancels in $\mathbb E[s_i s_k]$, leaving

\[
 \mathbb E[s_i s_k]
 =\frac1{\sqrt n}\sum_j
                \mathbb E[h_j\partial_{M_{ij}}s_k]
  +\frac1{n\sqrt n}\sum_j
       u_j\mathbb E[s_kM_{ij}\psi'(z_i)\phi'(b_j)].        \tag{30}
\]

Substitute (28). Its leading contribution is
$\mathbf1_{i=k}\mathbb EQ_n$.
The centered-Gram term is
$\mathbb E[\psi'(z_i)P_nR_{ki}]$, bounded by
$C\log(en)/\sqrt n$ using (19), Holder, and
$|P_n|\le U H_0$.
The remaining terms are $O(n^{-1/2})$ by (3), (10),
ordinary row Cauchy--Schwarz, and bounded fourth moments of $a_i,s_k$.

Those fourth moments do not need an extra assumption. The $a_i$ have
bounded Gaussian moments by linear growth. Equations (12), (29), and
(24) first give bounded second moments of $s_i$. Applying (24) to
$(s_i-\mathbb Es_i)^2$ gives

\[
 \mathbb E f^4-(\mathbb E f^2)^2
 \le4\mathbb E[f^2\|Df\|_2^2]
 \le4(\mathbb E f^4)^{1/2}
                         (\mathbb E\|Df\|_2^4)^{1/2},
\]

where $f=s_i-\mathbb Es_i$. Solving this quadratic inequality for
$(\mathbb E f^4)^{1/2}$ proves the uniform fourth-moment bound.
Subtracting the means in (30), whose product is $O(n^{-1})$,
completes (27).

The $2\times2$ matrix with entries $q_u,\mathbb EP_n,\mathbb EQ_n$
is positive semidefinite: $P_n^2\le q_uQ_n$ pointwise and Jensen
give $(\mathbb EP_n)^2\le q_u\mathbb EQ_n$.
Gaussian covariance interpolation, proved by density differentiation
and then a vanishing ridge, bounds a smooth-test change linearly in
the entrywise covariance change, including at singular covariance.
Consequently (22), (27) identify any chosen coordinate panel with
independent source pairs of this covariance, up to
$Cq^2\log(en)/\sqrt n$ for tests with fixed derivative bounds.

## 7. Explicit scalar Gaussian integrals for that covariance

The remaining expectations in (26) can be evaluated from a one-row
Gaussian calculation. Put $Z_0\sim N(0,q_u)$ and define

\[
 \kappa=\mathbb E\psi'(Z_0),\qquad
 q_a=\mathbb E\psi(Z_0)^2,\qquad
 P_* =\frac1n\sum_j u_j\mathbb E_Z\phi(u_j\kappa+\sqrt{q_a}Z),
\]
\[
 Q_* =\frac1n\sum_j\mathbb E_Z\phi(u_j\kappa+\sqrt{q_a}Z)^2,
 \qquad Z\sim N(0,1).                                   \tag{31}
\]

Then

\[
 |\mathbb EP_n-P_*|+|\mathbb EQ_n-Q_*|\le C/\sqrt n.      \tag{32}
\]

For completeness, write
$b_j=n^{-1/2}\sum_i X_{ij}$, with
$X_{ij}=M_{ij}\psi(z_i)$.
For a fixed $j$ these summands are independent over $i$, since they
use different rows of $M$. All their fixed finite moments are bounded
uniformly in $n,j$: the pair $(M_{ij},z_i)$ is Gaussian with variances
at most $1,U^2$, and $\psi$ has linear growth. Gaussian integration
by parts once and twice gives

\[
 \mathbb EX_{ij}=\frac{u_j\kappa}{\sqrt n},\qquad
 \operatorname{Var}(X_{ij})
 =q_a+\frac{u_j^2}{n}
       \left(\mathbb E(\psi^2)''(Z_0)-\kappa^2\right)
 =:\sigma_j^2.                                          \tag{33}
\]

This formula is valid even when $q_u=0$, by the same integration by
parts in the original standard Gaussian row. The variance is
nonnegative and uniformly bounded; no lower bound is needed.

Replace the centered summands successively by independent Gaussians
of variance $\sigma_j^2$, divided by $\sqrt n$.
Taylor expansion around the other summands cancels the first and
second moments at every replacement. The bounded third derivative
of $\phi$ bounds the total remainder by $C/\sqrt n$.
For the test $\phi^2$, its third derivative has at most linear growth.
The Taylor remainder is then bounded by
$C|v|^3(1+|x|+|v|)$, where $v$ is the replaced increment and $x$
is the sum of all other increments plus the mean $u_j\kappa$.
Independence, the uniform fourth moments, and the bounded variance
of the remaining sum bound the total remainder by
$C(1+|u_j|)/\sqrt n$.
Therefore

\[
 \left|\mathbb E\phi(b_j)
       -\mathbb E_Z\phi(u_j\kappa+\sigma_jZ)\right|
                                      \le C/\sqrt n,
\]
\[
 \left|\mathbb E\phi(b_j)^2
       -\mathbb E_Z\phi(u_j\kappa+\sigma_jZ)^2\right|
                              \le C(1+|u_j|)/\sqrt n.    \tag{34}
\]

Gaussian variance interpolation changes these two targets from
$\sigma_j^2$ to $q_a$ by at most
$Cu_j^2/n$ and $C(1+|u_j|)u_j^2/n$, respectively.
For the second bound, the second derivative of $\phi^2$ has at most
linear growth and its Gaussian mean is $u_j\kappa$.
Average (34), weighting the first inequality by $|u_j|$.
Use
$n^{-1}\sum|u_j|\le U$,
$\sum u_j^2\le nU^2$, and
$\sum|u_j|^3\le\|u\|_\infty\|u\|_2^2\le n^{3/2}U^3$.
These estimates prove (32) even without a coordinate bound on $u$.

The explicit target covariance is consequently

\[
 \Sigma_*=
 \begin{pmatrix}q_u&P_*\\P_*&Q_*\end{pmatrix}.             \tag{35}
\]

It is positive semidefinite by Cauchy--Schwarz applied to (31).
No spatial interpolation or inverse covariance enters its construction.
For any $p$ distinct row indices, let $(Z_r,S_r)_{r=1}^p$ be independent
Gaussian pairs with covariance (35). Combining (20)--(22), (27), and
(32), and shifting the $O(n^{-1/2})$ source means, proves

\[
 \left|\mathbb ET((z_{i_r},s_{i_r})_{r=1}^p)
       -\mathbb ET((Z_r,S_r)_{r=1}^p)\right|
 \le C_T\frac{p^2\log(en)}{\sqrt n},                     \tag{36}
\]

for separately specified tests whose first derivatives and Hessian
entries have common finite bounds. Constants depend on those bounds
and the displayed activation/input bounds, not on a covariance gap.
The estimate therefore permits $p$ growing polylogarithmically in $n$
in this fixed-sweep program.

If additionally $\phi^{(4)}$ is bounded, define
$\rho_*=n^{-1}\sum_j\mathbb E_Z
\phi'(u_j\kappa+\sqrt{q_a}Z)$.
The same replacement proof for the bounded test $\phi'$ gives
$|\mathbb E\rho-\rho_*|\le C/\sqrt n$.
Equations (10), (24) give $\operatorname{Var}(\rho)\le C/n$,
so $\|\rho-\rho_*\|_{L^2}\le C/\sqrt n$.
Because $y_i=s_i+\rho\psi(z_i)$, (36) then yields the
corresponding nonlinear output law

\[
 (z_{i_r},y_{i_r})_{r=1}^p
 \quad\hbox{against smooth tests is approximated by}\quad
 (Z_r,S_r+\rho_*\psi(Z_r))_{r=1}^p                       \tag{37}
\]

at the same stated rate. Indeed, replace $\rho$ by $\rho_*$ using
the test's first-derivative bound and Cauchy--Schwarz with the bounded
second moments of $a_i$. Then compose the test with
$(z,s)\mapsto(z,s+\rho_*\psi(z))$; its first derivatives and
Hessian entries remain bounded by (1).
Strip-analytic activations in the study satisfy the additional bounded
real fourth-derivative condition by Cauchy's formula on a smaller strip.

## 8. The invariant needed beyond this sweep

The proved invariant in this example is stronger than a list of small
coordinate Hessians. Equation (9) retains the row blocks of every
$D^2b_j$. Upon the next matrix contraction, these blocks produce the
weighted Gram $B_{ik}$ rather than an uncontrolled sum of their norms.
The retained response $\rho a_i$ removes its diagonal mean; (19)
controls its remaining entries. The collectively bounded Jacobian
$Db$ controls the other composition term by
$\|(Db)^T\operatorname{diag}(W_{i,:}\phi''(b))Db\|_{m op}$.
Both pieces of structure matter.

A subsequent induction would need to retain the exact second-order
chain-rule decomposition across all prior coordinate instructions.
For each new source it must establish all of the following, with
constants polynomial in the counted history size and at most the
allowed physical stability factor:

1. Collective operator bounds for the vector-field Jacobians and the
   downstream response maps, not only bounds on each row gradient.
2. Hessian blocks represented as pullbacks of diagonal coordinate
   curvature, together with direct matrix-derivative and empirical-
   coefficient terms whose contracted operator norms are small.
3. Identification of the non-small diagonal return coefficients with
   the exact causal response terms subtracted by the scalar DAG.
4. Entrywise fluctuation bounds for the resulting weighted return
   matrices, with quantitative centering and localization as in
   (13)--(19).

The dependence on history size cannot be supplied by multiplying a
generic instruction Lipschitz constant at every call. For the target
trajectory it must follow from its physical residual/response
structure, a stable temporal scheme, or another proved estimate.

An algebraic counterexample shows why the weaker invariant is
insufficient. Let $G$ be a standard Gaussian independent of $M$, fix
one row index $i$, and define

\[
 v_j(M,G)=\frac{G^2}{2\sqrt n}\tanh(M_{ij}).               \tag{38}
\]

Each scalar Hessian has operator norm at most
$C(1+G^2)/\sqrt n$, and the collective Jacobian of $v$ has operator
norm at most $|G|+G^2/(2\sqrt n)$.
Nevertheless its matrix-contracted coordinate is

\[
 (Wv)_i=\frac{G^2}{2n}\sum_jM_{ij}\tanh(M_{ij})
 \longrightarrow \frac c2G^2,
 \qquad c=\mathbb E[Z\tanh Z]>0,                          \tag{39}
\]

in $L^2$, by independence of the Gaussian row entries and their finite
moments. The Hessian in the $G$ direction tends to $c$, and the
limit after centering is not Gaussian.
Thus individually small Hessians plus a collectively bounded first
Jacobian do not alone propagate through an adaptively correlated
matrix action. The example is an obstruction to that proposed
induction invariant, not a counterexample to the original training
model; it does not claim that its queried coordinate array is
generated by the allowed network chronology. In a valid causal
response theorem, its surviving return must be retained and
subtracted, just as $\rho a_i$ is retained in (2).

The result of this bounded route is therefore a proved, explicit
nonlinear two-reuse law with computable Gaussian coefficients and a
polylogarithmic-panel rate. It is a substantive check of the proposed
Hessian mechanism. The general growing-chronology structured Hessian
induction remains open, so the absolute-polylogarithmic autonomous
late-query decoder is still neither proved nor refuted here.
