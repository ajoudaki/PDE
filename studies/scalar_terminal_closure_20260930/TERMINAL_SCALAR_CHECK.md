# Internal check of the finite scalar terminal theorem

Check date: 2026-09-30.

Candidate: `TERMINAL_SCALAR_THEOREM.md`.

Frozen candidate SHA256:

`2d89e4613b8f7729bb772a7da21b7453278735eb644583b189a95cdefc042ddd`

Verdict: **PASS for the stated conditional finite-width q=1 theorem.** No
material algebraic error, missing bootstrap hypothesis, or incorrect error
constant was found. The passive-observable extension and the comparison at
equal physical times also pass. This is an internal mathematical check, not
an independent promotion review or an approval to promote the result.

The scientific inputs were the complete frozen candidate and
`paper/main.tex`, lines 178–443, solely to verify the exact q=1 model and its
normalization. The repository instructions and the
`solve-math-rigorously` skill were also read. No study README, other study,
route, prior discussion, numerical experiment, or external source was used.
The candidate was not edited.

## Exact finite model and residual equation

The permitted manuscript passage gives, after setting
\(v_a=-2\bar\delta_{a,0}\) and
\(k_a=\bar h_{a,0}/\tau\), the exact equations

\[
\dot w=-\frac2m\sum_b r_b g_b,\qquad
\dot A=-\frac2m\sum_b r_b\ell_b\frac{x_b^T}{\sqrt d},
\]
\[
\dot v_b=-2r_bd_b,\qquad
\dot k_b=\frac{\|r\|}{\sqrt m\tau}(h_b-k_b),\qquad
\dot\tau=\frac{\|r\|}{\sqrt m}.
\]

Differentiating \(B=W_0+(mn)^{-1}\sum_bv_bk_b^T\) therefore gives precisely
candidate equation (1). In particular, the motion of the normalized keys
contributes a second term to \(\dot B\); it cannot generally be omitted.

Differentiating the output and substituting these velocities gives

\[
\begin{aligned}
\dot r_a={}&-\frac2m\sum_b r_b\frac{g_a^Tg_b}{n}
-\frac2m\sum_b r_b I_{ab}\frac{\ell_a^T\ell_b}{n}\\
&-\frac2m\sum_b r_b
  \frac{d_a^Td_b}{n}\frac{k_b^Th_a}{n}
+\frac{\|r\|}{m\sqrt m\tau}\sum_b
  \frac{d_a^Tv_b}{n}\frac{(h_b-k_b)^Th_a}{n}.
\end{aligned}
\]

This verifies every factor of \(m,n,\sqrt m\), both signs, the index order in
\(C_{ab}\), and the vector \(b\) in (2)–(4). The first two terms of \(C\)
are symmetric positive semidefinite; the third need not be symmetric or
positive. The additional \(\|r\|b\) term is genuinely homogeneous of degree
one in the residual when the coefficients are frozen. It is not generally
quadratic in the residual.

The displayed state equations verify (5). For finite \(n,m,d\), with fixed
finite \(W_0\), all coefficient fields are smooth on \(\tau>0\). The full
vector field is locally Lipschitz there: the residual is a smooth function
of the state, its Euclidean norm is locally Lipschitz, and all remaining
factors are smooth. Smoothness of the full vector field at \(r=0\) is not
needed or asserted. Its value at \(r=0\) is zero.

At the stipulated zero-readout initialization, the manuscript's moment
initialization implies \(v=0\), \(k=h\), and \(\tau=1\). Consequently
\(\dot A=\dot v=\dot k=0\), \(\dot B=0\), and \(\dot g=0\).
Although \(\dot w\) and \(\dot\tau\) can be nonzero, \(d=\ell=0\) initially,
so the last two terms of \(C\) have zero first derivative. Both \(b\) and its
first derivative vanish initially. The candidate's onset statement follows.
This statement is conditional on zero readout; the manuscript's more general
phrase “small” readout alone would not imply it.

## Terminal certificate and continuation

Let \(z=\|r\|\) and \(q=\|X-X_0\|\), using the stated state norm for the
latter. For \(z>0\), the residual equation gives

\[
\dot z=-\frac{r^TC(X)r}{z}+r^Tb(X)
\le-\bigl(\lambda_0-
\|C(X)-C_0\|_{\rm op}-\|b(X)-b_0\|\bigr)z.
\]

