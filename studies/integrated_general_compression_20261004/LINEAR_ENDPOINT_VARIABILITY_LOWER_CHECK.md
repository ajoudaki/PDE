# Internal reconstruction of the deep-linear endpoint lower bound

2026-10-04. **PASS within the candidate's stated scope.** This is an
adversarial internal reconstruction, not a promotion review. No candidate
file was edited, and no experiment or additional scientific source was
used.

## Frozen inputs and scope

Both files were read completely.

| Input | SHA-256 |
|---|---|
| LINEAR_ENDPOINT_VARIABILITY_LOWER.md | 212841e1591ce11a632e0e68d2e7a1f39286ee41ec599d552ab550578dc8c66f |
| GENERAL_EXPLICIT_FITTING.md | 5c6f12b78847a2b2874c5bc82eb1cea5f4929ee071b114d09b098397c5e2b8d6 |

The reconstruction checked the conditional endpoint law, independence of
the fitting event from unused Gaussian directions, canonical
normalizations, fitting/energy constants, all finite-width probability
bounds, and the precise scope of the two-sided scaling.

The candidate is correct for identity activation at every layer, fixed
\(L\ge2\), linearly independent unit training vectors, and its displayed
small-label condition. It proves a true fixed-nonzero-label fitted-endpoint
lower bound. Its only probabilistic input beyond elementary Gaussian
calculations is the explicitly quantified initialization/fitting event
of the second frozen input.

## 1. Normalizations and reduction to active input coordinates

Let \(V=[v_1,\ldots,v_m]\), \(G=V^\top V>0\), and let \(U\) and
\(U_\perp\) be deterministic orthonormal bases of the training span and
its orthogonal complement. Set
\[
C=U^\top V,\qquad A_{\mathcal S}=AU,\qquad A_\perp=AU_\perp.
\]
Then \(C\) is square and invertible, \(V=UC\), and
\(G=C^\top C\). Each column of \(C\) has norm one because its
corresponding training vector belongs to the span of \(U\).

For each Gaussian row of \(A_0\), its coordinates in the deterministic
orthogonal basis \([U\ U_\perp]\) are independent standard Gaussians.
Consequently \(A_{\mathcal S,0}\) and \(A_{\perp,0}\) are independent
standard Gaussian matrices, and both are independent of all initialized
hidden mixers. This establishes the claimed active/unused independence
without any conditioning on training success.

Writing
\[
b(t)=n^{-1}W^{(2)}(t)^\top\cdots W^{(L)}(t)^\top w(t)
\]
gives \(f_n(t,v)=v^\top A(t)^\top b(t)\) and
\(\delta_a^{(1)}=nb(t)\). The canonical first-weight equation is
\[
\dot A=-\frac{2n}{m}b\,r^\top V^\top.
\]
Thus \(\dot A_\perp=0\), and
\(\dot A_{\mathcal S}=-(2n/m)b\,r^\top C^\top\).
All training features and the remaining block velocities involve only
\(A_{\mathcal S}\), the hidden mixers, and the readout.
These are exactly the equations of the same canonical model in input
dimension \(m\), with unit inputs given by the columns of \(C\).

There is no extra factor of \(m\), \(d\), or \(n\) in this reduction.
The loss still averages over the same \(m\) samples; the first-weight and
readout mobilities are still \(n\); the hidden mobilities remain one.
The physical clock is unchanged.

## 2. Quantitative fitting event and its independence

For identity activation the fitting input specializes to
\[
b_{\rm activation}=0,\quad s=1,\quad t_2=0,\quad H=1,\quad
Q^{(j)}=G.
\]
Its depth constant is
\[
F=9^{2L-2}+4\sum_{j=0}^{L-2}9^{2j}
=\frac{21\,9^{2L-2}-1}{20},
\]
so the candidate's condition
\(Y\le\lambda/(8\sqrt F)\), \(\lambda=\gamma/m\), is precisely the
fitting theorem's sufficient condition.

The initialization threshold also specializes exactly:

- The covariance Lipschitz constant is \(1\), and the propagation sum is \(L\).
- The fourth-moment envelope is \(96\).
- The entrywise tolerance is \(e_0=\min(1/4,\lambda/2)\).
- The sphere mesh radius in the reduced input space is \(1/(4\,8^L)\).
- Its cardinality bound is \(P_0=(1+8^{L+1})^m\).
- The Chebyshev/union term is
  \(2L(m^2+P_0)96L^2/(\varepsilon e_0^2)
   =192L^3(m^2+P_0)/(\varepsilon e_0^2)\).
