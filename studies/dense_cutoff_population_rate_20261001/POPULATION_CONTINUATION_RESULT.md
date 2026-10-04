# Direct dense-to-population continuation

2026-10-03. Coordinator synthesis of the direct comparison and negative
search. This continues this study; it is not a manuscript addition.

**Status: the requested dichotomy remains unresolved.** No all-time
near-root dense-to-population theorem, and no canonical example with a
polynomially slower rate, has been established. The local finite-network
and auxiliary probability results below are completed progress, not
substitutes for that target.

## Model and target

There are fixed \(L\) hidden layers of width \(n\), fixed training inputs
\(\|x_a\|=\sqrt d\), and fixed compatible labels. Define
\[
 h^{(0)}(x)=x/\sqrt d,\qquad
 z^{(1)}=W^{(1)}h^{(0)},\qquad
 z^{(\ell)}=W^{(\ell)}h^{(\ell-1)},\qquad
 h^{(\ell)}=\phi_\ell(z^{(\ell)}),\qquad
 f_n=w^\top h^{(L)}/n.
\]
The first weights are independent standard Gaussians, the hidden
matrices have independent \(N(0,1/n)\) entries, all blocks are
independent, and \(w(0)=0\). Each activation is \(C^3\) with bounded
first three derivatives; values may have linear growth.

Write \(r_a=f_n(x_a)-y_a\), \(\mathcal L=\sum_a p_a r_a^2\), where
\(p_a>0\) are fixed and sum to one. The backward variables are
\[
 \delta_a^{(L)}=\phi_L'(z_a^{(L)})\odot w,\qquad
 \delta_a^{(\ell)}
   =\phi_\ell'(z_a^{(\ell)})\odot
                       W^{(\ell+1)\top}\delta_a^{(\ell+1)}.
\]
The physical gradient flow is
\[
 \dot w=-2\sum_a p_a r_a h_a^{(L)},\qquad
 \dot W^{(1)}=-2\sum_a p_a r_a\delta_a^{(1)}h_a^{(0)\top},
 \qquad
 \dot W^{(\ell)}=-\frac2n\sum_a p_a r_a
                       \delta_a^{(\ell)}h_a^{(\ell-1)\top}.
\]
This is the actual dense model, with no clipping or frozen learned
matrices. The label RMS \(Y=(\sum_a p_a y_a^2)^{1/2}\) is sufficiently
small under DEPTH_EXTENSION_RESULT. The positive initial feature gap
is understood on the compatible data quotient specified there.

Let \(f_\infty\) be the manuscript's canonical Gaussian-operator
population solution. For a query law with finite second moment, the
target remains
\[
 \mathcal E_\mu(f_n,f_\infty)
 :=\left(\int\sup_{t\ge0}|f_n(t,x)-f_\infty(t,x)|^2d\mu(x)\right)^{1/2}
 \le C_{\delta,\mu}n^{-1/2}e^{K\sqrt{\log(e+n)}}
 \tag{1}
\]
with probability at least \(1-\delta\) for all sufficiently large \(n\).
This is a near-root target, distinct from a strict \(C_\delta/\sqrt n\)
bound. Constants may depend on the fixed data, depth, activation,
labels, confidence and query law, but not width or time.

## Completed finite-network improvement

[POPULATION_DIRECT_COUPLING.md](POPULATION_DIRECT_COUPLING.md),
Sections 3–5, improves the finite deletion/reinsertion calculation to
near-root accuracy. Its complete internal reconstruction is
[POPULATION_DIRECT_CHECK.md](POPULATION_DIRECT_CHECK.md).

