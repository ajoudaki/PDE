# Fixed-depth cavity probability and all-time check

2026-10-03. Internal collaborative validation, not an independent
promotion review. The complete 751-line source was read and reconstructed.
No experiments, manuscript changes, other-study reads, or Git operations.

Checked source: DEPTH_CAVITY_ROUTE.md, SHA256
e8f9f43c137a9c74b751cbd2e54cf5a2b13f090c560d912b4b17994c53bc1478.
Additional scientific inputs are the current canonical manuscript and
the same-study checked response-modulus, finite mixed-moment, and
deterministic depth-tracking arguments.

**Verdict.** Sections 7–8 correctly convert the local insertion estimates
into an unconditional all-time finite-width carrier bound. Section 9's
same-width near-quarter memory conclusion follows from the already checked
DEPTH_TRACKING_ROUTE.md. This report's probability conclusion is conditional
on the local estimates (24) and (28), whose separate complete reconstruction
is assigned to the coordinating author. The report checks their use and
all subsequent probability steps; it does not replace that local review.

The final repaired source was checked at every amended mathematical passage:
its explicit initialization event, rectangular/zero-activation deletion,
Section 9's stronger deterministic source bound, and fixed positive sample
weights. The earlier undefined-event, dependency-attribution, and stripped
inline-delimiter issues are resolved. The fixed-weight extension is valid:
the symmetric residual Gram is \(D_pH_L^\top H_LD_p/n\), where
\(D_p=\operatorname{diag}(\sqrt{p_a})\); replacing sample averages
by \(\sum_a p_a\) preserves every activity and moment estimate.
The coordinator has separately reconstructed the bounded local lemma with
PASS; this report supplies the complete probability part of that modular
internal validation.

## 1. Model, events, and hypotheses used

There are \(m\) fixed data points, a fixed depth \(L\ge2\), and \(n\)
neurons per layer. The canonical network has
\[
 z_a^1=W^1v_a,\qquad z_a^\ell=W^\ell h_a^{\ell-1},\qquad
 h_a^\ell=\phi_\ell(z_a^\ell),\qquad f_a=w^\top h_a^L/n.
\]
The loss is \(m^{-1}\sum_a(f_a-y_a)^2\), with mobilities
\((n,1,\ldots,1,n)\). First-layer entries are independent standard
Gaussians, hidden entries are independent \(N(0,1/n)\), and \(w(0)=0\).
All initialized blocks are independent. Each activation and its first
three derivatives are bounded, and each activation is \(C^3\).

Set \(r_a=f_a-y_a\), \(\rho^2=m^{-1}\sum_a r_a^2\),
\(Y^2=m^{-1}\sum_a y_a^2\), and \(S=2Y/\kappa\).
The zero-label case is stationary; take fixed \(S>0\) below.
The backward quantities are
\[
 k_a^L=w,\qquad \delta_a^\ell=\phi_\ell'(z_a^\ell)\odot k_a^\ell,
 \qquad k_a^\ell=W^{\ell+1\top}\delta_a^{\ell+1}.
\]
The positive limiting initial readout-feature Gram gap and sufficiently
small labels supply an all-time physical tube with
\[
 \rho(t)\le Y e^{-\kappa t},\quad
 \|W^\ell(t)\|_{\rm op}\le C,\quad
 \|w(t)\|_\infty\le CS,\quad
 \|k_a^\ell(t)\|_2/\sqrt n\le CS .
\]
The first-layer normalized matrix bound and corresponding forward
physical speeds are also part of this tube.

Take \(\mathcal G_n\) to be the full initialization event with strict
operator, first-layer, and Gram margins sufficient for this tube and its
fixed-size rectangular cavities. Then
\(\mathbb P(\mathcal G_n)\to1\). It is independent of the later moment
degree. A fixed deletion count may affect the width from which the margins
are inherited, but not the chosen gap, label threshold, or event.

Only layers \(j<L\) enter the empirical budget:
\[
 \mathcal H_\eta(t)
 =\frac1n\sum_{j<L}\sum_i
       \exp\left\{\frac{\eta}{S}
             \max_a\sup_{u\le t}|k_{a,i}^j(u)|\right\}.
\]
At initialization it equals \(L-1\) exactly. Choose \(B>L\), stop it at
\(B\), and cap time at \(T_n=c_T\log(e+n)\); denote this stop by
\(\sigma\). Each cavity has its own stop at budget \(2B\).
These are analysis stops only. The actual dense and closure algorithms
remain unchanged.

