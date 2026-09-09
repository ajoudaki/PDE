# Independent hostile audit: depth--time compiler

## Verdict

**PASS, with two non-substantive presentation corrections.**  The analytic
compiler in `COMPILER_DEPTH_TIME.md` proves the claims it assigns to itself:
for every fixed finite pair \((L,N)\), the inverse-free Gaussian DAG is
\(C^5\) through the singular covariance at \(h=0\), its cubic jet is given by
a terminating activation-integral recursion, and its fifth derivative has
the explicit shared-base bound

\[
 \overline{\mathcal J}_5(F_{N,L})\le B_\phi^{E_{L,N}}.
\]

This verdict is only for the analytic compiler.  It does not promote the
separate finite-width identification; Section 10 correctly keeps that bridge
outside the compiler.

The two corrections are:

1. Equation (8.5a) contains the TeX typo
   `p_{2t}^{,8t+2}`.  It must read
   \(p_{2t}^{8t+2}\).  The exponent itself is correct because
   \(M_{3,2t}=(4t+1)(3-1)=8t+2\).
2. The prose after (2.3) lists the four nonterminal call dimensions and the
   terminal interior dimension but does not explicitly list the terminal top
   dimension \(N+2\).  This omission is harmless: \(N+2\le2N+2=D_N\).

Neither correction changes a definition, inequality, or proof.

Both presentation corrections were applied after this audit; the audited
formulas and bounds are unchanged.

## 1. Chronology, call count, and dimensions

At a nonterminal time \(s\), the call counts are

\[
 (L-2)+1+(L-2)+1=2(L-1):
\]

the interior forward calls, top call, interior backward calls, and bottom
call.  The terminal sweep has \((L-2)+1=L-1\) calls.  Hence

\[
 2N(L-1)+(L-1)=(2N+1)(L-1),
\]

exactly as in (2.3).  For \(L=2\), both interior ranges are empty and the
same formula gives the top/bottom chronology correctly.  For \(L=1\), no
matrix call exists and the one scalar Gaussian call in (2.5) is correctly
handled separately.

The dimensions are

\[
 \begin{array}{c|c}
 \text{call}&\text{dimension}\\ \hline
 \text{interior forward at }s&(s+1)+s=2s+1\\
 \text{top at }s&1+(s+1)=s+2\\
 \text{interior backward at }s&(s+1)+(s+1)=2s+2\\
 \text{bottom at }s&1+(s+1)=s+2\\
 \text{terminal interior}&(N+1)+N=2N+1\\
 \text{terminal top}&1+(N+1)=N+2.
 \end{array}
\]

All are at most \(D_N=2N+2\).  The off-by-one histories are also correct:
an interior terminal/forward reconstruction needs \(\xi_{\ell,0:s}\) but
only \(\chi_{\ell+1,0:s-1}\), whereas the backward reconstruction at a
nonterminal time needs both blocks through \(s\).  At terminal time no new
cotangent is required.  Thus the construction in Section 2 is acyclic.

## 2. Singular Price lemma

Lemma 3.1 has the right derivative budget.  After \(r\) Price operations,
every term is a coefficient made from derivatives of \(C\) through order
\(r\), times a derivative

\[
 \partial_h^jD_x^\alpha\psi,
 \qquad j+\left\lceil |\alpha|/2\right\rceil\le r.
\]

Consequently \(C\in C^5\) and the mixed derivatives stated in (3.1) are
exactly sufficient for \(r\le5\); neither a sixth covariance derivative nor
an eleventh spatial derivative is used.

The regularization argument also survives rank changes.  For
\(C_\epsilon=C+\epsilon I\), ordinary Price differentiation applies, while

\[
 \sup_h\|C_\epsilon(h)^{1/2}-C(h)^{1/2}\|_{\rm op}
 \le\sqrt\epsilon.
\]

Compact-set convergence plus the common polynomial envelope gives uniform
integrability of every one of the finitely many derived integrands.  Their
expectations therefore converge uniformly in \(h\).  Applying the integrated
derivative identity successively for orders zero through five identifies the
limit as a \(C^5\) function with (3.2).  This closes the point sometimes
missed by merely writing the formal Price operator at a singular Gram.

## 3. Exact envelope recursion

Differentiating

\[
 \Psi_{r+1}=\partial_h\Psi_r+\tfrac12C':D^2\Psi_r
\]

by \(\partial_h^jD^q\) gives

\[
 \partial_h^{j+1}D^q\Psi_r
 +\frac12\sum_{a=0}^j\binom ja
 C^{(a+1)}:D^{q+2}\partial_h^{j-a}\Psi_r.
\]

This is precisely (4.8).  Its strict guard
\(r+j+\lceil q/2\rceil<5\) ensures that every requested child lies in the
base domain (4.7), and the recursion terminates after at most five Price
levels.  The sums over ordered multiindices and covariance pairs are
upper-bounded by the \(\oplus\) aggregation and the entrywise covariance
norm in (4.6); no sign or multiplicity is discarded.

For \(hQ\), Leibniz gives

\[
 (hQ)^{(j)}=hQ^{(j)}+jQ^{(j-1)},
\]

so (4.12) is correct on \(|h|\le1\), including \(j=0\).  The same check
applies to \(hK\).  Previous scalar jets are used only through the tokens in
(4.4), and the guard never differentiates a fifth token.

## 4. The \(C^{12}\) budget

An undifferentiated state/Gram/output integrand contains activation atoms of
order at most one.  A response integrand first applies one ambient source
derivative, raising the maximal atom order to two.  A reachable Price term
then applies at most

