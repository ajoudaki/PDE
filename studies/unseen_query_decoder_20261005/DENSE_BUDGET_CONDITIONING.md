# Conditioning at the dense-forward query budget

2026-10-06. Bounded author derivation in the existing unseen-query decoder
study. No experiment, Git operation, promotion, or complete fast-decoder
claim.

Two useful conditioning statements are proved here. A row law of relative
entropy \(h\) from the Gaussian prior admits a bounded-likelihood
approximation of total-variation error at most \(h/(\log M-1)\). A fixed
cutoff \(M=4\) already makes that bias \(O(h)\). Bounded weighted averages
under the prior, combined with the supplied finite-seed cubature lemma,
then integrate all prescribed bounded row tests on one sphere/time/prefix
event in \(n\operatorname{polylog}(n)=o(n^2)\) operations under the displayed
range and evaluation bounds. All samples can be regenerated from a retained
polylogarithmic seed. No pointwise likelihood bound on the original tilt
is required.

Separately, the actual first initialized-feature Gram already defeats
prior rejection and independent mean-matching proposals at the tiny scalar
noise used in the current decoder. Its posterior concentrates its collective
empirical norm to order \(\eta\), while an independent matched Gaussian
proposal has norm fluctuations of order \(n^{-1/2}\). That particular
constraint nevertheless has an exact radial sampler with constant expected
rejection cost, and a one-pass orientation sampler using \(O(n^2)\) Gaussian
draws and constant live scalar workspace. This establishes a concrete
representation repair for one actual block, not for the later nonlinear
history.

## 1. Contract and notation

The intended target retains arbitrary fixed depth \(L\ge2\), spanning
training inputs on the sphere, the original label allowance and positive
initial feature-Gram gap, Gaussian initialization, zero readout, mean-square
loss, and mobilities \((n,1,\ldots,1,n)\). The desired approximation is on
one event uniform over the sphere, all time, and the fitted endpoint.
There are no test labels, predeclared query points, dense-root access, or
scalar-training replay. Total retained information and peak query workspace
must have an absolute-polylogarithmic bound. Only query runtime is relaxed
to \(O(Ln^2+dn)\); source-dependent preprocessing remains permitted.

The existing scalar history is

\[
 C_r=\frac1n\sum_{i=1}^nF_r(Z_i;C_{<r})+\eta E_r,
 \qquad 1\le r\le P.                                      \tag{1}
\]

The \(Z_i\) have independent Gaussian law \(\mu\); the \(E_r\) are independent
standard Gaussians. The scalar noise satisfies

\[
 \log(1/\eta)\le C[\log(en)]^a
\]

for an absolute exponent, and the construction chooses it small enough
that \(n^b\eta\to0\) for each fixed \(b\). At a realized prefix \(c\),

\[
 F(z)=(F_r(z;c_{<r}))_{r\le j},\qquad |F_r|\le B.
\]

The physical-synthesis note constructs, on one event for every prefix, a
row law \(\nu\) satisfying

\[
 D(\nu\Vert\mu)\le h:=\frac{H}{\alpha n},\qquad
 H=\frac P2\log(1+B^2/\eta^2),                              \tag{2}
\]

and matching the retained moments within \(2\eta T\). Its density is

\[
 r(z):=\frac{d\nu}{d\mu}(z)
       =\exp\{\lambda^TF(z)-\psi\},\qquad
 \psi=\log\int e^{\lambda^TF(z)}\,\mu(dz),\qquad
 \|\lambda\|_1\le\frac{h}{\eta T}.                         \tag{3}
\]

The law \(\nu\) is a calibrated **one-row law**. It is not the conditional
joint law of all \(n\) rows in (1). That distinction is essential in
Sections 5–8.

## 2. Entropy controls the discarded likelihood mass

The following lemma does not require the exponential representation (3).
Let \(\nu\ll\mu\) be probability laws with density \(r\) and
\(D(\nu\Vert\mu)\le h<\infty\). Fix \(M>e\), and define

\[
 w_M=\min(r,M),\quad Z_M=\int w_M\,d\mu,
 \quad e_M=1-Z_M=\int(r-M)_+\,d\mu,
 \quad d\nu_M=\frac{w_M}{Z_M}\,d\mu.                       \tag{4}
\]

Then

\[
 \nu\{r>M\}\le\frac{h}{\log M-1},\qquad
 e_M\le\frac{h}{\log M-1},\qquad
 \|\nu_M-\nu\|_{\rm TV}\le e_M.                           \tag{5}
\]

Here total variation is the supremum over measurable events. To prove
the first inequality, use \(r\log r-r+1\ge0\) for \(r\ge0\), with its
continuous value at zero. Its integral is the relative entropy, because
\(\int r\,d\mu=1\). On \(r>M\),

