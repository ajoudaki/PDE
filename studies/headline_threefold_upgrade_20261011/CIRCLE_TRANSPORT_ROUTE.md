# Circle transport: dimension-free probe control and the remaining cancellation

2026-10-11. Scoped first-round theoretical route. Scientific inputs were only
`paper/compact.tex`, `paper/compact_fitting.tex`,
`ENDPOINT_SEPARATION_STRUCTURE.md`, `ENDPOINT_SEPARATION_CAVITY.md`, and
`ENDPOINT_PROBE_NONCANCELLATION.md`. The required conjecture, rigorous-proof,
and canonical-notation skills, including the neural-network reference, were
applied. No experiment, manuscript edit, external scientific source, or Git
operation was used.

**Result.** The original label cap gives width-independent probabilistic
control of a trained top-neuron probe and a width-independent trace-norm
bound on the derivative of its incoming-root transport. This repairs the
vanishing-probability unit-ball chart as a method for obtaining upper bounds.
It does not supply a lower bound on the compensated influence covariance.
The requested actual-network circle separation remains open in this route.

The targeted second round in `CIRCLE_PROBE_READOUT.md` adds the uniform
direct-readout lower bound \(\|a_\infty\|_{L^2(g)}\ge Y/(6H)\) on
a cavity event of probability tending to one, under the unchanged cap.
The compensated covariance and actual-network separation gaps below remain.

## Contract

The input dimension is two, so write
\(v(\theta)=(\cos\theta,\sin\theta)\) and
\(x(\theta)=\sqrt2v(\theta)\). There are finitely many fixed pairwise
nonparallel training directions, nonzero fixed labels, a fixed depth
\(L\ge2\), zero initial readout, and the canonical Gaussian hidden
initialization. All layers train with the original mobilities. The
activations are nonaffine, strip analytic, with bounded strip derivative;
they need not be bounded. Put

\[
\lambda=\gamma/m,\qquad
Y=\|y\|/\sqrt m,\qquad
0<Y\le\lambda\beta^{-30L}.
\]

The target is that, for every \(\delta>0\), some width-independent
\(c_\delta>0\) satisfies, eventually at every individual width,

\[
\Pr\left\{\sup_\theta
 |f_n(\infty,x(\theta))-\widetilde f_n(\infty,x(\theta))|
 \ge c_\delta n^{-1/2}\right\}\ge1-\delta.
\]

An open arc separated from the training directions and their antipodes
would suffice. No smaller label cap, frozen hidden layer, or replacement
initialization is introduced below.

## 1. Typical roots are controlled by the feature path, not their norm

Fix a successful cavity obtained by deleting one top neuron, retaining the
original width in every normalization. Its lower training features are

\[
H_a(t)=h^{(L-1)}(t,v_a)/\sqrt n\in\mathbb R^n.
\]

The cavity path is fixed throughout the conditional arguments. Let
\(\rho(t)=\|r(t)\|/\sqrt m\). The supplied fitting estimates give

\[
\rho(t)\le Ye^{-\lambda t/2},\qquad
\sup_{t,a}\|H_a(t)\|\le B:=2H.
\tag{1}
\]

The forward differentiation recursion in the fitting proof gives, for
the already defined fitting coefficient \(F_{L-1}\),

\[
\|\dot H_a(t)\|
\le2F_{L-1}\rho(t)\frac{\|w(t)\|}{\sqrt n}
\le\frac{4F_{L-1}Y}{\sqrt\lambda}\rho(t).
\]

Consequently each feature path has total variation at most

\[
\int_0^\infty\|\dot H_a(t)\|\,dt
\le V:=\frac{8F_{L-1}Y^2}{\lambda^{3/2}}.
\tag{2}
\]

Let \(g\sim N(0,I_n)\), independently of the cavity. Define

\[
M(g)=\max_{1\le a\le m}\sup_{t\ge0}|g^\top H_a(t)|.
\tag{3}
\]

Although \(\|g\|\) grows as \(\sqrt n\), the random variable (3) has
width-independent moments. If \(Z\sim N(0,1)\) and
\(c_p=(\mathbb E|Z|^p)^{1/p}\), then for every \(p\ge1\),

\[
\|M\|_{L^p(g)}\le m^{1/p}c_p(B+V).
\tag{4}
\]

Indeed absolute continuity gives

\[
\sup_t|g^\top H_a(t)|
\le |g^\top H_a(0)|+
\int_0^\infty|g^\top\dot H_a(t)|\,dt.
\]

Minkowski's inequality and the exact Gaussian one-dimensional moment
formula bound its \(L^p\) norm by \(c_p(B+V)\). Finally use
\(\max_a z_a^p\le\sum_a z_a^p\).

There is also a dimension-free exponential-moment bound. Let

