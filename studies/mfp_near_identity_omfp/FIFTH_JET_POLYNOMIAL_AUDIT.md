# Hostile audit: the exact quartic-in-time fifth jet

Date: 25 August 2026.

## 1. Verdict

The polynomial-time algebra, the inverse Vandermonde matrix, and the
constant \(1524\) in FIFTH_JET_POLYNOMIAL_THEOREM.md are correct. The
result does not require, and must not be read as asserting, a globally
\(C^5\) Nemytskii map on an open \(L^2\) ball.

There is one proof issue in the draft that needs the replacement lemma in
Section 3 below. Repeated differentiation of an aggregate adjoint cannot be
declared finite merely because the step-derivative order is at most five:
source-derivative order and step-derivative order are different gradings.
For a fixed chronology the full marked construction is finite, but that
fact has to be proved by the chronological marked-response induction.
Section 3 supplies that induction through order five. With this
replacement, the theorem passes.

The exact claim boundary is:

1. For every separately fixed \(N,L\) and every fixed \(h\ne0\), the
   actual finite-width expected output converges to the inverse-free
   Gaussian DAG.
2. At \(h=0\), the inverse-free DAG supplies the continuous \(C^5\)
   extension and its singular-Price derivatives.
3. The fifth coefficient of the resulting width-first function has the
   asserted quartic-in-\(t\) law.
4. No estimate of the fifth derivative on a nonzero interval uniformly in
   \(t\) follows.

Item 1 is exactly WIDTH_DEPTH_TIME.md, Theorem 1, including its
pointwise-all-\(h\ne0\) rank proof. Items 2 and 3 are local statements
after that limit. They do not exchange a finite-width Taylor coefficient
with width.

## 2. Frozen objects and notation

Fix \(N,L<\infty\). The identified inverse-free temporal DAG has

\[
 (2N+1)(L-1)
\]

chronological Gaussian actions when \(L\ge2\), and the exact iid coordinate
recursion when \(L=1\). Its nodes and response coefficients are those in
COMPILER_DEPTH_TIME.md, equations (1.3)--(2.5). The fixed-operator
realization is

\[
 W_{a,0}=I_a+J_a^*,\qquad W_{a,0}^*=I_a^*+J_a,
\]

from OPERATOR_BRIDGE_CHECK.md, Sections 1--3. It proves equality with the
temporal DAG for every finite schedule, including schedules containing
zero entries. It is useful for the coefficientwise potential-gradient
identity, but it is not used to assert ambient Frechet smoothness.

For a finite step vector

\[
 \varepsilon=(\varepsilon_0,\ldots,\varepsilon_{N-1}),
\]

write

\[
 \mathfrak A_N
 =\mathbb R[\varepsilon_0,\ldots,\varepsilon_{N-1}]
  /(\varepsilon_0,\ldots,\varepsilon_{N-1})^6.
\]

All assertions below are identities in this finite algebra. The number of
multiindices of total order at most five is

\[
 {N+5\choose5}<\infty.
\]

The exact provenance of the order-five lift is as follows.

1. CUBIC_MARKED_BRIDGE.md, equations (2.1)--(2.16), give every
   coefficientwise node: Leibniz, explicit-step insertion, activation,
   Gram, marked-source covariance, response, learned action, and boundary
   update. These identities have no use of the cutoff \(3\) except the
   displayed finite index range.
2. Its Lemma 3.1, equations (3.1)--(3.7), proves the full
   source-response binomial convolution; Lemma 4.1, equations
   (4.1)--(4.12), proves the causal adjoint and the singular quotient.
3. Its Section 5, especially Lemmas 5.1--5.3, proves formal
   potential-gradient adjointness, substitution naturality, and
   temporal/static intertwining in the truncated algebra. Section 8
   asserts the cutoff-five extension, but does not itself spell out the
   enlarged finite induction.
4. COMPILER_DEPTH_TIME.md, Lemma 3.1 and equations (4.1)--(4.13), proves
   actual \(C^5\) singular-Price regularity with the \(C^{12}\) envelope;
   equations (6.1)--(6.6) give the terminating activation-integral
   evaluation.

