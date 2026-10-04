# Check of the explicit source-to-runtime comparison

2026-10-04. **PASS for the deterministic comparison in §13**, conditional
on the source event, exact selected-metric/source interfaces, and the
separately proved dense and corrected-runtime fitting allowances. The
finite-horizon estimate, all-time extension, natural exponential prefactor,
polynomial-prefactor threshold, and prescribed-prefactor threshold all have
the stated constants. No minimum selected weight or extra sample-count
factor appears.

The principal input was the complete §13 of
`UNBOUNDED_COMPRESSOR_BRIDGE.md`, whole-file SHA-256
`63b0613ca4c028f780e3342fb3ddf21efc739fa9257f903691ee967276f8cc08`.
Its §§1--12 were already read completely and checked at the preceding
half-strip revision. The complete `EXPLICIT_COMPRESSOR_RUNTIME_FITTING.md`
and the complete inherited `STORAGE_QUADRATIC_IMPROVEMENT.md` were already
read for the immediately preceding runtime check; their exact equations,
rather than their verdict labels, are used below. The other source inputs
and required notation/proof instructions remain those recorded in the
source and runtime reports. No new external source or other-agent report
was read.

The certificate does not quantify the stochastic source-event width.
Equations (51) and (53) are additional deterministic thresholds; the
original source thresholds and all stated accuracy restrictions must still
hold. This is an internal component check, not a promotion review.

## 1. Pairing errors, norms, and learned actions

Assume \(\epsilon=n^{-1}\le\min\{1,Y,S\}\). For an actual source vector
of normalized empirical norm at most \(U\), an approximant with coordinate
error at most \(\epsilon\) has empirical norm at most \(U+\epsilon\).
Its restriction has exactly that norm by source isometry. The restricted
error has selected-metric norm at most \(2\epsilon\). Hence the actual
restricted source has norm at most \(U+3\epsilon\). This proves the
candidate's \(H_r=H_{\max}+3\) and
\(D_r=S(\tau+3)\), including the latter's use of \(\epsilon\le S\).

For actual source norms bounded by \(U,V\), comparison of the empirical
pairing with its approximant pairing costs
\(\epsilon(U+V)+\epsilon^2\). On the selected side, the two cross errors
cost at most \(2\epsilon(U+V)+4\epsilon^2\), and the error-error product
costs \(4\epsilon^2\). Adding the two defects proves exactly

\[
3\epsilon(U+V)+9\epsilon^2.
\]

For forward sources this is at most \(P_h\epsilon\). For backward
sources, whose true norms are at most \(S\tau\), it is at most
\(SP_\delta\epsilon\). These estimates also apply to different times,
samples, or queries represented in the same source spaces.

For the initialized action, let \(s\) and \(W_0s\) be an exact paired
approximant. The selected initial operator has norm at most eight, its
input restriction error is at most \(2\epsilon\), and its output
restriction error is at most \(2\epsilon\). Thus the action defect is
\(8(2\epsilon)+2\epsilon=18\epsilon\), in both orientations.
No coordinate approximation error is incorrectly pushed through the
original dense operator in an infinity norm.

The learned forward action integrates a selected backward vector of norm
at most \(D_r\) against a forward pairing defect \(P_h\epsilon\).
The absolute residual activity is at most \(S\), so the additional error
is \(S D_rP_h\epsilon=S^2(\tau+3)P_h\epsilon\).
The reverse action instead integrates a selected forward vector of norm
at most \(H_r\) against the backward pairing defect, giving
\(S^2H_rP_\delta\epsilon\). This verifies \(A_f,A_b\).
The raw reference readout is the integral of true selected forward
features, so its norm is at most \(W_r=SH_r\), and its observation
defect is at most \(O\epsilon=SP_h\epsilon\).

## 2. Forward, effective-readout, and backward errors

Let \(d\) be the sum of the raw parameter distances specified in the
candidate and \(u=\|c_C-c_n\|_2/\sqrt m\). The first selected reference
preactivation equals the corresponding true selected preactivation
exactly, so its error is at most \(d\). For later layers, write the
preactivation difference as compressed operator times lower feature
error, parameter difference times the true selected feature, and the
reference action defect. Their coefficients are
\(9F_{j-1}^h,H_r,A_f\). The selected activation Lipschitz constant is
\(2s\). This proves the complete recurrence (44).

