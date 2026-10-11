# Internal check of the initial-time compression error bounds

Reviewer: scoped agent `uniform_time_scope`, 2026-10-11.

Verdict: **PASS for the stated deterministic extension of the existing
source/fitting/comparison results. No substantive flaw found.** This is an
internal bounded review, not a promotion review and not a new validation of the
source-event construction.

## Scope and frozen inputs

I read `EARLY_ERROR_BOUNDS.md` completely and checked its new steps against the
referenced Legendre projection, defect, fitting, signed comparison, coefficient
and absorption formulas in `paper/compact_legendre.tex`; and against the
selected-model definition, fitting estimates, pair-defect identity, comparison
variables, readout-deficit identity, cancelled-energy estimate, scalar integral
comparison and tolerance in `paper/compact_selected.tex`. The canonical setup
in `paper/compact.tex` was already read in this scoped context.

No other agent's report or joint-result draft was read. The reviewer previously
authored `UNIFORM_TIME_SCOPE.md`; that earlier assignment concerns endpoint
obstructions, not the derivation reviewed here. The rigorous-solution and
canonical-notation skills, including the neural-network reference, remain the
applicable presentation and proof instructions.

The reviewed note has SHA-256
`b78f533571d0136fae8c29a8859f786cc0109239ef36314e05b170bf7f3e960a`.
The relevant paper files have SHA-256

```
862aa37139ad9af67ac04b52949f838031e91077021b2da9060244d36ab4e0f9  paper/compact_legendre.tex
3add2b694f38a4d7dbce90e51dafd375a7e8dee2e06d26b2d5af451bddb44885  paper/compact_selected.tex
```

HEAD was `ef8362764b4eb8144d7af8d6f8db080fdaaf82ca`; the index was empty.
This review edits only the present report.

## 1. Legendre terminal-tail factor

Let \(\lambda=\gamma/m\le1\), \(z=Y/\lambda\), and \(a_0=4z\),
as in the candidate. Since the compressed residual RMS obeys
\(\widehat\rho(s)\le Y\), its physical clock satisfies

\[
0\le A(T)-1\le\min\{YT,a_0\},\qquad
\frac{A(T)-1}{a_0}\le\min\{\lambda T/4,1\}
\le\min\{T,1\}.
\]

The forward clock history is constant on \([0,1]\), and its clock derivative
has aggregate sample/neuron RMS at most \(V_h\) afterward. The weighted
projection estimate therefore gives, at each terminal \(A=A(T)\),

\[
\|(I-\Pi_q^A)h\|_{L^2}^2
\le\frac{V_h^2}{q(q+1)}\int_1^A\xi(A-\xi)\,d\xi
\le\frac{V_h^2(1+a_0)(A-1)^2}{2q^2}.
\]

Thus the candidate's terminal coefficient is exactly the valid upper bound
\(F_h(T)=F_h(A(T)-1)/a_0\), where
\(F_h=V_ha_0\sqrt{(1+a_0)/2}\).

The crucial integration step is also valid. For the *actual fixed trajectory
history* \(h\), define
\(e_h(A)=h(A)-(\Pi_q^Ah)(A)\). The growing-interval projection identity
and zero prefix error yield

\[
\int_1^{A(T)}\|e_h(A)\|^2\,dA
=\|(I-\Pi_q^{A(T)})h\|_{L^2([0,A(T)])}^2.
\]

The analogous identity applies to the actual backward history, whose prefix
is zero and whose value at the join is zero because the initial readout is
zero. Sample Cauchy--Schwarz in the exact defect formula, followed by
time Cauchy--Schwarz with \(dA=\widehat\rho\,dt\), bounds the integrated
defect by the product of these two terminal tail norms. There is no replacement
of a time-dependent history by a different terminal history in this step.
Consequently the refined forward factor multiplies both terms in the original
absorption inequality.

The original backward-tail coefficient is a uniform upper bound for every
horizon. If the current horizon precedes the prescribed freezing time, the
freezing discrepancy on the current interval is zero, while the derivative
integral remains bounded by its original upper bound. The backwards-history
comparison term \(B_d\sqrt{a_0}D(T)\) also remains valid. No refinement of
either backward term is needed.

Since \(F_h(T)\le F_h\), the original absorption condition keeps its
coefficient at most one half. Signed stability and output subtraction therefore
give the candidate's equation (6), with the original coefficient multiplied by
\(\min\{T,1\}\). Substituting the unchanged prescribed Legendre order
uses exactly the original coefficient ledger. Taking \(T=t\), and then the
existing fitted limit, proves the asserted all-time statement.