\[
 r\log r-r+1\ge r(\log M-1).
\]

Integrating this inequality on that set proves the first bound, without
an additive \(\log2\) or a square-root loss. The second follows from
\((r-M)_+\le r\mathbf1_{\{r>M\}}\). If \(e_M>0\), the remaining
nonnegative density gives a probability law \(\rho\) such that

\[
 \nu=Z_M\nu_M+e_M\rho.
\]

Subtracting \(\nu_M\) proves the total-variation bound; \(e_M=0\) is
immediate. Consequently every measurable \(|G|\le B_G\) obeys

\[
 \left|\int G\,d\nu_M-\int G\,d\nu\right|
      \le \frac{2B_Gh}{\log M-1}.                          \tag{6}
\]

These inequalities are deterministic statements about measures. Thus the
same all-prefix entropy event from (2) supports (5)–(6) for every prefix
and every bounded row test selected using that prefix and a late query.
This simultaneous bias bound is distinct from the sampling guarantee
below.

## 3. Streaming sampling and integration of the clipped row law

Draw \(Z\sim\mu\) and \(U\) uniform on \([0,1]\), independently, and
accept \(Z\) when

\[
 U\le w_M(Z)/M.                                           \tag{7}
\]

The acceptance probability is \(Z_M/M\), and the accepted law is exactly
\(\nu_M\): integrate the acceptance probability over any measurable set
and divide by its total. Independent repetitions give independent accepted
rows. The sampler never evaluates \(r\) before clipping; it can compute

\[
 w_M(z)=\exp\{\min(\lambda^TF(z)-\psi,\log M)\}.            \tag{8}
\]

Thus enormous original likelihood ratios need not be formed.

Assume \(h/(\log M-1)\le1/2\), so that the success probability in (7)
is at least \(1/(2M)\). To integrate \(|G|\le B_G\) with random error
at most \(\varepsilon\) and failure at most \(\delta/2\), it suffices to
take

\[
 K\ge\frac{2B_G^2}{\varepsilon^2}\log\frac4\delta           \tag{9}
\]

accepted rows and average \(G\). For completeness, a variable in an
interval of length \(2B_G\) has centered log moment-generating function
at most \(s^2B_G^2/2\). Differentiate that log moment-generating function
twice: the second derivative is a variance of a law supported in the same
interval and is at most \(B_G^2\). Integrating twice proves the bound.
Independence, exponential Markov, and optimization over \(s>0\) give
the two-sided failure bound \(2e^{-K\varepsilon^2/(2B_G^2)}\).

A deterministic proposal cap of

\[
 N=\left\lceil16M\left(K+\log\frac2\delta\right)\right\rceil \tag{10}
\]

loses at most another \(\delta/2\) by returning a failure flag if it has
not obtained \(K\) accepts. Indeed the number of accepts is binomial
with mean \(\mu_N\ge N/(2M)\ge8(K+\log(2/\delta))\). For a sum of
independent Bernoulli variables of mean \(\mu_N\), exponential Markov
at parameter \(\log2\), and \(1-u\le e^{-u}\), give

\[
 \Pr\{S_N\le\mu_N/2\}
 \le \exp[-(1-\log2)\mu_N/2]\le e^{-\mu_N/8}.
\]

Since \(K\le\mu_N/2\), (10) gives the claimed probability. The first
\(K\) accepted rows of the underlying unlimited stream have the desired
iid law; the capped procedure agrees with them whenever it succeeds.
Combining this event with (9) proves

\[
 \left|\widehat I_G-\int G\,d\nu\right|
 \le\varepsilon+\frac{2B_Gh}{\log M-1}                    \tag{11}
\]

with probability at least \(1-\delta\), for each fixed current prefix
and requested row test. Multiple fixed tests can share the accepted rows,
with one accumulator per test and a union bound when desired.

Only one proposed row, its row-circuit workspace, a few counters, and
the running integral need be live. A row has \(d+O(R)\) coordinates,
and the source supplies an absolute-polylogarithmic workspace bound for
its evaluation. No \(n\)-row sample panel is stored.

Suppose in addition that one evaluation of the fixed-prefix row circuit
and \(G\) costs \(Q_n=\operatorname{polylog}(n)\) arithmetic operations.
With \(M=n^\kappa\), \(0<\kappa<1\), the proposal work is

\[
 O\!\left(n^\kappa B_G^2\varepsilon^{-2}
                 Q_n\log(1/\delta)\right).                 \tag{12}
\]

If \(B_G\), \(Q_n\), \(1/(\sqrt n\,\varepsilon)\), and the requested
confidence factor are polylogarithmic, (12) is
\(n^{1+\kappa}\operatorname{polylog}(n)=o(n^2)\). The clipping bias
is \(O(B_GH/(n\log n))\), by (2). This is a concrete bounded-row
integration result at the relaxed budget.

