# Internal reconstruction of the improved local cavity estimate

2026-10-03. Scoped internal check of Sections 3–5 of
POPULATION_DIRECT_COUPLING.md. This checker previously authored
POPULATION_NEGATIVE_SEARCH.md, but did not author the candidate or its
insertion dependencies. The check uses the completed same-study inputs
listed below; it is collaborative internal validation, not an isolated
promotion review.

**Verdict: PASS for the local finite insertion estimate and the random
cavity equations in their stated scope.** No mathematical error was found
in the frozen Sections 3–5. The training-prediction deletion error is
\(n^{-1}\exp\{C\sqrt{\log(e+n)}\}\), rather than the coordinate
scale \(n^{-1/2}\exp\{C\sqrt{\log(e+n)}\}\). The passage to all time
is valid for retained coordinates and predictions using physical tails.
The original linear variation and the unfrozen equations (19) are only
asserted through the logarithmic horizon. No quantitative identification
with the deterministic population is checked or supplied here.

## 1. Frozen input and precise scope

The author confirmed that Sections 3–5 were frozen before this check.
The whole-file hash is
145895536ea2e006ff444e2ca4eeb8b408ee1adf594dc317e9ea28a05936cb00.
The UTF-8 text starting at the heading for Section 3 and ending
immediately before the heading for Section 6 has hash
08b66b586665910fca69a0aac4dbd5b171beb34d1324f84c6890b3295852f3ed.
Both hashes were rechecked after the reconstruction and were unchanged.

Keep the canonical dense model, zero readout, independent Gaussian
initialization, fixed depth and finite compatible data, and sufficiently
small fixed labels from DEPTH_EXTENSION_RESULT.md. Activations are fixed
\(C^3\) functions with bounded first three derivatives; values can grow
linearly. Fixed quotient weights \(p_a>0\) sum to one. The residual is
\(r_a=f_a-y_a\), and \(\rho^2=\sum_a p_a r_a^2\).

For one omitted interior neuron \(i\) in layer \(j\), its incoming
initialized row and outgoing initialized column, written as column vectors,
are \(y_i,x_i\sim N(0,I_n/n)\). They are independent conditional on
all retained initialization. The retained layer is rectangular, with
normalizations still \(n\); setting its preactivation to zero would
be incorrect when \(\phi_j(0)\ne0\).