The correction residual entering the effective readout can be bounded
by adding and subtracting the selected true prediction. Its four costs
are the residual discrepancy \(u\), raw readout discrepancy \(H_Cd\),
feature discrepancy \(W_rF(d+\epsilon)\), and observation defect
\(O\epsilon\). Thus its norm is at most
\(u+C_r(d+\epsilon)\). The compressed Gram gap gives the inverse-feature
map norm \(2/\sqrt\lambda\). Adding the raw readout discrepancy yields
the claimed bound

\[
\|\widehat w_C-w_R\|
\le B_w(d+u+\epsilon),\qquad
B_w=1+\frac2{\sqrt\lambda}(1+C_r).
\]

For a changed gate multiplied by the true selected carrier, diagonal
metric comparison gives
\(2tM\) times the preactivation error, where the true coordinate
carrier bound is \(M\ge1\). At the top, the other term is
\(2s\) times the effective-readout difference. At a lower layer, its
carrier difference is bounded by nine times the next response error,
plus \(D_r d\), plus \(A_b\epsilon\). This proves (46) by downward
induction. The single factor \(M\) is pulled outside the whole induction;
it is not multiplied once more at each layer. No bounded activation
value or unproved response-coordinate bound is used.

## 3. Every Gram and velocity coefficient

Put \(E_0=d+u+\epsilon\). First compare compressed pairings with true
selected pairings. The top feature pairing costs
\((H_C+H_r)F E_0\). A response pairing costs
\((D_C+D_r)BM E_0\). A hidden product of response and feature pairings
can be decomposed using the compressed feature pairing and the selected
response pairing. It therefore costs at most

\[
\big[H_C^2(D_C+D_r)BM
 +D_r^2(H_C+H_r)F\big]E_0.
\]

Next compare true selected pairings with true empirical pairings.
The top feature and first-response terms cost \(P_h\epsilon\) and
\(SP_\delta\epsilon\). Each hidden product costs at most

\[
SP_\delta H_r^2\epsilon+S^2\tau^2P_h\epsilon.
\]

Summing over the \(L-1\) hidden matrices and using \(M\ge1\) gives
exactly the displayed \(G\) in (47). Thus each entry of the residual-Gram
difference is at most \(GM E_0\). An \(m\times m\) matrix whose entries
are bounded by \(a\) has operator norm at most \(ma\); division by
\(m\) gives \(\|(K_C-K_n)/m\|\le GM E_0\), with no remaining
sample-count factor.

For velocity subtraction, place the residual discrepancy against the
compressed update direction. The first block costs \(2D_Cu\); each
hidden block costs \(2D_CH_Cu\); the readout costs \(2H_Cu\).
These are exactly \(P_vu\). The remaining true-residual terms cost
\(2BM\rho E_0\) at the first block,
\(2(BMH_C+D_rF)\rho E_0\) at each hidden block, and
\(2F\rho E_0\) at the readout. Using \(M\ge1\) gives exactly
\(Q_vM\rho E_0\). Integration proves the parameter inequality in §13.

The compressed residual equation is its exact actual-residual equation,
even though its hidden update directions are not ordinary gradients.
Subtracting it from the dense residual equation and using
\(K_C/m\succeq\lambda I/4\) gives

\[
D^+u\le-\frac\lambda2u+2GM\rho E_0.
\]

Integrating with damping gives
\(\int u\le(4GM/\lambda)\int\rho E_0\); dropping damping gives
\(u(t)\le2GM\int\rho E_0\). Substitution into the parameter inequality
therefore produces

\[
d(t)+u(t)\le AM\int_0^t\rho(d+u+\epsilon),\qquad
A=4P_vG/\lambda+Q_v+2G.
\]

The integral majorant and Gronwall give
\(d+u+\epsilon\le\epsilon e^{AM\int\rho}\). The allowance
\(\int\rho\le S/2\) is conservative and valid. No assumption
\(\lambda\le1\) is used in this calculation.

