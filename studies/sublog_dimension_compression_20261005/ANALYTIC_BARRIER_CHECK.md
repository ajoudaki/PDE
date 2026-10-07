# Independent check of `ANALYTIC_BARRIER_PROOF.md`

## Verdict: FAIL as written; repairable

The dimension count, endpoint-zero construction, Borsuk--Ulam step, and final
substitution are correct once the analytic domains and representation maps are
made precise.  The theorem as stated is nevertheless false for an arbitrary
"nondegenerate complex neighborhood," and the displayed analytic embedding is
asserted rather than established.  The result is a static lower bound for a
continuous encoder, not yet a lower bound for an explicitly stable autonomous
model or for reachable dense-network trajectories.

## Line-by-line audit

1. **Dimensions and endpoint modes (lines 43--59): PASS.**  On
   (S_{sqrt d}^{d-1}), the real spherical harmonics of degrees at most (p)
   have dimension
   
   \[
   H_{p,d}=\binom{p+d-1}{d-1}+\binom{p+d-2}{d-1}
   \asymp_d p^{d-1}.
   \]
   
   The map (Q\mapsto s(1-s)Q), with (deg Q<p), is injective and has
   dimension (p).  Since (s=e^{-t}), its factors vanish at (t=0)
   ((s=1)) and (t=\infty) ((s=0)).  Thus the tensor space has
   (N_p=pH_{p,d}\asymp_d p^d).  The radius-(\sqrt d) sphere changes no
   dimension count.

2. **Analytic-ball embedding (lines 16--20 and 61--68): FAIL as stated.**
   A complex neighborhood need not be bounded.  For example, if the time
   neighborhood is all of (\mathbb C), bounded entire dependence on (s) is
   constant; imposing both endpoint zeros leaves only zero dependence, so the
   claimed polynomial ball is not contained in the analytic unit ball.  The
   same issue is visible directly: nonconstant polynomials have infinite
   supremum on an unbounded neighborhood.

   Replace "any nondegenerate complex neighborhood" by fixed bounded complex
   domains (U_s\subset\mathbb C) and (U_x\subset\mathbb C^d) containing
   ([0,1]) and (S_{sqrt d}^{d-1}), respectively (fixed positive-radius
   tubular neighborhoods are sufficient).  They and the analytic norm bound
   must be independent of (p), (\epsilon), and (n).  Then state and prove
   the needed evaluation estimate for the tensor space (V_p):
   
   \[
   \lVert g\rVert_{H^\infty(U_s\times U_x)}
   \le A e^{Bp}\lVert g\rVert_{L^2([0,1]\times S_{sqrt d}^{d-1})},
   \tag{A}
   \]
   
   where (A,B) depend only on the two domains and (d).  An orthonormal
   tensor basis, Cauchy--Schwarz, the complex polynomial evaluation bound in
   (s), and the spherical-harmonic addition formula give (A); polynomial
   factors in (p) can then be absorbed into (e^{Bp}).  Equation (A), not an
   unspecified finite-dimensional norm comparison, yields the embedded radius
   (r_p=A^{-1}e^{-Bp}).  Every element still has both endpoint zeros because
   of the common factor (s(1-s)).

3. **Norm comparison (lines 61 and 73--76): PASS after definition.**  Define
   explicitly
   
   \[
   \lVert g\rVert_2^2=\int_0^1\int_{S_{sqrt d}^{d-1}}
   |g(s,x)|^2\,d\sigma(x)\,ds,
   \]
   
   with (\sigma) probability surface measure.  This must be (ds), not
   (dt); there is no normalized Lebesgue measure on ([0,\infty)).  The
   change (s=e^{-t}) preserves the supremum, and
   (\lVert h\rVert_\infty\ge\lVert h\rVert_2).

