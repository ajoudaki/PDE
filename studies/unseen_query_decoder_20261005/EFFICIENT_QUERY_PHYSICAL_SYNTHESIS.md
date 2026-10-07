# Preserving learned identities in a low-information population substitution

2026-10-06. Bounded second-round author synthesis. No experiment, Git
operation, promotion, or completed efficient-decoder claim.

There are two concrete repairs to the naive population substitution.
First, the current prefix admits a unique minimum-entropy row law which
matches every retained moment within twice a proved posterior noise
tolerance. A strict-slack argument produces a finite exponential-tilt
representation and a counted rounding bound; it needs no covariance gap.
Second, a query can reuse the known moments exactly and average only its
remaining row-function component. Its statistical error depends on that
remainder and on the original noise times the reuse coefficients. This
exactly repairs the redundant-moment counterexample in
`EFFICIENT_QUERY_INFORMATION.md`.

Physical mobility geometry supplies an inverse-free propagation theorem
if those remaining moment errors can be realized as small physical
forcings. That realization is not proved for the actual unseen-query
circuit. Neither the exponential normalization nor the residual Gaussian
integrals below are free or proved efficiently evaluable.

## 1. Setup and one event controlling information and noise

Keep the original nonlinear network, depth, full spanning sphere data,
label allowance, activations, initialization, loss, physical clock,
whole-sphere norm and fitted endpoint. The target is the same inherited
dense-self-variability upper certificate \(b_n\), with compact current
state, no dense-weight oracle and no scalar-training replay at query.

The allowed information note has iid Gaussian row packets with law
\(\mu\), independent standard scalar noises \(E_r\), and updates

\[
 C_r=\frac1n\sum_{i=1}^nF_r(Z_i;C_{<r})+\eta E_r,
 \qquad |F_r|\le B,\quad B\ge1,\quad 1\le r\le P,\quad \eta>0.
 \tag{1}
\]

All row functions are the same for each row. Its information bound is

\[
 H=\frac P2\log(1+B^2/\eta^2),\qquad
 I(Z_{1:n};C_{\le P})\le H.
 \tag{2}
\]

At prefix \(c=C_{\le j}\), write \(\pi_c\) for the conditional
law of all rows, \(\pi_c^1\) for their common marginal, and
\(K(c)=D(\pi_c\Vert\mu^{\otimes n})\). The source proves an
event of probability at least \(1-\alpha\) on which, for every
prefix,

\[
 K(c)\le H/\alpha,\qquad D(\pi_c^1\Vert\mu)\le H/(\alpha n).
 \tag{3}
\]

The scalar noise is not independent after conditioning on \(c\).
To control it correctly, set \(S_E=\sum_{r=1}^PE_r^2\).
The conditional expectations \(\mathbb E[S_E\mid C_{\le j}]\)
form a nonnegative martingale of mean \(P\). The same first-crossing
argument as in the information note gives, with probability at least
\(1-\beta\),

\[
 \mathbb E[S_E\mid C_{\le j}]\le P/\beta
                 \quad\text{for every }j\le P.
 \tag{4}
\]

For example, stop at the first crossing of \(P/\beta\); conditional
expectation of the terminal nonnegative martingale there is at least
\(P/\beta\). Summing over the disjoint first-crossing events bounds
their total probability by \(\beta\).

Henceforth work on the intersection of (3) and (4), of probability at
least \(1-\alpha-\beta\), and put

\[
 T=\sqrt{P/\beta},\qquad h=H/(\alpha n).
 \tag{5}
\]

For fixed \(c\), abbreviate the \(j\)-vector of retained row tests
as \(F(z)=(F_r(z;c_{<r}))_{r\le j}\). Taking the conditional
expectation of (1), using exchangeability, proves

\[
 \left|\int F_r\,d\pi_c^1-c_r\right|
   =\eta|\mathbb E[E_r\mid c]|
   \le\eta\sqrt{\mathbb E[S_E\mid c]}\le\eta T.
 \tag{6}
\]

This is simultaneous at every prefix on the same event. There is no
inverse power of the scalar-noise scale in its error.

## 2. A finite constrained tilt exists, even with dependent moments

For a current prefix define the optimization problem

\[
 \min_\nu D(\nu\Vert\mu)
 \quad\text{subject to}\quad
 \left|\int F_r\,d\nu-c_r\right|\le2\eta T
                      \quad(1\le r\le j).
 \tag{7}
\]

