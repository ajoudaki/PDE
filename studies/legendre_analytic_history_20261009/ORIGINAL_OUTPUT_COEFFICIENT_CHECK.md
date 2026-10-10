# Independent check of the original Legendre output counterexample

Date: 2026-10-09.

## Verdict and scope

**PASS.** The scaled equations, defect normalization, fifth-order prediction coefficient, uniform remainder estimate, and resulting \(q^{-10}\) lower bound are correct. The readout feedback reinforces the direct hidden-matrix contribution; omitting it would give the wrong coefficient.

The candidate proves that the unchanged residual-clock, constant-prefix Legendre method cannot achieve the paper's displayed absolute accuracy with any order \(q=n^{o(1)}\), including fixed powers of \(\log n\), uniformly over the allowed problems. Its caution that a dense-variability **lower** bound cannot establish failure of the relative criterion is correct. Using the additionally permitted dense-variability **upper** bound from `integrated_appendix.tex` does establish that failure for this example; the ratio grows without bound in probability, with a zero denominator treated as failure under the paper's convention.

This bounded check uses the complete candidate, the original setup and Legendre/fitting equations in the permitted compact paper files, and only the authorized dense-upper statement and proof passage in the integrated appendix. The relevant paper context and required mathematical-presentation skills were reused from this reviewer's existing context; this is not a claim of fresh-context isolation. No other study note or reviewer report was used. No candidate or paper file was changed.

## Source hashes

| Input | SHA256 |
|---|---|
| `studies/legendre_analytic_history_20261009/ORIGINAL_OUTPUT_ANALYSIS.md` | `6bf9c51316b5425eb0cb9288a0859b24e6f08d5adcf6155e21bf2dbfad967320` |
| `paper/compact.tex` | `47199d5c9e374b80b9eafefd60699c2f4bfe06dde00ebd0a1c53e2805598a0c4` |
| `paper/compact_legendre.tex` | `862aa37139ad9af67ac04b52949f838031e91077021b2da9060244d36ab4e0f9` |
| `paper/compact_fitting.tex` | `6efe077759c846c4b3d79f999c37d2d1478bae549d49fc9666837efbf9f1a01f` |
| `paper/integrated_appendix.tex` | `24067e29771847f4e182c63a7a43e9cffa9d2fef8518239d7553145dffa4e65a` |

The integrated appendix was consulted only at the authorized dense-upper statement, lines 222--245, and proof passage, lines 9079--9730. The dense upper bound remains an imported paper result; this check does not re-certify its probabilistic source theorem. The counterexample's coefficient and remainder argument do not require that upper bound or any dense complex-source theorem.

## Admissibility and normalization

The example takes \(L=m=d=2\), \(v_1=e_1\), \(v_2=e_2\), and identity activations. The actual inputs are \(x_a=\sqrt2e_a\), so they have the required norm \(\sqrt d\). Identity activations are real and holomorphic with bounded first derivative on every fixed strip, and are allowed by the paper's assumptions. The population covariance recursion preserves \(I_2\), hence \(\gamma=1\), \(\lambda=\gamma/m=1/2\), and any sufficiently small fixed nonzero label vector meets the label cap. No strict nonlinearity hypothesis excludes this example.

With

\[
A=W^{(1)}/\sqrt n,\quad B=W^{(2)},\quad c=w/\sqrt n,
\]

the two training outputs are \(f=A^\top B^\top c\), the residual is \(r=f-y\), and \(\rho=\|r\|_2/\sqrt2\). The canonical factors \(2/m=1\) give exactly

\[
\dot A=-B^\top cr^\top,\qquad
\dot B=-c(Ar)^\top,\qquad
\dot c=-BAr.
\]

For the original Legendre model, each physical forward history column is \(\sqrt n A_a\), and each physical backward history column is \(\sqrt n c r_a/\rho\). The paper's hidden defect is \(2\rho/(mn)\) times the sum of their endpoint-error outer products. Dividing each history by \(\sqrt n\) therefore gives

\[
\mathcal E=(2\rho/m)e_be_h^\top=\rho e_be_h^\top,
\]

with the positive sign in candidate (3). The prefix is exactly \(h=A_0\), \(b=0\) on \([0,1]\), and the clock is the unchanged \(\tau=1+\int\rho\). This check is of the original method, not a different time parametrization or initialization.

The initialized Gram is \(G=A_0^\top B_0^\top B_0A_0\). The paper's initialization event says \(G/m\succeq\gamma I/(2m)\), which here is exactly \(G\succeq I_2/2\). Its operator bounds and the original Legendre construction's order-independent physical bounds are sufficient for the candidate. They give constants uniform in width, initialization within the event, and finite order. In particular \(\|A\|_F\le\sqrt2\|A\|_{\mathrm{op}}\); no width-growing bound on \(\|B_0\|_F\) is used.

## Uniform endpoint and forcing expansion

