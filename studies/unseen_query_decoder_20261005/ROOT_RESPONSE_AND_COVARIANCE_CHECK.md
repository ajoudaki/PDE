# Independent check of Gaussian responses and covariance coupling

2026-10-06. Scoped mathematical audit of Sections 1–3 of
`ROOT_RESPONSE_AND_COVARIANCE.md`. No candidate edits, experiments,
external-paper review, promotion, or Git operations.

**Verdict:** Sections 1–3 pass this check within their stated partial-result
scope. The good-set vector extension and derivative-locality argument are
valid, the scalar Gaussian-divergence constants are correct, the covariance
coupling handles noncommuting and singular covariances correctly, and the
two-dimensional chronological-factor counterexample has the claimed rate.
The dense-path specialization is certified at every fixed **finite**
physical time. Derivative traces of fitted-limit vector fields at
$t=\infty$ would require an additional regularity argument; the present
check does not infer one from a uniform-in-time Lipschitz bound alone.

This verdict does not certify a compact trace evaluator, a growing causal
Gaussian program, a simultaneous sphere/time error bound, or the requested
compressed model. The candidate explicitly leaves those steps open.

## Frozen inputs and scope

Candidate SHA-256:

`2f9519eb0cda41b550c6e94d706f20481ca6c515d657b7ad57613359bb3bacc6`

Authorized dense source,
`studies/integrated_general_compression_20261004/GENERAL_DENSE_COMPARISON.md`,
SHA-256:

`ab97a860d7a6e175905a6848a9126ca8a194e08f52764738e94dcde2675100a9`

The candidate was read completely to identify the assigned claims and
their scope. Only Sections 1–3 are adjudicated here. The dense source had
been read completely under the standing assignment; its hash and the
specific good-pair estimates were checked again. The linked
`GROWING_PROGRAM_STABILITY.md` was not opened: the complete divergence
proof needed for this audit is in the candidate itself. The external-paper
screening in Section 4 is outside this assignment and was not verified.
No other route note, review report, other study, or archived book was read
for this check.

## 1. Vector extension and derivative locality

The claimed Euclidean extension is justified by the displayed finite-ball
argument. If the active gradients at a minimizer did not contain zero in
their convex hull, a separating direction would decrease all active
quadratics. The finite inactive collection remains below the maximum for
a sufficiently small step, contradicting minimality. Thus active weights
$\alpha_i\geq0$, $\sum_i\alpha_i=1$ exist with
$u=\sum_i\alpha_i u_i$. The two identities used in the candidate are

\[
 \sum_i\alpha_i\|u-u_i\|^2
   =\tfrac12\sum_{i,j}\alpha_i\alpha_j\|u_i-u_j\|^2,
\]
\[
 \sum_i\alpha_i\|x-x_i\|^2
   -\tfrac12\sum_{i,j}\alpha_i\alpha_j\|x_i-x_j\|^2
   =\left\|x-\sum_i\alpha_i x_i\right\|^2.
\]

They give a nonpositive minimum from the old Lipschitz inequalities,
so the finite balls intersect. Restricting to one compact ball supplies
the finite-intersection argument for an arbitrary old domain. Adding a
countable dense set and taking the continuous extension preserves all
old values. Projection onto the radius-$B\sqrt n$ Euclidean ball
preserves those values and the Lipschitz constant.

The Jacobian of each extended map has operator norm at most $A$ almost
everywhere and rank at most $n$, regardless of the dimension of the
complete Gaussian root. Hence

\[
 \|D_Gc\|_{\rm HS}^2,\ \|D_Gh\|_{\rm HS}^2\leq nA^2.
\]

There is no missing factor proportional to the $n^2$ matrix-root
coordinates in this step.

Derivative locality on the measurable good set $E$ is valid. In an open
neighborhood where an original field is smooth, its difference from the
extension is locally Lipschitz and vanishes on $E$. At a density point
of $E$ where that difference is differentiable, a nonzero derivative
would imply nonzero values in a cone of positive relative volume. This
contradicts density one. The weak derivatives therefore agree almost
everywhere on $E$, and Gaussian absolute continuity preserves that
statement. This is why no boundary derivative of an indicator of $E$
enters the proof.

## 2. Divergence identity, constants, and source specialization

For matrix-entry indices $p,q$, Gaussian integration by parts gives