The minimization is over probability measures. By (3) and (6),
\(\pi_c^1\) is feasible with entropy at most \(h\) and lies a
distance at least \(\eta T\) from each boundary of the constraint
box. This derived slack is why no strict-interior hypothesis is needed.

Define, for \(\lambda\in\mathbb R^j\),

\[
 \psi(\lambda)=\log\int e^{\lambda^TF(z)}\,\mu(dz),\qquad
 J(\lambda)=\lambda^Tc-2\eta T\|\lambda\|_1-\psi(\lambda).
 \tag{8}
\]

Boundedness of \(F\) makes \(\psi\) finite and differentiable
for every finite \(\lambda\), with
\(\nabla\psi(\lambda)=\int F\,d\nu_\lambda\), where

\[
 \frac{d\nu_\lambda}{d\mu}(z)
                      =\exp(\lambda^TF(z)-\psi(\lambda)).
 \tag{9}
\]

The entropy inequality applied to \(\pi_c^1\) gives
\(\psi(\lambda)\ge\lambda^T\int Fd\pi_c^1-D(\pi_c^1\Vert\mu)\).
Using (6),

\[
 J(\lambda)\le h-\eta T\|\lambda\|_1,
 \qquad J(0)=0.
 \tag{10}
\]

Thus the continuous concave function \(J\) attains a maximum at a
finite \(\lambda_*\), and a maximizer can be chosen with

\[
                 \|\lambda_*\|_1\le h/(\eta T).
 \tag{11}
\]

To see attainment directly, outside any radius greater than
\(h/(\eta T)\), (10) is negative, while the value at zero is zero.
Maximize the continuous function on that closed finite-dimensional ball.

At a maximizer, the first-order subgradient condition gives a vector
\(s\) with \(s_r\in[-1,1]\),
\(s_r=\operatorname{sign}(\lambda_{*,r})\) whenever that coordinate
is nonzero, such that

\[
       \int F\,d\nu_{\lambda_*}=c-2\eta T s.
 \tag{12}
\]

This follows equivalently by taking both one-sided coordinate directional
derivatives of \(J\). It proves feasibility of \(\nu_{\lambda_*}\).
Since \(\lambda_*^Ts=\|\lambda_*\|_1\),

\[
 D(\nu_{\lambda_*}\Vert\mu)
 =\lambda_*^T\int Fd\nu_{\lambda_*}-\psi(\lambda_*)
 =J(\lambda_*).
 \tag{13}
\]

For every feasible \(\nu\), the entropy inequality instead gives

\[
 D(\nu\Vert\mu)
 \ge\lambda_*^T\int Fd\nu-\psi(\lambda_*)
 \ge J(\lambda_*).
 \tag{14}
\]

Equations (13)--(14) prove that the tilted law solves (7), with entropy
at most \(h\). Strict convexity of \(u\log u\) proves uniqueness
of its density: two distinct minimizing densities would have a feasible
midpoint with smaller entropy. Multipliers themselves need not be unique.
No covariance rank or eigenvalue assumption occurred in the proof.
If \(h=0\), (10) selects \(\lambda_*=0\); an empty prefix likewise
gives \(\nu_* =\mu\).

This repairs more than feasibility alone: it gives a finite description
using the current row circuit and \(j\) multipliers. It does not require
query inputs to be known during acquisition.

## 3. Precision of that description, and its computational limitation

Let \(\widetilde\lambda\) be a rounded multiplier vector and put
\(\Delta=\|\widetilde\lambda-\lambda_*\|_1\). Since
\(|F_r|\le B\),

\[
 |\psi(\widetilde\lambda)-\psi(\lambda_*)|\le B\Delta,
 \qquad
 \left|\log\frac{d\nu_{\widetilde\lambda}}{d\nu_*}\right|
                                                    \le2B\Delta.
 \tag{15}
\]

The first inequality follows by bounding the ratio of the two
normalization integrands between \(e^{-B\Delta}\) and
\(e^{B\Delta}\), then integrating. Thus, with total variation
defined as a supremum over events,

\[
 \|\nu_{\widetilde\lambda}-\nu_*\|_{\rm TV}
                  \le e^{2B\Delta}-1.
 \tag{16}
\]

