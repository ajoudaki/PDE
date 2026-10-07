# A causal Taylor source with logarithmic power five-halves

2026-10-06. Scoped author derivation in the authorized efficiency search.
This is an internally derived source-solver result, conditional on the
existing dense fitting and finite-query complex source events. It is not
an independent reconstruction, promotion, compact decoder, or bit-cost
theorem. No experiment was performed.

The actual nonlinear source can be advanced by a causal time-Taylor
recurrence with one initialized matrix action per coefficient and layer.
On the inherited event, its initialized matrix-call count is at most

\[
 C\left[d+mL\beta^{200L}(1+m/\gamma)^2
                 Z^2\sqrt{\log(en)}\right].                 \tag{1}
\]

Here \(Z\) is defined below. At fixed problem parameters, the width
dependence is logarithmic power \(5/2\). The activation jets in this
statement are explicitly charged scalar operations; Section 6 supplies
a finite real-value approximation and explains its precision cost. The
construction still uses width-\(n\) vectors and the initialized matrices.
In particular, squaring (1) is not yet a proof of logarithmic-power-five
decoder storage.

The proof has two separate parts. A thin parameter neighborhood of the
true complex trajectory supplies analytic nearby flows and stable Taylor
maps at approximate anchors. A coefficientwise forward/backward recurrence
then removes the extra factor from repeated Picard iterations. The thin
neighborhood is a deterministic consequence of the existing source event;
no new large complex-time domain or Gaussian event is needed.

## 1. Model, accuracy, and the explicit horizon gate

Keep the model, loss, initialization, and label allowance of
[PHYSICAL_PARAMETER_ACCOUNTING.md](PHYSICAL_PARAMETER_ACCOUNTING.md):
\(v_a=x_a/\sqrt d\) has Euclidean norm one, the first matrix is \(A\),
the hidden matrices are \(W^{(j)}\), the stored readout is \(w\), and

\[
 z^{(1)}=Av,\qquad z^{(j)}=W^{(j)}h^{(j-1)},\qquad
 h^{(j)}=\phi_j(z^{(j)}),\qquad f_n(v)=w^Th^{(L)}/n.
\]

The readout is initially exactly zero. The residual is
\(r_a=f_n(v_a)-y_a\), with no residual inside the backward derivative.
All blocks train with mean squared loss and mobilities
\((n,1,\ldots,1,n)\). Let

\[
 \lambda=\gamma/m,\quad r=\lambda^{-1},\quad
 Y=\|y\|_2/\sqrt m>0,\quad S=16Yr\le1,\quad
 \ell=\log(en),\quad B=\beta^{100L},
\]
\[
 Z=(a_0+1)\ell+\log(e+B(1+r)),\qquad 1\le a_0\le12.
                                                               \tag{2}
\]

The scalar \(r\) is the inverse normalized gap; \(r_a\) is a sample
residual. The activation envelope \(\beta\ge10\) is accounting (2).
Use the original intersection of source and fitting label allowances,
without strengthening it. For \(Y=0\), the exact zero predictor needs
no solver.

The learned displacement is
\(u=(A-A_0,W^{(2)}-W_0^{(2)},\ldots,W^{(L)}-W_0^{(L)},w)\), with

\[
 \|u\|=\|A-A_0\|_F/\sqrt n+
     \sum_{j=2}^L\|W^{(j)}-W_0^{(j)}\|_F+\|w\|_2/\sqrt n.
                                                               \tag{3}
\]

Set \(\tau=\lambda t\), \(\bar u(\tau)=u(\tau/\lambda)/Y\).
This changes the proof coordinates, not the physical optimizer. Choose

\[
 T=2\{a_0\log n+\log(1+66Br)\}.
                                                               \tag{4}
\]

In addition to all inherited width gates, impose the explicit numerical gate

\[
 n\ge\max\{1,e^{-1}\sqrt{1+66Br}\}.                 \tag{5}
\]

