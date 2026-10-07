# Independent check of the explicit setup orders

2026-10-06. Scoped audit of the frozen deterministic order prescription.

**Verdict: PASS for the stated conditional deterministic interface.**
No algebraic, rounding, dimensional, label
scope, or source-jet tolerance blocker was found. This verdict does not promote
the result, independently reprove the inherited stochastic source theorem, or
make its confidence-to-width threshold effective.

## Frozen inputs and scope

The reviewed candidate is IMPLICIT_SETUP_ORDERS.md, SHA-256
3f5ff8a63c97ea76dda4890b0f464f05e8bb8576760cde93ff1f4c18d00a6009.
It was read completely. Its recorded source hashes agree with the files read:

| Input | SHA-256 |
| --- | --- |
| RESULT.md | c2cbd1bb0e6a39de87181df89be977eaf2e272fda4f1459ac934396d84e1b278 |
| POLYNOMIAL_SETUP_ODE_ROUTE.md | 46e9c2b4ed9f118b3812ce8208d26ebbfa9c9f1fb3efc6e68f3854e0be8cf5a6 |
| POLYNOMIAL_SETUP_QUADRATURE_ROUTE.md | 2d58da5a418f6d5a8f1bb54ce343b205978770424c0940789b15231e251daf42 |
| LOCAL_CONTINUATION_SETUP.md | c4c12b38e49e37ac5096e69ceabee1d41be6ad6bc4a1c57ece943959ef425bbe |
| LOCAL_ACTIVATION_BACKEND.md | cbf26326c081fc19da31f5d38781eff2dfa2a5b97dee12eb1a8022770a2843e4 |
| LOCAL_TAYLOR_ASSEMBLY_BRIDGE.md | dedba0b570d6a73b5c9eabbd414953d01fdc6d46056de023748eede621c64f2b |
| docs/notation.qmd | 78e11eb3dafc5321a8a3923742993c0bad78df53b0e80b6319f16e48f0131023 |

The initial audit examined candidate
eebf061e1754863173048ce95a3b0d101744a94b57d379210deac5e69058c4c6.
A complete-text comparison verified that the final version changes only the
activation-hypothesis sentence to retain the original full-strip derivative
bound explicitly. No displayed formula or order changed, and the earlier
minor clarification is resolved.

The five component notes were read completely. The relevant complete sections
of RESULT.md were read for shared model/activation conventions, common
labels and confidence, dense fitting coefficients, Legendre and Harmonic
label coefficients, source recurrences S.5–S.10 and S.22–S.31, the activation
power ledger, exact source counts and source-expansion proof, width gates, and
all-horizon extension/counting proofs. The stochastic source event remains an
imported hypothesis; the finite-deletion proof was not independently audited.
No other review reports, other studies, archived book, or historical sources
were consulted. The reviewer independently authored the Gaussian sampler
component, which is not an input or premise of this order check.

The accessible rigorous-math skill, adversarial-audit reference, supplied
canonical presentation rules, and maintained notation contract were applied.
The prescribed canonical-notation skill remained permission-denied. There
were no numerical, statistical, or training experiments and no Git mutations.

## 1. Original model and full label allowance

The recipe uses the original width $n$, sample count $m$, input dimension
$d$, hidden depth $L\ge2$, normalized gap $\lambda=\gamma/m$, label RMS
$Y=\|y\|_2/\sqrt m$, and activity $S=16Y/\lambda$. Its positive-label
branch has the required $T\ge32\lambda^{-1}\log(en)$ and
$0<\eta\le\min(1,Y,S)$. Its separate $Y=0$ branch avoids all divisions
by $Y$.

The four entries in its common label minimum match RESULT.md:

1. $1/(8H_D\sqrt{F_D})$, with the actual scalar Gaussian moment recursion
   for $H_D$ and the correct unrolled formula for $F_D$.
2. $S_*^{\rm Leg}/8$, with all four entries of the Legendre minimum,
   including the outer square root in $(8\sqrt{C_L^{\rm Leg}})^{-1/2}$
   and exponent $2/7$ in the last entry.
3. $1/(16H_c\sqrt{F_c})$, with the original Harmonic recurrences and
   $F_c=(d_1^c)^2+4H_c^2\sum_{j=2}^L(d_j^c)^2$.
