# Practical two-sample constants: an affine positivity certificate

2026-09-08. New theoretical analysis of the exact L3 model. No experiment,
old-artifact modification, or review-as-premise is used. The main new result
is the finite-mesh affine certificate in Sections 2--5. It does not establish
a moderately nonlinear global training theorem.

## 1. Primary derivations read and the existing numerical threshold

The source conventions and independence assertion are from
`studies/mean_field_peeling/two_sample_odd_activation_theorem/sources/TWO_SAMPLE_SOURCE_BASELINE.md`,
Sections 3 and 4. The exact normalized coefficient equations, positivity
argument, and beta scaling are from
`two_sample_odd_activation_power10/AFFINE_SOURCE_CERTIFICATE.md`, Sections
2, 3, and 6. The currently sufficient source closure and response estimates
are the actual derivations in
`two_sample_odd_activation_power4/SECTOR_SUPERSOLUTION.md` and
`PRIMAL_L2_RESPONSE.md`. The latter documents give

\[
 eH^{22}M^{19}\le1,\qquad
 q\le H^{30}eM^{19},\qquad q\le H^{-16}M^{-12}.
\]

Thus their source bootstrap only requires

\[
 eM^{31}\le H^{-46}. \tag{1.1}
\]

Together with the existing primal/nonaffinity restriction
\(e\le c_*\delta^{7/4}\), the bound \(M^{32}\le24^8\delta^{-4}\)
shows that the unchanged power-four proof permits

\[
 e\le c_{4,\mathrm{trim}}\delta^4,\qquad
 c_{4,\mathrm{trim}}=
 \min\{1/4,c_*,24^{-8}H^{-46}\}. \tag{1.2}
\]

Indeed \(eM^{32}\le H^{-46}\), \(M>1\), and therefore
\(eH^{22}M^{19}\le H^{-24}M^{-13}<1\) and
\(qM^{12}\le H^{30}eM^{31}<H^{-16}\). Also
\(\delta^4\le\delta^{7/4}\). No assertion about any improved replacement
for \(c_*\) is needed for (1.2). If a separately proved stronger
nonaffinity lemma removes one constituent of \(c_*\), the remaining
primal restrictions must still be retained explicitly.

This is a valid numerical improvement over \(10^{-70}H^{-400}\), but
\(H=10^{30}(1+C_0+C_z+C_g+e^{1410})^4\) is enormous. It does not
satisfy a practical moderate-nonlinearity goal. Replacing 400 by 46 is
bookkeeping, not a structural solution.

## 2. Exact normalized affine setup

Work only in the active mean/contrast sample sector after label folding
and the exact normalization already displayed in the power-ten source
certificate. Let \(H\) denote the strict integration matrix on an arbitrary
positive finite mesh, \(H_{kj}=h_j\) for \(j<k\). The normalized total
duration is \(T\le2\). All quantities below are scalar time arrays in
this active sector. The inactive sector is handled separately by its
explicit affine formulas.

Scale the initial first root and the two initial Gaussian matrices by
\(\beta\in[1,1.001]\). Let the primary affine fields be
\(p,A,B,C\), with

\[
 x_2=Ap,\quad x_3=BAp,\quad q_2=B^*C,\quad q_1=A^*B^*C.
\]

The source equations, with all deterministic arrays frozen, are exactly

\[
 p=\mathbf1 p_0+Hq_1,\quad q_1=\zeta_1+B_2p,
\]
\[
 x_2=\xi_2+A_2q_2,\quad q_2=\zeta_2+B_3x_2,
\]
\[
 x_3=\xi_3+A_3C,\quad C=Hx_3. \tag{2.1}
\]

The five groups \(p_0,\zeta_1,\xi_2,\zeta_2,\xi_3\) are mutually
independent centered Gaussian groups; \(\operatorname{Var}p_0=\beta^2\),
and

\[
 \operatorname{Cov}(\xi_{2,k},\xi_{2,j})
 =\beta^2\mathbb E[p_kp_j],\qquad
 \operatorname{Cov}(\xi_{3,k},\xi_{3,j})
 =\beta^2\mathbb E[x_{2,k}x_{2,j}]. \tag{2.2}
\]

The other source covariances are likewise \(\beta^2\) times the
corresponding backward-input second moments. Their covariance matrices
may be singular. No inverse covariance matrix is used here.

Define the actual affine transfer arrays