\[
 \mathbb E[(M_pu-\partial_pu)(M_qv-\partial_qv)]
  =\mathbf1_{p=q}\mathbb E[uv]
    +\mathbb E[(\partial_qu)(\partial_pv)].
\]

One direct derivation applies the adjoint relation to the first factor,
then applies integration by parts in coordinate $q$ to the remaining
$M_q\partial_pv$ term; the mixed second derivatives cancel. Summing
over $p,q$ yields the candidate's identity for $\delta(U)$. The estimate

\[
 \sum_{p,q}(\partial_qU_p)(\partial_pU_q)
    \leq\sum_{p,q}|\partial_qU_p|^2
\]

follows by $2ab\leq a^2+b^2$ and exchanging $p,q$ in one sum.

For $U_{ij}=c_ih_j/n^{3/2}$, the bounds are exactly

\[
 \|U\|_2^2\leq B^4/n,
\]
\[
 \|D_MU\|_{\rm HS}^2
 \leq\frac{2\|h\|_2^2\|D_Mc\|_{\rm HS}^2
           +2\|c\|_2^2\|D_Mh\|_{\rm HS}^2}{n^3}
 \leq4B^2A^2/n.
\]

The independent auxiliary Gaussian roots cause no change: either use
integration by parts only in the matrix block, or condition on the
auxiliary coordinates and integrate the result. Bounded Lipschitz
extensions admit smooth approximations whose values and first weak
derivatives converge in the needed Gaussian $L^2$ spaces. Uniform
boundedness controls multiplication by $M$, and bounded derivatives
control the derivative terms. Thus the identity and inequality pass to
the nonsmooth extensions.

Markov's inequality for $\delta(U)^2$, followed by derivative locality,
gives precisely candidate equation (2):

\[
 \mathbb P\left(E\cap\left\{
  \left|\frac{c^TMh-\sum_{i,j}\partial_{M_{ij}}(c_ih_j)}{n^{3/2}}
       \right|>
  \frac{\sqrt{B^4+4B^2A^2}}{\sqrt{n\eta}}
                    \right\}\right)\leq\eta.
\]

The probability is not conditioned on $E$. An unconditional success
event for the actual fields loses $\mathbb P(E^c)+\eta$, as stated.

For the dense-path application, let $Y$ be label RMS and $M_n$ the
training-carrier cap. The source estimates give

\[
 D_h+D_w/Y\leq C e^{CYM_n}
                    \|G-\widetilde G\|_2/\sqrt n,
\]
\[
 \frac{\|h-\widetilde h\|_2}{\sqrt n}\leq CD_h,
 \qquad
 \frac{\|\delta-\widetilde\delta\|_2}{\sqrt n}
       \leq C[D_w+(Y+M_n)D_h].
\]

Thus the unnormalized vector Lipschitz constants can be chosen as

\[
 A_h\leq C e^{C\sqrt{\log(en)}},\qquad
 A_\delta\leq C(1+\sqrt{\log(en)})
                          e^{C\sqrt{\log(en)}}.
\]

All fixed label, data, depth, and gap dependence is absorbed into $C$.
The RMS bounds give a fixed $B$. The scalar response remainder therefore
has the claimed $n^{-1/2+o(1)}$ upper scale at fixed confidence, with no
history-covariance inverse. The initialized hidden block satisfies
$M=\sqrt nW_0$, so $c^TMh/n^{3/2}=c^TW_0h/n$; the normalization is
consistent with the source model.

For every finite specified time, local smooth dependence of the finite
ODE on its initial condition supplies the smooth original fields used
in the lemma. A fitted endpoint needs its own differentiability argument
or a carefully stated weak-derivative limit. The candidate does not
establish that additional assertion. Likewise, good-root Lipschitz
constants alone do not convert the scalar probability estimate into a
simultaneous bound over all queries and times. A union bound over
$n^c$ points would insert a factor $n^{c/2}$ in this particular
second-moment estimate. The candidate correctly records this limitation.

## 3. Singular and noncommuting covariance coupling

Work on the range of $Q=\mathbb E XX^T$. Every null vector of $Q$ has
$v^TX=0$ almost surely, so both the samples and $\widehat Q$ lie in
that range. The zero-rank case is trivial. On the positive-rank range,
define $R=Q^{-1/2}\widehat Q Q^{-1/2}$ and use

\[
 Q^{1/2}Z,\qquad Q^{1/2}R^{1/2}Z,
\]

