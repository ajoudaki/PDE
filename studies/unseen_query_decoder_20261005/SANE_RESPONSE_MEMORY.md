# Causal response memory: an exact realization and the missing return kernel

2026-10-06. Bounded theoretical route in the current unseen-query study.
This note does **not** prove the requested efficient decoder. It proves
operator and compatibility lemmas that distinguish a causally computable positive
response from the nonlinear memory that still needs acquisition. All
complexity counts here are real-coordinate/arithmetic counts; no bit
complexity theorem is inferred from them.

The original network, Gaussian law, zero readout, mean squared loss,
mobilities, full label allowance, training gap, and whole-sphere/all-time
prediction target remain unchanged. No experiment or Git operation was
performed. This is an author result, not an independent review.

## 1. Exact objects and inherited bounds

For the width-n network use mobility coordinates

\[
 \theta=(A/\sqrt n,W^{(2)},\ldots,W^{(L)},w/\sqrt n),\qquad
 e_a=(f_n(v_a)-y_a)/\sqrt m,\qquad v_a=x_a/\sqrt d.
\]

The columns of the parameter Jacobian \(\mathcal J(t)\) are
\(\nabla_\theta e_a\). The self-adjoint residual curvature is
\(\mathcal H(t)=\sum_a e_a\nabla_\theta^2e_a\). The derivative
propagator of the actual nonlinear parameter flow is

\[
 \partial_t U(t,s)=-2[\mathcal J(t)\mathcal J(t)^T+
                         \mathcal H(t)]U(t,s),\qquad U(s,s)=I.
 \tag{1}
\]

The allowed `EFFICIENT_QUERY_DIRECT.md` and its check establish, under
their explicit inherited carrier/residual assumptions,

\[
 M=2\int_0^\infty\|\mathcal H(t)\|_{\rm op}\,dt
       \le C Y(1+Y\sqrt{\log(en)}).
 \tag{2}
\]

The constant in this recalled bound depends on the fixed original
problem. It is not an explicit modest polynomial certificate. Only the
lemmas below have fully displayed numerical constants.

## 2. Positive response has a causal realization without Gram inversion

The following statement applies to a supplied finite representation of
the Jacobian. Let the columns of a fixed matrix \(B\) be vectors in
parameter space, let \(G=B^TB\), and suppose

\[
 \mathcal J(t)=B C(t),\qquad C(t)\in\mathbb R^{r\times m}.
 \tag{3}
\]

No linear independence of the r columns is required. Define the r by r
matrix \(Z(t)\) by the causal ODE

\[
 \dot Z=-2 C(t)[C(t)^T+(C(t)^T G)Z],\qquad Z(0)=0.
 \tag{4}
\]

Then the propagator of the positive Gauss--Newton part is exactly

\[
 S(t,0)=I+B Z(t)B^T.
 \tag{5}
\]

Indeed, differentiating the right side of (5) with (4) gives
\(-2 B C C^T B^T[I+B Z B^T]\), its required vector field, and
the initial value is I. Uniqueness of the finite linear ODE proves (5).
For arbitrary boundary vectors a,b its contraction is

\[
 a^T S(t,0)b=a^Tb+(B^Ta)^T Z(t)(B^Tb).
 \tag{6}
\]

The actual operator is contractive, since each solution satisfies
\(\frac d{dt}\|S(t,0)b\|_2^2=-4\|\mathcal J(t)^TS(t,0)b\|_2^2\le0\).
This operator bound does not assert that every overcomplete coordinate
matrix Z is well conditioned.

There is also an exact causal rule for appending new directions. When
new columns are appended to B, pad the old Z with zero rows and columns
and append the new Gram entries to G. Formula (5) then describes exactly
the same current operator before the next evolution interval. This is
why no response to a newly appended vector has to be replayed from time
zero. The construction stores the finite-rank correction to the identity,
rather than only storing images of directions already encountered.

The retained matrices G,Z cost \(2r^2\) coordinates, and C costs rm.
Compute \(C^TG\), then \((C^TG)Z\), then the final product with C.
One right-hand-side evaluation costs \(O(mr^2)\) arithmetic and
\(O(r^2+rm)\) peak coordinates; a boundary contraction costs
\(O(r^2)\) once its r pairings are available. There is no history-Gram
inverse and no stored two-time resolvent table.

