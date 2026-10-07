# Finite-panel cost interfaces and a linear-scratch collocation schedule

2026-10-06. Bounded clarification of the existing cost result, not a new
numerical-training or finite-bit theorem. The input scope was the current
parameter/resource notes, the compiler note, and the authorized finite-panel
`RESULT.md`. The required rigorous-math skill was applied; the canonical
notation skill remained permission-inaccessible, as already reported to the
supervisor. No maintained source or other study was changed.

Use the existing parameters: dense width \(n\), training count \(m\), total
declared panel size \(p\ge m\ge d\ge1\), depth \(L\ge2\), training gap
\(\gamma>0\), label RMS \(Y>0\), and activation envelope \(\beta\ge10\).
Put \(r=m/\gamma\), \(\ell=\log(en)\), and retain the common logarithm

\[
Z=\ell+\log\!\left(e+
\frac{(m+d+2)\beta^{100L}(1+r)}\delta\right),\qquad 0<\delta<1.
\]

The source radius coefficient obeys \(1\le\chi^{-1}\le\beta^{36L}\)
on the full inherited label allowance. Let \(K\) be the retained temporal
source degree, \(Q\) the least power of two at least \(2(K+1)\), and
\(K_{\rm solver}\) the power-of-two node count on a physical solver patch.
These are different quantities. Write \(H\) for the patch count,
\(J=K_{\rm solver}\) for the Picard iteration count, and
\(N_F=HK_{\rm solver}(J+1)\) for its field-evaluation count. All constants
denoted by \(C\) below are universal numerical constants.

## 1. No quadratic integration-weight array is necessary

Set \(k=K_{\rm solver}\). On a patch, retain old nodal derivative vectors
and a separate array for new nodal states; their dimension is
\(O((Ln^2+dn)k)\). For each scalar state coordinate, let \(f_i\) be its
old derivatives at

\[
x_i=\cos\frac{(i+1/2)\pi}{k},\qquad s_i=(1+x_i)/2,
\qquad 0\le i<k.
\]

Execute the following coordinate loop, reusing its scratch for the next
state coordinate.

1. Form the interpolation coefficients
   \[
   a_0=\frac1k\sum_i f_i,\qquad
   a_j=\frac2k\sum_i f_iT_j(x_i),\quad 1\le j<k.
   \]
   For each node, generate its \(T_j(x_i)\) successively using
   \(T_0=1\), \(T_1=x_i\), and
   \(T_{j+1}=2x_iT_j-T_{j-1}\); accumulate the length-\(k\) array.
   This costs \(O(k^2)\) arithmetic operations and \(O(k)\) scratch.
2. Construct the degree-at-most-\(k\) antiderivative
   \(A(s)=\int_0^s\sum_{j<k}a_jT_j(2u-1)\,du\) as a Chebyshev
   coefficient array. The constant and linear terms integrate as
   \(a_0s\) and \(a_1(s^2-s)\). For \(j\ge2\), use
   \[
   \int_0^sT_j(2u-1)\,du=
   \frac14\left[
   \frac{T_{j+1}(2s-1)-(-1)^{j+1}}{j+1}
   -\frac{T_{j-1}(2s-1)-(-1)^{j-1}}{j-1}
   \right].
   \]
   Each coefficient contributes to at most three positions, so this
   costs \(O(k)\) arithmetic operations and \(O(k)\) storage.
3. Evaluate \(A(s_i)\) at all \(k\) nodes by the three-term recurrence
   or Clenshaw recurrence, and write the corresponding new nodal states
   \(u_{\rm left}+hA(s_i)\). This costs \(O(k^2)\) arithmetic operations
   and constant extra scratch beyond the coefficient arrays. After all
   state coordinates are written, evaluate the field at those new states.

The discrete-cosine formula is the interpolant at the root nodes, and
termwise integration therefore produces exactly the same Picard map as
the integrated Lagrange weights. No \(k\times k\) transform or integration
table is materialized. Two generations of dense stage arrays and
\(O(k)\) scalar scratch suffice; the old derivatives remain intact while
the new states are formed. Endpoint and requested interior-time evaluation
use the same antiderivative, with \(O(k)\) work per coordinate once its
coefficients are formed. After the last iteration, its coefficient arrays
can replace released patch arrays before requested source times are read.

The nodes themselves need no exact trigonometric primitive. For
power-of-two \(k\), start from \(\cos(\pi/2)=0\) and use the positive
half-angle square root to obtain \(c=\cos(\pi/(2k))\); set
\(s=\sqrt{1-c^2}\). Generate successive node cosines by rotating
\((c,s)\) through the fixed angle \(\pi/k\), whose cosine and sine are
\(2c^2-1\) and \(2cs\). This uses \(O(k)\) arithmetic,
\(O(\log(k+1))\) square roots, and \(O(k)\) node storage. The same
construction works for \(Q\). These are exact-real identities, not a
finite-precision stability assertion.

