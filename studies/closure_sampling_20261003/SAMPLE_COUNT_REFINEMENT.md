# Sample-count refinement: label budgets and quadratic total storage

2026-10-04. Coordinator synthesis in the existing study. **Internally
checked research result**, not a manuscript claim or a promotion review.
The quadratic runtime, whole-query source interfaces, samplewise-budget
refinement and initialized geometry argument have all passed separate
reconstructions. Their complete reports, final versions and the
coordinator's assembly check are recorded in SAMPLE_COUNT_REFINEMENT_CHECK.md.

The reference remains the actual realized canonical width-n dense network.
The new representation uses a different autonomous optimizer, specified
in STORAGE_QUADRATIC_IMPROVEMENT.md. All retained fixed and moving real
coordinates count. Finite exact-real preprocessing may be arbitrarily
expensive; no trained reference trajectory is an input.

## 1. Setup and the combined theorem

Fix input dimension \(d\ge2\), hidden depth \(L\ge2\), sample count \(m\),
and training inputs \(v_a=x_a/\sqrt d\in S^{d-1}\). Every hidden layer of
the original network has width \(n\):

\[
z^{(1)}(x)=Av,\qquad z^{(\ell)}(x)=W^{(\ell)}h^{(\ell-1)}(x),
\qquad h^{(\ell)}(x)=\phi_\ell(z^{(\ell)}(x)),\qquad
f_n(x)=w^\top h^{(L)}(x)/n .
\]

The middle-layer recurrence is for \(\ell\ge2\). The entries of \(A_0\)
are independent \(N(0,1)\), those of each \(W_0^{(\ell)}\) are independent
\(N(0,1/n)\), all initialized blocks are independent, and \(w_0=0\).
The activations are real on the real axis and bounded and holomorphic on
one fixed horizontal strip. This is the existing analytic-compression
activation class; bounded \(C^3\) regularity alone is insufficient here.