If H temporal patches of degree p supply the Jacobian directions, then
\(r\le mH(p+1)\). Under the conditional temporal scales already used
in the allowed response source, \(H=O(\log(en)^{3/2})\) and
\(p=O(\log(en))\), this gives an \(O(m^2\log(en)^5)\)
coordinate realization. This statement is conditional on acquiring B's
Gram, C, and the boundary pairings. It is not an algorithm acquiring the
neural nonlinear contractions, and no time discretization or coefficient
precision bound is proved here.

## 3. Exact elimination of the complement

Fix an orthogonal projection P whose range contains every column of
\(\mathcal J(t)\) over the interval under consideration, and put
\(Q=I-P\). This is a proof device; a fixed future-dependent P is not
asserted to be causally available. Let V(t,s) be the propagator on the
range of Q with generator \(-2Q\mathcal H(t)Q\).

For an initial vector in the range of P, write its propagated P and Q
components as x(t) and z(t). Direct projection of (1) gives

\[
 \dot x=-2[\mathcal J\mathcal J^T+P\mathcal H P]x
                      -2P\mathcal H Qz,
 \qquad
 \dot z=-2Q\mathcal H Px-2Q\mathcal H Qz,\quad z(0)=0.
\]

Variation of constants in the second equation yields

\[
 \dot x(t)=-2[\mathcal J(t)\mathcal J(t)^T+
                           P\mathcal H(t)P]x(t)
             +\int_0^t K(t,s)x(s)\,ds,
 \tag{7}
\]

where the exact return kernel is

\[
 K(t,s)=4P\mathcal H(t)Q V(t,s)Q\mathcal H(s)P.
 \tag{8}
\]

Every escape from the retained space has to return through another
off-space curvature factor to influence x. Equation (8) identifies the
missing coefficient; it does not grant V as a computation primitive.

## 4. Two-sided leakage bound

Let \(U_P(t,0)\) be the propagator on the range of P with generator
\(-2[\mathcal J\mathcal J^T+P\mathcal H P]\), and define

\[
 \Lambda(t)=2\int_0^t\|Q\mathcal H(s)P\|_{\rm op}\,ds,
 \qquad M(t)=2\int_0^t\|\mathcal H(s)\|_{\rm op}\,ds.
\]

Then

\[
 \|P U(t,0)P-U_P(t,0)\|_{\rm op}
                  \le e^{M(t)}[\cosh\Lambda(t)-1].
 \tag{9}
\]

To prove this, split the generator into its block-diagonal part and
\(-2[P\mathcal H Q+Q\mathcal H P]\). The latter has norm
\(2\|Q\mathcal H P\|\), because \(\mathcal H\) is self-adjoint
and the square of its off-diagonal block matrix has diagonal blocks
\((Q\mathcal H P)^T(Q\mathcal H P)\) and its reverse product.
The block-diagonal propagator between s and t has norm at most
\(\exp(2\int_s^t\|\mathcal H(u)\|du)\): differentiation of
the squared norm uses the nonpositive Gauss--Newton contribution and
the bound on each compressed curvature block.

Iterate variation of constants in the off-diagonal part. A term with k
insertions is bounded by \(e^{M(t)}\Lambda(t)^k/k!\), since the
propagator factors occupy disjoint time intervals and the ordered
simplex integral of the scalar insertion norms equals their kth total
mass divided by k!. Odd k terms have zero P-to-P block. The k=0 term
is \(U_P\). Summing positive even k proves (9); absolute convergence
also justifies the series and its identification with (1).

For \(0\le\Lambda\le1\), the same series gives
\(\cosh\Lambda-1\le(\cosh1-1)\Lambda^2<\Lambda^2\).
Thus a sufficient condition for response error at most epsilon is
\(\Lambda\le\min\{1,e^{-M/2}\sqrt\varepsilon\}\).
For a near-root error \(\varepsilon=n^{-1/2+o(1)}\) and
\(M=O(\sqrt{\log n})\), this certificate calls for
\(\Lambda\le n^{-1/4+o(1)}\). The inherited source gives only
\(\Lambda\le M\); it supplies no such width decay. Fixed small
labels do not turn a fixed power of Y into an error tending to zero.
This invalidates that proposed deduction, not the existence of another
compression of (8).

