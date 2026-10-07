# Reconstruction of the Gaussian harmonic initialization synthesis

2026-10-06. **PASS for the complete circle initialization module, taking
the stated BSS theorem as the authorized external hypothesis.** The
finite-width second-jet moment identities, tagged three-Gaussian limit,
and single-origin continuation exponent also reconstruct. This does not
establish the full nonlinear training comparison.

This is a bounded same-study reconstruction with prior task context
retained, not an independent blind attempt or a promotion review. All five
assigned files were read completely. An initially truncated combined tool
return was repaired by reading each scientific file separately. No linked
study, unassigned report, archived book, or external scientific source was
opened. Current `AGENTS.md` and workflow Part 1 were reread; the proof and
research skills and the previously read notation contract were reused.
The required canonical-notation skill was previously permission denied;
the supervisor-authorized explicit-notation fallback remains in effect.
No experiment or Git operation was performed. Only this report was written.

## Frozen inputs and scope

| Complete input | SHA-256 |
| --- | --- |
| `GAUSSIAN_INITIALIZATION_RESULT.md` | `1bd076c5061aae43385c779fe8da2f38f869dbb765b0fcf2424f634cd23777da` |
| `GAUSSIAN_HARMONIC_JETS.md` | `8615cb31fb586954e2330e8531c5a224017f79be8f4e82725a10830bb18a74af` |
| `GAUSSIAN_ENVELOPE_TRANSFER.md` | `0c198bc39d7a66bce034e5693a9ca5bb107201d6fb6c4c157ac7fa824e689762` |
| `GAUSSIAN_SYNTHETIC_SELECTION.md` | `3eb17a6963242bf9336e645a203fd6e67983e626de0ef39a85d917cb44a9e384` |
| `GAUSSIAN_JET_CONTINUATION.md` | `e69d7f8542eb0aae29bbee829121cf61dea00f32b264de7744123e5e9aae28bc` |

The selection hash recorded in the envelope note agrees with the assigned
selection input. The primary audit target is Section 2 of the synthesis:
deterministic tanh rows on the circle, an explicit positive definite
feature metric, uniform initial-kernel error, and retained storage.
The general-dimensional quadrature module and the maintained Gaussian
compiler are cited by the supplied notes but their proofs are outside this
assignment. They are not needed for the circle theorem and were not
independently verified here.

## 1. The circle theorem and its exact rank

Let \(a\sim\mathcal N(0,I_2)\),
\(v_\theta=(\cos\theta,\sin\theta)\), and
\(h_a(\theta)=\tanh(a^Tv_\theta)\). The target is the initial
population pairing

\[
K(\theta,\psi)=\mathbb E[h_a(\theta)h_a(\psi)].
\]

This matches the maintained first-layer normalization for inputs
\(x=\sqrt2v_\theta\). The claim is a deterministic selection of
\(q\) rows and a positive definite \(q\)-by-\(q\) matrix \(H\)
such that

\[
\sup_{\theta,\psi}|h_C(\theta)^THh_C(\psi)-K(\theta,\psi)|
\le\varepsilon,
\quad q=O([\log(C/\varepsilon)]^{3/2}),
\]

for \(0<\varepsilon\le1/2\). The metric includes the required
normalization; no missing additional division by \(q\) is needed.

For the Fourier coefficients
\(c_j(a)=\int h_a(\theta)e^{-ij\theta}\,d\theta/(2\pi)\),
write \(a=r(\cos\alpha,\sin\alpha)\). Then
\(c_j(a)=t_j(r)e^{-ij\alpha}\), where \(t_j\) is real,
\(t_{-j}=t_j\), and even modes vanish. Gaussian polar angle is uniform
and independent of the Rayleigh radius, so

\[
\mathbb Ec_j=0,\qquad
\mathbb E[c_j\overline{c_k}]=\mathbf1_{\{j=k\}}\lambda_j.
\]

