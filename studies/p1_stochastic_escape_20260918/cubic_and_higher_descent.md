# Cubic descent is not universal: a classification at collapsed states

2026-09-19. Continuation of this study's noise-escape investigation: determine
whether the bad equilibria have a cubic loss-decreasing direction. This is a
landscape statement, not a proof of canonical reachability or noisy fitting.
Lead derivation, before comparison with the independent cubic-order route.
Scientific inputs: complete `docs/observable_p1.md`, `docs/NOTATION.md`, and
this study's complete `sgd_geometry.md` and `four_input_noise_geometry.md`.
No other study is an input. No simulation or external theorem is used.

## 1. Exact model and meaning of a direction

Use the canonical p=1 correlated Gaussian carriers, ridge-normalized marks,
and physical population-L2/L2/Frobenius metric. Work in the odd invariant
sector: b_1 has 2d coordinates, b_2 has d, and all d-by-2d entries of M
are trainable. Removing the inactive constants is exact here. The canonical
initial state is (w,c,M)=(g,0,D). None of the collapsed states below is
asserted to be reached from that initialization. Frozen marks are unchanged.

For finite inputs x_i in sqrt(d) S^(d-1), weights mu_i>0 summing to one,
and labels y_i, write

\[
 a_i=E_1[b_1\phi(w\cdot x_i/\sqrt d)],\quad
 H_i=\phi(b_2^TMa_i),\quad f_i=E_2[cH_i],\quad
 L=\sum_i\mu_i(f_i-y_i)^2,\qquad \phi=\tanh.
\tag{1}
\]

A cubic descending direction means a fixed admissible variation (h,k,N)
such that along the straight line (w,c,M)+epsilon(h,k,N), the linear and
quadratic loss coefficients vanish and

\[
 L(\epsilon)=L(0)-a\epsilon^3+o(|\epsilon|^3),\qquad a>0.
\tag{2}
\]

A nonzero third derivative in a direction with positive quadratic curvature
does not imply local descent. All constructed directions below have bounded
fields, so ordinary one-variable Taylor expansions are justified. For the
claim that *every* cubic direction vanishes, we also cover arbitrary fixed
L2 fields. We do not assume an unrestricted third Frechet derivative of the
loss everywhere on the population Hilbert space.

The canonical nonconstant feature Grams E_l[b_l b_l^T] are positive definite.
For b_2 this follows from independent nondegenerate centered coordinates.
For b_1, conditional on G_i the reverse feature has positive variance from
its fresh Gaussian Z_i; thus no nonzero combination of h_i and k_i can
vanish almost surely. Coordinate independence and invertible normalization
give the assertion. Both marks are bounded. The law of b_2 gives positive
probability to every nonempty open subset of its supporting open cube.

## 2. Complete quadratic/cubic classification when w=c=0

For every finite matrix M_*, the state

\[
                         S_*=(0,0,M_*)                         \tag{3}
\]

is stationary for every individual sample: a_i=H_i=c=0 makes every block
of its sample gradient vanish. Its loss is sum_i mu_i y_i^2. These are
members of the common-sample-stationary family already identified in this
study; full-batch flow and every minibatch update are motionless exactly there.

Define the label-weighted first input moment

\[
                     m_y=\sum_i\mu_i y_i x_i/\sqrt d.
\tag{4}
\]

For a fixed direction h in L2(Omega_1;R^d), k in L2(Omega_2), and finite N,
put A_h=E_1[b_1h^T] and v_k=E_2[b_2k]. Along
(w,c,M)=(epsilon h,epsilon k,M_*+epsilon N),

\[
\begin{split}
 L(\epsilon)=L(S_*)&-2\epsilon^2 v_k^TM_*A_hm_y\\
                 &-2\epsilon^3 v_k^TNA_hm_y+o(|\epsilon|^3).
\end{split}                                                    \tag{5}
\]

To prove it for L2 directions, phi''(0)=0 and bounded phi'' imply

\[
 E_1[b_1\phi(\epsilon h\cdot x_i/\sqrt d)]
   =\epsilon A_hx_i/\sqrt d+o(\epsilon^2).
\]

Indeed the second-order remainder divided by epsilon^2 is bounded by a
constant times |h|^2 and converges pointwise to zero. Dominated convergence
applies. The resulting upper argument is uniformly O(epsilon) since b_2
is bounded. Expanding its tanh through second order and multiplying by
epsilon k gives