Then \(2\log(1+66Br)\le4\ell\), and hence
\(T\le(2a_0+4)\ell\le28\ell<32\ell\). In particular the usual
choice \(a_0=10\) gives \(T<24\ell\). This use of the original
source horizon avoids any need for a late complex-carrier extension.
The gate is displayed and has polynomial dependence on the fixed
parameters; it does not hide a numerical-conditioning exponent.

The finite-query source in
[GENERAL_TRAJECTORY_LOWER_BRIDGE.md](../integrated_general_compression_20261004/GENERAL_TRAJECTORY_LOWER_BRIDGE.md),
Sections 2–3, supplies a complex-time radius \(r_\tau\) through
normalized time \(32\ell\), with

\[
 r_\tau^{-1}\le B\sqrt\ell.
                                                               \tag{6}
\]

The source (23), including its complex-time maximum, gives training
carrier bounds \(K_{\rm src}S\sqrt\ell\), preactivation imaginary
parts at most \(a/4\), operator caps ten, and its feature/backward RMS
bounds. Its short-contour residual argument gives, on a disk of radius
\(r_\tau/2\) about any real anchor \(\tau_j\le T\),

\[
 \|r(\zeta/\lambda)\|_2/\sqrt m
       \le2Y e^{-\tau_j/4}.                           \tag{7}
\]

Indeed the real fitting rate is at least \(1/4\) in normalized time,
and the complex residual equation has growth at most two on those short
pieces by the inherited width gates. All these disks lie inside the
source rectangle; the left endpoint has the source's negative-time padding.

The true complex derivative in the norm (3), after both normalizations,
is bounded by \(M=B(1+r)\). The prediction sensitivity on the real
parameter neighborhood used below is at most \(B\), uniformly over
all real unit queries. These bounds are the accounting subtraction
estimates with their exponent slack. The fitting tail divided by \(Y\)
after \(T\) is at most \(n^{-a_0}/4\).

## 2. A thin complex parameter neighborhood is sufficient

Define a deterministic decreasing cap and a normalized neighborhood radius:

\[
 q(\tau)=2^{-\lfloor\tau/4\rfloor},\qquad q_T=q(T),
 \qquad
 d_n=\frac{\beta^{-200L}q_T}{(1+r)^2\sqrt n}.
                                                               \tag{8}
\]

Thus a normalized-state distance \(d_n\) means physical parameter
distance \(Yd_n\) in (3). The radius is small for numerical stability;
it is not a new label restriction. Its logarithm satisfies

\[
 \log(d_n^{-1})
 \le200L\log\beta+2\log(1+r)+\tfrac12\ell
                         +\tfrac{\log2}{4}T\le CZ.             \tag{9}
\]

We record why the original, unclipped physical field is holomorphic
and controlled on this neighborhood of every complex source state.

First, the fitting assumptions imply
\(Y\le\beta^{3L}\) and \(r^{-1}=\lambda\le\beta^{6L}\);
these follow from \(Y\le H/(8\sqrt F)\), \(H\le\beta^{3L}\),
and \(\lambda\le H^2\). In a parameter segment of length \(Yd_n\),
stopped at the first exit from the half-strip, forward subtraction gives

\[
 \max_j\|\Delta z^{(j)}\|_2/\sqrt n
       \le\beta^{4L}Yd_n,
 \qquad
 \max_{i,j}|\Delta z_i^{(j)}|
       \le\sqrt n\,\beta^{4L}Yd_n<a/16.             \tag{10}
\]

The source operator cap ten may increase to eleven on this neighborhood;
the same finite forward recurrence with eleven in place of ten fits
inside \(\beta^{4L}\). The strict inequality in (10) follows from
\(a\ge16/\beta\), (8), and \(Y\le\beta^{3L}\). Thus the stopped
segment cannot exit the half-strip. Activation values retain linear
growth and all first/second derivative bounds used below.

Second, compare the backward pass with the reference source state.
At the top \(\Delta k^{(L)}=\Delta w\). At each lower layer split
the response difference as

