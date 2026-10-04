# Check of the width-doubling profile and coupling attempts

2026-10-03. Coordinator reconstruction of complete scoped route notes.
This is a collaborative internal check, not an independent promotion
review. The coordinator supplied the bounded-variation and signed
factorization ideas to the profile author. The coupling author separately
checked the profile's Gaussian estimates, bootstrap implication and
normalizations. Neither check establishes the requested trained theorem.

Complete checked sources and frozen hashes:

- WIDTH_DOUBLING_COUPLING_ROUTE.md:
  `ed5958fdb0ef5a947d6752d765fa6610c34d31fee7b8c51f5af9e813a03b2d4e`.
- WIDTH_DOUBLING_PROFILE_ROUTE.md:
  593fc1472832dead0f121005abc7c459761ca51471688aa28bcdf96c41894331.

The current study's previously read physical-tube, cavity and
self-averaging derivations supply the explicitly conditional inputs.
No other study or external scientific source was used. The current
manuscript sources are unchanged. No experiment, Git write or manuscript
edit was performed.

**Outcome:** the exact finite calculations and the abstract conditional
estimates below check. Applying them to the entire trained signed edge
response remains unproved. The canonical width-doubling bound has not
been obtained, and no canonical-network lower bound has been obtained.

## 1. Endpoint embeddings and alternative couplings

The duplicated embedding preserves the entire prediction trajectory.
If \(Dv=(v,v)\), its hidden matrix is

\[
 W^{\rm dup}={1\over2}
 \begin{pmatrix}W&W\\W&W\end{pmatrix}.
\]

It maps \(Dh\) to \(DWh\), and its canonical width-\(2n\) hidden
velocity is exactly half the width-\(n\) velocity. The read-in and
readout velocities duplicate. The initialized Gaussian law is
noncanonical: four hidden entries are identical, with variance

\[
 {1\over4n}={1\over2N},\qquad N=2n.
\]

It therefore supplies an exact dynamical identity, not the desired
random-model comparison.

In the straight covariance interpolation, writing

\[
 q=\mathbb E\phi(Z)^2,\qquad
 p_s=\mathbb E[\phi(Z^+(s))\phi(Z^-(s))],
\]

direct conditional variance calculation gives the limiting next-layer
variance

\[
 v_s={(1+s)q+(1-s)p_s\over2}.
\]

For nonconstant continuous activations and \(0<s<1\),

\[
 q-p_s={1\over2}\mathbb E|\phi(Z^+(s))-\phi(Z^-(s))|^2>0.
\]

Both endpoints have variance \(q\), while the interior generally does
not. This is an obstruction to a particular absolute-derivative proof;
it is not a lower bound on the actual endpoint difference.

The activation-commuting orthogonal matrices are correctly restricted
to signed permutations for nonaffine \(C^2\) scalar activations. The
mixed second derivative is

\[
 \phi''((Oz)_i)O_{ij}O_{ik}=0\quad(j\ne k).
\]

Surjectivity of a nonzero row and a nonzero value of
\(\phi''\) force at most one nonzero entry in each row. A negative
entry additionally requires oddness. A general block rotation changes
the activation and cannot be used as a canonical-network identity.

The fresh-Gaussian coupling formula is exact when the matrix is
independent of the feature histories. Its square-root sensitivity at
singular covariances, and the need to preserve both forward and
transpose constraints for a reused matrix, are correctly separated.
No impossibility theorem follows from either issue.

## 2. Balanced autonomous profile and its signed derivative

The profile assigns variance \(c_{ij}/N\) and hidden mobility
\(c_{ij}\), with \(c_{ij}=2(1-s)\) within blocks and \(2s\) between
blocks. Thus the actual hidden update coefficient is \(c_{ij}/N\).
This gives the shared-residual endpoint at \(s=0\) and the canonical
width-\(N\) endpoint at \(s=1/2\).

At an interior profile, the coordinate change

\[
 W_e=\sqrt{c_e/N}\,\widetilde H_e
\]

indeed makes the training field the Euclidean gradient field of the
width-scaled loss. No division by a zero variance is needed at the
endpoint, where the original weight equations remain the definition.

