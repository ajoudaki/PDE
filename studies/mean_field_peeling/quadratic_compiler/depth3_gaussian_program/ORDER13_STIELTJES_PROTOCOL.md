# Depth-3 extension through order thirteen: frozen protocol

## Authorized extension and canonical object

The user explicitly requested two further Stieltjes moments.  This protocol
therefore supersedes only the previous order-nine stopping rule; every model,
normalization, and limit convention remains unchanged.

The object is the raw activation (phi(x)=x^2), one-input, equal-width,
three-hidden-layer network defined in `PROTOCOL.md`, with independent standard
Gaussian initialization and

\[
D_n=n\nabla f_n\mathbin\cdot\nabla,
\qquad
F^{(r)}(0)=\lim_{n\to\infty}D_n^r f_n
\]

at each separately fixed (r).  No unit-Gram quotient, activation
normalization, depth-2 coefficient, finite-width extrapolation, or
positive-time interpretation is admissible.

## Primary targets and exact stopping point

Compute the complete formal jet through order thirteen, including

\[
F^{(11)}(0),
\qquad
F^{(13)}(0),
\]

then transform it by

\[
K(y)=F'\!\left(F^{-1}(y)\right)
=F'(0)+\sum_{r\ge0}(-1)^r\mu_r y^{2r+2}.
\]

The order-eleven derivative determines (\mu_4), and order thirteen
determines (\mu_5).  Stop after (\mu_5).  Do not attempt (F^{(15)}(0)),
(\mu_6), or any positive-time observable.

## Stieltjes decision objects

With (\mu_0,\ldots,\mu_5), audit every nonempty principal minor of every
available ordinary and shifted Hankel matrix

\[
H_d=(\mu_{i+j})_{i,j=0}^d,
\qquad
H_d^+=(\mu_{i+j+1})_{i,j=0}^d.
\]

The two newly completed matrices are

\[
H_2=
\begin{pmatrix}
\mu_0&\mu_1&\mu_2\\
\mu_1&\mu_2&\mu_3\\
\mu_2&\mu_3&\mu_4
\end{pmatrix},
\qquad
H_2^+=
\begin{pmatrix}
\mu_1&\mu_2&\mu_3\\
\mu_2&\mu_3&\mu_4\\
\mu_3&\mu_4&\mu_5
\end{pmatrix}.
\]

- **Finite-order compatible:** all available principal minors are
  nonnegative.  If all are positive, report positive definiteness.
- **Finite-order violation:** at least one exact principal minor is negative;
  retain the corresponding principal submatrix or rational vector as the
  counter-witness.
- **Inconclusive:** a validation gate fails or a route exhausts its frozen
  resource bound.

Either determinant sign would change the finite-order conclusion and is
accepted without a trend-based override.

## Derivative validation gates

1. The exact prefix through order nine must remain

   \[
   0, 14175, 0, 139445032896, 0,
   4298284752832899360, 0,
   272967464957028310013451264, 0,
   29466555372596241677766026853605376.
   \]

2. Orders ten and twelve vanish exactly by parity.
3. Every output rational has denominator one.
4. The ordinary-Taylor and derivative-normalized/binomial assemblers agree
   on every derivative through order thirteen.
5. Source hashes are frozen before the first scaling pilot.

## Moment and Hankel validation gates

1. Two transformations agree exactly:
   direct rational reversion/composition and the triangular identity
   (F'(t)=K(F(t))).
2. The previously accepted (\mu_0,\ldots,\mu_3), (H_1), and (H_1^+)
   are reproduced exactly.
3. PSD decisions use exact principal minors.  Floating eigenvalues are only
   conditioning diagnostics.
4. Every claimed (3\times3) positive-definiteness result must include all
   seven nonempty principal minors, not only the full determinant.

## Precommitted compute branches and hard budget

The frozen baseline engine has SHA-256

`2f053874429f02c4c2830fceadc13d688e5962d85503741f76c40a98ef380f0e`.

1. Run the ordinary-Taylor route through order eleven as a scaling/validity
   pilot.  If it completes within 10 minutes and 2 GiB while passing all
   gates, proceed to order thirteen.
2. If the order-eleven pilot passes but projects beyond the full-route cap,
   an exact representation or caching optimization is authorized.  It may
   not alter the recurrence, prune by an unproved sign assumption, use
   floating arithmetic, or inspect the unknown derivative values as tuning
   targets.  Any modified engine must re-run the full prefix gates.
3. Each complete order-thirteen route has a 45-minute wall-clock and 8-GiB
   resident-memory cap.  Run routes sequentially.
4. The cumulative terminal budget is 100 minutes of production wall time.
   Stop after the two routes agree or after any cap is exceeded.

## Claim boundary

Passing all available order-thirteen conditions proves only six-moment
Stieltjes compatibility for this fixed depth-3 formal jet.  A negative minor
would disprove the all-order Stieltjes conjecture for this model.  A positive
result does not prove the missing higher conditions, a representing measure
for an unknown full sequence, formal-series convergence, or identification
with a positive-time mean-field limit.

