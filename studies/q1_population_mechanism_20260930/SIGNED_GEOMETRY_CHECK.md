# Bounded internal check of the signed-geometry route

Reviewed the complete `SIGNED_GEOMETRY_ROUTE.md` at SHA256
`fd57973e0158207a2abbbd317da923715c7faf8d030580a3b8b3c4b21492d27a`.
This is a same-study post-freeze cross-check using that note and the intrinsic equations already derived in the predictor route. It is not an isolated promotion review. No other study, literature search, or experiment was used.

**Conclusion:** the main startup reinforcement theorem and all its displayed constants are correct. The almost-sure finite-data startup criterion, parity floors, signed-input transformation, and adaptive population counterexample also check. Two introductory/concluding phrases merit the qualifications below; neither changes a displayed theorem.

## 1. Startup coefficients and correlation reinforcement

Use the note's b=E_lambda g_0 and G=E_lambda[g_0g_0^T]/n. At initialization r=-1, w=v=0, and k=h_0. Hence

\[
\dot w_0=2b,\qquad \dot A_0=\dot B_0=\dot h_0=\dot g_0=0.
\]

Writing s_h=1-h_0^2 and s_g=1-g_0^2 gives

\[
\dot d_0=2b\odot s_g,\qquad
\dot\ell_0=2s_h\odot W_0^\top(b\odot s_g).
\]

Differentiating the actual intrinsic A and v equations therefore yields

\[
\ddot A_0=4C_A,\qquad
\ddot v_0(u)=4b\odot s_g(u).
\]

For B=W_0+M and M=E[vk^T]/n, all terms in its second derivative except E[ddot v_0 h_0^T]/n vanish. Thus

\[
\ddot B_0=\ddot M_0=4C_B.
\]

The readout second derivative is

\[
\ddot w_0=-2\mathbb E\left[\frac{2b^\top g_0}{n}g_0\right]
=-4Gb.
\]

These formulas imply exactly the factors 2 in the t^2 terms of A,v,M and the factor -2 in the t^2 term of w in (15). No m factor is missing: it is already contained in the empirical expectation.

The key has both first and second derivative zero: differentiating dot k=(rho/tau)(h-k) uses h_0-k_0=0 and dot h_0-dot k_0=0. Also L'(0)=-4||b||^2/n, so rho'(0)=-2F_0 and tau=1+t-F_0t^2+O(t^3). These parts of (15) check as well.

For a perturbation delta A,delta B of the independent forward coordinates, differentiation of the correlation functional gives

\[
\begin{aligned}
\delta\mathcal F
={}&\frac2n\mathbb E\left[(b\odot s_g)^\top\delta B\,h_0\right]\\
&+\frac2n\mathbb E\left[(s_h\odot W_0^\top(b\odot s_g))^\top
\delta A\,u/\sqrt d\right].
\end{aligned}
\]

Consequently

\[
\nabla_A\mathcal F=2C_A/n,\qquad
\nabla_B\mathcal F=2C_B,
\]

which verifies (17) and (18). Since dot A_0=dot B_0=0, the Hessian term in the second derivative of the composed functional vanishes at zero. The remaining term is

\[
\frac{d^2}{dt^2}\mathcal F(A_t,B_t)\bigg|_{t=0}
=\frac8n\|C_A\|_F^2+8\|C_B\|_F^2.
\]

Its Taylor coefficient is one half this value, giving precisely

\[
\mathcal F(A_t,B_t)
=F_0+4t^2\left(\|C_A\|_F^2/n+\|C_B\|_F^2\right)+O(t^3).
\]

Thus there is no factor-of-two discrepancy in (19). This calculation retains the actual mixer and actual q1 memory update; it does not assume an independent gradient descent equation for B.

The remainders can be uniform over the sphere at each fixed initialization: the sphere is compact, the population measure has total mass one, local state variables remain bounded, and rho starts at one. The square root is smooth in this local neighborhood, while tanh and the integral operations have the required bounded local derivatives. For a population law, the fields can be placed in C(S^{d-1};R^n) with the supremum norm; the same local differentiability argument applies. The output expansion (20) follows because g_t-g_0=O(t^2) multiplies w_t=O(t).

**Wording qualification:** the introduction says that the presence of the startup signal makes representations move in directions that increase correlation. The precise proved statement is that their leading accelerations are positively scaled gradients and the quadratic coefficient is nonnegative. Strict quadratic reinforcement needs C_A or C_B nonzero, exactly as stated after (19). The note does not prove that b nonzero alone implies that additional condition. The introduction should retain this qualification when summarized.

## 2. Almost-sure startup gate