- The rectangular first-layer net term uses input dimension \(m\), giving
  the stated \(m\log9+\log(8/\varepsilon)\) numerator.

These reproduce every entry of candidate (12). Both denominators,
\(8-2\log9\) and \(8-\log9\), are positive.

The resulting event \(\mathcal E\) is measurable entirely with respect
to the active initialization and has probability at least
\(1-\varepsilon\). On it, the reduced fitting theorem gives global
existence, convergence of all active parameters, interpolation, the
hidden operator bounds \(9\), and
\[
\|w(t)\|_2/\sqrt n\le2Y/\sqrt\lambda.
\]
Its all-query first-layer feature bound, specialized to identity,
also gives
\[
\sup_{\|u\|=1}\|A_{\mathcal S}(t)u\|_2/\sqrt n<2.
\]
Hence \(\|A_{\mathcal S,\infty}\|_{\rm op}\le2\sqrt n\).
This sharper constant is justified by the feature bound, not by
incorrectly replacing the separate operator cap \(9\).

The frozen unused columns can be arbitrary finite values on
\(\mathcal E\): they never enter the active equations. The polynomial
vector field and uniqueness therefore identify the full solution with
the convergent active solution plus these frozen columns. In particular
full-parameter and endpoint existence do not require a full
\(d\)-dimensional sphere event that would depend on \(A_{\perp,0}\).

## 3. Deterministic fitted component and effective-vector bounds

Let \(\beta_\infty=A_\infty^\top b_\infty\) denote the coefficient of
the linear predictor in unit input coordinates. Interpolation gives
\[
C^\top A_{\mathcal S,\infty}^\top b_\infty=y,
\quad
A_{\mathcal S,\infty}^\top b_\infty=C^{-\top}y.
\]
It follows that
\[
P_{\mathcal S}\beta_\infty
=UC^{-\top}y=VG^{-1}y,\qquad
\|C^{-\top}y\|_2^2=y^\top G^{-1}y=a_y^2.
\]
Thus the active fitted predictor is deterministic even though its
parameter factorization is random.

The first-layer bound from Section 2 yields
\[
a_y\le2\sqrt n\,\|b_\infty\|_2,
\qquad \|b_\infty\|_2\ge a_y/(2\sqrt n).
\]
The fitting energy bound and the \(L-1\) hidden operator bounds give
\[
\|b_\infty\|_2
\le9^{L-1}\|w_\infty\|_2/n
\le\frac{2\,9^{L-1}Y}{\sqrt{\lambda n}}.
\]
The order and number of transposed hidden mixers are correct. No
minimum-norm or implicit-bias characterization is being assumed.

## 4. Exact conditional Gaussian law

