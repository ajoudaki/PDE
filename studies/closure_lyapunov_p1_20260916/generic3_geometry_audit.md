# Internal audit of the generic three-input geometry route

Date: 2026-09-16. Scope: fresh internal mathematical audit, not promotion.

**Verdict: PASS for the stated fixed-order population result.** The candidate
proves that a nonempty open set of equally weighted, distinct, non-antipodal
circle triples with labels `(1,1,-1)` has increasing same-label squared
distance in both hidden layers for a sufficiently short positive interval
along the prescribed canonical `p=1` initialized flow. This refutes universal
monotone same-class attraction in either layer. I found no mathematical
correction required for this statement or equations (1)–(22). The result
does not establish generic fitting, eventual clustering, or any additional
identification with the original Gaussian-action model.

## 1. Scope, complete reading, and frozen fingerprints

The assignment was to audit every equation and claim of
`generic3_geometry_route.md`, with the specified scientific dependencies.
I read the entire candidate (lines 1–412), all of `docs/NOTATION.md`, and
the complete following authorized sections:

| Source | Complete section coverage | Lines |
|---|---|---|
| `arbitrary_pair_local.md` | Sections 1–4 | 20–331 |
| `three_four_input_extension.md` | Section 2 only | 111–167 |
| `docs/global_nonlinear.md` | C.4.7.9.3–4 | 12249–12377 |
| `docs/global_nonlinear.md` | C.4.7.10.B | 13161–13430 |
| `docs/global_nonlinear.md` | C.4.7.10.C.1 | 13431–13786 |
| `docs/global_nonlinear.md` | C.4.7.10.D.3 | 15146–15528 |

I also read and applied `solve-math-rigorously/SKILL.md`,
`investigate-conjectures/SKILL.md`, and its
`references/adversarial-audit.md`. No README, research contract, other route,
prior verdict, other study, or author discussion was used. No scientific
experiment, numerical integration, or subagent was used. Hash computation
was provenance work only. Only this audit report was written.

Whole-file SHA-256 fingerprints, recorded after the complete reading:

```text
generic3_geometry_route.md
536726d952eb3fb3487a799903c028c4b9f98a4be54df854a3b2075dc59eb0fb

arbitrary_pair_local.md
4bdb878378518455ca4e0cf7ea2ded8281d056b7aec98cef36c5ebf337c47b9a

three_four_input_extension.md
59c93c8756167fef609df326fd1633266c73d526e54e61aadc8f4b05d75791d9

docs/NOTATION.md
199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b

docs/global_nonlinear.md
81d969a531fc6daee26dbee2041fad8a3425a4b01580351387c5fc376cef412c
```

To distinguish the actually read sections from the unread remainder of
partially assigned files, their SHA-256 fingerprints follow. A section hash
uses the exact source bytes of the listed inclusive line range, retaining
line terminators.

```text
arbitrary_pair_local.md:20–331
e0a71a968e2831e2dbb65083dfa0e387312540ebfd09a580235dd168054c5bc1

three_four_input_extension.md:111–167
cbd33eff6a677e0d83655edd55047ac388e9bb5cacfbca7ba9ab7479bca1df13

docs/global_nonlinear.md:12249–12377
30960f45a2cd8dadf6d09ca2cd262471d30144bfa5e5fc305e13e01d79e827be

docs/global_nonlinear.md:13161–13430
b77fb96abfbf592faa64e401d4456f52c087723737df667abe834f6eea217380

docs/global_nonlinear.md:13431–13786
20c0590f399064f42ee8aa2ec51b72779e4dc889802caab7be6361d1446063ec

docs/global_nonlinear.md:15146–15528
3815d81705fac51fcd5b5489b6f6f961021cba525acf88e74bdc82fe818ae386
```

Whole-file hashing does not enlarge the scientific read scope. The
historical author-process assertions in the candidate's opening and final
section are not independently reconstructed by this mathematical audit.

## 2. Exact model and equation-by-equation checks

At order one, the prescribed raw columns are
`psi_1=(1,X_1,X_2,Y_1,Y_2)` and `psi_2=(1,Z_1,Z_2)`. Thus `M` has shape
`3 by 5`, the ridge is `1/4096`, and the candidate's dimensions and
normalization agree with (H3.N1). Inputs are the unit vectors
`u=x/sqrt(2)`, so there is no missing first-layer input factor. The full
metric is the population `L2` metric on `w,c` and the ordinary Frobenius
metric on `M`. It is not the Hilbert–Schmidt metric on the lifted filtered
action. The candidate correctly uses the former.

