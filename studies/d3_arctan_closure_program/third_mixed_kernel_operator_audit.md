# Exact third-mixed kernel: factorization and cavity recursion

This note audits the operator estimate required after summing the centered
feeding rows.  It is self-contained and uses the normalized convention

\[
 \langle u,v\rangle_n=n^{-1}\sum_{a=1}^n u_av_a,
 \qquad (b\otimes x)u=b\langle x,u\rangle_n,                              \tag{1}
\]

with bare top matrix

\[
 G_{ra}=n^{-1/2}g_{ra},\qquad g_{ra}\stackrel{\rm iid}{\sim}N(0,1),
 \qquad W=G+P.                                                           \tag{2}
\]

All operator norms below are the usual Euclidean matrix operator norm.  For
equal widths this is also the operator norm for the normalized Hilbert
spaces.

Fix a source entry `e=(s,l)`, two feeding rows `r,q` distinct from one
another and from `s`, and a lower output coordinate `j`.  Write
`Delta_e`, `Delta_r`, and `Delta_q` for commuting replacement differences.

## 1. Exact four-corner identity

For a scalar quantity `z`, set

\[
 \eta_e=z^e-z,\qquad \eta_q=z^q-z,
 \qquad \eta_{qe}=z^{qe}-z^q-z^e+z.                                    \tag{3}
\]

Then, with

\[
 \mathfrak D^2d(z;a,b)=\int_0^1\!\int_0^1d''(z+ua+vb)\,du\,dv,           \tag{4}
\]

the following identity is exact:

\[
\begin{split}
 \Delta_q\Delta_ed(z)
  ={}&Dd(z+\eta_q+\eta_e,
         z+\eta_q+\eta_e+\eta_{qe})\,\eta_{qe}\\
    &+\mathfrak D^2d(z;\eta_q,\eta_e)\,\eta_q\eta_e.                    \tag{5}
\end{split}
\]

For `d(z)=(1+z^2)^(-1)`, all divided differences in (5) are bounded by
absolute constants.  No Taylor remainder has been discarded.

For `z=Wx`, the corresponding field increments are also exact:

\[
 \eta_e=W\Delta_ex+(\Delta_eW)x^e,
 \qquad
 \eta_q=W\Delta_qx+(\Delta_qW)x^q,                                     \tag{6}
\]

and

\[
\begin{split}
 \eta_{qe}={}&W\Delta_q\Delta_ex
   +(\Delta_qW)(\Delta_ex)^q
   +(\Delta_eW)^q(\Delta_qx)^e
   +(\Delta_q\Delta_eW)x^{qe}.                                         \tag{7}
\end{split}
\]

Thus (6)--(7) retain every learned-rank-one and covariance correction.

The exact product rule for `B=A d(z)` is

\[
\begin{split}
 \Delta_q\Delta_eB={}&A\,\Delta_q\Delta_ed
  +(\Delta_qA)(\Delta_ed)^q
  +(\Delta_eA)^q(\Delta_qd)^e
  +(\Delta_q\Delta_eA)d^{qe}.                                          \tag{8}
\end{split}
\]

For row `r`, the part of `Delta_q Delta_e R_{2,j}` carrying the fresh bare
outer coordinate is therefore

\[
 \boxed{
 \begin{split}
 K_{rq,e,j}^{G}={g_{rj}\over\sqrt n}\big[&
 A_rD^{(1)}_{rq,e}\eta_{r,qe}
 +A_rD^{(2)}_{rq,e}\eta_{r,q}\eta_{r,e}\\
 &+(\Delta_qA_r)(\Delta_ed_r)^q
 +(\Delta_eA_r)^q(\Delta_qd_r)^e
 +(\Delta_q\Delta_eA_r)d_r^{qe}
 \big],                                                               \tag{9}
 \end{split} }
\]

where `D^(1)` and `D^(2)` are the two bounded divided differences in (5).
Terms with an outer `Delta P_{rj}` are separate learned terms; their
normalization is smaller and is recorded below.  Formula (9) is the exact
third-mixed feeding kernel, not a schematic Hessian.

## 2. Common-base matrix form

At one common trajectory define

\[
 v_e=\Delta_ex,qquad
 U=(u_q)_q,\quad u_q=\Delta_qx,qquad
 V_e=(v_{q,e})_q,\quad v_{q,e}=\Delta_q\Delta_ex.                        \tag{10}
\]

Also put

\[
 a=Wv_e,\qquad M=WU,qquad N=WV_e,qquad
 c_j=(G_{rj})_{r=1}^n.                                                   \tag{11}
\]

Thus `a_r` has the entry-field scale `n^(-1)`, `M_rq` has the row-field
scale `n^(-1/2)` off the diagonal, and `N_rq` has the third-mixed field
scale `n^(-3/2)` entrywise.  The linear part of (9) is the exact
diagonal--matrix decomposition

