# Gaussian finite jets and quantitative continuation

Status: scoped author calculation, not an independent review or a promoted result. The asymptotic and conditional continuation lemmas below have complete proofs. Their use as a quantitative all-time Gaussian-network approximation remains open. No experiment or Git write was performed.

The supplied source was read completely: `studies/closure_sampling_20261003/DIMENSION_PREFACTOR_OPTIMIZATION.md`, 455 lines. Its named upstream study dependencies were not opened. Its analytic-event and fitting interfaces are consequently treated as supplied conditional hypotheses, not independently re-established results. This cross-study input was explicitly authorized in the assignment.

## 1. The single-origin continuation map

Let \(T,r,M>0\). Assume a scalar source \(g\) is holomorphic on a neighborhood of the closed time rectangle

\[
\{-r\le\operatorname{Re}t\le T+r,\ |\operatorname{Im}t|\le r\}
\]

and has modulus at most \(M\) there. The discussion applies to each source coordinate and each fixed real input direction. Define

\[
q=\frac{\pi T}{8r},\quad b_0=\tanh q,\quad
b_1=\tanh(q+\pi/4),\quad\eta=b_0/b_1,
\quad \xi_* =\frac{2\eta}{1+\eta^2},\quad d_*=1-\xi_*.
\tag{1}
\]

These are the source's notation; \(q\) in this note is not network width or source count. Its conformal coordinate is

\[
\psi(\xi)=\frac{\xi-\eta}{1-\eta\xi},\qquad
z(\xi)=\frac T2+\frac{2r}{\pi}
 \log\frac{1+b_1\psi(\xi)}{1-b_1\psi(\xi)}.
\tag{2}
\]

Here the logarithm is its analytic branch on the right half-plane. Since \(|\psi(\xi)|<1\) for \(|\xi|<1\), the fraction inside that logarithm has positive real part. Its argument lies in \((-\pi/2,\pi/2)\), giving \(|\operatorname{Im}z|<r\). Also

\[
\left|\log\left|\frac{1+b_1\psi}{1-b_1\psi}\right|\right|
\le \log\frac{1+b_1}{1-b_1}
=2(q+\pi/4),
\]

which gives \(-r<\operatorname{Re}z<T+r\). Thus the disk maps inside the required rectangle. Substituting \(\psi(0)=-\eta\) and \(\psi(\xi_*)=\eta\), and using \(b_1\eta=b_0\), proves \(z(0)=0\) and \(z(\xi_*)=T\). Both maps increase on this real interval, so every \(t\in[0,T]\) has a preimage in \([0,\xi_*]\).

The composition \(G(\xi)=g(z(\xi))\) is bounded by \(M\) on the unit disk. Writing \(G(\xi)=\sum_{j\ge0}A_j\xi^j\), Cauchy's integral formula on circles of radius \(\rho<1\), followed by \(\rho\uparrow1\), gives \(|A_j|\le M\). A degree-\(K\) Taylor sum therefore has uniform error on \([0,\xi_*]\) at most

\[
\frac{M\xi_*^{K+1}}{1-\xi_*}
\le \frac M{d_*}\exp[-d_*(K+1)].
\tag{3}
\]

For a target nodal tolerance \(\mathrm{tol}>0\), the sufficient certificate is

\[
K+1\ge d_*^{-1}\log\frac{M}{d_*\mathrm{tol}}.
\tag{4}
\]

If the logarithm is negative, any nonnegative \(K\) already suffices. The large-width applications below have a positive logarithm. A condition stated with \(K\), rather than \(K+1\), on the left is slightly stronger and also sufficient.

## 2. Exact formula and asymptotics for the distance to the disk boundary

Set \(a=e^{-2q}\) and \(c=e^{-\pi/2}\). Then

\[
b_0=\frac{1-a}{1+a},\quad b_1=\frac{1-ca}{1+ca},\quad
\eta=\frac{(1-a)(1+ca)}{(1+a)(1-ca)}.
\]

Since \(1-2\eta/(1+\eta^2)=(1-\eta)^2/(1+\eta^2)\), direct subtraction yields

\[
d_*=
\frac{2(1-c)^2a^2}
 {(1-ca^2)^2+(1-c)^2a^2}.
\tag{5}
\]

