# Adversarial audit of the revised fifth-jet polynomial theorem

Date: 25 August 2026.

Audited artifact:
`FIFTH_JET_POLYNOMIAL_THEOREM.md`.

## Verdict

**PASS, with the claim restricted exactly as the theorem restricts it.**

The following statement is proved for every separately fixed finite hidden
depth \(L\):

\[
 \beta_{t,\psi,L}
 :=[\eta^5]\{F_{2t,L}(\eta)-F_{t,L}(2\eta)\}
\]

is an activation-defined polynomial in the positive integer \(t\) of degree
at most four, and

\[
 |\beta_{t,\psi,L}|
 \le {227\over180}B_\psi^{E_{L,5}}t^4.
 \tag{A.1}
\]

The coefficient-level power \(t^4\) is sharp for the class, because the
identity activation at \(L=1\) has a nonzero quartic leading coefficient.

This is **not** a proof of a horizon-uniform nonzero-step Taylor remainder.
In particular, it does not prove

\[
 \sup_{0<|\eta|\le \rho/t}
 {\left|\Delta_{t,L}(\eta)
 -[\eta^3]\Delta_{t,L}(\eta)\eta^3\right|\over |\eta|^5}
 \lesssim_{\psi,L}t^4.
 \tag{A.2}
\]

Section 7 of the audited theorem states this boundary explicitly.  Thus the
artifact passes as an exact width-first fifth-jet theorem and must not be
cited as the still-open uniform finite-step theorem.

## 1. Width-first provenance

The limit order is the required one.  The proof chain inside the scoped
study is:

1. `temporary_depth_time_doubling/WIDTH_DEPTH_TIME.md` states the exact
   finite-width network, the \(n\nabla f_n\) mean-field ascent scaling, and
   the simultaneous recomputed updates.  Its theorem proves, for every fixed
   finite \((L,N)\) and every fixed \(h\ne0\), convergence of expected output
   and of the complete adaptive row/column history to the inverse-free
   Gaussian DAG.  Its proof includes concentration, regression coefficients,
   reused-column responses, and terminal uniform integrability.
2. `temporary_depth_time_doubling/CUBIC_DEPTH_TIME.md`, Section 4.3, proves
   equality of that already width-limited temporal DAG, at every fixed step
   vector, with repeated population Euler updates
   \(\theta_{s+1}=\theta_s+\varepsilon_s\mathbf g(\theta_s)\).  Despite the
   filename, this equality is an equality of the complete finite schedule,
   not merely of its cubic jet.
3. Only after those two fixed-step identifications does the audited theorem
   differentiate the population construction at the coalesced step vector.
   No finite-width derivative is used or sent through \(n\to\infty\).

The constant-activation branch causes no exception.  Normalization gives
\(\psi\equiv\pm1\), for which the finite-width expected output is exactly
\(N\eta\), so the fifth coefficient vanishes.  The nonconstant branch is
covered by the adaptive-conditioning theorem.

I found no reversed limit, hidden uniform-in-\(h\) assumption, or use of an
initialization derivative obtained before the width limit.

## 2. Reused adjoints and the generated \(C^5\) germ

The fragile identity is intrinsic Gaussian integration by parts for the
fixed isometry \(J_a\):

\[
 J_a^*\Phi(J_ac_1,\ldots,J_ac_q,\zeta)
 =\sum_{i=1}^q\mathbb E[\partial_i\Phi]c_i.
 \tag{A.3}
\]

It remains valid for singular and linearly dependent source lists because it
is obtained by testing against an arbitrary vector in the Hilbert space; no
Gram inverse occurs.  For moving sources, differentiating (A.3) gives

\[
 (J_a^*X)^{[\alpha]}
 =\sum_i\sum_{\beta\le\alpha}{\alpha\choose\beta}
 \rho_i^{[\alpha-\beta]}c_i^{[\beta]}.
 \tag{A.4}
\]

This is precisely the missing source-response convolution: derivatives of
the source vectors are present, rather than being silently frozen.  The
same argument applies to \(I_a^*\).  It also explains why an entrywise
finite response list is not being promoted to an ambient operator: the
operator \(J_a^*\) is fixed first, and the finite formula is only its
intrinsic action on the current cylindrical query.

The order-five extension terminates for each fixed \((L,N)\).  In the
truncated multi-step algebra

\[
 \mathbb R[\varepsilon_0,\ldots,\varepsilon_{N-1}]/\mathfrak m^6,
\]

