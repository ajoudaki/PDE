# Whole-query backward sources remove the remaining sample-family factor

2026-10-04. **Internally checked source refinement.** The independent
reconstruction in
[WHOLE_QUERY_RESPONSE_CHECK.md](WHOLE_QUERY_RESPONSE_CHECK.md) passed
at report SHA-256
`dfefa67af9a7d8b7a9b1d7a279169b5cc8d6efe7b29ad4092853f121907524ce`.
The author derivation before this status update had SHA-256
`9c762455cf049a1fd025c4125775b988cc3735d26a80f0204d273c89741bda69`.
This is an internal study check, not a promotion review.

**2026-10-04 label update.** The independently checked
[LABEL_SEPARATE_BUDGETS.md](LABEL_SEPARATE_BUDGETS.md), with complete
[check](LABEL_SEPARATE_BUDGETS_CHECK.md), supplies the inherited complex
source and training-carrier event under Y<=c lambda. This supersedes the
smaller sufficient range (3), which is retained below as the historical
input to the original derivation. No approximation or dimension argument
in this note changes. Both complete check reports were read before this
update.

The existing source theorem already implies an initialization-only source
space of dimension

\[
 R\le C\lambda^{-1}[\log(en)]^{d(L+5)+1},                 \tag{1}
\]

with no additional m times a temporal degree. The key is that analytic
approximation needs the logarithm of a source's magnitude: a bound
C sqrt(n) is sufficient. The new whole-query backward families have this
crude bound on the already proved complex forward domain. No uniform
polylogarithmic query-carrier theorem, additional Gaussian conditioning,
or population approximation is required.

This bounded continuation uses the complete DEEP_COMPLEX_SOURCE.md,
DEEP_ACTIVATION_EXTENSION.md, DATASET_SOURCE_CONSTANTS.md,
DATASET_MAXIMUM_REFINEMENT.md, and the previous assigned compression and
comparison notes. The coordinator supplied the polynomial-magnitude
observation after those source inputs were read. During that derivation,
no other studies, other current routes, experiments, or maintained-book
files were read or changed. The subsequent status update reads only the
explicitly authorized check reports identified above.

## 1. Fixed model and inherited complex event

The reference remains the canonical width-n Gaussian deep model with
hidden depth L, normalized inputs v=x/sqrt(d), and forward equations

\[
 z^{(1)}(t,x)=A(t)v,\quad h^{(l)}(t,x)=\phi_l(z^{(l)}(t,x)),
 \quad z^{(l)}(t,x)=W^{(l)}(t)h^{(l-1)}(t,x)\ (l\ge2),
 \qquad f_n(t,x)=w(t)^\top h^{(L)}(t,x)/n.                \tag{2}
\]

A(0) has independent N(0,1) entries, hidden W(0) have independent
N(0,1/n) entries, all arrays are independent, and w(0)=0. Training uses
squared mean loss and mobilities (n,1,...,1,n). There are m fixed sphere
training inputs and fixed labels with RMS Y. The activations are real on
the real axis, holomorphic and bounded on a common strip of width b.
Let Q^(L) be the existing initialized limiting top-feature covariance and

\[
 \lambda=\min\{1,\lambda_{\min}(Q^{(L)}/m)\}>0,
 \quad \ell_n=\log(en),\quad S=C_0Y/\lambda.
\]

Constants C,c below depend only on d,L,b and the common strip bound.
Retain the checked full-source sufficient label class

\[
 0<Y\le c\lambda\exp\{-C\sqrt{\log(em)}\}.             \tag{3}
\]

This historical range ensures fixed small S and the carrier-budget
conditions in DATASET_MAXIMUM_REFINEMENT.md. The dated label update above
supersedes (3) by Y<=c lambda using the separately checked proof-budget
change. Zero labels give the separately exact zero model.

Write x=sqrt(d) v(theta), using the fixed (d-1)-angle periodic sphere
parameterization from the source theorem. On its high-probability event,
the actual parameter solution is holomorphic in the time neighborhood
of

\[
 -r_n\le\Re t\le T+r_n,\quad |\Im t|\le r_n,
 \qquad T=C\lambda^{-1}\ell_n,\qquad
 r_n=c\ell_n^{-(L+4)}.                                  \tag{4}
\]

The query forward pass is jointly holomorphic there and on
|Im theta_j|<=r_n; every query preactivation stays in a strictly narrower
safe activation strip. The same event supplies

\[
 \sup_t\max_{l\ge2}\|W^{(l)}(t)\|_{\rm op}\le K,
 \quad \sup_t\|w(t)\|_\infty\le CS,
 \quad \max_l\|W_0^{(l)}\|_{\rm op}\le K_0,              \tag{5}
\]

