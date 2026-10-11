# Internal cross-check of the positive-loss escape construction

Verdict: **PASS for the assigned mathematical scope.** No blocking gap was
found in the moving escape construction, its use of global existence, or
the finite-accumulation stationarity lemma. This is a reused-author-context
cross-check within the study, not an isolated promotion review and not a
promotion approval.

Checker: the scoped stationary-classification agent
/root/tanh_stationary_classification, author of the separate
TANH_NECESSARY_GEOMETRY.md contribution. The present check was performed
after that contribution was frozen, in the same agent context. The checker
did not author the escape candidate, but has received supervisor messages
and has participated in the same research program; this is not blind review.

## Frozen input and coverage

The only scientific input read for this assignment was the complete file

studies/label_scale_obstruction_20261007/GLOBAL_FAILURE_ALTERNATIVES.md

with SHA256

37ac6f2ec3316b42dc73f775b20d70467a0a04194338707de102f5cfff851a1f.

The hash was checked before the audit and again after this report was
written; both checks returned the frozen hash above. The full file was read without
truncation. Detailed reconstruction focused on the sections “Global
existence and finite energy,” “Every finite accumulation point is
stationary,” and “A moving, positive-loss trajectory escaping to infinity.”
The remaining sections were read for consistency and claim scope; they
were not the subject of a second complete promotion-style audit.

No other scientific source, external theorem source, other study, or
experiment was used. The existing mathematical and process instructions
were reused. All mathematical checks below are direct derivations.
Only this assigned report was written; the frozen candidate was not edited.

## 1. Canonical model and normalization

The candidate uses \(X\in\mathbb R^{d\times m}\) with unit columns and

\[
U=\tanh(AX),\qquad H=\tanh(WU),\qquad
f=H^\top w/n,\qquad r=f-y,\qquad
\mathcal L=\|r\|^2/m.
\]

Its column notation \(x_a\) means the already-normalized input column:
it equals \(x_a/\sqrt d\) in a convention where the unnormalized original
sample has norm \(\sqrt d\). There is no additional input scaling inside
the candidate's forward pass.

The parameter mobilities in the order \((A,W,w)\) are \((n,1,n)\).
Writing \(S=1-U^2\) and \(D=1-H^2\), differentiation gives

\[
\begin{aligned}
\dot w&=-\frac2mHr,\\
\dot W&=-\frac2{mn}[(wr^\top)\odot D]U^\top,\\
\dot A&=-\frac2m
 \{W^\top[(wr^\top)\odot D]\odot S\}X^\top.
\end{aligned}
\]

These coincide with the frozen candidate. In particular, the second-layer
equation retains its \(1/n\), while the first-layer and readout mobility
factors cancel their gradient \(1/n\).

## 2. Global existence and finite-cluster stationarity

Let \(M\) be the positive diagonal mobility operator with blocks
\(nI,I,nI\). Its inverse metric is

\[
\|\delta\theta\|_{M^{-1}}^2
=\|\delta A\|_F^2/n+\|\delta W\|_F^2+\|\delta w\|^2/n.
\]

The chain rule along \(\dot\theta=-M\nabla\mathcal L\) gives

\[
\frac{d\mathcal L}{dt}
=-\nabla\mathcal L^\top M\nabla\mathcal L
=-\|\dot\theta\|_{M^{-1}}^2.
\]

Integration and Cauchy--Schwarz therefore imply

\[
\|\theta(t)-\theta(s)\|_{M^{-1}}
\leq \sqrt{(t-s)\,[\mathcal L(s)-\mathcal L(t)]}
\leq \sqrt{(t-s)\mathcal L(0)}.
\]

If the maximal existence interval had finite endpoint \(T\), the last
bound would make the trajectory Cauchy as \(t\uparrow T\). The limit is a
finite parameter vector. The vector field is smooth at every finite vector,
so the locally unique solution from that limit extends the original one.
This contradicts maximality. Thus the solution exists uniquely for every
finite positive time. The loss has a nonnegative limit
\(\mathcal L_\infty\), because it is nonincreasing and bounded below.

Now suppose \(t_k\to\infty\) and \(\theta(t_k)\to\theta_*\). Define

