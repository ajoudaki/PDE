# Check of the trained two-layer transverse tangent estimate

2026-10-04. Complete scoped reconstruction of
TRAINED_TWO_LAYER_TANGENT_STABILITY.md by the author of its earlier
trained-response dependency, who did not author the candidate checked here.
Both complete input files were read. This is an internal check, not an
isolated promotion review.

| Input | SHA-256 |
| --- | --- |
| TRAINED_TWO_LAYER_TANGENT_STABILITY.md | fe5faf2c08caa391e520a1221805dd7316de9006c06001025f7b41753c6c9151 |
| TRAINED_NORMALIZED_RESPONSE_ROUTE.md | 4784c003ae8e449b945939d38fae4fea188d816f264d4f60c927f10a70bdd923 |

Verdict: the fitting event, exact tangent representation, normalized
Frobenius estimate, all-time tangent-drift estimate, and integrated top-gate
estimate pass. The confidence and label factors are correct. No repair is
required for the stated norm estimates. A negative-label sign correspondence,
already covered by the source's declared change of readout sign, is made
explicit below to preserve the canonical residual-free response definition.

The result concerns the actual trained finite network, but only at its
single training input and for tangent directions perpendicular to that input.
It does not establish arbitrary-query control, higher input derivatives,
arbitrary-depth bounds, or autonomous compression.

## 1. Setup, mobilities, and the inherited fitting event

There is one unit training input \(e_1\in\mathbb R^d\), with \(d\ge2\),
and label \(y\), with \(Y=|y|>0\). For two hidden layers of width \(n\),
\[
z^{(1)}(v)=Av,\quad h^{(1)}(v)=\phi(Av),\quad
z^{(2)}(v)=Wh^{(1)}(v),\quad h^{(2)}(v)=\phi(z^{(2)}(v)),
\quad f(v)=w^\top h^{(2)}(v)/n.
\]
The loss is \(r^2\), where \(r=f(e_1)-y\), and the mobilities of
\((A,W,w)\) are \((n,1,n)\). Let
\[
a=Ae_1,\quad A=[a,G],\quad
\delta=\phi'(z^{(2)}(e_1))\odot w,\quad b=W^\top\delta .
\]
All training-only features below are evaluated at \(e_1\).
Direct differentiation of \(f\), including its factor \(1/n\), gives
\[
\dot w=-2rh^{(2)},\qquad
\dot W=-2r\delta h^{(1)\top}/n,\qquad
\dot a=-2r\phi'(a)\odot b,\qquad \dot G=0.
\tag{T1}
\]
These are the source's equations with exactly the prescribed mobilities.
They imply
\[
\dot r=-2\mathcal K r,\qquad
\mathcal K=\|h^{(2)}\|_{2,n}^2
 +\|h^{(1)}\|_{2,n}^2\|\delta\|_{2,n}^2
 +\|\phi'(a)\odot b\|_{2,n}^2,
\tag{T2}
\]
where \(\|q\|_{2,n}=\|q\|_2/\sqrt n\). In particular the residual has
the sign of \(-y\) at every finite time.

