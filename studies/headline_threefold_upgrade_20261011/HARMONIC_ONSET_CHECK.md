# Scoped check of the Harmonic source-rank obstruction

2026-10-11. Fresh mathematical check of `HARMONIC_ONSET_ROUTE.md` and
the relevant current-paper definitions. No earlier Harmonic verdict was
used. No experiments, paper edits, or Git operations were performed.

## Verdict

The candidate's obstruction is correct for the current **coordinate-source
approximation plus exact source-metric selection** class. At fixed
\(d=m=L=2\) and one fixed admissible activation, it rules out a sufficient
width polynomial jointly in \(\gamma^{-1}\) and \(Y^{-1}\), uniformly
over the full allowed small-label range, while preserving the stated
Harmonic retained-state bound. Along the candidate's admissible family
\(Y=\lambda^2\), \(\lambda=\gamma/2\to0\), the necessary width is
\(\exp(c_C/\sqrt\lambda-1)\) on an initialization event whose probability
tends to one.

No mathematical correction is needed. The result is not a fixed-positive-
\(Y\) result, not a fixed-positive-\(Y/\lambda\) result, and not a lower
bound for arbitrary output-only compressors. It does not contradict the
paper's original eventual theorem for each separately fixed problem.

## 1. The interface really is part of the current construction

The source-to-runtime proposition in `paper/compact_selected.tex` requires
linear spaces \(E_j\subset\mathbb R^n\) approximating the four source
families to coordinate accuracy \(\eta\), and explicitly assumes
\(0<\eta\le\min\{1,Y,16Y/\lambda\}\). The particular displayed
source tolerance also obeys \(\eta\le Y\). The first family in
`cp:source-families` is \(h^{(j)}\). Harmonic promises all unit
directions and includes time zero, so

\[
\sup_{v\in S^1}\inf_{u\in E_1}
\|\phi(W_0^{(1)}v)-u\|_\infty\le\eta\le Y
\tag{1}
\]

is indeed necessary for a source-compliant instance of this construction.
It is not inferred from output accuracy alone.

The exact selection identity is
\(u_I^\top Mu_I=\|u\|_2^2/n\) for \(u\in E_1\). If
\(u_I=0\), then \(u=0\), so restriction to \(I\) is injective and
\(\dim E_1\le|I|\). The current retained inventory explicitly stores
the selected support and first-layer matrix, hence contains at least
\(|I|\) real coordinates. No inference from the **upper** coefficient
count or the bound \(|I|\le9\dim E_1\) is used.

## 2. Unlimited finite initialized rank

The proposed activation \(\phi(t)=t+\cos t\) satisfies the paper's
requirements: it is entire, real on the real axis, and has bounded first
derivative on a fixed horizontal strip. Its first two derivatives on the
half strip have a fixed finite bound, so \(\beta\) is fixed. Its
unbounded values are permitted.

For standard Gaussian \(g\in\mathbb R^2\), unit \(v,w\), and
\(c=v^\top w\), simultaneous sign reversal makes the linear/cosine
mixed terms zero. The cosine product identity gives

\[
K(v,w)=\mathbb E[\phi(g^\top v)\phi(g^\top w)]
=c+e^{-1}\cosh c.
\tag{2}
\]

For any fixed integer \(J\), choose the candidate's distinct angles in
\((0,\pi/2)\). Their values \(a_j=\cos^2\theta_j\) are distinct.
For \(K_J=(K(v_i,v_j))\) and real \(b\in\mathbb R^J\),

\[
b^\top K_Jb
=\left\|\sum_jb_jv_j\right\|^2
+e^{-1}\sum_{k\ge0}\frac1{(2k)!}
\left\|\sum_jb_jv_j^{\otimes2k}\right\|^2.
\tag{3}
\]

The series is absolutely convergent because all inner products have
modulus at most one and the sum over \(i,j\) is finite. If (3) is zero,
each nonnegative summand vanishes. The all-first-coordinate component for
\(k=0,\ldots,J-1\) gives \(\sum_jb_ja_j^k=0\).
The corresponding Vandermonde determinant is nonzero, proving
\(\mu_J=\lambda_{\min}(K_J)>0\). No rate for \(\mu_J\) as
\(J\to\infty\) is needed: \(J\) is fixed after the claimed headline
constant is fixed, and before the gap/label limit.

## 3. Empirical event and adaptive-space rank lower bound

For independent initialized rows \(g_i\), let
\(H_{ij}=\phi(g_i^\top v_j)\) and \(G_{n,J}=H^\top H/n\).
Since \(|\phi(G)|\le|G|+1\) and \(G\) is standard normal,

\[
\mathbb E|\phi(G)|^4\le8(\mathbb E|G|^4+1)=32.
\]

Cauchy–Schwarz therefore bounds the second moment of every product of
two entries in one row by 32. Independence across rows, Chebyshev, and
an entrywise union bound yield

\[
\Pr\{G_{n,J}\not\succeq(\mu_J/2)I\}
\le\frac{128J^4}{n\mu_J^2}.
\tag{4}
\]

The conversion used here is
\(\|G_{n,J}-K_J\|_{\rm op}\le J\max_{a,b}|(G_{n,J}-K_J)_{ab}|\),
with entry threshold \(\mu_J/(2J)\). Correlation between different
entries within a row is immaterial.

On the complementary event, suppose a space \(E\) has approximants
\(u_j\) at the \(J\) test directions with coordinate error at most
\(\eta\). Put \(A=H/\sqrt n\) and
\(B=[u_1,\ldots,u_J]/\sqrt n\). If \(\dim E<J\), then
\(B\) has a unit null vector \(b\). Consequently

