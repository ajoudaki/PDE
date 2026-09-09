# Two-Scale Forest Rescue and Its Remaining Circularity

## Claim level

This note records a narrow but rigorous conclusion about the factorial
finite-width obstruction in `CHRONOLOGICAL_FOREST_AUDIT.md`.

- The obstruction **does** falsify uniform finite-width moment bounds and
  annealed termwise absolute summation.
- It **does not** falsify convergence in probability of normalized
  observables in the iterated order: first width, then response cutoff and
  mesh removal.
- The rescue below is complete for the row-backtracking toy sector.  Its
  extension to the full nonlinear reachable tangent remains conditional on
  two explicit lemmas.  In particular, localization cannot be justified by
  assuming the stability it is meant to prove.

## 1. Exact row-backtracking calculation

Let one normalized Gaussian row be represented by

\[
 S_n=(GG^*)_{ii}=\frac1n\chi_n^2.
\]

Then, exactly,

\[
 \mathbb E S_n^k
 =\prod_{r=0}^{k-1}\left(1+\frac{2r}{n}\right).
\tag{1}
\]

Writing the product by collision-defect number gives

\[
 \mathbb E S_n^k=\sum_{d=0}^k m_{n,k,d},\qquad
 m_{n,k,d}=e_d\!\left(0,\frac2n,\ldots,
                      \frac{2(k-1)}n\right),
\]

and the elementary-symmetric-polynomial bound yields

\[
 m_{n,k,d}\le \frac1{d!}\left(\frac{k(k-1)}n\right)^d,
 \qquad
 \sum_{d\ge1}m_{n,k,d}
 \le e^{k(k-1)/n}-1.
\tag{2}
\]

Thus every fixed response grade has the expected leading-width value, while
the all-grade moment sum is nonuniform because grades of order at least
`sqrt(n)` see collisions.

## 2. Localization removes the false moment obstruction

For fixed `L>1`, set `E_(n,L)={S_n<=L}`.  The chi-square Chernoff bound is

\[
 \Pr(E_{n,L}^c)
 \le \exp\!\left[-\frac n2(L-1-\log L)\right].
\tag{3}
\]

Assume that the already-time-integrated star series has the deterministic
localized majorant

\[
 |a_k|h^kS_n^k\mathbf1_{E_{n,L}}\le A q^k,
 \qquad q=CLh<1.
\tag{4}
\]

Choose `K_n=n^(1/3)` (any `K_n=o(sqrt(n))` works).  Equations (2)--(4) give

\[
 \sum_{k\le K_n}q^k\sum_{d\ge1}m_{n,k,d}
 \le \frac{e^{K_n^2/n}}n\sum_{k\ge0}q^k k^2
 =O_q(n^{-1}),
\tag{5}
\]

whereas, pathwise on `E_(n,L)`,

\[
 \sum_{k>K_n}|a_k|h^kS_n^k
 \le \frac{Aq^{K_n+1}}{1-q}.
\tag{6}
\]

Consequently the omitted collision/depth sector converges to zero in
probability.  Its exploding high moments are caused by exponentially rare
large rows, not typical order-one response.

This calculation also shows that no width-dependent training mesh is needed.
One can choose a fixed short block with `q<1`, take `n->infinity` for each
fixed truncation/program, remove the response cutoff, and finally concatenate
finitely many blocks.  A width-dependent program length would not follow
from fixed-program MFP and is therefore deliberately avoided.

## 3. Candidate typed defect expansion

For fixed observable grade `g`, port number `p`, response grade `k`, and
equality defect `d`, the natural full-diagram target is

\[
 W_{g,p,k,d}^{(n)}
 \le A_{g,p}C_{g,p}^k k!
      \frac{(C_{g,p}k^2/n)^d}{d!}.
\tag{7}
\]

For an orientable genus defect `gamma`, the analogous activity is expected
to be `C k^4/n^2`; nonorientable/equality corrections occur at activity
`C k^2/n`.  These powers are combinatorial targets, not yet theorems for the
nonlinear adaptive forest.

For centered fluctuation observables the grading must be shifted: collisions
forced by the external `sqrt(n)` scaling belong to the leading covariance
sector.  Only defects above that forced count are remainders.

## 4. The three actual lemmas

The row calculation reduces, but does not solve, the full problem.  A valid
two-scale calculus needs:

1. **Reachable good event.**  Events `E_(n,L,T)` of probability tending to
   one that control the required primal, operator, occupation, and tangent
   quantities throughout a short time block.
2. **Localized joint analytic estimate.**  On `E_(n,L,T)`, the complete
   already-time-integrated grade-`k` diagram mass is at most `A q^k`, with
   `q<1`, uniformly in width and finite-step mesh.  Gate derivatives, tree
   automorphisms, partial-order volumes, and Wick gluings must be treated
   jointly.
3. **Defect insertion.**  Each excess equality/nonorientable defect costs
   activity `Ck^2/n` and each orientable handle costs `Ck^4/n^2`, after the
   correct external-port regrading.

The first two lemmas cannot prove one another by a closed loop.  If the good
event includes the desired tangent bound and the localized analytic estimate
is then used to claim that same tangent bound, the calculus has merely renamed
the original obstruction.

## 5. Correct signed resummation

For an exact finite-width tangent propagator

\[
 \partial_tR(t,s)=A_n(t)R(t,s),
\]

