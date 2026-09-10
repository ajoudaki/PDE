# Exact structure of the unresolved cubic sign

Author: `sign_structure`, 2026-09-10. This is a continuation of analytic
approach A after the user explicitly reopened the study. It changes neither
the network, the data nor the teacher. No training, quadrature, random
sampling or implementation-API calculation was performed for this note.
The statements below are analytic identities with proofs. They are not a
positive-sign certificate and have not yet received independent checking.

The main useful identity is (5): the sign is a particular alignment of two
hidden-parameter directions after the training-speed component is removed.
The harmonic reduction (9)--(13) identifies the desired coefficient with
one Fourier mode and makes the frozen comparison's teacher projection a
single initial-kernel harmonic. Symmetry and positive hidden energy alone
cannot determine that coefficient, as the explicit profiles in (14) show.

## 1. Frozen model and initialized notation

The study's exact model remains two tanh hidden layers, a linear scalar
readout, stored initialization variances `1,1/n,1/n^2`, mobilities `(n,1,n)`
and mean squared loss on the three angles `0,pi/5,-pi/5`. Write

\[
q=\frac{\sqrt5-1}{4},\qquad
(p_1,p_2,p_3)=\frac13(1,-q,-q),\qquad
e_\alpha=(\cos\alpha,\sin\alpha).
\]

The test probability measure is `dmu=dalpha/(2pi)` and its teacher is
`y(alpha)=cos(3 alpha)`. In the notation of CUBIC_DERIVATION,

\[
Z_\alpha=\xi\cdot e_\alpha,\quad h_\alpha=\tanh Z_\alpha,
\quad Y_\alpha=Wh_\alpha,\quad H_\alpha=\tanh Y_\alpha,
\quad S=\sum_a p_a H_a.
\]

`W` and `W*` are the actual two orientations of the initial Gaussian
connector action. Lower and upper fields belong to distinct probability
spaces `Omega_1` and `Omega_2`. All tangent norms and pairings below use
their stated population expectations; no unidentified row/column pairing
is introduced. Define

\[
B=E_2[S^2]>0,\qquad
T=\int y(\alpha)H_\alpha\,d\mu(\alpha),\qquad
b=E_2[ST].                                             \tag{1}
\]

`T` is an upper-population field, not physical time. It is bounded because
`|H_alpha|<=1` and the integral is a probability integral. The positivity
`b>0` is proved below rather than assumed.

## 2. A Hilbert-space identity retaining both hidden blocks

Use the real Hilbert space

\[
\mathscr H=L^2(\Omega_1;\mathbb R^2)
 \mathbin\oplus\operatorname{HS}
       (L^2(\Omega_1),L^2(\Omega_2)).
\]

For an upper-population field `v` in `L2`, let