\[
 \Delta\delta^{(j)}
 =\phi_j'(\widetilde z^{(j)})\odot\Delta k^{(j)}
  +[\phi_j'(\widetilde z^{(j)})-\phi_j'(z^{(j)})]
                                      \odot k^{(j)},
\]
\[
 \Delta k^{(j)}
 =\widetilde W^{(j+1)T}\Delta\delta^{(j+1)}
     +\Delta W^{(j+1)T}\delta^{(j+1)}.              \tag{11}
\]

The changed gate is multiplied by the *reference* carrier maximum
\(K_{\rm src}S\sqrt\ell\). The matrix difference multiplies a
bounded reference backward RMS. Using accounting's
\(K_{\rm src}\le\beta^{40L}\), forward bound (10), and a downward
induction, (11) yields the deliberately loose estimate

\[
 \max_j\frac{\|\Delta k^{(j)}\|_2+
                     \|\Delta\delta^{(j)}\|_2}{\sqrt n}
       \le\beta^{50L}(1+S\sqrt\ell)Yd_n.
                                                               \tag{12}
\]

There is one carrier maximum in this induction, not its \(L\)th power.
Converting (12) to a coordinate bound, and using
\(Y/S=(16r)^{-1}\), gives

\[
 \frac{\max_{i,j}|\Delta k_i^{(j)}|}{S\sqrt\ell}
 \le\frac{\beta^{-150L}q_T}{16r(1+r)^2}
                       (\ell^{-1/2}+S)<1.                     \tag{13}
\]

Here \(r^{-1}\le\beta^{6L}\), \(S\le1\), and \(\ell\ge1\)
make the last inequality explicit. Therefore nearby carriers have a
maximum at most \(2K_{\rm src}S\sqrt\ell\). The readout RMS can
increase from \(SH_L\) to \(2SH_L\); this and the operator cap eleven
are covered by the unused powers between the source recurrences and
\(\beta^{70L}\).

Finally, prediction subtraction in this same complex parameter segment
has coefficient at most \(\beta^{8L}\). On the neighborhood over a
patch anchored at \(\tau_j\), (7) and (8) give

\[
 \|\widetilde r\|_2/\sqrt m
 \le2Yq_j+\beta^{8L}Yd_n\le3Yq_j,
 \qquad q_j=q(\tau_j).                              \tag{14}
\]

Subtract the unclipped gradient products in residual, backward response,
and feature factors, as in accounting (6)–(8). The residual-difference
term does not contain the residual size; each of the other two terms
contains (14). The physical Jacobian norm is consequently bounded by

\[
 \beta^{70L}[1+Yq_j+YSq_j\sqrt\ell].
\]

Normalization multiplies a field Lipschitz bound by \(r\), not
\(r/Y\). Since \(Yr\le1/16\), the normalized holomorphic field
\(\overline F\) has, throughout these neighborhoods, the bound

\[
 \|D\overline F\|\le
 \Lambda_j:=B(1+r)(1+q_j\sqrt\ell).                 \tag{15}
\]

All norms here are the complex extensions of the ordinary block norms
in (3). They need not themselves be holomorphic. Holomorphy concerns
the field formulas, which use ordinary algebraic transposes and the
holomorphic activations, with no conjugates, clips, or projections.

## 3. Nearby flows and the Taylor-map stability estimate

Choose the ordinary patch length and shorten the last patch only:

\[
 h=\min\{1/8,r_\tau/8,[64B(1+r)\sqrt\ell]^{-1}\}.
                                                               \tag{16}
\]

Let \(h_j\le h\) be a patch length, \(H\) their count, and put

\[
 E=B(1+r)(T+9\sqrt\ell).
\]

Since the integral of \(q\) on the nonnegative line equals eight,
its left sums obey \(\sum_j h_jq_j\le8+h\le9\). Thus

\[
 H\le CB(1+r)Z\sqrt\ell,
 \qquad \sum_j h_j\Lambda_j\le E\le CB(1+r)Z,
 \qquad4h_j\Lambda_j\le1/8.                        \tag{17}
\]

At one patch start, let \(a=\bar u(\tau_j)\) be the exact anchor
and let \(b\) be real with \(\|b-a\|=e\le d_n/8\).
Let \(X_a(z)\) be the supplied exact flow, with local time \(z=0\)
at the anchor. The flow \(X_b\) of the same *unclipped* field exists
holomorphically for \(|z|<4h_j\) and satisfies

