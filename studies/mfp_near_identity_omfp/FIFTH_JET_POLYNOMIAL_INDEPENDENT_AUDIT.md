# Independent audit: fifth-jet polynomial theorem

Date: 25 August 2026.

## Verdict

**PASS for the exact local fifth-coefficient theorem, with one wording
correction and several notation repairs.**  The argument proves, after the
width limit and for every separately fixed depth (L), that

\[
 [\eta^5]\{F_{2t,L}(\eta)-F_{t,L}(2\eta)\}
\]

is an activation-defined polynomial of degree at most four in (t).  The
Vandermonde constants, the factor (5!=120), the chain factor (2^5=32),
and the envelope (127B_\psi^{E_{L,5}}/10) are correct.  The theorem does
not prove a uniform finite-(\eta) remainder, and the draft says so.

## 1. Provenance and limit order

The proof uses the valid order

\[
 n\to\infty\text{ at fixed finite }(N,L,\eta),
 \qquad\text{then }\eta\to0.
\]

The required source chain is:

1. `temporary_depth_time_doubling/WIDTH_DEPTH_TIME.md` identifies the actual
   finite-width network with the inverse-free population DAG at each fixed
   nonzero step.
2. `temporary_depth_time_doubling/COMPILER_DEPTH_TIME.md`, Sections 3--6,
   proves (C^5) regularity of that already width-limited DAG through the
   singular coalesced covariance and constructs
   \(\mathcal J^{\rm PJ}_{5,N,L}\) before identifying it with
   (F_{N,L}^{(5)}(0)).
3. `temporary_depth_time_doubling/CUBIC_DEPTH_TIME.md`, (4.1)--(4.6),
   realizes every finite population schedule as repeated autonomous Euler
   updates with fixed raw operators (I+J^*).
4. `temporary_general_depth_general_time_stepdoubling_bound/
   CUBIC_MARKED_BRIDGE.md`, Section 8, extends the finite marked
   temporal/static construction to order five and proves that
   (N\mapsto F_{N,L}^{(5)}(0)) has degree at most five.

No finite-width derivative is passed through the width limit.  The only new
regularity used in Lemma 2.1 of the theorem is fixed-horizon generated
directional (C^5) regularity.  Its finite (L^p)-ladder argument is
compatible with the existing marked proof: at fixed (N) and total order
five there are only finitely many generated fields and source marks, so
Holder closes after choosing sufficiently high finite moments.  This does
not supply, and does not claim, a bound uniform in (N).

To prevent confusion with the false ambient Frechet route, every occurrence
of (D^k\mathbf g(\theta_0)) and (D^k\mathcal F(\theta_0)) in (3.3)--(3.4)
should explicitly mean the generated mixed coefficient tensors from Lemma
2.1, not Frechet derivatives on an (L^2) neighborhood.

## 2. Coefficient convention and sign

Let (A_5(N)=[\eta^5]F_{N,L}(\eta)).  Since

\[
 F_{m,L}^{(5)}(0)=\mathcal J^{\rm PJ}_{5,m,L},
\]

the data interpolated by the Vandermonde system are correctly

\[
 A_5(m)=\mathcal J^{\rm PJ}_{5,m,L}/120.
\]

Thus the (1/5!) in (1.6) is necessary and correct.  Because
(A_5(0)=0), its five values at (m=1,\ldots,5) determine its five
nonconstant monomial coefficients.  For

\[
 \Delta_{t,L}=F_{2t,L}(\eta)-F_{t,L}(2\eta),
\]

one obtains

\[
 [\eta^5]\Delta_{t,L}
 =\sum_{d=1}^5(2^d-32)\gamma_dt^d.
\]

The (d=5) term vanishes.  The sign is therefore correct for this
orientation.  Every cubic and fifth coefficient is negated in the convention
(F_{t,L}(2\eta)-F_{2t,L}(\eta)) used in
`temporary_depth_time_doubling/PROOF.md`.

