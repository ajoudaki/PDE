# Bounded negative route for the required memory order

2026-10-03. Independent scoped theoretical attempt. The candidate analysis was
frozen before accessing any sibling route. No experiments, other studies,
archived book material, Git operations, or manuscript edits were used.

**Outcome:** no admissible evolved-prediction lower bound was obtained. In
particular, this attempt does not prove that strict root-width accuracy requires
an order larger than (n^{1/4}), and does not rule out a sublinear order. It
does identify two concrete reasons why a slow normalized-residual mode is not,
by itself, the requested obstruction: its forward response has an extra clock
integral, and a slow mode seeded at root-width amplitude takes over only after
the remaining clock mass has become smaller than root width.

The exact calculations below concern specified histories or a frozen
two-mode residual equation. They are diagnostics of the proposed negative
mechanism, not replacements for the actual nonlinear closure.

## 1. Contract and scientific inputs

The target systems are the current manuscript's dense gradient flow and
autonomous Legendre closure, at the same width (n), with shared independent
Gaussian initialized matrices, exactly zero initialized readout, tanh hidden
activations, arbitrary fixed depth, and the original clock

\[
\rho(t)^2=\frac1m\sum_{a=1}^m(f(t,x_a)-y_a)^2,
\qquad \dot\tau=\rho,\qquad \tau(0)=1.
\]

Training inputs (x_a/\sqrt d) lie on a fixed finite sphere dataset, and the
fixed labels respect all duplicate and antipodal identities. Their RMS size

\[
Y=\left(\frac1m\sum_a y_a^2\right)^{1/2}
\]

is in the manuscript's order-independent fitting regime. Geometry, labels,
depth, activation, and the query law may not depend on width. The observable is

\[
\mathcal E_\mu(\widehat f_{n,q},f_{n,D})
=\left(\int\sup_{t\ge0}
 |\widehat f_{n,q}(t,x)-f_{n,D}(t,x)|^2\,d\mu(x)\right)^{1/2}.
\tag{1}
\]

A negative answer needs failure of tightness of
\(\sqrt n\mathcal E_\mu\) for the proposed order schedule, with probability
bounded away from zero. A deterministic unfavorable initialization whose
Gaussian probability vanishes is insufficient. A lower bound on a stored
matrix, an independent prescribed history, or a projection tail is also
insufficient without its causal transfer to (1).

Inputs read were the relevant complete definitions and proofs in
`paper/main.tex`, `paper/results.tex`, `paper/proof_alltime.tex`
(initialization, projection, fitting, and speed sections), and
`paper/proof_tracking.tex`; `docs/index.qmd` and `docs/notation.qmd`; and the
assigned own-study `GENERAL_DATA_ASSESSMENT.md`, `DATA_QUOTIENT_CLOCK.md`,
`DATA_QUOTIENT_CHECK.md`, `PERSISTENT_CLOCK_ENDPOINT_DIAGNOSTIC.md`, and
`NEGATIVE_RATE_ASSESSMENT.md`. The required canonical-notation,
research-contract, adversarial-audit, and rigorous-math instructions were
applied. The manuscript's symbol (w) is its stored readout
((W^{(L+1)}) in the book notation).

The compatible quotient has zero irreducible residual. The common fitting
event therefore gives, for both actual trajectories separately,

\[
\rho(t)\le Ye^{-\kappa t},\qquad
\tau_\infty=1+\int_0^\infty\rho(t)dt<\infty,
\qquad
\frac{\|\dot h_a^{(\ell)}(t)\|_2}{\sqrt n}
\le CY\rho(t).
\tag{2}
\]

Consequently, with (s=\tau_\infty-\tau(t)),

\[
\frac{\|h_a^{(\ell)}(\infty)-h_a^{(\ell)}(t)\|_2}{\sqrt n}
\le CYs.
\tag{3}
\]