## 5. A sharp finite-dimensional check, with its scope stated

Take parameter space \(\mathbb R^2\), P projection onto its first
coordinate, a constant Jacobian \(\mathcal J=(\sqrt a,0)^T\)
with \(a>0\), and

\[
 \mathcal H=\begin{pmatrix}0&b\\b&0\end{pmatrix},\qquad b\ne0.
\]

The retained coefficients \(\mathcal J^T\mathcal J=a\) and
\(P\mathcal H P=0\) contain no b. But the exact return kernel
in (8) is the constant \(4b^2P\), while the compressed propagator
is \(e^{-2at}P\). Expanding the matrix exponential of
\(-2(\mathcal J\mathcal J^T+\mathcal H)t\) at zero gives

\[
 P U(t,0)P-e^{-2at}P=2b^2t^2P+O(t^3).
\]

Indeed the first-order coefficients coincide, and the first diagonal
entry of \([\mathcal J\mathcal J^T+\mathcal H]^2\) is
\(a^2+b^2\). This verifies the two-insertion order and shows that
G and the retained curvature block alone cannot determine the response
of a general supplied operator system.

This example is **not** claimed to be a Jacobian/curvature pair generated
by the admissible neural gradient flow. That distinction matters. For
one training sample, differentiating the actual Jacobian gives
\(\dot{\mathcal J}=-2\mathcal H\mathcal J\). Thus the example's
constant Jacobian and nonzero off-diagonal curvature fail a real
trajectory compatibility relation. No network impossibility claim
follows. Conversely, that one-sample relation controls
\(\mathcal H(t)\mathcal J(t)\); it does not identify
\(\mathcal H(t)\mathcal J(s)\) for all earlier s or a new query
boundary field.

## 6. Actual trajectory compatibility isolates a nonvanishing neural source

The abstract example can be replaced by a more informative calculation
inside the actual gradient flow. Write \(\mathcal J_a=\nabla e_a\)
for its ath column, and define the parameter vector

\[
 C_b(t)=\sum_{a=1}^m e_a(t)
       [D\mathcal J_a(t)\mathcal J_b(t)
                   -D\mathcal J_b(t)\mathcal J_a(t)].
 \tag{10}
\]

Here \(D\mathcal J_a=\nabla^2e_a\) is the ordinary derivative
in mobility coordinates. The bracketed difference measures failure of
the two sample-gradient vector fields to commute. Let \(C_*\) denote
the parameter-by-m matrix with columns C_b, avoiding any identification
with the coefficient matrix C in Section 2. Differentiation along
\(\dot\theta=-2\sum_a e_a\mathcal J_a\) gives exactly

\[
 \dot{\mathcal J}=-2\mathcal H\mathcal J+2C_*.
 \tag{11}
\]

Indeed its bth column is
\(-2\sum_a e_aD\mathcal J_b\mathcal J_a\); adding and
subtracting \(-2\sum_a e_aD\mathcal J_a\mathcal J_b\)
proves (11).

Let \(R(t,s)\) solve the m by m ODE
\(\partial_tR=-2(\mathcal J^T\mathcal J)R\), with
\(R(s,s)=I_m\). It is contractive by differentiating squared
Euclidean norms. The product rule and (11), followed by variation of
constants in (1), prove

\[
 U(t,s)\mathcal J(s)=\mathcal J(t)R(t,s)
        -2\int_s^t U(t,u)C_*(u)R(u,s)\,du.
 \tag{12}
\]

In particular, commuting sample gradients have an exact finite
training-response closure, and every one-sample trajectory has this
closure because the single bracket is identically zero. For the general
case the error from deleting the second term is at most

\[
 2\int_s^t
 \exp\!\left(2\int_u^t\|\mathcal H(v)\|_{\rm op}\,dv\right)
                       \|C_*(u)\|_{\rm op}\,du.
 \tag{13}
\]

