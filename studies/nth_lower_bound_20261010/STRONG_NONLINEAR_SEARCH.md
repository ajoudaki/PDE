# Bounded search for a stronger nonlinear NTH obstruction

This is a theory-only scoped route, authored separately from the supervisor's
linear route. Its authorized scientific inputs were its earlier
`NONLINEAR_ROUTE.md` and lines 1–150 of
`docs/08b-trajectory-compression.qmd`; only the latter was newly consulted.
No other studies, numerical experiments, or external scientific sources were
used. The canonical-notation and rigorous-mathematics skills remain in force;
the conjecture-investigation skill and its research-contract and adversarial-audit
references were read for this bounded continuation.

**Outcome.** An explicit activation satisfying the book's analytic-strip
assumptions has individual source-flow Taylor radii tending to zero at large
Gaussian initialization values. Among Gaussian particles the smallest such
radius tends to zero with high probability. This disproves an elementary
width-independent source-analyticity argument based only on those activation
assumptions. It does **not** prove an \(\Omega(n)\), superpolynomial, or exponential
storage lower bound for frozen-top NTH. Gaussian averaging and the actual
self-consistent deep training equations are decisive missing bridges. A separate
exact example below demonstrates why the averaging bridge cannot be assumed.

## 1. Target and stopping rule

The intended target is the canonical fixed-depth \(L\ge2\) network with Gaussian
hidden initialization, zero initial readout, mobility \((n,1,\ldots,1,n)\),
fixed admissible dataset and activation, fixed positive population Gram gap,
and the stipulated fixed small nonzero labels. The approximation is specifically
the hierarchy which freezes its highest retained tensor at initialization.
Its error is compared to independent-dense variability in the same requested
prediction norm; changing to a parameter norm or an easier reference system
would not answer the question.

For a literal unsymmetrized tensor implementation and fixed sample count
\(m\ge2\), storage through tensor order \(q\) is of order \(m^q\). Consequently
an \(\Omega(n)\) raw-array lower bound requires an order lower bound of at least
\(\log_m n-O(1)\); a superpolynomial raw-array lower bound requires
\(q/\log n\to\infty\). These statements concern this representation only,
not optimal storage of tensors with symmetry or factorizations.

The bounded route tests one possible mechanism: real-unbounded activations,
Gaussian tails, and nearby complex singularities might make source-flow Taylor
truncation require such large orders, or might even prevent its convergence.
The route stops once the first unresolved bridge to actual prediction error is
identified. The desired complexity lower bound is a hypothesis, not a premise.

## 2. An explicit admissible activation

Fix \(c>1\), set \(b=\operatorname{arcosh}c>0\), and choose a fixed

\[
0<\varepsilon<\frac{(c-1)^2}{2(c+1)}.
\]

Define

\[
\phi(z)=z-\varepsilon\frac{\sin z}{c+\cos z}.
\tag{1}
\]

It is odd and real on the real axis. Its poles are at
\((2k+1)\pi\pm ib\), so it is holomorphic on every strip
\(|\operatorname{Im}z|<a<b\). On such a strip,

\[
|c+\cos z|\ge c-\cosh a>0,
\qquad
\phi'(z)=1-\varepsilon\frac{c\cos z+1}{(c+\cos z)^2},
\]

and hence

\[
|\phi'(z)|\le
1+\varepsilon\frac{c\cosh a+1}{(c-\cosh a)^2}.
\]

