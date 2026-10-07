# Independent check of the fixed-order insertion remainder

2026-10-07. Verdict: **PASS as a conditional deterministic local lemma.**
The gradient estimate (15), the full insertion estimate (23), and their
displayed activation-depth exponents are valid under the candidate's local
hypotheses. The cutoff power is one in those estimates and at most three
in the additional forces (25)--(26). The complex statement requires the
additional strip condition (27). This check supplies no event probability,
uniform control-class construction, global continuation, or promotion.

## Frozen scope

The candidate read completely was `FIXED_ORDER_INSERTION_JETS.md`, SHA-256
`dcc9dad21a3141e5c2e2a1f4e81eb1cea43f14a7d552f680f137b0d71cc82f7f`.
The complete supporting inputs were exactly:

- `studies/unseen_query_decoder_20261005/EXPLICIT_FITTING_WIDTH.md`,
  `62d018c6448b0e6af6085827a856667ba58747810c6b284452dea21ce800919d`;
- `studies/dense_cutoff_population_rate_20261001/UNBOUNDED_INSERTION_CHECK.md`,
  `bec5707fccc99597570ce51c94d3a487fd0b1ede14578617275cb708fdd95578`;
- `studies/dense_cutoff_population_rate_20261001/DEPTH_CAVITY_ROUTE.md`,
  `e8f9f43c137a9c74b751cbd2e54cf5a2b13f090c560d912b4b17994c53bc1478`;
- `studies/dense_cutoff_population_rate_20261001/DEPTH_INSERTION_CHECK.md`,
  `77c51e725629e736a33c16dbe4ec179b5aa859b527539815f55422a818a1e977`;
- `studies/integrated_general_compression_20261004/UNBOUNDED_COMPRESSOR_BRIDGE.md`,
  `e018f0291b4456913a6541d5db7d90a678c4564928edcd5f47dd8c5326336f5d`.

Linked research files were not followed. No study README, study history,
other new review, archived book, or Git history was read. The
`solve-math-rigorously` and `explain-with-canonical-notation` skills and the
latter's neural-network reference were read and applied. This report is
the only write. There was no experiment, Git mutation, or candidate edit.

## Norms, first derivatives, and the available slack

The inherited setup has \(L\ge2\), \(\beta\ge10\), and unit training
inputs \(\|v_a\|_2=1\). In mobility coordinates

\[
\Theta=(A,H^{(2)},\ldots,H^{(L)},w),\qquad
H^{(j)}=\sqrt n W^{(j)},\qquad F_a=w^\top h_a^{(L)},
\]

the norm on parameters and ports is the ordinary Hilbert direct-sum norm:
Frobenius on matrices and Euclidean on vectors. It is not the normalized
parameter norm from the dense-fitting proof. The actual vector field is

\[
-\frac2m\sum_a r_a\nabla_\Theta F_a,\qquad
r_a=F_a/n-y_a.
\]

This verifies the factors of \(n\) in all parameter, port, and residual
derivatives. Rectangular deletion changes vector dimensions, while all
displayed factors \(1/\sqrt n\) and \(1/n\) remain unchanged.

Write \(s_0=N+u\), \(J=\beta^{10L}\), \(J_b=\beta^{20L}(1+M)\),
and \(A_f=\beta^{30L}\), with \(R,P\) as in candidate (4). The
assumption \(s_0\le\sqrt n\) increases each normalized operator norm by
at most one and bounds every port RMS by one. Consequently

\[
\frac{\|h^{(j)}\|_2}{\sqrt n}\le\beta^{3L},\quad
\frac{\|w\|_2}{\sqrt n}\le\beta^{4L},\quad
\frac{\|k^{(j)}\|_2}{\sqrt n}\le\beta^{7L},\quad
\frac{\|\delta^{(j)}\|_2}{\sqrt n}\le\beta^{8L}.
\]

These bounds follow from linear activation growth, not a coordinate bound
on activation values. The geometric propagation factor needed below obeys

\[
L(11\beta)^{L-1}\le\beta^{4L}.
\]

The forward derivative recurrence has a direct term at most

