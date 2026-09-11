# Source calculus, second phase: candidate uniform output C2 estimate

Status: candidate proof requiring independent reconstruction. This phase read
the coordinator's `source_calculus_candidate.md` after the first-round report
was frozen. It preserves both source orientations, all residual feedback, and
the actual alpha/beta corrections representing A0 and its adjoint. It does
not assert an ambient L2 derivative of the raw flow.

The proof below establishes a proposed uniform first/second derivative bound
for the scalar predictions of finite population raw Euler programs. Its
mechanism is a short-interval estimate. A covariance derivative involving a
new lower source can act only on the change of the lower feature since the
start of the interval; every fixed source derivative of that change is O of
the interval length. No product of atom masses is required for upper source
derivatives.

## 1. Statement and derivative conventions

Take a fixed smaller ball whose closure lies inside C.4.7.N-cap's law
neighborhood. Decrease the admitted maximum step if necessary. Let

\[
 \lambda=\sum_{a=1}^N p_a\delta_{(\sqrt2u_a,y_a)},\qquad
 p_a>0,\quad\sum_ap_a=1,
\]

be in this ball. Inputs and labels remain fixed when differentiating masses.
Let s,t be zero-sum real mass vectors, S=sum_a|s_a| and R=sum_a|t_a|.
Derivatives are taken on the relative open set of masses with positive
coordinates and law in the capped ball. All covariance matrices may be
singular there. At its boundary the assertions mean the continuous one-sided
limits described below.

Write f_h(lambda;t0,u) for the scalar prediction from the population raw Euler
algorithm through time t0<=40, with its exact population residuals. A partial
final step is allowed. The proposed conclusion is a finite C, depending only
on the chosen ball, Y and T=40, such that

\[
 \sup_{h,t_0,u}|\partial_s f_h|\le CS,
 \qquad \sup_{h,t_0,u}|\partial_s\partial_t f_h|\le CSR.       \tag{A}
\]

The constant is independent of N, the positive masses, covariance rank and
number of steps. Consequently (A) holds in L2(circle), with its normalized
measure, with the same constant.

Use the exact finite source expressions N2–N8. A prime on a scalar
coefficient or covariance means its full mass derivative. A superscript [s]
on a coordinate expression means its explicit mass derivative **holding all
Gaussian source coordinates fixed**. Thus, for an upper expectation G,

\[
 \partial_s EG=E G^{[s]}+
       \tfrac12\sum_{pq}(C_\xi^{s})_{pq}E\partial_{pq}G,     \tag{B}
\]

and similarly for the lower population with C_zeta. The first-round Lemma 2
proves this formula at singular covariance. Source derivatives in (B) retain
the fixed named-slot convention. Initialized lower roots are unchanged and
are included in the expectation; their distribution has no mass derivative.

At each fixed graph all coefficients and outputs have these first and mixed
second derivatives. To verify existence rather than assume it, proceed in
the construction order N2–N8. The next lower features are smooth coordinate
expressions in earlier coefficients. Their expectations determine the next
forward covariance and alpha rows. The forward expression then determines
upper fields, upper contractions and beta. These determine the next reverse
covariance and lower update. At each expectation use the first-round Gaussian
lemma. The finite coordinate expressions and each fixed derivative have
polynomial Gaussian envelopes on compact mass parameter sets. Thus the
lemma's hypotheses hold at every finite step. No inverse Gram or
differentiated covariance square root is used.

## 2. Base source jets and increments

For a named expression V, let

\[
 J_j(V)=\sum_{p_1,...,p_j}|\partial_{p_1}\cdots
              \partial_{p_j}V|,\qquad J_0(V)=|V|.
\]

The first-round Lemma 1 gives every fixed-order upper source jet of c,
Delta and hidden activations a uniform pointwise bound; jets of upper Z of
positive order also have that bound. Every fixed-order lower jet has all
finite moments uniformly. A Q value is Gaussian plus a bounded correction;
its positive-order jets equal a direct first impulse plus a bounded D row
acting on lower feature jets. In particular their finite moments are
uniform. The needed orders here are base jets through five, first explicit
mass derivatives through source order three, and second explicit mass
derivatives through source order one.

Let b be a node, and consider later nodes k with
ell_bk=sum_{j=b}^{k-1}h_j<=ell. All expressions can be regarded as functions
on the same enlarged source list, by giving unused coordinates derivative
zero. Denote H_b(u)=phi(w_b.u), including its passive-query extension.
For each fixed j and p,

