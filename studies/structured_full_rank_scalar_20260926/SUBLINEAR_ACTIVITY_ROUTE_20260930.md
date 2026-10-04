# Finite activity, passive memory, and sublinear aggregate complexity

Scoped independent theoretical route, 2026-09-30. Internal result; no experiments or promotion. Inputs were the supervisor's contract and Sections 1–3 of `AGGREGATE_SCALAR_CONSTRUCTION.md`, together with the required research and proof skills. The historical histogram construction is not used as an admissible approximation.

**Conclusion.** Finite activity and terminal stability control propagation of an already small approximation error. They do not produce that error bound, determine the selected test function, or establish sublinear complexity. There is, however, an elementary constructive result for a particular additional mechanism: a positive mixture of relaxation kernels with bounded spectral mass admits a passive finite ODE approximation using

\[
q=O\bigl(\eta^{-1}\log(1/\eta)\bigr)
\]

memory modes on bounded activity, with constants independent of sampled width. At an error target proportional to \(n^{-1/2}\), this conditional construction uses \(O(\sqrt n\log n)\) modes. The missing P1 implication is substantive: no derivation below identifies its unresolved memory with such a kernel or gives computable coefficients for that kernel. P1's exact memory contribution is not manifestly positive or symmetric.

## 1. Contract and claim levels

The target is the P1 neural response-memory population with changing first and second features, canonical outer-weight motion, and

\[
W=W_0-\frac{2AB^\top}{mnL},\qquad
\dot A_a=r_a\delta_{2,a},\qquad
\dot B_a=\rho h_{1,a},\qquad \dot L=\rho,
\]

where \(r_a=f(u_a)-y_a\), \(\rho^2=m^{-1}\sum_a r_a^2\), \(L(0)=1\), \(A(0)=0\), and \(B_a(0)=h_{1,a}(0)\). The equivalent block-expectation notation is permitted. The desired approximation retains finitely many ordinary scalar aggregate coordinates, admits restart from its current state, and obtains coefficients from the prescribed model, initialization and training data. It may not retain a density, histogram, population particles, fixed initial feature dictionary, trajectory playback, or a full moment basis disguised as compression.

Output accuracy, training-loss accuracy and terminal test-function accuracy are separate requirements. A finite ODE whose state dimension is independent of \(n\) is not sufficient: its state, coefficient storage, construction cost and evaluation cost must be compared with the sampled reference at the same error target. The construction below permits one initial pass over a finite sample if an empirical initializer is used; it does not claim that reading \(n\) initialization records costs \(o(n)\).

The proved statements here are exact identities, conditional approximation/error theorems, and counterexamples to proposed general implications. They are neither an unconditional construction for P1 nor a no-go theorem for all admissible P1 aggregate models.

## 2. Exact P1 output identity and what onset misses

Use \(\langle x,y\rangle=n^{-1}x^\top y\). In the population version this means the expectation of the normalized contraction within a Gaussian block. Write

\[
\bar a_a=A_a/L,\quad \bar b_a=B_a/L,\quad
\delta_2(u)=c\odot\tanh'(Wh_1(u)),\quad
\delta_1(u)=\tanh'(wu)\odot W^\top\delta_2(u).
\]

The outer-weight equations give

\[
K_{\rm out}(u,a)
=\langle h_2(u),h_2(u_a)\rangle
 +(u^\top u_a)\langle\delta_1(u),\delta_1(u_a)\rangle.
\]

This is a Gram kernel. Differentiating the stipulated middle matrix, rather than substituting an ordinary gradient-flow middle update, gives

\[
\dot W=-\frac{2}{mn}\sum_a
\left[r_a\delta_2(u_a)\bar b_a^\top
+\rho\bar a_a\bigl(h_1(u_a)-\bar b_a\bigr)^\top\right].
\]

Since the contribution of \(\dot W\) to \(\dot f(u)\) is \(n^{-1}\delta_2(u)^\top\dot W h_1(u)\), define

