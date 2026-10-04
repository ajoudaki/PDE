# Check of the numerical same-width Legendre comparison

2026-10-04. **PASS for the numerical deterministic transfer, degree choice,
and moving-coordinate count in the revised source.** The checked conclusion
is a same-initialization, same-width comparison in the original physical
time, uniformly on the input sphere and including the fitted endpoint.
The final error coefficient is one. The source-event width threshold is
eventual, and fixed initialized mixers remain quadratic in width.

This is a bounded algebra and interface check, not a new source-probability
proof or an independent promotion review. The numerical carrier maximum is
the supplied source interface; its scientific status is inherited from
that component. No sensitivity or trained-moment assumption is introduced.

## 1. Inputs and claim level

The complete principal input is `EXPLICIT_LEGENDRE_COMPARISON.md`, revised
SHA-256
`7834b325b31aa667d9c751a2c180439399433d82d77cdd078b38ea54e0168a1c`.
The other reads in this check were precisely:

- Section 6 of `GENERAL_LEGENDRE_TRANSFER.md`, file SHA-256
  `a5db32caeb53cc375b8448b9f65f192d05be80fc314e8927d0fa93f0b3207820`.
- Complete `GENERAL_EXPLICIT_CLOSURE_FITTING.md`, SHA-256
  `2247f0d4b189b8d38f1c996db3438a55d562ca6b0e6c82c8ae71b3110e708cbd`.
- Complete `GENERAL_EXPLICIT_CLOSURE_FITTING_CHECK.md`, SHA-256
  `f646306951521f0ea63f22d3a0d84324e3d134704492bd8cb338bc82c82500a9`.

The previously read dense fitting theorem and explicit source maximum
were used only for their already specified interfaces. No additional
study, manuscript passage, or probabilistic source was fetched. The
canonical-notation and rigorous-math instructions remain in force.

Let \(L\ge2\) be fixed, all hidden widths be \(n\), and the finite
training data have \(\|x_a\|=\sqrt d\). Let
\(Y=\|y\|_2/\sqrt m\), \(\gamma=\lambda_{\min}(Q_L)>0\),
and \(\lambda=\gamma/m\). Activations have the stipulated strip
extension and bounded first derivative; their values need not be bounded.
The dense network and original residual-RMS-clock Legendre closure use
the same Gaussian initialization and zero initial readout. The three
explicit label caps in the principal input are retained separately.

The common constants \(\kappa=\lambda/4\) and
\(R=8Y/\sqrt\lambda\) dominate both fitting interfaces: dense
decay is faster, its readout bound is smaller, and the closure has the
stated decay and readout bound \(R/2\). Both full mean tangent Grams
dominate a readout Gram of gap \(\lambda/4\), which is stronger
than the transfer's required gap \(\kappa/2\). Both have whole-sphere
feature RMS at most \(2H\) and matrix caps nine. The closure outputs
\(V_h\) and \(C_c\) in its equations (18)--(19) give exactly the
two additional transfer inputs. There is no unverified trajectory
condition left in this deterministic matching.

The source supplies, eventually with probability tending to one,
\[
 M=2K_{\rm src}(16Y/\lambda)\sqrt{\log(en)}
\]
as a dense training-carrier maximum through all physical time. Only
training carriers are used; a maximum over passive query carriers is not
needed. The factor two accommodates the deterministic post-horizon tail.

## 2. Parameter and residual comparison constants

Use the constants \(F_z,B,P,G,B_d,J\) of the principal input and let
\(d(t)\) be the sum of the first-weight normalized Frobenius discrepancy,
hidden Frobenius discrepancies, and readout RMS discrepancy. Let
\(D_T=\sup_{t\le T}d(t)\), and let
\(\varepsilon_T=\int_0^T\sum_{\ell=2}^L\|E_\ell(t)\|_F\,dt\)
be the integrated absolute reconstruction defect.