The extra assumption on \(Q_n\) is visible: a polynomial-space row
evaluator is not automatically a polynomial-time row evaluator. In
particular, the source's very long contraction-series implementations of
small matrix functions do not, by their workspace bound alone, verify
this assumption. Likewise its global row bounds permit
\(B_G=\exp[\operatorname{polylog}(n)]\); those bounds alone do not verify
the bounded-row cost in (12).

### 3.1 A fixed cutoff and one retained seed are enough for row integration

For the root-width numerical target it is unnecessary to let \(M\) grow.
Take \(M=4\). Equation (5) gives

\[
 e_4\le\frac{h}{\log4-1},\qquad Z_4\ge\frac12              \tag{12a}
\]

for sufficiently large width, because \(h=H/(\alpha n)\to0\).
The bias in (6) is then \(O(B_Gh)\), without a factor \(n^\kappa\)
in the runtime. A deterministic number of weighted prior samples also
avoids query-dependent rejection stopping times.

Here is a precise application of Section 2 of
[`EFFICIENT_QUERY_RANDOMIZED_INTEGRATION.md`](EFFICIENT_QUERY_RANDOMIZED_INTEGRATION.md).
Condition on a complete training tape, including its finitely many current
tilts and cached normalizers, but not on a new independent cubature seed.
Let \(G_\ell(z;\theta)\), \(1\le\ell\le J_0\), be its finite families
of row tests, indexed by the applicable prefix, instruction and time patch.
The parameter \(\theta\) contains a sphere input and the bounded local time
coordinate; additional bounded coordinates such as a test threshold may
be included. Assume uniformly

\[
 |G_\ell|\le B_G,
 \quad\operatorname{Lip}_z(G_\ell)\le L_G,
 \quad\operatorname{Lip}_\theta(G_\ell)\le L_\theta,
 \quad B_G\ge1.                                           \tag{12b}
\]

Different indices may use different current-prefix weights \(w_4\).
Those weights depend on the tape and row but not on \(\theta\) or on
the cubature seed. Include two bounded test families per relevant index:

\[
             w_4(z),\qquad w_4(z)G_\ell(z;\theta)/B_G.      \tag{12c}
\]

Their range bound is four. If every coordinate of \(F\) is
\(L_F\)-Lipschitz in \(z\), their row Lipschitz constants are at most

\[
 4\|\lambda\|_1L_F,
 \qquad 4L_G/B_G+4\|\lambda\|_1L_F,                        \tag{12d}
\]

respectively: \(u\mapsto e^{\min(u,\log4)}\) is globally
four-Lipschitz, and the product rule for differences gives the second
bound. Their parameter Lipschitz constants are respectively zero and
\(4L_\theta/B_G\). The logarithms of (12d) are polylogarithmic by
(3) and the source bounds. They need not be polynomial in \(n\).

The cited cubature lemma states the following precise form. For finitely
many functions of Gaussian rows bounded by \(B_0\), with uniform row and
parameter Lipschitz constants, a proof-only parameter net of size
\(M_\Theta\) and an even integer \(k\ge2\) satisfying
\(2J_0M_\Theta4^{-k}\le\beta\) suffice. With
\(Q\ge256kB_0^2u^{-2}\), there is a retained seed polynomial in
row dimension, \(k\), \(\log Q\), and the logarithmic range, Lipschitz,
and precision bounds. Its sequentially regenerated row averages have
error at most \(u\) for every function and every parameter on one seed
event of probability at least \(1-\beta\). The construction uses clipped
finite Gaussian quantiles and degree-\((k-1)\) polynomials over a retained
finite binary field; the Vandermonde identity supplies \(k\)-wise
independence. Its even-moment bound and proof-only net give the stated
simultaneous event. The node list and the net are not stored, and finite
Gaussian generation has polynomial cost in its logarithmic parameters.

Apply that lemma to (12c), including the denominator as another family,
with \(B_0=4\) and

\[
 u=\frac{\varepsilon}{8B_G}\le\frac14,
 \qquad Q=O(k B_G^2\varepsilon^{-2}).                       \tag{12e}
\]

It produces, from the same finite seed, approximations \(\widehat A\)
and \(\widehat Z\) to \(A=\int w_4G_\ell/B_G\,d\mu\) and
\(Z=\int w_4\,d\mu\), with both errors at most \(u\), simultaneously
over every index and parameter. Since \(Z\ge1/2\),
\(\widehat Z\ge1/4\) and \(|A|\le Z\). Therefore

\[
 \left|B_G\frac{\widehat A}{\widehat Z}
                  -\int G_\ell\,d\nu_4\right|
 \le B_G\left[4u+4u\frac{|A|}{Z}\right]
 \le8B_Gu=\varepsilon.                                    \tag{12f}
\]