4. $S_*^{\rm src}/16$, with the complete source budget minimum.

Omitting the Legendre entry for the Harmonic-only result is exactly the
original distinction. The new order choices introduce no further small-label
condition. The narrower $\lambda\beta^{-30L}$ cap is explicitly optional.
The warning that replacing activation coefficients by looser bounds can
shrink the certified interval is mathematically necessary and correctly
included.

## 2. Source coefficients, gates, and confidence

Every source recurrence displayed in candidate Section 2 matches its cited
formula. In particular:

- The source budget tolerance $\eta_{\rm bud}$ is kept distinct from the
  requested approximation tolerance $\eta$.
- The coefficients $U,V_{\rm qry}$ retain the actual activity $S$ in the
  terms $ST_Q$ and $S^2H_{j-1}^{\rm src}q_{j-1}^{\rm src}$.
- $c_t=a/(64YSU)$ and $c_q=\min\{1/8,a/(8V_{\rm qry})\}$ have the
  original factors, and $r_t,r_q$ divide by $\sqrt{\log(en)}$.
- The late extension uses its own radius $b_{\rm ext}$ and carrier
  recurrence, separate from the later numerical tube radius $b_n$.

The explicit fitting threshold $N_{\rm fit}(\delta/32)$ and deterministic
radius, counting, and analytic-extension gates match RESULT.md. Both
dimension-specific counting branches are included. No dependence on $T$ or
$\eta$ has been added to the stochastic event. Allocating source failure
$\delta/32$ is conservative; independence is unnecessary for the union bound.
The lower/CLT events are not needed for this setup interface.

The recipe explicitly retains the existential source threshold. It therefore
does not claim a numerical width bound or confidence-to-work theorem. At a
fixed admissible width, the deterministic orders do not need another
confidence parameter. This is the correct logical boundary.

## 3. Source counts and positive quadrature

For $d\ge2$, the floor formulas enumerate exactly
$\alpha_T k+r_q\ell\le H(T,\eta)$, with every harmonic multiplicity
$h_\ell$. In particular $p_\ell+1$ includes its zero temporal mode,
$N$ counts the weighted simplex rather than a rectangular enlargement, and
$R=2m+d+1+4N$ is the original source dimension certificate.

The original gates and $T\ge T_0$ ensure $0<\alpha_T\le1$;
also $0<r_q\le1/8$. Since $\eta\le1$ and $M_n\ge10$, the displayed
logarithmic thresholds are positive. Thus the retained mode set is nonempty
and all floors, maxima, and denominators used in the recipe are valid.

The positive quadrature orders reproduce the route note's equations
(6), (11), (16), (22)–(24). Writing $a_t=\alpha_T/2$, each of the $d$
univariate error contributions is at most $\epsilon_c/(2d)$, giving total
exact-value quadrature error at most $\epsilon_c/2$. The selected nodal
tolerance satisfies

$$
2A_d\mathcal Y\,\delta_{\rm node}
=2A_d\mathcal Y\frac{\eta}{64NA_d\mathcal Y^2}
=\frac{\epsilon_c}{2}.
$$

The omitted-mode tail is $\eta/16$ and retained coefficient reconstruction
adds at most $N\mathcal Y\epsilon_c=\eta/16$. No equality between
quadrature node counts and mode counts is presumed.

For $d=1$, the two points are handled separately:

$$
N=2N_1,\qquad p=N_1-1,\qquad H_{\rm sph}=N_x=2,\qquad
R=2m+d+1+8N_1.
$$

The per-point coefficient tolerance is $\eta/(16N_1)$, not a tolerance
with $2N_1$ inserted accidentally. Its nodal tolerance is one quarter of
that quantity. The cosine normalization costs at most two, so the nodal
coefficient error is again at most half the coefficient allowance. There is
no spurious spherical degree or polar quadrature in this branch.

The sufficient selected budget $\min(n,9R)$ and the explicit full-width
fallback are valid. Actual rank may be smaller, but the candidate does not
rely on preserving accidental rank deficiencies under approximation.

## 4. Continuation, activation degree, and the stronger source interface

The real stability constants, complex continuation recurrences, carrier
extension $M_c$, tube radius $b_n$, and polynomial-backend radius
$\widehat R_n=\min\{r_t/2,(8L_n)^{-1}\}$ agree with the frozen
component formulas. The numerical radius uses the corrected $a/16$ tube
margin. It does not accidentally revert to the earlier radius of the
original-activation backend.

