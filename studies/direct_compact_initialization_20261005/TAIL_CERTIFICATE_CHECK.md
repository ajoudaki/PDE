# Independent check of the finite-state tail certificates

2026-10-06. Independent isolated proof audit; no promotion is implied.

**Verdict: PASS for the stated conditional finite-system results.** The
dense and corrected compact certificates, their constants, the dense
invariant embedding, eventual success, openness under varying positive
metrics, sphere-uniform endpoint control, and bounded continuous dense
gate are valid. The computability statements are valid as strict-test
semidecision statements without a running-time bound. They do not supply
a compact initializer or a width bound.

The complete frozen inputs read were:

- `COMPUTABLE_TAIL_CERTIFICATES.md`, SHA-256
  `c605ad12f7308568770a03d47c78305d5f01c29af37ed354dcf2f1434bfcf9d9`;
- the explicitly assigned architecture source
  `studies/closure_sampling_20261003/STORAGE_QUADRATIC_IMPROVEMENT.md`,
  SHA-256
  `ec18f54a3e3977bf9c99ce5c26066f48688848f8b5a9c142b75424badeb025e2`;
- `docs/notation.qmd`, SHA-256
  `78e11eb3dafc5321a8a3923742993c0bad78df53b0e80b6319f16e48f0131023`.

No linked dependencies, study history, README, separate review reports,
other studies, or archived book passages were read. Status claims embedded
in the architecture source were not used as evidence. Only its explicit
autonomous equations were used as the architectural specification; its
source, compression, probability, and storage theorems are outside this
audit. No experiments or Git operations were performed.

The rigorous-math skill was read. Reading the required canonical-notation
skill at `/home/amir/.codex/skills/explain-with-canonical-notation/SKILL.md`
returned `Permission denied`; its linked neural-network reference was
therefore unavailable. The supervisor's explicit fallback was used with
the maintained notation contract. In this report \(c=y-f=-r\) is the
negative of the canonical residual, \(\rho=\|c\|_2/\sqrt m\), and \(t\)
is physical time. Weighted norms refer only to the explicitly specified
finite positive definite matrices \(H_i\).

## 1. Architecture and exact energy identity

For the compact model, let \(F\) have columns equal to the current top
features at the \(m\) training inputs, and put

\[
 V=F/\sqrt m,\qquad q=V^TH_2V,\qquad Q=mq.
\]

On \(q\succ0\), multiplication of the supplied correction by \(F^TH_2\)
gives

\[
 F^TH_2\widehat w
 =F^TH_2w+QQ^{-1}(y-c-F^TH_2w)=y-c.
\]

Thus the auxiliary residual is exactly the negative residual of the
reported output, including away from the dense constraint. The candidate
uses \(\widehat w\), as required, in every compact backward signal. Its
two-layer equations are the corresponding specialization of the
architecture source, including \(B^*=H_1^{-1}B^TH_2\) and the right factor
\(H_1\) in \(\dot B\). They are not ordinary output-gradient equations
for general metrics; the candidate correctly makes no such assertion.

Let \(\theta=(A,B,w)\), with the candidate's parameter norm

\[
 \|\theta\|_{\mathrm{par}}^2
 =\operatorname{tr}(A^TH_1A)
  +\|H_2^{1/2}BH_1^{-1/2}\|_F^2+w^TH_2w.
\]

Expanding the squared norms of the three raw velocities gives the three
terms of the specified Gram \(K\), with all cross-sample products retained.
In particular,

\[
 H_2^{1/2}\dot B H_1^{-1/2}
 =\frac2m\sum_a c_a
       (H_2^{1/2}\delta_a^{(2)})(H_1^{1/2}h_a^{(1)})^T.
\]

The \(A\) and \(w\) terms give respectively the last and first terms of
\(K\). Since \(\dot c=-2Kc/m\), the exact identity is

\[
 \|\dot\theta\|_{\mathrm{par}}^2
 =\frac4{m^2}c^TKc=-\frac{d}{dt}\rho^2.
\]

Each of the two terms of \(K-Q\) is a tensor-product Gram matrix, so
\(K\succeq Q\). The argument does not confuse the raw readout \(w\) with
the reconstructed readout \(\widehat w\).

For the dense specialization \(H_1=H_2=I_n/n\), the parameter norm is
exactly \(\|A\|_F^2/n+\|W\|_F^2+\|w\|_2^2/n\). Differentiating the
dense output under the stated mobilities \((n,1,n)\) produces this same
\(K\) and residual equation. There is no missing factor of \(n\), \(m\),
or two.

The dense constraint is \(e=y-c-F^Tw/n=0\). On it,
\(\widehat w=w\), the raw compact velocities equal the dense velocities,
and \(\dot e=0\). More directly, augmenting any dense solution by its
actual residual solves the entire compact system while \(q\succ0\).
Local uniqueness of the smooth compact vector field therefore proves
invariance. No embedding is claimed across a singular Gram.

## 2. Path length, gap preservation, and continuation