Delete one neuron, retaining the original normalizations, and let the
retained network train against its own residual. Conditional on that
cavity's initialization, the omitted incoming and outgoing Gaussian
weights are independent of the cavity response kernels. On the already
proved physical tube and carrier events, put
\[
 A_n=e^{C\sqrt{\log(e+n)}},\qquad
 \varepsilon_n=A_n/\sqrt n,\qquad T_n=C_0\log n.
\]
In mobility coordinates (read-in/readout divided by \(\sqrt n\), hidden
increments in Frobenius norm), write the retained-state change after
restoring the neuron as \(V+U\), where \(V\) is the explicit first
response to the restored neuron's actual bounded histories. Then
\[
 \sup_{t\le T_n}\|U(t)\|_2\le\varepsilon_n.
 \tag{2}
\]
The adaptive histories are retained. They are not replaced by prescribed
independent controls. The scalar training prediction changes by at most
\(A_n/n\). Exponential fitting controls the remaining training-prediction
tail. The unfrozen variational formula itself is asserted through
\(T_n\), not integrated without damping to infinite time.

The crucial estimate is coordinatewise. A conditional Gaussian kernel
probe has coordinate size \(A_n/\sqrt n\) but Euclidean size \(A_n\).
One uses the small coordinate factor in nonlinear Taylor products.
The resulting bootstrap has the form
\[
 \|U\|\le A_n\{n^{-1/2}+n^{-1/2}\|U\|+\|U\|^2\},
\]
which closes at (2). Bounding both factors only by Euclidean norms
would lose this conclusion. Uniformity over bounded restored histories
comes from bounding the Gaussian kernels before multiplying and
integrating those histories; a net of adaptive control functions is
unnecessary.

The calculation yields explicit conditional Gaussian forward/backward
equations with near-root remainders. Their coefficients are the
**actual random cavity covariance and response kernels**. It does not
replace those kernels by the deterministic population kernels.

The follow-up [POPULATION_ADJACENT_ATTEMPT.md](POPULATION_ADJACENT_ATTEMPT.md)
keeps the leading width-renormalization term, derives tagged-history
response identities, and examines localization. Its final empirical
observable comparison explicitly assumes an extension property for
that particular observable. It is not an unconditional population
theorem. The corresponding internal check records the exact accepted
scope and the conditioning repair.

## Completed Gaussian path comparison

[POPULATION_COVARIANCE_COUPLING.md](POPULATION_COVARIANCE_COUPLING.md)
proves an unconditional auxiliary theorem, reconstructed in
[POPULATION_COVARIANCE_CHECK.md](POPULATION_COVARIANCE_CHECK.md).
Let \(X_1,\ldots,X_n\) be independent copies of a random Hilbert-space
path \(X\). Suppose \(\|K^{1/2}X\|\le B\) almost surely and
\(\operatorname{tr}K^{-1}<\infty\). Put
\[
 Q=\mathbb E[X\otimes X],\qquad
 \widehat Q_n=n^{-1}\sum_iX_i\otimes X_i.
\]
For the least mean-squared coupling distance \(d_{\rm G}\) between
centered Gaussian laws with these covariances,
\[
 \mathbb E\,d_{\rm G}(Q,\widehat Q_n)^2
       \le B^2\operatorname{tr}(K^{-1})/n.
 \tag{3}
\]
No positive lower bound on covariance eigenvalues is required. A
Sobolev choice of \(K\) makes (3) control the supremum over a finite
time interval for paths bounded in \(H^2\).

This avoids a misleading square-root loss caused by comparing
covariances in an unweighted norm. However, trained neurons are
dependent. For them the empirical covariance variance contains
\[
 \frac1{n^2}\sum_{r\ne s}
   \operatorname{Cov}(X_{r,i}X_{r,j},X_{s,i}X_{s,j}).
 \tag{4}
\]
The proof of (3) does not control (4) in the necessary
\((\lambda_i+\lambda_j)^{-1}\)-weighted covariance norm.
Declaring the paths independent would change the model.

## What the negative search established

[POPULATION_NEGATIVE_SEARCH.md](POPULATION_NEGATIVE_SEARCH.md)
obtained no canonical lower bound. Its exact calculations show:

1. Initialized smooth feature-Gram maps are Lipschitz in covariance,
   even at singular covariances. The finite initialized feature
   covariances and initial output velocities have root-width accuracy
   at fixed query lists. Population null relations are also exact
   finite initialized relations.
2. With zero readout, hidden motion begins at order \(t^2\); a new
   feature-history innovation has squared norm starting at \(t^4\).
   This is a finite-width local expansion, not an all-time rate.
