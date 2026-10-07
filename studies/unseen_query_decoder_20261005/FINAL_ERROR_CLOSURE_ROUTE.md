# Final-error closure: acquired-pair calibration and a frozen open lemma

2026-10-07. Scoped author derivation, proof only. The first route below was
frozen before evaluating the supervisor's separate retained-source-seed
proposal. This note is not an independent review or a promotion.

The unchanged fast passive decoder is not proved to attain the original
independent-dense-pair certificate at polynomial width here. A new exact
calibration identity removes the constant and linear posterior likelihood
terms from a query moment. Its remaining curvature estimate is explicit
and unproved for the actual neural source. This identifies a possible
correction to the decoder, rather than another choice of its old sample
count. Section 6 records the subsequent collaborative source-seed route
separately when assessed.

## 1. Fixed target and the source likelihood

Keep width \(n\), depth \(L\), \(m\ge d\) spanning training inputs,
the original Gaussian deep network, zero readout, mean squared loss,
mobilities \((n,1,\ldots,1,n)\), and the entire original small-label
intersection. Put \(Y=\|y\|_2/\sqrt m\); \(Y=0\) remains exactly
zero. The target is current-state evaluation on the entire sphere and at
every physical time, including the endpoint, within
\(3b_n(\delta/256)\) of an independent dense width-\(n\) trajectory.
The original certificate is not enlarged. Memory, query work, numerical
precision, and finite random seeds must retain their counted meaning.

Fix a scalar prefix \(c=(c_1,\ldots,c_P)\) of the continuous-noise
shadow in FAST_FINITE_POSTERIOR.md. Here \(P\) is its actual acquired
pair count, bounded by a constant times \(R^2\), and \(\mu\) is the
actual finite packet prior. Once \(c\) is fixed, all creation-time
arguments in every acquired row test are fixed. Define the finite vector

\[
 F_c(z)=(F_1(z),F_2(z;c_1),\ldots,F_P(z;c_{<P}))\in\mathbb R^P,
 \qquad s_c=\mu F_c,
 \qquad V_c(z)=F_c(z)-s_c.
 \tag{1}
\]

The source observes rounded Gaussian-noisy empirical means. If the
\(r\)-th scalar grid is \(h_r\), let

\[
 \ell_c(s)=\prod_{r=1}^P
 \Pr\{s_r+\eta E_r\in[c_r-h_r/2,c_r+h_r/2)\},
 \qquad E_r\sim N(0,1)\text{ independently}.
 \tag{2}
\]

Cell endpoint conventions do not matter for continuous Gaussian noise.
Adaptivity changes the frozen functions in (1), but not the likelihood
identity

\[
 \frac{d\pi_c}{d\mu^{\otimes n}}(z_{1:n})
 =\frac{\ell_c(n^{-1}\sum_iF_c(z_i))}{p_c},
 \qquad
 p_c=\mathbb E_{\mu^{\otimes n}}\ell_c(n^{-1}\sum_iF_c(Z_i))>0.
 \tag{3}
\]

Indeed, given the packets and the prescribed preceding codes, the next
scalar channel has precisely the corresponding factor in (2). Multiply
these conditional probabilities. This gives the full prefix likelihood,
including all redundant or degenerate acquired pairs.

The one-row marginal \(\nu_c\) consequently satisfies

\[
 \frac{d\nu_c}{d\mu}(z)=w_c(V_c(z)),\qquad
 w_c(v)=\frac{1}{p_c}\mathbb E_{\mu^{\otimes(n-1)}}
 \ell_c\!\left(s_c+\frac{v+\sum_{i=2}^nV_c(Z_i)}n\right).
 \tag{4}
\]

This is an exact finite-law identity. It is not a free evaluator for
the expectation over the other \(n-1\) packets.

## 2. An exact first-order calibration cancellation

Let \(H(z)\) be any finite scalar query row integrand at held-fixed
incoming passive moments. Its definition can already integrate the fresh
passive Gaussian, or include that Gaussian in the packet identically in
the prior and posterior. Define

\[
 \Sigma_c=\mu(V_cV_c^\top),\qquad
 q_c=\mu[V_c(H-\mu H)],\qquad
 a_c=\Sigma_c^\dagger q_c,
\]
\[
 H_{\mathrm{res}}(z)=H(z)-\mu H-a_c^\top V_c(z).
 \tag{5}
\]

The pseudoinverse in (5) is a mathematical definition, with no numerical
conditioning claim. It is well defined even for singular \(\Sigma_c\):
if \(u\) is in its nullspace, then \(u^\top V_c=0\) almost surely,
so \(u^\top q_c=0\). Thus \(q_c\) belongs to its range, and

\[
 \mu H_{\mathrm{res}}=0,\qquad
 \mu[V_cH_{\mathrm{res}}]=0.
 \tag{6}
\]

Write \(\varepsilon_c=\|\nu_c F_c-c\|_2\), and suppose