| Candidate item | Check and result |
|---|---|
| Unnumbered loss and metric; (1) | Exactly the unhalved probability-weighted loss and (H3.N1)–(H3.N2), specialized to three masses `1/3`. All expectations stay within their layer. |
| (2) | Differentiating `a_i`, then `z_i`, then `H_i` gives the displayed `J_i`. Pairing with `v`, exchanging the bounded feature contraction and expectation, and applying matrix transposition gives precisely both components of `J_i^*v`. The matrix adjoint is `E_2[b_2 S_i v] a_i^T`. |
| (3) | The lower gate linearization and its population adjoint are correct. Its matrix component is zero. The time derivatives used below are justified in the bounded-increment topology; see Section 5. |
| (4) | The loss variation is `(2/3) sum_i r_i {<J_i^*c,delta theta>+<H_i,delta c>}`. Negative gradient flow gives exactly `-2/3` in both equations. |
| (5) and its lower analogue | Differentiate the squared norm to obtain twice its pairing with `(J_i-J_j)theta'`, then substitute (4). The coefficient is `-4/3`; the residual index is the training index `k`. No pairwise label-only sign emerges. |
| (6)–(7) | `c(0)=0` gives `theta'(0)=0`, while `r_i(0)=-y_i` gives `c'(0)=2U_0`. In differentiating the hidden equation only the `c'` term survives, giving `theta''(0)=4J_U^*U_0`. |
| (8) | Terms quadratic in `theta'(0)` vanish. The remaining squared-distance second derivative is `2<difference, derivative times theta''(0)>`, giving the coefficient `8` in both layers. |
| (9)–(10) | Input oddness holds for every hidden state, with the same action in both directions. For this labeled law `U=H/3` and `J_U=J/3`, giving `4/9`, not `4/3`. |
| (11) | `D^2_12=4||H||_2^2` and `H'(0)=0` give `(32/9)||J^*H||^2`. Strict positivity is established by a nonzero matrix component, checked below. |
| (12)–(14) and the adjacent unnumbered constants | These are the exact order-one conditional Gaussian law, regression row, and reverse contraction. Both the upper ridge denominator and the `tau chi` response term are present. Section 3 supplies the independent normalization check. |
| Unnumbered `w''(0)` and (15) | The row component of `J^*H` is `sech^2(g_1)q_H e_1`. A second gate arises when differentiating the lower activation, so the distance curvature contains `sech^4(g_1)` with coefficient `32/9`. Conditioning gives the claimed positive integral. |
| (16)–(18) | The proposed family is admissible for `0<epsilon<pi/6`, the two curvature functions are continuous, and strict signs give an open set and positive initial-time derivatives. Section 5 checks each bridge. |
| (19) and the class-mean formula | `U'(0)=0`, `U''(0)=4J_U J_U^*U_0`, hence the coefficient is `8`. Also `U=(2/3) Hbar_+-(1/3) Hbar_-`; it is not a fixed multiple of their difference. |
| (20) and squared lower bounds | Opposite labels have difference of magnitude `2`. The residual triangle bound, Cauchy–Schwarz, and the one-Lipschitz gate give the exact chain. Both squared denominators and the handling of zero denominators are correct. |
| (21) | Equal labels cancel from `f_i-f_j`, leaving precisely `r_i-r_j`. Fitting annihilates this one readout projection; it imposes no equality of the two hidden fields. |
| (22) | The initial hidden velocities vanish and `c'(0)=2U_0`, so energy gives `L'(0)=-4||U_0||_2^2`. The assigned initialized Gram argument makes it strictly negative for every admissible triple. |

For the aggregate interpretation, the hidden gradient of `||U||_2^2` is
`2J_U^*U`. Thus (7) is twice that gradient at initialization. Calling it
initial ascent of this aggregate is exact; it would not justify an
all-time ascent claim, and the candidate explicitly avoids that inference.

## 3. Reverse-response normalization and analytic sign dependency

The book's exact core contraction is

\[
 C_{B,F}=\sum_i E_1[F\tanh g_i]E_2[\partial_{\xi_i}B]
       +\sum_i E_1[\partial_{\zeta_i}F]E_2[B\tanh\xi_i].
\]

For `B=Z_1`, the nonzero lower raw entries are consequently

\[
 C_{Z_1,X_1}=\alpha v_0,\qquad
 C_{Z_1,Y_1}=\alpha r+\tau\chi.
\]

