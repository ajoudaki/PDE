# Independent order-five derivation and atom audit

**Status:** algebraically audited Gaussian normal form; this note is an
independent compiler audit, not by itself the finite-width probability theorem  
**Scope:** two hidden layers, one sample, ordinary Taylor order five  
**Activation approximation:** none

## 1. Frozen outputs

The authoritative independent unit-Gram coefficient map is
`independent_coefficient_map.json`, section `unit_gram`.  It uses

\[
M_{\nu_0\ldots\nu_5}
=\mathbb E_{G\sim N(0,1)}\prod_{r=0}^5\phi^{(r)}(G)^{\nu_r},
\qquad M_{200000}=1.
\]

Its exact-file SHA-256 (including its terminal line feed) is

```
fa3b4a6f7dc665e63e2c02355a14122f89f56bdfd34f0fe7402be4cab0ff2878
```

The separate layer-tagged map is
`independent_layer_tagged_coefficient_map.json`.  It fixes \(Q^0=1\), but
does not impose unit forward variance:

\[
X_\nu=\mathbb E_{N(0,Q^0)}\prod_r\phi^{(r)}(G)^{\nu_r},
\qquad
Y_\nu=\mathbb E_{N(0,Q^1)}\prod_r\phi^{(r)}(G)^{\nu_r},
\qquad Q^1=X_{200000}.
\]

Its exact-file SHA-256 is

```
52832afc4f9e1cf27f5b8465f2f5373bcb3e9f5c56b0686c9366162da2e17c11
```

The full explicit symbolic-\(Q^0\) coefficient map was subsequently
reconstructed by exact rational interpolation and frozen separately as
`independent_symbolic_q0_coefficient_map.json`, with SHA-256

```
e682c708fedadc577b7446a7b9c07b79262c945fbae5726918436153876f889a
```

Its independent degree bounds and post-freeze comparison are documented in
`SYMBOLIC_Q0_INTERPOLATION_AUDIT.md`.  The observed degrees are (1,3,5) for
(A,B,C), and all 3, 50, and 1045 graded coefficients agree with the primary
symbolic map.  The earlier rational spot checks in
`Q0_SPOT_COMPARISON.json` remain as additional evidence.

This tagged map is the correct independent artifact for the unnormalised
quadratic control.  The first unit-map freeze contained a duplicated,
incorrectly labelled `layer_tagged` field.  It was removed in an explicitly
reported one-time metadata re-freeze; no coefficient in the `unit_gram`
section changed.

The distributively expanded unit maps contain respectively 3, 46, and 974
monomials for \(A,B,C\); the tagged maps contain 3, 50, and 1045.  The plain
text files `A.txt`, `B.txt`, and `C.txt` are a human-readable expansion of the
unit map.  In particular,

\[
\boxed{A=1+M_{020000}+M_{020000}^2.}
\]

The 46-term \(B\) and 974-term \(C\) expressions are literal finite formulas,
not programs to be evaluated.  Their JSON representation is the canonical
coefficient map; each record is one rational coefficient and one product of
declared \(M_\nu\) atoms.

## 2. Exact finite-width flow used by this route

