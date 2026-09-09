# Identity-activation depth-2/depth-3 jet: frozen protocol

## Frozen objects

All hidden widths are equal to \(n\), all trainable parameter entries are
independent standard Gaussians at initialization, and every hidden activation
is the raw identity \(\phi(x)=x\).  The two-hidden-layer model is

\[
 X=u,\qquad Z=n^{-1/2}WX,\qquad f_{n,2}=n^{-1}A^\top Z,
\]

and the three-hidden-layer model is

\[
 X=u,\qquad Z=n^{-1/2}WX,\qquad Y=Z,\qquad
 T=n^{-1/2}VY,\qquad f_{n,3}=n^{-1}A^\top T.
\]

Every displayed block is trained with unit metric weight.  Define

\[
 D_n=n\nabla f_{n,H}\mathbin\cdot\nabla,\qquad
 F_H^{(r)}(0)=\lim_{n\to\infty}D_n^r f_{n,H},
 \qquad H\in\{2,3\}.
\]

The limit is width first at each fixed derivative order.  The requested
maximum order is eleven.

## Frozen method

Because the identity activation keeps every limiting coordinate state
linear-Gaussian, use the exact chronological detransposition recurrence rather
than a nonlinear sparse-polynomial or derivative-forest compiler.  Integrate
each moving matrix before taking the width limit, replace each forward and
transpose use of its initialization by jointly Gaussian innovations, and keep
all causal Stein-response terms.  All scalar covariances and coefficients are
computed over the rationals.

Two coefficient assemblers will be run:

1. ordinary Taylor coefficients, with explicit Volterra denominators;
2. derivative-normalized coefficients, with binomial/multinomial weights.

They may share the exact linear-Gaussian covariance primitive, but not the
coefficient recurrence assembler.

## Research contract

- **H1.**  The linear-Gaussian detransposition program gives the exact
  width-first jets through order eleven for both depths within the frozen
  resource bound.
- **H0.**  A missing causal response or matrix-memory term causes a control
  mismatch, the two coefficient normalizations disagree, or the program
  exceeds the resource bound.
- **Primary output.**  Exact values of \(F_H^{(r)}(0)\) for
  \(H=2,3\) and \(0\le r\le11\).

## Validation gates

1. Reproduce the pre-existing independent leading-width path/Wick controls

   \[
   (F_2'(0),F_2^{(3)}(0),F_2^{(5)}(0))=(3,48,1464),
   \]

   \[
   (F_3'(0),F_3^{(3)}(0),F_3^{(5)}(0))=(4,160,13888).
   \]

2. The ordinary-Taylor and derivative-normalized routes agree exactly at
   every order through eleven.
3. Centered-Gaussian parity gives exact zero at every even order, including
   order zero.
4. Every reported value is an integer.

An exploratory pre-freeze run of the older diagram enumerator produced
\(F_2^{(7)}(0)=76800\).  It may be recorded as retrospective corroboration,
but it is not a preregistered primary gate.

## Frozen resources and claim boundary

- Maximum order: eleven.
- Per exact route and depth: two minutes wall time and 1 GiB virtual memory.
- No positive-time trajectory, convergence radius, arbitrary-depth
  complexity theorem, all-order sign theorem, or Stieltjes representation is
  claimed here.
- “Fast” means that the exact width-limit recurrence completes inside this
  explicit bound without enumerating derivative histories or Wick pairings.