\[
 2r+j+q\le10
\]

additional ordinary formal derivatives.  Thus the worst response atom is
\(\phi^{(12)}\), and no \(\phi^{(13)}\) is requested.  The linear-growth
rule for \(\phi\), bounded rules for \(\phi^{(r)}\), and finite syntax give
the common polynomial domination required by Lemma 3.1.

## 5. One-call syntax and multiplicity majorant

The raw-history bound in (5.1) is conservative but valid.  Each raw
assignment is a sum of at most \(2N+3\) monomials, every monomial has at most
three previously built factors, and at most \(4(N+1)\) state assignments are
needed in a matrix call.  The \(8(N+1)\) iterations therefore also cover the
slightly longer \(L=1\) scalar unrolling.

After integer coefficients, covariance contractions, and ordered
multiindices are expanded as stipulated, the structural estimate

\[
 |\partial e|\le2(|e|+1)^2
\]

absorbs one formal differentiation.  The operation count is at most ten
mixed-derivative levels, one response derivative, one multiindex
aggregation, five Price levels, and two assembly levels: nineteen operations,
strictly below the twenty-four iterations in (5.3).  At a Price level the
number of new summands is bounded by

\[
 1+D^2\sum_{a=0}^j\binom ja\le1+32D^2,
\]

and the factor \(64(D+1)^{10}\) also absorbs the one-time \(D^{10}\)
multiindex aggregation.  Thus no dimension, binomial, or contraction
multiplicity is hidden in a leaf.

With syntax size, token-leaf count, and polynomial degree at most \(C_N\),
the envelope coefficient is bounded by

\[
 (2B_\phi)^{C_N}S^{C_N}.
\]

If each covariance entry is at most \(S\), its entrywise norm is at most
\((D+1)^2S\), and

\[
 \mu_{d,C_N}((D+1)^2S)
 \le S^{C_N/2}\nu_N.
\]

Since \(S\ge2\), \(B_\phi\ge4\), and
\(2^{C_N}\nu_N\le B_\phi^{\alpha_N}\), this yields exactly
\(B_\phi^{r_N}S^{p_N}\).  The proof of Lemma 5.1 therefore closes with its
stated exponents.

## 6. Exponent and horizon monotonicity

At initialization, \(d_\phi\le M_\phi^2\le B_\phi^2\), so all variances
\(d_\phi^j\), \(0\le j\le L\), and the unit tokens are bounded by
\(S_0=B_\phi^{2L}\).  Iterating the one-call map through exactly
\(M_{L,N}\) calls gives

\[
 a_{m+1}=r_N+p_Na_m,qquad a_0=2L,
\]

and hence

\[
 a_{M_{L,N}}
 =2L p_N^{M_{L,N}}
  +r_N\frac{p_N^{M_{L,N}}-1}{p_N-1}=E_{L,N}.
\]

Here \(p_N>1\), so the denominator is harmless.  Increasing \(N\)
increases the multiplier and number of iterations in (5.1), then the
dimension/multiplier in (5.3), and hence \(C_N,\nu_N,\alpha_N,p_N,r_N\).
It also increases \(M_{L,N}\) for \(L\ge2\), while \(M_{1,N}=1\).
Therefore the proof of Lemma 5.2 correctly establishes
\(E_{L,N+1}\ge E_{L,N}\).

## 7. Taylor factors and radius

Oddness gives the vanishing constant, quadratic, and quartic jets.  The
clock identity gives \(F'_{N,L}(0)=N\Theta_L\), so the two linear terms are
both \(2t\Theta_L\).  Fourth-degree Taylor expansion with fifth-derivative
remainder therefore gives factors

\[
 \frac{(2\eta)^5}{5!}=\frac{32}{120}\eta^5,
 \qquad
 \frac{\eta^5}{5!}=\frac1{120}\eta^5.
\]

The cubic coefficient is correspondingly

\[
 \frac{8\mathcal J_3(F_{t,L})-\mathcal J_3(F_{2t,L})}{6}.
\]

The domain \(|\eta|\le1/2\) keeps both Taylor segments in \([-1,1]\).
Monotonicity and \(33/120<1\) yield (8.3).  Since
\(B_\phi\ge4\), \(h_\phi=(2B_\phi)^{-1}\le1/8\), and
\(E_{L,2t}\ge1\), the smaller radius \(h_\phi^{E_{L,2t}}\) is valid.
Finally,

\[
 B_\phi^{E_{L,2t}}|\eta|^5
 \le \frac{B_\phi^{E_{L,2t}}}{1+B_\phi^{E_{L,2t}}}
       \varepsilon|\eta|^3
 <\varepsilon|\eta|^3,
\]

which proves (8.6)--(8.7) with the displayed explicit radius.

## 8. Non-circularity

The exact jets in Section 6 are triangular in the chronology of Section 2.
For a new call, all \(S^{[j]}\) values belong to earlier scalar nodes; five
applications of \(\mathcal P_C\) then define the new numbers
\(\mathcal J_r(T)\).  Lemma 3.1 identifies those already-defined numbers
with derivatives only afterward.  Likewise, the remainder constant is
constructed from \(M_\phi\), explicit integer recursions, Gaussian moments,
and the finite call count.  It contains no supremum of an output, trained
trajectory, continuity modulus, or opposite-order finite-width Taylor
limit.

The compiler also states its logical boundary correctly: its quantitative
conclusion applies to the actual width-first network only in conjunction
with the independent fixed-\(h\) identification theorem.