## 2. Selected prefix readout and observation error

All norms in this section are the selected metric norms or the corresponding
Euclidean sample norms. Write \(c_n=y-f_n\) on the training panel and
\(\rho_n=\|c_n\|_2/\sqrt m\le Y\). Because restriction commutes with
the dense readout's integral equation,

\[
w_R(t)=\frac2m\sum_a\int_0^t c_{n,a}(s)h_{R,a}(s)\,ds.
\]

The uniform feature bound \(\|h_{R,a}\|\le H_r\) gives
\(\|w_R(t)\|\le2H_rYt\). The pair-defect formula applies to a training
feature at time \(s\) and a query feature at time \(t\): both belong to
families approximated by the same fixed source space. It does not require
equal times. Thus its \(P_h\eta\) bound integrates to

\[
|\langle w_R(t),h_R(t,x)\rangle-f_n(t,x)|\le2P_h\eta Yt.
\]

On the training inputs, dividing the vector of these errors by \(\sqrt m\)
gives \(\|d_R\|_2\le2P_h\eta Yt\), with no extra factor of \(m\).

In the exact readout-deficit identity, \(P_C\) is the orthogonal projection
for the selected metric and \(p\) lies in its range. Hence

\[
\|\widehat w_C-w_R\|
\le b_e+\frac{4H_rFYt}{\sqrt\lambda}(a_h+\eta)
       +\frac{4P_hYt}{\sqrt\lambda}\eta.
\]

Split the query error into the corrected-readout difference paired with
\(h_C\), the feature difference paired with \(w_R\), and the observation
defect. This gives exactly the candidate's equation (10). In particular every
source-only output term carries \(Yt\); no derivative of an approximation
error is taken.

## 3. Scalar coefficient and unchanged orders

For \(X=\beta^L\), \(u=\sqrt{\log(en)}\), the source operator norm
satisfies \(\|V_R\|\le H_r\). Indeed its columns have norm at most
\(H_r/\sqrt m\), so its Hilbert--Schmidt norm is at most \(H_r\).
Therefore \(\nu=\|V_Rc_n/\sqrt m\|\le H_rY\).

Using the candidate's ledger and \(z\le1\), the three terms of \(g\)
are bounded respectively by

\[
200X^{15}Y,\qquad
X^{18}Y+32X^{39}Yu,\qquad
40X^9Y/\sqrt\lambda.
\]

These are bounded by
\(YA_X(1+\lambda^{-1/2})(1+u)\) for the displayed \(A_X\).
The existing integrated coefficient estimate gives
\(\int_0^Tg\le1+u\). Applied to the scalar integral inequality with
zero initial error, it yields

\[
E(t)\le\eta(1+\lambda^{-1/2})e^{1+u}\int_0^tg(s)\,ds
\le4eA_Xz\eta(1+u)e^u t,
\]

because
\(Y(1+\lambda^{-1/2})^2\le4Y/\lambda=4z\).
This is the important cancellation: the pointwise coefficient estimate does
not leave an additional inverse-gap power in the final accuracy requirement.

For \(t\le1\), direct substitution in equation (10) bounds its coefficient
of \(E\) by
\(2X^3+16X^{12}+4X^9=C_0\), and its source-only coefficient by
\((16X^{12}+4X^9+8X^7+2X^4)z\eta t=C_1z\eta t\).
Both stated constants are sufficient. The original tolerance satisfies

\[
z\eta(1+u)e^u
\le\frac{Y}{2Cn(1+\lambda^{-1/2})}
\le\frac{Y}{2Cn}.
\]

The early bound is consequently \(C'Yt/n\), with \(C'\) depending only
on activations and depth. For \(t\ge1\), the existing \(Y/n\) complete
trajectory bound applies. No new source space, optimizer, clock, or power of
\(n,m,\gamma^{-1},Y\) is introduced. Tightening the activation/depth
constant in the tolerance is optional for this conclusion; it only changes
the constant inside the existing logarithmic accuracy requirement.

## Limits of this verdict

The check establishes that the proposed initial-time factors follow from the
specific existing deterministic estimates it cites. It does not independently
reprove the analytic source construction, its probability, or every coefficient
bound in the prior manuscript. It establishes no dense same-time lower bound
and no simultaneous relative-error theorem. The note states these limitations
correctly. No changes to its proof are required by this review.