The omitted top carrier \(w\) is deterministically bounded by \(CS\).
Whenever a modulus or Schatten estimate includes its exponential
moment, that term is bounded by a fixed constant and can be absorbed.
No top-layer stochastic carrier budget is needed.

The local input used below is the source's uniform insertion result:
for each fixed same-layer deletion set \(I\),
\[
 \max_{\text{retained }a,\ell,i,t}
       |k_{a,i}^\ell(t)-k_{a,i}^{\ell,-I}(t)|
 \le \epsilon_{n,|I|},\qquad
 \epsilon_{n,r}=C_r n^{-1/30},
\]
on the common full/cavity stopped prefix, with superpolynomial failure.
Its upper-response Euclidean discrepancy is at most \(C_r n^{1/100}\).
For a singleton \(i\) in layer \(j<L\), with deleted initialized outgoing
column \(x_i\sim N(0,I/n)\), its stronger scalar conclusion is
\[
 \sup_{a,t\le\min(\sigma,\sigma_{-i})}
 |k_{a,i}^j(t)-x_i^\top\delta_a^{j+1,-i}(t)|
 \le R(B,S)+o(1),\qquad
 R(B,S)=CS(1+S^2B).
 \tag{A}
\]
The constant in (A) is a singleton constant, independent of the moment
degree. This distinction is essential.

## 2. Preliminary audit of the local/probability interface

The source deletes only neurons in one fixed layer, retaining rectangular
matrices and the original normalization \(n\). It does not replace a
deleted activation by \(\phi(0)\); this matters for nonzero \(\phi(0)\).
Incoming Gaussian rows and outgoing Gaussian columns are disjoint
initialized blocks. Conditional on the retained initialization, their
pairs are independent across the deleted neurons.

The retained equation includes the reverse force
\[
 -\frac2m\sum_a r_a
       D_\Theta h_a^{j-1}{}^\top
       \sum_{i\in I} y_i\delta_{a,i}^j .
\]
Its residual remains the original forward residual. Hence the local
statement, if proved, applies to the actual adaptive dense flow.

The numerical net exponents are compatible:
\[
 a=0.01,\quad b=0.1,\quad
 \|J\|_{\rm op}\le n^{0.001},\quad
 \|{\rm linear\ response\ operator}\|\le n^{0.005}.
\]
Coordinate Gaussian tails at \(n^{-0.1}\) have exponent \(n^{0.79}\).
The Lipschitz control net at precision \(n^{-1/8}\) has log cardinality
at most \(C_r n^{0.625}(\log n)^{C_L}\). Interpolation error is at most
\(n^{-0.12}\) times fixed constants, smaller than the coordinate
threshold. A union over \(n^r\) sets preserves superpolynomial failure.
The stated nonlinear bootstrap uses \(2a-b=-0.08\) and remainder
radius \(n^{-0.04}\), leaving a strict exponent margin even after
variational amplification. These arithmetic checks do not substitute
for the coordinator's reconstruction of the nonlinear expansions.

The trace formulas also have the correct factor count: \(h\) residual
Hessian insertions between two response endpoints require Schatten
exponent \(h+2\). The term containing the budget starts at \(S^4B\)
before its exterior residual integral, and at \(S^5B\) afterward.
The looser bound \(CS(1+S^2B)\) in (A) is valid for small \(S\).
The direct external derivative contributes \(CS\) by the carrier RMS
bound, and the adaptive rank-one term has a vanishing normalized trace.
This matches the separately checked endpoint modulus/trace source.

## 3. Activity modulus and conditional Gaussian moments

For a stopped cavity use residual activity
\[
 \mu([s,t])=\frac2m\sum_a\int_s^t|r_a(u)|\,du,\qquad
 v=\mu([s,t])/S.
\]
Its total normalized range is bounded by a fixed constant.
For \(0\le v\le1\), physical speeds give
\[
 \|\Delta w\|_2/\sqrt n\le CSv,\quad
 \|\Delta W^\ell\|_{\mathrm{physical}}\le CS^2v,\quad
 \|\Delta z_a^\ell\|_2/\sqrt n\le CS^2v.
\]
At a changed backward gate, split its reference carrier at \(SR\).
The small part contributes \(CS^3Rv\). The exponential budget bounds
the large part in normalized Euclidean norm by
\(CS\sqrt{2B}e^{-c_\eta R}\).
Other backward changes propagate by bounded operators or cost \(CS^3v\).