This follows by integrating the last bound in (2). The constants in (2)--(3)
are independent of width and order. The persistent-clock final-feature
identity from the assigned quotient note assumes positive irreducible
residual and (\tau_\infty=\infty); it cannot be used here.

## 2. A restriction already imposed by the manuscript

The manuscript gives, on events of probability tending to one,

\[
\mathcal E_\mu(\widehat f_{n,q},f_{n,D})
\le C_\mu q^{-2}\exp\{K\sqrt{\log(e+q)}\}+b_n,
\qquad b_n\xrightarrow{\Pr}0,
\tag{4}
\]

with (b_n) independent of order. Fix (q), first let (n\to\infty)
along a subsequence admitting a population predictor limit, and denote its
error from the dense population by (E_q). Then

\[
E_q\le C_\mu q^{-2}\exp\{K\sqrt{\log(e+q)}\}
\quad\hbox{almost surely}.
\]

Consequently there cannot be fixed (c,p_0>0), an exponent (p<2),
and such a family of fixed-order limits with
\(\Pr\{E_q\ge c q^{-p}\}\ge p_0\) for every sufficiently large (q).
The ratio of the proposed lower bound to this upper bound tends to infinity.
The order of limits here is width first at each fixed order, followed by
order tending to infinity. It is not a statement obtained by first setting
(q=q_n).

This does not prove the desired joint-width rate, since no rate for (b_n)
is supplied. It does mean that a negative construction forcing a substantially
larger power of (n) than (n^{1/4}) cannot come solely from a slower pure
population order power. It would need a nonuniform simultaneous width/order
effect. An additional logarithmic or other subpolynomial factor multiplying
(q^{-2}) is not excluded by (4).

## 3. Exact spectrum of an endpoint cusp and its primitive

Let (p_k(x)=P_k(2x-1)) be shifted Legendre polynomials on ([0,1]), with
\(\int_0^1p_k^2=1/(2k+1)\), and let (\Pi_q) project onto degrees below
(q). For a fixed noninteger (\alpha>0), define

\[
u_\alpha(x)=(1-x)^\alpha,
\qquad I_k(\alpha)=\int_0^1u_\alpha(x)p_k(x)dx.
\]

The exact coefficient is

\[
I_k(\alpha)
=\frac{(-1)^k\alpha(\alpha-1)\cdots(\alpha-k+1)}
 { (\alpha+1)(\alpha+2)\cdots(\alpha+k+1)}
=\frac{\Gamma(\alpha+1)}{\Gamma(-\alpha)}
  \frac{\Gamma(k-\alpha)}{\Gamma(k+\alpha+2)}.
\tag{5}
\]

For the finite product, use shifted Rodrigues,

\[
p_k(x)=\frac1{k!}\frac{d^k}{dx^k}[x^k(x-1)^k],
\]

and integrate by parts (k) times first for (\alpha>k-1). The remaining
beta integral is (\int_0^1x^k(1-x)^\alpha dx), yielding (5).
For each fixed (k), expanding the polynomial shows that its integral is
a rational function of (\alpha); thus the finite-product identity extends
to every (\alpha>-1) at which it is evaluated. The gamma expression is
the same identity by the recurrence of the gamma function. Integer
(\alpha\ge0) is a polynomial case and its omitted coefficients vanish
once (q>\alpha).

Put (c_\alpha=\Gamma(\alpha+1)/\Gamma(-\alpha)). The beta-integral
representation of the last ratio in (5) gives

\[
I_k(\alpha)=c_\alpha k^{-2\alpha-2}(1+o(1)).
\tag{6}
\]

To verify this limit directly, write the ratio as

\[
\frac1{\Gamma(2\alpha+2)}
\int_0^1t^{k-\alpha-1}(1-t)^{2\alpha+1}dt
\]