Combining (6), (12a) and (12f) proves, on one seed event,

\[
 \sup_{\ell,\theta}
 \left|B_G\frac{\widehat A_\ell(\theta)}{\widehat Z_\ell}
                   -\int G_\ell(\cdot;\theta)\,d\nu\right|
 \le\varepsilon+\frac{2B_Gh}{\log4-1}.                    \tag{12g}
\]

Averaging the conditional seed guarantee over the training tape produces
one joint event. Given the seed, the row-integral algorithm is deterministic
and repeatable, including for queries chosen after earlier answers. Thus
this numerical row-integration lemma does have the required uniformity
structure; it still has no identification with the collective query
posterior.

For the sphere and a fixed number of bounded interval coordinates, the
cited net bound makes \(k\) a polynomial in the logarithmic parameter
Lipschitz bound, precision, finite prefix count and confidence. Its degree
is absolute; \(d\) and fixed structural quantities multiply the constants.
The seed, counters, one row, two accumulators and row-evaluator workspace
therefore fit the absolute-polylogarithmic storage budget.

Let the row evaluation and finite-seed generation cost be \(Q_n\) per
sample. If \(Q_n\), \(B_G\), and \(1/(\sqrt n\varepsilon)\) are
polylogarithmic, total query work in (12e) is
\(n\operatorname{polylog}(n)=o(n^2)\), even after a polylogarithmic
number of moment integrals. More generally a proved multistep propagation
factor \(A_n\) requires replacing \(\varepsilon\) in (12e) by
\(\varepsilon/A_n\), hence \(Q=O(kB_G^2A_n^2\varepsilon^{-2})\).
The accumulated clipping bias must also be bounded by the corresponding
physical propagation argument. The existing inverse-noise bounds do not
provide a useful \(A_n\).

Clipping does not preserve the defining moment calibration to its original
tiny tolerance. Applied to a retained coordinate \(F_r\), (6) permits an
additional \(O(Bh)\) moment error, which may be much larger than \(\eta\).
Consequently any use of the calibrated law inside an inverse-noise
coefficient still needs exact reuse of retained moment identities or a
proved physical estimate tolerant of this weak error. The clipped law
must not silently replace \(\nu\) in an argument requiring
\(\int F_r\,d\nu=c_r+O(\eta)\).

The exact-argument method in the supplied cubature note covers a recursive
integral program when its deterministic exact arguments are seed-independent
and its empirical recursion has a proved pointwise stability bound.
It does not justify silently using arbitrary seed-dependent tests in
(12g). Current cached tilt parameters must likewise be acquired independently
of this seed, or a separate uniformity argument is needed.

## 4. Cached normalizers and precision

The lemma allows \(\lambda\) and \(\psi\) in (3) to have been computed
during the current-state acquisition. It neither computes the constrained
tilt cheaply nor treats its normalizer as a free oracle. A proof of a new
decoder must specify how those current values become part of its counted
state. Precomputing and storing an arbitrary table of future responses
is not authorized by this observation.

For a supplied ideal current prefix, suppose the evaluated log density
\(\widehat\ell(z)\) satisfies

\[
 |\widehat\ell(z)-[\lambda^TF(z)-\psi]|\le a
                  \quad\hbox{for every }z.                  \tag{13}
\]

Since \(u\mapsto\min(u,\log M)\) is one-Lipschitz, the implemented
weights \(\widehat w(z)=\exp(\min(\widehat\ell(z),\log M))\)
obey

\[
 e^{-a}w_M\le\widehat w\le e^aw_M.
\]

Their normalization obeys the same relative inequalities. If
\(d\widehat\nu_M=\widehat w\,d\mu/\int\widehat w\,d\mu\), then

\[
 e^{-2a}\le\frac{d\widehat\nu_M}{d\nu_M}\le e^{2a},\qquad
 \|\widehat\nu_M-\nu_M\|_{\rm TV}\le e^{2a}-1.             \tag{14}
\]

Consequently the additional integral error is at most
\(2B_G(e^{2a}-1)\), while the acceptance probability remains at least
\(e^{-a}(1-e_M)/M\). Changing the absolute constant in (10) covers this
loss for \(a\le1\).

For example, (13) follows if

\[
 B\|\widehat\lambda-\lambda\|_1\le a/3,\quad
 |\widehat\psi-\psi|\le a/3,\quad
 |\widehat\lambda^T(\widehat F(z)-F(z))|\le a/3.             \tag{15}
\]

The last condition can be imposed by uniformly evaluating each row
coordinate to error \(a/[3(1+\|\widehat\lambda\|_1)]\), with arithmetic
error allocated within the same budget. Because

\[
 \|\lambda\|_1\le h/(\eta T),\qquad
 |\psi|\le B\|\lambda\|_1,
\]