\[
Q(\theta)=\|M^{1/2}\nabla\mathcal L(\theta)\|^2.
\]

If \(\theta_*\) were not stationary, continuity would give a closed metric
ball of radius \(\rho>0\) about \(\theta_*\) on which \(Q\geq c>0\).
The speed in that same metric has a finite upper bound \(C>0\) there,
because the ball is compact and the vector field is continuous.
Eventually \(\theta(t_k)\) is in the ball of radius \(\rho/2\). The
trajectory must then spend at least \(\delta=\rho/(2C)\) further time
inside the larger ball: an earlier first exit would contradict the speed
bound and the distance to its boundary.

Consequently

\[
\mathcal L(t_k)-\mathcal L(t_k+\delta)\geq c\delta.
\]

Both loss values converge to \(\mathcal L_\infty\), a contradiction.
Hence every finite accumulation point is stationary. This argument does
not require a globally bounded trajectory, a globally bounded Hessian, or
disjoint visit intervals. One late visit already contradicts the vanishing
remaining loss drop. Those possible loopholes are therefore absent.

## 3. The four samples satisfy the stated geometry

The example chooses \(d=2\), \(m=4\), \(n\geq4\), and

\[
\frac34<s_1<s_2<1,\qquad
x_{k,\pm}=(s_k,\pm\sqrt{1-s_k^2})^\top.
\]

The four columns are unit vectors. Each sign pair is distinct because
\(s_k<1\), and the two pairs have different first coordinates. No two
are antipodal because every first coordinate is positive.

Set \(\vartheta_k=\arccos s_k\). Their polar angles are
\(\pm\vartheta_1,\pm\vartheta_2\), with
\(0<\vartheta_2<\vartheta_1<\arccos(3/4)\). Thus all angular
separations are less than \(2\arccos(3/4)\), and every pairwise inner
product exceeds

\[
\cos(2\arccos(3/4))=2(3/4)^2-1=1/8>0.
\]

The labels are \(\alpha\) for both \(k=1\) columns and \(\beta\) for both
\(k=2\) columns, where \(\alpha>\beta>0\). All geometric and label
assumptions used by the subsequent argument are satisfied.

## 4. Invariance and the reduced flow

Write \(\varepsilon_1=(1,0)^\top\). The invariant family is

\[
A_i=p\varepsilon_1^\top,\qquad
W_{ij}=q/n,\qquad w_i=v,
\qquad p(0),q(0)>0,\quad v(0)=0.
\]

For each sample type \(k\), define

\[
u_k=\tanh(ps_k),\qquad h_k=\tanh(qu_k),\qquad
r_1=vh_1-\alpha,\quad r_2=vh_2-\beta.
\]

Every first-layer coordinate equals \(u_k\); summing the \(n\) entries
\(q/n\) gives second-layer preactivation \(qu_k\). Averaging the \(n\)
readout contributions \(vh_k\) by \(1/n\) gives prediction \(vh_k\).
There are two identical residual contributions of each type, so

\[
\mathcal L=\frac{2r_1^2+2r_2^2}{4}
=\frac12(r_1^2+r_2^2).
\]

The three velocity computations independently reproduce all factors:

\[
\begin{aligned}
\dot w_i
 &=-\frac24\,2\sum_k r_kh_k
   =-\sum_k r_kh_k,\\
\dot W_{ij}
 &=-\frac2{4n}\,2v\sum_k r_ku_k(1-h_k^2)
   =-\frac vn\sum_k r_ku_k(1-h_k^2),\\
\dot A_{j,1}
 &=-\frac24\,2vq\sum_k
     r_ks_k(1-u_k^2)(1-h_k^2)\\
 &=-vq\sum_k r_ks_k(1-u_k^2)(1-h_k^2),\\
\dot A_{j,2}&=0.
\end{aligned}
\]

For the \(A\) calculation, summing
\(W_{ij}w_i=(q/n)v\) over \(i\) gives \(qv\). The last coordinate
cancels between the two signs of each sample type.

The right-hand side remains tangent to the stated family. Solving the
reduced equations therefore produces a full solution with the prescribed
initial condition, and uniqueness of the full smooth flow proves invariance.
The reduced equations are exactly