Forward subtraction costs \(F_zd\) in preactivation RMS. Backward
subtraction pairs its changed gate with the actual dense carrier, costing
\(t_2MF_zd\); the other terms are a changed readout or a changed hidden
matrix. Downward induction bounds every training-response discrepancy by
\(B_dd\). In normalized physical parameters the sample gradient has
sum of block norms at most \(G\), and its difference has sum at most
\(Jd\). Hence the mean tangent-Gram difference has operator norm at
most \(2GJd\). The defect's residual forcing has sample RMS at most
\(2HB\sum_\ell\|E_\ell\|_F\).

Solving the damped residual-difference equation and integrating gives
\[
 \int_0^T\|\widehat r-r\|_2/\sqrt m\,dt
 \le {4GJ\over\kappa}\int_0^T\rho_Dd\,dt
                              +{2HB\over\kappa}\varepsilon_T.
\]
Parameter subtraction has coefficient \(2G\) on this integral,
coefficient \(2J\) on \(\int\rho_Dd\), and direct defect
\(\varepsilon_T\). As \(\int\rho_D\le Y/\kappa\), Gronwall
therefore gives exactly
\[
 D_T\le\mathcal A\varepsilon_T,\qquad
 \mathcal A=\left(1+{4GHB\over\kappa}\right)
  \exp\left\{2J(1+4G^2/\kappa)Y/\kappa\right\}.
\]
There is no missing mean-loss factor or additional factor of \(m\).
The finite-horizon form makes subsequent absorption legitimate before
passing to infinity.

The dense hidden-block speed sum is at most \(2BP\rho_D\), so
\(V_z=2F_zBP\) is valid. The dense response derivative consists of
the readout speed, \(L-1\) changed matrix terms, and \(L\) changed
gates. Their respective bounds are
\(4sH\rho_D\), \(4sHB^2\rho_D\), and
\(t_2MV_z\rho_D\), propagated by at most \((9s)^{L-1}\).
This verifies the displayed \(V_\delta\).

## 3. Projection, freezing, and absorption

Write \(a_0=Y/\kappa\). The closure clock starts at one and ends
at most at \(1+a_0\). Its forward clock derivative has RMS at most
\(V_h\), and its unit prefix is constant. For any clock endpoint
\(A\le1+a_0\),
\[
 \int_1^A\xi(A-\xi)\,d\xi\le A(A-1)^2/2.
\]
The weighted Legendre inequality therefore gives the forward projection
error \(F_h/q\), with
\(F_h=V_ha_0\sqrt{(1+a_0)/2}\), exactly as claimed.

Record the dense response in this closure clock as
\(\widetilde b_a(t)=\widehat c_a(t)\delta_{D,a}(t)\), with zero
prefix. The initial readout is zero, so this history is continuous at
the end of the prefix. Its physical derivative in sample-averaged RMS
is at most \(C_cB+V_\delta\rho_D\). In the weighted derivative
energy, the bound
\(A-\widehat\tau(t)\le\widehat\rho(t)/\kappa\)
cancels the inverse closure clock speed. Before freezing at physical
time \(u\), that energy is bounded by
\[
 {1+a_0\over\kappa}
       \int_0^u(C_cB+V_\delta\rho_D)^2\,dt
 \le {1+a_0\over\kappa}
       \left[2C_c^2B^2u+V_\delta^2Y^2/\kappa\right].
\]
Here \(\int\rho_D^2\le Y^2/(2\kappa)\) is conservative for
the faster dense decay. With \(u=2\log q/\kappa\), square roots
give precisely the \(b_1\sqrt{\log q}\) and the first term of
\(b_0\). The frozen history differs from the original only on a
clock interval of length at most \(a_0e^{-\kappa u}\), and both
histories have sample RMS at most \(B\). Its error is thus at most
\(2B\sqrt{a_0}/q\), supplying the other term in \(b_0\).