the bits per cached multiplier and normalizer are bounded by a fixed
polynomial in

\[
 \log(1+B),\quad \log(1+h/(\eta T)),\quad
 \log(1+j),\quad \log(1/a).                                \tag{16}
\]

Their count is \(j+1\), hence absolute-polylogarithmic under the source
bounds. For \(a=O(\varepsilon/B_G)\), (14) fits the integration budget.
The same logarithmic quantities control the required accuracy of each
row operation, subject to the source's counted numerical interfaces.

This is a precision bound at a fixed ideal prefix. It does not prove
that a rounded retained prefix has nearby optimal multipliers, nor that
recomputing a tilt for a nearby prefix preserves the required physical
law. Those are distinct questions. Also, arbitrarily tiny positive weights
may be cut off numerically: a uniform weight error \(\zeta\) changes
the normalizer by at most \(\zeta\) and a normalized bounded integral
by \(O(B_G\zeta)\) when \(Z_M\ge1/2\). Thus the implementation need not
represent weights below its assigned absolute integration tolerance.

## 5. An actual nonlinear network already has a thin collective constraint

Take an admissible member of the original class with \(L=2\), \(d=m=1\),
training input \(x_1=1\), first activation \(\phi_1(z)=z\), and second
activation \(\phi_2(z)=\tanh z\). Choose a nonzero label satisfying the
inherited small-label condition. Both activations have bounded real
derivative and are analytic on a fixed strip; unbounded values of the
first activation are expressly allowed.

The initialized first feature vector is \(z=(Z_1,\ldots,Z_n)\), with
independent standard Gaussian entries. Define

\[
 S=\frac1n\sum_iZ_i^2.                                    \tag{17}
\]

Conditional on \(z\), its initialized next preactivation \(W_0z\)
has independent \(N(0,S)\) entries. Since \(S\to1\) in probability,
the population feature gap for the sole datum is

\[
 \gamma=\mathbb E[\tanh(G)^2]>0,
 \qquad G\sim N(0,1).                                     \tag{18}
\]

One may verify the finite-width convergence directly: \(\operatorname{Var}
S=2/n\); conditional on \(S\), the bounded feature squares have average
variance at most \(1/n\); and their common mean
\(\mathbb E\tanh(\sqrt S G)^2\) tends to (18) by bounded convergence.
The data span their one-dimensional space.

This example does retain hidden feature learning. In the normalization
\(f=n^{-1}w^T\tanh(Wz)\) and loss \((f-y)^2\), zero initial readout gives