Indeed, write the numerator and denominator of \(\eta\) as
\(A=1-(1-c)a-ca^2\) and \(B=1+(1-c)a-ca^2\). Then \(B-A=2(1-c)a\) and \(A^2+B^2=2[(1-ca^2)^2+(1-c)^2a^2]\), proving (5).

Consequently, as \(T/r\to\infty\),

\[
d_*=2(1-e^{-\pi/2})^2
 e^{-\pi T/(2r)}\bigl(1+O(e^{-\pi T/(2r)})\bigr).
\tag{6}
\]

The error term follows by expanding the denominator of (5), which is \(1+O(a^2)\); its reciprocal has the same expansion once \(a\) is sufficiently small. In particular the exponent is \(\pi T/(2r)\), not \(\pi T/(4r)\). The squaring in \((1-\eta)^2\) matters.

Write \(A_T=\pi T/(2r)\) and \(c_0=2(1-e^{-\pi/2})^2\). For the particular cutoff chosen by (4), its unrounded value has asymptotic

\[
\frac{e^{A_T}}{c_0}
\left[A_T+\log\frac{M}{\mathrm{tol}}-\log c_0+o(1)\right]
(\text{relative }o(1)\text{ in the prefactor}).
\tag{7}
\]

More precisely, this follows by inserting \(d_*=c_0e^{-A_T}(1+O(e^{-A_T}))\) separately into the reciprocal and logarithm. If \(\log(M/\mathrm{tol})=O(A_T)\), their product differs from \(c_0^{-1}e^{A_T}[A_T+\log(M/\mathrm{tol})-\log c_0]\) by a relative \(o(1)\).

In the supplied source, with \(\ell_n=\log(en)\),

\[
T_n=32\lambda^{-1}\ell_n,
\qquad r_n=c_t\ell_n^{-1/2},
\qquad A_{T_n}=\frac{16\pi}{\lambda c_t}\ell_n^{3/2}.
\tag{8}
\]

Its modulus is \(M_n=M_0\sqrt n\), and its chosen nodal tolerance is
\(\mathrm{tol}_n=n^{-1}/(32N_n)\), where the retained Fourier/Chebyshev coefficient count \(N_n\) is bounded by a fixed-data multiple of \(\ell_n^{3d/2+1}\). Therefore

\[
\log\frac{M_n}{\mathrm{tol}_n}
=\frac32\log n+\log(32M_0N_n)=O(\ell_n).
\]

The literal sufficient single-origin jet cutoff in (4) consequently obeys

\[
K_n+1\sim
\frac{16\pi}{2(1-e^{-\pi/2})^2\lambda c_t}
\ell_n^{3/2}
\exp\left(\frac{16\pi}{\lambda c_t}\ell_n^{3/2}\right),
\tag{9}
\]

when it is chosen as the smallest integer satisfying that certificate. Rounding changes neither asymptotic. This is superpolynomial in \(n\): dividing its logarithm by \(\log n\) gives a quantity asymptotic to \(16\pi\sqrt{\ell_n}/(\lambda c_t)\), which diverges.

Equation (9) concerns the sufficient preprocessing jet order of this construction. It does not increase the source's retained coefficient count \(N_n\), which remains polylogarithmic, and it does not refute its existential finite-jet assertion. The source explicitly disclaims efficient preprocessing. Large initializer work and workspace are permitted by the present task if explicit and dense-free; only the retained compact state must preserve the requested size bound.

It is also not a lower bound on all reconstruction methods, on all possible continuations, or on these particular neural sources. Even for this Taylor method, the certificate can overestimate the actual error when coefficients cancel or are much smaller than \(M\). Replacing \(e^{-d_*(K+1)}\) in (3) by the exact \(\xi_*^{K+1}\) improves constants but not this certificate's asymptotic order, because \(-\log(1-d_*)/d_*\to1\).

## 3. Approximate initial jets need a separate accuracy budget

The finite-jet provenance is exact algebra. With normalized initial derivatives \(b_k=g^{(k)}(0)/k!\),

\[
A_j=\sum_{k=0}^j b_k[\xi^j]z(\xi)^k.
\tag{10}
\]

The triangular form follows from \(z(0)=0\). If a Gaussian compiler instead supplies approximations \(\widehat b_k\), substitution and the triangle inequality give the exact deterministic propagation bound