As a concrete check, at (L=2,psi(x)=x), the theorem gives the reverse of
the audited polynomial in
`temporary_general_time_doubling/LINEAR_ACTIVATION_AUDIT.md`, (3.2):

\[
 [\eta^5]\Delta_{t,2}
 ={2452\over3}t^4-1896t^3+{4403\over3}t^2-369t.
\]

## 3. Gaussian-integral and envelope audit

The inverse Vandermonde matrix (4.2) is exact.  Its first four row
(\ell^1)-norms are

\[
 {887\over60},\quad {595\over24},\quad
 {335\over24},\quad {77\over24},
\]

and

\[
 \sum_{d=1}^4|2^d-32|\,
 \|(V^{-1})_{d,\cdot}\|_1=1524.
\]

The specialization of the compiler recursion to horizon five is also
correct:

\[
 D_5=12,quad8(5+1)=48,quad16(5+2)=112,quad
 M_{L,5}=11(L-1)\quad(L\ge2).
\]

Hence

\[
 |\mathcal J^{\rm PJ}_{5,m,L}|
 \le B_\psi^{E_{L,5}},\qquad1\le m\le5,
\]

implies

\[
 K_{\psi,L}\le{1524\over120}B_\psi^{E_{L,5}}
 ={127\over10}B_\psi^{E_{L,5}},
\]

and multiplying by (120) gives the stated bound on
(|\Delta_{t,L}^{(5)}(0)|).

The exact constants \(\gamma_d\) and (K_{\psi,L}) are finite rational
combinations of signed Gaussian activation integrals.  However, the sentence
after (1.13) overstates the provenance of **(1.12)**: its coarse base

\[
 B_\psi=\max\{4,M_\psi\}
\]

uses global weighted derivative suprema, not only Gaussian integrals.  It
should say: “(1.6) and (1.9) use Gaussian activation integrals; (1.12) uses
the explicit weighted activation envelope.”  This does not affect the
inequality.

For the residual class, (6.4) correctly gives
(M_{\psi_{\alpha,\varphi}}\le5/3), hence (B=4), uniformly for
(0<|\alpha|R\le1/4).  The nonlinear-class conclusion is therefore valid
at both (L=2) and (L=3), indeed at every separately fixed depth.

## 4. Exact claim boundary

The result is

\[
 \Delta_{t,L}(\eta)
 =[\eta^3]\Delta_{t,L}\,\eta^3
  +\beta_{t,\psi,L}\eta^5+o_t(\eta^5),
 \qquad |\beta_{t,\psi,L}|\le C_{\psi,L}t^4.
\]

It gives no uniform control of (o_t(\eta^5)) on
(|\eta|\le\rho/t).  Accordingly it does not close the generated-core or
all-source estimate that remains open for nonlinear activations at
(L=2,3).  The phrase “sharp universal power” is justified as a
class-wide lower bound by the identity examples (already at (L=1) and
(L=2)); it should not be read as saying that every activation and every
depth has a nonzero quartic coefficient.

## 5. Presentation repairs

The following are typographical, not mathematical:

- (1.2): `M_\psi=max` should be `M_\psi=\max`;
- prose near lines 26 and 257: raw `eta` should be `\(\eta\)`;
- prose near line 387: raw `ell^1` should be `\(\ell^1\)`;
- the inequality after (5.9): `K_{\psi,L}le` should be
  `K_{\psi,L}\le`;
- (7.1): `Delta_{t,L}` should be `\Delta_{t,L}`.

Subject to these wording and rendering corrections, no coefficient, sign,
limit-order, or envelope overclaim remains.

## Post-audit revision

The primary theorem has now applied all wording and rendering repairs,
replaced ambient derivative notation by the generated tensors
\(\mathbf G_k,\mathcal T_k\), and added the full marked adjoint convolution.
It also incorporates the independently derived Newton-basis estimate

\[
 |[\eta^5]\Delta_{t,L}|
 \le {227\over180}B_\psi^{E_{L,5}}t^4,
\]

which is sharper than the valid monomial-basis constant audited above.