Choose
\[
 R=C_\eta[1+\log(e+B)+\log(1/v)].
\]
The tail is at most \(CSv\), and descending through fixed depth gives
\[
 \frac{\|\delta_a^\ell(t)-\delta_a^\ell(s)\|_2}{S\sqrt n}
 \le Cv[1+S^2\log(e+B)+S^2\log(1/v)].
 \tag{B}
\]
If \(S^2\log(e+B)\le1\), then
\(v\log(1/v)\le C\sqrt v\) makes the last expression at most
\(C\sqrt v\), with \(C\) independent of \(B\) and small \(S\).
At \(v=0\) the parameter path is unchanged and the difference is zero.

Freeze every reference at its own stop. If its own initialization
conditions fail, define its entire reference coefficient path to be zero.
All these choices are measurable in retained initialization alone.
For each omitted outgoing Gaussian \(x_i\), conditional on the cavity,
\[
 Z_i^{-I}=\max_a\sup_{t\le T_n}
             |x_i^\top\delta_a^{j+1,-I}(t)|/S
\]
therefore has bounded diameter and covering numbers
\(N(\epsilon)\le C\epsilon^{-2}\). The path starts at zero, because
the readout starts at zero. At dyadic level \(k\) there are at most
\(C2^{2k}\) increments of standard deviation at most \(C2^{-k}\).
Gaussian tails and a union bound bound their maximum by
\(C2^{-k}(\sqrt{k+1}+z)\), with failure at most \(Ce^{-cz^2}\)
after a suitable summable allocation over levels.
Summing the increments proves
\[
 \mathbb P(Z_i^{-I}>C(1+z)\mid\mathrm{cavity})
 \le Ce^{-cz^2},\qquad
 \mathbb E(e^{\lambda Z_i^{-I}}\mid\mathrm{cavity})
 \le\mathcal L(\lambda)<\infty
 \tag{C}
\]
for every fixed \(\lambda\ge0\).
The constants are independent of width, fixed deletion count, physical
horizon, and \(B\), after the displayed smallness choice.
Thus one may choose \(B\) using \(\mathcal L\), and choose \(S\)
subsequently. This is stronger than a merely subpower dependence on \(B\).

Conditional on the common cavity, the variables \(Z_i^{-I}\) for its
distinct deleted indices are independent, since only their independent
outgoing roots vary. Incoming roots are unnecessary in this Gaussian
reference; their effects already occur in the singleton insertion shift.

## 4. Cavity initialization and survival

Uniform cavity initialization requires no union bound on an individual
Gram law of large numbers. On \(\mathcal G_n\), deleting \(r\) bounded
activations changes the next preactivation vector in Euclidean norm by
at most \(C\sqrt r\), using the full initialized matrix operator bound.
Propagation through fixed-depth bounded operators and Lipschitz
activations preserves this order. The normalized top feature discrepancy
is at most \(C\sqrt{r/n}\); hence the finite data Gram discrepancy tends
to zero, uniformly over every set of that fixed size.
Matrix operator bounds and the required first-layer bounds do not increase
under rectangular deletion. The initial budget is still \(L-1\), up to
the optional \(r/n\) contribution from zero-filled missing carriers.
A fixed strict full margin therefore initializes all fixed-size cavities.

On the uniform local event, compare full and cavity only up to the
earlier stop. Running coordinate maxima differ by
\(\epsilon_{n,r}\), so
\[
 \mathcal H_\eta^{-I}(t)
 \le e^{\eta\epsilon_{n,r}/S}\mathcal H_\eta(t)+O(r/n)
 \le B+o(1)<2B.
\]
A cavity cannot attain its stop first. Its physical fitting tube holds
independently for all time. Thus all references agree with their genuine
cavity trajectories throughout the full stopped interval.
No independence is inferred by conditioning on the full stop.

## 5. Common-cavity comparison on entire independent paths

Fix \(I\ni i\), \(|I|=r\). Full-to-singleton and full-to-\(I\)
comparisons give on the full stopped prefix
\[
 \sup_{a,t\le\sigma}
 \|\delta_a^{j+1,-i}(t)-\delta_a^{j+1,-I}(t)\|_2
 \le C_r n^{1/100}.
\]
This event and interval may depend on \(x_i\). The complete frozen
difference path itself does not, because both cavities omit \(x_i\).
Radially project that complete path onto the deterministic Euclidean
ball of radius \(C_r n^{1/100}\). Projection preserves root independence
and is nonexpansive. It agrees with the actual difference on the successful
full prefix. Different activity clocks are handled by their sum.

