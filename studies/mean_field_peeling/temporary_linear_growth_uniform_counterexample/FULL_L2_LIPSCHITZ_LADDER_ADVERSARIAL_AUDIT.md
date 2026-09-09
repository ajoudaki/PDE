# Adversarial audit of `FULL_L2_LIPSCHITZ_LADDER.md`

## Verdict

**Theorem 1.1 is not proved by the current draft.**  The universal
finite-dimensional tensor (3.2), the single-occurrence ridge symbol
(4.3), and the algebra of the diagonal argument are sound (with the minor
regularity correction recorded below).  The decisive full-`L=2` statements
(5.5), (5.10), and (5.11), however, do not follow from the supplied
arguments.  In particular, the draft does not prove either

1. that the displayed lower-node term is the complete same-source
   `w^{-3}` sector of the width-first reused-matrix coefficient; or
2. that every remaining OMFP response diagram satisfies the asserted
   activation-envelope estimate.

Consequently the file currently establishes a **conditional diagonal
construction**: if (5.5), (5.10), and (5.11) are supplied by an exact
width-first diagram theorem, then Section 6 gives the claimed nonlocal
counterexample.  Those three estimates are precisely the missing theorem,
not consequences of the present excess-count paragraph.

## 1. Universal paired tensor: pass, with one correction

For `g=grad f`, the second Euler iterate has

\[
 \theta_2-\theta
 =2hg+h^2Hg+\frac{h^3}{2}T[g,g]
  +\frac{h^4}{6}U[g,g,g]+\frac{h^5}{24}V[g,g,g,g]+o(h^5).
\]

Substitution in the fifth Taylor coefficient of `f` gives

\[
\begin{aligned}
 [h^5]\{f(E_h^2\theta)-f(E_{2h}\theta)\}
={}&\frac1{24}V[g^5]
 +\frac53U[Hg,g,g,g]+T[T[g,g],g,g]\\
 &+\frac12T[H^2g,g,g]+T[Hg,Hg,g],
\end{aligned}
\]

so (3.2) is correct.  For example, the two `U` contributions are
`1/3+4/3=5/3`, and the coarse `V` contribution cancels the `4/15` terminal
Taylor contribution, leaving `1/24`.

The stated hypothesis `f in C^5` does **not** justify the `O(h^6)` remainder
in (3.1).  It justifies `o(h^5)`, which is sufficient for coefficient
extraction.  The finite truncations are smooth, so this is not fatal to the
intended application.  With a nonidentity constant metric, all raised
indices and contractions must be defined after whitening; the choices in
(4.1) are consistent with that convention.

## 2. Single-occurrence ridge symbol: pass only at that scope

Freeze one activation occurrence, put `q=Phi'`, and retain only the highest
chain-rule symbol

\[
 D^k f=r\Phi^{(k)}\ell^{\otimes k}+\text{lower-excess terms}.
\]

Writing `q=b+delta R`, the quadratic terms of singular excess four in
(3.2) are exactly