Thus no earlier line alone is being treated as a proof of
\(|\alpha|\le5\). Lemma 3.1 below performs the missing cutoff-five
induction using precisely these cutoff-independent node identities.

## 3. Replacement lemma: complete order-five marked intertwining

### Lemma 3.1

For each fixed \(L\), there is one horizon-compatible family of symmetric
generated scalar tensors

\[
 \mathcal T_r,\qquad 0\le r\le5,
\]

and generated gradient tensors

\[
 \mathcal G_r,\qquad 0\le r\le4,
\]

defined on the finite rooted core by a terminating signed Gaussian recursion
before they are identified with derivatives. The family is independent of
the terminal horizon. For every fixed \(N\), if \(\vartheta_0=0\) and, in
\(\mathfrak A_N\),

\[
 \vartheta_{s+1}
 =\vartheta_s+\varepsilon_s
  \sum_{r=0}^4\frac1{r!}
  \mathcal G_r[\vartheta_s,\ldots,\vartheta_s],
 \qquad 0\le s<N,
 \tag{3.1}
\]

then the full total-order-five step jet of the width-first temporal DAG is

\[
 \sum_{r=0}^5\frac1{r!}
 \mathcal T_r[\vartheta_N,\ldots,\vartheta_N]
 \quad\bmod (\varepsilon)^6.
 \tag{3.2}
\]

For \(r=0\), the bracket in (3.1) or (3.2) means the corresponding
zeroth-order field. Every scalar coefficient in (3.1)--(3.2) is a finite
sum of products of one-dimensional Gaussian activation integrals involving
only \(\psi,\ldots,\psi^{(12)}\). No derivative of an unknown output and
no global Frechet derivative is used in its definition.

### Proof

The proof consists of five finite inductions. They are given because the
source-order issue is the only substantive vulnerability in the draft.

#### Step 1: marked algebra and chronological source blocks

For every temporal node \(Y(\varepsilon)\), introduce symbols

\[
 Y^{[\alpha]},\qquad |\alpha|\le5.
\]

Products and explicit step insertions are defined by

\[
 (UV)^{[\alpha]}
 =\sum_{\beta\le\alpha}{\alpha\choose\beta}
 U^{[\beta]}V^{[\alpha-\beta]},
 \tag{3.3}
\]

\[
 (\varepsilon_jUV)^{[\alpha]}
 =\mathbf1_{\{\alpha_j>0\}}\alpha_j
 \sum_{\beta\le\alpha-e_j}
 {\alpha-e_j\choose\beta}
 U^{[\beta]}V^{[\alpha-e_j-\beta]}.
 \tag{3.4}
\]

For a scalar activation \(\chi\), define

\[
 (\chi(Z))^{[\alpha]}
 =\sum_{\pi\in\Pi(\alpha)}
 \chi^{(|\pi|)}(Z^{[0]})
 \prod_{B\in\pi}Z^{[\nu(B)]}.
 \tag{3.5}
\]

This is a finite multiset-partition sum because \(|\alpha|\le5\).

At each forward or transpose action, append all marked Gaussian
coordinates at once. Their covariance is defined to be the marked Gram of
the already constructed query fields:

\[
 \mathbb E[\xi_{a,s}^{[\alpha]}\xi_{a,r}^{[\beta]}]
 =\mathbb E[X_{a-1,s}^{[\alpha]}X_{a-1,r}^{[\beta]}],
 \tag{3.6}
\]

\[
 \mathbb E[\chi_{a,s}^{[\alpha]}\chi_{a,r}^{[\beta]}]
 =\mathbb E[D_{a,s}^{[\alpha]}D_{a,r}^{[\beta]}].
 \tag{3.7}
\]

The query on the right has already been constructed: forward actions are
ordered upward and transpose actions downward, with the current forward
action preceding the current transpose action. Thus (3.6)--(3.7) are
acyclic. There are finitely many actions and finitely many marks per
action, so this induction terminates.

