# Independent reconstruction of the polynomial fitting-width proof

2026-10-07. Scoped mathematical verification; no experiment or promotion.

## Verdict and frozen inputs

**PASS for the initialization and deterministic dense-fitting theorem in
§§1–5 of `EXPLICIT_FITTING_WIDTH.md`, under its stated assumptions.** The
explicit width (5), the event (6), the original exact label allowance (8),
the all-time conclusions (9)–(10), and the finite-
\(\beta\) envelope (12) follow with their displayed constants. I found no
mathematical correction necessary in these sections.

This is not a verification of an analytic-source or unseen-query-decoder
success width. Section 6's source interfaces are not premises of the
dense-fitting theorem and are not independently certified here. Its
elementary initial Gaussian estimates are checked conditionally below.

The complete scientific inputs were exactly:

- `studies/unseen_query_decoder_20261005/EXPLICIT_FITTING_WIDTH.md`, SHA-256
  `62d018c6448b0e6af6085827a856667ba58747810c6b284452dea21ce800919d`.
- The expressly authorized
  `studies/integrated_general_compression_20261004/GENERAL_EXPLICIT_FITTING.md`,
  SHA-256
  `5c6f12b78847a2b2874c5bc82eb1cea5f4929ee071b114d09b098397c5e2b8d6`.

No study README, history, prior verdict, other research artifact, or linked
scientific source was read. The rigorous-math and canonical-notation skills,
including the neural-network reference, governed the reconstruction. This
report is the only file written.

## Setup and claim being checked