3. \(C^3\) regularity does not make arbitrary derivative observables
   covariance-Lipschitz. For a smooth cutoff of
   \((s_+)^{3+\beta}\), \(0<\beta<1\), the Gaussian average of its
   second derivative at variance \(v\) scales as
   \(v^{(1+\beta)/2}\). This invalidates a proposed proof step, but
   does not produce a neural prediction lower bound.
4. The fixed training gap and exponential fitting tails exclude
   critical slowing as a mechanism in this small-label regime.
   A putative polynomially slower error is already visible by
   logarithmic training time.

The already proved near-root concentration around deterministic
finite-width centers \(c_n\) has a further exact implication. A lower
bound of order \(n^{-1/2+\alpha}\), with fixed positive probability
and \(\alpha>0\), would force a deterministic center displacement
\(\mathcal E_\mu(c_n,f_\infty)\) of that order. Random macroscopic
branch selection cannot supply such a counterexample in this regime.
This observation does not bound the center displacement.

## Response transport and a precise limitation

The further [POPULATION_RESPONSE_TRANSPORT.md](POPULATION_RESPONSE_TRANSPORT.md)
removes a moving-projection difficulty for consistently coupled
population programs. For one initialized matrix, let \(H_-\) and
\(H_+\) be its lower and upper generated \(L^2\) spaces. Its forward
Gaussian source map \(I:H_-\to H_+\) and reverse source map
\(J:H_+\to H_-\) are isometries. The manuscript's causal
source rule and Gaussian integration by parts give
\[
 W_0=I+J^*,\qquad W_0^*=I^*+J.
 \tag{5}
\]
Here the adjoint terms are precisely the represented response
corrections. They are contractions, irrespective of the rank of a
finite source-history Gram. The compatible maps are constructed
through interleaved finite causal programs and consistent completion,
not by assuming independent random operators on circularly defined
spaces. This also yields the population-flow stability estimate in
that note, once two paths are realized in that common environment.
The complete reconstruction is
[POPULATION_RESPONSE_TRANSPORT_CHECK.md](POPULATION_RESPONSE_TRANSPORT_CHECK.md).

There is a separate obstruction to applying a full parameter-law
coupling directly to the finite network. For every \(n\)-point
empirical read-in law \(\nu_n\) in \(\mathbb R^d\),
\[
 W_2(\nu_n,N(0,I_d))\ge c_d n^{-1/d}.
 \tag{6}
\]
The proof in [POPULATION_TRANSPORT_LIMIT.md](POPULATION_TRANSPORT_LIMIT.md)
uses only the bounded Gaussian density and the volume of \(n\) small
balls; its reconstruction is
[POPULATION_TRANSPORT_LIMIT_CHECK.md](POPULATION_TRANSPORT_LIMIT_CHECK.md).
Its independent-average identity shows explicitly why (6)
does not imply a prediction lower bound. When \(d>2\), (6) prevents
a near-root comparison of entire parameter populations in quadratic
transport before training even begins. Comparing sampled population
fields or weaker prediction observables avoids that particular
requirement, but their joint forward/adjoint finite-matrix coupling
has not been constructed here.

Thus (5) removes a response-coordinate instability, while (6)
rules out an overstrong way of supplying its finite-width input.
Neither settles the requested prediction rate.

## Precise unresolved conclusion

The local finite-network Gaussian/response expansion is now
near-root. The collective response comparison is not. No estimate
in this continuation identifies the finite-width covariance and
represented-response centers with their population counterparts at
the rate (1). Adjacent-width deletion and renormalization also have
uncancelled terms of order \(A_n/n\); a summable difference at order
\(A_n/n^{3/2}\) has not been obtained.

These are statements about the limits of the attempted proofs,
not new assumptions offered in place of the requested theorem,
and not evidence that the actual rate is slower. The evidence in
this continuation favors a positive near-root result, but that is
a research judgment, not a proved conclusion.

No experiment, manuscript edit, promotion, commit or push was made.
The fixed query-law second-moment restriction has not been silently
strengthened. All proofs and checks remain internal to this study.