For every \(|G|\le B_G\), its expectation changes by at most
\(2B_G(e^{2B\Delta}-1)\). In particular it suffices to choose
\(\Delta\le\varepsilon/(8B\max\{1,B_G\})\) for an
expectation error at most \(\varepsilon\), when
\(0<\varepsilon\le1\). Rounding each of \(j\) coordinates
with error at most \(\Delta/j\) ensures that total error.

For the retained moments themselves, taking
\(\Delta\le\eta T/(8B\max\{1,B\})\), when \(\eta T\le1\),
keeps the rounded law within a \(3\eta T\) moment box. This is
obtained by applying (16) to each \(F_r\) and adding its error to
(12). One can impose the stronger minimum of these two rounding bounds.

Together with (11), each multiplier therefore needs a number of bits
bounded by a constant times

\[
 1+\log(1+h/(\eta T))+\log(1+j)+\log(1+B)
       +\log(1+B_G)+\log(1/\varepsilon)
       +\log(1+1/(\eta T)).
 \tag{17}
\]

All terms are absolute-polylogarithmic under the supplied program bounds
and inverse-polynomial requested error, for fixed confidence factors.
The current (j)-multiplier description therefore has a counted finite-bit
version for bounded row-test expectations. The expectation must still be
evaluated with a correspondingly budgeted error.

In particular, (17) does not provide fast acquisition of \(\lambda_*\)
or fast evaluation of \(\psi\). The normalization in (8) is an
integral of an exponential of a growing row circuit, and its magnitude
and conditioning cannot be discarded. The finite description is not
an integration oracle or a polynomial-time algorithm.

## 4. Reuse the known moments and average only a residual

There is a simpler identity-preserving rule which needs no tilted-law
integration. Fix a prefix \(c\), a query/time pair, and a row test
\(G(z)\). Choose any coefficient vector \(a\in\mathbb R^j\)
using those quantities, independently of the unseen full row array, and
define

\[
 R(z)=G(z)-a^TF(z),\qquad
 d_G(c)=a^Tc+\int R\,d\mu.
 \tag{18}
\]

The retained moments are used exactly. Only the remaining row function
is replaced by its prior expectation. This rule does not rerun a
training scalar update. It does not assume that a suitable \(a\)
can be found efficiently.

Suppose the oscillation of \(R\) is at most \(2B_R\); that is,
its supremum minus infimum is at most \(2B_R\). Subtracting their
midpoint does not change an empirical-minus-prior discrepancy. The
conditional entropy inequality in the information note therefore gives

\[
 \mathbb E_{\pi_c}\left|
       \frac1n\sum_iR(Z_i)-\int R\,d\mu\right|
       \le B_R\sqrt{\frac{2[K(c)+\log2]}n}.
 \tag{19}
\]

But (1) also gives the following exact identity on the joint posterior
of rows and scalar noises:

\[
 \frac1n\sum_iG(Z_i)-d_G(c)
 =\frac1n\sum_iR(Z_i)-\int R\,d\mu-\eta a^TE_{\le j}.
 \tag{20}
\]

Conditional Cauchy--Schwarz and (4) bound the last term, giving

\[
 \mathbb E\left[\left|
       \frac1n\sum_iG(Z_i)-d_G(c)\right|\mathrel{\Big|}c\right]
 \le B_R\sqrt{\frac{2(H/\alpha+\log2)}n}
                              +\eta T\|a\|_2.
 \tag{21}
\]

The same event supports (21) for every prefix and every deterministic
choice of query test and coefficients. There is no union over query
points. Fresh independent passive-query coordinates may be appended
to the row law exactly as in the information note. A fresh scalar
noise term contributes additionally at most \(\eta\mathbb E|E'|
\le\eta\) to the right side.

The bounded-oscillation hypothesis may be replaced by the explicit
sub-Gaussian condition

\[
 \log\int e^{\lambda(R-\int R\,d\mu)}d\mu
                    \le\lambda^2\sigma_R^2/2
                   \quad\text{for all real }\lambda.
 \tag{22}
\]

Then replace \(B_R\) in (19)--(21) by \(\sigma_R\). Independence
gives the empirical log-moment bound \(\lambda^2\sigma_R^2/(2n)\);
applying the entropy inequality to the exponential of the absolute
discrepancy adds \(\log2\), and optimizing \(\lambda\) proves
the claim. A variance bound alone does not imply (22).