\[
 K_{e,j}^{\rm lin}
  =D_{c_j\odot A\odot d'(z)}N
   +D_{c_j\odot A\odot d''(z)\odot a}M
   +K_{e,j}^{A}.                                                        \tag{12}
\]

The endpoint matrix `K^A` has the same form, because
`Delta A` is the time integral of a bounded diagonal gate times the field
increments (6)--(7).

The useful deterministic event is

\[
\begin{array}{lll}
 \|W\|_{\rm op}\le L,&\|U\|_{\rm op}\le L,&
 \|V_e\|_{\rm op}\le L/n,\\[2mm]
 \|c_j\|_\infty\le L/\sqrt n,&
 \|a\|_\infty\le L/n,&
 \|A\|_\infty\le L .                                                   \tag{13}
\end{array}
\]

On (13), (12) gives

\[
 \|K_{e,j}^{\rm lin}\|_{\rm op}\le {C L^C\over n^{3/2}}.              \tag{14}
\]

This exhibits the missing `n^(-1/2)`: it comes from the outer bare column,
while the entry field or the mixed response supplies `n^(-1)`.

## 3. Why the exact nonlinear gate preserves (14)

On the logarithmic-moment good event, the off-diagonal row increments in
(5) are smaller than a fixed constant.  Since `d` is analytic in a fixed
complex strip about the real axis, `D^(1)` and `D^(2)` have absolutely
convergent expansions in the entries of `M`, `a`, and `N`.  Every term is
a diagonal factor times a Hadamard product such as

\[
 N\odot M^{\odot k},qquad
 D_a M^{\odot k}.                                                       \tag{15}
\]

For arbitrary square matrices,

\[
 \|X\odot Y\|_{\rm op}\le\|X\|_{\rm op}\|Y\|_{\rm op}.              \tag{16}
\]

Indeed `X odot Y=V^*(X tensor Y)V`, where `Ve_i=e_i tensor e_i` is an
isometry.  Iterating (16) bounds (15) by

\[
 \|N\|_{\rm op}\|M\|_{\rm op}^k,qquad
 \|a\|_\infty\|M\|_{\rm op}^k.                                       \tag{17}
\]

Consequently the full two divided-difference terms in (9), not only their
linearization, satisfy (14) on (13).  The complement of the good event has
arbitrarily high polynomially small probability for `p <= c log n`; the
bounded exact divided differences control it without expanding.

This calculation also shows that no special sign of `d''` is needed at
this leaf.  Arctan is used through bounded exact divided differences and
through the characteristic cancellation in the propagators that define
`U` and `V_e`.

## 4. Learned rows have the same or better normalization

The Euler formula gives, entrywise,

\[
 P_{rj}^k={h\over n}\sum_{t<k}B_r^tX_{2,j}^t,                            \tag{18}
\]

and therefore

\[
 |P_{rj}^k|\le {C_T(1+|A_r^0|)\over n},
 \qquad \|P^k\|_{\rm op}le
 h\sum_{t<k}\|B^t\|_n\|X_2^t\|_n\le C_T(1+\|A^0\|_n).                \tag{19}
\]

More generally, if `||v||_n <= C/n`,

\[
 |(P^kv)_r|
 \le h\sum_{t<k}|B_r^t|\,|\langle X_2^t,v\rangle_n|
 \le {C_T(1+|A_r^0|)\over n}.                                         \tag{20}
\]

Thus an outer learned coordinate is `n^(-1)`, better than the bare
`n^(-1/2)`, and a learned entry field has the required `n^(-1)` scale.
The `Delta P` terms obtained by differentiating (18) factor through `U`
and `V_e` and obey (14) under (13).

## 5. The early-flow kernel really has the good operator scale

At the first nontrivial slab the lower causal response is one common
operator `S_0`.  Up to bounded diagonal gates,

\[
 U=S_0W^*D_b,qquad
 v_e=S_0e_l\,{\delta g_{sl}B_s\over\sqrt n},                             \tag{21}
\]

so

\[
 a=Wv_e,qquad
 V_e=S_0W^*D_{\theta_e},qquad
 \theta_e=A\odot d'(z)\odot a+\hbox{bounded learned terms}.             \tag{22}
\]

Two-row cavity gives

\[
 \|a\|_\infty\le {L\over n},qquad
 \|D_{\theta_e}\|_{\rm op}\le {L^C\over n},qquad
 \|V_e\|_{\rm op}\le {L^C\over n}.                                  \tag{23}
\]

Substitution in (12) proves `||K_e||_op <= L^C n^(-3/2)` for the actual
leading flow.  In particular the leading network kernel is a
diagonal--Gram--diagonal object; it is not a coherent arbitrary matrix with
entries `n^(-2)`.  There is no leading-order reachable counterexample to
the desired operator scale.

## 6. The unresolved hypothesis in (13)

The entry-field bound in (13) can be obtained from a one-row cavity:

\[
 (Gv_e^{(r)})_r\mid v_e^{(r)}
 \sim N(0,\|v_e^{(r)}\|_n^2),qquad \|v_e^{(r)}\|_n=O_T(n^{-1}),          \tag{24}
\]

and the replacement `v_e-v_e^(r)=Delta_rDelta_e x` is `n^(-3/2)`.
Union over `r` costs only logarithmic factors.  Hence `||a||_infty <=
L/n` is consistent with the row-summed second-mixed estimate.

The serious condition is

\[
 \boxed{\qquad \|V_e\|_{\rm op}\le L/n.\qquad}                         \tag{25}
\]

Scalar mixed FD/RD estimates give only

\[
 \|v_{q,e}\|_n\le L/n^{3/2}
 \quad\Longrightarrow\quad
 \|V_e\|_{\rm HS}\le L/\sqrt n,                                      \tag{26}
\]

which is a factor `sqrt(n)` short of (25).

At a **common differential base point**, (25) would follow from a common
signed propagator.  The mixed-Jacobian matrix obeys

\[
 \dot V_e=\mathcal H(t)V_e+\mathcal S_e(t),qquad
 \|\mathcal S_e(t)\|_{\rm op}\le {L^C\over n},                          \tag{27}
\]

where the source is a sum of factors of the form

\[
 W^*D_{A\odot d'(z)\odot (Wv_e)}
 \quad\hbox{and learned analogues}.                                    \tag{28}
\]

If the common evolution `Phi(t,s)` generated by `H` satisfied
`sup ||Phi(t,s)||_op <= C_T poly(L)`, Duhamel would give (25).  But this is
the arbitrary-time signed response estimate: after characteristic dressing
the diagonal arctan curvature cancels, while the off-diagonal bath
commutator remains.  Energy alone does not bound this propagator.

Gradient symmetry does not fix the issue.  `H(t)` is a Hessian and hence
symmetric at each time, but it is sign-indefinite, and time-ordered products
of symmetric matrices need not be contractive or symmetric.  Thus no
positive-energy estimate for `Phi` follows from the gradient structure.

## 7. Why a fourth finite-difference cavity does not terminate the proof

For finite row replacements, each column of `V_e` has its own averaged
propagator:

\[
 v_{q,e}=\int_0^T\Phi_q(T,t)s_{q,e}(t)\,dt.                              \tag{29}
\]

Even if every `||Phi_q||_op <= L`, the matrix with columns
`(Phi_qs_{q,e})_q` can have operator norm as large as its Frobenius norm:
the columnwise propagators may align the columns.  To apply matrix
Bernstein one replaces `Phi_q` by a common `q`-cavity propagator.  The
replacement error is

\[
 \Delta_u\Delta_q\Delta_r\Delta_eX_2,                                  \tag{30}
\]

a fourth mixed difference.  Freezing that fourth-order family jointly
requires a fifth cavity, and so on.

At order `m`, each additional distinct row gives the correct extra
`n^(-1/2)` in every individual leaf.  Summing the fresh rows recovers the
Hilbert--Schmidt scale, but converting the family of row-dependent
propagators into one jointly conditionable family again asks for the next
mixed difference.  The exact four-corner identity (5) repeats at every
order; arctan supplies bounded coefficients but does not set the
off-diagonal term to zero.  Hence the pure finite-replacement cavity
hierarchy has no finite algebraic stopping level.

There are two ways it could be closed:

1. prove the common signed-propagator bound in (27), and work with
   common-base Gaussian/Malliavin derivatives rather than columnwise finite
   differences; or
2. prove a summable all-orders cluster/cavity expansion whose `m`th level
   gains enough factorial or Euler-`h` decay.

The available identities provide neither.  The Euler `h` helps newest
innovations, but old row carriers are reused, so an `m`th cavity replacement
does not automatically gain `h^m/m!`.

## 8. Verdict

The exact third-mixed kernel has the favorable decomposition (9)--(12).
Under the matrix response bounds in (13), its operator norm is indeed

\[
 \|K_e\|_{\rm op}\le n^{-3/2}C_T\,\mathrm{poly}(p+\log n)               \tag{31}
\]

for logarithmic moments.  All leading bare, learned, endpoint, and exact
divided-difference terms respect this normalization, and the first
nontrivial Euler slab verifies it directly.

However, (31) does **not** follow from the scalar FD/RD and energy bounds
already available.  It is equivalent to the matrix mixed-response estimate
`||V_e||_op=O(n^(-1))`, or to a uniform common signed-propagator bound.  A
fourth cavity proves the frozen source part but creates a fourth mixed
replacement error, and the same mechanism repeats indefinitely.  Gradient
symmetry and exact arctan dressing do not terminate that recursion because
the off-diagonal bath commutator survives.