\[
 \|X_b(z)-X_a(z)\|\le e\exp(\Lambda_j|z|)<2e.
                                                               \tag{18}
\]

For a direct existence proof, on any closed disk of radius less than
\(4h_j\) iterate the difference equation

\[
 D(z)=b-a+\int_0^z
  [\overline F(X_a(s)+D(s))-\overline F(X_a(s))]\,ds.
\]

Use holomorphic functions continuous on that closed disk, with
\(\sup\|D\|\le d_n/2\), and integrate along the straight segment.
Section 2 makes the integrand holomorphic and (15) gives contraction
factor at most \(4h_j\Lambda_j\le1/8\). The map sends this ball
strictly into itself, since its norm is at most
\(d_n/8+(d_n/2)/8<d_n/2\). Successive differences are bounded by
a geometric series; the iterates converge uniformly to a holomorphic
solution. Uniqueness makes the solutions on nested disks agree.
Its sum with \(X_a\) solves the original field equation. Integrating
the difference inequality along each radial segment gives (18) by
the scalar integral Gronwall inequality. This proves existence and
stability without an analytic extension of a capped field.

Let \(\mathcal T_K(b;s)\) be the degree-\(K\) Taylor polynomial of
\(X_b\) at zero evaluated at \(s\in[0,h_j]\). Cauchy's coefficient
formula on the radius-\(2h_j\) circle and (18) give

\[
 \|[\mathcal T_K(b;s)-\mathcal T_K(a;s)]
                   -[X_b(s)-X_a(s)]\|
          \le2e\,2^{-K}.                            \tag{19}
\]

Indeed the tail is bounded by
\(2e\sum_{k>K}(s/(2h_j))^k\le2e2^{-K}\).
On the real segment the exact-flow difference is at most
\(e\exp(s\Lambda_j)\). The true derivative has bound \(M\)
on that same disk; integrating its Taylor tail bounds the true state
remainder by \(2Mh_j2^{-K}\). Consequently both endpoints and
interior times satisfy

\[
 \|\mathcal T_K(b;s)-X_a(s)\|
 \le[\exp(s\Lambda_j)+2\,2^{-K}]e
                          +2Mh_j2^{-K}.             \tag{20}
\]

In particular the committed endpoint obeys

\[
 e_{j+1}\le(1+2h_j\Lambda_j+2\,2^{-K})e_j
                              +2Mh_j2^{-K}.          \tag{21}
\]

The first-order stability factor in (21), rather than a constant two
per patch, is what permits logarithmic Taylor degree.

## 4. An explicit common degree closes the anchor bootstrap

Set

\[
 \varepsilon=\min\{d_n/64,n^{-a_0}/(64B)\},
\]
\[
 K=4+\left\lceil
 \frac{4E+\log[1+1024M(T+1)/\varepsilon]
                    +\log(1+16H)}{\log2}\right\rceil.
                                                               \tag{22}
\]

The additional \(H2^{-K}\) contribution in the product of (21)'s
multipliers is at most one. Starting from the exact zero displacement,
iteration of (21), followed by its interior version (20), gives

\[
 \sup_{0\le\tau\le T}
       \|\widetilde u(\tau)-\bar u(\tau)\|
 \le8M(T+1)e^{2E+1}2^{-K}<\varepsilon.              \tag{23}
\]

The right side is below \(d_n/64\), closing the assumed anchor
condition \(e_j\le d_n/8\) at every patch by induction. No clipping
of computed Taylor coefficients is used. Equations (9), (17), and
(22) give the explicit sufficient bound

\[
 K\le CB(1+r)Z.                                    \tag{24}
\]

Uniform prediction sensitivity contributes a factor \(B\), so the
normalized output error through \(T\) is less than
\(n^{-a_0}/64\). Freeze the numerical parameter state at \(T\).
The unchanged dense fitting tail then gives all-time, whole-sphere
normalized prediction error less than \(n^{-a_0}\), including the
true fitted endpoint. This finite source program need not itself fit
the labels exactly.

