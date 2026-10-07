# Local Gaussian kernels avoid one particular depth amplification

2026-10-06. Scoped exact-real author lemma. No experiment, finite-bit
implementation claim, complete compact bridge, or independent review.

The proposed augmentation works at complete matrix-call boundaries.
Match the marginal next physical answer, and attach to both laws the
approximate programme's conditional law of the newly acquired innovation
moments given that answer. Their joint total variation is then exactly
the total variation of the answer marginals. The attached moments add
no information about the hidden initialized matrix conditional on the
answer, so the next exact Gaussian posterior formula remains valid.

This removes the repeated amplification through the scalar-history graph
from the **matrix-law comparison**. It does not compare the programme
using noisy physical reductions to the programme using exact physical
reductions. That remaining comparison needs a physical forcing estimate.

## 1. Objects and scope

The only scientific inputs for this derivation are the complete
`NOISY_TWO_ORIENTATION_TRANSCRIPT.md`,
`NOISY_SCALAR_HISTORY_ACQUISITION.md`, and
`PHYSICAL_NOISY_PROGRAM_BRIDGE.md`. Their matrix labels, orientations,
normalizations, and positive answer-noise level \(0<\sigma\le1\)
are retained. The initial matrices have independent entries of variance
\(1/n\). The physical neural model and its original assumptions are
unchanged; this is a finite-program law lemma, not a new flow theorem.

Let \(H\) be a complete observable history before a matrix call. It
contains the external initial fields, every earlier raw matrix answer,
queries determined from those answers, and scalar acquisitions. It does
not contain raw matrix-oracle noise vectors or unconsumed future row
innovations. Conditional on \(H\), all
previous row fields and the next query are fixed.

For one matrix, let \(U,V\) collect its old reverse and forward queries,
and \(X,Y\) their observed answers. Their column counts are at most
\(R\), the total call bound. The true Grams and cross moments are
exact functions of \(H\), for example
\(K=U^TU/n\), \(Q=V^TV/n\), \(U^TY/n\), and \(X^TV/n\).
At the time an entry is acquired, the approximate programme records
its exact empirical value plus \(\eta e\), with fresh scalar
\(e\sim N(0,1)\). Old fields retain their creation-time arguments.
Thus an old acquired pair remains the pair of those same old fields.
No evolving-field reinterpretation of an old scalar is allowed.

The original exact posterior gives a new forward answer law

\[
       y\mid H\sim N(m,\Gamma),\qquad
       \Gamma=S^2,\qquad S\succeq\sigma I_n,
\]
\[
       S=\sqrt\beta I_n+\frac1nU T U^T.                  \tag{1}
\]

Here \(m\) is the explicit linear combination of \(Y,U\), and
\(\beta,T\) are the gapped small-matrix functions in the assigned
two-orientation note, equations (13), (21), and (24)--(30). Its formulas
apply to true moments at the currently fixed history, regardless of how
the predictable queries were selected. Reverse calls exchange the two
orientations.

Evaluate the same protected coefficient functions at the acquired noisy
moments, obtaining \(\widetilde m,\widetilde\beta,\widetilde T\).
Freeze these coefficients **before** introducing the fresh innovation
cross moments. Put

\[
 A=U^T/n,\qquad B=U\widetilde T,\qquad
 \widetilde S=\sqrt{\widetilde\beta}I_n+BA.
\]

The approximate raw next-answer construction is

\[
 g\sim N(0,I_n),\quad e\sim N(0,I_s),\quad g\perp e\perp H,
 \qquad t=Ag+\eta e,
\]
\[
 y=\widetilde m+Bt+\sqrt{\widetilde\beta}\,g
          =\widetilde m+\widetilde Sg+\eta Be.             \tag{2}
\]

Here \(s\le R\) is the number of columns in \(U\). This is the
specified scalar-noisy innovation update, not independent noise added
to each answer coordinate. In particular,

\[
 y\mid H\sim N(\widetilde m,\widetilde\Gamma),\qquad
 \widetilde\Gamma=\widetilde S^2+\eta^2BB^T.              \tag{3}
\]

The additional covariance in (3) has rank at most \(R\). Its size
includes a factor \(n\) from the unnormalized matrix \(U\).

## 2. Exact augmentation lemma