\[
\begin{aligned}
\dot v&=-\sum_k r_kh_k,\\
\dot q&=-v\sum_k r_ku_k(1-h_k^2),\\
\dot p&=-vq\sum_k r_ks_k(1-u_k^2)(1-h_k^2).
\end{aligned}
\]

They equal the negative Euclidean gradient of
\(\frac12(r_1^2+r_2^2)\) in \((p,q,v)\). The induced full parameter
metric independently confirms this:

\[
\frac1n(n\,\delta p^2)
+n^2(\delta q/n)^2+\frac1n(n\,\delta v^2)
=\delta p^2+\delta q^2+\delta v^2.
\]

There is consequently no suppressed width factor or rescaled time in
the reduction.

## 5. Strict positivity and the positive loss bound

Initially

\[
\dot v(0)=\alpha h_1(0)+\beta h_2(0)>0,
\]

so all three coordinates are positive for sufficiently small positive
time. On the respective coordinate faces in the nonnegative octant,

\[
\begin{aligned}
\dot v|_{v=0}&=\alpha h_1+\beta h_2\geq0,\\
\dot q|_{q=0}&=v(\alpha\tanh(ps_1)+\beta\tanh(ps_2))\geq0,\\
\dot p|_{p=0}&=vq(\alpha s_1+\beta s_2)\geq0.
\end{aligned}
\]

To justify strict, rather than merely weak, preservation of positivity,
suppose there is a first finite boundary time after a positive starting
time. The preceding trajectory and all its coordinate-face projections
fit in a compact nonnegative box, by finite-time existence and continuity.
The smooth reduced vector field is Lipschitz there, with some constant
\(C\). For each coordinate \(z\), comparison with its face value gives
\(\dot z\geq-Cz\) until the proposed first boundary time. Hence
\(z(t)\geq z(t_0)e^{-C(t-t_0)}>0\), a contradiction. The boundary
argument is valid even though the vector field may have no global
Lipschitz constant.

It follows that \(p,q,v>0\) for every \(t>0\), and strict monotonicity
of tanh gives

\[
0<f_1=vh_1<f_2=vh_2.
\]

But \(\alpha>\beta\). The identity

\[
\mathcal L
=\frac14\left[
(f_1+f_2-\alpha-\beta)^2+
(f_1-f_2-\alpha+\beta)^2
\right]
\]

therefore yields

\[
\mathcal L(t)\geq\frac{(\alpha-\beta)^2}{4}>0.
\]

For positive times the inequality is strict, since
\(f_1-f_2-\alpha+\beta<-(\alpha-\beta)\). A strict bound for every
finite time need not remain strict in the limit, so the candidate
correctly claims only
\(\mathcal L_\infty\geq(\alpha-\beta)^2/4\).

## 6. No positive stationary point and no finite cluster point

At a hypothetical stationary point with \(p,q,v>0\), the readout
equation gives

\[
v=\frac{\alpha h_1+\beta h_2}{h_1^2+h_2^2},\qquad
(r_1,r_2)=c(-h_2,h_1),
\quad
c=\frac{\alpha h_2-\beta h_1}{h_1^2+h_2^2}>0.
\]

The last positivity follows from \(h_2>h_1>0\) and
\(\alpha>\beta>0\), and the residual formula follows by substituting
the displayed value of \(v\).

At fixed \(p\), \(\partial_q h_k=u_k(1-h_k^2)\). Thus

\[
\sum_k r_k\partial_qh_k
=c h_1h_2
\left(\frac{\partial_qh_2}{h_2}
      -\frac{\partial_qh_1}{h_1}\right).
\]

For fixed \(q>0\),

\[
\frac{\partial_q\tanh(qu)}{\tanh(qu)}
=\frac{2u}{\sinh(2qu)}
\]

has derivative

\[
\frac{2[\sinh z-z\cosh z]}{\sinh^2 z}<0,
\qquad z=2qu>0.
\]

The sign is verified by differentiating
\(z\cosh z-\sinh z\): its derivative is \(z\sinh z>0\), and its
value at zero is zero. Because \(u_2>u_1>0\), the preceding sum is
negative. Consequently \(\dot q=-v\sum_k r_k\partial_qh_k>0\),
contradicting stationarity. No positive reduced stationary point exists.