\[
D=\sum_a\left(\|H_a(0)\|+
\int_0^\infty\|\dot H_a(t)\|\,dt\right)\le m(B+V).
\]

If \(D>0\), the sum of the preceding pathwise upper bounds is
\(D\int |g^\top e|\,d\mu(e)\) for a probability measure \(\mu\)
on unit vectors: normalize each nonzero initial vector and each nonzero
velocity, and weight by its norm. Jensen's inequality, followed by the
Gaussian moment generating function, therefore gives for every \(c>0\)

\[
\mathbb E_g e^{cM}
\le\int\mathbb E_g e^{cD|g^\top e|}\,d\mu(e)
\le2e^{c^2D^2/2}.
\tag{5}
\]

When \(D=0\), all the paths vanish and \(M=0\). This proof uses no
Gaussian-process limit theorem and is uniform over all successful cavities
having the fitting bounds (1)--(2).

## 2. The probe and its differential have uniform upper bounds

In the notation of the supplied cavity derivation, write the incoming
row as \(u=U/\sqrt n\) and the readout as \(a\). Their exact driven
equations are

\[
\begin{aligned}
\dot a&=-\frac2m\sum_b r_b\phi_L(U^\top H_b),\\
\dot U&=-\frac2m\sum_b r_ba\phi_L'(U^\top H_b)H_b,
\qquad a(0)=0,\quad U(0)=g.
\end{aligned}
\tag{6}
\]

Put

\[
A=\int_0^\infty2\rho(t)\,dt\le4Y/\lambda,
\qquad K=\beta(1+B)^2,\qquad k=AK.
\]

The source estimates \(1+B\le\beta^{2L}\) and the original cap imply
\(K\le\beta^{5L}\), \(k\le4\beta^{-25L}<1/4\).
These are the same constants as in the supplied probe note.

For \(s(t)=|a(t)|+\|U(t)-g\|\), the activation growth and derivative
bounds imply, using upper derivatives when a norm is zero,

\[
\dot s(t)\le2\rho(t)K\{1+M(g)+s(t)\}.
\]