Independence and centered oddness kill the other coordinate block and
constant entries. The lower Gram on `(X_1,Y_1)` is
`[[v_0,r],[r,ell]]`; the upper odd Gram is `tau I_2`.
With `R_l=G_l+eta I`, the prescribed Cholesky formula gives

\[
 B h=\psi_2^T R_2^{-1}C R_1^{-1}E_1[\psi_1h],\qquad
 B^*v=\psi_1^T R_1^{-1}C^T R_2^{-1}E_2[\psi_2v].
\]

This follows from `L_l^{-T}L_l^{-1}=R_l^{-1}`; it involves no replacement
metric. At `u=e_1`, the initialization formula gives
`H=tanh(kZ_1)`, `k=Phi(1)>0`. For `v=H(1-H^2)`, the constant upper
expectation vanishes by oddness, and the `Z_2` expectation vanishes by
independence and centering. The sole remaining coordinate is
`E[Z_1 tanh(kZ_1)sech^2(kZ_1)]`. Multiplication by `R_2^{-1}` therefore
produces exactly the candidate's `gamma`, with one denominator
`tau+eta`. Multiplication by the lower block produces
`gamma(a_*X+b_*Y)`. There is neither a missing ridge factor nor a missing
reverse response.

I checked the analytic monotonicity dependency rather than assuming the
sign of `a_*`. Its essential inequalities are valid:

1. `tanh^2 x >= x^2/(1+x^2)` and Gaussian Cauchy–Schwarz imply
   `v_0>=1/4`, `tau>=1/7`, and `0<alpha<=6/7`.
2. For `beta(x)=E sech^2(zeta+alpha x)` and `beta_0=beta(0)`, the centered
   Gaussian interval argument gives `beta(x)<=beta_0`. The symmetric tanh
   addition formula and `cosh(6/7)<=32/23` give
   `beta(x)>=q_0 beta_0` on `[-1,1]`, where `q_0=529/1024`.
   The stated factorial bound indeed yields `cosh(6/7)<=1+9/23`.
3. Conditional Gaussian integration by parts and Cauchy–Schwarz give
   `Var(Y|X)>=tau beta(X)^2`. Combining this with
   `E m(X)^2>=r^2/v_0` gives the regression denominator bound
   `ell+eta-r^2/(v_0+eta)>=tau chi^2+eta`.
4. The normal equations give `b_*>0`. Since
   `r<=alpha v_0`, the extra numerator term
   `alpha r eta/(v_0+eta)` is at most `eta`, hence at most `eta/chi`.
   It follows that `b_*<=1/chi<=1/(q_0 beta_0)`.
5. With `R_eta=v_0/(v_0+eta)>=1024/1025>q_0`, the negative coefficient
   of the upper bound on `b_*` is used in the correct direction. The
   derivative lower bound is

   \[
   \frac{d}{dx}\{a_*x+b_*m(x)\}
   \ge\alpha[1-R_\eta(q_0^{-1}-1)]
   \ge\alpha(2-q_0^{-1})=34\alpha/529>0.
   \]

Thus `j` is odd and `j'(g)>0` for every finite `g`. The dependency's
Gaussian integration-by-parts calculation of `Phi'` correctly cancels
the `tanh''` terms; bounded derivatives justify differentiation and
integration by parts, and dominated convergence handles the endpoints.
Its positive bound and oddness establish `Phi(1)>0`. No numerical sign
or positivity of `a_*` is needed.

The remaining assigned pair results also check: coordinatewise strict
monotonicity and the unit-circle norm prevent collinear coefficient vectors
except at equal or antipodal inputs. The two-function Gram argument then
uses positive density and the derivative at the origin correctly. These
are sufficient inputs for the three-function rank argument below.

## 4. Both strict curvatures and the Gram claim

For the upper layer, the normalized feature `X_1/sqrt(v_0+eta)` has
pairing `v_0/sqrt(v_0+eta)>0` with the initialized `h(e_1)=X_1`.
Hence `a(e_1)!=0`. The upper coordinate `Z_1/sqrt(tau+eta)` has a
strictly positive pairing with `tanh(kZ_1)sech^2(kZ_1)`: `k>0`, the
integrand is positive for `Z_1!=0`, and this variable has no atom at zero.
Consequently `d_H!=0`. The matrix component of `J^*H` is the rank-one
matrix `d_H a(e_1)^T`, whose Frobenius norm is their positive norm product.
This proves strictness of (11) without relying on the first-layer sign.