Let \(Q_H(dy,dt)\) be the joint Gaussian kernel in (2), and let
\(Q_H(dt\mid y)\) denote its conditional law. Define an ideal
augmented call by

\[
 y=Wq+\sigma\xi,\qquad \xi\sim N(0,I_n)
       \text{ fresh and hidden},\qquad
 t\mid(H,y,W)\sim Q_H(dt\mid y).                         \tag{4}
\]

Its scalar augmentation uses an additional independent random source;
it does not depend on \(W\) after \((H,y)\) are fixed.

**Lemma 1.** If the posterior of \(W\) at \(H\) is the usual noisy
Gaussian-matrix posterior, then (4) preserves that posterior after the
new answer, and

\[
 \|Q_H(dy,dt)-P_H(dy)Q_H(dt\mid y)\|_{\rm TV}
       =\|N(\widetilde m,\widetilde\Gamma)
                            -N(m,\Gamma)\|_{\rm TV}.     \tag{5}
\]

**Proof.** The conditional likelihood of \(t\) in (4), at fixed
\((H,y)\), is a factor independent of \(W\); it cancels in Bayes'
formula. Therefore \(W\mid H,y,t\) has the same law as
\(W\mid H,y\). The same argument works jointly for all matrix labels
and preserves their conditional independence. Future queries may depend
on \(t\), because it is now an ordinary observable argument.

For (5), integration of the signed difference against their common
conditional probability kernel gives the upper bound by the marginal
total variation. Projection onto \(y\) gives the reverse inequality.
Equivalently, use their common conditional density and integrate its
absolute difference. QED.

There is no implicit conditional-law oracle in the approximate algorithm:
it still implements (2). Formula (4) is a proof-only alternative process.
It is also explicit. If
\(K_t=AA^T+\eta^2I_s\) and
\(K_{ty}=A\widetilde S+\eta^2B^T\), then

\[
 Q_H(t\mid y)=N\bigl(K_{ty}\widetilde\Gamma^{-1}
                         (y-\widetilde m),
           K_t-K_{ty}\widetilde\Gamma^{-1}K_{ty}^T\bigr). \tag{6}
\]

The joint covariance is positive definite when \(\eta>0\) and
\(\widetilde\beta>0\): the block map from \((g,e)\) to \((y,t)\)
has determinant \(\eta^s\widetilde\beta^{n/2}\), as subtraction
of \(Bt\) from \(y\) makes it block triangular. Thus (6) is an
ordinary conditional Gaussian distribution. The zero-history case
\(s=0\) simply omits \(t\).

Any innovation field needed later can be reconstructed as
\(g=(y-\widetilde m-Bt)/\sqrt{\widetilde\beta}\). In the ideal
augmentation it need not be an independent standard Gaussian. Revealing
this reconstructed field adds no information beyond \((H,y,t)\), so
it does not change the preceding posterior argument. Subsequent noisy
scalar reductions of observable fields can use their identical ordinary
Gaussian scalar kernels in both processes; their conditional likelihoods
are again independent of \(W\).

## 3. An explicit one-call total-variation estimate

Assume the old physical fields and the new query have RMS at most
\(b\ge1\). Enlarge \(b\) to cover any other moment-generating fields
used by the current protected coefficient call. Assume every scalar
moment error entering that call has magnitude at most \(\eta u\),
where \(u\ge1\). A PSD projection leaves the true consistent Gram
unchanged and does not enlarge its Frobenius error, so its dimension
factors can be included in the one-call estimate below.

The assigned scalar-history note, equation (6), supplies absolute
one-call coefficient and Lipschitz bounds with exponent 100. After
including dimensions and universal constants, take

\[
             z=C(2+R+b+\sigma^{-1})\ge10,
             \mathcal L=z^{100}.                         \tag{7}
\]

This bounds the coefficient norms and their change divided by the
maximum input-moment error, including the mean coefficient vectors,
\(\sqrt\beta\), and \(T\). It is a one-call estimate on the protected
domain, not an induction through the scalar history. Write
\(D_0=4(1+Rb^2)\mathcal L\). Since
\(\|U\|_{\rm op},\|Y\|_{\rm op}\le\sqrt{nR}\,b\),

\[
 \|\widetilde m-m\|_2\le\sqrt n D_0\eta u,
 \qquad \|\widetilde S-S\|_{\rm op}\le D_0\eta u.         \tag{8}
\]