there are finitely many chronology nodes and finitely many multiindices.
Raw actions, the response convolution (A.4), rank-one learned actions,
products, and the multiset Faà di Bruno formula all preserve every finite
\(L^p\) moment.  At a fixed derivative order, Hölder's inequality merely
requires a higher but still finite moment.  Bounded derivatives of \(\psi\)
and its linear-growth bound supply the required dominators.  This proves
actual generated directional derivatives, not ambient Fréchet
differentiability of the Nemytskii map on an \(L^2\) ball.

There are two independent treatments of singularity, and they are
consistent:

- the fixed-operator construction has no moving covariance square root, so
  its generated derivatives commute directly;
- `COMPILER_DEPTH_TIME.md`, Lemma 3.1, regularizes a positive-semidefinite
  covariance by \(C+\delta I\), applies Price differentiation, and passes
  \(\delta\downarrow0\) with explicit polynomial Gaussian dominators.

A response contributes one spatial derivative and five Price operations
contribute at most ten more.  The \(C^{12}\) hypothesis therefore covers
the compiler's largest activation derivative.  Since the exact
fixed-operator schedule and inverse-free schedule agree as functions before
differentiation, the two fifth jets agree by uniqueness.  I found no omitted
\(W\)/\(W^\top\) response term or singular-covariance inverse in this bridge.

## 3. Generated-tensor recurrence

Let \(Y_r(N)\) denote the coefficient of \(\eta^r\) in the population
Euler state.  Extracting coefficients from

\[
 \theta_{s+1}=\theta_s+\eta\mathbf g(\theta_s)
\]

gives exactly

\[
 Y_r(N)=\sum_{s=0}^{N-1}\sum_{k=1}^{r-1}{1\over k!}
 \sum_{j_1+\cdots+j_k=r-1}
 \mathbf G_k[Y_{j_1}(s),\ldots,Y_{j_k}(s)]
 \tag{A.5}
\]

for \(r\ge2\), with \(Y_1(N)=N\mathbf g(\theta_0)\).  The external Euler
factor accounts for the shift from \(r\) to \(r-1\), and the ordered
positive compositions together with \(1/k!\) are the correct Taylor
coefficient convention.

Inductively, \(Y_r(N)\) has degree at most \(r\): an (A.5) summand has
degree at most \(j_1+\cdots+j_k=r-1\) in \(s\), and finite summation raises
degree by at most one.  Applying the output tensors to compositions of
total order five therefore makes

\[
 A_5(N):=[\eta^5]F_{N,L}(\eta)
\]

a scalar polynomial of degree at most five with \(A_5(0)=0\).

This conclusion uses one autonomous population vector field on the fixed
population parameter space.  It would be false to infer it merely from five
unrelated horizon-specific Gaussian DAGs.  Here the required compatibility
is supplied by the fixed \(I_a+J_a^*\) realization and the exact schedule
intertwining, so the objection does not apply.

## 4. Interpolation and exact quartic cancellation

The compiler values have the correct coefficient normalization:

\[
 q_m=A_5(m)={\mathcal J^{\mathrm{PJ}}_{5,m,L}\over5!}.
\]

Since \(A_5\) has no constant term and degree at most five, its values at
\(m=1,\ldots,5\) determine all five coefficients.  Direct rational
multiplication verifies that the displayed matrix (4.2) is the inverse of
\(V_{md}=m^d\).  Thus

\[
 A_5(N)=\sum_{d=1}^5\gamma_dN^d.
\]

For the theorem's orientation
\(\Delta_{t,L}=F_{2t,L}(\eta)-F_{t,L}(2\eta)\),

\[
 [\eta^5]\Delta_{t,L}
 =\sum_{d=1}^5(2^d-2^5)\gamma_dt^d.
\]

The \(d=5\) term cancels identically.  This proves degree at most four
without an activation-specific cancellation.

The equivalent Newton calculation is also exact:

\[
 A_5(N)=\sum_{j=1}^5{N\choose j}\Theta_{5,j},
\qquad
 d_{5,j}(t)={2t\choose j}-32{t\choose j}.
\]

Expanding these five binomials reproduces every polynomial in (1.8a).  For
integer \(t\ge1\), direct checking gives

\[
 {|d_{5,j}(t)|\over t^4}
 \le 30,14,4,{2\over3},{4\over3}.
 \tag{A.6}
\]

For \(j=4\), the finitely many values \(t=1,\ldots,6\) and the inequality
\(|-4t^2+32t-45|\le4t^2\) for \(t\ge7\) close the only non-immediate case.

As a sign and normalization check, for \(L=1\) and \(\psi(x)=x\),

\[
 F_{N,1}(\eta)
 ={(1+\eta)^{2N}-(1-\eta)^{2N}\over2},
\]

so direct binomial extraction gives

\[
 [\eta^5]\Delta_{t,1}
 ={64\over3}t^4-56t^3+{140\over3}t^2-12t,
\]

