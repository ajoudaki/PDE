# Scoped check of the generic residual-moment construction

2026-10-10. Checker: the `positive_arbitrary_labels` agent, assigned by the
study coordinator. Verdict: **PASS for the generic moment independence,
genericity, and strict replicated-minimum claims**, at the frozen source
version below. No mathematical correction is required for these claims.

The complete candidate was read, including its all-amplitude extension.
The independence assessment is narrower than a full independent review:
this checker previously authored the large-residual capture lemma used by
the coordinator and the candidate's Section 7. The moment-function
construction was not authored by this checker and was reconstructed here
without receiving the author's proof summary or another checker's verdict.
This is an internal scoped check, not an isolated promotion review.

## Frozen input and actual coverage

The scientific input for this check was the full
`NEGATIVE_LABEL_BOUNDARY.md`, frozen by its author at SHA-256

`fa1f21f8407401529248a6e1390f2bd4b07dc41b73f4a932f3ec2b25e297eedd`.

An earlier draft was also read while the author repaired formatting. The
final frozen file was then reread completely with `sed` ranges `1,280`,
`281,560`, and `561,880`; the last read reached EOF. `sha256sum` returned
the agreed hash after those reads. No earlier formatting artifact was
used to fill a gap in the frozen candidate.

No new scientific source beyond that assignment was fetched. The checker
had read `TANH_REPLICATION_CLASS.md` and `TANH_BAD_BASIN.md` for the earlier
capture task; those facts are disclosed as prior context, not additional
generic-moment evidence. Required proof, research, and canonical-notation
instructions were applied. No experiments or numerical rank tests were run.

## 1. Scalar-function independence

The candidate fixes \(p=ae_1\), with \(a>0\), and \(q>0\). With
\(t=p^\top x\), its scalar definitions are

\[
u=\tanh t,\quad\chi=1-u^2,\quad\tau=-2u\chi,\quad
h=\tanh(qu),\quad\psi=1-h^2,\quad\sigma=-2h\psi,
\]

\[
T=\psi\tau,\qquad
C=q^2\sigma\chi^2+q\psi\tau,\qquad
D=q\sigma u\chi+\psi\chi.
\]

The analytic separation argument is valid. If finitely many functions
\(F_k\) analytic near zero satisfy
\(\sum_k t^kF_k(e^{-2t})=0\), select the smallest Taylor order appearing
in a nonzero \(F_k\). After division by its exponential, a nonzero
polynomial in \(t\) would equal an exponentially decaying error.
That is impossible. Each scalar function above is analytic in
\(z=e^{-2t}\) near zero because \(u=(1-z)/(1+z)\); the finite point
\(qu=q\) is not a real pole of tanh. Real-analytic continuation in
\(t\) justifies using this argument after an identity on \((-a,a)\).

The three scalar independence tests were recomputed:

1. For \(\{h,\psi u,\sigma u^2,T,C\}\), division by \(\psi\)
   and multiplication by \(\cosh(qu)\) give
   \(b_0\sinh(qu)\cosh^2(qu)+P\cosh(qu)+Q\sinh(qu)=0\), with
   exactly the candidate's polynomials \(P,Q\). The exponential of
   order \(3qu\) first eliminates \(b_0\); the remaining exponential
   identity eliminates both polynomials. Their coefficients eliminate
   the other four constants. This uses \(q>0\), as assumed.
2. \(D/(\psi\chi)=1-2qu\tanh(qu)\) is nonconstant, establishing
   independence of \(\{\psi\chi,D\}\).
3. A relation between \(T,C\), divided by \(-2\psi\chi\), becomes
   \((b+cq)u+cq^2\tanh(qu)(1-u^2)=0\). The limit at \(u=1\),
   followed by a point in \((0,1)\), eliminates both coefficients.

Separating powers of \(t\) consequently proves the claimed independence
of the nine scalar functions in equation (8) and the four in equation
(9). There is no unproved numerical nondegeneracy premise.

## 2. Spherical decomposition, dimension, and genericity

