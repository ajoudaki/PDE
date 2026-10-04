# Internal mathematical check: scalar circle selection

Checked the complete corrected `SCALAR_CIRCLE_SELECTION.md`, SHA256
`b303194cf220c608dd8f841a5fee5d022dbaabc7caf55ffd8abe114980377347`, using only
that note and `ENERGY_ROUTE.md`, SHA256
`015b9c83cfdcc52c16913f56ef2e2d5f50bd391064a88dba8f0592253c9377b3`.
This is an internal check, not a promotion review. No experiments or candidate
edits were performed.

**Result:** the corrected note is mathematically correct under its stated
assumptions. The equations, exponential fitting, finite endpoint, exact
classification formula, angular risk, and positive limiting key lag all
verify. No outstanding correction remains.

## Resolved wording corrections

The initially checked version, SHA256
`41574000703c1d51455f9f02c090841bbbe76a707af1bcfb57f7895e9c1f5d7c`, omitted
an explicit condition from the sentence “its endpoint is strictly below its
right-hand limit at initialization.” It requires **\(\beta\ne0\)**.
For \(\beta=0\), permitted by the stated deterministic assumptions,
\(\mathcal R_{\rm cls}(t)=0\) for every \(t>0\), and its endpoint equals
its right-hand initialization limit. The final statement that classification
“improves” requires the same condition, or the statement that risk never
increases and decreases strictly when \(\beta\ne0\). Although \(\beta=0\) has
Gaussian probability zero, the stated theorem assumes only \(a_0W_0\ne0\).

The original phrase “The signed a grows strictly” is also clearer as
“\(|a|\) grows strictly”: when \(a_0<0\), \(a(t)\) itself decreases.
The formal statement already used the correct absolute value. The author
applied all three wording corrections; a complete reread of the corrected
source verified them, with the new source hash recorded above.

## Verified mathematical content

- The normalized training input is \((1,0)\), so only the first read-in
  component changes and \(\beta\) is constant. The transformed equations
  (3) agree exactly with the scalar equations in `ENERGY_ROUTE.md`.
  The sign-preserving region, positivity of the residual at finite time,
  and strict growth of \(H\) and \(|a|\) follow as stated. Local uniqueness
  applies at zero residual because the absolute-value clock is locally
  Lipschitz.

- Since \(\Gamma\ge\Gamma_0>0\),
  \(e'\le-2\Gamma_0^2e\), giving training MSE
  \(e^2\le\exp(-4\Gamma_0^2t)\). The bounds
  \(u\le\Gamma_0^{-1}\), \(\widetilde v\le\Gamma_0^{-3}\), and the
  displayed integrable bound on \(|a'|\) are correct. Together with
  \(\tau_\infty\le1+(2\Gamma_0^2)^{-1}\) and bounded monotone \(K\),
  they prove finite limits and rule out finite-time escape. Strict positive
  movement gives \(|a_\infty|>|a_0|\).

- For \(t>0\), \(\operatorname{sign}B=c\) and
  \(\operatorname{sign}w=ycs\). Odd monotonicity of both tanh functions
  gives
  \[
  \operatorname{sign}f_t(\theta)
  =ys\operatorname{sign}(a\cos\theta+\beta\sin\theta)
  =y\operatorname{sign}(\cos\theta+(\beta/a)\sin\theta).
  \]
  Thus equation (1) includes the negative-\(a_0\) case correctly.
  Boundary ties may use the usual \(\operatorname{sign}(0)=0\); any binary
  tie convention has no effect on the uniform-circle risk.

- The oriented normals differ by
  \(\delta=\arctan(\beta/a)\in(-\pi/2,\pi/2)\), independently of the
  common label sign \(y\). The two disagreement arcs have total length
  \(2|\delta|\), proving equation (2). In particular, with
  \(A=|a|\) and \(c_\beta=|\beta|\),
  \[
  \mathcal R'_{\rm cls}(t)
  =-\frac{c_\beta A'(t)}{\pi(A(t)^2+c_\beta^2)}.
  \]
  This is strictly negative for \(\beta\ne0,t>0\), and zero for
  \(\beta=0\). Since \(A_\infty\) is finite and strictly larger than
  \(A_0\), the endpoint risk is strictly positive and strictly below its
  initial right-hand limit exactly when \(\beta\ne0\).

- The key-lag formula is valid at the infinite-time limit: \(\tau\) is
  bounded, \(H'\ge0\) is integrable, and
  \((\tau(H-K))'=\tau H'\). Therefore
  \[
  H_\infty-K_\infty
  =\tau_\infty^{-1}\int_0^\infty\tau H'
  \ge(H_\infty-H_0)/\tau_\infty>0.
  \]

The note appropriately fixes an explicit test truth and acknowledges that
different true boundaries can reverse the risk comparison. Its conclusion
is a one-point scalar learning theorem; no general multi-sample or universal
generalization claim is supported or asserted.
