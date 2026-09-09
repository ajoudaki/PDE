# Candidate temporal cubic law — open after hostile audit

This note records a candidate proof of the cubic coefficient identity
inside the already width-limited inverse-free Gaussian DAG.  A hostile
audit found that Sections 2--5 do **not** yet prove compatibility of the
enlarged marked queries with every differentiated reused-matrix response.
Consequently every boxed factorization in this file is conditional, this
file is not used by `THEOREM.md`, and
\(\kappa_{42,\phi,L}=6\kappa_{21,\phi,L}\) remains open in this study.
The candidate does not differentiate a finite-width network or interchange
the width and learning-rate limits; its failure is the narrower response-
functor bridge described in Section 7.

## 1. Conditional statement

Give the successive Euler steps independent scalar sizes
\(\varepsilon_0,\ldots,\varepsilon_{k-1}\), and let
\(\mathcal F_k(\varepsilon)\) be the terminal output of the population DAG.
The singular Price compiler proves that this finite DAG is \(C^3\) at the
coalesced origin.  There are two activation-defined scalars

\[
 S_L=D^3\mathcal F[g,g,g],\qquad
 H_L=\|Dg[g]\|_{\mathcal P}^2,                         \tag{1.1}
\]

defined by the finite marked-DAG construction below, such that

\[
 \boxed{
 F_{k,L}^{(3)}(0)
 =\frac{k(4k^2-3k+1)}2S_L
 +2k(k-1)(2k-1)H_L.}                                  \tag{1.2}
\]

Conditionally on the missing compatibility lemma, this would imply

\[
 \boxed{
 \kappa_{42,\phi,L}=3S_L+12H_L
 =6\left(\frac12S_L+2H_L\right)
 =6\kappa_{21,\phi,L}.}                               \tag{1.3}
\]

Sections 2--5 give the candidate route to (1.2).  Section 6 gives the
candidate identification of \(S_L,H_L\) with the terminating
one-dimensional Gaussian recursions in `CUBIC_COEFFICIENT.md`.

## 2. Finite marked-source polarization

At one chronological Gaussian call, let \(x_{r,\alpha}\) denote the
already constructed jet of a lower query \(x_r\), where
\(|\alpha|\le3\) is a multiindex in the step variables.  Introduce the
finite centered Gaussian array \(\Xi_{r,\alpha}\) with Gram matrix

\[
 \mathbb E[\Xi_{r,\alpha}\Xi_{s,\beta}]
 =\mathbb E[x_{r,\alpha}x_{s,\beta}].                  \tag{2.1}
\]

This array exists because the right side is the Gram matrix of the finite
family \((x_{r,\alpha})\) in \(L^2\).  For formal degree-three series

\[
 x_r(t)=\sum_{|\alpha|\le3}\frac{t^\alpha}{\alpha!}
 x_{r,\alpha},\qquad
 \xi_r(t)=\sum_{|\alpha|\le3}\frac{t^\alpha}{\alpha!}
 \Xi_{r,\alpha},                                      \tag{2.2}
\]

we have, for \(|\gamma|\le3\),

\[
 \begin{aligned}
 \left.\partial_t^\gamma
 \mathbb E[\xi_r(t)\xi_s(t)]\right|_{t=0}
 &={}
 \sum_{\alpha+\beta=\gamma}{\gamma\choose\alpha}
 \mathbb E[x_{r,\alpha}x_{s,\beta}]\\
 &=\left.\partial_t^\gamma
 \mathbb E[x_r(t)x_s(t)]\right|_{t=0}.
 \end{aligned}                                        \tag{2.3}
\]

Apply the same construction to every transpose history.  Repeated Price
differentiation of a Gaussian expectation is uniquely determined by the
covariance jets and the integrand jets.  Therefore (2.3), induction on
\(|\gamma|\), and induction over the chronological calls identify the
marked construction with the signed Price compiler through order three.

A response coefficient is itself a Gaussian expectation whose integrand
has one additional spatial derivative.  The same induction applied to
that integrand includes every derivative of \(\rho\), \(\sigma\), every
Gram contraction, and every learned-plus-response coefficient.  Thus no
response remainder is omitted.

At a singular Gram, first add \(\delta I\) to each Gaussian covariance.
The preceding argument then concerns nonsingular Gaussian densities.
The polynomial envelopes from `COMPILER_AND_CONSTANTS.md` dominate all
terms through order three, so its compact/tail argument permits
\(\delta\downarrow0\).  Hence (2.3) also identifies the jets at the
coalesced covariance.

The construction terminates lexicographically: base forward and reverse
fields; order-one forward and reverse fields; order-two forward and
reverse fields; and the order-three fields needed by the terminal scalar.
At a fixed order, the forward sweep uses only reverse fields from earlier
times and the reverse sweep uses the just completed forward sweep.  There
is no same-call circularity.  The \(\Xi_{r,\alpha}\) are only a finite
polarization of Price contractions, not extra queries in the temporal
network.

## 3. The reused-matrix adjoint identity