For the lower layer, conditioning the exact reverse contraction on `g_1`
gives `E[q_H|g_1]=gamma j(g_1)`. Since `j` and `tanh` are odd and
strictly increasing, `tanh(g_1)j(g_1)>0` whenever `g_1!=0`.
The remaining weight `sech^4(g_1)` is positive, `gamma>0`, and all factors
are bounded and integrable. The expectation in (15) is strictly positive.
This is a separate proof for the first layer; positivity of a total hidden
gradient norm would not by itself establish it.

For the three-input Gram claim, the assigned Section 2 applies because the
vectors `nu(u_j)=(Phi(u_{j,1}),Phi(u_{j,2}))` are nonzero and pairwise
noncollinear. A null `L2` linear combination of
`tanh(Z dot nu(u_j))` vanishes on the whole open square by positive density
and continuity. Differentiating along `Z=s z` three times gives a zero
cubic homogeneous polynomial. Choose a coordinate vector avoiding the
finitely many perpendicular lines; its pairings `A_j` are nonzero, and
the ratios `B_j/A_j` are distinct. The first three coefficients of that
cubic give an invertible `3 by 3` Vandermonde system in `t_j A_j^3`.
This proves independence. The same argument with all four coefficients
also validates the assigned four-input version.

In particular `U_0=(H_1+H_2-H_3)/3` cannot be zero for an admissible
triple. The normalized Gram is the ordinary Gram divided by three, so
no probability-weight factor is missing. The assigned readout fitting
certificate uses the ordinary Gram and is algebraically correct; it is
only a represented-state certificate, not a convergence result. The
candidate uses it only through independence and does not substitute its
nonzero fitted readout for the prescribed `c(0)=0`.

## 5. Regularity, input continuity, and admissibility

The required time regularity holds in

\[
 (w-g,c,M)\in L^\infty(\Omega_1;\mathbb R^2)
       \times L^\infty(\Omega_2)\times\mathbb R^{3\times5}.
\]

At fixed order the feature envelopes are finite. Tanh and every derivative
used here are bounded on the real line. Taylor remainders uniformly bound
its superposition derivatives in the displayed supremum norm, even with
the fixed unbounded offset `g`. Bounded feature expectations are bounded
linear maps, and the remaining operations are finite products. The vector
field is therefore continuously differentiable, indeed smooth, on bounded
sets in this space. The book's continuation argument bounds `c`, `M`,
and `w-g` on every finite interval using only bounded labels and unit
inputs. The restricted two-arc or time-40 support assumptions needed for
identification with a different model are not needed for this fixed-order
existence proof. The initialized flow and the distance observables are
therefore `C2` on every finite interval, as required.

This topology matters: one should not infer unrestricted Fréchet
smoothness of the lower tanh superposition map from `L2` to `L2` merely
from bounded scalar derivatives. The candidate does not need that claim.
Its supremum-norm argument supplies time differentiation, while (3) is
the bounded `L2` linearization and adjoint used in those pairings. This is
a valid interpretation of its stated proof, not a required correction.

For continuity in the input triple, the initializer, feature marks, and
`D` are fixed. If the directions converge, `tanh(g dot u_i)` and their
gates converge pointwise and remain bounded. Thus every lower feature
contraction converges by dominated convergence. The upper preactivations
and gates then converge with bounded feature envelopes. In particular,
all coefficient vectors in (2) converge, their lower adjoint components
converge in `L2`, and their matrix components converge in Frobenius norm.
For the lower distance formula, the relevant field is
`(s_i u_i-s_j u_j)(h_i-h_j)`, which is likewise bounded and converges
pointwise. These facts prove continuity of both curvature expressions
in (8). No bound involving an unbounded power of `g` is needed.

The three angles in (16) are `0`, `pi-epsilon`, and `pi+2epsilon`.
For `0<epsilon<pi/6`, their differences are neither zero nor multiples
of `pi`. Hence the triples are pairwise distinct and non-antipodal.
Choose the sign-preserving `epsilon_*` smaller than `pi/6` if necessary.
Both curvature signs are then strict for every `epsilon` in this interval.
Their positivity persists in an open neighborhood of each such triple
in `(S1)^3`; intersecting with the open admissibility conditions still
leaves an open neighborhood. The full open set can include perturbations
of `u_1`, although the displayed witness curve fixes `u_1=e_1`.