\[
\sup_{0\le\xi\le\xi_*}
\left|\sum_{j=0}^K(\widehat A_j-A_j)\xi^j\right|
\le\sum_{k=0}^K|\widehat b_k-b_k|
 \sum_{j=k}^K\xi_*^j\left|[\xi^j]z(\xi)^k\right|.
\tag{11}
\]

Thus arbitrary fixed-order convergence of the individual moments does not calibrate the accuracy of the reconstructed nodal values when \(K=K_n\). The coefficient amplification in (11), the moment errors at every order, and the subsequent normalized-DFT reconstruction factor must all be controlled together. The source's exact linear paired-action identity remains true if identical linear operations are applied to exact paired jets. Approximate moments or separately estimated mixer entries require their own common-error analysis; exact pairing is not recovered merely from individual scalar consistency.

## 4. What stable staged continuation would prove

Here is a complete conditional numerical lemma, stated separately from the Gaussian application.

Let \(\Phi_h\) be the exact flow of an ODE on a normed state space, on an admissible region. Suppose that for every state visited by either the exact or approximate algorithm:

1. Its trajectory has a complex-time Taylor expansion on a disk of radius \(r\), with norm bounded by \(M\) on that disk.
2. Its real flow satisfies \(\|\Phi_h(x)-\Phi_h(y)\|\le e^{Lh}\|x-y\|\) for the compared states, with \(L\ge0\). A negative valid exponent may be replaced by zero.
3. All steps and the comparisons stay inside that region. A strict error margin and a first-exit argument may verify this condition.

Let \(0<\theta<1\), take step lengths \(h_j\le\theta r\) summing to \(T\), and at each current approximate state evaluate its own degree-\(p\) Taylor flow polynomial exactly. Denote the number of steps by \(J\). Cauchy's bound gives the one-step defect

\[
\tau\le\frac{M\theta^{p+1}}{1-\theta}.
\]

If \(e_j\) is the state error at the \(j\)-th node, add and subtract the exact flow started from the current approximate state:

\[
e_{j+1}\le e^{Lh_j}e_j+\tau.
\]

Iterating and using \(\sum h_j=T\) proves

\[
\max_{j\le J}e_j
\le e^{LT}\left(e_0+
\frac{JM\theta^{p+1}}{1-\theta}\right).
\tag{12}
\]

There is no assumption that a scalar source value alone determines its future. The lemma requires the current ODE state and its actual vector field. With \(e_0=0\), a sufficient order for error \(\mathrm{tol}\) is

\[
p+1\ge\frac{LT+\log[JM/((1-\theta)\mathrm{tol})]}
 {|\log\theta|}.
\tag{13}
\]

For \(\theta=1/2\), \(T_n\asymp\ell_n\), \(r_n\asymp\ell_n^{-1/2}\), bounded \(L\), polynomially bounded \(M_n\), and polynomially small tolerance, choose each step as large as permitted except possibly the last. This gives

\[
J_n=O(\ell_n^{3/2}),\qquad p_n=O(\ell_n).
\tag{14}
\]

Thus stable evolution from current states can avoid the huge single-origin order in (9). This is an upper bound for a different, conditionally available algorithm. It is not a proof that the source's initial jets can be stably re-expanded at new centers without access to the current state. Nor does the supplied high-probability analyticity of a reference path verify the lemma's uniform hypotheses for numerical states in a neighborhood. If only a width-dependent stability constant \(L_n\) is available, (13) retains the term \(L_nT_n\); it must not be replaced by \(O(\ell_n)\) without proof.

## 5. A concrete staged Gaussian-word recursion

For the canonical two-hidden-layer tanh population equations, write the connector as \(W^{(2)}=W_0^{(2)}+K\). At a stage center, let subscript \(k\) denote the coefficient of \(\tau^k\), not the unnormalized derivative. Each first-layer training field, readout, and connector increment has formal coefficients \(Z^{(1)}_{a,k}\), \(c_k\), and \(K_k\). Define activation and derivative-gate coefficients by formal composition with tanh. Set