\[
 \|J_j(w_k-w_b)\|_p+
       \sup_u\|J_j(H_k(u)-H_b(u))\|_p\le C_{j,p}\ell.       \tag{C}
\]

For the first bound differentiate the sum of lower updates over [b,k).
Leibniz and the finite partition rule bound each jet of
phi'(w_j.u_a)Q_ja by a finite sum of products of base jets and a Q value.
Their Lp norms are uniformly bounded by Holder. Multiplication by
|gamma_ja|<=2R0 h_j p_a and Minkowski then costs sum h_j p_a<=ell.
For the second bound use

\[
 H_k(u)-H_b(u)=\int_0^1\phi'((w_b+v(w_k-w_b)).u)
                         ((w_k-w_b).u)\,dv.
\]

After j source derivatives, every product contains at least one jet of
w_k-w_b. All remaining factors are bounded activation derivatives or base
w jets at the two endpoints. Apply the first bound at a larger moment
order and Holder, then integrate in v. This proves (C), including j=0.
It uses marginal Q moments summed over time; no supremum of Q values is
placed inside a moment.

For any product of two lower features, with each endpoint either before b
or in [b,k], replace each new endpoint by H_b at the **same input** and
retain old endpoints. Call the resulting product its boundary version.
The difference between the product and its boundary version has the bound
(C) at every fixed jet order. Subtract the products one factor at a time
and apply the product rule and Holder. The boundary version uses only
reverse slots strictly before b.

## 3. Exact explicit first derivative recursions

For clarity suppress the fixed input vectors in source subscripts and write
W=w^[s], C=c^[s], Z=Z2^[s], V=Delta2^[s], P=Q^[s]. Then

