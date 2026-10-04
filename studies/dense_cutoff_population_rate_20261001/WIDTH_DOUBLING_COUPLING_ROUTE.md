# Width doubling: exact embeddings and unresolved bias cancellation

Scoped derivation, 2026-10-03. This note uses the current study's
GENERAL_SELF_AVERAGING.md, DECISIVE_CONDITIONAL_ROUTE.md and the full-depth
physical-tube results. It does not establish the requested width-doubling
rate. The endpoint repair is developed separately in
WIDTH_DOUBLING_BLOCK_ROUTE.md.

The scope is fixed depth, a fixed compatible sphere training set, sufficiently
small fixed labels, and coordinate activations with bounded first three
derivatives. Activation values may have linear growth. The output is the
usual width-normalized scalar prediction, trained by the canonical gradient
flow. Write \(f_n(t,x)\) for width \(n\), and \(N=2n\).

## 1. Exact canonical duplication

Define \(D:\mathbb R^n\to\mathbb R^{2n}\) by \(Dv=(v,v)\), and
\(Q=D/\sqrt2\), so \(Q^\top Q=I_n\). For a width-\(n\) network with first-layer
array \(A\), hidden matrices \(W^{(\ell)}\), and readout \(w\), set
\[
 A^{\mathrm{dup}}=DA,\qquad
 W^{(\ell),\mathrm{dup}}=QW^{(\ell)}Q^\top
   =\frac12\begin{pmatrix}W^{(\ell)}&W^{(\ell)}\\
                          W^{(\ell)}&W^{(\ell)}\end{pmatrix},
 \qquad w^{\mathrm{dup}}=Dw .
\tag{1}
\]
All hidden preactivations, features and backpropagated neuron variables
duplicate. In particular
\[
 W^{(\ell),\mathrm{dup}}Dh=D W^{(\ell)}h,\qquad
 \phi(Dz)=D\phi(z),\qquad
 f_N^{\mathrm{dup}}=f_n .
\tag{2}
\]
The identities persist under canonical training. The first-layer and
readout velocities duplicate. The hidden velocity of every duplicated
entry is \(1/N=1/(2n)\) times its feature/adjoint product, exactly one half
of the corresponding width-\(n\) velocity. The loss residual is identical
by (2), so uniqueness of the finite-dimensional flow proves the assertion.
This verification applies to arbitrary coordinate activations in the
stated regularity class; bounded values are unnecessary.

The Gaussian endpoint is not canonical. First-layer rows duplicate
perfectly. The four corresponding hidden entries are the same Gaussian
divided by two, each with variance \(1/(4n)=1/(2N)\). Their joint covariance
has rank \(n^2\), whereas a canonical \(N\)-width hidden matrix has rank
\(N^2\). Thus (1) solves the dynamical endpoint problem but leaves a
substantial covariance comparison.

## 2. Straight covariance interpolation has an order-one interior defect

This is a failure of a proposed route, not a lower bound on the difference
between its endpoints. Fix a unit-variance scalar first-layer probe. Couple
duplicated rows to independent rows by
\[
 Z_j^\pm(s)=\sqrt{1-s}\,Z_j+\sqrt{s}\,B_j^\pm,\qquad 0\le s\le1,
\]
where all displayed base variables are independent standard Gaussians,
except for the shared \(Z_j\). Independently interpolate the hidden matrix
as
\[
 W_s=\sqrt{1-s}\,W^{\mathrm{dup}}+\sqrt{s}\,W_N^{\mathrm{iid}}.
\]
Put \(h_j^\pm=\phi(Z_j^\pm(s))\),
\(q=\mathbb E\phi(Z)^2\), and
\(p_s=\mathbb E[\phi(Z^+(s))\phi(Z^-(s))]\).
The activation has finite second moment by linear growth. Conditional on
the features, the variance of one second-layer preactivation is
\[
 \frac{1-s}{4n}\sum_{j=1}^n(h_j^++h_j^-)^2
 +\frac{s}{2n}\sum_{j=1}^n\big((h_j^+)^2+(h_j^-)^2\big).
\tag{3}
\]
The law of large numbers sends (3) to
\[
 v_s=\frac{1+s}{2}q+\frac{1-s}{2}p_s.
\tag{4}
\]
Both endpoints have variance \(q\). For \(0<s<1\), a nonconstant continuous
activation satisfies
\[
 q-p_s=\frac12\mathbb E|\phi(Z^+(s))-\phi(Z^-(s))|^2>0,
\tag{5}
\]
because the pair has a strictly positive density on \(\mathbb R^2\).
Consequently the limiting interior variance is smaller than \(q\) by a
positive amount independent of width. Even the initial forward law thus
changes at order one along this path. An absolute interpolation-derivative
bound cannot by itself produce a vanishing endpoint comparison; it must
capture cancellation along the path or modify the path substantially.