This uses the norm bound for U obtained from its nonpositive
Gauss--Newton part, and the contractivity of R. The one-sample identity
only transports training-gradient directions. It is not an evaluator of
the arbitrary root-derivative boundary contractions in the response trace.

The bracket source in (10) is not automatically negligible at large
width in the original neural model. For a concrete admissible example,
take L=2, m=d=2, unit inputs v_1,v_2 equal to the coordinate vectors,
\(\phi_1=\tanh\), and \(\phi_2(z)=z\). Thus
\(h_a^{(1)}=\tanh(A v_a)\), \(h_a^{(2)}=W h_a^{(1)}\), and
\(f_a=w^Th_a^{(2)}/n\). The tanh strip may be chosen strictly
inside its first complex poles; the identity activation is allowed and
has unbounded values. At zero readout, \(\mathcal J_a\) has only
the readout block \(h_a^{(2)}/\sqrt{mn}\).

The W block of the bracket in (10), for a=1,b=2, is exactly

\[
 [D\mathcal J_1\mathcal J_2-D\mathcal J_2\mathcal J_1]_W
   =\frac{h_2^{(2)}h_1^{(1)T}-h_1^{(2)}h_2^{(1)T}}{nm}.
 \tag{14}
\]

To verify the scaling, \(\nabla_W e_a=w h_a^{(1)T}/(n\sqrt m)\).
A readout mobility-coordinate variation equal to
\(\mathcal J_b\) changes the physical w by
\(\sqrt n\,h_b^{(2)}/\sqrt{mn}=h_b^{(2)}/\sqrt m\),
which gives (14). There are no other terms in this block at w=0.

Put \(q=\mathbb E\tanh^2(G_0)>0\), where G_0 is a standard
Gaussian scalar. The first-layer normalized feature Gram converges in
probability to \(qI_2\). Its diagonal variances are O(1/n) by
bounded independent coordinates; its off-diagonal mean is zero by oddness
of tanh and independence of the two Gaussian input columns, again with
variance O(1/n). Conditional on these first-layer features, the n rows
of \((h_1^{(2)},h_2^{(2)})\) are independent centered Gaussian
pairs with precisely that empirical covariance. Their empirical second
moments have conditional variances O(1/n), uniformly since every
first-layer normalized norm is at most one. Consequently their Gram
also converges in probability to \(qI_2\).

For vectors a,b,c,d,
\(\|ab^T-cd^T\|_F^2=\|a\|^2\|b\|^2+
\|c\|^2\|d\|^2-2(a^Tc)(b^Td)\). Applying this identity to
(14) yields

\[
 \big\|[D\mathcal J_1\mathcal J_2-
                      D\mathcal J_2\mathcal J_1]_W\big\|_F^2
                   \longrightarrow \frac{2q^2}{m^2}>0
 \quad\hbox{in probability}.
 \tag{15}
\]

The population training-feature Gram is \(qI_2\), so it has the
required positive gap; the training data span the input space. Choose
labels \((\eta,0)\) with any fixed \(\eta>0\) inside the full
original allowance. At initialization, the W block of C_2 in (10) has
norm converging to \(\eta q/m>0\), because
\(e_1=-\eta/\sqrt m\) and m=2. Thus width alone does not suppress
this actual neural source even initially. There is actual feature motion:
the physical gradient equations give
\(\dot w(0)=2\eta h_1^{(2)}/m\) and
\(\ddot W(0)=4\eta^2 h_1^{(2)}h_1^{(1)T}/(m^2n)\ne0\)
almost surely. In particular
\(\ddot W(0)h_1^{(1)}\ne0\). The accompanying first-matrix motion
cannot cancel this second-layer feature change: differentiation gives