Equation (21) is an estimate in a quotient of row functions by the span
of the retained tests, with the original small noise controlling the
reuse coefficients. Large \(\|a\|\) does not enter the sampling
term. In contrast, applying a raw range estimate to \(G\) would
charge that entire coefficient size there. There is no assertion that
the physical new-query residuals have small oscillation or satisfy
(22) with a useful constant.

For example, if \(G=a^TF+b\) exactly, (18) gives
\(d_G=a^Tc+b\) and (21) costs only \(\eta T\|a\|_2\).
This preserves every such affine identity automatically.

## 5. Exact repair of the redundant-moment instability

In the information note's counterexample, the retained mean is
\(C=M+\eta E\), the new mean is \(D=M+\eta E'\), and the
output is \(U=\tanh((D-C)/\sigma)\), with
\(\eta=\sigma^2\). The naive population choice \(d=0\)
produces an order-one error on typical histories.

Rule (18) takes \(G=F\), \(a=1\), \(R=0\), so
\(d_G=C\) and its output is exactly zero. Conditional on a prefix
satisfying (4),

\[
 \mathbb E[|U|\mid C]
 \le\frac\eta\sigma\bigl(\mathbb E[|E|\mid C]
                                  +\mathbb E|E'|\bigr)
 \le\sigma(T+1).
 \tag{23}
\]

The inequality uses \(|\tanh u|\le|u|\), which follows by
integrating its derivative, bounded by one, from zero. Thus the
inverse-\(\sigma\) gain multiplies the original noise, not the
root-width empirical fluctuation. This repairs exactly the
counterexample's identity failure. It is not a proof that every
inverse-noise factor in the neural row circuit has this form.

More generally, for a scalar output \(\Phi(c,z)\) which is
\(L_\Phi\)-Lipschitz in \(z\), (21) yields expected output error
at most \(L_\Phi\) times its right side, with the extra scalar-noise
term if present. Markov's inequality converts this to any fixed
conditional failure probability \(p>0\), at an additional factor
\(1/p\). Combining that conditional interval with the existing
posterior robust-center interval gives the same whole-query transfer
as the information note. A sufficient scale condition for this scalar
case is explicitly

\[
 L_\Phi\left[B_R\sqrt{\frac{H+1}{n}}
                    +\eta(T\|a\|_2+1)\right]=O(b_n),
 \tag{24}
\]

with fixed confidence factors included in the constant. This is an
exact conditional lemma, not an assertion that the actual full query
program satisfies (24). In a multistep query, subsequent row tests
depend on the earlier random query summaries. Applying (21) after
substituting those random summaries would require another argument;
they are not fixed functions of the training prefix.

## 6. What physical contractivity can propagate

The response result in `EFFICIENT_QUERY_DIRECT.md` supplies a precise
way to avoid inverse-noise sensitivity *once a perturbation has been
realized in physical parameter space*. The following finite-perturbation
lemma records exactly the required geometry.

Use mobility coordinates
\(\theta=(A/\sqrt n,W^{(2)},\ldots,W^{(L)},w/\sqrt n)\), loss
\(\mathcal L(\theta)=\|e(\theta)\|_2^2\), and the full parameter
Jacobian \(\mathcal J\) with columns \(\nabla e_a\). Suppose
a differentiable homotopy of paths solves

\[
 \dot\theta_u(t)=-\nabla\mathcal L(\theta_u(t))+u q(t),
 \qquad \theta_u(0)=\theta_0+u v,
 \qquad 0\le u\le1,
 \tag{25}
\]

where \(q\) is a physical forcing with finite integral norm. Assume
every path in this homotopy has the original sphere feature/mixer and
readout RMS bounds, and its residual curvature satisfies

\[
 \sup_{u\in[0,1]}2\int_0^\infty
 \left\|\sum_a e_a(\theta_u(t))\nabla^2e_a(\theta_u(t))
                                                    \right\|_{\rm op}dt
 \le M.
 \tag{26}
\]

Then

\[
 \sup_{t\ge0,v_{\rm query}\in S^{d-1}}
 |f(\theta_1(t),v_{\rm query})-f(\theta_0(t),v_{\rm query})|
       \le C e^M\left(\|v\|_2+\int_0^\infty\|q(t)\|_2dt\right).
 \tag{27}
\]

To prove it, differentiate (25) in \(u\). The resulting equation for
\(z_u=\partial_u\theta_u\) has generator
\(-2(\mathcal J\mathcal J^T+\sum_a e_a\nabla^2e_a)\),
forcing \(q\), and initial value \(v\). The positive first part
is contractive. The ordered response expansion from the direct note,
or its integral norm inequality, bounds its propagator by \(e^M\).
Variation of constants consequently bounds \(\|z_u(t)\|_2\)
by the right side of (27) without its constant \(C\).

The uniform query-gradient bound
\(\|\nabla_\theta f(\theta_u(t),v_{\rm query})\|_2\le C\)
follows from the outer-product gradient formulas: the forward RMS
bounds control features, while the mixer operator and bounded activation
derivative bounds propagate the readout RMS bound backwards at every
sphere query. Integrate
\(\partial_u f=\nabla_\theta f^Tz_u\) over \(0\le u\le1\)
to obtain (27). If both predictions have limits, taking \(t\to\infty\)
includes their endpoints. Alternatively an available prediction-tail
bound handles the terminal frozen extension.

For an actual good dense trajectory the inherited residual/carrier
interface bounds the action by \(C Y(1+Y\sqrt{\log(en)})\).
It does not establish (26) for arbitrary interpolated or forced paths.
Nor has replacing the remaining query row moments in (18) been
realized as a forcing \(q\) with a small integral norm. Both facts
must be proved before using (27) for this population substitution.
One cannot identify a small moment error with \(\|v\|+\int\|q\|\)
without constructing that physical lift.

If such a lift had size \(\varepsilon_n\), its precise sufficient
accuracy condition would be \(e^M\varepsilon_n=O(b_n)\).
Merely labeling both expressions \(n^{-1/2+o(1)}\) would not prove
this comparison with the fixed inherited certificate. This makes the
remaining physical estimate quantitative, without introducing an
inverse observation-noise scale.

## 7. Result and remaining neural-specific bridge

The all-prefix event, strict-slack entropy minimizer, finite dual bound,
rounding estimate, compensated row-test bound, counterexample repair,
and physical-forcing lemma are proved above. Their hypotheses and
conditional status are explicit. None changes the original label
allowance or freezes hidden feature learning.

The candidate mechanism is now concrete: preserve learned moment
identities, substitute population averages only for the remaining
components, and propagate those errors in the mobility geometry.
What remains to connect it to the original decoder is a neural-specific
description of those remaining components and their causal propagation.
It must handle new query cross-covariances and adaptive summary calls;
matching the training moments alone does not determine them. It must
also bound rounding errors in the retained prefix, rather than only
rounding multipliers for a fixed ideal prefix.

A precise possible reopening target is relative concentration in the
row-covariance geometry: feasible positive-semidefinite query Grams
constrain cross moments along almost-null history directions, and those
constraints may cancel apparent inverse-noise gains. Such a result must
control relative empirical errors and the physical mean/covariance
coupling, not just positive semidefiniteness. The present entropy bounds
give absolute test deviations; they do not prove that relative
concentration estimate for the nonlinear row circuit. This target is
recorded only, without a further derivation in this round.

Separately, the remaining Gaussian expectations and, if used, the tilt
optimization/normalization require deterministic polynomial-time
algorithms with counted workspace. Neither a finite dual representation
nor the existence of a small physical sensitivity bound supplies those
algorithms. Thus the full efficient decoder remains open, with a more
specific identity-preserving substitution available for further work.

## 8. Provenance and check status

New scientific input read completely:
`EFFICIENT_QUERY_INFORMATION.md`, SHA-256
`f8dad05300032801a45d47161127c99d3718eefbf61262e5c7be92c9037129a0`.
The already written/read `EFFICIENT_QUERY_DIRECT.md` has SHA-256
`8a027e2e2b92f538aecf2bde4fc305e9f064fd3f32cea0364b8e9b11331f840b`.
The six original allowed notes and the previously read research,
rigorous-proof and explicit notation-fallback instructions remain the
other inputs. No new other-study, archive, external-source or other-route
reading was performed. The supervisor's followups supplied the request
to test a constrained tilt and emphasized the noise, precision and
unresolved new-covariance issues.

This is an author derivation, not an independently checked or promoted
result. Only this new assigned file was edited in this round. No
experiment, numerical integration or Git operation was performed.