Consequently the existing direct bound remains valid:

\[
W_{\rm physical}\le C N_F(Ln^2+dn)(m+K_{\rm solver}),\qquad
M_{\rm physical}\le C(Ln^2+dn)K_{\rm solver}.
\]

The \(O(k)\) scratch and nodes fit the second bound even when
\(k>n^2\); there is no extra width condition \(k\le n^2\). Streaming
the \(Q\) panel samples into their retained degree-\(K\) cosine sums
uses \(O(LnpQ)\) coordinates and \(O(LnpQ^2)\) arithmetic, without a
\(Q^2\) weight table. Computing initialized images by identical linear
operations preserves their exact pairing with preimages.

With the already established
\(N_F\le C\beta^{300L}(1+r)^3Z^6\),
\(K_{\rm solver}\le C\beta^{100L}(1+r)Z^{3/2}\), and
\(Q\le C\beta^{36L}\ell^{5/2}\), the published bounds are unchanged:

\[
W_{\rm init}\le CL\beta^{400L}
\{n^2[m(1+r)^4+p]+np^3\}Z^8,
\]
\[
M_{\rm init}\le CL\beta^{100L}
\{n^2(1+r)Z^2+npZ^3+p^2Z^5\}+Cp(d+1).
\]

Here memory is real coordinates; primitive descriptions and workspace
are the additional interface below. The first bound counts scalar
arithmetic, with primitive calls charged separately if not unit cost.

## 2. Charge the primitives explicitly