with structural K,K_0. These are the complex operator/readout estimates
in DEEP_COMPLEX_SOURCE.md, equation (15), after its stopping conditions
are removed in Sections 6--8. The activation and quantitative constant
extensions justify them under (3). The usual complex norm is used in (5);
all transposes in the analytic formulas remain algebraic transposes,
without complex conjugation. Shrinking r_n by a structural factor, if
needed, retains (4) and provides a neighborhood of the closed domain.

## 2. Jointly holomorphic backward fields for every query

For any complex query angle on this same domain define

\[
 \begin{aligned}
 k^{(L)}(t,\theta)&=w(t),\\
 \delta^{(l)}(t,\theta)
   &=\phi_l'(z^{(l)}(t,\theta))\odot k^{(l)}(t,\theta),\\
 k^{(l)}(t,\theta)
   &=W^{(l+1)}(t)^\top\delta^{(l+1)}(t,\theta),\quad l<L.
 \end{aligned}                                               \tag{6}
\]

At a training angle theta_a these are precisely the actual backward
responses of the original trained model. Elsewhere they are passive
queries of those same current parameters; they add no training example,
loss term, residual, or force to the reference flow.

Holomorphy follows downward from w(t). Each step consists of the
holomorphic scalar derivative phi_l' evaluated at a pole-safe holomorphic
forward field, coordinate multiplication, and a finite matrix product.
Cauchy's formula on the fixed activation strip bounds |phi_l'| by a
structural D_1. Therefore

\[
 \begin{aligned}
 \|\delta^{(l)}(t,\theta)\|_2
 &\le D_1(KD_1)^{L-l}\|w(t)\|_2\le CS\sqrt n,\\
 \|W_0^{(l+1)\top}\delta^{(l+1)}(t,\theta)\|_2
 &\le K_0\|\delta^{(l+1)}(t,\theta)\|_2\le CS\sqrt n.
 \end{aligned}                                               \tag{7}
\]

The same estimates hold uniformly over the entire joint complex domain.
Since a coordinate magnitude is at most its Euclidean norm, (7) provides
the required coordinate bound. The forward sources also have a bound
C sqrt(n): h has bounded coordinates and W_0 h has Euclidean norm at most
K_0 B_phi sqrt(n). Thus all four whole-query families

\[
 h^{(l)}(t,\theta),\quad
 W_0^{(l)}h^{(l-1)}(t,\theta),\quad
 \delta^{(l)}(t,\theta),\quad
 W_0^{(l+1)\top}\delta^{(l+1)}(t,\theta)                  \tag{8}
\]

are jointly holomorphic on the same domain, with coordinate magnitude
at most C sqrt(n). The first and third families occur at every layer;
the matrix-image families have their natural adjacent-layer ranges.
There are a fixed number of families per layer, independent of m.

This is an exact finite-network deduction from (4)--(5). It does not
claim that a Gaussian initialized column remains independent of the
trained query field. No conditional Gaussian law for such an adaptive
field is used.

## 3. Why the square-root-width bound costs no new width power

Set the target coordinate approximation tolerance to epsilon=n^-1.
A holomorphic function bounded by M_n on the time strip (4) has a
polynomial approximation error bounded by
C M_n (T/r_n) exp(-c p r_n/T), with temporal degree p, up to the
fixed-dimensional tensor factors already accounted for in the source
construction. Angular Fourier truncation has the corresponding factor
C M_n r_n^-(d-1) exp(-c r_n J), where J is the degree in each angle.
The relevant numerator is logarithmic:

\[
 \log(M_n/\epsilon)\le C+\tfrac32\log n
                         \le C\ell_n,\qquad M_n=C\sqrt n. \tag{9}
\]

Hence the larger coordinate magnitude changes degree constants, not the
powers of log(n). To expose the small remaining logarithmic gap factor,
put

\[
 q_n=\ell_n+\log(e/\lambda).
\]

The elementary ellipse/Fourier tail estimates, including their polynomial
prefactors and interpolation aliasing factors, allow

\[
 p\le C\lambda^{-1}\ell_n^{L+5}q_n,\qquad
 J\le C\ell_n^{L+4}q_n.                                 \tag{10}
\]

Indeed T/r_n=C lambda^-1 ell_n^(L+5), 1/r_n=C ell_n^(L+4),
and the logarithms of all prefactors are bounded by C q_n. Choosing a
larger structural multiplier in (10) controls the finitely many source
families simultaneously. No accuracy demand proportional to 1/M_n is
imposed on the degree itself.

For each family the real algebraic/trigonometric coefficient-vector count
is at most (p+1)(2J+1)^(d-1). Therefore the complete coefficient span at
each layer has dimension at most

\[
 C\lambda^{-1}\ell_n^{d(L+4)+1}q_n^d.                    \tag{11}
\]