and set (v=k(1-t)). After multiplication by (k^{2\alpha+2}), the
integrand tends to (e^{-v}v^{2\alpha+1}/\Gamma(2\alpha+2)).
For sufficiently large (k), it is bounded by
(e^{-v/2}v^{2\alpha+1}/\Gamma(2\alpha+2)), an integrable majorant.
The integral tends to one. Parseval and summation of powers now yield

\[
\|(I-\Pi_q)u_\alpha\|_{L^2(0,1)}
=\frac{|c_\alpha|}{\sqrt{2\alpha+1}}
 q^{-2\alpha-1}(1+o(1)).
\tag{7}
\]

The primitive has exponent (\alpha+1), so its norm tail is of order
(q^{-2\alpha-3}). Even their signed pairing can be computed exactly:

\[
\begin{aligned}
\int_0^1[(I-\Pi_q)u_\alpha]
              [(I-\Pi_q)u_{\alpha+1}]dx
&=\sum_{k\ge q}(2k+1)I_k(\alpha)I_k(\alpha+1)\\
&=-\frac{(\alpha+1)c_\alpha^2}{2}
       q^{-4\alpha-4}(1+o(1)).
\end{aligned}
\tag{8}
\]

Here (c_{\alpha+1}=-(\alpha+1)^2c_\alpha). The summand is asymptotic
to (2c_\alpha c_{\alpha+1} k^{-4\alpha-5}); its tail sum gives (8).

This is relevant to the suggested endpoint mechanism because a frozen
two-mode residual with decay rates (0<\lambda_1<\lambda_2) has normalized
direction correction of order (s^\alpha), where

\[
\alpha=\frac{\lambda_2-\lambda_1}{\lambda_1}>0,
\qquad s=\tau_\infty-\tau.
\]

Indeed the physical residual ratio is (e^{-(\lambda_2-\lambda_1)t}),
while (s) is asymptotic to a positive constant times
(e^{-\lambda_1t}). A clock equation driven by this normalized residual
integrates its singular component into a forward term of order
(s^{\alpha+1}). Equation (8) shows that the isolated paired singularity
has much faster order decay than a near-quadratic obstruction. Treating the
backward cusp as the whole error discards this extra integration and the
paired projection.

This statement does not identify the complete histories of the actual
closure with these powers. Other history components, their cross terms,
and dynamical feedback must still be analyzed. Even without identifying a
matching primitive, the actual uniform forward (H^1) bound in the
manuscript and (7) give only a source contribution bounded by
(C_\alpha q^{-2\alpha-2}) for an isolated backward cusp with bounded
coefficient. That contribution supplies no source-level power slower than
(q^{-2}).

## 4. A late residual rotation seeded at root width

Consider the explicit frozen residual equation

\[
r(t)=a e^{-\lambda_1t}v_1+b e^{-\lambda_2t}v_2,
\qquad 0<\lambda_1<\lambda_2,
\tag{9}
\]

where (v_1,v_2) are orthonormal in the sample RMS inner product and
(0<a<b). Thus
\(\rho(t)=\sqrt{a^2e^{-2\lambda_1t}+b^2e^{-2\lambda_2t}}\).
The slow and fast components have equal magnitude at

\[
t_* =\frac{\log(b/a)}{\lambda_2-\lambda_1}.
\]

Writing (s_* =\int_{t_*}^\infty\rho(t)dt), the inequalities
(ae^{-\lambda_1t}\le\rho(t)\le ae^{-\lambda_1t}+be^{-\lambda_2t})
give the explicit two-sided estimate

\[
\frac1{\lambda_1}
 a^{\lambda_2/(\lambda_2-\lambda_1)}
 b^{-\lambda_1/(\lambda_2-\lambda_1)}
\le s_*
\le\left(\frac1{\lambda_1}+\frac1{\lambda_2}\right)
 a^{\lambda_2/(\lambda_2-\lambda_1)}
 b^{-\lambda_1/(\lambda_2-\lambda_1)}.
\tag{10}
\]

For fixed (b>0), fixed rates, and a seed
(a_n=O_{\Pr}(n^{-1/2})), this is