## 3. Orthogonal rotations do not preserve general coordinate activations

Suppose a nonaffine \(C^2\) scalar activation obeys
\(\phi(Oz)=O\phi(z)\) for every \(z\), where \(O\) is orthogonal and
\(\phi\) acts coordinatewise. Differentiating component \(i\) in two distinct
coordinates \(j,k\) gives
\[
 \phi''((Oz)_i)\,O_{ij}O_{ik}=0.
\tag{6}
\]
Since row \(i\) is nonzero, its linear form is surjective; since \(\phi\)
is nonaffine, \(\phi''\) is not identically zero. Thus \(O_{ij}O_{ik}=0\).
Every row has exactly one nonzero entry, so \(O\) is a signed permutation.
Each negative sign additionally requires the corresponding oddness
identity \(\phi(-z)=-\phi(z)\).

The block Hadamard rotation turns the matrix in (1) into
\(\operatorname{diag}(W,0)\), but it turns the activation into
\(z\mapsto O\phi(O^\top z)\), a coupled pair activation. It therefore does
not give a canonical network for the full activation class. An orthogonal
change of Gaussian coordinates can be useful in a distributional argument,
but it cannot be pushed through the nonlinear network by this algebra.

## 4. Balanced covariance and mobility: what the trace estimate misses

Divide every width-\(N\) layer into two blocks, with signs
\(\sigma_i\in\{-1,1\}\). The balanced variance profile is
\[
 c_{ij}(s)=1+(1-2s)\sigma_i\sigma_j,\qquad 0\le s\le\tfrac12.
\tag{7}
\]
Every row and column sum equals \(N\). Initialize hidden entries with
variance \(c_{ij}(s)/N\), and use the same coefficient \(c_{ij}(s)/N\)
in their learning mobility. This matching is essential. At \(s=0\),
the network is block diagonal with canonical width-\(n\) hidden dynamics;
at \(s=1/2\), it is canonical width \(N\).

For a fixed controlled residual path, let \(q\) denote the prediction's
activity derivative. Define the total normalized edge response
\[
 R_{ij}
 =N^2\mathbb E\left[
       \partial_{c_{ij}}q+\frac1{2N}\partial_{W_{ij}}^2q
                   \right],
\tag{8}
\]
where the first derivative keeps the initialized matrix fixed and
differentiates the mobility. Provided these derivatives are integrable
and differentiation under expectation is justified, Gaussian covariance
differentiation gives
\[
 \frac d{ds}\mathbb E q
   =-\frac2{N^2}\sum_{\ell,i,j}
             \sigma_i\sigma_j R_{ij}^{(\ell)}.
\tag{9}
\]
There are \(N^2/2\) edges of each sign per hidden layer. Equivalently, (9)
is the difference between the mean cross-block and within-block responses.
The needed estimate is a signed contrast, uniformly along the path and
over the required activity history.
The canonical high-probability physical tube does not by itself verify
these analytic hypotheses for the full expectations; a finite localization
must retain its derivative terms if used to justify the identity.

Even a uniform edgewise bound \(|R_{ij}|\le C\), stronger than an averaged
absolute trace bound, does not make (9) small. The admissible numerical
pattern
\[
 R_{ij}=b_0+b_1\sigma_i\sigma_j
\]
has bounded absolute averages but contributes \(-2b_1\) to (9) per
layer. Taking \(b_0\ge|b_1|\) makes this pattern nonnegative as well.
This is a logical test of the proposed norm argument, not an assertion
that the actual response has this form.