Only \(\phi_j\), \(\phi'_j\), and positive scalar square roots are
needed as function-evaluation primitives in this exact-real implementation.
The real-RAM convention also permits unit-cost exact sign/equality
comparisons, used by elimination, rank decisions and spectral selection.
Their counted decision slots fit the scalar operation bounds. This is
not a finite-bit procedure for deciding equality of arbitrary real inputs.
The \(\phi''_j\) bound enters the accuracy proof; its evaluation is not
an implementation step. The supplied integer schedule and its analytic
certificates are part of the initialization interface, not an uncharged
algorithm for obtaining activation bounds or the population gap.

Safe call bounds for initialization are

\[
N_\phi+N_{\phi'}\le CLn\{mN_F+pQ+m\},
\]
\[
N_{\sqrt{\ }}\le CL(m+1)N_F+L(R+1)
 +C\{1+\log(K_{\rm solver}+1)+\log(Q+1)\},
\qquad R\le3077\beta^{36L}p\ell^{5/2}.
\]

The first square-root term covers the physical solver's norm projections,
including optional feature/response projections; the second covers exact
basis normalization. Metric construction and solves can use elimination
without matrix-root primitives. All these call counts fit the displayed
initialization work order when each primitive has unit cost.

For any phase, let \(T_\phi,T_{\phi'},T_{\sqrt{\ }}\) bound the respective
single-call costs on its actual arguments. Its fully charged work is

\[
W_{\rm scalar}+N_\phi T_\phi+N_{\phi'}T_{\phi'}
 +N_{\sqrt{\ }}T_{\sqrt{\ }}+W_{\rm access}+W_{\rm cert}.
\]

Add the retained primitive-program descriptions and the maximum
single-call workspace to the coordinate-memory bound, under a consistent
storage unit. If descriptions or arithmetic are counted in bits, the
real-coordinate bound cannot silently be interpreted as a bit bound.
The envelope \(\beta\) does not bound these implementation costs. Exact
arbitrary-real activation evaluation is an explicit primitive assumption.

The old panel reads a specified dense reference. Its
\(O(Ln^2+nd+p(d+1))\) input real coordinates are already covered in peak
initialization memory; unit-cost reads fit the work bound. An external
encoding or precision oracle has its additional acquisition cost. The
statement does not generate an exact Gaussian reference from finite random
bits. Obtaining or verifying supplied analytic/gap certificates is likewise
not implied by their numerical values alone.

## 3. One training evaluation, one numerical step, and one query

Let \(q=9R\) be the common layer-width budget and let
\(D=qd+(L-1)q^2+q+m\) be the moving state dimension, including residuals.
The existing corrected-readout runtime gives

| Operation | Scalar arithmetic | Activation calls |
|---|---:|---:|
| One training vector-field evaluation | \(64Lmq^2\) | at most \(Lmq\) each of \(\phi,\phi'\) |
| Refresh the corrected-readout cache at a supplied state | \(24Lmq^2\) | at most \(Lmq\) of \(\phi\) |
| One panel query with that cache | \(4Lq^2\) | at most \(Lq\) of \(\phi\) |

There are no square-root or second-derivative calls in these three rows;
the training Gram solve is counted by arithmetic elimination. Cache
refresh is necessary after a state change and can be shared by all
queries at that state. A current query uses at most \(2q\) extra neuron
coordinates. Evaluating all \(p\) points multiplies the cached-query row
by \(p\), and optionally retains \(p\) outputs. The existing complete
runtime peak, rather than just \(D\), is

\[
2^{36}(L+1)\beta^{72L}p^2\ell^5+16p(d+1)
\]

real coordinates, plus primitive descriptions/workspace. Under the simpler
existing label cap, replace the two displayed \(\beta^{72L}\) and
\(\beta^{36L}\) width factors by one.

For a concrete numerical distinction, one forward-Euler step
\(\theta_{j+1}=\theta_j+hF(\theta_j)\) costs the RHS row plus at most
\(2D\) scalar operations; the existing RHS buffer permits an in-place
update. For a specified general explicit Runge--Kutta method with \(s\)
stages, a conservative per-step bound is \(sW_{\rm rhs}+Cs^2D\), with
\(s\) times the primitive calls and at most \(CsD+Cs^2\) extra coordinates
for retained stages and coefficients. Multiply by the actual step count,
and add requested observations and any rejected-step work.

These are costs conditional on the stated stage schedule and on its
training Grams being invertible. Neither a stable step size nor a number
of steps sufficient for a prescribed prediction error follows from the
continuous-time fitting theorem. No complete accurate numerical-training
cost, numerical endpoint theorem, or finite-bit selected-model conditioning
theorem has been established by this accounting.

## 4. Width and accuracy gates that must stay visible

The small-degree panel table uses the original degree gate

\[
\log_+(8192M_0/\chi)\le\ell,
\quad M_0=10\max_j\{H_j,\tau_j\},
\]

with the explicit activation recurrences in finite-panel `RESULT.md` (9).
This is what permits \(K+1\le768\chi^{-1}\ell^{5/2}\) and the stated
rank budget. Without that gate, retain the actual formula
\(K=\lceil\alpha^{-1}\log(64M_0n^{3/2}/\alpha)\rceil\),
\(\alpha=\chi/(128\ell^{3/2})\), in all counts; its activation logarithm
cannot be silently absorbed into \(\ell\).

All deterministic gates in finite-panel `RESULT.md` (20) admit the following
explicit, deliberately loose sufficient replacement:

\[
n^{-1}\le\min\{1,Y,16Yr\},\qquad
\ell\ge\beta^{50L}(1+r)^2.
\]

Here is the complete elementary check. Put \(S=16Yr\le1\), let
\(b=\max_j|\phi_j(0)|\), and let \(s\ge1\) bound the first derivatives
on the activation half-strip. The inherited envelope has
\(b,s\le\beta\), and the source recurrences are

\[
H_1=\max(1,b+20s),\qquad H_j=\max(1,b+10sH_{j-1}),\qquad
\tau_j=sH_L(10s)^{L-j}.
\]

Induction gives \(H_j\le\beta^{3j}\): the base uses
\(21\beta\le\beta^3\), and the step uses
\(\beta+10\beta^{3j-2}\le\beta^{3j}\). Therefore
\(\tau_j\le\beta^{5L-1}\le\beta^{6L}\) and
\(M_0\le\beta^{7L}\). The source quantities

\[
\mathcal K=H_L^2+S^2\left[\tau_1^2+
\sum_{j=2}^L\tau_j^2H_{j-1}^2\right],\qquad
D_W=\max\{\tau_1,\max_{j\ge2}\tau_jH_{j-1}\}
\]

satisfy \(\mathcal K\le(L+1)\beta^{18L}\le\beta^{20L}\) and
\(D_W\le\beta^{9L}\). Since \(\lambda=1/r\), the four quantities
on the right of the strip gate
\(\sqrt\ell\ge\chi r\max\{8,\lambda,4\mathcal K/\log2,32YSD_W\}\)
are respectively at most

\[
8r,\qquad1,\qquad6r\beta^{20L},\qquad
2\beta^{9L}.
\]

The last estimate uses \(32rYS=2S^2\). Each is at most
\(\beta^{25L}(1+r)\le\sqrt\ell\), because \(\beta\ge10\) and
\(L\ge2\). Also \(\beta^{50L}\ge2048e^2L\). Finally,

\[
\log_+(8192M_0/\chi)
\le\log8192+43L\log\beta
\le45L\log\beta\le\beta^{50L}\le\ell.
\]

Thus the degree gate is included as well. This replacement is an explicit
condition on \(\log n\); it can require an exponentially large \(n\).
It is not a polynomial sufficient-width theorem.

Retain the full original label intersection and the inherited,
unquantified stochastic success threshold. A strict width reduction needs
the separate check \(\lceil30000p\chi^{-1}\ell^{5/2}\rceil<n\).
No resource count makes that threshold or the actual-variability comparison
uniform as \(Y\to0\). If \(Y=0\), use the exact zero predictor.

The panel accuracy remains a maximum over the predeclared points and all
physical times. A forward pass on another point has the same computational
cost but no finite-panel approximation guarantee. The exact-real schedule
above closes a workspace ambiguity only; it does not close numerical
conditioning or the stochastic-width problem.