\[
\sqrt{\mu_J/2}\le\|Ab\|_2
=\|(A-B)b\|_2\le\|A-B\|_F\le\sqrt J\eta.
\tag{5}
\]

Thus \(\eta<\sqrt{\mu_J/(2J)}\) forces \(\dim E\ge J\).
The argument is simultaneous over all spaces, including initialization-
dependent spaces and supports; it uses no union bound over their choices.
The finite test inputs are passive evaluation directions, not added
training samples. This is a lower bound on actual required source rank.

## 4. Converting rank into the necessary onset

Fix the proposed activation/depth-only headline constant \(C>0\).
At \(m=d=2\), write \(z=Y/\lambda\) and \(\ell=\log(en)\).
The retained-state bound is

\[
S_n\le16C+(C/2)^3z^4\ell^8.
\tag{6}
\]

Choose \(J=\lfloor16C\rfloor+2\), so
\(\Delta_C=J-16C>1\), and let \(A_C=(C/2)^3>0\).
For \(Y<\sqrt{\mu_J/(2J)}\), (1), (4), and (5), followed by
metric injectivity, imply \(S_n\ge J\) on the empirical event.
Compatibility with (6) therefore requires

\[
\ell\ge c_Cz^{-1/2},\qquad
c_C=(\Delta_C/A_C)^{1/8}>0,
\quad\text{or equivalently}\quad
n\ge e^{c_Cz^{-1/2}-1}.
\tag{7}
\]

For any fixed \(\varepsilon>0\), the event has probability at least
\(1-\varepsilon\) once
\(n\ge128J^4/(\varepsilon\mu_J^2)\). That auxiliary threshold is
fixed independently of the shrinking training gap and labels. If (7)
fails above that threshold, source compliance and (6) can hold together
with probability at most \(\varepsilon\). This is an upper bound on
success probability, not merely a deterministic coefficient-count issue.

## 5. The shrinking-gap/label family is admissible

Take two unit training inputs of correlation \(c_0\in(0,1)\), tending
to one, and two layers with the same fixed activation. If the covariance
at one layer has diagonal \(q_j\) and off-diagonal \(c_j\), the same
Gaussian calculation as (2) gives

\[
q_{j+1}=q_j+e^{-q_j}\cosh q_j,\qquad
c_{j+1}=c_j+e^{-q_j}\cosh c_j,
\quad q_0=1.
\tag{8}
\]

For fixed positive \(q\), the latter map is strictly increasing on
\([0,q]\). Induction gives \(0<c_j<q_j\). Thus
\(\gamma=q_2-c_2>0\) is the smallest eigenvalue of the unnormalized
population Gram used by the paper, and continuity gives
\(\gamma\to0\). There is no missing factor of \(m\): the paper
defines \(\lambda=\gamma/m\), so here \(\lambda=\gamma/2\).

Set \(Y=\lambda^2\) and \(y_1=y_2=Y\); their label RMS is exactly
\(Y\), and \(z=\lambda\). Eventually
\(Y/\lambda=\lambda\le\beta^{-60}\), precisely the \(L=2\)
label condition, and \(0<\lambda\le1\). The original normalized
inputs are recovered by \(x_a=\sqrt2v_a\).

Every fixed polynomial in \(\gamma^{-1}\) and \(Y^{-1}\) is bounded
along this family by a fixed power of \(\lambda^{-1}\). Choose
\(n_\lambda=\lceil\lambda^{-A}\rceil\) with a larger fixed exponent
so it exceeds that proposed threshold. Then
\(\ell_\lambda=O(\log(1/\lambda))\), whereas
\(z^4\ell_\lambda^8\to0\). The rank event tends to probability one,
\(Y\) eventually meets (5)'s strict tolerance condition, and (6) tends
to the impossible bound \(S_n<J\). Equivalently, (7) reads
\(n\ge\exp(c_C/\sqrt\lambda-1)\). This verifies the claimed
superpolynomial obstruction with all activation/depth/dimension/sample
parameters fixed.

## Limits of the conclusion

- Both \(Y\) and \(z=Y/\lambda\) shrink. For fixed positive \(z\),
  (7) is only a constant gate, so this proof does not settle that narrower
  small-gap question.
- Fixed positive \(Y\) is not tested. In fact the paper's label cap
  prevents \(\lambda\to0\) with that \(Y\) fixed.
- Arbitrary output compression is not tested. The lower bound requires
  coordinate approximation of the initialized hidden-feature family and
  the present exact source-metric/retained-array mechanism.
- No quantitative rank-growth asymptotic in \(J\) is asserted. Finite
  positive \(\mu_J\), fixed after \(C\), is sufficient.
- No source probability, same-time denominator, numerical backend, or
  later trained-feature estimate is assumed. The obstruction is already
  present at initialization and is unaffected by a temporal proof repair.

## Frozen inputs

The complete candidate read for this check was
`HARMONIC_ONSET_ROUTE.md`, SHA-256
`a214a50824d6a60c54d79c6b6f0e0d5cefcc104b026c70c40bec170f5a96dea5`.
Relevant current-paper contracts were checked directly in
`paper/compact.tex` (`cp:data`, `cp:labels` and the constant convention),
`paper/compact_foundations.tex` (`cp:source-families`), and
`paper/compact_selected.tex` (`cp:selection`, `cp:selected`,
`cp:selected-tolerance`, `cp:harmonic`). Their full-file SHA-256 values
are respectively
`460f29eda118ffe5bbc24be3a04d1a25c5e4a9bddb0744f8235d97a3674cabfe`,
`6a49f8e35bb637416b7e330f7ace06286e482c942302bf57a46c8253a4cffbf0`, and
`3add2b694f38a4d7dbce90e51dafd375a7e8dee2e06d26b2d5af451bddb44885`.
