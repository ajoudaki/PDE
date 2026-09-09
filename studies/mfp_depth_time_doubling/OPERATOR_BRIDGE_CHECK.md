# Fixed Gaussian-operator bridge: independent check

This note isolates the construction that replaces the failed finite-list
oracle argument.  It is deliberately stated only for the finite smooth
core reached by finitely many Euler steps and finitely many directional
derivatives.

## 1. Simultaneous construction

For each hidden layer (a), choose a standard Gaussian probability space
((\Omega_a,\mathcal F_a,\mathbb P_a)), and put

\[
 H_a=L^2(\Omega_a).
\]

Split its first Gaussian chaos into mutually orthogonal infinite-dimensional
closed subspaces, one for each incident connector, plus an orthogonal
remainder.  Orthogonal Gaussian first-chaos blocks are independent.  Since
every (H_a) and every chosen chaos block is a separable infinite-dimensional
real Hilbert space, for (2\le a\le L) there are onto isometries

\[
 I_a:H_{a-1}\longrightarrow \mathcal C_a^{I}\subset H_a,
 \qquad
 J_a:H_a\longrightarrow \mathcal C_{a-1}^{J}\subset H_{a-1}.
 \tag{1.1}
\]

The blocks \(\mathcal C_a^I\) and \(\mathcal C_a^J\) are chosen orthogonal,
and the choices for different connectors use disjoint blocks.  Choose the
bottom seed (U\in H_1) and top seed (A\in H_L) as independent standard
Gaussian coordinates in the unused blocks.  Define

\[
 \boxed{W_{a,0}=I_a+J_a^*:H_{a-1}\to H_a},
 \qquad
 \boxed{W_{a,0}^*=I_a^*+J_a}.
 \tag{1.2}
\]

These are genuine bounded operators, with norm at most (2).  They are not
claimed to be Hilbert--Schmidt and are never included among the trainable
Hilbert--Schmidt perturbations.

For any finite list (x_1,\ldots,x_p\in H_{a-1}), the variables
(I_ax_1,\ldots,I_ax_p\) are jointly centered Gaussian and

\[
 \mathbb E[(I_ax_i)(I_ax_j)]=\langle x_i,x_j\rangle.
 \tag{1.3}
\]

The analogous assertion holds for (J_ac_j), and the primitive source
families belonging to distinct allocated blocks are independent.  Thus
(1.1) constructs all enlargements at once; no covariance square root or
Gram inverse is selected later.

## 2. Exact response identity, including singular histories

Let (c_1,\ldots,c_q\in H_a), put \(\chi_j=J_ac_j\), and suppose

\[
 x=\psi(\chi_1,\ldots,\chi_q,\zeta)\in H_{a-1},
 \tag{2.1}
\]

where \(\zeta\) is independent of the (J_a)-chaos used in (2.1), and
\(\psi\) is (C^1) with an integrable derivative envelope.  Then

\[
 \boxed{J_a^*x=\sum_{j=1}^q
       \mathbb E[\partial_j\psi(\chi,\zeta)]c_j.}
 \tag{2.2}
\]

Indeed, for arbitrary (y\in H_a), possibly outside the span of the
(c_j), degenerate Gaussian integration by parts gives

\[
\begin{aligned}
 \langle y,J_a^*x\rangle
 &=\mathbb E[(J_ay)\psi(\chi,\zeta)]\\
 &=\sum_{j=1}^q
   \mathbb E[(J_ay)\chi_j]\,
   \mathbb E[\partial_j\psi(\chi,\zeta)]\\
 &=\left\langle y,
   \sum_{j=1}^q\mathbb E[\partial_j\psi]c_j\right\rangle.
\end{aligned}
\]

This proves (2.2) by the Riesz theorem.  The argument uses no covariance
inverse, so it also covers linearly dependent (c_j).  Equivalently, the
right side is the first-chaos projection characterized intrinsically by
(J_a^*x), and is therefore independent of a redundant coordinate
description.  Interchanging (I_a) and (J_a) gives

\[
 I_a^*c=\sum_i\mathbb E[\partial_i\widetilde\psi]x_i
 \tag{2.3}
\]

whenever (c) depends cylindrically on the forward sources
(I_ax_i).  Equations (2.2)--(2.3) are exactly the row and column response
sums.

## 3. Equality with the inverse-free temporal DAG

At time (s), let

\[
 K_{a,s}=h\sum_{r<s}D_{a,r}\otimes X_{a-1,r}.
 \tag{3.1}
\]

