# Hostile audit of `CUBIC_DEPTH_TIME.md`

## Verdict

**FAIL as a self-contained proof of the cubic theorem.**  The universal
Euler combinatorics and the activation-moment recursion survive the audit,
but only conditionally on the existence of the claimed common cylindrical
\(C^3\) gradient germ.  Section 4 does not yet construct that germ with
enough precision to justify differentiation at the coalesced Gaussian law.
Consequently (1.3), (1.6), and the claim list in Section 11 must not yet be
labelled proved.

This is not an algebraic counterexample to the proposed cubic law.  It is a
failure of the indispensable intertwining bridge on which the law is based.

## Blocking findings

### B1. The common source-jet family is used before it is constructed

Lines 393--420 define the source index sets by

\[
 \mathscr Q_a=\{\partial^\alpha X_{a-1,s}(0)\},\qquad
 \mathscr C_a=\{\partial^\alpha\Delta_{a,s}(0)\},
\]

and then define the Gaussian vectors needed to produce those same
derivatives by taking the Grams of these lists.  A positive-semidefinite
Gram proves existence of a Gaussian vector **after the indexed vectors are
known**; it does not construct the indexed vectors or prove that the
self-consistent source-jet recursion has a solution.

The paragraph at lines 422--432 does not close this point.  It asserts a
lexicographic induction, but it does not give the dependency rule for a
same-connector response when a forward derivative uses a frozen direction
containing a generated transpose source.  In particular, after
\(\mathbf h=D\mathbf g[\mathbf g]\) is frozen, a forward variation in the
\(\mathbf h\)-direction contains the raw transpose fields occurring in
\(\mathbf h\); the response basis for that forward action contains the
corresponding generated cotangent fields.  Those fields are not part of the
order-only forward-then-reverse schedule stated at lines 422--432.  The
later instruction to "enlarge once" asserts that these extensions are
compatible but gives no construction showing it.

Thus neither existence nor non-circularity of the joint
\((\varepsilon,\lambda)\)-jet law follows from the displayed induction.
This is exactly the point at which a common source-jet theorem was needed.

### B2. Finite jet lists do not imply equality as functions of the step variables

The oracle in (4.9a)--(4.9b) is explicitly defined only on the finite lists
of jets in (4.1e).  Those lists contain
\(X_{a-1,s}(0),\partial X_{a-1,s}(0),\ldots\), not the nonlinear current
query \(X_{a-1,s}(\varepsilon,\lambda)\) at nonzero coordinates.  Equations
(4.10)--(4.11) nevertheless apply the oracle to the latter current query,
and lines 632--634 conclude that all nodes agree *as functions* of the step
variables.  A finite span of derivatives at one point need not contain the
query curve away from that point, so this conclusion does not follow.

The weaker conclusion actually needed is equality of all mixed jets through
order three.  That conclusion is also not proved by merely displaying
(4.10)--(4.11): the proof must show, for each derivative order, that
differentiating the moving response representation produces exactly the
source and response jets in the temporal DAG.  No such nodewise jet
induction is present.  Therefore line 649's order-three conclusion is not a
consequence of the preceding argument as written.

### B3. The history-dependent response formula is not proved to be one unchanged oracle

In (4.9a)--(4.9b) the response sum depends on "the already exposed finite
opposite history appropriate to that call."  Both the basis fields
\(\Delta_{a,r},X_{a-1,r}\) and their singular Gaussian coordinates change
when the history or the frozen-direction list is enlarged.  Lines 455--460
argue compatibility only from the fact that an old covariance is a
submatrix of a new covariance.  That proves compatibility of Gaussian
*marginals*.  It does not prove compatibility of the response sums, their
mixed derivatives, or the joint forward/transpose actions.

Lemma 3.1 supplies one scalar adjoint equality for a fixed finite list.  It
does not state or prove the required enlargement/cocycle identity for the
action variables themselves.  Consequently the phrases "retain the fixed
oracle" at line 572 and "unchanged finite-query oracles" at lines 618--621
are unsupported.  Without this compatibility, the tuple in (4.9) has not
been shown to represent repeated updates of one fixed initialization
matrix germ.

