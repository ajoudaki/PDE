# Independent audit of the finite matrix-oracle integrator

2026-10-11. This is a fresh isolated mathematical review of Section 6 of
`GELU_SILU_FLOW_ROUTE.md`. The complete four inputs listed below were read.
No study README, other study note, prior review, repository history,
experiment, or external research source was consulted. The
`solve-math-rigorously` and `explain-with-canonical-notation` skills, including
the latter's neural-network reference, were applied. Only this report was
written.

**Verdict: PASS for the Section 6 oracle approximation theorem, conditional
on the cited fitting and analytic-source results as permitted by the review
assignment.** Their proved interface does supply the stronger complex
carrier bound and uniform activation-strip margin required here. The
argument establishes physical parameter error
$O_{\mathrm{data}}(n^{-16})$ at the actual fitted endpoint, with
$O_{\mathrm{data}}(mL[\log(en)]^{9/2})$ total hidden-matrix actions, under
the original label cap. I found no blocking mathematical error in this
module. Two interpretation clarifications are recorded below. This verdict
does not establish the separate fitted-endpoint fluctuation lower theorem,
nor constitute a new independent proof of the entire source proposition.

## Frozen inputs

SHA-256 hashes were checked before and after the review and agreed.

| Input | SHA-256 |
| --- | --- |
| `paper/compact.tex` | `460f29eda118ffe5bbc24be3a04d1a25c5e4a9bddb0744f8235d97a3674cabfe` |
| `paper/compact_fitting.tex` | `6efe077759c846c4b3d79f999c37d2d1478bae549d49fc9666837efbf9f1a01f` |
| `paper/compact_foundations.tex` | `6a49f8e35bb637416b7e330f7ace06286e482c942302bf57a46c8253a4cffbf0` |
| `studies/general_nonlinear_endpoint_lower_20261010/GELU_SILU_FLOW_ROUTE.md` | `76cc89d3fbc592d51cc426e76c50be1099b54faf90ef96520884bf9d4356962a` |

The review preserves the source notation

\[
\theta=(W^{(1)}/\sqrt n,W^{(2)},\ldots,W^{(L)},w/\sqrt n),
\qquad \lambda=\gamma/m,\qquad \ell_n=\log(en).
\]

The norm of this tuple is the physical parameter norm. All constants in
this report may depend on the fixed training problem, including positive
(Y\), but not on width. No uniform growing-data, small-(Y), precision,
or arithmetic-runtime assertion is inferred.

## 1. The source interface is sufficient

The public proposition alone would not give the needed complex carrier
maximum: its all-time carrier assertion is real-time, and its complex
coordinate envelope is of order (\sqrt n\). Section 6 correctly invokes
additional estimates actually proved in the supplied source:

- The working whole-sphere estimates in `compact_foundations.tex:278`
  assert the complex training bound
  (\max_{a,j,i}|k_{a,i}^{(j)}|\le SK_{\rm src}\sqrt{\ell_n}\), with
  (S=16Y/\lambda\). The explicit improvement is
  `cp:src-improved-maxima` at line 1020. Its domain is the stopped complex
  domain subsequently continued and freed of stops, not only its real
  slice.
- The domain verification at line 1187 bounds complex-time
  preactivation displacement by (a/8\). The additional (a/8\) query
  displacement also leaves a fixed margin inside the half strip.
  Restricting to real training inputs therefore retains a quantitative
  margin; this is stronger than merely pointwise strict inclusion.
- The working radius dominates the public (R_n\) used in (25), as
  proved in the source's final reduction. Its operator and RMS bounds
  have constants independent of width.
- Lines 1208 onward explicitly justify local holomorphic ODE continuation
  and gluing across the compact complex domain. Thus parameter
  holomorphy, also obtained by integrating the canonical flow, is
  available along with field holomorphy.

These conclusions all use the unchanged cap
(Y/\lambda\le\beta^{-30L}\). The source's private smallness allowance
is explicitly implied by that cap. No extra cap is introduced when the
integrator chooses its tube radius or numerical width threshold.

For independence from the orthogonal query, let (V\) be the training
span and let (U\) have orthonormal columns spanning (V\). Training uses
only (A=W^{(1)}U\), and (A_0\) has independent standard Gaussian
entries. The source theorem can be applied to the inputs (U^\top v_a\)
in dimension (\dim V\). The Gram recursion, labels, flow normalization,
and parameter norm on moving coordinates are unchanged. This gives a
successful event measurable in (A_0\) and the hidden initialization.
The radius in the original dimension (d\) is no larger. Moreover,
(A_0\) is obtainable from the declared products (W_0^{(1)}v_a\) by
fixed linear algebra, because the (v_a\) span (V\).