For each fixed triple in this set, let the two positive curvatures be
`a_1,a_2`. Time continuity supplies a common `t_*>0` with
`(D^ell_12)''(t)>a_ell/2` for `0<=t<t_*`. Since both first derivatives
at zero vanish, integration gives

\[
 (D^\ell_{12})'(t)>a_\ell t/2>0\qquad(0<t<t_*).
\]

This verifies (18) along each triple's own actual initialized trajectory.
Neither a common time over the whole open set nor an explicit numerical
value for `epsilon_*` or `t_*` is claimed or necessary. Here “generic”
means the stated distinct, non-antipodal admissible class; the result
establishes a nonempty open subset, not density or full measure.

## 6. Fitting inequalities and remaining scope

For an opposite-label pair,
`2<=|f_i-f_j|+|r_i|+|r_j|`. Taking the positive part and then using the
common readout gives the first two inequalities in (20). With current
action `A=U_2MU_1^*`, the pointwise Lipschitz gate yields
`||H_i-H_j||_2<=||A||op ||h_i-h_j||_2`, establishing the last inequality.
At a finite fitted state `b_ij=2`, so neither required denominator can
vanish. Uniform upper bounds on the readout and action norms are enough
to preserve a positive lower distance bound along an asymptotically
fitted sequence. Finite-time continuation bounds are not uniform
all-time bounds, and the candidate correctly does not use them as such.

For same labels, equation (21) leaves an entire readout-orthogonal
subspace available. In this setting there are also represented fitted
states with the initialized, independent hidden fields and the assigned
Gram-based readout. Thus the statement that fitting alone does not
force equal same-class hidden fields is justified. No claim is made that
the prescribed training trajectory reaches that represented state.

The initialized loss slope is strictly negative for all admissible
triples by the rank argument and (22). Its continuity in time also makes
loss decrease on a sufficiently short interval for each witness. Initial
loss improvement and initial same-class separation therefore coexist
without contradiction.

The candidate's final restrictions are accurate: it does not decide
monotone opposite-label separation, eventual same-class clustering,
unit-label fitting at infinite time, uniform readout/action bounds, or
full-state convergence. The initialized aggregate identity is not an
all-time multi-residual estimate. Fixed order remains distinct from
neural width, dictionary order limits, particle quadrature, and long-time
limits. None of those conclusions is imported from the restricted
Gaussian-action identification theorems.

## 7. Adversarial checks and final claim level

| Claim under attack | Strongest alternative or failure signature | Discriminator and validity gate | Audit consequence |
|---|---|---|---|
| Correct physical trajectory | A hidden loss rescaling or action metric changes the coefficients. | Derive (4) directly from the unhalved loss in the canonical population/Frobenius metric. | Factors `2/3`, `4`, `8`, and `32/9` all check. |
| First-layer strict separation | Dropping the reused-action response or assuming `a_*>=0` creates the sign. | Reconstruct the raw adjoint with both ridge inverses and prove monotonicity of the full conditional combination. | The `tau chi` term is retained and the sign is analytic without that assumption. |
| Admissible counterexample | The phenomenon exists only at coincident or antipodal inputs. | Prove both strict curvatures, continuous input dependence, and admissibility of (16). | An open admissible counterexample set is established. |
| Positive-time increase | A merely formal second derivative does not control actual evolution. | Smooth bounded-increment characteristic dynamics and finite-time continuation, then integrate positive curvature. | Both distances increase along the actual initialized trajectories. |
| Strict initial loss decrease | An unseen three-input Gram null direction makes `U_0=0`. | Positive-density extension and the cubic Vandermonde argument. | The Gram is positive definite and the slope is strictly negative. |
| Stronger clustering or fitting theorem | Local acceleration is being promoted to an all-time conclusion or another model. | Compare each stated conclusion with its time, norm, and fixed-order quantifiers. | No such promotion occurs; the listed long-time gaps remain open. |

There is no surviving fatal, witness-fatal, major, or conditional defect
in the claimed theorem. The supremum-norm versus `L2` interpretation
above is a precision note, not a missing proof bridge. Numerical artifacts
cannot account for the result because the proof uses no numerical
experiment. The strongest remaining ordinary explanation is that inputs
near conflicting/coincident and same-label antipodal configurations
separate transiently; the open-set construction deliberately includes
such admissible configurations. That possibility limits any claim about
typical or eventual behavior, but it does not rescue a universal
monotonicity claim.

The audited claim level is an exact local-in-time result for the canonical
fixed `p=1` population closure, with an open existential input family.
This internal PASS supplies no established-book promotion or independent
promotion-review status.