In normalized Gaussian coordinates \(H=\sqrt N W\), the covariance
direction is a traceless diagonal sign matrix on the \(N^2\) edge
coordinates. It has operator norm one and Hilbert--Schmidt norm \(N\).
Neither tracelessness nor row/column balance controls its pairing with
an aligned Hessian. The existing averaged second-response estimates
control the size of that Hessian, not this signed pairing. Full
permutation symmetry at \(s=1/2\) forces the contrast to vanish there;
it supplies no quantitative estimate away from that endpoint.

Moreover, uniform physical-tube and concentration estimates for the
entire profile family (7), including zero cross-block variances at
\(s=0\), have to be checked. They cannot simply be read off from a theorem
stated for canonical iid initialization.

## 5. Alternative route: fresh Gaussian response coupling

Here is an exact coupling for a fresh layer and the point where it ceases
to provide a trained-network proof. For \(m\) probes let \(H_n\) be their
\(n\times m\) feature matrix and
\[
 Q_n=\frac1nH_n^\top H_n .
\]
Conditional on \(H_n\), one row of an independent canonical Gaussian
hidden matrix produces a centered Gaussian vector with covariance
\(Q_n\). With the analogous \(Q_N\), using the same standard
\(m\)-dimensional Gaussian \(g\) gives responses
\(Q_n^{1/2}g\) and \(Q_N^{1/2}g\), with
\[
 \mathbb E_g\|Q_n^{1/2}g-Q_N^{1/2}g\|^2
       =\|Q_n^{1/2}-Q_N^{1/2}\|_{\mathrm{HS}}^2 .
\tag{10}
\]
If both covariances have a fixed positive spectral lower bound, their
square roots are Lipschitz on that set, and a root-width covariance
estimate transfers at the same rate. This supplies a viable layerwise
initialization coupling when those additional hypotheses hold.

Those lower bounds are not part of the full-scope assumptions for every
joint collection of training, test and adaptive response probes. They
can fail through repeated or linearly dependent probes. Without a lower
bound, the square root is only one-half Hölder in general: the scalar
pair \(0,\varepsilon\) has response coupling distance
\(\sqrt\varepsilon\). This example diagnoses the matrix-square-root
argument; it does not exclude a better network-specific coupling.

Training introduces a second, separate obstruction. The same matrix is
reused in forward and transpose responses. After recording constraints
\[
 WV=Y,\qquad W^\top U=Z,
\tag{11}
\]
a new response has a conditional Gaussian mean and covariance determined
by these past constraints. A fresh independent rotation chosen to match
the current feature covariance will generally violate (11). Conditional
Gaussian regression expresses the required response through inverses or
pseudoinverses of the growing query Gram matrices. A uniform perturbation
bound for this history, including singular and nearly singular query
Grams, has not been derived here.

The missing step can be stated without an interpolation sign contrast:
construct a coupled reuse of the Gaussian matrices at widths \(n,N\)
which preserves their canonical marginal laws and all prior forward and
transpose answers, and bounds the next conditional response discrepancy
by \(n^{-1/2+o(1)}\) plus an activity-integrable multiple of accumulated
state error. Equation (10) alone proves this only for a fresh matrix,
not for the adaptive repeated-matrix dynamics.

## 6. Endpoint agreement and current status

For the balanced profile, the autonomous block-diagonal endpoint uses
one shared residual. It is not literally two independently trained
width-\(n\) networks. Independently deriving the residual equations
confirms the endpoint repair pursued in WIDTH_DOUBLING_BLOCK_ROUTE.md:
the difference of the two reference residuals is the forcing that drives
the discrepancy, and same-width concentration plus exponential fitting
make its time integral near-root, with an additional logarithmic factor.
This is useful endpoint progress, not a bound for the interior
covariance/mobility interpolation.

The exact duplication endpoint, the variance defect (4), and the rotation
restriction (6) are established finite-dimensional calculations.
The signed-response identity (9) holds under its stated integrability
and expectation-differentiation hypotheses. The fresh-response coupling (10) is
also exact under its stated independence assumption. None yields an
unconditional near-root bound on the width-dependent deterministic
centers. The remaining possibilities exposed here are a genuine signed
response cancellation for (9), or a quantitative conditional-Gaussian
history coupling preserving (11). An averaged second-response norm
estimate by itself supplies neither.
