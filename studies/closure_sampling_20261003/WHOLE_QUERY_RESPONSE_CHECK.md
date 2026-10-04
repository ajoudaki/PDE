# Independent check of whole-query backward source compression

2026-10-04. Scoped internal reconstruction of the supervisor's proposal.
The complete allowed scientific inputs were
`DEEP_COMPLEX_SOURCE.md`, `DEEP_ACTIVATION_EXTENSION.md`,
`DATASET_SOURCE_CONSTANTS.md`, `DATASET_MAXIMUM_REFINEMENT.md`, and
`GENERAL_ANALYTIC_COMPRESSION.md`. The concurrently authored source
extension and other route reports were not read. No prior-study references
were followed, and no experiment or Git operation was performed.

**Verdict: the proposed source extension and its interfaces close.**
The existing complex parameter bounds and uniform query pole exclusion
give a deterministic holomorphic backward recursion for every sphere query.
Its coordinate magnitude can be bounded by \(CS\sqrt n\). That coarse
bound is sufficient for the same approximation degrees. Replacing the
\(m\) separate backward sources by a fixed number of query-dependent
families therefore yields

\[
R\le C\lambda^{-1}[\log(en)]^{d(L+5)+1}
\tag{1}
\]

for each layer's source-space dimension, including exact initialized
training features and the first-weight columns. The existing positive
cubature construction consequently gives total retained storage at most

\[
C\lambda^{-4}[\log(en)]^{4[d(L+5)+1]}+Cm(d+1).
\tag{2}
\]

The constants are structural, as specified below. The sharper label
condition and the comparison error in `DATASET_MAXIMUM_REFINEMENT.md`
are unchanged. This is conditional on the existing complex-source and
comparison theorems stated in the allowed inputs; it is not a new review
of their earlier stochastic insertion proofs or of the full comparison
proof outside the assigned input scope.

## 1. Model and the exact inherited hypotheses

The normalized training inputs are \(v_a=x_a/\sqrt d\in S^{d-1}\), with
fixed \(d\ge2\), fixed hidden depth \(L\ge2\), and fixed sample count
\(m\). The finite network is

\[
z^{(1)}(t,v)=A(t)v,\qquad h^{(\ell)}(t,v)=\phi_\ell(z^{(\ell)}(t,v)),
\]
\[
z^{(\ell)}(t,v)=W^{(\ell)}(t)h^{(\ell-1)}(t,v)\quad(\ell\ge2),
\qquad f_n(t,v)=\frac1n w(t)^\top h^{(L)}(t,v).
\tag{3}
\]

Initialization has independent \(N(0,1)\) entries in \(A_0\), independent
\(N(0,1/n)\) entries in each \(W_0^{(\ell)}\), and \(w_0=0\).
Each activation is real on the real axis and bounded by \(B_\phi\) on
the strip \(|\operatorname{Im}z|<b\), where it is holomorphic. The loss
is \(m^{-1}\sum_a(y_a-f_n(v_a))^2\), with mobilities
\((n,1,\ldots,1,n)\), exactly as in the allowed compression theorem.

Define the deterministic initialized covariance and normalized gap by

\[
Q^{(0)}_{ab}=v_a^\top v_b,\qquad
Q^{(\ell)}_{ab}=\mathbb E[\phi_\ell(Z_a)\phi_\ell(Z_b)],
\quad Z\sim N(0,Q^{(\ell-1)}),
\]
\[
\lambda=\min\{1,\lambda_{\min}(Q^{(L)})/m\}>0,
\qquad Y=\left(\frac1m\sum_a y_a^2\right)^{1/2}.
\tag{4}
\]

Take the existing full-source sufficient condition

\[
0<Y\le c\lambda\exp\{-C\sqrt{\log(em)}\},
\qquad S=C_0Y/\lambda.
\tag{5}
\]

In particular \(S\) is bounded by a fixed small structural constant.
The zero-label case is stationary. Structural constants in this check
depend only on \(d,L,b,B_\phi\), including fixed bounds for activation
derivatives on narrowed strips. They are independent of
\(m,\lambda,Y,n\). Width thresholds keep all dependencies already
specified in the allowed inputs.

Write \(\ell_n=\log(en)\), \(K=L+4\), and

\[
T=C_T\lambda^{-1}\ell_n,\qquad r=c\ell_n^{-K}.
\tag{6}
\]

The existing source theorem, its activation extension and the quantitative
constant audit give, on their successful initialization event, a holomorphic
parameter solution on a neighborhood of the closed time rectangle

\[
-r\le\operatorname{Re}t\le T+r,\qquad
|\operatorname{Im}t|\le r,
\tag{7}
\]

and uniform forward-query pole exclusion on its product with
\(|\operatorname{Im}\theta_j|\le r\), using a periodic sphere map
\(v(\theta)\). In addition, after the stops are removed, equation (15)
of `DEEP_COMPLEX_SOURCE.md` and its quantitative audit give

