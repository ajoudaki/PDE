# Independent adversarial audit of the assembled depth--time theorem

> **SUPERSEDED HISTORICAL AUDIT.** The first compact-cubic bridge failed in
> `AUDIT_CUBIC.md`, so the pass reasoning below was correctly withdrawn.
> A later proof replaced that bridge by the fixed bounded operators
> \(W_{a,0}=I_a+J_a^*\). The replacement received a clean independent pass
> in `AUDIT_CUBIC_REAUDIT.md`, and `PROOF.md` now uses that replacement.
> Nothing below should be treated as an audit of the new operator bridge;
> the authoritative cubic audit is `AUDIT_CUBIC_REAUDIT.md`.

## Verdict

**WITHDRAWN.** This earlier verdict was invalidated by the independent
failure report summarized above.

I found no missing mathematical bridge in the chain

\[
 \text{finite network}
 \longrightarrow \text{fixed-}h\text{ Gaussian DAG}
 \longrightarrow C^5\text{ singular extension}
 \longrightarrow \text{cubic jet and fifth-order bound}.
\]

In particular, the finite-query intertwining in
`CUBIC_DEPTH_TIME.md` is strong enough for the compact coefficient
\(J_{\phi,L}\): it matches the complete cylindrical and learned actions,
not merely the rank-one learned terms, and it constructs all generated
directions in one extension-compatible finite Gaussian DAG before mixed
derivatives are commuted.

The assembled theorem should nevertheless not be released as written.
Most inline TeX delimiters in `PROOF.md` have been stripped, and two TeX
commands have been semantically damaged.  Also, `EVIDENCE_LEDGER.md` still
labels bridges that the supplements now prove as “under construction” or
“open.”  These are documentation defects, not defects in the theorem or
its constants, but the first directly violates the requirement that the
equations render correctly.

## 1. Dependency audit

Every main claim has a matching proved supplement:

| Main claim | Supplying result | Audit conclusion |
|---|---|---|
| exact network, scaling, and past-time learned terms (1.1)--(1.8) | `WIDTH_DEPTH_TIME.md`, Sections 2--3 | supplied exactly |
| pointwise fixed-\(h\) convergence of expected outputs | `WIDTH_DEPTH_TIME.md`, Theorem 1.3 and Sections 4--10 | supplied, including reused rows and columns |
| inverse-free operator DAG (2.3)--(2.7) | `WIDTH_DEPTH_TIME.md`, Sections 5--6 | same DAG and response conventions |
| \(C^5\) regularity at the singular covariance | `COMPILER_DEPTH_TIME.md`, Lemma 3.1 and Section 4 | supplied on \([-1,1]\) |
| explicit fifth derivative bound \(B_\phi^{E_{L,N}}\) | `COMPILER_DEPTH_TIME.md`, Lemma 5.1 and (5.12)--(5.14) | supplied with terminating integer recursions |
| finite-query gradient/Euler intertwining through order three | `CUBIC_DEPTH_TIME.md`, Sections 3--5 | supplied without a global Gaussian operator |
| compact activation recursion (T.7)--(T.13) | `CUBIC_DEPTH_TIME.md`, Sections 6--8 | formulas agree term for term |
| time polynomial and doubling coefficient | `CUBIC_DEPTH_TIME.md`, (1.3)--(1.6) and Section 5 | supplied with the stated sign and factors |
| parity, Taylor remainder, and epsilon radius | `COMPILER_DEPTH_TIME.md`, Sections 7--8, combined with the compact cubic law | supplied |

There is no circular use of an output derivative in the constants.  The
compiler first constructs the Price jets and their activation envelopes;
regularity identifies them with derivatives afterward.  The compact cubic
recursion is independently expressed through nine one-dimensional Gaussian
activation moments.

## 2. Exact finite-width and width-first checks

For

\[
 f_{n,L}=n^{-1}a^T X_L,
 \qquad Z_\ell=n^{-1/2}W_\ell X_{\ell-1},
\]

direct differentiation gives

\[
 \nabla_{W_\ell}f_{n,L}=n^{-3/2}D_\ell X_{\ell-1}^T,
 \qquad \nabla_uf_{n,L}=n^{-1}D_1.
\]

Thus \(\theta^+=\theta+hn\nabla f\) gives exactly (1.4)--(1.6).
Summing the matrix updates gives (1.7)--(1.8), with \(r<s\); hence every
gradient is recomputed before the next simultaneous update and no
current-time term has been inserted.

The chronology has

\[
 N\,2(L-1)+(L-1)=(2N+1)(L-1)
\]

