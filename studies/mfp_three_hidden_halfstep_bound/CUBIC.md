# Three hidden layers: a conditional compact cubic reduction

## 1. Result and proof boundary

Let the three-hidden-layer network have one input of squared RMS norm one,
equal hidden widths, standard Gaussian raw weights, no biases, and one
shared activation satisfying

\[
 \phi\in C^{8}(\mathbb R),\qquad
 \mathbb E\phi(G)^2=1,qquad G\sim N(0,1),
\]

with at most linear growth for \(\phi\) and bounded derivatives through
order eight.  The excess regularity is convenient here; the cubic formulas
themselves use derivatives only through order three.

This note starts from the fixed-learning-rate Gaussian operator DAG obtained
after taking width to infinity.  It differentiates that DAG only after it
has been defined.  No finite-width Taylor expansion, and hence no
interchange of the width and learning-rate limits, is used.

Let \(F_k(\eta)\) be the limiting expected output after \(k\) recomputed
Euler gradient-ascent steps of size \(\eta\), and put

\[
 \Delta_{21}(\eta)=F_2(\eta)-F_1(2\eta).
\]

The activation-only recursion in Section 5 defines two finite numbers
\(\mathsf S_3\) and \(\mathsf H_3\).  Under the population-intertwining
hypothesis isolated in Section 4, differentiation of the width-first DAG
would give

\[
 F_1'''(0)=\mathsf S_3,
 \qquad
 F_2'''(0)=11\mathsf S_3+12\mathsf H_3.
\tag{1.1}
\]

Moreover, \(F_k\) is odd and

\[
 F_k'(0)=k\Theta_3,
 \qquad
 \Theta_3=1+d+d^2+d^3,
 \qquad d=\mathbb E\phi'(G)^2.
\tag{1.2}
\]

Consequently, under that same hypothesis, the linear and even terms in the
discrepancy vanish and its compact cubic coefficient would be

\[
 \boxed{
 \kappa_{3,21}
 =\frac{F_2'''(0)-8F_1'''(0)}6
 =\frac{\mathsf S_3+4\mathsf H_3}{2}.}
\tag{1.3}
\]

The intended bridge in this note is

\[
 \text{fixed-}\eta\text{ Gaussian DAG}
 \longrightarrow
 \text{its cubic jet}
 \longrightarrow
 (\mathsf S_3,\mathsf H_3).
\]

The finite-width identification and activation-envelope remainder are proved
separately in `WIDTH_DAG.md` and `RANK_REMAINDER.md`.  There is, however, a
different unresolved bridge in the compact calculation below.  A reused
Gaussian matrix is a cylindrical population operator, not a Hilbert--Schmidt
random element.  Equations (4.1)--(4.15) give the required finite-query
adjoint and jet algebra, but they do **not** yet construct one \(C^3\) scalar
population functional on a fixed Hilbert neighbourhood whose gradient
iterates are exactly all seven fixed-step calls.  In particular, they do not
by themselves justify commuting the mixed derivatives used in (4.15).

Therefore (1.1)--(1.3) and the nine-moment reduction are **conditional and
are not used by the quantitative theorem**.  The unconditional coefficient
is instead \(\kappa_\phi^{\mathrm{PJ}}\), defined by the exact Price-jet
recursion (5.12)--(5.24) of `PROOF.md`.  At present this note does not prove

\[
 {\cal J}_3({\cal O}_2)-8{\cal J}_3({\cal O}_1)
 =3\mathsf S_3+12\mathsf H_3.
\tag{1.4}
\]

No quantitative remainder is claimed in this companion note.

## 2. The three-layer fixed-step Gaussian DAG

This section fixes the object that is differentiated.  At time \(s\), write

\[
 X_{\ell s}=\phi(Z_{\ell s}),\qquad
 \Delta_{\ell s}=R_{\ell s}\phi'(Z_{\ell s}),
 \qquad 1\leq\ell\leq3.
\]

The readout is

\[
 A_s=A+\eta\sum_{r<s}X_{3r},qquad R_{3s}=A_s,
 \qquad A\sim N(0,1),
\tag{2.1}
\]

