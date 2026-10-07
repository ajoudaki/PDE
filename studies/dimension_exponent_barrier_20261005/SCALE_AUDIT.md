# Statistical scale and representation audit

Status: independent scoped theoretical audit, frozen 2026-10-05 before reading
any other route's findings. No experiments were performed. The inputs were the
assignment, this study's README, and `docs/notation.qmd`. The rigorous-math and
conjecture-investigation skills and their research-contract/adversarial-audit
references were read. The required custom canonical-notation skill was
inaccessible; the explicit user instructions and maintained notation contract
were applied. Every mathematical result below is derived here; no theorem about
the actual network's fluctuations is imported from another study.

The requested general autonomous construction and general impossibility theorem
are not established by this audit. Its concrete results identify why several
apparently natural dimension-exponent lower bounds do not follow, and give a
sufficient all-time stability estimate and precise conditional truncation and
information bounds.

## 1. Canonical object and the quantifiers that matter

Fix hidden depth \(L\geq2\), dimension \(d\), sample count \(m\geq d\), training
inputs \(x_a\in\mathbb R^d\) of length \(\sqrt d\) spanning \(\mathbb R^d\), and
labels \(y_a\). No orthogonality is assumed. The first matrix has independent
\(\mathcal N(0,1)\) entries, hidden matrices have independent
\(\mathcal N(0,1/n)\) entries, and the stored readout starts at zero. With
\(h^{(\ell)}=\phi^{(\ell)}(z^{(\ell)})\), the prediction is

\[
z^{(1)}(x)=W^{(1)}x/\sqrt d,\qquad
z^{(\ell)}(x)=W^{(\ell)}h^{(\ell-1)}(x),\qquad
f_n(t,x)=\frac{(W^{(L+1)}(t))^T h^{(L)}(t,x)}n.
\]

The loss is \(m^{-1}\sum_a(f_n(t,x_a)-y_a)^2\), and block mobilities are
\((n,1,\ldots,1,n)\). Everything below keeps this nonlinear feature-learning
model. Arguments using kernels refer to its exact evolving tangent kernel,
not a kernel frozen at initialization.

Write \(\mathbb S_d=\{x:\|x\|_2=\sqrt d\}\). The trajectory error is

\[
\|f-\widehat f\|_{\mathrm{traj}}
  =\sup_{t\geq0}\sup_{x\in\mathbb S_d}|f(t,x)-\widehat f(t,x)|,
\]

including limiting predictions when they exist. Statements involving a
deterministic limit \(f_\infty\), tight fluctuations, or all-time kernel
concentration below are explicitly conditional: these facts have not been
established from the permitted inputs.

The natural probability contract is a specified success probability
\(1-\delta_n\) and a deterministic tolerance
\(\varepsilon_n=n^{-1/2}A_n\). Fixed \(\delta_n\), polynomially decreasing
\(\delta_n\), and guarantees for every Gaussian realization are different
problems. Likewise, \(A_n\equiv A>0\), \(A_n\to\infty\), and \(A_n\to0\)
have different information requirements. An unspecified phrase “up to logs”
does not identify which one is intended.

For a word model, a statement about \(S_n\) stored words must also specify
the bits \(b_n\) per word. If \(b_n=\Theta(\log(en))\), then a lower bound
on bits \(B_n\) gives only \(S_n\geq B_n/b_n\). All initialization-dependent
constants, decoder data, evolving state, and live workspace must be counted.
None of the finite-cover arguments below supplies an inexpensive decoder.

## 2. What is exactly visible at initialization

Let \(\theta\) denote all weight entries, with mobility \(\mu_j\) on entry
\(\theta_j\). Define the exact tangent kernel