\[
 f_i=\epsilon^2v_k^TM_*A_hx_i/\sqrt d
       +\epsilon^3v_k^TNA_hx_i/\sqrt d+o(|\epsilon|^3).
\]

The f_i^2 terms are O(epsilon^4), proving (5). The same dominated
argument makes the lower moments twice continuously differentiable along
this line. If F_i(epsilon)=E_2[kH_i(epsilon)], then f_i=epsilon F_i,
and f_i'''(0)=3F_i''(0). Thus the vanishing third coefficient also is a
vanishing ordinary third directional derivative at zero, not just a
formal expansion.

Consequences, with all matrix directions N admitted:

* If m_y=0, every quadratic and cubic directional coefficient vanishes,
  for every M_*. In particular there is no cubic descending direction.
* If m_y is nonzero and M_*=0, a cubic descending direction exists.
* If m_y is nonzero and M_* is nonzero, a strictly negative quadratic
  direction exists, so cubic descent is not needed to disprove minimality.

For the last two assertions, A_hm_y can be any vector: choose
h=(b_1^T G_1^{-1}a)m_y/|m_y|^2 with G_1=E_1[b_1b_1^T]. Similarly v_k
can be any vector by taking k=b_2^TG_2^{-1}v. If M_* is nonzero, choose
a with M_*a nonzero and v=M_*a, and set N=0. The quadratic coefficient
is negative. If M_*=0, choose nonzero a,v and N=va^T; the cubic
coefficient is negative. All of these fields are bounded.

The quadratic term in (5) is one half of the physical Hilbert Hessian
evaluated on the direction twice; the Hessian evaluation is
-4 v_k^T M_* A_h m_y. Its polarization is a bounded symmetric bilinear
form. In particular, when m_y=0 it is the
zero operator: differentiating the exact physical gradient at the state,
the linear readout/first-layer terms cancel by m_y=0, and the remaining
terms are O(||(h,k,N)||^2), using bounded marks and Lipschitz phi'.
This does not assert existence of an unrestricted third Frechet derivative.

## 3. A balanced four-input counterexample with the canonical M=D

Take d=3, equal weights 1/4, C,S>0, C^2+S^2=1, and

\[
\begin{array}{c|c}
 x_i/\sqrt3&y_i\\\hline
 (C,S,0)&+1\\
 (C,-S,0)&+1\\
 (C,0,S)&-1\\
 (C,0,-S)&-1.
\end{array}                                                     \tag{6}
\]

These are the same data as this study's noncollapsed cubic example. They
are pairwise distinct, nonparallel and nonantipodal, with balanced classes.
Their m_y is zero. Therefore S_*=(0,0,D) has L=1, zero Hessian, and zero
third derivative in *every* fixed population-state direction, even allowing
changes of every entry of M. This already disproves universal cubic descent.

It is nevertheless not a local minimum. The following construction proves
strict fourth-order descent and keeps the canonical matrix D unchanged
along the chosen direction.

Choose an upper coordinate vector s with D^Ts nonzero, and define

\[
 e=\operatorname{sign}(s^TDb_1),\quad
 A=E_1[b_1e],\quad Z=b_2^TDA.
\tag{7}
\]

Set sign(0)=0; changing it on the null event has no effect. Positive
definiteness of the lower Gram gives
s^TDA=E_1|s^TDb_1|>0, so DA is nonzero. Hence Z is bounded, odd, and
has positive probability in every open subinterval of an interval about
zero. In particular E_2[Z^2]>0. The lower law has a density on an open
set in the (h,k) coordinates after normalization, since each conditional
reverse Gaussian has positive variance; a nonzero linear form has no atom
at zero. Thus e^2=1 almost surely and e is an admissible bounded odd field.

Put

\[
 k=-\frac13\left(Z^3-\frac{E_2Z^4}{E_2Z^2}Z\right),\qquad
 h=e(e_1+e_2).
\tag{8}
\]

Here k is nonzero and E_2[kZ]=0. Nonzero follows since Z^3 cannot be
proportional to Z on an interval. Write P_i=(e_1+e_2) dot x_i/sqrt3.
Since e is a sign, along (epsilon h,epsilon k,D) the upper activations are
exactly phi(Z phi(epsilon P_i)). Their uniform expansion is

\[
 \phi(Z\phi(\epsilon P_i))
 =\epsilon P_i Z-\frac{\epsilon^3P_i^3}{3}(Z+Z^3)
       +O(\epsilon^5).
\]

The field k is precisely the component of -(Z+Z^3)/3 orthogonal to Z.
Consequently

\[
 f_i=\epsilon^4P_i^3\|k\|_2^2+O(\epsilon^6),\qquad
 \sum_i\mu_i y_iP_i^3=\frac32CS^2>0,
\]

and therefore

\[
 L(\epsilon h,\epsilon k,D)
       =1-3CS^2\|k\|_2^2\epsilon^4+O(\epsilon^6).
\tag{9}
\]

This is descent for both signs of sufficiently small nonzero epsilon.
All three trained blocks remain available; holding M fixed in one
admissible direction is not a restriction of the model.

For comparison, the state (0,0,0) on these same data has a fifth-order
descending direction. Keep e,Z from (7), take h=e(e_1+e_2), and use
(w,c,M)=(epsilon h,-epsilon Z,epsilon D). Then

\[
 f_i=-E_2[Z^2]\epsilon^3P_i
       +\tfrac13E_2[Z^2]\epsilon^5P_i^3+O(\epsilon^7),
\]
\[
 L=1-E_2[Z^2]CS^2\epsilon^5+O(\epsilon^6).
\tag{10}
\]

The cubic term still vanishes in every direction by (5). Thus both fourth-
and fifth-order descent arise in the existing collapsed family.

## 4. Positive replacement: every fully collapsed state has finite-order
## descent for compatible nonparallel finite data

Here is a stronger, bounded-scope replacement for the false cubic claim.
Let m>=1, x_i in sqrt(d) S^(d-1) be pairwise neither parallel nor antiparallel,
mu_i>0, and nonzero real labels y_i (in particular mixed binary labels).
Then every state (0,0,M_*) is not a local minimum. It has a bounded straight
descending direction of some even order at most 2m if M_* is nonzero,
and of some odd order at most 4m-1 if M_*=0. These are existence bounds,
not assertions that the first possible descent has that particular order.

Choose r outside the finite union of hyperplanes
r dot x_i=0 and r dot(x_i plus-or-minus x_j)=0. Such r exists: the product
of these nonzero linear polynomials is a nonzero polynomial, and a nonzero
real polynomial cannot vanish on all of R^d, by induction on dimension.
Thus P_i=r dot x_i/sqrt(d) are nonzero with distinct squares.

There is an odd q in {1,3,...,2m-1} for which

\[
                         T_q=\sum_i\mu_i y_iP_i^q\ne0.
\tag{11}
\]

Otherwise the Vandermonde matrix with entries (P_i^2)^j, 0<=j<m,
would annihilate the nonzero vector with entries mu_i y_iP_i. Its
determinant is the nonzero product of pairwise differences of the P_i^2,
a contradiction. One may take the least such q.

If M_* is nonzero, construct e,A,Z as in (7) with D replaced by M_*.
The same Gram and support arguments apply; no special rank of M_* is
assumed. The Taylor coefficient of t^j in phi(Z phi(t)), for odd j,
is a polynomial Q_j(Z) of degree exactly j and nonzero leading coefficient.
To see this, write tanh t=sum_{n>=0}(-1)^n b_n t^(2n+1), where b_0=1 and
(2n+1)b_n=sum_{a+b=n-1}b_a b_b>0. This recurrence follows by equating
coefficients in phi'=1-phi^2 and proves all required coefficients nonzero.
The highest Z power of Q_j comes uniquely from the outer j-th term and
the linear term of the inner tanh. The functions Q_1,Q_3,...,Q_q are
linearly independent in L2 because their degrees differ and Z has interval
support. Let R_q be Q_q minus its L2 projection onto the earlier Q_j.
It is bounded, odd, nonzero, and E_2[R_qQ_q]=||R_q||_2^2.

Take the straight line

\[
 w=\epsilon e r,\qquad
 c=\epsilon\operatorname{sign}(T_q)R_q,\qquad M=M_*.
\]

Uniform analyticity on the bounded arguments and the finite data gives

\[
 f_i=\operatorname{sign}(T_q)\|R_q\|_2^2
              P_i^q\epsilon^{q+1}+O(\epsilon^{q+3}),
\]
\[
 L=L(S_*)-2|T_q|\|R_q\|_2^2\epsilon^{q+1}
                       +O(\epsilon^{q+3}).                     \tag{12}
\]

The squared-output term is O(epsilon^(2q+2)), which is covered by the
displayed remainder for q>=1. Since q+1 is even, this proves the first bound.

If M_*=0, choose N=D and construct e,A,Z from D as in (7). Let R be
Z^q minus its L2 projection onto Z,Z^3,...,Z^(q-2). It is nonzero.
Let a_q be the nonzero coefficient of t^q in tanh t, and set
k=sign(a_q T_q)R. Along (epsilon e r,epsilon k,epsilon D),
the upper activation is phi(epsilon Z phi(epsilon P_i)). Its contraction
with k annihilates every outer odd power below q, and the first surviving
one gives

\[
 f_i=a_q\operatorname{sign}(a_qT_q)\|R\|_2^2
                 P_i^q\epsilon^{2q+1}+O(\epsilon^{2q+3}),
\]
\[
 L=L(S_*)-2|a_qT_q|\|R\|_2^2\epsilon^{2q+1}
                       +O(\epsilon^{2q+3}).                    \tag{13}
\]

Here squared outputs are O(epsilon^(4q+2)), also covered by the remainder.
This proves descent for positive epsilon and the odd-order bound 2q+1<=4m-1.

The same data are exactly fittable in this p=1 system. With e,A,Z from D,
choose w=e r and M=D. Then H_i=phi(Z phi(P_i)). The slopes phi(P_i)
are nonzero with distinct squares, so comparing the first m odd Taylor
coefficients in any relation among these H_i gives an invertible
Vandermonde system. Their Gram K is positive definite. The bounded odd
readout c=sum_i (K^{-1}y)_i H_i fits every label. Thus these saddle
statements are not caused by an architectural inability to fit the data.

## 5. Relation to earlier examples and stochastic escape

The two specific states explicitly called cubic saddles in this study
retain their complete cubic proofs: the three-input mixed-label origin
in `sgd_geometry.md` section 9 has m_y nonzero, and the noncollapsed
four-input family in `four_input_noise_geometry.md` section 2 has its
bounded Hessian-null cubic direction for every positive parameter a.
The latter example is not (0,0,D). One dataset can have different bad
equilibria with different orders of descent.

What is disproved is the extension to every bad equilibrium, including
the collapsed family already identified in the SGD analysis. Equations
(9)--(10) supply counterexamples without parallel/antipodal inputs,
without contradictory labels, and with exact zero-loss fits available.
Equation (12)--(13) gives a positive finite-order descent theorem for
the entire fully collapsed family under the stated finite-data hypotheses.
It does not classify every positive-loss equilibrium of p=1.

None of these local statements proves canonical approach, avoidance,
noise excitation, a uniform per-escape loss decrement, or global fitting.
Indeed every individual sample gradient vanishes exactly at (3), so
minibatch noise there is zero despite the descending directions. Added
field noise can have a different support, but its dynamical obligations
remain separate from this landscape calculation.

## 6. Internal review and verified supplements

The fresh isolated review `review_cubic_higher.md` checked the complete
candidate at SHA256
`d469d54a466fb60464f6c3c9e79d831718f333b09e98de20a9d7ff7fc78b9fe1`
against complete canonical p=1 and notation sources. All substantive
claims passed. Its sole required correction was the factor of two
between the quadratic Taylor coefficient and the Hessian evaluation;
the wording in section 2 is corrected above. No sign or descent order
changed. The reviewer also verified the following two supplements.

Equation (5), including the vanishing quadratic and third directional
derivatives when m_y=0, holds in the full unfolded p=1 state with the
constant dictionary features and arbitrary fixed L2 variations. The proof
uses only bounded marks and phi''(0)=0. The explicit descent witnesses
remain odd. This does not extend section 4's theorem to arbitrary
constant-containing matrices outside the odd invariant sector.

In fact at every reduced collapsed state (0,0,M_*), a cubic descending
direction exists if and only if m_y is nonzero. For sufficiency at
nonzero M_*, choose a nonzero vector a in ker M_*, which exists because
M_* has 2d columns and only d rows. Realize A_h m_y=a and v_k=v for
any nonzero v by the Gram constructions in section 2, and put N=va^T.
Equation (5) has zero quadratic coefficient and cubic coefficient
-2|v|^2|a|^2<0. Necessity was already proved by (5). The negative
quadratic direction for nonzero M_* and nonzero m_y remains valid too.

Status: internally reviewed with the stated correction and verified
supplements; not promoted. The lead read the complete review and checked
the final correction and supplement formulas against it.