Induction over the forward/backward chronology shows that
(X_{a-1,s}) depends on the (J_a)-block only through the already exposed
sources (J_aD_{a,r}), (r<s), whereas (D_{a,s}) depends on the
(I_a)-block only through (I_aX_{a-1,r}), (r\le s).  This is true at
initialization by the orthogonal block allocation, and every update in
(3.1) uses only a past-time field.

Define

\[
 \xi_{a,s}=I_aX_{a-1,s},\qquad
 \chi_{a,s}=J_aD_{a,s}.
\]

Using (2.2), (2.3), and the rank-one contraction gives, as equalities in
the corresponding (H_a),

\[
\begin{aligned}
 (W_{a,0}+K_{a,s})X_{a-1,s}
 ={}&\xi_{a,s}
 +\sum_{r<s}\rho^a_{sr}D_{a,r}
 +h\sum_{r<s}Q^{a-1}_{rs}D_{a,r},
 \tag{3.2}
\end{aligned}
\]

\[
\begin{aligned}
 (W_{a,0}+K_{a,s})^*D_{a,s}
 ={}&\chi_{a,s}
 +\sum_{r\le s}\sigma^a_{sr}X_{a-1,r}
 +h\sum_{r<s}K^a_{rs}X_{a-1,r}.
 \tag{3.3}
\end{aligned}
\]

By (1.3), the raw sources in (3.2)--(3.3) have exactly the Gram
covariances in the inverse-free DAG.  Their allocated first-chaos blocks
have exactly the required independence.  Equations (3.2)--(3.3) then prove
by chronological induction that the fixed-operator construction and the
inverse-free Gaussian DAG have identical nodes for every finite horizon
and every fixed step for which the finite moments exist.  This includes
(h=0): a singular history is merely a linearly dependent list of vectors
inside a fixed Hilbert space.

## 4. Gradient structure on the reachable smooth core

Let

\[
 \mathcal P_L=H_L\oplus
 \bigoplus_{a=2}^L\operatorname{HS}(H_{a-1},H_a)\oplus H_1.
\]

For \(\theta=(A,K_L,\ldots,K_2,u)\), define one forward evaluation by

\[
 Z_1=u,\quad X_1=\phi(Z_1),\qquad
 Z_a=(W_{a,0}+K_a)X_{a-1},\quad X_a=\phi(Z_a),
\]

and \(\mathcal F(\theta)=\langle A,X_L\rangle\).  Along the finite smooth
core generated from the Gaussian seeds by finitely many applications of
the operators, finite-rank tensors, algebraic operations, and
\(\phi,\ldots,\phi^{(12)}\), every field has moments of all finite orders.
The response formulas (2.2)--(2.3) keep every operator action inside that
core.

For a core direction (v), ordinary one-variable differentiation and the
bounded derivative envelope give, by dominated convergence,

\[
 D\mathcal F(\theta)[v]=\langle \mathbf g(\theta),v\rangle_{\mathcal P_L},
 \tag{4.1}
\]

where

\[
 \mathbf g=(X_L,D_L\otimes X_{L-1},\ldots,
 D_2\otimes X_1,D_1).
 \tag{4.2}
\]

The proof is the literal reverse chain rule using the genuine adjoint in
(1.2).  Repeating the dominated-difference-quotient argument through
order three is legitimate because every differentiated activation is a
finite sum of products of bounded \(\phi^{(r)}\) and core fields having all
moments.  It constructs a common (C^3) scalar map for every finite list
of generated directions, and hence mixed derivatives commute.  This is a
local statement on the reachable core; no false claim that the Nemytskii
map is globally (C^3) on an open (L^2) ball is used.

The population ascent recursion is therefore the genuine Euler recursion

\[
 \theta_{s+1}=\theta_s+h\mathbf g(\theta_s),
 \tag{4.3}
\]

because its three parameter blocks are exactly the readout, rank-one
matrix, and bottom-vector updates.  By Section 3, its scalar output is the
already width-identified inverse-free DAG.  Differentiating (4.3) through
order three is consequently a width-first calculation.  No finite-width
Taylor expansion and no exchange of the width and learning-rate limits is
involved.

## 5. Audit map

The construction closes the four blockers in `AUDIT_CUBIC.md` as follows.

1. There is no self-referential source-jet list: all source actions are
   restrictions of the fixed isometries in (1.1).
2. Moving nonlinear queries are in the domain of the fixed bounded
   operators, so only equality of jets is not being inferred from a list
   of origin jets.
3. Enlargement compatibility is literal restriction of the same
   operators (I_a,J_a); (2.2)--(2.3) identify every response sum.
4. Mixed (C^3) regularity is proved on the finite generated core by a
   common fixed-space dominated-difference-quotient argument.  Singular
   covariance matrices never need to be square-root differentiated.