The endpoint projection kernel satisfies \(|K_q^T(T,\xi)|\le q^2/T\), because \(|P_j|\le1\) and \(\sum_{j<q}(2j+1)=q^2\). For a history zero on the prefix, changing from clock time to physical time gives

\[
\|(\Pi_q^{\tau(t)}g)(\tau(t))\|
\le q^2\int_0^t\rho(s)\|g(\tau(s))\|ds.
\]

The use of \(1/\tau\le1\) is valid, and there is no inverse residual factor. For the forward history, subtracting \(A_0\) makes the prefix zero and leaves the projection error unchanged.

The physical bounds first imply \(c=O(t)\), \(A-A_0=O(t^2)\), and \(b=O(t)\). Therefore

\[
e_b=O(t+q^2t^2),\qquad e_h=O(t^2+q^2t^3).
\]

On \(t\le\min(1,q^{-2})\), this gives \(\mathcal E=O(t^3)\) and \(B-B_0=O(t^2)\), with constants independent of width and order. Since \(f=O(t)\), choose a fixed \(t_*>0\) so that \(\rho\ge Y/2\) through \(t_*\). It can be chosen uniformly on the stated event because \(Y>0\) is fixed and all physical bounds are uniform.

Put \(u=B_0A_0y\). On \(0\le t\le\min(t_*,q^{-2})\), ordinary product subtraction yields

\[
c=ut+O(t^2),\quad
A=A_0+\tfrac12B_0^\top uy^\top t^2+O(t^3),\quad
b=-uy^\top t/Y+O(t^2).
\]

These remainder constants remain order-independent. Applying the endpoint bound once more gives

\[
e_b=-uy^\top t/Y+O(q^2t^2),\qquad
e_h=\tfrac12B_0^\top uy^\top t^2+O(q^2t^3).
\]

Thus

\[
\mathcal E=E_3t^3+O(q^2t^4),\qquad
E_3=-\tfrac12\|y\|_2^2uu^\top B_0.
\]

The sign is negative: the leading backward history is \(-uy^\top t/Y\), while the leading changed forward history is \(+B_0^\top uy^\top t^2/2\). The product of the remainder terms is \(O(q^4t^5)\), which is at most \(O(q^2t^4)\) because \(q^2t\le1\). This is the key uniform-in-order remainder estimate; the proof does not use an uncontrolled fixed-order Taylor remainder.

## Fifth-order prediction coefficient, including readout feedback

Use \(\Delta\) for Legendre minus dense quantities. Product subtraction in the scaled physical equations is Lipschitz with a constant independent of width, using Frobenius norms for \(A\) and parameter differences, Euclidean norm for \(c\), and operator bounds for full mixers. The forcing bound gives

\[
\|\Delta A\|_F+\|\Delta B\|_F+\|\Delta c\|_2=O(t^4)
\]

by Gronwall on the fixed short interval. The sharper order sequence in the candidate is sound:

\[
\Delta c=O(t^5),\quad
\Delta f=\Delta r=O(t^5),\quad
\Delta A=O(t^6),\quad
\Delta\dot B-\mathcal E=O(t^5).
\]

For example, the output subtraction has the extra readout factor \(O(t)\) on \(\Delta A\) and \(\Delta B\), so the first bound on \(\Delta c\) indeed implies \(\Delta f=O(t^5)\). The first-layer equation then gives \(\Delta\dot A=O(t^5)\). There is no circular order improvement.

Integration of the forcing expansion gives

\[
\Delta B=\tfrac14E_3t^4+O(q^2t^5).
\]

The exact readout difference is

\[
\Delta\dot c=-\Delta B\,\widehat A\widehat r
-B_D\Delta A\widehat r-B_DA_D\Delta r.
\]

Since \(\widehat A\widehat r=-A_0y+O(t)\), its leading term is \(+E_3A_0y\,t^4/4\). Therefore

\[
\Delta c=\tfrac1{20}E_3A_0y\,t^5+O(q^2t^6).
\]

For the prediction, \(\Delta A^\top\widehat B^\top\widehat c=O(t^7)\). The remaining terms produce

\[
\Delta f=
\left(\tfrac14A_0^\top E_3^\top u
+\tfrac1{20}A_0^\top B_0^\top E_3A_0y\right)t^5
+O(q^2t^6).
\]

Let \(S=\|y\|_2^2(y^\top Gy)\). Since \(\|u\|_2^2=y^\top Gy\) and \(A_0^\top B_0^\top u=Gy\), the two coefficients are

\[
\underbrace{-\tfrac18 S Gy}_{\text{direct hidden-matrix effect}},
\qquad
\underbrace{-\tfrac1{40}S Gy}_{\text{readout feedback}}.
\]

They sum to \(-3S Gy/20\), verifying candidate (14), including its sign. Multiplication by \(5!=120\) gives the stated fifth derivative \(-18\|y\|_2^2(y^\top Gy)Gy\). For each fixed finite order the original ODE is smooth near the initial state, since \(\tau(0)=1\) and \(\rho(0)=Y>0\), so the derivative interpretation is legitimate.