\[
 \gamma_{ka}^{s}=-2h_k(s_a r_{ka}+p_a r_{ka}^{s}),            \tag{D}
\]
\[
 P_i=\sum_{q\le i}D_{iq}^{s}H_q+
             \sum_{q\le i}D_{iq}\phi'(w_q.u_q)(W_q.u_q),
\]
\[
 W_{k+1}=W_k+\sum_a\gamma_{ka}^{s}\phi'(w_k.u_a)Q_{ka}u_a
   +\sum_a\gamma_{ka}u_a
      [\phi''(w_k.u_a)Q_{ka}(W_k.u_a)+\phi'(w_k.u_a)P_{ka}],
                                                                    \tag{E}
\]
\[
 Z_i=\sum_{q<i}F_{iq}^{s}\Delta_q+\sum_{q<i}F_{iq}V_q,
\]
\[
 C_k=\sum_{q<k}\{\gamma_q^{s}\phi(Z_q^2)
                           +\gamma_q\phi'(Z_q^2)Z_q\},
 \qquad V_i=\phi'(Z_i^2)C_k+c_k\phi''(Z_i^2)Z_i.            \tag{F}
\]

These are explicit derivatives: there is no source derivative xi^[s] or
zeta^[s] in (E)–(F). Their changing covariance enters precisely through
(B), in every contraction and coefficient. In particular

\[
 F_{iq}^{s}=\alpha_{iq}^{s}+\gamma_q^{s}E H_iH_q
                              +\gamma_q\partial_sE H_iH_q,
\]
\[
 D_{iq}^{s}=\beta_{iq}^{s}+
  \mathbf1_{q<i}\{\gamma_q^{s}E\Delta_i\Delta_q
                  +\gamma_q\partial_sE\Delta_i\Delta_q\}. \tag{G}
\]

The covariances are Cxi_ij=E Hi Hj and Czeta_ij=E Delta_i Delta_j.
The residual derivative is the full derivative of E c_k phi(Z_ku^2),
and alpha^s, beta^s are the full derivatives of E partial_source H and
E partial_source Delta. Formula (B), not just (E)–(F), must be used for
these derivatives.

## 4. The local response estimate

Here is a precise norm in which to organize the interval induction. Suppose
all derivative data on the prefix strictly before b, together with explicit
state derivatives at b, already have uniform bounds. For deterministic
data these bounds comprise: absolute residual derivatives at every passive
input; entry suprema of both covariance derivative arrays; and absolute
row sums of F,D,alpha,beta derivative arrays, each uniform in the current
passive input. For random coordinate data they comprise all finite moments
of explicit lower state/source jets through order three and explicit upper
state/source jets through order three. Bounds on old expressions are taken
on their own marginal Gaussian source laws. Enlarging the source list does
not change any such marginal.

Let H denote a finite aggregate of the previously proved bounds and S;
whenever a larger finite moment is used, H includes that old bound. Let E
be the maximum of the deterministic derivative quantities just listed over
all newly constructed rows or covariance pairs whose latest node belongs to
[b,k]. Include the derivative F,D rows themselves in E. At a fixed graph E
is finite. Constants multiplying ell E below depend only on base caps and
fixed moment/jet orders; they do not depend on the history derivative bounds.
Constants denoted C_H may depend on those already known bounds.

The claim is

\[
                         E\le C_H+C\ell E.                 \tag{H}
\]

The following paragraphs prove every part of this inequality.

**Lower explicit response.** Equations (D)–(E), including their source
derivatives through order three, give

\[
 \max_{b\le i\le k}\|J_j(W_i)\|_p
                  \le C_{H,j,p}+C_{j,p}\ell E,\qquad j\le3. \tag{I}
\]

To check the propagation, first take j=0. The highest unknown W term has
pointwise coefficient bounded by
2R0 h_i(D0+2q_i), where q_i=sum_a p_a|Q_ia|, after taking the maximum of
the unknown W norms over current and earlier nodes in the interval. Its
propagator is bounded by exp(2R0D0 T+4R0 sum h_iq_i), with every fixed
moment by N11. All D^s-row forcing in the interval is bounded by h_i C E
times bounded lower features. Residual forcing in gamma^s is bounded by
h_i p_a E |Q_ia|. Direct s_a forcing has the same estimate with the
probability weights |s_a|/S and factor S. Minkowski and Holder bound their
integrated Lp norms by C_p ell(E+S). The random propagator can be included
by Holder at a higher fixed moment. Its joint dependence on the forcing
does not require independence.

For j>0, applying j source derivatives to (E) has the same highest-jet
linear coefficient. The other terms are products of lower-order response
jets and fixed-order base jets, or D^s rows and base jets. The source
derivatives of a direct Q impulse have total row sum one at order one and
zero at larger orders; thus no unweighted count of slots occurs. Induction
on j, the same random propagator, and Holder give (I). One can verify the
factor ell for the unknown-history-free part pointwise before taking
moments: its forcing contains only sums over interval updates, and every
such sum has Lp norm at most C_p ell E. Multiplication by the propagator
and finitely many base-jet factors preserves this estimate by Holder.
Terms from old response jets and explicit initial W_b contribute to C_H.

The corresponding explicit derivatives of H_i(u), and of products of two
lower features, obey (I) by the partition/product rules. The coefficient
of ell E is uniform over inputs. This reasoning gives bounds at every
finite p; it therefore supplies the higher old moments needed on the next
interval, without any repeated unproved Lp action bound.

**Lower Gaussian expectation terms.** Split any covariance derivative
array into its old-old block and its complement. The old-old block is
known from the prefix. Its contraction against an absolute source tensor
sum costs C_H by the base jet bounds. For the complement, any nonzero
entry has at least one reverse source at or after b. A boundary lower
expression uses only old reverse slots, so its source derivative with
respect to that new slot vanishes exactly. Subtracting the boundary
expression before contracting therefore gives, by (C),

\[
 \left|\sum_{pq\text{ not old-old}}(C_\zeta^s)_{pq}
                         E\partial_{pq}G\right|\le C\ell E,\tag{J}
\]

for G=Hi Hj or G=Hi. For the alpha row sum use G=partial_l Hi, sum also
over l, and apply (C) at source order three. The same cancellation applies
even when l is old: the covariance pair still contains a new source. For
new l the boundary first derivative itself is zero. This proves

\[
 \sup_{i,j}|(C_\xi^s)_{ij}|+
        \sup_i\sum_q|\alpha_{iq}^s|\le C_H+C\ell E.        \tag{K}
\]

Here i,j range over newly relevant pairs and their old partners; old-old
pairs already have their history bound. Equations (I), (B) and (J) account
respectively for explicit, old covariance, and new covariance terms.

**The F rows.** In (G), the alpha row has (K). Terms with q before b have
known gamma_q^s and total sum |gamma_q|<=2R0 T. Their changing lower
contractions have (K), so these terms cost C_H+C ell E. Terms with q in
the interval have sum |gamma_q^s|<=C ell(S+E), by (D). All lower
contractions are bounded by one. Thus

\[
                         \sup_i\sum_q|F_{iq}^s|
                                      \le C_H+C\ell E.     \tag{L}
\]

**Upper explicit response.** In (F), old V_q,C_b and their source jets
have known bounds. New F^s rows have (L). Multiplication by base Delta
jets is bounded pointwise, by the first-round upper jet lemma. The
propagating F row has the entrywise density |F_i,sb|<=fB h_s p_b.
The c propagation carries gamma's identical time/atom density. Taking
source jet row sums through order three, the product rule and base upper
jet bounds therefore give a deterministic Volterra estimate. Its highest
response-jet coefficient is bounded by fB(2R0T+2C0), as in first-round
equations (3)–(4); lower response jets are handled inductively. The only
new external terms are (L), interval gamma^s terms C ell(S+E), and
known old-prefix terms. Discrete Gronwall proves

\[
 \max_{b\le i\le k}\{J_j(Z_i)+J_j(V_i)+J_j(C_i)\}
                      \le C_{H,j}+C_j\ell E,\qquad j\le3.  \tag{M}
\]

This bound is pointwise for explicit upper derivatives. The coefficients
are deterministic and base upper jets are pointwise bounded. No density
product for repeated source indices has been used.

**Upper expectations, beta, and reverse covariance.** The full forward
covariance derivative array has entry supremum bounded by (K), including
its old-old block. Apply (B) to c phi(Z), Delta_i Delta_j, and to
partial_l Delta_i, summing over l in the last case. Formula (M) bounds the
explicit derivatives. The first-round upper source tensors of orders two
and three bound the covariance contributions against the entry supremum
in (K). Hence

\[
 \sup_{i,u}|r_i^s(u)|+\sup_{i,j}|(C_\zeta^s)_{ij}|
             +\sup_i\sum_q|\beta_{iq}^s|\le C_H+C\ell E.   \tag{N}
\]

This step is exactly where a new forward covariance first becomes a new
reverse covariance; no reverse covariance estimate was assumed in proving
(K), except as the unknown E multiplied by ell in (J).

Finally (G)'s D row is bounded using (N): old gamma^s rows are known,
sum old |gamma|<=2R0 T, new gamma^s rows sum to C ell(S+E), and all
base upper contractions are bounded by C0^2. Therefore

\[
                         \sup_i\sum_q|D_{iq}^s|
                                      \le C_H+C\ell E.     \tag{O}
\]

Together (K)–(O) bound every deterministic quantity used to define E and
prove (H). All source slot sums were either full absolute tensor sums or
the explicit time/atom density of gamma or F. No minimum mass or source
count entered.

## 5. Iterating the first derivative estimate through time 40

Choose ell>0 with C ell<=1/2 in (H). The constant C depends only on the
uniform base caps and on the finite collection of jet orders used in
(I)–(N), not on a previously obtained response bound. Decrease the maximum
step to at most ell/2. Greedily divide nodes into blocks of total length
between ell/2 and ell, except possibly the final block. There are at most
2T/ell+1 blocks, independent of the mesh.

At the first block, initialization has zero explicit mass derivatives and
zero covariance/coefficient derivatives. The direct s_a terms are linear
in S. Thus (H) gives E<=C S. Equations (I) and (M) then give the explicit
source-jet bounds, for every finite p, that comprise the next block's
history. The same argument on the next block gives finite bounds linear in
S. Iterate over the bounded number of blocks. Linearity of all first
derivative equations preserves the factor S; constants may increase over
this fixed number of blocks but remain independent of support and mesh.

This proves uniform first derivative bounds for all deterministic arrays
and for explicit lower/upper source jets through order three, at every
finite moment needed. In particular the full passive output derivative
has the first bound in (A).

## 6. Mixed second derivatives

Now fix s,t and use the just-proved first derivative bounds globally.
Denote mixed second derivatives by st. The exact weight formula is

\[
 \gamma_{ka}^{st}=-2h_k
        (s_a r_{ka}^t+t_a r_{ka}^s+p_a r_{ka}^{st}).         \tag{P}
\]

The first two terms are known, with total absolute sum over an interval at
most C ell SR. The last term is the same linear unknown term as in (D).
For any expectation the exact mixed version of the Gaussian formula is

\[
 \begin{aligned}
 \partial_{st}EG={}&EG^{[st]}
   +\tfrac12\sum_{pq}(C^{st})_{pq}E\partial_{pq}G\\
 &+\tfrac12\sum_{pq}(C^s)_{pq}E\partial_{pq}G^{[t]}
  +\tfrac12\sum_{pq}(C^t)_{pq}E\partial_{pq}G^{[s]}\\
 &+\tfrac14\sum_{pq,lr}(C^s)_{pq}(C^t)_{lr}
                                     E\partial_{pqlr}G.
 \end{aligned}                                                \tag{Q}
\]

The last three terms are bounded globally by CSR: use the first covariance
entry-supremum bounds, the first explicit source jets through order three,
and base source jets through order five. For alpha or beta, G already has
one source derivative and its row index is also summed, explaining orders
three and five. Scalar contractions require no higher orders.

Differentiating (E)–(G) twice gives the **identical linear principal system**
in W^[st], C^[st], Z^[st], V^[st], the st coefficient rows and st residuals,
with (P)'s p_a r^[st] term. Every remaining explicit term contains a
product of two first derivatives or a mass direction times a first
derivative. Its integrated source-jet norm is bounded by CSR, since the
first derivative source jets have all finite moments and the update
weights remain h_k p_a or h_k s_a/h_k t_a. For example the additional
lower terms include gamma^s phi'' Q W^t,
gamma phi''' Q W^s W^t,
gamma phi''(P^s W^t+P^t W^s), and their symmetric counterparts; Holder
and the first bounds control them. In the F,D derivative rows the extra
terms are gamma^s times a first contraction derivative and gamma^t times
the other, and in upper expressions they are F^s V^t+F^t V^s and the
ordinary product derivatives of c phi'(Z). Their full row sums are
bounded by the already proved first row-sum estimates. There is no new
unknown quadratic term of second order.

Repeat the block argument with E2 the same deterministic norm for st
derivatives and with explicit second response source jets through order
one in the history. The pure C_zeta^[st] term in (Q) has precisely the
old-old/new-block split (J), using the base increment tensor. Its unknown
part is C ell E2. The remaining terms in (Q) are already known CSR.
Equations (I)–(O) for the linear principal system are unchanged. Thus

\[
                         E_2\le C_{H_2}+CSR+C\ell E_2.     \tag{R}
\]

The same ell absorbs the last term: its coefficient depends only on the
base, not on the first derivative magnitude. Starting from zero second
initial data, iterate over the same finite number of blocks. The known
first-order products scale as SR, so all second bounds scale as SR.
The full output expectation, covered by (Q), has the second bound in (A).

This argument applies directly to mixed directions, so it does not require
polarization near a one-sided probability boundary.

## 7. Boundary, rank, observations, and limits of the claim

The calculations on positive masses have constants independent of their
minimum. For a fixed finite support, the coefficient and derivative
expressions obtained by the finite chronological Gaussian formulas extend
continuously as masses approach zero while the law stays in the ball.
At each fixed graph the expressions have common polynomial Gaussian
envelopes locally in the parameters; bounded covariance and dominated
convergence verify this claim inductively. Adding unused zero-mass slots
does not change the value recursion. Taking an interior approximation
therefore gives the same bounded one-sided first/second derivatives along
any admissible finite-law segment or rectangle, including directions
adding an atom. Source covariances can remain singular throughout; no
full-rank interior approximation is being made.

The estimates are uniform in a passive u. At non-node times append the
corresponding shorter final raw Euler step and recompute observations, as
in C.4.7. The same caps and proof apply. Thus (A) concerns the whole
physical interval and whole circle, and implies its Hilbert-output form.

This is a candidate analytic completion of the finite-program bound. The
remaining sampling and continuous-mesh passages should be checked against
their own exact requirements; they are not silently part of (A). In
particular the proof does not claim that A0 or A0* acts boundedly on Lp,
that upper repeated-source jets carry products of atom masses, that raw
L2 tangent multiplication is bounded, or that a finite-width derivative
can be interchanged with a width limit.

The fragile points for independent reconstruction are explicit: (C)'s
increment jets, the old-old cancellation (J) for alpha row sums as well as
lower covariance products, the uniform coefficient of ell E in (I), and
the assertion that the second-order principal system in (R) has exactly
the first-order coefficient. These are the estimates on which (A) rests.