\[
 \Lambda_c=\sup_{z\in\operatorname{supp}\mu,\ 0\le u\le1}
       \|D^2w_c(uV_c(z))\|_{\mathrm{op}}<\infty.
 \tag{7}
\]

Then the calibrated posterior moment obeys

\[
 \left|\nu_cH-\{\mu H+a_c^\top(c-s_c)\}\right|
 \le \|a_c\|_2\varepsilon_c
   +\frac{\Lambda_c}{2}\,
                 \mu[|H_{\mathrm{res}}|\,\|V_c\|_2^2].
 \tag{8}
\]

For the proof, the exact discrepancy after using \(\nu_cF_c\) instead
of \(c\) is \(\nu_cH_{\mathrm{res}}=\mu[H_{\mathrm{res}}w_c(V_c)]\).
Taylor's formula gives

\[
 w_c(v)=w_c(0)+Dw_c(0)v+
       \int_0^1(1-u)v^\top D^2w_c(uv)v\,du.
 \tag{9}
\]

Both first terms vanish after multiplying by \(H_{\mathrm{res}}\)
and averaging, by (6). Bound the integral by (7), and the replacement
of \(\nu_cF_c\) by \(c\) by Cauchy--Schwarz. This proves (8).
The source already gives
\(\varepsilon_c\le\sqrt P(\eta\sqrt{P/\alpha}+h_{\max}/2)\)
on its good-prefix event. This controls the first term only after the
coefficient norm and the required numerical precision have been counted.

The correction in braces uses acquired pair values. It has a different
target from merely averaging more prior packets. If \(H\) is already
affine in the acquired tests, its residual vanishes and (8) gives only
the explicitly controlled pair-observation error.

Ridge regularization does not silently preserve the cancellation. For
\(a_{c,\lambda}=(\Sigma_c+\lambda I)^{-1}q_c\), the residual has
\(\mu[V_cH_{\mathrm{res},\lambda}]=\lambda a_{c,\lambda}\).
Equation (9) then leaves the additional linear term
\(\lambda Dw_c(0)a_{c,\lambda}\). A covariance gap or a quantitative
bound on this term is needed for a counted ridge implementation.

## 3. The exact missing curvature estimate

Let \(\mathcal C_c=\prod_r[c_r-h_r/2,c_r+h_r/2)\). Differentiating
the Gaussian density inside its cell integral gives the exact identity

\[
 D^2w_c(v)=\frac{1}{n^2\eta^2p_c}
 \mathbb E\left[(EE^\top-I)
 \mathbf1_{\{s_c+(v+\sum_{i=2}^nV_c(Z_i))/n+\eta E
                     \in\mathcal C_c\}}\right].
 \tag{10}
\]

The packets in this expectation have their product prior and \(E\)
is an independent standard \(P\)-dimensional Gaussian. Formula (10)
follows first for each cell integral, whose second derivative is its
Gaussian score \((EE^\top-I)/\eta^2\), then by the chain rule for
the factor \(1/n\) in (4). Finite packet support and smooth Gaussian
cell probabilities justify all derivatives.

Bounding the score directly leaves \(n^{-2}\eta^{-2}\) and the
prefix normalizer \(p_c^{-1}\). The source's \(\eta\) is deliberately
much smaller than root-width statistical fluctuations. No polynomial
width conclusion follows from that direct derivative bound.

A sufficient new neural-source lemma is the following contraction bound,
uniformly over good prefixes and reachable query contexts:

\[
 \left|\mu\left[H_{\mathrm{res}}
  \int_0^1(1-u)V_c^\top D^2w_c(uV_c)V_c\,du\right]\right|
 \le \frac{A\,Z^q}{n},
 \tag{11}
\]

where \(q\) is an absolute constant and
\(A\) is a fixed polynomial in \(\beta^L,m,d,1+m/\gamma,\delta^{-1}\),
with all numerical coefficient and sampling costs inside the permitted
budgets. A norm estimate implying (11) is stronger than necessary; the
signed contraction in (11) allows useful cancellation. The entropy bound
\(D(\nu_c\Vert\mu)\le K_*/n\) controls neither (10) nor its
contraction with \(H_{\mathrm{res}}\). The acquired Gram bounds also
do not control the covariance of their pair tests or its pseudoinverse.
Thus (11) is an exposed new lemma, not an established consequence.

## 4. A solvable Gaussian calibration case

The inverse-noise factor in (10) can disappear after the leave-one-out
convolution. This is visible in an exact case, without claiming that the
nonlinear neural pair tests satisfy it. Let \(U_i\) be independent
\(N(0,I_q)\), and observe
\(C=n^{-1}\sum_iU_i+\eta E\). At the continuous observation \(c\),
put

\[
 a=\frac{1}{n(1+n\eta^2)},\qquad
 z_c=\frac{c}{\sqrt{1/n+\eta^2}}.
\]

