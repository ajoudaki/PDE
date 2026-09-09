# Arbitrary finite-step width-first identification

## 1. Result

Fix an integer (N\geq 1) and a real step size (h\neq0).  Consider the
two-hidden-layer network and simultaneous ascent rule

\[
u_j^s=(w_j^s)^Tx/\sqrt p,\qquad H_j^s=\phi(u_j^s),
\]

\[
z_i^s=n^{-1/2}\sum_jW_{ij}^sH_j^s,\qquad
f_n^s=n^{-1}\sum_i a_i^s\phi(z_i^s),
\]

\[
\begin{aligned}
a_i^{s+1}&=a_i^s+h\phi(z_i^s),\\
W_{ij}^{s+1}&=W_{ij}^s+\frac h{\sqrt n}C_i^sH_j^s,\\
u_j^{s+1}&=u_j^s+h b_j^s\phi'(u_j^s),
\end{aligned}
\qquad
C_i^s=a_i^s\phi'(z_i^s),\quad
b_j^s=n^{-1/2}\sum_iW_{ij}^sC_i^s.
\]

The initialization consists of mutually independent standard Gaussian
(a_i^0,W_{ij}^0,w_j^0), and (\|x\|^2/p=1).  Suppose
(\phi\in C^{12}), all derivatives of orders (1,\ldots,12) are bounded,
(\phi) has at most linear growth, and
(\mathbb E\phi(G)^2=1).

For every fixed (N) and every fixed (h\ne0), all the population Grams
needed in the chronological (2N+1)-action conditioning argument are
strictly positive definite whenever (\phi) is nonconstant.  Moreover,
at this fixed (h), every value field, empirical Gram, empirical response
cross-moment, and terminal output converges to the Gaussian DAG in Section
2.  In particular,

\[
\lim_{n\to\infty}\mathbb E f_n^N=F_N(h).
\tag{1.1}
\]

Thus no small-(h) rank radius is needed.  Any radius later imposed in a
quantitative Taylor theorem is needed only for the activation-envelope
estimate, not for the width-first identification.

If (\phi) is constant, normalization makes (\phi\equiv\pm1), and the
finite-width identity (\mathbb E f_n^N=Nh) holds directly.  This case
does not require conditioning on a cotangent Gram.

## 2. The finite Gaussian DAG

Put (W=W^0), and define the raw actions and empirical Grams

\[
Y^s=WH^s/\sqrt n,\qquad D^s=W^TC^s/\sqrt n,
\]

\[
Q_{rs}^{(n)}=n^{-1}(H^r)^TH^s,\qquad
K_{rs}^{(n)}=n^{-1}(C^r)^TC^s.
\]

The exact rank-one expansion of the trained matrix is

\[
W^s=W+\frac h{\sqrt n}\sum_{r<s}C^r(H^r)^T.
\]

Consequently,

\[
z^s=Y^s+h\sum_{r<s}Q_{rs}^{(n)}C^r,\qquad
b^s=D^s+h\sum_{r<s}K_{rs}^{(n)}H^r.
\tag{2.1}
\]

The matrix is exposed in the predictable order

\[
Y^0,D^0,Y^1,D^1,\ldots,Y^{N-1},D^{N-1},Y^N.
\tag{2.2}
\]

Let (A,U) be independent standard Gaussians.  At each stage use centered
Gaussian source blocks

\[
(\xi_0,\ldots,\xi_s)\sim N(0,Q^{[s]}),\qquad
(\chi_0,\ldots,\chi_s)\sim N(0,K^{[s]}),
\]

where the two blocks and (A,U) are mutually independent and

\[
Q_{rs}=\mathbb E[H_rH_s],\qquad K_{rs}=\mathbb E[C_rC_s].
\]

The blocks are extended chronologically and retain their within-block time
correlations.  Starting with (u_0=U), define, for (0\le s<N),

\[
\sigma_{sr}=\mathbb E[\partial_{\xi_r}C_s],\quad 0\le r\le s,
\]

\[
b_s=\chi_s+\sum_{r\le s}\sigma_{sr}H_r
       +h\sum_{r<s}K_{rs}H_r,
\tag{2.3}
\]

\[
u_{s+1}=u_s+h b_s\phi'(u_s),\qquad H_{s+1}=\phi(u_{s+1}).
\tag{2.4}
\]

For (0\le s\le N), define