Every omitted term is bounded by \(Cq^2t^6\) on the stipulated interval: the direct hidden-matrix remainder gains the factor \(c=O(t)\), the readout remainder is already of that order, and the first-layer/output coefficient corrections have order at least seven. All constants depend only on the fixed labels and the uniform physical bounds, not on width or order.

## Lower bound and its asymptotic consequences

The initialized Gram gap gives

\[
\left\|\tfrac3{20}\|y\|_2^2(y^\top Gy)Gy\right\|_2
\ge\tfrac3{80}\|y\|_2^5=:a_y>0.
\]

Choose a positive uniform \(\eta\le\min(t_*,1,a_y/(2C))\), taking the remainder constant \(C>0\). At \(t_q=\eta/q^2\), the leading term is at least \(a_y\eta^5q^{-10}\), and the remainder is at most \(C\eta^6q^{-10}\). Hence

\[
\|\Delta f(t_q)\|_2\ge\tfrac12a_y\eta^5q^{-10}.
\]

The maximum training error is at least this norm divided by \(\sqrt2\). Because these networks are linear in the unit normalized input \(v\), the whole-sphere supremum at that time equals the Euclidean norm of the two training-output differences. The witnessing time is positive and is part of the all-time supremum even when it tends to zero as the order grows.

The event and constants are common to every finite order. In particular, the conclusion applies to width-dependent orders; it does not exchange a fixed-order asymptotic expansion with an increasing-order limit. Comparison with the target \(CY/(\sqrt n[\log(en)]^3)\) gives exactly the necessary condition

\[
q\ge c_{\mathrm{problem}}n^{1/20}[\log(en)]^{3/10}.
\]

Thus \(q=n^{o(1)}\) cannot meet that target in the original construction on this admissible fixed problem. The exponent \(1/20\) is only a necessary lower bound and does not show sharpness of either the obstruction or the paper's sufficient \(1/4\) exponent.

## Additional permitted conclusion for actual dense variability

The candidate correctly leaves this step open without an upper bound. The additionally authorized current-paper upper envelope is

\[
\|f_n-\widetilde f_n\|_*
\le C\beta^{CL}Y(1+m/\gamma)^5
\sqrt{d/n}\,\log(en)e^{\sqrt{\log(en)}}
\]

eventually at each fixed confidence, with the exact confidence dependence handled by the cited certificate. Its authorized proof passage identifies the complete-time, whole-sphere norm and obtains probability \(1-\delta\) by Gaussian extension, a compactified-time/sphere net, and fitting/source events. This matches the numerator's query and time domain. In the present fixed problem the bound is \(C_{\delta,\mathrm{problem}}n^{-1/2}\log(en)e^{\sqrt{\log(en)}}=n^{-1/2+o(1)}\).

On the intersection of that upper event with the counterexample event, the ratio, whenever its denominator is positive, is at least

\[
\frac{c_{\mathrm{problem}}\sqrt n}
{C_{\delta,\mathrm{problem}}q^{10}\log(en)e^{\sqrt{\log(en)}}}.
\]

For every deterministic \(q(n)=n^{o(1)}\), this tends to infinity. The counterexample event has probability tending to one, and the dense upper event can have any fixed confidence \(1-\delta\). Taking arbitrarily small fixed \(\delta\) proves divergence in probability under the natural infinite-ratio convention at zero denominator; under the paper's stated convention such a zero denominator already counts as failure. No independence between these two events is needed.

Therefore, with this expressly imported upper certificate, the example rules out the original relative-error criterion as well as the displayed absolute target for all subpolynomial orders. It does not imply failure at fixed practical tolerances, for vanishing labels, or on a time domain that excludes the shrinking initial interval. No mathematical correction to the candidate is required.

## Subsequently authorized corollary scope check

After the coefficient check was complete, the supervisor explicitly authorized a brief check of `ORIGINAL_METHOD_RESULT.md`, SHA256 `1474b20463f8c21351bfe030fdbe3b3f44739170adabb5586b78ef93bb637c1b`. Its complete corollary was read. The comparison using \(C_\delta\log(en)\exp(C_\delta\sqrt{\log(en)})/\sqrt n\) is valid: for each fixed \(\delta\), the lower ratio tends to infinity for \(q=n^{o(1)}\), so the probability of comparison within any fixed factor has limiting superior at most \(\delta\), and then tends to zero. No interchange of a growing confidence parameter with width is required.

The relative-comparison necessary order \(n^{1/20-o(1)}\) and the exact learned-state count \(3n+1+4nq\) follow. Its endpoint observation is also correct: both fitted predictors are linear in the normalized input and take values \(y_1,y_2\) at the basis vectors, so both equal \(y^\top v\) on the whole sphere. The verified obstruction is entirely transient. The report correctly distinguishes the unchanged method from modified methods and does not claim a proved tanh counterexample; its separate nonlinear coefficient calculation was outside this check and was not consulted. No mathematical scope correction is needed.