Write \(x=(t/a,\rho z)\), with
\(\rho^2=1-t^2/a^2\) and \(z\in S^{d-2}\). A scalar relation among
the moment functions has coefficient vectors \(b,c\) and symmetric
coefficient matrices \(B,E\). Subtracting the relation at \(-z\)
extracts its linear part. The even part is a quadratic form constant
on the transverse sphere, hence its trace-free part vanishes.
Independence of \(T,C\) makes both transverse trace-free coefficient
matrices zero. Independence of the four functions in equation (9)
then makes the four transverse linear coefficient vectors zero.

For an explicit final check, write the remaining transverse blocks as
\(B_\perp=\beta I\), \(E_\perp=\varepsilon I\). The remaining relation
is

\[
\begin{aligned}
0={}&\beta_0h+\beta_1\psi u+\beta_2\sigma u^2
+\frac ta(b_1\psi\chi+c_1D)+\beta T+\varepsilon C\\
&+\frac{t^2}{a^2}\bigl[(B_{11}-\beta)T
                     +(E_{11}-\varepsilon)C\bigr].
\end{aligned}
\]

The nine-function independence annuls every coefficient, proving full
independence. For \(d=2\), the transverse space is one-dimensional,
so its trace-free matrices are identically zero; \(S^0=\{-1,1\}\)
still separates the linear and constant parts. The argument therefore
includes this smallest allowed dimension.

Counting upper-triangular entries gives

\[
N(d)=1+1+d+1+\frac{d(d+1)}2+\frac{d(d+1)}2+d
     =d^2+3d+3.
\]

Independence implies existence of \(N(d)\) evaluation columns spanning
\(\mathbb R^{N(d)}\). Thus the fixed first-\(N(d)\)-column determinant
is not identically zero on \((S^{d-1})^m\). For \(d\ge2\) this is a
connected real-analytic manifold; analytic continuation through charts
excludes an open zero set. Its nonzero set is therefore open dense.
The restriction to distinct nonantipodal samples is also open dense.
The evaluation map is consequently onto on the stated generic set.
No passage from genericity to every input configuration is made.

## 3. The reduced Hessian and every splitting direction

Let \(r^0\) satisfy the prescribed moments, and let the candidate
readout be \(s>0\), with labels \(sh-\gamma r^0\), \(\gamma>0\).
The actual residual is \(\gamma r^0\). Direct differentiation gives

\[
\partial_p h=q\psi\chi x,\qquad
\partial_qh=\psi u,\qquad
\partial_{pp}^2h=Cxx^\top,\qquad
\partial_{pq}^2h=Dx,\qquad
\partial_{qq}^2h=\sigma u^2.
\]

The moment equations therefore make the residual orthogonal to the
feature and its first derivatives, and make its contracted hidden
Hessian equal to \(\gamma I_{d+1}\). The reduced loss Hessian is
exactly equation (14). Its squared-Jacobian term plus
\(s\gamma(\|v\|^2+b^2)\) is positive definite because \(h\ne0\).
The latter follows from the moment \(\sum_a r_a^0\sigma_a u_a^2=1\).

The full Hessian was also reconstructed without assuming the replication
formula. For a full-network variation set
\(a_j=\delta A_{j,:}^\top\), \(b_i=\sum_j\delta W_{ij}\), and
\(c_i=\delta w_i\). At the replicated point,

\[
\delta Z_{ia}=u_a b_i+q\chi_a x_a^\top\bar a,
\]

\[
\delta^2Z_{ia}
=2\chi_a\sum_j\delta W_{ij}x_a^\top a_j
+\frac qn\tau_a\sum_j(x_a^\top a_j)^2.
\]

Contracting the second prediction derivative against \(\gamma r^0\)
eliminates every readout/hidden and mixed \(\delta W,\delta A\) term
by the three zero stationarity moments. The moment for \(D\), together
with the \(\psi\chi x\) moment, eliminates the mean top/lower mixed
term. The remaining contraction is

\[
s\gamma\left[
\frac1n\sum_i b_i^2
+(1-q)\|\bar a\|^2
+\frac qn\sum_j\|a_j\|^2\right].
\]