## 2. The complex parameter tube and Jacobian bound

For a physical parameter perturbation of norm (\eta\), forward
subtraction on the training inputs gives

\[
\|\Delta z_a^{(j)}\|_2\le C\sqrt n\eta,
\qquad
\|\Delta h_a^{(j)}\|_2/\sqrt n\le C\eta.
\]

At the first layer this follows from
(\|\Delta W^{(1)}\|_F\le\sqrt n\eta\); at later layers one uses
(\|\Delta W^{(j)}\|_{\rm op}\le\eta\), feature RMS bounds, and the
bounded activation derivative. A first-exit argument makes these estimates
valid before assuming the segment lies in the derivative strip. Choosing
(\eta_n=c_0/\sqrt n\) with fixed sufficiently small (c_0>0\)
preserves a uniform strip margin throughout each joining segment.

Backward subtraction uses

\[
\Delta\delta
=\phi'(z+\Delta z)\odot\Delta k
 +k\odot[\phi'(z+\Delta z)-\phi'(z)].
\]

The reference carrier maximum is (O(\sqrt{\ell_n})\), so induction
gives (\|\Delta k\|_2+\|\Delta\delta\|_2
\le C\sqrt{n\ell_n}\eta\). At (\eta\le\eta_n\), the new
coordinate maxima are still (O(\sqrt{\ell_n})\), and the added RMS
is (O(\sqrt{\ell_n/n})\), hence bounded. Residuals and gradients
therefore stay bounded in the tube.

The mobility conversion is exact. With
(\Theta=\sqrt n\theta\) and (F_a=nf_a\),

\[
D_\theta^2f_a=D_\Theta^2F_a.
\]

In `cp:src-Hessian`, the forward derivative operators have bounded norm;
each curvature term contains one carrier diagonal, and the mixed hidden
terms contain (\delta/\sqrt n\). Consequently

\[
\|D_\theta^2 f_a\|_{\rm op}\le C\sqrt{\ell_n},\qquad
\|G\|\le C,\qquad \|DG\|_{\rm op}\le C\sqrt{\ell_n}.
\]

Here (G=-(2/m)\sum_a r_a\nabla_\theta f_a\) is indeed the canonical
flow in physical coordinates. Algebraic transposes are appropriate for
the holomorphic extension; complex Euclidean norms still bound all terms.
There is no missing width factor in this calculation.

## 3. Numerical starts, accumulated error, and the fitted tail

Every disk (t_j+\{|z|\le R_n/2\}\) lies in the true source domain.
Suppose the numerical starting error is
(\delta_j<\eta_n/(2C_1)\), where
(C_1=\exp(CR_n\sqrt{\ell_n}/2)\) is bounded independently of (n\).
Gronwall along each radial complex segment bounds the discrepancy by
(C_1\delta_j\). This prevents exit from the parameter tube. Local
holomorphic existence and uniqueness then continue the numerical-start
solution throughout the disk. Equivalently, solve
(\partial_s X=zG(X)\) on (0\le s\le1\); the same bound permits
holomorphic dependence on the complex parameter (z\) and glues the
local solutions. This justifies the disk at the numerical state itself.

The bounded velocity gives a dimension-independent bound
(CR_n\) on the solution's increment. Applying Cauchy to this increment,
rather than to the possibly large initialization norm, gives the local
Taylor error (CR_n4^{-q_n}\), because (h_n\le R_n/8\). Thus

\[
\max_{j\le J_n}\delta_j
\le C J_nR_n e^{C\sqrt{\ell_n}T_n}4^{-q_n}
\le C\ell_n\exp\{C\ell_n^{3/2}-(\log4)\ell_n^3\}.
\]

For each fixed (K>0\), this is eventually at most (n^{-K}\).
The same bound is eventually below the tube threshold, so induction
closes the assumption at every numerical start. The large fixed constants
in (R_n\), (C_1\), and the stability factor affect only the eventual
width threshold.

The fitted-tail bound comes directly from `cp:eq-dense-tail`:

\[
\|\theta(\infty)-\theta(T_n)\|_{\rm par}
\le2Y\lambda^{-1/2}e^{-\lambda T_n/2}
=2Y\lambda^{-1/2}e^{-16\ell_n}.
\]

Taking (K=17\) for the numerical error proves (24) at the actual
parameter limit. This part does not merely approximate a fixed finite
training horizon or a frozen-feature model.

## 4. Oracle calls, increment spans, and measurability