\[
 \dot w(0)=2y\tanh(W_0z),\qquad
 \ddot W(0)=\frac{4y^2}{n}
 [\tanh(W_0z)\odot\tanh'(W_0z)]z^T\ne0                   \tag{19}
\]

almost surely. The hidden-matrix mobility is one, as stipulated. Thus
the obstruction below occurs before an actual nonlinear learning
trajectory, rather than in a substituted all-linear network.

The supplied physical bridge says that the first matrix is represented
by its Gaussian row coordinates and that the next initialized action
uses the first feature. The exact two-orientation representation,
equations (15), (21), and (30), requires its norm \(d=\|z\|^2/n=S\)
before that action: with empty old history, its observed answer is
\(\sqrt{S+\sigma^2}\,g\). The scalar-perturbed program therefore
contains a first-feature norm observation of the form

\[
                       C=S+\eta E.                        \tag{20}
\]

Root and RMS caps give a capped version of this statement. They are
inactive on the good initial range; Section 8 quantifies their effect.
No later history-Gram conditioning assumption is used here.

## 6. Prior rejection and an iid matched tilt miss the collective law

For \(n\ge4\), the density of (17) is

\[
 p_n(s)=\frac{(n/2)^{n/2}}{\Gamma(n/2)}
          s^{n/2-1}e^{-ns/2}\mathbf1_{s>0},
 \qquad \sup_s p_n(s)\le C\sqrt n.                         \tag{21}
\]

The density follows by polar coordinates in the standard Gaussian
integral. Here is an elementary maximum bound without an asymptotic
formula for \(\Gamma\). The mode is \(s_0=(n-2)/n\ge1/2\). For
\(s=s_0(1+u)\),

\[
 \log\frac{p_n(s)}{p_n(s_0)}
        =(n/2-1)[\log(1+u)-u].
\]

For \(|u|\le1/2\), \(\log(1+u)\ge u-u^2\). This inequality follows
by differentiating the difference: its derivative is
\(u(1+2u)/(1+u)\), and its value at zero is zero. On
\(|s-s_0|\le s_0/\sqrt n\), the log ratio is therefore at least
\(-1/2\). Integrating over that interval gives
\(1\ge e^{-1/2}p_n(s_0)/\sqrt n\), proving (21).

The elementary prior-likelihood rejection rule for (20) accepts with
probability

\[
 A(c)=\int e^{-(c-s)^2/(2\eta^2)}p_n(s)\,ds
                    \le C\eta\sqrt n.                    \tag{22}
\]

The factors from other retained scalar observations are at most one
under the same Gaussian envelope. Thus (22) also bounds rejection from
the complete product Gaussian row prior using the full-prefix
likelihood. Even granting unit cost to a complete proposal, \(O(n^2)\)
proposals have probability at most \(C\eta n^{5/2}\to0\) of an accept.
This is an explicit actual-program rejection obstruction.

There is a stronger collective statement. For \(c\in[1/2,2]\) and
\(n\eta\le1/8\), Section 7 proves

\[
 \mathbb E[(S-c)^2\mid C=c]\le C\eta^2.                    \tag{23}
\]

The Gaussian one-row tilt \(N(0,c)\) exactly matches the mean norm,
but its product law has

\[
 \mathbb E S=c,\qquad \operatorname{Var}S=2c^2/n,\qquad
 \sup_s p_{n,c}(s)\le C\sqrt n/c.                          \tag{24}
\]

For any \(T>0\), the true posterior gives the slab
\(|S-c|\le T\eta\) mass at least \(1-C/T^2\), whereas (24) gives it
mass at most \(CT\eta\sqrt n\), uniformly for \(c\in[1/2,2]\).
Taking \(T=(\eta\sqrt n)^{-1/2}\) shows that the total variation
between the full posterior and this iid mean-matching product law tends
to one. Mean matching therefore does not recover collective conditioning.

This example is compatible with small one-row relative entropy. If
\(|c-1|\le A/\sqrt n\), then

\[
 D(N(0,c)\Vert N(0,1))
        =\tfrac12(c-1-\log c)=O(A^2/n).                    \tag{25}
\]

For this formula, take the expectation of the log ratio of the two
Gaussian densities. The bound follows by integrating the derivative
\(1-1/c\) between (1) and \(c\), on \(c\in[1/2,2]\). Thus an
excellent low-entropy row proposal can remain almost mutually singular
from the relevant joint posterior at the collective scale.

Even optimized exact rejection from the product proposal has the small
success bound. If its success probability is \(a_c\) and its accepted
law is the target posterior, every event \(D\) satisfies
\(a_c\Pr(D\mid C=c)\le Q(D)\), where \(Q\) is the proposal law.
Choose a fixed \(T\) making the target slab mass at least \(1/2\),
and use (24). This gives \(a_c\le C\eta\sqrt n\). The same argument
applies to the product prior. It does not apply to proposals which
already enforce the shared radial constraint.

## 7. An exact radial repair, including counted one-pass orientation

The posterior constraint in (20) has a special exact solution. Fix
\(c>0\), write \(k=n/2\), and put

\[
 a=\eta\left(\frac{k-1}{c}-\frac n2\right).
\]

Draw \(U\sim N(a,1)\), set \(s=c+\eta U\), and reject when \(s\le0\).
Otherwise accept with probability

\[
 A_c(U)=\exp\left\{(k-1)
       \left[\log(s/c)-(s/c-1)\right]\right\}.              \tag{26}
\]

This lies in \([0,1]\), because \(\log v\le v-1\) for \(v>0\).
The accepted \(s\) has exactly the law \(S\mid C=c\). Indeed

\[
 \frac{p_n(c+\eta u)}{p_n(c)}
   =\exp\{a u+(k-1)[\log(1+\eta u/c)-\eta u/c]\},
\]

and completing the square in
\(e^{-u^2/2+a u}=e^{a^2/2}e^{-(u-a)^2/2}\) identifies the posterior
density with the proposal density times (26), up to its normalization.
The transformation samples the narrow coordinate at its own scale
\(u=(s-c)/\eta\); it never searches for that coordinate in a diffuse
proposal.

For \(c\in[1/2,2]\) and \(n\eta\le1/8\), one has \(|a|\le1/16\).
On \(|u|\le2\), \(|\eta u/c|\le4\eta\le1/2\), and the inequality
used in (21) gives

\[
 A_c(u)\ge e^{-8n\eta^2}.
\]

The \(N(a,1)\) probability of \(|U|\le2\) is bounded below by an
absolute positive constant, for example by integrating its density on
\([-1,1]\). Hence the total acceptance probability is at least some
absolute \(a_0>0\). Expected proposal count is at most \(a_0^{-1}\),
independent of \(\eta^{-1}\). Dividing the proposal second moment by
this same acceptance lower bound gives

\[
 \mathbb E[U^2\mid\hbox{accept}]
      \le(1+a^2)/a_0,
\]

which proves (23). Capping the number of attempts at \(J\) loses at
most \((1-a_0)^J\); that is a per-call randomized failure statement.

Conditional on \(S=s\), the row vector is uniform on the sphere of
radius \(\sqrt{ns}\), independently of (20). Its coordinates can be
emitted without storing an \(n\)-vector. Maintain the remaining squared
radius \(R^2\), initially \(ns\). At remaining dimension \(q\ge2\),
draw \(q\) fresh independent standard Gaussians, retain the first \(G_1\)
and the sum \(V=\sum_{r=1}^qG_r^2\), emit

\[
 z_i=R G_1/\sqrt V,qquad R^2\leftarrow R^2-z_i^2.           \tag{27}
\]

At the last coordinate emit \(R\) times an independent random sign.
Rotational invariance of a Gaussian vector shows that \(G_1/\sqrt V\)
has the first-coordinate law of a uniform unit sphere in dimension \(q\).
Conditional on that first coordinate, rotations of the remaining
coordinates preserve the law and give the uniform sphere of the residual
radius. Applying this observation inductively proves that (27) emits the
correct joint spherical law.

The algorithm draws \(n+(n-1)+\cdots+2=O(n^2)\) Gaussian scalars and
uses only \(R^2\), \(G_1\), \(V\), counters, and the current output
coordinate. Any fixed list of row integrands can be accumulated during
this pass. If its size and row-evaluation cost are polylogarithmic, its
additional \(n\operatorname{polylog}(n)\) work is \(o(n^2)\), and
the accumulators fit the same polylogarithmic workspace.

This is an exact mathematical randomized sampler in the scalar-arithmetic
model with fresh Gaussian draws. A full bit-runtime claim additionally
requires implementing and budgeting those draws, logarithms, exponentials,
acceptance decisions, and roundoff; no exact continuous sampler is being
identified with finite-bit output. More significantly, (27) is a
**one-pass** stream. It does not supply a short seed from which the same
exact \(n\) coordinates can be replayed. The later passive-query scalar
updates choose new row tests after previous empirical moments are known.
They cannot consume (27) repeatedly as though its discarded coordinates
had been retained. Resampling conditionally on all those later moments
would require a new conditioning theorem.

## 8. Initial caps and why the whole prefix is still unresolved

For the displayed witness, choose the allowed initial RMS cap strictly
above the typical unit RMS and root-coordinate caps at least \(b\sqrt n\)
for fixed \(b>0\), as in the supplied bridge. The event that any such cap
changes the initial norm computation has probability

\[
 q_n\le Cn e^{-c_0 n}.                                    \tag{28}
\]

The coordinate estimate is the elementary Gaussian tail and a union
bound. For an RMS radius \(B_0>1\), exponential Markov gives

\[
 \Pr(S>B_0^2)
 \le e^{-tnB_0^2}(1-2t)^{-n/2}
 \le e^{-c_0 n}
\]

by choosing a sufficiently small fixed \(t>0\); the logarithmic exponent
has negative derivative \(1-B_0^2\) at zero. Enlarge the cap if necessary
to keep its plateau outside the central range considered below.

For the capped scalar likelihood, the prior acceptance bound is at most
\(C\eta\sqrt n+q_n\), since capped and uncapped integrands coincide
off the event in (28). It still defeats \(O(n^2)\) prior proposals.

The ideal radial posterior also describes the capped initial block up
to vanishing total variation on typical observations. Fix \(A<\infty\)
and \(|c-1|\le A/\sqrt n\). Then

\[
 p_C(c)\ge c_A\sqrt n                                     \tag{29}
\]

for sufficiently large \(n\). One proof uses Chebyshev's inequality to
put at least half the \(S\)-mass in an interval of length \(4/\sqrt n\),
so that its mode has density at least \(\sqrt n/8\). The log-density
ratio in (21) then bounds \(p_n(c-\eta u)\) below by a positive
\(A\)-dependent multiple of \(\sqrt n\) for \(|u|\le1\). Integrating
against the standard Gaussian density in the convolution for \(C\)
proves (29).

The likelihood density of any scalar observation is at most
\((\sqrt{2\pi}\eta)^{-1}\). Thus its joint mass-density contributed
by the bad cap event is at most \(q_n/(\sqrt{2\pi}\eta)\), for
either program. The two programs have the same unnormalized law off
that event. By (29), normalizing their conditional laws gives

\[
 \|\pi^{\rm capped}_c-\pi^{\rm uncapped}_c\|_{\rm TV}
           \le C_A\frac{q_n}{\eta\sqrt n}=o(1).            \tag{30}
\]

Indeed the density difference is at most twice the displayed bad-event
mass-density, and the capped denominator is eventually at least one
half of (29). Since \(\log(1/\eta)=\operatorname{polylog}(n)\), the
right side tends to zero. Taking \(A\) large gives any fixed desired
high probability, because \(\operatorname{Var}C=2/n+\eta^2\).
Equation (30) is a controlled cap correction, not a claim that the
uncapped radial sampler exactly samples the original capped full prefix.

After the norm block, the actual passive and training row responses
include nonlinear activation products, opposite-orientation moments,
and adaptive cross moments. Fixing a scalar history makes the posterior
density proportional to

\[
 \prod_{r\le j}
 \exp\left[-\frac{\left(c_r-n^{-1}\sum_i
                         F_r(Z_i;c_{<r})\right)^2}{2\eta^2}\right]
\]

relative to the Gaussian product prior. There is no proved simultaneous
radial or other low-dimensional change of variables which isolates all
these thin constraints, with a controlled Jacobian and a streaming
conditional law for their remaining coordinates. The source imposes no
gap on their empirical history Grams; assuming such a gap would alter
the theorem.

Even the first norm posterior is not log-concave in the original row
coordinates: its log density is

\[
 -\frac12\|z\|^2-\frac{(c-\|z\|^2/n)^2}{2\eta^2}
                +\hbox{constant},
\]

whose Hessian at zero is
\((-1+2c/(n\eta^2))I\), positive for the central observations and tiny
noise used here. This does not obstruct the radial sampler; it excludes
an unverified appeal to joint log-concavity as a substitute for it.

## 9. Exact claim boundaries

| Claim | Status | Scope |
|---|---|---|
| Relative entropy controls discarded likelihood mass by (5) | Proved | Every finite-entropy row law |
| Clipped calibrated-row integration has (11)–(12) | Proved under displayed evaluation/range bounds | Randomized fixed-row-test guarantee |
| Constant-clipped weighted cubature has one event, (12g) | Proved under displayed range, regularity and evaluation bounds | Repeatable current-prefix row integrals, all sphere/time parameters |
| Cached tilt and normalizer precision is polylogarithmic | Proved | Fixed ideal prefix and counted primitive interface |
| Initial feature norm defeats diffuse exact rejection | Proved | Actual admissible nonlinear witness, with cap correction |
| Matching the norm mean recovers its collective posterior | Falsified | Product Gaussian tilt, equations (23)–(25) |
| Initial radial conditioning avoids inverse-noise cost | Proved | Uncapped block; controlled capped correction |
| Its orientation can be streamed in \(O(n^2)\) scalar work | Proved | Fresh one-pass randomness, not repeated access |
| Full-prefix posterior can be sampled/integrated within the budget | Open | Later nonlinear collective constraints remain |
| Deterministic one-event whole-sphere decoder follows | Open | Numerical row integration is uniform; collective physical identification remains missing |

The clipping error in (11) or (12g) is typically polylogarithmic over \(n\), and
its sampling error may be of root-width size. It is therefore not
automatically compatible with the exact existing remainder \(1/n\) in
\(2b_n+1/n\). A subsequent proof must allocate the original constants
and errors explicitly, or state a changed conclusion. Also, ordinary
sampling at a fixed query does not furnish one deterministic query
function with a simultaneous sphere/time guarantee. No per-query
success statement here is promoted to that conclusion. Section 3.1 does
resolve the finite-seed numerical uniformity problem for the displayed
row-integral families; the missing collective-to-row physical comparison
prevents its use as a full decoder theorem.

The usable advance is narrower: the unbounded likelihood of the
minimum-entropy **row** tilt is no longer itself a reason to expect
superquadratic integration time for bounded row tests. The actual
collective conditioning remains a separate, demonstrably nontrivial
step. For one real constraint its radial representation removes the
cost, suggesting the precise kind of identity-preserving representation
needed from a later neural-specific argument.

## 10. Scope and process record

Initial complete scientific inputs were exactly
`CURRENT_STATE_DECODER_CANDIDATE.md`,
`NOISY_TWO_ORIENTATION_TRANSCRIPT.md`,
`NOISY_SCALAR_HISTORY_ACQUISITION.md`,
`PHYSICAL_NOISY_PROGRAM_BRIDGE.md`,
`CONDITIONAL_PREFIX_CENTER.md`,
`EFFICIENT_QUERY_INFORMATION.md`, and
`EFFICIENT_QUERY_PHYSICAL_SYNTHESIS.md`.
The supervisor subsequently requested the capped-tilt lemma and the
nonlinear witness above, and explicitly authorized the additional complete
input `EFFICIENT_QUERY_RANDOMIZED_INTEGRATION.md` for the numerical
integration lemma in Section 3.1. No other scientific file was read.

The research and rigorous-proof skills and the required research
contract, evidence, and adversarial-audit references were read. The
custom canonical-notation skill remained unreadable with `Permission
denied`; the supervisor's supplied-notation fallback was used. Only
this assigned file was written. There were no experiments, Git-index
operations, other-study reads, or claims of independent review.