Fix the candidate's test time \(T\), positive lower gap \(g\), radius
\(R\), and feature constant \(L\) from its equation (6). Whenever
\(q\succeq gI\) and \(\rho>0\), put \(a=-\rho'\). The energy identity
and \(K\succeq mq\) give

\[
 a\ge2g\rho,\qquad
 \|\dot\theta\|_{\mathrm{par}}^2=2\rho a\le a^2/g.
\]

Consequently, on such an interval,

\[
 \int_t^s\|\dot\theta\|_{\mathrm{par}}\,du
 \le\frac{\rho(t)-\rho(s)}{\sqrt g},\qquad
 \rho(s)\le\rho(t)e^{-2g(s-t)}.
\]

At \(c=0\) every velocity vanishes, so the zero-residual case is covered.
In particular the claimed coefficient \(1/\sqrt g\) is correct.

For a diagonal gate \(D\) with entries of magnitude at most one,
\(\|H_i^{1/2}DH_i^{-1/2}\|_{\mathrm{op}}
\le\sqrt{\beta_i/\alpha_i}=\gamma_i\). Bounded tanh gives
\(\|h^{(i)}\|_{H_i}\le b_i=\sqrt{N_i\beta_i}\). On the parameter unit
ball about the state at \(T\), the weighted operator norm of \(B\) is at
most \(M_B\). The chain rule and the two-term Cauchy--Schwarz inequality
therefore give, for every sphere query,

\[
 \|d h^{(2)}\|_{H_2}
 \le\gamma_2\bigl(b_1\|H_2^{1/2}dB H_1^{-1/2}\|_F
       +M_B\gamma_1\|H_1^{1/2}dA\|_F\bigr)
 \le L\|d\theta\|_{\mathrm{par}}.
\]

The parameter ball is convex, so integrating on segments gives the
corresponding finite-difference bound. Averaging the squared training
feature bounds gives

\[
 \|V(\theta)-V(\theta(T))\|_{\mathbb R^m\to H_2}
 \le L\|\theta-\theta(T)\|_{\mathrm{par}}.
\]

There is no extra sample-count factor. With
\(R=\min\{1,\sqrt{\lambda_T}/(2L)\}\), every point of the closed
\(R\)-ball has smallest singular value of \(V\) at least
\(\sqrt{\lambda_T}/2\), hence \(q\succeq gI\) for \(g=\lambda_T/4\).
The strict condition \(\rho_T/\sqrt g<R\) prevents a first exit.

The raw state and residual then remain bounded, and \(q^{-1}\) remains
bounded. For the fixed finite metrics the parameter norm is equivalent
to the coordinate norm. Hence the solution remains in a compact subset
of the smooth vector-field domain. Bounded velocity yields a limit at
any putative finite maximal time, and local existence at that limit
extends the solution. This proves continuation without assuming the
conclusion in advance. Finite remaining path length gives raw-parameter
convergence, uniform feature convergence, and a limiting gap at least
\(g\).

Using certified upper and lower matrix bounds is valid provided the
constants and the radius are recomputed consistently from those bounds.
The Frobenius substitute for the mixer operator norm is such an upper
bound and preserves this proof.

## 3. Corrected readout and uniform endpoint bounds

All norms in this paragraph are between Euclidean sample space and the
\(H_2\) neuron space. Define

\[
 \mathcal T=Vq^{-1},\qquad P=\mathcal TV^*,\qquad
 b=(y-c)/\sqrt m.
\]

Then \(P\) is the orthogonal projector onto \(\operatorname{range}(V)\),
\(\mathcal T^*\mathcal T=q^{-1}\), and
\(\widehat w=(I-P)w+\mathcal Tb\). Therefore

\[
 \|V\|\le b_2,\quad \|\mathcal T\|\le g^{-1/2},\quad
 \|P\|\le1,\quad \|b\|_2\le J,
 \quad \|\widehat w\|_{H_2}\le M_w+J/\sqrt g.
\]

The inverse derivative identity gives exactly

\[
 \|\dot q\|\le2b_2\|\dot V\|,\qquad
 \|\dot{\mathcal T}\|
 \le(g^{-1}+2b_2^2g^{-2})\|\dot V\|=D_T\|\dot V\|,
\]
\[
 \|\dot P\|\le(b_2D_T+g^{-1/2})\|\dot V\|=D_P\|\dot V\|,
 \qquad \|\dot V\|\le L\|\dot\theta\|_{\mathrm{par}}.
\]

These verify both inverse constants in the candidate. Subtracting
\((I-P)w+\mathcal Tb\) at \(t\) and infinity, and using
\(\|b(\infty)-b(t)\|_2=\rho(t)\), gives

\[
 \|\widehat w(\infty)-\widehat w(t)\|_{H_2}
 \le\frac{\rho(t)}{\sqrt g}
       \{2+L(D_PM_w+D_TJ)\}.
\]

The two unit terms have distinct origins: remaining raw readout motion
and the terminal residual correction. Both are present. Multiplying by
the feature bound \(b_2\) and adding feature motion times the readout
bound \(M_{\widehat w}\) yields exactly the displayed \(C_C\). The same
bilinear subtraction without reconstruction yields
\(C_n=(b_2+M_wL)/\sqrt g\) in the dense case.

These estimates hold uniformly on the whole query sphere. They prove
endpoint error at most \(C\rho(t)\). For any \(s\ge t\), the triangle
inequality through the endpoint and \(\rho(s)\le\rho(t)\) give excursion
at most \(2C\rho(t)\), including \(s=\infty\). The exact output identities
and \(c\to0\) give interpolation by the limiting network.

## 4. Eventual success and varying-metric openness

Under the stated bounded-parameter and uniform-gap hypotheses, \(L(T)\)
is bounded above, \(R(T)\) is bounded away from zero, \(g(T)\) is bounded
away from zero, and \(M_w(T),J(T),C(T)\) are bounded above. Thus
\(\rho(T)\to0\) makes both strict inequalities hold eventually. The
stronger assumed exponential decay is sufficient but not necessary.
An integer time exists because the conclusion holds at every sufficiently
large real time. Combining a finite-horizon comparison with the two
certified tail excursions gives the claimed all-time comparison by the
triangle inequality, including the endpoint.

For openness, append the symmetric entries of \(H_1,H_2\) to the state
with zero velocities. The extended vector field is smooth on
\(H_1,H_2\succ0\), \(q\succ0\). On any compact reference time interval,
this open domain contains a tube around the trajectory with bounded
vector-field derivatives. Subtraction of the two integral equations and
Gronwall's elementary integrating-factor argument give existence and
uniform state convergence for sufficiently close initializers. Output
derivatives are bounded also over the compact query sphere. All test
constants are continuous in the state and metrics; repeated eigenvalues
cause no problem because only eigenvalue continuity is required.

A successful initializer acquires a uniform gap and bounded raw
parameters from its first certificate. Eventual success then supplies a
later time at which the reference excursion is below
\(\varepsilon/3\). Finite-time continuity preserves the strict tests,
puts the perturbed excursion below \(\varepsilon/3\), and makes the
finite-time prediction error below \(\varepsilon/3\). Their sum proves
the claimed uniform-in-time and uniform-in-query continuity. Each metric
is fixed along its own trajectory; the proof does not incorrectly apply
the energy identity to a time-varying metric.

Symmetric rational matrices are dense, and positive definiteness is open
under symmetric perturbations. Rational perturbations of \(A_0,B_0,H_1,H_2\)
can therefore be chosen inside this successful neighborhood while
\(w_0=0,c_0=y\) and the original data stay exact. This is an existence
statement; no denominator or width control follows.

## 5. Dense acceptance gate and effectivity

The terminal quantities in equations (22)--(23) are continuous, including
at a zero Gram eigenvalue. Since \(1+T>0\), a positive gate requires both
\(s_1,s_2>0\). The first forces \(\lambda_+>0\), and with
\(g=\lambda_+/4\) the two inequalities become exactly

\[
 \rho_T/\sqrt g<R_F,\qquad
 2\{1+(u+R_F)L_F\}\rho_T/\sqrt g<\eta.
\]

Thus positivity implies the Frobenius version of the dense certificate.
Under the eventual-success hypotheses the two margins have strictly
positive eventual lower bounds; multiplication by \(1+T\) makes both
clipped factors equal one eventually. The gate remains bounded between
zero and one everywhere and is not asserted to be a probability.

The candidate's separate dense finite-time bounds are correct:
\(\dot u\le2\rho(0)\) in the integrated norm sense,
\(\|\dot W\|_F\le2\rho(0)u\), and
\(\|\dot A\|_F/\sqrt n\le2\rho(0)\|W\|_{\mathrm{op}}u\).
They prevent finite-time blowup for every finite dense initialization.
An alternative direct verification is Cauchy--Schwarz in time applied
to the energy identity, which bounds raw path length on \([0,T]\) by
\(\rho(0)\sqrt T\) even without a Gram gap. Smooth finite-time dependence
therefore makes the gate continuous in dense initial coordinates.

For computable data and initial coordinates, every scalar and matrix
operation used in a strict test has arbitrarily accurate certified
approximations. Positive definiteness and strict inequalities are open
conditions, hence are detected after finitely many refinements whenever
they hold. On compact boxes with certified positive inverse margins, the
explicit vector field and its derivatives admit computable bounds.
Validated short-time integral-equation approximations can be concatenated;
a valid compact trajectory segment has a finite cover by such boxes.
Searching over rational boxes, time steps, and precision therefore
computes the finite-time state on its domain and semidecides a passing
test. The text correctly disclaims equality decisions, complexity bounds,
and unconditional computation for noncomputable data.

One implementation detail should be made explicit in any subsequent
algorithm: **dovetail the integer times and precision refinements**. A
serial routine that waits forever for a nonpassing strict test at its
first time would not inherit eventual termination. Dovetailing finds the
finite witness at an eventually passing integer time. This clarification
does not change the stated existential computability result.

For strict conformity with the maintained notation contract, the local
feature Lipschitz constant \(L\) could be renamed \(L_h\), since the book
reserves \(L\) for hidden depth. It is explicitly defined in the candidate,
so this is a presentation refinement rather than a mathematical defect.

No substantive correction is required for the audited conditional results.