Put \(A=W/\sqrt n\), \(h=\phi(u)\), \(g=\phi(z)\),
\(b=a\phi'(z)\), and \(r=A^Tb\).  The exact feature-ascent vector field
\(\dot\theta=n\nabla f_n(\theta)\) is

\[
\boxed{
\dot a=g,
\qquad
\dot A={1\over n}bh^T,
\qquad
\dot u=Q^0\phi'(u)r,
\qquad z=Ah.}
\tag{2.1}
\]

This is an identity at every finite \(n\), before expectation or a width
limit.  The independent calculation takes ordinary Taylor coefficients,
\(x(t)=\sum_{k\ge0}x_kt^k\), rather than exponential-jet coefficients.  Thus

\[
A_m={1\over m n}\sum_{p+q=m-1}b_ph_q^T,
\tag{2.2}
\]

and the exact coefficient identities are

\[
\begin{aligned}
z_k&=A_0h_k+
 \sum_{m=1}^k{1\over m}\sum_{p+q=m-1}
 b_p\,{h_q^Th_{k-m}\over n},\\
r_k&=A_0^Tb_k+
 \sum_{m=1}^k{1\over m}\sum_{p+q=m-1}
 h_q\,{b_p^Tb_{k-m}\over n},\\
u_{k+1}&={Q^0\over k+1}\sum_{p+q=k}
 [t^p]\phi'(u(t))\,r_q,\\
a_{k+1}&={g_k\over k+1}.
\end{aligned}
\tag{2.3}
\]

Finally,

\[
f_k={1\over n}\sum_{p+q=k}a_p^Tg_q,
\qquad D_n^kf_n=k!f_k.
\tag{2.4}
\]

Equations (2.1)--(2.4) fix all powers of \(n\), all factorials, and the two
orientations of the reused middle matrix independently of the tensor
contraction formula for \(D_n^5f_n\).

## 3. Complete leading equality-partition ledger

Let

\[
H_{k\ell}=\mathbb E[h_kh_\ell],
\qquad B_{k\ell}=\mathbb E[b_kb_\ell].
\tag{3.1}
\]

Chronological Gaussian integration by parts gives the following six and only
six leading sectors:

| matrix occurrence | leading equality/Wick sector | limiting contribution |
|---|---|---|
| \(A_0h_k\) | two forward occurrences pair at a free bottom index | fresh \(F_k\), with \(\mathbb E F_kF_\ell=H_{k\ell}\) |
| \(A_0h_k\) | the forward \(W_{ij}\) pairs with an earlier transpose occurrence | \(\sum_{s<k}b_s\alpha_{ks}\) |
| \(A_mh_{k-m}\) | explicit rank-one update, free bottom index | \(m^{-1}\sum_{p+q=m-1}b_pH_{q,k-m}\) |
| \(A_0^Tb_k\) | two reverse occurrences pair at a free top index | fresh \(R_k\), with \(\mathbb E R_kR_\ell=B_{k\ell}\) |
| \(A_0^Tb_k\) | the transpose \(W_{ij}\) pairs with an earlier forward occurrence | \(\sum_{s\le k}h_s\beta_{ks}\) |
| \(A_m^Tb_{k-m}\) | explicit transposed rank-one update, free top index | \(m^{-1}\sum_{p+q=m-1}h_qB_{p,k-m}\) |

Here the response coefficients, used only internally, are

\[
\alpha_{ks}=\mathbb E\,\partial_{R_s}h_k,
\qquad
\beta_{ks}=\mathbb E\,\partial_{F_s}b_k.
\tag{3.2}
\]

The chronological ranges in (3.2) are important: \(h_k\) can use reverse
calls only through \(R_{k-1}\), whereas \(b_k\) already uses the current
forward call \(F_k\).  Therefore

\[
\begin{aligned}
A_0h_k&\Longrightarrow F_k+\sum_{s<k}b_s\alpha_{ks},\\
A_0^Tb_k&\Longrightarrow R_k+\sum_{s\le k}h_s\beta_{ks}.
\end{aligned}
\tag{3.3}
\]

For width counting, every \(A_0\) entry contributes \(n^{-1/2}\), every free
neuron index contributes \(n\), and an explicit \(A_m\) entry contributes
\(n^{-1}\).  The fresh and single-response pairings in the table have net
power \(n^0\).  Any additional unpaired equality removes a free index without
restoring a matrix-pair factor and is \(o(1)\).  Nested leading pairings are
not discarded: repeated application of (3.3) enumerates them.  Thus the table
is also the transpose-response audit; deleting either response row already
changes the order-one NTK coefficient.

## 4. Inverse-free Wick--Stein flattening

After (3.3), every coordinate expression is a finite polynomial in

- activation jets \(X_r=\phi^{(r)}(U)\) and
  \(Y_r=\phi^{(r)}(F_0)\);
- a standard readout Gaussian;
- the jointly Gaussian \(F_1,\ldots,F_5\);
- the jointly Gaussian \(R_0,\ldots,R_4\);
- deterministic moment polynomials accumulated at earlier chronological
  steps.

The reverse variables and readout are eliminated by ordinary Isserlis
pairing.  The forward auxiliaries are correlated with the activation argument
\(F_0\), so they are removed without a covariance inverse by the recursion

\[
\begin{aligned}
\mathbb E\!\left[F_i\prod_{j\ge1}F_j^{m_j}\Psi(F_0)\right]
={}&\sum_{j\ge1}m_jH_{ij}\,
\mathbb E\!\left[F_j^{m_j-1}\!\prod_{\ell\ne j}F_\ell^{m_\ell}\Psi(F_0)\right]\\
&+H_{i0}\,
\mathbb E\!\left[\prod_{j\ge1}F_j^{m_j}\Psi'(F_0)\right].
\end{aligned}
\tag{4.1}
\]

Each use of (4.1) lowers the number of auxiliary forward Gaussians, so it
terminates.  Once all auxiliaries are gone, independence of \(U\) and \(F_0\)
turns every term into a product of one-dimensional \(X_\nu,Y_\nu\) atoms.
The unit-Gram homomorphism \(X_\nu,Y_\nu\mapsto M_\nu\), followed by
\(M_{200000}=1\), gives the requested unit map.  No pseudoinverse,
multidimensional atom, unnamed covariance, or implicit derivative remains.

Although syntactic response differentiation can transiently create a sixth
activation derivative, exact coefficient collection cancels every such term.
The audited terminal maximum derivative is one in \(A\), three in \(B\), and
five in \(C\), in both frozen maps.

## 5. Parity audit

For a fixed initialization, let \((a(t),A(t),u(t))\) solve (2.1).  Under the
initial readout sign flip \(a(0)\mapsto-a(0)\), the transformed path is

\[
\widetilde a(t)=-a(-t),\qquad
\widetilde A(t)=A(-t),\qquad
\widetilde u(t)=u(-t).
\]

It solves the same vector field with the sign-flipped initialization, and
\(\widetilde f(t)=-f(-t)\).  Symmetry of the Gaussian readout therefore gives

\[
\mathbb E D_n^kf_n=(-1)^{k+1}\mathbb E D_n^kf_n.
\]

All even coefficients vanish.  The independent sparse maps give literal
zero dictionaries for \(F(0),F''(0),F^{(4)}(0)\), before numerical
evaluation.

## 6. Independent canonicalization and controls

The independent compiler was frozen before the primary order-five maps were
opened.  It uses a sparse distributive random-polynomial representation and
the recursive eliminator (4.1); the primary compiler uses a separately
designed factored deterministic DAG.  Post-freeze comparison, recorded in
`PRIMARY_COMPARISON.json`, found zero rational coefficient discrepancies:

| map | \(A\) terms | \(B\) terms | \(C\) terms | discrepancies |
|---|---:|---:|---:|---:|
| unit | 3 | 46 | 974 | 0 |
| layer-tagged, \(Q^0=1\) | 3 | 50 | 1045 | 0 |

Exact polynomial specialization in `CONTROL_AUDIT.json` gives

\[
\begin{array}{c|ccc}
\phi & A&B&C\\ \hline
1&1&0&0\\
x&3&48&1464\\
1+x&6&112&4400\\
x^2&111&1685184&77400633120.
\end{array}
\]

The \(1+x\) and \(x^2\) rows use the layer-tagged map.  In particular the
quadratic row correctly uses \(Q^1=3,Q^2=27\), not the unit-Gram quotient.

For the preregistered smooth nonpolynomial activation

\[
\phi(x)={\sin x\over\sqrt{\mathbb E\sin^2G}},
\]

direct Gaussian quadrature of the frozen \(M_\nu\) atoms predicts

\[
(A,B,C)\approx
(4.037096946465641,-103.25733114677412,29944.432342937278).
\]

Orders 48 through 128 agree to the displayed precision for \(A,B\), and to
about \(10^{-9}\) for \(C\); see `NORMALIZED_SINE_PREDICTION.json`.  This is
quadrature of declared Gaussian expectations, not a Hermite approximation of
the activation.  The finite-width regression against this preregistered value
is a separate experimental gate.

## 7. Probability and regularity boundary

The identities (2.1)--(2.4) require only the finite derivatives actually
appearing and are exact at finite width.  The sparse maps are formal
large-width candidates until a probability theorem is invoked.

For theorem-level annealed limits, this audit adopts the frozen envelope

\[
\phi\in C^\infty(\mathbb R),
\qquad
|\phi^{(r)}(x)|\le C_r(1+|x|^{m_r})
\quad\text{for every }r\ge0.
\tag{7.1}
\]

With fixed depth, fixed batch, deterministic \(0<Q^0<\infty\), and
independent Gaussian initialization, (7.1) makes every order-five program
variable have all finite moments.  Fixed-program tensor-program convergence
then gives almost-sure and finite-\(L^p\) convergence for every finite \(p\).
In particular one may choose \(p>1\), obtaining uniform integrability and
therefore convergence of expectations.  A mere \(C^5\) assumption supports
the finite tensor identity when the required expectations exist, but is not
promoted here to the annealed theorem without a separate uniform-integrability
proof.

The claim levels are therefore:

1. (2.1)--(2.4): exact finite-width identities;
2. the chronological response system: formal fixed-width-limit candidate;
3. the two frozen atom maps: algebraically and atomwise audited normal forms;
4. the expected large-width equalities: theorem-level only under (7.1) and
   the fixed-program probability bridge.