These are the cutoff-five versions of CUBIC_MARKED_BRIDGE.md, equations
(2.1)--(2.16). Nothing in (3.3)--(3.7) depends on the old cutoff three.

#### Step 2: all response convolutions, including singular Grams

For one source history put

\[
 \widehat\chi_j(\varepsilon)
 =\sum_{|\gamma|\le5}
  \frac{\varepsilon^\gamma}{\gamma!}\chi_j^{[\gamma]}.
\]

Coefficient extraction gives, for every \(|\alpha|\le5\),

\[
 \partial_{\chi_j^{[\beta]}}Y^{[\alpha]}
 =\mathbf1_{\{\beta\le\alpha\}}
 {\alpha\choose\beta}
 [D^{\alpha-\beta}\partial_{\chi_j}Y]_{\varepsilon=0}.
 \tag{3.8}
\]

Therefore differentiating a response times a carrier produces the complete
binomial convolution

\[
 \sum_{\beta\le\alpha}{\alpha\choose\beta}
 \rho_{sr}^{[\alpha-\beta]}D_r^{[\beta]},
 \tag{3.9}
\]

and analogously for every \(\sigma X\) term. Equation (3.8) proves that no
mixed term such as \(2\rho'D'\), or any higher analogue, is omitted.

At a nonsingular Gram, repeated Price differentiation identifies these
formal response coefficients with the derivatives of the Gaussian call.
At a singular Gram, fix a scalar direction \(v\) in schedule space and
restrict to the curve \(\varepsilon=sv\). Lemma 3.1 of
COMPILER_DEPTH_TIME.md applies to that covariance curve, including its
rank changes. Its hypotheses hold by the exact envelope recursion in that
file, equations (4.1)--(4.13). Polarization over finitely many directions
recovers every mixed coefficient of total order at most five. Hence the
same identification holds at singular Grams.

The derivative budget is not assumed. It is the counted budget in
COMPILER_DEPTH_TIME.md immediately after equation (4.12): a response uses
one ambient derivative, while the reachable Price terms use at most ten
further formal or spatial derivatives, so no activation derivative above
\(\psi^{(12)}\) occurs. Equations (6.1)--(6.6) of that file then reduce
the signed values at the coalesced covariance to terminating Gaussian
activation integrals.

This proves the cutoff-five version of CUBIC_MARKED_BRIDGE.md, Lemma 3.1.
It is also the finite proof needed behind that file's Section 8 statement
that the marked construction extends to \(|\alpha|\le5\).

#### Step 3: intrinsic causal adjoints

For a marked lower query \(x_p\) and upper cotangent \(c_q\), chronology
splits the possible pair into \(q\prec p\) or \(p\preceq q\). Degenerate
Gaussian integration by parts gives

