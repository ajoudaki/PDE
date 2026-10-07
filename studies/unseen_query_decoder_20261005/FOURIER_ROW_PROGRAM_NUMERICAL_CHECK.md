# Numerical reconstruction of Fourier row-program evaluation

2026-10-06. Scoped independent calculation against the frozen candidate.
This is a conditional evaluator audit, not a full compressed-model verdict.
No experiment or other review was read.

## 1. Frozen input and audit conclusion

The complete input was `FOURIER_ROW_PROGRAM_EVALUATION.md`, SHA-256
`932b6f748e2c7562c1364c0cb8874f6fdccf21b022e61977df1e4e0967efba66`.

The probability identities, truncation bounds, streamed quadratures,
precision scales and conditional-prefix density argument reconstruct.
Under its explicit boundedness, global Lipschitz and scalar-evaluation
contracts, the proposed workspace is polynomial in the stated parameters,
with the number of rows entering through its logarithm. No array of all
rows or retained Gaussian-root oracle is used.

The conditional version correctly fixes the observed training summaries
and their actual update-noise level. It integrates only appended query
summaries and Fourier variables. It does not rerun the scalar training
recursion or replace a noisy-training likelihood by noise added after
training.

For a total numerical decoder, specify one harmless guard: if the
computed conditional denominator is below the certified threshold
$d_*/4$, return a fixed bounded value instead of dividing. With the
stated integration budgets this guard is inactive on the proved density
event, including after retained-state rounding. Outside that event no
accuracy guarantee is claimed, but the algorithm must still be defined.
Clipping its final answer to $[-H,H]$ is also harmless.

The conditional theorem's arbitrary fixed $\eta_{\rm tr}>0$ should
either be restricted to $0<\eta_{\rm tr}\le1$, as in the intended
small-noise application, or have $\log(2+\eta_{\rm tr})$ included
alongside $\log(2+\eta_{\rm tr}^{-1})$ in the enlarged parameter.
This is an input-size qualification for a very large training-noise
scale, not a problem at the stipulated tiny scale.

The introductory phrase about row independence after conditioning should
be read as the precise Fourier likelihood factorization proved later.
The actual posterior rows are generally dependent. The candidate's
Sections 3 and 8 correctly distinguish these statements.

## 2. Exact smoothing density and bias

Use the candidate's program
$C_r=n^{-1}\sum_iF_r(Z_i;C_{<r})$, with iid
$Z_i\sim N(0,I_D)$, global bounds $|F_r|\le B$, $|\psi|\le H$,
and the specified sup-norm Lipschitz constants $\Lambda,K\ge1$.
Add independent update noises $\eta E_r$ at every scalar step, not
only after the last step. Coupling the two programs on the same rows,
their maximum prefix error obeys

\[
 e_r\le\Lambda e_{r-1}+\eta|E_r|,
 \qquad
 |\mathbb E\psi(C^\eta)-\mathbb E\psi(C)|
       \le K\eta R(1+\Lambda)^R.
 \tag{1}
\]

The maximum includes old coordinates, and $\Lambda\ge1$ makes the
displayed recursion valid for them as well. This verifies the smoothing
bias without a derivative assumption on clipped instructions.

For fixed rows, sequential conditional densities give

\[
 L_c(Z)=\prod_{r=1}^R\kappa_\eta\left(
           c_r-\frac1n\sum_iF_r(Z_i;c_{<r})\right).
 \tag{2}
\]

There is no unjustified Jacobian or delta function: each new summary has
the displayed Gaussian density conditional on the previous summaries
and the rows. Multiplication proves (2) even for merely Lipschitz row
functions.

Choose $\eta$ within a fixed dyadic factor of the minimum in candidate
equation (9). Then the bias is at most $\varepsilon/64$ and, for its
parameter $P$, $\log\eta^{-1}=O(P^2)$. The global cap gives
$|C_r^\eta|\le B+\eta|E_r|$. A union bound outside
$[-M,M]^R$, $M=B+1$ or the stated larger dyadic value, costs at most
$2R e^{-1/(2\eta^2)}$. Multiplication by $H$ gives the claimed
summary-tail error.

## 3. Fourier factorization retains the exact finite-row law

The elementary identity

\[
 \kappa_\eta(x)=\frac1{2\pi}\int_{\mathbb R}
                      e^{-\eta^2\xi^2/2+i\xi x}\,d\xi
 \tag{3}
\]

can be checked by scaling and differentiating the Gaussian Fourier
integral: integration by parts gives $J'(x)=-xJ(x)$ and the Gaussian
integral gives $J(0)=\sqrt{2\pi}$. All those integrals are absolutely
convergent.