Equation (7) proves (16). On the interval stopped at either ball exit or
\(Jq=\lambda_0/2\), the resulting exponential estimate and (6) give exactly
(17). Its uniform upper bound is strictly less than both exit thresholds by
(9), so neither exit can occur.

More explicitly, for \(M=2HR/\lambda_0<a\), the trajectory remains in the
closed ball of radius \(M\) about \(X_0\). This is a compact subset of the
admissible domain, since the dimension is finite and the larger closed ball
is assumed admissible. A locally Lipschitz vector field can be continued
past any finite maximal existence time when its trajectory remains in such
a compact subset: it is bounded there, hence the trajectory has a limit at
that time, and local existence from the limit extends it. This supplies the
continuation step used by the candidate.

The speed is integrable, and in fact

\[
\|X(t)-X_\infty\|
\le\frac{2HR}{\lambda_0}e^{-\lambda_0t/2}.
\]

Thus the finite state converges. Continuity of the output map and decay of
the residual imply interpolation at the limit. No positive-loss stationary
point inside the certified region can invalidate this conclusion.

The edge cases are handled correctly:

- If \(R=0\), local uniqueness and the zero vector field give the stationary
  solution and zero errors in every stated bound.
- If \(J=0\), there is no aggregate-margin exit to stop at, and the frozen
  residual and clock are exact. The proof can simply omit that stopping
  condition.
- If \(H=0\), the state is stationary. With the residual defined by that
  state, a positive margin and \(R>0\) would contradict (16), so no
  nonstationary exception is hidden in this case.
- At a zero of the residual, the full state and frozen residual fields both
  vanish. Uniqueness and continuity justify the extension of estimates
  originally derived at positive residual norm.
- The strict inequalities in (9) provide a positive gap from the ball
  boundary and from loss of the dissipation margin. They are stronger than
  a non-strict invariance assertion and suffice as written.

The statement about an open finite-state region is appropriately an
existential possibility, not a reachability theorem for arbitrary data or
initialization. The certificate must actually be checked at a reached
handoff to apply it to that training trajectory.

## Frozen dynamics and all error constants

For \(T(u)=-C_0u+\|u\|b_0\), putting \(e=u-v\) gives

\[
e^T(T(u)-T(v))
=-e^T C_0e+(\|u\|-\|v\|)e^Tb_0
\le-\lambda_0\|e\|^2.
\]

The norm is 1-Lipschitz, so \(T\) is globally Lipschitz with constant at most
\(\|C_0\|_{\rm op}+\|b_0\|\). This proves global existence, contraction,
and the second decay bound in (12). Both residual velocities agree at the
handoff because the coefficients in (10) are the exact handoff values.

Writing the full residual equation as \(\dot r=T(r)+E\) yields

\[
\|E(t)\|\le Jq(t)z(t)
\le \frac{2JH}{\lambda_0}R^2e^{-\lambda_0t/2}.
\]

Contraction and zero initial error then give

\[
\begin{aligned}
\|r(t)-\widehat r(t)\|
&\le\int_0^t e^{-\lambda_0(t-s)}\|E(s)\|\,ds\\
&\le\frac{4JH}{\lambda_0^2}R^2
\bigl(e^{-\lambda_0t/2}-e^{-\lambda_0t}\bigr).
\end{aligned}
\]

This verifies (20). The maximum of \(u-u^2\) on \([0,1]\) is \(1/4\),
which gives (13). Multiplication by
\((\|r\|+\|\widehat r\|)/m\le2R/m\) gives (14). Integration gives

\[
\int_0^\infty\|r-\widehat r\|\,dt
\le\frac{4JH}{\lambda_0^3}R^2.
\]

Since both clocks start from the same \(\tau_0\) and have speeds equal to
their respective residual norms divided by \(\sqrt m\), this proves (15)
for every physical time and for their limiting values. Both clocks have
finite endpoints; separately,
\(\tau_\infty-\tau_0\le2R/(\sqrt m\lambda_0)\) and
\(\widehat\tau_\infty-\tau_0\le R/(\sqrt m\lambda_0)\).
No inversion or identification of the two clock parameterizations is used.
All constants in (12)–(15) are valid, though not optimized.

## Passive observables