\[
\rho_{sr}=\mathbb E[\partial_{\chi_r}H_s],\quad 0\le r<s,
\]

\[
z_s=\xi_s+\sum_{r<s}(\rho_{sr}+hQ_{rs})C_r,
\tag{2.5}
\]

\[
a_s=A+h\sum_{r<s}\phi(z_r),\qquad C_s=a_s\phi'(z_s).
\tag{2.6}
\]

Only (C_0,\ldots,C_{N-1}) are needed to construct the terminal value

\[
F_N(h)=\mathbb E[a_N\phi(z_N)].
\tag{2.7}
\]

All first source derivatives in (2.3)--(2.6) are integrable.  Indeed,
repeated use of the product and chain rules expresses them as finite sums
of products of Gaussian coordinates, value fields, and bounded derivatives
of (\phi).  The value fields have polynomial growth in finitely many
Gaussian marks because (\phi) has linear growth.

## 3. Strict rank at every nonzero step

We prove the following stronger statement.

**Rank lemma.**  If (\phi\) is nonconstant and (h\ne0), then, for every
(s\ge0),

\[
Q^{[s]}=(Q_{rs})_{0\le r,s\le s}>0,
\qquad
K^{[s]}=(K_{rs})_{0\le r,s\le s}>0.
\tag{3.1}
\]