Apply (3) to (2) only after restricting $c$ to its finite box.
The absolute integrand is bounded by
$H e^{-\eta^2\|\xi\|^2/2}$ on that box, so Fubini applies over
the summaries, frequencies and row probability measure. Define

\[
 \chi(c,\xi)=\mathbb E_Z
   e^{-i\sum_r\xi_rF_r(Z;c_{<r})/n}.
\]

The phase depending on the complete row array then factors under its
unconditional iid law into $n$ identical single-row expectations. This
proves candidate equation (14) with the factor $\chi(c,\xi)^n$.
It does not assert that rows remain independent conditional on their
empirical summaries. The same row is reused across all terms inside one
characteristic function, exactly as required by the adaptive program.

Integrating the absolute Gaussian frequency tail gives

\[
 (2\pi)^{-R}\int_{\xi\notin[-V,V]^R}
                  e^{-\eta^2\|\xi\|^2/2}\,d\xi
 \le(\sqrt{2\pi}\eta)^{-R}2R e^{-\eta^2V^2/2}.
 \tag{4}
\]

Thus the candidate's cutoff includes the essential summary volume
$H(2M)^R$ and the density-normalization factor. It yields
$\log V=O(P^2)$ and combined finite integration volume
$\log\mathcal V=O(P^3)$. No cancellation or contour deformation is
being used to avoid these factors.

## 4. Single-row and outer quadrature precision

The phase inequalities give

\[
 |\Delta_c\chi|\le RV\Lambda\|\Delta c\|_\infty/n,
 \qquad
 |\Delta_\xi\chi|\le RB\|\Delta\xi\|_\infty/n.
\]

Since $|\chi|\le1$ and $|z^n-w^n|\le n|z-w|$ in the unit disk,
the factor $n$ cancels from the outer Lipschitz estimate. Subtracting
the bounded test, oscillatory factor, Gaussian envelope and power
separately gives precisely the candidate's valid bounds

\[
 L_c=K+HRV(1+\Lambda),\qquad
 L_\xi=HR(M+B+\eta^2V).
 \tag{5}
\]

For single-row error
$\delta=\varepsilon/(128nH\mathcal V)$, a Gaussian box
$[-A,A]^D$ with $A^2\ge2\log(16D/\delta)$ loses at most
$\delta/8$ probability. The density-weighted single-row integrand
has sup-norm Lipschitz bound
$RV\Lambda/n+DA$: the phase contributes its first term, and the
sum of density derivative magnitudes is at most $DA$ on the box.
The displayed midpoint grid therefore has error below its budget and
$\log Q_z=O(P^3)$.

Project the numerical characteristic function into the complex unit disk
before powering. This preserves its error. If each later arithmetic
operation incurs error at most $\rho$, projection after products
gives a power error bounded by $Cn\rho$. For example, along an
addition chain the error for exponent $k+\ell$ is at most the sum
of the two old errors plus the local error; induction gives a bound
proportional to the exponent. This uses only $O(\log n)$ operations
and adds $O(\log n)$ accuracy bits.

An inside-disk finite-bit projection can be made explicit: for a rational
point outside the disk, use a certified upper approximation to its norm,
divide by that upper bound, and round coordinate magnitudes inward.
The resulting rational point is in the disk and approximates the exact
projection to the assigned tolerance. Comparison of its squared rational
norm with one uses ordinary integer arithmetic. Alternatively one can
include a small final inward rescaling. There is no exact irrational
normalization requirement.

The outer midpoint error is
$\mathcal V(L_c+L_\xi)\max(M,V)/Q$, yielding
$\log Q=O(P^3)$. The characteristic-function error contributes at
most $H\mathcal V n\delta=\varepsilon/128$. The remaining
explicit tail, quadrature, power, elementary-function and summation
budgets have ample slack under the displayed constants. Signed and
complex cancellations are handled by absolute error, not relative
error in a possibly small final integral.

## 5. Peak memory and the claimed exponent

The parameter includes $R,D,I$ and the logarithms of all numerical
envelopes. The preceding estimates give

\[
 \log\eta^{-1},\log V=O(P^2),\quad
 \log\mathcal V,\log\delta^{-1},\log Q,\log Q_z=O(P^3),
\]
\[
 2R\log Q+D\log Q_z=O(P^4).
 \tag{6}
\]

The final line counts the number of actual summands in the nested grids,
not merely their integration volume. Allocating per-summand error using
these counts requires $b=C P^4$ bits. Weighted accumulation bounds the
sum of summand magnitudes by volume times the integrand envelope, so no
larger integer accumulator is needed. The phase arguments can have large
values but only $O(P^2)$ integer-part bits; range reduction and the
displayed accuracy cover them.

