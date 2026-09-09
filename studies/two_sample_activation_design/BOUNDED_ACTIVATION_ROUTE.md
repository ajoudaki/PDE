# Bounded activations, exact learned memories, and a coordinate obstruction

This is a new partial analysis for the exact original three-hidden-layer, two-sample raw gradient flow. It is not a global population-identification theorem. No experiment was run, and no preexisting manuscript was edited. The reference contract and the actual source/continuation formulas were read; historical review outcomes were not used as premises.

The relevant local sources are `studies/mean_field_peeling/two_sample_separated_angle_theorem/sources/CONTRACT.md`, `SYMMETRY_RADIAL_CLOCK.md`, `L3_LOCAL_COMPLETE_PROOF.md` (especially its bounded-activation local source proof), `NONLINEAR_RESPONSE_PERTURBATION.md`, and `PRIMAL_COMPARISON_AND_CONTINUATION_BRIDGE.md`. The mathematical arguments below are proved directly.

## 1. A genuinely moderate candidate and what can actually be proved

One structurally different candidate is

\[
\phi(z)=1+\tanh z.
\]

It has bounded value and first two derivatives, is strictly increasing, and is not selected close to an affine activation. Odd `tanh` is another candidate under the stipulated exclusion of both endpoint correlations. The results below apply to every bounded C2 activation with bounded first and second derivatives; they do not prove the desired global theorem for either candidate.

Write `M=||phi||_infinity`, `D=||phi'||_infinity`. The three population spaces are separate probability spaces, with `A:H1->H2`, `B:H2->H3`, and readout `C in H3`. As in the contract,

\[
\delta_a^3=C\phi'(z_a^3),\qquad
q_a^2=B^*\delta_a^3,\quad
\delta_a^2=\phi'(z_a^2)q_a^2,\qquad
q_a^1=A^*\delta_a^2.
\]

The raw physical updates are

\[
\dot C=-\sum_a r_a h_a^3,\quad
\dot B=-\sum_a r_a\delta_a^3\otimes h_a^2,\quad
\dot A=-\sum_a r_a\delta_a^2\otimes h_a^1.
\]

Let `J(t)=integral_0^t sum_a |r_a(s)| ds`. All the following statements hold on any interval on which a strong raw solution exists and the displayed integrals are defined. They therefore apply to genuine finite-dimensional gradient flow without assuming population construction, and conditionally to any already-constructed strong population path. For the population initialization, `C(0)=0`.

### Exact bounded-memory lemma

For every such path,

\[
\|C(t)\|_\infty\le M J(t),\qquad
\|\delta_a^3(t)\|_\infty\le DM J(t).                 \tag{1}
\]

The trained top increment has an integral kernel, between the separate populations, satisfying

\[
\|(B(t)-B_0)(\omega_3,\omega_2)\|_\infty
 \le \tfrac12 DM^2J(t)^2.                            \tag{2}
\]

Consequently the middle incoming field admits the *exact* decomposition

\[
q_a^2(t)=B_0^*\delta_a^3(t)+m_a^2(t),\qquad
\|m_a^2(t)\|_\infty
 \le\tfrac12 D^2M^3J(t)^3.                          \tag{3}
\]

The bottom incoming field likewise has an exact decomposition

\[
q_a^1(t)=A_0^*\delta_a^2(t)+m_a^1(t),                 \tag{4}
\]

where

\[
\|m_a^1(t)\|_\infty
\le M\int_0^t\sum_b |r_b(s)|
       \|\delta_b^2(s)\|_2\|\delta_a^2(t)\|_2\,ds.   \tag{5}
\]

In particular, if `sup_{a,s<=T} ||delta_a^2(s)||_2 <= N_T`, then

\[
\sup_{a,t\le T}\|m_a^1(t)\|_\infty\le M J(T)N_T^2.  \tag{6}
\]

Proof. Integrating the readout equation and using `|h|<=M` proves (1). The top increment kernel is