and the output node is

\[
 F_s(\eta)=\mathbb E[A_sX_{3s}].
\tag{2.2}
\]

For \(\ell=2,3\), define the feature and cotangent Grams

\[
 Q^{\ell-1}_{rt}=\mathbb E[X_{\ell-1,r}X_{\ell-1,t}],
 \qquad
 K^{\ell}_{rt}=\mathbb E[\Delta_{\ell r}\Delta_{\ell t}].
\tag{2.3}
\]

Let \((\xi_{\ell r})_r\) and \((\chi_{\ell r})_r\) be centered Gaussian
blocks with covariances \(Q^{\ell-1}\) and \(K^\ell\), respectively.  Fresh
blocks belonging to different raw matrices are independent.  Matrix reuse
is retained by the response coefficients

\[
 \rho^\ell_{sr}
 =\mathbb E[\partial_{\chi_{\ell r}}X_{\ell-1,s}],
 \qquad r<s,
\tag{2.4}
\]

\[
 \sigma^\ell_{sr}
 =\mathbb E[\partial_{\xi_{\ell r}}\Delta_{\ell s}],
 \qquad r\leq s.
\tag{2.5}
\]

The forward and reverse raw-matrix actions are

\[
 Z_{\ell s}
 =\xi_{\ell s}
 +\sum_{r<s}
   \bigl(\rho^\ell_{sr}+\eta Q^{\ell-1}_{rs}\bigr)
   \Delta_{\ell r},
 \qquad \ell=2,3,
\tag{2.6}
\]

\[
 R_{\ell-1,s}
 =\chi_{\ell s}
 +\sum_{r\leq s}\sigma^\ell_{sr}X_{\ell-1,r}
 +\eta\sum_{r<s}K^\ell_{rs}X_{\ell-1,r}.
\tag{2.7}
\]

The first layer has no width-width matrix.  Since the input RMS is one,

\[
 Z_{1,s+1}=Z_{1s}+\eta\Delta_{1s},
 \qquad Z_{10}\sim N(0,1).
\tag{2.8}
\]

For each \(s\), the chronology is: forward through layers \(1,2,3\), form
the output and \(\Delta_{3s}\), then reverse through layers \(3,2,1\).
For \(F_2\), the reverse pass is required at \(s=0,1\), while time two is a
terminal forward pass.  Equations (2.1)--(2.8) therefore form a finite DAG.

The response terms in (2.6)--(2.7) are essential.  In particular,
\(X_{1s}\) depends on the reused column of the second-layer matrix through
\(\chi_{2r}\), and \(X_{2s}\) depends on the reused column of the third-layer
matrix through \(\chi_{3r}\).  These dependencies are precisely (2.4).

## 3. Singular Gaussian covariances and differentiation

At \(\eta=0\), all time copies in a given source block coalesce, so its
covariance is singular.  The following elementary realization removes any
need to differentiate a covariance square root or inverse.