To verify the bound, use
\(|U^\top H_b|\le M+B\|U-g\|\),
\(|\phi_L(z)|\le\beta(1+|z|)\),
\(|\phi_L'|\le\beta\), and
\(m^{-1}\sum_b|r_b|\le\rho\).
Integration gives

\[
\sup_t s(t)\le(1+M)(e^k-1)\le2k(1+M).
\tag{7}
\]

Integrating the second equation of (6) once more improves the incoming
displacement to

\[
\sup_t\|U(t)-g\|\le2k^2(1+M).
\tag{8}
\]

Thus the probe has uniformly bounded moments, conditional on any successful
cavity, without asking a Gaussian vector in dimension \(n\) to lie in a
fixed-radius Euclidean ball.

For completeness the same method gives a trace-norm estimate for the
incoming-root differential. Set
\(P=D_gU\in\mathbb R^{n\times n}\),
\(q=D_ga\in\mathbb R^{1\times n}\), and define

\[
b(t)=\frac2m\sum_a r_a\phi_L'(U^\top H_a)H_a,
\qquad
C(t)=\frac2m\sum_a r_a\phi_L''(U^\top H_a)H_aH_a^\top.
\]

Here \(\|b(t)\|\le2\rho(t)K\), and the nuclear norm satisfies
\(\|C(t)\|_1\le2\rho(t)K\), because
\(\|H_aH_a^\top\|_1=\|H_a\|^2\). Differentiating (6) gives

\[
\dot q=-b^\top P,\qquad
\dot P=-bq-aCP,\qquad q(0)=0,\quad P(0)=I.
\tag{9}
\]

The norm of the vector field's Jacobian with respect to its state is bounded by
\(2\rho K(1+|a|)\). Thus, with

\[
R(g)=\exp\{k[1+2k(1+M(g))]\},
\]

one has \(\|P(t)\|_{\mathrm{op}}\le R\) and the sharper bound
\(\|q(t)\|\le kR\). Integration of (9) now yields

\[
\|P(t)-I\|_1
\le k^2R+2k^2(1+M)R
=k^2(3+2M)R.
\tag{10}
\]

All differentiated coefficients are time integrable on compact sets of
roots. The finite-time derivatives consequently converge locally uniformly,
so (10) holds for \(P(\infty)=D_gU_\infty\). Equation (5) shows that
the right side has all finite moments bounded independently of width.
In particular, only a bounded number of singular directions can differ
substantially from the identity on each fixed-confidence event.

This last statement is an upper bound on the number of poorly transported
directions. It does not prove that every singular value is bounded below.
For example, a rank-one perturbation of the identity can be singular while
its nuclear norm remains one. For any confidence for which the right side
of (10) is below \(1/2\), invertibility follows on that event; the fixed
cap does not make this particular estimate smaller than \(1/2\) at every
arbitrarily high confidence.

## 3. Why this transport control still does not imply circle separation

The actual compensated probe influence is

\[
I_\theta(g)=a_\infty(g)
 \phi_L\bigl(U_\infty(g)^\top H_\theta(\infty)\bigr)
 +j_\theta(\infty)^\top V_\infty(g),
\tag{11}
\]

where \(H_\theta=h^{(L-1)}(v(\theta))/\sqrt n\),
\(j_\theta\) is the cavity prediction gradient in mobility coordinates,
and \(V\) solves the exact multiplicity derivative equation given in the
cavity input. All training influences vanish. The supplied probe theorem
proves infinite covariance rank on each open arc when the cavity satisfies
both its fitting bounds and its two-query initialization event (13). Their
intersection has probability tending to one; successful fitting alone is
not the full hypothesis of that theorem.

Equations (4)--(10) quantify the direct term's driving transport. They do
not bound from below the distance of that term from the compensation space

\[
\operatorname{span}\{g\mapsto[V_\infty(g)]_j:\ 1\le j\le D_n\},
\]

whose dimension may grow with width. Even a perfectly invertible direct
transport does not prevent that growing space from approximating all the
fixed-complexity spatial modes.

Here is a precise warning example concerning the inference, not a
counterexample to the canonical network. Let the training angles be
\(\theta_1,\ldots,\theta_m\), and put

\[
p(\theta)=\prod_{a=1}^m[1-\cos(\theta-\theta_a)],\qquad
X(\theta)=p(\theta)\sum_{j\ge1}2^{-j}Z_j\sin(j\theta),
\]

where the \(Z_j\) are independent standard Gaussians. Subtract the
rank-\(N\) compensation
\(p(\theta)\sum_{j=1}^N2^{-j}Z_j\sin(j\theta)\), obtaining

\[
X_N(\theta)=p(\theta)\sum_{j>N}2^{-j}Z_j\sin(j\theta).
\tag{12}
\]

The direct field is fixed as \(N\) varies and the root transport can be
the identity. Both fields vanish at all training angles. At every \(N\),
the covariance of (12) has infinite rank on every open arc: distinct sine
polynomials are linearly independent on an arc, and multiplication by the
nonzero analytic function \(p\) preserves that fact. The sample paths
are analytic on every closed complex strip of width less than \(\log2\),
as follows by summing the expectations of the absolute Fourier terms.
Nevertheless,

\[
\mathbb E\sup_\theta|X_N(\theta)|
\le\|p\|_\infty\sqrt{2/\pi}\sum_{j>N}2^{-j}
=\|p\|_\infty\sqrt{2/\pi}\,2^{-N}.
\tag{13}
\]

Taking \(N=\lceil\log_2 n\rceil\) makes the remaining field
\(o(n^{-1/2})\) in probability. The compensation needs only logarithmic
rank. Thus infinite rank, uniform analytic regularity, exact vanishing at
the training points, and ideal root transport together still do not
preclude loss of all fluctuations at the required scale.

This example does not show that the canonical compensation realizes such
a projection. It isolates precisely the estimate that an argument based
only on those properties omits.

## 4. Required new implication and route status

A useful intermediate target is a width-uniform covariance lower bound
on some fixed separated arc \(J\), such as

\[
\lim_{\eta\downarrow0}\limsup_{n\to\infty}
\Pr\left\{\int_J\operatorname{Var}_g(I_\theta\mid\text{cavity})
\,d\theta<\eta\right\}=0.
\tag{14}
\]

The estimates above do not prove (14). A proof must exploit the actual
equation for \(V\), for example by bounding its ability to cancel the
direct term in a norm relative to that term's covariance. An absolute
error estimate of order \(Y^3\) is insufficient when the relevant
nonaffine covariance can be arbitrarily small and the label cap contains
no lower bound for that covariance.

Even (14) would not alone prove the requested theorem. One still needs a
width-accurate collective insertion/replacement expansion for the actual
fitted network and a small-ball estimate. The existing finite-width
multiplicity derivative does not supply either step. Nonzero variance
alone would not yield arbitrarily high-confidence separation.

| Claim | Status |
| --- | --- |
| Width-independent moments of the Gaussian training-path projections | Proved in (4)--(5) |
| Width-independent probe displacement and differential trace-norm bounds under the original cap | Proved in (7)--(10) |
| A growing compensation space can defeat infinite rank even with ideal direct transport | Proved inference counterexample (12)--(13), not a canonical counterexample |
| Canonical compensated covariance satisfies (14) | Open |
| Actual two-network fitted circle gap has scale \(n^{-1/2}\) | Open |

The route is a proved transport refinement, blocked at quantitative
observability of the compensated field. Reopening requires a new estimate
on the compensation equation or a controlled limiting fluctuation
operator; another initialization-rank argument or finite-width
nonvanishing assertion would not address the gap.