Smaller parameter or passive-source tolerances can replace
\(n^{-a_0}/(64B)\) in (22) without increasing the horizon: their
logarithms are added to \(K\). For example accounting (25a)'s target
adds \(O(L\log\beta+\log(Q+1)+\log(en))\), where \(Q\) is its
number of coefficient samples. This is a precision refinement of the
same source program, not an extension of its original complex event.

## 5. Coefficient recurrence and honest vector/scalar counts

Use the dimensionless local variable \(\xi=(\tau-\tau_j)/h_j\).
At an anchor store coefficient arrays through degree \(K\), where
\([k]\) denotes the coefficient of \(\xi^k\). The exact recurrence is

\[
 \bar u[0]=b,\qquad
 \bar u[k+1]=\frac{h_j}{k+1}
        [\xi^k]\overline F\left(\sum_{p=0}^k\bar u[p]\xi^p\right),
 \qquad0\le k<K.                                  \tag{25}
\]

Only already computed state coefficients occur on the right. At order
\(k\), evaluate the forward coefficients in increasing layer order,
then the backward coefficients in decreasing layer order, then the
residual and gradient coefficients. Thus (25) is a finite causal
calculation, not an implicit solve or future-trajectory input.

These are scaled time coefficients, not unscaled high derivatives.
On \(|\xi|=2\), Section 2 and (18) bound the nearby forward and
backward coordinate fields by \(\beta^{50L}\sqrt\ell\), and bound
their RMS norms by \(\beta^{50L}\). Cauchy's formula therefore gives
coefficient coordinate bounds
\(\beta^{50L}\sqrt\ell\,2^{-k}\) and RMS bounds
\(\beta^{50L}2^{-k}\). For a positive-order normalized parameter
coefficient, the bound on its derivative gives
\(\|\bar u[k]\|\le4Mh_j2^{-k}/k\): the nearby derivative is
bounded by \(M+2\Lambda_j e\le2M\). An initialized image inherits
the corresponding RMS bound times its operator cap. Converting that
image bound to a coordinate bound may still cost \(\sqrt n\);
this argument does not assert a new polylogarithmic coordinate maximum
for every raw initialized-matrix answer.

For a hidden layer, write \(D^{(j)}=W^{(j)}-W_0^{(j)}\). Its forward
and backward products at order \(k\) are exactly

\[
 z^{(j)}[k]=W_0^{(j)}h^{(j-1)}[k]
             +\sum_{p+q=k}D^{(j)}[p]h^{(j-1)}[q],
\]
\[
 k^{(j)}[k]=W_0^{(j+1)T}\delta^{(j+1)}[k]
             +\sum_{p+q=k}D^{(j+1)}[p]^T\delta^{(j+1)}[q].
                                                               \tag{26}
\]

The top carrier is \(w[k]\); the first initialized layer uses its
\(d\) root columns and fixed input coordinates. Each displayed
initialized action is executed once for this coefficient. Every learned
matrix action in (26) uses stored rank-one factors and scalar inner
products, with no additional initialized action.

For explicit rank accounting, define
\(g_a^{(j)}[q]=\sum_{p+s=q}r_a[p]\delta_a^{(j)}[s]\).
The physical learned hidden coefficients satisfy

\[
 D^{(j)}[k+1]
 =-\frac{2h_jr}{mn(k+1)}
       \sum_a\sum_{q+s=k}g_a^{(j)}[q]h_a^{(j-1)}[s]^T.
                                                               \tag{27}
\]

First-layer and readout coefficients have the corresponding two-factor
formula from the exact physical gradient. There are \(O(mK^2)\)
rank-one summands per hidden layer and patch, but only \(O(mK)\)
distinct left factors and \(O(mK)\) distinct right factors in (27).
One must count both facts: the source vector count and the scalar
coefficient description are different quantities.

For a scalar series \(z(\xi)=z[0]+v(\xi)\), \(v(0)=0\), the
activation coefficients are