At a step, write each hidden matrix as its oracle initialization plus a
known increment. Once state coefficients through degree (k\) are known,
forward propagation at degree (k\) requires exactly one new action
(W_0^{(j)}h_{a,k}^{(j-1)}\) per sample and hidden layer. Descending
backward propagation requires exactly one new action
(W_0^{(j)\top}\delta_{a,k}^{(j)}\). Lower-degree actions are cached.
All convolutions with learned increments are algebra on known vectors
and scalars. The degree-(k\) vector-field coefficient determines the
degree-(k+1\) state coefficient, so the recursion is well founded.

Each hidden update coefficient is a sum of

\[
-\frac2{nm}r_{a,p}\delta_{a,q}^{(j)}
                h_{a,s}^{(j-1)\top},\qquad p+q+s=k.
\]

Its column and row factors belong to the transpose-input and
forward-input spans already queried, respectively. This remains true
after summing coefficients into the numerical update and accumulating
steps. The scalar convolution count may be larger than the query count,
but creates no new oracle directions. There is no matrix-entry access,
matrix-matrix oracle action, or access to a true later state.

At most (2m(L-1)J_nq_n\) hidden actions are needed, with harmless
endpoint indexing conventions. Since
(J_n=O_{\mathrm{data}}(\ell_n^{3/2})\) and
(q_n=O(\ell_n^3)\), the stated total bound follows. It also bounds
each queried span dimension. First-layer derivatives are explicit sums
with right factors (v_a^\top\), so require no further first-layer
initialization access. Every direction is a deterministic function of
earlier answers, fixed data, and scalar activation derivatives. The
algorithm does not test the good event, and no claim of independence of
adaptive directions from earlier answers is needed.

## 5. Query and fourth-moment transfers

If (v\perp V\), both actual and approximate first-layer updates
annihilate (v\). Thus their common first preactivation is
(Z=W_0^{(1)}v\), independently standard Gaussian under the active
conditioning. Real forward subtraction requires only bounded hidden
operators and linear activation growth, and gives

\[
|\widehat f_n(\sqrt d\,v)-f_n(\infty,\sqrt d\,v)|
\le C(1+\|Z\|_2/\sqrt n)
       \|\widehat\theta_n-\theta(\infty)\|_{\rm par}.
\]

The multiplier has uniformly bounded Gaussian moments of every fixed
order, so this gives conditional (L^p\) error (O(n^{-16})\) for
every fixed finite (p\), in particular the required scale
(o(n^{-1/2})\). This evaluation need not be included in the training
oracle transcript; a subsequent lower-bound argument must specify any
extra evaluation queries it uses.

For the normalized coordinate norms,

\[
\|\widehat w-w_\infty\|_{4,n}
\le n^{1/4}\|\widehat w-w_\infty\|_{2,n}
\le Cn^{-63/4}.
\]

The exponent and normalization in (38) are correct. An actual-readout
fourth-norm estimate therefore transfers by the triangle inequality.
This implication supplies no new passive mixed-time fourth-moment bound
and the module does not claim one.

## Nonblocking clarifications and boundary of the verdict

1. **The returned parameters use an implicit initialized base.** The
   accessible information does not contain the entries of the hidden
   matrices or the orthogonal first-layer block. Thus
   (\widehat\theta_n\) means the original initialized matrices plus
   the explicitly returned increments and readout. It is not a full
   entrywise reconstruction of initialization. This interpretation is
   already indicated by the oracle-and-increment model and is sufficient
   for every estimate and span claim; making it explicit would remove a
   possible ambiguity in “returning” the parameters.
2. **The measurable first-layer operator bound is restricted to the
   training span.** After applying the source argument to (V\), the
   bound is on (W^{(1)}U/\sqrt n\), not on unobserved orthogonal
   columns. The prose following (25) should be read accordingly. No
   argument here needs the full first-layer operator bound: training
   depends only on that restriction, inactive columns have zero error,
   and the query transfer uses the explicit (Z\).

Neither clarification requires a stronger assumption or changes the
algorithm or its rate. The separate deferred-Gaussian and endpoint lower
arguments remain separate proof obligations. No verdict on those
obligations is made here.

## Check of the two author clarifications

After the initial report, the author amended only the two interpretation
points identified above. The current `GELU_SILU_FLOW_ROUTE.md` hash is
`f3b33474289c38cc38bfbb9eeb90d5aed7652b7a025f4c3171f11e5140908c1c`.
I checked the amended text and reversed exactly the added
initialized-base representation paragraph and the replacement
first-layer-operator bullet in memory. The resulting SHA-256 is the
original frozen hash
`76cc89d3fbc592d51cc426e76c50be1099b54faf90ef96520884bf9d4356962a`.
This verifies that no other input text changed. The three paper hashes
remain unchanged. The clarifications resolve both presentation points,
and the conditional PASS verdict is unchanged.