\[
K_{\rm mem}(u,a)
=\langle\delta_2(u),\delta_2(u_a)\rangle
\langle h_1(u),\bar b_a\rangle,
\]

\[
D(u)=\sum_a\langle\delta_2(u),\bar a_a\rangle
\left[\langle h_1(u),h_1(u_a)\rangle
-\langle h_1(u),\bar b_a\rangle\right].
\]

Then the exact identity is

\[
\boxed{\dot f(u)=-\frac2m\sum_a r_a
 [K_{\rm out}(u,a)+K_{\rm mem}(u,a)]
-\frac{2\rho}{m}D(u).}
\tag{2.1}
\]

There is no sign assertion for the last two contributions. In particular, \(\langle h_1(u),\bar b_a\rangle\) need not be symmetric when \(u\) is a training point: its second argument is a past activity average. A fitted positive semidefinite training kernel therefore changes a term whose fidelity still needs proof.

For the stipulated population initialization \(c(0)=0\), both backpropagated signals vanish, \(A(0)=0\), and \(D(0)=0\). Thus

\[
\dot f(0,u)=-\frac2m\sum_a r_a(0)
\langle h_2(0,u),h_2(0,u_a)\rangle.
\]

Matching this onset identifies none of the subsequent memory source \(D\). Nor does it identify the future cross-kernel between training and test inputs.

At \(r=0\), \(\rho=0\), every stipulated parameter and memory derivative is zero. Absorption at zero loss is exact for P1. Absorption alone says nothing about which absorbing predictor is selected.

## 3. Activity compactifies the horizon but does not close the equations

Let

\[
s(t)=\int_0^t\rho(v)\,dv=L(t)-1.
\]

Where \(\rho>0\), put \(q_a=r_a/\rho\), so \(\sum_a q_a^2=m\). P1 becomes

\[
\begin{aligned}
\frac{dc}{ds}&=-\frac2m\sum_aq_a h_2(u_a),&
\frac{dw}{ds}&=-\frac2m\sum_aq_a\delta_1(u_a)u_a^\top,\\
\frac{dA_a}{ds}&=q_a\delta_2(u_a),&
\frac{dB_a}{ds}&=h_1(u_a),& L&=1+s.
\end{aligned}
\tag{3.1}
\]

In particular,

\[
\bar b_a(s)=\frac{h_{1,a}(0)+\int_0^s h_{1,a}(v)\,dv}{1+s},\qquad
\bar a_a(s)=\frac{\int_0^s q_a(v)\delta_{2,a}(v)\,dv}{1+s}.
\tag{3.2}
\]

These are exact changing-feature histories, not initial features.

Finite activity \(S=s(\infty)<\infty\) also gives useful coordinate bounds. Because \(\sum_a|q_a|\le m\), \(|h_2|\le1\), and \(c(0)=0\), each readout coordinate satisfies \(|c_i(s)|\le2s\). Consequently

\[
|A_{ia}(s)|\le\sqrt m\,s^2,\qquad
|B_{ia}(s)|\le1+s,\qquad |\bar b_{ia}(s)|\le1.
\]

After a prescribed seed cutoff these equations give bounded feature velocities on \([0,S]\). The Gaussian tail and removal of that cutoff are additional obligations if a uniform population assertion is wanted. Thus it would be too strong to say that P1 obtains no regularity from finite activity plus its equations. What remains missing is a finite aggregate representation of the relevant correlations and a small closure residual. A piecewise approximation of the resulting trajectory would use future information and would not solve this missing step.

For example, if two activity-parametrized states satisfy an error inequality

\[
e(s)\le e(0)+\int_0^s\bigl(Ce(v)+\xi(v)\bigr)\,dv,
\]

then

\[
e(S)\le e^{CS}\left[e(0)+\int_0^S\xi(v)\,dv\right].
\tag{3.3}
\]