Set \(c_a=y_a-f_n(x_a)\),
\(Y=(m^{-1}\sum_a y_a^2)^{1/2}\),
\(k_a^{(L)}=w\),
\(\delta_a^{(\ell)}=\phi_\ell'(z_a^{(\ell)})\odot k_a^{(\ell)}\), and
\(k_a^{(\ell)}=W^{(\ell+1)\top}\delta_a^{(\ell+1)}\).
Physical gradient flow is exactly

\[
\dot A=\frac2m\sum_a c_a\delta_a^{(1)}v_a^\top,\qquad
\dot W^{(\ell)}=\frac2{mn}\sum_a
c_a\delta_a^{(\ell)}h_a^{(\ell-1)\top},\qquad
\dot w=\frac2m\sum_a c_ah_a^{(L)} .
\tag{1}
\]

Define the deterministic initialized covariance by

\[
Q^{(0)}_{ab}=v_a^\top v_b,\qquad
Q^{(\ell)}_{ab}=\mathbb E[\phi_\ell(Z_a)\phi_\ell(Z_b)],
\quad Z\sim N(0,Q^{(\ell-1)}).
\]

Write

\[
Q=Q^{(L)},\quad \gamma=\lambda_{\min}(Q)>0,\quad
\bar\gamma=\min(1,\gamma),\quad
\lambda=\min(1,\gamma/m),\quad \ell_n=\log(en).
\tag{2}
\]

Structural constants below depend only on \(d,L\) and the activation strip
and bound. They do not hide \(m,\gamma,Y,n\), or elapsed time.

The combined sufficient label condition is

\[
                         0<Y\le c\lambda .
\tag{3}
\]

For tanh the cap in (2) is inactive, so this is \(Y\le c\gamma/m\).
For every fixed failure probability \(\eta>0\) and every sufficiently
large \(n\ge n_0(d,L,\phi,m,\gamma,Y,\eta)\), the construction has
probability at least \(1-\eta\) of satisfying

\[
\sup_{t\in[0,\infty]}\sup_{x\in\sqrt d S^{d-1}}
|f_C(t,x)-f_n(t,x)|\le C_{\mathrm{err}}/\sqrt n,
\tag{4}
\]

where \(C_{\mathrm{err}}\) is independent of width and time.
Both systems fit and converge, and \(t=\infty\) is included. A conservative
available prefactor is

\[
C_{\mathrm{err}}\le
C\lambda^{-1/2}\exp(CY/\lambda^{5/2}),
\tag{5}
\]

after enlarging the fixed-data width threshold to absorb polynomial
tail constants. This conditioning dependence is worse than that of the
older, larger representation; the storage improvement does not silently
preserve its sharper error prefactor.

The total retained size obeys, with \(a=d(L+5)+1\),

\[
\boxed{\quad
\mathrm{size}\le C\lambda^{-2}\ell_n^{2a}+Cm(d+1).
\quad}
\tag{6}
\]

When \(\lambda=\gamma/m\), this reads

\[
\boxed{\quad
\mathrm{size}\le C\frac{m^2}{\gamma^2}
[\log(en)]^{2[d(L+5)+1]}+Cm(d+1).
\quad}
\tag{7}
\]

There is no additional \(m^4\) training-history term. All fixed metric
matrices, moving matrices, readouts, internal residual coordinates,
training data and matrix-solve caches are counted.

The following version exposes the logarithmic gap dependence before it
is absorbed into the eventual width threshold:

\[
\mathrm{size}\le
C\lambda^{-2}\ell_n^{\,2d(L+4)+2}
[\ell_n+\log(e/\lambda)]^{2d}+Cm(d+1).
\tag{8}
\]

For \(\ell_n\ge\log(e/\lambda)\), (8) implies (6). This is only a
logarithmic simplification; no polynomial sample factor has been hidden
by assuming that \(\log n\) dominates a power of \(m\).

The case \(Y=0\) has exact zero predictions and needs no training dynamics.
The theorem has fixed-dataset quantifiers. It is not one event simultaneous
over independently initialized widths or growing datasets.

## 2. A label condition involving only the unnormalized gap

At fixed input dimension the initialized analytic covariance cannot have
arbitrarily many eigenvalues bounded below by a fixed positive number.
GEOMETRY_GAMMA_ONLY_LABELS.md proves, without extra input restrictions,

\[
m\le C[\log(e+1/\bar\gamma)]^\beta,\qquad
\beta=\frac{3(d-1)}2 .
\tag{9}
\]

Combining (9) with (3) gives the gap-only sufficient condition

\[
\boxed{\quad
Y\le
c\,\frac{\bar\gamma}
{[\log(e+1/\bar\gamma)]^{3(d-1)/2}} .
\quad}
\tag{10}
\]

Indeed \(\lambda\ge\bar\gamma/m\), and (9) implies
\(\lambda\ge c\bar\gamma[\log(e+1/\bar\gamma)]^{-\beta}\).
On the circle, \(d=2\), the logarithmic exponent is \(3/2\).
With both \(d=2\) and \(L=2\), (7) has width factor \(\log^{30}(en)\).
The logarithmic exponents and numerical constants are conservative.

There are two different kinds of improvement:

* Replacing the previous \(c\lambda e^{-C\sqrt{\log(em)}}\) threshold
  by (3) genuinely enlarges the sufficient label range for a given dataset.
* Equation (10) substitutes the largest sample count permitted by the
  existing gap and fixed-dimensional analytic geometry. It removes explicit
  \(m\), but does not enlarge the numerical threshold obtained by using
  that dataset's actual \(m\) in (3).

Neither argument proves that (3) or (10) is optimal. In particular it
does not show that \(Y\le c\gamma\) suffices for the general actual
trained model, or that the extra logarithmic loss is necessary.

Here is the heart of (9). The covariance has Hilbert feature maps
\(\Phi_\ell(v)=\phi_\ell(G_\ell(\Phi_{\ell-1}(v)))\), where
\(\Phi_0(v)=v\) and \(G_\ell\) is an isonormal Gaussian map. This is an
initialization representation only. Strip bounds and Gaussian moments
give, along every sphere angle,

\[
\|\partial_\theta^k\Phi_\ell\|
\le A B_\ell^k(k!)^{3/2}.
\]

The derivative order \(3/2\) remains the same at every fixed depth.
In the ordered-composition formula for derivatives, the activation
factor \(p!\) cancels its combinatorial denominator; the Gaussian factor
\(p^{p/2}\) is absorbed using
\(\prod_{i=1}^p j_i!\le k!/p!\).
Fourier truncation at degree \(J\) therefore approximates all feature
vectors by a space of dimension \(O(J^{d-1})\), with squared error
at most \(Ce^{-cJ^{2/3}}\). Projecting the \(m\)-sample Gram onto the
nullspace of this low-rank approximation gives
\(\gamma\le Ce^{-c m^{2/[3(d-1)]}}\), hence (9).

## 3. Why separate sample budgets improve labels

The old carrier proof bounded the neuron average of an exponential of
the maximum over samples. That introduced the exponential moment of a
maximum of \(m\) Gaussian paths. The new proof instead bounds, for every
sample separately,

\[
H_a=\frac1n\sum_{\ell<L}\sum_i
\exp\left\{\frac{\eta_0}{S}\sup_{t}|k_{a,i}^{(\ell)}(t)|\right\},
\qquad S=C_0Y/\lambda,
\tag{11}
\]

and stops when \(\max_a H_a=B\). Time suprema are over the current
stopped real or complex domain, as appropriate.

All deterministic uses of the budget require only individual-sample
carrier moments, their coordinate maxima, and products controlled by
Schatten Hölder inequalities. Thus (11) supplies the same estimates,
including products whose factors have different sample indices.
For each fixed \(a\), the omitted-neuron Gaussian reference has an
exponential-moment bound independent of \(m\).

The common-cavity expansion gives
\(\limsup_{n\to\infty}\mathbb E H_a^p\le D^p\) for every fixed integer
\(p\), with \(D<B/2\), after choosing a structural \(B\) and a
structurally small \(S\). The probability of any sample reaching its
budget is consequently at most \(m\,2^{-p}\) in the width limit.
Since \(m\) is fixed, taking the infimum over fixed \(p\) removes all
budget stops. Moment degree affects the width threshold, not the
admissible label size. This is why (3), rather than an additional
penalty in \(m\), suffices.

## 4. Why total storage is quadratic

Two separate losses have been removed.

First, backward responses are analytic functions of the query input on
the already proved whole-query forward domain. Their coarse complex
coordinate bound is \(C\sqrt n\), obtained from mixer operator bounds
and readout RMS. Analytic approximation uses
\(\log(\sqrt n/\epsilon)=O(\log n)\) at \(\epsilon=n^{-1}\).
Thus one jointly analytic query family covers every training response,
with the same degrees as before. There is no need to retain \(m\)
separate time families. Including exact initialization vectors gives

\[
                     R\le C\lambda^{-1}\ell_n^a .
\tag{12}
\]

Second, the old positive diagonal cubature used \(O(R^2)\) selected
neurons, and their full connections then cost \(O(R^4)\). The new
construction selects \(O(R)\) coordinates with a constant-distortion
spectral sampler. A fixed positive, generally non-diagonal matrix \(H\)
then makes the restriction of the source space exactly isometric.
Its comparison with positive diagonal masses is bounded by structural
constants, so pointwise activations remain uniformly Lipschitz.
All retained matrices now have \(O(R^2)\) entries.

The non-diagonal metric does not commute with activation derivatives.
Consequently ordinary gradient flow cannot simply be asserted for the
smaller model. The construction explicitly adds an internal residual
state \(c_C\) and uses the current top training-feature matrix \(F_C\)
to define the effective readout

\[
\widehat w_C=w_C+
F_C(F_C^\top HF_C)^{-1}
(y-c_C-F_C^\top Hw_C).
\tag{13}
\]

Its output is \(\widehat w_C^\top Hh_C(x)\); hence its actual
training residual equals \(c_C\) exactly. The internal residual evolves
by a positive Gram formed from the model's own current features and
backward signals. The raw parameter updates satisfy the exact identity

\[
-\frac{d}{dt}\|c_C\|_m^2
=\|\dot\theta_C\|_{\rm par}^2 .
\tag{14}
\]

This proves global fitting and controls hidden movement under (3).
Comparing the compressed and original residual equations yields damping;
the remaining error is amplified by total residual activity rather than
elapsed time. At source tolerance \(n^{-1}\), the amplification
\(\exp(C_{\rm data}\sqrt{\log n})\) is absorbed to give (4).
The separate tail proof uses weighted norms, avoiding any dependence
on the smallest selected mass or selected neuron count.

No population bias is omitted: (4) compares directly with the same
realized width-n dense run. The reference optimizer and initialization
are unchanged. The smaller optimizer is changed and is autonomous,
with no supplied trajectory, residual history, or endpoint.

## 5. Evidence and remaining questions

The proof components are:

* LABEL_SEPARATE_BUDGETS.md and its separate check: complete enlarged
  source/carrier label range.
* GEOMETRY_GAMMA_ONLY_LABELS.md: the initialized gap/count relation
  and its full Hilbert/Fourier proof, separately reconstructed in
  GEOMETRY_GAMMA_ONLY_CHECK.md.
* WHOLE_QUERY_RESPONSE_SOURCE.md and WHOLE_QUERY_RESPONSE_CHECK.md:
  removal of the extra training-source factor.
* STORAGE_QUADRATIC_IMPROVEMENT.md and STORAGE_QUADRATIC_CHECK.md:
  the new autonomous runtime, full error and all retained state.

The earlier results remain valid. Their historical open-status statements
about the residual \(m^4\) source term are superseded by the whole-query
refinement. The old gamma-only corollary includes an arbitrary extra
logarithmic exponent because it used the earlier label budget; substituting
(3) instead gives (10).

The strongest sufficient conditions proved here are not optimality
theorems. The unresolved genuine label improvement is control of learned,
feature-correlated backward products throughout the trajectory at larger
labels. LABEL_GEOMETRY_IMPROVEMENT.md proves an initialized Gaussian
derivative estimate but identifies the missing weighted-gradient estimate;
it does not establish that larger-label global theorem. No impossibility
claim follows from that missing estimate.

Ordinary-gradient-flow compression with the new quadratic count, a
matching lower bound on storage, growing-dimensional or growing-sample
quantifiers, and efficient bounded-precision preprocessing also remain
unproved. No experiment, manuscript edit, promotion, or Git write is part
of this continuation.