For a smooth scalar observable, differentiation of (5) gives
\(p_a(X)=DO(X)F_a(X)\) and \(q(X)=DO(X)F_0(X)\).
These coefficients are smooth on the same finite-dimensional domain, so a
finite local Lipschitz constant on the compact ball is available. The
candidate also states the needed coefficient bound explicitly.

If the frozen observable is initialized at its exact handoff value, direct
subtraction bounds its velocity error by

\[
J_O\|X-X_0\|\|r\|
+(\|p_0\|+|q_0|)\|r-\widehat r\|.
\]

The first integral is at most
\(4J_OHR^2/\lambda_0^2\) using the same dropped-factor estimate as the
candidate; retaining the factor in (17) would improve this to
\(2J_OHR^2/\lambda_0^2\). The second integral is exactly bounded as claimed
in (22). Thus (22) is correct and conservative. Both true and frozen
observable velocities are integrable because their coefficients are bounded
and the corresponding residual norms are integrable.

A fixed finite list of training Gram entries or predictions at fixed query
inputs consists of smooth functions of this finite state, so the extension
applies after recording the stated coefficients. This does not silently
provide a uniform bound over an unbounded query family. Taking the clock
observable, with \(p=0\) and \(q=1/\sqrt m\), reproduces (15). The stronger
cubic loss error follows from the quadratic form of the loss, and is not
automatically available for a general observable.

## Scope and minor presentation changes

The three examples in Section 5 support their stated limitations. Omitting
the frozen \(b_0\) term can produce an error of order \(R^2\) in loss; decay
of loss need not imply integrable residual norm; and a contracting rotating
residual can have a finite activity endpoint without a limiting activity-time
direction. The last example implicitly uses \(R>0\); stating that explicitly
would remove the zero-denominator edge case in its displayed endpoint
formula.

The checked theorem concerns the actual **finite-width q=1 closure**, with
its learned reconstructed matrix. It does not prove approximation of the
original dense gradient flow at fixed order q=1. It also supplies no
population theorem: compactness, smooth coefficient bounds, and continuation
here use finite dimension, and the constants may depend on width. A
population extension would require an explicitly specified state space,
well-posed dynamics, appropriate coefficient bounds, and a valid continuation
argument there. The candidate expressly preserves these distinctions.

Likewise, the terminal evaluator has the claimed \(m\) moving residual
scalars, optional scalar observables, \(m^2+m\) fixed coefficients, and
\(O(m^2)\) evaluation cost. This count neither computes its handoff data nor
establishes the cost of reaching a handoff with a prescribed accuracy. In
particular, a root-width accuracy claim would still need a choice of handoff
residual and control of the width-dependent constants. The candidate does
not claim those missing bridges are proved.

Two optional presentation repairs would improve self-containment without
changing the theorem:

1. Replace the opening dependency on the study README with the explicit
   state equations displayed at the beginning of this report, and state
   \(k(0)=h(0),v(0)=0,\tau(0)=1,w(0)=0\) where the onset claim is made.
   The permitted manuscript passage supplied the equations for this check;
   the candidate currently leaves \(\dot A\) and \(\dot w\) implicit.
2. In the sentence following the differentiated output, list the substitutions
   in the same order as (2): \(\dot w\), \(\dot A\), and the residual-driven
   part of \(\dot B\). The current list places (1) before \(\dot A\) while
   referring to the first, second, and third terms “respectively.” The formulas
   themselves have the correct order and normalization.

No correction to the mathematical theorem, hypotheses, rates, or constants
is required for its stated finite-width conditional scope.

## Addendum: check of the self-contained revision

Follow-up check date: 2026-09-30.

Revised candidate SHA256:

`fbb93521867a03c8a01ebe8c29f88d04b643cf3d6fa4af53151e13ddf4c6bde5`

The complete revised candidate was read. It now includes the exact state
equations and the initialization values needed for the onset statement,
lists the differentiated-output substitutions in the correct order, and
specifies \(R>0\) for the rotating-residual example. These additions agree
with the model and calculations checked above. Its opening now identifies
the theorem as conditional and points to this report. No hypothesis,
mathematical conclusion, error constant, or proof step was weakened by the
revision.

The verdict remains **PASS for the stated conditional finite-width q=1
theorem**. The original report and original candidate hash above remain
unchanged as the record of the first check. The revised candidate was not
edited during this follow-up check.