The projected Gaussian pairing has radius
\[
 D_n=C_r n^{-1/2+1/100}
\]
and entropy bounded using (B) by \(C(S/\epsilon)^2\).
The dyadic entropy sum starting at radius \(D_n\) bounds its mean by
\(CD_n\sqrt{\log(e+S/D_n)}=o(1)\).
Gaussian concentration at threshold \(n^{-1/10}\) has exponent of
order \(n^{0.78}\), up to constants. Thus
\[
 \sup_{a,t\le\sigma}
 |x_i^\top(\delta_a^{j+1,-i}(t)-\delta_a^{j+1,-I}(t))|
 \le n^{-1/10}
 \tag{D}
\]
simultaneously over all fixed-size sets, outside a superpolynomially
small event. Conditioning never uses the full-network good event.
The possibly growing Euclidean projection radius is correct: its
normalized Gaussian radius \(D_n\) tends to zero.

## 6. Mixed moments, collisions, and removal of the full stop

Define
\[
 H_{n,j}={\bf1}_{\mathcal G_n}\frac1n\sum_i
       e^{\eta\max_a\sup_{t\le\sigma}|k_{a,i}^j(t)|/S}.
\]
Fix an integer \(p\ge1\), independently of \(n\).
Expand \(H_{n,j}^p\). For a distinct \(p\)-tuple, use its common
same-layer cavity. Combining the singleton estimate (A) with (D) gives
the pathwise product upper bound by its \(p\) common Gaussian factors
times \(e^{p\eta R(B,S)/S+o(1)}\).

Only after this pathwise upper bound is obtained should its full-event
indicator be removed. The Gaussian reference on the right satisfies
(C) for every retained configuration, including failed initialization
under the zero-path convention. Conditional independence then bounds the
expected product by
\[
 [\mathcal L(\eta)e^{\eta R(B,S)/S}]^p+o(1).
\]
The constant multiplying the trace shift remains the singleton constant.
Replacing it with a shift growing in \(p\) would invalidate the closure.

A collision tuple has \(r<p\) distinct indices and multiplicities
\(d_1+\cdots+d_r=p\). The same reasoning uses the finite constants
\(\mathcal L(d_\ell\eta)\). Its constants may depend on \(p\).
There are \(O_p(n^{p-1})\) collision tuples, so after the normalization
\(n^{-p}\) their total contribution vanishes.
The common local exceptional event is also negligible: on a successful
full start the stopped total budget is at most \(B\), so its contribution
to the \(p\)-th moment is at most \(B^p\) times its failure probability.
It follows that
\[
 \limsup_{n\to\infty}\mathbb E H_{n,j}^p
 \le D(B,S)^p,\qquad
 D(B,S)=\mathcal L(\eta)e^{C\eta(1+S^2B)}.
 \tag{E}
\]
The base is independent of \(p\). The width needed for (E) may depend
on \(p\), as permitted.

Minkowski's inequality and the finite number of layers give
\[
 \limsup_n\mathbb E\left(\sum_{j<L}H_{n,j}\right)^p
 \le[(L-1)D(B,S)]^p.
\]
Choose \(B\) first, larger than
\(4(L-1)\mathcal L(\eta)e^{C\eta}\) and \(L\).
Then choose \(S>0\) small enough for all preceding local and modulus
conditions and \(e^{C\eta S^2B}\le2\).
These choices are independent of \(p\), width, and confidence.
On \(\mathcal G_n\), a full budget hit by \(T_n\) implies
\(\sum_{j<L}H_{n,j}=B\). Therefore, for every fixed \(p\),
\[
 \limsup_n\mathbb P(\mathcal G_n,\ \text{budget hit by }T_n)
 \le\left(\frac{(L-1)D(B,S)}B\right)^p.
\]
The ratio is strictly below one. Letting \(p\to\infty\) after taking
the width limit proves that the budget-hit probability tends to zero.
Adding \(\mathbb P(\mathcal G_n^c)=o(1)\) gives the unconditional
statement. There is no growing-deletion theorem hidden in this order
of limits and no independence between layers is needed.

## 7. Maximum, all-time tail, and deterministic closure consequence