### B4. Singular mixed differentiability is asserted, not derived

Lines 366--375 regularize a single Gaussian expectation by
\(\Sigma+\delta I\) and invoke domination.  Pointwise convergence of the
regularized Price identity does not by itself prove differentiability of
the singular expectation with respect to \(\varepsilon\), because that
requires control of the parameter difference quotient (or an integrated
Price identity) uniformly as \(\delta\downarrow0\).  Repeating the sentence
does not prove mixed derivatives through order three.

There is also no chronological induction establishing all of the premises
needed at each expectation call: \(C^3\) regularity of the covariance
entries, the required source derivatives of the integrand, a common
polynomial dominator for every mixed derivative, and commutation of the
singular mixed derivatives.  Formula (4.1) would avoid square-root
differentiation if \(Y(\varepsilon,\lambda)\) had already been constructed
as a \(C^3\) curve in one fixed \(L^2\) space.  B1 is precisely the missing
construction of such a curve, so (4.1) cannot be used to supply its own
hypothesis.

Because (4.3)--(4.5) and hence (4.7)--(4.8) require commuting mixed
derivatives at this singular point, B4 is a blocker rather than a cosmetic
regularity omission.

## Components that pass, conditionally or unconditionally

### 1. Finite-energy generated directions: conditional pass

Once the required source jets exist with the stated finite moments,
(2.4)--(2.5) correctly show that the endpoint blocks are in \(L^2\) and
the matrix blocks are finite sums of Hilbert--Schmidt simple tensors.  The
argument never puts a cylindrical initialization matrix in
\(\mathcal P_L\).  This part is sound, but it is conditional on the source
jet construction rejected in B1.

### 2. Finite-history adjoint identity: pass under its stated separation hypotheses

For a fixed finite forward list and a fixed finite transpose list,
(3.3)--(3.4) are the two Gaussian integration-by-parts identities and their
sum is exactly (3.2).  The covariance-inverse-free identity remains valid
at a singular Gram by regularization, provided \(c\) depends only on the
complete forward source block and \(\dot x\) only on the complete transpose
source block (with any other variables independent of the corresponding
new raw source).  The generated DAG still has to prove these separation and
completeness hypotheses; Lemma 3.1 cannot prove them for itself.

### 3. Universal time coefficients: algebraic pass conditional on the gradient germ

Assuming a common \(C^3\) scalar gradient germ, differentiation of explicit
Euler gives

\[
 \theta_N'=N\mathbf g,qquad
 \theta_N''=N(N-1)\mathbf h,
\]