At one time the calculation keeps outer summary/frequency coordinates,
their counters, a row point and row counters, a few accumulators, and
the scalar instruction evaluator's workspace. There is no array of
quadrature points and no array indexed by the $n$ rows. These live
coordinate and counter arrays use $O(P^5)$ bits at the conservative
precision. Elementary integer, real and complex arithmetic can be
implemented in $O(b^2)$ space, giving the claimed $O(P^8)$ overhead.
The actual row/test evaluator is then added through
$S_{\rm eval}(CP^4,CP^2,I,R,D)$, not hidden as a free oracle.

This validates the conditional finite-bit workspace statement. Its
activation/data computability assumption is necessary and explicitly
separate from the mathematical bounded-strip activation class. In a
real-arithmetic formulation the original activation primitives may
instead be supplied exactly, but that is not a finite-bit algorithm
for an uncomputable activation.

## 6. Fixed-prefix conditional density and its denominator

Now keep the actual training-noise scale $\eta_{\rm tr}$ fixed and
condition on a retained prefix $C=c$. Its likelihood is exactly the
product of Gaussian step densities in candidate equation (31), with
the observed preceding summaries substituted into every $F_r$. Its
expectation $p(c)$ is the true density of that noisy training state.
This is not the density of a different program with noise added only
at its endpoint.

Append passive query summaries with $c$ fixed and fresh query marks.
The training functions ignore the new marks. Fourier expansion of the
training and query density factors gives the single-row characteristic
function (33) and numerator (34). Training $c$ is not integrated;
only the appended query summaries and frequencies are integration
variables. The outer dimension is $R+2S$, and the row dimension is $D$.
Evaluating $F_r(z;c_{<r})$ is an evaluation of its supplied response
circuit, not regeneration of a training empirical mean.

If query smoothing is added for the calculation, its pathwise coupling
bias is uniform over every fixed row array and fixed $c$. Averaging
under the posterior therefore leaves the same bias bound; no reciprocal
denominator is needed for this part. Query-box tails have the same
property because the added query noises remain independent conditional
on the rows and training state. The Fourier tails, by contrast, are
absolute numerator/denominator errors and must include all factors in
candidate equation (35).

The density lower bound is elementary and valid without any smoothness
or independence of posterior rows. For a training box of volume $V_0$,

\[
 \Pr\{C\text{ in the box},\ p(C)<\rho/V_0\}
       \le\int_{\{p<\rho/V_0\}\cap\text{box}}p(c)\,dc
       \le\rho.
 \tag{7}
\]

Thus $d_*:=\rho/(2M)^R$ is a valid denominator lower bound at the
ideal observed state except for this failure and the explicit summary
tail. It is not a uniform lower bound at every possible state.
If $p\ge d_*$, $|\widehat p-p|\le d_*/2$ and $|N|\le Hp$,
division gives

\[
 \left|\frac{\widehat N}{\widehat p}-\frac Np\right|
       \le\frac{2}{d_*}
                    (|\widehat N-N|+H|\widehat p-p|).
 \tag{8}
\]

Allocating the proposed absolute errors of order
$\varepsilon d_*/(1+H)$ proves the conditional tolerance. Its bit
cost depends on $\log d_*^{-1}$, which is polynomial in the enlarged
parameter, not on a unit-cost reciprocal. Adding $S$, the query
instruction data, $\log\eta_{\rm tr}^{-1}$ and $\log\rho^{-1}$
to that parameter preserves the estimates (6) and the absolute workspace
exponent.

For a total implementation, if a computed denominator is below $d_*/4$,
return zero or another fixed value in $[-H,H]$. On the good density
event the proposed numerical errors, and the rounding estimate below,
leave it above that threshold. This guard only defines behavior where
the theorem has not guaranteed relative accuracy.

## 7. Retained-state precision and posterior continuity

The density assertion concerns the continuous ideal state. Applying it
directly to a rounded discrete observation would be incorrect; the
candidate correctly uses continuity instead.

The maximum single Gaussian density is
$(\sqrt{2\pi}\eta_{\rm tr})^{-1}$, and its derivative maximum
is at most that value divided by $\eta_{\rm tr}$. Each argument
$c_r-n^{-1}\sum_iF_r(Z_i;c_{<r})$ changes by at most
$(1+\Lambda)\|c-\widetilde c\|_\infty$. Product telescoping,
uniform over all row arrays, therefore gives

\[
 L_{\rm den}\le CR(1+\Lambda)
        (\sqrt{2\pi}\eta_{\rm tr})^{-R}/\eta_{\rm tr}.
 \tag{9}
\]