Finally, the three output errors are effective-readout discrepancy times
\(H_C\), feature discrepancy times \(W_r\), and \(O\epsilon\).
Their coefficient is precisely
\(C_{\rm out}=H_CB_w+W_rF+O\). Substituting
\(M=1+K_{\rm src}S\sqrt{\ell_n}\) proves (48), including
\(a_0=AS/2\) and \(b_0=AK_{\rm src}S^2/2\).

## 4. All-time tails

For a unit query, the normalized dense parameter-gradient norm is bounded
by \(\sqrt{\mathcal K}\); the same bound holds at every training sample.
Sample Cauchy--Schwarz in the physical flow gives
\(|\dot f_n(v)|\le2\mathcal K\rho\). Its weaker available residual rate
\(\lambda/4\) therefore yields tail
\((8\mathcal K Y/\lambda)e^{-\lambda t/4}\).
The separately checked corrected-runtime tail is
\((2B_fY/\lambda)e^{-\lambda t/2}\).

For \(t\ge T\), the displacement of either trajectory from its value
at \(T\) is at most twice its endpoint tail at \(T\). At
\(T=32\lambda^{-1}\ell_n\), this gives the coefficients
\(16\mathcal K\) and \(4B_f\), with decay factors
\(e^{-8\ell_n}\) and \(e^{-16\ell_n}\). Enlarging the latter factor
to the former proves (49). Both networks continue autonomously; neither
is frozen or supplied a reference endpoint.

## 5. Thresholds (50)--(53) and actual label dependence

Young's inequality gives
\(b_0\sqrt{\ell_n}\le\ell_n/2+b_0^2/2\). Since
\(\ell_n=1+\log n\), the finite-horizon term in (49) is at most

\[
\frac{C_{\rm out}}{\sqrt n}
e^{a_0+b_0^2/2+1/2}.
\]

The tail is at most its displayed coefficient divided by \(\sqrt n\)
for \(n\ge1\). This proves (50).

If \(n\ge N_{\rm det}\) from (51), then
\(\ell_n\ge4a_0\) and \(\ell_n\ge16b_0^2\). Consequently
\(a_0\le\ell_n/4\) and
\(b_0\sqrt{\ell_n}\le\ell_n/4\), proving (52) and its factor
\(\sqrt e\). All coefficients left in (52) are finite sums and products
of activation/depth quantities, the actual \(Y,S\), and reciprocal
powers of \(\sqrt\lambda\). Their sample dependence is through
\(Y\) and \(\lambda=\gamma/m\). The exponential conditioning cost is
retained in the explicit deterministic threshold rather than hidden in
the polynomial prefactor.

For (53), the exponential threshold similarly gives
\(a_0+b_0\sqrt{\ell_n}\le\ell_n/4\). The first term of (49) is then
at most \(e^{1/4}C_{\rm out}n^{-3/4}\). Requiring

\[
n\ge(2e^{1/4}C_{\rm out}/P)^4
\]

makes this at most \(P/(2\sqrt n)\). Put
\(D=Y(16\mathcal K+4B_f)/\lambda\). The other contribution is
\(De^{-8\ell_n}\le Dn^{-8}\); requiring
\(n\ge(2D/P)^{2/15}\) makes it at most \(P/(2\sqrt n)\).
Thus every constant and exponent in (53), including \(2/15\), is valid.

The natural \(C_{\rm out}\) is not proportional to \(Y\): several of
its terms remain positive as \(Y\downarrow0\). The conclusion with
\(P=Y\lambda^{-3/2}\) is nonetheless valid for each fixed \(Y>0\),
because (53) explicitly charges its additional width cost. It is not a
uniform small-label stability estimate and not a sharpness claim. The
condition \(\epsilon\le Y\) and all other source-width conditions remain
in force. At \(Y=0\), the separate exact stationary-zero result applies.

The deterministic comparison is therefore complete with the stated
interfaces. Its explicit width trade does not make the unquantified
stochastic success threshold effective, and it proves no lower bound or
optimality assertion.