matrix actions.  `WIDTH_DEPTH_TIME.md` conditions on the global predictable
filtration, so a current query may depend on every earlier forward or
transpose action of the same matrix and on the other matrices.  Its
rectangular cross block before the backward call includes the current row
action.  The two Gaussian integration-by-parts cancellations therefore
retain the dependence of \(X_{\ell-1}^s\) on the reused column through the
\(\rho\) response.

The rank proof covers all branches:

1. a nonlinear \(\phi'\) opens the top cotangent Schur complement with the
   fresh current forward innovation;
2. an affine nonconstant activation opens it through the explicit fresh
   term \(hp^2\tau E\);
3. a constant activation is treated without an inverse and gives
   \(F_{N,L}(h)=Nh\).

The stopped raw/extended/ideal coupling contains every Gram and cross
moment needed by the regressions.  Its finite moment tower closes the
field, coefficient, stopping-removal, and terminal uniform-integrability
estimates.  Therefore the supplement proves convergence of expectations,
not only convergence in probability.

This identification is pointwise for every fixed \(h\ne0\).  The compiler
is applied only after this pointwise identification.  At \(h=0\), both the
finite-width expected output and the inverse-free extension equal zero.
Consequently the assembled proof respects the order

\[
 n\to\infty\text{ at fixed }h,
 \qquad\text{then }h\to0.
\]

## 3. Audit of the finite-query intertwining

The compact coefficient would not follow merely from the formal claim that
the population dynamics is gradient ascent.  The supplement supplies the
needed stronger statement.

For each reused connector, its row queries live in the lower coordinate
space and its cotangents live in the upper coordinate space.  The two
isonormal source families are independent.  Gaussian integration by parts
then proves the inverse-free adjoint identity (4.1) even for a singular
Gram.  The common perturbation construction includes every base query and
every query derivative needed for

\[
 \mathbf g,quad D\mathbf g[\mathbf g],\quad
 D\mathbf g[D\mathbf g[\mathbf g]],\quad
 D^2\mathbf g[\mathbf g,\mathbf g]
\]

in one finite source list.  The list is finite, its covariance is an
ordinary positive-semidefinite Gram, and extension by another generated
direction leaves all old covariance subvectors and response derivatives
unchanged.  Thus all mixed derivatives used in (4.2)--(4.8) belong to one
common scalar \(C^3\) DAG; no incompatible covariance square roots are
being compared.

Most importantly, (4.10) and (4.11) match both parts of an actual reused
matrix action:

\[
 \mathscr W_{a,0}[X]+\mathcal K_{a,s}X
\quad\text{and}\quad
 \mathscr W_{a,0}^{!*}[D]+\mathcal K_{a,s}^*D.
\]

The first terms contain the raw Gaussian source and every adaptive response;
the second terms contain the accumulated rank-one updates.  The induction
over time and layer therefore establishes the Euler relation through the
three required derivatives.  This is enough to differentiate
\(F_{N,L}\) through order three and obtain

\[
 F_{N,L}^{(3)}(0)
 =\frac{N(4N^2-3N+1)}2\mathsf S_{\phi,L}
 +2N(N-1)(2N-1)\mathsf H_{\phi,L}.
\]

The coefficient algebra is correct:

\[
 8\mathcal A_t-\mathcal A_{2t}=-3t(2t-1),
 \qquad
 8\mathcal B_t-\mathcal B_{2t}=-12t(2t-1).
\]

After division by \(3!=6\), this gives

\[
 \kappa_{\phi,L,t}
 =-\frac{t(2t-1)}2
   (\mathsf S_{\phi,L}+4\mathsf H_{\phi,L}),
\]

with the sign in (T.23)--(T.24).

## 4. Audit of the activation recursion

The recursion in (T.7)--(T.13) is identical to (6.3)--(6.9) of the cubic
supplement.  The local contractions check as follows.

The first straight-path preactivation variation is

\[
 Z_a^{[1]}=E_{a1}+\Theta_{a-1}R_a\phi'(Z_a),
 \qquad \mathbb E E_{a1}^2=V_{a-1}.
\]

Its square gives (T.7).  The scalar second derivative and one-dimensional
Gaussian integration by parts give (T.8).  Differentiating the third
activation variation with respect to the local reverse carrier produces
the four terms in (T.9); none is imported from an initialization MFP jet.

For the reverse pass,

\[
 \widetilde R_a=B_a+\gamma_{a+1}\phi(Z_a),
\]

and

\[
 \widetilde D_a
 =R_a\phi''(Z_a)Z_a^{[1]}
  +\phi'(Z_a)\widetilde R_a.
\]

The five terms in \(\mathbb E\widetilde D_a^2\) are exactly the five
terms in (T.10), while differentiation in the base forward innovation plus
the learned transpose term gives (T.11).  Orthogonality of the parameter
blocks then gives (T.13).  This verifies the compact recursion independently
of the time-polynomial simplification.

The supplied exact-arithmetic falsification script also passes the
depth-two reduction, the identity activation for depths \(1\) through
\(20\), and the time-polynomial identities.  This script is corroborating
evidence only; the preceding nodewise argument supplies the proof.

## 5. Explicit constants, depth three, and the Taylor factors

All recursions defining \(R_{N,k},c_{N,q},C_N,\nu_N,\alpha_N,p_N,r_N\)
terminate at displayed finite upper indices.  The call exponent solves

\[
 a_{m+1}=r_N+p_Na_m,qquad a_0=2L,
\]

after \(M_{L,N}\) calls, so

\[
 E_{L,N}=2L p_N^{M_{L,N}}
 +r_N\frac{p_N^{M_{L,N}}-1}{p_N-1}.
\]

Here \(p_N>1\), and the monotonicity proof gives
\(E_{L,t}\le E_{L,2t}\).

For \(L=3\) and horizon \(N=2t\),

\[
 M_{3,2t}=(4t+1)(3-1)=8t+2,
\]

so (T.30) is correct.  Also

\[
 \pi_2=d^2,qquad \pi_3=d,
\]

which verifies every term in the depth-three specialization (T.29).  At
\(t=2\), \(t(2t-1)/2=3\), giving the sign and coefficient in (T.32).

For

\[
 D_{t,L}(\eta)=F_{t,L}(2\eta)-F_{2t,L}(\eta),
\]

the chain rule gives the fifth-derivative factor \(2^5=32\), not \(16\)
or \(64\).  On \(|\eta|\le1/2\), both Taylor segments remain in
\([-1,1]\), and

\[
 \sup|D_{t,L}^{(5)}|
 \le32B_\phi^{E_{L,t}}+B_\phi^{E_{L,2t}}
 \le33B_\phi^{E_{L,2t}}.
\]

The fourth-degree integral remainder contributes \(1/5!=1/120\).
Since \(33/120<1\), the coefficient in (T.23) is indeed
\(B_\phi^{E_{L,2t}}\), with no missing numerical prefactor.

The radius (T.26) is also correct:

\[
 B_\phi^{E_{L,2t}}|\eta|^2
 \le \frac{B_\phi^{E_{L,2t}}}
 {1+B_\phi^{E_{L,2t}}}\,\varepsilon
 \le\varepsilon.
\]

The compiler also records the smaller activation-base radius
\(h_\phi^{E_{L,2t}}\), with \(h_\phi=(2B_\phi)^{-1}\).  This does not
conflict with the main theorem: compiler equation (8.3) already proves the
remainder on the stronger universal interval \(|\eta|\le1/2\), which the
main theorem uses.

## 6. Exact repairs required before release

### Repair A: restore inline TeX in `PROOF.md`

The file has lost essentially all `\\(` and `\\)` inline delimiters.  Two
commands have also lost their backslashes.  For example, the opening must
read

```text
Let \(L,t\ge1\) be integers. All \(L\) hidden layers have width \(n\),
the input is the scalar \(1\), and there are no biases. Let
\(G\sim N(0,1)\), and assume ...
```

not

```text
Let (L,tge1) be integers. All (L) hidden layers have width (n), ...
(Gsim N(0,1)), ...
```

The same repair is required throughout the prose, including such instances
as `fixed (h)`, `If (d>0)`, `for (a=1,\ldots,L)`, `(eta)` on the Taylor
interval, and `(phi\equiv\pm1)` in the constant branch.  This should be
done by restoring the original inline delimiters, not by globally replacing
ordinary English parentheses.  Re-run a render check afterward.  No
displayed formula needs a mathematical change.

### Repair B: supersede the stale evidence statuses

`EVIDENCE_LEDGER.md` predates the completed supplements.  Its status column
must be updated as follows:

* E1--E7: `established`, with the relevant sections of
  `WIDTH_DEPTH_TIME.md`, `COMPILER_DEPTH_TIME.md`, and
  `CUBIC_DEPTH_TIME.md` cited;
* E8: `established by the finite-query intertwining and nodewise recursion
  in CUBIC_DEPTH_TIME.md, Sections 3--7`;
* E9: `established by COMPILER_DEPTH_TIME.md, Section 5`;
* E10: leave `open`, with the linear-activation lower-power obstruction.

After Repairs A and B, the assembled theorem has no remaining defect found
by this audit and merits an unconditional **PASS** for every fixed finite
pair \((L,t)\).  The explicitly excluded uniform-in-time
\(t^4|\eta|^5\) theorem remains open, exactly as Section 6 of `PROOF.md`
states.