\[
 [\xi^k]\phi(z(\xi))
  =\sum_{q=0}^k\frac{\phi^{(q)}(z[0])}{q!}
                                    [\xi^k]v(\xi)^q.
                                                               \tag{28}
\]

For \(\phi'\), the corresponding coefficient is
\(\phi^{(q+1)}(z[0])/q!\). Computing the powers by ordinary
coefficient convolutions costs at most \(O(K^3)\) scalar operations
per activation series and \(O(K^2)\) temporary scalar entries; no
unproved quadratic-time composition algorithm is assumed. Sequentially
requesting individual coefficients without caching may use a larger
fixed polynomial in \(K\), which still requires no extra matrix action.
The order-zero point \(z[0]\) is real, since every committed anchor
and every coefficient operation is real.

There are at most \(C mLHK\) initialized calls and principal coefficient
vectors, including forward, backward, residual-weighted backward, and
initialized-image vectors. Adding the first-layer roots and substituting
(17), (24) proves (1). Endpoint and interior polynomial evaluation uses
scalar combinations of these coefficients and adds no matrix calls.
A later passive query still needs its own forward initialized actions.

This count does not declare every temporary scalar-composition array a
new independent source vector. A row program can evaluate (28) within
its coordinatewise instruction and retain its coefficient output, while
charging that instruction's actual scalar work and scratch. If a compiler
instead records every scalar subinstruction as a separate history field,
its history size must be recomputed; it cannot simply substitute (1).
The learned coefficients in (27) alone may require
\(O(mLHK^2)\) scalar weights in a direct representation. Pairings,
coefficient selection, passive-query conditioning, and scalar-history
sensitivities remain separate costs.

## 6. Activation jets are a charged interface

The exact-real version of (25)–(28) uses the explicit scalar interface

\[
 (x,K)\longmapsto
    (\phi(x),\phi'(x),\phi''(x)/2!,\ldots,
                                    \phi^{(K+1)}(x)/(K+1)!),
 \qquad x\in\mathbb R.                            \tag{29}
\]

Let \(\mathcal A_\phi(K,b)\) be the actual work of evaluating this
list to absolute error \(2^{-b}\), and charge its storage as well.
The program uses \(mLH\) coordinatewise jet calls, hence
\(nmLH\) scalar calls of type (29), or \(O(nmLHK)\) scalar
derivative evaluations if the derivatives are evaluated separately.
Analytic derivative bounds do not make \(\mathcal A_\phi\) equal
to one. For a generic allowed activation, the original assumptions alone
do not supply a finite-bit cost for this interface.

There is nevertheless a direct finite real-value realization with no
additional initialized matrix calls. Put
\(D=\max\{1,4/a\}\) and choose a scalar spacing \(0<\eta\le1\).
For \(1\le q\le K+1\), define

\[
 J_q(x)=\frac{1}{q!\eta^q}
       \sum_{j=0}^q(-1)^{q-j}{q\choose j}\phi(x+j\eta).
                                                               \tag{30}
\]

The exact repeated-integral identity for forward differences is

\[
 \eta^{-q}\Delta_\eta^q\phi(x)
 =\int_{[0,1]^q}\phi^{(q)}(x+\eta(t_1+\cdots+t_q))\,dt.
\]

Cauchy's formula applied to \(\phi'\) on a circle of radius
\(a/4\) centered on the real line gives
\(\sup_{\mathbb R}|\phi^{(q+1)}|\le q!\beta D^q\).
Subtracting \(\phi^{(q)}(x)\) inside the integral therefore proves

\[
 |J_q(x)-\phi^{(q)}(x)/q!|
                    \le q\eta\beta D^q.             \tag{31}
\]

For a requested tolerance \(0<\varepsilon_{\rm jet}\le1\), choose
\(\eta=2^{-b}\), with integer \(b\ge0\), to be the largest such
power of two not exceeding one and the
following upper bound. This choice achieves jet error at most
\(\varepsilon_{\rm jet}/2\):

\[
 \eta\le
 \frac{\varepsilon_{\rm jet}}
            {2(K+1)\beta D^{K+1}}.
                                                               \tag{32}
\]