On the genuine domain \(\|S\|_{\rm op}\le\sqrt{\sigma^2+b^2}\).
If \(D_0\eta u\le\sigma/2\), then
\(\widetilde S\succeq\sigma I/2\) and
\(\|\widetilde S\|_{\rm op}\le2b\). Expanding the difference of
the squared matrices in (3), without assuming they commute, gives

\[
 \|\widetilde\Gamma-\Gamma\|_F
       \le4b\sqrt n D_0\eta u
                           +\eta^2 nRb^2\mathcal L^2.    \tag{9}
\]

Indeed \(\widetilde S^2-S^2=(\widetilde S-S)\widetilde S
+S(\widetilde S-S)\), and
\(\|BB^T\|_F\le\|B\|_F^2\le nRb^2\mathcal L^2\).

For two Gaussian laws with reference covariance
\(\Gamma\succeq\sigma^2I\), put
\(E=\Gamma^{-1/2}(\widetilde\Gamma-\Gamma)\Gamma^{-1/2}\).
If \(\|E\|_{\rm op}\le1/2\), their relative entropy is

\[
 \frac12\{\|\Gamma^{-1/2}(\widetilde m-m)\|^2
                         +\operatorname{tr}E-\log\det(I+E)\}
 \le\frac12\{\sigma^{-2}\|\widetilde m-m\|^2
                  +\sigma^{-4}\|\widetilde\Gamma-\Gamma\|_F^2\}.
                                                               \tag{10}
\]

The formula follows by integrating the log ratio of Gaussian densities.
The inequality uses \(x-\log(1+x)\le x^2\) for \(|x|\le1/2\),
verified by integrating its derivative \(x/(1+x)\). The entropy-to-TV
inequality then bounds TV by half the square root of the bracket on the
right. This inequality itself follows by the log-sum reduction to a
binary event and the lower second-derivative bound
\(1/[p(1-p)]\ge4\) for binary relative entropy.

Combining (8)--(10), an explicit conservative statement is

\[
 \kappa=z^{220}(\sqrt n\,\eta u+n\eta^2)\le1/16
 \quad\Longrightarrow\quad
 \|Q_H-P_HQ_H(dt\mid y)\|_{\rm TV}\le\kappa.             \tag{11}
\]

The same condition implies both smallness requirements preceding (9)
and (10), after fixing the universal constant in (7). In particular it
also deals with the possible loss of positivity when the covariance
coefficients are computed from a noisy Gram but multiplied by the true
history fields. Positivity of a projected *noisy* Gram alone would not
establish that property for \(\widetilde S\).

## 4. Sequential composition and filtration boundaries

Use the same deterministic row operations and the same **noisy physical
scalar reductions** in the approximate and ideal augmented programmes.
At a shared history they have identical queries and row fields. Apply
Lemma 1 at each complete call. Maximal coupling of its two answer
marginals, followed by the same conditional \(t\) kernel on matching
answers, keeps the augmented histories exactly equal except with the
probability in (11). Continuing this construction through at most \(R\)
calls costs at most \(R\kappa\) on histories satisfying the displayed
bounds. Stop the argument at the first violation of a bound and add
the probability of that stop. This is a genuine kernel comparison;
there is no error recurrence multiplying earlier discrepancies.

For example, at desired accumulated TV \(0<\rho<1\), the concrete
choice

\[
        \eta\le\frac{\rho}{16Rz^{220}\sqrt n\,u}          \tag{12}
\]

gives \(R\kappa\le\rho/8\). There are at most \(P\) scalar noises;
under the approximate iid-packet programme their ordinary Gaussian
noise failure is at most \(2P e^{-u^2/2}\). Thus one may take
\(u=\sqrt{2\log(2P/\rho)}\), enlarged to at least one.
Field/cap failures remain separately charged. A stopped coupling may
bound different stopping causes on different marginals: use the
approximate marginal for its iid scalar-noise event and the ideal
physical marginal for an initialized-operator/raw-answer event. Prior
to a coupling failure the histories are identical, so the probability
of either stopping cause is bounded by its corresponding marginal
event plus the already charged coupling failures.

The sufficient logarithmic scalar-noise precision in (12) is