**Proof.**  Normalization gives (Q_{00}=1).  Since a nonconstant (C^1)
function has (\phi'\not\equiv0),

\[
K_{00}=\mathbb E[A^2\phi'(\xi_0)^2]
=\mathbb E\phi'(G)^2>0.
\]

We first record three elementary facts.

1. If (g:\mathbb R\to\mathbb R) is continuous and nonconstant, then
   (\operatorname{Var}(g(x+\tau G))>0) for every (x\in\mathbb R) and
   every (\tau>0).  Otherwise (g) is constant almost everywhere for a
   measure having a strictly positive density, and continuity makes it
   constant everywhere.

2. Let (X_0,\ldots,X_{r-1}) be measurable with respect to a sigma-field
   (\mathcal F).  If
   (\mathbb E\operatorname{Var}(X_r\mid\mathcal F)>0), then the Gram of
   (X_0,\ldots,X_r) is positive definite provided the old Gram is.  For
   every coefficient vector (v),
   
   \[
   \mathbb E\left(X_r-\sum_{j<r}v_jX_j\right)^2
   \ge \mathbb E\operatorname{Var}(X_r\mid\mathcal F)>0.
   \]

3. For every (s\),
   
   \[
   \mathbb P\{\phi'(u_s)\ne0\}>0.
   \tag{3.2}
   \]
   
   It holds at (s=0), since (U) has full support.  If it holds at (s)
   and (K^{[s]}>0), write the Gaussian regression
   
   \[
   \chi_s=m_s(\chi_{<s})+\tau_sG_s,
   \qquad \tau_s^2
   =K_{ss}-K_{s,<s}(K^{[s-1]})^{-1}K_{<s,s}>0.
   \]
   
   In (2.3), every term except (\chi_s) is measurable with respect to
   (\mathcal L_s=\sigma(U,\chi_0,\ldots,\chi_{s-1})).  Therefore, on
   (\{\phi'(u_s)\ne0\}), (2.4) says that (u_{s+1}), conditionally on
   (\mathcal L_s), is a nondegenerate Gaussian and hence has full support.
   Since the open set (\{x:\phi'(x)\ne0\}) is nonempty, (3.2) follows at
   (s+1).

Suppose (Q^{[s]}>0) and (K^{[s]}>0).  Condition (2.4) on
(\mathcal L_s) and use the displayed regression for (\chi_s).  On the
positive-probability event in (3.2),

\[
H_{s+1}
=\phi\!\left(x_s+h\tau_s\phi'(u_s)G_s\right)
\]

has strictly positive conditional variance by fact 1.  Fact 2 proves
(Q^{[s+1]}>0).

It remains to extend (K).  First suppose (\phi') is nonconstant.
Condition on
(\mathcal T_s=\sigma(A,\xi_0,\ldots,\xi_{s-1})).  Positivity of
(Q^{[s]}) gives

\[
\xi_s=\widetilde m_s(\xi_{<s})+\upsilon_sE_s,
\qquad \upsilon_s>0,
\]

with (E_s) independent of (\mathcal T_s).  Equations (2.5)--(2.6) give

\[
C_s=a_s\phi'(\widetilde x_s+\upsilon_sE_s),
\tag{3.3}
\]

where (a_s) is (\mathcal T_s)-measurable.  Moreover,

\[
\mathbb P\{a_s\ne0\}>0.
\tag{3.4}
\]

For (s=0), this follows from (a_0=A).  For (s\ge1), condition instead
on (A,\xi_0,\ldots,\xi_{s-2}).  The variable (z_{s-1}) is a translate
of the fresh nondegenerate Gaussian innovation in (\xi_{s-1}), while

\[
a_s=a_{s-1}+h\phi(z_{s-1}).
\]

Since (h\ne0) and (\phi) is nonconstant, this conditional random
variable is nonconstant, proving (3.4).  On the event in (3.4), (3.3) has
positive conditional variance by fact 1 applied to (\phi').  Every old
(C_r), (r<s), is (\mathcal T_s)-measurable.  Fact 2 therefore gives
(K^{[s]}>0) from (K^{[s-1]}>0).  Equivalently, after first obtaining
(Q^{[s]}), this argument constructs (K^{[s]}).

Finally suppose (\phi') is constant.  Nonconstancy of (\phi) gives
(\phi(x)=px+c) with (p\ne0).  For (s\ge1), condition on
(A,\xi_0,\ldots,\xi_{s-2}).  Since

\[
C_s=pa_s=pa_{s-1}+hp^2z_{s-1}+hpc
\]

and (z_{s-1}) contains the fresh innovation of (\xi_{s-1}) with
coefficient one, the conditional innovation variance of (C_s) is

\[
h^2p^4\left(
Q_{s-1,s-1}-Q_{s-1,<s-1}
(Q^{[s-2]})^{-1}Q_{<s-1,s-1}
\right)>0.
\]

(For (s=1), the inverse term is absent.)  The old (C_0,\ldots,C_{s-1})
are measurable under this conditioning.  Fact 2 again proves the strict
(K)-extension.

Starting with (Q^{[0]},K^{[0]}>0), extend (Q^{[s]}) to
(Q^{[s+1]}), then extend (K^{[s]}) to (K^{[s+1]}).  This mutual
induction proves (3.1).  Notice that it uses no Taylor expansion and no
limit (h\to0).  \(\square\)

## 4. All reused-matrix responses

We first record the adaptive invariant, because conditioning on random
query spans as if they had been fixed before seeing the matrix would be
incorrect.  Let \(\mathcal F_m\) contain the external marks, the first
\(m\) predictable queries, and their revealed matrix actions.  Let
\(H_m,C_m\) collect the row and column queries revealed so far.  Inductively,

\[
\mathcal L(W\mid\mathcal F_m)
=\mathcal L\!\left(
M_m+P_{C_m}^\perp G_mP_{H_m}^\perp
\,\middle|\,\mathcal F_m\right),
\tag{4.1}
\]

where \(G_m\) is a fresh iid standard Gaussian matrix and

\[
M_m=P_{C_m}W+WP_{H_m}-P_{C_m}WP_{H_m}
\]

is determined by the revealed actions.  This is true with empty blocks at
\(m=0\).  If the next predictable query is a row query \(v\), decompose
\(v=P_{H_m}v+v_\perp\).  Conditionally on \(\mathcal F_m\), the only new
random part is \(P_{C_m}^\perp G_mv_\perp\).  For
\(v_\perp\ne0\), put \(e=v_\perp/\|v_\perp\|\).  The Gaussian matrix projections
\(G_mee^T\) and \(G_m(I-ee^T)\) are independent.  Revealing the former
therefore leaves a fresh residual
\(P_{C_m}^\perp G_{m+1}P_{\operatorname{span}(H_m,v)}^\perp\), which is
exactly (4.1) at \(m+1\).  If \(v_\perp=0\), nothing new is revealed.  A
column query is equally explicit.  For a predictable \(c_*\), write
\(c_*=P_{C_m}c_*+c_\perp\).  Its only new random action is
\(P_{H_m}^\perp G_m^Tc_\perp\).  If \(c_\perp\ne0\), put
\(e=c_\perp/\|c_\perp\|\).  The left projections
\(ee^TG_m\) and \((I-ee^T)G_m\) are independent Gaussian matrices;
revealing \(G_m^Te\) therefore leaves the fresh residual
\(P_{\operatorname{span}(C_m,c_*)}^\perp G_{m+1}P_{H_m}^\perp\).
If \(c_\perp=0\), again no new Gaussian projection is revealed.  This
proves (4.1) for every one of the \(2N+1\) alternating adaptive actions.

The corresponding orthogonal decomposition is

\[
W=P_CW+WP_H-P_CWP_H+P_C^\perp\widetilde WP_H^\perp,
\tag{4.2}
\]

conditional on all revealed actions.  Predictability is essential: after
(Y^s), the query (C^s) is known; after (D^s), the query (H^{s+1})
is known.  Thus (2.2), including the dependence of (H^1) on (D^0),
satisfies the hypothesis of (4.1).

Here is a single block calculation that proves every response, rather than
assuming a new cavity identity at each time.  Before a new row query, write

\[
y=\xi+P c,\qquad d=\chi+S h_0,
\tag{4.3}
\]

for the old raw row actions, old raw column actions, and old query blocks.
The strictly causal entries of (P) are the (\rho)'s, and the causal
entries of (S) are the (\sigma)'s.  Let (Q=\mathbb E[h_0h_0^T]),
(K=\mathbb E[cc^T]).  Gaussian integration by parts gives

\[
R:=\mathbb E[cy^T]=SQ+KP^T.
\tag{4.4}
\]

For the new lower query (H_*=H_s), put

\[
q=\mathbb E[h_0H_*],\qquad
\rho=\mathbb E[\nabla_\chi H_*].
\]

Then

\[
v:=\mathbb E[dH_*]=K\rho+Sq.
\tag{4.5}
\]

The population row-regression formula is

\[
y^TQ^{-1}q+c^TK^{-1}(v-RQ^{-1}q)+\text{innovation}.
\]

Substitution of (4.3)--(4.5) cancels
(c^TP^TQ^{-1}q) and leaves

\[
Y^s=\xi_s+\sum_{r<s}\rho_{sr}C_r.
\tag{4.6}
\]

Before a new column query, allow (h_0,y) to include the just-constructed
time-(s) feature query and row action, while (c,d) stop at time (s-1).
For (C_*=C_s), put

\[
k=\mathbb E[cC_*],\qquad
\sigma=\mathbb E[\nabla_\xi C_*].
\]

Gaussian integration by parts gives

\[
r:=\mathbb E[yC_*]=Q\sigma+Pk.
\tag{4.7}
\]

The population column-regression formula is

\[
d^TK^{-1}k+h_0^TQ^{-1}(r-R^TK^{-1}k)+\text{innovation}.
\]

Equations (4.3), (4.4), and (4.7) cancel the term
(h_0^TS^TK^{-1}k) and leave

\[
D^s=\chi_s+\sum_{r\le s}\sigma_{sr}H_r.
\tag{4.8}
\]

Equations (4.6) and (4.8), after adding the exact learned terms (2.1),
are precisely (2.3) and (2.5).  Since the same two matrix identities apply
at every stage, this closes all reused-(W/W^T) response terms for arbitrary
finite (N).

## 5. Concentration and uniform integrability

For completeness, fix (N,h), and define

\[
\gamma_{N,h}=\frac12\min_{0\le s<N}
\{\lambda_{\min}(Q^{[s]}),\lambda_{\min}(K^{[s]})\}>0.
\tag{5.1}
\]

The following stopped induction covers all (2N+1) actions.

At each action generate its orthogonal residual in (4.1) with a fresh iid
standard Gaussian vector, and use that same vector in the population
Gram--Schmidt construction.  Stop at the first action at which an empirical
old Gram has eigenvalue below (\gamma_{N,h}), or a nonterminal empirical
innovation Schur complement is below (\gamma_{N,h}).  Suppose all fields
through the preceding action converge in normalized (L^p), for every
finite (p), and have uniformly bounded moments.  Then:

1. Every new query is a polynomial-Lipschitz coordinate function of those
   fields.  The mean-value theorem, bounded derivatives of (\phi), and
   Holder's inequality give normalized (L^p) convergence of the new
   query.

2. An empirical Gram or cross-moment is split into its actual-to-ideal
   difference and its iid ideal fluctuation.  The first tends to zero by
   Cauchy--Schwarz and step 1; Rosenthal's inequality makes the second
   (O(n^{-1/2})) in every fixed (L^p).

3. On the stopped event, inverse Grams have norm at most
   (\gamma_{N,h}^{-1}).  The inverse identity
   (A^{-1}-B^{-1}=A^{-1}(B-A)B^{-1}) shows convergence of every regression
   coefficient.  Innovation variances converge as Schur complements.  Their
   square roots converge by
   ( |\sqrt x-\sqrt y|\le\sqrt{|x-y|}); away from zero the ordinary
   Lipschitz estimate applies.

4. For a fixed (r)-column old-query matrix (X), conditionally on (X),
   
   \[
   \left\|\|P_Xg\|_{n,p}\right\|_{L^q(g\mid X)}
   \le C_{p,q,r,\gamma_{N,h}}n^{-1/2}
       \sum_{j=1}^r\|X_j\|_{n,p}.
   \]
   
   Hence replacing (P_X^\perp g) by the coupled full iid vector changes
   the action by (o_{L^p}(1)).

These four statements prove the induction step.  They also show, by running
the empirical estimates at an arbitrarily high moment order and using
Markov's inequality, that the probability of a first stopping failure is
(O(n^{-m})) for every fixed (m).

It remains to remove stopping.  For (|h|\le H), define scalar majorants
recursively by

\[
\mathsf h_s=M_\phi(1+\mathsf u_s),\quad
\mathsf z_s=\mathsf w_s\mathsf h_s,\quad
\mathsf c_s=M_\phi\mathsf a_s,\quad
\mathsf b_s=\mathsf w_s\mathsf c_s,
\]

\[
\mathsf a_{s+1}=\mathsf a_s+HM_\phi(1+\mathsf z_s),\quad
\mathsf u_{s+1}=\mathsf u_s+HM_\phi\mathsf b_s,
\]

\[
\mathsf w_{s+1}=\mathsf w_s+H\mathsf c_s\mathsf h_s.
\tag{5.2}
\]

Starting from the normalized Gaussian norms of (A,U) and
(\|W\|_{\rm op}/\sqrt n), (5.2) is a finite polynomial with nonnegative
coefficients and dominates every raw network field through time (N).
The starting quantities have moments of every order uniformly in (n).
Choose the high-moment exponent in the stopping estimate larger than the
finite polynomial degree in (5.2); Holder's inequality then removes the
stopping indicator.  This proves normalized (L^p) convergence of all raw
fields, Grams, and cross-moments.

Finally,

\[
|f_n^N|
\le \|a^N\|_{n,2}\|\phi(z^N)\|_{n,2}
\le M_\phi\mathsf a_N(1+\mathsf z_N).
\]

The right side is bounded in (L^{1+\delta}), uniformly in (n), for any
fixed (\delta>0).  The terminal averages are uniformly integrable, so the
field convergence passes to expectations and proves (1.1).

This is a literal finite induction: it begins at (Y^0), performs the four
displayed estimates at each of exactly (2N+1) actions, and terminates at
(Y^N).  No unproved infinite-time state-evolution assertion is used.

## 6. Consequences for a general time-doubling theorem

The width-first bridge presents no obstruction for any fixed integer (t):
apply the theorem with (N=2t) separately at each fixed nonzero (\eta).
The rank lemma is valid on the whole punctured real line.

There cannot, however, be a useful (t)-uniform activation-envelope
estimate on a fixed step interval merely from bounded activation derivatives:
even affine activations generate iterated linear recurrences whose moments
grow exponentially in (t|\eta|).  A polynomial-in-(t) majorant must be
stated on a total-time interval

\[
|\eta|\le h_\phi/t
\tag{6.1}
\]

(or on a smaller interval).  This restriction comes from regularity and
remainder control, not from Gaussian Gram rank.

The cubic coefficient for

\[
\Delta_t(\eta)=F_t(2\eta)-F_{2t}(\eta)
\]

obtained after independently differentiating the width-first DAG is

\[
\kappa_t=-\frac{t(2t-1)}2\,(S_\phi+4H_\phi).
\tag{6.2}
\]

Thus the leading coefficient is exactly quadratic in (t).  The rank and
identification theorem above does not by itself prove that the fifth-order
remainder has only quadratic (t)-growth.  A direct fifth-derivative
majorant gives at best (C_\phi t^5|\eta|^5); exploiting equal total time
can cancel the degree-five coefficient and may improve this to
(C_\phi t^4|\eta|^5), but a (C_\phi t^2|\eta|^5) claim requires an
additional cancellation and must not be inferred from (6.2).  Therefore
the fixed-(h) part is proved here, while a globally quadratic-in-(t)
remainder remains a separate proof obligation.