\[
s_{*,n}=O_{\Pr}(n^{-\beta}),\qquad
\beta=\frac{\lambda_2}{2(\lambda_2-\lambda_1)}>\frac12.
\tag{11}
\]

The normalized residual can therefore make an order-one late rotation in a
clock interval much shorter than the target prediction scale. Resolving that
rotation as a function and controlling its contribution to a paired network
update are different demands. A nearly degenerate fixed rate pair makes
\(\beta\) larger; it does not make this late clock mass larger.

For clarity about the scale (a_n), a fixed two-dimensional symmetric matrix
whose entries differ from its limiting diagonal matrix by
(O_{\Pr}(n^{-1/2})) has slow-eigenvector leakage of that order when its
limiting eigenvalue gap is fixed. In its eigenvector equation, the fast
component equals an off-diagonal entry times the slow component divided by a
denominator tending to that nonzero gap. Projecting a fixed initial fast
vector onto the slow eigenvector gives the stated estimate. This verifies
the frozen-matrix calculation. It does not assume that the actual trained
matrix remains frozen or that its all-time finite-width fluctuations have
already been controlled.

There is a useful exact bound on the direct history-pairing contribution.
At any fixed clock endpoint (A\le C), let (\Delta b) be a vector
perturbation supported in a clock set of length (s), with
\(\|\Delta b(\xi)\|_2/\sqrt n\le B\). Let a forward history (h)
satisfy the manuscript's uniform derivative bound
\(n^{-1}\int_0^A\|h'(\xi)\|_2^2d\xi\le C\). Orthogonality and
Cauchy--Schwarz give

\[
\begin{aligned}
&\left\|\frac1n\int_0^A\Delta b\,h^\top d\xi
 -\frac1n\int_0^A(\Pi_q\Delta b)(\Pi_q h)^\top d\xi\right\|_F\\
&\qquad=\left\|\frac1n\int_0^A
   [(I-\Pi_q)\Delta b][(I-\Pi_q)h]^\top d\xi\right\|_F
\le \frac{CB\sqrt{s}}q.
\end{aligned}
\tag{12}
\]

The forward tail estimate is the weighted Legendre bound with
(\xi(A-\xi)\le A^2/4); projection contraction bounds the other factor
by (B\sqrt s). Combining (11) and (12), for
(q_n\ge c n^{1/4}) this source contribution is

\[
O_{\Pr}(n^{-1/4-\beta/2})=o_{\Pr}(n^{-1/2}).
\tag{13}
\]

Equation (13) concerns the direct pairing contribution of a perturbation
localized to the late clock interval. It does not bound the earlier slow-mode
component or its effect on the evolved parameters. It identifies the gap in
the particular proposal that the sharp *late normalized-residual turn alone*
forces an order beyond (n^{1/4}).

## 5. The missing causal lower bound

The actual closure obeys, exactly,

\[
\dot{\widehat\theta}=F(\widehat\theta)+E,
\qquad E_1=E_w=0,
\qquad
E_\ell=\frac{2\widehat\rho}{mn}\sum_a
 (\widehat b_a^{(\ell)}-\widehat b_a^{(\ell)*})
 (\widehat h_a^{(\ell-1)}-\widehat h_a^{(\ell-1)*})^\top.
\tag{14}
\]

Here (F) is the dense physical vector field, (b_a=r_a\delta_a/\rho),
and stars denote endpoint values of the corresponding projected histories.
All factors on the right are from the actual closure. The backward response
excludes the residual, as in the canonical definition.

At each fixed finite width and each finite physical time, the precise
prediction transfer can be written without an approximation. Let
(\Delta\theta=\widehat\theta-\theta_D), vectorizing physical parameters,
and define

\[
B(t)=\int_0^1 DF(\theta_D(t)+v\Delta\theta(t))dv.
\]

Let (U(t,s)) solve
\(\partial_tU(t,s)=B(t)U(t,s)\), (U(s,s)=I). Tanh smoothness and
finite-time boundedness make these definitions valid. Subtracting the two
equations and using the fundamental theorem of calculus yields

\[
\Delta\theta(t)=\int_0^tU(t,s)E(s)ds.
\]

For the network output (f_x(\theta)) at a specified query (x), another
application of the fundamental theorem gives

\[
\widehat f(t,x)-f_D(t,x)
=\int_0^t
 \left[\int_0^1 Df_x(\theta_D(t)+v\Delta\theta(t))dv\right]
 U(t,s)E(s)ds.
\tag{15}
\]

Thus a lower bound requires a surviving signed component of (15) with the
required Gaussian probability. Nonzero (E), nonzero
\(\int E\), or a lower bound on a tail norm does not ensure this: the
source can cancel in time or be annihilated by the prediction derivative.
Replacing the actual (E) by a source computed on the dense path also needs
a remainder bound uniform in the growing width and order. No such lower
bound or uniform remainder was established in this route.

For one effective compatible training input there is an additional exact
restriction on the singular-clock idea. On a nonstationary fitting trajectory
the scalar residual keeps its initial sign, since zero residual is an
equilibrium of the locally Lipschitz raw moment ODE and cannot first be
reached at a finite time. Hence (r/\rho=-\operatorname{sgn}(y)) is
constant. With (u=2\int_0^t\rho(s)ds), the clock is exactly
\(\tau=1+u/2\), and dividing the physical equations by (2\rho)
removes the label from the controlled curve. The label determines its fitted
stopping point. There is no rotating normalized-residual direction in this
case.

## 6. Separated large-label scope and final assessment

No fixed large-label pathology was constructed. The following bounded check
rules out the simplest Gaussian-seeded escape proposal at initialization.
Let (H) be the initialized top-layer feature matrix with columns indexed
by training inputs and let (\Gamma_w=H^\top H/(mn)). At zero readout,

\[
\dot w(0)=\frac2mHy,\qquad
\frac{\|\dot w(0)\|_2^2}{n}
=\frac4m y^\top\Gamma_w y\ge4\lambda Y^2
\]

on the initialized Gram event. This statement holds regardless of label
size. Therefore nonzero compatible labels do not produce a stationary
population initialization whose only motion is a Gaussian-sized empirical
leakage. The weighted compatible quotient gives the same conclusion. If an
incompatible redundant-label component instead has every effective label
zero, its cancellation is exact at every width and both physical flows
remain stationary; it supplies no random escape either.

Also the dense residual equation is always
\(\dot r=-2\Gamma(\theta)r\), with positive semidefinite tangent Gram
\(\Gamma\), for any label magnitude. A negative frozen decay eigenvalue
is therefore not an admissible dense residual mechanism. An unstable
*trajectory variation* could still arise through the residual-weighted
parameter Hessian, or from a later feature degeneracy. Producing such a
trained state from the canonical initialization and proving that the actual
closure defect excites it remain additional obligations. No concrete neural
construction of that type was found in this bounded extension.

Outside the small-label regime, a changing basin or persistent positive
residual could in principle alter all-time behavior, but an explicit
reachable Gaussian example and an actual prediction discrepancy are still
necessary. The assigned
persistent-clock diagnostic does not supply that implication: its static
pairing uses dense integrated responses, whereas an autonomous closure uses
its own path. Inconsistent duplicate labels would also change the present
compatible-label contract even if their magnitudes were small.

The results of this attempt are therefore the exact cusp spectrum
(5)--(8), the exact two-mode clock estimate (10), the localized source bound
(12), and the explicit causal identity (15). They invalidate particular
shortcuts to the proposed lower bound. They neither establish useful
root-width tracking nor disprove it. A successful negative construction must
now identify a nonuniform width/order feedback mechanism, or a sharp
subpolynomial order loss, and prove that its signed effect survives in (15)
with nonvanishing probability.