The order prescription correctly substitutes

$$
\delta_*=\frac{\delta_{\rm node}}{32\sqrt n}
$$

throughout the activation backend's nodal-error budgets, including $e_d$
and $\epsilon$. The layerwise activation error recurrences, $C_F^{\rm act}$,
$M_q$, $C_p$, scalar tolerance, ellipse parameters, polynomial degree $D$,
and $N_\phi=4(D+1)$ match the backend. All denominators are positive.
Inexact activation-value accuracy is exposed separately. Exact initialized
features remain original-activation evaluations.

The degree $K$ includes all three backend cutoffs and both additional
bridge cutoffs. To check the latter directly, let $v$ be the exact local
polynomial-field solution, $p$ its parameter Taylor polynomial, and $g_K$
the degree-$K$ source Taylor polynomial. The extra cutoffs guarantee

$$
\sqrt n C_g2^{-K}\le\frac{\delta_{\rm node}}{64},
$$

and

$$
\sqrt n\,C_{\rm src}n\,
       (2V_{\rm loc}\widehat R_n2^{-K})
\le\frac{\delta_{\rm node}}{64}.
$$

The second formula uses $n^{3/2}$, so the coordinate-to-Euclidean
conversion has not been lost. The backend activation replacement and
global-parameter error each contribute at most
$\sqrt n\,\delta_*/2=\delta_{\rm node}/64$. The bridge's four-term
decomposition consequently yields base-source Euclidean error at most
$\delta_{\rm node}/16$. Multiplication by an initialized matrix of
operator norm at most eight still gives coordinate error at most
$\delta_{\rm node}/2$, within the quadrature allowance.

Increasing $K$ preserves the previous tail and defect inequalities. Also

$$
J=\left\lceil\frac{2T}{\widehat R_n}\right\rceil
 =\left\lceil\max\{4T/r_t,16TL_n\}\right\rceil
$$

is the correct panel count and gives panel length at most
$\widehat R_n/2$. There is no dependence on an uncomputed trained-path norm
in these choices.

## 5. Activation-envelope dependence

The source power estimates quoted before the optional small-label
specialization do not use that specialization: they bound activation-only
recurrences. The factors $S$ first enter the stronger small-label estimates
for $U,V_{\rm qry}$.

There is also a short independent check of the candidate's conservative
full-interval envelopes. The full label interval gives $S\le1$. The
already proved full-range argument in RESULT.md, in its budget-count
proof, gives

$$
U\le\beta^{37L}\sqrt{d+3},\qquad
V_{\rm qry}\le\beta^{31L}\sqrt{d+3}.
$$

The candidate's $\beta^{40L}$ and $\beta^{36L}$ bounds are weaker and
therefore valid for $\beta\ge10$. Independently of those larger powers,
the radius formulas and $a^{-1}\le\beta/16$ give exactly

$$
c_t^{-1}\le4YS\beta^{40L+1}\sqrt{d+3},\qquad
c_q^{-1}\le
\max\{8,\tfrac12\beta^{36L+1}\sqrt{d+3}\}.
$$

The sharper exponents $26L$ and $2L$ are used only under the additional
smaller cap. The candidate does not claim that $\beta$ determines the actual
Gaussian moments, the data gap, scalar activation evaluation complexity, or
the stochastic source threshold. Nor does it infer a joint polynomial bound
in dimension, depth, and all inverse parameters from formulas that include
factorials, tensor products, and exponential stability factors.

## 6. Hypothesis alignment and remaining qualifications

The final candidate's Section 1 explicitly retains the original assumption
of a bounded first derivative on the full open strip. Its subsequent use of
half-strip first and second derivative bounds is therefore consistent with
the original activation class and imported source theorem. No label
restriction or numerical order was changed to make this clarification.

The following qualifications remain material and are already disclosed:
the stochastic confidence threshold is existential; exact activation moments
and valid coefficient bounds must be supplied or certified; scalar evaluation
cost needs its own input model; the computations use exact-real arithmetic;
and the full-width fallback is not a compression claim. Within these
boundaries, there is no unresolved blocker to using the stated deterministic
orders.