Once the full stop is removed through \(T_n\), use the singleton form
of (A) and the conditional Gaussian tail (C).
A union over \(n(L-1)\) neurons gives, for a sufficiently large fixed
constant,
\[
 \max_{a,j,i}\sup_{t\le T_n}|k_{a,i}^j(t)|
 \le CS\sqrt{\log(e+n)}
\]
with probability tending to one. The fixed trace shift is absorbed,
and the top carrier already satisfies \(\|w\|_\infty\le CS\).

For the tail after \(T_n\), the physical tube alone gives the crude
coordinate bound \(CS\sqrt n\). Backward differentiation with this
bound and the forward physical speed implies
\[
 \max_{a,j}
 \frac{\|\dot k_a^j\|_2+\|\dot\delta_a^j\|_2}{\sqrt n}
 \le C(1+\sqrt n)\rho.
\]
Since \(\int_{T_n}^\infty\rho\le(S/2)e^{-\kappa T_n}\),
the coordinate variation is bounded by
\(CSn e^{-\kappa T_n}=o(S)\) if \(c_T\kappa>1\).
No carrier moment or finite-horizon maximum is assumed in this tail
estimate. This proves the all-time carrier conclusion conditional
only on the separately checked local input.

To verify Section 9, use the stronger deterministic tracking result
already established in DEPTH_TRACKING_ROUTE.md:
\[
 D_{n,q}\le
 \frac{CA_M[1+M+\sqrt{\log(e+q)}]}{q^2},
 \qquad q\ge C(1+M)A_M,\qquad A_M=Ce^{CM}.
\]
On the carrier event take \(M=1+CS\sqrt{\log(e+n)}\).
Then
\[
 q_n=\left\lceil n^{1/4}
              e^{A\sqrt{\log(e+n)}}\right\rceil
\]
with fixed sufficiently large \(A\) satisfies the absorption threshold
and gives \(D_{n,q_n}\le Cn^{-1/2}\).
The repaired source now states precisely this stronger deterministic bound
and names its checked study dependency.

The deterministic whole-input estimate then gives, for every fixed query
law \(\nu\) with finite second moment,
\[
 \left(\int\sup_{t\ge0}
       |\widehat f_{n,q_n}(t,x)-f_{n,D}(t,x)|^2\,d\nu(x)\right)^{1/2}
 \le C_\nu n^{-1/2}
\]
on events of probability tending to one. The same-width initialization,
canonical mobilities, and actual autonomous residual-RMS closure are
retained. The order is \(n^{1/4+o(1)}=o(n)\); with fixed data and depth,
the moving memory state is \(n^{5/4+o(1)}\).
Initialized dense matrices remain stored and applied exactly.

The result still assumes a positive initial feature-Gram gap and small
fixed labels. Algebraic criteria for particular activations or compatible
data quotients are separate checked inputs. Nothing in this probability
check alone proves an unbounded-activation local insertion lemma.

## 8. Final synthesis quantifiers and scope

Read the complete DEPTH_EXTENSION_RESULT.md at SHA256
6867c597f5efc368ba54b2ce9d810c653a54a2788ece2e748a8b8d98c487ce11,
and the complete DEPTH_TRACKING_CHECK.md including its simultaneous-order
corollary. **Verdict: PASS; no scope overreach found.**

The same dense carrier event and order-independent physical tube support
every positive integer \(q\). Above
\(q_0=C(1+M)A_M\), the deterministic source bound applies.
Below \(q_0\), its coarse physical bound \(D_{n,q}\le C\) is bounded
by \(C e^{K\sqrt{\log(e+n)}}\sqrt{\log(e+q)}/q^2\) after choosing
\(K\) large enough to dominate \(q_0^2\).
The polynomial factor \((1+M)^2\) is absorbed by a fixed enlargement
of \(K\). Thus the all-orders assertion uses one event and constants
independent of order.

For \(q_n=\lceil n^{1/4}e^{a\sqrt{\log(e+n)}}\rceil\),
\(a>K/2\), the remaining factor
\(\sqrt{\log(e+n)}e^{-(2a-K)\sqrt{\log(e+n)}}\) is bounded.
This proves strict \(C_\mu n^{-1/2}\) error in the stated query norm.
Finite second moment suffices, and the time supremum includes the fitted
endpoint. The compatible weighted quotients, derivative-only activation
class with its separate automatic-Gram conditions, fixed-depth and
small-label qualifications, and moving-state count all agree with the
checked sources. Events have probability tending to one at each width;
no simultaneous event for independently initialized widths is asserted.