\[
 R_1=(I-HB_2)^{-1},\quad F=R_1H,\quad
 W_1=B_2R_1,\quad L_1=(I-B_2H)^{-1},
\]
\[
 R=(I-A_2B_3)^{-1},\quad V=RA_2,\quad
 W=B_3R,\quad L=(I-B_3A_2)^{-1},
\]
\[
 R_3=(I-A_3H)^{-1},\quad
 T_3=HR_3,\quad L_3=(I-HA_3)^{-1},\quad U=R_3A_3.
\tag{2.3}
\]

The subscript in \(T_3\) avoids confusing this transfer with the duration
\(T\). The arrays are finite causal polynomials because all products in
the inverses are strict triangular. The exact coefficient equations are

\[
 A_2=\beta^2F+M_1,\quad A_3=\beta^2V+M_2,
\quad B_3=\beta^2T_3+N_3,\quad B_2=\beta^2W+N_2,
\tag{2.4}
\]

where, at strict entries,

\[
 (M_1)_{kj}=h_j\mathbb E[p_kp_j],\quad
 (M_2)_{kj}=h_j\mathbb E[x_{2,k}x_{2,j}],
\]
\[
 (N_3)_{kj}=h_j\mathbb E[C_kC_j],\quad
 (N_2)_{kj}=h_j\mathbb E[q_{2,k}q_{2,j}].
\tag{2.5}
\]

The existing finite affine positivity argument applies here: normalized
ascent has positive scalar coefficients; expansion in the independent
Gaussian initialized coordinates gives nonnegative covariance terms by
Wick pairing; chronological Gaussian conditioning and (2.4) preserve
nonnegative entries. This is positivity of deterministic contractions
and source arrays, not positivity of realized Gaussian weights. In
particular all covariance entries occurring below are nonnegative.
Passing the finite-width expected contractions to their deterministic
fixed-mesh limits uses uniform integrability: every fixed affine Euler
prefix has polynomial bounds in its Gaussian initialized operator and
root norms, which have moments of every fixed order uniformly in width.

For a causal array let \(|K|_r=\max_k\sum_{j\le k}|K_{kj}|\), and
for a strict array let \(|K|_d=\max_{j<k}|K_{kj}|/h_j\).
The proof uses only

\[
 |AB|_d\le |A|_r|B|_d
\tag{2.6}
\]

when \(B\) is strict, and elementary row submultiplicativity. It never
asserts that multiplication by an arbitrary row-bounded array on the
right preserves strict density.

## 3. Positivity converts raw variances into actual response rows

For a nonnegative deterministic row \(a_j\) and a centered Gaussian
group \(Z_j\) with every covariance entry at least \(m^2\),

\[
 \mathbb E\left(\sum_j a_jZ_j\right)^2
 =\sum_{i,j}a_ia_j\mathbb E[Z_iZ_j]
 \ge m^2\left(\sum_j a_j\right)^2. \tag{3.1}
\]

Only an entrywise lower bound on covariance is used. This is not a
positive lower bound on its smallest eigenvalue: perfectly correlated
sources are admissible.

Solving (2.1) at the actual coefficient arrays gives

\[
 p=R_1\mathbf1p_0+F\zeta_1,\quad
 q_1=W_1\mathbf1p_0+L_1\zeta_1,
\]
\[
 x_2=R\xi_2+V\zeta_2,\quad q_2=W\xi_2+L\zeta_2,
\]
\[
 x_3=R_3\xi_3,\quad C=T_3\xi_3. \tag{3.2}
\]

All arrays in (3.2) are nonnegative; every resolvent is at least the
identity entrywise. Independence makes the covariance contributions
from different source groups add without cross terms. The covariance
contribution from the second group in each expression has nonnegative
entries. Thus

\[
 \mathbb E[p_kp_j]\ge\beta^2,
\quad \operatorname{Cov}(\xi_{2,k},\xi_{2,j})\ge\beta^4,
\quad \mathbb E[x_{2,k}x_{2,j}]\ge\beta^4,
\quad \operatorname{Cov}(\xi_{3,k},\xi_{3,j})\ge\beta^6.
\tag{3.3}
\]

Let \(P=\max_k\|p_k\|_2\), \(X=\max_k\|x_{2,k}\|_2\),
\(Y=\max_k\|x_{3,k}\|_2\), \(D=\max_k\|C_k\|_2\),
\(Q_i=\max_k\|q_{i,k}\|_2\). Applying (3.1)--(3.3) proves