Each hidden layer has \(N^2/2\) edges of each type. Combining this
count with derivatives \(c'_e=\pm2\) verifies exactly the normalized
signed response in the profile note. Gaussian covariance
differentiation must satisfy its stated integrability and
expectation-differentiation hypotheses. A high-probability physical
tube alone does not justify an unlocalized expectation identity.
The coupling note was clarified accordingly. A localization would
produce derivatives of its localization function; those cannot be
discarded.

An absolute response bound cannot imply small signed contrast. The
example \(R_{ij}=b_0+b_1\sigma_i\sigma_j\) verifies this logical point
even when \(b_0\ge|b_1|\). This example is not an actual network
response or a negative width-rate theorem.

## 3. Initialization cancellation

For the bounded-value two-layer subclass, let \(\Sigma_+,\Sigma_-\)
be the two first-layer empirical covariance matrices for a training
and query pair. The second-layer covariance matrices are

\[
 Q_+=(1-s)\Sigma_++s\Sigma_-,\qquad
 Q_-=s\Sigma_++(1-s)\Sigma_-.
\]

Let \(A(Q)=\mathbb E D^2F(Q^{1/2}G)\), where
\(F(z)=\phi_2(z_1)\phi_2(z_2)\) and \(G\) is standard Gaussian.
The tagged response has factor \(1/2\), and block interchange gives

\[
 \mathcal R_{\rm out}-\mathcal R_{\rm in}
 =-{1\over4}\mathbb E\operatorname{tr}
 [ (\Sigma_+-\Sigma_-)(A(Q_+)-A(Q_-))].
\]

The factor and sign check. With three bounded derivatives,
\(D^2F\) is Lipschitz, and the positive-matrix square-root estimate
makes \(A\) one-half Hölder, including at singular matrices. Since
\(\mathbb E\|\Sigma_+-\Sigma_-\|^2=O(N^{-1})\), the displayed
contrast is \(O(N^{-3/4})\) by
\(\mathbb E\|\Sigma_+-\Sigma_-\|^{3/2}=O(N^{-3/4})\).
The earlier tagged-exchange \(O(N^{-1/2})\) estimate is also valid.
Neither is an all-training-time estimate. The broader linear-growth
activation and finite-second-query-moment scope is not established
by this bounded-value initialization calculation.

## 4. Conditional Gaussian probes and the remainder bootstrap

For controls of amplitude at most \(A\) and total variation at most
\(R\), the uniform step approximation has \(L^1\) error at most
\(R/m\). Quantization proves the stated entropy bound. The linear
Gaussian chaining sum has scale

\[
 {K\over\sqrt N}(A+\sqrt{AR}).
\]

For centered quadratic forms, the two displayed increment bounds
give both Gaussian and exponential parts of the tail. Chaining is
truncated at precision \(N^{-1/2}\); its remaining operator-norm
error has expected size \(O(KN^{-1/2})\), since the Gaussian vector
has covariance \(I_d/N\) with \(d=O(N)\). For amplitude smaller
than this precision, use the remainder directly. There is no hidden
factor \(N\) in the residual estimate. The logarithmic factor in the
quadratic bound is retained.

These are conditional kernel statements. An application needs
cavity-measurable kernels independent of the deleted Gaussian vector,
the asserted increment representations, and control of the time index.
The centered quadratic estimate does not bound an uncentered trace
mean. Such means must be retained or bounded separately.

The residual-free linearized source
\(P_a=-2p_a g_a d_a^\top/N\) is correctly retained. An activity
metric alone cannot bound its integral. Normalized physical time on
a logarithmic horizon supplies the stated alternative, subject to
the full kernel hypotheses. It is not an all-time profile theorem.

Minkowski's inequality verifies the deterministic mean-square total
variation estimates under the physical and carrier tube. If the
sharper Gaussian event, all required probes and the remainder algebra
hold at every stopped time, the inequality

\[
 u_i\le K\left[{1+\sqrt{R_i}\over\sqrt N}+u_i^2\right]
\]

closes on its continuous branch starting from zero. Indeed the maximum
forcing times \(K^2\) is \(N^{-1/4+o(1)}\), which tends to zero.
The bound on the average \(R_i^2\) then gives the asserted near-root
mean-square remainder. This implication does not establish the
profile probability event or the required exact kernels.

## 5. Trace response versus transported edge adjoint

The deterministic trace surgery is valid with trace normalized by
\(1/N\) and endpoint Hilbert--Schmidt bounds
\(\sqrt N\,N^{o(1)}\). The ambient parameter dimension may be
\(O(N^2)\); replacing these endpoint norms by a dimension-free
operator bound would be insufficient. A small-operator perturbation
contributes near-root error; a bounded-rank perturbation contributes
\(N^{-1+o(1)}\), by Duhamel and the trace inequalities.
The necessary decomposition is a hypothesis of this calculation.

The trained mobility formula has the correct normalization. In
coordinates \(\Theta=(W^1,\sqrt N W^2,\ldots,w)\), the hidden
coordinate of \(g_a=\nabla_\Theta(Nf_a)\) is
\(\delta_{a,i}h_{a,j}/\sqrt N\). If \(v\) is the transported
terminal gradient and \(\psi_e=\sqrt N v_e\), differentiating the
mobility and multiplying the prediction derivative by \(N^2\)
gives exactly

\[
 N^2\mathbb E\,\partial_{c_e}f_x(t)
 =-2\sum_a p_a\int_0^t
 \mathbb E[r_a(u)\psi_e(u)\delta_{a,i}(u)h_{a,j}(u)]\,du,
\]

whenever the expectation is justified. At the terminal time the
edge gradient factors into two endpoint fields. The transported
gradient at earlier times does not have that asserted factorization.
The Gaussian covariance derivative also contains flow second
variations. A bound on first-response traces does not identify or
cancel their signed sum.

The block-swap bilinear identity is exact, but it has not been proved
applicable to this full trained response. Likewise, bounded
\(\phi'''\) gives a Lipschitz \(\phi''\), not a quantitative
Lipschitz bound on \(\phi'''\) itself. The notes correctly leave
the second-variation comparison open without adding a fourth
derivative to the requested activation scope.

## 6. Final proof boundary

The shared-residual endpoint comparison has a separate complete proof
and reconstruction in WIDTH_DOUBLING_BLOCK_ROUTE.md and
WIDTH_DOUBLING_BLOCK_CHECK.md. The rate-equivalence argument is checked
in WIDTH_DOUBLING_RESULT_CHECK.md.

The present route notes establish neither the trained signed response
contrast nor all of its probability, localization and query-envelope
requirements. They provide exact identities, an initialization
calculation and conditional estimates, without turning these remaining
requirements into assumptions of a purported completed theorem.