Thus the bounded-first-derivative strip condition is satisfied, although
\(\phi(x)=x+O(1)\) on the real line. On the real line the chosen epsilon also
gives \(\phi'(x)\ge1/2\), because
\(|c\cos x+1|\le c+1\) and \(|c+\cos x|\ge c-1\).
Its regularity constants are fixed independently of width. This activation
can be inserted into the admissible deep architecture; the next lemma instead
isolates a scalar source mechanism and does not claim that insertion preserves
the scalar dynamics.

## 3. A shrinking complex radius for a source particle

Consider the autonomous source system

\[
\frac{du}{d\tau}=\phi(z),\qquad
\frac{dz}{d\tau}=u\phi'(z),\qquad
u(0)=0,\quad z(0)=A,
\tag{2}
\]

and the particle output \(F_A(\tau)=u(\tau)\phi(z(\tau))\). The variable
\(\tau\) is an auxiliary source clock, not physical training time. This is
the unit-residual gradient direction for a scalar one-hidden-layer particle.
Because the vector field is holomorphic near its real initial point, it has
a locally holomorphic solution: for example, Picard iteration on a sufficiently
small complex disk converges uniformly using a local bound on the vector field
and its derivative, and uniform convergence preserves holomorphicity.

Take \(A=(2k+1)\pi>0\). Along the vertical segment \(z=A+iv\),
\(0\le v<b\), define the real functions

\[
V(v)=v+\varepsilon\frac{\sinh v}{c-\cosh v},\qquad
D(v)=1+\varepsilon\frac{c\cosh v-1}{(c-\cosh v)^2}>0.
\]

Then \(\phi(A+iv)=A+iV(v)\) and \(\phi'(A+iv)=D(v)\). Put

\[
I(v)=\int_0^v\frac{dw}{D(w)},\qquad
J(v)=\int_0^v\frac{V(w)}{D(w)}\,dw.
\]

Both are strictly positive for \(v>0\). Near \(v=b\),

\[
V(v)\sim\frac{\varepsilon}{b-v},\qquad
D(v)\sim\frac{\varepsilon}{(b-v)^2}.
\]

Consequently the finite limits \(I_*=I(b)>0\) and \(J_*=J(b)>0\) exist.

Eliminating source time from (2) gives the exact differential identity
\(d(u^2)/dz=2\phi(z)/\phi'(z)\). Integration on the vertical segment yields

\[
u(v)^2=2iA I(v)-2J(v).
\tag{3}
\]

Choose the square-root branch which has argument near \(\pi/4\) as
\(v\downarrow0\). It never encounters zero for \(v>0\), since the right
side has strictly positive imaginary part. The corresponding complex time is

\[
\tau_A(v)=\int_0^v
 \frac{i\,dw}{D(w)\sqrt{2iA I(w)-2J(w)}}.
\tag{4}
\]

This parametrizes the analytic continuation of the local solution from (2):
differentiating (3)–(4) reproduces both equations, and near zero
\(z-A=(A\phi'(A)/2)\tau^2+O(\tau^4)\), with the correct initial readout
derivative \(u'(0)=A\). No independent choice of a trajectory has been made.

Since \(|2iAI-2J|\ge2AI\),

\[
|\tau_A(v)|
\le\int_0^v\frac{dw}{D(w)\sqrt{2AI(w)}}
=\sqrt{\frac{2I(v)}A}
\le\sqrt{\frac{2I_*}A}.
\tag{5}
\]

The limit \(\tau_A^*=\lim_{v\uparrow b}\tau_A(v)\) therefore exists.
It is nonzero: the integrand in (4) has argument strictly between zero and
\(\pi/4\), so its integral cannot cancel. Dominated convergence in (4), using
the integrable bound \(1/[D(w)\sqrt{2I(w)}]\), further gives

\[
\sqrt A\,\tau_A^*\longrightarrow\sqrt{2iI_*}
\quad\text{as }A=(2k+1)\pi\longrightarrow\infty.
\tag{6}
\]

At this endpoint \(u\to u_*\ne0\), while \(z\to z_*=A+ib\), a pole of
the activation. The residue of \(\phi\) there is \(\varepsilon\), so

\[
\phi(z)\sim\frac{\varepsilon}{z-z_*},\qquad
F_A(\tau)\sim\frac{\varepsilon u_*}{z-z_*}.
\]

The output is therefore unbounded at \(\tau_A^*\). More precisely
\(\tau-\tau_A^*\sim-(z-z_*)^3/(3\varepsilon u_*)\), so this is a cubic-root
branch singularity of the output. The whole continuation path lies in the
disk bounded in (5). If the Taylor series of \(F_A\) at zero had a larger
radius, it would provide a bounded analytic continuation across this endpoint,
contradicting the divergence. Thus its radius \(R_A\) obeys

\[
R_A\le\sqrt{2I_*/A}.
\tag{7}
\]

This is a proved individual-source-output singularity, including its actual
observable. It is stronger than noting that the activation itself has poles.

## 4. The effect is not confined to probability-zero initialization values

Fix a small constant \(\delta_0>0\), for example \(1/4\). The same argument
gives, for all sufficiently large odd multiples \(A\) of \(\pi\), a uniform
bound

\[
R_{A+\delta}\le C A^{-1/2}
\qquad (|\delta|\le\delta_0),
\tag{8}
\]

where \(C\) depends on \(c,\varepsilon,\delta_0\) only. Here is the extension
explicitly. Continue first along the real segment from \(A+\delta\) to \(A\),
then along the earlier vertical segment. On the real segment,
\(\phi'(x)\) is bounded above and below by positive constants, and
\(\phi(x)\ge A/2\) for sufficiently large \(A\). Hence the absolute value of
\(u^2=2\int_{A+\delta}^z\phi/\phi'\) is at least a constant times
\(A|z-(A+\delta)|\); it has no zero other than the initial point. Integration
of \(d\tau=dz/(\phi'u)\) along this segment has absolute length at most
\(C\sqrt{|\delta|/A}\).

At the real endpoint \(u^2\) has a real value, denoted \(C_{A,\delta}\).
On the vertical segment the exact formula becomes

\[
u(v)^2=C_{A,\delta}+2iAI(v)-2J(v).
\]

It is nonzero for \(v>0\), and its modulus remains at least \(2AI(v)\).
The added time path has absolute length at most \(\sqrt{2I_*/A}\).
The endpoint readout is again nonzero and the particle output diverges at
the same activation pole. The entire time path lies within a disk of radius
\(CA^{-1/2}\), which proves (8), regardless of whether this continuation has
other singularities on other branches outside that path.

Now let \(G_1,\ldots,G_n\) be independent standard Gaussians. For large \(n\),
let \(A_n\) be the largest positive odd multiple of \(\pi\) at most
\(\sqrt{\log n}\). Thus \(A_n\sim\sqrt{\log n}\). The Gaussian probability
of \([A_n-\delta_0,A_n+\delta_0]\) is at least

\[
p_n\ge\frac{2\delta_0}{\sqrt{2\pi}}
 \exp\left[-\tfrac12(\sqrt{\log n}+\delta_0)^2\right].
\]

It satisfies \(np_n\to\infty\). Independence gives
\(\mathbb P(\text{no }G_i\text{ in this interval})\le e^{-np_n}\to0\).
Combining with (8), the Gaussian ensemble of scalar source particles satisfies

\[
\mathbb P\left(\min_{i\le n}R_{G_i}
                  \le C'(\log n)^{-1/4}\right)\longrightarrow1.
\tag{9}
\]

This is a high-probability statement about the minimum radius of individual
particle outputs. It does not assert the same radius for the empirical mean
or a lower bound on its real-axis approximation error.

## 5. Why the radius result does not prove an NTH complexity lower bound

First, a shrinking analytic radius has no general implication for the size of
a real-axis approximation error at the required scale. For instance, put

\[
A_n(t)=\frac{n^{-1}}{1+(t/\rho_n)^2},\qquad \rho_n\downarrow0.
\]

Its Taylor radius is \(\rho_n\), yet the degree-zero Taylor approximation
\(A_n(0)=n^{-1}\) has error at most \(n^{-1}=o(n^{-1/2})\) over the whole
real axis. A singularity may carry too little observable mass to matter.
In the network each particle has an explicit factor \(1/n\); that factor
cannot be ignored when using an extreme Gaussian particle.

Second, Gaussian averaging can restore a fixed analytic neighborhood even
when individual radii shrink. A complete example uses

\[
Q(z)=\frac1{c+\cos z},\qquad B_G(\tau)=Q(G\cosh\tau),\qquad G\sim N(0,1).
\]

For \(G=A=(2k+1)\pi\), a singularity occurs at
\(\cosh\tau=1+ib/A\), giving \(\tau\sim\sqrt{2ib/A}\) and thus radii
tending to zero as \(A\to\infty\). Nevertheless, the real-time population
average has a fixed analytic extension near zero. To see this, the geometric
series identity with \(r=e^{-b}\) gives the absolutely convergent real-axis
Fourier series

\[
\frac1{\cosh b+\cos z}
 =\frac1{\sinh b}\left[1+2\sum_{k\ge1}(-1)^k e^{-bk}\cos(kz)\right].
\]

For real \(\tau\), absolute convergence permits expectation term by term;
the Gaussian characteristic function then yields

\[
\mathbb E B_G(\tau)
 =\frac1{\sinh b}\left[1+2\sum_{k\ge1}(-1)^ke^{-bk}
          \exp\{-k^2\cosh^2\tau/2\}\right].
\tag{10}
\]

There is a fixed complex disk about zero on which
\(\operatorname{Re}\cosh^2\tau\ge1/2\). On that disk the terms are bounded
by \(e^{-bk-k^2/4}\), whose sum converges, as do the corresponding differentiated
series on every smaller disk. Formula (10) therefore defines a holomorphic
extension of the real-time population mean on a width-independent neighborhood.
This argument does not interchange a complex expectation across moving poles;
the Fourier formula is first proved on the real axis and then analytically
continued. It demonstrates that the averaging issue is real, not merely a
missing technical estimate.

Third, even divergence of an empirical source Taylor series would not by itself
control every finite order \(q=q(n)\). An order can depend on width; partial
sums may have a useful range before their ultimate divergence. A lower bound
must cover every smaller admissible order and quantify error at the relevant
shrinking target scale. The radius bound supplies neither estimate.

Fourth, the exact identification of frozen-top NTH with an ordinary Taylor
polynomial only holds in a scalar commuting-source reduction. With one training
sample, half-MSE loss, and \(\dot\tau=y-f\), the hierarchy becomes

\[
\frac{df}{d\tau}=K^{(2)},\qquad
\frac{dK^{(j)}}{d\tau}=K^{(j+1)}.
\]

Freezing order \(q\) makes the output a Taylor polynomial of degree \(q-1\)
in its **own** source clock. Even in that simplified setting its physical
clock solves \(\dot\tau_q=y-F_q(\tau_q)\); it need not agree with the exact
clock. Thus source error evaluated at a shared clock is not automatically
prediction error at a shared physical time.

The canonical problem has \(m\ge2\), a positive full feature Gram, and
\(L\ge2\). Its multiple residual directions and deep weight interactions
cannot be replaced by this scalar particle equation without an additional
exact invariant reduction or a quantitative perturbation proof. Choosing
antipodal duplicate inputs to force one scalar direction would make the
odd-activation feature Gram singular and would violate the stated setup.
Orthogonal inputs give a scalar population symmetry in the one-hidden-layer
case, but this does not produce an exact finite-width deep scalar reduction.

## 6. Claim ledger and stopping point

| Claim | Status | Evidence or missing bridge |
|---|---|---|
| Activation (1) obeys the fixed strip assumptions | Proved | Explicit derivative and denominator bounds |
| Its scalar source output has radius \(O(A^{-1/2})\) at large lattice initialization | Proved | Exact quadrature (3)–(7), with an actual output singularity |
| This survives initialization intervals of fixed positive length | Proved | Real-then-vertical continuation and uniform path-length bound (8) |
| Gaussian particle ensembles have vanishing minimum individual radius | Proved | Elementary Gaussian interval probability and (9) |
| Strip regularity alone supplies a uniform individual source radius | Refuted | The preceding admissible activation is a counterexample |
| Gaussian averaging necessarily retains the shrinking radius | Refuted as a general inference | Exact analytic population example (10) |
| The empirical NTH truncation has a prediction-level lower bound at some order scale | Open | Need finite partial-sum error, amplitude, cancellation, and clock control |
| The canonical deep network requires raw-array storage \(\Omega(n)\) or larger | Open in this route | Need a valid deep reduction or direct hierarchy argument and a same-norm dense-variability comparison |

The bounded route stops here. The first unresolved scientific bridge is a
quantitative lower bound for the empirical source observable at its relevant
finite truncation orders; a singularity radius is insufficient. Even closing
that bridge in the scalar diagnostic would leave the self-consistent-clock
and canonical-depth obligations. No \(\Omega(n)\), superpolynomial,
exponential, or all-order nonconvergence conclusion is established here.

The useful retained result is narrower: any proposed upper-bound proof which
asserts a width-independent complex source neighborhood for every Gaussian
particle from bounded-strip activation derivatives alone needs an additional
argument or assumption. This does not refute a population or observable-level
upper bound, whose cancellations can be materially different.