There are \(L\ge2\) hidden layers of width \(n\), unit inputs
\(v_a\in\mathbb R^d\), and \(m\) training samples. The network is
\[
z^{(1)}(v)=Av,\quad z^{(j)}(v)=W^{(j)}h^{(j-1)}(v),\quad
h^{(j)}(v)=\phi_j(z^{(j)}(v)),\quad
f_n(v)=w^\top h^{(L)}(v)/n.
\]
Initially, entries of \(A\) are independent \(N(0,1)\), entries of each
\(W^{(j)}\) are independent \(N(0,1/n)\), the blocks are mutually
independent, and \(w=0\). Each activation is \(C^2\), with bounded first
and second real derivatives. Write
\(b=\max_j|\phi_j(0)|\) and
\(s=\max\{1,\max_j\|\phi'_j\|_\infty\}\).

For a standard scalar Gaussian \(G\), let
\[
q_0=1,\qquad q_j=\mathbb E\phi_j(\sqrt{q_{j-1}}G)^2,
\qquad H=\max\{1,\sqrt{q_1},\ldots,\sqrt{q_L}\}.
\]
The population training Gram recursion starts at
\(Q^{(0)}_{ab}=v_a^\top v_b\) and applies
\(Q^{(j)}_{ab}=\mathbb E\phi_j(Z_a)\phi_j(Z_b)\), where
\(Z\sim N(0,Q^{(j-1)})\). Its diagonal is \(q_j\), even for singular
covariances. Consequently, for
\(\gamma=\lambda_{\min}(Q^{(L)})>0\) and \(\lambda=\gamma/m\),
\(0<\lambda\le H^2/m\le H^2\).

All constants \(R,K,D,T_1,T_2,C,\varepsilon,h,\Xi\) below retain the
definitions in candidate (4)–(5). In particular,
\[
R=2H,\quad K=b+sR,\quad D=2sb+4s^2R,\quad
T_1=\sum_{i=0}^{L-1}s^i,\quad T_2=\sum_{i=0}^{L-1}s^{2i},
\]
\[
C=T_2(2K+1+DT_1),\quad
\varepsilon=\min\{(8T_1)^{-1},\gamma/(2mC)\},\quad
h=\min\{1/2,H/[4(8s)^L]\}.
\]

## Gaussian concentration and polarization

For completeness, Gaussian concentration used here can be recovered
without an external probabilistic theorem. For positive smooth bounded
\(g\), the Ornstein–Uhlenbeck semigroup
\(P_tg(x)=\mathbb Eg(e^{-t}x+\sqrt{1-e^{-2t}}G)\) satisfies
\[
\operatorname{Ent}_\gamma(g)
=\int_0^\infty\mathbb E_\gamma
  \frac{|\nabla P_tg|^2}{P_tg}\,dt
\le\frac12\mathbb E_\gamma\frac{|\nabla g|^2}{g}.
\]
The equality follows by differentiating
\(\mathbb E_\gamma[P_tg\log P_tg]\), integrating by parts against the
Gaussian density, and using \(P_tg\to\mathbb E_\gamma g\). The inequality
uses \(\nabla P_tg=e^{-t}P_t\nabla g\), weighted Cauchy–Schwarz, Gaussian
invariance, and \(\int_0^\infty e^{-2t}dt=1/2\).

If a nonnegative function \(F(G)\) is \(a_0\)-Lipschitz, substitution of
\(g=e^{uF}\) gives, for \(\psi(u)=\log\mathbb Ee^{uF}\),
\(u\psi'(u)-\psi(u)\le u^2a_0^2/2\). Integrating
\((\psi(u)/u)'\) and applying the same argument to \(-F\) yields
\[
\log\mathbb Ee^{u(F-\mathbb EF)}\le u^2a_0^2/2,
\quad
\Pr(|F-\mathbb EF|>t)\le2e^{-t^2/(2a_0^2)},
\quad\operatorname{Var}(F)\le a_0^2.
\]
Smoothing and truncation are legitimate because a Lipschitz function grows
at most linearly and all exponential moments of its absolute value under a
finite-dimensional Gaussian are finite. Comparing the second derivatives
of the centered log moment-generating function at zero gives the displayed
variance bound. Nonnegativity then implies
\(0\le\sqrt{\mathbb EF^2}-\mathbb EF\le a_0\). Thus, if
\(\varepsilon\ge2a_0\),
\[
\Pr\bigl(|F-\sqrt{\mathbb EF^2}|>\varepsilon\bigr)
\le2e^{-\varepsilon^2/(8a_0^2)}.
\]
The case \(a_0=0\) is deterministic and requires no division by zero.

For independent identically distributed Gaussian rows with input marginal
standard deviations at most \(R\), the empirical RMS of one activated
coordinate is \(sR/\sqrt n\)-Lipschitz in standard Gaussian roots. For a
pair of coordinates, the covariance operator norm is at most \(2R^2\);
the gradient norm of their activated sum or difference is at most
\(\sqrt2s\). Their empirical RMS norms are therefore
\(2sR/\sqrt n\)-Lipschitz. This factorization also exists for singular
covariances.

Each population sum/difference RMS is at most \(2K\). If both empirical
RMS norms differ from their population values by at most
\(\varepsilon\le1\), each squared-norm error is at most
\((4K+\varepsilon)\varepsilon\). The polarization identity divides the
sum of the two errors by four, giving
\[
\left|n^{-1}\sum_i\phi(Z_{ia})\phi(Z_{ib})
       -\mathbb E\phi(Z_a)\phi(Z_b)\right|
\le2K\varepsilon+\varepsilon^2/2
\le(2K+1)\varepsilon.
\]
Every RMS test consequently fails with probability at most
\(2\exp[-n\varepsilon^2/(32s^2R^2)]\), provided
\(n\ge16s^2R^2/\varepsilon^2\). Candidate (5) implies this prerequisite
because \(\Xi>1/2\).

## Covariance comparison, including zero variances

The scalar RMS map
\(g_j(\sigma)=\|\phi_j(\sigma G)\|_{L^2}\) obeys
\(|g_j(\sigma)-g_j(\sigma')|\le s|\sigma-\sigma'|\) by using the same
Gaussian \(G\) and the reverse triangle inequality.

For two Gaussian pair covariances \(C,C'\), let their marginal standard
deviations be \(\sigma_a,\sigma_b\) and
\(\sigma'_a,\sigma'_b\), all at most \(R\), and put
\(\Delta=\max_i|\sigma_i-\sigma'_i|\). Shrink both pairs, preserving
their respective correlations, to marginal standard deviations
\(\tau_i=\min(\sigma_i,\sigma'_i)\). Subtracting product factors and
using their \(L^2\) bounds \(K\) makes the total shrinking cost at most
\(sK(|\sigma_a-\sigma'_a|+|\sigma_b-\sigma'_b|)\le2sK\Delta\).

At fixed positive marginals, Gaussian density differentiation and two
integrations by parts give the correlation derivative
\[
\frac{d}{d\rho}\mathbb E\phi_j(\tau_aG_1)\phi_j(\tau_bG_2)
=\tau_a\tau_b\mathbb E\phi'_j(\tau_aG_1)\phi'_j(\tau_bG_2).
\]
Its modulus is at most \(s^2\tau_a\tau_b\). Linear growth and bounded
derivatives justify the calculation on \(-1<\rho<1\); continuity of
Gaussian roots and Gaussian integrability extend the integrated bound to
\(\rho=\pm1\).

Writing \(p=\sigma_a\sigma_b\), \(p'=\sigma'_a\sigma'_b\), assume
first \(p\ge p'>0\). Since
\[
\rho-\rho'=(C_{ab}-C'_{ab})/p+C'_{ab}(1/p-1/p'),
\]
\(|C'_{ab}|\le p'\) and \(\tau_a\tau_b\le p\) imply
\[
\tau_a\tau_b|\rho-\rho'|
\le|C_{ab}-C'_{ab}|+|p-p'|
\le|C_{ab}-C'_{ab}|+2R\Delta.
\]
Interchanging the pairs handles \(p'\ge p\). Combining the shrinking
and correlation costs yields exactly
\[
|\Psi_j(C)_{ab}-\Psi_j(C')_{ab}|
\le s^2|C_{ab}-C'_{ab}|+(2sb+4s^2R)\Delta.
\]
Zero marginal variances follow by continuity, for example after adding
\(uI\) to both covariances and taking \(u\downarrow0\), with the
intermediate radius \(\sqrt{R^2+u}\) tending to \(R\). No positive lower
variance bound is used.

## Layer induction, probability, and sphere coverage

Choose a deterministic sphere \(h\)-net of size
\(P\le(1+2/h)^d\). There are \(m+P\) individual RMS tests and at most
\(2m^2\) polarization RMS tests per layer, hence at most \(3m^2+P\)
tests. Conditional on the previous layers, rows in the new layer are
independent identically distributed Gaussians with covariance equal to the
preceding empirical feature Gram.

Let \(\Delta_j\) be the largest individual RMS error at training and net
points relative to \(\sqrt{q_j}\), and \(E_j\) the largest training
Gram-entry error relative to \(Q^{(j)}\). Starting from
\(\Delta_0=E_0=0\), successful tests give
\[
\Delta_j\le\varepsilon+s\Delta_{j-1},\qquad
E_j\le(2K+1)\varepsilon+s^2E_{j-1}+D\Delta_{j-1}.
\]
Therefore \(\Delta_j\le\varepsilon T_1\le1/8\) and
\(E_j\le\varepsilon T_2(2K+1+DT_1)=\varepsilon C\le\gamma/(2m)\).
Every preceding empirical standard deviation is at most
\(H+1/8<R\), closing the conditional Gaussian prerequisite. Bounding the
first failed test uses conditional probabilities only; it does not require
independence between layers or test points.

Writing \(P_0=(1+2/h)^d\), the fourth gate in candidate (5) gives
\[
\begin{aligned}
\Pr(\text{a stopped test fails})
&\le2L(3m^2+P)e^{-\Xi}\\
&\le2L\,4(m+1)^2P_0
       \frac{\delta}{16L(m+1)^2P_0}=\delta/2.
\end{aligned}
\]
For a matrix \(M\), two one-quarter sphere nets give
\(\|M\|_{\rm op}\le2\max|u^\top Mv|\): approximating its maximizing
unit vectors costs at most \(\|M\|_{\rm op}/2\). At operator threshold
eight, the relevant scalar Gaussian thresholds are \(4\) for a hidden
mixer and \(4\sqrt n\) for \(A\); both give exponent \(-8n\).
Union over net pairs gives exactly candidate (21). Its width gates bound
the hidden-mixer union by \((L-1)\delta/(4L)\), and the first-layer
failure by \(\delta/4\), totaling less than \(\delta/2\).

On this operator event, \(h_0^{(j)}(v)/\sqrt n\) is
\((8s)^j\)-Lipschitz in \(v\). Net norms are at most \(H+1/8\), while
the net extension costs at most \((8s)^Lh\le H/4\). Thus all sphere norms
are at most \(11H/8<3H/2\). A symmetric matrix with maximum entry error
\(E_L\) has operator error at most \(mE_L\); hence the final empirical
Gram has least eigenvalue at least \(\gamma/2\). Dividing by \(m\)
proves the gap in (6). The total failure is at most \(\delta\).

## The numerical \(\beta^{32L}\) envelope

For finite candidate (11)'s \(\beta\), one has
\(\beta\ge10\), \(b,s\le\beta\), and the scalar recursion gives
\(H\le(2\beta)^L\le\beta^{2L}\). For \(L\ge2\), explicit estimates are
\[
\begin{gathered}
R\le2\beta^{2L}\le\beta^{3L},\qquad
K\le3\beta^{2L+1}\le\beta^{3L},\\
D\le10\beta^{2L+2}\le\beta^{4L},\qquad
T_1\le L\beta^{L-1}\le\beta^{2L},\qquad
T_2\le L\beta^{2L-2}\le\beta^{3L},\\
C\le2\beta^{9L}\le\beta^{10L},\qquad
\varepsilon^{-1}=\max\{8T_1,2mC/\gamma\}
 \le\beta^{11L}(1+m/\gamma),\\
32s^2R^2\le128\beta^{4L+2}\le\beta^{8L}.
\end{gathered}
\]
For the net logarithm,
\[
1+2/h=\max\{5,1+8(8s)^L/H\}
\le9\beta^{2L}\le\beta^{3L}.
\]
Put \(B=dL\log\beta+\log[16L(m+1)^2/\delta]\). Then \(\Xi\le3B\),
so the concentration gate is at most
\(3\beta^{30L}(1+m/\gamma)^2B\le
\beta^{31L}(1+m/\gamma)^2B\).
Both operator-gate denominators exceed one, their numerators are at most
\(B\), and \(B>1\). Thus the maximum in (5), and consequently its
ceiling, are bounded by the claimed \(\beta^{32L}\) envelope. This
calculation is uniform in all displayed parameters; it does not absorb
depth-dependent constants into an unspecified exponent.

## Deterministic fitting with the exact label cap

Let \(r_a=f_n(v_a)-y_a\), \(\rho=\|r\|_2/\sqrt m\), and
\(Y=\|y\|_2/\sqrt m\). The backpropagated vectors are
\(\delta_a^{(L)}=w\odot\phi'_L(z_a^{(L)})\) and
\(\delta_a^{(j)}=\phi'_j(z_a^{(j)})\odot
W^{(j+1)\top}\delta_a^{(j+1)}\). Candidate (22) is exactly the
authorized source's flow: mobilities are \(n\) for \(A,w\), and one
for the hidden mixers, relative to the loss \(\rho^2\).

Use the parameter norm
\(\|\theta\|_{\rm par}^2=\|A\|_F^2/n+
\sum_{j=2}^L\|W^{(j)}\|_F^2+\|w\|_2^2/n\). Before a first exit from
the tube with operator bounds nine, sphere feature bound \(2H\), and
normalized top Gram gap \(\lambda/4\), the chain rule gives
\[
-\frac{d}{dt}\rho^2=\|\dot\theta\|_{\rm par}^2,
\qquad
\|\dot w\|_2^2/n
=\frac4{m^2n}r^\top\mathsf H^\top\mathsf Hr
\ge\lambda\rho^2.
\]
Hence \(\rho(t)\le Ye^{-\lambda t/2}\) and
\(\int\rho\,dt\le2Y/\lambda\). While \(\rho>0\),
\[
\int\frac{\|\dot\theta\|_{\rm par}^2}{\rho}\,dt
=2(Y-\rho(t))\le2Y.
\]
Weighted Cauchy–Schwarz therefore bounds total parameter path length by
\(2Y/\sqrt\lambda\). In particular
\(\|w\|_2/\sqrt n\le2Y/\sqrt\lambda\), because \(w_0=0\).
If \(\rho=0\), every velocity vanishes and the solution is stationary.

With \(D_j=s(9s)^{L-j}\), \(U_1=D_1\), and \(U_j=2HD_j\) for
\(j\ge2\), backward propagation and sample Cauchy–Schwarz bound the
normalized Frobenius speed of hidden block \(j\) by
\(2\rho U_j\|w\|_2/\sqrt n\). Its displacement is consequently at most
\(8U_jY^2/\lambda^{3/2}\). Subtracting two forward passes gives the
feature displacement coefficients
\(F_1=sU_1\), \(F_j=s(2HU_j+9F_{j-1})\). At the top layer this is
exactly
\[
F=F_L=s^2\left[(9s)^{2L-2}
             +4H^2\sum_{i=0}^{L-2}(9s)^{2i}\right].
\]
The recurrence gives \(F\ge F_j,U_j,1\): the \(F_j\) increase, and
\(F_1\ge U_1\), \(F_j\ge2HsU_j\ge U_j\) for \(j\ge2\).

The exact original allowance is
\[
Y\le\frac{\gamma}{8mH\sqrt F}
=\frac{\lambda}{8H\sqrt F}.
\]
It yields
\[
8FY^2/\lambda^{3/2}
\le\frac{\sqrt\lambda}{8H^2}\le\frac1{8H}.
\]
Every operator bound thus improves to at most \(8+1/8<9\), and every
sphere feature bound improves to at most \(3H/2+H/8<2H\). The operator
change of \(\mathsf H/\sqrt{mn}\) is bounded by its Frobenius change,
at most \(\sqrt\lambda/(8H^2)\le\sqrt\lambda/8\). For any unit sample
vector, the triangle inequality therefore bounds the least singular value
below by
\(\sqrt\lambda(1/\sqrt2-1/8)>\sqrt\lambda/2\). This strictly improves
the stopped Gram boundary. A finite first exit cannot occur.

The vector field is locally Lipschitz at each fixed finite width. Finite
parameter path length prevents finite-time escape and gives convergence of
every parameter as \(t\to\infty\). Residual decay then proves exact
interpolation. This reasoning applies on the same initialization event to
every admissible label vector; no probability union over labels is needed.

Finally,
\(\|\dot w\|_2/\sqrt n\le4H\rho\) and the differentiated forward
recursion gives
\(\|\dot h^{(L)}(v)\|_2/\sqrt n\le2\rho F\|w\|_2/\sqrt n\).
The product rule yields
\[
|\dot f_n(t,v)|\le8(H^2+FY^2/\lambda)\rho(t).
\]
Integration from \(t\) to infinity, together with
\(FY^2/\lambda\le\lambda/(64H^2)\le1/64\le H^2/64\), gives the
claimed whole-sphere tail
\[
\sup_{\|v\|=1}|f_n(\infty,v)-f_n(t,v)|
\le\frac{65}{4}H^2\frac Y\lambda e^{-\lambda t/2}.
\]
For \(Y=0\), the initial residual and all velocities are zero. There is
no positive lower label bound, label-cap strengthening, or activation-value
normalization anywhere in this argument.

## Section 6: elementary checks and unverified interfaces

Conditional on the previous initialized layers having input variances at
most \(R^2\), suppose a supplied source constant satisfies
\(\eta_{\rm src}R\le1\). For \(Z\sim N(0,\sigma^2)\), \(\sigma\le R\),
\(e^{u|Z|}\le e^{uZ}+e^{-uZ}\) proves
\[
\mathbb Ee^{\eta_{\rm src}|Z|}\le2e^{1/2}<4,
\qquad\mathbb Ee^{2\eta_{\rm src}|Z|}\le2e^2<15.
\]
For a fixed layer and sample, rows are conditionally independent, so the
variance of their exponential average is at most \(15/n\). Its mean is
less than four, and Chebyshev bounds the probability of exceeding eight
by \(15/(16n)\). A stopped union over \(mL\) layer/sample choices gives
\(15mL/(16n)\). If the source's initial budget is the sum of these layer
averages and its initial carriers vanish, it is consequently at most
\(8L<\mathcal B/2\) for \(\mathcal B=1024e^2L\). Combining this with
the fitting event at confidence \(\delta/2\) and
\(n\ge2mL/\delta\) gives total failure at most
\(\delta/2+15\delta/32=31\delta/32<\delta\).

Separately, the same stopped Gaussian union over \(nLm\) coordinates
gives failure at most \(\delta/2\) for threshold
\(R\sqrt{2\log(4nLm/\delta)}\). Combined with the fitting event at
confidence \(\delta/2\), this is another event of probability at least
\(1-\delta\). If both this maximum event and the exponential-budget
event are required simultaneously, their failure allocations must also be
summed; the two separate \(1-\delta\) augmentations do not themselves
give a joint \(1-\delta\) assertion. The candidate states the maximum
estimate as an additional failure bound, so this is an accounting
qualification, not a correction to its central theorem.

The allowed inputs do not define the initial source budget, carriers,
\(H_{\max},W_{\rm G},C_{\rm abs}\), or the source recurrences. In
particular, the three displayed source inequalities imply only
\(\eta_{\rm src}R\le1/(65536C_{\rm abs})\); deriving
\(\eta_{\rm src}R\le1\) additionally requires the source's lower bound
\(C_{\rm abs}\ge1/65536\), or direct verification of that condition.
These source definitions and bounds must be checked in their authorized
inputs before treating the initial-budget interface as unconditional.

The following limited logical checks do not certify the cited sources:

- If (29) holds for every fixed positive integer \(p\), then its right
  side tends to zero as \(p\to\infty\), because
  \(16L/\mathcal B=1/(64e^2)<1\). It proves an asymptotic probability
  limit but supplies no numerical width for a given confidence.
- Given positive \(Y,S,U_{\rm fin}(S),a\), and \(S=16Y/\lambda\), the
  choice (32) has \(cM\le1\le\sqrt{\log(en)}\) for \(n\ge1\). Direct
  inversion gives exactly (33), since
  \(64YS/\lambda=4S^2\). This checks the algebra conditional on the
  source permitting that radius choice.
- An unchanged construction condition \(n^{-1}\le Y\) is
  \(n\ge1/Y\). No width threshold independent of arbitrarily small
  positive \(Y\) can enforce this particular condition for all such
  labels. This does not contradict the dense-fitting theorem, which has
  no such condition.

The trained-coordinate estimate, joint-budget and insertion estimates,
finite-query localization, allowed complex radius, and power ledger in
§6 remain unverified source interfaces in this review. None is used to
prove the passing §§1–5 result.