\[
K_n(t;x,x')=\sum_j\mu_j
 \frac{\partial f_n(t,x)}{\partial\theta_j}
 \frac{\partial f_n(t,x')}{\partial\theta_j}.
\]

Differentiating the loss and applying the chain rule gives

\[
\partial_t f_n(t,x)
 =-\frac2m\sum_{a=1}^m
       K_n(t;x,x_a)(f_n(t,x_a)-y_a).
\tag{2.1}
\]

At zero readout every hidden-weight derivative of the prediction vanishes.
The readout derivative is \(h^{(L)}(0,x)/n\), and its mobility is \(n\).
Consequently,

\[
K_n(0;x,x')
  =\frac{h^{(L)}(0,x)^T h^{(L)}(0,x')}n,
\qquad
\partial_t f_n(0,x)
  =\frac2m\sum_a y_a
     \frac{h^{(L)}(0,x)^T h^{(L)}(0,x_a)}n.
\tag{2.2}
\]

Also \(\partial_t W^{(\ell)}(0)=0\) for every hidden layer, while
\(\partial_t W^{(L+1)}(0)=2m^{-1}\sum_a y_a h^{(L)}(0,x_a)\).
These are exact initial identities, not a justification for freezing hidden
features at later times. In particular, the \(n^2\) Gaussian entries of a
dense hidden matrix are not directly observable as \(n^2\) independent
prediction coordinates at initialization: all predictions are exactly zero.
A useful lower bound must propagate distinguishable initialization information
into the prediction trajectory at the required error scale.

Even a central limit theorem for (2.2), if proved, would address an initial
slope. It would not by itself identify the distribution, all-time tightness,
or storage requirements of the full trained trajectory.

## 3. An all-time stability lemma without frozen features

The next statement is a deterministic comparison lemma. It applies to actual
time-dependent kernels; it does not construct either kernel.

Let \(f(t,x)\) and \(g(t,x)\) start at zero and satisfy (2.1) with kernels
\(K\) and \(G\), respectively. Set

\[
r_a(t)=f(t,x_a)-y_a,\qquad s_a(t)=g(t,x_a)-y_a.
\]

Let \(K(t),G(t)\in\mathbb R^{m\times m}\) be their training Gram matrices,
and let \(k(t,x),g_K(t,x)\in\mathbb R^m\) have entries
\(K(t;x,x_a),G(t;x,x_a)\). Suppose, uniformly in physical time,

\[
K(t)\succeq\lambda I,\qquad G(t)\succeq\mu I,
\qquad \|K(t)-G(t)\|_{\mathrm{op}}\leq\delta_{\mathrm{train}},
\tag{3.1}
\]

where \(\lambda,\mu>0\). Suppose also, for every \(x\in\mathbb S_d\),

\[
\|k(t,x)\|_2\leq B,\qquad
\|k(t,x)-g_K(t,x)\|_2\leq\delta_{\mathrm{cross}}.
\tag{3.2}
\]

Then both predictions have uniform limiting values on the sphere, and

\[
\|f-g\|_{\mathrm{traj}}
 \leq\frac{\|y\|_2}{\mu}
   \left(\delta_{\mathrm{cross}}
           +\frac{B\,\delta_{\mathrm{train}}}{\lambda}\right).
\tag{3.3}
\]

To prove this, \(s'=-(2/m)Gs\) and (3.1) imply
\(\|s(t)\|_2\leq\|y\|_2 e^{-2\mu t/m}\). The homogeneous equation
\(v'=-(2/m)Kv\) has evolution operator norm at most
\(e^{-2\lambda(t-u)/m}\) from time \(u\) to time \(t\), because
\((\|v\|_2^2)'=-(4/m)v^TKv\leq-(4\lambda/m)\|v\|_2^2\).
For \(e=r-s\),

\[
e'=-(2/m)Ke-(2/m)(K-G)s,\qquad e(0)=0.
\]

Variation of constants and then integration of its nonnegative bound give

\[
\begin{aligned}
\int_0^\infty\|e(t)\|_2\,dt
&\leq \frac{2\delta_{\mathrm{train}}}{m}
 \int_0^\infty\int_u^\infty
 e^{-2\lambda(t-u)/m}\|s(u)\|_2\,dt\,du\\
&\leq \frac{m\,\delta_{\mathrm{train}}\|y\|_2}
                 {2\lambda\mu}.
\end{aligned}
\]

At an arbitrary test input,

\[
\partial_t(f-g)=-(2/m)
 \left[k(t,x)^T e(t)
       +(k(t,x)-g_K(t,x))^Ts(t)\right].
\]

Integrating this identity, using (3.2), and using
\(\int_0^\infty\|s(t)\|_2dt\leq m\|y\|_2/(2\mu)\) proves (3.3).
The same estimates show that both time derivatives are integrable uniformly
on the sphere: \(r\) decays with gap \(\lambda\), and
\(\|g_K(t,x)\|_2\leq B+\delta_{\mathrm{cross}}\). Hence their limiting
values exist uniformly, and the bound includes the endpoints.

If the actual trained kernels and a deterministic reference satisfy these
conditions with \(\delta_{\mathrm{train}},\delta_{\mathrm{cross}}
=O(n^{-1/2}\operatorname{polylog}n)\), the prediction scale follows for all
time. An initialized gap alone is not (3.1), and initialized concentration is
not uniform concentration of the evolving kernels. Further, presenting
\(G(t)\) as a supplied time-dependent function would violate the autonomous
representation requirement. This lemma addresses stability and statistical
scale, not that missing construction.

## 4. Tight fluctuations do not imply growing information at their own scale

Suppose a deterministic trajectory \(f_\infty\) exists and define

\[
Z_n(t,x)=\sqrt n\,[f_n(t,x)-f_\infty(t,x)].
\]

The following consequences require tightness in the trajectory supremum norm,
not pointwise or compact-time convergence.

If \(\|Z_n\|_{\mathrm{traj}}=O_{\mathbb P}(1)\) and \(A_n\to\infty\), then

\[
\mathbb P\left(
\|f_n-f_\infty\|_{\mathrm{traj}}>n^{-1/2}A_n\right)\longrightarrow0.
\tag{4.1}
\]

Indeed, for every \(\delta>0\), tightness of these scalar norms supplies a
finite \(M\) with \(\limsup_n\mathbb P(\|Z_n\|>M)\leq\delta\).
Eventually \(A_n\geq M\), so the limit superior in (4.1) is at most
\(\delta\); let \(\delta\downarrow0\). Thus any positive logarithmic
slack permits dropping initialization fluctuations altogether at probability
tending to one, conditional on this tightness. A prescribed failure rate such
as \(n^{-10}\) needs quantitative tails and does not follow from tightness.

For fixed confidence and fixed normalized tolerance, there is a stronger
information statement. Suppose \(Z_n\) are tight as random elements of a
function space equipped with this norm. For any fixed \(\delta>0\), a compact
set \(\mathcal K_\delta\) contains \(Z_n\) with probability at least
\(1-\delta\) for all sufficiently large \(n\). For any \(c>0\), compactness
provides a finite \(c\)-net of \(\mathcal K_\delta\), of size
\(M(c,\delta)\) independent of \(n\). Translating by \(f_\infty\) and
scaling by \(n^{-1/2}\) gives a cover of the corresponding high-probability
prediction set at accuracy \(cn^{-1/2}\) using the same number of centers.

Consequently, neither the number of Gaussian weight entries nor infinitely
many nonzero fluctuation modes alone proves an increasing information lower
bound at fixed normalized tolerance. This argument is not a representation:
its centers are entire trajectories, and there is no permitted autonomous
procedure here for storing or evaluating them. It isolates exactly the
limitation of a metric-entropy argument.

## 5. Conditional analytic fluctuation truncation

There is a quantitative version of the preceding distinction. For \(d\geq2\),
suppose the normalized fluctuation has a spherical-harmonic decomposition
\(Z_n=\sum_{k\geq0}Z_{n,k}\), uniformly over all physical time, with

\[
\sup_{t,x}|Z_{n,k}(t,x)|
 \leq C_d(\log(en))^c e^{-\rho_d k},
\qquad C_d>0,\quad \rho_d>0,\quad c\geq0.
\tag{5.1}
\]

This assumption can hold on an event with a stated probability; all following
bounds then hold on that event. It is not inferred merely from the word
“analytic”: the radius, envelope, all-time control, and dependence on \(n\)
are part of the assumption. If \(C_d=0\), every harmonic component and the
fluctuation itself vanish identically, so no fluctuation coefficients need
be stored and the logarithmic truncation formula below is unnecessary.

For a desired fluctuation error
\(n^{-1/2}(\log(en))^{-b}\), where \(b\geq0\), choose

\[
p_n=\max\left\{0,
 \left\lceil\frac{
   \log(2C_d/(1-e^{-\rho_d}))
       +(b+c)\log\log(en)}{\rho_d}\right\rceil\right\}.
\]

Summing a geometric series gives

\[
\sup_{t,x}\left|Z_n-\sum_{k=0}^{p_n}Z_{n,k}\right|
 \leq\frac{C_d(\log(en))^c e^{-\rho_d(p_n+1)}}
                  {1-e^{-\rho_d}}
 \leq\tfrac12(\log(en))^{-b}.
\tag{5.2}
\]

The space of spherical polynomials of degree at most \(p\) has dimension

\[
N_d(p)=\binom{d+p}{d}-\binom{d+p-2}{d}
      =\binom{d+p-1}{d-1}+\binom{d+p-2}{d-1}
      =O_d((1+p)^{d-1}).
\tag{5.3}
\]

Terms with a negative degree are zero. One way to obtain this count is to
restrict ordinary degree-\(p\) polynomials to the sphere: the kernel consists
of multiples of \(\|x\|_2^2-d\) of degree at most \(p-2\). To verify this
description, divide a vanishing polynomial by the monic polynomial
\(x_d^2+\sum_{j<d}x_j^2-d\), leaving a remainder
\(a(x_1,\ldots,x_{d-1})x_d+b(x_1,\ldots,x_{d-1})\). At both sphere points
over every \((x_1,\ldots,x_{d-1})\) in the open radius-\(\sqrt d\) ball,
the remainder is zero. Addition and subtraction give \(a=b=0\) on an open
set, so these polynomials vanish identically. Division preserves the stated
total-degree bound. This proves the dimension difference; the second formula
uses Pascal's identity. The case \(d=1\) is a two-point sphere and has at most
two spatial coefficients.

In particular,

\[
N_d(p_n)=O_{d,C_d,\rho_d,b,c}
          ((1+\log\log(en))^{d-1}).
\tag{5.4}
\]

This growth has no dimension-linear exponent in \(\log n\) under the
specified fixed-dimension-first limit. For \(q\geq1\) and \(u\geq0\),

\[
(1+u)^q\leq q^q e^{1-q}e^u,
\]

because \((1+u)^qe^{-u}\) has its maximum at \(u=q-1\).
Taking \(u=\log\log(en)\) shows that (5.4) is
\(O_d(\log(en))\). The displayed constant grows at least as rapidly as
\(q^qe^{1-q}\) in this bound, in addition to the dependence on the analytic
envelope and radius. This is not a uniform joint \(d,n\) estimate.

The finite precision accounting is also favorable for this conditional
fluctuation truncation. Take an orthonormal basis \(Y_1,\ldots,Y_N\) of the
degree-at-most-\(p_n\) space in the uniform probability measure on the sphere.
Rotation invariance implies \(\sum_jY_j(x)^2=N\): the sum is independent of
the orthonormal basis, hence rotation invariant, and its integral is \(N\).
Quantizing each coefficient with error at most
\((\log(en))^{-b}/(2N)\) therefore incurs supremum error at most
\((\log(en))^{-b}/2\), by Cauchy–Schwarz. Assumption (5.1) bounds each
coefficient by \(C_d(\log(en))^c/(1-e^{-\rho_d})\), so each needs
\(O_d(1+\log\log(en))\) bits. The entire instantaneous fluctuation vector
uses \(O_d((1+\log\log(en))^d)=O_d(\log(en))\) bits.
Here and in the finite-precision counts above, \(O_d\) also permits dependence
on the fixed quantities \(b,c,\rho_d,C_d\); none may vary with \(n\).

This statement concerns a spatial representation at each time with one
uniform-in-time error bound. It gives no closed evolution for the retained
coefficients, no initialization-only method for finding them, and no decoder
for the deterministic \(f_\infty\). Storing their time histories would be
forbidden playback. Thus it is not an autonomous positive solution. It does,
however, invalidate an inference that analytic *fluctuation* modes must be
retained to degree \(\Theta(\log n)\) merely because the original prediction
error is \(n^{-1/2}\): their amplitude already contains that factor.

## 6. What finite-storage lower bounds actually need

Suppose the entire instance-dependent representation contains at most
\(B_n\) bits, and its evolution and decoder are fixed deterministic rules.
It can generate at most \(2^{B_n}\) distinct trajectories. Therefore:

* If the target class has \(M_n\) members separated by more than
  \(2\varepsilon_n\) in trajectory norm and every member must be
  approximated, then \(B_n\geq\log_2 M_n\). One decoded trajectory cannot
  approximate two separated targets, by the triangle inequality.
* For a random target, let
  \(q_n=\sup_h\mathbb P(\|f_n-h\|_{\mathrm{traj}}\leq\varepsilon_n)\),
  where the supremum is over deterministic trajectories. Success with
  probability at least \(1-\delta_n\) requires
  \(2^{B_n}q_n\geq1-\delta_n\), by the union bound, hence
  \(B_n\geq\log_2((1-\delta_n)/q_n)\).

These arguments need no regularity of the encoder or decoder. They do need a
finite bit budget. An unconstrained number of exact real coordinates has no
such counting bound; forbidding bit packing in prose alone does not determine
a substitute regularity or computational class.

Here is a concrete Gaussian specialization. At a fixed time, use uniform
probability measure on \(\mathbb S_d\) and \(D\) orthonormal test functions.
Suppose the corresponding coefficients of \(\sqrt n(f_n-f_\infty)\) are
exactly independent centered Gaussians with standard deviations
\(\sigma_1,\ldots,\sigma_D>0\). Supremum prediction error at most
\(\varepsilon_n\) implies Euclidean coefficient error at most
\(A_n=\sqrt n\varepsilon_n\), by the orthonormal projection inequality.
Every Euclidean ball of radius \(A_n\) has Gaussian probability at most

\[
q_n\leq\min\left\{1,
 \frac{A_n^D}
 {2^{D/2}\Gamma(D/2+1)\prod_{j=1}^D\sigma_j}\right\}.
\tag{6.1}
\]

Indeed, the Gaussian density is at most
\((2\pi)^{-D/2}\prod_j\sigma_j^{-1}\), and the ball's volume is
\(\pi^{D/2}A_n^D/\Gamma(D/2+1)\). Multiplying proves (6.1), uniformly over
the center and therefore over decoded functions.

The critical issue is the spectrum at the normalized tolerance \(A_n\).
For fixed \(D\), fixed \(\sigma_j\), and \(A_n\) bounded below, (6.1) has
no growing dependence on \(n\). A lower bound based on an increasing
\(D=D_n\) must prove that sufficiently many coefficients stay distinguishable
at that tolerance. A fixed-dimensional central limit theorem does not justify
using Gaussian estimates in dimensions growing with \(n\). Gaussian support
alone does not give such a high-probability statement: an arbitrarily unlikely
open neighborhood of an engineered initialization is insufficient.

There is a related restriction for deterministic limits parametrized by the
data. Let \(z\) range over a bounded subset of \(\mathbb R^p\), collecting
the admissible fixed-dimensional inputs and labels, and suppose

\[
\|f_\infty(z)-f_\infty(z')\|_{\mathrm{traj}}
 \leq C\|z-z'\|_2.
\tag{6.2}
\]

A Euclidean grid of mesh proportional to \(\varepsilon/C\) gives a cover
of this deterministic trajectory family with at most
\((1+C'/\varepsilon)^p\) elements. If the normalized fluctuation family is
uniformly tight over \(z\), its fixed-confidence compact set has a finite
\(c/2\)-net of size \(M\). Combining the two covers at
\(\varepsilon=cn^{-1/2}\) gives a high-probability target cover of size at most

\[
M\left(1+C''\sqrt n/c\right)^p,
\qquad \log_2 M_n=O_{p,C'',c,M}(\log(en)).
\tag{6.3}
\]

Neither (6.2) nor uniform tightness is asserted for the present network without
proof. If they hold, pure metric entropy cannot force a
dimension-linear power of \(\log n\) stored words. It can still be very hard
to compute the covered functions with small total workspace. A codebook of
entire trajectories would have large storage and violate the intended
autonomous construction; (6.3) is expressly not such a construction.

Conversely, the mode count of the *ambient class* of analytic sphere functions
is not a packing of the actual network trajectory family. Full rank of the
training inputs says their linear span is \(\mathbb R^d\). It does not say
that independently adjustable analytic coefficients in all spherical modes
are reachable under Gaussian initialization, small labels, and training.
That reachability-and-probability bridge is necessary for the usual generic
analytic-function entropy argument.

## 7. All-time and self-variability qualifications

Compact-time fluctuation control does not supply the tightness used in
Sections 4–6. A useful elementary check makes the growing horizon explicit.
If two prediction trajectories satisfy, for positive constants
\(A,\gamma\) independent of \(n\),
\(\sup_x|\partial_t f(t,x)|,\sup_x|\partial_t g(t,x)|\leq A e^{-\gamma t}\),
then, for \(t\geq T\),

\[
\sup_x|f(t,x)-g(t,x)|
 \leq\sup_x|f(T,x)-g(T,x)|+2A\gamma^{-1}e^{-\gamma T}.
\]

To make the last term comparable to \(n^{-1/2}\), one needs
\(T\) of order \(\log n\), unless a stronger direct fluctuation estimate is
available. Convergence on every fixed horizon permits constants depending on
that horizon and cannot be silently substituted at this growing \(T\).
The kernel lemma in Section 3 gives one direct all-time route, with its
additional hypotheses fully visible.

An upper error envelope is also different from the random discrepancy of two
independent runs. Even for the scalar model
\(F_n=\mu+n^{-1/2}Z\), \(F'_n=\mu+n^{-1/2}Z'\), where \(Z,Z'\) are
independent standard normals, there is no finite deterministic constant \(C\)
for which \(|F_n-\mu|\leq C|F_n-F'_n|\) almost surely. The event
\(1<Z<2\), \(|Z-Z'|<1/(2C)\) has positive probability and violates the
inequality. Thus “within self-variability” should refer to a specified
quantile, root-mean-square scale, or probabilistic comparison, rather than an
unstated pathwise domination by the observed discrepancy of one pair of runs.

For the actual network, zero initial readout makes run-to-run prediction
variability exactly zero at time zero. Exact interpolation makes it zero at
the training inputs at the endpoint. These facts do not eliminate whole-sphere
variability, but they preclude importing an everywhere positive pointwise
reference scale. If all labels are zero, the entire trajectory is identically
zero; a nontrivial lower bound must be a worst-case or nondegenerate-instance
statement, not a claim for every admissible label vector.

Finally, real analyticity alone gives neither the needed Gaussian moments nor
an all-time analytic envelope. For example, the entire function
\(\phi(z)=e^{z^2}\) has
\(\mathbb E\phi(Z)^2=\infty\) for a standard normal \(Z\), since its
Gaussian integral contains \(e^{3z^2/2}\). If the admissible activation class
already imposes growth and derivative bounds, those hypotheses should be
carried into any scale theorem explicitly. This example flags an assumption
needed by concentration arguments; it is not offered as a substitute model
or as a counterexample to a more restrictive established activation class.

## 8. Exact remaining obligations

The positive route still needs an initialization-only autonomous representation
for the deterministic feature-learning evolution and any retained random
corrections, with a count of all fixed data and live workspace. Spatial
truncation alone does not close the dynamics. It also needs a proved
all-time, whole-sphere error source bound; the stability estimate in Section 3
only propagates such a bound.

The negative route needs a precisely specified finite-precision, regular, or
computational representation class and an actual learned-trajectory packing
or small-ball bound at the normalized error scale. If it relies on Gaussian
fluctuations, it must justify the required number of distinguishable modes
and their probability mass in the relevant growing dimension. If it relies
on deterministic analytic functions, it must prove those functions are
reachable by the given model rather than count an ambient function class.

The scale question itself remains conditional: a positive initialized Gram
gap, small labels, and analytic activation do not, in the scoped inputs, supply
the uniform evolving-kernel concentration or tightness assumed above. The
highest-leverage missing scientific statement for this audit is a
whole-sphere, all-time normalized fluctuation bound for the actual trained
model, with its confidence and dimension dependence explicit. Without it,
neither a stochastic storage barrier nor a statistically accurate deterministic
surrogate has been proved.