\[
(B(t)-B_0)(\omega_3,\omega_2)
=-\int_0^t\sum_b r_b(s)\delta_b^3(s,\omega_3)
                                  h_b^2(s,\omega_2)ds.
\]

Its absolute value is at most `DM^2 integral_0^t J(s) dJ(s)`, which equals the right side of (2). Applying its adjoint to `delta_a^3(t)` and using (1) proves (3). For the next increment, adjunction of its exact rank-one integral gives

\[
 m_a^1(t)=-\int_0^t\sum_b r_b(s)h_b^1(s)
                \langle\delta_b^2(s),\delta_a^2(t)\rangle_2 ds.
\]

Bound `h_b^1` by M and use Cauchy--Schwarz. This proves (5)-(6). No independence assumption, source-response approximation, or coordinate pairing occurs.

At finite width the same proof uses the kernel `n(B-B0)_{ij}` and normalized sums. A nonzero initial readout adds `||C0||_infinity` to (1) and the corresponding term `DM||C0||_infinity J(t)` to (2). The actual prescribed initial readout has coordinate supremum tending to zero in probability, since its entries have variance `n^-2`.

### Compact-time physical constants

For a true gradient flow the exact energy identity and initial loss E0 give

\[
\mathcal L(t)\le E_0,\qquad
J(T)\le 2\sqrt{E_0}\,T,
\qquad
\|\Theta(t)-\Theta(0)\|_{\rm raw}\le\sqrt{TE_0}.       \tag{7}
\]

The residual inequality uses `sum|r_a| <= sqrt(2) sqrt(r_1^2+r_2^2)=2sqrt(L)`. Thus all constants in (1)-(6) are finite on every finite physical interval, independently of input separation. For example, when `||B0||op<=b0`,

\[
\|\delta_a^2(t)\|_2
\le D\|B(t)\|_{\rm op}\|\delta_a^3(t)\|_2
\le D^2M(b_0+\sqrt{TE_0})J(T),                       \tag{8}
\]

which supplies an explicit N_T in (6).

This is stronger trajectory information than a raw Hilbert ball: the actual learned top kernel is bounded pointwise, and both learned reverse-memory terms are bounded pointwise. It places all remaining possible reverse-field concentration in the two reused frozen Gaussian actions `B0*delta3` and `A0*delta2`. The physical residuals were retained in every step. It does not give approximate energy for a nongradient backward-cap flow automatically.

## 2. Why bounded inputs to a reused Gaussian matrix are not enough

There is an exact obstruction to inferring tails for `B0*delta3` merely from bounded delta3 and a bounded Gaussian operator norm.

Let `W_n` have independent N(0,1/n) entries and choose J uniformly from `{1,...,n}`, independently. Set

\[
 v_i=\operatorname{sign}(W_{iJ}),\qquad q=W_n^T v.
\]

Then `||v||infinity=1`, but

\[
q_J=\sum_i|W_{iJ}|,\qquad
\frac{q_J}{\sqrt n}\longrightarrow\sqrt{2/\pi}
\quad\hbox{in probability}.                          \tag{9}
\]

Indeed, condition on J and apply the weak law to the independent absolute standard normal variables `sqrt(n)|W_iJ|`. Therefore, for every fixed u,

\[
\liminf_{n\to\infty}\frac1n\sum_j q_j^2
          \mathbf1_{\{|q_j|>u\}}\ge 2/\pi
\quad\hbox{in probability}.                          \tag{10}
\]

A precise reading of (10) is that, for each eta>0, the probability that its left finite-n expression exceeds `2/pi-eta` tends to one. The single selected coordinate proves this. The arrays can be made exchangeable under input- and output-coordinate permutations: J is uniform and the definition uses only signs of its selected column. Thus coordinate exchangeability does not repair the conclusion. The Gaussian matrix operator norm still has its ordinary bounded high-probability behavior, and `||q||_n<=||W_n||op`; there is no contradiction with L2 control.