For every positive odd \(j=2l+1\), the Taylor recurrence from
\(\tanh'=1-\tanh^2\) shows that its coefficient of degree
\(2l+1\) is \((-1)^l b_l\) with \(b_l>0\). Lower-degree
powers cannot contribute to Fourier mode \(j\), and the degree-\(j\)
cosine power has coefficient \(2^{-j}\). Thus
\(t_j(r)=2^{-j}(-1)^lb_lr^j+O(r^{j+2})\). It is nonzero on a
positive-measure interval, proving \(\lambda_j>0\).

For an integer cutoff \(J\ge1\), let \(e_J\) be the radial
envelope in the next section. The proposed real source basis consists
of \(\operatorname{Re}c_j,\operatorname{Im}c_j\) for positive odd
\(j\le J\), together with \(1,e_J\). Its dimension is exactly

\[
R=2\#\{1\le j\le J:j\text{ odd}\}+2\le J+3.
\]

Indeed, distinct nonzero angular frequencies are orthogonal, and each
real sine/cosine coordinate has squared norm \(\lambda_j/2>0\).
They are orthogonal to all radial functions. The two radial functions
are independent because \(e_J\) is continuous and nonconstant on the
full-support radial distribution. Positivity at positive radii alone
would not prove this, but the displayed formula is strictly increasing
in radius and vanishes at zero, which does.

An explicit orthonormal basis makes the whitening step particularly
transparent:

\[
\sqrt{2/\lambda_j}\operatorname{Re}c_j,
\quad\sqrt{2/\lambda_j}\operatorname{Im}c_j,
\quad 1,
\quad\frac{e_J-\mathbb Ee_J}
 {\sqrt{\mathbb Ee_J^2-(\mathbb Ee_J)^2}}.
\]

All denominators are strictly positive by the preceding arguments. There
is no unresolved numerical rank cutoff in this particular application.
The source truncation
\(h_{a,J}(\theta)=2\sum_{j>0,\ j\le J}
\operatorname{Re}(c_j(a)e^{ij\theta})\) belongs to this real space
for every angle.

## 2. Pointwise envelope, Gaussian tails, and computability

For \(|\operatorname{Im}z|\le\pi/4\), the elementary formula
for \(|\tanh z|^2\) in the source bounds it by one. Consequently
\(u\mapsto\tanh(r\cos u)\) is analytic and bounded by one on
the closed strip of width
\(s(r)=\operatorname{arsinh}(\pi/(4r))\), when \(r>0\).
Contour shifting of a periodic Fourier coefficient therefore gives
\(|t_j(r)|\le e^{-|j|s(r)}\). The closed strip stays away from
the poles of tanh, so this contour argument has no boundary singularity.

Summing both signs of all omitted frequencies gives the pointwise bound

\[
\sup_\theta|h_a(\theta)-h_{a,J}(\theta)|
\le e_J(a):=\frac{2u(r)^{J+1}}{1-u(r)},
\qquad
u(r)=\frac{4r}{\pi+\sqrt{\pi^2+16r^2}}.
\]

For \(r>0\), \(u(r)=e^{-s(r)}\); at zero, the formula gives
\(e_J=0\). It is a continuous computable function without a division
by zero at the origin. Since \(u\) increases strictly from zero to
one, so does \(e_J\).

Writing \(c_0=\operatorname{arsinh}(\pi/4)>0\), the bounds
\(s(r)\ge c_0/(1+r)\) and
\((1-e^{-s})^{-1}\le1+s^{-1}\) give

\[
e_J(a)\le C(1+r)\exp[-c_0J/(1+r)].
\]

Split its squared Rayleigh expectation at \(r=J^{1/3}\). Below
that radius, the exponential is at most
\(\exp(-cJ^{2/3})\), with a polynomial prefactor. Above it,
discard the exponential and integrate
\((1+r)^2r e^{-r^2/2}\); the result has the same form. Absorbing
the polynomial factors into a weaker exponential proves

\[
\mathbb Ee_J^2\le C e^{-cJ^{2/3}}.
\]

The Fourier covariance bound in the harmonic note also reconstructs:
split at \(r=j^{1/3}\) to obtain
\(\lambda_j\le2e^{-j^{2/3}/2}\). Weighted Cauchy--Schwarz with
weights \(j^{-2}\) then bounds the expected squared uniform tail.
Absolute summability justifies the Fourier expansion of \(K\).

All moments needed for the displayed orthonormal basis are effective
finite-dimensional Gaussian/angular integrals. Fourier coefficients are
bounded, and the envelope grows at most linearly in radius. This gives
effective Gaussian second-moment tails; explicit formulas give effective
evaluation and continuity bounds on finite boxes. These suffice for
certified quadrature. Increasing the accuracy of positive quantities
\(\lambda_j\) and \(\operatorname{Var}(e_J)\) eventually
certifies a positive lower bound, so their inverse square roots are
computable. The precision and conditioning may be poor, but termination
does not require a decidable test for equality of an arbitrary computable
real. The source correctly makes no favorable bit-complexity claim.

## 3. Selection, corrected metric, and the selected-kernel bound

For the orthonormal source vector \(p\), effective positive Gaussian
quadrature supplies a finite frame matrix
\(M_Q\) with \(7I/8\preceq M_Q\preceq9I/8\). This follows
by separately controlling its omitted second-moment tail and bounded-box
quadrature error. The finite pool need not have size controlled by \(R\).

Whitening this finite frame makes its sum of outer products exactly
the identity. The authorized BSS statement with parameter 16 then gives
at most \(16R\) positive selected weights and a spectral factor
\(25/9\). Undoing the whitening and multiplying the weights by
\(6/5\) yields

\[
\frac{21}{20}I\preceq G:=P^TDP\preceq\frac{15}{4}I,
\]

where \(P\) evaluates the source basis at the selected marks and
\(D\) is positive diagonal. These arithmetic constants are correct.
Their strict margins allow positive rational weights to be found by a
terminating certified search, even if exact-real comparison steps in a
particular BSS implementation are not decidable. No efficient search
bound is proved or needed for the stated retained-size result.

Set \(Z=D^{1/2}P\) and use the source's corrected matrix

\[
H=D^{1/2}[ZG^{-2}Z^T+I-ZG^{-1}Z^T]D^{1/2}.
\]

The columns of \(ZG^{-1/2}\) are orthonormal. On their range, the
bracket has the eigenvalues of \(G^{-1}\); on its orthogonal
complement it is the identity. Thus

\[
\tfrac14D\preceq H\preceq D,
\qquad P^THP=I.
\]

In particular \(H\) is positive definite and exactly reproduces
the true source inner product. The constant-accuracy quadrature was
used to find marks; it has not replaced the exact population
normalization. Using approximate population whitening without a
separate error term would be invalid, but the source does not do so.

For the residual \(r_\theta(a)=h_a(\theta)-h_{a,J}(\theta)\),
the diagonal matrix \(D\) and the pointwise envelope imply

\[
\|(r_\theta)_I\|_H^2
\le(r_\theta)_I^TD(r_\theta)_I
\le(e_J)_I^TD(e_J)_I
\le4(e_J)_I^TH(e_J)_I
=4\mathbb Ee_J^2.
\]

The last equality is justified because the original envelope is in
the source span. No coordinatewise monotonicity of the non-diagonal
matrix \(H\), random sampling of the marks, or bounded point
evaluation on an arbitrary \(L^2\) remainder has been assumed.

Let \(\eta=\|e_J\|_{L^2}\). The population residual norm is
at most \(\eta\), its selected norm is at most \(2\eta\),
and the source approximant has population and selected norms at most
\(1+\eta\). Expanding a pairing, canceling the exactly reproduced
source-source term, and applying Cauchy--Schwarz to the two mixed terms
and the residual-residual term gives

\[
\sup_{\theta,\psi}
|h_C(\theta)^THh_C(\psi)-K(\theta,\psi)|
\le6\eta+11\eta^2.
\]

Choosing \(\eta\le\varepsilon/17\) suffices for the stated
range of \(\varepsilon\). The exponential envelope bound permits
\(J=O([\log(C/\varepsilon)]^{3/2})\), hence
\(q\le16R=O([\log(C/\varepsilon)]^{3/2})\). The retained
rows and metric contain \(2q+q^2=O([\log(C/\varepsilon)]^3)\)
reals. All temporary source functions, marks beyond the selected rows,
and evaluation matrices can be discarded after compilation.

This completes the claimed initialization module. It is a deterministic,
dataset-blind construction of actual tanh rows and a feature metric,
with uniform initial population-kernel accuracy. It is not an ordinary
unweighted random-feature rule, a complete two-hidden-layer model, a
runtime optimizer, or a comparison of trained trajectories. A pool larger
than the target dense width, expensive preprocessing, and large precision
requirements remain compatible with the explicitly stated real-coordinate
storage theorem.

## 4. Low-order second jet: exact moments and limiting law

For one training point \(x_1=\sqrt d\,e_1\), zero readout, and
feature time \(ds/dt=2(y-f_n(x_1))\), write
\(h_i=\tanh(a_{i1})\), \(v=Wh\),
\(b(z)=\tanh(z)\tanh'(z)\), and \(R=W^Tb(v)\).
The empirical variance \(q_n=\|h\|_2^2/n\) in this paragraph is
the harmonic note's variance, not the selected neuron count above.

At zero readout the first derivatives of \(A,W\) vanish, while
\(w'=\tanh(v)\). Differentiating the first-layer feature equation
therefore gives

\[
\partial_s^2 h_i(0,\theta)
=\cos\theta\,\tanh'(a_i\cdot v_\theta)
  \tanh'(a_{i1})R_i.
\]

There is no Taylor-coefficient factor of two. The physical second
derivative is \(4y^2\) times this expression, because the term
containing the first feature derivative vanishes.

Conditional on the full first layer, each row of \(W\) is Gaussian
with entry variance \(1/n\). One integration by parts gives
\(\mathbb E[W_{ri}b(v_r)]=h_i\zeta(q_n)/n\), where
\(\zeta(u)=\mathbb E b'(\sqrt uG)\). Two integrations by parts
give, with \(\beta(u)=\mathbb E b(\sqrt uG)^2\) and
\(\chi(u)=\mathbb E(b^2)''(\sqrt uG)\),

\[
\mathbb E[W_{ri}W_{rj}b(v_r)^2]
=\frac{\delta_{ij}}n\beta(q_n)
 +\frac{h_ih_j}{n^2}\chi(q_n).
\]

Summing equal and unequal row terms yields exactly

\[
\mathbb E_W R_i=h_i\zeta(q_n),\qquad
\mathbb E_W[R_iR_j]
=\delta_{ij}\beta(q_n)
 +h_ih_j[(1-1/n)\zeta(q_n)^2+\chi(q_n)/n].
\]

Thus the finite-width formulas retain both matrix reuse and the random
empirical variance. The subsequent harmonic moment formulas follow by
integrating the bounded angular multiplier; fixed-order Gaussian
polynomial envelopes justify the interchanges.

For the limiting-law claim, Gaussian row regression conditional on
\(h,v\) gives the exact representation

\[
R\overset d=hT_n/q_n+\sqrt{B_n}
 \left(I-\frac{hh^T}{nq_n}\right)\gamma,
\]

with \(T_n=n^{-1}\sum_rv_rb(v_r)\),
\(B_n=n^{-1}\sum_rb(v_r)^2\), and an independent standard
Gaussian vector \(\gamma\). The coefficient and covariance factors
are correct: each conditioned row has covariance
\(n^{-1}(I-hh^T/(nq_n))\).

Let \(q_*=\mathbb E\tanh(G)^2>0\). Variance bounds for bounded
averages give \(q_n\to q_*\),
\(T_n\to q_*\zeta(q_*)\), and \(B_n\to\beta(q_*)\) in
probability. Here \(zb(z)\) is bounded and its mean is
\(q_*\zeta(q_*)\) by integration by parts. For a fixed tagged
coordinate, the removed Gaussian projection has variance
\(h_i^2/(nq_n)\to0\). The coupled tagged response consequently
converges to

\[
R_* =\zeta(q_*)\tanh(a_1)+\sqrt{\beta(q_*)}\,\Gamma,
\]

where \(a_1,a_2,\Gamma\) are independent standard Gaussians.

The claimed mean-square upgrade is justified. Conditional row summands
have means \(O(n^{-1})\), second moments \(O(n^{-1})\), and
fourth moments \(O(n^{-2})\), uniformly in the first layer.
The centered fourth-power expansion gives uniformly bounded fourth
moments of their sum, and the target also has a bounded fourth moment.
This supplies uniform integrability of the squared coupling error.
The angular multiplier is bounded by one, so convergence holds in
expected squared uniform angular norm for this tagged second jet.
The same argument handles any fixed number of tagged neurons. It does
not give an exact finite-width Gaussian replacement or growing-order
uniformity.

The nonzero response term is essential. At the training direction,
\(\mathbb E[h_a(0)J_*(0)]
=\zeta(q_*)\mathbb E[\tanh(G)^2\tanh'(G)^2]>0\), since
\(q_*\zeta(q_*)=\mathbb E[Z\tanh(Z)\tanh'(Z)]>0\) for
\(Z\sim\mathcal N(0,q_*)\). The source's harmonic blocks,
including their response-square term, agree with this law.

## 5. Continuation calculation and remaining boundaries

The disk-to-rectangle map in the continuation note sends zero to time
zero and \(\xi_*=2\eta/(1+\eta^2)\) to time \(T\).
Its logarithm has the stated right-half-plane branch; the real and
imaginary bounds place its image inside the assumed rectangle.
Cauchy's coefficient bound consequently gives the source's tail
\(M\xi_*^{K+1}/(1-\xi_*)\).

Writing \(a=e^{-\pi T/(4r)}\) and \(c=e^{-\pi/2}\), direct
substitution into \((1-\eta)^2/(1+\eta^2)\) gives

\[
d_*=
\frac{2(1-c)^2a^2}{(1-ca^2)^2+(1-c)^2a^2}
\sim2(1-e^{-\pi/2})^2e^{-\pi T/(2r)}.
\]

The exponent \(\pi T/(2r)\), including its factor of two relative
to the unsquared expression, is correct. For
\(T_n=32\lambda^{-1}\log(en)\) and
\(r_n=c_t[\log(en)]^{-1/2}\), the smallest integer meeting the
stated sufficient certificate has the asymptotic in the note:
a constant times

\[
[\log(en)]^{3/2}
\exp\!\left(\frac{16\pi}{\lambda c_t}
                  [\log(en)]^{3/2}\right).
\]

This is the cost of that certificate, not a lower bound on all methods
and not a change to retained source dimension. The staged Taylor bound
is a separate conditional result requiring control of the actual current
states. Its displayed maximum-error estimate uses a nonnegative
stability exponent \(L\); one can always replace a negative exponent
by \(\max(L,0)\). Taking steps of the maximal permitted size except
possibly the last gives the stated step-count upper bound.

The initial-jet error propagation formula and the coefficient convolution
factors in the displayed staged recursions are consistent. The first-layer
recursion is explicitly restricted to orthonormal training directions;
it is not the general correlated-data equation. Applicability and growing
size estimates for the external Gaussian compiler are not established by
these algebraic recursions and were not independently checked here.

The counterexample \(g(t,X)=(1+t^2X^2)^{-1}\) is valid: on
\(|X|\le\sqrt{a\log n}\), for \(n>1\), it is bounded by four
on the stated strip, while the unconditional even Taylor coefficients
are \((-1)^k(2k-1)!!\) and have zero radius of convergence.
The truncated-moment ratio bound also follows from
\((2k-1)!!\ge k!\ge(k/e)^k\). Thus the distinction between
high-probability analyticity and unconditional expected-jet continuation
is substantive and correctly scoped.

## 6. Issues and check status

No substantive correction is required for the circle initialization
theorem, its rank/computability argument, or its stated real-coordinate
storage. Its success does not establish a full trained compact network,
ordinary backpropagation with the new metric, quantitative dense-reference
identification, or the required whole-trajectory and endpoint accuracy.
Those boundaries are correctly stated in the synthesis.

The only reported notation issue was resolved during this reconstruction.
The first synthesis version, SHA-256
`5fe045a56e309577b2996303e70b6eed1c640453dd1e432f39dd07e380f16470`,
called a state initialized at the labels a residual state. The current
version explicitly defines it as the opposite-sign fitting state
\(y-f_C\), initialized at \(y\), and distinguishes the canonical
residual \(f_C-y\), initialized at \(-y\). The current synthesis
was then reread completely and its hash verified as listed above.
The continuation note was also clarified to state \(L\ge0\) and to
choose maximal permitted steps except possibly the last, matching the
qualifications in Section 5 of this report. Both revised passages were
read and its updated hash was verified; its prior hash was
`46bae6553c8a10279737070297e33fd68b8259f40e0e3df1baa78aedff09b155`.
The harmonic, envelope, and selection inputs are unchanged. These
clarifications leave the audited mathematics unchanged, and no
unresolved issue remains for the checked initialization module.

The source-selection and envelope arguments were reconstructed from
their full supplied proofs, with BSS imported exactly as authorized.
The second-jet calculation and continuation boundary asymptotic were
also reconstructed. Further claims about an external Gaussian compiler,
general-dimensional quadrature, or a prior corrected optimizer retain
their original dependency requirements. This report is internal
evidence for the explicitly checked components, not approval to promote
them or evidence that the complete direct compact training task is solved.

This report is frozen at handoff; its hash is reported separately.