\[
\frac{\|h^{(j-1)}\|_2}{\sqrt n}\|U_{H^{(j)}}\|_F
+\|U_{e^{(j)}}\|_2
\]

and propagated term \(11\beta\|Dz^{(j-1)}[U]\|_2\). This proves
the stated bound \(J\). Summing the gradient and port blocks gives
\(\|DF_a\|_2\le\beta^{13L}\sqrt n\).

In the backward derivative, each forcing term is either

\[
\phi''\odot Dz[U]\odot k^0
\quad\text{or}\quad
U_H^\top\delta^0/\sqrt n.
\]

The first costs at most \(\beta JM\|U\|\), the second at most
\(\beta^{8L}\|U\|\). Propagation uses bounded mixers and slopes.
Thus \(J_b\) bounds both backward derivatives. It contains one carrier
factor, and no Euclidean-to-coordinate conversion involving \(\sqrt n\)
was used.

## Forward and backward nonlinear remainders

For an endpoint quantity \(g\), let

\[
g_{[1]}=Dg(X_a^0)(V_a+U_a),\qquad
E_g=g(X_a^0+V_a+U_a)-g(X_a^0)-g_{[1]}.
\]

The two linear-event bounds and the Euclidean bound on \(U_a\) give

\[
\|(z_{[1]})^{\odot2}\|_2
\le d_0N+2d_0Ju+J^2u^2\le3J^2R.
\]

This explicitly avoids a term \(Nu\) without a small coordinate factor.
No separate localization of \(U_a\) is needed.

Exact product subtraction gives

\[
E_{z^{(j)}}=W_1^{(j)}E_{h^{(j-1)}}
+\Delta H^{(j)}h_{[1]}^{(j-1)}/\sqrt n.
\]

The second term is at most \(JP\). Inserting \(z_0+z_{[1]}\) in the
activation difference gives

\[
\|E_h\|_2\le\beta\|E_z\|_2+
\frac\beta2\|(z_{[1]})^{\odot2}\|_2.
\]

The forcing coefficient is at most \(2\beta J^2\), and the propagation
factor above proves (10) with room below \(A_f\). In particular the
argument does not multiply an activation remainder by a derivative of
order increasing with depth.

The exact backward identities (11)--(12) also check. For their products,

\[
\|z_{[1]}\odot k_{[1]}\|_2\le3JJ_bR,
\qquad
\|E_z\odot k_{[1]}\|_2
\le A_f(R+P)(d_0+J_bu).
\]

The latter is at most \(2A_fJ_b(R+P)\), since \(u,d_0\le1\).
The reference-carrier term is at most

\[
M\left[\beta A_f(R+P)+\frac32\beta^2J^2R\right].
\]

Including the matrix cross term, an upper bound for the additive forcing
coefficient in the response recursion is

\[
\beta J_b+3\beta JJ_b+2\beta A_fJ_b+
M\beta A_f+\frac32M\beta^2J^2
\le\beta^{53L}(1+M).
\]

Geometric propagation gives response remainder at most
\(\beta^{57L}(1+M)(R+P)\); the extra mixer in the carrier identity is
still covered by candidate (13)'s \(\beta^{60L}\).

The hidden-gradient identity (14) is exact. Its three norm bounds are
respectively

\[
\beta^{63L}(1+M)(R+P),\qquad
JJ_bP,\qquad \beta^{38L}(R+P).
\]

The first-layer remainder is \(E_\delta v_a^\top\), and the readout
remainder is \(E_h\). The direct-sum block norm, even bounded by the
sum over \(L+1\) blocks, fits comfortably inside

\[
\beta^{70L}(1+M)(R+P).
\]

This reconstructs (15). The homogeneous backward propagation never
contains \(M\). All occurrences of a reference carrier are additive
forcing factors, which is why the cutoff exponent does not grow with
depth.

## Segment carriers and the adaptive residual

Applying the remainder bounds to each \(t(V_a+U_a)\), \(0\le t\le1\),
gives