exactly as stated.

## 5. The \(227/180\) envelope

Specializing the audited compiler recursion to horizon five gives

\[
 D=12,\qquad 8(5+1)=48,\qquad16(5+2)=112,
 \qquad M_{L,5}=11(L-1)\quad(L\ge2).
\]

Thus Section 5 of the theorem is exactly the \(N=5\) specialization of
the terminating recursion in `COMPILER_DEPTH_TIME.md`.  Horizon
monotonicity gives

\[
 |\mathcal J^{\mathrm{PJ}}_{5,m,L}|
 \le B_\psi^{E_{L,5}},\qquad1\le m\le5.
\]

Because \(q_0=0\), forward differences satisfy

\[
 |\Theta_{5,j}|
 \le {2^j-1\over120}B_\psi^{E_{L,5}}.
\]

Combining this with (A.6) gives

\[
 {1\over120}\left(
 30+14\cdot3+4\cdot7+{2\over3}\cdot15
 +{4\over3}\cdot31\right)
 ={227\over180}.
\]

Multiplication by \(5!=120\) gives
\(454B_\psi^{E_{L,5}}t^4/3\) for the fifth derivative.  I independently
checked the inverse Vandermonde matrix, its first four row \(\ell^1\)
norms

\[
 {887\over60},\quad{595\over24},\quad{335\over24},
 \quad{77\over24},
\]

and the weighted sum \(1524\).  Hence the alternative monomial constant
\(127/10\) is also correct.

All constants are noncircular.  The exact constants are finite rational
combinations of the explicitly compiled Gaussian activation integrals; the
coarse constant uses only \(M_\psi\), the fixed depth, and terminating
integer arithmetic.  None uses an output supremum, a trained-trajectory
norm, or an unknown continuity modulus.

## 6. Near-identity nonlinear class

For

\[
 \psi_{\alpha,\varphi}(x)
 ={x+\alpha\varphi(x)\over
   \|G+\alpha\varphi(G)\|_2},
\qquad
 \max_{0\le r\le12}\|\varphi^{(r)}\|_\infty\le R,
\]

the reverse triangle inequality gives

\[
 {3\over4}\le \|G+\alpha\varphi(G)\|_2\le{5\over4}
\]

when \(|\alpha|R\le1/4\).  Division by the lower bound yields

\[
 \sup_x{ |\psi(x)|\over1+|x|}\le{4\over3},\qquad
 \|\psi'\|_\infty\le{5\over3},\qquad
 \|\psi^{(r)}\|_\infty\le{1\over3}\quad(2\le r\le12).
\]

If \(\alpha\ne0\) and \(\varphi''\not\equiv0\), the normalized activation
is genuinely nonlinear.  Therefore \(M_\psi\le5/3\), \(B_\psi=4\), and
the uniform-over-activation-class coefficient bound (6.5) follows at
\(L=2\), \(L=3\), and indeed every separately fixed finite depth.

## 7. Counterexample search and scope stress test

I tested the following possible failure modes:

- constant activations: the fifth coefficient is zero;
- affine identity dynamics: direct binomial computation matches the theorem;
- singular or redundant source Grams: (A.3) is intrinsic and inverse-free;
- moving reused sources: (A.4) contains the missing derivatives of the
  source vectors;
- horizon-dependent derivatives: the common fixed population Euler map
  supplies compatible tensors independent of the selected horizon;
- a hidden factor \(5!\) or \(2^5\): both appear in the correct places;
- confusing local and uniform control: Section 7 explicitly excludes
  (A.2).

No counterexample survives these checks.

The last distinction is essential.  For example, a family of scalar germs

\[
 H_t(h)=\kappa_t h^3+q_t h^5+e^t h^7,
 \qquad |q_t|\lesssim t^4,
\]

has the desired polynomial fifth coefficient but can fail every useful
uniform remainder bound on \(|h|\asymp1/t\).  Hence the audited theorem is a
genuine positive polynomial result for the exact \(\eta^5\) coefficient,
but it cannot by itself establish well-behaved continuous-time dynamics.

## Final audit status

| Obligation | Status |
|---|---|
| Fixed-\(\eta\), width-first provenance | PASS |
| Reused \(W/W^\top\) response terms | PASS |
| Generated directional \(C^5\) germ | PASS |
| Singular Price identification | PASS |
| Euler coefficient recurrence | PASS |
| Degree-five-to-degree-four cancellation | PASS |
| Vandermonde/Newton arithmetic | PASS |
| \(227/180\) activation envelope | PASS |
| Genuine near-identity nonlinear class | PASS |
| Uniform nonzero-step \(t^4|\eta|^5\) remainder | **NOT CLAIMED / OPEN** |