Fix one connector.  Let \(x_i\) and \(c_j\) be its actually exposed lower
query and upper cotangent histories.  For a marked lower query \(x^\circ\)
and a marked upper cotangent \(c^\bullet\), define the inverse-free raw
actions

\[
 \mathcal W x^\circ
 =I(x^\circ)+\sum_j
 \mathbb E[\partial_{\chi_j}x^\circ]c_j,              \tag{3.1}
\]

\[
 \mathcal W^*c^\bullet
 =J(c^\bullet)+\sum_i
 \mathbb E[\partial_{\xi_i}c^\bullet]x_i.             \tag{3.2}
\]

Here \(I,J\) are the fresh forward and transpose Gaussian actions.  The
marked lower field is independent of the forward-source block of this
connector, and the marked upper field is independent of its
transpose-source block.  This property holds at the base level and is
preserved by sums, nonlinearities, response expectations, and learned
rank-one contractions: a forward contraction leaves an upper field times
a deterministic lower inner product, while a backward contraction leaves
a lower field times a deterministic upper inner product.

Gaussian integration by parts gives

\[
 \mathbb E[c^\bullet I(x^\circ)]
 =\sum_i\mathbb E[\partial_{\xi_i}c^\bullet]
 \mathbb E[x^\circ x_i],                              \tag{3.3}
\]

\[
 \mathbb E[x^\circ J(c^\bullet)]
 =\sum_j\mathbb E[\partial_{\chi_j}x^\circ]
 \mathbb E[c^\bullet c_j].                            \tag{3.4}
\]

Substitution in (3.1)--(3.2) proves the exact local adjoint identity

\[
 \boxed{
 \mathbb E[c^\bullet\mathcal W x^\circ]
 =\mathbb E[x^\circ\mathcal W^*c^\bullet].}           \tag{3.5}
\]

The same \(\delta I\) regularization and envelope domination prove (3.5)
at singular histories.  Thus every raw reused-matrix term is paired with
its corresponding response term.

## 4. The only variational identities needed

At initialization write

\[
 x_a=\phi(z_a),\qquad c_a=r_a\phi'(z_a).
\]

For any marked parameter direction \(u\) generated by the degree-three
temporal construction,

\[
 z_1^u=u_1,\qquad x_a^u=\phi'(z_a)z_a^u,              \tag{4.1}
\]

\[
 z_a^u=\mathcal W_a x_{a-1}^u+K_a^u x_{a-1},
 \qquad a\ge2.                                        \tag{4.2}
\]

The reverse tangent is

\[
 r_L^u=u_A,\qquad
 c_a^u=r_a^u\phi'(z_a)+r_a\phi''(z_a)z_a^u,           \tag{4.3}
\]

\[
 r_{a-1}^u=\mathcal W_a^*c_a^u+(K_a^u)^*c_a.          \tag{4.4}
\]

Telescope the top variation downward using (3.5).  The boundary terms are
exactly the readout, matrix, and first-layer metric pairings, so

\[
 D\mathcal F[u]=\langle g,u\rangle_{\mathcal P},       \tag{4.5}
\]

where

\[
 g=(x_L,c_L\otimes x_{L-1},\ldots,c_2\otimes x_1,c_1).
                                                               \tag{4.6}
\]

This is asserted only for the finite marked directions constructed above.
It is not a global cylindrical-potential assumption.

For two such directions \(u,v\), direct differentiation of (4.6), then
successive use of (3.5) and (4.1)--(4.4), gives

\[
 \begin{aligned}
 \langle Dg[u],v\rangle_{\mathcal P}
 ={}&\mathbb E[v_Ax_L^u+u_Ax_L^v]\\
 &+\sum_{a=1}^L
 \mathbb E[r_a\phi''(z_a)z_a^uz_a^v]\\
 &+\sum_{a=2}^L\left(
 \mathbb E[c_aK_a^ux_{a-1}^v]
 +\mathbb E[c_aK_a^vx_{a-1}^u]\right).
 \end{aligned}                                        \tag{4.7}
\]

The right side is symmetric in \(u,v\).  Hence, for these directions,

\[
 D^2\mathcal F[u,v]
 =\langle Dg[u],v\rangle_{\mathcal P}
 =\langle Dg[v],u\rangle_{\mathcal P}.                \tag{4.8}
\]

Define the finite marked fields

\[
 A=Dg[g],\qquad B=D^2g[g,g],\qquad C=Dg[A],            \tag{4.9}
\]

and the scalars

\[
 S=D^3\mathcal F[g,g,g],\quad H=\|A\|_{\mathcal P}^2,
\]

\[
 Q=D\mathcal F[B],\quad
 R=D^2\mathcal F[g,A],\quad P=D\mathcal F[C].         \tag{4.10}
\]

Along the one-step marked line \(t\mapsto\theta_0+tg\), (4.5) gives

\[
 \frac d{dt}\mathcal F(\theta_0+tg)
 =\langle g(\theta_0+tg),g\rangle_{\mathcal P}.
\]

