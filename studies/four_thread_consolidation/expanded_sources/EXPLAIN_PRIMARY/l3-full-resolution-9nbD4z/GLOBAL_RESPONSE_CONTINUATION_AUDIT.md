# Global response continuation: bounded diagonal terms and the remaining memory term

## Conclusion

The local coefficient bootstrap has not been extended to every finite
feature horizon. A more precise distinction is available: its current
response coefficients and its immediately next-time forward coefficients
cannot blow under the established primal bounds. The arctangent
characteristic also cancels the dangerous current-site curvature exactly.
The unresolved part is the response to earlier times, specifically the
time variation of the earlier-source forward kernel and its derivative.

The calculations below concern the same zero-readout scalar response
system as LOCAL_RESPONSE_BOOTSTRAP_AUDIT.md. They do not change the
network, omit trained blocks, or replace a reused Gaussian action.

## Current response coefficients are bounded without absolute row sums

Use \(a=\pi/2\), \(d_{\ell,k}=\phi'(Z_{\ell,k})\), and
\(\chi=\phi\circ F^{-1}\). All derivatives below hold the deterministic
coefficients fixed, as in the scalar response representation.

Because \(C_k\) and the earlier top backward fields do not depend on
the current source \(\xi_{3,k}\),
\[
 \frac{\partial Z_{3,k}}{\partial\xi_{3,k}}=1,\qquad
 b_{3,kk}=\mathbb E[C_k\phi''(Z_{3,k})].
\]
Thus, on every finite feature horizon \(S\),
\[
 |b_{3,kk}|\le2aS.                                      \tag{1}
\]

Similarly \(Z_{2,k}\) has current-source derivative one, while only
the current \(H_{2,k}\) in \(q_{2,k}\) depends on \(\xi_{2,k}\). Hence
\[
 \frac{\partial q_{2,k}}{\partial\xi_{2,k}}
       =b_{3,kk}d_{2,k},
\]
\[
 b_{2,kk}=
 \mathbb E\!\left[
  \phi''(Z_{2,k})\tau_R(q_{2,k})
  +d_{2,k}^2\tau_R'(q_{2,k})b_{3,kk}
 \right].                                               \tag{2}
\]
The known \(L^2\) bound on \(q_2\) therefore gives
\[
 |b_{2,kk}|\le2\|q_{2,k}\|_2+2aS.                       \tag{3}
\]
The norms in this scalar note are probability-space norms. Equations
(1)--(3) are independent of either absolute row sum \(U_k,V_k\).

The same distinction holds for the immediately next-time forward
coefficient. The bottom update gives exactly
\[
 \frac{\partial H_{1,k+1}}{\partial\zeta_{1,k}}
       =\Delta\chi'(X_{1,k+1}),
\]
so
\[
 \frac{a_{2,k+1,k}}{\Delta}
   =\mathbb E\chi'(X_{1,k+1})
     +\mathbb E[H_{1,k+1}H_{1,k}],
 \qquad
 \frac{|a_{2,k+1,k}|}{\Delta}\le a^2+1.                  \tag{4}
\]
Since \(H_{2,k}\) is independent of the current formal \(\zeta_{2,k}\)
source,
\[
 \frac{\partial H_{2,k+1}}{\partial\zeta_{2,k}}
 =d_{2,k+1}a_{2,k+1,k}d_{2,k}\tau_R'(q_{2,k}).
\]
Consequently
\[
 \frac{|a_{3,k+1,k}|}{\Delta}\le2a^2+1.                 \tag{5}
\]

These formulas prove boundedness of the specified coefficients for
every existing finite program on a finite horizon. They do not bound
the sums of coefficients from all earlier source times.

## The exact own-site characteristic

The following calculation is conditional on a continuum response
kernel with the stated time regularity; this regularity is not being
inferred from the local bootstrap. Suppose
\[
 z(t)=\xi(t)+\int_0^t a_2(t,u)\delta(u)\,du,\qquad
 \delta(t)=\phi'(z(t))q(t),
\]
and suppose differentiation in \(t\) is justified. Put
\[
 \alpha(t)=a_2(t,t),\qquad
 g(t)=\xi'(t)+\int_0^t\partial_ta_2(t,u)\delta(u)\,du.
\]
Then
\[
 z'=\alpha(t)\phi'(z)q+g.                               \tag{6}
\]
The diagonal limit of (4), if the finite programs have the indicated
continuous limit, is
\[
 \alpha(t)=\mathbb E H_1(t)^2+\mathbb E\chi'(X_1(t)).
\]
Thus the positive lower hidden second moment implies
\[
 0<m_{1,*}\le\alpha(t)\le a^2+1.                         \tag{7}
\]

Let \(w\) be a formal source variation of \(z\), with all
deterministic kernels fixed, and write \(\dot q,\dot g\) for the
corresponding variations. The natural tangent
\[
 j=\frac{w}{\phi'(z)}
\]
obeys exactly
\[
 j'=\alpha\,\dot q+\frac{\dot g}{\phi'(z)}
       -\frac{\phi''(z)}{\phi'(z)}g\,j.                  \tag{8}
\]
Indeed differentiating (6) first gives the coefficient
\(\alpha\phi''(z)q\) multiplying \(w\); differentiating
\(1/\phi'(z)\) in \(j\) cancels that term. The coefficient of the
remaining \(g\,j\) has absolute value at most one.

The instantaneous part of the backward response can be written
\[
 q(t)=\zeta(t)+\beta(t)\phi(z(t))
                    +\text{terms from times strictly below }t,
\]
where \(\beta(t)\) is the limiting current \(b_3\) coefficient.
Writing
\[
 \dot q=\beta(t)\phi'(z)^2j+\eta(t)
\]
isolates the direct Gaussian perturbation and the earlier-time
response in \(\eta\). Equation (8) becomes
\[
 j'=
 \left[\alpha\beta\,\phi'(z)^2
       -\frac{\phi''(z)}{\phi'(z)}g\right]j
       +\alpha\eta+\frac{\dot g}{\phi'(z)}.              \tag{9}
\]
The current-site deterministic part satisfies
\[
 |\alpha\beta\,\phi'(z)^2|\le2(a^2+1)aS
\]
by (1) and (7). The unbounded \(q\phi''(z)\) coefficient has
disappeared from this characteristic equation.

For example, if \(g=0\) and \(q\) is prescribed externally, the
equation is explicitly
\[
 F(z(t))=F(z(s))+\int_s^t\alpha(u)q(u)\,du.
\]
The derivative with respect to the starting value \(z(s)\) is
\[
 \frac{\partial z(t)}{\partial z(s)}
       =\frac{\phi'(z(t))}{\phi'(z(s))}
       \le1+z(s)^2.
\]
This illustrates the actual flattening mechanism: an exponential
bound in \(\int |q|\) is unnecessary for the current-site term.

## What still needs a bound

In the trained network, \(g\) in (6) is present. Its random memory
part is
\[
 \int_0^t\partial_ta_2(t,u)\delta(u)\,du,
\]
and, with kernels frozen,
\[
 \dot g(t)=\dot\xi'(t)
        +\int_0^t\partial_ta_2(t,u)\dot\delta(u)\,du.      \tag{10}
\]
Thus (9) has three unresolved contributions:

- the exponential moment needed to average its integrating factor
  \(\exp(\int |g|)\);
- the earlier-time response in \(\eta\);
- the term \(\dot g/\phi'(z)\), which also carries the unbounded
  factor \(1+z^2\).

The existing action and operator bounds control ordinary \(L^2\)
sizes of the physical fields and their appropriate velocities.
They do not give absolute time variation of the response kernel.
For example, a sufficient estimate for the random memory contribution
would involve
\[
 J_S=\int_0^S\int_0^t|\partial_ta_2(t,u)|\,du\,dt.         \tag{11}
\]
If the already available backward-field sub-Gaussian norm were \(K\)
and \(J_S\) were bounded, Minkowski's inequality would give
\[
 \left\|\int_0^S\left|
       \int_0^t\partial_ta_2(t,u)\delta(u)\,du
                       \right|dt\right\|_p
 \le KJ_S\sqrt p,\qquad p\ge2.                          \tag{12}
\]
This would control the associated exponential factor. At present,
however, neither (11) nor the response to (10) is bounded by the
known scalar action or by the bounded current coefficients.

The Gaussian part \(\xi'\), when defined from a mean-square
differentiable forward-feature path, does have Gaussian moment bounds
from that path's \(L^2\) velocity. It is the earlier-source kernel term
in (10)--(12) that remains unresolved.

Therefore the diagonal response terms and the scalar arctangent
characteristic are not the unclosed part of continuation. The
remaining proof must control the response kernel away from its
diagonal, or exploit a signed cancellation of those memory terms.
No such closed global inequality has been obtained in this audit.
