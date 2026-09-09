# Preregistered smooth nonpolynomial depth-order-five regression

**Status:** frozen before either producer prediction is inspected and before
the experiment is run.

## Decision question

Does the independently frozen terminal \(C_H=F_H^{(5)}(0)\) formula predict
the exact finite-width moving-feature jet for \(H=3,4\) on a smooth
nonpolynomial activation?

## Testbed

Use

\[
\phi(x)=\frac{\sin x}{\sqrt{(1-e^{-2})/2}},
\qquad Q^0=1.
\]

This preserves \(Q^\ell=1\) at every hidden layer and uses derivatives of all
orders without making the network polynomial.  All parameters are independent
standard Gaussians and \(B=1\).

Before any large-width comparison:

1. the two producer predictions must be frozen;
2. their exact canonical maps must agree;
3. two independently written finite-width order-five moving-flow oracles must
   agree seedwise at widths \(1,2,5\) for both depths.

## Primary metric

For each \(H\), estimate \(\mathbb E[D_n^5f_n]\) at
\(n\in\{32,64,128,256\}\).  Fit the prespecified affine model

\[
\mathbb E[D_n^5f_n]=C_H+\gamma_H/n
\]

by inverse-variance weighted least squares.  The primary statistic is

\[
z_H=\frac{\widehat C_H-C_H^{\rm GNF}}
{\operatorname{SE}(\widehat C_H)}.
\]

Record the chi-square per degree of freedom.  A visibly invalid affine fit
or chi-square \(p<0.01\) makes the result inconclusive rather than failed.

## Decision rule and budget

- Pass: both depths have \(|z_H|\leq3\) and pass the fit-validity gate.
- Fail: at least one replicated depth has \(|z_H|>5\) while every numerical
  validity gate passes.
- Inconclusive: otherwise.

The initial allocation is at most \(1800,1200,600,250\) networks at the four
widths for each depth, hence at most \(7700\) networks total.  Only an
otherwise valid \(3<|z_H|\leq5\) result may use the remaining budget, capped
at \(10\,000\) networks total and width \(256\).  No activation, depth, width,
fit model, or threshold may be changed after prediction inspection.

## Claim consequence

A pass supports the frozen algebraic map on this discriminator but cannot
prove the equality-partition calculation or the annealed theorem.  A fail
falsifies at least the current map or its scaling bridge.  An inconclusive
run changes no algebraic claim.