This is not a counterexample to the neural dynamics. The selected-column input is not asserted to be produced by the actual smooth finite-time training program. It is a rigorous obstruction to a proposed general lemma that would ignore adaptedness, causal source response, or the special origin of delta3. Adding any uniformly bounded memory to q leaves the concentrated coordinate contribution nonvanishing. Therefore (1)-(8), although useful, do not by themselves identify the population or remove backward caps.

## 3. A two-input obstruction to the one-input change of variables

The bounded-arctangent one-input local source proof simplifies the first-layer differential equation using `F'=1/phi'`; the transformed first field then has no `phi'' q` in its vector field. That cancellation does not extend to genuinely correlated two-input raw training by any C2 point-coordinate diffeomorphism that would remove both arbitrary incoming controls.

Assume `beta=phi'>0`, `|rho|<1`, and write

\[
\Gamma=\begin{pmatrix}1&\rho\\\rho&1\end{pmatrix},\qquad
\dot z=\Gamma\begin{pmatrix}\beta(z_1)u_1\\\beta(z_2)u_2\end{pmatrix}.
\]

The controls contain the actual residual/backward factors; this statement concerns simultaneous simplification for all possible controls. Define

\[
X_1(z)=\beta(z_1)\Gamma e_1,\qquad
X_2(z)=\beta(z_2)\Gamma e_2.
\]

If `rho != 0`, a C2 diffeomorphism that sends both vector fields to constant vector fields exists on all of R2 only when phi is affine. In fact the bracket is

\[
[X_1,X_2]
=\rho\beta(z_1)\beta'(z_2)\Gamma e_2
 -\rho\beta(z_2)\beta'(z_1)\Gamma e_1.                \tag{11}
\]

To prove the necessity without invoking an external differential-geometric theorem, suppose `DF X_b=c_b` are constant. Differentiate `DF X_2=c_2` in direction X_1, differentiate `DF X_1=c_1` in direction X_2, and subtract. The symmetric second derivatives of F cancel, leaving `DF [X_1,X_2]=0`. Invertibility gives a zero bracket. The two columns of Gamma are independent; `rho!=0` and positive beta therefore force `beta'(z_1)=beta'(z_2)=0` for every pair z. Thus beta is constant. Conversely affine phi already has constant vector fields.

When rho=0, the componentwise coordinate `F_a(z)=integral_0^{z_a} du/beta(u)` does straighten both fields wherever it is a diffeomorphism; bounded positive beta ensures its image is all R for each component. For nonzero rho the same attempted coordinate gives off-diagonal factors `rho beta(z_b)/beta(z_a)`, so the curvature-dependent response has merely moved into those factors.

This is a route obstruction, not a statement that a two-sample theorem is false. It excludes a tempting exact gauge reduction as a way to make a moderately nonlinear two-sample raw flow affine in its arbitrary incoming controls. Replacing Gamma by the identity would change the original metric and is not authorized. The interval `|rho|<=1-delta` contains nonzero correlations, so the orthogonal special case alone cannot discharge the target.

## 4. What survives and what is still missing

The bounded-activation class has a concrete structural advantage over the near-affine unbounded-value class: the readout, top trained kernel, and learned reverse-memory terms admit the exact finite-horizon bounds above without any small nonlinear amplitude. This is a reasonable nonperturbative class to investigate while preserving initialization, all trained layers, and the raw metric.

The new sufficient missing lemma is now sharply localized: exploit the actual causal neural origin of delta3 and delta2 to obtain cap-independent tails or an adequate stability modulus for the two *reused initial Gaussian adjoint actions*. Boundedness, energy, action norm, and exchangeability alone cannot imply that lemma, by (9)-(10). The original source coefficients are one possible language for this missing causal control, but their global closure has not been proved here. The existing near-affine source-response smallness cannot simply be deleted.

A successful proof must additionally remove caps for a stopped physical construction, recover enough approximate energy to remove the stop, identify both orientations of the Gaussian actions, and verify the exact raw-GD and hidden-velocity bridges. The existing finite-program/common-action machinery is a dependency for those steps, not an already-discharged conclusion for tanh. No practical positive epsilon(delta), global uniqueness, reached-state continuation, or population/raw-GD identification has been proved in this note.