\[
\mathscr V_\alpha(v)=
\left(
 e_\alpha\tanh'(Z_\alpha)
 W^*[v\tanh'(Y_\alpha)],\quad
 [v\tanh'(Y_\alpha)]\otimes h_\alpha
\right).                                                \tag{2}
\]

The first component is the first-weight direction and the second is a
Hilbert--Schmidt connector increment. A rank-one operator `u tensor h`
acts as `g -> u E_1[hg]`, and its Hilbert--Schmidt norm is `||u||_2||h||_2`.
This is exactly the population normalization corresponding to the finite
connector increment `u h^T/n` and its ordinary Frobenius norm.

The map in (2) is bounded and linear in `v`: bounded tanh and gates give
`||V_alpha(v)||_H <= (||W||_op^2+1)^(1/2)||v||_2` uniformly in alpha.
It is continuous in alpha for fixed `v`. To see this, the initial lower
field is continuous in every finite `Lp`; the upper field is continuous
in `L2` by boundedness of `W`. Bounded gates converge in probability, and
a bounded multiplier converging in probability times a fixed `L2` field
converges in `L2`, by truncating that fixed field. Apply this fact inside
`W*` first, and then to the lower gate, to obtain continuity of the first
component. The rank-one component is handled by its norm formula. These
bounds justify all Bochner integrals and interchanges below.

Set

\[
\mathscr P(v)=\sum_a p_a\mathscr V_a(v),\qquad
\mathscr M(v)=\int y(\alpha)\mathscr V_\alpha(v)\,d\mu(\alpha),
\qquad F=\mathscr P(S).
\]

Taking the two component pairings of (2) gives, exactly,

\[
\begin{split}
\langle\mathscr V_\alpha(v),\mathscr V_\gamma(w)\rangle
={}&G_{\alpha\gamma}E_1\!\left[
 \tanh'(Z_\alpha)\tanh'(Z_\gamma)
 W^*(v\tanh'(Y_\alpha))W^*(w\tanh'(Y_\gamma))\right]\\
&+Q_{\alpha\gamma}E_2\!\left[
 vw\tanh'(Y_\alpha)\tanh'(Y_\gamma)\right].
\end{split}                                               \tag{3}
\]

Thus the hidden energy in CUBIC_DERIVATION (9) is
`A=||F||_H^2`. In particular the exact reused-transpose response, including
its mean product, is present in the first term of (3).

Let `C_alpha` denote the contraction functional in CUBIC_DERIVATION (16).
Substitution into (3) yields

\[
\mathcal C_\alpha(U_\alpha)
 =\langle\mathscr V_\alpha(S),F\rangle,
\qquad
\sum_a p_a\mathcal C_a(H_\alpha\tanh'(Y_a))
 =\langle\mathscr P(H_\alpha),F\rangle.
\]

Both identities use the original `G` and `Q`; neither requires their
inverses. Inserting them into the established cubic formula gives

\[
J(\alpha)=4\langle\mathscr V_\alpha(S),F\rangle
       +\frac43\langle\mathscr P(H_\alpha),F\rangle.
                                                               \tag{4}
\]

The coefficients `4` and `4/3` retain, respectively, feature motion in
the prediction and the induced moving-readout term. They cannot be
replaced by equal coefficients. Integrating (4), and using
`beta=8||F||^2/(3B)` and `a(alpha)=2 E_2[S H_alpha]`, proves

\[
\boxed{\displaystyle
\chi=\frac83\left\langle F,
 3\mathscr M(S)+\mathscr P(T)-\frac{4b}{B}F\right\rangle.}
                                                               \tag{5}
\]

This is a sign-preserving equality, not a bound. For clarity, the factor
removed by the clock is `4 beta b=32||F||^2 b/(3B)` in the risk coefficient.

There is an equivalent orthogonalized form. Put `rho=b/B`,
`T_perp=T-rho S` and define the finite signed angle measure

\[
d\nu(\alpha)=y(\alpha)d\mu(\alpha)
                    -\rho\sum_a p_a\delta_{\alpha_a}(d\alpha).
\]

Then `E_2[S T_perp]=0`, and (5) becomes

\[
\chi=\frac83\left\langle F,
 3\int\mathscr V_\alpha(S)\,d\nu(\alpha)
                    +\mathscr P(T_\perp)\right\rangle.           \tag{6}
\]

The upper-population orthogonality does not make the second pairing zero:
`P` is a bounded linear map with its own Gram operator, and is not an
isometry. The signed measure in the first term is not nonnegative either.
Consequently positivity of `||F||^2`, positive gates, or positivity of the
kernel supplies no sign for (5) or (6). A bound for this particular
alignment, rather than a bound for hidden movement alone, is needed.

## 3. Exact Fourier reduction

The initial second-layer feature kernel is stationary:

\[
K(\alpha,\gamma)=E_2[H_\alpha H_\gamma]=k(\alpha-\gamma).
\]

Indeed rotational invariance of the two lower Gaussian roots makes the
first-feature covariance stationary. The centered Gaussian upper field
has that covariance, so its joint laws, and then the tanh feature kernel,
are stationary as well. Define its real Fourier eigenvalues

\[
\lambda_j=\int k(u)\cos(ju)\,d\mu(u),\qquad j\ge1.
\]

For `T_j=integral H_alpha cos(j alpha) dmu`, translation in the double
integral gives

\[
E_2[T_jH_\gamma]=\lambda_j\cos(j\gamma),\qquad
E_2[T_j^2]=\frac12\lambda_j.                             \tag{7}
\]

Thus `lambda_j>=0`. Odd activations give `H_(alpha+pi)=-H_alpha`
as an `L2` identity, so every even Fourier eigenvalue, including the
constant mode, vanishes. The cosine/sine projections are orthogonal under
stationarity. Their squared norms summed over modes are bounded by
`E H_0^2`; this follows by applying the finite trigonometric projection
inequality to each sample field and integrating. In particular
`sum_{j odd} lambda_j<infinity`. Convolution with the finite training
measure therefore has an absolutely convergent Fourier series.

For positive odd integers define

\[
u_j=1-2q\cos(j\pi/5),\qquad
1-2q\le u_j\le1+2q,
\qquad u_1=\frac12,\quad u_3=\frac{7-\sqrt5}{4}.           \tag{8}
\]

All these numbers are strictly positive. Reflection of the training
design gives `sum_a p_a sin(j alpha_a)=0`, while
`sum_a p_a cos(j alpha_a)=u_j/3`. Consequently

\[
a(\alpha)=\frac43\sum_{j\ge1,\ j\ {
odd}}\lambda_j u_j\cos(j\alpha),\qquad
B=\frac29\sum_{j\ge1,\ j\ {odd}}\lambda_j u_j^2,
\qquad b=\frac{\lambda_3u_3}{3}.                          \tag{9}
\]

The kernel Fourier coefficients have normalization `k(u)=2 sum lambda_j
cos(j u)`. Thus the `4/3` in (9) is required by the leading output
velocity `a=2 sum p K`. The last identity can also be read directly from
(7), because `T=T_3` and the teacher values at the three training angles
are exactly their labels. It follows that the entire frozen-clock
contribution to the cubic risk coefficient is

\[
2\int y(\alpha)\beta a(\alpha)\,d\mu
            =\frac{4\beta\lambda_3u_3}{3}.               \tag{10}
\]

Equation (10) can replace a whole-circle integration of the frozen
subtraction by a single initial-kernel harmonic. It does not remove the
need to certify that harmonic numerically if numerical values are used.

### Strict positivity of the initial third harmonic

This assertion does not require a numerical Gaussian moment. Let
`Q(alpha-gamma)=E_1[h_alpha h_gamma]` and let `lambda_3^(1)` be its
third Fourier eigenvalue. In polar coordinates, the lower roots have
radius `R`, a uniform independent angle `Theta`, and strictly positive
radial density on every open positive interval. Put

\[
c_3(r)=2\int\tanh(r\cos u)\cos(3u)\,d\mu(u).
\]

Taylor's theorem near zero, uniformly for `|cos u|<=1`, gives
`tanh(r cos u)=r cos u-r^3 cos^3 u/3+O(r^5)`. Integrating and using
`cos^3 u=(3 cos u+cos 3u)/4` gives
`c_3(r)=-r^3/12+O(r^5)`. Hence it is nonzero on a sufficiently small
positive radial interval. The third cosine projection of the lower
feature is `(c_3(R)/2) cos(3Theta)`, and (7) applied to `Q` yields

\[
\lambda_3^{(1)}=\frac14 E[c_3(R)^2]>0.
\]

Let `v=Q(0)>0` and `c=E[sech^2(sqrt(v)N)]>0`. Gaussian integration by
parts, including singular two-point covariances, gives
`E[H_alpha Y_gamma]=c Q(alpha-gamma)`. Define
`R_alpha=H_alpha-c Y_alpha`. This residual is orthogonal to every
`Y_gamma`; therefore the third cosine projection satisfies

\[
E[T_3^2]
 =c^2E\!\left[\left(\int Y_\alpha\cos(3\alpha)d\mu\right)^2\right]
  +E\!\left[\left(\int R_\alpha\cos(3\alpha)d\mu\right)^2\right].
\]

All integrals and pairings are justified by their uniform second moments.
The Gaussian integration-by-parts formula follows by writing the pair as
a linear image of independent standard Gaussian variables and integrating
their densities; the tanh and derivative bounds kill every boundary term.
Since the covariance of `Y` is `Q`, we obtain

\[
\lambda_3\ge c^2\lambda_3^{(1)}>0,
\qquad b=\lambda_3u_3/3>0.                              \tag{11}
\]

Thus every term subtracted in (10) is positive. This strengthens the
interpretation of the clock correction, not the sign of what remains.

## 4. What symmetry and matching can, and cannot, decide

Let `h(alpha)=J(alpha)-beta a(alpha)` be the matched cubic profile.
It is continuous, even, and satisfies `h(alpha+pi)=-h(alpha)`.
Antiperiodicity follows from oddness of the two activations and linear
readout for every fixed network parameter state. For reflection, change
the sign of the second lower Gaussian root and exchange the training
indices at `pi/5` and `-pi/5`; their labels and weights coincide. Every
expectation in the explicit formula for `J` is unchanged. The same holds
for `a`, which is already visible in (9). No assumption of isotropy of
the trained predictor beyond this surviving reflection is made.

Write the cosine coefficients as
`h_j=2 integral h(alpha) cos(j alpha) dmu`. Sine and even cosine
coefficients vanish. Orthogonality then gives exactly

\[
\chi=h_3.                                               \tag{12}
\]

The established matching identity `sum_a p_a h(alpha_a)=0` says

\[
h(0)-2q h(\pi/5)=0.
\]

For full rigor without an unproved assertion of pointwise Fourier-series
convergence, take the Fejer sums of this continuous periodic function.
Their kernel is nonnegative, has integral one, and outside any fixed
neighborhood of zero is bounded by a constant divided by the sum order.
Uniform continuity of `h`, splitting the convolution into that
neighborhood and its complement, proves uniform convergence. Evaluating
the matching functional on those finite sums therefore yields

\[
\lim_{N\to\infty}
\sum_{\substack{1\le j\le N\\j\ {odd}}}
 \left(1-\frac{j}{N+1}\right)u_j h_j=0.                  \tag{13}
\]

Since every `u_j>0`, a nonzero profile satisfying matching cannot have
all its nonzero cosine coefficients of the same sign. For example, if
all were nonnegative and some `h_j>0`, the displayed nonnegative sum
would eventually exceed `u_j h_j/2`, contradicting (13). The all-negative
case is identical after changing sign. If every coefficient vanishes,
the same Fejer argument gives `h=0`.

In particular, any positive third-harmonic correction must be accompanied
by a negative correction in at least one other odd harmonic. The frozen
initial velocity has nonnegative odd cosine coefficients by (9); the
matched feature correction changes their relative values. This is the
precise harmonic content of the comparison, not a claim that the first
harmonic necessarily supplies the compensating decrease.

To isolate the obstruction, the two trigonometric polynomials

\[
h_+(\alpha)=\cos(3\alpha)-2u_3\cos\alpha,
\qquad h_-(\alpha)=-h_+(\alpha)                           \tag{14}
\]

both obey evenness, antiperiodicity and exact training matching because
`u_3-2u_3u_1=0`. Their cubic risk coefficients are respectively `+1`
and `-1`. These are counterexamples only to an inference from symmetry
and matching. They are not claimed to be reachable cubic profiles of the
fixed tanh network and do not refute the desired positive theorem.

## 5. Status and read record

This continuation proves exact identities (5), (6), (9), (10), (12),
(13), and the strict initial harmonic bound (11), conditional only on
the initialized model and the already derived cubic formula. It supplies
no new positive-time population existence assertion. The remaining
obligation is the sign of the specific third coefficient in (12), or
equivalently the specific alignment in (5). The structural route has
not proved that sign and has not shown that a sign proof is impossible.
Its strongest contribution to a certification route is the exact
replacement (10) and the independent coefficient and normalization checks.

Read fully for this subtask: root AGENTS and research workflow; the study
README, RESULT and CUBIC_DERIVATION; docs README and NOTATION; the current
CONTINUATION_DISPOSITION; solve-math-rigorously and investigate-conjectures
skills, including research-contract, evidence-ledger, adversarial-audit
and proof-search-orchestration references. Complete operative initialized
Gaussian proofs read: global_nonlinear Sections 2--3 (181--500), the full
C.3 proof including its weighted correction (3443--3829), finite_dynamics
Sections 1--4 (1--227), and gaussian_calculus Sections 1--4 (1--262).
The C.1 statement and introductory dependency/scope correction were also
read. No claim in this note reopens C.1/C.2 or imports a new trajectory
estimate from an unread part of their proofs. The new argument starts
from the explicit initialized cubic coefficient read in full above.
No maintained implementation API was used.

Observed starting HEAD was `df1117948764a984e7fd2d28949a3c87bc284f84`.
Unrelated exporter and maintenance changes were present and preserved.
This author owns only this file and does not stage or commit anything.