the legitimate resummation is the chronological exponential after an
independent bound on `A_n`.  On a good event,

\[
 \sup_{t\le T}\|A_n(t)\|\le C_L
 \quad\Longrightarrow\quad
 \|R(t,s)\|\le e^{C_L(t-s)}.
\tag{8}
\]

If `A_n=-B_n^*B_n+E_n`, retain the dissipative sign:

\[
 \|R(t,s)\|
 \le \exp\!\int_s^t\|E_n(u)\|\,du.
\tag{9}
\]

Replacing `e^{-tS_n}` by the annealed absolute majorant `e^{tS_n}` is exactly
the invalid step exposed by the row example.  Conversely, calling a
response-dependent closure kernel a resolvent does not remove circularity;
it still needs a contraction or independent one-sided bound.

## 6. Mesh-removal order

Let `X_n` be the finite-width flow, `X_(n,M)` its fixed-mesh approximation,
`x_M` the fixed-program width limit, and `x` the limiting flow.  The valid
triangle is

\[
 \Pr(d(X_n,x)>\epsilon)
 \le \Pr(d(X_n,X_{n,M})>\epsilon/3)
   +\Pr(d(X_{n,M},x_M)>\epsilon/3)
   +\mathbf1_{\{d(x_M,x)>\epsilon/3\}}.
\tag{10}
\]

The required bridge is therefore

\[
 \lim_{M\to\infty}\limsup_{n\to\infty}
 \Pr(d(X_n,X_{n,M})>\epsilon)=0.
\tag{11}
\]

Fixed-program MFP handles only the middle term of (10).  Equations (3)--(7)
show how collision sectors could be compatible with (11); they do not supply
the independent localized Euler/tangent estimate needed for its first term.

For a full block decomposition, a schematic collision estimate has the form

\[
 \mathsf{Coll}_{R}(n,h,K)
 \lesssim \frac1h\big(e^{c_RK^2/n}-1\big)
 \lesssim_R \frac{K^2}{nh},
\tag{12}
\]

while a localized geometric forest tail has the form

\[
 \mathsf{Tail}_{R}(h,K)
 \lesssim_R h^{-1}(A_Rh)^K.
\tag{13}
\]

Hence the elementary compatibility conditions are

\[
 h\downarrow0,\qquad h^{-1}(A_Rh)^K\to0,
 \qquad K^2/(nh)\to0.
\tag{14}
\]

The exact row stress shows that `K=o(sqrt(n))` is not an artifact.  If
`k/sqrt(n)->c>0`, then the chi-square central limit theorem gives

\[
 S_n^k\ \Longrightarrow\ e^{c\sqrt2 Z},
\tag{15}
\]

so the grade-`k` row word no longer approaches its defect-zero value even in
probability.

## 7. What fixed-program MFP does and does not permit

A width-dependent program cannot be inserted directly into a theorem stated
only for each fixed program.  There are nevertheless two legal constructions.

### 7.1 Existential staircase

For each integer `j`, first freeze a localization radius `R_j`, a mesh `h_j`,
and a response cutoff `K_j` so that localization, deterministic block error,
and the tail (13) are at most `1/j`.  Only then use fixed-program MFP to choose
a width threshold `N_j` at which that one finite program has error at most
`1/j`.  Making `N_j` increasing and using the `j`-th frozen program on
`N_j<=n<N_(j+1)` gives a valid diagonal sequence.  This is rigorous but
noncomputable unless MFP supplies a convergence modulus.

### 7.2 Euler-first construction

The cleaner route never needs a growing-program theorem.  For every fixed
mesh `h`, MFP gives a deterministic finite-step limit `Y_h`.  If the stopped
finite-width exact flow satisfies a dimension-free Euler estimate

\[
 \|X_n-X_{n,h}\|_T\le C_Rh
 \quad\hbox{on }\{\tau_{n,R}>T\},
\tag{16}
\]

then joint fixed-program convergence for two fixed meshes gives

\[
 \|Y_h-Y_{h'}\|_T\le C_R(h+h').
\tag{17}
\]

Thus the `Y_h` form a Cauchy family; their limit defines the continuous-time
mean-field flow.  Compact-time convergence follows after removing the
stopping event.  This route makes the exact bottleneck especially clear:
prove a high-probability reachable tube and (16) without placing the unknown
tangent stability inside the definition of that tube.

Ordinary ODE theory would derive (16) from stopped bounds
`||F_n||<=B_R` and `||DF_n||<=L_R`, giving

\[
 \|X_n-X_{n,h}\|_T
 \le \tfrac12 B_R(e^{L_RT}-1)h.
\tag{18}
\]

But the earlier spike counterexamples show that normalized energy and matrix
operator norms alone do not give a dimension-free `L_R`.  Therefore (18) is
an implication, not a solution.  The calculus still needs a weaker
reachable-direction/occupation estimate sufficient for (16).

## Verdict

The finite-width factorial counterexample is not a fundamental negative
result against a width-first calculus.  It forces the claim mode to change
from uniform moments to localized convergence in probability.  Genus/defect
counting and fixed-program MFP are mutually compatible, even without an
explicit width-dependent schedule.  The remaining make-or-break issue is
whether a reachable exact-flow/Euler or tangent/occupation estimate can be
proved independently enough that localization and the forest bound are not
circular.