\[
\max_{\ell\ge2}\|W^{(\ell)}(t)\|_{\mathrm{op}}\le C,
\qquad \|w(t)\|_\infty\le CS,
\qquad \max_{\ell\ge2}\|W_0^{(\ell)}\|_{\mathrm{op}}\le C.
\tag{8}
\]

The parameters depend only on time, not on the passive query angles.
The stop-removal argument provides actual existence and strict strip
margins on this domain, rather than bounds that hold only up to an
uncontrolled stopping time. If necessary replace \(r\) by \(r/2\)
throughout this check; that changes only structural constants.

## 2. The additional query response is a deterministic analytic object

For every query, define the backward objects by the finite descending
recursion

\[
k^{(L)}(t,v)=w(t),\qquad
\delta^{(\ell)}(t,v)=
\phi_\ell'(z^{(\ell)}(t,v))\odot k^{(\ell)}(t,v),
\]
\[
k^{(\ell)}(t,v)=W^{(\ell+1)}(t)^\top
\delta^{(\ell+1)}(t,v)\quad(\ell<L).
\tag{9}
\]

At a training input these are exactly the existing training responses.
For other queries they are passive observations of the same finite
parameter trajectory. They do not add a force to its ODE, introduce
external residuals, or posit a population training process.

The preactivations in (9) already lie inside a fixed strip strictly
narrower than the activation strip. Cauchy's formula gives a structural
bound \(|\phi_\ell'|\le D_1\) there. Every operation in (9) is
holomorphic: the transpose is algebraic, with no complex conjugation,
and the recursion has finite depth. Thus
\(\delta^{(\ell)}(t,v(\theta))\) is jointly holomorphic in time and
angles on the same domain as the forward features.

For complex matrices the Euclidean operator norm satisfies
\(\|W^\top\|_{\mathrm{op}}=\|W\|_{\mathrm{op}}\). Therefore (8) gives

\[
\|k^{(L)}(t,v)\|_2\le CS\sqrt n,
\qquad
\|\delta^{(\ell)}(t,v)\|_2+
\|k^{(\ell)}(t,v)\|_2\le C_L S\sqrt n
\tag{10}
\]

by downward induction, uniformly over the complex time/angle domain.
The constant contains only a fixed number of factors from \(D_1\) and
the operator bound. In particular

\[
\max_i|\delta_i^{(\ell)}(t,v)|\le CS\sqrt n,
\qquad
\max_i|[W_0^{(\ell+1)\top}\delta^{(\ell+1)}(t,v)]_i|
\le CS\sqrt n.
\tag{11}
\]

No stochastic estimate for a maximum over query responses is needed.
The normalized Euclidean bound in (10), unlike its coordinate consequence,
is still \(CS\). The initialized transpose image is bounded directly
by (8); it need not be obtained by subtracting learned transpose actions.

For completeness, the four families now used, with natural layer ranges,
are

\[
h^{(\ell)}(t,v),\qquad
W_0^{(\ell)}h^{(\ell-1)}(t,v),\qquad
\delta^{(\ell)}(t,v),\qquad
W_0^{(\ell+1)\top}\delta^{(\ell+1)}(t,v).
\tag{12}
\]

All are jointly holomorphic. There are at most four such families per
layer, independent of \(m\). They share the safe coordinate magnitude
bound \(C\sqrt n\): gates are bounded, their initialized forward image
has Euclidean bound \(C\sqrt n\), and (11) handles the reverse families
using \(S\le c\). The sharper existing forward bounds remain true but
are not needed for the degree estimate.

## 3. Polynomial magnitude preserves the approximation degrees

Use absolute coordinate tolerance \(\epsilon=n^{-1}\). A Bernstein
ellipse for \([0,T]\) with log parameter \(\tau\asymp r/T\) lies
inside (7). Moving Fourier contours in the angular variables by a fixed
fraction of \(r\) gives joint coefficient decay of the form

\[
|a_{q,k}|\le C M_n e^{-cqr/T}e^{-cr|k|_1},
\qquad M_n=C\sqrt n,
\tag{13}
\]

for each coordinate of (12). Truncating the time degree at \(p\) and
every angular degree at \(J\) consequently has a uniform tail bounded
by

\[
C M_n(T/r)r^{-(d-1)}
\left(e^{-cpr/T}+e^{-crJ}\right).
\tag{14}
\]

Discrete cosine/Fourier interpolation has the same exponential estimates
after fixed changes in degrees and polynomial prefactors. Their logarithms
are harmless here. In fact

\[
\log(M_n/\epsilon)=\tfrac32\log n+O(1),
\]

and the remaining prefactors in (14) contribute only
\(O(\log\lambda^{-1}+\log\ell_n)\), with structural constants.
For sufficiently large width, including \(\ell_n\ge C\log(e/\lambda)\),
the choices

\[
p\le C\lambda^{-1}\ell_n^{L+6},\qquad
J\le C\ell_n^{L+5}
\tag{15}
\]

achieve the required tolerance. These are the existing powers. In particular
\(\sqrt n\) in a source magnitude does not become a \(\sqrt n\) degree
or retained-coordinate factor.

The number of real coefficient vectors per family is bounded by

\[
(p+1)(2J+1)^{d-1}
\le C\lambda^{-1}\ell_n^{L+6+(d-1)(L+5)}
=C\lambda^{-1}\ell_n^{d(L+5)+1}.
\tag{16}
\]

Fourier conjugate pairs can be represented by real sine/cosine
coefficients. Constant factors from real representation and the fixed
number of families are included in \(C\).

## 4. Initialization-only coefficients and exact paired matrix actions

The allowed `GENERAL_ANALYTIC_COMPRESSION.md`, Section 2, supplies the
finite initial-jet analytic continuation and interpolation procedure on
this time rectangle. Its contract permits unrestricted finite setup work,
temporary workspace and exact-real precision; only retained coordinates
are counted. The procedure uses finite derivatives at time zero to
approximate finitely many interpolation nodes to a specified positive
tolerance, then applies scalar discrete transforms.

The additional sources satisfy all of that procedure's hypotheses:
they are holomorphic on the same time domain and have an explicit finite
coordinate bound. Their initial time derivatives are computed by
differentiating the original finite-dimensional training ODE, the forward
pass and (9), all at time zero. Query angles are fixed interpolation-node
inputs during these calculations. Thus their coefficients require no
trained snapshots, observations of a trajectory, or supplied residual
path. A larger magnitude bound can increase the temporary initial-jet
order and work, but not the retained count (16).

The paired-vector interface deserves an exact check. Let \(u(t,\theta)\)
be a source and \(V_0u(t,\theta)\) its paired initialized matrix image,
where \(V_0\) is either \(W_0^{(\ell)}\) or
\(W_0^{(\ell+1)\top}\). Use the same time/angle nodes, truncation
orders, and finite scalar coefficient operations for the pair. At every
time derivative and every finite scalar operation,

\[
\partial_t^q(V_0u)=V_0\partial_t^q u,
\qquad \mathcal A[V_0u]=V_0\mathcal A[u],
\tag{17}
\]

because \(V_0\) is fixed and \(\mathcal A\) is linear and acts only on
the scalar time/angle variables. Take the maximum of all orders needed
for a pair, or a common order for all finitely many families. Then every
retained coefficient \(u_\alpha\) has its **exact** paired coefficient
\(V_0u_\alpha\) in the neighboring layer's space.

At the same time, each of the two polynomial approximants has its own
absolute coordinate error at most \(\epsilon\), because both source
families have the verified analytic magnitude bound. No coordinate error
is inferred by applying an operator norm to an \(\ell^\infty\) error.
For inexact node reconstruction by finite jets, choose the node tolerance
smaller than \(\epsilon\) divided by the finite interpolation operator
norm, simultaneously for both members of the pair. The jet operations
remain exactly linear, so (17) still holds. On the real axis all initialized
matrices are real; real coefficient extraction also commutes with them.

This checks the new source's interface with the existing initial-jet
construction. The continuation map and its finite-jet approximation are
inherited from the allowed general construction rather than rederived
from an unassigned reference.

## 5. Exact initialization, cubature and the improved space count

Let \(S_\ell\subset\mathbb R^n\) span the coefficient vectors assigned
to layer \(\ell\). As before, augment it by the initialized training
features \(h_a^{(\ell)}(0)\), by
\(W_0^{(\ell)}h_a^{(\ell-1)}(0)\) where applicable, and by the \(d\)
columns of \(A_0\) at the first layer. These exact additions ensure the
same initialized training forward pass and readout Gram after selection.
Their number is \(Cm+Cd\), not a further time-polynomial family count.
If the optional initialized feature-motion certificate is retained, its
paired vectors add another \(Cm\), with the same conclusion below.

Bounded initialized activations give the exact elementary relation

\[
m\lambda\le\lambda_{\min}(Q^{(L)})
\le\frac1m\operatorname{tr}Q^{(L)}\le B_\phi^2.
\tag{18}
\]

Therefore \(m\le B_\phi^2\lambda^{-1}\). Combining this with (16)
and \(\ell_n\ge1\), \(\lambda\le1\), proves (1), including all
initialization augmentations. The constants do not hide an additional
sample-count factor.

The existing positive cubature is insensitive to the magnitude of an
individual source coefficient. Normalize a real basis by
\(U_\ell^\top U_\ell/n=I\), and match the constant and all its pairwise
column products. It selects at most \(1+R(R+1)/2\) neurons per layer and
preserves the isometries used to construct the projected initialized edges.
The exact pairing (17) supplies the same forward and reverse initialized
action identities as before. Projection still bounds the weighted edge
operator norms independently of coefficient sizes, neuron counts and
minimum selected mass.

The retained full edge matrices cost \(O(R^4)\), first weights cost
\(O(dR^2)\), and readouts/masses cost \(O(R^2)\); retaining the training
data and labels costs \(O(md+m)\). Substituting (1) proves (2).
At fixed structural parameters, (18) also allows the data term to be
absorbed into the first term if one wants a single bound. Keeping it
visible records that the autonomous reduced model retains its training
data. For every fixed dataset and gap this storage is \(o(n)\).

## 6. Why the comparison keeps the training carrier bound

The new source spaces approximate every source required by the existing
comparison: evaluate their query-dependent polynomials at any training
input to obtain approximations to \(\delta_a^{(\ell)}\) and
\(W_0^{(\ell+1)\top}\delta_a^{(\ell+1)}\). Their errors are still
\(\epsilon\), and their exact coefficient pairing is unchanged.
The forward-query sources also retain the same errors.

The \(CS\sqrt n\) bound is used only to obtain the approximation degree.
It is not a replacement for the actual training carrier bound in the
comparison. On the existing real carrier event,

\[
M_{\mathrm{train}}:=
1+\max_{a,\ell,i,t\in[0,T]}|k_{a,i}^{(\ell)}(t)|
\le1+CS\sqrt{\ell_n}.
\tag{19}
\]

The trained hidden updates and the backward comparisons are evaluated at
training samples. The uniform query-output comparison uses forward query
features and the readout; it does not require comparing backward responses
at arbitrary queries. At a training input the polynomial approximation
itself has coordinate bound at most the actual training response maximum
plus \(\epsilon\). Thus no factor \(\sqrt n\) from (11) enters the
changed-gate carrier multiplication described in Section 4 of the allowed
general compression theorem.

Accordingly the quantitative comparison retained in the allowed dataset
audit and maximum refinement remains

\[
\sup_{t\le T,v}|f_C(t,v)-f_n(t,v)|
\le C e^{CY/\lambda^2}n^{-1}
e^{(CY^2/\lambda^3)\sqrt{\ell_n}}.
\tag{20}
\]

The same additional width requirement
\(\ell_n\ge C(1+Y^4/\lambda^6)\) absorbs the final exponential.
The same query tails then give

\[
\sup_{t\in[0,\infty]}\sup_{v\in S^{d-1}}
|f_C(t,v)-f_n(t,v)|
\le C e^{CY/\lambda^2}/\sqrt n,
\tag{21}
\]

including both fitted endpoints. The smaller weighted network still uses
its own forward pass, residuals and trained hidden matrices. Source
extension adds no forcing or frozen trained trajectory.

The full comparison proof was outside this check's permitted input list.
The claim here is that the explicitly stated source, pairing, initialization
and carrier hypotheses of its use in the allowed general construction
remain satisfied. No new comparison lemma is being asserted.

## 7. Adversarial checks and limits

The potentially fatal interfaces were checked as follows.

- **Complex parameter bounds:** the original parameter solution, not a
  surrogate, satisfies (8) after stop removal on the whole required time
  rectangle. Query angles do not alter its parameters.
- **Query poles:** forward query strip safety is already available before
  (9) is added; the new backward recursion is not used to prove its own
  pole exclusion.
- **Complex transposes:** algebraic transposes preserve holomorphy and
  have the same Euclidean operator norm. No Hermitian transpose appears
  inside the recurrence.
- **Polynomial source magnitudes:** only their logarithms enter (15);
  using them as comparison carriers would be invalid and is unnecessary.
- **Selection and both orientations:** (17) preserves paired coefficient
  actions exactly, and each orientation separately has coordinate error
  \(\epsilon\). The selection proof does not infer a coordinate estimate
  from an operator norm.
- **Initialization information:** all added initial jets follow by finite
  differentiation of the initialized ODE and query recursion; all later
  node values are finite analytic approximations, not trajectory samples.
- **Sample count:** the \(m\) training responses are covered by the query
  domain because all training inputs are on the sphere. For arbitrary
  off-sphere training inputs this replacement would require a new query
  domain or retention of their separate sources; that broader claim is
  not made here.
- **Exact initialization overhead:** its \(Cm\) count is absorbed using
  (18), not discarded. The raw training-data storage is also accounted for.

The original label condition (5), fixed-dataset order of limits, source
probability argument, dependence of the eventual width threshold on fixed
positive \(Y\), and unrestricted finite exact-real setup contract remain
unchanged. The extension supplies a sharper retained-state bound, not
an efficient preprocessing algorithm, a result uniform over growing
datasets, or a new population training theorem.