4. **Borsuk--Ulam (lines 70--76): PASS after specifying the model.**  Let one
   fixed deterministic encoder and decoder be
   
   \[
   E:(\mathcal A,\lVert\cdot\rVert_\infty)\to\mathbb R^q,
   \qquad D:\mathbb R^q\to\{​\text{trajectories}​\}.
   \]
   
   Require (E) to be continuous in the displayed real-domain supremum norm;
   (D) need not be continuous for this argument.  All function-dependent
   decoder, dictionary, or initialization parameters must be part of the
   (q) coordinates, so that equal codes really do give the same
   reconstruction.  On the (L^2)-sphere of radius (r_p) in the real
   (N_p)-dimensional space (V_p), Borsuk--Ulam applies whenever
   (q\le N_p-1) and gives (g,-g) with (E(g)=E(-g)).  Their distance is
   (2r_p), so at least one of (D(E(g))) and (D(E(-g))) has (L^2), hence
   supremum, error at least (r_p).  Thus error (<r_p) forces (q\ge N_p).

   Mere continuity is a topological hypothesis, not a quantitative
   conditioning or Lipschitz guarantee.  Nor does this statement define an
   autonomous flow.  It may be called a continuous-encoder static lower bound.
   To advertise an autonomous stable representation result, the theorem must
   additionally define a (q)-state well-posed autonomous flow, its fixed
   output map, and a continuous (or quantitatively stable) initialization map;
   it must also count every fixed or data-dependent retained coordinate.

5. **Choice of (p) and target substitution (lines 78--82): PASS.**  With
   (r_p=A^{-1}e^{-Bp}), choose the largest integer satisfying
   (r_p>\epsilon).  For sufficiently small (\epsilon), this gives
   (p\ge c\log(1/\epsilon)), and hence
   (q\ge c_{d,U_s,U_x}[\log(1/\epsilon)]^d).  At
   
   \[
   \epsilon_n=n^{-1/2}[\log(en)]^{-5/2},
   \qquad
   \log(1/\epsilon_n)=\tfrac12\log n+	frac52\log\log(en)
   \ge\tfrac12\log n,
   \]
   
   so (q\ge c'_{d,U_s,U_x}(\log n)^d) for all sufficiently large (n).
   The constant should be renamed after this substitution.

## Required claim corrections

- Delete **"sharp"** from the title unless a matching upper bound in the same
  representation model is supplied.
- Qualify lines 108--109: the proof obstructs uniform compression of a **full
  (H^\infty) unit ball on fixed bounded neighborhoods**.  Individual
  analyticity, an (n)-dependent/shrinking complex radius, or an
  (n)-dependent analytic norm does not yield an (n)-uniform constant and
  cannot support the displayed dense-scale substitution.
- Retain the reachability disclaimer: nothing here shows that dense training
  trajectories contain the required (N_p)-dimensional balls.  Consequently
  this does not answer the study's lower-bound question for the dense model.
- The single-time exponent (d-1) is correct provided the same fixed-domain
  spatial analytic ball occurs at one common non-endpoint time.

With these corrections, the finite-dimensional topological lower bound is
valid.  Without them, the theorem's neighborhood quantifier and its implied
stability scope are overclaims.

## Recheck — 2026-10-05

**Verdict: PASS for the repaired theorem in its stated scope.**

The revised proof makes the complex time and intrinsic spherical
neighborhoods bounded, of fixed positive radius, and independent of
\(p\), \(\epsilon\), and \(n\).  It defines the product \(L^2\) norm using
\(ds\) and probability surface measure, proves the required
\(H^\infty\)-to-\(L^2\) evaluation estimate through Bernstein--Walsh and
the complex spherical-harmonic addition formula, and retains the valid
\(s(1-s)\) endpoint-zero modes.  It also fixes one deterministic decoder,
specifies encoder continuity in the real-domain supremum norm, counts all
instance-dependent decoder data, and limits the conclusion to a static
continuous-encoder obstruction.  The Borsuk--Ulam dimension hypothesis,
the supremum/\(L^2\) norm comparison, and the substitution
\(\epsilon=n^{-1/2}[\log(en)]^{-5/2}\) are consequently valid.

The explicit disclaimer correctly leaves dense-trajectory reachability and
autonomous-model applicability unproved; neither is needed for this
conditional analytic-class theorem.
