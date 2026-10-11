# Scope of the proposed simultaneous-time relative bound

Author: scoped agent `uniform_time_scope`, 2026-10-11.

Status: complete direct proofs of endpoint obstructions under the manuscript's
stated denominator convention; a separate conditional late-time lemma. This is
study material, not a promoted theorem or an independent review. No claim is
made that the conditional spectral hypotheses hold for the current closures.

## Assignment and sources

The assigned question is whether adding only layerwise nonaffinity to the
current setup can give

\[
\sup_{t\in(0,\infty]}
\frac{\sup_{x\in\mathcal X}|f_{\rm model}(t,x)-f_n(t,x)|}
     {\sup_{x\in\mathcal X}|f_n(t,x)-\widetilde f_n(t,x)|}
\xrightarrow{\mathbb P}0,
\qquad n\longrightarrow\infty,
\tag{1}
\]

with the existing query domains: the whole sphere for Legendre and Harmonic;
training inputs and any prescribed finite passive panel, including an empty
panel, for Taylor. The two dense runs are independent and use the same data.

Scientific inputs were limited to `paper/compact.tex`,
`paper/compact_fitting.tex`, the selected-model definition and fitting statements
in `paper/compact_selected.tex`, the Legendre forward definition and fitting
statements in `paper/compact_legendre.tex`, and
`paper/feature_learning_theorem.tex`. The latter's nonparallel-training
hypothesis belongs to the separate feature-learning statement, not the headline.
No other study or archived book was read. The rigorous-solution and canonical
notation skills, including the neural-network reference, were applied.

The current headline instead proves a ratio of two trajectory suprema. Its
convention in `compact.tex:151–152` says that a zero denominator counts as
failure. The obstructions below use that explicit convention. The dense fitting
lemma gives, with probability tending to one, parameter limits and
\(f_n(\infty,x_a)=y_a\) for every training index \(a\).

## 1. The empty passive panel already excludes (1)

For Taylor with \(p=0\), set
\(\mathcal X=\{x_1,\ldots,x_m\}\). On the intersection of the two dense fitting
events,

\[
\sup_{x\in\mathcal X}|f_n(\infty,x)-\widetilde f_n(\infty,x)|=0.
\tag{2}
\]

Each event has probability tending to one, so their intersection does too by
the union bound. Consequently (1) fails with probability tending to one under
the stated convention, independently of the choice of compression. Layerwise
nonaffinity cannot change this interpolation identity.

The current constructions themselves also fit, so their endpoint numerator is
zero on their fitting events. This obstruction is thus \(0/0\), not a positive
compression error divided by zero. Defining \(0/0=0\) would remove this specific
obstruction, but would change the theorem's current convention.

## 2. A nonempty distinct passive panel with full training span

Take \(d=m=2\), any fixed \(L\ge2\), normalized training inputs
\(v_1=e_1\), \(v_2=e_2\), and physical inputs \(x_a=\sqrt2v_a\). Declare
the two passive inputs \(-x_1,-x_2\). All four inputs are distinct; the training
inputs are nonparallel and span the entire input space. At every layer choose

\[
\phi_\ell(z)=\cos z.
\]