The \(K+2\) real values at \(x+j\eta\), \(0\le j\le K+1\),
can be shared by all differences. A difference table needs
\(O(K^2)\) scalar arithmetic and \(O(K)\) scratch. If each value
has error at most

\[
 \xi=\frac{\varepsilon_{\rm jet}}2
                               (\eta/2)^{K+1},                 \tag{33}
\]

its contribution to every \(J_q\) is at most
\(2^q\xi/(q!\eta^q)\le\varepsilon_{\rm jet}/2\).
The extra factor \(q+1\) converting the normalized derivative jet
to coefficients of \(\phi'\) is charged by requesting a jet
tolerance smaller by \(K+1\).

Equations (31)–(33) are uniform over real \(x\). They prove
constructive scalar approximation, not well-conditioned differentiation.
The value precision already has

\[
 \log(\xi^{-1})
 =O\bigl(K[\log(\varepsilon_{\rm jet}^{-1})
                           +K\log D+\log(K\beta)]\bigr).
                                                               \tag{34}
\]

The necessary \(\varepsilon_{\rm jet}\) must also pay for propagation
through the finite coefficient program. Such a tolerance exists and can
be chosen before running the program without any extra initialized call:
expand its additions, products and divisions by specified nonzero scalar
constants into a finite straight-line calculation. Bound the real inputs
by their supplied operator/RMS event and a factor \(\sqrt n\); bound
the derivative jets and their derivatives using the same Cauchy formula.
For each addition use the sum of operand bounds, for multiplication the
product, and for each propagated error the two-operand subtraction
identity. Recursing these upper bounds in the known instruction order
gives an explicit finite amplification factor. Choosing each jet error
below the desired final error divided by this factor and the number of
jet outputs suffices, by induction on that calculation. The final
max-coordinate tolerance is multiplied by the explicit norm conversion
from coordinates to (3), including division by \(Y\). The inherited
source gate \(Y\ge n^{-1}\) makes that conversion finite and explicit.

This construction may be extremely expensive in bits. It proves only
that replacing exact jets by finite value evaluation preserves the
initialized-call chronology, if the activation has a value evaluator at
the charged precision. It does not establish a small precision exponent,
cheap scalar arithmetic, or a stable noisy-matrix compiler for this
Taylor chronology. One may allocate half the error margin in (22) to
this finite scalar implementation and the other half to (23).

## 7. Claim boundaries and provenance

Established within this derivation, conditional on the supplied source
event: the thin complex parameter neighborhood, nearby-flow stability,
Taylor truncation recurrence, explicit logarithmic degree, coefficientwise
initialized-call schedule, and bound (1). The original fitting result,
activation class, physical time, and full inherited label allowance are
preserved. The additional horizon gate is (5), not an unreported
sufficient-width absorption. The stochastic source width remains
unquantified.

The exact-real source stage has a specified activation-jet interface.
A finite real-value approximation is given in (30)–(34), with its value
and propagation precision charged rather than treated as free.
Open: a useful complete bit/work bound for this implementation, its
Gaussian answer-noise compiler, source-selection precision, the full
uniform unseen-query replacement, and total retained and peak decoder
memory. None follows by merely squaring (1).

The complete assigned inputs read were SHORT_CAUSAL_TRAINING_PROGRAM,
PHYSICAL_PARAMETER_ACCOUNTING, SANE_INTEGRATED_COLLOCATION,
SANE_ADAPTIVE_TIME, and the four expressly authorized integrated-study
interfaces UNBOUNDED_COMPRESSOR_BRIDGE, GENERAL_TRAJECTORY_LOWER_BRIDGE,
ANALYTIC_TAIL_EXTENSION, and GENERAL_EXPLICIT_FITTING. Links from these
inputs to other studies were not followed. The rigorous-math and
conjecture-research skills and their relevant audit instructions were
read. The private canonical-notation skill was permission-inaccessible;
the supervisor-authorized fallback was the explicit repository notation
instructions and the maintained docs/notation.qmd contract. No maintained
file, Git index, or other study artifact was changed.