Condition on both independent active initialization sigma-algebras.
On \(\mathcal E\cap\mathcal E'\), both limits \(b_\infty,b_\infty'\)
are measurable with respect to that conditioning. Their unused matrices
remain independent standard Gaussian matrices, even after imposing
\(\mathcal E\cap\mathcal E'\), since that event is active-measurable.

The active coefficients cancel exactly, leaving
\[
\beta_\infty-\beta_\infty'
=U_\perp
\left(A_{\perp,0}^\top b_\infty
      -A_{\perp,0}'{}^\top b_\infty'\right).
\]
The \(k=d-m\) coordinates in parentheses are conditionally independent
centered Gaussians of common variance
\[
\sigma^2=\|b_\infty\|_2^2+\|b_\infty'\|_2^2.
\]
Since \(U_\perp\) is an isometry, the full unit-sphere supremum is
the Euclidean norm of this coefficient difference. Hence its conditional
law is exactly \(\sigma\chi_k\), and
\[
\frac{a_y}{\sqrt{2n}}\le\sigma
\le\frac{2\sqrt2\,9^{L-1}Y}{\sqrt{\lambda n}}.
\]
Its conditional second moment is \(k\sigma^2\), with precisely the
bounds in candidate (25).

The statement is a conditional law on the active good event, not an
unconditional Gaussian law with a deterministic scale. No independence
of trained coordinates is required. On failures of the active event,
one may assign arbitrary values to the endpoint variables; probability
statements involving the theorem's lower and upper bounds must include
the active good event or endpoint existence, as the candidate states.

For a fixed unit direction in \(\mathcal S^\perp\), the law is instead
\(N(0,\sigma^2)\). Therefore the \(\sqrt{k}\) factor belongs specifically
to the sphere supremum. Returning to inputs \(x=\sqrt d\,v\) introduces
no extra \(\sqrt d\) factor.

## 5. Reconstruction of every finite-width probability bound

For \(X=\chi_k^2\), \(k\ge1\),
\(\mathbb EX=k\) and \(\mathbb EX^2=k^2+2k\). Splitting the expectation
at \(k/2\) and applying Cauchy--Schwarz on the upper event gives
\[
\Pr\{X\ge k/2\}\ge\frac{k^2}{4(k^2+2k)}
=\frac{k}{4(k+2)}\ge\frac1{12}.
\]
On that conditional Gaussian event,
\[
\sigma\sqrt X\ge
\frac{a_y}{\sqrt{2n}}\sqrt{k/2}
=\frac{a_y}{2}\sqrt{k/n}.
\]
Integration over the active good event therefore gives
\[
\Pr\{\mathcal E\cap\mathcal E',
 D_\infty\ge(a_y/2)\sqrt{k/n}\}
\ge(1-2\varepsilon)/12.
\]
For \(\varepsilon=1/8\), this is exactly \(1/16\). Thus candidate
(7), (26), and (27) have the correct constants and probability allocation.

For the tails, the exact moment generating function is
\((1-2t)^{-k/2}\). Its centered upper and lower cumulants obey
\[
\log\mathbb Ee^{t(X-k)}\le\frac{kt^2}{1-2t}
\quad(0<t<1/2),\qquad
\log\mathbb Ee^{-t(X-k)}\le kt^2\quad(t>0).
\]
For every \(x>0\), substituting
\(t=\sqrt x/(\sqrt k+2\sqrt x)\) in the upper Chernoff bound gives
exponent exactly \(-x\) at deviation \(2\sqrt{kx}+2x\).
Substituting \(t=\sqrt{x/k}\) in the lower bound gives exponent
\(-x\) at deviation \(2\sqrt{kx}\). This verifies candidate (28).

The union of the two conditional Gaussian tails has probability at most
\(2e^{-x}\). Adding at most \(2\varepsilon\) for the active failures
gives the probability \(1-2\varepsilon-2e^{-x}\) in candidate (29).
When the displayed lower square-root argument is negative, its positive
part gives the valid trivial bound zero.

Finally take \(\varepsilon=\delta/4\) and \(x=\log(4/\delta)\).
Then \(2\varepsilon+2e^{-x}=\delta\). If \(k\ge16x\), then
\[
k-2\sqrt{kx}\ge k/2,\qquad
k+2\sqrt{kx}+2x\le13k/8.
\]
The upper scale in (29) becomes at most
\[
2\sqrt2\,\sqrt{13/8}\,9^{L-1}Y\sqrt{k/(\lambda n)}
=\sqrt{13}\,9^{L-1}Y\sqrt{k/(\lambda n)}
\le4\,9^{L-1}Y\sqrt{\frac{mk}{\gamma n}}.
\]
The lower scale is \((a_y/2)\sqrt{k/n}\). This checks both constants
and all hypotheses of candidate (30). No limiting argument or
unquantified failure remainder enters these probability statements.

## 6. Scaling, degeneracies, and the exact matching claim

For a label vector in the \(\gamma\)-eigenspace of \(G\),
\[
a_y^2=\|y\|_2^2/\gamma=mY^2/\gamma.
\]
Thus the lower and upper scales match at
\(Y\sqrt{m(d-m)/(\gamma n)}\), up to absolute constants and the
displayed depth factor \(9^{L-1}\). For general labels only
\(a_y\le Y\sqrt{m/\gamma}\) is automatic; replacing \(a_y\) by the
right side in a lower bound would be invalid. The candidate correctly
keeps this distinction.

If \(d=m\), the perpendicular component is empty and all fitted linear
predictors coincide everywhere. If \(Y=0\), the zero-readout dynamics
are stationary. The positive lower statement explicitly excludes these
degeneracies. At every training input the endpoint difference is zero,
even when \(d>m\).

The endpoint lower bound transfers to the all-time sphere norm by
monotonicity of the supremum. The endpoint upper bound does not, by
itself, upper-bound the all-time trajectory discrepancy; the candidate
does not make that inference. The theorem is a construction within the
general activation class, not a uniform lower theorem for all allowed
activations or data.

The width threshold is explicit but conservative and can be exponential
in \(m\) through \(P_0\). Its independence of \(d-m\) is justified by
the active-event construction, not by ignoring an ambient-dimension
term in a full-dimensional fitting theorem.

## Verdict

The exact conditional law, active-event independence, operator and energy
constants, \(m,d,\gamma,Y\) scaling, and all stated finite-width lower
and two-sided probability inequalities reconstruct successfully.
No substantive mathematical correction is required for the frozen
candidate. This internal PASS does not constitute promotion approval or
a verification of statements beyond the scope listed above.