Here the coefficient \(1-q\) is checked using
\(\sum r^0 Cxx^\top=I_d\) and
\(\sum r^0 Txx^\top=I_d\), which imply
\(\sum r^0q^2\sigma\chi^2xx^\top=(1-q)I_d\).
After decomposing sums into their averages and variances, this is
precisely the coherent residual curvature plus the splitting terms in
equation (16), including its factor \(2s\gamma/(mn)\) and its lower
splitting factor \(q\). The assumed \(q>0\) makes both variance terms
strictly positive.

The Hessian kernel is therefore exactly
\(\delta A=0\), \(\delta W\mathbf1=0\), and
\(\mathbf1^\top\delta w=0\). These are the tangent equations of
the displayed affine manifold. The three stationarity moments also
make every point of that manifold critical, including unequal readout
entries and unequal row-weight entries. Thus the kernel is an actual
critical manifold, not an assumed higher-order flat direction.

Positive normal Hessian, continuity, and Taylor's formula give the
candidate's normal-gradient lower bound and finite-length trapping.
The argument applies in the stated positive constant mobility metric.
This establishes the open full-parameter attracting neighborhood; it
does not alone assert zero-readout reachability.

## 4. Capture, the extra moment, and probability scope

The small-label argument preserves the exact physical scaling:
\(\dot p=-\varepsilon^2\nabla_pJ\),
\(\dot q=-\varepsilon^2\partial_qJ\), and
\(\dot c=-\partial_cJ\). At zero scale the explicit readout path
approaches the strict minimum. Finite-time continuity followed by the
strong-convexity sublevel barrier proves capture for small positive
scale. Exact replication then preserves the actual dynamics at every
width, and finite-time pullback supplies an open basin on \(w=0\).

The mixed-label choice in Section 3 is valid in both stated cases. If
\(h\) is mixed, small \(\gamma\) preserves two opposite signs. If its
nonzero entries have one sign, orthogonality to \(r^0\), together with
the nonzero \(\sigma u^2\) moment, forces both residual signs among
those entries; large \(\gamma\) gives mixed labels.

For Section 7, every original moment function is odd under
\(x\mapsto-x\): in particular \(D\) is even and \(Dx\) is odd.
The additional constant function is therefore independent. The new
zero-sum residual moment forces the nonzero \(r^0\) to have both signs.
The same determinant argument now applies at \(N(d)+1\) samples.
The prescribed hidden Hessian is exactly \(I_{d+1}\), meeting the
capture hypothesis. The cylinder and block-Hessian estimates in that
section preserve the scale factors and give all-amplitude capture.
This last mechanism was previously authored by this checker and is
checked here for consistency, not claimed as an independent review of
its origin.

The added retained-loss identity is correct for every basin trajectory,
not only its symmetric reference path: zero initial readout makes the
initial loss depend only on the labels, and the attracting critical
manifold has constant terminal loss. Orthogonality gives

\[
\frac{\mathcal L(\infty)}{\mathcal L(0)}
=\frac{M^2\|r^0\|^2}{\|h_*\|^2+M^2\|r^0\|^2}.
\]

The full-rank-intersection argument, interpolation witness, and positive
Gaussian mass all follow from the stated nonantipodal data condition
and full-support finite-dimensional Gaussian law. These assertions do
not bound the mass away from zero as width grows. The candidate's
explicit limitations on high-probability Gaussian fitting, exceptional
input configurations, and unrestricted label directions remain necessary.

## Outcome

No blocking mathematical objection was found in the assigned generic
moment construction or its strict replicated-minimum consequences.
The stronger theorem establishes, on an open dense input class when
\(m\ge d^2+3d+4\), a constructed mixed label direction with positive
fixed-width Gaussian failure probability at every amplitude. It does
not resolve the user's high-probability large-width fitting target.

No candidate scientific text was changed during this check. Separately,
at the coordinator's request, the two missing TeX backslashes in
equation (27) of the checker's own `TANH_LARGE_RESIDUAL_CAPTURE.md` were
fixed before this audit. That file's new frozen SHA-256 is
`c2d11d60db89a68766e793a3f9384285b3a8099dc1db0d437b2656b91c2efb5f`.