For widths with log(e/lambda)<=ell_n this becomes
C lambda^-1 ell_n^[d(L+5)+1], as claimed. Alternatively one can retain
(11) with its explicit logarithmic gap factor at every width for which
the source event is available. This condition absorbs only log(lambda^-1)
and does not replace any polynomial sample factor by a width threshold.

## 4. Exact initialization, paired images, and preprocessing

The compression bridge additionally retains exact initialized training
features, their initialized forward images, and the d first-weight columns.
These add O(m+d) vectors per layer. The existing trace bound gives

\[
 m\lambda\le\lambda_{\min}(Q^{(L)})
       \le \operatorname{tr}(Q^{(L)})/m\le B_\phi^2.       \tag{12}
\]

Thus m<=B_phi²/lambda. Since ell_n,q_n>=1 and d is fixed, the extra
vectors are absorbed in (11) with structural constants. This is an
algebraic constraint already implied by bounded activations and the
chosen normalized gap; it holds independently of width. Optional O(m)
initialized motion-certificate vectors can be absorbed in the same way.
Consequently the former m temporal-family term is actually removed,
rather than dominated by a larger logarithmic power at a chosen width.

Construct the coefficients by the existing finite initialization-jet
procedure. Formula (6) defines every new query source from the original
parameter ODE and forward field, so its time derivatives at initialization
are obtained by finite differentiation of these formulas. Analytic
continuation from those derivatives to the finite interpolation grid is
exactly the procedure already allowed by the representation contract.
Increasing intermediate precision to offset the finite interpolation
operator norms adds no retained coordinates. No trained snapshots are
queried or stored.

For each lower forward source and its W_0 image, and each upper backward
source and its W_0^T image, use the same scalar interpolation and coefficient
operations. Since the initialized matrix is fixed and those operations
are linear, each pair has an exact coefficient-wise matrix-image relation.
Both members separately satisfy their coordinate error tolerance because
both were included among the uniformly bounded holomorphic families (8).
There is no deduction of coordinate approximation error from a matrix
operator norm. The original-width coefficient arrays are discarded after
the reduced initialization is formed.

## 5. Consequence for the quadratic-storage runtime

The deterministic bridge in STORAGE_QUADRATIC_IMPROVEMENT.md needs
coordinate approximation of training backward sources and both mixer
orientations. Restricting (8) to the training angles supplies exactly
those requirements. Its one-reference stability proof still uses the
existing training-only true-carrier estimate
max_{a,l,i,t}|k_{a,i}^(l)(t)|<=C S sqrt(ell_n). The crude sqrt(n) bound
in (7) is used only for source approximation and is never substituted
for that stability input. Thus the full-time C_data/sqrt(n) comparison,
including the endpoint, retains its stated constants and threshold.

Counting every fixed metric matrix, learned matrix, raw readout, internal
residual coordinate, and retained dataset as in that bridge gives

\[
 \begin{aligned}
 \mathrm{size}
 &\le C\lambda^{-2}\ell_n^{2d(L+4)+2}q_n^{2d}+Cm(d+1)\\
 &\le C\lambda^{-2}\ell_n^{2a}+Cm(d+1),\qquad
 a=d(L+5)+1,
 \end{aligned}                                               \tag{13}
\]

where the second line uses log(e/lambda)<=ell_n. When the gap cap is
inactive and gamma=lambda_min(Q^(L))=m lambda, this is

\[
          C\gamma^{-2}m^2\ell_n^{2a}+Cm(d+1).            \tag{14}
\]

There is no second m^4 term. Formula (13)'s first line is the version
retaining the logarithmic gap dependence explicitly. If the cap is active,
use lambda=min(1,gamma/m) directly; its inverse is max(1,m/gamma).

The combined runtime is the explicitly modified autonomous optimizer
from the quadratic-storage note, not ordinary reduced-network gradient
flow. This source refinement changes neither its equations nor the
reference model. Its conclusion has the same fixed-dataset quantifiers:
structural storage constants, finite dataset-dependent width threshold,
and probability at least 1-eta for each sufficiently large width. It does
not establish a joint growing-m theorem or practical preprocessing costs.
The source refinement and the separate runtime bridge have now passed
their independent internal checks, recorded here and in the runtime note.
The label update above changes only their inherited source regime.

## 6. Audit of the formerly suspected obstruction

A uniform polylogarithmic maximum for all passive-query carriers would
require extending the Gaussian insertion argument. Such an extension
would have to handle the dependence between trained weights and query
responses and would not follow from a finite grid by itself. This note
makes no claim that this stronger maximum theorem has been proved.

That theorem is unnecessary here. The inherited forward result already
provides joint holomorphy on a common query strip, and operator/RMS bounds
supply polynomial coordinate magnitudes. Analytic approximation depends
only logarithmically on these magnitudes. The source-space dimension and
the stability proof use different bounds for different purposes; keeping
them separate is what removes the extra source-family factor without an
unproved independence argument or a hidden power of m.