\[
\|k_t\|_\infty
\le M+d_0+J_bu+\beta^{60L}(1+M)(R+P)
\le\beta^{62L}(1+M).
\]

The last step uses exactly \(u+R+P\le1\). This is a derived segment
bound; it does not assume that a coordinate stop is convex in parameter
space. The forward and gradient remainders themselves do not use this
extra restriction.

For unit augmented directions \(U,V\), the scalar Hessian has two
readout terms, the layerwise curvature terms, and the mixed-weight terms
with their \(1/\sqrt n\) factors. Its norm at carrier maximum \(M'\) is
bounded by

\[
2J+L\beta J^2M'+2L\beta^{8L}J
\le\beta^{24L}(1+M').
\]

Substituting the segment bound proves (17), since

\[
\beta^{24L}[1+\beta^{62L}(1+M)]
\le\beta^{87L}(1+M).
\]

The scalar residual Taylor remainder carries \(1/n\), whereas the
reference gradient carries \(\sqrt n\). Thus its product costs \(P\),
not \(s_0^2\). The residual-increment times gradient-increment product
also costs at most \(\beta^{100L}(1+M)P\). The candidate's exact product
identity includes both terms. Averaging \(r_a^0E_{g_a}\) uses
\(m^{-1}\sum_a|r_a^0|\le\rho_0\); the factor two in the vector field
is covered by (19)'s \(\beta^{110L}\). No frozen-residual substitution
has occurred.

## Reverse probes and the full estimate

The probe hypotheses must include the top lower-network carrier \(y_i\)
itself, as well as its backpropagated carriers. This is the interpretation
of the original probe event. For \(q=\sum_i y_i b_{a,i}\), they imply

\[
\|q\|_2\le Q=2r_{\rm del}\beta M,\qquad
\max_\ell\|k_{q,0}^{(\ell)}\|_\infty
\le p=r_{\rm del}\beta Md_0.
\]

Subtracting the probe recursions gives a changed-gate forcing at most
\(\beta pJs_0\) and a changed-mixer forcing bounded by
\(s_0/\sqrt n\) times a reference probe Euclidean norm. That norm is
at most \((11\beta)^LQ\). Propagating the differences through the
perturbed maps proves (20), with coefficient at most \(\beta^{20L}\).
This step does not require localization of the changed probe.

The segment probe coordinate maximum is at most

\[
p+\beta^{20L}(p+Q/\sqrt n)s_0.
\]

Inserting this in the lower-network Hessian, and retaining \(1/\sqrt n\)
in its mixed terms, proves the \(\beta^{50L}\) Hessian bound and (21).
Because \(s_0\ge1\),

\[
s_0+s_0^2\le2s_0^2,\qquad
s_0^2\le2(N^2+Nu+u^2).
\]

The reverse remainder therefore costs a fixed coefficient times

\[
\rho_0r_{\rm del}\beta M
\left[d_0(N^2+Nu+u^2)+P\right],
\]

with coefficient far below \(\beta^{120L}\). Its residual-adaptation
term is bounded by \(2\beta^{23L}QP\). Combining these terms with
(19) proves (23), including its factors \(1+r_{\rm del}\) and \(1+M\).
The forward-port derivative also contains both displayed terms at
candidate lines 406--408, including the rank-one residual contribution.

With the inherited \(N,d_0,u\) choices, the six powers in the candidate's
braces are correct. In particular the reverse leading term is
\(n^{-8/100}\), and the ordinary matrix-product scale is

\[
P=n^{-48/100}+2n^{-49/100}u+n^{-1/2}u^2.
\]

These are local width powers. They do not establish a probabilistic
bootstrap or a numerical width threshold by themselves.

## Learned directions and the top offset

The original column velocity costs at most
\(2\rho S\beta^{9L}(1+M)/\sqrt n\); the incoming row velocity costs
at most \(2\rho\beta^{4L}M/\sqrt n\). Integrating the stated
activity bound and multiplying by the actual controls proves (24).
No independence is used for these learned increments.

Here is an explicit verification of (25) which also fixes the meaning of
its residual factor. At fixed retained parameters let

\[
e_a^1=e_a^0+\zeta_a,\quad q_a^1=q_a^0+\chi_a,\quad
g_a^i=\nabla_\Theta F_a(\Theta,e_a^i),\quad
r_a^i=F_a(\Theta,e_a^i)/n-y_a,
\]

where \(q_a^0=\sum_i y_i b_{a,i}\), and put
\(\rho_1=(m^{-1}\sum_a|r_a^1|^2)^{1/2}\). The actual forward
port is above \(h_a^{(j-1)}\), so this lower feature derivative does not
change when that port is interpolated. The exact difference is

\[
\begin{split}
\mathcal V_1-\mathcal V_0=-\frac2m\sum_a\big[&
r_a^1\{g_a^1-g_a^0+Dh_a^{(j-1)\top}\chi_a\}\\
&+(r_a^1-r_a^0)
\{g_a^0+Dh_a^{(j-1)\top}q_a^0\}\big].
\end{split}
\]

On the stipulated segment,

\[
\|g_a^1-g_a^0\|_2\le\beta^{87L}(1+M)\|\zeta_a\|_2,
\quad
|r_a^1-r_a^0|\le\beta^{8L}\|\zeta_a\|_2/\sqrt n,
\]

and \(\|Dh_a^{(j-1)\top}q_a^0\|_2\le JQ\). Substituting
(24) gives (25) with \(\rho=\rho_1\), the actual endpoint residual
RMS. This proof needs neither a further coordinate bound on the learned
reverse correction nor an unstated bound on residuals all along the
port-interpolation segment. Writing this endpoint identity in the
candidate would clarify its brief differentiation argument; it requires
no change to the claim or hypotheses.

For top deletion, the joint coordinate cap gives
\(|d_a|\le r_{\rm del}\beta(1+M)^2/n\). Under the explicitly
stated current-row norm bound,
\(\|q_a\|_2\le3r_{\rm del}\beta M\). Multiplication by the
gradient and by the reverse term gives respectively bounds proportional
to

\[
\frac{r_{\rm del}\beta^{13L+1}(1+M)^2}{\sqrt n},
\qquad
\frac{3r_{\rm del}^2\beta^{10L+2}(1+M)^3}{n}.
\]

Including the vector-field factor two, both fit (26). The reverse-offset
product has been retained. The current-row condition and the segment
condition in (25) remain actual hypotheses, not consequences of a generic
coordinate cutoff alone.

## Complex extension and claim boundary

For complex parameters all transpose gradients are algebraic holomorphic
gradients; norms remain Hermitian Euclidean norms. The estimates above
use modulus inequalities, not positivity of a complex Gram matrix.

Assume the complex reference also obeys the reference norm and
linear-event hypotheses, with preactivation imaginary parts at most
\(7a/16\). On a first-exit prefix from the half-strip, the forward
proof uses only the same bounds on \(\phi'\) and \(\phi''\).
Condition (27) bounds both the actual preactivation displacement and the
auxiliary displacement to \(z_0+z_{[1]}\) by \(a/32\).
All such points therefore have imaginary parts at most \(15a/32\).
The scalar Taylor segments remain inside this convex smaller strip, which
strictly improves the first-exit boundary.

A Cauchy circle of radius \(a/64\) around any such point stays in
the half-strip, and hence

\[
|\phi'''|\le64\beta/a\le4\beta^2.
\]

Using \(\widetilde\beta=\beta^2\) makes
\(4\beta^2\le\widetilde\beta^2\), and also enlarges all the other
valid derivative and physical envelopes. The real argument then gives
the claimed coefficient \(\beta^{240L}\) in the complex version
of (23). The tighter original forward envelopes used to check (27)
remain valid because this step does not use the third derivative.

No hidden bounded-activation or nonlinear-error localization assumption
was found. The scope is nevertheless conditional: the coordinate event,
probe event, physical interpolation bounds, and complex strip margins
must actually be produced by any subsequent application. In particular
this check does not supply the control-net probabilities, common-cavity
moment errors, propagator constants, or finite-confidence budget-removal
estimate listed at the end of the candidate.