\[
 \theta_N'''=6\binom N3D\mathbf g[\mathbf h]
 +\frac{N(N-1)(2N-1)}2D^2\mathbf g[\mathbf g,\mathbf g].
\]

The chain rule then gives exactly

\[
 \mathcal A_N=\frac{N(4N^2-3N+1)}2,qquad
 \mathcal B_N=2N(N-1)(2N-1).
\]

Direct expansion verifies

\[
 8\mathcal A_t-\mathcal A_{2t}=-3t(2t-1),\qquad
 8\mathcal B_t-\mathcal B_{2t}=-12t(2t-1).
\]

Thus the time polynomial and the factor
\(-t(2t-1)(\mathsf S+4\mathsf H)/2\) contain no arithmetic error.  Their
application to the Gaussian DAG remains conditional on B1--B4.

### 4. Activation recursion: contraction audit passes conditional on (7.1a)

Starting from the straight-path response formula (7.1a), every displayed
moment recursion checks out:

- squaring
  \(Z_a^{[1]}=E_{a1}+\Theta_{a-1}R_ap\) gives (6.3);
- \(\mathbb E[gpE_{a2}]=M_{a-1}\mathbb E[(gp)']\) gives the
  \((d+v)M_{a-1}\) term in (6.4);
- differentiating the three atoms in (7.5) gives exactly the four
  contractions in (6.5);
- squaring (7.8) gives exactly the five terms of (6.6), including the
  Gaussian fourth moment factor \(3\);
- differentiating (7.8) in the base forward source gives
  \(\Theta_{a-1}b_a(r+s)+\gamma_{a+1}(v+d)\), and adding the learned
  coefficient \(\pi_a\) gives (6.7);
- the parameter-block norm decomposition gives (6.9), because
  \(\mathbb E[X_{a-1}X_{a-1}^{[1]}]=0\).

The premise (7.1a), however, is an instance of the fixed-oracle claim in
B3.  Therefore this is a conditional verification of the recursion, not an
independent repair of the intertwining gap.

### 5. Depth-two reduction: pass

Expanding (6.3)--(6.9) at \(L=2\), with
\(c=1+d\), \(\beta=v+cr\), \(\delta=d+cs\), and
\(k=d+\beta+\delta\), reproduces (9.1)--(9.2).  Under
\((u,v,s,e)=(e_{\rm old},b_{\rm old},v_{\rm old},s_{\rm old})\), these
are the prior depth-two polynomials.  No coefficient mismatch was found.

### 6. Constant, identity, and affine checks: pass algebraically

For \(\phi\equiv\pm1\), all derivative moments vanish and the exact output
is \(Nh\).

For \(\phi(x)=x\), the recursions reduce to

\[
 V_a=\sum_{q\le a}q^2,qquad
 \beta_a=\sum_{q\le L-a+1}q^2,qquad \mathsf S_{x,L}=0,
\]

and hence

\[
 \mathsf H_{x,L}=\frac{L(L+1)^2(L+2)}6.
\]

At \(L=3\), this gives \((V_1,V_2,V_3)=(1,5,14)\),
\((\beta_3,\beta_2,\beta_1)=(1,5,14)\), \(\mathsf H=40\),
\(J=160\), and \(\kappa=-80t(2t-1)\), as stated.  The additional claim at
lines 1257--1262 about an "independent bounded cyclic-operator closure" is
not derived or cited anywhere in the admissible material and therefore is
not an independently verified check.

For \(\phi(x)=\alpha x+\beta\), the listed moments are correct,
\(M_a=T_a=0\), and the reduced \(V,\gamma,\beta\) recursions and
\(\mathsf S=0\) follow.  The endpoint \(d=0\) is correctly separated as
the constant branch.

### 7. Explicit depth majorant: pass

With \(M_\phi\ge1\), every moment in (6.1) is bounded by
\(A_\phi=\max\{4,4M_\phi^4\}\).  Also
\(\Theta_a\le A_\phi^{2L}\), \(b_a\le A_\phi^L\), and
\(\pi_a\le A_\phi^{L+1}\).  Termwise absolute values then give
(10.2)--(10.5).  These bounds are deliberately loose but valid and
terminate after the stated two depth passes.

## Limit-order audit

The note does **not** take a finite-width Taylor expansion and does not
interchange \(n\to\infty\) with \(h\to0\).  It works only with the proposed
width-first Gaussian DAG and explicitly leaves pointwise fixed-\(h\)
identification to another result.  Thus the forbidden opposite-order
argument is absent.

This also means that `CUBIC_DEPTH_TIME.md` alone proves no statement about
the actual finite-width network.  Even after an external pointwise
fixed-\(h\) theorem is supplied, the cubic identification still requires
B1--B4 to establish the \(C^3\) germ of the width-first DAG.

## Final claim status

| Claim | Audit status |
|---|---|
| Fixed-list adjoint identity (3.2) | pass under the displayed separation hypotheses |
| Generated directions have finite energy | conditional pass |
| Common singular \(C^3\) perturbation DAG | **fail / unproved** |
| Temporal DAG equals one Euler gradient germ | **fail / unproved** |
| Universal \(N\)-polynomials | conditional pass |
| Nine-moment depth recursion | conditional pass; contraction algebra verified |
| Depth-two reduction and elementary activation checks | pass algebraically |
| Cubic law (1.3), (1.6) for the width-first DAG | **conditional, not proved** |
| Actual-network cubic law | outside this note and not proved here |

Accordingly, items 2--5 in the "Proved here" list at lines 1421--1427 are
overstated until the common finite-query source construction, singular
mixed regularity, and oracle/Euler compatibility are supplied as actual
lemmas rather than asserted inductions.
