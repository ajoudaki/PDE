# Adversarial audit

## Claim ladder

1. **Abstract coupled Euler theorem:** pass.  It requires a restartable
   autonomous schedule observable with a horizon-uniform fifth
   \(\ell^1\)-schedule derivative.
2. **Actual \(L=1\) network:** pass after correction of the displayed
   plus sign in \(\kappa_{\phi,1}\).  No matrix-response bridge occurs.
3. **Actual reused-matrix network at fixed \((t,L)\):** pass.  The
   arbitrary-\(T\) fixed-step identification is fully action-indexed.
4. **Quadratic cubic law for \(L\ge2\):** pass after repair.  The final
   proof uses a truncated formal algebra rather than a false nonlinear
   finite-span neighborhood, and its temporal/static naturality lemma
   explicitly matches all cross-time source and response marks.  Two
   independent re-audits pass it.
5. **Uniform \(t^4\) network remainder for \(L\ge2\):** open.  No current
   proof supplies both a horizon-free restartable mixed-schedule
   functor and an activation/depth-only fifth schedule envelope on a
   total-time tube.

## Positive checks

- The hybrid split telescope factors every local defect by \(h^2\).
  Three remaining schedule derivatives cost \((2t)^3\), and summing
  \(t\) defects gives exactly \((8/3)Qt^4|h|^5\).
- The autonomous Euler fifth-order coefficient uses
  \({2t\choose l}-2^5{t\choose l}\), \(1\le l\le5\); every resulting
  polynomial has degree at most four.
- For \(L=1,\phi(x)=x\),
  \[
  F_{k,1}(h)=\frac{(1+h)^{2k}-(1-h)^{2k}}2
  \]
  and the quintic discrepancy coefficient is
  \[
  \frac43t(t-1)(2t-1)(8t-9),
  \]
  so the \(t^4\) power is sharp.
- The scalar activation-envelope constant is an explicit two-dimensional
  Gaussian integral and contains no output or trajectory modulus.

## Rejected shortcuts

- Separate fifth-derivative bounds for the fine and coarse outputs give
  \(t^5\), not the required coupled \(t^4\).
- A fixed-horizon compiler constant
  \(\mathcal S_{2t,L}\) grows much faster than a polynomial in \(t\);
  it cannot be renamed as an activation/depth-only constant.
- A finite span of initialization jet fields is not a neighborhood on
  which the nonlinear population network is defined.
- Equality of covariance matrices alone does not prove deletion of
  singular duplicate histories; the response must descend to the
  corresponding Hilbert quotient.

## Decisive unresolved bridge

For \(L\ge2\), construct a common population object for every finite
mixed schedule which:

1. agrees pointwise, after the width limit at fixed increments, with the
   actual adaptive reused-\(W,W^\top\) network;
2. is invariant under zero-step insertion/deletion and represents every
   hybrid fine/coarse schedule;
3. has an explicit activation/depth tube
   \(\sum_i|\delta_i|\le\rho_{\phi,L}\); and
4. obeys
   \[
   \sup_m\sup_{\|\delta\|_1\le\rho_{\phi,L}}
   \|D_\delta^5\mathcal F_m\|_{(\ell^1)^5\to\mathbb R}
   \le Q_{\phi,L}.
   \]

Until this bridge is proved, the sharp general-\(L\), general-\(t\)
statement is conditional/open.