Elementary Gaussian conditioning gives
\(U_1\mid C=c\sim N(\sqrt a\,z_c,(1-a)I_q)\), and \(a\le1/n\).
For a \(C^2\) integrand with globally bounded Hessian
\(\|D^2H\|\le M\), its linear regression coefficient is
\(q_H=\mathbb E[UH(U)]=\mathbb E\nabla H(U)\), by one-coordinate
Gaussian integration by parts. Taylor expansion in the mean shift and
Gaussian covariance interpolation therefore give

\[
 \left|\mathbb E[H(U_1)\mid C=c]
      -\mathbb EH(U)-q_H^\top\sqrt a\,z_c\right|
 \le\frac{Ma}{2}(\|z_c\|_2^2+q)
 \le\frac{M}{2n}(\|z_c\|_2^2+q).
 \tag{12}
\]

For the first step, compare \(N(\sqrt a z_c,I_q)\) to \(N(0,I_q)\)
by Taylor's theorem. For the second, interpolate covariance from
\((1-a)I_q\) to \(I_q\); the expectation derivative is half the
trace of the Hessian against \(aI_q\), at most \(Maq/2\).
Both statements are valid for bounded Hessian and the resulting Gaussian
integrability. This proves (12) uniformly as \(\eta\) tends to zero.
It explains what a nonlinear pair-statistic version of (11) must recover.

## 5. What would yield polynomial final-error absorption

Even (11) only repairs prior/posterior moment bias. The exact posterior
passive recursion still differs from the conditional dense query, as
FAST_FINITE_PASSIVE.md (29) and WEAK_PASSIVE_WIDTH_ROUTE.md explain.
Consequently a complete calibration theorem would additionally need a
same-reference scalar comparison, plus counted moment estimation, giving
the **combined** remainder

\[
 \sup_{t,x}|\widehat f_n-f_n^{\mathrm{independent}}|
 \le2b_n(\delta/256)+\frac{YA Z^q}{n}+CYn^{-10}.
 \tag{13}
\]

Neither (8) nor (12) proves (13). If (13) were established with the
specified polynomial \(A\), and if the original certificate satisfies
\(b_n(\delta/256)\ge c_*Y/\sqrt n\) with a controlled positive
\(c_*\), the required final inequality would be

\[
 A Z^q+C n^{-9}\le c_*\sqrt n.
 \tag{14}
\]

For fixed absolute \(q\), write \(Z=\log(en)+z\), \(z\ge0\),
and use \(Z^q\le(1+z)^q\log(en)^q\). The function
\(\log(en)^q/n^{1/4}\) is bounded by an absolute constant \(C_q\),
as follows by setting \(u=\log(en)\) and maximizing
\(e^{1/4}u^qe^{-u/4}\). Thus an explicit sufficient envelope for
the principal term is

\[
 n\ge[2C_qA(1+z)^q/c_*]^4.
 \tag{15}
\]

The harmless last term of (14) has its own elementary polynomial gate.
This illustrates a valid polynomial absorption after an actual extra
half-width power is gained. It neither enlarges \(b_n\) nor treats
an uncontrolled coefficient as universal. The currently supplied
calibration, curvature, posterior-to-dense, and numerical conditioning
estimates do not establish that gain.

## 6. Subsequent collaborative source-seed assessment

After Sections 1--5 were frozen, the supervisor proposed retaining a
pseudorandom seed for the source itself and recovering the same empirical
rows with exact conditional Gaussian rank corrections. The separate
SOURCE_SEED_TRANSCRIPT_CHECK.md proves the fixed-transcript probability
transfer and the revised source-ensemble amplification under explicit
interfaces. It also records why passive repetition on one source does
not suffice, and why the ensemble's memory bound changes from the current
sixth logarithmic power. That route does not establish the unproved
calibration lemma (11), and this frozen calibration attempt is not used
as an input to its probability proof.

## Provenance and claim level

The exact likelihood and calibration identities (1)--(10), Gaussian
example (12), and absorption implication (14)--(15) were derived here.
The current fast decoder, its unchanged costs, and its separate errors
were read in GAP_REFINED_PHASE_COSTS.md, FAST_FINITE_PASSIVE.md,
FAST_LOCAL_COMPOSITION.md, POLYNOMIAL_ACCURACY_ONSET.md,
WEAK_PASSIVE_WIDTH_ROUTE.md, and POLYNOMIAL_WIDTH_RESULT.md. The complete
FAST_FINITE_POSTERIOR.md and CONDITIONAL_PREFIX_CENTER.md were also read.
The explicitly authorized integrated GENERAL_DENSE_COMPARISON.md was
read completely; no sources linked from it outside the authorization
were fetched. UNBOUNDED_COMPRESSOR_BRIDGE.md was located but not used.
The required conjecture, rigorous-proof, and canonical-notation skills,
including neural conventions, were applied. No experiment, Git action,
other-study search, or sibling output was used. Only this note is owned
by this subtask.