\[
 r^2sv^4\frac{\delta^2}{w^4}
 \left(\frac5{24}R\rho'''+\frac53\rho\rho''+(\rho')^2\right).
\]

Since

\[
 \int R\rho'''=\int(\rho')^2,
 \qquad \int\rho\rho''=-\int(\rho')^2,
\]

their integral is

\[
 -\frac{11}{24}r^2sv^4\frac{\delta^2}{w^3}
 \int(\rho')^2.
\]

Thus (4.3) and its sign are correct for a **single fixed activation
occurrence**.  A derivative falling on the outer map, on `r`, or on a
nonlinear preactivation partitions a chain-rule block and lowers its
singular excess by at least one.  This observation does not, by itself,
classify source coincidences among different occurrences in the
width-first reused-matrix DAG.

## 3. Completeness of the full `w^{-3}` sector: fail

The sentence after Lemma 4.1 assumes that two distinct transition nodes
produce two independent integrations.  No theorem in the file proves this.
For the actual network, top and lower queries are connected through reused
`W` and `W^T`; after width limiting, response terms are represented by
singular Gaussian source identifications.  What is needed is not a count of
formal activation occurrences but a count of **distinct Gaussian source
classes after every equality/response contraction**.

Equation (5.6) is asserted rather than derived.  In particular, the draft
does not provide:

- the exact normal form of all five contractions in (3.2) after the two
  layer forward/adjoint peeling;
- the coefficient and source-history attached to each atom;
- a proof that every two-factor, excess-four atom supported on one Gaussian
  source comes from one physical activation occurrence and is already
  included in (4.5);
- a proof that all other two-factor, excess-four terms have a uniformly
  nondegenerate two-source law and hence really gain a second factor `w`;
- treatment of Gaussian polynomial weights and aggregate response
  coefficients produced by the reused adjoint.

The generic statement that Faa di Bruno does not increase the total excess
is correct but insufficient: it controls derivative order, not source rank,
coarea Jacobians, response coefficients, or cancellations among diagrams.
Therefore the claimed completeness of the negative sector is open in this
draft.

### Required repair

Construct the complete marked normal form for this particular
`F_2(h)-F_1(2h)` coefficient.  Each term must carry (i) its numerical
coefficient, (ii) its layer and source-equivalence labels, (iii) its
Gaussian polynomial weight, and (iv) every reused-adjoint response factor.
Then prove a source-rank lemma: rank one plus excess four and quadratic
transition amplitude is exactly the local symbol (4.5); every other term
has either excess at most three, amplitude at least three, or Gaussian
source rank at least two with a uniformly controlled density.  Without
this ledger, (5.5) has not been established.

## 4. Lower-node coefficient: exact algebra passes; limit theorem missing

The finite-width identities

\[
 r_j=b_j/n,\qquad s_j=n,\qquad v_j=b_jb,
\]

and hence

\[
 \sum_jr_j^2s_jv_j^4=\frac{b^4}{n}\sum_jb_j^6
\]

are correct for the metric `G=nI`.

The conclusion (5.4) is plausible but is not proved by the phrase
“initialization cavity law.”  A direct proof would condition on `(W,u)`:
because the readout variables are independent Gaussians,

\[
 b_j\mid(W,u)\sim N(0,V_{j,n}),\qquad
 V_{j,n}=\frac1n\sum_iW_{ij}^2\psi'(z_i)^2.
\]

One must prove, under the marked conditioning `u_j=X`, that
`V_{j,n}->d=E psi'(G)^2` in `L^6`; the bounded-slope estimate then gives
uniform twelfth moments and hence convergence of sixth moments to `15d^3`.
The conditional expression in (5.4), where `j` is simultaneously a dummy
index and the conditioned mark, should be replaced by a precise marked
test-function limit.

Even after this repair, a second bridge is required: the draft starts from
the finite-dimensional tensor (3.2), takes an initialization cavity limit,
and calls the result the fifth coefficient of the already width-limited
output.  This is exactly a derivative/width-limit interchange unless the
marked temporal/static intertwining theorem is invoked term by term and
its hypotheses are verified for the narrowing transition.  No such
invocation or verification appears between (5.2) and (5.5).

### Required repair

Prove the marked `L^1` convergence of every contraction in (3.2) to the
corresponding width-first DAG coefficient, including reused transpose
responses, at each fixed `(delta,w,X)`.  Only after that identification may
the finite-width local symbol be used inside `beta`.

## 5. Remainder estimate (5.10): fail

The bound (5.8) is a valid scalar estimate for a specified Gaussian atom
with a fixed smooth coefficient.  It does not prove (5.10) for the actual
coefficient because the exact list and coefficients of those atoms have
not been supplied.  The four-case discussion leaves the following
unproved:

1. response coefficients and conditional Gaussian densities are bounded
   independently of `(delta,w,X)` after the new transition is inserted;
2. distinct-node source covariances stay nondegenerate, or singular cases
   have been reassigned to the local symbol;
3. the coefficient multiplying a lone fifth derivative has three uniformly
   bounded spatial derivatives after all scale-`w` factors `R` are split
   off;
4. higher powers of `R`, tail-slope changes, products of atoms, and Gaussian
   polynomial weights obey one common polynomial `P(X)`;
5. the constant hidden in `C P(X)` is uniform over the complete reused-
   matrix diagram family.

The identities for `int rho'''`, `int y rho'''`, and
`int y^2 rho'''` correctly remove a lone fifth derivative against a fixed
`C^3` coefficient.  They do not establish that the full coefficient is of
that form.  Likewise, “there are finitely many diagrams” proves termination
only after the diagrams and their source ranks have actually been
constructed.

### Required repair

After the normal-form ledger required in Section 3 of this audit, state an
atomwise majorant with all coefficient norms explicit.  Prove it separately
for source ranks one and at least two, sum the finite ledger, and only then
deduce (5.10).  The proof must be performed after width-first
identification, not by an unproved finite-width Taylor interchange.

## 6. Cubic control (5.11): fail for the same reason

The scalar cubic principal combination

\[
 \frac12\Phi'''(\Phi')^3+2(\Phi'')^2(\Phi')^2
\]

has quadratic size `delta^2 gamma(X)/w`.  This verifies the stated scale
for one scalar occurrence.  The draft gives no complete cubic marked
normal form for the two-layer reused-matrix coefficient, no source-rank
classification, and no aggregate-response estimate.  Saying that the
same excess count applies does not prove (5.11).

### Required repair

Give the full cubic analogue of the fifth-order ledger and show atom by
atom that every omitted term is bounded by the right side of (5.11).

## 7. `d_1` continuity: essentially sound but not yet fully quantified

For a fixed smooth reference activation, fixed finite schedule, and compact
step interval, the normalized-state/operator-norm induction in Lemma 2.1 is
valid.  One minor correction in (2.9) is that the direct `d_1` term first
contains `1+||x||_n`, not `1+||y||_n`; use
`||x||_n<=||x-y||_n+||y||_n` and absorb the extra difference term.
Bounded `psi''` is needed only for the reference activation, as stated.

To justify (6.6a) numerically, the draft must also record a constant `K`
such that

\[
 d_1(\psi_N,\phi)\le K\sum_{q>N}\delta_q,
\]

including the change of RMS normalization, and incorporate `K` and the
continuity constants `C_{N,m}` into `r_N`.  This is a routine finite-
schedule repair and is not the central obstruction.

## 8. RMS normalization: current claim is false as written

The sentence that normalization “only multiplies” the negative principal
coefficient is not correct.  Replacing `Phi` by
`Phi/||Phi(G)||_2` rescales every old activation value and every old
derivative.  Since (3.2) is a sum of contractions with different chain-rule
structures, this also creates an **additive change of the whole background
coefficient**; it is not one common multiplicative factor.

The effect is likely controllable for a fixed finite background because the
normalizing-factor change caused by a remote slope step has a Gaussian-tail
bound.  But that estimate is absent, and at stage `N` it must be allowed to
depend on all earlier narrow transitions.

### Required repair

Prove explicit bounds for the normalizer and its increment, for example

\[
 |c_{\delta,w,X}-c_0|
 \le C_{\rm bg}\,\delta P(X)\,\gamma([X-1,\infty)),
 \qquad c=\|\Phi(G)\|_2^{-1},
\]

then propagate this global rescaling through the exact cubic and fifth
normal forms.  Show that the resulting additive fifth change is
`o(delta^2 gamma(X)w^{-3})` and the cubic change is `o(1)` under (5.9).

## 9. Diagonal argument: conditional pass

Assume (5.12), the quantified normalization bounds, and the `d_1`
continuity estimate.  Then Section 6 works:

- `beta(psi_N)<=-N` and the local fifth expansion permit a choice of `h_N`
  satisfying (6.4)--(6.5);
- the later cubic budgets give
  `|kappa_infinity-kappa(psi_N)|/h_N^2<=1/2`;
- the later output budgets contribute a bounded amount to the quotient;
- `|beta(psi_N)|h_N^2<=1/N` proves the scaled quotient tends to zero when
  comparing any `kappa != kappa_infinity`;
- `h_N<1/N` puts infinitely many witnesses in every interval `(0,r]`.

The simultaneous countable amplitude ceilings are compatible because each
new principal coefficient becomes more negative as `delta_N` decreases.
This part is not a substitute for (5.12), but it does not introduce a new
fatal obstruction.

## 10. Final activation and fixed-step outputs: conditional pass

The supports of `g'` are disjoint and the centers tend to infinity, so the
sum is locally finite.  Also `1<=g<2`; after normalization the final
activation is smooth, has two-sided positive bounded slope, and has at most
linear growth.  Every finite-width fixed-step output has finite moments.

Once the normalization-aware `d_1` estimate is supplied, uniform-in-width
approximation by `psi_N` gives existence and finiteness of the width-first
expected one- and two-step outputs by a correct three-epsilon argument.
Thus output existence is not the main gap; the unproved coefficient
estimates are.

## Claim-level status

| Claim | Verdict |
|---|---|
| Paired tensor (3.2) | proved, after replacing `O(h^6)` under `C^5` by `o(h^5)` |
| Single-node coefficient and sign (4.3) | proved at single-occurrence scope |
| Completeness of the full reused-matrix `w^{-3}` sector | open |
| Exact lower-node algebra (5.1)--(5.2) | proved |
| Conditional cavity/UI limit (5.3)--(5.4) | plausible but not proved |
| Width-first identification leading to (5.5) | open in this draft |
| Explicit fifth remainder (5.10) | open |
| Explicit cubic control (5.11) | open |
| Fixed-schedule `d_1` continuity | essentially proved; constants/normalization need quantification |
| RMS-normalized preservation of (5.5)--(5.12) | open; stated reasoning is incorrect |
| Diagonal implication from (5.12) | proved conditionally |
| Smooth bounded-slope final activation | proved |
| Existence of final fixed-step width-first outputs | proved conditionally on quantified `d_1` tail estimate and established limits for truncations |
| Theorem 1.1 | **not proved** |