For fixed rows, couple the query noises at $c$ and $\widetilde c$.
The query summary error recursion gives the candidate's bound
$L_g\le KS\Lambda_{\rm q}(1+\Lambda_{\rm q})^S$.
Combining it with the bounded query test and likelihood gives

\[
 L_N\le P_{\max}L_g+HL_{\rm den}.
 \tag{10}
\]

If $\|c-\widetilde c\|_\infty$ obeys candidate equation (41),
then $p(\widetilde c)\ge d_*/2$. The ratio subtraction (8), with
Lipschitz numerator and denominator changes, bounds the difference of
posterior test expectations by $\varepsilon/8$. Evaluating the ratio
at $\widetilde c$ with correspondingly reduced numerical budgets adds
only the already counted tolerance. The logarithms of (9)–(10) and the
required retention precision are polynomial in the enlarged parameters.

This is approximation to the posterior function evaluated at the ideal
state, not the exact posterior conditioned on a quantization bin. The
state acquisition/update procedure must independently achieve this
coupling to the ideal state; the Fourier theorem does not prove that
construction accuracy.

For finitely many retained prefixes, apply (7) with failure $\rho/R$
at each prefix. The extra precision cost is $O(\log R)$ and there is
one common high-probability density event for all prefixes. Query/time
uniformity requires uniform row-circuit bounds, not a new denominator
event for each query. A continuum of newly observed unrelated noisy
states is outside this finite-prefix argument.

## 8. Smoothing, CDF and current-state scope qualifications

The unconditional theorem may choose its update noise after fixing the
test's Lipschitz constant. The conditional theorem must not alter the
already observed training noise or add a new training-smoothing step at
query time. It fixes $\eta_{\rm tr}$ correctly. For an appended query
law that already contains scalar noise, either integrate that specified
law directly, or explicitly account for any additional query smoothing
by its uniform coupling bound. These are different targets unless that
bias is budgeted.

A bounded ramp CDF test has $H=1$ and $K$ of order the reciprocal
transition width. This adds only its logarithm to the numerical parameter,
but the smoothing-bias choice must use that $K$. For one bisection, the
query-noise level can be fixed uniformly across all threshold locations
using the same bound, so the decoder evaluates one family of CDF tests.
Atoms need no anti-concentration assumption for the stated smoothed
brackets or robust-center use. Exact CDF values at atoms are not proved.

The finite-bit theorem also requires counted precision interfaces for
all fixed data and any real query/time parameters appearing as circuit
coefficients. Its scalar-evaluation contract does not by itself invent
those interfaces or their error moduli. The physical bridge can provide
uniform bounds for them, but that is part of applying the theorem.

Root clipping can transfer a globally bounded test expectation with the
candidate's explicit $4HnD e^{-A_0^2/2}$ error. It does not repair an
uncapped inverse-history sensitivity, nor justify a small innovation cap
after conditioning on a full dense tape. Those are separate bridge
questions; the larger innovation caps in the corrected physical bridge
are compatible with this evaluator's logarithmic input bounds.

The algorithm genuinely avoids materializing the dense row randomness.
It still requires an exact finite iid-row interaction specification and
an explicit bounded/Lipschitz response circuit of counted size. It does
not prove that specification, weighted acquisition, posterior conditioning
on a retained state rather than private compilation data, or a complete
current-state compressed training model. Those interfaces remain outside
this numerical audit.

## 9. Provenance

The frozen evaluator was read completely, including its conditional
Section 8 and finite-precision subsection. The algebra and error budgets
were reconstructed directly. The checker also verified the separately
assigned corrected physical bridge and appended its own existing check;
that verification is not another review's scientific input. No external
source, experiment or other review was accessed for this calculation.

Only this assigned numerical check was created, with no candidate,
maintained-file or Git-index mutation. The previously applied proof and
notation instructions remain in force, including the reported custom
notation-skill access fallback.

## 10. Minimal corrected-version verification

At the supervisor's explicit request, only the two algorithmic
qualifications in Section 1 were corrected in the candidate: the retained
training scale now satisfies $0<\eta_{\rm tr}\le1$, and a computed
real denominator below $d_*/4$ returns zero. The existing absolute
integration tolerance is less than $d_*/4$; since (41) gives
$p(\widetilde c)\ge d_*/2$ on the rounded-density event, that guard
is inactive there. No other candidate claim or scientific scope was
changed.

The resulting candidate SHA-256 is
`55dd1adb0234448ac2ec022446fd1c3a4ad7245e26f10deabac614f2ac17b1d1`.
Both corrections were checked against the numerical argument above and
resolve this audit's two implementation qualifications. No assembly
review or other review report was read for this verification.