\[
 (h_1^{(2)})^T\ddot h_1^{(2)}(0)
 =\frac{4\eta^2}{m^2}
  \left[\frac{\|h_1^{(1)}\|_2^2}{n}\|h_1^{(2)}\|_2^2
   +\|\tanh'(A v_1)\odot W^T h_1^{(2)}\|_2^2\right]>0.
\]

All fields on the right are evaluated at initialization. This follows
from \(\ddot A(0)v_1=(4\eta^2/m^2)
\tanh'(Av_1)\odot W^T h_1^{(2)}\), and \(\dot A(0)=\dot W(0)=0\).
Thus this example retains a nonlinear first activation and actual
hidden-feature motion.

This calculation rules out an initial source bound tending to zero that
uses only width and the original assumptions. It does not by itself give
a lower bound for its integral on a width-independent time interval,
nor does it refute a compact way of retaining the brackets. Iterating
their transport introduces further derivatives/brackets; no bounded
closure of that hierarchy is proved here.

## 7. Evaluating the return kernel is still a specific open problem

For a finite temporal coefficient approximation write
\(Q\mathcal H(t)Q=\sum_{j=1}^D a_j(t)T_j\). The matrices T_j
act on the omitted parameter space. Expanding V(t,s) through order k
requires contractions of words

\[
 P\mathcal H(t)Q\,T_{j_k}\cdots T_{j_1}\,Q\mathcal H(s)P,
             \qquad (j_1,\ldots,j_k)\in\{1,\ldots,D\}^k.
 \tag{16}
\]

The scalar weights are computable by nested one-dimensional integrals:
for a word w obtained by appending j to a prefix u, its prefix integral
satisfies \(\dot I_w(t)=a_j(t)I_u(t)\), with \(I_\varnothing=1\)
and every nonempty I_w initially zero. Hence this is a concrete causal
calculation, not an unnamed expectation oracle. It has up to
\(\sum_{k=0}^K D^k\) coefficients before any algebraic word reduction.
The operator contractions in (16) must also be acquired; their bare
formulas do not supply compact nonlinear neural evaluators.

At the inherited scalar temporal scales, a putative
\(D=O(\log(en)^{5/2})\) coefficient count and the sufficient
Dyson order \(K=O(\log n/\log\log n)\) allow
\(D^K=n^{O(1)}\), not a polylogarithmic count. This is the cost of
this explicit enumeration, not a lower bound for all algorithms or a
claim that every word is independent in the neural system. Moreover,
an operator-norm temporal approximation with this D was not established
by the scalar source theorem and is not assumed as a neural result here.

A reopen condition for this route is therefore concrete: exploit the
actual layer structure and trajectory compatibility to evaluate the
sum in (16), including its query boundary contractions, from at most
the desired logarithmic-memory coefficient state with modest explicit
parameter factors. The existing source bounds, scalar resolvent, and
fixed label smallness do not provide such a reduction. Polynomial-size
formal descriptions of words do not provide polynomial-time evaluation
of their nonlinear contractions.

## 8. Status and provenance

Proved here: the exact causal finite-rank correction (4)--(6), including
direction appending; the exact return kernel (7)--(8); the bound (9);
the finite-dimensional check; the exact compatibility identities
(11)--(13); and the admissible initial bracket calculation (14)--(15).
Their hypotheses are explicitly
separated from the original network assumptions. The consequence that
discarding complement memory is accurate at the required width scale
is unproved. An efficient acquisition/evaluation of complement memory,
a whole-sphere boundary representation, finite-precision error control,
and final prediction transfer remain open.

Scientific inputs read completely for this route were
`EFFICIENT_QUERY_DIRECT.md`, `EFFICIENT_QUERY_DIRECT_CHECK.md`,
`POPULATION_DECODER.md`, `ROOT_RESPONSE_AND_COVARIANCE.md`,
`ROOT_RESPONSE_AND_COVARIANCE_CHECK.md`, and `docs/notation.qmd`.
`COST_CONTRACT.md` was read through its resource and interface sections;
the other authorized source files were not used. Metadata headings of
the explicitly authorized integrated RESULT were inspected, but no
scientific claim here is imported from that inspection. No other study,
archive, new route output, external source, or experiment was used.

The required canonical-notation skill was unreadable with OS
`Permission denied`, including an escalated read; its linked neural
reference was consequently unavailable. The supervisor authorized the
fallback to the explicit user notation requirements and maintained
notation contract. The research and rigorous-proof instructions were
applied. Only this file was written.