Use Euclidean mobility coordinates
\[
 \Theta=(W^{(1)},\sqrt nW^{(2)},\ldots,\sqrt nW^{(L)},w)
\]
on retained parameters, and \(\mathcal F_a=nf_a\).
The autonomous rectangular cavity is denoted by superscript \(0\).
Write
\[
 A_n=\exp\{C\sqrt{\log(e+n)}\},\qquad
 \epsilon_n=n^{-1/2}\exp\{C'\sqrt{\log(e+n)}\},\qquad
 T_n=C_T\log(e+n).
 \tag{1}
\]
Constants in these envelopes may be enlarged a fixed number of times;
each envelope remains \(n^{o(1)}\). Constants are independent of
width and time but may depend on the fixed data, depth, activation bounds
and label threshold.

The accepted existing inputs are the finite physical tube, fixed
exponential fitting, the completed full-network forward/backward maximum,
and the older coarse uniform deletion comparison. Their local proofs
and stop-transfer steps were reconstructed below from the complete
listed dependencies. This check does not rerun their entire independent
moment/probability review.

## 2. Conditional Gaussian kernels

Let \(K(t,s)\) be a cavity-measurable rectangular kernel, on
\(0\le s\le t\le T_n\), whose operator norm is at most \(A_n\),
whose number of rows is at most \(Cn^c\), and whose two time
Lipschitz constants are at most \(n^c A_n\). For each coordinate,
\[
 {\rm Var}((K(t,s)x_i)_u\mid\text{cavity})
                 =\|K(t,s)_{u,:}\|_2^2/n\le A_n^2/n.
 \tag{2}
\]
At \(u_n=C_D A_n\sqrt{\log(e+n)/n}\), a Gaussian tail is a
negative power of \(n\), with an exponent made arbitrarily large
by \(C_D\).

For a real square matrix \(R\), replace it by its symmetric part
in the quadratic form. If \(\lambda_k\) are its eigenvalues and
\(g_k\) are independent standard Gaussians, then
\[
 x_i^\top R x_i-\operatorname{tr}R/n
       =n^{-1}\sum_k\lambda_k(g_k^2-1).
 \tag{3}
\]
For \(|2t\lambda_k/n|\le1/2\), the exact Gaussian-square
moment-generating function and
\(-\log(1-u)-u\le C u^2\) give
\[
 \log\mathbb E e^{t(x_i^\top R x_i-\operatorname{tr}R/n)}
             \le C t^2\|R\|_{\rm HS}^2/n^2.
 \tag{4}
\]
Optimizing \(t\), using both signs, proves
\[
 \Pr\{|x_i^\top R x_i-\operatorname{tr}R/n|>u\}
 \le2\exp\!\left[-c\min\left\{
    \frac{n^2u^2}{\|R\|_{\rm HS}^2},
    \frac{nu}{\|R\|_{\rm op}}\right\}\right].
 \tag{5}
\]
The symmetric part has no larger relevant norm up to an absolute
constant, and \(\|R\|_{\rm HS}\le\sqrt n\|R\|_{\rm op}\).
For \(x_i^\top R y_i\), use the symmetric \(2n\)-dimensional
block matrix with off-diagonal blocks \(R/2,R^\top/2\); its trace
is zero and the same estimate follows. This verifies source (6)
without importing a named concentration theorem.

Choose a triangular grid of mesh \(n^{-c'}\) in \((t,s)\).
For fixed sufficiently large \(c'\), its size, the number of output
coordinates, and the number of kernels are polynomial in \(n\).
Choose \(C_D\) after those exponents. A union bound then has failure
at most \(n^{-D}\), for any prescribed fixed \(D\), after
enlarging constants. On the Gaussian norm event
\(\|x_i\|_2+\|y_i\|_2\le C\), interpolation errors are at most
\(Cn^{c-c'}A_n\). The same assertion applies to quadratic and
bilinear forms; normalized trace interpolation uses
\(|\operatorname{tr}(R-R')|/n\le\|R-R'\|_{\rm op}\).
The norm-event complement is exponentially small. Thus
\[
 \sup_{t,s}\|K(t,s)x_i\|_\infty\le\epsilon_n,\quad
 \sup_{t,s}\|K(t,s)x_i\|_2\le CA_n
 \tag{6}
\]
and the two quadratic/bilinear fluctuations are at most \(\epsilon_n\).

This event is independent of any later choice of insertion controls.
For every measurable scalar control \(|a(s)|\le M_n\), even one
chosen after observing \(x_i,y_i\),
\[
 \left\|\int_0^t K(t,s)x_i a(s)\,ds\right\|_\infty
          \le T_nM_n\sup_{t,s}\|K(t,s)x_i\|_\infty.
 \tag{7}
\]
The identical absolute-integral inequality handles centered forms.
No derivative of the control and no control net is required for this
improved event. Factors \(T_nM_n\) with polylogarithmic \(M_n\)
are absorbed in (1). The statement concerns the linear response
kernels, not linearity of the nonlinear forced trajectory.

## 3. Exact retained field and all first variations

Insert an external preactivation \(e_a\) at layer \(j+1\) and a
reverse source \(q_a\) at the derivative of the layer-\(j-1\)
features. Exact differentiation of the full network gives
\[
 \dot\Theta=-2\sum_a p_a r_a
 \left[\nabla_\Theta\mathcal F_a(\Theta,e)
       +D_\Theta h_a^{(j-1)}(\Theta)^\top q_a\right].
 \tag{8}
\]
Here \(r_a=\mathcal F_a(\Theta,e)/n-y_a\); an artificial
term \(q_a^\top h_a^{(j-1)}/n\) is not added to this residual.
The reverse term in (8) is precisely the chain-rule contribution
through the omitted neuron, absent when the external \(e_a\) is
held fixed.

The full sources are \(e_a=W^{(j+1)}_{:,i}h_{a,i}^{(j)}\) and
\(q_a=W^{(j)\top}_{i,:}\delta_{a,i}^{(j)}\).
Their leading parts are \(x_i a_a\) and \(y_i b_a\), with
\(a_a=h_{a,i}^{(j)}\), \(b_a=\delta_{a,i}^{(j)}\).
From the exact row/column update integrals and the proved coordinate
maxima, the learned row/column contributions to these sources have
Euclidean norm \(n^{-1/2}\operatorname{polylog}n\). These small
sources may be adaptive; their estimates are pathwise.

At the zero-source cavity put
\[
 d_a=\delta_a^{(j+1),0},\quad B_a=D_\Theta d_a,\quad
 C_a=D_\Theta h_a^{(j-1),0},\quad E_a=D_{e_a}d_a.
 \tag{9}
\]
Differentiating both the residual and the gradient in (8) gives
\[
 P_a=-\frac{2p_a}{n}\nabla\mathcal F_a d_a^\top,\qquad
 Q_a=-2p_a r_a^0 B_a^\top,\qquad
 T_a=-2p_a r_a^0 C_a^\top.
 \tag{10}
\]
The residual-free rank-one term \(P_a\) is necessary.
There is no direct derivative of the upper response \(d_a\)
with respect to \(q_a\).

The cavity variational generator is
\[
 DF_0=-\frac2n\sum_a p_a
           \nabla\mathcal F_a\nabla\mathcal F_a^\top
                  -2\sum_a p_a r_a^0D^2\mathcal F_a.
 \tag{11}
\]
The first term is negative semidefinite. The exact Hessian decomposition
in DEPTH_CAVITY_ROUTE.md has carrier diagonals between bounded forward
maps, plus mixed weight terms of bounded norm and rank \(O_L(n)\).
On the improved cavity maximum,
\[
 \|D^2\mathcal F_a\|_{\rm op}\le C(1+\sqrt{\log(e+n)}).
 \tag{12}
\]
Its residual coefficient has finite total variation. Differentiating
the norm of a variational solution therefore gives
\(\sup_{s\le t}\|J(t,s)\|_{\rm op}\le A_n\).
This avoids putting a physical-time factor in the exponent of \(A_n\).

The complete retained first variation is consequently
\[
 V(t)=\sum_a\int_0^t J(t,s)
       [(P_a+Q_a)x_i a_a(s)+T_a y_i b_a(s)]\,ds.
 \tag{13}
\]
The forward, backward and readout field variations are the corresponding
Jacobian images of \(V\), together with their direct \(e_a\) terms.
Forward Jacobians have bounded norm, backward derivatives have
polylogarithmic norm, and (12) bounds the propagator.
Time differentiation of these kernels uses at most \(\phi_\ell'''\):
the differentiated backward maps contain \(\phi_\ell''\), and one
physical-time derivative introduces \(\phi_\ell'''\).
Physical coordinate speeds are bounded by
\(\sqrt n\operatorname{polylog}n\). The identities
\(\partial_tJ=DF_0(t)J\), \(\partial_sJ=-JDF_0(s)\) bound the
remaining time derivatives. Thus these are kernels of Section 2.

The relevant lower adjoint probes are bounded linear transforms of
\(y_i\). Include them in the same conditional event. After integration,
all linear field variations have Euclidean norm \(A_n\) and
coordinate maximum \(\epsilon_n\). The actual controls have the
required polylogarithmic amplitudes on the final good event.

## 4. Nonlinear remainder and the reverse force

Let \(U=\Theta-\Theta^0-V\) and
\(u(t)=\sup_{s\le t}\|U(s)\|_2\). In a field expansion, separate
the Gaussian linear field \(v\) from its remainder \(u_0\).
The key products are
\[
 \|v^2\|_2\le\epsilon_n A_n,\qquad
 \|v\odot u_0\|_2\le\epsilon_n\|u_0\|_2,\qquad
 \|u_0^2\|_2\le\|u_0\|_2^2.
 \tag{14}
\]
Using only \(\|v\|_2\|u_0\|_2\) would incorrectly introduce
an unsuppressed \(A_nu\) coefficient. Forward induction and descending
backward induction use (14). Reference carriers add polylogarithmic
factors, and every changed-hidden-matrix product retains its explicit
\(1/\sqrt n\). In a gradient block
\(\delta h^\top/\sqrt n\), a single remainder is multiplied by
a reference RMS, while a product of two changes retains \(1/\sqrt n\).
These facts bound all forward/backward and gradient Taylor remainders.

The extra reverse force needs its own check. For a fixed sample define
\(\psi_y(\Theta)=y_i^\top h_a^{(j-1)}(\Theta)\).
Its reference lower adjoint probes have Euclidean norm \(O(1)\)
and coordinate maximum \(\epsilon_n\). Set \(N=A_n+u\).
Along the joining parameter segment, forward changes have Euclidean
size \(CN\), and changed hidden operators have norm at most
\(N/\sqrt n\). Subtract lower adjoint recursions using a changed
gate times the *reference* probe. This yields
\[
 \|\text{probe}_{\rm segment}-\text{probe}_0\|_2
               \le C(\epsilon_n N+N/\sqrt n).
 \tag{15}
\]
Previously estimated differences propagate through bounded operators;
no extra \(N\) factor is needed at each layer.

The Hessian of \(\psi_y\) has curvature diagonals weighted by these
segment probes. Its mixed weight terms carry \(1/\sqrt n\).
Therefore
\[
 \|D^2\psi_y\|_{\rm op}
          \le C\{\epsilon_n(1+N)+(1+N)/\sqrt n\}.
 \tag{16}
\]
Integrating this Hessian along the segment gives the candidate's
reverse-probe estimate
\[
 \|\nabla\psi_y(\Theta)-\nabla\psi_y(\Theta^0)\|_2
       \le C\{\epsilon_n(N+N^2)+(N+N^2)/\sqrt n\}.
 \tag{17}
\]
It is valid without delocalization of the changed probe. Multiplication
by the bounded scalar controls and the residual only adds the stated
polylogarithms and finite activity.

The scalar prediction Hessian, including the external \(e_a\)
coordinate, is bounded by \(A_n/n\). Segment carrier bounds follow
from the same forward/backward expansions: their differences from
the reference maximum are bounded by linear-coordinate terms and the
stopped remainder. Thus the scalar residual has second Taylor
remainder at most \(A_nN^2/n\). The reference gradient norm is
\(C\sqrt n\), so its contribution to the vector field is
\(A_nN^2/\sqrt n\). The product of first residual and gradient
variations has that scale as well. This explicitly accounts for
terms with no residual prefactor.

Residual-weighted terms integrate over finite activity; the remaining
terms integrate over \(T_n\), and (13) propagates them by \(A_n\).
After choosing one enlarged envelope, the resulting inequality is
\[
 u(t)\le A_n\{n^{-1/2}+n^{-1/2}u(t)+u(t)^2\}.
 \tag{18}
\]
At a first attainment of \(2A_n/\sqrt n\), the second term on the
right is \(2A_n^2/n\), and the third is \(4A_n^3/n\).
Each is \(o(A_n/\sqrt n)\), because \(A_n=n^{o(1)}\).
Continuity excludes that attainment, proving
\[
 \sup_{t\le T_n}\|\Theta-\Theta^0-V\|_2\le\epsilon_n.
 \tag{19}
\]
The same block expansions prove this bound for the nonlinear field
reconstruction remainders. Retained full/cavity fields therefore differ
coordinatewise by \(\epsilon_n\), though their Euclidean differences
can be \(A_n\). The argument needs no fourth activation derivative.

## 5. Probability logic and the pre-existing coarse comparison

The Gaussian kernels must not be conditioned on the full-network
good event. Here is a measurable implementation of the source's logic.

Let \(\Omega_n\) be the already established full-network good event.
On it the joint budget, tube and coordinate maximum hold with strict
fixed margins. The older insertion event is uniform over singleton
deletions and their old control class, with superpolynomial failure.
On its intersection with \(\Omega_n\), the coarse full/cavity
coordinate comparison applies until the first stop.
The joint cavity budget is bounded by \(e^{o(1)}B+O(1/n)<2B\),
so its stop cannot occur first. This is the common-prefix argument
in the complete bounded and unbounded sources. All singleton
cavities consequently survive through \(T_n\), and their retained
coordinates differ by \(o(1)\) from the full coordinates.
The improved full maximum therefore transfers to all singleton cavities.
Their initialized Gram margins and deterministic physical tubes were
already transferred uniformly by the initialization argument.

For deletion \(i\), let \(A_{n,i}\) now be the event that its *own*
autonomous cavity satisfies these bounds, with slightly larger fixed
constants. This event is measurable in retained roots only. The preceding
argument gives
\[
 \Pr\left(\bigcap_i A_{n,i}\right)\longrightarrow1.
 \tag{20}
\]
It does not obtain (20) by a union bound on \(o(1)\) individual
probabilities. The older simultaneous surgery event is what supplies
the conclusion.

Let \(E_{n,i}\) be the new Gaussian-kernel event, defined conditionally
on the retained roots. Its kernels can be set to zero when \(A_{n,i}\)
fails; on that set their value is immaterial. By Section 2,
\[
 \Pr(A_{n,i}\cap E_{n,i}^c)
   =\mathbb E\!\left[\mathbf1_{A_{n,i}}
             \Pr(E_{n,i}^c\mid\text{retained roots})\right]
   \le n^{-D}.
 \tag{21}
\]
There are at most \(Ln\) singletons. Hence the union of these
exceptions has probability at most \(Ln^{1-D}\).
Intersect with \(\Omega_n\) afterward to supply the actual control
amplitudes. No rate for \(\Pr(\Omega_n^c)\) is needed, and no
unconditional expectation estimate for the actual flow is inferred.
Taking fixed \(D>3\) verifies the source's probability claim.

## 6. Reconstruction of the two scalar cavity equations

At the cavity define
\[
 Q^h_{ab}(t,s)=h_a^{(j-1),0}(t)^\top h_b^{(j-1),0}(s)/n,\quad
 Q^\delta_{ab}(t,s)=d_a(t)^\top d_b(s)/n,
\]
\[
 R^h_{ab}(t,s)=\operatorname{tr}[C_a(t)J(t,s)C_b(s)^\top]/n,\quad
 R^\delta_{ab}(t,s)=\operatorname{tr}[B_a(t)J(t,s)B_b(s)^\top]/n,
 \quad e_a(t)=\operatorname{tr}E_a(t)/n.
 \tag{22}
\]
The last \(e_a(t)\) is the source's scalar trace coefficient, not
the external preactivation vector from (8). The distinct uses have
been kept in separate passages; a renamed trace coefficient would
improve typography but is not a mathematical error.

Conditional on retained roots,
\[
 \xi_{a,i}(t)=y_i^\top h_a^{(j-1),0}(t),\qquad
 \zeta_{a,i}(t)=x_i^\top d_a(t)
 \tag{23}
\]
are independent centered Gaussian groups. Their within-group
covariances are respectively \(Q^h,Q^\delta\).

The exact learned incoming-row integral, paired with the current lower
feature, contributes
\(-2\sum_b p_b\int r_b\,Q^{h,\mathrm{full}}_{ab}\,
\delta_{b,i}^{(j)}\,ds\).
For the initialized row pairing,
\[
 y_i^\top[h_a^{(j-1)}-h_a^{(j-1),0}]
                         =y_i^\top C_aV+O(\epsilon_n).
 \tag{24}
\]
The \(T_b y_i\) part of \(V\) gives the quadratic form with
mean \(-2p_b r_b^0 R^h_{ab}\); its \(x_i\) parts are centered
bilinear forms. The uniform kernel event permits the actual adaptive
control \(\delta_{b,i}^{(j)}\) to be inserted.

Similarly, the learned outgoing column paired with the upper response
contributes
\(-2\sum_b p_b\int r_b\,Q^{\delta,\mathrm{full}}_{ab}\,
h_{b,i}^{(j)}\,ds\).
Its initialized-column counterpart is
\[
 x_i^\top[\delta_a^{(j+1)}-d_a]
   =x_i^\top B_aV+x_i^\top E_a x_i\,h_{a,i}^{(j)}
                                      +O(\epsilon_n).
 \tag{25}
\]
The \(Q_bx_i\) term gives the mean
\(-2p_b r_b^0R^\delta_{ab}\), the \(T_by_i\) term is centered
bilinear, and the direct derivative gives
\(e_a h_{a,i}^{(j)}\). The \(P_b\) term was retained in \(V\);
only now its normalized trace can be discarded:
\[
 \frac1n|\operatorname{tr}[B_aJ P_b]|
                    \le A_n/n,
 \tag{26}
\]
because \(P_b\) has rank one. Its centered form is still covered by
the Gaussian event. This checks the location of the rank-one
simplification.

Full/cavity feature and response Euclidean differences are at most
\(A_n\), while their reference norms are \(C\sqrt n\).
Their normalized pairings therefore differ by \(A_n/\sqrt n\).
The coarse scalar residual difference has the same sufficient scale;
the sharper prediction estimate below is not needed for this step.
Multiplication by the coordinate controls, integration of residual terms
over finite activity, and integration of residual differences over
\(T_n\) preserve the envelope \(\epsilon_n\).

Combining these identities gives exactly, uniformly for \(t\le T_n\),
\[
 \begin{aligned}
 z_{a,i}^{(j)}(t)
 &=\xi_{a,i}(t)-2\sum_b p_b\int_0^t r_b^0(s)
       [Q^h_{ab}(t,s)+R^h_{ab}(t,s)]
                         \delta_{b,i}^{(j)}(s)\,ds+O(\epsilon_n),\\
 k_{a,i}^{(j)}(t)
 &=\zeta_{a,i}(t)+e_a(t)h_{a,i}^{(j)}(t)
       -2\sum_b p_b\int_0^t r_b^0(s)
       [Q^\delta_{ab}(t,s)+R^\delta_{ab}(t,s)]
                         h_{b,i}^{(j)}(s)\,ds+O(\epsilon_n).
 \end{aligned}
 \tag{27}
\]
The ordering of the two time/sample roles is correct; the response
traces have not been symmetrized. These are random cavity equations.
Their coefficients have not been compared quantitatively with a
deterministic population.

## 7. Training predictions, boundary layers and all time

For an interior deletion, expand the scalar prediction directly:
\[
 f_a-f_a^0
   =\frac1n\nabla\mathcal F_a^\top V
       +\frac1n d_a^\top x_i a_a
       +\frac1n\nabla\mathcal F_a^\top U
       +O(A_n/n).
 \tag{28}
\]
The final remainder includes the scalar second Taylor remainder and
the small learned source corrections.
Since \(\|\nabla\mathcal F_a\|_2\le C\sqrt n\), the row kernel
\(n^{-1}\nabla\mathcal F_a^\top J(P_b+Q_b)\), and the analogous
\(T_b\) kernel, has norm at most \(A_n/\sqrt n\). Its pairing
with \(N(0,I_n/n)\) therefore has standard deviation \(A_n/n\).
The direct row \(d_a^\top/n\) has this scale as well.
Apply the same polynomial-grid argument and absolute-control
integration as before. Their total is \(A_n/n\).
The \(U\) term has size \(C\|U\|_2/\sqrt n=A_n/n\) by (19).
This proves
\[
 \max_a\sup_{t\le T_n}|f_a(t)-f_a^0(t)|
       \le n^{-1}\exp\{C\sqrt{\log(e+n)}\}.
 \tag{29}
\]
The extra inverse square root is a prediction contraction; it is
not an improvement of the retained Euclidean state norm.

For a first-layer deletion there is no reverse source. The omitted
first row is an independent fixed-dimensional Gaussian root entering
only the scalar control, so the uniform-control event still applies.
For a top-layer deletion there is no outgoing initialized Gaussian
column. The omitted prediction
\(d_a^{\rm omit}=w_i h_{a,i}^{(L)}/n\) contributes the exact
retained field
\[
 -2\sum_a p_a(r_a^0+d_a^{\rm omit})
       [\nabla\mathcal F_a^{\rm ret}
                  +D_\Theta h_a^{(L-1)\top}q_a].
 \tag{30}
\]
It multiplies both the gradient and reverse force. Its Euclidean
forcing is \(n^{-1/2}\operatorname{polylog}n\), while its direct
prediction contribution is \(n^{-1}\operatorname{polylog}n\).
Thus both (19) and (29) survive. No fictitious outgoing Gaussian
column is introduced at this layer.

For all-time retained-coordinate comparison, use each path's crude
physical tail. Parameter Euclidean displacement after \(T_n\) is
at most \(C\sqrt n e^{-\kappa T_n}\); forward coordinate
displacement is no larger at this scale, and the crude backward
coordinate displacement is at most \(Cn e^{-\kappa T_n}\).
If \(C_T\kappa>3\), both are smaller than \(\epsilon_n\).
Consequently the retained-coordinate consequence of (19) extends to
all physical time.

There is an even simpler extension of (29) for training predictions:
both full and cavity paths fit the same labels, and
\[
 |f_a(t)-f_a^0(t)|
 \le |r_a(t)|+|r_a^0(t)|
 \le 2Yp_a^{-1/2}e^{-\kappa t}.
 \tag{31}
\]
For \(t\ge T_n\) this is smaller than (29).
Thus training-prediction deletion has the same all-time rate.
The candidate only claims its local calculation on the logarithmic
horizon; (31) is an immediate permitted strengthening for training
predictions.

Neither argument integrates the residual-free \(P_a\) over an
infinite interval. The original \(V(t)\) and (27) are checked only
through \(T_n\). One could freeze a comparison object there for an
all-time approximation, but that would have to be stated explicitly.

## 8. Source changes, coverage and commands

**Source changes are recorded separately from the scientific verdict.**
The preliminary whole-file read had hash
a380fa0d4f042fd2c805e23763ed5536c5f353b343d03fa325d46706ed5abd40.
Before the freeze, the author corrected the form-feed character in
source equation (6), added collaborative provenance, and changed later
material outside Sections 3–5. The author identified those changes;
the preliminary read was not used as the frozen certification version.
The frozen version has zero form-feed bytes. No later source change
occurred during this check. This checker did not edit the candidate.

The following dependencies were read completely, including the
nonlinear block calculations, time modulus, coarse Gaussian event,
stopping comparison and linear-growth extension. The complete
UNBOUNDED_INSERTION_CHECK.md was additionally read because it supplies
the explicitly cited block and top-layer calculations.

| Source | SHA-256 |
|---|---|
| POPULATION_DIRECT_COUPLING.md | 145895536ea2e006ff444e2ca4eeb8b408ee1adf594dc317e9ea28a05936cb00 |
| Sections 3–5 text | 08b66b586665910fca69a0aac4dbd5b171beb34d1324f84c6890b3295852f3ed |
| DEPTH_CAVITY_ROUTE.md | e8f9f43c137a9c74b751cbd2e54cf5a2b13f090c560d912b4b17994c53bc1478 |
| DEPTH_INSERTION_CHECK.md | 77c51e725629e736a33c16dbe4ec179b5aa859b527539815f55422a818a1e977 |
| DEPTH_RESPONSE_MODULUS.md | e32e3608e5a02d6f9aefb88cf77890f9110a8d65bede6faedf2f215d84dc6d24 |
| UNBOUNDED_ACTIVATION_CANDIDATE.md | e939e971d7a9e1b884b42d73d3ce65f5b1f548d9e25ab9cfe76c0502aa591713 |
| UNBOUNDED_INSERTION_CHECK.md | bec5707fccc99597570ce51c94d3a487fd0b1ede14578617275cb708fdd95578 |

The already-read DEPTH_EXTENSION_RESULT.md and
GENERAL_SELF_AVERAGING.md provide the theorem scope and completed
finite good event, at the hashes recorded in POPULATION_NEGATIVE_SEARCH.md.
The canonical manuscript equations and required mathematical/process
skills remain as previously read. No other study, archive, external
source or numerical experiment was used.

The frozen file and its Section 3–5 extract were copied to
data/generated/dense_cutoff_population_rate_20261001/population_direct_check_20261003/
for comparison. SHA-256 was computed with Python hashlib and with
sha256sum for the dependencies. Byte scanning confirmed zero form-feed
characters in the frozen candidate. The check itself consisted of the
explicit algebraic and probabilistic reconstructions in Sections 2–7.
No test run, GPU probe, trajectory simulation, Git staging or commit
was performed.

This report accepts only the local conclusions stated at the beginning.
It does not validate Sections 6 onward of the candidate, prove
concentration of the random response traces around population values,
or establish a dense-to-population width rate.