\[
 \mathbb E[c_qW_ax_p]
 =\sum_{p'\preceq q}Q_{pp'}S_{qp'}
  +\sum_{q'\prec p}R_{pq'}K_{qq'},
\]

\[
 \mathbb E[x_pW_a^*c_q]
 =\sum_{q'\prec p}K_{qq'}R_{pq'}
  +\sum_{p'\preceq q}S_{qp'}Q_{pp'}.
\]

The two expressions are equal term by term. If a Gram is singular, a null
coefficient vector represents the zero \(L^2\) carrier, so the aggregate
response vector is independent of its ambient coordinates. This is
CUBIC_MARKED_BRIDGE.md, Lemma 4.1 and equations (4.9)--(4.12). The proof
is coefficientwise and has no dependence on truncation degree; it applies
to every mark constructed in Steps 1--2.

#### Step 4: potential, gradient, and substitution naturality

On

\[
 \mathbb R[z_1,\ldots,z_m]/(z_1,\ldots,z_m)^6
\]

run one formal forward-reverse pass, adjoining marked sources as in Steps
1--3. Extract square-free coefficients to define \(\mathcal T_r\),
\(0\le r\le5\), and \(\mathcal G_r\), \(0\le r\le4\). Add a
square-zero variable \(\tau\) for one more parameter direction \(v\), and
retain the coefficient of \(\tau\) through \(z\)-degree four. The causal
adjoint identity from Step 3 telescopes through the layers and gives

\[
 \mathcal T_{r+1}[v,u_1,\ldots,u_r]
 =\langle\mathcal G_r[u_1,\ldots,u_r],v\rangle,
 \qquad 0\le r\le4.
 \tag{3.10}
\]

Here is the promised finite construction of the rooted directions; it is
also what makes the tensors independent of the horizon. Set

\[
 \mathscr R_1=\{\mathcal G_0\},
\]

and, for \(2\le r\le5\), set

\[
 \mathscr R_r=
 \left\{
 \mathcal G_k[v_1,\ldots,v_k]:
 \begin{array}{l}
  1\le k\le r-1,\quad v_i\in\mathscr R_{j_i},\\
  j_i\ge1,\quad j_1+\cdots+j_k=r-1
 \end{array}
 \right\}.
 \tag{3.11}
\]

This is a genuine induction: when \(\mathscr R_r\) is constructed, every
input direction on the right of (3.11) belongs to an already constructed
\(\mathscr R_j\), \(j<r\). For each listed tuple, run the finite formal
forward-reverse pass above and extract its square-free coefficient. There
are only finitely many compositions of each integer \(r-1\le4\), and the
previous sets are finite, so every \(\mathscr R_r\) is finite and the
recursion stops at \(r=5\). Extend the extracted maps multilinearly on the
finite spans. The scalar values

\[
 \mathcal T_k[v_1,\ldots,v_k],
 \qquad v_i\in\mathscr R_{j_i},\qquad
 j_1+\cdots+j_k\le5,
 \tag{3.12}
\]

are obtained by the same finite passes and require no new directions.

The isometries \(I_a,J_a\) in OPERATOR_BRIDGE_CHECK.md, Section 1, are
chosen once, before any horizon is specified. Extending a chronology from
\(N\) to \(N+1\) merely appends actions and restricts the same operators on
all old queries. Consequently (3.11)--(3.12) give literally the same
rooted coefficient on every common prefix. This proves horizon
compatibility. It is essential: tensors constructed separately with an
unproved dependence on \(N\) would not imply a polynomial in \(N\).

Every operation used here commutes with an augmented algebra homomorphism:
sums and products algebraically; activation by the finite Taylor formula
(3.5); expectations and Grams coefficientwise; Gaussian source adjoining
by the induced isometry of the Gram quotient; and responses by (3.8).
Thus the substitution-naturality proof in CUBIC_MARKED_BRIDGE.md, Lemma
5.2, applies with the ideal \((z)^6\). This is a finite chronological
induction, not an assertion about a neighborhood in an infinite-dimensional
function space.

#### Step 5: comparison with the temporal chronology

At time \(s\), substitute the already constructed formal displacement
\(\vartheta_s\) into the one-pass formal compiler. Compare it with the
temporal marked DAG lexicographically by

\[
 (s,\text{action within the forward-reverse sweep},|\alpha|,\alpha).
\]

The induction invariants are:

1. equality of the parameter marks accumulated before the action;
2. equality of every feature and cotangent mark already built;
3. equality of every current-to-old marked Gram row;
4. equality of every marked \(\rho\)- and \(\sigma\)-response convolution;
5. a Gram-preserving identification of all source blocks built so far.

At a forward action, (3.6), substitution naturality, and (3.9) extend all
five invariants; the learned rank-one term agrees by (3.4). At a transpose
action the same argument uses (3.7), the \(\sigma X\) convolution, and the
adjoint rank-one contraction. The state update then gives (3.1). At the
terminal forward sweep it gives (3.2). Singular source blocks cause no
exception because Step 3 identifies their quotient aggregates.

The induction range is the product of two finite sets:
\((2N+1)(L-1)\) actions and \({N+5\choose5}\) marks. Hence it terminates.
This is the cutoff-five proof of CUBIC_MARKED_BRIDGE.md, Lemma 5.3; it
does not replace an induction by the phrase “the same argument.”

Finally, the singular-Price theorem in COMPILER_DEPTH_TIME.md, equations
(3.1)--(4.13), proves that the width-first inverse-free DAG is genuinely
\(C^5\) in the scalar schedule directions at the coalesced covariance.
Therefore the formal coefficients just identified are its actual
derivatives. This proves the lemma. \(\square\)

## 4. Euler recursion and polynomial degree

With the generated tensors from Lemma 3.1, write the equal-step state as

\[
 \vartheta_N(h)=\sum_{r=1}^5h^rY_r(N)\pmod {h^6}.
\]

Coefficient extraction from (3.1) gives

\[
 Y_r(0)=0,
\]

\[
 Y_r(N+1)-Y_r(N)
 =\sum_{k=0}^{r-1}\frac1{k!}
 \sum_{\substack{j_1+\cdots+j_k=r-1\\j_i\ge1}}
 \mathcal G_k[Y_{j_1}(N),\ldots,Y_{j_k}(N)],
 \tag{4.1}
\]

where the \(k=0\) inner sum is one only for \(r=1\). This is equivalent
to equations (3.2)--(3.3) of the theorem draft. In particular,

\[
 Y_1(N)=N\mathcal G_0.
\]

If \(Y_j(N)\) has degree at most \(j\) for every \(j<r\), each summand on
the right of (4.1) has degree at most
\(j_1+\cdots+j_k=r-1\). Finite summation in \(N\) raises degree by at
most one. Hence

\[
 \deg_NY_r\le r.
\]

The fifth scalar coefficient is

\[
 A_5(N)
 =\sum_{k=1}^5\frac1{k!}
 \sum_{\substack{j_1+\cdots+j_k=5\\j_i\ge1}}
 \mathcal T_k[Y_{j_1}(N),\ldots,Y_{j_k}(N)],
 \tag{4.2}
\]

so \(\deg_NA_5\le5\) and \(A_5(0)=0\). This validates the theorem's
Euler recursion and polynomial-degree assertion without invoking an ambient
Frechet derivative.

## 5. Vandermonde and normalization audit

Let

\[
 V_{md}=m^d,\qquad1\le m,d\le5.
\]

Exact rational multiplication of the displayed matrix in the theorem by
\(V\) gives the \(5\times5\) identity. Thus, with

\[
 q_m=\frac{\mathcal J^{\rm PJ}_{5,m,L}}{5!},
\]

the formula

\[
 \gamma_d=\sum_{m=1}^5(V^{-1})_{dm}q_m
\]

has the correct \(5!\) normalization and reconstructs \(A_5(N)\), not its
fifth derivative.

The exact row \(\ell^1\)-norms are

\[
 \frac{887}{60},\quad
 \frac{595}{24},\quad
 \frac{335}{24},\quad
 \frac{77}{24},\quad
 \frac{31}{120}.
\]

Only the first four rows survive step doubling, and exact arithmetic gives

\[
 \sum_{d=1}^4|2^d-32|
 \sum_{m=1}^5|(V^{-1})_{dm}|=1524.
 \tag{5.1}
\]

Consequently

\[
 K_{\psi,L}
 \le\frac{1524}{120}B_\psi^{E_{L,5}}
 =\frac{127}{10}B_\psi^{E_{L,5}},
\]

and

\[
 |\Delta_{t,L}^{(5)}(0)|
 \le1524B_\psi^{E_{L,5}}t^4.
\]

Both constants in the draft are correct.

As an independent normalization check, for \(L=2\) and
\(\psi(x)=x\),

\[
 A_5(N)
 =20{N\choose2}+465{N\choose3}
  +1702{N\choose4}+1464{N\choose5}.
\]

Its monomial coefficients are

\[
 (\gamma_1,\ldots,\gamma_5)
 =\left(
 \frac{123}{10},-\frac{629}{12},79,-\frac{613}{12},
 \frac{61}{5}
 \right).
\]

Therefore

\[
 [h^5]\Delta_{t,2}(h)
 =\frac{2452}{3}t^4-1896t^3
  +\frac{4403}{3}t^2-369t,
\]

which agrees with the independently audited identity recursion and fixes
the orientation \(F_{2t}(h)-F_t(2h)\).

## 6. Explicit exponent audit

Section 5 of the theorem is exactly the \(N=5\) specialization of
COMPILER_DEPTH_TIME.md, equations (5.1)--(5.14):

\[
 D_5=12,
\]

\[
 16(5+2)=112,\qquad8(5+1)=48,
\]

\[
 64(D_5+1)^{10}=64\,13^{10},\qquad(D_5+1)^2=169,
\]

and

\[
 M_{L,5}=(2\cdot5+1)(L-1)=11(L-1).
\]

The recursion terminates after the displayed 48 and 24 assignments, and

\[
 E_{L,5}=2L\,p^{M_{L,5}}
 +r\frac{p^{M_{L,5}}-1}{p-1}
\]

is the exact solution of the finite exponent recurrence
\(a_{j+1}=r+pa_j\), \(a_0=2L\). No output-derived quantity enters it.

## 7. Sharpness within genuinely nonlinear activations

The phrase “sharp for the identity activation” should be read as “sharp
already at \(L=2\).” If sharpness is intended inside a genuinely nonlinear
class, it also holds, but one extra argument is needed.

Take

\[
 \psi_\alpha(x)
 =\frac{x+\alpha\sin x}
 {\|G+\alpha\sin G\|_2}.
\]

For \(|\alpha|\le1/4\), the activation and all derivatives through order
12 obey one common weighted envelope. By COMPILER_DEPTH_TIME.md, equations
(6.1)--(6.6), each
\(\mathcal J^{\rm PJ}_{5,m,2}(\psi_\alpha)\) is a finite sum of products
of elementary Gaussian activation moments. Dominated convergence therefore
makes it continuous in \(\alpha\). Hence
\(\gamma_{4,\psi_\alpha,2}\) is continuous, while

\[
 \gamma_{4,\psi_0,2}=-\frac{613}{12}\ne0.
\]

For every sufficiently small nonzero \(\alpha\),
\(\psi_\alpha''\not\equiv0\), and the quartic coefficient

\[
 (2^4-32)\gamma_{4,\psi_\alpha,2}
 =-16\gamma_{4,\psi_\alpha,2}
\]

remains nonzero. Thus degree four is sharp even among smooth,
RMS-normalized, genuinely nonlinear activations. This continuity argument
is used only to exhibit a sharpness witness; it is not used to define a
remainder radius or any theorem constant.

## 8. Required textual corrections

Before treating the theorem file as final, make these literal corrections:

1. Replace the aggregate-adjoint termination paragraph in Lemma 2.1 by a
   citation to Lemma 3.1 above, or incorporate its marked induction.
2. Replace ambient-looking \(D^k\mathbf g\) and \(D^k\mathcal F\) in the
   Euler recursion by the generated tensors \(\mathcal G_k,\mathcal T_k\),
   or explicitly state that the notation means only those finite scalar
   mixed derivatives.
3. Qualify sharpness as occurring already at \(L=2\), and use Section 7 if
   sharpness among genuine nonlinear activations is claimed.
4. State explicitly that actual-network identification is pointwise for
   every fixed \(h\ne0\), while the value and \(C^5\) germ at \(h=0\) come
   from the continuous inverse-free DAG.
5. Repair the rendering typos max, eta, le, and Delta by using
   \(\max,\eta,\le,\Delta\) in math mode.

With these corrections, the exact fifth-coefficient theorem is proved at
every separately fixed finite depth, including \(L=2\) and \(L=3\). The
uniform nonzero-\(h\) remainder remains open, exactly as stated in the
theorem's final section.

**Post-audit status.**  The primary theorem has incorporated items 1--5,
including the complete marked convolution and generated tensors.  It also
incorporates the sharper, independently derived Newton-basis envelope
\((227/180)B_\psi^{E_{L,5}}t^4\).  The later adversarial audit
`REVISED_FIFTH_JET_REDTEAM.md` gives the final PASS on that revised form.