Proposition 2 is correct. Necessity follows from dot w_0=2b, and b=0 makes the displayed arrested learning trajectory solve every equation. The finite-dimensional vector field is locally Lipschitz for tau>0. For a population law, the same claim is valid after specifying continuous k,v fields with the supremum norm on the compact sphere: expectations are bounded operators and the residual norm is Lipschitz by the reverse triangle inequality. Thus no uniqueness assumption is missing in the stated setting.

Proposition 3 correctly fixes the finite empirical law before the Gaussian draw. The proof's exceptional hyperplanes are proper: different unoriented pairs have representatives u_j not equal to plus or minus u_k, so neither u_j-u_k nor u_j+u_k vanishes. Avoiding their orthogonal hyperplanes makes the projection squares distinct, and avoiding u_j's orthogonal hyperplane makes each projection nonzero.

The tanh Taylor recurrence is correct and makes every a_k positive. If the signed ridge average vanished identically, its first J odd coefficients, for J antipodal pairs, would give a Vandermonde system with unknowns c_j t_j. Distinct t_j^2 and nonzero t_j force every c_j=0, contradicting nonsymmetry.

The second layer does not invalidate this witness: placing the nonzero ridge in one row of A and taking only W_11=s gives b_1=s times the nonzero ridge mean plus O(s^3). Therefore b_1 is a nonzero real analytic function on the full connected parameter space. The zero-set theorem used in the note applies to a nonidentically-zero real analytic function on such a domain; finite support ensures analyticity without any parameter-dependent integration difficulty. The Gaussian law has a full density for each n>=1, so its zero set has probability zero. The conclusion is qualitative startup, not a lower bound on the signal or eventual fitting.

The adaptive population example is also valid. There are n homogeneous linear constraints on an n+1 dimensional space of odd trigonometric functions. A nonzero solution can be normalized in supremum norm. The resulting density is positive, integrates to one, is not antipodally symmetric, and has zero integral against every initial feature. Its law depends on the already realized features.

**Wording qualification:** the final phrase describing this as a counterexample to a “uniform initialization-independent onset guarantee” is potentially ambiguous. It refutes an onset assertion uniform over all laws for each realized initialization. It does not refute an almost-sure assertion for each population law fixed independently of initialization. The construction, Proposition 3, and the table otherwise maintain this quantifier distinction correctly.

## 3. Signed inputs and parity floors

The label gauge is exact, including memory and clock. With u=yx, transformed residual yr, transformed keys yk, and transformed values yv, oddness gives h(u)=yh(x), g(u)=yg(x), while d and ell are unchanged. Each force and the product vk^T are preserved. Coincident signed inputs also have identical transformed initial keys and values and identical field equations, so collapsing their masses creates no ambiguity.

The measure decomposition and Radon–Nikodym target are correct. Relative to lambda_e, the measures lambda and its antipodal reflection have densities 1+eta and 1-eta. Hence |eta|<=1 and eta is odd almost everywhere. For odd f,

\[
\int f^2\,d\lambda=\int f^2\,d\lambda_e,
\qquad
\int f\,d\lambda=\int f\eta\,d\lambda_e,
\]

which proves the exact square completion and loss floor. Choosing an odd representative of eta attains the optimum in the unrestricted measurable class. The zero-loss condition |eta|=1 is equivalent to disjoint supports modulo lambda_e-null sets of the two nonnegative densities 1+eta and 1-eta, precisely mutual singularity of the two measures.

The classification floor uses the explicit half-error convention at zero and is correct. For s=sgn f,

\[
\operatorname{Err}=\frac12\left(1-\int s\eta\,d\lambda_e\right),
\]

and the best unrestricted odd decision is s=sgn eta. The pairwise squared-loss constant 4ab/(a+b) and error mass min(a,b) are consistent with both general floors. The note correctly distinguishes these unrestricted odd optima from finite-width representability and actual q1 convergence.

## 4. Remaining circle claims

Oddness, the exclusion of even Fourier modes, and the antipodal zero constraint are correct. The density formula (22) is the appropriate Radon–Nikodym ratio wherever its denominator is positive. The stated even-label and odd-label examples under uniform input have respectively symmetric signed law and antipodally disjoint signed law; their floors and the universal arrest of the even-label case follow.

The claim that nonlinear outputs can contain arbitrarily high odd harmonics is consistent with the architecture. Already a one-neuron circle output tanh(tanh(a cos theta)), with a nonzero, has no finite Fourier truncation: an even trigonometric polynomial in theta would be a polynomial in cos theta, whereas this nonconstant analytic bounded function of cos theta cannot coincide with a polynomial on an interval and remain bounded on the whole real line. This harmonic fact does not itself establish complex decision boundaries for one neuron, and the note does not claim that it does.

No theorem in the note proves global correlation ascent, general fitting on parity-compatible data, minimum norm, maximum margin, or a canonical terminal classifier. Its final limitations state that accurately.