\[
Z^{(2)}_{a,k}=W_0^{(2)}H^{(1)}_{a,k}
             +\sum_{i+j=k}K_iH^{(1)}_{a,j},
\quad
r_{a,k}=\sum_{i+j=k}E_2[c_iH^{(2)}_{a,j}]
                     -y_a\mathbf1_{\{k=0\}}.
\tag{15}
\]

The backward coefficients are obtained by the exact product recurrences

\[
\Delta^{(2)}_{a,k}
=\sum_{i+j=k}c_i[\phi'(Z^{(2)}_a)]_j,
\]

\[
\Delta^{(1)}_{a,k}
=\sum_{i+j=k}[\phi'(Z^{(1)}_a)]_i
\left((W_0^{(2)})^*\Delta^{(2)}_{a,j}
      +\sum_{b+c=j}K_b^*\Delta^{(2)}_{a,c}\right).
\tag{16}
\]

For orthonormal training directions and mean squared loss, the next coefficients are

\[
Z^{(1)}_{a,k+1}=-\frac2{m(k+1)}
                         \sum_{i+j=k}r_{a,i}\Delta^{(1)}_{a,j},
\quad
c_{k+1}=-\frac2{m(k+1)}
                    \sum_a\sum_{i+j=k}r_{a,i}H^{(2)}_{a,j},
\tag{17}
\]

\[
K_{k+1}=-\frac2{m(k+1)}\sum_a\sum_{i+j+l=k}
           r_{a,i}\Delta^{(2)}_{a,j}\otimes H^{(1)}_{a,l}.
\tag{18}
\]

These identities follow by equating coefficients in the exact ODE and its forward/backward definitions; a rank-one action is \((U\otimes V)F=U E_1[VF]\). They are causal in coefficient order: the parameters at order \(k\) are known before the forward pass, the backward pass then yields (17)–(18) at order \(k+1\).

For every fixed stage count and order, this is a finite initialized-word program. Tanh has bounded derivatives of each fixed order. Its composition coefficients are finite polynomials in earlier coefficient fields with such derivative factors. Hence each fixed coefficient and its needed source derivatives have polynomial Gaussian envelopes on compact sets of earlier deterministic coefficients. The maintained finite Gaussian source compiler applies to this finite graph; it supplies a direct-law quadrature construction for its contractions, retaining both \(W_0^{(2)}\) and its actual adjoint. Its source-response coefficients are held fixed when taking named-source derivatives. This assertion uses the fixed-program hypotheses, not a new uniform bound in the stage count or Taylor order.

The algebra also displays the accumulated memory. Evaluating the degree-\(p\) increment at a step \(h\) combines (18) into

\[
K_{\mathrm{next}}-K_0
=\sum_a\sum_{j+l\le p-1}\beta_{a,j,l}
              \Delta^{(2)}_{a,j}\otimes H^{(1)}_{a,l},
\]

\[
\beta_{a,j,l}=-\frac2m
\sum_{i=0}^{p-1-j-l}\frac{h^{i+j+l+1}}{i+j+l+1}r_{a,i}.
\tag{19}
\]

Thus a literal retained rank-one list adds at most \(mp(p+1)/2\) terms per stage. Up to fixed root and passive-panel instructions, (15)–(16) require at most \(2m(p+1)\) new initialized-action calls per stage: forward calls on \(H^{(1)}_{a,k}\) and reverse calls on \(\Delta^{(2)}_{a,k}\). Already known literal calls can be reused. A straightforward compiler therefore has an upper source-count bound \(s=O(Jmp)\), and stores an \(O(s^2)\) covariance/response prefix as well as the word graph and rank-one memories. These are algorithmic upper counts, not lower bounds on optimal encodings.

If all conditional hypotheses behind (14) held, this particular source count would be polylogarithmic in \(n\). That observation is useful: a fresh source at each stage does not by itself force polynomial width scaling. It still does not certify the old retained-size bound. One must count the entire word graph, coefficient quadratures, replay nodes, retained joint marks, and the final compact ODE state. Coefficient-node quadrature can be larger temporary setup work; nodes retained for runtime count toward the compact state.

Resetting the source covariance and rank-one memories at a stage boundary is not justified. A current nonlinear source generally has correlations and response terms inherited from earlier forward and reverse calls. The exact three-query calculation in this study's `DIRECT_GAUSSIAN_ATTEMPT.md` exhibits a fresh source and its nonzero predictor contribution. A valid fixed-size restart therefore needs a quantitative compression of the complete current joint action law, or a fixed initialized dictionary proved to approximate every reached query. Keeping a growing transcript gives a different storage contract; discarding it gives a different law unless its error is controlled.

The recursions above concern training and any separately fixed passive panel. They do not supply a whole-sphere error estimate or an all-time endpoint bound. Those require the stated spatial approximation and fitting/tail interfaces, with the same quantitative constants and approximate self-generated residuals.

## 6. High-probability analyticity does not justify annealed analytic continuation

Let \(E_n\) be a high-probability event on which a random source is holomorphic on a common complex disk and bounded there by \(M_n\). It is valid to differentiate its *truncated expectation*:

\[
\partial_t^k E[\mathbf1_{E_n}g_n(t)]
=E[\mathbf1_{E_n}\partial_t^kg_n(t)].
\tag{20}
\]

To prove this, use Cauchy's integral formula on a smaller common circle. Its integrand times \(\mathbf1_{E_n}\) is bounded by a deterministic integrable constant. Fubini moves expectation through the contour integral, and the same formula identifies both sides. The event is fixed when differentiating; it may depend on the random initialization but not on the contour integration variable.

This does not identify (20) with unconditional Gaussian word moments. The complement must be controlled. Whenever the derivatives exist there and have a finite \(p\)-th moment, Hölder gives only

\[
\left|E[\mathbf1_{E_n^c}\partial_t^kg_n(0)]\right|
\le \|\partial_t^kg_n(0)\|_{L^p}
       \Pr(E_n^c)^{1-1/p}.
\tag{21}
\]

For growing \(k\), both factors require quantitative bounds. A fixed-order finite-program moment theorem supplies no uniform estimate for the potentially enormous orders in (9), or even for the staged orders in (14).

A simple counterexample shows why the missing argument is substantive. It concerns only this inference, not a counterexample to the tanh-network target. Let \(X\sim N(0,1)\) and

\[
g(t,X)=\frac1{1+t^2X^2},\qquad t\in\mathbb R.
\tag{22}
\]

Fix \(a>0\), put \(R_n=\sqrt{a\log n}\), \(E_n=\{|X|\le R_n\}\), and \(r_n=1/(2R_n)\). Gaussian exponential moments give \(\Pr(E_n^c)\le2n^{-a/2}\). On \(E_n\), (22) is holomorphic throughout \(|\operatorname{Im}t|<1/R_n\) and bounded by four on \(|\operatorname{Im}t|\le r_n\), for arbitrary real part: factor its denominator as \((1+itX)(1-itX)\), whose factors each have modulus at least \(1/2\).

Nevertheless its unconditional expectation is not real analytic at zero. For each fixed derivative order, differentiation under the real expectation is valid: derivatives of \(s\mapsto(1+s^2)^{-1}\) are bounded on the real line, giving a dominator \(C_k|X|^k\). Its even Taylor coefficients are exactly

\[
\frac{1}{(2k)!}\partial_t^{2k}E[g(t,X)]\big|_{t=0}
=(-1)^kEX^{2k}=(-1)^k(2k-1)!!.
\]

Gaussian integration by parts gives the moment recurrence
\(EX^{2k}=(2k-1)EX^{2k-2}\), proving the displayed product. Each factor \(2j-1\ge j\), so \((2k-1)!!\ge k!\). Also
\(\log(k!)\ge\int_1^k\log x\,dx\ge k\log k-k\). Therefore the \((2k)\)-th root of the coefficient magnitude is at least \(\sqrt{k/e}\), which diverges. The Taylor series has radius zero. High-probability strips of width comparable to \(1/\sqrt{\log n}\), bounded real values, and valid expectation/differentiation at every separately fixed order do not imply an annealed holomorphic strip or convergence of its full Taylor series.

The same example quantifies the loss of high-order moments on the rare complement:

\[
\frac{E[X^{2k}\mathbf1_{E_n}]}{EX^{2k}}
\le\frac{R_n^{2k}}{(k/e)^k}
=\left(\frac{eR_n^2}{k}\right)^k.
\tag{23}
\]

For \(k\ge2eR_n^2\), this ratio is at most \(2^{-k}\). Thus an event with probability tending to one can discard almost all of a high-order derivative expectation. This is exactly the kind of estimate that must be checked before replacing good-event finite-width jets by unconditional Gaussian compiler coefficients.

## 7. The remaining feedback statement

The maintained compiler proves convergence for every fixed graph, fixed positive source regularization, and then its ordered quadrature/regularization limits. In a staged construction the graph size, source count, derivative order, horizon, and requested accuracy all depend on \(n\). A valid diagonal result must control, on the actual approximate program's own states:

- errors in its source covariances and response coefficients, including nearly dependent query directions;
- propagation of those errors through its computed residuals and trained rank-one memory;
- any retained-source truncation and any removed clipping/regularization;
- the error entering the final whole-sphere compact predictor and its fitting tail.

For a finite sequence of stages, if these errors yield an explicit defect \(\varepsilon_j\) in the state update, the same proof as (12) replaces \(\tau\) by \(\tau+\varepsilon_j\). The useful target is therefore a bound on \(\sum_j\varepsilon_j\) together with a verified stability constant, not merely consistency of each coefficient for a separately fixed stage. Orthogonal-data transformed-flow stability in book B.1 controls comparisons with fixed roots and bounded readout, but does not itself estimate a growing Gaussian compiler's source defects.

The decisive conclusions are accordingly distinct. The supplied initial-jet certificate is finite and has the superpolynomial sufficient order (9), without changing its retained polylogarithmic source count. Stable staged current-state evolution has the much smaller conditional orders (14), and (15)–(19) give a concrete direct Gaussian-word implementation at every separately fixed stage count and order. The missing theorem is a quantitative growing-program, own-feedback approximation with the required retained-state bound, plus justified passage between high-probability complex source control and the unconditional Gaussian moments actually compiled. No lower bound ruling out such a construction is established here.

## Provenance and check record

Required research/proof skill instructions from earlier tasks were reused; current `AGENTS.md` and workflow Part 1 were reread. The mandatory canonical-notation skill remained inaccessible as previously disclosed; the explicit user requirements and maintained notation contract were followed. Only this assigned report was written.

Complete source units used:

- Authorized source `DIMENSION_PREFACTOR_OPTIMIZATION.md`, all 455 lines, especially Sections 3–5. Its upstream analytic-event proof is not part of this audit's supplied inputs.
- Maintained `docs/08-autonomous-computation.qmd`, C.1, C.2 and C.6, read completely in the preceding task: precise compiler, numerical limits, and cost. Its circle/fixed-horizon trajectory theorem is not extended here.
- Maintained `docs/12-three-sample-learning.qmd`, III.F.1–7, read completely in the preceding task: finite Gaussian programs, response rules, singular-query handling, feedback, and action construction.
- Maintained `docs/04-continuing-flows.qmd`, B.1, read completely in the preceding task: the exact orthogonal-data transformed stability theorem and its qualitative width passage.
- This study's author-owned `DIRECT_GAUSSIAN_ATTEMPT.md`, whose exact three-query formula and scope are cited in Section 5.

Source hashes checked on 2026-10-06:

| Source | SHA-256 |
| --- | --- |
| Authorized dimension-prefactor note | `8e149122bcd83a8f64bceba97a6617f644f10e59fd97456f3cfa0e10273c8f2e` |
| `docs/08-autonomous-computation.qmd` | `72224d6c545531a768e090ac24b681c58046de0a42b37105a9a6ad51316c8b54` |
| `docs/12-three-sample-learning.qmd` | `06d6e45f1d7d6c280fb0c5dcac3303b49d56bec4d4a7df632cd73af5091d1d15` |
| `docs/04-continuing-flows.qmd` | `78728dbbcc551392f7dd6cf7b91bad42324e5b540655d4242e830e9c38774a43` |

HEAD on metadata check: `3834145d910202a84824d943fe7d7f65714d96f2`; the shared index was empty. Other changed/untracked study paths were observed only in status metadata, not read. Author checks: disk-image constants, the factor of two in the boundary exponent, the Taylor degree's off-by-one, fixed-data asymptotics, retained/setup cost distinction, normalized-jet convolution factors, the exact rank-one stage update, conditional numerical hypotheses, and the Gaussian rare-event derivative counterexample. No independent PASS is claimed.