\[
 |R_1|_r\le P/\beta,\quad |W_1|_r\le Q_1/\beta,
\]
\[
 |R|_r\le X/\beta^2,\quad |W|_r\le Q_2/\beta^2,
\]
\[
 |R_3|_r\le Y/\beta^3,\quad |T_3|_r\le D/\beta^3.
\tag{3.4}
\]

These bounds concern the actual frozen formal-source arrays because
(2.1)--(2.4) define those arrays exactly. No identification of an
arbitrary raw tangent with a source derivative occurs. In particular
the independent-root probe argument and the raw-Hessian exponential
are unnecessary for (3.4).

Since \(R_1,R\ge I\), positivity also gives

\[
 |B_2|_r\le Q_1/\beta,\qquad |B_3|_r\le Q_2/\beta^2.
\tag{3.5}
\]

## 4. An explicit complete algebraic transfer table

Assume \(R_*\ge1\) bounds every primary normalized field/operator,
namely \(\|p_k\|_2,\|A_k\|_{op},\|B_k\|_{op},\|C_k\|_2\le R_*\)
at every mesh node, and also \(\beta\le R_*\). Then
\(P,D\le R_*\), \(X,Q_2\le R_*^2\), and
\(Y,Q_1\le R_*^3\). With \(T\le2\) and \(1\le\beta\le1.001\),
the following bounds hold:

| Actual normalized affine array | Bound |
|---|---:|
| \(R_1\), row | \(R_*\) |
| \(W_1,B_2\), row | \(R_*^3\) |
| \(F\), strict density | \(R_*\) |
| \(A_2\), strict density | \(2R_*^2\) |
| \(R,W,B_3\), row | \(R_*^2\) |
| \(V\), strict density | \(2R_*^4\) |
| \(A_3\), strict density | \(4R_*^4\) |
| \(L\), row | \(5R_*^4\) |
| \(R_3\), row | \(R_*^3\) |
| \(T_3\), row | \(R_*\) |
| \(L_3\), row | \(9R_*^5\) |
| \(U=R_3A_3\), strict density | \(4R_*^7\) |
| \(L_1\), row | \(3R_*^3\) |
| \(RF\), strict density | \(R_*^3\) |
| \(FL\), strict density | \(3R_*^3\) |
| \(RFL\), strict density | \(3R_*^5\) |

Proof of the entries not already in (3.4)--(3.5):
\(F=R_1H\) gives its density bound. Cauchy--Schwarz gives
\(|M_1|_d\le P^2\), so
\(|A_2|_d\le\beta P+P^2\le2R_*^2\). Then
\(|V|_d\le |R|_r|A_2|_d\le2R_*^4\), and
\(|A_3|_d\le\beta^2|V|_d+X^2\le4R_*^4\).
Here \(2\beta^2+1<4\) throughout the stated beta range.

The identities

\[
 L=I+WA_2,\quad L_3=I+T_3A_3,
\quad L_1=I+W_1H
\]

give the displayed reverse rows by multiplication of row norms and
\(|A_i|_r\le T|A_i|_d\). The density bound for \(U\) follows by
left multiplication of \(A_3\) by \(R_3\). Likewise
\(|RF|_d\le R_*^3\).

The improvement for \(FL\) uses a genuine cancellation in the positive
coefficient equations. Equation (2.4) gives \(B_2\ge\beta^2W\), while

\[
 FB_2=R_1-I.
\]

Consequently, entrywise,

\[
 FL=F+FWA_2
 \le F+\beta^{-2}(R_1-I)A_2. \tag{4.1}
\]

Taking strict densities on the right proves
\(|FL|_d\le R_*+2R_*^3\le3R_*^3\). Left multiplication by
\(R\) proves the final \(RFL\) bound. No beta differentiation or
inverse beta gap appears in (4.1).

The interval \(1\le\beta\le1.001\) in this lemma is an algebraic
conditional range: a primal bound on a common interval is still required
for every beta to which the lemma is applied. The old continuation proof
supplies that bound only for its narrower family
\(\beta-1=O(M^{-2})\), not for every beta up to 1.001 on the original
endpoint interval. No such wider continuation assertion is made here.

The table is conditional only on the actual affine primal bound, which
the existing balance/continuation argument supplies. For exact
continuous time with initial Gaussian actions bounded by ten,
\(\|A\|^2\le101\beta^2+\|C\|^2\) follows directly from
\(A^*A=p\otimes p+(A_0^*A_0-p_0\otimes p_0)\); the other primary
bounds are smaller. Thus one may take
\(R_*=(101\beta^2+\max\|C\|^2)^{1/2}\), with an arbitrarily small
additional fixed margin for sufficiently fine Euler meshes. All finite
mesh conclusions then remain uniform over that sufficiently fine class.