The difference between the closure backward history and this dense
history has clock \(L^2\) norm at most
\(B_d\sqrt{a_0}D_T\). This uses
\(m^{-1}\sum_a\widehat c_a^2=1\); it incurs no \(\sqrt m\)
loss. Projection contraction therefore gives the total backward error
\[
 {b_0+b_1\sqrt{\log q}\over q}+B_d\sqrt{a_0}D_T.
\]
The growing projection-error identity converts the time integral of
squared endpoint errors into the final projection error. Applying
Cauchy--Schwarz in clock time and sample average to the exact defect
therefore gives
\[
 \varepsilon_T\le2(L-1)F_h
 \left[{b_0+b_1\sqrt{\log q}\over q^2}
                          +{B_d\sqrt{a_0}D_T\over q}\right].
\]
For \(q\ge4(L-1)F_hB_d\sqrt{a_0}\mathcal A\), the last term
is absorbed with factor at most one half. Passing to infinite time then
gives the principal input's equation (5). Prediction subtraction costs
at most \(C_fD_T\), with \(C_f=2H+RsF_z\), because both physical
tubes already have the sharper whole-sphere feature bound \(2H\).

This comparison evaluates both networks at the same physical time.
The closure clock is used inside the projection proof only. Both fitting
theorems give physical parameter limits, so taking time to infinity
preserves the sphere bound and includes the fitted endpoint.

## 4. Explicit order inversion and state count

For \(Y>0\), let \(C_n,Q_n,q_n\) have exactly the definitions in
equation (6) of the principal input. Since \(q\ge1\),
\[
 b_0+b_1\sqrt{\log q}
 \le(b_0+b_1)\sqrt{\log(eq)}.
\]
Thus equation (5) is bounded by
\(C_n\sqrt{\log(eq)}/q^2\).
Put \(l=\log(e+Q_n)\). Since \(Q_n\ge3\), the ceiling obeys
\[
 4Q_n\sqrt l\le q_n\le5Q_n\sqrt l,
 \qquad \log(eq_n)\le4l.
\]
For the latter inequality, one elementary verification is
\(l\le Q_n\) and \(5e\le Q_n^{5/2}\) for \(Q_n\ge3\):
then \(eq_n\le5eQ_n^{3/2}\le Q_n^4\le(e+Q_n)^4\).
Consequently
\[
 {C_n\sqrt{\log(eq_n)}\over q_n^2}
 \le {C_n\over8Q_n^2\sqrt l}
 \le {Y\over8\sqrt n\sqrt l}
 \le {Y\over\sqrt n}.
\]
The definition of \(Q_n\) also ensures the absorption condition.
The coefficient one is therefore a verified width-independent error
coefficient, without an unspecified multiplicative constant.

At fixed nonzero labels and fixed remaining problem parameters,
\(M=O(\sqrt{\log n})\), \(\log\mathcal A=O(\sqrt{\log n})\),
and all other width dependence is polynomial in \(\sqrt{\log n}\).
Hence \(q_{\rm abs}=n^{o(1)}\), \(C_n=n^{o(1)}\), and
\[
 q_n=n^{1/4+o(1)}.
\]
The lower asymptotic order also follows because \(C_n\) is bounded
below by a fixed positive constant at fixed \(Y>0\). The persistent
moving coordinates are the first block, readout, one scalar clock, and
two moment families for each training sample and hidden interface:
\[
 S_{\rm moving}=n(d+1)+1+2(L-1)mnq_n=n^{5/4+o(1)}.
\]
Thus \(n^{1/4+o(1)}\) is the mode order; the moving-coordinate count
is \(n^{5/4+o(1)}\). The \((L-1)n^2\) initialized fixed mixers
are additional retained storage. No subquadratic total-storage statement
follows. For \(Y=0\), the stationary zero predictor is handled directly.

## 5. Probability and corrected wording

The initialization event controls all closure orders deterministically,
and the only additional stochastic event is the actual dense carrier
event. Their intersection is common to every positive integer \(q\)
at a fixed width. Thus no order union or comparison of different
physical clocks is required. At confidence \(1-\delta\), allocate
\(\delta/2\) to initialization and \(\delta/2\) to the eventual
source event. The former width is explicit; the latter remains
unquantified by its inherited proof. The result concerns every sufficiently
large individual width, not one event over infinitely many independent
widths.

The first version's final sentence described all coefficients as width
independent, despite the explicit \(M\) and \(\mathcal A\) in its
fixed-order estimate. The author corrected this during the check. The
revised version identified by the hash above now states the distinction
correctly: the intermediate fixed-order coefficient depends on width,
whereas the final error coefficient one does not. No unresolved algebra
or interface defect was found in the scoped conclusion.