The activation is the source's normalized erf,
\[
\phi(x)=b_0+\sqrt{\pi\sqrt3/2}\operatorname{erf}(x/\sqrt2),
\qquad b_0=\sqrt{1-\pi/(2\sqrt3)}.
\]
Set
\[
B=b_0+\sqrt{\pi\sqrt3/2},\quad S=3^{1/4},\quad
T=Se^{-1/2},\quad K=9,\quad C_2=B^2+K^2S^2,
\]
\[
c=\min\{1,(16SB^2)^{-1/2},(64S^2BC_2)^{-1/2}\}.
\]
Thus \(|\phi|\le B\), \(|\phi'|\le S\), and \(|\phi''|\le T\).
The two Gaussian second moments of \(\phi,\phi'\) are both one, so here
\(m=\gamma=1\) and \(Y\le c\) is the intended small-label regime.

For completeness the fitting bootstrap can be checked without importing
an all-time source theorem. Assume
\[
\|W(0)\|_{\rm op}\le8,\qquad
\|h^{(2)}(0)\|_{2,n}\ge1/\sqrt2.
\tag{T3}
\]
As long as \(\|W\|_{\rm op}\le9\) and
\(\|h^{(2)}\|_{2,n}\ge1/2\), (T2) gives
\[
|r(t)|\le Ye^{-t/2},\qquad
\tau(t):=2\int_0^t|r(s)|\,ds\le4Y.
\tag{T4}
\]
For now take \(y>0\). A prime denotes differentiation in this increasing
activity clock. Then
\[
w'=h^{(2)},\quad W'=\delta h^{(1)\top}/n,\quad
a'=\phi'(a)\odot b.
\tag{T5}
\]
It follows that
\[
\begin{split}
\|w\|_\infty&\le B\tau,&
\|\delta\|_{2,n}&\le SB\tau,&
\|b\|_{2,n}&\le KSB\tau,\\
\|a'\|_{2,n}&\le KS^2B\tau,&
\|W'\|_F&\le SB^2\tau.
\end{split}
\tag{T6}
\]
The Frobenius estimate in (T6) is exact at the level of the rank-one
normalization:
\[
\|\delta h^{(1)\top}/n\|_F
=\|\delta\|_{2,n}\|h^{(1)}\|_{2,n}.
\]
It does not acquire a factor \(\sqrt n\).
Differentiating \(z^{(2)}=W\phi(a)\) gives
\[
(z^{(2)})'=\delta\|h^{(1)}\|_{2,n}^2
               +W[\phi'(a)^2\odot b],
\quad
\|(z^{(2)})'\|_{2,n}\le SBC_2\tau .
\tag{T7}
\]
Integration on \(\tau\le4Y\), using the two restrictions defining \(c\),
yields
\[
\|W-W(0)\|_{\rm op}\le8SB^2Y^2\le1/2,\qquad
\|h^{(2)}-h^{(2)}(0)\|_{2,n}\le8S^2BC_2Y^2\le1/8 .
\]
These estimates are strictly inside the two tubes. Local continuation
and a first-exit argument prove (T4)--(T7) for all times. Their bounded,
integrable activity-clock velocities also give limits of \(a,W,w\).
There is no circular use of a tangent bound in this bootstrap.

Initialization makes \(a(0)\) and the columns of \(G\) independent
standard Gaussian vectors, also independent of \(W(0)\). Event (T3)
depends only on \((a(0),W(0))\). Its probability tends to one: bounded
conditional second-moment estimates give
\(\|h^{(2)}(0)\|_{2,n}^2\to1\), and the elementary Gaussian net estimate
for the operator cap eight gives exponentially small failure.
Both facts are proved in the frozen dependency. For example, two
\(1/4\)-nets of size at most \(9^n\) and a Gaussian tail give the
operator failure bound \(2e^{-(8-2\log9)n}\).

## 2. Negative labels and the precise response normalization

For general \(y\ne0\), put \(\sigma=\operatorname{sign}(y)\).
The transformation
\[
\widetilde w=\sigma w,\quad
\widetilde y=Y,\quad \widetilde f=\sigma f,\quad
\widetilde r=\sigma r
\]
leaves \(a,W\), their training trajectories, and the positive clock
\(\tau=2\int|r|\) unchanged. Equations (T5)--(T7) hold with the transformed
readout and the corresponding transformed \(\delta,b\). All their bounds
are unchanged.

In the original coordinates
\(\Theta=(A,\sqrt n W,w)\), define the canonical response
\[
R^{(2)}(e_1)
=D_\Theta z^{(2)}(e_1)\,\nabla_\Theta(nf(e_1)).
\]
Equation (T1) implies exactly
\[
\dot z^{(2)}=-2rR^{(2)},\qquad
(z^{(2)})'=\sigma R^{(2)}.
\tag{T8}
\]
Thus \(R^{(2)}=(z^{(2)})'\) when \(y>0\), or in the positive-label
transformed network. For the original negative-label network they differ
by a minus sign. The source explicitly makes this readout transformation;
the mixed-product norms in its conclusions therefore remain valid.
No division by a possibly zero residual is needed to define \(R^{(2)}\):
its displayed state derivative defines it regularly, including at the
limit. The case \(y=0\), excluded from the clock calculation, is stationary.

## 3. Exact conditional linearity of the tangent

Let \(u\in\mathbb R^{d-1}\) have Euclidean norm one, representing a
direction in the input space perpendicular to \(e_1\). Define
\[
D_1=\operatorname{diag}(\phi'(a)),\qquad
D_2=\operatorname{diag}(\phi'(z^{(2)}(e_1))),\qquad
P=D_2WD_1.
\]
The chain rule at the training input gives
\[
J(t,u):=D_vh^{(2)}(t,e_1)[u]=P(t)G u .
\tag{T9}
\]
This is a derivative of the top feature, not of the top preactivation.
The top preactivation tangent is \(WD_1G u\); the distinction matters
for the mixed-product formula below.

By (T1), the complete training trajectory and hence \(P(\tau)\) depend
only on \((a(0),W(0),y)\). Conditional on these objects, \(G\) remains
an \(n\)-by-\((d-1)\) matrix with independent \(N(0,1)\) entries.
The label is fixed, and conditioning on (T3) does not affect this law.
No matrix inside the training computation has been replaced by an
independent copy.

This independence has exactly the asserted scope. At a different query,
the first and later gates generally depend on \(G\); conditional on the
training trajectory, its query tangent is no longer a deterministic
matrix times the independent \(G\).

## 4. The normalized Frobenius derivative

Differentiate the actual matrix curve:
\[
P'=\operatorname{diag}(\phi''(z^{(2)})(z^{(2)})')WD_1
       +D_2W'D_1
       +D_2W\operatorname{diag}(\phi''(a)a').
\tag{T10}
\]
All products inside each diagonal are coordinatewise. For any vector
\(q\in\mathbb R^n\), the row and column squared sums give
\[
\begin{split}
\|\operatorname{diag}(q)W\|_F^2
 &=\sum_iq_i^2\sum_jW_{ij}^2
 \le K^2\|q\|_2^2,\\
\|W\operatorname{diag}(q)\|_F^2
 &=\sum_jq_j^2\sum_iW_{ij}^2
 \le K^2\|q\|_2^2 .
\end{split}
\tag{T11}
\]
Indeed each row norm is \(\|W^\top e_i\|_2\le K\), and each column
norm is \(\|We_j\|_2\le K\). Multiplication by \(D_1,D_2\) costs at
most \(S\) in Frobenius norm. Apply (T6)--(T7) to the three terms:
\[
\begin{split}
\|\operatorname{diag}(\phi''(z^{(2)})(z^{(2)})')WD_1\|_F/\sqrt n
 &\le KTS^2BC_2\tau,\\
\|D_2W'D_1\|_F/\sqrt n
 &\le S^3B^2\tau/\sqrt n,\\
\|D_2W\operatorname{diag}(\phi''(a)a')\|_F/\sqrt n
 &\le K^2TS^3B\tau .
\end{split}
\]
Since \(n\ge1\), their sum is bounded by
\[
\|P'\|_F/\sqrt n\le D_P\tau,\qquad
D_P=KTS^2BC_2+K^2TS^3B+S^3B^2.
\tag{T12}
\]
This reconstructs every factor in the source's equation (7). It requires
only RMS training velocities. No fourth moment or maximum of the trained
backward carrier enters.

## 5. Conditional Gaussian integration and the time supremum

For any deterministic real \(n\)-by-\(n\) matrix \(M\),
the independence and unit variance of the Gaussian columns give
\[
\mathbb E_G\|MG\|_F^2=(d-1)\operatorname{tr}(M^\top M).
\tag{T13}
\]
This identity also applies to \(M=P'(\tau)\) after conditioning on the
entire training initialization: its whole matrix curve and terminal
clock \(\tau_\infty\) are then fixed.

The fundamental theorem of calculus implies
\[
\sup_{0\le\tau\le\tau_\infty}
 \|(P(\tau)-P(0))G\|_F/\sqrt n
\le\int_0^{\tau_\infty}\|P'(\tau)G\|_F/\sqrt n\,d\tau .
\tag{T14}
\]
Minkowski in conditional \(L^2(G)\), followed by (T12)--(T13), bounds
the \(L^2(G)\) norm of the right side by
\[
\sqrt{d-1}\int_0^{\tau_\infty}\|P'(\tau)\|_F/\sqrt n\,d\tau
\le\sqrt{d-1}\,D_P(4Y)^2/2.
\]
All integrations are justified by this finite bound; equivalently,
squaring the integral, using Tonelli, and applying Cauchy--Schwarz gives
the same inequality.

For \(0<\delta<1\), Markov's inequality on the square therefore proves,
with conditional probability at least \(1-\delta\),
\[
\sup_{t\in[0,\infty]}\sup_{\|u\|=1}
\|J(t,u)-J(0,u)\|_{2,n}
\le8D_P\sqrt{\frac{d-1}{\delta}}\,Y^2 .
\tag{T15}
\]
Here the direction supremum is bounded by the Frobenius norm in (T14).
The endpoint is valid because the trained parameters, hence \(P\), have
limits. The probability after removing conditioning is at least
\((1-\delta)\mathbb P(\mathrm{T3})\ge1-\delta-o_n(1)\).
Neither the coefficient nor the bound depends on physical training time
or width.

## 6. The top mixed product and its exact weaker norm

Take the first term of (T10) alone:
\[
M_{\rm top}(\tau)
=\operatorname{diag}(\phi''(z^{(2)})(z^{(2)})')WD_1 .
\]
By (T8), its action on \(Gu\), up to the immaterial sign \(\sigma\), is
the canonical top mixed product
\[
\phi''(z^{(2)})\odot R^{(2)}(e_1)\odot[WD_1G u].
\]
Define its integrated norm by
\[
I=\int_0^{\tau_\infty}\sup_{\|u\|=1}
\|\phi''(z^{(2)})\odot R^{(2)}(e_1)
                            \odot[WD_1Gu]\|_{2,n}\,d\tau .
\]
The first term estimate preceding (T12) and the same Gaussian calculation
give, with conditional probability at least \(1-\delta\),
\[
I\le8KTS^2BC_2\sqrt{\frac{d-1}{\delta}}\,Y^2.
\tag{T16}
\]
The residual-free response has not acquired or lost a factor of two:
the conversion to physical time is precisely
\[
I=2\int_0^\infty |r(t)|\sup_{\|u\|=1}
\|\phi''(z^{(2)})\odot R^{(2)}(e_1)
                            \odot[WD_1Gu]\|_{2,n}\,dt .
\]
Equivalently, this is the integral of the corresponding norm with
\(\dot z^{(2)}\) in place of \(R^{(2)}\), because
\(\dot z^{(2)}=-2rR^{(2)}\).

The statement is an integral in learning activity, not a supremum over
time of the residual-free product. The argument first integrates a
conditional \(L^2\) bound and only then controls the accumulated random
quantity. It has not exchanged expectation with a time supremum or
asserted that \(\sup_t\mathbb E X_t\) controls
\(\mathbb E\sup_t X_t\).

The events proving (T15) and (T16) need not coincide. Replacing
\(\delta\) by \(\delta/2\) in their right sides and taking a union bound
gives both conclusions simultaneously with conditional probability at
least \(1-\delta\), as stated in the candidate.

## 7. Final scope and check record

The checked advance is a finite-network, all-time \(O(Y^2)\) bound on the
change of top-feature tangents at one observed input, together with the
loss-integrated top mixed-product bound there. The lower and upper
nonlinear hidden layers both evolve. The proof neither freezes hidden
weights nor imposes a Gaussian law on the trained gates.

Its limitations are substantive:

- The query point is \(e_1\); the direction ranges over its tangent
  sphere, not over arbitrary query points.
- The result controls first input derivatives and an integrated product.
  It does not give a time-uniform bound on the unweighted top product.
- The dataset has one input, and the network has two hidden layers.
  No recurrence in depth or general-data extension is established.
- No compressed model, state-count estimate, output comparison, or new
  label/error/storage triple is constructed.

The zero-label case is stationary and satisfies the conclusions with
zero right sides, without using a residual clock. Width \(n=1\) causes no
algebraic exception if event (T3) occurs. The assumption \(d\ge2\)
ensures nonempty transverse unit directions. All normalization, sign,
endpoint, probability, and quantifier checks described above passed.
No numerical experiment or external scientific result was needed.
The frozen sources were not modified; only this assigned report was
written.