For boundary accumulation, initially only the readout velocity is
nonzero, and the exact reduced metric gives

\[
\mathcal L(0)=\frac{\alpha^2+\beta^2}{2},\qquad
\dot{\mathcal L}(0)
=-[\alpha h_1(0)+\beta h_2(0)]^2<0.
\]

Therefore \(\mathcal L_\infty<\mathcal L(0)\). At any finite
nonnegative boundary point at least one of \(p,q,v\) is zero, so
both predictions are zero and the loss equals \(\mathcal L(0)\).
Continuity rules out accumulation at such a point.

The family of full parameter vectors indexed by \((p,q,v)\) is the
image of an injective linear map, hence is closed; its inverse on the
image is continuous, for example by extracting \(A_{1,1}\),
\(nW_{11}\), and \(w_1\). A finite full accumulation point therefore
corresponds to a finite nonnegative scalar accumulation point. If that
point were positive, the finite-cluster lemma would make the full
gradient zero and hence all three reduced velocities zero, contrary
to the previous paragraph. Boundary points have already been excluded.

There is thus no finite accumulation point. If
\(p(t)^2+q(t)^2+v(t)^2\) did not tend to infinity, some sequence of
times tending to infinity would have bounded scalar vectors.
Finite-dimensional compactness would give a finite convergent
subsequence, contradicting the conclusion just established. This
proves the stronger escape assertion

\[
p(t)^2+q(t)^2+v(t)^2\longrightarrow\infty,
\qquad
\mathcal L_\infty\geq\frac{(\alpha-\beta)^2}{4}>0.
\]

Because the induced metric is exactly Euclidean in the scalar
coordinates, the full parameter norm in that metric also tends to
infinity. No claim about which individual coordinate diverges is needed.

## 7. Both hidden layers train, and the probability scope is correct

Let \(c_v=\alpha h_1(0)+\beta h_2(0)>0\). At initialization
\(\dot p=\dot q=0\) and \(\dot v=c_v\). Differentiating the reduced
equations once more, all terms multiplied by \(v(0)=0\) drop out,
leaving

\[
\begin{aligned}
\ddot q(0)
&=c_v[\alpha u_1(0)(1-h_1(0)^2)
      +\beta u_2(0)(1-h_2(0)^2)]>0,\\
\ddot p(0)
&=c_vq(0)[
\alpha s_1(1-u_1(0)^2)(1-h_1(0)^2)
+\beta s_2(1-u_2(0)^2)(1-h_2(0)^2)]>0.
\end{aligned}
\]

Thus both hidden layers move for sufficiently small positive time.
The example is a trajectory of the fully trained two-hidden-layer
flow, even though it stays in a specially constrained invariant family.

Both feature matrices initially have equal nonzero rows, and hence rank
one. The initialization also imposes exact row equalities and zero
second coordinates in \(A\), and exact equality of all entries of \(W\).
It lies in a proper linear subspace of the hidden-parameter space, so
it has probability zero under any absolutely continuous joint law,
including a nondegenerate Gaussian law. The candidate correctly avoids
claiming positive Gaussian failure probability or failure from
initially full-rank features.

The example disproves a universal assertion that all zero-readout
initializations not located at bad stable equilibria must fit: this
trajectory leaves initialization, never has a finite equilibrium
accumulation point, and does not fit. It does not resolve a restricted
almost-sure statement, an initially full-rank statement, or an open-basin
robustness statement. None of those stronger claims is proved in the
candidate.

## Findings and limitations

- No mathematical correction is required for the assigned escape and
  finite-cluster arguments.
- Two cosmetic notation defects occur outside the main assigned argument:
  candidate lines 226 and 236 write \(sigma_{\min}\) rather than
  \(\sigma_{\min}\). The neighboring displayed formulas use the correct
  symbol, so this does not affect the mathematics.
- The present report contains no numerical validation and does not identify
  individual scalar asymptotics, the exact limiting loss, stability under
  symmetry-breaking perturbations, or a Gaussian failure probability.
- This internal cross-check uses an author context from the same study.
  It does not satisfy the workflow's independent isolated promotion-review
  requirements.