\[
 \log\eta^{-1}\le
 C+\log R+220\log z+\tfrac12\log n+\log u+\log\rho^{-1}, \tag{13}
\]

when choosing a dyadic \(\eta\) within a factor two below the right
side of (12). It contains no multiplier \(R\log(1/\sigma)\).
This statement exposes the dependence on the supplied cap \(b\): a
cap already chosen through global amplification cannot be called a
local improvement. The assigned physical bridge supplies polynomial
one-call innovation caps in \(R,\sigma^{-1}\), rather than a history
product, for its genuine noisy-matrix programme; transferring all needed
cap events to this modified physical programme is still an assembly task.

Two chronology qualifications are essential.

1. In the approximate row code, \(t\) can be acquired immediately
   before \(y\). The proof-only ideal samples the pair in the order
   \(y\), then \(t\). The Gaussian posterior assertion is at the
   completed \((y,t)\) boundary. At the intermediate prefix revealing
   only \(t\), the ideal matrix posterior need not be Gaussian. No
   new physical matrix call may be inserted there using the completed-
   boundary formula. Grouping each such pair into one kernel nevertheless
   controls the law of its entire recorded finite transcript, and all
   projections of that transcript, by total variation.
2. The fresh \(t\) must enter (2) only through its stated affine term.
   A protection that mixes \(t\) into a fresh PSD projection or otherwise
   changes \(\widetilde\beta,\widetilde T\) after seeing \(t\) destroys
   the Gaussian marginal calculation (3). Keep innovation moments outside
   that coefficient protection, as their separate range treatment in the
   assigned physical bridge permits.

Likewise (2) uses raw Gaussian \(g\). A legacy finite root cap applied
before (2) requires a separate coupling to the uncapped Gaussian stream,
with its iid Gaussian union failure charged. Deterministic caps after
the raw answer are common postprocessing and cannot increase TV. The
raw answers must remain in the proof filtration; conditioning only on
clipped answers would not have the Gaussian likelihood of the input note.

## 5. Exact remaining physical obstruction

The augmentation does not preserve the old ideal law of every scalar.
It intentionally replaces the ideal innovation-moment conditional law
by (6). Moreover, ordinary physical reductions must be noisy in both
programmes for the shared-history comparison in Section 4. The ideal
therefore executes a physical matrix programme with perturbed scalar
reductions, not the original exact-reduction programme.

This distinction cannot be erased by an exact-real joint-TV argument.
For a fixed observable vector history \(H\), suppose the exact next
physical scalar is \(a(H)\), whereas the approximate one is
\(a(H)+\eta e\), \(\eta>0\). The laws of
\((H,a(H))\) and \((H,a(H)+\eta e)\) have TV one: the measurable
graph \(\{(h,c):c=a(h)\}\) has probability one for the former and
zero for the latter. The obstruction persists for a deterministic
subsequent vector operation if its graph distinguishes the two values.
Adding (6) to innovation moments does not smooth this different scalar
operation.

What remains necessary is a physical perturbation estimate for the
**same noisy-reduction algorithm**, expressed at fixed physical state:
bound the error in its learned-matrix actions, norm projections and
gradient field caused by replacing the relevant exact pair reductions
with their noisy versions, then propagate those defects through the
controlled solver. Section 3 of `PHYSICAL_NOISY_PROGRAM_BRIDGE.md`
provides that kind of forcing argument for matrix-answer noise, but
not for these physical scalar reductions. Its Section 5 instead uses
the global row-history estimate being replaced here. Thus the required
scalar forcing interface is an identified missing input, not a theorem
already supplied by the three notes.

The local result is nevertheless unconditional within its stated
finite Gaussian-call scope: the augmentation (4), explicit conditional
kernel (6), one-call estimate (11), and stopped sequential coupling are
fully constructed above. They settle the proposed matrix-law mechanism.
They do not prove finite-bit stability of roots or arithmetic, a useful
complete computational cost, source acquisition precision, a posterior
decoder theorem, or the original all-time compact approximation. No
claim about those bridges is obtained by equating their assumptions
with the desired conclusion.

The rigorous-mathematics and conjecture workflow instructions and the
canonical-notation skill with its neural reference remain current and
were applied. No other source, current route, study, or experimental
result was read. Only this assigned note was written in this subtask.