To verify this bound, substitute the integral inequality iteratively; the repeated constant-kernel integrals sum to \(e^{CS}\). The bound transports the source \(\xi\); it supplies no estimate making \(\xi\) small as the number of aggregates increases.

The normalized direction \(q\) need not have bounded total variation merely because the activity horizon is finite. Even a smooth exponentially damped rotating residual has a direction that rotates infinitely often as physical time tends to infinity. Bounded activity also places no general bound on an unresolved operator's spectral frequencies, spectral mass or approximation rank.

## 4. Constructive conditional theorem: compressible positive relaxation memory

This is a distinct mathematical mechanism, not a derived property of P1.

Let \(\mu\) be a finite positive semidefinite \(d\)-by-\(d\) matrix measure on \([0,\infty)\), with

\[
\operatorname{tr}\mu([0,\infty))\le M,
\qquad K(s)=\int e^{-\lambda s}\,d\mu(\lambda).
\tag{4.1}
\]

Assume \(\mu\), or the bin integrals used below with certified error, is computable from permitted source information. It cannot be fitted using the future reference trajectory. Fix \(S>0\) and \(0<\eta<MS\). There is an explicit kernel

\[
K_q(s)=\sum_{j=0}^{q-1}Q_j e^{-\lambda_j s},\qquad Q_j\succeq0,\quad\lambda_j\ge0,
\]

satisfying

\[
\int_0^S\|K(s)-K_q(s)\|_{\rm op}\,ds\le\eta,
\qquad
q\le2+6R\log\left(\tfrac92R^2\right),\quad R=MS/\eta.
\tag{4.2}
\]

For \(\eta\ge MS\), the zero kernel already meets the bound. If \(M=0\), the kernel is zero.

**Construction and proof.** Set

\[
\lambda_0^{\rm cut}=\frac{2\eta}{3MS^2},\qquad
\Lambda=\frac{3M}{\eta},\qquad
\delta=\frac{\eta}{3MS}.
\]

Map all rates below \(\lambda_0^{\rm cut}\) to zero. Partition \([\lambda_0^{\rm cut},\Lambda]\) into intervals whose upper endpoint is at most \((1+\delta)\) times the lower endpoint; replace every rate in a bin by its lower endpoint and take \(Q_j=\mu(\text{bin }j)\). Omit rates above \(\Lambda\).

The low-rate error has integral at most

\[
M\int_0^S\lambda_0^{\rm cut}s\,ds=\eta/3,
\]

using \(1-e^{-x}\le x\). For a middle-bin rate \(\lambda\) and its representative \(a\),

\[
0\le e^{-as}-e^{-\lambda s}
\le(\lambda-a)s e^{-as}\le\delta\,(as)e^{-as}\le\delta/e.
\]

The total integrated middle error is therefore at most \(M\delta S/e\le\eta/3\). The omitted tail contributes at most

\[
\int_{\lambda>\Lambda}\int_0^S e^{-\lambda s}\,ds\,d\operatorname{tr}\mu(\lambda)
\le M/\Lambda=\eta/3.
\]

These scalar bounds control operator norm because a positive semidefinite matrix has operator norm at most its trace; the triangle inequality handles the three regions. The number of middle bins is at most

\[
\left\lceil\frac{\log(\Lambda/\lambda_0^{\rm cut})}{\log(1+\delta)}\right\rceil.
\]

There is one low-rate mode, \(\Lambda/\lambda_0^{\rm cut}=\tfrac92R^2\), and \(\log(1+\delta)\ge\delta/2\) for \(0\le\delta\le1\). This proves (4.2).

For a varying input \(u(s)\in\mathbb R^d\), initialize \(z_j(0)=0\) and evolve

\[
z_j'=-\lambda_jz_j+u(s),\qquad h_q(s)=\sum_j Q_jz_j(s).
\tag{4.3}
\]

Integration of each scalar linear equation gives \(h_q=K_q*u\). If \(\sup_s\|u(s)\|\le U\), then