**Lemma 3.1 (isonormal jet).**  Let \(Y(t)\) be a \(C^m\) curve in a real
Hilbert space \(\mathcal H\), and let \(I:\mathcal H\to L^2(\Omega')\) be
isonormal:

\[
 \mathbb E[I(u)I(v)]=\langle u,v\rangle_{\mathcal H}.
\]

Then \(I(Y(t))\) is \(C^m\) in \(L^2(\Omega')\),

\[
 \frac{d^r}{dt^r}I(Y(t))=I(Y^{(r)}(t)),
 \qquad 0\leq r\leq m,
\tag{3.1}
\]

and its derivative vector has Gram matrix

\[
 \mathbb E[I(Y^{(r)})I(Y^{(s)})]
 =\langle Y^{(r)},Y^{(s)}\rangle_{\mathcal H}.
\tag{3.2}
\]

**Proof.**  Linearity and the isometry property give

\[
 \left\|
 \frac{I(Y(t+h))-I(Y(t))}{h}-I(Y'(t))
 \right\|_{L^2}
 =
 \left\|
 \frac{Y(t+h)-Y(t)}h-Y'(t)
 \right\|_{\mathcal H}.
\]

The right side tends to zero.  Repeating this argument proves (3.1), and
(3.2) is the defining isonormal covariance identity. \(\square\)

Apply the lemma with \(\mathcal H=L^2\) of an independent replica of the
already constructed coordinate law.  The replica is important: the
coordinate whose Gram is being represented may itself depend on earlier
sources from the same reused matrix, while the new isonormal map remains
fresh.  The Gaussian source in (2.6) can be realized as

\[
 \xi_{\ell s}=I_\ell(X_{\ell-1,s}),
\tag{3.3}
\]

and the source in (2.7) as an independent isonormal image of
\(\Delta_{\ell s}\).  Their covariances are exactly (2.3).  Thus a singular
time Gram at zero causes no loss of differentiability: its derivative
sources are jointly Gaussian with covariance equal to the Gram of the
corresponding node derivatives.

Bounded activation derivatives and Gaussian moment bounds allow the chain
and product rules in every finite node.  At-most-linear growth controls each
undifferentiated activation.  Induction over the finite chronology therefore
shows that all nodes needed below are \(C^3\) in the relevant \(L^p\)
spaces, and differentiation passes through every displayed expectation by
dominated convergence.

## 4. Candidate operator--Euler intertwining (conditional)

We next record the finite-query algebra that would imply (1.1) once the
missing fixed-Hilbert population realization described in Section 1 is
constructed.  Everything through the finite-query adjoint and the
layerwise jet recursions is exact; the passage to a single \(C^3\) potential
with commuting mixed derivatives remains an explicit hypothesis.

Let \(\Omega_1,\Omega_2,\Omega_3\) carry independent representative
initialization coordinates of the three hidden layers.  With tensor
products understood in the Hilbert-space sense, define the local population
parameter space

\[
\begin{aligned}
 \mathcal P={}&L^2(\Omega_3)
 \oplus L^2(\Omega_3)\otimes L^2(\Omega_2)\\
 &\oplus L^2(\Omega_2)\otimes L^2(\Omega_1)
 \oplus L^2(\Omega_1).
\end{aligned}
\tag{4.1}
\]

The summands are, in order, the readout, third-layer matrix, second-layer
matrix, and first-layer input-weight blocks.  For any finite collection of
directions in \(\mathcal P\), add their Hilbert--Schmidt kernel contractions
to both orientations of (2.6)--(2.7), extend each raw Gaussian source by the
independent-replica isonormal construction of Section 3, and recompute the
response expectations.  This defines a separate finite local perturbation
DAG for each chosen family of directions.  It is \(C^3\) in its finitely
many scalar coefficients by the envelope and domination argument in
Section 3.  What has not been proved is compatibility of all such finite
DAGs as restrictions of one scalar functional on \(\mathcal P\).

Reverse differentiation of its scalar terminal node gives

\[
 \mathbf g=
 \bigl(X_3,\,
 \Delta_3\otimes X_2,\,
 \Delta_2\otimes X_1,\,
 \Delta_1\bigr)\in\mathcal P,
\tag{4.2}
\]

where the input factor of squared norm one is suppressed in the last block.
For every generated finite-query direction \(v\in\mathcal P\), reverse
differentiation gives the candidate adjoint identity

\[
 DF[v]=\langle\mathbf g,v\rangle_{\mathcal P}.
\tag{4.3}
\]

This finite-query identity includes matrix reuse.  At a coalesced single
forward/transpose use of one reused matrix, let \(h,c\) be the old row and
column queries.  For a new row variation \(\dot h\), its raw row action and
the old reverse action have the response forms

\[
 \dot y=I(\dot h)+\rho c,qquad d=J(c)+\sigma h.
\]

Put

\[
 q=\mathbb E[h\dot h],\qquad
 \rho=\mathbb E[\partial_\chi\dot h].
\]

If \(\sigma=\mathbb E[\partial_\xi c]\) and
\(K=\mathbb E[c^2]\), the signed isonormal covariance identities and
Gaussian integration by parts give the exact scalar population adjoint
relation

\[
 \mathbb E[c\dot y]=\sigma q+\rho K
 =\mathbb E[d\dot h].
\tag{4.4}
\]

No inverse is used, so (4.4) also holds at a singular source Gram.  Its
vector-history version follows componentwise, with vectors of old overlaps
and response coefficients replacing the scalars.  Applying it successively
to the third- and second-layer matrices, followed by the ordinary scalar
chain rule, proves (4.3) for every fixed finite-query DAG.  It does not,
without the compatibility theorem stated above, prove that all those
directional identities are derivatives of one map on \(\mathcal P\).

Set

\[
 \mathbf H v=D\mathbf g[v],\qquad
 \mathsf S_3=D^3F[\mathbf g,\mathbf g,\mathbf g],\qquad
 \mathsf H_3=\|\mathbf H\mathbf g\|_{\mathcal P}^2.
\tag{4.5}
\]

Conditional on the compatibility hypothesis below, Section 5 eliminates
both invariants into a finite recursion of one-dimensional activation
integrals.

We now differentiate every reused-matrix node needed at cubic order.
Consider one hidden matrix on the straight population path
\(\theta(t)=\theta_0+t\mathbf g\).  If \(X(t)\) is its lower query,
\(\Delta\) its time-zero reverse source, and \(R\) its time-zero raw
transpose source, then the exact one-step forward operator is

\[
 Z(t)=I(X(t))
 +\mathbb E[\partial_RX(t)]\Delta
 +t\,\mathbb E[X(0)X(t)]\Delta.
\tag{4.6}
\]

Here \(I\) is the signed isonormal source from Section 3.  Write

\[
 X^{[r]}=\partial_t^rX(0),\quad
 F_r=I(X^{[r]}),\quad
 G_{rs}=\mathbb E[X^{[r]}X^{[s]}],\quad
 a_r=\mathbb E[\partial_RX^{[r]}].
\]

Lemma 3.1 and ordinary differentiation of the two deterministic terms in
(4.6) give, without an omitted covariance derivative,

\[
\begin{aligned}
 Z^{[1]}&=F_1+(a_1+G_{00})\Delta,\\
 Z^{[2]}&=F_2+(a_2+2G_{01})\Delta,\\
 Z^{[3]}&=F_3+(a_3+3G_{02})\Delta,
\end{aligned}
\qquad
 \mathbb E[F_rF_s]=G_{rs}.
\tag{4.7}
\]

Thus (4.7) explicitly contains the source jet, the derivative of the
transpose response, and the derivative of the learned term
\(tQ_{01}(t)\Delta\), for each \(r=1,2,3\).

For the differentiated reverse pass, define

\[
 \widetilde R_3=X_3^{[0]},\qquad
 \widetilde\Delta_a
 =\phi''(Z_a)Z_a^{[1]}R_a+\phi'(Z_a)\widetilde R_a
 \quad(a=3,2,1).
\tag{4.8}
\]

For \(a=3,2\), expose the four forward queries
\(X_{a-1}^{[0]},\ldots,X_{a-1}^{[3]}\).  Differentiating the exact transpose
operator (2.7), in that jet basis, gives

\[
 \widetilde R_{a-1}
 =E_{a-1}+\pi_aX_{a-1}^{[0]}
 +\sum_{r=0}^3\varrho_{ar}X_{a-1}^{[r]},
\tag{4.9}
\]

where

\[
\begin{gathered}
 \pi_a=\mathbb E\Delta_a^2,\qquad
 \beta_a=\mathbb E\widetilde\Delta_a^2,\qquad
 \varrho_{ar}
 =\mathbb E[\partial_{F_{ar}}\widetilde\Delta_a],\\
 \mathbb E E_{a-1}^2=\beta_a,\qquad
 \mathbb E[R_{a-1}E_{a-1}]
 =\mathbb E[\Delta_a\widetilde\Delta_a].
\end{gathered}
\tag{4.10}
\]

The first term in (4.9) is the signed isonormal derivative of the raw
transpose source.  The term \(\pi_aX_{a-1}^{[0]}\) is the derivative of the
learned matrix, and the sum is the complete response to all four exposed
forward queries.

We now prove every vanishing in that response sum.  Negate all base reverse
carriers and the odd innovations \(F_{a1},F_{a3}\), leaving the even
innovations fixed.  Bottom-up induction through (4.7) and the scalar chain
rule gives

\[
 X_a^{[r]}\longmapsto(-1)^rX_a^{[r]},\qquad
 G^a_{rs}=0\quad(r+s\ {\rm odd}),\qquad
 a^a_r=0\quad(r\ {\rm even}).
\tag{4.11}
\]

Top-down, \(\widetilde R_3=X_3^{[0]}\) is even and
\(\widetilde\Delta_3\) uses only \(F_{30},F_{31}\).  Suppose the same
statement holds at layer \(a\).  The conclusions below reduce (4.9) to a
function of \(E_{a-1},X_{a-1}^{[0]}\); then (4.8) at layer \(a-1\) uses
only \(F_{a-1,0},F_{a-1,1}\).  This descending induction proves
structurally that

\[
 \varrho_{a2}=\varrho_{a3}=0.
\]

Furthermore,

\[
 \partial_{F_{a1}}\widetilde\Delta_a=\phi''(Z_a)R_a,
\]

whose expectation vanishes because \(R_a\) is centered and independent of
\(Z_a\).  Finally, \(\Delta_a\) is odd under the involution and
\(\widetilde\Delta_a\) is even.  Hence

\[
 \varrho_{a1}=0,\qquad
 \mathbb E[\Delta_a\widetilde\Delta_a]=0.
\tag{4.12}
\]

The jointly Gaussian variables \(E_{a-1}\) and \(R_{a-1}\) are therefore
independent, and (4.9) reduces to

\[
 \widetilde R_{a-1}
 =E_{a-1}+\gamma_aX_{a-1}^{[0]},
 \qquad \gamma_a=\pi_a+\varrho_{a0}.
\tag{4.13}
\]

Equations (4.6)--(4.13) give the explicit layerwise finite-query jet
induction through every forward and transpose action needed at cubic order.
They are necessary evidence for the compatibility statement below, but do
not establish it.

**Intertwining hypothesis.**  The compatible finite-query DAGs above are
restrictions of a single \(C^3\) scalar functional on a neighbourhood of
zero in \(\mathcal P\); (4.3) is its Fr\'echet-gradient identity; and the
one- and two-step temporal operator DAGs equal one and two explicit Euler
iterates of that gradient map.

Assuming this hypothesis, differentiate the population gradient identity
(4.3), holding
\(v\in\mathcal P\) fixed:

\[
 D^2F[w,v]=\langle D\mathbf g[w],v\rangle_{\mathcal P}.
\tag{4.14}
\]

The hypothesized population functional is \(C^3\), so its mixed derivatives
commute.
Taking \(w=\mathbf g\), \(v=\mathbf H\mathbf g\), and then differentiating
(4.3) twice along the frozen direction \(\mathbf g\), gives

\[
\begin{aligned}
 D^2F[\mathbf H\mathbf g,\mathbf g]
 &=\|\mathbf H\mathbf g\|_{\mathcal P}^2=\mathsf H_3,\\
 DF[D^2\mathbf g[\mathbf g,\mathbf g]]
 &=D^3F[\mathbf g,\mathbf g,\mathbf g]=\mathsf S_3.
\end{aligned}
\tag{4.15}
\]

It remains to derive the two-step coefficients.  Apply the explicit Euler
map

\[
 E_\eta(\theta)=\theta+\eta\mathbf g(\theta)
\]

inside the hypothesized population functional.  Direct differentiation
gives

\[
 E_\eta(\theta)'\big|_0=\mathbf g,
\]

for one step, while for two recomputed steps

\[
 \theta_2(\eta)=E_\eta(E_\eta(\theta))
\]

satisfies

\[
 \theta_2'(0)=2\mathbf g,\qquad
 \theta_2''(0)=2\mathbf H\mathbf g,\qquad
 \theta_2'''(0)=3D^2\mathbf g[\mathbf g,\mathbf g].
\tag{4.16}
\]

Applying the third-order chain rule to \(F(\theta_2(\eta))\), and using
gradient symmetry, gives

\[
\begin{aligned}
 F_2'''(0)
 &=D^3F[2\mathbf g,2\mathbf g,2\mathbf g]\\
 &\quad+3D^2F[2\mathbf H\mathbf g,2\mathbf g]
   +DF[3D^2\mathbf g[\mathbf g,\mathbf g]]\\
 &=8\mathsf S_3+12\mathsf H_3+3\mathsf S_3
 =11\mathsf S_3+12\mathsf H_3.
\end{aligned}
\tag{4.17}
\]

For one step the same chain rule immediately gives

\[
 F_1'''(0)=D^3F[\mathbf g,\mathbf g,\mathbf g]=\mathsf S_3.
\tag{4.18}
\]

Conditional on the intertwining hypothesis, (4.15) supplies exactly the
two contractions in (4.17), and all derivatives in (4.16)--(4.18) are
derivatives of the width-first operator construction whose finite-query
matrix nodes were differentiated in (4.6)--(4.13).  No finite-width Taylor
expansion is used, but the conditional status must not be dropped.

## 5. Finite activation-integral recursion (candidate compact form)

Write, at one standard Gaussian \(G\),

\[
 g=\phi(G),\qquad p=\phi'(G),\qquad
 q=\phi''(G),\qquad t=\phi'''(G),
\]

and define the nine one-dimensional activation moments

\[
\begin{array}{lll}
 d=\mathbb E p^2,&u=\mathbb E p^4,&v=\mathbb E[gq],\\
 m=\mathbb E[gp^2q],&r=\mathbb E[pt],&s=\mathbb E q^2,\\
 j=\mathbb E[p^3t],&e=\mathbb E[p^2q^2],&
 \ell=\mathbb E[g^2p^2].
\end{array}
\tag{5.1}
\]

Every expectation in (5.1) is finite under the stated envelope.  Define

\[
 \Theta_0=1,qquad
 \Theta_a=1+d\Theta_{a-1}\quad(1\leq a\leq3),
\tag{5.2}
\]

and

\[
 b_1=d^2,\quad b_2=d,\quad b_3=1,\qquad
 \pi_a=db_a.
\tag{5.3}
\]

Thus \(b_a\) is the variance of the reverse carrier entering layer \(a\),
and \(\pi_a\) is the variance of \(\Delta_a\).

### 5.1 Straight third derivative

Initialize

\[
 V_1=d^2u,qquad M_1=d^2m,qquad J_1=3d^2j.
\tag{5.4}
\]

For \(a=2,3\), recursively set

\[
 V_a=dV_{a-1}+\Theta_{a-1}^2b_a u,
\tag{5.5}
\]

\[
 M_a=vV_{a-1}+\Theta_{a-1}^2b_a m+(d+v)M_{a-1},
\tag{5.6}
\]

\[
\begin{aligned}
 J_a={}&3\Theta_{a-1}V_{a-1}r
 +3\Theta_{a-1}^3b_a j\\
 &+3\Theta_{a-1}M_{a-1}(r+s)
 +d(J_{a-1}+3M_{a-1}).
\end{aligned}
\tag{5.7}
\]

Then

\[
 \boxed{\mathsf S_3=J_3+3M_3.}
\tag{5.8}
\]

### 5.2 Hessian-square contraction

Initialize

\[
 \beta_4=0,qquad \gamma_4=1.
\tag{5.9}
\]

For \(a=3,2,1\), in that order, set

\[
\begin{aligned}
 \beta_a={}&b_aV_{a-1}s
 +3\Theta_{a-1}^2b_a^2e+d\beta_{a+1}\\
 &+\gamma_{a+1}^2\ell
 +2\Theta_{a-1}\gamma_{a+1}b_am,
\end{aligned}
\tag{5.10}
\]

where \(V_0=0\), and

\[
 \gamma_a
 =\pi_a+\Theta_{a-1}b_a(r+s)
   +\gamma_{a+1}(v+d).
\tag{5.11}
\]

Finally,

\[
 \boxed{
 \mathsf H_3
 =V_3+\beta_1+\beta_2+d^2V_1+\beta_3+dV_2.}
\tag{5.12}
\]

Equations (5.1)--(5.12) are a completely specified finite recursion.  It
uses three bottom-up transitions and three top-down transitions and hence
terminates after a fixed number of arithmetic operations and nine
one-dimensional Gaussian integrations.

## 6. Conditional derivation of the recursion

Assuming the intertwining hypothesis, the following calculation verifies
every transition in Section 5 from the finite-query operator jets.

At initialization, let \(R_a\sim N(0,b_a)\) be independent of the base
forward preactivation \(Z_a\sim N(0,1)\), and put

\[
 \Delta_a=\phi'(Z_a)R_a.
\]

The reverse variance recursion is

\[
 b_3=1,qquad b_{a-1}=d b_a,
\]

which proves (5.3).  The first derivative of the forward preactivation at
layer \(a\geq2\) has the form

\[
 Z_a^{[1]}=F_{a1}+\Theta_{a-1}\phi'(Z_a)R_a,
\tag{6.1}
\]

where \(F_{a1}\) is centered Gaussian, independent of \(R_a\), and

\[
 \mathbb E F_{a1}^2=V_{a-1},qquad
 \mathbb E[F_{a1}Z_a]=0.
\tag{6.2}
\]

The coefficient in (6.1) is the sum of the direct learned-weight term and
the response term in (4.7).  Induction gives

\[
 \Theta_a=1+d\Theta_{a-1}.
\]

Since \(X_a^{[1]}=\phi'(Z_a)Z_a^{[1]}\), squaring (6.1) and using the
centered independent carrier proves (5.5).

Let

\[
 V_a=\mathbb E[(X_a^{[1]})^2],qquad
 M_a=\mathbb E[X_a^{[0]}X_a^{[2]}],qquad
 J_a=\mathbb E[\partial_{R_a}X_a^{[3]}].
\tag{6.3}
\]

Parity gives \(Z_a^{[2]}=F_{a2}\), with

\[
 \mathbb E[F_{a2}Z_a]=M_{a-1}.
\tag{6.4}
\]

The scalar chain rule gives

\[
 X_a^{[2]}=\phi''(Z_a)(Z_a^{[1]})^2
             +\phi'(Z_a)F_{a2}.
\]

The first term contracts to

\[
 vV_{a-1}+\Theta_{a-1}^2b_am.
\]

For the second term, one-dimensional Gaussian integration by parts in the
jointly Gaussian pair \((F_{a2},Z_a)\) gives

\[
 \mathbb E[\phi(Z_a)\phi'(Z_a)F_{a2}]
 =M_{a-1}\mathbb E[(\phi\phi')'(Z_a)]
 =(d+v)M_{a-1}.
\]

This proves (5.6).

Next,

\[
 X_a^{[3]}
 =\phi'''(Z_a)(Z_a^{[1]})^3
 +3\phi''(Z_a)Z_a^{[1]}F_{a2}
 +\phi'(Z_a)Z_a^{[3]}.
\tag{6.5}
\]

Equation (4.7) says

\[
 \partial_{R_a}Z_a^{[1]}=\Theta_{a-1}\phi'(Z_a),qquad
 \partial_{R_a}Z_a^{[3]}=(J_{a-1}+3M_{a-1})\phi'(Z_a).
\]

Differentiating (6.5) in \(R_a\), then applying (6.2), (6.4), and Gaussian
integration by parts, yields successively

\[
 3\Theta_{a-1}V_{a-1}r,\quad
 3\Theta_{a-1}^3b_aj,\quad
 3\Theta_{a-1}M_{a-1}(r+s),\quad
 d(J_{a-1}+3M_{a-1}),
\]

which are exactly the four terms in (5.7).  At the first layer,
\(Z_1^{[1]}=\phi'(Z_1)R_1\) and
\(Z_1^{[2]}=Z_1^{[3]}=0\); direct substitution gives (5.4).  At the top,
Gaussian integration by parts in \(R_3\sim N(0,1)\), together with the
readout derivative, gives

\[
 D^3F[\mathbf g^3]=J_3+3M_3,
\]

proving (5.8).

For the reverse recursion, let \(\widetilde R_a\) and
\(\widetilde\Delta_a\) be the derivatives of the reverse carrier and source
along \(\mathbf g\).  From (4.8) and (4.13),

\[
 \widetilde R_a=E_a+\gamma_{a+1}\phi(Z_a),
 \qquad E_a\sim N(0,\beta_{a+1}),
\tag{6.6}
\]

with \(E_a\) independent of the local forward and base reverse variables,
and

\[
 \widetilde\Delta_a
 =\phi''(Z_a)Z_a^{[1]}R_a
 +\phi'(Z_a)\widetilde R_a.
\tag{6.7}
\]

Expanding the square of (6.7) gives five nonzero contractions:

\[
 b_aV_{a-1}s,\quad
 3\Theta_{a-1}^2b_a^2e,\quad
 d\beta_{a+1},\quad
 \gamma_{a+1}^2\ell,\quad
 2\Theta_{a-1}\gamma_{a+1}b_am.
\]

They sum to (5.10).  Differentiating (6.7) syntactically in the base
forward innovation \(Z_a=F_{a0}\) gives

\[
 \varrho_{a0}
 =\Theta_{a-1}b_a(r+s)+\gamma_{a+1}(v+d).
\]

Adding the direct learned-weight coefficient \(\pi_a\) proves (5.11).

Finally, \(\mathbf H\mathbf g\) has four orthogonal parameter blocks.  The
readout block has squared norm \(V_3\); the first-layer block has squared
norm \(\beta_1\); and the two hidden-matrix blocks have squared norms

\[
 \beta_a+\pi_aV_{a-1},\qquad a=2,3.
\]

The potential cross contraction in each hidden-matrix block is zero by
(4.12).  Summing the four blocks and inserting
\(\pi_2=d^2,\pi_3=d\) proves (5.12).

## 7. Parity, linear cancellation, and checks

In the fixed-step DAG, simultaneously apply

\[
 \eta\mapsto-\eta,qquad A\mapsto-A,qquad
 \chi_{\ell r}\mapsto-\chi_{\ell r}\quad(\ell=2,3).
\tag{7.1}
\]

Induction through the chronology leaves every \(Z_{\ell s},X_{\ell s}\)
and both Grams \(Q,K\) unchanged, while it negates every reverse carrier,
\(\Delta\), every \(\rho,\sigma\), and the readout \(A_s\).
The centered Gaussian laws are invariant under (7.1).  Hence

\[
 F_k(-\eta)=-F_k(\eta).
\tag{7.2}
\]

In particular all even derivatives at zero vanish.  The first derivative is
the population gradient norm,

\[
 F_1'(0)=\Theta_3=1+d+d^2+d^3,
\]

and each recomputed step contributes the same first-order increment at the
coalesced node, so \(F_k'(0)=k\Theta_3\).  Therefore

\[
 \Delta_{21}'(0)=2\Theta_3-2\Theta_3=0.
\]

Combining this with (4.17)--(4.18) yields (1.3), conditional on the
intertwining hypothesis.  The exact Price-jet coefficient in `PROOF.md`
does not use this implication.

For the constant normalized activation, \(d=0\) and all nine derivative
moments vanish.  The recursion gives
\(\mathsf S_3=\mathsf H_3=\kappa_{3,21}=0\); directly,
\(F_2(\eta)=2\eta=F_1(2\eta)\).

For the identity activation, \(d=u=\ell=1\) and the other six moments
vanish.  The recursion gives

\[
 \Theta_3=4,qquad \mathsf S_3=0,qquad
 \mathsf H_3=40,qquad \kappa_{3,21}=80.
\]

This check also verifies every depth and step-size multiplicity in
(5.2)--(5.12).