## 5. Original-time consequences and what is still provisional

Retain the original slope range \(1/2\le a\le1\). Let
\(r=\sqrt{(1+y_1y_2\rho)/2}\), \(\lambda=a^3r\),
and \(M=(3/(\sqrt2\lambda))^{1/4}\). In the active sector the exact
normalizations give

\[
 A_2=(r/a)\widehat A_2,\quad A_3=ar\widehat A_3,
\quad B_3=(ar)^{-1}\widehat B_3,\quad B_2=(a/r)\widehat B_2.
\]

A normalized strict density gets an additional factor \(\lambda\)
on return to original feature time. Products \(FL,RF\) transform like
\(F\); \(U\) transforms like \(A_3\). Therefore, using only
\(R_*=O(M)\), the proved table implies the following orders, with
explicit algebraic constants obtainable from Section 4 and the existing
common enlarged-interval primal radius:

| Original-time active array | Order |
|---|---:|
| \(F\), density | \(M^{-7}\) |
| \(A_2\), density | \(M^{-6}\) |
| \(V,A_3\), density | \(M^{-4}\) |
| \(B_3\), row | \(M^6\) |
| \(B_2\), row | \(M^7\) |
| \(R_1,R,R_3,L,L_3\), respective rows | \(M,M^2,M^3,M^4,M^5\) |
| \(U\), density | \(M^{-1}\) |
| \(FL,RF\), density | \(M^{-5}\) |

These orders and the numerical normalized table are proved above.
The following potential consequence is **provisional**, not a new
nonlinear theorem: in the existing positive-supersolution calculation,
the two first-forward sandwiches would cost
\(M^{-10}q\) and \(M^{-6}q\), while the second-forward sandwich would
cost \(M^{-4}q\). Dividing by the old positive leading densities
\(cM^{-8}\), and paying its existing beta margin \(cM^{-2}\), suggests
\(qM^6\) small. Backward reconstruction uses the sharper product
\(|L|_r|R|_r=O(M^6)\), consistent with an active backward radius of
order one. An inactive radius of order \(M^{-4}\) would separately
control its time integration. This would improve the old closure
\(qM^{12}\) small, but a new complete box/response ledger is required
before asserting that result.

The affine exponential prefactor has been removed from the source
certificate, but the old primal comparison still contains
\(\exp(1404)\), and the nonlinear derivative envelope still contains
the curvature multiplier \(\phi''(Z)q\). Replacing every occurrence of
the old common \(H\) by a smaller number without redoing these other
estimates would be invalid. The source forcing constants, primal tube,
enlarged beta interval, all current backward returns, and cap-uniform
exponential moments must be assembled explicitly before a usable
nonlinear-amplitude conclusion can be made.

## 6. Activation-design boundary

Centering the odd arctangent perturbation can improve derivative
constants by a modest factor. For example

\[
 \phi_e(z)=z+e(\arctan z-z/2)
 =(1-e/2)z+e\arctan z
\]

has \(1-e/2\le\phi'_e\le1+e/2\). The choice \(e=1/2\) is
\(\phi(z)=3z/4+\arctan(z)/2\), an explicit moderate candidate in the
same odd shape family. The present affine positivity lemma does not
prove the desired global population limit for this candidate.

Merely making curvature tiny on the Gaussian bulk cannot certify strong
nonlinearity there. If an odd \(C^2\) activation has
\(\|\phi''\|_\infty\le K\), Taylor's theorem gives
\(|\phi(z)-\phi'(0)z|\le Kz^2/2\), hence

\[
 \inf_b\mathbb E[\phi(G)-bG]^2\le 3K^2/4.
\]

Thus a practical activation cannot be justified simply by hiding a
microscopic curvature coefficient inside a nominally order-one shape
coefficient. Bounded or piecewise-localized curvature still needs a
new cap-independent control of the actual \(q\)-weighted derivative
response when the nonlinear amplitude is moderate.

## 7. Status summary

* Established from existing proof: the safely trimmed cutoff (1.2).
* New proved lemma: Sections 2--4, an exponential-free affine response
  certificate using source independence, covariance positivity, and
  exact coefficient identities.
* New proved order conversion: the original-time table in Section 5.
* Provisional: source supersolution closure at \(qM^6\) small.
* Open: a complete L3 global theorem with an explicit moderate nonlinear
  coefficient; no such theorem is claimed by this note.