\[
\sup_{s\le S}\|(K-K_q)*u(s)\|\le U\eta.
\tag{4.4}
\]

The memory is passive: for \(E=\tfrac12\sum_j z_j^\top Q_jz_j\), differentiation gives

\[
E'=-\sum_j\lambda_jz_j^\top Q_jz_j+u^\top h_q\le u^\top h_q.
\]

Modes with singular \(Q_j\) can be restricted to its range. There are at most \(dq\) scalar states and \(O(d^2q)\) stored coefficients and elementary operations per vector-field evaluation. No neuron, density, grid mass, initial neural feature or moment hierarchy is evolved. The mode coordinates are integrated responses to the current input. An initial unresolved-memory free response, if present, requires its own admissible approximation; it is not included for free in the zero-initial-memory theorem.

### 4.1 Nonlinear feedback and genuine changing resolved features

Suppose the exact reduced equation has the independently established form

\[
x'=F(x)+C(K*g(x)),\qquad x(0)=x_0,
\tag{4.5}
\]

where \(C\) is a fixed matrix with norm at most \(c\), \(F\) is Lipschitz with constant \(L_F\), and \(g\) is Lipschitz with constant \(L_g\) and bounded by \(U\). Assume the exact and approximate trajectories exist in a common region on which these bounds hold. Replacing \(K\) by \(K_q\) makes (4.5) an autonomous finite ODE using (4.3) with input \(g(x)\). The input and resolved features may change with \(x\).

Let \(E(s)=\sup_{v\le s}\|x(v)-x_q(v)\|\). Split the memory difference into \(K*(g(x)-g(x_q))\) and \((K-K_q)*g(x_q)\). Since \(\int_0^S\|K\|\le MS\), integration of the differential equations and interchange of the nonnegative bounds yield

\[
E(s)\le cU\eta S+(L_F+cL_gMS)\int_0^sE(v)\,dv.
\]

Consequently

\[
E(S)\le cU\eta S\exp\bigl[(L_F+cL_gMS)S\bigr].
\tag{4.6}
\]

The same elementary iterated-integral argument as in (3.3) proves this estimate. A Lipschitz output map converts it to output error. With a state-dependent multiplier \(C(x)\), the proof adds the bounded-memory term to the Lipschitz constant and otherwise proceeds in the same way.

For fixed dimensions, \(S,M,U,c,L_F,L_g\) and output Lipschitz constant, error \(\varepsilon\) therefore requires \(q=O(\varepsilon^{-1}\log(1/\varepsilon))\). If an independently justified reference sampling error is \(\varepsilon_n\asymp n^{-1/2}\), the recurrent state and per-step work are \(O(\sqrt n\log n)=o(n)\). This does not establish a sampling rate for P1, bound the cost of finding \(\mu\), or guarantee that numerical stiffness will not increase the number of integration steps. The largest retained rate grows as \(O(1/\eta)\); a total-runtime claim needs an appropriate integrator and its accuracy/cost analysis.

Training loss follows from output accuracy: if \(\|r-r_q\|_m\le\varepsilon\) and \(\|r\|_m\le R_0\), then

\[
\big|\|r_q\|_m^2-\|r\|_m^2\big|\le2R_0\varepsilon+\varepsilon^2.
\]

A finite output vector does not by itself provide an arbitrary-input test evaluator. Uniform test-input accuracy requires a permitted output family with uniform estimates and affordable evaluation.

### 4.2 Stopping is an additional bridge

Equation (4.6) compares equal activity coordinates. The two physical-time models can stop at different total activities, so this estimate is not automatically an all-time or terminal-predictor theorem.