These activations are nonaffine and entire, real on the real axis, and satisfy
\(|\phi_\ell'(z)|\le\cosh a\) on every strip \(|\operatorname{Im}z|<a\).
The same bound holds for the second derivative, so the manuscript's finite
activation envelope \(\beta\) exists.

We verify the positive Gram gap explicitly. Write the population Gram at layer
\(j\) as

\[
Q^{(j)}=\begin{pmatrix}q_j&c_j\\c_j&q_j\end{pmatrix},
\qquad q_0=1,\quad c_0=0.
\]

For a centered Gaussian pair of marginal variance \(q\) and covariance \(c\),
the identity \(2\cos u\cos v=\cos(u-v)+\cos(u+v)\), together with
\(\mathbb E\cos G=e^{-\operatorname{Var}(G)/2}\), gives

\[
q_j=e^{-q_{j-1}}\cosh(q_{j-1}),\qquad
c_j=e^{-q_{j-1}}\cosh(c_{j-1}).
\tag{3}
\]

Starting from \(0\le c_0<q_0\), strict increase of \(\cosh\) on
\([0,\infty)\) implies \(0<c_j<q_j\) for every \(j\ge1\). The two
eigenvalues are \(q_j-c_j\) and \(q_j+c_j\), and therefore

\[
\gamma=q_L-c_L>0.
\]

Also \(q_j\le1\), since it is the expectation of a squared cosine. Hence
\(m/\gamma\ge1\). For example choose
\(y=(\varepsilon,2\varepsilon)\), where
\(0<\varepsilon\le(\gamma/2)\beta^{-30L}\sqrt{2/5}\). Then
\(Y=\varepsilon\sqrt{5/2}>0\) and the exact existing label cap holds.

For every parameter state, evenness of the first activation gives

\[
h^{(1)}(-v)=\cos(-W^{(1)}v)=h^{(1)}(v).
\]

Inductively all later features agree at \(v\) and \(-v\), and consequently
\(f_n(t,-x)=f_n(t,x)\) for every time and every initialization. The same
identity holds for the Legendre forward pass and the selected forward pass;
the latter's corrected readout is still a linear functional of the top
features. On the dense fitting event,

\[
f_n(\infty,\pm x_1)=y_1,\qquad
f_n(\infty,\pm x_2)=y_2.
\tag{4}
\]

Thus for Taylor on the declared four-input panel, the endpoint denominator in
(1) again vanishes with probability tending to one. The endpoint numerator
also vanishes when the compressor fits. The same construction with only
\(-x_1\) declared gives \(p=1\).

This example does not rely on an empty panel, a zero label vector, an affine
activation, a degenerate training Gram, parallel training inputs, or a proper
training span. It does use passive inputs antipodal to training inputs. It
therefore does not address a *different* query-domain requirement that every
passive input be nonparallel to every training input; that restriction is absent
from the headline and from (1) as assigned. No counterexample with that stronger
passive separation requirement is asserted here.

## 3. The current whole-sphere scope also permits a zero endpoint denominator

The headline does not impose \(d\ge2\). Take \(d=1\), \(m=2\),
\(x_1=v_1=1\), \(x_2=v_2=-1\), and any fixed \(L\ge2\). These training
points exhaust the input sphere. At every layer choose

\[
\phi_\ell(z)=1+\sin z.
\]

The activations are entire, nonaffine, real on the real axis, and have bounded
first and second derivatives on every fixed horizontal strip. Again write
\(Q^{(j)}\) with diagonal \(q_j\) and off-diagonal \(c_j\), now starting
from \(q_0=1,c_0=-1\). Gaussian symmetry eliminates the individual sine
means. The identity
\(2\sin u\sin v=\cos(u-v)-\cos(u+v)\) gives

\[
q_j=1+e^{-q_{j-1}}\sinh(q_{j-1}),\qquad
c_j=1+e^{-q_{j-1}}\sinh(c_{j-1}).
\tag{5}
\]

Set \(s=(1-e^{-2})/2\in(0,1/2)\). Then
\(q_1=1+s\), \(c_1=1-s\), so \(0<c_1<q_1\).
For all subsequent layers, strict increase of \(\sinh\) preserves
\(0<c_j<q_j\). Hence \(\gamma=q_L-c_L>0\). Moreover
\(q_j=1+(1-e^{-2q_{j-1}})/2<3/2\), and thus \(\gamma<3/2<m\).
Choose the same sufficiently small positive label vector as in the preceding
example, using this example's \(\gamma\) and \(\beta\).

Both independently trained dense runs fit at both sphere points. Their
endpoint difference on the *entire sphere* is therefore zero with probability
tending to one. Under the stated denominator convention, this excludes (1)
for Legendre and Harmonic as well. It also applies to Taylor on these inputs.

This example uses antipodal training points. They are admitted by the current
compression setup and by the proposed addition of nonaffinity alone. It is
not a counterexample under an additional nonparallel-training assumption or
under \(d\ge2\). Even if either restriction were added, Section 2 would still
obstruct the unrestricted Taylor passive-panel claim.

## 4. Different late-time rates are a separate conditional obstruction

The following is a deterministic statement; it does not assume a neural-network
model. It applies to a training-only panel, or to the antipodal panel of Section
2 after identifying repeated output coordinates. Equip its finite output space
with the maximum norm. Suppose that for one width the three residual vectors
have asymptotic expansions

\[
\begin{aligned}
f_n(t)-y&=u e^{-at}+o(e^{-at}),\\
\widetilde f_n(t)-y&=\widetilde u e^{-bt}+o(e^{-bt}),\\
f_{\rm model}(t)-y&=u_C e^{-ct}+o(e^{-ct}),
\end{aligned}
\tag{6}
\]

where \(u,\widetilde u,u_C\) are nonzero vectors, the little-oh statements
hold in that norm, and \(a,b,c>0\). If \(b>a\), then

\[
\|f_n(t)-\widetilde f_n(t)\|_\infty
=e^{-at}(\|u\|_\infty+o(1)).
\tag{7}
\]

If also \(c>a\), the analogous numerator is
\(e^{-at}(\|u\|_\infty+o(1))\), so its ratio to (7) tends to one.
If instead \(c<a\), the numerator is
\(e^{-ct}(\|u_C\|_\infty+o(1))\), and the ratio diverges to infinity.
These conclusions follow by dividing the differences in (6) by the slowest
exponential; nonzero leading vectors make the denominator eventually positive.

Therefore, if the event that (6) holds with \(b>a\) and \(c\ne a\) has
probability bounded below along a width subsequence, the supremum over finite
positive times cannot converge to zero in probability. This remains true if
one defines the fitted \(0/0\) value to be zero. In particular, rate
differences may be arbitrarily small as width increases: the supremum over
all times is taken separately at each width.

No claim is made here that current Legendre or selected dynamics satisfy the
spectral hypotheses on an event of nonvanishing probability. Such a claim
would require a proof of their residual asymptotics, nonzero leading
coefficients, and actual rate differences. Small absolute approximation error
does not prove those premises.

For a fully explicit illustration of the distinction between quantifiers, the
three scalar analytic curves

\[
f_n(t)=1-e^{-t},\qquad
\widetilde f_n(t)=1-e^{-(1+n^{-1/2})t},\qquad
f_{\rm model}(t)=1-e^{-(1+n^{-1})t}
\]

share zero initialization and fitted value one. Their pointwise error ratio is

\[
\frac{1-e^{-t/n}}{1-e^{-t/\sqrt n}}.
\]

For each fixed \(t>0\) this tends to zero, but its supremum over \(t>0\)
is one at every width. These curves are an illustration of the logical issue,
not an admissible independently initialized neural-network counterexample.

## 5. Consequence and remaining scope

Under the existing zero-denominator convention, adding only layerwise
nonaffinity cannot yield (1) on all current domains. Sections 1–3 prove actual
admissible obstructions. The ratio of trajectory suprema currently established
in the manuscript is unaffected: its denominator can have a positive-time
witness even when the endpoint denominator is zero.

If the convention is changed, these exact endpoint examples alone no longer
disprove the resulting statement. Nor does proving a positive endpoint
denominator for a restricted domain establish a simultaneous lower bound at
all intermediate times. A new proof or counterexample would be needed for the
revised problem. Section 4 isolates one sufficient mechanism for substantive
failure without asserting it for the current constructions.

## Check and provenance

The scoped author checked both Gaussian expectation formulas directly from the
cosine characteristic function, both strict Gram-gap inductions, the label
scaling, exact architectural symmetry, fitting-event probability, and the
late-time norm limits. These are direct proofs without simulation or external
theorem dependencies beyond the supplied fitting lemma. No independent check
or promotion review has occurred in this file.

Source HEAD at inspection: `ef8362764b4eb8144d7af8d6f8db080fdaaf82ca`.
The index was empty. Existing concurrent changes were preserved. Source SHA-256:

```
460f29eda118ffe5bbc24be3a04d1a25c5e4a9bddb0744f8235d97a3674cabfe  paper/compact.tex
6efe077759c846c4b3d79f999c37d2d1478bae549d49fc9666837efbf9f1a01f  paper/compact_fitting.tex
3add2b694f38a4d7dbce90e51dafd375a7e8dee2e06d26b2d5af451bddb44885  paper/compact_selected.tex
862aa37139ad9af67ac04b52949f838031e91077021b2da9060244d36ab4e0f9  paper/compact_legendre.tex
f03155050f7ab9dcbe8567bb53b148da294c0c11d3bb0147dd294f2692e7403f  paper/feature_learning_theorem.tex
```