Two further signed-Price differentiations give \(Q=S\).  Equations
(4.5) and (4.8) give

\[
 R=H,\qquad P=H.                                       \tag{4.11}
\]

Therefore

\[
 \boxed{Q=S,\qquad R=P=H.}                            \tag{4.12}
\]

## 5. Temporal causal patterns

The learned readout, first-layer, and finite-rank matrix displacements
satisfy exactly

\[
 \theta_{s+1}=\theta_s+\varepsilon_s g_s.             \tag{5.1}
\]

The initialization Gaussian oracles remain fixed.  Induction in time,
and within each time in forward then reverse layer order, using Section 2,
shows that the marked jets of \(g_s\) are obtained by applying the same
nodewise marked map to the jets of \(\theta_s\).  At the coalesced origin,
unmarked zero-size slices are identities in (5.1), and their duplicated
Gaussian histories reduce to the same aggregate source-plus-response
action by (3.5).  A mixed derivative consequently depends only on the
equality and temporal order pattern of its labels.

For labels \(i<j<\ell\), direct differentiation of (5.1) gives

\[
 \theta_i'=g,\qquad \theta_{ij}''=A,\qquad
 \theta_{ii}''=0,                                     \tag{5.2}
\]

\[
 \theta_{iij}^{(3)}=B,\qquad
 \theta_{ijj}^{(3)}=0,\qquad
 \theta_{ij\ell}^{(3)}=B+C.                           \tag{5.3}
\]

The scalar third-order chain rule and (4.12) now give

\[
\begin{array}{c|c}
\text{label pattern}&
\partial_{\varepsilon_i}\partial_{\varepsilon_j}
\partial_{\varepsilon_\ell}\mathcal F_k(0)\\ \hline
i=i=i&S\\
i=i<j&2S+2H\\
i<j=j&S+2H\\
i<j<\ell&2S+4H.
\end{array}                                            \tag{5.4}
\]

Along the diagonal \(\varepsilon_0=\cdots=\varepsilon_{k-1}=h\), there
are \(k\) all-equal ordered triples; for each of the
\({k\choose2}\) pairs there are three permutations of each repeated-label
pattern; and there are \(6{k\choose3}\) permutations for each distinct
triple.  Hence

\[
 \begin{aligned}
 F_{k,L}^{(3)}(0)
 ={}&kS+3{k\choose2}\{(2S+2H)+(S+2H)\}\\
 &+6{k\choose3}(2S+4H),
 \end{aligned}                                        \tag{5.5}
\]

which simplifies to (1.2).  In particular,

\[
 F_{1,L}^{(3)}(0)=S,\qquad
 F_{2,L}^{(3)}(0)=11S+12H,\qquad
 F_{4,L}^{(3)}(0)=106S+168H.                           \tag{5.6}
\]

Substitution in the definition of the step-doubling coefficients proves
(1.3).

## 6. Explicit Gaussian activation integrals

The forward recursion (3.3)--(3.7) and backward recursion
(3.8)--(3.11) of `CUBIC_COEFFICIENT.md` are obtained by applying
(4.1)--(4.4) to \(g,A,B,C\), expanding the scalar chain rule, and pairing
the raw Gaussian actions with their responses by (3.5).  They use only
the nine one-dimensional moments in (3.2) there, terminate after \(L\)
forward and \(L\) backward indices, and yield

\[
 S_L=\mathsf S_L,\qquad H_L=\mathsf H_L.               \tag{6.1}
\]

Conditionally, the fully explicit coefficient would be

\[
 \boxed{
 \kappa_{42,\phi,L}
 =12\mathsf H_L+3\mathsf S_L,}                        \tag{6.2}
\]

with no output-derived or trajectory-derived quantity.  At \(L=3\), the
recursion is run for exactly three forward and three backward indices.
For \(\phi(x)=x\), it gives
\(\mathsf S_3=0\), \(\mathsf H_3=40\), and
the conditional candidate \(\kappa_{42,\phi,3}=480\).

## 7. Exact unresolved bridge

The finite covariance polarization (2.1)--(2.3) does not by itself define
the complete enlarged marked forward/transpose histories or prove that
differentiating each \(\rho\)- and \(\sigma\)-response equals the response
of those enlarged histories with the correct multiplicities.  Accordingly:

1. the sums in (3.1)--(3.4) would have to range over all marked source
   queries, not merely the actually exposed unmarked temporal histories;
2. the adjoint identity would need a proved two-jet version along the
   marked line before (4.5) could be differentiated to infer \(Q=S\);
3. the scalar pairing (3.5) does not by itself justify deleting duplicated
   zero-step histories or the fieldwise temporal intertwining asserted in
   Section 5; and
4. the nodewise equality in (6.1) still depends on that missing
   intertwining.

Thus the algebra and time-label combinatorics after the bridge are
consistent, but the bridge itself is open.  The unconditional coefficient
used in the quantitative theorem remains the exact signed Price output
\((\mathcal J_3(F_{4,L})-8\mathcal J_3(F_{2,L}))/6\).