with an independent standard Gaussian $Z$. The second covariance is
$Q^{1/2}RQ^{1/2}=\widehat Q$, without requiring $Q$ and $R$ to commute.
The conditional squared distance is

\[
 \operatorname{tr}[Q(R^{1/2}-I)^2].
\]

The scalar inequality $(\sqrt u-1)^2\leq(u-1)^2$ holds for every
$u\geq0$. Spectral calculus applies it to the same symmetric matrix
$R$, giving a positive-semidefinite difference. Its trace against
$Q\succeq0$ is nonnegative because
$\operatorname{tr}(QS)=\operatorname{tr}(Q^{1/2}SQ^{1/2})\geq0$
for $S\succeq0$. This explicitly validates the noncommuting step.

Writing $\Delta Q=\widehat Q-Q$ and cycling the trace gives

\[
 \operatorname{tr}[Q(R-I)^2]
       =\operatorname{tr}[\Delta Q Q^\dagger\Delta Q].
\]

Independent centered summands $X_iX_i^T-Q$ eliminate all cross-sample
terms. Expanding a remaining term gives

\[
 \mathbb E\operatorname{tr}[\Delta Q Q^\dagger\Delta Q]
 =\frac1n\left(
       \mathbb E[\|X\|_2^2X^TQ^\dagger X]-\operatorname{tr}Q
                   \right).
\]

Finally $\mathbb E[X^TQ^\dagger X]=\operatorname{rank}Q$ gives the
stated $B^2\operatorname{rank}(Q)/n$ bound. No positive lower bound
on nonzero eigenvalues was used. The mixed-fourth-moment qualification
for unbounded $X$ is also correct: its finiteness at each fixed width
does not imply a uniform bound over a width-dependent family.

This coupling can depend on the entire sample covariance. The result
does not preserve chronological innovations, and the candidate does
not claim that it does.

## 4. The chronological-factor counterexample

Put $p=1/n$, $\varepsilon=p^{1/4}$, and use the two values
$(\varepsilon,1)$ and $(1,0)$ with probabilities $1-p$ and $p$.
Direct multiplication gives

\[
 Q_{11}=(1-p)\sqrt p+p,\qquad
 \det Q=p(1-p),\qquad
 U_{22}^2=\frac{p(1-p)}{(1-p)\sqrt p+p}.
\]

For $p\leq1/4$, $1-p\geq\sqrt p$, which implies
$U_{22}^2\geq\tfrac12\sqrt p$. If no rare sample is observed,
$\widehat Q=(\varepsilon,1)^T(\varepsilon,1)$ and its upper
chronological factor is

\[
 \widehat U=\begin{pmatrix}\varepsilon&1\\0&0\end{pmatrix}.
\]

The event has probability $(1-1/n)^n\geq1/4$. For example,
$x\log(1-1/x)$ is increasing for $x>1$, since its derivative is
$z-\log(1+z)>0$ with $z=1/(x-1)$; evaluate at $x=2$.
Consequently

\[
 \|U-\widehat U\|_F\geq 2^{-1/2}n^{-1/4}
 \quad\text{with probability at least }1/4,
\]

and, more strongly,

\[
 \mathbb E\|U-\widehat U\|_F^2\geq\tfrac18n^{-1/2}.
\]

The same-innovation Gaussian coupling uses $U^TZ$ and
$\widehat U^TZ$, so its expected squared distance conditional on
the samples is precisely this squared Frobenius norm. The free coupling
from Section 2 has expected squared distance at most $4/n$, because
$\|X\|\leq\sqrt2$ and $\operatorname{rank}Q=2$. Thus the separation
of rates is valid in expectation as well as on the displayed event.

The ordering and the common-innovation rule are essential to this
conclusion. The example does not rule out a different ordering, an
unrestricted Gaussian coupling, or a network-specific stable causal
construction. It is a width-dependent iid source family, not an
admissible-network realization. The candidate states these scope limits
correctly.

## Check disposition

There is no required mathematical correction to Sections 1–3 within
the finite-time interpretation of the response specialization. The one
recommended clarification is to write “each specified finite physical
time” there, unless fitted-endpoint derivative regularity is separately
proved. The displayed covariance estimate and counterexample need no
change. No finding here upgrades the compact-decoder claim.

The rigorous-math and conjecture-audit instructions already read in this
task were applied. The canonical-notation skill remained unavailable
under the previously observed permission denial; the maintained notation
contract and supplied presentation instructions were used directly.