A sufficient extra condition can be stated precisely. Suppose both activity flows have regular extensions through a scalar stopping coordinate \(\ell=0\), their first zeroes are \(S_*\) and \(S_{q,*}\), they are compared on a common interval containing those zeroes, \(|\ell-\ell_q|\le e\), and \(\ell'\le-\alpha<0\) throughout that interval. Evaluating \(\ell\) at the two zeroes and integrating its derivative gives

\[
|S_*-S_{q,*}|\le e/\alpha.
\]

If \(\|x'\|\le V\), then the terminal state error is at most the matched-activity error plus \(Ve/\alpha\). This is a conditional transversality estimate, not an assertion that the residual norm has a smooth extension through zero. For a Euclidean residual norm, such an extension or an equivalent terminal argument must be supplied.

In an ordinary residual equation \(\dot r=-(2/m)K r\) with symmetric \(K\succeq\kappa I\), direct differentiation yields \(d\rho/ds\le-2\kappa/m\) before stopping. P1's extra terms in (2.1) prevent applying that calculation on the basis of a fitted positive kernel alone.

## 5. Counterexamples to stronger implications

### 5.1 Matching onset and stable training does not select the test prediction

Fix an integer \(p\ge0\) and a real parameter \(a\). Consider a smooth predictor with parameters \((x,z,a)\), one training output and one test output:

\[
f_{\rm tr}=x,\qquad f_{\rm test}=z+a(1-x)^{p+2}.
\]

The training label is zero and the loss is \(x^2/2\). Its exact Euclidean gradient flow from \((x,z,a)=(1,0,a)\) is

\[
x=e^{-t},\qquad z=0,\qquad a(t)=a.
\]

The residual, training loss, and total activity \(\int_0^\infty|x(t)|dt=1\) are identical for every \(a\). The full predictor is stationary at zero training loss. Every initial derivative of \(f_{\rm test}\) through order \(p+1\) vanishes, independent of \(a\), but

\[
f_{\rm test}(\infty)=a.
\]

The training and test tangent kernel is positive semidefinite at every time, because it is the Gram matrix of the actual parameter gradients:

\[
\nabla f_{\rm tr}=(1,0,0),\qquad
\nabla f_{\rm test}=\bigl(-a(p+2)(1-x)^{p+1},\ 1,\ (1-x)^{p+2}\bigr).
\]

Thus even exact positive tangent geometry, identical stable training, bounded activity, and any prescribed finite onset jet do not determine the terminal test value. The initial coordinates invisible to training can matter later. With a smooth function flat near \(x=1\) and nonzero at \(x=0\), the same construction matches every onset derivative; the polynomial version already covers analytic finite-jet claims.

This is a counterexample to a general inference, not an embedding into the stipulated tanh P1 system. Its role is to identify missing information: one must approximate the relevant training-to-test coupling and hidden state, rather than certify only training dissipation and onset coefficients.

### 5.2 Passivity and finite horizon alone do not bound realization dimension

The positive-relaxation representation (4.1) is stronger than passivity. To see the distinction without appealing to realization theory, fix \(\gamma>0\) and consider \(N\) two-dimensional driven oscillators,

\[
z_j'=(-\gamma I+jJ)z_j+e_1u,\qquad
h=\sum_{j=1}^N e_1^\top z_j,\quad
J=\begin{pmatrix}0&-1\\1&0\end{pmatrix}.
\]

Every mode has decay rate \(\gamma\). The storage \(\frac12\sum_j\|z_j\|^2\) has derivative \(-\gamma\sum_j\|z_j\|^2+uh\), proving passivity. The impulse-response kernel is

\[
k_N(s)=e^{-\gamma s}\sum_{j=1}^N\cos(js).
\]

On the fixed past/future interval of length \(4\pi\), define its Hankel operator on \(L^2(0,2\pi)\) by

\[
(H_Nv)(t)=\int_0^{2\pi}k_N(t+s)v(s)\,ds.
\]

When \(\gamma=0\), orthogonality of \(\cos jt\) and \(\sin jt\) shows that this operator acts as multiplication by \(\pi\) and \(-\pi\), respectively, on their \(2N\)-dimensional span and is zero on its orthogonal complement. For \(\gamma>0\), write \(H_N=D H_N^{(0)}D\), where \((Dv)(t)=e^{-\gamma t}v(t)\). On the \(2N\)-dimensional space obtained by applying \(D^{-1}\) to that span,

\[
\|H_Nv\|_2\ge\pi e^{-4\pi\gamma}\|v\|_2.
\]

Any linear time-invariant memory with \(q\) scalar state variables has a kernel \(C e^{As}B\), and its Hankel operator has rank at most \(q\), since

\[
(H_qv)(t)=C e^{At}\left[\int_0^{2\pi}e^{As}Bv(s)\,ds\right].
\]

If \(q<2N\), the restriction of \(H_q\) to the preceding \(2N\)-dimensional space has a nonzero kernel vector. On a normalized such vector,

\[
\|H_N-H_q\|_{2\to2}\ge\pi e^{-4\pi\gamma}.
\tag{5.1}
\]

Therefore uniformly exponentially stable passive memory may require arbitrarily many states for fixed finite-horizon input/output accuracy. This obstruction is restricted to linear time-invariant realizations and does not rule out the broader nonlinear aggregate class. Its spectral mass is \(N\), so it does not contradict Section 4. Dividing the kernel by \(N\) divides the lower bound by \(N\); the example then supplies no linear-width obstruction at error \(n^{-1/2}\). These restrictions matter for applying it to bounded neural observables.

## 6. Exact open implication and recommended route status

The passive construction becomes relevant to P1 only after establishing an admissible resolved state \(x\) and the following bridge:

1. Derive the exact unresolved influence, including the terms \(K_{\rm mem}\) and \(D\) in (2.1), as a computable causal memory operator of the retained variables.
2. Prove its positive-relaxation spectral representation with width-independent mass, or prove a comparably efficient approximation property for its possibly nonpositive, time-dependent kernel.
3. Control a nonconvolution or nonlinear remainder by a bound that tends to zero with the number of retained modes, using no reference trajectory.
4. Supply the initial unresolved free response, initialization and coefficient computation costs, and a query-uniform test readout.
5. Establish a terminal comparison condition strong enough to identify the same selected predictor, and a numerical cost bound at the reference sampling accuracy.

Conditional expectation by itself supplies none of these points. Even if an exact projection identity rewrites unresolved influence as a memory term, the memory kernel is not thereby positive, low rank, computable from a finite aggregate state, or inexpensive to realize. A dissipative full system need not generate a positive-relaxation kernel after arbitrary projection.

| Claim | Status | Precise limit |
|---|---|---|
| Exact P1 decomposition (2.1) and zero-loss absorption | Proved identity | No dissipation or closure claim |
| Bounded activity controls propagation once the closure source is small | Proved conditional estimate | No source estimate or complexity bound |
| Positive relaxation memory admits \(O(\eta^{-1}\log(1/\eta))\) finite passive modes | Proved conditional construction | Requires computable PSD spectral measure and bounded mass |
| This gives sublinear recurrent state at \(n^{-1/2}\) accuracy | Proved conditional scaling | Constants, dimensions and sampling rate must be uniform; total runtime still needs analysis |
| Stable training plus onset matching determines final test output | False as a general implication | Counterexample is not asserted to be a P1 realization |
| Passivity plus finite activity/horizon bounds memory dimension | False for unrestricted LTI passive class | Does not prove a normalized P1 lower bound |
| P1 has the required efficiently realizable memory | Open | No spectral/causal bridge derived |

**Registry recommendation:** preserve the constructive theorem as a conditional mechanism and the exact P1 decomposition as an audit tool. The route is blocked at identification of the actual unresolved operator, not at passive discretization. Reopen it if a P1-specific projection produces either a bounded positive spectral measure or another verified approximation class with a quantitative mode count. Terminal stability or additional onset matching alone does not meet that condition.
